label alt_day6_un_fz_map_morning:
    $ disable_all_zones_alt2()
    $ disable_all_chibi_alt2()

    $ set_zone_alt2('boat_station_alt2', 'alt_day6_un_fz_map_boatstation')
    $ set_zone_alt2('sport_area_alt2',   'alt_day6_un_fz_map_playground')
    $ set_zone_alt2('music_club_alt2',   'alt_day6_un_fz_map_musclub')
    if counter_un_fz_dv_fake_date == 3:
        $ set_zone_alt2('dv_us_house_alt2', 'alt_day6_un_fz_map_house_dv')
        $ set_chibi_alt2('dv_us_house_alt2', 'dv')

    jump alt_day6_un_fz_map

label alt_day6_un_fz_map:
    play music music_list["smooth_machine"] fadein 2
    if alt_day6_un_fz_map1_quest == '':
        scene bg ext_dining_hall_near_day with dissolve
        "Стоя на крыльце столовой, я прикидывал, куда бы можно было податься."
    else:
        $ disable_all_zones_alt2()
        $ disable_all_chibi_alt2()
        $ set_zone_alt2('beach_alt2',         'alt_day6_un_fz_map_beach')
        $ set_zone_alt2('dining_hall_alt2',   'alt_day6_un_fz_map_dinner_hall')
        $ set_zone_alt2('camp_entrance_alt2', 'alt_day6_un_fz_map_busstation')
    $ show_map_alt2()

label alt_day6_un_fz_map_boatstation:
    call alt_day6_un_fz_map_boatstation1
    $ disable_current_zone_alt2()
    jump alt_day6_un_fz_map

label alt_day6_un_fz_map_playground:
    call alt_day6_un_fz_map_playground1
    $ disable_current_zone_alt2()
    jump alt_day6_un_fz_map

label alt_day6_un_fz_map_musclub:
    call alt_day6_un_fz_map_musclub1
    $ disable_current_zone_alt2()
    jump alt_day6_un_fz_map

label alt_day6_un_fz_map_house_dv:
    call alt_day6_un_fz_map_house_dv1
    $ disable_current_zone_alt2()
    jump alt_day6_un_fz_map

label alt_day6_un_fz_map_beach:
    call alt_day6_un_fz_map_beach2
    $ disable_current_zone_alt2()
    return

label alt_day6_un_fz_map_dinner_hall:
    call alt_day6_un_fz_map_dinner_hall2
    $ disable_current_zone_alt2()
    return

label alt_day6_un_fz_map_busstation:
    call alt_day6_un_fz_map_busstation2
    $ disable_current_zone_alt2()
    return
