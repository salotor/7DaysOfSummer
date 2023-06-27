label alt_day4_mi_dj_start:
    call alt_day4_mi_dj_vars
    $ persistent.sprite_time = "night"
    $ night_time()
    $ alt_chapter(4, u"Miku. DJ. Night")
    call alt_day4_mi_dj_begin
    pause(1)
    if alt_day4_mi_dj_hedg:
        call alt_day4_mi_dj_hedg_hunt
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Miku. DJ. Morning")
    call alt_day4_mi_dj_morning
    pause(1)
    call alt_day4_mi_dj_day
    pause(1)
    if alt_day3_technoquest1 >= 1:
        call alt_day4_mi_dj_radio
        pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(4, u"Miku. DJ. Day")
        call alt_day4_mi_dj_dinner
        pause(1)
    else:
        call alt_day4_mi_dj_cleaning
        pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        if not alt_day4_mi_dj_hedg:
            $ alt_chapter(4, u"Miku. DJ. Day")
            call alt_day4_mi_dj_dinner
            pause(1)
        else:
            $ alt_chapter(4, u"Miku. DJ. Day")
            call alt_day4_mi_dj_dinner2
            pause(1)
    call alt_day4_mi_dj_repetition
    pause(1)
    call alt_day4_mi_dj_volley
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Miku. DJ. Evening")
    call alt_day4_mi_dj_supper
    pause(1)
    call alt_day4_mi_dj_evening
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day4_mi_dj_night
    pause(1)
    call alt_day4_mi_dj_sleeptime
    pause(1)
    jump alt_day5_mi_dj_start

label alt_day5_mi_dj_start:
    call alt_day5_mi_dj_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Miku. DJ. Morning")
    call alt_day5_mi_dj_begin
    pause(1)
    call alt_day5_mi_dj_breakfast
    pause(1)
    $ alt_chapter(5, u"Miku. DJ. Movie")
    call alt_day5_mi_dj_cinema
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(5, u"Miku. DJ. Day")
    call alt_day5_mi_dj_dinner
    pause(1)
    call alt_day5_mi_dj_jammer
    pause(1)
    call alt_day5_mi_dj_vocadrama
    pause(1)
    call alt_day5_mi_dj_mapprepare
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Miku. DJ. Evening")
    call alt_day5_mi_dj_supper
    pause(1)
    call alt_day5_mi_dj_campfire
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    if alt_day5_mi_dj_voyeur == 2:
        call alt_day5_mi_dj_voyeur_2
    elif alt_day5_mi_dj_voyeur == 3:
        call alt_day5_mi_dj_voyeur_3
    else:
        call alt_day5_mi_dj_voyeur_4
    pause(1)
    if alt_day5_mi_dj_voyeur == 4 or (alt_day5_mi_dj_voyeur == 2 and alt_day5_mi_dj_dv_blade):
        $ alt_chapter(5, u"Miku. DJ. Night")
        call alt_day5_mi_dj_late_evening
        pause(1)
        if alt_day5_mi_dj_apology == 1:
            call alt_day5_mi_dj_evening_club1
            pause(1)
            if alt_day5_mi_dj_apology == 3:
                call alt_day5_mi_dj_sleeptime
                pause(1)
            else:
                call alt_day5_mi_dj_evening_club2
                pause(1)
                if not alt_day5_mi_dj_hentai_done:
                    call alt_day5_mi_dj_sleeptime
                    pause(1)
        else:
            call alt_day5_mi_dj_sleeptime
            pause(1)
    else:
        call alt_day5_mi_dj_sleeptime
        pause(1)
    jump alt_day6_mi_dj_start

