init 9999 python:
    # Labels

    ## Common
    ### Day 0
    sdl_repl_array_common_day0 = [
        sdl_repl_Label(
            "Loki",
            sdl_Replay("alt_day0_start_l", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Herc",
            sdl_Replay("alt_day0_start_h", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Wimp",
            sdl_Replay("alt_day0_start_d", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            char_mask = 1
        )
    ]
    ### 1 Day
    sdl_repl_array_common_day1 = [
        sdl_repl_Label(
            "Beginning",
            sdl_Replay("alt_day1_begin", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Awakening",
            sdl_Replay(
                        "alt_day1_bus_start", {"alt_replay_on" : "True"},
                        music = music_7dl["areyouabully"],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "First meeting",
            sdl_Replay(
                        "alt_day1_firts_met", {"alt_replay_on" : "True"},
                        meets = {'sl' : 'Blonde'},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Arrival",
            sdl_Replay(
                        "alt_day1_arrival", {"alt_replay_on" : "True"},
                        meets = {'dv' : 'Redhead', 'sl' : 'Blonde', 'un' : 'Sad girl', 'us' : 'Kid'},
                        meet_restr = {'sl' : 'alt_day1_sl_met'},
                        vars = [
                                    sdl_var_b_d1_sl_met,
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Redheads",
            sdl_Replay("alt_day1_chase1", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 6
        ),
        sdl_repl_Label(
            "Warehouse",
            sdl_Replay(
                        "alt_day1_warehouse", {"alt_replay_on" : "True"},
                        meets = {'sl' : 'Blonde'},
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 6
        ),
        sdl_repl_Label(
            "Squad leader",
            sdl_Replay(
                        "alt_day1_mod_tan", {"alt_replay_on" : "True"},
                        meets = {'cs' : 'Nurse', 'mt' : 'Counselor', 'sl' : 'Blonde', 'us' : 'Kid'},
                        meet_restr = {'sl' : 'alt_day1_sl_met'},
                        vars = [
                                    sdl_var_b_d1_sl_met,
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Elektronik",
            sdl_Replay(
                        "alt_day1_elektron", {"alt_replay_on" : "True"},
                        meets = {'el' : "Curly"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Excursion",
            sdl_Replay(
                        "alt_day1_meeting", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Football field",
            sdl_Replay(
                        "alt_day1_soccer_d1", {"alt_replay_on" : "True"},
                        meets = {'us' : 'Kid'},
                        vars = [
                                    sdl_var_b_d1_el_foll,
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay(
                        "alt_day1_supper", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Excursion. Evening",
            sdl_Replay(
                        "alt_day1_meeting2", {"alt_replay_on" : "True"},
                        meets = {'al' : 'Angry boy', 'dn' : 'Curly'},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Chasing",
            sdl_Replay(
                        "alt_day1_chase", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Chasing. Headshot",
            sdl_Replay(
                        "alt_day1_headshot", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Chasing. Too slow!",
            sdl_Replay(
                        "alt_day1_nocatch", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Saviour",
            sdl_Replay(
                        "alt_day1_slavya_saviour", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d1_us_shot
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lena",
            sdl_Replay(
                        "alt_day1_lena", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Light out",
            sdl_Replay(
                        "alt_day1_sleep", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_un,
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    ### 2 Day
    sdl_repl_array_common_day2 = [
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day2_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl,
                                    sdl_var_e_d1_cofr,
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lineup",
            sdl_Replay(
                        "alt_day2_lineup", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_lpp,
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day2_bf", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_un,
                                    sdl_var_i_un_lpp,
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Checklist. Lena",
            sdl_Replay(
                        "alt_day2_un_guide", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_brf
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Checklist. Slavya",
            sdl_Replay("alt_day2_sl_guide", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Checklist. Choice",
            sdl_Replay(
                        "alt_day2_convoy", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key,
                                    sdl_var_i_dv_lpp,
                                    sdl_var_i_sl_lpp,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_e_d1_cofr,
                                    sdl_var_e_d2_brf
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Checklist. Mus. Club",
            sdl_Replay(
                        "alt_day2_event_music_club1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_clt,
                                    sdl_var_e_d2_conv,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Checklist. Mus. Club. Inside",
            sdl_Replay(
                        "alt_day2_inmusic", {"alt_replay_on" : "True"},
                        meets = {'mi' : 'Japanese girl'},
                        vars = [
                                    sdl_var_e_d2_conv,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Checklist. Clubs",
            sdl_Replay(
                        "alt_day2_event_clubs1", {"alt_replay_on" : "True"},
                        meets = {'sh' : 'Nerd'},
                        meet_restr = {'sh' : 'alt_day2_sh_met'},
                        vars = [
                                    sdl_var_b_d2_sh_met,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_i_sl_clt,
                                    sdl_var_e_d2_conv,
                                    sdl_var_l_d2_voya,
                                    sdl_var_l_d2_jclu
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Checklist. Bus stop",
            sdl_Replay("alt_day2_event_camp_entrance1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Checklist. Redheads cabin",
            sdl_Replay(
                        "alt_day2_event_dv_us_house1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d1_us_shot,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_e_d2_conv
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Checklist. Canteen",
            sdl_Replay("alt_day2_event_dining_hall1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Checklist. Football field",
            sdl_Replay(
                        "alt_day2_event_sport_area1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl,
                                    sdl_var_i_sl_clt,
                                    sdl_var_e_d1_sl_key,
                                    sdl_var_e_d2_conv,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Checklist. Beach",
            sdl_Replay(
                        "alt_day2_event_beach1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_conv
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Checklist. Semyon's cabin",
            sdl_Replay("alt_day2_event_me_mt_house1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Checklist. Library",
            sdl_Replay(
                        "alt_day2_event_library1", {"alt_replay_on" : "True"},
                        meets = {'sh' : 'Nerd'},
                        meet_restr = {'sh' : 'alt_day2_sh_met'},
                        vars = [
                                    sdl_var_b_d2_sh_met,
                                    sdl_var_e_d2_conv,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Checklist. Library. Zhenya",
            sdl_Replay(
                        "alt_day2_mz", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_conv,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Checklist. Infirmary",
            sdl_Replay(
                        "alt_day2_event_medic_house1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d1_us_shot,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_e_d2_conv
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Checklist. Square",
            sdl_Replay("alt_day2_event_square_1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_conv,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Checklist. Square. Again",
            sdl_Replay("alt_day2_event_square_dunno", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Checklist. Square. Keys",
            sdl_Replay(
                        "alt_day2_sl_hyst", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Checklist. Pier",
            sdl_Replay(
                        "alt_day2_event_boat_station1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl,
                                    sdl_var_e_d2_conv,
                                    sdl_var_l_d2_jclu
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Checklist. Stage",
            sdl_Replay(
                        "alt_day2_event_estrade", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_clt,
                                    sdl_var_e_d2_conv,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Stage. Looking around",
            sdl_Replay(
                        "alt_day2_dubstep", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_me_mini,
                                    sdl_var_e_d2_conv
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Stage. Microphone",
            sdl_Replay("alt_day2_phone", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Stage. Minijack",
            sdl_Replay(
                        "alt_day2_dubstep2", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d1_us_shot,
                                    sdl_var_e_d2_conv,
                                    sdl_var_l_d2_voya,
                                    sdl_var_l_d2_jclu
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day2_dinner", {"alt_replay_on" : "True"},
                        meets = {'mi' : 'Japanese girl'},
                        meet_restr = {'mi' : 'alt_day2_mi_met'},
                        vars = [
                                    sdl_var_b_d1_el_foll,
                                    sdl_var_b_d1_us_shot,
                                    sdl_var_e_d1_un,
                                    sdl_var_e_d2_mi_date,
                                    sdl_var_b_d2_sh_met,
                                    sdl_var_b_d2_me_mini,
                                    sdl_var_b_d2_us_dubs,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_i_sl_clt,
                                    sdl_var_e_d2_conv,
                                    sdl_var_e_d2_mi_kumu,
                                    sdl_var_l_d2_voya,
                                    sdl_var_l_d2_jclu
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "The Grand Escape",
            sdl_Replay(
                        "alt_day2_grand_escape", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_conv
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Quiet hour",
            sdl_Replay(
                        "alt_day2_siesta", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_dubs,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_e_d2_conv,
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Tournament preparations",
            sdl_Replay(
                        "alt_day2_tournament", {"alt_replay_on" : "True"},
                        meets = {'mi' : 'Japanese girl'},
                        meet_restr = {'mi' : 'alt_day2_mi_met'},
                        vars = [
                                    sdl_var_e_d2_mi_date,
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Cards. Solo",
            sdl_Replay("alt_day2_walk_alone", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Cards. Slavya",
            sdl_Replay(
                        "alt_day2_walk_sl", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl,
                                    sdl_var_l_d1_sl
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Ultimatum",
            sdl_Replay(
                        "alt_day2_ultim", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d1_us_shot,
                                    sdl_var_b_d2_us_dubs,
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_e_d2_conv,
                                    sdl_var_e_d2_walk,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Tournament",
            sdl_Replay(
                        "alt_day2_cards_tournament", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_dv_ulti,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay(
                        "alt_day2_supper", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                    # Tournament int
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Supper. Later",
            sdl_Replay(
                        "alt_day2_sup2", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_us_cake,
                                    sdl_var_i_sl_lpp,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_e_d2_dv_ulti
                                    # Tournament int
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Chasing Ulyana",
            sdl_Replay(
                        "alt_day2_slot_us_try", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_us_lpp
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Supper. Beach",
            sdl_Replay(
                        "alt_day2_eventEv_beach1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_b_d2_dv_chas,
                                    sdl_var_i_dv_lpp,
                                    sdl_var_e_d2_dv_ulti,
                                    sdl_var_l_d2_jclu
                                    # Tournament int
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Supper. Mus. Club",
            sdl_Replay(
                        "alt_day2_eventEv_music_club1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_mi_snap,
                                    sdl_var_i_mi_lpp,
                                    sdl_var_e_d2_conv,
                                    sdl_var_e_d2_mi_kumu,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Evening. Clubs",
            sdl_Replay("alt_day2_eventEv_clubs1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Evening. Bus stop",
            sdl_Replay("alt_day2_eventEv_camp_entrance1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Evening. Canteen",
            sdl_Replay("alt_day2_eventEv_dining_hall1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Evening. Football field",
            sdl_Replay(
                        "alt_day2_eventEv_sport_area1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_lpp,
                                    sdl_var_e_d2_conv,
                                    sdl_var_l_d2_voya
                                    # Tournament int
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Evening. Lena and Miku's cabin",
            sdl_Replay(
                        "alt_day2_eventEv_un_mi_house1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_b_d2_dv_chas,
                                    sdl_var_i_un_lpp,
                                    sdl_var_e_d1_un,
                                    sdl_var_e_d2_brf,
                                    sdl_var_e_d2_conv,
                                    sdl_var_l_d2_voya,
                                    sdl_var_l_d2_club
                                    # Tournament int
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Evening. Redhead's cabin",
            sdl_Replay("alt_day2_eventEv_dv_us_house1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Evening. Olga and Semyon's cabin",
            sdl_Replay(
                        "alt_day2_eventEv_me_mt_house1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_clt
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Evening. Library",
            sdl_Replay("alt_day2_eventEv_library1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Evening. Infirmary",
            sdl_Replay(
                        "alt_day2_eventEv_medic_house1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Evening. Stage",
            sdl_Replay(
                        "alt_day2_eventEv_estrade1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_me_mini
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Evening. Square",
            sdl_Replay(
                        "alt_day2_eventEv_square1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_dv_chas,
                                    sdl_var_i_sl_lpp,
                                    sdl_var_i_sl_clt,
                                    sdl_var_e_d1_sl_key,
                                    sdl_var_e_d2_walk,
                                    sdl_var_l_d1_sl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Evening. Pier",
            sdl_Replay(
                        "alt_day2_eventEv_boat_station1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_dv_chas
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Evening with Miku",
            sdl_Replay(
                        "alt_day2_slot_mi", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_mi_snap,
                                    sdl_var_e_d2_conv,
                                    sdl_var_e_d2_mi_kumu,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Evening with Alisa",
            sdl_Replay(
                        "alt_day2_slot_dv", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_b_d2_dv_chas,
                                    sdl_var_i_dv_lpp,
                                    sdl_var_e_d2_dv_ulti,
                                    sdl_var_l_d2_jclu
                                    # Tournament int
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Evening with Slavya",
            sdl_Replay(
                        "alt_day2_slot_sl", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_clt,
                                    sdl_var_e_d2_walk,
                                    sdl_var_l_d1_sl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Evening with Lena (Loki)",
            sdl_Replay(
                        "alt_day2_un_loki_date", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_b_d2_dv_chas,
                                    sdl_var_e_d1_un,
                                    sdl_var_e_d2_conv,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Evening with Lena (Herc)",
            sdl_Replay(
                        "alt_day2_un_herc_date", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_b_d2_dv_chas,
                                    sdl_var_e_d1_un,
                                    sdl_var_e_d2_brf,
                                    sdl_var_e_d2_conv,
                                    sdl_var_l_d2_voya,
                                    sdl_var_l_d2_club
                                    # Tournament int
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Evening with Lena (Wimp)",
            sdl_Replay(
                        "alt_day2_slot_un", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_evening,
                        vars = [
                                    sdl_var_e_d2_conv,
                                    sdl_var_l_d2_voya
                                    # Tournament int
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Evening with Olga",
            sdl_Replay(
                        "alt_day2_slot_mt", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_clt
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Evening with Ulyana",
            sdl_Replay(
                        "alt_day2_slot_us", {"alt_replay_on" : "True"},
                        vars = None,    # Tournament int
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day2_dream", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_b_d2_mt_help,
                                    sdl_var_e_d2_date,
                                    sdl_var_l_d2_voya
                                    # Tournament int
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    ### 3 Day
    sdl_repl_array_common_day3 = [
        sdl_repl_Label(
            "Morning",
            sdl_Replay("alt_day3_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_mi_date,
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_i_sl_clt,
                                    sdl_var_e_d2_brf,
                                    sdl_var_e_d2_conv,
                                    sdl_var_e_d2_walk,
                                    sdl_var_e_d2_date,
                                    sdl_var_l_d1_sl,
                                    sdl_var_l_d2_club
                                    # Tournament int
                                ],
                        func_in = prolog_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day3_bf", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_i_sl_clt,
                                    sdl_var_e_d2_conv,
                                    sdl_var_e_d2_date,
                                    sdl_var_l_d1_sl,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Duty",
            sdl_Replay(
                        "alt_day3_bf_duty", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl,
                                    sdl_var_i_sl_clt,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d3_date,
                                    sdl_var_l_d2_club
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning. Mus. Club",
            sdl_Replay(
                        "alt_day3_event_music_club1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning. Clubs",
            sdl_Replay(
                        "alt_day3_event_clubs1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_club
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning. Bus stop",
            sdl_Replay(
                        "alt_day3_event_camp_entrance1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_e_d2_conv,
                                    sdl_var_e_d2_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning. Canteen",
            sdl_Replay(
                        "alt_day3_event_dining_hall1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning. Football field",
            sdl_Replay(
                        "alt_day3_event_sport_area1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_voya,
                                    sdl_var_l_d2_club
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning. Beach",
            sdl_Replay(
                        "alt_day3_event_beach1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_e_d1_un,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d3_date,
                                    sdl_var_l_d1_sl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning. Library",
            sdl_Replay(
                        "alt_day3_event_library1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_e_d3_date,
                                    sdl_var_l_d2_voya,
                                    sdl_var_l_d2_club
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning. Infirmary",
            sdl_Replay(
                        "alt_day3_event_medic_house1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning. Stage",
            sdl_Replay(
                        "alt_day3_event_estrade1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_me_mini,
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_i_dv_lpp,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d2_mi_date,
                                    sdl_var_e_d3_date,
                                    sdl_var_l_d2_voya,
                                    sdl_var_l_d2_jclu
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning. Square",
            sdl_Replay("alt_day3_event_square1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Morning. Pier",
            sdl_Replay("alt_day3_event_boat_station1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Morning with Miku",
            sdl_Replay(
                        "alt_day3_morning_mi", {"alt_replay_on" : "True"},
                        music = music_7dl["tellyourworld"],
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_e_d2_mi_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning with Alisa",
            sdl_Replay(
                        "alt_day3_morning_dv", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_l_d2_voya,
                                    sdl_var_l_d2_jclu
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning with Slavya",
            sdl_Replay(
                        "alt_day3_morning_sl", {"alt_replay_on" : "True"},
                        music = music_list["take_me_beautifully"],
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_e_d1_un,
                                    sdl_var_e_d2_date,
                                    sdl_var_l_d1_sl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning with Lena",
            sdl_Replay(
                        "alt_day3_morning_un", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_b_d2_us_esca
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Operation «Ы»",
            sdl_Replay(
                        "alt_day3_morning_un_fz", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_conv
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day3_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_shen,
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_i_un_lpp,
                                    sdl_var_i_sl_clt,
                                    sdl_var_i_un_fzd,
                                    sdl_var_e_d2_brf,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d3_date,
                                    sdl_var_l_d2_voya,
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Day. Clubs",
            sdl_Replay("alt_day3_eventAf_clubs_technoquest", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Day. Clubs. Again",
            sdl_Replay(
                        "alt_day3_eventAf_clubs_ladder", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_me_tec1,
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Day. Mus. club",
            sdl_Replay(
                        "alt_day3_eventAf_music_club1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_b_d3_mi_reje,
                                    sdl_var_i_un_lpp,
                                    sdl_var_i_dv_7dl,
                                    sdl_var_i_un_fzd,
                                    sdl_var_l_d2_voya,
                                    sdl_var_l_d2_club
                                    # Tournament int
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Day. Lena and Miku's cabin",
            sdl_Replay(
                        "alt_day3_eventAf_un_mi_house1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_mi_lpp,
                                    sdl_var_i_mi_7dl,
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_e_d2_date
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Day. Canteen",
            sdl_Replay(
                        "alt_day3_eventAf_dining_hall1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Day. Admin. building",
            sdl_Replay(
                        "alt_day3_eventAf_admins1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_mi_snap,
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_e_d2_walk,
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Day. Olga and Semyon's cabin",
            sdl_Replay("alt_day3_eventAf_me_mt_house1", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Day. Library",
            sdl_Replay(
                        "alt_day3_eventAf_library1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_mi_lpp,
                                    sdl_var_i_dv_lpp,
                                    sdl_var_i_sl_lpp,
                                    sdl_var_i_un_7dl,
                                    sdl_var_e_d2_brf
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Day. Stage",
            sdl_Replay(
                        "alt_day3_eventAf_estrade1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_sl_invi,
                                    sdl_var_i_mi_7dl,
                                    sdl_var_e_d2_brf,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d3_date,
                                    sdl_var_e_d3_dv_guit,
                                    sdl_var_e_d3_dj
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Choosing a DJ. Miku",
            sdl_Replay(
                        "alt_day3_day_mi_dj", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_mi_7dl,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d3_date
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Choosing a DJ. Alisa",
            sdl_Replay(
                        "alt_day3_day_dv_dj", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_dv_guit
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Day with Miku",
            sdl_Replay(
                        "alt_day3_day_mi", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_i_mi_lpp,
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_e_d2_date
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Day with Alisa",
            sdl_Replay(
                        "alt_day3_day_dv", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_b_d3_mi_reje
                                    # Tournament int
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Day with Lena",
            sdl_Replay(
                        "alt_day3_day_un", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_i_mi_lpp,
                                    sdl_var_i_dv_lpp,
                                    sdl_var_i_sl_lpp,
                                    sdl_var_e_d2_brf
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
         sdl_repl_Label(
            "Day. Friendzone",
            sdl_Replay("alt_day3_day_un_fz", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 2
         ),
         sdl_repl_Label(
            "Preparations with Alisa",
            sdl_Replay(
                        "alt_day3_day_un_fz_dv", {"alt_replay_on" : "True"},
                        meets = {'dn' : 'Curly', 'ka' : 'Counselor of squad 2'},
                        music = music_list["so_good_to_be_careless"],
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_l_d2_voya
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
         ),
         sdl_repl_Label(
            "Preparations with Slavya",
            sdl_Replay(
                        "alt_day3_day_un_fz_sl", {"alt_replay_on" : "True"},
                        music = music_list["so_good_to_be_careless"],
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
         ),
         sdl_repl_Label(
            "Preparations with Lena",
            sdl_Replay(
                        "alt_day3_day_un_fz_un", {"alt_replay_on" : "True"},
                        music = music_list["so_good_to_be_careless"],
                        ambience = ambience_camp_center_day,
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
         ),
        sdl_repl_Label(
            "Lunch with Slavya",
            sdl_Replay(
                        "alt_day3_sl_postlunch", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_i_sl_clt
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lunch with Ulyana",
            sdl_Replay(
                        "alt_day3_aftermath", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_i_un_fzd,
                                    sdl_var_i_un_fzd_dv,
                                    sdl_var_b_d2_us_shen,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d3_us_bugs

                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Nightmare",
            sdl_Replay(
                        "alt_day3_nightmare", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_b_d2_us_esca
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Evening. Friendzone",
            sdl_Replay(
                        "alt_day3_un_fz_dream", {"alt_replay_on" : "True"},
                        music = music_list["trapped_in_dreams"],
                        vars = [
                                    sdl_var_i_un_fzd_ol,
                                    sdl_var_e_d3_un_fz_work
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Dream. Lena",
            sdl_Replay("alt_day3_un_fz_dream_un", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Dream. The Road",
            sdl_Replay("alt_day3_un_fz_dream_road", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay(
                        "alt_day3_supper", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_mi_7dl,
                                    sdl_var_i_sl_clt,
                                    sdl_var_i_un_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Supper with Ulyana",
            sdl_Replay(
                        "alt_day3_supper1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty,
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Supper. Continued",
            sdl_Replay(
                        "alt_day3_supper2", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_i_mi_7dl,
                                    sdl_var_i_dv_7dl,
                                    sdl_var_i_sl_clt,
                                    sdl_var_e_d3_dj
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Supper. Friendzone",
            sdl_Replay(
                        "alt_day3_un_fz_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_un_fz_work
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Disco. Beginning",
            sdl_Replay(
                        "alt_day3_dance_dance", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_mi_7dl,
                                    sdl_var_i_un_fzd,
                                    sdl_var_e_d3_dv_guit,
                                    sdl_var_e_d3_un_medh,
                                    sdl_var_e_d3_dj,
                                    sdl_var_e_d3_me_tec1
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Disco. Makeup",
            sdl_Replay(
                        "alt_day3_makeup", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_mi_7dl,
                                    sdl_var_i_dv_7dl,
                                    sdl_var_i_un_fzd,
                                    sdl_var_e_d3_dv_guit
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "First dance",
            sdl_Replay(
                        "alt_day3_choose", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_sl_invi,
                                    sdl_var_i_mi_lpp,
                                    sdl_var_i_sl_lpp,
                                    sdl_var_i_mi_7dl,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_i_sl_clt,
                                    sdl_var_i_un_7dl,
                                    sdl_var_e_d2_brf,
                                    sdl_var_e_d2_walk,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d3_un_medh,
                                    sdl_var_e_d3_dj
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Between dances",
            sdl_Replay(
                        "alt_day3_dance_dance2", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_evening,
                        vars = [
                                    sdl_var_i_mi_lpp,
                                    sdl_var_i_dv_lpp,
                                    sdl_var_i_sl_lpp,
                                    sdl_var_i_un_lpp,
                                    sdl_var_i_sl_clt,
                                    sdl_var_e_d3_us_bugs,
                                    sdl_var_e_d3_un_medh,
                                    sdl_var_e_d3_dj,
                                    sdl_var_e_d3_me_tec1,
                                    sdl_var_e_d3_me_dan1
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Second dance",
            sdl_Replay(
                        "alt_day3_choose2", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_evening,
                        vars = [
                                    sdl_var_i_un_lpp,
                                    sdl_var_i_mi_7dl,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_i_sl_clt,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d2_mi_date,
                                    sdl_var_e_d3_un_medh,
                                    sdl_var_e_d3_dj,
                                    sdl_var_e_d3_me_dan1
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Disco. Ending",
            sdl_Replay(
                        "alt_day3_disco_past_d2", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_evening,
                        vars = [
                                    sdl_var_e_d2_walk,
                                    sdl_var_e_d3_dj
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Alisa ending",
            sdl_Replay(
                        "alt_day3_dv_lf", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_me_mini,
                                    sdl_var_e_d1_un,
                                    sdl_var_e_d2_conv,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d3_dv_guit
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Alisa. Catapult",
            sdl_Replay(
                        "alt_day3_dv_reunion", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d1_el_foll
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Alisa. Reunion",
            sdl_Replay(
                        "alt_day3_dv_stayhere1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_e_d2_date
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Infirmary with Lena",
            sdl_Replay(
                        "alt_day3_med_un", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty,
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lena. Strip cards",
            sdl_Replay(
                        "alt_day3_un_cards", {"alt_replay_on" : "True"},
                        vars = [
                                    # Tournament int
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lena. After the infirmary",
            sdl_Replay(
                        "alt_day3_post_strip", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_un_stri
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Disco. Friendzone",
            sdl_Replay(
                        "alt_day3_un_fz_dance", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_un_fz_work
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Walk with Lena",
            sdl_Replay(
                        "alt_day3_un_fz_evening_walk", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_un_fz_work
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Fairy tale about The Road",
            sdl_Replay("alt_day3_un_fz_evening_stories", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Dance with Lena",
            sdl_Replay(
                        "alt_day3_un_fz_dance2", {"alt_replay_on" : "True"},
                        music = music_7dl["shape_of_my_heart"],
                        vars = [
                                    sdl_var_e_d3_un_fz_work
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Miku. Trip to the town",
            sdl_Replay(
                        "alt_day3_mi_7dl_init", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_mi_spt
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Grand revenge",
            sdl_Replay(
                        "alt_day3_mt_scare", {"alt_replay_on" : "True"},
                        music = music_7dl["genki"],
                        ambience = ambience_camp_center_evening,
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Technoquest",
            sdl_Replay(
                        "alt_day3_technoquest3", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_clt,
                                    sdl_var_e_d3_me_tec1,
                                    sdl_var_e_d3_me_dan1
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Bathhouse",
            sdl_Replay(
                        "alt_day3_bath_voyeur", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_mi_7dl,
                                    sdl_var_i_dv_7dl,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_i_un_7dl,
                                    sdl_var_e_d3_me_dan1,
                                    sdl_var_e_d3_me_dan2
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day3_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_b_d3_sl_invi,
                                    sdl_var_b_d3_sl_bath,
                                    sdl_var_i_un_lpp,
                                    sdl_var_i_mi_7dl,
                                    sdl_var_i_dv_7dl,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_i_sl_clt,
                                    sdl_var_i_un_7dl,
                                    sdl_var_e_d2_brf,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d3_date,
                                    sdl_var_e_d3_dv_guit,
                                    sdl_var_e_d3_us_bugs,
                                    sdl_var_e_d3_dj,
                                    sdl_var_e_d3_me_tec1,
                                    sdl_var_e_d3_me_dan1,
                                    sdl_var_e_d3_me_dan2
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lights out. Friendzone",
            sdl_Replay(
                        "alt_day3_un_fz_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_un_fz_stories,
                                    sdl_var_b_d3_un_fz_transit,
                                    sdl_var_e_d3_un_fz_work
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        )
    ]

    ## Miku
    ### Miku-7DS
    #### 4 Day
    sdl_repl_array_mi_7dl_day4 = [
        sdl_repl_Label(
            "Trip",
            sdl_Replay(
                        "alt_day4_mi_7dl_ch1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_mi_7dl_dono
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day4_mi_7dl_ch2", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_mi_7dl_dono
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Miku-donor",
            sdl_Replay("alt_day4_mi_7dl_ch3", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "To the town!",
            sdl_Replay(
                        "alt_day4_mi_7dl_ch4", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_mi_7dl_dono
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Town. Olga's apartment",
            sdl_Replay(
                        "alt_day4_mi_7dl_ch5a", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_dv_hous
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Town. Walk with Miku",
            sdl_Replay(
                        "alt_day4_mi_7dl_ch5b", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_mi_7dl_dono
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Town. Sakishita",
            sdl_Replay(
                        "alt_day4_mi_7dl_ch52", {"alt_replay_on" : "True"},
                        ambience = ambience_7dl["town_day"],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Home sweet home",
            sdl_Replay(
                        "alt_day4_mi_7dl_ch6", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_mi_7dl_dono
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Evening",
            sdl_Replay(
                        "alt_day4_mi_7dl_ch7", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_mi_7dl_dono
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Miku's story",
            sdl_Replay(
                        "alt_day4_mi_7dl_ch8b", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_mi_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Rendezvous?",
            sdl_Replay(
                        "alt_day4_mi_7dl_ch8a", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Rendezvous. Herc",
            sdl_Replay("alt_day4_mi_7dl_ch81", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Rendezvous. Loki",
            sdl_Replay("alt_day4_mi_7dl_ch82", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay("alt_day4_mi_7dl_ch83", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        )
    ]
    #### 5 Day
    sdl_repl_array_mi_7dl_day5 = [
        sdl_repl_Label(
            "Rain together",
            sdl_Replay("alt_day5_mi_7dl_rain_2gether", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day5_mi_7dl_morning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_mi_7dl_dono
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day5_mi_7dl_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_7dl_savi
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Day",
            sdl_Replay(
                        "alt_day5_mi_7dl_router", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_7dl_savi
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Bathhouse",
            sdl_Replay("alt_day5_mi_7dl_lost", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Hentai",
            sdl_Replay("alt_day5_mi_7dl_hn", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Pier",
            sdl_Replay("alt_day5_mi_7dl_branch", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "GentleSemen",
            sdl_Replay(
                        "alt_day5_mi_7dl_potato", {"alt_replay_on" : "True"},
                        meets = {'uv' : 'Catgirl'},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Fire glade cleaning",
            sdl_Replay("alt_day5_mi_7dl_camp_cleance", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Hike",
            sdl_Replay(
                        "alt_day5_mi_7dl_firecamp", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_mi_7dl_voye,
                                    sdl_var_i_mi_hpt,
                                    sdl_var_e_d2_mi_date,
                                    sdl_var_e_d3_mi_7dl_dono,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day5_mi_7dl_goodnight", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_mi_7dl_voye
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 6 Day
    sdl_repl_array_mi_7dl_day6 = [
        sdl_repl_Label(
            "Morning",
            sdl_Replay("alt_day6_mi_7dl_wakeup", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Soul. Time capsule",
            sdl_Replay(
                        "alt_day6_mi_7dl_soul", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Star. Civil evening",
            sdl_Replay("alt_day6_mi_7dl_star", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Human. On a boat",
            sdl_Replay(
                        "alt_day6_mi_7dl_human", {"alt_replay_on" : "True"},
                        meets = {'bb' : 'Camp Leader'},
                        vars = [
                                    sdl_var_b_d2_mi_snap,
                                    sdl_var_e_d3_mi_7dl_dono
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day6_mi_7dl_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_mi_7dl_voye
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Soul. Hentai",
            sdl_Replay(
                        "alt_day6_mi_7dl_soul_day", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_7dl_savi
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Star. Mini-Concert",
            sdl_Replay("alt_day6_mi_7dl_star_day", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Miku's departure",
            sdl_Replay(
                        "alt_day6_mi_7dl_miku_sakishita", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_mi_7dl_voye,
                                    sdl_var_e_d2_mi_date
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Farewell Miku",
            sdl_Replay(
                        "alt_day6_mi_7dl_miku_farewell_finale", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_mi_snap
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Soul. Farewell",
            sdl_Replay(
                        "alt_day6_mi_7dl_miku_farewell_soul", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_mi_date
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Star. Farewell",
            sdl_Replay(
                        "alt_day6_mi_7dl_miku_farewell_star", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_mi_snap
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Human. Miku stays",
            sdl_Replay(
                        "alt_day6_mi_7dl_human_day", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_mi_7dl_dono
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Catapult",
            sdl_Replay("alt_day6_mi_7dl_catapult", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Disco",
            sdl_Replay(
                        "alt_day6_mi_7dl_discoteque", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_mi_7dl_left
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Hentai",
            sdl_Replay(
                        "alt_day6_mi_7dl_hentai", {"alt_replay_on" : "True"},
                        music = music_7dl["sam_lullaby"],
                        ambience = ambience_lake_shore_night,
                        vars = [
                                    sdl_var_b_d5_mi_7dl_kiss,
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 7 Day
    sdl_repl_array_mi_7dl_day7 = [
        sdl_repl_Label(
            "Dream",
            sdl_Replay("alt_day7_mi_7dl_begin", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day7_mi_7dl_wakeup", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_mi_7dl_left,
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Packing",
            sdl_Replay(
                        "alt_day7_mi_7dl_packing", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_mi_7dl_left,
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Departure. Alone",
            sdl_Replay("alt_day7_mi_7dl_departure_lone", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Departure. Miku",
            sdl_Replay(
                        "alt_day7_mi_7dl_departure_a2th", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_mi_lpp,
                                    sdl_var_i_mi_hpt
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    ### Miku-DJ
    #### 4 Day
    sdl_repl_array_mi_djt_day4 = [
        sdl_repl_Label(
            "Night",
            sdl_Replay(
                        "alt_day4_mi_dj_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_conv
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Hunting the predator",
            sdl_Replay(
                        "alt_day4_mi_dj_hedg_hunt", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_mi_kumu
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day4_mi_dj_morning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_dj_hedg
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Day start",
            sdl_Replay(
                        "alt_day4_mi_dj_day", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Radio room",
            sdl_Replay(
                        "alt_day4_mi_dj_radio", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_me_mini,
                                    sdl_var_b_d4_mi_dj_hedg
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Radio room. Cleaning",
            sdl_Replay(
                        "alt_day4_mi_dj_cleaning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_dj_hedg,
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_e_d2_mi_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day4_mi_dj_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_dj_hedg,
                                    sdl_var_e_d3_me_tec1
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dinner with Slavya",
            sdl_Replay(
                        "alt_day4_mi_dj_dinner2", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_dj_sl_blac
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Rehearsal",
            sdl_Replay(
                        "alt_day4_mi_dj_repetition", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_dj_sl_repe,
                                    sdl_var_b_d4_mi_dj_reas
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Volleyball",
            sdl_Replay(
                        "alt_day4_mi_dj_volley", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_b_d4_mi_dj_sl_repe
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day4_mi_dj_supper", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_dj_hedg,
                                    sdl_var_b_d4_mi_dj_sl_repe,
                                    sdl_var_e_d2_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Evening",
            sdl_Replay(
                        "alt_day4_mi_dj_evening", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_dj_hedg,
                                    sdl_var_b_d4_mi_dj_sl_repe,
                                    sdl_var_e_d2_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Night date",
            sdl_Replay(
                        "alt_day4_mi_dj_night", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_dj_hedg,
                                    sdl_var_e_d2_mi_date,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day4_mi_dj_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_dj_hedg,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d2_mi_date,
                                    sdl_var_e_d3_me_tec1
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 5 Day
    sdl_repl_array_mi_djt_day5 = [
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day5_mi_dj_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_dj_hedg,
                                    sdl_var_e_d3_me_tec1
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day5_mi_dj_breakfast", {"alt_replay_on" : "True"},
                        music = music_list["reflection_on_water"],
                        vars = [
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d3_me_tec1
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Movie",
            sdl_Replay("alt_day5_mi_dj_cinema", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay("alt_day5_mi_dj_dinner", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Jammer",
            sdl_Replay(
                        "alt_day5_mi_dj_jammer", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_dj_sl_repe,
                                    sdl_var_e_d3_me_tec1
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Vocaloidrama",
            sdl_Replay("alt_day5_mi_dj_vocadrama", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Searchings. Mus. Club",
            sdl_Replay(
                        "alt_day5_mi_dj_music_club1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d5_mi_dj_sear
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Searchings. Radioroom",
            sdl_Replay("alt_day5_mi_dj_clubs1", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Searchings. Bus stop",
            sdl_Replay(
                        "alt_day5_mi_dj_camp_entrance1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_mt_help,
                                    sdl_var_l_d5_mi_dj_sear
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Searchings. Miku's house",
            sdl_Replay(
                        "alt_day5_mi_dj_un_mi_house1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d5_mi_dj_sear
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Searchings. Stage",
            sdl_Replay("alt_day5_mi_dj_estrade1", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay("alt_day5_mi_dj_supper", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Fire",
            sdl_Replay(
                        "alt_day5_mi_dj_campfire", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_dj_hedg
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Shower. Miku",
            sdl_Replay("alt_day5_mi_dj_voyeur_4", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Shower. Alisa",
            sdl_Replay(
                        "alt_day5_mi_dj_voyeur_2", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_mi_dj_dv_blad,
                                    sdl_var_e_d3_me_tec1
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Shower. Slavya",
            sdl_Replay("alt_day5_mi_dj_voyeur_3", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Talk",
            sdl_Replay(
                        "alt_day5_mi_dj_late_evening", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_mi_dj_dv_blad,
                                    sdl_var_e_d5_mi_dj_voye
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Reconciliation",
            sdl_Replay(
                        "alt_day5_mi_dj_evening_club1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_mi_dj_dv_blad
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "«Watching the movie»",
            sdl_Replay("alt_day5_mi_dj_evening_club2", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Hentai",
            sdl_Replay(
                        "alt_day5_mi_dj_hentai", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_me_dan2
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day5_mi_dj_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_mi_dj_dv_blad,
                                    sdl_var_e_d5_mi_dj_apol,
                                    sdl_var_e_d5_mi_dj_voye
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 6 Day
    sdl_repl_array_mi_djt_day6 = [
        sdl_repl_Label(
            "Morning. Together",
            sdl_Replay(
                        "alt_day6_mi_dj_good", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d5_mi_dj_voye
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning. Alone",
            sdl_Replay(
                        "alt_day6_mi_dj_neutral", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_mi_dj_dv_blad,
                                    sdl_var_b_d5_mi_dj_dv_kiss,
                                    sdl_var_e_d5_mi_dj_voye
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day6_mi_dj_neutral_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d5_mi_dj_apol
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Broadcasting!",
            sdl_Replay(
                        "alt_day6_mi_dj_radio", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_dj_hedg,
                                    sdl_var_b_d5_mi_dj_dv_kiss,
                                    sdl_var_b_d5_mi_dj_hent,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d3_me_dan1,
                                    sdl_var_e_d3_me_dan2
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay("alt_day6_mi_dj_dinner", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Date",
            sdl_Replay(
                        "alt_day6_mi_dj_rendezvous", {"alt_replay_on" : "True"},
                        music = music_list["everyday_theme"],
                        ambience = ambience_dining_hall_full,
                        vars = [
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_e_d5_mi_dj_apol,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Farewell",
            sdl_Replay(
                        "alt_day6_mi_dj_forgiveness", {"alt_replay_on" : "True"},
                        music = music_list["everyday_theme"],
                        ambience = ambience_dining_hall_full,
                        vars = [
                                    sdl_var_b_d5_mi_dj_dv_kiss,
                                    sdl_var_e_d5_mi_dj_voye
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Miku's story",
            sdl_Replay(
                        "alt_day6_mi_dj_tale", {"alt_replay_on" : "True"},
                        music = music_list["everyday_theme"],
                        ambience = ambience_dining_hall_full,
                        vars = [
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d2_mi_date
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Quiet hour",
            sdl_Replay(
                        "alt_day6_mi_dj_plain", {"alt_replay_on" : "True"},
                        music = music_list["everyday_theme"],
                        ambience = ambience_dining_hall_full,
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Concert",
            sdl_Replay(
                        "alt_day6_mi_dj_concert", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d5_mi_dj_voye
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Speakers. Dragging",
            sdl_Replay(
                        "alt_day6_mi_dj_sonic", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_dubs,
                                    sdl_var_b_d6_mi_dj_walk
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Speakers. Drag evasion",
            sdl_Replay("alt_day6_mi_dj_reject", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Newspaper",
            sdl_Replay("alt_day6_mi_dj_newswall", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay("alt_day6_mi_dj_supper", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Late supper with Slavya",
            sdl_Replay(
                        "alt_day6_mi_dj_late_supper_sl", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_dj_hedg,
                                    sdl_var_b_d5_mi_dj_hent,
                                    sdl_var_e_d3_me_tec1
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Late supper with Lena",
            sdl_Replay(
                        "alt_day6_mi_dj_late_supper_un", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_mi_dj_hent
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Disco",
            sdl_Replay(
                        "alt_day6_mi_dj_discotheque", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_mi_dj_walk
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "First dance",
            sdl_Replay(
                        "alt_day6_mi_dj_first_dance", {"alt_replay_on" : "True"},
                        music = music_list["waltz_of_doubts"],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Second dance",
            sdl_Replay(
                        "alt_day6_mi_dj_second_dance", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_mi_dj_sl_evil,
                                    sdl_var_b_d6_mi_dj_un_evil,
                                    sdl_var_i_mi_lpp,
                                    sdl_var_e_d5_mi_dj_apol
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Second dance. Success",
            sdl_Replay("alt_day6_mi_dj_dance2_success", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Second dance. Failure",
            sdl_Replay(
                        "alt_day6_mi_dj_dance2_fail", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_mi_dj_sl_evil,
                                    sdl_var_b_d6_mi_dj_un_evil,
                                    sdl_var_b_d6_mi_dj_me_evil,
                                    sdl_var_e_d5_mi_dj_apol
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Escape from dances",
            sdl_Replay(
                        "alt_day6_mi_dj_escape", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Catapult",
            sdl_Replay(
                        "alt_day6_mi_dj_catapult", {"alt_replay_on" : "True"},
                        music = music_7dl["unforgotten"],
                        vars = [
                                    sdl_var_b_d6_mi_dj_sl_evil,
                                    sdl_var_b_d6_mi_dj_mi_reje,
                                    sdl_var_e_d5_mi_dj_voye,
                                    sdl_var_e_d5_mi_dj_apol
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Hentai",
            sdl_Replay(
                        "alt_day6_mi_dj_hentai", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day6_mi_dj_sleeptime", {"alt_replay_on" : "True"},
                        music = music_list["a_promise_from_distant_days"],
                        ambience = ambience_camp_center_night,
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 7 Day
    sdl_repl_array_mi_djt_day7 = [
        sdl_repl_Label(
            "Morning. Together",
            sdl_Replay(
                        "alt_day7_mi_dj_together", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_mi_dj_hent
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning. Alone",
            sdl_Replay(
                        "alt_day7_mi_dj_alone", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_mi_dj_hent,
                                    sdl_var_e_d6_mi_dj_cata
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Toxicosis",
            sdl_Replay(
                        "alt_day7_mi_dj_badfeel", {"alt_replay_on" : "True"},
                        music = music_list["everyday_theme"],
                        ambience = ambience_camp_center_evening,
                        vars = [
                                    sdl_var_b_d6_mi_dj_hent,
                                    sdl_var_e_d6_mi_dj_feed
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay("alt_day7_mi_dj_breakfast", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Gatherings",
            sdl_Replay(
                        "alt_day7_mi_dj_preparations", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_mi_dj_hent,
                                    sdl_var_e_d6_mi_dj_feed
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Departure",
            sdl_Replay(
                        "alt_day7_mi_dj_departure", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_mi_dj_cata
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Freezing without you",
            sdl_Replay(
                        "alt_day7_mi_dj_epilogue_frost", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_mi_dj_walk,
                                    sdl_var_e_d6_mi_dj_cata
                                ],
                        func_in = prolog_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "World went crazy",
            sdl_Replay("alt_day7_mi_dj_good", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load)
        )
    ]

    ## Alisa
    ### Alisa-7DS
    #### 4 Day
    sdl_repl_array_dv_7dl_day4 = [
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day4_dv_7dl_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Hike",
            sdl_Replay(
                        "alt_day4_dv_7dl_forest", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d1_us_shot,
                                    sdl_var_b_d2_me_mini,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_e_d2_conv
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay("alt_day4_dv_7dl_dinner", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Quiet hour",
            sdl_Replay(
                        "alt_day4_dv_7dl_silent_hour", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key,
                                    sdl_var_b_d2_us_esca
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Quiet hour",
            sdl_Replay(
                        "alt_day4_dv_7dl_repetition", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_lpp,
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lunch",
            sdl_Replay(
                        "alt_day4_dv_7dl_lunch", {"alt_replay_on" : "True"},
                        music = music_list["so_good_to_be_careless"],
                        ambience = ambience_camp_center_day,
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Viola's request",
            sdl_Replay(
                        "alt_day4_dv_7dl_help", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_voya,
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Trip",
            sdl_Replay(
                        "alt_day4_dv_7dl_roadtrip", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_i_karma
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Port Wine",
            sdl_Replay(
                        "alt_day4_dv_7dl_alco", {"alt_replay_on" : "True"},
                        music = music_list["into_the_unknown"],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Way back",
            sdl_Replay("alt_day4_dv_7dl_back_to_camp", {"alt_replay_on" : "True"})
        ),
        sdl_repl_Label(
            "Medications",
            sdl_Replay(
                        "alt_day4_dv_7dl_append", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Medications. Olga's house",
            sdl_Replay("alt_day4_dv_7dl_mt_aid", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Medications. Infirmary",
            sdl_Replay("alt_day4_dv_7dl_aidpost", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Hentai",
            sdl_Replay("alt_day4_dv_7dl_hentai", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay(
                        "alt_day4_dv_7dl_supper", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_dv_7dl_medi
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day4_dv_7dl_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_dv_7dl_medi
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 5 Day
    sdl_repl_array_dv_7dl_day5 = [
        sdl_repl_Label(
            "The Hangover",
            sdl_Replay(
                        "alt_day5_dv_7dl_alco_morning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_dv_7dl_hent
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day5_dv_7dl_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_dv_7dl_medi,
                                    sdl_var_e_d4_dv_7dl_vodk
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Return",
            sdl_Replay("alt_day5_dv_7dl_roadtrip", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Candle",
            sdl_Replay(
                        "alt_day5_dv_7dl_candle", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_dv_7dl_cs_help
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day5_dv_7dl_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_dv_7dl_vodk
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Quiet hour",
            sdl_Replay(
                        "alt_day5_dv_7dl_silent_hour", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_dv_7dl_cs_help,
                                    sdl_var_b_d2_us_shen,
                                    sdl_var_e_d4_dv_7dl_vodk
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lunch",
            sdl_Replay(
                        "alt_day5_dv_7dl_lunch", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_dv_7dl_cs_help,
                                    sdl_var_e_d4_dv_7dl_vodk
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Rehearsal",
            sdl_Replay(
                        "alt_day5_dv_7dl_repetition", {"alt_replay_on" : "True"},
                        music = music_list["my_daily_life"],
                        vars = [
                                    sdl_var_b_d2_me_mini,
                                    sdl_var_b_d2_us_esca
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay("alt_day5_dv_7dl_supper", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Evening",
            sdl_Replay("alt_day5_dv_7dl_evening", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Fire",
            sdl_Replay(
                        "alt_day5_dv_7dl_campfire", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_dv_7dl_cs_help
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Night date",
            sdl_Replay(
                        "alt_day5_dv_7dl_night", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_dv_7dl_cs_help,
                                    sdl_var_b_d4_dv_7dl_hent,
                                    sdl_var_e_d4_dv_7dl_vodk
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day5_dv_7dl_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_dv_7dl_cs_help,
                                    sdl_var_e_d4_dv_7dl_vodk
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 6 Day
    sdl_repl_array_dv_7dl_day6 = [
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day6_dv_7dl_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_dv_7dl_extr,
                                    sdl_var_b_d4_dv_7dl_port,
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Viola's task",
            sdl_Replay(
                        "alt_day6_dv_7dl_mission", {"alt_replay_on" : "True"},
                        music = music_list["my_daily_life"],
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_b_d4_dv_7dl_cs_help,
                                    sdl_var_b_d4_dv_7dl_port
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day6_dv_7dl_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_b_d4_dv_7dl_cs_help,
                                    sdl_var_b_d4_dv_7dl_port
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Rehearsal",
            sdl_Replay(
                        "alt_day6_dv_7dl_repetition", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day6_dv_7dl_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_b_d4_dv_7dl_ba_conv,
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Slavya",
            sdl_Replay(
                        "alt_day6_dv_7dl_sl", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_cofr,
                                    sdl_var_e_d2_date
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Slavya. Agreed to help",
            sdl_Replay(
                        "alt_day6_dv_7dl_sl_help", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_dv_7dl_hent
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Slavya. Helping",
            sdl_Replay("alt_day6_dv_7dl_sl_help2", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Slavya. Backroom",
            sdl_Replay(
                        "alt_day6_dv_7dl_sl_garret", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_dv_7dl_cs_help,
                                    sdl_var_i_dv_lpp,
                                    sdl_var_i_sl_lpp,
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lena",
            sdl_Replay("alt_day6_dv_7dl_un", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Lena. Meeting",
            sdl_Replay(
                        "alt_day6_dv_7dl_check", {"alt_replay_on" : "True"},
                        ambience = ambience_forest_day,
                        vars = [
                                    sdl_var_i_dv_lpp,
                                    sdl_var_i_un_lpp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Concert",
            sdl_Replay(
                        "alt_day6_dv_7dl_concert", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_dv_7dl_tran,
                                    sdl_var_e_d1_sl_key,
                                    sdl_var_e_d6_dv_7dl_rout
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay(
                        "alt_day6_dv_7dl_supper", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_dv_7dl_tran
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Disco",
            sdl_Replay(
                        "alt_day6_dv_7dl_dance", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_dv_7dl_tran,
                                    sdl_var_e_d6_dv_7dl_rout
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dance with Alisa",
            sdl_Replay("alt_day6_dv_7dl_dv_dancing", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Hentai",
            sdl_Replay(
                        "alt_day6_dv_7dl_love_scene", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_dv_7dl_port,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "No Sex???",
            sdl_Replay(
                        "alt_day6_dv_7dl_non_love", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_dv_7dl_hent
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Catapult",
            sdl_Replay(
                        "alt_day6_dv_7dl_catapult", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_mi_lpp,
                                    sdl_var_i_sl_lpp,
                                    sdl_var_i_un_lpp,
                                    sdl_var_e_d6_dv_7dl_rout
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Back to the dance",
            sdl_Replay(
                        "alt_day6_dv_7dl_predance", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_me_mini,
                                    sdl_var_b_d4_dv_7dl_ba_conv,
                                    sdl_var_b_d4_dv_7dl_port,
                                    sdl_var_i_mi_lpp,
                                    sdl_var_i_sl_lpp,
                                    sdl_var_e_d4_dv_7dl_vodk
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dance with Slavya",
            sdl_Replay(
                        "alt_day6_dv_7dl_sl_dancing", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_brf
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dance with Lena",
            sdl_Replay("alt_day6_dv_7dl_un_dancing", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Dance with Olga",
            sdl_Replay(
                        "alt_day6_dv_7dl_mt_dancing", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_me_mini,
                                    sdl_var_b_d4_dv_7dl_ba_conv,
                                    sdl_var_b_d4_dv_7dl_port,
                                    sdl_var_i_mi_lpp,
                                    sdl_var_i_sl_lpp,
                                    sdl_var_e_d4_dv_7dl_vodk
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day6_dv_7dl_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_dv_7dl_port,
                                    sdl_var_b_d6_dv_7dl_tran,
                                    sdl_var_e_d6_dv_7dl_rout,
                                    sdl_var_e_d6_dv_7dl_danc,
                                    sdl_var_e_d6_dv_7dl_hent
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 7 Day
    sdl_repl_array_dv_7dl_day7 = [
        sdl_repl_Label(
            "Dream",
            sdl_Replay("alt_day7_dv_7dl_begin", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day7_dv_7dl_router", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_dv_7dl_tran,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d6_dv_7dl_rout,
                                    sdl_var_e_d6_dv_7dl_danc,
                                    sdl_var_e_d6_dv_7dl_hent,
                                    sdl_var_e_d7_dv_7dl_chec
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Gathering with Alisa",
            sdl_Replay(
                        "alt_day7_dv_7dl_dv", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_me_mini,
                                    sdl_var_i_dv_lpp,
                                    sdl_var_e_d2_conv,
                                    sdl_var_e_d6_dv_7dl_hent
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Gathering with Slavya",
            sdl_Replay("alt_day7_dv_7dl_sl", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Gathering with Lena",
            sdl_Replay("alt_day7_dv_7dl_un", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Gathering with Olga",
            sdl_Replay("alt_day7_dv_7dl_mt", {"alt_replay_on" : "True"}),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Catapult. Loki",
            sdl_Replay(
                        "alt_day7_dv_7dl_loki", {"alt_replay_on" : "True"},
                        music = music_list["farewell_to_the_past_edit"],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Departure",
            sdl_Replay(
                        "alt_day7_dv_7dl_bus", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d7_dv_7dl_chec
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    ### Alisa-DJ
    #### 4 Day
    sdl_repl_array_dv_djt_day4 = [
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day4_dv_dj_morning", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day4_dv_dj_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d1_un_talk
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Save the readhead!",
            sdl_Replay(
                        "alt_day4_dv_dj_alise_free", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Red hurricane",
            sdl_Replay(
                        "alt_day4_dv_dj_radio_event", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day4_dv_dj_lunch", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Quiet hour",
            sdl_Replay(
                        "alt_day4_dv_dj_silent_hour", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lunch",
            sdl_Replay(
                        "alt_day4_dv_dj_afternoon", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Concert",
            sdl_Replay(
                        "alt_day4_dv_dj_concert", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay(
                        "alt_day4_dv_dj_dinner", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Searching for Ulyana",
            sdl_Replay(
                        "alt_day4_dv_dj_us_search", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Beach date",
            sdl_Replay(
                        "alt_day4_dv_dj_date_on_the_beach", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day4_dv_dj_sleeptime", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 5 Day
    sdl_repl_array_dv_djt_day5 = [
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day5_dv_dj_morning", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day5_dv_dj_breakfast", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "2ch-FM",
            sdl_Replay(
                        "alt_day5_dv_dj_dvachcast", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day5_dv_dj_lunch", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Map. Alisa's cabin",
            sdl_Replay(
                        "alt_day5_dv_dj_map_house_dv1", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Map. Square",
            sdl_Replay(
                        "alt_day5_dv_dj_map_square1", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Map. Library",
            sdl_Replay(
                        "alt_day5_dv_dj_map_library1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_voya
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Map. Miku",
            sdl_Replay(
                        "alt_day5_dv_dj_map_musclub1", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Map. Cybernetics",
            sdl_Replay(
                        "alt_day5_dv_dj_map_cyber_club1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_dv_lpp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay(
                        "alt_day5_dv_dj_afternoon", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d5_dv_dj_mapp,
                                    sdl_var_i_dv_lpp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Radio",
            sdl_Replay(
                        "alt_day5_dv_dj_radio_broadcast", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay(
                        "alt_day5_dv_dj_dinner", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Hike",
            sdl_Replay(
                        "alt_day5_dv_dj_campfire", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_dv_lpp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day5_dv_dj_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d5_dv_dj_mapp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 6 Day
    sdl_repl_array_dv_djt_day6 = [
        sdl_repl_Label(
            "Awakening",
            sdl_Replay(
                        "alt_day6_dv_dj_morning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_dv_lpp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day6_dv_dj_breakfast", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Radio",
            sdl_Replay(
                        "alt_day6_dv_dj_broadcast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_dv_lpp,
                                    sdl_var_b_d6_dv_dj_bett
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day6_dv_dj_lunch", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Quiet hour",
            sdl_Replay(
                        "alt_day6_dv_dj_siesta", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_dv_lpp,
                                    sdl_var_e_d5_dv_dj_mapp,
                                    sdl_var_e_d5_dv_dj_sljr,
                                    sdl_var_b_d6_dv_dj_secr,
                                    sdl_var_b_d6_dv_dj_bett
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Concert",
            sdl_Replay(
                        "alt_day6_dv_dj_concert", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_dv_dj_dvrn,
                                    sdl_var_i_dv_lpp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay(
                        "alt_day6_dv_dj_dinner", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Evening",
            sdl_Replay(
                        "alt_day6_dv_dj_no_dance", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_dv_dj_ends
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Heart-to-heart talk",
            sdl_Replay(
                        "alt_day6_dv_dj_un_night", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_dv_dj_ends,
                                    sdl_var_e_d5_dv_dj_mapp,
                                    sdl_var_i_dv_lpp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Light out. Variation 1",
            sdl_Replay(
                        "alt_day6_dv_dj_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_dv_dj_ends
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Light out. Variation 2",
            sdl_Replay(
                        "alt_day6_dv_dj_sleeptime2", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_dv_dj_ends
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 7 Day
    sdl_repl_array_dv_djt_day7 = [
        sdl_repl_Label(
            "Dream",
            sdl_Replay(
                        "alt_day7_dv_dj_dream", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_dv_dj_ends
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day7_dv_dj_morning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_dv_dj_ends
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dots over i",
            sdl_Replay(
                        "alt_day7_dv_dj_points", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_dv_dj_ends
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Departure",
            sdl_Replay(
                        "alt_day7_dv_dj_departure", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_dv_dj_ends
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        )    ]

    ## Slavya
    ### Slavya-7DS
    #### 4 Day
    sdl_repl_array_sl_7dl_day4 = [
        sdl_repl_Label(
            "Morning",
            sdl_Replay("alt_day4_sl_7dl_begin", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day4_sl_7dl_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_7dl_work
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning. Loki",
            sdl_Replay(
                        "alt_day4_sl_7dl_loki_morning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_7dl_help,
                                    sdl_var_l_d2_voya,
                                    sdl_var_l_d2_club
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Morning. Herc",
            sdl_Replay("alt_day4_sl_7dl_herc_morning", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Morning. Wimp",
            sdl_Replay(
                        "alt_day4_sl_7dl_morning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Day. Loki",
            sdl_Replay(
                        "alt_day4_sl_7dl_loki_day", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Day. Herc",
            sdl_Replay(
                        "alt_day4_sl_7dl_herc_day", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_dubs,
                                    sdl_var_b_d4_sl_7dl_work,
                                    sdl_var_b_d4_sl_7dl_rend,
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Day. Wimp",
            sdl_Replay(
                        "alt_day4_sl_7dl_day", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_karma,
                                    sdl_var_l_d2_voya,
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Evening. Loki",
            sdl_Replay(
                        "alt_day4_sl_7dl_loki_evening", {"alt_replay_on" : "True"},
                        meets = {'al' : 'Angry boy'},
                        vars = [
                                    sdl_var_l_d2_club
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Evening. Herc",
            sdl_Replay(
                        "alt_day4_sl_7dl_herc_evening", {"alt_replay_on" : "True"},
                        meets = {'al' : 'Angry boy', 'dn' : 'Curly'},
                        vars = [
                                    sdl_var_b_d4_sl_7dl_appl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Evening. Wimp",
            sdl_Replay("alt_day4_sl_7dl_evening", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Evening",
            sdl_Replay(
                        "alt_day4_sl_7dl_sundown", {"alt_replay_on" : "True"},
                        meets = {'dn' : 'Curly', 'tn' : 'Strange boy'},
                        vars = [
                                    sdl_var_b_d4_sl_7dl_rend,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day4_sl_7dl_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_7dl_work,
                                    sdl_var_b_d4_sl_7dl_rend,
                                    sdl_var_b_d4_sl_7dl_appl,
                                    sdl_var_l_d2_club
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 5 Day
    sdl_repl_array_sl_7dl_day5 = [
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day5_sl_7dl_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_7dl_work
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day5_sl_7dl_breakfast", {"alt_replay_on" : "True"},
                        ambience = ambience_7dl["rain"],
                        vars = [
                                    sdl_var_b_d4_sl_7dl_rend,
                                    sdl_var_b_d5_sl_7dl_work,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Candle",
            sdl_Replay(
                        "alt_day5_sl_7dl_candle", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_7dl_work
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Candle. Loki",
            sdl_Replay(
                        "alt_day5_sl_7dl_candle_loki", {"alt_replay_on" : "True"},
                        music = music_7dl["deep_inside"],
                        ambience = ambience_7dl["rain"],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Candle. Herc",
            sdl_Replay(
                        "alt_day5_sl_7dl_candle_herc", {"alt_replay_on" : "True"},
                        music = music_7dl["deep_inside"],
                        ambience = ambience_7dl["rain"],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Candle. Wimp",
            sdl_Replay(
                        "alt_day5_sl_7dl_candle_dr", {"alt_replay_on" : "True"},
                        music = music_7dl["deep_inside"],
                        ambience = ambience_7dl["rain"],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Day. Loki",
            sdl_Replay("alt_day5_sl_7dl_loki_day", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Day. Herc",
            sdl_Replay(
                        "alt_day5_sl_7dl_herc_day", {"alt_replay_on" : "True"},
                        meets = {'ka' : 'Leader of 2nd squad'},
                        vars = [
                                    sdl_var_b_d4_sl_7dl_rend,
                                    sdl_var_b_d4_sl_7dl_appl,
                                    sdl_var_b_d5_sl_7dl_work,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Day. Wimp",
            sdl_Replay(
                        "alt_day5_sl_7dl_day", {"alt_replay_on" : "True"},
                        meets = {'al' : 'Angry boy', 'dn' : 'Curly', 'tn' : 'Strange boy'},
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Evening. Loki",
            sdl_Replay("alt_day5_sl_7dl_loki_evening", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Evening. Herc",
            sdl_Replay("alt_day5_sl_7dl_herc_evening", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Evening. Wimp",
            sdl_Replay(
                        "alt_day5_sl_7dl_evening", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_karma
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Fire",
            sdl_Replay(
                        "alt_day5_sl_7dl_campfire", {"alt_replay_on" : "True"},
                        meets = {'tn' : 'Strange boy'},
                        vars = [
                                    sdl_var_b_d4_sl_7dl_rend,
                                    sdl_var_b_d5_sl_7dl_work,
                                    sdl_var_i_sl_lpp
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Hentai",
            sdl_Replay("alt_day5_sl_7dl_hentai", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day5_sl_7dl_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_7dl_work,
                                    sdl_var_b_d5_sl_7dl_hent
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Night date",
            sdl_Replay(
                        "alt_day5_sl_7dl_rendezvous", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_7dl_hent,
                                    sdl_var_b_d5_sl_7dl_sick,
                                    sdl_var_i_sl_lpp
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        )
    ]
    #### 6 Day
    sdl_repl_array_sl_7dl_day6 = [
        sdl_repl_Label(
            "Lake",
            sdl_Replay(
                        "alt_day6_sl_7dl_camping", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_7dl_hent
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Revenge on Ulyanka",
            sdl_Replay(
                        "alt_day6_sl_7dl_revenge", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_7dl_hent,
                                    sdl_var_b_d5_sl_7dl_sick
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                     ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day6_sl_7dl_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_7dl_sick
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Jog",
            sdl_Replay(
                        "alt_day6_sl_7dl_running", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_7dl_work,
                                    sdl_var_b_d5_sl_7dl_work
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day6_sl_7dl_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_7dl_rend,
                                    sdl_var_b_d5_sl_7dl_olro
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning. Loki",
            sdl_Replay("alt_day6_sl_7dl_loki_morning", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Morning. Herc. Healthy",
            sdl_Replay(
                        "alt_day6_sl_7dl_herc_morning_well", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_7dl_work,
                                    sdl_var_b_d5_sl_7dl_hent
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Morning. Herc. Sick",
            sdl_Replay(
                        "alt_day6_sl_7dl_herc_morning_sick", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Morning. Wimp. Slavya",
            sdl_Replay("alt_day6_sl_7dl_dr_morning_normal", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Morning. Wimp. The Road",
            sdl_Replay(
                        "alt_day6_sl_7dl_dr_morning_olroad", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Day. Loki",
            sdl_Replay(
                        "alt_day6_sl_7dl_loki_day", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_7dl_true
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Day. Herc. Electronik",
            sdl_Replay(
                        "alt_day6_sl_7dl_herc_day_normal", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_7dl_sick
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Day. Herc. On the roof",
            sdl_Replay(
                        "alt_day6_sl_7dl_herc_day_alt", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_7dl_sick
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Day. Wimp. Slavya",
            sdl_Replay(
                        "alt_day6_sl_7dl_dr_day_normal", {"alt_replay_on" : "True"},
                        meets = {'ka' : 'Leader of 2nd squad'},
                        func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Day. Wimp. The Road",
            sdl_Replay(
                        "alt_day6_sl_7dl_dr_day_olroad", {"alt_replay_on" : "True"},
                        meets = {'uv' : 'Catgirl'},
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Evening. Loki",
            sdl_Replay("alt_day6_sl_7dl_loki_evening", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Evening. Herc. Slavya",
            sdl_Replay(
                        "alt_day6_sl_7dl_herc_evening_normal", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_7dl_sick
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Evening. Herc. Concert",
            sdl_Replay(
                        "alt_day6_sl_7dl_herc_evening_alt", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_7dl_sick
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Evening. Wimp. Slavya",
            sdl_Replay("alt_day6_sl_7dl_dr_evening_normal", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Evening. Wimp. The Road",
            sdl_Replay(
                        "alt_day6_sl_7dl_dr_evening_olroad", {"alt_replay_on" : "True"},
                        meets = {'uv' : 'Catgirl'},
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay(
                        "alt_day6_sl_7dl_supper", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_sl_7dl_squa,
                                    sdl_var_b_d5_sl_7dl_olro
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Catapult",
            sdl_Replay(
                        "alt_day6_sl_7dl_catapult", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_sl_7dl_squa,
                                    sdl_var_b_d5_sl_7dl_sick,
                                    sdl_var_i_karma
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "The Pirate's Funeral",
            sdl_Replay("alt_day6_sl_7dl_dr_funeral", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Memory Forest",
            sdl_Replay(
                        "alt_day6_sl_7dl_loki_disco", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_lpp
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Disco. Herc",
            sdl_Replay(
                        "alt_day6_sl_7dl_herc_disco", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_sl_7dl_squa,
                                    sdl_var_b_d4_sl_7dl_rend,
                                    sdl_var_b_d5_sl_7dl_sick,
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Disco. Wimp. Slavya",
            sdl_Replay("alt_day6_sl_7dl_dr_disco_normal", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Disco. Wimp. The Road",
            sdl_Replay(
                        "alt_day6_sl_7dl_dr_disco_olroad", {"alt_replay_on" : "True"},
                        music = music_7dl["unforgotten"],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Hentai. Loki",
            sdl_Replay("alt_day6_sl_7dl_loki_hentai", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Hentai. Herc",
            sdl_Replay(
                        "alt_day6_sl_7dl_herc_hentai", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_7dl_hent
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Hentai. Wimp",
            sdl_Replay("alt_day6_sl_7dl_dr_hentai_normal", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Hentai. Wimp 2",
            sdl_Replay("alt_day6_sl_7dl_dr_hentai_olroad", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day6_sl_7dl_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_sl_7dl_hent
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 7 Day
    sdl_repl_array_sl_7dl_day7 = [
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day7_sl_7dl_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_sl_7dl_squa,
                                    sdl_var_b_d5_sl_7dl_olro,
                                    sdl_var_b_d5_sl_7dl_sick,
                                    sdl_var_b_d6_sl_7dl_hent
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning. Loki",
            sdl_Replay("alt_day7_sl_7dl_begin_loki", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Morning. Herc",
            sdl_Replay(
                        "alt_day7_sl_7dl_begin_herc", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_sl_7dl_squa
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Gatherings. Loki. Farewell",
            sdl_Replay("alt_day7_sl_7dl_packing_loki_forgive", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Gatherings. Loki. Asshole",
            sdl_Replay("alt_day7_sl_7dl_packing_loki_asshole", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Gatherings. Herc",
            sdl_Replay(
                        "alt_day7_sl_7dl_packing_herc", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_sl_7dl_squa,
                                    sdl_var_b_d4_sl_7dl_appl,
                                    sdl_var_b_d5_sl_7dl_defe
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Gatherings. Wimp",
            sdl_Replay(
                        "alt_day7_sl_7dl_packing", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_7dl_olro
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Departure",
            sdl_Replay(
                        "alt_day7_sl_7dl_leaving", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_7dl_olro,
                                    sdl_var_b_d6_sl_7dl_forg,
                                    sdl_var_i_sl_lpp,
                                    sdl_var_i_karma
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Epilogue. Loki",
            sdl_Replay(
                        "alt_day7_sl_7dl_loki", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_sl_7dl_forg
                                ],
                        func_in = prolog_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Epilogue. Loki. Asshole",
            sdl_Replay("alt_day7_sl_7dl_loki_rewind", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        # sdl_repl_Label(
            # "Epilogue. Herc",
            # sdl_Replay("alt_day7_sl_7dl_herc", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            # char_mask = 2
        # ),
        sdl_repl_Label(
            "Epilogue. Wimp",
            sdl_Replay("alt_day7_sl_7dl_epi", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            char_mask = 1
        )
    ]
    ### Slavya-Classic
    #### 4 Day
    sdl_repl_array_sl_clt_day4 = [
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day4_sl_cl_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_walk
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Buzzer",
            sdl_Replay("alt_day4_sl_cl_shurik", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Technodream",
            sdl_Replay(
                        "alt_day4_sl_cl_laundry", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_e_d4_me_neu_tran
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay(
                        "alt_day4_sl_cl_supper", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_dv_hous,
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Gatherings",
            sdl_Replay(
                        "alt_day4_sl_cl_party_up", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_b_d4_sl_cl_left,
                                    sdl_var_b_d4_sl_cl_un_reje,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Searchings",
            sdl_Replay(
                        "alt_day4_sl_cl_lf_coop", {"alt_replay_on" : "True"},
                        ambience = ambience_forest_evening,
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_b_d4_sl_cl_left,
                                    sdl_var_b_d4_sl_cl_un_reje,
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Old Camp",
            sdl_Replay(
                        "alt_day4_sl_cl_old_camp", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Catacombs ",
            sdl_Replay(
                        "alt_day4_sl_cl_old_camp2", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Witch",
            sdl_Replay(
                        "alt_day4_sl_wh_night", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day4_sl_cl_cs_night", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 5 Day
    sdl_repl_array_sl_clt_day5 = [
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day5_sl_cl_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Head of the camp",
            sdl_Replay(
                        "alt_day5_sl_cl_chief", {"alt_replay_on" : "True"},
                        meets = {'bb' : 'Head of the camp'},
                        ambience = ambience_7dl["rain"],
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Olga",
            sdl_Replay(
                        "alt_day5_sl_cl_mt", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day5_sl_cl_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Conversation with Sanich",
            sdl_Replay(
                        "alt_day5_sl_cl_ba_quest", {"alt_replay_on" : "True"},
                        music = music_list["everyday_theme"],
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_i_sl_lpp,
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Catacombs ",
            sdl_Replay(
                        "alt_day5_sl_cl_catacombs", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_lpp,
                                    sdl_var_i_sl_sp,
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "The Fog",
            sdl_Replay(
                        "alt_day5_sl_cl_fog", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_i_sl_sp,
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Return",
            sdl_Replay(
                        "alt_day5_sl_cl_return", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Viola's lecture",
            sdl_Replay(
                        "alt_day5_sl_cl_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_un_reje,
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Preparing the fire",
            sdl_Replay(
                        "alt_day5_sl_cl_campfire_prepare", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_e_d3_me_dan1
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Swimming",
            sdl_Replay("alt_day5_sl_cl_bathing", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay(
                        "alt_day5_sl_cl_supper", {"alt_replay_on" : "True"},
                        meets = {'dn' : 'Curly'},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Fire",
            sdl_Replay(
                        "alt_day5_sl_cl_campfire", {"alt_replay_on" : "True"},
                        ambience = ambience_forest_evening,
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Help the wounded",
            sdl_Replay(
                        "alt_day5_sl_cl_dn_aid", {"alt_replay_on" : "True"},
                        meets = {'dn' : 'Curly'},
                        ambience = ambience_forest_evening,
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Viola's Gift",
            sdl_Replay(
                        "alt_day5_sl_cl_cs_reward", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Night date",
            sdl_Replay(
                        "alt_day5_sl_cl_night", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_i_sl_sp,
                                    sdl_var_e_d2_date
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Hentai",
            sdl_Replay("alt_day5_sl_cl_hentai", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day5_sl_cl_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_sp,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 6 Day
    sdl_repl_array_sl_clt_day6 = [
        sdl_repl_Label(
            "Morning. Cave",
            sdl_Replay(
                        "alt_day6_sl_cl_begin_cave", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning. Together",
            sdl_Replay(
                        "alt_day6_sl_cl_begin_good", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning. Technodream",
            sdl_Replay(
                        "alt_day6_sl_cl_begin_techno", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Shurik's problems",
            sdl_Replay(
                        "alt_day6_sl_cl_sh_problems", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_b_d5_sl_cl_hent
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay("alt_day6_sl_cl_breakfast", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Sanich's task",
            sdl_Replay(
                        "alt_day6_sl_cl_ba_quest", {"alt_replay_on" : "True"},
                        ambience = ambience_dining_hall_empty,
                        vars = [
                                    sdl_var_b_d5_sl_cl_hent,
                                    sdl_var_e_d4_sl_cl_solo,
                                    sdl_var_l_d2_club
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Sanich's boss",
            sdl_Replay(
                        "alt_day6_sl_cl_ba_kgb", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_b_d5_sl_cl_hent
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day6_sl_cl_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_b_d5_sl_cl_hent,
                                    sdl_var_i_sl_sp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Amplifier",
            sdl_Replay(
                        "alt_day6_sl_cl_amp_list", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_sl_cl_shir
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Jammer",
            sdl_Replay(
                        "alt_day6_sl_cl_amp_club", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_b_d5_sl_cl_hent,
                                    sdl_var_b_d6_sl_cl_shir,
                                    sdl_var_i_sl_sp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Fainting Slavya",
            sdl_Replay(
                        "alt_day6_sl_cl_ambulance", {"alt_replay_on" : "True"},
                        ambience = ambience_clubs_inside_day,
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_b_d5_sl_cl_hent
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Anatoliy Ivanovich",
            sdl_Replay(
                        "alt_day6_sl_cl_kgb", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_b_d5_sl_cl_hent,
                                    sdl_var_e_d2_walk
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Pirate",
            sdl_Replay(
                        "alt_day6_sl_cl_pirate", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_cl_hent,
                                    sdl_var_i_sl_lpp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "World of Second Chances",
            sdl_Replay(
                        "alt_day6_sl_cl_regular_arc", {"alt_replay_on" : "True"},
                        music = music_7dl["gonna_be_ok"],
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_e_d2_conv,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Help from Sanich",
            sdl_Replay(
                        "alt_day6_sl_cl_ba_help", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_b_d5_sl_cl_hent
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Concert. Pirate",
            sdl_Replay(
                        "alt_day6_sl_cl_hala", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_cl_hent,
                                    sdl_var_i_sl_sp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Concert. Shurik",
            sdl_Replay(
                        "alt_day6_sl_cl_concert", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_cl_hent,
                                    sdl_var_i_sl_lpp,
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Algorithm",
            sdl_Replay(
                        "alt_day6_sl_cl_algorithm", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_sl_cl_hent
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Speakers",
            sdl_Replay("alt_day6_sl_cl_sonic", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay(
                        "alt_day6_sl_cl_supper", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Disco",
            sdl_Replay(
                        "alt_day6_sl_cl_dance", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dance",
            sdl_Replay(
                        "alt_day6_sl_cl_dancing", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_cl_hent,
                                    sdl_var_i_sl_sp
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Shurik's Story",
            sdl_Replay(
                        "alt_day6_sl_cl_sh_story", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_entrance_night,
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Viola",
            sdl_Replay(
                        "alt_day6_sl_cl_sh_tug", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Landing stage",
            sdl_Replay(
                        "alt_day6_sl_cl_debarkader", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 7 Day
    sdl_repl_array_sl_clt_day7 = [
        sdl_repl_Label(
            "Technodream",
            sdl_Replay("alt_day7_sl_cl_techno", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Morning. Isolator",
            sdl_Replay(
                        "alt_day7_sl_cl_begin_sh", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_cl_hent,
                                    sdl_var_b_d6_sl_cl_hent
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning. Landing stage",
            sdl_Replay("alt_day7_sl_cl_begin_pi", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Incident",
            sdl_Replay(
                        "alt_day7_sl_cl_incident", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_sl_cl_arc
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day7_sl_cl_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_sl_cl_arc
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Detour. Admin. building",
            sdl_Replay("alt_day7_sl_cl_admins1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Detour. Clubs",
            sdl_Replay(
                        "alt_day7_sl_cl_clubs1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_sl_cl_arc
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Detour. Canteen",
            sdl_Replay("alt_day7_sl_cl_dining_hall1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Detour. Sports ground",
            sdl_Replay(
                        "alt_day7_sl_cl_sport_area1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Detour. Volleyball court.",
            sdl_Replay(
                        "alt_day7_sl_cl_volleyball_alt2", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_club
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Detour. Stage",
            sdl_Replay("alt_day7_sl_cl_estrade1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Detour. Pier",
            sdl_Replay(
                        "alt_day7_sl_cl_boat_station1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Detour. Beach",
            sdl_Replay(
                        "alt_day7_sl_cl_beach", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_date,
                                    sdl_var_e_d6_sl_cl_arc
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "A commemorative photo",
            sdl_Replay(
                        "alt_day7_sl_cl_photo", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_mi_snap,
                                    sdl_var_b_d7_sl_cl_code,
                                    sdl_var_e_d6_sl_cl_arc
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day7_sl_cl_dinner", {"alt_replay_on" : "True"},
                        meets = {'bb' : 'Head of the camp'},
                        vars = [
                                    sdl_var_i_sl_lpp,
                                    sdl_var_i_sl_sp,
                                    sdl_var_e_d6_sl_cl_arc
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Departure. Got it",
            sdl_Replay("alt_day7_sl_cl_departure_a2th", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Departure. Late",
            sdl_Replay(
                        "alt_day7_sl_cl_departure_lone", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_sl_cl_shir,
                                    sdl_var_i_sl_lpp,
                                    sdl_var_i_sl_sp,
                                    sdl_var_e_d6_sl_cl_arc
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### ??? Day
    sdl_repl_array_sl_clt_dayx = [
        sdl_repl_Label(
            "At home",
            sdl_Replay("alt_day6_sl_cl_home", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Syomushka",
            sdl_Replay("alt_day6_sl_cl_intellectual", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Biggest fear",
            sdl_Replay("alt_day7_sl_cl_fear", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "1996",
            sdl_Replay("alt_day7_sl_cl_1996", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Rescue operation",
            sdl_Replay(
                        "alt_day7_sl_cl_loop", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Porridge",
            sdl_Replay("alt_day7_sl_cl_porridge", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Post-Scriptum",
            sdl_Replay("alt_day7_sl_cl_ps", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load)
        )
    ]

    ## Lena
    ### Lena-7DS
    #### 4 Day
    sdl_repl_array_un_7dl_day4 = [
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day4_un_7dl_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_e_d3_un_stri
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lineup",
            sdl_Replay("alt_day4_un_7dl_lineup", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day4_un_7dl_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_un_7dl_sear
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Bus stop",
            sdl_Replay(
                        "alt_day4_un_7dl_entrance", {"alt_replay_on" : "True"},
                        music = music_list["tried_to_bring_it_back"],
                        vars = [
                                    sdl_var_i_un_lpp
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Recording",
            sdl_Replay(
                        "alt_day4_un_7dl_declaration", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_un_7dl_sear
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Make up with Zhenya",
            sdl_Replay(
                        "alt_day4_un_7dl_library", {"alt_replay_on" : "True"},
                        music = music_list["everyday_theme"],
                        vars = [
                                    sdl_var_b_d4_un_7dl_sear
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day4_un_7dl_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_me_neu_tran,
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Day. Loki",
            sdl_Replay(
                        "alt_day4_un_7dl_day_loki", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_conv,
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_e_d3_me_stri,
                                    sdl_var_e_d4_me_neu_tran
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Hentai",
            sdl_Replay("alt_day4_un_7dl_hentai", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Day. Herc",
            sdl_Replay(
                        "alt_day4_un_7dl_day_herc", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_me_neu_tran
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Day. Wimp. newspaper",
            sdl_Replay(
                        "alt_day4_un_7dl_day_dr_nwsppr", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key,
                                    sdl_var_e_d4_me_neu_tran,
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Day. Wimp. Badminton",
            sdl_Replay(
                        "alt_day4_un_7dl_day_dr_badmin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_conv,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d4_me_neu_tran,
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Lunch",
            sdl_Replay(
                        "alt_day4_un_7dl_launch", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_un_7dl_duck,
                                    sdl_var_e_d4_me_neu_tran
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Concert",
            sdl_Replay(
                        "alt_day4_un_7dl_concert", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_un_7dl_duck,
                                    sdl_var_b_d4_un_7dl_ba_aler,
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Explosives",
            sdl_Replay(
                        "alt_day4_un_7dl_dynamite", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_e_d4_un_7dl_calm
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay(
                        "alt_day4_un_7dl_supper", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_un_7dl_expl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Evening",
            sdl_Replay(
                        "alt_day4_un_7dl_evening", {"alt_replay_on" : "True"},
                        music = music_list["a_promise_from_distant_days"],
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 6
        ),
        sdl_repl_Label(
            "Evening. Wimp",
            sdl_Replay(
                        "alt_day4_un_7dl_evening_dr", {"alt_replay_on" : "True"},
                        music = music_list["a_promise_from_distant_days"],
                        vars = [
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_e_d4_me_neu_tran
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Pier",
            sdl_Replay("alt_day4_un_7dl_dock", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay("alt_day4_un_7dl_sleeptime", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        )
    ]
    #### 5 Day
    sdl_repl_array_un_7dl_day5 = [
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day5_un_7dl_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_me_neu_tran
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day5_un_7dl_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_un_7dl_duck,
                                    sdl_var_e_d1_sl_key,
                                    sdl_var_e_d4_un_7dl_calm,
                                    sdl_var_l_d2_club
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning. Loki",
            sdl_Replay("alt_day5_un_7dl_breakfast_l", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Morning. Herc",
            sdl_Replay(
                        "alt_day5_un_7dl_breakfast_h", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_un_7dl_expl,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_l_d2_club
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Morning. Wimp",
            sdl_Replay(
                        "alt_day5_un_7dl_games", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_un_7dl_duck,
                                    sdl_var_b_d4_un_7dl_expl,
                                    sdl_var_e_d4_me_neu_tran,
                                    sdl_var_l_d2_club
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Clubs",
            sdl_Replay("alt_day5_un_7dl_clubs", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "«Lilac Balloon»",
            sdl_Replay(
                        "alt_day4_un_7dl_cinema", {"alt_replay_on" : "True"},
                        music = music_list["sweet_darkness"],
                        vars = [
                                    sdl_var_e_d4_me_neu_tran
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Square cleaning",
            sdl_Replay("alt_day5_un_7dl_cleaning", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day5_un_7dl_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_un_7dl_expl,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_e_d2_brf,
                                    sdl_var_e_d3_me_dan1,
                                    sdl_var_e_d4_me_neu_tran,
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Beach",
            sdl_Replay(
                        "alt_day5_un_7dl_np", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_me_neu_tran
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Article",
            sdl_Replay("alt_day5_un_7dl_article", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Alyona",
            sdl_Replay("alt_day5_un_7dl_unl", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Lunch",
            sdl_Replay(
                        "alt_day5_un_7dl_launch", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Library",
            sdl_Replay(
                        "alt_day5_un_7dl_library", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_un,
                                    sdl_var_e_d4_me_neu_tran
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Cleaning the campfire glade",
            sdl_Replay(
                        "alt_day5_un_7dl_washing", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key,
                                    sdl_var_e_d3_me_dan1,
                                    sdl_var_e_d4_me_neu_tran,
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay(
                        "alt_day5_un_7dl_supper", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d5_un_7dl_wash
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Fire",
            sdl_Replay(
                        "alt_day5_un_7dl_campfire", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_me_neu_tran,
                                    sdl_var_e_d5_un_7dl_wash
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Small quarrel",
            sdl_Replay(
                        "alt_day5_un_7dl_evening_un", {"alt_replay_on" : "True"},
                        sound_loop = sfx_forest_fireplace,
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Big quarrel",
            sdl_Replay(
                        "alt_day5_un_7dl_evening_dv", {"alt_replay_on" : "True"},
                        sound_loop = sfx_forest_fireplace,
                        vars = [
                                    sdl_var_b_d2_us_esca
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Runaway",
            sdl_Replay(
                        "alt_day5_un_7dl_runaway", {"alt_replay_on" : "True"},
                        sound_loop = sfx_forest_fireplace,
                        vars = [
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_l_d2_club
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Hentai in clubs",
            sdl_Replay(
                        "alt_day5_un_7dl_video", {"alt_replay_on" : "True"},
                        sound_loop = sfx_forest_fireplace,
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Hentai in the boat",
            sdl_Replay(
                        "alt_day5_un_7dl_island_hen", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_un_7dl_hent,
                                    sdl_var_e_d3_me_stri,
                                    sdl_var_e_d4_me_neu_tran
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day5_un_7dl_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 6 Day
    sdl_repl_array_un_7dl_day6 = [
        sdl_repl_Label(
            "Morning",
            sdl_Replay("alt_day6_un_7dl_begin", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Searchings. Library",
            sdl_Replay(
                        "alt_day6_un_7dl_search", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_me_neu_tran
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay("alt_day6_un_7dl_dinner", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Searchings. Quarry",
            sdl_Replay("alt_day6_un_7dl_career", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Searchings. Mus. club",
            sdl_Replay(
                        "alt_day6_un_7dl_music_club", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Concert",
            sdl_Replay(
                        "alt_day6_un_7dl_concert", {"alt_replay_on" : "True"},
                        music = music_list["everyday_theme"],
                        vars = [
                                    sdl_var_b_d4_un_7dl_duck,
                                    sdl_var_e_d1_sl_key,
                                    sdl_var_e_d5_un_7dl_wash,
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay("alt_day6_un_7dl_supper", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Catapult",
            sdl_Replay(
                        "alt_day6_un_7dl_catapult", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_karma
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Disco",
            sdl_Replay(
                        "alt_day6_un_7dl_dance", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_un_7dl_duck,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_e_d4_me_neu_tran,
                                    sdl_var_l_d2_club
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay("alt_day6_un_7dl_sleeptime", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        )
    ]
    #### 7 Day
    sdl_repl_array_un_7dl_day7 = [
        sdl_repl_Label(
            "Dream",
            sdl_Replay("alt_day7_un_7dl_begin", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Day",
            sdl_Replay(
                        "alt_day7_un_7dl_day", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key,
                                    sdl_var_e_d4_me_neu_tran
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay("alt_day7_un_7dl_dinner", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Hysteria",
            sdl_Replay(
                        "alt_day7_un_7dl_hysterics", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_me_neu_tran
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Pills",
            sdl_Replay("alt_day7_un_7dl_pills", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Miracle",
            sdl_Replay(
                        "alt_day7_un_7dl_miracle", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_karma,
                                    sdl_var_e_d1_sl_key,
                                    sdl_var_l_d2_club
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Rollback",
            sdl_Replay("alt_day7_un_7dl_rollback", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Departure",
            sdl_Replay(
                        "alt_day7_un_7dl_departure", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_me_neu_tran
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    ### Lena-FZ
    #### 4 Day
    sdl_repl_array_un_fzd_day4 = [
        sdl_repl_Label(
            "Dream. Lena",
            sdl_Replay("alt_day4_un_fz_dream_un", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Dream. The Road",
            sdl_Replay("alt_day4_un_fz_dream_road", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Morning",
            sdl_Replay("alt_day4_un_fz_morning", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Infirmary",
            sdl_Replay(
                        "alt_day4_un_fz_aidpost", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_fzd_dv,
                                    sdl_var_l_d2_club
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Wall newspaper",
            sdl_Replay(
                        "alt_day4_un_fz_un_nwsppr", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Assistant counselor",
            sdl_Replay("alt_day4_un_fz_mt_help", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Escape with Alisa",
            sdl_Replay("alt_day4_un_fz_dv_escape", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Lost",
            sdl_Replay("alt_day4_un_fz_old_road", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Dinner. After newspaper",
            sdl_Replay("alt_day4_un_fz_lunch_nwsppr", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Dinner. After boats",
            sdl_Replay("alt_day4_un_fz_lunch_boat", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Dinner. After forest",
            sdl_Replay(
                        "alt_day4_un_fz_lunch_forest", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_fzd_dv
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Quiet hour",
            sdl_Replay(
                        "alt_day4_un_fz_siesta", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_un_fz_stories,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_e_d4_un_fz_morn
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Lunch",
            sdl_Replay(
                        "alt_day4_un_fz_afternoon", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_un_fz_old_road
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Wild beach",
            sdl_Replay(
                        "alt_day4_un_fz_un_date", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_un_fz_walk
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay(
                        "alt_day4_un_fz_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_fzd_dv
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "The Chase",
            sdl_Replay(
                        "alt_day4_un_fz_run", {"alt_replay_on" : "True"},
                        meets = {'al' : 'Angry Boy'},
                        vars = [
                                    sdl_var_b_d3_un_fz_stories,
                                    sdl_var_i_un_fzd_dv
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "The showdown",
            sdl_Replay(
                        "alt_day4_un_fz_debriefing", {"alt_replay_on" : "True"},
                        meets = {'dn' : 'Curly'},
                        music = music_7dl["areyouabully"],
                        vars = [
                                    sdl_var_i_un_fzd_dv,
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Evening",
            sdl_Replay(
                        "alt_day4_un_fz_evening", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_un_fz_us_run,
                                    sdl_var_i_un_fzd_dv,
                                    sdl_var_i_un_fzd_mt
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Evening. Olga's cabin",
            sdl_Replay("alt_day4_un_fz_mt_house", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Evening. Port Wine",
            sdl_Replay(
                        "alt_day4_un_fz_portwine", {"alt_replay_on" : "True"},
                        music = music_list["smooth_machine"],
                        ambience = ambience_camp_center_evening,
                        vars = [
                                    sdl_var_b_d4_un_fz_old_road,
                                    sdl_var_b_d4_un_fz_us_run,
                                    sdl_var_i_un_fzd_dv,
                                    sdl_var_e_d4_un_fz_morn
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "«Tea Party»",
            sdl_Replay(
                        "alt_day4_un_fz_tea_party", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_un_fz_morn
                                    # Tournament int
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "After the party",
            sdl_Replay(
                        "alt_day4_un_fz_afterparty", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_un_fz_stories,
                                    sdl_var_i_un_fzd_ol,
                                    sdl_var_i_un_fzd_dv
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day4_un_fz_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_fzd_dv,
                                    sdl_var_i_un_fzd_mt
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        )
    ]
    #### 5 Day
    sdl_repl_array_un_fzd_day5 = [
        sdl_repl_Label(
            "Dream",
            sdl_Replay("alt_day5_un_fz_dream", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day5_un_fz_morning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_fzd_dv
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day5_un_fz_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_fzd_ol,
                                    sdl_var_i_un_fzd_dv,
                                    sdl_var_e_d4_un_fz_even
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Candle",
            sdl_Replay(
                        "alt_day5_un_fz_cndl", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_fzd_dv,
                                    sdl_var_e_d3_un_fz_work
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Dream. Alisa",
            sdl_Replay("alt_day5_un_fz_dream2_dv", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Dream. Lena",
            sdl_Replay("alt_day5_un_fz_dream2_un", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Dream. The Road",
            sdl_Replay("alt_day5_un_fz_dream2_road", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day5_un_fz_lunch", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_un_fz_un_run
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Cinderella",
            sdl_Replay(
                        "alt_day5_un_fz_beach_work", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_fzd_dv
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Lunch",
            sdl_Replay(
                        "alt_day5_un_fz_afternoon", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_un_fz_us_break
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Campfire glade",
            sdl_Replay(
                        "alt_day5_un_fz_bonfire_glade", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_fzd_dv
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Old Camp",
            sdl_Replay(
                        "alt_day5_un_fz_old_camp", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_un_fz_stories,
                                    sdl_var_b_d4_un_fz_old_road
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay(
                        "alt_day5_un_fz_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_un_fz_old_camp,
                                    sdl_var_i_un_fzd_dv
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Olga's errand",
            sdl_Replay(
                        "alt_day5_un_fz_mission", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_fzd_ol,
                                    sdl_var_e_d4_un_fz_morn
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Evening",
            sdl_Replay(
                        "alt_day5_un_fz_evening", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_un_fz_old_camp,
                                    sdl_var_i_un_fzd_ol,
                                    sdl_var_i_un_fzd_dv
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Fire",
            sdl_Replay(
                        "alt_day5_un_fz_campfire", {"alt_replay_on" : "True"},
                        ambience = ambience_forest_evening,
                        vars = [
                                    sdl_var_b_d3_un_fz_stories,
                                    sdl_var_b_d5_un_fz_old_camp
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Searchings",
            sdl_Replay(
                        "alt_day5_un_fz_search", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_fzd_dream_un,
                                    sdl_var_i_un_fzd_dream_ol
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Flare. FZ",
            sdl_Replay(
                        "alt_day5_un_fz_fzr", {"alt_replay_on" : "True"},
                        ambience = ambience_lake_shore_night,
                        vars = [
                                    sdl_var_i_un_fzd_dv
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Flare. The Road",
            sdl_Replay(
                        "alt_day5_un_fz_rr", {"alt_replay_on" : "True"},
                        ambience = ambience_lake_shore_night,
                        vars = [
                                    sdl_var_e_d4_un_fz_even
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Lights out. FZ",
            sdl_Replay(
                        "alt_day5_un_fz_fzr_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_un_fz_stories,
                                    sdl_var_i_un_fzd_dv
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Lights out. The Road",
            sdl_Replay("alt_day5_un_fz_rr_sleeptime", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 2
        )
    ]
    #### 6 Day. The Road
    sdl_repl_array_un_fzd_day6 = [
        sdl_repl_Label(
            "Dream",
            sdl_Replay("alt_day6_un_fz_rr_dream", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day6_un_fz_rr_morning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_un_fz_old_road,
                                    sdl_var_b_d5_un_fz_old_camp,
                                    sdl_var_e_d4_un_fz_morn
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Lineup",
            sdl_Replay("alt_day6_un_fz_rr_lineup", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day6_un_fz_rr_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_un_fz_us_break
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Searchings",
            sdl_Replay(
                        "alt_day6_un_fz_rr_search", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_un_fz_old_camp
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Searchings. Tree house",
            sdl_Replay(
                        "alt_day6_un_fz_rr_search3", {"alt_replay_on" : "True"},
                        music = music_list["get_to_know_me_better"],
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_b_d5_un_fz_us_break,
                                    sdl_var_i_un_fzd_dv
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Searchings. Old Camp",
            sdl_Replay(
                        "alt_day6_un_fz_rr_search2", {"alt_replay_on" : "True"},
                        meets = {'tn' : 'Strange boy'},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day6_un_fz_rr_lunch", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_un_fz_old_camp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Rescue the Guardsmen",
            sdl_Replay("alt_day6_un_fz_rr_guard_resque", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "The Old Road",
            sdl_Replay(
                        "alt_day6_un_fz_rr_old_road", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_un_fz_stories,
                                    sdl_var_b_d4_un_fz_old_road,
                                    sdl_var_b_d5_un_fz_old_camp,
                                    sdl_var_i_un_fzd_dream_ol
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Another world",
            sdl_Replay("alt_day6_un_fz_rr_another_world", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Farewell",
            sdl_Replay("alt_day6_un_fz_rr_farewell", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 2
        )
    ]
    #### 6 Day. FZ
    sdl_repl_array_un_fzd_day62 = [
        sdl_repl_Label(
            "Awakening",
            sdl_Replay(
                        "alt_day6_un_fz_morning", {"alt_replay_on" : "True"},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Lineup",
            sdl_Replay(
                        "alt_day6_un_fz_lineup", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_fzd_dv
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day6_un_fz_breakfast", {"alt_replay_on" : "True"},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Map. Boat station",
            sdl_Replay(
                        "alt_day6_un_fz_map_boatstation1", {"alt_replay_on" : "True"},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Map. Sports ground",
            sdl_Replay(
                        "alt_day6_un_fz_map_playground1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_un_fz_stories
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Map. Mus. club",
            sdl_Replay(
                        "alt_day6_un_fz_map_musclub1", {"alt_replay_on" : "True"},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Map. Alisa's house",
            sdl_Replay(
                        "alt_day6_un_fz_map_house_dv1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_dv_hous
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Map. Beach",
            sdl_Replay(
                        "alt_day6_un_fz_map_beach2", {"alt_replay_on" : "True"},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Map. Canteen",
            sdl_Replay(
                        "alt_day6_un_fz_map_dinner_hall2", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_un_fz_work
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Map. Bus stop",
            sdl_Replay(
                        "alt_day6_un_fz_map_busstation2", {"alt_replay_on" : "True"},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day6_un_fz_lunch", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_un_fz_map2
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Helping Slavya",
            sdl_Replay(
                        "alt_day6_un_fz_sl_help", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_un_fz_map1,
                                    sdl_var_i_un_fzd_dv,
                                    sdl_var_e_d6_un_fz_map2,

                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Lunch",
            sdl_Replay(
                        "alt_day6_un_fz_afternoon", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_fzd_dv,
                                    sdl_var_e_d6_un_fz_map1
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Concert",
            sdl_Replay(
                        "alt_day6_un_fz_concert", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_fzd_dv,
                                    sdl_var_e_d6_un_fz_map1,
                                    sdl_var_e_d6_un_fz_map2
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Supper with Alisa",
            sdl_Replay(
                        "alt_day6_un_fz_dv_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_un_fz_map1
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Evening with Alisa",
            sdl_Replay(
                        "alt_day6_un_fz_dv_date", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Searching for Lena",
            sdl_Replay(
                        "alt_day6_un_fz_dv_un_search", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Nightmare unfolding",
            sdl_Replay(
                        "alt_day6_un_fz_dv_un_night", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Supper with Lena",
            sdl_Replay(
                        "alt_day6_un_fz_good_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_un_fz_map1
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Dots over «i»",
            sdl_Replay(
                        "alt_day6_un_fz_good_un_evening", {"alt_replay_on" : "True"},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Dances alone",
            sdl_Replay(
                        "alt_day6_un_fz_dance1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_un_fz_map1,
                                    sdl_var_i_un_fzd_dv
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Conversation with Olga",
            sdl_Replay(
                        "alt_day6_un_fz_sleeptime1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_un_fz_map2
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Dances with Lena",
            sdl_Replay(
                        "alt_day6_un_fz_dance2", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Walk",
            sdl_Replay(
                        "alt_day6_un_fz_night_walk", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day6_un_fz_sleeptime2", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Supper alone",
            sdl_Replay(
                        "alt_day6_un_fz_bad_neu_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_un_fz_old_road
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Search",
            sdl_Replay(
                        "alt_day6_un_fz_un_search", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_un_fz_old_road
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Escort to camp",
            sdl_Replay(
                        "alt_day6_un_fz_neu_sleeptime", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Returning Alone",
            sdl_Replay(
                        "alt_day6_un_fz_neu_bad_sleeptime", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "At Hell's gate",
            sdl_Replay(
                        "alt_day6_un_fz_night_in_hell", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        )
    ]
    #### 7 Day. FZ
    sdl_repl_array_un_fzd_day7 = [
        sdl_repl_Label(
            "Hell. Morning",
            sdl_Replay(
                        "alt_day7_un_fz_bad_morning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_fzd_dv
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Hell. In Search of Olga",
            sdl_Replay(
                        "alt_day7_un_fz_bad_mt_search", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_fzd_dv
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Hell. Departure",
            sdl_Replay(
                        "alt_day7_un_fz_bad_departure", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_fzd_dv,
                                    sdl_var_e_d6_un_fz_map2
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Lena. Morning",
            sdl_Replay(
                        "alt_day7_un_fz_good_morning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Lena. Breakfast",
            sdl_Replay(
                        "alt_day7_un_fz_good_breakfast", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Lena. Farewell",
            sdl_Replay(
                        "alt_day7_un_fz_good_farewell", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_un_fz_map2,
                                    sdl_var_e_d4_un_fz_morn,
                                    sdl_var_i_un_fzd_dv,
                                    sdl_var_b_d4_un_fz_old_road
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Lena. Departure",
            sdl_Replay(
                        "alt_day7_un_fz_good_departure", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_un_fz_map2
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day7_un_fz_neu_morning", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day7_un_fz_neu_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_un_fz_hent
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Goodbye, Camp",
            sdl_Replay(
                        "alt_day7_un_fz_neu_camp_farewell", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_un_fz_map2,
                                    sdl_var_e_d1_sl_key,
                                    sdl_var_b_d3_un_fz_stories,
                                    sdl_var_b_d6_un_fz_hent
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Departure",
            sdl_Replay(
                        "alt_day7_un_fz_neu_departure", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_un_fz_hent
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        )
    ]

    ## Olga
    ### Olga-7DS
    #### 6 Day
    sdl_repl_array_mt_7dl_day6 = [
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day6_mt_7dl_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_mt_hent
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay("alt_day6_mt_7dl_breakfast", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Party assignment",
            sdl_Replay(
                        "alt_day6_mt_7dl_morning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_mt_hent
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning. Alisa",
            sdl_Replay("alt_day6_mt_7dl_dv_morning", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Morning. Lena",
            sdl_Replay(
                        "alt_day6_mt_7dl_un_morning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl,
                                    sdl_var_i_un_fzd_mt,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d4_me_neu_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "About unneeded",
            sdl_Replay(
                        "alt_day6_mt_7dl_retail", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_mt_hent
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Bitterness",
            sdl_Replay(
                        "alt_day6_mt_7dl_bitter", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_mt_diar
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Farewell",
            sdl_Replay("alt_day6_mt_7dl_forgive", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "First meetings",
            sdl_Replay(
                        "alt_day6_mt_7dl_memento", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_mt_hent
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Diary P. 3",
            sdl_Replay("alt_day6_mt_7dl_diary3", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day6_mt_7dl_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_mt_hent
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Memories",
            sdl_Replay(
                        "alt_day6_mt_7dl_memory", {"alt_replay_on" : "True"},
                        music = music_7dl["seven_summer_days"],
                        vars = [
                                    sdl_var_b_d5_me_neu_mt_hent,
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Concert",
            sdl_Replay(
                        "alt_day6_mt_7dl_concert", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_dj
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Speakers",
            sdl_Replay(
                        "alt_day6_mt_7dl_sonic", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_voya
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay("alt_day6_mt_7dl_supper", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Catapult",
            sdl_Replay(
                        "alt_day6_mt_7dl_catapult", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_mt_hent,
                                    sdl_var_i_karma
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Disco",
            sdl_Replay(
                        "alt_day6_mt_7dl_disco", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_mt_diar,
                                    sdl_var_b_d5_me_neu_mt_hent,
                                    sdl_var_i_mt_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Tea",
            sdl_Replay("alt_day6_mt_7dl_nighttime", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Hentai",
            sdl_Replay(
                        "alt_day6_mt_7dl_hentai", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_mt_hent
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 7 Day
    sdl_repl_array_mt_7dl_day7 = [
        sdl_repl_Label(
            "Dream",
            sdl_Replay("alt_day7_mt_7dl_begin", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day7_mt_7dl_morning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_mt_volo
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Olga-comet",
            sdl_Replay(
                        "alt_day7_mt_7dl_comet", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_mt_volo,
                                    sdl_var_e_d4_me_neu_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day7_mt_7dl_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_mt_hent,
                                    sdl_var_e_d4_me_neu_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Farewell. Slavya",
            sdl_Replay(
                        "alt_day7_mt_7dl_byes", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_mt_diar,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d3_me_dan2
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Farewell. Alisa",
            sdl_Replay("alt_day7_mt_7dl_dv_bye", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Farewell. Lena",
            sdl_Replay("alt_day7_mt_7dl_un_bye", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Farewell. Lena-FZ",
            sdl_Replay("alt_day7_mt_7dl_un_fz_bye", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Departure",
            sdl_Replay(
                        "alt_day7_mt_7dl_departure", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_mt_diar,
                                    sdl_var_b_d5_me_neu_mt_hent
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Choice",
            sdl_Replay("alt_day7_mt_7dl_choice", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Choice: past",
            sdl_Replay("alt_day7_mt_7dl_loopthru", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Choice: future",
            sdl_Replay("alt_day7_mt_7dl_loopback", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load)
        )
    ]

    ## Ulyana
    ### Ulyana-7DS
    #### 6 Day
    sdl_repl_array_us_7dl_day6 = [
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day6_us_7dl_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_us_7dl_pxs
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Lineup",
            sdl_Replay(
                        "alt_day6_us_7dl_exercises", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_us_7dl_pxs
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day6_us_7dl_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_us_7dl_pxs,
                                    sdl_var_e_d3_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Separated",
            sdl_Replay(
                        "alt_day6_us_7dl_separation", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_us_7dl_pxs,
                                    sdl_var_b_d5_me_neu_us_pota
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Help",
            sdl_Replay(
                        "alt_day6_us_7dl_helping", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_evening,
                        vars = [
                                    sdl_var_i_us_7dl,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d6_us_7dl_mi_frie,
                                    sdl_var_e_d6_us_7dl_sl_frie
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Morning. Miku",
            sdl_Replay(
                        "alt_day6_us_7dl_preps", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_tec2,
                                    sdl_var_i_mi_7dl,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Morning. Slavya",
            sdl_Replay(
                        "alt_day6_us_7dl_warehouse", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_us_7dl_pxs
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Morning. Lena",
            sdl_Replay(
                        "alt_day6_us_7dl_un_met", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_us_7dl_pxs,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d6_us_7dl_mi_frie
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day6_us_7dl_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_mi_7dl,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d6_us_7dl_mi_frie,
                                    sdl_var_e_d6_us_7dl_sl_frie
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Bear",
            sdl_Replay(
                        "alt_day6_us_7dl_button", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_b_d5_me_neu_pota,
                                    sdl_var_i_us_7dl_pxs
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Saving the deserter",
            sdl_Replay(
                        "alt_day6_us_7dl_deserter", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_i_us_lpp,
                                    sdl_var_i_us_7dl,
                                    sdl_var_i_us_7dl_pxs
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Ghost",
            sdl_Replay(
                        "alt_day6_us_7dl_ghost", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_b_d4_me_neu_voll,
                                    sdl_var_b_d5_me_neu_us_stor
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Fiasco",
            sdl_Replay(
                        "alt_day6_us_7dl_fiasco", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_day,
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Soundcheck",
            sdl_Replay(
                        "alt_day6_us_7dl_soundcheck", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_tec2,
                                    sdl_var_i_mi_7dl,
                                    sdl_var_i_us_7dl_pxs,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d6_us_7dl_mi_frie,
                                    sdl_var_e_d6_us_7dl_sl_frie
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Date",
            sdl_Replay(
                        "alt_day6_us_7dl_rendezvous", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_us_lpp,
                                    sdl_var_i_us_7dl_pxs
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Concert",
            sdl_Replay(
                        "alt_day6_us_7dl_concert", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_us_7dl_px_sl_join,
                                    sdl_var_i_us_7dl_pxs,
                                    sdl_var_e_d6_us_7dl_mi_frie,
                                    sdl_var_e_d6_us_7dl_sl_frie,
                                    sdl_var_e_d6_us_7dl_un_frie
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay(
                        "alt_day6_us_7dl_supper", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_us_7dl_help,
                                    sdl_var_i_mi_7dl,
                                    sdl_var_i_us_7dl_pxs,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d3_me_dan1,
                                    sdl_var_e_d6_us_7dl_mi_frie,
                                    sdl_var_e_d6_us_7dl_sl_frie
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Disco. Beginning",
            sdl_Replay(
                        "alt_day6_us_7dl_disco_prepare", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_us_7dl_help,
                                    sdl_var_i_mi_7dl,
                                    sdl_var_e_d6_us_7dl_mi_frie,
                                    sdl_var_e_d6_us_7dl_sl_frie,
                                    sdl_var_e_d6_us_7dl_un_frie
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Disco. Makeup",
            sdl_Replay(
                        "alt_day6_us_7dl_makeup", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_us_7dl_help,
                                    sdl_var_i_mi_7dl,
                                    sdl_var_i_us_7dl_pxs,
                                    sdl_var_e_d6_us_7dl_mi_frie,
                                    sdl_var_e_d6_us_7dl_un_frie
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Disco",
            sdl_Replay(
                        "alt_day6_us_7dl_disco", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_us_7dl_pxs,
                                    sdl_var_e_d3_me_dan1,
                                    sdl_var_e_d3_me_dan2,
                                    sdl_var_e_d6_us_7dl_mi_frie,
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Dance with Ulyana",
            sdl_Replay(
                        "alt_day6_us_7dl_us_dancing", {"alt_replay_on" : "True"},
                        music = music_7dl["stilllovingyou"],
                        vars = [
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_e_d6_us_7dl_un_frie
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Dance with Lena",
            sdl_Replay(
                        "alt_day6_us_7dl_un_dancing", {"alt_replay_on" : "True"},
                        music = music_7dl["stilllovingyou"],
                        vars = [
                                    sdl_var_i_un_7dl,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d4_me_neu_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Dance with Miku",
            sdl_Replay(
                        "alt_day6_us_7dl_mi_dancing", {"alt_replay_on" : "True"},
                        music = music_7dl["stilllovingyou"],
                        vars = [
                                    sdl_var_i_mi_7dl,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d2_mi_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Dance with Slavya",
            sdl_Replay(
                        "alt_day6_us_7dl_sl_dancing", {"alt_replay_on" : "True"},
                        music = music_7dl["stilllovingyou"],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Disco, forever alone",
            sdl_Replay(
                        "alt_day6_us_7dl_no_dancing", {"alt_replay_on" : "True"},
                        music = music_7dl["stilllovingyou"],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Tea party",
            sdl_Replay(
                        "alt_day6_us_7dl_tea", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_us_7dl_help
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day6_us_7dl_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_us_7dl_help,
                                    sdl_var_i_us_7dl_pxs,
                                    sdl_var_e_d6_us_7dl_mi_frie,
                                    sdl_var_e_d6_us_7dl_sl_frie,
                                    sdl_var_e_d6_us_7dl_un_frie
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Flares. Morning",
            sdl_Replay("alt_day6_us_7dl_px_begin", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Flares. Breakfast",
            sdl_Replay("alt_day6_us_7dl_px_breakfast", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Flares. Quarry",
            sdl_Replay("alt_day6_us_7dl_px_carrier", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Flares. Dinner",
            sdl_Replay("alt_day6_us_7dl_px_dinner", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Flares. LFG. Slavya",
            sdl_Replay("alt_day6_us_7dl_px_party_sl", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Flares. LFG. Lena",
            sdl_Replay("alt_day6_us_7dl_px_party_un", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Flares. Problems",
            sdl_Replay("alt_day6_us_7dl_px_far_gate", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Flares. Disco",
            sdl_Replay(
                        "alt_day6_us_7dl_px_disco", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_us_7dl_px_sl_join
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Flares. Happiness",
            sdl_Replay(
                        "alt_day6_us_7dl_px_afterwords", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_us_7dl_px_sl_join
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        )
    ]
    #### 7 Day
    sdl_repl_array_us_7dl_day7 = [
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day7_us_7dl_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_us_7dl_help,
                                    sdl_var_b_d6_us_7dl_px_sl_join,
                                    sdl_var_i_us_7dl_pxs,
                                    sdl_var_e_d6_us_7dl_mi_frie,
                                    sdl_var_e_d6_us_7dl_sl_frie,
                                    sdl_var_e_d6_us_7dl_un_frie
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day7_us_7dl_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_us_7dl_help,
                                    sdl_var_e_d6_us_7dl_mi_frie,
                                    sdl_var_e_d6_us_7dl_un_frie
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Pictures",
            sdl_Replay(
                        "alt_day7_us_7dl_photo", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_mi_snap,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_i_sl_clt
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Treehouse",
            sdl_Replay(
                        "alt_day7_us_7dl_treehouse", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_us_7dl_pxs
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Packing with Ulyana",
            sdl_Replay("alt_day7_us_7dl_packing_us", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Packing with Lena",
            sdl_Replay(
                        "alt_day7_us_7dl_packing_un", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl,
                                    sdl_var_e_d2_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Packing with Miku",
            sdl_Replay(
                        "alt_day7_us_7dl_packing_mi", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_mi_7dl,
                                    sdl_var_e_d2_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Packing. Alone",
            sdl_Replay(
                        "alt_day7_us_7dl_packing", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl,
                                    sdl_var_i_us_7dl_pxs
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Departure",
            sdl_Replay(
                        "alt_day7_us_7dl_leaving", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_us_7dl_help,
                                    sdl_var_i_mi_7dl,
                                    sdl_var_i_us_7dl_pxs,
                                    sdl_var_i_karma,
                                    sdl_var_e_d6_us_7dl_mi_frie,
                                    sdl_var_e_d6_us_7dl_un_frie
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Epilogue",
            sdl_Replay(
                        "alt_day7_us_7dl_wakeup", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_us_7dl_help,
                                    sdl_var_e_d6_us_7dl_mi_frie,
                                    sdl_var_e_d6_us_7dl_un_frie
                                ],
                        func_in = prolog_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Flares. Breakfast",
            sdl_Replay(
                        "alt_day7_us_7dl_px_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_us_7dl_px_sl_join
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Flares. Escape",
            sdl_Replay(
                        "alt_day7_us_7dl_px_escape", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_us_7dl_px_sl_join,
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Flares. Bus",
            sdl_Replay("alt_day7_us_7dl_px_bus", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Flares. Way back",
            sdl_Replay(
                        "alt_day7_us_7dl_px_mourning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_us_7dl_px_sl_join
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Flares. Wastelands",
            sdl_Replay("alt_day7_us_7dl_px_wastelands", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 5
        )
    ]

    ## Loner
    ### Loner
    #### 4 Day
    sdl_repl_array_me_neu_day4 = [
        sdl_repl_Label(
            "Morning. Cabin",
            sdl_Replay("alt_day4_me_neu_home", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Morning. Infirmary",
            sdl_Replay(
                        "alt_day4_me_neu_aid", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_i_mi_7dl,
                                    sdl_var_i_un_7dl,
                                    sdl_var_e_d2_conv,
                                    sdl_var_e_d3_date,
                                    sdl_var_e_d3_dj,
                                    sdl_var_e_d3_me_tec1,
                                    sdl_var_e_d3_me_dan1
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Morning. Alisa",
            sdl_Replay(
                        "alt_day4_me_neu_dv", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_dv_hous,
                                    sdl_var_b_d2_us_esca
                                    # Tournament int
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Infirmary. Slavya",
            sdl_Replay("alt_day4_me_neu_aid_sl", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Infirmary. Lena",
            sdl_Replay("alt_day4_me_neu_aid_un", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Infirmary. Ulyana",
            sdl_Replay("alt_day4_me_neu_aid_generic", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Miku. Cleaning",
            sdl_Replay(
                        "alt_day4_me_neu_mi", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_tec2,
                                    sdl_var_i_mi_7dl,
                                    sdl_var_e_d3_dj
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Slavya. Tasks",
            sdl_Replay(
                        "alt_day4_me_neu_sl", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl,
                                    sdl_var_i_sl_clt,
                                    sdl_var_l_d2_club
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lena. Amnesia",
            sdl_Replay(
                        "alt_day4_me_neu_un", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_lpp,
                                    sdl_var_e_d2_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Olga. Fire",
            sdl_Replay(
                        "alt_day4_me_neu_mt", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_tec2,
                                    sdl_var_e_d2_conv
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Ulyana. Snake",
            sdl_Replay(
                        "alt_day4_me_neu_us", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_b_d3_sl_bath,
                                    sdl_var_i_mi_lpp,
                                    sdl_var_i_dv_lpp,
                                    sdl_var_i_sl_lpp,
                                    sdl_var_i_un_lpp,
                                    sdl_var_e_d3_us_bugs
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay("alt_day4_me_neu_dinner", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Escape",
            sdl_Replay(
                        "alt_day4_me_neu_curl", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_esca
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Olga. Bicycle",
            sdl_Replay("alt_day4_me_neu_day_mt", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Ulyana. Changing",
            sdl_Replay(
                        "alt_day4_me_neu_day_us", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_esca
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lunch",
            sdl_Replay(
                        "alt_day4_me_neu_lunch", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_b_d3_me_tec2,
                                    sdl_var_i_us_lpp,
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Concert",
            sdl_Replay(
                        "alt_day4_me_neu_concert", {"alt_replay_on" : "True"},
                        meets = {'dn' : 'Curly'},
                        vars = [
                                    sdl_var_e_d4_me_neu_date
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Volleyball",
            sdl_Replay(
                        "alt_day4_me_neu_volley", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_sl_bath
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day4_me_neu_supper", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_voll,
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d2_mi_date,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Ice cream",
            sdl_Replay(
                        "alt_day4_me_neu_reward", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Pirate",
            sdl_Replay(
                        "alt_day4_me_neu_pirate", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_evening,
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "evening. Square",
            sdl_Replay(
                        "alt_day4_me_neu_square", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_voll
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Evening. Olga and Semyon's cabin",
            sdl_Replay(
                        "alt_day4_me_neu_map_me_mt_house1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_me_dan2,
                                    sdl_var_e_d4_me_neu_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Evening. Canteen",
            sdl_Replay("alt_day4_me_neu_map_dining_hall1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Evening. Stage",
            sdl_Replay(
                        "alt_day4_me_neu_map_estrade1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_me_neu_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Evening. Clubs",
            sdl_Replay(
                        "alt_day4_me_neu_map_cyber1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_us_debt
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Evening. Administration",
            sdl_Replay(
                        "alt_day4_me_neu_map_admin_house1", {"alt_replay_on" : "True"},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Evening. Boat station",
            sdl_Replay(
                        "alt_day4_me_neu_map_boat_station1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_date,
                                    sdl_var_i_dv_7dl,
                                    sdl_var_e_d3_dj,
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Miku. Songs",
            sdl_Replay(
                        "alt_day4_me_neu_songs", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_me_neu_date
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Alisa. Prank",
            sdl_Replay(
                        "alt_day4_me_neu_prank", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_voll,
                                    sdl_var_i_us_7dl
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Olga. Diary P-1",
            sdl_Replay(
                        "alt_day4_me_neu_mt_diary_vol1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_voll
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Ulyana. Candies",
            sdl_Replay(
                        "alt_day4_me_neu_us_candies", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_voll
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Ulyana. Guardsmen",
            sdl_Replay(
                        "alt_day4_me_neu_us_guards", {"alt_replay_on" : "True"},
                        meets = {'dn' : 'Curly', 'tn' : 'Strange boy'},
                        vars = [
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_i_us_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Ulyana. Flares",
            sdl_Replay("alt_day4_me_neu_us_launch", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day4_me_neu_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_mt_diar,
                                    sdl_var_i_mt_7dl,
                                    sdl_var_i_us_7dl,
                                    sdl_var_i_us_7dl_pxs,
                                    sdl_var_e_d4_me_neu_date
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 5 Day
    sdl_repl_array_me_neu_day5 = [
        sdl_repl_Label(
            "Dream",
            sdl_Replay("alt_day5_me_neu_morningdream", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Morning",
            sdl_Replay(
                        "alt_day5_me_neu_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_voll,
                                    sdl_var_i_us_7dl_pxs
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Breakfast",
            sdl_Replay(
                        "alt_day5_me_neu_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_voll,
                                    sdl_var_b_d4_me_neu_mi_song,
                                    sdl_var_b_d4_me_neu_mt_diar,
                                    sdl_var_i_us_7dl_pxs,
                                    sdl_var_i_un_fzd_mt,
                                    sdl_var_e_d4_me_neu_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Rain",
            sdl_Replay(
                        "alt_day5_me_neu_rain", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d5_me_neu_cand
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Quiet hour",
            sdl_Replay("alt_day5_me_neu_along", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Candle",
            sdl_Replay(
                        "alt_day5_me_neu_cndl", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_tec2,
                                    sdl_var_e_d3_dj,
                                    sdl_var_e_d3_me_tec1,
                                    sdl_var_e_d3_us_bugs,
                                    sdl_var_e_d5_me_neu_cand,
                                    sdl_var_i_mt_7dl,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Candle. Escape",
            sdl_Replay(
                        "alt_day5_me_neu_cndl_esc", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_dv_lpp,
                                    sdl_var_e_d4_me_neu_date,
                                    sdl_var_b_d3_me_tec2,
                                    sdl_var_i_mt_7dl
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Candle. Answers. Herc",
            sdl_Replay(
                        "alt_day5_me_neu_day_answ_h", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Candle. Answers. Loki",
            sdl_Replay(
                        "alt_day5_me_neu_day_answ_l", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Candle. Answers. Wimp",
            sdl_Replay(
                        "alt_day5_me_neu_day_answ_d", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Gaming",
            sdl_Replay(
                        "alt_day5_me_neu_gaming", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_tec2,
                                    sdl_var_l_d2_club
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Convicted",
            sdl_Replay(
                        "alt_day5_me_neu_arrest", {"alt_replay_on" : "True"},
                        meets = {'dn' : 'Curly', 'tn' : 'Strange boy'},
                        meet_restr = {'dn' : 'loki', 'tn' : 'loki'},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Dinner",
            sdl_Replay(
                        "alt_day5_me_neu_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_mi_song,
                                    sdl_var_i_us_7dl_pxs,
                                    sdl_var_e_d4_me_neu_date,
                                    sdl_var_e_d5_me_neu_cand
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Miku. Stage",
            sdl_Replay(
                        "alt_day5_me_neu_mi_estrade", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_voll,
                                    sdl_var_b_d4_me_neu_mi_song
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Miku. Help",
            sdl_Replay(
                        "alt_day5_me_neu_mi_help", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_b_d4_me_neu_mi_song,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Olga. Beach",
            sdl_Replay(
                        "alt_day5_me_neu_mt_beach", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_mt_diar,
                                    sdl_var_i_mt_7dl,
                                    sdl_var_e_d3_me_dan2
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Clubs. Cybernetic",
            sdl_Replay(
                        "alt_day5_me_neu_cyber_sh", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Clubs. Newspaper",
            sdl_Replay(
                        "alt_day5_me_neu_nwsppr_sh", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_me_neu_answ,
                                    sdl_var_b_d4_me_neu_mz_news
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Clubs. Sport",
            sdl_Replay(
                        "alt_day5_me_neu_sport_sh", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Ulyana. Longing",
            sdl_Replay(
                        "alt_day5_me_neu_us_melancholy", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_us_stor
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Ulyana. Quarry",
            sdl_Replay("alt_day5_me_neu_us_career", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Ulyana. Got caught",
            sdl_Replay(
                        "alt_day5_me_neu_us_caught", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_us_stor
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Lunch",
            sdl_Replay(
                        "alt_day5_me_neu_lunch", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_sl_chas,
                                    sdl_var_b_d4_me_neu_voll,
                                    sdl_var_e_d5_me_neu_mt_voye
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Spy gaming",
            sdl_Replay(
                        "alt_day5_me_neu_sl_secret", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_me_neu_date
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Supper",
            sdl_Replay(
                        "alt_day5_me_neu_supper", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_sl_voye,
                                    sdl_var_i_mt_7dl,
                                    sdl_var_i_us_7dl,
                                    sdl_var_e_d4_me_neu_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Ulyana. Punishment",
            sdl_Replay(
                        "alt_day5_me_neu_us_punishment", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_us_stor
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Ulyana. Satiated",
            sdl_Replay("alt_day5_me_neu_us_full", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Ulyana. Hungry",
            sdl_Replay(
                        "alt_day5_me_neu_us_hungry", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key,
                                    sdl_var_e_d4_me_neu_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Evening",
            sdl_Replay(
                        "alt_day5_me_neu_evening", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_tec2,
                                    sdl_var_b_d5_me_neu_pota,
                                    sdl_var_e_d5_me_neu_cand
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Hike",
            sdl_Replay(
                        "alt_day5_me_neu_campfire", {"alt_replay_on" : "True"},
                        ambience = ambience_forest_evening,
                        vars = [
                                    sdl_var_b_d5_me_neu_pota
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Map. DvaChe cabin",
            sdl_Replay(
                        "alt_day5_me_neu_map_house_dv1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key,
                                    sdl_var_i_me_neu_answ
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Map. Warehouse",
            sdl_Replay(
                        "alt_day5_me_neu_map_shed1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Map. Infirmary",
            sdl_Replay(
                        "alt_day5_me_neu_map_medic_house1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_cs_debt,
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 6
        ),
        sdl_repl_Label(
            "Map. Boat station",
            sdl_Replay(
                        "alt_day5_me_neu_map_boat_station1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_me_neu_answ
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Map. Clubs",
            sdl_Replay(
                        "alt_day5_me_neu_map_cyber1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Map. Football field",
            sdl_Replay(
                        "alt_day5_me_neu_map_playground1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_sprt
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Map. Beach",
            sdl_Replay(
                        "alt_day5_me_neu_map_beach1", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Map. Library",
            sdl_Replay(
                        "alt_day5_me_neu_map_library1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key,
                                    sdl_var_i_me_neu_answ,
                                    sdl_var_b_d5_me_neu_nwpp
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Map. Loser",
            sdl_Replay(
                        "alt_day5_me_neu_map_fail", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Evening. Answer. Herc",
            sdl_Replay(
                        "alt_day5_me_neu_evening_answ_h", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Evening. Answers. Loki",
            sdl_Replay(
                        "alt_day5_me_neu_evening_answ_l", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Evening. Answers. Wimp",
            sdl_Replay(
                        "alt_day5_me_neu_evening_answ_d", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Ulyana. Hide-n-Seek",
            sdl_Replay("alt_day5_me_neu_us_hideandseek", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Ulyana. Swimming",
            sdl_Replay("alt_day5_me_neu_us_warm_evening", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Ulyana. Robbery",
            sdl_Replay(
                        "alt_day5_me_neu_us_robbery", {"alt_replay_on" : "True"},
                        music = music_list["eat_some_trouble"],
                        vars = [
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Ulyana. Cleaning",
            sdl_Replay("alt_day5_me_neu_us_cleaning", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Lights out",
            sdl_Replay(
                        "alt_day5_me_neu_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_mt_diar,
                                    sdl_var_b_d5_me_neu_sl_voye,
                                    sdl_var_i_mt_7dl,
                                    sdl_var_i_us_7dl,
                                    sdl_var_e_d5_me_neu_mt_voye
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lights out. Wet",
            sdl_Replay(
                        "alt_day5_me_neu_sleeptime_wet", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_cesc,
                                    sdl_var_b_d5_me_neu_cybr,
                                    sdl_var_b_d5_me_neu_sl_voye,
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_i_mt_7dl
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lights out. Drunk",
            sdl_Replay(
                        "alt_day5_me_neu_sleeptime_drunk", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_cs_debt
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lights out. Escaped",
            sdl_Replay(
                        "alt_day5_me_neu_sleeptime_map", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_cesc,
                                    sdl_var_e_d5_me_neu_mapi,
                                    sdl_var_i_dv_lpp
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Lights out. Answers. Herc",
            sdl_Replay(
                        "alt_day5_me_neu_sleeptime_answ_h", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Lights out. Answers. Wimp",
            sdl_Replay(
                        "alt_day5_me_neu_sleeptime_answ_d", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),

        sdl_repl_Label(
            "Ulyana. Lights out",
            sdl_Replay(
                        "alt_day5_me_neu_us_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_us_stor
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Olga. Diary P-2",
            sdl_Replay(
                        "alt_day5_me_neu_mt_retrib", {"alt_replay_on" : "True"},
                        ambience = ambience_int_cabin_night,
                        vars = [
                                    sdl_var_b_d4_me_neu_mt_diar
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Olga. «Tea party»",
            sdl_Replay(
                        "alt_day5_me_neu_mt_tea_party", {"alt_replay_on" : "True"},
                        ambience = ambience_int_cabin_night,
                        vars = [
                                    sdl_var_e_d2_date,
                                    sdl_var_e_d5_me_neu_mt_voye
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]

    sdl_repl_label_frozen = [
                             ]

    # Days

    ## Common
    sdl_repl_common_day0 = sdl_repl_Day("Prologue", sdl_repl_array_common_day0)
    sdl_repl_common_day1 = sdl_repl_Day("Day 1", sdl_repl_array_common_day1)
    sdl_repl_common_day2 = sdl_repl_Day("Day 2", sdl_repl_array_common_day2)
    sdl_repl_common_day3 = sdl_repl_Day("Day 3", sdl_repl_array_common_day3)
    sdl_repl_common_days = [
        sdl_repl_common_day0,
        sdl_repl_common_day1,
        sdl_repl_common_day2,
        sdl_repl_common_day3
    ]

    ## Miku
    ### Miku-7DS
    sdl_repl_mi_7dl_day4 = sdl_repl_Day("Day 4", sdl_repl_array_mi_7dl_day4)
    sdl_repl_mi_7dl_day5 = sdl_repl_Day("Day 5", sdl_repl_array_mi_7dl_day5)
    sdl_repl_mi_7dl_day6 = sdl_repl_Day("Day 6", sdl_repl_array_mi_7dl_day6)
    sdl_repl_mi_7dl_day7 = sdl_repl_Day("Day 7", sdl_repl_array_mi_7dl_day7)
    sdl_repl_mi_7dl_days = [
        sdl_repl_mi_7dl_day4,
        sdl_repl_mi_7dl_day5,
        sdl_repl_mi_7dl_day6,
        sdl_repl_mi_7dl_day7
    ]
    ### Miku-DJ
    sdl_repl_mi_djt_day4 = sdl_repl_Day("Day 4", sdl_repl_array_mi_djt_day4)
    sdl_repl_mi_djt_day5 = sdl_repl_Day("Day 5", sdl_repl_array_mi_djt_day5)
    sdl_repl_mi_djt_day6 = sdl_repl_Day("Day 6", sdl_repl_array_mi_djt_day6)
    sdl_repl_mi_djt_day7 = sdl_repl_Day("Day 7", sdl_repl_array_mi_djt_day7)
    sdl_repl_mi_djt_days = [
        sdl_repl_mi_djt_day4,
        sdl_repl_mi_djt_day5,
        sdl_repl_mi_djt_day6,
        sdl_repl_mi_djt_day7
    ]

    ## Alisa
    ### Alisa-7DS
    sdl_repl_dv_7dl_day4 = sdl_repl_Day("Day 4", sdl_repl_array_dv_7dl_day4)
    sdl_repl_dv_7dl_day5 = sdl_repl_Day("Day 5", sdl_repl_array_dv_7dl_day5)
    sdl_repl_dv_7dl_day6 = sdl_repl_Day("Day 6", sdl_repl_array_dv_7dl_day6)
    sdl_repl_dv_7dl_day7 = sdl_repl_Day("Day 7", sdl_repl_array_dv_7dl_day7)
    sdl_repl_dv_7dl_days = [
        sdl_repl_dv_7dl_day4,
        sdl_repl_dv_7dl_day5,
        sdl_repl_dv_7dl_day6,
        sdl_repl_dv_7dl_day7
    ]
    ### Alisa-DJ
    sdl_repl_dv_djt_day4 = sdl_repl_Day("Day 4", sdl_repl_array_dv_djt_day4)
    sdl_repl_dv_djt_day5 = sdl_repl_Day("Day 5", sdl_repl_array_dv_djt_day5)
    sdl_repl_dv_djt_day6 = sdl_repl_Day("Day 6", sdl_repl_array_dv_djt_day6)
    sdl_repl_dv_djt_day7 = sdl_repl_Day("Day 7", sdl_repl_array_dv_djt_day7)
    sdl_repl_dv_djt_days = [
        sdl_repl_dv_djt_day4,
        sdl_repl_dv_djt_day5,
        sdl_repl_dv_djt_day6,
        sdl_repl_dv_djt_day7
    ]

    ## Slavya
    ### Slavya-7DS
    sdl_repl_sl_7dl_day4 = sdl_repl_Day("Day 4", sdl_repl_array_sl_7dl_day4)
    sdl_repl_sl_7dl_day5 = sdl_repl_Day("Day 5", sdl_repl_array_sl_7dl_day5)
    sdl_repl_sl_7dl_day6 = sdl_repl_Day("Day 6", sdl_repl_array_sl_7dl_day6)
    sdl_repl_sl_7dl_day7 = sdl_repl_Day("Day 7", sdl_repl_array_sl_7dl_day7)
    sdl_repl_sl_7dl_days = [
        sdl_repl_sl_7dl_day4,
        sdl_repl_sl_7dl_day5,
        sdl_repl_sl_7dl_day6,
        sdl_repl_sl_7dl_day7
    ]
    ### Slavya-Classic
    sdl_repl_sl_clt_day4 = sdl_repl_Day("Day 4", sdl_repl_array_sl_clt_day4)
    sdl_repl_sl_clt_day5 = sdl_repl_Day("Day 5", sdl_repl_array_sl_clt_day5)
    sdl_repl_sl_clt_day6 = sdl_repl_Day("Day 6", sdl_repl_array_sl_clt_day6)
    sdl_repl_sl_clt_day7 = sdl_repl_Day("Day 7", sdl_repl_array_sl_clt_day7)
    sdl_repl_sl_clt_dayx = sdl_repl_Day("Day ???", sdl_repl_array_sl_clt_dayx)
    sdl_repl_sl_clt_days = [
        sdl_repl_sl_clt_day4,
        sdl_repl_sl_clt_day5,
        sdl_repl_sl_clt_day6,
        sdl_repl_sl_clt_day7,
        sdl_repl_sl_clt_dayx
    ]

    ## Lena
    ### Lena-7DS
    sdl_repl_un_7dl_day4 = sdl_repl_Day("Day 4", sdl_repl_array_un_7dl_day4)
    sdl_repl_un_7dl_day5 = sdl_repl_Day("Day 5", sdl_repl_array_un_7dl_day5)
    sdl_repl_un_7dl_day6 = sdl_repl_Day("Day 6", sdl_repl_array_un_7dl_day6)
    sdl_repl_un_7dl_day7 = sdl_repl_Day("Day 7", sdl_repl_array_un_7dl_day7)
    sdl_repl_un_7dl_days = [
        sdl_repl_un_7dl_day4,
        sdl_repl_un_7dl_day5,
        sdl_repl_un_7dl_day6,
        sdl_repl_un_7dl_day7
    ]
    ### Lena-FZ
    sdl_repl_un_fzd_day4 = sdl_repl_Day("Day 4", sdl_repl_array_un_fzd_day4, char_mask=2)
    sdl_repl_un_fzd_day5 = sdl_repl_Day("Day 5", sdl_repl_array_un_fzd_day5, char_mask=2)
    sdl_repl_un_fzd_day6 = sdl_repl_Day("Day 6. The Road", sdl_repl_array_un_fzd_day6, char_mask=2)
    sdl_repl_un_fzd_day62 = sdl_repl_Day("Day 6. FZ", sdl_repl_array_un_fzd_day62, char_mask=2)
    sdl_repl_un_fzd_day7 = sdl_repl_Day("Day 7. FZ", sdl_repl_array_un_fzd_day7, char_mask=2)
    sdl_repl_un_fzd_days = [
        sdl_repl_un_fzd_day4,
        sdl_repl_un_fzd_day5,
        sdl_repl_un_fzd_day6,
        sdl_repl_un_fzd_day62,
        sdl_repl_un_fzd_day7
    ]

    ## Olga
    ### Olga-7DS
    sdl_repl_mt_7dl_day6 = sdl_repl_Day("Day 6", sdl_repl_array_mt_7dl_day6)
    sdl_repl_mt_7dl_day7 = sdl_repl_Day("Day 7", sdl_repl_array_mt_7dl_day7)
    sdl_repl_mt_7dl_days = [
        sdl_repl_mt_7dl_day6,
        sdl_repl_mt_7dl_day7
    ]

    ## Ulyana
    ### Ulyana-7DS
    sdl_repl_us_7dl_day6 = sdl_repl_Day("Day 6", sdl_repl_array_us_7dl_day6, char_mask=5)
    sdl_repl_us_7dl_day7 = sdl_repl_Day("Day 7", sdl_repl_array_us_7dl_day7, char_mask=5)
    sdl_repl_us_7dl_days = [
        sdl_repl_us_7dl_day6,
        sdl_repl_us_7dl_day7
    ]

    ## Loner
    ### Loner
    sdl_repl_me_neu_day4 = sdl_repl_Day("Day 4", sdl_repl_array_me_neu_day4)
    sdl_repl_me_neu_day5 = sdl_repl_Day("Day 5", sdl_repl_array_me_neu_day5)
    sdl_repl_me_neu_days = [
        sdl_repl_me_neu_day4,
        sdl_repl_me_neu_day5
    ]

    # Routes | Sections

    ## Common
    sdl_repl_common = sdl_repl_Section("Common-route", None, None, sdl_repl_common_days)

    ## Miku
    sdl_repl_mi_7dl = sdl_repl_Section("Miku-7DS",     None, None, sdl_repl_mi_7dl_days)
    sdl_repl_mi_djt = sdl_repl_Section("Miku-DJ",  None, None, sdl_repl_mi_djt_days)
    sdl_repl_mi_routes = [
        sdl_repl_mi_7dl,
        sdl_repl_mi_djt
    ]
    sdl_repl_mi = sdl_repl_Section("Miku", "sdl_repl_section_label_mi", sdl_repl_mi_routes, None)

    ## Alisa
    sdl_repl_dv_7dl = sdl_repl_Section("Alisa-7DS",     None, None, sdl_repl_dv_7dl_days)
    sdl_repl_dv_djt = sdl_repl_Section("Alisa-DJ",  None, None, sdl_repl_dv_djt_days)
    sdl_repl_dv_routes = [
        sdl_repl_dv_7dl,
        sdl_repl_dv_djt
    ]
    sdl_repl_dv = sdl_repl_Section("Alisa", "sdl_repl_section_label_dv", sdl_repl_dv_routes, None)

    ## Slavya
    sdl_repl_sl_7dl = sdl_repl_Section("Slavya-7DS",     None, None, sdl_repl_sl_7dl_days)
    sdl_repl_sl_clt = sdl_repl_Section("Slavya-Classic", None, None, sdl_repl_sl_clt_days)
    sdl_repl_sl_routes = [
        sdl_repl_sl_7dl,
        sdl_repl_sl_clt
    ]
    sdl_repl_sl = sdl_repl_Section("Slavya", "sdl_repl_section_label_sl", sdl_repl_sl_routes, None)

    ## Lena
    sdl_repl_un_7dl = sdl_repl_Section("Lena-7DS",       None, None, sdl_repl_un_7dl_days)
    sdl_repl_un_fzd = sdl_repl_Section("Lena-Friendzone", None, None, sdl_repl_un_fzd_days)
    sdl_repl_un_routes = [
        sdl_repl_un_7dl,
        sdl_repl_un_fzd
    ]
    sdl_repl_un = sdl_repl_Section("Lena", "sdl_repl_section_label_un", sdl_repl_un_routes, None)

    ## Olga
    sdl_repl_mt_7dl = sdl_repl_Section("Olga-7DS",       None, None, sdl_repl_mt_7dl_days)
    sdl_repl_mt_routes = [
        sdl_repl_mt_7dl
    ]
    sdl_repl_mt = sdl_repl_Section("Olga", "sdl_repl_section_label_mt", sdl_repl_mt_routes, None)

    ## Ulyana
    sdl_repl_us_7dl = sdl_repl_Section("Ulyana-7DS",     None, None, sdl_repl_us_7dl_days)
    sdl_repl_us_routes = [
        sdl_repl_us_7dl
    ]
    sdl_repl_us = sdl_repl_Section("Ulyana", "sdl_repl_section_label_us", sdl_repl_us_routes, None)

    ## Loner
    sdl_repl_me_neu = sdl_repl_Section("Semyon-Loner", None, None, sdl_repl_me_neu_days)
    sdl_repl_me_routes = [
        sdl_repl_me_neu
    ]
    sdl_repl_me = sdl_repl_Section("Semyon", "sdl_repl_section_label_me", sdl_repl_me_routes, None)

    sdl_repl_sections = [
        sdl_repl_common,
        sdl_repl_mi,
        sdl_repl_dv,
        sdl_repl_sl,
        sdl_repl_un,
        sdl_repl_mt,
        sdl_repl_us,
        sdl_repl_me
    ]



    # Protags
    sdl_repl_characters = [
        sdl_Character("sdl_repl_char_none", 15, None, None),
        sdl_Character("sdl_repl_char_loki", 4, "sdl_repl_char_label_loki", "loki"),
        sdl_Character("sdl_repl_char_herc", 2, "sdl_repl_char_label_herc", "herc"),
        sdl_Character("sdl_repl_char_dr",   1, "sdl_repl_char_label_dr",   "dr")
    ]



    sdl_repl_engine = sdl_repl_Engine(sdl_repl_sections)
