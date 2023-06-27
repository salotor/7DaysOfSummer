label alt_day4_map_un_cl:
    $ disable_all_zones_alt2()
    $ disable_all_chibi_alt2()
    $ set_zone_alt2('un_mi_house_alt2', 'alt_day4_fake_map_un_cl')
    $ set_zone_alt2('boat_station_alt2', 'alt_day4_fake_map_un_cl')
    $ set_zone_alt2('volleyball_alt2',  'alt_day4_fake_map_un_cl')
    $ set_zone_alt2('beach_alt2',     'alt_day4_fake_map_un_cl')
    $ show_map_alt2()

label alt_day4_fake_map_un_cl:
    return

label alt_day4_map_un_cl_2_prepare:
    play music music_7dl["lazy_olga"] fadein 3
    $ disable_all_zones_alt2()
    $ disable_all_chibi_alt2()
    $ set_zone_alt2('library_alt2', 'alt_day4_un_cl_library')
    $ set_zone_alt2('sport_area_alt2', 'alt_day4_un_cl_sport_area')
    $ set_zone_alt2('beach_alt2',  'alt_day4_un_cl_beach')
    jump alt_day4_map_un_cl_2

label alt_day4_map_un_cl_2:
    $ show_map_alt2()

label alt_day4_un_cl_library:
    scene bg int_library_day
    with dissolve
    play sound sfx_door_squeak_light
    "Дедуктивный метод подсказывал, что если вчера Лена рисовала тут, то высока была вероятность того, что и сегодня она будет в этом же самом месте."
    "Если повезёт, конечно."
    "Я вошёл внутрь и огляделся."
    "Было что-то странное в атмосфере этого места сегодня — что-то инородное."
    "Сделав несколько шагов вперёд, я понял, что именно."
    "Тишина."
    "Жужелица в этот раз не рубила лбом столешницу и её посапывание не разносилось эхом по всей библиотеке."
    "На этот раз она придумала кое-что получше."
    "Она просто физически отсутствовала на рабочем месте, в то время как библиотека была открыта."
    "Странно."
    "Впрочем, я не хотел думать о ней. У меня была другая цель."
    scene bg int_editorial_day_7dl with dissolve
    play sound sfx_medpunkt_door_open
    "Я распахнул дверь в комнату редакции…"
    "…чтобы обнаружить, что там тоже никого не было."
    "Блин. И где все-то?"
    "Что-то важное случилось, а я не в курсе?"
    scene bg ext_library_day with dissolve
    "Я вышел из библиотеки."
    "Где ещё Лена может быть?"
    $ disable_current_zone_alt2()
    jump alt_day4_map_un_cl_2

label alt_day4_un_cl_sport_area:
    scene ext_square_day
    with dissolve
    "Она говорила, что учится играть в бадминтон, и это значит, что она могла быть на спортплощадке."
    dreamgirl "Сразу после приёма пищи побежала ракеткой махать, да?"
    "Бадминтон — не теннис. Там такой нагрузки нет, можно и помахать."
    dreamgirl "Ну да, конечно."
    "Не веришь?"
    dreamgirl "Верю конечно, родненький ты мой! Вот только кажется мне, почему-то, что её там не будет. Вот прям чуйствую."
    "Пока не проверим, не узнаем."
    scene bg ext_playground_day with dissolve
    "Когда я пришёл на спортплощадку, с моих губ сорвался горестный вздох."
    "Все корты, тренажеры и площадки были пусты."
    "Перекати-поля только не хватает."
    dreamgirl "Я же говорил."
    "Я не ответил."
    "Нужно было искать дальше."
    $ disable_current_zone_alt2()
    jump alt_day4_map_un_cl_2

label alt_day4_un_cl_beach:
    pass