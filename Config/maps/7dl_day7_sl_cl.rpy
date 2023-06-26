label alt_day7_sl_cl_bl_tt_map:
    $ disable_all_zones_alt2()
    $ disable_all_chibi_alt2()
    $ set_zone_alt2('admin_house_alt2', 'alt_day7_sl_cl_admins')
    $ set_zone_alt2('kyber_club_alt2',  'alt_day7_sl_cl_clubs')
    $ set_zone_alt2('dining_hall_alt2', 'alt_day7_sl_cl_dining_hall')
    $ set_zone_alt2('sports_hall_alt2', 'alt_day7_sl_cl_sport_area')
    $ set_zone_alt2('volleyball_alt2',  'alt_day7_sl_cl_volleyball_alt')
    $ set_zone_alt2('estrade_alt2',     'alt_day7_sl_cl_estrade')
    jump alt_day7_sl_cl_map

label alt_day7_sl_cl_map:
    play music music_list["smooth_machine"] fadein 2
    if len(list_sl_cl_map_7dl) > 4:
        if alt_day6_sl_cl_arc == 'pi':
            $ set_zone_alt2('boat_station_alt2', 'alt_day7_sl_cl_boat_station')
        else:
            $ set_zone_alt2('beach_alt2',        'alt_day7_sl_cl_beach')
    scene black with fade
    $ show_map_alt2()

label alt_day7_sl_cl_admins:
    call alt_day7_sl_cl_admins1
    $ list_sl_cl_map_7dl.append('admins')
    $ disable_current_zone_alt2()
    jump alt_day7_sl_cl_map

label alt_day7_sl_cl_clubs:
    call alt_day7_sl_cl_clubs1
    $ list_sl_cl_map_7dl.append('clubs')
    $ disable_current_zone_alt2()
    jump alt_day7_sl_cl_map

label alt_day7_sl_cl_dining_hall:
    call alt_day7_sl_cl_dining_hall1
    $ list_sl_cl_map_7dl.append('dining_hall')
    $ disable_current_zone_alt2()
    jump alt_day7_sl_cl_map

label alt_day7_sl_cl_sport_area:
    call alt_day7_sl_cl_sport_area1
    $ list_sl_cl_map_7dl.append('sport_area')
    $ disable_current_zone_alt2()
    jump alt_day7_sl_cl_map

label alt_day7_sl_cl_volleyball_alt:
    call alt_day7_sl_cl_volleyball_alt2
    $ list_sl_cl_map_7dl.append('volleyball')
    $ disable_current_zone_alt2()
    jump alt_day7_sl_cl_map

label alt_day7_sl_cl_estrade:
    call alt_day7_sl_cl_estrade1
    $ list_sl_cl_map_7dl.append('estrade')
    $ disable_current_zone_alt2()
    jump alt_day7_sl_cl_map

label alt_day7_sl_cl_boat_station:
    call alt_day7_sl_cl_boat_station1
    call alt_day7_sl_cl_beach
    return
