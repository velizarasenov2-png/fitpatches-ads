# -*- coding: utf-8 -*-
# Shot list for the FitPatches VSL "Кантарът не казва всичко".
# Mostly stock footage, AI only where stock can't deliver (like the EternaDrop reference).
# type: СТОК, AI, AI3D, ТЕКСТ, ГРАФИКА, ПРОДУКТ, UGC
# style (AI only): photo | d3 | macro | product | hero | custom
# sub: on-screen subtitle, *word* = gold key word

BLOCKS = [
    ("b1", "Хук", "Призив към нея, шокиращ факт, обещание"),
    ("b2", "Кантарът не казва всичко", "Нов механизъм на проблема (SWAN) и метафората с пуха"),
    ("b3", "Как изглежда в живота", "Пералнята, дънките, възглавницата"),
    ("b4", "Всичко пробвано", "Провалени решения, сънят и гладът"),
    ("b5", "Трите неща", "Какво зависи от нея; честно признание"),
    ("b6", "ФитПачес", "Продуктът, как се ползва, съставки, жълтият корен"),
    ("b7", "Какво да очакваш", "Само усещане, без обещания"),
    ("b8", "Доказателство", "Реални продажби и реален UGC"),
    ("b9", "Оферта", "3+2, цена на ден, плащане при получаване"),
    ("b10", "Два пътя", "Избор и призив"),
]

S = []
def add(b, vo, sub, typ, desc, scene="", motion="", q="", img=None, style="photo", dur=None, anim=False):
    S.append(dict(b=b, vo=vo, sub=sub, type=typ, desc=desc, scene=scene, motion=motion,
                  q=q, img=img or [], style=style, dur=dur, anim=anim))

# ---------------- 1. ХУК ----------------
add("b1", "Ако си жена над 40 и кантарът показва почти същото като преди,",
    "АКО СИ ЖЕНА НАД *40*…", "AI",
    "Колаж 2×2 от четири AI кадъра (дънките, пералнята, възглавницата, балконът) + червена лента горе „АКО СИ ЖЕНА НАД 40…“, точно като при EternaDrop.",
    "",
    img=["f01_jeans", "f06_washer", "f12_cushion", "f03_cardigan"], style="custom")
add("b1", "а дънките вече не се закопчават —",
    "ДЪНКИТЕ НЕ СЕ *ЗАКОПЧАВАТ*", "СТОК",
    "Втори колаж 2×2 от стокови кадри: жена в пробна с дънки, жена пред гардероб, селфи отвисоко, жена в широка туника.",
    q="woman fitting room jeans")
add("b1", "спри и гледай това.",
    "*СПРИ*", "ТЕКСТ",
    "Черен екран, огромно червено „СПРИ“ с бял контур. 0,8–1 сек, кратък звук „туп“.")
add("b1", "Защото това, което се случва с тялото ти точно сега,",
    "С ТЯЛОТО ТИ *ТОЧНО СЕГА*", "СТОК",
    "Жена 45–55 г. седи вкъщи и гледа сериозно в камерата.", q="mature woman looking at camera serious")
add("b1", "рядко някой ще ти го обясни.",
    "РЯДКО НЯКОЙ ЩЕ ТИ ГО *ОБЯСНИ*", "СТОК",
    "Жена сама в чакалня.", q="woman waiting room")
add("b1", "Около две години преди менопаузата",
    "*2 ГОДИНИ* ПРЕДИ МЕНОПАУЗАТА", "СТОК",
    "Календар, страниците се обръщат.", q="calendar pages flipping")
add("b1", "тялото започва да трупа мазнини",
    "ТЯЛОТО ТРУПА *МАЗНИНИ*", "AI3D",
    "3D разрез на корема с кехлибарено светеща дълбока мазнина около органите (стилът на 3D кадрите от VSL #2).",
    "Side cross-section of a woman's abdomen showing skin, a thin layer of subcutaneous fat, abdominal muscles and deeper visceral fat wrapped around the intestines, the visceral fat glowing as warm amber.",
    "Slow 10-degree orbit around the cross-section, the amber fat layer gently pulses brighter.",
    img=["f09_3d_fat"], style="d3", anim=True)
add("b1", "два пъти по-бързо.",
    "*2×* ПО-БЪРЗО", "ГРАФИКА",
    "Голямо златно „2×“ на черно, бързо мащабиране от 80% до 100%.")
