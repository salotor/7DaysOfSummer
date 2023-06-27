init:
    $ use_settings_7dl = False

screen alt_game_menu_selector:
    tag menu
    modal True
    $ timeofday = persistent.timeofday
    button:
        style "blank_button"
        xpos 0
        ypos 0
        xfill True
        yfill True
        action Return()
    add get_image("gui/ingame_menu/"+timeofday+"/ingame_menu.png"):
        xalign 0.5
        yalign 0.5
    imagemap:
        if _preferences.language == "spanish":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_es_%s.png")
            xalign 0.5
            yalign 0.5
        elif _preferences.language == "italian":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_it_%s.png")
            xalign 0.5
            yalign 0.5
        elif _preferences.language == "english":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_en_%s.png")
            xalign 0.5
            yalign 0.5
        elif _preferences.language == "chinese":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_ch_%s.png")
            xalign 0.5
            yalign 0.5
        elif _preferences.language == "french":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_fr_%s.png")
            xalign 0.5
            yalign 0.5
        else:
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_%s.png")
            xalign 0.5
            yalign 0.5
        hotspot (0, 83, 660, 65):
            focus_mask None
            clicked [Function(alt_exit), MainMenu()]
        hotspot (0, 148, 660, 65):
            focus_mask None
            clicked ShowMenu('save')
        hotspot (0, 213, 660, 65):
            focus_mask None
            clicked ShowMenu('load')
        hotspot (0, 278, 660, 65):
            focus_mask None
            clicked ShowMenu('preferences')
        hotspot (0, 343, 660, 65):
            focus_mask None
            clicked ShowMenu('quit')

