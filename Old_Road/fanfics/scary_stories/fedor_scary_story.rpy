init:
    $ path_scry = default_7dl_path + "Old_Road/fanfics/scary_stories/"
    $ sfx_scry_scotch = path_scry + "scotch_scry.ogg"

label fedor_scary_story:
    scene black with fade
    $ alt_pause(2)
    play ambience ambience_music_club_night fadein 1
    $ persistent.sprite_time = "night"
    scene bg int_library_night2
    show us normal pioneer at cright
    show dv normal pioneer2 at cleft
    show sl normal pioneer at fright behind us
    with fade3
    play music music_list["dance_of_fireflies"] fadein 1
    me "Однажды, самым обычным днем, когда ничего не предвещало беды, а на улице светило летнее солнце…"
    show us dontlike pioneer
    show dv dontlike pioneer2
    show sl upset pioneer behind us
    with dspr
    us "Семен, ну так не интересно! Мы страшилки рассказываем, а не детские сказки на ночь!"
    "Как я и ожидал, Ульяну получилось поддеть затянутым началом."
    "Впрочем, остальные тоже были не в особом восторге от моих прикольчиков. Всем здесь собравшимся хотелось мурашек по коже и шорохов во тьме, случайных скрипов и уханий птицы."
    "Да и мне самому, если уж совсем откровенно."
    show mz bukal glasses pioneer far at fleft behind dv
    show dv normal pioneer2
    with dspr
    mz  "Семен опять сам пошутил и сам посмеялся."
    "Послышалось из дальнего угла, где за столом, совсем без света, сидела Жужелица."
    hide mz with dissolve
    me "Ладно, ладно, слушайте, раз уж хотите."
    "Сдался я под гнетом критики и сердитых взглядов, и тут же понизил голос, играя на контрасте, нагоняя жути."
    me "Это случилось в лагере, когда все дети уже давно легли спать, а вожатые перестали следить за детьми."
    me "На улице царила королевская ночь – вожатые не ожидали ее, не смогли о ней узнать, а потому детей никто не сдерживал."
    show us normal pioneer
    show dv normal pioneer2
    show sl normal pioneer behind us
    with dspr
    us "Что дальше?"
    "Слегка недоверчиво прошептала Ульяна, но я-то видел, что я смог ее заинтересовать. Даже Алиса со Славей заинтересовались."
    play music music_list['door_to_nightmare'] fadein 1
    scene bg ext_camp_entrance_day
    show sh normal pioneer
    with dissolve
    $ set_mode_nvl()
    "За день до этой самой ночи в лагерь приехал самый обычный мальчик, немного стеснительный, в очках, опоздавший на начало смены."
    scene bg ext_house_of_el_night_7dl with dissolve
    "Ему не доверяли, боялись, что он расскажет вожатым, поэтому про королевскую ночь он не знал и спокойно спал."
    scene bg int_extra_house_nolight_7dl with dissolve
    "Естественно, над ним решили подшутить. Пока тот спал, его простынь, которой он укрывался, привязали к ножкам кровати, а по бокам налепили скотча."
    "Тот не просыпался, и те, кто это придумал, решили найти себе другое занятие, позабыв про мальчика."
    scene bg int_extra_house_day_7dl with dissolve
    "Уже позже утром, когда вожатые стали будить детей, оказалось, что простыня осталась на своем месте, приклеенная и привязанная."
    "Но когда ее стали раскрывать, под ней никого не было."
    "На подушке остались лежать очки мальчика, а с обратной стороны простыни чем-то красным было написано: ПоМогитЕ."
    nvl clear
    "Кровать пустовала еще долго – мальчика не могли найти, как бы ни пытались. Пока однажды, уже повзрослевшие и позабывшие этот случай ребята не приехали снова."
    scene bg int_extra_house_nolight_7dl with dissolve
    "В очередную королевскую ночь все веселились и шутили, будто ничего и не было."
    "Когда последний из детей лег спать, всегда заправленная простынь на пустующей кровати вдруг отодвинулась, и с нее встал мертвенно-бледный, шатающийся мальчик в очках."
    "Он, ничего не говоря, взял с чужой полки скотч и направился к другим кроватям."
    $ alt_pause(0.3)
    with flash_red
    "Утром в лагере было очень тихо."
    stop music fadeout 3
    $ alt_pause(1.5)
    $ set_mode_adv()
    scene bg int_library_night2
    show sl scared pioneer at fleft
    show us fear pioneer at cleft
    show el shocked pioneer at cright
    with dissolve
    play sound sfx_scry_scotch
    "Снаружи раздался скрип, будто отрывают скотч."
    "Славя нервно теребила косу, хотя я до конца не верил, что она способна бояться такого, а Ульяна уже откровенно шугалась смотреть в сторону от света фонаря."
    "Электроник вообще с середины рассказа от напряга открыл рот, просидев с такой моськой до конца."
    show dv normal pioneer2 at fright with dspr
    dv "Это конец?"
    "Спросила Алиса, пряча за дрожащей ухмылкой детский страх."
    me "Да."
    "Я внимательно оглядел серьезные лица, с трудом сдерживая улыбку."
    th "Расскажи я эту историю в детском лагере в своем родном мире, вызвал бы только пренебрежительные и скучающие взгляды."
    play music music_7dl["dead_silence"] fadein 3
    scene
    $ renpy.show("bg int_library_night2", what = Noir("bg int_library_night2"))
    with dissolve
    play sound sfx_open_door_squeak_2
    "Вдруг дверь в библиотеку скрипнула, и в библиотеку шагнула фигура, скрытая за простыней."
    "Простыней, покрытой какими-то красноватыми узорами, невидимыми в темноте."
    $ renpy.show("bg int_library_night2", at_list = [sdl_transform7], what = SS_com("bg int_library_night2"))
    with diam
    play music "<from 22.1>" + music_7dl["dead_silence"]
    voice "Нет.{w} Не конец."
    "Раздался замогильный голос."
    stop music fadeout 3
    scene bg int_library_night2
    show un shy pioneer
    with dissolve

    "У меня уже началась шевелиться шерсть на загривке, как простыня опустилась, и стало понятно, что под ней скрывалось бледное, но вполне человеческое лицо Лены."
    pause(1)
    show un laugh pioneer with dspr
    play music music_list["timid_girl"] fadein 3
    "Она смутилась под светом фонаря, но прыснула, увидев наши ошалелые морды."
    show un smile3 pioneer with dspr
    un "Вы сами не позвали меня, так что я решила напугать вас."
    "Объяснила девушка, присаживаясь в круг рядом с нами."
    show us dontlike pioneer at right
    show un smile pioneer
    with dspr
    us "Мы не знали, где ты гуляешь!"
    "Возмутилась Ульяна."
    show us normal pioneer at right with dspr
    "Хотя едва ли кто-то из нашей компании, даже Женя, остались равнодушными. Лена поступила по совести, отомстив нам, заодно и внеся перчинку в наши посиделки."
    dreamgirl "Гляди, как рассуждает, а у самого сердце в пятки ушло, взрослый!"
    un "Мне вожатая дала простынь на холст, я ее не воровала."
    "На всякий случай для Слави объяснила Лена."
    un "Можно я следующая рассказываю?"
    "В новом коллективе истории шли гораздо интереснее и живее."
    if not persistent.pivo_default_7dl:
        jump alt_stories_start
    else:
        return