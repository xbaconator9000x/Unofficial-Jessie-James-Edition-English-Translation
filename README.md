<p align="center">
  <a href="#art-credit">
    <img src="site/media/jessie-james-logo-snowmudk99.webp" alt="Jessie & James fan logo with Rocket R, by SnowMudK99" width="320">
  </a>
</p>

<h1 align="center">Pokémon Team Rocket: Jessie & James Edition</h1>

<p align="center"><strong>Unofficial English Translation</strong></p>

<p align="center">
  <a href="https://xbaconator9000x.github.io/Unofficial-Jessie-James-Edition-English-Translation/"><strong>Visit the Team Rocket website</strong></a>
  &nbsp;|&nbsp;
  <a href="https://xbaconator9000x.github.io/Unofficial-Jessie-James-Edition-English-Translation/#releases"><strong>Patch your ROM</strong></a>
  &nbsp;|&nbsp;
  <a href="https://xbaconator9000x.github.io/Unofficial-Jessie-James-Edition-English-Translation/#spanish">Español QoL</a>
  &nbsp;|&nbsp;
  <a href="https://xbaconator9000x.github.io/Unofficial-Jessie-James-Edition-English-Translation/#changelog">Changelogs</a>
  &nbsp;|&nbsp;
  <a href="https://tally.so/r/M1N2oE">Submit a private bug report</a>
</p>

---

## What is Jessie & James Edition?

*Pokémon Team Rocket: Jessie & James Edition* is an original FireRed-based game by MrNightology, first released in Spanish. You play as James alongside Jessie and Meowth.

After another failed attempt to steal Pikachu, a Delibird arrives with a message from Giovanni. The trio return to Kanto to carry out Team Rocket missions. Expect to steal Pokémon and items, investigate places and get in other people's way. I won't spoil the missions themselves.

The game covers **Kanto and Johto**. It also includes the Battle Subway, shop robberies, a day/night cycle, dynamic overworld palettes, a Black/White-style Repel system, Ruins of Alph puzzles, region-specific wild Pokémon music, extra trainer themes, expanded overworld and music tables, dynamic healing locations and VS bars.

