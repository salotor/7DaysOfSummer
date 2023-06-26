init python:
    def noir_screens_save():
        renpy.display.screen.screens[("original_game_menu_selector", None)] =  renpy.display.screen.screens[("game_menu_selector", None)]
        renpy.display.screen.screens[("original_choice", None)] =              renpy.display.screen.screens[("choice", None)]
        renpy.display.screen.screens[("original_say", None)] =                 renpy.display.screen.screens[("say", None)]
        renpy.display.screen.screens[("original_nvl", None)] =                 renpy.display.screen.screens[("nvl", None)]
        renpy.display.screen.screens[("original_text_history_screen", None)] = renpy.display.screen.screens[("text_history_screen", None)]

    def noir_screens_on():
        renpy.display.screen.screens[("game_menu_selector", None)] =           renpy.display.screen.screens[("noir_game_menu_selector", None)]
        renpy.display.screen.screens[("choice", None)] =                       renpy.display.screen.screens[("noir_choice", None)]
        renpy.display.screen.screens[("say", None)] =                          renpy.display.screen.screens[("noir_say", None)]
        renpy.display.screen.screens[("nvl", None)] =                          renpy.display.screen.screens[("noir_nvl", None)]
        renpy.display.screen.screens[("text_history_screen", None)] =          renpy.display.screen.screens[("noir_text_history_screen", None)]
        config.mouse = {'default' : [(get_image_7dl("gui/noir/mouse/1.png"), 0, 0)]}

    def replay_noir_screens_on():
        renpy.display.screen.screens[("game_menu_selector", None)] =           renpy.display.screen.screens[("noir_game_menu_selector", None)]
        renpy.display.screen.screens[("choice", None)] =                       renpy.display.screen.screens[("noir_choice", None)]
        renpy.display.screen.screens[("say", None)] =                          renpy.display.screen.screens[("noir_say", None)]
        renpy.display.screen.screens[("nvl", None)] =                          renpy.display.screen.screens[("noir_nvl", None)]
        renpy.display.screen.screens[("text_history_screen", None)] =          renpy.display.screen.screens[("replay_noir_text_history_screen", None)]
        config.mouse = {'default' : [(get_image_7dl("gui/noir/mouse/1.png"), 0, 0)]}

    def noir_screens_load():
        renpy.display.screen.screens[("game_menu_selector", None)] =           renpy.display.screen.screens[("original_game_menu_selector", None)]
        renpy.display.screen.screens[("choice", None)] =                       renpy.display.screen.screens[("original_choice", None)]
        renpy.display.screen.screens[("say", None)] =                          renpy.display.screen.screens[("original_say", None)]
        renpy.display.screen.screens[("nvl", None)] =                          renpy.display.screen.screens[("original_nvl", None)]
        renpy.display.screen.screens[("text_history_screen", None)] =          renpy.display.screen.screens[("original_text_history_screen", None)]
        config.mouse = {'default' : [('images/misc/mouse/1.png', 0, 0)]}

    noir_screens_save()

init -999:
    $ noir_interface = False
    $ persistent.noir_interface = False

init 1:
    image noir_ctc_animation = Animation(
        get_image_7dl("gui/noir/ctc/ctc01.png"), 0.15,
        get_image_7dl("gui/noir/ctc/ctc02.png"), 0.15,
        get_image_7dl("gui/noir/ctc/ctc03.png"), 0.15,
        get_image_7dl("gui/noir/ctc/ctc04.png"), 0.15,
        get_image_7dl("gui/noir/ctc/ctc05.png"), 0.15,
        get_image_7dl("gui/noir/ctc/ctc06.png"), 0.15,
        get_image_7dl("gui/noir/ctc/ctc07.png"), 0.15,
        get_image_7dl("gui/noir/ctc/ctc08.png"), 0.15,
        xpos=0.905, ypos=0.98, xanchor=1.0, yanchor=1.0)
    image noir_ctc_animation_nvl = Animation(
        get_image_7dl("gui/noir/ctc/ctc01.png"), 0.15,
        get_image_7dl("gui/noir/ctc/ctc02.png"), 0.15,
        get_image_7dl("gui/noir/ctc/ctc03.png"), 0.15,
        get_image_7dl("gui/noir/ctc/ctc04.png"), 0.15,
        get_image_7dl("gui/noir/ctc/ctc05.png"), 0.15,
        get_image_7dl("gui/noir/ctc/ctc06.png"), 0.15,
        get_image_7dl("gui/noir/ctc/ctc07.png"), 0.15,
        get_image_7dl("gui/noir/ctc/ctc08.png"), 0.15,
        xpos=0.9, ypos=0.94, xanchor=1.0, yanchor=1.0)

