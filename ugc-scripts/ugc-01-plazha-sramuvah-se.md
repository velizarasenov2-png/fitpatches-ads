# UGC ВИДЕО #01 — „Миналото лято за първи път не си свалих ризата на плажа"

**Продукт:** FitPatches (берберинови пластири)
**Формат:** вертикално 9:16, UGC / talking head, снимано „с iPhone 12"
**Героиня:** жена на 45, обикновена външност, не модел
**Общо:** 26 сцени · ~226 секунди суров материал · ~3:10 след изрязване на паузите
**Модели:** първи кадър → **gptimage2** · видео → **omniflash** (image-to-video)

---

## КАК СЕ ПУСКА В KIE (прочети веднъж, после само копираш)

1. **Kie → gptimage2 (Text to Image).** Пействаш `КАДЪР` промпта на сцената. Формат **9:16** (ако няма 9:16 — избери 2:3 и после кропни). Сваляш картинката.
2. **ВАЖНО за консистентност на лицето:** генерирай **първо СЦЕНА 01**. Като си харесаш лицето, за всички останали сцени пускаш gptimage2 в режим **Image Edit / с референтна снимка** — качваш кадъра от Сцена 01 + пействаш промпта на новата сцена и добавяш най-отгоре:
   `Use the woman from the reference image. Keep her face, age, body type and hair identical. Only change the location, clothes and pose as described below.`
   Без това всяка сцена ще е различна жена.
3. **Kie → omniflash (Image to Video).** Качваш кадъра от стъпка 1 + пействаш `ВИДЕО` промпта. Дължина = секундите, изписани в заглавието на сцената. Резолюция **720p** (не 1080p — по-мърлявото качество работи по-добре за UGC).
4. Сглобяваш 26-те клипа по ред, режеш мъртвите паузи в началото/края на всеки клип (там ще имаш по ~1–1.5 сек луфт — това е нарочно).

**Две неща, които не бива да променяш:**
- Репликите се пействат **буквално** — числата са изписани с думи („тридесет и три", „шейсет дневен"), за да не ги изчете грешно моделът.
- „FitPatches" е написано **ФитПачис** в репликата, за да го произнесе по български. На екран после слагаш логото в монтажа.

**За продукта:** кутията в промптите е описана **без четим текст** нарочно — AI видео моделите пишат буквите разкривени. Реалната кутия/пластир я слагаш на монтаж (freeze frame + твоя packshot) в сцени 15, 16, 23, 25.

---

## БЛОКОВЕ, КОИТО СЕ ПОВТАРЯТ (вече са вградени във всеки промпт — тук са само за справка)

**CHARACTER LOCK**
> 45-year-old Bulgarian woman, ordinary plain looks, not a model, not attractive in a commercial way. Full round face, soft double chin, overweight body (EU size 46), broad shoulders, heavy upper arms. Shoulder-length dyed light-brown hair with visible grey roots at the parting, slightly frizzy. Small hazel-brown eyes, thin sparse eyebrows, crow's feet, nasolabial lines, mild under-eye shadows, visible skin pores, a few sun spots on the cheeks, a small mole above the right corner of her mouth, thin lips, no makeup. Short unpainted nails, thin gold wedding band, small stud earrings.

**LOOK**
> Amateur UGC selfie video shot on an iPhone 12 front camera, 1080p downscaled, slightly soft and lo-fi, visible digital noise in the shadows, flat unedited colours, slight overexposure on the skin from raw daylight, no colour grading, no shallow depth of field, no bokeh, no professional lighting. Vertical 9:16, arm's-length framing, head slightly off-centre, imperfect handheld. Looks like a real woman filming herself on her phone, not like an ad.

**NEGATIVE**
> no text, no captions, no subtitles, no watermark, no logo, no on-screen graphics, no readable writing, not a model, no beauty retouch, no smooth plastic skin, no studio lighting, no cinematic look.

---
---

## СЦЕНА 01 — 8 секунди

**Ситуация:** върви по алея в парка, снима се на протегната ръка (движение = скрол-стопер)
**Реплика:** „Миналото лято за първи път не си свалих ризата на плажа. Не защото ми беше студено."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. A 45-year-old Bulgarian woman, ordinary plain looks, not a model: full round face, soft double chin, overweight body (EU size 46), heavy upper arms, shoulder-length dyed light-brown hair with visible grey roots at the parting, slightly frizzy, small hazel-brown eyes, thin sparse eyebrows, crow's feet, mild under-eye shadows, visible skin pores, sun spots on the cheeks, a small mole above the right corner of her mouth, thin lips, no makeup, small stud earrings, thin gold wedding band. She wears a loose navy-blue cotton t-shirt and a light cardigan. She is walking along a paved alley in a city park, holding the phone at arm's length slightly above eye level, looking into the lens, mouth open mid-sentence. Behind her: green trees, a park bench, a blurry passer-by far away, overcast soft daylight. Shot on an iPhone 12 front camera, 1080p, slightly soft and lo-fi, digital noise in the shadows, flat unedited colours, slight overexposure on the skin, no colour grading, no bokeh, no professional lighting, imperfect handheld framing, head slightly off-centre. Looks like a real woman filming herself, not an ad. No text, no captions, no watermark, no logo, not a model, no beauty retouch, no smooth plastic skin.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same park. She walks slowly forward holding the phone at arm's length and talks straight into the camera. Natural head movements, blinks, one small shrug, real speech mouth shapes. The phone is handheld while walking so the frame bounces and drifts slightly, background trees move past her.
DIALOGUE (Bulgarian, spoken exactly as written, nothing added, nothing skipped): „Миналото лято за първи път не си свалих ризата на плажа. Не защото ми беше студено."
VOICE: real 45-year-old Bulgarian woman, warm slightly hoarse mid-tone, conversational and confiding, unpolished, not an announcer. Slightly embarrassed, like admitting something to a friend.
AUDIO: only her voice plus faint outdoor park ambience. No music.
CAMERA: handheld selfie, one continuous take, no cuts, no zoom.
NEGATIVE: no subtitles, no captions, no on-screen text, no watermark, no music, no other person speaking, no scene change, no beauty filter, no slow motion.
```

---

## СЦЕНА 02 — 8 секунди

**Ситуация:** седнала на пейка в парка, телефонът подпрян
**Реплика:** „А защото ме беше срам да ме видят. Едно време бях първата, която скачаше във водата."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, overweight body (EU size 46), shoulder-length dyed light-brown hair with grey roots, small hazel-brown eyes, crow's feet, visible pores, small mole above the right corner of her mouth, no makeup. Same navy-blue t-shirt and light cardigan. She is sitting on a wooden park bench, slightly slouched, hands in her lap, looking into the phone camera which is propped up in front of her at chest height, talking. Behind her: park path, green bushes, autumn leaves on the ground, soft overcast daylight. Shot on an iPhone 12, 1080p, slightly soft, digital noise in the shadows, flat unedited colours, no colour grading, no bokeh, no professional lighting, slightly crooked framing. Looks like a real woman filming herself, not an ad. No text, no captions, no watermark, no logo, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same bench. She sits and talks into the phone, looks down for half a second when she says the shameful part, then back into the lens. Small hand gesture, blinks, natural speech mouth shapes. Phone is propped up so the frame is almost static with a tiny drift.
DIALOGUE (Bulgarian, spoken exactly as written): „А защото ме беше срам да ме видят. Едно време бях първата, която скачаше във водата."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, conversational. First sentence quiet and ashamed, second sentence a little warmer, almost a smile at the memory.
AUDIO: only her voice plus faint park ambience, distant birds. No music.
CAMERA: static handheld-propped selfie, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no watermark, no music, no scene change, no beauty filter.
```

