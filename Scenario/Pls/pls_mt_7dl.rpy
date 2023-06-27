label alt_day6_mt_7dl_start:
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Olga. Morning")
    call alt_day6_mt_7dl_begin
    pause(1)
    call alt_day6_mt_7dl_breakfast
    pause(1)
    $ alt_chapter(6, u"Olga. About unneeded")
    call alt_day6_mt_7dl_morning
    pause(1)
    if alt_day5_me_neu_mt_hentai:
        call alt_day6_mt_7dl_dv_morning
    else:
        call alt_day6_mt_7dl_un_morning
    pause(1)
    call alt_day6_mt_7dl_retail
    pause(1)
    if alt_day5_me_neu_mt_hentai:
        call alt_day6_mt_7dl_bitter
        pause(1)
        $ alt_chapter(6, u"Olga. First meetings")
        call alt_day6_mt_7dl_memento
    else:
        call alt_day6_mt_7dl_forgive
        pause(1)
        if alt_day4_me_neu_mt_diary and alt_day5_me_neu_mt_diary:
            $ alt_chapter(6, u"Olga. Diary. 1989")
            call alt_day6_mt_7dl_diary3
        else:
            call alt_day6_mt_7dl_memento
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(6, u"Olga. Day")
    call alt_day6_mt_7dl_dinner
    pause(1)
    call alt_day6_mt_7dl_memory
    pause(1)
    $ alt_chapter(6, u"Olga. Concert")
    call alt_day6_mt_7dl_concert
    pause(1)
    call alt_day6_mt_7dl_sonic
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Olga. Evening")
    call alt_day6_mt_7dl_supper
    pause(1)
    if counter_mt_7dl < 13:
        call alt_day6_mt_7dl_catapult
        pause(1)
        if alt_day_catapult:
           return
    call alt_day6_mt_7dl_disco
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    $ alt_chapter(6, u"Olga. Reunion")
    call alt_day6_mt_7dl_nighttime
    pause(1)
    call alt_day6_mt_7dl_hentai
    pause(1)
    if counter_mt_7dl < 13:
        $ routetag = "mt7dl_bad"
    jump alt_day7_mt_7dl_start

label alt_day7_mt_7dl_start:
    call alt_day7_mt_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(7, u"Olga. Morning")
    call alt_day7_mt_7dl_begin
    pause(1)
    call alt_day7_mt_7dl_morning
    pause(1)
    call alt_day7_mt_7dl_comet
    pause(1)
    call alt_day7_mt_7dl_breakfast
    pause(1)
    $ alt_chapter(7, u"Olga. Farewells")
    call alt_day7_mt_7dl_byes
    pause(1)
    if alt_day5_me_neu_mt_hentai:
        call alt_day7_mt_7dl_dv_bye
    else:
        if (counter_un_fz_mt_transit == 3):
            call alt_day7_mt_7dl_un_fz_bye
        else:
            call alt_day7_mt_7dl_un_bye
    pause(1)
    call alt_day7_mt_7dl_departure
    pause(1)
    if alt_day7_mt_7dl_pt == 1:
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(7, u"Olga. Choice: Past")
        call alt_day7_mt_7dl_loopthru
        pause(1)
        if (counter_mt_7dl >= 15) and (alt_day2_date == 'mt') and alt_day5_me_neu_mt_diary and alt_day4_me_neu_mt_diary:
            call alt_day7_mt_7dl_true
        else:
            call alt_day7_mt_7dl_neu
    elif alt_day7_mt_7dl_pt == 3:
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(7, u"Olga. Face of the Past")
        call alt_day7_mt_7dl_shard
    else:
        $ persistent.sprite_time = "prolog"
        $ prolog_time()
        $ alt_chapter(7, u"Olga. Choice: Future")
        call alt_day7_mt_7dl_loopback
        pause(1)
        if (counter_mt_7dl >= 13) and (alt_day2_date == 'mt') and (alt_day3_dancing2 == 'me_2') and (alt_day4_me_neu_date == 'mt'):
            call alt_day7_mt_7dl_good
        else:
            if (counter_un_fz_mt_transit == 3):
                call alt_day7_mt_7dl_herc_exc
            else:
                call alt_day7_mt_7dl_bad
    pause(1)
    return