init 3:
    $ colors['ai']['noir'] = (117, 117, 117, 255)
    $ colors['al']['noir'] = (196, 196, 196, 255)
    $ colors['am']['noir'] = (176, 176, 176, 255)
    $ colors['ase']['noir'] = (168, 168, 168, 255)
    $ colors['ba']['noir'] = (231, 231, 231, 255)
    $ colors['bb']['noir'] = (203, 203, 203, 255)
    $ colors['cs']['noir'] = (174, 174, 174, 255)
    $ colors['dn']['noir'] = (160, 160, 160, 255)
    $ colors['dreamgirl']['noir'] = (192, 192, 192, 255)
    $ colors['dv']['noir'] = (204, 204, 204, 255)
    $ colors['dy']['noir'] = (71, 71, 71, 255)
    $ colors['el']['noir'] = (230, 230, 230, 255)
    $ colors['hg']['noir'] = (115, 115, 115, 255)
    $ colors['ka']['noir'] = (191, 191, 191, 255)
    $ colors['kids']['noir'] = (190, 190, 190, 255)
    $ colors['me']['noir'] = (214, 214, 214, 255)
    $ colors['mi']['noir'] = (92, 92, 92, 255)
    $ colors['ml']['noir'] = (119, 119, 119, 255)
    $ colors['ml2']['noir'] = (88, 88, 88, 255)
    $ colors['ml3']['noir'] = (130, 130, 130, 255)
    $ colors['mt']['noir'] = (75, 75, 75, 255)
    $ colors['mz']['noir'] = (110, 110, 110, 255)
    $ colors['pi']['noir'] = (138, 138, 138, 255)
    $ colors['sa']['noir'] = (216, 216, 216, 255)
    $ colors['sak']['noir'] = (165, 165, 165, 255)
    $ colors['sh']['noir'] = (229, 229, 229, 255)
    $ colors['sl']['noir'] = (216, 216, 216, 255)
    $ colors['tn']['noir'] = (189, 189, 189, 255)
    $ colors['un']['noir'] = (162, 162, 162, 255)
    $ colors['us']['noir'] = (168, 168, 168, 255)
    $ colors['uv']['noir'] = (123, 123, 123, 255)
    $ colors['voice']['noir'] = (214, 214, 214, 255)
    $ colors['voice1']['noir'] = (213, 213, 213, 255)
    $ colors['voices']['noir'] = (192, 192, 192, 255)
    $ colors['we']['noir'] = (175, 175, 175, 255)

