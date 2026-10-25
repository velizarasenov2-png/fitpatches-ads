# Halloween visual refresh for a Shopify store: playbook + fitpatches.net visual audit (as of 25 Oct 2026)

Scope: visual changes only (no new offers or prices). They have to work on Shopify Basic and go live before 31 Oct 2026. The audit was read-only. No theme or store setting was changed.
Screenshots (taken 25 Oct 2026 ~08:28–08:30 UTC, all four pages returned HTTP 200 on the first request, no 429):
- `/home/user/fitpatches-ads/research_notes/Halloween визия за сайта/shots/fitpatches_home_desktop.png` (1280 wide, full page 6109 px)
- `/home/user/fitpatches-ads/research_notes/Halloween визия за сайта/shots/fitpatches_home_mobile.png` (390 wide @2x, full page 7701 CSS px)
- `/home/user/fitpatches-ads/research_notes/Halloween визия за сайта/shots/fitpatches_product_desktop.png` (1280 wide, full page 12396 px)
- `/home/user/fitpatches-ads/research_notes/Halloween визия за сайта/shots/fitpatches_product_mobile.png` (390 wide @2x, full page 14816 CSS px)
Raw extraction data (computed colours, fonts, section list, HTML) is in `/tmp/claude-0/-home-user-fitpatches-ads/7bae3ff3-1b65-59a1-af86-fbf004e30a8b/scratchpad/audit_data/`. Scripts: `audit.js`, `perf.js`, `rm.js` in the same scratchpad folder.

Labelling: "Cited Findings" are sourced facts or direct observations of the live site. "Inferences" are my own reasoning. Vendor or agency claims that give no method are marked as such.

---

## Q1. Which visual elements do stores change for Halloween, and which give the most impact for the least risk?

### Takeaway
The cheapest high-visibility changes are a recoloured strip or announcement band, a themed hero image swap at the same dimensions, a favicon or logo variant, themed section dividers and background textures, and icon/emoji accents. They cost almost nothing in performance. Falling or floating JS effects, custom cursors, autoplay video or audio, countdowns with no real deadline, and anything inside the buy box or order form carry the most risk for the least proven upside. I found no published A/B data that isolates purely visual Halloween theming.