screen alt_preferences:
    tag menu
    modal True
    $ bar_null = Frame(get_image("gui/settings/bar_null.png"),36,36)
    $ bar_full = Frame(get_image("gui/settings/bar_full.png"),36,36)
    if persistent.pivo_default_7dl and (plthr != "Меню"):
        $ grid_y_val = 21
    else:
        $ grid_y_val = 20
    window:
        background get_image("gui/settings/preferences_bg.jpg")
        if not persistent.pivo_default_7dl:
            textbutton translation_new["SAVE"]:
                style "log_button"
                text_style "settings_link"
                xalign 0.02
                yalign 0.08
                action ShowMenu('save')
            textbutton translation_new["LOAD"]:
                style "log_button"
                text_style "settings_link"
                xalign 0.98
                yalign 0.08
                action ShowMenu('load')
        hbox:
            xalign 0.5
            yalign 0.08
            add get_image("gui/settings/star.png"):
                yalign 0.65
            text " "+translation_new["settings"]+" ":
                style "settings_link"
                yalign 0.5
                color "#ffffff"
            add get_image("gui/settings/star.png"):
                yalign 0.65
        if not persistent.pivo_default_7dl:
            textbutton translation_new["Back"]:
                style "log_button"
                text_style "settings_link"
                xalign 0.015
                yalign 0.92
                action Return()
        else:
            textbutton translation_new["Back"]:
                style "log_button"
                text_style "settings_link"
                xalign 0.015
                yalign 0.92
                action [Hide("alt_preferences"), Return()]
        side "c b r":
            area (0.25, 0.23, 0.51, 0.71)
            viewport:
                id "preferences"
                mousewheel True
                scrollbars None
                grid 1 grid_y_val:
                    xfill True
                    spacing 15
                    if persistent.pivo_default_7dl and (plthr != "Меню"):
                        if not use_settings_7dl:
                            textbutton "Показать меню 7ДЛ:LA":
                                style "log_button"
                                text_style "settings_header"
                                xalign 0.5
                                action SetVariable("use_settings_7dl", True)
                        else:
                            textbutton "Скрыть меню 7ДЛ:LA":
                                style "log_button"
                                text_style "settings_header"
                                xalign 0.5
                                action SetVariable("use_settings_7dl", False)
                    text translation_new["Window_mode"]:
                        style "settings_header"
                        xalign 0.5
                    grid 2 1:
                        xfill True
                        hbox:
                            xalign 0.5
                            if _preferences.fullscreen:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Fullscreen"]:
                                style "log_button"
                                text_style "settings_text"
                                action Preference("display", "fullscreen")
                        hbox:
                            xalign 0.5
                            if not _preferences.fullscreen:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Window"]:
                                style "log_button"
                                text_style "settings_text"
                                action Preference("display", "window")
                    text translation_new["Skip"]:
                        style "settings_header"
                        xalign 0.5
                    grid 2 1:
                        xfill True
                        hbox:
                            xalign 0.5
                            if _preferences.skip_unseen:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Skip_all"]:
                                style "log_button"
                                text_style "settings_text"
                                action Preference("skip", "all")
                        hbox:
                            xalign 0.5
                            if not _preferences.skip_unseen:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Skip_seen"]:
                                style "log_button"
                                text_style "settings_text"
                                action Preference("skip", "seen")
                    text translation_new["Volume"]:
                        style "settings_header"
                        xalign 0.5
                    grid 2 1:
                        xfill True
                        textbutton translation_new["Music_lower"]:
                            style "log_button"
                            text_style "settings_text"
                            action Play("sound", "sound/test.ogg")
                            xpos 0.1
                        bar:
                            value Preference("music volume")
                            left_bar bar_full
                            right_bar bar_null
                            thumb "images/gui/settings/htumb.png"
                            hover_thumb "images/gui/settings/htumb.png"
                            xmaximum 1.35
                            ymaximum 36
                            xpos -0.55
                    grid 2 1:
                        xfill True
                        textbutton translation_new["Sound"]:
                            style "log_button"
                            text_style "settings_text"
                            action Play("sound", "sound/test.ogg")
                            xpos 0.1
                        bar:
                            value Preference("sound volume")
                            left_bar bar_full
                            right_bar bar_null
                            thumb "images/gui/settings/htumb.png"
                            hover_thumb "images/gui/settings/htumb.png"
                            xmaximum 1.35
                            ymaximum 36
                            xpos -0.55
                    grid 2 1:
                        xfill True
                        textbutton translation_new["Ambience"]:
                            style "log_button"
                            text_style "settings_text"
                            action Play("sound", "sound/test.ogg")
                            xpos 0.1
                        bar:
                            value Preference("voice volume")
                            left_bar bar_full
                            right_bar bar_null
                            thumb "images/gui/settings/htumb.png"
                            hover_thumb "images/gui/settings/htumb.png"
                            xmaximum 1.35
                            ymaximum 36
                            xpos -0.55
                    text translation_new["Text_speed"]:
                        style "settings_header"
                        xalign 0.5
                    bar:
                        value Preference("text speed")
                        left_bar bar_full
                        right_bar bar_null
                        thumb "images/gui/settings/htumb.png"
                        hover_thumb "images/gui/settings/htumb.png"
                        xalign 0.5
                        xmaximum 0.8
                        ymaximum 36
                    text translation_new["Autoforward"]:
                        style "settings_header"
                        xalign 0.5
                    grid 2 1:
                        xfill True
                        hbox:
                            xalign 0.5
                            if _preferences.afm_time != 0:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Adult_content_on"]:
                                style "log_button"
                                text_style "settings_text"
                                action Preference("auto-forward after click", "enable")
                        hbox:
                            xalign 0.5
                            if _preferences.afm_time == 0:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Adult_content_off"]:
                                style "log_button"
                                text_style "settings_text"
                                action (Preference("auto-forward time", 0), Preference("auto-forward after click", "disable"))
                    text translation_new["Autoforward_time"]:
                        style "settings_header"
                        xalign 0.5
                    bar:
                        value Preference("auto-forward time")
                        left_bar bar_full
                        right_bar bar_null
                        thumb "images/gui/settings/htumb.png"
                        hover_thumb "images/gui/settings/htumb.png"
                        xalign 0.5
                        xmaximum 0.8
                        ymaximum 36
                    text translation_new["Font"]:
                        style "settings_header"
                        xalign 0.5
                    grid 2 1:
                        xfill True
                        hbox:
                            xalign 0.5
                            if persistent.font_size == "small":
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Normal_font"]:
                                style "log_button"
                                text_style "settings_text"
                                action SetField(persistent, "font_size", "small")
                        hbox:
                            xalign 0.5
                            if not persistent.font_size == "small":
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Big_font"]:
                                style "log_button"
                                text_style "settings_text"
                                action SetField(persistent, "font_size", "large")
                    textbutton translation_new["Language"]:
                        style "log_button"
                        text_style "settings_text"
                        text_size 50
                        xalign 0.5
                        action ShowMenu("language_menu")
                    text translation_new["show_achievments"]:
                        style "settings_header"
                        xalign 0.5
                    grid 2 1:
                        xfill True
                        hbox:
                            xalign 0.5
                            if persistent.show_achievements:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Yes"]:
                                style "log_button"
                                text_style "settings_text"
                                action SetField(persistent, "show_achievements", True)
                        hbox:
                            xalign 0.5
                            if not persistent.show_achievements:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["No"]:
                                style "log_button"
                                text_style "settings_text"
                                action SetField(persistent, "show_achievements", False)
                    null
            bar:
                value XScrollValue("preferences")
                left_bar "images/misc/none.png"
                right_bar "images/misc/none.png"
                thumb "images/misc/none.png"
                hover_thumb "images/misc/none.png"
            vbar:
                value YScrollValue("preferences")
                bottom_bar "images/misc/none.png"
                top_bar "images/misc/none.png"
                thumb "images/gui/settings/vthumb.png"
                thumb_offset -12
    if use_settings_7dl:
        use settings_7dl(embedded=True)

