label alt_day4_me_neu_start:
    call alt_day4_me_neu_vars
    call alt_day4_sl_cl_vars
    call alt_day4_un_7dl_vars
    call alt_day4_un_fz_vars
    $ routetag = "neu"
    if (lp_us >= 6) and (lp_us <= 8):
        $ counter_us_7dl += 1
    elif (lp_us >= 9):
        $ counter_us_7dl += 2
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Одиночка. Утро")
    if counter_dv_7dl == 4:
        call alt_day4_me_neu_dv
        pause(1)
    elif (alt_day3_technoquest2) and (alt_day3_dj != 'dv'):
        call alt_day4_me_neu_aid
        pause(1)
        if alt_day3_un_med_help != 0:
            call alt_day4_me_neu_aid_un
            pause(1)
        elif (counter_sl_cl == 7) or (lp_sl >= 13) or ((alt_day3_dancing1 == 'sl_1') and (counter_sl_7dl == 4)):
            call alt_day4_me_neu_aid_sl
            pause(1)
            if alt_day4_me_neu_transit == 'sl_cl':
                $ routetag = "sl"
                jump alt_day4_sl_cl_start
        else:
            call alt_day4_me_neu_aid_generic
            pause(1)
            if alt_day4_me_neu_date == 'mt':
                call alt_day4_me_neu_mt
                pause(1)
            elif alt_day4_me_neu_date == 'us':
                call alt_day4_me_neu_us
                pause(1)
    else:
        call alt_day4_me_neu_home
        pause(1)
        if alt_day3_dj == 'dv' and alt_day3_dancing2 == 'dv_2':
            call alt_day4_me_neu_dv
            pause(1)
        elif alt_day3_us_bugs == 1:
            $ alt_day4_me_neu_date = 'us'
            call alt_day4_me_neu_us
            pause(1)
        elif alt_day3_un_med_help != 0:
            call alt_day4_me_neu_un
            pause(1)
            if alt_day4_me_neu_transit == 'un_7dl':
                $ routetag = "un7dl"
                jump alt_day4_un_7dl_start
        elif (alt_day2_date == 'mi') and (alt_day2_mi_date != 2):
            call alt_day4_me_neu_mi
            pause(1)
        else:
            call alt_day4_me_neu_sl
            pause(1)
            if alt_day4_me_neu_date == 'mt':
                call alt_day4_me_neu_mt
                pause(1)
            elif alt_day4_me_neu_date == 'us':
                call alt_day4_me_neu_us
                pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(4, u"Одиночка. День")
    call alt_day4_me_neu_dinner
    pause(1)
    if alt_day4_me_neu_escape:
        call alt_day4_me_neu_curl
        pause(1)
        if lp_us >= 9:
            call alt_day4_me_neu_day_us
        else:
            call alt_day4_me_neu_day_mt
    else:
        if ('soccer' in list_clubs_7dl) or ('volley' in list_clubs_7dl) or ('badmin' in list_clubs_7dl):
            call alt_day4_me_neu_sport
        elif 'cyber' in list_clubs_7dl:
            call alt_day4_me_neu_cyber
        elif 'nwsppr' in list_clubs_7dl:
            call alt_day4_me_neu_nwsppr
        elif 'music' in list_clubs_7dl:
            call alt_day4_me_neu_music
    pause(1)
    call alt_day4_me_neu_lunch
    pause(1)
    if alt_day4_me_neu_volley:
        call alt_day4_me_neu_volley
    else:
        call alt_day4_me_neu_concert
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Одиночка. Вечер")
    call alt_day4_me_neu_supper
    pause(1)
    if not alt_day4_me_neu_volley:
        call alt_day4_me_neu_reward
        pause(1)
        call alt_day4_me_neu_pirate
        pause(1)
    call alt_day4_me_neu_square
    pause(1)
    call alt_day4_me_neu_map_evening
    pause(1)
    if alt_day4_me_neu_mt_diary:
        call alt_day4_me_neu_mt_diary_vol1
        pause(1)
    elif (alt_day4_me_neu_date == 'us') and (alt_day4_me_neu_us_backpack):
        call alt_day4_me_neu_us_candies
        pause(1)
        call alt_day4_me_neu_us_guards
        pause(1)
        if counter_us_7dl_px == 1:
            $ persistent.sprite_time = "night"
            $ night_time()
            call alt_day4_me_neu_us_launch
            pause(1)
    elif alt_day4_me_neu_mi_songs:
        $ persistent.sprite_time = "night"
        $ night_time()
        call alt_day4_me_neu_songs
        pause(1)
    elif alt_day4_me_neu_dv_help:
        $ persistent.sprite_time = "night"
        $ night_time()
        call alt_day4_me_neu_prank
        pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day4_me_neu_sleeptime
    pause(1)
    jump alt_day5_me_neu_start