---

## СЦЕНА 03 — 8 секунди

**Ситуация:** на маса пред кафене (тераса, картонена чаша кафе)
**Реплика:** „Намазвах се със слънцезащитно и право в морето, без да се замислям. А сега седя облечена на шезлонга."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, overweight (EU size 46), shoulder-length dyed light-brown hair with grey roots, small hazel-brown eyes, crow's feet, visible pores, small mole above the right corner of her mouth, no makeup, stud earrings. She wears a burgundy short-sleeve blouse. She is sitting at a small round outdoor table on a coffee-shop terrace, a plain white takeaway coffee cup and her keys on the table, one hand around the cup, looking into the phone camera held at arm's length, talking. Background: café terrace chairs, a shop window, a city street, people blurred in the distance, bright daylight with harsh reflections. Shot on an iPhone 12, 1080p, slightly soft and lo-fi, digital noise, flat unedited colours, slight overexposure on the skin, no colour grading, no bokeh, no professional lighting. Looks like a real woman filming herself, not an ad. No text, no captions, no readable writing, no brand logo, no watermark, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same café terrace. She talks into the camera, lifts the coffee cup once and puts it back down, small tired half-smile on the last sentence. Blinks, natural head movement, real speech mouth shapes. Handheld phone drifts slightly.
DIALOGUE (Bulgarian, spoken exactly as written): „Намазвах се със слънцезащитно и право в морето, без да се замислям. А сега седя облечена на шезлонга."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, conversational. First half nostalgic and lively, second half flat and resigned.
AUDIO: only her voice plus faint street and café ambience. No music.
CAMERA: handheld selfie at arm's length, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no watermark, no music, no scene change, no beauty filter.
```

---

## СЦЕНА 04 — 8 секунди

**Ситуация:** в колата, паркирана, на шофьорското място
**Реплика:** „В тридесет и три градуса пек. Не ми пука толкова за килограмите — те са само цифра."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, overweight (EU size 46), shoulder-length dyed light-brown hair with grey roots, tucked behind one ear, small hazel-brown eyes, crow's feet, visible pores, small mole above the right corner of her mouth, no makeup. She wears a plain grey t-shirt and a seatbelt. She is sitting in the driver's seat of an ordinary older parked car, holding the phone slightly above her face, looking into the lens, talking. Background: car headrest, side window with a sunny parking lot and blocks of flats outside, harsh daylight coming through the windscreen, small dashboard clutter. Shot on an iPhone 12 front camera, 1080p, slightly soft, digital noise, flat unedited colours, blown-out window highlights, no colour grading, no bokeh, no professional lighting. Looks like a real woman filming herself in her car, not an ad. No text, no captions, no watermark, no logo, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same car interior. She talks into the phone, raises her eyebrows on the first line, then makes a small dismissive hand wave on the second. Blinks, natural micro head movement, real speech mouth shapes. Slight handheld shake.
DIALOGUE (Bulgarian, spoken exactly as written): „В тридесет и три градуса пек. Не ми пука толкова за килограмите — те са само цифра."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, conversational, a bit sarcastic on the first line, matter-of-fact on the second.
AUDIO: only her voice plus faint car interior ambience. No music.
CAMERA: handheld selfie in a car, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no watermark, no music, no driving, no scene change, no beauty filter.
```

---

## СЦЕНА 05 — 10 секунди

