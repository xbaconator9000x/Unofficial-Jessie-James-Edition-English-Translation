"use strict";
(() => {
  // The supplied Option B MP3 is a General MIDI preview, not a GBA voicebank render.
  // Its source MIDI contains markers at 7.993508 and 30.523148 seconds.
  const INTRO_END = 7.993508;
  const LOOP_END = 30.523148;
  const button = document.getElementById("music-toggle");
  if (!button) return;
  const AudioContextType = window.AudioContext || window.webkitAudioContext;
  if (!AudioContextType) {
    button.disabled = true;

    return;
  }

  let context;
  let audioBuffer;
  let activeSource = null;
  let playbackStartedAt = 0;
  let playbackOffset = 0;
  let loading = null;

  function positionAt(seconds) {
    if (seconds < LOOP_END) return seconds;
    return INTRO_END + (seconds - LOOP_END) % (LOOP_END - INTRO_END);
  }

  async function load() {
    context ||= new AudioContextType();
    await context.resume();
    if (audioBuffer) return;
    loading ||= (async () => {
      const response = await fetch("title-motto-loop.mp3");
      if (!response.ok) throw new Error("Couldn't load the theme.");
      const data = await response.arrayBuffer();
      const decoded = await context.decodeAudioData(data);
      if (decoded.duration < LOOP_END - 0.2) throw new Error("Audio file is incomplete.");
      audioBuffer = decoded;
    })();
    try { await loading; } catch (error) { loading = null; throw error; }
  }

  function pause() {
    if (!activeSource) return;
    playbackOffset = positionAt(context.currentTime - playbackStartedAt);
    const previous = activeSource;
    activeSource = null;
    previous.stop();
    previous.disconnect();
    button.textContent = "♪ Play theme";
    button.setAttribute("aria-pressed", "false");

  }

  async function play() {
    button.disabled = true;

    try {
      await load();
      const source = context.createBufferSource();
      source.buffer = audioBuffer;
      source.loop = true;
      source.loopStart = INTRO_END;
      source.loopEnd = LOOP_END;
      source.connect(context.destination);
      playbackStartedAt = context.currentTime - playbackOffset;
      source.start(0, playbackOffset);
      activeSource = source;
      button.textContent = "Ⅱ Pause theme";
      button.setAttribute("aria-pressed", "true");

    } catch (error) {

      button.textContent = "♪ Theme unavailable";
      console.warn("Title music unavailable:", error);
    } finally {
      button.disabled = false;
    }
  }

  button.addEventListener("click", () => {
    if (activeSource) pause();
    else void play();
  });
  document.addEventListener("visibilitychange", () => {
    if (document.hidden) pause();
  });
})();