label alt_day5_me_neu_start:
    call alt_day5_me_neu_vars
    $ alt_chapter(5, u"Одиночка. Утро")
    if counter_us_7dl_px == 1:
        $ persistent.sprite_time = "night"
        $ night_time()
        call alt_day5_me_neu_morningdream
        pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    call alt_day5_me_neu_begin
    pause(1)
    call alt_day5_me_neu_breakfast
    pause(1)
    call alt_day5_me_neu_rain
    pause(1)
    if alt_day5_me_neu_candle == 1:
        call alt_day5_me_neu_along
        pause(1)
    if alt_day5_me_neu_candle in (1, 2):
        call alt_day5_me_neu_cndl
        pause(1)
        if alt_day5_me_neu_candle_escape:
            call alt_day5_me_neu_cndl_esc
            pause(1)
        elif counter_me_neu_answers >= 1:
            if herc:
                call alt_day5_me_neu_day_answ_h
                pause(1)
            elif loki:
                call alt_day5_me_neu_day_answ_l
                pause(1)
            else:
                call alt_day5_me_neu_day_answ_d
                pause(1)
    elif alt_day5_me_neu_candle == 3:
        call alt_day5_me_neu_gaming
        pause(1)
    elif alt_day5_me_neu_candle == 4:
        call alt_day5_me_neu_arrest
        pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(5, u"Одиночка. Обед")
    call alt_day5_me_neu_dinner
    pause(1)
    if counter_us_7dl_px == 2:
        call alt_day5_me_neu_us_melancholy
        pause(1)
        call alt_day5_me_neu_us_career
        pause(1)
        call alt_day5_me_neu_us_caught
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(5, u"Одиночка. Вечер")
        call alt_day5_me_neu_us_punishment
        pause(1)
        if alt_day5_me_neu_us_stores:
            call alt_day5_me_neu_us_full
            pause(1)
            call alt_day5_me_neu_us_hideandseek
            pause(1)
            $ persistent.sprite_time = "night"
            $ night_time()
            call alt_day5_me_neu_us_warm_evening
            pause(1)
        else:
            call alt_day5_me_neu_us_hungry
            pause(1)
            call alt_day5_me_neu_us_robbery
            pause(1)
            $ persistent.sprite_time = "night"
            $ night_time()
            call alt_day5_me_neu_us_cleaning
            pause(1)
        call alt_day5_me_neu_us_sleeptime
        pause(1)
        if counter_us_7dl_px == 3:
            $ routetag = "us_7dl_px_good"
        else:
            $ counter_us_7dl += 2
            $ routetag = "us_7dl"
        jump alt_day6_us_7dl_start
    else:
        if alt_day5_me_neu_mi_help:
            call alt_day5_me_neu_mi_estrade
            pause(1)
            if alt_day5_me_neu_mt_voyeur == 1:
                call alt_day5_me_neu_mt_beach
            else:
                call alt_day5_me_neu_mi_help
        elif ('soccer' in list_clubs_7dl) or ('volley' in list_clubs_7dl) or ('badmin' in list_clubs_7dl):
            call alt_day5_me_neu_sport_sh
        elif 'cyber' in list_clubs_7dl:
            call alt_day5_me_neu_cyber_sh
        elif 'nwsppr' in list_clubs_7dl:
            call alt_day5_me_neu_nwsppr_sh
        pause(1)
        call alt_day5_me_neu_lunch
        pause(1)
        call alt_day5_me_neu_sl_secret
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(5, u"Одиночка. Вечер")
        call alt_day5_me_neu_supper
        pause(1)
        call alt_day5_me_neu_evening
        pause(1)
        $ alt_chapter(5, u"Одиночка. Костёр")
        call alt_day5_me_neu_campfire
        pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        if alt_day5_me_neu_campfire_choise == 1:
            call alt_day5_me_neu_map_evening
            if alt_day5_me_neu_map_points >= 3:
                call alt_day5_me_neu_map_fail
            pause(1)
            if alt_day5_me_neu_map_ivent == 'boat':
                call alt_day5_me_neu_sleeptime_wet
            elif alt_day5_me_neu_map_ivent == 'medic':
                call alt_day5_me_neu_sleeptime_drunk
            else:
                call alt_day5_me_neu_sleeptime_map
            jump alt_day6_me_neu_start
        elif alt_day5_me_neu_campfire_choise == 2:
            if herc:
                call alt_day5_me_neu_evening_answ_h
                pause(1)
                call alt_day5_me_neu_sleeptime_answ_h
            elif loki:
                call alt_day5_me_neu_evening_answ_l
            else:
                call alt_day5_me_neu_evening_answ_d
                pause(1)
                call alt_day5_me_neu_sleeptime_answ_d
            pause(1)
            jump alt_day7_me_neu_start
        elif alt_day5_me_neu_campfire_choise == 3:
            call alt_day5_me_neu_sleeptime
            if (counter_mt_7dl >= 7) and (alt_day5_me_neu_mt_voyeur != 0):
                $ routetag = "mt7dl"
                if alt_day5_me_neu_mt_diary:
                    call alt_day5_me_neu_mt_retrib
                elif alt_day5_me_neu_mt_hentai:
                    call alt_day5_me_neu_mt_tea_party
                jump alt_day6_mt_7dl_start
            elif (counter_us_7dl >= 6):
                $ routetag = "us_7dl"
                jump alt_day6_us_7dl_start
            else:
                jump alt_day6_me_neu_start

