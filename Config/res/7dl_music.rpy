# От избыточного количества кнопок на экране ренпай начинает подлагивать.
# Чтобы этого избежать, плейлист разбит на отдельные страницы.
# Данный параметр определяет число треков на 1 странице.
define SDL_MUS_PAGE_SIZE = 60
# Скорость прокрутки названия трека в бегущей строке
define SDL_MUS_ADJ_STEP = 2

init 999 python:
    ##\\\\\\\\\\\\\\\\\\\\\\\\\СТИЛИ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # Текущий трек
    style.sdl_mus_current_font = Style(style.default)
    style.sdl_mus_current_font.font = get_image_7dl("fonts/ARIALUNI.TTF")
    style.sdl_mus_current_font.size = 20
    style.sdl_mus_current_font.color = "#3E464D"
    style.sdl_mus_current_font.layout = "nobreak"

    # Плейлист
    style.sdl_mus_playlist_button = Style(style.button)
    style.sdl_mus_playlist_button.child = None
    style.sdl_mus_playlist_button.focus_mask = None
    style.sdl_mus_playlist_button.background = None
    style.sdl_mus_playlist_button.hover_background  = "#3E464D"
    style.sdl_mus_playlist_button.selected_background  = "#CCCCCC"
    style.sdl_mus_playlist_button.xsize = 571
    style.sdl_mus_playlist_button.ysize = 31

    style.sdl_mus_playlist_font = Style(style.default)
    style.sdl_mus_playlist_font.font = get_image_7dl("fonts/ARIALUNI.TTF")
    style.sdl_mus_playlist_font.size = 20
    style.sdl_mus_playlist_font.color = "#3E464D"
    style.sdl_mus_playlist_font.hover_color = "#8299B1"
    style.sdl_mus_playlist_font.selected_bold = True
    style.sdl_mus_playlist_font.insensitive_color = "#CCCCCC"
    style.sdl_mus_playlist_font.layout = "nobreak"

    # Номер страницы плейлиста
    style.sdl_mus_page_font = Style(style.default)
    style.sdl_mus_page_font.font = get_image_7dl("fonts/ARIALUNI.TTF")
    style.sdl_mus_page_font.size = 20
    style.sdl_mus_page_font.color = "#98A3AD"

init:
    ##\\\\\\\\\\\\\\\\\\\\\\\\\ЭКРАНЫ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    image sdl_mus_screen_main = get_image_7dl("gui/music/screens/mus_screen_7dl.png")



