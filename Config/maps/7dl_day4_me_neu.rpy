label alt_day4_me_neu_map_evening:
    $ alt_chapter(4, u"Одиночка. Поиск ответов.")
    $ disable_all_zones_alt2()
    $ disable_all_chibi_alt2()

    if alt_day4_me_neu_date in ('mt', 'us'):
        $ set_zone_alt2('me_mt_house_alt2', 'alt_day4_me_neu_map_me_mt_house')
        if alt_day4_me_neu_date == 'mt' or herc:
            $ set_chibi_alt2('me_mt_house_alt2', 'mt')
        elif alt_day4_me_neu_date == 'us':
            $ set_chibi_alt2('me_mt_house_alt2', 'us')

    if (alt_day3_technoquest2) and (alt_day3_dj != 'dv'):
        $ set_zone_alt2('medic_house_alt2', 'alt_day4_me_neu_map_medic_house')
        $ set_chibi_alt2('medic_house_alt2', 'cs')

    $ set_zone_alt2('estrade_alt2', 'alt_day4_me_neu_map_estrade')
    $ set_chibi_alt2('estrade_alt2', 'mi')

    if herc:
        $ set_zone_alt2('kyber_club_alt2', 'alt_day4_me_neu_map_cyber')
        if persistent.alt_binder and (alt_day2_date == '') and (counter_dv_7dl == 0) and (alt_day3_dj != 'dv') and alt_day3_technoquest2:
            $ set_chibi_alt2('kyber_club_alt2', 'heart2')
        else:
            $ set_chibi_alt2('kyber_club_alt2', 'heart1')

    if loki:
        $ set_zone_alt2('admin_house_alt2', 'alt_day4_me_neu_map_admin_house')
        if persistent.alt_binder and (alt_day2_date == '') and (counter_dv_7dl == 0) and (alt_day3_dj != 'dv') and (alt_day1_sl_keys_took in (1, 3)):
            $ set_chibi_alt2('admin_house_alt2', 'heart2')
        else:
            $ set_chibi_alt2('admin_house_alt2', 'heart1')

    $ set_zone_alt2('boat_station_alt2', 'alt_day4_me_neu_map_boat_station')
    if persistent.alt_binder and dr and (alt_day2_date == '') and (counter_dv_7dl == 0) and (alt_day3_dj != 'dv') and (alt_day1_sl_keys_took in (1, 3)):
        $ set_chibi_alt2('boat_station_alt2', 'heart2')
    elif dr:
        $ set_chibi_alt2('boat_station_alt2', 'heart1')

    $ set_zone_alt2('dining_hall_alt2', 'alt_day4_me_neu_map_dining_hall')
    $ set_chibi_alt2('dining_hall_alt2', 'mt')
    play music music_list["smooth_machine"] fadein 2

    jump alt_day4_me_neu_map_answers

label alt_day4_me_neu_map_answers:
    scene black with fade
    $ show_map_alt2()

label alt_day4_me_neu_map_dining_hall:
    call alt_day4_me_neu_map_dining_hall1
    if alt_day4_me_neu_mt_dream:
        call alt_day4_me_neu_map_estrade1
        return
    $ disable_current_zone_alt2()
    jump alt_day4_me_neu_map_answers

label alt_day4_me_neu_map_estrade:
    call alt_day4_me_neu_map_estrade1
    return

label alt_day4_me_neu_map_cyber:
    if persistent.alt_binder and herc and (alt_day2_date == '') and (counter_dv_7dl == 0) and (alt_day3_dj != 'dv') and alt_day3_technoquest2:
        call alt_day4_me_neu_map_cyber1
        return
    else:
        scene bg ext_clubs_sunset_7dl with dissolve
        th "И что мне тут делать?"
        th "Пытаться объяснить будущим светилам советской науки что такое мультиварка?"
        th "Лучше отправлюсь куда-нибудь ещё."
        $ disable_current_zone_alt2()
        jump alt_day4_me_neu_map_answers
label alt_day4_me_neu_map_admin_house:
    if persistent.alt_binder and loki and (alt_day2_date == '') and (counter_dv_7dl == 0) and (alt_day3_dj != 'dv') and (alt_day1_sl_keys_took in (1, 3)):
        call alt_day4_me_neu_map_admin_house1
        return
    else:
        scene bg ext_admins_day_7dl with dissolve
        th "За все четыре дня в лагере я ни разу не видел ни одного представителя местной администрации."
        th "Делать здесь мне решительно нечего."
        $ disable_current_zone_alt2()
        jump alt_day4_me_neu_map_answers

label alt_day4_me_neu_map_boat_station:
    call alt_day4_me_neu_map_boat_station1
    if alt_day4_me_neu_boat:
        return
    $ disable_current_zone_alt2()
    jump alt_day4_me_neu_map_answers

label alt_day4_me_neu_map_me_mt_house:
    if herc:
        call alt_day4_un_fz_mt_house
    else:
        call alt_day4_me_neu_map_me_mt_house1
    if alt_day4_me_neu_mt_diary or (alt_day4_me_neu_date == 'us'):
        return
    else:
        $ disable_current_zone_alt2()
        jump alt_day4_me_neu_map_answers

