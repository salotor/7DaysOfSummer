init:
    $ stories_mode_7dl = "" # Режимы раздела "Истории"

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
    $ alt_thoughts_tilde_update()
    $ reload_names()
    call alt_vars_saved

    if (not sdl_mus_engine.is_active) and ("breath_again" not in renpy.music.get_playing(channel="music")):
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
    $ alt_pos = 1
    textbutton "Фанфики по 7дл":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.235
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action ShowTransient("road_fanfics_7dl", transition=Dissolve(0.2))
    $ alt_pos += 1
    textbutton "Старые концовки":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.235
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        if persistent.alt_binder:
            action ShowTransient("old_ends_7dl", transition=Dissolve(0.2))
        else:
            action Show("alt_need_binder", transition=Dissolve(0.2))
    $ alt_pos += 1
    textbutton "Прочие сценарии":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.235
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
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
    $ alt_pos = 1
    textbutton "Кошкорут (Кошкотим)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day0_uvao_start") if persistent.pivo_default_7dl else Jump("alt_day0_uvao_start")]
    $ alt_pos += 1
    textbutton "Кровь на снегу (Н. Ильин)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("kns_start") if persistent.pivo_default_7dl else Jump("kns_start")]
    $ alt_pos += 1
    textbutton "Цвета (Г. Польши)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_colors_7dl") if persistent.pivo_default_7dl else Jump("alt_colors_7dl")]
    $ alt_pos += 1
    textbutton "Чудо новогоднее":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_chudo_novogodnee") if persistent.pivo_default_7dl else Jump("alt_chudo_novogodnee")]
    $ alt_pos += 1
    textbutton "Возрождение":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_chudesa_byvayut") if persistent.pivo_default_7dl else Jump("alt_chudesa_byvayut")]
    $ alt_pos += 1
    textbutton "Частичка души":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_bit_of_soul") if persistent.pivo_default_7dl else Jump("alt_bit_of_soul")]
    $ alt_pos += 1
    textbutton "Призрак унылой девочки":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("the_ghost_of_a_sad_girl") if persistent.pivo_default_7dl else Jump("the_ghost_of_a_sad_girl")]
    $ alt_pos += 1
    textbutton "Cтрашилки в библиотеке (Ф. Лопатин)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("fedor_scary_story") if persistent.pivo_default_7dl else Jump("fedor_scary_story")]
    $ alt_pos += 2
    textbutton "Лагерная страшилка (ranger)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("ranger_scary_story") if persistent.pivo_default_7dl else Jump("ranger_scary_story")]
    $ alt_pos += 2
    textbutton "Идеальное оружие (Славя-ведьма)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("ultimate_weapon_sl_vedma") if persistent.pivo_default_7dl else Jump("ultimate_weapon_sl_vedma")]
    $ alt_pos += 2

# Старые концовки
screen old_ends_7dl:
    tag list
    $ alt_pos = 1
    textbutton "Концовки Мику":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("old_ends_7dl", transition=Dissolve(0.2)), ShowTransient("old_ends_mi_7dl", transition=Dissolve(0.2))]
    $ alt_pos += 1
    textbutton "Старые послесловия":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("old_ends_7dl", transition=Dissolve(0.2)), ShowTransient("old_ends_ps_7dl", transition=Dissolve(0.2))]
    $ alt_pos += 1
    textbutton "Концовки Септима":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("old_ends_7dl", transition=Dissolve(0.2)), ShowTransient("old_ends_sept_7dl", transition=Dissolve(0.2))]

# Концовки Мику
screen old_ends_mi_7dl:
    tag list
    $ alt_pos = 1
    textbutton "Признан негодным":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day4_mi2sl_transit2") if persistent.pivo_default_7dl else Jump("alt_day4_mi2sl_transit2")]
    $ alt_pos += 1
    textbutton "Спасибо тебе (старая версия)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day7_mi_7dl_reject") if persistent.pivo_default_7dl else Jump("alt_day7_mi_7dl_reject")]
    $ alt_pos += 2
    textbutton "Искорка (старая версия)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day7_mi_7dl_sparkle") if persistent.pivo_default_7dl else Jump("alt_day7_mi_7dl_sparkle")]

