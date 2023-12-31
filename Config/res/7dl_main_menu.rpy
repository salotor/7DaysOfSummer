init 1 python:
    presentscript_font = default_7dl_path + "Pics/fonts/presentscript.ttf"
    control_freak_upset_font = default_7dl_path + "Pics/fonts/ContFU.ttf"

    style.alt_settings_textbutton = Style(style.base_font)
    style.alt_settings_textbutton.font  = presentscript_font
    style.alt_settings_textbutton.size = 37
    style.alt_settings_textbutton.kerning = -2
    style.alt_settings_textbutton.color = "#2f059a"
    style.alt_settings_textbutton.hover_color = "#9a0505"
    style.alt_settings_textbutton.selected_color = "#2f059a"
    style.alt_settings_textbutton.selected_idle_color = "#2f059a"
    style.alt_settings_textbutton.selected_hover_color = "#9a0505"
    style.alt_settings_textbutton.insensitive_color = "#2f059a"

    style.alt_settings_text = Style(style.base_font)
    style.alt_settings_text.font  = presentscript_font
    style.alt_settings_text.size = 37
    style.alt_settings_text.kerning = -2
    style.alt_settings_text.color = "#2f059a"

    style.alt_version_text = Style(style.base_font)
    style.alt_version_text.font  = control_freak_upset_font
    style.alt_version_text.size = 20

    sdl_cheat_watcher_on = False

    #def check_time_7dl(time_7dl):
        #from time import localtime, strftime
        #t = strftime("%H:%M:%S", localtime())
        #hour, min, sec = t.split(":")
        #hour = int(hour)
        #if hour in (6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18):
            #time_7dl = "day"
            #return time_7dl
        #elif hour in (19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5):
            #time_7dl = "night"
            #return time_7dl

    def get_menu_track_7dl():
        if (persistent.waifu_7dl == 'un'):
            return music_7dl["take_my_hand"]
        elif (persistent.waifu_7dl == 'sl'):
            return music_7dl["slavyas_fantazm"]
        elif (persistent.waifu_7dl == 'dv'):
            return music_7dl["sheiscool"]
        elif (persistent.waifu_7dl == 'mi'):
            return music_7dl["tellyourworld"]
        elif (persistent.waifu_7dl == 'us'):
            return music_7dl["thousand_of_pixies"]
        elif (persistent.waifu_7dl == 'mt'):
            return music_7dl["wheres_wonderland"]
        elif (persistent.waifu_7dl == 'uv'):
            return music_7dl["uvao2"]

init 1:
    if not persistent.list_waifu_7dl: # дефайним список фонов в меню
        $ persistent.list_waifu_7dl = []
    #$ time_7dl = ""
    image bg un_bg_7dl = get_image_7dl("gui/menu_main/un_bg.jpg")
    image bg sl_bg_7dl = get_image_7dl("gui/menu_main/sl_bg.jpg")
    image bg dv_bg_7dl = get_image_7dl("gui/menu_main/dv_bg.jpg")
    image bg mi_bg_7dl = get_image_7dl("gui/menu_main/mi_bg.jpg")
    image bg us_bg_7dl = get_image_7dl("gui/menu_main/us_bg.jpg")
    image bg mt_bg_7dl = get_image_7dl("gui/menu_main/mt_bg.jpg")
    image bg uv_bg_7dl = get_image_7dl("gui/menu_main/uv_bg.jpg")

transform left_menu_7dl(xal, yal):
    xalign -0.1
    alpha 0.0
    easein 1 xalign xal alpha 1.0

