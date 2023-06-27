##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ФУНКЦИИ И КЛАССЫ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
init 2:
    $ sdl_achv_engine = None

init python:
    # Сброс перзистентов
    def sdl_achv_clear_persistents_ask(achv_arr):
        layout.yesno_screen(
            "Сбросить полученные концовки в этом руте?",
            yes = [Function(sdl_achv_clear_persistents, achv_arr), Function(sdl_achv_progress_calc), Play("sound", sdl_achv_clear)],
            no  = NullAction()
            )

    def sdl_achv_clear_persistents(achv_arr):
        for achv in achv_arr:
            setattr(persistent, achv.get_persistent(), False)
        alt_binder_update()
        return

    # Калькулятор прогресса
    def sdl_achv_progress_calc():
        global sdl_achv_progress
        seen_count = 0.0
        label_count = 0.0
        for ch, char in sdl_achv_section_to_routes.items():
            if ch != "va":
                for route in char:
                    for achieve in route.achv_arr:
                        if getattr(persistent, achieve.persistent):
                            seen_count += 1
                        label_count += 1
        ratio = seen_count / label_count * 100
        sdl_achv_progress = round(ratio, 1)

    # Das ist OOP!

    # Основной класс
    class sdl_achv_Engine:
        def __init__(self, default_route):
            self.hovered_route = None
            self.hovered_achv = None
            self.hovered_icon = None
            self.default_route = default_route
            self.available_chars = []

            self.cur_section = None
            self.cur_route = default_route
            self.cur_prerequisites = None
            self.cur_char_idx = 0

        def set_hovered_route(self, route):
            self.hovered_route = route

        def set_hovered_achv(self, achv):
            self.hovered_achv = achv

        def set_hovered_icon(self, icon):
            self.hovered_icon = icon

        def set_cur_section(self, section):
            self.cur_section = section
            self.reset_vars()

        def set_cur_route(self, route):
            self.cur_route = route
            self.check_available_chars()

        def set_cur_prerequisites(self, prerequisites):
            self.cur_prerequisites = prerequisites

        def cur_char_idx_inc(self):
            self.cur_char_idx += 1

        def cur_char_idx_dec(self):
            self.cur_char_idx -= 1

        def get_hovered_route(self):
            return self.hovered_route

        def get_hovered_achv(self):
            return self.hovered_achv

        def get_hovered_icon(self):
            return self.hovered_icon

        def get_cur_section(self):
            return self.cur_section

        def get_cur_route(self):
            return self.cur_route

        def get_cur_prerequisites(self):
            return self.cur_prerequisites

        def get_cur_char_idx(self):
            return self.cur_char_idx

        def get_chars_amount(self):
            return len(self.available_chars)

        def get_cur_char(self):
            return self.available_chars[self.cur_char_idx]

        def reset_vars(self):
            self.hovered_route = None
            self.hovered_achv = None
            self.hovered_icon = None
            self.cur_prerequisites = None
            self.run_func_out()
            self.cur_route = self.default_route
            self.cur_char_idx = 0
            self.available_chars = []
            return

        def check_available_chars(self):
            self.cur_char_idx = 0
            self.available_chars = []
            for char in sdl_achv_characters:
                if self.cur_route.check_mask(char.get_char_mask()):
                    self.available_chars.append(char)
            return

        def run_func_in(self):
            if self.cur_route.get_func_in() != None:
                self.cur_route.get_func_in()()
            return

        def run_func_out(self):
            if self.cur_route != None and self.cur_route.get_func_out() != None:
                self.cur_route.get_func_out()()
            return

    # Интерфейс рута
    class sdl_achv_Interface:
        def __init__(self, screen, section_buttons, del_button, ext_button):
            self.screen = screen
            self.section_buttons = section_buttons
            self.del_button = del_button
            self.ext_button = ext_button

        def get_screen(self):
            return self.screen

        def get_section_buttons(self):
            return self.section_buttons

        def get_del_button(self):
            return self.del_button

        def get_ext_button(self):
            return self.ext_button

    ## Дефолтный интерфейс
    sdl_achv_interface_default = sdl_achv_Interface(
        "sdl_achv_screen_main",
        {
            "mi_active"  : "sdl_achv_mi_button_active",
            "mi_inactive": "sdl_achv_mi_button_inactive",
            "dv_active"  : "sdl_achv_dv_button_active",
            "dv_inactive": "sdl_achv_dv_button_inactive",
            "sl_active"  : "sdl_achv_sl_button_active",
            "sl_inactive": "sdl_achv_sl_button_inactive",
            "un_active"  : "sdl_achv_un_button_active",
            "un_inactive": "sdl_achv_un_button_inactive",
            "mt_active"  : "sdl_achv_mt_button_active",
            "mt_inactive": "sdl_achv_mt_button_inactive",
            "us_active"  : "sdl_achv_us_button_active",
            "us_inactive": "sdl_achv_us_button_inactive",
            "me_active"  : "sdl_achv_me_button_active",
            "me_inactive": "sdl_achv_me_button_inactive",
            "va_active"  : "sdl_achv_va_button_active",
            "va_inactive": "sdl_achv_va_button_inactive"
        },
        "sdl_achv_del_active",
        "sdl_achv_ext_active"
    )

    # Рут
    class sdl_achv_Route:
        def __init__(self, title, typology, icon_active, icon_inactive, achv_arr, sprite_who, sprite_clothes, char_mask=7, interface=sdl_achv_interface_default, func_in=None, func_out=None, status="completed"):
            self.title = title
            self.typology = typology
            self.icon_active = icon_active
            self.icon_inactive = icon_inactive
            self.achv_arr = achv_arr
            self.sprite_who = sprite_who
            self.sprite_clothes = sprite_clothes
            self.char_mask = char_mask
            self.interface = interface
            self.func_in = func_in
            self.func_out = func_out
            self.status = status

        def get_title(self):
            return self.title

        def get_typology(self):
            return self.typology

        def get_icon_active(self):
            return self.icon_active

        def get_icon_inactive(self):
            return self.icon_inactive

        def get_achv_arr(self):
            return self.achv_arr

        def get_sprite_who(self):
            return self.sprite_who

        def get_sprite_clothes(self):
            return self.sprite_clothes

        def check_mask(self, char_mask):
            return self.char_mask & char_mask

        def get_interface(self):
            return self.interface

        def get_func_in(self):
            return self.func_in

        def get_func_out(self):
            return self.func_out

        def get_status(self):
            return self.status

    ## Заглушка (дефолтный рут)
    sdl_achv_route_default = sdl_achv_Route(None, None, None, None, [], None, None)

    # Ачивка
    class sdl_achv_Achievement:
        def __init__(self, icon, persistent, text, prerequisites, replay, sprite_emo=None, char_mask=7, postscriptum=None, override=None, if_override=None):
            self.icon = icon
            self.persistent = persistent
            self.text = text
            self.prerequisites = prerequisites
            self.replay = replay
            self.sprite_emo = sprite_emo
            self.char_mask = char_mask
            self.postscriptum = postscriptum
            self.override = override
            self.if_override = if_override

        def get_icon(self):
            return self.icon

        def get_persistent(self):
            return self.persistent

        def get_text(self):
            return self.text

        def get_prerequisites(self):
            return self.prerequisites

        def get_replay(self):
            return self.replay

        def get_sprite_emo(self):
            return self.sprite_emo

        def check_mask(self, char_mask):
            return self.char_mask & char_mask

        def get_postscriptum(self):
            return self.postscriptum

        def get_override(self):
            return self.override

        def check_override(self):
            return self.if_override

    # Требование к ачивке
    class sdl_achv_Prerequisite:
        def __init__(self, text, achievements, conditions=None):
            self.text = text
            self.achievements = achievements
            self.conditions = conditions

        def check_conditions(self):
            if self.achievements:
                for achv in self.achievements:
                    if getattr(persistent, achv.get_persistent()):
                        return True
            if self.conditions:
                for cond in self.conditions:
                    if getattr(persistent, cond):
                        return True
            return False

        def get_text(self):
            return self.text

        def get_achievements(self):
            return self.achievements

    # Требование к пазлу
    class sdl_achv_Puzzle_prerequisites:
        def __init__(self, cur_prerequisites):
            self.cur_prerequisites = cur_prerequisites
        def get_cur_prerequisites(self):
            return self.cur_prerequisites

