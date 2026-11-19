# Publishing an update

Keep each previous BPS unchanged. For each new English version, generate a BPS from the exact original Spanish ROM to the new ROM and an incremental BPS from the preceding English ROM to the new ROM. Keep every intervening update edge so the browser can upgrade older English ROMs automatically. A matching size and CRC32 identify each ROM; every patch also has its own CRC32, size and SHA-256. Record those values in releases.json, including the source and output ROM SHA-256 fingerprints in romSha256. Update the target, latest version, versions dictionary and changelog. Only replace a published BPS for an explicitly approved same-version correction. Keep the earlier ROM fingerprint and an independently verified incremental patch to the corrected build; do not change the public version or changelog.

Before publishing verify both clean- and incremental-patch outputs byte-for-byte, including the final output checksum. Back up saves and separately test in-game save compatibility. The patcher does not modify save files.

For v1.0, place the supplied verified BPS at site/patches/jessie-james-english-v1.0.bps. Its SHA-256 is df832fba47d571295b56d92480bab9462e39725e4fa98c8d0f723be3c2190263. The earlier English v1.0 ROM is supported through jessie-james-english-v1.0-hotswap.bps (SHA-256 b6f0f9eb81ecc509a82cf2359af8be382593130561ec2771c1be5f7533e5c3b7). The site refuses mismatches. The second same-version correction upgrades CRC32 610FFD7B to 6C2FC9B2 using jessie-james-english-v1.0-hotswap-2.bps (SHA-256 a3b62df69cd1d8efea6ae89d217ef6183fda318bf0bc1e6beb10741fe425e518). All required patches must be present and verified before deployment.

Run node tests/bps.test.mjs before publishing. GitHub Pages also checks the manifest and every hosted BPS before deploying.

## Independent Spanish QoL edition

The English release manifest remains separate from spanish-releases.json. Do not add the Spanish QoL target to the English update graph or vice versa. Both start from the exact original Spanish FINAL v1.1 ROM. The Spanish patch is jessie-james-spanish-qol-v1.0.bps, SHA-256 6763fe3cb2566fd1725ab2725d22cca5942a3d48f172655f12d801b0dabda43d. Its target CRC32 is 79880DD1. The English v1.0 replacement is jessie-james-english-v1.0-3e48128c.bps, SHA-256 c60e05f88e388149826d58a801069020eae1a8ac927bfa11cb76668db3d3e32a, with the additional update edge jessie-james-english-v1.0-hotswap-3.bps. GitHub Pages publishes the validated current full English BPS at the stable original download URL as well. The English changelog is unchanged.

## Same-version crash correction and English gallery

Both editions remain v1.0. Current English target 15810EE0, Spanish QoL target 343C20A7. The manifests are authoritative for current patch names and checksums; the published canonical download URLs serve the latest verified full patch in each edition. Keep earlier update edges. The three gallery assets are required and checksum-verified before deployment.

English v1.0 same-version replacement: target D8616D2C, with incremental edge 15810EE0 to D8616D2C. See releases.json for current fingerprints. Spanish QoL remains unchanged.

Same-version EXP. ALL update: English target E1DDF011, Spanish QoL target 252AE8A8. The supplied Spanish BPS targeted vanilla Spanish FINAL v1.1 and contained 951 changed bytes, none overlapping the previous Spanish QoL build's 268,779 changed bytes. The new Spanish full patch preserves all earlier QoL edits and adds the supplied changes; full and incremental outputs were verified byte-for-byte. Gameplay behavior and save compatibility remain unverified. See manifests for authoritative checksums.

Same-version replacement: English target 532F1751 (77 bytes different from the preceding build), Spanish QoL target E67818B3 (53 bytes different). The complete supplied patches are preserved byte-for-byte. Both incremental patches were applied to the previous exact ROM and verified against the new output. Gameplay behavior and save compatibility remain unverified.

Same-version replacement: English target 01EB7D14, Spanish QoL target B4BC72F6. Each differs from the preceding build by 416 bytes; zero previously changed bytes reverted to the original ROM. The supplied full patches are preserved byte-for-byte. Both incremental patches were applied to the previous exact ROM and verified against the new output. Gameplay behavior and save compatibility remain unverified.

Same-version replacement: English target 91D1183A (109 bytes changed, including 66 restored to original ROM values), Spanish QoL target ED932AB3 (40 bytes changed, no reversions). The supplied full patches are preserved byte-for-byte. Both incremental patches were applied to the previous exact ROM and verified against the new output. Gameplay behavior and save compatibility remain unverified.

Same-version English-only replacement: target 80DA34B3 (64 bytes differ from 91D1183A, including one restored to the original ROM value). The supplied full patch is preserved byte-for-byte; the incremental patch was applied to the preceding ROM and yielded an identical output. Spanish QoL remains ED932AB3. Gameplay and save compatibility remain unverified.

Same-version Hard Mode replacement: English target D44FDE23 (75,187 changed bytes, 1,605 restored to original ROM values), Spanish QoL target A7935E07 (71,963 changed bytes, zero restored). Supplied full patches preserved byte-for-byte; both incremental patches verified against exact prior ROMs and identical new outputs. Hard Mode description is supplied by the developer; battle behavior, unchanged Normal Mode and save compatibility have not been independently playtested.

Same-version Hard Mode revision: English target 68CB83E3 (79,692 changed bytes, 173 restored to original ROM values), Spanish QoL target 5B141B2B (79,668 changed bytes, 63 restored). Supplied full BPS files preserved byte-for-byte. Both incremental patches verified against exact previous ROMs and reproduced supplied target ROMs. Gameplay behavior, mode isolation and save compatibility remain unverified.

Same-version full-patch replacement: English target 9EA90390 (21,045 changed bytes, 63 restored to original ROM values), Spanish QoL target 9901EE6E (21,922 changed bytes, 61 restored). Both supplied full patches preserved byte-for-byte and validated against the original Spanish FINAL v1.1 ROM. At the developer's request, no incremental patches were generated for this replacement. Active manifests accept the original ROM and identify the current output only; earlier builds must be replaced by applying the full patch to the original ROM. Historical patch files remain in the repository. Future update routing infrastructure remains intact. Gameplay and save compatibility remain unverified.
