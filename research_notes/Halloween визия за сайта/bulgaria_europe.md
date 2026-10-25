# Halloween website visuals in Bulgarian and European e-commerce (2021–2026) and how Halloween is perceived in Bulgaria

How the evidence was gathered (read this first):
- The Wayback Machine (web.archive.org) was blocked from this container. curl, the headless browser and WebFetch all failed, and Firecrawl had run out of credits. The archive.org availability API worked, but it only returns timestamps. archive.ph returned a CAPTCHA.
- **Historical evidence (2021–2025)** therefore comes from **Common Crawl** homepage captures. I looked them up in the CC indexes and fetched the original HTML (WARC records) from data.commoncrawl.org, then scanned it for Halloween and Black Friday terms after removing scripts and styles. Where useful I rendered it locally with live assets. Each observation carries its exact capture timestamp (UTC). Caveat: the CC crawls 2022-40 (24 Sep–7 Oct), 2023-40 (21 Sep–5 Oct), 2024-42 (3–16 Oct) and 2025-43 (~5–18 Oct) end **before** the usual Halloween switch-on week. Only 2021-43 (16–28 Oct) covers late October, and 2024-46 / 2025-47 cover early to mid November. "No Halloween terms" in an early-October capture does not prove a shop ran no Halloween visuals later.
- **Live evidence:** today is 2026-10-25, six days before Halloween. I screenshotted the live sites with headless Chromium between 08:30 and 09:10 UTC. That makes 2026 the best-observed year. eMAG, Notino.bg, Douglas.bg, Sopharmacy, Fashion Days, GymBeam.bg, Answear, Sephora, Douglas.de, Zalando and Boots blocked the headless browser.
- **Labels:** "OBSERVED" means I saw it directly in a screenshot or captured HTML. "INFERENCE" means my interpretation.

## 1. What did Bulgarian e-shops actually show for Halloween, and how strongly?