add("b1", "Два пъти.",
    "*ДВА ПЪТИ.*", "ТЕКСТ",
    "Черен екран, червено „ДВА ПЪТИ“. Пауза в гласа.")
add("b1", "И не чака да си готова.",
    "НЕ ЧАКА ДА СИ *ГОТОВА*", "СТОК",
    "Пясъчен часовник, пясъкът тече.", q="hourglass sand")
add("b1", "Затова ще ти го обясня аз.",
    "ЩЕ ТИ ГО ОБЯСНЯ *АЗ*", "СТОК",
    "Жена 50+ в кухнята с чаша чай поглежда към камерата.", q="mature woman kitchen tea smiling")
add("b1", "В следващите пет минути.",
    "СЛЕДВАЩИТЕ *5 МИНУТИ*", "СТОК",
    "Тиктакащ часовник отблизо.", q="clock ticking")

# ---------------- 2. КАНТАРЪТ НЕ КАЗВА ВСИЧКО ----------------
add("b2", "Голямо американско проучване — SWAN —",
    "ПРОУЧВАНЕТО *SWAN*", "СТОК",
    "Лаборатория, изследователка с микроскоп.", q="scientist microscope laboratory")
add("b2", "мери телата на жените години наред.",
    "ГОДИНИ *НАРЕД*", "СТОК",
    "Медицински скенер / жена при преглед.", q="medical scan patient")
add("b2", "И открива нещо странно.",
    "НЕЩО *СТРАННО*", "СТОК",
    "Изследовател гледа графики на монитор.", q="scientist looking at data monitor")
add("b2", "Точно когато мазнините се ускоряват,",
    "МАЗНИНИТЕ *СЕ УСКОРЯВАТ*", "ГРАФИКА",
    "Проста графика: златна линия „мазнини“ тръгва стръмно нагоре. Без числа по оста.")
add("b2", "мускулите започват да намаляват.",
    "МУСКУЛИТЕ *НАМАЛЯВАТ*", "AI3D",
    "3D анатомичен рендер на мускул на ръката; влакната изтъняват.",
    "Anatomical render of the upper arm muscle of a middle-aged woman, the red muscle fibres slowly becoming thinner and sparser, semi-transparent skin outline around it.",
    "Muscle fibres slowly thin out as the camera drifts along the arm.", style="d3")
add("b2", "Едното се качва. Другото слиза.",
    "ЕДНОТО *↑* ДРУГОТО *↓*", "ГРАФИКА",
    "Същата графика + сива линия „мускули“ слиза. Червена стрелка нагоре, сива надолу.")
add("b2", "И на кантара двете се уравновесяват.",
    "НА КАНТАРА СЕ *УРАВНОВЕСЯВАТ*", "СТОК",
    "Везна с тасове се люлее и застава в равновесие (без човек на кантар).", q="balance scale")
add("b2", "Числото почти не мърда.",
    "ЧИСЛОТО *НЕ МЪРДА*", "AI",
    "Стар пазарен кантар с кръгъл циферблат, стрелката стои неподвижно.",
    "An old round white-faced mechanical market scale with a thin red needle and black numbers on a weathered wooden stall at an open-air Bulgarian farmers market, a brown paper bag of red apples on its tray, the needle holds perfectly still. Crates of peppers and tomatoes blurred behind.",
    "The needle trembles slightly, then stops dead still.", img=["f11_dial"])
add("b2", "Кантарът не лъже. Просто не ти казва всичко.",
    "КАНТАРЪТ НЕ ЛЪЖЕ. *НЕ КАЗВА ВСИЧКО.*", "ТЕКСТ",
    "Черен екран: бяло „КАНТАРЪТ НЕ ЛЪЖЕ.“, после червено „ПРОСТО НЕ КАЗВА ВСИЧКО.“")
add("b2", "Кое е по-тежко — килограм пух или килограм пирони?",
    "ПУХ ИЛИ *ПИРОНИ*?", "AI",
    "Месингова везна на пазара: огромна купчина пух срещу малка купчина пирони, в равновесие. Главният „уау“ кадър.",
    "An old-fashioned brass market balance scale with two hanging pans on a weathered wooden stall at an open-air Bulgarian farmers market. The left pan holds a huge fluffy overflowing mountain of white feathers, the right pan holds a small neat pile of dark iron nails. The beam is perfectly level. Crates of vegetables blurred behind.",
    "A few feathers lift in a light breeze, slow push-in toward the level beam.", img=["f05_feathers"], anim=True)
