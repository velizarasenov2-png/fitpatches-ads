# FitPatches — Скелет реклама: „Апетитът и роклята"

**Продукт:** FitPatches — берберинови лепенки за намаляване на апетита
**Пазар:** България (глас зад кадър и надписи на български)
**Формат:** вертикално 9:16, кратко видео ~35–40 сек
**Визуален стил:** „skeleton" (гланциран порцеланов скелет анимационен герой в изцяло бял минималистичен свят — виж `skeleton-ad-style`)

---

## Сторителинг структура

Класическа дъга **Проблем → Агитация → Отчаяние → Откритие → Механизъм → Трансформация**. Всеки кадър тласка емоцията напред и води логично към следващия — зрителят преживява пътя на героинята, а продуктът се появява като естественото решение, не като реклама, залепена отгоре.

| # | Бийт | Роля в историята |
|---|------|------------------|
| 1 | Пълна скелет-жена се оглежда | Проблем / кука |
| 2 | Мъжът ѝ казва, че е надебеляла | Емоционална рана |
| 3 | Яде от стрес на работа, опитва да се спре | Агитация / провалени опити |
| 4 | Мисли, че нищо не помага на апетита | Отчаяние / фалшиво убеждение |
| 5 | Приятелка: „намалих си апетита с лепенки" | Откритие |
| 6 | Решава да ги пробва — заради него | Желание / мотив |
| 7 | Той не знае — малки, на скрито място | Продуктова полза (дискретност) |
| 8 | Натуралните съставки се отделят, апетитът спада | Механизъм / как работи |
| 9 | Оставя лепенките, отива при мъжа си в хубава рокля | Трансформация / развръзка |

---

## Библия на героите (за консистентност между всички кадри)