### Cited Findings
- A Shopify-agency article (Glued) uses a load-time budget: "Under 0.2 seconds added LCP" is safe on desktop and mobile. 0.2–0.5 s means desktop only or a lighter mobile version. "Over 0.5 seconds added LCP" means skip it. It names snowfall animations, autoplay video backgrounds and unoptimised festive background images as typically over the threshold. **This is vendor opinion, not measured data.** — [Glued: Shopify Holiday Themes](https://getglued.co/insights/shopify-holiday-themes)
- The same article claims "JavaScript-based effects add 0.3–1.0 seconds of load time" and JS countdown timers "add ~0.1–0.2 seconds of LCP impact". It also says announcement-bar updates are "near-zero" performance cost. It recommends hero images under 150 KB on mobile and under 300 KB on desktop. **Unsourced vendor figures.** — [Glued](https://getglued.co/insights/shopify-holiday-themes)
- Glued also says that "performance degradation from decorative elements increases bounce rate by 44%". This is attributed to its own manifesto with no methodology, so treat it as unverified. — [Glued](https://getglued.co/insights/shopify-holiday-themes)
- Many Shopify apps exist only to add Halloween falling or flying effects: "Spooky Halloween" (pumpkins and bats falling "through the screen" on the main pages), Dakaas Seasonal Effects (flying bats, fog), FX Halloween Effects (page targeting and date scheduling), MIT Festival Effects ($0 free plan / $1.49 per month premium), and Festival Effect by MageCurious ($1.20 per month, including **background music**). — [Shopify App Store: Spooky Halloween](https://apps.shopify.com/halloween?rating=3); [Shopify App Store: AWE Holiday Effects](https://apps.shopify.com/awe-seasonal-effects); [Shopify App Store: Festival Effect](https://apps.shopify.com/festival-effect); [Meetanshi roundup](https://meetanshi.com/blog/best-shopify-apps-to-add-halloween-effects/); [Zoko roundup](https://www.zoko.io/post/top-10-best-shopify-apps-for-seasonal-design)
- Favicon swap in Shopify: Online Store > Edit theme > Theme settings > Logo (or Favicon) > Favicon image. 16×16 or 32×32 px is ideal, and larger uploads are reduced to 32×32. Favicons don't show inside the theme editor preview. — [Shopify Help: Add a favicon](https://help.shopify.com/en/manual/online-store/images/add-favicon)
- NN/g: "Movement in a person's peripheral vision triggers a stimulus-driven shift in visual attention." "Animations that are repeatedly encountered are roadblocks to content". By the third view an animation is "downright annoying". "Gratuitous, purposeless animations discourage the user from interacting further with the website." — [NN/g: Animation for Attention and Comprehension](https://www.nngroup.com/articles/animation-usability/)

### Inferences
Impact/risk matrix for this store. This is my ranking, built from the sources above and the audit in Q5.

| Element | Visibility impact | Perf / UX risk | Verdict |
|---|---|---|---|
| Recolour the existing scrolling marquee strip (dark band, 🦇/🎃 separators instead of ✦) | High (sits right under the hero) | ~0 (text + CSS) | **Do** |
| Hero image swap: same pack shot with Halloween props (mini pink pumpkins, black candles, autumn leaves), same aspect ratio and weight (≤ ~150 KB) | High | Low if size and dimensions are unchanged (the image is the LCP element, see Q5) | **Do** |
| Favicon swap (pink pumpkin or bat version of the FP monogram) | Low–medium (tab and bookmarks) | ~0 | **Do** (2-minute job) |
| Logo variant (tiny bat or witch hat on the "FP" monogram) | Medium | Low (same file size and dimensions) | Optional |
| Small "Хелоуин издание 🎃" pill or badge in the hero and on one later PDP image | Medium | Low | **Do**, but not on the main gallery image and never in the buy box |
| Section dividers (spider-web corners, "drip" SVG edge) at fixed height | Medium | Low (inline SVG/CSS, fixed height = no CLS) | **Do** on 2–3 seams only |
| Subtle background texture (bats or web pattern at 5–8% opacity) on one or two decorative sections | Medium | Low; can reduce text contrast if placed behind copy | Optional, only behind headings or in empty margins |
| Icons/emoji in eyebrows ("— КАК РАБОТИ —" → "🦇 КАК РАБОТИ") | Low–medium | ~0 | Optional |
| New announcement bar above the header | Medium | Low–medium (banner blindness, CLS if JS-injected) | Optional; must be server-rendered |
| Falling or floating bats/ghosts (app or JS) | High novelty, distracting | Medium–high: CPU on mobile, peripheral-motion distraction, WCAG 2.2.2 pause requirement, app code left behind after uninstall | **Skip**, or at most a ≤5 s one-shot CSS-only effect, gated by `prefers-reduced-motion`, pointer-events:none, homepage only |
| Custom cursor | Desktop only, tiny audience | Hides standard affordances; no effect on mobile/touch | **Skip** |
| Countdown to 31 Oct | Implies urgency with no offer behind it | Fake-urgency feel, JS cost | **Skip** (no offer is allowed in scope) |
| Themed cart drawer / empty-cart message | Very low (the store's order path is a COD form, not the cart) | Low | Skip |
| Themed 404 | Very low traffic | ~0 | Nice-to-have only |
| Loading/scroll-reveal animations | Low | Medium (INP/LCP, distraction) | Skip |
| Spooky sound or music (the theme has a global music-player section) | Negative | WCAG 1.4.2; startles users | **Never** |
| Product photography props (pumpkins, candles, leaves) | High; fits the existing prop style (pomegranate, herbs on pink) | ~0 if exported at the same size | **Do** (hero + 1 extra PDP image + the "Природата в помощ" centre image) |

- Short themed microcopy, purely decorative: "Хелоуин издание", "🎃 Честит Хелоуин от FitPatches", and "🦇" or "🎃" separators in the marquee. Don't rewrite claims, headlines or CTAs.

### Gaps
- I found no controlled study that measures the conversion effect of purely visual seasonal theming with no offer change. All the A/B data I found mixes in offers or messages (see Q2).
- I found no independent measurement of what the named Halloween apps cost in performance. The only numbers are Glued's unsourced ranges.
- Klaviyo and Omnisend publish holiday email and SMS statistics, but I found no Halloween-specific on-site visual guidance or data from either.

---

## Q2. Evidence on what helps or hurts conversion: seasonal theming, performance, contrast, reduced motion, banner blindness, trust signals, A/B data

### Takeaway
The evidence base for theming lifting conversion is thin and mostly about offers. The evidence for the guardrails is strong and comes from primary sources: keep LCP, CLS and INP within Core Web Vitals, animate only with transform and opacity, honour `prefers-reduced-motion`, give a pause control for any motion over 5 s, meet WCAG contrast (4.5:1 text, 3:1 large text or UI), and don't make content look like an ad. Leave trust signals and the buy box visually as they are.

### Cited Findings
**A/B and seasonal data (weak or offer-confounded):**
- MeUndies: a "large, colorful banner promoting active offers" on PDPs gave +9.8% transactions, +10% add-to-cart clicks and over $400,000 added revenue. **This is an offer/message banner, not purely visual theming.** No duration is stated. Page last updated 7 Oct 2022. — [ROI Revolution: 8 holiday A/B tests](https://roirevolution.com/blog/8-holiday-a-b-tests-to-boost-your-ecommerce-growth-this-holiday-shopping-season/)
- Kusmi Tea: a prize wheel launched with the Christmas shop got 42% engagement. Among participants, conversion was +2% and bounce −8%. **Gamified offer, not visual.** — [ROI Revolution](https://roirevolution.com/blog/8-holiday-a-b-tests-to-boost-your-ecommerce-growth-this-holiday-shopping-season/)
- A search snippet credits Invesp with "+26% revenue" from a holiday homepage variation. I couldn't see what changed or how long the test ran, so **treat it as unverified**. — [Invesp blog](https://www.invespcro.com/blog/?p=97688)
- A VWO case (MedaliaArt) compared a large red "Holiday Sale" banner with a small sidebar message. VWO's founder advised adding a no-message control and measuring sales rather than bounce. — [Practical Ecommerce](https://www.practicalecommerce.com/Split-Testing-Can-Increase-Conversion-Rates); [VWO blog](https://vwo.com/blog/using-ab-split-testing-reduce-bounce-rate-ecommerce-store/)
- Glued says Lull "doubled BFCM conversion without snowfall animations". Glued attributes this to narrative and checkout work, not aesthetics, citing "Shopify analytics, 2024", which can't be verified. — [Glued](https://getglued.co/insights/shopify-holiday-themes)

**Performance (primary sources):**
- CLS: "Good CLS values are 0.1 or less. Poor values are greater than 0.25." Banners and forms that appear without reserved space shift the page, and content injected near the top of the viewport causes bigger shifts. "Composited animations using `translate` can't impact other elements, and so don't count toward CLS." Changing `top`/`left` causes layout shifts. Web fonts can cause shifts. Recommended fixes: reserve space (`min-height`/`aspect-ratio`) or overlay the element instead of inserting it. — [web.dev: Optimize CLS](https://web.dev/articles/optimize-cls)
- Core Web Vitals "good" thresholds are LCP ≤ 2.5 s, INP ≤ 200 ms and CLS ≤ 0.1, measured at the 75th percentile of page loads. — [web.dev: Web Vitals](https://web.dev/articles/vitals)
- Animate only cheap properties: "restrict animations to `opacity` and `transform`" and "Avoid any property that triggers layout or paint unless it's absolutely necessary". Use `will-change` sparingly. — [web.dev: Animations guide](https://web.dev/articles/animations-guide)
- Shopify's own guidance: "Too many apps loading assets on your storefront can slow performance." "Uninstalling an app doesn't automatically remove its code from your theme." "Animations can slow down pages." Slow INP is "most likely" too much JavaScript from theme, app or third-party code. "High numbers of sections on pages can lower web performance." — [Shopify Help: Improving store speed](https://help.shopify.com/en/manual/online-store/store-speed/improving-speed)

**Accessibility (primary sources):**
- WCAG 2.2 SC 2.2.2 Pause, Stop, Hide (Level A) applies to moving, blinking or scrolling content that "(1) starts automatically, (2) lasts more than five seconds, and (3) is presented in parallel with other content". Such content needs "a mechanism for the user to pause, stop, or hide it", unless the motion is essential. Animations that stop within 5 s comply without a control. — [W3C Understanding 2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)
- `prefers-reduced-motion` exists because "some users outright experience motion sickness when faced with parallax scrolling, zooming effects, and more". Vestibular reactions "include dizziness, nausea, and migraine headaches". The recommended pattern is to put motion inside `@media (prefers-reduced-motion: no-preference)`. Supported since Chrome 74 / Firefox 63 / Safari 10.1. — [web.dev: prefers-reduced-motion](https://web.dev/articles/prefers-reduced-motion)
- WCAG 2.2 SC 1.4.3 (AA) requires 4.5:1 for normal text and 3:1 for large text. Large text is 18 pt, or 14 pt bold, which is about 24 px, or about 18.5 px bold. Pure decoration and logotypes are exempt. — [W3C Understanding 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- WCAG 2.2 SC 1.4.11 Non-text Contrast (AA) requires 3:1 for UI components and meaningful graphics. — [W3C Understanding 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)
- WCAG 2.2 SC 1.4.2 Audio Control (A): audio that plays automatically for more than 3 s needs a pause/stop or volume mechanism. — [W3C Understanding 1.4.2](https://www.w3.org/WAI/WCAG22/Understanding/audio-control.html)

**Banner blindness and attention:**
- Banner blindness is learned behaviour, documented since 1997 and reconfirmed. Users skip content in ad-typical places, such as the top of the page and the right rail, and content styled like ads. Ad-like traits include "animation", "fancy formatting", "a colored background", and "text embedded in an image". On mobile, users mistook non-ad content that stood out for ads. Recommendation: "Avoid styling content like ads." — [NN/g: Banner Blindness Revisited](https://www.nngroup.com/articles/banner-blindness-old-and-new-findings/)

**Trust signals:**
- Baymard: users' sense of a site's security is "largely determined by their 'gut feeling'", which visual design strongly shapes. Users rate some parts of the same checkout page as more secure than others (seen in 2009, 2012 and later testing). Visually reinforcing sensitive fields and showing recognisable seals raise perceived security. — [Baymard: Perceived security of payment form](https://baymard.com/blog/perceived-security-of-payment-form)

### Inferences
- Applied to fitpatches.net: the order area (bundle picker, "Поръчай сега", the "Бърза поръчка" COD form with name and phone, the delivery-date timeline, "Плащане при доставка" pills, the guarantee box, review stars) is where users form that "gut feeling" of safety. Halloween decoration there could make it read as "promo" or "ad" (banner blindness) or "less serious" (perceived security). Keep it pixel-identical.
- Any themed strip or banner should look like part of the site: the same Poppins type, brand pink, and a band style the site already uses (the marquee). That avoids looking like a third-party ad. A JS-injected app bar with a different style is the worst case on both NN/g criteria and web.dev CLS.
- The safe motion budget: at most one ambient animation, the marquee that already exists. Any new effect should be CSS-only, transform/opacity, end within 5 s, use `pointer-events:none`, and be wrapped in `prefers-reduced-motion: no-preference`.
- Contrast: orange text on white fails AA (computed 2.69:1 for #ff7518, see Q3). Halloween orange should only be decoration, or sit on dark backgrounds.
- Because Meta-ad traffic is mostly mobile (an assumption I did not verify for this store), mobile CPU cost matters most. That is the main reason to skip particle effects.

### Gaps
- No public A/B test isolates "Halloween look vs. control" without an offer. Measuring it here would need Shopify Rollouts Experiments, which require the Grow plan or higher (see Q4) and far more than 6 days of traffic.
- I couldn't get PageSpeed Insights field data (CrUX) for fitpatches.net because the API daily quota was exhausted. Only lab, unthrottled numbers are in Q5. Run PSI before and after publishing.

---

## Q3. Halloween palettes that work with a pink core colour (#d64d87), and brands that did "pink Halloween"

### Takeaway
"Pinkoween" became a mainstream retail trend in 2023–2025, so a pink-led Halloween look is on-trend and not a compromise. For FitPatches the strongest option is pink + near-black ("Pink Night"): it reuses #d64d87 and the #121212 already in the theme, and pink on black passes AA (4.70:1). Use pumpkin orange only as small decoration or on dark backgrounds. The theme already holds a Halloween-ready purple (#6d388b).

### Cited Findings
- Michaels launched 2025 Halloween lines on 13 June 2025. One of them, "Sweet & Spooky", is described as: "Pink and black collide in this bold update to #Pinkoween". Its motifs are heart-eyed skulls, disco ghosts and skeletons on pool floats, with Y2K/goth-glam styling. The CMO quote mentions "playful punk-inspired pastels". — [Michaels press release, 12 Jun 2025](https://www.michaelspressroom.com/news/detail/4973/codeorange-michaels-kicks-off-summerween-this-friday-the)
- A trade association reported pink pumpkins, skulls and decorations "taking more and more shelf space" at HomeGoods, Target, Walmart, T.J. Maxx and Michaels. It partly credits the "Pink-centric 'Barbie' movie". It quotes a consumer: "The pastel colors give more of a whimsical vibe", and notes that traditional Halloween goods come in black and orange. Dated 22 Aug 2024. — [Shop! Association: Pinkoween turning red hot](https://shopassociation.org/pinkoween-turning-red-hot/)
- NewsNation calls Pinkoween "the spooky season decor trend that's sweeping retailers, TikTok For You Pages…". Its shade range is "hot pink to fuchsia to coral to blush", recolouring the traditional black, grey, purple, orange and green. It names products such as pink skeletons, hot-pink pumpkins, pink bats wall décor and pink ghost candles (Hyde & EEK! Boutique at Target, Winlyn, Lakeside Collection, Minatee). Dated 25 Sep 2024. — [NewsNation/BestReviews: Pinkoween](https://products.newsnationnow.com/articles/holiday/halloween/pink-halloween-decor-pinkoween)
- In July 2025 HomeGoods stocked light-coloured, "more lighthearted" ghosts, monsters and skeletons, per a search snippet only (page not fetched). — [Apartment Therapy](https://www.apartmenttherapy.com/homegoods-pink-ghost-find-37497458)
- Contrast basis: SC 1.4.3 requires 4.5:1 for normal text and 3:1 for large text. — [W3C 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)

### Inferences
Contrast ratios I computed with the WCAG relative-luminance formula (my calculation, not a source):

| Pair | Ratio | Normal text AA | Large text / UI |
|---|---|---|---|
| White on brand pink #d64d87 (current PDP CTA) | 3.98:1 | fail | pass |
| #d64d87 on #121212 (pink on near-black) | **4.70:1** | **pass** | pass |
| #d64d87 on light pink #fbe9f1 (current PDP pills and price text) | 3.42:1 | fail | pass |
| White on coral #ea7e7e (current **homepage** CTA + marquee) | 2.70:1 | fail | **fail** |
| Light pink #ff9ec7 on #121212 | 9.78:1 | pass | pass |
| Pastel pink #f6c3dc on deep plum #2b1433 | 11.00:1 | pass | pass |
| Pumpkin #ff7518 on white | 2.69:1 | fail | fail |
| Pumpkin #ff7518 on #121212 | 6.97:1 | pass | pass |
| Dark orange #c2410c on white | 5.18:1 | pass | pass |
| White on theme purple #6d388b | 8.11:1 | pass | pass |
| Candy yellow #ffb400 on #121212 | 10.51:1 | pass | pass |

Proposed palettes (my inference):
1. **"Pink Night" (recommended):** #121212 (night; already the footer scheme and text colour), #d64d87 (brand pink: CTAs unchanged, pink text on dark bands), #ff9ec7 or #f6c3dc (soft pink for small text on dark), #fbe9f1 (existing blush backgrounds), plus a tiny accent of #ff7518 pumpkin or #ffb400 candy-corn yellow in icons only. It is closest to Michaels' "pink and black … #Pinkoween" look and keeps the brand recognisable.
2. **Pink + purple ("witchy"):** #6d388b (already the theme's link/outline colour and part of its `--gradient-base-accent-2` purple→maroon gradient) or deep plum #2b1433 for bands, with #d64d87 and blush. Halloween-coded without orange.
3. **Pink + orange ("candy pumpkin"):** works as illustration (pink pumpkins with orange stems, orange bats) but never as orange text on light backgrounds. If orange text is unavoidable, use #c2410c.
4. **Pastel spooky (lavender/mint/blush):** backgrounds and illustrations only. Low-contrast text risk, and it can wash out the existing light-pink site.
- Brand-consistency note: the homepage uses the theme accent coral #ea7e7e (CTA, marquee, "Как работи" band, footer strip), while the PDP uses #d64d87. A Halloween pass that recolours the homepage bands to #121212 + #d64d87 would also make the two pages more consistent and fix the 2.70:1 white-on-coral failure on those bands.

### Gaps
- I didn't verify any specific beauty or skin-patch brand's 2025/2026 pink Halloween storefront. Other researchers' screenshots in the same `shots/` folder (Starface, Peace Out, Hero, ZitSticka, ColourPop, Kylie) cover that.
- I found no data on how Bulgarian shoppers respond to Halloween or to "Pinkoween" specifically. Halloween's cultural weight in Bulgaria isn't researched here.

---

## Q4. Shopify mechanics: duplicate the live theme, edit the copy, schedule, sections vs CSS/JS, apps, revert after 31 Oct and move on to Black Friday

### Takeaway
On Basic, the safest workflow is: Duplicate the live theme → build the Halloween look on the copy → schedule it with an **Event rollout** ("Replace the current theme" with the copy, start and end date). Shopify then rolls back automatically after Halloween. Use theme-editor settings and section "Custom CSS" for most changes; a small CSS/SVG snippet inside the copy covers the rest. Avoid effect apps, because their code can stay behind after you uninstall them.

### Cited Findings
- Duplicate: Online Store > Themes > "…" > **Duplicate**. The copy appears as "Copy of [name]". The store can hold **20 themes**. If it already has 20 you must delete one first, and you can download it before deleting. — [Shopify Help: Duplicating themes](https://help.shopify.com/en/manual/online-store/themes/managing-themes/duplicating-themes)
- Rollouts (Markets > Rollouts) has three types. **Launch** "merges your changes into your store permanently". **Event** "publishes your changes for a set period, and then rolls them back". **Experiment** compares treatment and control. — [Shopify Help: Rollouts](https://help.shopify.com/en/manual/markets/rollouts)
- Plans: "Rollouts are available on the Basic plan or higher." "Experiments are available to stores on the Grow plan or higher." "You can't apply rollouts to vintage themes." "You can't change Liquid templates as part of a rollout." — [Shopify Help: Rollouts requirements and considerations](https://help.shopify.com/en/manual/markets/rollouts/requirements-and-considerations)
- Creating one: Create rollout → type → Add changes → under Online store either **"Replace the current theme"** (pick another theme already added to the store) or Edit theme (main theme only) → set a Start date and time ("Event runs from") → **Set end date** → Save. The timezone is the store's (Settings > General). Limits: **one theme change per rollout**. You can edit only your main theme. You can't target by device or customer segment. An active rollout must be ended manually. Adding an end date to a Launch turns it into an Event. — [Shopify Help: Create a rollout](https://help.shopify.com/en/manual/markets/rollouts/create-a-rollout)
- The 5 June 2026 changelog says Rollouts can set "a whole new theme" to go live at a chosen date and time, and has a "temporary swap" option that activates a theme for a set period "and revert[s] automatically afterward". It also covers A/B testing between two different themes. — [Shopify Changelog, 5 Jun 2026](https://changelog.shopify.com/posts/schedule-publish-and-a-b-test-new-themes-and-checkout-and-customer-account-configurations)
- Theme-editor Custom CSS: theme-wide under Theme settings > Custom CSS, which "applies to all pages except Checkout", or per section. Limits: "CSS rules that affect the entire theme are limited to 1500 characters" and "CSS rules that affect a specific section are limited to 500 characters". `@import`, `@charset` and `@namespace` aren't allowed. "The `content` property isn't available in custom CSS". Only cdn.shopify.com URLs are allowed. You can't target the wrapping `.shopify-section` element. — [Shopify Help: Add custom CSS](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/add-css)
- Apps: "Uninstalling an app doesn't automatically remove its code from your theme". Also: "Too many apps loading assets on your storefront can slow performance." — [Shopify Help: Improving speed](https://help.shopify.com/en/manual/online-store/store-speed/improving-speed)
- Third-party theme schedulers also exist, for example the "Themify: Theme scheduler" app. — [Shopify App Store: Themify](https://apps.shopify.com/themify-theme-scheduler?locale=cs)
- Agency advice: duplicate, edit the copy, test on mobile and desktop, then publish ("one-click rollback"), and "Never make significant theme changes during peak traffic hours". **Recommendation, not data.** — [Glued](https://getglued.co/insights/shopify-holiday-themes)

### Inferences
Recommended timeline. It's my plan, built on the mechanics above. 25 Oct 2026 is a Sunday and 31 Oct a Saturday. Black Friday 2026 is 27 Nov.
1. **Sun 25 – Mon 26 Oct:** Duplicate the current live theme ("FitPatches — снимки на пакетите 25.10", Shrine PRO 1.3.0) and name the copy "FitPatches — Halloween 2026". Check that the library isn't at 20 themes. Make all edits on the copy:
   - theme editor: favicon, logo variant, hero image, marquee text and colour, a new image in the "Природата в помощ" section;
   - section-level Custom CSS (≤500 chars each) for band colours and dividers;
   - any SVG patterns uploaded to Files (served from cdn.shopify.com).
   Because `content:` is blocked in editor Custom CSS, emoji or pseudo-element decorations go either in the marquee text itself or in a small snippet in the copy's code (Edit code). That is fine because the code lives only in the copy.
2. **Mon 26 Oct:** Preview the copy on real mobile devices. Check the COD form ("Бърза поръчка", middleware.bg script), the bundle picker, the sticky order bar, Meta Pixel and web pixels. Confirm visually that the order area is identical to live.
3. **Create an Event rollout:** "Replace the current theme" with the Halloween copy, starting e.g. **Tue 27 Oct 00:00** and ending **Sun 1 Nov 00:00 (or 06:00)** in store time (Europe/Sofia, which returned to EET on 25 Oct). Shopify then rolls back to the normal theme automatically.
   - If Rollouts doesn't show up in the admin, or the replace-theme option is unavailable: publish the copy manually on 27 Oct (Online Store > Themes > Publish) and re-publish the original on 1 Nov. Both stay in the library, so either switch is one click.
4. **Black Friday:** Make a fresh duplicate of the then-live theme in early November and schedule it as its own Event. Don't build Black Friday on top of the Halloween copy, because live-theme edits made after 25 Oct would be missing from it. Only one theme change is allowed per rollout, so Halloween and Black Friday must be separate rollouts.
- **Live-edit freeze risk:** the live theme was renamed today ("…25.10"), so the team edits it often. Any change made to the live theme during the Event won't appear while the Halloween copy is live. Freeze live-theme edits 27–31 Oct, or repeat them on the copy.
- **Apps vs snippet:** if any motion is wanted, a ≤40-line CSS-only snippet in the copy's code is better than an effect app. The snippet disappears when the theme reverts, while an app may leave code behind and loads JS on every page.

### Gaps
- The Help Center doesn't say whether a "Replace the current theme" Event works when the replacement theme contains code (Liquid/asset) edits. The rule "You can't change Liquid templates as part of a rollout" is about editing the main theme inside a rollout. Verify in the admin before relying on it, and keep manual publishing as the fallback.
- Not documented: whether duplicating copies app-embed toggles exactly, and what happens to main-theme edits made during an active Event. Verify in the preview.
- I didn't verify which Shopify plan fitpatches.net is actually on (the brief says Basic).

---

## Q5. Audit of fitpatches.net as it looks today (25 Oct 2026), and the natural spots for Halloween accents

### Takeaway
The site is a light, blush-pink and cream Shrine PRO theme, set entirely in Poppins. The homepage uses coral (#ea7e7e) accents and the PDP uses the brand pink (#d64d87). There is **no announcement bar** today. The best places for accents are the header logo and favicon, the homepage hero image, the coral marquee strip under the hero, the coral "Как работи" band, section seams, the centre image of the PDP "Природата в помощ на фигурата" section, and the footer. The whole PDP order block (bundle picker → "Поръчай сега" → delivery timeline → "Бърза поръчка" COD form → phone → sticky order bar) must stay untouched.

### Cited Findings (direct observation of the live site; sources: [fitpatches.net homepage](https://fitpatches.net/) and [main product page](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30), audited 25 Oct 2026 with Playwright, read-only)

**Theme and tech**
- `Shopify.theme`: name "FitPatches — снимки на пакетите 25.10", schema **Shrine PRO 1.3.0**, id 209287643473, role main. — [fitpatches.net](https://fitpatches.net/)
- Global sections in the DOM that are hidden or zero-height: `cart-drawer`, `promo-popup`, `scroll-to-top-btn`, `global-music-player`. — [fitpatches.net](https://fitpatches.net/)
- Third-party scripts on the PDP:
  - `co.middleware.bg/shopify/co/…js` (COD order integration);
  - `intl-tel-input 17.0.19` (phone field);
  - two Meta Pixel configs;
  - Shopify web pixels;
  - privacy banner;
  - Shopify perf-kit.
  — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30)
- Favicon: `cdn/shop/files/fitpatches-favicon-512.png` rendered at 32×32. — [fitpatches.net](https://fitpatches.net/)
- Lab check (mobile 390×844, unthrottled, so it shows which element is LCP but isn't a field score):
  - Homepage: LCP element = hero pack PNG `fitpatches_2048_no_white_background.png` (~149 KB), LCP ≈ 1.0 s, CLS 0.000, 738 DOM nodes, about 2.5 MB decoded JS.
  - PDP: LCP element = first gallery image (before/after composite), LCP ≈ 1.0 s, CLS 0.000, 1,875 DOM nodes.
  — [fitpatches.net](https://fitpatches.net/), [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30)
- The theme already contains some `prefers-reduced-motion` CSS rules. But the homepage marquee (`fp_scroll`, 25 s infinite loop) **keeps scrolling when reduced motion is requested**, and there is no visible pause control. A loading-spinner SVG animation (`rotator`/`dash`) is also present. — [fitpatches.net](https://fitpatches.net/)

**Colour palette (from `:root` variables and computed styles)**
- Theme tokens:

  Note: the brief gives the core brand colour as #d64d87. On the live site only the PDP's custom `fp` sections use it; the theme-level accent is the coral #ea7e7e.

  | Token | Value |
  |---|---|
  | `--color-base-background-1` | #fcf1f1 (blush; body background) |
  | `--color-base-background-2` | #f3f3f3 |
  | `--color-base-text` | #121212 |
  | `--color-base-accent-1/2` | #ea7e7e (coral; homepage buttons, marquee, "Как работи" band) |
  | `--color-base-outline-button-labels` / link | #6d388b (purple) |
  | `--gradient-base-accent-2` | linear-gradient(54deg, #6d388b 14% → #690e0e 85%) |

  — [fitpatches.net](https://fitpatches.net/)
- PDP custom section variables: `--fp-accent: #d64d87` (brand pink: "Поръчай сега"/"Бърза поръчка" buttons, prices per day, eyebrows), `--fp-accent-soft: #fbe9f1`, `--fp-warm: #faf0f4`, `--fp-red: #e23b3b`. Savings chips are green (#1f8a4c / #2e7d32 on #edf7ed). Review stars are yellow (#ffb400 / #f6c343). — [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30)
- Other observed colours:

  | Where | Colour |
  |---|---|
  | Header background | #f0c3dc (pink) |
  | Homepage hero background | #faf6f1 (cream) |
  | Homepage "notes" | #c0392b |
  | Footer | Renders as a thin **coral #ea7e7e** strip (52 px desktop / 39 px mobile) with no visible links, checked by pixel sampling of the screenshots. The footer section's inline CSS declares a #121212 custom colour scheme, but that is not what renders. |

  — [fitpatches.net](https://fitpatches.net/)

**Fonts**
- `--font-body-family` and `--font-heading-family` are both **Poppins**. Weights in use: 400, 500, 600, 700, 800, 900. Headings are mostly 900 (22–30 px). PDP CTAs are 800 at 16–19 px. Also present: Material Symbols Outlined (FAQ check-box icons), a couple of Assistant nodes, and Arial for icon-only buttons. — [fitpatches.net](https://fitpatches.net/)

**Homepage sections, top to bottom** (desktop y-offset / height px):
1. **Header** (0/161, mobile 111): pink #f0c3dc, centred round "FP FitPatches" monogram logo, search and account icons. **No announcement bar.**
2. **Hero `qv_hero`** (161/580): cream background; left, the pack shot on a pink backdrop with pomegranate and herb props (LCP); right, "★★★★★ 4.8/5 според 1,837 клиентки", H1 "КОНТРОЛИРАЙ АПЕТИТА И ОТСЛАБНИ ДО 8 КГ ЗА 30 ДНИ", 3 outline pills (БЕЗ ХАПЧЕТА / БЕЗ ДИЕТИ / 100% НАТУРАЛНО), coral CTA "ПАЗАРУВАЙ СЕГА →", microcopy "Наложен платеж · 30 дни гаранция". On mobile the image stacks above the text.
3. **Marquee `qv_marquee`** (741/49): coral band, white uppercase "✦ КОНТРОЛ НА АПЕТИТА ✦ 100% НАТУРАЛНО …" scrolling.
4. **VS `qv_vs`** (790/721): "FitPatches срещу Ozempic" check/cross table on white.
5. **How `qv_how`** (1511/537): full-width **coral band**, white heading "Ето как FitPatches работи", 4 photo cards (Избери/Отлепи/Залепи/Усети).
6. **Science `qv_science`** (2048/557): cream, 3 numbered points with a photo of a doctor holding the pack.
7. **Before/after `qv_ba`** (2605/788): belly before/after image card.
8. **Stats `qv_stats`** (3393/340): 97% / 95% / 92% cards.
9. **Doctor quote `qv_doctor`** (3733/268): "ПРЕПОРЪЧАНО ОТ ЛЕКАР", д-р Александър Димитров.
10. **FAQ `qv_faq`** (4001/482): blush background, 7 accordion rows.
11. **Guarantee `qv_guarantee`** (4483/176): coral-outlined card "30-дневна гаранция за връщане".
12. **Reviews `qv_reviews`** (4659/1398): "4.8 ★★★★★ според 1,012", grid of review cards with "Потвърдена покупка" chips.
13. **Footer** (6057/52): thin strip with almost no links visible.

— [fitpatches.net](https://fitpatches.net/)

**PDP sections, top to bottom** (desktop y / height px):
1. **Header** (same as the homepage).
2. **Main `main`** (161/2615):
   - Left: gallery with the first image a before/after mirror-selfie composite with the pack and a patch close-up (LCP), plus thumbnails.
   - Right:
     - title "Започни да сваляш килограми след 20 дни…", "4.8/5 според 2365 доволни клиенти", "само 0,27 € на ден", pill "Плащане при доставка";
     - 4 benefit rows with pink icon circles;
     - **bundle picker "Колко пакета желаете?"** (1 пакет 14,99 € / 2+1 подарък 27,99 € / 3+2 подаръка 39,99 € with a "Най-изгодно" ribbon, struck-through prices, green "Спестяваш" chips);
     - pink CTA **"Поръчай сега"** with the microcopy "Плащане при доставка · Доставка до 2–4 работни дни · Без предплащане";
     - **delivery timeline** (25 / 26 / 27 октомври: Поръчано / Изпращане / Доставено);
     - **"Предпочиташ по-лесна поръчка?" box with the "Бърза поръчка" button**, opening the `fp-order` form (fields Име, Телефон, a hidden honeypot field, "Изпрати заявка");
     - phone line "0887 459 494";
     - "50+ диетолози…" authority strip;
     - objections accordion "Знаем какво си мислиш.";
     - 2 mini-reviews and "Виж още отзиви".
   - A **sticky order bar** ("3+2 подаръка 149,95 € 39,99 € / Поръчай сега") stays fixed on scroll on desktop and mobile.
3. **`fp_features`** (2776/596): "Природата в помощ на фигурата. Без хапчета. Без мъчение." (second line in pink), with a centred pink card holding the pack image and 4 icon bullets.
4. **`fpx_vs`** (3372/825): "Лепенка срещу берберин на капсули".
5. **`fp_howworks`** (4197/537): 4 numbered photos.
6. **`fpx_layers`** (4734/586): "Какво има в една лепенка" exploded-layer render.
7. **`fpx_nostomach`** (5320/563).
8. **`fp_science`** (5883/759): pomegranate, ginger and flowers prop photo.
9. **`fpx_timeline`** (6642/926): "Първите 30 дни с FitPatches".
10. **`fp_fb_reviews`** (7568/1432): Facebook-style comment cards.
11. **`fp_analysis`** (9000/1878): "Научен анализ".
12. **`fpx_faq`** (10878/1466): grouped FAQ (ЗА ПРОДУКТА / УПОТРЕБА / БЕЗОПАСНОСТ / РЕЗУЛТАТИ / ПОРЪЧКА И ДОСТАВКА) with the phone number.
13. **Footer.**

— [PDP](https://fitpatches.net/products/fitpatches-berberinovi-plastiri-30)

### Inferences: where Halloween accents fit (✅ = recommended, ⚪ = optional, ⛔ = do not touch)

**Global**
- ✅ Favicon: pink pumpkin, or the FP monogram with a bat, 32×32.
- ⚪ Logo: same circular monogram with a tiny bat or witch hat. Keep the file dimensions so the 161/111 px header height doesn't change.
- ⚪ Header background stays #f0c3dc. Optionally add a 6–8 px spider-web/"drip" SVG edge under the header, at fixed height.
- ⚪ Optional new announcement bar, e.g. "🎃 Честит Хелоуин от FitPatches", in #121212 with #ff9ec7 text. If added, it must be a native header-group section (server-rendered, fixed height), not an app bar.
- ✅ Footer strip: recolour it to #121212 / plum and add one line, "Честит Хелоуин 🦇".
- ⛔ The global music player and the promo popup: don't activate them for Halloween. No sound, no new popup.

**Homepage**
- ✅ Hero: swap the hero pack shot for the same composition with Halloween props: mini pink and orange pumpkins, black taper candle, a few dry leaves, maybe a small ghost. Same 2048 px PNG/WebP, ≤150 KB, same aspect ratio. It is the LCP element, so don't add any overlay animation to it.
- ⚪ Hero: a small "Хелоуин издание" pill above the stars. Leave the H1, the 3 pills, the CTA and the COD/guarantee line unchanged.
- ✅ **Marquee strip, the single best spot:** background #121212 or plum #2b1433, text #ff9ec7 or #d64d87, separators "🦇" and "🎃" instead of "✦". At the same time, add a `prefers-reduced-motion: reduce` stop and ideally a pause-on-hover/tap. This also fixes the existing WCAG 2.2.2 gap.
- ✅ "Как работи" coral band: recolour it to the dark Pink Night band, or keep coral and add faint spider-web corner SVGs at 6–8% opacity, outside the card area.
- ⚪ Section eyebrows ("— СРАВНЕНИЕ —", "— НАУЧЕН АНАЛИЗ —", "ПРЕДИ / СЛЕД", "✦ ОЦЕНКИ НА КЛИЕНТИТЕ ✦"): swap the dashes or ✦ for a tiny bat. Eyebrow text only.
- ✅ Section seams: one spider-web or "drip" divider between hero and marquee, and one before the footer. Fixed-height inline SVG.
- ⛔ Leave these exactly as they are:
  - VS Ozempic table;
  - before/after;
  - 97/95/92% stats;
  - doctor card;
  - FAQ;
  - guarantee box;
  - reviews grid (trust and claims content, see Baymard and NN/g in Q2).

**PDP**
- ⛔ Leave the first gallery image (before/after, the LCP element) as it is. ⚪ Optionally add one Halloween-propped pack photo as a later gallery image.
- ⛔ **Do not touch:**
  - title, stars, "само 0,27 € на ден", "Плащане при доставка" pill, benefit rows;
  - **bundle picker**;
  - **"Поръчай сега"**;
  - **delivery timeline**;
  - **"Бърза поръчка" box and `fp-order` form**;
  - phone line;
  - **sticky order bar**;
  - objections accordion and mini reviews.

  The COD form (middleware.bg) and the honeypot field are functional, and any CSS bleed-over risks breaking orders.
- ✅ `fp_features` "Природата в помощ на фигурата": swap the centre pack image for the Halloween-propped version. Optionally add faint bat silhouettes inside the pink card.
- ⚪ Eyebrows on later sections ("СРАВНЕНИЕ", "КАК ДЕЙСТВА", "ОТВЪТРЕ", "БЕЗ КАПСУЛИ", "ПРИРОДНА ФОРМУЛА", "КАКВО ДА ОЧАКВАШ", "ВЪПРОСИ"): a tiny bat or pumpkin icon only.
- ⛔ Leave the FB reviews, "Научен анализ" and FAQ content unchanged.

**Palette and type for the refresh**
- Use "Pink Night" (#121212 + #d64d87 + #ff9ec7 + blush #fbe9f1, with pumpkin #ff7518 or candy #ffb400 only in icons).
- Keep **Poppins** and don't load a "spooky" web font. web.dev says web fonts can cause layout shift, and an extra font adds weight. For a themed wordmark, use a small SVG/PNG.
- Leave the existing contrast problems on order-path elements as they are during Halloween (the "don't touch" rule): white on #ea7e7e is 2.70:1 and #d64d87 on #fbe9f1 is 3.42:1. Note them for a later fix.

**Motion budget:** no falling elements, no custom cursor, no countdown. The only motion is the existing marquee, made to respect reduced motion. If the owner insists on bats: one CSS-only fly-across of 3–5 bats on the homepage, ending within 5 s, transform/opacity only, `pointer-events:none`, inside `@media (prefers-reduced-motion: no-preference)`, in the theme copy's code, never via an app.

### Gaps
- I only audited the homepage and the main PDP. I didn't open the collection pages, cart drawer, 404 page or the middleware.bg COD modal itself, because opening the modal or submitting the form could create a real order request and the audit was read-only.
- I have no field (CrUX) Core Web Vitals for fitpatches.net because the PSI API quota was exhausted. The lab numbers above are unthrottled and only show which element is the LCP.
- I didn't check whether the Shrine PRO theme has a built-in seasonal-effects or announcement-bar section that could be enabled without code. Check Theme editor > Add section in the duplicate.