screen alt_save:
    tag menu
    modal True
    timer 0.01 action FilePage(701)
    window:
        background get_image("gui/save_load/save_bg.jpg")
        hbox:
            xalign 0.5
            yalign 0.08
            add get_image("gui/settings/star.png"):
                yalign 0.65
            text " "+translation_new["SAVE"]+" ":
                style "settings_link"
                yalign 0.5
                color "#ffffff"
            add get_image("gui/settings/star.png"):
                yalign 0.65
        textbutton translation_new["Back"]:
            style "log_button"
            text_style "settings_link"
            xalign 0.015
            yalign 0.92
            action [Hide("alt_save"), Return()]
        textbutton translation_new["Save_game"]:
            style "log_button"
            text_style "settings_link"
            yalign 0.92
            xalign 0.5
            action (FunctionCallback(on_save_callback, selected_slot), FileSave(selected_slot))
        textbutton "{size=-12}{b}x{/b} {/size}"+translation_new["Delete"]:
            style "log_button"
            text_style "settings_link"
            yalign 0.92
            xalign 0.97
            action FileDelete(selected_slot)
        vbox:
            xanchor 0.0
            xcenter 0.03
            ycenter 0.5
            ymaximum 0.57
            viewport:
                mousewheel True
                scrollbars None
                grid 1 99:
                    for i in range(701, 800):
                        textbutton str(i-700):
                            text_size 50
                            right_padding 50
                            style "log_button"
                            text_style "settings_link"
                            action (FilePage(i), SetVariable("selected_slot", False))
        grid 4 3:
            xpos 0.13
            ypos 0.2
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True
            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i):
                        xpos 10
                        ypos 10
                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "save_load_button"
                        fixed:
                            text ( "%s." % i + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation_new["Empty_slot"]) + "\n" +FileSaveName(i)):
                                style "file_picker_text"
                                xpos 15
                                ypos 15

screen alt_load:
    tag menu
    modal True
    timer 0.01 action FilePage(701)
    window:
        background get_image("gui/save_load/load_bg.jpg")
        hbox:
            xalign 0.5
            yalign 0.08
            add get_image("gui/settings/star.png"):
                yalign 0.65
            text " "+translation_new["LOAD"]+" ":
                style "settings_link"
                yalign 0.5
                color "#ffffff"
            add get_image("gui/settings/star.png"):
                yalign 0.65
        textbutton translation_new["Back"]:
            style "log_button"
            text_style "settings_link"
            xalign 0.015
            yalign 0.92
            action [Hide("alt_load"), Return()]
        textbutton translation_new["Load_game"]:
            style "log_button"
            text_style "settings_link"
            yalign 0.92
            xalign 0.5
            action (FunctionCallback(on_load_callback,selected_slot), FileLoad(selected_slot))
        textbutton "{size=-12}{b}x{/b} {/size}"+translation_new["Delete"]:
            style "log_button"
            text_style "settings_link"
            yalign 0.92
            xalign 0.97
            action FileDelete(selected_slot)
        vbox:
            xanchor 0.0
            xcenter 0.03
            ycenter 0.5
            ymaximum 0.57
            viewport:
                mousewheel True
                scrollbars None
                grid 1 100:
                    textbutton translation_new["Auto"]:
                        text_size 50
                        style "log_button"
                        text_style "settings_link"
                        action (FilePage("auto"), SetVariable("selected_slot", False))
                    for i in range(701, 800):
                        textbutton str(i-700):
                            text_size 50
                            right_padding 50
                            style "log_button"
                            text_style "settings_link"
                            action (FilePage(i), SetVariable("selected_slot", False))
        grid 4 3:
            xpos 0.13
            ypos 0.2
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True
            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i):
                        xpos 10
                        ypos 10
                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "save_load_button"
                        fixed:
                            text ( "%s." % i + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation_new["Empty_slot"]) + "\n" +FileSaveName(i)):
                                style "file_picker_text"
                                xpos 15
                                ypos 15

