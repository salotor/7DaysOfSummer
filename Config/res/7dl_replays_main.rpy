##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ФУНКЦИИ И КЛАССЫ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
init python:
    # Основной класс
    class sdl_repl_Engine:
        def __init__(self, section_arr):
            self.section_arr = section_arr
            self.available_chars = []

            self.cur_section = None
            self.cur_route = None
            self.cur_day = None
            self.cur_page = 0
            self.cur_char_idx = 0

        def set_cur_section(self, section):
            self.cur_section = section

        def set_cur_route(self, route):
            self.cur_route = route

        def set_cur_day(self, day):
            self.cur_day = day
            self.cur_page = 0
            self.check_available_chars()

        def cur_page_inc(self):
            self.cur_page += 2

        def cur_page_dec(self):
            self.cur_page -= 2

        def cur_char_idx_inc(self):
            self.cur_char_idx += 1

        def cur_char_idx_dec(self):
            self.cur_char_idx -= 1

        def get_section_arr(self):
            return self.section_arr

        def get_cur_section(self):
            return self.cur_section

        def get_cur_route(self):
            return self.cur_route

        def get_cur_day(self):
            return self.cur_day

        def get_cur_page(self):
            return self.cur_page

        def get_cur_tag(self):
            if self.cur_route != None:
                return self.cur_route.get_title() + ". " + self.cur_day.get_title()
            else:
                return self.cur_section.get_title() + ". " + self.cur_day.get_title()

        def get_cur_char_idx(self):
            return self.cur_char_idx

        def get_chars_amount(self):
            return len(self.available_chars)

        def get_cur_char(self):
            return self.available_chars[self.cur_char_idx]

        def reset_vars(self):
            self.cur_day = None
            self.cur_page = 0
            self.cur_char_idx = 0
            self.available_chars = []
            return

        def check_available_chars(self):
            self.cur_char_idx = 0
            self.available_chars = []
            for char in sdl_repl_characters:
                if self.cur_day.check_mask(char.get_char_mask()):
                    self.available_chars.append(char)
            return

    # Раздел | Рут
    class sdl_repl_Section:
        def __init__(self, title, icon, route_arr, day_arr, available=True):
            self.title = title
            self.icon = icon
            self.route_arr = route_arr
            self.day_arr = day_arr
            self.available = available

        def get_title(self):
            return self.title

        def get_icon(self):
            return self.icon

        def get_route_arr(self):
            return self.route_arr

        def get_day_arr(self):
            return self.day_arr

        def is_available(self):
            return self.available

    # День
    class sdl_repl_Day:
        def __init__(self, title, label_arr, char_mask=7):
            self.title = title
            self.label_arr = label_arr
            self.char_mask = char_mask

        def get_title(self):
            return self.title

        def get_label_arr(self):
            return self.label_arr

        def check_mask(self, char_mask):
            return self.char_mask & char_mask

    # Лейбл
    class sdl_repl_Label:
        def __init__(self, title, replay, char_mask=7):
            self.title = title
            self.replay = replay
            self.char_mask = char_mask

        def get_title(self):
            return self.title

        def get_label(self):
            return self.replay.get_label()

        def get_replay(self):
            return self.replay

        def check_mask(self, char_mask):
            return self.char_mask & char_mask

    # Калькулятор прогресса
    def sdl_repl_progress_calc():
        global sdl_repl_progress
        seen_count = 0.0
        label_count = 0.0
        for i in sdl_repl_sections:
            if i == sdl_repl_common:
                for k in i.day_arr:
                    for l in k.label_arr:
                        if renpy.seen_label(l.replay.label):
                            seen_count += 1
                        label_count += 1
            else:
                for a in i.route_arr:
                    for k in a.day_arr:
                        for l in k.label_arr:
                            if renpy.seen_label(l.replay.label):
                                seen_count += 1
                            label_count += 1
        ratio = seen_count / label_count * 100
        sdl_repl_progress = round(ratio, 1)

