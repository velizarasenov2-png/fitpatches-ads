# Who Bulgarian ingrown-hair competitors actually reach on Meta: EU transparency audience data for an ICP (research date: 6 Oct 2026)

**How the data was collected.** Firecrawl's scrape tool in this session has no click "actions" and the account reported low credits, so the Meta Ad Library was read with a headless Chromium (Playwright) session instead. For each keyword query and advertiser page (country=BG, statuses all/active/inactive), the script parsed the ad list that the Ad Library page embeds, then requested each ad's "See ad details" data. That is the same `AdLibraryV3AdDetailsQuery` call the Ad Library UI makes when the ad-details modal opens. It returns Meta's **EU transparency** block for that ad: targeted locations, targeted age range, targeted gender, `eu_total_reach`, and reach broken down by country × age group × gender. Meta documents that ads delivered to the EU carry total reach plus age, gender and location data — [Meta Ad Library API page](https://www.facebook.com/ads/library/api/). All scraping took place on 6 Oct 2026 between 18:10 and 19:20 UTC.

- **Sample:** 487 ads returned EU transparency data. **395** were classed as relevant to hair removal, ingrown hairs or intimate care. Excluded were other products from the same brands (for example LUMI's eye cream, BeNatural's lemon cream, and Vitalaiz tattoo-removal and body ads), B2B laser-equipment sellers, and off-topic hits.
- **Collection limit:** Meta's search endpoint rate-limited repeatedly (`"Rate limit exceeded", code 1675004`). Each query or page view therefore yielded only the **first ~30 ads**, which the Ad Library sorts by impressions. Sample sizes are stated per advertiser below.
- **Definitions:**
  - "Reach" is Meta's per-ad `eu_total_reach` (unique EU accounts). Sums across ads are **not de-duplicated**.
  - "% women / men" and age splits are shares of the summed age × gender reach counts. Age columns are always **18-24 / 25-34 / 35-44 / 45-54 / 55-64 / 65+**.
  - "Open targeting" means gender = All and age 18–65+, so Meta's delivery, not the advertiser, chose who saw the ad.
- **Full data:** per-ad raw data for all 487 ads is in `competitor_meta_audiences_ads.csv` in this folder (ad URL, targeting, reach, % by gender, % by age, female and male counts by age, primary text, landing URL).

## 1. Direct at-home ingrown-hair competitors (Deroli, LUMI, Savenae, PFB Vanish/SimplyBeauty): who do their Meta ads reach?

### Takeaway
Across **79 direct ingrown-hair ads (2.36M summed EU reach)**, Meta delivered **91.4% to women and 7.5% to men**. **74% of all reach went to 18–34-year-olds**: 35% were 18–24 and 39% were 25–34. 35–44 took 18%, and everyone 45+ only 8%. The two brands ran different targeting settings (LUMI: all genders 18–65; Deroli: mostly women-only 18–65) and still got the same result. When gender was left open, the algorithm still sent 91% of reach to women. Savenae itself has **no ads** in the BG Ad Library.

### Cited Findings
**Category summary (all A-category ads)**

| Category | Ads with EU data | Summed EU reach | % women / men / unknown | Age split % (18-24/25-34/35-44/45-54/55-64/65+) | Subset with open targeting |
|---|---|---|---|---|---|
| A. Ingrown-hair treatment (direct) | 79 | 2,356,050 | 91.4 / 7.5 / 1.0 | 35 / 39 / 18 / 6 / 1 / 1 | 46 ads: 91.1 / 7.8; 36 / 40 / 17 / 6 / 1 / 1 |

**Per-advertiser summary**

