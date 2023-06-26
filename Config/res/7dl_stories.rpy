init:
    $ stories_mode_7dl = "" # Режимы раздела "Истории"
    $ sdl_repl_progress = 0 # Прогресс в %

init 999 python:
    style.old_road_textbutton = Style(style.replays_textbutton)
    style.old_road_textbutton.xmaximum = 500

# Отсюда запускаются "Истории"
label alt_stories_start:
    stop ambience
    stop sound
    stop sound_loop

    $ plthr = u"Меню"
    call alt_vars
    $ day_time()
    $ make_names_known_7dl()

    window auto
    if not persistent.thoughts_tilde_7dl:
        $ th_prefix = "«"
        $ th_suffix = "»"
    $ reload_names()
    call alt_vars_saved

    if not sdl_mus_engine.is_active:
        play music music_7dl["breath_again"] fadein 3
    scene bg gallery_7dl with fade
    if stories_mode_7dl == "":
        $ stories_mode_7dl = "moments"
    $ renpy.block_rollback()

    $ sdl_repl_progress_calc()

    call screen stories_main_7dl

# Фон и интерфейс
screen stories_main_7dl:
    timer 0.01 action ShowTransient("stories_exit_7dl", transition=Dissolve(0.2))
    if not stories_mode_7dl == "moments":
        imagebutton:
            auto get_image_7dl("gui/stories/stories_navig_moments_%s.png") xcenter 504 ycenter 50
            action [SetVariable("stories_mode_7dl", "moments"), Hide("stories_main_7dl", transition=Dissolve(0.2)), Jump("alt_stories_start")]
    else:
        add get_image_7dl("gui/stories/stories_navig_moments_hover.png") xcenter 504 ycenter 50
    if not stories_mode_7dl == "road":
        imagebutton:
            auto get_image_7dl("gui/stories/stories_navig_road_%s.png") xcenter 1422 ycenter 50
            action [SetVariable("stories_mode_7dl", "road"), Hide("stories_main_7dl", transition=Dissolve(0.2)), Jump("alt_stories_start")]
    else:
        add get_image_7dl("gui/stories/stories_navig_road_hover.png") xcenter 1422 ycenter 50
    if stories_mode_7dl == "moments":
        timer 0.01 action [Hide("road_main_7dl", transition=Dissolve(0.2)), ShowTransient("sdl_replays_main", engine=sdl_repl_engine, transition=Dissolve(0.2))]
    if stories_mode_7dl == "road":
        timer 0.01 action [Hide("sdl_replays_main", transition=Dissolve(0.2)), ShowTransient("road_main_7dl", transition=Dissolve(0.2))]

    # Панелька плеера
    if sdl_mus_engine.is_active:
        use music_panel_7dl(default_music=music_7dl["breath_again"])

screen stories_exit_7dl:
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xcenter 131 ycenter 994
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), SetVariable("stories_mode_7dl", ""), Jump("main_menu_7dl")]

# Подраздел "Лес Памяти" находится в отдельных файлах 7dl_replays_%s.rpy"

# Подраздел "Старая Дорога"
screen road_main_7dl:
    tag menu
    add "bg repl_screen_7dl" xcenter 0.503 ycenter 0.532
    timer 0.01 action ShowTransient("road_main_info_7dl", transition=Dissolve(0.2))
    textbutton "Фанфики по 7дл":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.235
        ypos 0.187
        action ShowTransient("road_fanfics_7dl", transition=Dissolve(0.2))
    textbutton "Старые концовки":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.235
        ypos 0.236
        if persistent.alt_binder:
            action ShowTransient("old_ends_7dl", transition=Dissolve(0.2))
        else:
            action Show("alt_need_binder", transition=Dissolve(0.2))
    textbutton "Прочие сценарии":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.235
        ypos 0.285
        if persistent.alt_binder:
            action ShowTransient("unreleased_1_7dl", transition=Dissolve(0.2))
        else:
            action Show("alt_need_binder", transition=Dissolve(0.2))

# Инфо по "Старой Дороге"
screen road_main_info_7dl:
    tag list
    text "В разделе «Старая Дорога» представлены неканоничные сценарии для модификации. Они были либо созданы для устаревших концепций, либо изначально создавались без учёта канона.":
        style "old_road_textbutton"
        xpos 0.534
        ypos 0.187

# Фанфики по 7дл
screen road_fanfics_7dl:
    tag list
    textbutton "Кровь на снегу (Н. Ильин)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.187
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("kns_start")]
    textbutton "Кошкорут (Кошкотим)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.236
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day0_uvao_start")]
    textbutton "Цвета (Г. Польши)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.285
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_colors_7dl")]
    textbutton "Чудо новогоднее":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.333
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_chudo_novogodnee")]
    textbutton "Возрождение":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.382
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_chudesa_byvayut")]
    textbutton "Частичка души":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.431
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_bit_of_soul")]
    textbutton "Призрак унылой девочки":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.480
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("the_ghost_of_a_sad_girl")]
    textbutton "Cтрашилки в библиотеке \n(Федор Лопатин)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.529
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("fedor_scary_story")]
    textbutton "Лагерная страшилка \n(ranger)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.627
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("ranger_scary_story")]

