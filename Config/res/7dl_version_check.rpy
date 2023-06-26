init python:
    def sdl_after_load():
        renpy.call("alt_after_load")

init:
    # Номер релиза сохранения, пустой по инициализации, в начале игры - присваивается номер релиза мода,
    # при загрузке:
    #  - если было сохранение с присвоением номера, при загрузке переменная будет взята из сохранения;
    #  - если загружается "старое" сохранение (до ввода процедуры контроля загрузок) - останется None
    $ alt_save_release_no = None
    $ alt_save_fixed = False
    $ alt_aicr_string = " "
    $ vars_040_saved = False
    $ vars_0401_saved = False
    $ vars_0402_saved = False
    $ vars_043_saved = False
    $ vars_049_saved = False

    $ config.after_load_callbacks.append(sdl_after_load)

init 1: # Переименования персистентов
    if not persistent.not_first_start_7dl:
        $ persistent.not_first_start_7dl = True
        if persistent.dv_7dl_good_ussr_rf:
            $ persistent.dv_7dl_good_rf = True
        if persistent.un_7dl_true:
            $ persistent.un_7dl_rej = True
            $ persistent.un_7dl_true = False

    if not persistent.not_first_start2_7dl:
        $ persistent.not_first_start2_7dl = True
        if persistent.mi_7dl_ps:
            $ persistent.mi_7dl_sept = persistent.mi_7dl_ps
            $ persistent.mi_7dl_ps = False
        if persistent.mi_7dl_neutral_human:
            $ persistent.mi_7dl_neu_human = persistent.mi_7dl_neutral_human
            $ persistent.mi_7dl_neutral_human = False
        if persistent.dv_7dl_true:
            $ persistent.dv_7dl_sept = persistent.dv_7dl_true
            $ persistent.dv_7dl_true = False
        if persistent.dv_7dl_reject_ussr:
            $ persistent.dv_7dl_rej_ussr = persistent.dv_7dl_reject_ussr
            $ persistent.dv_7dl_reject_ussr = False
        if persistent.dv_7dl_reject_rf:
            $ persistent.dv_7dl_rej_rf = persistent.dv_7dl_reject_rf
            $ persistent.dv_7dl_reject_rf = False
        if persistent.dv_7dl_bad_mt:
            $ persistent.dv_7dl_tran_mt = persistent.dv_7dl_bad_mt
            $ persistent.dv_7dl_bad_mt = False
        if persistent.dv_7dl_un:
            $ persistent.dv_7dl_tran_un = persistent.dv_7dl_un
            $ persistent.dv_7dl_un = False
        if persistent.dv_7dl_tulpa:
            $ persistent.dv_7dl_loki_exc = persistent.dv_7dl_tulpa
            $ persistent.dv_7dl_tulpa = False
        if persistent.sl_7dl_true:
            $ persistent.sl_7dl_sept = persistent.sl_7dl_true
            $ persistent.sl_7dl_true = False
        if persistent.sl_7dl_herc_good:
            $ persistent.sl_7dl_herc_neu = persistent.sl_7dl_herc_good
            $ persistent.sl_7dl_herc_good = False
        if persistent.sl_7dl_herc_good2:
            $ persistent.sl_7dl_herc_good = persistent.sl_7dl_herc_good2
            $ persistent.sl_7dl_herc_good2 = False
        if persistent.sl_7dl_good:
            $ persistent.sl_7dl_dr_good = persistent.sl_7dl_good
            $ persistent.sl_7dl_good = False
        if persistent.sl_7dl_good2:
            $ persistent.sl_7dl_dr_good2 = persistent.sl_7dl_good2
            $ persistent.sl_7dl_good2 = False
        if persistent.sl_cl_int_ok:
            $ persistent.sl_cl_int_true = persistent.sl_cl_int_ok
            $ persistent.sl_cl_int_ok = False
        if persistent.sl_cl_reject_same:
            $ persistent.sl_cl_rej_rf = persistent.sl_cl_reject_same
            $ persistent.sl_cl_reject_same = False
        if persistent.sl_cl_reject_late:
            $ persistent.sl_cl_rej = persistent.sl_cl_reject_late
            $ persistent.sl_cl_reject_late = False
        if persistent.sl_cl_cata:
            $ persistent.sl_cl_loki_exc = persistent.sl_cl_cata
            $ persistent.sl_cl_cata = False
        if persistent.un_7dl_true:
            $ persistent.un_7dl_sept = persistent.un_7dl_true
            $ persistent.un_7dl_true = False
        if persistent.un_7dl_true_transit:
            $ persistent.un_7dl_true_tran = persistent.un_7dl_true_transit
            $ persistent.un_7dl_true_transit = False
        if persistent.mt_7dl_neutral:
            $ persistent.mt_7dl_neu = persistent.mt_7dl_neutral
            $ persistent.mt_7dl_neutral = False
        if persistent.us_7dl_un:
            $ persistent.us_7dl_tran_un = persistent.us_7dl_un
            $ persistent.us_7dl_un = False
        if persistent.us_7dl_mi:
            $ persistent.us_7dl_tran_mi = persistent.us_7dl_mi
            $ persistent.us_7dl_mi = False
        if persistent.us_px_true:
            $ persistent.us_px_sept = persistent.us_px_true
            $ persistent.us_px_true = False
        if persistent.us_px_rf_good:
            $ persistent.us_px_good = persistent.us_px_rf_good
            $ persistent.us_px_rf_good = False
        if persistent.neu_true:
            $ persistent.me_neu_true = persistent.neu_true
            $ persistent.neu_true = False
        if persistent.neu_loki_neu:
            $ persistent.me_neu_loki_neu = persistent.neu_loki_neu
            $ persistent.neu_loki_neu = False
        if persistent.neu_neu:
            $ persistent.me_neu_dr_neu = persistent.neu_neu
            $ persistent.neu_neu = False
        if persistent.neu_bad:
            $ persistent.me_neu_bad = persistent.neu_bad
            $ persistent.neu_bad = False

    if not persistent.not_first_start3_7dl:
        python:
            persistent.not_first_start3_7dl = True
            if persistent.filters:
                for i in persistent.filters:
                    try:
                        if (i['id'] == "widget__7dl_widget") or (i['id'] == "music_widget_7dl"):
                            persistent.filters.remove(i)
                    except Exception:
                        pass

    if not persistent.not_first_start4_7dl:
        $ persistent.not_first_start4_7dl = True
        if persistent.mi_7dl_true:
            $ persistent.mi_7dl_int_reject = persistent.mi_7dl_true
            $ persistent.mi_7dl_true = False

    if not persistent.not_first_start5_7dl:
        $ persistent.not_first_start5_7dl = True
        if persistent.dv_7dl_tran_mt:
            $ persistent.alt_drunk = persistent.dv_7dl_tran_mt
            $ persistent.dv_7dl_tran_mt = False
        if persistent.us_px_true:
            $ persistent.us_7dl_px_true = persistent.us_px_true
            $ persistent.us_px_true = False
        if persistent.us_px_good:
            $ persistent.us_7dl_px_good = persistent.us_px_good
            $ persistent.us_px_good = False
            
    if not persistent.not_first_start6_7dl:
        $ persistent.not_first_start6_7dl = True
        $ persistent.achv_sprite_emo_7dl = True

