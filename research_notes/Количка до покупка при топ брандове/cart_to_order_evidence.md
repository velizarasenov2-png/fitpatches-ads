# Cart-to-order conversion and cart abandonment for mobile Meta-ad shoppers in COD markets (FitPatches, Bulgaria): evidence and funnel benchmark

Research date: 2 Oct 2026. Labels used below: **[IND]** = independent research or benchmark (Baymard, Littledata, Dynamic Yield, BEA, official docs). **[VENDOR]** = vendor or app-maker claim (Shopify about its own checkout, EasySell, Releasit, OTP/RTO tool vendors). **[BLOG]** = practitioner or agency blog with no primary data. **[SNIPPET]** = seen only in a search-engine summary; the underlying page was not opened.

FitPatches inputs (Shopify, last 90 days, given by the user): 5,653 sessions → 608 sessions with add-to-cart → 160 sessions reached Shopify checkout → 77 completed Shopify checkout. Another 244 orders came through the EasySell COD form. That is 324 orders in total, with AOV €27.64.

---

## 1. How to read this funnel correctly (what Shopify counts, true cart→order rate, adding COD-app steps)

### Takeaway
Shopify's "reached checkout", "completed checkout" and "conversion rate" metrics only count purchases made through Shopify's own checkout. The 244 EasySell orders are missing from them, so the store's real placed-order conversion is about 5.7% of sessions, not the 1.36% Shopify reports. Cart→order is at most about 53% of cart sessions. The funnel needs extra COD steps (form opened → form submitted → confirmed → shipped → delivered/paid) taken from EasySell pixel events and courier data.

### Cited Findings
- **[IND, official]** Shopify's definitions:
  - "Sessions with cart additions" = sessions where a customer added a product to a cart.
  - "Sessions that reached checkout" = "sessions where there was user input (for example, a key press or mouse click) during checkout".
  - "Sessions that completed checkout" = "sessions where a customer purchased a product".
  - Conversion rate = "percentage of sessions that resulted in a purchase".
  - Shopify also notes that "your order count and your sessions that completed checkout count might not be the same" because one session can contain several purchases.
  - Source: [Shopify Help Center – behaviour reports](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/behaviour-reports)
- **[IND, merchant forum, May 2024]** A merchant reported that orders placed through the EasySell COD app are valid orders on the Orders page but do not appear in Shopify's conversion-rate analytics. The thread links the cause to COD apps (Releasit, EasySell) creating orders without Shopify Checkout, and to "conversion details unavailable… for orders that were created via the Checkout API". No official Shopify or EasySell answer was given. — [Shopify Community thread](https://community.shopify.com/t/conversion-rates-not-reflecting-accurately-especially-orders-coming-in-from-easy-sell-cod-app/323993)
- **[SNIPPET, third-party checkout help centre]** With third-party checkout apps it is "normal" for Shopify's online-store conversion rate to drop, because "Reached checkout" and "Sessions converted" go to the app and Shopify does not track them. Apps often calculate their own conversion as orders ÷ checkouts (each unique cart session = one checkout). — [Checkout help center FAQ](https://intercom.help/checkouthelpcenter/en/articles/3106347-faqs-report-tracking)
- **[VENDOR-adjacent doc]** EasySell's Meta pixel integration fires "InitiateCheckout, Purchase or Lead". On TikTok it fires InitiateCheckout and CompletePayment; on Google Tag (gtag) it fires InitiateCheckout and Purchase. The doc does not say when InitiateCheckout fires (form open or something else). — [Tyslo/EasySell help: tracking pixels](https://help.tyslo.com/en/article/how-to-add-tracking-pixels-to-easysell-laiv2w/)
- **[VENDOR]** EasySell warns that if pixels are also installed through the theme or another app, purchase events can be duplicated. Duplicates "inflate your reported ROAS and confuse your ad platform's optimization". — [EasySell setup guide, via search result](https://easysellapp.com/blogs/wiki/easysell-setup-guide-get-started-15-minutes-2026)
- **[VENDOR]** EasySell's OTP article suggests tracking "verification completion rates (should exceed 85%)" and RTO before and after OTP. It does not describe a dashboard metric for form views versus orders. — [EasySell: OTP verification setup (Apr 2026)](https://easysellapp.com/blogs/wiki/shopify-cod-otp-verification-setup)

### Inferences
- **FitPatches' funnel recomputed** (arithmetic on the user's numbers):
  - Add-to-cart rate: 608 / 5,653 = **10.8%**
  - Shopify-checkout path:
    - 160 / 608 = **26.3%** of cart sessions reach Shopify checkout
    - 77 / 160 = **48.1%** checkout completion
    - 77 / 5,653 = **1.36%** "Shopify conversion"
  - All orders: 324 / 5,653 = **5.73% orders per session**
  - EasySell share of orders: 244 / 324 = **75.3%**
  - Orders per cart session: 324 / 608 = **53.3%**. This is an upper bound. Some sessions place more than one order. If the EasySell button also sits on the product page, some EasySell orders may come from sessions with no Shopify add-to-cart event, which would make the true cart→order rate lower.
  - Implied cart abandonment: about 1 − 0.533 = **~47%**. Compare Baymard's 70% average (Section 3).
