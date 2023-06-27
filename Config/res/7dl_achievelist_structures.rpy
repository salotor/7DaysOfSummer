init 9999 python:
    ##### КАК ЭТО РАБОТАЕТ #####
    # Все концовки загоняются в массив концовок рута (в том порядке, в котором они и будут выводиться).
    # А руты - в массивы рутов персонажа.
    #
    # Объект sdl_achv_Achievement (ачивка):
    ## icon          - иконка концовки
    ## persistent    - название перзистента
    ## text          - надпись (объявляется в ресурсах), описывающая характер концовки
    ## prerequisites - массив объектов sdl_achv_Prerequisite, описывающих требования для выхода на концовку
    ## replay        - объект sdl_Replay, использующийся для перехода к концовке
    ## sprite_emo    - эмоции персонажей, отображаемые в ачивлисте
    ## char_mask     - определяет, каким ГГ доступна концовка (1 - дрищ, 2 - герк, 3 - не локи, 4 - локи, 5 - не герк, 6 - не дрищ, 7 - любой)
    ## postscriptum  - аналогично replay, но на послесловия
    #
    # Объект sdl_achv_Prerequisite (требование к концовке):
    ## text         - надпись (объявляется в ресурсах), описывающая тип требования
    ## achievements - список объектов sdl_achv_Achievement, удовлетворяющих условию (поля prerequisites и replay не обязательны)
    ## conditions   - список перзистентов, удовлетворяющих условию
    ###
    ### Пример: пусть для выхода на концовку стоит условие:
    ###     (persistent.us_7dl_tran_un or persistent.us_7dl_tran_mi) and persistent.us_px_good
    ### Тогда нужно создать 2 объекта-требования
    ###     sdl_achv_Prerequisite(
    ###         "sdl_achv_info_end",
    ###         {
    ###             sdl_achv_Achievement("acm_logo_us_px_good", "us_px_good", "sdl_achv_us_good", None, None)
    ###         }
    ###     ),
    ###     sdl_achv_Prerequisite(
    ###         "sdl_achv_info_end",
    ###         {
    ###             sdl_achv_Achievement("acm_logo_us_7dl_tran_un", "us_7dl_tran_un", "sdl_achv_us_tran_un", None, None),
    ###             sdl_achv_Achievement("acm_logo_us_7dl_tran_mi", "us_7dl_tran_mi", "sdl_achv_us_tran_mi", None, None)
    ###         }
    ###     )
    #
    # Объект sdl_Replay (повтор):
    ## label      - метка, к которой надо перейти для просмотра
    ## scope      - scope-параметр ренпаевского Replay. Здесь следует инициализировать необходимые переменные
    ## meets      - переназначения стандартных имён персонажей
    ## meet_restr - условия, при которых переназывать персонажей не требуется
    ## music      - музыка, включаемая в начале лейбла
    ## ambience   - амбиенс, включаемый в начале лейбла
    ## sound_loop - sound_loop, включаемый в начале лейбла
    ## vars       - флаги, влияющие на события лейбла
    ## func_in    - функция, которую требуется выполнить перед просмотром лейбла
    ## func_out   - функция, которую требуется выполнить после просмотра лейбла
    ############################

    # Массивы концовок всех рутов

    ## Мику-7дл
    sdl_achv_array_mi_7dl = [
        sdl_achv_Achievement(    # Осколок памяти
            "acm_logo_mi_7dl_shard",
            "mi_7dl_shard",
            "sdl_achv_mi_shard",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_puz",
                    None,
                    conditions = {"alt_binder"}
                )
            ],
            sdl_Replay("alt_day7_mi_7dl_shard", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "serious",
            7,
            None,
            Show("sdl_achv_sprite", Dissolve(0.5), "ars", "smile3", "pajama"),
            persistent.alt_binder
        ),
        sdl_achv_Achievement(    # Гуд-СССР
            "acm_logo_mi_7dl_good_ussr",
            "mi_7dl_good_ussr",
            "sdl_achv_mi_good_US",
            [],
            sdl_Replay("alt_day7_mi_7dl_good_ussr", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "smile"
        ),
        sdl_achv_Achievement(    # Гуд-M
            "acm_logo_mi_7dl_good_human",
            "mi_7dl_good_human",
            "sdl_achv_mi_good",
            [],
            sdl_Replay("alt_day7_mi_7dl_good_human", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "happy",
            7,
            sdl_Replay(
                        "alt_day7_mi_7dl_good_human_ps", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_mi_snap
                                ],
                        func_in = prolog_interface_on, func_out = replay_screens_load
                      ),
        ),
        sdl_achv_Achievement(    # Гуд-S
            "acm_logo_mi_7dl_good_star",
            "mi_7dl_good_star",
            "sdl_achv_mi_good_IN",
            [],
            sdl_Replay("alt_day7_mi_7dl_good_star", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "happy",
            7,
            sdl_Replay("alt_day7_mi_7dl_good_star_ps", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
        ),
        sdl_achv_Achievement(    # Эксклюзив-Локи
            "acm_logo_mi_7dl_loki_exc",
            "mi_7dl_loki_exc",
            "sdl_achv_mi_LO_exc",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mi_7dl_good_human", "mi_7dl_good_human", "sdl_achv_mi_good", None, None),
                        sdl_achv_Achievement("acm_logo_mi_7dl_good_star", "mi_7dl_good_star", "sdl_achv_mi_good_IN", None, None)
                    }
                )
            ],
            sdl_Replay("alt_day7_mi_7dl_loki_exc", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "upset",
            char_mask = 4
        ),
        sdl_achv_Achievement(    # Эксклюзив-Герк
            "acm_logo_mi_7dl_herc_exc",
            "mi_7dl_herc_exc",
            "sdl_achv_mi_HE_exc",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mi_7dl_good_human", "mi_7dl_good_human", "sdl_achv_mi_good", None, None),
                        sdl_achv_Achievement("acm_logo_mi_7dl_good_star", "mi_7dl_good_star", "sdl_achv_mi_good_IN", None, None)
                    }
                )
            ],
            sdl_Replay("alt_day7_mi_7dl_herc_exc", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "smile",
            char_mask = 2
        ),
        sdl_achv_Achievement(    # Эксклюзив-Дрищ
            "acm_logo_mi_7dl_dr_exc",
            "mi_7dl_dr_exc",
            "sdl_achv_mi_DR_exc",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mi_7dl_good_human", "mi_7dl_good_human", "sdl_achv_mi_good", None, None),
                        sdl_achv_Achievement("acm_logo_mi_7dl_good_star", "mi_7dl_good_star", "sdl_achv_mi_good_IN", None, None)
                    }
                )
            ],
            sdl_Replay("alt_day7_mi_7dl_dr_exc", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "smile2",
            char_mask = 1
        ),
        sdl_achv_Achievement(    # Бэд-M
            "acm_logo_mi_7dl_bad_human",
            "mi_7dl_bad_human",
            "sdl_achv_mi_bad",
            [],
            sdl_Replay("alt_day7_mi_7dl_bad_human", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "sad"
        ),
        sdl_achv_Achievement(    # Бэд-S
            "acm_logo_mi_7dl_bad_star",
            "mi_7dl_bad_star",
            "sdl_achv_mi_bad",
            [],
            sdl_Replay(
                        "alt_day7_mi_7dl_bad_star", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d3_date
                                ],
                        func_in = prolog_interface_on, func_out = replay_screens_load
                      ),
            "sad"
        )
    ]

    ## Мику-DJ
    sdl_achv_array_mi_djt = [
        sdl_achv_Achievement(    # ТруЪ
            "acm_logo_mi_dj_true",
            "mi_dj_true",
            "sdl_achv_mi_true",
            [],
            sdl_Replay("alt_day7_mi_dj_true", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "cry_smile"
        ),
        sdl_achv_Achievement(    # Гуд-Япония
            "acm_logo_mi_dj_good",
            "mi_dj_good_jap",
            "sdl_achv_mi_good",
            [],
            sdl_Replay("alt_day7_mi_dj_good_jap", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "happy"
        ),
        sdl_achv_Achievement(    # Гуд-РФ
            "acm_logo_mi_dj_good_rf",
            "mi_dj_good_rf",
            "sdl_achv_mi_good_RF",
            [],
            sdl_Replay(
                        "alt_day7_mi_dj_good_rf", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_mi_dj_hedg,
                                    sdl_var_b_d6_mi_dj_walk,
                                    sdl_var_e_d5_mi_dj_apol
                                ],
                        func_in = prolog_interface_on, func_out = replay_screens_load
                      ),
            "happy"
        ),
        sdl_achv_Achievement(    # Рикошет
            "acm_logo_mi_dj_rej",
            "mi_dj_reject",
            "sdl_achv_mi_rej",
            [],
            sdl_Replay("alt_day7_mi_dj_reject", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "surprise"
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_mi_dj_bad",
            "mi_dj_bad",
            "sdl_achv_mi_bad",
            [],
            sdl_Replay("alt_day7_mi_dj_bad", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "cry"
        )
    ]


    ## Алиса-7дл
    sdl_achv_array_dv_7dl = [
        sdl_achv_Achievement(    # Осколок памяти
            "acm_logo_dv_7dl_shard",
            "dv_7dl_shard",
            "sdl_achv_dv_shard",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_puz",
                    None,
                    conditions = {"alt_binder"}
                )
            ],
            sdl_Replay("alt_day7_dv_7dl_shard", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "normal",
            7,
            None,
            Show("sdl_achv_sprite", Dissolve(0.5), "ars", "smile", "coat"),
            persistent.alt_binder
        ),
        sdl_achv_Achievement(    # Гуд-СССР
            "acm_logo_dv_7dl_good_ussr",
            "dv_7dl_good_ussr",
            "sdl_achv_dv_good_US",
            [],
            sdl_Replay(
                        "alt_day7_dv_7dl_good_ussr", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d4_dv_7dl_cs_help,
                                    sdl_var_i_sl_7dl
                                ],
                        func_in = prolog_interface_on, func_out = replay_screens_load
                      ),
            "laugh"
        ),
        sdl_achv_Achievement(    # Гуд-РФ
            "acm_logo_dv_7dl_good_rf",
            "dv_7dl_good_rf",
            "sdl_achv_dv_good_RF",
            [],
            sdl_Replay("alt_day7_dv_7dl_good_rf", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "laugh",
            7,
            sdl_Replay("alt_day7_dv_7dl_good_rf_ps", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
        ),
        sdl_achv_Achievement(    # Реджект-СССР
            "acm_logo_dv_7dl_rej_ussr",
            "dv_7dl_rej_ussr",
            "sdl_achv_dv_rej_US",
            [],
            sdl_Replay("alt_day7_dv_7dl_rej_ussr", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "sad"
        ),
        sdl_achv_Achievement(    # Реджект-РФ
            "acm_logo_dv_7dl_rej_rf",
            "dv_7dl_rej_rf",
            "sdl_achv_dv_rej_RF",
            [],
            sdl_Replay("alt_day7_dv_7dl_rej_rf", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "shy"
        ),
        sdl_achv_Achievement(    # Транзит-Лена
            "acm_logo_dv_7dl_tran_un",
            "dv_7dl_tran_un",
            "sdl_achv_dv_tran",
            [],
            sdl_Replay("alt_day7_dv_7dl_tran_un", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "rage",
            7,
            None,
            Show("sdl_achv_sprite", Dissolve(0.5), "un", "cry", "casual")
        ),
        sdl_achv_Achievement(    # Эксклюзив-Локи
            "acm_logo_dv_7dl_loki_exc",
            "dv_7dl_loki_exc",
            "sdl_achv_dv_LO_exc",
            [],
            sdl_Replay(
                        "alt_day7_dv_7dl_loki_exc", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_date
                                ],
                        func_in = day_interface_on, func_out = replay_screens_load
                      ),
            "guilty",
            char_mask = 4
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_dv_7dl_bad",
            "dv_7dl_bad",
            "sdl_achv_dv_bad",
            [],
            sdl_Replay(
                        "alt_day7_dv_7dl_bad", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d3_me_duty,
                                    sdl_var_b_d4_dv_7dl_port,
                                    sdl_var_e_d6_dv_7dl_rout
                                ],
                        func_in = prolog_interface_on, func_out = replay_screens_load
                      ),
            "cry",
            7,
            sdl_Replay("alt_day7_dv_7dl_bad_ps", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
        )
    ]

    ## Алиса-DJ
    sdl_achv_array_dv_djt = [
        sdl_achv_Achievement(    # ТруЪ
            "acm_logo_dv_dj_true",
            "dv_dj_true",
            "sdl_achv_dv_true",
            [],
            sdl_Replay("alt_day7_dv_dj_true", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "sad"
        ),
        sdl_achv_Achievement(    # Гуд
            "acm_logo_dv_dj_good",
            "dv_dj_good",
            "sdl_achv_dv_good",
            [],
            sdl_Replay("alt_day7_dv_dj_good", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "laugh"
        ),
        sdl_achv_Achievement(    # Нейтрал
            "acm_logo_dv_dj_neu",
            "dv_dj_neu",
            "sdl_achv_dv_neu",
            [],
            sdl_Replay("alt_day7_dv_dj_neu", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "normal"
        ),
        sdl_achv_Achievement(    # Реджект
            "acm_logo_dv_dj_rej",
            "dv_dj_rej",
            "sdl_achv_dv_rej",
            [],
            sdl_Replay("alt_day7_dv_dj_rej", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "smile"
        ),
        sdl_achv_Achievement(    # Эксклюзив-Герк
            "acm_logo_dv_dj_herc_exc",
            "dv_dj_herc_exc",
            "sdl_achv_dv_HE_exc",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_dv_dj_true", "dv_dj_true", "sdl_achv_dv_true", None, None)
                    }
                )
            ],
            sdl_Replay("alt_day7_dv_dj_herc_exc", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "shy",
            char_mask = 2
        ),
        sdl_achv_Achievement(    # Эксклюзив-Локи
            "acm_logo_dv_dj_loki_exc",
            "dv_dj_loki_exc",
            "sdl_achv_dv_LO_exc",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_dv_dj_true", "dv_dj_true", "sdl_achv_dv_true", None, None)
                    }
                )
            ],
            sdl_Replay("alt_day7_dv_dj_loki_exc", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "normal",
            char_mask = 4
        ),
        sdl_achv_Achievement(    # Эксклюзив-Дрищ
            "acm_logo_dv_dj_dr_exc",
            "dv_dj_dr_exc",
            "sdl_achv_dv_DR_exc",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_dv_dj_true", "dv_dj_true", "sdl_achv_dv_true", None, None)
                    }
                )
            ],
            sdl_Replay("alt_day7_dv_dj_dr_exc", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "guilty",
            char_mask = 1
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_dv_dj_bad",
            "dv_dj_bad",
            "sdl_achv_dv_bad",
            [],
            sdl_Replay("alt_day7_dv_dj_bad", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "cry"
        )
    ]

    ## Славя-7дл
    sdl_achv_array_sl_7dl = [
        sdl_achv_Achievement(    # Осколок памяти
            "acm_logo_sl_7dl_shard",
            "sl_7dl_shard",
            "sdl_achv_sl_shard",
            [
                sdl_achv_Prerequisite(
                        "sdl_achv_info_puz",
                        None,
                        conditions = {"alt_binder"}
                )
            ],
            sdl_Replay("alt_day7_sl_7dl_shard", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "sad",
            7,
            None,
            Show("sdl_achv_sprite", Dissolve(0.5), "ars", "sad", "casual"),
            persistent.alt_binder
        ),
        sdl_achv_Achievement(    # РФ-гуд
            "acm_logo_sl_7dl_good_rf",
            "sl_7dl_good_rf",
            "sdl_achv_sl_good_RF",
            [],
            sdl_Replay(
                        "alt_day7_sl_7dl_good_rf", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_karma
                                ],
                        func_in = prolog_interface_on, func_out = replay_screens_load
                      ),
            "shy",
            7,
            sdl_Replay(
                        "alt_day7_sl_7dl_good_rf_ps", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_karma
                                ],
                        func_in = prolog_interface_on, func_out = replay_screens_load
                      ),
        ),
        sdl_achv_Achievement(    # Локи-Гуд
            "acm_logo_sl_7dl_loki_good",
            "sl_7dl_loki_good",
            "sdl_achv_sl_LO_good",
            [],
            sdl_Replay(
                        "alt_day7_sl_7dl_loki_good", {"alt_replay_on" : "True"},
                        meets = {'uv' : 'Кошкодевочка'},
                        vars = [
                                    sdl_var_b_d2_me_mini
                                ],
                        func_in = prolog_interface_on, func_out = replay_screens_load
                      ),
            "happy",
            char_mask = 4
        ),
        sdl_achv_Achievement(    # Локи-Нейтрал
            "acm_logo_sl_7dl_loki_neu",
            "sl_7dl_loki_neu",
            "sdl_achv_sl_LO_neu",
            [],
            sdl_Replay(
                        "alt_day7_sl_7dl_loki_neu", {"alt_replay_on" : "True"},
                        meets = {'uv' : 'Кошкодевочка'},
                        func_in = prolog_interface_on, func_out = replay_screens_load
                      ),
            "normal",
            char_mask = 4
        ),
        sdl_achv_Achievement(    # Локи-Реджект
            "acm_logo_sl_7dl_loki_rej",
            "sl_7dl_loki_rej",
            "sdl_achv_sl_LO_rej",
            [],
            sdl_Replay("alt_day7_sl_7dl_loki_rej", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "dontlike",
            char_mask = 4
        ),
        sdl_achv_Achievement(    # Герк-Гуд
            "acm_logo_sl_7dl_herc_good",
            "sl_7dl_herc_good",
            "sdl_achv_sl_HE_good",
            [],
            sdl_Replay(
                        "alt_day7_sl_7dl_herc_good", {"alt_replay_on" : "True"},
                        meets = {'uv' : 'Кошкодевочка'},
                        func_in = prolog_interface_on, func_out = replay_screens_load
                      ),
            "happy",
            char_mask = 2
        ),
        sdl_achv_Achievement(    # Дрищ-Гуд
            "acm_logo_sl_7dl_dr_good",
            "sl_7dl_dr_good",
            "sdl_achv_sl_DR_good",
            [],
            sdl_Replay("alt_day7_sl_7dl_dr_good", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "smile",
            1
        ),
        sdl_achv_Achievement(    # Дрищ-Гуд 2
            "acm_logo_sl_7dl_dr_good2",
            "sl_7dl_dr_good2",
            "sdl_achv_sl_DR_good",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_sl_7dl_dr_good", "sl_7dl_dr_good", "sdl_achv_sl_DR_good", None, None)
                    }
                )
            ],
            sdl_Replay(
                        "alt_day7_sl_7dl_dr_good2", {"alt_replay_on" : "True"},
                        meets = {'uv' : 'Кошкодевочка'},
                        func_in = prolog_interface_on, func_out = replay_screens_load
                      ),
            "happy",
            1
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_sl_7dl_bad",
            "sl_7dl_bad",
            "sdl_achv_sl_bad",
            [],
            sdl_Replay(
                        "alt_day7_sl_7dl_bad", {"alt_replay_on" : "True"},
                        meets = {'uv' : 'Кошкодевочка'},
                        vars = [
                                    sdl_var_i_karma
                                ],
                        func_in = prolog_interface_on, func_out = replay_screens_load
                      ),
            "sad"
        )
    ]

    ## Славя-Классик
    sdl_achv_array_sl_clt = [
        sdl_achv_Achievement(    # Инт-ТруЪ
            "acm_logo_sl_cl_int_true",
            "sl_cl_int_true",
            "sdl_achv_sl_true_IN",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_sl_cl_good_ussr", "sl_cl_good_ussr", "sdl_achv_sl_good_US", None, None),
                        sdl_achv_Achievement("acm_logo_sl_cl_good_rf", "sl_cl_good_rf", "sdl_achv_sl_good_RF", None, None),
                        sdl_achv_Achievement("acm_logo_sl_cl_good_rf2", "sl_cl_good_rf2", "sdl_achv_sl_good_RF", None, None)
                    }
                )
            ],
            sdl_Replay("alt_day7_sl_cl_int_true", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            "sad"
        ),
        sdl_achv_Achievement(    # Инт-гуд
            "acm_logo_sl_cl_int_good",
            "sl_cl_int_good",
            "sdl_achv_sl_good_IN",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_sl_cl_good_ussr", "sl_cl_good_ussr", "sdl_achv_sl_good_US", None, None),
                        sdl_achv_Achievement("acm_logo_sl_cl_good_rf", "sl_cl_good_rf", "sdl_achv_sl_good_RF", None, None),
                        sdl_achv_Achievement("acm_logo_sl_cl_good_rf2", "sl_cl_good_rf2", "sdl_achv_sl_good_RF", None, None)
                    }
                )
            ],
            sdl_Replay("alt_day7_sl_cl_int_good", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            "smile"
        ),
        sdl_achv_Achievement(    # Инт-реджект
            "acm_logo_sl_cl_int_rej",
            "sl_cl_int_rej",
            "sdl_achv_sl_rej_IN",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_sl_cl_good_ussr", "sl_cl_good_ussr", "sdl_achv_sl_good_US", None, None),
                        sdl_achv_Achievement("acm_logo_sl_cl_good_rf", "sl_cl_good_rf", "sdl_achv_sl_good_RF", None, None),
                        sdl_achv_Achievement("acm_logo_sl_cl_good_rf2", "sl_cl_good_rf2", "sdl_achv_sl_good_RF", None, None)
                    }
                )
            ],
            sdl_Replay("alt_day7_sl_cl_int_rej", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "upset"
        ),
        sdl_achv_Achievement(    # СССР-гуд
            "acm_logo_sl_cl_good_ussr",
            "sl_cl_good_ussr",
            "sdl_achv_sl_good_US",
            [],
            sdl_Replay(
                        "alt_day7_sl_cl_good_ussr", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_e_d2_walk,
                                    sdl_var_e_d6_sl_cl_arc
                                ],
                        func_in = prolog_interface_on, func_out = replay_screens_load
                      ),
            "happy"
        ),
        sdl_achv_Achievement(    # РФ-гуд (Плюс-минус)
            "acm_logo_sl_cl_good_rf",
            "sl_cl_good_rf",
            "sdl_achv_sl_good_RF",
            [],
            sdl_Replay("alt_day7_sl_cl_good_rf", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "happy"
        ),
        sdl_achv_Achievement(    # РФ-гуд
            "acm_logo_sl_cl_good_rf2",
            "sl_cl_good_rf2",
            "sdl_achv_sl_good_RF",
            [],
            sdl_Replay("alt_day7_sl_cl_good_rf2", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "happy"
        ),
        sdl_achv_Achievement(    # Реджект-РФ
            "acm_logo_sl_cl_rej_rf",
            "sl_cl_rej_rf",
            "sdl_achv_sl_rej_RF",
            [],
            sdl_Replay("alt_day7_sl_cl_rej_rf", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "tender"
        ),
        sdl_achv_Achievement(    # Реджект-2
            "acm_logo_sl_cl_rej",
            "sl_cl_rej",
            "sdl_achv_sl_rej_RF",
            [],
            sdl_Replay(
                        "alt_day7_sl_cl_rej", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_mi_lpp,
                                    sdl_var_i_dv_lpp,
                                    sdl_var_i_un_lpp,
                                    sdl_var_i_us_lpp
                                ],
                        func_in = prolog_interface_on, func_out = replay_screens_load
                      ),
            "surprise"
        ),
        sdl_achv_Achievement(    # Эксклюзив-Локи
            "acm_logo_sl_cl_loki_exc",
            "sl_cl_loki_exc",
            "sdl_achv_sl_LO_exc",
            [],
            sdl_Replay(
                        "alt_day6_sl_cl_loki_exc", {"alt_replay_on" : "True"},
                        music = music_7dl["gonna_be_ok"],
                        ambience = ambience_camp_center_day,
                        vars = [
                                    sdl_var_b_d5_sl_cl_hent
                                ],
                        func_in = prolog_interface_on, func_out = replay_screens_load
                      ),
            "cry",
            char_mask = 4
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_sl_cl_bad",
            "sl_cl_bad",
            "sdl_achv_sl_bad",
            [],
            sdl_Replay("alt_day7_sl_cl_bad", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "sad"
        )
    ]

    ## Лена-7дл
    sdl_achv_array_un_7dl = [
        sdl_achv_Achievement(    # Осколок памяти
            "acm_logo_un_7dl_shard",
            "un_7dl_shard",
            "sdl_achv_un_shard",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_puz",
                    None,
                    conditions = {"alt_binder"}
                )
            ],
            sdl_Replay("alt_day7_un_7dl_shard", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            "sad",
            7,
            None,
            Show("sdl_achv_sprite", Dissolve(0.5), "ars", "laugh", "casual"),
            persistent.alt_binder
        ),
        sdl_achv_Achievement(    # Гуд-СССР
            "acm_logo_un_7dl_good_ussr",
            "un_7dl_good_ussr",
            "sdl_achv_un_good_US",
            [],
            sdl_Replay("alt_day7_un_7dl_good_ussr", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            "smile2"
        ),
        sdl_achv_Achievement(    # Гуд-РФ
            "acm_logo_un_7dl_good_rf",
            "un_7dl_good_rf",
            "sdl_achv_un_good_RF",
            [],
            sdl_Replay("alt_day7_un_7dl_good_rf", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            "smile2",
            7,
            sdl_Replay("alt_day7_un_7dl_good_rf_ps", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
        ),
        sdl_achv_Achievement(    # Реджект
            "acm_logo_un_7dl_rej",
            "un_7dl_rej",
            "sdl_achv_un_rej",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mt_7dl_good", "mt_7dl_good", "sdl_achv_mt_good", None, None)
                    }
                )
            ],
            sdl_Replay("alt_day7_un_7dl_rej", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "normal"
        ),
        sdl_achv_Achievement(    # Реджект2
            "acm_logo_un_7dl_rej2",
            "un_7dl_rej2",
            "sdl_achv_un_rej",
            [],
            sdl_Replay("alt_day7_un_7dl_rej2", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            "sad"
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_un_7dl_bad",
            "un_7dl_bad",
            "sdl_achv_un_bad",
            [],
            sdl_Replay(
                        "alt_day7_un_7dl_bad", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_i_karma
                                ],
                        func_in = night_interface_on, func_out = replay_screens_load
                      ),
            "sorrow"
        )
    ]

    ## Лена-ФЗ
    sdl_achv_array_un_fzd = [
        sdl_achv_Achievement(    # Инт-ТруЪ
            "acm_logo_un_fz_rr_true",
            "un_fz_rr_true",
            "sdl_achv_un_true_IN",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_un_fz_rr_good", "un_fz_rr_good", "sdl_achv_un_good_IN", None, None)
                    }
                )
            ],
            sdl_Replay("alt_day6_un_fz_rr_true", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            "cry_smile",
            char_mask = 2
        ),
        sdl_achv_Achievement(    # Инт-гуд
            "acm_logo_un_fz_rr_good",
            "un_fz_rr_good",
            "sdl_achv_un_good_IN",
            [],
            sdl_Replay("alt_day6_un_fz_rr_good", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            "smile",
            2,
            sdl_Replay("alt_day6_un_fz_rr_good_ps", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
        ),
        sdl_achv_Achievement(    # Инт-бэд
            "acm_logo_un_fz_rr_bad",
            "un_fz_rr_bad",
            "sdl_achv_un_bad_IN",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_un_fz_rr_good", "un_fz_rr_good", "sdl_achv_un_good_IN", None, None)
                    }
                )
            ],
            sdl_Replay("alt_day6_un_fz_rr_bad", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            "sad",
            char_mask = 2
        ),
        sdl_achv_Achievement(    # Хорошая-СССР.
            "acm_logo_un_fz_good",
            "un_fz_good",
            "sdl_achv_un_good_US",
            [],
            sdl_Replay("alt_day7_un_fz_good_end", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load), #суды
            "smile",
            char_mask = 2
        ),
        sdl_achv_Achievement(    # Нейтрал.
            "acm_logo_un_fz_neu",
            "un_fz_neu",
            "sdl_achv_un_neu",
            [],
            sdl_Replay("alt_day7_un_fz_neu_end", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load), #суды
            "serious",
            char_mask = 2
        ),
        sdl_achv_Achievement(    # Реджект.
            "acm_logo_un_fz_rj",
            "un_fz_rj",
            "sdl_achv_un_rej",
            [],
            sdl_Replay("alt_day7_un_fz_rj_end", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            "normal",
            char_mask = 2
        ),
        sdl_achv_Achievement(    # Плохая.
            "acm_logo_un_fz_bad",
            "un_fz_bad",
            "sdl_achv_un_bad",
            [],
            sdl_Replay("alt_day7_un_fz_bad_end", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            "cry",
            char_mask = 2
        ),
        sdl_achv_Achievement(    # Постскриптум Алисы.
            "acm_logo_un_fz_bad_post",
            "un_fz_bad_post",
            "sdl_achv_un_bad_POST",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_un_fz_bad", "un_fz_bad", "sdl_achv_un_bad", None, None)
                    }
                )
            ],
            sdl_Replay("alt_day7_un_fz_bad_end_postscriptum", {"alt_replay_on" : "True"}, func_in = night_interface_on, func_out = replay_screens_load),
            "sad",
            2,
            None,
            Show("sdl_achv_sprite", Dissolve(0.5), "dv", "smile", "casual")
        )
    ]

    ## Ольга-7дл
    sdl_achv_array_mt_7dl = [
        sdl_achv_Achievement(    # Осколок памяти
            "acm_logo_mt_7dl_shard",
            "mt_7dl_shard",
            "sdl_achv_mt_shard",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_puz",
                    None,
                    conditions = {"alt_binder"}
                )
            ],
            sdl_Replay("alt_day7_mt_7dl_shard", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load),
            "smile",
            7,
            None,
            Show("sdl_achv_sprite", Dissolve(0.5), "ars", "laugh", "casual"),
            persistent.alt_binder
        ),
        sdl_achv_Achievement(    # ТруЪ
            "acm_logo_mt_7dl_true",
            "mt_7dl_true",
            "sdl_achv_mt_true",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mt_7dl_good", "mt_7dl_good", "sdl_achv_mt_good", None, None)
                    }
                )
            ],
            sdl_Replay("alt_day7_mt_7dl_true", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            "normal"
        ),
        sdl_achv_Achievement(    # Гуд
            "acm_logo_mt_7dl_good",
            "mt_7dl_good",
            "sdl_achv_mt_good",
            [],
            sdl_Replay("alt_day7_mt_7dl_good", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            "grin",
            7,
            sdl_Replay("alt_day7_mt_7dl_good_ps", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
        ),
        sdl_achv_Achievement(    # Нейтрал
            "acm_logo_mt_7dl_neu",
            "mt_7dl_neu",
            "sdl_achv_mt_neu",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mt_7dl_good", "mt_7dl_good", "sdl_achv_mt_good", None, None)
                    }
                )
            ],
            sdl_Replay("alt_day7_mt_7dl_neu", {"alt_replay_on" : "True"}, func_in = day_interface_on, func_out = replay_screens_load),
            "normal"
        ),
        sdl_achv_Achievement(    # Бэд Герка
            "acm_logo_mt_7dl_herc_exc",
            "mt_7dl_herc_exc",
            "sdl_achv_mt_herc_exc",
            [],
            sdl_Replay("alt_day7_mt_7dl_herc_exc", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "sad",
            char_mask = 2
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_mt_7dl_bad",
            "mt_7dl_bad",
            "sdl_achv_mt_bad",
            [],
            sdl_Replay("alt_day7_mt_7dl_bad", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "sad"
        )
    ]

    ## Ульяна-7дл
    sdl_achv_array_us_7dl = [
        sdl_achv_Achievement(    # Осколок памяти
            "acm_logo_us_7dl_shard",
            "us_7dl_shard",
            "sdl_achv_us_shard",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_puz",
                    None,
                    conditions = {"alt_binder"}
                )
            ],
            sdl_Replay("alt_day7_us_7dl_shard", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "normal",
            7,
            None,
            Show("sdl_achv_sprite", Dissolve(0.5), "ars", "surp", "casual"),
            persistent.alt_binder
        ),
        sdl_achv_Achievement(    # ТруЪ
            "acm_logo_us_7dl_true",
            "us_7dl_true",
            "sdl_achv_us_true",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_us_7dl_px_good", "us_7dl_px_good", "sdl_achv_us_good", None, None)
                    }
                ),
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_us_7dl_tran_un", "us_7dl_tran_un", "sdl_achv_us_tran_un", None, None),
                        sdl_achv_Achievement("acm_logo_us_7dl_tran_mi", "us_7dl_tran_mi", "sdl_achv_us_tran_mi", None, None)
                    }
                )
            ],
            sdl_Replay("alt_day7_us_7dl_true", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "grin",
            5,
            None,
            Show("sdl_achv_sprite", Dissolve(0.5), "us", "grin", "grow_dress")
        ),
        sdl_achv_Achievement(    # ТруЪ-огоньки
            "acm_logo_us_7dl_px_true",
            "us_7dl_px_true",
            "sdl_achv_us_true_IN",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_us_7dl_px_good", "us_7dl_px_good", "sdl_achv_us_good", None, None)
                    }
                )
            ],
            sdl_Replay("alt_day7_us_7dl_px_true", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "sad",
            char_mask = 5
        ),
        sdl_achv_Achievement(    # Гуд
            "acm_logo_us_7dl_good",
            "us_7dl_good",
            "sdl_achv_us_good",
            [],
            sdl_Replay(
                        "alt_day7_us_7dl_good", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d2_us_esca
                                ],
                        func_in = prolog_interface_on, func_out = replay_screens_load
                      ),
            "laugh2",
            7,
            sdl_Replay("alt_day7_us_7dl_good_ps", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
        ),
        sdl_achv_Achievement(    # Гуд-огоньки
            "acm_logo_us_7dl_px_good",
            "us_7dl_px_good",
            "sdl_achv_us_good_IN",
            [],
            sdl_Replay(
                        "alt_day7_us_7dl_px_good", {"alt_replay_on" : "True"},
                        vars = [
                                    sdl_var_b_d6_us_7dl_px_sl_join
                                ],
                        func_in = prolog_interface_on, func_out = replay_screens_load
                      ),
            "laugh2",
            char_mask = 5
        ),
        sdl_achv_Achievement(    # Лена-энд
            "acm_logo_us_7dl_tran_un",
            "us_7dl_tran_un",
            "sdl_achv_us_tran_un",
            [],
            sdl_Replay("alt_day7_us_7dl_tran_un", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "dontlike",
            5,
            None,
            Show("sdl_achv_sprite", Dissolve(0.5), "un", "smile", "modern")
        ),
        sdl_achv_Achievement(    # Мику-энд
            "acm_logo_us_7dl_tran_mi",
            "us_7dl_tran_mi",
            "sdl_achv_us_tran_mi",
            [],
            sdl_Replay("alt_day7_us_7dl_tran_mi", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "dontlike",
            7,
            None,
            Show("sdl_achv_sprite", Dissolve(0.5), "mi", "smile", "casual")
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_us_7dl_bad",
            "us_7dl_bad",
            "sdl_achv_us_bad",
            [],
            sdl_Replay("alt_day7_us_7dl_bad", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "sad"
        )
    ]

    ## Семён-Одиночка
    sdl_achv_array_me_owl = [
        # sdl_achv_Achievement(    # Нейтрал Герка
            # "acm_logo_me_neu_herc_exc",
            # "me_neu_herc_exc",
            # "sdl_achv_me_herc_exc",
            # [],
            # sdl_Replay("alt_day7_me_neu_herc_exc", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            # "pi_normal"
        # ),
        # sdl_achv_Achievement(    # Нейтрал Локи
            # "acm_logo_me_neu_loki_exc",
            # "me_neu_loki_exc",
            # "sdl_achv_me_loki_exc",
            # [],
            # sdl_Replay("alt_day7_me_neu_loki_exc", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            # "pi_normal"
        # ),
        # sdl_achv_Achievement(    # Нейтрал Дрищ
            # "acm_logo_me_neu_dr_exc",
            # "me_neu_dr_exc",
            # "sdl_achv_me_dr_exc",
            # [],
            # sdl_Replay("alt_day7_me_neu_dr_exc", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            # "pi_normal"
        # ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_me_neu_bad",
            "me_neu_bad",
            "sdl_achv_me_bad",
            [],
            sdl_Replay("alt_day7_me_neu_bad", {"alt_replay_on" : "True"}, func_in = prolog_interface_on, func_out = replay_screens_load),
            "pi_normal"
        )
    ]

    ## Разное-Прочее
    sdl_achv_array_va_smt = [
        sdl_achv_Achievement(    # Проиграл
            "acm_logo_va_lost",
            "alt_lost",
            "sdl_achv_va_lost",
            [],
            None
        ),
        sdl_achv_Achievement(    # Ламповость
            "acm_logo_va_lamp",
            "alt_lamp",
            "sdl_achv_va_kat",
            [],
            sdl_Replay("alt_achv_catapult", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_achv_Achievement(    # Глубина
            "acm_logo_va_deep",
            "alt_deep",
            "sdl_achv_va_kat",
            [],
            sdl_Replay("alt_day3_dv_reunion", {"alt_replay_on" : "True"}, func_in = sunset_interface_on, func_out = replay_screens_load)
        ),
        sdl_achv_Achievement(    # QTE
            "acm_logo_va_qte",
            "alt_qte",
            "sdl_achv_va_qte",
            [],
            None
        ),
        sdl_achv_Achievement(    # QTE victim
            "acm_logo_va_victim",
            "alt_victim",
            "sdl_achv_va_victim",
            [],
            None
        ),
        sdl_achv_Achievement(    # пьяная, помятая
            "acm_logo_va_drunk",
            "alt_drunk",
            "sdl_achv_va_drunk",
            [],
            None
        )
    ]

    sdl_achv_hidden = [ # ачивки не отображаются до момента получения
        "alt_lost",
        "alt_lamp",
        "alt_deep",
        "alt_qte",
        "alt_victim",
        "alt_drunk"
                      ]

    # Руты
    ## Мику
    sdl_achv_route_mi_7dl = sdl_achv_Route("sdl_achv_mi_7dl", "sdl_achv_7dl_route", "sdl_achv_mi_7dl_active", "sdl_achv_mi_7dl_inactive", sdl_achv_array_mi_7dl, "mi",  "casual")
    sdl_achv_route_mi_djt = sdl_achv_Route("sdl_achv_mi_djt", "sdl_achv_xxx_route", "sdl_achv_mi_dj_active",  "sdl_achv_mi_dj_inactive",  sdl_achv_array_mi_djt, "mi",  "voca")
    ## Алиса
    sdl_achv_route_dv_7dl = sdl_achv_Route("sdl_achv_dv_7dl", "sdl_achv_7dl_route", "sdl_achv_dv_7dl_active", "sdl_achv_dv_7dl_inactive", sdl_achv_array_dv_7dl, "dv",  "sport")
    sdl_achv_route_dv_djt = sdl_achv_Route("sdl_achv_dv_djt", "sdl_achv_xxx_route", "sdl_achv_dv_dj_active",  "sdl_achv_dv_dj_inactive",  sdl_achv_array_dv_djt, "dv",  "casual")
    ## Славя
    sdl_achv_route_sl_7dl = sdl_achv_Route("sdl_achv_sl_7dl", "sdl_achv_7dl_route", "sdl_achv_sl_7dl_active", "sdl_achv_sl_7dl_inactive", sdl_achv_array_sl_7dl, "sl",  "casual")
    sdl_achv_route_sl_clt = sdl_achv_Route("sdl_achv_sl_clt", "sdl_achv_xxx_route", "sdl_achv_sl_cl_active",  "sdl_achv_sl_cl_inactive",  sdl_achv_array_sl_clt, "sl",  "pioneer")
    ## Лена
    sdl_achv_route_un_7dl = sdl_achv_Route("sdl_achv_un_7dl", "sdl_achv_7dl_route", "sdl_achv_un_7dl_active", "sdl_achv_un_7dl_inactive", sdl_achv_array_un_7dl, "un",  "modern")
    sdl_achv_route_un_fzd = sdl_achv_Route("sdl_achv_un_fzd", "sdl_achv_xxx_route", "sdl_achv_un_fz_active",  "sdl_achv_un_fz_inactive",  sdl_achv_array_un_fzd, "un",  "dress",      char_mask=2)
    ## Ольга
    sdl_achv_route_mt_7dl = sdl_achv_Route("sdl_achv_mt_7dl", "sdl_achv_7dl_route", "sdl_achv_mt_7dl_active", "sdl_achv_mt_7dl_inactive", sdl_achv_array_mt_7dl, "mt",  "sport")
    ## Ульяна
    sdl_achv_route_us_7dl = sdl_achv_Route("sdl_achv_us_7dl", "sdl_achv_7dl_route", "sdl_achv_us_7dl_active", "sdl_achv_us_7dl_inactive", sdl_achv_array_us_7dl, "us",  "dress")
    ## Семён
    sdl_achv_route_me_owl = sdl_achv_Route("sdl_achv_me_owl", "sdl_achv_xxx_route", "sdl_achv_me_ow_active",  "sdl_achv_me_ow_inactive",  sdl_achv_array_me_owl, "am",  "pioneer")
    ## Разное
    sdl_achv_route_va_smt = sdl_achv_Route("sdl_achv_va_smt", "sdl_achv_smt_route", "sdl_achv_va_sm_active",  "sdl_achv_va_sm_inactive",  sdl_achv_array_va_smt, None,  None)



    # Разделы
    sdl_achv_mi_routes = [
        sdl_achv_route_mi_7dl,
        sdl_achv_route_mi_djt
    ]
    sdl_achv_dv_routes = [
        sdl_achv_route_dv_7dl,
        sdl_achv_route_dv_djt
    ]
    sdl_achv_sl_routes = [
        sdl_achv_route_sl_7dl,
        sdl_achv_route_sl_clt
    ]
    sdl_achv_un_routes = [
        sdl_achv_route_un_7dl,
        sdl_achv_route_un_fzd
    ]
    sdl_achv_mt_routes = [
        sdl_achv_route_mt_7dl
    ]
    sdl_achv_us_routes = [
        sdl_achv_route_us_7dl
    ]
    sdl_achv_me_routes = [
        sdl_achv_route_me_owl
    ]
    sdl_achv_va_routes = [
        sdl_achv_route_va_smt
    ]

    sdl_achv_section_to_routes = {
        "mi": sdl_achv_mi_routes,
        "dv": sdl_achv_dv_routes,
        "sl": sdl_achv_sl_routes,
        "un": sdl_achv_un_routes,
        "mt": sdl_achv_mt_routes,
        "us": sdl_achv_us_routes,
        "me": sdl_achv_me_routes,
        "va": sdl_achv_va_routes
    }



    # Протагонисты
    sdl_achv_characters = [
        sdl_Character("sdl_achv_char_none", 15, None, None),
        sdl_Character("sdl_achv_char_loki", 4, "sdl_achv_char_label_loki", "loki"),
        sdl_Character("sdl_achv_char_herc", 2, "sdl_achv_char_label_herc", "herc"),
        sdl_Character("sdl_achv_char_dr",   1, "sdl_achv_char_label_dr",   "dr")
    ]

    # Требования для пазла-сердечка
    sdl_achv_puzzle_prereq = sdl_achv_Puzzle_prerequisites(
        [
            sdl_achv_Prerequisite(
                "sdl_achv_info_end",
                {
                    sdl_achv_Achievement("acm_logo_mi_dj_true", "mi_dj_true", "sdl_achv_mi_true", None, None)
                }
            ),
            sdl_achv_Prerequisite(
                "sdl_achv_info_end",
                {
                    sdl_achv_Achievement("acm_logo_dv_dj_true", "dv_dj_true", "sdl_achv_dv_true", None, None)
                }
            ),
            sdl_achv_Prerequisite(
                "sdl_achv_info_end",
                {
                    sdl_achv_Achievement("acm_logo_sl_cl_int_true", "sl_cl_int_true", "sdl_achv_sl_true_IN", None, None)
                }
            ),
            sdl_achv_Prerequisite(
                "sdl_achv_info_end",
                {
                    sdl_achv_Achievement("acm_logo_un_fz_rr_true", "un_fz_rr_true", "sdl_achv_un_true_IN", None, None)
                }
            ),
            sdl_achv_Prerequisite(
                "sdl_achv_info_end",
                {
                    sdl_achv_Achievement("acm_logo_mt_7dl_true", "mt_7dl_true", "sdl_achv_mt_true", None, None)
                }
            ),
            sdl_achv_Prerequisite(
                "sdl_achv_info_end",
                {
                    sdl_achv_Achievement("acm_logo_us_7dl_true", "us_7dl_true", "sdl_achv_us_true", None, None)
                }
            )
        ]
    )