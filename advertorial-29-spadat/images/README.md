# Снимки за адверториал 29 „Спадът“

Сложете файловете в тази папка с **точно тези имена**. Докато някоя липсва, страницата показва сиво поле с описание какво трябва да има там.

**Формат:** JPG или WebP, до ~150 KB всяка (компресирайте със squoosh.app). Цялата страница трябва да остане под 1.5 MB, защото около 42% от кликовете се губят, преди страницата да се зареди.

| Файл | Размер | Какво показва | Реална или генерирана |
|---|---|---|---|
| `01-hero.jpg` | 1200×800 | Жена ~45–50 г. в кухнята вечер, от гърдите нагоре, замислена, с чаша в ръка. Топла светлина, обикновена българска кухня. | AI/стокова, с надпис „Илюстративна снимка“ (вече е на страницата) |
| `02-hladilnik.jpg` | 1200×800 | Тъмна кухня, светлината идва само от отворения хладилник. Ръка посяга към рафта. **Без лице и без тяло в кадър.** | AI/стокова |
| `03-berberis.jpg` | 1200×800 | Берберис (кисел трън): клонка с продълговати червени плодове и разрязан жълт корен. Светъл фон. | Стокова |
| `04-lepenka-ramo.jpg` | 1200×800 | Сутрин: ръка лепи розовата кръгла лепенка FitPatches на рамото или горната част на ръката, до нея чаша кафе. Близък план. | **Реална** (истинската лепенка) |
| `05-stapka-1.jpg` | 600×600 | Чиста кожа на рамото или горната част на ръката. | Реална |
| `06-stapka-2.jpg` | 600×600 | Пръсти притискат лепенката към кожата. | Реална |
| `07-stapka-3.jpg` | 600×600 | Жена в ежедневието (офис или разходка), лепенката едва се вижда на ръката. | Реална или AI |

## Правила за снимките (за да мине в Meta)
- **Без** снимки „преди/след“, кантари, метри, хващане на корем и кадри под гърдите.
- Лепенката е на **рамото или горната част на ръката**, не на корема.
- Продуктът и лепенката са **истинските** (без ретуш на опаковката).
- Хора от AI или стокови снимки **не** се представят като реални клиентки. Надписът „Илюстративна снимка“ остава.

## Промптове за генериране (Higgsfield / Nano Banana)
**01-hero:** `Photorealistic candid photo of a Bulgarian woman in her late 40s standing in a modest home kitchen in the evening, warm tungsten light, holding a mug of tea, thoughtful expression looking slightly away from camera, framed from the chest up, natural skin texture, no makeup look, shallow depth of field, 3:2`

**02-hladilnik:** `Dark home kitchen at night, the only light comes from an open refrigerator, a woman's hand reaching toward a shelf with cheese and leftovers, no face visible, no body visible, moody cinematic lighting, photorealistic, 3:2`

**03-berberis:** `Close-up of a barberry branch (Berberis vulgaris) with elongated red berries next to a cut piece of bright yellow root, on a light linen background, natural daylight, botanical editorial photo, 3:2`

**07-stapka-3:** `Photorealistic photo of a woman in her 40s walking in a park in the morning, casual clothes, small round pink patch barely visible on her upper arm, natural light, candid, square 1:1`

## Преди пускане
- [ ] ЕИК и адрес на управление във футъра (`[ЕИК]`, `[адрес на управление]`; жълто маркирани в страницата)
- [ ] Гаранцията: 30 или 60 дни? На страницата е 30. Трябва да съвпада с продуктовата страница.
- [ ] Съставките (берберин, канела, нар) да съвпадат дословно с етикета
- [ ] Цените и пакетите (14,99 / 27,99 / 39,99 € за 3+1) да съвпадат с Shopify
- [ ] Реални отзиви: добавете ги в скритата секция „Какво казват клиентките“ и махнете `hidden`