**Ситуация:** у тях, седнала на дивана, вечер
**Реплика:** „Най-лошото е, че бавно спрях да правя нещата, които обичам. И си измислях причини, за да не си признавам истинския проблем."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, overweight (EU size 46), shoulder-length dyed light-brown hair with grey roots, loose and a bit messy, small hazel-brown eyes, crow's feet, under-eye shadows, visible pores, small mole above the right corner of her mouth, no makeup. She wears a soft oversized dark-green sweatshirt. She is sitting on a beige fabric sofa in an ordinary modest Bulgarian living-room, legs tucked under her, a folded blanket and a cushion beside her, holding the phone at chest height, looking into the lens, talking. Background: living-room wall, a framed family photo, a small lamp, warm indoor light in the evening. Shot on an iPhone 12, 1080p, slightly soft and grainy in the low light, flat unedited colours, no colour grading, no bokeh, no professional lighting. Looks like a real woman filming herself at home, not an ad. No text, no captions, no watermark, no logo, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same sofa. She talks into the phone quietly, looks away once, gives a small resigned sigh between the two sentences, tucks a strand of hair behind her ear. Blinks, natural head movement, real speech mouth shapes. Small handheld drift.
DIALOGUE (Bulgarian, spoken exactly as written): „Най-лошото е, че бавно спрях да правя нещата, които обичам. И си измислях причини, за да не си признавам истинския проблем."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, quiet, honest, a little heavy — like a confession late in the evening.
AUDIO: only her voice plus quiet room tone. No music.
CAMERA: handheld selfie, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no watermark, no music, no scene change, no beauty filter.
```

---

## СЦЕНА 06 — 10 секунди

**Ситуация:** на балкона сутрин, книга и кафе на масичката
**Реплика:** „На плажа приятелките ми ме викаха: „Ела бе, стига си седяла!" Казах им, че искам да си дочета главата от книгата."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, overweight (EU size 46), shoulder-length dyed light-brown hair with grey roots, tied in a loose low ponytail, small hazel-brown eyes, crow's feet, visible pores, small mole above the right corner of her mouth, no makeup. She wears a light-blue housecoat over a t-shirt. She is sitting on a small balcony of a Bulgarian apartment block, at a tiny plastic table with a mug of coffee and a closed paperback book on it, holding the phone at arm's length, looking into the lens, talking. Background: balcony railing, drying laundry on a rack, neighbouring apartment blocks and a tree, bright morning daylight. Shot on an iPhone 12, 1080p, slightly soft, digital noise, flat unedited colours, slightly overexposed sky, no colour grading, no bokeh, no professional lighting. Looks like a real woman filming herself, not an ad. No text, no captions, no readable writing on the book, no watermark, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same balcony. She talks into the camera, does a small mocking imitation voice gesture when she quotes her friends, then rolls her eyes slightly at herself on the second sentence. Blinks, natural head movement, real speech mouth shapes. Handheld drift, laundry moves faintly in the breeze.
DIALOGUE (Bulgarian, spoken exactly as written, keep the quoted part in the same voice): „На плажа приятелките ми ме викаха: Ела бе, стига си седяла! Казах им, че искам да си дочета главата от книгата."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, conversational. Playful when quoting the friends, then flat and slightly guilty on the excuse.
AUDIO: only her voice plus faint outdoor morning ambience. No music.
CAMERA: handheld selfie, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no watermark, no music, no second person on screen, no scene change, no beauty filter.
```

---

## СЦЕНА 07 — 8 секунди

**Ситуация:** седнала на стъпалата пред входа на блока
**Реплика:** „Останах под чадъра, докато те си говореха и се забавляваха в морето."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, overweight (EU size 46), shoulder-length dyed light-brown hair with grey roots, small hazel-brown eyes, crow's feet, visible pores, small mole above the right corner of her mouth, no makeup. She wears a simple black t-shirt and dark trousers. She is sitting on the concrete steps in front of the entrance of an old Bulgarian apartment block, elbows on her knees, holding the phone slightly below eye level so the angle is unflattering, looking into the lens, talking. Background: entrance door, mailboxes, a bit of grass and parked cars, flat late-afternoon daylight. Shot on an iPhone 12, 1080p, slightly soft and lo-fi, digital noise, flat unedited colours, no colour grading, no bokeh, no professional lighting, slightly tilted framing. Looks like a real woman filming herself, not an ad. No text, no captions, no watermark, no logo, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same steps. She talks into the phone, looks slightly down and to the side as she remembers, small shrug at the end. Blinks, natural head movement, real speech mouth shapes. Handheld drift.
DIALOGUE (Bulgarian, spoken exactly as written): „Останах под чадъра, докато те си говореха и се забавляваха в морето."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, quiet and a bit lonely, no self-pity.
AUDIO: only her voice plus faint outdoor street ambience. No music.
CAMERA: handheld selfie from a low angle, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no watermark, no music, no scene change, no beauty filter.
```

---

## СЦЕНА 08 — 10 секунди

**Ситуация:** вкъщи, в креслото до прозореца, книгата в скута
**Реплика:** „Четох една и съща страница десет минути. Не защото беше интересна, а защото се чудех дали не ме обсъждат."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, overweight (EU size 46), shoulder-length dyed light-brown hair with grey roots, small hazel-brown eyes, crow's feet, under-eye shadows, visible pores, small mole above the right corner of her mouth, no makeup. She wears a mustard-yellow knitted cardigan. She is sitting in an old armchair next to a window, an open paperback book resting face-down on her lap, holding the phone at chest height, looking into the lens, talking. Background: net curtain, window light on one side of her face, a radiator, a plant on the windowsill, ordinary Bulgarian flat interior. Shot on an iPhone 12, 1080p, slightly soft, digital noise in the shadow side of the face, flat unedited colours, window highlights blown out, no colour grading, no bokeh, no professional lighting. Looks like a real woman filming herself, not an ad. No text, no captions, no readable writing on the book, no watermark, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same armchair. She talks into the phone, taps the book on her lap once with two fingers on the first sentence, then a short uncomfortable pause before the second sentence, small nervous half-smile at the end. Blinks, natural head movement, real speech mouth shapes. Handheld drift.
DIALOGUE (Bulgarian, spoken exactly as written): „Четох една и съща страница десет минути. Не защото беше интересна, а защото се чудех дали не ме обсъждат."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, low and vulnerable, slows down on the last words.
AUDIO: only her voice plus quiet room tone. No music.
CAMERA: handheld selfie, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no watermark, no music, no scene change, no beauty filter.
```

---

## СЦЕНА 09 — 8 секунди