##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ЭКРАНЫ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Начальный экран
screen sdl_achvlist_main(engine):
    tag menu
    layer "transient"

    add engine.get_cur_route().get_interface().get_screen()

    # Дефолтный спрайт персонажа
    if engine.get_cur_route() == sdl_achv_route_default:
        if engine.get_cur_section() == "me":
            use sdl_achv_sprite("am", "pi_smile", "pioneer")
        elif engine.get_cur_section() != "va":
            use sdl_achv_sprite(engine.get_cur_section(), "smile", "pioneer")

    on "show" action Show("sdl_achv_section_selector", engine=engine)
    on "hide" action [Hide("sdl_achv_section_selector"), Hide("sdl_achv_sprite")]
# ------------------------------------------------------------------------------------------------
# Экран выбора раздела
screen sdl_achv_section_selector(engine):
    tag section_selector

    # Мику
    if engine.get_cur_section() == "mi":
        add engine.get_cur_route().get_interface().get_section_buttons()['mi_active'] pos (0, 0)
    else:
        imagebutton pos (0, 0):
            focus_mask True
            hover_sound sdl_achv_pagina
            idle (engine.get_cur_route().get_interface().get_section_buttons()['mi_inactive'])
            hover (engine.get_cur_route().get_interface().get_section_buttons()['mi_active'])
            action [Hide("sdl_achvlist_main", transition=Dissolve(0.5)), Call("sdl_achvlist_section", engine, "mi")]
    # Алисхен
    if engine.get_cur_section() == "dv":
        add engine.get_cur_route().get_interface().get_section_buttons()['dv_active'] pos (0, 270)
    else:
        imagebutton pos (0, 270):
            focus_mask True
            hover_sound sdl_achv_pagina
            idle (engine.get_cur_route().get_interface().get_section_buttons()['dv_inactive'])
            hover (engine.get_cur_route().get_interface().get_section_buttons()['dv_active'])
            sensitive not sdl_mus_engine.is_panel_open
            action [Hide("sdl_achvlist_main", transition=Dissolve(0.5)), Call("sdl_achvlist_section", engine, "dv")]
    # Славя
    if engine.get_cur_section() == "sl":
        add engine.get_cur_route().get_interface().get_section_buttons()['sl_active'] pos (0, 540)
    else:
        imagebutton pos (0, 540):
            focus_mask True
            hover_sound sdl_achv_pagina
            idle (engine.get_cur_route().get_interface().get_section_buttons()['sl_inactive'])
            hover (engine.get_cur_route().get_interface().get_section_buttons()['sl_active'])
            sensitive not sdl_mus_engine.is_panel_open
            action [Hide("sdl_achvlist_main", transition=Dissolve(0.5)), Call("sdl_achvlist_section", engine, "sl")]
    # Лена
    if engine.get_cur_section() == "un":
        add engine.get_cur_route().get_interface().get_section_buttons()['un_active'] pos (0, 810)
    else:
        imagebutton pos (0, 810):
            focus_mask True
            hover_sound sdl_achv_pagina
            idle (engine.get_cur_route().get_interface().get_section_buttons()['un_inactive'])
            hover (engine.get_cur_route().get_interface().get_section_buttons()['un_active'])
            action [Hide("sdl_achvlist_main", transition=Dissolve(0.5)), Call("sdl_achvlist_section", engine, "un")]
    # Ольга
    if engine.get_cur_section() == "mt":
        add engine.get_cur_route().get_interface().get_section_buttons()['mt_active'] pos (1480, 0)
    else:
        imagebutton pos (1480, 0):
            focus_mask True
            hover_sound sdl_achv_pagina
            idle (engine.get_cur_route().get_interface().get_section_buttons()['mt_inactive'])
            hover (engine.get_cur_route().get_interface().get_section_buttons()['mt_active'])
            action [Hide("sdl_achvlist_main", transition=Dissolve(0.5)), Call("sdl_achvlist_section", engine, "mt")]
    # Ульяна
    if engine.get_cur_section() == "us":
        add engine.get_cur_route().get_interface().get_section_buttons()['us_active'] pos (1576, 270)
    else:
        imagebutton pos (1576, 270):
            focus_mask True
            hover_sound sdl_achv_pagina
            idle (engine.get_cur_route().get_interface().get_section_buttons()['us_inactive'])
            hover (engine.get_cur_route().get_interface().get_section_buttons()['us_active'])
            action [Hide("sdl_achvlist_main", transition=Dissolve(0.5)), Call("sdl_achvlist_section", engine, "us")]
    # Одиночка
    if engine.get_cur_section() == "me":
        add engine.get_cur_route().get_interface().get_section_buttons()['me_active'] pos (1576, 540)
    else:
        imagebutton pos (1576, 540):
            focus_mask True
            hover_sound sdl_achv_pagina
            idle (engine.get_cur_route().get_interface().get_section_buttons()['me_inactive'])
            hover (engine.get_cur_route().get_interface().get_section_buttons()['me_active'])
            action [Hide("sdl_achvlist_main", transition=Dissolve(0.5)), Call("sdl_achvlist_section", engine, "me")]
    # Разное
    if engine.get_cur_section() == "va":
        add engine.get_cur_route().get_interface().get_section_buttons()['va_active'] pos (1480, 810)
    else:
        imagebutton pos (1480, 810):
            focus_mask True
            hover_sound sdl_achv_pagina
            idle (engine.get_cur_route().get_interface().get_section_buttons()['va_inactive'])
            hover (engine.get_cur_route().get_interface().get_section_buttons()['va_active'])
            action [Hide("sdl_achvlist_main", transition=Dissolve(0.5)), Call("sdl_achvlist_section", engine, "va")]

    # Выбранная секция
    if engine.get_cur_section() != None:
        use sdl_achvlist_section(engine)

    # Выход
    imagebutton xcenter 1325 ycenter 70:
        hover_sound sdl_achv_click
        idle ("sdl_achv_ext_inactive")
        hover (engine.get_cur_route().get_interface().get_ext_button())
        hovered [Function(engine.set_hovered_icon, "sdl_achv_ext")]
        unhovered [Function(engine.set_hovered_icon, None)]
        action [Stop("ambience"), Function(engine.run_func_out), Hide("sdl_achvlist_main", transition=Dissolve(0.5)), Jump("main_menu_7dl")]

    # Всплывающая инфа
    if engine.get_hovered_icon() != None:
        add engine.get_hovered_icon() xcenter 440 ycenter 675

    # Панелька плеера
    if sdl_mus_engine.is_active:
        use music_panel_7dl(default_music=music_7dl["ambience_safe"])

    # Инфа по прогрессу
    if engine.get_cur_route().get_title() == None:
        text "Открыто\nконцовок: [sdl_achv_progress]%":
            style "sdl_achv_font_small_inactive"
            xcenter 795
            ycenter 1010

    # Пазл-сердечко
        imagebutton xcenter 595 ycenter 1010:
            focus_mask True
            idle "sdl_achv_puzzle"
            hovered SetVariable("sdl_achv_show_puzzle_prereq", True)
            unhovered SetVariable("sdl_achv_show_puzzle_prereq", False)
            action SetVariable("sdl_achv_show_puzzle_prereq", True)

    if sdl_achv_show_puzzle_prereq and (not persistent.alt_binder):
        use sdl_achv_prerequisites(sdl_achv_puzzle_prereq)

