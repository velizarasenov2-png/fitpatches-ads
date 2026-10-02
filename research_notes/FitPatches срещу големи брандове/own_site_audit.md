# fitpatches.net — Own-Site CRO Audit (offer, UX/visual design, funnel, trust, compliance) — state as of 2 Oct 2026

Method note (applies to every section): all site facts below were observed directly on the live store on 2 Oct 2026 with Playwright (iPhone 13 emulation = 390×664 CSS px viewport, locale bg-BG, timezone Europe/Sofia; plus a 1440×900 desktop pass), raw HTML via curl, and `/products.json`. No forms were submitted and no order was placed. After ~10 automated sessions Shopify's bot protection started answering with HTTP 429 "Your connection needs to be verified before you can proceed", so the checkout page content could not be captured (see Gaps). Local evidence (screenshots, logs) lives in `/tmp/claude-0/-home-user-fitpatches-ads/77d5f012-1d96-5267-aa86-a2c530bc0277/scratchpad/` (`shots/net-*.png|txt`, `audit/drawer-tier1.png`, `audit/drawer-tier3.png`, `audit/easysell-popup.png`, `audit/perf-*.json`, `audit/funnel.log`, `slices/gallery.png`, `site/pg_44d0f356.html` = PDP HTML, `site/net_home.html` = home HTML).

Page URLs used as sources:
- Home: https://fitpatches.net/
- Main PDP: https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30
- Bundle PDP "2+1 ПОДАРЪК": https://fitpatches.net/products/fitpatches-2-1-подарък-берберинови-пластири
- Bundle PDP "5+5 / 2+1 БЕЗПЛАТНО ПОДАРЪК": https://fitpatches.net/products/fitpatches-5-5-премиум-пакет-берберинови-пластири
- Catalog JSON: https://fitpatches.net/products.json ; Cart: https://fitpatches.net/cart ; Collection: https://fitpatches.net/collections/all

## 1. Above the fold on mobile (home + PDP): what the visitor sees first, and how far the offer is

### Takeaway
On the home page the first screen is a pack shot + "4.8/5 според 1,837 клиентки" + an aggressive weight-loss H1, but the only CTA sits just below the fold and there is no price anywhere on the home page; on the PDP the first screen is a before/after mirror selfie with a composited pack and the first two lines of a long headline — no price, no rating, no CTA — and the buy button is ~2.5 screens down, after which the page runs another ~12 screens with no CTA and no sticky add-to-cart.

