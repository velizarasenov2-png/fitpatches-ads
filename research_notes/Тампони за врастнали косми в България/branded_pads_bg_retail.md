# Branded ingrown-hair pads (тампони/подложки/дискове/кърпички/падове) and close substitutes in Bulgarian retail, October 2026

Scope and method: I searched in Bulgarian and English (Firecrawl Google-style search with `site:` operators), scraped retailer search and product pages, and pulled schema.org/JSON-LD price data with curl where a site allowed it. Research date: 6 Oct 2026. Prices are copied exactly as shown, mostly in EUR (Bulgaria uses the euro since 1 Jan 2026). A few pages still show BGN next to EUR.

Access limits:
- eMAG.bg returned a CAPTCHA (HTTP 511) to every scraper, so all eMAG data comes from Google snippets.
- SOpharmacy, Douglas.bg, Galen, BayShop and Ubuy blocked curl (403).
- Ubuy.bg prices load dynamically and could not be read even with a headless scrape.
- Mareshki and Benu searches failed (connection reset / HTTP 500), and their internal search pages could not be read.

## 1. Which ingrown-hair PAD products can a Bulgarian shopper actually buy from a Bulgarian retailer today?

### Takeaway
No dedicated ingrown-hair or razor-bump pad is in stock today at any mainstream Bulgarian retailer I could check: Notino, Douglas, Makeup.bg, Framar, Ozone, SOpharmacy/Galen/Lilly via search, and eMAG via snippets. The only such pad listed by a mainstream BG retailer is **First Aid Beauty Ingrown Hair Pads (28 pcs) on notino.bg, and it is out of stock with 0 reviews**. Bulgarians can still get these pads in two ways. One is cross-border marketplaces: Ubuy.bg lists FAB 60, Bushbalm Radiant Reset, Waxness Dr. Bump, Pure Ease, Inlon and others, with prices not readable. The other is EU/UK retailers that ship to BG, such as Lookfantastic, which sells FAB 28/60 pads in GBP. Otherwise shoppers end up with face pads used off-label (Nip+Fab Glycolic Fix, COSRX, Neogen on Notino) or with liquids: roll-ons, lotions and serums.

### Cited Findings

**A. Dedicated ingrown-hair / razor-bump PADS, as listed to Bulgarian shoppers**