add("b2", "Еднакво.",
    "*ЕДНАКВО.*", "СТОК",
    "Близък план на везна в равновесие.", q="scale balance close up")
add("b2", "Но пухът заема много повече място.",
    "ПУХЪТ ЗАЕМА *ПОВЕЧЕ МЯСТО*", "AI",
    "Пухът прелива от таса и пада върху сергията.",
    "Close-up of a brass scale pan overflowing with white feathers, feathers spilling over the edge onto a wooden market stall, morning sun backlighting them.",
    "Feathers slowly tumble over the rim and drift down.", style="macro", anim=True)
add("b2", "Същото е с тялото. Същите килограми — друго разпределение.",
    "СЪЩИТЕ КИЛОГРАМИ — *ДРУГО РАЗПРЕДЕЛЕНИЕ*", "СТОК",
    "Жена пред огледалото оглежда дрехата си, замислена (без близък план на тялото).", q="woman mirror trying clothes")
add("b2", "И отиват на едно място.",
    "НА *ЕДНО МЯСТО*", "AI3D",
    "3D: полупрозрачна женска фигура в профил, около корема бавно се появява кехлибарено сияние.",
    "Translucent glass-like female figure in side profile, standing calmly, a soft warm amber glow slowly appears deep inside the abdomen around the organs.",
    "The amber glow fades in around the abdomen.", style="d3")
add("b2", "Преди менопаузата дълбоката мазнина в корема е 5 до 8 процента от цялата мазнина в тялото.",
    "ПРЕДИ: *5–8%*", "AI3D",
    "Същият 3D разрез, но кехлибарената зона е малка. Отгоре „5–8%“ в монтажа.",
    "Side cross-section of a woman's abdomen with only a small, thin amount of visceral fat around the intestines highlighted as soft amber, mostly organs and muscle visible.",
    "Slow orbit, the small amber zone glows softly.", img=["f09_3d_fat"], style="d3")
add("b2", "След нея — 15 до 20.",
    "СЛЕД: *15–20%*", "ГРАФИКА",
    "Голямо червено „15–20%“ с брояч от 5 до 20.")
add("b2", "Почти три пъти повече.",
    "ПОЧТИ *3 ПЪТИ* ПОВЕЧЕ", "AI3D",
    "3D разрезът: кехлибарената зона се разширява и обгръща органите.",
    "Side cross-section of a woman's abdomen where the amber visceral fat has grown thick and wraps around the intestines and organs, glowing warmly.",
    "The amber layer slowly expands and thickens around the organs.", img=["f09_3d_fat"], style="d3", anim=True)
add("b2", "Затова коремът. Затова дънките.",
    "ЗАТОВА *ДЪНКИТЕ*", "AI",
    "Жената пред гардероба се опитва да закопчае дънките. Среден план, не близък.",
    "A 47-year-old Eastern European woman with shoulder-length dark blonde hair, average build with a soft midsection, stands in a small bedroom on a weekday morning trying to button her blue jeans. She holds her breath and pulls the waistband together, the button stops short of the hole, quiet frustration. Open wardrobe behind her with mostly black and dark clothes. Medium shot.",
    "She sucks in her stomach, tugs the waistband, gives up and exhales.", img=["f01_jeans"])

# ---------------- 3. КАК ИЗГЛЕЖДА В ЖИВОТА ----------------
add("b3", "Първата година обвиняваш пералнята.",
    "ОБВИНЯВАШ *ПЕРАЛНЯТА*", "AI",
    "Жена коленичи пред пералнята, вдига дънките и подозрително ги оглежда. Самоирония. Тя е героинята и в края.",
    "A 46-year-old woman with curly dark hair kneels in front of a front-loading washing machine in a small Bulgarian bathroom, holding a pair of blue jeans up to the light and inspecting the waistband with a suspicious, slightly comic squint, as if accusing the washing machine of shrinking them. Plastic laundry basket beside her.",
    "She lowers the jeans and gives the washing machine a slow accusing side-eye.", img=["f06_washer"], anim=True)
add("b3", "Свила ги е.",
    "*СВИЛА* ГИ Е", "СТОК",
    "Ръка върти копчето на пералня.", q="washing machine dial")
add("b3", "Втората — дънките. Сега ги шият по-тесни.",
    "СЕГА ГИ ШИЯТ *ПО-ТЕСНИ*", "СТОК",
    "Жена в магазин държи дънки пред себе си и ги гледа скептично.", q="woman shopping jeans store")