screen replay_text_history_screen:
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
        background Frame("images/gui/choice/"+persistent.timeofday+"/choice_box.png")
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
                    text h.what:
                        style "normal_day"
                        size history_text_size
                        xmaximum xmax
                        xpos 100
        vbar:
            value YScrollValue("text_history_screen")
            bottom_bar "images/misc/none.png"
            top_bar "images/misc/none.png"
            thumb "images/gui/settings/vthumb.png"
            xoffset 1700

screen replay_preferences:
    tag menu
    modal True
    $ bar_null = Frame(get_image("gui/settings/bar_null.png"),36,36)
    $ bar_full = Frame(get_image("gui/settings/bar_full.png"),36,36)
    window:
        background get_image("gui/settings/preferences_bg.jpg")
        hbox:
            xalign 0.5
            yalign 0.08
            add get_image("gui/settings/star.png"):
                yalign 0.65
            text " "+translation_new["settings"]+" ":
                style "settings_link"
                yalign 0.5
                color "#ffffff"
            add get_image("gui/settings/star.png"):
                yalign 0.65
        textbutton translation_new["Back"]:
            style "log_button"
            text_style "settings_link"
            xalign 0.015
            yalign 0.92
            action Return()
        side "c b r":
            area (0.25, 0.23, 0.51, 0.71)
            viewport:
                id "preferences"
                mousewheel True
                scrollbars None
                grid 1 21:
                    xfill True
                    spacing 15
                    textbutton "Выйти из повтора":
                        style "log_button"
                        text_style "settings_header"
                        xalign 0.5
                        action [Function(replay_screens_load), EndReplay(confirm=False)]
                    text translation_new["Window_mode"]:
                        style "settings_header"
                        xalign 0.5
                    grid 2 1:
                        xfill True
                        hbox:
                            xalign 0.5
                            if _preferences.fullscreen:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Fullscreen"]:
                                style "log_button"
                                text_style "settings_text"
                                action Preference("display", "fullscreen")
                        hbox:
                            xalign 0.5
                            if not _preferences.fullscreen:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Window"]:
                                style "log_button"
                                text_style "settings_text"
                                action Preference("display", "window")
                    text translation_new["Skip"]:
                        style "settings_header"
                        xalign 0.5
                    grid 2 1:
                        xfill True
                        hbox:
                            xalign 0.5
                            if _preferences.skip_unseen:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Skip_all"]:
                                style "log_button"
                                text_style "settings_text"
                                action Preference("skip", "all")
                        hbox:
                            xalign 0.5
                            if not _preferences.skip_unseen:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Skip_seen"]:
                                style "log_button"
                                text_style "settings_text"
                                action Preference("skip", "seen")
                    text translation_new["Volume"]:
                        style "settings_header"
                        xalign 0.5
                    grid 2 1:
                        xfill True
                        textbutton translation_new["Music_lower"]:
                            style "log_button"
                            text_style "settings_text"
                            action Play("sound", "sound/test.ogg")
                            xpos 0.1
                        bar:
                            value Preference("music volume")
                            left_bar bar_full
                            right_bar bar_null
                            thumb "images/gui/settings/htumb.png"
                            hover_thumb "images/gui/settings/htumb.png"
                            xmaximum 1.35
                            ymaximum 36
                            xpos -0.55
                    grid 2 1:
                        xfill True
                        textbutton translation_new["Sound"]:
                            style "log_button"
                            text_style "settings_text"
                            action Play("sound", "sound/test.ogg")
                            xpos 0.1
                        bar:
                            value Preference("sound volume")
                            left_bar bar_full
                            right_bar bar_null
                            thumb "images/gui/settings/htumb.png"
                            hover_thumb "images/gui/settings/htumb.png"
                            xmaximum 1.35
                            ymaximum 36
                            xpos -0.55
                    grid 2 1:
                        xfill True
                        textbutton translation_new["Ambience"]:
                            style "log_button"
                            text_style "settings_text"
                            action Play("sound", "sound/test.ogg")
                            xpos 0.1
                        bar:
                            value Preference("voice volume")
                            left_bar bar_full
                            right_bar bar_null
                            thumb "images/gui/settings/htumb.png"
                            hover_thumb "images/gui/settings/htumb.png"
                            xmaximum 1.35
                            ymaximum 36
                            xpos -0.55
                    text translation_new["Text_speed"]:
                        style "settings_header"
                        xalign 0.5
                    bar:
                        value Preference("text speed")
                        left_bar bar_full
                        right_bar bar_null
                        thumb "images/gui/settings/htumb.png"
                        hover_thumb "images/gui/settings/htumb.png"
                        xalign 0.5
                        xmaximum 0.8
                        ymaximum 36
                    text translation_new["Autoforward"]:
                        style "settings_header"
                        xalign 0.5
                    grid 2 1:
                        xfill True
                        hbox:
                            xalign 0.5
                            if _preferences.afm_time != 0:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Adult_content_on"]:
                                style "log_button"
                                text_style "settings_text"
                                action Preference("auto-forward after click", "enable")
                        hbox:
                            xalign 0.5
                            if _preferences.afm_time == 0:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Adult_content_off"]:
                                style "log_button"
                                text_style "settings_text"
                                action (Preference("auto-forward time", 0), Preference("auto-forward after click", "disable"))
                    text translation_new["Autoforward_time"]:
                        style "settings_header"
                        xalign 0.5
                    bar:
                        value Preference("auto-forward time")
                        left_bar bar_full
                        right_bar bar_null
                        thumb "images/gui/settings/htumb.png"
                        hover_thumb "images/gui/settings/htumb.png"
                        xalign 0.5
                        xmaximum 0.8
                        ymaximum 36
                    text translation_new["Font"]:
                        style "settings_header"
                        xalign 0.5
                    grid 2 1:
                        xfill True
                        hbox:
                            xalign 0.5
                            if persistent.font_size == "small":
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Normal_font"]:
                                style "log_button"
                                text_style "settings_text"
                                action SetField(persistent, "font_size", "small")
                        hbox:
                            xalign 0.5
                            if not persistent.font_size == "small":
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Big_font"]:
                                style "log_button"
                                text_style "settings_text"
                                action SetField(persistent, "font_size", "large")
                    textbutton translation_new["Language"]:
                        style "log_button"
                        text_style "settings_text"
                        text_size 50
                        xalign 0.5
                        action ShowMenu("language_menu")
                    text translation_new["show_achievments"]:
                        style "settings_header"
                        xalign 0.5
                    grid 2 1:
                        xfill True
                        hbox:
                            xalign 0.5
                            if persistent.show_achievements:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Yes"]:
                                style "log_button"
                                text_style "settings_text"
                                action SetField(persistent, "show_achievements", True)
                        hbox:
                            xalign 0.5
                            if not persistent.show_achievements:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["No"]:
                                style "log_button"
                                text_style "settings_text"
                                action SetField(persistent, "show_achievements", False)
                    null
            bar:
                value XScrollValue("preferences")
                left_bar "images/misc/none.png"
                right_bar "images/misc/none.png"
                thumb "images/misc/none.png"
                hover_thumb "images/misc/none.png"
            vbar:
                value YScrollValue("preferences")
                bottom_bar "images/misc/none.png"
                top_bar "images/misc/none.png"
                thumb "images/gui/settings/vthumb.png"
                thumb_offset -12