label alt_day6_me_neu_start:
    call alt_day6_me_neu_vars
    $ routetag = "neu_main"
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    if alt_day5_me_neu_map_ivent == 'boat':
        $ alt_chapter(6, u"Одиночка. Пробуждение.")
        call alt_day6_me_neu_begin_duty
    else:
        if alt_day5_me_neu_map_ivent == 'medic':
            $ alt_chapter(6, u"Одиночка. Пьяный-помятый")
        else:
            $ alt_chapter(6, u"Одиночка. Пробуждение")
        call alt_day6_me_neu_begin
    $ alt_save_name(6, u"Одиночка. Завтрак")
    $ persistent.sprite_time = "day"
    $ day_time()
    if alt_day5_me_neu_map_ivent == 'dv':
        call alt_day6_me_neu_breakfast_dv
    else:
        call alt_day6_me_neu_breakfast
        if alt_day5_me_neu_map_ivent == 'boat':
            call alt_day6_me_neu_breakfast_duty
    if not (alt_day6_me_neu_dv_revenge or alt_day6_me_neu_mt_help or alt_day5_me_neu_cs_debt2):
        call alt_day6_me_neu_after_breakfast
        if alt_day6_me_neu_walk:
            $ alt_save_name(6, u"Одиночка. Двадцать тысяч лье под водой")
            call alt_day6_me_neu_beach
        elif ('soccer' in list_clubs_7dl) or ('volley' in list_clubs_7dl) or ('badmin' in list_clubs_7dl):
            $ alt_save_name(6, u"Одиночка. День физкультурника")
            call alt_day6_me_neu_sport
        elif 'cyber' in list_clubs_7dl:
            $ alt_save_name(6, u"Одиночка. Приключения Электроника")
            call alt_day6_me_neu_cyber
        elif ('nwsppr' in list_clubs_7dl and counter_mz_7dl != 2):
            $ alt_save_name(6, u"Одиночка. Дни минувшего прошлого")
            call alt_day6_me_neu_nwsppr
        elif ('nwsppr' in list_clubs_7dl and counter_mz_7dl == 2):
            $ alt_save_name(6, u"Одиночка. В глубине души твоей")
            call alt_day6_me_neu_nwsppr_mz
        elif 'music' in list_clubs_7dl:
            $ alt_save_name(6, u"Одиночка. Музыкальная пауза")
            call alt_day6_me_neu_music
    else:
        if alt_day6_me_neu_dv_revenge:
            $ alt_save_name(6, u"Одиночка. Месть Алисы")
            call alt_day6_me_neu_dv_revenge
        elif alt_day6_me_neu_mt_help:
            $ alt_save_name(6, u"Одиночка. Рандеву с вожатой")
            call alt_day6_me_neu_mt_help
        elif alt_day5_me_neu_cs_debt2:
            $ alt_save_name(6, u"Одиночка. Вопрос с подвохом")
            call alt_day6_me_neu_viola_duty
            pause(1)
            $ alt_save_name(6, u"Одиночка. Двадцать тысяч лье под водой")
            call alt_day6_me_neu_beach
    pause(1)
    $ alt_chapter(6, u"Одиночка. Обед")
    if alt_day5_me_neu_map_ivent == 'boat':
        call alt_day6_me_neu_duty
        pause(1)
    call alt_day6_me_neu_lunch
    pause(1)
    $ alt_save_name(6, u"Одиночка. Тихий час")
    call alt_day6_me_neu_map_sh
    pause(1)
    if alt_day6_me_neu_dance_invite == 'mt':
        call alt_day6_me_neu_mt_invite
    pause(1)
    call alt_day6_me_neu_afternoon
    pause(1)
    $ alt_save_name(6, u"Одиночка. Концерт")
    call alt_day6_me_neu_concert
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    if alt_day6_me_neu_un_escape:
        $ alt_save_name(6, u"Одиночка. Побег")
        call alt_day6_me_neu_un_escape
    else:
        $ alt_save_name(6, u"Одиночка. Инспекция")
        call alt_day6_me_neu_inspection
    pause(1)
    $ alt_save_name(6, u"Одиночка. Ужин")
    call alt_day6_me_neu_dinner
    pause(1)
    $ alt_save_name(6, u"Одиночка. Перед дискотекой")
    call alt_day6_me_after_dinner
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()

    if alt_day6_me_neu_dance_invite == 'dv':
        $ alt_save_name(6, u"Одиночка. У тебя бы и не вышло…")
        call alt_day6_me_neu_dv_dance
    else:
        $ alt_chapter(6, u"Одиночка. Дискотека")
        call alt_day6_me_neu_dance
        if alt_day6_me_neu_dance_invite == 'mi':
            $ alt_save_name(6, u"Одиночка. Танец с Мику")
            call alt_day6_me_neu_mi_dance
        elif alt_day6_me_neu_dance_invite == 'sl':
            $ alt_save_name(6, u"Одиночка. Хороший Пират -")
            call alt_day6_me_neu_sl_dance
        elif alt_day6_me_neu_dance_invite == 'un':
            $ alt_save_name(6, u"Одиночка. ЧП")
            call alt_day6_me_neu_un_dance
        elif alt_day6_me_neu_dance_invite == 'us':
            $ alt_save_name(6, u"Одиночка. Танец с Ульяной")
            call alt_day6_me_neu_us_danсe
        elif counter_mz_7dl == 3:
            $ alt_save_name(6, u"Одиночка. Танец с Женей")
            call alt_day6_me_neu_mz_danсe
        elif counter_mt_7dl >= 5:
            $ alt_save_name(6, u"Одиночка. Сбежавшая невеста")
            call alt_day6_me_neu_mt_dance
        elif alt_day4_me_neu_us_debt and alt_day5_me_neu_clubs_cyber and alt_day6_me_neu_clubs_cyber:
            $ alt_save_name(6, u"Одиночка. Рыбный день")
            call alt_day6_me_neu_el_dance
        else:
            $ alt_save_name(6, u"Одиночка. Джон Тайтор")
            call alt_day6_me_neu_ka_danсe
    pause(1)
    if alt_day6_me_neu_dance_invite == 'un':
        $ alt_save_name(6, u"Одиночка. Отмена свечки")
        call alt_day6_me_neu_no_candle
    else:
        $ alt_save_name(6, u"Одиночка. Свечка")
        call alt_day6_me_neu_candle
        pause(1)
        $ alt_save_name(6, u"Одиночка. Отбой")
        call alt_day6_me_neu_sleeptime
    pause(1)
    jump alt_day7_me_neu_start

label alt_day7_me_neu_start:
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    $ alt_chapter(-1, u"Одиночка. Обречённое")
    scene black
    show screen alt_me_neu_wip
    call alt_day7_me_neu_bad
    pause(1)
    return

screen alt_me_neu_wip:
    modal True
    add get_image("gui/o_rly/base.png")
    text "Продолжение находится в разработке. А пока что можете прочитать преждевременный «финал»-заглушку":
        text_align 0.5
        yalign 0.46
        xalign 0.5
        xmaximum 880
        color "#64483c"
        font header_font
        size 40
    textbutton _("OK"):
        text_size 60
        style "log_button"
        text_style "settings_link"
        yalign 0.6
        xalign 0.5
        action Hide("alt_me_neu_wip")