##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ЭКРАНЫ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Начальный экран
screen sdl_replays_main(engine=sdl_repl_engine):
    tag menu

    add "bg repl_screen_7dl" xcenter 0.503 ycenter 0.532

    if engine.get_cur_day() != None:
        use sdl_repl_day(engine)
    else:
        use sdl_repl_section_selector(engine)
# ------------------------------------------------------------------------------------------------
# Экран выбора раздела | рута
screen sdl_repl_section_selector(engine):
    tag selector

    if (engine.get_cur_route() != None) or ((engine.get_cur_section() != None) and (engine.get_cur_section().get_route_arr() != None)):
        # Селектор рута

        textbutton "…":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action [Function(engine.set_cur_section, None), Function(engine.set_cur_route, None)]

        if engine.get_cur_section().get_icon() != None:
            add engine.get_cur_section().get_icon() xalign 0.415 ypos 0.187 maxsize (250, 50)

        $ sdl_route_count = 0
        for route in engine.get_cur_section().get_route_arr():
            if route == engine.get_cur_route():
                text route.get_title():
                    style "replays_text_current"
                    xpos 0.235
                    ypos (0.236 + 0.049 * sdl_route_count)
            elif route.is_available():
                textbutton route.get_title():
                    style "log_button"
                    text_style "replays_textbutton"
                    xpos 0.235
                    ypos (0.236 + 0.049 * sdl_route_count)
                    action [Function(engine.set_cur_route, route)]
            else:
                text route.get_title():
                    style "replays_text_locked"
                    xpos 0.235
                    ypos (0.236 + 0.049 * sdl_route_count)
            $ sdl_route_count += 1
    else:
        # Селектор раздела

        $ sdl_section_count = 0
        for section in engine.get_section_arr():
            if section.get_route_arr() != None:
                textbutton section.get_title():
                    style "log_button"
                    text_style "replays_textbutton"
                    xpos 0.235
                    ypos (0.187 + 0.049 * sdl_section_count)
                    action [Function(engine.set_cur_section, section)]
            else:
                if section == engine.get_cur_section():
                    text section.get_title():
                        style "replays_text_current"
                        xpos 0.235
                        ypos (0.187 + 0.049 * sdl_section_count)
                else:
                    textbutton section.get_title():
                        style "log_button"
                        text_style "replays_textbutton"
                        xpos 0.235
                        ypos (0.187 + 0.049 * sdl_section_count)
                        action [Function(engine.set_cur_section, section)]
            $ sdl_section_count += 1
        if engine.get_cur_section() == None:
            text "Прогресс прохождения мода: [sdl_repl_progress]%":
                style "old_road_textbutton"
                xpos 0.534
                ypos 0.187
                xmaximum 450
    if (engine.get_cur_route() != None) or ((engine.get_cur_section() != None) and (engine.get_cur_section().get_route_arr() == None)):
        use sdl_repl_route(engine)
# ------------------------------------------------------------------------------------------------
# Экран рута
screen sdl_repl_route(engine):
    tag route

    if (engine.get_cur_route() != None):
        $ sdl_day_count = 0
        for day in engine.get_cur_route().get_day_arr():
            textbutton day.get_title():
                style "log_button"
                text_style "replays_textbutton"
                xpos 0.544
                ypos (0.187 + 0.049 * sdl_day_count)
                action [Function(engine.set_cur_day, day)]
            $ sdl_day_count += 1
    else:
        $ sdl_day_count = 0
        for day in engine.get_cur_section().get_day_arr():
            textbutton day.get_title():
                style "log_button"
                text_style "replays_textbutton"
                xpos 0.544
                ypos (0.187 + 0.049 * sdl_day_count)
                action [Function(engine.set_cur_day, day)]
            $ sdl_day_count += 1
