# Global DTC supplement / wellness / beauty brands: cart → checkout flows on mobile (teardown + transferable patterns for a COD market)

Method note (applies to every section): Between 02-Oct-2026 ~12:05 and ~13:30 UTC I walked live US mobile flows with Playwright (Chromium, iPhone 13 viewport, en-US, US exit IP). I added to cart, opened the cart, clicked through to checkout, and stopped at the empty checkout form. I entered no data and placed no orders. "Observed" bullets cite the live page I walked. The screenshots and the full text dumps are in the session scratchpad at `/tmp/claude-0/-home-user-fitpatches-ads/77d5f012-1d96-5267-aa86-a2c530bc0277/scratchpad/shots/` (prefix `co-gl-`; contact sheets are `co-gl-*-sheet-co.png` and `co-gl-row-*.png`). Caveats:
- Chromium cannot render Apple Pay, so Apple Pay buttons never show in these captures. Real iPhone users would see them.
- Express-checkout buttons sometimes appear only as grey loading skeletons in the screenshot.
- The script-tag app detection covers only scripts present in the PDP DOM, so it is not exhaustive.
- Brands covered (10): Kind Patches, Lemme, Ritual, Seed, Bloom Nutrition, Olaplex, Glossier, Gymshark, Huel, and AG1 (secondary sources only, because the site blocked automation).
- Hims & Hers was excluded because its flow is a telehealth intake, not a cart.

## 1. Per-brand mobile teardown: cart → checkout → confirmation

### Takeaway
Of the 8 brands whose checkout I reached, all 8 hand off to native Shopify one-page checkout. That includes the headless storefronts: Gymshark (us.checkout.gymshark.com) and Seed (checkout.seed.com). The differentiation happens in the cart drawer:
- tiered progress bars,
- subscription and cadence upgrades,
- auto-added gifts and free samples,
- one cross-sell block,
- a single dominant checkout CTA, often with the total inside the button.

Checkout pages differ mostly in light branding, which fields are optional, trust blocks, and the payment-method mix.

### Cited Findings

