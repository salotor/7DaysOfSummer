init: # Стили надписей
    $ style.alt_days = Style(style.default)
    $ style.alt_days.color = "#390874"
    $ style.alt_days.italic = False
    $ style.alt_days.bold = True
    $ style.alt_days.size = 64
    $ style.alt_days.text_align = 0.5

    $ style.alt_chapters = Style(style.default)
    $ style.alt_chapters.color = "#2572ff"
    $ style.alt_chapters.italic = False
    $ style.alt_chapters.bold = True
    $ style.alt_chapters.size = 48
    $ style.alt_chapters.text_align = 0.5

    $ style.alt_chapters_noir = Style(style.default)
    $ style.alt_chapters_noir.font = get_image_7dl("fonts/PT_Sans.ttf")
    $ style.alt_chapters_noir.color = "#121212"
    $ style.alt_chapters_noir.italic = False
    $ style.alt_chapters_noir.bold = True
    $ style.alt_chapters_noir.size = 90
    $ style.alt_chapters_noir.text_align = 0.5

    $ style.alt_credits = Style(style.default)
    $ style.alt_credits.color = "#EFF"
    $ style.alt_credits.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.alt_credits.drop_shadow_color = "#111"
    $ style.alt_credits.italic = False
    $ style.alt_credits.bold = False
    $ style.alt_credits.text_align = 0.5
    image alt_credits = ParameterizedText(style = "alt_credits", size = 50)

    $ style.alt_credits_jap = Style(style.alt_credits)
    $ style.alt_credits_jap.font = get_image_7dl("fonts/ARIALUNI.TTF")
    $ style.alt_credits_jap.color = "#fff"
    image alt_credits_jap = ParameterizedText(style = "alt_credits_jap", size = 50)

    $ style.alt_letter = Style(style.default)
    $ style.alt_letter.color = "#00ffff"
    $ style.alt_letter.drop_shadow = [ (-1, 0), (0, 0), (-1, 1), (0, 1) ]
    $ style.alt_letter.drop_shadow_color = "#0ff"
    $ style.alt_letter.italic = True
    $ style.alt_letter.bold = False
    image alt_letter = ParameterizedText(style = "alt_letter", size = 70)

init 3 python: # Операции с войс каналами
    def meet(who, name):
        global store
        gl = globals()
        gl[who + "_name"] = name
        store.names[who] = name

    def save_names_known():
        gl = globals()
        global store
        for x in store.names_list:
            if not (x == 'narrator' or x == 'th'):
                store.names[x] = gl["%s_name"%x]

    def make_names_unknown_7dl():
        global store
        meet('al',u"Сердитый мальчик")
        meet('ase',u"Девочка")
        meet('ba',u"Физрук")
        meet('bb',u"Начальник лагеря")
        meet('cs',u"Медсестра")
        meet('dn',u"Кудрявый")
        meet('dreamgirl',u"…")
        meet('dv',u"Рыжая")
        meet('el',u"Кудрявый")
        meet('ka',u"Вожатая 2 отряда")
        meet('me',u"Семён")
        meet('mi',u"Японка")
        meet('mt',u"Вожатая")
        meet('mz',u"Девушка в очках")
        meet('pi',u"Пионер")
        meet('sak',u"Пожилой японец")
        meet('sh',u"Очкарик")
        meet('sl',u"Блондинка")
        meet('tn',u"Странный мальчик")
        meet('un',u"Грустная девочка")
        meet('us',u"Мелкая")
        meet('uv',u"Кошкодевочка")
        meet('voice',u"Голос")

    def make_names_known_7dl():
        global store
        meet('al',u"Алька")
        meet('ase',u"Алиса")
        meet('ba',u"Саныч")
        meet('bb',u"Алексей Максимыч")
        meet('cs',u"Виола")
        meet('dn',u"Даня")
        meet('dv',u"Алиса")
        meet('el',u"Электроник")
        meet('ka',u"Катюшка")
        meet('mi',u"Мику")
        meet('mt',u"Ольга Дмитриевна")
        meet('mz',u"Женя")
        meet('sak',u"Сакишита Чихиро")
        meet('sh',u"Шурик")
        meet('sl',u"Славя")
        meet('tn',u"Тоник")
        meet('un',u"Лена")
        meet('us',u"Ульяна")
        meet('uv',u"Юля")

    def reset_names_to_default():
        global store
        store.names['voice'] = translation_new["voice"]
        store.names['me'] = translation_new["Semyon"]
        store.names['el'] = translation_new["el"]
        store.names['un'] = translation_new["un"]
        store.names['dv'] = translation_new["dv"]
        store.names['sl'] = translation_new["sl"]
        store.names['us'] = translation_new["us"]
        store.names['mt'] = translation_new["mt"]
        store.names['cs'] = translation_new["cs"]
        store.names['mz'] = translation_new["mz"]
        store.names['mi'] = translation_new["mi"]
        store.names['uv'] = translation_new["uv"]
        store.names['sh'] = translation_new["sh"]
        store.names['pi'] = translation_new["pi"]
        store.names['dreamgirl'] = translation_new["dreamgirl"]

init -265 python: # Фильтры для изображений
    # Пресеты с возможностью настройки
    def Noir(id, brightness = -0.4, tint_r = 0.2126, tint_g = 0.7152, tint_b = 0.0722, saturation = 0.5):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(brightness) * im.matrix.tint(tint_r, tint_g, tint_b) * im.matrix.saturation(saturation))
    def D3_intro(id, brightness = -0.2, opacity = 0.5):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(brightness) *  im.matrix.opacity(opacity))
    def Desat(id, brightness = -0.35, saturation = 0.5):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(brightness) *  im.matrix.saturation(saturation))
    def Desat1(id, brightness = -0.4, saturation = 0.35):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(brightness) *  im.matrix.saturation(saturation))

    # Пресеты без возможности настройки
    # Мику-матрица
    def SS_com(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.2) * im.matrix.contrast(1.6) * im.matrix.saturation(0)* im.matrix.colorize("#0aa", "#000"))
    # Алиса-матрица
    def SS_com_o(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.2) * im.matrix.contrast(1.6) * im.matrix.saturation(0)* im.matrix.colorize("#eb4", "#000"))
    # Ульяна-матрица
    def SS_com_r(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.2) * im.matrix.contrast(1.6) * im.matrix.saturation(0)* im.matrix.colorize("#a00", "#000"))

    def Sepia(id):
        return im.MatrixColor(ImageReference(id), im.matrix.saturation(0.15) * im.matrix.tint(1.0, .94, .76))

    def OldPhoto(id):
        return im.MatrixColor(ImageReference(id), im.matrix.saturation(0.6) * im.matrix.brightness(0.03))
    def Grayed(id):
        return im.MatrixColor(ImageReference(id), im.matrix.saturation(0.01))
    def Gjs(id):
        return im.MatrixColor(ImageReference(id), im.matrix.colorize("#007", "#000"))

    # Тинты для разного времени суток
    def Notch(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.2) * im.matrix.saturation(0.6))
    def Dawn(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.1) * im.matrix.tint(0.94, 0.82, 1.0))
    def Noon(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(0.2) * im.matrix.tint(1.0, 0.94, 0.82))
    def HomeCity(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.1) * im.matrix.tint(0.82, 0.84, 1.0))
    def Rained(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.4) * im.matrix.tint(0.68, 0.90, 0.8) * im.matrix.saturation(0.6))

    def filmetile(bitmap, opacity=0.1):
        return im.Tile(im.Alpha(bitmap,opacity))