### Cited Findings
**Home (mobile, 390×664 viewport)**
- Header: sticky, ~111 px tall (≈17% of the 664 px viewport), contains only a search icon, a small circular script logo, and an account/"Вход" icon. A `/cart` link exists in the header HTML but is hidden (`vis=false`); there is no navigation menu on mobile or desktop — [Home](https://fitpatches.net/) (Playwright DOM check, `audit/funnel.log`).
- First screen, top to bottom: square pack-shot image (pomegranate + barberry plant styling, pack text in English: "Berberine Patches · 30 Metabolic Balance Patches · Vegan · Cruelty-Free · Discreet & Comfortable · Metabolism & Appetite Control · 1 Month Pack"), then "★★★★★ 4.8/5 според 1,837 клиентки", then H1 "КОНТРОЛИРАЙ АПЕТИТА И ОТСЛАБНИ ДО 8 КГ ЗА 30 ДНИ", then three pill badges "БЕЗ ХАПЧЕТА / БЕЗ ДИЕТИ / 100% НАТУРАЛНО" — [Home](https://fitpatches.net/) (`shots/net-home-fold.png`).
- The only CTA, "ПАЗАРУВАЙ СЕГА →", starts at ≈700 CSS px, i.e. just below the 664 px fold, followed by "Безплатна доставка над €60 · Наложен платеж · 30 дни гаранция" — [Home](https://fitpatches.net/).
- The home page contains exactly one link to a product (`href='/products/fitpatches-berberinovi-plastiri-30'`, the hero CTA); there is no price, no bundle, no "add to cart" and no closing CTA anywhere on the 7,580 px-tall page (it ends with the last review card and an empty coral footer bar) — [Home HTML](https://fitpatches.net/).
- Home section order: hero → scrolling marquee ("✦ КОНТРОЛ НА АПЕТИТА ✦ 100% НАТУРАЛНО ✦ БЕЗ ХАПЧЕТА ✦ БЕЗ ДИЕТИ ✦ ПЪЛНА ЕНЕРГИЯ ✦ ДИСКРЕТЕН РАЗМЕР ✦ БАЛАНС") → "СРАВНЕНИЕ — FitPatches срещу Ozempic" table → "КАК РАБОТИ" 4 tiny tiles ("Избери / Отлепи / Залепи / Усети") → "НАУЧЕН АНАЛИЗ — Защо берберинът наистина работи" (3 one-line points) → "ПРЕДИ / СЛЕД — Какво се случва след 1 месец" (split belly image) → "Над 1,837 успешни трансформации" + 97% / 95% / 92% stat tiles → "ПРЕПОРЪЧАНО ОТ ЛЕКАР" doctor card → FAQ (7 items) → 30-day guarantee box → reviews ("4.8 … според 1,012 доволни клиента", 10 cards) → end — [Home](https://fitpatches.net/) (`shots/net-home-full.png`, `shots/net-home.txt`).

**Main PDP (mobile)**
- First screen: same sticky header, then gallery image #1 = a mirror before/after selfie of a woman (~30s, grey T-shirt vs white T-shirt) with a FitPatches pack pasted between the two halves; the pasted pack's small print renders garbled ("…Patohes", "Vagen · Cruelly Free · Disareet & Comlorlsiole", "Metabolism & Appotite Conhol"), then the first two lines of the H1 — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30) (`shots/net-pdp-fold.png`).
- The H1 is the product title itself: "Започни да сваляш килограми след 20 дни, използвайки тези лепенки, които намаляват апетита" (4 lines on mobile) — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
- Approximate vertical positions from the full-page capture (CSS px, mobile): rating "1012 Ревюта" ≈740, price block ≈770–810 (≈1.2 screens), "Колко пакета желаете?" selector ≈1,175, "Поръчай сега" button ≈1,700 (≈2.6 screens). Total PDP height 10,312–10,797 px (≈16 screens) — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30) (`shots/net-pdp-full.png`, `audit/perf-pdp.json`).
- No sticky add-to-cart: at 25% and 55% scroll depth the only fixed elements are the header and a "scroll-to-top" button (`BUTTON.floating-btn scroll-to-top-btn`) — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30) (`audit/funnel.log`).
- After the offer block (selector → "Поръчай сега" → lead form → phone → "50+ диетолози" → objections), the remaining sections ("Природата в помощ на фигурата", autoplay video, "ПРИРОДНА ФОРМУЛА", "FitPatches срещу диети и хапчета", "КАК ДЕЙСТВА", "Какво се случва след 30 дни", "Научен анализ" ×3, "Какво казват клиентите ни във Facebook") contain no CTA at all — [PDP text](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30) (`shots/net-pdp.txt`).
- Desktop PDP (1440×900): two-column layout, gallery left (B/A selfie + thumbnails), title/price/timer/benefits/selector right; first tier visible above the fold, "Поръчай сега" below it; header again has no menu and no visible cart icon; the gallery column ends early leaving large empty space beside the long right column; footer is an empty coral bar — [PDP desktop](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30) (`shots/net-pdp-desktop-fold.png`, `slices/desk-montage.png`).

### Inferences
- Meta-ad traffic landing on the home page must scroll, tap the CTA, wait for a heavy PDP (see §4) and scroll ~2.5 more screens before seeing a buy button — at least 2 page loads and ~3–4 screens to the offer. Landing on the PDP: ~1.2 screens to price, ~2.6 screens to CTA.
- Because ~80% of the PDP length (≈1,700 px → ≈10,300 px) has no buy button and no sticky ATC, every visitor who is persuaded by the lower "proof" sections must scroll back up ~8,000+ px to buy — a classic, high-impact leak on long-form COD PDPs.
- A hidden cart icon means a returning visitor who already added an item has no visible route back to the cart except re-clicking "Поръчай сега" (which adds another unit — see §6).

### Gaps
- Real scroll-depth / click data (e.g., Shopify/Clarity heatmaps) was not available; positions are measured from emulated screenshots, not real devices or Facebook/Instagram in-app browsers.

## 2. Offer architecture: bundle selector, anchoring, discount claims, timer, free-shipping threshold, gift, guarantee, COD — and internal consistency

### Takeaway
The PDP has a clean 3-tier radio selector (1 pack €14.99 / 2 packs €27.99 / "3 пакета + 1 подарък" €39.99 preselected) with heavy compare-at anchoring, but almost every number around it contradicts another number on the site: the selected tiers add products whose titles/descriptions promise different quantities, the "-50%" badge sits next to a "66%" saving, the "expiring" timer is a midnight loop, free shipping is €60 on home vs €70 in the cart (unreachable by any single bundle), and the guarantee is 30 days, 60 days, or "just don't reorder" depending on where you look.

### Cited Findings
**Selector & price anchoring**
- Selector heading "Колко пакета желаете?" + "Повечето клиенти избират 2 или 3 пакета за пълен резултат." Tiers: "1 пакет · 30 лепенки · 1 месец — 29.99 EUR → 14.99 EUR · Спестяваш 50%"; "2 пакета · 60 лепенки · 2 месеца — 59.98 → 27.99 · Спестяваш 53%"; "3 пакета + 1 подарък · 120 лепенки · 4 месеца — 119.96 → 39.99 · Спестяваш 66%", badge "Най-популярен", preselected (`checked`) — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
- Effective price per patch: €0.50 (1 pack), €0.47 (2 packs), €0.33 (3+1). The 3+1 compare-at (119.96 = 4 × 29.99) prices the free gift pack at full "regular" price; the real saving vs 119.96 is 66.7% — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30); [products.json](https://fitpatches.net/products.json).
- Main price block above the selector shows "119.96 EUR / 39.99 EUR" with a red badge "-50% ОТСТЪПКА · изтича след HH:MM:SS" — i.e., a "-50%" label next to an offer the selector itself calls "Спестяваш 66%" — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
- The "regular" price €29.99 for one pack is the Shopify compare-at price on a product created 22 May 2026; there is no evidence on the site of the pack ever being sold at €29.99 — [products.json](https://fitpatches.net/products.json) (`created_at 2026-05-22`).
- Under EU Omnibus rules, any announced price reduction must show the lowest price applied during the prior 30 days (Art. 6a inserted into Directive 98/6/EC) — [Directive (EU) 2019/2161](https://eur-lex.europa.eu/eli/dir/2019/2161/oj).

**Selector → cart product mapping (confirmed by adding each tier and reading `/cart.js`)**
- "1 пакет" → variant 53836021039441 → cart line title "Започни да сваляш килограми след 20 дни, използвайки тези лепенки, които намаляват апетита" (the headline is the product title) — [PDP HTML / cart.js](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30) (`audit/funnel.log`).
- "2 пакета · 60 лепенки" → variant 53837384024401 → cart line "FitPatches 2+1 ПОДАРЪК — Берберинови пластири", whose product description says "Купи 2, Вземи 1 Безплатно! Нашата най-популярна оферта — три пакета FitPatches … на цената на два" (i.e., 3 packs) — [Bundle 2+1](https://fitpatches.net/products/fitpatches-2-1-подарък-берберинови-пластири); [products.json](https://fitpatches.net/products.json).
- "3 пакета + 1 подарък · 120 лепенки" → variant 53837385859409 → cart line "FitPatches 2+1 БЕЗПЛАТНО ПОДАРЪК — Берберинови пластири" (implies 3 packs); its handle is `fitpatches-5-5-премиум-пакет-…`, tags `5+5, премиум`, and description "Максималната стойност — 5+5 пластира! … Десет пакета FitPatches … за над 10 месеца употреба" (10 packs) — [Bundle 5+5](https://fitpatches.net/products/fitpatches-5-5-премиум-пакет-берберинови-пластири); [products.json](https://fitpatches.net/products.json).
- So one €39.99 SKU is simultaneously described as 4 packs (PDP selector, compare price), 3 packs (title "2+1") and 10 packs (handle/description); one €27.99 SKU as 2 packs (selector) and 3 packs (title/description) — [products.json](https://fitpatches.net/products.json); [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
- "Most popular" is claimed for the 3+1 tier on the PDP ("Най-популярен") and for the 2+1 product in its description ("Нашата най-популярна оферта") — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30); [products.json](https://fitpatches.net/products.json).
- Both bundle URLs render the full main-PDP template with the same 3-tier selector (3+1 preselected → headline price €39.99), only the H1 changes; e.g., the "FitPatches 2+1 ПОДАРЪК" page (a €27.99 product) shows "119.96 EUR / 39.99 EUR" at the top and offers "2 пакета" in the selector. The 2+1 hero image shows three packs — [Bundle 2+1](https://fitpatches.net/products/fitpatches-2-1-подарък-берберинови-пластири); [Bundle 5+5](https://fitpatches.net/products/fitpatches-5-5-премиум-пакет-берберинови-пластири) (`slices/bundles-fold.png`).
- Bundle variants have no SKU and all variants have `grams: 0` — [products.json](https://fitpatches.net/products.json).
- The collection and cart "You may also like" blocks list the three products side by side: "FitPatches 2+1 БЕЗПЛАТНО ПОДАРЪК … €39,99 / €119,96 … 66%", "FitPatches 2+1 ПОДАРЪК … €27,99 / €59,98 … 53%", "Започни да сваляш килограми след 20 дни… €14,99 / €29,99 … 50%" — two different "2+1" offers at two different prices — [Collection](https://fitpatches.net/collections/all); [Cart](https://fitpatches.net/cart).

**Countdown timer**
- The badge "изтича след" is computed client-side as the time remaining until the visitor's local midnight: `var end=new Date(now.getFullYear(),now.getMonth(),now.getDate()+1,0,0,0,0)`; the HTML placeholder is "00:30:00" before JS runs — [PDP HTML](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
- Two consecutive loads 7 s apart (Sofia time 12:53:27 and 12:53:34) showed 11:06:33 and 11:06:26 — it does not reset on reload, but it restarts every midnight, so the "-50%" offer never actually expires; no cookie/localStorage state is used — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30) (`audit/funnel.log`).
- UCPD Annex I (blacklist) prohibits falsely stating that a product or terms will only be available for a very limited time to elicit an immediate decision (point 7) — [Directive 2005/29/EC consolidated](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A02005L0029-20220528).

**Delivery promise**
- Under the CTA: "Плащане при доставка · Доставка до 2–4 работни дни · Без предплащане", followed by a timeline "2 октомври Поръчано → 3 октомври Изпращане → 4 октомври Доставено" generated as today +0/+1/+2 calendar days (`data-tl`) — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30). On 2 Oct 2026 (a Friday) this promises shipping on Saturday and delivery on Sunday 4 Oct, contradicting "2–4 работни дни" (weekday check done locally).

**Free shipping**
- Home hero trust line: "Безплатна доставка над €60" — [Home](https://fitpatches.net/).
- Cart drawer code: `FREESHIP=70`; drawer shows "Остават 55.01 EUR до безплатна доставка" for 1 pack and would show "Остават 30.01 EUR…" for the €39.99 bundle — [PDP HTML](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30) (`audit/drawer-tier1.png`).
- Home FAQ: "Какви бонуси? — Безплатна доставка, 30-дневна гаранция." (unconditional) — [Home](https://fitpatches.net/).
- The most expensive offer is €39.99, so no single offer reaches either the €60 or €70 threshold; the shipping fee itself is not stated anywhere on home/PDP, and `/policies/shipping-policy` returns 404 — [products.json](https://fitpatches.net/products.json); [Shipping policy 404](https://fitpatches.net/policies/shipping-policy).

**Guarantee / risk reversal**
- Home: trust line "30 дни гаранция"; box "30-дневна гаранция за връщане — Пробвай цял месец. Ако не усетиш разлика — задръж продукта и ние ще ти върнем парите." — [Home](https://fitpatches.net/).
- Cart drawer badges: "Наложен платеж · 60 дни гаранция" — [PDP drawer HTML](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30) (`audit/drawer-tier1.png`).
- PDP objection "А ако на мен не ми подейства?" answers: "Точно затова започваш без риск с наложен платеж. Пробвай един пакет — ако не усетиш разлика в апетита, просто не поръчваш пак." (no refund mentioned; and nudges toward 1 pack, against the 3+1 default) — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
- The PDP offer block itself contains no guarantee statement; `/policies/refund-policy` returns 404 — [Refund policy 404](https://fitpatches.net/policies/refund-policy).

**Gift / upsell**
- The "1 подарък" in the 3+1 tier is simply a 4th pack (no separate gift item, no gift image) — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
- Drawer upsell "Може още да ти хареса — 3 пакета + 1 подарък 119.96 39.99 [Добави]" adds the 3+1 bundle as an additional line (no swap/upgrade); it is hidden only if the 3+1 variant is already in the cart — [PDP drawer JS](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).

### Inferences
- The tier-to-title mismatch is probably the single most damaging inconsistency: a woman who chose "2 пакета" sees "2+1 ПОДАРЪК" in the cart/checkout/order confirmation (and possibly expects 3 packs); one who chose "3 пакета + 1 подарък" sees "2+1 БЕЗПЛАТНО ПОДАРЪК" (fewer packs than chosen) — a trust break at the moment of commitment and a likely source of COD refusals, complaints and picking errors (warehouse may pack by title).
- Showing free shipping thresholds that no offer can hit, while not stating the shipping fee, means the first time the COD buyer sees the delivery cost is in checkout — a classic surprise-cost abandonment trigger. A single, honest rule (e.g., free shipping on the 2- and 3+1-pack tiers) would also make the higher tiers more attractive.
- The evergreen midnight timer and the inconsistent "-50%"/"66%" labels add little urgency for repeat visitors (it is visibly the same "deal" every day) while carrying UCPD risk.
- The PDP gives the weakest risk reversal exactly where it matters (offer block and objection section), while the strongest version ("задръж продукта и ние ще ти върнем парите") is buried on the home page.

### Gaps
- Actual shipping fee, COD fee and courier options (Econt/Speedy/address) in Shopify checkout could not be captured (bot protection, see Method note).
- Whether €29.99 was ever a real selling price (Omnibus 30-day prior-price rule) cannot be verified from outside.
- Which physical quantity is actually shipped for each SKU is unknown.

## 3. Social proof & trust: reviews, doctor, "50+ диетолози", Facebook block, stats, Ozempic comparison, store legitimacy

### Takeaway
There is no review app — every rating, count, review, stat and "Facebook comment" is hard-coded theme content, and the numbers disagree with each other (1,837 vs 1,012 vs "над 1000" vs "хиляди"; 4.8 vs a 4.5-star graphic); reviews are dated months before the products existed, testimonials and lifestyle imagery appear AI-generated, the "doctor" is unverifiable, and the store lacks basic legitimacy signals (no footer, no company identity, no refund/shipping/terms pages, a typo in the privacy policy title).

### Cited Findings
**Reviews & ratings**
- No review app is installed: the only third-party storefront app found in the HTML is EasySell COD Form (`cdn.shopify.com/extensions/…/easysell-cod-form-524/…`); no Judge.me/Loox/Okendo/Yotpo/Stamped/Trustoo/Ryviu code, and no `aggregateRating` structured data on the PDP — [Home HTML](https://fitpatches.net/); [PDP HTML](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
- Counts/ratings used across the site: "4.8/5 според 1,837 клиентки" (home hero), "Над 1,837 успешни трансформации" (home), "4.8 … според 1,012 доволни клиента" (home reviews block), "1012 Ревюта" with a 4½-star graphic (PDP and both bundle pages), "над 1000 доволни клиенти в България" (PDP gallery slide), "Хиляди клиенти усещат…" (PDP bullet), "Хиляди българи вече опитаха FITPATCHES" (gallery slide) — [Home](https://fitpatches.net/); [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30); [gallery slide](https://cdn.shopify.com/s/files/1/1048/3269/6657/files/fp-slide-s2_ugc_v5.png).
- The PDP's "1012 Ревюта" is not linked to any reviews; the PDP shows no review list at all (only a Facebook-style comment carousel) — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
- Home review cards (10): initials avatars only, no photos, each with a green "✓ Потвърдена покупка" badge, dated 14 март 2025 → 28 юли 2025; 3 of 10 are men (Георги Димитров, Николай Колев, Калин Георгиев) although the hero says "клиентки" — [Home](https://fitpatches.net/).
- All three products were created in Shopify on 22 May 2026 (`created_at 2026-05-22`), i.e. 10–14 months after the review dates — [products.json](https://fitpatches.net/products.json).
- Reviews' own results are modest: "минус 3 кг за 6 седмици", "Скептична бях в началото, но след 3 седмици…", "Първите 10 дни не видях нищо особено" — versus the hero promise "ОТСЛАБНИ ДО 8 КГ ЗА 30 ДНИ" — [Home](https://fitpatches.net/).
- Omnibus-added UCPD blacklist points: 23b — stating reviews come from consumers who used/purchased the product without taking reasonable steps to check; 23c — submitting/commissioning false reviews or misrepresenting reviews — [EU Commission UCPD guidance](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A52021XC1229%2805%29); [UCPD consolidated](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A02005L0029-20220528).

**Facebook-style comment block (PDP)**
- "Какво казват клиентите ни във Facebook": 5 posts rendered with Facebook's UI (reaction icons, "Харесвам / Коментар / Сподели", reply threads) — Мария Иванова "преди 3 дни" 213 reactions/18 коментара; Петя Стоянова "преди 5 дни" 156/9; Галя Димитрова "преди 1 седмица" 301/24 ("минус 4 кг"); Ивелина Колева "преди 2 седмици" 88/6; Радост Ангелова "преди 3 седмици" 142/11. All are static HTML (relative dates never change), grey default avatars, no link to any real Facebook post — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30) (`shots/net-pdp.txt`).
- Replies are generic purchase prompts ("И аз ги поръчах, чакам ги с нетърпение!", "Браво! От къде ги взе?", "Точно това ми е проблемът, поръчвам!") — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).

**Doctor / experts / stats**
- Home: "✓ ПРЕПОРЪЧАНО ОТ ЛЕКАР — „Виждам резултати с FitPatches. Без хапчета, без диети — само постоянство.“ — д-р Александър Димитров, Диетолог · Партньор на FitPatches" (photo file `doktora.png`); no surname credentials, institution, registration number or link — [Home](https://fitpatches.net/).
- Home "Защо берберинът наистина работи" section uses an image whose file name is `ChatGPT_Image_May_22_2026_02_38_15_PM.png` (a smiling female doctor at a desk with the product) — [Home HTML](https://fitpatches.net/).
- PDP: "50+ диетолози и специалисти по хранене препоръчват FitPatches на своите клиенти." with a stock-style photo (`fp-doctor.png`) and a "50+" badge; no names — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
- Stats with no source, sample or method: "97% от жените споделят, че желанието за сладко е намалено в 14 дни", "95% усещат видими промени в тялото в 45 дни", "92% казват, че се чувстват по-енергични" — [Home](https://fitpatches.net/).
- EU Regulation 1924/2006 restricts health claims: no health claim for berberine is on the EU authorised list, and claims referring to the rate or amount of weight loss are not allowed (Art. 12) — [Regulation 1924/2006](https://eur-lex.europa.eu/eli/reg/2006/1924/oj/eng); [EU Register of claims](https://ec.europa.eu/food/food-feed-portal/backend/claims/files/euregister.pdf). (Art. 12(c) of the same regulation also bars claims referring to recommendations of individual doctors/health professionals — stated from the regulation text; EUR-Lex could not be fetched in this session to quote it.)

**Ozempic comparison (home)**
- "СРАВНЕНИЕ — FitPatches срещу Ozempic — Единствената разлика е цената, болката и страничните ефекти." Table rows (✓ FitPatches / ✕ Ozempic): "Без инжекции и болка", "Без рецепта от лекар", "Без гадене и повръщане", "Без 200+ евро на месец", "Дискретно — никой не вижда", "100% натурален състав"; uses an Ozempic pen product photo (file `210316112336ozempic-solution-for-injection-in-a-pre-filled-pen-025-mg.jpg`) — [Home](https://fitpatches.net/).

**Store legitimacy signals**
- Footer: empty except "Методи на плащане © 2026, Fitpatches Powered by Shrine" and a link to shrinesolutions.com; no policy links, no company name/ЕИК/address/e-mail — [PDP DOM](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30); [Contact page](https://fitpatches.net/pages/contact).
- `/policies/refund-policy`, `/policies/shipping-policy`, `/policies/terms-of-service`, `/policies/contact-information`, `/policies/legal-notice`, `/pages/about` → HTTP 404; only `/policies/privacy-policy` exists, and its title is "Правила за повелителност" (should be "Политика за поверителност") — [Refund 404](https://fitpatches.net/policies/refund-policy); [Terms 404](https://fitpatches.net/policies/terms-of-service); [Privacy](https://fitpatches.net/policies/privacy-policy).
- Contact page: page title "Contact" (English), a bare form (Име/Имейл/Телефонен номер/Коментар) with English validation text "This field is required", no address, e-mail or company data — [Contact](https://fitpatches.net/pages/contact).
- The only phone number on the site appears inside the PDP offer block: "Имате въпроси? Свържете се с нас на 0887 459 494" — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
- Bulgarian E-Commerce Act art. 4 obliges an online provider to give unobstructed, direct and permanent access to its name, registered address, place of business and correspondence details — [ЗЕТ (mi.government.bg)](https://www.mi.government.bg/file/2015/09/zet_bg.pdf).
- Home `<title>` is just "Fitpatches"; og:description "Fitpatches" (no meta description); Organization schema has nine empty `sameAs` strings (no social profiles linked) — [Home HTML](https://fitpatches.net/).

### Inferences
- For a skeptical Bulgarian audience that is heavily exposed to "чудо" weight-loss offers, the combination of perfectly round stats, contradictory counts, pre-launch review dates, a Facebook-UI mock and AI-looking faces is more likely to read as "измама" than as proof — the PDP even voices this objection ("„Честно казано, звучи ми като измама.“") but answers it with biochemistry rather than verifiable proof (real reviews, company identity, policies).
- The Ozempic block implies equal efficacy to semaglutide ("единствената разлика…"); in addition to UCPD/claims exposure it uses a third party's trademark and product photo — a comparative-advertising and Meta-policy liability (legal analysis is outside this audit; see the compliance researcher's notes).
- The missing legal pages/company identity are both a legal gap (ЗЕТ art. 4) and a conversion gap: COD buyers commonly check "кой стои зад магазина" before committing, and Meta's landing-page review also looks for policies/contact info.

### Gaps
- No reverse-image search was run on the before/after selfie, the review/UGC faces or the doctor photos, so "AI-generated/stock" is an assessment from visual style and file names, not proof.
- It is unknown whether any real customer reviews exist (e.g., in Meta comments or an unconnected app).

## 4. Visual design, imagery, page weight & speed

### Takeaway
The home page is a fairly clean coral-on-cream "DTC" design, but the PDP switches to a different magenta palette, different heading font treatment and a heavy mix of AI-looking "Balkan kitchen" lifestyle images of older women and men; packaging is English-only, the hero composite has garbled text, and the PDP weighs ~4.7 MB (2.9 MB autoplay video) with LCP ≈5.8 s and full load ≈17 s in emulation — slow for Meta in-app traffic.

### Cited Findings
**Palette, type, consistency**
- Home accent colour #ea7e7e (coral, 41 occurrences in home HTML), body cream #faf6f1/#fef3f3, headings Poppins; FAQ icons from the Google "Material Symbols Outlined" font — [Home HTML](https://fitpatches.net/).
- PDP/drawer accent #d64d87 (magenta; `#fpDrawer{--a:#d64d87;--soft:#fbe9f1}`), yellow review stars, red "-50%" badge; EasySell buttons orange #f59e0b — [PDP HTML](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30); [EasySell config in Home HTML](https://fitpatches.net/).
- Home H1 is set in a heavy condensed style with very tight letter-spacing ("КОНТРОЛИРАЙ АПЕТИТА И ОТСЛАБНИ ДО 8 КГ ЗА 30 ДНИ" — glyphs nearly touch on mobile); PDP H1 uses wide-tracked Poppins bold — [Home](https://fitpatches.net/) (`shots/net-home-fold.png`); [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30) (`shots/net-pdp-fold.png`).
- The logo is a thin pink script monogram in a circle with an illegible micro-tagline; the cart drawer uses a different, typographic "FitPatches" wordmark — [Home](https://fitpatches.net/) (`audit/drawer-tier1.png`).

**Product & lifestyle imagery**
- Product pack art (all images): white pouch, pink circle, English text "Berberine Patches / 30 Metabolic Balance Patches / Vegan · Cruelty-Free · Discreet & Comfortable / Metabolism & Appetite Control / 1 Month Pack" — no Bulgarian text on pack — [Home](https://fitpatches.net/); [gallery](https://cdn.shopify.com/s/files/1/1048/3269/6657/files/3_patcha_size_new.png).
- PDP gallery has 13 images: B/A selfie; "Как се използва" (3 steps); "Лепенка, създадена да овладее глада — Без хапчета. Без диети. Без мъчение."; "По-лесният начин" diets/pills/FitPatches table; "ХИЛЯДИ БЪЛГАРИ ВЕЧЕ ОПИТАХА FITPATCHES" collage of 9 smiling people holding the pack, "★★★★★ над 1000 доволни клиенти в България"; patch-on-wrist photo; "КЪДЕ СЕ ПОСТАВЯТ FITPATCHES?" (долната част на ръката, корема, рамото, бедрото; "ВАЖНО: … на обезкосмена част на тялото"); ingredient infographic; 3-pack shot; plus duplicates — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30); [gallery images](https://cdn.shopify.com/s/files/1/1048/3269/6657/files/fp-slide-s2_ugc_v5.png) (`slices/gallery.png`).
- PDP lifestyle images (files `fp-hw-hw1..4.png`, `fp-balk-res_before.png`, `fp-balk-res_after.png`, `fp-balk-an_health.png`, `fp-balk-an_self.png`) show women roughly 55–70 in dated Balkan kitchens/bedrooms, and step 4 "Виждаш резултат" shows an older man; the hero B/A shows a woman in her ~30s; the home "How it works" tiles and doctor images use a third, glossier stock/AI style — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30) (`slices/M-net-pdp-full-1.png`, `-2.png`); [Home](https://fitpatches.net/).
- Home before/after = a split close-up of a belly (pinched/soft vs flat) — [Home](https://fitpatches.net/) (`slices/M-net-home-full-0.png`).
- All PDP custom-section assets (tier thumbnails, `fp-spin.mp4`, `fp-doctor.png`, `fp-features.png`, how-it-works, before/after, analysis images, drawer thumbnail) are hot-linked from a different Shopify store's file CDN path (`cdn.shopify.com/s/files/1/1019/0929/9545/…`), while this store's own files live under `/1/1048/3269/6657/` (shop ID 104832696657) — [PDP HTML](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30); [Home HTML](https://fitpatches.net/).

**Speed / weight (Playwright, iPhone 13 emulation, no CPU/network throttling, through the session's proxy — treat as indicative)**
- PDP: 115 requests, ~4.7 MB transferred; 2.9 MB is the autoplay video `fp-spin.mp4` (in "Природата в помощ на фигурата"); 44 scripts ≈777 KB (incl. ~297 KB from connect.facebook.net); LCP ≈5.8 s; DOMContentLoaded ≈9.9 s; load ≈17.1 s; 1,736 DOM nodes; 57 `<img>`; CLS 0 — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30) (`audit/perf-pdp.json`).
- Home: 104 requests, ~2.3 MB; the Material Symbols icon font alone is 351 KB (used for 7 FAQ checkbox icons); LCP ≈4.2 s; load ≈10.7 s — [Home](https://fitpatches.net/) (`audit/perf-home.json`).
- Server time-to-first-byte for HTML via curl was 1.9–3.1 s for home/PDP (includes proxy overhead) — [Home](https://fitpatches.net/); [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).

### Inferences
- The visual identity splits into three systems (coral home, magenta PDP, orange EasySell), which makes the click from home to PDP feel like a different site and makes the COD popup look like a third-party form — both erode trust at the decision point.
- Persona drift (30-something B/A, 60+ "babushka" lifestyle shots, male reviewers and a male "result" image) dilutes identification for the core buyer (Bulgarian women; likely 30–55). Choosing one persona and using real customer photos would align the page with the ad.
- English-only packaging, garbled pack text in the hero composite and AI-looking faces are "cheap import" signals; they also undercut "Хиляди българи вече опитаха".
- Hot-linked assets from another store are a single point of failure: if that store's files are removed, most PDP imagery, the video and the cart-drawer thumbnail break at once.
- A 2.9 MB autoplay video and ~45 scripts are a poor fit for Meta in-app browsers on mid-range Android over mobile data; lazy-loading/compressing the video and dropping the 351 KB icon font are cheap wins.

### Gaps
- No real-user field data (CrUX/Shopify Web Performance) was checked; lab numbers are from an unthrottled emulator behind a proxy.

## 5. Copy, claims, FAQ quality and objection handling

### Takeaway
Copy is benefit-heavy and emotionally targeted ("Всяко преяждане ти струва фигура и самочувствие"), and the PDP objection accordion is the strongest copy on the site, but headline claims are extreme and inconsistent (8 kg/30 days vs "след 20 дни" vs reviews' 2–4 kg), the home FAQ is one-word answers (including a nonsensical "На диета съм? — Абсолютно."), ingredients and usage instructions differ between sections, and the science section contains a factual error.

### Cited Findings
**Result/time claims (all on-site)**
- Home H1 "КОНТРОЛИРАЙ АПЕТИТА И ОТСЛАБНИ ДО 8 КГ ЗА 30 ДНИ"; PDP H1 "Започни да сваляш килограми след 20 дни…"; home FAQ "Кога ще усетя ефект? — 7-14 дни — първи промени."; stats "…в 14 дни", "…в 45 дни"; PDP objection "Повечето клиенти усещат по-малко желание за храна още в първите дни. За видима промяна във фигурата дай на организма 4–8 седмици"; PDP disclaimer "Резултатите са индивидуални. За най-добър ефект — една лепенка на ден в продължение на 4–8 седмици." — [Home](https://fitpatches.net/); [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
- Claims of mechanism: "Трансдермален = без странични ефекти — Лепенката доставя берберин директно в кръвта." (home); "FitPatches доставя берберина трансдермално … Така до организма достига по-висока и по-стабилна концентрация, която действа върху ензима AMPK и върху апетита." (PDP) — no study, dose or absorption data is cited — [Home](https://fitpatches.net/); [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
- Safety claims: "Безопасни ли са? — 100% натурални." (home FAQ); "Натурални съставки, без странични ефекти." (PDP bullet); PDP objection "Има ли странични ефекти?" adds "При бременност, кърмене или прием на лекарства се консултирай с лекар преди употреба." — [Home](https://fitpatches.net/); [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
- EFSA's March 2026 draft opinion (Art. 8 procedure of Regulation 1925/2006, initiated by ANSES) concluded "no safe intake levels can currently be established" for berberine-containing plant preparations, citing genotoxicity signals, rodent tumour findings and idiosyncratic liver injury; consultation ran to 4 May 2026 — [NutraIngredients, 10 Mar 2026](https://www.nutraingredients.com/Article/2026/03/10/no-safe-intake-level-for-berberine-efsa-opens-consultation/).
- Meta's Health & Wellness ad standards were reportedly rewritten on 22 July 2026 to claims-based enforcement: before/after imagery no longer auto-rejected, but timeline promises (e.g., "lose 10kg in 10 days"), guaranteed outcomes and inferiority framing remain violations, and secondary sources advise stripping them from landing pages too (secondary blog source; no link to Meta's official text) — [Clikim](https://clikim.com/meta-health-wellness-policy-update/); [Adligator](https://adligator.com/blog/meta-health-wellness-ad-policy-update-2026).

**Home FAQ (complete answers, verbatim)**
- "Ще ми помогнат ли FitPatches? — Да." / "Какво съдържат? — Берберин, канела и екстракт от нар. 100% натурални." / "Как се използват? — Залепи на кожата 8 часа." / "Безопасни ли са? — 100% натурални." / "Кога ще усетя ефект? — 7-14 дни — първи промени." / "На диета съм? — Абсолютно." / "Какви бонуси? — Безплатна доставка, 30-дневна гаранция." — [Home](https://fitpatches.net/).

**PDP objection accordion ("ПРЕДИ ДА ПОРЪЧАШ — Знаем какво си мислиш.")**
- Six objections in the customer's voice: "Наистина ли работи? Как лепенка може да свали килограми?", "Пробвах други лепенки и добавки, но нямаше ефект.", "Честно казано, звучи ми като измама.", "Колко бързо ще усетя резултат?", "Има ли странични ефекти?", "А ако на мен не ми подейства?" — answers are 1–4 sentences, mechanism-based ("FitPatches не „топи мазнини“ с магия. Действа, като намалява апетита…"; "Не е чудо — а обяснима биохимия.") — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).

**Ingredient & usage inconsistencies**
- Ingredients: home FAQ "Берберин, канела и екстракт от нар"; main product description "берберин и нар"; bundle descriptions "берберин, канела и нар"; PDP gallery infographic lists six: "Берберин — Подпомага баланса на кръвната захар", "Хром — Подобрява инсулиновата чувствителност", "L-глутамин — Подпомага активността и възстановяването", "Витамин B комплекс — Поддържа стабилна енергия през деня", "Нар — Намалява възпалението и подпомага метаболизма", "Канела — Регулира апетита и енергийния баланс" — [Home](https://fitpatches.net/); [products.json](https://fitpatches.net/products.json); [ingredient infographic](https://cdn.shopify.com/s/files/1/1048/3269/6657/files/sustavki_patchove.png).
- Usage: home FAQ "Залепи на кожата 8 часа"; gallery "Носи я през целия ден … Сваляш вечерта"; PDP "Сутрин, върху чиста и суха кожа — ръка, корем или бедро"; gallery placement chart adds "рамото"; home review "Залепям на рамото сутрин, свалям вечер" — [Home](https://fitpatches.net/); [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30); [gallery](https://cdn.shopify.com/s/files/1/1048/3269/6657/files/fp-detail-howto.png).
- PDP "ПРИРОДНА ФОРМУЛА" says berberine "се съдържа в растения като жълт кантарион и берберис" — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30). Berberine's commonly listed plant sources are Berberis spp. (barberry, Oregon grape), Hydrastis canadensis (goldenseal) and Coptis chinensis; St John's wort (жълт кантарион, Hypericum) is not among them — [Wikipedia: Berberine](https://en.wikipedia.org/wiki/Berberine); [ScienceDirect topic: Berberine](https://www.sciencedirect.com/topics/pharmacology-toxicology-and-pharmaceutical-science/berberine).

**Other copy observations**
- PDP benefit bullets: "Всяко преяждане ти струва фигура и самочувствие. FitPatches ти помага да овладееш глада, без да се измъчваш." / "По-малко желание за сладко и нездравословни храни още в първите дни." / "Хиляди клиенти усещат по-стабилен апетит през целия ден — без диети и без хапчета." / "Натурални съставки, без странични ефекти. Една лепенка на ден — толкова е просто." — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
- PDP "Научен анализ" contains no study about berberine or patches; its three cards cite only WHO data on obesity risk ("От 1990 г. насам затлъстяването в света се е повече от удвоило", "Източник: СЗО (WHO)") and two emotional essays ("Не е въпрос на воля. Въпрос е на глад.", "Не е само за дрехите. За самочувствието е.") — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
- The main product title shown in cart/checkout is the 14-word headline "Започни да сваляш килограми след 20 дни…" — [Cart](https://fitpatches.net/cart).

### Inferences
- "На диета съм? — Абсолютно." is presumably meant as "Мога ли да ги ползвам, ако съм на диета?" but reads as "you must diet", contradicting "БЕЗ ДИЕТИ"; one-word answers ("Да.", "100% натурални.") on a home page that is supposed to handle objections signal low effort and raise rather than lower suspicion. The PDP accordion copy should replace them.
- Mixed result promises (8 kg/30 days vs 20 days vs 4–8 weeks vs reviews' 2–4 kg/month) let the skeptic catch the brand in a contradiction; a single, believable promise built around appetite/cravings (the mechanism the site itself emphasises) would be more credible and is more defensible under Meta's claims-based rules and Reg. 1924/2006 Art. 12.
- With EFSA's 2026 berberine safety opinion in the public domain, "100% натурални" as the entire safety answer and "без странични ефекти" are both a credibility and a liability problem.
- Listing three ingredients in one place and six (incl. chromium, L-glutamine, B-vitamins) in another, with no dose per patch anywhere, undermines "100% натурално" and makes the product look improvised.

### Gaps
- No dosage/ingredient amounts per patch, manufacturer, country of origin or any certificate are published on the site, so these could not be verified.

## 6. Funnel mechanics: CTA → cart drawer → COD form/checkout; upsells; tracking

### Takeaway
There are three different, partly contradictory ways to order — (1) "Поръчай сега" → custom cart drawer → Shopify checkout, (2) an orange EasySell "Поръчай" COD popup inside the drawer that shows no product, price or shipping, and (3) a "leave your name and phone and we'll call you" form that actually captures nothing and silently redirects to Shopify checkout — plus English strings, a broken savings row and a second-pixel tracking setup that risks duplicated/split events.

### Cited Findings
**Path 1 — "Поръчай сега" (main CTA)**
- Click → `POST /cart/add.js` with the selected variant (quantity 1, existing cart contents are kept) → `fbq('track','AddToCart',{content_ids:['fitpatches'],…})` → opens a custom slide-in cart drawer (`window.fpCart.open()`); fallback `/cart` — [PDP HTML](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
- Drawer contents (observed): "Остават 55.01 EUR до безплатна доставка" progress bar; line item with product title, qty −/+, "Премахни", price; upsell card "Може още да ти хареса — 3 пакета + 1 подарък 119.96 39.99 [Добави]"; "Крайна сума: 14.99 EUR"; a "Спестени:" row rendered with no value; then two stacked full-width buttons — orange "🛍 Поръчай" (EasySell) and pink "Преминаване към плащане" (→ `/checkout`); badges "Наложен платеж · 60 дни гаранция". Line items show no compare-at strike-through; in the test capture two of three line-item thumbnails were blank — [PDP drawer](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30) (`audit/drawer-tier1.png`, `audit/drawer-tier3.png`).
- "Преминаване към плащане" reached Shopify's standard checkout at `fitpatches.net/checkouts/cn/<token>/bg-bg` (Bulgarian locale) — [Checkout redirect](https://fitpatches.net/checkout) (`audit/funnel.log`).

**Path 2 — EasySell COD Form (app "easysell-cod-form", app-embed active)**
- Opened from the drawer's orange "Поръчай": popup titled "Предпочиташ по-лесна поръчка?" with five required fields — "Две Имена", "Телефон", "Адрес на Еконт и Град", "Пощенски код" (digits only), "Регион" (dropdown in Latin transliteration: "Blagoevgrad … Sofia, Sofia City … Yambol") — and an orange "Поръчай" submit button. No product, quantity, price, total, shipping cost or delivery time is displayed in the form — [EasySell popup on PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30) (`audit/easysell-popup.png`).
- EasySell config (embedded `EASYSELL_CONFIG`): `form_type: "popup"`, `placement: "both"`, `cod_gateway: true`, `draft_order: false` (creates real orders), `cart_content`/`order_summary`/`shipping_options` fields all `hide: true`, `include_upsell: false`, `disable_abandoned: true`, `buyer_accepts_marketing` hidden, `otp_first: false`, `auto_detect_pixels: true` with `fbSendAPI: true`, `fbICEvent: "InitiateCheckout"`, `fbPurchaseEvent: "Purchase"`; untranslated strings "This field is required.", "This field is invalid.", "Sold Out", "Sorry, you are not allowed to place more orders…"; `thankyou_text` template in English ("Thank You, {{customer.first_name}}! 🎉 Your order {{order.number}} is confirmed … Order Summary"); `redirect_url: "https://shopify.com"` with `redirects: "default"` — [Home HTML](https://fitpatches.net/).

**Path 3 — "Предпочиташ по-лесна поръчка?" call-back form on the PDP**
- Copy: "Остави име и телефон и ще се свържем с теб за потвърждение на поръчката и адреса." + "Избран пакет: 3 пакета + 1 подарък · 39.99 EUR" + fields "Име", "Телефон (0888 123 456)" + button "Изпрати заявка" — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
- Code: on submit it validates name (≥2 chars)/phone (≥6 digits), fires `InitiateCheckout`, sends the lead to `endpoint` only if set — but the section has `data-endpoint=""` (empty), so the lead is not stored anywhere — then calls `/cart/clear.js`, adds the selected variant and redirects to `/checkout?checkout[shipping_address][first_name]=…&checkout[shipping_address][phone]=…` (button text changes to "Пренасочване…") — [PDP HTML](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).

**Cart page & other UX**
- `/cart` (theme cart page) shows English blocks "You may also like", "Subscribe to our emails — Join our email list for exclusive offers and the latest news. — Sign up"; collection filters show "Availability", "Price" — [Cart](https://fitpatches.net/cart); [Collection](https://fitpatches.net/collections/all).
- No post-purchase upsell app, no email/SMS capture, no review-request app was detected in storefront code (only EasySell, Meta pixels, Shopify's own pixels and one unidentified analytics web pixel with `siteId "jsmNXNjuV1bThvEs"`) — [Home HTML](https://fitpatches.net/).

**Tracking**
- Theme `<head>` hard-codes Meta Pixel `1036098062073138` (`fbq('init')` + PageView); the Facebook & Instagram app web pixel uses a different pixel `1051819453965625` (`dataSharingState: "optimized"`, CAPI enabled); a Shopify custom pixel named "Meta FitPatches COD" also exists; the PDP offer section is configured with `data-pixel="1051819453965625"` but only initialises it if `fbq` is undefined (it never is, because the theme already loaded 1036098062073138) — [Home HTML](https://fitpatches.net/); [PDP HTML](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
- Custom events use `content_ids:['fitpatches']` (not variant IDs) and `InitiateCheckout` is fired on the call-back form submit (before any checkout) — [PDP HTML](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).

### Inferences
- The call-back form is the most serious funnel defect after the title mismatch: it promises a phone call (a strong COD-market reassurance), then dumps the user into a full Shopify checkout; anyone who abandons there was promised a call that will never come, and their name/phone is not saved anywhere (Shopify only records an abandoned checkout if contact info is entered in checkout).
- Two adjacent primary buttons in the drawer with different colours, labels and destinations ("Поръчай" vs "Преминаване към плащане") create choice friction; the EasySell form that hides price, total and shipping is the opposite of reassurance for COD buyers and may also fall short of EU pre-contract information requirements (to be checked by the compliance researcher).
- "Поръчай сега" never clears or de-duplicates the cart, and the upsell adds a second bundle rather than upgrading, so stacked/duplicate bundles are possible (observed in testing: 3+1 + 2+1 = €67.98 cart) — expect some COD refusals or "I only wanted one" calls.
- Two Meta pixels plus EasySell auto-detected pixels/CAPI plus a custom pixel risk double-counted or split AddToCart/InitiateCheckout/Purchase events, weakening Meta's optimisation signal; consolidating on one pixel with deduplicated CAPI is a measurement prerequisite for any CRO testing.

### Gaps
- Shopify checkout contents (shipping fee, COD availability/fee, express wallets, field count, language quality) could not be captured due to bot protection (HTTP 429).
- Whether the EasySell English thank-you template or Shopify's own thank-you page is shown after a COD order could not be verified without ordering.
- The owner of the hot-linked shop path `1019/0929/9545` and of pixel `1036098062073138` could not be identified from outside.

## 7. Issues ranked by likely conversion impact (high → low)

### Takeaway
The biggest leaks are structural (CTA placement, offer/title mismatch, three conflicting order paths, hidden shipping cost) rather than cosmetic; fixing the first five would likely move conversion more than any redesign, while the claims/social-proof problems are simultaneously a trust leak and an ad-account/legal risk.

### Cited Findings
1. **No CTA/sticky ATC on ~80% of the PDP; home has no price and one CTA below the fold** — buy button only at ≈1,700 px of ≈10,300 px; no sticky bar; home links to the product once — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30); [Home](https://fitpatches.net/).
2. **Selected tier ≠ product in cart** — "2 пакета" → "2+1 ПОДАРЪК" (3 packs per description); "3 пакета + 1 подарък" → "2+1 БЕЗПЛАТНО ПОДАРЪК" (handle 5+5, description 10 packs); 1 pack → headline as title; bundle URLs reuse the same selector — [products.json](https://fitpatches.net/products.json); [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
3. **Three conflicting order paths; call-back form captures nothing** (`data-endpoint=""`, redirect to checkout); EasySell popup hides price/total/shipping; dual CTAs in drawer — [PDP HTML](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
4. **Shipping cost hidden + contradictory free-shipping rules** (€60 home, €70 drawer, "Безплатна доставка" FAQ; no offer qualifies; shipping policy 404) — [Home](https://fitpatches.net/); [Shipping policy 404](https://fitpatches.net/policies/shipping-policy).
5. **Weak/contradictory risk reversal** (30-day money-back vs "60 дни гаранция" vs "просто не поръчваш пак"; refund policy 404; no guarantee in PDP offer block) — [Home](https://fitpatches.net/); [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30); [Refund 404](https://fitpatches.net/policies/refund-policy).
6. **Legitimacy gaps** — empty footer, no company identity/ЕИК/address, terms/refund/shipping 404, hidden cart icon, no menu, English UI strings, "Правила за повелителност" typo, "Powered by Shrine" — [Privacy](https://fitpatches.net/policies/privacy-policy); [Contact](https://fitpatches.net/pages/contact); [ЗЕТ](https://www.mi.government.bg/file/2015/09/zet_bg.pdf).
7. **Implausible, hard-coded social proof** (1,837 vs 1,012 vs "над 1000"; 4.8 vs 4.5 stars; reviews dated before product creation; Facebook-UI mock; AI-style faces; unverifiable doctor/"50+ диетолози"; unsourced 97/95/92%) — [Home](https://fitpatches.net/); [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30); [UCPD guidance 23b/23c](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A52021XC1229%2805%29).
8. **Page weight/speed** — PDP ≈4.7 MB, 2.9 MB autoplay video, 44 scripts, LCP ≈5.8 s / load ≈17 s (lab) — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30) (`audit/perf-pdp.json`).
9. **Visual/persona inconsistency** — coral home vs magenta PDP vs orange EasySell; 30s B/A vs 60+ AI lifestyle vs male reviewers; English-only pack; garbled composite pack text; assets hot-linked from another store — [Home](https://fitpatches.net/); [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
10. **Fake-feeling urgency & price labels** — midnight-loop timer; "-50%" badge beside "66%"; Sunday "Доставено" date vs "2–4 работни дни"; compare-at counts the gift at full price — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30); [UCPD Annex I](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A02005L0029-20220528).
11. **Copy quality** — one-word FAQ answers, "На диета съм? — Абсолютно.", inconsistent ingredients (3 vs 6) and usage (8 h vs all day), "жълт кантарион" error, extreme/inconsistent result claims — [Home](https://fitpatches.net/); [ingredient infographic](https://cdn.shopify.com/s/files/1/1048/3269/6657/files/sustavki_patchove.png).
12. **Compliance exposure that can cut traffic** — weight-loss rate/timeline claims (Reg. 1924/2006 Art. 12; Meta claims-based rules), Ozempic equivalence + Ozempic imagery, doctor endorsement, "без странични ефекти" despite EFSA 2026 berberine opinion — [Reg. 1924/2006](https://eur-lex.europa.eu/eli/reg/2006/1924/oj/eng); [NutraIngredients](https://www.nutraingredients.com/Article/2026/03/10/no-safe-intake-level-for-berberine-efsa-opens-consultation/); [Clikim](https://clikim.com/meta-health-wellness-policy-update/).
13. **Measurement noise** — two Meta pixels + EasySell CAPI + custom pixel; generic `content_ids`; InitiateCheckout on a non-checkout form — [Home HTML](https://fitpatches.net/); [PDP HTML](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).

### Inferences
- Quick wins (hours, not weeks): add a sticky "Поръчай сега – 39.99 EUR" bar on the PDP and repeat the selector/CTA after the proof sections; rename the two bundle products to match the selector exactly (e.g., "FitPatches – 2 пакета (60 лепенки)", "FitPatches – 3+1 пакета (120 лепенки)") and give the 1-pack a neutral title; state the delivery fee next to the CTA and set free shipping to apply to the 2-pack and 3+1 tiers; unify the guarantee (one number, one wording, plus a real refund/shipping/terms page and company details in the footer); pick one COD path (either EasySell with a visible order summary in brand colours, or Shopify checkout) and either wire the call-back form to a real endpoint/Google Sheet/Shopify draft order or remove it.
- Medium effort: replace hard-coded reviews/FB mock with a real review app seeded from actual customers (with photo reviews), cut the Ozempic and "8 кг за 30 дни" claims, align ingredients/usage text with the actual product leaflet, compress/defer the video, unify palette/persona.
- Because COD orders can be refused at the door, consistency between what was clicked, what the confirmation says and what arrives (item 2) affects not just conversion rate but delivered-order rate and courier costs.

### Gaps
- No access to Shopify analytics (sessions, add-to-cart rate, checkout reach, COD refusal rate) was used in this audit, so the ranking is based on CRO heuristics and the severity of the observed defects, not on measured drop-off.
