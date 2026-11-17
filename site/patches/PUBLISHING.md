# Publishing an update

Keep each previous BPS unchanged. For each new English version, generate a BPS from the exact original Spanish ROM to the new ROM and an incremental BPS from the preceding English ROM to the new ROM. Keep every intervening update edge so the browser can upgrade older English ROMs automatically. A matching size and CRC32 identify each ROM; every patch also has its own CRC32, size and SHA-256. Record those values in releases.json. Update the target, latest version, versions dictionary and changelog. Never overwrite an existing published BPS.

Before publishing verify both clean- and incremental-patch outputs byte-for-byte, including the final output checksum. Back up saves and separately test in-game save compatibility. The patcher does not modify save files.

For v1.0, place the supplied verified BPS at site/patches/jessie-james-english-v1.0.bps. Its SHA-256 is 1465ae91e0c55b328d7b5fa871387525a361fa9746e71f4083dea84c66aecbb9. The site refuses mismatches and permits a local copy of the same patch until a hosted copy is present.

Run node tests/bps.test.mjs before publishing.