# Старый экран. Показывается в доисторических сейвах
screen alt_incompatible_release:
    tag menu
    modal True
    python: # почти цельностянуто из "menu:" в игре, цвета меняются со временем дня игры

        aicr_colors_hover = {'day': '#9dcd55', 'night': '#3ccfa2', 'sunset': '#dcd168', 'prologue': '#98d8da'}
        aicr_colors = {'day': '#466123', 'night': '#145644', 'sunset': '#69652f', 'prologue': '#496463'}

    window:
        text alt_aicr_string align (0.5, 0.05) color "#FF2500" font 'fonts/corbel.ttf' size 60 bold True text_align 0.5 line_spacing 20
        text u"РАБОТОСПОСОБНОСТЬ НЕ ГАРАНТИРУЕТСЯ. ВЫЛЕТ ИГРЫ ВОЗМОЖЕН В ЛЮБОЙ МОМЕНТ" align(0.5, 0.25) color "#FF2500" font 'fonts/corbel.ttf' size 60 bold True text_align 0.5 line_spacing 20
        text u"РЕКОМЕНДУЕТСЯ НАЧАТЬ ИГРУ ЗАНОВО"  align(0.5, 0.45) color aicr_colors_hover[persistent.timeofday] font 'fonts/corbel.ttf' size 60 bold True text_align 0.5 line_spacing 20
        text u"Ваши действия:"  align(0.5, 0.55) color aicr_colors_hover[persistent.timeofday] font 'fonts/corbel.ttf' size 55 bold True text_align 0.5 line_spacing 20

        right_padding 75
        bottom_padding 50
        yalign 0.5
        top_padding 50
        xfill True
        background (Frame(get_image((('gui/choice/' + persistent.timeofday) + '/choice_box.png')), 50, 50))
        left_padding 75
# кнопки выборов
        button: # начинаем заново
            xalign 0.5
            yalign 0.65
            action Jump("start_7dl")
            background None
            text u"Начать игру заново":
                hover_size 50
                color aicr_colors[persistent.timeofday]
                xcenter 0.5
                hover_color aicr_colors_hover[persistent.timeofday]
                font 'fonts/corbel.ttf'
                size 50
        button: # выходим в меню загрузки, ищем что-то другое
            xalign 0.5
            yalign 0.75
            action ShowMenu('load')
            background None
            text u"Загрузить другое сохранение":
                hover_size 50
                color aicr_colors[persistent.timeofday]
                xcenter 0.5
                hover_color aicr_colors_hover[persistent.timeofday]
                font 'fonts/corbel.ttf'
                size 50
# Для особо упёртых\упорных\…. Пробуем продолжить, авось получится.
# Продолжение игры номер сохранения не перепишет; так что окно проверки будет вываливаться каждый раз
        button:
            xalign 0.5
            yalign 0.85
            action Return() # возвращаемся в игру
            background None
            text u"Загрузить это сохранение. На свой страх и риск, о возможных последствиях предупрежден.":
                hover_size 40
                color aicr_colors[persistent.timeofday]
                xcenter 0.5
                hover_color aicr_colors_hover[persistent.timeofday]
                font 'fonts/corbel.ttf'
                size 40

