label alt_day4_mi_cl_vars:
    $ alt_day4_mi_mi2midj_transit = False
    $ alt_day4_mi_vodka = False
    $ alt_day4_mi_clothes = False
    $ alt_day4_mi_bake = False
    $ alt_day4_mi_coal = False
    $ alt_day4_mi_senio = 0
    $ alt_day4_mi_photo_slavya = False
    $ alt_day4_mi_photo = False
    $ alt_day4_mi_rival_won = False
    $ alt_day4_mi_dance = False
    $ alt_day4_mi_comfort = False
    $ alt_day4_mi_supper_sl = False
    return

label alt_day4_mi_cl_start:
    call alt_day4_mi_cl_vars
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Мику. Утро. Медпункт")
    call alt_day4_mi_start
    pause(1)
    call alt_day4_mi_cs_med_play
    pause(1)
    if not alt_day4_mi_rival_won:
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(4, u"Мику. Медпункт. Дежурство")
        call alt_day4_mi_duty
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Мику. Ужин")
        call alt_day4_mi_supper_sick
        pause(1)
    else:
        $ persistent.sprite_time = "day"
        $ day_time()
        if alt_day4_mi_mi2midj_transit:

            $ alt_chapter(4, u"Мику.Свидание")
            call alt_day4_mi_visit_sick
            pause(1)
            call alt_day4_mi_rps3
            pause(1)
            call alt_day4_mi_movealong
            pause(1)
            call alt_day4_mi_med_EV
            pause(1)
            call alt_day4_mi_back2radio
            pause(1)
            $ persistent.sprite_time = "sunset"
            $ sunset_time()
            if alt_day4_mi_comfort:
                $ sunset_time()
                $ alt_chapter(4, u"Мику. DJ. Вечер")
                call alt_day4_mi_date
                pause(1)
                jump alt_stories_start
            else:
                $ persistent.sprite_time = "sunset"
                $ sunset_time()
                $ alt_chapter(4, u"Мику. Вечер.")
                call alt_day4_mi_date_sick
                pause(1)
                call alt_day4_mi_xroad
                pause(1)
                $ night_time()
                $ persistent.sprite_time = "night"
                call alt_day4_mi_herbs
                pause(1)
                jump alt_stories_start
        else:
            $ alt_chapter(4, u"Мику. Клуб")
            call alt_day4_mi_club_sick
            pause(1)
            $ alt_chapter(4, u"Мику. Вечер")
            call alt_day4_mi_med_EV
    call alt_day4_mi2sl_mi
    pause(1)
    if not alt_day4_mi_dance:
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Мику. Вечер.")
        call alt_day4_mi_date_sick
        pause(1)
        call alt_day4_mi_xroad
        pause(1)
        $ night_time()
        $ persistent.sprite_time = "night"
        call alt_day4_mi_herbs
        pause(1)
    jump alt_stories_start
