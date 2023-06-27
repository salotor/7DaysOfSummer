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

    $ alt_changelog_text = "{size=35}{u}Список изменений в версии 0.51:{/u}{/size}\n- написан шестой день рута Семёна-Одиночки (“обычная” ветка);\n- добавлено 11 новых иллюстраций;\n- изменениям подверглись некоторые концовки и сцены в вышедших рутах (подробности по ссылке ниже);\n- добавлена концовка в рут Мику-дж;\n- добавлена возможность замены меню БЛ на меню 7ДЛ:ЛА;\n- множество прочих менее масштабных изменений, весь список {a=https://vk.com/@bl_7dl-spisok-izmenenii-obnovleniya-051}здесь{/a}.\n\nЧтобы быть в курсе последних новостей, подписывайтесь на наши ресурсы: {a=https://vk.com/bl_7dl}группа ВКонтакте{/a}, {a=https://t.me/sevendaysofbeer}канал в Телеграме{/a}, {a=https://discord.gg/qd8drECDHp}сервер в Дискорде{/a}\n\nСтраница со схемами и гайдами для прохождения {a=https://vk.com/page-128046483_52527656}здесь{/a}"

transform left_menu_7dl(xal, yal):
    xalign -0.1
    alpha 0.0
    easein 1 xalign xal alpha 1.0

screen alt_changelog(alt_text):
    modal True
    add get_image_7dl("gui/menu_elem/changelog_bg.png")
    text alt_text:
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

screen alt_copy_saves(msg, fnkt):
    modal True
    add get_image("gui/o_rly/base.png")
    text msg:
        text_align 0.5
        yalign 0.46
        xalign 0.5
        xmaximum 0.45
        color "#64483c"
        font header_font
        size 30
    textbutton translation_new["Yes"]:
        text_size 60
        style "log_button"
        text_style "settings_link"
        yalign 0.65
        xalign 0.3
        action [Hide("alt_copy_saves", Dissolve(0.5)), Function(fnkt), Show("alt_confirm_reload", Dissolve(0.5), True)]
    textbutton translation_new["No"]:
        text_size 60
        style "log_button"
        text_style "settings_link"
        yalign 0.65
        xalign 0.7
        action [Hide("alt_copy_saves", Dissolve(0.5)), Show("alt_confirm_reload", Dissolve(0.5), False)]

screen alt_confirm_reload(saves_copied):
    modal True
    if saves_copied:
        $ alt_text = "Скопировано "+str(alt_copy_counter)+" сохранений из "+str(alt_safe_counter)+". Игра будет перезапущена."
    else:
        $ alt_text = "Игра будет перезапущена."
    add get_image("gui/o_rly/base.png")
    text alt_text:
        text_align 0.5
        yalign 0.46
        xalign 0.5
        xmaximum 0.45
        color "#64483c"
        font header_font
        size 30
    textbutton _("OK"):
        text_size 60
        style "log_button"
        text_style "settings_link"
        xalign 0.5
        yalign 0.65
        action [Function(renpy.music.stop), Function(renpy.utter_restart)]

