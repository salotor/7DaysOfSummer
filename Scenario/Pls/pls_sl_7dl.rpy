label alt_day4_sl_7dl_start:
    if herc or loki:
        $ routetag = "sl7dl_sport"
    else:
        $ routetag = "sl7dl"
    call alt_day4_sl_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Slavya. 7DS. Morning")
    pause(1)
    call alt_day4_sl_7dl_begin
    pause(1)
    call alt_day4_sl_7dl_breakfast
    pause(1)
    if loki:
        $ routetag = "sl7dl_loki"
        call alt_day4_sl_7dl_loki_morning
        pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(4, u"Slavya. 7DS. Day")
        call alt_day4_sl_7dl_loki_day
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Slavya. 7DS. Evening")
        call alt_day4_sl_7dl_loki_evening
    elif herc:
        $ routetag = "sl7dl_herc"
        call alt_day4_sl_7dl_herc_morning
        pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(4, u"Slavya. 7DS. Day")
        call alt_day4_sl_7dl_herc_day
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Slavya. 7DS. Evening")
        call alt_day4_sl_7dl_herc_evening
    else:
        call alt_day4_sl_7dl_morning
        pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(4, u"Slavya. 7DS. Day")
        call alt_day4_sl_7dl_day
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Slavya. 7DS. Evening")
        call alt_day4_sl_7dl_evening
    pause(1)
    call alt_day4_sl_7dl_sundown
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day4_sl_7dl_sleeptime
    pause(1)
    jump alt_day5_sl_7dl_start

label alt_day5_sl_7dl_start:
    if herc and alt_day4_sl_7dl_workout:
        $ routetag = "sl7dl_sport"
    call alt_day5_sl_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Slavya. 7DS. Morning")
    pause(1)
    call alt_day5_sl_7dl_begin
    pause(1)
    call alt_day5_sl_7dl_breakfast
    pause(1)
    if loki:
        $ routetag = "sl7dl_loki"
    elif herc:
        $ routetag = "sl7dl_herc"
    call alt_day5_sl_7dl_candle
    pause(1)
    if loki:
        call alt_day5_sl_7dl_candle_loki
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(5, u"Slavya. 7DS. Day")
        call alt_day5_sl_7dl_loki_day
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(5, u"Slavya. 7DS. Evening")
        call alt_day5_sl_7dl_loki_evening
    elif herc:
        call alt_day5_sl_7dl_candle_herc
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(5, u"Slavya. 7DS. Day")
        call alt_day5_sl_7dl_herc_day
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(5, u"Slavya. 7DS. Evening")
        call alt_day5_sl_7dl_herc_evening
        pause(1)
    else:
        call alt_day5_sl_7dl_candle_dr
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(5, u"Slavya. 7DS. Day")
        call alt_day5_sl_7dl_day
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(5, u"Slavya. 7DS. Evening")
        call alt_day5_sl_7dl_evening
    pause(1)
    $ alt_chapter(5, u"Slavya. 7DS. Campfire")
    call alt_day5_sl_7dl_campfire
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    if herc and (lp_sl > 16) and persistent.sl_7dl_herc_neu:
        call alt_day5_sl_7dl_hentai
        pause(1)
    call alt_day5_sl_7dl_sleeptime
    pause(1)
    if herc:
        call alt_day5_sl_7dl_rendezvous
        pause(1)
    with fade
    jump alt_day6_sl_7dl_start

