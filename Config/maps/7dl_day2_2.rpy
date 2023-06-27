﻿label alt_day2_mapEv_prepare:
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(2, u"Evening events")
    $ disable_all_zones_alt2()
    $ disable_all_chibi_alt2()

    $ set_zone_alt2('music_club_alt2',    'alt_day2_eventEv_music_club')
    if lp_mi >= 5:
        $ set_chibi_alt2('music_club_alt2',   'mi')
    $ set_zone_alt2('kyber_club_alt2',    'alt_day2_eventEv_clubs')
    $ set_zone_alt2('camp_entrance_alt2', 'alt_day2_eventEv_camp_entrance')
    $ set_zone_alt2('dv_us_house_alt2',   'alt_day2_eventEv_dv_us_house')
    $ set_zone_alt2('un_mi_house_alt2',   'alt_day2_eventEv_un_mi_house')
    if lp_un >= 6 and (loki or herc):
        $ set_chibi_alt2('un_mi_house_alt2',  'un')
    $ set_zone_alt2('dining_hall_alt2',   'alt_day2_eventEv_dining_hall')
    $ set_zone_alt2('court_alt2',         'alt_day2_eventEv_sport_area')
    if lp_un >= 6 and dr:
        $ set_chibi_alt2('court_alt2',        'un')
    $ set_zone_alt2('me_mt_house_alt2',   'alt_day2_eventEv_me_mt_house')
    $ set_chibi_alt2('me_mt_house_alt2',      'mt')
    $ set_zone_alt2('library_alt2',       'alt_day2_eventEv_library')
    $ set_zone_alt2('medic_house_alt2',   'alt_day2_eventEv_medic_house')
    $ set_zone_alt2('estrade_alt2',       'alt_day2_eventEv_estrade')
    if lp_dv < 5:
        $ set_chibi_alt2('estrade_alt2',      'dv')
    $ set_zone_alt2('square_alt2',        'alt_day2_eventEv_square')
    if (lp_sl >= 8) and ((counter_sl_cl == 1) or (counter_sl_7dl == 3)):
        $ set_chibi_alt2('square_alt2',       'sl')
    $ set_zone_alt2('boat_station_alt2',  'alt_day2_eventEv_boat_station')
    if not alt_day2_dv_chased:
        $ set_zone_alt2('beach_alt2',     'alt_day2_eventEv_beach')
        if lp_dv >= 5:
            $ set_chibi_alt2('beach_alt2',    'dv')
    play music music_list["smooth_machine"] fadein 2
    jump alt_day2_mapEv

label alt_day2_mapEv:
    scene black with fade
    $ show_map_alt2()

label alt_day2_eventEv_music_club:
    call alt_day2_eventEv_music_club1
    pause(1)
    if alt_day2_mi_date:
        return
    else:
        $ disable_current_zone_alt2()
        jump alt_day2_mapEv

label alt_day2_eventEv_clubs:
    call alt_day2_eventEv_clubs1
    if been_there_alt2()>1:
        $ disable_current_zone_alt2()
    jump alt_day2_mapEv

label alt_day2_eventEv_camp_entrance:
    call alt_day2_eventEv_camp_entrance1
    $ disable_current_zone_alt2()
    jump alt_day2_mapEv

label alt_day2_eventEv_un_mi_house:
    call alt_day2_eventEv_un_mi_house1
    pause(1)
    if ((lp_un >= 6) and (loki or herc)) or alt_day2_date == 'un_fz':
        return
    else:
        $ disable_current_zone_alt2()
        jump alt_day2_mapEv

label alt_day2_eventEv_dv_us_house:
    call alt_day2_eventEv_dv_us_house1
    $ disable_current_zone_alt2()
    jump alt_day2_mapEv

label alt_day2_eventEv_dining_hall:
    call alt_day2_eventEv_dining_hall1
    $ disable_current_zone_alt2()
    jump alt_day2_mapEv

label alt_day2_eventEv_sport_area:
    call alt_day2_eventEv_sport_area1
    pause(1)
    if (lp_un >= 6) and dr:
        return
    else:
        $ disable_current_zone_alt2()
        jump alt_day2_mapEv

label alt_day2_eventEv_beach:
    call alt_day2_eventEv_beach1
    if (alt_day2_gamblers_result['me'] == 22) and (alt_day2_dv_ultim == 1):
        return
    else:
        $ disable_current_zone_alt2()
        jump alt_day2_mapEv

label alt_day2_eventEv_me_mt_house:
    call alt_day2_eventEv_me_mt_house1
    if alt_day2_mt_help:
        pass
    else:
        $ disable_current_zone_alt2()
    return

label alt_day2_eventEv_library:
    call alt_day2_eventEv_library1
    $ disable_current_zone_alt2()
    jump alt_day2_mapEv

label alt_day2_eventEv_medic_house:
    call alt_day2_eventEv_medic_house1
    $ disable_current_zone_alt2()
    jump alt_day2_mapEv

label alt_day2_eventEv_estrade:
    call alt_day2_eventEv_estrade1
    $ disable_current_zone_alt2()
    jump alt_day2_mapEv

label alt_day2_eventEv_square:
    call alt_day2_eventEv_square1
    pause(1)
    if (lp_sl >= 8) and ((counter_sl_cl == 1) or (counter_sl_7dl == 3)):
        return
    elif alt_day2_cake:
        return
    else:
        $ disable_current_zone_alt2()
        jump alt_day2_mapEv

label alt_day2_eventEv_boat_station:
    call alt_day2_eventEv_boat_station1
    if alt_day2_cake:
        return
    else:
        $ disable_current_zone_alt2()
        jump alt_day2_mapEv
