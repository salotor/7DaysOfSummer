init 999 python:
    ##\\\\\\\\\\\\\\\\\\\\\\\\\ШРИФТЫ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    olgactt_font = default_7dl_path + "Pics/fonts/olgactt.ttf"
    cinzel_bold_font = default_7dl_path + "Pics/fonts/ljk_Cinzel-Bold.ttf"

    style.replays_textbutton = Style(style.base_font)
    style.replays_textbutton.font  = olgactt_font
    style.replays_textbutton.size = 42
    style.replays_textbutton.color = "#7847f3"
    style.replays_textbutton.hover_color = "#2f059a"
    style.replays_textbutton.selected_color = "#7847f3"
    style.replays_textbutton.selected_idle_color = "#7847f3"
    style.replays_textbutton.selected_hover_color = "#2f059a"
    style.replays_textbutton.insensitive_color = "#7847f3"
    style.replays_textbutton.xmaximum = 450
    style.replays_textbutton.line_spacing = 6

    style.replays_text = Style(style.base_font)
    style.replays_text.font  = olgactt_font
    style.replays_text.size = 42
    style.replays_text.color = "#7847f3"

    style.replays_text_locked = Style(style.base_font)
    style.replays_text_locked.font  = olgactt_font
    style.replays_text_locked.size = 42
    style.replays_text_locked.color = "#808080"

    style.replays_text_current = Style(style.base_font)
    style.replays_text_current.font  = olgactt_font
    style.replays_text_current.size = 42
    style.replays_text_current.color = "#FF0000"

    # Имена персонажей
    style.sdl_repl_font_medium = Style(style.base_font)
    style.sdl_repl_font_medium.font = olgactt_font
    style.sdl_repl_font_medium.size = 50
    style.sdl_repl_font_medium.color = "#7847f3"

    style.sdl_repl_font_small = Style(style.base_font)
    style.sdl_repl_font_small.font = olgactt_font
    style.sdl_repl_font_small.size = 32
    style.sdl_repl_font_small.color = "#7847f3"

    # Настройка переменных
    style.sdl_repl_font_var_big = Style(style.base_font)
    style.sdl_repl_font_var_big.font = cinzel_bold_font
    style.sdl_repl_font_var_big.size = 30
    style.sdl_repl_font_var_big.color = "#D6D6D6"

    style.sdl_repl_font_var_medium = Style(style.base_font)
    style.sdl_repl_font_var_medium.font = cinzel_bold_font
    style.sdl_repl_font_var_medium.size = 25
    style.sdl_repl_font_var_medium.color = "#D6D6D6"

    style.sdl_repl_font_var_small = Style(style.base_font)
    style.sdl_repl_font_var_small.font = cinzel_bold_font
    style.sdl_repl_font_var_small.size = 20
    style.sdl_repl_font_var_small.color = "#D6D6D6"

    style.sdl_repl_font_var_num = Style(style.base_font)
    style.sdl_repl_font_var_num.font = control_freak_upset_font
    style.sdl_repl_font_var_num.size = 20
    style.sdl_repl_font_var_num.color = "#D6D6D6"




