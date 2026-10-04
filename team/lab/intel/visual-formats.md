# Библиотека с визуални формати (извън UGC talking head)

Води я `market-scout`. Една карта = един визуален формат (VF-###). Картите със статус „нов“ влизат в лаб смяната като ген `visual_format`. Поне 1/3 от вариантите в рунд са от тук (решение на собственика, 02.10).

**Създадена:** 02.10.2026, 20:30–21:00 (София), по искане на собственика: „искам постоянно да скаутват и за други визуални формати освен UGC видеа“. Без заявки към Ads Library (бюджетът за деня е изчерпан, ≈19). Източници: публични разбивки по света (WebSearch, WebFetch) и сигналите в заглавията от нашата памет `ads-seen.jsonl`.

**Ограничение.** Ads Library API дава само страница, заглавие и дати. Snapshot-ът връща 403, а TikTok Creative Center без JS е празен. Затова визията на конкретна чужда реклама не се вижда. Сигналите за скалиране тук са два вида: (1) количествени бенчмаркове от публични отчети (Motion: 578 750 креатива, IX.2025–I.2026) и брой марки, които ползват формата; (2) дълголетие и обем в нашата памет, по заглавията. Числа без източник няма. Където няма данни, пише „няма данни“.

**Правила за риска** (същите като `team/compliance-rules.md`): без преди/след, без кг и срокове, без „ти след 40“ и „имаш ли“, без фалшиви коментари, отзиви и новини, без „без инжекции“ като свойство на продукта, без „през кожата“. Цена винаги с доставката: „14.99 € + доставка“. „3+1 подарък 39.99 € · безплатна доставка“ и „около 0.33 € на ден“ стоят само в един ред. Персона или първо лице означава надпис „Драматизация“ (при AI: „Драматизация · създадено с AI“). Срокът на гаранцията чака собственика: `[ГАРАНЦИЯ: 60 или 30?]`.
> Бележка: според разбор на adligator.com Meta от 22.07.2026 съди здравните реклами по конкретните твърдения, а не по категорията, и „преди/след“ вече не е забранено само по себе си ([източник](https://adligator.com/blog/meta-health-wellness-ad-policy-update-2026); това е тълкуване на блога, не текст на Meta). **Нашите правила не се променят:** преди/след остава забранено, докато compliance-officer не реши друго.

---

## Таблица (подредена по сила на сигнала, че скалира)

Сила: **A** = количествен бенчмарк за скалиране + сигнал в здраве/wellness или в нашата памет; **B** = много марки или бенчмарк в средата; **C** = само описания, органичен тренд или сигнал под средното.

| Код | Формат | Скалира ли (сигнал) | Трудност | Статус |
|---|---|---|---|---|
| VF-001 | „Цената първа“ (offer-first банер) | **A.** Motion: 29.3% от разхода при 21.9% от креативите, hit rate 8.6%. Памет: статики с оферта 33 реклами ≥30 дни; BG „1 закупен = 1 БЕЗПЛАТНО“ 79.5 дни; ES 03.10: Velia Parches 1+1 → 2+2 GRATIS, 30 за 6 дни · DE 04.10 (уеб): статиките с оферта водят и при законните марки за жени в DE: Bears with Benefits Offer-First 36% (74 активни, ≈28 нови на седмица), MORE Nutrition 17% (топ рекламата е статик с отстъпки; 1 084 активни, €2.7M в DE), FEMNA: и трите топ реклами са статики с оферта на 19–21 дни („Nur im September: 2-für-1“) | ниска | нов |
| VF-002 | „Стек от доверие“ (F-010) | **A.** Памет: FreshHaut (DE) 14 варианта за 25 ч; Bany RO 25.4 дни; Chillama „✅ 90 дни гаранция“ 35.6 дни; 3+ марки; ES 03.10: стек с наложен платеж на първо място при лепенките 21–25 дни (Dra. Laura Martínez, LuzMar) · RO 04.10 (уеб): същият стек е и на сайта на Bany („Livrare 1–3 zile · Plată la livrare · Retur 14 zile · Comandă rapidă, fără cont necesar · Mii de comenzi livrate“) | ниска | нов (гаранцията чака собственика) |
| VF-003 | Карта с цитат или отзив | **A.** Motion: Testimonial 13.3% от разхода, hit rate 6.5%. Памет: карти с брой отзиви 26 реклами ≥30 дни (HarmonyHug 106 дни) | ниска | нов (реален отзив: чака `voc.md`) |
| VF-004 | Писмо (letter) | **A.** Motion: hit rate 10.83%, ≈1.7× дял от разхода спрямо обема; №2 по spend use в Health & Wellness | ниска | нов |
| VF-005 | Голям текст без снимка (native) | **A.** Motion: Text only hit rate 11.6% (по-високо е само Stitch в H&W) | ниска | нов |
| VF-006 | Скрийншот от бележника в телефона | **A.** Motion: 100+ марки (Reframe 393 реклами, Headway 216); „social post mockup“ е №1 по spend use в Health & Wellness. Против: 2 теста на NextAfter губят | ниска | нов |
| VF-007 | Разопаковане без лице (ръце + плик от Еконт) | **A.** Motion: Unboxing hit rate 9.8%, spend use 1.3; в топ по hit rate в Health & Wellness | ниска–средна | нов |
| VF-024 | „Въпросът горе, отговорът долу“ (Stitch: чужд въпрос, наш отговор; видео с 2 жени) | **A.** Motion: Stitch е №1 по hit rate в Health & Wellness (12.50), Reaction video №2 (11.24); 11 марки с 13–59 реклами (Dose, Primal Queen, Auri, Rise Science, DRMTLGY). Лаб: „човек отговаря на въпроси“ печели (F-004 37.0, S3-30 36.4, A17 34.7). Памет: възражението като заглавие при 4 марки (Krista G BG, 03.10) | ниска–средна (2 клипа с телефон) | **нов (03.10), за лаб смяната (CB-036)** |
| VF-025 | „Снимка с човек + текст отгоре“ (UGC overlay, статик) | **A.** Motion: UGC overlay в топ 10 по spend use в Health & Wellness; JSHealth 1 000+, Happy Mammoth EU 600 + 531, Vitabiotics 511, Nutrition Geeks 364. Лаб: статиките без човек губят (19.5–24.2) | ниска (1 снимка + Canva) | **в симулация като CB-035 (4) (20261003-0859-active); чист A/B: CB-037** |
| VF-008 | Ръкописно листче, тетрадка, post-it | **B+.** Motion: Post It ≈1.3×, 100+ марки (Happy Mammoth); Sign 7.86%; Unconventional text placement 9.63%. ADM: +26% ROAS, −23% цена на поръчка (здраве и красота) | ниска | **за 23:11** (F-011) |
| VF-009 | Карусел-чеклист (A13 в 5 карти) | **B+.** Happy Mammoth: Listicle = 13% от ≈1 000 активни реклами; Motion Listicle 5.3%; A13 два пъти в топ 4 в симулацията | ниска | **за 23:11** (A13) |
| VF-022 | „Какво е · за какво е · как се ползва“ (етикетна карта + How To с ръце) | **B+.** Motion: Demo е №3 в Meta, hit rate 8.1%, 12.6% от креативите и 12.9% от разхода; How To при AG1, HUM. BR 03.10: 4 страници за 2 дни слагат името и какво е продуктът в заглавието (Arnaldo Roberto ×43). Лаб: P15 (59 г.) в 8 от 11 варианта казва „не разбрах за какво е“ | ниска | **нов (03.10), за лаб смяната** |
| VF-023 | „Един ден, 4 снимки“: демонстрация с ръце, тест за носене (без персона и без „Драматизация“) | **B+.** Kind Patches (US, най-голямата марка с лепенки): Demo 15% от ≈2 000 активни реклами, ≈168 нови на седмица. Motion Demo: hit rate 8.1%, 12.9% от разхода. ES 03.10: Velia Parches ×30 за 6 дни, Kind Patches ES с „Parches de Berberina“ (нашите 3 съставки). Число за „тест за носене“ няма | ниска (1 ден снимки с телефон) | **нов (03.10), за лаб смяната (CB-032)** |
| VF-026 | „Скептикът вкъщи“ (скеч в кухнята: съпругът пита, тя отговаря) | **B+.** Motion Skit: Liven 3K реклами, Rise Science 2K, WalkFit 1K. WalkFit (жени 50+, менопауза): 426 активни, ≈192 нови на седмица, скечове, в които едната е скептична. Hit rate за Skit няма. Лаб 08:59: печели диалогът (A18 35.0, анкета 33.0, A19 „дъщеря ми пита“ 32.6), монолозите губят (20.6–25.2) | ниска (1 кухня, 2 души, телефон) | **в симулация: №2 на 15:11 (37.4, 73%); №1 на 23:11 (36.2, 66% срещу A19); контрола в 03:11 (20261004-0312-active)** (CB-040) |
| VF-028 | „Пратката в колата“ (майка и дъщеря в паркираната кола, двете лица в кадъра; Reaction при отварянето: „Това ли е? Толкова малка?“) | **B+.** Motion: Reaction video е №2 по hit rate в Health & Wellness (11.24); в определението на Motion един от примерите е „двама приятели в паркирана кола“; Hismile 703, Zeely 387, BOTB 162 реклами. US: Bioma (GLP-1, 459 активни, ≈111 нови на седмица) ползва двойка и подкаст. Лаб 19:11: семейството пита и печели (A19 38.7, VF-026 36.0), без лица губи (гласовите 28.4, комикс 23.8). Число за „майка и дъщеря“ няма | ниска (1 кола, 2 души, телефон на таблото) | **в симулация (20261003-2312-active):** V-б (сестрата) №5, 31.4 (53%); V-а и V-в чакат compliance по ред 210 |
| VF-029 | „Разпит на разходката“ (walk-and-talk: двамата вървят един до друг, селфи two-shot в движение; мъжът пита, тя отговаря) | **B.** WalkFit (жени 50+, Motion): 426 активни, ≈192 нови на седмица; рекламите с двама са „two-shot walking sequences“ (данните са отпреди ≈4 месеца). Ready Set (Motion, VI.2026): „нова двойка, същият кадър“ дава нов топ резултат. Лаб 23:11: мъжът пита е №1 (VF-026 36.2), но задържането пада 69% → 44% във втората половина. В PL формат с двама не е видян (няма данни). Число за „разходка с двама“ при добавките няма | ниска (1 алея, 2 души, телефон); средна при AI | **губещ в симулация (20261004-0312-active):** последна, 24.3 (8%); движещият се фон губи от статичната кухня |
| VF-030 | „Реакцията на фризьорката“ (Reaction + Demo във фризьорския стол: двете лица фронтално, фризьорката чете кутията и реагира на лепенката; несемеен питащ) | **B+.** Motion: Reaction video е №2 по hit rate в Health & Wellness (11.24), най-често с Demo (36%); Hismile 703, Dr. Squatch 95, Clean Skin Club 86 реклами. Motion Skit: WalkFit (жени 50+) 426 активни, ≈192 нови на седмица, скечове с две жени, едната скептична. Лаб: A17 „фризьорката пита“ (само ръце и глас) 35.7 → 34.7; VF-026 (кухня, статично) 35.0; реакция в колата 30.0 и 28.8, разходката 24.3. Число за „салон“ или „фризьорка“ в реклами няма · RO 04.10: Catena (ТВ) снима съседка вместо фармацевт → несемейният връстник е наследникът на забранения авторитет; RO наследник VF-033 | ниска (1 салон, 2 актриси, телефон на плота) | **нов (04.10, 07:11), в рунд 20261004-0712-active (CB-054)** |
| VF-031 | „Подкастът на дивана“ (две жени на дивана с обикновени микрофони, статичен two-shot; водещата задава 5 бързи въпроса, гостенката отговаря с по едно изречение) | **B.** GB (04.10): в списъка Podcast на Motion 3 от 12 марки са британски (Your Heights, Spacegoods, Huel), плюс Happy Mammoth. Your Heights (UK, 40+): 343 активни, ≈109 нови на седмица, основателят интервюира клиент; Spacegoods (UK, жени 25–55): 272, ≈112 на седмица; Happy Mammoth EU: 988, ≈106 на седмица, „две жени на жълт диван“, статични кадри. Hit rate няма, данните са отпреди 4–5 месеца. Лаб 03:11: анкетата без монолога №1 два пъти (35.8), статичната кухня бие всички, разходката последна (24.3) | ниска (1 хол, 2 души, телефон на статив) | **нов (04.10, 07:11)**; V-а без хормони и не е семеен скеч; V-б е чист A/B срещу VF-027 V-а (улица → диван); V-в (собственикът + истинска клиентка) е блокиран |
| VF-010 | „Ние срещу тях“ без марки (рутина, не ефект) | **B.** Motion: hit rate 6.52%; Ridge върти формата постоянно. Памет: 92 реда „сравнение“ (Hormone Health Lab ×32 в партида) · RO 04.10 (уеб): 4 марки с „без хапчета“ (Bany 40.6 дни, Tinyshopstore 84.8 дни, Plasturel с таблица „лепенки срещу хапчета“, Kenku „vs Alte Mărci“) | ниска | нов |
| VF-011 | Скрийншот от чат | **B.** Motion: 20 марки, сред тях AG1, Happy Mammoth, Magic Mind, Hims; „social post mockup“ №1 в H&W | ниска | **губещ в симулация (20261003-2312-active):** A19 като чат 23.6, последен, 0% срещу контролата |
| VF-012 | Split screen (говорещ кадър + карти) | **B.** Motion: 4K+ уникални реклами от топ марки (Health Insider, Shapermint); в топ листата по hit rate (диапазон ≈5–9%) | средна | нов |
| VF-013 | Статик „проблем → решение“ | **B.** Superscale и Adrio: най-подходящ за добавки; Problem Agitation в топ листата на Motion. Памет: F-003 (Bany RO 40 дни, Tinyshopstore 84.8 дни; визията неясна) | ниска | нов |
| VF-014 | Подкаст клип (2 жени, 2 микрофона) | **B−.** Motion: 12 марки (Happy Mammoth, Primal Queen, Magic Mind, hims); числа няма. Лаб: диалогът S3 е №1 на 08:59 | висока | нов; GB 04.10: 3 британски марки в списъка Podcast на Motion (Your Heights, Spacegoods, Huel). Домашната версия с ниска трудност е VF-031 |
| VF-027 | „Пет бързи въпроса на улицата“ (интервюиращата не спира да пита, жената с плика от Еконт отговаря; брояч 1/5…5/5) | **B−.** Motion Street Interview: 18 реклами от 17 марки, 4 от здраве и добавки (BetterHelp, Cadence, Your Heights, Drink Magna); hit rate няма. Лаб: уличната анкета (WILD) е №1 на 15:11 (37.7), но задържането пада от 81% на 56% в сцената без въпрос. VF-027 маха монолога | ниска (1 улица, 2 души, телефон + микрофон без лого) | **в симулация (20261003-2312-active):** V-б №3, 35.1 (56%) над WILD 32.6; V-а №6, 31.2 (36%) |
| VF-032 | „Екранът на поръчката“ (Checkout Mockup: истинската COD форма на телефон в ръка, изрязана до цената и плащането при доставка) | **B−.** GB (04.10): Vitabiotics (UK) е №1 в Motion по брой реклами в този формат (21); 760 активни, ≈75 нови на седмица, „цената първа“ 35%, „3 за 2“ на целия сайт. Още в здравето: Ancient + Brave (UK), Four Sigmatic, Bloom. Hit rate няма. Лаб: цената от 0 сек печели (A9 41.1), статиките без човек губят (19.5–24.2) | ниска (1 снимка) | **нов (04.10, 07:11)**; V-а (1 пакет) минава; V-б (3+1) чака ред 94 |
| VF-033 | „Съседката от входа“ (скеч пред пощенските кутии: съседката вижда плика от Еконт и пита, героинята отговаря; двете лица фронтално, есенни палта; несемеен връстник) | **B−.** RO (04.10): Catena, най-голямата аптечна верига, снима ТВ спот с две съседки („Bună, vecino!“), защото на фармацевтите е забранено да препоръчват в реклама (CNA 573/2025); CNA го забрани заради препоръката за чужд симптом. Bitdefender: „диалог на двама“ е сред форматите на мрежи с десетки хиляди реклами в RO (с фалшив авторитет; мрежата на DIICOT е и в BG). Motion Skit: Liven 3K, Rise Science 2K, WalkFit 1K. Лаб: VF-030 34.2 ≈ контролата 34.4, служителката на гишето A25 губи (25.4). Число за „съседка“ в Meta няма | ниска (1 вход на блок, 2 актриси, телефон на перваза) | **нов (04.10, 08:59), за 11:11:** V-а 27 сек срещу VF-026; V-б 20 сек е чист A/B на дължината; V-в статик |
| VF-034 | „Класацията на двете приятелки“ (две връстнички на кухненската маса подреждат 5 неща, които са пробвали сутрин, по това кое не забравят; лепенката е последна и без номер; двете лица фронтално, несемейни) | **B−.** DE (04.10): MORE Nutrition, най-голямата DTC марка в Meta в DE (Brandsearch: 1 084 активни, €2.7M в DE; Motion: 209 активни, ≈21 нови на седмица), органично пуска две инфлуенсърки, които „класират“ вкусовете (webnetz, 13.02.2026); „Supplement-Tierlist“ е тренд в немския TikTok (Марио Мюлер, 62.1K харесвания); Dr. Squatch с немски глас „Die drei besten Deodorants“ (Motion Skit). Листикъл: Happy Mammoth 13%. Лаб: несемейната питаща стига контролата (34.2 срещу 34.4), краят губи (19–25% стигат края). Hit rate за класация с двама няма | ниска (1 кухня, 2 актриси, 5 предмета, телефон на статив) | **нов (04.10, 11:11), за 15:11:** V-а 30 сек (5 предмета) срещу VF-026; V-б 21 сек (3 предмета) е чист A/B на броя; V-в карусел |
| VF-015 | Карусел-история (пратката пристига) | **B−.** Adlibrary: 10 разбора на карусели, всички въртят 60+ дни (MUD/WTR при добавките). AdRiseLab: 5 карти = +27% CTR (собствено проучване, 320 реклами) | ниска | нов |
| VF-016 | Инфографика „какво има вътре“ | **B−.** Motion Infographic: AG1, IM8, Nutrafol; Feature benefit pointout 5.61%; Curtis Howland: за добавки със съставки | ниска | нов |
| VF-035 | „Истинският човек зад телефона“ (статик: снимка на човека, който вдига 0887 459 494, с първото име и почерк; без продукт и без съвети) | **C+.** DE (04.10): VitaMoment (€247.6K в DE, 28 активни, 1.7M посещения на месец), топ статик на 9+ дни „Hinter jeder Nachricht an uns steckt ein echter Mensch“; Doppelherz говори през служители (≈20 млн. показвания в TikTok при ≈15K последователи). Лаб: статиките без човек губят (19.5–24.2). Hit rate няма | ниска (1 снимка) | **нов (04.10, 11:11)**, блокиран: собственикът потвърждава кой вдига телефона и кога |
| VF-017 | Green screen с адвърториала | **C.** Motion: Greenscreen 4.87% (под средното). Памет: адвърториалите са 27% от рекламите, но 30+ дни оцеляват само 5 от 392 | средна | нов (блокер: AD27/AD28) |
| VF-018 | Google търсене (native search) | **C.** Motion: 17 топ марки (SHEIN 366 реклами); в здраве няма данни | ниска | нов |
| VF-019 | Кинетична типография (видео само с текст) | **C.** Пряко число няма. RocketShip HQ: сложната кинетика губи, простото „pop/fade“ печели | ниска | нов |
| VF-020 | 2D анимация / skeleton | **C.** Motion Animation: 100+ марки (Liven 654 реклами, BetterMe 587), hit rate не е потвърден. Skeleton е органичен тренд без рекламни данни. Лаб: анимацията ad1 дърпа грешна аудитория | висока | нов (CB-008) |
| VF-021 | AI аватар (водеща, не клиентка) | **C.** Данни за ефект няма (само цена: 15 сек ≈ 4.46 $ срещу 150–300+ $ за UGC). Meta: етикет „AI info“ | средна | нов, висок риск |

---

## Какво казва нашата памет (`ads-seen.jsonl`, 1 438 реда, 02.10)

**Метод (груб, по заглавието).** Заглавието е заглавието на линка, не текстът на визията. Правила, в този ред:
1. **Карусел или каталог:** няколко заглавия в една реклама, слепени с „ | “, с повторение, цени, продукти или „(Katalog)“; или етикет „каталог“. Ако са различни hook-ове, това е DCO (динамични текстове), визията е неясна.
2. **Статика · рейтинг:** „4,8/5“, ★, „N отзива“, Trustpilot.
3. **Статика · стек от доверие:** 2+ емоджита-доверие (✓ ✅ 🌿 💯 🚚 💰 🇩🇪…) + гаранция, доставка, „произведено в…“ или разделител „|“.
4. **Статика · оферта:** %, 1+1, „Buy 1“, „OFF“, „RABATT“, „безплатно“, „подарък“, код, цена; или етикет „статична оферта“ от предишните смени.
5. **Адвърториал:** „Lies den Artikel“, „Read more“, „Научи повече“, „Here's why“, „скрита причина“ и т.н.; или етикет „новинарски адвърториал“, „история от първо лице“, „партньорска страница“, „листикъл“.
6. **Квиз:** „Take the Quiz“, „квиз“, „challenge“. Визията е неясна, ясна е само фунията.
7. **Вероятно видео (слаб сигнал):** етикет „UGC / отзиви“ или „лекар“ без рейтинг. Явни думи за видео („Watch“, „▶“, „подкаст“) в заглавията: **0**.
8. Всичко друго е **неясно**.

От 02.10 всеки ред има поле `visual` (`static` | `carousel` | `advertorial` | `unknown`), а при нужда и `visual_hint` (`static_offer`, `static_rating`, `static_trust_stack`, `quiz_link`, `video_ugc?`, `video_other?`, `dco_multi_title`, `empty_title`). „unknown“ е честен отговор.

| Визуален сигнал | Редове | Дял | Въртят ≥21 дни | Въртят ≥30 дни |
|---|---|---|---|---|
| **Статика (общо)** | 287 | 20% | 70 (24%) | **59** |
| · оферта | 204 | 14% | 41 | 33 |
| · рейтинг / брой отзиви | 61 | 4% | 26 | 26 |
| · стек от доверие | 22 | 2% | 3 | 0 |
| **Адвърториал / статия** | 392 | **27%** | 27 (7%) | **5** |
| Карусел / каталог | 25 | 2% | 0 | 0 |
| Вероятно видео (слаб сигнал) | 89 | 6% | 18 (20%) | 14 |
| Квиз (линк към квиз) | 71 | 5% | 0 | 0 |
| Неясно (вкл. 44 празни заглавия и 2 DCO) | 574 | 40% | 84 (15%) | 57 |
| **Общо** | **1 438** | | | **135** |

**Какво доминира:**
- **По брой пуснати реклами водят адвърториалите** (27%), но рядко оцеляват: само 5 от 392 въртят 30+ дни (Ethnica Herbs 135 дни, Bany RO, Михаил Михов 94 дни).
- **По оцеляване водят статиките.** От 135-те реклами на 30+ дни 59 (44%) са с „оферта“ или „брой отзиви“ в заглавието. Те обаче идват само от 6 страници: HarmonyHug 24 („Над 8 000 положителни отзива“, 106 дни), Здравословен живот след 40 19 („1 закупен = 1 БЕЗПЛАТНО“, 79.5 дни), Chillama 9, Adeline Mercier (PL) 5, GreenActive 1, herbalnatura 1. Пет от тях са в BG: **в България офертата и броят отзиви на статична карта оцеляват най-дълго.**
- **BG срещу света:** в BG статика 24% и адвърториал 22%; извън BG статика 18% и адвърториал 29%. Статиките са най-много в DE (46% от 76), NL (38%) и PL (6 от 11). Адвърториалите са най-много в AU (55%), FR (39%), GB (36%) и US (31%). IT: 14 от 50 са каталози-карусели (WeightWorld, Spiritual Green).
- **Обемни тестове на визии (F-014):** 585 реда (41%) са в 53 партиди от 37 страници, по 5+ реклами с едно заглавие за 10 минути. Значи текстът е един, а се тестват визиите. По заглавие: неясно 214, адвърториал 177, статика 138, квиз 35.
- **Видеото не се вижда от заглавията.** Каква част от пазара е видео, няма данни. Отключва се с Brandsearch или със скрийншоти от собственика или Боян.

---

## Източници (световни разбивки)

- Motion, Creative Benchmarks 2026, топ визуални формати (578 750 креатива, IX.2025–I.2026, вкл. Black Friday): [top-visual-formats](https://motionapp.com/library/research/creative-benchmarks-2026/top-visual-formats) · по вертикали: [visual-formats-by-vertical](https://motionapp.com/library/research/creative-benchmarks-2026/visual-formats-by-vertical) · hit rate по формати: [thumbstop-pulse](https://motionapp.com/thumbstop-pulse/creative-benchmarks-2026/) · обобщение: [Foxwell Digital](https://www.foxwelldigital.com/blog/motion-creative-benchmarks-2026-8-key-takeaways)
- Motion, страници на формати: [Letter](https://motionapp.com/library/formats/letter) · [Post It](https://motionapp.com/library/formats/post-it) · [Notes App](https://motionapp.com/library/formats/notes-app) · [Text Message](https://motionapp.com/library/formats/text-message) · [Social Comments](https://motionapp.com/library/formats/social-comments) · [Us Vs Them](https://motionapp.com/library/formats/us-vs-them) · [Split Screen](https://motionapp.com/library/formats/split-screen) · [Podcast](https://motionapp.com/library/formats/podcast) · [Infographic](https://motionapp.com/library/formats/infographic) · [Listicle](https://motionapp.com/library/formats/listicle) · [Animation](https://motionapp.com/library/formats/animation) · [Native Search](https://motionapp.com/library/formats/native-search) · [Stitch](https://motionapp.com/library/formats/stitch) · [Reaction video](https://motionapp.com/library/formats/reaction-video) · [UGC overlay](https://motionapp.com/library/formats/ugc-overlay) · [Street Interview](https://motionapp.com/library/formats/street-interview) (03.10, 08:59) · [Headline](https://motionapp.com/library/formats/headline) · [Demo](https://motionapp.com/library/formats/demo) · [How To](https://motionapp.com/library/formats/how-to) (03.10) · марка в нашата ниша: [Happy Mammoth](https://motionapp.com/library/happy-mammoth) (хормони и тегло при жени 40+: ≈1 000 активни реклами, ≈116 нови на седмица)
- Curtis Howland: [The DTC static ad system, 67 852 реклами от 106 марки](https://newsletter.curtishowland.com/p/the-dtc-static-ad-system-what-67852) (статиките са 55.6% от всички реклами, 64.8% при DTC) · [DTC Meta Ads Tier List](https://newsletter.curtishowland.com/p/the-dtc-meta-ads-tier-list)
- [Superscale: static ads 2026](https://superscale.ai/learn/static-ads/) · [Adrio: 7 static формата](https://adrio.ai/blog/best-meta-ad-formats) · [Adlibrary: 8 DTC формата](https://adlibrary.com/posts/best-dtc-meta-ads-examples-2026) · [Adlibrary: 10 карусела](https://adlibrary.com/posts/carousel-ad-examples-2026) · [AdRiseLab: анатомия на карусела](https://adriselab.com/blog/meta-carousel-ads-anatomy-2026) · [Segwise: 5 формата](https://segwise.ai/blog/100m-meta-ads-5-formats-dtc)
- [ADM: post-it реклами](https://www.accelerateddigitalmedia.com/insights/using-post-it-graphics-in-paid-social-ads/) · [NextAfter: тест на notes app](https://www.nextafter.com/experiments/how-using-an-iphone-notes-app-style-of-facebook-ad-creative-impact-clicks/) · [RocketShip HQ: текст във видео](https://www.rocketshiphq.com/text-overlays-video-ads-mobile/) · [The Performers: 40 000 реклами от 11 DTC марки](https://www.blog.theperformers.io/p/9-figure-dtc-report)
- AI и skeleton: [Higgsfield: AI аватари срещу UGC](https://higgsfield.ai/blog/ai-avatars-vs-ugc-creators-2026) · [Cinerads: Meta и AI хора в реклами](https://www.cinerads.com/blog/ai-ugc-facebook-ad-policy) · [AITuber: skeleton канал, 119 млн. гледания (органично)](https://aituber.app/blog/skeleton-channel-case-study-million-views/) · [Hustler Marketing: green screen](https://www.hustlermarketing.com/types-of-ugc-ads-the-formats-that-work-for-ecommerce-brands-2026/)
- Брандове с човек отпред (03.10, 08:59): [Brandsearch: 523 реклами на 30+ дни, при добавките founder-led UGC е 67% от оцелелите видеа](https://brandsearch.co/blog/winning-meta-ad-patterns-2026)
- Диалог с двама (03.10, 11:11): Motion [Skit](https://motionapp.com/library/formats/skit) (Liven 3K, Rise Science 2K, WalkFit 1K) · [WalkFit](https://motionapp.com/library/walkfit-daily-walking-plan) (жени 50+, 426 активни, ≈192 нови на седмица) · [Duet](https://motionapp.com/library/formats/duet) (MoonBrew 82, Primal Queen 42) · [Comment Response](https://motionapp.com/library/formats/comment-response) (5 марки добавки: Arrae, Goli, Create, Transparent Labs, Dose) · [Podcast](https://motionapp.com/library/formats/podcast) (структура „единият разказва, другият пита“)
- Улична анкета (03.10, 19:11): Motion [Street Interview](https://motionapp.com/library/formats/street-interview) (18 реклами, 17 марки, от тях 4 в здраве и добавки; hit rate няма) · AU контекст: [AHCRA: TGA свали 3 000+ реклами за отслабване](https://www.ahcra.com.au/blog/tga-weight-loss-ads-removed-compliance/)
- Двама в кадъра + реакция (03.10, 23:11): Motion [Reaction video](https://motionapp.com/library/formats/reaction-video) (определение с „двама приятели в паркирана кола“; Hismile 703, Zeely 387, BOTB 162, Mixtiles 118) · US марки: [Bioma](https://motionapp.com/library/bioma-health) (459 активни, ≈111 нови на седмица; двойка и подкаст) · [Lemme](https://motionapp.com/library/lemme) (266 активни, ≈62 нови на седмица; без формати с двама) · [Adlibrary: добавки](https://adlibrary.com/posts/best-supplement-ads-examples) (AG1, Ritual, Seed въртят 45–90+ дни; пример с двама няма)
- Разходка с двама (04.10, 03:11): Motion [WalkFit](https://motionapp.com/library/walkfit-daily-walking-plan) („two-shot walking sequences“ в рекламите с двама; Demo 18%, Before and After 12%, Expert Explainer 9%; данните са отпреди ≈4 месеца) · Motion [Scaling UGC Ads Post-Andromeda](https://motionapp.com/library/talk/scaling-ugc-ads-post-andromeda-one-winner-many-formats/) (Ready Set, VI.2026: „talent refresh“, нова двойка в същия кадър) · Motion [индекс на формати](https://motionapp.com/library/formats) (с двама в разговор са само Street Interview, Duet, Stitch и Comment Response) · PL: [Allegro: berberyna plastry](https://allegro.pl/listing?string=berberyna+plastry) (моринга + берберин + NAD+, микроигли, 29.90–45 zł; ревюта „по-малки, отколкото очаквах“; по резюмето на търсачката, страницата не е отворена)
- GB (04.10, 07:11): Motion [Your Heights](https://motionapp.com/library/your-heights) (343 активни, ≈109 нови на седмица; основателят интервюира клиент) · [Spacegoods](https://motionapp.com/library/spacegoods) (272, ≈112; „Menobelly?“) · [Kind Patches](https://motionapp.com/library/kind-patches) (2 000, ≈168) · [Vitabiotics](https://motionapp.com/library/vitabiotics) (760, ≈75; „цената първа“ 35%) · [Happy Mammoth EU](https://motionapp.com/library/happy-mammoth-eu) (988, ≈106; две жени на диван) · [Join ZOE](https://motionapp.com/library/join-zoe) (155, ≈44) · [Wild Nutrition](https://motionapp.com/library/wild-nutrition) (594, ≈39) · формати [Checkout Mockup](https://motionapp.com/library/formats/checkout-mockup) · [Phone Call Mockup](https://motionapp.com/library/formats/phone-call-mockup) · [Social Proof Mashup](https://motionapp.com/library/formats/social-proof-mashup) · [индекс, 113 формата](https://motionapp.com/library/formats/) · ASA: [Kind Patches „GLP-1 Patch“ (III.2026)](https://www.asa.org.uk/rulings/kind-patches-ltd-a26-1333913-kind-patches-ltd.html) · [GuLP-1 (V.2026)](https://www.asa.org.uk/rulings/glp-1-pro-ltd-a25-1317723-glp-1-pro-ltd.html) · [Minerva „without HRT“](https://www.asa.org.uk/rulings/minerva-wellness-ltd-a25-1313816-minerva-wellness-ltd.html) · [Nova](https://www.asa.org.uk/rulings/nova-relief-a25-1313821-nova-relief.html) · [NutraIngredients: AI мониторинг на ASA](https://www.nutraingredients.com/Article/2026/03/26/asa-puts-menopause-claims-back-under-scrutiny-after-ai-review/) · микроиглите в GB: [форум на Diabetes UK](https://forum.diabetes.org.uk/threads/new-scam-alert-berberine-patches.122638/) · [MalwareTips](https://malwaretips.com/blogs/berberine-x-nad-patch/) · дълголетие: [Evolut, 500 топ реклами на добавки](https://evolutagency.com/supplement-marketing-2026/) · доставчик: [Influee, podcast-style](https://influee.co/landing/podcast-style-ads)
- DE (04.10, 11:11, само уеб): публичните страници на Brandsearch (без вход; брой активни реклами и разход в ЕС по държави): [MORE Nutrition](https://brandsearch.co/brands/morenutrition.de) (1 084 активни, €2.7M в DE) · [XbyX](https://brandsearch.co/brands/xbyx.de) (146, €908.3K в DE) · [VitaMoment](https://brandsearch.co/brands/vitamoment.de) (28, €247.6K) · [FEMNA](https://brandsearch.co/brands/femna.de) (11, €26.3K) · [Happy Mammoth](https://brandsearch.co/brands/happymammoth.com) (DE 5%) · [Kind Patches](https://brandsearch.co/brands/kindpatches.com) (DE под 5%). Motion: [MORE Nutrition](https://motionapp.com/library/more-nutrition) · [Bears with Benefits](https://motionapp.com/library/bears-with-benefits) · [ESN](https://motionapp.com/library/esn) · [YAZIO](https://motionapp.com/library/yazio). Публичен разбор: [webnetz, 13.02.2026: социалното съдържание на 20+ немски марки добавки](https://www.webnetz.de/know-how/blog/milliardenmarkt-nahrungsergaenzungsmittel-wie-wirkt-der-social-content-von-doppelherz-orthomol-more-nutrition-co-auf-user) · [ÖIAT, XII.2025: 4 632 проблемни реклами в Meta, 75% към хора над 45](https://research.oiat.at/fileadmin/Research/Dokumente/Safe-NEM-Bericht.pdf)
- По-възрастна аудитория (03.10): [CDMG: Marketing to Seniors, 44 съвета от директния маркетинг](https://cdmginc.com/2026/09/09/marketing-to-seniors-46-surprising-advertising-insights/) (яснота, едър шрифт, без обърнат текст; твърдения на автора)

Числата на доставчици (Segwise „60–70% от конверсиите“, AdRiseLab „+27% CTR“) са твърдения на самите блогове. Ползват се като посока, не като доказателство.

---

## Карти

### VF-001 „Цената първа“ (offer-first банер)
**Какво е визуално:** една статична карта 4:5. Горната третина е голям ценови блок на жълта лента. В средата е истинският пакет и ръка с една лепенка. Долу има ред с 3 иконки. Без лице и без история.
**Къде и защо скалира:**
- Motion: Offer-First Banner е 21.9% от креативите, но взима 29.3% от разхода (spend use 1.3), hit rate 8.6%. Това е най-големият дял от разхода в таблицата на Motion ([източник](https://motionapp.com/library/research/creative-benchmarks-2026/top-visual-formats)). Внимание: в периода е Black Friday.
- Памет: 33 статики с оферта въртят 30+ дни. BG: Здравословен живот след 40 „1 закупен = 1 БЕЗПЛАТНО“ **79.5 дни** (27549902074662944), 19 реклами на 30+ дни. GreenActive BG „До -40% САМО тази седмица“ 69.9 дни (1697117554892076). Chillama „✅ Купи 1 и Вземи 1 Безплатно“ 43 дни (2150479305848676). PL: Adeline Mercier 41.6 дни.
- Лаб: A9 с цена в първата секунда беше 41.1 срещу 30.6 за S2 (07:11), но не се повтори (29.5).
- **ES, 03.10 (обновено):** Velia Parches (лепенки) пусна 30 нови статики с оферта за 6 дни, на 4 партиди: „1 + 1 GRATIS“ ×9 на 27.09 и ×6 на 01.10, после „2 + 2 GRATIS“ ×9 на 02.10 и ×6 на 02.10 вечерта ([2272718843572923](https://www.facebook.com/ads/library/?id=2272718843572923)). Офертата се вдига вместо визията. „2 + 2 Gratis“ е и на испанската страница на Kind Patches ([kindpatches.com](https://kindpatches.com/pages/glplpv4-es)). Kind Patches: Offer-First Banner е 12% от ≈2 000 активни реклами ([Motion](https://motionapp.com/library/kind-patches)). **За нас:** по-голямата отстъпка е решение на собственика, не ген за лабораторията.

**Адаптация за FitPatches** (ъгъл: прозрачна цена + плащане при доставка):
- Горе, голямо: „14.99 € + доставка.“ / „Плащаш, като го получиш.“
- Средата: истинският пакет на кухненска маса, ръка държи 1 лепенка.
- Долу: „30 лепенки · берберин, канела и нар · 1 сутрин на рамото · не е хапче“.
- Вариант B (за AOV): „3+1 подарък · 39.99 € · безплатна доставка · около 0.33 € на ден“ на един ред, + „Плащаш при доставка“.
- Заглавие: „Колко струва? 14.99 € + доставка.“

**Продукция:** Canva + истинска снимка на пакета (или фон от Kie gptimage2, текстът се слага в Canva). Ниска.
**Риск в Meta:** нисък. Цената винаги с доставката. Без таймери и „само днес“. Без „без скрити такси“, докато ops не потвърди дали Еконт взима такса за наложен платеж. Вариант B е блокиран преди Meta, докато продуктите в Shopify не отговарят на 3+1.
**Статус:** нов

---

### VF-002 „Стек от доверие“ (F-010 като статична карта)
**Какво е визуално:** статична карта с пакета вляво и 4 реда вдясно. Всеки ред е иконка + 3–4 думи, разделени с „|“ или един под друг. Същият стек може да е заглавието на линка.
**Къде и защо скалира:**
- Памет: FreshHaut (DE) пусна 14 стека за 25 ч (5 варианта: „произведено в Германия · натурални съставки · 60/180 дни гаранция · бърза доставка“; 1098944869348229, 2144137146178980). Bany RO „Купена от хиляди румънци ⭐ Плащане при доставка 💰 Бърза доставка 🚚“ върти 25.4 дни (38140466842266432). Dr. Evelina Martin (BG) прави същото с „Плащане при доставка • Изпращане до 24 часа“ (1084115891132496). Гаранцията като заглавие: Chillama „✅ 90 дни гаранция“ 35.6 дни (1790852648576632). С това са 3+ марки, затова стекът е отделна карта (виж бележката във F-010).
- **RO, 04.10 (уеб):** стекът е и на сайта на Bany RO: „Livrare 1–3 zile lucrătoare · Plată la livrare · Retur 14 zile · Comandă rapidă, fără cont necesar · Mii de comenzi livrate cu succes“ ([bany.ro](https://bany.ro/)). Нов ред за нас: **„Бърза поръчка: без регистрация, без карта“**. Вярно е за формата EasySell само ако cro-specialist потвърди, че не иска акаунт. „Хиляди поръчки“ не взимаме без проверим брой.
- Свят: „Benefit-Stack Static“ при [Adlibrary](https://adlibrary.com/posts/best-dtc-meta-ads-examples-2026) и „Offer Stack“ при [Adrio](https://adrio.ai/blog/best-meta-ad-formats). Числа няма.
- **ES, 03.10 (обновено): стекът с наложен платеж на първо място оцелява 21–25 дни при лепенките.** Dra. Laura Martínez (2 страници с едно име): „📦 Pago contra reembolso | ✅ Garantía de devolución de 180 días | 🇪🇸Fabricado en España | 🌿 Ingredientes 100% naturales“, 24.5 дни ([2023055651683124](https://www.facebook.com/ads/library/?id=2023055651683124)) и нова на 27.09 ([1402544591369134](https://www.facebook.com/ads/library/?id=1402544591369134)). LuzMar: „Pago contra entrega | Envío desde almacén local | Entrega en 2-4 días hábiles | Garantía…180 días“, 20.8 дни ([1577209623900448](https://www.facebook.com/ads/library/?id=1577209623900448)). И двете са от заявката „parches adelgazar“, която има само 13 активни реклами. Значи в ES стекът е 3 от 13. **Наложеният платеж е първият ред и при двете**, както в нашата адаптация. „Dra.“ е лекарска страница без доказан лекар (compliance-rules, ред 15), а „100%“ и листото-значка са забранени при нас (ред 74).

**Адаптация за FitPatches:**
- 4 реда: „Плащаш при доставка | Берберин, канела и нар | Гаранция [ГАРАНЦИЯ: 60 или 30?] дни | 3+1 подарък · 39.99 € · безплатна доставка“.
- Докато собственикът не реши за гаранцията, третият ред е „1 лепенка сутрин, не е хапче“.
- Визия: пакетът на бял плот, иконки с тънка линия (камионче, лист, календар, пакет).

**Продукция:** Canva, 30 мин. Ниска.
**Риск в Meta:** нисък. Без печати, щитове, медали и „сертифицирано“ (2005/29, Прил. I т.2 и т.4). Иконките не трябва да приличат на печат. Без „хиляди клиенти“, докато няма проверим брой. Гаранцията се пише само след решението на собственика и само ако условията са на PDP.
**Статус:** нов (пълната версия чака решението 60/30)

---

### VF-003 Карта с цитат или отзив
**Какво е визуално:** голям цитат в кавички на кремав фон. Под него е малка снимка на пакета и подпис. Без звезди, ако няма проверим източник.
**Къде и защо скалира:**
- Motion: Testimonial е 13.3% от креативите и 13.3% от разхода, hit rate 6.5% ([източник](https://motionapp.com/library/research/creative-benchmarks-2026/top-visual-formats)). Curtis Howland: „social proof“ статиките са най-подходящи за добавки и здраве ([източник](https://newsletter.curtishowland.com/p/the-dtc-static-ad-system-what-67852)).
- Памет: 26 карти с рейтинг или брой отзиви въртят 30+ дни. HarmonyHug „🎖️ Над 8 000 положителни отзива“ **106.4 дни** (1337690151666478), Chillama същото заглавие 92.8 дни (1004641399226552). FR: Maya Slim „4,8/5 в Trustpilot“ 18.3 дни. NL: Overgang Tips „4,9/5 | 31 847 отзива“ ×17 в една партида.

**Адаптация за FitPatches:**
- **Реална версия** (когато в `voc.md` има отзив със съгласие): точният цитат, име и първа буква на фамилията, „отзив, публикуван със съгласие“.
- **Драматизация** (сега, само за симулацията): цитат за покупката, не за тялото: „Платих чак като го взех от Еконт. Така поне не рисках.“ Подпис „Мария · драматизация“, без снимка на лице и без звезди.

**Продукция:** Canva. Ниска.
**Риск в Meta:** среден до висок. Измислен отзив е нарушение (Омнибус 2019/2161), затова драматизацията не изглежда като отзив: без звезди, без „отзив“, без профилна снимка. „4.4 · 1012 Ревюта“ от PDP не се ползва, докато не стане проверимо.
**Статус:** нов (реалната версия чака CB-007)

---

### VF-004 Писмо (letter)
**Какво е визуално:** статична снимка на лист, написан на ръка или напечатан, на кухненската маса. Или бавно видео, в което камерата върви по листа. Обръщение, 6–8 кратки реда, подпис.
**Къде и защо скалира:**
- Motion: Letter има hit rate 10.83% и взима ≈1.7 пъти повече разход от дела си в креативите. В Health & Wellness е №2 по spend use ([hit rate](https://motionapp.com/thumbstop-pulse/creative-benchmarks-2026/), [по вертикали](https://motionapp.com/library/research/creative-benchmarks-2026/visual-formats-by-vertical)). Над 100 марки: Liven, Health Boost, BetterMe, Calm, Noom ([източник](https://motionapp.com/library/formats/letter)).
- В нашата памет е близо до F-012 „До жената, която…“ (15 страници в 5 държави).

**Адаптация за FitPatches** (ъгъл: вината и „не е мързел“):
„До жената, която всяка вечер се обвинява за едно и също.
Която прави всичко за другите и най-малко прощава на себе си.
Не е мързел. Не е характер. Много жени минават през същото.

Не обещаваме чудо. Направихме нещо просто за сутрините: 1 лепенка на рамото. Берберин, канела и нар. Не е хапче.
14.99 € + доставка. Плащаш при доставка.
— Екипът на FitPatches“
- Най-долу, дребно: „Не замества разнообразното хранене и движението.“

**Продукция:** истински лист, написан на ръка (Боян) и сниман на телефон, или Canva с ръкописен шрифт. Ниска.
**Риск в Meta:** нисък до среден. Подпис само от истински екип и пуск само от страница FitPatches (правило в compliance-rules). Без измислен „основател“. В трето лице се описват поведение и чувства, без тегло, болест и възраст. „Не е мързел“ не стои непосредствено до лепенката: между тях е „Не обещаваме чудо.“
**Статус:** нов

---

### VF-005 Голям текст без снимка (native)
**Какво е визуално:** едноцветен фон и 2–3 реда с много голям шрифт, като статус в профил. Само малко лого в ъгъла. Цялото предложение е в текста под рекламата.
**Къде и защо скалира:**
- Motion: Text only има hit rate 11.6%. По-високо от него е само Stitch (12.50) в Health & Wellness. Product image with text е 8.75% ([източник](https://motionapp.com/thumbstop-pulse/creative-benchmarks-2026/)). Изводът на Motion: текстовите реклами, снимките на продукт с текст и простите GIF-ове са сред най-честите победители ([Foxwell](https://www.foxwelldigital.com/blog/motion-creative-benchmarks-2026-8-key-takeaways)).
- Памет: визиите не се виждат, данни няма.

**Адаптация за FitPatches:**
- Вариант „вина“: тъмнозелен фон. „Не е мързел.“ / „Не е характер.“ / по-дребно: „5 неща, които много жени забелязват с годините.“
- Вариант „цена“: кремав фон. „14.99 € + доставка.“ / „Плащаш, като го получиш.“ / по-дребно: „30 лепенки с берберин, канела и нар.“
- Текст под рекламата: тялото на A13 или S2 (без промяна).

**Продукция:** Canva, минути. Ниска.
**Риск в Meta:** нисък. Без 2-ро лице към зрителката като голям надпис („Не си виновна“, „Спри да се кориш“; ред 49 в compliance-rules). Безличното „Човек без воля не почва сто пъти.“ е одобрено и като голям надпис.
**Статус:** нов

---

### VF-006 Скрийншот от бележника в телефона (notes app)
**Какво е визуално:** статична картина на екран с бележка: заглавие, 3–5 реда с отметки, понякога емоджи. За да не се слее с бялата лента, се снима телефон в ръка над кухненската маса, бележката е в тъмен режим.
**Къде и защо скалира:**
- Motion: над 100 марки ползват формата. Най-много реклами имат Reframe (393), Motion (261) и Headway (216); сред тях са Happy Mammoth, Noom, Calm, Orgain и Spacegoods ([източник](https://motionapp.com/library/formats/notes-app)). В Health & Wellness „social post mockup“ е №1 по spend use ([източник](https://motionapp.com/library/research/creative-benchmarks-2026/visual-formats-by-vertical)).
- **Против:** NextAfter има 2 контролирани теста, в които стилът „бележник“ губи от контролата. Причината е, че белият фон се слива с лентата ([източник](https://www.nextafter.com/experiments/how-using-an-iphone-notes-app-style-of-facebook-ad-creative-impact-clicks/)). Затова при нас е тъмен режим и телефон в ръка.

**Адаптация за FitPatches** (сутрешен списък, без вина към лепенката):
„Сутрин, 7:10
☑ кафе
☑ обяд за малката
☑ 1 лепенка на рамото (берберин, канела, нар)
☑ без укори за вчера“
- Под телефона: „FitPatches · 30 лепенки · 14.99 € + доставка · плащаш при доставка“.
- Надпис „Драматизация“ в ъгъла (личната бележка е на персона).

**Продукция:** макет на бележка в Canva или Figma, без логото и името на Apple + Kie gptimage2 за ръка с телефон и празен екран. Екранът се слага отделно. Ниска.
**Риск в Meta:** нисък. „Сутрин — без укори“ е одобрената формулировка (ред 48). Без „3/3“ и печати. Без търговски марки на приложения.
**Статус:** нов

---

### VF-007 Разопаковане без лице (unboxing)
**Какво е визуално:** видео 9:16, 12–15 сек, отгоре, само ръце, ASMR звук. Сивият плик от Еконт на масата → ръцете го скъсват → пакетът FitPatches → отваря се → 30 лепенки → една на пръста. На всеки кадър има кратък надпис.
**Къде и защо скалира:**
- Motion: Unboxing има hit rate 9.8% и spend use 1.3. Заедно с Celebrity е формат, който „надскача ефективността си“ ([източник](https://motionapp.com/library/research/creative-benchmarks-2026/top-visual-formats)). В Health & Wellness е в топ 3 по hit rate ([източник](https://motionapp.com/library/research/creative-benchmarks-2026/visual-formats-by-vertical)).
- Лаб: „какво точно има вътре“ (A4) държи 30.7 и 31.2, а четенето на етикета печели скептичните (P05, P08, P02, P13).

**Адаптация за FitPatches** (ъгъл: „измама ли е? ето какво пристига“):
- 0–3 с: пликът от Еконт, ръце. Надпис: „Поръчах с плащане при доставка. Ето какво пристигна.“
- 3–7 с: пакетът. Надпис: „1 пакет · 30 лепенки“.
- 7–10 с: етикетът отблизо. Надпис: „берберин · канела · нар“.
- 10–13 с: една лепенка на пръста. Надпис: „1 сутрин · на рамото · не е хапче“.
- 13–15 с: пакетът на масата. Надпис: „14.99 € + доставка · плащаш при доставка“.
- Без глас или с 1 изречение. Надпис „Драматизация“ (личната поръчка е на персона).

**Продукция:** най-евтино е истинско видео с телефон и истински пакет (Боян или собственикът). Иначе Kling или Veo от референтен кадър, текстът в монтажа. Ниска до средна.
**Риск в Meta:** нисък. Етикетът трябва да е истинският (съставките да се сверят дословно). Без лепенка на корема.
**Статус:** нов

---

### VF-008 Ръкописно листче, тетрадка, post-it
**Какво е визуално:** снимка с телефон. Жълто листче, залепено на пакета или на хладилника, или отворена тетрадка на кухненската маса. Текст на ръка с маркер или химикал.
**Къде и защо скалира:**
- Motion: Post It взима ≈1.3 пъти разход спрямо обема си. Над 100 марки го ползват, сред тях Happy Mammoth, Happy Mammoth EU, Nutrition Geeks и Norse Organics ([източник](https://motionapp.com/library/formats/post-it)). Близките формати: Sign (надпис в кадъра) 7.86%, Unconventional Text Placement (текст върху предмет) 9.63%, Letter 10.83% ([източник](https://motionapp.com/thumbstop-pulse/creative-benchmarks-2026/)).
- ADM тества post-it реклами при голяма марка за здраве и красота: +26% ROAS и −23% цена на поръчка спрямо средното за акаунта ([източник](https://www.accelerateddigitalmedia.com/insights/using-post-it-graphics-in-paid-social-ads/)).

**Адаптация за FitPatches:**
- Post-it на пакета: „1 сутрин. На рамото. Не е хапче.“
- Post-it на хладилника, до пакета: „14.99 € + доставка. Плащам, като дойде.“
- Тетрадка: F-011 (брифът за 23:11 по-долу).

**Продукция:** истинска снимка с истински почерк. AI изкривява кирилицата, затова се пише на ръка или с ръкописен шрифт в Canva. Ниска.
**Риск в Meta:** нисък. „Отметнах и трите“ на ръка е ОК, а „3 от 3 ✓“ като отделен надпис не е (ред 41).
**Статус:** **за 23:11** (F-011)

---

### VF-009 Карусел-чеклист (A13 в 5 карти)
**Какво е визуално:** карусел от 5 карти 4:5: hook → списък с отметки → вината пада → продуктът → цена и плащане при доставка. Пълният текст е в брифа за 23:11.
**Къде и защо скалира:**
- Happy Mammoth (хормони и тегло при жени 40+): Listicle е 13% от ≈1 000 активни реклами, а Headline 12%. Пускат ≈116 нови на седмица; един от hook-овете им е „5 хормонални червени флага“ ([източник](https://motionapp.com/library/happy-mammoth)).
- Motion: Listicle има hit rate 5.3%. Post It се комбинира с Listicle в 25% от случаите ([източник](https://motionapp.com/library/formats/post-it)). Curtis Howland: листикълът е най-подходящ за добавки ([източник](https://newsletter.curtishowland.com/p/the-dtc-static-ad-system-what-67852)).
- Карусел: AdRiseLab в собствено проучване на 320 реклами отчита +27% CTR за 5 карти спрямо единична снимка, с ред hook → проблем → решение → доказателство → CTA ([източник](https://adriselab.com/blog/meta-carousel-ads-anatomy-2026)).
- Лаб: A13 е №1 на 15:11 (36.8, 75% срещу S2) и №3–4 на 19:11 (33.2 и 33.0).

**Продукция:** Canva, 1 час, без кредити. Ниска.
**Риск в Meta:** нисък. Без „колко от тях имаш?“, без „ти“. „С годините тялото работи по друг начин“ не влиза в карусела, защото там всеки ред е надпис (ред 39 и 45).
**Статус:** **за 23:11** (A13)

---

### VF-010 „Ние срещу тях“ без марки (рутина, не ефект)
**Какво е визуално:** статична карта с 2 колони: „Капсули“ (сива, обща иконка) срещу пакета FitPatches. 2–3 реда сравнение, само за навика и удобството.
**Къде и защо скалира:**
- Motion: Us vs them има hit rate 6.52% ([източник](https://motionapp.com/thumbstop-pulse/creative-benchmarks-2026/)). Ползват го Shapermint, Dr. Squatch, Loop и BURGA ([източник](https://motionapp.com/library/formats/us-vs-them)). Curtis Howland: Ridge е изградила марката си върху формата и никога не е спирала да го пуска ([източник](https://newsletter.curtishowland.com/p/the-dtc-static-ad-system-what-67852)).
- **RO, 04.10 (уеб): 4 марки сравняват с хапчетата.** Plasturel (румънска марка, 79 лей) има на продуктовата страница таблица „лепенки срещу хапчета“ (постепенно освобождаване, стомахът, дискретност) и инфографика в 3 стъпки ([plasturel.ro](https://plasturel.ro/)). Kenku Romania има „GLP-1 Patches vs. Alte Mărci“ и „Control fără pastile și fără injecții“, преведени от испански ([kenkuromania.com](https://kenkuromania.com/products/parches-glp-1-kit-30-parches)). Към тях са Bany „Nu toată lumea…“ (40.6 дни) и Tinyshopstore (84.8 дни). При нас редът за стомаха и „без инжекции“ са забранени (ред 20, 29), остава само навикът.
- Памет: 92 реда с етикет „сравнение“. Hormone Health Lab „Skip the injections - 50% OFF“ ×32 в партида (US). Bany RO „Не всеки иска хапчета, добавки или сложни режими“ ×22 в партида, 40 дни (F-003). Визиите са неясни.

**Адаптация за FitPatches:**

| | Капсули | FitPatches |
|---|---|---|
| Как се приема | гълта се, с вода | лепва се на рамото |
| Кога | по схемата на опаковката | 1 сутрин |

- Заглавие на картата: „Една сутрешна стъпка. Не още едно хапче.“ Под нея: „берберин, канела и нар · 14.99 € + доставка · плащаш при доставка“.

**Продукция:** Canva. Ниска.
**Риск в Meta:** среден. Без марки и без „по-добре усвоимо“, „не минава през стомаха“, „през кожата“ (ред 20). Без „вместо“ (внушение, че замества лекарство), без колона „инжекции“ и без „без инжекции“ като свойство (ред 29). Сравнението е само за навика. Твърдението за капсулите трябва да е вярно за категорията, иначе редът отпада.
**Статус:** нов (свързан с CB-014)

---

### VF-011 Скрийншот от чат
**Какво е визуално:** екран с разговор: сиви балончета вляво (приятелка пита), цветни вдясно (Мария отговаря). Без логото на приложението, без профилни снимки на хора, с име и инициал. Пълният текст е в брифа за 23:11.
**Къде и защо скалира:**
- Motion: Text Message ползват 20 марки, сред тях добавки и здраве: AG1, Happy Mammoth (с „2.8 милиона жени“), Magic Mind, Perelel, Create Wellness, Hims, BetterHelp ([източник](https://motionapp.com/library/formats/text-message)). „Social post mockup“ е №1 по spend use в Health & Wellness.
- Curtis Howland: „UGC-native / screenshot“ заобикаля „филтъра за реклами“ ([източник](https://newsletter.curtishowland.com/p/the-dtc-static-ad-system-what-67852)).
- Лаб: диалогът със скептичната приятелка S3 е №1 на 08:59 (36.3, 66% срещу S2): възраженията от друг човек правят рекламата разговор.

**Продукция:** макет в Figma или Canva. Ниска.
**Риск в Meta:** среден. Двете жени са измислени, затова има надпис „Драматизация“. Не прилича на коментари във Facebook (ред 27) и не е „отзив“. Всичко, което Мария казва, е твърдение на FitPatches.
**Статус:** **за 23:11** (S2)

---

### VF-012 Split screen
**Какво е визуално:** видео 9:16, разделено хоризонтално. Горе е говорещият кадър (наличният S2), долу големи карти с въпроса и отговора. Друг вариант: две сутрини една до друга, „капсули, вода, аларма“ срещу „1 лепенка, кафе“, без тяло.
**Къде и защо скалира:** Motion: 20+ марки и 4K+ уникални реклами от топ марки, сред тях Health Insider, Health Boost, Shapermint, Headway ([източник](https://motionapp.com/library/formats/split-screen)). Split Screen е в топ листата по hit rate, където диапазонът е ≈5–9% ([източник](https://motionapp.com/library/research/creative-benchmarks-2026/top-visual-formats)).
**Адаптация за FitPatches:** горе е S2 („Колко струва?“), долу е картата „14.99 € + доставка · 30 лепенки · плащаш при доставка“. Картите стоят по 2.5 сек на 10 думи (4 думи в секунда, [RocketShip HQ](https://www.rocketshiphq.com/text-overlays-video-ads-mobile/)). Монтаж на наличните кадри.
**Продукция:** CapCut. Средна.
**Риск в Meta:** нисък. **Никога** две тела или „преди/сега“ с фигура. Само въпроси и рутина.
**Статус:** нов

---

### VF-013 Статик „проблем → решение“
**Какво е визуално:** 40% горе е проблемът с голям текст, в средата е продуктът в употреба, долу е доказателството (етикетът) и CTA.
**Къде и защо скалира:** Superscale и Adrio го сочат като най-подходящ за добавки и студен трафик ([Superscale](https://superscale.ai/learn/static-ads/), [Adrio](https://adrio.ai/blog/best-meta-ad-formats)). Problem Agitation е в топ листата на Motion по hit rate. Памет: F-003 „без хапчета и сложни режими“. Bany RO върти 40 дни, Tinyshopstore „Fara pastile si diete“ 84.8 дни (1193299577202524). Визиите са неясни.
**Адаптация за FitPatches** (проблемът е сложността, не тялото):
- Горе: „Още едно хапче. Още една аларма. Още едно правило.“
- Средата: ръка лепва лепенка на рамото, под пуловер.
- Долу: „1 лепенка сутрин · берберин, канела и нар · 14.99 € + доставка · плащаш при доставка“.
**Продукция:** Canva + кадър от S2 (лепването) или Kie gptimage2. Ниска.
**Риск в Meta:** нисък. Проблемът никога не е тяло, кантар или „не мога да сваля“. Без „лесно“ без обект (ред 32).
**Статус:** нов

---

### VF-014 Подкаст клип
**Какво е визуално:** две жени на кухненската маса с 2 микрофона. Кадри през рамо и отблизо, субтитри, долен надпис „Разговор за лепенките · Драматизация“.
**Къде и защо скалира:** Motion: 12 марки, сред тях Happy Mammoth, Primal Queen, Magic Mind, hims и Huel. Числа за ефект няма ([източник](https://motionapp.com/library/formats/podcast)). Stitch (12.50) и Reaction video (11.24) водят по hit rate в Health & Wellness, а те също са „разговор“.
**Адаптация за FitPatches:** скептичната приятелка от S3 пита, Мария отговаря. 30 сек: „Това не е ли поредната измама?“ → „Платих като го взех.“ → „Какво има вътре?“ → „Берберин, канела, нар.“ → „Колко?“ → „14.99 € + доставка.“
**Продукция:** две говорещи лица с lip sync е трудно в Higgsfield и Kling, по-добре истински запис. Висока.
**Риск в Meta:** нисък до среден. Без име на „подкаст“, което звучи като истинско предаване. Без „лекар“. При AI: „Драматизация · създадено с AI“.
**Статус:** нов

---

### VF-015 Карусел-история (пратката пристига)
**Какво е визуално:** 5 снимки като дневник, без тяло. Карта 1 е hook, карти 2–4 са стъпките, карта 5 е цената.
**Къде и защо скалира:** Adlibrary разбира 10 карусела, които въртят 60+ дни; при wellness MUD/WTR има 7 карти „проблем → 6 съставки → продукт“ ([източник](https://adlibrary.com/posts/carousel-ad-examples-2026)). AdRiseLab: най-големият спад е между карта 2 и карта 3 (47% → 31%; без посочен източник) ([източник](https://adriselab.com/blog/meta-carousel-ads-anatomy-2026)). Памет: 25 карусела-каталога, никой не върти 21+ дни.
**Адаптация за FitPatches:**
1. „Поръчах го с плащане при доставка. Ето какво пристигна.“ (пликът на Еконт)
2. „Платих чак на гишето.“ (касова бележка и плик, без лице)
3. „1 пакет · 30 лепенки · берберин, канела, нар“ (етикетът)
4. „1 сутрин на рамото. Под блузата не се вижда.“ (рамо под пуловер)
5. „14.99 € + доставка · плащаш при доставка“ (пакетът на масата)
- Надпис „Драматизация“ на карта 1.
**Продукция:** 5 истински снимки с телефон. Ниска.
**Риск в Meta:** нисък. Без „седмица 1“ и срокове до ефект.
**Статус:** нов

---

### VF-016 Инфографика „какво има вътре“
**Какво е визуално:** пакетът в центъра и 3 изнесени надписа с тънки линии към него. Чисто, с много въздух.
**Къде и защо скалира:** Motion Infographic: AG1, IM8 Health, Nutrafol, Function Health, Magic Mind ([източник](https://motionapp.com/library/formats/infographic)). Feature benefit pointout има hit rate 5.61%. Curtis Howland: „feature callout“ е за добавки със съставки. Лаб: A4 „какво има вътре“ 30.7 и 31.2 (резерва).
**Адаптация за FitPatches:** заглавие „Какво има вътре.“ Изнесени надписи: „берберин“ · „канела“ · „нар“ · „30 лепенки · 1 на ден · на рамото“. Долу: „14.99 € + доставка · плащаш при доставка“.
**Продукция:** Canva + снимка на истинския етикет. Ниска.
**Риск в Meta:** среден. **Само имената, без функции** на съставките (за берберина няма разрешени здравни претенции, 1924/2006). Без мг, докато собственикът не даде реалната доза. Без проценти. Съставките да се сверят с етикета (сайтът казва „берберин, канела и нар“, старите текстове казват „хром“).
**Статус:** нов

---

### VF-017 Green screen с адвърториала
**Какво е визуално:** Мария е изрязана пред скрийншот на статията (AD28) и сочи заглавието. Скролва и реагира с 1 изречение на всеки абзац.
**Къде и защо скалира:** Motion: Greenscreen има hit rate 4.87%, под средното ([източник](https://motionapp.com/thumbstop-pulse/creative-benchmarks-2026/)). Близките Stitch (12.50) и Reaction video (11.24) обаче водят в Health & Wellness. Памет: адвърториалите са 27% от рекламите (FreshHaut „Lies den Artikel“ ×5 в DE), но 30+ дни оцеляват само 5 от 392.
**Адаптация за FitPatches:** реакция на собствената ни статия „Пробвала съм всичко…“ (AD28): „Тази статия ми я прати сестра ми. Третият абзац съм аз.“ → цена и плащане при доставка.
**Продукция:** CapCut green screen + наличен говорещ кадър. Средна.
**Риск в Meta:** висок, докато AD27 и AD28 нямат „Рекламна публикация“ най-горе и в тях има „ендокринолог“ с име. Страницата на фона трябва да е същата като landing-а.
**Статус:** нов (блокер: AD27/AD28)

---

### VF-018 Google търсене (native search)
**Какво е визуално:** 6-секундно видео или статик. Лента за търсене, в която се изписва въпрос → курсор → срез към отговора.
**Къде и защо скалира:** Motion: 17 топ марки (SHEIN 366 реклами, Uber, Hilton, Anker, Loop). В 14% от случаите се комбинира с Text Message ([източник](https://motionapp.com/library/formats/native-search)). В здраве данни няма. Памет: F-016 „съмнението е заглавието“, Билков дневник „…измама? Ето истината“ 15–16 дни (857734534000246).
**Адаптация за FitPatches:** в лентата: „лепенки с берберин измама?“ → карта „И аз го търсих. Ето какво проверих:“ → „какво пише на кутията · как се плаща · какво пристига“ → „14.99 € + доставка · плащаш при доставка“.
**Продукция:** Canva или CapCut. Ниска.
**Риск в Meta:** среден. Без логото на Google и без фалшиви резултати, рейтинги и „хиляди търсения“.
**Статус:** нов

---

### VF-019 Кинетична типография (видео само с текст)
**Какво е визуално:** видео 9:16, 10–15 сек. Думите изскачат с прост ефект (pop или fade, 150–250 ms) на едноцветен фон. Последните 2 сек са пакетът.
**Къде и защо скалира:** пряко число за кинетичната типография няма. RocketShip HQ: сложната кинетика (букви, които летят и се въртят) губи, защото бави разбирането; простото „pop/fade“ печели. Задължително е 1.5 сек на ред и ≈4 думи в секунда. 85% от видеата във Facebook се гледат без звук (по Meta) ([източник](https://www.rocketshiphq.com/text-overlays-video-ads-mobile/)). Статичният еквивалент Text only е 11.6%.
**Адаптация за FitPatches:** A13 като текст: „5 неща.“ → „И не са от мързел.“ → петте реда с ✓ по 1.5 сек → „Не е мързел. Не е характер.“ → пакетът → „14.99 € + доставка · плащаш при доставка“.
**Продукция:** CapCut. Ниска.
**Риск в Meta:** нисък (като VF-009).
**Статус:** нов

---

### VF-020 2D анимация / skeleton
**Какво е визуално:** стилът от skill-а `anthropic-skills:skeleton-ad-style`: лъскав бял „порцеланов“ скелет с големи анимационни очи в изцяло бял минималистичен интериор. Продуктът е единственият цветен и реалистичен предмет.
**Къде и защо скалира:** Motion Animation: над 100 марки, най-много реклами имат Liven (654), BetterMe (587) и Today Is The Day (358) ([източник](https://motionapp.com/library/formats/animation)). Hit rate за анимацията не е потвърден. Skeleton е органичен тренд в Shorts и TikTok (напр. канал със 119 млн. гледания, [AITuber](https://aituber.app/blog/skeleton-channel-case-study-million-views/)), но данни за реклами няма. Лаб: анимацията ad1 („говорещото сърце“) дърпа мъже и хора с антикоагуланти (N04, P15), тоест грешна аудитория.
**Адаптация за FitPatches** (хумор и рутина, без физиология): скелетът седи на бял стол в бялата кухня и чете списъка „5 неща, които много жени забелязват с годините“. Кима на всеки ред, отваря истинския пакет и лепва лепенка на рамото. Надписи в монтажа.
**Продукция:** референтен кадър в Higgsfield (Nano Banana или Seedream) → Kling или Veo. Висока (кредити, проверка на баланса).
**Риск в Meta:** среден. Без органи, мазнини, кости, които „отслабват“, и метаболизъм в анимация (физиология без източник). Скелетът не показва форма на тялото. Остава CB-008, P3.
**Статус:** нов (CB-008)

---

### VF-021 AI аватар (водеща, не клиентка)
**Какво е визуално:** AI водеща от името на FitPatches отговаря на най-честите въпроси (S2) като говорител на марката, без лична история.
**Къде и защо скалира:** надеждни данни за ефект няма. Higgsfield дава само цена: 15 сек ≈ 4.46 $ срещу 150–300+ $ за UGC видео, и сам предупреждава, че това не е гаранция за резултат ([източник](https://higgsfield.ai/blog/ai-avatars-vs-ugc-creators-2026)). Meta слага етикет „AI info“ на фотореалистичен синтетичен човек. Аватарът като говорител с текст на марката е ОК, но като „проверена купувачка“ не е ([Cinerads, по стандартите на Meta](https://www.cinerads.com/blog/ai-ugc-facebook-ad-policy)).
**Адаптация за FitPatches:** „Аз съм от екипа на FitPatches. Ето петте въпроса, които ни задавате най-често.“ → цена, плащане при доставка, как се лепи, кожата. Без „при мен работят“.
**Продукция:** Higgsfield. Средна.
**Риск в Meta:** висок, ако аватарът разказва „моите резултати“ (забранено в compliance-rules). Надпис „Драматизация · създадено с AI“ (EU AI Act, чл. 50).
**Статус:** нов

---

### VF-022 „Какво е · за какво е · как се ползва“ (етикетна карта + 17 сек How To с ръце)
*Добавена на 03.10, 03:11, лаб смяна BR. Защо точно сега: панелът на 23:11 показа, че по-възрастните не разбират за какво е продуктът, а 4-те визуални формата, които вече тествахме, не го казват (карусел-чеклист 26.0, тетрадка 30.8, чат 31.2, статик с цената 19.6).*

**Какво е визуално:** два варианта на един формат. Без персона и без лице, затова не е нужна „Драматизация“ (ред 68 в compliance-rules).
- **Статик 4:5 (основен).** Светъл фон (крем или бяло) и тъмен текст. Без светъл текст на тъмен фон. Горе: истинският пакет FitPatches, до него 1 лепенка извън плика, снимка с телефон на кухненска маса. Под тях 3 реда с номера, без иконки в кръг (ред 74). Шрифтът е едър: думата в началото на реда е ≥ 64 px, текстът ≥ 48 px при ширина 1080 px.
  1. **Какво е:** лепенка с берберин, канела и нар. 30 в пакет.
  2. **За какво е:** [един от трите реда по-долу, избира compliance-officer]
  3. **Как се ползва:** 1 лепенка сутрин, на рамото. Не е хапче, не се гълта.
  Лента долу, на един ред, в един цвят и размер: „14.99 € + доставка · плащаш при доставка“. Под нея дребен печатен ред (≥ 30 px): „Не е лекарство. Не замества разнообразното хранене и движението. При лекарства, бременност или кърмене — първо лекарят.“ Пакетът не докосва дребния ред (ред 72).
- **Видео 17 сек, 9:16 (How To, само ръце).** Надписите се четат и без звук. Гласът е по желание, бавен, женски, 50+.

| Време | Кадър | Надпис | Глас |
|---|---|---|---|
| 0–3 сек | Ръце държат пакета на кухненската маса, етикетът се чете | „Какво е това?“ (голямо) | „Какво е това и за какво е? Казвам го направо.“ |
| 3–6 сек | Ръката вади 1 лепенка от плика | „Лепенка с берберин, канела и нар · 30 в пакет“ | „Лепенка с берберин, канела и нар. Трийсет в пакет.“ |
| 6–10 сек | Ръката лепва лепенката на рамото през деколтето на блузата (рамото, не корема), с едно движение | „1 сутрин · на рамото · не се гълта“ | „Една сутрин, на рамото. Не е хапче.“ |
| 10–13 сек | Ръкавът пада, лепенката не се вижда. Ръцете оставят пакета | „За какво е: [ред от compliance]“ | същият ред на глас |
| 13–15 сек | Пакетът и отвореният сив плик от Еконт без товарителница (ред 76) | „14.99 € + доставка · плащаш при доставка“ | „Четиринайсет и деветдесет и девет плюс доставка. Плащаш, като я получиш.“ |
| 15–17 сек | Чаша кафе, без продукт в кадър (ред 36, 43), твърд срез | „Не е лекарство. При лекарства, бременност или кърмене — първо лекарят.“ | същото, на глас |

**Редът „За какво е“ (решава compliance-officer, подредени от най-ясния към най-безопасния):**
- **А:** „За жени, които искат да отслабнат и не искат още едно хапче.“ Отговаря точно на въпроса на P15 („за килограмите ли е?“). Рискът е най-висок: това е функция на продукта, а за берберина няма разрешена здравна претенция (1924/2006). Meta изисква 18+ и без обещан резултат.
- **Б:** „Част от сутрешната рутина на жени, които внимават с храненето и теглото.“ Описва кой го ползва, не какво прави. Рискът е среден: „теглото“ стои близо до продукта.
- **В:** „За жени, които искат да внимават с храненето и не искат още едно хапче.“ Без тегло, затова е най-безопасен, но и най-малко ясен.
- Към всеки от тях стои „Не е лекарство.“. Ред „Не е за кръвно или кръвна захар.“ би отговорил директно на P15, но назовава заболяване. Пускаме го само с ОК от compliance.

**Текст под рекламата:**
„Какво е това? Казваме го направо.
Какво е: лепенка с берберин, канела и нар. 30 в пакет.
За какво е: [ред от compliance].
Как се ползва: 1 лепенка сутрин, на рамото. Не е хапче, не се гълта.
1 пакет 14.99 € + доставка. Плащаш при доставка.
Не е лекарство. Не замества разнообразното хранене и движението. При лекарства, бременност или кърмене — първо лекарят.“
**Заглавия:** „Какво е, за какво е и как се ползва“ · „Лепенка с берберин: 1 сутрин, на рамото“. **CTA:** като родителя.

**Къде и защо скалира (сигнал):**
- **Motion 2026:** Demo („продуктът прави това, за което е създаден“) е №3 сред най-добрите формати в Meta: hit rate 8.1%, 12.6% от креативите и 12.9% от разхода ([formats](https://motionapp.com/library/formats/)). Примери в здраве и красота: AG1, SkinCeuticals, Gisou ([Demo](https://motionapp.com/library/formats/demo)). How To (стъпка по стъпка, ръце отблизо, надпис на всяка стъпка) ползват AG1, HUM Nutrition, Dog is Human и Function Health ([How To](https://motionapp.com/library/formats/how-to)). За How To отделни числа няма.
- **BR, 03.10 (нашата памет):** 4 страници за 2 дни слагат в заглавието само името и какво е продуктът. Seviva „Berberina HCL 500mg“ ([1554709433342845](https://www.facebook.com/ads/library/?id=1554709433342845)). BiotipoFarma „Conheça o Destrave Metabólico“ („Запознай се с…“, 6 карти в една реклама, [1822334802434822](https://www.facebook.com/ads/library/?id=1822334802434822)). Estação Saúde „KIT BERBERINA + MELÃO SÃO CAETANO“ ([927561833448102](https://www.facebook.com/ads/library/?id=927561833448102)). Arnaldo Roberto „Glutanac 60 Cápsulas — Fórmula Hepática…“ ×43 за 7 ч, от тях 36 за 62 сек ([2142461056400643](https://www.facebook.com/ads/library/?id=2142461056400643)). Всички са на 0–1 ден, дълголетие няма. Визията е неясна, сигналът е само в заглавията.
- **Лаб, 23:11** (`team/lab/runs/20261002-2312-active/panel-H.json`): P15 (59 г., пие лекарство за кръвно) в 8 от 11 варианта казва, че не е разбрала за какво е продуктът: „Ама за какво е това, за кръвно ли, за отслабване ли, не разбрах.“ Поправките, които самата тя предлага: „Да почне с това за какво е, на глас и с голям надпис.“ и „Всичко на една голяма картинка, с цената и за какво е.“
- **CDMG** (директен маркетинг към 55+): „Clarity beats cleverness“. Според автора тест с шрифт 14 срещу 10 пункта дава +18% отговор, а светъл текст на тъмен фон намалява четенето ([източник](https://cdmginc.com/2026/09/09/marketing-to-seniors-46-surprising-advertising-insights/)). Това е твърдение на автора и го ползваме само като посока.

**Защо ще работи:** това е единственият формат в библиотеката, който казва какво е продуктът още в първия ред и с едър шрифт. Карусел, тетрадка, чат и статик с цената оставят въпроса „за какво е“ без отговор, а P15 казва точно това. Цената и плащането при доставка (ядрото на S2) остават, а продуктът се вижда в употреба, тоест Demo. Без кредити: една снимка и 17 сек с телефон.

**Как ще подейства:** спира с „Какво е това?“, защото е същият въпрос, който тя си задава за всяка реклама с лепенки. Не изглежда като обещание, а като етикет. Чете 3 реда (какво е, за какво, как), едри като на кутия от аптеката, и вижда ръката, която лепва на рамото, тоест „толкова е лесно“. Цената с доставката и плащането при доставка махат страха от измама. Редът за лекаря стои накрая, без продукт в кадъра. За P15 това е доверие, а за нас е защита → клик.

**Продукция:** снимка с телефон + Canva (статик) и 17 сек с телефон, само ръце (видео). Ниска, без AI кредити.
**Риск в Meta:** нисък до среден. Целият риск е в реда „За какво е“: виж А/Б/В. Без кг, срокове и „през кожата“. Цената е винаги с „+ доставка“ (ред 73). Без иконки-значки (ред 74). Лепенката е на рамото (ред 26). Редът за лекаря е в дребния печатен ред и в последната сцена, без продукт (ред 36, 72). **Внимание:** колкото по-ясно е, толкова повече дърпа и хора с лекарства (P15, N04), затова редът за лекаря е задължителен и в статика, и във видеото.
**Ген за лаб смяната:** `visual_format` върху контролата S3-30 + отворения ген „безопасен ред „за какво е““ от `gene-queue.json` → `next.angle`. Сравнение: VF-022 статик срещу VF-022 видео срещу S3-30.
**Статус:** нов (03.10), за следващата лаб смяна след ОК на compliance за реда „За какво е“

---

### VF-023 „Един ден, 4 снимки“: демонстрация с ръце от сутринта до вечерта (тест за носене, без персона)
*Добавена на 03.10, 07:11, лаб смяна ES. Защо точно сега: на 03:11 статикът изравни видеото само когато тялото е списък за четене (тетрадка 33.7, чат 31.9). Лентата „Драматизация“ свали доверието („значи е нагласено“, P16, P08, P03). Търсим формат, който е истински по природа: истински продукт, ръце, часовник, без измислен човек.*

**Какво е визуално:** демонстрация на продукта, не история. Няма име, „при мен“, покупка или ефект, затова „Драматизация“ не е нужна (compliance-rules, ред 68). Условието е снимките да са **истински**.
- **Статик 4:5 (основен).** Решетка 2×2 от 4 снимки с телефон на един и същи ден. Всяка снимка има в ъгъла час, дребен и бял на тъмна лентичка, и 1 кратък надпис под нея. Горе има лента със заглавието. Долу има бяла лента с продукта, цената и задължителните редове. Пакетът е само на снимка 4, далеч от реда за лекаря (compliance-rules, ред 72).
- **Видео 12 сек, 9:16 (по желание).** Същите 4 кадъра по 2.5 сек, с часа в ъгъла и истинския звук: лепването, шумоленето на ръкава, отлепването (ASMR, без глас). Последните 2 сек са крайна карта без продукт.

| Карта / кадър | Какво се вижда | Надпис |
|---|---|---|
| Лента горе | само текст, тъмен на крем | **„Една лепенка. Един ден. 4 снимки.“** Под нея, по-дребно: „Най-честият въпрос е „вижда ли се и държи ли“. Снимахме я.“ |
| 1 · 07:40 | Ръка лепва лепенката на рамото (горната част на ръката) с едно движение. Отзад, размазана, чаша кафе | „07:40 · Лепва се на рамото, на чиста и суха кожа.“ |
| 2 · 12:15 | Същото рамо под ръкава на обикновена тениска или блуза. Нищо не се вижда | „12:15 · Под ръкава не се вижда.“ |
| 3 · 17:30 | Ръка повдига ръкава и лепенката е на мястото си. На другото рамо има дръжка на пазарска чанта (нормален ден, без спорт) | „17:30 · Още е на мястото си.“ |
| 4 · 21:00 | Пръсти отлепват лепенката с едно движение и тя е на върха на пръста. До нея, на нощното шкафче, е пакетът | „21:00 · Маха се с едно движение. Утре е нова.“ |
| Лента долу | само текст | „FitPatches · берберин, канела и нар · 30 лепенки · 1 на ден · Не е хапче.“ · „За жени, които внимават какво ядат.“ · **„14.99 € + доставка · плащаш при доставка“** (един ред, един цвят и размер) · дребен печатен ред ≥ 30 px: „Не замества разнообразното хранене и движението. При лекарства, бременност или кърмене — първо лекарят.“ |
| Видео: крайна карта 10–12 сек | чаша кафе, без продукт в кадъра (compliance-rules, ред 36 и 43) | цената и дребния ред от лентата долу |

**Текст под рекламата:**
„Най-честият въпрос за лепенките е „вижда ли се и държи ли“.
Вместо да обясняваме, снимахме една лепенка от 07:40 до 21:00.
Лепва се на рамото. Под ръкава не се вижда. Вечер се маха с едно движение.
Берберин, канела и нар. 30 лепенки в пакет. Не е хапче, не се гълта.
За жени, които внимават какво ядат.
1 пакет 14.99 € + доставка. Плащаш при доставка.
Не замества разнообразното хранене и движението. При лекарства, бременност или кърмене — първо лекарят.“
**Заглавия:** „Една лепенка. Един ден. 4 снимки.“ · „Вижда ли се и държи ли? Снимахме я.“ **Описание:** „14.99 € + доставка · плащаш при доставка“. **CTA:** като родителя.

**Къде и защо скалира (сигнал):**
- **Kind Patches (US), най-голямата марка с лепенки** (в 890 магазина на Target, [avenuez](https://avenuez.com/blog/kind-patches-in-890-target-stores/)): ≈2 000 активни реклами и ≈168 нови креатива на седмица. **Demo е 15%** от библиотеката им и дели първото място с Testimonial (15%), следва Offer-First Banner (12%). Демонстрациите показват лепването и близки планове на пакета и лепенката ([Motion](https://motionapp.com/library/kind-patches)). Испанската им страница продава „Parches de Berberina“ с **берберин, нар и канела, нашите три съставки**, с оферта „2 + 2 Gratis“ ([kindpatches.com](https://kindpatches.com/pages/glplpv4-es)).
- **ES, 03.10 (нашата памет):** Velia Parches пуска 30 нови реклами за 6 дни с офертата „1 + 1 GRATIS“, а после „2 + 2 GRATIS“ ([2272718843572923](https://www.facebook.com/ads/library/?id=2272718843572923)). Заглавието съвпада с офертата на Kind Patches. Визията не се вижда.
- **Motion 2026:** Demo е №3 в Meta с hit rate 8.1%, 12.6% от креативите и 12.9% от разхода ([formats](https://motionapp.com/library/formats/)). Love Wellness държи продукта в ръка с балончета за ползата (Demo 11%, Feature Benefit Pointout 7%; [Motion](https://motionapp.com/library/love-wellness)).
- **adlibrary (2026):** при физически продукт демонстрацията с ръце маха възражението „прави ли това, което казва“. Почва се направо в употреба, без лайфстайл пълнеж ([източник](https://adlibrary.com/posts/best-dtc-meta-ads-examples-2026)).
- **Честно:** собствено число за „тест за носене“ (часове на лепенката) няма. Сигналът е за семейството Demo, затова силата е **B+**.

**Защо ще работи:**
- **Тялото е списък за четене:** 4 реда по 4–6 думи, както при тетрадката (33.7) и чата (31.9). Няма глас и човек, които да липсват, а това свали бележката (24.1) и големия текст (28.6).
- **Не е нужна лента „Драматизация“:** няма измислен човек, само продуктът, ръце и часовник. Махаме точно това, което на 03:11 свали доверието.
- **Отговаря на въпроса от победителя S2:** „как се лепи и вижда ли се“. Това е единственото възражение, което се доказва със снимка, а не с думи.
- **Отговаря на P15** (59 г., „не разбрах за какво е“) с реда „За жени, които внимават какво ядат.“. На 03:11 този ред не навреди (A13 33.5, 57%), а P15 каза „разбрах всичко“.

**Как ще подейства:**
- **0–1 сек (спира):** 4 снимки с часове изглеждат като нечий телефон, не като реклама. Окото тръгва към часовете: „какво става с нея през деня?“.
- **1–3 сек (разпознава се):** „Лепва се на рамото“, „под ръкава не се вижда“. Това е нейното мълчаливо възражение: „ще ми личи под блузата“.
- **3–5 сек (възражението пада):** „17:30 · Още е на мястото си“ и „маха се с едно движение“. Отговорът е снимка, не обещание.
- **5–7 сек (доверие):** „берберин, канела и нар · не е хапче“ и „За жени, които внимават какво ядат“. Вече знае какво е и за кого е.
- **7–8 сек (клик):** „14.99 € + доставка · плащаш при доставка“. Цената не е скрита и няма риск с картата.

**Продукция:** един ден със снимки с телефон. Снима собственикът или Боян, на ръката на човек от екипа, с писмено съгласие. Решетката се прави в Canva. 0 € и ниска трудност.
- **Без AI:** демонстрация на свойство на продукта (държи, не се вижда), направена с AI, е подвеждаща (2005/29, чл. 6). Ако няма истински снимки, картата остава само за симулацията.
- **Часовете се нагласят по етикета:** колко часа се носи лепенката, трябва да потвърди собственикът. Ако е под 13 часа, 17:30 и 21:00 се местят по-рано. В сляпата версия на рунда стоят часовете от таблицата, без „[…?]“.
- **„Още е на мястото си“** влиза в Meta само ако истинският тест го покаже. Ако не издържи, картата 3 става „17:30 · Под блузата пак не се вижда.“.

**Риск в Meta:** нисък.
- Само рамо и горната част на ръката, без корем (ред 26).
- Само свойства на продукта, без ефект: никакъв апетит, „не ми се яде“ или енергия на часовете. Това би бил срок до ефект (ред 22, 23).
- Без „ден 1… ден 7“ (ред 75): часовете са в един ден и показват носене, не резултат.
- Без „водоустойчива“ и „душ“, докато не се потвърдят с истински тест и етикета.
- Без „през кожата“ (ред 20).
- Лепенката се слага само на себе си. ASA (UK) на 02.09.2026 забрани реклама на Kind Patches, в която лепенка се слага на друг човек без съгласие, като „безотговорна“. Там заради недоказани ефекти падна и „Dopamine Patch“ ([ASA](https://www.asa.org.uk/rulings/kind-patches-ltd.html)).
- Без иконки-значки и „100% натурално“ (ред 74).

**Ген за лаб смяната:** `visual_format`, самостоятелен статик. Сравнява се с VF-008 (тетрадката, 33.7, най-добрият статик) и с контролата S3-30. Хипотеза: ще спечели практичните и скептичните (P05, P08, P13) и 50+ (P15). Ще загуби емоционалните (P10, P14), защото няма болка в hook-а.
**Статус:** нов (03.10), за следващата лаб смяна (CB-032)

---

### VF-024 „Въпросът горе, отговорът долу“ (Stitch: чужд въпрос, наш отговор)
*Добавена на 03.10, 08:59, дневен скан BG + IT. Защо точно сега: урокът от 07:11 е, че демонстрациите без човек губят (19.5–24.2), а печели „човек отговаря на въпроси“ (F-004 37.0, S3-30 36.4, A17 34.7). В S3-30 приятелката само се чува от телефона. Stitch я показва и я прави на годините на P04 и P15.*

**Какво е визуално:** видео 9:16, 31 сек, от 2 клипа, снимани поотделно с телефон.
- **Горният клип е въпросът,** 1.5–3 сек на всяко връщане. Друга жена, около 55 г., у дома вечер, селфи кадър. Казва съмнението или въпроса към своя телефон. Появява се 5 пъти: hook-ът, 3 кратки въпроса и финалът.
- **Долният клип е отговорът.** Героинята на S3-30 в кухнята, сутрин. Докато горе питат, тя е в долната половина и реагира (кима, вдига пръст). Когато отговаря, кадърът ѝ е на цял екран.
- **Без интерфейс на TikTok или Instagram:** без потребителско име, без думата „Stitch“, без „отговор на @…“, без бутони и сърчица (compliance-rules, ред 27 и 70). Двата клипа са разделени от тънка бяла линия.
- **Постоянен надпис „Драматизация“** от първия до последния кадър, защото и двете жени са роли.

| Време | 🎬 Кадър | 🖊 Надпис | 🎙 Глас |
|---|---|---|---|
| 0–3 сек (HOOK) | Сплит 50/50. Горе: жена ~55 г., сребриста коса на кок, очила за четене на главата, диван и вечерна лампа; гледа в телефона с вдигната вежда. Долу: героинята на S3-30 (кухнята, маслиненозелен пуловер, чаша кафе, разкъсан плик на Еконт) гледа нагоре към горния клип, усмихва се и вдига пръст: „чакай“ | субтитри: горе в жълто, долу в бяло · голям надпис на линията между клиповете: „Отговарям.“ | (горе) „Лепенки с берберин? Това е поредната измама от нета.“ |
| 3–8 сек | Цял екран: героинята. Кимва на „И аз така мислех“, потупва плика на Еконт на „платих чак като ги взех“ | „Плащаш при доставка“ | „И аз така мислех. Затова поръчах с плащане при доставка. Платих чак като ги взех от Еконт.“ |
| 8–9.5 сек | Сплит. Горе: жената, скептична | субтитри | (горе) „И колко?“ |
| 9.5–14 сек | Цял екран: кухненската маса. Изважда 4 пакетчета от плика и ги нарежда. На „Един пакет“ вдига едно, в края ги избутва от кадъра | „1 пакет 14.99 € + доставка · 30 лепенки“ / „3+1 подарък 39.99 € · безплатна доставка“ | „Един пакет е 14.99 евро плюс доставка, трийсет лепенки.“ |
| 14–15.5 сек | Сплит. Горе: жената | субтитри | (горе) „И работят ли?“ |
| 15.5–20 сек | Цял екран: говореща глава. На „Не са магия“ свива рамене. В кадъра няма шоколад | „Не са магия. Само моят опит.“ | „Не са магия. Но обичам шоколад, а вечер вече не посягам към него като преди.“ |
| 20–21.5 сек | Сплит. Горе: жената | субтитри | (горе) „Как се слага?“ |
| 21.5–26 сек | Близък план на рамото: лепва лепенката с едно движение и оправя пуловера. Кадърът свършва на покритото рамо | „сутрин · чиста кожа · на рамото“ / „не е хапче, не се гълта“ | „Сутрин, на чиста кожа, на рамото. Не е хапче, не се гълта.“ |
| 26–28.5 сек | Твърд срез към лицето, без J-cut. Без лепенка и пакет в кадъра, на масата е само чашата | карта (бял фон, тъмен текст): „Лекарства, бременност, кърмене? Първо лекарят.“ | „При лекарства, бременност или кърмене — първо лекарят.“ |
| 28.5–31 сек | Сплит. Горе: жената кимва с половин усмивка. Долу: героинята поглежда в камерата и посочва надолу | „Линкът е отдолу“ | (горе) „Добре де. Къде ги има?“ (долу) „Линкът е отдолу.“ |

**Текст под рекламата:**
„„Лепенки с берберин? Това е поредната измама от нета.“
И аз така мислех. Затова поръчах с плащане при доставка. Платих чак като ги взех от Еконт.
„И колко?“ 1 пакет е 14.99 € + доставка, 30 лепенки. Аз взех 3+1 подарък за 39.99 € с безплатна доставка.
„Как се слага?“ Сутрин, на чиста и суха кожа, на рамото. Не е хапче, не се гълта.
При лекарства, бременност или кърмене — първо лекарят.
Линкът е отдолу.
*Видеото е драматизация. Лепенката не замества разнообразното хранене и движението.“
**Заглавия:** „Измама ли е? Плащаш при доставка“ (от S3-30) · „Отговарям на най-честите въпроси“ · „Колко струват и как се лепят“. **CTA:** SEE_DETAILS, като родителя.

**Къде и защо скалира (сигнал, сила A):**
- **Motion, Creative Benchmarks 2026 по вертикали:** в Health & Wellness Stitch е №1 по hit rate, а Reaction video е №2. Според Motion в тази вертикала „доминират форматите около доверие, авторитет и лична история“ ([visual-formats-by-vertical](https://motionapp.com/library/research/creative-benchmarks-2026/visual-formats-by-vertical)). Числата (Stitch 12.50, Reaction video 11.24) са взети на 02.10 ([thumbstop-pulse](https://motionapp.com/thumbstop-pulse/creative-benchmarks-2026/)). Днес страницата не ги показва без JS. Извадката е 550 000+ реклами от 6 000+ рекламодатели, IX.2025–I.2026.
- **Motion, Stitch:** 11 марки с по 13–59 реклами. В здраве и добавки: Her Fantasy Box 59, Rise Science 25, Dose 20, Primal Queen 14, Auri Nutrition 13. В красота: Carpe 26, DRMTLGY 21, Hismile 21, Prose 19. Половината реклами Stitch са и Testimonial, половината и Demo. Пример DRMTLGY: 0–3 сек жена пита за продукт за пори → 3–7 сек започва отговорът → 16–21 сек продуктът с експерт → 38–46 сек цена и CTA ([Stitch](https://motionapp.com/library/formats/stitch)).
- **Motion, Reaction video:** Hismile 703 реклами, Dr. Squatch 95, Clean Skin Club 86, Spacegoods (добавки). Най-често се съчетава с Demo (36%), Testimonial (21%) и ASMR (21%) ([Reaction video](https://motionapp.com/library/formats/reaction-video)).
- **Нашата памет, 03.10:** възражението като заглавие вече е при 4 марки. Днес се добави Krista G (BG) с „Да, не е евтин. Ето защо.“ ×2 ([1811060966715331](https://www.facebook.com/ads/library/?id=1811060966715331)), до Билков дневник, SoulBotanic и FreshHaut (F-016). Визията им е неясна.
- **Лаб, 07:11:** F-004 37.0, S3-30 36.4 (в топ 2 три рунда подред), A17 34.7. P04 и P15 спират, когато „жената е на моите години“ (A17).

**Защо ще работи:** S3-30 вече печели, защото пита друг човек. Stitch добавя лицето на питащата: скептична жена на 55 е огледало за P04, P15 и 50+ персоните. Въпросът идва от непозната, не от приятелка, затова звучи като публично съмнение, от което марката не бяга. Тялото е почти дума по дума S3-30, значи новото е само hook-ът и формата.

**Как ще подейства:**
- **0–3 сек:** в лентата вижда две лица и чува собственото си съмнение („измама“), казано от жена на нейните години, и спира. Долу някой вдига пръст „чакай“, значи следва отговор.
- **3–8 сек:** „платих чак като ги взех от Еконт“ маха страха от измама.
- **8, 14 и 20 сек:** горе пак питат. Всяко връщане е нов мини hook и държи задържането.
- **9.5–26 сек:** цената с доставката, 1 ред опит без обещание и как се слага (вижда колко е лесно).
- **26–31 сек:** редът за лекаря, после питащата кимва „Добре де“. Това е разрешение и за зрителката, и тя кликва.

**Продукция:** 2 клипа с телефон за 1 ден, 2 жени с писмено съгласие (или актриси). Монтаж в CapCut, сплит 50/50. Трудността е ниска до средна. За симулацията може AI (Kling/Veo), за Meta само истински запис.
**Риск в Meta:** среден.
1. Без вид на чужд пост: без потребителско име, лого на платформа и „отговор на“ (ред 27, 70).
2. „Драматизация“ сваля доверието (урок 03:11). Резерва: двете жени са реални хора от свое име. Тогава лентата не е нужна, но всичко, което казва героинята, трябва да е вярно за нея.
3. „Измама“ казва питащата за категорията. Марката не напада други („китайско“, „другите лъжат“).
4. Редът за ефект е 1, в първо лице и относителен, както в S3-30. Без кг, срокове и „през кожата“.
5. Редът за лекаря е с твърд срез и без продукт в кадъра (ред 36, 43).

**Ген за лаб смяната:** `visual_format` върху S3-30, в два варианта:
- **V-а** е основният, по-горе.
- **V-б** е чист A/B: S3-30 дума по дума, но приятелката се вижда горе като видеоразговор, вместо да се чува от телефона. Сменя се само едно нещо: вижда ли се питащата.
**Статус:** нов (03.10), за следващата лаб смяна (CB-036)

---

### VF-025 „Снимка с човек + текст отгоре“ (UGC overlay, статик)
*Добавена на 03.10, 08:59. Защо точно сега: статиките без човек губят в лабораторията. VF-022 има 19.5, VF-007 24.0, а VF-023 24.2 („Няма човек, няма история, не ме засяга.“). Най-добрият статик досега е тетрадката (33.7), но и тя е без лице. Проверяваме дали човек на снимката спасява статика.*

**Какво е визуално:** статик 4:5 (+ 9:16). Снимка, която изглежда като от телефона на обикновена жена, а текстът е върху снимката в бели кутийки като в сторис. Без интерфейс на Instagram, без звезди и без вид на отзив (ред 70).
- **Снимката:** истинска, с телефон. Жена ~45–50 г. в кухнята, сутрешна светлина, чаша кафе. С едната ръка отмества ръкава на тениската и показва лепенката горе на рамото (само рамото, ред 26), гледа в камерата с половин усмивка. Истинският пакет е на масата в долния ляв ъгъл и не докосва долната лента (ред 72).
- **Текстът** повтаря 3-те реда на VF-022, за да е чист A/B. Сменя се само едно: има ли човек.
  - горе, по-дребно: „Често ме питат:“; под него, едро, в бяла кутийка: „„Какво е това на рамото ти?““
  - до рамото, кутийка със стрелка към лепенката: „Лепенка с берберин, канела и нар. 30 в пакет.“
  - в средата: „За жени като мен, които внимават какво ядат. Не е лекарство.“ (одобрен ред 2, ред 112)
  - под него: „1 сутрин, на рамото. Не е хапче, не се гълта.“
  - жълта лента долу: „1 пакет 14.99 € + доставка · плащаш при доставка“
  - дребен печатен ред най-долу (≥ 30 px, вътре във всяко изрязване): „Драматизация · Не замества разнообразното хранене и движението. · При лекарства, бременност или кърмене — първо лекарят.“
- **Вариант б (без „Драматизация“):** истински човек от екипа с името си („Мила, от екипа на FitPatches“), текст от името на марката: „Често ни питат: „Какво е това на рамото?““. Без „при мен“ и без ред за опит. „За жени, които внимават какво ядат.“ (ред 111).

**Текст под рекламата:** „Често ме питат: „Какво е това на рамото ти?“ / Лепенка с берберин, канела и нар. 30 в пакет. / За жени като мен, които внимават какво ядат. Не е лекарство. / 1 лепенка сутрин, на рамото. Не е хапче, не се гълта. / 1 пакет 14.99 € + доставка. Плащаш при доставка. / При лекарства, бременност или кърмене — първо лекарят. / *Снимката е драматизация. Лепенката не замества разнообразното хранене и движението.“
**Заглавия:** „Какво е това на рамото ти?“ · „Лепенка с берберин: 1 сутрин, на рамото“.

**Къде и защо скалира (сигнал, сила A):**
- **Motion, UGC Overlay:** само статик („снимка, която може да е от нечий телефон: човек държи продукта… с текст отгоре“). Най-много го ползват марки за добавки: JSHealth Vitamins 1 000+ реклами, Happy Mammoth EU 600, Happy Mammoth 531, Vitabiotics 511, Nutrition Geeks 364. В красота: Norse Organics 1 000+, Chāmpo 836, Frøya 677. Най-често се съчетава с Listicle (20%), Review (16%), Offer-First Banner (14%) и Feature Benefit Pointout (14%) ([UGC overlay](https://motionapp.com/library/formats/ugc-overlay)).
- **Motion, Health & Wellness:** UGC overlay е в топ 10 по spend use, заедно със Social post mockup, Letter, Founder и Offer-first banner ([visual-formats-by-vertical](https://motionapp.com/library/research/creative-benchmarks-2026/visual-formats-by-vertical)).
- Happy Mammoth е в нашата ниша (жени 40+, хормони и тегло, ≈1 000 активни реклами, VF-008).

**Защо ще работи:** като етикетна карта същите 3 реда губят (19.5), защото „няма човек“. Лицето и „Често ме питат“ ги превръщат в човек, който отговаря на въпрос. Това е ядрото на победителите, на цената на статик. Текстът остава едър и ясен за P15.

**Как ще подейства:** в лентата прилича на снимка от сторис на позната, не на реклама. Спира на лицето и на въпроса в кавички. Стрелката към рамото отговаря „какво е“ за 1 секунда. После чете 3 реда, цената с доставката и плащането при доставка, а накрая реда за лекаря и кликва.

**Продукция:** 1 снимка с телефон + Canva, 20 минути, 0 €. Истинска жена с писмено съгласие. AI снимка на човек е само за симулацията (Meta: етикет „AI info“; ред 18).
**Риск в Meta:** нисък до среден. „Драматизация“ сваля доверието (урок 03:11), а вариант б го избягва. Без звезди, „отзив“ и „истинско мнение“ (ред 70). Само рамото. „+ доставка“. Редът за лекаря е в дребния ред, далеч от пакета (ред 72).
**Ген за лаб смяната:** `visual_format`, самостоятелен статик. Сравнява се с VF-022 статик (19.5, същите редове без човек), VF-008 тетрадка (33.7) и контролата S3-30.
**Връзка със CB-035:** стратегът вече пусна в рунда `20261003-0859-active` „селфи-статик с цитат“ (CB-035, точка 4), със собствен текст за колежката и Еконт. Тази карта дава пазарния сигнал за формата. CB-037 е чистият A/B: същите редове като VF-022 + лице. Пуска се след резултата на CB-035 (4).
**Статус:** нов (03.10); формата е в симулация като CB-035 (4), а чистият A/B е CB-037

---

### VF-026 „Скептикът вкъщи“ (скеч в кухнята: съпругът пита, тя отговаря)
*Добавена на 03.10, 11:11, скаут NL (без Ads Library, бюджетът е изчерпан). Защо точно сега: урокът от 08:59 е „печели диалогът, не лицето“. A18 (приятелка пита) взе 35.0, уличната анкета 33.0, A19 (дъщерята пита) 32.6, подкастът 31.8. Монолозите губят: green screen 25.2, split screen 22.9, селфи-статикът 20.6. Вече сме тествали като питащ приятелка, фризьорка, дъщеря, непознати на улицата и водеща. Най-скептичният човек вкъщи, съпругът, още не е тестван.*

**Какво е визуално:** видео 9:16, ≈32 сек, 1 локация, 2 души в кадър едновременно. Не е сплит и не е разговор по телефона.
- **Камерата е статична**, телефонът е подпрян на буркан на плота, като домашно видео. Двамата се виждат цели в кадъра (two-shot). Има само 2 вмъквания отблизо: пакетите на масата и рамото.
- **Той пита, тя знае.** Съпругът е на около 55, с очила за четене на носа. Той е гласът на съмнението на зрителката. Никога не обяснява и никога не говори за тялото ѝ. Тя е на около 50, спокойна, и отговаря кратко. Ролите са обърнати нарочно: на 08:59 основателят (мъж, който обяснява) падна до 21.2 („Мъж в офис ми обяснява за женското тяло — не.“).
- **Хуморът е в hook-а и във финала:** той срича „Бер… бер-бе-рин?“ (ехо от „Бер-какво?“ в уличната анкета, първата реклама с хумор, 33.0). Скептикът се предава с „Прати ми линка. За сестра ми.“
- **Субтитри:** той в жълто, тя в бяло. Постоянен надпис „Драматизация“ от първия до последния кадър. Без интерфейс на TikTok или Instagram.

| Време | 🎬 Кадър | 🖊 Надпис | 🎙 Глас |
|---|---|---|---|
| 0–3.5 сек (HOOK) | Кухнята сутрин, статичен кадър от плота. Тя (тъмна коса на опашка, сив пуловер с широко деколте) си налива кафе с гръб към него. Той (домашна жилетка, очила на носа) влиза с разкъсания сив плик от Еконт в едната ръка и пакета FitPatches в другата. Чете кутията отблизо, после я отдалечава на една ръка разстояние. Товарителницата е покрита с бял стикер | голям надпис горе: „Мъжът ми намери плика.“ · субтитри | (той, сричайки) „Бер… бер-бе-рин?“ (поглежда я над очилата) „Това пак някоя измама от интернет ли е?“ |
| 3.5–8 сек | Тя се обръща с чашата и се усмихва с половин уста. Взима плика от ръката му и го потупва на „платих чак като ги взех“ | „Плащаш при доставка“ | (тя) „И аз така мислех. Затова платих чак като ги взех от Еконт.“ |
| 8–12 сек | Той върти пакета в ръце. Тя го взима и посочва етикета (текстът на кутията се слага в монтажа) | „лепенка · берберин, канела, нар · 30 в пакет“ | (той) „Хормони ли са?“ (тя) „Не. Не е хормонален пластир. Берберин, канела и нар.“ |
| 12–15.5 сек | Two-shot. Той присвива очи недоверчиво, тя отпива от кафето | „Не е лекарство.“ | (той) „И за какво е?“ (тя) „За жени като мен, които внимават какво ядат. Не е лекарство.“ |
| 15.5–19 сек | Близък план на масата: тя изважда 4 пакета от плика и ги нарежда. На „Трийсет“ вдига един, в края ги избутва от кадъра | „1 пакет 14.99 € + доставка · 30 лепенки“ / „3+1 подарък 39.99 € · безплатна доставка“ | (той) „Колко даде?“ (тя) „Четиринайсет и деветдесет и девет плюс доставка. Трийсет лепенки.“ |
| 19–22 сек | Two-shot. Той с половин надежда, тя свива рамене. В кадъра няма храна | „Не е магия.“ | (той) „И помага ли?“ (тя) „Нищо няма да ти обещая. Не е магия.“ |
| 22–26 сек | Близък план на рамото: тя дръпва леко деколтето и лепва лепенката с едно движение, после оправя пуловера. Той се навежда да види. Кадърът свършва на покритото рамо | „сутрин · чиста кожа · на рамото“ / „не е хапче, не се гълта“ | (той) „И как се слага?“ (тя) „Сутрин, на рамото. Не е хапче.“ (той) „Толкова ли?“ (тя) „Толкова.“ |
| 26–28.5 сек | Твърд срез към лицето ѝ, без J-cut. Пакетите и лепенката не са в кадър, на плота е само чашата | карта (бял фон, тъмен текст): „Лекарства, бременност, кърмене? Първо лекарят.“ | (тя) „При лекарства, бременност или кърмене — първо лекарят.“ |
| 28.5–32 сек | Two-shot. Той вади телефона си. Тя вдига вежди, после поглежда в камерата и посочва надолу | „Линкът е отдолу“ | (той) „Добре де. Прати ми линка.“ (тя) „Защо?“ (той) „За сестра ми.“ |

**Ако compliance не пусне реда за хормоните** (същият е в A18 и чака решение), сцената 8–12 сек става: (той) „И какво е това изобщо?“ (тя) „Лепенка. Берберин, канела и нар.“ Всичко друго остава.

**Текст под рекламата:**
„„Бер-бе-рин? Това пак някоя измама от интернет ли е?“
И аз така мислех. Затова платих чак като ги взех от Еконт.
„Хормони ли са?“ Не. Лепенка с берберин, канела и нар.
„И за какво е?“ За жени като мен, които внимават какво ядат. Не е лекарство.
„Колко даде?“ 1 пакет е 14.99 € + доставка, 30 лепенки. Аз взех 3+1 подарък за 39.99 € · безплатна доставка.
„И помага ли?“ Нищо няма да ти обещая. Не е магия.
Сутрин, на чиста и суха кожа, на рамото. Не е хапче.
При лекарства, бременност или кърмене — първо лекарят.
Линкът е отдолу.
*Видеото е драматизация. Лепенката не замества разнообразното хранене и движението.“
**Заглавия:** „Пак ли измама от интернет?“ · „Платих чак като ги взех от Еконт“ · „Най-скептичният вкъщи зададе 6 въпроса“. **CTA:** SEE_DETAILS, като родителя.

**Варианти за лабораторията:**
- **V-а** е основният, по-горе.
- **V-б е чист A/B срещу S3-30.** S3-30 се взима дума по дума, сменя се само кой пита: вместо приятелката на високоговорител в кадъра е съпругът и казва нейните реплики (в мъжки род, където трябва). Голямият надпис в hook-а става „Казах на най-скептичния човек вкъщи…“ вместо „…на най-скептичната си приятелка…“. Така разбираме дали печели „питащият е в кадъра и е мъж“, или само новите реплики на V-а.
- **V-в е без „Драматизация“.** Истинска двойка с писмено съгласие говори от свое име. Всичко, което казва тя, трябва да е вярно за нея: сама е поръчала и е платила на Еконт. Става само ако customer-care намери такава двойка.

**Къде и защо скалира (сигнал, сила B+):**
- **Motion, Skit** (сценаризирана мини история с актьори, продуктът е решението или поантата): най-много реклами имат Liven (wellbeing) 3K, Rise Science (сън) 2K, Speechify 2K, Motion 2K, Dr. Squatch 1K и WalkFit (ходене за жени 50+) 1K. Три от шестте са от здраве и wellness. Примери от здраве: Instant Hydration и AG1 (Хю Джакман в кухнята, съседите реагират). Hit rate за Skit Motion не публикува ([Skit](https://motionapp.com/library/formats/skit)).
- **Motion, WalkFit** (нашата аудитория): основно жени на 50–55+ с притеснения около менопаузата; 426 активни реклами, ≈192 нови на седмица. Скечовете им са диалози, в които едната жена е скептична („няма начин бавните движения да стегнат каквото и да е“), а другата отговаря ([WalkFit](https://motionapp.com/library/walkfit-daily-walking-plan)). Внимание: WalkFit ползва и обещания за кг и „15 години по-млада“. Тях не взимаме.
- **Съседни формати с двама при добавките:** Duet (две видеа едно до друго): MoonBrew 82 и Primal Queen 42 реклами ([Duet](https://motionapp.com/library/formats/duet)). Comment Response: 5 марки добавки. Arrae отговаря за страничните ефекти на GLP-1, а Dose на възражението за цената ([Comment Response](https://motionapp.com/library/formats/comment-response)). Podcast: „единият разказва, другият пита“ при Happy Mammoth, Primal Queen и Magic Mind ([Podcast](https://motionapp.com/library/formats/podcast)). В Health & Wellness Stitch и Reaction video са №1 и №2 по hit rate (VF-024), и двата са формати с двама души.
- **Лаб 08:59:** първите 3 места са с „друг човек пита“: A18 35.0, анкетата 33.0, A19 32.6. Член на семейството като питащ вече работи (A19). Съпругът е следващата стъпка.
- **NL, 03.10 (уеб):** в Нидерландия „лепенка в менопаузата“ значи естрадиол по рецепта (HST-pleisters, Systen). До тях се продават растителни лепенки за менопауза (Holistik, 39.95 € за 30). Въпросът „Хормони ли са?“ е истинско объркване на пазара, не измислено възражение. Това подкрепя реда от A18.

**Защо ще работи:** скептикът е най-трудният зрител. Съпругът, който пита „измама ли е?“, казва на глас съмнението на P-персоните, а тя отговаря спокойно и знае повече от него. Това е идентичност („аз съм тази, която провери“), не обещание. Ролите са обърнати спрямо основателя, който загуби: мъжът не обяснява, а пита. Hook-ът е смешен, без да е подигравателен, точно като „Бер-какво?“. Финалът „За сестра ми“ е социално доказателство вътре в семейството: дори скептикът праща линка.

**Как ще подейства:**
- **0–3.5 сек:** вижда семейна кухня, не реклама. Мъж срича „бер-бе-рин“ и пита „измама ли е?“. Усмихва се, защото и нейният мъж би казал същото, и спира.
- **3.5–8 сек:** „платих чак като ги взех от Еконт“ сваля страха от измама. Това е най-силният ред на S3-30.
- **8–22 сек:** 4 бързи въпроса с кратки отговори. Всеки въпрос е нов мини hook и държи задържането. „Не е хормонален пластир“ отговаря на въпроса на P02, P06 и P14. „Нищо няма да ти обещая“ сваля защитата.
- **22–26 сек:** „Толкова ли?“ – „Толкова.“ показва колко е лесно.
- **26–32 сек:** редът за лекаря, после скептикът сам иска линка. Това е разрешение за зрителката и тя кликва.

**Продукция:** 1 кухня, 2 души, телефон на буркан и 2 вмъквания. 1–1.5 часа, 0 кредита. Актьори или истинска двойка с писмено съгласие. За симулацията може AI (Kling/Veo), за Meta само истински запис (ред 18).
**Риск в Meta:** нисък до среден.
1. Той никога не коментира тялото, теглото, възрастта или външността ѝ: без „корем“, „отслабна ли“, „напълня“ (правилото на Meta за лични характеристики и образа на тялото).
2. „Драматизация“ през цялото видео. Вариант В го избягва.
3. Редът за хормоните чака compliance, както в A18. Резервният ред е готов.
4. Единственият ред за ефект е „Нищо няма да ти обещая. Не е магия.“ Без кг, срокове и „през кожата“.
5. Редът за лекаря е с твърд срез и без продукт в кадъра (ред 36, 43).
6. Казва се „от интернет“, не „от Фейсбук“: марка на Meta в текста на рекламата е излишен риск. Марката не напада други.
7. Хуморът не е за сметка на пола: той е внимателен, не глупав, а тя не е „жената, която купува глупости“.
8. Товарителницата на Еконт е покрита (лични данни).
**Ген за лаб смяната:** `visual_format` върху S3-30: V-а и V-б (CB-040).
**Статус:** в симулация (20261003-1512-active): V-а е №2 със SIM 37.4 и 73% срещу контролата; V-б (S3, пита съпругът) е №8 с 26.7. Печели целият скеч, не само смяната на питащия (CB-040).

---

### VF-027 „Пет бързи въпроса на улицата“ (интервюиращата не спира да пита, жената с пратката отговаря)
*Добавена на 03.10, 19:11, скаут AU (само уеб: конекторът meta_ads иска нов вход, Ads Library е недостъпна). Защо точно сега: на 15:11 уличната анкета (WILD, V4) е №1 със SIM 37.7, но губи зрителките точно там, където интервюиращата спира да пита. Задържането по сцени е 100% → 94% → 94% → 81% → 81% → **56%** → 56% → **38%** → 25% → 25%. Сцена 6 (18–21.5 сек) е първата, в която жената говори сама, без въпрос. VF-026, където въпросите вървят до края, държи 75% до 6-ата от 9 сцени. Урокът: печели човек, който отговаря на въпросите на друг човек в реална сцена. Щом диалогът стане монолог, зрителката си тръгва.*

**Какво е визуално:** видео 9:16, ≈30 сек, 1 улица, кадър от ръка. В кадъра е една жена, която отговаря. Интервюиращата се чува и се вижда само ръката ѝ с обикновения микрофон, до реда за лекаря.
- **Въпросите не спират.** На всеки 3–5 сек има нов въпрос. Никой отговор не е по-дълъг от 4 сек и никоя сцена не е монолог.
- **Брояч горе вляво:** „1/5“ … „5/5“, бял на тъмен фон, под горните 14%. Това е отворената примка: зрителката иска да стигне до 5/5. Числото е само брояч на въпросите, не оценка (без „5/5 ★“ и без „тест“; ред 74).
- **Hook-ът е предмет, не човек:** тя върви и разкъсва сивия плик от Еконт. Плик в ръката на жена на улицата всяка българка разпознава за 1 секунда, а въпросът „Какво си взе?“ е чисто любопитство.
- **Субтитри:** интервюиращата в жълто, жената в бяло. „Драматизация“ от първия до последния кадър. Долен надпис с марката „Реклама · FitPatches“ ≥ 30 px през цялото видео (ред 212). Без интерфейс на TikTok или Instagram.
- **Тя:** около 50 г., тъмна коса до раменете, бежов тренч върху светла блуза с широко деколте, платнена чанта. Спокойна, бърза, с чувство за хумор. Възрастта ѝ не се казва (ред 191).

| Време | 🎬 Кадър | 🖊 Надпис | 🎙 Глас |
|---|---|---|---|
| 0–3 сек (HOOK) | Улица (Пловдив, Капана), сутрин, кадър от ръка. Тя върви към камерата и разкъсва сивия плик от Еконт (товарителницата е покрита). Влиза ръката с микрофона. Тя спира и се засмива | голям надпис горе: „Какво си взе от Еконт?“ · брояч „1/5“ | (инт.) „Може ли един въпрос? Какво си взе от Еконт?“ (тя) „Лепенки.“ (инт.) „Лепенки?!“ |
| 3–7 сек | Тя вади пакета FitPatches наполовина от плика и го обръща с етикета към камерата (текстът на кутията се слага в монтажа) | „берберин · канела · нар · 30 в пакет“ · „2/5“ | (инт.) „Какви лепенки?“ (тя) „С берберин, канела и нар.“ |
| 7–11 сек | Среден план от гърдите нагоре, пакетът е в ръката ѝ под кадъра | едро: „За жени като мен, които внимават какво ядат.“ · по-дребно отдолу: „Не е лекарство.“ · „3/5“ | (инт.) „И за какво е?“ (тя) „За жени като мен, които внимават какво ядат. Не е лекарство.“ |
| 11–15.5 сек | Тя потупва плика с пакета вътре и се смее | „1 пакет 14.99 € + доставка · 30 лепенки“ / „плащаш при доставка“ · „4/5“ | (инт.) „Колко даде?“ (тя) „Четиринайсет и деветдесет и девет плюс доставката. И платих чак като ги взех.“ |
| 15.5–19 сек | Близък план на лицето. Тя свива рамене. Продукт няма в кадъра | „Не е магия.“ | (инт.) „И какво очакваш?“ (тя) „Нищо няма да ти обещая. Не е магия.“ |
| 19–23.5 сек | Тя дръпва леко яката на блузата: малката бежова лепенка е горе на рамото. Веднага оправя блузата. Кадърът свършва на покритото рамо | „сутрин · на рамото · не е хапче, не се гълта“ · „5/5“ | (инт.) „Последен: как се слага?“ (тя) „Сутрин, на рамото. С кафето. Толкова.“ |
| 23.5–27 сек | Твърд срез без J-cut: за първи път се вижда лицето на интервюиращата (около 35, дънково яке), с микрофона към себе си. Пакет и лепенка няма в кадъра | карта (бял фон, тъмен текст, без иконки): „При лекарства, бременност или кърмене — първо лекарят.“ | (инт., към камерата) „При лекарства, бременност или кърмене — първо лекарят.“ |
| 27–30 сек | Срез към жената, която вече се отдалечава с плика под мишница и маха през рамо. Продукт няма в кадъра | „линк отдолу“ · малък ред долу: „Не замества разнообразното хранене и движението.“ | (инт.) „Благодаря!“ (тя, през рамо) „Линкът е отдолу!“ |

**Текст под рекламата:**
„„Какво си взе от Еконт?“ — „Лепенки.“
1. Какви? С берберин, канела и нар. 30 в пакет.
2. За какво? За жени като мен, които внимават какво ядат. Не е лекарство.
3. Колко? 1 пакет 14.99 € + доставка. Платих чак като ги взех.
4. Какво да очакваш? Нищо няма да ти обещая. Не е магия.
5. Как се слага? Сутрин, на рамото. Не е хапче, не се гълта.
При лекарства, бременност или кърмене — първо лекарят.
Линкът е отдолу.
*Видеото е драматизация. Лепенката не замества разнообразното хранене и движението.“
**Заглавия:** „Какво си взе от Еконт?“ · „Пет въпроса. Пет кратки отговора.“ · „Платих чак като ги взех от Еконт“. **CTA:** SEE_DETAILS, като родителя.

**Варианти за лабораторията:**
- **V-а** е основният, по-горе: една жена, 5 въпроса, hook с плика.
- **V-б е чист A/B срещу WILD (V4, 37.7).** 0–13.5 сек са дума по дума като WILD: минувачките с „Бер-какво?“ и после „Аз я нося в момента.“. От 13.5 сек монологът става 4 въпроса на интервюиращата с брояча „2/5“…„5/5“: „Какво е?“, „За какво е?“, „Колко?“, „Как се слага?“. Отговорите са думите на WILD, разделени на парчета. Финалът с „Бер-бе-рин. Запомних го.“ остава. Сменя се само един ген: монолог → бързи въпроси. Така ще разберем дали спадът от 81% на 56% идва от монолога.
- **V-в е без „Драматизация“.** Истинска клиентка с писмено съгласие, заснета пред офиса, след като си вземе пратката. Всичко, което казва, трябва да е вярно за нея. Става само ако customer-care намери такава клиентка. Това е истинската сила на формата: Motion пише, че на уличната анкета се вярва, защото отговорите не са по сценарий.

**Къде и защо скалира (сигнал, сила B−):**
- **Motion, Street Interview:** 18 скорошни реклами от 17 марки. Финанси: Rocket Money, Chime, Joko, Brex, SoFi. Облекло: Allbirds, True Classic, Vessi. Красота: Glossier. **Здраве и добавки: BetterHelp, Cadence (електролити), Your Heights (витамини на капсули), Drink Magna.** Hook-овете са директен въпрос: „Can I ask you a question?“ (Vessi). Hit rate и разход няма ([Street Interview](https://motionapp.com/library/formats/street-interview)). Сигналът е широк (много категории), но малък по брой.
- **Лаб:** уличната анкета (WILD) е №2 на 08:59 (33.0) и №1 на 15:11 (37.7, 65% срещу контролата). Тя е най-силното тяло, което имаме днес. VF-027 поправя мястото, където губи (сцена 6).
- **Персоните искат точно тази поправка:** „Жена на моите години на улицата, не младо момиче.“ (P11, panel-F); „Нагласена анкета, а мен ме интересува…“ (panel-F); „Улична анкета, гледам за смях… После става реклама за жени.“ (panel-B). Във V-а жената е една, на тяхната възраст, а въпросите не позволяват „да стане реклама“.
- **AU, 03.10 (контекст, не сигнал за формата):** в Австралия TGA е свалил над 3 000 реклами за отслабване (2024–25) заради преди/след, отзиви с числа и лекарства с рецепта. Позволено остава да се говори за процеса, не за резултата ([AHCRA](https://www.ahcra.com.au/blog/tga-weight-loss-ads-removed-compliance/)). Петте въпроса са точно процесът: какво е, за какво е, колко струва, как се плаща, как се слага. Ред за резултат няма.
- Числото за брояча „1/5 … 5/5“ като механизъм за задържане **няма източник**. Това е хипотеза от нашата крива на задържане и я проверява V-б.

**Защо ще работи:** уличната анкета вече печели при нас, а VF-027 запазва силната ѝ част (непознат пита, тя знае отговора) и маха слабата (монолога). Пликът от Еконт в hook-а слага в първия кадър най-силния ни ред („платих чак като ги взех“). Петте въпроса са петте възражения на панела: какво е, за какво е, колко, ще стане ли чудо, сложно ли е. Всяко се сваля за 4 секунди.

**Как ще подейства:**
- **0–3 сек:** вижда жена на улицата, която разкъсва плик от Еконт. Това е и нейният ден, не реклама. „Какво си взе?“ е въпросът, който и тя би задала. Спира.
- **3–11 сек:** „1/5, 2/5, 3/5“: броячът ѝ казва, че ще е кратко и че има край. „За жени като мен, които внимават какво ядат“: разпознава се.
- **11–15.5 сек:** „платих чак като ги взех“: страхът от измама пада.
- **15.5–19 сек:** „Нищо няма да ти обещая. Не е магия.“: защитата срещу реклами пада, защото никой не ѝ продава чудо.
- **19–23.5 сек:** „Сутрин, на рамото. С кафето. Толкова.“: изглежда лесно. Стига 5/5 и чувства, че е разбрала всичко.
- **23.5–30 сек:** редът за лекаря от човек, който не продава, носи доверие. Жената си тръгва нормално, без натиск, и тя кликва сама.

**Продукция:** 1 улица, 2 души (в V-б и минувачките с писмено съгласие), телефон + обикновен микрофон без лого. 1–1.5 часа, 0 кредита. За симулацията може AI (Kling/Veo), за Meta само истински запис. Пликът е от истинска пратка; ако е постановъчен, най-долу стои „Демонстрация“ (ред 153).
**Трудност:** ниска.
**Риск в Meta:** нисък до среден.
1. Правилата за улична анкета (ред 212): „Драматизация“ върху цялото видео, долен надпис с марката ≥ 30 px, роли без имена, обикновен микрофон, без име на предаване, „на живо“, бадж или числа от анкетата. Задният план е размазан, а разпознаваемите минувачи са с писмено съгласие (GDPR).
2. Еконт: логото е само върху истинския плик като предмет, а фасадата и табелата на офиса не влизат в кадър (ред 163). Товарителницата е покрита (ред 76). Ако Еконт възрази, hook-ът става „Какво има в плика?“.
3. „Плащаш при доставка“: ако Еконт взима такса за наложен платеж от получателя, тя се казва до цената (ред 100, чака operations-manager).
4. „И какво очакваш?“ → дословно „Нищо няма да ти обещая. Не е магия.“ (ред 181 и решението от 15:11). Без „Помага ли?“ и „Действа ли?“.
5. „Не е лекарство.“ е само по-дребно под реда „за какво е“ и само защото редът за лекаря е в същото видео (ред 112, 113). Без „натурално“, „безопасно“ и „без странични ефекти“ до него.
6. Редът за лекаря: твърд срез, ≥ 0.5 сек само лице, без продукт в кадъра (ред 36, 43). След него няма „затова поръчах“, а само „Благодаря!“ и линк.
7. Без възраст, менопауза, корем, тегло и хормони. Лепенката е на рамото. Интервюиращата пита само за предмета, цената и плащането, никога за нея (решението от 15:11).
8. Броячът „5/5“ не стои сам като голям надпис и не е в кръг или звезда (ред 74). В последната сцена брояч няма.
**Ген за лаб смяната:** `visual_format` (V-а, нов формат) и чист A/B върху WILD (V-б, ген монолог → бързи въпроси).
**Статус:** нов (03.10, 19:11)

---

### VF-028 „Пратката в колата“ (майка и дъщеря в паркираната кола: двете лица в кадъра, реакция при отварянето)
*Добавена на 03.10, 23:11, скаут US (само уеб: конекторът meta_ads иска нов вход, Ads Library е недостъпна). Защо точно сега: на 19:11 печелят форматите, в които пита член на семейството. A19 „дъщеря ми пита“ е №1 с 38.7 (71% срещу контролата), VF-026 „скептикът вкъщи“ е №2 с 36.0. Форматите без лица губят дори с диалог: гласовите на сестра ми 28.4, комиксът 23.8. В A19 лицето на дъщерята не се вижда (POV, ред 210). VF-028 слага двете лица в един кадър и добавя момента, който Motion нарича Reaction video: човек вижда продукта за първи път пред камерата.*

**Какво е визуално:** видео 9:16, ≈31 сек, 1 локация, паркирана кола с изгасен двигател. Телефонът е на стойка на таблото с предната камера. Двете се виждат едновременно, рамо до рамо: дъщерята на шофьорското място, майката до нея. Това е кадърът „разговор в колата“, който всяка зрителка е виждала в стотици истински клипове.
- **Камерата не мърда.** Има само 2 смени: близък план на лепенката на пръста и твърдият срез към реда за лекаря.
- **Реакцията е към предмета, не към резултат:** „Това ли е? Толкова малка?“. Това е изненадата, която Motion описва като Reaction video („някой открива продукта за първи път пред камерата“).
- **Дъщерята пита, майката знае.** Дъщерята е видимо пълнолетна: около 25–30, тя кара колата и държи ключовете. Няма училище, раница или детски глас. Не говори за храна и тяло, не ползва и не иска продукта.
- **Майката:** около 50, къса тъмна коса, светъл пуловер с широко деколте. Възрастта не се казва (ред 191).
- **Субтитри:** дъщерята в жълто, майката в бяло. „Драматизация“ от първия до последния кадър, под горните 14%. Без интерфейс на TikTok или Instagram.
- **През стъклата** се вижда размазана улица. Фасадата и табелата на офиса на Еконт не влизат в кадър (ред 163).

| Време | 🎬 Кадър | 🖊 Надпис | 🎙 Глас |
|---|---|---|---|
| 0–3 сек (HOOK) | Двете в колата, кадър от таблото. Майката вече разкъсва сивия плик от Еконт в скута си (товарителницата е покрита с бял стикер). Дъщерята се обръща към нея с ключовете в ръка | голям надпис горе: „Закарах мама до Еконт. Отвори го още в колата.“ · субтитри | (дъщерята) „Мамо, за това ли те карах до Еконт? Какво е това?“ (майката, без да вдига поглед) „Лепенки.“ (дъщерята) „Лепенки?!“ |
| 3–7 сек | Майката вади пакета FitPatches. Дъщерята го взима от ръката ѝ и го чете отблизо (текстът на кутията се слага в монтажа) | „берберин · канела · нар · 30 в пакет“ | (дъщерята, сричайки) „Бер… бер-бе-рин?“ (майката) „Берберин, канела и нар.“ |
| 7–11 сек | Two-shot. Дъщерята вдига вежди. Майката потупва плика | „Плащаш при доставка“ | (дъщерята) „Това не е ли поредната измама от интернет?“ (майката) „И аз така мислех. Затова платих чак като ги взех.“ |
| 11–14.5 сек | Two-shot. Дъщерята връща пакета | едро: „За жени като мен, които внимават какво ядат.“ · по-дребно отдолу: „Не е лекарство.“ | (дъщерята) „И за какво е?“ (майката) „За жени като мен, които внимават какво ядат. Не е лекарство.“ |
| 14.5–18 сек | Two-shot. Майката обръща пакета към дъщерята | „1 пакет 14.99 € + доставка · 30 лепенки“ | (дъщерята) „Колко даде?“ (майката) „Четиринайсет и деветдесет и девет плюс доставка. Трийсет лепенки.“ |
| 18–23 сек (РЕАКЦИЯТА) | Майката отваря пакета и вади една лепенка. Близък план: лепенката на върха на пръста ѝ, до камерата. Обратно в two-shot: дъщерята се навежда към нея с широко отворени очи. Майката дръпва леко деколтето, лепва лепенката горе на рамото с едно движение и оправя пуловера. Кадърът свършва на покритото рамо | „сутрин · на рамото · не е хапче, не се гълта“ | (дъщерята) „Това ли е? Толкова малка?“ (майката) „Толкова. Сутрин, на рамото. Не е хапче.“ |
| 23–25.5 сек | Two-shot. Майката свива рамене. Дъщерята гледа през стъклото и не реагира | „Не е магия.“ | (дъщерята) „И какво очакваш?“ (майката) „Нищо няма да ти обещая. Не е магия.“ |
| 25.5–28 сек | Твърд срез без J-cut: само лицето на майката, дъщерята е извън кадъра. Пакет и лепенка няма в кадъра | карта (бял фон, тъмен текст, без иконки): „При лекарства, бременност или кърмене — първо лекарят.“ | (майката) „При лекарства, бременност или кърмене — първо лекарят.“ |
| 28–31 сек | Two-shot. Дъщерята посяга към телефона на таблото | „Линкът е отдолу“ · малък ред долу: „Не замества разнообразното хранене и движението.“ | (дъщерята) „Добре де. Поне не плащаш, преди да дойде. Ще те кача.“ (майката, към камерата) „Щом ще ме качваш — линкът е отдолу.“ |

**Текст под рекламата:**
„„Мамо, за това ли те карах до Еконт?“ — „Лепенки.“
Берберин, канела и нар. 30 в пакет.
„Това не е ли поредната измама от интернет?“ И аз така мислех. Затова платих чак като ги взех.
„И за какво е?“ За жени като мен, които внимават какво ядат. Не е лекарство.
„Колко даде?“ 1 пакет е 14.99 € + доставка, 30 лепенки. Има и 3+1 подарък за 39.99 € · безплатна доставка.
„Това ли е? Толкова малка?“ Толкова. Сутрин, на чиста и суха кожа, на рамото. Не е хапче.
„И какво очакваш?“ Нищо няма да ти обещая. Не е магия.
При лекарства, бременност или кърмене — първо лекарят.
Линкът е отдолу.
*Видеото е драматизация. Лепенката не замества разнообразното хранене и движението.“
**Заглавия:** „Закарах мама до Еконт“ · „Отвори го още в колата“ · „Платих чак като ги взех“. **CTA:** SEE_DETAILS, като родителя.

**Варианти за лабораторията:**
- **V-а** е основният, по-горе: пълнолетна дъщеря, двете лица в кадъра, реакцията при отварянето. **Чака compliance:** ред 210 днес казва за дъщерята „без лице и възраст“. Правилото е писано за A19, където дъщерята звучи като тийнейджърка. Нужно е решение дали видимо пълнолетна дъщеря (кара колата, около 25–30) може да е с лице в кадъра.
- **V-б е със сестрата вместо дъщерята** и минава по сегашните правила. Репликите са същите: „Мамо, за това ли те карах…“ става „Сестро, за това ли те карах…“, а hook-ът става „Закарах сестра си до Еконт…“. Това е и чист тест на урока от 19:11: сестрата, която в гласовите съобщения губи (28.4), сега е с лице в кадъра.
- **V-в е чист A/B срещу A19** (контролата от 23:11). A19 остава дума по дума, в същата кухня. Сменя се само кадърът: POV от телефона на дъщерята (лицето ѝ не се вижда) → предна камера с двете лица. Така разбираме дали лицето на питащата добавя нещо над A19. Чака същото решение по ред 210 като V-а.

**Къде и защо скалира (сигнал, сила B+):**
- **Motion, Creative Benchmarks 2026:** в Health & Wellness Reaction video е №2 по hit rate (11.24) след Stitch (12.50). Числата са взети на 02.10 от извадка от 550 000+ реклами на 6 000+ рекламодатели, IX.2025–I.2026 ([thumbstop-pulse](https://motionapp.com/thumbstop-pulse/creative-benchmarks-2026/), VF-024).
- **Motion, Reaction video** (проверено на 03.10, 23:11): определението е „някой открива продукта за първи път пред камерата“, а един от примерите е „двама приятели си разменят глътки в паркирана кола“. Най-много реклами имат Hismile 703, Zeely 387, BOTB 162 и Mixtiles 118. От добавките е Spacegoods. Число за подвида „майка и дъщеря в колата“ няма ([Reaction video](https://motionapp.com/library/formats/reaction-video)).
- **US, GLP-1 добавки с двама в кадъра:** Bioma (459 активни реклами, ≈111 нови на седмица) има двойка („She noticed“) и подкаст с експерт. Двойката им е преди/след и „жена му забеляза“, затова от тях взимаме само идеята за двама в кадъра, не съдържанието ([Bioma](https://motionapp.com/library/bioma-health)). Lemme (266 активни, ≈62 нови на седмица) в извадката няма формати с двама ([Lemme](https://motionapp.com/library/lemme)).
- **Лаб 19:11:** семейството пита и печели: A19 38.7, VF-026 36.0, A22 „майка ми пита“ 31.8. Без лица губи: гласовите 28.4, комиксът 23.8. Цитат от A19: P07 „Е, това съм аз сутрин — и моята щерка така ме снима и се заяжда.“
- **Число за „майка и дъщеря“ в рекламите за добавки няма.** Търсенето на 03.10 не върна нито един пример от категорията.

**Защо ще работи:** взима най-силния ни ъгъл (A19: дъщерята скептик, 38.7) и му добавя двете неща, които A19 няма. Първото са лицата, урокът от 19:11. Второто е реакцията към предмета: Reaction е №2 по hit rate в Health & Wellness. Разговорът в колата е най-честият кадър в истинските клипове, затова рекламата изглежда като видео от семейния чат. Пликът от Еконт и „платих чак като ги взех“ са в първите 11 секунди. „Толкова малка?“ сваля възражението „сложно е“, без да обещава нищо.

**Как ще подейства:**
- **0–3 сек:** вижда майка и дъщеря в кола и плик от Еконт. Това е и нейният живот: пратката и детето, което я кара. „За това ли те карах?“ е смешно. Спира.
- **3–11 сек:** „Бер-бе-рин?“ и „измама от интернет“ казват на глас нейното съмнение. „Платих чак като ги взех“ го сваля.
- **11–18 сек:** за какво е и колко струва. Разпознава се в „жени като мен“, а цената е ясна заедно с доставката.
- **18–23 сек:** реакцията „Толкова малка?“ е моментът, заради който гледа. Вижда истинската лепенка и колко лесно се слага.
- **23–28 сек:** „Нищо няма да ти обещая“ и редът за лекаря. Никой не ѝ продава чудо, затова вярва.
- **28–31 сек:** скептичката дъщеря сама казва „поне не плащаш, преди да дойде“. Това е разрешение и зрителката кликва.

**Продукция:** 1 кола (паркирана, с изгасен двигател), 2 актриси или истински майка и дъщеря с писмено съгласие, телефон на стойка, 1 истински плик от Еконт. ≈1 час, 0 кредита. За симулацията може AI (Kling/Veo), за Meta само истински запис (ред 18). Ако пликът е постановъчен, най-долу стои „Демонстрация“ (ред 153).
**Трудност:** ниска.
**Риск в Meta:** нисък до среден.
1. **Ред 210:** дъщерята е пълнолетна и изглежда пълнолетна (кара колата). Без училище, раница, „тийнейджърка“ и детски глас. Не говори за храна и тяло, не ползва и не иска продукта. Лицето ѝ в кадъра е ново спрямо A19, затова решава compliance-officer. Докато няма решение, V-б със сестрата е резервата.
2. **Ред 225 по аналогия:** на „Не е магия“ дъщерята не кима и не реагира. Във видеото няма ред за ефект (шкафа, шоколада).
3. Реакцията е към размера и към това, че се слага лесно, никога към резултат: без „уау, работи“, без огледало, без поглед към тялото.
4. „Драматизация“ през цялото видео; при AI „Драматизация · създадено с AI“.
5. **Еконт:** само истинският плик като предмет, без фасада и табела (ред 163). Товарителницата е покрита (ред 76). Ако Еконт възрази, hook-ът става „Мамо, за това ли те карах до офиса?“.
6. Казва се „от интернет“, не „от TikTok“ (ред 209).
7. Колата е паркирана с изгасен двигател. Никой не шофира, докато снима.
8. Без възраст, менопауза, корем, тегло и хормони. Лепенката е на рамото. Редът за лекаря е с твърд срез и без продукт в кадъра (ред 36, 43).
9. „Не е лекарство.“ стои само по-дребно под реда „за какво е“ и само защото редът за лекаря е в същото видео (ред 112, 113).
**Ген за лаб смяната:** `visual_format` върху A19 (контролата от 23:11). V-а е новият формат, а V-в е чист A/B „POV → двете лица“. V-б е резервата и тест „с лице срещу гласово“ при сестрата.
**Статус:** нов (03.10, 23:11)

### VF-029 „Разпит на разходката“ (walk-and-talk: двамата вървят един до друг, селфи two-shot в движение; мъжът пита, тя отговаря)
*Добавена на 04.10, 03:11, скаут PL (само уеб: конекторът meta_ads иска нов вход, Ads Library е недостъпна). Защо точно сега: на 23:11 (`20261003-2312-active`) VF-026 „скептикът вкъщи“ е №1 с 36.2 (66% срещу A19), A19 „дъщеря ми пита“ е №2 с 35.2. Губят монологът (ad1 24.6) и статичният чат на победителя (VF-011 23.6, 0% срещу контролата). Скептикът вкъщи вече е контрола, но задържането му пада във втората половина: 69% → 50% на „И какво очакваш?“ и 44% на финала. VF-029 държи печелившото (мъжът пита, двете лица в кадъра) и сменя само кадъра: статичната кухня става разходка, в която фонът се мени всяка секунда. В PL формат с двама не е видян (няма данни), затова сигналът е от света.*

**Какво е визуално:** видео 9:16, ≈29 сек, 1 локация: алея в парка през есента, следобед. Двамата вървят към камерата рамо до рамо. Той държи телефона на една ръка, с предната камера, и кадърът е от гърдите нагоре. Лекото клатене от ходенето остава, защото така изглеждат истинските клипове „на разходка“.
- **Движи се само фонът:** листа, пейки, размазана алея. Лицата са в един и същ кадър през цялото видео. Има 1 смяна: твърд срез, когато спират, за реда за лекаря.
- **Той пита, тя знае.** Съпругът е на около 55, с яке и без спортен екип. Пита само за предмета, цената и плащането (ред 226) и никога не обяснява. Тя е на около 50, с плетена жилетка и шал, и държи чаша кафе за вкъщи. Отговаря кратко и с усмивка.
- **Хуморът е в hook-а** („Сега няма къде да избягаш.“) и в „Бер-бе-рин. Звучи като бразилски футболист.“ Финалът е топъл: „Още една обиколка?“
- **Лепенката се вижда в 3-тата секунда:** тя дръпва за 1 секунда яката на жилетката и я показва горе на рамото. В PL купувачките пишат, че лепенките са „по-малки, отколкото очаквах“ (Allegro, 04.10), затова истинският размер се показва още в началото, а не в пакета у дома.
- **Субтитри:** той в жълто, тя в бяло. Надписът „Драматизация“ стои от първия до последния кадър, под горните 14%. Без интерфейс на TikTok или Instagram.
- **Без спорт:** няма крачкомер, смарт часовник, клин, пот или „км“. Това е разходка с кафе, не тренировка.

| Време | 🎬 Кадър | 🖊 Надпис | 🎙 Глас |
|---|---|---|---|
| 0–3 сек (HOOK) | Алея в парка, есен. Двамата вървят към камерата, той я гледа отстрани и се полуусмихва. Тя е с чаша кафе | голям надпис горе: „Мъжът ми ме разпита на разходката.“ · субтитри | (той) „Добре. Сега няма къде да избягаш. Какво е това, дето го лепиш всяка сутрин?“ (тя, смее се) „Лепенка.“ |
| 3–7 сек | Вървят. Тя дръпва за 1 секунда яката на жилетката встрани: лепенката се вижда горе на рамото. После оправя жилетката. Кадърът остава от гърдите нагоре | „лепенка · берберин · канела · нар“ | (тя) „Берберин, канела и нар. Ето я.“ (той) „Бер-бе-рин. Звучи като бразилски футболист.“ (тя) „Звучи. Не е.“ |
| 7–11 сек | Вървят. Тя отпива от кафето, той вдига вежди | „Плащаш при доставка“ | (той) „От интернет ли? Да не е някоя измама?“ (тя) „Затова платих чак като ги взех от Еконт.“ |
| 11–14.5 сек | Вървят. Той поглежда към нея | „1 пакет 14.99 € + доставка · 30 лепенки“ | (той) „И колко даде?“ (тя) „Четиринайсет и деветдесет и девет плюс доставка. Трийсет лепенки.“ |
| 14.5–18.5 сек | Вървят по-бавно, падат листа. Той пита, като гледа напред | едро: „За жени като мен, които внимават какво ядат.“ · по-дребно отдолу: „Не е лекарство.“ | (той) „И за какво е?“ (тя) „За жени като мен, които внимават какво ядат. Не е лекарство.“ |
| 18.5–22 сек | Вървят. Тя свива рамене. Той гледа напред по алеята и не реагира | „Не е магия.“ | (той) „И какво очакваш?“ (тя) „Нищо няма да ти обещая. Не е магия.“ |
| 22–25 сек | Твърд срез без J-cut: спрели са. Само лицето ѝ, кадърът е неподвижен, той е извън кадъра. В кадъра няма пакет и лепенка | карта (бял фон, тъмен текст, без иконки): „При лекарства, бременност или кърмене — първо лекарят.“ | (тя) „При лекарства, бременност или кърмене — първо лекарят.“ |
| 25–29 сек | Two-shot. Тръгват отново, той се обръща към нея | „Линкът е отдолу“ · малък ред долу: „Не замества разнообразното хранене и движението.“ | (той) „Добре де. Поне плащаш, като дойдат. Още една обиколка?“ (тя, към камерата) „Още една. Линкът е отдолу.“ |

**Текст под рекламата:**
„„Добре. Сега няма къде да избягаш. Какво е това, дето го лепиш всяка сутрин?“ — „Лепенка.“
Берберин, канела и нар. 30 в пакет.
„От интернет ли? Да не е някоя измама?“ Затова платих чак като ги взех от Еконт.
„И колко даде?“ 1 пакет е 14.99 € + доставка, 30 лепенки. Има и 3+1 подарък за 39.99 € · безплатна доставка.
„И за какво е?“ За жени като мен, които внимават какво ядат. Не е лекарство.
„И какво очакваш?“ Нищо няма да ти обещая. Не е магия.
Всяка сутрин една, на чиста и суха кожа, на рамото. Не е хапче.
При лекарства, бременност или кърмене — първо лекарят.
Линкът е отдолу.
*Видеото е драматизация. Лепенката не замества разнообразното хранене и движението.“
**Заглавия:** „Мъжът ми ме разпита на разходката“ · „Платих чак като ги взех“ · „Нищо няма да ти обещая“. **CTA:** SEE_DETAILS, като родителя.

**Варианти за лабораторията:**
- **V-а** е основният, по-горе: съпругът, ново тяло и без разговор за хормоните. Минава по сегашните правила и не чака юрист (ред 192 не важи).
- **V-б е чист A/B срещу VF-026** (контролата в 03:11). Скриптът на VF-026 остава дума по дума, вкл. обмена „хормонален пластир“ и реда на сцените. Сменя се само кадърът: статична камера на буркан в кухнята → селфи two-shot на разходка. Двете вмъквания стават: рамото (яката на жилетката) и пакетът, който тя вади от плика от Еконт в ръката си, вместо 4 пакета на масата. Така разбираме дали движението в кадъра задържа втората половина (69% → 44% при VF-026). Това е лостът на Ready Set „същият победител, нов кадър“. Юрист преди Meta, както при VF-026 (ред 192).
- **V-в е с пълнолетна дъщеря** (около 25–30), хванала майка си под ръка. Дъщерята държи телефона, репликите са от V-а, а „Мъжът ми“ става „Дъщеря ми“. Без разговор за хормоните (ред 281). Чака същото решение по ред 210 като VF-028 V-а: може ли видимо пълнолетна дъщеря да е с лице в кадъра.

**Къде и защо скалира (сигнал, сила B):**
- **WalkFit (US, ходене за жени 50+), Motion:** 426 активни реклами, ≈192 нови на седмица. Рекламите с двама са заснети като „two-shot walking sequences“ и разговорни статични кадри. Едната жена казва съмнението си („The guilt is exhausting. So what am I supposed to do on the days I'm stuck home?“), другата отговаря. Разпределение по формати: Demo 18%, Before and After 12%, Expert Explainer 9%. Данните на страницата са обновени „преди 4 месеца“ (≈VI.2026). Взимаме само кадъра. Преди/след и „баса“ с резултат („sister asked if I lost 20 pounds“) не взимаме ([WalkFit](https://motionapp.com/library/walkfit-daily-walking-plan), проверено на 04.10).
- **Motion, Ready Set (Sophia Beauvoir, Creative Strategy Bootcamp, юни 2026):** лостът „talent refresh“. Печеливша реклама с двойка е заснета наново със същия кадър и послание, но с нова двойка, и е дала нов топ резултат: „We recreated the ad with new talent and just secured a new top performer really easily“. Примерът е Earnest (студентски кредити), не здраве ([Motion](https://motionapp.com/library/talk/scaling-ugc-ads-post-andromeda-one-winner-many-formats/)).
- **Motion Skit** (VF-026): Liven 3K, Rise Science 2K, WalkFit 1K реклами.
- **Motion, индекс на форматите (04.10):** освен Street Interview, Duet, Stitch и Comment Response няма отделен формат с двама в разговор ([formats](https://motionapp.com/library/formats)). Тоест „разходка с двама“ е подвид на Skit, а не отделна категория с бенчмарк.
- **Лаб 23:11:** мъжът пита: 36.2 (№1); дъщерята: 35.2; сестрата с лице: 31.4; свекървата: 29.7; майката: 27.6. Цитат от VF-026: N07 „Ха, мъжът ѝ срича „бер-бе-рин“ и пита дали е измама — точно моят!“
- **Число за „разходка с двама“ в рекламите за добавки няма.** В PL формат с двама не е видян (няма данни: креативите не се виждат без Ads Library).

**Защо ще работи:** взима победителя (VF-026: скептикът е мъжът ѝ, №1 с 36.2) и сменя само мястото. Разходката е най-естественото място, където двама си говорят и единият снима. WalkFit снима точно така рекламите си с двама за жени 50+. Фонът, който се сменя всяка секунда, е хипотеза за задържането във втората половина, където VF-026 губи 25 п.п. Редът „Не замества разнообразното хранене и движението“ престава да е бележка под линия: тя върви, докато го чете. V-а е без разговор за хормоните, затова минава към Meta без юрист. Лепенката се вижда в 3-тата секунда, така че никой не остава изненадан от размера при доставката (оплакването от PL).

**Как ще подейства:**
- **0–3 сек:** вижда двойка на разходка, кадър като от семейния телефон, не реклама. „Сега няма къде да избягаш“ е смешно и обещава разпит. Спира.
- **3–7 сек:** за секунда вижда истинската лепенка на рамото и чува съставките. „Бразилски футболист“ я разсмива и тя остава.
- **7–14.5 сек:** мъжът казва на глас нейното съмнение („измама?“). „Платих чак като ги взех“ го сваля, после идва цената с доставката.
- **14.5–22 сек:** разпознава се в „жени като мен“. „Нищо няма да ти обещая“ значи, че никой не ѝ продава чудо.
- **22–25 сек:** двамата спират и идва редът за лекаря. Сериозният момент носи доверие.
- **25–29 сек:** скептикът одобрява само плащането, а „Още една обиколка?“ дава топъл финал. Тя кликва на линка.

**Продукция:** 2 души (актьори или истинска двойка с писмено съгласие), 1 телефон (по желание гимбал), 2 петлични микрофона заради вятъра, алея в парка без разпознаваеми минувачи (размазан фон; ако минувачите се разпознават, трябва им писмено съгласие). ≈1–1.5 часа, 0 кредита. За симулацията може AI (Kling/Veo), но ходенето в AI трудно държи лицата и ръцете еднакви. За Meta само истински запис (ред 18).
**Трудност:** ниска (на живо); средна при AI.
**Риск в Meta:** нисък до среден.
1. **Ред 226:** мъжът пита само за предмета, цената и плащането. Не коментира тялото, възрастта, храненето ѝ, не ползва и не иска продукта.
2. **Ред 226, втората част (кимане):** на „Не е магия“ той гледа напред и не реагира. Във видеото няма ред за ефект.
3. **Тяло (ред 228 по аналогия):** кадърът е от гърдите нагоре, дрехите са свободни. Без кадри в цял ръст, отзад или в профил. Яката се дръпва само на рамото, за 1 секунда.
4. **Движение без фитнес (ред 21, 47):** без спортен екип, крачкомер, часовник, „км“, „стъпки“ и пот. Разходката е фон, не начин за отслабване. Редът „Не замества разнообразното хранене и движението.“ е на екрана и в текста.
5. „Драматизация“ през цялото видео; при AI „Драматизация · създадено с AI“.
6. „Не е лекарство.“ стои само по-дребно под реда „за какво е“ и само защото редът за лекаря е в същото видео (ред 112, 113). Редът за лекаря идва след твърд срез и без продукт в кадъра (ред 36, 43).
7. Казва се „от интернет“, не „от TikTok“ (ред 209). Еконт е само като дума; в V-б пликът е истински, а товарителницата е покрита (ред 76, 164).
8. **V-б** носи обмена „хормонален пластир“ от VF-026, затова там важат ред 185–192 (юрист преди Meta), както при контролата. **V-в** е без хормони (ред 281) и чака ред 210.
9. Който държи телефона, върви по алея, не до улица с коли.
**Ген за лаб смяната:** `visual_format` върху VF-026 (контролата в 03:11). V-б е чист A/B „статична кухня → разходка в движение“. V-а е новият формат с ново тяло. V-в се пуска след решението по ред 210.
**Статус:** губещ в симулация (`20261004-0312-active`): разходката с двамата в кадър е последна, 24.3 (8%). Движещият се фон и бързото темпо губят, а статичната кухня бие всички. Наследник е VF-031 (статичен two-shot, 04.10, 07:11)

---

### VF-030 „Реакцията на фризьорката“ (Reaction + Demo във фризьорския стол: двете лица фронтално, несемеен питащ)
*Добавена на 04.10, 07:11, от creative-strategist (Ads Library: 0 заявки, конекторът meta_ads иска нов вход). Защо точно сега: собственикът иска нов визуален формат с две реални лица, но без семейство и без медицинско лице. На 03:11 в рунда имаше 6 семейни скеча от 10 и панелът се умори (A19 38.7 → 30.8). Контролата VF-026 губи жените, които „мъж вкъщи нямат“ (P02, P07, P10, N03 на A11). Reaction video е №2 по hit rate в Health & Wellness, а при нас е тестван само в кола и със семейство (VF-028). A17 доказа салона при 50+ (35.7 → 34.7), но там фризьорката беше само ръце и глас. Сестра на VF-031 (подкастът на дивана, скаут GB): и двете са несемейни, статични, с две лица. VF-031 е интервю, а VF-030 е реакция към предмета.*

**Какво е визуално:** видео 9:16 (+ изрязване 4:5), 34.5 сек, 1 локация: квартален фризьорски салон, делник сутрин, без други клиентки, без име и лого на салона.
- **Камерата е статична.** Телефонът е подпрян на флакон лак на плота пред огледалото, а огледалото е зад него и не влиза в кадъра. Има само 1 с вмъкване (пръстите с лепенката) и 1 кроп (лицето за реда за лекаря).
- **Двете лица са фронтално едновременно.** И двете гледат към огледалото, тоест към камерата: героинята седи на стола долу вляво, фризьорката стои зад нея горе вдясно. В кухнята на VF-026 лицата са в три четвърти, в колата на VF-028 в профил. Тук всяка реакция се чете без звук.
- **Пелерината закрива тялото до врата.** Кадърът е от кръста нагоре, но тялото не се вижда. Кадър под гърдите и жест към кръста просто няма.
- **Фризьорката пита и реагира, героинята знае.** Двете изглеждат на около 50. Фризьорката е с очила на верижка и черна престилка. Пита само за предмета, плащането, размера, мястото, целта, цената и очакванията. Реагира с вежди, присвити очи и бавно кимане. Никога не коментира вида, прическата, тялото или храненето ѝ.
- **Реакцията е към предмета (Demo), не към резултат:** лепенката срещу светлината, „Толкова малка?“. Така зрителката вижда истинския размер преди поръчката (в PL оплакването в Allegro е „по-малки, отколкото очаквах“).
- **Хуморът е от професията ѝ:** „Бер-бе-рин? Това нова боя ли е?“ и във финала, по срички: „Бер-бе-рин. Не е боя.“
- **Субтитри:** фризьорката в жълто, героинята в бяло. „Драматизация“ стои от първия до последния кадър (при AI: „Драматизация · създадено с AI“). Без интерфейс на TikTok или Instagram.
- **Без преди/след с прическата:** косата е мокра до края, столът не се върти и никой не се оглежда в огледалото.

| Време | 🎬 Кадър | 🖊 Надпис | 🎙 Глас |
|---|---|---|---|
| 0–3.5 сек (HOOK) | Two-shot в стола. Героинята държи разкъсания плик от Еконт на нивото на гърдите (товарителницата е покрита с бял стикер). Фризьорката вече държи пакета, слага очилата, отдалечава кутията на една ръка разстояние и вдига вежди към огледалото. Героинята се смее | голям надпис горе вляво, без да покрива лицата: „Фризьорката реши, че е боя за коса.“ · субтитри | (фризьорката) „Бер-бе-рин? Това нова боя ли е?“ |
| 3.5–6.5 сек | Two-shot. Героинята клати глава през смях, фризьорката присвива очи към кутията | „лепенка · берберин · канела · нар“ | (тя) „Не е боя. Лепенка. Берберин, канела и нар.“ |
| 6.5–10 сек | Two-shot. Фризьорката почуква плика с кутията и я гледа над очилата, после бавно кимва | „Плащаш при доставка“ | (фризьорката) „От интернет? Плати ли вече?“ (тя) „Не. Чак в Еконт, като го взех.“ |
| 10–13.5 сек (РЕАКЦИЯТА) | Фризьорката вади 1 лепенка и я вдига срещу светлината. 1 с вмъкване само на пръстите с лепенката, без тяло. Обратно в two-shot: широко отворени очи. Прибира лепенката в кутията, кутията в плика и оставя плика на рафта, извън кадъра | едро, в жълто: „Толкова малка?“ · по-дребно: „30 лепенки в пакет“ | (фризьорката) „Толкова малка?“ (тя) „Толкова.“ (фризьорката) „Дай го тук, че ще пръскам.“ |
| 13.5–17 сек | Същият two-shot, без вмъкване. Героинята с дясната ръка отмества встрани пелерината и яката от лявото рамо за 1 с, а лявата ръка е отпусната на подлакътника. Фризьорката гледа лицето ѝ. Свършва на покритото рамо и лицата | „1 лепенка сутрин · на рамото“ / „не е хапче · не се гълта“ | (фризьорката) „И къде я слагаш?“ (тя) „Тук, на рамото. Всяка сутрин една.“ |
| 17–21.5 сек | Two-shot. Фризьорката пръска косата с вода и реше. Продукт няма | едро: „За жени като мен, които внимават какво ядат.“ · по-дребно: „Не е лекарство.“ | (фризьорката) „И за какво е?“ (тя) „За жени като мен, които внимават какво ядат. Не е лекарство.“ |
| 21.5–25 сек | Two-shot. Гребенът спира във въздуха, после „аха“ с вежди. Продукт няма | „1 пакет 14.99 € + доставка“ / „30 лепенки“ / „3+1 подарък 39.99 € · безплатна доставка“ | (фризьорката) „И колко струва?“ (тя) „Четиринайсет и деветдесет и девет евро плюс доставка.“ |
| 25–28 сек | Two-shot. Фризьорката опира ръце на облегалката и я гледа над очилата. Героинята свива рамене. Фризьорката кимва бавно, без думи | „Не е магия.“ | (фризьорката) „И какво очакваш?“ (тя) „Нищо няма да ти обещая. Не е магия.“ |
| 28–30.5 сек | Твърд срез без J-cut: само лицето на героинята. Фризьорка, пакет и лепенка няма | карта (бял фон, тъмен текст, без икони): „При лекарства, бременност или кърмене — първо лекарят.“ | (тя) „При лекарства, бременност или кърмене — първо лекарят.“ |
| 30.5–34.5 сек | Two-shot. Фризьорката подава визитка на салона (с гърба към камерата) и химикал. Героинята пише, фризьорката чете по срички и се смее. Героинята поглежда в обектива и посочва надолу. Продукт няма | „Линкът е отдолу“ · малък ред (≥ 30 px): „Не замества разнообразното хранене и движението.“ | (фризьорката) „Е, поне се плаща на гишето. Запиши ми го.“ … „Бер-бе-рин. Не е боя.“ |

**Текст под рекламата (кратък):**
„„Бер-бе-рин? Това нова боя ли е?“
Фризьорката ми видя кутията, докато ми слагаше пелерината.
Не е боя. Лепенка с берберин, канела и нар. 30 в пакет.
Всяка сутрин една, на рамото. Не е хапче, не се гълта.
Платих чак в Еконт, като взех пратката.
1 пакет е 14.99 € + доставка.
При лекарства, бременност или кърмене — първо лекарят.
Линкът е отдолу.
*Видеото е драматизация. Лепенката не замества разнообразното хранене и движението.“
Дългият текст (целият диалог) е в `team/lab/runs/20261004-0712-active/drafts/strategist.json`.
**Заглавия:** „Фризьорката реши, че е боя за коса“ · „Не е боя. Лепенка с берберин.“ · „Платих чак в Еконт, като взех пратката“. **CTA:** SEE_DETAILS.

**Къде и защо скалира (сигнал, сила B+):**
- **Motion, Creative Benchmarks 2026 по вертикали:** в Health & Wellness Reaction video е №2 по hit rate (11.24), след Stitch (12.50). Числата са взети на 02.10, а извадката е 550 000+ реклами ([visual-formats-by-vertical](https://motionapp.com/library/research/creative-benchmarks-2026/visual-formats-by-vertical), [thumbstop-pulse](https://motionapp.com/thumbstop-pulse/creative-benchmarks-2026/)).
- **Motion, Reaction video:** Hismile 703 реклами, Dr. Squatch 95, Clean Skin Club 86, Spacegoods (добавки). Най-често се съчетава с Demo (36%), Testimonial (21%) и ASMR (21%) ([Reaction video](https://motionapp.com/library/formats/reaction-video)).
- **Motion, Skit и WalkFit:** WalkFit (жени 50+) има 426 активни реклами и ≈192 нови на седмица. Рекламите с двама са диалози на две жени, от които едната е скептична ([WalkFit](https://motionapp.com/library/walkfit-daily-walking-plan), [Skit](https://motionapp.com/library/formats/skit)).
- **Лаб:** A17 (същият салон, но фризьорката е само ръце и глас) е 35.7 → 34.7, като P04 дава stop 7, а P15 stop 6 и buy 3. VF-026 (статична кухня, двама в кадъра) е 37.4 → 36.0 → 36.2 → 35.0. Колата е 30.0 и 28.8, а разходката 24.3: движещото се и тясното губи.
- Число за „салон“ или „фризьорка“ в чужди реклами **няма** (Ads Library не е достъпна, а Brandsearch не е свързан).

**Защо ще работи:** взима механиката на контролата (скептичка чете кутията, пита на всеки 3–4 с, героинята отговаря с едно изречение, накрая скептичката одобрява плащането и си записва името). Сменя трите неща, които я ограничават. (1) Питащата не е съпругът, затова пада филтърът „мъж вкъщи нямам“, а фризьор имат всички. (2) Не е от семейството, затова в рунда няма умора от семейни скечове. (3) Двете лица са фронтално, затова реакцията се чете на телефон без звук. Пелерината решава тялото, а реакцията на размера отговаря на най-честото разочарование при доставката.

**Как ще подейства:**
- **0–3.5 сек:** фризьорски стол и две жени на нейните години. „Нова боя ли е?“ я разсмива, защото и тя не знае какво е берберин. Спира.
- **3.5–10 сек:** разбира какво е („лепенка, берберин, канела и нар“) и чува, че се плаща в Еконт. Скептичката кима, страхът пада.
- **10–13.5 сек:** „Толкова малка?“ Вижда истинския размер и смешното лице на фризьорката.
- **13.5–25 сек:** на рамото, всяка сутрин една, за жени като нея, не е лекарство, 14.99 евро плюс доставка. Разговорът е на всеки 3–4 секунди, докато фризьорката работи с косата, затова не е лекция.
- **25–30.5 сек:** „Нищо няма да ти обещая.“ Скептичката кимва, после идва редът за лекаря. Това е доверие.
- **30.5–34.5 сек:** „Е, поне се плаща на гишето. Запиши ми го.“ – „Бер-бе-рин. Не е боя.“ Шегата се затваря, а щом и фризьорката си го записва, може и тя. Кликва.

**Продукция:** 1 салон сутрин преди отваряне (със съгласие на собственика), 2 актриси около 50 с писмено съгласие, телефон на флакон лак, 1 вмъкване на пръстите и 1 кроп. 1–1.5 часа, 0 кредита. За симулацията може AI (Kling/Veo), а за Meta само истински запис и истинската лепенка, защото „Толкова малка?“ показва свойство на продукта (ред 18; логиката на ред 149).
**Трудност:** ниска.
**Риск в Meta:** нисък до среден. Без юрист: няма разговор за хормоните и ред за ефект (ред 301).
1. Лепенката се вижда 1 с в същия среден план, с лицето в кадъра и отпусната ръка, а яката се дърпа встрани. Без вмъкване на рамото и без деколте (ред 26, 162, 258, 297). Фризьорката гледа лицето, не рамото (ред 295).
2. Пликът излиза от кадър на 13.5 с, сцените 17–28 с са без продукт, редът за лекаря е след твърд срез, а след него продукт няма (ред 36, 43). Финалът назовава плащането, без „затова“ (ред 206, 268).
3. Ред 112 е между плащането и цената, а между него и „Не е магия.“ стои цената (ред 143, 293). „Не е лекарство.“ е по-дребно под ред 112 (ред 113, 224).
4. Салонът е място за външен вид: без коментар за вида, прическата, тялото или възрастта ѝ, без показване на новата прическа и без поглед „как изглеждам“ (ред 13, 14, 25, 226).
5. Казва се „от интернет“ (ред 209). Еконт е само като дума и истински плик, а товарителницата е покрита (ред 76, 163, 164, 270). Без име и лого на салона и без четими марки по рафтовете.
6. „14.99 € + доставка“ е на един ред, 3+1 също на един ред (ред 28, 73). „1 лепенка сутрин“ (ред 244). „Драматизация“ стои постоянно (ред 53).
7. Блокери като при всички: H1 на PDP, 3+1 = 4 пакета в Shopify, истинският етикет, таксата за НП, само страница FitPatches, 18+.
**Ген за лаб смяната:** `visual_format`, нов формат с ново тяло срещу контролата VF-026 (CB-054). Ако спечели, следващият чист A/B е V-б: същото тяло, но питащата е колежка в кухнята на офиса. Така ще разберем дали печели салонът или несемейният питащ.
**Статус:** нов (04.10, 07:11), в рунд `20261004-0712-active` (`drafts/strategist.json`)

---

### VF-031 „Подкастът на дивана“ (две жени на дивана с обикновени микрофони, статичен two-shot: водещата задава 5 бързи въпроса, гостенката отговаря с по едно изречение)
*Добавена на 04.10, 07:11, скаут GB (само уеб: meta_ads иска нов вход, facebook.com/ads/library връща 403, а TikTok Creative Center без JS е празен). Защо точно сега: на 03:11 (`20261004-0312-active`) анкетата без монолога се повтори като №1 (35.1 → 35.8). Статичният кадър в кухнята бие всички, а разходката (VF-029) е последна с 24.3 (8%), защото движещият се фон и бързото темпо губят. Панелът се уморява от семейни скечове (6 от 10 в рунда), затова правилото е най-много 2 скеча с един и същ питащ в рунд. VF-031 събира двете печеливши неща, бързите въпроси без монолог и статичния кадър, в рамка, която не е семеен скеч: две жени на дивана като в подкаст. Двете лица са в кадъра през цялото време, а питащата не е от семейството.*

**Какво е визуално:** видео 9:16, ≈29 сек, 1 хол. Телефонът е на статив на нивото на очите и кадърът не мърда. Two-shot от кръста нагоре: двете седят на дивана в три четвърти една към друга. Пред тях има ниска масичка с две чаши чай и два обикновени черни микрофона на настолни стойки (без лого и без кубче на медия). Отзад има топла лампа, растение и плетено одеяло.
- **Водещата** (около 40, дънкова риза, тетрадка с въпросите в ръка) пита кратко и не коментира. **Гостенката** (около 50, тъмна коса до раменете, свободна плетена жилетка, възглавница в скута) отговаря с едно изречение. Никой отговор не е по-дълъг от 4 сек.
- **Правилото на играта е hook-ът:** „Отговаряш с едно изречение.“ Брояч горе вдясно „въпрос 1/5“ … „въпрос 5/5“, като във VF-027 V-б: винаги с думата „въпрос“, без звезди, кръг, ✓ и думата „тест“ (ред 74).
- **Вмъкванията са само 3:** лепенката на рамото за 1 сек (тя дръпва яката на жилетката), пакетът към камерата за 2 сек и картата за лекаря. Всичко останало е един и същ статичен two-shot.
- **Субтитри:** водещата в жълто, гостенката в бяло. „Драматизация“ стои от първия до последния кадър, под горните 14%. Долният надпис „Реклама · FitPatches“ е ≥ 30 px през цялото видео (ред 212). Без име на предаване, номер на епизод, „на живо“, лого на канал и интерфейс на TikTok или Instagram.
- **Разлика от VF-014** (подкаст в студио, висока трудност, не е симулиран): тук е домашен хол, един статичен кадър, бързи въпроси вместо разказ и ниска трудност. **Разлика от VF-030** (фризьорката, на стратега): там е реакция и демо в салона, тук няма реакция и демо, а бързи въпроси в рамка на подкаст. Двата формата не са семейни и могат да са в един рунд.

| Време | 🎬 Кадър | 🖊 Надпис | 🎙 Глас |
|---|---|---|---|
| 0–3 сек (HOOK) | Статичен two-shot на дивана. Водещата поглежда в тетрадката, после към гостенката. Двете се засмиват | голям надпис горе: „Пет въпроса. По едно изречение.“ · субтитри | (водещата) „Пет въпроса за лепенката ти. Отговаряш с едно изречение.“ (гостенката) „Давай.“ |
| 3–6.5 сек | Two-shot. На „Лепенка“ има вмъкване за 1 сек: гостенката дръпва яката на жилетката и показва малката бежова лепенка горе на рамото, после я оправя. Обратно в two-shot | „въпрос 1/5“ · „лепенка · берберин · канела · нар · 30 в пакет“ · на отделен ред, по-дребно: „За жени, които внимават какво ядат.“ | (водещата) „Какво е?“ (гостенката) „Лепенка с берберин, канела и нар.“ |
| 6.5–10 сек | Two-shot. Водещата вдига вежди | „въпрос 2/5“ · „плащаш при доставка“ | (водещата) „От интернет? Да не е измама?“ (гостенката) „Платих чак като ги взех от Еконт.“ |
| 10–14 сек | Вмъкване за 2 сек: гостенката вдига пакета FitPatches пред микрофона с етикета към камерата (истинската опаковка, текстът се слага в монтажа). После го прибира в чантата до дивана, под кадъра. Обратно в two-shot, пакет няма | „въпрос 3/5“ · „1 пакет 14.99 € + доставка · 30 лепенки“ | (водещата) „Колко?“ (гостенката) „Четиринайсет и деветдесет и девет плюс доставка. За трийсет.“ |
| 14–17.5 сек | Two-shot. Гостенката свива рамене. Водещата гледа в тетрадката и не реагира | „въпрос 4/5“ · „Не е магия.“ | (водещата) „И какво очакваш?“ (гостенката) „Нищо няма да ти обещая. Не е магия.“ |
| 17.5–21 сек | Two-shot. Гостенката докосва рамото си върху жилетката, без да я дърпа | „въпрос 5/5“ · „сутрин · на рамото · не е хапче“ | (водещата) „Последен: как се слага?“ (гостенката) „Сутрин, на рамото, с кафето.“ |
| 21–25 сек | Твърд срез без J-cut: за първи път водещата е сама в кадъра и говори към камерата. Пакет и лепенка няма | карта (бял фон, тъмен текст, без иконки): „При лекарства, бременност или кърмене — първо лекарят.“ · без брояч | (водещата) „При лекарства, бременност или кърмене — първо лекарят.“ |
| 25–29 сек | Обратно в two-shot. Водещата затваря тетрадката | „линк отдолу“ · малък ред долу: „Не замества разнообразното хранене и движението.“ | (водещата) „Пет въпроса, пет изречения.“ (гостенката, към камерата, с усмивка) „Линкът е отдолу.“ |

**Текст под рекламата:**
„Пет въпроса за лепенката. По едно изречение.
1. Какво е? Лепенка с берберин, канела и нар. 30 в пакет. За жени, които внимават какво ядат.
2. От интернет? Да не е измама? Платих чак като ги взех от Еконт.
3. Колко? 1 пакет 14.99 € + доставка.
4. И какво очакваш? Нищо няма да ти обещая. Не е магия.
5. Как се слага? Сутрин, на рамото. Не е хапче.
При лекарства, бременност или кърмене — първо лекарят.
Линкът е отдолу.
*Видеото е драматизация. Лепенката не замества разнообразното хранене и движението.“
**Заглавия:** „Пет въпроса. По едно изречение.“ · „Платих чак като ги взех от Еконт“ · „Нищо няма да ти обещая“. **CTA:** SEE_DETAILS, като родителя.

**Варианти за лабораторията:**
- **V-а** е основният, по-горе. Двете не са роднини, хормоните не се споменават, а редът „за какво е“ е надпис в трето лице, а не въпрос. Причината е, че на 03:11 задържането падна точно на „А за какво е?“ (88% → 56%). Ако A/B-то в 07:11 покаже, че въпросът не пречи, той се връща като „въпрос 2/5“ с дословния ред 112 в първо лице.
- **V-б е чист A/B срещу VF-027 V-а** (31.2 на 23:11). Думите на VF-027 V-а остават дума по дума: hook „Какво си взе от Еконт?“, като пликът от Еконт е в скута на гостенката, а товарителницата е покрита; после „Какви лепенки?“, „И за какво е?“, „Колко даде?“, „И какво очакваш?“, „Как се слага?“. Сменя се само кадърът: улица, кадър от ръка и невидима интервюираща → диван, статичен two-shot и двете лица през цялото време. Така се мери чисто колко носят статичният кадър и второто лице.
- **V-в е версията на Your Heights:** истинският собственик на FitPatches пита истинска клиентка. Изисква ред 211 (основателят от свое име, само от страница FitPatches), писмено съгласие на клиентката и неин реален цитат в `voc.md`, който засега е празен. Блокиран, докато няма такава клиентка.

**Къде и защо скалира (сигнал, сила B):**
- **Motion, формат Podcast:** в списъка с 12 марки 3 са британски: Your Heights, Spacegoods и Huel. Там е и Happy Mammoth. По описанието на Motion „единият обикновено пита, другият отговаря“, а микрофоните се виждат във всички примери. Има и домашни версии с диван. Hit rate няма ([Podcast](https://motionapp.com/library/formats/podcast)).
- **Your Heights (UK, енергия и мозък, 40+, скептици към добавките):** 343 активни реклами и ≈109 нови на седмица, тоест около 1/3 от библиотеката се сменя всяка седмица. Основателят интервюира клиент: „Dan asks Mark what was going on in his life before trying Heights“, „Dan asks what Mark's wife had to say“. Пускат и знаменитост (Matt Willis) и 30-дневно изпитание ([Your Heights](https://motionapp.com/library/your-heights)).
- **Spacegoods (UK, цени в £, жени 25–55):** 272 активни и ≈112 нови на седмица. Hook-ове „Menobelly?“, „Cortisol belly?“, „Perimenopause weight?“. Марката е в списъка Podcast ([Spacegoods](https://motionapp.com/library/spacegoods)).
- **Happy Mammoth EU** (австралийска марка с реклами в UK; ASA е забранявала нейни реклами 2 пъти): 988 активни и ≈106 нови на седмица. В описанието на Motion: „Two women sit on a yellow couch as one shows the other … on her phone“ и „The pacing is slow, with static shots“. Взимаме само дивана и статичния кадър. Преди/след не взимаме ([Happy Mammoth EU](https://motionapp.com/library/happy-mammoth-eu)).
- **Influee** (платформа за UGC, твърдение на самия доставчик): podcast-style реклами с „40%+ hook rates across 12+ campaigns“. Ползва се само като посока ([Influee](https://influee.co/landing/podcast-style-ads)).
- Данните на Motion са обновени „преди 4–5 месеца“. **Число за „две жени на дивана“ в рекламите за добавки в GB няма.**
- **Лаб:** анкетата без монолога е №1 два пъти (35.1 → 35.8). Скептичната приятелка S3 е №1 на 08:59 (36.3). Статичният кадър в кухнята бие всички (03:11), а разходката е последна (24.3, 8%).

**Защо ще работи:** взима двете неща, които панелът награди на 03:11: бързите въпроси без монолог (анкетата, №1 два пъти) и статичния кадър (кухнята бие разходката). Добавя рамката, с която британските марки скалират: подкаст с двама, в който единият пита. Питащата е приятелка, не съпруг или дъщеря, затова форматът не уморява панела като шестия семеен скеч в рунда. Двете лица са в кадъра през цялото време, а точно това печели в лабораторията. Правилото „едно изречение“ държи отговорите под 4 сек, а брояч 1/5…5/5 дава причина да се гледа до края.

**Как ще подейства:**
- **0–3 сек:** вижда две жени с микрофони на дивана. Изглежда като клип от подкаст, не като реклама. „Отговаряш с едно изречение“ е игра и тя иска да види дали гостенката ще издържи. Спира.
- **3–6.5 сек:** за секунда вижда истинската лепенка на рамото и чете съставките. Отдолу пише за кого е, без въпрос, който да я спре.
- **6.5–14 сек:** водещата казва на глас нейното съмнение („Да не е измама?“). „Платих чак като ги взех“ го сваля, после идва цената с доставката.
- **14–21 сек:** „Нищо няма да ти обещая“ значи, че никой не ѝ продава чудо. „Сутрин, на рамото, с кафето“ е рутина, която може да си представи.
- **21–25 сек:** водещата става сериозна за реда за лекаря. Това носи доверие.
- **25–29 сек:** „Пет въпроса, пет изречения“ затваря играта. Гостенката казва „Линкът е отдолу“ и тя кликва.

**Продукция:** 1 хол, 2 актриси с писмено съгласие, 1 телефон на статив, 2 петлични микрофона за звука и 2 обикновени настолни микрофона в кадъра (без лого). ≈1 час, 0 кредита. За симулацията може AI (Kling/Veo): седнал статичен two-shot е много по-лесен за AI от ходене. За Meta само истински запис (ред 18).
**Трудност:** ниска.
**Риск в Meta:** нисък.
1. **Ред 212 (подкаст):** без име на предаване, епизод, лого, „на живо“ и бадж; обикновени микрофони; роли без имена; „Реклама · FitPatches“ ≥ 30 px; „Драматизация“ през цялото видео.
2. **Без разговор за хормоните**, затова редове 185–192 не важат и не е нужен юрист.
3. **Тяло (ред 228 по аналогия):** седнали, кадър от кръста нагоре, свободна жилетка, възглавница в скута. Яката се дръпва само на рамото, за 1 сек.
4. **Ред 112** е надпис в трето лице, на отделен ред, без нищо добавено и не до симптоми или ред за ефект. „Не е лекарство.“ не се ползва.
5. **„И какво очакваш?“** е дословно, отговорът също (ред 181). Водещата не кима и не реагира на „Не е магия“.
6. **Редът за лекаря** идва след твърд срез и без продукт (ред 36, 43). Пакетът е прибран още в 14-та секунда.
7. Казва се „от интернет“ (ред 209). Във V-а Еконт е само дума, във V-б пликът е с покрита товарителница (ред 76, 164).
8. Броячът е само с думата „въпрос“ (ред 74).
9. **V-в:** ред 211 + писмено съгласие + реален цитат в `voc.md`.
**Ген за лаб смяната:** `visual_format`. V-а е новият формат. V-б е чист A/B „улица с невидима интервюираща → диван с двете лица“ върху думите на VF-027 V-а. Двете не са семеен скеч, затова не влизат в лимита „най-много 2 скеча с един и същ питащ в рунд“.
**Статус:** нов (04.10, 07:11)

---

### VF-032 „Екранът на поръчката“ (Checkout Mockup: истинската форма за поръчка на телефон в ръка, изрязана до цената и плащането при доставка)
*Добавена на 04.10, 07:11, скаут GB. Защо: Vitabiotics, най-голямата британска марка витамини, е №1 по брой реклами в този формат в Motion и строи акаунта си около офертата: „цената първа“ е 35% от рекламите, на целия сайт върви „3 за 2“. При нас цената и наложеният платеж в първата секунда вече печелят (A9 „честната“ 41.1, 67% срещу S2), но статиките без човек губят (19.5–24.2). Затова екранът е в ръката на жена, а не на чист фон.*

**Какво е визуално:** статик 4:5 (и 9:16). Снимка от ръка: женска ръка държи телефона над кухненската маса, до чаша кафе и сивия плик от Еконт с покрита товарителница. На екрана е истинската форма „Бърза поръчка“ на fitpatches.net, снимана в деня на снимките. Изрязана е до реда с цената и реда за плащане при доставка. Полетата за име и телефон са празни или изрязани, а бутонът за поръчка, звездите, таймерът и лентата на браузъра не се виждат (ред 213).
- **Горе**, с ръкописен шрифт като на листче (VF-008): „Така изглежда поръчката.“
- **На екрана** има ръчно нарисуван кръг около реда за плащане при доставка.
- **Лента отдолу:** „1 пакет 14.99 € + доставка · 30 лепенки · плащаш, като ги вземеш“
- **Най-долу, по-дребно:** „Лепенка с берберин, канела и нар. За жени, които внимават какво ядат.“

**Текст под рекламата:**
„Така изглежда поръчката. Без карта: плащаш, като ги вземеш от Еконт.
1 пакет 14.99 € + доставка · 30 лепенки с берберин, канела и нар.
За жени, които внимават какво ядат. Сутрин една, на рамото. Не е хапче.
При лекарства, бременност или кърмене — първо лекарят.“
**Заглавия:** „Плащаш, като ги вземеш“ · „Така изглежда поръчката“. **CTA:** SEE_DETAILS.

**Варианти:**
- **V-а** е основният, по-горе: 1 пакет с плащане при доставка. Може да се пусне по сегашните правила.
- **V-б** е за 3+1: във формата е избран „3+1 подарък“, а на лентата пише „3+1 подарък 39.99 € · безплатна доставка · около 0.33 € на ден“ на един ред (ред 37). **Блокер ред 94:** продуктите в Shopify са „2+1 БЕЗПЛАТНО ПОДАРЪК“ и „Десет пакета“, и екранът ще покаже точно това несъответствие. Чака собственика. Това е и лостът „1 пакет → 3+1“ (+330 €/мес. по CLAUDE.md).
- **Във видео:** във VF-031 или VF-026, на „Колко?“, гостенката обръща телефона с формата към камерата вместо пакета.

**Къде и защо скалира (сигнал, сила B−):**
- **Motion, Checkout Mockup:** „screenshot-style mockup of a shopping cart or checkout page, typically showing product bundles, discount codes applied, or a sale price breakdown“. Най-много реклами в този формат имат Vitabiotics (21), Tractive (14), Aarke (11), Turo (8) и Skylight (6). От здравето са Vitabiotics, Ancient + Brave (UK), Four Sigmatic и Bloom. Hit rate няма ([Checkout Mockup](https://motionapp.com/library/formats/checkout-mockup)).
- **Vitabiotics (UK):** 760 активни и ≈75 нови на седмица. „Цената първа“ е 35%, Demo 12%, UGC overlay 10%. Офертата е „3 за 2“ на целия сайт ([Vitabiotics](https://motionapp.com/library/vitabiotics)).
- **VF-001 „Цената първа“** е със сила A (Motion: 29.3% от разхода при 21.9% от креативите).
- Данните на Motion са обновени „преди 5 месеца“. Число за ефекта на формата няма.

**Защо ще работи:** най-честите въпроси на персоните са „колко?“ и „плащам ли предварително?“. Тук отговорът е снимка на истинския екран, не обещание. Ръката, кафето и пликът от Еконт правят статика „човешки“, а точно човек липсваше на статиките, които губят.
**Как ще подейства:** вижда екран, който познава от собствените си поръчки → чете цената с доставката → кръгът ѝ показва, че няма карта и плаща при доставка → съмнението „измама?“ пада → кликва, за да види същия екран.
**Продукция:** 1 снимка с телефон, ≈15 мин, 0 кредита. Екранът трябва да е истински и от деня на снимките. Ако във формата няма отделен ред за плащане при доставка, форматът не става: няма данни, продуцентът трябва да провери формата.
**Трудност:** ниска.
**Риск в Meta:** нисък. Ред 213 (изрязване, празни полета, истински екран от деня на снимките); цената винаги с доставката; без звезди, ревюта и таймер; ред 37 и 94 за V-б.
**Статус:** нов (04.10, 07:11). V-б чака ред 94.

---

### VF-033 „Съседката от входа“ (скеч пред пощенските кутии: съседката вижда плика от Еконт и пита, двете лица фронтално, несемеен връстник)
*Добавена на 04.10, 08:59, скаут RO (само уеб; Ads Library: 0 заявки, конекторът meta_ads иска нов вход). Защо точно сега: собственикът иска формати с две реални лица без семейство. На 07:11 несемейната фризьорка (VF-030) стигна контролата (34.2 срещу 34.4), а служителката на гишето (A25) загуби (25.4). Затова тук питащата е **връстничка със собствена история за измама**, не служителка. В RO най-голямата аптечна верига снима точно тази сцена със съседката, защото фармацевтите нямат право да препоръчват в реклама. CNA я забрани, защото съседката препоръчва за чужд симптом. Тук препоръката е обърната: съседката пита, никой не препоръчва.*

**Какво е визуално:** видео 9:16 (+ изрязване 4:5), ≈27 сек, 1 локация: входът на панелен блок, делник сутрин, площадката пред металните пощенски кутии. Без други хора в кадъра. Имената и номерата на кутиите са покрити, а номер на блок и адрес не се виждат.
- **Камерата е статична.** Телефонът е на перваза на прозореца на стълбището, срещу двете. Има само 1 с вмъкване (пръстите с лепенката) и 1 кроп (лицето за реда за лекаря).
- **Двете лица са фронтално едновременно.** Двете стоят една до друга с лице към прозореца, тоест към камерата, и гледат плика, който героинята държи на нивото на гърдите. Не са в профил (колата на VF-028 губи), не вървят (разходката на VF-029 губи).
- **Есенните палта закриват тялото**, както пелерината във VF-030. Кадърът е от кръста нагоре, без жест към кръста и без кадър под гърдите.
- **Съседката пита, героинята знае.** Съседката е на около 60, с очила, торбичка от пазара на ръката и ключове. Героинята е на около 50. Съседката пита само за пратката, плащането, размера, целта, цената и очакванията. Никога не коментира вида, възрастта, тялото или храненето ѝ и няма свой симптом.
- **Хуморът е от архетипа:** съседката, която вижда всяка пратка („Пак Еконт?“), и „Лепенки? За плочките ли?“. Нейната история за измамата („излъгаха ме с едни чорапи“) прави възражението лично.
- **Субтитри:** съседката е в жълто, героинята в бяло. „Драматизация“ стои от първия до последния кадър (при AI: „Драматизация · създадено с AI“). Без интерфейс на TikTok или Instagram.

| Време | 🎬 Кадър | 🖊 Надпис | 🎙 Глас |
|---|---|---|---|
| 0–3 сек (HOOK) | Two-shot пред пощенските кутии. Героинята държи разкъсания сив плик от Еконт (товарителницата е покрита с бял стикер). Съседката се навежда към плика, вдига вежди и поглежда героинята над очилата | голям надпис горе, без да покрива лицата: „Съседката вижда всяка пратка.“ · субтитри | (съседката) „Пак Еконт? Какво си поръчала този път?“ |
| 3–6 сек | Two-shot. Героинята вади кутията наполовина от плика. Съседката присвива очи към нея | „лепенка · берберин · канела · нар“ | (тя) „Лепенки.“ (съседката) „Лепенки? За плочките ли?“ (тя, през смях) „Не. Берберин, канела и нар.“ |
| 6–10 сек | Two-shot. Съседката клати глава и почуква плика с ключа | „Плащаш при доставка“ | (съседката) „От интернет? Мен миналата година ме излъгаха с едни чорапи.“ (тя) „Аз платих чак в Еконт, като ги взех.“ |
| 10–13 сек (РЕАКЦИЯТА) | Съседката взима кутията, вади 1 лепенка и я вдига срещу светлината от прозореца. 1 с вмъкване само на пръстите с лепенката, без тяло. Обратно в two-shot: очите ѝ се отварят. Връща лепенката в кутията и кутията в плика, а героинята пуска плика в чантата си, извън кадъра | едро, в жълто: „Толкова малка?“ · по-дребно: „30 лепенки · 1 сутрин, на рамото · не е хапче“ | (съседката) „Толкова малка?“ (тя) „Толкова. Сутрин една, на рамото.“ |
| 13–16.5 сек | Two-shot. Продукт няма. Съседката оправя торбичката на ръката си | едро: „За жени като мен, които внимават какво ядат.“ · по-дребно: „Не е лекарство.“ | (съседката) „И за какво е?“ (тя) „За жени като мен, които внимават какво ядат. Не е лекарство.“ |
| 16.5–19.5 сек | Two-shot. Продукт няма. Съседката вдига вежди и чака | „1 пакет 14.99 € + доставка“ / „30 лепенки“ / „3+1 подарък 39.99 € · безплатна доставка“ | (съседката) „Колко даде?“ (тя) „Четиринайсет и деветдесет и девет евро плюс доставка.“ |
| 19.5–22 сек | Two-shot. Съседката я гледа над очилата, героинята свива рамене. Съседката кимва бавно, без думи | „Не е магия.“ | (съседката) „И какво очакваш?“ (тя) „Нищо няма да ти обещая. Не е магия.“ |
| 22–24.5 сек | Твърд срез без J-cut: само лицето на героинята. Съседка, плик и пакет няма | карта (бял фон, тъмен текст, без икони): „При лекарства, бременност или кърмене — първо лекарят.“ | (тя) „При лекарства, бременност или кърмене — първо лекарят.“ |
| 24.5–27 сек | Two-shot. Съседката вече е на първото стъпало и се обръща. Героинята поглежда в обектива и посочва надолу. Продукт няма | „Линкът е отдолу“ · малък ред (≥ 30 px): „Не замества разнообразното хранене и движението.“ | (съседката) „Е, поне се плаща на гишето.“ (тя, към камерата) „Линкът е отдолу.“ |

**Текст под рекламата (кратък):**
„„Пак Еконт? Какво си поръчала този път?“
Съседката вижда всяка пратка. Този път бяха лепенки.
Берберин, канела и нар. 30 в пакет. Сутрин една, на рамото. Не е хапче.
„От интернет?“ Платих чак в Еконт, като ги взех.
1 пакет е 14.99 € + доставка.
При лекарства, бременност или кърмене — първо лекарят.
Линкът е отдолу.
*Видеото е драматизация. Лепенката не замества разнообразното хранене и движението.“
**Заглавия:** „Съседката вижда всяка пратка“ · „Платих чак в Еконт, като ги взех“ · „Лепенки? Не за плочките.“ **CTA:** SEE_DETAILS.

**Варианти:**
- **V-а** е основният, по-горе (≈27 сек).
- **V-б е чист A/B на дължината** (≈20 сек). Махат се шегата с плочките (3–6 сек става „Лепенки. Берберин, канела и нар.“) и сцената „Толкова малка?“ (10–13 сек), а „Сутрин една, на рамото.“ отива в отговора на 3–6 сек. Всичко друго е дума по дума. Мери дали по-късото видео задържа края: VF-030 стига до края с 19% от ICP, VF-026 с 25%. V-а и V-б са с едно тяло, тоест 2 от позволените 2 в рунда.
- **V-в е статик 4:5** (VF-025): кадърът от hook-а (двете лица и пликът) + горе „Съседката вижда всяка пратка.“ + лента „Лепенки с берберин, канела и нар · 1 пакет 14.99 € + доставка · плащаш, като ги вземеш“ + малко „Драматизация“. Евтин тест дали hook-ът работи и без видео.

**Къде и защо скалира (сигнал, сила B−):**
- **RO, Catena:** най-голямата аптечна верига в RO пусна ТВ спот с две съседки („Bună, vecino!“). Съседката препоръчва добавка и на съседката, и на фармацевтката. Paginademedia пише, че съседката е заместител на фармацевта, на когото е забранено да препоръчва. CNA го обяви за незаконен (самолечение, чл. 29(1)(f) от Закон 504/2002), а Валентин Жукан каза „Ce vedeţi aici este fenomenul TikTok.“ ([HotNews, 20.03.2026](https://hotnews.ro/doua-reclame-ale-farmaciilor-catena-i-au-scos-din-sarite-pe-membrii-cna-cuvinte-grele-in-sedinta-neobrazarea-unei-industrii-ce-vedeti-aici-este-fenomenul-tiktok-2198998), [Paginademedia](https://www.paginademedia.ro/stiri-media/reclama-catena-interzisa-cna-22383275)). Колко дълго е вървял и дали е бил в Meta: няма данни.
- **RO, регулацията:** CNA 573/2025 забранява публични личности, инфлуенсъри, лекари и фармацевти в рекламата на добавки ([cristinatudor.ro](https://www.cristinatudor.ro/post/interdic%C8%9Biile-de-promovare-a-suplimentelor-pentru-sl%C4%83bit-ce-prevede-decizia-cna-nr-573-2025), тълкуване на блог). Законно остава само обикновеният човек.
- **Регионът, незаконно:** Bitdefender изброява „диалог на двама с псевдонаучно обяснение“ сред форматите на мрежи с „десетки хиляди реклами“ в RO ([Bitdefender](https://www.bitdefender.com/ro-ro/blog/hotforsecurity/o-analiza-detaliata-a-fraudelor-cu-suplimente-afla-cum-este-folosita-inteligenta-artificiala-in-fraudele-cu-tratamente-miraculoase)). Мрежата на DIICOT е работила в RO, MD, **BG**, HU и PL. Взимаме само диалога, без авторитета.
- **Свят:** Motion Skit: Liven 3K, Rise Science 2K, WalkFit 1K (жени 50+, скечове със скептичка) ([Skit](https://motionapp.com/library/formats/skit)). Класическият ТВ троп е „две жени в кухнята, едната предлага продукт“ ([All The Tropes](https://allthetropes.org/wiki/Two_Chicks_in_a_Kitchen)).
- **Лаб:** несемейният питащ стигна контролата (VF-030 34.2 срещу VF-026 34.4, 07:11). Служителката на гишето (A25, около 30, на работа) губи с 25.4. Статичното печели, движещото се губи (разходката 24.3, колата 28.8–30.0).
- Число за „съседка“ в реклами в Meta **няма**.

**Защо ще работи:** взима механиката на контролата: скептичката пита на всеки 3 сек, а героинята отговаря с едно изречение. Сменя питащата с човек, когото има всяка жена: съседката от входа, която вижда всяка пратка. Тя е връстничка и е била излъгана от интернет, затова „измама ли е?“ звучи като нейното съмнение, а не като реплика от реклама. Пликът от Еконт е естественият повод и подава отговора „платих, като ги взех“. В сравнение с A25 питащата не е служителка, която тъкмо е взела парите, а човек със същия страх. В сравнение с VF-030 няма салон, тоест няма място за външен вид, а видеото е със 7.5 сек по-кратко, там където панелът губи края.

**Как ще подейства:**
- **0–3 сек:** входът на блока и съседката, която вижда всичко. Тя я познава и се усмихва. Спира.
- **3–10 сек:** „За плочките ли?“ я разсмива. Чува какво е (берберин, канела и нар), после чужда история за измама от интернет и отговора „платих чак в Еконт“. Страхът пада.
- **10–13 сек:** „Толкова малка?“ Вижда истинския размер преди поръчката, тоест няма изненада на гишето.
- **13–22 сек:** за жени като нея, не е лекарство, 14.99 € плюс доставка, „Нищо няма да ти обещая“. Съседката кимва, значи и скептичката приема. Това е доверие.
- **22–27 сек:** редът за лекаря, после „Е, поне се плаща на гишето.“ Последното, което чува, е плащането при доставка. Кликва.

**Продукция:** 1 вход на панелен блок сутрин (със съгласие на домоуправителя, без други хора), 2 актриси (около 50 и около 60) с писмено съгласие, телефон на перваза, 1 вмъкване на пръстите и 1 кроп. Около 1 час, 0 кредита. За симулацията може AI (Kling/Veo), а за Meta само истински запис и истинската лепенка, защото „Толкова малка?“ показва свойство на продукта (ред 18; логиката на ред 149).
**Трудност:** ниска.
**Риск в Meta:** нисък до среден. Без юрист: няма разговор за хормоните и ред за ефект (ред 301).
1. **Урокът Catena:** героинята не препоръчва нищо на съседката, съседката няма симптом и не казва „вземи и ти“, „ще ти помогне“, „и на мен ми трябва“. Финалът назовава само плащането (2005/29, чл. 6; ред 206, 268).
2. Съседката не коментира вида, възрастта, тялото и храненето ѝ („отслабнала ли си?“ е свидетел на ефект, ред 38). Палтата закриват тялото, без жест към кръста (ред 13, 14, 26).
3. Пликът излиза от кадър на 13 сек, сцените 13–27 сек са без продукт, редът за лекаря е след твърд срез, а след него продукт няма (ред 36, 43).
4. Ред 112 е между плащането и цената, „Не е лекарство.“ е по-дребно под него, а цената стои между ред 112 и „Не е магия.“ (ред 113, 143, 224, 293).
5. „От интернет“ без марка, а чорапите са без магазин и платформа (ред 209). Еконт е само като дума и истински плик, товарителницата е покрита (ред 76, 163, 164, 270).
6. Имената и номерата по пощенските кутии, номерът на блока и адресът са покрити (GDPR). Без други живущи в кадъра.
7. „14.99 € + доставка“ е на един ред, 3+1 също на един ред (ред 28, 73). „Драматизация“ стои постоянно (ред 53).
8. Блокери като при всички: H1 на PDP, 3+1 = 4 пакета в Shopify (ред 94), истинският етикет, таксата за НП, само страница FitPatches, 18+.
**Ген за лаб смяната:** `visual_format`, нов формат с ново тяло срещу контролата VF-026. V-б е чист A/B на дължината (27 → 20 сек).
**Статус:** нов (04.10, 08:59, скаут RO), за 11:11.

---

### VF-034 „Класацията на двете приятелки“ (две връстнички на кухненската маса подреждат 5 неща, които са пробвали сутрин, по това кое не забравят; двете лица фронтално, несемейни)
*Добавена на 04.10, 11:11, скаут DE (само уеб; Ads Library: 0 заявки, конекторът meta_ads иска нов вход). Защо точно сега: собственикът иска формати с две реални лица без семейство. Несемейната питаща вече стига контролата (VF-030 34.2 срещу VF-026 34.4, 07:11), но краят губи: до края стигат само 19% (VF-030) и 25% (VF-026) от ICP. Класацията дава на разговора вграден повод (игра, а не разпит) и отворен въпрос до последната секунда: „кое остава последно?“. В DE тази механика ползва най-голямата DTC марка в Meta (MORE Nutrition: две инфлуенсърки „класират“ новите вкусове), а „Supplement-Tierlist“ е органичен тренд в немския TikTok.*

**Какво е визуално:** видео 9:16 (+ изрязване 4:5), ≈30 сек, 1 локация: кухненска маса у дома, делник сутрин. Двете приятелки (около 45 и около 50) седят една до друга от едната страна на масата, с лице към камерата. Пред тях в редица има 5 предмета, покрити с кухненска кърпа: шишенце с капкомер, саше с прах, чаша с пакетче чай, буркан с капсули и нашата кутия. Чуждите предмети са без етикет и без марка.
- **Камерата е статична.** Телефонът е на статив от другата страна на масата. Има само 1 с вмъкване (лепенката на рамото) и 1 кроп (лицето за реда за лекаря).
- **Двете лица са фронтално през цялото време.** Статичният two-shot печели, а колата (28.8–30.0) и разходката (24.3) губят.
- **Играта движи разговора.** Всяка мести по един предмет встрани и казва по едно изречение. Пред предмета застава картонче с номер („5.“, „4.“, „3.“, „2.“), написано на ръка (истински почерк, ред 75).
- **Критерият е един и личен:** „кое не забравяме сутрин“. Никоя не казва дали нещо „действа“.
- **Лепенката е последна и без номер.** Картончето пред нея е „не я забравих“.
- Кадърът е от гърдите нагоре, в свободни ежедневни дрехи, без спортни екипи (ред 278).
- **Субтитри:** героинята (А) е в бяло, приятелката (Б) в жълто. „Драматизация“ стои от първия до последния кадър (при AI: „Драматизация · създадено с AI“). Без интерфейс на TikTok или Instagram.

| Време | 🎬 Кадър | 🖊 Надпис | 🎙 Глас |
|---|---|---|---|
| 0–3 сек (HOOK) | Two-shot. А дърпа кърпата от 5-те предмета. Б се навежда напред и потрива ръце | голям надпис горе, без да покрива лицата: „Кое не забравяме сутрин?“ · по-дребно: „5 неща, които сме пробвали“ | (А) „Пет неща. Подреждаме ги по това кое не забравяме.“ (Б) „Почвай отзад.“ |
| 3–6 сек | Б мести шишенцето встрани, слага пред него картонче „5.“ | „5. Капките“ | (Б) „Капките. Броя и на седмата се обърквам.“ (А, през смях) „Пети.“ |
| 6–9 сек | А мести сашето, картонче „4.“ | „4. Прахът“ | (А) „Прахът. Шейкър, вода, бъркане. До сряда.“ (Б) „Четвърти.“ |
| 9–12 сек | Б мести чашата с чая, картонче „3.“ | „3. Чаят“ | (Б) „Чаят е хубав. Ама до вечерта съм забравила.“ (А) „Трети.“ |
| 12–15 сек | А мести буркана с капсулите, картонче „2.“. Б посочва кутията | „2. Капсулите“ | (А) „Капсулите са лесни. Ама с вода, а аз все тичам.“ (Б) „Втори. А това?“ |
| 15–19 сек (ДЕМО) | А вдига ръкава на блузата до рамото. 1 с вмъкване: лепенката на горната част на ръката, ръката е отпусната, без приближаване и без кръг. Обратно в two-shot: А пуска ръкава. Б взима кутията и я обръща | картонче без номер: „не я забравих“ · надпис: „Лепенка · берберин, канела, нар · 1 сутрин, на рамото“ | (А) „Лепва се сутрин и толкова. Не се гълта.“ (Б) „Какво има вътре?“ (А) „Берберин, канела и нар.“ |
| 19–23 сек | Two-shot. Б връща кутията, А я прибира в чантата до стола, извън кадъра | „Плащаш при доставка“, после „1 пакет 14.99 € + доставка · 30 лепенки“ | (Б) „Откъде я взе?“ (А) „От интернет. Платих, като я взех от Еконт.“ (Б) „Колко?“ (А) „Четиринайсет и деветдесет и девет плюс доставка.“ |
| 23–25.5 сек | Two-shot, продукт няма. Б я гледа с вдигната вежда, А свива рамене | „Не е магия.“ | (Б) „И какво очакваш?“ (А) „Нищо няма да ти обещая. Не е магия.“ |
| 25.5–28 сек | Твърд срез без J-cut: само лицето на А. Масата и предметите не се виждат | карта (бял фон, тъмен текст, без икони): „При лекарства, бременност или кърмене — първо лекарят.“ | (А) „При лекарства, бременност или кърмене — първо лекарят.“ |
| 28–30.5 сек | Two-shot. На масата са само 4-те чужди предмета с картончетата. Б ги нарежда в редица. А поглежда в обектива и посочва надолу | „Линкът е отдолу“ · малък ред (≥ 30 px): „Не замества разнообразното хранене и движението.“ | (Б) „Добре де. Единствената, дето не я забрави.“ (А, към камерата) „Линкът е отдолу.“ |

**Текст под рекламата (кратък):**
„Пет неща, които сме пробвали сутрин. Подредихме ги по едно: кое не забравяме.
Капките, прахът, чаят, капсулите. И една лепенка.
Берберин, канела и нар. 30 в пакет. Сутрин една, на рамото. Не се гълта.
Платих, като я взех от Еконт. 1 пакет е 14.99 € + доставка.
Нищо няма да ти обещая. Не е магия.
При лекарства, бременност или кърмене — първо лекарят.
Линкът е отдолу.
*Видеото е драматизация. Лепенката не замества разнообразното хранене и движението.“
**Заглавия:** „Кое не забравяме сутрин?“ · „Пет неща. Една лепенка.“ · „Подредихме ги по едно: кое не забравяме“. Без „№1“, „победител“, „най-…“ и брояч. **CTA:** SEE_DETAILS.

**Варианти:**
- **V-а** е основният, по-горе (≈30 сек, 5 предмета).
- **V-б е чист A/B на броя** (≈21 сек, 3 предмета: чаят, капсулите и лепенката, с картончета „3.“ и „2.“). Сцените с капките и праха (3–9 сек) отпадат, а hook-ът става „Три неща. Подреждаме ги по това кое не забравяме.“. Всичко друго е дума по дума. Мери дали по-късата класация задържа края по-добре от дългата. V-а и V-б са с едно тяло, тоест 2 от позволените 2 в рунда.
- **V-в е карусел 4:5** (VF-009). Карта 1 е кадърът от hook-а (двете и покритите предмети) с „Кое не забравяме сутрин?“. Карти 2–5 са по един предмет с картончето и репликата. Карта 6 е кутията с „не я забравих“ и лента „берберин, канела и нар · 1 пакет 14.99 € + доставка · плащаш при доставка“. „Драматизация“ е на всяка карта. Евтин тест дали класацията работи и без видео.

**Къде и защо скалира (сигнал, сила B−):**
- **DE, MORE Nutrition:** най-голямата DTC марка в Meta в DE. Brandsearch (публичната страница, видяна на 04.10): 1 084 активни реклами от 12.3K проследени, €2.7M разход в DE (81% от €3.3M в ЕС и UK; периодът не е посочен) ([brandsearch](https://brandsearch.co/brands/morenutrition.de)). Motion: 209 активни, ≈21 нови на седмица, Offer-First 17%, Headline 13%, Demo 8%; данните са отпреди 4 месеца ([Motion](https://motionapp.com/library/more-nutrition)). Webnetz (13.02.2026) описва органичния пост: „zwei Influencerinnen neue Matcha-Editionen auf humorvoll-zweideutige Weise „ranken““. Профилът на основателя Кристиан Волф събира ≈105 000 реакции срещу ≈10 000 на марката ([webnetz](https://www.webnetz.de/know-how/blog/milliardenmarkt-nahrungsergaenzungsmittel-wie-wirkt-der-social-content-von-doppelherz-orthomol-more-nutrition-co-auf-user)). Дали класацията с двете върви и като платена реклама: **няма данни**.
- **DE, органично:** „Supplement-Tierlist“ и „Supplement Ranking“ са редовен формат в немския TikTok, например Марио Мюлер с 62.1K харесвания ([TikTok](https://www.tiktok.com/@muellermario/video/7431637865974500641), [Supplements Tier List](https://www.tiktok.com/discover/supplements-tier-list)). Там говори един човек, а класацията с двама е вариантът на MORE.
- **DE, платено:** в Motion Skit единственият пример с немски глас е Dr. Squatch „Die drei besten Deodorants“, тоест класация като скеч ([Skit](https://motionapp.com/library/formats/skit)). В Street Interview (17 марки) и Duet (13 марки) няма нито една марка от DACH.
- **Свят:** листикълът е 13% от ≈1 000 активни реклами на Happy Mammoth и 5.3% в бенчмарка на Motion (VF-009).
- **Лаб:** чеклистът A13 е два пъти в топ 4. Несемейната питаща стига контролата (VF-030 34.2 срещу 34.4). Краят губи: до края стигат 19–25% от ICP.
- Число за „класация с двама“ в Meta (hit rate, дни) **няма**.

**Защо ще работи:** „Пробвала е всичко“ е ядрото на Мария (аватарът, AD28 „Пробвала съм всичко…“), а петте предмета са нейният рафт. Класацията обръща „пробвала съм всичко“ от болка в игра. Двете се смеят на собствените си опити без вина, защото проблемът е в рутината, а не във волята. Втората е връстничка със същия опит, а не служителка (A25 губи с 25.4) и не роднина. Вграденият въпрос „кое остава последно?“ дърпа до края, точно там, където панелът губи. Сравнението е само по рутината (VF-010), което е най-безопасната форма на сравнение.

**Как ще подейства:**
- **0–3 сек:** кърпата пада и се виждат 5 познати неща. „И аз имам тези.“ Спира.
- **3–15 сек:** всяка реплика е нейна („броя и се обърквам“, „до сряда“). Смее се и се разпознава. Иска да види кое остава последно.
- **15–19 сек:** малката лепенка на рамото, „не се гълта“, какво има вътре. Любопитство без обещание.
- **19–25.5 сек:** плаща, като я вземе, 14.99 € плюс доставка, „Нищо няма да ти обещая“. Приятелката кимва. Това е доверие.
- **25.5–30.5 сек:** редът за лекаря, после „Единствената, дето не я забрави.“ Последното, което чува, е рутината, а не ефект. Кликва.

**Продукция:** 1 кухня, 2 актриси (около 45 и около 50) с писмено съгласие, 4 чужди предмета без етикет и марка (капкомер, саше, пакетче чай без етикет, буркан с капсули), нашата кутия и истинска лепенка, 5 картончета с истински почерк, телефон на статив. Около 1 час, 0 кредита. За симулацията може AI, а за Meta само истински запис, защото лепенката на рамото е свойство на продукта (ред 149).
**Трудност:** ниска.
**Риск в Meta:** среден към нисък. Без юрист: няма разговор за хормоните и ред за ефект (ред 301).
1. **Сравнението е само по рутината и само от първо лице** („броя и се обърквам“, „до вечерта съм забравила“). Без „не действа“, „безполезно“, „по-добре от“ и без марки (2006/114, чл. 4; VF-010). Предметите са без етикети. Капсулите са в буркан, не в блистер, и никой не казва „хапче“ (ред 119, 127).
2. **Номерата стоят само пред 4-те чужди предмета.** Пред лепенката няма „1.“, „№1“, „победител“ или „най-…“. В заглавието, thumbnail-а и първия ред няма брояч (ред 316; 2005/29, Прил. I т.2 и т.4).
3. Без „калории“, „кг“, „следобед“, „след ядене“ (ред 75, 260). „До вечерта съм забравила“ е за чая, не за ефект.
4. **Лепенката:** на рамото, ръката е отпусната, без кръг и без приближаване (ред 26, 240). „Не се гълта“ е шега за формата като „Не е хапче, не се гълта.“ (ред 119, 269). Без „минава през кожата“ (ред 20).
5. Кутията излиза от кадър на 23 сек, сцените след това са без продукт, а редът за лекаря е след твърд срез (ред 36, 43).
6. „14.99 € + доставка“ е на един ред (ред 28, 73). „Драматизация“ стои постоянно (ред 53). „Платих, като я взех от Еконт“ е вярно (ред 270), товарителница в кадъра няма.
7. Приятелката не иска лепенката за себе си и не казва защо би я искала („И аз ли да си взема?“, „На нашите години…“): финалът е само „Единствената, дето не я забрави.“ (ред 317).
8. Блокери като при всички: H1 на PDP, 3+1 = 4 пакета в Shopify (ред 94), истинският етикет, таксата за НП, само страница FitPatches, 18+.
**Ген за лаб смяната:** `visual_format`, нов формат с ново тяло срещу контролата VF-026. V-б е чист A/B на броя (5 → 3).
**Статус:** нов (04.10, 11:11, скаут DE), за 15:11.

---

### VF-035 „Истинският човек зад телефона“ (статик: снимка на човека, който вдига 0887 459 494, с първото име; без продукт в ръцете и без съвети)
*Добавена на 04.10, 11:11, скаут DE. Защо точно сега: в DE законните марки за жени 35–55 се борят за доверие със статики, а една от най-големите (VitaMoment, €247.6K в DE) държи сред топ рекламите си карта за хората от обслужването. Пазарът там е залят с фалшив авторитет (ÖIAT: 4 632 проблемни реклами за 7 месеца, 75% към хора над 45). При наложения платеж страхът „ще ме излъжат ли“ (VF-033: „излъгаха ме с едни чорапи“) има прост и верен отговор: вдига истински човек.*

**Какво е визуално:** статик 4:5 (+ 9:16 за Stories). Истинска снимка с телефон на човека, който вдига 0887 459 494, на бюрото му: телефон в ръка, усмивка, лицето е в центъра. Отгоре с истински почерк (ред 75): „Обаждаш се на 0887 459 494 и вдига [първото име].“ Под него: „Питай каквото искаш, преди да поръчаш.“ Долу лента: „Лепенки с берберин, канела и нар · 1 пакет 14.99 € + доставка · плащаш, като ги вземеш“ и работното време. Това не е драматизация. Ако на снимката е актриса, форматът отпада, защото текстът става неверен.
- **V-а:** снимката + почеркът (по-горе).
- **V-б (VF-024 като статик):** горе е истински въпрос на клиентка от `voc.md` (без име), долу са снимката и отговорът в 1 изречение. Отговорът е само за предмета, плащането или как се слага.

**Къде и защо скалира (сигнал, сила C+):**
- **DE, VitaMoment** (витамини, има колекция „Wechseljahre“): 28 активни от 410 проследени, €247.6K в DE (98%), 1.7M посещения на месец. Две от топ рекламите са статики, които въртят 9+ дни: „Hinter jeder Nachricht an uns steckt ein echter Mensch“ („Customer Happiness Team“) и „Qualität ist überall ein Versprechen. Bei uns ist sie ein Beweis“ ([brandsearch](https://brandsearch.co/brands/vitamoment.de)).
- **DE, Doppelherz:** марка на 100+ години, която говори през собствени служители (corporate influencers). Това дава ≈20 млн. показвания в TikTok при ≈15K последователи ([W&V, 16.02.2026](https://www.wuv.de/Themen/Media/TikTok-Ueberraschung-Doppelherz-liefert-20-Millionen-Impressionen), [webnetz](https://www.webnetz.de/know-how/blog/milliardenmarkt-nahrungsergaenzungsmittel-wie-wirkt-der-social-content-von-doppelherz-orthomol-more-nutrition-co-auf-user)).
- **Свят:** F-018 („заставам лично зад това“). Лаб: статиките без човек губят (19.5–24.2), а тук човекът е в центъра (VF-025 е в симулация).
- Hit rate няма. Дълголетието е само 9+ дни, затова силата е C+.

**Защо ще работи:** купувачката с наложен платеж се страхува от измама в интернет. Истински човек с истински телефон е обратното на фалшивия лекар: не е авторитет, но носи отговорност. Отговаря на „кой стои зад това?“ още преди клика. Евтин тест дали доверието, а не продуктът, спира скрола.
**Как ще подейства:** спира на лице и почерк, не на банер. Чете името и номера: „мога да звънна“. Лентата казва какво е, цената с доставката и плащането при доставка. Кликва или звъни.
**Продукция:** 1 снимка с телефон, около 15 минути, 0 кредита. Почеркът е на ръка и е сниман.
**Трудност:** ниска.
**Риск в Meta:** нисък до среден.
1. **Всичко е вярно:** кой вдига, работното време и че вдига човек, а не автоматичен отговор. **Блокер:** собственикът или operations-manager потвърждават кой вдига 0887 459 494 и кога. Ако телефонът е на склада (BigArena) или на колцентър, текстът се сменя.
2. Човекът е в роля „обслужване“. В рекламата не дава съвет и не говори за ефект, тяло, хранене, хормони или лекарства. Без бяла престилка, бадж, „консултант“ или „специалист“ (ред 170; 1924/2006, чл. 12(в), ако лепенката е храна; ред 314 по аналогия).
3. Лични данни: само първото име, писмено съгласие, нищо друго лично.
4. Продуктът не е в ръцете му, за да не се чете като препоръка от служител.
5. „14.99 € + доставка“ е на един ред (ред 28, 73).
**Ген за лаб смяната:** `visual_format` (статик с човек) срещу VF-025.
**Статус:** нов (04.10, 11:11, скаут DE), блокиран до потвърждение на точка 1.

---

## За 23:11 (3 визуални варианта на най-силните ъгли)

Ген `visual_format`: сменя се само визуалният формат. Ъгълът, думите и офертата са като на родителя от рунд `20261002-1912-active`, доколкото форматът позволява. Панелът оценява по правилата за статики, карусели и скрийншоти в `.claude/agents/audience-panel.md`. Контрола е S2. Най-много 2 реклами с тялото на S2 в рунда: S2 + VF23-3.

### VF23-1 · A13 „5 неща… не са от мързел“ → VF-009 карусел-чеклист (5 карти, 4:5)
**Родител:** A13 · без „след 40“ (№3, SIM 33.2). **Формат:** карусел. Няма персона и няма първо лице в надписите, затова не е нужна „Драматизация“. Ако compliance прецени, че „ям по-малко от преди“ е първо лице, на карта 2 се слага малък надпис „Драматизация“.

| Карта | Визия | Текст на картата | Заглавие под картата |
|---|---|---|---|
| 1 (hook) | Отворена тетрадка на дървена кухненска маса, сутрешна светлина, снимка отгоре. Вдясно 5 празни квадратчета на ръка; петото се реже от ръба и продължава на карта 2. Малко лого FitPatches долу вдясно. Без лице и без продукт | голямо: „5 неща, които много жени забелязват с годините.“ · с жълт маркер: „И не са от мързел.“ · малко: „плъзни →“ | „5 неща. И не са от мързел.“ |
| 2 (разпознаване) | Същата страница, квадратчетата са отметнати с химикал | „✓ сладкото вика по-силно“ · „✓ гладът идва по-рано вечер“ · „✓ „ям по-малко от преди““ · „✓ каквото работеше едно време — вече не“ · „✓ вината, всяка вечер“ | „Петте неща“ |
| 3 (вината пада) | Тъмнозелен фон, само текст | голямо: „Не е мързел.“ / „Не е характер.“ · по-дребно: „Много жени минават през същото.“ | „Не е мързел. Не е характер.“ |
| 4 (продуктът) | Истинският пакет до чаша кафе, ръка държи 1 лепенка. Без тяло | „1 лепенка сутрин · на рамото“ · „берберин · канела · нар“ · „не е хапче, не се гълта · 30 в пакет“ | „1 лепенка сутрин. Не е хапче.“ |
| 5 (оферта) | Жълто листче на ръка, залепено на пакета, до него отвореният сив плик от Еконт | на листчето: „1 пакет 14.99 € + доставка · 30 лепенки“ · голямо: „Плащаш при доставка“ · малко долу: „Не замества разнообразното хранене и движението.“ | „14.99 € + доставка · плащаш при доставка“ |

**Текст под рекламата:**
„5 неща, които много жени забелязват с годините. И не са от мързел.
✓ сладкото вика по-силно
✓ гладът идва по-рано вечер
✓ „ям по-малко от преди“
✓ каквото работеше едно време — вече не
✓ вината, всяка вечер
Не е мързел. Не е характер. Много жени минават през същото.
FitPatches е 1 лепенка сутрин на рамото: берберин, канела и нар. Не е хапче, не се гълта.
1 пакет 14.99 € + доставка · 30 лепенки. Плащаш при доставка.
Лепенката не замества разнообразното хранене и движението.“
**CTA и оферта:** като родителя (1 пакет, без 3+1 на финала: урок от 02.10, 3+1 на финала губи 10/24).

**Защо ще работи:**
- A13 е в топ 4 два поредни рунда: №1 на 15:11 (36.8, 75% срещу S2), №3 и №4 на 19:11 (33.2 и 33.0). Ъгълът „вината пада“ печели в симулацията. Цитати от панела: „Вината, всяка вечер… това съм аз“ (P10), „Най-после някой го казва на глас“ (P14).
- Листикълът е формат №1 при Happy Mammoth (13% от ≈1 000 активни реклами), марка в същата ниша (жени 40+, хормони и тегло). Curtis Howland го препоръчва за добавки. Статиките са 64.8% от рекламите на DTC марките, а в нашата памет са 44% от рекламите на 30+ дни.
- Продукцията е без кредити, 1 час в Canva. Ако бие видеото на A13, имаме евтин победител.

**Как ще подейства:** карта 1 спира с „не са от мързел“: това е вината, която тя носи, и звучи като нещо, което никой не ѝ е казвал. Плъзга, за да види дали петте съвпадат. На карта 2 се отмята сама наум, а продукт още няма, затова „филтърът за реклами“ не се включва. Карта 3 сваля вината. Карта 4 дава най-малкото усилие: 1 лепенка сутрин, не е хапче. Карта 5 маха страха „измама ли е“ с цената с доставката и плащането при доставка → клик. **Риск:** около 70% не плъзгат след карта 1 (AdRiseLab, посока). Затова карта 1 носи hook-а и логото и работи и сама.

---

### VF23-2 · F-011 „Преди да купиш берберин, провери 3 неща“ → VF-008 тетрадка на ръка (1 статична снимка, 4:5)
**Родител:** ugc1 · F-011 провери 3 неща (№2, SIM 33.3; в топ 3 два рунда). **Формат:** статик, истинска снимка.

**Визия:** снимка отгоре на отворена тетрадка на квадратчета, на дървена кухненска маса, сутрешна светлина. Син химикал. Вдясно истинският пакет FitPatches и отвореният сив плик от Еконт със скъсан ръб. Чаша кафе в ъгъла. Почеркът е **истински** (Боян или собственикът), не AI.

**Текст:**
- Лента най-горе (печатен текст, бял на тъмен фон, точно думите на родителя): „Преди да купиш берберин, провери 3 неща.“
- В тетрадката, на ръка:
  „1. Какво пише на кутията?
     → берберин, канела, нар ✓
  2. Как се приема? Всеки ден ли ще го правя?
     → 1 лепенка сутрин, на рамото. Не е хапче. 30 в пакет ✓
  3. Колко излиза? Кога плащам?
     → 14.99 € + доставка. Плащам при доставка ✓
     (3+1 подарък — 39.99 €, безплатна доставка, около 0.33 € на ден)
  Отметнах и трите.“
- Най-долу, печатно и дребно: „Драматизация · Не замества разнообразното хранене и движението. · При лекарства, бременност или кърмене — първо лекарят.“

**Текст под рекламата, заглавия и CTA:** като родителя, текст 2 („Преди да купиш берберин, провери 3 неща. Отнема минута…“), заглавие „Преди да купиш берберин, провери 3 неща“.

**Защо ще работи:**
- F-011 е повторен победител (32.3 → 33.3; 72% срещу S2 на 15:11). В лабораторията е най-евтиният за продукция.
- Ръкописното е от най-силните сигнали в бенчмарка на Motion: Letter 10.83% и ≈1.7× (№2 в Health & Wellness), Post It ≈1.3× при 100+ марки, сред тях Happy Mammoth и Nutrition Geeks. ADM отчита +26% ROAS и −23% цена на поръчка за марка в здраве и красота.
- Клонингите на F-011 по света: Solvéra ×3 (945043961523266), в BG „НЕ ВСЕКИ БЕРБЕРИН Е ЕДНАКЪВ.“ 43 дни.
- Без кредити: една снимка с телефон, 20 минути.

**Как ще подейства:** в лентата не изглежда като реклама, а като чужда маса и чужда тетрадка. Спира жените, които вече проучват берберина. Трите въпроса са техните собствени възражения. Всеки отговор е факт, не обещание: прозрачността маха „магията“, която им е омръзнала. Пликът от Еконт и „плащам при доставка“ казват тихо „пристигна, платих на гишето“, тоест рискът е нулев → клик. **Риск:** думата „берберин“ дърпа фармацевти и критици (N05), а P05 и P08 питат „колко мг?“. Без реалната доза тази точка остава празна.

---

### VF23-3 · S2 „Отговарям на най-честите въпроси“ → VF-011 скрийншот от чат (1 статик, 9:16 + изрязване 4:5)
**Родител:** ugc1 · S2 (шампион, 38.8 → 38.9; сам в рунда №1 с 35.3). **Формат:** статичен скрийншот. Чат без логото на приложението, профил „Деси“ с кръг и инициал „Д“, без снимки на хора. Малък надпис „Драматизация“ горе вляво.

**Балончетата** (сиво вляво = Деси, зелено вдясно = Мария):
1. Деси: „Видях, че си поръчала от тези лепенки. Това не е ли поредната измама от нета?“
2. Мария: „И аз така мислех, хаха. Затова поръчах с плащане при доставка. Платих чак като ги взех от Еконт.“
3. Деси: „Добре де, работят ли изобщо?“
4. Мария: „Не са магия и цифри няма да ти казвам. Но вечер вече не посягам към шоколада като преди.“
5. Деси: „Как се лепи? Вижда ли се?“
6. Мария: „Сутрин, на чиста и суха кожа, всеки ден на различно място. Аз я слагам на рамото, под блузата не се вижда.“
7. Деси: „Колко струва?“
8. Мария: „1 пакет е 14.99 € + доставка, 30 лепенки. Аз взех 3+1 подарък за 39.99 €, с безплатна доставка.“
9. Деси: „А ако не ми хареса?“
10. Мария: „Имат [ГАРАНЦИЯ: 60 или 30?]-дневна гаранция, пише го на сайта. Ще ти пратя линка.“
- Под чата, дребно: „Не замества разнообразното хранене и движението.“
- В 4:5 изрязването остават балончета 1–8, а гаранцията е в текста под рекламата.

**Текст под рекламата, заглавие и CTA:** като родителя, текст 3 („Най-честите въпроси за тези лепенки…“), с поправката от 15:11. Заглавие: „Отговарям на най-честите въпроси“.

**Защо ще работи:**
- S2 е шампионът, защото единствен казва цена, плащане при доставка и как се лепи. Чатът запазва точно тези отговори.
- Диалогът със скептичната приятелка (S3) е №1 на 08:59 (36.3, 66% срещу S2), защото възраженията звучат от друг човек. Чатът събира двете неща: въпросите на S2 и гласа на S3.
- По света: Text Message ползват 20 марки, сред тях AG1, Happy Mammoth, Magic Mind, Perelel и Hims. В Health & Wellness „social post mockup“ е №1 по spend use. Curtis Howland: скрийншотите заобикалят „филтъра за реклами“.
- Без кредити: макет в Figma, 30 минути. Това е ново тяло за S2, тоест отговор на умората от едно тяло (S2 падна до 22.7 с 5 копия на видеото си).

**Как ще подейства:** в лентата изглежда като скрийншот, който приятелка е пратила. Първото сиво балонче е нейното собствено съмнение („измама?“) и тя чете отговора, за да види дали ще я убеди. „Платих като ги взех“ маха риска. После очите търсят цената (балонче 8) и „вижда ли се“ (6). Последното балонче е „ще ти пратя линка“, тоест кликът е естественото следващо действие. **Риск:** ако персоната усети, че чатът е нагласен, доверието пада (панелът го оценява изрично). Гаранцията пак е заместител, затова S2 и VF23-3 са сравними помежду си, но не с варианти без гаранция.

**Комплайънс за трите:** без кг, тяло и срокове; „14.99 € + доставка“; 3+1 само в един ред с 39.99 € и безплатната доставка. Ред за ефекта е само в чата (балонче 4): 1 ред, първо лице, относително, под „Драматизация“. В тетрадката има ред за лекаря, само като надпис. В карусела карта 3 („Не е мързел. Не е характер.“) е точно преди продукта: compliance да реши дали е нужен буфер (ред 49). Резерва: 6 карти, с „Много жени минават през същото.“ като отделна карта между тях. Преди Meta: решение за гаранцията, 3+1 в Shopify, таксата за наложен платеж (ops), истинският етикет.