- **The 26% "cart→checkout" figure is not a leak.** Most cart sessions go to the orange EasySell button and never touch Shopify checkout. Do not compare it with benchmarks.
- **Placed is not delivered.** Delivered conversion = 5.73% × (1 − refusal/cancellation rate).

  | Refusal rate | Delivered orders | Delivered orders per session |
  |---|---|---|
  | 10% | ≈292 | 5.2% |
  | 15% | ≈275 | 4.9% |
  | 20% | ≈259 | 4.6% |

  These are illustrative scenarios, not FitPatches data. Check the real refusal rate against Econt/Speedy delivery statuses.
- **Recommended funnel**, rebuilt in a sheet, GA4 or Looker Studio:
  1. Sessions (Shopify)
  2. Sessions with add-to-cart (Shopify)
  3. Branch:
     - 3a. COD form opened. Use EasySell InitiateCheckout, or a GTM click trigger on the "Поръчай" button sending a custom `cod_form_open` event.
     - 3b. Shopify checkout reached (Shopify)
  4. Branch:
     - 4a. COD form submitted = EasySell orders. Count them by order tag, source or payment gateway in Shopify admin.
     - 4b. Shopify checkout completed.
  5. Order confirmed (call, SMS or OTP)
  6. Shipped
  7. Delivered and paid (courier COD remittance)
  8. Separately: "call me back" leads, then call → order.
- **Before using InitiateCheckout as "form opened", verify it.** Watch Meta Events Manager → Test Events while opening and submitting the form. The Shopify checkout also fires InitiateCheckout, so the two paths mix in Meta unless EasySell uses a distinct event or parameter.

### Gaps
- No official Shopify document was found that explicitly says orders created by COD apps through the Admin API are excluded from "sessions that completed checkout". The evidence is the metric definitions plus merchant reports.
- No public EasySell documentation was found describing an in-app "form views → orders" report, or exactly when InitiateCheckout fires. This needs testing in the store.

---

## 2. Benchmarks for each funnel step (health/beauty, mobile, Shopify, COD/CEE)

### Takeaway
On all credible benchmarks, FitPatches' add-to-cart rate (10.8%) and placed-order conversion (5.7%) sit in or above the top decile. Shopify checkout completion (48%) is about average. Placed COD orders are not comparable with prepaid-order benchmarks, though: after typical COD refusals the gap shrinks. No credible public benchmark exists for one-page COD form conversion in CEE.