init 4 python:
    def noir_get_color(x):
        global store
        global time_of_day
        if 'noir' in store.colors[x]:
            return store.colors[x]['noir']
        else:
            return store.colors[x][time_of_day]

    def noir_char_define(x,is_nvl=False):
        global DynamicCharacter
        global _show_two_window
        global nvl
        global store
        gl = globals()
        v = "_voice"
        if  x == 'narrator':
            if  is_nvl:
                gl['narrator'] = Character(None, kind=nvl, what_style="nvl_narrator_noir", ctc="noir_ctc_animation_nvl", ctc_position="fixed")
            else:
                gl['narrator'] = Character(None, what_style="narrator_noir", ctc="noir_ctc_animation", ctc_position="fixed")
            return
        if  x == 'th':
            if  is_nvl:
                gl['th'] = Character(None, kind=nvl, what_style="nvl_thoughts_noir",what_prefix = th_prefix,what_suffix=th_suffix, ctc="noir_ctc_animation_nvl", ctc_position="fixed")
            else:
                gl['th'] = Character(None, what_style="thoughts_noir",what_prefix = th_prefix,what_suffix=th_suffix, ctc="noir_ctc_animation", ctc_position="fixed")
            return
        if  is_nvl:
            gl[x] = DynamicCharacter("%s_name"%x, color=noir_get_color(x), kind=nvl, what_style="nvl_normal_noir",who_suffix=":", ctc="noir_ctc_animation_nvl", ctc_position="fixed")
            gl["%s_name"%x] = store.names[x]
        else:
            gl[x] = DynamicCharacter("%s_name"%x, color=noir_get_color(x), show_two_window=_show_two_window,  what_style="normal_noir", ctc="noir_ctc_animation", ctc_position="fixed")
            gl["%s_name"%x] = store.names[x]

    def noir_set_mode_adv():
        nvl_clear()

        global menu
        menu = renpy.display_menu

        global store
        for x in store.names_list:
            noir_char_define(x)

    def noir_set_mode_nvl():
        nvl_clear()

        global menu
        menu = nvl_menu

        global narrator
        global th
        narrator_nvl = narrator
        th_nvl = th

        global store
        for x in store.names_list:
            noir_char_define(x,True)

    style.normal_noir = Style(style.base_font)
    style.normal_noir.color = "#000"
    style.normal_noir.drop_shadow=(2, 2)
    style.normal_noir.drop_shadow_color = "#FFF"
    style.narrator_noir = Style(style.normal_noir)
    style.narrator_noir.italic = False
    style.thoughts_noir = Style(style.normal_noir)
    style.thoughts_noir.bold = False

    style.nvl_normal_noir = Style(style.base_font)
    style.nvl_normal_noir.color = "#FFF"
    style.nvl_normal_noir.drop_shadow=(2, 2)
    style.nvl_normal_noir.drop_shadow_color = "#000"
    style.nvl_narrator_noir = Style(style.nvl_normal_noir)
    style.nvl_narrator_noir.italic = False
    style.nvl_thoughts_noir = Style(style.nvl_normal_noir)
    style.nvl_thoughts_noir.bold = False

init 5 python:
    def noir_interface_on():
        noir_screens_on()
        noir_set_mode_adv()
        persistent.noir_interface = True
        persistent.sprite_time = 'noir'

    def replay_noir_interface_on():
        replay_noir_screens_on()
        noir_set_mode_adv()
        persistent.noir_interface = True
        persistent.sprite_time = 'noir'

    def noir_interface_off():
        global time_of_day
        noir_screens_load()
        set_mode_adv()
        persistent.noir_interface = False
        persistent.sprite_time = time_of_day
        any_time(time_of_day)

screen noir_game_menu_selector: # поправить координаты
    tag menu
    modal True
    button:
        style "blank_button"
        xpos 0
        ypos 0
        xfill True
        yfill True
        action Return()
    add get_image_7dl("gui/noir/ingame_menu/ingame_menu.png"):
        xalign 0.5
        yalign 0.5
    imagemap:
        auto get_image_7dl("gui/noir/ingame_menu/ingame_menu_%s.png")
        xalign 0.5
        yalign 0.5
        hotspot (0, 83, 660, 65):
            focus_mask None
            clicked [Function(noir_interface_off), MainMenu(confirm=False)]
        hotspot (0, 148, 660, 65):
            focus_mask None
            clicked ShowMenu('save')
        hotspot (0, 213, 660, 65):
            focus_mask None
            clicked ShowMenu('load')
        hotspot (0, 278, 660, 65):
            focus_mask None
            clicked (ShowMenu('alt_preferences'), Hide('noir_game_menu_selector'))
        hotspot (0, 343, 660, 65):
            focus_mask None
            clicked ShowMenu('quit')

screen noir_choice:
    modal True
    python:
        choice_colors_hover = "#ffffff"
        choice_colors = "#cccccc"
        choice_colors_selected = "#000000"
    window:
        background Frame(get_image_7dl("gui/noir/choice/choice_box.png"),50,50)
        xfill True
        yalign 0.5
        left_padding 75
        right_padding 75
        bottom_padding 50
        top_padding 50
        vbox:
            xalign 0.5
            for caption, action, chosen  in items:
                if action and caption:
                    button:
                        background None
                        xalign 0.5
                        action action
                        text caption:
                            font header_font
                            size 37
                            hover_size 37
                            color choice_colors_selected
                            outlines [ (1, "#CCC", 1, 1) ]
                            hover_color choice_colors_hover
                            hover_outlines [ (1, "#CCC", 1, 1) ]
                            xcenter 0.5
                            text_align 0.5
                else:
                    text caption:
                        font header_font
                        size 60
                        color choice_colors
                        outlines [ (1, "#FFF", 1, 1) ]
                        text_align 0.5
                        xcenter 0.5

