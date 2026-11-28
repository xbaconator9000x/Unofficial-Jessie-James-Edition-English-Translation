import assert from "node:assert/strict";
import {trackPatcherEvent, PATCH_EVENTS} from "../site/patch-events.mjs";

const previous = globalThis.goatcounter;
try {
  delete globalThis.goatcounter;
  assert.equal(trackPatcherEvent(PATCH_EVENTS.englishRom), false, "no configured backend");
  const calls = [];
  globalThis.goatcounter = {count: event => calls.push(event)};
  for (const key of Object.values(PATCH_EVENTS)) {
    assert.equal(trackPatcherEvent(key), true);
  }
  assert.equal(calls.length, 6);
  assert.deepEqual(calls.map(e => e.path), Object.values(PATCH_EVENTS));
  for (const call of calls) {
    assert.equal(call.event, true);
    assert.equal(call.no_session, true);
    assert.deepEqual(Object.keys(call).sort(), ["event","no_session","path","title"]);
  }
  assert.equal(trackPatcherEvent("fake-custom-event"), false, "reject unknown event names");
  assert.equal(trackPatcherEvent("rom-hash=private"), false, "reject dynamic identifiers");
  assert.equal(calls.length, 6, "invalid events must not be transmitted");
  globalThis.goatcounter = {count: () => {throw new Error("tracker blocked");}};
  assert.equal(trackPatcherEvent(PATCH_EVENTS.englishRom), false, "tracker failures cannot break patcher");
  console.log("PASS: exact patch event names, privacy allowlist, no-backend and failure behavior");
} finally {
  if (previous === undefined) delete globalThis.goatcounter;
  else globalThis.goatcounter = previous;
}
