# Publishing a release

The English translation and Spanish quality of life edition use independent release manifests (`releases.json` and `spanish-releases.json`). Both require the original Spanish FINAL v1.1 ROM (16 MiB, CRC32 `805E24CA`). Never mix the two editions' update routes.

## Current release

| Edition | Version | Output ROM CRC32 | Full patch |
| --- | --- | --- | --- |
| English | 1.02 | CADC8480 | jessie-james-english-v1.02-cadc8480.bps |
| Spanish QoL | 1.02 | 0486144D | jessie-james-spanish-qol-v1.02-0486144d.bps |

The v1.02 full BPS files are assembled during Pages deployment from the previously published full patches and the small, source-locked v1.02 updates by `assemble_release.py`, without using or publishing a ROM. The outputs were verified offline against the owned original ROM to match both uploaded v1.02 target ROMs byte-for-byte. The manifests are authoritative for patch filenames, sizes, CRC32 and SHA-256 fingerprints. GitHub Pages publishes the latest verified full patches at the stable download URLs as well.

## Update procedure

- Generate a full BPS against the exact original ROM for each edition being updated, or assemble an equivalent full BPS with the verified source-independent composer.
- Verify the patched ROM byte-for-byte against the intended output.
- Update the appropriate manifest with the target ROM fingerprint, patch filename, size, CRC32 and SHA-256.
- For a new numbered release, update the version and changelog. For a same-version correction, retain the version and original release date.
- Maintain independently verified incremental BPS update paths for supported earlier releases. Record the exact source and target ROM fingerprints and the patch integrity values in the relevant manifest. Unsupported builds require the full patch applied to the original ROM.
- Update the README checksums and run `node tests/bps.test.mjs` and `node tests/edition-routes.test.mjs`.

GitHub Pages validates the release manifests, BPS files and gallery assets before deployment. Only patches are distributed, not complete ROMs or save files. Save compatibility and gameplay behaviour require separate in-game testing; the patcher does not modify save files.