init:
    ##\\\\\\\\\\\\\\\\\\\\\\\\\ЭКРАНЫ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # Главный экран
    image bg repl_screen_7dl = get_image_7dl("gui/stories/repl/screens/repl_screen_7dl.png")

    # Окно выбора персонажа
    image sdl_repl_screen_char = get_image_7dl("gui/stories/repl/screens/repl_screen_char.png")

    # Окно настройки переменных
    image sdl_repl_screen_var = get_image_7dl("gui/stories/repl/screens/repl_screen_var.png")

    ##\\\\\\\\\\\\\\\\\\\\\\\\\РАМКИ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # Рамка выбора персонажа
    image sdl_repl_frame_char = get_image_7dl("gui/stories/repl/frames/repl_frame_char.png")
    # Рамки переменных
    image sdl_repl_frame_var_int = get_image_7dl("gui/stories/repl/frames/repl_frame_var_int.png")

    ##\\\\\\\\\\\\\\\\\\\\\\\\\КНОПКИ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # Кнопки смены персонажа
    image sdl_repl_arrow_up_hover = get_image_7dl("gui/stories/repl/buttons/repl_arrow_up_hover.png")
    image sdl_repl_arrow_up_idle = get_image_7dl("gui/stories/repl/buttons/repl_arrow_up_idle.png")
    image sdl_repl_arrow_down_hover = get_image_7dl("gui/stories/repl/buttons/repl_arrow_down_hover.png")
    image sdl_repl_arrow_down_idle = get_image_7dl("gui/stories/repl/buttons/repl_arrow_down_idle.png")
    # Кнопки выбора значений переменных
    image sdl_repl_arrow2_left_hover = get_image_7dl("gui/stories/repl/buttons/repl_arrow2_left_hover.png")
    image sdl_repl_arrow2_left_idle = get_image_7dl("gui/stories/repl/buttons/repl_arrow2_left_idle.png")
    image sdl_repl_arrow2_right_hover = get_image_7dl("gui/stories/repl/buttons/repl_arrow2_right_hover.png")
    image sdl_repl_arrow2_right_idle = get_image_7dl("gui/stories/repl/buttons/repl_arrow2_right_idle.png")
    # Кнопки чекбоксов-переменных
    image sdl_repl_checkbox_unchecked_hover = get_image_7dl("gui/stories/repl/buttons/repl_checkbox_unchecked_hover.png")
    image sdl_repl_checkbox_unchecked_idle = get_image_7dl("gui/stories/repl/buttons/repl_checkbox_unchecked_idle.png")
    image sdl_repl_checkbox_checked_hover = get_image_7dl("gui/stories/repl/buttons/repl_checkbox_checked_hover.png")
    image sdl_repl_checkbox_checked_idle = get_image_7dl("gui/stories/repl/buttons/repl_checkbox_checked_idle.png")
    # Кнопки радио-переменных
    image sdl_repl_radiobutton_unchecked_hover = get_image_7dl("gui/stories/repl/buttons/repl_radiobutton_unchecked_hover.png")
    image sdl_repl_radiobutton_unchecked_idle = get_image_7dl("gui/stories/repl/buttons/repl_radiobutton_unchecked_idle.png")
    image sdl_repl_radiobutton_checked_hover = get_image_7dl("gui/stories/repl/buttons/repl_radiobutton_checked_hover.png")
    image sdl_repl_radiobutton_checked_idle = get_image_7dl("gui/stories/repl/buttons/repl_radiobutton_checked_idle.png")
    # Кнопка ОК
    image sdl_repl_button_ok_hover = get_image_7dl("gui/stories/repl/buttons/repl_button_ok_hover.png")
    image sdl_repl_button_ok_idle = get_image_7dl("gui/stories/repl/buttons/repl_button_ok_idle.png")

    ##\\\\\\\\\\\\\\\\\\\\ПОЛОСЫ ПРОКРУТКИ\\\\\\\\\\\\\\\\\\\\\\\\\
    # Прокрутка значений переменных
    image sdl_repl_bar_null = get_image_7dl("gui/stories/repl/bars/repl_bar_null.png")
    image sdl_repl_bar_full = get_image_7dl("gui/stories/repl/bars/repl_bar_full.png")
    image sdl_repl_bar_thumb_hover = get_image_7dl("gui/stories/repl/bars/repl_bar_thumb_hover.png")
    image sdl_repl_bar_thumb_idle  = get_image_7dl("gui/stories/repl/bars/repl_bar_thumb_idle.png")
    image sdl_repl_vbar_null = get_image_7dl("gui/stories/repl/bars/repl_vbar_null.png")
    image sdl_repl_vbar_full = get_image_7dl("gui/stories/repl/bars/repl_vbar_full.png")
    image sdl_repl_vbar_thumb_hover = get_image_7dl("gui/stories/repl/bars/repl_vbar_thumb_hover.png")
    image sdl_repl_vbar_thumb_idle  = get_image_7dl("gui/stories/repl/bars/repl_vbar_thumb_idle.png")

    ##\\\\\\\\\\\\\\\\\\\\\\\\\ИКОНКИ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # Иконки персонажей
    image sdl_repl_char_loki = get_image_7dl("gui/stories/repl/icons/repl_char_loki.png")
    image sdl_repl_char_herc = get_image_7dl("gui/stories/repl/icons/repl_char_herc.png")
    image sdl_repl_char_dr   = get_image_7dl("gui/stories/repl/icons/repl_char_dr.png")
    image sdl_repl_char_none = get_image_7dl("gui/stories/repl/icons/repl_char_none.png")

    ##\\\\\\\\\\\\\\\\\\\\\\\\\ТЕКСТЫ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # Персонажи
    image sdl_repl_char_label = Text("Character", style="sdl_repl_font_small")
    image sdl_repl_char_label_loki = Text("Loki", style="sdl_repl_font_small")
    image sdl_repl_char_label_herc = Text("Herc", style="sdl_repl_font_small")
    image sdl_repl_char_label_dr   = Text("Wimp", style="sdl_repl_font_small")
    # Разделы
    image sdl_repl_section_label_mi = Text("Miku",     style="sdl_repl_font_medium", color="#00DFFF")
    image sdl_repl_section_label_dv = Text("Alisa",    style="sdl_repl_font_medium", color="#FF7F00")
    image sdl_repl_section_label_sl = Text("Slavya",    style="sdl_repl_font_medium", color="#FFD400")
    image sdl_repl_section_label_un = Text("Lena",     style="sdl_repl_font_medium", color="#D456FF")
    image sdl_repl_section_label_mt = Text("Olga",    style="sdl_repl_font_medium", color="#00EA00")
    image sdl_repl_section_label_us = Text("Ulyana",   style="sdl_repl_font_medium", color="#FF0000")
    image sdl_repl_section_label_me = Text("Loner", style="sdl_repl_font_medium", color="#808080")

    ##\\\\\\\\\\\\\\\\\\\\\\\\\ЗВУКИ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # SFX
    $ repl_page_turning_1 = get_sfx_7dl("repl/repl_page_turning_1_7dl.ogg")
    $ repl_page_turning_2 = get_sfx_7dl("repl/repl_page_turning_2_7dl.ogg")
    $ repl_page_turning_3 = get_sfx_7dl("repl/repl_page_turning_3_7dl.ogg")
    $ repl_page_turning_4 = get_sfx_7dl("repl/repl_page_turning_4_7dl.ogg")
    $ repl_page_turning_5 = get_sfx_7dl("repl/repl_page_turning_5_7dl.ogg")
    $ repl_page_turnings = {
        "1" : repl_page_turning_1,
        "2" : repl_page_turning_2,
        "3" : repl_page_turning_3,
        "4" : repl_page_turning_4,
        "5" : repl_page_turning_5
      }