screen alt_changelog:
    modal True
    add get_image_7dl("gui/menu_elem/changelog_bg.png")
    text "{size=35}{u}General information regarding translation:{/u}{/size}\n\n\nThis is a first test version of the translation,\n it was made by using online translator then fixed manually.\nWe also added notifications for local stuff and jokes.\nMost of it was proofread and fixed to an acceptable state\nBut please remember that there could be any kind of errors.\nIf you found one or have any questions, please leave them on:\n{a=https://steamcommunity.com/sharedfiles/filedetails/?id=441054187&searchtext=}workshop page{/a} or {a=https://discord.com/invite/qd8drECDHp}discord{/a}\n\n{u}Useful links{/u}\n{a=https://steamcommunity.com/workshop/filedetails/discussion/441054187/3762229949257518764/}Steam topic{/a}\n{a=https://boosty.to/7dlla}Boosty{/a}\n{a=https://docs.google.com/document/d/1BxW93oXhYJpLn3iIav-kqxKscjxRQaqBnubuMYNniLU/edit?usp=sharing}FAQ{/a}\n{a=https://docs.google.com/document/d/1IiImL_c2R-CSoffJdtRp5ePF3yxZ-xuMQJhHcCbkz8E/edit?usp=sharing}Guides{/a}":
        text_align 0.5
        xcenter 0.5
        ycenter 0.5
        xmaximum 880
        color "#64483c"
        font header_font
        size 30
    textbutton _("OK"):
        text_size 60
        style "log_button"
        text_style "settings_link"
        xcenter 0.5
        ycenter 980
        action [Hide("alt_changelog", transition=Dissolve(0.5))]

screen settings_widget_lp_on_7dl():
    text "Enable widget for" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "progress monitoring" xpos 0.653 ypos 0.646:
        style "alt_settings_text"
    text "and mod information" xpos 0.653 ypos 0.692:
        style "alt_settings_text"
    text "(Girls' points included)." xpos 0.653 ypos 0.738:
        style "alt_settings_text"

screen settings_widget_lp_off_7dl():
    text "Disable widget for" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "progress monitoring" xpos 0.653 ypos 0.646:
        style "alt_settings_text"
    text "and mod information" xpos 0.653 ypos 0.692:
        style "alt_settings_text"
    text "(Girls' points included)." xpos 0.653 ypos 0.738:
        style "alt_settings_text"

screen settings_widget_music_on_7dl():
    text "Enable widget for" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "music that plays" xpos 0.653 ypos 0.646:
        style "alt_settings_text"
    text "right now." xpos 0.653 ypos 0.692:
        style "alt_settings_text"

screen settings_widget_music_off_7dl():
    text "Disable widget for" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "music that plays" xpos 0.653 ypos 0.646:
        style "alt_settings_text"
    text "right now." xpos 0.653 ypos 0.692:
        style "alt_settings_text"

screen settings_hentai_graphics_on_7dl():
    text "Enable 18+ visuals and" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "remove sprite censorship." xpos 0.653 ypos 0.646:
        style "alt_settings_text"
    text "Available for all" xpos 0.653 ypos 0.692:
        style "alt_settings_text"
    text "current scenes." xpos 0.653 ypos 0.738:
        style "alt_settings_text"

screen settings_hentai_graphics_off_7dl():
    text "Disable 18+ visuals and" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "add censorship to" xpos 0.653 ypos 0.646:
        style "alt_settings_text"
    text "sprites." xpos 0.653 ypos 0.692:
        style "alt_settings_text"

screen settings_chapter_on_7dl():
    text "Enable splashcreen at" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "label start." xpos 0.653 ypos 0.646:
        style "alt_settings_text"

screen settings_chapter_off_7dl():
    text "Disable splashscreen at" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "label start." xpos 0.653 ypos 0.646:
        style "alt_settings_text"

screen settings_achv_sprite_emo_on_7dl():
    text "Enable character's emotions" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "in the achievelist." xpos 0.653 ypos 0.646:
        style "alt_settings_text"

screen settings_achv_sprite_emo_off_7dl():
    text "Disable character's emotions" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "in the achievelist." xpos 0.653 ypos 0.646:
        style "alt_settings_text"

screen settings_thoughts_tilde_on_7dl():
    text "Change thoughts design" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "to tilde" xpos 0.653 ypos 0.646:
        style "alt_settings_text"

screen settings_thoughts_tilde_off_7dl():
    text "Change thoughts design" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "to quotations." xpos 0.653 ypos 0.646:
        style "alt_settings_text"

