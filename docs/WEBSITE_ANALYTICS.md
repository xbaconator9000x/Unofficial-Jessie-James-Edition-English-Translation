# Website analytics and download-start counts

The GitHub Pages launcher uses two independent, cookie-free counters:

- **Cloudflare Web Analytics:** pageviews, approximate visits and referrers. Site identifier: `xbaconator9000x.github.io`.
- **GoatCounter:** ordinary pageviews, plus four events: `english-rom-download-started`, `spanish-rom-download-started`, `english-bps-download-started`, and `spanish-bps-download-started`. Dashboard: https://xbaconator9000x.goatcounter.com/.

These are *download starts*, not completed downloads. Browsers do not report whether a visitor kept the resulting file or loaded it successfully. The two services may show different visit totals, and blockers may suppress events. No historical visits can be reconstructed.

The patcher runs locally in the visitor's browser. It doesn't transmit ROM bytes, patch contents, save data, local filenames or game checksums to the counters. Only fixed event names are tracked. Analytics failures never block patching.

## Deployment configuration

The Pages workflow injects the tracking scripts after running the patcher tests:

- `scripts/inject_web_analytics.py` uses the public Cloudflare site token. To change it, set the repository Actions variable `CLOUDFLARE_WEB_ANALYTICS_TOKEN` to the new 32-character site token.
- `scripts/inject_patch_events.py` uses the GoatCounter site code `xbaconator9000x` by default. To change it, set the Actions variable `GOATCOUNTER_SITE_CODE` to the new subdomain label.
- The corresponding tests are `tests/website-analytics.test.py`, `tests/patch-events-injection.test.py` and `tests/patch-events.test.mjs`.

The site tokens and codes used by browser analytics are public identifiers, **not API secrets**. Do not commit private analytics credentials.

## Email reports

For a daily GoatCounter email, sign in to https://xbaconator9000x.goatcounter.com/, select the email address in the top navigation, open **User preferences**, choose **Daily** under **Email reports**, then save. Cloudflare's built-in Web Analytics email summary is weekly; its notification settings are managed in the Cloudflare dashboard.

The counts reflect site usage and verified patcher actions, not individual players or gameplay success.
