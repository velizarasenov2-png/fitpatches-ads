# Halloween website visuals of health, wellness, supplement, weight-loss and better-for-you food/drink brands (2021–2025)

Research notes compiled 2026-10-25 for fitpatches.net, a pink (#d64d87) Shopify store selling berberine patches for weight and blood sugar to Bulgarian women aged about 30–55.

**How to read these notes.** Every website observation carries the exact capture date and time (UTC) and links to the raw archived record. Each item is tagged with how it was obtained:
- **[OBSERVED]**: I read the archived HTML myself, rendered it, or viewed the original image file.
- **[PRESS]**: taken from trade press or a brand press release.
- **[INFERENCE]**: my own reasoning.

**Why the evidence comes from Common Crawl.** The Wayback Machine could not be used this session:
- web.archive.org and wayback.archive.org reset the connection from the shell.
- WebFetch refuses web.archive.org.
- The Firecrawl account ran out of credits on the first call.
- The archive.org availability API returned HTTP 429 once requests ran in parallel.

Instead, the primary evidence comes from **Common Crawl (CC)** web archives on data.commoncrawl.org. These are raw HTML captures of the real sites, stored in WARC files. Each citation links to the WARC file and gives the byte offset of the record. Images, hero banners and mascots were then downloaded from the brands' own CDNs, where most of the original files still exist. Where the theme CSS still exists, archived pages were re-rendered in headless Chrome.

---

## 0. Evidence base: what was captured, the crawl windows, and the saved files

### Takeaway
Archived HTML from 9 crawls was checked for 37 brand domains: 133,098 index records scanned, 337 pages fetched and parsed, of which 244 are homepage captures. Captures exist for every brand in the brief except where noted. The October crawls mostly cover **early to mid October**. The November crawls cover **the first two weeks after Halloween**. So the evidence shows each brand's first Halloween wave and its take-down, but usually not the final week of October.

### Cited Findings
- **Crawl windows**, measured from the capture timestamps actually retrieved:

| Crawl | Dates covered |
|---|---|
| CC-MAIN-2021-43 | 15–28 Oct 2021, the best late-October coverage |
| CC-MAIN-2022-40 | 24 Sep – 7 Oct 2022 |
| CC-MAIN-2022-49 | 26 Nov – 10 Dec 2022 |
| CC-MAIN-2023-40 | 21 Sep – 5 Oct 2023 |
| CC-MAIN-2023-50 | 28 Nov – 11 Dec 2023 |
| CC-MAIN-2024-42 | 3–16 Oct 2024 |
| CC-MAIN-2024-46 | 1–15 Nov 2024 |
| CC-MAIN-2025-43 | 5–18 Oct 2025 |
| CC-MAIN-2025-47 | 6–19 Nov 2025 |

  [Common Crawl crawl index list](https://data.commoncrawl.org/crawl-data/index.html)
- **Domains checked:**
  - Supplements, wellness and weight-loss brands: athleticgreens.com / drinkag1.com (AG1), ritual.com, olly.com, goli.com, sugarbearhair.com, lemmelive.com, bloomnu.com, ghostlifestyle.com, forhims.com, forhers.com, noom.com, arrae.com, seed.com, cymbiotika.com, gruns.co, myprotein.com, myprotein.bg (the Bulgarian store), gymshark.com, huel.com, drinklmnt.com, lovewellness.com.
  - Better-for-you food and drink brands: drinkolipop.com, drinkpoppi.com, liquiddeath.com, magicspoon.com, feastables.com, smartsweets.com, lilys.com, hukitchen.com, unrealsnacks.com, skinnydipped.com, yumearth.com.
  - Full-takeover references: krispykreme.com, oreo.com.
  - Also queried but with no usable homepage capture: obvi.com and myprotein.co.uk (which redirects to myprotein.com).
- **Asset dates.** On Shopify, the `?v=` number in a file URL is the Unix timestamp of the file's last upload or update. Decoding it shows when each Halloween asset was created. [The values are OBSERVED; reading them as upload dates is an INFERENCE from Shopify's cache-busting convention.]
  - SmartSweets 2021 Halloween product tiles: v=1632756819, i.e. 27 Sep 2021.
  - SmartSweets 2024 hero: v=1727207996, i.e. 24 Sep 2024.
  - Unreal 2024 hero: v=1726773734, i.e. 19 Sep 2024.
  - Feastables 2024 Halloween pack image: v=1723740026, i.e. 15 Aug 2024.
  - Unreal 2025 ghost tile: v=1757099894, i.e. 5 Sep 2025.
  - Feastables 2025 sweepstakes hero: v=1757627140, i.e. 11 Sep 2025.
  - Bloom "Witching Hour Sale" banner: v=1730222824, i.e. 29 Oct 2024.

### Saved files
All files are in `/home/user/fitpatches-ads/research_notes/Halloween визия за сайта/shots/`.
- **RENDER**: archived HTML re-rendered with its still-live CSS. JavaScript is off and lazy images are forced to load, so carousels and pop-ups do not appear.
- **ASSET**: the original image file, fetched from the brand's CDN using the URL found in the archived HTML.
- **RECONSTRUCTION**: assembled by me from archived text plus the original asset. The layout is approximate.

| File | Type | What it shows |
|---|---|---|
| `health_smartsweets_2021-10-19_product-tile-with-bat-overlay.png` | ASSET from the 2021-10-19 homepage | Standard Sweet Fish pouch with a small grey bat silhouette added top-left. The normal product photo is unchanged otherwise; this "Halloween grid" version was used site-wide. |
| `health_smartsweets_2021-10-19_hero-buildabox-desktop.jpg` | ASSET, hero | Flat orange background, cobwebs, scattered gummies, an open kraft box of colourful pouches, and the black shadow of a clawed hand reaching in. |
| `health_smartsweets_2021-10-19_buildabox-tile-shadow-hand.png` | ASSET | Orange Build-a-Box with the shadow hand and a bat. |
| `health_smartsweets_2022-10-06_halloween-buildabox-tile.png` | ASSET | 2022 version of the same idea: orange box, shadow hand, bat. |
| `health_smartsweets_2024-10-09_hero-image-desktop.png` / `..._hero-image-mobile.png` | ASSET, hero | Regular pastel pouches over a black/grey smoky panel with white cobwebs, cut into a curved "portal" shape. |
| `health_smartsweets_2024-10-09_hero_RECONSTRUCTION.png` | RECONSTRUCTION | Hero image beside the archived headline: purple #4c0185 condensed "BRINGING CANDY BACK TO LIFE", "Sugar is spooky. But candy doesn't have to be!" and a "Shop Now" pill button. |
| `health_CONTACTSHEET_smartsweets_2021-2025.png` | Contact sheet | Every SmartSweets image pulled from the 2021–2025 captures. |
| `health_unreal_2022-09-29_halloween-box-coconut.png` / `..._pbcups.png` | ASSET | Halloween retail boxes: purple and orange, black bats, haunted-house silhouettes, with the white UNREAL logo kept. |
| `health_unreal_2023-09-28_halloween-landing-render.png` | RENDER of /pages/halloween22 | Orange headline "all treats, no tricks."; white photo backdrop with plastic spiders, mini pumpkins, cinnamon, cobweb, and Halloween boxes in a mesh trick-or-treat bag. |
| `health_unreal_2024-10-14_home-render-desktop.png` / `..._mobile.png` | RENDER of the homepage | Full-bleed orange hero with shadow "zombie hands", white rounded headline "spooky good!" and sub-line "(no spooky ingredients)", stacked purple/orange Halloween boxes, white pill CTAs. Below it, purple text on cream: "snatch up your halloween treats, before it's too late!" |
| `health_unreal_2024-10-14_hero-banner-asset.jpg` | ASSET | The 1800px hero photo (orange set, shadow hands). |
| `health_unreal_2025-10-16_home-render-desktop.png` | RENDER | The 2025 hero is NOT Halloween: yellow "HOLD ONTO YOUR TASTEBUDS." Halloween appears only in the product grid. |
| `health_unreal_2025-10-16_cute-ghost-mascot-product-tile.png` | ASSET | A friendly white cartoon ghost mascot hugging a red bag of peanut butter cups, used as a product-tile image. |
| `health_yumearth_2022-09-26_home-render.png` / `..._halloween-banner-mobile.jpg` | RENDER + ASSET | Hero "Spooktacular Treats are Here!" in purple on a yellow/lime block. Allergy-free icon row. Lime banner with products and bats. |
| `health_yumearth_2023-09-22_home-render.png`, `..._kids-costume-banner.jpg`, `..._pumpkin-shaped-pack.png` | RENDER + ASSETS | Teal hero "Delicious Allergy Friendly Treats! Enjoy for all your Halloween Festivities!" Photo of smiling kids in witch, owl and other costumes with a teal pumpkin bucket. Pumpkin-silhouette pack. |
| `health_yumearth_2025-10-09_home-render-desktop.png` / `..._mobile.png` | RENDER | Orange hero "New Halloween Choco Yums!" and a teal announcement bar with code SPOOKYBUNDLE. |
| `health_CONTACTSHEET_yumearth_2021-2025.png` | Contact sheet | YumEarth Halloween packaging and banners. |
| `health_feastables_2024-10-08_home-render.png` | RENDER | Dark/orange hero "THIS HALLOWEEN, YOU COULD WIN CASH ALL MONTH LONG – $10,000 DAILY WINNER / $1,000,000 GRAND PRIZE", with bats, a graveyard and MrBeast. |
| `health_feastables_2025-10-17_home-render.png` | RENDER | The homepage hero is the non-Halloween "DRIP" bar. Halloween items sit in the grid and nav. |
| `health_feastables_2025-10-17_halloween-sweeps-render.png` | RENDER | Purple swirl and orange "HALLOWEEN SWEEPS – THIS HALLOWEEN, ENTER FOR A CHANCE TO WIN SCARY GOOD PRIZES". |
| `health_feastables_2025-10-17_jack-o-lantern-cups-pack.png` | ASSET | Jack-o-lantern-moulded chocolate cups in orange/purple packaging. |
| `health_CONTACTSHEET_feastables-oreo_2024-2025.png` | Contact sheet | Feastables and Oreo Halloween assets. |
| `health_oreo_2025-10-09_oreoid-halloween-spider-box.png` / `..._fullmoon-box.png` | ASSET | Custom OREOiD Halloween boxes: dark navy/purple, orange "BOO!" and jack-o-lantern printed cookies, a cartoon spider, a full moon. |
| `health_krispykreme_2021-10-27_hero-halloween-dozen.png`, `..._scary-sharies-promo.png`, `..._spooky-gift-card.png` | ASSET, homepage carousel | Full takeover. Violet/purple sky, cauldron with purple smoke, a "Spellbook" box, lime-green script "Halloween Dozen", "Saturday Scary Sharies $1 Dozen code SCARY", "Send a Spooky Gift!" |
| `health_krispykreme_2025-10-16_hero-trick-or-treat-collection.png` | ASSET, desktop + mobile hero | Purple steps and a haunted-house door, an orange floor, a cute paper ghost and a jack-o-lantern, plus decorated doughnuts with white script labels. |
| `health_bloom_2024-10-29_witching-hour-sale-banner-desktop-ANIMATED.gif`, `..._mobile-ANIMATED.gif`, `..._desktop-frames.png` | ASSET, /collections/halloween-sale | Bloom Nutrition's "WITCHING HOUR SALE – up to 25% OFF assorted treats". Pastel pink-to-mint gradient, a cauldron with smoke, floating bubbles, tubs flying out. Two-frame animation (1.2 s per frame) swapping a pink-gloved hand for a green witch hand. |
| `health_lilys_2025-10-15_fall-hero-not-halloween.png` | ASSET | Lily's (no-sugar-added chocolate) used an autumn hero (pumpkin muffins, cinnamon) instead of Halloween. |
| `health_hu_2021-10-18_pumpkin-spice-hero-not-halloween.jpg` | ASSET | Hu Kitchen's rust-orange velvet "pumpkin spice" bar launch, a fall look rather than Halloween. |
| `health_LIVE_2026-10-25_{smartsweets, unreal, yumearth, krispykreme, olipop, bloom, feastables, goli, olly, ritual, noom, lemme, gruns, cymbiotika, myprotein_bg, gymshark, huel, ghost, lilys}.png` | LIVE screenshots (JavaScript on), taken today, 2026-10-25 | Cookie or pop-up overlays are visible on some, e.g. SmartSweets, Krispy Kreme and YumEarth. See section 4. |

### Inferences
- Common Crawl is a valid substitute for the Wayback Machine here: it holds the same kind of record (the raw HTML the site served at a timestamp). Where the brands' CDNs still serve the original files, it also yields the original hero images at full resolution.
- Captures cluster in early October and early November. "No Halloween seen" therefore means "nothing by about 5–16 October". It does not mean "nothing in the last week of October". Section 4 handles this.

### Gaps
- No Wayback, Milled or Really Good Emails screenshots could be fetched: Wayback was blocked, Firecrawl had no credits, and Milled returned 403.
- Pages built in JavaScript show little in their static HTML: Noom 2021–2023, parts of Bloom, Krispy Kreme 2022, Hers. For those, a "no Halloween" verdict rests only on the server-rendered text and image URLs.
- No captures were found for sugarbearhair.com's homepage in these crawls, and only partial ones for Grüns, Lemme and Olly.
- Some captures were truncated by Common Crawl at 1 MiB: Bloom 2022–2023, Gymshark and Hers. Halloween content placed late in those pages could be missing.

### Capture reference table (every Common Crawl record cited in these notes)
Each record can be fetched with `curl -r OFFSET-(OFFSET+LENGTH-1) WARC_URL | gunzip`.

| Capture (UTC) | Original URL | Crawl | WARC file | Offset | Length |
|---|---|---|---|---|---|
| 2021-10-19 21:40:11 | https://athleticgreens.com/ | CC-MAIN-2021-43 | [CC-MAIN-20211019202148-20211019232148-00684.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323585281.35/warc/CC-MAIN-20211019202148-20211019232148-00684.warc.gz) | 209476787 | 53239 |
| 2022-09-30 00:19:45 | https://athleticgreens.com | CC-MAIN-2022-40 | [CC-MAIN-20220929225326-20220930015326-00755.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030335396.92/warc/CC-MAIN-20220929225326-20220930015326-00755.warc.gz) | 142763759 | 74863 |
| 2024-10-05 06:25:00 | https://bloomnu.com | CC-MAIN-2024-42 | [CC-MAIN-20241005051646-20241005081646-00893.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253348.29/warc/CC-MAIN-20241005051646-20241005081646-00893.warc.gz) | 116112840 | 120737 |
| 2024-11-02 08:34:17 | https://bloomnu.com | CC-MAIN-2024-46 | [CC-MAIN-20241102071948-20241102101948-00893.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477027709.8/warc/CC-MAIN-20241102071948-20241102101948-00893.warc.gz) | 124601473 | 129645 |
| 2024-11-02 09:05:56 | https://bloomnu.com/collections/halloween-sale | CC-MAIN-2024-46 | [CC-MAIN-20241102071948-20241102101948-00823.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477027709.8/warc/CC-MAIN-20241102071948-20241102101948-00823.warc.gz) | 125991943 | 129872 |
| 2025-10-14 13:08:21 | https://bloomnu.com/ | CC-MAIN-2025-43 | [CC-MAIN-20251014122347-20251014152347-00850.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648359174.55/warc/CC-MAIN-20251014122347-20251014152347-00850.warc.gz) | 110878817 | 237513 |
| 2024-11-02 08:32:49 | https://cymbiotika.com/ | CC-MAIN-2024-46 | [CC-MAIN-20241102071948-20241102101948-00080.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477027709.8/warc/CC-MAIN-20241102071948-20241102101948-00080.warc.gz) | 182704102 | 175951 |
| 2025-10-17 18:14:17 | https://cymbiotika.com/ | CC-MAIN-2025-43 | [CC-MAIN-20251017160008-20251017190008-00280.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648665632.70/warc/CC-MAIN-20251017160008-20251017190008-00280.warc.gz) | 200590811 | 206893 |
| 2024-10-15 09:04:14 | https://drinkag1.com/ | CC-MAIN-2024-42 | [CC-MAIN-20241015081428-20241015111428-00661.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944255673.65/warc/CC-MAIN-20241015081428-20241015111428-00661.warc.gz) | 183222979 | 163797 |
| 2025-10-18 14:02:54 | https://drinkag1.com/ | CC-MAIN-2025-43 | [CC-MAIN-20251018123814-20251018153814-00161.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648666508.88/warc/CC-MAIN-20251018123814-20251018153814-00161.warc.gz) | 211909657 | 58764 |
| 2024-10-11 01:39:07 | https://drinklmnt.com/ | CC-MAIN-2024-42 | [CC-MAIN-20241011011611-20241011041611-00121.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253749.74/warc/CC-MAIN-20241011011611-20241011041611-00121.warc.gz) | 189409290 | 23667 |
| 2021-10-21 19:08:31 | https://drinkolipop.com/ | CC-MAIN-2021-43 | [CC-MAIN-20211021164535-20211021194535-00127.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323585439.59/warc/CC-MAIN-20211021164535-20211021194535-00127.warc.gz) | 328263091 | 43013 |
| 2022-10-07 01:55:58 | https://drinkolipop.com/ | CC-MAIN-2022-40 | [CC-MAIN-20221007014029-20221007044029-00047.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030337906.7/warc/CC-MAIN-20221007014029-20221007044029-00047.warc.gz) | 267865043 | 61900 |
| 2022-10-07 04:05:22 | https://drinkolipop.com/blogs/digest/keeping-your-gut-healthy-during-a-sugar-filled-holiday-a-parents-survival-guide-to-halloween | CC-MAIN-2022-40 | [CC-MAIN-20221007014029-20221007044029-00791.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030337906.7/warc/CC-MAIN-20221007014029-20221007044029-00791.warc.gz) | 272594263 | 63838 |
| 2023-09-27 22:27:39 | https://drinkolipop.com | CC-MAIN-2023-40 | [CC-MAIN-20230927203115-20230927233115-00052.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233510326.82/warc/CC-MAIN-20230927203115-20230927233115-00052.warc.gz) | 243314378 | 69056 |
| 2024-10-14 17:17:51 | https://drinkolipop.com | CC-MAIN-2024-42 | [CC-MAIN-20241014163540-20241014193540-00052.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944255489.84/warc/CC-MAIN-20241014163540-20241014193540-00052.warc.gz) | 182127838 | 87286 |
| 2024-11-13 18:40:40 | https://drinkolipop.com/pages/olipop-halloween-sweepstakes-official-rules | CC-MAIN-2024-46 | [CC-MAIN-20241113171551-20241113201551-00079.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477028387.69/warc/CC-MAIN-20241113171551-20241113201551-00079.warc.gz) | 195100077 | 80775 |
| 2024-11-13 18:47:42 | https://drinkolipop.com/ | CC-MAIN-2024-46 | [CC-MAIN-20241113171551-20241113201551-00847.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477028387.69/warc/CC-MAIN-20241113171551-20241113201551-00847.warc.gz) | 189608879 | 90930 |
| 2025-10-13 12:37:29 | https://drinkolipop.com | CC-MAIN-2025-43 | [CC-MAIN-20251013111241-20251013141241-00552.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648358967.31/warc/CC-MAIN-20251013111241-20251013141241-00552.warc.gz) | 190121391 | 100585 |
| 2024-10-15 22:48:36 | https://drinkpoppi.com/ | CC-MAIN-2024-42 | [CC-MAIN-20241015204737-20241015234737-00298.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944591543.93/warc/CC-MAIN-20241015204737-20241015234737-00298.warc.gz) | 178513147 | 62293 |
| 2025-10-13 12:53:46 | https://drinkpoppi.com/ | CC-MAIN-2025-43 | [CC-MAIN-20251013111241-20251013141241-00098.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648358967.31/warc/CC-MAIN-20251013111241-20251013141241-00098.warc.gz) | 199971808 | 72425 |
| 2024-10-08 08:32:01 | https://feastables.com/ | CC-MAIN-2024-42 | [CC-MAIN-20241008075444-20241008105444-00790.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253528.64/warc/CC-MAIN-20241008075444-20241008105444-00790.warc.gz) | 212968326 | 63725 |
| 2025-10-17 13:24:13 | https://feastables.com/ | CC-MAIN-2025-43 | [CC-MAIN-20251017125300-20251017155300-00590.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648665304.94/warc/CC-MAIN-20251017125300-20251017155300-00590.warc.gz) | 216373078 | 99759 |
| 2025-10-17 13:55:23 | https://feastables.com/pages/halloween-sweepstakes | CC-MAIN-2025-43 | [CC-MAIN-20251017125300-20251017155300-00004.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648665304.94/warc/CC-MAIN-20251017125300-20251017155300-00004.warc.gz) | 226030662 | 111218 |
| 2021-10-20 01:27:14 | https://goli.com | CC-MAIN-2021-43 | [CC-MAIN-20211019233130-20211020023130-00040.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323585290.83/warc/CC-MAIN-20211019233130-20211020023130-00040.warc.gz) | 418741915 | 62530 |
| 2024-10-13 00:15:13 | https://goli.com/ | CC-MAIN-2024-42 | [CC-MAIN-20241012235949-20241013025949-00879.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944255020.72/warc/CC-MAIN-20241012235949-20241013025949-00879.warc.gz) | 239735644 | 39762 |
| 2025-10-11 12:30:42 | https://goli.com/ | CC-MAIN-2025-43 | [CC-MAIN-20251011121535-20251011151535-00279.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648358675.50/warc/CC-MAIN-20251011121535-20251011151535-00279.warc.gz) | 262730866 | 39792 |
| 2025-10-17 16:47:32 | https://gruns.co/ | CC-MAIN-2025-43 | [CC-MAIN-20251017160008-20251017190008-00836.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648665632.70/warc/CC-MAIN-20251017160008-20251017190008-00836.warc.gz) | 270831611 | 362253 |
| 2025-11-12 23:20:07 | https://gruns.co/ | CC-MAIN-2025-47 | [CC-MAIN-20251112221848-20251113011848-00836.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-47/segments/1762439343356.79/warc/CC-MAIN-20251112221848-20251113011848-00836.warc.gz) | 216916874 | 404099 |
| 2024-10-04 17:33:43 | https://huel.com/ | CC-MAIN-2024-42 | [CC-MAIN-20241004164748-20241004194748-00864.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253334.22/warc/CC-MAIN-20241004164748-20241004194748-00864.warc.gz) | 269792150 | 41293 |
| 2021-10-18 00:31:30 | https://hukitchen.com/ | CC-MAIN-2021-43 | [CC-MAIN-20211018000838-20211018030838-00597.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323585186.33/warc/CC-MAIN-20211018000838-20211018030838-00597.warc.gz) | 426082047 | 132234 |
| 2024-10-15 10:36:40 | https://hukitchen.com/ | CC-MAIN-2024-42 | [CC-MAIN-20241015081428-20241015111428-00597.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944255673.65/warc/CC-MAIN-20241015081428-20241015111428-00597.warc.gz) | 263099463 | 68307 |
| 2021-10-23 12:18:04 | https://krispykreme.com/promos/halloween | CC-MAIN-2021-43 | [CC-MAIN-20211023095849-20211023125849-00002.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323585671.36/warc/CC-MAIN-20211023095849-20211023125849-00002.warc.gz) | 453061506 | 15362 |
| 2023-09-23 22:22:12 | https://lemmelive.com/ | CC-MAIN-2023-40 | [CC-MAIN-20230923194908-20230923224908-00172.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233506528.3/warc/CC-MAIN-20230923194908-20230923224908-00172.warc.gz) | 397191095 | 56290 |
| 2024-10-14 06:28:07 | https://lemmelive.com/ | CC-MAIN-2024-42 | [CC-MAIN-20241014040415-20241014070415-00172.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944255399.95/warc/CC-MAIN-20241014040415-20241014070415-00172.warc.gz) | 319352056 | 68962 |
| 2025-10-16 01:11:49 | https://lemmelive.com/ | CC-MAIN-2025-43 | [CC-MAIN-20251015230254-20251016020254-00972.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648659977.75/warc/CC-MAIN-20251015230254-20251016020254-00972.warc.gz) | 359490428 | 85239 |
| 2023-10-04 15:41:49 | https://liquiddeath.com/ | CC-MAIN-2023-40 | [CC-MAIN-20231004152134-20231004182134-00660.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233511386.54/warc/CC-MAIN-20231004152134-20231004182134-00660.warc.gz) | 394229463 | 69405 |
| 2024-10-15 01:07:44 | https://liquiddeath.com/en-mf/collections/halloween | CC-MAIN-2024-42 | [CC-MAIN-20241014225046-20241015015046-00829.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944255525.69/warc/CC-MAIN-20241014225046-20241015015046-00829.warc.gz) | 316218334 | 209797 |
| 2025-10-14 04:27:08 | https://liquiddeath.com/en-uz/collections/halloween | CC-MAIN-2025-43 | [CC-MAIN-20251014025303-20251014055303-00649.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648359062.46/warc/CC-MAIN-20251014025303-20251014055303-00649.warc.gz) | 338617357 | 187649 |
| 2024-10-15 02:44:50 | https://magicspoon.com/ | CC-MAIN-2024-42 | [CC-MAIN-20241015015910-20241015045910-00336.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944255568.89/warc/CC-MAIN-20241015015910-20241015045910-00336.warc.gz) | 334682935 | 81935 |
| 2021-10-16 08:32:55 | https://ritual.com/ | CC-MAIN-2021-43 | [CC-MAIN-20211016074500-20211016104500-00409.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323584554.98/warc/CC-MAIN-20211016074500-20211016104500-00409.warc.gz) | 626440437 | 100192 |
| 2024-10-08 17:52:52 | https://ritual.com/ | CC-MAIN-2024-42 | [CC-MAIN-20241008171352-20241008201352-00589.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253554.4/warc/CC-MAIN-20241008171352-20241008201352-00589.warc.gz) | 438409185 | 80406 |
| 2025-10-09 17:08:36 | https://ritual.com/ | CC-MAIN-2025-43 | [CC-MAIN-20251009162709-20251009192709-00489.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648358466.81/warc/CC-MAIN-20251009162709-20251009192709-00489.warc.gz) | 465168515 | 82286 |
| 2025-11-13 08:25:46 | https://ritual.com | CC-MAIN-2025-47 | [CC-MAIN-20251113072720-20251113102720-00222.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-47/segments/1762439343503.72/warc/CC-MAIN-20251113072720-20251113102720-00222.warc.gz) | 410044217 | 86264 |
| 2024-10-09 07:13:54 | https://seed.com/ | CC-MAIN-2024-42 | [CC-MAIN-20241009054103-20241009084103-00307.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253572.98/warc/CC-MAIN-20241009054103-20241009084103-00307.warc.gz) | 451338599 | 21632 |
| 2022-09-30 21:51:44 | https://skinnydipped.com/ | CC-MAIN-2022-40 | [CC-MAIN-20220930212504-20221001002504-00064.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030335504.37/warc/CC-MAIN-20220930212504-20221001002504-00064.warc.gz) | 570384791 | 66930 |
| 2025-10-18 14:06:57 | https://skinnydipped.com/ | CC-MAIN-2025-43 | [CC-MAIN-20251018123814-20251018153814-00464.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648666508.88/warc/CC-MAIN-20251018123814-20251018153814-00464.warc.gz) | 481763957 | 109348 |
| 2021-10-19 19:14:53 | https://smartsweets.com/ | CC-MAIN-2021-43 | [CC-MAIN-20211019171139-20211019201139-00288.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323585280.84/warc/CC-MAIN-20211019171139-20211019201139-00288.warc.gz) | 703584029 | 64858 |
| 2022-10-06 12:16:25 | https://smartsweets.com/ | CC-MAIN-2022-40 | [CC-MAIN-20221006092601-20221006122601-00448.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030337803.86/warc/CC-MAIN-20221006092601-20221006122601-00448.warc.gz) | 549417157 | 27158 |
| 2023-09-30 04:02:29 | https://smartsweets.com/pages/halloween-giveaway | CC-MAIN-2023-40 | [CC-MAIN-20230930014147-20230930044147-00502.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233510575.93/warc/CC-MAIN-20230930014147-20230930044147-00502.warc.gz) | 560595026 | 64895 |
| 2023-10-01 04:51:10 | https://smartsweets.com/ | CC-MAIN-2023-40 | [CC-MAIN-20231001041719-20231001071719-00648.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233510781.66/warc/CC-MAIN-20231001041719-20231001071719-00648.warc.gz) | 579313940 | 120793 |
| 2024-10-09 01:32:40 | https://smartsweets.com/ | CC-MAIN-2024-42 | [CC-MAIN-20241008232729-20241009022729-00648.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253565.32/warc/CC-MAIN-20241008232729-20241009022729-00648.warc.gz) | 457659964 | 123433 |
| 2024-11-13 13:06:18 | https://smartsweets.com/ | CC-MAIN-2024-46 | [CC-MAIN-20241113103539-20241113133539-00648.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477028347.28/warc/CC-MAIN-20241113103539-20241113133539-00648.warc.gz) | 493664139 | 123285 |
| 2025-10-14 18:54:32 | https://smartsweets.com/products/halloween-lollipops | CC-MAIN-2025-43 | [CC-MAIN-20251014183945-20251014213945-00901.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648359227.51/warc/CC-MAIN-20251014183945-20251014213945-00901.warc.gz) | 481198653 | 98347 |
| 2025-10-14 19:32:32 | https://smartsweets.com/products/halloween-gummy-worms | CC-MAIN-2025-43 | [CC-MAIN-20251014183945-20251014213945-00723.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648359227.51/warc/CC-MAIN-20251014183945-20251014213945-00723.warc.gz) | 507301640 | 79940 |
| 2025-11-19 04:28:46 | https://smartsweets.com/?gspk=SmFpbWVBbGxpc29u&gsxid=lnknCrGRDOwN | CC-MAIN-2025-47 | [CC-MAIN-20251119032929-20251119062929-00809.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-47/segments/1762439657349.95/warc/CC-MAIN-20251119032929-20251119062929-00809.warc.gz) | 412908647 | 116408 |
| 2021-10-26 09:52:08 | https://unrealsnacks.com/collections/unreal-halloween/products/dark-chocolate-coconut-bars-large-1-3oz-bars-12-count | CC-MAIN-2021-43 | [CC-MAIN-20211026072759-20211026102759-00281.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323587854.13/warc/CC-MAIN-20211026072759-20211026102759-00281.warc.gz) | 724971224 | 34054 |
| 2022-09-29 05:54:22 | https://unrealsnacks.com/ | CC-MAIN-2022-40 | [CC-MAIN-20220929034214-20220929064214-00560.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030335304.71/warc/CC-MAIN-20220929034214-20220929064214-00560.warc.gz) | 622507932 | 48686 |
| 2023-09-28 08:50:57 | https://unrealsnacks.com/pages/halloween22 | CC-MAIN-2023-40 | [CC-MAIN-20230928063033-20230928093033-00182.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233510368.33/warc/CC-MAIN-20230928063033-20230928093033-00182.warc.gz) | 644501862 | 42460 |
| 2024-10-14 11:27:32 | https://unrealsnacks.com/ | CC-MAIN-2024-42 | [CC-MAIN-20241014102032-20241014132032-00060.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944255430.85/warc/CC-MAIN-20241014102032-20241014132032-00060.warc.gz) | 497428450 | 38846 |
| 2024-11-04 01:15:57 | https://unrealsnacks.com/ | CC-MAIN-2024-46 | [CC-MAIN-20241104003052-20241104033052-00060.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477027809.13/warc/CC-MAIN-20241104003052-20241104033052-00060.warc.gz) | 572728975 | 37334 |
| 2025-10-16 00:15:45 | https://unrealsnacks.com/ | CC-MAIN-2025-43 | [CC-MAIN-20251015230254-20251016020254-00360.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648659977.75/warc/CC-MAIN-20251015230254-20251016020254-00360.warc.gz) | 555355114 | 61068 |
| 2025-10-17 08:03:07 | https://unrealsnacks.com/collections/halloween-flash-sale/products/dark-chocolate-almond-butter-cups | CC-MAIN-2025-43 | [CC-MAIN-20251017063345-20251017093345-00214.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648665046.80/warc/CC-MAIN-20251017063345-20251017093345-00214.warc.gz) | 557896450 | 89514 |
| 2025-11-07 08:58:44 | https://unrealsnacks.com/?utm_source=aisle&utm_medium=one_free_campaign | CC-MAIN-2025-47 | [CC-MAIN-20251107081817-20251107111817-00327.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-47/segments/1762439342474.62/warc/CC-MAIN-20251107081817-20251107111817-00327.warc.gz) | 481290077 | 60912 |
| 2024-10-10 01:52:52 | https://www.arrae.com/ | CC-MAIN-2024-42 | [CC-MAIN-20241010002016-20241010032016-00218.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253656.81/warc/CC-MAIN-20241010002016-20241010032016-00218.warc.gz) | 583595682 | 95644 |
| 2022-09-30 02:51:18 | https://www.drinkpoppi.com/articles/functional-halloween-mocktail/ | CC-MAIN-2022-40 | [CC-MAIN-20220930020521-20220930050521-00634.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030335424.32/warc/CC-MAIN-20220930020521-20220930050521-00634.warc.gz) | 784544875 | 17274 |
| 2024-10-10 13:43:32 | https://www.forhers.com/?ref=a-fresh.website | CC-MAIN-2024-42 | [CC-MAIN-20241010124812-20241010154812-00534.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253682.6/warc/CC-MAIN-20241010124812-20241010154812-00534.warc.gz) | 694087651 | 130971 |
| 2024-11-11 23:33:51 | https://www.forhers.com/news/healthiest-to-unhealthiest-halloween-candy | CC-MAIN-2024-46 | [CC-MAIN-20241111222353-20241112012353-00676.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477028240.82/warc/CC-MAIN-20241111222353-20241112012353-00676.warc.gz) | 704635813 | 198585 |
| 2025-10-07 21:24:19 | https://www.forhers.com/news/healthiest-to-unhealthiest-halloween-candy | CC-MAIN-2025-43 | [CC-MAIN-20251007202507-20251007232507-00176.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648358303.82/warc/CC-MAIN-20251007202507-20251007232507-00176.warc.gz) | 754561837 | 263104 |
| 2025-10-13 15:20:08 | https://www.forhers.com/ | CC-MAIN-2025-43 | [CC-MAIN-20251013142204-20251013172204-00468.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648358982.27/warc/CC-MAIN-20251013142204-20251013172204-00468.warc.gz) | 746556414 | 139431 |
| 2022-10-03 11:52:48 | https://www.forhims.com/ | CC-MAIN-2022-40 | [CC-MAIN-20221003101805-20221003131805-00307.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030337415.12/warc/CC-MAIN-20221003101805-20221003131805-00307.warc.gz) | 822869203 | 97054 |
| 2023-09-30 13:02:46 | https://www.ghostlifestyle.com/ | CC-MAIN-2023-40 | [CC-MAIN-20230930113949-20230930143949-00859.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233510676.40/warc/CC-MAIN-20230930113949-20230930143949-00859.warc.gz) | 852757226 | 111709 |
| 2024-10-05 03:27:21 | https://www.ghostlifestyle.com/ | CC-MAIN-2024-42 | [CC-MAIN-20241005020917-20241005050917-00859.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253346.35/warc/CC-MAIN-20241005020917-20241005050917-00859.warc.gz) | 705149618 | 69549 |
| 2025-10-16 13:06:26 | https://www.ghostlifestyle.com/ | CC-MAIN-2025-43 | [CC-MAIN-20251016113935-20251016143935-00959.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648663798.77/warc/CC-MAIN-20251016113935-20251016143935-00959.warc.gz) | 700321158 | 67340 |
| 2021-10-23 00:30:24 | https://www.gymshark.com | CC-MAIN-2021-43 | [CC-MAIN-20211023002852-20211023032852-00644.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323585537.28/warc/CC-MAIN-20211023002852-20211023032852-00644.warc.gz) | 914402976 | 90887 |
| 2022-09-29 16:33:13 | https://www.gymshark.com | CC-MAIN-2022-40 | [CC-MAIN-20220929163117-20220929193117-00164.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030335362.18/warc/CC-MAIN-20220929163117-20220929193117-00164.warc.gz) | 836478056 | 87690 |
| 2022-11-27 02:36:18 | https://www.gymshark.com/ | CC-MAIN-2022-49 | [CC-MAIN-20221127005113-20221127035113-00635.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-49/segments/1669446710155.67/warc/CC-MAIN-20221127005113-20221127035113-00635.warc.gz) | 884596955 | 96017 |
| 2023-10-04 23:55:56 | https://www.gymshark.com/ | CC-MAIN-2023-40 | [CC-MAIN-20231004220037-20231005010037-00395.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233511424.48/warc/CC-MAIN-20231004220037-20231005010037-00395.warc.gz) | 845881859 | 75017 |
| 2021-10-27 20:04:05 | https://www.krispykreme.com/ | CC-MAIN-2021-43 | [CC-MAIN-20211027181907-20211027211907-00471.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323588242.22/warc/CC-MAIN-20211027181907-20211027211907-00471.warc.gz) | 1023638304 | 11345 |
| 2023-10-03 13:54:54 | https://www.krispykreme.com/ | CC-MAIN-2023-40 | [CC-MAIN-20231003124522-20231003154522-00651.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233511106.1/warc/CC-MAIN-20231003124522-20231003154522-00651.warc.gz) | 918033887 | 38744 |
| 2024-10-07 11:49:47 | https://www.krispykreme.com/ | CC-MAIN-2024-42 | [CC-MAIN-20241007100838-20241007130838-00651.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253467.23/warc/CC-MAIN-20241007100838-20241007130838-00651.warc.gz) | 720136551 | 42861 |
| 2024-11-05 13:05:08 | https://www.krispykreme.com/ | CC-MAIN-2024-46 | [CC-MAIN-20241105114407-20241105144407-00651.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477027881.88/warc/CC-MAIN-20241105114407-20241105144407-00651.warc.gz) | 804259715 | 39122 |
| 2025-10-16 19:54:41 | https://www.krispykreme.com/ | CC-MAIN-2025-43 | [CC-MAIN-20251016175923-20251016205923-00951.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648664410.92/warc/CC-MAIN-20251016175923-20251016205923-00951.warc.gz) | 787231186 | 24962 |
| 2024-10-16 06:18:18 | https://www.lilys.com/ | CC-MAIN-2024-42 | [CC-MAIN-20241016061231-20241016091231-00402.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944595810.97/warc/CC-MAIN-20241016061231-20241016091231-00402.warc.gz) | 739373772 | 16949 |
| 2025-10-15 14:51:43 | https://www.lilys.com/ | CC-MAIN-2025-43 | [CC-MAIN-20251015133709-20251015163709-00802.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648359357.38/warc/CC-MAIN-20251015133709-20251015163709-00802.warc.gz) | 834844590 | 17752 |
| 2021-10-19 15:42:15 | https://www.myprotein.bg/ | CC-MAIN-2021-43 | [CC-MAIN-20211019140046-20211019170046-00364.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323585270.40/warc/CC-MAIN-20211019140046-20211019170046-00364.warc.gz) | 1083593623 | 89548 |
| 2022-09-28 00:30:58 | https://www.myprotein.bg/ | CC-MAIN-2022-40 | [CC-MAIN-20220927225413-20220928015413-00044.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030335059.31/warc/CC-MAIN-20220927225413-20220928015413-00044.warc.gz) | 945517439 | 118496 |
| 2023-09-27 18:53:55 | https://www.myprotein.bg/ | CC-MAIN-2023-40 | [CC-MAIN-20230927171156-20230927201156-00544.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233510319.87/warc/CC-MAIN-20230927171156-20230927201156-00544.warc.gz) | 983024854 | 117382 |
| 2024-10-14 02:48:39 | https://www.myprotein.bg/ | CC-MAIN-2024-42 | [CC-MAIN-20241014005649-20241014035649-00544.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944255355.53/warc/CC-MAIN-20241014005649-20241014035649-00544.warc.gz) | 782825641 | 115434 |
| 2024-11-07 20:16:55 | https://www.myprotein.bg/ | CC-MAIN-2024-46 | [CC-MAIN-20241107181317-20241107211317-00544.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477028009.81/warc/CC-MAIN-20241107181317-20241107211317-00544.warc.gz) | 852940472 | 115815 |
| 2025-10-11 01:13:44 | https://www.myprotein.bg/ | CC-MAIN-2025-43 | [CC-MAIN-20251010234701-20251011024701-00244.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648358592.53/warc/CC-MAIN-20251010234701-20251011024701-00244.warc.gz) | 866258451 | 102830 |
| 2021-10-28 01:03:06 | https://www.myprotein.com/ | CC-MAIN-2021-43 | [CC-MAIN-20211028003812-20211028033812-00028.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323588246.79/warc/CC-MAIN-20211028003812-20211028033812-00028.warc.gz) | 1060639169 | 139772 |
| 2022-10-03 11:20:16 | https://www.myprotein.com/ | CC-MAIN-2022-40 | [CC-MAIN-20221003101805-20221003131805-00428.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030337415.12/warc/CC-MAIN-20221003101805-20221003131805-00428.warc.gz) | 918340859 | 130730 |
| 2025-11-12 01:41:59 | https://www.myprotein.com/ | CC-MAIN-2025-47 | [CC-MAIN-20251112010046-20251112040046-00828.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-47/segments/1762439343096.76/warc/CC-MAIN-20251112010046-20251112040046-00828.warc.gz) | 748446208 | 177402 |
| 2024-10-15 19:04:48 | https://www.noom.com:443/ | CC-MAIN-2024-42 | [CC-MAIN-20241015174011-20241015204011-00221.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944256311.87/warc/CC-MAIN-20241015174011-20241015204011-00221.warc.gz) | 782709669 | 25713 |
| 2023-10-03 19:50:27 | https://www.olly.com/ | CC-MAIN-2023-40 | [CC-MAIN-20231003192425-20231003222425-00727.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233511220.71/warc/CC-MAIN-20231003192425-20231003222425-00727.warc.gz) | 1004095125 | 111214 |
| 2024-10-08 08:13:29 | https://www.olly.com/ | CC-MAIN-2024-42 | [CC-MAIN-20241008075444-20241008105444-00727.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253528.64/warc/CC-MAIN-20241008075444-20241008105444-00727.warc.gz) | 769442034 | 114870 |
| 2025-10-17 03:50:12 | https://www.olly.com/ | CC-MAIN-2025-43 | [CC-MAIN-20251017032409-20251017062409-00027.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648665010.99/warc/CC-MAIN-20251017032409-20251017062409-00027.warc.gz) | 896527359 | 83523 |
| 2023-09-28 07:30:34 | https://www.oreo.com/ | CC-MAIN-2023-40 | [CC-MAIN-20230928063033-20230928093033-00364.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233510368.33/warc/CC-MAIN-20230928063033-20230928093033-00364.warc.gz) | 992308701 | 31072 |
| 2024-10-07 18:37:46 | https://www.oreo.com/collections/halloween?collection=New+Arrivals | CC-MAIN-2024-42 | [CC-MAIN-20241007162146-20241007192146-00408.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253475.8/warc/CC-MAIN-20241007162146-20241007192146-00408.warc.gz) | 793444835 | 35810 |
| 2025-10-09 12:01:32 | https://www.oreo.com/ | CC-MAIN-2025-43 | [CC-MAIN-20251009100738-20251009130738-00464.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648358434.74/warc/CC-MAIN-20251009100738-20251009130738-00464.warc.gz) | 892710920 | 53124 |
| 2025-11-07 15:52:25 | https://www.oreo.com/halloween | CC-MAIN-2025-47 | [CC-MAIN-20251107142324-20251107172324-00885.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-47/segments/1762439342479.6/warc/CC-MAIN-20251107142324-20251107172324-00885.warc.gz) | 746186550 | 28165 |
| 2021-10-22 06:18:55 | https://yumearth.com/collections/vegan-halloween-candy | CC-MAIN-2021-43 | [CC-MAIN-20211022052742-20211022082742-00032.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323585460.87/warc/CC-MAIN-20211022052742-20211022082742-00032.warc.gz) | 1277893455 | 41237 |
| 2021-10-22 06:39:23 | https://yumearth.com/pages/halloween-bundle-giveaway | CC-MAIN-2021-43 | [CC-MAIN-20211022052742-20211022082742-00204.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323585460.87/warc/CC-MAIN-20211022052742-20211022082742-00204.warc.gz) | 1260647026 | 34462 |
| 2022-09-26 16:15:00 | https://yumearth.com/ | CC-MAIN-2022-40 | [CC-MAIN-20220926144455-20220926174455-00659.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030334912.28/warc/CC-MAIN-20220926144455-20220926174455-00659.warc.gz) | 1166499857 | 34697 |
| 2023-09-22 01:15:12 | https://yumearth.com/ | CC-MAIN-2023-40 | [CC-MAIN-20230922002008-20230922032008-00159.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233506320.28/warc/CC-MAIN-20230922002008-20230922032008-00159.warc.gz) | 1234379052 | 37005 |
| 2023-11-29 02:45:14 | https://yumearth.com/ | CC-MAIN-2023-50 | [CC-MAIN-20231129010302-20231129040302-00159.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-50/segments/1700679100047.66/warc/CC-MAIN-20231129010302-20231129040302-00159.warc.gz) | 1229277577 | 36535 |
| 2024-11-10 21:17:27 | https://yumearth.com/ | CC-MAIN-2024-46 | [CC-MAIN-20241110201420-20241110231420-00159.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477028191.83/warc/CC-MAIN-20241110201420-20241110231420-00159.warc.gz) | 1010913137 | 37564 |
| 2025-10-09 10:53:42 | https://yumearth.com/ | CC-MAIN-2025-43 | [CC-MAIN-20251009100738-20251009130738-00859.warc.gz](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648358434.74/warc/CC-MAIN-20251009100738-20251009130738-00859.warc.gz) | 1049935418 | 40119 |

---

## 1. Did supplement and wellness brands change their websites for Halloween? What exactly changed?

### Takeaway
Almost none of them did. In 147 homepage captures of 20 supplement, wellness and weight-loss brands (83 from late Sep to mid Oct, 64 from Nov–Dec, 2021–2025), I found **no Halloween homepage hero, announcement bar, badge or product renaming** on:
- AG1, Ritual, Olly, Goli, Lemme, Ghost, Hims, Hers, Noom, Arrae, Seed, Cymbiotika, Grüns, Myprotein (UK flagship and Bulgaria), Gymshark, Huel, LMNT, Love Wellness.

The exceptions are small and sit **off the homepage**:
- **Bloom Nutrition**: a dedicated "Witching Hour Sale" collection page with an animated pastel-witch banner, Oct 2024.
- **Hers**: a weight-loss SEO article "23 Halloween Candies Ranked from Healthiest to Unhealthiest" that ends in a weight-loss CTA.
- **Olipop**: an Instagram-only Halloween sweepstakes and a SPOOKY20 code.
- **Myprotein**: Halloween flavours and promo codes (TRICK, a mystery bundle), shown in product naming rather than a site re-skin.

Most of these brands went straight from their evergreen look into Black Friday.

### Cited Findings
**Brands with no Halloween on the homepage [OBSERVED].** The search covered "hallow", "spook", "trick-or-treat", 🎃, 👻 and 🦇 in the full HTML, plus Halloween words in image filenames and alt text. It returned zero hits on every homepage capture of:
- **AG1**:
  - 2021-10-19: hero "Welcome to the Essentialist Nutrition Movement." ([CC 2021-10-19 21:40 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323585281.35/warc/CC-MAIN-20211019202148-20211019232148-00684.warc.gz), offset 209476787)
  - 2022-09-30: hero "The Foundation of Daily Health". ([CC 2022-09-30 00:19 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030335396.92/warc/CC-MAIN-20220929225326-20220930015326-00755.warc.gz), offset 142763759)
  - 2024-10-15: hero "Goodbye Bloat, Hello Energy". ([CC 2024-10-15 09:04 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944255673.65/warc/CC-MAIN-20241015081428-20241015111428-00661.warc.gz), offset 183222979)
  - 2025-10-18: hero "All-in-one nutrition for daily performance". ([CC 2025-10-18 14:02 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648666508.88/warc/CC-MAIN-20251018123814-20251018153814-00161.warc.gz), offset 211909657)
- **Ritual**:
  - 2021-10-16 hero "The future of health— is clear." ([CC 2021-10-16 08:32 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323584554.98/warc/CC-MAIN-20211016074500-20211016104500-00409.warc.gz), offset 626440437)
  - 2024-10-08 hero "Talk fertility to me." ([CC 2024-10-08 17:52 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253554.4/warc/CC-MAIN-20241008171352-20241008201352-00589.warc.gz), offset 438409185)
  - 2025-10-09 hero "For the real body builders". ([CC 2025-10-09 17:08 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648358466.81/warc/CC-MAIN-20251009162709-20251009192709-00489.warc.gz), offset 465168515)
- **Olly**:
  - 2023-10-03: "Everyone Deserves to Have Great Sex". ([CC 2023-10-03 19:50 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233511220.71/warc/CC-MAIN-20231003192425-20231003222425-00727.warc.gz), offset 1004095125)
  - 2024-10-08: "For Every Evolution", plus a "Seasonal Flavors – Get in on the limited edition deliciousness" tile with no Halloween wording. ([CC 2024-10-08 08:13 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253528.64/warc/CC-MAIN-20241008075444-20241008105444-00727.warc.gz), offset 769442034)
  - 2025-10-17: "Choose Science Over Shame". ([CC 2025-10-17 03:50 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648665010.99/warc/CC-MAIN-20251017032409-20251017062409-00027.warc.gz), offset 896527359)
- **Goli**: captures from 2021-10-20, 2022-10-06, 2023-10-01, 2024-10-13 and 2025-10-11. Only free-shipping / "SHOP NOW" bars. ([CC 2021-10-20 01:27 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323585290.83/warc/CC-MAIN-20211019233130-20211020023130-00040.warc.gz), offset 418741915) ([CC 2024-10-13 00:15 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944255020.72/warc/CC-MAIN-20241012235949-20241013025949-00879.warc.gz), offset 239735644) ([CC 2025-10-11 12:30 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648358675.50/warc/CC-MAIN-20251011121535-20251011151535-00279.warc.gz), offset 262730866)
- **Lemme**:
  - 2023-09-23: free-shipping marquee. ([CC 2023-09-23 22:22 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233506528.3/warc/CC-MAIN-20230923194908-20230923224908-00172.warc.gz), offset 397191095)
  - 2024-10-14: "meet lemme GLP-1 Daily™" with a "FREE GIFT ON ALL ORDERS OVER $75" marquee. ([CC 2024-10-14 06:28 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944255399.95/warc/CC-MAIN-20241014040415-20241014070415-00172.warc.gz), offset 319352056)
  - 2025-10-16: "wellness made right". ([CC 2025-10-16 01:11 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648659977.75/warc/CC-MAIN-20251015230254-20251016020254-00972.warc.gz), offset 359490428)
- **Bloom Nutrition** homepage:
  - 2024-10-05 bar: "While supplies last! Spend $100 and get a FREE Tote Bag!" ([CC 2024-10-05 06:25 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253348.29/warc/CC-MAIN-20241005051646-20241005081646-00893.warc.gz), offset 116112840)
  - 2025-10-14 bar: "JUST LAUNCHED: our #1 greens powder, now in a snackable gummy!" ([CC 2025-10-14 13:08 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648359174.55/warc/CC-MAIN-20251014122347-20251014152347-00850.warc.gz), offset 110878817)
- **Ghost**:
  - 2023-09-30 hero "ALL THE FALL THINGS", with Whey Oreo and Cereal Milk product tiles. ([CC 2023-09-30 13:02 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233510676.40/warc/CC-MAIN-20230930113949-20230930143949-00859.warc.gz), offset 852757226)
  - 2024-10-05 "HOT OUT THE OVEN". ([CC 2024-10-05 03:27 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253346.35/warc/CC-MAIN-20241005020917-20241005050917-00859.warc.gz), offset 705149618)
  - 2025-10-16 "CHOC-FULL OF GAINS". ([CC 2025-10-16 13:06 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648663798.77/warc/CC-MAIN-20251016113935-20251016143935-00959.warc.gz), offset 700321158)
  - The ghost-shaped logo is never used for Halloween in these captures.
- **Hims / Hers**:
  - Hers 2024-10-10 hero "Weight loss for your body's unique needs". ([CC 2024-10-10 13:43 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253682.6/warc/CC-MAIN-20241010124812-20241010154812-00534.warc.gz), offset 694087651)
  - Hers 2025-10-13: "Weight loss personalized to you". ([CC 2025-10-13 15:20 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648358982.27/warc/CC-MAIN-20251013142204-20251013172204-00468.warc.gz), offset 746556414)
  - Hims 2022-10-03: "Personalized, doctor-backed treatment plans". ([CC 2022-10-03 11:52 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030337415.12/warc/CC-MAIN-20221003101805-20221003131805-00307.warc.gz), offset 822869203)
- **Noom**: 2024-10-15 hero "Trusted, proven, sustainable weight loss". ([CC 2024-10-15 19:04 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944256311.87/warc/CC-MAIN-20241015174011-20241015204011-00221.warc.gz), offset 782709669)
- **Arrae** (2021, 2023, 2024, 2025), **Seed** (2021–2025), **Huel** (2021–2025) and **LMNT** (2021–2025): evergreen heroes.
  - ([CC 2024-10-10 01:52 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253656.81/warc/CC-MAIN-20241010002016-20241010032016-00218.warc.gz), offset 583595682) ([CC 2024-10-09 07:13 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253572.98/warc/CC-MAIN-20241009054103-20241009084103-00307.warc.gz), offset 451338599) ([CC 2024-10-04 17:33 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253334.22/warc/CC-MAIN-20241004164748-20241004194748-00864.warc.gz), offset 269792150) ([CC 2024-10-11 01:39 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253749.74/warc/CC-MAIN-20241011011611-20241011041611-00121.warc.gz), offset 189409290)
- **Cymbiotika**: 2025-10-17 bar "Free shipping sitewide", with leftover LABOR25/LABOR20 codes. ([CC 2025-10-17 18:14 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648665632.70/warc/CC-MAIN-20251017160008-20251017190008-00280.warc.gz), offset 200590811)
- **Grüns** 2025-10-17 bar: "🍏 Grünny Smith Apple is here! Get our new limited-edition flavor before it's gone! 🍏". A fall flavour, not Halloween. ([CC 2025-10-17 16:47 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648665632.70/warc/CC-MAIN-20251017160008-20251017190008-00836.warc.gz), offset 270831611)
- **Gymshark**:
  - 2021-10-23 "Power" ([CC 2021-10-23 00:30 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323585537.28/warc/CC-MAIN-20211023002852-20211023032852-00644.warc.gz), offset 914402976)
  - 2022-09-29 "NEW ADAPT ANIMAL REEF" ([CC 2022-09-29 16:33 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030335362.18/warc/CC-MAIN-20220929163117-20220929193117-00164.warc.gz), offset 836478056)
  - 2023-10-04 "Train like the greats with Heritage" ([CC 2023-10-04 23:55 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233511424.48/warc/CC-MAIN-20231004220037-20231005010037-00395.warc.gz), offset 845881859)
- **Myprotein (myprotein.com, the UK flagship)**: 2021-10-28, 2022-10-03 ("35% off Best Sellers | Use code: BEST"), 2023-09-25, 2024-10-13 and 2025-10-16. ([CC 2021-10-28 01:03 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323588246.79/warc/CC-MAIN-20211028003812-20211028033812-00028.warc.gz), offset 1060639169) ([CC 2022-10-03 11:20 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030337415.12/warc/CC-MAIN-20221003101805-20221003131805-00428.warc.gz), offset 918340859)
- **Myprotein Bulgaria (myprotein.bg)**, all in Bulgarian:
  - 2021-10-19 "30% ОТСТЪПКА | КОД: 30BG" ([CC 2021-10-19 15:42 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323585270.40/warc/CC-MAIN-20211019140046-20211019170046-00364.warc.gz), offset 1083593623)
  - 2022-09-28 "35% ОТСТЪПКА | КОД: 35BG" ([CC 2022-09-28 00:30 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030335059.31/warc/CC-MAIN-20220927225413-20220928015413-00044.warc.gz), offset 945517439)
  - 2023-09-27 "30% НА ПОЧТИ ВСИЧКО | КОД: MYPBG" ([CC 2023-09-27 18:53 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233510319.87/warc/CC-MAIN-20230927171156-20230927201156-00544.warc.gz), offset 983024854)
  - 2024-10-14 "35% ОТСТЪПКА | КОД: MYPBG" ([CC 2024-10-14 02:48 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944255355.53/warc/CC-MAIN-20241014005649-20241014035649-00544.warc.gz), offset 782825641)
  - 2025-10-11. ([CC 2025-10-11 01:13 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648358592.53/warc/CC-MAIN-20251010234701-20251011024701-00244.warc.gz), offset 866258451)
  - No Halloween wording or imagery appears in any of these.

**Bloom Nutrition "Witching Hour Sale", the closest analogue to FitPatches [OBSERVED].**
- Live on `bloomnu.com/collections/halloween-sale`. Captured 2024-11-02 08:05 UTC, two days after Halloween and still up. ([CC 2024-11-02 09:05 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477027709.8/warc/CC-MAIN-20241102071948-20241102101948-00823.warc.gz), offset 125991943)
- Banner: an animated GIF, 1920×444 desktop and 789×500 mobile. The file was uploaded 29 Oct 2024 (v=1730222824).
- Copy: "WITCHING HOUR SALE / up to 25% OFF assorted treats / *Discount automatically applied at checkout".
- Visual: Bloom's own pastel pink → mint-green gradient, soft pink smoke and clouds, iridescent bubbles. Bloom tubs float out of a smoking cauldron. A two-frame loop swaps a pink sheer-gloved hand for a green witch hand.
- Typeface: a dark-green "witchy" display serif.
- The same day's homepage carried no Halloween reference. ([CC 2024-11-02 08:34 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477027709.8/warc/CC-MAIN-20241102071948-20241102101948-00893.warc.gz), offset 124601473)

**Hers (weight-loss telehealth) Halloween content [OBSERVED].**
- Article: "23 Halloween Candies Ranked from Healthiest to Unhealthiest", published 10/09/2024 and reviewed by an obesity-medicine MD. Live in Nov 2024 and Oct 2025. ([CC 2025-10-07 21:24 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648358303.82/warc/CC-MAIN-20251007202507-20251007232507-00176.warc.gz), offset 754561837) ([CC 2024-11-11 23:33 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477028240.82/warc/CC-MAIN-20241111222353-20241112012353-00676.warc.gz), offset 704635813)
- It frames candy as unavoidable, not forbidden. Section titles: "How to Enjoy a Healthy Halloween" and "Halloween Treats Don't Have to Haunt You".
- It gives blood-sugar advice: "Pair candy with fiber… helping to slow absorption of sugar".
- It ends with: "Get more guidance on how to reach your health goals through Halloween and beyond. Get a free consultation…", next to "View weight loss medications" CTAs.

**Olipop [OBSERVED].**
- The homepage never went Halloween:
  - 2021-10-21 ([CC 2021-10-21 19:08 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323585439.59/warc/CC-MAIN-20211021164535-20211021194535-00127.warc.gz), offset 328263091)
  - 2022-10-07 ([CC 2022-10-07 01:55 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030337906.7/warc/CC-MAIN-20221007014029-20221007044029-00047.warc.gz), offset 267865043)
  - 2023-09-27 ([CC 2023-09-27 22:27 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233510326.82/warc/CC-MAIN-20230927203115-20230927233115-00052.warc.gz), offset 243314378)
  - 2024-10-14 ([CC 2024-10-14 17:17 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944255489.84/warc/CC-MAIN-20241014163540-20241014193540-00052.warc.gz), offset 182127838)
  - 2025-10-13: a SpongeBob takeover. ([CC 2025-10-13 12:37 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648358967.31/warc/CC-MAIN-20251013111241-20251013141241-00552.warc.gz), offset 190121391)
- 2024: an "OLIPOP Halloween Sweepstakes" ran on Instagram, 11–15 Oct 2024. Prize: two one-of-a-kind Olipop can costumes, ARV $1,580 each. The site also had an auto-apply code "SPOOKY20". ([CC 2024-11-13 18:40 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477028387.69/warc/CC-MAIN-20241113171551-20241113201551-00079.warc.gz), offset 195100077)
- A dietitian-written blog post, "Keeping Your Gut Healthy During a Sugar-Filled Holiday: A Parents Survival Guide to Halloween", was live in 2022 and 2023. ([CC 2022-10-07 04:05 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030337906.7/warc/CC-MAIN-20221007014029-20221007044029-00791.warc.gz), offset 272594263)

**Poppi [OBSERVED].**
- Homepage: no Halloween in 2021, 2022, 2023, 2024 or 2025. ([CC 2024-10-15 22:48 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944591543.93/warc/CC-MAIN-20241015204737-20241015234737-00298.warc.gz), offset 178513147) ([CC 2025-10-13 12:53 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648358967.31/warc/CC-MAIN-20251013111241-20251013141241-00098.warc.gz), offset 199971808)
- A 2022 recipe page, "Functional Halloween Mocktail", used a lab beaker and a syringe of grenadine "for an extra spooky effect" and the line "Witch, please!". ([CC 2022-09-30 02:51 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030335424.32/warc/CC-MAIN-20220930020521-20220930050521-00634.warc.gz), offset 784544875)

**Myprotein's Halloween lives in product names and codes [PRESS].**
- 2020: "Trick or Treat" Impact Whey flavour. [Stack3d](https://www.stack3d.com/2020/10/myprotein-trick-or-treat-impact-whey-protein/)
- 2021: Halloween "Blood Orange" Clear Whey with code TRICK for 40–50% off. [Stack3d](https://www.stack3d.com/2021/10/myprotein-halloween-blood-orange-clear-whey-isolate/)
- A "Halloween Mystery Bundle" (2×500 g Impact Whey, mystery flavours) was indexed on myprotein.bg at €23.99. [myprotein.bg listing via search](https://www.myprotein.bg/p/sports-nutrition/halloween-mystery-bundle/12666671)
  - That URL returned 404 when I checked today, so the date is unknown.

**Live check today (2026-10-25, a week before Halloween) [OBSERVED].** Homepages were screenshotted with JavaScript on and their visible text searched. No Halloween wording on:
- Olipop, Poppi, Bloom, Goli, Olly, Ritual, Noom, Lemme, Grüns, Cymbiotika, Myprotein BG, Gymshark.

AG1 and Hers served bot-check pages. See section 4 and the `health_LIVE_2026-10-25_*` files.

### Inferences
- The category norm for **supplement/weight-loss brands is "do nothing on the homepage"**. For a brand that sells weight or blood-sugar control, a candy holiday sits awkwardly. The brands that engaged did it with **content** (Hers' candy ranking, Olipop's gut-health guide) or a **sale page** (Bloom). A full re-skin was not used.
- That leaves a gap: in this category, a tasteful Halloween treatment will stand out, because peers are visually silent.
- Bloom's banner is the strongest template for FitPatches:
  - a women-targeted wellness brand;
  - a pink-dominant palette kept intact;
  - Halloween carried by props (cauldron, witch hand, smoke, bubbles) and a display font;
  - a sale angle ("Witching Hour") that does not glorify candy;
  - a tiny two-frame GIF for motion.

### Gaps
- No captures from the last week of October for 2022–2025, so a homepage that went Halloween only after about 16 October cannot be ruled out for any brand. The Bloom sale shows that late-October-only pages exist.
- Goli, Olly, Noom and Hers were checked from server HTML only. Their client-rendered hero banners could contain Halloween imagery that is invisible in static HTML.
- No evidence was found about Sugarbear, AG1, Ritual or Seed emails, which may have carried Halloween themes even when the site did not.

---

## 2. How did better-for-you and low-sugar food/drink brands frame Halloween visually without contradicting their health message?

### Takeaway
The low-sugar candy brands (SmartSweets, Unreal, YumEarth) went all-in **every year**. They used one consistent rhetorical trick: **make sugar the monster, and the product the safe treat**. Examples:
- "Sugar is spooky. But candy doesn't have to be!"
- "spooky good! (no spooky ingredients)"
- "all treats, no tricks."

Visually they **kept their core packaging and colours** and added a thin Halloween layer: shadow hands, bats, cobwebs, smoke, a cute ghost mascot, an orange/purple accent. Imagery stayed **playful, not gory**. Brands whose identity is "healthy alternative" without candy (Lily's, Hu, Olipop, Poppi, Magic Spoon) mostly chose **autumn/pumpkin-spice** visuals rather than Halloween.

### Cited Findings
**SmartSweets (low-sugar candy, brand pink) [OBSERVED].**
- **2021-10-19 homepage** ([CC 2021-10-19 19:14 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323585280.84/warc/CC-MAIN-20211019171139-20211019201139-00288.warc.gz), offset 703584029):
  - Hero copy: "Kick Sugar Keep Candy™ – This Spooky Szn, Build a Box with your fav sweet and sour candy flavors with up to 92% less sugar."
  - Hero image (`HEADER-CG-USA-1_desktop`): an orange set with cobwebs and the black shadow of a clawed hand reaching into a box of pouches.
  - Every product tile was swapped to a Halloween version (`USA-3B-HALLOWEEN-2021_GRID_*.png`). Each is the normal pouch photo with **one small grey bat silhouette added**.
- **2022-10-06** ([CC 2022-10-06 12:16 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030337803.86/warc/CC-MAIN-20221006092601-20221006122601-00448.warc.gz), offset 549417157):
  - Menu feature: "Shop Our Limited Edition Halloween Build a Box 👻🎃".
  - Halloween Build-a-Box tile with the same shadow-hand and bat motif (`USA-3B-HALLOWEEN-2022_GRID.png`).
  - The main hero was a Caramels launch, not Halloween.
- **2023-09-30**: `/collections/halloween` and `/pages/halloween-giveaway` already existed, but the homepage on 2023-10-01 was still evergreen. ([CC 2023-09-30 04:02 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233510575.93/warc/CC-MAIN-20230930014147-20230930044147-00502.warc.gz), offset 560595026) ([CC 2023-10-01 04:51 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233510781.66/warc/CC-MAIN-20231001041719-20231001071719-00648.warc.gz), offset 579313940)
- **2024-10-09 homepage** ([CC 2024-10-09 01:32 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253565.32/warc/CC-MAIN-20241008232729-20241009022729-00648.warc.gz), offset 457659964):
  - Announcement bar: "Build a #KickSugar Halloween candy box".
  - Hero headline is an inline SVG in purple #4c0185: "BRINGING CANDY BACK TO LIFE".
  - Body copy: "Sugar is spooky. But candy doesn't have to be! We're bringing candy back to life with Halloween candy you can actually feel good about." Then a "Shop Now" button.
  - Hero image (uploaded 24 Sep 2024): the regular pastel pouches over a smoky black panel with cobwebs.
  - The markup includes `data-animation="PositionedCandy"` elements: rotated candy pieces positioned around the hero and animated in. This is motion without a re-skin.
- **2025-10-14** ([CC 2025-10-14 19:32 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648359227.51/warc/CC-MAIN-20251014183945-20251014213945-00723.warc.gz), offset 507301640) ([CC 2025-10-14 18:54 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648359227.51/warc/CC-MAIN-20251014183945-20251014213945-00901.warc.gz), offset 481198653):
  - Announcement bar: "NEW: Spooky Halloween Lollipops are here for a limited time!"
  - Nav: "Shop by candy type → Halloween".
  - Gummy Worms PDP: "Creepy-crawly and wickedly fun… Feel Good About Candy™ 2g Sugar Per 35g Bag".
  - Lollipops PDP: "A spooky spin on a classic… 88% less sugar".
  - A "Sour Zombie Buddies" SKU.
- **[PRESS] 2025 retail packs**: Halloween Gummy Worms and Sour Zombie Buddies at Target, with lollipops in "Boo Raspberry" and "Watermelon Brew". [Nosh / SmartSweets PR via search](https://www.nosh.com/pr/2025/10/02/smartsweets-releases-the-lowsugar-halloween-candy-youve-been-screaming-for); [Well.ca listing](https://well.ca/products/smartsweets-halloween-lollipops_327817.html?cat=6859)

**Unreal (lower-sugar chocolate) [OBSERVED].**
- **2021-10-26**: a `/collections/unreal-halloween` collection with Halloween 2-box SKUs. ([CC 2021-10-26 09:52 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323587854.13/warc/CC-MAIN-20211026072759-20211026102759-00281.warc.gz), offset 724971224)
- **2022-09-29**: homepage product grid switched to "halloween coconut bars – 2 boxes" and "halloween peanut butter cups – 2 boxes". The box art keeps the white UNREAL logo on purple or orange, with black bats and a haunted-house silhouette. A `/collections/trick-or-treat` page existed. ([CC 2022-09-29 05:54 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030335304.71/warc/CC-MAIN-20220929034214-20220929064214-00560.warc.gz), offset 622507932)
- **2023-09-28**: landing page `/pages/halloween22` ([CC 2023-09-28 08:50 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233510368.33/warc/CC-MAIN-20230928063033-20230928093033-00182.warc.gz), offset 644501862):
  - Headline "all treats, no tricks."; sub-line "free shipping on orders $30+ / order by oct 25 to get in time for halloween".
  - Section "halloween must haves".
  - Copy: "You already chose natural chocolate for yourself, it's time to share the goodness this halloween!"
  - Rendered: spiders, mini pumpkins and cobweb on white, products in a trick-or-treat bag.
- **2024-10-14 homepage** ([CC 2024-10-14 11:27 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944255430.85/warc/CC-MAIN-20241014102032-20241014132032-00060.warc.gz), offset 497428450):
  - Full Halloween hero: h1 "spooky good!" over h2 "(no spooky ingredients)".
  - Orange set with shadow zombie hands (asset uploaded 19 Sep 2024).
  - CTAs "shop all snacks" and "build your box & save!".
  - Next band: "snatch up your halloween treats, before it's too late!"
- **2025-10-16/17** ([CC 2025-10-16 00:15 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648659977.75/warc/CC-MAIN-20251015230254-20251016020254-00360.warc.gz), offset 555355114) ([CC 2025-10-17 08:03 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648665046.80/warc/CC-MAIN-20251017063345-20251017093345-00214.warc.gz), offset 557896450):
  - Homepage hero NOT Halloween.
  - Halloween variety packs in the grid; collections `/collections/halloween-flash-sale` and `/collections/spooky-savings`.
  - Product tile art: a cute white cartoon ghost mascot hugging a bag (`GhostPDP-f6-homepage_v2.png`, uploaded 5 Sep 2025).
- **[PRESS] 2025 packaging**: "new mascots and formats designed to support trial and increase basket size". Dye-free positioning. Retail from 1 Sep 2025, DTC from 15 Sep 2025. [Candy Industry / Snack & Bakery](https://www.snackandbakery.com/articles/114415-unreal-reveals-dye-free-halloween-candy-lineup)
- **[PRESS] Positioning**: Unreal uses "fun, colorful branding" but is "not looking to market directly to kids". Its messaging targets parents. [Modern Retail, 24 Oct 2024](https://www.modernretail.co/marketing/better-for-you-candy-brands-are-going-all-in-on-halloween/)

**YumEarth (allergy-friendly organic candy) [OBSERVED].**
- **2021-10-22**: `/collections/vegan-halloween-candy` and a `/pages/halloween-bundle-giveaway`. ([CC 2021-10-22 06:18 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323585460.87/warc/CC-MAIN-20211022052742-20211022082742-00032.warc.gz), offset 1277893455) ([CC 2021-10-22 06:39 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323585460.87/warc/CC-MAIN-20211022052742-20211022082742-00204.warc.gz), offset 1260647026)
- **2022-09-26** ([CC 2022-09-26 16:15 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030334912.28/warc/CC-MAIN-20220926144455-20220926174455-00659.warc.gz), offset 1166499857):
  - h1 "Spooktacular Treats are Here!"; sub-line "the perfect allergy friendly candy for all Halloween occasions! top 9 free • no artificial dyes • safe for the classroom".
  - Lime/yellow banner with bats.
- **2023-09-22** ([CC 2023-09-22 01:15 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233506320.28/warc/CC-MAIN-20230922002008-20230922032008-00159.warc.gz), offset 1234379052):
  - Teal hero "Delicious Allergy Friendly Treats! Enjoy for all your Halloween Festivities!".
  - Photo of costumed kids holding a teal pumpkin bucket.
  - Pumpkin-silhouette packaging.
- **2025-10-09** ([CC 2025-10-09 10:53 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648358434.74/warc/CC-MAIN-20251009100738-20251009130738-00859.warc.gz), offset 1049935418):
  - h1 "New Halloween Choco Yums!"; sub-line "allergy-friendly • no artificial dyes • classroom safe".
  - Announcement bar: "Save $8! NEW Bundle! Halloween Sour Littles 15ct (2), Choco Yums 5ct (2), and Halloween Gummy Fruits (1) code: SPOOKYBUNDLE. Ends 10/10!"

**Feastables (MrBeast chocolate, "simple ingredients") [OBSERVED].**
- **2024-10-08 homepage** ([CC 2024-10-08 08:32 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253528.64/warc/CC-MAIN-20241008075444-20241008105444-00790.warc.gz), offset 212968326):
  - Hero "THIS HALLOWEEN, YOU COULD WIN CASH ALL MONTH LONG – $10,000 USD DAILY WINNER – ENTER WITH PURCHASE THROUGH OCTOBER 30TH / $1,000,000 USD GRAND PRIZE WINNER – ENTER ON HALLOWEEN DAY".
  - Bats and a graveyard; nav category "Halloween".
- **2025-10-17** ([CC 2025-10-17 13:24 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648665304.94/warc/CC-MAIN-20251017125300-20251017155300-00590.warc.gz), offset 216373078) ([CC 2025-10-17 13:55 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648665304.94/warc/CC-MAIN-20251017125300-20251017155300-00004.warc.gz), offset 226030662):
  - Homepage hero not Halloween.
  - Grid includes "Halloween Jack-O-Lantern Cups $39.99" and "Halloween Snack-Size Variety Bag $49.99".
  - Separate `/pages/halloween-sweepstakes`: purple hypno-swirl with an orange frame, "HALLOWEEN SWEEPS… SCARY GOOD PRIZES". Ran 9/15/25–10/15/25, entry by receipt upload or QR code on pack.
  - Footer background `footer-bg-hwn` is an orange wavy ripple.

**Magic Spoon (keto cereal) [OBSERVED].** Only an announcement-bar line, 2024-10-15: "Limited: Pumpkin Spice & Salted Carmel🍂🎃". No other Halloween. ([CC 2024-10-15 02:44 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944255568.89/warc/CC-MAIN-20241015015910-20241015045910-00336.warc.gz), offset 334682935)

**Lily's (no-sugar-added sweets) [OBSERVED].**
- 2024-10-16 hero "Sweeten Your Expectations" (no Halloween). ([CC 2024-10-16 06:18 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944595810.97/warc/CC-MAIN-20241016061231-20241016091231-00402.warc.gz), offset 739373772)
- 2025-10-15 hero "Discover Fall Sweetness with No Added Sugar" / "Fall for Sweets with No Added Sugar", with an image of muffins, cinnamon sticks and autumn leaves. ([CC 2025-10-15 14:51 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648359357.38/warc/CC-MAIN-20251015133709-20251015163709-00802.warc.gz), offset 834844590)
- Fall, not Halloween.

**Hu Kitchen [OBSERVED].**
- 2021-10-18 hero "chocolate, spice & everything nice." Rust velvet backdrop for a Pumpkin Spice bar; announcement code "FALLFORHU". ([CC 2021-10-18 00:31 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323585186.33/warc/CC-MAIN-20211018000838-20211018030838-00597.warc.gz), offset 426082047)
- 2022–2025: no Halloween. ([CC 2024-10-15 10:36 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944255673.65/warc/CC-MAIN-20241015081428-20241015111428-00597.warc.gz), offset 263099463)

**SkinnyDipped [OBSERVED].** No Halloween on homepage captures of 2022-09-30, 2023-10-04 and 2025-10-18. ([CC 2022-09-30 21:51 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030335504.37/warc/CC-MAIN-20220930212504-20221001002504-00064.warc.gz), offset 570384791) ([CC 2025-10-18 14:06 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648666508.88/warc/CC-MAIN-20251018123814-20251018153814-00464.warc.gz), offset 481763957)
- [PRESS] It marketed Halloween through retail and influencers, saying Halloween "has typically performed strongly". [Modern Retail](https://www.modernretail.co/marketing/better-for-you-candy-brands-are-going-all-in-on-halloween/)

**Liquid Death [OBSERVED].** Its brand is permanently "horror". Halloween is a merch category, not a site change.
- Nav "HALLOWEEN" merch on 2023-10-04, with "DON'T BE SCARED. IT'S JUST WATER." and "STEVE-O VOODOO DOLL" tiles. ([CC 2023-10-04 15:41 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233511386.54/warc/CC-MAIN-20231004152134-20231004182134-00660.warc.gz), offset 394229463)
- "Killer Halloween Collection" collection on 2024-10-15 and 2025-10-14. ([CC 2024-10-15 01:07 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944255525.69/warc/CC-MAIN-20241014225046-20241015015046-00829.warc.gz), offset 316218334) ([CC 2025-10-14 04:27 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648359062.46/warc/CC-MAIN-20251014025303-20251014055303-00649.warc.gz), offset 338617357)
- [PRESS] Oct 2022: Martha Stewart "Dismembered Moments" severed-hand candle, $58, sold on Martha.com with an Oct 20 ship-by. [Apartment Therapy](https://www.apartmenttherapy.com/martha-stewart-liquid-death-candle-37142573)

**Krispy Kreme (full-takeover reference) [OBSERVED].**
- **2021**:
  - The 2021-10-27 homepage carousel was wholly Halloween: "Order our Limited Edition Halloween Dozen today!" (purple sky, cauldron, "Spellbook" box), "Saturday Scary Sharies $1 Dozen code SCARY", and "Send a spooky gift!". ([CC 2021-10-27 20:04 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323588242.22/warc/CC-MAIN-20211027181907-20211027211907-00471.warc.gz), offset 1023638304)
  - `/promos/halloween` "We Are Krispy Skreme… Now thru Halloween": Bewitched Broomstick, Abra Cat Dabra, Enchanted Cauldron, Spooky Sprinkle. ([CC 2021-10-23 12:18 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323585671.36/warc/CC-MAIN-20211023095849-20211023125849-00002.warc.gz), offset 453061506)
- **2023-10-03**: pumpkin spice and apple fritters only, no Halloween yet. ([CC 2023-10-03 13:54 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233511106.1/warc/CC-MAIN-20231003124522-20231003154522-00651.warc.gz), offset 918033887)
- **2024-10-07**: "Explore the Ghostbusters Collection" plus "Bring Ghostbusters to Your Party… spooky gathering". ([CC 2024-10-07 11:49 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253467.23/warc/CC-MAIN-20241007100838-20241007130838-00651.warc.gz), offset 720136551)
- **2025-10-16**: hero "Krispy Kreme Halloween Trick or Treat! Collection". Purple and orange, a cute paper ghost and jack-o-lantern, haunted-house steps. Plus "GET KRISPY KREME HALLOWEEN DOUGHNUTS – CATERED". ([CC 2025-10-16 19:54 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648664410.92/warc/CC-MAIN-20251016175923-20251016205923-00951.warc.gz), offset 787231186)

**Oreo [OBSERVED].**
- 2023: "Halloween" was a gifting nav category alongside Birthday, Holidays, Pride and Wedding. ([CC 2023-09-28 07:30 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233510368.33/warc/CC-MAIN-20230928063033-20230928093033-00364.warc.gz), offset 992308701)
- 2024-10-07: `/collections/halloween` (15 products). ([CC 2024-10-07 18:37 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253475.8/warc/CC-MAIN-20241007162146-20241007192146-00408.warc.gz), offset 793444835)
- 2025-10-09 homepage module "GET IN THE SPIRIT": OREOiD Full Moon Halloween and Halloween Spider boxes (navy/purple, orange "BOO!", jack-o-lantern and spider prints). ([CC 2025-10-09 12:01 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648358434.74/warc/CC-MAIN-20251009100738-20251009130738-00464.warc.gz), offset 892710920)
- `/halloween` copy: "It's time to get in the spirit. Our spidey senses say you should probably stock up…". ([CC 2025-11-07 15:52 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-47/segments/1762439342479.6/warc/CC-MAIN-20251107142324-20251107172324-00885.warc.gz), offset 746186550)

### Inferences
- **Proven framing for "healthy" brands.** Turn the scare onto the thing you replace. "Sugar is spooky", "no spooky ingredients", "all treats, no tricks", "treats don't have to haunt you". This flatters the customer's health choice instead of contradicting it.
  - For FitPatches, the equivalent villain is the **sugar spike / cravings**, never the customer's body.
- **Keep the product shot and brand colour; add one or two motifs.** SmartSweets added just a bat to each tile. Unreal kept its logo and added bats and shadow hands. Bloom kept pink and mint. This keeps recognition and conversion assets intact.
- **Cute beats gory.** The scariest element used by any health or BFY brand was a shadow hand; the rest were bats, cobwebs, cute ghosts and pumpkins. Liquid Death is the only "dark" brand, and it is dark all year.
- Brands with no Halloween product either chose a **fall/autumn** look (Lily's, Hu, Magic Spoon, Grüns) or did nothing. For a patch brand without a Halloween SKU, "seasonal bundle + light Halloween accents" is the natural middle path.

### Gaps
- No direct capture of the SmartSweets or Unreal homepage in the final week of October 2022–2025, so peak intensity (e.g., announcement-bar countdowns) is unknown.
- Poppi's and Olipop's Halloween social and email creative was not retrievable (Milled blocked).

---

## 3. Which visual tone worked for health brands (cute/cosy vs dark/scary vs playful)? Did they keep core colours or fully re-skin?

### Takeaway
**Playful-cute won, and nobody in health/BFY fully re-skinned.** Across every Halloween treatment observed, the brands:
- kept their logo and core palette;
- used **orange and/or purple as accents**, or backgrounds on one hero only;
- added a small set of motifs: bat, cobweb, shadow hand, smoke/cauldron, pumpkin, cute ghost.

Full takeovers (deep purple sky, cauldrons, spellbooks across the whole carousel) appear only at indulgence brands such as Krispy Kreme and Oreo.

### Cited Findings
**Colour behaviour [OBSERVED].**
- SmartSweets kept its multicolour pastel pouches in every year and added black/grey smoke and white cobwebs (2024) or an orange set (2021). The CTA and headline used its brand purple #4c0185. ([CC 2024-10-09 01:32 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944253565.32/warc/CC-MAIN-20241008232729-20241009022729-00648.warc.gz), offset 457659964)
- Unreal kept its white logo and used **orange as the full hero background** (2024), with purple and orange boxes. ([CC 2024-10-14 11:27 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-42/segments/1727944255430.85/warc/CC-MAIN-20241014102032-20241014132032-00060.warc.gz), offset 497428450)
- Bloom kept its **pastel pink + mint** gradient. The only Halloween colours were dark-green type and the green witch hand. ([CC 2024-11-02 09:05 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477027709.8/warc/CC-MAIN-20241102071948-20241102101948-00823.warc.gz), offset 125991943)
- YumEarth kept its teal/lime/orange brand palette; Halloween came through product packs and photos. ([CC 2023-09-22 01:15 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233506320.28/warc/CC-MAIN-20230922002008-20230922032008-00159.warc.gz), offset 1234379052)
- Krispy Kreme used a near-total purple/orange re-skin of carousel creative (2021, 2025). ([CC 2021-10-27 20:04 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323588242.22/warc/CC-MAIN-20211027181907-20211027211907-00471.warc.gz), offset 1023638304) ([CC 2025-10-16 19:54 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648664410.92/warc/CC-MAIN-20251016175923-20251016205923-00951.warc.gz), offset 787231186)

**Motif inventory [OBSERVED].**

| Motif | Where |
|---|---|
| Bat silhouettes | SmartSweets 2021–22 tiles; Unreal packs; Feastables 2024; YumEarth 2022 |
| Cobwebs | SmartSweets 2021 and 2024; Unreal 2023 |
| Shadow "claw" hands | SmartSweets 2021–22; Unreal 2024 |
| Smoke / cauldron | Bloom 2024; Krispy Kreme 2021; SmartSweets 2024 |
| Cute ghost | Unreal 2025 mascot; Krispy Kreme 2025 paper ghost |
| Pumpkins / jack-o-lanterns | Unreal 2023; Feastables 2025 cups; Oreo 2025; Krispy Kreme 2025 |
| Costumed kids / teal pumpkin | YumEarth 2023 |
| Witch hand | Bloom 2024 |

**Typography [OBSERVED].**
- Rounded friendly sans in lowercase: Unreal "spooky good!".
- Condensed poster caps: SmartSweets "BRINGING CANDY BACK TO LIFE".
- A witchy display serif: Bloom "WITCHING HOUR SALE".
- Script: Krispy Kreme "Halloween Dozen".
- Nobody used dripping-blood or horror lettering.

**Motion [OBSERVED].**
- Bloom: a two-frame GIF banner.
- SmartSweets 2024: animated positioned candy pieces (`data-animation="PositionedCandy"`).
- Magic Spoon: emoji in a scrolling announcement bar ("🍂🎃").

**Copy tone [OBSERVED].** Puns and reassurance, not fear:
- "Spooktacular Treats" (YumEarth)
- "This Spooky Szn" (SmartSweets)
- "all treats, no tricks." (Unreal)
- "Witching Hour Sale" (Bloom)
- "scary good prizes" (Feastables)
- "Halloween Treats Don't Have to Haunt You" (Hers)

**[PRESS] Audience.** Unreal targets parents, not kids. SkinnyDipped's core customers are "health-conscious adults seeking a guilt-free indulgence", who buy "for self-treating around Halloween". [Modern Retail](https://www.modernretail.co/marketing/better-for-you-candy-brands-are-going-all-in-on-halloween/)

### Inferences
**Pattern catalogue for fitpatches.net**, ranked by evidence strength and fit for a pink, women 30–55, blood-sugar/weight brand:
1. **Keep the pink, add a witchy accent (the Bloom model).** Pink #d64d87 → a soft pastel gradient, with one accent such as deep aubergine/purple text or a small mint/green witch-hand detail. Bloom shows pink and Halloween can coexist without orange.
2. **Villain = sugar/cravings, hero = the patch.** Bulgarian lines in the "Sugar is spooky / no spooky ingredients" pattern, e.g. "Страшни са само захарните пикове" ("Only the sugar spikes are scary"), or "Сладко без страшни последствия" ("Sweet without the scary consequences"). Pair with Hers-style tips: "pair sweets with fibre", "plan your treats".
3. **Light-touch product-tile overlay.** Add one small bat, ghost or cobweb corner to the existing product images, as SmartSweets 2021 did. This is cheap, reversible, and keeps conversion photography intact.
4. **One themed hero or collection page, not a whole-site re-skin.** Every supplement brand that engaged used a single sale or landing page, e.g. Bloom /collections/halloween-sale.
5. **Cute over scary.** A cute ghost (Unreal 2025, Krispy Kreme 2025), cauldron smoke or bubbles. Unreal promoted its 2025 ghost mascot from a product tile to the full homepage hero in 2026: "BE THE HOUSE WITH THE GOOD STUFF. Frighteningly delicious. 100% real. Less sugar." (live screenshot, 2026-10-25). A friendly recurring mascot is worth building once and reusing. Avoid skulls, blood or gore, which none of the health brands used. This also suits a 30–55 female audience.
6. **Tiny motion.** A 2-frame GIF or a subtle animated sticker. Bloom's banner swapped two frames every 1.2 s.
7. **Announcement-bar pun plus code.** YumEarth "SPOOKYBUNDLE", Olipop "SPOOKY20", Krispy Kreme "SCARY", Myprotein "TRICK", Bloom's auto-applied discount.

### Gaps
- No A/B or conversion data comparing "accent" and "full re-skin" treatments in the health category was found.
- No Bulgarian-market Halloween examples from health brands were found. Myprotein.bg showed no Halloween visuals in any October capture, 2021–2025.

---

## 4. Timing: when did the visuals go live and come down, and did they flow into Black Friday?

### Takeaway
**Assets were created in early to late September**; the Bloom sale banner was the exception, made on 29 Oct. Halloween products and collection pages went live from **late September to the first week of October**. Homepage heroes went Halloween from about **1–14 October**. Everything was swapped within **1–5 days after 31 October**, usually straight into holiday or Black Friday creative. Leftover Halloween SKUs stayed in grids, discounted, into November.

### Cited Findings
**Go-live [OBSERVED].**

| Brand | When | What |
|---|---|---|
| SmartSweets | by 19 Oct 2021 | hero + tiles (assets uploaded 23–27 Sep 2021) |
| SmartSweets | by 6 Oct 2022 | menu + Build-a-Box |
| SmartSweets | by 30 Sep 2023 | Halloween collection and giveaway pages |
| SmartSweets | by 9 Oct 2024 | homepage hero (asset 24 Sep 2024) |
| SmartSweets | by 14 Oct 2025 | announcement + PDPs |
| Unreal | by 26 Oct 2021 | collection |
| Unreal | by 29 Sep 2022 | product grid |
| Unreal | by 28 Sep 2023 | landing page |
| Unreal | by 14 Oct 2024 | homepage hero (asset 19 Sep 2024) |
| YumEarth | by 26 Sep 2022 | homepage hero |
| YumEarth | by 22 Sep 2023 | homepage hero |
| Feastables | by 8 Oct 2024 | homepage hero; pack images uploaded 15 Aug 2024 |
| Feastables | 15 Sep – 15 Oct 2025 | sweepstakes |
| Krispy Kreme | by 23 Oct 2021 | homepage |
| Krispy Kreme | by 7 Oct 2024 | homepage |
| Krispy Kreme | by 16 Oct 2025 | homepage |

Sources: ([CC 2021-10-19 19:14 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2021-43/segments/1634323585280.84/warc/CC-MAIN-20211019171139-20211019201139-00288.warc.gz), offset 703584029) ([CC 2022-09-29 05:54 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-40/segments/1664030335304.71/warc/CC-MAIN-20220929034214-20220929064214-00560.warc.gz), offset 622507932) ([CC 2023-09-22 01:15 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233506320.28/warc/CC-MAIN-20230922002008-20230922032008-00159.warc.gz), offset 1234379052) ([CC 2025-10-17 13:55 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-43/segments/1759648665304.94/warc/CC-MAIN-20251017125300-20251017155300-00004.warc.gz), offset 226030662)

**[PRESS] Launch dates.**
- Krispy Kreme: "Krispy Skreme" announced 11 Oct 2021 [Business Wire](https://www.businesswire.com/news/home/20211011005020/en/Witches%E2%80%99-Spell-Transforms-KRISPY-KREME%C2%AE-to-KRISPY-%E2%80%98SKREME%E2%80%99-for-Halloween-Season-including-4-New-Treats-and-Saturday-%E2%80%98Scary-Sharies%E2%80%99); Ghostbusters 7 Oct 2024 [Business Wire](https://www.businesswire.com/news/home/20241007303208/en/Capture-Your-Cravings-This-Halloween%21-KRISPY-KREME%E2%80%99S%C2%AE-Ghostbusters-Collection-Celebrates-1984-Film%E2%80%99s-40th-Anniversary); "Trick or Treat!" from 6 Oct 2025, with free doughnuts for costumed guests on 25 and 31 Oct [Business Wire](https://www.businesswire.com/news/home/20251006344063/en/No-Tricks-Only-Treats-KRISPY-KREME%C2%AE-Unleashes-Spooktacular-New-%E2%80%98Trick-or-Treat%21%E2%80%99-Doughnuts-so-Good-It%E2%80%99s-Scary%21).
- Unreal 2025: DTC from 15 Sep. [Snack & Bakery](https://www.snackandbakery.com/articles/114415-unreal-reveals-dye-free-halloween-candy-lineup)

**Late-October-only pages [OBSERVED].** Bloom's "Witching Hour Sale" banner was uploaded 29 Oct 2024 and the page was still live on 2 Nov 2024. This was a short last-week sale. ([CC 2024-11-02 09:05 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477027709.8/warc/CC-MAIN-20241102071948-20241102101948-00823.warc.gz), offset 125991943)

**Order-by deadline in the creative [OBSERVED].** Unreal 2023: "order by oct 25 to get in time for halloween". ([CC 2023-09-28 08:50 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-40/segments/1695233510368.33/warc/CC-MAIN-20230928063033-20230928093033-00182.warc.gz), offset 644501862)

**Take-down and handover [OBSERVED].**
- **Krispy Kreme**: by 5 Nov 2024 the hero was "Explore Our Sweets of the Season" (no Halloween). ([CC 2024-11-05 13:05 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477027881.88/warc/CC-MAIN-20241105114407-20241105144407-00651.warc.gz), offset 804259715)
- **Unreal**:
  - By 4 Nov 2024 the hero was "stock up on treats that make every gathering unreal!", with Halloween boxes still in the grid. ([CC 2024-11-04 01:15 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477027809.13/warc/CC-MAIN-20241104003052-20241104033052-00060.warc.gz), offset 572728975)
  - On 7 Nov 2025, Halloween variety packs were still listed. ([CC 2025-11-07 08:58 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-47/segments/1762439342474.62/warc/CC-MAIN-20251107081817-20251107111817-00327.warc.gz), offset 481290077)
- **SmartSweets**:
  - By 13 Nov 2024 the bar was back to "Build a #KickSugar candy box of your dreams". ([CC 2024-11-13 13:06 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477028347.28/warc/CC-MAIN-20241113103539-20241113133539-00648.warc.gz), offset 493664139)
  - By 19 Nov 2025 it was "Sweet stocking stuffers you can feel good about". Halloween Lollipops were still in Build-a-Box. ([CC 2025-11-19 04:28 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-47/segments/1762439657349.95/warc/CC-MAIN-20251119032929-20251119062929-00809.warc.gz), offset 412908647)
- **YumEarth**:
  - 10 Nov 2024 hero: "Delicious Holiday Treats". ([CC 2024-11-10 21:17 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477028191.83/warc/CC-MAIN-20241110201420-20241110231420-00159.warc.gz), offset 1010913137)
  - 29 Nov 2023: "Holiday Gingerbread House Kit!", with "halloween variety pack $23.99" marked down from $29.99. ([CC 2023-11-29 02:45 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2023-50/segments/1700679100047.66/warc/CC-MAIN-20231129010302-20231129040302-00159.warc.gz), offset 1229277577)
- **Olipop**: 13 Nov 2024 bar "NEW OLI & POP's Holiday Pack—the least naughty soda on the list!" ([CC 2024-11-13 18:47 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477028387.69/warc/CC-MAIN-20241113171551-20241113201551-00847.warc.gz), offset 189608879)
- **Black Friday from 2 November**:
  - Cymbiotika 2 Nov 2024: "BLACK FRIDAY SALE – 25% Off Sitewide". ([CC 2024-11-02 08:32 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477027709.8/warc/CC-MAIN-20241102071948-20241102101948-00080.warc.gz), offset 182704102)
  - Ritual 13 Nov 2025: "Black Friday: 40% Off Sitewide". ([CC 2025-11-13 08:25 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-47/segments/1762439343503.72/warc/CC-MAIN-20251113072720-20251113102720-00222.warc.gz), offset 410044217)
  - Myprotein 12 Nov 2025: "HOW DO YOU BLACK FRIDAY?" ([CC 2025-11-12 01:41 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-47/segments/1762439343096.76/warc/CC-MAIN-20251112010046-20251112040046-00828.warc.gz), offset 748446208)
  - Grüns 12 Nov 2025: "❄️ Our best deal of the year ❄️". ([CC 2025-11-12 23:20 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-47/segments/1762439343356.79/warc/CC-MAIN-20251112221848-20251113011848-00836.warc.gz), offset 216916874)
  - Gymshark 27 Nov 2022: "BLACK FRIDAY SALE". ([CC 2022-11-27 02:36 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-49/segments/1669446710155.67/warc/CC-MAIN-20221127005113-20221127035113-00635.warc.gz), offset 884596955)
- **Myprotein.bg, 7 Nov 2024**: "40% отстъпка на протеини!" ("40% off proteins!"), with no Halloween before or after. ([CC 2024-11-07 20:16 UTC](https://data.commoncrawl.org/crawl-data/CC-MAIN-2024-46/segments/1730477028009.81/warc/CC-MAIN-20241107181317-20241107211317-00544.warc.gz), offset 852940472)

**Live today, 2026-10-25 [OBSERVED].** Headless Chrome with JavaScript on; files `health_LIVE_2026-10-25_*.png`. Visible text was searched for Halloween terms, then the screenshots were checked by eye. AG1 ("Vercel Security Checkpoint") and Hers ("Just a moment...") served bot-check pages and could not be assessed.

- **What the screenshots show today (2026-10-25, six days before Halloween) [OBSERVED].**
  - **Unreal**:
    - The full homepage hero is Halloween: purple background, yellow condensed headline "BE THE HOUSE WITH THE GOOD STUFF.", sub-line "Frighteningly delicious. 100% real. Less sugar."
    - The 2025 cute white **ghost mascot** has been promoted from a product tile to the hero, peeking around a stack of peanut-butter cups, with dark bats.
    - File: `health_LIVE_2026-10-25_unreal.png`.
  - **SmartSweets**:
    - Orange announcement bar: "Limited-edition Halloween candy is back–grab yours before it disappears! 👻".
    - Hero split lime | orange, with **black slime drips** along the top edge and a purple base. "Sour Zombie Buddies" pack, gummy worms.
    - Copy: "With up to 93% less sugar than traditional candy, Halloween just got a whole lot sweeter."
    - File: `health_LIVE_2026-10-25_smartsweets.png`; the cookie banner covers part of the headline.
  - **YumEarth**:
    - Announcement bar: "Order by 10/21 5pm ET to get your treats by Halloween."
    - Orange hero with Halloween Choco Yums pack and bats. File: `health_LIVE_2026-10-25_yumearth.png`.
  - **Krispy Kreme**: purple hero with a spider-web line drawing and the Looney Tunes Halloween doughnut dozen. File: `health_LIVE_2026-10-25_krispykreme.png`.
  - **Olipop**:
    - Already on its holiday-season "Pomegranate Sparkle – Come sip with us" (pink, sparkles), with no Halloween, even though a Caramel Apple Halloween can launched in Sep 2026. [Sporked, 9 Sep 2026](https://sporked.com/article/a-new-ghoulish-flavor-is-coming-to-olipop/); [Beverage Industry](https://www.bevindustry.com/articles/98661-olipop-releases-limited-edition-flavor)
    - File: `health_LIVE_2026-10-25_olipop.png`.
  - **Bloom**:
    - "CLUB APPLE NYC Oct 24+25" fall/apple hero, no Halloween on the homepage. File: `health_LIVE_2026-10-25_bloom.png`.
    - [PRESS] Bloom released a "Pear Scare" Halloween flavour and a "Double Trouble" pack with jack-o'-lantern cans in 2026. [Sporked](https://sporked.com/article/bloom-energy-just-packed-two-fall-faves-into-one-with-a-halloween-makeover/); [Stack3d](https://www.stack3d.com/2026/09/bloom-double-trouble-crisp-apple/)
  - **Feastables**: no Halloween text on the homepage today.
  - **Lily's**: only "LILY'S Pumpkin Spice Muffins".
  - **Goli, Olly, Ritual, Noom, Lemme, Grüns, Cymbiotika, Myprotein BG, Gymshark, Huel, Ghost, Sugarbear (now sugarbearpro.com), Arrae, Seed**: no Halloween wording.
- **The pattern holds into 2026 [INFERENCE].** Low-sugar candy brands theme the homepage; supplement and wellness brands keep it evergreen, putting any Halloween into a product (a flavour or can) or a side page rather than the homepage.


### Inferences
- **Recommended FitPatches timeline**, inferred from the observed cadence:

| When | Action |
|---|---|
| Mid/late Sep | Design assets |
| ~1–10 Oct | Soft launch: announcement bar, product-tile accents, collection or bundle page |
| ~15–31 Oct | Peak: Halloween hero + "witching hour" style sale |
| 1–3 Nov | Remove all Halloween visuals; move straight into Black Friday |

- Courier lead times in Bulgaria matter. Two brands put a shipping deadline into the Halloween creative: Unreal 2023 ("order by oct 25 to get in time for halloween") and YumEarth live in 2026 ("Order by 10/21 5pm ET to get your treats by Halloween"). Its uplift is unmeasured.
- A short late-October sale page (Bloom, 29 Oct 2024) can be bolted on even if the main site stays evergreen. That fits a brand that does not want a month-long candy theme.
- **Black Friday starts on 1–2 November** in this category (Cymbiotika 2024). The Halloween design must be easy to swap. Keep Halloween to removable layers (bar, hero, overlays) rather than theme-wide CSS.

### Gaps
- No Common Crawl capture after 18 October in 2022–2025 (only 2021 reaches 28 Oct). The exact peak-week state and the precise switch-off date (31 Oct vs 1 Nov vs 2 Nov) are not observed.
- Bloom's sale end date is unknown; the page was still live on 2 Nov 2024. Unreal's hero swap happened on or before 4 Nov 2024; the exact day is unknown.

---

## 5. Measured results tied to Halloween visuals or limited editions in this category

### Takeaway
Hard numbers are scarce. **No brand published a conversion or sales lift attributable to Halloween website visuals.** The available evidence is directional:
- Unreal's DTC store was "on track to have our best month ever" during its Halloween push.
- SmartSweets' Halloween social post beat its like target by 20%.
- SkinnyDipped says Halloween "has typically performed strongly".
- Category spend is large: $6.4bn of Halloween chocolate and candy in 2023, per the NCA.

### Cited Findings
- **Unreal (Oct 2024)**: "on track to have our best month ever in our online brand shop". Its Halloween variety pack on its DTC site was sold out at the time of writing. First year in Target's seasonal aisle; Halloween packaging since 2015. [Modern Retail, 24 Oct 2024](https://www.modernretail.co/marketing/better-for-you-candy-brands-are-going-all-in-on-halloween/) [PRESS]
- **Unreal (2025)**: says its Halloween packaging and formats are "designed to support trial and increase basket size". No figures given. [Snack & Bakery](https://www.snackandbakery.com/articles/114415-unreal-reveals-dye-free-halloween-candy-lineup) [PRESS]
- **SkinnyDipped**: the CEO said the Halloween period "has typically performed strongly". Customers buy "for self-treating around Halloween". [Modern Retail](https://www.modernretail.co/marketing/better-for-you-candy-brands-are-going-all-in-on-halloween/) [PRESS]
- **SmartSweets (2022)**: promised a low-sugar candy corn if an Instagram post reached 10,000 likes. It passed 12,000. [Stack3d](https://www.stack3d.com/2022/10/smart-sweets-candy-corn/) [PRESS]
- **Category size**: NCA reported $6.4bn of Halloween chocolate and candy sales in 2023 and projected 3–5% growth for 2024. Better-for-you is "a growing subcategory" without a market-share figure. [Modern Retail](https://www.modernretail.co/marketing/better-for-you-candy-brands-are-going-all-in-on-halloween/) [PRESS]
- **Krispy Kreme**: launch releases state goals ("boosting seasonal sales through product innovation") but give no results. I found no earnings-call quantification. [Restaurant India summary of the 2025 launch](https://www.restaurantindia.in/news/restaurant-india-news-krispy-kreme-unveils-halloween-trick-or-treat-collection-with-four-new) [PRESS]
- **Limited-time offers**: a claim that they "can boost sales up to 34%" appears on a Brand360 page. It traces to a CrazyEgg blog, not primary data, so I treat it as **unverified**. [Brand360](https://www.brand360.com.my/chinese/wp-json/wp/v2/posts/9291)

### Inferences
- The repeat behaviour is itself evidence of payback. SmartSweets themed every year 2021–2025; Unreal ran Halloween SKUs and pages every year 2021–2025 (and since 2015 per press); YumEarth, Feastables and Krispy Kreme did so every year observed. Brands rarely keep a costly seasonal programme going for five years if it does not pay. This is an inference, not a measured lift.
- The supplement brands' consistent silence suggests either low expected return or brand-safety caution about tying a wellness product to candy. A FitPatches test should be **cheap and reversible**: an overlay, a bar, one banner and a bundle. Measure it against the prior two weeks and a non-themed holdout, e.g. an A/B hero test in Shopify.

### Gaps
- No public conversion-rate, AOV or revenue data tied to Halloween website visuals for any brand in scope.
- No social-engagement metrics for Bloom's "Witching Hour Sale", Olipop's costume sweepstakes, or Feastables' Halloween sweepstakes.
- No Bulgaria-specific data on Halloween e-commerce uplift for health or beauty products was found within this scope.