# ------------------------------------------------------------------------------------------------
# Экран раздела
screen sdl_achvlist_section(engine):
    tag section

    # Руты
    $ sdl_route_count = 0
    for route in sdl_achv_section_to_routes[engine.get_cur_section()]:
        if sdl_route_count == 3 and len(sdl_achv_section_to_routes[engine.get_cur_section()]) == 4:    # для красивого отображения 4 значков
            $ sdl_achv_x_shift = 1
            $ sdl_achv_y_shift = sdl_route_count // 3
        else:
            $ sdl_achv_x_shift = sdl_route_count % 3
            $ sdl_achv_y_shift = sdl_route_count // 3
        if engine.get_cur_route() == route:
            add route.get_icon_active() xcenter (1091 + 117 * sdl_achv_x_shift) ycenter (165 + 69 * sdl_achv_y_shift)
        else:
            imagebutton xcenter (1091 + 117 * sdl_achv_x_shift) ycenter (165 + 69 * sdl_achv_y_shift):
                hover_sound sdl_achv_click
                idle (route.get_icon_inactive())
                hover (route.get_icon_active())
                hovered [Function(engine.set_hovered_route, route)]
                unhovered [Function(engine.set_hovered_route, None)]
                action [Function(engine.set_hovered_route, None), Function(engine.run_func_out), Function(engine.set_cur_route, route), Function(engine.run_func_in), Show("sdl_achv_sprite", Dissolve(0.5), route.get_sprite_who(), "pi_smile" if route == sdl_achv_route_me_owl else "smile", route.get_sprite_clothes())]
        $ sdl_route_count += 1

    # Всплывающая инфа
    if engine.get_hovered_route() != None:
        add engine.get_hovered_route().get_typology() xcenter 440 ycenter 405
        add engine.get_hovered_route().get_title() xcenter 960 ycenter 70
        if engine.get_hovered_route().get_status() == "incompleted":
            add "sdl_achv_need_route" xcenter 440 ycenter 675
    elif engine.get_cur_route() != sdl_achv_route_default:
        add engine.get_cur_route().get_typology() xcenter 440 ycenter 405
        add engine.get_cur_route().get_title() xcenter 960 ycenter 70
        if (engine.get_cur_route().get_status() == "incompleted") and (engine.get_hovered_icon() == None):
            add "sdl_achv_need_route" xcenter 440 ycenter 675

    # Выбранный рут
    if engine.get_cur_route() != sdl_achv_route_default:
        use sdl_achv_route(engine)