**Kind Patches (patches; closest analogue to FitPatches; product walked: Berberine Patches 3-Pack)**
- PDP: the default option is "Subscribe & Save – SAVE 43% – ~~$45.00~~ $25.50, Ships every 30 days", with bullets "Extra 15% off every month / Free shipping on every order / Skip, pause or cancel anytime". The ATC button shows the price inside: "Add to Cart | $25.50". The announcement bar reads "BUY 2, GET 1 FREE + UP TO 50% OFF BUNDLES" — [kindpatches.com PDP, observed](https://kindpatches.com/products/berberine-patches-formerly-glp-1-3-pack)
- Cart:
  - A slide-out drawer opens automatically after ATC (UpCart).
  - The drawer header has a tier bar reading "Max savings unlocked 🎉" with the milestone "Buy 2 Get 1 FREE!".
  - The bundle is split into component lines: 2 paid units plus 1 unit at $0.00, each labelled "Ships every 30 days with 15% discount".
  - The auto discount shows as a pill: "KIND BUNDLE & SAVE −$12.75".
  - There is one dark full-width CTA, "CHECKOUT • $25.50", with the total inside the button.
  - No express-wallet buttons were visible in the drawer.
  - The /cart page says "Shipping calculated at checkout." — [kindpatches.com, observed](https://kindpatches.com/products/berberine-patches-formerly-glp-1-3-pack)
- Checkout (Shopify one-page, kindpatches.com/checkouts/cn/…):
  - The header is branded: logo, a pink pill "4+ Million Patches Sold", and "30 Day Money Back Guarantee · As Seen In Vogue & Forbes".
  - The order summary is collapsed and shows the struck-through price ($38.25 → $25.50).
  - Express buttons: Shop Pay, PayPal, G Pay.
  - A 5-star customer review card ("Burn Naturally… – Elizabeth, Verified buyer") sits directly under the express buttons.
  - Fields: email with the marketing box pre-checked; country, first, last, address, apt (optional), city, state, ZIP; phone required, with SMS opt-in unchecked.
  - Shipping methods appear only after the address is entered.
  - Payment: card or PayPal.
  - The total block shows "Total savings $12.75" and "Recurring subtotal $38.25 every 30 days".
  - The final button reads "Review order".
  - An in-checkout cross-sell, "Don't miss these bestsellers", offers 3 products with "Add" buttons and star ratings.
  - A trust icon row closes the page: "3-6 Day Shipping / Secure Payments / 30-Day Money Back Guarantee".
  — [Kind Patches checkout, observed](https://kindpatches.com/products/berberine-patches-formerly-glp-1-3-pack) (screenshot `co-gl-kind-sheet-checkout.png`)

**Lemme (gummies / capsules; product walked: Lemme Burn)**
- Cart (Rebuy Smart Cart flyout):
  - Top strip: "Free Lemme Play for Subscription Orders $55+".
  - Multi-tier bar: "Free Shipping ✓" then "Lemme Shroom Lollipops (GWP)", with the copy "Add $32 to unlock 1 Free Lemme Immunity Gummies Pack On Any Order".
  - Each line shows the sale price, the original price, and the auto-applied code (FALLKICKOFF25).
  - Each line has a subscription selector: "One-time only / Subscribe & Save every 4 / 8 / 12 weeks", plus a "Subscribe & Save 15%" option.
  - Single cross-sell block: "Throw In One Of Our Bestsellers" (one product + ADD).
  - Summary: Subtotal $70 / "Total savings −$26" / "Taxes: Calculated at checkout" / "SUBTOTAL [37% OFF] $44 ~~$70~~".
  - One lime full-width "CHECKOUT" button.
  - A trust strip under the CTA: "Expert formulated / Validated by 3rd party testing / Thousands of 5-star testimonials ★★★★★", plus subscription billing disclosure text.
  - The drawer markup contains `additional-checkout-buttons`, but no wallet buttons were visible.
  — [lemmelive.com, observed](https://lemmelive.com/products/lemme-burn-gummies)
- PDP: a "lemme get the full routine" bundle builder with "Add Bundle to Cart" (TOTAL PRICE ~~$70~~ $62) and one-time add-on checkboxes — [lemmelive.com PDP, observed](https://lemmelive.com/products/lemme-burn-gummies)
- Checkout (Shopify one-page):
  - Minimal branding (logo only).
  - Express buttons (signals for Shop Pay, PayPal, Google Pay; Affirm present).
  - Email marketing consent pre-checked.
  - The Address field has the autocomplete magnifier.
  - "Phone (required outside of USA)".
  - Two separate "I agree to the following agreement" subscription checkboxes plus a Terms / Consumer Health Data checkbox. The page showed the banner "Agreement must be checked to proceed".
  - "Recurring subtotal $28.00 every 4 weeks"; the button reads "Pay now".
  — [Lemme checkout, observed](https://lemmelive.com/products/lemme-burn-gummies) (`co-gl-lemme-sheet-co.png`)

**Ritual (vitamins; product walked: Women's Multivitamin 18+)**
- PDP: "Buy More, Save More: New subscribers save 20% on 1 item—up to 30% when you bundle 3+ different items". Also "HSA/FSA eligible" and subscriber perks ("Save 12% on every order", "Free shipping, no minimums") — [ritual.com PDP, observed](https://ritual.com/products/essential-for-women-multivitamin)
- After ATC, no drawer opens first. Instead:
  - a green toast: "Women's Multivitamin 18+ added to cart",
  - then a full-screen upsell sheet: "Add Synbiotic+ and save 25% on your entire bundle", with product image, 3 benefit bullets, and the CTA "Add to cart $43.20 ~~$54.00~~".
  — [ritual.com, observed](https://ritual.com/products/essential-for-women-multivitamin) (`co-gl-row-atc1.png`)
- Cart drawer:
  - Top strip: "You're saving $7.80 on your order".
  - "Add 1 more product to unlock 25% off", with a progress bar.
  - Lines are grouped by "Delivered every 30 days" and "Delivered once", with struck-through prices and a "$7.80 savings" line.
  - "You may also like" cross-sell.
  - One navy "Checkout" button.
  - A hidden sub-panel, "Select Shipping Method – Your new item can ship with an upcoming order", serves existing subscribers.
  — [ritual.com, observed](https://ritual.com/products/essential-for-women-multivitamin)
- Checkout (Shopify one-page):
  - Fully re-skinned in brand colours and fonts.
  - Express: Shop Pay, PayPal, G Pay.
  - "Use Store Credits" block.
  - "First name (optional)"; no phone field at all.
  - Address autocomplete.
  - Payment: card or PayPal.
  - Under "Pay now", three guarantee blocks: "30 Day Money-Back Guarantee / Your Ritual, Your Way (flexible delivery, anytime cancellation) / Subscriptions Ship Free".
  — [Ritual checkout, observed](https://ritual.com/products/essential-for-women-multivitamin) (`co-gl-ritual-sheet-co.png`)

**Seed (probiotics; headless storefront; product walked: DS-01 Daily Synbiotic)**
- The PDP "Get Started" button leads to a /products chooser with an "Add To Cart" button per product — [seed.com, observed](https://seed.com/daily-synbiotic)
- Cart drawer (custom React):
  - Banner: "Save 25% when you add another product".
  - The line reads "Delivered monthly $49.99". A cadence upsell follows: "Save 10% on 3 Month Delivery – Upgrade".
  - An auto-added gift line: "Glass Travel Vial – Bonus gift – FREE".
  - A "Bundle + Save 25%" carousel (e.g., DM-02 $29.99 ~~$39.99~~ [Add]).
  - A collapsed "Apply Promo Code" link.
  - "Total $49.99 – Shipping + taxes calculated at checkout".
  - One "Checkout" button.
  — [seed.com/products, observed](https://seed.com/products) (`co-gl-row-d2.png`)
- Checkout (Shopify, on checkout.seed.com):
  - Brand palette.
  - Express: Shop Pay, G Pay.
  - The express disclaimer bundles marketing consent ("You also agree to receive news and offers from Seed").
  - Phone required (SMS opt-in unchecked); address autocomplete.
  - Required checkbox "I agree to the Subscription Terms and Conditions…".
  - Trust row under "Pay now": "30-day money-back guarantee / Cancel anytime, no strings attached / Free US shipping included on every order".
  — [Seed checkout, observed](https://seed.com/products) (`co-gl-seed-sheet-co.png`)

**Bloom Nutrition (powders / gummies; product walked: Creatine Gummies)**
- After ATC, a full-screen gamified pop-up appears: "You've got a mystery discount", with a 0:55 countdown and quiz buttons (Fitness Fuel / Gut Health / Energy Boost / I'm not sure!) — [bloomnu.com, observed](https://bloomnu.com/products/creatine-gummies)
- Cart drawer:
  - "Your bag (1 item)", with the free-shipping bar "You're $30.01 away from your Free Shipping".
  - The line has an inline "Subscribe and save 15% →" upgrade button and a "Why subscribe?" accordion.
  - "Pick 1 free sample 0/1" (three free single-serve sticks to choose from).
  - "Picked just for you" cross-sell carousel.
  - Total; one black "🔒 Secure Checkout" button; "★★★★★ 30,000+ five-star reviews" under the CTA.
  — [bloomnu.com, observed](https://bloomnu.com/products/creatine-gummies)
- Checkout (Shopify one-page):
  - Brand colours and fonts.
  - Express: Shop Pay, PayPal.
  - Email opt-in pre-checked.
  - "First name (optional)", "Phone (optional)"; address autocomplete.
  - The free-shipping progress bar is repeated inside the checkout order summary ("YOU'RE $30.01 AWAY FROM FREE SHIPPING!").
  - Loyalty login "Log in to Shopify – powered by tyb" and "Earn and redeem Bloom Nutrition rewards".
  - Payment: card, Shop Pay ("Pay in full or in installments"), PayPal, Sezzle.
  — [Bloom checkout, observed](https://bloomnu.com/products/creatine-gummies) (`co-gl-bloom-sheet-co.png`)

**Olaplex (haircare)**
- Cart drawer ("SHOPPING CART"):
  - Gift-with-purchase bar: "You are $41.00 away from a free Gift. Use code: STYLE".
  - Line item with the link "UPGRADE TO SUBSCRIPTION & SAVE 10%".
  - Discount-code field.
  - "CHECKOUT • $34.00", followed by three wallet buttons inside the drawer: PayPal, Shop Pay, G Pay.
  - This is the only brand that showed express wallets in the cart.
  — [olaplex.com, observed](https://olaplex.com/products/olaplex-n-9-bond-protector-nourishing-hair-serum-90ml)
- Checkout (Shopify one-page):
  - Logo only.
  - Express buttons.
  - "Company (optional)" field; phone required.
  - Payment: card, Shop Pay (installments), PayPal, Klarna.
  - Order summary shown; "Pay now".
  — [Olaplex checkout, observed](https://olaplex.com/products/olaplex-n-9-bond-protector-nourishing-hair-serum-90ml) (`co-gl-olaplex-sheet-co.png`)

**Glossier (beauty)**
- PDP: "or 4 interest-free payments of $4.00 with Afterpay" and a "SAVE WITH SETS" block. An email pop-up for 15% off ("Join the list") intercepted the first ATC tap — [glossier.com PDP, observed](https://www.glossier.com/products/balm-dotcom)
- Cart drawer ("SHOPPING BAG"):
  - "$24 away from free standard shipping" bar.
  - Per-line dropdown "One-time purchase / Ship every 1–5 months".
  - "BUNDLE + SAVE – Save on Lip Line – You save 11% by bundling with items in your bag".
  - "All orders receive a free sample of You!" plus "NEW Add a free sample" (a picker with 7 samples).
  - "Subtotal / Tax calculated in checkout / Shipping and promotions calculated in checkout / Estimated total $16.00".
  - One black "Checkout" button.
  — [glossier.com, observed](https://www.glossier.com/products/balm-dotcom) (`co-gl-row-d3.png`)
- Checkout (Shopify one-page):
  - Express: Shop Pay, PayPal, G Pay, Venmo.
  - Ship / Pick Up toggle.
  - "Apt / Floor / Suite"; phone required (with a help tooltip); SMS opt-in unchecked.
  - "Please allow 1-3 business days processing time".
  - "Gift Options – Add a gift message".
  - Brand-ritual opt-in "Would you like a free Pink Pouch?".
  - Payment: card, Shop Pay, PayPal, Afterpay.
  - The CTA is labelled "Place Order".
  — [Glossier checkout, observed](https://www.glossier.com/products/balm-dotcom) (`co-gl-glossier-sheet-co.png`)

**Gymshark (fitness apparel; headless storefront)**
- Cart drawer ("YOUR BAG"):
  - "You're $19 away from Free Standard Shipping", with a $0–$75 bar.
  - Scarcity note: "Your items aren't reserved, checkout quickly to make sure you don't miss out."
  - Delivery options with costs and ETAs: "Standard $5 – Estimated 5-8 working days – Free over $75; Express $15 – Estimated 5 working days".
  - "Free 30-day returns".
  - "ADD A LITTLE EXTRA – Add one or more of these items to get free delivery" (a threshold-targeted cross-sell carousel).
  - Discount-code field.
  - Order summary that shows **Estimated Shipping $5** and **Total $61** before checkout.
  - Sticky "🔒 Checkout securely" plus payment-logo row: Visa, MC, PayPal, Apple Pay, Klarna, Amex, Afterpay, Sezzle.
  — [gymshark.com, observed](https://www.gymshark.com/products/gymshark-power-satchel-bags-black-aw26) (`co-gl-row-gym.png`)
- Checkout (Shopify on us.checkout.gymshark.com):
  - Logo and font only.
  - Express: Shop Pay, PayPal, G Pay, Venmo.
  - No visible email marketing box.
  - "Address Line 1" field with autocomplete; phone required.
  - Payment: card, PayPal, Klarna, Afterpay, Cash App Pay, Sezzle; "Pay Now".
  — [Gymshark checkout, observed](https://www.gymshark.com/products/gymshark-power-satchel-bags-black-aw26) (`co-gl-gymshark-sheet-co.png`)

**Huel (meal shakes; Next.js on Vercel, not a Shopify theme)**
- PDP is a flavour builder with +/– steppers per flavour. The primary CTA is subscription-first: "Add to subscription | $105" — [huel.com PDP, observed](https://huel.com/products/huel-black-edition)
- After ATC, an "Added to your cart" bottom sheet appears:
  - Two-tier bar: "FREE" delivery at $65 ✓, then "−10%" at $120.
  - "Get 10% off when you spend $15 more".
  - "Meal prep made simple" cross-sell with "Add to subscription".
  - "Go to cart".
- Cart:
  - Per-line delivery frequency (2/4/6/8 weeks) and an "Unsubscribe" option.
  - "Welcome Kit $40 FREE" (shaker, t-shirt and scoop for new customers).
  - "Estimated: 210 Huel+ points".
  - "You'll love this" cross-sells.
  - Summary: "Subtotal $135 / Discount Automatic −$30 / Shipping FREE / Total $105 / Discount codes applied at checkout".
  - "Secure Checkout".
  — [huel.com, observed](https://huel.com/products/huel-black-edition) (`co-gl-row-huel.png`)
- Checkout was not reached: a cookie-consent centre intercepted the click, and I stopped there.

**AG1 (greens powder) — blocked; secondary sources only**
- drinkag1.com served a "Vercel Security Checkpoint" page to Playwright and returned HTTP 429 to the fetch tool, so the walk was impossible — [drinkag1.com, observed block](https://drinkag1.com/en-us)
- Secondary sources on the PDP and offer:
  - "Subscribe button is primary. One-time is secondary. 90-day money-back guarantee lives right below CTA" — [vms.nik.co teardown](https://vms.nik.co/)
  - The welcome kit (shaker, canister, scoop, travel packs) is used as the first-subscription incentive — [vms.nik.co](https://vms.nik.co/); [AG1 search result / drinkag1.com](https://drinkag1.com/ag1-membership)
- AG1 runs modular ad landers whose URLs encode the modules (e.g., `/landers/custom_Offer Anchor/Offer-price-builder/testimonials-…/replacement-value-chart-…`) — [drinkag1.com lander URL](https://drinkag1.com/landers/custom_Offer%20Anchor/Offer-price-builder/testimonials-primary-general/customer-reviews-review-blocks-broad-appeals/how-to-use-gallery-general/closing-hook-text-general/replacement-value-chart-general/dietary-list-checks-stone-background/hero-half-healthy-aging/2480)
- Platform: Anatta (agency) built a headless PWA for Athletic Greens. The agency claims a 2.8% conversion increase and a 10x increase in subscriptions; these are agency-reported numbers — [Anatta case study](https://anatta.io/case-study/athleticgreens)
- A search snippet said AG1 runs Shopify Plus with Recharge. I did not verify this against a primary source.
- Pricing ("$79/30-day subscription vs $99 one-time + $9 shipping") appeared only in search snippets. The source page returned 404, so this is unverified.

### Inferences
- Shopify one-page checkout is effectively the industry default even for headless brands. The cart drawer, not the checkout, is where these brands compete.
- Every brand I reached except Olaplex shows one primary checkout action in the cart. Olaplex adds three wallet buttons under it; Gymshark shows wallets only as logos. None stacks two differently coloured primary CTAs the way FitPatches' drawer does (orange COD "Поръчай" over pink "Преминаване към плащане").

### Gaps
- Thank-you pages and post-purchase one-click upsells could not be observed without placing orders.
- The Apple Pay button is invisible in Chromium.
- AG1 was blocked, and Huel's checkout was not reached.
- Ritual's drawer contained a Prenatal subscription line I did not add. It came from page state I could not explain, so I treated only the structure as evidence.
- On Lemme and Olaplex, the generic script clicked a bundle or recommended-product ATC rather than the main PDP button. The cart structure is still representative.

## 2. Cart: drawer vs page and what is inside

### Takeaway
All 10 brands use an overlay cart (side drawer or bottom sheet), and two (Ritual, Huel) add a post-ATC interstitial upsell before the cart. The near-universal building blocks are:
- a threshold or tier progress bar (9 of 9 observed carts),
- a single cross-sell or bundle block,
- a subscription or cadence upgrade on the line item,
- a free gift or sample,
- the subtotal with savings made explicit,
- one full-width checkout CTA.

Showing actual shipping cost and a delivery ETA in the cart is rare: only Gymshark (and Huel, as "Shipping FREE") did it.

### Cited Findings
- **Drawer vs page:** an overlay opened on ATC at Kind, Lemme, Bloom, Glossier, Olaplex, Gymshark, Seed and Huel (bottom sheet, then a cart drawer). Ritual showed a toast plus a full-screen upsell sheet first — [observed sites above](https://kindpatches.com/products/berberine-patches-formerly-glp-1-3-pack)
- **Progress / threshold bars (9/9 carts observed):**

  | Brand | What the bar unlocks |
  |---|---|
  | Kind | "Buy 2 Get 1 FREE" tier |
  | Lemme | free shipping, then a GWP |
  | Ritual | 25% off at 2+ products |
  | Seed | 25% off when adding another product (banner) |
  | Bloom | free shipping |
  | Olaplex | free gift via a code |
  | Glossier | free shipping |
  | Gymshark | free shipping at $75 |
  | Huel | free delivery at $65, −10% at $120 |

  Sources: [Kind](https://kindpatches.com/products/berberine-patches-formerly-glp-1-3-pack); [Lemme](https://lemmelive.com/products/lemme-burn-gummies); [Ritual](https://ritual.com/products/essential-for-women-multivitamin); [Seed](https://seed.com/products); [Bloom](https://bloomnu.com/products/creatine-gummies); [Olaplex](https://olaplex.com/products/olaplex-n-9-bond-protector-nourishing-hair-serum-90ml); [Glossier](https://www.glossier.com/products/balm-dotcom); [Gymshark](https://www.gymshark.com/products/gymshark-power-satchel-bags-black-aw26); [Huel](https://huel.com/products/huel-black-edition)
- **Upgrade the same item (rather than add another SKU):**
  - Seed: "Save 10% on 3 Month Delivery – Upgrade".
  - Olaplex: "Upgrade to subscription & save 10%".
  - Bloom: "Subscribe and save 15% →".
  - Lemme and Glossier: per-line one-time/subscription dropdowns.
  - Huel: per-line frequency.
  - Kind: subscription preselected on the PDP; the 3-pack is a bundle line.
  — [Seed](https://seed.com/products); [Olaplex](https://olaplex.com/products/olaplex-n-9-bond-protector-nourishing-hair-serum-90ml); [Bloom](https://bloomnu.com/products/creatine-gummies); [Lemme](https://lemmelive.com/products/lemme-burn-gummies); [Glossier](https://www.glossier.com/products/balm-dotcom); [Huel](https://huel.com/products/huel-black-edition); [Kind](https://kindpatches.com/products/berberine-patches-formerly-glp-1-3-pack)
- **Cross-sell (usually one block):** Lemme "Throw In One Of Our Bestsellers" (1 product); Ritual "You may also like"; Seed "Bundle + Save 25%"; Bloom "Picked just for you"; Glossier "Bundle + Save"; Gymshark "Add a little extra… to get free delivery" (tied to the threshold); Huel "You'll love this". Sources: same pages as above.
- **Gift-with-purchase / free sample:**
  - Seed: auto-added "Glass Travel Vial – Bonus gift – FREE".
  - Lemme: GWP tiers (Lollipops, then Immunity Gummies).
  - Bloom: "Pick 1 free sample".
  - Glossier: "free sample of You!" plus a sample picker.
  - Huel: "Welcome Kit $40 FREE".
  - Olaplex: "free Gift" at a threshold.
  - AG1: welcome kit (secondary source).
  — [Seed](https://seed.com/products); [Lemme](https://lemmelive.com/products/lemme-burn-gummies); [Bloom](https://bloomnu.com/products/creatine-gummies); [Glossier](https://www.glossier.com/products/balm-dotcom); [Huel](https://huel.com/products/huel-black-edition); [Olaplex](https://olaplex.com/products/olaplex-n-9-bond-protector-nourishing-hair-serum-90ml); [vms.nik.co on AG1](https://vms.nik.co/)
- **Savings line:**
  - Kind: discount pill "−$12.75".
  - Lemme: "Total savings −$26" and "37% OFF $44 ~~$70~~".
  - Ritual: "You're saving $7.80 on your order".
  - Huel: "Discount Automatic −$30".
  - Seed and Glossier: struck-through bundle prices.
  — sources as above
- **Trust / reviews in the cart:**
  - Lemme: 3 trust icons plus "Thousands of 5-star testimonials" under the CTA.
  - Bloom: "30,000+ five-star reviews" under the CTA.
  - Gymshark: "Free 30-day returns" plus payment logos.
  — [Lemme](https://lemmelive.com/products/lemme-burn-gummies); [Bloom](https://bloomnu.com/products/creatine-gummies); [Gymshark](https://www.gymshark.com/products/gymshark-power-satchel-bags-black-aw26)
- **Shipping transparency in the cart:**
  - Only Gymshark showed a shipping cost ("Estimated Shipping $5", "Total $61") and delivery ETAs per method.
  - Huel showed "Shipping FREE" after crossing the threshold.
  - Seed, Glossier and Kind say "Shipping … calculated at checkout".
  — [Gymshark](https://www.gymshark.com/products/gymshark-power-satchel-bags-black-aw26); [Huel](https://huel.com/products/huel-black-edition); [Seed](https://seed.com/products); [Glossier](https://www.glossier.com/products/balm-dotcom); [Kind](https://kindpatches.com/products/berberine-patches-formerly-glp-1-3-pack)
- **CTA count and express wallets in the cart:**
  - One primary checkout CTA at every brand.
  - Kind and Olaplex put the total inside the button ("CHECKOUT • $25.50").
  - Bloom and Gymshark use a lock icon plus "Secure/securely".
  - Only Olaplex rendered wallet buttons (PayPal, Shop Pay, G Pay) in the drawer.
  — [Olaplex](https://olaplex.com/products/olaplex-n-9-bond-protector-nourishing-hair-serum-90ml); [Kind](https://kindpatches.com/products/berberine-patches-formerly-glp-1-3-pack); [Bloom](https://bloomnu.com/products/creatine-gummies); [Gymshark](https://www.gymshark.com/products/gymshark-power-satchel-bags-black-aw26)
- **Interruptions:** Bloom's post-ATC "mystery discount" pop-up with a countdown; Glossier's 15%-off email pop-up blocked the ATC tap; Gymshark's "items aren't reserved" scarcity line — [Bloom](https://bloomnu.com/products/creatine-gummies); [Glossier](https://www.glossier.com/products/balm-dotcom); [Gymshark](https://www.gymshark.com/products/gymshark-power-satchel-bags-black-aw26)
- **Independent evidence (Baymard, cart page):**
  - Average documented cart abandonment is 70.22% (50 studies, updated Sept 22, 2025).
  - Among US shoppers who abandoned during checkout: "extra costs too high (shipping, tax, fees)" 40%, delivery too slow 20%, distrust of site 19%, "unable to see/calculate total cost upfront" 12%, "not enough payment methods" 9%.
  — [Baymard cart-abandonment list](https://baymard.com/lists/cart-abandonment-rate)
- Baymard (2017): 64% of test users looked for shipping costs on the product page before adding to cart, and 43% of sites gave no shipping estimate there. In an older survey, 21% abandoned because they could not see the total cost upfront. The current list shows 12%, so the survey years differ — [Baymard](https://baymard.com/blog/show-shipping-costs-on-product-pages)
- **Vendor-reported results for cart drawers and tests:**
  - Rebuy Smart Cart: OLLY added subscribe-and-save in the cart and reported +25.06% AOV and +63% subscription revenue. Magic Spoon reported +14.75% AOV with Smart Cart.
  - Intelligems: raising a free-shipping threshold lifted revenue per visitor 12% with no conversion loss for one sports brand; lower shipping rates raised profit per visitor 19% for Dossier.
  - All of these are vendor-reported.
  — [Rebuy Magic Spoon](https://www.rebuyengine.com/case-studies/magic-spoon); [Rebuy Smart Cart blog](https://www.rebuyengine.com/blog/rebuy-smart-cart); [Intelligems customer story](https://www.intelligems.io/resources/customer-stories/boost-aov-by-upping-your-free-shipping-threshold); [Intelligems shipping](https://www.intelligems.io/shipping)

### Inferences
- The progress bar is table stakes. What varies is what it unlocks: free shipping, a gift, or a percentage off. For brands with free shipping already, the bar unlocks a bundle discount or gift instead.
- The upsell pattern most relevant to FitPatches is "upgrade the line item": a bigger pack, longer cadence, or subscription replacing the current SKU. Adding a second different product is the less common pattern. Ritual, Seed and Huel do push a second product, but they frame it as unlocking a bundle-wide discount, not as an extra item.
- Shipping cost is usually deferred to checkout because most of these US brands offer free shipping on subscriptions or above a low threshold. Gymshark, which charges shipping below $75, is the one that surfaces cost and ETA in the cart. That matches Baymard's finding that extra costs are the top abandonment reason.

### Gaps
- No independent (non-vendor) A/B evidence was found comparing a drawer with a cart page, or one CTA with two CTAs.
- Rebuy and Intelligems numbers are vendor case studies.
- The Baymard reason percentages come from US surveys; I found no Bulgarian equivalent.

## 3. Checkout: Shopify one-page vs custom, express, fields, shipping cost, payments, branding, trust, post-purchase, thank-you

### Takeaway
All 8 reached checkouts are native Shopify one-page checkout. All share: express wallets at the top (Shop Pay plus PayPal and/or G Pay, sometimes Venmo), shipping methods hidden until the address is entered, address autocomplete at most brands, and card plus 1–5 alternative methods (PayPal, Klarna, Afterpay, Sezzle, Affirm, Cash App).

Brands differentiate with:
- optional first name or phone (Ritual, Bloom),
- branded trust headers and guarantee blocks (Kind, Ritual, Seed),
- in-checkout cross-sells and loyalty blocks (Kind, Bloom),
- small brand rituals (Glossier's Pink Pouch).

None of these merchants offers cash on delivery.

### Cited Findings
- **One-page layout and URL pattern:** every reached checkout is `/checkouts/cn/…` with contact, delivery, shipping method and payment on one scrolling page. This includes the headless Gymshark (us.checkout.gymshark.com) and Seed (checkout.seed.com) — [observed](https://www.gymshark.com/products/gymshark-power-satchel-bags-black-aw26); [observed](https://seed.com/products)
- **Shopify's own claims (vendor):**
  - One-page checkout became the default on Oct 2, 2023. The changelog calls it "optimized for speed and conversion" but gives no numbers — [Shopify changelog](https://changelog.shopify.com/posts/one-page-checkout-is-now-the-default-shopify-checkout)
  - The widely repeated "15% average improvement" figure appears only in agency blogs with no primary source. Treat it as unverified — [charle.co.uk](https://www.charle.co.uk/articles/shopify-one-page-checkout/)
  - One agency measured a single store's checkout conversion going from 54% to 57%, which they call "~7.5%" (the arithmetic gives about 5.6% relative). It was a period-over-period comparison, not an A/B test — [Digismoothie](https://www.digismoothie.com/blog/one-page-checkout-vs-multi-page-checkout)
- **Shop Pay claims (vendor-commissioned):**
  - "Up to 50%" lift versus guest checkout.
  - At least 10% better than other accelerated checkouts.
  - Its mere presence lifts lower-funnel conversion 5%.
  - Source: a "Big Three" consultancy study from April 2023, commissioned by Shopify.
  — [Shopify blog](https://www.shopify.com/blog/shop-pay-checkout)
  - Independent counter-view: a search snippet from an agency says the real-world lift is 1–4%, concentrated among existing Shop Pay users. I did not fetch that page to verify it — [cleancommit.io](https://cleancommit.io/blog/shop-pay-conversion-rate/)
- **Express placement:**
  - Express buttons sit at the top of every checkout: Kind (Shop, PayPal, G Pay), Ritual (Shop, PayPal, G Pay), Glossier and Gymshark (Shop, PayPal, G Pay, Venmo), Bloom (Shop, PayPal), Seed (Shop, G Pay), and Lemme and Olaplex (rendered as skeletons).
  - Subscription brands add the text "By continuing with your payment, you agree to the future charges…".
  — [Kind](https://kindpatches.com/products/berberine-patches-formerly-glp-1-3-pack); [Ritual](https://ritual.com/products/essential-for-women-multivitamin); [Glossier](https://www.glossier.com/products/balm-dotcom); [Gymshark](https://www.gymshark.com/products/gymshark-power-satchel-bags-black-aw26); [Bloom](https://bloomnu.com/products/creatine-gummies); [Seed](https://seed.com/products)
- **Required fields (Shopify labels optional fields "(optional)"):**

  | Field | What I saw |
  |---|---|
  | Email | Required everywhere |
  | First name | Optional at Ritual and Bloom; required elsewhere |
  | Last name, address, city, state, ZIP | Required everywhere |
  | Phone | Required at Kind, Olaplex, Glossier, Gymshark, Seed; "(required outside of USA)" at Lemme; "(optional)" at Bloom; absent at Ritual |
  | Company | Optional, only at Olaplex |
  | Marketing email box | Pre-checked at Kind, Ritual, Bloom, Glossier, Lemme |
  | SMS opt-in | Unchecked at Kind, Glossier, Seed |

  — [observed checkouts](https://ritual.com/products/essential-for-women-multivitamin)
- **Address autocomplete:** the magnifier icon in the Address field appeared at Lemme, Ritual, Glossier, Bloom, Gymshark and Seed — [observed](https://bloomnu.com/products/creatine-gummies)
- **Shipping cost transparency in checkout:**
  - Every checkout shows "Enter your shipping address to view available shipping methods" until the address is entered.
  - Bloom repeats a free-shipping progress bar in the checkout summary.
  - Ritual ("Subscriptions Ship Free") and Seed ("Free US shipping included on every order") state free shipping in trust blocks.
  — [Bloom](https://bloomnu.com/products/creatine-gummies); [Ritual](https://ritual.com/products/essential-for-women-multivitamin); [Seed](https://seed.com/products)
- **Payment methods:**

  | Brand | Methods offered |
  |---|---|
  | Kind | Card, PayPal |
  | Ritual | Card, PayPal |
  | Seed | Card, PayPal |
  | Olaplex | Card, Shop Pay (installments), PayPal, Klarna |
  | Glossier | Card, Shop Pay, PayPal, Afterpay |
  | Bloom | Card, Shop Pay, PayPal, Sezzle |
  | Gymshark | Card, PayPal, Klarna, Afterpay, Cash App Pay, Sezzle |

  Lemme's checkout signals Affirm. No brand offers cash on delivery. — [observed checkouts](https://www.gymshark.com/products/gymshark-power-satchel-bags-black-aw26)
- **Branding and trust inside checkout:**
  - Kind: custom header with "4+ Million Patches Sold / 30 Day Money Back Guarantee / As Seen In Vogue & Forbes"; a review card under express; trust icon row (shipping days, secure payments, money-back); "Don't miss these bestsellers" add-on block.
  - Ritual and Seed: guarantee and cancel-anytime blocks under "Pay now".
  - Bloom: tyb loyalty and rewards blocks.
  - Glossier: gift message and free Pink Pouch opt-in.
  - Olaplex and Gymshark: logo and fonts only.
  — [Kind](https://kindpatches.com/products/berberine-patches-formerly-glp-1-3-pack); [Ritual](https://ritual.com/products/essential-for-women-multivitamin); [Seed](https://seed.com/products); [Bloom](https://bloomnu.com/products/creatine-gummies); [Glossier](https://www.glossier.com/products/balm-dotcom)
- **Plan constraint:** checkout UI extensions on the information, shipping and payment steps (review cards, trust rows, in-checkout upsells like Kind's) are Shopify Plus only. Thank-you and order-status page extensions are available on all plans — [Shopify Help Center – checkout apps](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-apps)
- **Thank-you page migration:** legacy non-Plus thank-you and order-status customisations (Additional Scripts, script tags) were retired on Aug 26, 2026, with automatic upgrade. Any tracking pasted there needed moving to app blocks or web pixels. Sources are agency and app blogs — [Consentmo](https://www.consentmo.com/blog-posts/shopify-thank-you-order-status-upgrade-august-2026); [absolute-design](https://www.absolute-design.co.uk/blogs/insights/shopify-checkout-upgrade-august-2026)
- **Post-purchase one-click upsell limits (vendor documentation):**
  - Shopify's post-purchase page does not display when the buyer paid with "a gift card or any payment method other than a credit card".
  - It also does not display with wallets or BNPL (Klarna, Affirm, Afterpay, Apple Pay, Amazon Pay, Google Pay). Shop Pay is supported.
  - Other blockers: a non-default currency, orders with duties, local delivery.
  — [Rebuy help: Shopify post-purchase limitations](https://help.rebuyengine.com/en/articles/6706477-shopify-s-post-purchase-offer-considerations-limitations); see also the [Shopify dev forum thread on COD](https://community.shopify.dev/t/post-purchase-extension-with-cash-on-delivery-cod/14296)
- **Post-purchase take rates (vendor and blog figures):**
  - Zipify OCU claims a 16.2% average post-purchase conversion.
  - Blogs cite 10–15% typical, and about 4% for set-and-forget offers.
  — [Zipify](https://zipify.com/blog-post-purchase-upsells-shopify-2026/); [digitalapplied](https://www.digitalapplied.com/blog/post-purchase-upsell-thank-you-page-2026-ecommerce-playbook)
- **Independent checkout-UX evidence (Baymard, updated Nov 25, 2025):**
  - 63% of mobile sites have "mediocre or worse" checkout UX.
  - 48% show delivery speed instead of dates.
  - 83% don't show the order cutoff as a countdown.
  - 49% don't explain why a phone number is required.
  - 61% don't mark both required and optional fields.
  - Large sites could gain about 35% conversion through better checkout design.
  — [Baymard 2025 checkout UX](https://baymard.com/blog/current-state-of-checkout-ux)
  - The average checkout has 23.48 form elements (14.88 fields); the ideal is 12–14 elements (7–8 fields) — [Baymard](https://baymard.com/lists/cart-abandonment-rate)
  - Separately, Baymard reports that 41% of sites don't give delivery dates — [Baymard delivery date vs speed](https://baymard.com/blog/shipping-speed-vs-delivery-date)

### Inferences
- The big brands accept Shopify checkout's constraints and invest in two places: the drawer before checkout, and trust content around the pay button. On a non-Plus plan, FitPatches can copy the drawer patterns fully, but only the checkout-editor branding (logo, colours, fonts), not Kind-style review cards or upsells inside checkout.
- Because Shopify's post-purchase page never fires for COD or manual payments, FitPatches' 244 EasySell COD orders cannot get Shopify-native one-click upsells. Any post-purchase offer for COD buyers has to live in the COD app's own flow or the thank-you page.

### Gaps
- Thank-you and order-status pages and live post-purchase offers were not observed.
- Which app powers Kind's in-checkout "Don't miss these bestsellers" block is unconfirmed (UpCart, Rebuy or another app).
- Lemme's and Olaplex's express buttons rendered only as skeletons in the screenshots.
- No independent study isolates the effect of pre-checked marketing boxes or optional name fields.

## 4. Apps / tools in use

### Takeaway
The cart layer is either a cart app (Kind: UpCart; Lemme: Rebuy Smart Cart) or custom code (Ritual, Seed, Bloom, Glossier, Gymshark, Huel). Subscriptions run on Recharge where detectable (Kind, Olaplex). Price and offer testing uses Intelligems (Kind, Lemme), Optimizely (Olaplex, Glossier, Seed) or Dynamic Yield (Gymshark). Reviews run on Okendo, Yotpo or Bazaarvoice, and email/SMS on Klaviyo.

### Cited Findings
Each row lists scripts found on the PDP; the link goes to that page.

| Brand | Scripts detected | Notes |
|---|---|---|
| Kind Patches | UpCart (`upcart-bundle.js`), Recharge (rechargecdn), Intelligems, Klaviyo, Yotpo, Northbeam | [PDP](https://kindpatches.com/products/berberine-patches-formerly-glp-1-3-pack) |
| Lemme | Rebuy (`rebuy.js`, `rebuy-extensions.js`, personalization engine), Intelligems, Klaviyo | Cart DOM class `rebuy-cart__flyout`. [PDP](https://lemmelive.com/products/lemme-burn-gummies) |
| Ritual | Okendo reviews, Klaviyo, Amplitude | Cart is custom. [PDP](https://ritual.com/products/essential-for-women-multivitamin) |
| Olaplex | Recharge, Klaviyo (email/SMS/back-in-stock), Bazaarvoice, Algolia, Optimizely | Cart opened via a `showLlamaCart` URL parameter, so it is likely custom or agency-built. [PDP](https://olaplex.com/products/olaplex-n-9-bond-protector-nourishing-hair-serum-90ml) |
| Glossier | Optimizely, Klaviyo, Gorgias chat | Cart DOM class `bag bag--mini` (custom). [PDP](https://www.glossier.com/products/balm-dotcom) |
| Bloom | Okendo reviews and Okendo loyalty, Klaviyo | Cart DOM class `cart-next` (custom). Checkout loyalty block "powered by tyb". [PDP](https://bloomnu.com/products/creatine-gummies) |
| Seed | Optimizely, Segment, Amplitude, Northbeam, Yotpo pixel | Headless storefront, Shopify checkout on checkout.seed.com. [products page](https://seed.com/products) |
| Gymshark | Dynamic Yield | Headless storefront, Shopify checkout on us.checkout.gymshark.com. [PDP](https://www.gymshark.com/products/gymshark-power-satchel-bags-black-aw26) |
| Huel | — | Next.js on Vercel (response headers `x-powered-by: Next.js`, `server: Vercel`); custom cart. [PDP](https://huel.com/products/huel-black-edition) |
| AG1 | — (blocked) | Headless PWA by Anatta. [Anatta](https://anatta.io/case-study/athleticgreens) |

- Vendor claims for the COD tool FitPatches uses (EasySell):
  - "Trusted by 70,000+ stores", "+38% conversions" (demo), "42% fewer abandoned orders" (testimonial), "+28% revenue per order" from post-purchase upsells (testimonial).
  - Features: quantity offers ("+30% AOV on average"), pre-purchase upsells in the form, post-purchase offers, OTP via SMS/WhatsApp, "Pay 10% Now, 90% on Delivery".
  - All are vendor claims.
  — [easysellapp.com](https://easysellapp.com/)

### Inferences
- A third-party cart app (UpCart, Rebuy) gives a mid-size brand roughly the feature set the custom-built carts have: tier bars, gifts, subscription upgrades, one cross-sell. Kind Patches, the closest analogue to FitPatches, runs UpCart plus Intelligems, which is achievable without Plus.

### Gaps
- App detection only covered PDP script tags. Apps loaded via app embeds or web pixels, server-side tools, and checkout extensions are under-detected.
- I could not confirm Ritual's, Bloom's or Glossier's subscription engine (Glossier's cart has a subscription selector, but no Recharge script was detected).

## 5. Cross-brand patterns most likely to raise cart-to-order rate, and transferability to a cash-on-delivery market (FitPatches)

### Takeaway
The patterns with the best mix of evidence and adoption:
1. One unambiguous primary CTA in the cart.
2. Total cost visible before checkout: shipping price, and a delivery date or ETA.
3. A tier bar that unlocks a gift, discount or free shipping.
4. A line-item upgrade (bigger pack or cadence) instead of a separate add-on.
5. Auto-added or pick-your-own free gift.
6. Guarantee and review proof right under the CTA.
7. A short form with optional fields marked and the phone field explained.

Patterns 1, 2, 3, 5, 6 and 7 transfer directly to a COD market. Subscriptions, BNPL and Shopify one-click post-purchase upsells transfer poorly, because COD orders carry no stored card.

### Cited Findings
- **FitPatches baseline (user-provided data, my arithmetic), last 90 days:**
  - 5,653 sessions → 608 ATC sessions (10.8%) → 160 reached Shopify checkout (26.3% of ATC) → 77 completed Shopify checkout (48.1% of those who reached it).
  - Plus 244 EasySell COD orders, for 321 orders in total: 5.7% of sessions, 76% of them COD.
  - If every EasySell order came from an ATC session, cart-to-order would be 52.8% (321/608). EasySell can also be triggered from the PDP, so that figure is an upper bound.
  — [user-provided funnel; no external source](https://fitpatches.net)
- **COD context:**
  - About 55% of Bulgarian online shoppers still choose cash on delivery. The figure is reported in May 2025 with no primary statistical source cited — [Novinite](https://www.novinite.com/articles/232122/E-Commerce+Growth+in+Bulgaria+Fuels+Shift+from+Cash+on+Delivery+to+Seamless+Online+Payments)
  - Shopify Payments in Bulgaria auto-activates Apple Pay, Google Pay and Shop Pay. The page does not mention Shop Pay Installments or Klarna — [Shopify Help Center – Bulgaria payment methods](https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries/bulgaria/payment-methods)
- **Single primary CTA:** observed at all 9 brands whose carts I captured. None stacks two equal-weight checkout buttons; Olaplex adds wallet buttons under one primary button — [observed sites](https://olaplex.com/products/olaplex-n-9-bond-protector-nourishing-hair-serum-90ml)
- **Total cost before checkout:**
  - Baymard ranks extra costs (40%) and not seeing the total cost upfront (12%) among the top abandonment reasons — [Baymard](https://baymard.com/lists/cart-abandonment-rate)
  - 41% of sites lack delivery dates — [Baymard](https://baymard.com/blog/shipping-speed-vs-delivery-date)
  - Gymshark shows shipping cost, ETA and the total in the cart — [Gymshark](https://www.gymshark.com/products/gymshark-power-satchel-bags-black-aw26)
- **Tier bar plus gift:** used by 9 of 9 carts (section 2). Vendor tests from Intelligems show threshold changes moving RPV or profit (vendor-reported) — [Intelligems](https://www.intelligems.io/resources/customer-stories/boost-aov-by-upping-your-free-shipping-threshold)
- **Line-item upgrade instead of a separate add-on:** Seed, Olaplex, Bloom, Lemme, Glossier, Huel (section 2). In Rebuy's OLLY case, adding subscribe-and-save in the cart raised AOV 25% (vendor-reported) — [Rebuy](https://www.rebuyengine.com/blog/rebuy-smart-cart)
- **Guarantee and social proof near the CTA:**
  - Under the cart CTA: Lemme, Bloom.
  - In checkout: Kind, Ritual, Seed.
  - Under the PDP CTA: AG1 (90-day guarantee directly below the CTA).
  - Baymard lists "distrust of site security" at 19% of abandonments.
  — [Lemme](https://lemmelive.com/products/lemme-burn-gummies); [Bloom](https://bloomnu.com/products/creatine-gummies); [Kind](https://kindpatches.com/products/berberine-patches-formerly-glp-1-3-pack); [vms.nik.co](https://vms.nik.co/); [Baymard](https://baymard.com/lists/cart-abandonment-rate)
- **Form length and phone explanation:** Baymard puts the ideal at 7–8 fields, notes that 49% of sites don't explain the phone requirement, and that 61% don't mark required and optional fields. Ritual and Bloom make first name optional; Bloom makes phone optional — [Baymard](https://baymard.com/blog/current-state-of-checkout-ux); [Ritual](https://ritual.com/products/essential-for-women-multivitamin); [Bloom](https://bloomnu.com/products/creatine-gummies)
- **COD-specific practice (vendor and app sources):**
  - Pre-dispatch SMS/WhatsApp confirmation, 12–24 h before shipping and stating the exact COD amount, is promoted to cut refusals. One vendor claims a "60%" reduction in COD returns.
  - OTP verification is offered by EasySell and Konfirm.
  — [releas.it](https://www.releas.it/blogs/news/how-to-reduce-cod-rto-shopify); [Konfirm app](https://apps.shopify.com/konfirm-1); [EasySell](https://easysellapp.com/)
- **Shopify post-purchase does not run on COD orders** — [Rebuy help](https://help.rebuyengine.com/en/articles/6706477-shopify-s-post-purchase-offer-considerations-limitations)

### Inferences (FitPatches-specific; these are reasoning, not tested results)
1. **Collapse the two stacked CTAs into one primary action. (Transfer: high.)** Every benchmark brand shows one primary checkout button. Two options:
   - Make "Поръчай с наложен платеж" the single dominant button, since 76% of orders are COD, and demote "Плащане с карта" to a secondary outline or text link.
   - Or use one "Поръчай" button that opens a single form with payment-method radios, COD preselected.

   Either removes the choice moment at the highest-intent step. This should be A/B tested, since no source isolates the two-CTA effect.
2. **Show shipping price and a delivery date in the drawer. (Transfer: high; COD buyers pay the courier, so price surprises matter even more.)** For example: "Доставка до офис на Еконт/Спиди: X € · Безплатна над Y €" and "Получаваш до [ден, дата]". This follows Gymshark's pattern and Baymard's top abandonment reasons. If a COD fee exists, show it too.
3. **Turn the add-a-second-product upsell into a line-item upgrade.** For example: "Вземи курс 2 месеца – спести X%" replaces the 1-pack, Seed/Olaplex/Bloom-style. Or frame it as a bundle-wide unlock: "Добави още 1 → −15% на цялата поръчка" (Ritual, Seed). Kind Patches, the closest analogue, sells the 3-pack as "Buy 2 Get 1 FREE" in a tier bar. (Transfer: high; needs no card.)
4. **Make the free-shipping bar unlock something tangible.** Options: a free gift (Seed's travel vial, Glossier's or Bloom's free sample), or "+1 пакет пластири безплатно" at the multi-pack tier. (Transfer: high.)
5. **Put the guarantee and review proof directly under the CTA:** e.g. "30 дни гаранция за връщане на парите · 4.8★ от N клиенти · Плащаш при получаване". Lemme and Bloom do this in the cart, Kind/Ritual/Seed in checkout. (Transfer: high. For COD, "pay on delivery / inspect parcel" is itself a trust lever.)
6. **Express wallets (Apple Pay, Google Pay, Shop Pay) are available in Bulgaria via Shopify Payments.** Most brands show them at the top of checkout; only Olaplex shows them in the cart. For FitPatches they matter only for the card minority. Placing them in the drawer adds CTAs, which conflicts with point 1. (Transfer: medium-low.)
7. **Subscriptions, BNPL and Shopify one-click post-purchase upsells transfer poorly to COD.** No stored card means no recurring billing and no Shopify post-purchase page. Substitutes:
   - multi-month "course" packs,
   - EasySell's own in-form quantity offers and post-purchase offer,
   - a thank-you-page offer,
   - a pre-dispatch SMS/WhatsApp confirmation that can add an upsell.
   (Transfer: low as-is; medium via the COD app.)
8. **Form hygiene for the COD popup and the Shopify checkout:**
   - Make the phone field required and explain why: "куриерът ще ви се обади".
   - Keep the field count near 7–8.
   - Mark optional fields.
   - Pre-select the most common courier option.
   (Transfer: high.)
9. **Avoid adding Bloom/Glossier-style interrupt pop-ups** (mystery discount, email capture) after ATC. They blocked ATC in my own test (Glossier), and the FitPatches audience is 95% mobile with paid-social traffic.

### Gaps
- I found no independent A/B data on single vs dual CTAs, on COD-vs-card button order, or on cart-drawer patterns in CEE/COD markets. The recommendations above are inferences from benchmark-brand practice plus Baymard's US data.
- Bulgarian COD share figures (around 55% of shoppers) lack a primary NSI/Eurostat citation in the source found.
- The vendor numbers (EasySell, Rebuy, Intelligems, Zipify, COD-confirmation apps) are unverified.
- Whether FitPatches' EasySell orders start from the drawer or from the PDP is unknown, so its true cart-to-order rate cannot be computed.
