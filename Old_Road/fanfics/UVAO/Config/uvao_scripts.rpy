init -999 python:
    path_uvao = default_7dl_path + "Old_Road/fanfics/UVAO/"

    def get_image_uvao_7dl(file):
        return path_uvao+"Pics/%s" % (file)

init -998 python:
    def get_sfx_uvao_7dl(file):
        return path_uvao+"Sound/sfx/%s" % (file)
    def get_music_uvao_7dl(file):
        return path_uvao+"Sound/music/%s" % (file)

init -5 python:
    # Фабрика спрайтов (Provided by UVAO)
    # Константы:
    # тонировка:
    tint_night = im.matrix.tint(0.63, 0.78, 0.82)
    tint_sunset = im.matrix.tint(0.94, 0.82, 1.0)

    # Простая функция, строит спрайт из переданных путей
    def ComposeSprite(*argv):
        #строим аргументы для im.Composite
        subargs = list()
        for arg in argv:
           subargs.append( (0,0) )
           subargs.append( arg )
        sprite = im.Composite(None, *subargs)
        return ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(sprite, tint_sunset), "persistent.sprite_time=='night'", im.MatrixColor(sprite, tint_night), True, sprite)
    # /ComposeSprite(*argv)

    # Функция, собирающая спрайты из запчастей
    # types - набор калибров спрайтов. Любой набор из ('far', 'close', 'normal', 'veryfar'). По пути, где лежат спрайты, должны быть соотвествующие директории, иначе не найдет
    # argv - файлы-запчасти. передаются в формате ('path', 'file') - например ('images/1080/sprites/','dv/dv_1_coat.png'), или просто 'file'
    # на выходе - dict спрайтов, по одному для каждого из types
    def ComposeSpriteSet(distance, *argv):
        if isinstance(distance, str): #если types содержит только один параметр.
            distances = (distance,) # 1-tuple. Иначе for будет перебирать символы в строке.
        else:
            distances = distance
        ret = dict()
        for dst in distances:
            #строим аргументы для ComposeSprite
            subargs = list()
            for arg in argv:
                if isinstance(arg, str): #просто file
                    subarg = (path_uvao+'Pics/sprites/', arg)
                else: # (path, file)
                    subarg = arg;
                subargs.append( subarg[0] + '/' + dst +'/' + subarg[1] ) # 'images/1080/sprites/normal/dv/dv_1_coat.png'
            ret[dst] = ComposeSprite(*subargs)
        return ret
    # /ComposeSpriteSet(type, *argv)

screen alt_uvao_info:
    modal True
    add get_image_uvao_7dl("info.png") xcenter 0.5 ycenter 0.5
    text "Вы запускаете недописанное (обрывается в конце 5-го дня) фанатское дополнение к моду. Сейчас запустится 7ДЛ с самого начала, при этом добавятся новые выборы и текст в первых 3 днях. Чтобы выйти на собственно кошкорут, нужно сделать следующее:\n\n- В 1 день после ужина бежать на площадь за Ульяной;\n- Вечером 1 дня при разговоре с Леной спросить её о Генде (выбор \"Сменить тему\");\n- Вечером 3 дня ни с кем не танцевать, кибернетикам не помогать, от Ольги сбежать;\n- Иметь меньше 6 ЛП с каждой из девушек.":
        text_align 0.5
        xcenter 957
        ycenter 480
        xmaximum 1600
        color "#64483c"
        font header_font
        size 40
    textbutton _("OK"):
        text_size 60
        style "log_button"
        text_style "settings_link"
        xcenter 0.5
        ycenter 800
        action [Hide("alt_uvao_info", transition=Dissolve(0.5)), Return()]
