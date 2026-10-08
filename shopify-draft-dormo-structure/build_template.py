import json, sys
out = sys.argv[1]
fb_posts = [
 ("Гинка Москова",False,"преди 1 час","Купих си 3 опаковки и вече свалих 4 кг за месец! Най-накрая нещо, което ми потиска апетита.","like, haha","14","avatar-ginka-moskova.jpg"),
 ("Гаврил Станков",False,"преди 1 час","Напълно доволен! Лепенките наистина помагат да се чувствам сит.","love","7","avatar-gavrail-stankov.jpg"),
 ("Боряна Атанасова",False,"преди 19 часа","Най-доброто решение за контрол на апетита, което съм опитвала.","love","6","avatar-boryana-atanasova-1.jpg"),
 ("Боряна Атанасова",False,"преди 19 часа","Свалих цели 2 кг благодарение на тези лепенки. Горещо ги препоръчвам!","like","12","avatar-boryana-atanasova-2.jpg"),
 ("Гинка Москова",False,"преди 1 ден","Използвам ги само от седмица, но вече виждам разлика. Определено действат.","like, love","14","avatar-ginka-moskova-2.jpg"),
 ("Мими Попова",False,"преди 1 час","Продуктът е страхотен! Не усещам глад през деня и вече виждам разлика в талията.","love","9","avatar-mimi-popova.jpg"),
 ("Бане Демов",False,"преди 1 час","Откакто ги ползвам, се чувствам отлично, силно ги препоръчвам!","love","7","avatar-bane-demov.jpg"),
 ("Ваня Димова",True,"преди 9 часа","Най-доброто решение за контрол на апетита, което съм опитвала.","love","6","avatar-vanya-dimova.jpg"),
 ("Анелия Радулова",False,"преди 1 ден","Забелязвам, че порциите ми намаляха значително, откакто започнах да ползвам лепенките.","like","10","avatar-anelia-radulova.jpg"),
 ("Мариана Григорова",False,"преди 54 минути","Пробвах ги и съм много доволна! Апетитът ми е овладян!","like","5","avatar-mariana-grigorova.jpg"),
 ("Катя Димитрова",False,"преди 1 ден","След две седмици ползване, имам много повече енергия и по-малко желание за сладко.","like, love","10","avatar-katya-dimitrova.jpg"),
 ("Георги Ахмедов",False,"преди 2 дни","Вече година ги ползвам. Усещам се много по-добре и енергичен през целия ден.","love","8","avatar-georgi-ahmedov.jpg"),
 ("Огнян Ахмедов",False,"преди 22 часа","Вече не мисля за храна на всеки два часа. Чудесен резултат!","like","6","avatar-ognian-ahmedov.jpg"),
 ("Петя Галева",False,"преди 23 часа","Усещането за глад е много по-слабо и съм успяла да сваля 3 кг.","love","13","avatar-petya-galeva-1.jpg"),
 ("Петя Галева",False,"преди 23 часа","Наистина ме изненадаха тези лепенки. Препоръчвам ги с две ръце.","love","13","avatar-petya-galeva-2.jpg"),
]
fb_blocks = {}
for i,(a,v,t,txt,r,rt,av) in enumerate(fb_posts,1):
    fb_blocks[f"post{i}"] = {"type":"column","settings":{"post_author":a,"post_author_verified":v,"post_time":t,"post_text":f"<p>{txt}</p>","post_reactions":r,"post_reactions_text":rt,"post_comments_text":"","comment_1_author":"","comment_1_author_verified":False,"comment_1_time":"","comment_1_text":"","comment_2_author":"","comment_2_author_verified":False,"comment_2_time":"","comment_2_text":"","post_author_avatar":f"shopify://shop_images/{av}"}}

main_settings = {"display_id":False,"enable_sticky_info":True,"display_variant_image_first":False,"disable_prepend":True,"hide_variants":False,"variant_image_filtering":"none","image_zoom":"none","thumbnails_ratio":"square","arrows_color_scheme":"inverse","transparent_arrows":False,"dots_color_scheme":"inverse","video_player":"play_btn","enable_video_looping":False,"autoplay_videos_pause_btn":False,"video_sound_btn":False,"video_timeline":False,"play_btn_color_scheme":"accent-1","sound_btn_color_scheme":"inverse","timeline_color":"accent-1","media_size":"medium","media_position":"left","gallery_layout":"thumbnail_slider","desktop_thumbnails_position":"bottom","desktop_thumbnails_count":5,"desktop_vertical_thumbnails_width":16,"desktop_vertical_thumbnails_hide_arrows":False,"constrain_to_viewport":True,"media_fit":"contain","desktop_arrows_position":"hidden","mobile_media_corner_radius":0,"mobile_spacing_pixels":0,"mobile_arrows_position":"sides","mobile_pagination":"dots_overlay","mobile_thumbnails_position":"hidden","mobile_thumbnails_count":5,"mobile_vertical_thumbnails_width":22,"mobile_vertical_thumbnails_hide_arrows":True,"mobile_scroll_padding_percentage":0,"mobile_scroll_padding_pixels":14,"enable_mobile_outher_spacing":False,"mobile_slides_container_width":100,"mobile_slides_inner_width":100,"trust_badge_position":"top-right","trust_badge_size":"medium","mobile_padding_top":0,"mobile_padding_bottom":16,"desktop_padding_top":8,"desktop_padding_bottom":36}