screen menu_7dl():
    imagemap at left_menu_7dl(0.1, 0.7):
        alpha False
        if not persistent.pivo_default_7dl:
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
            hotspot (170, 511, 299, 33):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=2), SetField(sdl_mus_engine, "is_active", False), Jump("start_7dl")]
            hotspot (170, 558, 243, 39):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("settings_7dl", transition=Dissolve(0.2), embedded=False)]
            hotspot (170, 617, 293, 38):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Jump("sdl_achvlist_main")]
            hotspot (170, 670, 221, 33):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("contacts_7dl", transition=Dissolve(0.2))]
            hotspot (170, 723, 190, 33):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Jump("alt_stories_start")]
            hotspot (170, 776, 143, 33):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("media_7dl", transition=Dissolve(0.2))]
            hotspot (170, 823, 137, 39):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Function(alt_exit), MainMenu(confirm=False)]
        else:
            if persistent.waifu_7dl == 'un':
                auto get_image_7dl("gui/menu_main/un_menu_def_%s.png")
            elif persistent.waifu_7dl == 'sl':
                auto get_image_7dl("gui/menu_main/sl_menu_def_%s.png")
            elif persistent.waifu_7dl == 'dv':
                auto get_image_7dl("gui/menu_main/dv_menu_def_%s.png")
            elif persistent.waifu_7dl == 'mi':
                auto get_image_7dl("gui/menu_main/mi_menu_def_%s.png")
            elif persistent.waifu_7dl == 'us':
                auto get_image_7dl("gui/menu_main/us_menu_def_%s.png")
            elif persistent.waifu_7dl == 'mt':
                auto get_image_7dl("gui/menu_main/mt_menu_def_%s.png")
            elif persistent.waifu_7dl == 'uv':
                auto get_image_7dl("gui/menu_main/uv_menu_def_%s.png")
            hotspot (170, 511, 299, 33):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=2), SetField(sdl_mus_engine, "is_active", False), Start()]
            hotspot (170, 563, 238, 33):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Show('alt_load')]
            hotspot (170, 610, 243, 39):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("settings_7dl", transition=Dissolve(0.2), embedded=False)]
            hotspot (170, 669, 293, 38):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Jump("sdl_achvlist_main")]
            hotspot (170, 722, 221, 33):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("contacts_7dl", transition=Dissolve(0.2))]
            hotspot (170, 775, 190, 33):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Jump("alt_stories_start")]
            hotspot (170, 828, 143, 33):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("media_7dl", transition=Dissolve(0.2))]
            hotspot (170, 874, 137, 39):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Quit(confirm=False)]
            if persistent.alt_config_developer:
                hotspot (1673, 81, 214, 120):
                    hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                    action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Start("scenario__sdl_selector")]
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
        action [Show("alt_changelog", Dissolve(0.2), alt_changelog_text)]

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

screen settings_description_7dl(alt_text="", embedded=False):
    if embedded:
        $ xpos_val = 0.75
        $ ypos_val = 0.682
    else:
        $ xpos_val = 0.65
        $ ypos_val = 0.642
    text alt_text xpos xpos_val ypos ypos_val:
        style "alt_settings_text"
        xmaximum 400
        line_spacing 10