add("b3", "Третата — себе си.",
    "ТРЕТАТА — *СЕБЕ СИ*", "СТОК",
    "Жена седи тъжна в банята / на ръба на леглото. Музиката утихва.", q="sad woman sitting alone bedroom")
add("b3", "Когато дойдат гости, сядаш с възглавница в скута.",
    "ВЪЗГЛАВНИЦА *В СКУТА*", "AI",
    "Хол с гости; жената на фотьойла прегръща възглавница в скута. Пробният кадър е с по-млада жена: генерирай пак с жена около 50.",
    "A cosy Bulgarian living room in the evening, friends around a low coffee table with salads and glasses of wine laughing, a 50-year-old woman with short brown hair sits in an armchair hugging a large embroidered decorative cushion on her lap in front of her stomach while smiling politely, warm lamp light.",
    "Friends laugh, she pulls the cushion a little closer.", img=["f12_cushion"])
add("b3", "А на снимките — само от кръста нагоре.",
    "САМО *ОТ КРЪСТА НАГОРЕ*", "СТОК",
    "Жена си прави селфи отвисоко.", q="woman taking selfie")

# ---------------- 4. ВСИЧКО ПРОБВАНО ----------------
add("b4", "И разбира се, пробваш.",
    "И РАЗБИРА СЕ, *ПРОБВАШ*", "СТОК",
    "Жена налива билков чай.", q="pouring tea")
add("b4", "Чай за отслабване.",
    "*ЧАЙ*", "СТОК",
    "Пакетчета чай отблизо.", q="tea bag")
add("b4", "Хапчета.",
    "*ХАПЧЕТА*", "СТОК",
    "Хапчета се изсипват в шепа.", q="pills hand")
add("b4", "Диета от понеделник.",
    "ДИЕТА *ОТ ПОНЕДЕЛНИК*", "AI",
    "Жълто листче на хладилника: „ОТ ПОНЕДЕЛНИК!“ (провери правописа).",
    "Close-up of a white fridge door with a yellow sticky note held by a magnet, handwritten in Bulgarian with a black marker: 'ОТ ПОНЕДЕЛНИК!', a child's drawing and a calendar magnet beside it, kitchen light.",
    "The sticky note flutters as the fridge door closes.", style="macro")
add("b4", "Карта за фитнес, ползвана три пъти.",
    "ФИТНЕС — *3 ПЪТИ*", "СТОК",
    "Празна фитнес зала / маратонки в ъгъла.", q="empty gym")
add("b4", "Събери ги наум. Сметката не е малка.",
    "СМЕТКАТА *НЕ Е МАЛКА*", "AI",
    "Дълга касова бележка с всички опити (както бележката от аптеката при тях).",
    "Two hands of a middle-aged woman hold a very long curling thermal paper receipt in a kitchen. The receipt is printed in Bulgarian Cyrillic, monospace font, clearly readable lines: 'СМЕТКА', 'ЧАЙ ЗА ОТСЛАБВАНЕ  8,90', 'ХАПЧЕТА ЗЕЛЕН ЧАЙ  19,90', 'ПРОТЕИНОВ ШЕЙК  24,50', 'СОКОВА ДИЕТА 7 ДНИ  29,00', 'КАРТА ФИТНЕС 1 М.  45,00', 'ХАПЧЕТА ЗА АПЕТИТ  22,90', 'ДИЕТИЧНИ БАРЧЕТА  12,40', 'ОБЩО  162,60 EUR'.",
    "The receipt slowly unrolls further down out of frame.", img=["f10b_receipt"], style="macro")
add("b4", "Някои от тези неща не са лоши.",
    "НЕ СА *ЛОШИ*", "СТОК",
    "Жена прави йога вкъщи.", q="woman yoga home")
add("b4", "Но почти всички искат от теб едно и също.",
    "ИСКАТ *ЕДНО И СЪЩО*", "СТОК",
    "Отегчена жена над чиния салата.", q="bored woman eating salad")
add("b4", "Воля.",
    "*ВОЛЯ.*", "ТЕКСТ",
    "Черен екран, червено „ВОЛЯ“.")
add("b4", "Три пъти на ден. Всеки ден.",
    "*3 ПЪТИ* НА ДЕН. ВСЕКИ ДЕН.", "СТОК",
    "Ръка зачертава дни в календар.", q="marking calendar")
