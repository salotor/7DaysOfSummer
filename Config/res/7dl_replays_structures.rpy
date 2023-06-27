init 9999 python:
    # Лейблы

    ## Коммон
    ### 0 День
    sdl_repl_array_common_day0 = [
        sdl_repl_Label(
            "Локи",
            sdl_Replay("alt_day0_start_l", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Герк",
            sdl_Replay("alt_day0_start_h", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Дрищ",
            sdl_Replay("alt_day0_start_d", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            char_mask = 1
        )
    ]
    ### 1 День
    sdl_repl_array_common_day1 = [
        sdl_repl_Label(
            "Начало",
            sdl_Replay("alt_day1_begin", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Пробуждение",
            sdl_Replay(
                        "alt_day1_bus_start", {"alt_replay_on" : "True"},
                        music = music_7dl["areyouabully"],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Первое знакомство",
            sdl_Replay(
                        "alt_day1_firts_met", {"alt_replay_on" : "True"},
                        meets = {'sl' : 'Блондинка'},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Прибытие",
            sdl_Replay(
                        "alt_day1_arrival", {"alt_replay_on" : "True"},
                        meets = {'dv' : 'Рыжая', 'sl' : 'Блондинка', 'un' : 'Грустная девочка', 'us' : 'Мелкая'},
                        meet_restr = {'sl' : 'alt_day1_sl_met'},
                        vars = [
                                    sdl_var_b_d1_sl_met,
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Побег от рыжих",
            sdl_Replay("alt_day1_chase1", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 6
        ),
        sdl_repl_Label(
            "Склад",
            sdl_Replay(
                        "alt_day1_warehouse", {"alt_replay_on" : "True"},
                        meets = {'sl' : 'Блондинка'},
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 6
        ),
        sdl_repl_Label(
            "Вожатая",
            sdl_Replay(
                        "alt_day1_mod_tan", {"alt_replay_on" : "True"},
                        meets = {'cs' : 'Медсестра', 'mt' : 'Вожатая', 'sl' : 'Блондинка', 'us' : 'Мелкая'},
                        meet_restr = {'sl' : 'alt_day1_sl_met'},
                        vars = [
                                    sdl_var_b_d1_sl_met,
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Электроник",
            sdl_Replay(
                        "alt_day1_elektron", {"alt_replay_on" : "True"},
                        meets = {'el' : "Кудрявый"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Экскурсия",
            sdl_Replay(
                        "alt_day1_meeting", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Футбольное поле",
            sdl_Replay(
                        "alt_day1_soccer_d1", {"alt_replay_on" : "True"},
                        meets = {'us' : 'Мелкая'},
                        vars = [
                                    sdl_var_b_d1_el_foll,
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Ужин",
            sdl_Replay(
                        "alt_day1_supper", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Экскурсия. Вечер",
            sdl_Replay(
                        "alt_day1_meeting2", {"alt_replay_on" : "True"},
                        meets = {'al' : 'Сердитый мальчик', 'dn' : 'Кудрявый'},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Погоня",
            sdl_Replay(
                        "alt_day1_chase", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Погоня. Хэдшот",
            sdl_Replay(
                        "alt_day1_headshot", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Погоня. Не догнал",
            sdl_Replay(
                        "alt_day1_nocatch", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Спасительница",
            sdl_Replay(
                        "alt_day1_slavya_saviour", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d1_us_shot
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Лена",
            sdl_Replay(
                        "alt_day1_lena", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Отбой",
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
    ### 2 День
    sdl_repl_array_common_day2 = [
        sdl_repl_Label(
            "Утро",
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
            "Линейка",
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
            "Завтрак",
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
            "Обход с Леной",
            sdl_Replay(
                        "alt_day2_un_guide", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_brf
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Обход со Славей",
            sdl_Replay("alt_day2_sl_guide", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Обход. Выбор спутницы",
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
            "Обход. Музклуб",
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
            "Обход. Музклуб. Внутри",
            sdl_Replay(
                        "alt_day2_inmusic", {"alt_replay_on" : "True"},
                        meets = {'mi' : 'Японка'},
                        vars = [
                                    sdl_var_e_d2_conv,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Обход. Клубы",
            sdl_Replay(
                        "alt_day2_event_clubs1", {"alt_replay_on" : "True"},
                        meets = {'sh' : 'Очкарик'},
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
            "Обход. Стоянка",
            sdl_Replay("alt_day2_event_camp_entrance1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Обход. Дом рыжих",
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
            "Обход. Столовая",
            sdl_Replay("alt_day2_event_dining_hall1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Обход. Спортплощадка",
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
            "Обход. Пляж",
            sdl_Replay(
                        "alt_day2_event_beach1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_conv
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Обход. Дом Семёна и Ольги",
            sdl_Replay("alt_day2_event_me_mt_house1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Обход. Библиотека",
            sdl_Replay(
                        "alt_day2_event_library1", {"alt_replay_on" : "True"},
                        meets = {'sh' : 'Очкарик'},
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
            "Обход. Библиотека. Женя",
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
            "Обход. Медпункт",
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
            "Обход. Площадь",
            sdl_Replay("alt_day2_event_square_1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_conv,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Обход. Площадь. Повторно",
            sdl_Replay("alt_day2_event_square_dunno", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Обход. Площадь. Ключи",
            sdl_Replay(
                        "alt_day2_sl_hyst", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Обход. Лодочная станция",
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
            "Обход. Эстрада",
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
            "Эстрада. Осмотр",
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
            "Эстрада. Микрофон",
            sdl_Replay("alt_day2_phone", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Эстрада. Миниджек",
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
            "Обед",
            sdl_Replay(
                        "alt_day2_dinner", {"alt_replay_on" : "True"},
                        meets = {'mi' : 'Японка'},
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
            "Великий побег",
            sdl_Replay(
                        "alt_day2_grand_escape", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_conv
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Тихий час",
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
            "Подготовка к турниру",
            sdl_Replay(
                        "alt_day2_tournament", {"alt_replay_on" : "True"},
                        meets = {'mi' : 'Японка'},
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
            "За картами. Один",
            sdl_Replay("alt_day2_walk_alone", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "За картами. Со Славей",
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
            "Ультиматум",
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
            "Турнир",
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
            "Ужин",
            sdl_Replay(
                        "alt_day2_supper", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                    # переменные турнира
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Ужин. Продолжение",
            sdl_Replay(
                        "alt_day2_sup2", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_us_cake,
                                    sdl_var_i_sl_lpp,
                                    sdl_var_i_sl_7dl,
                                    sdl_var_e_d2_dv_ulti
                                    # переменные турнира
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Погоня за Ульяной",
            sdl_Replay(
                        "alt_day2_slot_us_try", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_us_lpp
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Вечер. Пляж",
            sdl_Replay(
                        "alt_day2_eventEv_beach1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_b_d2_dv_chas,
                                    sdl_var_i_dv_lpp,
                                    sdl_var_e_d2_dv_ulti,
                                    sdl_var_l_d2_jclu
                                    # переменные турнира
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Вечер. Музклуб",
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
            "Вечер. Клубы",
            sdl_Replay("alt_day2_eventEv_clubs1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Вечер. Стоянка",
            sdl_Replay("alt_day2_eventEv_camp_entrance1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Вечер. Столовая",
            sdl_Replay("alt_day2_eventEv_dining_hall1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Вечер. Спортплощадка",
            sdl_Replay(
                        "alt_day2_eventEv_sport_area1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_lpp,
                                    sdl_var_e_d2_conv,
                                    sdl_var_l_d2_voya
                                    # переменные турнира
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Вечер. Дом Лены и Мику",
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
                                    # переменные турнира
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Вечер. Дом рыжих",
            sdl_Replay("alt_day2_eventEv_dv_us_house1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Вечер. Дом Семёна и Ольги",
            sdl_Replay(
                        "alt_day2_eventEv_me_mt_house1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_clt
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Вечер. Библиотека",
            sdl_Replay("alt_day2_eventEv_library1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Вечер. Медпункт",
            sdl_Replay(
                        "alt_day2_eventEv_medic_house1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Вечер. Эстрада",
            sdl_Replay(
                        "alt_day2_eventEv_estrade1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_me_mini
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Вечер. Площадь",
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
            "Вечер. Пристань",
            sdl_Replay(
                        "alt_day2_eventEv_boat_station1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_dv_chas
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Вечер с Мику",
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
            "Вечер с Алисой",
            sdl_Replay(
                        "alt_day2_slot_dv", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_b_d2_dv_chas,
                                    sdl_var_i_dv_lpp,
                                    sdl_var_e_d2_dv_ulti,
                                    sdl_var_l_d2_jclu
                                    # переменные турнира
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Вечер со Славей",
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
            "Вечер с Леной (Локи)",
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
            "Вечер с Леной (Герк)",
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
                                    # переменные турнира
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Вечер с Леной (Дрищ)",
            sdl_Replay(
                        "alt_day2_slot_un", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_evening,
                        vars = [
                                    sdl_var_e_d2_conv,
                                    sdl_var_l_d2_voya
                                    # переменные турнира
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Вечер с Ольгой",
            sdl_Replay(
                        "alt_day2_slot_mt", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_clt
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Вечер с Ульяной",
            sdl_Replay(
                        "alt_day2_slot_us", {"alt_replay_on" : "True"},
                        vars = None,    # переменные турнира
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Отбой",
            sdl_Replay(
                        "alt_day2_dream", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_b_d2_mt_help,
                                    sdl_var_e_d2_date,
                                    sdl_var_l_d2_voya
                                    # переменные турнира
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    ### 3 День
    sdl_repl_array_common_day3 = [
        sdl_repl_Label(
            "Утро",
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
                                    # переменные турнира
                                ],
                        func_in = prolog_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Завтрак",
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
            "Дежурство",
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
            "Утро. Музклуб",
            sdl_Replay(
                        "alt_day3_event_music_club1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Утро. Клубы",
            sdl_Replay(
                        "alt_day3_event_clubs1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_club
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Утро. Стоянка",
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
            "Утро. Столовая",
            sdl_Replay(
                        "alt_day3_event_dining_hall1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Утро. Спортплощадка",
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
            "Утро. Пляж",
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
            "Утро. Библиотека",
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
            "Утро. Медпункт",
            sdl_Replay(
                        "alt_day3_event_medic_house1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Утро. Эстрада",
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
            "Утро. Площадь",
            sdl_Replay("alt_day3_event_square1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Утро. Пристань",
            sdl_Replay("alt_day3_event_boat_station1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Утро с Мику",
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
            "Утро с Алисой",
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
            "Утро со Славей",
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
            "Утро с Леной",
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
            "Операция «Ы»",
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
            "Обед",
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
            "День. Клубы",
            sdl_Replay("alt_day3_eventAf_clubs_technoquest", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "День. Клубы. Продолжение",
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
            "День. Музклуб",
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
                                    # переменные турнира
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "День. Дом Лены и Мику",
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
            "День. Столовая",
            sdl_Replay(
                        "alt_day3_eventAf_dining_hall1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "День. Админ. корпус",
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
            "День. Дом Семёна и Ольги",
            sdl_Replay("alt_day3_eventAf_me_mt_house1", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "День. Библиотека",
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
            "День. Эстрада",
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
            "Выбор диджея. Мику",
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
            "Выбор диджея. Алиса",
            sdl_Replay(
                        "alt_day3_day_dv_dj", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_dv_guit
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "День с Мику",
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
            "День с Алисой",
            sdl_Replay(
                        "alt_day3_day_dv", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_b_d3_mi_reje
                                    # переменные турнира
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "День с Леной",
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
            "День Френдзоны",
            sdl_Replay("alt_day3_day_un_fz", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 2
         ),
         sdl_repl_Label(
            "Подготовка с Алисой",
            sdl_Replay(
                        "alt_day3_day_un_fz_dv", {"alt_replay_on" : "True"},
                        meets = {'dn' : 'Кудрявый', 'ka' : 'Вожатая 2 отряда'},
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
            "Подготовка со Славей",
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
            "Подготовка с Леной",
            sdl_Replay(
                        "alt_day3_day_un_fz_un", {"alt_replay_on" : "True"},
                        music = music_list["so_good_to_be_careless"],
                        ambience = ambience_camp_center_day,
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
         ),
        sdl_repl_Label(
            "Полдник со Славей",
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
            "Полдник с Ульяной",
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
            "Кошмар",
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
            "Вечер Френдзоны",
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
            "Сон. Лена",
            sdl_Replay("alt_day3_un_fz_dream_un", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Сон. Дорога",
            sdl_Replay("alt_day3_un_fz_dream_road", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Ужин",
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
            "Ужин с Ульяной",
            sdl_Replay(
                        "alt_day3_supper1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty,
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Ужин. Продолжение",
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
            "Ужин Френдзоны",
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
            "Дискотека. Начало",
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
            "Дискотека. Мейкап",
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
            "Первый танец",
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
            "Между танцами",
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
            "Второй танец",
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
            "Дискотека. Конец",
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
            "Концерт Алисы",
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
            "Алиса. Катапульта",
            sdl_Replay(
                        "alt_day3_dv_reunion", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d1_el_foll
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Алиса. Воссоединение",
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
            "Медпункт с Леной",
            sdl_Replay(
                        "alt_day3_med_un", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty,
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Лена. Карты на раздевание",
            sdl_Replay(
                        "alt_day3_un_cards", {"alt_replay_on" : "True"},
                        vars = [
                                    # переменные турнира
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Лена. После медпункта",
            sdl_Replay(
                        "alt_day3_post_strip", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_un_stri
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Дискотека Френдзоны",
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
            "Прогулка с Леной",
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
            "Сказка о Дороге",
            sdl_Replay("alt_day3_un_fz_evening_stories", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Танец с Леной",
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
            "Мику. Поездка в город",
            sdl_Replay(
                        "alt_day3_mi_7dl_init", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_mi_spt
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Великая Месть",
            sdl_Replay(
                        "alt_day3_mt_scare", {"alt_replay_on" : "True"},
                        music = music_7dl["genki"],
                        ambience = ambience_camp_center_evening,
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Техноквест",
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
            "Баня",
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
            "Отбой",
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
            "Отбой Френдзоны",
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

    ## Мику
    ### Мику-7дл
    #### 4 День
    sdl_repl_array_mi_7dl_day4 = [
        sdl_repl_Label(
            "Поездка",
            sdl_Replay(
                        "alt_day4_mi_7dl_ch1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_mi_7dl_dono
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Утро",
            sdl_Replay(
                        "alt_day4_mi_7dl_ch2", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_mi_7dl_dono
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Мику-донор",
            sdl_Replay("alt_day4_mi_7dl_ch3", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "В город!",
            sdl_Replay(
                        "alt_day4_mi_7dl_ch4", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_mi_7dl_dono
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Город. Квартира Ольги",
            sdl_Replay(
                        "alt_day4_mi_7dl_ch5a", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_dv_hous
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Город. Прогулка с Мику",
            sdl_Replay(
                        "alt_day4_mi_7dl_ch5b", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_mi_7dl_dono
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Город. Сакишита",
            sdl_Replay(
                        "alt_day4_mi_7dl_ch52", {"alt_replay_on" : "True"},
                        ambience = ambience_7dl["town_day"],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Домой",
            sdl_Replay(
                        "alt_day4_mi_7dl_ch6", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_mi_7dl_dono
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Вечер",
            sdl_Replay(
                        "alt_day4_mi_7dl_ch7", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_mi_7dl_dono
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "История Мику",
            sdl_Replay(
                        "alt_day4_mi_7dl_ch8b", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_mi_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Рандеву?",
            sdl_Replay(
                        "alt_day4_mi_7dl_ch8a", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Рандеву. Герк",
            sdl_Replay("alt_day4_mi_7dl_ch81", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Рандеву. Локи",
            sdl_Replay("alt_day4_mi_7dl_ch82", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Отбой",
            sdl_Replay("alt_day4_mi_7dl_ch83", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        )
    ]
    #### 5 День
    sdl_repl_array_mi_7dl_day5 = [
        sdl_repl_Label(
            "Дождь вместе",
            sdl_Replay("alt_day5_mi_7dl_rain_2gether", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Утро",
            sdl_Replay(
                        "alt_day5_mi_7dl_morning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_mi_7dl_dono
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Обед",
            sdl_Replay(
                        "alt_day5_mi_7dl_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_7dl_savi
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "День",
            sdl_Replay(
                        "alt_day5_mi_7dl_router", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_7dl_savi
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Баня",
            sdl_Replay("alt_day5_mi_7dl_lost", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Хентай",
            sdl_Replay("alt_day5_mi_7dl_hn", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Пирс",
            sdl_Replay("alt_day5_mi_7dl_branch", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "ДжентльСемён",
            sdl_Replay(
                        "alt_day5_mi_7dl_potato", {"alt_replay_on" : "True"},
                        meets = {'uv' : 'Кошкодевочка'},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Уборка костровой поляны",
            sdl_Replay("alt_day5_mi_7dl_camp_cleance", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Костёр",
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
            "Отбой",
            sdl_Replay(
                        "alt_day5_mi_7dl_goodnight", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_mi_7dl_voye
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 6 День
    sdl_repl_array_mi_7dl_day6 = [
        sdl_repl_Label(
            "Утро",
            sdl_Replay("alt_day6_mi_7dl_wakeup", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Soul. Капсулы времени",
            sdl_Replay(
                        "alt_day6_mi_7dl_soul", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Star. Культурный вечер",
            sdl_Replay("alt_day6_mi_7dl_star", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Human. Прогулка на лодке",
            sdl_Replay(
                        "alt_day6_mi_7dl_human", {"alt_replay_on" : "True"},
                        meets = {'bb' : 'Начальник лагеря'},
                        vars = [
                                    sdl_var_b_d2_mi_snap,
                                    sdl_var_e_d3_mi_7dl_dono
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Обед",
            sdl_Replay(
                        "alt_day6_mi_7dl_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_mi_7dl_voye
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Soul. Хентай",
            sdl_Replay(
                        "alt_day6_mi_7dl_soul_day", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_7dl_savi
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Star. Мини-концерт",
            sdl_Replay("alt_day6_mi_7dl_star_day", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Отъезд Мику",
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
            "Прощание с Мику",
            sdl_Replay(
                        "alt_day6_mi_7dl_miku_farewell_finale", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_mi_snap
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Soul. Прощание",
            sdl_Replay(
                        "alt_day6_mi_7dl_miku_farewell_soul", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_mi_date
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Star. Прощание",
            sdl_Replay(
                        "alt_day6_mi_7dl_miku_farewell_star", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_mi_snap
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Human. Мику остаётся",
            sdl_Replay(
                        "alt_day6_mi_7dl_human_day", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_mi_7dl_dono
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Катапульта",
            sdl_Replay("alt_day6_mi_7dl_catapult", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Дискотека",
            sdl_Replay(
                        "alt_day6_mi_7dl_discoteque", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_mi_7dl_left
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Хентай",
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
    #### 7 День
    sdl_repl_array_mi_7dl_day7 = [
        sdl_repl_Label(
            "Сон",
            sdl_Replay("alt_day7_mi_7dl_begin", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Утро",
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
            "Сборы",
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
            "Отъезд. Один",
            sdl_Replay("alt_day7_mi_7dl_departure_lone", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Отъезд. С Мику",
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
    ### Мику-Диджей
    #### 4 День
    sdl_repl_array_mi_djt_day4 = [
        sdl_repl_Label(
            "Ночь",
            sdl_Replay(
                        "alt_day4_mi_dj_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_conv
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Охота на хыщника",
            sdl_Replay(
                        "alt_day4_mi_dj_hedg_hunt", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_mi_kumu
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Утро",
            sdl_Replay(
                        "alt_day4_mi_dj_morning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_dj_hedg
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Начало дня",
            sdl_Replay(
                        "alt_day4_mi_dj_day", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Радиорубка",
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
            "Радиорубка. Уборка",
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
            "Обед",
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
            "Обед со Славей",
            sdl_Replay(
                        "alt_day4_mi_dj_dinner2", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_dj_sl_blac
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Репетиция",
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
            "Волейбол",
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
            "Ужин",
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
            "Вечер",
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
            "Ночное свидание",
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
            "Отбой",
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
    #### 5 День
    sdl_repl_array_mi_djt_day5 = [
        sdl_repl_Label(
            "Утро",
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
            "Завтрак",
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
            "Кино",
            sdl_Replay("alt_day5_mi_dj_cinema", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Обед",
            sdl_Replay("alt_day5_mi_dj_dinner", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Глушилка",
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
            "Вокалоидодрама",
            sdl_Replay("alt_day5_mi_dj_vocadrama", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Поиски. Музклуб",
            sdl_Replay(
                        "alt_day5_mi_dj_music_club1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d5_mi_dj_sear
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Поиски. Радиорубка",
            sdl_Replay("alt_day5_mi_dj_clubs1", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Поиски. Стоянка",
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
            "Поиски. Дом Мику",
            sdl_Replay(
                        "alt_day5_mi_dj_un_mi_house1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d5_mi_dj_sear
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Поиски. Эстрада",
            sdl_Replay("alt_day5_mi_dj_estrade1", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Ужин",
            sdl_Replay("alt_day5_mi_dj_supper", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Костёр",
            sdl_Replay(
                        "alt_day5_mi_dj_campfire", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_dj_hedg
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Душевые. Мику",
            sdl_Replay("alt_day5_mi_dj_voyeur_4", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Душевые. Алиса",
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
            "Душевые. Славя",
            sdl_Replay("alt_day5_mi_dj_voyeur_3", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Разговор",
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
            "Примирение",
            sdl_Replay(
                        "alt_day5_mi_dj_evening_club1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_mi_dj_dv_blad
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "«Просмотр кино»",
            sdl_Replay("alt_day5_mi_dj_evening_club2", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Хентай",
            sdl_Replay(
                        "alt_day5_mi_dj_hentai", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_me_dan2
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Отбой",
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
    #### 6 День
    sdl_repl_array_mi_djt_day6 = [
        sdl_repl_Label(
            "Утро. Вместе",
            sdl_Replay(
                        "alt_day6_mi_dj_good", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d5_mi_dj_voye
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Утро. Один",
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
            "Завтрак",
            sdl_Replay(
                        "alt_day6_mi_dj_neutral_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d5_mi_dj_apol
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "В эфире!",
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
            "Обед",
            sdl_Replay("alt_day6_mi_dj_dinner", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Свидание",
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
            "Прощение",
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
            "Рассказ Мику",
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
            "Тихий час",
            sdl_Replay(
                        "alt_day6_mi_dj_plain", {"alt_replay_on" : "True"},
                        music = music_list["everyday_theme"],
                        ambience = ambience_dining_hall_full,
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Концерт",
            sdl_Replay(
                        "alt_day6_mi_dj_concert", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d5_mi_dj_voye
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Колонки. Таскаем",
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
            "Колонки. Отлыниваем",
            sdl_Replay("alt_day6_mi_dj_reject", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Стенгазета",
            sdl_Replay("alt_day6_mi_dj_newswall", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Ужин",
            sdl_Replay("alt_day6_mi_dj_supper", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Поздний ужин у Слави",
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
            "Поздний ужин у Лены",
            sdl_Replay(
                        "alt_day6_mi_dj_late_supper_un", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_mi_dj_hent
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Дискотека",
            sdl_Replay(
                        "alt_day6_mi_dj_discotheque", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_mi_dj_walk
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Первый танец",
            sdl_Replay(
                        "alt_day6_mi_dj_first_dance", {"alt_replay_on" : "True"},
                        music = music_list["waltz_of_doubts"],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Второй танец",
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
            "Второй танец. Успех",
            sdl_Replay("alt_day6_mi_dj_dance2_success", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Второй танец. Неудача",
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
            "Побег с танцев",
            sdl_Replay(
                        "alt_day6_mi_dj_escape", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Катапульта",
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
            "Хентай",
            sdl_Replay(
                        "alt_day6_mi_dj_hentai", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Отбой",
            sdl_Replay(
                        "alt_day6_mi_dj_sleeptime", {"alt_replay_on" : "True"},
                        music = music_list["a_promise_from_distant_days"],
                        ambience = ambience_camp_center_night,
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 7 День
    sdl_repl_array_mi_djt_day7 = [
        sdl_repl_Label(
            "Утро. Вместе",
            sdl_Replay(
                        "alt_day7_mi_dj_together", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_mi_dj_hent
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Утро. Один",
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
            "Токсикоз",
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
            "Завтрак",
            sdl_Replay("alt_day7_mi_dj_breakfast", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Сборы",
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
            "Отъезд",
            sdl_Replay(
                        "alt_day7_mi_dj_departure", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_mi_dj_cata
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Мёрзну без тебя",
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
            "Мир сошёл с ума",
            sdl_Replay("alt_day7_mi_dj_good", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load)
        )
    ]

    ## Алиса
    ### Алиса-7дл
    #### 4 День
    sdl_repl_array_dv_7dl_day4 = [
        sdl_repl_Label(
            "Утро",
            sdl_Replay(
                        "alt_day4_dv_7dl_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Поход",
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
            "Обед",
            sdl_Replay("alt_day4_dv_7dl_dinner", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Тихий час",
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
            "Репетиция",
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
            "Полдник",
            sdl_Replay(
                        "alt_day4_dv_7dl_lunch", {"alt_replay_on" : "True"},
                        music = music_list["so_good_to_be_careless"],
                        ambience = ambience_camp_center_day,
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Просьба Виолы",
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
            "Поездка",
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
            "Портвейн",
            sdl_Replay(
                        "alt_day4_dv_7dl_alco", {"alt_replay_on" : "True"},
                        music = music_list["into_the_unknown"],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Обратный путь",
            sdl_Replay("alt_day4_dv_7dl_back_to_camp", {"alt_replay_on" : "True"})
        ),
        sdl_repl_Label(
            "Лекарства",
            sdl_Replay(
                        "alt_day4_dv_7dl_append", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Лекарства. Дом Ольги",
            sdl_Replay("alt_day4_dv_7dl_mt_aid", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Лекарства. Медпункт",
            sdl_Replay("alt_day4_dv_7dl_aidpost", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Хентай",
            sdl_Replay("alt_day4_dv_7dl_hentai", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Ужин",
            sdl_Replay(
                        "alt_day4_dv_7dl_supper", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_dv_7dl_medi
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Отбой",
            sdl_Replay(
                        "alt_day4_dv_7dl_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_dv_7dl_medi
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 5 День
    sdl_repl_array_dv_7dl_day5 = [
        sdl_repl_Label(
            "Похмелье",
            sdl_Replay(
                        "alt_day5_dv_7dl_alco_morning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_dv_7dl_hent
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Утро",
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
            "Возвращение",
            sdl_Replay("alt_day5_dv_7dl_roadtrip", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Свечка",
            sdl_Replay(
                        "alt_day5_dv_7dl_candle", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_dv_7dl_cs_help
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Обед",
            sdl_Replay(
                        "alt_day5_dv_7dl_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_dv_7dl_vodk
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Тихий час",
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
            "Полдник",
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
            "Репетиция",
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
            "Ужин",
            sdl_Replay("alt_day5_dv_7dl_supper", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Вечер",
            sdl_Replay("alt_day5_dv_7dl_evening", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Костёр",
            sdl_Replay(
                        "alt_day5_dv_7dl_campfire", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_dv_7dl_cs_help
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Ночное свидание",
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
            "Отбой",
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
    #### 6 День
    sdl_repl_array_dv_7dl_day6 = [
        sdl_repl_Label(
            "Утро",
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
            "Поручение Виолы",
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
            "Завтрак",
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
            "Репетиция",
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
            "Обед",
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
            "Славя",
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
            "Славя. Согласился помочь",
            sdl_Replay(
                        "alt_day6_dv_7dl_sl_help", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_dv_7dl_hent
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Славя. Помогаем",
            sdl_Replay("alt_day6_dv_7dl_sl_help2", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Славя. Каморка",
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
            "Лена",
            sdl_Replay("alt_day6_dv_7dl_un", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Лена. Встреча",
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
            "Концерт",
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
            "Ужин",
            sdl_Replay(
                        "alt_day6_dv_7dl_supper", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_dv_7dl_tran
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Дискотека",
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
            "Танец с Алисой",
            sdl_Replay("alt_day6_dv_7dl_dv_dancing", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Хентай",
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
            "Облом",
            sdl_Replay(
                        "alt_day6_dv_7dl_non_love", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_dv_7dl_hent
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Катапульта",
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
            "Возвращаемся на танцы",
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
            "Танец со Славей",
            sdl_Replay(
                        "alt_day6_dv_7dl_sl_dancing", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_brf
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Танец с Леной",
            sdl_Replay("alt_day6_dv_7dl_un_dancing", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Танец с Ольгой",
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
            "Отбой",
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
    #### 7 День
    sdl_repl_array_dv_7dl_day7 = [
        sdl_repl_Label(
            "Сон",
            sdl_Replay("alt_day7_dv_7dl_begin", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Утро",
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
            "Сборы с Алисой",
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
            "Сборы со Славей",
            sdl_Replay("alt_day7_dv_7dl_sl", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Сборы с Леной",
            sdl_Replay("alt_day7_dv_7dl_un", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Сборы с Ольгой",
            sdl_Replay("alt_day7_dv_7dl_mt", {"alt_replay_on" : "True"}),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Катапульта Локи",
            sdl_Replay(
                        "alt_day7_dv_7dl_loki", {"alt_replay_on" : "True"},
                        music = music_list["farewell_to_the_past_edit"],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Отъезд",
            sdl_Replay(
                        "alt_day7_dv_7dl_bus", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d7_dv_7dl_chec
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    ### Алиса-Диджей
    #### 4 День
    sdl_repl_array_dv_djt_day4 = [
        sdl_repl_Label(
            "Утро",
            sdl_Replay(
                        "alt_day4_dv_dj_morning", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Завтрак",
            sdl_Replay(
                        "alt_day4_dv_dj_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d1_un_talk
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Освобождение рыжей!",
            sdl_Replay(
                        "alt_day4_dv_dj_alise_free", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Рыжий ураган",
            sdl_Replay(
                        "alt_day4_dv_dj_radio_event", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Обед",
            sdl_Replay(
                        "alt_day4_dv_dj_lunch", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Тихий час",
            sdl_Replay(
                        "alt_day4_dv_dj_silent_hour", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Полдник",
            sdl_Replay(
                        "alt_day4_dv_dj_afternoon", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Концерт",
            sdl_Replay(
                        "alt_day4_dv_dj_concert", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Ужин",
            sdl_Replay(
                        "alt_day4_dv_dj_dinner", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Поиски Ульяны",
            sdl_Replay(
                        "alt_day4_dv_dj_us_search", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Свидание на пляже",
            sdl_Replay(
                        "alt_day4_dv_dj_date_on_the_beach", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Отбой",
            sdl_Replay(
                        "alt_day4_dv_dj_sleeptime", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 5 День
    sdl_repl_array_dv_djt_day5 = [
        sdl_repl_Label(
            "Утро",
            sdl_Replay(
                        "alt_day5_dv_dj_morning", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Завтрак",
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
            "Обед",
            sdl_Replay(
                        "alt_day5_dv_dj_lunch", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Карта (идём к Дваче)",
            sdl_Replay(
                        "alt_day5_dv_dj_map_house_dv1", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Карта (идём на площадь)",
            sdl_Replay(
                        "alt_day5_dv_dj_map_square1", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Карта (идём в библ-ку)",
            sdl_Replay(
                        "alt_day5_dv_dj_map_library1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_voya
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Карта (идём к Мику)",
            sdl_Replay(
                        "alt_day5_dv_dj_map_musclub1", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Карта (идём к киб-кам)",
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
            "Полдник",
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
            "Радиоэфир",
            sdl_Replay(
                        "alt_day5_dv_dj_radio_broadcast", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Ужин",
            sdl_Replay(
                        "alt_day5_dv_dj_dinner", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Костёр",
            sdl_Replay(
                        "alt_day5_dv_dj_campfire", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_dv_lpp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Отбой",
            sdl_Replay(
                        "alt_day5_dv_dj_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d5_dv_dj_mapp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 6 День
    sdl_repl_array_dv_djt_day6 = [
        sdl_repl_Label(
            "Пробуждение",
            sdl_Replay(
                        "alt_day6_dv_dj_morning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_dv_lpp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Завтрак",
            sdl_Replay(
                        "alt_day6_dv_dj_breakfast", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Радиоэфир",
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
            "Обед",
            sdl_Replay(
                        "alt_day6_dv_dj_lunch", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Тихий час",
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
            "Концерт",
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
            "Ужин",
            sdl_Replay(
                        "alt_day6_dv_dj_dinner", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Вечер",
            sdl_Replay(
                        "alt_day6_dv_dj_no_dance", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_dv_dj_ends
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Разговор по душам",
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
            "Отбой (вариант 1)",
            sdl_Replay(
                        "alt_day6_dv_dj_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_dv_dj_ends
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Отбой (вариант 2)",
            sdl_Replay(
                        "alt_day6_dv_dj_sleeptime2", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_dv_dj_ends
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 7 День
    sdl_repl_array_dv_djt_day7 = [
        sdl_repl_Label(
            "Сон",
            sdl_Replay(
                        "alt_day7_dv_dj_dream", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_dv_dj_ends
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Утро",
            sdl_Replay(
                        "alt_day7_dv_dj_morning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_dv_dj_ends
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Точки над Ё",
            sdl_Replay(
                        "alt_day7_dv_dj_points", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_dv_dj_ends
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Отбытие",
            sdl_Replay(
                        "alt_day7_dv_dj_departure", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_dv_dj_ends
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        )    ]

    ## Славя
    ### Славя-7дл
    #### 4 День
    sdl_repl_array_sl_7dl_day4 = [
        sdl_repl_Label(
            "Утро",
            sdl_Replay("alt_day4_sl_7dl_begin", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Завтрак",
            sdl_Replay(
                        "alt_day4_sl_7dl_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_7dl_work
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Утро. Локи",
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
            "Утро. Герк",
            sdl_Replay("alt_day4_sl_7dl_herc_morning", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Утро. Дрищ",
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
            "День. Локи",
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
            "День. Герк",
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
            "День. Дрищ",
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
            "Вечер. Локи",
            sdl_Replay(
                        "alt_day4_sl_7dl_loki_evening", {"alt_replay_on" : "True"},
                        meets = {'al' : 'Сердитый мальчик'},
                        vars = [
                                    sdl_var_l_d2_club
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Вечер. Герк",
            sdl_Replay(
                        "alt_day4_sl_7dl_herc_evening", {"alt_replay_on" : "True"},
                        meets = {'al' : 'Сердитый мальчик', 'dn' : 'Кудрявый'},
                        vars = [
                                    sdl_var_b_d4_sl_7dl_appl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Вечер. Дрищ",
            sdl_Replay("alt_day4_sl_7dl_evening", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Вечер",
            sdl_Replay(
                        "alt_day4_sl_7dl_sundown", {"alt_replay_on" : "True"},
                        meets = {'dn' : 'Кудрявый', 'tn' : 'Странный мальчик'},
                        vars = [
                                    sdl_var_b_d4_sl_7dl_rend,
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Отбой",
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
    #### 5 День
    sdl_repl_array_sl_7dl_day5 = [
        sdl_repl_Label(
            "Утро",
            sdl_Replay(
                        "alt_day5_sl_7dl_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_7dl_work
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Завтрак",
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
            "Свечка",
            sdl_Replay(
                        "alt_day5_sl_7dl_candle", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_7dl_work
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Свечка. Локи",
            sdl_Replay(
                        "alt_day5_sl_7dl_candle_loki", {"alt_replay_on" : "True"},
                        music = music_7dl["deep_inside"],
                        ambience = ambience_7dl["rain"],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Свечка. Герк",
            sdl_Replay(
                        "alt_day5_sl_7dl_candle_herc", {"alt_replay_on" : "True"},
                        music = music_7dl["deep_inside"],
                        ambience = ambience_7dl["rain"],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Свечка. Дрищ",
            sdl_Replay(
                        "alt_day5_sl_7dl_candle_dr", {"alt_replay_on" : "True"},
                        music = music_7dl["deep_inside"],
                        ambience = ambience_7dl["rain"],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "День. Локи",
            sdl_Replay("alt_day5_sl_7dl_loki_day", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "День. Герк",
            sdl_Replay(
                        "alt_day5_sl_7dl_herc_day", {"alt_replay_on" : "True"},
                        meets = {'ka' : 'Вожатая 2 отряда'},
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
            "День. Дрищ",
            sdl_Replay(
                        "alt_day5_sl_7dl_day", {"alt_replay_on" : "True"},
                        meets = {'al' : 'Сердитый мальчик', 'dn' : 'Кудрявый', 'tn' : 'Странный мальчик'},
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Вечер. Локи",
            sdl_Replay("alt_day5_sl_7dl_loki_evening", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Вечер. Герк",
            sdl_Replay("alt_day5_sl_7dl_herc_evening", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Вечер. Дрищ",
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
            "Костёр",
            sdl_Replay(
                        "alt_day5_sl_7dl_campfire", {"alt_replay_on" : "True"},
                        meets = {'tn' : 'Странный мальчик'},
                        vars = [
                                    sdl_var_b_d4_sl_7dl_rend,
                                    sdl_var_b_d5_sl_7dl_work,
                                    sdl_var_i_sl_lpp
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Хентай",
            sdl_Replay("alt_day5_sl_7dl_hentai", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Отбой",
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
            "Ночное свидание",
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
    #### 6 День
    sdl_repl_array_sl_7dl_day6 = [
        sdl_repl_Label(
            "Озеро",
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
            "Месть Ульянке",
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
            "Утро",
            sdl_Replay(
                        "alt_day6_sl_7dl_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_7dl_sick
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Пробежка",
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
            "Завтрак",
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
            "Утро. Локи",
            sdl_Replay("alt_day6_sl_7dl_loki_morning", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Утро. Герк. Здоров",
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
            "Утро. Герк. Болен",
            sdl_Replay(
                        "alt_day6_sl_7dl_herc_morning_sick", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Утро. Дрищ. Славя",
            sdl_Replay("alt_day6_sl_7dl_dr_morning_normal", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Утро. Дрищ. Дорога",
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
            "День. Локи",
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
            "День. Герк. Электроник",
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
            "День. Герк. На крыше",
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
            "День. Дрищ. Славя",
            sdl_Replay(
                        "alt_day6_sl_7dl_dr_day_normal", {"alt_replay_on" : "True"},
                        meets = {'ka' : 'Вожатая 2 отряда'},
                        func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 1
        ),
        sdl_repl_Label(
            "День. Дрищ. Дорога",
            sdl_Replay(
                        "alt_day6_sl_7dl_dr_day_olroad", {"alt_replay_on" : "True"},
                        meets = {'uv' : 'Кошкодевочка'},
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Вечер. Локи",
            sdl_Replay("alt_day6_sl_7dl_loki_evening", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Вечер. Герк. Славя",
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
            "Вечер. Герк. Концерт",
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
            "Вечер. Дрищ. Славя",
            sdl_Replay("alt_day6_sl_7dl_dr_evening_normal", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Вечер. Дрищ. Дорога",
            sdl_Replay(
                        "alt_day6_sl_7dl_dr_evening_olroad", {"alt_replay_on" : "True"},
                        meets = {'uv' : 'Кошкодевочка'},
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Ужин",
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
            "Катапульта",
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
            "Похороны Пирата",
            sdl_Replay("alt_day6_sl_7dl_dr_funeral", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Лес Памяти",
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
            "Дискотека. Герк",
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
            "Дискотека. Дрищ. Славя",
            sdl_Replay("alt_day6_sl_7dl_dr_disco_normal", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Дискотека. Дрищ. Дорога",
            sdl_Replay(
                        "alt_day6_sl_7dl_dr_disco_olroad", {"alt_replay_on" : "True"},
                        music = music_7dl["unforgotten"],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Хентай. Локи",
            sdl_Replay("alt_day6_sl_7dl_loki_hentai", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Хентай. Герк",
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
            "Хентай. Дрищ",
            sdl_Replay("alt_day6_sl_7dl_dr_hentai_normal", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Хентай. Дрищ 2",
            sdl_Replay("alt_day6_sl_7dl_dr_hentai_olroad", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Отбой",
            sdl_Replay(
                        "alt_day6_sl_7dl_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_sl_7dl_hent
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 7 День
    sdl_repl_array_sl_7dl_day7 = [
        sdl_repl_Label(
            "Утро",
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
            "Утро. Локи",
            sdl_Replay("alt_day7_sl_7dl_begin_loki", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Утро. Герк",
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
            "Сборы. Локи. Прощение",
            sdl_Replay("alt_day7_sl_7dl_packing_loki_forgive", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Сборы. Локи. Сволочь",
            sdl_Replay("alt_day7_sl_7dl_packing_loki_asshole", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Сборы. Герк",
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
            "Сборы. Дрищ",
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
            "Отъезд",
            sdl_Replay(
                        "alt_day7_sl_7dl_leaving", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_7dl_olro,
                                    sdl_var_b_d6_sl_7dl_forg,
                                    sdl_var_i_sl_lpp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Эпилог. Локи",
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
            "Эпилог. Локи. Сволочь",
            sdl_Replay("alt_day7_sl_7dl_loki_rewind", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        # sdl_repl_Label(
            # "Эпилог. Герк",
            # sdl_Replay("alt_day7_sl_7dl_herc", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            # char_mask = 2
        # ),
        sdl_repl_Label(
            "Эпилог. Дрищ",
            sdl_Replay("alt_day7_sl_7dl_epi", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            char_mask = 1
        )
    ]
    ### Славя-Классик
    #### 4 День
    sdl_repl_array_sl_clt_day4 = [
        sdl_repl_Label(
            "Утро",
            sdl_Replay(
                        "alt_day4_sl_cl_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_walk
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Гуделка",
            sdl_Replay("alt_day4_sl_cl_shurik", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Техносон",
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
            "Ужин",
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
            "Сборы",
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
            "Поиски",
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
            "Старый лагерь",
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
            "Катакомбы",
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
            "Ведьма",
            sdl_Replay(
                        "alt_day4_sl_wh_night", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Отбой",
            sdl_Replay(
                        "alt_day4_sl_cl_cs_night", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 5 День
    sdl_repl_array_sl_clt_day5 = [
        sdl_repl_Label(
            "Утро",
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
            "Начальник лагеря",
            sdl_Replay(
                        "alt_day5_sl_cl_chief", {"alt_replay_on" : "True"},
                        meets = {'bb' : 'Начальник лагеря'},
                        ambience = ambience_7dl["rain"],
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Ольга",
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
            "Завтрак",
            sdl_Replay(
                        "alt_day5_sl_cl_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_b_d5_sl_cl_cs
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Разговор с Санычем",
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
            "Катакомбы",
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
            "Туман",
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
            "Возвращение",
            sdl_Replay(
                        "alt_day5_sl_cl_return", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Лекция Виолы",
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
            "Подготовка костра",
            sdl_Replay(
                        "alt_day5_sl_cl_campfire_prepare", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_me_dan1
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Купание",
            sdl_Replay("alt_day5_sl_cl_bathing", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Ужин",
            sdl_Replay(
                        "alt_day5_sl_cl_supper", {"alt_replay_on" : "True"},
                        meets = {'dn' : 'Кудрявый'},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Костёр",
            sdl_Replay(
                        "alt_day5_sl_cl_campfire", {"alt_replay_on" : "True"},
                        ambience = ambience_forest_evening,
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Транспортировка раненого",
            sdl_Replay(
                        "alt_day5_sl_cl_dn_aid", {"alt_replay_on" : "True"},
                        meets = {'dn' : 'Кудрявый'},
                        ambience = ambience_forest_evening,
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Презент Виолы",
            sdl_Replay(
                        "alt_day5_sl_cl_cs_reward", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Ночное свидание",
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
            "Хентай",
            sdl_Replay("alt_day5_sl_cl_hentai", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Отбой",
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
    #### 6 День
    sdl_repl_array_sl_clt_day6 = [
        sdl_repl_Label(
            "Сон. Выбор",
            sdl_Replay(
                        "alt_day6_sl_cl_begin_yulya", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_sp
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Утро. Пещера",
            sdl_Replay(
                        "alt_day6_sl_cl_begin_cave", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Утро. Вместе",
            sdl_Replay(
                        "alt_day6_sl_cl_begin_good", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Утро. Техносон",
            sdl_Replay(
                        "alt_day6_sl_cl_begin_techno", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Проблемы Шурика",
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
            "Завтрак",
            sdl_Replay("alt_day6_sl_cl_breakfast", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Поручение Саныча",
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
            "Начальство Саныча",
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
            "Обед",
            sdl_Replay(
                        "alt_day6_sl_cl_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti,
                                    sdl_var_b_d5_sl_cl_hent,
                                    sdl_var_b_d6_sl_cl_agre,
                                    sdl_var_i_sl_sp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Усилитель",
            sdl_Replay(
                        "alt_day6_sl_cl_amp_list", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_sl_cl_shir
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Глушилка",
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
            "Обморок Слави",
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
            "Анатолий Иванович",
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
            "Пират",
            sdl_Replay(
                        "alt_day6_sl_cl_pirate", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_sl_cl_hent,
                                    sdl_var_b_d6_sl_cl_agre,
                                    sdl_var_i_sl_lpp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Мир Вторых Шансов",
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
            "Помощь Саныча",
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
            "Концерт. Пират",
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
            "Концерт. Шурик",
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
            "Вечер. Медпункт",
            sdl_Replay(
                        "alt_day6_sl_cl_algorithm", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_sl_cl_hent
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Колонки",
            sdl_Replay("alt_day6_sl_cl_sonic", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Ужин",
            sdl_Replay(
                        "alt_day6_sl_cl_supper", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Дискотека",
            sdl_Replay(
                        "alt_day6_sl_cl_dance", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Танец",
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
            "История Шурика",
            sdl_Replay(
                        "alt_day6_sl_cl_sh_story", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_entrance_night,
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Виола",
            sdl_Replay(
                        "alt_day6_sl_cl_sh_tug", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_sl_cl_tuti
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Дебаркадер",
            sdl_Replay(
                        "alt_day6_sl_cl_debarkader", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 7 День
    sdl_repl_array_sl_clt_day7 = [
        sdl_repl_Label(
            "Техносон",
            sdl_Replay("alt_day7_sl_cl_techno", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Утро. Изолятор",
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
            "Утро. Дебаркадер",
            sdl_Replay("alt_day7_sl_cl_begin_pi", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Инцидент",
            sdl_Replay(
                        "alt_day7_sl_cl_incident", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_sl_cl_arc
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Завтрак",
            sdl_Replay(
                        "alt_day7_sl_cl_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_sl_cl_arc
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Обход. Админ. корпус",
            sdl_Replay("alt_day7_sl_cl_admins1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Обход. Клубы",
            sdl_Replay(
                        "alt_day7_sl_cl_clubs1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_sl_cl_arc
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Обход. Столовая",
            sdl_Replay("alt_day7_sl_cl_dining_hall1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Обход. Спортплощадка",
            sdl_Replay(
                        "alt_day7_sl_cl_sport_area1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_voya
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Обход. Воллейбол. площадка",
            sdl_Replay(
                        "alt_day7_sl_cl_volleyball_alt2", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_club
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Обход. Эстрада",
            sdl_Replay("alt_day7_sl_cl_estrade1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Обход. Пристань",
            sdl_Replay(
                        "alt_day7_sl_cl_boat_station1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Обход. Пляж",
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
            "Фото на память",
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
            "Обед",
            sdl_Replay(
                        "alt_day7_sl_cl_dinner", {"alt_replay_on" : "True"},
                        meets = {'bb' : 'Начальник лагеря'},
                        vars = [
                                    sdl_var_i_sl_lpp,
                                    sdl_var_i_sl_sp,
                                    sdl_var_e_d6_sl_cl_arc
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Отъезд. Успел",
            sdl_Replay("alt_day7_sl_cl_departure_a2th", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Отъезд. Опоздал",
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
    #### ??? День
    sdl_repl_array_sl_clt_dayx = [
        sdl_repl_Label(
            "Спасательная операция",
            sdl_Replay(
                        "alt_day7_sl_cl_loop", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_sl_cl_solo
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Порридж",
            sdl_Replay(
                        "alt_day7_sl_cl_porridge", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_sl_lpp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load)
        )
    ]

    ## Лена
    ### Лена-7дл
    #### 4 День
    sdl_repl_array_un_7dl_day4 = [
        sdl_repl_Label(
            "Утро",
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
            "Линейка",
            sdl_Replay("alt_day4_un_7dl_lineup", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Завтрак",
            sdl_Replay(
                        "alt_day4_un_7dl_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_un_7dl_sear
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Стоянка",
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
            "Запись",
            sdl_Replay(
                        "alt_day4_un_7dl_declaration", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_un_7dl_sear
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Примирение с Женей",
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
            "Обед",
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
            "День. Локи",
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
            "Хентай",
            sdl_Replay("alt_day4_un_7dl_hentai", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "День. Герк",
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
            "День. Дрищ. Газета",
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
            "День. Дрищ. Бадминтон",
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
            "Полдник",
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
            "Концерт",
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
            "Взрывчатка",
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
            "Ужин",
            sdl_Replay(
                        "alt_day4_un_7dl_supper", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_un_7dl_expl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Вечер",
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
            "Вечер. Дрищ",
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
            "Пристань",
            sdl_Replay("alt_day4_un_7dl_dock", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Отбой",
            sdl_Replay("alt_day4_un_7dl_sleeptime", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        )
    ]
    #### 5 День
    sdl_repl_array_un_7dl_day5 = [
        sdl_repl_Label(
            "Утро",
            sdl_Replay(
                        "alt_day5_un_7dl_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_me_neu_tran
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Завтрак",
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
            "Утро. Локи",
            sdl_Replay("alt_day5_un_7dl_breakfast_l", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Утро. Герк",
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
            "Утро. Дрищ",
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
            "Клубы",
            sdl_Replay("alt_day5_un_7dl_clubs", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 4
        ),
        sdl_repl_Label(
            "«Лиловый шар»",
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
            "Уборка площади",
            sdl_Replay("alt_day5_un_7dl_cleaning", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Обед",
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
            "Пляж",
            sdl_Replay(
                        "alt_day5_un_7dl_np", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_me_neu_tran
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Статья",
            sdl_Replay("alt_day5_un_7dl_article", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Алёна",
            sdl_Replay("alt_day5_un_7dl_unl", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Полдник",
            sdl_Replay(
                        "alt_day5_un_7dl_launch", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Библиотека",
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
            "Уборка костровой поляны",
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
            "Ужин",
            sdl_Replay(
                        "alt_day5_un_7dl_supper", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d5_un_7dl_wash
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Костёр",
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
            "Лёгкая ссора",
            sdl_Replay(
                        "alt_day5_un_7dl_evening_un", {"alt_replay_on" : "True"},
                        sound_loop = sfx_forest_fireplace,
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Серьёзная ссора",
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
            "Побег с костра",
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
            "Хентай в клубах",
            sdl_Replay(
                        "alt_day5_un_7dl_video", {"alt_replay_on" : "True"},
                        sound_loop = sfx_forest_fireplace,
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Хентай в лодке",
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
            "Отбой",
            sdl_Replay(
                        "alt_day5_un_7dl_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 6 День
    sdl_repl_array_un_7dl_day6 = [
        sdl_repl_Label(
            "Утро",
            sdl_Replay("alt_day6_un_7dl_begin", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Поиски. Библиотека",
            sdl_Replay(
                        "alt_day6_un_7dl_search", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_me_neu_tran
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Обед",
            sdl_Replay("alt_day6_un_7dl_dinner", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Поиски. Карьер",
            sdl_Replay("alt_day6_un_7dl_career", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Поиски. Музклуб",
            sdl_Replay(
                        "alt_day6_un_7dl_music_club", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Концерт",
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
            "Ужин",
            sdl_Replay("alt_day6_un_7dl_supper", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Катапульта",
            sdl_Replay(
                        "alt_day6_un_7dl_catapult", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_karma
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Дискотека",
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
            "Отбой",
            sdl_Replay("alt_day6_un_7dl_sleeptime", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        )
    ]
    #### 7 День
    sdl_repl_array_un_7dl_day7 = [
        sdl_repl_Label(
            "Сон",
            sdl_Replay("alt_day7_un_7dl_begin", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "День",
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
            "Обед",
            sdl_Replay("alt_day7_un_7dl_dinner", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Истерика",
            sdl_Replay(
                        "alt_day7_un_7dl_hysterics", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_me_neu_tran
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Таблетки",
            sdl_Replay("alt_day7_un_7dl_pills", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Чудо",
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
            "Откат",
            sdl_Replay("alt_day7_un_7dl_rollback", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Отъезд",
            sdl_Replay(
                        "alt_day7_un_7dl_departure", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_karma
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    ### Лена-Френдзона
    #### 4 День
    sdl_repl_array_un_fzd_day4 = [
        sdl_repl_Label(
            "Сон. Лена",
            sdl_Replay("alt_day4_un_fz_dream_un", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Сон. Дорога",
            sdl_Replay("alt_day4_un_fz_dream_road", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Утро",
            sdl_Replay("alt_day4_un_fz_morning", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Медпункт",
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
            "Стенгазета",
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
            "Помощник вожатой",
            sdl_Replay("alt_day4_un_fz_mt_help", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Побег с Алисой",
            sdl_Replay("alt_day4_un_fz_dv_escape", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Заблудший",
            sdl_Replay("alt_day4_un_fz_old_road", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Обед. После стенгазеты",
            sdl_Replay("alt_day4_un_fz_lunch_nwsppr", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Обед. После лодок",
            sdl_Replay("alt_day4_un_fz_lunch_boat", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Обед. После леса",
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
            "Тихий час",
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
            "Полдник",
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
            "Песчаная коса",
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
            "Ужин",
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
            "Погоня",
            sdl_Replay(
                        "alt_day4_un_fz_run", {"alt_replay_on" : "True"},
                        meets = {'al' : 'Сердитый мальчик'},
                        vars = [
                                    sdl_var_b_d3_un_fz_stories,
                                    sdl_var_i_un_fzd_dv
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Разборки",
            sdl_Replay(
                        "alt_day4_un_fz_debriefing", {"alt_replay_on" : "True"},
                        meets = {'dn' : 'Кудрявый'},
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
            "Вечер",
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
            "Вечер. Дом Семёна и Ольги",
            sdl_Replay("alt_day4_un_fz_mt_house", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Вечер. Портвейн",
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
            "«Чаепитие»",
            sdl_Replay(
                        "alt_day4_un_fz_tea_party", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_un_fz_morn
                                    # переменные турнира
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "После вечеринки",
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
            "Отбой",
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
    #### 5 День
    sdl_repl_array_un_fzd_day5 = [
        sdl_repl_Label(
            "Сон",
            sdl_Replay("alt_day5_un_fz_dream", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Утро",
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
            "Завтрак",
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
            "Свечка",
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
            "Сон. Алиса",
            sdl_Replay("alt_day5_un_fz_dream2_dv", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Сон. Лена",
            sdl_Replay("alt_day5_un_fz_dream2_un", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Сон. Дорога",
            sdl_Replay("alt_day5_un_fz_dream2_road", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Обед",
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
            "Золушка",
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
            "Полдник",
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
            "Костровая поляна",
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
            "Старый лагерь",
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
            "Ужин",
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
            "Поручение Ольги",
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
            "Вечер",
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
            "Костёр",
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
            "Поиски",
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
            "Огонёк. ФЗ",
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
            "Огонёк. Дорога",
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
            "Отбой. ФЗ",
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
            "Отбой. Дорога",
            sdl_Replay("alt_day5_un_fz_rr_sleeptime", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 2
        )
    ]
    #### 6 День. Дорога
    sdl_repl_array_un_fzd_day6 = [
        sdl_repl_Label(
            "Сон",
            sdl_Replay("alt_day6_un_fz_rr_dream", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Утро",
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
            "Линейка",
            sdl_Replay("alt_day6_un_fz_rr_lineup", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Завтрак",
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
            "Поиски",
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
            "Поиски. Домик на дереве",
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
            "Поиски. Старый лагерь",
            sdl_Replay(
                        "alt_day6_un_fz_rr_search2", {"alt_replay_on" : "True"},
                        meets = {'tn' : 'Странный мальчик'},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Обед",
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
            "Спасение Гвардии",
            sdl_Replay("alt_day6_un_fz_rr_guard_resque", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Старая Дорога",
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
            "Иной мир",
            sdl_Replay("alt_day6_un_fz_rr_another_world", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Прощание",
            sdl_Replay("alt_day6_un_fz_rr_farewell", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 2
        )
    ]
    #### 6 День. ФЗ
    sdl_repl_array_un_fzd_day62 = [
        sdl_repl_Label(
            "Пробуждение",
            sdl_Replay(
                        "alt_day6_un_fz_morning", {"alt_replay_on" : "True"},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Линейка",
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
            "Завтрак",
            sdl_Replay(
                        "alt_day6_un_fz_breakfast", {"alt_replay_on" : "True"},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Карта. Лодочная станция",
            sdl_Replay(
                        "alt_day6_un_fz_map_boatstation1", {"alt_replay_on" : "True"},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Карта. Спортплощадка",
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
            "Карта. Музклуб",
            sdl_Replay(
                        "alt_day6_un_fz_map_musclub1", {"alt_replay_on" : "True"},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Карта. Домик Алисы",
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
            "Карта. Пляж",
            sdl_Replay(
                        "alt_day6_un_fz_map_beach2", {"alt_replay_on" : "True"},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Карта. Столовая",
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
            "Карта. Автоб. остановка",
            sdl_Replay(
                        "alt_day6_un_fz_map_busstation2", {"alt_replay_on" : "True"},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Обед",
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
            "Помощь Славе",
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
            "Полдник",
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
            "Концерт",
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
            "Ужин с Алисой",
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
            "Вечер с Алисой",
            sdl_Replay(
                        "alt_day6_un_fz_dv_date", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Поиски Лены",
            sdl_Replay(
                        "alt_day6_un_fz_dv_un_search", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Кошмар наяву",
            sdl_Replay(
                        "alt_day6_un_fz_dv_un_night", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Ужин с Леной",
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
            "Точки над «Ё»",
            sdl_Replay(
                        "alt_day6_un_fz_good_un_evening", {"alt_replay_on" : "True"},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Танцы в одиночестве",
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
            "Разговор с Ольгой",
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
            "Танцы с Леной",
            sdl_Replay(
                        "alt_day6_un_fz_dance2", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Прогулка",
            sdl_Replay(
                        "alt_day6_un_fz_night_walk", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Отбой",
            sdl_Replay(
                        "alt_day6_un_fz_sleeptime2", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Ужин в одиночестве",
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
            "На поиски",
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
            "Сопровождение до лагеря",
            sdl_Replay(
                        "alt_day6_un_fz_neu_sleeptime", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Возвращение в одиночку",
            sdl_Replay(
                        "alt_day6_un_fz_neu_bad_sleeptime", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "На границе чистилища",
            sdl_Replay(
                        "alt_day6_un_fz_night_in_hell", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        )
    ]
    #### 7 День. ФЗ
    sdl_repl_array_un_fzd_day7 = [
        sdl_repl_Label(
            "Ад. Утро",
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
            "Ад. В поисках Ольги",
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
            "Ад. Отбытие",
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
            "Лена. Утро",
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
            "Лена. Завтрак",
            sdl_Replay(
                        "alt_day7_un_fz_good_breakfast", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Лена. Прощание",
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
            "Лена. Отбытие",
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
            "Утро",
            sdl_Replay(
                        "alt_day7_un_fz_neu_morning", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Завтрак",
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
            "Прощание с лагерем",
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
            "Отбытие",
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

    ## Ольга
    ### Ольга-7дл
    #### 6 День
    sdl_repl_array_mt_7dl_day6 = [
        sdl_repl_Label(
            "Утро",
            sdl_Replay(
                        "alt_day6_mt_7dl_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_mt_hent
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Завтрак",
            sdl_Replay("alt_day6_mt_7dl_breakfast", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Партийное задание",
            sdl_Replay(
                        "alt_day6_mt_7dl_morning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_mt_hent
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Утро. Алиса",
            sdl_Replay("alt_day6_mt_7dl_dv_morning", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Утро. Лена",
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
            "О ненужных",
            sdl_Replay(
                        "alt_day6_mt_7dl_retail", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_mt_hent
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Горечь",
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
            "Прощение",
            sdl_Replay("alt_day6_mt_7dl_forgive", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Первые встречи",
            sdl_Replay(
                        "alt_day6_mt_7dl_memento", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_mt_hent
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Дневник ч. 3",
            sdl_Replay("alt_day6_mt_7dl_diary3", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Обед",
            sdl_Replay(
                        "alt_day6_mt_7dl_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_mt_hent
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Воспоминания",
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
            "Концерт",
            sdl_Replay(
                        "alt_day6_mt_7dl_concert", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_dj
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Колонки",
            sdl_Replay(
                        "alt_day6_mt_7dl_sonic", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_voya
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Ужин",
            sdl_Replay("alt_day6_mt_7dl_supper", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Катапульта",
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
            "Дискотека",
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
            "Чай",
            sdl_Replay("alt_day6_mt_7dl_nighttime", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Хентай",
            sdl_Replay(
                        "alt_day6_mt_7dl_hentai", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_mt_hent
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        )
    ]
    #### 7 День
    sdl_repl_array_mt_7dl_day7 = [
        sdl_repl_Label(
            "Сон",
            sdl_Replay("alt_day7_mt_7dl_begin", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Утро",
            sdl_Replay(
                        "alt_day7_mt_7dl_morning", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_mt_volo
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Олька-комета",
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
            "Завтрак",
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
            "Прощание. Славя",
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
            "Прощание. Алиса",
            sdl_Replay("alt_day7_mt_7dl_dv_bye", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Прощание. Лена",
            sdl_Replay("alt_day7_mt_7dl_un_bye", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Прощание. Лена-ФЗ",
            sdl_Replay("alt_day7_mt_7dl_un_fz_bye", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Отъезд",
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
            "Выбор",
            sdl_Replay("alt_day7_mt_7dl_choice", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Выбор: прошлое",
            sdl_Replay("alt_day7_mt_7dl_loopthru", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Выбор: будущее",
            sdl_Replay("alt_day7_mt_7dl_loopback", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load)
        )
    ]

    ## Ульяна
    ### Ульяна-7дл
    #### 6 День
    sdl_repl_array_us_7dl_day6 = [
        sdl_repl_Label(
            "Утро",
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
            "Линейка",
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
            "Завтрак",
            sdl_Replay(
                        "alt_day6_us_7dl_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_us_7dl_pxs,
                                    sdl_var_e_d3_date,
                                    sdl_var_e_d2_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Разлука",
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
            "Помощь",
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
            "Утро. Мику",
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
            "Утро. Славя",
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
            "Утро. Лена",
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
            "Обед",
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
            "Медведь",
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
            "Спасение дезертира",
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
            "Привидение",
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
            "Фиаско",
            sdl_Replay(
                        "alt_day6_us_7dl_fiasco", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_day,
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Саундчек",
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
            "Свидание",
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
            "Концерт",
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
            "Ужин",
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
            "Дискотека. Начало",
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
            "Дискотека. Мейкап",
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
            "Дискотека",
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
            "Танец с Ульяной",
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
            "Танец с Леной",
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
            "Танец с Мику",
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
            "Танец со Славей",
            sdl_Replay(
                        "alt_day6_us_7dl_sl_dancing", {"alt_replay_on" : "True"},
                        music = music_7dl["stilllovingyou"],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Дискотека в одиночестве",
            sdl_Replay(
                        "alt_day6_us_7dl_no_dancing", {"alt_replay_on" : "True"},
                        music = music_7dl["stilllovingyou"],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Чаепитие",
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
            "Отбой",
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
            "Огоньки. Утро",
            sdl_Replay("alt_day6_us_7dl_px_begin", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Огоньки. Завтрак",
            sdl_Replay("alt_day6_us_7dl_px_breakfast", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Огоньки. Карьер",
            sdl_Replay("alt_day6_us_7dl_px_carrier", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Огоньки. Обед",
            sdl_Replay("alt_day6_us_7dl_px_dinner", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Огоньки. Сбор. Славя",
            sdl_Replay("alt_day6_us_7dl_px_party_sl", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Огоньки. Сбор. Лена",
            sdl_Replay("alt_day6_us_7dl_px_party_un", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Огоньки. Проблемы",
            sdl_Replay("alt_day6_us_7dl_px_far_gate", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Огоньки. Дискотека",
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
            "Огоньки. Счастье",
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
    #### 7 День
    sdl_repl_array_us_7dl_day7 = [
        sdl_repl_Label(
            "Утро",
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
            "Завтрак",
            sdl_Replay(
                        "alt_day7_us_7dl_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_us_7dl_help,
                                    sdl_var_e_d6_us_7dl_mi_frie,
                                    sdl_var_e_d6_us_7dl_un_frie,
                                    sdl_var_b_d6_us_7dl_px_sl_join,
                                    sdl_var_i_us_7dl_pxs
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Фотокарточки",
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
            "Домик на дереве",
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
            "Сборы с Ульяной",
            sdl_Replay("alt_day7_us_7dl_packing_us", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Сборы с Леной",
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
            "Сборы с Мику",
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
            "Сборы. Один",
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
            "Отъезд",
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
            "Эпилог",
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
            "Огоньки. Поход",
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
            "Огоньки. Автобус",
            sdl_Replay("alt_day7_us_7dl_px_bus", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Огоньки. Возвращение",
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
            "Огоньки. Пустоши",
            sdl_Replay("alt_day7_us_7dl_px_wastelands", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 5
        )
    ]

    ## Одиночка
    ### Одиночка
    #### 4 День
    sdl_repl_array_me_neu_day4 = [
        sdl_repl_Label(
            "Утро. Дома",
            sdl_Replay("alt_day4_me_neu_home", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Утро. Медпункт",
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
            "Утро. Алиса",
            sdl_Replay(
                        "alt_day4_me_neu_dv", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_dv_hous,
                                    sdl_var_b_d2_us_esca
                                    # переменные турнира
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Медпункт. Славя",
            sdl_Replay("alt_day4_me_neu_aid_sl", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Медпункт. Лена",
            sdl_Replay("alt_day4_me_neu_aid_un", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Медпункт. Ульяна",
            sdl_Replay("alt_day4_me_neu_aid_generic", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Мику. Уборка",
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
            "Славя. Поручения",
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
            "Лена. Амнезия",
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
            "Ольга. Костёр",
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
            "Ульяна. Змея",
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
            "Обед",
            sdl_Replay("alt_day4_me_neu_dinner", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Помощь Санычу",
            sdl_Replay(
                        "alt_day4_me_neu_sport", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_mi_snap
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Помощь Мику",
            sdl_Replay(
                        "alt_day4_me_neu_music", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_me_neu_date
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Помощь Жене",
            sdl_Replay(
                        "alt_day4_me_neu_nwsppr", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_me_neu_date,
                                    sdl_var_b_d3_un_fz_transit
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Помощь Кибернетикам",
            sdl_Replay(
                        "alt_day4_me_neu_cyber", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_tec2
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Побег",
            sdl_Replay(
                        "alt_day4_me_neu_curl", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_esca
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Ольга. Велосипед",
            sdl_Replay("alt_day4_me_neu_day_mt", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Ульяна. Переодевание",
            sdl_Replay(
                        "alt_day4_me_neu_day_us", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_esca
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Полдник",
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
            "Концерт",
            sdl_Replay(
                        "alt_day4_me_neu_concert", {"alt_replay_on" : "True"},
                        meets = {'dn' : 'Кудрявый'},
                        vars = [
                                    sdl_var_e_d4_me_neu_date
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Волейбол",
            sdl_Replay(
                        "alt_day4_me_neu_volley", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_sl_bath
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Ужин",
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
            "Мороженое",
            sdl_Replay(
                        "alt_day4_me_neu_reward", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Пират",
            sdl_Replay(
                        "alt_day4_me_neu_pirate", {"alt_replay_on" : "True"},
                        ambience = ambience_camp_center_evening,
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Вечер. Площадь",
            sdl_Replay(
                        "alt_day4_me_neu_square", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_voll
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Вечер. Дом Семёна и Ольги",
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
            "Вечер. Столовая",
            sdl_Replay("alt_day4_me_neu_map_dining_hall1", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Вечер. Эстрада",
            sdl_Replay(
                        "alt_day4_me_neu_map_estrade1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_me_neu_date
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Вечер. Клубы",
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
            "Вечер. Администрация",
            sdl_Replay(
                        "alt_day4_me_neu_map_admin_house1", {"alt_replay_on" : "True"},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Вечер. Лодочная станция",
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
            "Мику. Песни",
            sdl_Replay(
                        "alt_day4_me_neu_songs", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_me_neu_date
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Алиса. Шалость",
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
            "Ольга. Дневник ч. 1",
            sdl_Replay(
                        "alt_day4_me_neu_mt_diary_vol1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_voll
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Ульяна. Конфеты",
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
            "Ульяна. Гвардия",
            sdl_Replay(
                        "alt_day4_me_neu_us_guards", {"alt_replay_on" : "True"},
                        meets = {'dn' : 'Кудрявый', 'tn' : 'Странный мальчик'},
                        vars = [
                                    sdl_var_b_d2_us_esca,
                                    sdl_var_i_us_7dl
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Ульяна. Огоньки",
            sdl_Replay("alt_day4_me_neu_us_launch", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Отбой",
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
    #### 5 День
    sdl_repl_array_me_neu_day5 = [
        sdl_repl_Label(
            "Сон",
            sdl_Replay("alt_day5_me_neu_morningdream", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Утро",
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
            "Завтрак",
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
            "Дождь",
            sdl_Replay(
                        "alt_day5_me_neu_rain", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d5_me_neu_cand
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Тихий час",
            sdl_Replay("alt_day5_me_neu_along", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_repl_Label(
            "Свечка",
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
            "Свечка. Побег",
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
            "Свечка. Ответы. Герк",
            sdl_Replay(
                        "alt_day5_me_neu_day_answ_h", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Свечка. Ответы. Локи",
            sdl_Replay(
                        "alt_day5_me_neu_day_answ_l", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Свечка. Ответы. Дрищ",
            sdl_Replay(
                        "alt_day5_me_neu_day_answ_d", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Игротека",
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
            "Арестанты",
            sdl_Replay(
                        "alt_day5_me_neu_arrest", {"alt_replay_on" : "True"},
                        meets = {'dn' : 'Кудрявый', 'tn' : 'Странный мальчик'},
                        meet_restr = {'dn' : 'loki', 'tn' : 'loki'},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Обед",
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
            "Мику. Эстрада",
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
            "Мику. Помощь",
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
            "Ольга. Пляж",
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
            "Кружки. Кибернетика",
            sdl_Replay(
                        "alt_day5_me_neu_cyber_sh", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Кружки. Стенгазета",
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
            "Кружки. Спорт",
            sdl_Replay(
                        "alt_day5_me_neu_sport_sh", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Ульяна. Тоска",
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
            "Ульяна. Карьер",
            sdl_Replay("alt_day5_me_neu_us_career", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Ульяна. Попались",
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
            "Полдник",
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
            "Слежка за Славей",
            sdl_Replay(
                        "alt_day5_me_neu_sl_secret", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d4_me_neu_date
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Ужин",
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
            "Ульяна. Наказание",
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
            "Ульяна. Сытые",
            sdl_Replay("alt_day5_me_neu_us_full", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Ульяна. Голодные",
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
            "Вечер",
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
            "Костёр",
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
            "Карта. Домик ДваЧе",
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
            "Карта. Склад",
            sdl_Replay(
                        "alt_day5_me_neu_map_shed1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Карта. Медпункт",
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
            "Карта. Лодочная станция",
            sdl_Replay(
                        "alt_day5_me_neu_map_boat_station1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_me_neu_answ
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Карта. Клубы",
            sdl_Replay(
                        "alt_day5_me_neu_map_cyber1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Карта. Спортплощадка",
            sdl_Replay(
                        "alt_day5_me_neu_map_playground1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_sprt
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Карта. Пляж",
            sdl_Replay(
                        "alt_day5_me_neu_map_beach1", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Карта. Библиотека",
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
            "Карта. Неудача",
            sdl_Replay(
                        "alt_day5_me_neu_map_fail", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Вечер. Ответы. Герк",
            sdl_Replay(
                        "alt_day5_me_neu_evening_answ_h", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Вечер. Ответы. Локи",
            sdl_Replay(
                        "alt_day5_me_neu_evening_answ_l", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 4
        ),
        sdl_repl_Label(
            "Вечер. Ответы. Дрищ",
            sdl_Replay(
                        "alt_day5_me_neu_evening_answ_d", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),
        sdl_repl_Label(
            "Ульяна. Прятки",
            sdl_Replay("alt_day5_me_neu_us_hideandseek", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Ульяна. Купание",
            sdl_Replay("alt_day5_me_neu_us_warm_evening", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Ульяна. Ограбление",
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
            "Ульяна. Уборка",
            sdl_Replay("alt_day5_me_neu_us_cleaning", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            char_mask = 5
        ),
        sdl_repl_Label(
            "Отбой",
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
            "Отбой. Промокший",
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
            "Отбой. Пьяный",
            sdl_Replay(
                        "alt_day5_me_neu_sleeptime_drunk", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_cs_debt
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Отбой. Сбежавший",
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
            "Отбой. Ответы. Герк",
            sdl_Replay(
                        "alt_day5_me_neu_sleeptime_answ_h", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 2
        ),
        sdl_repl_Label(
            "Отбой. Ответы. Дрищ",
            sdl_Replay(
                        "alt_day5_me_neu_sleeptime_answ_d", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            char_mask = 1
        ),

        sdl_repl_Label(
            "Ульяна. Отбой",
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
            "Ольга. Дневник ч. 2",
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
            "Ольга. «Чаепитие»",
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
    #### 6 День
    sdl_repl_array_me_neu_day6 = [
        sdl_repl_Label(
            "Дежурный. Пробуждение",
            sdl_Replay(
                        "alt_day6_me_neu_begin_duty", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_mt_7dl,
                                    sdl_var_i_us_lpp,
                                    sdl_var_b_d3_me_duty
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Пробуждение",
            sdl_Replay(
                        "alt_day6_me_neu_begin", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d5_me_neu_mapi
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Завтрак с Алисой",
            sdl_Replay(
                        "alt_day6_me_neu_breakfast_dv", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Завтрак",
            sdl_Replay(
                        "alt_day6_me_neu_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d5_me_neu_mapi,
                                    sdl_var_l_d2_club,
                                    sdl_var_b_d5_me_neu_cs_debt
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Завтрак. Дежурство",
            sdl_Replay(
                        "alt_day6_me_neu_breakfast_duty", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_me_neu_mt_help
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "После завтрака",
            sdl_Replay(
                        "alt_day6_me_neu_after_breakfast", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_club
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Месть Алисы",
            sdl_Replay(
                        "alt_day6_me_neu_dv_revenge", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Рандеву с вожатой",
            sdl_Replay(
                        "alt_day6_me_neu_mt_help", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_l_d2_club,
                                    sdl_var_i_mt_7dl
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Дни минувшего прошлого",
            sdl_Replay(
                        "alt_day6_me_neu_nwsppr", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_mz_news,
                                    sdl_var_i_me_neu_answ,
                                    sdl_var_i_sl_lpp,
                                    sdl_var_e_d1_sl_key
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "В глубине души твоей",
            sdl_Replay(
                        "alt_day6_me_neu_nwsppr_mz", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Приключения Электроника",
            sdl_Replay(
                        "alt_day6_me_neu_cyber", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_cybr,
                                    sdl_var_e_d5_me_neu_mapi,
                                    sdl_var_i_mi_lpp,
                                    sdl_var_i_dv_lpp,
                                    sdl_var_i_sl_lpp,
                                    sdl_var_i_un_lpp,
                                    sdl_var_i_us_lpp,
                                    sdl_var_i_mt_7dl
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "День физкультурника",
            sdl_Replay(
                        "alt_day6_me_neu_sport", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_ba_duty,
                                    sdl_var_b_d5_me_neu_sprt,
                                    sdl_var_e_d5_me_neu_mapi
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Музыкальная пауза",
            sdl_Replay(
                        "alt_day6_me_neu_music", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_mi_club,
                                    sdl_var_i_mi_lpp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Вопрос с подвохом",
            sdl_Replay(
                        "alt_day6_me_neu_viola_duty", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Под водой",
            sdl_Replay(
                        "alt_day6_me_neu_beach", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_cs_debt,
                                    sdl_var_e_d5_me_neu_mapi
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Обед. Дежурство",
            sdl_Replay(
                        "alt_day6_me_neu_duty", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_mz_7dl,
                                    sdl_var_e_d5_me_neu_mapi
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Обед",
            sdl_Replay(
                        "alt_day6_me_neu_lunch", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d5_me_neu_mapi
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Карта. Домик рыжих",
            sdl_Replay(
                        "alt_day6_me_neu_map_house_dv1", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_dv_lpp,
                                    sdl_var_i_us_lpp,
                                    sdl_var_e_d5_me_neu_mapi,
                                    sdl_var_b_d6_me_neu_dv_reve,
                                    sdl_var_b_d4_me_neu_cs_debt,
                                    sdl_var_e_d6_me_neu_danc
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Карта. Музклуб",
            sdl_Replay(
                        "alt_day6_me_neu_map_musclub", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_me_neu_mi_club,
                                    sdl_var_i_mi_lpp
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Карта. Склад",
            sdl_Replay(
                        "alt_day6_me_neu_map_shed", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_me_neu_nwsp,
                                    sdl_var_e_d1_sl_key,
                                    sdl_var_b_d4_me_neu_voll,
                                    sdl_var_i_sl_lpp,
                                    sdl_var_i_sl_clt,
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Карта. Свой домик",
            sdl_Replay(
                        "alt_day6_me_neu_map_mt_house", {"alt_replay_on" : "True"},
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Приглашение Ольги",
            sdl_Replay(
                        "alt_day6_me_neu_mt_invite", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d5_me_neu_mapi
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Полдник",
            sdl_Replay(
                        "alt_day6_me_neu_afternoon", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d5_me_neu_mapi
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Возле столовой",
            sdl_Replay(
                        "alt_day6_me_neu_concert", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_un_lpp,
                                    sdl_var_e_d6_me_neu_danc
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Инспекция",
            sdl_Replay(
                        "alt_day6_me_neu_inspection", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_mz_7dl,
                                    sdl_var_e_d6_me_neu_danc
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Побег",
            sdl_Replay(
                        "alt_day6_me_neu_un_escape", {"alt_replay_on" : "True"},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Ужин",
            sdl_Replay(
                        "alt_day6_me_neu_dinner", {"alt_replay_on" : "True"},
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Общий сбор",
            sdl_Replay(
                        "alt_day6_me_after_dinner", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_me_neu_danc,
                                    sdl_var_b_d6_me_neu_un_esca
                                ],
                        func_in = sunset_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Дискотека",
            sdl_Replay(
                        "alt_day6_me_neu_dance", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_me_neu_danc
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "ЧП",
            sdl_Replay(
                        "alt_day6_me_neu_un_dance", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Танец с Мику",
            sdl_Replay(
                        "alt_day6_me_neu_mi_dance", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Вечер с Алисой",
            sdl_Replay(
                        "alt_day6_me_neu_dv_dance", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Пират",
            sdl_Replay(
                        "alt_day6_me_neu_sl_dance", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Сбежавшая вожатая",
            sdl_Replay(
                        "alt_day6_me_neu_mt_dance", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Танец с Ульяной",
            sdl_Replay(
                        "alt_day6_me_neu_us_danсe", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d5_me_neu_cs_debt
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Дискотека с Женей",
            sdl_Replay(
                        "alt_day6_me_neu_mz_danсe", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Вечер с Кибернетиками",
            sdl_Replay(
                        "alt_day6_me_neu_el_dance", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_tec2,
                                    sdl_var_e_d3_dj
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Танец с Катюшкой",
            sdl_Replay(
                        "alt_day6_me_neu_ka_danсe", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_me_neu_cs_debt
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Отмена свечки",
            sdl_Replay(
                        "alt_day6_me_neu_no_candle", {"alt_replay_on" : "True"},
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Свечка",
            sdl_Replay(
                        "alt_day6_me_neu_candle", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_me_neu_danc,
                                    sdl_var_i_mt_7dl,
                                    sdl_var_i_us_7dl,
                                    sdl_var_i_mz_7dl,
                                    sdl_var_i_mi_lpp,
                                    sdl_var_i_dv_lpp,
                                    sdl_var_i_sl_lpp,
                                    sdl_var_i_un_lpp,
                                    sdl_var_b_d4_me_neu_us_debt,
                                    sdl_var_b_d5_me_neu_cybr,
                                    sdl_var_b_d6_me_neu_cybr,
                                    sdl_var_b_d6_me_neu_mt_help
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
        sdl_repl_Label(
            "Отбой",
            sdl_Replay(
                        "alt_day6_me_neu_sleeptime", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d6_me_neu_danc,
                                    sdl_var_i_mz_7dl,
                                    sdl_var_b_d4_me_neu_us_debt,
                                    sdl_var_b_d5_me_neu_cybr,
                                    sdl_var_b_d6_me_neu_cybr
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      )
        ),
    ]

    sdl_repl_label_frozen = [
                             ]

    # Дни

    ## Коммон
    sdl_repl_common_day0 = sdl_repl_Day("Пролог", sdl_repl_array_common_day0)
    sdl_repl_common_day1 = sdl_repl_Day("День 1", sdl_repl_array_common_day1)
    sdl_repl_common_day2 = sdl_repl_Day("День 2", sdl_repl_array_common_day2)
    sdl_repl_common_day3 = sdl_repl_Day("День 3", sdl_repl_array_common_day3)
    sdl_repl_common_days = [
        sdl_repl_common_day0,
        sdl_repl_common_day1,
        sdl_repl_common_day2,
        sdl_repl_common_day3
    ]

    ## Мику
    ### Мику-7дл
    sdl_repl_mi_7dl_day4 = sdl_repl_Day("День 4", sdl_repl_array_mi_7dl_day4)
    sdl_repl_mi_7dl_day5 = sdl_repl_Day("День 5", sdl_repl_array_mi_7dl_day5)
    sdl_repl_mi_7dl_day6 = sdl_repl_Day("День 6", sdl_repl_array_mi_7dl_day6)
    sdl_repl_mi_7dl_day7 = sdl_repl_Day("День 7", sdl_repl_array_mi_7dl_day7)
    sdl_repl_mi_7dl_days = [
        sdl_repl_mi_7dl_day4,
        sdl_repl_mi_7dl_day5,
        sdl_repl_mi_7dl_day6,
        sdl_repl_mi_7dl_day7
    ]
    ### Мику-Диджей
    sdl_repl_mi_djt_day4 = sdl_repl_Day("День 4", sdl_repl_array_mi_djt_day4)
    sdl_repl_mi_djt_day5 = sdl_repl_Day("День 5", sdl_repl_array_mi_djt_day5)
    sdl_repl_mi_djt_day6 = sdl_repl_Day("День 6", sdl_repl_array_mi_djt_day6)
    sdl_repl_mi_djt_day7 = sdl_repl_Day("День 7", sdl_repl_array_mi_djt_day7)
    sdl_repl_mi_djt_days = [
        sdl_repl_mi_djt_day4,
        sdl_repl_mi_djt_day5,
        sdl_repl_mi_djt_day6,
        sdl_repl_mi_djt_day7
    ]

    ## Алиса
    ### Алиса-7дл
    sdl_repl_dv_7dl_day4 = sdl_repl_Day("День 4", sdl_repl_array_dv_7dl_day4)
    sdl_repl_dv_7dl_day5 = sdl_repl_Day("День 5", sdl_repl_array_dv_7dl_day5)
    sdl_repl_dv_7dl_day6 = sdl_repl_Day("День 6", sdl_repl_array_dv_7dl_day6)
    sdl_repl_dv_7dl_day7 = sdl_repl_Day("День 7", sdl_repl_array_dv_7dl_day7)
    sdl_repl_dv_7dl_days = [
        sdl_repl_dv_7dl_day4,
        sdl_repl_dv_7dl_day5,
        sdl_repl_dv_7dl_day6,
        sdl_repl_dv_7dl_day7
    ]
    ### Алиса-Диджей
    sdl_repl_dv_djt_day4 = sdl_repl_Day("День 4", sdl_repl_array_dv_djt_day4)
    sdl_repl_dv_djt_day5 = sdl_repl_Day("День 5", sdl_repl_array_dv_djt_day5)
    sdl_repl_dv_djt_day6 = sdl_repl_Day("День 6", sdl_repl_array_dv_djt_day6)
    sdl_repl_dv_djt_day7 = sdl_repl_Day("День 7", sdl_repl_array_dv_djt_day7)
    sdl_repl_dv_djt_days = [
        sdl_repl_dv_djt_day4,
        sdl_repl_dv_djt_day5,
        sdl_repl_dv_djt_day6,
        sdl_repl_dv_djt_day7
    ]

    ## Славя
    ### Славя-7дл
    sdl_repl_sl_7dl_day4 = sdl_repl_Day("День 4", sdl_repl_array_sl_7dl_day4)
    sdl_repl_sl_7dl_day5 = sdl_repl_Day("День 5", sdl_repl_array_sl_7dl_day5)
    sdl_repl_sl_7dl_day6 = sdl_repl_Day("День 6", sdl_repl_array_sl_7dl_day6)
    sdl_repl_sl_7dl_day7 = sdl_repl_Day("День 7", sdl_repl_array_sl_7dl_day7)
    sdl_repl_sl_7dl_days = [
        sdl_repl_sl_7dl_day4,
        sdl_repl_sl_7dl_day5,
        sdl_repl_sl_7dl_day6,
        sdl_repl_sl_7dl_day7
    ]
    ### Славя-Классик
    sdl_repl_sl_clt_day4 = sdl_repl_Day("День 4", sdl_repl_array_sl_clt_day4)
    sdl_repl_sl_clt_day5 = sdl_repl_Day("День 5", sdl_repl_array_sl_clt_day5)
    sdl_repl_sl_clt_day6 = sdl_repl_Day("День 6", sdl_repl_array_sl_clt_day6)
    sdl_repl_sl_clt_day7 = sdl_repl_Day("День 7", sdl_repl_array_sl_clt_day7)
    sdl_repl_sl_clt_dayx = sdl_repl_Day("День ???", sdl_repl_array_sl_clt_dayx)
    sdl_repl_sl_clt_days = [
        sdl_repl_sl_clt_day4,
        sdl_repl_sl_clt_day5,
        sdl_repl_sl_clt_day6,
        sdl_repl_sl_clt_day7,
        sdl_repl_sl_clt_dayx
    ]

    ## Лена
    ### Лена-7дл
    sdl_repl_un_7dl_day4 = sdl_repl_Day("День 4", sdl_repl_array_un_7dl_day4)
    sdl_repl_un_7dl_day5 = sdl_repl_Day("День 5", sdl_repl_array_un_7dl_day5)
    sdl_repl_un_7dl_day6 = sdl_repl_Day("День 6", sdl_repl_array_un_7dl_day6)
    sdl_repl_un_7dl_day7 = sdl_repl_Day("День 7", sdl_repl_array_un_7dl_day7)
    sdl_repl_un_7dl_days = [
        sdl_repl_un_7dl_day4,
        sdl_repl_un_7dl_day5,
        sdl_repl_un_7dl_day6,
        sdl_repl_un_7dl_day7
    ]
    ### Лена-Френдзона
    sdl_repl_un_fzd_day4 = sdl_repl_Day("День 4", sdl_repl_array_un_fzd_day4, char_mask=2)
    sdl_repl_un_fzd_day5 = sdl_repl_Day("День 5", sdl_repl_array_un_fzd_day5, char_mask=2)
    sdl_repl_un_fzd_day6 = sdl_repl_Day("День 6. Дорога", sdl_repl_array_un_fzd_day6, char_mask=2)
    sdl_repl_un_fzd_day62 = sdl_repl_Day("День 6. ФЗ", sdl_repl_array_un_fzd_day62, char_mask=2)
    sdl_repl_un_fzd_day7 = sdl_repl_Day("День 7. ФЗ", sdl_repl_array_un_fzd_day7, char_mask=2)
    sdl_repl_un_fzd_days = [
        sdl_repl_un_fzd_day4,
        sdl_repl_un_fzd_day5,
        sdl_repl_un_fzd_day6,
        sdl_repl_un_fzd_day62,
        sdl_repl_un_fzd_day7
    ]

    ## Ольга
    ### Ольга-7дл
    sdl_repl_mt_7dl_day6 = sdl_repl_Day("День 6", sdl_repl_array_mt_7dl_day6)
    sdl_repl_mt_7dl_day7 = sdl_repl_Day("День 7", sdl_repl_array_mt_7dl_day7)
    sdl_repl_mt_7dl_days = [
        sdl_repl_mt_7dl_day6,
        sdl_repl_mt_7dl_day7
    ]

    ## Ульяна
    ### Ульяна-7дл
    sdl_repl_us_7dl_day6 = sdl_repl_Day("День 6", sdl_repl_array_us_7dl_day6, char_mask=5)
    sdl_repl_us_7dl_day7 = sdl_repl_Day("День 7", sdl_repl_array_us_7dl_day7, char_mask=5)
    sdl_repl_us_7dl_days = [
        sdl_repl_us_7dl_day6,
        sdl_repl_us_7dl_day7
    ]

    ## Одиночка
    ### Одиночка
    sdl_repl_me_neu_day4 = sdl_repl_Day("День 4", sdl_repl_array_me_neu_day4)
    sdl_repl_me_neu_day5 = sdl_repl_Day("День 5", sdl_repl_array_me_neu_day5)
    sdl_repl_me_neu_day6 = sdl_repl_Day("День 6", sdl_repl_array_me_neu_day6)
    sdl_repl_me_neu_days = [
        sdl_repl_me_neu_day4,
        sdl_repl_me_neu_day5,
        sdl_repl_me_neu_day6
    ]

    # Руты | Разделы

    ## Коммон
    sdl_repl_common = sdl_repl_Section("Коммон-рут", None, None, sdl_repl_common_days)

    ## Мику
    sdl_repl_mi_7dl = sdl_repl_Section("Мику-7дл",     None, None, sdl_repl_mi_7dl_days)
    sdl_repl_mi_djt = sdl_repl_Section("Мику-Диджей",  None, None, sdl_repl_mi_djt_days)
    sdl_repl_mi_routes = [
        sdl_repl_mi_7dl,
        sdl_repl_mi_djt
    ]
    sdl_repl_mi = sdl_repl_Section("Мику", "sdl_repl_section_label_mi", sdl_repl_mi_routes, None)

    ## Алиса
    sdl_repl_dv_7dl = sdl_repl_Section("Алиса-7дл",     None, None, sdl_repl_dv_7dl_days)
    sdl_repl_dv_djt = sdl_repl_Section("Алиса-Диджей",  None, None, sdl_repl_dv_djt_days)
    sdl_repl_dv_routes = [
        sdl_repl_dv_7dl,
        sdl_repl_dv_djt
    ]
    sdl_repl_dv = sdl_repl_Section("Алиса", "sdl_repl_section_label_dv", sdl_repl_dv_routes, None)

    ## Славя
    sdl_repl_sl_7dl = sdl_repl_Section("Славя-7дл",     None, None, sdl_repl_sl_7dl_days)
    sdl_repl_sl_clt = sdl_repl_Section("Славя-Классик", None, None, sdl_repl_sl_clt_days)
    sdl_repl_sl_routes = [
        sdl_repl_sl_7dl,
        sdl_repl_sl_clt
    ]
    sdl_repl_sl = sdl_repl_Section("Славя", "sdl_repl_section_label_sl", sdl_repl_sl_routes, None)

    ## Лена
    sdl_repl_un_7dl = sdl_repl_Section("Лена-7дл",       None, None, sdl_repl_un_7dl_days)
    sdl_repl_un_fzd = sdl_repl_Section("Лена-Френдзона", None, None, sdl_repl_un_fzd_days)
    sdl_repl_un_routes = [
        sdl_repl_un_7dl,
        sdl_repl_un_fzd
    ]
    sdl_repl_un = sdl_repl_Section("Лена", "sdl_repl_section_label_un", sdl_repl_un_routes, None)

    ## Ольга
    sdl_repl_mt_7dl = sdl_repl_Section("Ольга-7дл",       None, None, sdl_repl_mt_7dl_days)
    sdl_repl_mt_routes = [
        sdl_repl_mt_7dl
    ]
    sdl_repl_mt = sdl_repl_Section("Ольга", "sdl_repl_section_label_mt", sdl_repl_mt_routes, None)

    ## Ульяна
    sdl_repl_us_7dl = sdl_repl_Section("Ульяна-7дл",     None, None, sdl_repl_us_7dl_days)
    sdl_repl_us_routes = [
        sdl_repl_us_7dl
    ]
    sdl_repl_us = sdl_repl_Section("Ульяна", "sdl_repl_section_label_us", sdl_repl_us_routes, None)

    ## Одиночка
    sdl_repl_me_neu = sdl_repl_Section("Семён-Одиночка", None, None, sdl_repl_me_neu_days)
    sdl_repl_me_routes = [
        sdl_repl_me_neu
    ]
    sdl_repl_me = sdl_repl_Section("Семён", "sdl_repl_section_label_me", sdl_repl_me_routes, None)

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



    # Протагонисты
    sdl_repl_characters = [
        sdl_Character("sdl_repl_char_none", 15, None, None),
        sdl_Character("sdl_repl_char_loki", 4, "sdl_repl_char_label_loki", "loki"),
        sdl_Character("sdl_repl_char_herc", 2, "sdl_repl_char_label_herc", "herc"),
        sdl_Character("sdl_repl_char_dr",   1, "sdl_repl_char_label_dr",   "dr")
    ]



    sdl_repl_engine = sdl_repl_Engine(sdl_repl_sections)