screen menu_7dl():
    imagemap at left_menu_7dl(0.1, 0.7):
        alpha False
        if persistent.waifu_7dl == 'un':
            auto get_image_7dl("gui/menu_main/un_menu_%s.png")
        elif persistent.waifu_7dl == 'sl':
            auto get_image_7dl("gui/menu_main/sl_menu_%s.png")
        elif persistent.waifu_7dl == 'dv':
            auto get_image_7dl("gui/menu_main/dv_menu_%s.png")
        elif persistent.waifu_7dl == 'mi':
            auto get_image_7dl("gui/menu_main/mi_menu_%s.png")
        elif persistent.waifu_7dl == 'us':
            auto get_image_7dl("gui/menu_main/us_menu_%s.png")
        elif persistent.waifu_7dl == 'mt':
            auto get_image_7dl("gui/menu_main/mt_menu_%s.png")
        elif persistent.waifu_7dl == 'uv':
            auto get_image_7dl("gui/menu_main/uv_menu_%s.png")
        hotspot (168, 507, 248, 37):
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=2), SetField(sdl_mus_engine, "is_active", False), Jump("start_7dl")]
        hotspot (168, 558, 187, 47):
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            action [Show("settings_7dl", transition=Dissolve(0.2))]
        hotspot (168, 613, 323, 37):
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Jump("sdl_achvlist_main")]
        hotspot (168, 666, 197, 36):
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            action [Show("contacts_7dl", transition=Dissolve(0.2))]
        hotspot (168, 719, 148, 37):
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Jump("alt_stories_start")]
        hotspot (168, 772, 140, 37):
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            action [Show("media_7dl", transition=Dissolve(0.2))]
        hotspot (168, 824, 225, 39):
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Function(alt_exit), MainMenu(confirm=False)]

    # Открываем экран для ввода чит-кодов
    key "~" action Show("sdl_cheat_reader")
    key "+" action SetVariable("sdl_cheat_watcher_on", True)
    if sdl_cheat_watcher_on:
        use sdl_cheat_watcher

    # Чейнджлог
    imagebutton xcenter 1890 ycenter 1046:
        if persistent.waifu_7dl == 'un':
            auto get_image_7dl("gui/menu_elem/mail/un_mail_%s.png")
        elif persistent.waifu_7dl == 'sl':
            auto get_image_7dl("gui/menu_elem/mail/sl_mail_%s.png")
        elif persistent.waifu_7dl == 'dv':
            auto get_image_7dl("gui/menu_elem/mail/dv_mail_%s.png")
        elif persistent.waifu_7dl == 'mi':
            auto get_image_7dl("gui/menu_elem/mail/mi_mail_%s.png")
        elif persistent.waifu_7dl == 'us':
            auto get_image_7dl("gui/menu_elem/mail/us_mail_%s.png")
        elif persistent.waifu_7dl == 'mt':
            auto get_image_7dl("gui/menu_elem/mail/mt_mail_%s.png")
        elif persistent.waifu_7dl == 'uv':
            auto get_image_7dl("gui/menu_elem/mail/uv_mail_%s.png")
        hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
        action [Show("alt_changelog", transition=Dissolve(0.2))]

    # Указываем номер версии
    if persistent.waifu_7dl == 'un':
        if alt_hotfix_no != "":
            text "v.[alt_release_no].[alt_hotfix_no]"    style "alt_version_text" xcenter 1810 ycenter 1055 color "#FFFFFF" outlines [ (absolute(1), "#D456FF", absolute(0), absolute(0)) ]
        else:
            text "v.[alt_release_no]"                    style "alt_version_text" xcenter 1810 ycenter 1055 color "#FFFFFF" outlines [ (absolute(1), "#D456FF", absolute(0), absolute(0)) ]
    elif persistent.waifu_7dl == 'sl':
        if alt_hotfix_no != "":
            text "v.[alt_release_no].[alt_hotfix_no]"    style "alt_version_text" xcenter 1810 ycenter 1055 color "#FFFFFF" outlines [ (absolute(1), "#AA8700", absolute(0), absolute(0)) ]
        else:
            text "v.[alt_release_no]"                    style "alt_version_text" xcenter 1810 ycenter 1055 color "#FFFFFF" outlines [ (absolute(1), "#AA8700", absolute(0), absolute(0)) ]
    elif persistent.waifu_7dl == 'dv':
        if alt_hotfix_no != "":
            text "v.[alt_release_no].[alt_hotfix_no]"    style "alt_version_text" xcenter 1810 ycenter 1055 color "#FFFFFF" outlines [ (absolute(1), "#FF7F00", absolute(0), absolute(0)) ]
        else:
            text "v.[alt_release_no]"                    style "alt_version_text" xcenter 1810 ycenter 1055 color "#FFFFFF" outlines [ (absolute(1), "#FF7F00", absolute(0), absolute(0)) ]
    elif persistent.waifu_7dl == 'mi':
        if alt_hotfix_no != "":
            text "v.[alt_release_no].[alt_hotfix_no]"    style "alt_version_text" xcenter 1810 ycenter 1055 color "#FFFFFF" outlines [ (absolute(1), "#1A9183", absolute(0), absolute(0)) ]
        else:
            text "v.[alt_release_no]"                    style "alt_version_text" xcenter 1810 ycenter 1055 color "#FFFFFF" outlines [ (absolute(1), "#1A9183", absolute(0), absolute(0)) ]
    elif persistent.waifu_7dl == 'us':
        if alt_hotfix_no != "":
            text "v.[alt_release_no].[alt_hotfix_no]"    style "alt_version_text" xcenter 1810 ycenter 1055 color "#FFFFFF" outlines [ (absolute(1), "#FF0000", absolute(0), absolute(0)) ]
        else:
            text "v.[alt_release_no]"                    style "alt_version_text" xcenter 1810 ycenter 1055 color "#FFFFFF" outlines [ (absolute(1), "#FF0000", absolute(0), absolute(0)) ]
    elif persistent.waifu_7dl == 'mt':
        if alt_hotfix_no != "":
            text "v.[alt_release_no].[alt_hotfix_no]"    style "alt_version_text" xcenter 1810 ycenter 1055 color "#FFFFFF" outlines [ (absolute(1), "#00EA00", absolute(0), absolute(0)) ]
        else:
            text "v.[alt_release_no]"                    style "alt_version_text" xcenter 1810 ycenter 1055 color "#FFFFFF" outlines [ (absolute(1), "#00EA00", absolute(0), absolute(0)) ]
    elif persistent.waifu_7dl == 'uv':
        if alt_hotfix_no != "":
            text "v.[alt_release_no].[alt_hotfix_no]"    style "alt_version_text" xcenter 1810 ycenter 1055 color "#FFFFFF" outlines [ (absolute(1), "#00EA00", absolute(0), absolute(0)) ]
        else:
            text "v.[alt_release_no]"                    style "alt_version_text" xcenter 1810 ycenter 1055 color "#FFFFFF" outlines [ (absolute(1), "#00EA00", absolute(0), absolute(0)) ]

    # Панелька плеера
    if sdl_mus_engine.is_active:
        use music_panel_7dl(default_music=get_menu_track_7dl())

    on "show" action SetVariable("sdl_cheat_watcher_on", False)
    on "hide" action SetVariable("sdl_cheat_watcher_on", False)