add("b4", "А точно в тези години волята е най-уморена.",
    "ВОЛЯТА Е *НАЙ-УМОРЕНА*", "СТОК",
    "Уморена жена се прибира вечер.", q="tired woman coming home")
add("b4", "Сънят се разбива.",
    "СЪНЯТ *СЕ РАЗБИВА*", "СТОК",
    "Жена лежи будна нощем.", q="woman cant sleep night")
add("b4", "Горещи вълни.",
    "*ГОРЕЩИ ВЪЛНИ*", "СТОК",
    "Жена се вее нощем, топло ѝ е.", q="woman hot fanning herself")
add("b4", "Будене в три сутринта.",
    "*3:00*", "СТОК",
    "Часовник показва 3:00 в тъмното.", q="alarm clock night")
add("b4", "И ето нещо, за което почти никой не говори.",
    "ЗА КОЕТО *НИКОЙ НЕ ГОВОРИ*", "СТОК",
    "Жена се навежда към камерата, доверително.", q="woman talking to camera")
add("b4", "В лабораторни опити само две нощи по четири часа сън",
    "2 НОЩИ ПО *4 ЧАСА* СЪН", "СТОК",
    "Лаборатория за сън, електроди.", q="sleep study")
add("b4", "увеличават глада с около една четвърт.",
    "ГЛАДЪТ *+¼*", "СТОК",
    "Следобед, жена посяга към бисквити в кухнята.", q="woman eating cookies kitchen")
add("b4", "Не е липса на характер.",
    "НЕ Е *ЛИПСА НА ХАРАКТЕР*", "СТОК",
    "Жена гледа през прозореца вечер.", q="woman looking out window evening")
add("b4", "Тялото ти просто е сменило правилата.",
    "СМЕНИЛО *ПРАВИЛАТА*", "AI",
    "Позната улица с нов знак „еднопосочна“; жена с пазарски чанти спира объркана.",
    "A familiar quiet Bulgarian residential street, a brand-new 'one way' road sign has appeared on a pole, a 50-year-old woman carrying grocery bags stops and looks up at it, puzzled, late afternoon light.",
    "She stops walking and looks up at the sign.")
add("b4", "А никой не ти е дал новите.",
    "НИКОЙ НЕ ТИ Е ДАЛ *НОВИТЕ*", "AI",
    "Ръце прелистват книжка с инструкции — всички страници са празни.",
    "Close-up of a woman's hands opening an instruction booklet on a kitchen table and flipping through it, every page is completely blank, soft daylight.",
    "Pages flip, all blank.", style="macro")

# ---------------- 5. ТРИТЕ НЕЩА ----------------
add("b5", "Хормоните не можеш да ги спреш.",
    "ХОРМОНИТЕ *НЕ МОЖЕШ ДА ГИ СПРЕШ*", "AI3D",
    "Абстрактни молекули се носят в кръвоносен съд, топли тонове.",
    "Abstract visualisation of small rounded hormone molecules drifting through a translucent blood vessel, gentle pink, coral and amber tones, calm and elegant.",
    "Molecules drift slowly past the camera.", style="d3")
add("b5", "Но три неща зависят от теб.",
    "*3 НЕЩА* ЗАВИСЯТ ОТ ТЕБ", "ТЕКСТ",
    "Черна дъска с бял тебешир: „1. … 2. … 3. …“ (като списъка с трите неща при тях).")
add("b5", "Първо — сънят.",
    "1. *СЪН*", "СТОК",
    "Жена спи спокойно, сутрин.", q="woman sleeping peacefully morning")
add("b5", "Второ — движението.",
    "2. *ДВИЖЕНИЕ*", "СТОК",
    "Жени 50+ вървят бързо в парка.", q="senior women walking park")
add("b5", "За да пазиш мускулите, които си отиват.",
    "ПАЗИШ *МУСКУЛИТЕ*", "СТОК",
    "Жена вдига леки дъмбели вкъщи.", q="woman dumbbells home")
add("b5", "И трето — апетитът.",
    "3. *АПЕТИТЪТ*", "СТОК",
    "Жена в офиса поглежда сладкиши на бюрото.", q="office snacks desk woman")
add("b5", "Първите две ги знаеш.",
    "ПЪРВИТЕ ДВЕ *ГИ ЗНАЕШ*", "ТЕКСТ",
    "Списъкът: отметки ✓ на 1 и 2, точка 3 светва в златно.")