fb_settings = {"display_id":False,"visibility":"always-display","title":"Какво казват клиентите ни във Facebook","title_highlight_color":"#6d388b","heading_size":"h1","text":"","color_scheme":"background-2","type":"slide","autoplay":False,"autoplay_speed":5,"arrows_color_scheme":"inverse","transparent_arrows":True,"dots_color_scheme":"inverse","desktop_full_page":False,"columns_desktop":3,"slider_desktop":False,"per_move_desktop":1,"desktop_spacing":24,"desktop_side_padding":0,"desktop_padding_calc":True,"desktop_adaptive_height":False,"desktop_dots_position":"under","desktop_arrows_position":"sides","slider_mobile":True,"enable_mobile_preview":False,"mobile_adaptive_height":False,"mobile_dots_position":"under","mobile_arrows_position":"under","post_bg_color":"#ffffff","post_text_color":"#101010","comments_bg_color":"#f0f2f5","separators_color":"#a4b0be","post_border_color":"#dfdfdf","border_width":1,"like_label":"Харесвам","comment_label":"Коментар","reply_label":"Отговор","share_label":"Сподели","padding_top":40,"padding_bottom":40,"custom_colors_background":"#f3f3f3","custom_gradient_background":"","custom_colors_text":"#2e2a39"}

def blocks(prefix, items, btype, keys):
    b, order = {}, []
    for i,it in enumerate(items,1):
        k=f"{prefix}{i}"; order.append(k)
        b[k]={"type":btype if isinstance(btype,str) else it[0],"settings":dict(zip(keys,it if isinstance(btype,str) else it[1:]))}
    return b, order

ly_b, ly_o = blocks("ly",[
 ("Дишащ външен слой","Пази активния слой и не оставя следи по дрехите."),
 ("Активен слой","Берберин и растителни екстракти, които се подават постепенно през деня."),
 ("Мек лепилен слой","Държи лепенката на място, без да дърпа кожата при сваляне."),
 ("Защитно фолио","Сваляш го точно преди да залепиш — лепенката е чиста до момента на употреба.")],"layer",["heading","text"])

tl_b, tl_o = blocks("st",[
 ("Първите дни","Свикваш с лепенката — една сутрин и забравяш за нея. Някои усещат по-малко желание за сладко още тогава, други не. И двете са нормални."),
 ("Седмица 1 – 2","Берберинът се подава постепенно всеки ден. Тук много клиенти казват, че вечер посягат по-рядко към сладкото."),
 ("Седмица 3 – 4","Вече е навик. Съчетай лепенката с нормално хранене и малко движение — така промяната се задържа.")],"step",["when","text"])