[View MrNightology's original Spanish release](https://www.whackahack.com/juegos/pokemon-team-rocket-jessie-james/).

## Translation

This is my unofficial English translation of the completed v1.1 game. I'm not affiliated with the original developer.

I extracted the Spanish text and replaced matching FireRed lines with their official English versions. For the rest, I used Google Translate as a starting point, then went through the dialogue with the anime as a reference for the characters' voices. I also fixed text wrapping and page breaks where needed.

Finally, I added some additional quality of life features that were not included in the original rom, to help make the game a bit more accessible to modern audiences.

### Quality of life

- **Classic / Modern battles** -- Choose the original Gen 3 mechanics or the physical/special split and updated ability effects when starting a new game. I've also made TMs reusable in Modern Mode, though they remain single use in Classic Mode.
- **Nature colours** -- Increased stats in red, decreased stats in blue.
- **Move details** -- Press L when choosing a move to view its description, power, accuracy and category.
- **Effectiveness indicators** -- See whether a move's type matchup is super effective, neutral, resisted or has no effect.
- **Optional and toggleable EXP. ALL key item**
- **Optional Hard Mode** -- I've written custom scripts to improve trainer AI, increased team depth and added more variety to movesets, without increasing levels or placing restrictions on the player.
- **Title music** -- A looping version of the Team Rocket motto theme.

#### Major QOL additions in v1.02

- **Nature mints**
- **Bottle caps and Golden bottle caps**
- **EV berries** -- Restored their original function.
- **IV and EV readers** -- Available through the scientists at Rocket HQ.
- **Five-digit prices** -- Expanded the price display to support five digits.
- **Item prices** -- Adjusted reusable TM prices in Modern Mode and vitamin prices.

#### New in v1.03

- **Expanded bag item storage**
- **Reusable Escape Rope** -- Now a key item.
- **EV training Power items** -- Power Anklet, Band, Belt, Bracer, Lens and Weight.
- **EV/IV reader fix** -- Fixed a glitch in the reader.

I have yet to complete an end-to-end run of the game, and so I have not confirmed and tested every possible bug or exploit. I cannot guarantee that the translation is 100% perfect. As such, I would appreciate if you could report any bugs or translation mistakes you do find in the [bug reporting section of this page](#testing-and-bug-reports). Providing screenshots or a .sav file would also be incredibly helpful!

## Original Spanish Screenshots

These are screenshots from MrNightology's original Spanish version, not the English translation.

<p align="center">
  <a href="https://www.whackahack.com/juegos/pokemon-team-rocket-jessie-james/">
    <img src="https://i.imgur.com/dzyKZbR.png" alt="Original Spanish Jessie & James Edition gameplay screenshots" width="720">
  </a>
</p>

<details>
<summary>Original Spanish release -- Battle Subway map</summary>

<p align="center">
  <img src="https://i.imgur.com/XZrC1aW.png" alt="Battle Subway map from the original Spanish release" width="720">
</p>

</details>

## Fan art and emulator box art

<p align="center">
  <a href="#art-credit">
    <img src="site/media/jessie-james-cover-snowmudk99.jpg" alt="Unofficial GBA box art for Pokémon Team Rocket: Jessie & James Edition" width="320">
  </a>
</p>

Download for use in emulators that use GBA cover art.

[Download artwork (ZIP)](https://xbaconator9000x.github.io/Unofficial-Jessie-James-Edition-English-Translation/media/jessie-james-fan-art-pack.zip)

Includes:
- GBA box art (JPG)
- Logo with Rocket R (WEBP)
- Logo without Rocket R (WEBP)

## Website traffic analytics (maintainer)

This repository's GitHub **Insights → Traffic** measures *GitHub repository* visits, **not** visits to the launcher at GitHub Pages. The launcher supports optional [Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/get-started/) so its owner can see website pageviews, approximate unique visitors, referrers and traffic trends without cookies or moving the site away from GitHub Pages.

To activate it:

1. Create/sign in to a free Cloudflare account and open **Web Analytics → Add a site**. Enter the hostname `xbaconator9000x.github.io` (not the full repository path). Cloudflare doesn't need your domain's DNS or proxy moved.
2. In Cloudflare's **Manage site** page, copy the 32-character hexadecimal **site token** found inside its JavaScript snippet (the `"token"` value). This is a public site identifier, **not** a Cloudflare API key.
3. On GitHub, open this repository's **Settings → Secrets and variables → Actions → Variables → New repository variable**. Name it `CLOUDFLARE_WEB_ANALYTICS_TOKEN` and paste the site token.
4. Run **Actions → Publish Team Rocket landing page → Run workflow** (or publish a subsequent site change). The deploy workflow checks the token and injects the official Cloudflare beacon *into the published page only*, leaving the source HTML unchanged.
5. Open the launcher, then open the **Cloudflare Web Analytics dashboard** to see visits, pages and referrers. Allow for reporting delay; test pageviews may not show instantly.

The tracker is **off** when the variable isn't set. No ROM contents, BPS files, save data, upload contents or patcher activity are sent to this analytics service; this tracks website visits, **not** successful downloads or patch usage. No historic website visits can be recovered retroactively, and views of Reddit or the GitHub repository are separate numbers. Cloudflare's JavaScript-based counts can miss blocked scripts and aren't a definitive unique-person tally.

## Testing and Bug Reports

Testing is still ongoing. There's a lot of conditional dialogue and one-off events, so there may still be untranslated lines, odd wording, text errors or bugs that only show up under certain conditions.

If you find something, [submit a private bug report](https://tally.so/r/M1N2oE). Screenshots or a short video help, especially if you can include the location, emulator, patch version and how to reproduce it.

No sign-in or personal details needed. Reports and attachments aren't public. Please don't upload ROMs or patches.

## Releases

**English v1.03** -- 22 November 2026.

[Open the browser ROM patcher](https://xbaconator9000x.github.io/Unofficial-Jessie-James-Edition-English-Translation/#releases).

Choose your own matching original Spanish FINAL v1.1 ROM (16 MiB, CRC32 `805E24CA`), English v1.0 (`C043455C`), English v1.01 (`A3E3CC2F`) or either English v1.02 build (`CADC8480` or `D2866130`). The browser patcher verifies the selected ROM, applies the verified BPS update path locally and downloads English v1.03. Nothing is uploaded. A diagnostic report is available if something goes wrong.

Expected English v1.03 output CRC32: `6E1E5095`. The patcher handles earlier releases automatically, including both v1.02 builds. The original Spanish ROM uses the complete v1.03 patch. Keep backups of your ROM and save. No pre-patched ROMs.

## Prefer to play español?

Si prefieres jugar a la versión original en español, he preparado otro parche para que también puedas disfrutar de las mejoras de calidad de vida que he añadido a mi versión inglesa, sin tener que jugar en inglés. El objetivo es mantener el juego de MrNightology en español y añadir esas mejoras, no hacer una nueva traducción.

**Modo difícil opcional** -- He escrito scripts propios para mejorar la IA de los entrenadores, he ampliado sus equipos y he dado más variedad a sus movimientos, sin subir los niveles ni imponer restricciones al jugador.

[Aplicar el parche de mejoras a la versión en español](https://xbaconator9000x.github.io/Unofficial-Jessie-James-Edition-English-Translation/#spanish).

Utiliza la ROM original FINAL v1.1 en español (CRC32 `805E24CA`), la versión española QoL v1.0 (`7C042814`) o cualquiera de las versiones QoL v1.02 (`0486144D` o `58F089B9`). El resultado QoL v1.03 permanece en español (CRC32 `222A0072`). El parche es independiente de la traducción inglesa. No envíes ROMs ni archivos de guardado.

## Changelog

### English v1.03 -- 22 November 2026

- Expanded bag item storage
- Escape rope is now a reuseable key item
- Added Power items for EV training (Power Anklet, Band, Belt, Bracer, Lens, and Weight)
- Fixed EV/IV reader glitch

### English v1.02 -- 21 November 2026

- Translated additional hidden Spanish dialogue
- Fixed pick-up table bug
- Repaired text wrapping issues
- Updated move description text wrapping
- Restored native English localisation to items
- Translated trainer names and classes to English localisation standards
- Added Oak battle to boss pool for improved combat AI in HARD mode.
- Location and reference localisation fixes
- Prices tweaked for Modern mode reuseable TMs
- Prices tweaked for vitamins
- **MAJOR QOL additions:**
  - Nature mints
  - Bottle caps and Golden bottle caps
  - Restored function to EV berries
  - IV and EV readers (Rocket HQ Scientists)
  - Expanded price list to five-digits

### English v1.01 -- 20 November 2026

- Fixed graphical issue during blast-off sequence
- Corrected byte allocation overlap for EXP. ALL and Hard mode
- Corrected game-breaking freeze in Oak's lab.

### English v1.0 -- 20 November 2026

- Initial public English translation release.
- English dialogue, menus and text formatting.
- Classic and Modern battle options, nature colours, move details and effectiveness indicators, and title music.

[Release history and patcher](https://xbaconator9000x.github.io/Unofficial-Jessie-James-Edition-English-Translation/#changelog).

## Credits

Full credit for the original game, story, maps, artwork and gameplay goes to **MrNightology and the original project's contributors**. The game was translated without author consultation.

English localisation and patcher maintenance -- [@xbaconator9000x](https://github.com/xbaconator9000x).

<a id="art-credit"></a>
Box art and logos -- **u/SnowMudK99**, used with permission.

Small Team Rocket R icons and the website favicon are sourced from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Team_Rocket_Logo.svg). Original Spanish screenshots are from [MrNightology's release](https://www.whackahack.com/juegos/pokemon-team-rocket-jessie-james/).

