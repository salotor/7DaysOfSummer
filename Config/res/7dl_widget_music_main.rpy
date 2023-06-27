init -998 python:
    style.button_text_music_7dl = Style(style.button_text_7dl)
    style.button_text_music_7dl.font = get_image_7dl("fonts/ARIALUNI.TTF")

python early:
    def check_muzlo(value):
        for k, v in music_list.items():
            if v == value:
                return k
    def check_muzlo_7dl(value):
        for k, v in music_list_7dl.items():
            if v == value:
                return k
    def get_playing_7dl(channel='music'):
        m = renpy.music.get_playing(channel=channel)
        if m is not None:
            m = parse_music(m)
        return m
    def parse_music(mus_string):
        return re.sub('<.*?>', '', str(mus_string))

    def widget_music_7dl():
        if (not persistent.music_widget_7dl) or (plthr == u"None" and (not alt_replay_on)):
            return
        else:
            # Берём трек из канала music
            m = get_playing_7dl('music')
            # Если там нет - берём из music2
            if m is None:
                m = get_playing_7dl('music2')
            # Парсим название трека
            # Выводим текущий трек
            ui.button(clicked=None, style="button_7dl", xpos=0.40, xanchor=0.0, xminimum=200, xmaximum=490)
            if m in music_list.values():
                ui.text(check_muzlo(m), style="button_text_music_7dl")
            elif m in music_list_7dl.values():
                ui.text(check_muzlo_7dl(m), style="button_text_music_7dl", yalign=0)
            elif m == None:
                ui.text("%s" % "Нет музыки", style="button_text_music_7dl")
            else:
                ui.text("%s" % "Неизвестный трек", style="button_text_music_7dl")
    config.overlay_functions.append(widget_music_7dl)
