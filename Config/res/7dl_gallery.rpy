init 1:
    $ page_7dl = 1
    $ max_bgs_page_7dl = 11
    $ max_arts_page_7dl = 16
    $ max_un_page_7dl = 3
    $ max_sl_page_7dl = 2
    $ max_dv_page_7dl = 3
    $ max_mi_page_7dl = 4
    $ max_us_page_7dl = 2
    $ max_mt_page_7dl = 1

    $ show_image_7dl = ""
    $ show_image2_7dl = ""
    $ show_image3_7dl = ""
    $ show_image4_7dl = ""
    $ gallery_mode_7dl = ""

    $ style.page_7dl_text = Style(style.default)
    $ style.page_7dl_text.font  = get_image_7dl("fonts/a_AvanteLtNr.ttf")
    $ style.page_7dl_text.color = "#ffffff"
    $ style.page_7dl_text.size = 60

    image bg gallery_7dl = get_image_7dl("gui/gallery/gallery_bg.png")
    $ locked_img_7dl = ["gallery_stub_1.png", "gallery_stub_2.png", "gallery_stub_3.png"]

    $ list_gallery_cg_7dl = []
    $ list_gallery_bg_7dl = []
    $ alt_slide_show = False

screen gallery_main_7dl:
    add get_image_7dl("gui/gallery/gallery_bg.png")
    if not gallery_mode_7dl == "bgs":
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_bgs_%s.png") xalign 0.31 yalign 0.029
            action [Show("bgs_7dl_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), Show("slide_show_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "bgs"), SetVariable("page_7dl", 1)]
    else:
        add get_image_7dl("gui/gallery/gallery_navig_bgs_hover.png") xalign 0.31 yalign 0.029
    if not gallery_mode_7dl == "arts":
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_arts_%s.png") xalign 0.733 yalign 0.032
            action [Show("arts_7dl_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), Show("slide_show_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "arts"), SetVariable("page_7dl", 1)]
    else:
        add get_image_7dl("gui/gallery/gallery_navig_arts_hover.png") xalign 0.733 yalign 0.032
    if not (gallery_mode_7dl == "bgs"):
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_filter_%s.png") xcenter 0.917 ycenter 0.148
            action [Show("filter_settings_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "filter"), SetVariable("page_7dl", 1)]
    if gallery_mode_7dl == "arts":
        timer 0.01 action [Show("arts_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), Show("slide_show_7dl", transition=Dissolve(0.2)), Show("gallery_exit_7dl", transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "bgs":
        timer 0.01 action [Show("bgs_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), Show("slide_show_7dl", transition=Dissolve(0.2)), Show("gallery_exit_7dl", transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "filter":
        timer 0.01 action [Show("filter_settings_7dl", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), Show("gallery_exit_7dl", transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "un":
        timer 0.01 action [Show("arts_7dl_un_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), Show("gallery_exit_7dl", transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "sl":
        timer 0.01 action [Show("arts_7dl_sl_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), Show("gallery_exit_7dl", transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "dv":
        timer 0.01 action [Show("arts_7dl_dv_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), Show("gallery_exit_7dl", transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "mi":
        timer 0.01 action [Show("arts_7dl_mi_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), Show("gallery_exit_7dl", transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "us":
        timer 0.01 action [Show("arts_7dl_us_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), Show("gallery_exit_7dl", transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "mt":
        timer 0.01 action [Show("arts_7dl_mt_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), Show("gallery_exit_7dl", transition=Dissolve(0.2))]

    # Панелька плеера
    if sdl_mus_engine.is_active:
        use music_panel_7dl(default_music=music_7dl["more_than_alive"])

screen gallery_exit_7dl:
    if alt_slide_show:
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971
            action [Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("alt_slide_show", False), Jump("alt_gallery")]
    elif gallery_mode_7dl == "bgs":
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971
            action [Hide("bgs_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", ""), SetVariable("page_7dl", 1), Jump("main_menu_7dl")]
    elif gallery_mode_7dl == "arts":
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971
            action [Hide("arts_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", ""), SetVariable("page_7dl", 1), Jump("main_menu_7dl")]
    elif gallery_mode_7dl == "filter":
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971
            action [Hide("filter_settings_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", ""), SetVariable("page_7dl", 1), Jump("main_menu_7dl")]
    elif gallery_mode_7dl == "un":
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971
            action [Hide("arts_7dl_un_%s" % str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", ""), SetVariable("page_7dl", 1), Jump("main_menu_7dl")]
    elif gallery_mode_7dl == "sl":
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971
            action [Hide("arts_7dl_sl_%s" % str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", ""), SetVariable("page_7dl", 1), Jump("main_menu_7dl")]
    elif gallery_mode_7dl == "dv":
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971
            action [Hide("arts_7dl_dv_%s" % str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", ""), SetVariable("page_7dl", 1), Jump("main_menu_7dl")]
    elif gallery_mode_7dl == "mi":
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971
            action [Hide("arts_7dl_mi_%s" % str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", ""), SetVariable("page_7dl", 1), Jump("main_menu_7dl")]
    elif gallery_mode_7dl == "us":
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971
            action [Hide("arts_7dl_us_%s" % str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", ""), SetVariable("page_7dl", 1), Jump("main_menu_7dl")]
    elif gallery_mode_7dl == "mt":
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971
            action [Hide("arts_7dl_mt_%s" % str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", ""), SetVariable("page_7dl", 1), Jump("main_menu_7dl")]

screen gallery_bw_7dl:
    if gallery_mode_7dl == "bgs":
        if not renpy.get_screen("bgs_7dl_1"):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5
                action [SetVariable("page_7dl", page_7dl-1), Hide("bgs_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("bgs_7dl_%s" % str(page_7dl-1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "arts":
        if not renpy.get_screen("arts_7dl_1"):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5
                action [SetVariable("page_7dl", page_7dl-1), Hide("arts_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_%s" % str(page_7dl-1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "un":
        if not renpy.get_screen("arts_7dl_un_1"):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5
                action [SetVariable("page_7dl", page_7dl-1), Hide("arts_7dl_un_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_un_%s" % str(page_7dl-1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "sl":
        if not renpy.get_screen("arts_7dl_sl_1"):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5
                action [SetVariable("page_7dl", page_7dl-1), Hide("arts_7dl_sl_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_sl_%s" % str(page_7dl-1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "dv":
        if not renpy.get_screen("arts_7dl_dv_1"):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5
                action [SetVariable("page_7dl", page_7dl-1), Hide("arts_7dl_dv_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_dv_%s" % str(page_7dl-1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "mi":
        if not renpy.get_screen("arts_7dl_mi_1"):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5
                action [SetVariable("page_7dl", page_7dl-1), Hide("arts_7dl_mi_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_mi_%s" % str(page_7dl-1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "us":
        if not renpy.get_screen("arts_7dl_us_1"):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5
                action [SetVariable("page_7dl", page_7dl-1), Hide("arts_7dl_us_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_us_%s" % str(page_7dl-1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "mt":
        if not renpy.get_screen("arts_7dl_mt_1"):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5
                action [SetVariable("page_7dl", page_7dl-1), Hide("arts_7dl_mt_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_mt_%s" % str(page_7dl-1), transition=Dissolve(0.2))]

screen gallery_fw_7dl:
    if gallery_mode_7dl == "bgs":
        if not renpy.get_screen("bgs_7dl_%s" % str(max_bgs_page_7dl)):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5
                action [SetVariable("page_7dl", page_7dl+1), Hide("bgs_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("bgs_7dl_%s" % str(page_7dl+1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "arts":
        if not renpy.get_screen("arts_7dl_%s" % str(max_arts_page_7dl)):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5
                action [SetVariable("page_7dl", page_7dl+1), Hide("arts_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_%s" % str(page_7dl+1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "un":
        if not renpy.get_screen("arts_7dl_un_%s" % str(max_un_page_7dl)):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5
                action [SetVariable("page_7dl", page_7dl+1), Hide("arts_7dl_un_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_un_%s" % str(page_7dl+1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "sl":
        if not renpy.get_screen("arts_7dl_sl_%s" % str(max_sl_page_7dl)):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5
                action [SetVariable("page_7dl", page_7dl+1), Hide("arts_7dl_sl_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_sl_%s" % str(page_7dl+1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "dv":
        if not renpy.get_screen("arts_7dl_dv_%s" % str(max_dv_page_7dl)):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5
                action [SetVariable("page_7dl", page_7dl+1), Hide("arts_7dl_dv_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_dv_%s" % str(page_7dl+1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "mi":
        if not renpy.get_screen("arts_7dl_mi_%s" % str(max_mi_page_7dl)):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5
                action [SetVariable("page_7dl", page_7dl+1), Hide("arts_7dl_mi_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_mi_%s" % str(page_7dl+1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "us":
        if not renpy.get_screen("arts_7dl_us_%s" % str(max_us_page_7dl)):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5
                action [SetVariable("page_7dl", page_7dl+1), Hide("arts_7dl_us_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_us_%s" % str(page_7dl+1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "mt":
        if not renpy.get_screen("arts_7dl_mt_%s" % str(max_mt_page_7dl)):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5
                action [SetVariable("page_7dl", page_7dl+1), Hide("arts_7dl_mt_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_mt_%s" % str(page_7dl+1), transition=Dissolve(0.2))]

screen filter_settings_7dl:
    tag menu
    imagebutton:
        auto get_image_7dl("gui/gallery/filter/gallery_filter_un_%s.png") xalign 0.19 yalign 0.15
        action [Hide("filter_settings_7dl", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "un"), SetVariable("page_7dl", 1), Show("arts_7dl_un_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))]
    imagebutton:
        auto get_image_7dl("gui/gallery/filter/gallery_filter_sl_%s.png") xalign 0.5 yalign 0.15
        action [Hide("filter_settings_7dl", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "sl"), SetVariable("page_7dl", 1), Show("arts_7dl_sl_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))]
    imagebutton:
        auto get_image_7dl("gui/gallery/filter/gallery_filter_dv_%s.png") xalign 0.8 yalign 0.15
        action [Hide("filter_settings_7dl", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "dv"), SetVariable("page_7dl", 1), Show("arts_7dl_dv_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))]
    imagebutton:
        auto get_image_7dl("gui/gallery/filter/gallery_filter_mi_%s.png") xalign 0.2 yalign 0.93
        action [Hide("filter_settings_7dl", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "mi"), SetVariable("page_7dl", 1), Show("arts_7dl_mi_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))]
    imagebutton:
        auto get_image_7dl("gui/gallery/filter/gallery_filter_us_%s.png") xalign 0.5 yalign 0.93
        action [Hide("filter_settings_7dl", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "us"), SetVariable("page_7dl", 1), Show("arts_7dl_us_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))]
    imagebutton:
        auto get_image_7dl("gui/gallery/filter/gallery_filter_mt_%s.png") xalign 0.8 yalign 0.93
        action [Hide("filter_settings_7dl", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "mt"), SetVariable("page_7dl", 1), Show("arts_7dl_mt_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))]

screen slide_show_7dl:
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_navig_slide_show_%s.png") xcenter 1761 ycenter 280
        if gallery_mode_7dl == "bgs":
            action [Hide("bgs_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Jump("bg_slide_show_7dl")]
        elif gallery_mode_7dl == "arts":
            action [Hide("arts_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Jump("cg_slide_show_7dl")]

screen bgs_7dl_1:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_adductius_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_adductius_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_adductius_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_backdoor_day_7dl") or renpy.seen_image("bg ext_backdoor_sunset_7dl") or renpy.seen_image("bg ext_backdoor_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_backdoor_day_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_backdoor_day_7dl"), SetVariable("show_image2_7dl", "bg ext_backdoor_sunset_7dl"), SetVariable("show_image3_7dl", "bg ext_backdoor_night_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("bg ext_backroad_day_7dl") or renpy.seen_image("bg ext_backroad_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_backroad_day_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_backroad_day_7dl"), SetVariable("show_image2_7dl", "bg ext_backroad_sunset_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_boathouse_alt_day_7dl") or renpy.seen_image("bg ext_boathouse_alt_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_boathouse_alt_day_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_boathouse_alt_day_7dl"), SetVariable("show_image2_7dl", "bg ext_boathouse_alt_night_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_busstop_dust_7dl") or renpy.seen_image("bg ext_busstop_sun_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_busstop_dust_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_busstop_dust_7dl"), SetVariable("show_image2_7dl", "bg ext_busstop_sun_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_city_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_city_night_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_city_night_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen bgs_7dl_2:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_entrance_night_clear_7dl") or renpy.seen_image("bg ext_entrance_night_clear_closed_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_entrance_night_clear_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_entrance_night_clear_7dl"), SetVariable("show_image2_7dl", "bg ext_entrance_night_clear_closed_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_lake_day_7dl") or renpy.seen_image("bg ext_lake_night_7dl") or renpy.seen_image("bg ext_lake_sunset_7dl") or renpy.seen_image("bg ext_lake_night_px_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_lake_day_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_lake_day_7dl"), SetVariable("show_image2_7dl", "bg ext_lake_night_7dl"), SetVariable("show_image3_7dl", "bg ext_lake_sunset_7dl"), SetVariable("show_image4_7dl", "bg ext_lake_night_px_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("bg ext_mv2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_mv2_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_mv2_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_railbridge_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_railbridge_sunset_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_railbridge_sunset_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_sandpit_day_7dl") or renpy.seen_image("bg ext_sandpit_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_sandpit_day_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_sandpit_day_7dl"), SetVariable("show_image2_7dl", "bg ext_sandpit_night_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_shower_night_7dl") or renpy.seen_image("bg ext_shower_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_shower_night_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_shower_night_7dl"), SetVariable("show_image2_7dl", "bg ext_shower_day_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen bgs_7dl_3:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_tennis_court_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_tennis_court_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_tennis_court_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_townscape_ph_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_townscape_ph_day_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_townscape_ph_day_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("bg ext_un_hideout_day_7dl") or renpy.seen_image("bg ext_un_hideout_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_un_hideout_day_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_un_hideout_day_7dl"), SetVariable("show_image2_7dl", "bg ext_un_hideout_night_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_volley_court_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_volley_court_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_volley_court_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg int_access2_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_access2_day_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_access2_day_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_admins_day_7dl") or renpy.seen_image("bg ext_admins_night_7dl") or renpy.seen_image("bg ext_admins_rain_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_admins_day_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_admins_day_7dl"), SetVariable("show_image2_7dl", "bg ext_admins_night_7dl"), SetVariable("show_image3_7dl", "bg ext_admins_rain_7dl"), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen bgs_7dl_4:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg int_chief_office_day_7dl") or renpy.seen_image("bg int_chief_office_rain_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_chief_office_day_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_chief_office_day_7dl"), SetVariable("show_image2_7dl", "bg int_chief_office_rain_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg int_editorial_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_editorial_day_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_editorial_day_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("bg int_home_lift_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_home_lift_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_home_lift_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg int_mt_sam_room_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_mt_sam_room_7dl_%s.png")xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_mt_sam_room_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg int_mt_sam_room_away_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_mt_sam_room_away_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_mt_sam_room_away_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg int_mt_sam_room_close_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_mt_sam_room_close_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_mt_sam_room_close_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen bgs_7dl_5:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg int_hospital_hall_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_hospital_hall_day_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_hospital_hall_day_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg int_potato_storage_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_potato_storage_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_potato_storage_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("bg int_sporthall_day_7dl") or renpy.seen_image("bg int_sporthall_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_sporthall_day_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_sporthall_day_7dl"), SetVariable("show_image2_7dl", "bg int_sporthall_night_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg int_store_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_store_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_store_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg int_train_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_train_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_train_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg int_wardrobe_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_wardrobe_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_wardrobe_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen bgs_7dl_6:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg int_wardrobe2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_wardrobe2_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_wardrobe2_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg int_warehouse_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_warehouse_day_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_warehouse_day_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("bg int_warehouse_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_warehouse_night_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_warehouse_night_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_japan_graveyard_rain_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_japan_graveyard_rain_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_japan_graveyard_rain_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_khruschevka_day_7dl") or renpy.seen_image("bg ext_khruschevka_night_7dl") or renpy.seen_image("bg ext_khruschevka_rain_7dl") or renpy.seen_image("bg ext_khruschevka_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_khruschevka_day_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_khruschevka_day_7dl"), SetVariable("show_image2_7dl", "bg ext_khruschevka_night_7dl"), SetVariable("show_image3_7dl", "bg ext_khruschevka_rain_7dl"), SetVariable("show_image4_7dl", "bg ext_khruschevka_sunset_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_winter_night_7dl") or renpy.seen_image("bg ext_winter_night_rotate_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_winter_night_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_winter_night_7dl"), SetVariable("show_image2_7dl", "bg ext_winter_night_rotate_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen bgs_7dl_7:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_winterpark_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_winterpark_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_winterpark_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg int_excalator_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_excalator_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_excalator_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("bg int_excalator2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_excalator2_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_excalator2_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg int_refinery_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_refinery_day_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_refinery_day_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_valun_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_valun_day_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_valun_day_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_countryside_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_countryside_day_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_countryside_day_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen bgs_7dl_8:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_dining_hall_backroad_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_dining_hall_backroad_day_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_dining_hall_backroad_day_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_dv_hideout_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_dv_hideout_day_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_dv_hideout_day_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("bg int_semen_room_window_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_semen_room_window_day_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_semen_room_window_day_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_warehouse_day_7dl") or renpy.seen_image("bg ext_warehouse_night_7dl") or renpy.seen_image("bg ext_warehouse_sunset_7dl") or renpy.seen_image("bg ext_warehouse_rain_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_warehouse_day_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_warehouse_day_7dl"), SetVariable("show_image2_7dl", "bg ext_warehouse_night_7dl"), SetVariable("show_image3_7dl", "bg ext_warehouse_sunset_7dl"), SetVariable("show_image4_7dl", "bg ext_warehouse_rain_day_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_warehouse2_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_warehouse2_day_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_warehouse2_day_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg int_coupe_day_7dl") or renpy.seen_image("bg int_coupe_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_coupe_day_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_coupe_day_7dl"), SetVariable("show_image2_7dl", "bg int_coupe_night_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen bgs_7dl_9:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_childhouse_day_7dl") or renpy.seen_image("bg ext_childhouse_winter_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_childhouse_day_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_childhouse_day_7dl"), SetVariable("show_image2_7dl", "bg ext_childhouse_winter_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg int_wagon_day_7dl") or renpy.seen_image("bg int_wagon_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_wagon_day_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_wagon_day_7dl"), SetVariable("show_image2_7dl", "bg int_wagon_sunset_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("bg int_childhouse_room_day_7dl") or renpy.seen_image("bg int_childhouse_room_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_childhouse_room_day_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_childhouse_room_day_7dl"), SetVariable("show_image2_7dl", "bg int_childhouse_room_night_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg int_hospital_corridor_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_hospital_corridor_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_hospital_corridor_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_bush_day_7dl") or renpy.seen_image("bg ext_bush_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_bush_day_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_bush_day_7dl"), SetVariable("show_image2_7dl", "bg ext_bush_sunset_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_smolensky_graveyard_winter_7dl") or renpy.seen_image("bg ext_smolensky_graveyard_winter_day_7dl") or renpy.seen_image("bg ext_smolensky_graveyard_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_smolensky_graveyard_winter_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_smolensky_graveyard_winter_7dl"), SetVariable("show_image2_7dl", "bg ext_smolensky_graveyard_winter_day_7dl"), SetVariable("show_image3_7dl", "bg ext_smolensky_graveyard_day_7dl"), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen bgs_7dl_10:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_square2_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_square2_day_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_square2_day_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_tree_house_7dl") or renpy.seen_image("bg ext_tree_house_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_tree_house_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_tree_house_7dl"), SetVariable("show_image2_7dl", "bg ext_tree_house_sunset_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("bg int_tree_house_7dl") or renpy.seen_image("bg int_tree_house_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_tree_house_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_tree_house_7dl"), SetVariable("show_image2_7dl", "bg int_tree_house_sunset_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg int_warehouse_day2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_warehouse_day2_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_warehouse_day2_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg int_admins_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_admins_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_admins_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg int_clubs_dj_7dl") or renpy.seen_image("bg int_clubs_dj_nolight_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_clubs_dj_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_clubs_dj_7dl"), SetVariable("show_image2_7dl", "bg int_clubs_dj_nolight_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen bgs_7dl_11:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg int_staircase_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_staircase_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_staircase_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_townscape_ph2_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_townscape_ph2_day_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_townscape_ph2_day_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    # if renpy.seen_image("bg ctrlv3"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/bgs/ctrlv3_%s.png") xalign 0.8 yalign 0.15
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ctrlv3"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    # if renpy.seen_image("bg ctrlv4"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/bgs/ctrlv4_%s.png") xalign 0.2 yalign 0.93
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ctrlv4"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    # if renpy.seen_image("bg ctrlv5"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/bgs/ctrlv5_%s.png") xalign 0.5 yalign 0.93
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ctrlv5"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    # if renpy.seen_image("bg ctrlv6"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/bgs/ctrlv6_%s.png") xalign 0.8 yalign 0.93
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ctrlv6"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_1:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d1_un_book_7dl") or renpy.seen_image("cg d1_un_book0_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d1_un_book_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "arts"), SetVariable("show_image_7dl", "cg d1_un_book_7dl"), SetVariable("show_image2_7dl", "cg d1_un_book0_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d2_mi_me_polaroid_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_mi_me_polaroid_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "arts"), SetVariable("show_image_7dl", "cg d2_mi_me_polaroid_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d2_mt_me_resort_afar_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_mt_me_resort_afar_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "arts"), SetVariable("show_image_7dl", "cg d2_mt_me_resort_afar_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d2_un_kissing_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_un_kissing_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "arts"), SetVariable("show_image_7dl", "cg d2_un_kissing_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d2_un_knees_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_un_knees_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "arts"), SetVariable("show_image_7dl", "cg d2_un_knees_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if persistent.hentai_graphics_7dl and renpy.seen_image("cg d2_us_soccer_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_us_soccer_sunset_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "arts"), SetVariable("show_image_7dl", "cg d2_us_soccer_sunset_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_2:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d2_us_trainhop_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_us_trainhop_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_us_trainhop_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d3_mi_dance_afar_7dl") or renpy.seen_image("cg d3_mi_dance_afar_bordo_7dl") or renpy.seen_image("cg d3_mi_dance_close_7dl") or renpy.seen_image("cg d3_mi_dance_close_bordo_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d3_mi_dance_afar_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d3_mi_dance_afar_7dl"), SetVariable("show_image2_7dl", "cg d3_mi_dance_afar_bordo_7dl"), SetVariable("show_image3_7dl", "cg d3_mi_dance_close_7dl"), SetVariable("show_image4_7dl", "cg d3_mi_dance_close_bordo_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if persistent.hentai_graphics_7dl and renpy.seen_image("cg d3_sl_bath_unplaited_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d3_sl_bath_unplaited_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d3_sl_bath_unplaited_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d4_mi_dj_lib_7dl") or renpy.seen_image("cg d4_mi_dj_lib0_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_mi_dj_lib_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_mi_dj_lib_7dl"), SetVariable("show_image2_7dl", "cg d4_mi_dj_lib0_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d4_mi_hedgehod_7dl") or renpy.seen_image("cg d4_mi_hedgehod_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_mi_hedgehod_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_mi_hedgehod_7dl"), SetVariable("show_image2_7dl", "cg d4_mi_hedgehod_day_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d4_us_stardust_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_us_stardust_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_us_stardust_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_3:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d5_un_carrier_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_un_carrier_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_un_carrier_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d5_us_rendezvous_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_us_rendezvous_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_us_rendezvous_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d5_us_sneakpeak_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_us_sneakpeak_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_us_sneakpeak_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d6_dance_alt_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_dance_alt_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_dance_alt_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d6_mi_departure_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_departure_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_departure_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d6_mi_farewell_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_farewell_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_farewell_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_4:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d6_mi_hugs_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_hugs_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_hugs_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d6_sl_clean_7dl") or renpy.seen_image("cg d6_sl_clean_dress_7dl") or renpy.seen_image("cg d6_sl_clean_dress2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_sl_clean_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_sl_clean_7dl"), SetVariable("show_image2_7dl", "cg d6_sl_clean_dress_7dl"), SetVariable("show_image3_7dl", "cg d6_sl_clean_dress2_7dl"), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d6_sl_zettai_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_sl_zettai_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_sl_zettai_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d6_un_evening_0_1_7dl") or renpy.seen_image("cg d6_un_evening_0_2_7dl") or renpy.seen_image("cg d6_un_evening_0_7dl") or renpy.seen_image("cg d6_un_evening_3_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_un_evening_0_1_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_un_evening_0_1_7dl"), SetVariable("show_image2_7dl", "cg d6_un_evening_0_2_7dl"), SetVariable("show_image3_7dl", "cg d6_un_evening_0_7dl"), SetVariable("show_image4_7dl", "cg d6_un_evening_3_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d7_dv_addic_happy_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_addic_happy_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_addic_happy_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d7_dv_alice_dj_7dl") or renpy.seen_image("cg d3_dv_alice_dj80_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_alice_dj_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_alice_dj_7dl"), SetVariable("show_image2_7dl", "cg d3_dv_alice_dj80_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_5:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_dv_looney_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_looney_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_looney_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_dv_rf_reject_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_rf_reject_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_rf_reject_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d7_frozen_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_frozen_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_frozen_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d7_mi_ghost_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_ghost_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_ghost_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d7_mi_hugs_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_hugs_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_hugs_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d7_mi_lost_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_lost_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_lost_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_6:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_mi_ramen_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_ramen_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_ramen_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_mi_reenter_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_reenter_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_reenter_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d7_sh_ai_4eva_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_sh_ai_4eva_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_sh_ai_4eva_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d7_sl_gonna_be_ok_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_sl_gonna_be_ok_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_sl_gonna_be_ok_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d7_un_epilogue_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_epilogue_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_epilogue_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d7_un_epilogue_d1_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_epilogue_d1_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_epilogue_d1_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_7:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_un_reanimation_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_reanimation_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_reanimation_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_us_pixie_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_us_pixie_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_us_pixie_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d4_cs_car_day_ba_gl_7dl") or renpy.seen_image("cg d4_cs_car_day_cs_7dl") or renpy.seen_image("cg d4_cs_car_open_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_cs_car_day_ba_gl_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_cs_car_day_ba_gl_7dl"), SetVariable("show_image2_7dl", "cg d4_cs_car_day_cs_7dl"), SetVariable("show_image3_7dl", "cg d4_cs_car_open_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d4_sl_lookup_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_sl_lookup_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_sl_lookup_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d4_sl_lookup2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_sl_lookup2_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_sl_lookup2_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d5_sl_hugs_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_sl_hugs_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_sl_hugs_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_8:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d5_sl_snark_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_sl_snark_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_sl_snark_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if persistent.hentai_graphics_7dl and renpy.seen_image("cg d6_dv_hentai_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_dv_hentai_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_dv_hentai_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if persistent.hentai_graphics_7dl and renpy.seen_image("cg d6_dv_hentai2_7dl"):    # renpy не засчитывает это cg увиденным
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_dv_hentai2_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_dv_hentai2_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d6_sl_bag_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_sl_bag_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_sl_bag_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d6_us_dance_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_us_dance_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_us_dance_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d5_sl_square_us_lead_7dl") or renpy.seen_image("cg d5_sl_square_sl_lead_7dl") or renpy.seen_image("cg d5_sl_square_me_lead_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_sl_square_us_lead_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_sl_square_us_lead_7dl"), SetVariable("show_image2_7dl", "cg d5_sl_square_sl_lead_7dl"), SetVariable("show_image3_7dl", "cg d5_sl_square_me_lead_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_9:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d1_mi_bus_7dl") or renpy.seen_image("cg d1_mi_bus2_7dl") or renpy.seen_image("cg d1_mi_bus3_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d1_mi_bus_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d1_mi_bus_7dl"), SetVariable("show_image2_7dl", "cg d1_mi_bus2_7dl"), SetVariable("show_image3_7dl", "cg d1_mi_bus3_7dl"), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d1_mi_dv_bus_7dl") or renpy.seen_image("cg d1_mi_dv_bus2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d1_mi_dv_bus_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d1_mi_dv_bus_7dl"), SetVariable("show_image2_7dl", "cg d1_mi_dv_bus2_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d7_dv_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_epilogue_bus_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d7_me_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_me_epilogue_bus_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_me_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d7_mi_club27_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_club27_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_club27_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d7_mi_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_epilogue_bus_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_10:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_mt_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mt_epilogue_bus_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mt_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_sl_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_sl_epilogue_bus_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_sl_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d7_un_epilogue_bus_7dl") or renpy.seen_image("cg d7_un_modern_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_epilogue_bus_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_epilogue_bus_7dl"), SetVariable("show_image2_7dl", "cg d7_un_modern_epilogue_bus_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d7_us_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_us_epilogue_bus_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_us_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d5_sl_bench_day_7dl") or renpy.seen_image("cg d5_sl_bench_sunset_7dl") or renpy.seen_image("cg d5_sl_bench_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_sl_bench_day_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_sl_bench_day_7dl"), SetVariable("show_image2_7dl", "cg d5_sl_bench_sunset_7dl"), SetVariable("show_image3_7dl", "cg d5_sl_bench_night_7dl"), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d6_mt_salute_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mt_salute_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mt_salute_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_11:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_mi_sparkle_7dl") or renpy.seen_image("cg d7_mi_sparkle_smile_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_sparkle_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_sparkle_7dl"), SetVariable("show_image2_7dl", "cg d7_mi_sparkle_smile_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d5_sl_piano_1_7dl") or renpy.seen_image("cg d5_sl_piano_2_7dl") or renpy.seen_image("cg d5_sl_piano_4_7dl") or renpy.seen_image("cg d5_sl_piano_5_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_sl_piano_1_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_sl_piano_1_7dl"), SetVariable("show_image2_7dl", "cg d5_sl_piano_2_7dl"), SetVariable("show_image3_7dl", "cg d5_sl_piano_4_7dl"), SetVariable("show_image4_7dl", "cg d5_sl_piano_5_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d7_dv_hugs2_7dl") or renpy.seen_image("cg d7_dv_hugs_7dl") or renpy.seen_image("cg d7_dv_hugs3_7dl") or renpy.seen_image("cg d7_dv_hugs4_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_hugs2_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_hugs2_7dl"), SetVariable("show_image2_7dl", "cg d7_dv_hugs_7dl"), SetVariable("show_image3_7dl", "cg d7_dv_hugs3_7dl"), SetVariable("show_image4_7dl", "cg d7_dv_hugs4_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d6_us_ghost_7dl") or renpy.seen_image("cg d6_us_ghost_hole_7dl"):
        if persistent.hentai_graphics_7dl:
            imagebutton:
                auto get_image_7dl("gui/gallery/arts/d6_us_ghost_7dl_%s.png") xalign 0.2 yalign 0.93
                action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_us_ghost_7dl"), SetVariable("show_image2_7dl", "cg d6_us_ghost_hole_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
        else:
            imagebutton:
                auto get_image_7dl("gui/gallery/arts/d6_us_ghost_7dl_%s.png") xalign 0.2 yalign 0.93
                action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_us_ghost_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d5_dv_arm_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_dv_arm_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_dv_arm_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d6_ka_dance_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_ka_dance_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_ka_dance_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_12:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d6_us_kiss_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_us_kiss_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_us_kiss_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_un_take_my_hand_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_take_my_hand_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_take_my_hand_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d3_un_dance_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d3_un_dance_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d3_un_dance_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d6_mi_salute_7dl") or renpy.seen_image("cg d6_mi_salute2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_salute_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_salute_7dl"), SetVariable("show_image2_7dl", "cg d6_mi_salute2_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d7_mi_sunk_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_sunk_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_sunk_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d7_mt_epilogue_miracle_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mt_epilogue_miracle_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mt_epilogue_miracle_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_13:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d3_dv_kiss_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d3_dv_kiss_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d3_dv_kiss_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d4_un_fz_mt_board_7dl mt_smile") or renpy.seen_image("cg d4_un_fz_mt_board_7dl mt_grin") or renpy.seen_image("cg d4_un_fz_mt_board_7dl mt_dontlike") or renpy.seen_image("cg d4_un_fz_mt_board_7dl mt_normal2"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_un_fz_mt_board_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_un_fz_mt_board_7dl mt_smile"), SetVariable("show_image2_7dl", "cg d4_un_fz_mt_board_7dl mt_grin"), SetVariable("show_image3_7dl", "cg d4_un_fz_mt_board_7dl mt_dontlike"), SetVariable("show_image4_7dl", "cg d4_un_fz_mt_board_7dl mt_normal2"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d5_un_fz_tousand_twinkles_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_un_fz_tousand_twinkles_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_un_fz_tousand_twinkles_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d5_un_fz_twinkles_6_7dl") or renpy.seen_image("cg d5_un_fz_twinkles_1_7dl") or renpy.seen_image("cg d5_un_fz_twinkles_2_7dl") or renpy.seen_image("cg d5_un_fz_twinkles_3_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_un_fz_twinkles_6_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_un_fz_twinkles_6_7dl"), SetVariable("show_image2_7dl", "cg d5_un_fz_twinkles_1_7dl"), SetVariable("show_image3_7dl", "cg d5_un_fz_twinkles_2_7dl"), SetVariable("show_image4_7dl", "cg d5_un_fz_twinkles_3_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d7_sl_hug_7dl") or renpy.seen_image("cg d7_sl_hug2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_sl_hug_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_sl_hug_7dl"), SetVariable("show_image2_7dl", "cg d7_sl_hug2_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d6_un_fz_rr_faceless_hands_7dl") or renpy.seen_image("cg d6_un_fz_rr_faceless_hands_2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_un_fz_rr_faceless_hands_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_un_fz_rr_faceless_hands_7dl"), SetVariable("show_image2_7dl", "cg d6_un_fz_rr_faceless_hands_2_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_14:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_dv_child_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_child_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_child_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d6_mi_dv_concert_7dl") or renpy.seen_image("cg d4_dv_concert_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_dv_concert_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_dv_concert_7dl"), SetVariable("show_image2_7dl", "cg d4_dv_concert_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d6_un_fz_un_death_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_un_fz_un_death_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_un_fz_un_death_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d6_us_kiss2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_us_kiss2_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_us_kiss2_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d5_dv_sleep_7dl") or renpy.seen_image("cg d5_dv_sleep2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_dv_sleep_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_dv_sleep_7dl"), SetVariable("show_image2_7dl", "cg d5_dv_sleep2_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d5_dv_sleep_together_7dl") or renpy.seen_image("cg d5_dv_sleep_together2_7dl") or renpy.seen_image("cg d5_dv_sleep_together3_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_dv_sleep_together_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_dv_sleep_together_7dl"), SetVariable("show_image2_7dl", "cg d5_dv_sleep_together2_7dl"), SetVariable("show_image3_7dl", "cg d5_dv_sleep_together3_7dl"), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_15:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_mi_lost2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_lost2_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_lost2_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_mt_mj_7dl") or renpy.seen_image("cg d7_mt_mj2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mt_mj_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mt_mj_7dl"), SetVariable("show_image2_7dl", "cg d7_mt_mj2_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d7_mt_old_7dl") or renpy.seen_image("cg d7_mt_old2_7dl") or renpy.seen_image("cg d7_mt_old3_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mt_old_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mt_old_7dl"), SetVariable("show_image2_7dl", "cg d7_mt_old2_7dl"), SetVariable("show_image3_7dl", "cg d7_mt_old3_7dl"), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d6_un_rape_7dl") or renpy.seen_image("cg d6_un_rape2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_un_rape_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_un_rape_7dl"), SetVariable("show_image2_7dl", "cg d6_un_rape2_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d7_un_fire_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_fire_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_fire_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d7_un_fireyes_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_fireyes_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_fireyes_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_16:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_un_firebridge_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_firebridge_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_firebridge_7dl"), SetVariable("show_image2_7dl", "cg d7_un_firebridge2_7dl"), SetVariable("show_image3_7dl", "cg d7_un_firebridge3_7dl"), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_us_bedroom_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_us_bedroom_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_us_bedroom_7dl"), SetVariable("show_image2_7dl", "cg d7_us_bedroom2_7dl"), SetVariable("show_image3_7dl", "cg d7_us_bedroom3_7dl"), SetVariable("show_image4_7dl", "cg d7_us_bedroom4_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d7_dv_come_with_me_1_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_come_with_me_1_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_come_with_me_1_7dl"), SetVariable("show_image2_7dl", "cg d7_dv_come_with_me_2_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    # if renpy.seen_image("cg ctrlv4"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv4_%s.png") xalign 0.2 yalign 0.93
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv4"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    # if renpy.seen_image("cg ctrlv5"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv5_%s.png") xalign 0.5 yalign 0.93
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv5"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    # if renpy.seen_image("cg ctrlv6"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv6_%s.png") xalign 0.8 yalign 0.93
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv6"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_un_1:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_un_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d1_un_book_7dl") or renpy.seen_image("cg d1_un_book0_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d1_un_book_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d1_un_book_7dl"), SetVariable("show_image2_7dl", "cg d1_un_book0_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d2_un_kissing_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_un_kissing_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_un_kissing_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d2_un_knees_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_un_knees_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_un_knees_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d5_un_carrier_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_un_carrier_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_un_carrier_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d6_un_evening_0_1_7dl") or renpy.seen_image("cg d6_un_evening_0_2_7dl") or renpy.seen_image("cg d6_un_evening_0_7dl") or renpy.seen_image("cg d6_un_evening_3_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_un_evening_0_1_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_un_evening_0_1_7dl"), SetVariable("show_image2_7dl", "cg d6_un_evening_0_2_7dl"), SetVariable("show_image3_7dl", "cg d6_un_evening_0_7dl"), SetVariable("show_image4_7dl", "cg d6_un_evening_3_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d7_un_epilogue_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_epilogue_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_epilogue_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_un_2:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_un_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_un_reanimation_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_reanimation_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_reanimation_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_un_epilogue_bus_7dl") or renpy.seen_image("cg d7_un_modern_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_epilogue_bus_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_epilogue_bus_7dl"), SetVariable("show_image2_7dl", "cg d7_un_modern_epilogue_bus_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d7_un_take_my_hand_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_take_my_hand_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_take_my_hand_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d3_un_dance_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d3_un_dance_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d3_un_dance_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d6_un_fz_un_death_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_un_fz_un_death_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_un_fz_un_death_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d6_un_rape_7dl") or renpy.seen_image("cg d6_un_rape2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_un_rape_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_un_rape_7dl"), SetVariable("show_image2_7dl", "cg d6_un_rape2_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
screen arts_7dl_un_3:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_un_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_un_fireyes_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_fireyes_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_fireyes_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_un_firebridge_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_firebridge_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_firebridge_7dl"), SetVariable("show_image2_7dl", "cg d7_un_firebridge2_7dl"), SetVariable("show_image3_7dl", "cg d7_un_firebridge3_7dl"), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    # if renpy.seen_image("cg ctrlv3"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv3_%s.png") xalign 0.8 yalign 0.15
            # action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv3"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    # if renpy.seen_image("cg ctrlv4"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv4_%s.png") xalign 0.2 yalign 0.93
            # action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv4"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    # if renpy.seen_image("cg ctrlv5"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv5_%s.png") xalign 0.5 yalign 0.93
            # action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv5"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    # if renpy.seen_image("cg ctrlv6"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv6_%s.png") xalign 0.8 yalign 0.93
            # action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv6"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_sl_1:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_sl_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if persistent.hentai_graphics_7dl and renpy.seen_image("cg d3_sl_bath_unplaited_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d3_sl_bath_unplaited_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d3_sl_bath_unplaited_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d6_sl_clean_7dl") or renpy.seen_image("cg d6_sl_clean_dress_7dl") or renpy.seen_image("cg d6_sl_clean_dress2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_sl_clean_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_sl_clean_7dl"), SetVariable("show_image2_7dl", "cg d6_sl_clean_dress_7dl"), SetVariable("show_image3_7dl", "cg d6_sl_clean_dress2_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d6_sl_zettai_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_sl_zettai_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_sl_zettai_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d4_sl_lookup2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_sl_lookup2_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_sl_lookup2_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d5_sl_hugs_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_sl_hugs_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_sl_hugs_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d6_sl_bag_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_sl_bag_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_sl_bag_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_sl_2:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_sl_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_sl_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_sl_epilogue_bus_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_sl_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d5_sl_bench_day_7dl") or renpy.seen_image("cg d5_sl_bench_sunset_7dl") or renpy.seen_image("cg d5_sl_bench_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_sl_bench_day_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_sl_bench_day_7dl"), SetVariable("show_image2_7dl", "cg d5_sl_bench_sunset_7dl"), SetVariable("show_image3_7dl", "cg d5_sl_bench_night_7dl"), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d5_sl_piano_1_7dl") or renpy.seen_image("cg d5_sl_piano_2_7dl") or renpy.seen_image("cg d5_sl_piano_4_7dl") or renpy.seen_image("cg d5_sl_piano_5_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_sl_piano_1_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_sl_piano_1_7dl"), SetVariable("show_image2_7dl", "cg d5_sl_piano_2_7dl"), SetVariable("show_image3_7dl", "cg d5_sl_piano_4_7dl"), SetVariable("show_image4_7dl", "cg d5_sl_piano_5_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d7_sl_hug_7dl") or renpy.seen_image("cg d7_sl_hug2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_sl_hug_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_sl_hug_7dl"), SetVariable("show_image2_7dl", "cg d7_sl_hug2_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d4_sl_lookup_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_sl_lookup_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_sl_lookup_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    # if renpy.seen_image("cg ctrlv6"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv6_%s.png") xalign 0.8 yalign 0.93
            # action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv6"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_dv_1:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/" + str(max_dv_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_dv_addic_happy_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_addic_happy_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_addic_happy_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_dv_alice_dj_7dl") or renpy.seen_image("cg d3_dv_alice_dj80_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_alice_dj_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_alice_dj_7dl"), SetVariable("show_image2_7dl", "cg d3_dv_alice_dj80_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d7_dv_looney_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_looney_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_looney_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d7_dv_rf_reject_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_rf_reject_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_rf_reject_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if persistent.hentai_graphics_7dl and renpy.seen_image("cg d6_dv_hentai_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_dv_hentai_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_dv_hentai_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if persistent.hentai_graphics_7dl and renpy.seen_image("cg d6_dv_hentai2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_dv_hentai2_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_dv_hentai2_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_dv_2:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_dv_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d1_mi_dv_bus_7dl") or renpy.seen_image("cg d1_mi_dv_bus2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d1_mi_dv_bus_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d1_mi_dv_bus_7dl"), SetVariable("show_image2_7dl", "cg d1_mi_dv_bus2_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_dv_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_epilogue_bus_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d5_dv_arm_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_dv_arm_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_dv_arm_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d3_dv_kiss_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d3_dv_kiss_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d3_dv_kiss_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d6_mi_dv_concert_7dl") or renpy.seen_image("cg d4_dv_concert_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_dv_concert_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_dv_concert_7dl"), SetVariable("show_image2_7dl", "cg d4_dv_concert_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d5_dv_sleep_7dl") or renpy.seen_image("cg d5_dv_sleep2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_dv_sleep_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_dv_sleep_7dl"), SetVariable("show_image2_7dl", "cg d5_dv_sleep2_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_dv_3:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_dv_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d5_dv_sleep_together_7dl") or renpy.seen_image("cg d5_dv_sleep_together2_7dl") or renpy.seen_image("cg d5_dv_sleep_together3_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_dv_sleep_together_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_dv_sleep_together_7dl"), SetVariable("show_image2_7dl", "cg d5_dv_sleep_together2_7dl"), SetVariable("show_image3_7dl", "cg d5_dv_sleep_together3_7dl"), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_dv_child_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_child_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_child_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d7_dv_hugs2_7dl") or renpy.seen_image("cg d7_dv_hugs_7dl") or renpy.seen_image("cg d7_dv_hugs3_7dl") or renpy.seen_image("cg d7_dv_hugs4_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_hugs2_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_hugs2_7dl"), SetVariable("show_image2_7dl", "cg d7_dv_hugs_7dl"), SetVariable("show_image3_7dl", "cg d7_dv_hugs3_7dl"), SetVariable("show_image4_7dl", "cg d7_dv_hugs4_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d7_dv_come_with_me_1_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_come_with_me_1_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_come_with_me_1_7dl"), SetVariable("show_image2_7dl", "cg d7_dv_come_with_me_2_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    # if renpy.seen_image("cg ctrlv5"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv5_%s.png") xalign 0.5 yalign 0.93
            # action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv5"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    # if renpy.seen_image("cg ctrlv6"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv6_%s.png") xalign 0.8 yalign 0.93
            # action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv6"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_mi_1:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_mi_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d2_mi_me_polaroid_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_mi_me_polaroid_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_mi_me_polaroid_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d3_mi_dance_afar_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d3_mi_dance_afar_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d3_mi_dance_afar_7dl"), SetVariable("show_image_7dl", "cg d3_mi_dance_afar_bordo_7dl"), SetVariable("show_image_7dl", "cg d3_mi_dance_close_7dl"), SetVariable("show_image4_7dl", "cg d3_mi_dance_close_bordo_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d4_mi_dj_lib_7dl") or renpy.seen_image("cg d4_mi_dj_lib0_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_mi_dj_lib_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_mi_dj_lib_7dl"), SetVariable("show_image2_7dl", "cg d4_mi_dj_lib0_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d4_mi_hedgehod_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_mi_hedgehod_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_mi_hedgehod_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d6_mi_departure_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_departure_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_departure_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d6_mi_farewell_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_farewell_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_farewell_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_mi_2:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_mi_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d6_mi_hugs_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_hugs_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_hugs_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_mi_ghost_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_ghost_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_ghost_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d7_mi_hugs_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_hugs_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_hugs_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d7_mi_lost_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_lost_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_lost_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d7_mi_ramen_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_ramen_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_ramen_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d7_mi_reenter_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_reenter_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_reenter_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_mi_3:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_mi_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d1_mi_bus_7dl") or renpy.seen_image("cg d1_mi_bus2_7dl") or renpy.seen_image("cg d1_mi_bus3_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d1_mi_bus_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d1_mi_bus_7dl"), SetVariable("show_image2_7dl", "cg d1_mi_bus2_7dl"), SetVariable("show_image3_7dl", "cg d1_mi_bus3_7dl"), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d1_mi_dv_bus_7dl") or renpy.seen_image("cg d1_mi_dv_bus2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d1_mi_dv_bus_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d1_mi_dv_bus_7dl"), SetVariable("show_image2_7dl", "cg d1_mi_dv_bus2_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d7_mi_club27_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_club27_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_club27_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d7_mi_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_epilogue_bus_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d7_mi_sparkle_7dl") or renpy.seen_image("cg d7_mi_sparkle_smile_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_sparkle_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_sparkle_7dl"), SetVariable("show_image2_7dl", "cg d7_mi_sparkle_smile_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d6_mi_salute_7dl") or renpy.seen_image("cg d6_mi_salute2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_salute_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_salute_7dl"), SetVariable("show_image2_7dl", "cg d6_mi_salute2_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_mi_4:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_mi_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_mi_sunk_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_sunk_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_sunk_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d6_mi_dv_concert_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_dv_concert_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_dv_concert_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d7_mi_lost2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_lost2_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_lost2_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    # if renpy.seen_image("cg ctrlv4"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv4_%s.png") xalign 0.2 yalign 0.93
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv4"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    # if renpy.seen_image("cg ctrlv5"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv5_%s.png") xalign 0.5 yalign 0.93
            # action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv5"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    # if renpy.seen_image("cg ctrlv6"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv6_%s.png") xalign 0.8 yalign 0.93
            # action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv6"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_us_1:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_us_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if persistent.hentai_graphics_7dl and renpy.seen_image("cg d2_us_soccer_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_us_soccer_sunset_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_us_soccer_sunset_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d2_us_trainhop_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_us_trainhop_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_us_trainhop_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d4_us_stardust_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_us_stardust_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_us_stardust_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d5_us_sneakpeak_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_us_sneakpeak_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_us_sneakpeak_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d7_us_pixie_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_us_pixie_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_us_pixie_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d6_us_dance_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_us_dance_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_us_dance_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_us_2:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_us_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d5_us_rendezvous_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_us_rendezvous_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_us_rendezvous_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_us_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_us_epilogue_bus_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_us_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d6_us_ghost_7dl") or renpy.seen_image("cg d6_us_ghost_hole_7dl"):
        if persistent.hentai_graphics_7dl:
            imagebutton:
                auto get_image_7dl("gui/gallery/arts/d6_us_ghost_7dl_%s.png") xalign 0.8 yalign 0.15
                action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_us_ghost_7dl"), SetVariable("show_image2_7dl", "cg d6_us_ghost_hole_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
        else:
            imagebutton:
                auto get_image_7dl("gui/gallery/arts/d6_us_ghost_7dl_%s.png") xalign 0.8 yalign 0.15
                action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_us_ghost_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d6_us_kiss_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_us_kiss_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_us_kiss_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d6_us_kiss2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_us_kiss2_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_us_kiss2_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d7_us_bedroom_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_us_bedroom_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_us_bedroom_7dl"), SetVariable("show_image2_7dl", "cg d7_us_bedroom2_7dl"), SetVariable("show_image3_7dl", "cg d7_us_bedroom3_7dl"), SetVariable("show_image4_7dl", "cg d7_us_bedroom4_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen arts_7dl_mt_1:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_mt_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d2_mt_me_resort_afar_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_mt_me_resort_afar_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_mt_me_resort_afar_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_mt_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mt_epilogue_bus_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mt_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d6_mt_salute_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mt_salute_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mt_salute_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d7_mt_epilogue_miracle_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mt_epilogue_miracle_7dl_%s.png") xalign 0.2 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mt_epilogue_miracle_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d4_un_fz_mt_board_7dl mt_smile") or renpy.seen_image("cg d4_un_fz_mt_board_7dl mt_grin") or renpy.seen_image("cg d4_un_fz_mt_board_7dl mt_dontlike") or renpy.seen_image("cg d4_un_fz_mt_board_7dl mt_normal2"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_un_fz_mt_board_7dl_%s.png") xalign 0.5 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_un_fz_mt_board_7dl mt_smile"), SetVariable("show_image2_7dl", "cg d4_un_fz_mt_board_7dl mt_grin"), SetVariable("show_image3_7dl", "cg d4_un_fz_mt_board_7dl mt_dontlike"), SetVariable("show_image4_7dl", "cg d4_un_fz_mt_board_7dl mt_normal2"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d7_mt_old_7dl") or renpy.seen_image("cg d7_mt_old2_7dl") or renpy.seen_image("cg d7_mt_old3_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mt_old_7dl_%s.png") xalign 0.8 yalign 0.93
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mt_old_7dl"), SetVariable("show_image2_7dl", "cg d7_mt_old2_7dl"), SetVariable("show_image3_7dl", "cg d7_mt_old3_7dl"), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

label alt_gallery_start:
    $ make_names_known_7dl()
    if not sdl_mus_engine.is_active:
        play music music_7dl["more_than_alive"] fadein 3
    scene bg gallery_7dl with fade
    $ gallery_mode_7dl = "arts"
    $ renpy.block_rollback()
    call screen gallery_main_7dl

label alt_gallery:
    $ renpy.block_rollback()
    call screen gallery_main_7dl

label show_img_7dl:
    $ renpy.scene()
    if show_image_7dl == "cg d7_dv_rf_reject_7dl":
        $ renpy.show(show_image_7dl, at_list=[bottotop])
    elif show_image_7dl == "cg d7_mi_ghost_7dl":
        $ renpy.show(show_image_7dl, at_list=[bottotop])
    elif show_image_7dl == "cg d7_mi_hugs_7dl":
        $ renpy.show(show_image_7dl, at_list=[bottotop])
    else:
        $ renpy.show(show_image_7dl)
    $ renpy.with_statement(fade)
    $ renpy.pause()
    $ show_image_7dl = ""
    if show_image2_7dl:
        $ renpy.scene()
        $ renpy.show(show_image2_7dl)
        $ renpy.with_statement(fade)
        $ renpy.pause()
        $ show_image2_7dl = ""
    if show_image3_7dl:
        $ renpy.scene()
        $ renpy.show(show_image3_7dl)
        $ renpy.with_statement(fade)
        $ renpy.pause()
        $ show_image3_7dl = ""
    if show_image4_7dl:
        $ renpy.scene()
        $ renpy.show(show_image4_7dl)
        $ renpy.with_statement(fade)
        $ renpy.pause()
        $ show_image4_7dl = ""
    $ renpy.show("bg black")
    jump alt_gallery

label cg_slide_show_7dl:
    python:
        alt_slide_show = True
        for file in renpy.list_files():
            if file.startswith(default_7dl_path+"Pics/gui/gallery/arts/") and file.endswith("_hover.png"):
                if renpy.seen_image("cg "+str(file)[len(default_7dl_path)+22:-10]):
                    list_gallery_cg_7dl.append("cg "+str(file)[len(default_7dl_path)+22:-10])
        random.shuffle(list_gallery_cg_7dl)
        renpy.scene()
        for i in list_gallery_cg_7dl:
            if i == "cg d7_dv_rf_reject_7dl":
                renpy.show(i, at_list=[bottotop])
                renpy.with_statement(fade)
                renpy.pause(12)
            elif i == "cg d7_mi_ghost_7dl":
                renpy.show(i, at_list=[bottotop])
                renpy.with_statement(fade)
                renpy.pause(12)
            elif i == "cg d7_mi_hugs_7dl":
                renpy.show(i, at_list=[bottotop])
                renpy.with_statement(fade)
                renpy.pause(12)
            elif "d4_un_fz_mt_board_7dl" in i:
                renpy.show("cg d4_un_fz_mt_board_7dl mt_smile", at_list=[normal_gallery])
                renpy.with_statement(fade)
                renpy.pause(4)
            else:
                renpy.show(i, at_list=[normal_gallery])
                renpy.with_statement(fade)
                renpy.pause(4)
    hide screen gallery_exit_7dl
    $ alt_slide_show = False
    jump alt_gallery

label bg_slide_show_7dl:
    python:
        alt_slide_show = True
        for file in renpy.list_files():
            if file.startswith(default_7dl_path+"Pics/gui/gallery/bgs/") and file.endswith("_hover.png"):
                if renpy.seen_image("bg "+str(file)[len(default_7dl_path)+21:-10]):
                    list_gallery_bg_7dl.append("bg "+str(file)[len(default_7dl_path)+21:-10])
        random.shuffle(list_gallery_bg_7dl)
        renpy.scene()
        for i in list_gallery_bg_7dl:
            renpy.show(i, at_list=[normal_gallery])
            renpy.with_statement(fade)
            renpy.pause(4)
    hide screen gallery_exit_7dl
    $ alt_slide_show = False
    jump alt_gallery

# screen bgs_7dl_x: # x - pagenum
    # tag menu
    # $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    # textbutton next_page_7dl:
        # text_style "page_7dl_text"
        # style "page_7dl_text"
        # xalign 0.95
        # yalign 0.95
    # if renpy.seen_image("bg ctrlv1"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/bgs/ctrlv1_%s.png") xalign 0.19 yalign 0.15
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ctrlv1"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    # if renpy.seen_image("bg ctrlv2"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/bgs/ctrlv2_%s.png") xalign 0.5 yalign 0.15
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ctrlv2"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    # if renpy.seen_image("bg ctrlv3"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/bgs/ctrlv3_%s.png") xalign 0.8 yalign 0.15
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ctrlv3"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    # if renpy.seen_image("bg ctrlv4"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/bgs/ctrlv4_%s.png") xalign 0.2 yalign 0.93
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ctrlv4"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    # if renpy.seen_image("bg ctrlv5"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/bgs/ctrlv5_%s.png") xalign 0.5 yalign 0.93
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ctrlv5"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    # if renpy.seen_image("bg ctrlv6"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/bgs/ctrlv6_%s.png") xalign 0.8 yalign 0.93
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ctrlv6"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

# screen arts_7dl_x: # x - pagenum
    # tag menu
    # $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    # textbutton next_page_7dl:
        # text_style "page_7dl_text"
        # style "page_7dl_text"
        # xalign 0.95
        # yalign 0.95
    # if renpy.seen_image("cg ctrlv1"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv1_%s.png") xalign 0.19 yalign 0.15
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv1"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    # if renpy.seen_image("cg ctrlv2"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv2_%s.png") xalign 0.5 yalign 0.15
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv2"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    # if renpy.seen_image("cg ctrlv3"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv3_%s.png") xalign 0.8 yalign 0.15
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv3"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    # if renpy.seen_image("cg ctrlv4"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv4_%s.png") xalign 0.2 yalign 0.93
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv4"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    # if renpy.seen_image("cg ctrlv5"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv5_%s.png") xalign 0.5 yalign 0.93
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv5"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    # if renpy.seen_image("cg ctrlv6"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv6_%s.png") xalign 0.8 yalign 0.93
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv6"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

# screen arts_7dl_xx_x: #xx - girlname, x - pagenum
    # tag menu
    # $ next_page_7dl = str(page_7dl)  + "/" + str(max_xx_page_7dl)
    # textbutton next_page_7dl:
        # text_style "page_7dl_text"
        # style "page_7dl_text"
        # xalign 0.95
        # yalign 0.95
    # if renpy.seen_image("cg ctrlv1"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv1_%s.png") xalign 0.19 yalign 0.15
            # action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv1"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    # if renpy.seen_image("cg ctrlv2"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv2_%s.png") xalign 0.5 yalign 0.15
            # action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv2"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    # if renpy.seen_image("cg ctrlv3"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv3_%s.png") xalign 0.8 yalign 0.15
            # action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv3"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    # if renpy.seen_image("cg ctrlv4"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv4_%s.png") xalign 0.2 yalign 0.93
            # action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv4"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    # if renpy.seen_image("cg ctrlv5"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv5_%s.png") xalign 0.5 yalign 0.93
            # action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv5"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    # if renpy.seen_image("cg ctrlv6"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv6_%s.png") xalign 0.8 yalign 0.93
            # action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("slide_show_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv6"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