**Ситуация:** на кухненската маса, отворен лаптоп с фитнес клип
**Реплика:** „Прибрах се от тази почивка и започнах пак. Диети, ютуб инструктори, следене на калории."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, overweight (EU size 46), shoulder-length dyed light-brown hair with grey roots, small hazel-brown eyes, crow's feet, visible pores, small mole above the right corner of her mouth, no makeup. She wears a plain white t-shirt. She is sitting at an ordinary kitchen table, an open laptop turned away from the camera beside her, a notebook, a pen and a kitchen scale on the table, holding the phone at arm's length, looking into the lens, talking. Background: modest Bulgarian kitchen, cupboards, a kettle, a fridge with magnets, plain ceiling light. Shot on an iPhone 12, 1080p, slightly soft, digital noise, flat unedited colours, yellowish indoor white balance, no colour grading, no bokeh, no professional lighting. Looks like a real woman filming herself, not an ad. No text, no captions, no readable writing on the screen or the notebook, no watermark, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same kitchen. She talks into the phone and counts the three things off on her fingers as she lists them, small tired smile. Blinks, natural head movement, real speech mouth shapes. Handheld drift.
DIALOGUE (Bulgarian, spoken exactly as written): „Прибрах се от тази почивка и започнах пак. Диети, ютуб инструктори, следене на калории."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, conversational, slightly faster pace, a bit self-ironic on the list.
AUDIO: only her voice plus quiet kitchen room tone. No music.
CAMERA: handheld selfie, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no watermark, no music, no scene change, no beauty filter.
```

---

## СЦЕНА 10 — 8 секунди

**Ситуация:** в спалнята, седнала на ръба на леглото, кантар на пода
**Реплика:** „Свалях по два килограма, връщах три. По някое време разбрах нещо, което дотогава никой не ми беше казвал."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, overweight (EU size 46), shoulder-length dyed light-brown hair with grey roots, slightly messy, small hazel-brown eyes, crow's feet, under-eye shadows, visible pores, small mole above the right corner of her mouth, no makeup. She wears a grey pyjama top. She is sitting on the edge of an unmade bed in a modest bedroom, a white bathroom scale on the floor near her bare feet, holding the phone at arm's length, looking into the lens, talking. Background: bedroom wall, wardrobe door, a chair with clothes on it, soft morning light through the curtains. Shot on an iPhone 12, 1080p, slightly soft, digital noise, flat unedited colours, no colour grading, no bokeh, no professional lighting. Looks like a real woman filming herself, not an ad. No text, no captions, no readable numbers on the scale, no watermark, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same bedroom. She talks into the phone, glances down at the scale on the first sentence, then leans slightly closer to the camera on the second sentence as if letting the viewer in on something. Blinks, natural head movement, real speech mouth shapes. Handheld drift.
DIALOGUE (Bulgarian, spoken exactly as written): „Свалях по два килограма, връщах три. По някое време разбрах нещо, което дотогава никой не ми беше казвал."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse. Flat and defeated on the first sentence, then quieter and more intriguing on the second — a small cliffhanger.
AUDIO: only her voice plus quiet room tone. No music.
CAMERA: handheld selfie, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no watermark, no music, no scene change, no beauty filter.
```

---

## СЦЕНА 11 — 8 секунди

**Ситуация:** кухнята вечерта, застанала до отворения хладилник
**Реплика:** „Проблемът ми не беше волята. Проблемът беше постоянният глад. Цял ден се мъчех да издържа."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, overweight (EU size 46), shoulder-length dyed light-brown hair with grey roots, small hazel-brown eyes, crow's feet, visible pores, small mole above the right corner of her mouth, no makeup. She wears a dark long-sleeve top. She is standing in a dim kitchen at night next to a half-open fridge, the cold fridge light falling on one side of her face and body, holding the phone at arm's length, looking into the lens, talking. Background: dark kitchen, cupboards, a window with night outside, the lit interior of the fridge with ordinary food. Shot on an iPhone 12 front camera in low light, 1080p, soft and noticeably grainy, mixed colour temperature, flat unedited colours, no colour grading, no bokeh, no professional lighting. Looks like a real woman filming herself at night, not an ad. No text, no captions, no readable labels, no watermark, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same kitchen. She talks into the phone, shakes her head slightly on the first sentence, closes the fridge door with her free hand near the end. Blinks, natural head movement, real speech mouth shapes. Handheld drift, the light on her face changes slightly as the fridge closes.
DIALOGUE (Bulgarian, spoken exactly as written): „Проблемът ми не беше волята. Проблемът беше постоянният глад. Цял ден се мъчех да издържа."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, firm and clear — this is the point of the whole story, not a complaint.
AUDIO: only her voice plus faint fridge hum. No music.
CAMERA: handheld selfie in low light, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no watermark, no music, no scene change, no beauty filter.
```

---

## СЦЕНА 12 — 10 секунди

**Ситуация:** на работа, седнала на бюрото в пауза
**Реплика:** „И не, това не е слабост на характера. Апетитът просто се управлява от процеси, които не решаваш съзнателно."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, overweight (EU size 46), shoulder-length dyed light-brown hair with grey roots, pinned back, small hazel-brown eyes, crow's feet, visible pores, small mole above the right corner of her mouth, minimal worn-off makeup. She wears a simple dark-blue office blouse. She is sitting at an ordinary office desk during a break, a monitor turned away from the camera, a mug and papers on the desk, holding the phone at arm's length, looking into the lens, talking quietly. Background: plain office wall, a shelf with folders, cold fluorescent ceiling light, a window with grey daylight. Shot on an iPhone 12, 1080p, slightly soft, digital noise, flat unedited colours, greenish fluorescent tint, no colour grading, no bokeh, no professional lighting. Looks like a real woman filming herself at work, not an ad. No text, no captions, no readable writing on the papers or screen, no watermark, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same office. She talks into the phone in a lowered voice as if colleagues are nearby, one firm hand gesture on the first sentence, glances briefly off to the side once. Blinks, natural head movement, real speech mouth shapes. Handheld drift.
DIALOGUE (Bulgarian, spoken exactly as written): „И не, това не е слабост на характера. Апетитът просто се управлява от процеси, които не решаваш съзнателно."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, lowered volume, calm and convinced — explaining, not selling.
AUDIO: only her voice plus faint office room tone. No music.
CAMERA: handheld selfie, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no watermark, no music, no other person speaking, no scene change, no beauty filter.
```

---

## СЦЕНА 13 — 8 секунди