screen settings_7dl():
    tag menu
    add get_image_7dl("gui/menu_elem/settings/settings_bg.png")
    if not persistent.lp_widget_7dl:
        textbutton "Widget (LP): off." xpos 0.65 ypos 0.255:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_widget_lp_on_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_widget_lp_on_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'lp_widget_7dl', True), Hide("settings_widget_lp_on_7dl", transition=Dissolve(0.2)), Show("settings_widget_lp_off_7dl", transition=Dissolve(0.2))]
    else:
        textbutton "Widget (LP): on." xpos 0.65 ypos 0.255:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_widget_lp_off_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_widget_lp_off_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'lp_widget_7dl', False), Hide("settings_widget_lp_off_7dl", transition=Dissolve(0.2)), Show("settings_widget_lp_on_7dl", transition=Dissolve(0.2))]
    if not persistent.music_widget_7dl:
        textbutton "Widget (music): off." xpos 0.65 ypos 0.3:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_widget_music_on_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_widget_music_on_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'music_widget_7dl', True), Hide("settings_widget_music_on_7dl", transition=Dissolve(0.2)), Show("settings_widget_music_off_7dl", transition=Dissolve(0.2))]
    else:
        textbutton "Widget (Music): on." xpos 0.65 ypos 0.3:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_widget_music_off_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_widget_music_off_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'music_widget_7dl', False), Hide("settings_widget_music_off_7dl", transition=Dissolve(0.2)), Show("settings_widget_music_on_7dl", transition=Dissolve(0.2))]
    if not persistent.thoughts_tilde_7dl:
        textbutton "Thoughts: quotations" xpos 0.65 ypos 0.347:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_thoughts_tilde_on_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_thoughts_tilde_on_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'thoughts_tilde_7dl',True), Hide("settings_thoughts_tilde_on_7dl", transition=Dissolve(0.2)), Show("settings_thoughts_tilde_off_7dl", transition=Dissolve(0.2))]
    else:
        textbutton "Thoughts: tilde" xpos 0.65 ypos 0.347:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_thoughts_tilde_off_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_thoughts_tilde_off_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'thoughts_tilde_7dl',False), Hide("settings_thoughts_tilde_off_7dl", transition=Dissolve(0.2)), Show("settings_thoughts_tilde_on_7dl", transition=Dissolve(0.2))]
    if not persistent.hentai_graphics_7dl:
        textbutton "Hentai-content: Off." xpos 0.65 ypos 0.392:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_hentai_graphics_on_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_hentai_graphics_on_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'hentai_graphics_7dl',True), Hide("settings_hentai_graphics_on_7dl", transition=Dissolve(0.2)), Show("settings_hentai_graphics_off_7dl", transition=Dissolve(0.2))]
    else:
        textbutton "Hentai-content: on." xpos 0.65 ypos 0.392:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_hentai_graphics_off_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_hentai_graphics_off_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'hentai_graphics_7dl',False), Hide("settings_hentai_graphics_off_7dl", transition=Dissolve(0.2)), Show("settings_hentai_graphics_on_7dl", transition=Dissolve(0.2))]
    if not persistent.chapter_off_7dl:
        textbutton "Splashcreen: on." xpos 0.65 ypos 0.438:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_chapter_off_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_chapter_off_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'chapter_off_7dl',True), Hide("settings_chapter_off_7dl", transition=Dissolve(0.2)), Show("settings_chapter_on_7dl", transition=Dissolve(0.2))]
    else:
        textbutton "Splashcreen: off." xpos 0.65 ypos 0.438:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_chapter_on_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_chapter_on_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'chapter_off_7dl',False), Hide("settings_chapter_on_7dl", transition=Dissolve(0.2)), Show("settings_chapter_off_7dl", transition=Dissolve(0.2))]
    if not persistent.achv_sprite_emo_7dl:
        textbutton "Emotions (Achievelist): off." xpos 0.65 ypos 0.483:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_achv_sprite_emo_on_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_achv_sprite_emo_on_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'achv_sprite_emo_7dl',True), Hide("settings_achv_sprite_emo_on_7dl", transition=Dissolve(0.2)), Show("settings_achv_sprite_emo_off_7dl", transition=Dissolve(0.2))]
    else:
        textbutton "Emotions (Achievelist): on." xpos 0.65 ypos 0.483:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_achv_sprite_emo_off_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_achv_sprite_emo_off_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'achv_sprite_emo_7dl',False), Hide("settings_achv_sprite_emo_off_7dl", transition=Dissolve(0.2)), Show("settings_achv_sprite_emo_on_7dl", transition=Dissolve(0.2))]