init -5 python: # Заставки и названия глав
    def alt_chapter0():
        global save_name
        if alt_hotfix_no != "":
            save_name = (u"7ДЛ v.%s.%s: пролог. %s") % (alt_release_no, alt_hotfix_no, plthr)
        else:
            save_name = (u"7ДЛ v.%s: пролог. %s") % (alt_release_no, plthr)

    def alt_chapter(alt_day_number, alt_chapter_name):
        global save_name
        if alt_hotfix_no != "":
            sdn = (u"7ДЛ v.%s.%s: День %d") % (alt_release_no, alt_hotfix_no, alt_day_number)
        else:
            sdn = (u"7ДЛ v.%s: День %d") % (alt_release_no, alt_day_number)
        save_name = ((sdn) + (u" — ")) + (alt_chapter_name)
        if not persistent.chapter_off_7dl:
            _window_hide()
            renpy.scene()
            if persistent.sprite_time == "day":
                renpy.show('bg ext_stand3_7dl')
            elif persistent.sprite_time == "sunset":
                renpy.show('bg ext_stand3_sunset_7dl')
            elif persistent.sprite_time == "night":
                renpy.show('bg ext_stand3_night_7dl')
            elif persistent.sprite_time == "prolog":
                renpy.show('bg ext_stand3_prolog_7dl')
            elif persistent.sprite_time == "noir":
                renpy.show('anim_noir')
            renpy.pause(1.0)
            renpy.transition(dissolve)

            if routetag == "dvdj":
                renpy.show("dv normal pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)

            elif routetag == "dv7dl":
                renpy.show("dv normal pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "dv7dlbad":
                renpy.show("dv guilty pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "dv7dlgood":
                renpy.show("dv smile pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)

            elif routetag == "mi7dl":
                renpy.show("mi normal pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dlbad":
                renpy.show("mi cry pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dlgood":
                renpy.show("mi happy pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dldress":
                renpy.show("mi normal dress", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7rej":
                renpy.show("mi serious pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7true":
                renpy.show("mi shy pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dlvoca":
                renpy.show("mi shy voca", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dlcas":
                renpy.show("mi happy casual", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dlcas1":
                renpy.show("mi sad casual", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dlcas2":
                renpy.show("mi cry casual", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dlvoca1":
                renpy.show("mi sad voca", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)

            elif routetag == "sl":
                renpy.show("sl normal pioneer2", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sltrue":
                renpy.show("sl shy sport", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "slbad":
                renpy.show("sl sad pioneer2", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)

            elif routetag == "sl7dl":
                renpy.show("sl normal pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dl_herc":
                renpy.show("sl smile pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dl_loki":
                renpy.show("sl smile2 pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dl_sport":
                renpy.show("sl smile sport", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dl_dress":
                renpy.show("sl smile2 dress", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dlneu":
                renpy.show("sl serious casual", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dlgood":
                renpy.show("sl happy casual", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dluv":
                renpy.show("sl normal_uv dress", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dlbad":
                renpy.show("sl cry pioneer2", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)

            elif routetag == "un":
                renpy.show("un normal pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "un7dl":
                renpy.show("un normal pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "un7dlbad":
                renpy.show("un sorrow modern", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "un7dlgood":
                renpy.show("un smile modern", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)

            elif routetag == "mt7dl":
                renpy.show("mt grin pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mt7dl_bad":
                renpy.show("mt sad pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)

            elif routetag == "us_7dl_px_good":
                renpy.show("us smile sport", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "us_7dl_px_good_surp":
                renpy.show("us surp1 sport", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)

            elif routetag == "us_7dl":
                renpy.show("us normal pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "us_7dl_good":
                renpy.show("us laugh pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "us_7dl_bad":
                renpy.show("us sad pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)

            elif routetag == "Noir":
                renpy.pause(0.3)

            else:
                renpy.show("owl")
                renpy.pause(0.3)

            dn = (u"7ДЛ: День %d") % (alt_day_number)
            if persistent.sprite_time == "prolog":
                renpy.show('day_num', what=Text(dn, style=style.alt_days,xcenter=0.5215,ycenter=0.25))
                renpy.show('day_text', what=Text(alt_chapter_name, style=style.alt_chapters,xcenter=0.5215,ycenter=0.35,xmaximum=720))
            elif persistent.sprite_time == "noir":
                renpy.show('day_text', what=Text(alt_chapter_name, style=style.alt_chapters_noir,xcenter=0.5215,ycenter=0.35,xmaximum=720))
            else:
                renpy.show('day_num', what=Text(dn, style=style.alt_days,xcenter=0.5215,ycenter=0.35))
                renpy.show('day_text', what=Text(alt_chapter_name, style=style.alt_chapters,xcenter=0.5215,ycenter=0.45,xmaximum=720))

            renpy.pause(3)
            renpy.scene()
            renpy.show('bg black')
            renpy.transition(blind_r)
            if noir_interface:
                noir_set_mode_adv()
            else:
                set_mode_adv()
            _window_auto = True

    def alt_save_name(alt_day_number, alt_chapter_name):
        global save_name
        if alt_hotfix_no != "":
            sdn = (u"7ДЛ v.%s.%s: День %d") % (alt_release_no, alt_hotfix_no, alt_day_number)
        else:
            sdn = (u"7ДЛ v.%s: День %d") % (alt_release_no, alt_day_number)
        save_name = ((sdn) + (u" — ")) + (alt_chapter_name)

init -1001 python: # Дополнительные звуковые каналы
    renpy.music.register_channel("music2", "music", True)

init -1000 python: # Путь до папки мода
    default_7dl_path = 'scenario_alt/'

init -999 python: # Функции для получения пути к ресурсам
    def get_image_7dl(file):
        return default_7dl_path+"Pics/%s" % (file)
    def get_sfx_7dl(file):
        return default_7dl_path+"Sound/sfx/%s" % (file)
    def get_ambience_7dl(file):
        return default_7dl_path+"Sound/ambience/%s" % (file)
    def get_music_7dl(file):
        return default_7dl_path+"Sound/music/%s" % (file)
    def get_sprite_7dl(file):
        return default_7dl_path+"Pics/sprites/%s" % (file)
    def get_sprite_ori(file):
        return get_image("sprites/%s") % (file)

init -999 python: # Прочие функции
    def alt_pause(time): # Пауза со скрытием интерфейса
        _window_hide()
        renpy.pause(time)
        _window_auto = True
    def alt_binder_update():
        if (persistent.mi_7dl_good_human or persistent.mi_7dl_good_star) and persistent.dv_7dl_good_ussr and (persistent.sl_7dl_loki_good or persistent.sl_7dl_herc_good or persistent.sl_7dl_dr_good) and persistent.un_7dl_good_ussr and persistent.mt_7dl_good and persistent.us_7dl_good:
            persistent.alt_binder = True
        else:
            persistent.alt_binder = False

init python: # Новые переходы

    import math

    class Shaker(object):

        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }

        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child

        def __call__(self, t, sizes):
            # Float to integer… turns floating point numbers to
            # integers.
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor

            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)

    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)

        return renpy.display.layout.Motion(move,
                      time,
                      child,
                      add_sizes=True,
                      **properties)

    Shake = renpy.curry(_Shake)

### ФИКСЫ ДЛЯ БЛ И МОДОВ ###

init -1000 python: # Для совместимости с одной из ранних сборок на RenPy 7.0.0
    if not 'translation_new' in globals():
        translation_new = translation

init 9999 python: # Боремся с трейсбеками из-за ПЛ
    try:
        del(max)
    except NameError:
        pass

# Чиним баг в БЛ, вызывающий ошибку "Can't pickle <class 'store.Layout'>: attribute lookup store.Layout failed"
init -1399 python hide:
    try:
        if _preferences.language == "spanish":
            layout.ARE_YOU_SURE = "¿Estás seguro?"
            layout.DELETE_SAVE = "¿Estás seguro de que quieres eliminar esta partida?"
            layout.OVERWRITE_SAVE = "¿Estás seguro de que quieres sobrescribir tu partida?"
            layout.LOADING = "Cargar una partida te hará perder el progreso no guardado.\n¿Estás seguro de que quieres hacerlo?"
            layout.QUIT = "¿Estás seguro de que quieres salir?"
            layout.MAIN_MENU = "¿Estás seguro de que quieres volver al menú principal?\nSe perderá el progreso no guardado."
            layout.SLOW_SKIP = "¿Estás seguro de que quieres avanzar?"
            layout.FAST_SKIP_UNSEEN = "¿Estás seguro de que quieres avanzar hasta la siguiente elección?"
            layout.FAST_SKIP_SEEN = "¿Estás seguro de que quieres avanzar hasta diálogo no visto o hasta la próxima elección?"
        elif _preferences.language == "italian":
            layout.ARE_YOU_SURE = "Sei sicuro?"
            layout.DELETE_SAVE = "Sei sicuro di voler eliminare questo salvataggio?"
            layout.OVERWRITE_SAVE = "Sei sicuro di voler sovrascrivere questo salvataggio?"
            layout.LOADING = "Caricando questa partita perderai i progressi non salvati.\nSei sicuro di volerlo fare?"
            layout.QUIT = "Sei sicuro di voler uscire dal gioco?"
            layout.MAIN_MENU = "Sei sicuro di voler tornare al menu principale?\nI progressi non salvati andranno persi."
            layout.SLOW_SKIP = "Sei sicuro di voler iniziare a saltare le frasi?"
            layout.FAST_SKIP_UNSEEN = "Sei sicuro di voler saltare le frasi fino alla prossima scelta?"
            layout.FAST_SKIP_SEEN = "Sei sicuro di voler saltare il testo fino alla prossima frase non letta o alla prossima scelta?"
        elif _preferences.language == "english":
            layout.ARE_YOU_SURE = "Are you sure?"
            layout.DELETE_SAVE = "Are you sure you want to delete this save?"
            layout.OVERWRITE_SAVE = "Are you sure you want to overwrite your save?"
            layout.LOADING = "Loading will lose unsaved progress.\nAre you sure you want to do this?"
            layout.QUIT = "Are you sure you want to quit?"
            layout.MAIN_MENU = "Are you sure you want to return to the main menu?\nThis will lose unsaved progress."
            layout.SLOW_SKIP = "Are you sure you want to begin skipping?"
            layout.FAST_SKIP_UNSEEN = "Are you sure you want to skip to the next choice?"
            layout.FAST_SKIP_SEEN = "Are you sure you want to skip to unseen dialogue or the next choice?"
        elif _preferences.language == "chinese":
            layout.ARE_YOU_SURE = "你确定吗？"
            layout.DELETE_SAVE = "你确定删除存档吗？"
            layout.OVERWRITE_SAVE = "你确定覆盖存档吗？"
            layout.LOADING = "读档后将失去当前进度。\n你确定吗？"
            layout.QUIT = "你确定要退出吗?"
            layout.MAIN_MENU = "你确定返回主菜单吗？\n这样会丢失当前进度。"
            layout.SLOW_SKIP = "你确定开始跳过吗？"
            layout.FAST_SKIP_UNSEEN = "你确定跃至下一选项吗？"
            layout.FAST_SKIP_SEEN = "你确定要跃至未读信息或下一选项吗？"
        elif _preferences.language == "french":
            layout.ARE_YOU_SURE = "Êtes-vous sûr ?"
            layout.DELETE_SAVE = "Êtes-vous sûr de vouloir supprimer cette sauvegarde ?"
            layout.OVERWRITE_SAVE = "Êtes-vous sûr de vouloir écraser cette sauvegarde ?"
            layout.LOADING = "Le chargement entraînera la perte de votre progression depuis la dernière sauvegarde.\nÊtes-vous sûr de vouloir faire cela ?"
            layout.QUIT = "Êtes-vous sûr de vouloir quitter ??"
            layout.MAIN_MENU = "Êtes-vous sûr de vouloir retourner au menu principal ?\nVotre progression depuis la dernière sauvegarde sera perdue."
            layout.SLOW_SKIP = "Êtes-vous sûr de vouloir sauter les dialogues ?"
            layout.FAST_SKIP_UNSEEN = "Êtes-vous sûr de vouloir sauter les dialogues jusqu’au prochain choix ?"
            layout.FAST_SKIP_SEEN = "Êtes-vous sûr de vouloir sauter les dialogues non vus jusqu’au prochain choix ?"
        else:
            layout.MAIN_MENU = 'Вы действительно хотите выйти в главное меню?\nНесохраненные данные будут потеряны.'
            layout.ARE_YOU_SURE = "Вы уверены?"
            layout.DELETE_SAVE = "Вы уверены, что хотите удалить это сохранение?"
            layout.OVERWRITE_SAVE = "Вы уверены, что хотите переписать это сохранение?"
            layout.LOADING = "Загрузка приведёт к потере несохранённых данных.\nВы уверены, что хотите сделать это?"
            layout.QUIT = "Вы уверены, что хотите выйти?"
            layout.SLOW_SKIP = "Вы уверены, что хотите начать пропуск?"
            layout.FAST_SKIP_UNSEEN = "Вы уверены, что хотите пропустить всё до следующего выбора?"
            layout.FAST_SKIP_SEEN = "Вы уверены, что хотите пропустить всё до следующего нового диалога или выбора?"
    except Exception:
        pass

init 2 python:
    def translate():
        pass

### === ###

### КАСТОМНЫЕ МЕНЮ ###

init python:
    def alt_screens_save():
        renpy.display.screen.screens[("original_game_menu_selector", None)] =         renpy.display.screen.screens[("game_menu_selector", None)]

    alt_screens_save()

    def alt_screens_on():
        renpy.display.screen.screens[("game_menu_selector", None)] =                  renpy.display.screen.screens[("alt_game_menu_selector", None)]

    def alt_screens_load():
        renpy.display.screen.screens[("game_menu_selector", None)] =                  renpy.display.screen.screens[("original_game_menu_selector", None)]

    orig_config_version = config.version

    def alt_interface_on():
        # пишем версию 7дл в трейсбеках
        global alt_release_no
        global alt_hotfix_no
        if not "7DL" in config.version:
            if alt_save_release_no == alt_release_no:
                config.version = config.version + " + 7DL v.%s.%s" % (alt_release_no, alt_hotfix_no)
            else:
                config.version = config.version + " + 7DL v.%s.%s (save v.%s)" % (alt_release_no, alt_hotfix_no, alt_save_release_no)
        alt_screens_on()
        config.window_auto_hide = [ "scene", "call screen", "menu", "pause" ]
        persistent.alt_interface = True

    def alt_interface_off():
        global orig_config_version
        config.version = orig_config_version
        alt_screens_load()
        plthr = u"None"
        config.window_auto_hide = [ "scene", "call screen", "menu" ]
        persistent.alt_interface = False

    def alt_exit():
        global th_prefix
        global th_suffix
        alt_interface_off()
        reset_names_to_default()
        if not persistent.thoughts_tilde_7dl:
            th_prefix = "~ "
            th_suffix = " ~"
        reload_names()

# Замена экрана истории в реплеях
    def replay_screens_save():
        renpy.display.screen.screens[("original_text_history_screen", None)] =         renpy.display.screen.screens[("text_history_screen", None)]
        renpy.display.screen.screens[("original_preferences", None)] =                 renpy.display.screen.screens[("preferences", None)]

    replay_screens_save()

    def replay_screens_on():
        renpy.display.screen.screens[("text_history_screen", None)] =                  renpy.display.screen.screens[("replay_text_history_screen", None)]
        renpy.display.screen.screens[("preferences", None)] =                          renpy.display.screen.screens[("replay_preferences", None)]

    def replay_screens_load():
        renpy.display.screen.screens[("text_history_screen", None)] =                  renpy.display.screen.screens[("original_text_history_screen", None)]
        renpy.display.screen.screens[("preferences", None)] =                          renpy.display.screen.screens[("original_preferences", None)]

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
            if persistent.alt_config_developer:
                clicked (ShowMenu('preferences'), Hide('alt_game_menu_selector'))
            else:
                clicked (ShowMenu('alt_preferences'), Hide('alt_game_menu_selector'))
        hotspot (0, 343, 660, 65):
            focus_mask None
            clicked ShowMenu('quit')

screen alt_preferences:
    tag menu
    modal True
    $ translate()
    $ bar_null = Frame(get_image("gui/settings/bar_null.png"),36,36)
    $ bar_full = Frame(get_image("gui/settings/bar_full.png"),36,36)
    window:
        background get_image("gui/settings/preferences_bg.jpg")
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
                grid 1 20:
                    xfill True
                    spacing 15
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
    $ translate()
    $ bar_null = Frame(get_image("gui/settings/bar_null.png"),36,36)
    $ bar_full = Frame(get_image("gui/settings/bar_full.png"),36,36)
    window:
        background get_image("gui/settings/preferences_bg.jpg")
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

### === ###

### РЕПЛЕИ ###

init python:
    # Списки всех ачивок
    sdl_achv_mi_names = [
        "mi_7dl_shard",
        "mi_7dl_good_human",
        "mi_7dl_good_star",
        "mi_7dl_neu_human",
        "mi_7dl_loki_exc",
        "mi_7dl_herc_exc",
        "mi_7dl_dr_exc",
        "mi_7dl_bad_human",
        "mi_7dl_bad_star",
        "mi_dj_true",
        "mi_dj_good_jap",
        "mi_dj_good_rf",
        "mi_dj_bad"
        ]
    sdl_achv_dv_names = [
        "dv_7dl_shard",
        "dv_7dl_good_ussr",
        "dv_7dl_good_rf",
        "dv_7dl_rej_ussr",
        "dv_7dl_rej_rf",
        "dv_7dl_tran_un",
        "dv_7dl_loki_exc",
        "dv_7dl_bad",
        "dv_dj_true",
        "dv_dj_good",
        "dv_dj_neu",
        "dv_dj_rej",
        "dv_dj_herc_exc",
        "dv_dj_loki_exc",
        "dv_dj_dr_exc",
        "dv_dj_bad"
        ]
    sdl_achv_sl_names = [
        "sl_7dl_shard",
        "sl_7dl_good_rf",
        "sl_7dl_loki_good",
        "sl_7dl_loki_neu",
        "sl_7dl_loki_rej",
        "sl_7dl_herc_good",
        "sl_7dl_herc_neu",
        "sl_7dl_dr_good",
        "sl_7dl_dr_good2",
        "sl_7dl_bad",
        "sl_cl_int_true",
        "sl_cl_int_good",
        "sl_cl_int_rej",
        "sl_cl_int_bad",
        "sl_cl_good_ussr",
        "sl_cl_good_rf",
        "sl_cl_good_rf2",
        "sl_cl_rej_rf",
        "sl_cl_rej",
        "sl_cl_loki_exc",
        "sl_cl_bad"
        ]
    sdl_achv_un_names = [
        "un_7dl_shard",
        "un_7dl_true_tran",
        "un_7dl_good_ussr",
        "un_7dl_good_rf",
        "un_7dl_rej",
        "un_7dl_bad",
        "un_fz_rr_true",
        "un_fz_rr_good",
        "un_fz_rr_bad",
        "un_fz_good",
        "un_fz_neu",
        "un_fz_rj",
        "un_fz_bad",
        "un_fz_bad_post"
        ]
    sdl_achv_mt_names = [
        "mt_7dl_shard",
        "mt_7dl_true",
        "mt_7dl_good",
        "mt_7dl_neu",
        "mt_7dl_herc_exc",
        "mt_7dl_bad"
        ]
    sdl_achv_us_names = [
        "us_7dl_shard",
        "us_7dl_true",
        "us_7dl_good",
        "us_7dl_tran_un",
        "us_7dl_tran_mi",
        "us_7dl_bad",
        "us_7dl_px_true",
        "us_7dl_px_good"
        ]
    sdl_achv_me_names = [
        "me_neu_bad"
        ]
    sdl_achv_va_names = [
        "alt_lost",
        "alt_lamp",
        "alt_deep",
        "alt_qte",
        "alt_victim",
        "alt_drunk"
        ]
    sdl_achv_names = [
        sdl_achv_mi_names,
        sdl_achv_dv_names,
        sdl_achv_sl_names,
        sdl_achv_un_names,
        sdl_achv_mt_names,
        sdl_achv_us_names,
        sdl_achv_me_names,
        sdl_achv_va_names
        ]

    # Добавляем ключ в словарь
    def sdl_add_to_dict(x, key, val):
        z = x.copy()
        if key != None:
            z.update({key : val})
        return z

    # Увеличиваем счётчик концовок
    def sdl_persistent_inc(p):
        if getattr(persistent, p):
            setattr(persistent, p, getattr(persistent, p) + 1)
        else:
            setattr(persistent, p, 1)
        alt_binder_update()

    # Получаем счётчик концовок
    def sdl_achv_count():
        total = 0;
        for group in sdl_achv_names:
            for name in group:
                if getattr(persistent, name):
                    total += getattr(persistent, name)
        return total

    # Генерируем фразу
    def sdl_achv_count_phrase():
        text = ''
        count = sdl_achv_count()
        if (count <= 5):
            text = 'Пять? Десять раз?'
        elif (count <= 10):
            text = 'Десять? Двадцать раз?'
        elif (count <= 20):
            text = 'Двадцать? Тридцать раз?'
        elif (count <= 30):
            text = 'Тридцать? Сорок раз?'
        elif (count <= 40):
            text = 'Сорок? Пятьдесят раз?'
        elif (count <= 50):
            text = 'С полсотни раз?'
        elif (count <= 100):
            text = 'Десятки раз?'
        else:
            text = 'Сотни раз?'

        return text

    # Сбрасываем счётчик концовок
    def sdl_persistent_res(p):
        setattr(persistent, p, 0)

    # Повтор
    class sdl_Replay:
        def __init__(self, label, scope, meets=None, meet_restr=None, music=None, ambience=None, sound_loop=None, vars=None, func_in=None, func_out=None):
            self.label = label
            self.scope = scope
            self.meets = meets
            self.meet_restr = meet_restr
            self.music = music
            self.ambience = ambience
            self.sound_loop = sound_loop
            self.vars = vars
            self.func_in = func_in
            self.func_out = func_out

        def get_label(self):
            return self.label

        def get_scope(self):
            return sdl_add_to_dict(self.scope, "cur_replay", self)

        def get_meets(self):
            return self.meets

        def get_music(self):
            return self.music

        def get_ambience(self):
            return self.ambience

        def get_sound_loop(self):
            return self.sound_loop

        def get_vars(self):
            return self.vars

        def get_func_in(self):
            return self.func_in

        def get_func_out(self):
            return self.func_out

        def apply_scope(self):
            global store

            for s in self.scope:
                setattr(store, s, self.scope[s])
            return

        def apply_meets(self):
            global store

            if self.meets != None:
                for c in self.meets:
                    # Проверяем ограничения флагов
                    if self.meet_restr != None:
                        if c in self.meet_restr:
                            if getattr(store, self.meet_restr[c]):
                                continue
                    meet(c, self.meets[c])
            return

        def apply_vars(self):
            global store

            if self.vars != None:
                for f in self.vars:
                    setattr(store, f.get_variable(), f.get_cur_value())
                    f.reset()
            return

    # Персонаж-протагонист
    class sdl_Character:
        def __init__(self, icon, char_mask, text, variable):
            self.icon = icon
            self.char_mask = char_mask
            self.text = text
            self.variable = variable

        def get_icon(self):
            return self.icon

        def get_char_mask(self):
            return self.char_mask

        def get_text(self):
            return self.text

        def get_variable(self):
            return self.variable

    # Переменные
    class sdl_Var:
        def __init__(self, type, variable, text):
            self.type = type
            self.variable = variable
            self.text = text

        def get_type(self):
            return self.type

        def get_variable(self):
            return self.variable

        def get_text(self):
            return self.text

    class sdl_Bool(sdl_Var):
        def __init__(self, variable, text):
            sdl_Var.__init__(self, 0, variable, text)
            self.cur_value = False

        def toggle_value(self):
            self.cur_value = not self.cur_value

        def get_cur_value(self):
            return self.cur_value

        def reset(self):
            self.cur_value = False

    class sdl_Int(sdl_Var):
        def __init__(self, variable, text, range):
            sdl_Var.__init__(self, 1, variable, text)
            self.cur_value = 0
            self.range = range

        def cur_val_inc(self):
            self.cur_value += 1

        def cur_val_dec(self):
            self.cur_value -= 1

        def get_range(self):
            return self.range

        def get_cur_value(self):
            return self.cur_value

        def reset(self):
            self.cur_value = 0

    class sdl_Enum(sdl_Var):
        def __init__(self, variable, text, values):
            sdl_Var.__init__(self, 2, variable, text)
            self.cur_val_idx = 0
            self.values = values

        def cur_val_idx_inc(self):
            self.cur_val_idx += 1

        def cur_val_idx_dec(self):
            self.cur_val_idx -= 1

        def get_values_amount(self):
            return len(self.values)

        def get_cur_val_idx(self):
            return self.cur_val_idx

        def get_cur_value(self):
            return self.values[self.cur_val_idx][0]

        def get_cur_descr(self):
            return self.values[self.cur_val_idx][1]

        def reset(self):
            self.cur_val_idx = 0

    class sdl_List(sdl_Var):
        def __init__(self, variable, text, values, max_len):
            sdl_Var.__init__(self, 3, variable, text)
            self.cur_value = []
            self.values = values
            self.max_len = max_len

        def add_value(self, val):
            if len(self.cur_value) < self.max_len:
                self.cur_value.append(val)

        def del_value(self, val):
            self.cur_value.remove(val)

        def is_full(self):
            return len(self.cur_value) == self.max_len

        def get_values(self):
            return self.values

        def get_cur_value(self):
            return self.cur_value

        def reset(self):
            self.cur_value = []

    # Объекты всех переменных
    sdl_var_b_d1_el_foll = sdl_Bool('alt_day1_el_followed', "Сбежал от Алисы")
    sdl_var_b_d1_sl_met  = sdl_Bool('alt_day1_sl_met', "Знаком со Славей")
    sdl_var_b_d1_us_shot = sdl_Bool('alt_day1_us_shotted', "Пнул мячик")
    sdl_var_b_d1_un_talk = sdl_Bool('alt_day1_un_talk', "Подошёл к Лене вечером в 1 дне")
    # ====================
    sdl_var_b_d2_dv_chas = sdl_Bool('alt_day2_dv_chased', "Бегал от Алисы после турнира")
    sdl_var_b_d2_dv_hous = sdl_Bool('alt_day2_dv_us_house_visited', "Посетил на обходе дом Алисы и Ульяны")
    sdl_var_b_d2_me_mini = sdl_Bool('alt_day2_minijack', "Добыл миниджек")
    sdl_var_b_d2_mi_met  = sdl_Bool('alt_day2_mi_met', "Знаком с Мику")
    sdl_var_b_d2_mi_snap = sdl_Bool('alt_day2_mi_snap', "Сфотографировался с Мику")
    sdl_var_b_d2_mt_help = sdl_Bool('alt_day2_mt_help', "Помог Ольге с путёвками")
    sdl_var_b_d2_sl_chas = sdl_Bool('alt_day2_sl_chased', "Пытался проследить за Славей после турнира")
    sdl_var_b_d2_sh_met  = sdl_Bool('alt_day2_sh_met', "Знаком с Шуриком")
    sdl_var_b_d2_us_dubs = sdl_Bool('alt_day2_us_dubstep', "Устроил мини-дискотеку")
    sdl_var_b_d2_us_shen = sdl_Bool('alt_day2_us_shenan', "Устроил Ульяне трюк со стаканом")
    sdl_var_b_d2_us_esca = sdl_Bool('alt_day2_us_escape', "Сбежал с Ульяной")
    # ====================
    sdl_var_b_d3_me_duty = sdl_Bool('alt_day3_duty', "Назначен дежурным на 3 день")
    sdl_var_b_d3_me_tec2 = sdl_Bool('alt_day3_technoquest2', "Согласился помочь кибернетикам на крыше")
    sdl_var_b_d3_mi_reje = sdl_Bool('alt_day3_mi_rejected', "Отказал Мику в танцах")
    sdl_var_b_d3_sl_invi = sdl_Bool('alt_day3_sl_invite', "Славя попросила помочь с организацией танцев")
    sdl_var_b_d3_sl_bath = sdl_Bool('alt_day3_sl_bath_voy', "Подглядывал за Славей в бане")
    sdl_var_b_d3_un_fz_walk    = sdl_Bool('alt_day3_un_fz_walk', "Прогулялся с Леной вместо дискотеки")
    sdl_var_b_d3_un_fz_stories = sdl_Bool('alt_day3_un_fz_stories', "Рассказывал истории с компанией Ульяны")
    sdl_var_b_d3_un_fz_transit = sdl_Bool('alt_day3_un_fz_neu_transit', "Танцевал с Леной, френдзоня её")
    # ====================
    sdl_var_b_d4_mi_7dl_savi = sdl_Bool('alt_day4_mi_7dl_ev_savior', "Не оставил Мику спать одну в музклубе")
    sdl_var_b_d5_mi_7dl_voye = sdl_Bool('alt_day5_mi_7dl_voyeur', "Подглядывал за Мику в бане")
    sdl_var_b_d5_mi_7dl_kiss = sdl_Bool('alt_day5_mi_7dl_kiss', "Поцеловал Мику на костре")
    sdl_var_b_d6_mi_7dl_left = sdl_Bool('alt_day6_mi_7dl_left', "Мику уехала")
    # ====================
    sdl_var_b_d4_mi_dj_hedg    = sdl_Bool('alt_day4_mi_dj_hedg', "Поймал хыщника")
    sdl_var_b_d4_mi_dj_sl_blac = sdl_Bool('alt_day4_mi_dj_blackmailed', "Славя напомнила про подглядывание в бане")
    sdl_var_b_d4_mi_dj_sl_repe = sdl_Bool('alt_day4_mi_dj_sl_repet', "Обедал со Славей")
    sdl_var_b_d4_mi_dj_reas    = sdl_Bool('alt_day4_mi_dj_reasons', "Пытался найти причины плохого самочувствия Мику")
    sdl_var_b_d5_mi_dj_dv_blad = sdl_Bool('alt_day5_mi_dj_dv_blade', "Вернул бритву Алисе")
    sdl_var_b_d5_mi_dj_dv_kiss = sdl_Bool('alt_day5_mi_dj_dv_kissing', "Получил поцелуй от Алисы")
    sdl_var_b_d5_mi_dj_hent    = sdl_Bool('alt_day5_mi_dj_hentai_done', "Был хентай вечером 5 дня")
    sdl_var_b_d6_mi_dj_walk    = sdl_Bool('alt_day6_mi_dj_walkman', "Подарил плеер Мику")
    sdl_var_b_d6_mi_dj_sl_evil = sdl_Bool('alt_day6_mi_dj_sl_evil', "Разозлил Славю")
    sdl_var_b_d6_mi_dj_un_evil = sdl_Bool('alt_day6_mi_dj_un_evil', "Разозлил Лену")
    sdl_var_b_d6_mi_dj_mi_reje = sdl_Bool('alt_day6_mi_dj_rejected', "Мику отказалась танцевать")
    sdl_var_b_d6_mi_dj_me_evil = sdl_Bool('alt_day6_mi_dj_me_evil', "Пытался бороться со страхом")
    sdl_var_b_d6_mi_dj_hent    = sdl_Bool('alt_day6_mi_dj_hentai2', "Был хентай вечером 6 дня")
    # ====================
    sdl_var_b_d4_dv_7dl_extr    = sdl_Bool('alt_day4_dv_7dl_extra_key', "Отцепил себе ключик")
    sdl_var_b_d4_dv_7dl_ba_conv = sdl_Bool('alt_day4_dv_7dl_ba_conv', "Поздоровался с Санычем")
    sdl_var_b_d4_dv_7dl_cs_help = sdl_Bool('alt_day4_dv_7dl_help_cs', "Согласился помочь Виоле")
    sdl_var_b_d4_dv_7dl_port    = sdl_Bool('alt_day4_dv_7dl_portwine', "Добыл бутылку портвейна")
    sdl_var_b_d4_dv_7dl_hent    = sdl_Bool('alt_day4_dv_7dl_hentai_done', "Был хентай в медпункте")
    sdl_var_b_d6_dv_7dl_tran    = sdl_Bool('alt_day6_dv_7dl_transit', "Флаг транзита")
    # ====================
    sdl_var_b_d6_dv_dj_bett    = sdl_Bool('alt_day6_dv_dj_bet', "Поспорил с Алисой")
    sdl_var_b_d6_dv_dj_secr    = sdl_Bool('alt_day6_dv_dj_secret', "Узнал правду про Алису")
    sdl_var_b_d6_dv_dj_dvrn    = sdl_Bool('alt_day6_dv_dj_dv_run', "Решил догнать Алису")
    # ====================
    sdl_var_b_d4_sl_7dl_work    = sdl_Bool('alt_day4_sl_7dl_workout', "Вышел на пробежку утром 4 дня")
    sdl_var_b_d4_sl_7dl_help    = sdl_Bool('alt_day4_sl_7dl_help1', "Согласился таскать колонки")
    sdl_var_b_d4_sl_7dl_rend    = sdl_Bool('alt_day4_sl_7dl_herc_rendezvous', "Договорился о свидании со Славей")
    sdl_var_b_d4_sl_7dl_appl    = sdl_Bool('alt_day4_sl_7dl_herc_appletree', "Ходил с Ульянкой за яблоками")
    sdl_var_b_d5_sl_7dl_work    = sdl_Bool('alt_day5_sl_7dl_workout', "Вышел на пробежку утром 5 дня")
    sdl_var_b_d5_sl_7dl_true    = sdl_Bool('alt_day5_sl_7dl_loki_true', "Поговорил со Славей о правде")
    sdl_var_b_d5_sl_7dl_defe    = sdl_Bool('alt_day5_sl_7dl_defend', "Заступился за Ульянку перед Ольгой")
    sdl_var_b_d5_sl_7dl_olro    = sdl_Bool('alt_day5_sl_7dl_olroad', "Принял помощь Ульяны с Леной")
    sdl_var_b_d5_sl_7dl_hent    = sdl_Bool('alt_day5_sl_7dl_hentai_done', "Был хентай вечером 5 дня")
    sdl_var_b_d5_sl_7dl_sick    = sdl_Bool('alt_day5_sl_7dl_herc_sick', "Простудился в 5 день")
    sdl_var_b_d6_sl_7dl_forg    = sdl_Bool('alt_day6_sl_7dl_forgive', "Простил Славю")
    sdl_var_b_d6_sl_7dl_hent    = sdl_Bool('alt_day6_sl_7dl_hentai_done', "Был хентай вечером 6 дня")
    sdl_var_b_d6_sl_7dl_squa    = sdl_Bool('alt_day6_sl_7dl_square', "Пошёл на площадь")
    # ====================
    sdl_var_b_d4_sl_cl_tuti    = sdl_Bool('alt_day4_sl_cl_tut_iz', "Не пошёл смотреть на гуделку")
    sdl_var_b_d4_sl_cl_left    = sdl_Bool('alt_day4_sl_cl_tut_lf', "Славя с Леной ушли на поиски без нас")
    sdl_var_b_d4_sl_cl_un_reje = sdl_Bool('alt_day4_sl_cl_un_rej', "Выступил против участия Лены в поисках")
    sdl_var_b_d5_sl_cl_hent    = sdl_Bool('alt_day5_sl_cl_hentai_done', "Был хентай вечером 5 дня")
    sdl_var_b_d6_sl_cl_shir    = sdl_Bool('alt_day6_sl_cl_shirt', "Решил принарядиться к дискотеке")
    sdl_var_b_d6_sl_cl_hent    = sdl_Bool('alt_day6_sl_cl_hentai_done', "Был хентай в медпункте")
    sdl_var_b_d7_sl_cl_code    = sdl_Bool('alt_day7_sl_cl_code', "Нашёл бумажку с кодом")
    # ====================
    sdl_var_b_d4_un_7dl_sear    = sdl_Bool('alt_day4_un_7dl_morning_searching', "Отпросился с линейки искать Лену")
    sdl_var_b_d4_un_7dl_hent    = sdl_Bool('alt_day4_un_7dl_hen1', "Был хентай на 4 день")
    sdl_var_b_d4_un_7dl_duck    = sdl_Bool('alt_day4_un_7dl_ducks', "Обучал шестой отряд «Танцу маленьких утят»")
    sdl_var_b_d4_un_7dl_ba_aler = sdl_Bool('alt_day4_un_7dl_ba_alerted', "Саныч спалил целующимися на корте")
    sdl_var_b_d4_un_7dl_expl    = sdl_Bool('alt_day4_un_7dl_dv_us_explosives', "Не помешал рыжим делать взрывчатку")
    # ====================
    sdl_var_b_d4_un_fz_old_road = sdl_Bool('alt_day4_un_fz_old_road', "Случайно вышел на Дорогу")
    sdl_var_b_d4_un_fz_us_run   = sdl_Bool('alt_day4_un_fz_us_run', "Побежал за Ульяной из столовой")
    sdl_var_b_d5_un_fz_us_break = sdl_Bool('alt_day5_un_fz_us_breakfast', "Завтракал утром 5 дня с Ульяной")
    sdl_var_b_d5_un_fz_un_run   = sdl_Bool('alt_day5_un_fz_un_run', "Побежал за Леной со свечки")
    sdl_var_b_d5_un_fz_old_camp = sdl_Bool('alt_day5_un_fz_old_camp', "Сходил в старый лагерь")
    # ====================
    sdl_var_b_d6_un_fz_hent     = sdl_Bool('alt_day6_un_fz_hentai', "Был хентай с Леной")
    # ====================
    sdl_var_b_d6_us_7dl_help    = sdl_Bool('alt_day6_us_7dl_help', "Не бросил Ульянку и принёс шорты")
    # ====================
    sdl_var_b_d6_us_7dl_px_sl_join  = sdl_Bool('alt_day6_us_7dl_px_sl_join', "Славя согласилась присоединиться к поискам")
    # ====================
    sdl_var_b_d4_me_neu_voll    = sdl_Bool('alt_day4_me_neu_volley', "Уговорил вожатую сыграть в волейбол")
    sdl_var_b_d4_me_neu_mi_song = sdl_Bool('alt_day4_me_neu_mi_songs', "Готовил с Мику песни к костру")
    sdl_var_b_d4_me_neu_mt_volo = sdl_Bool('alt_day4_me_neu_mt_volonteer', "Задолжал Ольге велосипед")
    sdl_var_b_d4_me_neu_mt_diar = sdl_Bool('alt_day4_me_neu_mt_diary', "Прочитал первую часть дневника Ольги")
    sdl_var_b_d4_me_neu_us_debt = sdl_Bool('alt_day4_me_neu_us_debt', "Заглянул к кибернетикам после обеда")
    sdl_var_b_d4_me_neu_cs_debt = sdl_Bool('alt_day4_me_neu_cs_debt', "Провёл вечер в компании двух дам")
    sdl_var_b_d4_me_neu_mz_news = sdl_Bool('alt_day4_me_neu_mz_newspaper', "Помог починить полку в библиотеке")
    sdl_var_b_d5_me_neu_sprt    = sdl_Bool('alt_day5_me_neu_sport', "Был разыгран добрым дедушкой Санычем")
    sdl_var_b_d5_me_neu_nwpp    = sdl_Bool('alt_day5_me_neu_nwsppr', "Посетил библиотеку в тихий час")
    sdl_var_b_d5_me_neu_pota    = sdl_Bool('alt_day5_me_neu_potato', "Получил поручение нести мешок картошки")
    sdl_var_b_d5_me_neu_cesc    = sdl_Bool('alt_day5_me_neu_candle_escape', "Сбежал со свечки")
    sdl_var_b_d5_me_neu_cybr    = sdl_Bool('alt_day5_me_neu_clubs_cyber', "Прятал эротический клад")
    sdl_var_b_d5_me_neu_sl_voye = sdl_Bool('alt_day5_me_neu_sl_voyeur', "Подглядывал за Славей в озере")
    sdl_var_b_d5_me_neu_mt_diar = sdl_Bool('alt_day5_me_neu_mt_diary', "Прочитал вторую часть дневника Ольги")
    sdl_var_b_d5_me_neu_mt_hent = sdl_Bool('alt_day5_me_neu_mt_hentai', "Был хентай вечером 5 дня")
    sdl_var_b_d5_me_neu_us_stor = sdl_Bool('alt_day5_me_neu_us_stores', "Получил еду для рыжих")
    sdl_var_b_d5_me_neu_us_pota = sdl_Bool('alt_day5_me_neu_us_potato', "Поделился с Ульяной картошкой")
    ##############################
    sdl_var_i_mi_lpp = sdl_Int('lp_mi', "ЛП Мику", 25)
    sdl_var_i_dv_lpp = sdl_Int('lp_dv', "ЛП Алисы", 25)
    sdl_var_i_sl_lpp = sdl_Int('lp_sl', "ЛП Слави", 25)
    sdl_var_i_un_lpp = sdl_Int('lp_un', "ЛП Лены", 25)
    sdl_var_i_us_lpp = sdl_Int('lp_us', "ЛП Ульяны", 15)
    sdl_var_i_mi_7dl = sdl_Int('counter_mi_7dl', "Мику-7дл", 2)
    sdl_var_i_dv_7dl = sdl_Int('counter_dv_7dl', "Алиса-7дл", 4)
    sdl_var_i_sl_7dl = sdl_Int('counter_sl_7dl', "Славя-7дл", 5)
    sdl_var_i_sl_clt = sdl_Int('counter_sl_cl',  "Славя-Классик", 7)
    sdl_var_i_un_7dl = sdl_Int('counter_un_7dl', "Лена-7дл", 6)
    sdl_var_i_un_fzd = sdl_Int('counter_un_fz',  "Лена-ФЗ", 4)
    sdl_var_i_un_fzd_un = sdl_Int('counter_un_fz_un_route',     "ФЗ. Очки Лены", 9)
    sdl_var_i_un_fzd_ol = sdl_Int('counter_un_fz_old_road',     "ФЗ. Очки Дороги", 9)
    sdl_var_i_un_fzd_dv = sdl_Int('counter_un_fz_dv_fake_date', "ФЗ. Очки Алисы", 3)
    sdl_var_i_un_fzd_mt = sdl_Int('counter_un_fz_mt_transit',   "ФЗ. Очки Ольги", 3)
    sdl_var_i_un_fzd_dream_un = sdl_Int('counter_un_fz_dream_un',   "ФЗ. Сны с Леной", 3)
    sdl_var_i_un_fzd_dream_ol = sdl_Int('counter_un_fz_dream_road', "ФЗ. Сны с Дорогой", 3)
    sdl_var_i_me_neu_answ = sdl_Int('counter_me_neu_answers',  "Очки ответов", 3)
    sdl_var_i_mt_7dl = sdl_Int('counter_mt_7dl', "Ольга-7дл", 16)
    sdl_var_i_us_7dl = sdl_Int('counter_us_7dl', "Ульяна-7дл", 8)
    sdl_var_i_us_7dl_pxs = sdl_Int('counter_us_7dl_px',  "Ульяна-Огоньки", 3)
    sdl_var_i_karma  = sdl_Int('karma', "Карма", 300)
    sdl_var_i_sl_sp  = sdl_Int('alt_sp', "Воля", 14)
    sdl_var_i_mi_spt = sdl_Int('alt_spt', "Princess-поинты", 10)
    sdl_var_i_mi_hpt = sdl_Int('alt_hpt', "Human-поинты", 10)
    ##############################
    sdl_var_e_d1_cofr    = sdl_Enum(
                                'alt_day1_cofront_sl_dv', "Конфликт Слави и Алисы",
                                (
                                    (1, "Закрыл собой Славю"),
                                    (2, "Отговорил Алису")
                                )
                              )
    sdl_var_e_d1_un      = sdl_Enum(
                                'alt_day1_un', "Лена в 1 день",
                                (
                                    (0, "Не подходил к Лене"),
                                    (1, "Поговорил с Леной"),
                                    (2, "Попросил Лену задержаться"),
                                    (3, "Попросил Лену рассказать о лагере"),
                                    (4, "Позвал Лену прогуляться по лагерю")
                                )
                              )
    sdl_var_e_d1_sl_key  = sdl_Enum(
                                'alt_day1_sl_keys_took', "Ключи Слави",
                                (
                                    (0, "Ключей нет"),
                                    (1, "Оставил ключи себе"),
                                    (2, "Отдал ключи вожатой"),
                                    (3, "Оставил ключи себе, у Слави новая связка")
                                )
                              )
    # ====================
    sdl_var_e_d2_brf     = sdl_Enum('alt_day2_bf', "Завтрак во 2 день",
                                (
                                    ('me', "Один"),
                                    ('sl', "Со Славей"),
                                    ('un', "С Леной"),
                                    ('dv_us', "С рыжими")
                                )
                              )
    sdl_var_e_d2_conv    = sdl_Enum('alt_day2_convoy', "Обход лагеря",
                                (
                                    ('me', "Один"),
                                    ('dv', "С Алисой"),
                                    ('dv_prep', "Алиса — договаривался"),
                                    ('dv_rej', "Алиса — пришёл поздно"),
                                    ('sl', "Со Славей"),
                                    ('sl_prep', "Славя — договаривался"),
                                    ('un', "С Леной")
                                )
                              )
    sdl_var_e_d2_mi_kumu = sdl_Enum(
                                'alt_day2_mi_kumuhimo', "Кумухимо Мику",
                                (
                                    (0, "Не находил"),
                                    (1, "Нашёл"),
                                    (2, "Вернул Мику")
                                )
                              )
    sdl_var_e_d2_walk    = sdl_Enum(
                                'alt_day2_walk', "Ходил за картами",
                                (
                                    (0, "Один"),
                                    (1, "Один. Пометил карты"),
                                    (2, "Со Славей")
                                )
                              )
    sdl_var_e_d2_dv_ulti = sdl_Enum(
                                'alt_day2_dv_ultim', "Ультиматум Алисы",
                                (
                                    (0, "Не спорил"),
                                    (1, "Спорил"),
                                    (2, "Лапал Алису")
                                )
                              )
    sdl_var_e_d2_us_cake = sdl_Enum(
                                'alt_day2_us_cake', "Торт Ульяны",
                                (
                                    (0, "Не бежал за Ульяной"),
                                    (1, "Побежал за Ульяной"),
                                    (2, "Догнал Ульяну")
                                )
                              )
    sdl_var_e_d2_date    = sdl_Enum('alt_day2_date', "Свидание на 2 день",
                                (
                                    ('', "Ни с кем"),
                                    ('mi', "Мику"),
                                    ('dv', "Алиса"),
                                    ('sl', "Славя"),
                                    ('un', "Лена"),
                                    ('un_fz', "Лена. Френдзона"),
                                    ('mt', "Ольга"),
                                    ('us', "Ульяна")
                                )
                              )
    sdl_var_e_d2_mi_date = sdl_Enum(
                                'alt_day2_mi_date', "Вечер с Мику на пляже",
                                (
                                    (0, "Не виделся с Мику"),
                                    (1, "Поговорил с Мику"),
                                    (2, "Отшил Мику"),
                                    (3, "Выслушал истерику Мику")
                                )
                              )
    # ====================
    sdl_var_e_d3_date    = sdl_Enum('alt_day3_date', "Свидание на 3 день",
                                (
                                    ('', "Ни с кем"),
                                    ('mi', "Мику"),
                                    ('dv', "Алиса"),
                                    ('sl', "Славя"),
                                    ('un', "Лена")
                                )
                              )
    sdl_var_e_d3_us_bugs = sdl_Enum('alt_day3_us_bugs', "Жуки Ульяны",
                                (
                                    (0, "Не собирал жуков"),
                                    (1, "Помог набрать жуков"),
                                    (2, "Пригрозил рассказать вожатой")
                                )
                              )
    sdl_var_e_d3_dv_guit = sdl_Enum('alt_day3_dv_guitar', "Мини-концерт Алисы",
                                (
                                    (0, "Не встречал Алису днём на эстраде"),
                                    (1, "Встретил Алису днём на эстраде"),
                                    (2, "Обещал прийти вечером"),
                                    (3, "Пришёл вечером")
                                )
                              )
    sdl_var_e_d3_un_medh = sdl_Enum('alt_day3_un_med_help', "Помощь в медпункте",
                                (
                                    (0, "Виола не просила о помощи"),
                                    (1, "Согласился помочь в медпункте"),
                                    (2, "Отказался помогать в медпункте")
                                )
                              )
    sdl_var_e_d3_dj      = sdl_Enum('alt_day3_dj', "Выбор диджея",
                                (
                                    ('', "Не назначен"),
                                    ('mi', "Мику"),
                                    ('dv', "Алиса")
                                )
                              )
    sdl_var_e_d3_me_tec1 = sdl_Enum('alt_day3_technoquest1', "Техноквест 1",
                                (
                                    (0, "Не помогал кибернетикам"),
                                    (1, "Помог убраться в кладовке"),
                                    (2, "Раздобыл лестницу")
                                )
                              )
    sdl_var_e_d3_un_fz_work = sdl_Enum('alt_day3_un_fz_work', "Подготовка к дискотеке",
                                (
                                    ('dv', "С Алисой"),
                                    ('sl', "Со Славей"),
                                    ('un', "С Леной")
                                )
                              )
    sdl_var_e_d3_me_dan1 = sdl_Enum('alt_day3_dancing1', "Первый танец в 3 день",
                                (
                                    ('me_1', "Ни с кем не танцевал"),
                                    ('mi_1', "С Мику"),
                                    ('dv_1', "С Алисой-ДЖ"),
                                    ('sl_1', "Со Славей"),
                                    ('un_1', "С Леной"),
                                    ('un_fz', "С Леной-ФЗ")
                                )
                              )
    sdl_var_e_d3_me_dan2 = sdl_Enum('alt_day3_dancing2', "Второй танец в 3 день",
                                (
                                    ('',      "Не было второго танца"),
                                    ('me_2',  "Ни с кем не танцевал"),
                                    ('mi_2',  "С Мику"),
                                    ('mi_12', "С Мику, повторно"),
                                    ('dv_2',  "С Алисой-ДЖ"),
                                    ('dv_12', "С Алисой-ДЖ, повторно"),
                                    ('dv_0',  "С Алисой, не вышло"),
                                    ('sl_2',  "Со Славей"),
                                    ('sl_12', "Со Славей, повторно"),
                                    ('un_2',  "С Леной"),
                                    ('un_12', "С Леной, повторно"),
                                    ('un_0',  "С Леной, не вышло")
                                )
                              )
    sdl_var_e_d3_me_stri = sdl_Enum('alt_day3_un_strip_pool_sp', "Карты на раздевание (Семён)",
                                (
                                    (5, "Не играл / Не раздевался"),
                                    (4, "Проиграл 1 раз (рубашка)"),
                                    (3, "Проиграл 2 раза (обувь)"),
                                    (2, "Проиграл 3 раза (шорты)"),
                                    (1, "Проиграл 4 раза (трусы)"),
                                    (0, "Полностью разделся и проиграл")
                                )
                              )
    sdl_var_e_d3_un_stri = sdl_Enum('alt_day3_un_strip_pool_un', "Карты на раздевание (Лена)",
                                (
                                    (5, "Не играл / Не раздевал Лену"),
                                    (4, "Выиграл 1 раз (туфельки)"),
                                    (3, "Выиграл 2 раза (платье)"),
                                    (2, "Выиграл 3 раза (лифчик)"),
                                    (1, "Выиграл 4 раза (трусики)"),
                                    (0, "Полностью раздел и обыграл Лену")
                                )
                              )
    # ====================
    sdl_var_e_d3_mi_7dl_dono = sdl_Enum('alt_day3_mi_7dl_donor', "Поездка в город",
                                (
                                    (0, "Поехал в город без Мику"),
                                    (1, "Поехал в город вместе с Мику"),
                                    (2, "Мику решила стать донором")
                                )
                              )
    # ====================
    sdl_var_e_d5_mi_dj_voye = sdl_Enum('alt_day5_mi_dj_voyeur', "Поиски Мику в душевых",
                                (
                                    (2, "Выбрал кабинку Алисы"),
                                    (3, "Выбрал кабинку Слави"),
                                    (4, "Выбрал кабинку Мику")
                                )
                              )
    sdl_var_e_d5_mi_dj_apol = sdl_Enum('alt_day5_mi_dj_apology', "Извинения перед Мику",
                                (
                                    (0, "Не нашёл Мику / Не угадал с песней"),
                                    (1, "Выбрал любимую песню Мику"),
                                    (2, "Порезал себе руку"),
                                    (3, "Попытался извиниться перед Мику")
                                )
                              )
    sdl_var_e_d6_mi_dj_feed = sdl_Enum('alt_day6_mi_dj_feed', "Ужин в 6 день",
                                (
                                    ('', "Ужинал нормально"),
                                    ('sl', "Накормила Славя"),
                                    ('un', "Накормила Лена")
                                )
                              )
    sdl_var_e_d6_mi_dj_cata = sdl_Enum('alt_day6_mi_dj_catapult', "Катапульта",
                                (
                                    (0, "Не было катапульты"),
                                    (1, "Выбрал остаться"),
                                    (2, "Попытался свалить")
                                )
                              )
    # ====================
    sdl_var_e_d4_dv_7dl_medi = sdl_Enum('alt_day4_dv_7dl_medication', "Лекарства для Алисы",
                                (
                                    (0, "Не искал лекарств"),
                                    (1, "Достал таблетки у Ольги"),
                                    (2, "Залез в медпункт")
                                )
                              )
    sdl_var_e_d4_dv_7dl_vodk = sdl_Enum('alt_day4_dv_7dl_vodka', "Водка",
                                (
                                    (0, "Не лазили в медпункт"),
                                    (1, "Забрали водку себе"),
                                    (2, "Выпили водку")
                                )
                              )
    sdl_var_e_d6_dv_7dl_rout = sdl_Enum('alt_day6_dv_7dl_route', "Выбор 6 дня",
                                (
                                    ('sl', "Подождал Алису (ивент Слави)"),
                                    ('un', "Сходил переодеться (ивент Лены)")
                                )
                              )
    sdl_var_e_d6_dv_7dl_danc = sdl_Enum('alt_day6_dv_7dl_dance', "Танец в 6 день",
                                (
                                    ('dv', "С Алисой"),
                                    ('sl', "Со Славей"),
                                    ('un', "С Леной"),
                                    ('mt', "С Ольгой")
                                )
                              )
    sdl_var_e_d6_dv_7dl_hent = sdl_Enum('alt_day6_dv_7dl_hentai', "Хентай-флаги",
                                (
                                    (  0, "Нет ключей; нет алкоголя; не здоровался с Санычем"),
                                    (  1, "Нет ключей; нет алкоголя; здоровался с Санычем"),
                                    ( 10, "Нет ключей; есть алкоголь; не здоровался с Санычем"),
                                    ( 11, "Нет ключей; есть алкоголь; здоровался с Санычем"),
                                    (100, "Есть ключи; нет алкоголя; не здоровался с Санычем"),
                                    (101, "Есть ключи; нет алкоголя; здоровался с Санычем"),
                                    (110, "Есть ключи; есть алкоголь; не здоровался с Санычем"),
                                    (111, "Есть ключи; есть алкоголь; здоровался с Санычем")
                                )
                              )
    sdl_var_e_d7_dv_7dl_chec = sdl_Enum('alt_day7_dv_7dl_check', "С кем провёл последний день",
                                (
                                    ('dv_1', "С Алисой"),
                                    ('dv_2', "С Алисой. Подарил плеер с записью"),
                                    ('dv_0', "С Алисой. Разошлись"),
                                    ('sl', "Со Славей"),
                                    ('un', "С Леной"),
                                    ('mt', "С Ольгой")
                                )
                              )
    # ====================
    sdl_var_e_d5_dv_dj_mapp = sdl_Enum('alt_day5_dv_dj_map', "Куда пошли во время тихого часа",
                                (
                                    ('dv', "К Алисе"),
                                    ('us', "К Ульяне"),
                                    ('un', "К Лене"),
                                    ('mi', "К Мику"),
                                    ('cyber', "К кибернетикам")
                                )
                              )
    sdl_var_e_d5_dv_dj_sljr = sdl_Enum('alt_day5_dv_dj_sl_jeer', "Участвовали в конфликте со Славей",
                                (
                                    (0, "Не участвовали"),
                                    (1, "Запугали"),
                                    (2, "Предупредили")
                                )
                              )
    sdl_var_e_d6_dv_dj_ends = sdl_Enum('alt_dv_dj_ends', "К какой концовке идём",
                                (
                                    ('true', "Истинная"),
                                    ('good', "Хорошая"),
                                    ('rej', "Реджект"),
                                    ('neu', "Нейтральная"),
                                    ('bad', "Плохая")
                                )
                              )
    # ====================
    sdl_var_e_d4_sl_cl_solo = sdl_Enum('alt_day4_sl_cl_lf_solo', "Поиски Шурика",
                                (
                                    (0, "Отправился с Леной и Славей"),
                                    (1, "Отправился один"),
                                    (2, "Отправился один, но неудачно"),
                                    (3, "Отправился один, но наткнулся на девочек")
                                )
                              )
    sdl_var_e_d6_sl_cl_arc  = sdl_Enum('alt_day6_sl_cl_arc', "Сюжетная арка 6 дня",
                                (
                                    ('sh', "Арка Шурика"),
                                    ('pi', "Арка Пирата")
                                )
                              )
    # ====================
    sdl_var_e_d4_un_7dl_calm = sdl_Enum('alt_day4_un_7dl_calm', "Кто пришёл на стоянку поговорить",
                                (
                                    ('', "Не сбегал на стоянку"),
                                    ('un', "Лена"),
                                    ('dv', "Алиса")
                                )
                              )
    sdl_var_e_d5_un_7dl_wash = sdl_Enum('alt_day5_un_7dl_washing', "Мытьё после уборки костровой",
                                (
                                    ('', "Не убирал костровую"),
                                    ('me', "Мылся сам"),
                                    ('sl_un', "Мыли Славя с Леной")
                                )
                              )
    # ====================
    sdl_var_e_d4_un_fz_morn = sdl_Enum('alt_day4_un_fz_morning_event', "Утренний ивент 4 дня",
                                (
                                    ('un', "Помогал в стенгазете"),
                                    ('mt', "Помогал Ольге"),
                                    ('dv', "Сбежал с Алисой")
                                )
                              )
    sdl_var_e_d4_un_fz_even = sdl_Enum('alt_day4_un_fz_un_evening', "Вечером после пьянки",
                                (
                                    ('sleep', "Уложил Лену спать"),
                                    ('walk', "Решил проветриться")
                                )
                              )
    sdl_var_e_d6_un_fz_map1 = sdl_Enum('alt_day6_un_fz_map1_quest', "Куда пошёл утром 6 дня",
                                (
                                    ('musclub', "Музклуб"),
                                    ('boatstation', "Причал"),
                                    ('playground', "Спортплозадка"),
                                    ('dv_house', "Домик Алисы")
                                )
                              )
    sdl_var_e_d6_un_fz_map2 = sdl_Enum('alt_day6_un_fz_map2_quest', "Куда ещё пошёл утром 6 дня",
                                (
                                    ('beach', "Пляж"),
                                    ('dinner_hall', "Столовая"),
                                    ('busstation', "Стоянка")
                                )
                              )
    # ====================
    sdl_var_e_d4_me_neu_date = sdl_Enum('alt_day4_me_neu_date', "Свидание утром 4 дня",
                                (
                                    ('', "Ни с кем"),
                                    ('mi', "Мику"),
                                    ('dv', "Алиса"),
                                    ('sl', "Славя"),
                                    ('un', "Лена"),
                                    ('mt', "Ольга"),
                                    ('us', "Ульяна")
                                )
                              )
    sdl_var_e_d4_me_neu_tran = sdl_Enum('alt_day4_me_neu_transit', "Транзит Одиночки",
                                (
                                    ('', "Не был на руте Одиночки"),
                                    ('un_7dl', "Лена-7ДЛ"),
                                    ('sl_cl', "Славя-Классик")
                                )
                              )
    sdl_var_e_d5_me_neu_mapi = sdl_Enum('alt_day5_me_neu_map_ivent', "Прогулка вечером 5 дня",
                                (
                                    ('', "Не был"),
                                    ('dv', "Домик Алисы"),
                                    ('medic', "Медпункт"),
                                    ('boat', "Пирс"),
                                    ('beach', "Пляж")
                                )
                              )
    sdl_var_e_d5_me_neu_cand = sdl_Enum('alt_day5_me_neu_candle', "Свечка",
                                (
                                    (1, "Пошёл домой спать"),
                                    (2, "Отправлен на свечку"),
                                    (3, "Назначен ответственным за игротеку"),
                                    (4, "Получил поручение присматривать за гвардейцами")
                                )
                              )
    sdl_var_e_d5_me_neu_mt_voye = sdl_Enum('alt_day5_me_neu_mt_voyeur', "Пляж с Ольгой",
                                (
                                    (0, "Не был на пляже с Ольгой"),
                                    (1, "Был с Ольгой на пляже"),
                                    (2, "Подглядывал за переодевающейся Ольгой")
                                )
                              )
    # ====================
    sdl_var_e_d6_us_7dl_mi_frie = sdl_Enum('alt_day6_us_7dl_mi_friends', "Ветка Мику",
                                (
                                    (0, "Не завтракал с Мику"),
                                    (1, "Завтракал с Мику"),
                                    (2, "Согласился помочь Мику"),
                                    (3, "Сблизился с Мику")
                                )
                              )
    sdl_var_e_d6_us_7dl_sl_frie = sdl_Enum('alt_day6_us_7dl_sl_friends', "Ветка Слави",
                                (
                                    (0, "Не завтракал со Славей"),
                                    (1, "Завтракал со Славей"),
                                    (2, "Согласился помочь на складе")
                                )
                              )
    sdl_var_e_d6_us_7dl_un_frie = sdl_Enum('alt_day6_us_7dl_un_friends', "Ветка Лены",
                                (
                                    (0, "Не договаривался с Леной о танце"),
                                    (2, "Договорился с Леной о танце"),
                                    (3, "Сблизился с Леной")
                                )
                              )
    ##############################
    sdl_var_l_d1_sl = sdl_List(
                                'list_slavya_7dl', "Экскурсия со Славей",
                                [
                                  ('clubs'      , "Клубы"),
                                  ('aidstation' , "Медпункт"),
                                  ('sports'     , "Спортплощадка"),
                                  ('estrade'    , "Эстрада")
                                ],
                                2
                              )
    sdl_var_l_d2_voya = sdl_List(
                                'list_voyage_7dl', "Обход",
                                [
                                  ('library'    , "Библиотека"),
                                  ('cyber'  , "Клубы"),
                                  ('medic'      , "Медпункт"),
                                  ('music_club' , "Музклуб"),
                                  ('sport_area' , "Спортплощадка"),
                                  ('cleaning_dv', "Уборка площади с Алисой"),
                                  ('cleaning_sl', "Уборка площади со Славей"),
                                  ('cleaning_un', "Уборка площади с Леной")
                                ],
                                4
                              )
    sdl_var_l_d2_jclu = sdl_List(
                                'list_joined_clubs_7dl', "Записывался в кружки",
                                [
                                  ('badmin', "Бадминтон"),
                                  ('volley', "Волейбол"),
                                  ('cyber' , "Кибернетика"),
                                  ('music' , "Музкружок"),
                                  ('nwsppr', "Стенгазета"),
                                  ('soccer', "Футбол")
                                ],
                                4
                              )
    sdl_var_l_d2_club = sdl_List(
                                'list_clubs_7dl', "Записан в кружки",
                                [
                                  ('badmin', "Бадминтон"),
                                  ('volley', "Волейбол"),
                                  ('cyber' , "Кибернетика"),
                                  ('music' , "Музкружок"),
                                  ('nwsppr', "Стенгазета"),
                                  ('soccer', "Футбол")
                                ],
                                2
                              )
    # ====================
    sdl_var_l_d5_mi_dj_sear = sdl_List(
                                'list_mi_search_7dl', "Поиски Мику",
                                [
                                  ('musclub' , "Музклуб"),
                                  ('entrance', "Стоянка"),
                                  ('estrade' , "Эстрада"),
                                  ('home'    , "Дом Мику"),
                                  ('clubs'   , "Радиорубка")
                                ],
                                5
                              )

    # Функции переключения интерфейса
    def day_interface_on():
        persistent.sprite_time = "day"
        day_time()
        replay_screens_on()
    def sunset_interface_on():
        persistent.sprite_time = "sunset"
        sunset_time()
        replay_screens_on()
    def night_interface_on():
        persistent.sprite_time = "night"
        night_time()
        replay_screens_on()
    def prolog_interface_on():
        persistent.sprite_time = "prolog"
        prolog_time()
        replay_screens_on()

screen sdl_replay_vars(vars): # Экран переменных
    add "sdl_repl_screen_var"

    text "Настройка переменных":
        style "sdl_repl_font_var_big"
        bold True
        underline True
        xalign 0.5

    # Bool
    text "Флаги":
        style "sdl_repl_font_var_medium"
        bold True
        xalign 0.105
        yalign 0.05
    $ gen_vars = (var for var in vars if var.get_type() == 0)
    side "c r":
        area (0, 100, 480, 825)

        viewport id "vp_bool":
            mousewheel True
            draggable True

            vbox:
                spacing 25
                xsize 415

                for var in gen_vars:
                    hbox:
                        spacing 25
                        null width 10
                        imagebutton:
                            if var.get_cur_value():
                                auto "sdl_repl_checkbox_checked_%s"
                            else:
                                auto "sdl_repl_checkbox_unchecked_%s"
                            action [Function(var.toggle_value)]
                        text var.get_text() style "sdl_repl_font_var_small" yalign 0.5
                        null width 10

        vbar:
            value YScrollValue("vp_bool")
            top_bar    Frame("sdl_repl_vbar_full", 10, 10)
            bottom_bar Frame("sdl_repl_vbar_null", 10, 10)
            thumb "sdl_repl_vbar_thumb_idle"
            hover_thumb "sdl_repl_vbar_thumb_hover"
            unscrollable "hide"

    # Int
    text "Поинты":
        style "sdl_repl_font_var_medium"
        bold True
        xalign 0.365
        yalign 0.05
    $ gen_vars = (var for var in vars if var.get_type() == 1)
    side "c r":
        area (480, 100, 480, 825)

        viewport id "vp_int":
            mousewheel True
            draggable True

            vbox:
                spacing 25
                xsize 415

                for var in gen_vars:
                    if (var == sdl_var_i_me_neu_answ) and (not persistent.alt_binder):
                        pass
                    else:
                        hbox:
                            spacing 25
                            xsize 415

                            null width 10
                            vbox:
                                spacing 25

                                hbox:
                                    spacing 25

                                    if var.get_cur_value() > 0:
                                        imagebutton:
                                            auto "sdl_repl_arrow2_left_%s"
                                            action [Function(var.cur_val_dec)]
                                    else:
                                        null width 50

                                    frame:
                                        xysize (50, 50)
                                        background Frame("sdl_repl_frame_var_int", 0, 0)

                                        add Text(str(var.get_cur_value()), style = "sdl_repl_font_var_num") maxsize (40, 40) align (0.5, 0.5)

                                    if var.get_cur_value() < var.get_range():
                                        imagebutton:
                                            auto "sdl_repl_arrow2_right_%s"
                                            action [Function(var.cur_val_inc)]
                                    else:
                                        null width 50

                                    text var.get_text() style "sdl_repl_font_var_small" yalign 0.5

                                bar:
                                    value FieldValue(var, "cur_value", var.get_range())
                                    left_bar  Frame("sdl_repl_bar_full", 36, 36)
                                    right_bar Frame("sdl_repl_bar_null", 36, 36)
                                    thumb       "sdl_repl_bar_thumb_idle"
                                    hover_thumb "sdl_repl_bar_thumb_hover"
                                    ymaximum 36
                            null width 10

        vbar:
            value YScrollValue("vp_int")
            top_bar    Frame("sdl_repl_vbar_full", 10, 10)
            bottom_bar Frame("sdl_repl_vbar_null", 10, 10)
            thumb "sdl_repl_vbar_thumb_idle"
            hover_thumb "sdl_repl_vbar_thumb_hover"
            unscrollable "hide"

    # Enum
    text "Перечисления":
        style "sdl_repl_font_var_medium"
        bold True
        xalign 0.635
        yalign 0.05
    $ gen_vars = (var for var in vars if var.get_type() == 2)
    side "c r":
        area (960, 100, 480, 825)

        viewport id "vp_enum":
            mousewheel True
            draggable True

            vbox:
                spacing 25
                xsize 415

                for var in gen_vars:
                    hbox:
                        spacing 25

                        null width 10
                        vbox:
                            spacing 25
                            xsize 395

                            text var.get_text() style "sdl_repl_font_var_small" xalign 0.5
                            hbox:
                                spacing 25

                                if var.get_cur_val_idx() > 0:
                                    imagebutton:
                                        auto "sdl_repl_arrow2_left_%s"
                                        action [Function(var.cur_val_idx_dec)]
                                else:
                                    null width 50

                                frame:
                                    xysize (50, 50)
                                    background Frame("sdl_repl_frame_var_int", 0, 0)

                                    add Text(str(var.get_cur_value()), style = "sdl_repl_font_var_num") maxsize (40, 40) align (0.5, 0.5)

                                if var.get_cur_val_idx() < (var.get_values_amount() - 1):
                                    imagebutton:
                                        auto "sdl_repl_arrow2_right_%s"
                                        action [Function(var.cur_val_idx_inc)]
                                else:
                                    null width 50
                                text var.get_cur_descr() style "sdl_repl_font_var_small" yalign 0.5
                        null width 10

        vbar:
            value YScrollValue("vp_enum")
            top_bar    Frame("sdl_repl_vbar_full", 10, 10)
            bottom_bar Frame("sdl_repl_vbar_null", 10, 10)
            thumb "sdl_repl_vbar_thumb_idle"
            hover_thumb "sdl_repl_vbar_thumb_hover"
            unscrollable "hide"

    # List
    text "Списки":
        style "sdl_repl_font_var_medium"
        bold True
        xalign 0.895
        yalign 0.05
    $ gen_vars = (var for var in vars if var.get_type() == 3)
    side "c r":
        area (1440, 100, 480, 825)

        viewport id "vp_list":
            mousewheel True
            draggable True

            vbox:
                spacing 25
                xsize 415

                for var in gen_vars:
                    hbox:
                        spacing 25

                        null width 10
                        vbox:
                            spacing 15
                            xsize 395

                            text var.get_text() style "sdl_repl_font_var_small" xalign 0.5
                            for v in var.get_values():
                                hbox:
                                    spacing 25

                                    null width 15
                                    if var.is_full():
                                        if v[0] in var.get_cur_value():
                                            imagebutton:
                                                auto "sdl_repl_radiobutton_checked_%s"
                                                action [Function(var.del_value, v[0])]
                                        else:
                                            add "sdl_repl_radiobutton_unchecked_idle"
                                    else:
                                        imagebutton:
                                            if v[0] in var.get_cur_value():
                                                auto "sdl_repl_radiobutton_checked_%s"
                                                action [Function(var.del_value, v[0])]
                                            else:
                                                auto "sdl_repl_radiobutton_unchecked_%s"
                                                action [Function(var.add_value, v[0])]
                                    text v[1] style "sdl_repl_font_var_small" yalign 0.5
                        null width 10

        vbar:
            value YScrollValue("vp_list")
            top_bar    Frame("sdl_repl_vbar_full", 10, 10)
            bottom_bar Frame("sdl_repl_vbar_null", 10, 10)
            thumb "sdl_repl_vbar_thumb_idle"
            hover_thumb "sdl_repl_vbar_thumb_hover"
            unscrollable "hide"

    imagebutton xalign 0.5 yalign 0.95:
        auto "sdl_repl_button_ok_%s"
        action [Hide("sdl_replay_vars", transition=Dissolve(0.5)), Return()]

label sdl_replay(): # Лейбл для запуска реплеев
    if cur_replay != None:
        # XXX: Replay не умеет сам останавливать музыку, запущенную в MusicRoom
        stop music fadeout 3

        # Инициализируем все необходимые переменные…
        ## Инициализируем значения переменных
        call alt_vars
        if cur_replay.get_vars() != None:
            call screen sdl_replay_vars(cur_replay.get_vars()) with dissolve
            $ cur_replay.apply_vars()
        ## Устанавливаем значения переменных из scope (их после alt_vars сбросило)
        $ cur_replay.apply_scope()
        ## Устанавливаем переменную персонажа (иначе она сбросится в alt_vars)
        if cur_char != None:
            if cur_char == "loki":
                $ loki = True
            elif cur_char == "herc":
                $ herc = True
            elif cur_char == "dr":
                $ dr = True
        ## Инициализируем имена
        $ make_names_known_7dl()
        $ cur_replay.apply_meets()
        ## Задаём спрайт-таймы и прочее
        $ cur_replay.get_func_in()()

        ## Включаем музыку
        if cur_replay.get_music() != None:
            play music cur_replay.get_music() fadein 3
        if cur_replay.get_ambience() != None:
            play ambience cur_replay.get_ambience() fadein 3
        if cur_replay.get_sound_loop() != None:
            play sound_loop cur_replay.get_sound_loop() fadein 3

        # Let's do this!
        call expression cur_replay.get_label()

        if cur_replay.get_func_out() != None:
            $ cur_replay.get_func_out()()

    return

### === ###
