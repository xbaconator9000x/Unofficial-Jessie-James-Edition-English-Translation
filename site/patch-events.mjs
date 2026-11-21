// Patch telemetry is intentionally aggregate-only. No ROM bytes, checksums,
// filenames, input versions, saves, or visitor identifiers are passed to analytics.
// This is optional: the patcher works normally if the provider is unavailable.
export const PATCH_EVENTS = Object.freeze({
  englishRom: "english-rom-download-started",
  spanishRom: "spanish-rom-download-started",
  englishBps: "english-bps-download-started",
  spanishBps: "spanish-bps-download-started"
});

const LABELS = Object.freeze({
  [PATCH_EVENTS.englishRom]: "English ROM verified and save initiated",
  [PATCH_EVENTS.spanishRom]: "Spanish QoL ROM verified and save initiated",
  [PATCH_EVENTS.englishBps]: "English BPS verified and download initiated",
  [PATCH_EVENTS.spanishBps]: "Spanish QoL BPS verified and download initiated"
});

/**
 * Counts a verified output/save initiation, NOT a guaranteed file write on disk
 * or successful gameplay. Silently fails closed when analytics is not enabled.
 */
export function trackPatcherEvent(name) {
  if (!Object.prototype.hasOwnProperty.call(LABELS, name)) return false;
  try {
    const counter = globalThis.goatcounter;
    if (typeof counter?.count !== "function") return false;
    counter.count({path: name, title: LABELS[name], event: true, no_session: true});
    return true;
  } catch {
    return false; // Analytics must never interfere with verified patching.
  }
}
