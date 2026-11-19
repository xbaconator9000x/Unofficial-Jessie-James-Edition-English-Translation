# Publishing a release

The English translation and Spanish quality of life edition use independent release manifests (`releases.json` and `spanish-releases.json`). Both require the original Spanish FINAL v1.1 ROM (16 MiB, CRC32 `805E24CA`). Never mix the two editions' update routes.

## Current release

| Edition | Version | Output ROM CRC32 | Full patch |
| --- | --- | --- | --- |
| English | 1.0 | C043455C | jessie-james-english-v1.0-c043455c.bps |
| Spanish QoL | 1.0 | 7C042814 | jessie-james-spanish-qol-v1.0-7c042814.bps |

The manifests are authoritative for patch filenames, sizes, CRC32 and SHA-256 fingerprints. GitHub Pages publishes the latest verified full patches at the stable download URLs as well.

## Update procedure

- Generate a full BPS against the exact original ROM for each edition being updated.
- Verify the patched ROM byte-for-byte against the intended output.
- Update the appropriate manifest with the target ROM fingerprint, patch filename, size, CRC32 and SHA-256.
- For a new numbered release, update the version and changelog, and provide verified incremental update paths from supported earlier releases.
- For a same-version correction to v1.0, retain the version and original release date. The current manifests accept the original ROM and recognise the latest patched output. Earlier v1.0 builds require reapplying the full patch to the original ROM.
- Update the README checksums and run `node tests/bps.test.mjs` and `node tests/edition-routes.test.mjs`.

GitHub Pages validates the release manifests, BPS files and gallery assets before deployment. Only patches are distributed, not complete ROMs or save files. Save compatibility and gameplay behaviour require separate in-game testing; the patcher does not modify save files.