# ------------------------------------------------------------------------------------------------
# Экран рута
screen sdl_achv_route(engine):
    tag route

    # Удалятор
    imagebutton xcenter 595 ycenter 70:
        hover_sound sdl_achv_click
        idle ("sdl_achv_del_inactive")
        hover (engine.get_cur_route().get_interface().get_del_button())
        hovered [Function(engine.set_hovered_icon, "sdl_achv_del")]
        unhovered [Function(engine.set_hovered_icon, None)]
        action [Function(engine.set_hovered_icon, None), Function(sdl_achv_clear_persistents_ask, engine.get_cur_route().get_achv_arr())]

    # Ачивки
    $ sdl_achv_count = 0
    for achv in engine.get_cur_route().get_achv_arr():
        if (achv.get_persistent() in sdl_achv_hidden) and not (getattr(persistent, achv.get_persistent())):
            pass
        elif achv.check_mask(engine.get_cur_char().get_char_mask()):
            $ sdl_achv_pers_counter = 0
            if getattr(persistent, achv.get_persistent()):
                $ sdl_achv_pers_counter = getattr(persistent, achv.get_persistent())
                # Значок ачивки
                imagebutton xcenter 780 ycenter (165 + 64 * sdl_achv_count):
                    focus_mask True
                    idle (achv.get_icon())
                    hovered [Function(engine.set_hovered_achv, achv), achv.get_override() if ((achv.get_override() != None) and (achv.check_override() != False)) else Show("sdl_achv_sprite", Dissolve(0.5), engine.get_cur_route().get_sprite_who(), achv.get_sprite_emo(), engine.get_cur_route().get_sprite_clothes())]
                    unhovered [Function(engine.set_hovered_achv, None), Show("sdl_achv_sprite", Dissolve(0.5), engine.get_cur_route().get_sprite_who(), "pi_smile" if engine.get_cur_route() == sdl_achv_route_me_owl else "smile", engine.get_cur_route().get_sprite_clothes())]
                    action [Function(engine.set_hovered_achv, achv)]

                if achv.get_replay() != None:
                    # Кнопка перехода к концовке
                    imagebutton xcenter 595 ycenter (165 + 64 * sdl_achv_count):
                        hover_sound sdl_achv_click
                        idle ("sdl_achv_check_inactive")
                        hover ("sdl_achv_check_active")
                        hovered [Function(engine.set_hovered_icon, "sdl_achv_jump")]
                        unhovered [Function(engine.set_hovered_icon, None)]
                        action [Function(engine.set_hovered_icon, None), Replay("sdl_replay", scope=sdl_add_to_dict(achv.get_replay().get_scope(), "cur_char", engine.get_cur_char().get_variable()), locked=False), Play('music', get_playing_7dl(), fadein=5)]

                if achv.get_postscriptum() != None and persistent.alt_binder:
                    imagebutton xcenter 970 ycenter (165 + 64 * sdl_achv_count):
                        hover_sound sdl_achv_click
                        idle ("sdl_achv_ps_inactive")
                        hover ("sdl_achv_ps_active")
                        hovered [Function(engine.set_hovered_icon, "sdl_achv_ps_jump")]
                        unhovered [Function(engine.set_hovered_icon, None)]
                        action [Function(engine.set_hovered_icon, None), Replay("sdl_replay", scope=sdl_add_to_dict(achv.get_postscriptum().get_scope(), "cur_char", engine.get_cur_char().get_variable()), locked=False), Play('music', get_playing_7dl(), fadein=5)]
            else:
                # Заблокированная ачивка
                imagebutton xcenter 780 ycenter (165 + 64 * sdl_achv_count):
                    focus_mask True
                    idle ("sdl_achv_lock")
                    hovered [Function(engine.set_hovered_achv, achv), achv.get_override() if ((achv.get_override() != None) and (achv.check_override() != False)) else Show("sdl_achv_sprite", Dissolve(0.5), engine.get_cur_route().get_sprite_who(), achv.get_sprite_emo(), engine.get_cur_route().get_sprite_clothes())]
                    unhovered [Function(engine.set_hovered_achv, None), Show("sdl_achv_sprite", Dissolve(0.5), engine.get_cur_route().get_sprite_who(), "pi_smile" if engine.get_cur_route() == sdl_achv_route_me_owl else "smile", engine.get_cur_route().get_sprite_clothes())]
                    action [Function(engine.set_hovered_achv, achv)]

                # Иконка пререквизитов
                $ sdl_achv_prerequisites = achv.get_prerequisites()
                for prerequisite in sdl_achv_prerequisites:
                    if not prerequisite.check_conditions():
                        imagebutton xcenter 595 ycenter (165 + 64 * sdl_achv_count):
                            hover_sound sdl_achv_info
                            idle ("sdl_achv_info_inactive")
                            hover ("sdl_achv_info_active")
                            hovered [Function(engine.set_cur_prerequisites, achv.get_prerequisites())]
                            unhovered [Function(engine.set_cur_prerequisites, None)]
                            action [Function(engine.set_cur_prerequisites, achv.get_prerequisites())]
                        $ sdl_achv_prerequisites = {}
            # Счётчик прохождений
            if False:
                frame:
                    xysize (50, 50)
                    xcenter 965
                    ycenter (165 + 64 * sdl_achv_count)
                    background Frame("sdl_achv_frame_counter", 0, 0)

                    add Text(str(sdl_achv_pers_counter), style="sdl_achv_font_small_inactive") maxsize (25, 25) align (0.5, 0.5)
            $ sdl_achv_count += 1
        else:
            # Закрываем недоступные выбранному персонажу ачивки туманом
            fixed:
                xcenter 750
                ycenter (165 + 64 * sdl_achv_count)
                xysize (360, 52)

                if getattr(persistent, achv.get_persistent()):
                    add achv.get_icon() pos (60, 0)
                    if achv.get_replay() != None:
                        add "sdl_achv_check_inactive" pos (0, 0)
                else:
                    add "sdl_achv_lock" pos (60, 0)
                    $ sdl_achv_prerequisites = achv.get_prerequisites()
                    for prerequisite in sdl_achv_prerequisites:
                        if not prerequisite.check_conditions():
                            add "sdl_achv_info_inactive" pos (0, 0)
                            $ sdl_achv_prerequisites = {}

                add "sdl_achv_fog" pos (0, 0)
            # Счётчик прохождений
            if False:
                frame:
                    xysize (50, 50)
                    xcenter 965
                    ycenter (165 + 64 * sdl_achv_count)
                    background Frame("sdl_achv_frame_counter", 0, 0)

                    add Text(str(sdl_achv_pers_counter), style="sdl_achv_font_small_inactive") maxsize (25, 25) align (0.5, 0.5)
            $ sdl_achv_count += 1

    # Всплывающая инфа
    if engine.get_hovered_achv() != None:
        add engine.get_hovered_achv().get_text() xcenter 440 ycenter 675

    if engine.get_cur_prerequisites() != None:
        use sdl_achv_prerequisites(engine)

    # Выбор персонажа
    add "sdl_achv_char_label" xcenter 780 ycenter 891
    frame:
        xcenter 780
        ycenter 973
        background Frame("sdl_achv_frame_char", 0, 0)

        add engine.get_cur_char().get_icon()
    if engine.get_cur_char().get_text() != None:
        add engine.get_cur_char().get_text() xcenter 780 ycenter 1055

    if engine.get_cur_char_idx() > 0:
        imagebutton xcenter 652 ycenter 973:
            focus_mask True
            hover_sound sdl_achv_click
            idle ("sdl_achv_arrow_left_inactive")
            hover ("sdl_achv_arrow_left_active")
            action [Function(engine.cur_char_idx_dec)]

    if engine.get_cur_char_idx() < (engine.get_chars_amount() - 1):
        imagebutton xcenter 908 ycenter 973:
            focus_mask True
            hover_sound sdl_achv_click
            idle ("sdl_achv_arrow_right_inactive")
            hover ("sdl_achv_arrow_right_active")
            action [Function(engine.cur_char_idx_inc)]