# Старые послесловия
screen old_ends_ps_7dl:
    tag list
    $ alt_pos = 1
    textbutton "Послесловие Мику-дж":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day7_mi_dj_good_rf_ps_old") if persistent.pivo_default_7dl else Jump("alt_day7_mi_dj_good_rf_ps_old")]
    $ alt_pos += 1
    textbutton "Послесловие Алисы-7дл":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day7_dv_7dl_good_rf_ps_old") if persistent.pivo_default_7dl else Jump("alt_day7_dv_7dl_good_rf_ps_old")]
    $ alt_pos += 1
    textbutton "Послесловие Лены-7дл":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day7_un_7dl_good_rf_ps_old") if persistent.pivo_default_7dl else Jump("alt_day7_un_7dl_good_rf_ps_old")]

# Концовки Септима
screen old_ends_sept_7dl:
    tag list
    $ alt_pos = 1
    textbutton "Обязательно найду (Алиса)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day7_dv_7dl_sept") if persistent.pivo_default_7dl else Jump("alt_day7_dv_7dl_sept")]
    $ alt_pos += 1
    textbutton "Чудес не бывает (Славя)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day7_sl_7dl_sept") if persistent.pivo_default_7dl else Jump("alt_day7_sl_7dl_sept")]
    $ alt_pos += 1
    textbutton "Поиски продолжаются (Лена)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day7_un_7dl_sept") if persistent.pivo_default_7dl else Jump("alt_day7_un_7dl_sept")]
    $ alt_pos += 2
    textbutton "Отблеск лета (Ульяна)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day7_us_px_sept") if persistent.pivo_default_7dl else Jump("alt_day7_us_px_sept")]
    $ alt_pos += 1
    textbutton "Странные люди (Ольга)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day7_mt_7dl_sept") if persistent.pivo_default_7dl else Jump("alt_day7_mt_7dl_sept")]
    $ alt_pos += 1
    textbutton "Горькая правда (Мику)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day7_mi_7dl_sept") if persistent.pivo_default_7dl else Jump("alt_day7_mi_7dl_sept")]
    $ alt_pos += 1
    textbutton "Безликие руки (Одиночка)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day7_me_neu_sept") if persistent.pivo_default_7dl else Jump("alt_day7_me_neu_sept")]

# Прочее
screen unreleased_1_7dl:
    tag list
    imagebutton:
        auto get_image_7dl("gui/stories/repl/buttons/repl_arrow_right_%s.png") xcenter 0.749 ycenter 0.923
        activate_sound repl_page_turnings[str(random.choice([1, 2, 3, 4, 5]))]
        action [Hide("unreleased_1_7dl", transition=Dissolve(0.2)), ShowTransient("unreleased_2_7dl", transition=Dissolve(0.2))]
    $ alt_pos = 1
    textbutton "Демиург-Трио (2014 г.)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day4_start_neutral_ending") if persistent.pivo_default_7dl else Jump("alt_day4_start_neutral_ending")]
    $ alt_pos += 1
    textbutton "Загадочная дверка (Славя-кл)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day7_sl_cl_square1") if persistent.pivo_default_7dl else Jump("alt_day7_sl_cl_square1")]
    $ alt_pos += 2
    textbutton "ИИ Шурика (Славя-кл)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day7_sl_cl_ps") if persistent.pivo_default_7dl else Jump("alt_day7_sl_cl_ps")]
    $ alt_pos += 1
    textbutton "Телефон в старом лагере (Славя-7дл)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day4_sl_7dl_old_phone") if persistent.pivo_default_7dl else Jump("alt_day4_sl_7dl_old_phone")]
    $ alt_pos += 2
    textbutton "Вишенка (старый Лена-ФЗ)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_cherry_berry") if persistent.pivo_default_7dl else Jump("alt_cherry_berry")]
    $ alt_pos += 2
    textbutton "Бездна анального угнетения (старый д.6 Одиночки)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_uvao_hentai") if persistent.pivo_default_7dl else Jump("alt_uvao_hentai")]
    $ alt_pos += 2
    textbutton "Старые сцены кекса (Лена-7дл)":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day4_un_7dl_hentai_old") if persistent.pivo_default_7dl else Jump("alt_day4_un_7dl_hentai_old")]
    $ alt_pos += 2
    textbutton "Свидание с Мику на пляже":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day4_beach_night_mi") if persistent.pivo_default_7dl else Jump("alt_day4_beach_night_mi")]

