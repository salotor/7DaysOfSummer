label alt_day6_me_neu_start_old:
    "За кого будем играть?"
    menu:
        "Локи":
            $ loki = True
            $ plthr = u"Локи"
        "Дрищ":
            $ dr = True
            $ plthr = u"Дрищ"
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Одиночка. Утро")
    call alt_day6_me_neu_begin_old
    pause(1)
    call alt_day6_me_neu_morning_old
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    if loki:
        $ alt_chapter(6, u"Одиночка. День")
        call alt_day6_me_neu_loki_day_old
        pause(1)
        call alt_day6_me_neu_loki_concert_old
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(6, u"Одиночка. Танцы")
        call alt_day6_me_neu_loki_disco_old
        pause(1)
    else:
        $ alt_chapter(6, u"Одиночка. День")
        call alt_day6_me_neu_dr_day_old
        pause(1)
        call alt_day6_me_neu_dr_concert_old
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(6, u"Одиночка. Танцы")
        call alt_day6_me_neu_dr_disco_old
        pause(1)
    call alt_day6_me_neu_pirate_old
    pause(1)
    if loki:
        call alt_day6_me_neu_loki_disco2_old
        pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        call alt_day6_me_neu_loki_evening_old
    else:
        call alt_day6_me_neu_dr_disco2_old
        pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        call alt_day6_me_neu_dr_evening_old
    pause(1)
    call alt_day6_me_neu_sleeptime_old
    pause(1)
    jump alt_stories_start

label alt_day7_me_neu_start_old:
    "За кого будем играть?"
    menu:
        "Локи":
            $ loki = True
            $ plthr = u"Локи"
        "Дрищ":
            $ dr = True
            $ plthr = u"Дрищ"
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(7, u"Одиночка. Сон")
    call alt_day7_me_neu_sleep_old
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(7, u"Одиночка. Подъём")
    call alt_day7_me_neu_wakeup_old
    pause(1)
    call alt_day7_me_neu_explore_old
    pause(1)
    $ persistent.sprite_time = 'night'
    $ night_time()
    $ alt_chapter(7, u"Одиночка. Диалог")
    call alt_day7_me_neu_dialogue_old
    pause(1)
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    menu:
        "Настоящее":
            $ alt_chapter(7, u"Одиночка. Настоящее")
            if loki:
                call alt_day7_me_neu_loki_neu_old
            else:
                call alt_day7_me_neu_dr_neu_old
        "Будущее":
            $ alt_chapter(7, u"Одиночка. Будущее")
            call alt_day7_me_neu_sept
    jump alt_stories_start