# ------------------------------------------------------------------------------------------------
# Экран пререквизитов
screen sdl_achv_prerequisites(engine):
    frame xalign 0.5 yalign 0.5:
        background Frame("sdl_achv_frame_prerequisite", 0, 0)

        vbox:
            spacing 25
            null height 25
            hbox xalign 0.5:
                spacing 25
                null width 25
                add engine.get_cur_prerequisites()[0].get_text() xalign 0.5
                null width 25
            for prerequisite in engine.get_cur_prerequisites():
                if not prerequisite.check_conditions():
                    if prerequisite.get_achievements() != None:
                        hbox xalign 0.5:
                            spacing 25
                            null width 25
                            $ sdl_not_first_image = False
                            for prereq_achv in prerequisite.get_achievements():
                                if sdl_not_first_image:
                                    add "sdl_achv_info_or"
                                vbox:
                                    spacing 10
                                    add prereq_achv.get_icon()
                                    add prereq_achv.get_text() zoom 0.85 xalign 0.5
                                $ sdl_not_first_image = True
                            null width 25
            null height 25
# ------------------------------------------------------------------------------------------------
# Экран спрайта персонажа
screen sdl_achv_sprite(who, emo, clothes):
    tag sprite
    layer "transient"

    # Для защиты от перекраски спрайтов после реплеев
    $ persistent.sprite_time = "day"

    if who != None:
        if persistent.achv_sprite_emo_7dl or (who == "ars"):
            add (who + " " + emo + " " + clothes) yoffset 60 at cright
        elif who == "am":
            add "am pi_smile pioneer" yoffset 60 at cright
        else:
            add (who + " smile " + clothes) yoffset 60 at cright



##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ЛЕЙБЛЫ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Точка входа
label sdl_achvlist_main:
    $ day_time()
    $ persistent.sprite_time = "day"
    $ plthr = u"Достижения"
    if not sdl_mus_engine.is_active:
        if persistent.alt_binder:
            play music music_7dl["ambience_safe_true"] fadein 5
        else:
            play music music_7dl["ambience_safe"] fadein 5

    $ renpy.block_rollback()
    $ sdl_achv_engine = sdl_achv_Engine(sdl_achv_route_default)
    $ sdl_achv_progress_calc()
    $ sdl_achv_show_puzzle_prereq = False
    call screen sdl_achvlist_main(sdl_achv_engine)
# ------------------------------------------------------------------------------------------------
# Выбор раздела
label sdl_achvlist_section(engine, section=None):
    $ engine.set_cur_section(section)

    call screen sdl_achvlist_main(engine)

    return
