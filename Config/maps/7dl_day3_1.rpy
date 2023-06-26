label alt_day3_map_prepare:
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(3, u"День")
    $ disable_all_zones_alt2()
    $ disable_all_chibi_alt2()

    play music music_list["smooth_machine"] fadein 2

    $ set_zone_alt2("music_club_alt2",   "alt_day3_event_music_club")
    if alt_day3_date == 'mi':
        $ set_chibi_alt2("music_club_alt2",    "mi")
    $ set_zone_alt2("clubs_alt2",        "alt_day3_event_clubs")
    $ set_zone_alt2("camp_entrance_alt2","alt_day3_event_camp_entrance")
    $ set_zone_alt2("dining_hall_alt2",  "alt_day3_event_dining_hall")
    $ set_zone_alt2("sport_area_alt2",   "alt_day3_event_sport_area")
    $ set_zone_alt2("beach_alt2",        "alt_day3_event_beach")
    if alt_day3_date == 'sl':
        $ set_chibi_alt2("beach_alt2",         "sl")
    if not (alt_day2_date == 'un_fz'):
        $ set_zone_alt2("library_alt2",  "alt_day3_event_library")
        if alt_day3_date == 'un':
            $ set_chibi_alt2("library_alt2",   "un")
    $ set_zone_alt2("medic_house_alt2",  "alt_day3_event_medic_house")
    $ set_zone_alt2("estrade_alt2",      "alt_day3_event_estrade")
    if alt_day3_date == 'dv':
        $ set_chibi_alt2("estrade_alt2",       "dv")
    else:
        $ set_chibi_alt2("estrade_alt2",        "?")
    $ set_zone_alt2("square_alt2",       "alt_day3_event_square")
    $ set_zone_alt2("boat_station_alt2", "alt_day3_event_boat_station")

    jump alt_day3_map

label alt_day3_map:
    $ show_map_alt2()

label alt_day3_event_music_club:
    call alt_day3_event_music_club1
    if alt_day3_date == 'mi':
        return
    else:
        $ disable_current_zone_alt2()
        jump alt_day3_map


label alt_day3_event_clubs:
    call alt_day3_event_clubs1
    $ disable_current_zone_alt2()
    jump alt_day3_map

label alt_day3_event_camp_entrance:
    call alt_day3_event_camp_entrance1
    $ disable_current_zone_alt2()
    jump alt_day3_map

label alt_day3_event_dining_hall:
    call alt_day3_event_dining_hall1
    $ disable_current_zone_alt2()
    jump alt_day3_map

label alt_day3_event_sport_area:
    call alt_day3_event_sport_area1
    $ disable_current_zone_alt2()
    jump alt_day3_map

label alt_day3_event_beach:
    call alt_day3_event_beach1
    if alt_day3_date == 'sl':
        return
    else:
        $ disable_current_zone_alt2()
        jump alt_day3_map

label alt_day3_event_library:
    call alt_day3_event_library1
    if alt_day3_date == 'un':
        return
    else:
        $ disable_current_zone_alt2()
        jump alt_day3_map

label alt_day3_event_medic_house:
    call alt_day3_event_medic_house1
    $ disable_current_zone_alt2()
    jump alt_day3_map

label alt_day3_event_estrade:
    call alt_day3_event_estrade1
    return

label alt_day3_event_square:
    call alt_day3_event_square1
    $ disable_current_zone_alt2()
    jump alt_day3_map

label alt_day3_event_boat_station:
    call alt_day3_event_boat_station1
    $ disable_current_zone_alt2()
    jump alt_day3_map