| Cat | Advertiser | Ads (active 6 Oct) | First → last start date | Targeting settings | Locations | Summed EU reach | % W / M | Age split % | Highest-reach ad |
|---|---|---|---|---|---|---|---|---|---|
| A | LUMI | 30 (3 active) | 2025-10-16 → 2026-09-29 | All 18-65 ×30 | Bulgaria ×30 | 1,900,121 | 91 / 8 | 36 / 40 / 17 / 6 / 1 / 1 | [3594968063986071](https://www.facebook.com/ads/library/?id=3594968063986071) (260,032) |
| A | Deroli Cosmetics | 48 (30 active) | 2026-04-19 → 2026-10-06 | Women 18-65 ×32; All 18-65 ×16 | Bulgaria ×48 | 454,760 | 93 / 7 | 34 / 37 / 20 / 7 / 2 / 1 | [1603053431394356](https://www.facebook.com/ads/library/?id=1603053431394356) (53,125) |
| A | SimplyBeauty | 1 (1 active) | 2026-09-30 → 2026-09-30 | Women 35-65 ×1 | Bulgaria ×1 | 1,169 | 100 / 0 | 0 / 0 / 48 / 38 / 10 / 4 | [2316889675723385](https://www.facebook.com/ads/library/?id=2316889675723385) (1,169) |

- **Deroli Cosmetics** (page id 994779313728183): all **48** BG ads in the Ad Library were captured. The page view showed "~30 results" active and "~18 results" inactive — [Deroli active](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BG&view_all_page_id=994779313728183&search_type=page&media_type=all); [Deroli inactive](https://www.facebook.com/ads/library/?active_status=inactive&ad_type=all&country=BG&view_all_page_id=994779313728183&search_type=page&media_type=all).
  - The first ads (19–23 Apr 2026, landing /smooth-roller) had open targeting and skewed youngest: 54% of reach aged 18–24 — [ad 1275023818033998](https://www.facebook.com/ads/library/?id=1275023818033998).
  - From 4 May to Aug 2026 Deroli switched to **Women 18–65**. On 1 Oct 2026 it switched back to **All genders 18–65**. The October open-gender ads still delivered 89–93% to women — [ad 1580431803886169](https://www.facebook.com/ads/library/?id=1580431803886169) (1,693 reach, 90% W, 20/33/31/13/3/1); [ad 1763489551754055](https://www.facebook.com/ads/library/?id=1763489551754055) (5,424 reach, 89% W, 34/41/19/5/1/0).
  - The background note's page id 61572163727533 is not the Ad Library page id. The correct one is 994779313728183.
- **LUMI** (page id 599988969856679) has 30 relevant ingrown-serum ads with EU data, out of ~3 active plus ~82 inactive on the page. That is the first 30 inactive by impressions plus all active ones — [LUMI active](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BG&view_all_page_id=599988969856679&search_type=page&media_type=all); [LUMI inactive](https://www.facebook.com/ads/library/?active_status=inactive&ad_type=all&country=BG&view_all_page_id=599988969856679&search_type=page&media_type=all).
  - **Every one** of the 30 ads targets All genders 18–65 in Bulgaria. Each one delivered 85–95% to women, except one 9-day ad at 73% — [ad 1234925171824996](https://www.facebook.com/ads/library/?id=1234925171824996).
  - LUMI has run the same "Единственият продукт…" copy since 16 Oct 2025.
  - The longest-running LUMI ads, the likeliest profitable ones, are:
    - [ad 3594968063986071](https://www.facebook.com/ads/library/?id=3594968063986071): 170 days, 260,032 reach, 91% W, 32/40/19/6/1/1
    - [ad 1299129028935876](https://www.facebook.com/ads/library/?id=1299129028935876): 155 days, 235,123 reach, 93% W, 28/35/24/10/3/1
    - [ad 1302228438511250](https://www.facebook.com/ads/library/?id=1302228438511250): 125 days, 176,716 reach, 91% W, 35/42/17/4/1/0
  - LUMI also runs other products (an under-eye firming cream) from the same page. Those ads were excluded.
- **SimplyBeauty** (official PFB Vanish importer) ran one content ad, targeted **Women 35–65**. It reached only 1,169 people (48% aged 35–44) — [ad 2316889675723385](https://www.facebook.com/ads/library/?id=2316889675723385).
- **Savenae** has no ads in the BG Ad Library:
  - Keyword "savenae" (all statuses, BG) returned "No ads match" — [query](https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=BG&q=savenae&search_type=keyword_unordered&media_type=all).
  - Keyword "savenae.com" also returned "No ads match" — [query](https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=BG&q=savenae.com&search_type=keyword_unordered&media_type=all).
  - The product page links to no Facebook or Instagram page. It sells "SAVENAE Ексфолиращи тампони при враснали косъмчета" at €18,90 (regular €22,90) — [savenae.com](https://savenae.com/products/savenae-smooth-reset-pads).
  - A query for "ексфолиращи тампони" returned no parseable ads — [query](https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=BG&q=%D0%B5%D0%BA%D1%81%D1%84%D0%BE%D0%BB%D0%B8%D1%80%D0%B0%D1%89%D0%B8%20%D1%82%D0%B0%D0%BC%D0%BF%D0%BE%D0%BD%D0%B8&search_type=keyword_unordered&media_type=all).

**Women × age grid for category A** (% of all A-category reach; women / men):

| Category | 18-24 W / M | 25-34 W / M | 35-44 W / M | 45-54 W / M | 55-64 W / M | 65+ W / M |
|---|---|---|---|---|---|---|
| A. Ingrown-hair treatment (direct) | 32.6 / 2.1 | 35.6 / 3.1 | 16.3 / 1.6 | 5.2 / 0.6 | 1.2 / 0.2 | 0.5 / 0.1 |

**Ads that ran ≥30 days (a proxy for profitable ads) versus shorter tests, category A**

| Subset (category A) | Ads | Summed reach | % W / M | Age split % | Women-only age split (% of total reach) |
|---|---|---|---|---|---|
| ran >=30 days | 29 | 1,383,283 | 91.6 / 7.4 | 34 / 39 / 19 / 6 / 1 / 1 | F-only age split: 31 / 36 / 17 / 5 / 1 / 1 |
| ran <30 days | 50 | 972,767 | 91.2 / 7.7 | 37 / 39 / 17 / 6 / 1 / 1 | F-only age split: 34 / 35 / 15 / 5 / 1 / 0 |

**Targeting setting versus actual delivery, category A**

| Subset | Ads | Summed reach | % W / M / unknown | Age split % |
|---|---|---|---|---|
| A: targeted Women | 33 | 432,549 | 93.0 / 6.5 / 0.6 | 33 / 37 / 21 / 7 / 2 / 1 |
| A: targeted All genders | 46 | 1,923,501 | 91.1 / 7.8 / 1.1 | 36 / 40 / 17 / 6 / 1 / 1 |

**Per-ad table: Deroli Cosmetics** (all 48 BG ads; "last" = last delivery date shown by Meta; angle tags come from automatic keyword matching on the primary text)

| Ad | Start → last (days) | Status 6 Oct | Targeting | EU reach | % W / M | Age split % | Angle tags | Primary-text hook | Landing |
|---|---|---|---|---|---|---|---|---|---|
| [1275023818033998](https://www.facebook.com/ads/library/?id=1275023818033998) | 2026-04-19 → 2026-04-23 (5d) | Inactive | All 18-65, Bulgaria | 11,204 | 93 / 6 | 54 / 35 / 7 / 2 / 1 / 1 | dynamic/catalog (copy not visible) | (dynamic catalog text) | derolibg.com/products/smooth-roller |
| [1315126500473191](https://www.facebook.com/ads/library/?id=1315126500473191) | 2026-04-19 → 2026-04-22 (4d) | Inactive | All 18-65, Bulgaria | 2,085 | 70 / 29 | 44 / 34 / 12 / 6 / 2 / 1 | failed/painful alternatives, mechanism/education, fast-result promise, discount/urgency | Враснали косми, тъмни петна и раздразнена кожа след депилация –  три проблема, с които всяка же | derolibg.com/products/smooth-roller |
| [1272228545102742](https://www.facebook.com/ads/library/?id=1272228545102742) | 2026-04-19 → 2026-04-22 (4d) | Inactive | All 18-65, Bulgaria | 300 | 76 / 24 | 22 / 28 / 19 / 16 / 10 / 6 | dynamic/catalog (copy not visible) | (dynamic catalog text) | derolibg.com/products/smooth-roller |
| [944891101631684](https://www.facebook.com/ads/library/?id=944891101631684) | 2026-04-19 → 2026-04-19 (1d) | Inactive | All 18-65, Bulgaria | 5 | 80 / 0 | 0 / 0 / 0 / 0 / 60 / 40 | dynamic/catalog (copy not visible) |  | derolibg.com/products/smooth-roller |
| [1658061775509838](https://www.facebook.com/ads/library/?id=1658061775509838) | 2026-04-19 → 2026-04-21 (3d) | Inactive | All 18-65, Bulgaria | 18 | 28 / 72 | 33 / 50 / 0 / 6 / 6 / 6 | shame/hiding & confidence, failed/painful alternatives, fast-result promise, summer/beach | Уморена ли си да криеш кожата си?  От враснали косми по бикини зоната, от тъмните петна по крак | http://derolibg.com/ |
| [1502043934927778](https://www.facebook.com/ads/library/?id=1502043934927778) | 2026-05-04 → 2026-05-05 (2d) | Inactive | Women 18-65, Bulgaria | 17 | 100 / 0 | 29 / 53 / 18 / 0 / 0 / 0 | dynamic/catalog (copy not visible) | (dynamic catalog text) | derolibg.com/products/smoothing-solution |
| [1277157651292625](https://www.facebook.com/ads/library/?id=1277157651292625) | 2026-05-04 → 2026-10-06 (156d) | Active | Women 18-65, Bulgaria | 23,255 | 94 / 5 | 40 / 33 / 18 / 6 / 2 / 1 | dynamic/catalog (copy not visible) | (dynamic catalog text) | derolibg.com/products/smoothing-solution |
| [1420963646502602](https://www.facebook.com/ads/library/?id=1420963646502602) | 2026-05-04 → 2026-10-03 (153d) | Active | Women 18-65, Bulgaria | 556 | 96 / 3 | 27 / 36 / 26 / 8 / 2 / 1 | dynamic/catalog (copy not visible) | (dynamic catalog text) | derolibg.com/products/smoothing-solution |
| [4335667636751697](https://www.facebook.com/ads/library/?id=4335667636751697) | 2026-05-04 → 2026-10-05 (155d) | Active | Women 18-65, Bulgaria | 35,101 | 94 / 5 | 43 / 37 / 15 / 4 / 1 / 0 | dynamic/catalog (copy not visible) | (dynamic catalog text) | derolibg.com/products/smoothing-solution |
| [1272999705036195](https://www.facebook.com/ads/library/?id=1272999705036195) | 2026-05-04 → 2026-08-28 (117d) | Inactive | Women 18-65, Bulgaria | 39,983 | 90 / 10 | 32 / 35 / 22 / 8 / 2 / 1 | dynamic/catalog (copy not visible) | (dynamic catalog text) | derolibg.com/products/smoothing-solution |
| [2114944995746890](https://www.facebook.com/ads/library/?id=2114944995746890) | 2026-05-04 → 2026-05-05 (2d) | Inactive | Women 18-65, Bulgaria | 220 | 93 / 7 | 46 / 26 / 19 / 6 / 2 / 0 | dynamic/catalog (copy not visible) | (dynamic catalog text) | derolibg.com/products/smoothing-solution |
| [1686005882750535](https://www.facebook.com/ads/library/?id=1686005882750535) | 2026-05-04 → 2026-05-05 (2d) | Inactive | Women 18-65, Bulgaria | 982 | 92 / 7 | 50 / 37 / 9 / 2 / 1 / 1 | dynamic/catalog (copy not visible) | (dynamic catalog text) | derolibg.com/products/smoothing-solution |
| [946734571517749](https://www.facebook.com/ads/library/?id=946734571517749) | 2026-05-04 → 2026-10-06 (156d) | Active | Women 18-65, Bulgaria | 34,468 | 95 / 5 | 38 / 38 / 16 / 6 / 1 / 1 | dynamic/catalog (copy not visible) | (dynamic catalog text) | derolibg.com/products/smoothing-solution |
| [951623180938096](https://www.facebook.com/ads/library/?id=951623180938096) | 2026-05-04 → 2026-10-04 (154d) | Active | Women 18-65, Bulgaria | 10,542 | 94 / 6 | 46 / 35 / 14 / 4 / 1 / 1 | dynamic/catalog (copy not visible) | (dynamic catalog text) | derolibg.com/products/smoothing-solution |
| [35134290669548934](https://www.facebook.com/ads/library/?id=35134290669548934) | 2026-05-05 → 2026-10-06 (155d) | Active | Women 18-65, Bulgaria | 39,257 | 96 / 4 | 43 / 35 / 15 / 5 / 1 / 0 | dynamic/catalog (copy not visible) | (dynamic catalog text) | derolibg.com/products/smoothing-solution |
| [26610984555252096](https://www.facebook.com/ads/library/?id=26610984555252096) | 2026-05-07 → 2026-10-03 (150d) | Active | Women 18-65, Bulgaria | 744 | 95 / 5 | 33 / 39 / 21 / 5 / 1 / 1 | dynamic/catalog (copy not visible) | (dynamic catalog text) | derolibg.com/products/smoothing-solution |
| [1024217403456991](https://www.facebook.com/ads/library/?id=1024217403456991) | 2026-06-20 → 2026-10-06 (109d) | Active | Women 18-65, Bulgaria | 6,932 | 92 / 8 | 35 / 40 / 19 / 5 / 1 / 0 | failed/painful alternatives, mechanism/education, fast-result promise, discount/urgency | Враснали косми, тъмни петна и раздразнена кожа след депилация –  три проблема, с които всяка же | derolibg.com/products/smoothing-solution |
| [1029734312805937](https://www.facebook.com/ads/library/?id=1029734312805937) | 2026-06-20 → 2026-10-06 (109d) | Active | Women 18-65, Bulgaria | 50,425 | 91 / 8 | 33 / 42 / 19 / 5 / 1 / 0 | failed/painful alternatives, mechanism/education, fast-result promise, discount/urgency | Враснали косми, тъмни петна и раздразнена кожа след депилация –  три проблема, с които всяка же | derolibg.com/products/smoothing-solution |
| [2301460510639874](https://www.facebook.com/ads/library/?id=2301460510639874) | 2026-08-03 → 2026-08-07 (5d) | Inactive | Women 18-65, Bulgaria | 7,256 | 94 / 6 | 22 / 40 / 27 / 9 / 2 / 1 | failed/painful alternatives, mechanism/education, fast-result promise, discount/urgency | Враснали косми, тъмни петна и раздразнена кожа след депилация –  три проблема, с които всяка же | derolibg.com/products/smoothing-solution |
| [1471051168376414](https://www.facebook.com/ads/library/?id=1471051168376414) | 2026-08-03 → 2026-08-07 (5d) | Inactive | Women 18-65, Bulgaria | 24,275 | 94 / 6 | 23 / 37 / 28 / 9 / 2 / 1 | failed/painful alternatives, mechanism/education, fast-result promise, discount/urgency | Враснали косми, тъмни петна и раздразнена кожа след депилация –  три проблема, с които всяка же | derolibg.com/products/smoothing-solution |
| [1553004756499926](https://www.facebook.com/ads/library/?id=1553004756499926) | 2026-08-06 → 2026-10-06 (62d) | Active | Women 18-65, Bulgaria | 3,632 | 93 / 7 | 24 / 35 / 29 / 10 / 2 / 1 | failed/painful alternatives, mechanism/education, fast-result promise, discount/urgency | Враснали косми, тъмни петна и раздразнена кожа след депилация –  три проблема, с които всяка же | derolibg.com/products/smoothing-solution |
| [1603053431394356](https://www.facebook.com/ads/library/?id=1603053431394356) | 2026-08-06 → 2026-08-20 (15d) | Inactive | Women 18-65, Bulgaria | 53,125 | 92 / 8 | 22 / 34 / 28 / 12 / 3 / 1 | failed/painful alternatives, mechanism/education, fast-result promise, discount/urgency | Враснали косми, тъмни петна и раздразнена кожа след депилация –  три проблема, с които всяка же | derolibg.com/products/smoothing-solution |
| [1420882626630383](https://www.facebook.com/ads/library/?id=1420882626630383) | 2026-08-06 → 2026-10-06 (62d) | Active | Women 18-65, Bulgaria | 1,203 | 91 / 8 | 24 / 34 / 27 / 12 / 2 / 1 | failed/painful alternatives, mechanism/education, fast-result promise, discount/urgency | Враснали косми, тъмни петна и раздразнена кожа след депилация –  три проблема, с които всяка же | derolibg.com/products/smoothing-solution |
| [1622593279581302](https://www.facebook.com/ads/library/?id=1622593279581302) | 2026-08-06 → 2026-08-15 (10d) | Inactive | Women 18-65, Bulgaria | 51,192 | 94 / 6 | 30 / 40 / 22 / 7 / 1 / 1 | failed/painful alternatives, mechanism/education, fast-result promise, discount/urgency | Враснали косми, тъмни петна и раздразнена кожа след депилация –  три проблема, с които всяка же | derolibg.com/products/smoothing-solution |
| [4387115234834729](https://www.facebook.com/ads/library/?id=4387115234834729) | 2026-08-14 → 2026-10-05 (53d) | Active | Women 18-65, Bulgaria | 810 | 89 / 10 | 28 / 30 / 28 / 11 / 3 / 1 | failed/painful alternatives, mechanism/education, fast-result promise, discount/urgency | Враснали косми, тъмни петна и раздразнена кожа след депилация –  три проблема, с които всяка же | derolibg.com/products/smoothing-solution |
| [1069278385675428](https://www.facebook.com/ads/library/?id=1069278385675428) | 2026-08-18 → 2026-10-02 (46d) | Active | Women 18-65, Bulgaria | 3,078 | 89 / 10 | 33 / 39 / 20 / 6 / 1 / 0 | failed/painful alternatives, mechanism/education, fast-result promise, discount/urgency | Враснали косми, тъмни петна и раздразнена кожа след депилация –  три проблема, с които всяка же | derolibg.com/products/smoothing-solution |
| [1999094070805646](https://www.facebook.com/ads/library/?id=1999094070805646) | 2026-08-18 → 2026-08-28 (11d) | Inactive | Women 18-65, Bulgaria | 24,763 | 93 / 6 | 35 / 38 / 19 / 6 / 1 / 0 | failed/painful alternatives, mechanism/education, fast-result promise, discount/urgency | Враснали косми, тъмни петна и раздразнена кожа след депилация –  три проблема, с които всяка же | derolibg.com/products/smoothing-solution |
| [1654637272895648](https://www.facebook.com/ads/library/?id=1654637272895648) | 2026-08-18 → 2026-09-28 (42d) | Active | Women 18-65, Bulgaria | 52 | 90 / 8 | 17 / 35 / 38 / 10 / 0 / 0 | failed/painful alternatives, mechanism/education, fast-result promise, discount/urgency | Враснали косми, тъмни петна и раздразнена кожа след депилация –  три проблема, с които всяка же | derolibg.com/products/smoothing-solution |
| [1738644290792121](https://www.facebook.com/ads/library/?id=1738644290792121) | 2026-08-18 → 2026-10-01 (45d) | Active | Women 18-65, Bulgaria | 245 | 94 / 5 | 26 / 39 / 28 / 7 / 0 / 0 | dynamic/catalog (copy not visible) | (dynamic catalog text) | derolibg.com/products/smoothing-solution |
| [1563307325445887](https://www.facebook.com/ads/library/?id=1563307325445887) | 2026-08-18 → 2026-10-02 (46d) | Active | Women 18-65, Bulgaria | 48 | 92 / 4 | 17 / 40 / 33 / 10 / 0 / 0 | failed/painful alternatives, mechanism/education, fast-result promise, discount/urgency | Враснали косми, тъмни петна и раздразнена кожа след депилация –  три проблема, с които всяка же | derolibg.com/products/smoothing-solution |
| [1038139255496638](https://www.facebook.com/ads/library/?id=1038139255496638) | 2026-08-18 → 2026-08-28 (11d) | Inactive | Women 18-65, Bulgaria | 11,907 | 93 / 6 | 24 / 35 / 26 / 11 / 3 / 1 | failed/painful alternatives, mechanism/education, fast-result promise, discount/urgency | Враснали косми, тъмни петна и раздразнена кожа след депилация –  три проблема, с които всяка же | derolibg.com/products/smoothing-solution |
| [2432836083793711](https://www.facebook.com/ads/library/?id=2432836083793711) | 2026-08-18 → 2026-10-03 (47d) | Active | Women 18-65, Bulgaria | 24 | 92 / 8 | 42 / 25 / 25 / 8 / 0 / 0 | failed/painful alternatives, mechanism/education, fast-result promise, discount/urgency | Враснали косми, тъмни петна и раздразнена кожа след депилация –  три проблема, с които всяка же | derolibg.com/products/smoothing-solution |
| [901015179339813](https://www.facebook.com/ads/library/?id=901015179339813) | 2026-08-18 → 2026-09-28 (42d) | Active | Women 18-65, Bulgaria | 69 | 94 / 6 | 21 / 36 / 23 / 14 / 4 / 1 | dynamic/catalog (copy not visible) | (dynamic catalog text) | derolibg.com/products/smoothing-solution |
| [1001243686284101](https://www.facebook.com/ads/library/?id=1001243686284101) | 2026-08-19 → 2026-09-24 (37d) | Active | Women 18-65, Bulgaria | 21 | 100 / 0 | 24 / 33 / 33 / 10 / 0 / 0 | dynamic/catalog (copy not visible) | (dynamic catalog text) | derolibg.com/products/smoothing-solution |
| [28280220198331415](https://www.facebook.com/ads/library/?id=28280220198331415) | 2026-08-20 → 2026-09-10 (22d) | Active | Women 18-65, Bulgaria | 6 | 100 / 0 | 17 / 50 / 33 / 0 / 0 / 0 | dynamic/catalog (copy not visible) | (dynamic catalog text) | derolibg.com/products/smoothing-solution |
| [1564411391334983](https://www.facebook.com/ads/library/?id=1564411391334983) | 2026-08-27 → 2026-08-29 (3d) | Inactive | Women 18-65, Bulgaria | 5,638 | 94 / 6 | 34 / 41 / 18 / 5 / 1 / 1 | failed/painful alternatives, mechanism/education, fast-result promise, discount/urgency | Враснали косми, тъмни петна и раздразнена кожа след депилация –  три проблема, с които всяка же | derolibg.com/products/smoothing-solution |
| [1309720747734185](https://www.facebook.com/ads/library/?id=1309720747734185) | 2026-08-27 → 2026-08-29 (3d) | Inactive | Women 18-65, Bulgaria | 1,554 | 94 / 5 | 28 / 32 / 25 / 10 / 3 / 1 | failed/painful alternatives, mechanism/education, fast-result promise, discount/urgency | Враснали косми, тъмни петна и раздразнена кожа след депилация –  три проблема, с които всяка же | derolibg.com/products/smoothing-solution |
| [1706982660796460](https://www.facebook.com/ads/library/?id=1706982660796460) | 2026-10-01 → 2026-10-06 (6d) | Active | All 18-65, Bulgaria | 1,510 | 91 / 8 | 28 / 34 / 26 / 9 / 3 / 1 | failed/painful alternatives, mechanism/education, fast-result promise | Знаеш ли защо враснали косми се появяват отново след всяка депилация?  Проблемът не е в начина, | derolibg.com/products/smoothing-solution |
| [1066995442837630](https://www.facebook.com/ads/library/?id=1066995442837630) | 2026-10-01 → 2026-10-06 (6d) | Active | All 18-65, Bulgaria | 531 | 93 / 6 | 32 / 34 / 25 / 8 / 2 / 0 | shame/hiding & confidence, failed/painful alternatives, fast-result promise, summer/beach | Уморена ли си да криеш кожата си?  От враснали косми по бикини зоната, от тъмните петна по крак | derolibg.com/products/smoothing-solution |
| [1801512997854582](https://www.facebook.com/ads/library/?id=1801512997854582) | 2026-10-01 → 2026-10-06 (6d) | Active | All 18-65, Bulgaria | 158 | 93 / 7 | 17 / 33 / 41 / 8 / 1 / 1 | shame/hiding & confidence, failed/painful alternatives, fast-result promise, summer/beach | Уморена ли си да криеш кожата си?  От враснали косми по бикини зоната, от тъмните петна по крак | derolibg.com/products/smoothing-solution |
| [1763489551754055](https://www.facebook.com/ads/library/?id=1763489551754055) | 2026-10-01 → 2026-10-05 (5d) | Inactive | All 18-65, Bulgaria | 5,424 | 89 / 11 | 34 / 41 / 19 / 5 / 1 / 0 | failed/painful alternatives, mechanism/education, fast-result promise, discount/urgency | Враснали косми, тъмни петна и раздразнена кожа след депилация –  три проблема, с които всяка же | derolibg.com/products/smoothing-solution |
| [1580431803886169](https://www.facebook.com/ads/library/?id=1580431803886169) | 2026-10-01 → 2026-10-06 (6d) | Active | All 18-65, Bulgaria | 1,693 | 90 / 9 | 20 / 33 / 31 / 13 / 3 / 1 | shame/hiding & confidence, failed/painful alternatives, fast-result promise, summer/beach | Уморена ли си да криеш кожата си?  От враснали косми по бикини зоната, от тъмните петна по крак | derolibg.com/products/smoothing-solution |
| [1521859699957366](https://www.facebook.com/ads/library/?id=1521859699957366) | 2026-10-01 → 2026-10-06 (6d) | Active | All 18-65, Bulgaria | 246 | 93 / 6 | 30 / 37 / 21 / 10 / 2 / 0 | shame/hiding & confidence, failed/painful alternatives, fast-result promise, summer/beach | Уморена ли си да криеш кожата си?  От враснали косми по бикини зоната, от тъмните петна по крак | derolibg.com/products/smoothing-solution |
| [40038101975789171](https://www.facebook.com/ads/library/?id=40038101975789171) | 2026-10-06 → 2026-10-06 (1d) | Active | All 18-65, Bulgaria | 43 | 91 / 9 | 37 / 37 / 19 / 5 / 2 / 0 | mechanism/education, social proof/reviews | Бръсненето не трябва да значи враснали косъмчета и тъмни точици 🙌  ⭐ 4,9 от над 100 ревюта.  Ед | derolibg.com/products/smoothing-solution |
| [1659117398969991](https://www.facebook.com/ads/library/?id=1659117398969991) | 2026-10-06 → 2026-10-06 (1d) | Active | All 18-65, Bulgaria | 11 | 90 / 0 | 20 / 40 / 30 / 10 / 0 / 0 | mechanism/education, social proof/reviews | Бръсненето не трябва да значи враснали косъмчета и тъмни точици 🙌  ⭐ 4,9 от над 100 ревюта.  Ед | derolibg.com/products/smoothing-solution |
| [1112142581292268](https://www.facebook.com/ads/library/?id=1112142581292268) | 2026-10-06 → 2026-10-06 (1d) | Active | All 18-65, Bulgaria | 101 | 89 / 10 | 34 / 31 / 28 / 4 / 3 / 0 | mechanism/education, social proof/reviews | Бръсненето не трябва да значи враснали косъмчета и тъмни точици 🙌  ⭐ 4,9 от над 100 ревюта.  Ед | derolibg.com/products/smoothing-solution |
| [1622602142648545](https://www.facebook.com/ads/library/?id=1622602142648545) | 2026-10-06 → 2026-10-06 (1d) | Active | All 18-65, Bulgaria | 1 | 100 / 0 | 0 / 0 / 0 / 0 / 100 / 0 | mechanism/education, social proof/reviews | Бръсненето не трябва да значи враснали косъмчета и тъмни точици 🙌  ⭐ 4,9 от над 100 ревюта.  Ед | derolibg.com/products/smoothing-solution |
| [1426778409542660](https://www.facebook.com/ads/library/?id=1426778409542660) | 2026-10-06 → 2026-10-06 (1d) | Active | All 18-65, Bulgaria | 50 | 92 / 8 | 32 / 34 / 26 / 6 / 2 / 0 | mechanism/education, social proof/reviews | Бръсненето не трябва да значи враснали косъмчета и тъмни точици 🙌  ⭐ 4,9 от над 100 ревюта.  Ед | derolibg.com/products/smoothing-solution |

**Per-ad table: LUMI** (30 relevant ads: the top 30 inactive by impressions plus all 3 active)

| Ad | Start → last (days) | Status 6 Oct | Targeting | EU reach | % W / M | Age split % | Angle tags | Primary-text hook | Landing |
|---|---|---|---|---|---|---|---|---|---|
| [1573702593602409](https://www.facebook.com/ads/library/?id=1573702593602409) | 2025-10-16 → 2025-12-15 (61d) | Inactive | All 18-65, Bulgaria | 18,348 | 91 / 8 | 46 / 38 / 11 / 3 / 1 / 1 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |
| [659567140298473](https://www.facebook.com/ads/library/?id=659567140298473) | 2025-10-16 → 2025-12-12 (58d) | Inactive | All 18-65, Bulgaria | 70,324 | 91 / 8 | 44 / 41 / 11 / 3 / 1 / 1 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |
| [1401753841308669](https://www.facebook.com/ads/library/?id=1401753841308669) | 2025-12-04 → 2025-12-23 (20d) | Inactive | All 18-65, Bulgaria | 61,182 | 90 / 9 | 48 / 40 / 9 / 3 / 1 / 0 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |
| [1234925171824996](https://www.facebook.com/ads/library/?id=1234925171824996) | 2025-12-12 → 2025-12-20 (9d) | Inactive | All 18-65, Bulgaria | 17,995 | 73 / 27 | 54 / 38 / 6 / 2 / 1 / 0 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |
| [2422785978138132](https://www.facebook.com/ads/library/?id=2422785978138132) | 2025-12-20 → 2026-01-19 (31d) | Inactive | All 18-65, Bulgaria | 119,478 | 92 / 7 | 39 / 44 / 13 / 3 / 1 / 0 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |
| [3851543598471733](https://www.facebook.com/ads/library/?id=3851543598471733) | 2025-12-31 → 2026-01-19 (20d) | Inactive | All 18-65, Bulgaria | 88,773 | 91 / 8 | 42 / 41 / 13 / 3 / 1 / 0 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |
| [1222402456128579](https://www.facebook.com/ads/library/?id=1222402456128579) | 2026-01-15 → 2026-02-03 (20d) | Inactive | All 18-65, Bulgaria | 35,741 | 90 / 8 | 45 / 39 / 11 / 3 / 1 / 0 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |
| [1138987758139088](https://www.facebook.com/ads/library/?id=1138987758139088) | 2026-01-19 → 2026-02-12 (25d) | Inactive | All 18-65, Bulgaria | 70,575 | 91 / 8 | 41 / 40 / 14 / 4 / 1 / 1 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |
| [1558964905364199](https://www.facebook.com/ads/library/?id=1558964905364199) | 2026-02-02 → 2026-04-30 (88d) | Inactive | All 18-65, Bulgaria | 130,450 | 88 / 11 | 26 / 39 / 24 / 8 / 2 / 1 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |
| [25901502902843634](https://www.facebook.com/ads/library/?id=25901502902843634) | 2026-02-12 → 2026-03-05 (22d) | Inactive | All 18-65, Bulgaria | 78,637 | 91 / 8 | 44 / 41 / 11 / 3 / 1 / 1 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |
| [3594968063986071](https://www.facebook.com/ads/library/?id=3594968063986071) | 2026-02-19 → 2026-08-07 (170d) | Inactive | All 18-65, Bulgaria | 260,032 | 91 / 8 | 32 / 40 / 19 / 6 / 1 / 1 | dynamic/catalog (copy not visible) | (dynamic catalog text) | lumibg.com/products/lumi-ingrown |
| [1299129028935876](https://www.facebook.com/ads/library/?id=1299129028935876) | 2026-02-26 → 2026-07-30 (155d) | Inactive | All 18-65, Bulgaria | 235,123 | 93 / 6 | 28 / 35 / 24 / 10 / 3 / 1 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |
| [26390557380632070](https://www.facebook.com/ads/library/?id=26390557380632070) | 2026-03-17 → 2026-04-23 (38d) | Inactive | All 18-65, Bulgaria | 98,085 | 93 / 5 | 36 / 44 / 15 / 4 / 1 / 0 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |
| [1302228438511250](https://www.facebook.com/ads/library/?id=1302228438511250) | 2026-04-13 → 2026-08-15 (125d) | Inactive | All 18-65, Bulgaria | 176,716 | 91 / 8 | 35 / 42 / 17 / 4 / 1 / 0 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |
| [1938630626853036](https://www.facebook.com/ads/library/?id=1938630626853036) | 2026-05-26 → 2026-07-25 (61d) | Inactive | All 18-65, Bulgaria | 24,282 | 93 / 6 | 35 / 36 / 19 / 7 / 2 / 1 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |
| [1521763295944998](https://www.facebook.com/ads/library/?id=1521763295944998) | 2026-07-31 → 2026-08-18 (19d) | Inactive | All 18-65, Bulgaria | 68,183 | 91 / 8 | 23 / 35 / 28 / 11 / 2 / 1 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |
| [2444799539362203](https://www.facebook.com/ads/library/?id=2444799539362203) | 2026-08-18 → 2026-09-05 (19d) | Inactive | All 18-65, Bulgaria | 59,403 | 90 / 8 | 35 / 36 / 19 / 7 / 2 / 1 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |
| [1549834522782616](https://www.facebook.com/ads/library/?id=1549834522782616) | 2026-08-18 → 2026-08-28 (11d) | Inactive | All 18-65, Bulgaria | 18,903 | 93 / 6 | 25 / 33 / 26 / 12 / 3 / 1 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |
| [1368626028179434](https://www.facebook.com/ads/library/?id=1368626028179434) | 2026-08-22 → 2026-09-02 (12d) | Inactive | All 18-65, Bulgaria | 19,215 | 94 / 5 | 30 / 35 / 24 / 9 / 2 / 1 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | http://lumibg.com/ingrown |
| [1385500577039371](https://www.facebook.com/ads/library/?id=1385500577039371) | 2026-09-01 → 2026-09-05 (5d) | Inactive | All 18-65, Bulgaria | 19,366 | 94 / 5 | 32 / 38 / 20 / 7 / 2 / 1 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | http://lumibg.com/ingrown |
| [1479418464236701](https://www.facebook.com/ads/library/?id=1479418464236701) | 2026-09-04 → 2026-09-09 (6d) | Inactive | All 18-65, Bulgaria | 20,498 | 91 / 8 | 26 / 39 / 24 / 8 / 2 / 1 | dynamic/catalog (copy not visible) | (dynamic catalog text) | lumibg.com/products/lumi-ingrown |
| [1643790970681780](https://www.facebook.com/ads/library/?id=1643790970681780) | 2026-09-11 → 2026-09-16 (6d) | Inactive | All 18-65, Bulgaria | 15,695 | 94 / 5 | 45 / 36 / 13 / 4 / 1 / 0 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |
| [2072894626666208](https://www.facebook.com/ads/library/?id=2072894626666208) | 2026-09-14 → 2026-09-27 (14d) | Inactive | All 18-65, Bulgaria | 28,693 | 91 / 7 | 40 / 39 / 16 / 4 / 1 / 0 | failed/painful alternatives, mechanism/education | Ако и при теб след бръснене или кола маска бикини зоната остава с врастнали косъмчета, червени  | lumibg.com/products/lumi-ingrown |
| [902064742755456](https://www.facebook.com/ads/library/?id=902064742755456) | 2026-09-15 → 2026-09-20 (6d) | Inactive | All 18-65, Bulgaria | 23,283 | 85 / 13 | 46 / 39 / 11 / 3 / 1 / 0 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |
| [1724786861969102](https://www.facebook.com/ads/library/?id=1724786861969102) | 2026-09-15 → 2026-09-27 (13d) | Inactive | All 18-65, Bulgaria | 21,654 | 94 / 6 | 41 / 39 / 15 / 4 / 1 / 0 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |
| [1083151101351962](https://www.facebook.com/ads/library/?id=1083151101351962) | 2026-09-19 → 2026-09-27 (9d) | Inactive | All 18-65, Bulgaria | 20,640 | 93 / 5 | 35 / 42 / 16 / 5 / 1 / 0 | dynamic/catalog (copy not visible) | (dynamic catalog text) | lumibg.com/products/lumi-ingrown |
| [1691160699300876](https://www.facebook.com/ads/library/?id=1691160699300876) | 2026-09-22 → 2026-09-28 (7d) | Inactive | All 18-65, Bulgaria | 55,495 | 93 / 5 | 43 / 44 / 10 / 2 / 0 / 0 | other | След почти всяко бръснене кожата ми оставаше с червени точки, врастнали косъмчета и раздразнени | lumibg.com/products/lumi-ingrown |
| [1072774725622074](https://www.facebook.com/ads/library/?id=1072774725622074) | 2026-09-28 → 2026-10-06 (9d) | Active | All 18-65, Bulgaria | 22,477 | 90 / 9 | 38 / 41 / 15 / 4 / 1 / 0 | dynamic/catalog (copy not visible) | (dynamic catalog text) | lumibg.com/products/lumi-ingrown |
| [1090434123354805](https://www.facebook.com/ads/library/?id=1090434123354805) | 2026-09-29 → 2026-10-06 (8d) | Active | All 18-65, Bulgaria | 9,668 | 89 / 10 | 28 / 39 / 24 / 7 / 1 / 1 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |
| [1081091171475488](https://www.facebook.com/ads/library/?id=1081091171475488) | 2026-09-29 → 2026-10-06 (8d) | Active | All 18-65, Bulgaria | 11,207 | 95 / 4 | 53 / 35 / 9 / 2 / 0 / 0 | fast-result promise, discount/urgency | Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7  | lumibg.com/products/lumi-ingrown |

**Per-ad table: SimplyBeauty (PFB Vanish)**

| Ad | Start → last (days) | Status 6 Oct | Targeting | EU reach | % W / M | Age split % | Angle tags | Primary-text hook | Landing |
|---|---|---|---|---|---|---|---|---|---|
| [2316889675723385](https://www.facebook.com/ads/library/?id=2316889675723385) | 2026-09-30 → 2026-10-06 (7d) | Active | Women 35-65, Bulgaria | 1,169 | 100 / 0 | 0 / 0 / 48 / 38 / 10 / 4 | mechanism/education | 🔍Враснали косми след бръснене или епилация? Понякога проблемът не е в начина, по който премахва | simplybeauty.bg/article/vrasnali-kosmi-zashto |

- Offers and hooks seen in these ads (primary text visible in the Ad Library):
  - **LUMI:** "Единственият продукт, който премахва врастнали косми, изсветлява петна и успокоява кожата за 7 дни!… Намалението приключва след 4 часа!", with the card "✨ LUMI Серум Против Врастнали Косми (4.8/5) - 7356 Доволни Клиенти", landing lumibg.com/products/lumi-ingrown — [ad 1299129028935876](https://www.facebook.com/ads/library/?id=1299129028935876).
  - **Deroli:** "Враснали косми, тъмни петна и раздразнена кожа след депилация – три проблема, с които всяка жена се е борила…", landing derolibg.com/products/smoothing-solution — [ad 1029734312805937](https://www.facebook.com/ads/library/?id=1029734312805937). New on 6 Oct 2026: "Бръсненето не трябва да значи враснали косъмчета и тъмни точици 🙌 ⭐ 4,9 от над 100 ревюта. Един рол-он, три задачи" — [ad 40038101975789171](https://www.facebook.com/ads/library/?id=40038101975789171).
  - Prices and offers on the landing pages are covered in the background note (Deroli €19.90, LUMI €20.90).

### Inferences
- **Core ICP evidence:** For an at-home ingrown-hair product sold in BG, Meta finds its audience among **women aged 18–34**. Women 25–34 are the single largest cell at 35.6% of reach, with women 18–24 at 32.6% and women 35–44 at 16.3%. Women 45+ make up only ~7%. Two separate advertisers with different settings (LUMI open-gender, Deroli women-only) converged on almost the same split. That suggests the pattern reflects the product and audience rather than one advertiser's setup. This is a reach proxy, not purchase data (see Gaps).
- **Men are a small, real tail.** With gender left open (46 ads, 1.92M reach), 7.8% of reach went to men, mostly aged 18–34 (5.2 of the 7.5 points in the grid). Women-only targeting still delivered 6.5% to men. That suggests Advantage+ audience expansion treats the gender setting as a suggestion (an inference, since Meta does not expose the setting).
- **Long-running ads did not deliver to an older audience.** Ads that ran ≥30 days had 34/39/19% for 18-24/25-34/35-44, nearly identical to short tests (37/39/17%). The 18–34 skew therefore holds for the ads the advertisers kept funding, not just early tests.
- Deroli's later Women-only ads (Aug 2026) drifted slightly older (22–35% aged 18–24, 34–40% aged 25–34, 22–28% aged 35–44) than LUMI. For a pad brand, **25–34 is the safest core age, with 18–24 and 35–44 as testable flanks.**
- No direct pad competitor is advertising in BG. Savenae has no Meta ads, and the only pad-format ad found was MoiataKozmetika's exfoliating mitt-pads (section 2).

### Gaps
- **Reach is not purchases.** Meta delivers toward each campaign's optimization goal, which the Ad Library does not show (purchase, add-to-cart, traffic, etc.). Delivery is also shaped by auction prices, so cheaper inventory can be over-delivered. Using reach as a proxy for "who converts" assumes these DTC Shopify sellers run sales/conversion objectives. That is likely but not verified.
- LUMI coverage is ~33 of ~85 page ads (rate limits capped retrieval at 30 per view). Spend and impressions per ad are not published for commercial ads.
- "{{product.brand}}" / dynamic-creative ads (18 Deroli and 4 LUMI) do not show their primary text in the Ad Library, so their angle is unknown.
- Video and image content was not reviewed, so imagery cues are not coded. Pronoun analysis is limited to primary text. Deroli writes in the feminine ("Уморена ли си…", "всяка жена"). LUMI's main copy is gender-neutral second person.

## 2. Adjacent at-home advertisers (Sèlestre, Merréh, BeNatural, Bielle, Cyra, Follixa, others): targeting and reach by age/gender

### Takeaway
Adjacent at-home products also deliver 82–100% to women, but their **age centre depends on the problem framed**:
- **Shaving and ingrown framings sit young.** Veloura: 38% aged 18–24. Glowie IPL: 26% aged 18–24. Waxx: 26% aged 18–24.
- **Hair-removal crystal (Sèlestre) sits at 35–54.** 62% of its reach is in that band.
- **"Dry, rough skin" towel copy (Bielle) sits at 45+.** About two-thirds of its reach is 45+, even with open targeting.

So the ingrown-hair or razor-bump framing is what pulls delivery to women under 35.

### Cited Findings
| Cat | Advertiser | Ads (active 6 Oct) | First → last start date | Targeting settings | Locations | Summed EU reach | % W / M | Age split % | Highest-reach ad |
|---|---|---|---|---|---|---|---|---|---|
| B | BeNatural | 8 (5 active) | 2025-07-01 → 2026-06-23 | Women 18-65 ×6; Women 18-55 ×2 | Bulgaria ×8 | 1,958,249 | 92 / 7 | 17 / 32 / 27 / 14 / 7 / 3 | [684769117843102](https://www.facebook.com/ads/library/?id=684769117843102) (503,050) |
| B | Bielle | 21 (8 active) | 2026-08-02 → 2026-09-30 | All 18-65 ×21 | Bulgaria ×21 | 649,077 | 82 / 17 | 4 / 11 / 17 / 21 / 24 / 22 | [1419285633390744](https://www.facebook.com/ads/library/?id=1419285633390744) (213,754) |
| B | Merréh | 26 (21 active) | 2025-10-30 → 2026-10-05 | Women 18-65 ×19; Women 18-50 ×4; Women 18-55 ×3 | Bulgaria ×26 | 121,797 | 99 / 1 | 4 / 20 / 36 / 27 / 9 / 5 | [1343080167333268](https://www.facebook.com/ads/library/?id=1343080167333268) (17,472) |
| B | MoiataKozmetika (Olcom LTD) | 1 (0 active) | ? → ? | All 18-65 ×1 | Bulgaria ×1 | 2,620 | 94 / 6 | 15 / 41 / 30 / 10 / 2 / 1 | [1039165575270037](https://www.facebook.com/ads/library/?id=1039165575270037) (2,620) |
| C | Glowie.bg | 25 (0 active) | 2025-07-16 → 2026-07-03 | All 18-65 ×25 | Bulgaria ×25 | 4,483,136 | 82 / 16 | 26 / 32 / 22 / 13 / 5 / 2 | [1164646012305982](https://www.facebook.com/ads/library/?id=1164646012305982) (390,262) |
| C | Sèlestre - България | 33 (10 active) | 2025-04-16 → 2026-09-30 | All 18-65 ×28; Women 24-65 ×3; Women 18-65 ×1; Women 18-60 ×1 | Bulgaria ×33 | 2,013,797 | 90 / 9 | 5 / 20 / 37 / 25 / 10 / 3 | [27246555998338974](https://www.facebook.com/ads/library/?id=27246555998338974) (319,076) |
| C | Waxx.me - България | 6 (0 active) | 2024-01-17 → 2026-07-22 | All 18-65 ×6 | Bulgaria ×6 | 1,725,203 | 85 / 14 | 26 / 36 / 25 / 10 / 3 / 1 | [432581536163107](https://www.facebook.com/ads/library/?id=432581536163107) (846,825) |
| C | CyraBulgaria | 22 (21 active) | 2026-04-03 → 2026-10-02 | Women 18-65 ×22 | Bulgaria ×22 | 1,697,687 | 88 / 11 | 20 / 27 / 23 / 17 / 10 / 4 | [1307674641441942](https://www.facebook.com/ads/library/?id=1307674641441942) (424,850) |
| C | Gillette Venus Bulgaria | 2 (0 active) | 2026-08-05 → 2026-08-05 | Women 18-44 ×2 | Bulgaria ×2 | 674,042 | 100 / 0 | 23 / 38 / 39 / 0 / 0 / 0 | [1626182422416767](https://www.facebook.com/ads/library/?id=1626182422416767) (556,775) |
| C | Colorlamb Bulgaria | 2 (0 active) | 2024-05-20 → 2025-08-27 | Women 18-65 ×2 | Bulgaria ×2 | 611,434 | 88 / 11 | 17 / 34 / 30 / 14 / 4 / 1 | [1541605599721933](https://www.facebook.com/ads/library/?id=1541605599721933) (588,138) |
| C | Philips | 5 (0 active) | 2026-02-06 → 2026-08-05 | Women 18-45 ×3; Women 18-50 ×1; All 18-45 ×1 | Bulgaria ×5 | 439,622 | 81 / 19 | 25 / 38 / 28 / 9 / 0 / 0 | [1946325536023921](https://www.facebook.com/ads/library/?id=1946325536023921) (130,306) |
| C | Shopche.bg | 1 (0 active) | 2025-05-02 → 2025-05-02 | Women 18-65 ×1 | Bulgaria ×1 | 250,897 | 80 / 19 | 9 / 14 / 19 / 24 / 20 / 14 | [546694398236974](https://www.facebook.com/ads/library/?id=546694398236974) (250,897) |
| C | Braun | 2 (2 active) | 2026-10-01 → 2026-10-01 | Women 18-44 ×2 | Bulgaria ×2 | 187,208 | 100 / 0 | 18 / 33 / 49 / 0 / 0 / 0 | [1084321514322229](https://www.facebook.com/ads/library/?id=1084321514322229) (157,742) |
| C | Follixa BG | 1 (1 active) | 2026-09-19 → 2026-09-19 | Women 24-65 ×1 | Bulgaria ×1 | 38,964 | 85 / 14 | 2 / 22 / 28 / 24 / 17 / 7 | [1409209508022974](https://www.facebook.com/ads/library/?id=1409209508022974) (38,964) |
| C | Veloura | 1 (0 active) | 2026-08-06 → 2026-08-06 | All 18-65 ×1 | Bulgaria ×1 | 30,538 | 89 / 11 | 38 / 38 / 17 / 5 / 2 / 1 | [37351294337850142](https://www.facebook.com/ads/library/?id=37351294337850142) (30,538) |
| C | Alenika.bg | 3 (2 active) | 2026-10-01 → 2026-10-01 | Women 18-65 ×3 | Bulgaria ×3 | 3,472 | 90 / 9 | 24 / 36 / 25 / 10 / 3 / 2 | [2150186462197945](https://www.facebook.com/ads/library/?id=2150186462197945) (2,433) |
| C | Arvela | 1 (1 active) | 2026-09-26 → 2026-09-26 | All 18-65 ×1 | Bulgaria ×1 | 70 | 90 / 10 | 33 / 31 / 29 / 6 / 1 / 0 | [1099551699702920](https://www.facebook.com/ads/library/?id=1099551699702920) (70) |

Category-level summary:

| Category | Ads with EU data | Summed EU reach | % women / men / unknown | Age split % | Subset with open targeting |
|---|---|---|---|---|---|
| B. Exfoliation / body care | 56 | 2,731,743 | 90.1 / 9.4 / 0.5 | 13 / 27 / 25 / 17 / 11 / 8 | 22 ads: 81.9 / 17.3; 4 / 12 / 17 / 21 / 24 / 22 |
| C. Hair-removal & hair-growth products | 104 | 12,156,070 | 86.4 / 12.7 / 0.9 | 20 / 30 / 27 / 14 / 6 / 2 | 61 ads: 84.4 / 14.5; 22 / 30 / 25 / 15 / 6 / 2 |

Representative ads (highest reach per advertiser):
- **Sèlestre** crystal: testimonial hook "Кристала е супер! Бях скептична… Изпробвах го първо на мъжа ми…". Open targeting (All 18–65), running 18 Jun–6 Oct 2026, 319,076 reach, 93% W, age 4/13/30/32/17/4 — [ad 27246555998338974](https://www.facebook.com/ads/library/?id=27246555998338974). The summer hook "Точно преди морето осъзнаваш, че си забравила да махнеш косъмчетата…" got 185,029 reach, 88% W, age 4/17/37/29/11/2 — [ad 4461164357429422](https://www.facebook.com/ads/library/?id=4461164357429422).
- **Bielle** Japanese exfoliating towel: "Кожата ти е суха, груба и лющеща се… мъртвите клетки блокират пътя му…". All 21 ads use open targeting. The top ad got 213,754 reach, 79% W / 20% M, age 7/20/24/20/16/13 — [ad 1419285633390744](https://www.facebook.com/ads/library/?id=1419285633390744). The active ad got 52,420 reach, 87% W, age 1/4/10/21/31/32 — [ad 1123240766692474](https://www.facebook.com/ads/library/?id=1123240766692474).
- **Merréh** body scrubs (26 scrub-related ads out of 58 captured; the page shows ~28 active and ~1,100 inactive ads — [Merréh active](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BG&view_all_page_id=175015329021941&search_type=page&media_type=all)):
  - Targeting is Women 18–65/18–55/18–50, with 99% W delivery and age 4/20/36/27/9/5.
  - The scrub-with-ingrown copy "Целулит, сухота, врастнали косми? Един продукт се грижи за всичко" reached only 7,824 people — [ad 1457134469653060](https://www.facebook.com/ads/library/?id=1457134469653060).
- **BeNatural** Matcha detox bran (8 relevant ads; the page shows ~210 ads — [BeNatural page](https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=BG&view_all_page_id=102889571888094&search_type=page&media_type=all)):
  - "Обърнати косъмчета, широки пори, черни точки - кажи СТОП…": Women 18–65, running 1 Dec 2025–6 Oct 2026, 503,050 reach, 94% W, age 4/19/32/25/14/6 — [ad 684769117843102](https://www.facebook.com/ads/library/?id=684769117843102).
  - The "Коледна оферта!" variant of the same copy skewed younger: 299,871 reach, 83% W, age 26/42/20/7/3/1 — [ad 1405471964308436](https://www.facebook.com/ads/library/?id=1405471964308436).
  - The "Пъпки, зачервяване и обърнати косъмчета след епилация?" ad: Women 18–65, 67,843 reach — [ad 1325889239051463](https://www.facebook.com/ads/library/?id=1325889239051463).
- **CyraBulgaria** hair-growth serum: all 22 ads target Women 18–65 (88% W, age 20/27/23/17/10/4). The top ad is face-hair-led ("Спри да влошаваш окосмяването на лицето…"), with 424,850 reach and age 16/23/21/21/13/5 — [ad 1307674641441942](https://www.facebook.com/ads/library/?id=1307674641441942).
- **Follixa BG** cyperus oil (only 1 ad with EU data; a "follixa" keyword search returned "No ads match"): testimonial hook "Бръснех се през ден…", **Women 24–65**, 38,964 reach, 85% W, age 2/22/28/24/17/7 — [ad 1409209508022974](https://www.facebook.com/ads/library/?id=1409209508022974).
- **Veloura** hair-growth serum with ingrown-hair care: "Всеки път след бръснене едно и също? Зачервяване. Малки пъпчици. Болезнени врастнали косъмчета." Open targeting, 30,538 reach, 89% W, age **38/38/17/5/2/1** — [ad 37351294337850142](https://www.facebook.com/ads/library/?id=37351294337850142).
- **Glowie.bg** IPL: "#1 Решение за премахване на косми… Живей без: -Враснали косъмчета…". 25 open-targeting ads (Jul 2025–Jul 2026), 4.48M summed reach, 82% W, age 26/32/22/13/5/2. The top ad got 390,262 reach — [ad 1164646012305982](https://www.facebook.com/ads/library/?id=1164646012305982).
- **Waxx.me** at-home wax: open targeting, 846,825 reach, 84% W, age 22/34/27/12/4/1 — [ad 432581536163107](https://www.facebook.com/ads/library/?id=432581536163107).
- **Philips OneBlade Intimate** (a men's intimate trimmer, influencer video): All 18–45, **35% W / 64% M**, age 38/44/17/1 — [ad 1946325536023921](https://www.facebook.com/ads/library/?id=1946325536023921). This is the only male-majority ad in the hair-removal set.
- **Alenika.bg** Fler razor ("…подкожните косъмчета след епилация!"): Women 18–65, 2,433 reach, age 24/37/25/10/3/1 — [ad 2150186462197945](https://www.facebook.com/ads/library/?id=2150186462197945).
- **MoiataKozmetika** (Olcom LTD) MadForCos body peeling pads, the only pad-format ad: open targeting, 2,620 reach, 94% W, age 15/41/30/10/2/1 — [ad 1039165575270037](https://www.facebook.com/ads/library/?id=1039165575270037).

### Inferences
- The age centre tracks the **problem named in the hook**:
  - shaving bumps, ingrown hairs, "after every shave" → 18–34 (LUMI, Veloura, Glowie, Waxx, BeNatural's promo variant)
  - convenience hair removal, "before the beach" → 35–54 (Sèlestre)
  - dry, rough or flaky skin → 45+ (Bielle)

  For pads, a hook built on ingrown hairs and razor bumps should pull delivery young. A "smooth, soft skin / exfoliation" hook risks drifting toward 45+.
- Open-gender targeting in these categories sends 15–20% of reach to men (C: 15.2%, B: 17.3%), against ~8% for ingrown serums. The ingrown-hair message is more female-specific than generic body-care messages.
- The Philips OneBlade Intimate result suggests a separate men's 18–34 intimate-grooming segment exists. No BG ingrown-hair brand addresses it yet.

### Gaps
- Merréh, BeNatural, Glowie and Vitalaiz have far more ads than the first 30 retrieved per view, so their figures are samples.
- NONA's, Glowie's and the second Cyra page's view pages returned "No ads match" or empty on retry even though ads with EU data exist. These page views are unreliable under rate limiting, so advertiser totals may be incomplete.

## 3. Intimate-care advertisers (NONA Elixir and others): who they reach

### Takeaway
Intimate-odour and intimate-hygiene products reach a **distinctly older** female audience. **NONA Elixir peaks at 45–54 (33%) and 55–64 (24%)**, and only 6% of its reach is under 35. The pharmacist-voiced So Healthy discharge/odour product is the exception at 25–44.

### Cited Findings
| Cat | Advertiser | Ads (active 6 Oct) | First → last start date | Targeting settings | Locations | Summed EU reach | % W / M | Age split % | Highest-reach ad |
|---|---|---|---|---|---|---|---|---|---|
| D | NONA-Свежест на всяка възраст | 35 (9 active) | 2025-10-13 → 2026-09-21 | Women 18-65 ×30; All 18-65 ×5 | Bulgaria ×35 | 2,955,145 | 90 / 9 | 1 / 5 / 20 / 33 / 24 / 16 | [1558371019211836](https://www.facebook.com/ads/library/?id=1558371019211836) (271,649) |
| D | So Healthy | 14 (14 active) | 2026-07-17 → 2026-09-24 | All 18-65 ×8; Women 18-65 ×6 | Bulgaria ×14 | 990,144 | 97 / 3 | 19 / 30 / 30 / 16 / 4 / 1 | [1021611070799995](https://www.facebook.com/ads/library/?id=1021611070799995) (415,580) |
| D | Carnium Botanicals Bulgaria | 7 (0 active) | 2025-10-09 → 2026-08-05 | Women 18-65 ×7 | Bulgaria ×7 | 594,421 | 98 / 2 | 14 / 27 / 27 / 21 / 8 / 3 | [1288515696071047](https://www.facebook.com/ads/library/?id=1288515696071047) (138,686) |
| D | Натурпродукт България | 5 (0 active) | 2026-08-03 → 2026-09-14 | Women 24-64 ×3; Women 18-65 ×1; All 20-60 ×1 | Bulgaria ×5 | 500,460 | 98 / 2 | 1 / 9 / 13 / 26 / 40 / 11 | [1735020534418205](https://www.facebook.com/ads/library/?id=1735020534418205) (143,123) |
| D | Leyra  | 2 (2 active) | 2026-08-11 → 2026-08-11 | Women 18-65 ×2 | Bulgaria ×2 | 137,394 | 100 / 0 | 28 / 35 / 23 / 10 / 2 / 1 | [1066517199226937](https://www.facebook.com/ads/library/?id=1066517199226937) (136,815) |
| D | InaEssentials - Семеен Онлайн Органичен Магазин за Био Козметика | 2 (2 active) | 2026-10-02 → 2026-10-02 | All 18-65 ×2 | Bulgaria ×2 | 1,574 | 96 / 3 | 5 / 31 / 39 / 20 / 4 / 1 | [1362083595729522](https://www.facebook.com/ads/library/?id=1362083595729522) (1,129) |
| D | Kinnzy | 1 (1 active) | 2026-09-08 → 2026-09-08 | Women 18-65 ×1 | Blagoevgrad, Bulgaria; Burgas, Bulgaria; Gabrovo, Bulgaria; Plovdiv, Bulgaria; Ruse, Bulgaria; Schumen, Shumen, Bulgaria; Sofia, Bulgaria; Stara Zagora, Bulgaria; Veliko Tarnovo, Bulgaria; Varna, Bulgaria ×1 | 1,266 | 93 / 6 | 7 / 33 / 40 / 16 / 3 / 1 | [1057293263840084](https://www.facebook.com/ads/library/?id=1057293263840084) (1,266) |

- **NONA Elixir:**
  - The "МИРИЗМА / дъщеря ми ми каза: „Мамо… миришеш различно." А аз бях на 47" story ad: Women 18–65, 215,717 reach, 95% W, age 1/7/28/37/20/7 — [ad 1477373863500233](https://www.facebook.com/ads/library/?id=1477373863500233).
  - The "българска формула, създадена по японска технология" ad: 271,649 reach, age 0/3/15/34/29/19 — [ad 1558371019211836](https://www.facebook.com/ads/library/?id=1558371019211836).
  - The ad cited in the background note: 575 reach, payer "Georgi valchkov" — [ad 1067157216308795](https://www.facebook.com/ads/library/?id=1067157216308795).
- **So Healthy** "Бяло течение или неприятна интимна миризма… Като фармацевт…": Women 18–65, 415,580 reach, 100% W, age 15/29/32/18/5/1 — [ad 1021611070799995](https://www.facebook.com/ads/library/?id=1021611070799995). An open-gender variant delivered 79% W / 20% M — [ad 1144171514846167](https://www.facebook.com/ads/library/?id=1144171514846167).

### Inferences
- The "intimate zone" framing on its own does not imply young buyers. NONA's odour and menopause-adjacent story pulls 45+ delivery. Ingrown-hair pads should be framed around **shaving and hair removal of the bikini line** (an 18–34 behaviour) rather than intimate hygiene, or delivery may drift older.

### Gaps
- NONA's page view returned "No ads match" twice under rate limiting. The 35 NONA ads were found through keyword searches ("NONA Elixir", "интимна зона"), so NONA coverage is partial.

## 4. Laser clinics advertising bikini or intimate laser (premium-alternative segment): targeting and reach

### Takeaway
Clinic ads that mention **bikini or "интим"** are **always targeted at Women only**, usually aged **18–55**, city by city. They deliver 99% to women with **25–44 = 64%** of reach (15/33/31/19/2/1). That is about a decade older than the DTC ingrown-serum buyer.

Clinic ads that do not mention bikini or intim, or that use open gender, reach many men and older people: open-gender clinic ads went 60% male. G Point dominates bikini laser on Meta (34 ads, 2.85M summed reach, "Пълен интим - 24 €").

### Cited Findings
| Subset | Ads | Summed reach | % W / M | Age split % | Gender settings | Age settings (top 5) |
|---|---|---|---|---|---|---|
| clinic ads mentioning bikini/intim | 36 | 2,658,509 | 99.2 / 0.8 | 15 / 33 / 31 / 19 / 2 / 1 | targets: {'Women': 36} | ages: {'18-55': 28, '20-45': 2, '20-40': 1, '24-65': 1, '25-65': 1} |
| other clinic ads | 54 | 2,470,207 | 58.2 / 41.4 | 10 / 24 / 23 / 19 / 13 / 12 | targets: {'Women': 33, 'All': 18, 'Men': 3} | ages: {'18-65': 22, '25-65': 9, '18-55': 5, '18-54': 3, '22-65': 3} |

Top bikini/intim clinic ads by reach:

| Clinic | Ad | Start → last | Targeting | Location | EU reach | % W / M | Age split % | Hook |
|---|---|---|---|---|---|---|---|---|
| G Point | [877066782128445](https://www.facebook.com/ads/library/?id=877066782128445) | 2026-07-10→2026-10-06 | Women 18-55 | Sofia, Bulgaria | 543,098 | 100/0 | 12 / 29 / 32 / 24 / 2 / 0 | Лесно е като 1 + 2 = 3😉 По-малко косми и бръснене + трайно гладка кожа = Повече време за себе си. Красотата и  |
| G Point | [2144026433122255](https://www.facebook.com/ads/library/?id=2144026433122255) | 2026-07-30→2026-10-06 | Women 18-55 | Plovdiv, Bulgaria | 458,983 | 100/0 | 15 / 32 / 31 / 21 / 1 / 0 | Пловдив, време е за истински резултати! Всяка регистрация = БЕЗПЛАТНА зона!🎁 Мишници или интим? Ти избираш! Ел |
| G Point | [1023345210341323](https://www.facebook.com/ads/library/?id=1023345210341323) | 2026-07-30→2026-10-06 | Women 18-55 | Varna, Bulgaria | 348,432 | 100/0 | 14 / 31 / 33 / 22 / 1 / 0 | Лесно е като 1 + 2 = 3😉 По-малко косми и бръснене + трайно гладка кожа = Повече време за себе си. Красотата и  |
| G Point | [2190068601822876](https://www.facebook.com/ads/library/?id=2190068601822876) | 2026-06-02→2026-06-13 | Women 20-45 | Bulgaria | 194,900 | 100/0 | 14 / 43 / 40 / 3 / 0 / 0 | Пише се лазерна епилация - чете се СВО-БО-ДА.🆓 Без бръснене всеки ден. Без врастнали косми. 💬 Без "чакай само  |
| G Point | [2867030886965280](https://www.facebook.com/ads/library/?id=2867030886965280) | 2026-07-30→2026-10-06 | Women 18-55 | Ruse, Bulgaria | 154,697 | 100/0 | 16 / 34 / 29 / 20 / 1 / 0 | Русе, време е за истински резултати! Всяка регистрация = БЕЗПЛАТНА зона!🎁 Мишници или интим? Ти избираш! Ела н |
| G Point | [1628354338655214](https://www.facebook.com/ads/library/?id=1628354338655214) | 2026-09-23→2026-10-06 | Women 18-55 | Burgas, Bulgaria | 137,113 | 100/0 | 28 / 33 / 23 / 15 / 1 / 0 | Лесно е като 1 + 2 = 3😉 По-малко косми и бръснене + трайно гладка кожа = Повече време за себе си. Красотата и  |
| G Point | [1613755617023255](https://www.facebook.com/ads/library/?id=1613755617023255) | 2026-09-16→2026-10-06 | Women 18-55 | Veliko Tarnovo, Bulgaria | 78,710 | 100/0 | 14 / 35 / 30 / 20 / 1 / 0 | Лесно е като 1 + 2 = 3😉 По-малко косми и бръснене + трайно гладка кожа = Повече време за себе си. Красотата и  |
| G Point | [867250366238707](https://www.facebook.com/ads/library/?id=867250366238707) | 2026-07-30→2026-10-06 | Women 18-55 | Ruse, Bulgaria | 74,024 | 100/0 | 15 / 33 / 30 / 21 / 1 / 0 | Лесно е като 1 + 2 = 3😉 По-малко косми и бръснене + трайно гладка кожа = Повече време за себе си. Красотата и  |
| G Point | [1482128346242731](https://www.facebook.com/ads/library/?id=1482128346242731) | 2026-05-27→2026-06-01 | Women 20-45 | Bulgaria | 59,739 | 100/0 | 20 / 50 / 29 / 2 / 0 / 0 | Пише се лазерна епилация - чете се СВО-БО-ДА.🆓 Без бръснене всеки ден. Без врастнали косми. 💬 Без "чакай само  |
| G Point | [1356596503212144](https://www.facebook.com/ads/library/?id=1356596503212144) | 2026-09-23→2026-10-06 | Women 18-55 | Blagoevgrad, Bulgaria | 56,148 | 100/0 | 26 / 34 / 24 / 15 / 1 / 0 | Лесно е като 1 + 2 = 3😉 По-малко косми и бръснене + трайно гладка кожа = Повече време за себе си. Красотата и  |
| Нирвана Естетичен център | [1544847256572315](https://www.facebook.com/ads/library/?id=1544847256572315) | 2026-02-02→2026-02-16 | Women 25-65 | Sofia Province, Bulgaria; Sofia, Bu | 55,881 | 64/35 | 0 / 32 / 35 / 21 / 8 / 5 | 💖 Гладка кожа за перфектния Свети Валентин в Нирвана! 💖  Подгответе се за романтичния ден с александритна епил |
| G Point | [1618654506329389](https://www.facebook.com/ads/library/?id=1618654506329389) | 2026-09-16→2026-10-06 | Women 18-55 | Shumen, Bulgaria | 42,758 | 100/0 | 14 / 31 / 31 / 23 / 1 / 0 | Шумен, време е за истински резултати! Всяка регистрация = БЕЗПЛАТНА зона!🎁 Мишници или интим? Ти избираш! Ела  |
| G Point | [1886767128684041](https://www.facebook.com/ads/library/?id=1886767128684041) | 2026-05-29→2026-10-06 | Women 18-55 | Kardzhali, Kŭrdzhali, Bulgaria | 36,864 | 100/0 | 14 / 33 / 27 / 24 / 2 / 0 | Кърджали, време е за истински резултати! Всяка регистрация = БЕЗПЛАТНА зона!🎁 Мишници или интим? Ти избираш! Е |
| G Point | [3228323574165649](https://www.facebook.com/ads/library/?id=3228323574165649) | 2026-09-16→2026-10-06 | Women 18-55 | Pleven, Bulgaria | 30,222 | 100/0 | 13 / 30 / 32 / 24 / 2 / 0 | Плевен, време е за истински резултати! Всяка регистрация = БЕЗПЛАТНА зона!🎁 Мишници или интим? Ти избираш! Ела |
| G Point | [2200865590489664](https://www.facebook.com/ads/library/?id=2200865590489664) | 2026-09-17→2026-10-06 | Women 18-55 | Pazardjik, Bulgaria | 28,821 | 100/0 | 15 / 32 / 30 / 21 / 1 / 0 | Пазарджик, време е за истински резултати! Всяка регистрация = БЕЗПЛАТНА зона!🎁 Мишници или интим? Ти избираш!  |

Per-clinic summary (hair-removal ads only):

| Cat | Advertiser | Ads (active 6 Oct) | First → last start date | Targeting settings | Locations | Summed EU reach | % W / M | Age split % | Highest-reach ad |
|---|---|---|---|---|---|---|---|---|---|
| E | G Point | 34 (32 active) | 2026-05-27 → 2026-09-23 | Women 18-55 ×32; Women 20-45 ×2 | Bulgaria ×2; Varna, Bulgaria ×2; Sofia, Bulgaria ×2 | 2,851,147 | 100 / 0 | 15 / 32 / 31 / 20 / 1 / 0 | [877066782128445](https://www.facebook.com/ads/library/?id=877066782128445) (543,098) |
| E | Abi Beauty | 8 (6 active) | 2026-01-13 → 2026-09-26 | Women 18-54 ×3; Women 18-65 ×2; Men 18-54 ×1; All 25-54 ×1; Women 25-54 ×1 | Sofia, Bulgaria ×8 | 347,059 | 48 / 52 | 6 / 12 / 13 / 16 / 24 / 30 | [1167757538465190](https://www.facebook.com/ads/library/?id=1167757538465190) (191,788) |
| E | VM Aesthetics - Sofia | 2 (0 active) | 2025-11-29 → 2026-07-06 | All 18-45 ×1; Women 18-65 ×1 | Sofia, Bulgaria ×2 | 338,748 | 35 / 64 | 10 / 27 / 34 / 13 / 10 / 6 | [28617279941196091](https://www.facebook.com/ads/library/?id=28617279941196091) (173,778) |
| E | Dr Kamberova Aesthetic | 3 (1 active) | 2026-02-13 → 2026-09-13 | All 22-65 ×2; Women 22-65 ×1 | Smolyan Province, Bulgaria ×3 | 251,032 | 37 / 62 | 9 / 26 / 20 / 19 / 16 / 11 | [1112073164832176](https://www.facebook.com/ads/library/?id=1112073164832176) (117,481) |
| E | Vitalaiz Естетичен център | 17 (17 active) | 2025-10-16 → 2026-09-30 | All 25-65 ×9; Women 18-65 ×8 | Burgas, Bulgaria ×17 | 188,933 | 87 / 12 | 8 / 15 / 25 / 24 / 16 / 12 | [1033958752403458](https://www.facebook.com/ads/library/?id=1033958752403458) (69,189) |
| E | GRAND Лазерен Център by Mariana Aleksieva | 2 (0 active) | 2025-10-13 → 2026-06-04 | Women 18-65 ×2 | Burgas, Bulgaria ×2 | 165,001 | 47 / 52 | 10 / 17 / 18 / 21 / 19 / 15 | [1014461401032354](https://www.facebook.com/ads/library/?id=1014461401032354) (110,359) |
| E | VM aesthetics - Център за лазерна епилация | 2 (0 active) | 2026-07-06 → 2026-09-05 | All 18-35 ×2 | Pazardzhik Province, Bulgaria ×2 | 129,644 | 42 / 58 | 30 / 64 / 6 / 0 / 0 / 0 | [1650959832645129](https://www.facebook.com/ads/library/?id=1650959832645129) (71,631) |
| E | Derma-Act | 2 (0 active) | 2026-05-26 → 2026-08-12 | Women 25-55 ×1; Women 22-47 ×1 | Sofia, Bulgaria ×2 | 126,888 | 100 / 0 | 1 / 33 / 32 / 31 / 3 / 0 | [1331237678984594](https://www.facebook.com/ads/library/?id=1331237678984594) (97,386) |
| E | Laser Expert | 1 (0 active) | 2025-11-01 → 2025-11-01 | All 18-65 ×1 | Sofia, Bulgaria ×1 | 126,697 | 37 / 62 | 7 / 12 / 17 / 23 / 24 / 17 | [1167511598814308](https://www.facebook.com/ads/library/?id=1167511598814308) (126,697) |
| E | Естетичен център Satori | 2 (0 active) | 2025-09-30 → 2026-01-16 | Men 20-50 ×1; Men 20-55 ×1 | Sofia, Bulgaria ×2 | 91,075 | 0 / 100 | 14 / 42 / 28 / 15 / 1 / 0 | [831474772743303](https://www.facebook.com/ads/library/?id=831474772743303) (62,610) |
| E | Beauty Derm | 1 (1 active) | 2026-02-09 → 2026-02-09 | Women 18-50 ×1 | Varna, Bulgaria ×1 | 75,344 | 100 / 0 | 25 / 38 / 26 / 11 / 0 / 0 | [1630704358295830](https://www.facebook.com/ads/library/?id=1630704358295830) (75,344) |
| E | Нирвана Естетичен център | 1 (0 active) | 2026-02-02 → 2026-02-02 | Women 25-65 ×1 | Sofia Province, Bulgaria; Sofia, Bulgaria ×1 | 55,881 | 64 / 35 | 0 / 32 / 35 / 21 / 8 / 5 | [1544847256572315](https://www.facebook.com/ads/library/?id=1544847256572315) (55,881) |
| E | Skin Line | 1 (1 active) | 2026-09-21 → 2026-09-21 | Women 18-65 ×1 | Plovdiv, Bulgaria; Sofia, Bulgaria; Varna, Bulgaria ×1 | 49,537 | 40 / 60 | 1 / 2 / 3 / 10 / 26 / 58 | [964886106634150](https://www.facebook.com/ads/library/?id=964886106634150) (49,537) |
| E | Лоримар лазерна естетика | 1 (1 active) | 2026-09-14 → 2026-09-14 | Women 18-65 ×1 | Stara Zagora, Bulgaria ×1 | 41,871 | 52 / 47 | 3 / 12 / 25 / 26 / 19 / 14 | [1634724104986114](https://www.facebook.com/ads/library/?id=1634724104986114) (41,871) |
| E | Orange Aesthetics | 1 (1 active) | 2026-06-04 → 2026-06-04 | Women 18-55 ×1 | Sofia, Bulgaria ×1 | 41,480 | 92 / 7 | 9 / 20 / 36 / 33 / 2 / 0 | [2193828231410286](https://www.facebook.com/ads/library/?id=2193828231410286) (41,480) |
| E | Laser Derm | 1 (0 active) | 2025-12-02 → 2025-12-02 | Women 18-65 ×1 | Dulovo, Bulgaria ×1 | 34,327 | 52 / 48 | 4 / 9 / 12 / 18 / 29 / 28 | [1496602691599595](https://www.facebook.com/ads/library/?id=1496602691599595) (34,327) |
| E | MORE laser center | 1 (0 active) | 2026-04-04 → 2026-04-04 | All 18-65 ×1 | Burgas, Bulgaria ×1 | 32,403 | 54 / 45 | 3 / 8 / 11 / 15 / 27 / 35 | [4505736946379598](https://www.facebook.com/ads/library/?id=4505736946379598) (32,403) |
| E | Естетичен център Елинор | 1 (1 active) | 2026-01-13 → 2026-01-13 | Women 18-65 ×1 | Sofia, Bulgaria ×1 | 32,340 | 54 / 46 | 2 / 6 / 11 / 20 / 30 / 31 | [1473198864811931](https://www.facebook.com/ads/library/?id=1473198864811931) (32,340) |
| E | ASIA health & beauty | 1 (0 active) | 2026-05-12 → 2026-05-12 | Women 18-65 ×1 | Lovech, Bulgaria; Pleven, Bulgaria; Veliko Tarnovo, Bulgaria; Vratza, Bulgaria ×1 | 29,601 | 100 / 0 | 7 / 10 / 18 / 32 / 17 / 17 | [1735584977465250](https://www.facebook.com/ads/library/?id=1735584977465250) (29,601) |
| E | Лазерна Епилация Бургас /Микронидлинг/ Козметика - Център Under your Skin | 1 (0 active) | 2025-12-03 → 2025-12-03 | All 18-45 ×1 | Burgas, Bulgaria ×1 | 27,944 | 44 / 56 | 39 / 41 / 18 / 2 / 0 / 0 | [2000530734061168](https://www.facebook.com/ads/library/?id=2000530734061168) (27,944) |
| E | Allúre Beauty Studio | 1 (0 active) | 2026-02-03 → 2026-02-03 | Women 18-65 ×1 | Burgas Province, Bulgaria; Yambol, Yambol, Bulgaria ×1 | 27,916 | 100 / 0 | 9 / 10 / 8 / 9 / 21 / 43 | [1604756073895745](https://www.facebook.com/ads/library/?id=1604756073895745) (27,916) |
| E | BOMI Laser Studio | 1 (0 active) | 2026-01-21 → 2026-01-21 | Women 20-40 ×1 | Sofia City Province, Bulgaria ×1 | 22,267 | 100 / 0 | 21 / 53 / 26 / 0 / 0 / 0 | [4387207808228130](https://www.facebook.com/ads/library/?id=4387207808228130) (22,267) |
| E | Satori Clinics | 1 (1 active) | 2026-08-06 → 2026-08-06 | Women 20-50 ×1 | Sofia, Bulgaria ×1 | 15,563 | 100 / 0 | 27 / 50 / 18 / 5 / 0 / 0 | [2458411064668790](https://www.facebook.com/ads/library/?id=2458411064668790) (15,563) |
| E | Медико-естетичен център Grand | 1 (0 active) | 2026-06-01 → 2026-06-01 | Women 18-65 ×1 | Velingrad, Bulgaria ×1 | 14,549 | 72 / 28 | 10 / 20 / 24 / 17 / 16 / 13 | [1507019794405557](https://www.facebook.com/ads/library/?id=1507019794405557) (14,549) |
| E | д-р Лилия Гюдюлева | 1 (1 active) | 2026-10-02 → 2026-10-02 | Women 30-55 ×1 | Plovdiv, Bulgaria ×1 | 5,150 | 100 / 0 | 0 / 9 / 28 / 54 / 8 / 0 | [1450141163643829](https://www.facebook.com/ads/library/?id=1450141163643829) (5,150) |
| E | La Belle Clinic | 1 (1 active) | 2026-10-04 → 2026-10-04 | Women 24-65 ×1 | Varna, Bulgaria ×1 | 4,988 | 70 / 30 | 2 / 14 / 12 / 16 / 21 / 37 | [1805980517380444](https://www.facebook.com/ads/library/?id=1805980517380444) (4,988) |
| E | GM Studio | 1 (1 active) | 2026-09-28 → 2026-09-28 | Women 18-65 ×1 | Plovdiv, Bulgaria ×1 | 1,331 | 84 / 16 | 16 / 27 / 28 / 13 / 7 / 9 | [1084708804295660](https://www.facebook.com/ads/library/?id=1084708804295660) (1,331) |

- **G Point** runs city-specific copies, for example "Пловдив, време е за истински резултати! Всяка регистрация = БЕЗПЛАТНА зона!🎁 Мишници или интим? Ти избираш!" — [ad 2144026433122255](https://www.facebook.com/ads/library/?id=2144026433122255). Price-list copy reads "✔️Цели крака - 45 € ✔️Мишници - 19 € ✔️Пълен интим - 24 €" — [ad 1057150097191827](https://www.facebook.com/ads/library/?id=1057150097191827). Summed G Point reach by targeted city:
  - Sofia 716,083 (2 ads)
  - Plovdiv 545,834 (2 ads)
  - Varna 380,988 (2 ads)
  - national 254,639 (2 ads)
  - Ruse 228,721 (2 ads)
  - Burgas 164,918 (2 ads)
  - 19 smaller towns
  
  Source: [G Point page](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BG&view_all_page_id=106545644262179&search_type=page&media_type=all); per-ad data in the CSV.
- **Abi Beauty** (Sofia):
  - New-client gift ads, "ПОДАРЪК ЛАЗЕРНА ЕПИЛАЦИЯ ЗА НОВИ КЛИЕНТИ… враснали косми": Women 18–54, age 38/33/19/9 — [ad 1419568556966783](https://www.facebook.com/ads/library/?id=1419568556966783).
  - A men's version: Men 18–54, age 23/37/28/12 — [ad 2305166276913777](https://www.facebook.com/ads/library/?id=2305166276913777).
  - Its January "Women 18–65" ads delivered **64% men and 65% aged 55+** — [ad 1167757538465190](https://www.facebook.com/ads/library/?id=1167757538465190).
- Other examples:
  - **Satori** (Sofia): men-only laser ads (Men 20–55), 100% M, 25–34 = 42% — [ad 831474772743303](https://www.facebook.com/ads/library/?id=831474772743303).
  - **Derma-Act** (Sofia): "лазерна епилация интим и бикини линия" catalogue ad, Women 25–55, age 1/36/27/33/3/0 — [ad 1331237678984594](https://www.facebook.com/ads/library/?id=1331237678984594).
  - **д-р Гюдюлева** (Plovdiv): Women 30–55 — [ad 1450141163643829](https://www.facebook.com/ads/library/?id=1450141163643829).
  - **Skin Line**: "Women 18–65" but delivered 60% M, with 58% aged 65+ — [ad 964886106634150](https://www.facebook.com/ads/library/?id=964886106634150).
  - **Vitalaiz** (Burgas) ingrown-hook laser ads: All 25–65 or Women 18–65 — [ad 975425235609388](https://www.facebook.com/ads/library/?id=975425235609388).

### Inferences
- The **premium-alternative (bikini laser) segment is women 25–44, then 45–54**. Clinics deliberately cap age at 45–55, while DTC ingrown sellers leave 18–65 open and Meta finds 18–34. A pad brand can treat clinic prospects aged 25–44 who are put off by price ("Пълен интим" at €24 per session, packages more) as a secondary audience with a "between sessions / instead of laser" angle.
- Clinic ads delivering to men and 55+ despite "Women" settings most likely run engagement or message objectives with Advantage+ audience expansion. Their demographics are weak evidence of who buys, so the women-only bikini subset is the better read.

### Gaps
- Clinic campaign objectives (messages, leads, traffic) are not visible. Booking or conversion data is not public.
- The rate limit capped clinic coverage at the first 30 ads per query or page. Many smaller clinics are represented by a single ad.

## 5. Aggregate: share of reach by gender and age bucket; Sofia vs the rest of Bulgaria

### Takeaway
Pooled across the 395 relevant ads, women receive **79–93% of reach in every category**. The **ingrown-hair category is the youngest**, with 74% of reach aged 18–34, against 50% for hair-removal products, 40% for exfoliation/body care, 42% for laser clinics and 21% for intimate care. **Sofia vs the rest cannot be measured from reach.** Meta's EU breakdown is country-level only, and every DTC competitor targets all of Bulgaria.

### Cited Findings
**All categories** (A = direct ingrown treatment; B = exfoliation/body care; C = hair-removal and hair-growth products; D = intimate care; E = laser clinics, hair-removal ads only):

| Category | Ads with EU data | Summed EU reach | % women / men / unknown | Age split % | Subset with open targeting |
|---|---|---|---|---|---|
| A. Ingrown-hair treatment (direct) | 79 | 2,356,050 | 91.4 / 7.5 / 1.0 | 35 / 39 / 18 / 6 / 1 / 1 | 46 ads: 91.1 / 7.8; 36 / 40 / 17 / 6 / 1 / 1 |
| B. Exfoliation / body care | 56 | 2,731,743 | 90.1 / 9.4 / 0.5 | 13 / 27 / 25 / 17 / 11 / 8 | 22 ads: 81.9 / 17.3; 4 / 12 / 17 / 21 / 24 / 22 |
| C. Hair-removal & hair-growth products | 104 | 12,156,070 | 86.4 / 12.7 / 0.9 | 20 / 30 / 27 / 14 / 6 / 2 | 61 ads: 84.4 / 14.5; 22 / 30 / 25 / 15 / 6 / 2 |
| D. Intimate care | 66 | 5,180,404 | 93.2 / 6.3 / 0.5 | 7 / 14 / 22 / 27 / 19 / 11 | 15 ads: 87.5 / 11.8; 6 / 11 / 23 / 29 / 17 / 14 |
| E. Laser clinics | 90 | 5,128,716 | 79.4 / 20.4 / 0.2 | 13 / 29 / 27 / 19 / 7 / 6 | 2 ads: 40.5 / 58.3; 6 / 11 / 16 / 21 / 25 / 21 |

**Women × age grid** (% of each category's reach; women / men):

| Category | 18-24 W / M | 25-34 W / M | 35-44 W / M | 45-54 W / M | 55-64 W / M | 65+ W / M |
|---|---|---|---|---|---|---|
| A. Ingrown-hair treatment (direct) | 32.6 / 2.1 | 35.6 / 3.1 | 16.3 / 1.6 | 5.2 / 0.6 | 1.2 / 0.2 | 0.5 / 0.1 |
| B. Exfoliation / body care | 11.9 / 1.2 | 24.1 / 2.6 | 22.6 / 2.1 | 15.0 / 1.5 | 9.7 / 1.1 | 6.8 / 0.8 |
| C. Hair-removal & hair-growth products | 17.7 / 2.4 | 25.3 / 4.4 | 23.5 / 3.2 | 12.7 / 1.7 | 5.3 / 0.7 | 2.0 / 0.3 |
| D. Intimate care | 6.4 / 0.3 | 13.1 / 0.7 | 21.1 / 1.1 | 25.1 / 1.7 | 18.1 / 1.3 | 9.4 / 1.2 |
| E. Laser clinics | 10.6 / 1.9 | 23.2 / 5.3 | 22.3 / 4.5 | 15.4 / 3.5 | 4.1 / 2.9 | 3.7 / 2.3 |

**Targeting setting versus delivery, by category:**

| Subset | Ads | Summed reach | % W / M / unknown | Age split % |
|---|---|---|---|---|
| A: targeted Women | 33 | 432,549 | 93.0 / 6.5 / 0.6 | 33 / 37 / 21 / 7 / 2 / 1 |
| A: targeted All genders | 46 | 1,923,501 | 91.1 / 7.8 / 1.1 | 36 / 40 / 17 / 6 / 1 / 1 |
| B: targeted All | 22 | 651,697 | 81.9 / 17.3 / 0.8 | 4 / 12 / 17 / 21 / 24 / 22 |
| B: targeted Women | 34 | 2,080,046 | 92.7 / 6.9 / 0.4 | 16 / 32 / 27 / 15 / 7 / 3 |
| C: targeted All | 62 | 7,966,277 | 83.6 / 15.2 / 1.2 | 22 / 30 / 25 / 15 / 6 / 2 |
| C: targeted Women | 42 | 4,189,793 | 91.7 / 7.8 / 0.4 | 17 / 29 / 30 / 14 / 7 / 3 |
| D: targeted All | 16 | 752,039 | 87.2 / 12.2 / 0.7 | 6 / 10 / 22 / 29 / 19 / 13 |
| D: targeted Women | 50 | 4,428,365 | 94.3 / 5.3 / 0.4 | 7 / 14 / 22 / 27 / 20 / 10 |
| E: targeted All | 18 | 640,311 | 39.6 / 59.7 / 0.7 | 15 / 35 / 24 / 11 / 9 / 7 |
| E: targeted Women | 69 | 4,389,484 | 87.1 / 12.8 / 0.1 | 12 / 27 / 27 / 20 / 7 / 6 |

- **Location:**
  - Every Deroli, LUMI, Bielle, Sèlestre, Cyra, Merréh, BeNatural, NONA and Glowie ad with EU data targets "Bulgaria" (country). Reach breakdowns are reported only at country level ("BG") — see per-ad rows above and the CSV, for example [ad 1580431803886169](https://www.facebook.com/ads/library/?id=1580431803886169).
  - Only clinics target cities: Sofia (Abi Beauty, Satori, Derma-Act, BOMI, Orange, Елинор, Нирвана, Laser Expert, VM Aesthetics), Burgas (Vitalaiz, MORE, GRAND, Under your Skin), Plovdiv (Гюдюлева, GM Studio), Varna (Beauty Derm, La Belle, CLINIC Varna), and others. G Point runs one ad set per city across ~25 towns.
  - One laser ad (Laser Derm, Dulovo) also delivered in Romania — [ad 1496602691599595](https://www.facebook.com/ads/library/?id=1496602691599595).

### Inferences
- **ICP from delivery evidence:** woman, **18–34 (core 25–34)**, anywhere in Bulgaria. She shaves or epilates the bikini line, legs and underarms and gets red dots and ingrown hairs. Secondary audiences:
  - women 35–44, about 16–18% of category reach
  - men 18–34, about 5% of category reach, a test segment
- Expect women 45+ to make up under 8% of reach for an ingrown-framed creative. Older women respond to dry-skin and intimate-odour framings instead.
- National targeting is the market norm for DTC. A Sofia-only test is not supported by any competitor practice observed. G Point's city reach (Sofia 25%, Plovdiv 19%, Varna 13% of its total) follows clinic locations and budget, not proven demand.

### Gaps
- Sofia vs rest split of reach: not available. Meta's `age_country_gender_reach_breakdown` stops at country, and DTC targeting is national.
- The pooled percentages weight advertisers by reach (LUMI is 81% of category A reach), so they describe the reach-weighted market, not the average advertiser.
- The Meta Ad Library *Report* (the country-level spend dashboard) was not opened in this session. Commercial spend per advertiser is not shown in the per-ad EU transparency data.

## 6. Creative angles and the audiences they reach (direct ingrown ads)

### Takeaway
Within the direct competitors, **testimonial and "after shaving / bikini line" copy reached the youngest audience** (LUMI testimonial 43/44/10). **Deroli's shame-led "Уморена ли си да криеш кожата си?" and mechanism ("Знаеш ли защо…") creatives reached the oldest** (35–44 = 26–29%). The LUMI "only product / 7 days / discount" ad, which carried most of the category's reach, sat at 36/39/17. The angle-level samples for Deroli's October creatives are tiny (under 3,000 reach), so these differences are directional only.

### Cited Findings
| Advertiser | Creative (first words of primary text) | Ads | Summed reach | % women | Age split % | Highest-reach ads |
|---|---|---|---|---|---|---|
| Deroli Cosmetics | dynamic {{product}} ads | 18 | 196,975 | 94 | 40 / 36 / 16 / 6 / 1 / 1 | [1272999705036195](https://www.facebook.com/ads/library/?id=1272999705036195), [35134290669548934](https://www.facebook.com/ads/library/?id=35134290669548934), [4335667636751697](https://www.facebook.com/ads/library/?id=4335667636751697) |
| Deroli Cosmetics | Враснали косми, тъмни петна и раздразнен | 19 | 253,423 | 92 | 29 / 38 / 23 / 8 / 2 / 1 | [1603053431394356](https://www.facebook.com/ads/library/?id=1603053431394356), [1622593279581302](https://www.facebook.com/ads/library/?id=1622593279581302), [1029734312805937](https://www.facebook.com/ads/library/?id=1029734312805937) |
| Deroli Cosmetics | Бръсненето не трябва да значи враснали к | 5 | 206 | 90 | 33 / 33 / 25 / 5 / 3 / 0 | [1112142581292268](https://www.facebook.com/ads/library/?id=1112142581292268), [1426778409542660](https://www.facebook.com/ads/library/?id=1426778409542660), [40038101975789171](https://www.facebook.com/ads/library/?id=40038101975789171) |
| Deroli Cosmetics | Знаеш ли защо враснали косми се появяват | 1 | 1,510 | 91 | 28 / 34 / 26 / 9 / 3 / 1 | [1706982660796460](https://www.facebook.com/ads/library/?id=1706982660796460) |
| Deroli Cosmetics | Уморена ли си да криеш кожата си?  От вр | 5 | 2,646 | 91 | 23 / 33 / 29 / 11 / 2 / 1 | [1580431803886169](https://www.facebook.com/ads/library/?id=1580431803886169), [1066995442837630](https://www.facebook.com/ads/library/?id=1066995442837630), [1521859699957366](https://www.facebook.com/ads/library/?id=1521859699957366) |
| LUMI | Единственият продукт, който премахва вра | 24 | 1,492,286 | 91 | 36 / 39 / 17 / 6 / 1 / 1 | [1299129028935876](https://www.facebook.com/ads/library/?id=1299129028935876), [1302228438511250](https://www.facebook.com/ads/library/?id=1302228438511250), [1558964905364199](https://www.facebook.com/ads/library/?id=1558964905364199) |
| LUMI | dynamic {{product}} ads | 4 | 323,647 | 91 | 33 / 40 / 19 / 6 / 1 / 1 | [3594968063986071](https://www.facebook.com/ads/library/?id=3594968063986071), [1072774725622074](https://www.facebook.com/ads/library/?id=1072774725622074), [1083151101351962](https://www.facebook.com/ads/library/?id=1083151101351962) |
| LUMI | След почти всяко бръснене кожата ми оста | 1 | 55,495 | 93 | 43 / 44 / 10 / 2 / 0 / 0 | [1691160699300876](https://www.facebook.com/ads/library/?id=1691160699300876) |
| LUMI | Ако и при теб след бръснене или кола мас | 1 | 28,693 | 91 | 40 / 39 / 16 / 4 / 1 / 0 | [2072894626666208](https://www.facebook.com/ads/library/?id=2072894626666208) |

- LUMI testimonial: "След почти всяко бръснене кожата ми оставаше с червени точки, врастнали косъмчета и раздразнени…" got 55,495 reach in 7 days, 93% W, 43/44/10/2/0/0 — [ad 1691160699300876](https://www.facebook.com/ads/library/?id=1691160699300876).
- LUMI problem/mechanism copy: "Ако и при теб след бръснене или кола маска бикини зоната остава с врастнали косъмчета, червени…" got 28,693 reach, 91% W, 40/39/16/4/1/0 — [ad 2072894626666208](https://www.facebook.com/ads/library/?id=2072894626666208).
- Deroli's shame hook "Уморена ли си да криеш кожата си?… на плажа, в интимни моменти" got 1,693 reach, 90% W, 20/33/31/13/3/1 — [ad 1580431803886169](https://www.facebook.com/ads/library/?id=1580431803886169).
- Deroli's problem stack "Враснали косми, тъмни петна и раздразнена кожа след депилация…": 19 ads, 253,423 reach, 29/38/23/8/2/1 — [ad 1603053431394356](https://www.facebook.com/ads/library/?id=1603053431394356).

### Inferences
- For a pad launch, **shaving-moment testimonials and bikini-line-after-shaving problem copy** are the angles most associated with 18–34 delivery. "Hiding skin / intimate moments" copy, and dark-spot or pigmentation as the lead benefit, pull slightly older (35–44). That suits a 25–44 premium or laser-alternative variant. The shame framing also carries Meta Health & Wellness policy risk (see the background note).
- Every direct-competitor ad uses feminine or female-addressed copy ("всяка жена", "Уморена ли си", "Заслужаваш", "3000+ жени"). LUMI's neutral copy still delivered 91% to women, so male reach does not need to be suppressed with copy. A separate men's creative would be needed to reach men deliberately.

### Gaps
- Angle comparisons mix time periods, budgets and settings: Deroli's Aug ads were Women-only, its Oct ads open. They are not controlled tests.
- Angle tags were assigned by keyword rules on the primary text. Images and video (hook frames, models' apparent age) were not reviewed.
