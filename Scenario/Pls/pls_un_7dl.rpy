label alt_day4_un_7dl_start:
    if (counter_un_7dl == 6) and (lp_un >= 13):
        call alt_day4_un_7dl_vars
        call alt_day4_me_neu_vars
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Лена. 7ДЛ. Утро")
        call alt_day4_un_7dl_begin
        pause(1)
        if not alt_day4_un_7dl_morning_searching:
            call alt_day4_un_7dl_lineup
            pause(1)
        call alt_day4_un_7dl_breakfast
        pause(1)
        if herc:
            call alt_day4_un_7dl_entrance
            pause(1)
        call alt_day4_un_7dl_declaration
        pause(1)
        call alt_day4_un_7dl_library
        pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(4, u"Лена. 7ДЛ. День")
    call alt_day4_un_7dl_dinner
    pause(1)
    if loki:
        call alt_day4_un_7dl_day_loki
    elif herc:
        call alt_day4_un_7dl_day_herc
    else:
        if 'nwsppr' in list_clubs_7dl:
            call alt_day4_un_7dl_day_dr_nwsppr
        else:
            call alt_day4_un_7dl_day_dr_badmin
    call alt_day4_un_7dl_launch
    pause(1)
    call alt_day4_un_7dl_concert
    pause(1)
    call alt_day4_un_7dl_dynamite
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Лена. 7ДЛ. Вечер")
    call alt_day4_un_7dl_supper
    pause(1)
    if herc or loki:
        call alt_day4_un_7dl_evening
    else:
        call alt_day4_un_7dl_evening_dr
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day4_un_7dl_dock
    pause(1)
    call alt_day4_un_7dl_sleeptime
    pause(1)
    jump alt_day5_un_7dl_start

label alt_day5_un_7dl_start:
    pause(1)
    call alt_day5_un_7dl_vars
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Лена. 7ДЛ. Утро")
    call alt_day5_un_7dl_begin
    pause(1)
    call alt_day5_un_7dl_breakfast
    pause(1)
    if loki and (alt_day1_sl_keys_took in (1, 3)):
        call alt_day5_un_7dl_breakfast_l
        pause(1)
        call alt_day5_un_7dl_clubs
        pause(1)
        call alt_day4_un_7dl_cinema
        pause(1)
    else:
        if loki:
            call alt_day5_un_7dl_breakfast_l
            pause(1)
        elif herc:
            call alt_day5_un_7dl_breakfast_h
            pause(1)
        if dr:
            call alt_day5_un_7dl_games
            pause(1)
        else:
            call alt_day5_un_7dl_cleaning
            pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(5, u"Лена. 7ДЛ. Обед")
        call alt_day5_un_7dl_dinner
        pause(1)
        if dr and ('nwsppr' in list_clubs_7dl):
            call alt_day5_un_7dl_article
            pause(1)
            call alt_day5_un_7dl_unl
            pause(1)
        else:
            call alt_day5_un_7dl_np
            pause(1)
        call alt_day5_un_7dl_launch
        pause(1)
        if dr and ('nwsppr' in list_clubs_7dl):
            call alt_day5_un_7dl_library
            pause(1)
        else:
            call alt_day5_un_7dl_washing
            pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Лена. 7ДЛ. Вечер")
    call alt_day5_un_7dl_supper
    pause(1)
    call alt_day5_un_7dl_campfire
    pause(1)
    if loki and (alt_day1_sl_keys_took in (1, 3)):
        call alt_day5_un_7dl_video
        pause(1)
    else:
        if dr and ('nwsppr' in list_clubs_7dl):
            call alt_day5_un_7dl_runaway
            pause(1)
        elif alt_day5_un_7dl_washing == 'me':
            call alt_day5_un_7dl_evening_un
            pause(1)
            call alt_day5_un_7dl_runaway
            pause(1)
        elif alt_day5_un_7dl_washing == 'sl_un':
            call alt_day5_un_7dl_evening_dv
            pause(1)
        call alt_day5_un_7dl_island_hen
        pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    $ alt_chapter(5, u"Лена. 7ДЛ. Ночь")
    call alt_day5_un_7dl_sleeptime
    pause(1)
    jump alt_day6_un_7dl_start