label alt_day6_sl_7dl_start:
    if herc:
        call alt_day6_sl_7dl_camping
        pause(1)
        call alt_day6_sl_7dl_revenge
    if not alt_day5_sl_7dl_herc_sick:
        $ routetag = "sl7dl_sport"
    call alt_day6_sl_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Slavya. 7DS. Morning")
    pause(1)
    call alt_day6_sl_7dl_begin
    pause(1)
    if not alt_day5_sl_7dl_herc_sick:
        call alt_day6_sl_7dl_running
        pause(1)
        call alt_day6_sl_7dl_breakfast
        pause(1)
    if loki:
        $ routetag = "sl7dl_loki"
        call alt_day6_sl_7dl_loki_morning
        pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(6, u"Slavya. 7DS. Day")
        call alt_day6_sl_7dl_loki_day
        pause(1)
        call alt_day6_sl_7dl_loki_evening
    elif herc:
        $ routetag = "sl7dl_herc"
        if alt_day5_sl_7dl_herc_sick:
            call alt_day6_sl_7dl_herc_morning_sick
        else:
            call alt_day6_sl_7dl_herc_morning_well
        pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(6, u"Slavya. 7DS. Day")
        if alt_day6_sl_7dl_square:
            call alt_day6_sl_7dl_herc_day_alt
            pause(1)
            call alt_day6_sl_7dl_herc_evening_alt
        else:
            call alt_day6_sl_7dl_herc_day_normal
            pause(1)
            call alt_day6_sl_7dl_herc_evening_normal
    else:
        $ routetag = "sl7dl"
        if alt_day5_sl_7dl_olroad:
            call alt_day6_sl_7dl_dr_morning_olroad
        else:
            call alt_day6_sl_7dl_dr_morning_normal
        pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(6, u"Slavya. 7DS. Day")
        if alt_day5_sl_7dl_olroad:
            call alt_day6_sl_7dl_dr_day_olroad
            pause(1)
            call alt_day6_sl_7dl_dr_evening_olroad
        else:
            call alt_day6_sl_7dl_dr_day_normal
            pause(1)
            call alt_day6_sl_7dl_dr_evening_normal
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    call alt_day6_sl_7dl_supper
    pause(1)
    call alt_day6_sl_7dl_catapult
    pause(1)
    if alt_day_catapult:
        return
    if (herc or loki) or alt_day5_sl_7dl_olroad:
        $ routetag = "sl7dl_dress"
    $ alt_chapter(6, u"Slavya. 7DS. Disco")
    if loki:
        call alt_day6_sl_7dl_loki_disco
    elif herc:
        call alt_day6_sl_7dl_herc_disco
    else:
        call alt_day6_sl_7dl_dr_funeral
        if alt_day5_sl_7dl_olroad:
            call alt_day6_sl_7dl_dr_disco_olroad
        else:
            call alt_day6_sl_7dl_dr_disco_normal
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    if (lp_sl >= 19) and (karma > 120) and ((not loki) or (alt_day6_sl_7dl_forgive)):
        $ routetag = "sl7dlgood"
        pause(1)
    elif lp_sl >= 19:
        $ routetag = "sl7dlneu"
    else:
        $ routetag = "sl7dlbad"
    if lp_sl >= 19:
        if loki:
            if alt_day6_sl_7dl_forgive:
                call alt_day6_sl_7dl_loki_hentai
        elif herc:
            call alt_day6_sl_7dl_herc_hentai
        elif alt_day5_sl_7dl_olroad:
            call alt_day6_sl_7dl_dr_hentai_olroad
        else:
            call alt_day6_sl_7dl_dr_hentai_normal
    pause(1)
    if not alt_day6_sl_7dl_hentai_done or dr:
        call alt_day6_sl_7dl_sleeptime
    pause(1)
    jump alt_day7_sl_7dl_start

label alt_day7_sl_7dl_start:
    call alt_day7_sl_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(7, u"Slavya. 7DS. Morning")
    pause(1)
    if alt_day6_sl_7dl_hentai_done:
        if loki:
            call alt_day7_sl_7dl_begin_loki
        elif herc:
            call alt_day7_sl_7dl_begin_herc
        else:
            call alt_day7_sl_7dl_begin
    else:
        call alt_day7_sl_7dl_begin
    pause(1)
    if loki:
        if alt_day6_sl_7dl_forgive:
            call alt_day7_sl_7dl_packing_loki_forgive
        else:
            call alt_day7_sl_7dl_packing_loki_asshole
    elif herc:
        call alt_day7_sl_7dl_packing_herc
    else:
        call alt_day7_sl_7dl_packing
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(7, u"Slavya. 7DS. Departure")
    call alt_day7_sl_7dl_leaving
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ prolog_time()
    if lp_sl >= 20:
        if loki and not alt_day6_sl_7dl_forgive:
            $ routetag = "sl7dlneu"
        elif herc and not alt_day6_sl_7dl_square:
            $ routetag = "sl7dluv"
        else:
            $ routetag = "sl7dlgood"
    else:
        $ routetag = "sl7dlbad"
    $ alt_chapter(7, u"Slavya. 7DS. Epilogue")
    if alt_day7_sl_7dl_story_end:
        call alt_day7_sl_7dl_shard
    elif lp_sl >= 20:
        if karma < 120:
            if loki and not alt_day6_sl_7dl_forgive:
                call alt_day7_sl_7dl_bad
            else:
                call alt_day7_sl_7dl_good_rf
        else:
            if loki:
                call alt_day7_sl_7dl_loki
                pause(1)
                if alt_day6_sl_7dl_forgive:
                    call alt_day7_sl_7dl_loki_good
                else:
                    call alt_day7_sl_7dl_loki_rewind
                    pause(1)
                    if alt_day7_sl_7dl_loki_park:
                        call alt_day7_sl_7dl_loki_neu
                    else:
                        call alt_day7_sl_7dl_loki_rej
            elif herc:
                if karma >= 180:
                    call alt_day7_sl_7dl_herc_good
                else:
                    call alt_day7_sl_7dl_good_rf
            else:
                call alt_day7_sl_7dl_epi
                pause(1)
                if alt_day5_sl_7dl_olroad:
                    call alt_day7_sl_7dl_dr_good2
                else:
                    call alt_day7_sl_7dl_dr_good
    else:
        call alt_day7_sl_7dl_bad
    pause(1)
    return
