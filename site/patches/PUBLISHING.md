# Publishing a release

The English translation and Spanish quality of life edition use independent release manifests (`releases.json` and `spanish-releases.json`). Both require the original Spanish FINAL v1.1 ROM (16 MiB, CRC32 `805E24CA`). Never mix the two editions' update routes.

## Current release

| Edition | Version | Output ROM CRC32 | Full patch |
| --- | --- | --- | --- |
| English | 1.03.2 | 5DAE93EA | jessie-james-english-v1.03.2-5dae93ea.bps |
| Spanish QoL | 1.03 | 222A0072 | jessie-james-spanish-qol-v1.03-222a0072.bps |

The v1.03.2 English full BPS is composed from the verified v1.03 full BPS and the 51-byte source-locked crash-sweep update (CRC32 `6E1E5095` → `5DAE93EA`) during Pages deployment. The v1.03 full BPS files are assembled during Pages deployment from previously verified v1.02 full patches and source-locked incremental updates by `assemble_release.py`, without using or publishing a ROM. All prior v1.02 ROM builds remain recognised for automatic upgrading. The new v1.03 deltas are checked in as compressed BPS streams, and the resulting ROM images were verified offline against the original ROM and the uploaded RC127/ES95 patch outputs. The manifests are authoritative for patch filenames, sizes, CRC32 and SHA-256 fingerprints. English v1.03 and the earlier Aqua ship hotfix can be upgraded with the English patcher. The patcher changes the ROM file, not the save; back up both before updating. GitHub Pages publishes the latest verified full patches at the stable download URLs as well.

## Update procedure

- Generate a full BPS against the exact original ROM for each edition being updated, or assemble an equivalent full BPS with the verified source-independent composer.
- Verify the patched ROM byte-for-byte against the intended output.
- Update the appropriate manifest with the target ROM fingerprint, patch filename, size, CRC32 and SHA-256.
- For a new numbered release, update the version and changelog. For a same-version correction, retain the version and original release date.
- Maintain independently verified incremental BPS update paths for supported earlier releases. Record the exact source and target ROM fingerprints and the patch integrity values in the relevant manifest. Unsupported builds require the full patch applied to the original ROM.
- Update the README checksums and run `node tests/bps.test.mjs` and `node tests/edition-routes.test.mjs`.

GitHub Pages validates the release manifests, BPS files and gallery assets before deployment. Only patches are distributed, not complete ROMs or save files. Save compatibility and gameplay behaviour require separate in-game testing; the patcher does not modify save files.