- **ГЕРОИНЯТА** — женски скелет с гланцирани млечнобели порцеланови кости, заоблени опростени форми, големи кръгли анимационни очи с малки тъмни зеници, дружелюбни зъбки. Около скелета — **едва забележим полупрозрачен стъклен силует на тялото**; в началото силуетът е **по-заоблен и пълен** (така показваме „надебеляла", без реализъм и без анатомия). В края силуетът е по-стегнат, облечен в елегантна рокля.
- **МЪЖЪТ** — по-едър мъжки скелет, същият материал и стил, леко по-широки рамене.
- **ПРИЯТЕЛКАТА** — женски скелет, различима с друга прическа/аксесоар (напр. светла кърпа/шал), същият гланциран стил.
- **ПРОДУКТЪТ** — берберинова лепенка FitPatches: реалистичен материал, реални цветове на марката и етикет. Единственият фотореалистичен и наситен на цвят обект в белия свят.

**Важно:** това е анимационен, сладък и безобиден скелет — Pixar-мащаб, НЕ медицинска илюстрация, НЕ рентген, без кръв/органи/ужаси. „Пълнотата" и слабостта се предават само чрез стъкления силует, стойката и как стои дрехата.

---

## Многократно използван стилов блок (лепи се в края на всеки промпт)

```
cartoon 3D skeleton character with glossy white porcelain bones, smooth rounded
simplified bone shapes, large round googly cartoon eyes with small dark pupils, friendly
cartoon teeth, faint translucent glassy body silhouette around the skeleton, bright
all-white minimalist interior, white quilted padded wall panels, white furniture, soft
diffuse high-key daylight, no harsh shadows, cool pale blue-white color grade, low
saturation except the product in realistic materials and colors, clean uncluttered
composition, shallow-ish depth of field, vertical 9:16, slow gentle camera move, playful
lighthearted mood, Pixar-like stylized 3D render
```

**Негативен промпт (за всеки кадър):**
```
realistic bone texture, medical illustration, x-ray, anatomy chart, gore, blood, muscles,
organs, horror, scary, dark, dramatic shadows, moody lighting, black background, neon glow,
cluttered background, gritty, photorealistic skeleton, baked-in text, garbled letters
```

**Надписи:** добавят се в пост-продукция като истински текстов слой (заоблена сиво-бяла „хапче"-кутийка, долна трета, тъмен bold sans-serif), синхронизирани с гласа. Никога не се разчита на текст, генериран от видео модела.

---

## Разкадровка (shot-by-shot)

### Кадър 1 — Проблемът · ~4 сек
**Действие:** Героинята стои пред високо бяло огледало в спалня, обръща се леко настрани и се оглежда; по-пълният стъклен силует и стойката издават притеснение. Големите очи гледат тъжно надолу.
**Камера:** бавно приближаване (push-in) към отражението.
**Надпис:** `Напоследък не се харесвах…`
**Глас (жена, зад кадър):** „Знаех, че съм понапълняла. Просто не исках да си го призная."

> **Промпт:** A female skeleton stands in front of a tall white mirror in an all-white bedroom, turning slightly to the side and studying her fuller rounded glassy body silhouette with a worried look, big cartoon eyes glancing down, slow push-in toward the reflection, [СТИЛОВ БЛОК]

---

### Кадър 2 — Раната · ~4 сек
**Действие:** Мъжът-скелет седи на белия диван; обръща глава към нея и казва нещо направо. Тя застива, очите ѝ се разширяват, раменете леко се свиват.
**Камера:** среден план на двамата, лек статичен кадър.
**Надпис:** `„Понапълняла си…"`
**Глас (мъж, в кадър):** „Понапълняла си, любов."
**Глас (жена, зад кадър):** „Каза го без злоба. Но заболя."

> **Промпт:** A larger male skeleton sits on a white sofa and turns his head to speak gently to a female skeleton standing beside him; she freezes, her big cartoon eyes widen and shoulders shrink slightly, medium two-shot, locked-off camera, [СТИЛОВ БЛОК]

---

### Кадър 3 — Агитация · ~5 сек
**Действие:** Героинята на бяло бюро/офис, стресирана, посяга и хапе от закуска; после решително оставя опаковката настрани, опитвайки да се спре — но ръката ѝ пак се връща към нея.
**Камера:** среден план, лек ръчен усет.
**Надпис:** `Ядях заради стреса… и не можех да спра.`
**Глас (жена):** „Работата ме стресираше и посягах към храна непрекъснато. Опитвах се да се спра… напразно."

> **Промпт:** A female skeleton at a clean white office desk looks stressed, reaches for a snack and nibbles, then firmly pushes the snack away trying to restrain herself, but her hand drifts back toward it, expressive frustrated cartoon eyes, medium shot with subtle handheld feel, [СТИЛОВ БЛОК]

---

### Кадър 4 — Отчаянието · ~4 сек
**Действие:** Едър план на черепа; очите гледат право в камерата, уморени и примирени. Лек въздишащ жест с ръка.
**Камера:** бавно приближаване към лицето (сигнатурен близък план на очите).
**Надпис:** `Мислех, че нищо няма да ми помогне.`
**Глас (жена):** „Бях сигурна, че нищо не може да укроти този апетит."

> **Промпт:** Tight close-up on a female skeleton skull, tired resigned big cartoon eyes looking straight into camera, a small sighing hand gesture, slow push-in on the face, [СТИЛОВ БЛОК]

---

### Кадър 5 — Откритието · ~5 сек
**Действие:** Приятелката-скелет (със светъл шал) сяда до нея с две бели чаши; навежда се и споделя с усмивка, посочвайки нещо. Героинята вдига поглед с искра любопитство.
**Камера:** среден план на двете, лек орбитален завой.
**Надпис:** `Приятелка ми сподели нещо.`
**Глас (приятелка, в кадър):** „Аз си намалих апетита… с едни лепенки."
**Глас (жена, зад кадър):** „И изведнъж се появи надежда."

> **Промпт:** A female skeleton friend with a light headscarf sits down beside her holding two white cups, leans in and shares something with a friendly smile while gesturing, the heroine looks up with a spark of curiosity in her big cartoon eyes, medium two-shot with a slow gentle orbit, [СТИЛОВ БЛОК]

---

### Кадър 6 — Желанието · ~4 сек
**Действие:** Героинята държи опаковката FitPatches на нивото на гърдите към камерата, оглежда я решително; в отражението/ума ѝ проблясва мъжът ѝ. Очите ѝ светват с решимост.
**Камера:** близък план на продукта в ръце, после нагоре към лицето.
**Надпис:** `Реших да ги пробвам — заради него. И заради мен.`
**Глас (жена):** „Реших да опитам. Исках отново да се харесвам — и той да ме гледа както преди."

> **Промпт:** A female skeleton holds up a realistic FitPatches berberine patch pack at chest height facing camera, examining it with determination, her big cartoon eyes lighting up with resolve, the product is the only saturated real-material object, close-up on the pack then tilt up to the face, [СТИЛОВ БЛОК]

---

### Кадър 7 — Дискретността · ~5 сек
**Действие:** Героинята залепва малка лепенка на скрито място (напр. отстрани на кръста/бедрото под дрехата). Дрехата на това място става леко **прозрачна**, за да се види лепенката отдолу — после отново непрозрачна. Мъжът минава на заден план, без да забележи.
**Камера:** среден план; кратко „надникване" през прозрачната дреха към лепенката.
**Надпис:** `Малки и незабележими — слагаш ги на скрито.`
**Глас (жена):** „Толкова са малки, че никой не разбира. Слагаш ги на скрито място — а той дори не подозира."

> **Промпт:** A female skeleton discreetly applies a small realistic FitPatches patch on a hidden spot on her side/hip under her clothing; the fabric over that exact spot turns briefly translucent to reveal the patch underneath, then becomes opaque again, the male skeleton passes in the soft-focus background without noticing, medium shot, [СТИЛОВ БЛОК]

---

### Кадър 8 — Механизмът · ~5 сек
**Действие:** Полу-макро към лепенката върху тялото: от нея се отделят нежни светли частици/съставки, които потъват навътре. Стъкленият силует показва как усещането за глад утихва (символично — малки „вълнички", които се успокояват). Героинята въздъхва облекчено.
**Камера:** бавно приближаване към лепенката, после назад към спокойното ѝ лице.
**Надпис:** `Натуралните съставки на берберина намаляват апетита.`
**Глас (жена):** „Натуралните съставки на берберина се отделят бавно и апетитът просто утихва."

> **Промпт:** Semi-macro on the realistic FitPatches patch on the skeleton's body, gentle glowing natural ingredient particles releasing from the patch and absorbing inward through the translucent glassy silhouette, small ripples calming down to symbolize hunger fading, the heroine exhales with relief, slow push-in on the patch then pull back to her calm face, [СТИЛОВ БЛОК]

---

### Кадър 9 — Трансформацията · ~5 сек
**Действие:** На преден план героинята (сега с по-стегнат силует, в елегантна **хубава рокля**) оставя опаковката берберинови лепенки FitPatches върху бял шкаф, усмихва се и на заден план тръгва към мъжа си, който я гледа възхитено. Той протяга ръка към нея.
**Камера:** широк план; фокусът плавно преминава от лепенките на шкафа към двойката отзад.
**Надпис:** `FitPatches — отново си харесвам.`
**Глас (жена):** „Днес отново съм си аз. А той пак ме гледа както преди."
**Краен надпис / CTA:** `FitPatches · берберинови лепенки`

> **Промпт:** In the foreground a slimmer female skeleton in an elegant nice dress sets a realistic FitPatches berberine patch pack down on a white cabinet, smiles, then in the soft-focus background walks toward the male skeleton who looks at her admiringly and reaches out his hand; rack focus from the pack on the cabinet to the couple behind, wide shot, warm happy resolution, [СТИЛОВ БЛОК]

---

## Продукционни бележки

- **Консистентност:** използвай един и същ референтен кадър на героинята (image-to-video pipeline), за да е един и същ герой във всички 9 кадъра. Смяната става само в силуета (пълен → стегнат) и облеклото.
- **Продукт:** дръж лепенката/опаковката фотореалистична и с реалните цветове на FitPatches — тя е единственото цветно петно в белия свят и трябва да „грабва" окото.
- **Тон:** топъл, човешки, леко хумористичен — контрастът „скелет говори за апетит и любов" е част от чара; никога не изпадай в ужас или медицинщина.
- **Надписи и глас:** български, кратки фрази, синхронизирани; надписите се добавят в пост-продукция като текстов слой, не от видео модела.
- **Музика:** мека, ведра, лек оптимистичен ъндъртон; повдига се в кадър 8–9 при трансформацията.