# ------------------------------------------------------------------------------------------------
# Экран дня
screen sdl_repl_day(engine):
    tag day

    textbutton "…":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Function(engine.reset_vars)]

    if engine.get_cur_section().get_icon() != None:
        add engine.get_cur_section().get_icon() xalign 0.415 ypos 0.187 maxsize (250, 50)

    text engine.get_cur_tag():
        style "replays_text_current"
        xalign 0.690
        ypos 0.187

    $ sdl_label_count = 0
    for label in engine.get_cur_day().get_label_arr()[engine.get_cur_page() * 12 : (engine.get_cur_page()+2) * 12]:
        $ sdl_x_shift = sdl_label_count // 12
        $ sdl_y_shift = sdl_label_count % 12

        if label.check_mask(engine.get_cur_char().get_char_mask()):
            if renpy.seen_label(label.get_label()):
                textbutton label.get_title():
                    style "log_button"
                    text_style "replays_textbutton"
                    xpos (0.235 + 0.309 * sdl_x_shift)
                    ypos (0.236 + 0.049 * sdl_y_shift)
                    action [Replay("sdl_replay", scope=sdl_add_to_dict(label.get_replay().get_scope(), "cur_char", engine.get_cur_char().get_variable()), locked=False), Play('music', get_playing_7dl(), fadein=3)]
            elif label.get_label() in sdl_repl_label_frozen:
                pass
            else:
                text "?????":
                    style "replays_text_locked"
                    xpos (0.235 + 0.309 * sdl_x_shift)
                    ypos (0.236 + 0.049 * sdl_y_shift)
        else:
            # Зачёркиваем недоступные выбранному персонажу лейблы
            if renpy.seen_label(label.get_label()):
                text ("{s}" + label.get_title() + "{/s}"):
                    style "replays_text_locked"
                    xpos (0.235 + 0.309 * sdl_x_shift)
                    ypos (0.236 + 0.049 * sdl_y_shift)
            elif label.get_label() in sdl_repl_label_frozen:
                pass
            else:
                text "{s}?????{/s}":
                    style "replays_text_locked"
                    xpos (0.235 + 0.309 * sdl_x_shift)
                    ypos (0.236 + 0.049 * sdl_y_shift)

        $ sdl_label_count += 1

    # Нумерация страниц
    text "Часть " + str(engine.get_cur_page() + 1):
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    text "Часть " + str(engine.get_cur_page() + 2):
        style "replays_text"
        xcenter 0.741
        ycenter 0.883

    # Стрелки
    if engine.get_cur_page() > 0:
        imagebutton:
            auto get_image_7dl("gui/stories/repl/buttons/repl_arrow_left_%s.png") xcenter 0.256 ycenter 0.923
            activate_sound repl_page_turnings[str(random.choice([1, 2, 3, 4, 5]))]
            action Function(engine.cur_page_dec)
    if len(engine.get_cur_day().get_label_arr()) > ((engine.get_cur_page() + 2) * 12):
        imagebutton:
            auto get_image_7dl("gui/stories/repl/buttons/repl_arrow_right_%s.png") xcenter 0.749 ycenter 0.923
            activate_sound repl_page_turnings[str(random.choice([1, 2, 3, 4, 5]))]
            action Function(engine.cur_page_inc)

    # Выбор персонажа
    add "sdl_repl_screen_char" xcenter 0.9 ycenter 0.5
    add "sdl_repl_char_label" xcenter 0.89  ycenter 0.3
    frame:
        xcenter 0.89
        ycenter 0.53
        background Frame("sdl_repl_frame_char", 0, 0)

        add engine.get_cur_char().get_icon()
    if engine.get_cur_char().get_text() != None:
        add engine.get_cur_char().get_text() xcenter 0.89 ycenter 0.6575

    if engine.get_cur_char_idx() > 0:
        imagebutton xcenter 0.89 ycenter 0.36:
            auto "sdl_repl_arrow_up_%s"
            action [Function(engine.cur_char_idx_dec)]

    if engine.get_cur_char_idx() < (engine.get_chars_amount() - 1):
        imagebutton xcenter 0.89 ycenter 0.72:
            auto "sdl_repl_arrow_down_%s"
            action [Function(engine.cur_char_idx_inc)]