### Takeaway
Bulgarian shops that sell to adult women (pharmacies, drugstores, beauty and fashion) treat Halloween lightly or not at all. The pharmacies (Subra, Remedium, BENU) and Lilly Drogerie show **no** Halloween on their homepages. Beauty players add **one product-led Halloween banner or tile** (Notino: makeup on a flat orange-red background; dm: a soft pastel "Хелоуин" tile and inspiration page) and never re-skin the whole site. **Strong, dark "spooky" creative** appears only at shops with a younger, gamer or gym audience (Ozone.bg's zombie hand, Pulse Fitness's evil jack-o'-lantern kettlebell) and at mass grocer Lidl (a haunted-castle teaser in 2025). Even then it sits in one hero slide or teaser, not across the whole site.

### Cited Findings
**Live, 2026-10-25 (OBSERVED)**
- **Notino.bg** (homepage blocked by Cloudflare, so I pulled the banner file from Notino's CDN folder for BG). The BG Halloween homepage banner for week 43 of 2026 exists as `bg_desk_hp_halloween_w43_26_ff4f30.jpg` (desktop) and `bg_mob_hp_halloween_w43_26.jpg` (mobile). Text: **"Грим за Хелоуин за тъмната страна във вас"**, button **"Вдъхновете се"**. The background is a flat orange-red (#ff4f30 per the file name) with cut-out products: Maybelline Sky High mascara, Estée Lauder Double Wear foundation and Rimmel Wonder Ink liner. There are no pumpkins, bats or illustrations. — [Notino CDN, BG desktop banner](https://cdn.notinoimg.com/c=85/images/gallery/ba/12/bg_desk_hp_halloween_w43_26_ff4f30.jpg); [BG mobile banner](https://cdn.notinoimg.com/c=85/images/gallery/ba/12/bg_mob_hp_halloween_w43_26.jpg)
- The same template is live as a homepage banner on notino.de, .ro, .gr and .cz (alt text "MUP HALLOWEEN LOOKS HP - 2606950"). Each links to `/halloween-looks/`. On notino.de it is the **first hero slide**: "Halloween-Make-up-Looks für Ihre dunkle Seite". — [notino.de](https://www.notino.de/); [notino.ro](https://www.notino.ro/); [DE banner file](https://cdn.notinoimg.com/c=85/images/gallery/ba/5/de_ch_desk_hp_halloween_w43_26_ff4f30.jpg)
- Notino.bg also has a standing Halloween makeup category, "Грим за Хелоуин", at /grim-za-khelouin/. The search index gave it an age of about 6 years. I could not fetch it (403). — [notino.bg/grim-za-khelouin](https://www.notino.bg/grim-za-khelouin/)
- **dm Bulgaria**, homepage on 2026-10-25:
  - In "Актуални предложения", a **"Halloween"** tile sits next to "Женско здраве", "Красива усмивка с Dontodent" and **"Коледни календари"**.
  - A carousel teaser reads "dmLIVE: Приготвeте се за Хелоуин с NYX".
  - The product rail includes a "Balea Маска кърпа за лице Vanilla Pumpkin".
  - The hero itself is not Halloween: it is a red "-20% … от 15.10. до 11.11.26" oral-care promo. — [dm-drogeriemarkt.bg](https://www.dm-drogeriemarkt.bg/)
- **dm Bulgaria, Halloween landing page.** Page title "🎃 Хелоуин: Зловещи вдъхновения | dm България". The visual is **soft pastel peach circles with small doodle cobwebs, flowers and sparkles**, organised as three categories: Грим / Идеи за декорация / Рецепти.
  - Copy, verbatim: "Когато дните станат по-къси, вятърът засвири около къщата, а тиквите заблестят по прозорците, отново е време за Хелоуин. Независимо дали планирате голямо парти с приятели, **уютна семейна вечер с децата** … Така 31 октомври със сигурност ще бъде **страховито красив**."
  - The text is a translation of dm Austria's page ("Wenn die Tage kürzer werden, der Wind ums Haus pfeift und Kürbisse in den Fenstern leuchten…"), i.e. a group template. — [dm BG Halloween page](https://www.dm-drogeriemarkt.bg/vdahnovenie-i-saveti/tematichni-predlozhenia-i-idei/halloween); [dm.at Halloween page](https://www.dm.at/inspiration-und-beratung/themenwelten/halloween)
- **dmLIVE (dm BG).** Live show "Приготвeте се за Хелоуин с NYX PROFESSIONAL MAKEUP" on 21 Oct 2026 at 18:00 in the dm app, with a make-up artist and an influencer. Viewers received a 15% NYX coupon valid for 7 days. — [dm BG dmLIVE](https://www.dm-drogeriemarkt.bg/services/klientski-programi-i-uslugi/dmlive)
- **Lilly Drogerie.** Homepage hero: "СУПЕР ЦЕНА — Период на акцията: 01-31.10.2026" in yellow and black hazard stripes with Lattafa, Max Factor and L'Oréal deals. **No Halloween words or images anywhere in the DOM** (desktop and mobile). — [lillydrogerie.bg](https://lillydrogerie.bg/)
- **Ozone.bg** (games, books, toys). Hero slide 1: **"Ужасно яки оферти" / "50 000 ПРОДУКТА НА ПЛАШЕЩО ДОБРИ ЦЕНИ" / "ВИЖ ТУК"**. The whole hero background is neon green, with a round image of a green zombie hand with purple claws rising from soil and holding a torn price tag, set against a full moon. The lettering is dripping magenta. Other slides are normal (iPhone, Sony, perfume). Halloween products appear in rails, e.g. "LEGO Creator – Призрачно имение" and "Пъзел … Хелоуин". — [ozone.bg](https://www.ozone.bg/); [slide image](https://cdn.ozone.bg/media/slider/image/2026/10/os_main_500h500_01.jpg)
- **Pulse Fitness** (gym chain, not a shop). Homepage image with alt text "Scary offer 2026":
  - **"SCARY OFFER – СТРАШНО ДОБРА ОФЕРТА."**
  - A jack-o'-lantern carved into a kettlebell with an evil glowing face, set in a dark gym with fire, smoke and orange embers.
  - This is maximum "scary" intensity. — [pulsefit.bg image](https://pulsefit.bg/wp-content/uploads/02-1080h1080-1200.webp)
- **Pharmacies (Subra, Remedium, BENU): no Halloween** on the homepages (DOM keyword scan and screenshots). Remedium's hero is an immunity product ("Серия Sambucus… имуностимулатор", -10%). BENU shows "до -37% на избрани продукти + подарък". Sopharmacy (403) and Аптеки Марешки (502) could not be loaded. — [subra.bg](https://subra.bg/); [remedium.bg](https://remedium.bg/); [benu.bg](https://benu.bg/)
- **Kaufland BG and Lidl BG: no Halloween** on the homepages on 2026-10-25. Lidl's hero reads "Сваляме цените от 12.10. до 08.11."; Kaufland shows "SUPER СДЕЛКИ". — [lidl.bg](https://www.lidl.bg/); [kaufland.bg](https://www.kaufland.bg/)

**Historical, from Common Crawl captures (OBSERVED in the HTML; timestamps in UTC)**
- **Lidl BG, 2025-10-14 13:24.**
  - The homepage marketing teaser image `MT_Halloween_LG-1818327.jpg` has the alt text "**Хелоуин в Lidl: призрачен замък с прилепи, пълнолуние и мълнии.**"
  - The image is still on Lidl's CDN. It is a dark, cinematic night scene: a Lidl store as a castle on a cliff, bats on a dead tree, a full moon, lightning, cemetery gates and a "HALLOWEEN" badge with a black cat.
  - **2021-10-22 16:06:** the homepage flyout held a themed tile `slot_2142_halloween_420x316.jpg` alongside other themed tiles (books, burger, pizza).
  - 2024-11-03: only a "Чийзкейк с тиква" recipe teaser. — [CC index CC-MAIN-2025-43, lidl.bg](https://index.commoncrawl.org/CC-MAIN-2025-43-index?url=https://www.lidl.bg/&output=json); [teaser image](https://www.lidl.bg/static/assets/MT_Halloween_LG-1818327.jpg); [CC index CC-MAIN-2021-43](https://index.commoncrawl.org/CC-MAIN-2021-43-index?url=https://www.lidl.bg/&output=json)
- **dm BG.**
  - 2025-10-15 14:43: the homepage had a teaser "**Хелоуин**" linking to the same Halloween inspiration page, next to "Крем супа от тиква, Есенна рецепта".
  - 2025-11-14 02:13: the Halloween teaser was gone, but the pumpkin soup recipe and a "Pumpkin Spice Latte" candle remained, i.e. pumpkin persists as an autumn motif after Halloween.
  - 2024-10-11 and 2024-11-02: no Halloween terms. — [CC index CC-MAIN-2025-43, dm BG](https://index.commoncrawl.org/CC-MAIN-2025-43-index?url=https://www.dm-drogeriemarkt.bg/&output=json); [CC-MAIN-2025-47](https://index.commoncrawl.org/CC-MAIN-2025-47-index?url=https://www.dm-drogeriemarkt.bg/&output=json)
- **Notino BG, 2025-10-16 23:36.**
  - The homepage had **no Halloween terms**.
  - The hero carousel showed "-10% / -15% на цялата поръчка … с кода all" on a pink-purple background with **Christmas baubles**, and the top nav already had "**Подаръци за Коледа**".
  - 2022-10-07 and 2023-09-28: no Halloween terms. — [CC index CC-MAIN-2025-43, notino.bg](https://index.commoncrawl.org/CC-MAIN-2025-43-index?url=https://www.notino.bg/&output=json)
- **Kaufland BG, 2024-11-03 07:16.**
  - An offer tile "**Тиква Хелоуин рисувана**" (a painted Halloween pumpkin) was still on the homepage.
  - The hero teaser had already switched to "**Kaufland: Ексклузивни black week оферти още от неделя**".
  - 2023-09-30, 2023-10-04 and 2025-10-10: no Halloween terms. — [CC index CC-MAIN-2024-46, kaufland.bg](https://index.commoncrawl.org/CC-MAIN-2024-46-index?url=https://www.kaufland.bg/&output=json)
- **Pulse Fitness, 2025-11-16 19:14.** The homepage block "**🎃 Halloween Events by Pulse!**" linked to /halloween-events-by-pulse/. Captures from 2021, 2022, 2023 and 2024 (Oct/Nov) had no Halloween terms. — [CC index CC-MAIN-2025-47, pulsefit.bg](https://index.commoncrawl.org/CC-MAIN-2025-47-index?url=https://pulsefit.bg/&output=json)
- **No Halloween terms** were found on these homepage captures:
  - **eMAG.bg:** 2021-10-21, 2021-10-27 (late October), 2022-09-24, 2024-10-11, 2024-10-13
  - **Fashion Days BG:** 2021-10-22, 2022-09-28, 2023-09-30, 2024-10-10, 2025-10-15/18
  - **Douglas BG:** 2021-10-23, 2022-09-29, 2024-10-06/11, 2025-10-10
  - **Answear BG:** 2021-10-17, 2025-10-10
  - **GymBeam BG:** 2021-10-23, 2021-10-26, 2022-10-04, 2023-10-03
  - **Myprotein BG:** 2021-10-19, 2022-09-27, 2023-09-27, 2024-10-14, 2024-11-07, 2025-10-11
  - **Remedium:** 2021-10-17, 2022-09-28, 2025-10-13 (hero: "Месец на Avène -22%")
  - **Subra:** 2023-09-23, 2024-10-12, **2024-11-01**, 2025-10-09
  - **BENU:** 2023-09-21, 2024-10-07, 2024-11-03, 2025-10-08
  - **Lilly Drogerie:** 2025-10-12, **2025-10-17**, 2025-11-15/16

  The full keyword scan is saved in `shots/data/commoncrawl_homepage_keyword_scan_2021-2025.txt`. — [CC index example, emag.bg 2021](https://index.commoncrawl.org/CC-MAIN-2021-43-index?url=https://www.emag.bg/&output=json); [CC index example, fashiondays.bg 2025](https://index.commoncrawl.org/CC-MAIN-2025-43-index?url=https://www.fashiondays.bg/&output=json)
- **eMAG (secondary source):** in Romania in 2017, eMAG joined a Halloween discount wave, with offers from 27 Oct to 1 Nov of up to 40%. This is Romania, not Bulgaria, and it is old. — [Mobilissimo.ro 2017](https://www.mobilissimo.ro/articole-diverse/iata-lista-retailerilor-si-a-operatorilor-ce-organizeaza-campanii-speciale-de-halloween-2017)
- **Physical retail context (2019):** Bulgarian stores turned into "карнавални лабиринти, залети с всякаква магическа стока". "Рафтовете се огъват от … черепи, тикви, мантии и магьоснически шапки", and the season's hit with teenagers was a severed bloody hand on a plate for 3.99 lv. The buyers are framed as parents and teenagers. — [Mirogled, 31.10.2019](https://mirogled.com/news-view/maghazinitie-ss-strashni-iekstri-za-khielouin-skielieti-i-otriazani-rtsie-po-4-lieva)

### Saved files (screenshot index, folder `shots/`)
Live, 2026-10-25:
- `bg_notino_halloween_banner_desktop_2026-wk43.jpg` and `bg_notino_halloween_banner_mobile_2026-wk43.jpg`: Notino BG homepage Halloween banner files, "Грим за Хелоуин за тъмната страна във вас", flat orange-red background with makeup products.
- `bg_dm_homepage_2026-10-25.png`: dm BG homepage hero (oral-care -20%, with a cookie overlay). The "Halloween" tile is confirmed in the DOM.
- `bg_dm_halloween_landing_2026-10-25.png`, `bg_dm_halloween_landing_mobile_2026-10-25.png` and `bg_dm_halloween_landing_fullpage_2026-10-25.jpg`: dm BG "Хелоуин: Зловещи вдъхновения" page; pastel peach circles with tiny cobweb doodles.
- `bg_dm_dmlive_nyx_halloween_2026-10-25.png`: dmLIVE "Приготвeте се за Хелоуин с NYX" page.
- `bg_lillydrogerie_homepage_2026-10-25.png` and `bg_lillydrogerie_homepage_mobile_2026-10-25.png`: Lilly, "Супер цена 01–31.10.2026", no Halloween.
- `bg_ozone_hero_halloween_2026-10-25.png`: Ozone hero slide "Ужасно яки оферти", neon green, zombie hand. `bg_ozone_halloween_slide_image_2026-10-25.jpg` is the slide image alone.
- `bg_pulsefit_scary_offer_2026-10-25.jpg`: Pulse "SCARY OFFER – СТРАШНО ДОБРА ОФЕРТА.", evil jack-o'-lantern kettlebell, fire.
- `bg_contactsheet_pharmacies_retail_2026-10-25.png`: Subra, Remedium, BENU, Kaufland, Lidl and Ozone (slide 2) homepages; none of the pharmacies or grocers show Halloween.

Historical, rendered from Common Crawl HTML with live assets and JavaScript off, so some layouts are broken:
- `bg_lidl_2025-10-14_homepage_halloween_teaser_image.jpg`: Lidl BG 2025 haunted-castle Halloween teaser image.
- `bg_notino_2025-10-16_commoncrawl_render.png`: Notino BG on 16 Oct 2025; -10/-15% hero with Christmas baubles, "Подаръци за Коледа" in the nav, no Halloween.
- `bg_benu_2024-11-03_commoncrawl_render_black_november.png`: BENU on 3 Nov 2024, "Black November" in the top bar and menu.
- `bg_remedium_2025-10-13_commoncrawl_render.png`: Remedium on 13 Oct 2025, "Месец на Avène", no Halloween.
- `bg_emag_2021-10-27_commoncrawl_render.png`: eMAG on 27 Oct 2021, "Оферти на фокус", no Halloween; the hero carousel is empty because JavaScript was off.
- `bg_emag_2024-11-14_commoncrawl_render.png`: eMAG on 14 Nov 2024 with "Guide Black Friday" in the nav.
- `bg_contactsheet_commoncrawl_A.png` and `bg_contactsheet_commoncrawl_B.png`: contact sheets of all the BG historical renders.

Data:
- `shots/data/google_trends_BG_*.csv`: Google Trends weekly data (Bulgaria, 2021–2025).
- `shots/data/commoncrawl_homepage_keyword_scan_2021-2025.txt`: the per-capture keyword scan.

### Inferences
- I sorted shops into an intensity ladder:
  - **None:** pharmacies, Lilly, Answear and Fashion Days homepages.
  - **Subtle:** a nav category, a coupon code or a single tile (dm homepage tile, Notino's standing "Грим за Хелоуин" category).
  - **Moderate:** one product-led banner in the colour orange, no monsters (Notino 2026).
  - **Strong:** a dark or neon spooky illustration in one hero slide or teaser (Ozone 2026, Lidl 2025, Pulse 2026).
- No Bulgarian shop I observed re-skinned the whole site (header, logo, background, product cards) for Halloween.
- The shops closest to fitpatches' audience (women 30–55 buying health or beauty products, often in pharmacies) either skip Halloween or keep it **beauty-functional and light**. dm frames it as "уютна семейна вечер с децата" and "страховито красив" with pastel peach doodles. Notino frames it as "тъмната страна във вас", but visually it is just products on an orange background.
- In Bulgaria, the dark or cartoon-horror end of the spectrum belongs to categories aimed at teens, gamers and gym-goers, plus Lidl's pan-brand creative. INFERENCE: for a pink (#d64d87), wellness-oriented brand, the closest analogue is the dm/Notino style: a small seasonal accent, products in front and a playful "страшно добра оферта" style pun, not dark imagery.
- Most BG shops appear to run Halloween only in the last ~10 days of October. Mid-October captures (Notino on 16 Oct 2025, eMAG on 11–13 Oct 2024, Lilly on 17 Oct 2025) had nothing, while 2026 live captures from the 43rd week did. Notino's banner file is explicitly tagged week 43 (`w43`).

### Gaps
- I could not view Wayback snapshots from 20–31 October 2022–2025. They exist per the availability API and can be opened manually in a normal browser:
  - notino.bg: 20221028234133, 20231029001135, 20241027225708
  - emag.bg: 20221030154043, 20231029233159, 20251027185244
  - fashiondays.bg: 20221028082241, 20231027105548, 20241029095614
  - answear.bg: 20221027095852, 20231030154826
  - ozone.bg: 20221030153634, 20231029002855, 20251026124526
  - douglas.bg: 20231029141438
  - dm-drogeriemarkt.bg: 20231024120036, 20251028194918
  - myprotein.bg: 20221028201612, 20231028191443
  - remedium.bg: 20221026134411
- There is no direct observation of the eMAG, Notino.bg, Douglas BG, Sopharmacy, Аптеки Марешки, Fashion Days, Answear, GymBeam BG or Myprotein BG homepages in late October of any year: they were either blocked or only captured early in the month.
- I found no data for Vitaslim, BB-Team/bbshop.bg or other Bulgarian supplement brands: their sites blocked or redirected.
- The Notino BG banner's live placement on the BG homepage is inferred from the CDN file plus its placement on DE/RO/GR/CZ. I did not see it rendered on notino.bg.
- Prior-year Notino BG Halloween banners could not be located: the file-name patterns for 2022–2025 are unknown.

## 2. What did European health and beauty retailers do visually for Halloween?

### Takeaway
Large EU and UK health and beauty retailers treat Halloween as a **small merchandising moment**: a nav link, a "Halloween beauty" category, a makeup-tutorial page, a coupon code or one banner. The homepage hero usually belongs to a regular promo or, by late October, to **Christmas**. Pure health or supplement retailers (Holland & Barrett, Myprotein UK, GymBeam) showed **no Halloween** on their homepages in any capture. Where sports-nutrition brands do Halloween, it is a promo-code mechanic (Myprotein CA "Halloween Mystery Discount", code TREAT) rather than spooky visuals. "Pumpkin" appears as a cosy-autumn product flavour (pumpkin spice, Pumpkin Pie) independently of Halloween.

### Cited Findings
- **Notino (DE/RO/GR/CZ), live 2026-10-25.**
  - The homepage Halloween banner ("Halloween-Make-up-Looks für Ihre dunkle Seite") is hero slide 1 on notino.de, in flat orange-red with products.
  - The landing page `/halloween-looks/` reads: "Halloween ist die perfekte Gelegenheit, Ihrer dunklen Seite mehr Raum als sonst zu geben! … gruselig-inspirierende Looks". It offers looks such as "Cracked Doll 🖤" and "-20 % auf Bestellungen aus dieser Kategorie über 10,00 €". — [notino.de/halloween-looks](https://www.notino.de/halloween-looks/)
- **Douglas.de, Common Crawl 2021-10-26 04:34.**
  - A pink promo bar read "20 % Beauty-Bonus ab 59 € Bestellwert – Code: **HALLOWEEN20**".
  - The homepage linked to "Halloween-Specials" make-up tutorials (Poseidon, Medusa, "gruseliger Püppchen-Look") under /c/herbst/halloween-specials/.
  - The hero itself was a hotel/short-break voucher promo, i.e. Halloween appeared only as a code and as content. — [CC index CC-MAIN-2021-43, douglas.de](https://index.commoncrawl.org/CC-MAIN-2021-43-index?url=https://www.douglas.de/de&output=json)
- **Sephora FR, CC 2021-10-25 16:14.** The make-up nav had a "**🎃Halloween Beauty**" selection (/nos-selections-halloween/). Halloween did not appear in the hero. — [CC index CC-MAIN-2021-43, sephora.fr](https://index.commoncrawl.org/CC-MAIN-2021-43-index?url=https://www.sephora.fr/&output=json)
- **Boots UK.**
  - CC 2021-10-27 22:22: the nav had "halloween beauty products", and the black site-wide strip read "**Start your Christmas shopping** with 3 for 2 on selected No7".
  - CC 2025-10-16: Offers › seasonal events › "halloween" in the nav.
  - Live 2026: blocked. — [CC index CC-MAIN-2021-43, boots.com](https://index.commoncrawl.org/CC-MAIN-2021-43-index?url=https://www.boots.com/&output=json)
- **Lookfantastic.**
  - CC 2021-10-25 10:59: Seasonal › Halloween nav plus one "Halloween" image card. The hero was "SUPER SAVINGS… 20FLASH" with gold festive stars.
  - CC 2024-10-16 and 2025-10-18: no Halloween beyond the "Ghost" brand and "Witch Hazel" links, which are false positives.
  - Live 2026-10-25: the nav starts with "Christmas" and a "CHRISTMAS SHOP IS OPEN" strip; no Halloween.
  - Their blog runs a "Battle of the Halloween looks: scary vs cute" piece. — [CC index CC-MAIN-2021-43, lookfantastic](https://index.commoncrawl.org/CC-MAIN-2021-43-index?url=https://www.lookfantastic.com/&output=json); [lookfantastic.com](https://www.lookfantastic.com/); [LF blog](https://www.lookfantastic.com/blog/discover/battle-of-the-halloween-looks-scary-vs-cute/)
- **Cult Beauty.**
  - CC 2024-10-15: the nav linked a blog post, "10 Halloween Make Up Looks".
  - CC 2025-10-12: the global primary banner was the Laneige Lip Sleeping Mask "**Pumpkin Pie**": "Fulfil your '**cosy season**' fantasies…". This is autumn and pumpkin, not Halloween.
  - Live 2026-10-25: Christmas in the nav, no Halloween. — [CC index CC-MAIN-2025-43, cultbeauty](https://index.commoncrawl.org/CC-MAIN-2025-43-index?url=https://www.cultbeauty.co.uk/&output=json); [cultbeauty.co.uk](https://www.cultbeauty.co.uk/)
- **Rossmann.de.**
  - CC 2025-10-10: a teaser alt mentions "eine Isana Tuchmaske mit Halloween-Motiv".
  - CC 2025-11-07: the homepage app-teaser slots were still named `app_start_btt_halloween_vampir_de_2025_kw43` and `…halloween_joker…kw43`, but they now showed **Advent calendars**. This means a week-43 (late October) Halloween slot that was re-used for Christmas by early November. — [CC index CC-MAIN-2025-47, rossmann.de](https://index.commoncrawl.org/CC-MAIN-2025-47-index?url=https://www.rossmann.de/de/&output=json)
- **dm.de and dm.at.**
  - dm.de, CC 2025-10-08: pumpkin carving set, felt-pumpkin decor and "Bliss Balls, Pumpkin Spice".
  - dm.de, live 2026-10-25: Balea "Tuchmaske Vanilla Pumpkin" and a "Pumpkin Spice Pancake Bowl" recipe, but no Halloween banner on the homepage.
  - dm.at has a full "Halloween: schaurige Inspiration" theme world with pastel visuals (the same template as dm BG). — [dm.de](https://www.dm.de/); [dm.at Halloween](https://www.dm.at/inspiration-und-beratung/themenwelten/halloween)
- **Holland & Barrett.**
  - CC 2022-10-07 and 2023-09-28: the only seasonal item was a Health Hub recipe, "Vegan pumpkin spice latte".
  - CC 2024-10-12: nothing.
  - Live 2026-10-25: the hero is "Discover 100s of new products", with no Halloween.
  - Its promotional T&Cs list a BOGOF running 30 Sep–4 Nov 2026 that is not labelled as Halloween. — [hollandandbarrett.com](https://www.hollandandbarrett.com/); [H&B promo T&Cs](https://www.hollandandbarrett.com/info/terms-and-conditions/promotional-terms/)
- **Myprotein.**
  - UK homepage captures had no Halloween terms: 2021-10-23, 2022-10-03, 2023-09-25, 2024-10-11/13, 2024-11-04/06 and 2025-10-15/16.
  - Live UK 2026-10-25: "EXTRA… USE CODE: EXTRA", with "Advent" in the nav.
  - Myprotein Canada has a "**Halloween Mystery Discount**" page: "This Halloween we're offering a Mystery Discount of between 45% and 50% OFF. How lucky are you feeling? Will it be Trick or Treat... use code TREAT". There is no Halloween imagery in its headings or alt texts. — [Myprotein CA](https://ca.myprotein.com/c/all-offers/halloween-mystery-discount/); [CC index CC-MAIN-2024-42, myprotein.com](https://index.commoncrawl.org/CC-MAIN-2024-42-index?url=https://www.myprotein.com/&output=json)
- **GymBeam SK, live 2026-10-25.** The top bar offers a free immunity bundle ("balíček na posilnenie imunity ZADARMO… Kód: NAZDRAVIE"); no Halloween. — [gymbeam.sk](https://gymbeam.sk/)

### Saved files
- `eu_notino_de_homepage_2026-10-25.png`: Notino DE hero slide 1, the Halloween make-up banner.
- `eu_notino_de_halloween_banner_desktop_2026-wk43.jpg`: the banner file.
- `eu_notino_de_halloween_landing_2026-10-25.png`: the /halloween-looks/ page.
- `eu_dm_at_halloween_landing_2026-10-25.png`: dm.at "Halloween: schaurige Inspiration".
- `eu_myprotein_ca_halloween_mystery_page_2026-10-25.png`: Myprotein CA, code TREAT.
- `eu_contactsheet_A_2026-10-25.png`: Notino DE landing, dm.at, Myprotein CA, H&B, Myprotein UK and Rossmann (error page).
- `eu_contactsheet_B_2026-10-25.png`: Lookfantastic (Christmas), Cult Beauty, Boots (blocked), dm.de, GymBeam SK and Notino DE.
- `eu_douglas_de_2021-10-26_commoncrawl_render_HALLOWEEN20_bar.png`: pink promo bar with code HALLOWEEN20 above a travel-voucher hero.
- `eu_boots_2021-10-27_commoncrawl_render.png`: "Start your Christmas shopping" strip on 27 Oct 2021.
- `eu_lookfantastic_2021-10-25_commoncrawl_render.png`: "SUPER SAVINGS" hero, with Halloween only in the nav.
- `eu_contactsheet_commoncrawl.png`: all the EU historical renders.

### Inferences
- In mainstream EU beauty and health e-commerce, Halloween is a **category and content play, not a site skin**. The consistent EU pattern is: a nav link, a tutorial page or one banner, a coupon code with a Halloween name (HALLOWEEN20, TREAT), and the hero often already selling Christmas or a generic sale by late October.
- Health and supplement retailers (H&B, Myprotein UK, GymBeam) largely ignore Halloween on site. Pumpkin is used as a **cosy-autumn flavour or scent cue**, which suits a wellness brand better than horror imagery.
- Myprotein's TREAT "mystery discount" shows the safest Halloween mechanic for a supplement brand: a **"trick or treat" mystery-discount game** with minimal spooky visuals.

### Gaps
- Live captures failed for Sephora, Douglas.de, Zalando, Boots and Rossmann (access denied).
- Common Crawl has no late-October captures for 2022–2025, so the presence or absence of hero banners in the final Halloween week is unverified for those years. Wayback timestamps exist for later manual checking:
  - H&B: 20221028164508, 20231030093445, 20251027140702
  - Lookfantastic: 20221029015832, 20231028202830, 20241029005902, 20251029002850
  - Boots: 20221028202605, 20231029013302, 20241030092618, 20251029000413
  - Cult Beauty: 20221028164103, 20231028175129
  - Sephora FR: 20221028224604, 20231030143702, 20241027142208, 20251029065517
  - Zalando DE: 20221028182019, 20231028190940
  - Myprotein UK: 20221028201601, 20231028175225, 20241030140813, 20251029183713
  - Notino DE: 20221028214727, 20231029001121
- I found no Holland & Barrett Halloween campaign in search.

## 3. How is Halloween perceived in Bulgaria (especially by women ~30–55), and what local occasions clash?

### Takeaway
Halloween is a **real but short, youth- and child-driven occasion** in Bulgaria. Search interest spikes only in the last week of October and in that week is roughly equal to searches for the 1 November Ден на народните будители. It carries a **visible "не е наш празник" / church backlash** that resurfaces every year: a metropolitan's 2014 statement, Elin Pelin's repeated bans in schools (2016, 2017 and again in 2025), and Neshka Robeva's "тиквопоклонци" column in 2025. It also collides directly with **Ден на народните будители (1 Nov)** and in some years **Архангелова задушница** (a day for remembering the dead; Sat 1 Nov in 2025). Ordinary adults in vox pops are relaxed ("всеки сам решава", "децата се радват"). No representative survey exists, and none breaks attitudes down for women aged 30–55. The evidence therefore points to **cute or cosy autumn and pumpkin over scary or dark** for a mature female, health-oriented audience. That conclusion is an inference.

### Cited Findings
**Search interest (Google Trends; I pulled the weekly data via pytrends; geo BG, 2021-01-01 to 2025-12-31; weeks start on Sunday)**
- "Хелоуин" peaks every year in the week containing 31 Oct:
  - Scaled 0–100 against "Halloween" and "тиква", the peak weeks score 2021-10-31: 89, 2022-10-30: 100, 2023-10-29: 62, 2024-10-27: 83, 2025-10-26: 69.
  - It is near zero in June (≈1) and low in September (mean ≈3–5).
  - In 2024 the build-up ran 29 Sep: 10 → 6 Oct: 14 → 13 Oct: 18 → 20 Oct: 32 → 27 Oct: 83, then **collapsed to 4 the following week** (3–9 Nov). 2025 was similar: 19 Oct: 25 → 26 Oct: 69 → 2 Nov: 7. — [Google Trends BG: Хелоуин / Halloween / тиква](https://trends.google.com/trends/explore?date=2021-01-01%202025-12-31&geo=BG&q=%D0%A5%D0%B5%D0%BB%D0%BE%D1%83%D0%B8%D0%BD,Halloween,%D1%82%D0%B8%D0%BA%D0%B2%D0%B0)
- In the Halloween week, "Хелоуин" and "будители" are close. On a common scale: 2023: 35 vs 27; 2024: 46 vs 36; 2025: 39 vs 34; 2022: 56 vs 27; 2021: 50 vs 24. Both drop to ≈1–4 the next week. — [Google Trends BG: Хелоуин / Black Friday / Черен петък / будители](https://trends.google.com/trends/explore?date=2021-01-01%202025-12-31&geo=BG&q=%D0%A5%D0%B5%D0%BB%D0%BE%D1%83%D0%B8%D0%BD,Black%20Friday,%D0%A7%D0%B5%D1%80%D0%B5%D0%BD%20%D0%BF%D0%B5%D1%82%D1%8A%D0%BA,%D0%B1%D1%83%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D0%B8)
- "тиква" (pumpkin) behaves as an **autumn/food** term, not a Halloween one. It peaks in December in 2021, 2022 and 2024 and stays elevated through November (≈17–24) after Halloween searches have collapsed. — same Trends source as the first bullet.

**Popularity and who celebrates**
- Halloween gained popularity after the 1990s, first in language schools, then universities and city clubs. Today children and teenagers celebrate with costumes and themed events, and "shopping centers, restaurants, and bars decorate their spaces and host contests, photo corners, and parades". Views are divided: critics see "a foreign, overly commercial celebration that overshadows local traditions", others "a day for fun, creativity, and escape from routine". (Novinite, 31 Oct 2025) — [Novinite](https://www.novinite.com/articles/235195/Halloween:+From+Celtic+Rituals+to+Modern+Celebration+in+Bulgaria)
- In 2017, Balkan Insight reported that Halloween "has gained significant popularity among children and young people" and that dressing up is banned in some Bulgarian schools. This is per the search snippet; I did not fetch the page. — [Balkan Insight 2017](https://balkaninsight.com/2017/10/31/bulgaria-named-eu-s-largest-pumpkin-producer-on-halloween-10-31-2017/)
- A 2017 Dnes.bg article said there was no study of how Bulgarian society relates to Halloween. This is per the search snippet. I found **no representative survey** from Alpha Research, Gallup, Trend, Market Links or anyone else, 2021–2025. — [Dnes.bg 2017](https://www.dnes.bg/obshtestvo/2017/10/31/helouin-i-bylgariia-lipsvat-li-chudesata-v-praznicite-ni.357865)
- **Street poll, Sofia, 28 Oct 2025** (informal, on camera, no sample size or demographics). Most respondents said everyone should decide for themselves. Quotes: "Децата се радват", "Това за мен е повод да се съберем с приятели", "Нищо лошо не виждам в празнуването на Хелоуин". — [Таралеж, 28.10.2025](https://taralej.bg/obshtestvo/anketa-na-taralej-trqbva-li-da-praznuvame-helouin)
- Women's portal Ladyzone.bg ran an online poll on 1 Nov 2025: "Хелоуин или Денят на будителите?" (options: Будителите / Хелоуин / Всеки празник е повод за радост / И двата / Нито един). No vote counts were shown. — [Ladyzone.bg](https://ladyzone.bg/laifstail/helouin-ili-denjat-na-buditelite-kakvo-praznuvate-vie.html)
- **BG-Mamma**, the main Bulgarian mothers' forum, has a Halloween thread. Per the search-result summary (the page was not fetchable, 403): parents disagree. Some families don't celebrate but don't object if the kindergarten organises costumes; some see it as fun or neighbourhood bonding; some oppose it outright. — [BG-Mamma thread](https://www.bg-mamma.com/?topic=618529.15)

**Backlash ("не е наш празник")**
- **Metropolitan Yoan of Varna (BOC), 31 Oct 2014.** He said Halloween should not become "part of the Bulgarian soul" and called it "especially unacceptable to Orthodox consciousness" and "the worship of evil and death". He urged honouring the Day of the Enlighteners on 1 Nov instead of "foreign-generated affection for the devil". He also noted with alarm that some schools in his diocese would celebrate it. — [Sofia Globe, 2014](https://sofiaglobe.com/?p=38312)
- **Elin Pelin municipality, 2017.** The ban on Halloween in schools, kindergartens and community centres ran for a second year. Mayor Ivailo Simeonov said children "did not even know why they had a day off" and that "There is nothing Christian in this holiday". — [Sofia Globe, 31 Oct 2017](https://sofiaglobe.com/?p=68533)
- **Elin Pelin, 2025.** The mayor again banned Halloween in schools, kindergartens and community centres because 1 Nov is Ден на народните будители (Таралеж, 28.10.2025). Novinite reports quick online backlash, with residents organising their own celebrations in protest. — [Таралеж](https://taralej.bg/obshtestvo/anketa-na-taralej-trqbva-li-da-praznuvame-helouin); [Novinite](https://www.novinite.com/articles/235195/Halloween:+From+Celtic+Rituals+to+Modern+Celebration+in+Bulgaria)
- **Neshka Robeva, 31 Oct 2025.** The famous former rhythmic-gymnastics coach is a public figure with resonance among older Bulgarians; that characterisation is my inference. Her column was titled "Честит празник, тиквопоклонци!". She praised the mayor's ban, called Halloween a "сатанински маскарад" and mocked its promoters as "господа червенотиквеничковци". — [Focus News](https://www.focus-news.net/novini/Bylgaria/Neshka-Robeva-Chestit-praznik-tikvopoklonci-2767363)
- **Civic campaign "НЕ на Хелоуин! ДА на Будителите!"** argues that Halloween "НЯМА МЯСТО в българските училища и детски градини". A 2015 petition was sent to institutions; per the search summary it had about 2,500 signatures. — [Граждани в действие](https://civilactionbg.com/campaign/%D0%B7%D0%B0%D1%89%D0%B8%D1%82%D0%B8-%D0%B4%D0%B5%D1%86%D0%B0%D1%82%D0%B0-%D0%BE%D1%82-%D0%BD%D0%B0%D1%82%D1%80%D0%B0%D0%BF%D0%B2%D0%B0%D0%BD%D0%B5%D1%82%D0%BE-%D0%BD%D0%B0-%D1%85%D0%B5%D0%BB%D0%BE/); [Асоциация Общество и Ценности](https://www.sva.bg/%D0%BF%D0%B8%D1%81%D0%BC%D0%BE%D1%82%D0%BE-%D0%B8-%D0%BF%D0%B5%D1%82%D0%B8%D1%86%D0%B8%D1%8F%D1%82%D0%B0-%D0%BD%D0%B5-%D0%BD%D0%B0-%D1%85%D0%B5%D0%BB%D0%BE%D1%83%D0%B8%D0%BD-%D0%B4%D0%B0-%D0%BD/)
- **"Анти-Хелоуин" in Pernik:** children were invited to Surva (kukeri) traditions instead of pumpkins. This is per the search snippet. — [ZaPernik](https://zapernik.com/220146/anti-helouin-v-pernik-v-kv-czarkva-zovat-deczata-na-surva-vmesto-na-tikvi/)
- BNT also covered the theme ("Народните будители под маската на Хелоуин"); I did not fetch it. — [BNT](https://bnt.bg/bg/a/narodnite-buditeli-pod-maskata-na-helouin-41203)

**Clashing local dates**
- **1 November, Ден на народните будители:** a fixed national day, a school holiday since its revival by Parliament in 1992. — [Sofia Globe 2017](https://sofiaglobe.com/?p=68533)
- **Архангелова задушница**, the last big remembrance-of-the-dead Saturday of the year, falls on the first Saturday before Archangel Michael's Day (8 Nov). In **2025 it fell on Saturday 1 Nov**, the day after Halloween and the same day as Будители. — [Actualno](https://www.actualno.com/curious/poslednata-zadushnica-prez-2025-koga-e-i-kakvo-se-pravi-news_2496371.html); [Iskra.bg](https://www.iskra.bg/arhangelova-zadushnitsa-2025-koga-se-pada-i-kakvi-sa-traditsiite-na-tozi-den/)

**Words and phrases used by Bulgarian shops (OBSERVED unless noted)**
- "Ужасно яки оферти" and "50 000 продукта на **плашещо добри цени**" (Ozone, 2026).
- "**Страшно добра оферта**" / "Scary offer" (Pulse, 2026).
- "**Грим за Хелоуин** за **тъмната страна във вас**" / "Вдъхновете се" (Notino BG, 2026).
- "Хелоуин: **Зловещи вдъхновения**", "**страховито красив**", "уютна семейна вечер с децата" (dm BG).
- "Приготвeте се за Хелоуин с NYX" (dm BG).
- "Хелоуин в Lidl" (Lidl 2025).
- "Тиква Хелоуин рисувана" (Kaufland 2024).
- Pumpkin used as an autumn, non-Halloween cue: "Крем супа от тиква, Есенна рецепта", "Pumpkin Spice Latte" candle (dm BG 2025), "Чийзкейк с тиква" (Lidl 2024).
- I did **not** observe "Страшно добри цени" or "Тиквено" verbatim on any shop. A web search for "Страшно добри цени" Хелоуин found no shop using that exact phrase. — sources as cited in sections 1 and 2

### Inferences
- Halloween in Bulgaria is a **kids', teens' and party occasion**. For women 30–55 it is mostly experienced as parents (costumes, kindergarten parties) or as a reason for a social evening. That makes **"family-friendly, cute, cosy"** framing safer than horror.
- There is an active minority, plus church and nationalist voices, for whom Halloween is "сатанински" or "чужд". A brand selling health products to this demographic risks little by being light, and something by being dark: skulls, blood, demons or witches next to "health" claims. Older and more traditional customers in smaller towns, which is typical of cash-on-delivery buyers, are more likely to hold the "не е наш празник" view. This is an inference; I found no survey to confirm it.
- **Pumpkin is culturally neutral in Bulgaria.** It is an autumn food (тиква, тиквеник, крем супа) and searches stay high into December, so a pumpkin or autumn-leaf accent reads as "есен" even to people who dislike Halloween.
- A Halloween theme should **end on the evening of 31 Oct**. On 1 Nov (Будители, and in some years Задушница) "spooky" imagery could look tone-deaf, especially imagery of graves or death.
- Light word-play ("страшно добра оферта", "страшно добри цени", "плашещо ниски цени") is used by Bulgarian brands and is low-risk. It can work as text alone without spooky imagery.

### Gaps
- There is no representative Bulgarian survey on Halloween attitudes, and certainly none broken down by gender and age 30–55.
- The BG-Mamma thread content is known only from the search summary. A comment-level sentiment analysis was not possible.
- I found no official Holy Synod statement on Halloween in 2021–2025 (searches on bg-patriarshia.bg returned nothing); church statements found are from individual metropolitans (2014).
- I did not verify the 2026 Архангелова задушница date with a source. By the stated rule (the Saturday before 8 Nov, which is a Sunday in 2026) it would be **Sat 7 Nov 2026**; this is an inference.

## 4. When do shops switch to Halloween visuals, and when to Black Friday (Bulgaria and EU)?

### Takeaway
In Bulgaria, Halloween site visuals appear roughly **from mid-October and intensify in the final 7–10 days** (Notino's banner is tagged week 43; dm's homepage teaser was live by 15 Oct 2025). They come down **by 1 November**. **Black Friday / "Black Week" / "Black November" takes over immediately**: Fashion Days started Black Friday on 31 Oct 2025 and 4 Nov 2024, Kaufland had "black week" by 3 Nov 2024, and BENU ran "Black November" by 3 Nov 2024. eMAG's main Black Friday day is mid-November (14 Nov 2025, 13 Nov 2026). In EU and UK beauty, **Christmas** is already on the homepage in late October (Boots 2021, Lookfantastic and Cult Beauty in 2026, Notino BG on 16 Oct 2025).

### Cited Findings
- **Halloween switch-on:**
  - Notino's Halloween homepage banner files are tagged `w43_26` (week 43 = 19–25 Oct 2026).
  - Notino BG's homepage on 16 Oct 2025 (week 42) had no Halloween.
  - dm BG's homepage had a "Хелоуин" teaser on 15 Oct 2025.
  - dm BG's NYX Halloween livestream was on 21 Oct 2026.
  - Rossmann.de's Halloween app teasers were tagged "2025_kw43". — sources as in sections 1 and 2 ([Notino BG banner](https://cdn.notinoimg.com/c=85/images/gallery/ba/12/bg_desk_hp_halloween_w43_26_ff4f30.jpg); [CC dm BG 2025-43](https://index.commoncrawl.org/CC-MAIN-2025-43-index?url=https://www.dm-drogeriemarkt.bg/&output=json); [dm dmLIVE](https://www.dm-drogeriemarkt.bg/services/klientski-programi-i-uslugi/dmlive); [CC Rossmann 2025-47](https://index.commoncrawl.org/CC-MAIN-2025-47-index?url=https://www.rossmann.de/de/&output=json))
- **Halloween switch-off:**
  - dm BG's homepage on 14 Nov 2025 had no Halloween teaser, only pumpkin-soup and autumn content.
  - Kaufland on 3 Nov 2024 still had a leftover "Тиква Хелоуин" offer tile under a Black Week hero.
  - Pulse still showed "🎃 Halloween Events by Pulse!" on 16 Nov 2025. That is an events page, not a sale. — [CC dm BG 2025-47](https://index.commoncrawl.org/CC-MAIN-2025-47-index?url=https://www.dm-drogeriemarkt.bg/&output=json); [CC Kaufland 2024-46](https://index.commoncrawl.org/CC-MAIN-2024-46-index?url=https://www.kaufland.bg/&output=json); [CC Pulse 2025-47](https://index.commoncrawl.org/CC-MAIN-2025-47-index?url=https://pulsefit.bg/&output=json)
- **Fashion Days BG:**
  - 2024-11-03 16:52 homepage: "**BLACK FRIDAY е толкова близо! Старт: УТРЕ след 7:00 ч.!**" (i.e. a 4 Nov 2024 start).
  - 2024-11-09: campaign banner coded "BLACK FRIDAY 04-10 NOIEMBRIE".
  - 2025: "Fashion Days Black Friday 2025 ще стартира на **31 октомври** след 07:00 ч." (Profitshare BG, published 28.10.2025).
  - 2025-11-15: "BLACK FRIDAY AFTERPARTY 10-19 NOV".
  - A coupon site claims a 6 Nov 2024 start, which conflicts with the CC capture; I treat the CC capture as primary. — [CC Fashion Days 2024-46](https://index.commoncrawl.org/CC-MAIN-2024-46-index?url=https://www.fashiondays.bg/&output=json); [Profitshare BG blog](https://blog.profitshare.bg/gotvi-se-za-fashion-days-black-friday-nachalo-31-oktomvri-sled-0700-chasa/); [Promobroshura](https://promobroshura.com/fashion-days-black-friday/)
- **Kaufland BG, 2024-11-03:** hero teaser "Ексклузивни black week оферти още от неделя". — [CC Kaufland 2024-46](https://index.commoncrawl.org/CC-MAIN-2024-46-index?url=https://www.kaufland.bg/&output=json)
- **BENU pharmacy, 2024-11-03:** "Black November" in the top bar and in the e-shop menu. — [CC index CC-MAIN-2024-46, benu.bg](https://index.commoncrawl.org/CC-MAIN-2024-46-index?url=https://www.benu.bg/&output=json)
- **eMAG BG Black Friday dates:**
  - 2025: 14 Nov 2025, Friday morning (Profitshare via Crazy-Deals; 24chasa, Trud and Standart reported it as company announcements).
  - 2024: Crazy-Deals cites a 15 Nov 2024 start. The CC capture from 14 Nov 2024 shows a "Guide Black Friday" header link.
  - 2026: 13 Nov 2026, "the first one where the offers will be entirely in euros".
  - eMAG Romania runs about a week earlier (8 Nov 2024; 10 Nov 2023). — [Crazy-Deals.bg](https://crazy-deals.bg/black-friday-2025-v-bulgaria-nai-dobrite-saveti-za-umno-pazaruvane-i-realni-oferti/); [Standart](https://www.standartnews.com/biznes/emag-black-friday-2025-za-30-minuti-sled-nachaloto-na-kampaniyata-balgarite-sa-porachali-30-poveche-produkti-ot-minalata-godina-614023.html); [Kafene.bg (2026 date)](https://kafene.bg/%D1%82%D0%B0%D0%B7%D0%B8-%D0%B3%D0%BE%D0%B4%D0%B8%D0%BD%D0%B0-emag-black-friday-%D1%89%D0%B5-%D0%B1%D1%8A%D0%B4%D0%B5-%D0%BD%D0%B0-13-%D0%BD%D0%BE%D0%B5%D0%BC%D0%B2%D1%80%D0%B8/); [Business Forum RO 2024](https://www.businessforum.ro/economy/20241104/emag-black-friday-brings-on-november-8-over-15-million-offers-at-best-price-of-the-year-990)
- **"Black November":** "Много брандове вече разширяват кампанията в рамките на „Black November", с отстъпки през целия месец" (Crazy-Deals, 2025). Chudenka.bg's 2026 list gives 6 Nov as the earliest campaign start and names Parfium.bg among stores using "Black November". This is per the search summary; the page itself listed no dates when I fetched it. — [Crazy-Deals.bg](https://crazy-deals.bg/black-friday-2025-v-bulgaria-nai-dobrite-saveti-za-umno-pazaruvane-i-realni-oferti/); [Chudenka.bg](https://chudenka.bg/cheren-petak/)
- **Search behaviour (Google Trends BG):**
  - "Черен петък" searches start the week right after Halloween: 2024-11-03 week: 39; 2025-11-02: 30; 2023-11-05: 42.
  - They peak in the second week of November: 2021-11-14: 100; 2022-11-13: 95; 2023-11-12: 75; 2024-11-10: 72; 2025-11-09: 58.
  - "Хелоуин" falls to ≈1–4 in those same weeks. — [Google Trends BG](https://trends.google.com/trends/explore?date=2021-01-01%202025-12-31&geo=BG&q=%D0%A5%D0%B5%D0%BB%D0%BE%D1%83%D0%B8%D0%BD,Black%20Friday,%D0%A7%D0%B5%D1%80%D0%B5%D0%BD%20%D0%BF%D0%B5%D1%82%D1%8A%D0%BA,%D0%B1%D1%83%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D0%B8)
- **Christmas already in late October:**
  - Boots, 27 Oct 2021: "Start your Christmas shopping…".
  - Notino BG, 16 Oct 2025: baubles in the hero and "Подаръци за Коледа" in the nav.
  - dm BG, 25 Oct 2026: a "Коледни календари" tile next to the "Halloween" tile.
  - Lookfantastic and Cult Beauty, 25 Oct 2026: "Christmas" nav and "Christmas shop is open".
  - Myprotein UK, 25 Oct 2026: "Advent" in the nav.
  - Rossmann.de, 7 Nov 2025: Advent calendars in ex-Halloween slots. — sources as in section 2

### Inferences
- The **effective Halloween visual window in Bulgaria is about 20–31 October** (search interest more than doubles in the final week). An accent added around 20 October and removed on 1 November matches both shop practice and demand.
- **From 1 November the Bulgarian market moves straight into Black Friday mode.** Fashion Days, BENU and Kaufland were live by 31 Oct–4 Nov; consumer search for "Черен петък" ramps up in the first November week and peaks around eMAG's day (13 Nov in 2026).
- A small store therefore has a short window. Options:
  - a light Halloween/autumn accent 20–31 Oct, then a neutral "Black November / Черен петък" look from 1 Nov; or
  - skip Halloween and launch Black November early. Halloween's search interest is concentrated in one week and skews to children, teens and parties.
- Because 1 Nov is Будители (and in 2025 also Задушница), any Halloween creative should be scheduled to switch off **at midnight on 31 Oct**, not left running into the weekend.

### Gaps
- I have no direct observation of eMAG's late-October homepage in any year, so I could not tell whether eMAG runs a pre-Black-Friday Halloween "campaign" in Bulgaria. Search found only a 2017 Romanian example.
- Exact Black Friday start dates for Notino BG, Douglas BG, dm BG, Lilly and the pharmacy chains in 2021–2025 were not found.
- The Fashion Days 2024 start date conflicts: the CC capture implies 4 Nov, while Promobroshura says 6 Nov.
