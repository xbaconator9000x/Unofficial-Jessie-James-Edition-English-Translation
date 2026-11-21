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

The Jessie & James GitHub Pages launcher has privacy-friendly, cookie-free [Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/get-started/) enabled using the project's public Cloudflare site token. No custom domain, DNS change, paid plan or additional GitHub setup is required.

- After deployment, visit the [launcher](https://xbaconator9000x.github.io/Unofficial-Jessie-James-Edition-English-Translation/), then open the Cloudflare account's **Web Analytics** dashboard and select `xbaconator9000x.github.io`.
- The tracker measures website page views, approximate visits and referral sources. Metrics can be delayed, browser ad blockers may suppress events, and historical visits from before activation cannot be reconstructed.
- It does **not** track ROM contents, save files, patch file contents, completed patch downloads or identities. GitHub repository traffic and Reddit views are separate from launcher visits.
- The site identifier is public (as Cloudflare's embed snippet requires), not a credential. The deploy workflow injects the beacon into the published HTML only. To change accounts, set the Actions variable `CLOUDFLARE_WEB_ANALYTICS_TOKEN` to another 32-character site token; the variable takes priority over the default.

## Patcher conversions (optional event counts)

GitHub Pages is a static website, and **Cloudflare Web Analytics does not support custom events**. To measure verified patcher outcomes separately from Cloudflare's site-visit metrics, the English and Spanish browser patchers now have privacy-limited event hooks for:

- `english-rom-download-started`: English ROM was patched and verified against the target checksums, and browser save was initiated.
- `spanish-rom-download-started`: Spanish QoL ROM was patched and verified, and browser save was initiated.
- `english-bps-download-started`: Verified English BPS download was initiated.
- `spanish-bps-download-started`: Verified Spanish QoL BPS download was initiated.

These events are deliberately named **download started**, rather than download completed: browser JavaScript cannot verify whether the user kept the downloaded file or loaded it into an emulator. Only these four fixed event names and human-readable titles are transmitted. **No ROM bytes, names, file paths, save files, checksums, input revisions, patches or user-identifying fields are sent.** Tracking errors never block patching.

**Combined daily website and patcher reporting:** The owner's site at `https://xbaconator9000x.goatcounter.com` is configured in the GitHub Pages deploy workflow. Its script now records ordinary launcher pageviews **and** the four fixed patcher events, so a single GoatCounter daily email can include both types of activity. Cloudflare Web Analytics also independently measures website traffic and referrers; the two products may show different counts because of their counting rules and browser blockers. No API credentials or extra GitHub variable are required.

**To enable daily emails:** First verify the email address registered with GoatCounter. Log in to the [GoatCounter dashboard](https://xbaconator9000x.goatcounter.com/), click **your email address in the top navigation** (not **Settings**, which is for site settings), and open **User preferences**. Under **Email reports**, select **Daily** and save. The daily reports are sent by GoatCounter; the launcher itself does not send email. Cloudflare's built-in Web Analytics email summary is weekly only; optionally enable that in the [Cloudflare Notifications dashboard](https://dash.cloudflare.com/?to=/:account/notifications).

The configured GoatCounter site code is a public hostname, not a password or API credential. To use a different GoatCounter site later, set the optional GitHub Actions variable `GOATCOUNTER_SITE_CODE` to its subdomain label; it overrides the default `xbaconator9000x`. Visit and patcher statistics begin when tracking is enabled; historical counts cannot be recovered. The patcher events reflect verified output and **download initiation**, not guaranteed file completion or successful gameplay.


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