label alt_day6_un_7dl_start:
    pause(1)
    call alt_day6_un_7dl_vars
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Лена. 7ДЛ. Утро")
    call alt_day6_un_7dl_begin
    pause(1)
    call alt_day6_un_7dl_search
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(6, u"Лена. 7ДЛ. День")
    call alt_day6_un_7dl_dinner
    pause(1)
    call alt_day6_un_7dl_career
    pause(1)
    call alt_day6_un_7dl_music_club
    pause(1)
    call alt_day6_un_7dl_concert
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Лена. 7ДЛ. Вечер")
    call alt_day6_un_7dl_supper
    pause(1)
    call alt_day6_un_7dl_catapult
    pause(1)
    if alt_day_catapult:
        return
    $ persistent.sprite_time = "night"
    $ night_time()
    $ alt_chapter(6, u"Лена. 7ДЛ. Танцы")
    call alt_day6_un_7dl_dance
    pause(1)
    $ alt_chapter(6, u"Лена. 7ДЛ. Ночь")
    call alt_day6_un_7dl_sleeptime
    pause(1)
    $ alt_day7_un_7dl_rnm = lp_un * 4
    if (alt_day5_un_7dl_washing == 'sl_un') or alt_day4_un_7dl_dv_us_explosives:
        $ alt_day7_un_7dl_rnm = alt_day7_un_7dl_rnm * 1.1
    if (alt_day5_un_7dl_washing == 'sl_un') and alt_day4_un_7dl_dv_us_explosives:
        $ alt_day7_un_7dl_rnm = alt_day7_un_7dl_rnm * 1.2
    if persistent.mt_7dl_good:
        $ alt_day7_un_7dl_rnm = alt_day7_un_7dl_rnm * 0.9

    if alt_day4_me_neu_transit == 'un_7dl':
        $ routetag = "un"
    elif alt_day6_un_7dl_agreed or (alt_day7_un_7dl_rnm <= 75):
        $ routetag = "un7dlbad"
    else:
        $ routetag = "un7dlgood"
    jump alt_day7_un_7dl_start

label alt_day7_un_7dl_start:
    call alt_day7_un_7dl_vars
    pause(1)
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    $ alt_chapter(7, u"Лена. 7ДЛ. Утро")
    call alt_day7_un_7dl_begin
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    call alt_day7_un_7dl_day
    pause(1)
    call alt_day7_un_7dl_dinner
    pause(1)
    call alt_day7_un_7dl_hysterics
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day7_un_7dl_pills
    pause(1)
    $ alt_chapter(7, u"Лена. 7ДЛ. Эпилог")
    if routetag == "un7dlgood":
        call alt_day7_un_7dl_miracle
        pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        call alt_day7_un_7dl_rollback
        pause(1)
        call alt_day7_un_7dl_departure
        pause(1)
        if alt_day7_un_7dl_shard_end:
            call alt_day7_un_7dl_shard
            pause(1)
        elif alt_day7_un_7dl_rej_end:
            $ persistent.sprite_time = "prolog"
            $ prolog_time()
            call alt_day7_un_7dl_rej
            pause(1)
        elif karma >= 75:
            call alt_day7_un_7dl_good_ussr
            pause(1)
        else:
            call alt_day7_un_7dl_good_rf
            pause(1)
    elif routetag == "un7dlbad":
        call alt_day7_un_7dl_bad
        pause(1)
    elif routetag == "un":
        if alt_day7_un_7dl_shard_end:
            call alt_day7_un_7dl_shard
            pause(1)
        elif (alt_day7_un_7dl_rnm > 75) and (karma >= 75):
            call alt_day7_un_7dl_miracle
            pause(1)
            $ persistent.sprite_time = "day"
            $ day_time()
            call alt_day7_un_7dl_rollback
            pause(1)
            call alt_day7_un_7dl_departure
            pause(1)
            call alt_day7_un_7dl_good_ussr
        else:
            call alt_day7_un_7dl_rej2
        pause(1)
    return