screen contacts_7dl():
    tag menu
    imagemap xalign 0.9 yalign 0.7:
        auto get_image_7dl("gui/menu_elem/contacts/contacts_%s.png")
        hotspot(1265, 330, 329, 59):
            action OpenURL("https://vk.com/bl_7dl")
        hotspot(1265, 389, 329, 59):
            action OpenURL("https://vk.com/page-128046483_52530462")
        hotspot(1265, 449, 329, 59):
            action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=441054187")

screen media_7dl():
    tag menu
    imagemap:
        auto get_image_7dl("gui/menu_elem/media/media_%s.png")
        hotspot(1218, 384, 700, 700):
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            clicked [Hide("media_7dl", transition=Dissolve(0.2)), Hide("menu_7dl", transition=Dissolve(0.2)), Jump("alt_gallery_start")]
    add get_image_7dl("gui/menu_elem/media/media_player.png") xpos 1254 ypos 214
    imagebutton xpos 1652 ypos 253:
        auto get_image_7dl("gui/menu_elem/media/media_player_on_%s.png")
        hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
        action [Hide("media_7dl", transition=Dissolve(0.2)), Show("music_7dl", transition=Dissolve(0.2), default_music=get_menu_track_7dl())]

label main_menu_7dl:
    stop ambience
    stop sound
    stop sound_loop

    $ plthr = u"Menu"
    call alt_vars
    $ renpy.block_rollback()
    $ day_time()
    jump random_bg_7dl