**Ситуация:** до кафемашината в офиса
**Реплика:** „Един ден си преглътнах егото и попитах една колежка как успява да яде толкова малко."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, overweight (EU size 46), shoulder-length dyed light-brown hair with grey roots, pinned back, small hazel-brown eyes, crow's feet, visible pores, small mole above the right corner of her mouth, minimal makeup. Same dark-blue office blouse. She is standing in a small office kitchenette next to a coffee machine, holding a paper cup in one hand and the phone at arm's length in the other, looking into the lens, talking. Background: kitchenette counter, sink, a microwave, a few mugs, cold ceiling light. Shot on an iPhone 12, 1080p, slightly soft, digital noise, flat unedited colours, mixed indoor light, no colour grading, no bokeh, no professional lighting, slightly crooked framing. Looks like a real woman filming herself at work, not an ad. No text, no captions, no readable labels, no watermark, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same kitchenette. She talks into the phone, gives a small embarrassed smile on "преглътнах егото", takes half a sip from the cup at the end. Blinks, natural head movement, real speech mouth shapes. Handheld drift.
DIALOGUE (Bulgarian, spoken exactly as written): „Един ден си преглътнах егото и попитах една колежка как успява да яде толкова малко."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, conversational, slightly embarrassed but light.
AUDIO: only her voice plus faint office kitchenette ambience. No music.
CAMERA: handheld selfie, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no watermark, no music, no other person on screen, no scene change, no beauty filter.
```

---

## СЦЕНА 14 — 10 секунди

**Ситуация:** в коридора на офиса, до асансьора
**Реплика:** „Тя си вдигна ръкава и видях една розова лепенка. Каза ми, че точно това ѝ е помогнало да свали килограмите."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, overweight (EU size 46), shoulder-length dyed light-brown hair with grey roots, small hazel-brown eyes, crow's feet, visible pores, small mole above the right corner of her mouth, minimal makeup. Same dark-blue office blouse. She is standing in an office corridor next to a lift, leaning one shoulder against the wall, holding the phone at arm's length, looking into the lens, talking, her free hand touching her own upper arm through the sleeve as if showing where something was. Background: plain corridor, lift doors, a fire extinguisher, cold ceiling light. Shot on an iPhone 12, 1080p, slightly soft, digital noise, flat unedited colours, no colour grading, no bokeh, no professional lighting. Looks like a real woman filming herself, not an ad. No text, no captions, no readable signs, no watermark, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same corridor. She talks into the phone and mimes pulling up her own sleeve on her upper arm to show what her colleague did, taps the spot twice with two fingers, then raises her eyebrows on the last sentence. Blinks, natural head movement, real speech mouth shapes. Handheld drift.
DIALOGUE (Bulgarian, spoken exactly as written): „Тя си вдигна ръкава и видях една розова лепенка. Каза ми, че точно това ѝ е помогнало да свали килограмите."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, conversational, a bit surprised — retelling something she did not expect.
AUDIO: only her voice plus faint corridor ambience. No music.
CAMERA: handheld selfie, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no watermark, no music, no other person on screen, no scene change, no beauty filter.
```

---

## СЦЕНА 15 — 10 секунди

**Ситуация:** в банята пред огледалото, лепи пластира на рамото си
**Реплика:** „Така попаднах на тези малки пластирчета с берберин, който се усвоява през кожата. Лепиш го сутрин и си продължаваш деня."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo taken in a bathroom mirror. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, overweight (EU size 46), shoulder-length dyed light-brown hair with grey roots, damp and pushed back, small hazel-brown eyes, crow's feet, visible pores, small mole above the right corner of her mouth, no makeup. She wears a sleeveless white top so her bare upper arm is visible. She is standing in front of an ordinary bathroom mirror, filming her reflection with the phone in one hand, her other hand pressing a small round pale-pink adhesive patch onto her upper arm. Background: bathroom tiles, a sink with a toothbrush cup, a small plain white-and-pink cardboard box with no readable text on the shelf. Bright unflattering bathroom light. Shot on an iPhone 12, 1080p, slightly soft, digital noise, flat unedited colours, mirror glare, no colour grading, no bokeh, no professional lighting. Looks like a real woman filming herself, not an ad. No text, no captions, no readable writing on the box, no brand logo, no watermark, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same bathroom mirror. She presses the small pale-pink patch flat onto her upper arm, smooths it with two fingers, then looks up into the mirror and keeps talking to her own reflection. Blinks, natural head movement, real speech mouth shapes. Handheld phone, slight shake and mirror reflection.
DIALOGUE (Bulgarian, spoken exactly as written): „Така попаднах на тези малки пластирчета с берберин, който се усвоява през кожата. Лепиш го сутрин и си продължаваш деня."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, simple and matter-of-fact, like explaining a small everyday habit.
AUDIO: only her voice plus faint bathroom room tone. No music.
CAMERA: handheld mirror selfie, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no readable packaging text, no watermark, no music, no scene change, no beauty filter.
```

> **Монтаж:** тук сложи 1–2 сек close-up на реалния FitPatches пластир/кутия (твой packshot), после се връщаш на нея.

---

## СЦЕНА 16 — 8 секунди

**Ситуация:** на дивана, държи кутията в ръка
**Реплика:** „Първата ми мисъл беше „поредната глупост". Но реших да пробвам един месец. Първите три дни — нищо."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, overweight (EU size 46), shoulder-length dyed light-brown hair with grey roots, small hazel-brown eyes, crow's feet, visible pores, small mole above the right corner of her mouth, no makeup. She wears a soft oversized dark-green sweatshirt. She is sitting on the beige fabric sofa in her living-room, holding a small plain white-and-pink cardboard box with no readable text in one hand, the phone at arm's length in the other, looking into the lens, talking. Background: living-room wall, a lamp, a cushion, warm ordinary indoor light. Shot on an iPhone 12, 1080p, slightly soft, digital noise, flat unedited colours, no colour grading, no bokeh, no professional lighting. Looks like a real woman filming herself at home, not an ad. No text, no captions, no readable writing on the box, no brand logo, no watermark, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same sofa. She talks into the phone, gives a sceptical shrug and a small laugh on the first sentence, turns the little box once in her hand, then a flat honest face on the last sentence. Blinks, natural head movement, real speech mouth shapes. Handheld drift.
DIALOGUE (Bulgarian, spoken exactly as written): „Първата ми мисъл беше поредната глупост. Но реших да пробвам един месец. Първите три дни — нищо."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, sceptical and self-ironic at first, then plain and honest — she is not overselling.
AUDIO: only her voice plus quiet room tone. No music.
CAMERA: handheld selfie, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no readable packaging text, no watermark, no music, no scene change, no beauty filter.
```

