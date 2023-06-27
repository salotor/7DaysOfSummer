label alt_day6_me_neu_map_sh:
    $ alt_chapter(6, u"Одиночка. Тихий час.")
    $ disable_all_zones_alt2()
    $ disable_all_chibi_alt2()

    $ set_zone_alt2('me_mt_house_alt2', 'alt_day6_me_neu_map_mt_house')

    $ set_zone_alt2('dv_us_house_alt2', 'alt_day6_me_neu_map_house_dv')
    $ set_chibi_alt2('dv_us_house_alt2', 'dv_us')

    $ set_zone_alt2('music_club_alt2',   'alt_day6_me_neu_map_musclub')
    $ set_chibi_alt2('music_club_alt2', 'mi')

    $ set_zone_alt2('store_house_alt2', 'alt_day6_me_neu_map_shed')
    $ set_chibi_alt2('store_house_alt2', 'sl')

    jump alt_day6_me_neu_map_search

label alt_day6_me_neu_map_search:
    scene black with fade
    $ show_map_alt2()
    return

label alt_day6_me_neu_map_house_dv:
    call alt_day6_me_neu_map_house_dv1
    if (lp_dv or counter_us_7dl) < 0 or ((alt_day5_me_neu_map_ivent == 'boat') and (counter_mz_7dl == 3)):
        $ disable_current_zone_alt2()
        jump alt_day6_me_neu_map_search
    else:
        $ alt_day6_me_neu_map_ivent = 'dv_house'
        return
