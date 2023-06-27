label alt_day3_mapAf_prepare:
    $ disable_all_zones_alt2()
    $ disable_all_chibi_alt2()
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(3, u"Вообще-то, тихий час!")
    $ set_zone_alt2("music_club_alt2",      "alt_day3_eventAf_music_club")
    if alt_day3_date == 'dv':
        $ set_chibi_alt2("music_club_alt2",      "dv")
    if (counter_sl_cl == 4):
        $ set_zone_alt2("admin_house_alt2", "alt_day3_eventAf_admins")
        $ set_chibi_alt2("admin_house_alt2",     "sl")
    else:
        $ set_zone_alt2("clubs_alt2",       "alt_day3_eventAf_clubs")
        $ set_chibi_alt2("clubs_alt2",           "el")
        if (counter_sl_cl <= 3) or alt_day3_sl_invite:
            $ set_chibi_alt2("estrade_alt2", "?")
            $ set_zone_alt2("estrade_alt2", "alt_day3_eventAf_estrade")
    $ set_zone_alt2("dining_hall_alt2",     "alt_day3_eventAf_dining_hall")
    $ set_chibi_alt2("dining_hall_alt2",         "us")
    $ set_zone_alt2("me_mt_house_alt2",     "alt_day3_eventAf_me_mt_house")
    $ set_zone_alt2("un_mi_house_alt2",     "alt_day3_eventAf_un_mi_house")
    if counter_mi_7dl == 1:
        $ set_chibi_alt2("un_mi_house_alt2",     "mi")
    $ set_zone_alt2("library_alt2",         "alt_day3_eventAf_library")
    jump alt_day3_mapAf

label alt_day3_mapAf:
    stop ambience
    stop sound_loop
    stop music
    scene black with fade
    play music music_list["smooth_machine"] fadein 3
    $ show_map_alt2()

label alt_day3_eventAf_clubs:
    if been_there_alt2() > 1:
        call alt_day3_eventAf_clubs_ladder
        $ disable_current_zone_alt2()
        jump alt_day3_mapAf
    else:
        call alt_day3_eventAf_clubs_technoquest
        pause(1)
        jump alt_day3_mapAf

label alt_day3_eventAf_music_club:
    call alt_day3_eventAf_music_club1
    if counter_dv_7dl == 3:
        return
    else:
        $ disable_current_zone_alt2()
        jump alt_day3_mapAf

label alt_day3_eventAf_un_mi_house:
    call alt_day3_eventAf_un_mi_house1
    if counter_mi_7dl == 2:
        return
    else:
        $ disable_current_zone_alt2()
        jump alt_day3_mapAf

label alt_day3_eventAf_dining_hall:
    call alt_day3_eventAf_dining_hall1
    if alt_day3_us_bugs == 1:
        return
    else:
        $ disable_current_zone_alt2()
        jump alt_day3_mapAf

label alt_day3_eventAf_admins:
    call alt_day3_eventAf_admins1
    pause(1)
    call alt_day3_sl_postlunch
    return

label alt_day3_eventAf_me_mt_house:
    call alt_day3_eventAf_me_mt_house1
    return

label alt_day3_eventAf_library:
    call alt_day3_eventAf_library1
    $ disable_current_zone_alt2()
    jump alt_day3_mapAf

label alt_day3_eventAf_estrade:
    call alt_day3_eventAf_estrade1
    if alt_day3_dj == 'mi':
        return
    elif alt_day3_dv_dj_fale and not alt_day3_mi_dj_fale:
        jump alt_day3_day_mi_dj
    elif (alt_day3_dv_dj_fale and alt_day3_mi_dj_fale) or not alt_day3_dv_dj_fale:
        jump alt_day3_eventAf_me_mt_house
    else:
        $ disable_current_zone_alt2()
        jump alt_day3_mapAf