### Cited Findings
- **Littledata [IND]** — 2023 benchmark, 2,800 sites. Source: [Littledata – average website performance](https://www.littledata.io/average-website-performance)

  | Metric | Average | Top 20% | Top 10% | Mobile average | Mobile top 10% | Desktop average |
  |---|---|---|---|---|---|---|
  | Conversion rate | 1.4% | >3.2% | >4.7% | 1.2% | >3.9% | 1.9% |
  | Checkout completion | 45% | >59% | >66% | 44% | >64% | 49% |
  | Add-to-cart rate | 4.6% | >7.5% | >9.6% | – | – | – |

  Add-to-cart rate is 5.4% for fashion and 4.8% for food/beverage. Average AOV is $85.
- **Littledata via third-party summaries [SNIPPET, conflicting]** cite "12,000+ Shopify stores, median ATC 4.6%, average 7.0–8.5%, top 20% >11.5%". This does not match Littledata's own page (above); treat it as unverified. — [conversion.studio / blendcommerce search results](https://conversion.studio/blog/add-to-cart-rate)
- **Dynamic Yield [IND, DY client sites, trailing 12 months to August, viewed Oct 2026]** — add-to-cart. DY defines the metric as items added to cart after product page views, a different denominator from Shopify's session-based rate. Source: [DY add-to-cart benchmark](https://marketing.dynamicyield.com/benchmarks/add-to-cart-rate/)
  - Global: 6.09%
  - By device: mobile 6.37%, tablet 6.05%, desktop 5.13%
  - By region: EMEA 6.45%
  - Beauty & Personal Care: 9.56%, the highest industry
- **Dynamic Yield [IND]** — conversion rate. Source: [DY conversion-rate benchmark](https://marketing.dynamicyield.com/benchmarks/conversion-rate/)
  - Global: 2.71%
  - By device: mobile 2.88%, desktop 2.31%
  - By region: EMEA 2.86%
  - By industry: Beauty & Personal Care 5.39%, the highest
- **IRP Commerce / category benchmarks [SNIPPET, unverified]** — not opened at the primary source. Source: [convertcart / konvertiq search results](https://konvertiq.com/en/blog/ecommerce-conversion-rate-by-industry/)
  - IRP overall conversion: 2.26% in July 2026
  - Health & Wellness: median 3.31%, upper quartile 5.94%
  - Beauty & Personal Care: median 3.16%; add-to-cart 8.85%; cart abandonment 82.51%
- **Baymard [IND]** — documented average cart abandonment is **70.22%** across 50 studies. The latest data point is 71.72% (Uptain, 2025). — [Baymard cart abandonment stats](https://baymard.com/lists/cart-abandonment-rate)
- **Baymard [IND]** — "70% of ecommerce users abandon their purchase after adding items to their cart". 63% of mobile sites have "mediocre" or worse checkout UX. — [Baymard: Checkout UX 2025](https://baymard.com/research-articles/current-state-of-checkout-ux)
- **BEA Passport 2025 [IND, industry association]** — Bulgarian e-commerce is about €2.69bn in 2025, up about 15% year on year. The study ran Aug–Oct 2025 and covered more than 4.9m online orders. It reports growth in lockers, click & collect and card/bank/mobile payments at the expense of COD. — [BTA](https://www.bta.bg/bg/news/economy/1025127-onlayn-prodazhbite-na-produkti-i-uslugi-v-stranata-rastat-po-prognozni-danni-s-1); [Enterprise.bg](https://enterprise.bg/management/elektronnata-targoviya-v-balgariya-prodalzhava-da-raste-i-dostiga-blizo-2-7-mlrd-evro-obem-prez-2025-g)

### Inferences
- **Benchmark table for FitPatches**

  | Step | FitPatches | Benchmark | Read |
  |---|---|---|---|
  | Add-to-cart / session | 10.8% | Littledata avg 4.6%, top 10% >9.6%; DY mobile 6.37%, Beauty 9.56% | Top decile; the product page/offer works |
  | Cart → any order | ≤53% (implied abandonment ~47%) | Baymard abandonment avg 70% (so cart→order ~30%) | Well above average, mainly because of the COD form |
  | Shopify checkout completion | 48% | Littledata mobile avg 44%, top 10% >64% | Average. Only ~25% of orders use this path |
  | Placed orders / session | 5.7% | Littledata mobile avg 1.2%, top 10% >3.9%; DY mobile 2.88%, Beauty 5.39% | Top decile on placed orders, but placed COD ≠ paid |
  | Delivered orders / session | Unknown (~4.6–5.2% if 10–20% refused) | No credible public COD benchmark | Measure it |

- **Why the high numbers are plausible:** a single low-price hero product (€27.64 AOV), a COD form with no payment step, and Meta traffic aimed at a narrow audience. Benchmarks blend multi-SKU stores with lower intent per session. Benchmark sessions also count *paid* orders, while COD "orders" are promises to pay.
- **Biggest remaining upside:** probably not add-to-cart. It is (a) the ~47% of cart sessions with no order and (b) the share of placed orders that get refused.

### Gaps
- No credible, public benchmark was found for health/supplements on mobile from Meta traffic specifically, or for COD one-page form conversion in Bulgaria/CEE. App vendors do not publish per-market form-open→submit rates.
- IRP Commerce health & beauty figures were not verified at source.

---

## 3. Cart abandonment reasons (Baymard's current list) and which apply to COD shoppers

### Takeaway
Baymard's current list is led by extra costs (40%), slow delivery (20%), card-security distrust (19%), forced account creation (18%), and checkout length/complexity and site errors (17% each). COD forms remove the card, account and payment-method reasons. That leaves **surprise costs, delivery speed, form length, errors, returns/guarantee and not seeing the total upfront** as the main drivers for FitPatches. Hidden shipping cost before ordering is the most evidence-backed problem in its current setup.

### Cited Findings
- **Baymard [IND]** — reasons for abandoning during checkout. The base is US shoppers who abandoned in the last 3 months, excluding the 42% who were "just browsing / not ready to buy". Source: [Baymard cart abandonment stats](https://baymard.com/lists/cart-abandonment-rate)

  | Reason | Share |
  |---|---|
  | Extra costs too high (shipping, tax, fees) | 40% |
  | Delivery too slow | 20% |
  | Didn't trust site with credit card info | 19% |
  | Site required account creation | 18% |
  | Checkout too long/complicated | 17% |
  | Website errors/crashes | 17% |
  | Returns policy not satisfactory | 13% |
  | Couldn't see/calculate total order cost upfront | 12% |
  | Credit card declined | 10% |
  | Not enough payment methods | 9% |
  | Unknown | 7% |

  Note: older editions of this list (e.g., 39% extra costs, 18% "didn't trust the site") still circulate. Use the live page.
- **Baymard [IND, 2017 study]** — 64% of test users looked for shipping costs on the product page before adding to cart. 43% of sites show no shipping-cost information on product pages. Another survey had 21% of US shoppers abandoning because they "weren't able to see the total order cost upfront before initiating checkout". Baymard ranks the best ways to show cost as:
  1. Lowest flat rate
  2. IP-geo estimate
  3. Prior address
  4. A range

  It also notes that cost sensitivity is highest when shipping is large relative to a low product price. — [Baymard: show shipping costs on product pages](https://baymard.com/blog/show-shipping-costs-on-product-pages)
- **Baymard [IND]** — 18% abandoned because they refused to create an account. 62% of sites don't make guest checkout prominent enough. — [Baymard: Checkout UX 2025](https://baymard.com/research-articles/current-state-of-checkout-ux)
- **COD prevalence in Bulgaria:**
  - [IND/SNIPPET] COD is **50.30% of all payment types** in Bulgarian online commerce, per BEA data as cited in a search summary. — [Search result citing BEA (BTA / bia-bg.com)](https://www.bia-bg.com/news/view/35112/)
  - [IND, press] "about 55% still choose cash on delivery". — [Novinite](https://www.novinite.com/articles/232122/E-Commerce+Growth+in+Bulgaria+Fuels+Shift+from+Cash+on+Delivery+to+Seamless+Online+Payments)
  - The two figures likely use different bases: share of transactions versus share of shoppers.
- **[IND, ECDB]** In Bulgaria, COD is the number-one payment method and Speedy the leading shipping provider. — [ECDB Bulgaria](https://ecdb.com/resources/sample-data/market/bg/all)

### Inferences
- **Reasons and how they apply to a FitPatches COD shopper:**
  - **Extra costs / no total upfront (40% + 12%): applies strongly.** The EasySell form does not show shipping before the order. The courier and COD fees then appear at the door or in the confirmation call. That can cause abandonment before submitting and refusal at delivery. For a €27.64 product, a shipping fee of a few euros is a large share of the price, which is exactly the situation Baymard flags as most sensitive.
  - **Delivery too slow (20%): applies.** Show a concrete delivery date ("Доставка до петък, 10 окт."), not "1–3 работни дни".
  - **Card-security distrust (19%), declined card (10%), payment methods (9%): mostly removed by COD.** They are relevant only to the pink Shopify-checkout path.
  - **Account creation (18%): removed** by the COD form. Confirm that Shopify checkout is set to guest.
  - **Checkout too long (17%): partly applies.** The five-field form is short, but typing an address, postcode and city on a phone is the heaviest part.
  - **Site errors (17%): applies.** Test the form on popular Android browsers and in the in-app browsers of Facebook and Instagram.
  - **Returns policy (13%): applies as "guarantee".** For a supplement bought on impulse, a clear "if it doesn't suit you" promise is the COD equivalent.
- **COD-specific risks not on Baymard's list:** change of mind between order and delivery, ordering on impulse, and not being home or not picking up. These hit *delivered* orders rather than placed orders.

### Gaps
- No Bulgarian or CEE survey of abandonment reasons, or of COD-specific abandonment reasons, was found. Baymard's base is US shoppers.
- No independent split of Baymard's reasons by mobile versus desktop was found in this session.

---

## 4. Evidence for each lever (effect size, source type, placed vs delivered)

### Takeaway
The strongest *independent* evidence supports: showing the full cost including delivery before the order; keeping the form to about 7–8 fields with smart autofill; showing a delivery date; and a clear returns/guarantee promise. Evidence that COD forms beat checkout, and for OTP, upsells, trust badges and confirmation calls, is almost entirely vendor or anecdote. Shop Pay is available in Bulgaria, but its claimed lifts come from Shopify itself and are of little relevance when about 75% of orders choose COD.

### Cited Findings
- **One-step COD form vs multi-step checkout:**
  - [IND] Baymard: "the number of overall steps in the workflow isn't the most important or impactful aspect"; what matters is the number of visible fields. — [Baymard: checkout form fields (Jun 2024)](https://baymard.com/blog/checkout-flow-average-form-fields)
  - [VENDOR] EasySell homepage claims:
    - Demo section: "+38% conversions", "2.3s avg checkout"
    - Testimonials: "+35% conversion rate", "42% fewer abandoned orders"
    - Over 70,000 stores
    - Source: [EasySell](https://easysellapp.com/)
  - [VENDOR, testimonials] Releasit's site makes no numeric claim. Its testimonials say "Visible, dramatic increase in Conversion Rate versus standard Shopify checkout"; the app has 115,000+ stores. — [Releasit](https://www.releas.it/)
- **Number of form fields:**
  - [IND] Baymard's average checkout had 11.3 fields in 2024 (11.8 in 2021, 12.7 in 2019); the ideal is about 8. — [Baymard (Jun 2024)](https://baymard.com/blog/checkout-flow-average-form-fields)
  - [IND] Baymard's stats page gives a different count: an average of 23.48 form elements / 14.88 fields against an ideal of 12–14 elements / 7–8 fields. The counting method differs. Checkout design improvements alone could raise conversion by **35.26%** for large sites. — [Baymard](https://baymard.com/lists/cart-abandonment-rate)
  - [IND] 28% of mobile sites don't auto-detect city from postal code. Baymard recommends hiding "Address line 2" behind a link because 30% of test users paused at it. — [Baymard (Jun 2024)](https://baymard.com/blog/checkout-flow-average-form-fields)
  - [IND] 49% of sites don't explain why a phone number is required. 61% don't mark both required and optional fields. 94% don't use adaptive error messages. — [Baymard: Checkout UX 2025](https://baymard.com/research-articles/current-state-of-checkout-ux)
- **Show shipping cost and total upfront:**
  - [IND] 40% of abandoners cite extra costs; 12% couldn't see the total upfront. — [Baymard](https://baymard.com/lists/cart-abandonment-rate)
  - [IND] 64% look for shipping cost on the product page; 21% abandoned for not seeing the total cost upfront (2017). — [Baymard](https://baymard.com/blog/show-shipping-costs-on-product-pages)
- **Delivery date:**
  - [IND] Baymard recommends a date or date range ("Delivery on April 4th") instead of "delivery speed". 48% of sites don't do this; 83% don't show a cutoff-time countdown. — [Baymard: Checkout UX 2025](https://baymard.com/research-articles/current-state-of-checkout-ux)
  - [IND] 20% abandon over slow delivery. — [Baymard](https://baymard.com/lists/cart-abandonment-rate)
- **Econt/Speedy office picker:**
  - [IND] Baymard: 52% of sites don't show all fulfilment options. — [Baymard: Checkout UX 2025](https://baymard.com/research-articles/current-state-of-checkout-ux)
  - [IND, **2019, dated**] Pragmatica/Metrica survey: 52% of Bulgarians prefer to collect from a courier office and 47.5% prefer address delivery. In the same survey 48% used COD and 30% cards. — [Investor.bg (Oct 2019)](https://www.investor.bg/a/332-ikonomika-i-politika/290545-logistikata-nay-chesto-sreshtaniyat-problem-za-onayn-targovtsite)
  - [IND] BEA 2025 reports growing use of lockers and click & collect. — [Enterprise.bg](https://enterprise.bg/management/elektronnata-targoviya-v-balgariya-prodalzhava-da-raste-i-dostiga-blizo-2-7-mlrd-evro-obem-prez-2025-g)
  - [SNIPPET] Office delivery is cheaper: about 7.50 лв to an Econt office versus 9–12 лв to an address, and the COD fee is 0.94% at an office versus 1.8% at an address. Unverified. — [search result summary](https://www.sendaro.bg/blog/ekont-ili-spidi-za-onlain-magazin.html)
- **OTP/SMS verification:**
  - [VENDOR] EasySell: "One Shopify store documented a 40% drop in fake orders". Manual confirmation calls "drop by 60–70%". A 3–5% fall in order volume after adding OTP is "normal"; 15% or more means too much friction. Recommended only for COD, first-time customers, high-value orders or high-RTO zones. — [EasySell OTP article (Apr 2026)](https://easysellapp.com/blogs/wiki/shopify-cod-otp-verification-setup)
  - [VENDOR] EasySell homepage: "Reduce failed deliveries by up to 40%". — [EasySell](https://easysellapp.com/)
  - [BLOG/VENDOR, India] OTP gives a "20–30% reduction in fraudulent orders" and a "5–10 percentage point improvement in RTO". Average COD RTO is 28–35% versus 4–8% for prepaid. These are Indian-market figures from tool vendors and blogs, not peer-reviewed. — [eGrow RTO guide](https://www.egrow.com/en/blog/the-complete-guide-to-reducing-return-to-origin-rto-in-cod-e-commerce-2026); [bepragma.ai](https://www.bepragma.ai/blogs/how-to-reduce-rto-in-indian-e-commerce-without-hurting-cod-orders)
- **Phone-only order plus confirmation call:**
  - [BLOG, Bulgaria, Nov 2025, unsourced] SMS confirmation before shipping, a 10 BGN prepayment for high-risk orders and office-only delivery are said to give a "20 percent reduction in refusals over 30 days". The same post claims that refusals above 5% per month wipe out ad profit. No data source is given. — [bezraboten.net](https://bezraboten.net/onlayn-magazini-kak-da-namalite-otkazani-nalozheni-plashtaniya/)
- **Order bumps, upsells and quantity offers inside the form:**
  - [VENDOR] EasySell: "+30% AOV on average" from quantity offers. One testimonial claims "+28% revenue per order". — [EasySell](https://easysellapp.com/)
- **Trust badges:**
  - [IND] Baymard's perceived-security studies (2013–2023 editions) find that any visual security cue raises perceived security around payment fields. Well-known consumer brands' seals (Norton, Google) perform best, and "trust seals" beat SSL seals. — [Baymard: perceived security of payment form](https://baymard.com/blog/perceived-security-of-payment-form)
  - A circulating claim that badges lift conversion "15–30%" has no traceable primary source; treat it as unverified.
- **Guarantees / returns:**
  - [IND] 13% abandon over an unsatisfactory returns policy. — [Baymard](https://baymard.com/lists/cart-abandonment-rate)
  - [IND, BEA] 7.1% of Bulgarian online orders were refused or returned under the 14-day right of withdrawal in 2024. The search summary says this was 7.99% in 2023, with the highest category being clothing at 15%. — [Enterprise.bg](https://enterprise.bg/management/elektronnata-targoviya-v-balgariya-prodalzhava-da-raste-i-dostiga-blizo-2-7-mlrd-evro-obem-prez-2025-g)
- **Express checkout (Shop Pay, Apple/Google Pay):**
  - [IND, official] With Shopify Payments active in Bulgaria, Apple Pay, Google Pay and Shop Pay are available. — [Shopify Help – Bulgaria payment methods](https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries/bulgaria/payment-methods)
  - [VENDOR, Shopify about itself] Shop Pay "lifts conversion by up to 50% compared to guest checkout" and outpaces other accelerated checkouts by at least 10%.
  - [VENDOR] Shopify checkout "converts up to 36% better… average 15%", per a consulting-firm study commissioned by Shopify.
  - [VENDOR] Shopify also claims that the mere presence of Shop Pay raises lower-funnel conversion by 5%.
  - Sources: [Shopify blog – Shop Pay](https://www.shopify.com/blog/shop-pay-checkout); [BetaKit](https://betakit.com/shopify-claims-best-conversion-rates-among-checkout-solutions-on-the-market/)

### Inferences — ranked levers between add-to-cart and a delivered COD order
Ranking is by strength of evidence × relevance to FitPatches. "Placed" = raises submitted orders. "Delivered" = raises the share of orders that are paid for.

| # | Lever | Best evidence and effect size | Source type | Raises |
|---|---|---|---|---|
| 1 | **Show shipping cost and total (incl. COD fee) in the cart drawer and form before submit**, e.g. "Доставка до офис на Еконт: X € · Общо: Y €" | 40% of abandoners cite extra costs; 12–21% cite not seeing the total; 64% look for shipping on the product page | IND (Baymard) | Placed (fewer abandons). **Likely also delivered**, because there is no price surprise at the door (inference, no direct study) |
| 2 | **Measure delivered orders and feed them back to Meta** (Section 5) | Meta CAPI accepts events up to 7 days old; avoids optimising toward refused orders | IND (Meta docs) + reasoning | Delivered (and ad efficiency) |
| 3 | **Shorter, smarter form**: office picker as an alternative to street address, postcode→city autofill, explain why the phone is needed ("за куриера"), numeric keypad for phone | Ideal ~7–8 fields; 28% of mobile sites lack postcode autofill; 49% don't explain the phone field; steps matter less than fields | IND (Baymard) | Placed. Office delivery **may** help delivered (cheaper, collected at the shopper's convenience); only 2019 preference data and unverified prices |
| 4 | **Concrete delivery date** in the cart and form | 20% abandon over slow delivery; 48% of sites don't show a date | IND (Baymard) | Placed. Plausibly delivered (shorter window to change one's mind), unproven |
| 5 | **Guarantee / easy-return promise** next to the button | 13% abandon over returns policy; BEA 7.1% 14-day returns baseline | IND | Placed. Effect on refusals unknown |
| 6 | **Keep the COD form as the primary CTA** (already orange "Поръчай" on top) | COD is ~50–55% of Bulgarian payments; 75% of FitPatches orders already use it. Uplift claims for COD forms are vendor-only (+35–38%) | IND for COD preference; VENDOR for uplift | Placed |
| 7 | **Confirmation call/SMS before shipping** | Only unsourced blog claims (~20% fewer refusals); vendor says calls fall 60–70% with OTP | BLOG/VENDOR | Delivered (cuts fakes and changed minds); small risk to placed |
| 8 | **OTP verification** (only for risky segments) | Vendor: −40% fake orders (one store), "up to 40%" fewer failed deliveries; cost of 3–5% fewer placed orders; India RTO data not transferable | VENDOR | Delivered ↑, placed ↓. Use only if fake or duplicate orders are a measured problem |
| 9 | **Quantity offers / bumps in the form** (e.g. 2 packs) | Vendor "+30% AOV" | VENDOR | Revenue per order. Effect on refusal rate unknown (a higher COD amount could raise refusals; untested) |
| 10 | **Trust badges** | Raise *perceived* security of card fields; little relevance when there is no card entry | IND (Baymard), indirect | Marginal for COD |
| 11 | **Shop Pay / Apple Pay / Google Pay** | Shopify's own claims (up to +50% vs guest checkout); no Bulgarian Shop Pay adoption data | VENDOR | Placed and prepaid share on the minority card path. Prepaid orders cannot be refused at the door |
| 12 | **Name+phone "call me back" form** | No evidence found | — | Unknown. Track as a separate lead funnel |

- **Two-button cart drawer.** With 75% of orders on COD, keeping COD as the visually dominant CTA is consistent with the data. A test worth running is whether the pink Shopify button pulls clicks from people who then abandon: 83 of 160 Shopify-checkout sessions did not complete.

### Gaps
- No independent A/B test or academic study was found comparing a COD popup form with Shopify's multi-step checkout. All uplift numbers are vendor or testimonial.
- No independent data was found on: confirmation calls, OTP, office-vs-address delivery, or upsell size and their effect on *refusal* rates in Bulgaria.
- No evidence was found for "name + phone only" quick forms or callback forms.
- No peer-reviewed checkout-friction paper from 2023–2026 was retrieved in this session.

---

## 5. Measuring: form opens vs submits, Meta pixel/GA4, refusal (RTO) rates, optimising for delivered orders

### Takeaway
Track "COD form opened → submitted" with EasySell's InitiateCheckout/Purchase pixel events (verify when each fires) or a GTM click event. Pull refused-parcel rates from Econt/Speedy shipment statuses, not from Shopify. Then send *delivered* orders back to Meta through the Conversions API within 7 days. Bulgarian refusal benchmarks are weak: the best public anchor is BEA's 7.1% for 14-day returns, and practitioner estimates for refusals range from 5% to 20% by category.

### Cited Findings
- **[VENDOR doc]** EasySell's Meta pixel fires InitiateCheckout, Purchase or Lead; gtag fires InitiateCheckout and Purchase. The timing is not documented. — [Tyslo/EasySell help](https://help.tyslo.com/en/article/how-to-add-tracking-pixels-to-easysell-laiv2w/)
- **[VENDOR]** Duplicate pixels (theme plus EasySell) double-count purchases and inflate ROAS. — [EasySell setup guide](https://easysellapp.com/blogs/wiki/easysell-setup-guide-get-started-15-minutes-2026)
- **[IND, Meta developer docs]**
  - "The event_time can be up to 7 days before you send an event to Facebook". Events older than 7 days cause the whole request to fail.
  - "All action sources enable ad optimization capabilities."
  - Source: [Meta Conversions API – server event parameters](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/server-event)
- **[BLOG/VENDOR]** In COD, many submitted orders are never confirmed or delivered, so browser-pixel Purchases overstate sales. Sending confirmed or delivered orders through CAPI gives Meta "a more meaningful conversion to optimize toward". — [MyLeadDone: CAPI for COD](https://www.myleaddone.com/blog/meta-conversions-api-cod/)
- **[BLOG]** Standard events (e.g., Purchase) get better optimisation than custom events. This is a practitioner view, not a Meta statement. — [adsuploader](https://adsuploader.com/blog/meta-conversions-api); [Jon Loomer](https://www.jonloomer.com/differences-between-custom-events-and-custom-conversions/)
- **Bulgarian refusal and return rates:**
  - [IND] BEA: 7.1% of 2024 online orders were refused or returned within the 14-day window. — [Enterprise.bg](https://enterprise.bg/management/elektronnata-targoviya-v-balgariya-prodalzhava-da-raste-i-dostiga-blizo-2-7-mlrd-evro-obem-prez-2025-g)
  - [BLOG, author estimates, "indicative"] Refusal rates by category: fashion 15–25%, cosmetics 5–10%, electronics 3–8%, household 8–15%, sports/fitness 10–18%. COD fees run about 0.80–2 BGN plus 1–2%; each refusal costs about 15–24 BGN plus tied-up capital. — [XLOG.BG (2026)](https://xlog.bg/nalozhen-platezh-za-onlayn-magazini/)
  - [SNIPPET] "5–15% of shipments won't be collected". — [search summary of BG merchant guides](https://bizzupp.bg/blog/nalozhen-platezh-za-onlain-magazini)
  - [BLOG/VENDOR, India] COD RTO is 28–35% versus 4–8% for prepaid. This is not transferable to Bulgaria. — [eGrow](https://www.egrow.com/en/blog/the-complete-guide-to-reducing-return-to-origin-rto-in-cod-e-commerce-2026)

### Inferences
- **Form-open → submit rate:**
  - In Meta Ads Manager or Events Manager, compare EasySell InitiateCheckout against EasySell Purchase.
  - Shopify checkout also fires InitiateCheckout, so either (a) split by `content_name`/URL or another parameter, or (b) add a GTM listener on the "Поръчай" button that sends a custom event (`cod_form_open`) to GA4 and Meta.
  - In GA4, build a funnel exploration: `session_start` → `add_to_cart` → `cod_form_open` / `begin_checkout` → `purchase`. EasySell's gtag "InitiateCheckout" is not GA4's recommended `begin_checkout` name, so it may need mapping in GTM.
  - Track the callback form as `generate_lead`.
- **Delivered-order rate:**
  - Export Econt/Speedy shipment statuses (delivered/paid versus refused or returned to sender) weekly and join them to Shopify orders.
  - Report: placed → confirmed → shipped → delivered.
  - Compute refusal rate = returned-to-sender ÷ shipped.
  - Report it separately for EasySell, Shopify checkout and callback-form orders, and by ad set or creative where UTMs or pixel data allow.
- **Optimising Meta for delivered orders:**
  - Bulgarian delivery usually completes within the 7-day CAPI window. Delivered or paid orders can therefore be sent server-side, either as the Purchase event (with the browser Purchase turned off or renamed to avoid double counting) or as a separate event or custom conversion.
  - Trade-off: fewer optimisation events. 324 orders in 90 days is about 25 per week; delivered orders will be fewer. That may be too thin for some ad sets, so a common compromise is to optimise on placed Purchase but *report* ROAS on delivered.
  - Meta's commonly cited learning-phase guideline of about 50 events per week was not verified in this session.
- **Break-even refusal rate:**
  - With AOV €27.64, each refusal costs roughly €8–12 (XLOG's 15–24 BGN estimate) plus wasted ad cost (CPA).
  - Compare refusal rate × (CPA + return shipping) against the margin on delivered orders.

### Gaps
- No official Econt or Speedy statistics were found on refused COD parcels, nationally or by category.
- BEA's 7.1% covers 14-day returns and refusals together; it is not a COD-door-refusal rate.
- EasySell's exact event timing, and whether it supports CAPI deduplication with Shopify's Meta channel, was not confirmed from documentation.
- No independent study was found showing that delivered-order CAPI optimisation improves Meta performance for COD stores. The evidence is vendor or practitioner reasoning.
