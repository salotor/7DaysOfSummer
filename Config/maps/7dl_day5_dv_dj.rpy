label alt_day5_dv_dj_map_siesta:
    $ disable_all_zones_alt2()
    $ disable_all_chibi_alt2()

    $ set_zone_alt2('dv_us_house_alt2', 'alt_day5_dv_dj_map_house_dv')
    $ set_chibi_alt2('dv_us_house_alt2', 'dv')
    if loki:
        $ set_zone_alt2('square_alt2', 'alt_day5_dv_dj_map_square')
    elif herc:
        $ set_zone_alt2('music_club_alt2',   'alt_day5_dv_dj_map_musclub')
    elif dr:
        $ set_zone_alt2('kyber_club_alt2',   'alt_day5_dv_dj_map_cyber_club')
    if not alt_day4_dv_dj_un_quarrel:
        $ set_zone_alt2('library_alt2',   'alt_day5_dv_dj_map_library')

    play music music_list["smooth_machine"] fadein 2
    $ show_map_alt2()
    return


label alt_day5_dv_dj_map_house_dv:
    call alt_day5_dv_dj_map_house_dv1
    $ alt_day5_dv_dj_map = "dv"
    $ lp_dv += 1
    $ disable_current_zone_alt2()
    return

label alt_day5_dv_dj_map_square:
    call alt_day5_dv_dj_map_square1
    $ alt_day5_dv_dj_map = "us"
    $ disable_current_zone_alt2()
    return

label alt_day5_dv_dj_map_library:
    call alt_day5_dv_dj_map_library1
    $ alt_day5_dv_dj_map = "un"
    $ disable_current_zone_alt2()
    return

label alt_day5_dv_dj_map_musclub:
    call alt_day5_dv_dj_map_musclub1
    $ alt_day5_dv_dj_map = "mi"
    $ disable_current_zone_alt2()
    return

label alt_day5_dv_dj_map_cyber_club:
    call alt_day5_dv_dj_map_cyber_club1
    $ alt_day5_dv_dj_map = "cyber"
    $ disable_current_zone_alt2()
    return