label alt_day6_mi_dj_start:
    pause(1)
    call alt_day6_mi_dj_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Miku. DJ. Morning")
    if alt_day5_mi_dj_hentai_done:
        call alt_day6_mi_dj_good
        pause(1)
    else:
        call alt_day6_mi_dj_neutral
        pause(1)
        call alt_day6_mi_dj_neutral_breakfast
        pause(1)
    $ alt_chapter(6, u"Miku. DJ. Live!")
    call alt_day6_mi_dj_radio
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(6, u"Miku. DJ. Day")
    call alt_day6_mi_dj_dinner
    pause(1)
    if alt_day5_mi_dj_hentai_done:
        call alt_day6_mi_dj_rendezvous
    elif alt_day5_mi_dj_voyeur != 4:
        call alt_day6_mi_dj_forgiveness
    elif alt_day5_mi_dj_apology in (0, 3):
        call alt_day6_mi_dj_tale
    else:
        call alt_day6_mi_dj_plain
    $ alt_chapter(6, u"Miku. DJ. Concert")
    call alt_day6_mi_dj_concert
    pause(1)
    if alt_day5_mi_dj_voyeur != 4:
        if alt_day6_mi_dj_sonic_agreed:
            if alt_day5_mi_dj_apology == 2:
                call alt_day6_mi_dj_newswall
                pause(1)
                $ persistent.sprite_time = "sunset"
                $ sunset_time()
                call alt_day6_mi_dj_late_supper_un
                pause(1)
            else:
                call alt_day6_mi_dj_sonic
                pause(1)
                $ persistent.sprite_time = "sunset"
                $ sunset_time()
                call alt_day6_mi_dj_late_supper_sl
                pause(1)
        else:
            call alt_day6_mi_dj_reject
            pause(1)
            if alt_day6_mi_dj_un_evil:
                $ persistent.sprite_time = "sunset"
                $ sunset_time()
                call alt_day6_mi_dj_supper
                pause(1)
            else:
                call alt_day6_mi_dj_newswall
                pause(1)
                $ persistent.sprite_time = "sunset"
                $ sunset_time()
                call alt_day6_mi_dj_late_supper_un
                pause(1)
    else:
        call alt_day6_mi_dj_sonic
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        call alt_day6_mi_dj_late_supper_sl
        pause(1)
    $ alt_chapter(6, u"Miku. DJ. Disco")
    call alt_day6_mi_dj_discotheque
    pause(1)
    call alt_day6_mi_dj_first_dance
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day6_mi_dj_second_dance
    pause(1)
    if lp_mi >= 19 and not alt_day6_mi_dj_me_evil:
        call alt_day6_mi_dj_dance2_success
        pause(1)
        call alt_day6_mi_dj_escape
        pause(1)
    else:
        call alt_day6_mi_dj_dance2_fail
        pause(1)
        call alt_day6_mi_dj_catapult
        pause(1)
        if alt_day_catapult:
            return
        call alt_day6_mi_dj_sleeptime
        pause(1)
    jump alt_day7_mi_dj_start

label alt_day7_mi_dj_start:
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(7, u"Miku. DJ. Morning")
    if alt_day6_mi_dj_hentai2:
        $ routetag = "mi7dlgood"
        call alt_day7_mi_dj_together
    else:
        if alt_day6_mi_dj_catapult == 2:
            $ routetag = "mi7dlbad"
        elif alt_day6_mi_dj_catapult == 1:
            $ routetag = "mi7true"
        else:
            $ routetag = "mi7dl"
        call alt_day7_mi_dj_alone
    pause(1)
    if alt_day5_mi_dj_hentai_done:
        call alt_day7_mi_dj_badfeel
    else:
        call alt_day7_mi_dj_breakfast
    pause(1)
    call alt_day7_mi_dj_preparations
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    call alt_day7_mi_dj_departure
    pause(1)
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    if alt_day6_mi_dj_catapult in (1, 2):
        $ alt_chapter(7, u"Freezing without you")
        call alt_day7_mi_dj_epilogue_frost
        pause(1)
        if alt_day6_mi_dj_catapult == 2:
            call alt_day7_mi_dj_bad
            pause(1)
        else:
            call alt_day7_mi_dj_true
            pause(1)
    else:
        $ alt_chapter(7, u"World has gone mad")
        call alt_day7_mi_dj_good
        pause(1)
        if alt_day6_mi_dj_hentai2:
            call alt_day7_mi_dj_good_jap
            pause(1)
        else:
            call alt_day7_mi_dj_good_rf
            pause(1)
    return