label random_bg_7dl:
    if ((len(persistent.list_waifu_7dl) >= 6) and ('uv' not in persistent.list_waifu_7dl)) or (len(persistent.list_waifu_7dl) >= 7):
        $ persistent.list_waifu_7dl = []
    if not persistent.waifu_7dl:
        if renpy.random.randint(1, 95) == 1:
            $ persistent.waifu_7dl = 'uv'
            $ sdl_persistent_inc("got_lucky_7dl") # повезло, повезло
        else:
            $ persistent.waifu_7dl = renpy.random.choice(['un', 'sl', 'dv', 'mi', 'us', 'mt'])
    if (persistent.waifu_7dl == 'un') and ('un' not in persistent.list_waifu_7dl):
        scene bg un_bg_7dl with fade
    elif (persistent.waifu_7dl == 'sl') and ('sl' not in persistent.list_waifu_7dl):
        scene bg sl_bg_7dl with fade
    elif (persistent.waifu_7dl == 'dv') and ('dv' not in persistent.list_waifu_7dl):
        scene bg dv_bg_7dl with fade
    elif (persistent.waifu_7dl == 'mi') and ('mi' not in persistent.list_waifu_7dl):
        scene bg mi_bg_7dl with fade
    elif (persistent.waifu_7dl == 'us') and ('us' not in persistent.list_waifu_7dl):
        scene bg us_bg_7dl with fade
    elif (persistent.waifu_7dl == 'mt') and ('mt' not in persistent.list_waifu_7dl):
        scene bg mt_bg_7dl with fade
    elif (persistent.waifu_7dl == 'uv') and ('uv' not in persistent.list_waifu_7dl):
        scene bg uv_bg_7dl with fade
    else:
        $ persistent.waifu_7dl = False
        jump random_bg_7dl
    if not sdl_mus_engine.is_active:
        play music get_menu_track_7dl() fadein 3
    if not persistent.alt_changelog_050: # список изменений для 0.50
        show screen alt_changelog
        $ persistent.alt_changelog_050 = True
        $ renpy.pause(0.1)
    call screen menu_7dl

label start_7dl:
# режим окон - автоматический
    window auto
# переименовываем персонажей
    $ make_names_unknown_7dl()
    if not persistent.thoughts_tilde_7dl:
        $ th_prefix = "«"
        $ th_suffix = "»"
    $ reload_names()
# отмечаем, что переменные "спасать" не нужно
    call alt_vars_saved
# вызываем переменные
    call alt_vars
# вызываем сценарий
    call alt_day0_prologue
    jump main_menu_7dl

label alt_7dl_titles:
    scene black with dissolve2
    pause(1)
    show alt_credits alt_credits_text:
        xalign 0.5
        ypos 1.0
        linear 50.0 ypos -5.5
    $ renpy.pause(48, hard = True)
    stop music fadeout 5
    show alt_credits "The End":
        xcenter 0.5
        ycenter 0.5
    with dissolve2
    $ renpy.pause(3, hard = True)
    scene black with fade
    if (not alt_replay_on) and persistent.waifu_7dl: # если вышли на титры с игры
        $ persistent.list_waifu_7dl.append(persistent.waifu_7dl) # записываем текущий фон в меню в список
        if routetag[:2] in ('un', 'sl', 'dv', 'mi', 'us', 'mt', 'uv'):
            python:
                try:
                    persistent.list_waifu_7dl.remove(routetag[:2]) # пытаемся удалить фон девочки из списка
                except Exception:
                    pass
            $ persistent.waifu_7dl = routetag[:2] # текущий фон в меню = фон девочки из текущего рута
        else:
            $ persistent.waifu_7dl = False # обнуляем текущий фон в меню
    return