add("b5", "Третото е най-трудното, защото там се бориш сама. По три пъти на ден.",
    "ТРЕТОТО Е *НАЙ-ТРУДНОТО*", "СТОК",
    "Семейна вечеря, хлебна кошничка в центъра.", q="family dinner table")
add("b5", "И точно за третото е направена една малка розова лепенка.",
    "ЕДНА МАЛКА *РОЗОВА ЛЕПЕНКА*", "ПРОДУКТ",
    "Реално видео от телефон: лепенката на върха на пръста, сутрешна светлина. Тук музиката се разведрява.")

# ---------------- 6. ФИТПАЧЕС ----------------
add("b6", "Казва се ФитПачес.",
    "*FITPATCHES*", "ПРОДУКТ",
    "Пликът (снимката от магазина без бял фон), бавно приближаване.")
add("b6", "Кръгла, колкото монета.",
    "КОЛКОТО *МОНЕТА*", "ПРОДУКТ",
    "Реално видео: лепенката до монета от 1 евро върху бял плот.")
add("b6", "Сутрин я залепваш на ръката,",
    "СУТРИН *НА РЪКАТА*", "AI",
    "Жена в кухнята залепва лепенката на горната част на ръката. По-добре е реално видео; AI е резервен вариант.",
    "A 48-year-old Bulgarian woman in a light grey t-shirt stands in her sunlit kitchen on a weekday morning and presses one pink patch onto the outside of her upper arm with two fingers, calm relaxed smile. A cup of coffee and the white pouch lie on the wooden counter.",
    "She smooths the patch with two fingers and smiles.", img=["f08b_patch"], style="product", anim=True)
add("b6", "на чиста и суха кожа,",
    "ЧИСТА И *СУХА КОЖА*", "ПРОДУКТ",
    "Реално видео: отлепване на защитното фолио.")
add("b6", "и я носиш до осем часа.",
    "ДО *8 ЧАСА*", "СТОК",
    "Жена взима ключовете и излиза от вкъщи.", q="woman leaving home keys")
add("b6", "Не я гълташ.",
    "*НЕ Я ГЪЛТАШ*", "СТОК",
    "Хапчета в шепа + червен X в монтажа.", q="pills in hand")
add("b6", "Не я помниш на обяд.",
    "НЕ Я ПОМНИШ *НА ОБЯД*", "СТОК",
    "Жени обядват в кафене и се смеят.", q="women lunch cafe laughing")
add("b6", "Под ръкава никой не я вижда.",
    "*НИКОЙ НЕ Я ВИЖДА*", "СТОК",
    "Жена оправя ръкава на блузата си.", q="woman adjusting blouse sleeve")
add("b6", "Вътре има шест съставки: берберин, канела, нар,",
    "*6 СЪСТАВКИ*", "AI",
    "Флатлей на дървена маса: жълт корен, канела, разрязан нар и пликът.",
    "Top-down flat lay on a rustic wooden table: a piece of barberry root with bright yellow inner wood, a bundle of cinnamon sticks, half a pomegranate with glossy red seeds, and the white FitPatches pouch with its pink circle in the centre, soft natural daylight.",
    "Slow top-down rotation.", style="product")
add("b6", "хром, L-глутамин и витамини от група B.",
    "ХРОМ · L-ГЛУТАМИН · *ВИТАМИНИ B*", "ГРАФИКА",
    "6 иконки със съставките, направени в монтажа. Не ползвай снимката на съставките от магазина: на нея пише за кръвна захар.")
add("b6", "Берберинът е изследван от години.",
    "ИЗСЛЕДВАН *ОТ ГОДИНИ*", "СТОК",
    "Научни списания / пипета в лаборатория.", q="laboratory research pipette")
add("b6", "И ето нещо, което малко хора знаят.",
    "МАЛКО ХОРА *ЗНАЯТ*", "СТОК",
    "Планинска пътека в мъгла, жена се разхожда.", q="woman hiking mountain fog")
add("b6", "Кисел трън. Бодливият храст по нашите баири.",
    "*КИСЕЛ ТРЪН*", "AI",
    "Кисел трън с червени плодчета на скалист родопски склон.",
    "A wild barberry bush (Berberis vulgaris) with hanging clusters of bright red oblong berries and small green leaves grows on a rocky mountain hillside, misty Rhodope ridges behind, golden hour. In the foreground a weathered hand holds a freshly cut piece of barberry root, its inner wood a vivid bright yellow.",
    "Berries sway in the wind, slow push-in toward the yellow root.", img=["f07_barberry"], style="macro", anim=True)
