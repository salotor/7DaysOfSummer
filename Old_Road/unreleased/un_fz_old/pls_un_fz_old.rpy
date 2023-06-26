label alt_day4_un_fz_vars_old:
    $ alt_day4_un_fz_sl_walk = False
    $ alt_day4_un_fz_sl_again = False
    $ alt_day4_un_fz_sl_wish = False
    $ alt_day4_un_fz_letter = False
    $ alt_day4_un_fz_companions = ['un', 'sl', 'dv', 'el', 'me']
    $ alt_day4_un_fz_companion = ''
    $ alt_day4_un_fz_senio = 1


    $ alt_day2_bf = 'sl'
    $ list_voyage_7dl = ['medic', 'library', 'cyber']
    $ alt_day2_us_escape = True

    "С кем ходили на обход лагеря?"
    menu:
        "С Алисой":
            $ alt_day2_convoy = 'dv'
        "Со Славей":
            $ alt_day2_convoy = 'sl'
    "Отношения со Славей:"
    menu:
        "Так себе":
            $ lp_sl = 0
        "Отличные":
            $ lp_sl = 5
    "Отношения со Алисой:"
    menu:
        "Так себе":
            $ lp_dv = 0
        "Отличные":
            $ lp_dv = 7
    "Отношения с Леной:"
    menu:
        "Так себе":
            $ lp_un = 0
        "Отличные":
            $ lp_un = 5
    "Провожала Славя до домика Ольги по приезде?"
    menu:
        "Да":
            $ counter_sl_7dl = 1
        "Нет":
            $ counter_sl_7dl = 0
    return

label alt_day4_un_fz_start_old:
    pause(1)
    call alt_day4_un_fz_vars_old
    call alt_day4_me_neu_vars
    call alt_day4_sl_cl_vars
    pause(1)
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    $ alt_chapter(4, u"Лена. ФЗ. Утро")
    call alt_day4_un_fz_begin_old
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    if (alt_day2_convoy == 'sl'):
        call alt_day4_un_fz_sl_old
        pause(1)
        call alt_day4_un_fz_sl_cards_old
    elif (alt_day2_convoy == 'dv'):
        call alt_day4_un_fz_dv_old
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    call alt_day4_un_fz_postcard_old
    pause(1)
    if (alt_day2_convoy == 'sl'):
        call alt_day4_un_fz_sl_dinner_old
    elif (alt_day2_convoy == 'dv'):
        call alt_day4_un_fz_dv_dinner_old
    pause(1)
    call alt_day4_un_fz_lost_coun_old
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Лена. ФЗ. Вечер.")
    call alt_day4_un_fz_supper_old
    pause(1)
    call alt_day4_un_fz_mt_old
    pause(1)
    $ alt_chapter(4, u"Лена. ФЗ. Шурик.")
    call alt_day4_un_fz_sh_old
    pause(1)
    call alt_day4_un_fz_sh_choose_old
    pause(1)
    call alt_day4_un_fz_old_camp_old
    pause(1)
    call alt_day4_un_fz_xroad
    pause(1)
    call alt_day4_un_fz_exit_old
    pause(1)
    call alt_day4_un_fz_herbs_old
    pause(1)
    if alt_day4_un_fz_companion not in ['sl', 'dv']:
        jump alt_day5_un_fz_start
    else:
        jump alt_stories_start

label alt_day5_un_fz_start:
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Лена. ФЗ. Утро.")
    call alt_day5_fz_begin_old
    pause(1)
    jump alt_stories_start
