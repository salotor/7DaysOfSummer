﻿label alt_day4_mi_7dl_start:
    call alt_day4_mi_7dl_vars
    $ routetag = "mi7dl"
    $ persistent.sprite_time = "night"
    $ night_time()
    $ alt_chapter(4, u"Мику. 7ДЛ. Поездка.")
    call alt_day4_mi_7dl_ch1
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Мику. 7ДЛ. Утро.")
    call alt_day4_mi_7dl_ch2
    $ persistent.sprite_time = "day"
    $ day_time()
    if alt_day3_mi_7dl_donor == 2:
        call alt_day4_mi_7dl_ch3
        pause(1)
    $ alt_chapter(4, u"Мику. 7ДЛ. В город!")
    call alt_day4_mi_7dl_ch4
    pause(1)
    if alt_day3_mi_7dl_donor == 0:
        call alt_day4_mi_7dl_ch5a
    else:
        call alt_day4_mi_7dl_ch5b
        pause(1)
        call alt_day4_mi_7dl_ch52
    pause(1)
    $ alt_chapter(4, u"Мику. 7ДЛ. Домой.")
    call alt_day4_mi_7dl_ch6
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Мику. 7ДЛ. Вечер.")
    call alt_day4_mi_7dl_ch7
    pause(1)
    if alt_day3_mi_7dl_donor >= 1:
        $ alt_chapter(4, u"Мику. 7ДЛ. Рандеву?")
        call alt_day4_mi_7dl_ch8a
        pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        if alt_day4_mi_7dl_ev_savior and herc:
            call alt_day4_mi_7dl_ch81
        elif alt_day4_mi_7dl_ev_savior and loki:
            call alt_day4_mi_7dl_ch82
        else:
            call alt_day4_mi_7dl_ch83
    else:
        call alt_day4_mi_7dl_ch8b
    pause(1)
    jump alt_day5_mi_7dl_start

label alt_day5_mi_7dl_start:
    call alt_day5_mi_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    if alt_day4_mi_7dl_ev_savior and loki:
        $ alt_chapter(5, u"Мику. 7ДЛ. Дождь вместе")
        call alt_day5_mi_7dl_rain_2gether
    else:
        $ alt_chapter(5, u"Мику. 7ДЛ. У мира есть ты")
        call alt_day5_mi_7dl_morning
    pause(2)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(5, u"Мику. 7ДЛ. День")
    call alt_day5_mi_7dl_dinner
    pause(1)
    call alt_day5_mi_7dl_router
    pause(1)
    if persistent.mi_7dl_good_human or persistent.mi_7dl_good_star:
        call alt_day5_mi_7dl_lost
        pause(1)
        if alt_day5_mi_7dl_voyeur:
            call alt_day5_mi_7dl_hn
        else:
            call alt_day5_mi_7dl_branch
    else:
        call alt_day5_mi_7dl_branch
    pause(2)
    $ alt_chapter(5, u"Мику. 7ДЛ. ДжентльСемён.")
    call alt_day5_mi_7dl_potato
    pause(1)
    if not alt_day5_mi_7dl_voyeur:
        call alt_day5_mi_7dl_camp_cleance
        pause(2)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Мику. 7ДЛ. Костёр")
    call alt_day5_mi_7dl_firecamp
    pause(3)
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day5_mi_7dl_goodnight
    pause(2)
    jump alt_day6_mi_7dl_start

label alt_day6_mi_7dl_start:
    call alt_day6_mi_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Мику. 7ДЛ. Утро")
    call alt_day6_mi_7dl_wakeup
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    if alt_day5_mi_7dl_voyeur:
        call alt_day6_mi_7dl_soul
        pause(1)
        $ alt_chapter(6, u"Мику. 7ДЛ. День")
        call alt_day6_mi_7dl_dinner
        pause(1)
        call alt_day6_mi_7dl_soul_day
        pause(1)
        call alt_day6_mi_7dl_miku_sakishita
        pause(1)
        call alt_day6_mi_7dl_miku_farewell_finale
        pause(1)
        call alt_day6_mi_7dl_miku_farewell_soul
    elif alt_hpt < alt_spt:
        call alt_day6_mi_7dl_star
        pause(1)
        $ alt_chapter(6, u"Мику. 7ДЛ. День")
        call alt_day6_mi_7dl_dinner
        pause(1)
        call alt_day6_mi_7dl_star_day
        pause(1)
        call alt_day6_mi_7dl_miku_sakishita
        call alt_day6_mi_7dl_miku_farewell_finale
        pause(1)
        call alt_day6_mi_7dl_miku_farewell_star
    else:
        call alt_day6_mi_7dl_human
        pause(1)
        call alt_day6_mi_7dl_human_day
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Мику. 7ДЛ. Вечер")
    if alt_day6_mi_7dl_left:
        call alt_day6_mi_7dl_catapult
        pause(1)
        if alt_day_catapult:
            return
    call alt_day6_mi_7dl_discoteque
    pause(1)
    if not alt_day6_mi_7dl_left:
        call alt_day6_mi_7dl_hentai
        pause(1)
    jump alt_day7_mi_7dl_start

label alt_day7_mi_7dl_start:
    if alt_day6_mi_7dl_left:
        if alt_day5_mi_7dl_voyeur:
            $ routetag = "mi7dlcas"
        else:
            if alt_spt > 6 and alt_day5_mi_7dl_kiss:
                $ routetag = "mi7dlcas1"
            elif alt_spt >= 8:
                $ routetag = "mi7dlvoca"
            else:
                $ routetag = "mi7dlvoca1"
    else:
        if lp_mi > 16:
            if alt_hpt >= 9:
                $ routetag = "mi7dldress"
            else:
                $ routetag = "mi7rej"
        else:
            $ routetag = "mi7dlcas2"
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    call alt_day7_mi_7dl_begin
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(7, u"Мику. 7ДЛ. Утро")
    call alt_day7_mi_7dl_wakeup
    pause(1)
    call alt_day7_mi_7dl_packing
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    if alt_day6_mi_7dl_left:
        $ alt_chapter(7, u"Мику. 7ДЛ. Отъезд")
        call alt_day7_mi_7dl_departure_lone
        pause(1)
        $ persistent.sprite_time = "prolog"
        $ prolog_time()
        if alt_day5_mi_7dl_voyeur:
            if loki:
                call alt_day7_mi_7dl_loki_exc
            elif herc:
                call alt_day7_mi_7dl_herc_exc
            else:
                call alt_day7_mi_7dl_dr_exc
        else:
            if alt_spt >= 8:
                call alt_day7_mi_7dl_good_star
            else:
                call alt_day7_mi_7dl_bad_star
        pause(1)
        return
    else:
        $ alt_chapter(7, u"Мику. 7ДЛ. Не отпускай")
        call alt_day7_mi_7dl_departure_a2th
        pause(1)
        $ persistent.sprite_time = "prolog"
        $ prolog_time()
        if alt_day7_mi_7dl_pt == 1:
            if alt_hpt >= 9:
                $ alt_chapter(-1, u"Мику. 7ДЛ. Сны.")
                call alt_day7_mi_7dl_good_human
            else:
                call alt_day7_mi_7dl_neu_human
        elif alt_day7_mi_7dl_pt == 2:
            call alt_day7_mi_7dl_bad_human
        elif alt_day7_mi_7dl_pt == 3:
            call alt_day7_mi_7dl_shard
    pause(1)
    return