---

## СЦЕНА 17 — 10 секунди

**Ситуация:** в кухнята, застанала пред отворен шкаф със сладки неща
**Реплика:** „Към седмия ден забелязах нещо странно. Минах покрай шкафа с бисквити и шоколад, които обожавам. Или по-скоро обожавах."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, overweight (EU size 46), shoulder-length dyed light-brown hair with grey roots, small hazel-brown eyes, crow's feet, visible pores, small mole above the right corner of her mouth, no makeup. She wears a plain white t-shirt. She is standing in her kitchen in front of an open cupboard filled with biscuits, wafers and chocolate bars in plain unbranded wrappers, her body turned half towards the cupboard, holding the phone at arm's length, looking into the lens, talking. Background: kitchen cupboards, tiled wall, a kettle, daylight from a window. Shot on an iPhone 12, 1080p, slightly soft, digital noise, flat unedited colours, yellowish indoor white balance, no colour grading, no bokeh, no professional lighting. Looks like a real woman filming herself, not an ad. No text, no captions, no readable writing on the wrappers, no brand logos, no watermark, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same kitchen. She talks into the phone, gestures with an open palm towards the sweets in the open cupboard, then corrects herself with a small amused smile on the last three words. Blinks, natural head movement, real speech mouth shapes. Handheld drift.
DIALOGUE (Bulgarian, spoken exactly as written): „Към седмия ден забелязах нещо странно. Минах покрай шкафа с бисквити и шоколад, които обожавам. Или по-скоро обожавах."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, curious and slightly surprised, with a small laugh on the correction at the end.
AUDIO: only her voice plus quiet kitchen room tone. No music.
CAMERA: handheld selfie, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no readable packaging, no watermark, no music, no scene change, no beauty filter.
```

---

## СЦЕНА 18 — 8 секунди

**Ситуация:** същата кухня, затваря шкафа и си налива чаша вода
**Реплика:** „И изненадващо не ми се доядоха. Не се борих — просто не ми се дояде."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, overweight (EU size 46), shoulder-length dyed light-brown hair with grey roots, small hazel-brown eyes, crow's feet, visible pores, small mole above the right corner of her mouth, no makeup. Same plain white t-shirt. She is standing by the kitchen counter with the cupboard now closed behind her, a glass of water in one hand, the phone at arm's length in the other, looking into the lens, talking. Background: closed kitchen cupboards, the sink, a tea towel, daylight from a window. Shot on an iPhone 12, 1080p, slightly soft, digital noise, flat unedited colours, no colour grading, no bokeh, no professional lighting. Looks like a real woman filming herself, not an ad. No text, no captions, no watermark, no logo, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same kitchen. She talks into the phone, gives a small "I don't know" shrug, takes a sip of water at the end and shrugs again. Blinks, natural head movement, real speech mouth shapes. Handheld drift.
DIALOGUE (Bulgarian, spoken exactly as written): „И изненадващо не ми се доядоха. Не се борих — просто не ми се дояде."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, calm and almost puzzled by her own words, understated.
AUDIO: only her voice plus quiet kitchen room tone. No music.
CAMERA: handheld selfie, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no watermark, no music, no scene change, no beauty filter.
```

---

## СЦЕНА 19 — 8 секунди

**Ситуация:** в спалнята пред огледалото на гардероба, с дънките
**Реплика:** „След месец готините ми дънки, които не бях обличала две години, се закопчаха."

```
КАДЪР — gptimage2
Vertical 9:16 amateur mirror selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, still overweight but slightly slimmer (EU size 44), shoulder-length dyed light-brown hair with grey roots, small hazel-brown eyes, crow's feet, visible pores, small mole above the right corner of her mouth, light everyday makeup. She wears blue jeans and a simple black top, standing in front of a wardrobe mirror in her bedroom, filming her reflection with the phone in one hand while her other hand touches the waistband of the jeans, half-smiling, talking to the mirror. Background: bedroom, open wardrobe door, a bed with a folded blanket, daylight from a window. Shot on an iPhone 12, 1080p, slightly soft, digital noise, flat unedited colours, mirror glare, no colour grading, no bokeh, no professional lighting. Looks like a real woman filming herself, not an ad. No text, no captions, no watermark, no logo, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same bedroom mirror. She tugs lightly at the waistband of the jeans to show they fasten, turns slightly sideways once, then looks up into the mirror and smiles while talking. Blinks, natural head movement, real speech mouth shapes. Handheld phone, slight shake.
DIALOGUE (Bulgarian, spoken exactly as written): „След месец готините ми дънки, които не бях обличала две години, се закопчаха."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, quietly happy, a bit proud but not shouting.
AUDIO: only her voice plus quiet room tone. No music.
CAMERA: handheld mirror selfie, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no watermark, no music, no scene change, no beauty filter, no dramatic body transformation.
```

---

## СЦЕНА 20 — 10 секунди

