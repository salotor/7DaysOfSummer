label alt_day5_mi_dj_mapprepare:
    $ day_time()
    $ persistent.sprite_time = "day"
    $ alt_chapter(5, u"Miku. DJ. In search of Miku!")
    $ disable_all_zones_alt2()
    $ disable_all_chibi_alt2()
    $ set_zone_alt2('music_club_alt2',    'alt_day5_mi_dj_music_club')
    $ set_chibi_alt2 ('music_club_alt2',      '?')
    $ set_zone_alt2('clubs_alt2',         'alt_day5_mi_dj_clubs')
    $ set_chibi_alt2 ('clubs_alt2', '?')
    $ set_zone_alt2('camp_entrance_alt2', 'alt_day5_mi_dj_camp_entrance')
    $ set_chibi_alt2 ('camp_entrance_alt2',   '?')
    $ set_zone_alt2('un_mi_house_alt2',   'alt_day5_mi_dj_un_mi_house')
    $ set_chibi_alt2 ('un_mi_house_alt2',     '?')
    $ set_zone_alt2('estrade_alt2',       'alt_day5_mi_dj_estrade')
    $ set_chibi_alt2 ('estrade_alt2',         '?')
    play music music_list["two_glasses_of_melancholy"] fadein 2
    jump alt_day5_mi_dj_map

label alt_day5_mi_dj_map:
    scene black with fade
    if len(list_mi_search_7dl) >= 5:
        "I'm tired, I'm beat, I've ran around this damned camp about a 100 times now…"
        "And nowhere, not in any single place, where the girl could be she either wasn't seen, or she just left."
        "I thought about where else I could go."
        play sound sfx_7dl["eat_horn"] fadein 5
        th "It's almost dinner. How time flies."
        dreamgirl "Going to go eat?"
        th "Uhh, nah. But the camp leader's going to be there. And Slavya. Maybe it's time to ask for help."
        stop sound fadeout 3
        return
    else:
        $ show_map_alt2()

label alt_day5_mi_dj_music_club:
    call alt_day5_mi_dj_music_club1
    $ disable_current_zone_alt2()
    $ list_mi_search_7dl.append('musclub')
    jump alt_day5_mi_dj_map

label alt_day5_mi_dj_clubs:
    call alt_day5_mi_dj_clubs1
    $ disable_current_zone_alt2()
    $ list_mi_search_7dl.append('clubs')
    jump alt_day5_mi_dj_map

label alt_day5_mi_dj_camp_entrance:
    call alt_day5_mi_dj_camp_entrance1
    $ disable_current_zone_alt2()
    $ list_mi_search_7dl.append('entrance')
    jump alt_day5_mi_dj_map

label alt_day5_mi_dj_un_mi_house:
    call alt_day5_mi_dj_un_mi_house1
    $ disable_current_zone_alt2()
    $ list_mi_search_7dl.append('home')
    jump alt_day5_mi_dj_map

label alt_day5_mi_dj_estrade:
    call alt_day5_mi_dj_estrade1
    $ disable_current_zone_alt2()
    $ list_mi_search_7dl.append('estrade')
    if len(list_mi_search_7dl) <= 4:
        play music music_list["two_glasses_of_melancholy"] fadein 2
    else:
        stop music fadeout 6
    jump alt_day5_mi_dj_map