init 2 python:
    def get_mus_pos_7dl():
        pos = renpy.music.get_pos()
        if pos is not None:
            pos = int(pos)
            return pos
        else:
            return 0

    def get_mus_len_7dl():
        len = int(renpy.music.get_duration())
        return len

    # Основной класс
    class sdl_mus_Engine:
        def __init__(self, page_count):
            self.is_active = False
            self.is_panel_open = False
            self.page_cur = 0
            self.page_count = page_count
            self.cur_file = ""
            self.cur_file_name = ""
            self.cur_file_pos = 0
            self.cur_file_len = 0
            self.cur_file_adj = ui.adjustment()
            self.adj_sign = 1

        def set_cur_file_pos(self):
            renpy.music.play("<from " + str(self.cur_file_pos) + ">" + self.cur_file)
            sdl_mus_room.queue_if_playing()

        def update_cur_file_pos(self):
            self.cur_file_pos = get_mus_pos_7dl()
            # XXX: По какой-то причине get_duration иногда не отрабатывает корректно сразу при переключении трека. Если это произошло - повторно вызываем здесь
            if self.cur_file_len == 0:
                self.cur_file_len = get_mus_len_7dl()

        def update_ticker(self):
            if self.cur_file_adj.value == 0:
                self.adj_sign = 1
            elif self.cur_file_adj.value == self.cur_file_adj.range:
                self.adj_sign = -1
            self.cur_file_adj.change(self.cur_file_adj.value + self.adj_sign * SDL_MUS_ADJ_STEP)

        def update_cur_track(self):
            self.cur_file = get_playing_7dl('music')
            self.cur_file_name = check_muzlo_7dl(self.cur_file)
            self.cur_file_pos = get_mus_pos_7dl()
            self.cur_file_len = get_mus_len_7dl()
            self.cur_file_adj.change(0)
            self.adj_sign = 1

        def cur_page_inc(self):
            self.page_cur += 1

        def cur_page_dec(self):
            self.page_cur -= 1

        def get_cur_file_pos(self):
            return "{:02d}:{:02d}".format(self.cur_file_pos // 60, self.cur_file_pos % 60) + " / " + "{:02d}:{:02d}".format(self.cur_file_len // 60, self.cur_file_len % 60)

        def get_cur_page(self):
            return "СТРАНИЦА " + "{:d}/{:d}".format(self.page_cur + 1, self.page_count)

    sdl_mus_engine = sdl_mus_Engine((len(music_list_7dl) - len(music_list_excluded_7dl)) // SDL_MUS_PAGE_SIZE + 1)

    sdl_mus_room = MusicRoom_7dl(fadein=1.0, loop=False)
    for name, file in sorted(music_list_7dl.iteritems()):
        if file not in music_list_excluded_7dl:
            sdl_mus_room.add(file, action=Function(sdl_mus_engine.update_cur_track))



screen music_7dl(engine=sdl_mus_engine, default_music):
    modal True

    add "sdl_mus_screen_main"

    # Плеер
    add get_image_7dl("gui/music/mus_player.png") xalign 0.5 ypos 126
    imagebutton xpos 980 ypos 199:
        auto get_image_7dl("gui/music/buttons/mus_prev_%s.png")
        activate_sound sdl_achv_click
        action [sdl_mus_room.Previous(), Function(engine.update_cur_track)]
    imagebutton xpos 1046 ypos 199:
        auto get_image_7dl("gui/music/buttons/mus_play_%s.png")
        activate_sound sdl_achv_click
        selected not renpy.music.get_pause()
        action [PauseAudio("music", value="toggle")]
    imagebutton xpos 1112 ypos 199:
        auto get_image_7dl("gui/music/buttons/mus_next_%s.png")
        activate_sound sdl_achv_click
        action [sdl_mus_room.Next(), Function(engine.update_cur_track)]
    imagebutton xpos 1046 ypos 265:
        auto get_image_7dl("gui/music/buttons/mus_shuffle_%s.png")
        activate_sound sdl_achv_click
        action [sdl_mus_room.ToggleShuffle()]
    imagebutton xpos 1046 ypos 133:
        auto get_image_7dl("gui/music/buttons/mus_loop_%s.png")
        activate_sound sdl_achv_click
        selected sdl_mus_room.single_track
        action [If(sdl_mus_room.loop, true=If(sdl_mus_room.single_track, true=[sdl_mus_room.SetLoop(False), sdl_mus_room.SetSingleTrack(False)], false=sdl_mus_room.SetSingleTrack(True)), false=sdl_mus_room.SetLoop(True))]
    if sdl_mus_room.shuffle:
        add get_image_7dl("gui/music/indicators/mus_ind_shuffle.png") xpos 908 ypos 207
    if sdl_mus_room.loop:
        if sdl_mus_room.single_track:
            add get_image_7dl("gui/music/indicators/mus_ind_loop_one.png") xpos 884 ypos 207
        else:
            add get_image_7dl("gui/music/indicators/mus_ind_loop_all.png") xpos 884 ypos 207

    # Свернуть
    imagebutton xpos 1145 ypos 128:
        auto get_image_7dl("gui/music/buttons/mus_min_%s.png")
        activate_sound sdl_achv_click
        action [Hide("music_7dl", transition=Dissolve(0.2))]

    # Выключение
    imagebutton xpos 1191 ypos 186:
        auto get_image_7dl("gui/music/buttons/mus_off_%s.png")
        activate_sound sdl_achv_click
        action [sdl_mus_room.Stop(), Hide("music_7dl", transition=Dissolve(0.2)), SetField(engine, "is_active", False), Play('music', default_music, fadein=3)]

    # Название текущего трека
    viewport id "vp_track" area (702, 174, 227, 35):
        xadjustment engine.cur_file_adj
        text engine.cur_file_name style "sdl_mus_current_font"
    text engine.get_cur_file_pos() style "sdl_mus_current_font" xpos 702 ypos 205
    # Таймер для обновления текущей позиции в треке и бегущей строки
    timer 0.1 repeat True action [Function(engine.update_cur_file_pos), Function(engine.update_ticker)]

    # Прогресс бар текущего трека
    bar xpos 667 ypos 254:
        if renpy.version_tuple[0]*100000+renpy.version_tuple[1]*10000+renpy.version_tuple[2]*1000+renpy.version_tuple[3] >= 735606:
            value FieldValue(engine, "cur_file_pos", engine.cur_file_len, action=Function(engine.set_cur_file_pos))
        else:
            value FieldValue(engine, "cur_file_pos", engine.cur_file_len)
        left_bar  Frame(get_image_7dl("gui/music/bars/mus_bar_full.png"), 12, 12)
        right_bar Frame(get_image_7dl("gui/music/bars/mus_bar_null.png"), 12, 12)
        thumb       get_image_7dl("gui/music/bars/mus_bar_thumb_idle.png")
        hover_thumb get_image_7dl("gui/music/bars/mus_bar_thumb_hover.png")
        xmaximum 280
        ymaximum 12

    # Плейлист
    add get_image_7dl("gui/music/frames/mus_frame_playlist.png") xalign 0.5 ypos 301

    side "c r":
        xpos 664
        ypos 327
        xysize (599, 585)

        default sdl_mus_bar_value = ui.adjustment()
        viewport id "vp_playlist":
            mousewheel True
            yadjustment sdl_mus_bar_value

            has vbox spacing 2

            for name, file in sorted(music_list_7dl.iteritems())[engine.page_cur * SDL_MUS_PAGE_SIZE : (engine.page_cur + 1) * SDL_MUS_PAGE_SIZE]:
                if file not in music_list_excluded_7dl:
                    if renpy.seen_audio(file):
                        button style "sdl_mus_playlist_button":
                            viewport xsize 561:
                                text name style "sdl_mus_playlist_font"
                            action [sdl_mus_room.Play(file), Function(sdl_mus_engine.update_cur_track)]
                    else:
                        text " ?????" style "sdl_mus_playlist_font"

        vbar:
            value YScrollValue("vp_playlist")
            top_bar    Frame(get_image_7dl("gui/music/bars/mus_vbar_full.png"), 12, 12)
            bottom_bar Frame(get_image_7dl("gui/music/bars/mus_vbar_null.png"), 12, 12)
            thumb       get_image_7dl("gui/music/bars/mus_bar_thumb_idle.png")
            hover_thumb get_image_7dl("gui/music/bars/mus_bar_thumb_hover.png")
            unscrollable "hide"

    # Стрелки
    if engine.page_cur > 0:
        imagebutton:
            auto get_image_7dl("gui/music/buttons/mus_arrow_left_%s.png") xcenter 860 ypos 927
            activate_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            action [Function(engine.cur_page_dec), Function(sdl_mus_bar_value.change, 0)]
    if (len(music_list_7dl) - len(music_list_excluded_7dl)) > ((engine.page_cur + 1) * SDL_MUS_PAGE_SIZE):
        imagebutton:
            auto get_image_7dl("gui/music/buttons/mus_arrow_right_%s.png") xcenter 1060 ypos 927
            activate_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            action [Function(engine.cur_page_inc), Function(sdl_mus_bar_value.change, 0)]
    text engine.get_cur_page() style "sdl_mus_page_font" xcenter 0.5 ypos 923

    on "show" action [SetField(engine, "is_active", True), Function(engine.update_cur_track)]

# Панель быстрого доступа для плеера
screen music_panel_7dl(engine=sdl_mus_engine, default_music):
    modal True

    if engine.is_panel_open:
        add get_image_7dl("gui/music/frames/mus_frame_panel_show.png") xpos 0 yalign 0.5
        imagebutton xpos 7 ypos 479:
            auto get_image_7dl("gui/music/buttons/mus_prev_%s.png")
            activate_sound sdl_achv_click
            action [sdl_mus_room.Previous(), Function(engine.update_cur_track)]
        imagebutton xpos 73 ypos 479:
            auto get_image_7dl("gui/music/buttons/mus_play_%s.png")
            activate_sound sdl_achv_click
            selected not renpy.music.get_pause()
            action [PauseAudio("music", value="toggle")]
        imagebutton xpos 139 ypos 479:
            auto get_image_7dl("gui/music/buttons/mus_next_%s.png")
            activate_sound sdl_achv_click
            action [sdl_mus_room.Next(), Function(engine.update_cur_track)]
        imagebutton xpos 60 ypos 601:
            auto get_image_7dl("gui/music/buttons/mus_max_%s.png")
            activate_sound sdl_achv_click
            action [Show("music_7dl", transition=Dissolve(0.2), default_music=default_music), ToggleField(engine, "is_panel_open")]
        imagebutton xpos 162 ypos 548:
            auto get_image_7dl("gui/music/buttons/mus_panel_min_%s.png")
            activate_sound sdl_achv_click
            action [ToggleField(engine, "is_panel_open")]
    else:
        add get_image_7dl("gui/music/frames/mus_frame_panel_hide.png") xpos 0 yalign 0.5
        imagebutton xpos 7 ypos 548:
            auto get_image_7dl("gui/music/buttons/mus_panel_min_%s.png")
            activate_sound sdl_achv_click
            action [ToggleField(engine, "is_panel_open")]

    on "hide" action [SetField(engine, "is_panel_open", False)]
