function crc32(bytes){let crc=0xffffffff;for(const b of bytes){crc^=b;for(let j=0;j<8;j++)crc=(crc>>>1)^((crc&1)?0xedb88320:0);}return (crc^0xffffffff)>>>0;}

function hex(n){return (n>>>0).toString(16).toUpperCase().padStart(8,"0");}

function inspectBps(p){
  if(p.length<19||p[0]!==66||p[1]!==80||p[2]!==83||p[3]!==49)throw Error("Not a BPS patch.");
  if(p.length>64*1024*1024)throw Error("Patch is too large.");
  const end=p.length-12, dv=new DataView(p.buffer,p.byteOffset,p.byteLength);
  const sourceCrc=dv.getUint32(end,true),targetCrc=dv.getUint32(end+4,true),patchCrc=dv.getUint32(end+8,true);
  if(crc32(p.subarray(0,p.length-4))!==patchCrc)throw Error("Patch checksum mismatch. Download it again.");
  let pos=4;function num(){let value=0,shift=1;for(let i=0;i<8;i++){if(pos>=end)throw Error("Truncated patch.");const b=p[pos++];value+=(b&127)*shift;if(!Number.isSafeInteger(value))throw Error("Invalid patch number.");if(b&128)return value;shift*=128;value+=shift;}throw Error("Invalid patch number.");}
  const sourceSize=num(),targetSize=num(),meta=num();if(sourceSize<1||targetSize<1||sourceSize>64*1024*1024||targetSize>64*1024*1024||meta>end-pos)throw Error("Invalid patch size or metadata.");pos+=meta;
  return {sourceSize,targetSize,sourceCrc,targetCrc,patchCrc,end,num,get pos(){return pos},read(n){if(n>end-pos)throw Error("Truncated patch data.");const bytes=p.subarray(pos,pos+n);pos+=n;return bytes;}};
}

function applyBps(source,patch){
  const h=inspectBps(patch);
  if(source.length!==h.sourceSize)throw Error("Wrong ROM size. Expected "+h.sourceSize+" bytes; received "+source.length+".");
  if(crc32(source)!==h.sourceCrc)throw Error("Wrong ROM checksum. Expected "+hex(h.sourceCrc)+".");
  const out=new Uint8Array(h.targetSize);let o=0,s=0,t=0;
  const relative=()=>{const v=h.num();return (v%2?-1:1)*Math.floor(v/2);};
  while(o<out.length){const op=h.num(),kind=op%4,len=Math.floor(op/4)+1;if(len>out.length-o)throw Error("Patch writes beyond output.");
    if(kind===0){if(o+len>source.length)throw Error("Source read out of range.");out.set(source.subarray(o,o+len),o);}
    if(kind===1)out.set(h.read(len),o);
    if(kind===2){s+=relative();if(s<0||s+len>source.length)throw Error("Source copy out of range.");out.set(source.subarray(s,s+len),o);s+=len;}
    if(kind===3){t+=relative();if(t<0||t>=o)throw Error("Target copy out of range.");for(let j=0;j<len;j++)out[o+j]=out[t++];}
    o+=len;
  }
  if(h.pos!==h.end)throw Error("Unexpected trailing patch instructions.");
  if(crc32(out)!==h.targetCrc)throw Error("Output checksum mismatch. No ROM was produced.");
  return out;
}

function identify(bytes){return bytes.length+":"+hex(crc32(bytes));}

function findRoute(edges,start,target){
  const queue=[[start,[]]],seen=new Set([start]);for(let i=0;i<queue.length;i++){const [key,path]=queue[i];if(key===target)return path;for(const edge of edges){if(edge.from===key&&!seen.has(edge.to)){seen.add(edge.to);queue.push([edge.to,path.concat(edge)]);}}}return null;
}

function validateEdge(bytes,edge){const h=inspectBps(bytes);if(h.sourceSize+":"+hex(h.sourceCrc)!==edge.from||h.targetSize+":"+hex(h.targetCrc)!==edge.to||hex(h.patchCrc)!==edge.crc||bytes.length!==edge.bytes)throw Error("Patch does not match the release manifest.");return h;}
export {crc32,hex,inspectBps,applyBps,identify,findRoute,validateEdge};