faq = [
 ("category","За продукта"),
 ("qa","Какво е FitPatches?","<p>Тънка лепенка с берберин и растителни екстракти. Слагаш я сутрин на чиста кожа и активните съставки се подават постепенно през деня. Отвън е затворена — нищо не остава по дрехите.</p>"),
 ("qa","Какво съдържа?","<p>Берберин и растителни екстракти. Пълният състав е написан на опаковката.</p>"),
 ("qa","Защо през кожата, а не на капсули?","<p>Капсулите минават през стомаха и черния дроб, където част от берберина се губи, а при много хора дразнят стомаха. Лепенката заобикаля стомаха и подава съставките бавно и равномерно.</p>"),
 ("qa","FitPatches лекарство ли е?","<p>Не. FitPatches не е лекарство, не лекува и не замества терапия, назначена от лекар.</p>"),
 ("category","Употреба"),
 ("qa","Къде да я залепя?","<p>На чиста и суха кожа — ръка, корем или бедро. Сменяй мястото всеки ден, за да не се дразни едно и също петно.</p>"),
 ("qa","Кога да я слагам?","<p>Сутрин, след като кожата е чиста и суха. Носи я през деня и следвай указанията на опаковката.</p>"),
 ("qa","Ако забравя един ден?","<p>Нищо страшно — продължаваш на следващия ден. Не слагай две наведнъж, за да наваксаш.</p>"),
 ("category","Безопасност"),
 ("qa","Има ли странични ефекти?","<p>Съставките са растителни и обикновено се понасят добре. Ако кожата се зачерви или засърби, махни лепенката и смени мястото. Ако раздразнението продължи, спри употребата.</p>"),
 ("qa","Мога ли, ако пия лекарства?","<p>Берберинът може да влияе на действието на някои лекарства — например за кръвна захар или кръвно налягане. Ако пиеш лекарства всеки ден, първо попитай лекаря си.</p>"),
 ("qa","При бременност и кърмене?","<p>Не използвай FitPatches при бременност и кърмене без консултация с лекар.</p>"),
 ("category","Резултати"),
 ("qa","За колко време ще усетя разлика?","<p>При всеки е различно. Много клиенти усещат по-малко желание за храна още в първите дни. За видима промяна дай на тялото 4–8 седмици — по една лепенка на ден.</p>"),
 ("qa","Ами ако не усетя нищо?","<p>Затова започваш без риск — плащаш при получаване. Пробвай един пакет и ако не усетиш разлика в апетита, просто не поръчваш пак.</p>"),
 ("category","Поръчка и доставка"),
 ("qa","Как плащам?","<p>С наложен платеж — плащаш на куриера, когато получиш пратката. Без предплащане.</p>"),
 ("qa","За колко време пристига?","<p>Изпращаме с Еконт до адрес или офис. Обикновено пристига за 2–4 работни дни.</p>"),
 ("qa","За колко стига един пакет?","<p>30 лепенки — по една на ден, точно за един месец.</p>"),
 ("qa","Има ли абонамент?","<p>Няма. Плащаш веднъж за това, което поръчаш. Няма автоматични плащания.</p>"),
]
faq_b, faq_o = {}, []
for i,it in enumerate(faq,1):
    k=f"f{i}"; faq_o.append(k)
    faq_b[k] = {"type":"category","settings":{"name":it[1]}} if it[0]=="category" else {"type":"qa","settings":{"q":it[1],"a":it[2]}}

tpl = {
 "sections": {
  "main": {"type":"main-product","blocks":{
     "title":{"type":"title","settings":{"text_size":"h1","title_alignment":"left","uppercase_title":False,"margin_top":0,"margin_bottom":0}},
     "a6eb81db-40e4-43e0-972f-32db010a4a56":{"type":"rating_stars","settings":{"rating":4.8,"star_color":"#ffcc00","bg_stars_style":"full","bg_star_color":"#ececec","label":"<strong>4.8/5</strong> според <strong>2365</strong> доволни клиенти","size":16,"alignment":"flex-start","scroll_id":"","margin_top":0,"margin_bottom":9}},
     "fp_custom_offer":{"type":"custom_liquid","settings":{"custom_liquid":"{% render 'fp-offer-v2', product: product %}"}},
     "fpx_extras":{"type":"custom_liquid","settings":{"custom_liquid":"{% render 'fpx-buybox-extras' %}"}}},
   "block_order":["title","a6eb81db-40e4-43e0-972f-32db010a4a56","fp_custom_offer","fpx_extras"],
   "custom_css":[],"settings":main_settings},
  "fp_features":{"type":"fp-features","settings":{}},
  "fpx_vs":{"type":"fpx-vs","settings":{"img_fp":"shopify://shop_images/fpx-vs-patch.jpg","img_other":"shopify://shop_images/fpx-vs-capsules.jpg"}},
  "fp_howworks":{"type":"fp-howworks","settings":{}},
  "fpx_layers":{"type":"fpx-layers","blocks":ly_b,"block_order":ly_o,"settings":{"image":"shopify://shop_images/fpx-layers.jpg"}},
  "fpx_nostomach":{"type":"fpx-nostomach","settings":{"image":"shopify://shop_images/fpx-nostomach.jpg"}},
  "fp_science":{"type":"fp-science","settings":{}},
  "fpx_timeline":{"type":"fpx-timeline","blocks":tl_b,"block_order":tl_o,"settings":{"image":"shopify://shop_images/fpx-timeline.jpg"}},
  "fp_fb_reviews":{"type":"facebook-testimonials","blocks":fb_blocks,"block_order":list(fb_blocks),"settings":fb_settings},
  "fpx_faq":{"type":"fpx-faq","blocks":faq_b,"block_order":faq_o,"settings":{}},
  "fp_vs":{"type":"fp-vs","disabled":True,"settings":{}},
  "fp_results":{"type":"fp-results","disabled":True,"settings":{}},
  "fp_analysis":{"type":"fp-analysis","disabled":True,"settings":{}},
  "fp_img_collage":{"type":"fp-image-slot","disabled":True,"settings":{"label":"Място за снимка: много хора използват FitPatches (колаж)","height":"360"}}
 },
 "order":["main","fp_features","fpx_vs","fp_howworks","fpx_layers","fpx_nostomach","fp_science","fpx_timeline","fp_fb_reviews","fpx_faq","fp_vs","fp_results","fp_analysis","fp_img_collage"]
}
open(out,"w").write(json.dumps(tpl, ensure_ascii=False, separators=(",",":")))
print(len(open(out).read()))