screen noir_say:
    window:
        background None
        id "window"
        if persistent.font_size == "large":
            imagebutton:
                auto get_image_7dl("gui/noir/dialogue_box/backward_%s.png")
                xpos 38
                ypos 924
                action ShowMenu("text_history")
            add get_image_7dl("gui/noir/dialogue_box/dialogue_box_large.png"):
                xpos 174
                ypos 866
            imagebutton:
                auto get_image_7dl("gui/noir/dialogue_box/hide_%s.png")
                xpos 1508
                ypos 883
                action HideInterface()
            imagebutton:
                auto get_image_7dl("gui/noir/dialogue_box/save_%s.png")
                xpos 1567
                ypos 883
                action ShowMenu('save')
            imagebutton:
                auto get_image_7dl("gui/noir/dialogue_box/menu_%s.png")
                xpos 1625
                ypos 883
                action ShowMenu('game_menu_selector')
            imagebutton:
                auto get_image_7dl("gui/noir/dialogue_box/load_%s.png")
                xpos 1682
                ypos 883
                action ShowMenu('load')
            if not config.skipping:
                imagebutton:
                    auto get_image_7dl("gui/noir/dialogue_box/forward_%s.png")
                    xpos 1768
                    ypos 924
                    action Skip()
            else:
                imagebutton:
                    auto get_image_7dl("gui/noir/dialogue_box/fast_forward_%s.png")
                    xpos 1768
                    ypos 924
                    action Skip()
            text what:
                id "what"
                xpos 194
                ypos 914
                xmaximum 1541
                size 35
                line_spacing 1
            if who:
                text who:
                    id "who"
                    xpos 194
                    ypos 877
                    size 35
                    line_spacing 1
        elif persistent.font_size == "small":
            imagebutton:
                auto get_image_7dl("gui/noir/dialogue_box/backward_%s.png")
                xpos 38
                ypos 949
                action ShowMenu("text_history")
            add get_image_7dl("gui/noir/dialogue_box/dialogue_box.png"):
                xpos 174
                ypos 916
            imagebutton:
                auto get_image_7dl("gui/noir/dialogue_box/hide_%s.png")
                xpos 1508
                ypos 933
                action HideInterface()
            imagebutton:
                auto get_image_7dl("gui/noir/dialogue_box/save_%s.png")
                xpos 1567
                ypos 933
                action ShowMenu('save')
            imagebutton:
                auto get_image_7dl("gui/noir/dialogue_box/menu_%s.png")
                xpos 1625
                ypos 933
                action ShowMenu('game_menu_selector')
            imagebutton:
                auto get_image_7dl("gui/noir/dialogue_box/load_%s.png")
                xpos 1682
                ypos 933
                action ShowMenu('load')
            if not config.skipping:
                imagebutton:
                    auto get_image_7dl("gui/noir/dialogue_box/forward_%s.png")
                    xpos 1768
                    ypos 949
                    action Skip()
            else:
                imagebutton:
                    auto get_image_7dl("gui/noir/dialogue_box/fast_forward_%s.png")
                    xpos 1768
                    ypos 949
                    action Skip()
            text what:
                id "what"
                xpos 194
                ypos 964
                xmaximum 1541
                size 28
                line_spacing 2
            if who:
                text who:
                    id "who"
                    xpos 194
                    ypos 931
                    size 28
                    line_spacing 2

