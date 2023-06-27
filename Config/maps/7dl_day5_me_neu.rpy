label alt_day5_me_neu_map_evening:
    $ alt_chapter(5, u"Одиночка. Вечерняя прогулка.")
    $ disable_all_zones_alt2()
    $ disable_all_chibi_alt2()

    if alt_day4_me_neu_date == 'us' and lp_dv >= 4:
        $ set_zone_alt2('dv_us_house_alt2', 'alt_day5_me_neu_map_house_dv')
        $ set_chibi_alt2('dv_us_house_alt2', '?')

    $ set_zone_alt2('store_house_alt2', 'alt_day5_me_neu_map_shed')
    $ set_chibi_alt2('store_house_alt2', '?')

    if not dr:
        $ set_zone_alt2('medic_house_alt2', 'alt_day5_me_neu_map_medic_house')
        $ set_chibi_alt2('medic_house_alt2', '?')

    $ set_zone_alt2('boat_station_alt2', 'alt_day5_me_neu_map_boat_station')
    $ set_chibi_alt2('boat_station_alt2', '?')

    $ set_zone_alt2('library_alt2', 'alt_day5_me_neu_map_library')
    $ set_chibi_alt2('library_alt2', '?')

    $ set_zone_alt2('sports_hall_alt2', 'alt_day5_me_neu_map_playground')
    $ set_chibi_alt2('sports_hall_alt2', '?')

    $ set_zone_alt2('kyber_club_alt2', 'alt_day5_me_neu_map_cyber')
    $ set_chibi_alt2('kyber_club_alt2', '?')

    $ set_zone_alt2('beach_alt2', 'alt_day5_me_neu_map_beach')
    $ set_chibi_alt2('beach_alt2', '?')

    jump alt_day5_me_neu_map_search

label alt_day5_me_neu_map_search:
    if alt_day5_me_neu_map_points >= 3:
        return
    scene black with fade
    $ show_map_alt2()

label alt_day5_me_neu_map_house_dv:
    call alt_day5_me_neu_map_house_dv1
    $ disable_current_zone_alt2()
    if alt_day1_sl_keys_took not in (1, 3):
        $ alt_day5_me_neu_map_points += 1
        jump alt_day5_me_neu_map_search
    else:
        $ alt_day5_me_neu_map_ivent = 'dv'
        return

label alt_day5_me_neu_map_shed:
    call alt_day5_me_neu_map_shed1
    $ disable_current_zone_alt2()
    if alt_day1_sl_keys_took not in (1, 3):
        $ alt_day5_me_neu_map_points += 1
        jump alt_day5_me_neu_map_search
    else:
        return

label alt_day5_me_neu_map_medic_house:
    call alt_day5_me_neu_map_medic_house1
    $ disable_current_zone_alt2()
    if alt_day1_sl_keys_took not in (1, 3):
        $ alt_day5_me_neu_map_points += 1
        jump alt_day5_me_neu_map_search
    else:
        $ alt_day5_me_neu_map_ivent = 'medic'
        return

label alt_day5_me_neu_map_boat_station:
    call alt_day5_me_neu_map_boat_station1
    $ alt_day5_me_neu_map_ivent = 'boat'
    return

label alt_day5_me_neu_map_library:
    call alt_day5_me_neu_map_library1
    $ disable_current_zone_alt2()
    if (not (loki and counter_me_neu_answers == 1)) or (alt_day5_me_neu_nwsppr):
        $ alt_day5_me_neu_map_points += 1
        jump alt_day5_me_neu_map_search
    else:
        return

label alt_day5_me_neu_map_playground:
    call alt_day5_me_neu_map_playground1
    $ disable_current_zone_alt2()
    $ alt_day5_me_neu_map_points += 1
    jump alt_day5_me_neu_map_search

label alt_day5_me_neu_map_cyber:
    call alt_day5_me_neu_map_cyber1
    $ disable_current_zone_alt2()
    $ alt_day5_me_neu_map_points += 1
    jump alt_day5_me_neu_map_search

label alt_day5_me_neu_map_beach:
    $ alt_day5_me_neu_map_ivent = 'beach'
    call alt_day5_me_neu_map_beach1
    return