| Brand / product | Pads | Actives | Price as shown | Where / status | Reviews | Source |
|---|---|---|---|---|---|---|
| First Aid Beauty Ingrown Hair Pads ("ексфолиращи възглавнички за враснали косъмчета", form "кърпички") | 28 бр. | Glycolic acid + salicylic acid, witch hazel, licorice, feverfew, aloe, bisabolol | **No price shown, "Продуктът в момента не е в наличност"** (code FAI04071) | notino.bg, **OUT OF STOCK** | 0 | [Notino FAB](https://www.notino.bg/first-aid-beauty/ingrown-hair-pads-eksfolirasshi-vzglavnichki/p-16296840/) |
| Same FAB pads: the only real pad hit in Notino BG's "ingrown" (3 results) and "Врастнали косми" (16 results) searches | n/a | n/a | n/a | out of stock | n/a | [Notino search "ingrown"](https://www.notino.bg/search.asp?exps=ingrown); [Notino search "Врастнали косми"](https://www.notino.bg/search.asp?exps=%D0%92%D1%80%D0%B0%D1%81%D1%82%D0%BD%D0%B0%D0%BB%D0%B8%20%D0%BA%D0%BE%D1%81%D0%BC%D0%B8) |
| First Aid Beauty Ingrown Hair Pads with BHA & AHA | 60 ct | BHA + AHA (glycolic/salicylic) | price not readable (loaded dynamically) | Ubuy.bg (cross-border import; product image from Walmart, i.e. US store) | n/a | [Ubuy.bg FAB 60](https://www.ubuy.bg/en/product/M0OHFWOVO-first-aid-beauty-ingrown-hair-pads-with-bha-aha-daily-treatment-prevents-razor-bumps-ingrown-hairs-and-soothes-irritation-60-pads); also a UK-store listing [Ubuy.bg FAB 60 (UK)](https://www.ubuy.bg/en/productuk/U0C21X59A-first-aid-beauty-ingrown-hair-pads-60-pads) |
| First Aid Beauty Smooth Skin Body Bestsellers Set (KP Bump Eraser + Ingrown Hair Pads 28 ct) | 28 ct in set | AHA pads | price not readable | Ubuy.bg | n/a | [Ubuy.bg FAB set](https://www.ubuy.bg/bg/product/TY5DMAZJA-first-aid-beauty-smooth-skin-body-bestsellers-set-kp-bump-eraser-scrub-ingrown-hair-pads-exfoliate-keratosis-pilaris-help-prevent-razor) |
| Bushbalm Radiant Reset Exfoliating Ingrown Hair Pads ("Radiant Reset Exfoliating Toner Pads") | 30 large pads | Tranexamic acid + AHAs + BHAs, alcohol-free | Ubuy: price not readable. Brand US site: **USD 19.00** | Ubuy.bg (Amazon ASIN B0CVS7JQVT); or direct from Bushbalm (ships to EU) | n/a | [Ubuy.bg Bushbalm](https://www.ubuy.bg/en/product/IRACP9W28-radiant-reset-exfoliating-toner-pads-enhanced-with-bha-aha-to-brighten-dark-spots-soothe-bikini-area-ingrown-hairs-razor-bumps-30); [Bushbalm product](https://bushbalm.com/products/radiant-reset-exfoliating-toner-pads) |
| Waxness Dr. Bump Enzymatic Ingrown Hair Pads 2 Steps (Peeling & Brightening) | 30 pcs | Peptides, salicylic acid, ginkgo biloba, green tea (enzymatic) | Ubuy: price not readable. Brand site lists **$24.00** | Ubuy.bg only. Not found at any BG salon supplier | 1 review on brand site | [Ubuy.bg Waxness](https://www.ubuy.bg/bg/product/FNKRQPVWO-waxness-dr-bump-enzymatic-ingrown-hair-pads-2-steps-peeling-brightening-30-pcs); [Waxness](https://waxness.com/44-post-waxing-intimate-care); [Beautyways ingredients](https://beautyways.com/home/17845-waxness-dr-bump-enzymatic-ingrown-hair-peeling-pads-2-steps-peeling-brightening-30-pads.html) |
| Pure Ease Ingrown Hair Treatment & Exfoliating Pads | 50 pre-soaked wipes | not captured | n/a | Ubuy.bg (US store) | n/a | [Ubuy.bg Pure Ease](https://www.ubuy.bg/bg/product/IX57OYTAM-ingrown-hair-treatment-exfoliating-pads-50-pre-soaked-wipes-for-razor-bumps-treatment-for-women-skin-smoothing-formula-for-face-neck-underarms) |
| Inlon Treatment Hair Pad with AHA+BHA for Bikini Area | 50 pads | AHA + BHA | n/a | Ubuy.bg (JP store) | n/a | [Ubuy.bg Inlon](https://www.ubuy.bg/en/productjp/TB00U3V3A-inlon-treatment-hair-pad-with-aha-bha-for-bikini-area-includes-razor-bumps-underarms-exfoliating-face-neck-50-pads-built-in-hair-serum) |
| Generic "Ingrown Hair Pads 60 Count, Dual-Texture, Salicylic & Glycolic" | 60 | salicylic + glycolic | n/a | Ubuy.bg | 0 | [Ubuy.bg generic 60](https://www.ubuy.bg/bg/productuk/U14YMKLVG-ingrown-hair-pads-60-count) |
| Generic "Ingrown Hair Pads with BHA + AHA – Aftershave… Underarms & Bikini – Compostable" | n/a | BHA + AHA | n/a | Ubuy.bg | n/a | [Ubuy.bg BHA+AHA pads](https://www.ubuy.bg/en/productuk/U03THNGGK-ingrown-hair-pads-with-bha) |
| Yimimde "Ingrown Hair Treatment Pads for Razor Bumps & Bikini Line" | n/a | n/a | n/a | Ubuy.bg brand page | n/a | [Ubuy.bg Yimimde](https://www.ubuy.bg/bg/brand/yimimde) |
| Razor Bump Treatment for Bikini Area Roll-On 3.5 oz **with Ingrown Hair Treatment Pads** | roll-on + pads | n/a | n/a | Ubuy.bg | n/a | [Ubuy.bg roll-on + pads](https://www.ubuy.bg/bg/product/LUDW76UOI-razor-bump-treatment-for-bikini-area-roll-on-3-5-oz-with-ingrown-hair-treatment-pads) |
| We Do Derm Acne Wipes RX (salicylic + glycolic pads, marketed also for ingrown hair) | n/a | salicylic + glycolic | n/a | Ubuy.bg | n/a | [Ubuy.bg We Do Derm](https://www.ubuy.bg/bg/product/4LZ18UQ2G-we-do-derm-acne-wipes-rx-correction-pads-for-face-chest-and-back) |

**B. Off-label exfoliating face pads on BG retailers (not marketed for ingrown hairs, but the same format and actives)**

| Product | Pads | Price | Rating | Source |
|---|---|---|---|---|
| NIP+FAB Glycolic Fix почистващи тампони | 60 бр. | **16,90 €** | 4,0 (1) | [Notino "nip fab" search (34 products)](https://www.notino.bg/search.asp?exps=nip%20fab) |
| NIP+FAB Vitamin C Fix почистващи тампони | 60 бр. | 14,90 € | n/a | same |
| Neogen Dermalogy Bio-Peel+ Gauze Peeling (Wine / Green Tea / Lemon) | 30 / 8 / 1 бр. | from 1,70 € | Wine 4,9 (10); Green Tea 5,0 (3); Lemon 5,0 (1) | [Notino "peel pads"](https://www.notino.bg/search.asp?exps=peel%20pads) |
| Peter Thomas Roth Even Smoother Glycolic Retinol Resurfacing Peel Pads | n/a | no price | **out of stock** | same |
| Cosrx One Step Green Hero Calming pads | 70 бр. | 18,90 € | n/a | [Notino Cosrx search snippet](https://www.notino.bg/search.asp?exps=cosrx%20good%20morning) |
| Cosrx One Step Original Tone Clarifying Moisture Pad | 100 pc | listed on notino.bg; €24.90 on notino.ie | n/a | [Notino.bg Cosrx pad](https://www.notino.bg/cosrx/one-step-original-tone-clarifying-moisture-pad-tonizirasshi-vzglavnichki-s-khidratirassh-efekt/); [Notino.ie](https://www.notino.ie/cosrx/one-step-original-tone-clarifying-moisture-pad-toner-pads-with-moisturising-effect/) |
| Dr. Althea StretchFit Calming Pad (the only hit for "dr. dennis gross" on Notino BG) | 50 бр. | 14,70 € | n/a | [Notino "dr. dennis gross"](https://www.notino.bg/search.asp?exps=dr.%20dennis%20gross) |
| Plantifique exfoliating pads with AHA, BHA, PHA and CICA | 60 бр. | price not captured | n/a | eMAG snippet: [eMAG](https://www.emag.bg/zaharen-skrab-za-tjalo-noni-care-200-ml-s-aha-hidratirasht-citrusov-aromat-fertes-5903240869336/pd/D57RG23BM/) |

**C. Other Bulgarian retailers checked: no ingrown-hair pads found**
- Framar's dedicated category "Козметични продукти за врастнали косми" lists only 5 products and no pads: PFB Vanish x2, Е-Лек Вранас ointment x2, Skin Doctors Ingrow Go. — [Framar category](https://apteka.framar.bg/%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B8/%D0%BA%D0%BE%D0%B7%D0%BC%D0%B5%D1%82%D0%B8%D1%87%D0%BD%D0%B8-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B8-%D0%B2%D1%80%D0%B0%D1%81%D1%82%D0%BD%D0%B0%D0%BB%D0%B8-%D0%BA%D0%BE%D1%81%D0%BC%D0%B8)
- Douglas.bg: a `site:` search for ingrown/врастнали/враснали returned only guides and after-shave products (Kiehl's, Payot, Eisenberg, Acqua di Parma), no pads. — [Douglas guide](https://douglas.bg/naruchnik-za-grizha-na-kozhata-9919/obezkosmyavane/vrasnali-kosmi/99191602); [Douglas Kiehl's](https://douglas.bg/kiehls-ultimate-razor-burn-bump-relief-88638)
- Makeup.bg: a `site:` search for "врастнали косми" returned serums, oils, sprays, after-shaves and tools, no pads. A search for Bushbalm/First Aid Beauty/Bliss/Fur on makeup.bg returned zero results. — [Makeup.bg Fler](https://makeup.bg/product/928613/); [Makeup.bg Acorelle](https://makeup.bg/product/582237/)
- Ozone.bg: a `site:` search returned PFB Vanish, Skin Doctors, a GIGI intimate peel, SVR Xerial, Cocosolis mitt and tweezers, no pads. — [Ozone PFB](https://www.ozone.bg/product/pfb-vanish-rol-on-serum-za-premahvane-i-preventsiya-na-vrastnali-kosmi-93-gr/)
- SOpharmacy, Benu, Subra, Mareshki: a combined `site:` search returned only Biotrade Acne Out lotion, SVR, Nuxe Men gel and CeraVe SA, no pads. — [SOpharmacy Acne Out](https://sopharmacy.bg/bg/product/000000000010006109); [Subra Acne Out](https://subra.bg/bg/kozmetika/kozmetika-za-lice/biotrade-acne-out-aktiven-losion-60ml/4/1146)
- dm Bulgaria, Lilly Drogerie, Galen, ePharma: a `site:` search found no ingrown pads. It did find Balea bleaching cream, Gillette Venus Pubic razor, SVR Xerial 30, Fluff salicylic body lotion and Acne Out. — [Lilly Gillette Venus](https://lillydrogerie.bg/gillette-venus-damska-sistema-za-br-snene-satin-care-1-br-1-nozhche-544620); [Galen Fluff](https://galen.bg/flaff-losion-za-tyalo-izglazhdasht-sas-salitsilova-kiselina-150ml)
- eMAG.bg: a `site:` search for "тампони OR кърпички OR падове врастнали косми" returned no branded ingrown pads. Hits were generic Chinese roll-ons/serums (Jaysuing etc.), Alveola/Italwax/Depilflax/Thalgo lotions, tweezers and brushes. — [eMAG Jaysuing listing](https://www.emag.bg/produkti-terapia-za-tialo/brand/jaysuing/filter/forma-tekstura-f8091,techen-v-3951177/price,between-1-and-50/c)

**D. EU/UK retailers that ship to Bulgaria and sell ingrown pads**
- Lookfantastic (GBP prices on the .com site):
  - First Aid Beauty Ingrown Hair Treatment Pads (28 Pads): **£10.00** (RRP £20.00)
  - First Aid Beauty Ingrown Hair Pads 28 Ct.: **£15.00** (RRP £20.00)
  - First Aid Beauty Ingrown Hair Pads 60 Ct.: **£25.50** (RRP £34.00)
  - Murdock London Ingrown Hair Treatment 100ml: £18.00
  - Source: [Lookfantastic search "ingrown"](https://www.lookfantastic.com/search/?q=ingrown)
- Lookfantastic delivers to Bulgaria: tracked from £6.99, express from £8.99 (1–2 days). — [Lookfantastic international delivery](https://www.lookfantastic.com/c/info/international-delivery/)
- Notino's other EU stores sell FAB Ingrown Hair Pads 60 pcs at **36.00 €** (Notino.ee/LT, via price comparators). This shows the 60-pack exists in Notino's EU catalogue even though notino.bg only lists the 28-pack, out of stock. — [Kaina24.lt](https://www.kaina24.lt/ru/s/ingrown/?page=2); [Hind.ee](https://www.hind.ee/ru/s/aid-beauty/)
- Cult Beauty's "ingrown" search (EUR, Bulgarian geolocation) returned only Fur products and **no pads**. — [Cult Beauty search](https://www.cultbeauty.com/search/?q=ingrown)

### Inferences
- There is a clear shelf gap in Bulgaria for ingrown pads. The only mainstream listing (FAB 28 at Notino) is out of stock with zero reviews, and no Bulgarian pharmacy chain or drugstore stocks any ingrown/razor-bump pad.
- The pad format is still known to Bulgarian shoppers. Glycolic and BHA face pads (Nip+Fab, COSRX, Neogen) sell on Notino at €1.70–€18.90, which sets a price anchor for a body/bikini ingrown pad at roughly €15–25 for 30–60 pads.
- Most "pads" a Bulgarian searcher finds are on Ubuy, a cross-border reseller with slow delivery and opaque pricing. A local, in-stock, Bulgarian-language pad would likely face almost no direct retail competition.

### Gaps
- Ubuy.bg prices and stock could not be read (dynamic rendering). Delivery time and price to BG for FAB, Bushbalm and Waxness pads are unknown.
- eMAG blocked direct reading, so marketplace sellers listing pads (e.g. FAB) under titles my searches did not surface cannot be ruled out.
- I could not reach Mareshki's (mareshki.bg) and Benu's internal searches directly, so pad absence there rests on Google `site:` results only.
- Lookfantastic prices are in GBP from the UK storefront. The EUR price at checkout for Bulgaria, and whether import duty/VAT applies post-Brexit, was not verified.

## 2. Are the major global ingrown-pad and ingrown-care brands available in Bulgaria, and at what price?

### Takeaway
None of the US "hero" ingrown brands has a Bulgarian retail distributor: Bushbalm, Fur, Tend Skin, Bliss (ingrown line), Malin+Goetz Ingrown Hair Cream, Anthony, European Wax Center, Completely Bare, Coochy, Bodyographie. The exceptions are **PFB Vanish**, which has a BG distributor site and wide pharmacy/e-shop distribution, and **First Aid Beauty**, which is listed on Notino but out of stock. Fur is buyable cross-border (Cult Beauty in EUR; Beauty Bay) and Bushbalm ships direct to the EU. Tend Skin appears only via Ubuy.

### Cited Findings

**Brand-by-brand status for a Bulgarian buyer**

| Brand | Pads in range? | BG retail status | Best verified price for a BG buyer | Source |
|---|---|---|---|---|
| **First Aid Beauty** | Yes: Ingrown Hair Pads 28 / 60 | Notino.bg lists 28-pack, **out of stock**, 0 reviews. Ubuy.bg lists 60-pack and set | Lookfantastic £10–£15 (28), £25.50 (60). Notino EE/LT €36.00 (60) | [Notino FAB](https://www.notino.bg/first-aid-beauty/ingrown-hair-pads-eksfolirasshi-vzglavnichki/p-16296840/); [Lookfantastic](https://www.lookfantastic.com/search/?q=ingrown) |
| **Bushbalm** | Yes: Radiant Reset Exfoliating Toner Pads (30 large). Also Ingrown Hair Oil, Ingrown Hair Exfoliating Scrub, Roller Rescue serum | No BG retailer found. Ubuy.bg lists the pads (no readable price). The Ubuy brand page showed no products when scraped | Direct US list prices: pads **$19.00**; Ingrown Hair Oil (Nude/Watermelon/Vanilla) **$26.00**; mini oil $10.00; scrub $23.00; 2-Step Ingrown Routine $44.10 | [Bushbalm pads](https://bushbalm.com/products/radiant-reset-exfoliating-toner-pads); [Bushbalm oil](https://bushbalm.com/products/ingrown-hair-oil); [Ubuy.bg Bushbalm](https://www.ubuy.bg/en/product/IRACP9W28-radiant-reset-exfoliating-toner-pads-enhanced-with-bha-aha-to-brighten-dark-spots-soothe-bikini-area-ingrown-hairs-razor-bumps-30) |
| Bushbalm shipping | n/a | Brand ships to UK & EU through Passport Shipping, which acts as Seller of Record. International parcels take about 10–14 business days after leaving the US | n/a | [Bushbalm FAQ](https://bushbalm.com/pages/faqs); [Bushbalm help: international timeline](https://help.bushbalm.com/en-US/what-is-your-international-shipping-timeline-817705) |
| **Fur** | **No pads.** Line is Ingrown Concentrate (oil + mitt), Ingrown Eliminator Serum, Ingrown Microdart Patch, Bump Eliminator Scrub | No BG retailer (makeup.bg and notino searches negative). Ubuy.bg lists "Fur Oil" | **Cult Beauty (EUR, BG geo):** Ingrown Concentrate 0.5 fl oz **32.20€** (3.63★, 16 reviews); Ingrown Eliminator Serum 32ml **44.85€** (4.75★, 8); Ingrown Haircare Duo 35ml **46.95€**; Ingrown Microdart Patch **32.20€** (1★, 1). **Beauty Bay:** Ingrown Concentrate 14ml **$30.75** (3.99★, **1,362 reviews**), "Free Worldwide" delivery. Brand site (USD): Concentrate $34, Eliminator Serum $37, Microdart Patch $32 (12-pack) / $17 (6-pack) | [Cult Beauty](https://www.cultbeauty.com/search/?q=ingrown); [Beauty Bay Fur](https://www.beautybay.com/p/fur/ingrown-concentrate/); [Fur Concentrate](https://furyou.com/products/ingrown-concentrate); [Fur Microdart](https://furyou.com/products/ingrown-microdart-patch); [Ubuy.bg Fur Oil](https://www.ubuy.bg/bg/product/Q5J39RMQC-ingrown-hair-oil-for-bikini-line-underarms-legs-more-soothes-razor-bumps-prevents-ingrowns-reduces-redness-irritation-jojoba-clary-sage) |
| Cult Beauty / Beauty Bay shipping | n/a | Cult Beauty → Bulgaria: standard £4.95, 2–8 business days. Beauty Bay lists Bulgaria among delivery countries | n/a | [Cult Beauty BG delivery](https://www.cultbeauty.co.uk/c/info/delivery-information/europe/bulgaria/); [Beauty Bay countries](https://www.beautybay.com/s/delivery-countries/) |
| **Tend Skin** (liquid, not pads) | No | No BG retailer. Notino search for "Tend solution" returned unrelated items. Available only via Ubuy.bg (4 oz, 8 oz, 16 oz listings) | Ubuy prices not readable | [Ubuy.bg Tend Skin brand](https://www.ubuy.bg/en/brand/tend-skin); [Ubuy.bg Tend Skin 8 oz](https://www.ubuy.bg/en/product/6EXB2A-tend-skin-the-skin-care-solution-for-unsightly-razor-bumps-ingrown-hair-and-razor-burns-8-fl-oz-bottle); [Notino "Tend solution"](https://www.notino.bg/search.asp?exps=Tend%20solution) |
| Tend Skin demand signal | n/a | BG-Mamma forum threads ask where to buy Tend Skin in Bulgaria (thread is old and undated in snippet) | n/a | [BG-Mamma thread](https://www.bg-mamma.com/?topic=126256) |
| **PFB Vanish** (roll-on, not pads) | No | **Widely available in BG**: Framar, Ozone, Arteka, Simply Beauty, Befit, Baby.bg. Has a BG brand/distributor site vanishbg.com | Roll-on 93 g: **17,90 €** (Arteka) to **21,95 €** (Framar). + Chromabright 93 g: **26,00 €** (Simply Beauty) to **31,00 €** (Framar). See section 3 | [vanishbg.com](https://vanishbg.com/); [Framar category](https://apteka.framar.bg/%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B8/%D0%BA%D0%BE%D0%B7%D0%BC%D0%B5%D1%82%D0%B8%D1%87%D0%BD%D0%B8-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B8-%D0%B2%D1%80%D0%B0%D1%81%D1%82%D0%BD%D0%B0%D0%BB%D0%B8-%D0%BA%D0%BE%D1%81%D0%BC%D0%B8) |
| **Bliss** (Bump Attendant / ingrown pads) | Historically yes | Notino.bg has a Bliss brand page but the `site:` search surfaced only a cleansing gel/peel, **no ingrown products** | n/a | [Notino Bliss](https://www.notino.bg/bliss/); [Notino Bliss gel](https://www.notino.bg/bliss/skin-care-pochistvassh-gel-i-piling-2-v-1/) |
| **Malin+Goetz** Ingrown Hair Cream | No pads | Not found at any BG retailer. Brand runs an EU webstore | EU site lists shaving/ingrown category (cream price not captured) | [Malin+Goetz EU](https://eu.malinandgoetz.com/face/shaving) |
| **Kiehl's** Ultimate Razor Burn & Bump Relief (cream, not pads) | No | **Douglas.bg in stock** | **22,40 € / 43,81 лв.** promo (std 32,00 € / 62,59 лв.), 75 ml, 0 reviews. Also listed on makeup.bg (price not verified) | [Douglas.bg Kiehl's](https://douglas.bg/kiehls-ultimate-razor-burn-bump-relief-88638); [Makeup.bg Kiehl's](https://makeup.bg/product/549133/) |
| **Gillette Venus** for Pubic Hair & Skin | No pads | Notino.bg: Satin Care For Pubic Hair & Skin soothing serum 50 ml **13,50 €** (10,80 € with code "combi"), 4,0★ (6). Pubic razor 12,90 € (4,4★, 21). Blades from 14,50 € (4,2★, 15). eMAG sells a razor + bikini shave gel + serum kit | see left | [Notino ingrown hub](https://www.notino.bg/vrasnal-kosam/); [eMAG Gillette kit](https://www.emag.bg/komplekt-samobrysnachka-i-epilator-gillette-venus-pubic-hair-and-skin-samobrysnachka-satin-care-gel-za-brysnene-na-bikini-2-in-1-cleanser-shave-gel-190-ml-satin-care-izglazhdasht-serum-za-sled-brysnen/pd/D685CHYBM/) |
| **Nip+Fab** (off-label pads) | Glycolic Fix pads (face) | Notino.bg | **16,90 €** for 60 pads (4,0★, 1) | [Notino nip fab](https://www.notino.bg/search.asp?exps=nip%20fab) |
| **Pixi** Glow Tonic To-Go (off-label pads) | 60 pads, 5% glycolic | **Not found** on Notino.bg (search returned unrelated "glow" items). Niche Beauty CZ shows it out of stock | n/a | [Notino "glow tonic to-go"](https://www.notino.bg/search.asp?exps=glow%20tonic%20to-go); [Niche Beauty](https://www.niche-beauty.com/en-cz/products/pixi-glow-tonic-to-go/311-068) |
| **Dr. Dennis Gross** (off-label peel pads) | Yes (face) | **Not on Notino.bg** (search returned only Dr. Althea) | n/a | [Notino "dr. dennis gross"](https://www.notino.bg/search.asp?exps=dr.%20dennis%20gross) |
| **COSRX** (off-label BHA pads) | Yes (face) | Notino.bg lists several One Step pads | 18,90 € (Green Hero Calming, 70 pcs) | [Notino Cosrx](https://www.notino.bg/cosrx/one-step-original-tone-clarifying-moisture-pad-tonizirasshi-vzglavnichki-s-khidratirassh-efekt/) |
| **Waxness Dr. Bump** pads | Yes, 30 pcs | Ubuy.bg only | brand site $24.00 | [Ubuy.bg Waxness](https://www.ubuy.bg/bg/product/FNKRQPVWO-waxness-dr-bump-enzymatic-ingrown-hair-pads-2-steps-peeling-brightening-30-pcs) |
| **Skin Doctors** Ingrow Go (lotion, not pads) | No | Widely available (Framar, Ozone, drugstore.bg, store.bg) | 19,60 € to 24,00 € (see section 3) | [Framar Skin Doctors](https://apteka.framar.bg/30029040/%D1%81%D0%BA%D0%B8%D0%BD-%D0%B4%D0%BE%D0%BA%D1%82%D0%BE%D1%80%D1%81-ingrow-go-%D0%BB%D0%BE%D1%81%D0%B8%D0%BE%D0%BD-120-%D0%BC%D0%BB) |
| **Lycon** Ingrown-X-it (salon brand) | Solution/cream/foaming gel | Not found on BG sites (results were only from Lycon's other national sites and Amazon UK) | n/a | [Lycon Germany](https://www.lycon-germany.de/produkte/lycon-spa-essentials/ingrown-x-it/) |

### Inferences
- The global "pad" leaders (FAB, Bushbalm) have no working Bulgarian shelf presence. FAB is technically listed but unavailable, and Bushbalm is only reachable by direct import or Ubuy. The BG market is served by the liquid/roll-on format led by PFB Vanish and Skin Doctors.
- Fur is the most-reviewed ingrown brand reachable from BG (1,362 reviews on Beauty Bay). It sells at €32–47 cross-border, which signals that Bulgarian buyers who import are paying premium prices.
- Fur's Microdart Patch at Cult Beauty is a premium ingrown patch format, €32.20 for 12. A patch-format ingrown product therefore already exists at the top end of the market, but it has only 1 review on Cult Beauty.

### Gaps
- I could not check Anthony, European Wax Center, Completely Bare, Coochy, Bodyographie, Billie, Eos, Alpha-H, Paula's Choice or The Ordinary item by item. None appeared in any BG ingrown search, but I did not run a dedicated brand query for each. Treat them as "not found / likely unavailable", not as confirmed absent.
- The "Gigi" in the brief (US Gigi waxing brand) was not found. A different company, GIGI Laboratories (Israeli professional skincare), appears on Ozone (see section 3).
- Bushbalm's EUR price at checkout for Bulgaria could not be read (the storefront geolocated to USD). Passport's duties/fees are unknown.

## 3. Close substitutes (serums, roll-ons, lotions, sprays, oils) sold in Bulgaria for ingrown hairs and razor bumps

### Takeaway
The Bulgarian ingrown category is dominated by liquids:
- **PFB Vanish** roll-on, about €18–22, and the Chromabright version, about €26–31.
- **Skin Doctors Ingrow Go** lotion, about €19.60–24.
- The Bulgarian acne lotion **Biotrade Acne Out**, €9.29–19.79, which is applied with a cotton pad and explicitly indicated for ingrown hairs after epilation.
- A Bulgarian DTC serum, **LUMI**, at €20.90 (compare-at €40).
- Professional waxing-brand lotions (Alveola, Italwax, Depilflax, Thalgo, Perron Rigot) and many cheap Chinese roll-ons on eMAG.

**All entries below are SUBSTITUTES, not pads.**

### Cited Findings

| Product (SUBSTITUTE, not pad) | Format / size | Actives | Price as shown | Retailer / stock | Rating (count) | Source |
|---|---|---|---|---|---|---|
| PFB Vanish серум рол-он за враснали косми | roll-on 93 g | salicylic, glycolic, lactic acid; willow bark, camphor oil | **21.95 €** | Framar, InStock | 3.9 (**62**) | [Framar PFB](https://apteka.framar.bg/30049735/%D0%B2%D0%B0%D0%BD%D0%B8%D1%88-pfb-%D1%81%D0%B5%D1%80%D1%83%D0%BC-%D1%80%D0%BE%D0%BB-%D0%BE%D0%BD-%D0%B7%D0%B0-%D0%B2%D1%80%D0%B0%D1%81%D1%82%D0%BD%D0%B0%D0%BB%D0%B8-%D0%BA%D0%BE%D1%81%D0%BC%D0%B8-120-%D0%BC%D0%BB) |
| same | 93 g | same | **20.39 €** | Ozone, InStock | n/a | [Ozone PFB](https://www.ozone.bg/product/pfb-vanish-rol-on-serum-za-premahvane-i-preventsiya-na-vrastnali-kosmi-93-gr/) |
| same ("120 мл") | 120 ml | same | **17,90 €** | Arteka (pharmacy) | 0 reviews | [Arteka PFB](https://www.arteka.bg/%D0%BA%D0%BE%D0%B7%D0%BC%D0%B5%D1%82%D0%B8%D0%BA%D0%B0-%D0%B7%D0%B0-%D0%BE%D0%B1%D0%B5%D0%B7%D0%BA%D0%BE%D1%81%D0%BC%D1%8F%D0%B2%D0%B0%D0%BD%D0%B5/5138-%D1%80%D0%BE%D0%BB-%D0%BE%D0%BD-%D1%81%D0%B5%D1%80%D1%83%D0%BC-%D0%B7%D0%B0-%D0%BF%D1%80%D0%B5%D0%BC%D0%B0%D1%85%D0%B2%D0%B0%D0%BD%D0%B5-%D0%B8-%D0%BF%D1%80%D0%B5%D0%B2%D0%B5%D0%BD%D1%86%D0%B8%D1%8F-%D0%BD%D0%B0-%D0%B2%D1%80%D0%B0%D1%81%D1%82%D0%BD%D0%B0%D0%BB%D0%B8-%D0%BA%D0%BE%D1%81%D0%BC%D0%B8-120-%D0%BC%D0%BB-pfb-vanish.html) |
| PFB Vanish Post & Waxing Shaving Serum (roll-on) | roll-on | n/a | **18,00 €** (button reads "Виж детайли" instead of "Купете", so possibly unavailable) | Simply Beauty | 0.0 | [Simply Beauty PFB](https://simplybeauty.bg/vendor/pfb-vanish) |
| PFB Vanish + Chromabright (депигментиращ) | 93 g / "120 мл" | salicylic, glycolic, lactic + Chromabright brightener | **31.00 €** | Framar, InStock | 3.8 (**78**) | [Framar Chromabright](https://apteka.framar.bg/30049736/%D0%B2%D0%B0%D0%BD%D0%B8%D1%88-pfb-%D0%B4%D0%B5%D0%BF%D0%B8%D0%B3%D0%BC%D0%B5%D0%BD%D1%82%D0%B8%D1%80%D0%B0%D1%89-%D1%81%D0%B5%D1%80%D1%83%D0%BC-%D0%B7%D0%B0-%D0%B2%D1%80%D0%B0%D1%81%D1%82%D0%BD%D0%B0%D0%BB%D0%B8-%D0%BA%D0%BE%D1%81%D0%BC%D0%B8-120-%D0%BC%D0%BB-93-%D0%B3%D1%80) |
| same | 93 g | same | **27,16 €** (ПЦД 31,95 €, −15%) | Ozone, InStock (also Baby.bg at same price per snippet) | n/a | [Ozone Chromabright](https://www.ozone.bg/product/pfb-vanish-depigmentirasht-serum-za-premahvane-na-vrastnali-kosmi-93-gr/); [Baby.bg](https://www.baby.bg/brand_pfb_vanish/) |
| same | roll-on | same | **26,00 €** | Simply Beauty ("Купете") | 5.0 | [Simply Beauty PFB](https://simplybeauty.bg/vendor/pfb-vanish) |
| Skin Doctors Ingrow Go лосион | 120 ml | salicylic acid, glycolic acid | **24.00 €** | Framar, InStock | 4.2 (**86**), the highest review count among BG ingrown listings found | [Framar Skin Doctors](https://apteka.framar.bg/30029040/%D1%81%D0%BA%D0%B8%D0%BD-%D0%B4%D0%BE%D0%BA%D1%82%D0%BE%D1%80%D1%81-ingrow-go-%D0%BB%D0%BE%D1%81%D0%B8%D0%BE%D0%BD-120-%D0%BC%D0%BB) |
| same | 120 ml | same | **24.00 €** | drugstore.bg, InStock | n/a | [drugstore.bg](https://drugstore.bg/%D1%81%D0%BA%D0%B8%D0%BD-%D0%B4%D0%BE%D0%BA%D1%82%D0%BE%D1%80%D1%81-%D0%BB%D0%BE%D1%81%D0%B8%D0%BE%D0%BD-%D0%BF%D1%80%D0%B8-%D1%80%D0%B0%D1%81%D1%82%D1%8F%D1%89%D0%B8-%D0%BF%D0%BE%D0%B4%D0%BA%D0%BE%D0%B6%D0%BD%D0%BE-%D0%BA%D0%BE%D1%81%D0%BC%D0%B8-120-%D0%BC%D0%BB-skin-doctors-ingrow-go-8098) |
| same | 120 ml | same | **19.60 €** | Ozone, InStock | n/a | [Ozone Skin Doctors](https://www.ozone.bg/product/skin-doctors-losion-protiv-podkozhni-kosmi-ingrow-go-120-ml/) |
| same | 120 ml | same | **21.40 €** (schema price). Box Now delivery 0,99 € | store.bg | snippet: 5.0 (10) | [store.bg](https://www.beauty.store.bg/p244135/skin-doctors-ingrow-go-ingrown-hair-lotion.html) |
| **LUMI Серум Против Врастнали Косми** (Bulgarian DTC brand, Shopify) | serum (size not stated) | BHA (salicylic), AHA (glycolic), gluconolactone, niacinamide, centella (madecassoside/asiaticoside), witch hazel, aloe, zinc PCA | **20,90 €** (compare-at 40,00 €), InStock | lumibg.com | Review widget: **4.9/5 from 34 reviews**. Page header claims "4.8 – 7356 Ревюта" and "7356 клиента закупиха" (an unverified marketing claim that conflicts with the widget). Uses an urgency timer ("Промоцията приключва след 4 часа!") and a stock counter ("Остават 11 броя") | [LUMI product](https://lumibg.com/products/lumi-ingrown) |
| Biotrade **Acne Out** Активен лосион (Bulgarian brand; label indications include "врастнали косми след епилация; фоликулит". Applied "с обилно напоен" cotton pad) | 60 ml | (acne active lotion; full INCI not captured) | **13.29 €** | SOpharmacy | 4.6 (16) | [SOpharmacy](https://sopharmacy.bg/bg/product/000000000010006109) |
| same | 60 ml | | **9.29 €** promo (reg. 12.39 €) | Galen | n/a | [Galen](https://galen.bg/biotrade-acne-out-aktiven-losion-za-akneichna-kozha-60-ml) |
| same | 60 ml | | **12,15 €** (std 16,20 €) | Lilly Drogerie | n/a | [Lilly](https://lillydrogerie.bg/v-cherni-tochki-p-pki-60ml) |
| same | 60 ml | | 13.95 € (Afya) / 16,61 € (Prime) / **€19,79** (brand store biotrade.bg) | various | n/a | [Afya](https://www.afya-pharmacy.bg/biotrade-acne-out-aktiven-losion-pri-akne-60-ml); [Prime](https://primepharmacy.bg/biotrade-acne-out-aktiven-losion-pri-akne-60-ml); [biotrade.bg](https://biotrade.bg/collections/acne-out) |
| Acorelle Anti-Ingrown Hair Care (Алое и Мед), spray, ECOCERT | 50 ml | fruit AHAs, lactic acid, lemon, aloe, honey | **39.28 €** (as shown) | Makeup.bg, "В наличност!" | 5★ (1) | [Makeup.bg Acorelle](https://makeup.bg/product/582237/) |
| BioMD Ingrow Gone emulsion | n/a | AHA/BHA, glycolic + salicylic acid | metadata price "0" (likely unavailable; **unverified**) | Makeup.bg | n/a | [Makeup.bg BioMD](https://makeup.bg/product/931588/) |
| Fler Hoily Drops Ingrown Treatment (oil) | 14 ml | almond, jojoba, tea tree, tamanu, bisabolol (99.4% natural) | Makeup.bg metadata price "0" (likely unavailable). Also listed on eMAG | Makeup.bg / eMAG | n/a | [Makeup.bg Fler](https://makeup.bg/product/928613/); [eMAG Fler](https://www.emag.bg/lechenie-protiv-hvyrchashta-kosa-hoily-drops-ingrown-treatment-14-ml-194-1/pd/DMJ9M9YBM/) |
| Perron Rigot (Cirépil) Ingrown Hair Skincare Serum | 30 ml | gluconolactone (PHA), fruit enzymes, gentle acids | **€15.85 / 31.00 лв.**, "В наличност" (parsed from tag listing; verify on product page) | expertcosmetics.online | n/a | [Expert Cosmetics tag "врастли косми"](https://expertcosmetics.online/tag/16/vrastli-kosmi.html?page=1&view=list) |
| Kiehl's Ultimate Razor Burn & Bump Relief | 75 ml | aloe, lipo-hydroxy acid, willow herb | **22,40 €** promo (32,00 € std) | Douglas.bg, in stock | 0 | [Douglas.bg](https://douglas.bg/kiehls-ultimate-razor-burn-bump-relief-88638) |
| Gillette Satin Care For Pubic Hair & Skin soothing serum | 50 ml | n/a | **13,50 €** (10,80 € with code) | Notino.bg | 4,0 (6) | [Notino](https://www.notino.bg/vrasnal-kosam/) |
| Australian Bodycare Tea Tree Oil Lemon Myrtle intimate after-shave balm | 100 ml | tea tree | 15,50 € | Notino.bg | n/a | [Notino](https://www.notino.bg/vrasnal-kosam/) |
| BusyB Beaver Reliever Becky Blossom after-shave balm (sensitive) | 75 ml | n/a | 8,50 € | Notino.bg | n/a | [Notino](https://www.notino.bg/vrasnal-kosam/) |
| GIGI Laboratories Retin A Интимен пилинг | 5 × 5 ml | glycolic, lactic, mandelic, kojic acids; retinyl palmitate | **127,82 €**, **"Изчерпан" (sold out)** | Ozone | n/a | [Ozone GIGI](https://www.ozone.bg/product/gigi-retin-a-intimen-piling-5-x-5-ml/) |
| Alveola Waxing Pre-Hair Growth lotion (spray) for ingrown hairs | 100 ml | fruit acids | **6,69 € / 13,08 лв.** (ПЦД 7,27 €), in stock, seller Info Depozit | eMAG | n/a | [eMAG Alveola](https://www.emag.bg/aksesoari-za-depilacia/brand/alveola/filter/produkti-na-oferta-f9989,oferti-v9/c) |
| Italwax cream for prevention/treatment of ingrown hairs | 30 ml | n/a | "Продуктът временно не е в наличност" | eMAG, **out of stock** | n/a | [eMAG Italwax cream](https://www.emag.bg/krem-za-profilaktika-i-lechenie-na-vrastnali-kosmi-italwax-30-ml-it177000-eol/pd/D91ZWRMBM/) |
| Italwax Ingrown Hairs Therapy lotion | 100 ml | n/a | price not captured | eMAG | n/a | [eMAG Italwax lotion](https://www.emag.bg/losion-sled-epilacija-ingrown-hairs-therapy-italwax-100ml-itw77024/pd/DBQ96XMBM/) |
| Depilflax Hair Puller lotion | 125 ml | n/a | price not captured | eMAG | n/a | [eMAG Depilflax](https://www.emag.bg/losion-hair-puller-za-profilaktika-i-lechenie-na-vrastnali-kosmi-depilflax-125-ml-dpx32416/pd/DMKJCPYBM/) |
| Thalgo Targets Ingrown Hairs lotion | 30 ml | n/a | price not captured | eMAG | n/a | [eMAG Thalgo](https://www.emag.bg/losion-thalgo-targets-ingrown-hairs-30-ml-hidratacija-protivovyzpalitelen-efekt-za-chuvstvitelna-kozha-fertes-3525801644750/pd/DR8J623BM/) |
| WOMN Intimate Comfort serum (vegan, sensitive skin) | 50 ml | n/a | price not captured | eMAG | n/a | [eMAG WOMN](https://www.emag.bg/serum-womn-intimate-comfort-50-ml-za-chuvstvitelna-kozha-predotvratjava-vrastnali-kosmi-vegan-5451/pd/DPJ2XW3BM/) |
| Lanthome hair-growth-inhibitor emulsion | 30 ml | n/a | ПЦД 16,08 € (sale price not captured) | eMAG | n/a | [eMAG Lanthome](https://www.emag.bg/emulsija-za-inhibitor-na-rastezha-na-kosata-lanthome-30-ml-namaljava-razdraznenieto-sled-epilacija-em-ccm250103-14455/pd/D6B5Q8YBM/) |
| Generic "Серум за третиране на врастнали косми, 50мл, за бикини линия, подмишници и крака" (OEM) | 50 ml | "натурални екстракти" | snippets conflict: "9,60 €… 2,62 €" in one, "3,82 € / 7,47 лв." (4.5★, 2) in another; also "Smart Deals −64% / −72%" | eMAG | 3.3 (3) on product page snippet | [eMAG generic serum](https://www.emag.bg/serum-za-tretirane-na-vrastnali-kosmi-50ml-za-bikini-linija-podmishnici-i-kraka-s-naturalni-ekstrakti-a000030/pd/DY8ZT63BM/) |
| JAYSUING roll-on against ingrown hairs, set of 2 × 50 ml | roll-on | "exfoliating, soothing" | **20,77 €** | eMAG (Chinese marketplace seller) | n/a | [eMAG Jaysuing](https://www.emag.bg/tretirane-za-vrasnali-kosmi-eksfolirasht-uspokojavasht-50ml-komplekt-ot-3-broja-jaysuing-fgevk0225-0905-1115/pd/DG96DV3BM/) |
| "Bump Stopper" roll-on for ingrown hairs (men & women) | 100 ml | n/a | price not captured | eMAG | n/a | [eMAG Bump Stopper](https://www.emag.bg/lechenie-za-vrasnali-kosmi-i-razdraznenija-bump-stopper-za-myzhe-i-zheni-rol-on-aplikator-100-ml-aplug-fu-k0228-250901-2084/pd/DDM24S3BM/) |
| SVR Xerial 30 gel-cream (urea; label mentions ingrown hairs/KP) | 75 ml | urea | price not captured | Ozone, Galen, ePharma, SOpharmacy | n/a | [Ozone SVR](https://www.ozone.bg/product/svr-xerial-30-krem-za-kozhni-zadebelyavaniya-75-ml/); [ePharma SVR](https://epharma.bg/svr-xerial-30-%D0%B3%D0%B5%D0%BB-%D0%BA%D1%80%D0%B5%D0%BC-%D0%B7%D0%B0-%D1%82%D1%8F%D0%BB%D0%BE-%D0%B7%D0%B0-%D1%81%D1%83%D1%85%D0%B0-%D0%BA%D0%BE%D0%B6%D0%B0-%D1%8575-%D0%BC%D0%BB-1-19238) |
| Fluff smoothing body lotion with salicylic acid (Polish brand; label mentions ingrown hairs) | 150 ml | salicylic acid | price not captured, "In stock" per snippet | Galen | n/a | [Galen Fluff](https://galen.bg/flaff-losion-za-tyalo-izglazhdasht-sas-salitsilova-kiselina-150ml) |
| Е-Лек Вранас мехлем с невен (calendula ointment, listed in Framar's ingrown category) | 20 ml / 40 ml | calendula | 7.20 € / 12.80 € | Framar | n/a | [Framar category](https://apteka.framar.bg/%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B8/%D0%BA%D0%BE%D0%B7%D0%BC%D0%B5%D1%82%D0%B8%D1%87%D0%BD%D0%B8-%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B8-%D0%B2%D1%80%D0%B0%D1%81%D1%82%D0%BD%D0%B0%D0%BB%D0%B8-%D0%BA%D0%BE%D1%81%D0%BC%D0%B8) |

Patch-format items (relevant if the client plans an ingrown-hair *patch*):
- Fur Ingrown Microdart Patch: 32.20 € at Cult Beauty (1★, 1 review); brand site $32 for 12 / $17 for 6. — [Cult Beauty](https://www.cultbeauty.com/search/?q=ingrown); [Fur](https://furyou.com/products/ingrown-microdart-patch)
- Ubuy.bg lists several generic ingrown patches: "Ingrown Hair Treatment Patch, 30 Pcs… bikini area"; "FunnAura 18 Pcs Ingrown Hair Pads (patches)"; "Ingrown Hair – 9 Pieces… Patches", € 10. — [Ubuy 30 pcs](https://www.ubuy.bg/en/product/QVEWED20G-ingrown-hair-treatment-patch); [Ubuy FunnAura](https://www.ubuy.bg/bg/productuk/U14Z6OJL2-funnaura-18-pcs-ingrown-hair); [Ubuy 9 pcs](https://www.ubuy.bg/bg/productuk/T2RNZRPJA-ingrown-hair-9-pieces)

### Inferences
- PFB Vanish is the de-facto category leader on the BG shelf. It has a local distributor site, is in 6+ BG retailers, and carries 62 + 78 ratings at Framar. Skin Doctors Ingrow Go is second, with 86 ratings at Framar. Both are liquids priced about €18–31, which gives a pad product a clear price ceiling to position against.
- LUMI is the closest local competitor in marketing style. It is a BG DTC Shopify brand with a BHA/AHA serum at €20.90 against a "€40" anchor, using urgency/scarcity widgets and a large claimed review count. This suggests other DTC players are already running paid social in this niche in Bulgaria.
- The Biotrade Acne Out case shows that Bulgarian consumers and pharmacists already use "lotion + cotton pad" as an ingrown routine. A pre-soaked pad is a natural convenience upgrade on that habit.

### Gaps
- eMAG prices for Thalgo, Italwax lotion, Depilflax, WOMN, Fler, Bump Stopper and Lanthome (sale price) could not be read because of the CAPTCHA.
- No BG pages were found for the Polish/German drugstore brands named in the brief (Joanna, Ziaja, Eveline, Bielenda, Lirene, Floslek, Delia, Isana, Balea) as ingrown-specific products. One combined search returned nothing ingrown-related, and dm.bg surfaced only Balea bleaching cream. Fluff (Polish) is the only such brand found, with a salicylic body lotion.
- SVR Xerial 30 and Fluff prices were not captured (Galen blocked curl).

## 4. Reviews and ratings on Bulgarian listings (demand signal)

### Takeaway
Review volumes on Bulgarian ingrown listings are small: the highest is 86 ratings, for Skin Doctors at Framar. The dedicated pad listing (FAB at Notino) has 0 reviews. The largest review counts reachable by Bulgarians are on foreign sites (Fur on Beauty Bay: 1,362). This suggests a small but real category in BG where liquids dominate, with no pad incumbent.

### Cited Findings
- Skin Doctors Ingrow Go: **4.2★ / 86 ratings** (Framar). — [Framar](https://apteka.framar.bg/30029040/%D1%81%D0%BA%D0%B8%D0%BD-%D0%B4%D0%BE%D0%BA%D1%82%D0%BE%D1%80%D1%81-ingrow-go-%D0%BB%D0%BE%D1%81%D0%B8%D0%BE%D0%BD-120-%D0%BC%D0%BB)
- PFB Vanish + Chromabright: **3.8★ / 78** (Framar). PFB Vanish roll-on: **3.9★ / 62** (Framar). — [Framar Chromabright](https://apteka.framar.bg/30049736/%D0%B2%D0%B0%D0%BD%D0%B8%D1%88-pfb-%D0%B4%D0%B5%D0%BF%D0%B8%D0%B3%D0%BC%D0%B5%D0%BD%D1%82%D0%B8%D1%80%D0%B0%D1%89-%D1%81%D0%B5%D1%80%D1%83%D0%BC-%D0%B7%D0%B0-%D0%B2%D1%80%D0%B0%D1%81%D1%82%D0%BD%D0%B0%D0%BB%D0%B8-%D0%BA%D0%BE%D1%81%D0%BC%D0%B8-120-%D0%BC%D0%BB-93-%D0%B3%D1%80); [Framar roll-on](https://apteka.framar.bg/30049735/%D0%B2%D0%B0%D0%BD%D0%B8%D1%88-pfb-%D1%81%D0%B5%D1%80%D1%83%D0%BC-%D1%80%D0%BE%D0%BB-%D0%BE%D0%BD-%D0%B7%D0%B0-%D0%B2%D1%80%D0%B0%D1%81%D1%82%D0%BD%D0%B0%D0%BB%D0%B8-%D0%BA%D0%BE%D1%81%D0%BC%D0%B8-120-%D0%BC%D0%BB)
- LUMI serum: 4.9/5 from 34 reviews in its review widget. The header claims 4.8 from 7,356 reviews (unverified, self-reported). — [LUMI](https://lumibg.com/products/lumi-ingrown)
- Biotrade Acne Out: 4.6★ / 16 (SOpharmacy). — [SOpharmacy](https://sopharmacy.bg/bg/product/000000000010006109)
- Gillette Venus pubic: serum 4,0★ (6), razor 4,4★ (21), blades 4,2★ (15) on Notino. — [Notino](https://www.notino.bg/vrasnal-kosam/)
- First Aid Beauty Ingrown Hair Pads on Notino.bg: **0 reviews**, out of stock. — [Notino FAB](https://www.notino.bg/first-aid-beauty/ingrown-hair-pads-eksfolirasshi-vzglavnichki/p-16296840/)
- Nip+Fab Glycolic Fix pads on Notino.bg: 4,0★ (1). — [Notino](https://www.notino.bg/search.asp?exps=nip%20fab)
- Skin Doctors on store.bg: 5.0 (10) per search snippet. — [store.bg](https://www.beauty.store.bg/p244135/skin-doctors-ingrow-go-ingrown-hair-lotion.html)
- Cross-border for comparison: Fur Ingrown Concentrate 3.99★ / **1,362** (Beauty Bay); 3.63★ / 16 (Cult Beauty). — [Beauty Bay](https://www.beautybay.com/p/fur/ingrown-concentrate/); [Cult Beauty](https://www.cultbeauty.com/search/?q=ingrown)
- Notino BG's "Враснал косъм" hub aggregates 477 products, mostly razors, trimmers, epilators and IPL. It names the intimate area as "може би най-честият проблем" for ingrown hairs, and the ingrown products in the hub are only creams and serums. — [Notino hub](https://www.notino.bg/vrasnal-kosam/)

### Inferences
- With the leading ingrown SKUs at under 100 ratings each on BG retail sites, the category is small but proven, and repeat buyers exist (Framar ratings accumulate over years). Mediocre ratings (3.8–3.9 for PFB) leave room for a better-rated alternative.
- Absolute demand is not measurable from these counts alone. Search-volume data from a different research thread would be needed.

### Gaps
- eMAG review counts for generic roll-ons were mostly unreadable (only 3.3★/3 for one OEM serum).
- No sales-rank data was available from any BG retailer.

## 5. Which big global ingrown-pad brands are NOT available in Bulgaria at all (the gap)?

### Takeaway
No Bulgarian retailer stocks a working ingrown-hair pad, so there is no in-stock incumbent on the Bulgarian shelf. FAB pads are listed at Notino but out of stock. Bushbalm, Waxness Dr. Bump and generic pads are reachable only through Ubuy cross-border import or direct/EU-UK shipping. The other named brands were not found in Bulgarian retail at all.

### Cited Findings
- **Listed but unavailable:** First Aid Beauty Ingrown Hair Pads 28 (Notino.bg, out of stock). — [Notino FAB](https://www.notino.bg/first-aid-beauty/ingrown-hair-pads-eksfolirasshi-vzglavnichki/p-16296840/)
- **Only cross-border (Ubuy.bg, prices not visible) or direct-ship:**
  - Bushbalm Radiant Reset pads: Ubuy, and direct from Bushbalm, which ships to EU via Passport. — [Ubuy](https://www.ubuy.bg/en/product/IRACP9W28-radiant-reset-exfoliating-toner-pads-enhanced-with-bha-aha-to-brighten-dark-spots-soothe-bikini-area-ingrown-hairs-razor-bumps-30); [Bushbalm FAQ](https://bushbalm.com/pages/faqs)
  - FAB 60: Ubuy. — [Ubuy](https://www.ubuy.bg/en/product/M0OHFWOVO-first-aid-beauty-ingrown-hair-pads-with-bha-aha-daily-treatment-prevents-razor-bumps-ingrown-hairs-and-soothes-irritation-60-pads)
  - Waxness Dr. Bump pads, Pure Ease, Inlon and other generic pads: Ubuy. — [Ubuy Waxness](https://www.ubuy.bg/bg/product/FNKRQPVWO-waxness-dr-bump-enzymatic-ingrown-hair-pads-2-steps-peeling-brightening-30-pcs)
  - Tend Skin: Ubuy only. — [Ubuy Tend Skin](https://www.ubuy.bg/en/brand/tend-skin)
- **Available only from foreign retailers that ship to BG:**
  - Fur: Cult Beauty in EUR, Beauty Bay. — [Cult Beauty](https://www.cultbeauty.com/search/?q=ingrown)
  - FAB pads: Lookfantastic in GBP. — [Lookfantastic](https://www.lookfantastic.com/search/?q=ingrown)
- **Not found in any BG retailer or BG-facing search:**
  - Bliss ingrown line (Notino carries Bliss, but no ingrown products). — [Notino Bliss](https://www.notino.bg/bliss/)
  - Malin+Goetz Ingrown Hair Cream (EU webstore exists). — [M+G EU](https://eu.malinandgoetz.com/face/shaving)
  - Pixi Glow Tonic To-Go. — [Notino search](https://www.notino.bg/search.asp?exps=glow%20tonic%20to-go)
  - Dr. Dennis Gross peel pads. — [Notino search](https://www.notino.bg/search.asp?exps=dr.%20dennis%20gross)
  - Lycon Ingrown-X-it. — [Lycon search results were non-BG only](https://lyconswitzerland.com/ingrown-x-it/)
- **Present in BG (liquids, not pads):** PFB Vanish, Skin Doctors, Kiehl's (Douglas), Gillette Venus pubic serum (Notino), Acorelle (Makeup.bg), Perron Rigot (Expert Cosmetics), LUMI (DTC), Biotrade Acne Out (pharmacies), plus Alveola, Italwax, Depilflax and Thalgo (eMAG). See section 3 for sources.

### Inferences
- A Bulgarian-language, locally stocked, pre-soaked ingrown pad for the bikini/intimate area would currently have **no in-stock branded pad competitor on any Bulgarian retail shelf**. Its practical competitors are PFB Vanish and Skin Doctors (€18–31 liquids), LUMI (€20.90 DTC serum) and imported FAB/Bushbalm pads.
- Price anchors a new pad would be compared against:
  - FAB 28 pads: £10–15 at Lookfantastic
  - FAB 60 pads: €36 at Notino EU, £25.50 at Lookfantastic
  - Bushbalm 30 pads: $19 direct
  - Nip+Fab 60 face pads: €16.90 at Notino.bg
  - PFB roll-on: about €20

### Gaps
- Not checked brand by brand: Anthony, European Wax Center, Completely Bare, Coochy, Bodyographie, Billie, Eos, Alpha-H, Paula's Choice, The Ordinary, Nair, Veet ingrown products. Their absence is inferred from all-category ingrown searches, not confirmed by a per-brand query.
- Whether Bushbalm's or FAB's EU wholesale is moving into Bulgaria (e.g., a pending Notino restock date) is unknown. Notino offers a "Проследяване на наличност" (stock-alert) button but no restock date.