add("b6", "Срежеш ли корена му, вътре е яркожълт.",
    "ВЪТРЕ Е *ЯРКОЖЪЛТ*", "AI",
    "Нож разрязва корена на дъска; срезът е яркожълт. Уау кадър.",
    "A knife slicing through a barberry root on a wooden cutting board, the fresh cross-section revealing intensely bright yellow wood, rustic kitchen, side light.",
    "The knife cuts through and the two halves fall apart, showing the yellow.", style="macro", anim=True)
add("b6", "Това жълто е берберинът.",
    "ТОВА ЖЪЛТО Е *БЕРБЕРИНЪТ*", "AI",
    "Отблизо: жълтият срез в длан (може да е изрязан детайл от кадъра с кисел трън).",
    "Extreme close-up of a cut barberry root cross-section resting in an open palm, the vivid yellow inner wood with fine rings, warm light.",
    "Slow rack focus onto the yellow wood.", style="macro")

# ---------------- 7. КАКВО ДА ОЧАКВАШ ----------------
add("b7", "Какво да очакваш? Не и за седмица.",
    "*НЕ ЗА СЕДМИЦА*", "СТОК",
    "Ръка обръща лист на календар.", q="turning calendar page")
add("b7", "Целта е по-спокоен апетит през деня.",
    "*ПО-СПОКОЕН* АПЕТИТ", "СТОК",
    "Жена в офиса спокойно пие вода.", q="woman drinking water office")
add("b7", "Без война в главата за всяко парче.",
    "БЕЗ *ВОЙНА В ГЛАВАТА*", "СТОК",
    "Семеен обяд, жената се смее.", q="family lunch laughing")
add("b7", "Бавно, но стабилно.",
    "БАВНО, НО *СТАБИЛНО*", "СТОК",
    "Таймлапс на растящо растение.", q="plant growing timelapse")
add("b7", "Седмици, не дни.",
    "*СЕДМИЦИ*, НЕ ДНИ", "ГРАФИКА",
    "Календар с ограждани седмици (не дни) в златно.")

# ---------------- 8. ДОКАЗАТЕЛСТВО ----------------
add("b8", "Над 40 000 продадени лепенки из цяла България.",
    "*40 000+* ЛЕПЕНКИ", "СТОК",
    "Ръце опаковат пратки + брояч „40 000+“ в монтажа. От Shopify: 1 539 пакета ≈ 46 000 лепенки.", q="packing parcels")
add("b8", "",
    "", "UGC",
    "Реалният UGC „Бях скептична до последно…“ (печелившата реклама), 8–12 сек, с нейния глас и надписи.", dur=10)
add("b8", "Усещането е индивидуално. И не трябва да вярваш на никого на думата.",
    "НЕ ВЯРВАЙ *НА ДУМАТА*", "СТОК",
    "Жена на дивана чете на телефона, присвива очи.", q="woman reading phone couch")

# ---------------- 9. ОФЕРТА ----------------
add("b9", "Един пакет е 30 лепенки — за месец.",
    "30 ЛЕПЕНКИ = *1 МЕСЕЦ*", "ПРОДУКТ",
    "Пликът + разпилени лепенки (снимка от магазина).")
add("b9", "Но тялото се променя за години, не за дни. Затова има 3+2.",
    "ЗАТОВА *3+2*", "ПРОДУКТ",
    "5 плика в редица (снимката на 3+2 от магазина или реално видео).")
add("b9", "Пет пакета. Пет месеца. 39,99 евро.",
    "5 ПАКЕТА · *39,99 €*", "ГРАФИКА",
    "Ценова карта: „3+2 = 5 пакета = 39,99 €“.")
add("b9", "Под 27 евроцента на ден.",
    "*< 0,27 €* НА ДЕН", "ГРАФИКА",
    "Голямо „под 0,27 € на ден“.")
add("b9", "Едно кафе струва колкото четири дни лепенки.",
    "1 КАФЕ = *4 ДНИ*", "СТОК",
    "Еспресо на масичка в кафене.", q="espresso cup")
add("b9", "И не плащаш нищо предварително.",
    "*0 €* ПРЕДВАРИТЕЛНО", "ТЕКСТ",
    "Черен екран: „0 € ПРЕДВАРИТЕЛНО“.")