screen noir_nvl:
    window:
        background Frame(get_image_7dl("gui/noir/choice/choice_box.png"),50,50)
        xfill True
        yfill True
        yalign 0.5
        left_padding 175
        right_padding 175
        bottom_padding 150
        top_padding 150
        vbox:
            for who, what, who_id, what_id, window_id  in dialogue:
                window:
                    id window_id
                    hbox:
                        spacing 10
                        if persistent.font_size == "large":
                            if who is not None:
                                text who:
                                    id who_id
                                    size 35
                            text what:
                                id what_id
                                size 35
                        elif persistent.font_size == "small":
                            if who is not None:
                                text who:
                                    id who_id
                                    size 28
                            text what:
                                id what_id
                                size 28
            if items:
                vbox:
                    id "menu"
                    for caption, action, chosen  in items:
                        if action:
                            button:
                                style "nvl_menu_choice_button"
                                action action
                                text caption:
                                    style "nvl_menu_choice"
                        else:
                            text caption:
                                style "nvl_dialogue"
    imagebutton:
        auto get_image_7dl("gui/noir/dialogue_box/backward_%s.png")
        xpos 38
        ypos 924
        action ShowMenu("text_history")
    if not config.skipping:
        imagebutton:
            auto get_image_7dl("gui/noir/dialogue_box/forward_%s.png")
            xpos 1768
            ypos 949
            action Skip()
    else:
        imagebutton:
            auto get_image_7dl("gui/noir/dialogue_box/fast_forward_%s.png")
            xpos 1768
            ypos 949
            action Skip()

screen noir_text_history_screen:
    tag menu
    predict False
    $ xmax = 1600
    $ xposition = 100
    $ history_text_size = 21
    $ history_name_size = 22
    if persistent.font_size == "large":
        $ history_text_size = 28
        $ history_name_size = 29
    elif persistent.font_size == "giant":
        $ history_text_size = 36
        $ history_name_size = 37
    button:
        style "blank_button"
        xpos 0
        ypos 0
        xfill True
        yfill True
        action Return()
    window:
        background Frame(get_image_7dl("gui/noir/choice/choice_box.png"))
        left_padding 75
        right_padding 75
        bottom_padding 120
        top_padding 120
        viewport:
            id "text_history_screen"
            draggable True
            mousewheel True
            scrollbars None
            yinitial 1.0
            vbox:
                for h in _history_list:
                    if h.who:
                        text h.who:
                            font main_font
                            ypos 0
                            xpos xposition
                            xalign 0.0
                            size history_name_size
                            if "color" in h.who_args:
                                color h.who_args["color"]
                    textbutton h.what:
                        style "log_button"
                        text_style "normal_day"
                        text_size history_text_size
                        action RollbackToIdentifier(h.rollback_identifier)
                        xmaximum xmax
                        text_color "#808080"
                        text_hover_color "#FFF"
                        xpos 100
        vbar:
            value YScrollValue("text_history_screen")
            bottom_bar "images/misc/none.png"
            top_bar "images/misc/none.png"
            thumb get_image_7dl("gui/noir/choice/vthumb.png")
            xoffset 1700

screen replay_noir_text_history_screen:
    tag menu
    predict False
    $ xmax = 1600
    $ xposition = 100
    $ history_text_size = 21
    $ history_name_size = 22
    if persistent.font_size == "large":
        $ history_text_size = 28
        $ history_name_size = 29
    elif persistent.font_size == "giant":
        $ history_text_size = 36
        $ history_name_size = 37
    button:
        style "blank_button"
        xpos 0
        ypos 0
        xfill True
        yfill True
        action Return()
    window:
        background Frame(get_image_7dl("gui/noir/choice/choice_box.png"))
        left_padding 75
        right_padding 75
        bottom_padding 120
        top_padding 120
        viewport:
            id "text_history_screen"
            draggable True
            mousewheel True
            scrollbars None
            yinitial 1.0
            vbox:
                for h in _history_list:
                    if h.who:
                        text h.who:
                            font main_font
                            ypos 0
                            xpos xposition
                            xalign 0.0
                            size history_name_size
                            if "color" in h.who_args:
                                color h.who_args["color"]
                    textbutton h.what:
                        style "log_button"
                        text_style "normal_day"
                        text_size history_text_size
                        action NullAction
                        xmaximum xmax
                        text_color "#808080"
                        text_hover_color "#FFF"
                        xpos 100
        vbar:
            value YScrollValue("text_history_screen")
            bottom_bar "images/misc/none.png"
            top_bar "images/misc/none.png"
            thumb get_image_7dl("gui/noir/choice/vthumb.png")
            xoffset 1700
