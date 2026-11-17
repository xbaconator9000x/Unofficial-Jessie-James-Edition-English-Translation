# Publishing an update

Keep each previous BPS unchanged. For each new English version, generate a BPS from the exact original Spanish ROM to the new ROM and an incremental BPS from the preceding English ROM to the new ROM. Keep every intervening update edge so the browser can upgrade older English ROMs automatically. A matching size and CRC32 identify each ROM; every patch also has its own CRC32, size and SHA-256. Record those values in releases.json, including the source and output ROM SHA-256 fingerprints in romSha256. Update the target, latest version, versions dictionary and changelog. Only replace a published BPS for an explicitly approved same-version correction. Keep the earlier ROM fingerprint and an independently verified incremental patch to the corrected build; do not change the public version or changelog.

Before publishing verify both clean- and incremental-patch outputs byte-for-byte, including the final output checksum. Back up saves and separately test in-game save compatibility. The patcher does not modify save files.

For v1.0, place the supplied verified BPS at site/patches/jessie-james-english-v1.0.bps. Its SHA-256 is c6b07a2cc6fdfa1a32c923ae6b1d0aa747a5c2c4d15ceb0c1663ba2a675130bf. The earlier English v1.0 ROM is supported through jessie-james-english-v1.0-hotswap.bps (SHA-256 b6f0f9eb81ecc509a82cf2359af8be382593130561ec2771c1be5f7533e5c3b7). The site refuses mismatches. Both patches must be present and verified before deployment.

Run node tests/bps.test.mjs before publishing. GitHub Pages also checks the manifest and every hosted BPS before deploying.