screen settings_7dl(embedded=False):
    tag menu
    $ pos_no = 0
    if embedded:
        $ xpos_val = 0.75
        $ ypos_val = 0.223
        $ xpos_bg_val = 0.1
        $ ypos_bg_val = 0.04
    else:
        $ xpos_val = 0.65
        $ ypos_val = 0.209
        $ xpos_bg_val = 0.0
        $ ypos_bg_val = 0.0
    add get_image_7dl("gui/menu_elem/settings/settings_bg.png") xpos xpos_bg_val ypos ypos_bg_val
    if persistent.pivo_default_7dl and (not embedded):
        $ pos_no += 1
        textbutton "Настройки БЛ" xpos xpos_val ypos ypos_val+0.0455*pos_no:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_description_7dl", Dissolve(0.2), "Открыть собственные настройки Бесконечного лета", embedded)
            unhovered [Hide("settings_description_7dl", transition=Dissolve(0.2))]
            action [Hide("settings_description_7dl", transition=Dissolve(0.2)), Show("alt_preferences", transition=Dissolve(0.2))]
    $ pos_no += 1
    if not persistent.pivo_default_7dl:
        textbutton "Старт с 7ДЛ:LA: выкл." xpos xpos_val ypos ypos_val+0.0455*pos_no:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_description_7dl", Dissolve(0.2), "Заменить стартовое меню БЛ на меню 7ДЛ:LA.", embedded)
            unhovered [Hide("settings_description_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'pivo_default_7dl',True), Show("alt_copy_saves", Dissolve(0.2), "В этом режиме у мода включаются свои слоты под сохранения. Скопировать сохранения мода из слотов БЛ в собственные слоты? Сохранения будут записаны последовательно в пустые слоты.", alt_saves_copy_in)]
    else:
        textbutton "Старт с 7ДЛ:LA: вкл." xpos xpos_val ypos ypos_val+0.0455*pos_no:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_description_7dl", Dissolve(0.2), "Вернуть стартовое меню БЛ вместо меню 7ДЛ:LA.", embedded)
            unhovered [Hide("settings_description_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'pivo_default_7dl',False), Show("alt_copy_saves", Dissolve(0.2), "Скопировать сохранения мода из собственных слотов в слоты БЛ? Сохранения будут записаны последовательно в пустые слоты.", alt_saves_copy_out)]
    $ pos_no += 1
    if not persistent.hentai_graphics_7dl:
        textbutton "Х-графика: выкл." xpos xpos_val ypos ypos_val+0.0455*pos_no:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_description_7dl", Dissolve(0.2), "Включить 18+ арты и убрать цензуру со спрайтов. Доступно не для всех сцен.", embedded)
            unhovered [Hide("settings_description_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'hentai_graphics_7dl',True), Hide("settings_description_7dl", transition=Dissolve(0.2))]
    else:
        textbutton "Х-графика: вкл." xpos xpos_val ypos ypos_val+0.0455*pos_no:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_description_7dl", Dissolve(0.2), "Выключить 18+ арты и добавить цензуру на спрайты.", embedded)
            unhovered [Hide("settings_description_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'hentai_graphics_7dl',False), Hide("settings_description_7dl", transition=Dissolve(0.2))]
    $ pos_no += 1
    if not persistent.lp_widget_7dl:
        textbutton "Виджет (ЛП): выкл." xpos xpos_val ypos ypos_val+0.0455*pos_no:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_description_7dl", Dissolve(0.2), "Включить виджет для отображения прогресса и информации по моду (в т.ч. очков отношений).", embedded)
            unhovered [Hide("settings_description_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'lp_widget_7dl', True), Hide("settings_description_7dl", transition=Dissolve(0.2))]
    else:
        textbutton "Виджет (ЛП): вкл." xpos xpos_val ypos ypos_val+0.0455*pos_no:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_description_7dl", Dissolve(0.2), "Выключить виджет для отображения прогресса и информации по моду (в т.ч. очков отношений).", embedded)
            unhovered [Hide("settings_description_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'lp_widget_7dl', False), Hide("settings_description_7dl", transition=Dissolve(0.2))]
    $ pos_no += 1
    if not persistent.music_widget_7dl:
        textbutton "Виджет (музыка): выкл." xpos xpos_val ypos ypos_val+0.0455*pos_no:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_description_7dl", Dissolve(0.2), "Включить виджет для отображения музыки, играющей в данный момент.", embedded)
            unhovered [Hide("settings_description_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'music_widget_7dl', True), Hide("settings_description_7dl", transition=Dissolve(0.2))]
    else:
        textbutton "Виджет (музыка): вкл." xpos xpos_val ypos ypos_val+0.0455*pos_no:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_description_7dl", Dissolve(0.2), "Выключить виджет для отображения музыки, играющей в данный момент.", embedded)
            unhovered [Hide("settings_description_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'music_widget_7dl', False), Hide("settings_description_7dl", transition=Dissolve(0.2))]
    $ pos_no += 1
    if not persistent.thoughts_tilde_7dl:
        textbutton "Мысли героя: кавычки" xpos xpos_val ypos ypos_val+0.0455*pos_no:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_description_7dl", Dissolve(0.2), "Переключить оформление мыслей героя на тильды.", embedded)
            unhovered [Hide("settings_description_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'thoughts_tilde_7dl',True), Function(alt_thoughts_tilde_update), Function(reload_names), Hide("settings_description_7dl", transition=Dissolve(0.2))]
    else:
        textbutton "Мысли героя: тильды" xpos xpos_val ypos ypos_val+0.0455*pos_no:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_description_7dl", Dissolve(0.2), "Переключить оформление мыслей героя на кавычки.", embedded)
            unhovered [Hide("settings_description_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'thoughts_tilde_7dl',False), Function(alt_thoughts_tilde_update), Function(reload_names), Hide("settings_description_7dl", transition=Dissolve(0.2))]
    $ pos_no += 1
    if not persistent.chapter_off_7dl:
        textbutton "Заставки: вкл." xpos xpos_val ypos ypos_val+0.0455*pos_no:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_description_7dl", Dissolve(0.2), "Выключить заставки в начале глав.", embedded)
            unhovered [Hide("settings_description_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'chapter_off_7dl',True), Hide("settings_description_7dl", transition=Dissolve(0.2))]
    else:
        textbutton "Заставки: выкл." xpos xpos_val ypos ypos_val+0.0455*pos_no:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_description_7dl", Dissolve(0.2), "Включить заставки в начале глав.", embedded)
            unhovered [Hide("settings_description_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'chapter_off_7dl',False), Hide("settings_description_7dl", transition=Dissolve(0.2))]
    $ pos_no += 1
    if not persistent.achv_sprite_emo_7dl:
        textbutton "Эмоции (ачивлист): выкл." xpos xpos_val ypos ypos_val+0.0455*pos_no:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_description_7dl", Dissolve(0.2), "Включить смену эмоций персонажей в ачивлисте.", embedded)
            unhovered [Hide("settings_description_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'achv_sprite_emo_7dl',True), Hide("settings_description_7dl", transition=Dissolve(0.2))]
    else:
        textbutton "Эмоции (ачивлист): вкл." xpos xpos_val ypos ypos_val+0.0455*pos_no:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_description_7dl", Dissolve(0.2), "Выключить смену эмоций персонажей в ачивлисте.", embedded)
            unhovered [Hide("settings_description_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'achv_sprite_emo_7dl',False), Hide("settings_description_7dl", transition=Dissolve(0.2))]

screen contacts_7dl():
    tag menu
    imagemap xalign 0.9 yalign 0.7:
        auto get_image_7dl("gui/menu_elem/contacts/contacts_%s.png")
        hotspot(1265, 330, 329, 59):
            action OpenURL("https://boosty.to/7dlla")
        hotspot(1265, 390, 329, 59):
            action OpenURL("https://vk.com/bl_7dl")
        hotspot(1265, 450, 329, 59):
            action OpenURL("https://t.me/sevendaysofbeer")
        hotspot(1265, 510, 329, 59):
            action OpenURL("https://discord.com/invite/qd8drECDHp")
        hotspot(1265, 570, 329, 59):
            action OpenURL("https://www.youtube.com/@7dlLA")
        hotspot(1265, 630, 329, 59):
            action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=441054187")

screen media_7dl():
    tag menu
    imagebutton xpos 1254 ypos 384:
        auto get_image_7dl("gui/menu_elem/media/media_%s.png")
        hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
        action [Hide("media_7dl", transition=Dissolve(0.2)), Hide("menu_7dl", transition=Dissolve(0.2)), Jump("sdl_gall_start")]
    imagebutton xpos 1254 ypos 214:
        auto get_image_7dl("gui/menu_elem/media/media_player_%s.png")
        hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
        action [Hide("media_7dl", transition=Dissolve(0.2)), Function(sdl_mus_progress_calc), Show("music_7dl", transition=Dissolve(0.2), default_music=get_menu_track_7dl())]

label main_menu_7dl:
    stop ambience
    stop sound
    stop sound_loop

    $ plthr = u"Меню"
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
    if persistent.alt_changelog != "0.51":
        show screen alt_changelog(alt_changelog_text)
        $ persistent.alt_changelog = "0.51"
        $ renpy.pause(0.1)
    call screen menu_7dl

label start_7dl:
# режим окон - автоматический
    window auto
# переименовываем персонажей
    $ make_names_unknown_7dl()
    $ alt_thoughts_tilde_update()
    $ reload_names()
# отмечаем, что переменные "спасать" не нужно
    call alt_vars_saved
# вызываем переменные
    call alt_vars
# вызываем сценарий
    call alt_day0_prologue
    if not persistent.pivo_default_7dl:
        jump main_menu_7dl
    else:
        return

label alt_7dl_titles:
    if not alt_replay_on: # если вышли на титры с игры
        scene black with dissolve2
        pause(1)
        show alt_credits alt_credits_text:
            xalign 0.5
            ypos 1.0
            linear 40.0 ypos -4.8
        $ renpy.pause(40, hard = True)
        show alt_credits "Отдельная огромная благодарность нашим донатерам:":
            xcenter 0.5
            ycenter 0.1
        $ alt_show_donators(alt_donator_list)
        stop music fadeout 5
        show alt_credits "КОНЕЦ":
            xcenter 0.5
            ycenter 0.5
        with dissolve2
        $ renpy.pause(3, hard = True)
        scene black with fade
        if persistent.waifu_7dl:
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
    else:
        stop music fadeout 2
        scene black with fade2
    return