# Новый экран с возможностью вернуться в начало игрового дня
screen alt_load_warning:
    tag menu
    modal True
    python: # почти цельностянуто из "menu:" в игре, цвета меняются со временем дня игры

        aicr_colors_hover = {'day': '#9dcd55', 'night': '#3ccfa2', 'sunset': '#dcd168', 'prologue': '#98d8da'}
        aicr_colors = {'day': '#466123', 'night': '#145644', 'sunset': '#69652f', 'prologue': '#496463'}

    window:
        text alt_aicr_string align (0.5, 0.05) color aicr_colors_hover[persistent.timeofday] font 'fonts/corbel.ttf' size 60 bold True text_align 0.5 line_spacing 20
        text u"ЕСЛИ В ПРОЦЕССЕ ДАЛЬНЕЙШЕГО ПРОХОЖДЕНИЯ ВЫ СТОЛКНЁТЕСЬ С ОШИБКАМИ, ЗАГРУЗИТЕ ЭТО СОХРАНЕНИЕ И ВЫБЕРИТЕ «ВЕРНУТЬСЯ НА НАЧАЛО ДНЯ»\n\n" align(0.5, 0.45) color aicr_colors_hover[persistent.timeofday] font 'fonts/corbel.ttf' size 40 bold True text_align 0.5 line_spacing 20

        right_padding 75
        bottom_padding 50
        yalign 0.5
        top_padding 50
        xfill True
        background (Frame(get_image((('gui/choice/' + persistent.timeofday) + '/choice_box.png')), 50, 50))
        left_padding 75
        button: # продолжаем игру
            xalign 0.5
            yalign 0.85
            action [Hide("alt_load_warning"), Return()]
            background None
            text u"Загрузить это сохранение":
                hover_size 50
                color aicr_colors[persistent.timeofday]
                xcenter 0.5
                hover_color aicr_colors_hover[persistent.timeofday]
                font 'fonts/corbel.ttf'
                size 50
        button: # выходим в меню загрузки, ищем что-то другое
            xalign 0.5
            yalign 0.75
            action ShowMenu('load')
            background None
            text u"Загрузить другое сохранение":
                hover_size 50
                color aicr_colors[persistent.timeofday]
                xcenter 0.5
                hover_color aicr_colors_hover[persistent.timeofday]
                font 'fonts/corbel.ttf'
                size 50
        button: # начинаем с начала дня
            xalign 0.5
            yalign 0.65
            if (alt_save_release_no in ["0.42", "0.43"]) and counter_un_cl:
                action Jump("alt_day3_un_cl_start")
            elif routetag == "prologue":
                if "пролог" in save_name:
                    action Jump("start_7dl")
                elif "День 1 — ОТКАТ" in save_name:
                    action Jump("alt_day1_me_d3_start")
                elif "День 2 — ОТКАТ" in save_name:
                    action Jump("alt_day2_me_d3_start")
                elif "День 1" in save_name:
                    action Jump("alt_day1_start")
                elif "День 2" in save_name:
                    action Jump("alt_day2_start")
                elif "День 3" in save_name:
                    action Jump("alt_day3_start")
                elif "День 4" in save_name:
                    action Jump("alt_day4_me_neu_start")
                elif "День 5" in save_name:
                    action Jump("alt_day5_me_neu_start")
                elif "День 6" in save_name:
                    action Jump("alt_day6_me_neu_start")
                elif "День 7" in save_name:
                    action Jump("alt_day7_me_neu_start")
            elif "dv7dl" in routetag:
                if "День 4" in save_name:
                    action Jump("alt_day4_dv_7dl_start")
                elif "День 5" in save_name:
                    action Jump("alt_day5_dv_7dl_start")
                elif "День 6" in save_name:
                    action Jump("alt_day6_dv_7dl_start")
                elif "День 7" in save_name:
                    action Jump("alt_day7_dv_7dl_start")
            elif routetag == "Noir":
                action Jump("alt_day4_no_start")
            elif ("mi7" in routetag) and (alt_day3_dj == "mi"):
                if "День 4" in save_name:
                    action Jump("alt_day4_mi_dj_start")
                elif "День 5" in save_name:
                    action Jump("alt_day5_mi_dj_start")
                elif "День 6" in save_name:
                    action Jump("alt_day6_mi_dj_start")
                elif "День 7" in save_name:
                    action Jump("alt_day7_mi_dj_start")
            elif "mi7" in routetag:
                if "День 4" in save_name:
                    action Jump("alt_day4_mi_7dl_start")
                elif "День 5" in save_name:
                    action Jump("alt_day5_mi_7dl_start")
                elif "День 6" in save_name:
                    action Jump("alt_day6_mi_7dl_start")
                elif "День 7" in save_name:
                    action Jump("alt_day7_mi_7dl_start")
            elif "mt7dl" in routetag:
                if "День 6" in save_name:
                    action Jump("alt_day6_mt_7dl_start")
                elif "День 7" in save_name:
                    action Jump("alt_day7_mt_7dl_start")
            elif "sl7dl" in routetag:
                if "День 4" in save_name:
                    action Jump("alt_day4_sl_7dl_start")
                elif "День 5" in save_name:
                    action Jump("alt_day5_sl_7dl_start")
                elif "День 6" in save_name:
                    action Jump("alt_day6_sl_7dl_start")
                elif "День 7" in save_name:
                    action Jump("alt_day7_sl_7dl_start")
            elif "sl" in routetag:
                if "День 4" in save_name:
                    action Jump("alt_day4_sl_cl_start")
                elif "День 5" in save_name:
                    action Jump("alt_day5_sl_cl_start")
                elif "День 6" in save_name:
                    action Jump("alt_day6_sl_cl_start")
                elif "День 7" in save_name:
                    action Jump("alt_day7_sl_cl_start")
            elif (alt_day2_date == 'un_fz') and (alt_day3_dancing1 == 'un_fz') and (routetag == "un7dl"):
                if "День 4" in save_name:
                    action Jump("alt_day4_un_fz_start")
                elif "День 5" in save_name:
                    action Jump("alt_day5_un_fz_start")
            elif ("un7dl" in routetag) or (routetag == "un"):
                if "День 4" in save_name:
                    action Jump("alt_day4_un_7dl_start")
                elif "День 5" in save_name:
                    action Jump("alt_day5_un_7dl_start")
                elif "День 6" in save_name:
                    action Jump("alt_day6_un_7dl_start")
                elif "День 7" in save_name:
                    action Jump("alt_day7_un_7dl_start")
            elif ("us_7dl" in routetag) or ("us_px" in routetag):
                if "День 6" in save_name:
                    action Jump("alt_day6_us_7dl_start")
                elif "День 7" in save_name:
                    action Jump("alt_day7_us_7dl_start")
            else:
                action Jump("start_7dl")
            background None
            text u"Вернуться на начало дня":
                hover_size 50
                color aicr_colors[persistent.timeofday]
                xcenter 0.5
                hover_color aicr_colors_hover[persistent.timeofday]
                font 'fonts/corbel.ttf'
                size 50