**Ситуация:** на плажа, седнала на шезлонг, по бански с парео, морето отзад
**Реплика:** „Най-важната промяна беше, че това лято не ме беше срам да съм по бански и в морето с приятелките ми."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, still a full body (EU size 44), shoulder-length dyed light-brown hair with grey roots, damp and pulled back, small hazel-brown eyes, crow's feet, visible pores, sun-flushed cheeks, small mole above the right corner of her mouth, no makeup. She wears a modest dark one-piece swimsuit with a light sarong loosely over her hips, sitting on a beach sun lounger, holding the phone at arm's length, looking into the lens, talking, relaxed. Background: sandy Black Sea beach, a beach umbrella, the sea and a few blurred people far away, very bright midday sun. Shot on an iPhone 12 front camera, 1080p, slightly soft, harsh contrast, blown-out bright sand and sky, flat unedited colours, no colour grading, no bokeh, no professional lighting. Looks like a real woman filming herself on holiday, not an ad. No text, no captions, no watermark, no logo, not a model, no beauty retouch, no glamour posing.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same swimsuit, same beach. She talks into the phone, squints slightly against the sun, pushes a damp strand of hair back, smiles genuinely at the end. Blinks, natural head movement, real speech mouth shapes. Handheld drift, the sea and umbrella move faintly in the wind.
DIALOGUE (Bulgarian, spoken exactly as written): „Най-важната промяна беше, че това лято не ме беше срам да съм по бански и в морето с приятелките ми."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, light and free, with real relief in it — this is the emotional payoff.
AUDIO: only her voice plus faint beach ambience, waves and wind on the microphone. No music.
CAMERA: handheld selfie, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no watermark, no music, no slow motion, no scene change, no beauty filter, no sexualised framing.
```

---

## СЦЕНА 21 — 8 секунди

**Ситуация:** на плажа, права до водата, мокра коса
**Реплика:** „Със сигурност не бих искала да се връщам към старото си аз."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, full body (EU size 44), wet shoulder-length dyed light-brown hair slicked back, small hazel-brown eyes, crow's feet, visible pores, water droplets on her skin and shoulders, small mole above the right corner of her mouth, no makeup. She wears the same modest dark one-piece swimsuit, standing ankle-deep at the water's edge, holding the phone at arm's length slightly above her, looking into the lens, talking, breathing a little heavily after swimming. Background: sea, shallow waves, wet sand, bright afternoon sun, a few distant blurred people. Shot on an iPhone 12, 1080p, slightly soft, harsh sunlight, blown-out highlights on the water, flat unedited colours, no colour grading, no bokeh, no professional lighting. Looks like a real woman filming herself, not an ad. No text, no captions, no watermark, no logo, not a model, no beauty retouch, no glamour posing.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same swimsuit, same shoreline. She talks into the phone slightly out of breath, wipes water from her forehead with the back of her hand, shakes her head once firmly on the word "не". Blinks, natural head movement, real speech mouth shapes. Handheld drift, small waves move around her feet, wind noise on the microphone.
DIALOGUE (Bulgarian, spoken exactly as written): „Със сигурност не бих искала да се връщам към старото си аз."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, firm and certain, slightly breathless.
AUDIO: only her voice plus waves and wind. No music.
CAMERA: handheld selfie, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no watermark, no music, no slow motion, no scene change, no beauty filter, no sexualised framing.
```

---

## СЦЕНА 22 — 8 секунди

**Ситуация:** на маса в плажен бар, приятелките ѝ размазани отзад
**Реплика:** „Да ме е срам от тялото ми и да не мога да се социализирам с приятелите си."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, full body (EU size 44), shoulder-length dyed light-brown hair with grey roots, drying after a swim, small hazel-brown eyes, crow's feet, visible pores, sun-flushed cheeks, small mole above the right corner of her mouth, no makeup. She wears a light open beach shirt over her swimsuit, sitting at a wooden table in a beach bar, a glass of lemonade in front of her, holding the phone at arm's length, looking into the lens, talking. Background: beach bar under a straw roof, two or three women of similar age sitting further away out of focus, the sea in the distance, bright daylight in the shade. Shot on an iPhone 12, 1080p, slightly soft, digital noise, flat unedited colours, no colour grading, no bokeh, no professional lighting. Looks like a real woman filming herself, not an ad. No text, no captions, no readable signs, no watermark, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same beach bar. She talks into the phone, glances briefly over her shoulder towards her friends in the background, then back to the lens with a small warm smile. Blinks, natural head movement, real speech mouth shapes. Handheld drift, the blurred women in the background move naturally but do not speak.
DIALOGUE (Bulgarian, spoken exactly as written): „Да ме е срам от тялото ми и да не мога да се социализирам с приятелите си."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, honest and grounded, finishing the previous thought.
AUDIO: only her voice plus faint beach bar ambience. No music.
CAMERA: handheld selfie, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no watermark, no music, no other person speaking, no scene change, no beauty filter.
```

---

## СЦЕНА 23 — 8 секунди

**Ситуация:** вкъщи на терасата/двора, кутията на масата пред нея
**Реплика:** „Честно казано, не мисля да спирам да ползвам тези ФитПачис лепенки."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, full body (EU size 44), shoulder-length dyed light-brown hair with grey roots, small hazel-brown eyes, crow's feet, visible pores, small mole above the right corner of her mouth, light everyday makeup. She wears a coral-coloured summer blouse. She is sitting at a small table on a home terrace or in a small garden, a small plain white-and-pink cardboard box with no readable text on the table in front of her, one hand resting next to it, holding the phone at arm's length, looking into the lens, talking. Background: terrace railing, potted plants, a neighbouring building, warm late-afternoon daylight. Shot on an iPhone 12, 1080p, slightly soft, digital noise, flat unedited colours, no colour grading, no bokeh, no professional lighting. Looks like a real woman filming herself, not an ad. No text, no captions, no readable writing on the box, no brand logo, no watermark, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same terrace. She talks into the phone and taps the small box on the table twice with one finger, small confident smile. Blinks, natural head movement, real speech mouth shapes. Handheld drift, leaves move faintly in the breeze.
DIALOGUE (Bulgarian, spoken exactly as written): „Честно казано, не мисля да спирам да ползвам тези ФитПачис лепенки."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, casual and certain, like stating an obvious fact.
AUDIO: only her voice plus faint outdoor ambience. No music.
CAMERA: handheld selfie, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no readable packaging text, no watermark, no music, no scene change, no beauty filter.
```

---

## СЦЕНА 24 — 8 секунди

