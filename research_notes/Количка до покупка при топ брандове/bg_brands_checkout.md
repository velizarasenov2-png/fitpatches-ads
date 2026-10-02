# From "added to cart" to a paid order: cart, checkout and COD flow teardown of InaEssentials and other Bulgarian/Balkan DTC health & beauty brands (observed 2 Oct 2026)

**Method.** Every site fact below was observed live on **2 Oct 2026** with Playwright. The browser emulated an iPhone 13 (390 px wide, locale bg-BG, timezone Europe/Sofia).

For each brand, the walk-through followed the same path:
1. Open the product page.
2. Tap the real add-to-cart button.
3. Screenshot what opened.
4. Tap the cart/checkout button.
5. Screenshot the checkout or COD form.

**Safety and data rules:**
- No order was placed. No form was submitted. No personal data was typed into any form.
- The walking script had a hard guard: it refused to click any submit button inside a form that contained name or phone fields. It blocked VitaPatch's "Поръчай бързо" twice.
- To read delivery prices, Shopify's public `/cart/shipping_rates.json` endpoint was called with the generic postcode 1000 / Sofia. Because of that call, "1000 / Sofia" appears pre-filled in the Tasty Dose checkout screenshot.

**Ad volume.** Counts come from the Meta Ad Library API (BG, active ads, 2 Oct 2026). They are estimates, and the API does not return landing-page URLs.

**Evidence files.** Screenshots and text dumps are in `/tmp/claude-0/-home-user-fitpatches-ads/77d5f012-1d96-5267-aa86-a2c530bc0277/scratchpad/shots/co-bg-*`:
- Ina: `co-bg-ina-1atc.png` (post-ATC upsell), `co-bg-ina-1drawer.png`, `co-bg-ina-co-sheet0.png` (checkout)
- Smile: `co-bg-smile-1atc.png`, `co-bg-smile-2checkout.png` + `-2co-c.png` (Sendica pop-up), `co-bg-smile-3shopco.png`
- VitaPatch: `co-bg-vita-1atc.png`, `co-bg-vita-co-sheet0.png`, `co-bg-vita-0quick.png`
- Tasty Dose: `co-bg-tasty-1atc.png`, `co-bg-tasty-1drawer.png`, `co-bg-tasty-co-sheet0.png`
- forlife: `co-bg-forlife-1atc.png`, `co-bg-forlife-co-sheet.png`, `co-bg-forlife-courier.png`
- Chillama: `co-bg-chil-order-sheet0.png`
- Valendy: `co-bg-valendy-2checkout.png`
- FitPatches: `co-bg-fp-2easysell.png`
- Contact sheets: `co-bg-sheetA/B/C.png`
- Walk logs: `co-bg-<brand>-log.txt`
- Walk script: `scratchpad/cowalk.js`; per-site configs in `scratchpad/cfg/`

**FitPatches baseline (user-provided Shopify data, 90 days to 2 Oct 2026):**

| Metric | Value |
|---|---|
| Sessions | 5,653 |
| Sessions with add-to-cart | 608 (10.8%) |
| Reached Shopify checkout | 160 |
| Completed Shopify checkout | 77 (48% of those who reached it) |
| EasySell COD-form orders | 244 |
| Total orders | 324 (about 53% of add-to-cart sessions; about 75% of orders came through EasySell) |
| AOV | €27.64 |

---

## Q0. What is "Inna Essentials", and which brands were benchmarked (and why)?

### Takeaway
"Inna Essentials" is almost certainly **InaEssentials (inaessentials.com)**. It is a Bulgarian family brand of organic and bio cosmetics. It runs a Shopify store and is by far the heaviest Meta advertiser in this set, with about 613 active ads in Bulgaria.

The benchmark set covers several platforms:
- Shopify stores: InaEssentials, Smile Patches, Tasty Dose, and Valendy (a small control)
- a custom Next.js store: VitaPatch
- WooCommerce: forlife.bg
- a custom platform: Chillama

### Cited Findings