add("b9", "Плащаш на куриера, когато пратката е в ръцете ти.",
    "ПЛАЩАШ *ПРИ ПОЛУЧАВАНЕ*", "СТОК",
    "Куриер подава пратка на жена на вратата.", q="courier delivering package")

# ---------------- 10. ДВА ПЪТЯ ----------------
add("b10", "И сега имаш два пътя.",
    "*ДВА* ПЪТЯ", "ТЕКСТ",
    "Разделен екран „1“ | „2“.")
add("b10", "Първият. Затваряш видеото.",
    "*ПЪРВИЯТ*", "СТОК",
    "Палец затваря приложение на телефона, полутъмно. Път 1 е обезцветен.", q="scrolling phone dark room")
add("b10", "Утре сутрин отваряш гардероба. Посягаш към същите широки дрехи.",
    "СЪЩИТЕ *ШИРОКИ ДРЕХИ*", "AI",
    "Героинята от кадъра с пералнята отваря гардероба: тъмни широки дрехи, студена светлина. Референция: кадърът с пералнята.",
    "The same woman as in the reference image (46, curly dark hair) opens a wardrobe in grey early morning light, rows of dark loose tunics and black cardigans inside, she reaches for a loose black tunic with a flat expression, muted desaturated colours.",
    "Wardrobe doors swing open, her hand reaches in.", style="hero")
add("b10", "Дънките пак не стигат.",
    "ДЪНКИТЕ *ПАК НЕ СТИГАТ*", "СТОК",
    "Дънки, хвърлени на леглото (обезцветено).", q="jeans on bed")
add("b10", "И пак обвиняваш пералнята.",
    "ПАК *ПЕРАЛНЯТА*", "AI",
    "Обратна връзка към началото: героинята пак гледа пералнята. Обезцветено.",
    "The same woman as in the reference image (46, curly dark hair) stands in her small bathroom holding jeans and gives the front-loading washing machine a long tired look, muted desaturated colours.",
    "She stares at the machine and shakes her head.", style="hero")
add("b10", "Или вторият. Натискаш бутона отдолу. Поръчваш.",
    "*ВТОРИЯТ*", "ПРОДУКТ",
    "Запис на екрана: реалната поръчка на fitpatches.net от телефон. Оттук нататък цветовете са топли.")
add("b10", "След няколко дни куриерът звъни.",
    "КУРИЕРЪТ *ЗВЪНИ*", "СТОК",
    "Звънец / куриер пред вратата.", q="doorbell")
add("b10", "Плащаш, чак когато я държиш.",
    "ПЛАЩАШ, ЧАК КОГАТО *Я ДЪРЖИШ*", "AI",
    "Героинята на вратата държи белия плик и се усмихва. Референции: героинята + пликът.",
    "The same woman as in the reference image (46, curly dark hair) stands at her apartment door holding a small courier parcel and the white FitPatches pouch with the pink circle, a curious pleased smile, warm natural light.",
    "She turns the pouch in her hands and smiles.", style="hero", anim=True)
add("b10", "И на следващата сутрин залепваш първата.",
    "ЗАЛЕПВАШ *ПЪРВАТА*", "AI",
    "Ярка сутрин: героинята залепва лепенката пред огледалото в банята.",
    "The same woman as in the reference image (46, curly dark hair) in bright warm morning light in her bathroom presses a round dusty-pink coin-sized patch onto her upper arm in front of the mirror, a small determined smile.",
    "She presses the patch and smooths it with two fingers.", style="hero", anim=True)
add("b10", "Без да гълташ. Без да броиш. Без да се бориш по три пъти на ден.",
    "БЕЗ ДА ГЪЛТАШ · БЕЗ ДА БРОИШ · *БЕЗ БОРБА*", "AI",
    "Героинята излиза от блока на слънчевата улица с цветна блуза, спокойна.",
    "The same woman as in the reference image (46, curly dark hair) walks out of a Bulgarian apartment building entrance into a sunny tree-lined street wearing a colourful blouse and a light jacket, relaxed easy stride, warm golden light.",
    "She steps out into the sun and walks toward the camera.", style="hero", anim=True)
add("b10", "Натисни бутона отдолу.",
    "*НАТИСНИ* ОТДОЛУ ↓", "ПРОДУКТ",
    "Финален кадър: пликът + „3+2 · 39,99 € · Плащаш при получаване“ + стрелка надолу.")