screen unreleased_2_7dl:
    tag list
    imagebutton:
        auto get_image_7dl("gui/stories/repl/buttons/repl_arrow_left_%s.png") xcenter 0.554 ycenter 0.923
        activate_sound repl_page_turnings[str(random.choice([1, 2, 3, 4, 5]))]
        action [Hide("unreleased_2_7dl", transition=Dissolve(0.2)), ShowTransient("unreleased_1_7dl", transition=Dissolve(0.2))]
    imagebutton:
        auto get_image_7dl("gui/stories/repl/buttons/repl_arrow_right_%s.png") xcenter 0.749 ycenter 0.923
        activate_sound repl_page_turnings[str(random.choice([1, 2, 3, 4, 5]))]
        action [Hide("unreleased_2_7dl", transition=Dissolve(0.2)), ShowTransient("unreleased_3_7dl", transition=Dissolve(0.2))]
    $ alt_pos = 1
    textbutton "3-4 дни Лены-классик":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day3_un_cl_start") if persistent.pivo_default_7dl else Jump("alt_day3_un_cl_start")]
    $ alt_pos += 1
    textbutton "4-й день старой Лены-ФЗ":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day4_un_fz_start_old") if persistent.pivo_default_7dl else Jump("alt_day4_un_fz_start_old")]
    $ alt_pos += 1
    textbutton "4-й день Мику-классик":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day4_mi_cl_start") if persistent.pivo_default_7dl else Jump("alt_day4_mi_cl_start")]
    $ alt_pos += 1
    textbutton "Начало Алисы-классик":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day4_dv_cl_start") if persistent.pivo_default_7dl else Jump("alt_day4_dv_cl_start")]
    $ alt_pos += 1
    textbutton "Начало Слави-ведьмы":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day4_sl_wh_start") if persistent.pivo_default_7dl else Jump("alt_day4_sl_wh_start")]

screen unreleased_3_7dl:
    tag list
    imagebutton:
        auto get_image_7dl("gui/stories/repl/buttons/repl_arrow_left_%s.png") xcenter 0.554 ycenter 0.923
        activate_sound repl_page_turnings[str(random.choice([1, 2, 3, 4, 5]))]
        action [Hide("unreleased_3_7dl", transition=Dissolve(0.2)), ShowTransient("unreleased_2_7dl", transition=Dissolve(0.2))]
    $ alt_pos = 1
    textbutton "Старый 6 день Сыча":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day6_me_neu_start_old") if persistent.pivo_default_7dl else Jump("alt_day6_me_neu_start_old")]
    $ alt_pos += 1
    textbutton "Старый 7 день Сыча":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day7_me_neu_start_old") if persistent.pivo_default_7dl else Jump("alt_day7_me_neu_start_old")]
    $ alt_pos += 1
    textbutton "Первый пролог Септима":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_septim_prologue_old") if persistent.pivo_default_7dl else Jump("alt_septim_prologue_old")]
    $ alt_pos += 1
    textbutton "Второй пролог Септима":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_septim_prologue") if persistent.pivo_default_7dl else Jump("alt_septim_prologue")]
    $ alt_pos += 1
    textbutton "Начало рута Септима":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day1_me_d3_start") if persistent.pivo_default_7dl else Jump("alt_day1_me_d3_start")]
    $ alt_pos += 1
    textbutton "4-й день Нуара":
        style "log_button"
        text_style "old_road_textbutton"
        xpos 0.534
        ypos 0.138+0.0485*alt_pos
        xmaximum 0.25
        action [Hide("stories_main_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=1), SetField(sdl_mus_engine, "is_active", False), Start("alt_day4_no_start") if persistent.pivo_default_7dl else Jump("alt_day4_no_start")]

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