**Identifying the brand**
- An exact-phrase search for "Inna Essentials" returns only an Apple Music playlist for the Romanian singer INNA. No company uses that exact spelling — [Apple Music](https://music.apple.com/us/playlist/inna-essentials/pl.717990502ab246a09f0d1d4a0eae7c9d).
- The Bulgarian search "Inna Essentials България" returns InaEssentials (one "n"):
  - pharmacy listings on Galen.bg, Аптека Нове and Framar — [Galen.bg](https://galen.bg/brands/ina-essentials), [Framar](https://apteka.framar.bg/%D0%BF%D1%80%D0%BE%D0%B8%D0%B7%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB/ina-essentials)
  - the employer "InaEssentials LTD" on jobs.bg — [jobs.bg](https://www.jobs.bg/en/company/314994)
- InaEssentials describes itself as "Семеен Онлайн Магазин за 100% Био Козметика" — [inaessentials.com](https://inaessentials.com/).
- Its homepage FAQ claims "повече от 100,000 доволни клиенти в цяла Европа" — [inaessentials.com](https://inaessentials.com/).
- Its Facebook page is "InaEssentials - Семеен Онлайн Органичен Магазин за Био Козметика" (page ID 388962071556621) — [Meta Ad Library ad 1722886143533582](https://www.facebook.com/ads/library/?id=1722886143533582).

**Platform and apps detected on inaessentials.com (page HTML and network)**
- Shopify
- Shrine theme
- Klaviyo
- Judge.me
- Recart ("recart-sms-list-growth")
- Brevo
- Zipchat AI chatbot
- Nice-Team bundler
- Shipwill "insurance.js"
- a custom app called "INA Post Purchase", hosted on ina-post-purchase.vercel.app

Sources: [inaessentials.com PDP](https://inaessentials.com/products/florasync-active-intimna-pyana-layka); [ina-post-purchase.vercel.app](https://ina-post-purchase.vercel.app/) (an embedded Shopify admin dashboard titled "INA Post Purchase").

**Meta ad volume (BG, active, 2 Oct 2026)**

| Brand | Active ads | Source |
|---|---|---|
| InaEssentials | ~613 | [Ad Library page 388962071556621](https://www.facebook.com/ads/library/?id=1472842058019255) |
| Tasty Dose (3 pages) | ~184 | [ad 2877415902627486](https://www.facebook.com/ads/library/?id=2877415902627486) |
| Smile Patches | ~168 | [ad 1605222694312480](https://www.facebook.com/ads/library/?id=1605222694312480) |
| forlife.bg | ~61 | [ad 1470836138208121](https://www.facebook.com/ads/library/?id=1470836138208121) |
| Chillama – България | ~57 | [ad 3031993197143439](https://www.facebook.com/ads/library/?id=3031993197143439) |
| VitaPatch.bg | ~6 | [ad 2122780684978495](https://www.facebook.com/ads/library/?id=2122780684978495) |
| Valendy.com | 1 | [ad 1119801123810859](https://www.facebook.com/ads/library/?id=1119801123810859) |

A keyword search for "InaEssentials" across all statuses estimates about 5,925 ads.

**InaEssentials ad headlines are almost all gift-with-purchase offers**, for example:
- "❤️ Купи 2 и вземи шампоан и балсам подарък" — [ad 1412975120255045](https://www.facebook.com/ads/library/?id=1412975120255045)
- "❤️ Купи 2 крема за вени, третият е подарък" — [ad 2166721700866592](https://www.facebook.com/ads/library/?id=2166721700866592)
- "2 пени, 2 подаръка" — [ad 1472842058019255](https://www.facebook.com/ads/library/?id=1472842058019255)
- "Плащаш само пените" — [ad 1864356468258121](https://www.facebook.com/ads/library/?id=1864356468258121)

**Other brands in the set**
- **Tasty Dose** is a multi-country brand. Its x-default hreflang points to `/sl-si`, and it has storefronts for about 20 EU locales, including `bg-bg`, `ro-ro`, `hr-hr` and `el-gr`. It claims "MORE THAN 400K SATISFIED CUSTOMERS" — [tastydose.com](https://tastydose.com/); [tastydose.com/bg-bg](https://tastydose.com/bg-bg/products/energy-2-0-starter-pack).
- **Chillama** sells supplements from a Plovdiv base (бул. Христо Ботев 122), has country storefronts on chillama.co, and accepts COD or card — [chillama.co/bg](https://chillama.co/bg/). Its ads claim "✅40000 доволни клиенти" — [ad 1614301403699756](https://www.facebook.com/ads/library/?id=1614301403699756).
- **Smile Patches:** "4.78/5 на базата на 10,250 мнения" on its berberine PDP — [smilepatchesbg.com](https://smilepatchesbg.com/products/berberin-lepenki).
- **VitaPatch** is run by "ВИТА ДОЗА" ООД (Плевен) — [vitapatch.bg](https://vitapatch.bg/dostavka-i-plashtane).

### Inferences
- "Inna Essentials" in the user's request is very likely a misspelling of InaEssentials. Four things point to it:
  - It is the only Bulgarian brand matching that name.
  - It is in the health and beauty category.
  - It is a very heavy Meta advertiser.
  - It runs an offer style (gift-with-purchase bundles) similar to FitPatches' bundle model.
- InaEssentials sells cosmetics, not supplements. Its cart and checkout mechanics are product-agnostic, so they transfer to FitPatches.
- Valendy is kept only as a small control: it has a single active ad, so it is not a "high-performing" benchmark.

### Gaps
- No public revenue or conversion-rate figures were found for any of these brands. Ad counts are a proxy for spend, not proof of performance.
- The Ad Library API gives no destination URLs. The product pages walked were chosen to match current ad themes:
  - InaEssentials: the FloraSync intimate foam ad
  - Smile: berberine
  - VitaPatch: berberine
  - Tasty Dose: Energy 2.0 starter pack
  - forlife: berberine capsules
  - Chillama: SugarSentry

---

## Q1. What exactly happens after "add to cart" on each site? (Flow, steps, order-form app, fields, courier/office picker, whether delivery price and total are shown)

### Takeaway
Every high-volume brand funnels the shopper into **one clearly primary path**, and every order screen shows a **line-item summary, delivery price and total** before the final tap.

Courier and office selection is a **structured picker**: tiles, tabs, city autocomplete plus office dropdown, or a search box. The shopper never types free text for this.

Typical required typing is 5–7 fields, and most brands add email. Five distinct models were observed:

| Model | Brands |
|---|---|
| Shopify checkout with heavy customisation | InaEssentials, Valendy |
| Pre-checkout courier pop-up, then Shopify checkout | Smile Patches, using the Sendica Pickup Points app |
| Custom one-page COD checkout | VitaPatch, Chillama, forlife |
| Prepaid-only Shopify checkout | Tasty Dose |
| PDP call-back "quick order" as a secondary path | VitaPatch |

### Cited Findings

**Comparison table (mobile, observed 2 Oct 2026)**

| Brand | What opens after ATC | Screens from ATC to final button | Required typed fields at order | Courier/office selection | Delivery price shown before final tap? | Total shown in order form? | Payment options |
|---|---|---|---|---|---|---|---|
| **InaEssentials** (Shopify) | Full-screen timed upsell ("Офертата изтича след 04min 55sec") over the cart drawer | 3: upsell → drawer → Shopify one-page checkout | 7: email, first name, last name, address, postcode, city, phone | Shipping options appear after the address is entered: Speedy office €2.80, Econt office €3.20, BOX NOW locker €1.90 (card only), personal address €4.00; free over €40 | Yes (checkout) | Yes | Card (pre-selected), Revolut Pay, COD "(+ 0.99€)"; Google Pay express |
| **Smile Patches** (Shopify + Sendica + Releasit COD Fee) | Cart drawer | 3: drawer → Sendica pop-up ("ПРОДЪЛЖИ →") → Shopify checkout | Pop-up: Име, Фамилия, Телефон (+ optional Имейл) and an office search. Shopify checkout: email or phone, names, address, postcode, city, phone (pre-fill not verified) | Tabs "До Офис/Автомат" / "До Адрес"; Speedy €2.50, Econt €3.40, BoxNow free (card only); search box "Напиши град, офис или адрес" | Yes (pop-up) | Yes | COD "(+0.99€)" listed first, then card |
| **VitaPatch** (custom Next.js) | Cart drawer | 2: drawer → one-page checkout | Име и фамилия, Телефон, Имейл, city (autocomplete), office (dropdown); plus 2 consent checkboxes | Tiles Econt/Speedy, then "До офис"/"До адрес", then "Населено място" autocomplete, then "Офис на Еконт" | Yes ("Безплатна" for the 3+2 bundle; €2.99 for 1 pack) | Yes, and on the button: "Завърши поръчката — 41,70 €" | COD only |
| **Tasty Dose** (Shopify, UpCart + Rebuy) | Timed upsell pop-up ("ОГРАНИЧЕНА ОФЕРТА…", 2:54 countdown) | 3: pop-up → drawer → Shopify checkout | Email, first name, last name, street, house number, postcode, city, phone; plus Packeta pickup-point selection | Packeta pickup point €3.90 or standard €4.50, "3 to 5 business days" | Yes | Yes | Card, PayPal, Revolut Pay; express Shop Pay / PayPal / Google Pay; **no COD** |
| **forlife.bg** (WooCommerce) | Side cart | 2: side cart → one-page checkout with a 3-step progress bar | Име, Фамилия, Телефон, Имейл, city (dropdown), office (dropdown), postcode; terms checkbox | Logo tiles: Офис Speedy / Офис Еконт / BOX NOW / До адрес | Yes (€3.00) | Yes (incl. VAT) | COD pre-selected; card via Stripe ("Payment options") |
| **Chillama** (custom) | No cart: "Поръчай" opens the order page directly | 1: order page | Имейл, Име и фамилия, Мобилен телефон, Град, Адрес | Radio: Pigeon to address (default) / Speedy office / Pigeon office | Yes (€2.60) | Yes (€27.50) | COD pre-selected ("Преглед преди плащане"), card (Mollie), PayPal |
| **Valendy** (Shopify, control) | Redirect to the /cart page | 2: cart page → Shopify checkout | Email or phone, first name, last name, address, postcode, city, phone | After the address: BOX NOW €2.99, Speedy office €3.79, Econt office €3.99… | After the address | Yes | Card, COD; Shop Pay / Google Pay express |
| **FitPatches** (Shopify + EasySell) | Custom drawer with two stacked primary buttons | 2: drawer → EasySell pop-up, OR drawer → Shopify checkout | EasySell: "Две Имена", "Телефон", "Адрес на Еконт и Град" (free text), "Пощенски код", "Регион" (Latin dropdown) | **None**: office typed as free text | **No** | **No** | COD only in the pop-up |

**Sources for the table rows:**
- InaEssentials: [PDP](https://inaessentials.com/products/florasync-active-intimna-pyana-layka); [shipping policy](https://inaessentials.com/policies/shipping-policy)
- Smile Patches: [PDP](https://smilepatchesbg.com/products/berberin-lepenki)
- VitaPatch: [PDP](https://vitapatch.bg/products/berberine); [checkout](https://vitapatch.bg/checkout)
- Tasty Dose: [PDP](https://tastydose.com/bg-bg/products/energy-2-0-starter-pack)
- forlife: [PDP](https://www.forlife.bg/produkt/berberin); [checkout](https://www.forlife.bg/checkout)
- Chillama: [PDP](https://chillama.co/bg/products/chillama-sugar-sentry); [order page](https://chillama.co/bg/order/)
- Valendy: [PDP](https://www.valendy.com/products/pms-balance)
- FitPatches: [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30)

**Step-by-step detail per brand**

*InaEssentials*
- The PDP bundle selector "КУПИ ПОВЕЧЕ - СПЕСТИ ПОВЕЧЕ" has "Купи 1 €15,99" and "Купи 2, Вземи Шампоан роза + Балсам Безплатно" ("НАЙ-ПРОДАВАНО", "Спестяваш €21,48", €31,98, struck €53,46).
- The two-pack is **pre-selected**, and the free gifts are pictured with red "€0.00" tags.
- One tap on "ДОБАВЯНЕ КЪМ КОЛИЧКАТА" put **2 foams + 2 free gifts** (shampoo €9.99 → €0, balm €11.49 → €0) in the cart. The `/cart.js` total was €31.98.
- Source: [Ina PDP](https://inaessentials.com/products/florasync-active-intimna-pyana-layka).
- Right after add-to-cart, a full-screen layer opens titled "Пазарувай с голяма отстъпка сега", with a countdown "Офертата изтича след: 04min 55sec". It lists other products with yellow "Добави в количката +" buttons, for example "Bio Лавандулова Вода… Купете 2, Получете 1 Безплатно €13,98 ~~€20,97~~ (33% отстъпка)". It has two exits: green "ОТИДИ В КОЛИЧКАТА" and "ПРОПУСНИ И ПРОДЪЛЖИ" — [Ina PDP](https://inaessentials.com/products/florasync-active-intimna-pyana-layka).
- The drawer behind it shows:
  - "Количка • 4 продукта"
  - a 3-milestone progress bar: "Още €8,02 до БЕЗПЛАТНА доставка!" with icons for Безплатна доставка / Безплатен подарък / Голям безплатен подарък. The thresholds are €40 free delivery, €50 for a "мистериозен подарък" worth over €7, and €120 for a gift worth over €51.
  - gift lines showing "Обичайна цена €9,99 … €0,00 (Спестяваш €9,99)"
  - "Подарък-изненада 🎁 4,99 € → 0,00 € БЕЗПЛАТЕН само при плащане с карта"
  - "ОТСТЪПКА - €21,48"
  - "ОБЩО €31,98"
  - a green "Преминаване към плащане" button
  - payment logos including Apple Pay, Google Pay and "Cash on delivery"
  - Source: [Ina PDP drawer](https://inaessentials.com/products/florasync-active-intimna-pyana-layka)
- "Преминаване към плащане" goes to the Shopify one-page checkout (`/checkouts/cn/…/bg-bg`). Its contents, in order:
  - "Експресно плащане" (Google Pay in Chromium)
  - "Контакт" with email
  - **pre-checked** "ВАЖНО: Искам да получа имейл с потвърждение на поръчката си, имейли с промоции…"
  - "Доставка" with the address fields
  - **pre-checked** "Искам да получа БЕЗПЛАТЕН СМС при получаване на пратката си" with a phone field pre-filled "+359"
  - "Плащане", with "Кредитна/Дебитна карта" selected by default, then "Платете с карта или със сметката си на Revolut", then "Наложен платеж (+ 0.99€)"
  - a green box: "✅ Подаръкът-изненада ще бъде добавен към пратката ви! 🎁 … Добавя се САМО към поръчки, платени с карта"
  - a cross-sell block "Хората купуват често:" (Ina Dent-All pack €14.97, SPF 50 €19.99, gift box €1.49, each with "+ Добави")
  - the final button "Платете сега"
  - Source: Shopify checkout reached from the [Ina drawer](https://inaessentials.com/cart)
- Shipping policy: Speedy €2.80, Econt €3.20, BOX NOW €1.90, personal address €4.00, free over €40, "*Такса наложен платеж: 0.99 €"; orders received by 14:00 on a working day are delivered within 2 working days. Rate names include "(възможност за наложен платеж)" and "(само с картово плащане)" — [Ina shipping policy](https://inaessentials.com/policies/shipping-policy); [/cart/shipping_rates.json](https://inaessentials.com/cart).

*Smile Patches*
- On the PDP, the three tiers are radio buttons:
  - "Купи 1 пакет — €14,99"
  - "Купи 2 Вземи 1 Безплатно — €26,99"
  - "БЕЗПЛАТНА ДОСТАВКА — Купи 3 Вземи 2 Безплатно — €43,99"
- The PDP also shows "Поръчай сега за доставка преди 4. Октомври". One tap on "КУПЕТЕ СЕГА" added **3 units** (the 2+1 tier was the default) — [Smile PDP](https://smilepatchesbg.com/products/berberin-lepenki).
- The drawer shows:
  - "Количка • 3 броя"
  - a gift progress bar: "Поздравления! Получавате 1 безплатен"
  - the line item "~~€23,52~~ €9,00 · 2+1 ПОДАРЪК", "~~€70,56~~ €26,99 Спестявате €43,57"
  - a cross-sell "За пълна грижа за вашето тяло може да комбинирате с:" (3 other patches, each "€14,99 ~~€23,52~~ ДОБАВИ")
  - "Отстъпка -€43,57", "Общо €26,99"
  - payment logos
  - one blue "Преминаване към плащане" button
  - footer badges "ДОСТАВКА С ЕКОНТ И СПИДИ" and "НАЛОЖЕН ПЛАТЕЖ"
  - Source: [Smile PDP drawer](https://smilepatchesbg.com/products/berberin-lepenki)
- "Преминаване към плащане" does **not** leave the page. It opens a full-screen pop-up from the **Sendica Pickup Points** app. The app's assets are `sendica-pickup-points-246/assets/pickup-point-popup.js` and `i18n-bg.js`; the DOM uses `#spp-dialog`. The pop-up shows:
  - "Информация за поръчката EUR 26.99"
  - "Вашите данни": Име, Фамилия, Имейл, Телефон with a 🇧🇬 country-code picker
  - "Избери начин за доставка", with tabs "До Офис/Автомат" and "До Адрес"
  - carrier cards: "До офис/автомат на Спиди EUR 2.50", "До офис на Еконт EUR 3.40", "BoxNow (само с карта) Безплатно"
  - an office search box "Напиши град, офис или адрес"
  - an order summary: 3 units, "2+1 ПОДАРЪК (-EUR 17.98)", a discount-code box, Междинна сума, Отстъпка, Доставка, Общо
  - a blue "ПРОДЪЛЖИ →" button
  - Source: [Smile PDP](https://smilepatchesbg.com/products/berberin-lepenki)
- In one capture the summary read "Доставка: EUR 2.50 … Общо: EUR 26.99", i.e. the total did not visibly include delivery. Another capture showed "Доставка: Безплатно". This looks like an inconsistency in the app's summary.
- The page also loads the **Releasit COD Fee** app embed (`releasit-cod-fee-158`). The older Releasit COD *form* is no longer what the shopper sees — [Smile PDP HTML](https://smilepatchesbg.com/products/berberin-lepenki).
- Sendica's app-store listing describes "a pre-checkout popup allowing customers to select their preferred delivery method before proceeding to the standard Shopify checkout". It supports "70+ local couriers and pickup networks in 12+ markets" (Econt, Speedy, BoxNow among them) and "Enable[s] Cash on Delivery and custom fees by market or courier". It also offers "volume discounts and one-click physical or virtual add-ons". Rated 5.0 from 19 reviews; launched 3 Jun 2025; free up to 50 orders/month, paid plans $17.49–$69.99/month — [Shopify App Store: Sendica Pickup Points](https://apps.shopify.com/shipping-popup-app).
- The Smile Shopify checkout itself (opened directly at `/checkout`) shows:
  - "Имейл адрес или номер на мобилен телефон" (email OR phone)
  - an address field labelled "Адрес за доставка: офис на Спиди/Еконт/Личен адрес"
  - the payment list with "Наложен платеж (+0.99€)" first, captioned "Начинът на плащане с наложен платеж изисква допълнителна такса от €0,99 която се заплаща при доставка. Молим да бъдете отговорни към вашата поръчка :)", then "Кредитна карта"
  - "Спестявате общо 17,98 €"
  - Source: [Smile checkout](https://smilepatchesbg.com/checkout)

*VitaPatch*
- The PDP has bundle cards:
  - "1 ПАКЕТ 13,90 € 0,46 €/ден"
  - "ПЛАЩАШ 2, ПОЛУЧАВАШ 3 — 27,80 € ~~41,70 €~~ 0,31 €/ден"
  - "НАЙ-ИЗГОДНО ПЛАЩАШ 3, ПОЛУЧАВАШ 5 — 41,70 € ~~69,50 €~~ 0,28 €/ден, БЕЗПЛАТНА ДОСТАВКА"
- After the bundle cards come the "ДОБАВИ В КОЛИЧКАТА" button and trust lines "Доставка 1–2 дни · Безплатна доставка над 39,90 € · Плащане при доставка".
- Below that is a **separate inline call-back form**: "Бърза поръчка по телефон — Нямаш време за попълване? Остави име и телефон — ще ти се обадим, ще уточним адреса и ще потвърдим поръчката. Berberine 30 пача · 1 месец 13,90 € + доставка 2,99 € = 16,89 €". It has fields Име, Фамилия, Телефон and a consent checkbox, the button "Поръчай бързо", and the line "Плащане при доставка · Без предплащане · Ще потвърдим по телефона" — [VitaPatch PDP](https://vitapatch.bg/products/berberine).
- Add-to-cart (with the 3+2 tier active) opened the drawer, which shows:
  - "Кошница (5)"
  - "🎁 Активна оферта: ПЛАЩАШ 3, ПОЛУЧАВАШ 5 — Подаръци: Berberine, Berberine · Още 3 пача до следващите 2 безплатни пача"
  - "🚚 Получаваш безплатна доставка" with a green bar
  - toggle chips for the two offers
  - line items, including "Berberine — Безплатен подарък 2 бр. 0,00 €"
  - "Междинна сума 41,70 € · Спестяваш −27,80 € · Доставка Безплатна · Общо 41,70 €"
  - "Към поръчката →"
  - "Наложен платеж · Доставка 1–2 дни · 30 дни гаранция"
  - Source: [VitaPatch PDP](https://vitapatch.bg/products/berberine)
- The checkout (`/checkout`) is one page with these sections, in order:
  - "Твоите данни": Име и фамилия*, Телефон*, Имейл*, plus "Искам фактура"
  - "Доставка": "ИЗБЕРИ КУРИЕР" Еконт/Спиди, then "КАК ИСКАШ ДА ПОЛУЧИШ ПОРЪЧКАТА?" До офис/До адрес, then "Населено място* (Започни да пишеш град или село…)", then "Офис на Еконт* (Първо избери населено място)", then "Бележка"
  - "Плащане": only "Наложен платеж (при доставка) — Плащаш в брой на куриера, когато получиш поръчката. Без предплащане."
  - a dismissible order bump: "Само днес: добави NAD+ за −25% — 10,43 € ~~13,90 €~~ Добави към поръчката"
  - "Твоята поръчка" with Стойност на продуктите 69,50 € / Безплатни пачове −27,80 € / Доставка Безплатна / Крайна сума 41,70 €
  - two checkboxes (terms; data processing "Не ги споделяме с трети страни извън куриера")
  - the button "Завърши поръчката — 41,70 €"
  - "Плащане при доставка (наложен платеж). 30 дни гаранция за връщане."
  - Source: [VitaPatch checkout](https://vitapatch.bg/checkout)

*Tasty Dose*
- The PDP CTA reads "Добави в кошницата · 69,80€". The starter pack bundles a free bottle, spoon and sample pack ("FREE Premium bottle ~~19,90 €~~ … Metal spoon ~~14,90 €~~ … Sample pack ~~14,90 €~~") — [Tasty Dose PDP](https://tastydose.com/bg-bg/products/energy-2-0-starter-pack).
- Add-to-cart opens a modal "ОГРАНИЧЕНА ОФЕРТА ЗА ОПРЕДЕЛЕНО ВРЕМЕ 2:54". It reads "Back to school: вземете втората си чанта на най-ниската цена досега!", offers "СПЕСТИ 25% Coffee 2.0 29,90€ ~~39,90€~~" and "СПЕСТИ 58% Energy 2.0 16,90€ ~~39,90€~~" with flavour pickers and orange "Добави в количката" buttons, and warns "Тази оферта изчезва, когато затворите този прозорец. Пропуснете офертата" — [Tasty Dose PDP](https://tastydose.com/bg-bg/products/energy-2-0-starter-pack).
- The drawer (UpCart) shows:
  - "КОЛИЧКА 1"
  - "Остават само 45,20€ до безплатна доставка!" with a red progress bar (implied threshold about €115)
  - a line item "~~129,50€~~ 69,80€" with "Show 4 items"
  - "Междинна сума 69,80€"
  - "Продължи към плащане"
  - Source: [Tasty Dose PDP](https://tastydose.com/bg-bg/products/energy-2-0-starter-pack)
- The Shopify checkout opened under the **`en-ie` locale, in English**, for a BG-market cart. The cart attribute was "_mkt_guard: v6|BG". It shows:
  - Express checkout: Shop Pay, PayPal, Google Pay
  - Email, with a **pre-checked** "Email me with news and offers"
  - Street name, House number (required), Postal code, City, Phone, plus "Text me with news and offers"
  - Shipping: "Доставка до пикап пункт 3 to 5 business days €3.90 (Packeta / Zasilkovna pickup point — Select pickup point)" or "Стандартна доставка €4.50"
  - an optional "Shipping Protection €1.90" toggle
  - Payment: Credit card / PayPal / Revolut Pay
  - "✨ Exclusive offer for your order ✨" (Coffee 2.0, Energy 2.0, Refresh 2.0 at €24.90, struck €39.90)
  - trust blocks "90-Day Money-Back Guarantee", "Made in the EU", "Secure Payment"
  - Source: Tasty Dose checkout reached from [the BG cart](https://tastydose.com/bg-bg/cart)

*forlife.bg*
- The PDP CTA reads "ПОРЪЧАЙ" (sticky: "ПОРЪЧАЙ 21.00€"). It opens a side cart with:
  - "До безплатната доставка остават 39.00€" (free delivery at €60) with a bar
  - the line item
  - "Имате промо код?"
  - an upsell carousel "Още малко до безплатна доставка" (ALA €33, collagen €34, curcumin €33, hyaluronic acid €32, each with "+")
  - primary "ПОРЪЧАЙ (21.00€)" and secondary "ПРОДЪЛЖИ С ПАЗАРУВАНЕТО"
  - Source: [forlife PDP](https://www.forlife.bg/produkt/berberin)
- The checkout shows:
  - a 3-step progress bar "Вашата количка → Вашите данни → Приета поръчка"
  - Име*, Фамилия*, Страна*, Телефон*, Имейл адрес*
  - "Изберете куриер" logo tiles (Офис speedy / Офис ЕКОНТ / BOX NOW / ДО АДРЕС), then "Изберете град Спиди*" and "Изберете офис Спиди*" dropdowns, then Пощенски код*
  - "Регистрация на профил в сайта?" and order notes
  - order review: "ДОСТАВКА 3.00€, ОБЩО 24.00€ (включва 3.50€ ДДС)"
  - a gift-voucher box
  - payment: "Наложен платеж — Плащане в брой при доставка" (selected) plus "Payment options" (Stripe)
  - a terms checkbox, an "Искам да получавам информация…" opt-in (AutomateWoo), and "ПОРЪЧВАНЕ"
  - seals: Sectigo, B-Secure, Visa Secure, Mastercard ID Check, and "256-Bit Bank Level защита"
  - phone "+359 877 600 010" and office hours
  - Source: [forlife checkout](https://www.forlife.bg/checkout)

*Chillama*
- The PDP offer reads "Купи 1, получи 1 БЕЗПЛАТНО: SugarSentry €24.90 ~~€55.80~~", with "Купи 2, вземи 2 безплатно €45.90" (Най-продаван) and "Купи 3, вземи 3 безплатно €64.90" (Най-изгодно). It also shows "Безплатна доставка за поръчки над €41" and "Методи за плащане: НАЛОЖЕН ПЛАТЕЖ" — [Chillama PDP](https://chillama.co/bg/products/chillama-sugar-sentry).
- "Поръчай" goes straight to `/bg/order/`. That page shows:
  - "Поръчка — При нужда или въпроси: 0876 33 04 10"
  - the item with a quantity field and "Общо: ~~€55.80~~ €24.90"
  - "Междинна сума (преди отстъпките) €55.80 · Общо отстъпки −€30.90 · Доставка €2.60 · Имате промокод? · Общо €27.50"
  - delivery radios: "Pigeon до Ваш адрес / до офис на Speedy / До офис на Pigeon — Безплатна доставка над €41, 1-2 работни дни"
  - fields Имейл, Име и фамилия, Мобилен телефон, Град, Адрес за доставка, Коментари
  - payment "Наложен платеж — Плащане при доставка. Преглед преди плащане." (default), card, PayPal
  - "КУПИ"
  - Source: [Chillama order page](https://chillama.co/bg/order/)

*FitPatches (re-checked 2 Oct 2026)*
- The orange EasySell pop-up is titled "Предпочиташ по-лесна поръчка?". It has five required fields: "Две Имена", "Телефон", "Адрес на Еконт и Град", "Пощенски код", and "Регион" (a dropdown in Latin script: "Blagoevgrad … Sofia, Sofia City … Yambol"). The button is "Поръчай".
- It shows **no product, quantity, price, delivery fee or total** — [FitPatches PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
- The PDP also carries a separate name+phone form (`fp_name`, `fp_phone`). The 2 Oct own-site audit found that this form "captures nothing and silently redirects to Shopify checkout" — see `research_notes/FitPatches срещу големи брандове/own_site_audit.md`; [FitPatches PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30).
- Shopify bot protection returned HTTP 429 "Your connection needs to be verified" on `/cart/*.js`. As a result, FitPatches' own shipping rates and checkout could not be re-captured in this session — [fitpatches.net](https://fitpatches.net/).

### Inferences
- **Field count is not the main difference.** FitPatches' EasySell pop-up (5 fields) is about as short as the leaders' forms (5–7 fields). The difference is *what the shopper sees while typing*:
  - leaders show the product, savings, delivery fee and total
  - leaders replace free-text "Адрес на Еконт" with a carrier/office picker
  - leaders use one CTA path, not two competing buttons
- A free-text office plus postcode plus a Latin-script region dropdown is the most error-prone pattern observed. It produces the bad-address and unreachable-phone failures that BG logistics sources blame for undelivered COD parcels (see Q4).
- Smile Patches, a direct berberine-patch competitor, moved from a one-step COD form to "courier pop-up → Shopify checkout". That is two screens, but each is structured.
- InaEssentials uses the plain Shopify checkout, plus a COD fee and a card incentive.
- The big advertisers therefore do **not** depend on one-tap COD pop-ups. They depend on structured, transparent forms.

### Gaps
- Whether Sendica pre-fills the Shopify checkout after "ПРОДЪЛЖИ →" (and whether payment is chosen only on that second screen) was not verified. It would require typing data and clicking the continue button.
- InaEssentials' office picker (how a Speedy or Econt office is chosen inside the Shopify checkout) appears only after an address is typed, so it was not observed.
- Chillama's Speedy-office option showed no office dropdown before an address was typed. Whether one appears afterwards is unknown.
- The Tasty Dose checkout rendering in English (`en-ie`) for a BG cart may be an artefact of the headless session. It was not re-tested from a real Bulgarian IP.

---

## Q2. What do they show in the cart and checkout to reduce abandonment? (Trust, guarantee, delivery date, "преглед преди плащане", free-shipping bars, upsells, gifts, timers, reviews, phone/Viber support)

### Takeaway
The common toolkit is:
1. A **progress bar** to free delivery or a gift, with thresholds from €20 to €60, or milestones up to €120.
2. **Free gifts shown as €0.00 lines with the struck original price**, plus a running "Спестяваш/Отстъпка" amount.
3. A **compact trust strip** under the CTA: COD, 1–2 day delivery, the guarantee, and Econt/Speedy logos.
4. **One upsell moment**: a timed interstitial after add-to-cart (InaEssentials, Tasty Dose), a drawer cross-sell (Smile, forlife), or a checkout order bump (VitaPatch, InaEssentials, Tasty Dose).
5. A **visible phone number** or chat on the order step.

Countdown timers are used only for post-add-to-cart upsells, never on the main product price.

### Cited Findings

**Progress bars and thresholds**

| Brand | Bar text | Threshold |
|---|---|---|
| InaEssentials | "Още €8,02 до БЕЗПЛАТНА доставка!" | €40 delivery / €50 gift / €120 "ГОЛЯМ безплатен подарък" |
| Smile Patches | "Поздравления! Получавате 1 безплатен" | gift progress |
| VitaPatch | "Още 3 пача до следващите 2 безплатни пача", "Получаваш безплатна доставка" | free over €39.90 |
| Tasty Dose | "Остават само 45,20€ до безплатна доставка!" | about €115 |
| forlife | "До безплатната доставка остават 39.00€" | €60 |
| Valendy | "Още 0,10 € до безплатна доставка" | €20 ("Безплатна доставка от 20 €") |
| Chillama | header "Безплатна доставка за поръчки над €41" | €41 |

Sources: [Ina](https://inaessentials.com/products/florasync-active-intimna-pyana-layka), [Smile](https://smilepatchesbg.com/products/berberin-lepenki), [VitaPatch](https://vitapatch.bg/products/berberine), [Tasty Dose](https://tastydose.com/bg-bg/products/energy-2-0-starter-pack), [forlife](https://www.forlife.bg/produkt/berberin), [Valendy](https://www.valendy.com/cart), [Chillama](https://chillama.co/bg/order/).

**Gifts made visible in the cart**
- InaEssentials adds the gift products automatically, at €0.00 with "Спестяваш €9,99 / €11,49". It promotes a "Подарък-изненада 4,99 € → 0,00 € … само при плащане с карта" — [Ina drawer](https://inaessentials.com/products/florasync-active-intimna-pyana-layka).
- VitaPatch shows a "Безплатен подарък 2 бр. 0,00 €" line and "Безплатни пачове −27,80 €" in checkout — [VitaPatch checkout](https://vitapatch.bg/checkout).
- Tasty Dose lists the bundled "1 × Bottle, 1 × Spoon, 1 × Sample Pack" inside the checkout order summary — [Tasty Dose](https://tastydose.com/bg-bg/products/energy-2-0-starter-pack).

**Trust strips next to the CTA**
- VitaPatch drawer: "Наложен платеж · Доставка 1–2 дни · 30 дни гаранция". Checkout footer: "Плащане при доставка (наложен платеж). 30 дни гаранция за връщане." — [VitaPatch](https://vitapatch.bg/checkout)
- Smile drawer: payment logos plus "ДОСТАВКА С ЕКОНТ И СПИДИ · НАЛОЖЕН ПЛАТЕЖ". FAQ: "Пратките се изпращат с ЕКОНТ или СПИДИ и пристигат до 48 часа. Включена е опция за преглед преди плащане." — [Smile PDP](https://smilepatchesbg.com/products/berberin-lepenki)
- InaEssentials drawer: Apple Pay, Google Pay, Visa, Mastercard and "Cash on delivery" logos — [Ina](https://inaessentials.com/products/florasync-active-intimna-pyana-layka)
- forlife checkout: Sectigo, B-Secure, Visa Secure and Mastercard ID Check seals, plus "256-Bit Bank Level защита | 100% Сигурни плащания" — [forlife checkout](https://www.forlife.bg/checkout)
- Tasty Dose checkout: "90-Day Money-Back Guarantee … Made in the EU … Secure Payment" — [Tasty Dose](https://tastydose.com/bg-bg/cart)
- Chillama: the COD option is captioned "Плащане при доставка. Преглед преди плащане." — [Chillama order](https://chillama.co/bg/order/)

**Delivery promise and date**
- Smile PDP: "Поръчай сега за доставка преди 4. Октомври" (a dynamic date) — [Smile](https://smilepatchesbg.com/products/berberin-lepenki)
- VitaPatch header: "Доставка за 1–2 работни дни" — [VitaPatch](https://vitapatch.bg/checkout)
- Valendy header: "Доставка до 2 работни дни" — [Valendy](https://www.valendy.com/cart)
- Chillama: "1-2 работни дни" on each delivery option — [Chillama](https://chillama.co/bg/order/)
- Tasty Dose: "3 to 5 business days" — [Tasty Dose](https://tastydose.com/bg-bg/cart)

**Upsell moments**
- Timed post-add-to-cart interstitials:
  - InaEssentials: 5-minute countdown, "Пазарувай с голяма отстъпка сега"
  - Tasty Dose: about 3 minutes, "Тази оферта изчезва, когато затворите този прозорец"
  - Sources: [Ina](https://inaessentials.com/products/florasync-active-intimna-pyana-layka); [Tasty Dose](https://tastydose.com/bg-bg/products/energy-2-0-starter-pack)
- Drawer cross-sells:
  - Smile: "За пълна грижа за вашето тяло може да комбинирате с:"
  - forlife: "Още малко до безплатна доставка", products tied to the free-shipping gap
  - InaEssentials cart page: "Може да харесате също:"
  - Sources: [Smile](https://smilepatchesbg.com/products/berberin-lepenki); [forlife](https://www.forlife.bg/produkt/berberin); [Ina cart](https://inaessentials.com/cart)
- Checkout order bumps:
  - VitaPatch: "Само днес: добави NAD+ за −25%"
  - InaEssentials: "Хората купуват често:" with "+ Добави"
  - Tasty Dose: "✨ Exclusive offer for your order ✨"
  - Sources: [VitaPatch](https://vitapatch.bg/checkout); [Ina](https://inaessentials.com/cart); [Tasty Dose](https://tastydose.com/bg-bg/cart)

**Reviews**
- Smile: "4.78/5 на базата на 10,250 мнения" — [Smile PDP](https://smilepatchesbg.com/products/berberin-lepenki)
- VitaPatch: "★★★★★ 4.8 (156)" — [VitaPatch PDP](https://vitapatch.bg/products/berberine)
- InaEssentials product cards: for example "4.91 / 5.0 (2600)" — [Ina home](https://inaessentials.com/)
- Tasty Dose: Trustpilot "Excellent" — [Tasty Dose PDP](https://tastydose.com/bg-bg/products/energy-2-0-starter-pack)
- None of the observed carts or checkouts repeat star ratings inside the drawer or form itself.

**Human contact at the order step**
- Chillama: "При нужда или въпроси: 0876 33 04 10" at the top of the order page — [Chillama](https://chillama.co/bg/order/)
- forlife: phone and hours under the checkout — [forlife](https://www.forlife.bg/checkout)
- VitaPatch: footer contact "0879 502 555" and the call-back form — [VitaPatch](https://vitapatch.bg/checkout)
- InaEssentials: an AI chat bubble (Zipchat) on PDP and drawer, plus a spin-to-win widget (discount wheel) — [Ina](https://inaessentials.com/products/florasync-active-intimna-pyana-layka)

### Inferences
- **Free delivery thresholds sit at or below the "best value" bundle price:**

  | Brand | Free-delivery threshold | Best-value bundle price |
  |---|---|---|
  | InaEssentials | €40 | 2-pack €31.98, plus gifts that push it toward the threshold |
  | VitaPatch | €39.90 | 3+2 €41.70 |
  | Chillama | €41 | 2+2 €45.90 |
  | Smile Patches | free on 3+2 | 3+2 |
  | Valendy | €20 | single unit €19.90 |

  FitPatches' €60 threshold is above all its bundles, so its bar can never complete. This is consistent with the 2 Oct own-site audit.
- **Gifts are framed as money saved** (€0.00 plus the struck value) in the cart and checkout, not only on the product page. This keeps the perceived value visible at the moment of commitment.
- Timers are kept to the optional upsell layer, which limits the credibility cost on the core offer.

### Gaps
- Whether any brand shows the review stars or a guarantee badge *inside* the COD/checkout form was checked visually: none did, except Tasty Dose's guarantee block.
- Viber or WhatsApp click-to-chat buttons were not seen in any cart or checkout. VitaPatch mentions Viber only in its policy (see Q4).

---

## Q3. Shopify checkout customisations: express checkout, payment methods (COD, card, BNPL), language/branding, address autocomplete, required fields

### Takeaway
The Shopify brands keep Shopify's one-page checkout but customise it in four ways:
1. Bulgarian translations and custom field labels.
2. A **COD fee of €0.99** (InaEssentials, Smile Patches).
3. **Incentives to prepay**: InaEssentials pre-selects card and gives a €4.99 gift for card payment; BOX NOW lockers are card-only at both InaEssentials and Smile.
4. Pre-checked marketing and SMS consents, plus checkout upsell blocks.

Express wallets observed: Shop Pay, Google Pay, PayPal. No brand offered BNPL or instalments (TBI, iCredit, Klarna) in checkout.

### Cited Findings

**Express checkout**
- InaEssentials: Google Pay. Apple Pay is advertised in the drawer logos; it was not visible in Chromium — [Ina checkout](https://inaessentials.com/cart).
- Tasty Dose: Shop Pay, PayPal, Google Pay — [Tasty Dose checkout](https://tastydose.com/bg-bg/cart).
- Valendy: Shop Pay, Google Pay — [Valendy checkout](https://www.valendy.com/cart).
- The Smile checkout shows an "Експресно плащане" block — [Smile checkout](https://smilepatchesbg.com/checkout).
- The Tasty Dose and Valendy checkout URLs carry `skip_shop_pay=true` — [Valendy](https://www.valendy.com/cart).

**Payment methods and order**

| Brand | Payment options shown, in order |
|---|---|
| InaEssentials | Card (pre-selected), Revolut, COD "(+ 0.99€)" |
| Smile Patches | COD "(+0.99€)" first, then card |
| Valendy | Card, "Наложен платеж (COD)" |
| Tasty Dose | Card, PayPal, Revolut Pay (**no COD**) |
| forlife (WooCommerce) | COD (pre-selected), Stripe card |
| Chillama (custom) | COD (pre-selected), card (Mollie), PayPal |
| VitaPatch (custom) | COD only |

Sources: [Ina](https://inaessentials.com/cart), [Smile](https://smilepatchesbg.com/checkout), [Valendy](https://www.valendy.com/cart), [Tasty Dose](https://tastydose.com/bg-bg/cart), [forlife](https://www.forlife.bg/checkout), [Chillama](https://chillama.co/bg/order/), [VitaPatch](https://vitapatch.bg/checkout).

- No instalment or BNPL options (TBI Bank, iCredit, Klarna, NewPay) appeared in any of the seven checkouts.

**Language and branding**
- InaEssentials, Smile and Valendy checkouts are fully in Bulgarian (`/bg-bg` locale) with the brand logo. InaEssentials uses a red logo tile and green accents.
- Tasty Dose's BG cart opened an English (`en-ie`) checkout with Bulgarian shipping-method names.
- Sources: [Ina](https://inaessentials.com/cart); [Tasty Dose](https://tastydose.com/bg-bg/cart).

**Custom labels, consents and blocks**
- Smile relabels address line 1 as "Адрес за доставка: офис на Спиди/Еконт/Личен адрес" — [Smile](https://smilepatchesbg.com/checkout).
- InaEssentials pre-checks the marketing consent ("ВАЖНО: Искам да получа имейл с потвърждение на поръчката си, имейли с промоции…") and the SMS-on-delivery opt-in. It adds a card-gift banner and an upsell block — [Ina](https://inaessentials.com/cart).
- Tasty Dose pre-checks "Email me with news and offers" and adds a Shipping Protection €1.90 toggle — [Tasty Dose](https://tastydose.com/bg-bg/cart).

**Required fields**
- InaEssentials: Email, Собствено име, Фамилно име, Адрес, Пощенски код, Град, Телефон (address line 2 optional) — [Ina](https://inaessentials.com/cart).
- Valendy and Smile accept "Имейл адрес или номер на мобилен телефон" in the contact field, so a phone number can replace email — [Valendy](https://www.valendy.com/cart); [Smile](https://smilepatchesbg.com/checkout).
- Tasty Dose requires a separate "House number" field — [Tasty Dose](https://tastydose.com/bg-bg/cart).

**Address autocomplete**
- Shopify's hidden autofill inputs (`autofill_address1`, `autofill_postalCode` and so on) were present in every Shopify checkout.
- A Google-style dropdown was not observed, because no address was typed.
- The non-Shopify sites use their own lookups:
  - VitaPatch: "Започни да пишеш град или село…" then office
  - forlife: city dropdown, then office dropdown
- Sources: [VitaPatch](https://vitapatch.bg/checkout); [forlife](https://www.forlife.bg/checkout).

**Card-only carrier options**
- InaEssentials: "До автомат на Box Now (само с картово плащане) €1.90" — [Ina rates](https://inaessentials.com/policies/shipping-policy).
- Smile: "BoxNow (само с карта) Безплатно" — [Smile](https://smilepatchesbg.com/products/berberin-lepenki).

### Inferences
- The two most COD-heavy Shopify brands do not hide COD, but they **price it** (€0.99) and **reward prepaying** (a gift, or a free or cheaper locker). This moves part of the order mix to prepaid, which removes refusal risk on those orders.
- FitPatches' EasySell pop-up is COD-only and never shows a card option or a reason to prepay.
- Using "email OR phone" in the Shopify contact field (Smile, Valendy) removes the most-skipped field for COD shoppers. FitPatches could use the same Shopify checkout setting if it keeps a Shopify-checkout path.

### Gaps
- Apple Pay visibility could not be tested; the emulation used Chromium, not Safari.
- Shopify Checkout Blocks or Plus status could not be confirmed. The InaEssentials gift banner and upsell are consistent with checkout UI extensions, but the specific app was not identified.

---

## Q4. After the order: thank-you-page upsells, SMS/Viber confirmation, confirmation calls

### Takeaway
No orders were placed, so the post-purchase steps were not observed directly. The evidence is indirect:
- InaEssentials runs its own **custom post-purchase app** and SMS list tooling (Recart), and offers a free "SMS when the parcel arrives".
- VitaPatch states that staff may confirm orders by **phone, SMS or Viber** and send the waybill by email, SMS or Viber. Its quick-order path is explicitly "ще ти се обадим… ще потвърдим поръчката".
- Bulgarian logistics sources recommend confirmation calls and SMS/Viber pre-delivery notices to cut undelivered COD parcels.

### Cited Findings
- InaEssentials has a custom embedded Shopify app titled "INA Post Purchase" (its admin dashboard is at ina-post-purchase.vercel.app). The storefront loads Recart's "recart-sms-list-growth" block, Klaviyo and Brevo — [ina-post-purchase.vercel.app](https://ina-post-purchase.vercel.app/); [Ina PDP HTML](https://inaessentials.com/products/florasync-active-intimna-pyana-layka).
- InaEssentials' checkout has the pre-checked option "Искам да получа БЕЗПЛАТЕН СМС при получаване на пратката си" — [Ina checkout](https://inaessentials.com/cart).
- VitaPatch policy:
  - "получаваш автоматично потвърждение по имейл. За допълнителна сигурност и уточняване на детайли наш служител може да се свърже с теб по телефон, SMS или Viber, за да потвърди поръчката, адреса за доставка и избрания начин на плащане"
  - "Номерът на товарителницата се предоставя по имейл, SMS или Viber"
  - "Отказана без основание пратка при наложен платеж — разходите по връщането могат да бъдат за сметка на клиента при последваща поръчка"
  - Source: [VitaPatch Доставка и плащане](https://vitapatch.bg/dostavka-i-plashtane)
- VitaPatch quick order: "Остави име и телефон — ще ти се обадим, ще уточним адреса и ще потвърдим поръчката … Ще потвърдим по телефона" — [VitaPatch PDP](https://vitapatch.bg/products/berberine).
- Tasty Dose loads Rebuy and an "upsell-event-receiver" endpoint, and has a checkout upsell. A post-purchase page could not be verified — [Tasty Dose PDP](https://tastydose.com/bg-bg/products/energy-2-0-starter-pack).
- forlife has an AutomateWoo marketing opt-in at checkout (follow-up emails) — [forlife checkout](https://www.forlife.bg/checkout).

**Regional context**
- In Bulgaria and Romania "over 60% of orders are paid at the door", and "5–15% of orders in the region go undelivered". About 20% of failed orders stem from data inaccuracies or poor communication. Recommended fixes: "don't be afraid to make a quick confirmation call" for first-time or high-value COD orders, SMS/Viber notifications before delivery, parcel-shop or locker selection at checkout to avoid address errors, and 5–10% prepayment incentives (article dated Oct 2025) — [iHub.bg](https://ihub.bg/en/articles/how-reduce-undelivered-parcels-e-commerce).
- 92.9% of Bulgarian online stores offer COD (vs 32% in Romania and 20–30% in Greece, Croatia and Hungary), and over 77% accept cards. Source: Balkan Ecommerce Summit, "State of E-commerce in the Balkans 2025", published 26 Feb 2026 — [Digipay.bg](https://digipay.bg/bg/blog/e-commerce-92-9-of-online-stores-in-bulgaria-offer-cash-on-delivery).
- A COD fulfilment provider reports a "4–7 percentage-point improvement on supplements campaigns when confirmation is enabled" for pre-dispatch confirmation calls. This is self-reported vendor data — [BigArena](https://bigarena.net/en/blog/cash-on-delivery-europe-guide) (as cited in the earlier CRO notes in this repo).

**FitPatches**
- The EasySell config observed on 2 Oct (own-site audit) has `disable_abandoned: true`, `otp_first: false`, `include_upsell: false`, and an English thank-you template ("Thank You, {{customer.first_name}}! 🎉 Your order {{order.number}} is confirmed…") — [fitpatches.net](https://fitpatches.net/); see `research_notes/FitPatches срещу големи брандове/own_site_audit.md`.
- EasySell itself supports quantity offers, downsells, post-purchase and one-tick upsells, OTP phone verification, and IP/postcode blocking — [EasySell (Shopify App Store)](https://apps.shopify.com/easy-order-form); [easysellapp.com](https://easysellapp.com/).

### Inferences
- The leaders treat the order as **unconfirmed until a human or automated touch** (call, SMS or Viber), and they collect email or SMS consent to run recovery and review flows.
- FitPatches' pop-up collects no email, has abandoned-order capture disabled, and uses an English thank-you template. This loses both the recovery channel and the reassurance moment.
- These EasySell features are already paid for and could be switched on.

### Gaps
- Actual thank-you pages, post-purchase one-click offers, confirmation SMS/Viber content and call scripts were not observed for any brand; a real order would be required.
- No brand publishes its confirmation-call rate, refusal rate or delivered-order rate.

---

## Q5. Pattern summary: what the leaders do differently from FitPatches between add-to-cart and purchase

### Takeaway
The leaders differ from FitPatches in six ways, and none of them depends on a shorter form:
1. **One** clear path after add-to-cart.
2. An order form that **shows what you are buying, what you save, the delivery fee and the total**.
3. A **picker** for courier and office (or locker), not free text.
4. Free delivery reachable by the default bundle.
5. Exactly one well-placed upsell moment.
6. A light push toward prepaying, plus post-order confirmation and contact capture.

FitPatches' 244 EasySell orders out of 324 show that COD shoppers want a light form. The gap is transparency and structure in that form.

### Cited Findings
- **Single primary CTA:**
  - InaEssentials drawer: one green "Преминаване към плащане" — [Ina](https://inaessentials.com/products/florasync-active-intimna-pyana-layka)
  - Smile: one blue "Преминаване към плащане" — [Smile](https://smilepatchesbg.com/products/berberin-lepenki)
  - VitaPatch: one "Към поръчката →" — [VitaPatch](https://vitapatch.bg/products/berberine)
  - forlife: one primary "ПОРЪЧАЙ (21.00€)", with "ПРОДЪЛЖИ С ПАЗАРУВАНЕТО" as a secondary — [forlife](https://www.forlife.bg/produkt/berberin)
  - Tasty Dose: one "Продължи към плащане" — [Tasty Dose](https://tastydose.com/bg-bg/products/energy-2-0-starter-pack)
  - FitPatches: two stacked full-width buttons, orange "Поръчай" (EasySell) and pink "Преминаване към плащане" — [FitPatches](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30)
- **Order summary in the form:**
  - Smile's Sendica pop-up opens with "Информация за поръчката EUR 26.99" and lists discount, delivery and total — [Smile](https://smilepatchesbg.com/products/berberin-lepenki)
  - VitaPatch's button reads "Завърши поръчката — 41,70 €" — [VitaPatch](https://vitapatch.bg/checkout)
  - Chillama shows "Общо €27.50" above the fields — [Chillama](https://chillama.co/bg/order/)
  - The FitPatches pop-up shows none — [FitPatches](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30)
- **Structured office selection:** Smile (search box "Напиши град, офис или адрес"), VitaPatch (city autocomplete, then office), forlife (tiles plus dropdowns), Chillama (radios). FitPatches uses free text "Адрес на Еконт и Град" — sources as in Q1.
- **Default bundle pre-selected:** InaEssentials 2 + 2 gifts; Smile 2+1; VitaPatch 3+2 (the cart opened as 3 paid + 2 free) — [Ina](https://inaessentials.com/products/florasync-active-intimna-pyana-layka); [Smile](https://smilepatchesbg.com/products/berberin-lepenki); [VitaPatch](https://vitapatch.bg/products/berberine).
- **Delivery fees are low and itemised** (€1.90–€4.00):

  | Brand | Delivery fee | Free over |
  |---|---|---|
  | InaEssentials | €1.90–€4.00 | €40 |
  | Smile Patches | €2.50 / €3.40 | free with BoxNow |
  | Chillama | €2.60 | €41 |
  | forlife | €3.00 | €60 |
  | Valendy | €2.99–€3.99 | — |

  Sources as in Q1.
- **Prepay incentives:** InaEssentials (card default, €4.99 gift for card, COD +€0.99); Smile (COD +€0.99; BoxNow free but card-only) — [Ina](https://inaessentials.com/cart); [Smile](https://smilepatchesbg.com/checkout).

### Inferences

**Concrete differences, ranked by expected impact on FitPatches' add-to-cart-to-order gap (608 add-to-cart sessions → 324 orders):**

1. **Collapse to one path.** Make the COD order form *the* checkout button; one button, labelled with the total. Options:
   - EasySell with the order summary and shipping options turned on
   - a Sendica-style pre-checkout pop-up into Shopify checkout

   Either way, drop the competing pink button, or demote it to a text link such as "Плащане с карта". The leaders never present two equal primary buttons.
2. **Show the order inside the form.** Include product, bundle, gift lines at €0.00, "Спестяваш", delivery fee by carrier, and "Общо". Put the total on the button ("Поръчай — 27,99 €").
3. **Replace free-text "Адрес на Еконт и Град" + postcode + Latin "Регион"** with an Econt/Speedy/Box Now office picker (city autocomplete, then office), plus a "До адрес" option. This cuts typing and the address errors linked to undelivered COD parcels (iHub's ~20% of failed orders).
4. **Pre-select the middle bundle** and make free delivery reachable by it. Market practice is a threshold of €39.90–€41, or free shipping attached to the bundle, versus FitPatches' €60.
5. **Add one upsell moment, not several.** Either a dismissible order bump inside the COD form ("Само днес: добави … −25%", VitaPatch-style) or a timed post-add-to-cart interstitial (InaEssentials, Tasty Dose).
6. **Steer some buyers to prepay.** Use a small COD fee or a card-only perk (a gift, or a free Box Now locker) as InaEssentials and Smile do. Keep COD prominent; 92.9% of BG stores offer it and over 60% of orders are paid at the door.
7. **Close the loop after the order:**
   - collect an email (optional) or SMS/Viber consent
   - switch on EasySell abandoned-order capture and OTP or phone confirmation
   - localise the thank-you page
   - run confirmation calls or SMS for first-time COD orders (VitaPatch's stated practice; iHub and BigArena guidance)

**Caveat on alternatives.** Two leaders, VitaPatch and Chillama, use fully custom one-page checkouts. Two others, InaEssentials and Valendy, use the native Shopify checkout. The winning pattern is therefore not tied to an app; it is the presence of transparency, structure, a single CTA and an anchored bundle.

### Gaps
- There is no independent A/B evidence in Bulgaria comparing COD pop-up forms with Shopify checkout, or office pickers with free text. The ranking above is inferred from observed practice and from logistics-vendor guidance, not from measured lifts.
- Competitor add-to-cart-to-order rates are not public, so FitPatches' roughly 53% (orders per add-to-cart session) cannot be benchmarked directly.