**Ситуация:** пред входа на блока, с получен колет в ръка
**Реплика:** „Проблемът е, че предния път едвам успях да си взема, защото хората ги бяха изкупили."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, full body (EU size 44), shoulder-length dyed light-brown hair with grey roots, small hazel-brown eyes, crow's feet, visible pores, small mole above the right corner of her mouth, light everyday makeup. She wears the coral summer blouse and a light jacket over it. She is standing in front of the entrance of a Bulgarian apartment block, holding a small plain brown cardboard parcel with no readable text under one arm, the phone at arm's length in the other hand, looking into the lens, talking. Background: entrance door, mailboxes, a strip of grass, parked cars, flat daylight. Shot on an iPhone 12, 1080p, slightly soft, digital noise, flat unedited colours, no colour grading, no bokeh, no professional lighting, slightly crooked framing. Looks like a real woman filming herself, not an ad. No text, no captions, no readable writing on the parcel, no watermark, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same entrance. She talks into the phone, lifts the small parcel slightly towards the camera once, raises her eyebrows on "изкупили". Blinks, natural head movement, real speech mouth shapes. Handheld drift.
DIALOGUE (Bulgarian, spoken exactly as written): „Проблемът е, че предния път едвам успях да си взема, защото хората ги бяха изкупили."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, slightly hurried and a bit annoyed, like a genuine complaint — not a sales line.
AUDIO: only her voice plus faint outdoor street ambience. No music.
CAMERA: handheld selfie, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no readable packaging text, no watermark, no music, no scene change, no beauty filter.
```

---

## СЦЕНА 25 — 10 секунди

**Ситуация:** вкъщи в креслото, кутията в ръка, по-близък кадър
**Реплика:** „Аз даже не се замислих, като ги взимах първия път. Защото имат шейсет дневен тест период и ако нямат ефект, ти връщат парите."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo, closer framing — head and shoulders. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, shoulder-length dyed light-brown hair with grey roots, small hazel-brown eyes, crow's feet, visible pores, small mole above the right corner of her mouth, light everyday makeup. She wears a simple cream top. She is sitting in the armchair at home, holding a small plain white-and-pink cardboard box with no readable text up near her shoulder so it is visible next to her face, holding the phone closer than usual, looking straight into the lens, talking. Background: living-room wall, a plant, warm indoor daylight from a window. Shot on an iPhone 12, 1080p, slightly soft, digital noise, flat unedited colours, no colour grading, no bokeh, no professional lighting. Looks like a real woman filming herself, not an ad. No text, no captions, no readable writing on the box, no brand logo, no watermark, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same armchair. She talks into the phone and holds the small box a little higher next to her face, gives a small "so what do you risk" shrug at the end. Blinks, natural head movement, real speech mouth shapes. Handheld drift.
DIALOGUE (Bulgarian, spoken exactly as written): „Аз даже не се замислих, като ги взимах първия път. Защото имат шейсет дневен тест период и ако нямат ефект, ти връщат парите."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, relaxed and reassuring, slightly faster — like removing the last doubt.
AUDIO: only her voice plus quiet room tone. No music.
CAMERA: handheld selfie, closer framing, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no readable packaging text, no watermark, no music, no scene change, no beauty filter.
```

---

## СЦЕНА 26 — 8 секунди

**Ситуация:** на дивана, сочи надолу към долния край на екрана (CTA)
**Реплика:** „Ще оставя линка отдолу, така че може да ги погледнете."

```
КАДЪР — gptimage2
Vertical 9:16 amateur selfie photo. The same 45-year-old Bulgarian woman: ordinary plain looks, not a model, full round face, soft double chin, shoulder-length dyed light-brown hair with grey roots, small hazel-brown eyes, crow's feet, visible pores, small mole above the right corner of her mouth, light everyday makeup. Same simple cream top. She is sitting on the beige sofa in her living-room, leaning slightly towards the camera, one index finger pointing downwards towards the bottom of the frame, holding the phone at arm's length, looking straight into the lens, smiling warmly, talking. Background: living-room wall, a lamp, a cushion, warm indoor daylight. Shot on an iPhone 12, 1080p, slightly soft, digital noise, flat unedited colours, no colour grading, no bokeh, no professional lighting. Looks like a real woman filming herself, not an ad. No text, no captions, no watermark, no logo, not a model, no beauty retouch.
```

```
ВИДЕО — omniflash
Animate this exact frame. Same woman, same face, same clothes, same sofa. She talks into the phone and points down towards the bottom of the frame two or three times, then gives a small friendly nod and a warm closing smile, holding the smile for a beat after she stops talking. Blinks, natural head movement, real speech mouth shapes. Handheld drift.
DIALOGUE (Bulgarian, spoken exactly as written): „Ще оставя линка отдолу, така че може да ги погледнете."
VOICE: same real 45-year-old Bulgarian woman, warm slightly hoarse, friendly and casual, absolutely not salesy.
AUDIO: only her voice plus quiet room tone. No music.
CAMERA: handheld selfie, one continuous take, no cuts.
NEGATIVE: no subtitles, no captions, no on-screen text, no watermark, no music, no scene change, no beauty filter.
```

---
---

## МОНТАЖ — накратко

- Ред: 01 → 26. Реже се веднага след последната сричка на всяка сцена (0 паузи между клиповете = задържа гледането).
- Първите 3 секунди решават всичко: ако Сцена 01 не дърпа, тествай алтернативните хукове по-долу като нова Сцена 01 (същият промпт, само репликата се сменя).
- Субтитри: **добавят се в монтажа**, не в промпта. Едри бели букви с черен кант, максимум 3–4 думи на ред, долна трета.
- Продуктови вложки (по 1–1.5 сек, от твоите реални снимки): след Сцена 15, след Сцена 16, върху Сцена 23 и Сцена 25.
- Звук: без музика през първите ~30 сек. После тиха фонова музика на 8–10% под гласа.
- Край: last frame с логото, цената/офертата и „60 дни гаранция" — статичен кадър 2 сек.

## АЛТЕРНАТИВНИ ХУКОВЕ ЗА ТЕСТ (само сменяш репликата в Сцена 01)

1. „Миналото лято за първи път не си свалих ризата на плажа. И не защото ми беше студено."
2. „На четиридесет и пет години седях облечена на плажа в тридесет и три градуса. Ще ви кажа защо."
3. „Проблемът ми никога не е бил волята. Разбрах го чак миналата година."
4. „Приятелките ми бяха в морето, а аз се правех, че чета книга под чадъра."
