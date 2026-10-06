# Buyer psychographics and segments for ingrown-hair exfoliating pads (bikini, legs, underarms), for a Bulgarian ICP (Savenae Smooth Reset Pads) — research date 6 Oct 2026

Scope note: Savenae sells "Ексфолиращи тампони при враснали косъмчета", 50 pads, €18.90 (compare-at €22.90), "За крака, подмишници и външна бикини линия", "Не се използва върху лице, врат или лигавици", with "Безплатна доставка", "Плащане при доставка", "Гаранция за връщане на парите", "Изпраща се от България", currently "Предварителна поръчка" — [savenae.com product page](https://savenae.com/products/savenae-smooth-reset-pads). The product page makes no dark-spot or brightening claim; it promises smoother skin and fewer trapped hairs ("Помагат на косъмчетата да излизат свободно, вместо да врастват"). Everything below from US/UK retailers is a **global proxy**, not Bulgarian evidence, unless it is labelled BG. This file builds on, and does not repeat, `research_notes/Тампони за врастнали косми в България/ads_and_customer_voice_bg.md` (BG ads, prices, 2010–2020 bg-mamma VOC).

**How the review data was gathered (applies to every tally below):**
- **Sephora** reviews came from Sephora's public Bazaarvoice review feed: `https://api.bazaarvoice.com/data/reviews.json?Filter=ProductId:<ID>&passkey=calXm2DyQVjcCy9agq85vmTJv5ELuuBCF2sdg4BnJzJus&apiversion=5.4&Locale=en_US&Limit=100`. Products pulled: P479320 First Aid Beauty (FAB) Ingrown Hair Pads, 408 reviews; P63308 Bliss Ingrown Eliminating Pads, 776; P479355 Topicals High Roller tonic, 1,097; P170545 Anthony Ingrown Hair Treatment, 139; P378718 Jack Black Bump Fix, 120.
- **Ulta** reviews came from Ulta's public PowerReviews feed: FAB pads (pimprod2057164), 226 reviews; Bushbalm Radiant Reset pads (pimprod2045737), 49 reviews.
- **Bushbalm** reviews came from its public Okendo feed: the Radiant Reset pads (47 reviews) and the 3,000 most recent store-wide reviews, dated 19 Jul 2025–6 Oct 2026. Okendo also stores reviewer self-reported attributes (age, skin tone, skin type, hair-removal method, application area, skin concern).
- **Amazon** data is the "Customers say" aspect counts plus the top reviews on the product page, scraped with Firecrawl.
- **Coding:** areas, methods and objections were tagged with keyword rules in Python, so counts are approximate. FAB Sephora and Ulta reviews were de-duplicated on body text, leaving FAB n=577 (Dec 2021–Aug 2026).
- **Incentives:** 36 of the 577 FAB reviews are flagged as incentivized or received free. 2,014 of the 3,000 Bushbalm store reviews carry Okendo's `isIncentivized` flag, and so do 1,489 of the 1,827 reviews that answered the attribute questions. Treat Bushbalm sentiment as positively biased; the attribute distributions (who buys) are less affected.

## 1. Which buyer segments exist, and how do they rank by frequency? (triggers, JTBD, emotions, desired outcome, failed solutions, objections, words)

### Takeaway
The dominant buyer is a **woman aged 25–44 who shaves her bikini line (and often her underarms) at home**. She has red bumps and ingrown hairs, usually reports sensitive skin, and buys after many failed fixes, often with a summer, beach or partner trigger. **Post-wax (Brazilian) clients** are a strong second, skewing younger. **Underarm** and **legs/"strawberry legs"** users are large overlapping use-cases rather than separate people. **Dark marks and scars** concern about a third of buyers, and that share rises steeply with darker skin tone. **Men, between-laser clients and coarse-hair self-identifiers** are small in the review data. Men mostly appear through a female partner who buys and shares the product.

### Cited Findings
**Frequency evidence: Bushbalm reviewer self-reported attributes (proxy, mostly US/Canada, n = reviewers who answered each question, 3,000 reviews from 19 Jul 2025–6 Oct 2026)** — [Bushbalm Okendo review feed](https://api.okendo.io/v1/stores/cb31d0ec-c21a-406d-8287-1d91c3b18f7c/reviews?limit=100&orderBy=date%20desc); [Bushbalm pads page](https://bushbalm.com/products/radiant-reset-exfoliating-toner-pads)

| Attribute | Breakdown |
|---|---|
| Application area (n=1,363, multi-select) | Bikini line 1,176 (86.3%) · Underarms 624 (45.8%) · Legs 504 (37.0%) · Face 164 (12.0%) |
| Hair-removal method (n=1,729, multi-select) | Shaving 1,024 (59.2%) · Waxing 835 (48.3%) · Lasering 119 (6.9%) · "Other" 97 (5.6%) · Trimming 55 (3.2%) · "I embrace the bush" 54 (3.1%) · Epilating 37 (2.1%) · Sugaring 27 (1.6%) |
| Skin concern (n=1,654) | Ingrown hairs 1,454 (87.9%) · Razor bumps 1,013 (61.2%) · Dark spots 590 (35.7%) |
| Age (n=1,738) | Under 18: 10 (0.6%) · 18–24: 301 (17.3%) · 25–34: 492 (28.3%) · 35–44: 499 (28.7%) · 45–54: 306 (17.6%) · 55+: 124 (7.1%) · Prefer not to say: 42 (2.4%) |
| Skin type (n=1,679) | Sensitive 929 (55.3%) · Combination 565 · Dry 411 · Oily 75 |

- Cross-tab, **dark-spot concern by skin tone**: fair 84/352 (24%), light 146/554 (26%), light-medium 36/111 (32%), olive 36/90 (40%), medium 166/368 (45%), tan 55/86 (64%), medium-dark 17/24 (71%), deep 48/57 (84%) — [Bushbalm Okendo feed](https://api.okendo.io/v1/stores/cb31d0ec-c21a-406d-8287-1d91c3b18f7c/reviews?limit=100&orderBy=date%20desc)
- Cross-tab, **concern by method**: shavers name razor bumps 790/978 (81%) and dark spots 305/978 (31%); waxers name razor bumps 353/785 (45%) and dark spots 323/785 (41%) — same source
- Cross-tab, **method by age**: ages 18–24 report waxing more than shaving (170 vs 149 of 294); ages 55+ report shaving 73/112 and waxing 34/112 — same source
- Cross-tab, **area by method**: bikini line is the top area for every method (shaving 651/764, waxing 540/603, lasering 59/71) — same source

**Frequency evidence: FAB Ingrown Hair Pads text mentions (proxy, Sephora + Ulta, n=577 de-duplicated, Dec 2021–Aug 2026)** — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320); [Ulta FAB](https://www.ulta.com/p/ingrown-hair-pads-with-bha-aha-pimprod2057164)
- Areas named: bikini 142 (24.6% of all reviews), underarm 91 (15.8%), legs 55 (9.5%), face/neck/beard 37 (6.4%), butt/back/chest 22 (3.8%). Among the 266 reviews that name any area: bikini 53%, underarm 34%, legs 21%.
- Methods named, among the 255 reviews that name one: shaving 211 (83%), waxing 67 (26%), laser 5 (2%), epilator 2, depilatory cream 2, sugaring 1.
- Self-described sensitive skin: 70 (12.1%). Strawberry legs/KP/"chicken skin": 19 (3.3%). Dark marks, scars or discoloration: 26 (4.5%). Explicitly "coarse/curly/dark hair": 4 (0.7%).
- Men: **0 reviews self-identify as male**. 16 reviews (2.8%) mention a husband, boyfriend, fiancé or son using the product, mostly on the face or neck.
- Average rating by area: bikini 4.59 (n=142), underarm 4.68 (n=91), legs 4.58 (n=55), wax-mentioning reviews 4.82 (n=67), against 4.36 overall.

**Frequency evidence: older and adjacent products (proxies)**
- Bliss Ingrown Eliminating Pads on Sephora (n=776, **2008–2015, dated**): bikini named in 208 (26.8%), waxing in 164 (21.1%), shaving in 205 (26.4%), post-wax context in 50 (6.4%), price/value mentioned in 206 (26.5%), "cut the pad in half" in 20 — [Sephora/Bazaarvoice P63308](https://api.bazaarvoice.com/data/reviews.json?Filter=ProductId:P63308&passkey=calXm2DyQVjcCy9agq85vmTJv5ELuuBCF2sdg4BnJzJus&apiversion=5.4&Locale=en_US&Limit=100)
- Topicals High Roller tonic on Sephora (n=1,097, Jan 2022–Sep 2026): bikini 216 (19.7%), underarm 166 (15.1%), dark marks/scars 132 (12.0%), PCOS/hormones 18 — [Sephora/Bazaarvoice P479355](https://api.bazaarvoice.com/data/reviews.json?Filter=ProductId:P479355&passkey=calXm2DyQVjcCy9agq85vmTJv5ELuuBCF2sdg4BnJzJus&apiversion=5.4&Locale=en_US&Limit=100)
- Men's-brand ingrown treatments, Anthony + Jack Black on Sephora (n=259, 2008–2024): only 2 reviews self-identify as male. 39 (15.1%) say the product was bought for or used by a husband/boyfriend/son, and 37 (14.3%) mention the bikini area, mostly women using a men's product — [Sephora/Bazaarvoice P170545](https://api.bazaarvoice.com/data/reviews.json?Filter=ProductId:P170545&passkey=calXm2DyQVjcCy9agq85vmTJv5ELuuBCF2sdg4BnJzJus&apiversion=5.4&Locale=en_US&Limit=100); [P378718](https://api.bazaarvoice.com/data/reviews.json?Filter=ProductId:P378718&passkey=calXm2DyQVjcCy9agq85vmTJv5ELuuBCF2sdg4BnJzJus&apiversion=5.4&Locale=en_US&Limit=100)

**Segment-defining quotes (proxy; verbatim)**
- *Home bikini shaver:* "As someone who still shaves my bikini line versus having laser hair removal, this product is one I wish I had been using sooner." (dwalke39, 10 Feb 2026, incentivized) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
- *Post-wax:* "I get a Brazilian wax every month and aftercare in the weeks between waxes is essential to prevent ingrown hair" (jenlea14, 16 Jun 2022) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
- *Underarm:* "Over the last few years I get horrific ingrown cystic hairs in my armpits after shaving. After numerous deodorant switches, razor changes, shaving creams, exfoliators, etc. nothing seemed to remedy the issue." (aez1995, 17 Jun 2022) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
- *Legs/KP:* "Helped with my strawberry legs and ingrown hairs in my bikini line." (SuzyDB, 1 Apr 2026) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
- *Dark marks:* "I always struggled with ingrowns that left dark spots" (Zoi H., deep skin tone, 18–24, shaving, bikini line, 18 Sep 2026) — [Bushbalm Dark Spot Oil](https://bushbalm.com/products/dark-spot-treatment)
- *Coarse/dark hair + fair skin:* "I have dark coarse hair and fair sensitive skin… ingrown hairs are a huge struggle and a big insecurity of mine." (westcoastbeaut, 11 Oct 2023) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
- *Wants laser but can't yet:* "(I'm someone who definitely wants laser hair removal once I have enough money)" (Michelle C., 24 Mar 2026); "Right now, during pregnancy and breastfeeding, I can't do laser hair removal, so shaving is my only option." (Iryna B., 23 Mar 2026) — [Bushbalm Shave Jelly](https://bushbalm.com/products/shave-jelly-watermelon-sugar)
- *Men, reached through a partner:* "I actually purchased this product for my boyfriend. He gets a haircut faithfully every week - followed by bumps and ingrown hairs." (theOGtiffani, 26 Apr 2022) — [Ulta FAB](https://www.ulta.com/p/ingrown-hair-pads-with-bha-aha-pimprod2057164)
- *Severe or medical (boundary case):* "I tried getting rid of two ingrown hairs in the groin area that appeared after shaving for weeks using some ointment my doctor gave me but wasn't noticing any changes. I saw this on TikTok and after just TWO DAYS of using this product the ingrown hairs disappeared completely!" (Nicole J, 2 Aug 2026) — [Amazon US FAB](https://www.amazon.com/First-Aid-Beauty-Ingrown-Hair/dp/B0GSWW3RFP)

### Inferences
**Segment ranking (inference; frequency uses Bushbalm attributes as the primary weight and FAB text mentions as the secondary weight; segments overlap)**

| Rank | Segment | Frequency evidence | Fit with Savenae (legs, underarms, outer bikini only) |
|---|---|---|---|
| 1 | **A. Women who shave the bikini line at home** (often also underarms) | Shaving 59% (Bushbalm); bikini line 86% of areas; 83% of FAB method mentions | Core fit |
| 2 | **B. Post-wax / Brazilian-wax clients** | Waxing 48% (Bushbalm), 58% among ages 18–24; 26% of FAB method mentions; 21% of Bliss reviews | Strong fit (must wait 24–48 h after waxing; see objections) |
| 3 | **C. Underarm shavers** (bumps, odor, darkening) | 46% of Bushbalm areas; 34% of FAB area mentions | Fit |
| 4 | **D. People with dark marks or scars from ingrowns** | 36% of Bushbalm concerns, rising to 64–84% for tan/deep tones; 12% of Topicals reviews; 4.5% of FAB | Partial fit. Savenae makes no brightening claim, so expectations may not match |
| 5 | **E. Legs: strawberry legs / KP / red dots** | 37% of Bushbalm areas; 9.5% legs and 3.3% KP in FAB | Fit, but small pads are a known objection on large areas |
| 6 | **F. Sensitive-skin self-identifiers** (cuts across A–E) | 55% of Bushbalm skin types; 12% of FAB | Fit if "doesn't sting" is shown credibly |
| 7 | **G. Laser aspirants and between-session users** | Lasering 6.9% (Bushbalm); FAB under 1% | Niche; a "bridge until laser" message |
| 8 | **H. Dark, coarse or curly hair self-identifiers** | Under 3% explicit mentions in reviews; implicit in A–D | Relevant in BG (see question 4) |
| 9 | **I. Men** (razor bumps, manscaping) | 0 self-identified men in FAB; 2.8% partner mentions; the 0.6% male-signal text tag in Bushbalm counts any male word, including husband/boyfriend references, not male reviewers | Weak: Savenae excludes face and neck, where most male use happens |
| 10 | **J. Severe or medical cases** (cysts, folliculitis, boils) | About 9 FAB mentions of cyst or infection | Not a target: these people go to a doctor or pharmacy |

**Segment profiles (inference built on the cited quotes in questions 1–5)**
- **A. Home bikini shaver (core).**
  - Triggers: summer or a trip ("before a trip to Mexico", "beach trips"); a new partner or date; a fresh flare-up after shaving.
  - Job to be done: "let me keep shaving at home without red bumps and hairs trapped under the skin, without paying for laser."
  - Emotions: insecurity, hiding, "TMI" embarrassment, then relief and confidence.
  - Desired outcome: a smooth, "clear" bikini line she does not have to hide.
  - Failed solutions: scrubs, loofahs and gloves, "every product and tip in the book", alcohol, picking.
  - Objections: "does it actually work?", stinging on freshly shaved skin, price per pad, "nothing works on me."
  - Her words: "razor bumps", "ingrowns", "bikini line", "down there", "red bumps", "smooth", "holy grail", "game changer".
- **B. Post-wax client.**
  - Triggers: the monthly Brazilian wax cycle, often on a salon or esthetician recommendation.
  - Job to be done: aftercare between waxes.
  - Emotions: maintenance pride; a "routine staple" ritual.
  - Objections: stings if used too soon after waxing; price, because she already pays for the salon.
  - Her words: "between waxes", "after care", "partner-in-crime".
- **C. Underarm shaver.**
  - Triggers: sleeveless season; dark underarms; odor.
  - Desired outcome: "sleeveless clothing" confidence. Reviewers also report deodorant-like or less-odor side benefits ("doubles as a deodorant", "helped me smell and discoloration"). Savenae makes no such claim.
  - Objections: burning on thin underarm skin.
- **D. Dark marks or scars.** The emotional peak, with the longest suffering ("I could cry writing this").
  - Desired outcome: an even tone.
  - Key risk: Savenae's page makes no dark-spot claim. BG competitors (Deroli, LUMI) do promise "изсветлява петна", so this segment may compare unfavourably.
- **E. Legs / strawberry legs.** Triggers: shorts and dress season. Objection: small pads mean "go through really fast".
- **I. Men.** The female partner is often the buyer and decision-maker ("my husband even uses them"). Men's own needs centre on the face, neck and haircut line, which Savenae excludes. Groin and manscaping use exists but is rarely verbalised in reviews.

### Gaps
- No source records **gender** as a field. The male share is inferred from text, which undercounts men who don't mention it, and Sephora, Ulta and Bushbalm skew female by audience. No men-focused pad product with reviewer attributes was mined: Completely Bare and Anthony pads on Amazon were not scraped because Firecrawl credits ran low.
- Bushbalm attributes are self-selected, mostly incentivized and US/Canada-centric. They show who reviews, not the share of all buyers.
- The keyword coding is approximate. For example, "face" catches "I also use it on my face". The rankings should be read as orders of magnitude.

## 2. Review mining of the leading pad products: tallies (age, area, method, skin type) and representative verbatim quotes

### Takeaway
Across 577 FAB pad reviews, 49 Bushbalm pad reviews (Ulta) plus 47 (bushbalm.com), 776 Bliss pad reviews, Amazon aspect summaries, and Amazon UK for Skin Doctors Ingrow Go, the praise is about **speed ("after 3 times", "within days") and the end of a long run of failures**. The complaints are about **no effect, irritation or stinging, and price per pad**: small pads, dry pads, and cutting pads in half to make them last. Reviewer profiles skew **light-to-medium skin and brown or black hair**. Sensitive skin is the most common self-description in Bushbalm's reviewer attributes (55%).

### Cited Findings
**Tallies**
- FAB pads (Sephora + Ulta, n=577): ratings 400×5★, 88×4★, 27×3★, 19×2★, 43×1★ (average 4.36). By year: 2021: 11, 2022: 306, 2023: 92, 2024: 68, 2025: 37, 2026: 63 — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320); [Ulta FAB](https://www.ulta.com/p/ingrown-hair-pads-with-bha-aha-pimprod2057164)
- FAB Sephora reviewer **skin tone** (profile field, n=323): Fair 68, Fair Light 28, Light 92, Light Medium 59, Medium 33, Medium Tan 18, Tan 11, Deep 11, Rich 3. That makes fair-to-light-medium 76.5%. **Hair colour** (n=314): Brown 158, Black 72, Blonde 65, Red 13, Auburn 6, so 73% brown or black. **Skin type** (n=337): Combination 183, Dry 61, Normal 58, Oily 35 — [Sephora/Bazaarvoice P479320](https://api.bazaarvoice.com/data/reviews.json?Filter=ProductId:P479320&passkey=calXm2DyQVjcCy9agq85vmTJv5ELuuBCF2sdg4BnJzJus&apiversion=5.4&Locale=en_US&Limit=100). Sephora's age field was filled by only 24 reviewers, so it is not usable.
- FAB **1–2★ reviews (n=62)**, themes coded by regex: no effect 25, irritation/breakout/"made it worse" 20, price/value 16, stinging/burning 8, smell 3, dry pads 1 — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320); [Ulta FAB](https://www.ulta.com/p/ingrown-hair-pads-with-bha-aha-pimprod2057164)
- FAB **stinging/burning/tingling**: mentioned in 80 of 577 reviews, excluding "razor burn". Of these, 31 say it does *not* sting, so about 49 (8.5%) report some sting — same sources. Comparison figures: Bliss pads about 69 of 776 report sting; Topicals about 49 of 1,097.
- FAB pads on **Amazon US**: 5,651 global ratings, 4.5★ (72% 5★, 3% 1★). Amazon's "Customers say" aspect counts: Effectiveness 445 (347 positive / 98 negative); Ingrown hair reduction 225 (188/37); Value for money 141 (75/66); Skin compatibility 77 (50/27); Life-saving 43 (40/3); Fragrance 36 (29/7); Drying time 31 (20/11); Skin improvement 26 (23/3) — [Amazon US FAB](https://www.amazon.com/First-Aid-Beauty-Ingrown-Hair/dp/B0GSWW3RFP)
- Skin Doctors **Ingrow Go on Amazon UK**: 8,041 ratings, 4.2★. Aspect counts: Effectiveness 532 (374/158); Quality 460 (364/96); Ingrown hair reduction 299 (223/76); Skin irritation 143 (32/**111 negative**); Value for money 142 (91/51); Odor 123 (25/**98 negative**); Dryness 82 (29/53); Durability 54 (37/17) — [Amazon UK Ingrow Go](https://www.amazon.co.uk/Skin-Doctors-Ingrow-Go-120ml/dp/B000CST4H0)
- Bushbalm Radiant Reset pads: Ulta n=49, average 4.69 (Mar 2024–Mar 2026) — [Ulta Bushbalm](https://www.ulta.com/p/radiant-reset-toner-pads-dark-spots-ingrown-hairs-pimprod2045737). bushbalm.com n=47; of reviewers who answered: Application Areas Underarms 8, Bikini Line 12, Face 2, Legs 1; method Waxing 9, Shaving 5; concerns Ingrown 12, Dark Spots 11; skin type Sensitive 10 of 16 — [Bushbalm pads](https://bushbalm.com/products/radiant-reset-exfoliating-toner-pads)
- Discovery and triggers named in text (counts): TikTok — FAB 2, Topicals 4, Bushbalm 2; esthetician/waxer — Bliss 17, Bushbalm 25, FAB 4; summer/vacation/beach/pool — FAB 45 (7.8%), Topicals 65, Bushbalm 120; "tried everything / nothing worked" — FAB 17, Bliss 22, Topicals 18; travel/convenience — FAB 37, Topicals 83, Bushbalm 198 — same sources

**Representative verbatim quotes (proxy; 34 quotes)**
1. "I've been more self-conscious of ingrown hairs as the weather warms up. These have been terrific to use on my bikini line." (KTWill, 6 Jun 2022, 5★) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
2. "I used these pads religiously on my legs and bikini line a few weeks before a trip to Mexico and I saw a hugeee improvement. Only con is the pads are small so I did go through really fast" (westcoastbeaut, 11 Oct 2023) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
3. "I am happy something finally works for Ingrown hairs! … I no longer have to hide my bikini line!" (ROJONYC, 3 May 2023, 4★) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
4. "TMI but I got waxed down there and had severe irritation and ingrown hair - this (plus some aloe vera gel after) healed everything up in less than two weeks! Worth it! Price is kinda sus but if you're really looking for something that'll work, then worth it!" (deliriousdua, 8 Dec 2024, 4★) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
5. "I will use it for the first few days after shaving (I wait a day or two to use after waxing) and the result is always ZERO ingrown hairs." (rwh1203, 12 Apr 2026) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
6. "Theres absolutely no way I can avoid my ingrown hairs, I have tried every product and tip in the book however these are great for reducing the scareing I suffer with afterwards. Without these my marks would take forever to fade." (Nebeh, 1 Feb 2024, 3★) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
7. "I could cry writing this, but I have been struggling with ingrown hairs and discoloration from razor bumps, and these pads have done wonders. Don't expect immediate results!!!!" (Yajjyen, 7 Mar 2023, tagged Sephora employee) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
8. "I tried this out before a couple beach trips … so easy to pop into your bag instead of juggling liquids and extra cotton rounds. The only downside would be that it's a bit pricey and I found I needed to use it consistently" (sincerelyemmie, 13 Jul 2022, 4★) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
9. "…all I wanna do now is shave my armpits so I can put sleeveless clothing." (Janeliz07, 23 Jun 2022) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
10. "I shave which makes me very prone of ingrown hair and so far I've gotten none. Also, it has helped me smell and discoloration." (SquishyPam, underarms, 11 Apr 2026) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
11. "Zero stinging or irritation EVEN applying it immediately after shaving!" (mmh1210, 6 May 2024) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
12. "I was really worried they burn/sting, but they did not at all!" (aph18, 25 Jun 2022) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
13. "Don't use it immediately after shaving (follow the directions) or it will burn a bit and could irritate the skin more." (Rosestr, 6 Nov 2022, 4★) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
14. "My husband has a really bad case of pseudofolliculitis barbae (razor bumps) and he has dark skin with curly beard hairs that curl into his skin … I couldn't find ANYTHING that worked for him. We were so close to finding a dermatologist when I came across this product" (AshNaomi, 15 Jun 2022) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
15. "First time in my entire life of shaving (35 years) I do NOT have any bumps, or irritation. Arm pits, legs, bikini NOTHING. NOT ONE! I am thrilled and my husband even noticed." (27 Mar 2026, 5★) — [Ulta FAB](https://www.ulta.com/p/ingrown-hair-pads-with-bha-aha-pimprod2057164)
16. "Saw a girl on TikTok rave about it, decided to try it out because I always suffered with bumpy skin after shaving/waxing. I tried literally everything to get rid of it … nothing worked. … After 3 times of using it I saw a drastic change on my legs!" (Daisy, 1 Aug 2022) — [Ulta FAB](https://www.ulta.com/p/ingrown-hair-pads-with-bha-aha-pimprod2057164)
17. "Tried this on my husband's ingrown neck hairs. Did not work but to be fair, the hairs are thick and curly." (MelissaInTN, 13 Aug 2024, 3★) — [Ulta FAB](https://www.ulta.com/p/ingrown-hair-pads-with-bha-aha-pimprod2057164)
18. "I have been using this for about a month now and I still don't see any difference." (Bambam, 10 Aug 2026, 1★) — [Ulta FAB](https://www.ulta.com/p/ingrown-hair-pads-with-bha-aha-pimprod2057164)
19. "There were less ingrowns with consistent use, 2-3 times a week for a few months. Unfortunately, they only decreased by about 40%. Definitely not worth $55" (Kubbaya, 12 Mar 2026, 2★) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
20. "the pads feel almost completely dry to the touch … I just paid $40 for a jar of cotton rounds." (GeminiCarolyn, 18 Jun 2026, 1★) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
21. "This product made me break out down there. … It has made me so insecure" (Chiam, 21 Jul 2025, 1★) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
22. "I cut the pad in half because I feel like a lot goes to waste … I've actually noticed I'm getting more ingrown hairs than I've ever had in my life and the sensitive areas I'm using these for are getting even darker." (gloomygirl, 7 Feb 2025, 1★) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
23. "the amount of product on the pads feels stingey and they're basically fully dry by the second application on your armpits … makes a big difference on itch especially on a bikini shave." (nikkibrof, 25 Aug 2025, 4★) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
24. "I was hesitant to try this because of the cost, but I gave in and it works! No itching, hairs are growing out normally, and scars are minimized..." (excerpt, review R1Q7O6R83346P0) — [Amazon US FAB](https://www.amazon.com/First-Aid-Beauty-Ingrown-Hair/dp/B0GSWW3RFP)
25. "Great product! Used it for after care with a bikini sugaring. It soothed the skin and prevented in-grown hairs." (excerpt, R6OUBDN0FV8AM) — [Amazon US FAB](https://www.amazon.com/First-Aid-Beauty-Ingrown-Hair/dp/B0GSWW3RFP)
26. "I have struggled with ingrown hairs on my bikini line for YEARS - I have tried everything from shaving, waxing, laser, even opting to pluck sometimes because I was so desperate to get rid of them and felt so insecure when summer came around when it was time to get in a bikini." (Ingrow Go, 23 Jul 2025, 5★) — [Amazon UK Ingrow Go](https://www.amazon.co.uk/Skin-Doctors-Ingrow-Go-120ml/dp/B000CST4H0)
27. "if you have a large amount of ingrowns or bumps, it can really sting. The stinging does go within a few minutes but you really have to push through it. You also have to get through the smell, the peeling skin and slight itchiness" (Leah, "Burns like beeeeech", 2 Jun 2024, 3★) — [Amazon UK Ingrow Go](https://www.amazon.co.uk/Skin-Doctors-Ingrow-Go-120ml/dp/B000CST4H0)
28. "This burns and stings the skin. I have now been left woth dark burns on my bikini line. I am now using tendsin to correct. Stay away from this." (excerpt, R8WEHMA9RHJMR, date not shown) — [Amazon UK Ingrow Go](https://www.amazon.co.uk/Skin-Doctors-Ingrow-Go-120ml/dp/B000CST4H0)
29. "I can't even begin to explain how self conscious i was of my legs before using this product. this has completely transformed my body and my mindset ab myself. i have the most sensitive skin ever and waxing gives me the worst reaction so im left with shaving." (Syd R., 14 Aug 2026) — [Bushbalm Mini Ingrown Hair Oil](https://bushbalm.com/products/vanilla-tangerine-mini-ingrown-hair-oil)
30. "I have been getting waxed for years, but have struggled to find an exfoliant that my skin worked well with. I have sensitive skin, and even sugar scrubs resulted in ingrown hairs. These pads worked within days" (Kyra B., fair, 25–34, waxing + shaving, 16 Aug 2026, incentivized) — [Bushbalm pads](https://bushbalm.com/products/radiant-reset-exfoliating-toner-pads)
31. "I started using one pad a day right after my monthly Brazilian wax. Specifically in the bikini line area since that is where I'm prone to get an ingrown hair bump." (Jessica B., deep skin tone, 35–44, 16 Dec 2025, incentivized) — [Bushbalm pads](https://bushbalm.com/products/radiant-reset-exfoliating-toner-pads)
32. "Religiously uses it from the day it arrived up to now (at least 3 weeks) and there is no change. AT ALL. … Should have known better than to listen to an influencer." (Anonymous, 15 Apr 2024, 1★) — [Bushbalm pads](https://bushbalm.com/products/radiant-reset-exfoliating-toner-pads)
33. "These are a must between waxes! I don't use them every day because they're kind of expensive … do not use less than 24-48 hrs after waxing because it will sting--a lot!" (ebednar, 20 Dec 2009) — [Sephora/Bazaarvoice Bliss P63308](https://api.bazaarvoice.com/data/reviews.json?Filter=ProductId:P63308&passkey=calXm2DyQVjcCy9agq85vmTJv5ELuuBCF2sdg4BnJzJus&apiversion=5.4&Locale=en_US&Limit=100)
34. "they are so small I need 4 pads to cover my legs. They are much too expensive to have to go through them this fast. I won't buy them again for this reason." (898900, 19 Feb 2010, 3★) — [Sephora/Bazaarvoice Bliss P63308](https://api.bazaarvoice.com/data/reviews.json?Filter=ProductId:P63308&passkey=calXm2DyQVjcCy9agq85vmTJv5ELuuBCF2sdg4BnJzJus&apiversion=5.4&Locale=en_US&Limit=100)

Additional adjacent quotes:
- "I have PCOS and a lot of hyperpigmentation around my bikini area and chest from shaving." (samiahhh, 10 Dec 2024) — [Sephora/Bazaarvoice Topicals P479355](https://api.bazaarvoice.com/data/reviews.json?Filter=ProductId:P479355&passkey=calXm2DyQVjcCy9agq85vmTJv5ELuuBCF2sdg4BnJzJus&apiversion=5.4&Locale=en_US&Limit=100)
- "I have very curly hair. . .everywhere. … my bikini area would always have the worst flare ups, and I would suffer from huge ingrown cysts and scarring as a result. I saw this product on TikTok" (Liliasxa, 9 Jun 2022) — same source

### Inferences
- Value is judged **per pad and per area**. Small pads that run out on legs, dry pads, and cutting pads in half are recurring signals in every pad brand from 2010 to 2026. Savenae's 50 pads for €18.90 (about €0.38 per pad) is an argument to lead with, and pad size and saturation must not disappoint.
- **"Does it work on *me*"** is the top objection: no effect was the largest 1–2★ theme, 25 of 62. Copy should set a realistic timeline ("consistency", "2–3 times a week"). Reviewers who succeed describe results "after 3 times", "within days" or "two weeks".
- **Stinging** is a salient fear even when it doesn't happen. Many 5★ reviews pre-empt it ("I was really worried they burn/sting"). Most stinging stories follow application on freshly shaved or waxed skin, so a usage rule (not right after waxing; follow the label) works as an objection-handler.
- Reviewers are mostly light-to-medium skin with brown or black hair. That profile plausibly resembles much of Bulgaria (an inference, not tested here). Dark-spot concern is meaningful even at fair and light tones (24–26%).

### Gaps
- Amazon US and UK pages yield only the aspect summaries and about 8 top reviews each, so full Amazon review bodies were not tallied. Amazon.de, lookfantastic, Completely Bare, Anthony pads and Bliss Bump Attendant (new name) reviews were not captured: lookfantastic redirected, and Firecrawl credits were low. The Bliss Sephora data is 2008–2015.
- The Sephora age field is nearly empty (24 of 408), so age comes only from Bushbalm.

## 3. Reddit and TikTok: discussion themes on ingrown-hair bikini pads

### Takeaway
Reddit threads could not be opened: Reddit returns 403 to curl, WebFetch and Firecrawl. Search-result excerpts show the same pattern as the reviews. Women ask "how do I shave down there without bumps". The community answer is **chemical exfoliation on a cotton pad (glycolic/salicylic, FAB pads, Stridex) plus technique changes, or laser as the final fix**. The cheap DIY substitute ("glycolic toner on a cotton pad") is the main competitive objection to branded pads. TikTok content mixes esthetician education about **bikini hyperpigmentation**, with high engagement, and occasional infection or sepsis scare stories.

### Cited Findings
Reddit (verbatim search-result excerpts; post dates were not visible in the excerpts):
- "FAB ingrown hair pads are my HG. Not from Sephora but after I use those 3x a week I'll moisturize with Fur ingrown hair oil. Works like a charm!" — [r/Sephora, "Looking for bikini line ingrown hair recommendations"](https://www.reddit.com/r/Sephora/comments/15jkysm/looking_for_bikini_line_ingrown_hair/)
- "Glycolic acid is the only thing that works for me. I use the cotton pads to wipe it all over the shaved area. It's really helped my red bumps ..." — [r/SkincareAddiction, "I am at my wit's end with ingrown hairs!"](https://www.reddit.com/r/SkincareAddiction/comments/1dstraa/hair_removal_i_am_at_my_wits_end_with_ingrown/)
- "pick up GLYCOLIC ACID TONER. this is the ultimate game changer i swear!! soak a cotton pad and wipe it thoroughly on the shaved areas when you ..." — [r/WomensHealth, "How can I get rid of razor bumps down there?"](https://www.reddit.com/r/WomensHealth/comments/1jegh9q/how_can_i_get_rid_of_razor_bumps_down_there/)
- "Stridex red box pads on the area right after shaving, and at bedtime 1-2 days afterward prevents all ingrowns for me." — [r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/bzr1xi/routine_help_best_options_to_preventtreat/)
- "The only thing that works (kind of) for me is shaving against the grain, glycolic acid wipes after shaving, and a little cetaphil moisturizer ..." — [r/SkincareAddiction, "razor bumps in 'that' area"](https://www.reddit.com/r/SkincareAddiction/comments/1j9icws/hair_removal_razor_bumps_in_that_area/)
- "There is a product on amazon called "First Aid Beauty- Ingrown Hair Pads" and do ..." — [r/TheGirlSurvivalGuide, "How do you shave down there without getting bumps"](https://www.reddit.com/r/TheGirlSurvivalGuide/comments/1h7z6vp/how_do_you_shave_down_there_without_getting_bumps/)
- "The only thing that worked for me was getting laser hair treatments. To avoid ingrown hairs, exfoliate with a dove body scrub or other scrub ..." — [r/AskWomen, "How do you maintain your hair free bikini line…"](https://www.reddit.com/r/AskWomen/comments/1rfw7v5/how_do_you_maintain_your_hair_free_bikini_line/)
- "I use Fur's oil and it's amazing. I get them horribly in my bikini line area and this helps minimize them greatly." — [r/Ulta, "Best product for ingrown hair?"](https://www.reddit.com/r/Ulta/comments/1c3hsyr/best_product_for_ingrown_hair/)
- "What worked for me: I stopped sleeping in panties, especially right after shaving." — [r/beauty, "Ingrown Hairs on Bikini Line"](https://www.reddit.com/r/beauty/comments/18o8u04/ingrown_hairs_on_bikini_line/)
- "I clean the area with alcohol after shaving, and yes it hurts like hell for a second but it passes quickly." — [r/AskWomen, "how do you prevent razor burn on your bikini line??"](https://www.reddit.com/r/AskWomen/comments/nu1bu3/okay_ladies_how_do_you_prevent_razor_burn_on_your/)
- Thread title showing an intimacy trigger: "hiding razor bumps before date?" — [r/Healthyhooha](https://www.reddit.com/r/Healthyhooha/comments/1b1u597/hiding_razor_bumps_before_date/)
- Stinging and safety worry, about Ingrow Go: "I have a slight worry that I could be damaging my skin, as this stuff stings like no other. Can anyone tell me if it's safe?" — [r/SkincareAddiction, "Question about ingrow go"](https://www.reddit.com/r/SkincareAddiction/comments/2vv9yn/question_about_ingrow_go/)
- Men's threads focus on technique: "I trim first, shave at the end of a warm shower, use a clean sharp razor with gentle shaving gel, and shave with the grain" — [r/AskMen](https://www.reddit.com/r/AskMen/comments/1qvnm8o/what_are_your_strategies_to_avoid_razor_burn_or/); "Try Clubman razor bump & ingrown hair treatment. It's cheap and works well for minor issues." — [r/wicked_edge](https://www.reddit.com/r/wicked_edge/comments/1ahbr7j/how_to_prevent_ingrown_hairs/). A search for men's pubic ingrown threads returned mostly women's threads (snapshot of 10 results).

TikTok and Instagram (comment threads not accessible):
- @7cristinarenee (ATL esthetician), "Tips for correcting bikini line ingrown hairs and hyperpigmentation", 87.3K likes, 426 comments; the video ID decodes to 24 Oct 2025 — [TikTok](https://www.tiktok.com/@7cristinarenee/video/7564914662077205815)
- TikTok discover page for FAB pads: "First Aid Beauty ingrown hair pads can soothe your bikini line and underarms for summer readiness", 716 likes — [TikTok discover](https://www.tiktok.com/discover/how-to-use-first-aid-beauty-ingrown-hair-pad)
- @makeupmaddie, "First Aid Beauty Ingrown Hair Pads: Bikini-Area Relief" ("The formula is safe for sensitive skin, which matters for delicate bikini-line skin where irritation is common"); ID decodes to 4 Jun 2026 — [TikTok](https://www.tiktok.com/@makeupmaddie/video/7647580405348060446)
- The #bikinilineingrownhair tag surfaces a scare story: "A content creator says shaving her bikini line left her fighting for her life after an infected ingrown hair developed into sepsis." — [TikTok tag](https://www.tiktok.com/tag/bikinilineingrownhair)
- FAB Instagram reel: "PSA: Ingrown Hair Pads aren't just for your bikini line. 👀 Anywhere you shave or wax = fair game. Legs, underarms, bikini line, ..." — [Instagram](https://www.instagram.com/reel/Da2ztz6lBBp/)
- Reviews name TikTok as a purchase trigger: "I saw this on TikTok and after just TWO DAYS…" (Amazon US, 2 Aug 2026) — [Amazon US FAB](https://www.amazon.com/First-Aid-Beauty-Ingrown-Hair/dp/B0GSWW3RFP); "Saw a girl on TikTok rave about it" (1 Aug 2022) — [Ulta FAB](https://www.ulta.com/p/ingrown-hair-pads-with-bha-aha-pimprod2057164). The backlash also exists: "Should have known better than to listen to an influencer." (15 Apr 2024) — [Bushbalm pads](https://bushbalm.com/products/radiant-reset-exfoliating-toner-pads)

### Inferences
- Reddit-literate buyers already know the mechanism (glycolic/salicylic on a pad). For them the objection is "why pay for a branded pad instead of toner plus cotton?" The answer is convenience (pre-soaked, "no extra cotton rounds", travel), the right strength for intimate skin, and price per pad.
- On TikTok, bikini **hyperpigmentation** content shows engagement in the tens of thousands of likes. Dark marks are an emotional hook even when the product's job is prevention. For Savenae this means "prevent new marks by preventing new ingrowns", which is a claim-safe framing (inference).

### Gaps
- No full Reddit threads, comment counts or post dates could be read (Reddit blocks every tool available here), and r/malegrooming and r/TwoXChromosomes produced no usable excerpts. TikTok comments could not be scraped (Firecrawl does not support TikTok). The themes above come from excerpts and titles, not comment-level coding.
- **r/Bulgaria**: no ingrown-hair threads found (consistent with the earlier BG file).

## 4. Bulgarian-language voice of the customer: new sources (adds to the earlier BG file)

### Takeaway
New BG material adds four things. (1) A **May 2017 bg-mamma page focused on legs**: red marks left after squeezing, gels that did nothing, laser seen as "the only salvation", and the explicit complaint that exfoliating the bikini triangle is "много трудно и неудобно", which is a direct pad-format JTBD. (2) A self-description of the **dark-hair segment** ("космите са черни… мъхнат тип"). (3) A **couple-buying** signal for PFB Vanish ("Двамата с мъжо ще ползваме"). (4) A **2025 thread** showing that painful underarm or groin lumps go to doctors and prescription creams (Фусидин, Далацин), outside the pad market. Bulgarian retail review pages (Framar, Notino, Sopharmacy) give star counts but no text VOC that could be retrieved.

### Cited Findings
**bg-mamma, "Борбата с подкожните косми #2", page 19 (posts dated 29–30 May 2017)** — [bg-mamma ?topic=673349.270](https://www.bg-mamma.com/?topic=673349.270)
- Mира, 29 May 2017 13:14: "Когато попитах дали това с краката ми е т.нар фоликулит, дерматоложката поклати глава и рече "не, това си е "враснал косъм", това му е наименованието"… каза, че това било свързано с епилатора, той променял растежа на косъма." / "Тези дни съм и в две студия за лазерна епилация да видим дали с лазер не може да се отстраняват тези червени петна."
- Iseult, 29 May 2017 14:15, on a pumice stone: "Аз я взех от ДМ, беше нещо за 1-2 лв. примерно. Но трябва много да се внимава, за да не разрани... Даже сега малко ми щипе, защото вчера се "драх"" / "И мен повече ме притесняват червените петна, които остават по краката..."
- Mира, 29 May 2017 14:23: "Аз не съм пробвала никакви кремове конкретно за останалите петна от минали стискания, доколкото разбрах това било едва ли не непреодолимо"
- Mира, 29 May 2017 14:41: "За нищо не съм била толкова постоянна, както за краката ми. Основен приоритет ми е подобряването им. Просто не знам с какво да пробвам, че да има ефект."
- vici75, 29 May 2017 14:45: "Аз поръчах този PFB VANISH POST WAXING SHAVING BUMP SERUM ROLL. Двамата с мъжо ще ползваме и ще ви дам отзиви"
- Йолка, 29 May 2017 19:27: "Аз си купих един гел за крака уж против подкожни, с успокояващо действие, отлични оценки онлайн, но при мен няма ефект, вече втори месец мажа всяка вечер, без да пропускам. Онзи ден като си погледнах краката и се отчаях отново - от коленете нагоре са ужасни"
- Mира, 29 May 2017 20:35: "от всички прехвалени и подействали на някого мазила при мен ефект нулев." / "Чудя се лазер дали би повлиял качествено на пигментация."
- Йолка, 29 May 2017 21:36: "От вътрешната страна на бедрата е още по-зле. Аз мисля, че лазерната епилация е единственото спасение за дълбоките подкожни косми."
- aya_2012, 30 May 2017 08:17: "Ексфолирам краката си с ръкавица 1 или 2 пъти през седмицата и нямам такъв проблем… На триъгълника направо ми се образуват големи пъпки и незнам там какво да предприема." Then at 13:10, asked why she doesn't exfoliate there: "веднъж пробвах, но е много трудно и неудобно."

**bg-mamma, same thread, page 4.** These excerpts did not appear in the earlier file. The earlier notes date this page's posts to Jan–Feb 2013; the exact post dates were not visible in the excerpt — [bg-mamma ?topic=673349.45](https://www.bg-mamma.com/?topic=673349.45)
- "И аз имам проблем с врасналите косъмчета. Кожата ми е мъничко по-тъмна, а космите са черни и като цяло съм мъхнат тип."
- "По принцип съм много предразположена към врасналите косми… навсякъде ми излизат - на краката, мишниците, триъгълник." / "На краката буквално всеки косъм ми излизаше враснат - и на бедра и под коленете."
- "По съшия начин се получи и с интимната зона - в никакъв случай не се скубя там, защото после няма изчистване на подкожните с месеци."

**bg-mamma, "Борбата с подкожните косми" (first thread), word of mouth for Ingrow Go (date not visible in excerpt)** — [bg-mamma ?topic=193559.255](https://www.bg-mamma.com/?topic=193559.255)
- "Намене ми препоръчаха следната марка:Skin Doctors InGrow Go 125ml.Жената която ми го препоръча каза че е много доволна от тази марка."

**bg-mamma, "Фоликулит" (posts dated 5–6 Mar 2025, the newest organic BG thread found)** — [bg-mamma ?topic=1750810](https://www.bg-mamma.com/?topic=1750810)
- Блатно кокиче, 5 Mar 2025: "…Накрая заключи, че това е фоликулит - от бръсненето под мишницата. Каза нищо да не правя, тъй като не ме боли… Преди години имах подобен проблем - пих Далацин и отшумя."
- magito, 6 Mar 2025: "Аз съм имала подобен проблем но, на сгъвката между интимните части. При мен се появяваше периодично подпухнало топче като в един от случаите се влоши до степен, при която се наложи лека хирургична интервенция и дренаж… Фусидин крем при по-леки случаи винаги ми помага. Иначе аз бих Ви препоръчала да си запазите час при добър кожен лекар."

**Other BG**
- CosmopolisBG forum, laser thread (date not visible): "Пък и окосмяването ми е предимно русо, тоест няма да има голям ефект... Ами 3 месеца докато ходех нямах въобще подкожни косми, ама сега ако се епилирам пак ..." — [cosmopolisbg.com](http://cosmopolisbg.com/forum/viewtopic.php?f=16&t=193&p=104879)
- Framar.bg, Skin Doctors Ingrow Go 120 ml: the "comments" section shows 0 text comments despite 4.2/5 from 86 ratings (checked 6 Oct 2026). The product text says "За поддържане: Мъжете го използват ежедневно след бръснене, а жените няколко пъти седмично." — [Framar](https://apteka.framar.bg/30029040/%D1%81%D0%BA%D0%B8%D0%BD-%D0%B4%D0%BE%D0%BA%D1%82%D0%BE%D1%80%D1%81-ingrow-go-%D0%BB%D0%BE%D1%81%D0%B8%D0%BE%D0%BD-120-%D0%BC%D0%BB)
- Ingrow Go is also listed at ozone.bg and drugstore.bg ("лосион за третиране на подкожни, растящи навътре косми") — [ozone.bg](https://www.ozone.bg/product/skin-doctors-losion-protiv-podkozhni-kosmi-ingrow-go-120-ml/); [drugstore.bg](https://drugstore.bg/%D1%81%D0%BA%D0%B8%D0%BD-%D0%B4%D0%BE%D0%BA%D1%82%D0%BE%D1%80%D1%81-%D0%BB%D0%BE%D1%81%D0%B8%D0%BE%D0%BD-%D0%BF%D1%80%D0%B8-%D1%80%D0%B0%D1%81%D1%82%D1%8F%D1%89%D0%B8-%D0%BF%D0%BE%D0%B4%D0%BA%D0%BE%D0%B6%D0%BD%D0%BE-%D0%BA%D0%BE%D1%81%D0%BC%D0%B8-120-%D0%BC%D0%BB-skin-doctors-ingrow-go-8098)
- PFB Vanish BG positioning: "Pfd Vanish – най-доброто средство за отстраняване и превенция на врастнали косми! Само за 48 часа…" — [Pfb Vanish Facebook](https://www.facebook.com/vanishbg/); vanishbg.com: "Рол-он серумът pfb Vanish успешно премахва врастналите косми, хидратира кожата и успокоява раздразненията." — [vanishbg.com](https://vanishbg.com/)

### Inferences
- **New BG words for copy** (in addition to the earlier file's vocabulary): "щипе" (the BG word for the stinging objection; use as "не щипе"); "червените петна, които остават по краката"; "петна от минали стискания"; "от коленете нагоре"; "вътрешната страна на бедрата"; "големи пъпки на триъгълника"; "мъхнат тип"; "космите са черни"; "ефект нулев"; "прехвалени мазила"; "единственото спасение" (said of laser); "много трудно и неудобно" (said of exfoliating the bikini area).
- **A BG pad-format JTBD stated in her own words**: a mitt or pumice works on legs, but on the bikini triangle it is "много трудно и неудобно" and pumice "щипе / разранява". A pre-soaked pad answers exactly this: "ексфолиране там, където ръкавицата не става".
- **The BG dark-hair segment** has a voice ("космите са черни", "мъхнат тип", "кожата ми е мъничко по-тъмна"). It lines up with the Bushbalm finding that dark-spot concern rises with darker tone. Copy can name "тъмни, плътни косъмчета" without stigma.
- **Couples** buy together (PFB Vanish "Двамата с мъжо"), echoing the US partner-sharing pattern. A "за двама" or "и за него" message may lift the average order value via the duo or 2-packs.
- **Boundary**: painful lumps ("подпухнало топче", "дренаж", "фоликулит") are medical. Ads should avoid implying a pad treats these, and should say "при болезнени, подути… потърси лекар".

### Gaps
- Still no independent 2024–2026 BG product-review VOC: Notino.bg and Sopharmacy.bg returned 403 to direct fetch, and Firecrawl credits were too low to scrape them. Framar has ratings only. eMAG was captcha-blocked in the earlier file.
- No BG TikTok comment threads, public Facebook group posts or BG-language Reddit content could be accessed.
- Exact post dates for the bg-mamma p.4 and 193559 excerpts are unknown.

## 5. Identity and emotional layer: shame, intimacy, self-care ritual, smooth-skin aesthetic, men's confidence — what language triggers purchase?

### Takeaway
The purchase moment is driven by **anticipated exposure**: summer, bikini, beach or a trip; sleeveless clothes; a date or partner noticing. It is reinforced by **shame and hiding** language ("insecure", "self-conscious", "hide", "TMI", "срам"). After purchase the frame shifts to **relief, pride and ritual** ("staple", "holy grail", "my routine", "my husband even noticed"). Men rarely speak for themselves. Their confidence story is told by a female partner, and men's own conversation is about technique and the face or neck.

### Cited Findings
- Exposure triggers in text: summer/vacation/beach/pool/swim/trip mentioned in 45 of 577 FAB reviews (7.8%), 120 of 3,000 Bushbalm reviews, and 65 of 1,097 Topicals reviews — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320); [Bushbalm feed](https://api.okendo.io/v1/stores/cb31d0ec-c21a-406d-8287-1d91c3b18f7c/reviews?limit=100&orderBy=date%20desc); [Sephora/Bazaarvoice P479355](https://api.bazaarvoice.com/data/reviews.json?Filter=ProductId:P479355&passkey=calXm2DyQVjcCy9agq85vmTJv5ELuuBCF2sdg4BnJzJus&apiversion=5.4&Locale=en_US&Limit=100)
- Shame and confidence words (confident, embarrass, self-conscious, insecure, hide, ugly, gross) appear in 24 of 577 FAB reviews (4.2%) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
- "felt so insecure when summer came around when it was time to get in a bikini … it is so worthwhile for me to just feel so much for confident in myself." (23 Jul 2025) — [Amazon UK Ingrow Go](https://www.amazon.co.uk/Skin-Doctors-Ingrow-Go-120ml/dp/B000CST4H0)
- "before bushbalm I was so self conscious of my under arms, not to mention uncomfortable with the red bumps on my skin." (Katie T., 35–44, 13 Aug 2026) — [Bushbalm feed](https://api.okendo.io/v1/stores/cb31d0ec-c21a-406d-8287-1d91c3b18f7c/reviews?limit=100&orderBy=date%20desc)
- "this has completely transformed my body and my mindset ab myself." (Syd R., 14 Aug 2026) — [Bushbalm Mini Ingrown Hair Oil](https://bushbalm.com/products/vanilla-tangerine-mini-ingrown-hair-oil)
- Partner as validator: "I am thrilled and my husband even noticed." (27 Mar 2026) — [Ulta FAB](https://www.ulta.com/p/ingrown-hair-pads-with-bha-aha-pimprod2057164); "My husband notices a huge difference in my skin. It looks and feels smooth and the skin/ scars and slowing fading away." (Sonja D., 10 Aug 2026) — [Bushbalm Dark Spot Exfoliant](https://bushbalm.com/products/bermuda-dark-spot-exfoliant)
- Pre-date anxiety: thread title "hiding razor bumps before date?" — [r/Healthyhooha](https://www.reddit.com/r/Healthyhooha/comments/1b1u597/hiding_razor_bumps_before_date/)
- Taboo marker: reviewers preface with "TMI" or "Maybe TMI but I use them on my “bikini line” (only up top of course)" (jay2326, 7 Jun 2022) and "WARNING TMI- I get A LOT of ingrown hairs" (Amriette, 8 Aug 2022) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
- Ritual and identity words: "holy grail / HG / game changer / life saver / obsessed / repurchase / staple" appear in 109 of 577 FAB reviews (18.9%) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320). Amazon groups 43 mentions under "Life-saving" (40 positive) — [Amazon US FAB](https://www.amazon.com/First-Aid-Beauty-Ingrown-Hair/dp/B0GSWW3RFP). Example: "A routine staple." (rwh1203, 12 Apr 2026) — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
- Negative identity hit when a product fails: "It has made me so insecure" (Chiam, 21 Jul 2025, 1★, after a breakout "down there") — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320)
- BG persistence and priority: "За нищо не съм била толкова постоянна, както за краката ми. Основен приоритет ми е подобряването им." (29 May 2017) — [bg-mamma](https://www.bg-mamma.com/?topic=673349.270). The earlier BG file documents "Малко ме е срам, но да попитам", "По цяло лято ходех с дълъг панталон" and "не ми е комфортно през летните месеци да ходя с къси панталонки" — [earlier notes / bg-mamma](https://www.bg-mamma.com/?topic=522144)
- Men's voice is mostly second-hand: 0 of 577 FAB reviews self-identify as male, while 16 mention a husband, boyfriend or fiancé. In the men's-brand reviews (Anthony + Jack Black), 39 of 259 mention buying for or sharing with a male partner — [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320); [Sephora/Bazaarvoice P170545](https://api.bazaarvoice.com/data/reviews.json?Filter=ProductId:P170545&passkey=calXm2DyQVjcCy9agq85vmTJv5ELuuBCF2sdg4BnJzJus&apiversion=5.4&Locale=en_US&Limit=100)

### Inferences
- **The highest-converting emotional sequence** (inference): anticipated exposure (summer, a trip, a date) → "I've tried everything" → simple ritual (one pad, one swipe) → "I stopped hiding" / "he noticed" → "staple". This matches the BG competitor hooks already live (Deroli: "на плажа, в интимни моменти"). Because of Meta's negative self-perception rules (earlier file, question 6), the **after-state** should carry the copy, not the shame. Examples: "кожа, която не криеш", "гладка бикини линия и след бръснене", "ритуал от 30 секунди", "без чоплене".
- Claim-safe Bulgarian equivalents of reviewer language: "най-накрая нещо, което помага" (finally something that helps), "без червени точици след бръснене", "не щипе" (only if tested), "между две кола маски", "за крака, подмишници и бикини линия", "един тампон – една стъпка" (already on the Savenae page).
- **"Clean girl" / smooth-skin aesthetic**: in the reviews it appears as "smooth", "clear", "soft", "my skin has never looked better". It is an aspiration layer, not the trigger. The trigger remains a concrete event (summer, a date, a wax appointment).
- **Men's confidence**: in the data, men's identity language is absent. The usable angle is the woman as gatekeeper ("и той ще го ползва") or couple use, not a standalone male ad, especially since Savenae excludes face and neck.

### Gaps
- No quantified link was found between emotional framing and conversion (no ad test data). The rankings are frequencies in reviews, not causal.
- BG-specific 2024–2026 emotional language from real customers was not found beyond seller-curated reviews (see the earlier file).

## 6. Which segment is most likely to buy a ~€20 product online via a Meta ad in Bulgaria, and which goes to the pharmacy or laser instead? (reasoned inference)

### Takeaway
**Inference (clearly labelled):** the best Meta-ad buyer is **Segment A (and C): a woman aged 25–44 who shaves her bikini line and underarms at home**. Her problem is recurring, mild-to-moderate and embarrassing to discuss. She has already "tried everything", is not ready to pay for laser, and values discreet COD delivery. **Segment B (post-wax, younger)** is the second Meta target, and also reachable via salons. **Pharmacy buyers** skew to brand-searchers (Ingrow Go, PFB Vanish), men (face and neck), and people with painful lumps sent there by a doctor. **Laser** draws long-sufferers with budget, and BG clinics now advertise intimate laser at about the pad's price per session.

### Cited Findings
- Segment A/C size and profile: shaving 59%, bikini line 86%, underarms 46%, ages 25–44 = 57% of Bushbalm reviewers who answered; sensitive skin 55% — [Bushbalm feed](https://api.okendo.io/v1/stores/cb31d0ec-c21a-406d-8287-1d91c3b18f7c/reviews?limit=100&orderBy=date%20desc)
- BG DTC rivals already sell this exact job on Meta at €19.90–€20.90, with bikini-zone, shame and 7-day hooks. **G Point advertises laser "Пълен интим - 24 €"** (one creative across 33 ads) — earlier file: [ads_and_customer_voice_bg.md, Q1/Q3]; [Deroli ad](https://www.facebook.com/ads/library/?id=1420963646502602); [G Point ad](https://www.facebook.com/ads/library/?id=1328683552710904)
- Savenae's offer has the features that lower the online-purchase barrier: "Плащане при доставка", "Безплатна доставка", "Гаранция за връщане на парите", "Изпраща се от България" — [savenae.com](https://savenae.com/products/savenae-smooth-reset-pads)
- Price sensitivity is real among pad users: Bliss reviewers mention price or value in 206 of 776 reviews; price/value is the third-largest 1–2★ theme for FAB (16 of 62); Amazon value-for-money is 75 positive vs 66 negative; reviewers cut pads in half (Bliss 20, FAB 5) — [Sephora/Bazaarvoice P63308](https://api.bazaarvoice.com/data/reviews.json?Filter=ProductId:P63308&passkey=calXm2DyQVjcCy9agq85vmTJv5ELuuBCF2sdg4BnJzJus&apiversion=5.4&Locale=en_US&Limit=100); [Sephora FAB](https://www.sephora.com/product/first-aid-beauty-ingrown-hair-pads-with-bha-aha-P479320); [Amazon US FAB](https://www.amazon.com/First-Aid-Beauty-Ingrown-Hair/dp/B0GSWW3RFP)
- Laser as the perceived end-game in BG ("лазерната епилация е единственото спасение за дълбоките подкожни косми", 29 May 2017), and in the US ("definitely wants laser hair removal once I have enough money", 24 Mar 2026) — [bg-mamma](https://www.bg-mamma.com/?topic=673349.270); [Bushbalm Shave Jelly](https://bushbalm.com/products/shave-jelly-watermelon-sugar). Lasering is reported by 6.9% of Bushbalm reviewers, so laser users still buy aftercare — [Bushbalm feed](https://api.okendo.io/v1/stores/cb31d0ec-c21a-406d-8287-1d91c3b18f7c/reviews?limit=100&orderBy=date%20desc)
- Pharmacy and doctor route for painful or inflamed cases: "фоликулит… Далацин", "Фусидин крем… запазите час при добър кожен лекар" (Mar 2025) — [bg-mamma](https://www.bg-mamma.com/?topic=1750810). Ingrow Go has a pharmacy footprint (Framar, 86 ratings; drugstore.bg; ozone.bg) and BG word of mouth ("препоръчаха… Skin Doctors InGrow Go") — [Framar](https://apteka.framar.bg/30029040/%D1%81%D0%BA%D0%B8%D0%BD-%D0%B4%D0%BE%D0%BA%D1%82%D0%BE%D1%80%D1%81-ingrow-go-%D0%BB%D0%BE%D1%81%D0%B8%D0%BE%D0%BD-120-%D0%BC%D0%BB); [bg-mamma](https://www.bg-mamma.com/?topic=193559.255). Framar's own copy targets men's daily post-shave use ("Мъжете го използват ежедневно след бръснене") — [Framar](https://apteka.framar.bg/30029040/%D1%81%D0%BA%D0%B8%D0%BD-%D0%B4%D0%BE%D0%BA%D1%82%D0%BE%D1%80%D1%81-ingrow-go-%D0%BB%D0%BE%D1%81%D0%B8%D0%BE%D0%BD-120-%D0%BC%D0%BB)
- Post-wax clients follow salon and esthetician advice (esthetician/waxer mentioned in 17 Bliss and 25 Bushbalm reviews), and BG waxers skew young (18–24 waxing 58% vs shaving 51% in the proxy) — [Sephora/Bazaarvoice P63308](https://api.bazaarvoice.com/data/reviews.json?Filter=ProductId:P63308&passkey=calXm2DyQVjcCy9agq85vmTJv5ELuuBCF2sdg4BnJzJus&apiversion=5.4&Locale=en_US&Limit=100); [Bushbalm feed](https://api.okendo.io/v1/stores/cb31d0ec-c21a-406d-8287-1d91c3b18f7c/reviews?limit=100&orderBy=date%20desc)

### Inferences
**Channel propensity by segment (inference, not measured)**

| Segment | Meta-ad €20 online | Pharmacy | Laser / salon | Reasoning |
|---|---|---|---|---|
| A. Home bikini shaver, 25–44 | **High** | Medium | Low–medium (aspires to it) | Recurring and embarrassing (prefers not to ask a pharmacist); impulse price; COD; competitors prove the channel |
| C. Underarm shaver | High (as add-on to A) | Medium | Low | Same person as A in about half of cases |
| B. Post-wax, 18–34 | **Medium–high** | Low | High (already in salon) | Also reachable via esthetician partnerships; must handle "wait 24–48 h after waxing" |
| E. Legs / strawberry legs | Medium | Medium | Low | Pad size and count is the objection; 50 pads helps |
| D. Dark marks / scars | Medium (high emotion) | Medium–high (searches for "избелващ" creams) | Medium (asks whether laser fixes pigmentation) | Savenae makes no brightening claim, so the creative must promise "fewer new bumps = fewer new marks" |
| G. Between-laser / laser aspirants | Medium | Low | Already there | Message: "докато стигнеш до лазер / между сесиите" (check the laser clinic's aftercare rules) |
| I. Men | Low via own ads; medium via partner | **High** (face/neck lotions, Ingrow Go) | Low–medium (men's intimate laser offers exist) | Savenae excludes face and neck; reach through women and couples |
| J. Painful lumps / folliculitis | Low | High (doctor → Fusidin) | — | Not a target; add a safety disclaimer |

- **Best initial ICP for Savenae on Meta in BG** (inference): a woman aged 25–44 who shaves her bikini line and underarms at home, has light-to-olive skin and dark hair, and says her skin is sensitive. She has tried scrubs, mitts and "прехвалени мазила", is saving for or putting off laser, and buys before summer or a trip, or after a bad flare-up. She is reassured by COD, a money-back guarantee, "не щипе" and a clear price per pad. Secondary: women aged 18–30 who get waxed (post-wax care).
- **Biggest threats to conversion** (inference): (1) intro laser offers at ~€24 per session reframe a €18.90 pad as "temporary"; (2) "nothing works on me" fatigue after the many failures documented in BG forums; (3) DIY substitutes (pumice, coffee grounds, glycolic toner on cotton); (4) competitors' bolder claims (dark-spot lightening, "7 days"), which Savenae does not make.

### Gaps
- No BG conversion, CTR or channel-share data exists for these segments; the table is reasoned inference. No BG survey data exists on where women buy intimate-care cosmetics (pharmacy vs online vs drogerie). See the parallel file `bg_demographics_behavior.md` for demographics.
- No data was found on the share of BG men who groom their pubic area, or on willingness to pay for male intimate grooming care.