# Старые концовки
screen old_ends_7dl:
    tag list
    textbutton "Концовки Септима":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.187
        action [Hide("old_ends_7dl", transition=Dissolve(0.2)), ShowTransient("old_ends_sept_7dl", transition=Dissolve(0.2))]
    textbutton "Концовки Мику":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.236
        action [Hide("old_ends_7dl", transition=Dissolve(0.2)), ShowTransient("old_ends_mi_7dl", transition=Dissolve(0.2))]
    textbutton "Старые послесловия":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.285
        action [Hide("old_ends_7dl", transition=Dissolve(0.2)), ShowTransient("old_ends_ps_7dl", transition=Dissolve(0.2))]

# Концовки Септима
screen old_ends_sept_7dl:
    tag list
    textbutton "Обязательно найду (Алиса)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.187
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day7_dv_7dl_sept")]
    textbutton "Чудес не бывает (Славя)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.236
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day7_sl_7dl_sept")]
    textbutton "Поиски продолжаются (Лена)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.285
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day7_un_7dl_sept")]
    textbutton "Отблеск лета (Ульяна)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.334
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day7_us_px_sept")]
    textbutton "Странные люди (Ольга)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.383
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day7_mt_7dl_sept")]
    textbutton "Горькая правда (Мику)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.431
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day7_mi_7dl_sept")]
    textbutton "Безликие руки (Одиночка)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.479
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day7_me_neu_sept")]

# Концовки Мику
screen old_ends_mi_7dl:
    tag list
    textbutton "Рикошет":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.187
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_ricochet")]
    textbutton "Признан негодным":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.236
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day4_mi2sl_transit2")]
    textbutton "Спасибо тебе (старая вер.)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.285
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day7_mi_7dl_reject")]
    textbutton "Искорка (старая версия)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.333
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day7_mi_7dl_sparkle")]

# Старые послесловия
screen old_ends_ps_7dl:
    tag list
    textbutton "Лена-7дл":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.187
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day7_un_7dl_good_rf_ps_old")]
    textbutton "Мику-диджей":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.236
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day7_mi_dj_good_rf_ps_old")]
    textbutton "Алиса-7дл":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.285
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day7_dv_7dl_good_rf_ps_old")]

# Прочее
screen unreleased_1_7dl:
    tag list
    imagebutton:
        auto get_image_7dl("gui/stories/repl/buttons/repl_arrow_right_%s.png") xcenter 0.749 ycenter 0.923
        activate_sound repl_page_turnings[str(random.choice([1, 2, 3, 4, 5]))]
        action [Hide("unreleased_1_7dl", transition=Dissolve(0.2)), ShowTransient("unreleased_2_7dl", transition=Dissolve(0.2))]
    textbutton "Старый Демиург-Трио":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.187
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day4_start_neutral_ending")]
    textbutton "Вишенка":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.236
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_cherry_berry")]
    textbutton "Бездна анального угнетения":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.285
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_uvao_hentai")]
    textbutton "Свидание на пляже":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.333
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day4_beach_night_mi")]
    textbutton "Начало Алисы-классик":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.382
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day4_dv_cl_start")]
    textbutton "Начало Слави-ведьмы":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.431
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day4_sl_wh_start")]
    textbutton "3-й день Лены-классик":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.479
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day3_un_cl_start")]
    textbutton "Старый рут Лены-ФЗ":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.528
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day4_un_fz_start_old")]
    textbutton "4-й день Мику-классик":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.577
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day4_mi_cl_start")]
    textbutton "Первый пролог Септима":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.626
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_septim_prologue_old")]
    textbutton "Пролог Септима":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.675
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_septim_prologue")]
    textbutton "Начало рута Септима":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.724
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day1_me_d3_start")]
    textbutton "4-й день Нуара":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.773
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day4_no_start")]

screen unreleased_2_7dl:
    tag list
    imagebutton:
        auto get_image_7dl("gui/stories/repl/buttons/repl_arrow_left_%s.png") xcenter 0.554 ycenter 0.923
        activate_sound repl_page_turnings[str(random.choice([1, 2, 3, 4, 5]))]
        action [Hide("unreleased_2_7dl", transition=Dissolve(0.2)), ShowTransient("unreleased_1_7dl", transition=Dissolve(0.2))]
    textbutton "Загадочная дверка":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.187
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day7_sl_cl_square1")]
    textbutton "Старый 6 день Сыча":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.236
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day6_me_neu_start_old")]
    textbutton "Старый 7 день Сыча":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.285
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day7_me_neu_start_old")]
    textbutton "Старые сцены кекса из\n   Лены-7дл":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.333
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day4_un_7dl_hentai_old")]
    textbutton "Телефон в старом лагере":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.431
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Jump("alt_day4_sl_7dl_old_phone")]

screen alt_need_binder:
    modal True
    add get_image("gui/o_rly/base.png")
    text "Для доступа в этот подраздел нужно собрать пазл-сердечко":
        text_align 0.5
        yalign 0.46
        xalign 0.5
        xmaximum 880
        color "#64483c"
        font header_font
        size 40
    textbutton _("OK"):
        text_size 60
        style "log_button"
        text_style "settings_link"
        yalign 0.6
        xalign 0.5
        action Hide("alt_need_binder")