# После загрузки файла переходим именно в это место.
label alt_after_load:
    # читаем 'save_name' и ищем в строке "7ДЛ" - думаю, этого для идентификации мода достаточно
    if save_name.find(u'7ДЛ') != -1: # Если нашли вхождение '7ДЛ' в имени сохранения игры

        # загружаем имена персонажей
        $ save_names_known()

        # меняем тильды на кавычки, если указано в настройках
        if not persistent.thoughts_tilde_7dl:
            $ th_prefix = "«"
            $ th_suffix = "»"
        else:
            $ th_prefix = "~ "
            $ th_suffix = " ~"

        $ reload_names()

        # если загружаем сейв с Нуара - включаем нуарный интерфейс; иначе если нуарный интерфейс был, но больше не нужен - отключаем
        if noir_interface: # если загружаем сейв с Нуара - включаем нуарный интерфейс
            $ noir_interface_on()
        else:
            if persistent.noir_interface:
                $ noir_interface_off() # если нуарный интерфейс был, но больше не нужен - отключаем
            $ alt_interface_on() # если сейв не с Нуара - включаем обычный интерфейс 7дл

        # режим окон - автоматический
        window auto

        # Переносим старые переменные
        if (alt_save_release_no in ["0.34.a", "0.34.b", "0.35.a", "0.36.a", "0.37.a", "0.38.a", "0.39.a", "0.40"]) and (not vars_040_saved):
            $ vars_040_saved = True
            python:
                # Спасаем сейвы Дрища
                try:
                    if not (loki or herc or d3):
                        dr = True
                except Exception:
                    pass
                # Спасаем данные в списках
                try:
                    if (len(list_joined_clubs_7dl) == 0) and (len(list_clubs_7dl) > 0):
                        list_joined_clubs_7dl = list_clubs_7dl
                except Exception:
                    pass
                try:
                    if not alt_day2_convoy:
                        alt_day2_convoy = list_d2_convoy_7dl[0]
                except Exception:
                    pass
                try:
                    if not alt_day2_date:
                        alt_day2_date = list_d2_date_7dl[0]
                except Exception:
                    pass
        if (alt_save_release_no in ["0.34.a", "0.34.b", "0.35.a", "0.36.a", "0.37.a", "0.38.a", "0.39.a", "0.40", "0.40.1"]) and (not vars_0401_saved):
            $ vars_0401_saved = True
            python:
                # Новая переменная
                try:
                    if (alt_day2_convoy == 'un_rej'):
                        alt_day2_un_rej_convoy = True
                except Exception:
                    pass
        if (alt_save_release_no in ["0.34.a", "0.34.b", "0.35.a", "0.36.a", "0.37.a", "0.38.a", "0.39.a", "0.40", "0.40.1", "0.40.2"]) and (not vars_0402_saved):
            $ vars_0402_saved = True
            python:
                # Новые переменные
                try:
                    if alt_day1_cofront_sl_dv == 2:
                        alt_day1_cofront_sl_dv = 1
                except Exception:
                    pass
                try:
                    if alt_day1_cofront_sl_dv == 3:
                        alt_day1_cofront_sl_dv = 2
                except Exception:
                    pass
                try:
                    if alt_day1_un_ignored:
                        alt_day1_un = 0
                except Exception:
                    pass
                try:
                    if alt_day1_un_stopped:
                        alt_day1_un = 2
                except Exception:
                    pass
                try:
                    if alt_day1_un_camp:
                        alt_day1_un = 3
                except Exception:
                    pass
                try:
                    if alt_day1_un_dated:
                        alt_day1_un = 4
                except Exception:
                    pass
                try:
                    if alt_day2_bf_dv_us:
                        alt_day2_bf = 'dv_us'
                except Exception:
                    pass
                try:
                    if alt_day2_bf_un:
                        alt_day2_bf = 'un'
                except Exception:
                    pass
                try:
                    if alt_day2_sl_bf:
                        alt_day2_bf = 'sl'
                except Exception:
                    pass
                try:
                    if alt_day2_loki_minijack:
                        alt_day2_minijack = True
                except Exception:
                    pass
                try:
                    if alt_day2_dv_bet_approve:
                        alt_day2_dv_ultim = 1
                except Exception:
                    pass
                try:
                    if alt_day2_dv_harass:
                        alt_day2_dv_ultim = 2
                except Exception:
                    pass
                try:
                    if alt_day2_slot_us_cake:
                        alt_day2_us_cake = 1
                except Exception:
                    pass
                try:
                    if alt_day2_sup == 1:
                        alt_day2_us_cake = 1
                except Exception:
                    pass
                try:
                    if alt_day2_olga_help:
                        alt_day2_mt_help = True
                except Exception:
                    pass
                try:
                    if alt_day3_us_shenan:
                        alt_day2_us_shenan = True
                except Exception:
                    pass
                try:
                    if alt_day2_mi_rejected:
                        alt_day2_mi_date = 2
                except Exception:
                    pass
                try:
                    if alt_day2_mi_hyst:
                        alt_day2_mi_date = 3
                except Exception:
                    pass
                try:
                    if alt_day3_dv_event:
                        alt_day3_date = 'dv'
                        counter_dv_7dl = 1
                except Exception:
                    pass
                try:
                    if alt_day3_mi_event:
                        alt_day3_date = 'mi'
                except Exception:
                    pass
                try:
                    if alt_day3_un_event:
                        alt_day3_date = 'un'
                except Exception:
                    pass
                try:
                    if counter_sl_cl == 2:
                        alt_day3_date = 'sl'
                except Exception:
                    pass
                try:
                    if alt_day3_technoquest_st1:
                        alt_day3_technoquest1 = 1
                except Exception:
                    pass
                try:
                    if alt_day3_technoquest_st2:
                        alt_day3_technoquest1 = 2
                except Exception:
                    pass
                try:
                    if alt_day3_technoquest_st3_help:
                        alt_day3_technoquest2 = True
                except Exception:
                    pass
                try:
                    if alt_day3_dv_rep:
                        counter_dv_7dl = 3
                except Exception:
                    pass
                try:
                    if alt_day3_dv_evening:
                        counter_dv_7dl = 4
                except Exception:
                    pass
                try:
                    if alt_day3_dv2_event:
                        alt_day3_dv_guitar = 2
                except Exception:
                    pass
                try:
                    if alt_day3_dv_guitar_lesson:
                        alt_day3_dv_guitar = 3
                except Exception:
                    pass
                try:
                    if alt_day3_un_fz_dinner:
                        counter_un_fz_un_route = 2
                except Exception:
                    pass
                try:
                    if alt_day3_un_fz_evening:
                        counter_un_fz_un_route = 4
                except Exception:
                    pass
                try:
                    if alt_day3_mi_invite:
                        counter_mi_7dl = 1
                except Exception:
                    pass
                try:
                    if alt_day3_mi_invite2:
                        counter_mi_7dl = 2
                except Exception:
                    pass
                try:
                    if alt_day3_mi_date:
                        counter_mi_7dl = 2
                except Exception:
                    pass
                try:
                    if alt_day3_un_invite == 1:
                        counter_un_7dl = 4
                except Exception:
                    pass
                try:
                    if alt_day3_un_invite == 2:
                        counter_un_7dl = 5
                except Exception:
                    pass
                try:
                    if alt_day3_un_date:
                        counter_un_7dl = 5
                except Exception:
                    pass
                try:
                    if alt_day3_un_med_help == 1:
                        counter_un_7dl = 6
                except Exception:
                    pass
                try:
                    if alt_day3_dv_dj:
                        alt_day3_dj = 'dv'
                except Exception:
                    pass
                try:
                    if alt_day3_mi_dj:
                        alt_day3_dj = 'mi'
                except Exception:
                    pass
                try:
                    if alt_day3_dancing == 0:
                        alt_day3_dancing1 = 'me_1'
                except Exception:
                    pass
                try:
                    if alt_day3_dancing == 1:
                        alt_day3_dancing1 = 'un_1'
                except Exception:
                    pass
                try:
                    if alt_day3_dancing == 2:
                        alt_day3_dancing1 = 'sl_1'
                except Exception:
                    pass
                try:
                    if alt_day3_dancing == 3:
                        alt_day3_dancing1 = 'dv_1'
                except Exception:
                    pass
                try:
                    if alt_day3_dancing == 4:
                        alt_day3_dancing1 = 'mi_1'
                except Exception:
                    pass
                try:
                    if alt_day3_dancing == 132:
                        alt_day3_dancing1 = 'un_fz'
                except Exception:
                    pass
                try:
                    if alt_day3_dancing == 5:
                        alt_day3_dancing2 = 'me_2'
                except Exception:
                    pass
                try:
                    if alt_day3_dancing == 10:
                        alt_day3_dancing2 = 'un_2'
                except Exception:
                    pass
                try:
                    if alt_day3_dancing == 11:
                        alt_day3_dancing2 = 'un_12'
                except Exception:
                    pass
                try:
                    if alt_day3_dancing == 12:
                        alt_day3_dancing2 = 'un_0'
                except Exception:
                    pass
                try:
                    if alt_day3_dancing == 20:
                        alt_day3_dancing2 = 'sl_2'
                except Exception:
                    pass
                try:
                    if alt_day3_dancing == 21:
                        alt_day3_dancing2 = 'sl_12'
                except Exception:
                    pass
                try:
                    if alt_day3_dancing == 30:
                        alt_day3_dancing2 = 'dv_2'
                except Exception:
                    pass
                try:
                    if alt_day3_dancing == 31:
                        alt_day3_dancing2 = 'dv_12'
                except Exception:
                    pass
                try:
                    if alt_day3_dancing == 32:
                        alt_day3_dancing2 = 'dv_0'
                except Exception:
                    pass
                try:
                    if alt_day3_dancing == 40:
                        alt_day3_dancing2 = 'mi_2'
                except Exception:
                    pass
                try:
                    if alt_day3_dancing == 41:
                        alt_day3_dancing2 = 'mi_12'
                except Exception:
                    pass
                try:
                    if alt_day3_mi_donor:
                        alt_day3_mi_7dl_donor = 1
                except Exception:
                    pass
                try:
                    if alt_day4_mi_7dl_donor:
                        alt_day3_mi_7dl_donor = 2
                except Exception:
                    pass
                try:
                    if alt_day5_mi_dj_musclub_visited:
                        list_mi_search_7dl.append('musclub')
                except Exception:
                    pass
                try:
                    if alt_day5_mi_dj_entrance_visited:
                        list_mi_search_7dl.append('entrance')
                except Exception:
                    pass
                try:
                    if alt_day5_mi_dj_estrade_visited:
                        list_mi_search_7dl.append('estrade')
                except Exception:
                    pass
                try:
                    if alt_day5_mi_dj_home_visited:
                        list_mi_search_7dl.append('home')
                except Exception:
                    pass
                try:
                    if alt_day5_mi_dj_favorite_song:
                        alt_day5_mi_dj_apology = 1
                except Exception:
                    pass
                try:
                    if alt_day5_mi_dj_cut:
                        alt_day5_mi_dj_apology = 2
                except Exception:
                    pass
                try:
                    if alt_day5_mi_dj_forgive:
                        alt_day5_mi_dj_apology = 3
                except Exception:
                    pass
                try:
                    if alt_day5_mi_dj_hentai:
                        alt_day5_mi_dj_hentai_done = True
                except Exception:
                    pass
                try:
                    if alt_day6_mi_dj_letmestay:
                        alt_day6_mi_dj_catapult = 1
                except Exception:
                    pass
                try:
                    if alt_day6_mi_dj_letmeout:
                        alt_day6_mi_dj_catapult = 2
                except Exception:
                    pass
                try:
                    if alt_day6_mi_dj_sl_feed:
                        alt_day6_mi_dj_feed = 'sl'
                except Exception:
                    pass
                try:
                    if not alt_day6_mi_dj_un_evil:
                        alt_day6_mi_dj_feed = 'un'
                except Exception:
                    pass
                try:
                    if alt_day4_dv_7dl_hentai:
                        alt_day4_dv_7dl_hentai_done = True
                except Exception:
                    pass
                try:
                    if alt_day4_dv_7dl_mt_drugs:
                        alt_day4_dv_7dl_medication = 1
                except Exception:
                    pass
                try:
                    if alt_day4_dv_7dl_aidpost:
                        alt_day4_dv_7dl_medication = 2
                except Exception:
                    pass
                try:
                    if alt_day4_dv_7dl_vodka:
                        alt_day4_dv_7dl_vodka = 1
                except Exception:
                    pass
                try:
                    if alt_day4_dv_7dl_drank_vodka:
                        alt_day4_dv_7dl_vodka = 2
                except Exception:
                    pass
                try:
                    if alt_day6_dv_7dl_sl_route:
                        alt_day6_dv_7dl_route = 'sl'
                except Exception:
                    pass
                try:
                    if alt_day6_dv_7dl_mi_route:
                        alt_day6_dv_7dl_route = 'un'
                except Exception:
                    pass
                try:
                    if alt_day6_dv_7dl_dance == 1:
                        alt_day6_dv_7dl_dance = 'un'
                except Exception:
                    pass
                try:
                    if alt_day6_dv_7dl_dance == 22:
                        alt_day6_dv_7dl_dance = 'sl'
                except Exception:
                    pass
                try:
                    if alt_day7_dv_7dl_check == 0:
                        alt_day7_dv_7dl_check = 'dv_0'
                except Exception:
                    pass
                try:
                    if alt_day7_dv_7dl_check == 2:
                        alt_day7_dv_7dl_check = 'dv_1'
                except Exception:
                    pass
                try:
                    if alt_day7_dv_7dl_check == 1:
                        alt_day7_dv_7dl_check = 'dv_2'
                except Exception:
                    pass
                try:
                    if alt_day7_dv_7dl_check == 4:
                        alt_day7_dv_7dl_check = 'un'
                except Exception:
                    pass
                try:
                    if alt_day7_dv_7dl_check == 22:
                        alt_day7_dv_7dl_check = 'sl'
                except Exception:
                    pass
                try:
                    if alt_day7_dv_7dl_check == 5:
                        alt_day7_dv_7dl_check = 'mt'
                except Exception:
                    pass
                try:
                    if alt_day4_sl_lf_solo == 0:
                        alt_day4_sl_cl_lf_solo = 0
                except Exception:
                    pass
                try:
                    if alt_day4_sl_lf_solo == 1:
                        alt_day4_sl_cl_lf_solo = 2
                except Exception:
                    pass
                try:
                    if alt_day4_sl_lf_solo == 2:
                        alt_day4_sl_cl_lf_solo = 1
                except Exception:
                    pass
                try:
                    if alt_day4_sl_lf_solo == 3:
                        alt_day4_sl_cl_lf_solo = 3
                except Exception:
                    pass
                try:
                    if alt_day4_sl_un_rej:
                        alt_day4_sl_cl_un_rej = True
                except Exception:
                    pass
                try:
                    if alt_day4_sl_tut_iz:
                        alt_day4_sl_cl_tut_iz = True
                except Exception:
                    pass
                try:
                    if alt_day4_sl_tut_lf:
                        alt_day4_sl_cl_tut_lf = True
                except Exception:
                    pass
                try:
                    if alt_day6_sl_shirt:
                        alt_day6_sl_cl_shirt = True
                except Exception:
                    pass
                try:
                    if alt_day6_sl_int:
                        alt_day6_sl_cl_int = True
                except Exception:
                    pass
                try:
                    if alt_day5_sl_extra_house:
                        alt_day5_sl_cl_hentai_done = True
                except Exception:
                    pass
                try:
                    if alt_day6_sl_repel:
                        alt_day6_sl_cl_hentai_done = True
                except Exception:
                    pass
                try:
                    if alt_day6_sl_arc == 0:
                        alt_day6_sl_cl_arc = 'pi'
                except Exception:
                    pass
                try:
                    if alt_day6_sl_arc == 1:
                        alt_day6_sl_cl_arc = 'sh'
                except Exception:
                    pass
                try:
                    if alt_day4_un_7dl_dv_calm:
                        alt_day4_un_7dl_calm = 'dv'
                except Exception:
                    pass
                try:
                    if alt_day4_un_7dl_un_calm:
                        alt_day4_un_7dl_calm = 'un'
                except Exception:
                    pass
                try:
                    if alt_day5_un_7dl_sl_un_washing:
                        alt_day5_un_7dl_washing = 'sl_un'
                except Exception:
                    pass
                try:
                    if alt_day5_un_7dl_solo_washing:
                        alt_day5_un_7dl_washing = 'me'
                except Exception:
                    pass
                try:
                    if alt_day4_fz_un_letter:
                        alt_day4_un_fz_letter = True
                except Exception:
                    pass
                try:
                    if alt_day4_fz_sh == 1:
                        alt_day4_un_fz_companion = 'un'
                except Exception:
                    pass
                try:
                    if alt_day4_fz_sh == 2:
                        alt_day4_un_fz_companion = 'sl'
                except Exception:
                    pass
                try:
                    if alt_day4_fz_sh == 3:
                        alt_day4_un_fz_companion = 'dv'
                except Exception:
                    pass
                try:
                    if alt_day4_fz_sh == 4:
                        alt_day4_un_fz_companion = 'el'
                except Exception:
                    pass
                try:
                    if alt_day4_neu_transit == 0:
                        alt_day4_me_neu_transit = ''
                except Exception:
                    pass
                try:
                    if alt_day4_neu_transit == 1:
                        alt_day4_me_neu_transit = 'un_7dl'
                except Exception:
                    pass
                try:
                    if alt_day4_neu_transit == 11:
                        alt_day4_me_neu_transit = 'un_cl'
                except Exception:
                    pass
                try:
                    if alt_day4_neu_transit == 2:
                        alt_day4_me_neu_transit = 'sl_cl'
                except Exception:
                    pass
                try:
                    if alt_day4_neu_transit == 5:
                        alt_day4_me_neu_date = 'us'
                except Exception:
                    pass
                try:
                    if alt_day4_neu_us_snake:
                        alt_day4_me_neu_date = 'us'
                except Exception:
                    pass
                try:
                    if alt_day4_neu_transit == 6:
                        alt_day4_me_neu_date = 'mt'
                except Exception:
                    pass
                try:
                    if alt_day4_neu_mt_fire:
                        alt_day4_me_neu_date = 'mt'
                except Exception:
                    pass
                try:
                    if alt_day4_neu_date == 3:
                        alt_day4_me_neu_date = 'dv'
                except Exception:
                    pass
                try:
                    if alt_day4_neu_date == 4:
                        alt_day4_me_neu_date = 'mi'
                except Exception:
                    pass
                try:
                    if alt_day4_neu_mt_volley:
                        alt_day4_me_neu_volley = True
                except Exception:
                    pass
                try:
                    if alt_day4_neu_mt_songs:
                        alt_day4_me_neu_mi_songs = True
                except Exception:
                    pass
                try:
                    if alt_day4_neu_mt_diary:
                        alt_day4_me_neu_mt_diary = True
                except Exception:
                    pass
                try:
                    if alt_day4_neu_mt_volonteer:
                        alt_day4_me_neu_mt_volonteer = True
                except Exception:
                    pass
                try:
                    if mt_pt:
                        counter_mt_7dl = mt_pt
                except Exception:
                    pass
                try:
                    if us_pt:
                        counter_us_7dl = us_pt
                except Exception:
                    pass
                try:
                    if alt_day4_neu_us_pixies:
                        counter_us_px = alt_day4_neu_us_pixies
                except Exception:
                    pass
                try:
                    if alt_day5_neu_candle:
                        alt_day5_me_neu_candle = alt_day5_neu_candle
                except Exception:
                    pass
                try:
                    if alt_day5_neu_mt_voyeur:
                        alt_day5_me_neu_mt_voyeur = alt_day5_neu_mt_voyeur
                except Exception:
                    pass
                try:
                    if alt_day5_neu_us_stores:
                        alt_day5_me_neu_us_stores = True
                except Exception:
                    pass
                try:
                    if alt_day5_neu_sl_voyeur:
                        alt_day5_me_neu_sl_voyeur = True
                except Exception:
                    pass
                try:
                    if alt_day5_neu_potato:
                        alt_day5_me_neu_potato = True
                except Exception:
                    pass
                try:
                    if alt_day5_neu_mt_diary:
                        alt_day5_me_neu_mt_diary = True
                except Exception:
                    pass
                try:
                    if alt_day5_neu_us_potato:
                        alt_day5_me_neu_us_potato = True
                except Exception:
                    pass
                try:
                    if alt_day5_mt_7dl_hentai:
                        alt_day5_me_neu_mt_hentai = True
                except Exception:
                    pass
                try:
                    if alt_day6_us_7dl_tr:
                        alt_day6_us_7dl_help = True
                except Exception:
                    pass
                try:
                    if ('men_clubs' in list_voyage_7dl):
                        list_voyage_7dl.append('cyber')
                except Exception:
                    pass
                try:
                    if routetag == "us7dl_good":
                        routetag = "us_px_good"
                except Exception:
                    pass
                try:
                    if routetag == "us7dl_good_surp":
                        routetag = "us_px_good_surp"
                except Exception:
                    pass
                try:
                    if routetag == "us7dl_bad":
                        routetag = "us_7dl"
                except Exception:
                    pass
                try:
                    if routetag == "us7dl_bad_laugh":
                        routetag = "us_7dl_good"
                except Exception:
                    pass
                try:
                    if routetag == "us7dl_bad_sad":
                        routetag = "us_7dl_bad"
                except Exception:
                    pass
                # Новый турнир
                try:
                    if alt_pe == 1:
                        alt_my_rival_1_tour.take = 'un'
                except Exception:
                    pass

                try:
                    if alt_day2_hf2 == 1:
                        alt_my_rival_semifinal.take = 'un'
                except Exception:
                    pass

                try:
                    if alt_day2_hf2 == 5:
                        alt_my_rival_semifinal.take = 'us'
                except Exception:
                    pass

                try:
                    if alt_day2_round3 == 1:
                        alt_day2_gamblers_result['me'] = 21
                except Exception:
                    pass

                try:
                    if alt_day2_round3 == 2:
                        alt_day2_gamblers_result['me'] = 22
                except Exception:
                    pass

                try:
                    if alt_day2_f1 == 1 and alt_day2_round3 == 2:
                        alt_day2_gamblers_result['un'] = 21
                    elif alt_day2_f1 == 1 and alt_day2_round3 == 1:
                        alt_day2_gamblers_result['un'] = 22
                except Exception:
                    pass

                try:
                    if alt_day2_f1 == 4 and alt_day2_round3 == 2:
                        alt_day2_gamblers_result['mi'] = 21
                    elif alt_day2_f1 == 4 and alt_day2_round3 == 1:
                        alt_day2_gamblers_result['mi'] = 22
                except Exception:
                    pass

                try:
                    if alt_day2_f1 == 5 and alt_day2_round3 == 2:
                        alt_day2_gamblers_result['us'] = 21
                    elif alt_day2_f1 == 5 and alt_day2_round3 == 1:
                        alt_day2_gamblers_result['us'] = 22
                except Exception:
                    pass

                try:
                    if alt_day2_round1 == 1:
                        alt_day2_gamblers_result['me'] = 1
                except Exception:
                    pass

                try:
                    if alt_day2_round2 == 1:
                        alt_day2_gamblers_result['me'] = 11
                except Exception:
                    pass

                try:
                    if alt_day2_fail == 1:
                        alt_day2_gamblers_result['me'] = 1
                except Exception:
                    pass

                try:
                    if alt_day2_dv_bet_won == 2:
                        alt_day2_gamblers_result['me'] = 21
                except Exception:
                    pass
        if (alt_save_release_no == "0.43") and (not vars_043_saved):
            $ vars_043_saved = True
            python:
                try:
                    if alt_day3_un_fz_dv_fake_date:
                        counter_un_fz_dv_fake_date = alt_day3_un_fz_dv_fake_date
                        alt_day3_un_fz_work = 'dv'
                except Exception:
                    pass
                try:
                    if alt_day4_un_fz_mt_transit:
                        counter_un_fz_mt_transit = alt_day4_un_fz_mt_transit
                except Exception:
                    pass
                try:
                    if counter_old_road:
                        counter_un_fz_old_road = counter_old_road
                except Exception:
                    pass
                try:
                    if counter_un_fz:
                        counter_un_fz_un_route = counter_un_fz
                except Exception:
                    pass
                try:
                    if alt_day3_un_fz_un_work:
                        alt_day3_un_fz_work = 'un'
                except Exception:
                    pass
                try:
                    if alt_day3_un_fz_sl_work:
                        alt_day3_un_fz_work = 'sl'
                except Exception:
                    pass
                try:
                    if alt_day4_un_fz_un_help:
                        alt_day4_un_fz_morning_event = 'un'
                except Exception:
                    pass
                try:
                    if alt_day4_un_fz_mt_transit:
                        alt_day4_un_fz_morning_event = 'mt'
                except Exception:
                    pass
                try:
                    if alt_day4_un_fz_dv_escape:
                        alt_day4_un_fz_morning_event = 'dv'
                except Exception:
                    pass
                try:
                    if alt_day4_un_fz_un_evening_walk:
                        alt_day4_un_fz_un_evening = 'walk'
                except Exception:
                    pass
                try:
                    if alt_day4_un_fz_un_evening_sleep:
                        alt_day4_un_fz_un_evening = 'sleep'
                except Exception:
                    pass
                try:
                    if alt_day3_un_fz_us_help:
                        counter_un_fz = 1
                except Exception:
                    pass
                try:
                    if alt_day3_mt_quest:
                        counter_un_fz = 2
                except Exception:
                    pass
                try:
                    if counter_un_fz_dv_fake_date == 0:
                        counter_un_fz_dream_un += 1
                except Exception:
                    pass
                try:
                    if alt_day3_un_fz_walk:
                        counter_un_fz_dream_un += 1
                except Exception:
                    pass
                try:
                    if alt_day3_un_fz_stories:
                        counter_un_fz_dream_road += 1
                except Exception:
                    pass
                try:
                    if counter_un_fz_old_road == 7:
                        counter_un_fz_dream_road += 1
                except Exception:
                    pass
        if (("0.3" in alt_save_release_no) or ("0.4" in alt_save_release_no)) and (not vars_049_saved):
            $ vars_049_saved = True
            python:
                try:
                    if alt_day4_sl_7dl_phone:
                        alt_day6_sl_7dl_square = True
                except Exception:
                    pass
                try:
                    if alt_day6_us_px_sl_join:
                        alt_day6_us_7dl_px_sl_join = True
                except Exception:
                    pass
                try:
                    if alt_day7_us_px_escaped:
                        alt_day7_us_7dl_px_escaped = True
                except Exception:
                    pass
                try:
                    if counter_us_px:
                        counter_us_7dl_px = counter_us_px
                except Exception:
                    pass
                try:
                    if dv_dj_morning:
                        routetag = "dvdj"
                except Exception:
                    pass
                if routetag == "prologue":
                    for i in ["День 1","День 2","День 3"]:
                        if i in save_name:
                            routetag = "common"
                    for i in ["День 4","День 5","День 6","День 7"]:
                        if i in save_name:
                            routetag = "neu"
        if (alt_save_release_no not in alt_compatible_release_no) and (not alt_save_fixed): # и если сохранение несовместимо
            python: # генерируем строку с номерами версий
                alt_aicr_string = (u"ЗАГРУЖАЕМАЯ ВЕРСИЯ СОХРАНЕНИЯ (%s) НЕСОВМЕСТИМА С ЭТОЙ ВЕРСИЕЙ МОДА (%s)") % (alt_save_release_no, alt_release_no)
            $ alt_save_fixed = True
            call screen alt_incompatible_release # и показываем экран предупреждения с выбором вариантов
        elif ((alt_save_release_no in ["0.34.a", "0.34.b", "0.35.a", "0.36.a", "0.37.a", "0.38.a", "0.39.a", "0.40", "0.40.1", "0.40.2"]) or ((alt_save_release_no in ["0.42", "0.43"]) and counter_un_cl) or ((("0.3" in alt_save_release_no) or ("0.4" in alt_save_release_no)) and ("us_px" in routetag))) and (not alt_save_fixed): # если сохранение частично совместимо
            python: # генерируем строку с предупреждением
                alt_aicr_string = (u"ВЫ ЗАГРУЖАЕТЕ СОХРАНЕНИЕ С УСТАРЕВШЕЙ (%s) ВЕРСИИ МОДА") % (alt_save_release_no)
            $ alt_save_fixed = True
            call screen alt_load_warning # и показываем экран с возможностью перейти на начало игрового дня
    else: # если сейв не от 7дл
        if persistent.noir_interface: # если был включён нуарный интерфейс
            $ noir_interface_off() # выключаем нуарный интерфейс
        if persistent.alt_interface: # если был включён интерфейс 7дл
            $ alt_interface_off() # выключаем интерфейс 7дл
            $ reset_names_to_default() # сбрасываем имена персонажей на дефолтные
            $ reload_names() # загружаем сброшенные имена
    return # возвращаемся в игру

label alt_vars_saved:
    $ vars_040_saved = True
    $ vars_0401_saved = True
    $ vars_0402_saved = True
    $ vars_043_saved = True
    $ vars_049_saved = True
    return
