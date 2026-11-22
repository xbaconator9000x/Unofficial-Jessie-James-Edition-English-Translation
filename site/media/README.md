# Jessie & James Edition fan artwork

The fan-made header logo, alternate logo and Game Boy Advance-style box art were created by **u/SnowMudK99** and supplied with permission for this unofficial English localisation. Please credit u/SnowMudK99 when sharing these images. Permission to use them for this release is not a general open-source licence or an endorsement by Nintendo, The Pokémon Company, or the original game's creator, MrNightology.

## Artwork files

- `jessie-james-logo-snowmudk99.webp` -- fan logo with red Rocket R, used in the website and README mastheads
- `jessie-james-logo-clean-snowmudk99.webp` -- clean logo variant, available as an optional download
- `jessie-james-cover-snowmudk99.jpg` -- full-resolution 1536×1536 fan box art, offered for emulator frontends

These are independent media files, not changes to any GBA ROM, BPS patch, or save.

## Using the cover in an emulator frontend

Many emulator libraries allow custom box images but do not extract artwork from GBA ROM headers. Download the JPG and use the frontend's custom media or artwork assignment. For RetroArch, thumbnail naming and playlist matching depend on the playlist; for ES-DE, local media scraping or an image path in a gamelist can be used; Android frontends may offer manual image assignment. Availability varies by app and version.

For an ES-DE/EmulationStation `gamelist.xml` entry, adapt the path and game filename to your own setup:

```xml
<game>
  <path>./Jessie-James-English-v1.03.2.gba</path>
  <name>Pokémon Team Rocket: Jessie &amp; James Edition</name>
  <image>./media/jessie-james-cover-snowmudk99.jpg</image>
</game>
```

Place the JPG at that image path (relative to the gamelist) and use your actual ROM filename. This is an example only, not universal auto-detection.

The images are not embedded in or distributed as a modified ROM.

## Complete artwork pack

The website offers `jessie-james-fan-art-pack.zip` containing the three images listed above. GitHub Pages generates the ZIP from the approved repository media during each deployment; no ROMs, patches, or saves are included.
