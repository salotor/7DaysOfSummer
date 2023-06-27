# ================================================================================================
#                                            начало турнира
# ================================================================================================
label alt_day2_cards_tournament:
    play sound sfx_close_door_1
    scene bg int_dining_hall_day with fade
    play music music_list["i_want_to_play"] fadein 1
    play ambience ambience_medium_crowd_indoors_1 fadein 1
    "А внутри уже всё было готово!"
    "Столы были сдвинуты плей-офф таблицей, победитель пересаживался за соседний стол, проигравший просто вставал с места."
    "Настроение у всех было приподнятое и праздничное."
    "Я пригляделся, смотря по соперникам и прикидывая шансы."

    show sh normal pioneer far at right
    show us laugh2 pioneer far at left
    with dissolve
    "Шурик, как и я, не совсем понимающий, что он здесь забыл, сидел рядом с Ульяной."
    show sh serious pioneer far
    show us laugh pioneer far
    with dspr
    "Егоза нетерпеливо раскачивалась на стуле и пыталась вытянуть из Шурика какие-то сведения о предстоящей игре, на что тот только недовольно хмурился и делал вид, что он вообще не с ней."
    hide sh
    hide us
    with dissolve

    show sl normal pioneer far at right
    show mz normal glasses pioneer far at left
    with dissolve
    if ('library' in list_voyage_7dl):
        "Следующий стол оккупировала жужелица из библиотеки, ей противостояла Славя."
    else:
        "Следующий стол занимала та самая Женя, против неё играла Славя."
    "Я, поймав её взгляд, ободряюще улыбнулся:"
    me "Удачи."
    show sl smile pioneer far with dspr
    sl "Спасибо."
    "Она улыбнулась в ответ."
    hide sl
    hide mz
    with dissolve

    show dv smile pioneer2 far at left
    show mi normal pioneer far at right
    with dissolve
    "Алисе в жертвы досталась Мику, и я на секунду пожалел несчастную японскую девочку."
    "То, каким азартом горели глаза Алисы, говорило лишь об одном — хищница настроена на победу и ни на что иное!"
    if alt_day2_dv_ultim == 1:
        show dv laugh pioneer2 far with dspr
        pause(0.3)
        show dv smile pioneer2 far with dspr
        "Поймав мой взгляд, Алиса подмигнула, напоминая о пари, и я ответно кивнул."
    elif alt_day2_dv_ultim == 2:
        show dv sad pioneer2 far with dspr
        "Встретившись со мной глазами, она почему-то вздрогнула и{nw}"
        hide dv with dissolve
        extend " мгновенно отвернулась."
        "Кажется, сценка у дверей произвела на неё неизгладимое впечатление!"
    else:
        "Меня она не удостоила даже взглядом."
    hide dv
    hide mi
    with dissolve

    show un normal pioneer far with dissolve
    "Пустовало одно место — напротив Лены. Кажется, мне предстоит играть с ней."
    "Всё остальное пространство было занято болельщиками и зрителями."
    show un smile pioneer with dspr
    me "Привет ещё раз."
    "Я опустился на стул напротив."
    me "Кажется, нам предстоит выступить друг против друга."
    show un shy pioneer with dissolve
    un "Да…"
    "От внимания зрителей она явно чувствовала себя не в своей тарелке."
    me "Значит, удачи нам обоим."
    "На секундочку вдруг захотелось сдать партию, чтобы немного приободрить эту грустную девочку. Надо же иногда делать и добрые дела, не так ли?"
    hide un with dissolve

    $ persistent.sprite_time = "day"
    $ day_time()
    with dissolve
# ------------------------------------------------------------- ADD загоняем БГ зала на нижний слой
    python:
        renpy.scene('underlay')
        renpy.show('bg int_dining_hall_day',layer='underlay')
        renpy.scene('master')
        renpy.transition(dissolve)
# ------------------------------------------------------------- /ADD
    show el smile pioneer at right with dissolve
    "Закончив считать карты, Электроник повернулся в нашу сторону и с нездоровым даже для него оживлением обратился к нам:"
    el "Карты у нас есть, все на местах. Начинаем турнир!"
    show el normal pioneer with dspr
    me "Погоди, торопыга."
    "Проворчал я."
    me "Как насчёт правил? Или мы в техасский холдем поиграть присели?"
    show el surprise pioneer with dspr
    el "Ой, правила. Точно."
    show el normal pioneer with dspr
    "Электроник взял маркер, которым чертил схемы игры, и погрузился в размышления, машинально покусывая колпачок."
    show el serious pioneer with dspr
    el "Так вот."
    "Он показал на схему."
# ------------------------------------------------------------- ADD Показываем схему турнира на фоне зала
    python:
        renpy.show('alt_tournament_bg',layer='underlay')
        renpy.transition(dissolve)
# ------------------------------------------------------------- /ADD
    el "Это схема турнира, и…"
    show dv angry pioneer2 at left
    show el normal pioneer at cright
    with dissolve
    dv "Да уж не тупые. Поняли, что проигравший выбывает."
    "Перебила его Алиса."
    dv "О правилах игры давай."
    hide dv
    show el sad pioneer at center
    with dissolve
# ------------------------------------------------------------- ADD Убираем схему турнира
    python:
        renpy.hide('alt_tournament_bg',layer='underlay')
        renpy.transition(dissolve)
# ------------------------------------------------------------- /ADD
    el "Ладно."
    "Смутившийся было Электроник мгновенно набрал привычный темп."
    show el smile pioneer at center with dspr
    el "Основное правило — проигравший выбывает. Поэтому никаких вторых шансов, переигровок, реваншей и прочего!"
    "Он отмахнулся от тянущей руку Ульянки, и продолжил."
    el "Каждый тур состоит из двух игр, если и после них у игроков будет ничья, исход решит третья партия. После этого проигравшие в туре выбывают, и начинается сле…"
    me "Я тебя умоляю."
    "Не выдержал я."
    me "Хватит уж о системе плей-офф! Мы все прекрасно знаем, как она работает! Давай о правилах игры!"
    el "Я уже почти перешёл к ним."
    "Выкрутился Электроник."
    el "Поскольку добровольцев…"
    "Он кинул взгляд в мою сторону и мгновенно поправился."
    el "Участников будет восемь, то туров, будет, соответственно, три."
    show el laugh pioneer with dspr
    "Тут у него загорелась во лбу звезда, и он поднял указательный палец."
    el "Победитель последнего тура получит огромный приз!"
    show dv angry pioneer2 at left
    show el surprise pioneer at cright
    $ meet('we',"Семён | Алиса")
    we "К игре!" with vpunch
    $ meet('we',"Хором")
    "Хором с Алисой рявкнули мы."
    el "Да я уже почти там. Чего вы, в самом деле!"
    "Он спрятал растерянность, делая вид, что прочищает горло."
    hide dv
    show el normal pioneer at center
    with dissolve
    el "Итак, все комбинации покерные, вы должны собрать у себя комбинацию сильнее, чем у противника. Двойку, тройку, четвёрку…"
    show us grin pioneer at cleft
    show el normal pioneer at cright
    with dissolve
    us "Пятёрку!"
    "Крикнула Ульяна, видимо, уставшая от того, что её игнорируют."
    el "Если кто-то не в курсе относительно ценности комбинаций."
    "Проигнорировал реплику Эл."
    hide us
    show el normal pioneer at center
    with dissolve
    el "Их можно посмотреть на таблице."
    "И он показал на другую половину бумажного листа."
# ----------------------------------------------------------------------------------- ADD Показываем правила игры
    if persistent.altRulesRead_new:                            # если правила игры уже прочитаны
        menu:
            "Показать комбинации":
                jump alt_day2_poker_rules_reading
            "Комбинации вроде бы помню, но нужна подсказка при игре":
                $ alt_hint_poker_contractual = True
                jump alt_day2_poker_rules_known
            "Я комбинации знаю, и подсказки не нужны":
                $ alt_hint_poker_contractual = False
                jump alt_day2_poker_rules_known
    else:                                                       # если ещё правил не читали — читаем.
        jump alt_day2_poker_rules_reading

label alt_day2_poker_rules_reading:
    $ alt_hint_poker_contractual = True
    $ set_mode_nvl()
    "{size=35}{u}Возможные комбинации карт в порядке увеличения достоинства:{/u}{/size}{nw}"
    ""

    "- {b}Старшая карта{/b} (англ. {i}high card{i}): ни одна из вышеописанных комбинаций,{nw}"
    if persistent.font_size == 'small':
        "например: {b}{color=#FF6600}Т{image=suit_2ch_S} 10{image=suit_2ch_S}{color=#009833} 9{image=suit_utan_S} 5{image=suit_uvao_S} 4{image=suit_uvao_S}{/color}{color=#FF6600} 2{image=suit_ussr_S}{/color}{/color}{/b}."
    elif persistent.font_size == 'large':
        "например: {b}{color=#FF6600}Т{image=suit_2ch_L} 10{image=suit_2ch_L}{color=#009833} 9{image=suit_utan_L} 5{image=suit_uvao_L} 4{image=suit_uvao_L}{/color}{color=#FF6600} 2{image=suit_ussr_L}{/color}{/color}{/b}."
    "Вышеприведённая комбинация называется «старший туз»."
    "Если у соперников на руках оказывается по старшей карте,{nw}"
    "победитель определяется по старшей из имеющихся на руках карт."
    "Если старшие карты у игроков равны, объявляется ничья.{nw}"
    ""

    if persistent.font_size == 'small':
        "- {b}Пара{/b}/Двойка (англ. {i}one pair{/i}): две карты одного достоинства, например: {b}{color=#FF6600}9{image=suit_ussr_S}{color=#009833} 9{image=suit_utan_S}{/color}{/b}."
    elif persistent.font_size == 'large':
        "- {b}Пара{/b}/Двойка (англ. {i}one pair{/i}): две карты одного достоинства, например: {b}{color=#FF6600}9{image=suit_ussr_L}{color=#009833} 9{image=suit_utan_L}{/color}{/b}."
    "При наличии этой комбинации у двух игроков, преимущество у того, у кого выше{nw}"
    "достоинство карт, составляющих пару. Если пары идентичны, объявляется ничья.{nw}"
    ""

    pause(1)
    nvl clear

    if persistent.font_size == 'small':
        "- {b}Две пары{/b}/Две двойки/Два плюс два (англ. {i}two pairs{/i}): две пары карт, например: {b}{color=#009833}8{image=suit_uvao_S} 8{image=suit_utan_S} {color=#FF6600}4{image=suit_ussr_S} 4{image=suit_2ch_S}{/color}{/b}."
    elif persistent.font_size == 'large':
        "- {b}Две пары{/b}/Две двойки/Два плюс два (англ. {i}two pairs{/i}): две пары карт, например: {b}{color=#009833}8{image=suit_uvao_L} 8{image=suit_utan_L} {color=#FF6600}4{image=suit_ussr_L} 4{image=suit_2ch_L}{/color}{/b}."
    "Если на руках {b}три{/b} пары, пара карт самого младшего достоинства не учитывается,{nw}"
    "{i}комбинации «Три пары» в игре нет{/i}."
    "Когда у двух игроков на руках окажутся по две пары, старшей является та,{nw}"
    "в которую входят две наиболее высокие по достоинству карты."
    "В случае, когда старшие пары карт оказываются идентичными, старшинство{nw}"
    "комбинации в целом определяется по младшей паре карт."
    "Победителем будет считаться игрок, у которого младшая пара состоит из старших карт.{nw}"
    "Если у обоих игроков комбинации по достоинству карт полностью идентичны, объявляется ничья.{nw}"
    ""

    "- {b}Тройка{/b}/Сет/Триплет/Трипс (англ. {i}three of a kind, set{/i} — «три одинаковых», «набор»):{nw}"
    if persistent.font_size == 'small':
        "три карты одного достоинства, например: {b}{color=#009833}7{image=suit_uvao_S} 7{image=suit_utan_S} {color=#FF6600}7{image=suit_2ch_S}{/color}{/b}."
    elif persistent.font_size == 'large':
        "три карты одного достоинства, например: {b}{color=#009833}7{image=suit_uvao_L} 7{image=suit_utan_L} {color=#FF6600}7{image=suit_2ch_L}{/color}{/b}."
    "Когда у двух соперников на руках одновременно окажутся тройки, победителем объявляется{nw}"
    "тот игрок, у которого тройку составляют карты более высокого достоинства."
    "Идентичных троек, как и покеров, и фулл-хаусов, в игре быть не может.{nw}"
    ""

    pause(1)
    nvl clear

    "- {b}Стрит{/b} (англ. {i}straight{/i} — «порядок»): пять карт по порядку любых мастей,{nw}"
    if persistent.font_size == 'small':
        "например: {b}{color=#FF6600}5{image=suit_2ch_S} 4{image=suit_ussr_S} {color=#009833}3{image=suit_utan_S} {color=#FF6600}2{image=suit_2ch_S} Т{image=suit_2ch_S}{/color}{/color}{/b}."
    elif persistent.font_size == 'large':
        "например: {b}{color=#FF6600}5{image=suit_2ch_L} 4{image=suit_ussr_L} {color=#009833}3{image=suit_utan_L} {color=#FF6600}2{image=suit_2ch_L} Т{image=suit_2ch_L}{/color}{/color}{/b}."
    "Если на руках оказывается {b}шесть{/b} карт по порядку, младшая карта в комбинации не участвует.{nw}"
    "Туз может как начинать порядок, так и заканчивать его."
    if persistent.font_size == 'small':
        "В приведённом выше примере {b}{color=#FF6600}Т{image=suit_2ch_S}{/color}{/b} заканчивает комбинацию и его достоинство{nw}"
        "оценивается в единицу, а {b}{color=#FF6600}5{image=suit_2ch_S}{/color}{/b} считается старшей картой."
        "Вышеприведённая комбинация является самым младшим стритом; самый старший стрит —{nw}"
        "это стрит от туза: {b}{color=#FF6600}Т{image=suit_ussr_S} {color=#009833}К{image=suit_uvao_S} {color=#FF6600}Д{image=suit_2ch_S} В{image=suit_2ch_S} 10{image=suit_ussr_S}{/color}{/color}{/b}."
    elif persistent.font_size == 'large':
        "В приведённом выше примере {b}{color=#FF6600}Т{image=suit_2ch_L}{/color}{/b} заканчивает комбинацию и его достоинство{nw}"
        "оценивается в единицу, а {b}{color=#FF6600}5{image=suit_2ch_L}{/color}{/b} считается старшей картой."
        "Вышеприведённая комбинация является самым младшим стритом; самый старший стрит —{nw}"
        "это стрит от туза: {b}{color=#FF6600}Т{image=suit_ussr_L} {color=#009833}К{image=suit_uvao_L} {color=#FF6600}Д{image=suit_2ch_L} В{image=suit_2ch_L} 10{image=suit_ussr_L}{/color}{/color}{/b}."
    "При одновременном наличии стритов у двух игроков победитель определяется по старшей{nw}"
    "карте комбинации; если и старшие карты окажутся одинаковыми — объявляется ничья.{nw}"
    ""

    if persistent.font_size == 'small':
        "- {b}Флеш{/b} (англ. {i}flush{/i} — «масть»): пять карт одной масти, например: {b}{color=#009833}К{image=suit_utan_S} В{image=suit_utan_S} 8{image=suit_utan_S} 4{image=suit_utan_S} 3{image=suit_utan_S}{/b}.{nw}"
    elif persistent.font_size == 'large':
        "- {b}Флеш{/b} (англ. {i}flush{/i} — «масть»): пять карт одной масти, например: {b}{color=#009833}К{image=suit_utan_L} В{image=suit_utan_L} 8{image=suit_utan_L} 4{image=suit_utan_L} 3{image=suit_utan_L}{/b}.{nw}"
    "Такую комбинацию для оценки называют «флеш от короля» — старшей карты комбинации."
    "Самая старшая комбинация — с тузом.{nw}"
    "Если на руках оказывается {b}шесть{/b} карт одной масти, младшая карта комбинации игнорируется."
    "Если у обоих соперников на руках будет такая комбинация, преимущество отдаётся тому,{nw}"
    "у кого старшая карта в комбинации окажется более высокого достоинства."
    "Если же получится так, что достоинство старших карт одинаково, объявляется ничья.{nw}"
    ""

    pause(1)
    nvl clear

    "- {b}Фулл-хаус{/b}/Полный дом/Три плюс два (англ. {i}full house, full boat{/i} — «полный дом», «полная лодка»):{nw}"
    if persistent.font_size == 'small':
        "одна тройка и одна пара, например: {b}{color=#FF6600}10{image=suit_ussr_S} 10{image=suit_2ch_S} {color=#009833}10{image=suit_utan_S} 8{image=suit_uvao_S} {color=#FF6600}8{image=suit_ussr_S}{/color}{/color}{/b}{/b}."
    elif persistent.font_size == 'large':
        "одна тройка и одна пара, например: {b}{color=#FF6600}10{image=suit_ussr_L} 10{image=suit_2ch_L} {color=#009833}10{image=suit_utan_L} 8{image=suit_uvao_L} {color=#FF6600}8{image=suit_ussr_L}{/color}{/color}{/b}{/b}."
    "Если на руках две тройки, тройка карт младшего достоинства считается, как пара карт;{nw}"
    "{i}комбинации «Две тройки» в игре нет{/i}."
    "Если у соперников одновременно оказались на руках такие комбинации,{nw}"
    "старшей считается та, в которой тройку составляют более высокие по достоинству карты,"
    if persistent.font_size == 'small':
        "например: {b}{color=#009833}В{image=suit_uvao_S} {color=#FF6600}В{image=suit_2ch_S} В{image=suit_ussr_S} {color=#009833}9{image=suit_uvao_S} 9{image=suit_utan_S}{/color}{/color}{/b}{/b} старше, чем {b}{color=#FF6600}7{image=suit_2ch_S} 7{image=suit_ussr_S} {color=#009833}7{image=suit_utan_S} Т{image=suit_uvao_S} {color=#FF6600}Т{image=suit_2ch_S}{/color}{/color}{/b}."
    elif persistent.font_size == 'large':
        "например: {b}{color=#009833}В{image=suit_uvao_L} {color=#FF6600}В{image=suit_2ch_L} В{image=suit_ussr_L} {color=#009833}9{image=suit_uvao_L} 9{image=suit_utan_L}{/color}{/color}{/b}{/b} старше, чем {b}{color=#FF6600}7{image=suit_2ch_L} 7{image=suit_ussr_L} {color=#009833}7{image=suit_utan_L} Т{image=suit_uvao_L} {color=#FF6600}Т{image=suit_2ch_L}{/color}{/color}{/b}."
    "Два фулл-хауса, как и два покера, одинаковыми быть не могут (джокеров в колоде нет).{nw}"
    ""

    "- {b}Покер{/b}/Каре/Четвёрка (англ. {i}four of a kind, quads{/i} — «четыре одинаковых»): четыре карты{nw}"
    if persistent.font_size == 'small':
        "одинакового достоинства, например: {b}{color=#FF6600}8{image=suit_ussr_S} 8{image=suit_2ch_S} {color=#009833}8{image=suit_uvao_S} 8{image=suit_utan_S}{/color}{/b}{/b}, остальные карты не важны."
    elif persistent.font_size == 'large':
        "одинакового достоинства, например: {b}{color=#FF6600}8{image=suit_ussr_L} 8{image=suit_2ch_L} {color=#009833}8{image=suit_uvao_L} 8{image=suit_utan_L}{/color}{/b}{/b}, остальные карты не важны."
    "Если в дополнение к покеру на руках у игрока имеется ещё и пара, она не считается;{nw}"
    "{i}комбинации «Четыре + два» в игре нет{/i}."
    "Два покера принципиально не могут быть одинаковыми, так что когда у двух игроков в наличии{nw}"
    "такие комбинации, побеждает тот, у кого покер состоит из карт более высокого достоинства.{nw}"
    ""

    pause(1)
    nvl clear

    "- {b}Стрит-флеш{/b} (англ. {i}straight flush{/i} — «масть по порядку»): любые пять карт одной масти по порядку,{nw}"
    if persistent.font_size == 'small':
        "например: {b}{color=#009833}9{image=suit_utan_S} 8{image=suit_utan_S} 7{image=suit_utan_S} 6{image=suit_utan_S} 5{image=suit_utan_S}{/color}{/b}. Туз может как начинать порядок (роял-флеш),{nw}"
        "так и заканчивать его: {b}{color=#009833}5{image=suit_uvao_S} 4{image=suit_uvao_S} 3{image=suit_uvao_S} 2{image=suit_uvao_S} Т{image=suit_uvao_S}{/color}{/b}."
        "Комбинации карт {b}{color=#FF6600}2{image=suit_ussr_S} Т{image=suit_ussr_S} К{image=suit_ussr_S} Д{image=suit_ussr_S} В{image=suit_ussr_S}{/color}{/b} или {b}{color=#FF6600}4{image=suit_2ch_S} 3{image=suit_2ch_S} 2{image=suit_2ch_S} Т{image=suit_2ch_S} К{image=suit_2ch_S}{/color}{/b} — не являются стрит-флешами.{nw}"
    elif persistent.font_size == 'large':
        "например: {b}{color=#009833}9{image=suit_utan_L} 8{image=suit_utan_L} 7{image=suit_utan_L} 6{image=suit_utan_L} 5{image=suit_utan_L}{/color}{/b}. Туз может как начинать порядок (роял-флеш),{nw}"
        "так и заканчивать его: {b}{color=#009833}5{image=suit_uvao_L} 4{image=suit_uvao_L} 3{image=suit_uvao_L} 2{image=suit_uvao_L} Т{image=suit_uvao_L}{/color}{/b}."
        "Комбинации карт {b}{color=#FF6600}2{image=suit_ussr_L} Т{image=suit_ussr_L} К{image=suit_ussr_L} Д{image=suit_ussr_L} В{image=suit_ussr_L}{/color}{/b} или {b}{color=#FF6600}4{image=suit_2ch_L} 3{image=suit_2ch_L} 2{image=suit_2ch_L} Т{image=suit_2ch_L} К{image=suit_2ch_L}{/color}{/b} — не являются стрит-флешами.{nw}"
    "Если на руках у игрока оказывается {b}шесть{/b} карт по порядку, младшая карта игнорируется."
    "Если у двух игроков одновременно на руках оказывается стрит-флеш, выигрывает тот,{nw}"
    "у кого комбинация начинается с карты более высокого достоинства."
    "Если у обоих игроков стрит-флеши идентичные, объявляется ничья.{nw}"
    ""

    "- {b}Роял-флеш{/b} (англ. {i}royal flush{/i} — «королевская масть»): не является отдельной комбинацией,{nw}"
    "а является частным случаем стрит-флеша, старшим из всех возможных, и состоит из 5 старших{nw}"
    if persistent.font_size == 'small':
        "(туз, король, дама, валет, десять) карт одной масти, например: {b}{color=#FF6600}Т{image=suit_ussr_S} К{image=suit_ussr_S} Д{image=suit_ussr_S} В{image=suit_ussr_S} 10{image=suit_ussr_S}{/color}{/b}."
    elif persistent.font_size == 'large':
        "(туз, король, дама, валет, десять) карт одной масти, например: {b}{color=#FF6600}Т{image=suit_ussr_L} К{image=suit_ussr_L} Д{image=suit_ussr_L} В{image=suit_ussr_L} 10{image=suit_ussr_L}{/color}{/b}."
    "Если хотя бы одна из пяти карт не совпадает по масти с остальными, в таком случае получившаяся{nw}"
    "комбинация будет расцениваться как стрит от туза."
    "Эта комбинация выпадает достаточно редко; может быть, кому-то и повезёт…{nw}"
    ""

    pause(1)
    $ set_mode_adv()
    $ persistent.altRulesRead_new = True

label alt_day2_poker_rules_known:
# ----------------------------------------------------------------------------------- /ADD
    el "Ну а сейчас для лучшего усвоения материала, давайте сыграем пробную партию."
    el "На сторону сдаётся по шесть карт…"
    show us dontlike pioneer at left
    show el angry pioneer at right
    with dissolve
    extend " По шесть, а не по двенадцать!"
    "Закричал он, кинув косой взгляд на столик Шурика и Ульяны."
    "Немудрено — рыжая бестия забрала себе все 12 карт и разглядывала их, выбирая покрасивее."
    hide us with dissolve
    "После нескольких минут споров и ругани Ульянка фыркнула и вернула карты на родину, после чего, перемешав колоду, сдала себе и Шурику по шесть карт."
# --------------------------------------------------------------------- ADD Блокировка роллбэка включена
    $ d2_cardgame_block_rollback = True
# --------------------------------------------------------------------- /ADD
    stop music fadeout 2


    if persistent.altCardsDemo_new:
        menu:
            "Пройти обучение":
                jump alt_day2_demo_play_new
            "Пропустить обучение":
                jump alt_day2_cards_continue_new

label alt_day2_demo_play_new:
    python:
        dialogs = {
                        (3, 'rival_select','call'): 'alt_day2_demo_play_intro_new',
                        (3, 'me_defend_1','call'):  'alt_day2_demo_play_me_defend_1_new',
                        (3, 'me_defend_2','call'):  'alt_day2_demo_play_me_defend_2_new',
                        (3, 'me_select_1','call'):  'alt_day2_demo_play_me_select_1_new',
                        (3, 'rival_defend','call'): 'alt_day2_demo_play_rival_defend_new',
                        (2, 'rival_select','jump'): 'alt_day2_demo_play_after_loop_new'
                    }
        generate_cards_alt('bg hall', dialogs)
        rival = CardGameRivalWiseUsual(un_avatar_set, u"Пробная игра", 'foolplay', 5)
        alt_name_my_rival_r = "Лены"
        VISIBLE = False
        alt_whose_first_move = 'rival'
    jump cards_gameloop_wise_alt

label alt_day2_demo_play_intro_new:
    play music music_list["get_to_know_me_better"] fadein 2
    show el normal pioneer at cleft with dissolve
    $ show_cards_alt()
    $ renpy.transition(dissolve)
    el "Это не просто карты."
    if alt_day2_walk == 1:
        th "Это ещё и ваш способ оставить противника без штанов."
        th "Если бы мы играли на деньги…"
        dreamgirl "Или на раздевание…"
        "Впрочем, не будем о грустном."
    el "Это ваши войска специального назначения. {w}Элита!"
    el "Вы дорожите каждым из них, ведь его жизнь неповторима."
    el "Потеря каждого из них критична."
    el "А теперь переверните карты и посмотрите."
    $ VISIBLE = True
    $ alt_hint_poker = True
    if alt_day2_walk == 1:
        $ INVISIBLE = True
    $ show_cards_alt()
    $ renpy.transition(dissolve)
    "Чего и следовало ожидать, Ульянка перевернула карты Шурика, и задумчиво изучала их."
    show el angry pioneer at cleft with dspr
    el "Свои карты!"
    "Закричал Электроник."
    el "Свои! А не чужие."
    us "А это была разведка! Вот!"
    "По сравнению с непрошибаемым Шуриком, Ульяна являла собой образец неуправляемой стихии."
    "Вздохнув, Шурик собрал свои карты и, тщательно перемешав, сдал себе ещё шестёрку карт."
    show el normal pioneer at cleft with dspr
    "Между тем, Электроник продолжил объяснение:"
    el "Итак, вы во главе элитных войск."
    el "Но само сражение ещё впереди. А пока вам надо укрепить порядки."
    "Окопаться, не иначе."
    el "А для этого… Необходимо сманивать элиту противника на свою сторону!"
    us "Сманивать в смысле «красть»?"
    "В голосе Ульяны слышался неприкрытый восторг."
    show el upset pioneer at cleft with dspr
    el "В целом, д-да…"
    "Ведущего немного смутил эпитет, но крыть было нечем, и он согласился."
    show el normal pioneer at cleft with dspr
    el "В целом. Но не всё так просто."
    el "Первым ходом вы намечаете себе цель, и пытаетесь её сманить."
    el "Вы не видите, кто это, поэтому здесь работает удача."
    us "Мой дедушка — офицер!"
    "Заявила Ульяна."
    show el smile pioneer at cleft with dspr
    el "Итак, противник тянется к карте, но и вы не должны дремать!"
    el "У вас есть две попытки запутать врага, поменяв карты местами!"
    show el serious pioneer at cleft with dspr
    el "Или можно не менять, если под ударом ненужная вам карта. Просто пропускаете ход, и карта отходит к атакующему."
    el "Естественно, обороняющийся рано или поздно становится атакующим — и вот тогда может вернуть карту или забрать нужную карту у противника."
    show el grin pioneer at cleft with dspr
    el "Но от слов к делу. На практике это легче понять, правда?"
    el "Так что… Играем!"

    hide el with dissolve
    me "Первый ход твой…"
    "Я, как мог, разложил карты поудобнее."
    "И Лена, смутившись ещё больше обычного, потянулась к моим картам…"
    return

label alt_day2_demo_play_me_defend_1_new:
    "Но тут её рука застыла на полпути."
    un "Т-ты будешь…"
    th "Точно! Я же должен защищать свою карту!"
    "Я вспомнил, что там говорил Электроник…"
    th "Чтобы попытаться запутать соперника, можно поменять карты местами — и так два раза. А можно и не менять…"
    th "Защищать мне эту карту или нет?"
    return

# ============================================ добавлена одна метка
label alt_day2_demo_play_me_defend_2_new:
    th "И Лена может изменить свой выбор, взяв другую карту, а может и не менять."
    th "Понемногу всё становилось понятно!"
    return
# ============================================ добавлена одна метка

label alt_day2_demo_play_me_select_1_new:
    me "Теперь моя очередь."
    th "Я могу вернуть украденную карту или выбрать любую другую…"
    if alt_day2_walk == 1:
        th "А зная карты противника, легко выбрать нужную…"
        th "Никогда бы не подумал, что буду жульничать на турнире, но, возможно, как раз это меня и спасёт…"
    return

label alt_day2_demo_play_rival_defend_new:
    th "Лена может попробовать защитить свою карту."
    th "Но если я буду внимательным, то всё равно возьму ту, что выбрал с самого начала…"
    return

label alt_day2_demo_play_after_loop_new:
    $ show_cards_alt()
    $ renpy.transition(dissolve)
    th "Получилось!"
    window auto
    $ ui.jumpsoutofcontext('alt_day2_cards_continue_new')

label alt_day2_cards_continue_new:
    scene bg int_dining_hall_sunset with dissolve
    python:
        renpy.scene('underlay')
    $ persistent.altCardsDemo_new = True
    play music music_list["my_daily_life"] fadein 5
    "Электроник, до этого наблюдавший за нами, удовлетворённо кивнул."
    "Похоже, теперь мы действительно разобрались в его игре."
    show el normal pioneer at center with dissolve
    el "Итак, во время игры противники три раза обмениваются своими бойцами, а потом открывают карты."
    el "И мы смотрим, чья армия сильнее."
    hide el with dissolve
    "Электроник отошёл к своему ватману, а Ульяна не выдержала и закричала."
    show us laugh pioneer with dissolve
    us "Моя армия будет самой сильной!"
    show us grin pioneer with dspr
    us "Давайте уже играть!"
    hide us with dissolve

label alt_day2_tournament_prep_new:
    scene bg int_dining_hall_sunset with dissolve
    show mt normal pioneer with dissolve
    mt "Давайте-ка мы немного разнообразим игру!"
    show el surprise pioneer at left with dissolve
    el "Что вы имеете в виду?"
    show mt laugh pioneer with dspr
    mt "Я вижу, тут кое-кто очень настроен на победу, так что внесём элемент случайности."
    hide mt with dissolve
    "Она достала из кармана несколько бумажек и, быстро нарвав их, написала на них номера, ссыпала в панамку и обнесла присутствующих."
    show el sad pioneer with dspr
    el "Воооот, лишние хлопоты."
    "Вздохнул парень."
    show mt normal pioneer with dissolve
    mt "Всё хорошо! {w}Тянем жребий и по нему распределяемся на пары."
    mt "А то знаю я эти договорные матчи!"
    "Не прошло и пяти минут, а мы уже разбились по парам."

    if persistent.altCardsWon1_new or persistent.altCardsFail_new:
        menu:
            "Играть самостоятельно":
                pass
            "Победа в финале" if persistent.altCardsWon3_new:
                $ alt_day2_detour_1_tour = True                         # Пропускаем 1 тур
                $ alt_day2_detour_semifinal = True                      # Пропускаем полуфинал
                $ alt_day2_detour_final = True                          # Пропускаем финал
                $ alt_day2_tournament_fast_win = True                   # Победа в финале на халяву
                $ karma += 10
                menu:
                    "Против случайного соперника":
                        pass
                    "Против Лены":
                        $ alt_day2_detour_number = 1
                    "Против Слави":
                        $ alt_day2_detour_number = 2
                    "Против Алисы":
                        $ alt_day2_detour_number = 3
                    "Против Мику":
                        $ alt_day2_detour_number = 4
                    "Против Ульяны":
                        $ alt_day2_detour_number = 5
                    "Против Шурика":
                        $ alt_day2_detour_number = 6
                    "Против Жени":
                        $ alt_day2_detour_number = 7
            "Поражение в финале" if persistent.altCardsWon2_new:
                $ alt_day2_detour_1_tour = True                         # Пропускаем 1 тур
                $ alt_day2_detour_semifinal = True                      # Пропускаем полуфинал
                $ alt_day2_detour_final = True                          # Пропускаем финал
                $ karma -= 10
                menu:
                    "Против случайного соперника":
                        $ alt_day2_detour_number = 0
                    "Против Лены":
                        $ alt_day2_detour_number = 1
                    "Против Слави":
                        $ alt_day2_detour_number = 2
                    "Против Алисы":
                        $ alt_day2_detour_number = 3
                    "Против Мику":
                        $ alt_day2_detour_number = 4
                    "Против Ульяны":
                        $ alt_day2_detour_number = 5
                    "Против Шурика":
                        $ alt_day2_detour_number = 6
                    "Против Жени":
                        $ alt_day2_detour_number = 7
            "Поражение в полуфинале" if persistent.altCardsWon1_new:
                $ alt_day2_detour_1_tour = True                         # Пропускаем 1 тур
                $ alt_day2_detour_semifinal = True                      # Пропускаем полуфинал
                $ karma -= 10
            "Поражение в первом же коне":
                $ alt_day2_detour_1_tour = True                         # Пропускаем 1 тур

 # ---------------------------------------------------------------------------------
label alt_day2_tournament_tour_1_new:
    $ alt_tournament_state = "1_round_start"                                                # устанавливаем начало 1-го раунда
    $ alt_day2_gamblers_begin = alt_gamblers_shuffler()                                     # вызываем рандомизатор — получаем список игроков, отсортированный по уcловным номерам.
    $ alt_my_rival_1_tour = alt_get_me_rival(alt_day2_gamblers_begin)                       # узнаём своего соперника
    $ alt_name_my_rival_i = alt_my_rival_1_tour.name['i']                                   # узнаём ИМЯ своего соперника (в именительном падеже)
    $ alt_name_my_rival_r = alt_my_rival_1_tour.name['r']                                   # узнаём ИМЯ своего соперника (в родительном падеже)
    $ alt_name_my_rival_d = alt_my_rival_1_tour.name['d']                                   # узнаём ИМЯ своего соперника (в дательном падеже)
    $ alt_name_my_rival_v = alt_my_rival_1_tour.name['v']                                   # узнаём ИМЯ своего соперника (в винительном падеже)
    $ alt_name_my_rival_t = alt_my_rival_1_tour.name['t']                                   # узнаём ИМЯ своего соперника (в творительном падеже)
    $ alt_spr_my_rival = alt_my_rival_1_tour.take                                           # получаем спрайт соперника — заголовок
    $ alt_emo_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][0]                 # эмоция (строка)
    $ alt_acc_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][1]                 # аксессуар (строка)
    $ alt_clot_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][2]                # одежда (строка)
    $ alt_pos_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][3]                 # положение
    $ alt_nick_my_rival = alt_my_rival_1_tour.nick                                          # получаем характер соперника (для диалога)
 # ---------------------------------------------------------------------------------
    scene bg int_dining_hall_sunset with dissolve
    $ renpy.fix_rollback()                                                                  # фиксируем выбор — "откатом" поменять будет нельзя
    "Рандом послал мне в оппоненты {nw}%(alt_name_my_rival_v)s.{w}"                             # называем своего соперника

# ------------------------------------------------- ДИАЛОГИ
    if alt_my_rival_1_tour.take == 'un':
        show un shy pioneer at cright with dissolve
        me "И снова добрый вечер."
        show un smile pioneer with dspr
        "Она смущённо улыбнулась, но ничего не сказала."

    elif alt_my_rival_1_tour.take == 'sl':
        show sl smile2 pioneer at cright with dissolve
        sl "Знаешь, я не очень хороша в картах."
        me "Да я вообще ничего про эту игру не знаю."
        "Славя улыбнулась мне и села напротив."

    elif alt_my_rival_1_tour.take == 'dv':
        show dv grin pioneer2 at cright with dissolve
        dv "Ну что, готов к сокрушительному поражению?"
        "Усмехнулась она, садясь на противоположное место."
        if herc or loki:
            me "А как же. {w}Я принесу на твою могилку два гладиолуса."
        else:
            me "Алис, может, всё-таки не надо?.."
            dv "Надо, Сёма, надо."

    elif alt_my_rival_1_tour.take == 'mi':
        show mi smile pioneer at cright with dissolve
        if ('music_club' in list_voyage_7dl):
            mi "И снова здравствуй, Сенечка."
        else:
            mi "Ой, привет, Семён!"
        if loki:
            me "Ну привет, Мику."
        elif herc:
            me "И тебе не хворать."
        else:
            me "Привет."
        show mi laugh pioneer with dspr
        mi "Как здорово, что ты достался мне в противники! Я очень хотела, чтобы это был ты!"
        "Я немного опешил."
        me "Зачем?"
        show mi grin pioneer with dspr
        mi "Ну как же, как же!"
        "Воскликнула Мику."
        if ('music_club' in list_voyage_7dl):
            show mi smile pioneer with dspr
            mi "Ты же новый человек в лагере, а мы с тобой ещё толком не поговорили друг с другом!"
            th "Так вот она о чём."
            "Сказать по правде, я бы с радостью променял карточную игру на беседу с Мику."
            "Она может и болтушка, но болтушка красивая."
            "Главное умело фильтровать поток её слов и вычленять самое главное."
            "А там глядишь и увижу в ней ещё что-то."
            "Однако…"
            me "Давай после игры, ладно?"
            me "Раз уж взялись за гуж… — и далее по тексту."
            show mi happy pioneer with dspr
            mi "Мы можем побеседовать в процессе."
            "Продолжала настаивать хафу."
            show mi smile pioneer with dspr
            mi "Как говорит мой Па — ничто не мешает совместить приятное с полезным!"
            "Я бы не назвал турнир «полезным»."
            me "По рукам."
        else:
            show mi laugh pioneer with dspr
            mi "Ты же новый человек в лагере, а мы ещё толком не знакомы!"
            "Не переставая болтать, она села за стол и сложила руки."
            th "Эта игра будет о-о-очень долгой."
            if dr:
                dreamgirl "Ты дрищ, а значит, должен страдать."
                th "Катись к чёрту."

    elif alt_my_rival_1_tour.take == 'us':
        stop music fadeout 2
        show us laugh pioneer at cright with dissolve
        us "Готов поддаваться?"
        play music music_7dl["carefree"] fadein 1
        me "И не мечтай."
        show us calml pioneer with dspr
        us "И не надо! Но играть будем по моим правилам!"
        me "Это по каким это?"
        us "Увидишь!"

    elif alt_my_rival_1_tour.take == 'sh':
        show sh normal pioneer at cright with dissolve
        sh "Ну что, пусть победит сильнейший?"
        "Я молча пожал ему руку."

    elif alt_my_rival_1_tour.take == 'mz':
        show mz normal glasses pioneer at cright with dissolve
        mz "Я твой противник."
        "Скрипнула она, присаживаясь напротив."
        "Я молча кивнул в ответ."
# ------------------------------------------------- /ДИАЛОГИ


label alt_day2_participate_new:
    $ alt_day2_gamblers_1_tour = alt_gamblers_arrange(alt_day2_gamblers_begin)      # получаем список игроков, рассаженных по столам попарно (1 тур)
    $ renpy.fix_rollback()                                                          # фиксируем выбор — "откатом" поменять будет нельзя
    $ places_my_table = alt_get_my_table(alt_day2_gamblers_1_tour)                  # Стол Семёна = [место Семёна, место соперника, № их стола]

    if not alt_day2_detour_1_tour:                                                  # если НЕ пропуск 1 тура
        scene bg int_dining_hall_sunset with dissolve
        "Пока суд да дело, я решил разузнать, какая диспозиция сложилась на игровом поле."
        $ alt_mstt = 9
        call show_tournament_table                                                  # показываем турнирную таблицу — ПУСТУЮ


    $ alt_table_no = 1                                                              # № стола = 1 (начинаем с первого)
    $ alt_mstt = 0                                                                  # обнуляем глобальный счетчик таблицы
    $ alt_random_box_1 = range(1,len(alt_table_affiliation)+1)                      # черный ящик — список от 1 до длины представлений столов +1
    while alt_table_no <= 4:                                                        # перебираем столы от 1 до 4
        if not alt_day2_detour_1_tour:                                              # если НЕ пропуск 1 тура
            $ sitting_at_table,gambler_upper,gambler_lower,must_taunt = alt_declare_tournament_tables(alt_table_no)  #расссадка, игроки, таунты — по номеру стола
            "%(sitting_at_table)s"
            call show_tournament_table                                                  # переход по метке — вызов очередной фишки
            extend " %(gambler_upper)s"                                                 # выводим в окно имя верхнего игрока
            call show_tournament_table                                                  # переход по метке — вызов очередной фишки
            extend " и %(gambler_lower)s."                                              # выводим в окно имя нижего игрока
            if must_taunt != None:                                                      # если таунт есть
                "%(must_taunt)s"                                                        # выводим его

            if alt_table_no == 1 and alt_table_no != places_my_table[2]:
                "С первым столом разобрались, кто-то из них сегодня не дойдёт до финала."
            elif alt_table_no == 2 and places_my_table[2] == 1:
                "Со вторым столом разобрались, кто-то из них сегодня не дойдёт до финала."

        if alt_table_no != places_my_table[2]:                                                       # если номер стола — НЕ свой
            $ alt_day2_gamblers_1_tour[2*alt_table_no - renpy.random.choice([1,2])].winner = True    # тогда один из игроков (рандомно) — победитель в этапе
            $ renpy.block_rollback()                                                                 # блокируем роллбак
        $ alt_table_no += 1                                                                          # следующий стол
    if (alt_day2_detour_number != 0):                                                                # если выбрали конкретного соперника для финала
        $ alt_day2_gamblers_1_tour[6].winner = False                                                 # его соперник в первом коне проигрывает
        $ alt_day2_gamblers_1_tour[7].winner = True                                                  # а он сам выигрывает в первом коне
    if not alt_day2_detour_1_tour:                                                                   # если НЕ пропуск 1 тура
        "Таким нехитрым образом удалось немного разобраться с тем, кто и против кого играет."
        "Что ж…"
        if alt_day2_dv_ultim == 1:
            "Пусть мне повезёт, а одна рыжая зазнайка утрётся!"
        "Я кивнул, сигнализируя о готовности."

    if alt_day2_detour_1_tour and not alt_day2_detour_semifinal:                # если пропуск 1 тура и не пропуск полуфинала
        jump alt_day2_participate_fail_end_new                                  # переход на  поражение в 1 туре
    elif alt_day2_detour_semifinal:                                             # если пропуск полуфинала
        jump alt_day2_participate_win_end_new                                   # переход на победу в 1 туре

label alt_day2_tournament_start_new:                                            # начало 1 тура — сюда переходим при реванше
    call alt_day2_stipulation_new                                               # определяемся, кто первый ходит

#-------------------------------------------------------------------------------------------------
    # первоначальные "настройки" игроков — могут меняться по результатам игры
    # 'defense' — защита, 'gamble' — риск, 'succumb' — слив, 'foolplay' — рандом
    # вероятность ошибки: 1 = 80%, …, 4 = 20%, 5 — ошибок нет.

    if alt_my_rival_1_tour.take == 'un':                                                    # Лена
        if alt_day2_dv_ultim != 1:                                                              # если с Алисой не спорить
            $ alt_day2_gambler_behavior = 'gamble'                                              # Лена пытается рискнуть
            $ alt_day2_gambler_skill = 3                                                        # правда, ошибок многовато — 40%(3)
        else:
            $ alt_day2_gambler_behavior = 'succumb'                                             # Если поспорить — то также игра в поддавки
            $ alt_day2_gambler_skill = 4                                                        # может ошибиться  — 20%(4)
    elif alt_my_rival_1_tour.take == 'sl':                                                  # Славя будет защищаться, ошибок — 40%(3)
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 3
    elif alt_my_rival_1_tour.take == 'dv':                                                  # Алиса рискует, ошибок — 20%(4)
        $ alt_day2_gambler_behavior = 'gamble'
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_1_tour.take == 'mi':                                                  # Мику будет защищаться, ошибок — 40%(3)
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 3
    elif alt_my_rival_1_tour.take == 'us':                                                  # Ульяна будет защищаться
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 1                                                        # ошибок — 80%(1)
    elif alt_my_rival_1_tour.take == 'sh':                                                  # Шурик экспериментирует, так что может и рискнуть, и защищаться, и слить; ошибки 40%(3)
        $ alt_day2_gambler_behavior = renpy.random.choice(['defense', 'gamble'])            # у него своя кухня — набор из возможных вариантов
        $ alt_day2_gambler_skill = 3
    elif alt_my_rival_1_tour.take == 'mz':                                                  # Женя играет рандомно, как в классике, ошибки = 5
        $ alt_day2_gambler_behavior = 'foolplay'
        $ alt_day2_gambler_skill = 5
#-------------------------------------------------------------------------------------------------

label alt_day2_1_tour_re_game:                                                              # игра 1 тура — сюда возвращаемся на повторную игру
    $ alt_my_poker_hand = None
    $ alt_rival_poker_hand = None

    if alt_day2_walk == 1:
        $ VISIBLE = True
        $ INVISIBLE = True
    else:
        $ VISIBLE = True
        $ INVISIBLE = False

    python:
        dialogs = {
                        (0, 'win','jump'):'alt_day2_one_play_win_new',
                        (0, 'fail','jump'):'alt_day2_one_play_fail_new',
                        (0, 'draw','jump'):'alt_day2_one_play_draw_new'
                    }
        generate_cards_alt('bg hall', dialogs)

# ****************   НОВЫЕ  СОПЕРНИКИ   ******************************************
        if alt_my_rival_1_tour.take == 'un':
            rival = CardGameRivalWiseUsual(un_avatar_set, u"Лена", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_1_tour.take == 'sl':
            rival = CardGameRivalWiseUsual(sl_avatar_set, u"Славя", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_1_tour.take == 'dv':
            rival = CardGameRivalWiseUsual(dv_avatar_set, u"Алиса", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_1_tour.take == 'mi':
            rival = CardGameRivalWiseUsual(mi_avatar_set, u"Мику", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_1_tour.take == 'us':
            rival = CardGameRivalWiseLikeUS(us_avatar_set, u"Ульяна", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_1_tour.take == 'sh':
            rival = CardGameRivalWiseUsual(sh_avatar_set, u"Шурик", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_1_tour.take == 'mz':
            rival = CardGameRivalWiseUsual(mz_avatar_set, u"Женя", alt_day2_gambler_behavior, alt_day2_gambler_skill)
# ************************************************************************************

    $ alt_hint_poker = alt_hint_poker_contractual                                           # подсказки комбинаций — по просмотру правил
    jump cards_gameloop_wise_alt                                                            # переход карточный стол

#-------------------------------------------------------------------------------------------------
label alt_day2_participate_fail_end_new:
    $ alt_day2_result_tour = 1                                              # Семён проиграл в 1 туре

    $ persistent.altCardsFail_new = True

    $ alt_day2_gamblers_1_tour[places_my_table[1]].winner = True            # соперник выиграл
    $ alt_tournament_state = "1_round_end"                                  # устанавливаем конец 1-го раунда

    scene bg int_dining_hall_sunset with dissolve
    call alt_day2_summary_poker_round

# ---------------------------------------------------- ДИАЛОГИ
    if alt_my_rival_1_tour.take == 'un':
        $ lp_un = lp_un + 1
        stop music fadeout 2
        if alt_day2_dv_ultim == 1:
            show un angry2 pioneer at center with dissolve
            un "Ты поддался… Ты чёртов жулик, ты поддался…"
            play music music_list["you_lost_me"] fadein 2
            "О чем это она? Ещё и жуликом обозвала."
            if alt_day2_walk == 1:
                th "Впрочем, она не так уж и далека от истины."
            me "Лена, извини, но…"
            un "Не говори ничего. Я знаю, о чём ты спорил с этой рыжей."
            un "И я знаю — что на кону!"
            show un sad pioneer with dspr
            un "Ты не понимаешь, что никому такая победа не нужна? А тебя завтра… на весь лагерь…"
            me "А ты правда думаешь, что мне не плевать? Пусть говорит, что хочет. Я сделал так, как считал правильным."
        else:
            show un angry2 pioneer with dspr
            un "Что ты наделал?"
            play music music_list["you_lost_me"] fadein 2
            "Она приподнялась было над столом и тут же упала обратно."
            un "Зачем? Кому нужна такая победа…"
            me "Мне?"
            th "Она такая симпатичная, когда сердится."
        show un angry2 pioneer with dspr
        "А Лена хлопнула ладонью по столу, да так, что на секунду все смолкли и обернулись на неё."
        un "Кому нужна такая победа…"
        "Повторила она."
        me "Эта победа была нужна мне."
        "В гробовой тишине произнёс я."
        show un serious pioneer with dspr
        me "Просто для того, чтобы указать кое-кому, что не всё решают угрозы или шантаж."
        me "Наслаждайся вечером."
        stop music fadeout 3
        hide un with dissolve
        "Я кивнул и вышел из-за стола, оставляя Лену беззвучно хватать ртом воздух."
        play music music_list["my_daily_life"] fadein 5

    elif alt_my_rival_1_tour.take == 'sl':
        show sl smile pioneer with dissolve
        sl "Семён, если ты захочешь сыграть ещё раз, я не против."
        "Забавная девочка, готова даже поступиться собственной победой."
        th "Нет уж, сегодня моя очередь быть благородным."
        "Я наклонился над столом и произнёс:"
        me "Желаю тебе удачи в полуфинале!"
        sl "Но я же просто за компанию играть села!"
        sl "Я вообще карты не люблю."
        me "А что поделаешь. {w}Записалась — так играй до конца!"
        show sl sad pioneer with dspr
        me "К тому же, мне очень хочется, чтобы сегодня ты победила. Сумеешь?"
        show sl normal pioneer with dspr
        "Славя неуверенно кивнула, а я поднялся и показал ей большой палец."
        "Чуточку уверенности в себе вне привычной сферы обитания — вот что ей нужно."

    elif alt_my_rival_1_tour.take == 'dv':
        if alt_day2_dv_ultim == 1:
            show dv grin pioneer2 with dspr
            dv "Ну что, ты уже приготовился?"
            "Она упивалась моментом."
            if alt_day2_walk == 1:
                th "Мда, и стоило карты метить, если они мне не помогли?"
            else:
                pass
            me "К чему?"
            dv "Как к чему? К рассказу о том, куда смотрел, за что трогал."
            dv "Очень интересный рассказ будет, чувствую!"
            show dv laugh pioneer2 with dspr
            dv "Но ладно."
            me "Да?"
            "Я аж приподнялся на месте."
            th "Неужели передумала!"
            show dv smile pioneer2 with dissolve
            dv "Я расскажу всё в финале, когда меня будут приветствовать как победителя!"
            "Да, зря надеялся."
            "Это же Двачевская, в конце-то концов!"
            th "Ничего хорошего от неё ожидать нельзя."
        "Я постарался сохранить лицо."
        "Вежливо встал, наклонил голову, и сказал:"
        me "Поздравляю тебя с победой."
        me "И удачи в полуфинале."
        "Развернулся и ушёл к болельщикам."
        th "Может быть, удастся затеряться в толпе?"

    elif alt_my_rival_1_tour.take == 'mi':
        show mi happy pioneer with dspr
        mi "Ой, какое счастье! А то мне никогда-никогда не везло в картах, я и решила, что это не моё, а тут попросили, и я согласилась."
        mi "Я даже не думала, что сумею победить! Сенечка, ты не обижаешься? А то хочешь, переиграем, мне не жалко! Нет, правда-правда не обижаешься?"
        show mi smile pioneer with dspr
        mi "Просто я не хочу, чтобы мне было хорошо за счёт других, это плохо, мне всегда Па говорил, что счастья на чужих слезах не построишь."
        me "Всё в порядке. Ты здорово играешь, поэтому и победила."
        me "Удачи тебе в полуфинале."
        hide mi with dissolve
        "Пожелал я и, отвернувшись, удалился."

    elif alt_my_rival_1_tour.take == 'us':
        show us laugh pioneer with dissolve
        us "Хы! Продул!"
        "Спасибо, кэп."
        me "Обязательно орать об этом на всю столовую?"
        us "Ну конечно же!"
        show us grin pioneer with dspr
        us "А хочешь, ещё сыграем? {w}На просто так."
        us "Пока остальные тормозят, как раз партию успеем. Ну что?"
        me "В чём подвох?"
        us "Подвоха нет."
        us "Так что, будешь?"
        me "Спасибо, но нет."
        show us dontlike pioneer with dissolve
        us "Зануда! {w}И что, даже отыграться не хочешь?"
        us "Неужели не обидно проиграть девчонке?"
        me "Да мне фиолетово, на самом-то деле."
        th "Кто там что думает и решает, остаётся его достоянием."
        "Мудрый совет на все случаи жизни: болтать поменьше."
        us "Зануда! {w}Зануда."
        "Кричала она."
        show us dontlike pioneer at fright with move
        "А потом резко вскочила и пошла к столику, отведённому под следующую игру."
        us "Просто боишься проиграть ещё раз! Слабак!"
        me "Да, возьми меня ещё раз на «слабо», детка."
        me "Наслаждайся вечером."
        stop music fadeout 3
        hide us with dissolve
        "Я отправился в сторону толпы зрителей. Пришёл мой черёд сменить амплуа."
        play music music_list["my_daily_life"] fadein 3

    elif alt_my_rival_1_tour.take == 'sh':
        show sh normal pioneer with dissolve
        sh "Это была достойная игра. Спасибо."
        if loki:
            me "Взаимно."
        elif herc:
            "Он протянул мне руку, которую я с достоинством пожал."
        else:
            "Мы обменялись рукопожатиями."
            "Всё же крепкая у него хватка для того, кто тяжелее паяльника ничего не поднимает."
        sh "А я пошёл дальше громить вражеские порядки."

    elif alt_my_rival_1_tour.take == 'mz':
        show mz normal glasses pioneer with dissolve
        "Женя пожала плечами и встала из-за стола."
        mz "Похоже, это будет ещё проще, чем мне казалось."
# ---------------------------------------------------- \\Диалоги

    scene bg int_dining_hall_sunset with dissolve
    "А ситуация, между тем, складывалась следующая:"
    pause(.5)
    call alt_day2_1_tour_analizer                                                   # Вызов анализатора 1 раунда
    $ renpy.block_rollback()                                                          # блокируем роллбак
    stop music fadeout 3
    $ alt_drawing_of_detour()                                                       # вызываем рандомизатор пропуска полуфинала и финала
    $ renpy.fix_rollback()                                                          # фиксируем выбор — "откатом" поменять будет нельзя
    jump alt_day2_semifinal_new                                                     # переход в полуфинал ?

#------------------------------------------------------------------------------------------------
label alt_day2_participate_win_end_new:
    $ alt_day2_result_tour = 2                                              # Семён выиграл в 1 туре
    if not alt_day2_detour_semifinal:                                       # если не "выигрыш" в 1 туре скипом
        $ persistent.altCardsWonRivals_new[alt_spr_my_rival] = True         # Выиграли у этого соперника
    $ persistent.altCardsWon1_new = True
    $ alt_day2_gamblers_1_tour[places_my_table[0]].winner = True            # Семён выиграл
    $ alt_tournament_state = "1_round_end"                                  # устанавливаем конец 1-го раунда

# -------------------------------------------------------------------------
# ЕСЛИ Славя, Мику или Шурик и НЕ скип тура — итоги ДО диалогов
    if (alt_my_rival_1_tour.take in ['sl','mi','sh']) and not alt_day2_detour_semifinal:
        scene bg int_dining_hall_sunset with dissolve
        "Первый тур закончился."
        "Ситуация, между тем, складывалась следующая:"
        call alt_day2_1_tour_analizer                                                   # вызываем анализатор 1 тура
        $ renpy.block_rollback()                                                          # блокируем роллбак
# -------------------------------------------------------------------------
    pause(1)
    scene bg int_dining_hall_sunset with dissolve
    call alt_day2_summary_poker_round

# ---------------------------------------------------- ДИАЛОГИ
    if alt_my_rival_1_tour.take == 'un':
        if alt_day2_rival_win == 0:
            "У неё не было ничего."
            "А с тем, что было, я бы постеснялся открывать карты."
        else:
            "Лене досталась за эти игры пара-другая хороших карт."
            "К сожалению, для победы этого оказалось недостаточно."
        "Бедная девочка."
        show un sad pioneer with dissolve
        "Она сидела, будто сама не способная поверить в то, что только что произошло."
        if lp_un >= 6 and not alt_day2_detour_semifinal:
            menu:
                "Предложить матч-реванш":
                    $ karma += 5
                    $ lp_un += 1
                    me "Неудачная партия."
                    un "Да…"
                    me "Может, ещё разок?"
                    show un smile pioneer with dspr
                    "Лена улыбнулась."
                    un "Предложение соблазнительное, но я откажусь."
                    me "Почему?"
                    show un shy pioneer with dspr
                    un "Ну…"
                    pause(0.5)
                    if dr:
                        me "Ладно, можешь не говорить."
                        me "Не хочешь — твоё право."
                        me "Не могу же я тебя заставлять."
                        show un smile pioneer with dspr
                        "Лена благодарно улыбнулась."
                        un "Удачи. Я буду болеть за тебя."
                        me "Угу…{w} Спасибо."
                    else:
                        me "Да?…"
                        th "Прости, Лена, но я чуточку поработаю клещами."
                        show un sad pioneer with dspr
                        un "Я не слишком люблю такие игры, и играть в них совсем не умею."
                        un "Поэтому к победе я не рвусь. Ещё до начала решила для себя — будь что будет."
                        un "А реванш… {w}Реванш — это не то."
                        "А на лице явственно читалось — я не хочу больше проигрывать."
                        me "Право твоё. Настаивать не буду."
                        show un cry_smile pioneer with dspr
                        un "Спасибо."
                        show un shy pioneer with dspr
                        un "Лучше я буду болеть за тебя."
                    hide un with dissolve
                    "Она встала из-за стола и исчезла за болельщиками."
                    jump alt_day2_1_tour_end                                                 # В ПОЛУФИНАЛ
                "Ничего не делать":
                    pass
        $ lp_un -= 1
        $ lp_dv += 1
        "Я улыбнулся."
        me "Спасибо за игру!"
        show un shy pioneer with dspr
        un "Н-не за что."
        hide un with dissolve
        "Она встала из-за стола и исчезла за болельщиками."

# ====================================================== Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not alt_day2_detour_semifinal:
            "А я не мог сдержать ликования."
            th "Я подебил! То есть я победил."
            dreamgirl "Ура! {w=.4}У девочки. {w=.4}В игру, которую ни ты, ни она не знаете. {w}Велико достижение."
            th "Заткнись."
            th "Я буду радоваться победе так, как буду радоваться только когда раскатаю эту рыжую нахалку!"
            dreamgirl "Нет, ну ты и правда герой. Спору нет."
            dreamgirl "Может, следовало дать девочке выиграть? Она и так выглядит не самой счастливой, а ты выбил из-под неё остатки почвы."
            dreamgirl "И как оно по ощущениям? Стоило того?"
            th "Я сказал — заткнись."
            show blinking with dissolve
            if herc or loki:
                "У меня цель — не ободрить каждого сирого, а утереть нос одной рыжей зазнайке!"
                "Хотя, честно сказать, искушение слить партию просто для того, чтобы посмотреть, как она выполнит свои угрозы, достаточно велико. {w}Нет, ну серьезно!"
                scene bg ext_square_sunset
                show prologue_dream
                with fade
                "Завтра мы встаём, идём на линейку, а там уже на трибуне, между Ольгой Дмитриевной и Славей, стоит она."
                show dv grin pioneer2 behind prologue_dream with diam
                "И своим вредным голосом говорит — так, мол, и так, некий Семён, приехать в лагерь ещё не успел, как пошёл подглядывать за мной и даже полапал немного."
                "Да это же реклама такая, что я за неё ещё и приплачивать должен!"
                "В духе «Сёма едет! Прячьте девок!»."
                hide dv with dissolve
            else:
                "Даже если девочки внезапно начнут строить мне глазки, я не собираюсь кому-либо из них сливать партию."
                "Представляю себе, как рыжая стерлядь воплотит свои угрозы."
                scene bg ext_square_sunset
                show prologue_dream
                with fade
                "Например, на утренней линейке."
                show dv grin pioneer behind prologue_dream with dissolve
                "Выйдет вперёд, самодовольно подмигнёт мне и скажет во всеуслышанье:"
                dv "{i}Ольга Дмитриевна, разрешите доложить!{/i}"
                "И далее по тексту."
                "Коллективный суд, а вместе с ним и позор, мне обеспечен."
                dreamgirl "А вот правильный перевод твоего словоблудия — я трясусь за свою шкуру."
                dreamgirl "Волков бояться — в лес не ходить, в курсе?"
                th "Мне и в городе неплохо живётся."
                th "А волки пускай достаются охотникам."
        scene bg int_dining_hall_sunset with dissolve

    elif alt_my_rival_1_tour.take == 'sl':
        "Славя резко вскочила и оперлась кулаками о стол."
        show sl serious pioneer with dspr
        sl "А ты серьёзный противник."
        "Исподлобья процедила она."
        show sl angry pioneer with dspr
        sl "Напомни мне никогда не недооценивать тебя!"
        me "Многие, кто недооценили Семёна, горько пожалели об этом!"
        "Подыграл я."
        show sl smile2 pioneer with dspr
        "Тут она не выдержала и разулыбалась, испортив всю сценку."
        sl "А партия действительно была интересная!"
        if lp_sl >= 6 and not alt_day2_detour_semifinal:
            menu:
                "Хочешь ещё разок?":
                    $ karma += 5
                    show sl smile pioneer with dspr
                    sl "Спасибо"
                    $ lp_sl += 1
                    show sl laugh pioneer with dspr
                    extend ", но… Нет!"
                    sl "Давай-ка ты сам покажешь класс!"
                    "Девочка потрепала меня по плечу и направилась в стан болельщиков."
                    hide sl with dissolve
                    jump alt_day2_semifinal_new
                "Ничего не делать":
                    pass
        else:
            pass
        "Я улыбнулся."
        me "Спасибо за игру!"
        sl "Тебе спасибо!"
        hide sl with dissolve
        "Кивнув мне, она поднялась и отошла к Ольге Дмитриевне, и у них там завязалась оживлённая беседа."

# ====================================================== Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not alt_day2_detour_semifinal:
            "Что ж, это была трудная схватка, но я победил."
            th "Идеальное же противостояние — игра, в которой вы оба ничего не понимаете."
            dreamgirl "Ну да, ну да."
            "Пробормотал внутренний голос."
            dreamgirl "Носкиллер рандомный."
            th "Помолчи. Ты ничего не понимаешь."
            th "Это вопрос индивидуального престижа. Я буду двигаться к финалу."
            if alt_result_dv_1_tour == 4:                                                       # Дваче в другом полуфинале
                th "И раскатаю там рыжее хамло!"
            elif alt_result_dv_1_tour == 3:                                                     # Дваче в 1/2 к Семёну
                th "И раскатаю там любого!"
            elif alt_result_dv_1_tour == 2:                                                     # Дваче слетела в 1 туре
                th "Чего не скажешь о Алисе. Значит, это будет лёгкая победа."
            dreamgirl "Надежды… Мечты… Фантазии…"
            th "Ты что, сомневаешься во мне?!"
            dreamgirl "Нет-нет-нет, ты что! {w}Я в тебя верю! Я знаю твой потенциал."
            th "Вот видишь!"
            dreamgirl "Ты слетишь на полпути."
            th "Да ну тебя!"
            if alt_result_dv_1_tour == 4:                                                                # Дваче в другом полуфинале
                "Может быть, это {i}она{/i} слетит на полпути!"
                "Вот возьмёт и проиграет."
                dreamgirl "Надежды… Мечты…"
                th "Ты повторяешься."
                dreamgirl "Просто ты слишком нос задираешь. {w}А, как говорят Великие, — настоящий мастер лишён гордыни."
            elif alt_result_dv_1_tour == 3:                                                              # Дваче в 1/2 к Семёну
                th "Между прочим, у нас сейчас как раз будет шанс стреножить Рыжевскую в полуфинале."
                dreamgirl "Ну да, это нам, конечно, повезло."
                dreamgirl "Но лучше приготовься к суровому испытанию — просто так она тебе победу не отдаст!"
            elif alt_result_dv_1_tour == 2:                                                              # Дваче слетела в 1 туре
                "Я усмехнулся."
                th "А даже если и слечу."
                th "Обращаю твоё внимание, что пока мы тут препирались, Двачевская изволила вылететь в самом первом раунде."
                "Я снял воображаемую шапку и прижал её к груди."
                me "Помянем!"
                show dv angry pioneer2 far at left with dissolve
                "Двачевская оскалилась, но ничего не сказала."

    elif alt_my_rival_1_tour.take == 'dv':
        show dv sad pioneer2 with dspr
        "Алиска облажалась."
        "Ха. Ха. Ха."
        "Её вид — это то, что не купишь ни за какие мастеркарды с визами."
        "Поистине бесценное зрелище!"

# ====================================================== Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not alt_day2_detour_semifinal:
            if lp_dv >= 6:
                menu:
                    "Ну что, как я тебя?":
                        $ karma += 5
                        if loki or herc:
                            $ lp_dv += 1
                            show dv rage pioneer2 with dspr
                            "Алиса надулась, набычилась…"
                            me "Разделал как Рандом черепаху!"
                            "Не удивлюсь, если она сейчас придумает ещё какую-нибудь гадость, только чтобы уязвить меня."
                            show dv angry pioneer2 with dspr
                            "Но она меня удивила."
                            show dv laugh pioneer2 with dspr
                            dv "А ты хорош! Хорош!"
                            "Расхохоталась она, ткнув меня кулаком в плечо."
                            dv "Пожалуй, будем считать наше пари закрытым."
                            th "Уффф."
                            "Я подавил желание облегчённо вытереть лоб."
                            show dv grin pioneer2 with dspr
                            dv "А то если хочешь, можем ещё на что-нибудь поспорить?"
                            "Я отшатнулся."
                            "Но постарался ответить солидно:"
                            me "Нет. {w}Свою натюрель ты уже поставила на кон."
                            dreamgirl "Дальше только честь девичья! {w}Ну-ка, скажешь это вслух?"
                            "Ага, сейчас. У меня и «натюрель»-то вышла дрожащим голосом."
                            show dv laugh pioneer2 with dspr
                            "Алиса снова рассмеялась, увидев мою реакцию, и поднялась."
                            show dv smile pioneer2 with dspr
                            dv "Удачи тебе."
                        else:
                            "Начал было я, и, чувствуя, как запал иссякает, продолжил уже куда спокойнее:"
                            me "Кажется, я победил."
                            dv "Угу."
                            me "И ты теперь…"
                            show dv sad pioneer2 with dspr
                            pause(.4)
                            show dv guilty pioneer2 with dissolve
                            dv "Да…"
                            dv "Никому я ничего не скажу. {w}Ты победитель."
                            "Алиса выглядела подавленной и какой-то… Обескураженной, что ли."
                            "Кажется, её смутил не столько проигрыш, сколько моя на него реакция."
                            dv "Ладно, бывай."
                        hide dv with dissolve
                        jump alt_day2_1_tour_end
                    "Партия":
                        hide dv with dissolve
                        "Алиса кивнула и молча поднялась из-за стола."
                        pass
            else:
                pass
        if alt_day2_dv_ultim == 1:
            "Кажется, свою малюсенькую проблему с пари я только что успешно решил."

    elif alt_my_rival_1_tour.take == 'mi':
        show mi surprise pioneer with dissolve
        mi "Ой!"
        "Она прижала руки ко рту."
        mi "Я что, я проиграла, да? А то я так и не поняла, что тут делать, только таскала у тебя карты и не отдавала тебе свои."
        show mi upset pioneer with dspr
        "Она покачала головой."
        mi "Какая-то непонятная игра."
        show mi smile pioneer with dspr
        mi "Но всё равно, спасибо, что играл со мной!"
        if lp_mi >= 6 and not alt_day2_detour_semifinal:
            menu:
                "Может, ещё?":
                    $ karma += 5
                    $ lp_mi += 1
                    "Мне понравилось просто сидеть с ней за одним столом."
                    "Тем более, что на нас всё равно никто не смотрел."
                    "Внимание зала сфокусировалось на основных действующих лицах сегодняшнего вечера — Алисе и Ульяне."
                    me "Давай?"
                    show mi shy pioneer with dspr
                    mi "А разве так можно?"
                    me "Нет, но… Кому какое дело?"
                    show el serious pioneer at left with dissolve
                    show mi surprise pioneer with dspr
                    el "Мне есть дело!"
                    "Ответил появившийся из ниоткуда Электроник."
                    el "Ты победил, пожалте за полуфинальный столик!"
                    hide el with dissolve
                    "Блин."
                    "Моя улыбка вышла извиняющейся."
                    me "Тогда увидимся."
                "Всегда рад":
                    "Я улыбнулся."
                    me "Если вдруг захочешь ещё как-нибудь сыграть, обращайся!"
            hide mi with dissolve
            "Мику кивнула и встала из-за стола."
        else:
            "Я улыбнулся."
            me "Всегда пожалуйста!"
            mi "Я пойду, ладно? Хочу увидеть, как ты будешь побеждать! Ты же будешь побеждать, правда? Я буду очень-очень за тебя болеть!"
            "Не в силах сдержать улыбку, я кивнул."
            me "Конечно же, буду."
            mi "Тогда удачи тебе дальше!"
            hide mi with dissolve
            "Она ушла."

# ====================================================== Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not alt_day2_detour_semifinal:
            "Не могу сказать, что пришлось потрудиться."
            "По мне, так это было чистое везение."
            "Хотя, конечно, моя карма и везение — это слова-антонимы."
            "Я — ходячее олицетворение закона Мэрфи."
            dreamgirl "Ну да, ну да. {w}А то, что ты вытянул билет даже не на миллион, а на новую жизнь, это мы в расчёт как бы не берём, да?"
            th "Ты о попадании в лагерь?"
            th "Я не могу назвать это везением в прямом смысле этого слова."
            dreamgirl "А как это ещё назвать?"
            th "Ну… Просто оказался в ненужном месте в ненужное время."
            dreamgirl "И получил полон рот молодости, лета и сексапильных пионерок."
            th "Знаешь, я не верю, когда много хорошо. {w}Обязательно где-то должен быть подвох."
            dreamgirl "И какой в этот раз?"
            th "Ну, например, может оказаться, что перенос в лагерь является побочным эффектом от попадания под луч космической энергии."
            th "Или вообще это спецслужбы тестировали прототип телепортатора, и у них что-то сбилось в настройках."
            dreamgirl "Не знаю, что ты употребляешь, но отсыпь немного."
            if alt_day2_dv_ultim == 1:
                dreamgirl "К тому же у тебя тут эротическое пари, помнишь?"
                if alt_result_dv_1_tour == 4:                                                                   # Дваче в другом полуфинале
                    th "Помню, помню."
                    th "Но у этого пари все шансы разрешиться совершенно самостоятельно."
                    dreamgirl "Надежды вьюношей питают…"
                    th "Не науки разве?"
                    dreamgirl "В твоём случае именно надежды."
                    dreamgirl "Будь уверен, она доберётся до тебя и порвёт на мелкие клочки, а потом исполнит свою угрозу."
                    th "О, спасибо тебе, мрачный зануда."
                elif alt_result_dv_1_tour == 3:                                                                 # Дваче в 1/2 к Семёну
                    th "Забудешь тут."
                    "Судя по графику, моим противником в полуфинале выступает как раз Двачевская."
                    dreamgirl "Вот свезло так свезло!"
                    dreamgirl "Давай сделаем ей больно!"
                elif alt_result_dv_1_tour == 2:                                                                 # Дваче слетела в 1 туре
                    "Это было бы даже смешно."
                    th "Пари? Какое пари?"
                    th "Пока мы тут о везении судачили, Алиску вышибли на первом же кону."
                    "Я снял воображаемую шапку и прижал её к груди."
                    me "Помянем!"
                    show dv angry pioneer2 far at left with dissolve
                    "Двачевская оскалилась, но ничего не сказала."

    elif alt_my_rival_1_tour.take == 'us':
        show us sad pioneer with dspr
        us "Так нельзя, я только разыгрываться начала!"
        me "Я тоже. {w}Ты проиграла, я победил. Всё честно."
        play music music_7dl["genki"] fadein 3
        us "Переиграем! Только ты теперь поддавайся, слышишь?"
        us "Я должна победить и забрать главный приз!"
        show us angry pioneer with dspr
        us "Ты должен проиграть! Должен! Понял!"
        "Ещё немного, и начну хохотать в голос, настолько потешно это выглядело."

# ====================================================== Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not alt_day2_detour_semifinal:
            if alt_day2_us_escape:
                us "Ах так! Да я тогда… Я тогда завтра снова сбегу, понял!"
                us "И чисти тогда свою картошку сам! На весь лагерь!"
                "А вот эта угроза была уже посерьёзнее, дежурить по столовой одному мне совершенно не улыбалось."
            else:
                us "Ах так! Тогда я всем расскажу про тебя и Двачевскую!"
                if (alt_day2_dv_ultim == 1) and (loki or herc):
                    me "Мелкая нахалка, не смей! Это только наш с ней спор, ты только разрубала!"
                    show us grin pioneer with dspr
                    "Ульяна только улыбнулась."
                else:
                    me "Ты всем расскажешь то, что она обещала рассказать? В случае моего проигрыша?"
                    "Она кивнула."
            if herc or loki:
                me "А тебе не надо горячего шоколада?"
                show us surp1 pioneer with dspr
                us "Что?"
                me "Я говорю, можешь делать как хочешь, но ты проиграла."
                show us dontlike pioneer with dspr
                me "А карточный долг священен. Всё, брысь отсюда, я к победе иду."
                "Она надулась, но сделала, как я сказал."
                hide us
                with flash_red
                "Правда, попутно наступила мне на ногу — пускай."
                stop music fadeout 3
                "Я был благодушен и простил ей эту маленькую шалость."
            if dr:
                me "Ладно"
                "Я вздохнул."
                me "Уговорила. Дам тебе ещё один шанс."
                show el serious pioneer at left with dissolve
                "Её крики привлекли внимание Электроника."
                el "Никаких переигровок!"
                el "Один матч, игра до двух побед, проигравший выбывает."
                "Ульяна кинула на Электроника недвусмысленный взгляд, означающий для него грядущие неприятности."
                stop music fadeout 3
                "Но хотя бы с меня внимание переключила, и я вздохнул с облегчением."
        else:
            me "Можешь делать как хочешь, но ты проиграла."
            me "А карточный долг священен. Всё, брысь отсюда, я к победе иду."
            "Она надулась, но сделала, как я сказал."
            hide us
            with flash_red
            "Правда, попутно наступила мне на ногу — пускай."
            stop music fadeout 3
            "Я был благодушен и простил ей эту маленькую шалость."
        play music music_list["my_daily_life"] fadein 5

    elif alt_my_rival_1_tour.take == 'sh':
        "Шурику не повезло."
        "Но, похоже, его больше интересовал сам процесс проверки новых правил и алгоритмов, чем победа."
        "Настоящий фанатик своего дела."
        show sh normal pioneer with dissolve
        sh "Ты очень хорошо умеешь приспособиться к новым правилам игры."
        "Похвалил он."
        hide sh with dissolve
        "И, пожав мне руку, удалился."


# ====================================================== Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not alt_day2_detour_semifinal:
            "Наверное, отправился изобретать очередную дикую штуку или строчить очерк об оной в стенгазету."
            "Я с удивлением поймал себя на мысли, что нахожу Шурика и Славю очень похожими."
            "Оба увлечены своим делом, оба дико ответственные."
            "И оба почти не отдыхают."
            th "Наверное, стоило бы сдать партию, я раздолбай, я и так способ ляжки потянуть найду, а он, похоже, сейчас уйдёт обратно сидеть в клуб."
            "Так и лето пройдёт, а он всё будет бледным."
            dreamgirl "Эй!"
            th "Что?"
            dreamgirl "Это у тебя там что за гадость? {w}Совесть? {w}Выброси её немедленно."
            dreamgirl "Вечно всякую дрянь с пола поднимаешь."
            if alt_day2_dv_ultim == 1:
                th "Что такое?"
                dreamgirl "Напоминаю, что мы не просто так тут штаны просиживаем."
                dreamgirl "У нас есть одна цель! Показать одной рыжей террористке, чего стоит слово!"
                if alt_result_dv_1_tour == 4:                                                           # Дваче в другом полуфинале
                    dreamgirl "И особый воспитательный момент несёт то, что мы умоем её в игре по её же правилам!"
                    th "Если она проиграет за другим столом, то никого мы не умоем."
                    dreamgirl "Есть подозрение, что такие, как она, так просто не сдаются."
                    th "Ну, если встретимся в финале, я её обыграю."
                    dreamgirl "С таким настроем ты никого не обыграешь. {w}Соберись!"
                elif alt_result_dv_1_tour == 3:                                                         # Дваче в 1/2 к Семёну
                    th "Ага, прямо сейчас и покажем."
                    dreamgirl "Здорово! Расправа оказалась куда ближе, чем мне казалось!"
                    if alt_day2_us_escape:
                        dreamgirl "Она просила сделать ей посопротивляться, исполни её просьбу."
                elif alt_result_dv_1_tour == 2:                                                         # Дваче слетела в 1 туре
                    "Заниматься оценками слов, честно говоря, было уже поздновато."
                    "Я посмотрел на таблицу участников — Алиса вылетела после первой же партии."
                    th "Не{w=.3} по{w=.2}вез{w=.3}ло."
                    th "Покойся с миром, дорогая бандитка."
                    th "Я отомщу за тебя."
            else:
                th "Что в этом плохого?"
                dreamgirl "То, что совесть рождает сомнения, а сомнения ведут к поражению."
                th "Я в курсе."
                th "Вот только нужна она мне — победа?"
                dreamgirl "Ты ещё начни лепетать чепуху про то, что «главное — участие»."
                "Фыркнул внутренний голос."
                th "Скажу — на всё воля Рандома."

    elif alt_my_rival_1_tour.take == 'mz':
        show mz normal glasses pioneer with dissolve
        "Реакция Жужи позабавила."
        mz "Аллилуйя!"
        show mz angry glasses pioneer far with dspr
        pause(0.5)
        hide mz with moveoutleft
        "Хлопнув по столу, она поднялась и исчезла."
        "Наверняка помчалась к своим лучшим друзьям — книгам."
        "Вот уж кому много не надо для счастья."

# ---------------------------------------------------- \\ Диалоги


# -------------------------------------------------------------------------
label alt_day2_1_tour_end:
# ЕСЛИ НЕ Славя, Мику или Шурик ИЛИ при скипе — итоги после диалогов
    if (alt_my_rival_1_tour.take not in ['sl','mi','sh']) or alt_day2_detour_semifinal:
        scene bg int_dining_hall_sunset with dissolve
        "Первый тур закончился."
        "Ситуация, между тем, складывалась следующая:"
        call alt_day2_1_tour_analizer                                                     # вызываем анализатор 1 тура
        $ renpy.block_rollback()                                                          # блокируем роллбак
    scene bg int_dining_hall_sunset with dissolve
    stop music fadeout 3
# -------------------------------------------------------------------------

    "Ладно, это всё лирика."
    jump alt_day2_semifinal_new                                             # переход в полуфинал

#-------------------------------------------------------------------------------------------------
label alt_day2_semifinal_new:
    stop music fadeout 1
    scene bg int_dining_hall_sunset with dissolve
    show el smile pioneer at left with dissolve
    play music music_list["get_to_know_me_better"] fadein 2
    el "Итак!"
    "Подал голос Электроник, явно гордящийся своей ролью мастер-церемониймейстера."
    el "Первый тур окончен, победители встречаются во втором туре!"

    $ alt_tournament_state = "semifinal_start"                                                      # устанавливаем начало полуфинала
#-------------------------------------------------------------------------------------------------
    if alt_day2_result_tour != 1:                                                                       # если не продули в 1 туре
        $ alt_day2_my_win = alt_day2_rival_win = alt_day2_game_played_out = 0                           # обнуляем результат игр
        $ alt_my_rival_semifinal = alt_get_me_rival(alt_day2_gamblers_semifinal)                        # узнаём своего соперника

        $ alt_name_my_rival_i = alt_my_rival_semifinal.name['i']                                        # узнаём ИМЯ своего соперника (в именительном падеже)
        $ alt_name_my_rival_r = alt_my_rival_semifinal.name['r']                                        # узнаём ИМЯ своего соперника (в родительном падеже)
        $ alt_name_my_rival_d = alt_my_rival_semifinal.name['d']                                        # узнаём ИМЯ своего соперника (в дательном падеже)
        $ alt_name_my_rival_v = alt_my_rival_semifinal.name['v']                                        # узнаём ИМЯ своего соперника (в винительном падеже)
        $ alt_name_my_rival_t = alt_my_rival_semifinal.name['t']                                        # узнаём ИМЯ своего соперника (в творительном падеже)

        $ alt_spr_my_rival = alt_my_rival_semifinal.take                                                # получаем спрайт соперника — заголовок
        $ alt_emo_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][0]                         # эмоция (строка)
        $ alt_acc_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][1]                         # аксессуар (строка)
        $ alt_clot_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][2]                        # одежда (строка)
        $ alt_pos_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][3]                         # положение

        $ alt_nick_my_rival = alt_my_rival_semifinal.nick                                               # получаем характер соперника (для диалога)

        if alt_my_rival_1_tour.take == 'un':
            hide el with dissolve
            "Лена скромно стояла в сторонке и следила за событиями турнира."
            show un smile2 pioneer far at right with dissolve
            "При этом на лице её не было ни злости, ни обиды, ни чего-либо в этом духе."
            "Напротив, она искренне поддерживала меня и остальных ребят."
            hide un with dissolve
            "Что ж, убедившись в том, что не обидел её, я немного расслабился."
    "Между тем, в таблице уже появились имена участников второго тура."
    call show_tournament_table                                                                      # "показали таблицу"
    $ alt_mstt = 0
    if alt_day2_result_tour != 1:                                                                       # если не продули в 1 туре
        $ places_my_table = alt_get_my_table(alt_day2_gamblers_semifinal)                               # Стол Семёна = [место Семёна, место соперника, № их стола]
    else:                                                                                               # продули в 1 туре
        $ alt_table_no = 5
    "И если верить этой таблице, то в полуфинале встречаются четыре игрока."
    $ alt_random_box_1 = range(1,len(alt_table_affiliation)+1)                                      # черный ящик — список от 1 до длины представлений столов +1
    while alt_table_no <= 6:                                                                        # перебираем столы от 5 по 6
        $ sitting_at_table,gambler_upper,gambler_lower,must_taunt = alt_declare_tournament_tables(alt_table_no)  #расссадка, игроки, таунты — по номеру стола
        "%(sitting_at_table)s"
        call show_tournament_table
        extend " %(gambler_upper)s"                                                                 # выводим в окно имя верхнего игрока
        call show_tournament_table
        extend " и %(gambler_lower)s."                                                              # выводим в окно имя нижего игрока
        if must_taunt != None:                                                                      # если таунт есть
            "%(must_taunt)s"                                                                        # выводим его
        if alt_day2_result_tour != 1:                                                                       # если не продули в 1 туре
            if alt_table_no != places_my_table[2]:                                                          # если номер стола — НЕ свой
                $ alt_day2_gamblers_semifinal[2*(alt_table_no-4)-renpy.random.choice([1,2])].winner = True  # тогда один из игроков (рандомно) — победитель в этапе
                $ renpy.block_rollback()
        $ alt_table_no += 1
    if (alt_day2_detour_number != 0):                                                               # если выбрали конкретного соперника для финала
        $ alt_day2_gamblers_semifinal[2].winner = False                                             # его соперник в полуфинале проигрывает
        $ alt_day2_gamblers_semifinal[3].winner = True                                              # а он сам выигрывает в полуфинале

    if alt_day2_result_tour == 1:                                                               # если продули в 1 туре
        scene bg int_dining_hall_sunset with joff_r
        $ alt_tournament_state = "semifinal_end"                                                # устанавливаем конец полуфинала
        $ alt_drawing_of_detour_semifinal()
        $ renpy.fix_rollback()                                                                  # фиксируем выбор — "откатом" поменять будет нельзя
        jump alt_day2_semifinal_detour                                                          # и переходим в конец проигрыша в 1/2

    pause (0.3)
    scene bg int_dining_hall_sunset with dissolve


# ---------------------------------------------------- ДИАЛОГИ
    if alt_my_rival_semifinal.take == 'un':
        show un shy pioneer with dspr
        me "Удачи нам обоим?"
        show un smile pioneer with dspr
        pause(.3)
        show un shy pioneer with dspr
        un "Д-да…"
        "Она попыталась улыбнуться, но тут же снова смешалась и смолкла."

    elif alt_my_rival_semifinal.take == 'sl':
        show sl smile pioneer with dspr
        sl "Ух! Не думала, что так далеко зайду!"
        "Улыбнулась Славя."
        me "Это не значит, что я теперь буду тебе поддаваться!"
        show sl laugh pioneer with dspr
        sl "И не надо!"
        "Рассмеялась девочка."
        sl "Пускай победит сильнейший!"

    elif alt_my_rival_semifinal.take == 'dv':
        "Ехидство и озорство во взгляде Алисы не сулило ничего хорошего для меня."
        show dv grin pioneer2 with dspr
        dv "Я придумала новое правило."
        "Прошептала она, наклонившись ко мне."
        me "Какое ещё правило?"
        dv "Если ты меня победишь сейчас, но проиграешь в финале — я всё равно всё всем расскажу."
        me "Эй, так нечестно!"
        show dv laugh pioneer2 with dspr
        dv "Хотя ты не победишь."
        "Рассмеялась девочка."
        dv "Тебе конец!"

    elif alt_my_rival_semifinal.take == 'mi':
        stop music fadeout 2
        show mi normal pioneer far with dissolve
        "Рандом послал мне в оппоненты Мику."
        play music music_7dl["tellyourworld"] fadein 3
        show mi normal pioneer with dspr
        "Пионерка заняла место напротив и спросила."
        show mi upset pioneer with dspr
        mi "Скажи, Сенечка, а какой у тебя размер?"
        "Я аж поперхнулся воздухом."
        dreamgirl "Ну, не стесняйся ты так! Девочка {b}хочет{/b} знать!"
        th "Это не те вещи, которые следует обсуждать на людях."
        dreamgirl "А где же ещё? Пионерке одиноко и тоскливо, она хочет тепла и ласки."
        th "Ты вообще о чём-нибудь другом думаешь?"
        dreamgirl "Думаю, конечно, но об этом интереснее!"
        me "Да я не…"
        show mi happy pioneer with dspr
        mi "Не знаешь? Не страшно. У меня в клубе есть всё необходимое."
        mi "Снимем мерки после турнира. А когда закончим, можем поиграть на гитарах!"
        if not ('music' in list_joined_clubs_7dl):
            show mi smile pioneer with dspr
            mi "Ты же умеешь играть, да?"
            show mi grin pioneer with dspr
            extend " Если нет, я тебя научу!"
        dreamgirl "Тебе однозначно понравится, соглашайся!"
        dreamgirl "Она аккуратно возьмёт в одну руку твой гриф, в другую каподастр…"
        dreamgirl "И поднимет голоску тональность!"
        show mi shocked pioneer with dspr
        mi "Ой, Сенечка, ты вдруг так покраснел. Тебе жарко? Или плохо? Может позвать ме…"
        show mi scared pioneer with dspr
        me "Не надо!" with vpunch
        "Замечательно. Испугал девушку и пустил петуха чуть-ли не на всю столовую."
        dreamgirl "Лох — это судьба."
        "Выдохнув, я попробовал ещё раз, уже спокойнее."
        show mi surprise pioneer with dspr
        me "Прости, что накричал. Со мной всё в порядке."
        show mi smile pioneer with dspr
        mi "Ничего страшного, Сенечка. Я всё понимаю."
        "Действительно ли понимаешь?"
        "Повезло, что Мику такая отходчивая."
        dreamgirl "Просто уточню — ты в самом деле собрался променять юное и мягкое на серое и унылое?"
        th "А сам как думаешь?"
        dreamgirl "Какой же ты…" # дегенерат, пиздец просто!
        me "Если найдёшь меня после турнира, схожу с тобой в клуб."
        show mi grin pioneer with dspr
        mi "Отлично! Ты будешь самым красивым на дискотеке!"
        "Дискотеке? А причём тут дискотека?"
        dreamgirl "Рубашку тебе пошить по размеру хотят, балбес."
        th "Почему сразу не сказал, Штирлиц?"
        dreamgirl "Был слишком далеко от провала."
        dreamgirl "Главное, сам не облажайся, когда будешь позировать для юной девы голышом."
        show mi smile pioneer with dspr
        stop music fadeout 2
        me "Кхм… Давай начнём игру уже."
        play music music_list["get_to_know_me_better"] fadein 3

    elif alt_my_rival_semifinal.take == 'us':
        stop music fadeout 2
        show us grin pioneer with dissolve
        us "Будешь поддаваться, будешь?"
        play music music_list["i_want_to_play"] fadein 1
        "С улыбкой до ушей она уставилась на меня."
        us "Я хочу всех победить!"
        if (alt_day2_dv_ultim == 1) and (loki or herc):
            me "Не буду."
            "Я отрицательно покачал головой."
            me "У нас же спор, помнишь?"
            if loki or herc:
                extend " Ты разбивала!"
            show us sad pioneer with dspr
            us "Спор — это да, но…"
            show us grin pioneer with dspr
        us "Играть будем по моим правилам!"
        me "Каким ещё правилам?!"
        us "Простым!"
        me "А-а-а! Очень информативно."
        us "А то!"
        show us laugh pioneer with dspr
        "Вдоволь насладившись моей кислой физиономией, Ульяна начала объяснять."
        show us smile pioneer with dspr
        us "Всё просто: ты отдаёшь мне хорошие карты, а я тебе — какие захочу."
        me "А мне с этого какая выгода?"
        us "Ты поможешь ребёнку выиграть и получишь…"
        show us normal pioneer with dspr
        "Ульяна задумалась."
        "Похоже есть не так много вещей, с которыми мелкая готова расстаться."
        us "Конфеты. Я дам тебе конфеты. " #(хочется написать «дружбу» или «и дружбу», но в дальнейшем это никак не проявит себя. Досадно.)
        me "Равноценный обмен…"
        show us grin pioneer with dspr
        us "Ну вот, рада, что мы пришли к кон…"
        show us calml pioneer with dspr
        extend " кансе…"
        show us angry pioneer with dspr
        extend " кунсекасу…"
        if herc:
            us "Что ты ржёшь?!"
            me "Тебе лучше не знать."
            us "А я хочу знать."
            us "Говори, новичок!"
            show us smile pioneer with dspr
            us "Или наутро проснёшься с муравьями под одеялом!"
            th "Внушительная угроза."
            me "Ладно, давай на ушко."
            show us grin pioneer close with dissolve
            us "То-то же!"
            "Ульянка подалась мне навстречу."
            "И когда между нами остались считанные сантиметры…"
            with hpunch
            show us surp2 pioneer with dspr
            us "Ай!"
            show us angry pioneer with dspr
            us "Ах ты!…"
            "Мелкая оказалась не промах: не растерялась и ударила лбом в лоб." with vpunch
            "Не сильно. Из этого положения у неё не вышло бы иначе."
            "Несколько секунд мы буравили другу друга взглядом."
            show us laugh pioneer with dspr
            "А потом оба не удержались и засмеялись."
            me "Ладно, давай играть уже, а то на нас вожатая косится."
            us "А муравьёв всё равно жди."
            th "Надеюсь, что она всё же шутит. Или забудет."
        else:
            me "Консенсусу."
            show us dontlike pioneer with dspr
            me "Не пытайся в сложные слова, рано тебе ещё."
            "И почему люди считают, что использование сложных слов делает их умнее в глазах других?"
            show us upset pioneer with dspr
            us "Бу-бу-бу. Вредина."
            me "Давай играть уже."

    elif alt_my_rival_semifinal.take == 'sh':
        show sh normal pioneer with dissolve
        sh "Это будет достойная схватка."
        "Кивнул он."
        me "Не думай, что я буду тебе поддаваться."
        show sh smile pioneer with dspr
        sh "И ты тоже не надейся!"
        me "Тогда к оружию!"

    elif alt_my_rival_semifinal.take == 'mz':
        "Серьёзно, как Жужа победить-то умудрилась, с таким отношением к игре?"
        show mz normal glasses pioneer with dissolve
        mz "Слушай. Как там тебя."
        "Начала она."
        me "Семён."
        mz "А, вот. Семён."
        mz "Семён, хочешь, я скажу, что ты победил, и пойду уже?"
        me "А так разве можно?"
        mt "Нет, нельзя! Играйте давайте!"
        "Крикнула со стороны болельщиков вожатая."
        show mz angry glasses pioneer with dspr
        "Чертыхнувшись, Женя отказалась от своих планов."
# ---------------------------------------------------- /ДИАЛОГИ

# ----------------------------------------------------------------------------------------------------
    if alt_day2_detour_semifinal:                                           # если пропуск полуфинала
        scene bg int_dining_hall_sunset with dissolve2
        pause(1.0)
        if not alt_day2_detour_final:                                       # Если НЕ пропуск финала
            jump alt_day2_semifinal_fail_end_new                            # на поражение в 1/2 финала
        elif alt_day2_detour_final:                                         # Если выбрано "проиграть в финале"
            jump alt_day2_semifinal_win_end_new                             # на победу в 1/2 финала

# ----------------------------------------------------------------------------------------------------
label alt_day2_semifinal_start_new:                                                     # начало полуфинала
    call alt_day2_stipulation_new                                                       # определяемся, кто первый ходит

    # первоначальные "настройки" игроков — могут меняться по результатам игры
    # 'defense' — защита, 'gamble' — риск, 'succumb' — слив, 'foolplay' — рандом
    # вероятность ошибки: 1 = 80%, …, 4 = 20%, 5 — ошибок нет.

    if alt_my_rival_semifinal.take == 'un':                                                    # Лена
        if alt_day2_dv_ultim != 1:                                                              # если с Алисой не спорить
            $ alt_day2_gambler_behavior = 'gamble'                                              # пытается рискнуть
            $ alt_day2_gambler_skill = 3                                                        # правда, ошибок многовато — 40%(3)
        else:
            $ alt_day2_gambler_behavior = 'succumb'                                             # Если поспорить — то также игра в поддавки
            $ alt_day2_gambler_skill = 4                                                        # может ошибиться  — 20%(4)
    elif alt_my_rival_semifinal.take == 'sl':                                                  # Славя будет защищаться, ошибок — 20%(4)
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_semifinal.take == 'dv':                                                  # Алиса рискует, ошибок — 20%(4)
        $ alt_day2_gambler_behavior = 'gamble'
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_semifinal.take == 'mi':                                                  # Мику будет защищаться, ошибок — 20%(4)
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_semifinal.take == 'us':                                                  # Ульяна будет защищаться по-своему
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 3                                                            # ошибок — 40%(3)
    elif alt_my_rival_semifinal.take == 'sh':                                                   # Шурик экспериментирует, так что может и рискнуть, и защищаться, и слить; ошибки 20%(4)
        $ alt_day2_gambler_behavior = renpy.random.choice(['defense', 'gamble'])                # у него своя кухня — набор из возможных вариантов
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_semifinal.take == 'mz':                                                  # Женя играет рандомно, как в классике, ошибки = 5
        $ alt_day2_gambler_behavior = 'foolplay'
        $ alt_day2_gambler_skill = 5

label alt_day2_semifinal_re_game:                                                           # игра в полуфинале — сюда возвращаемся на повторную игру
    $ alt_my_poker_hand = None
    $ alt_rival_poker_hand = None

    if alt_day2_walk == 1:
        $ VISIBLE = True
        $ INVISIBLE = True
    else:
        $ VISIBLE = True
        $ INVISIBLE = False

    python:
        dialogs = {
                        (0, 'win','jump'):'alt_day2_one_play_win_new',
                        (0, 'fail','jump'):'alt_day2_one_play_fail_new',
                        (0, 'draw','jump'):'alt_day2_one_play_draw_new'
                    }
        generate_cards_alt('bg hall', dialogs)


# ****************   НОВЫЕ  СОПЕРНИКИ   ******************************************

        if alt_my_rival_semifinal.take == 'un':
            rival = CardGameRivalWiseUsual(un_avatar_set, u"Лена", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_semifinal.take == 'sl':
            rival = CardGameRivalWiseUsual(sl_avatar_set, u"Славя", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_semifinal.take == 'dv':
            rival = CardGameRivalWiseUsual(dv_avatar_set, u"Алиса", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_semifinal.take == 'mi':
            rival = CardGameRivalWiseUsual(mi_avatar_set, u"Мику", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_semifinal.take == 'us':
            rival = CardGameRivalWiseLikeUS(us_avatar_set, u"Ульяна", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_semifinal.take == 'sh':
            rival = CardGameRivalWiseUsual(sh_avatar_set, u"Шурик", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_semifinal.take == 'mz':
            rival = CardGameRivalWiseUsual(mz_avatar_set, u"Женя", alt_day2_gambler_behavior, alt_day2_gambler_skill)

# ************************************************************************************

    $ alt_hint_poker = alt_hint_poker_contractual                                           # подсказки комбинаций — по просмору правил
    jump cards_gameloop_wise_alt                                                            # переход карточный стол

#-------------------------------------------------------------------------------------------------
label alt_day2_semifinal_fail_end_new:
    $ alt_day2_result_tour = 11                                                 # Семён проиграл в полуфинале
    $ persistent.altCardsWon1_new = True

    $ alt_day2_gamblers_semifinal[places_my_table[1]].winner = True            # соперник выиграл
    $ alt_rival_final = alt_day2_gamblers_semifinal[places_my_table[1]]         # и он выходит в финал
    $ alt_day2_gamblers_semifinal[places_my_table[0]].winner = False            # Семён проиграл
    $ alt_tournament_state = "semifinal_end"                                   # устанавливаем конец полуфинала
    scene bg int_dining_hall_sunset with dissolve
    call alt_day2_summary_poker_round

# ---------------------------------------------------- ДИАЛОГИ;
    if alt_my_rival_semifinal.take == 'un':
        $ lp_un += 1
        stop music fadeout 2
        if alt_day2_dv_ultim == 1:
            show un serious pioneer at center with dissolve
            un "И зачем ты это сделал?"
            play music music_7dl["areyouabully"] fadein 3
            "Спросила она, смотря на меня с явно выраженной неприязнью."
            me "Извини?"
            un "Думаешь, я не слышала о вашем с Алисой маленьком «пари»?"
            un "Так и выигрывал бы!"
            if alt_day2_walk == 1:
                th "Да я и планировал. Даже карты пометил. Но…"
            th "Как-то не срослось."
            me "Да что теперь-то говорить? Я проиграл, ты победила. Удачного вечера."
            "Тем более, что мы не ведём переговоров с террористами."
        else:
            show un angry pioneer with dissolve
            un "Ты поддался, да?"
            play music music_7dl["areyouabully"] fadein 3
            "Лена наклонила голову набок и сверлила меня неприязненным взглядом."
            un "Вместо того, чтобы нормально играть, ты устроил поддавки."
            me "Тебе показалось."
            "Усмехнулся я."
        un "Прошу разрешить нам сыграть ещё раз!"
        "В наступившей тишине попросила Лена."
        un "Мой соперник поддавался."
        show dv grin pioneer2 far at fleft with dissolve
        dv "Поддавался — значит, сам дурак."
        "Фыркнула Алиса."
        "Ну да, она-то знает, что на кону."
        show un angry2 pioneer with dspr
        un "А ты бы вообще молчала! Это всё из-за тебя! Снова!"
        stop music fadeout 3
        show un sad pioneer with dspr
        "Она спрятала лицо в ладонях, а я поднялся из-за стола, чувствуя себя ракетной ступенью, что вывела на орбиту очередной шаттл."
        hide dv
        hide un
        with dissolve
        pause(0.3)
        play music music_list["get_to_know_me_better"] fadein 1

    elif alt_my_rival_semifinal.take == 'sl':
        show sl normal pioneer with dissolve
        sl "И снова меня заставляют заниматься непонятными вещами."
        me "Прости?"
        th "Заговаривается, что ли?"
        show sl serious pioneer with dspr
        "Славя отмахнулась."
        sl "Не обращай внимания, просто мысли вслух."
        me "Ясно. Что ж, тогда удачи тебе в финале!"
        sl "Точно."
        show sl sad pioneer with dissolve
        sl "Зачем я вообще играть согласилась?"
        me "Не любишь карты?"
        sl "Нет. Я другие игры люблю."
        "Она сморщилась, будто съела нечто кислое."
        "А я поднялся — меня ждала волнительная роль болельщика за финалистов."

    elif alt_my_rival_semifinal.take == 'dv':
        if alt_day2_dv_ultim == 1:
            show dv grin pioneer2 with dspr
            dv "Как думаешь, будет лучше, если я сама с трибуны объявлю?"
            "Алиса злорадствовала так, будто я был её кровный враг с традициями пяти колен."
            dv "Или лучше вытащить тебя на трибуну вместе с собой?"
            if alt_day2_walk == 1:
                th "Лучше объясни мне, откуда ты знаешь {i}мой собственный{/i} крап."
            me "Не получится."
            show dv surprise pioneer2 with dspr
            dv "Почему?"
            me "Потому что, если ты вытащишь меня на трибуны, никто в жизни не поверит, что мне хватило сил справиться с тобой и — что ты там говорила?"
            show dv laugh pioneer2 with dspr
            dv "Да. Ну…"
            "Ей пришла в голову мысль."
            dv "Я скажу, что ты меня связал."
            me "Колготками!"
        "Алиса весело расхохоталась, а я поднялся."
        "Господи, почему все стервы такие рыжие?"
        "Неужели у меня где-то написано «издеваться сюда»?"
        me "Играй. Тебя финал ждёт."
        me "А если проиграешь, то стыд тебе и позор."
        "Развернулся и ушёл к болельщикам."

    elif alt_my_rival_semifinal.take == 'mi':
        show mi happy pioneer with dspr
        mi "Ура! Я снова побеждаю!"
        mi "Да я, да я… Я супер-Мику!"
        me "О господи, где вы откопали это чудо?"
        "Пробормотал я."
        show mi smile pioneer with dspr
        mi "Я хочу отметить свою победу каким-нибудь очень хорошим делом или даже поступком, но мне что-то ничего в голову не приходит, может быть, ты, Сенечка, что-нибудь посоветуешь?"
        "Человек-пулемёт."
        th "Временами нами неминуемо на кон были выкинуты карты, да масти не те…"
        th "Солнышко, милая, ну хватит уже трещать, я же ничего плохого не сделал тебе, за что ты меня тут расстреливаешь!"
        me "Не знаю."
        "Угрюмо ответил я."
        "Поражение меня несколько подкосило."
        show mi happy pioneer with dspr
        mi "Ой, а я знаю, кажется! Да! Мне только что идея в голову пришла! Я…"
        show mi happy pioneer far with dissolve
        "Она забралась на стол."
        mi "Я вам спою!"
        "Она набрала в грудь воздуха, и…"
        show dv angry pioneer2 at cleft with easeinleft
        show mt angry pioneer at cright with easeinright
        with vpunch
        "Неизвестно откуда взявшиеся Ольга и Алиса, взревев в унисон, ринулись стаскивать её на пол."
        "Усмехнувшись, я встал из-за стола и отошёл к болельщикам."

    elif alt_my_rival_semifinal.take == 'us':
        if (alt_day2_dv_ultim == 1) and (loki or herc):
            show us laugh pioneer with dissolve
            us "Ура-ура-ура, прекрасная игра! Красив я и умён, и ловок, и силён!"
            "Прокричала она."
            me "Ты ещё фляк сделай от радости."
            th "Почему ей так нравится факт, что теперь меня освистают на весь лагерь?"
            me "Не знал, что твоим кумиром является Винни Пух со своими кричалками."
            us "А как же!"
            if alt_day2_us_escape:
                us "У меня и медведь есть!"
                "Она показала язык."
                us "Но не узнать лучшее в мире приведение… стыд и срам!"
        hide us with dissolve
        "Я поморщился и встал."
        us "Неудачникам привет."
        "Крикнула она мне в спину."
        "А я не среагировал. Привык."

    elif alt_my_rival_semifinal.take == 'sh':
        show sh normal pioneer with dissolve
        sh "Жаль, что так быстро всё закончилось."
        "С достоинством кивнул Шурик."
        sh "Идеально, если бы нам дали партий десять с одной колоды, чтобы можно было вычислить логику."
        me "И сидеть до утра?"
        me "Я-то не против, да кто ж нам позволит."
        "Я кивнул и поднялся из-за стола."

    elif alt_my_rival_semifinal.take == 'mz':
        show mz normal glasses pioneer with dissolve
        mz "Упс."
        "Пробормотала она себе под нос."
        mz "Специально же карты не открывала. Здесь вообще как-нибудь проиграть возможно?"
        me "Как видишь."
        "Сказал я и встал из-за стола."
# ---------------------------------------------------- \\ Диалоги

label alt_day2_semifinal_detour:
    pause(.5)
    scene bg int_dining_hall_sunset with dissolve
    "В полуфинале был такой расклад:"
#-------------------------------------------------------------------------------------------------
    call alt_day2_semifinal_analizer                                                  # анализ полуфинала
    $ renpy.block_rollback()                                                          # блокируем роллбак
    jump alt_day2_final_new                                 # и смотрим финал

#-------------------------------------------------------------------------------------------------
label alt_day2_semifinal_win_end_new:
    $ alt_day2_result_tour = 12                                             # Семён выиграл в полуфинале
    if not alt_day2_detour_final:                                           # если не "выигрыш" в полуфинале скипом
        $ persistent.altCardsWonRivals_new[alt_spr_my_rival] = True         # Выиграли у этого соперника

    $ persistent.altCardsWon2_new = True
    $ alt_day2_gamblers_semifinal[places_my_table[0]].winner = True             # Семён выиграл
    $ alt_rival_final = alt_day2_gamblers_semifinal[places_my_table[0]]         # и он выходит в финал
    $ alt_day2_gamblers_semifinal[places_my_table[1]].winner = False            # Соперник проиграл
    $ alt_tournament_state = "semifinal_end"                                    # устанавливаем конец полуфинала
    scene bg int_dining_hall_sunset with dissolve
    call alt_day2_summary_poker_round

# ---------------------------------------------------- ДИАЛОГИ
    if alt_my_rival_semifinal.take == 'un':
        stop music fadeout 2
        "Лена старалась изо всех сил."
        play music music_list["lets_be_friends"]
        "Видно было, что ей понравилось то, как её восприняли всерьёз."
        "Жаль только, что иногда даже старания изо всех сил решительно недостаточно."
        show un sad pioneer with dissolve
        un "Досадно. У меня почти получилось."
        "Вот они злобятся, и кричат, и ножками мотылькают, и невдомёк им, почему окружающим так смешно."
        me "Хочешь реванш?"
        show un normal pioneer with dspr
        un "Нееет, реванш — это не то."
        "Вздохнула она."
        if alt_day2_walk == 1:
            th "Это ничего, знала бы ты, за счёт чего я тебя обыграл…"
        me "То есть всё нормально?"
        "Она кивнула."
        "Что она ещё могла сделать?"
        th "А она азартная."
        "Отметил я для себя."
        th "То есть, в случае чего, её можно взять на слаб{b}о{/b}?"
        "Кого-то она мне напомнила этой своей импульсивностью."
        "И когда я понял кого именно, то долго тряс головой, отгоняя глупые мысли."
        show un shy pioneer with dspr
        un "Почему ты смотришь так странно?"
        th "Да нет, быть не может."
        "Это просто я надышался запахов из столовой, и меня разбирает галлюцинациями."
        show un shocked pioneer with dspr
        me "Двачевскую!"
        "Алиса покосилась на меня — мол, кто поминает имя моё всуе — но промолчала."
        hide un with dissolve
        "А я, не объясняя ничего больше, отправился за стол местных небожителей."
        stop music fadeout 2
        th "Меня ждёт финал!"
        "Ребята за соседними столами тоже время даром не теряли."
        play music music_list["get_to_know_me_better"] fadein 2

    elif alt_my_rival_semifinal.take == 'sl':
        show sl smile2 pioneer with dspr
        "Славя тихонько вздохнула и улыбнулась."
        "Я не очень понимал, чем вызвана её позитивная реакция, но обрадовался, что не обидел своей победой девушку."
        show sl normal pioneer with dspr
        "Она легко поднялась со стула и кивнула мне:"
        sl "Не успел приехать, а уже первое место занял."
        sl "Так вот и становятся легендами!"
        me "Так я же ещё ничего не занимал…"
        show sl laugh pioneer with dspr
        sl "Только не говори мне, что ты не нацелен на победу!"
        hide sl with dissolve
        "Она отошла к болельщикам."
        "А я пошёл к столу финалистов, между делом оценивая получившуюся ситуацию."

    elif alt_my_rival_semifinal.take == 'dv':
        show dv surprise pioneer2 with dissolve
        $ lp_dv += 1
        if herc or loki:
            play music music_list["that_s_our_madhouse"] fadein 3
        else:
            play music music_list["glimmering_coals"] fadein 3
        th "Итак, Гагарин долетался, Пушкин дописался."
        th "Выиграл!!!"
        show dv sad pioneer2 with dspr
        th "А рыжая облажалась."
        "Я поднялся из-за стола и бросил пренебрежительный взгляд на несчастную Алису."
        "Кажется, она чувствовала себя совершенно не в своей тарелке."
        "Теперь мой путь лежит к горним высям, где мне оппонентами выступят сами боги!"
        th "А не всякие самодовольные гадины, считающие, что меня можно запугать или запутать."
        if herc or loki:
            "Я подмигнул Двачевской."
            me "Поздравляю!"
            dv "Что?"
            me "С позорным поражением тебя!"
            $ lp_dv += 1
            show dv rage pioneer2 with dspr
            "По-моему, она меня всё-таки обругала матом."
            "Не могу сказать — её перекосило так, что я расхохотался."
            th "Ладно, на сегодня с неё хватит."
        else:
            "Я молча встал и направился к столу финалистов."
            "У меня нет времени на детсадовскую возню с неудачниками."
        "Я пошёл к столу финалистов, между делом оценивая текущую ситуацию."

    elif alt_my_rival_semifinal.take == 'mi':
        show mi sad pioneer with dspr
        "Мику однозначно расстроилась из-за проигрыша."
        "Похоже, она начала худо-бедно разбираться в правилах — и тут на тебе."
        "Humiliating Defeat."
        "Наткнулась на меня."

        show mi serious pioneer with dspr
        mi "В следующий раз победа будет моя!"

        show mi serious pioneer far with dspr
        show mi serious pioneer far at left with move
        hide mi with moveoutleft

        "Она вздёрнула нос к потолку и, поднявшись, гордо удалилась, занимая место среди проигравших."

        show mi grin pioneer far at fleft with moveinleft
        "Правда, немного подпортила картинку, обернувшись и показав мне язык."

        show mi smile pioneer far with dspr
        pause(0.3)
        hide mi with moveoutleft

        "Культурный человек, наследие эпохи…"
        me "Спасибо за игру!"
        "Ребята за соседними столами тоже время даром не теряли."
        "Игра сложилась весьма занятно."

    elif alt_my_rival_semifinal.take == 'us':
        show us dontlike pioneer with dissolve
        "Выиграть у Ульяны оказалось легче, чем…"
        "Чем пережить последствия этой победы…"
        play music music_list["awakening_power"] fadein 1
        show us angry pioneer with dspr
        pause(0.3)
        "Потому что она вдруг перегнулась через стол и принялась колотить меня своими маленькими кулачками."
        "И довольно сильно!" with vpunch
        us "Ты ведь обещал проиграть!" with hpunch
        "Она была так обижена, будто я её предал!"
        us "Обещал! Я ведь тебя просила!" with vpunch
        "Интересно, она понимает, что только что призналась в жульничестве?" with hpunch
        if alt_day2_walk == 1:
            th "Впрочем, я и сам жульничал, но…"
        me "Ничего я не обещал!"
        "С трудом, но мне удалось вставить пару слов в перерыве между ударами…"
        "И мне было не ясно только одно…"
        th "Почему меня никто не спасает?!!" with vpunch
        th "Где Ольга Дмитриевна, когда она так нужна?!" with hpunch
        "Но, кажется, всем было настолько весело наблюдать, как меня убивают, что никто и не думал прекращать развлечение…"
        stop music fadeout 6
        "Наконец поставив сотый синяк на моих руках и голове, Ульяна немного запыхалась и перестала меня бить." with vpunch
        show us dontlike pioneer with dspr
        "Но она всё ещё была недовольна…"
        play music music_list["i_want_to_play"] fadein 2
        "И это ещё мягко сказано…"
        show us angry pioneer with dspr
        us "У-у-у!"
        "Она свирепо топнула ножкой." with vpunch
        us "Ладно-ладно!"
        us "Я это тебе ещё припомню."
        hide us with moveoutleft
        "И с этими словами она резко развернулась и пошла в зал."
        "У меня появилась пара минут на то, чтобы привести себя в порядок и уточнить ситуацию в плей-офф."

    elif alt_my_rival_semifinal.take == 'sh':
        show sh normal pioneer with dissolve
        "Шурик кивнул мне и поднялся."
        "Не знаю, впечатлил его мой навык игры, в которую я играю сегодня первый раз в жизни, или нет."
        "Так или иначе, он достаточно равнодушно отнёсся к поражению."
        if not ('cyber' in list_joined_clubs_7dl) and ('cyber' in list_voyage_7dl):
            show sh smile pioneer with dspr
            sh "Насчёт клуба кибернетиков, если вдруг что…"
            "Я кивнул."
        hide sh with dissolve
        if not ('cyber' in list_joined_clubs_7dl) and ('cyber' in list_voyage_7dl):
            "Но давайте насчёт кибернетики позже, а пока посмотрим, что там у других пионеров творится."
        else:
            "А я покамест решил посмотреть, что там у других пионеров творится."

    elif alt_my_rival_semifinal.take == 'mz':
        show mz normal glasses pioneer with dissolve
        "Реакция Жужи меня позабавила."
        "Сначала она бросила карты на стол и спрятала лицо в ладонях."
        "А затем вскинула руки вверх и рявкнула:"
        show mz laugh glasses pioneer with dspr
        mz "Аллилуйя!" with vpunch

        show mz normal glasses pioneer far with dissolve
        pause(0.25)
        show mz normal glasses pioneer far at fleft with move
        hide mz with moveoutleft

        "После чего телепортировалась из столовой."
        "А я же решил узнать, как там дела у соседей."
# ---------------------------------------------------- \\ Диалоги

#-------------------------------------------------------------------------------------------------
    pause(.5)
    call alt_day2_semifinal_analizer                                    # анализ полуфинала
    $ renpy.block_rollback()                                                          # блокируем роллбак
#-------------------------------------------------------------------------------------------------
label alt_day2_final_new:
    $ alt_day2_my_win = alt_day2_rival_win = alt_day2_game_played_out = 0                       # обнуляем результат игр
    $ alt_tournament_state = "final_start"                                                      # устанавливаем начало финала
    if alt_day2_result_tour == 1:                                                               # Если продул в 1 туре
        $ alt_drawing_of_detour_final()                                                         # вызываем рандомизатор
        $ renpy.fix_rollback()                                                                  # фиксируем выбор — "откатом" поменять будет нельзя
# -----------------------------------------------------------------------
    $ alt_my_rival_final, alt_index_rival_final = alt_get_me_rival_final(alt_day2_gamblers_final,alt_rival_final)      # узнаём второго соперника в финале и его индекс  в рассадке

    $ alt_name_my_rival_i = alt_my_rival_final.name['i']                                   # узнаём ИМЯ второго финалиста (в именительном падеже)
    $ alt_name_my_rival_r = alt_my_rival_final.name['r']                                   # узнаём ИМЯ второго финалиста (в родительном падеже)
    $ alt_name_my_rival_d = alt_my_rival_final.name['d']                                   # узнаём ИМЯ второго финалиста (в дательном падеже)
    $ alt_name_my_rival_v = alt_my_rival_final.name['v']                                   # узнаём ИМЯ второго финалиста (в винительном падеже)
    $ alt_name_my_rival_t = alt_my_rival_final.name['t']                                   # узнаём ИМЯ второго финалиста (в творительном падеже)

    $ alt_spr_my_rival = alt_my_rival_final.take                                                # получаем спрайт соперника — заголовок
    $ alt_emo_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][0]                     # эмоция (строка)
    $ alt_acc_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][1]                     # аксессуар (строка)
    $ alt_clot_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][2]                    # одежда (строка)
    $ alt_pos_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][3]                     # положение

    $ alt_nick_my_rival = alt_my_rival_final.nick                                               # получаем характер соперника (для диалога)
# -----------------------------------------------------------------------

    # ================================================ пересаживаемся за финальный стол.
    show el smile pioneer at left with dissolve
    el "Полуфиналы завершены, победители встречаются в финале!"
    hide el with dissolve
    $ alt_mstt = 2
    call show_tournament_table                                                                  # показать таблицу — итоги полуфинала
# ----------------------------------------------------------------------------------------------------
label alt_day2_final_choice_new:
    if alt_rival_final.take == 'me':                                                            # Семён прошел в финал
        "Я уверенно двигаюсь к победе, следующая моя жертва уже видна на горизонте."

# ---------------------------------------------------- ДИАЛОГИ
        if alt_my_rival_final.take == 'un':
            "Прости, Лена. Ничего личного."
        elif alt_my_rival_final.take == 'sl':
            "Славя. Ну, она всё равно без души играет, так что я ей только доброе дело сделаю."
        elif alt_my_rival_final.take == 'dv':
            "Алиса, ага."
            me "Алиса, а Алиса."
            dv "Чего?"
            me "Тебе конец."
            "Она расхохоталась."
        elif alt_my_rival_final.take == 'mi':
            "Мику."
            "Как галантный парень я склонен сдать эту партию, чтобы сделать девушке приятное."
            "Но как игрок я чувствую запах победы, поэтому никакой пощады!"
        elif alt_my_rival_final.take == 'us':
            "Мелкая? Блин, кто-нибудь, объясните мне внятно: какого чёрта это мелкое недоразумение забыло в финале?"
        elif alt_my_rival_final.take == 'sh':
            "Шурик? Хм. Это будет интересный бой."
        elif alt_my_rival_final.take == 'mz':
            "Жужелица."
            "Может быть, и скрипит о том, что играть не хочет, но — блин, она же в финале!"
            "Придётся потрудиться."
# ---------------------------------------------------- /ДИАЛОГИ

        if alt_day2_detour_final:                                                                  # если пропуск финала
            scene bg int_dining_hall_sunset with dissolve2
            pause(1.0)
            if not alt_day2_tournament_fast_win:                                                   # Если НЕ победа в финале
                $ alt_day2_result_tour = 21                                                         # Семён проиграл в финале
                "Похоже, у меня не было ни шанса."
                call alt_day2_summary_poker_round
                jump alt_day2_final_fail_end_new                                                    # на поражение в финале
            elif alt_day2_tournament_fast_win:                                                      # если победа в финале
                $ alt_day2_result_tour = 22                                                         # Семён выиграл в финале
                call alt_day2_summary_poker_round
                jump alt_day2_final_win_end_new                                                    # на победу в финале

        jump alt_day2_final_start_new                                                              # играем финал
# ----------------------------------------------------------------------------------------------------
    else:                                                                                      # Семён продул в 1/2
        $ alt_name_rival_final = alt_rival_final.name['i']                                     # Получаем имя финалиста — кому Семён проиграл
        if alt_day2_result_tour == 1:                                                           # Если продул в 1 туре
            if alt_rival_final.take == alt_my_rival_1_tour.take:                                # соперник в 1 туре и финале тот же
                "В финал выходит мой соперник в первом коне — %(alt_name_rival_final)s{nw}"
            else:
                if alt_my_rival_1_tour.take == 'sh':
                    "Шурик, мой удачливый соперник, в полуфинале проиграл."
                else:
                    $ alt_name_rival_1_tour = alt_my_rival_1_tour.name['i']
                    "%(alt_name_rival_1_tour)s, отправившая меня в компанию болельщиков, сама проиграла в полуфинале."
                "А в финал выходит %(alt_name_rival_final)s{nw}"
        else:
            "Так как я сдулся и проиграл, в финал отправляется %(alt_name_rival_final)s{nw}"
        extend ", где встретит{nw}"
# ---------------------------------------------------
        if alt_my_rival_semifinal == None:                                                                        # Если каким-то образом второй финалист не назначен (может быть и такое)
            $ alt_my_rival_semifinal = alt_day2_gamblers_final[1-alt_day2_gamblers_final.index(alt_rival_final)]  # Это НЕ тот, кому Семён проиграл
# ---------------------------------------------------

# ---------------------------------------------------- ДИАЛОГИ
        if alt_my_rival_final.take == 'un':
            extend " Лену и попытается обыграть её."
        elif alt_my_rival_final.take == 'sl':
            extend " Славю и докажет всем, что блондинка — это диагноз."
        elif alt_my_rival_final.take == 'dv':
            if alt_rival_final.take == 'us':
                extend "… Алису? Так они с самого начала это планировали?!"
            else:
                extend " Алису и попробует уцелеть в этой схватке."
        elif alt_my_rival_final.take == 'mi':
            extend " Мику. {w}Не думаю, что там будет много проблем. Хотя японка и добралась до финала."
        elif alt_my_rival_final.take == 'us':
            if alt_rival_final.take == 'dv':
                extend " Ульянку."
                "Смешно, но, похоже, рыжие в самом деле попросту разметали этот турнир по брёвнышку, как и хотели."
            else:
                extend " Ульяну и попробует выжить после встречи с ней."
        elif alt_my_rival_final.take == 'sh':
            extend " Шурика и попробует доказать, что мозги в карточной игре не решают."
        elif alt_my_rival_final.take == 'mz':
            extend " Женю."
            "Что ещё можно про сказать про оппонентку Ульянки?"
            "Во. Жужелица."
# ---------------------------------------------------- /ДИАЛОГИ
        scene bg int_dining_hall_sunset with joff_r
        $ alt_day2_gamblers_final[renpy.random.choice([0,1])].winner = True                                    #  один из игроков (рандомно) — победитель в финале
        $ alt_tournament_state = "final_end"
        call alt_day2_final_analizer

        if (alt_day2_dv_ultim == 1):
            "Что ж, теперь можно подвести итоги."
            "Спор я закономерно продул — с моей удачей надеяться было глупо. Задним умом теперь уж я понял, нужно было заранее узнать, во что мы будем играть."
            th "Это же не игра, а простое подбрасывание монетки! Случайно раздали карты, случайно выбираешь, какую из них забрать у противника."
            if (alt_day2_walk == 1) and (alt_my_rival_final.take != 'dv'):
                dreamgirl "Да ты же карты пометил, дубина! Как ты вообще с таким раскладом умудрился продуть?!"
                th "Критический промах."
            else:
                "В общем, в поражении я не виноват. Вот."
        $ renpy.block_rollback()                                                                                # блокируем роллбак
        stop music fadeout 2
        jump alt_day2_prepare_transition_to_supper
# ------------------------------------------------------------------------------------------------------------------------------

label alt_day2_final_start_new:
    call alt_day2_checking_scores
    call alt_day2_stipulation_new                                                       # определяемся, кто первый ходит
# ----------------------------------------------------------------------------
    # первоначальные "настройки" игроков — могут меняться по результатам игры
    # 'defense' — защита, 'gamble' — риск, 'succumb' — слив, 'foolplay' — рандом
    # вероятность ошибки: 1 = 80%, …, 4 = 20%, 5 — ошибок нет.
    if alt_my_rival_final.take == 'un':                                                    # Добрались сюда — так что нефиг, Лена защищается
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 4                                                       # ошибки, правда, есть — 20%(4)
    elif alt_my_rival_final.take == 'sl':                                                  # Славя будет защищаться, может ошибиться — 20%(4)
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_final.take == 'dv':                                                  # Алиса рискует, вероятность ошибки 20%
        $ alt_day2_gambler_behavior = 'gamble'
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_final.take == 'mi':                                                  # Мику будет защищаться, может ошибиться — 20%(4)
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_final.take == 'us':                                                  # Ульяна к финалу научилась играть и будет защищаться, но с ошибками 40% (3)
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 3                                                       # ошибок — 40%(3)
    elif alt_my_rival_final.take == 'sh':                                                  # Шурик экспериментирует по-прежнему, вероятность ошибки 20%
        $ alt_day2_gambler_behavior = renpy.random.choice(['defense', 'gamble'])           # у него своя кухня — набор из возможных вариантов
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_final.take == 'mz':                                                  # Женя играет рандомно, как в классике, вероятность ошибки 20%
        $ alt_day2_gambler_behavior = 'foolplay'
        $ alt_day2_gambler_skill = 4
# ----------------------------------------------------------------------------

    if alt_day2_walk == 1:
        $ VISIBLE = True
        $ INVISIBLE = True
    else:
        $ VISIBLE = True
        $ INVISIBLE = False

# ------------------------------------------------------------------------------------------------------------------------------
# Палим Семёна с крапом карт
    if alt_day2_walk == 1 and INVISIBLE:                                    # Если Сёма мухлевал И ЕГО ещё не поймали, его таки в финале МОГУТ спалить
        if alt_my_rival_final.take == 'dv':                               # палит Алиса
            "Но прежде, чем всё началось, Алиса с подозрением оглядела карты, которыми мы играли."
            th "Неужели…"
            "По спине пробежал холодок…"
            "А она слегка перегнулась через стол и, лукаво улыбаясь, спросила шёпотом — так, что слышать её мог только я…"
            show dv smile pioneer2 with dissolve
            dv "Так ты все карты пометил, да?"
            dv "Предусмотрительный…"
            th "Она знала, что я жульничал!!!"
            "Я покраснел."
            th "Если сейчас она встанет и скажет всем…"
            th "Это будет ужасно!!!"
            th "Невыносимо!!!"
            th "Кошмарно!!!"
            "Но Алиса, кажется, и не думала выдавать меня…"
            "Она улыбалась!"
            dv "Надеялся и меня так обыграть?"
            "И я, проклиная свою честность, тоже шёпотом, ответил:"
            me "Да…"
            "Она фыркнула, впрочем, совсем беззлобно."
            dv "Даже не мечтай…"
            "Незаметно для зрителей она достала из кармана совершенно новую колоду карт и поменяла её местами с помеченной мной…"
            dv "Играть будем моими!"
            show dv laugh pioneer2 with dissolve
            "Она довольно улыбнулась."
            dv "Я тоже предусмотрительная…"
            "Игра началась."
            $ INVISIBLE = False
# ------------------------------------------------------------------------------------------------------------------------------

label alt_day2_final_re_game:                                                           # игра в финале — сюда возвращаемся на повторную игру
    $ alt_my_poker_hand = None
    $ alt_rival_poker_hand = None

    python:
        dialogs = {
                        (0, 'win','jump'):'alt_day2_one_play_win_new',
                        (0, 'fail','jump'):'alt_day2_one_play_fail_new',
                        (0, 'draw','jump'):'alt_day2_one_play_draw_new'
                    }
        generate_cards_alt('bg hall', dialogs)

# ****************   НОВЫЕ  СОПЕРНИКИ   ******************************************
        if alt_my_rival_final.take == 'un':
            rival = CardGameRivalWiseUsual(un_avatar_set, u"Лена", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_final.take == 'sl':
            rival = CardGameRivalWiseUsual(sl_avatar_set, u"Славя", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_final.take == 'dv':
            rival = CardGameRivalWiseUsual(dv_avatar_set, u"Алиса", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_final.take == 'mi':
            rival = CardGameRivalWiseUsual(mi_avatar_set, u"Мику", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_final.take == 'us':
            rival = CardGameRivalWiseUsual(us_avatar_set, u"Ульяна", alt_day2_gambler_behavior, alt_day2_gambler_skill) # К финалу Ульянка уже и играть научиться должна бы
        elif alt_my_rival_final.take == 'sh':
            rival = CardGameRivalWiseUsual(sh_avatar_set, u"Шурик", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_final.take == 'mz':
            rival = CardGameRivalWiseUsual(mz_avatar_set, alt_day2_gambler_behavior, alt_day2_gambler_skill)           # Женя играет рандомно, как в классике
# ************************************************************************************

    $ alt_hint_poker = alt_hint_poker_contractual                                           # подсказки комбинаций — по просмору правил
    jump cards_gameloop_wise_alt                                                            # переход карточный стол

#-------------------------------------------------------------------------------------------------
label alt_day2_final_fail_end_new:
    $ alt_day2_result_tour = 21                                             # Семён проиграл в финале
    scene bg int_dining_hall_sunset with dissolve
    $ persistent.altCardsWon2_new = True

    if alt_day2_gamblers_final[0].take != 'me':                             # если 1-й игрок — НЕ Семён
        $ alt_day2_gamblers_final[0].winner = True                          # он и выиграл
    else:                                                                   # если 2-й игрок — НЕ Семён
        $ alt_day2_gamblers_final[1].winner = True                          # он и выиграл
    $ alt_tournament_state = "final_end"                                    # устанавливаем конец финала

    if not alt_day2_detour_final:                                           # если НЕ пропуск финала
        "Похоже, у меня не было ни шанса."
        call alt_day2_summary_poker_round

    scene
    call alt_day2_final_analizer
    $ renpy.block_rollback()                                                          # блокируем роллбак
    scene bg int_dining_hall_sunset with dissolve

# ---------------------------------------------------- ДИАЛОГИ
    if alt_my_rival_final.take == 'un':
        $ lp_un += 1
        stop music fadeout 2
        show un surprise pioneer with dissolve
        "Кажется, Лена ещё не до конца поняла, что именно сейчас произошло."
        play music music_7dl["take_my_hand"] fadein 3
        "А произошло рождение легенды, +50 к опыту, новый уровень и разблокировка уверенности в себе!"
        show un cry_smile pioneer with dspr
        "Лена смотрела на меня долго, неотрывно, и у неё тряслись руки."
        "Я молчу, она молчит, а вокруг как будто выросла некая отталкивающая стенка, защищающая нас — но лишь пока мы вместе."
        "Как будто два человека, каждый из которых неполон в одиночестве, вместе намного сильнее, чем если просто сложить их характеристики."
        "Я не могу сказать сейчас, поддавался ли я или играл в полную силу, но просто прийти сюда уже было хорошей идеей, сторицей окупившейся этими мгновениями."
        dreamgirl "Не влюбись в неё, барин, вы знакомы меньше суток."
        "Я пожал плечами."
        th "Ну и что?"
        "Ведь поют же все вокруг о любви с первого взгляда, почему бы и мне не пасть жертвой этого волшебного явления?"
        "Ну ладно, но просто признаться себе в том, что она мне нравится, я могу?"
        "Просто лицо, фигура и манера поведения."
        th "Возможно, у неё килограммовые тараканы там, и она только с виду няша-скромняша, глазки в пол, ресничками бяк-бяк."
        th "Но я-то об этом не знаю, правда?"
        th "А значит, буду наслаждаться неведением."
        th "Ибо оно и есть истинное блаженство."
        "Не знать плохого о любимых, не понимать смысл текста красивой песни на японском, не думать об удобрениях для клубники и яблонь, не понимать, что красивая шубка означает смерть животного."
        "Здесь и сейчас — на малую долю секунды — просто влюбиться, пасть жертвой ситуации, настроения и атмосферы."
        with fade
        "И отпустить мгновение, потому что пора просыпаться и идти на работу."
        me "Поздравляю с победой."
        "Улыбнулся я."
        show un shy pioneer with dspr
        un "С-спасибо…"
        "Её имя уже внесли в список победителей, и завтра, скорее всего, заставят поднимать флаг, как самую активную участницу."
        "Ведь нельзя же занять первое место, не принимая активного участия."
        "Правда?"
        "Ох, мои соболезнования."
        if alt_day2_dv_ultim == 1:
            th "Хотя это, наверное, мне соболезновать надо?"
            dreamgirl "Намекаешь на двачевские инсинуации? Не дрейфь, она умылась, не дойдя и до финала, постесняется."
            "Будто подтверждая мои слова, Алиса, что всю партию следила за нами, казалось, забыв дышать, вздрогнула и отвела глаза."
            "Похоже, да, не хватит ей пороху довести свою гадость до логического завершения."
        stop music fadeout 3

    elif alt_my_rival_final.take == 'sl':
        $ lp_sl -= 1
        $ karma += 10
        stop music fadeout 3
        show sl sad pioneer with dspr
        "Славя застонала и уронила голову на сложенные руки."
        play music music_list["forest_maiden"] fadein 5
        sl "Вы хотя бы пытались, ребята?"
        me "Я — старался!"
        sl "Семен, пожалуйста."
        show sl serious pioneer with dspr
        "Она нахмурилась."
        sl "Хуже меня нет игрока в карты, а я заняла… Ах, зачем я вообще согласилась!"
        me "Но мы же…"
        sl "Вам что, и правда было настолько всё равно, что вы даже поленились немного постараться?"
        show sl sad pioneer with dspr
        sl "Я очень, очень расстроена."
        sl "Если вы и на завтрашних танцах будете такими же активными, я пойму намёк, и до конца смены развлекайте себя сами."
        show mt laugh pioneer at left with dissolve
        mt "Что это у нас, а?"
        mt "Демарш победителя? Ну, наконец-то! {w}Я уже было подумала, что ты оживший экспонент мадам Тюссо." # "экспонент" — так задумано или меняем на "экспонат"? ## полагаю, трудно случайно вместо "экспонат" написать "экспонент"
        show sl angry pioneer with dspr
        sl "Ольга Дмитриевна, я серьёзно, а вы!"
        show mt normal pioneer with dspr
        mt "Славя, просто наслаждайся победой, хорошо? {w}Я знаю твоё отношение к карточным играм, и если бы у меня была возможность поставить кого-нибудь вместо тебя, я бы так и поступила."
        hide mt with moveoutleft
        "Ольга сочувственно повздыхала, подмигнула ей и скрылась на кухне."
        "Похоже, слова о призе имели под собой кое-какое обоснование!"

    elif alt_my_rival_final.take == 'dv':
        $ lp_dv = lp_dv/2
        stop music fadeout 2
        if loki or herc:
            "Проиграть было забавно."
            play music music_list["you_lost_me"]
            "С любой из сторон, как ни крути, я оказывался в выигрыше — в случае победы мне удастся немного заткнуть Двачевскую."
            dreamgirl "Ровно до того момента, пока она не созреет для новой шалости."
            th "Этого достаточно."
            "А в случае поражения она устроит мне пиар-акцию в духе «Сёма едет, прячьте тёлок.»"
            "Так что я от всей души пожелал удачи сопернице."
            "И приготовился к шоу."
        else:
            th "Я слил."
            th "Я облажался."
            play music music_list["you_lost_me"]
            th "Как всегда…"
            if alt_day2_walk == 1:                                                 # была лишняя проверка
                th "Несмотря даже на то, что я пометил карты."
            "Появилось это противное чувство, что сейчас на меня начнут показывать пальцем и шептаться «Смотрите, это он! Да, он! Он облажался.»"
            "Я двинулся прочь от стола, не поднимая ни на кого глаз."
            "Особенно — на Алису."
            "Её взгляд буквально жёг мне спину."
        if alt_day2_dv_ultim == 1:                                                 # Спорил
            th "Я проиграл пари."
            if loki or herc:
                "Теперь ждём завтрашнего дня и наслаждаемся бесплатной рекламой?"
            else:
                "Теперь мне… {w}Крышка? Кранты? Конец?"
                th "Может, сбежать из лагеря, пока не поздно?"
        else:                                                                       # НЕ спорил
            if alt_day2_dv_ultim == 2:                                              # Если лапал
                "И теперь, если она расскажет всем, что я её лапал — это же правдой будет, да?"
                "Как говорил мой батя в трудных ситуациях — не упс, а йопс."
            else:                                                                   # НЕ лапал
                "Хотя я не спорил с Двачевской, она теперь вполне может рассказать всем то, что она напридумывала на крыльце."
                "И ей поверят. Как обычно верят любому победителю."

        "Алиса победила, и все наперебой принялись её поздравлять."
        "Электроник взмахнул руками, ознаменовав окончание турнира, и дописал в таблицу её имя."
        th "Алиса выиграла…"
        if alt_day2_dv_ultim == 1:
            th "А я проиграл и турнир, и пари…"
        else:
            th "А я проиграл… Как и всегда, впрочем."
        th "Что же будет?!"
        show dv normal pioneer2 at fleft with dissolve
        "Я посмотрел на Алису. Казалось, на её лице не было и следа радости…"
        if alt_day2_dv_ultim == 2:
            "Алиса встала из-за стола и, ощутимо заставляя себя…"
            show mt normal pioneer at fright with dissolve
            "Направилась к вожатой! Да! Момент истины!"
            show dv normal pioneer2 at fleft with moveinleft
            th "Хватит ли девочке пороху?"
            "Внутри меня всё трепетало в предвкушении."
            "Я подвинулся поближе, пытаясь расслышать подробности"
            "Но она говорила шёпотом, и я ничего не мог расслышать…"
            show dv guilty pioneer2 at cright
            show mt normal pioneer at fright
            with dissolve
            "Она краснела всё сильнее, и я буквально мог читать по губам."
            "…руками…"
            "…прямо за грудь…"
            "…и под юбку…"
            me "Двачевская, у тебя такая пылкая фантазия!"
            "Подвёл черту их шептанью я."
            show dv sad pioneer2 at left
            show mt normal pioneer at right
            with dissolve
            me "Может, вслух расскажешь? Мне тоже охота послушать."
            stop music fadeout 3
            "А Ольга Дмитриевна спокойно посмотрела на меня и сказала:"
            mt "Алиса говорит, что игрок из тебя аховый."
            show mt smile pioneer at right with dspr
            mt "По-моему, всё верно."
            hide dv
            hide mt
            with dissolve
            "Я расхохотался и освободил столик."
            "Кто бы сомневался. Не такой реакции от меня ждала Алиска, совсем не такой."
        else:
            "С равнодушием, лениво бросив на меня прищуренный взгляд, Алиса…"
            show mt normal pioneer at fright with dissolve
            "Пошла прямо к Ольге Дмитриевне, стоявшей всё это время среди зрителей!"
            show dv normal pioneer2 at fleft with dspr:
                xalign 0.1
                linear 3.0 xalign 0.7
            if loki:
                th "Неужели скажет?"
            elif herc:
                th "Таки решила рассказать свою байку?"
            if dr:
                th "Она в самом деле расскажет?!"
            if not alt_day2_dv_ultim:
                if loki:
                    th "Я же не стал с ней спорить."
                elif herc:
                    th "До чего ж упёртая."
                    dreamgirl "Никого не напоминает?"
            if dr:
                "Всё во мне словно перевернулось."
                "Я бросился вслед за ней…"
                "Но было уже поздно…"
            elif herc:
                "Я поудобнее уселся и стал ждать развязки."
                dreamgirl "Не боишься?"
                th "Ничуть."
                th "Если вожатая поверит в эту чушь, я в ней разочаруюсь."
            show dv smile pioneer2 at cright
            show mt normal pioneer at fright
            with dissolve
            "Алиса стояла рядом с Ольгой Дмитриевной и что-то горячо шептала ей на ухо, весьма лукаво поглядывая на меня."
            if dr:
                "Этого я не мог допустить!"
                "С громким криком…"
                me "Это неправда!"
                me "Всё, что она говорит обо мне — НЕ-ПРАВ-ДА!"
                show dv smile pioneer2 at left
                show mt normal pioneer at right
                with dissolve
                "Я подбежал к ним."
                stop music fadeout 3
                "А Ольга Дмитриевна спокойно посмотрела на меня и сказала:"
                mt "А по-моему, всё верно."
                show mt smile pioneer at right with dspr
                mt "Ты совсем не умеешь играть в карты."
                "Такого позора я ещё никогда не испытывал."
            elif herc:
                "Я усмехнулся рыжей в ответ."
                me "Давай-давай."
                show dv sad pioneer2 at cright with dspr
                pause(0.3)
                show dv normal pioneer2 at cright with dissolve
                "Не думаю, что Двачевская умеет читать по губам, но она поняла насколько безразличны мне её потуги."
                th "Поздновато ты это поняла."
                dreamgirl "Подлей маслица в огонь."
                th "Каким образом?"
                "В воображении возникло по меньшей мере пять способов вогнать Двачевскую в краску."
                "И все пять — неприличные жесты."
                "Делать это я не стану, но мысль об этом меня позабавила."
                th "Спасибо."
                dreamgirl "К вашим услугам."
                "Ольга посмотрела на меня и спокойно сказала:"
                mt "Ну да, всё верно, не умеет играть."
                mt "Но похоже, его это не слишком заботит."
                stop music fadeout 3
                "Я едва не расхохотался."
                "Сдрейфила!"
            elif loki:
                show dv normal pioneer2 at cright with dissolve
                "Я старался держать лицо и не терять достоинства, ожидая развязки."
                "Не верю, что квалифицированный педагог, вроде нашей вожатой, поверит в эту нелепую чушь."
                "Тем более из уст Двачевской."
                "Если поверит, я в ней немного разочаруюсь."
                "А Двачевской я это припомню."
                "Наконец, Ольга спокойно сказала:"
                mt "Ну да, всё верно."
                mt "Он совсем не умеет играть в карты."
                stop music fadeout 3
                "Рыжая не смогла и пошла на попятную."
                "Я не скрывал улыбки."

    elif alt_my_rival_final.take == 'mi':
        stop music fadeout 3
        show mi happy pioneer with dspr
        $ lp_mi += 1
        $ karma += 10
        mi "Да! Да! Вы понимаете это?! Это снова я, и я снова на коне!"
        play music music_7dl["ourfirstmet"] fadein 3
        mi "У меня не было никаких сомнений в том, что я приду и всех победю!"
        mi "И я пришла и победила."
        mi "Да я, да я… Я супер-Мику!"
        me "Очаровательное чудовище."
        "Пробормотал я."
        show mi smile pioneer with dspr
        mi "Я не так часто выхожу из клуба, потому что всем постоянно что-то надо, все куда-то спешат и говорят мне «потом поговорим!»."
        mi "А я не хочу потом, я сейчас хочу! И сейчас, пока я победитель, вы все должны меня слушать и не ругаться, что я много болтаю!"
        th "Дефицит внимания, ласки, тепла и заботы… А я ещё себя хикикомори считал."
        me "А кричать-то зачем?"
        stop music fadeout 3
        "Оказаться в финале для меня уже было изрядным достижением, поэтому я не особо расстраивался насчёт проигрыша."
        play music music_7dl["tender_song"] fadein 3
        "А Мику вдруг воздела к небу пальчик."
        show mi happy pioneer with dspr
        mi "Ой, а я знаю, кажется! Да! Мне только что идея в голову пришла! Я…"
        show mi happy pioneer far with dissolve
        "Она забралась на стол."
        mi "Я вам спою!"
        "Она набрала в грудь воздуха, и…"
        show dv angry pioneer2 at cleft with easeinleft
        show mt angry pioneer at cright with easeinright
        with vpunch
        "Неизвестно откуда взявшиеся Ольга и Алиса, взревев в унисон, ринулись было стаскивать её на пол."
        "Но где там!"
        show mi laugh pioneer far at fleft with diam
        "Стол для игры финалистов был большой, не чета узеньким, за которым мы квалифицировались."
        "Поэтому маленькая, юркая японочка успешно прыгала между руками загребущими и голосила во всю силу своих развитых лёгких."
        "Пела она о чём-то своём, на лунном наречии, которое я даже под градусом считал зубодробительным, а потому и не пытался вслушиваться."
        "Куда интереснее было слушать голос."
        "И смеяться над тем, как тут и там в такт пению раздаются хлопки."
        "Чаще ловящих Мику Алисы и Ольги Дмитриевны, но и из благодарной публики тоже шла своя доля оваций."
        mi "Ла-ла, ла-ла-ла-ла, ла-ла-ла, ла-ла-ла-ла!"
        "Вопила она, бегая по столам, стульям и демонстрируя нам не только высокий уровень игры в карты, но и недюжинную подготовку по части паркура."
        "Я бы поставил на японку и не прогадал."
        "У неё вся жизнь такая."
        "Суетная, бегательно-прыгательная на сцене, и выступления не по три форматных минутки, а полноценные концерты на несколько часов."
        hide mt
        hide dv
        with dissolve
        "Так что ещё минут пять — и обе ловчих свалились рядом со столами, а она всё продолжала и продолжала петь, делая в воздухе странные, стригущие движения пальцами."
        "Отчего-то от таких движений, да ещё в исполнении ультрамаринового маникюра, неприятно-холодно ёкало в животе."
        show mi normal pioneer far at center with easeinleft
        with fade
        "Но всё когда-нибудь кончается."
        show mi smile pioneer with dissolve
        "Кончилась и долгоиграющая песенка японской старлетки, и она, подойдя по столу с моей стороны, протянула мне руку."
        "И я, как истинный джентльмен, принял её и помог девочке спуститься."
        show mi happy pioneer close with dspr
        mi "Спасибо! Ты мой герой!"
        show mt rage pioneer at fleft with dissolve
        mt "Ну, Хацунэ!"
        "Мику на миг прижалась ко мне всем телом, а затем убежала от криков разъярённой вожатой."
        hide mi with flash

    elif alt_my_rival_final.take == 'us':
        $ lp_us += 1
        stop music fadeout 2
        "Как известно, в карты везёт новичкам и дурачкам."
        play music music_7dl["genki"] fadein 3
        "Так как мы все здесь новички, мы были в равных условиях."
        "Но кое-кому перепало на один шанс больше!"
        "И все догадываются, о ком речь, и почему ему больше досталось!"
        show us normal pioneer with dissolve
        "Эти пустые, стеклянные голубые глаза очень странно смотрятся в обрамлении алой чёлки."
        "Косица пшеничного цвета, как у Слави, этому ребёнку подошла куда бы больше."
        "Такая вот несостоявшаяся блондинка."
        show us laugh pioneer with dspr
        us "Ура! Я победила!"
        "Она вскочила на стул!"
        us "Я победила! И теперь суперприз мой! {w}Моооооой!"
        me "Твой, твой. Ты только слезь со стула, а то брякнешься ещё."
        "Да где там."
        "Ульянка начала подпрыгивать на опасно скрипящем стуле и скандировать:"
        us "Приз! Приз! Приз!"
        me "Успокойся, а?"
        show us grin pioneer with dspr
        us "Ты просто завидуешь, что у меня будет приз, а у тебя нет!"
        "Понятия не имею, о каком призе она говорит."
        "Вообще, пойду-ка я, пока чего не случилось."
        hide us with dissolve
        scene
        call show_tournament_table
        "А в самом центре таблицы огромными красными буквами значилось имя."
        el "Победитель — Ульяна!"
        "Все стали кричать «поздравляем, поздравляем»!"
        scene bg int_dining_hall_sunset
        show us grin pioneer
        with dissolve
        "Но Ульяна отмахнулась. {w}Её интересовало другое:"
        us "А где призы?"

    elif alt_my_rival_final.take == 'sh':
        show sh normal pioneer with dissolve

        "Чествование Шурика выглядело неловко и натянуто."

        show sh serious pioneer far with dissolve
        pause(0.25)
        show sh serious pioneer far at fright with move
        hide sh with moveoutright

        "Он встал, поклонился и вышел из столовой, не дожидаясь даже, когда его имя внесут в таблицу лидеров."

        show mi shocked pioneer far at center with dspr
        mi "Кошмарный человек."
        "Заметила Мику."

        show mi upset pioneer far with dspr
        mi "Совершенно далёк от публичности."

        show un normal pioneer far at left with dspr
        show mi upset pioneer far at right with move
        un "У него другие достоинства."

        show us smile pioneer far at fleft with moveinleft
        us "Да? Ну-ка подробнее, пожалуйста, о достоинствах, а то я не расслышала."

        show mi surprise pioneer far at fright
        show un serious pioneer far at center
        with move
        un "Тебе бы только о похабностях слушать."

        show sl serious pioneer far at cleft with dspr
        show un serious pioneer far at cright with move
        sl "Лена, а ты бы сама немного думала, что говоришь в присутствии ребёнка."

        show un surprise pioneer far
        show us dontlike pioneer far
        show mi dontlike pioneer far
        with dspr
        us "Эй, мне уже четырнадцать!" #us "Эй, мне уже двадцать девять!"
        mi "Эй, мне уже шестнадцать!"

        un "Э…"
        sl "Да-да, ты тут о достоинствах Шурика разглагольствовала."

        show dv surprise pioneer2 far at center with dspr
        dv "Девочки, а что это вы тут обсуждаете, и без меня?"

        show mi cry_smile pioneer far:
            xcenter 0.86
        show un grin pioneer far:
            xcenter 0.67
        show sl surprise pioneer far:
            xcenter 0.33
        show us surp1 pioneer far:
            xcenter 0.10
        with move
        un "Ой, Двачевская, потеряйся! Кошмарище лесное, додумалась новичка сиськами запугивать."
        me "Эй, я всё ещё здесь!"

        show mi rage pioneer far
        show un rage pioneer far
        show dv rage pioneer2 far
        show sl angry pioneer far
        show us angry pioneer far
        with dspr
        all "Заткнись!" with vpunch

        show mi smile pioneer far
        show un shy pioneer far
        show dv grin pioneer2 far
        show sl shy pioneer far
        show us normal pioneer far
        with dspr
        "Я и заткнулся."

        show mi laugh pioneer far
        show un laugh pioneer far
        show dv laugh pioneer2 far
        show sl laugh pioneer far
        show us laugh pioneer far
        with dspr
        "Что мне ещё оставалось." #Сёма, какой же ты дегенерат, пиздец просто!

    elif alt_my_rival_final.take == 'mz':
        show mz normal glasses pioneer with dissolve
        "Жужелица встала."
        "Окинула всех диковатым взглядом."
        mz "Всё, что ли? Больше жертв не будет?"
        play sound sfx_7dl["highfive"]
        pause(1)
        play sound sfx_7dl["highfive"]
        pause(1)
        "В полной тишине спросила она."
        play sound sfx_7dl["highfive"]
        pause(1)
        play sound sfx_7dl["highfive"]
        show el smile pioneer at left with dissolve
        "Только Электроник продолжал хлопать."
        mz "Ну ладно. Я пойду тогда."
        el "Ура, да здравствует победитель!"

        show mz normal glasses pioneer far with dissolve
        pause(0.25)
        show mz normal glasses pioneer far at fleft with move
        hide mz with moveoutleft

        play sound sfx_7dl["highfive"]
        "Закричал Сыроежкин ей вслед."
        "По-моему, это всё-таки любовь."
        sh "Эл, всё, она ушла. Успокойся."
# ---------------------------------------------------- \\ Диалоги
    stop music fadeout 3
    jump alt_day2_prepare_transition_to_supper                        # пошли ужинать

#-------------------------------------------------------------------------------------------------
label alt_day2_final_win_end_new:
    $ alt_day2_result_tour = 22                                             # Семён выиграл в финале
    $ lp_dv += 1

    if not alt_day2_detour_final:                                          # если НЕ пропуск финала
        $ persistent.altCardsWonRivals_new[alt_spr_my_rival] = True        # Выиграли у этого соперника
    $ persistent.altCardsWon3_new = True

    if alt_day2_gamblers_final[0].take == 'me':                             # если 1-й игрок — Семён
        $ alt_day2_gamblers_final[0].winner = True                            # он и выиграл
    else:                                                                   # если 2-й игрок — Семён
        $ alt_day2_gamblers_final[1].winner = True                            # он и выиграл
    $ alt_tournament_state = "final_end"                                   # устанавливаем конец финала

    if not alt_day2_detour_final:                                                # если НЕ пропуск финала
        call alt_day2_summary_poker_round

    scene
    call alt_day2_final_analizer
    $ renpy.block_rollback()                                                          # блокируем роллбак
    stop music fadeout 3
    scene bg int_dining_hall_sunset with dissolve

# ---------------------------------------------------- ДИАЛОГИ
    if alt_my_rival_final.take == 'un':
        show un shy pioneer with dissolve
        un "К-кажется, в-всё."
        play music music_7dl["take_my_hand"] fadein 3
        me "Что?"
        show un sad pioneer with dspr
        un "Н-ну… Ты выиграл. П-поздравляю."
        "Пробормотала она."
        "Её с трудом можно было разобрать за шумом толпы, а она всё продолжала и продолжала говорить…"
        "Будь моя воля, я бы, наверное, попросил её говорить громче."
        th "Но где там."
        th "Это же означает неминуемое сближение."
        scene bg int_dining_hall_sunset with dissolve
        "Не слушая больше то, что она мне говорит, я поднялся."
        "И пошёл к доске, где Электроник уже писал моё имя."
        scene
        call show_tournament_table
        "Моё!"
        if alt_day2_dv_ultim in (1, 2):
            th "И пусть только рыжая стерлядь попробует что-нибудь там вякнуть."
        scene bg int_dining_hall_sunset with dissolve
        if alt_day2_dv_ultim == 2:
            show dv shy pioneer2 with dissolve
            "Поймав мой взгляд, она покраснела как маков цвет."
            "А я, склонив голову набок, изобразил пантомиму под названием «натягиваю резиновую перчатку»."
            show dv shocked pioneer2 with dspr
            "И красноречиво так пошевелил пальцами."
            "Алисе аж плохо стало."
            th "Или это она подумала, что я не перчатку надеваю, а… Фу, какая она испорченная."
        else:
            "Лена потерялась где-то на заднем плане, а я неотрывно чувствовал чей-то взгляд лопатками."
            show dv smile pioneer2 with dspr
            play sound sfx_punch_medium
            dv "Поздравляю!" with vpunch
            "Поэтому почти ожидал хлопка между лопаток."
            "Видимо, Двачевская так приветствует всех, кто ей интересен."
        hide dv with dissolve

    elif alt_my_rival_final.take == 'sl':
        $ lp_sl += 1
        show sl smile pioneer with dspr
        "Я победил?"
        play music music_7dl["please_reprise"] fadein 3
        "Победил?!"
        me "Да!"
        "Бросив над головой карты, рявкнул я:"
        me "Я — победитель!!!" with vpunch
        show sl smile2 pioneer with dspr
        "Почему-то здесь и сейчас хотелось вести себя так, как душа лежит."
        "Не так, как правила того требуют, или «что же люди скажут»."
        "Это её влияние. Её."
        "А ведь мы знакомы меньше суток."
        "Но уже сейчас искренность проявлений чувств становится одной из самых важных добродетелей."
        sl "Да!"
        "Звонко произнесла она."
        "Её глаза сияли."
        sl "Ты победитель турнира."
        sl "Ты — победитель."
        "Как в боксе, она стоит рядом со мной."
        "Хватает меня за запястье."
        "И тянет к небу поднятой рукой."
        show sl happy pioneer with dspr
        sl "Се-{w=.3}мён! Се-{w=.3}мён!"
        "Скандирует она."
        "Трудно бороться с чувством сюрреалистичности происходящего."
        "Как будто бы я попал в какую-нибудь космическую оперу или ещё какой-то пафосный жанр."
        th "Но эти люди не умеют стесняться честного слова и честного чувства."
        "Они кричат вместе с ней."
        "Смотрят на меня."
        "Мои пятнадцать минут славы."
        dreamgirl "Пятнадцать минут Слави?"
        "А я расхохотался."
        th "Да! Да, чёрт возьми. Именно так."
        "К нам протолкалась Ольга Дмитриевна."
        show mt normal pioneer at left with dissolve
        mt "Не уходи никуда после ужина, будет вручение призов."
        show sl normal pioneer with dspr
        dv "Поздравляю!"
        "Из-за спины я услышал голос, который слышать бы очень не хотел."
        "Судя по сузившимся глазам Слави, не я один."
        "Но я обернулся."
        hide mt
        hide sl
        with dissolve
        show dv smile pioneer2 at cright with dissolve
        if alt_day2_dv_ultim == 1:
            dv "Ты победил в споре и турнире."
        else:
            dv "Молоток!"
        hide dv with dissolve
        "Она ткнула меня кулаком в плечо и, развернувшись, растворилась в толпе."

    elif alt_my_rival_final.take == 'dv':
        $ lp_dv += 1
        th "Я выиграл!"
        play music music_7dl["sheiscool"] fadein 3
        th "Выиграл?"
        th "Выиграл!!!"
        show dv normal pioneer2 with dspr
        "Ещё несколько часов назад я не мог и представить себя таким счастливым!"
        "Я победно смотрел на Алису, ещё не веря до конца в свою удачу…"
        "А вокруг уже все поздравляли меня с победой, и Электроник писал моё имя в своей таблице!"
        scene
        call show_tournament_table
        th "Моё имя!!!"
        th "Я выиграл турнир!"
        scene bg int_dining_hall_sunset with dissolve
        "Словно и не было этих часов переживаний и напряжения…"
        "Я стал лёгким как пёрышко…"
        "Я как будто научился летать!"
        if alt_day2_dv_ultim == 1:
            th "Я выиграл пари!!!"
        if alt_day2_dv_ultim == 2:
            show dv shy pioneer2 with dissolve
            "Алиса была готова на месте провалиться — до такой степени она покраснела."
            "Поймав её взгляд, я подмигнул, сделав препохабнейшую морду лица."
            show dv rage pioneer2 with dspr
            "Её перекосило."
            "А я расхохотался."
            "Вечер сегодня определённо мой!"
        else:
            show dv smile pioneer2 with dissolve
            "А Алиса наконец поднялась со своего места и, проходя мимо меня, хлопнула по плечу."
            dv "Поздравляю!"
            "И от этих слов мне стало так радостно!"
            th "Я победил Алису!!!"
        hide dv with dissolve

    elif alt_my_rival_final.take == 'mi':
        $ lp_mi += 2
        $ alt_day2_mi_snap = True
        show mi smile pioneer with dspr
        mi "Ты и правда победил! Ты молодец!"
        play music music_7dl["tellyourworld"] fadein 3
        "Воскликнула она."
        show mi normal pioneer with dspr
        mi "Только не думай, что тебе это поможет!"
        "Строго сказала девочка."
        mi "В следующий раз я тебя обязательно обыграю!"
        "Конечно. Сколько угодно. Но — в следующий раз."
        "А сейчас…"
        "В таблице красовалось моё имя, выведенное толстым красным маркером."
        "Мику схватила меня за руку и потащила за собой."
        me "Эй!"
        mi "Да быстрее же ты!"
        "Ничего не понимая, я поспешил за ней."
        me "И что?"
        "Мы остановились у доски, и девочка кому-то замахала."
        mi "Дядя Боря-сенсей! Мы здесь!"
        if ('sport_area' in list_voyage_7dl):
            th "Что ей может понадобиться от Саныча?"
            "С любопытством подумал я."
        show ba normal uniform at cleft behind mi # Здесь не надо meet поставить? ## "знакомство" уже состоялось к этому моменту либо при посещении спортплощадки, либо по завершению обхода на экстраде заочно
        show mi smile pioneer at right
        with dissolve
        ba "Да, мал{b}а{/b}я, чего звала?"
        mi "У вас ещё есть кадры?"
        show ba smile uniform with dspr
        ba "Для тебя, мал{b}а{/b}я, сколько влезет."
        "Из ниоткуда в его руках появился жёсткий коричневый чехол для фотоаппарата, а оттуда…"
        "Старый добрый «компакт-автомат», плёночный."
        "Я чуть было не сказал «раритет», но видно было, что машинка рабочая."
        ba "Только без вспышки сегодня, так что становитесь как-нибудь, где посветлее."
        "Мику улыбнулась и развернула кипучую деятельность, тормоша всех и переставляя."
        "В результате полотнище таблицы было снято и перенесено поближе к окошку, где Шурик и Электроник держали его нарастяг."
        scene bg int_dining_hall_sunset with dissolve
        with dissolve
        scene
        call show_tournament_table
        "Мику встала рядом."
        show mi normal pioneer at cleft with dissolve
        "Ещё ближе."
        "Ещё чуточку."
        show mi dontlike pioneer with dspr
        mi "Сень!"
        "Наконец не выдержала она."
        mi "Я же с тобой фотографируюсь! А ну, быстро обними девушку."
        me "Но я…"
        "Я вздохнул."
        th "Я не помню, когда я последний раз так фотографировался с кем-то."
        th "Я не умею никого обнимать для фото…"
        show mi normal pioneer with dspr
        mi "Смелее же, ну!"
        "Она нетерпеливо пошевелила плечиком."
        scene cg d2_mi_polaroid_7dl
        with dissolve
        "И я, вздохнув, положил ей на плечо руку."
        "Неловко — как и чувствовал себя — неловко."
        "Свисающая кисть, нечувствительные пальцы."
        "Как фотографировался бы с другом, а не с девушкой."
        "До меня слишком поздно дошло, что девушку надо обнимать за талию, а не вот так."
        "Но… поздно!"
        play sound sfx_7dl["snap"]
        scene
        $ renpy.show("cg d2_mi_polaroid_7dl", what = Sepia("cg d2_mi_polaroid_7dl"))
        show PolaroidFrame_7dl
        with flash
        pause(3)
        me "Сыыыр."
        "Запоздало опомнился я."
        scene bg int_dining_hall_sunset
        show mi laugh pioneer at cleft
        with dissolve
        mi "Хи-хи-хи."
        mi "Сенечка, ты чудо."
        hide mi with moveoutleft
        "Она рассмеялась и убежала."

    elif alt_my_rival_final.take == 'us':
        $ lp_us -= 1
        th "Я выиграл!"
        th "Выиграл?"
        th "Выиграл!!!"
        play music music_7dl["genki"] fadein 3
        "Бац!" with vpunch
        with flash_red
        show us calml pioneer with dissolve
        us "И ничего ты не выиграл!"
        "Она хмуро смотрела на меня снизу вверх."
        us "Ты играл неправильно, переигрываем!"
        me "Что это значит, «неправильно»?"
        show us dontlike pioneer with dspr
        me "Я выиграл турнир! {w}Как я могу играть неправильно?"
        us "Молча! Ты жульничал!"
        "Она топнула ногой."
        us "Ты неправильно играл и жульничал!"
        if alt_day2_walk == 1:
            th "Неужели про крап узнала? Но как?"
            th "Если она сейчас всем про него раcскажет, меня линчуют на ближайшей осине."
        us "Ты плохо мне поддавался."
        "А. Ну, это меняло всё дело."
        hide us with dissolve
        "Я расхохотался и отошёл."
        show dv smile pioneer2 with dissolve
        "А Алиса наконец поднялась со своего места и, проходя мимо меня, хлопнула по плечу."
        dv "Поздравляю!"
        "И от этих слов мне стало так радостно!"
        th "Я победил!!!"
        hide dv with dissolve

    elif alt_my_rival_final.take == 'sh':
        stop ambience
        show sh rage pioneer with dissolve
        sh "Значит, победил?"
        play music music_7dl["dead_silence"] fadein 3
        "Медленно произнёс он."
        "Он так странно стоял, что я никак не мог разглядеть его глаз из-за бликов на очках."
        show sh serious pioneer with dspr
        "Да и сама его поза…"
        "Почему-то вдруг вспомнился персонаж Элайджи Вуда из «Города Грехов»."
        "Вроде бы, ничего такого сверхъестественного не делал, но тревогу внушал примерно так же — одним появлением на экране."
        "И Шурик заставлял меня тревожиться."
        sh "То есть думаешь, что можно просто так прийти и выиграть мой турнир?"
        scene black
        show sh rage pioneer close
        with diam
        sh "Да кто ты такой вообще?"
        sh "Ведёшь себя, будто тебе уже давно не семнадцать лет."
        show sh rage pioneer close with dspr
        sh "А может быть, ты…"
        scene
        $ renpy.show("bg int_dining_hall_sunset", what = Noir("bg int_dining_hall_sunset"))
        show sh rage pioneer close with dspr:
            xalign .5 yalign .7 zoom 0.7
            ease 0.3 yalign .4 zoom 1.25
        "Он сделал резкий шаг в мою сторону и протянул руку."
        mt "Шурик!"
        stop music fadeout 3
        play ambience ambience_dining_hall_full fadein 5
        show blinking
        scene bg int_dining_hall_sunset with dissolve
        with diam
        show sh upset pioneer with dissolve
        "Наваждение момента исчезло, Шурик из зловещей фигуры превратился обратно в обычного, чуть рассеянного, парня."
        "Серые, давящие стены уступили место красноватому свету катящегося на закат светила."
        "И самое главное —"
        "Ведь я же победитель!"
        hide sh with dissolve
        scene
        call show_tournament_table
        "Электроник внёс моё имя в список победителей."
        el "А после ужина…"
        scene bg int_dining_hall_sunset with dissolve
        "Ольга Дмитриевна заткнула ему рот рукой."
        th "Правильно, пусть будет сюрпризом. А для спойлерщиков в аду отдельный котёл стоит."

    elif alt_my_rival_final.take == 'mz':
        "Реакция Жужелицы была обескураживающей."
        "Её не было."
        "Но меня это не смущало."
        "Самое главное, что я победил!"
        "Остальные пусть думают и делают что хотят."
        "Даже Алиса."
        "Сейчас-то ей никто не поверит."
        "И это, пожалуй, радует больше всего."
# ---------------------------------------------------- \\ Диалоги

    stop music fadeout 3
    jump alt_day2_prepare_transition_to_supper                                            # ушли ужинать

# ======================================================================================================================
#                                          ОБЩИЕ МЕТКИ ПО ОБРАБОТКЕ ТУРНИРА
# ======================================================================================================================

# ----------------------------------------------------------------------------------
# ОПРЕДЕЛЯЕМСЯ С ОЧЕРЁДНОСТЬЮ ПЕРВОГО ХОДА В КОНЕ
label alt_day2_stipulation_new:
    scene bg int_dining_hall_sunset with dissolve
    python:
        alt_spr_rival = [alt_spr_my_rival,alt_emo_my_rival,alt_acc_my_rival,alt_clot_my_rival]
        alt_spr_my_riv_1 = " ".join(alt_spr_rival)
        renpy.show(alt_spr_my_riv_1,[alt_pos_my_rival])
        renpy.transition(dspr)
    alt_nick_my_rival "Кто первый ходит?"

    $ alt_whose_first_move = renpy.random.choice(['rival', 'player'])
    pause(1)
    if alt_tournament_state == "1_round_start":                             # если первый тур
        "Я достал из нагрудного кармана пятирублёвую монетку — очень надеюсь, что ни у кого не возникнет вопросов касательно номинала — и подбросил её в воздух."
        "Сомнительная честь сделать первый ход выпала"
    elif alt_tournament_state == "semifinal_start":                         # если полуфинал
        "Я снова подбросил монетку в воздух."
        "В этот раз не повезло"
    elif alt_tournament_state == "final_start":                             # если финал
        "В третий раз закинул он невод… В смысле, подбросил монетку."
        "Похоже, первому ходить придётся"
    if alt_whose_first_move == 'rival':
        extend " %(alt_name_my_rival_d)s."
    elif alt_whose_first_move == 'player':
        extend " мне."

    return

# ----------------------------------------------------------------------------------
# Победа Семёна в очередной игре тура
label alt_day2_one_play_win_new:
    window auto
    $ alt_day2_my_win += 1                                                  # +1 к победам Семёна
    $ alt_day2_game_played_out += 1                                         # +1 результативная игра
    $ alt_day2_result_current_game = 1                                      # победа Семёна
    jump alt_day2_checking_scores                                           # считаем очки

# ----------------------------------------------------------------------------------
# Поражение Семёна в очередной игре тура
label alt_day2_one_play_fail_new:
    window auto
    $ alt_day2_rival_win += 1                                               # +1 к победам соперника
    $ alt_day2_game_played_out += 1                                         # +1 результативная игра
    $ alt_day2_result_current_game = 2                                      # победа соперника
    jump alt_day2_checking_scores                                           # считаем очки

#-----------------------------------------------------------------------------------
# НИЧЬЯ в очередной игре тура
label alt_day2_one_play_draw_new:
    window auto
    $ show_cards_alt()
    $ renpy.transition(dissolve)
    el "Ничья! Играйте ещё раз."
    if alt_tournament_state == "1_round_start":                             # если первый тур
        jump alt_day2_1_tour_re_game                                        # играем первый тур
    elif alt_tournament_state == "semifinal_start":                         # если полуфинал
        jump alt_day2_semifinal_re_game                                  # играем полуфинал
    elif alt_tournament_state == "final_start":                             # если финал
        jump alt_day2_final_re_game                                      # играем финал

#-----------------------------------------------------------------------------------
# Анилизируем счёт по играм в этапе
label alt_day2_checking_scores:
    scene bg int_dining_hall_sunset with dissolve
    if alt_day2_my_win == alt_day2_rival_win:                                                   # если счёт равный
        if alt_day2_game_played_out == 0:                                                       # ещё не играли (0:0)
            if alt_day2_gamblers_final[0].take == 'me':                                         # если 1-й игрок — Семён
                $ alt_day2_upper_gambler_name = "Семёном"
                $ alt_day2_bottom_gambler_name = alt_name_my_rival_t
            else:
                $ alt_day2_upper_gambler_name = alt_name_my_rival_t
                $ alt_day2_bottom_gambler_name = "Семёном"
            show el normal pioneer far at left with dissolve
            el "До начала финальной игры между %(alt_day2_upper_gambler_name)s и %(alt_day2_bottom_gambler_name)s осталась минута, счёт по-прежнему ноль-ноль."
            "Электроник комментировал игру, как умел."
            hide el with dissolve
            return
        else:                                                                                   # если 1:1
            call alt_day2_current_game_end_compare_hands                                        # сравнение комбинаций по итогам игры
            show el serious pioneer far at left with dspr
            el "Итак, по итогам двух игр у нас пока ничья; победитель определится в решающей игре."
            el "А кто будет ходить первым — сейчас разыграем, и поможет нам в этом портативный генератор случайных чисел."
            "Электроник выудил из кармана монету."
            el "Орёл? Решка?"
            menu:
                "Орёл":
                    $ alt_whose_first_move_choice = 1
                "Решка":
                    $ alt_whose_first_move_choice = 0
            $ alt_whose_first_move_random = renpy.random.choice([0, 1])
            if alt_whose_first_move_random == 0:
                "Эл подбросил монетку, выпала решка."
            else:
                "Подброшенная монета упала орлом."
            $ renpy.block_rollback()                                                                # блокируем роллбак
            if alt_whose_first_move_choice == alt_whose_first_move_random:
                if alt_name_my_rival_i == "Шурик":
                    el "Надо же, угадал. Первым ходить будет Шурик{nw}"
                else:
                    el "Надо же, угадал. Первой ходить будет %(alt_name_my_rival_i)s{nw}"
                if alt_whose_first_move == 'player':
                    extend ", как и в первой игре."
                else:
                    extend ", как и во второй игре."
                $ alt_whose_first_move = 'rival'
            else:
                el "Мимо. Так что первый ход — твой{nw}"
                if alt_whose_first_move == 'player':
                    extend ", как и во второй игре."
                else:
                    extend ", как и в первой игре."
                $ alt_whose_first_move = 'player'
            scene bg int_dining_hall_sunset with dissolve
            jump alt_day2_transition_to_game
    elif alt_day2_my_win > alt_day2_rival_win:                                                  # Семён ведёт в счёте
        call alt_day2_current_game_end_compare_hands                                            # сравнение комбинаций по итогам игры
        if alt_day2_game_played_out == 1:                                                       # по итогам первой игры
            show el normal pioneer far at left with dspr
            if alt_whose_first_move == 'rival':                                                 # если первым ходил соперник
                el "Семён, теперь первым будешь ходить ты."
                $ alt_whose_first_move = 'player'                                               # то первым ходит Семён
            else:                                                                               # если ходил Семён
                el "Право первого хода переходит к %(alt_name_my_rival_d)s."
                $ alt_whose_first_move = 'rival'                                                # то первым ходит соперник
            scene bg int_dining_hall_sunset with dissolve
            jump alt_day2_transition_to_game                                                    # переход к игре
        else:                                                                                   # по итогам тура
            show el normal pioneer far at left with dspr
            el "Семён выигрывает у %(alt_name_my_rival_r)s со счётом %(alt_day2_my_win)d-%(alt_day2_rival_win)d."
            scene bg int_dining_hall_sunset with dissolve
            if alt_tournament_state == "final_start":                                           # если финал
                jump alt_day2_final_win_end_new                                                 # победа в финале
            elif alt_tournament_state == "semifinal_start":                                     # если полуфинал
                jump alt_day2_semifinal_win_end_new                                             # победа в полуфинале
            elif (alt_tournament_state == "1_round_start"):                                     # если первый тур
                jump alt_day2_participate_win_end_new                                           # победа в 1 туре
    else:                                                                                       # соперник выигрывает
        call alt_day2_current_game_end_compare_hands                                            # сравнение комбинаций по итогам игры
        if alt_day2_game_played_out == 1:                                                       # по итогам первой игры
            show el normal pioneer far at left with dspr
            if alt_whose_first_move == 'rival':                                                 # если первым ходил соперник
                el "В следующей игре первым будет ходить Семён."
                $ alt_whose_first_move = 'player'                                               # то первым ходит Семён
            else:                                                                               # если ходил Семён
                el "%(alt_name_my_rival_i)s, теперь первый ход — твой."
                $ alt_whose_first_move = 'rival'                                                # то первым ходит соперник
            scene bg int_dining_hall_sunset with dissolve
            jump alt_day2_transition_to_game                                                    # переход к игре
        else:                                                                                   # по итогам тура
            show el normal pioneer far at left with dissolve
            el "%(alt_name_my_rival_i)s одерживает победу со счётом %(alt_day2_rival_win)d-%(alt_day2_my_win)d."
            scene bg int_dining_hall_sunset with dissolve
            if alt_tournament_state == "final_start":                                           # если финал
                jump alt_day2_final_fail_end_new                                                # поражение в финале
            elif alt_tournament_state == "semifinal_start":                                     # если полуфинал
                jump alt_day2_semifinal_fail_end_new                                            # поражение в полуфинале
            elif (alt_tournament_state == "1_round_start"):                                     # если первый тур
                jump alt_day2_participate_fail_end_new                                          # поражение в 1 туре


#-----------------------------------------------------------------------------------
# Возвращаемся к обратно к игре на соответствующий этап
label alt_day2_transition_to_game:                                                    # переход к игре
    if alt_tournament_state == "final_start":                                         # если финал
        jump alt_day2_final_re_game                                                   # играем финал
    elif alt_tournament_state == "semifinal_start":                                   # если полуфинал
        jump alt_day2_semifinal_re_game                                               # играем полуфинал
    elif (alt_tournament_state == "1_round_start"):                                   # если первый тур
        jump alt_day2_1_tour_re_game                                                  # играем 1 тур

#-----------------------------------------------------------------------------------
# Результат ИГРЫ (сравниваем и оцениваем комбинации)
label alt_day2_current_game_end_compare_hands:                                      # Результат текущей игры
    $ alt_day2_current_rout_status = 0                                              # текущая игра закончена
    if alt_day2_result_current_game == 1:                                           # победа Семёна
        $ alt_day2_summary_poker_1, alt_day2_summary_poker_2 = alt_comparison_poker_hands(alt_my_poker_hand, alt_rival_poker_hand, 'me', alt_spr_my_rival)
        if alt_day2_game_played_out == 1:                                           # сыграли раз
            $ alt_day2_current_rout_status = 1                                      # Семён выиграл 1-ю игру
        elif alt_day2_game_played_out == 2:                                         # сыграли два раза
            if alt_day2_rival_win == 1:                                             # соперник выиграл один раз
                $ alt_day2_current_rout_status = 2                                  # Семён отыгрался

    elif alt_day2_result_current_game == 2:                                         # победа соперника
        $ alt_day2_summary_poker_1, alt_day2_summary_poker_2 = alt_comparison_poker_hands(alt_rival_poker_hand, alt_my_poker_hand, alt_spr_my_rival, 'me')
        if alt_day2_game_played_out == 1:                                           # сыграли раз
            $ alt_day2_current_rout_status = 3                                      # соперник выиграл 1-ю игру
        elif alt_day2_game_played_out == 2:                                         # сыграли два раза
            if alt_day2_my_win == 1:                                                # Семён выиграл один раз
                $ alt_day2_current_rout_status = 4                                  # соперник отыгрался

    $ alt_day2_result_current_game = 0                                              # результат текущей игры = 0 (ничья)
    "%(alt_day2_summary_poker_1)s"
    "%(alt_day2_summary_poker_2)s"

    if alt_day2_current_rout_status in [1,2,3,4]:                                   # если игра не закончена
        call alt_day2_current_game_ending_dialogs                                   # вызов диалога по текущей ситуации
    else:
        pass
    return

#-----------------------------------------------------------------------------------
# диалоги по итогам очередной игры (выиграл/проиграл-сравнял счёт)
# сортировка — сначала по персонажам, потом — по ситуациям (0-проверка, 1 — Семён выиграл 1-ю, 2 — Семен сравнял счёт, 3 — соперник выиграл 1-ю, 4 — соперник сравнял счёт)
# ---------------------------------------------------------
# тут же "накручиваем" скилл соперникам по итогам очередной игры

label alt_day2_current_game_ending_dialogs:
# Лена
    if alt_spr_my_rival == 'un':
        if alt_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
            if alt_day2_gambler_behavior != 'succumb':          # если не "поддавки"
                $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            "Видимо, скилл удачи у Лены прокачан ещё ниже, чем у меня."
            show un smile pioneer at cright with dissolve
            "Но, похоже, её это не слишком расстраивает."
            un "Молодец."
            "Похвалила Лена."
            me "Спасибо."
            show un shy pioneer at cright with dspr
            "И через секунду залилась краской."


        elif alt_day2_current_rout_status == 2:                 # если Семён отыгрался
            if alt_day2_gambler_behavior != 'succumb':          # если не "поддавки"
                $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            show un shy pioneer at cright with dissolve
            "Взгляд Лены метался от меня и до лежащих на столе карт, и так несколько раз."
            "Она явно хотела что-то сказать, но не могла перебороть смущение."
            "Не понимаю, что могло вогнать эту, пару минут назад серьёзную, девочку в краску."
            dreamgirl "Идиот."
            "Буркнуло подсознание."
            "В любом случае, тянуть из Лены слова клещами я не стану."


        elif alt_day2_current_rout_status == 3:                 # и она выиграла первый раз
            if alt_day2_gambler_behavior == 'succumb':          # если "поддавки"
                $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            if alt_day2_gambler_behavior == 'succumb':
                "Мда. Я показал явно не лучший уровень игры. И Лена явно это заметила."
                show un serious pioneer at cright with dissolve
                "Её осуждающий взгляд пробудил во мне неясное чувство вины."
                "Будто я виноват в том, что проиграл."
                dreamgirl "Ещё как виноват."
                dreamgirl "Девочка поддавалась тебе, но ты всё равно облажался."
                th "Доказательства?"
                dreamgirl "Налицо."
                "Неясно ответил внутренний голос и замолчал."
            else:
                "Лена оказалась серьёзным противником, спрятавшим пару тузов в рукаве."
                show un shy pioneer at cright with dissolve
                "Не ожидал от неё такого упорства."
                "Видимо, она и сама была удивлена."


        elif alt_day2_current_rout_status == 4:                 # и она отыгралась
            if alt_day2_gambler_behavior == 'succumb':          # если "поддавки"
                $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            if alt_day2_gambler_behavior == 'succumb':          # если "поддавки"
                show un sad pioneer at cright with dissolve
                "Сама Лена не слишком радовалась маленькой победе — наоборот, она глядела на меня так, словно провинилась в чём-то."
                dreamgirl "Не будь дубом и приободри."
                th "Без тебя знаю."
                me "Молодец, Лен. Хорошо сыграла."
                show un shy pioneer at cright with dspr
                un "С-спасибо."
                "Голос у девочки взволнованный, она не верила в то, что произошло."
                "Потому и вздрогнула, когда Электроник громко произнёс её имя."
            else:
                "Похоже, Лена не намерена сдаваться."
                show un smile pioneer at cright with dissolve
                un "Не надейся на лёгкую победу."
                "Только что она сидела, смутившись, а теперь ещё подзадоривает меня!"
                "Вот что азарт с людьми делает."
                show un shy pioneer at cright with dspr
                "Впрочем, эффект оказался недолгим."

# Славя
    elif alt_spr_my_rival == 'sl':
        if alt_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            show sl smile pioneer at cright with dissolve
            "Похоже, что Славя нисколько не огорчена поражением."
            sl "Всё-таки карты не моё."
            me "Тебе просто не повезло, вот и всё."
            show sl laugh pioneer at cright with dspr
            sl "Дело не в везении, я правда не умею!"
            show sl smile2 pioneer at cright with dspr
            sl "Много раз пробовала, всё без толку."
            sl "Не понимаю я смысла этой глупой игры."
            me "Так зачем играешь?"
            show sl smile pioneer at cright with dspr
            sl "Лагерное мероприятие, Семён. Все обязаны присутствовать."






        elif alt_day2_current_rout_status == 2:                 # если Семён отыгрался
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            show sl smile pioneer at cright with dissolve
            sl "Ведь можешь же, когда захочешь!"
            me "Мне просто повезло."
            show sl normal pioneer at cright with dspr
            "Славя явно хотела услышать от меня большего, но я не знал, что тут ещё добавить."
            sl "Вот сейчас и узнаем — везение или талант."
            th "Второе, однозначно."
            th "Талантливый неудачник."
            "Славя словно услышала мои мысли и постаралась приободрить меня."
            show sl happy pioneer at cright with dspr
            sl "Выше нос!"



        elif alt_day2_current_rout_status == 3:                 # и она выиграла первый раз


            show sl surprise pioneer at cright with dissolve
            me "Что-то не так?"
            show sl normal pioneer at cright with dspr
            sl "Нет, просто…"
            sl "Я не очень хорошо играю в карты."
            me "Насколько «не очень»?"
            show sl sad pioneer at cright with dspr
            sl "Много раз пробовала, всё без толку."
            sl "Не понимаю я смысла этой глупой игры."
            "А мне казалось, что хуже меня игрока здесь нет."
            "Активистка преуспела во многом, кроме азартных игр."
            "Но даже она смогла меня обыграть."

        elif alt_day2_current_rout_status == 4:                 # и она отыгралась

            show sl angry pioneer at cright with dissolve
            sl "Ты нарочно, да?"
            "А я, стараясь сохранить невозмутимое выражение лица, ответил:"
            me "Нисколько."
            sl "Неправда! Ты же знаешь, что я…"
            pause(1)
            show sl normal pioneer at cright with dspr
            sl "Ладно, не важно."

# Алиса
    elif alt_spr_my_rival == 'dv':
        if alt_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            show dv surprise pioneer2 at cright with dissolve
            "Рыжая находилась в лёгком шоке."
            "Что тут скажешь — я умею удивлять.{w} Особенно себя."
            me "Мадмуазель готова пасть на колени и рыдать от поражения?"
            show dv smile pioneer2 at cright with dspr
            "Моя реплика вывела Алису из оцепенения и раззадорила."
            dv "Ещё чего!"
            show dv angry pioneer2 at cright with dspr
            dv "Мадмуазель готова съездить кавалеру по физиономии."
            "Я едва не расхохотался."

        elif alt_day2_current_rout_status == 2:                 # если Семён отыгрался
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык
            $ alt_day2_gambler_behavior = 'gamble'          # и начинает рисковать

            show dv guilty pioneer2 at cright with dissolve
            "Приятно видеть, как маска надменности спадает с лица Двачевской."
            "Я даже говорить ничего не стал — молча подобрал эту самую маску и примерил на себя."
            show dv angry pioneer2 at cright with dspr
            "Алисе это не понравилось, Алиса сжала кулаки."
            if herc or loki:
                "А мне плевать."
                "Угрозы Двачевской меня не пугают."
                "Я с вызовом продолжил глядеть на рыжую."
                pause(1)
                show dv guilty pioneer2 at cright with dspr
                "Победителем в гляделки стал я."
                "Алиса разжала кулаки и отвела взгляд."
                if herc:
                    "Мне даже стало немного стыдно за то, что, кажется, обидел девушку."
                    "Но не настолько, чтобы торопиться извиняться."
                    "Алиса должна сама понять, что сделала не так."

                elif loki:
                    dreamgirl "Ну вот, обидел девочку."
                    th "Она заслужила, ибо нефиг."

            else:
                "Я поднял руки в примирительном жесте."
                me "Тише-тише, я просто пошутил."
                dv "Ещё одна такая шутка…"
                me "Понял, не дурак."




        elif alt_day2_current_rout_status == 3:                 # и она выиграла первый раз
            $ alt_day2_gambler_behavior = 'defense'              # садится в оборону

            show dv grin pioneer2 at cright with dissolve
            "Алиса с ехидной усмешкой глядела на меня."
            "Наверняка радуется, что получила подтверждение своим словам."
            "И это бесит."
            me "Не рановато празднуешь победу, Двачевская?"
            show dv laugh pioneer2 at cright with dspr
            dv "По-моему — нет."
            "Я уже собрался плюнуть ядом в рыжую, как услышал реплику внутреннего голоса."
            dreamgirl "Балда, она же специально провоцирует тебя, а ты ведёшься!"
            dreamgirl "Если хочешь утереть нос Двачевской, тебе нужно сохранять спокойствие."
            th "В этом есть смысл."
            show dv normal pioneer2 at cright with dspr
            "Алиса как-то разочарованно хмыкнула — явно ждала другой реакции."
            th "А вот фиг тебе."

        elif alt_day2_current_rout_status == 4:                 # и она отыгралась
            $ alt_day2_gambler_behavior = 'gamble'          # и начинает рисковать

            show dv laugh pioneer2 at cright with dissolve
            "Дваче чертовски довольна собой."
            me "Чего лыбу давишь?"
            show dv grin pioneer2 at cright with dspr
            dv "А нельзя?"
            dreamgirl "Можно!"
            th "Ты вообще на чьей стороне?"
            dreamgirl "Своей собственной."
            dreamgirl "А ты, балбес, не понял, что девочка заигрывает с тобой."
            th "Двачевская? Заигрывает?"
            th "Никогда не поверю. Не тот типаж."
            dreamgirl "Пф… Больно ты в них разбираешься."
            "Фыркнул внутренний голос и смолк."

# Мику
    elif alt_spr_my_rival == 'mi':

        if alt_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            stop music fadeout 2
            show mi smile pioneer at cright with dissolve
            mi "Молодец, Сенечка. Ты хорошо играешь."
            play music music_7dl["what_am_i_doing_here"] fadein 1
            me "Это всё везение."
            show mi shocked pioneer at cright with dspr
            mi "Правда? А я решила, что ты — опытный игрок."
            "Если у Мику такая тактика — наносить каждым словом удар по моей самооценке — у неё это получилось."
            dreamgirl "Можно подумать, она у тебя была."
            show mi sad pioneer at cright with dspr
            mi "А мне вот совсем не везёт в карты."
            mi "Я не умею в них играть! Не понимаю!{w} Или просто глупая."
            me "Ты не глупая."
            "Хотя мы не так хорошо знакомы, чтобы я мог это утверждать."
            dreamgirl "Так узнай её {i}поближе{/i}."
            "По спине аж мурашки прошли."
            "Закравшиеся в голос внутреннего пошляка интонации напомнили о нашей очаровательной медсестре."

            me "Просто у каждого человека что-то получается лучше, чем у другого."
            if loki:
                me "Я не понаслышке знаю, что научиться играть даже на одном инструменте непросто, а ты смогла сразу на нескольких."
                me "Это не просто талант, это упорный труд."
                me "Глупые такого не умеют."
                me "Как правило они…"
                "Слова комом застряли в горле."
                mi "Как правило — что?"
                me "Трудности их быстро ломают."
                th "Порой ещё и физически."
                me "Они застревают на одном месте и найдут тысячу оправданий, чтобы ныть о несбывшемся вместо хотя бы одной причины двигаться вперёд, к своей мечте."
                dreamgirl "Прямо как?.."
                th "Прямо как я."
            elif herc:
                me "Например у меня не сложилось с музыкой."
                th "Зато во владении холодным и огнестрельным оружием я преуспел."
                me "А у тебя получилось."
                me "Талант то или упорство — не суть."
                me "Глупые такого не умеют."
            elif dr:
                me "Азартные игры не твоё. Только и всего."

            mi "Наверное, ты прав."
            show mi smile pioneer at cright with dspr
            mi "Нет, так и есть!"
            show mi smile pioneer at cright with dspr
            mi "Вот уж кто действительно умеет играть в карты, так это Алиса."
            "Двачевская-то?"

            scene bg ext_dining_hall_near_day
            show dv smile pioneer2
            show prologue_dream
            with flash

            "Нисколько не сомневался."
            "Человек с такой самодовольной миной не стал бы предлагать пари, будучи не уверенным в победе."
            if (alt_day2_dv_ultim != 1) and (alt_day2_walk == 1):
                dreamgirl "А что ж ты тогда спорить-то не стал, шулер?"

            scene bg int_dining_hall_sunset
            show mi shy pioneer at cright
            with flash

            show mi normal pioneer at cright with dspr
            mi "Мы с ней как-то играли, и я проиграла шесть раз подряд!"

            menu:
                "Спросить про игру":

                    $ lp_mi += 1

                    me "Ты и в карты? С Двачевской?"
                    me "Ты, как там по вашему… камикадзе?!"
                    show mi laugh pioneer at cright with dspr
                    mi "Скажешь тоже! Оно само как-то так вышло!"
                    "Видимо это норма, что у женщин «оно» всегда само."
                    show mi normal pioneer at cright with dspr
                    mi "Я тогда сидела в клубе и расписывала ноты одной из моих песен для пианино."
                    mi "Очень красиво получилось. По-моему, даже лучше, чем в оригинале. Мелодичнее, эмоциональнее!"
                    show mi smile pioneer at cright with dspr
                    mi "Так вот, точно помню, что то была среда!"
                    show mi surprise pioneer at cright with dspr
                    mi "Хотя нет, меня в тот день Ульяна…"
                    "Я уже начал жалеть, что решил поддержать диалог, перешедший в монолог, когда Мику сама вернулась к теме."
                    show mi normal pioneer at cright with dspr
                    mi "В общем, неважно!"

                    scene bg int_musclub_day
                    show prologue_dream
                    with flash

                    mi "Я уже почти закончила с песней…"
                    mi "…как вдруг в клуб ворвалась взъерошенная Алиса!"

                    play sound sfx_open_door_strong
                    with vpunch
                    show dv scared pioneer2 far at center behind prologue_dream
                    with moveinright

                    dv "{i}Если Шляпа зайдёт — меня тут нет!{/i}"

                    hide dv with moveoutleft
                    play sound sfx_close_door_clubs_nextroom
                    with vpunch

                    mi "И спряталась в подсобке."

                    scene bg int_dining_hall_sunset
                    show mi shocked pioneer at cright
                    with fade

                    mi "Я сначала перепугалась: что такого сделала Алиса, чтобы настолько сильно испугаться вожатой?"
                    show mi happy pioneer at cright with dspr
                    mi "Ольга Дмитриевна же не злая. Она строгая, но добрая."
                    "Мику — прямо сама наивность."
                    dreamgirl "Воспользуешься?"
                    th "У тебя, смотрю, всё сплошные хиханьки да хаханьки, да всё об одном."
                    dreamgirl "О добром, вечном."
                    show mi dontlike pioneer at cright with dspr
                    mi "В общем, Алиса меня напугала."
                    show mi upset pioneer at cright with dspr
                    mi "Я замерла и всё прислушивалась: вдруг действительно кто-то идёт?"
                    show mi normal pioneer at cright with dspr
                    mi "Минут десять так сидела, пока Алиса не решила выбраться из укрытия."
                    show mi laugh pioneer at cright with dspr
                    mi "Ты бы видел её лицо!"
                    me "Представляю…"

                    scene bg int_musclub_day
                    show prologue_dream
                    with flash
                    show dv surprise pioneer2 at fleft behind prologue_dream with moveinleft
                    show dv surprise pioneer2 at fleft behind prologue_dream with dissolve
                    show dv normal pioneer2 at fleft behind prologue_dream with dspr

                    mi "Когда Алисочка собралась уходить, я её спросила:"
                    show dv normal pioneer2 at cright behind prologue_dream with move
                    mi "{i}Ой, Алиса, а что ты натворила? Зачем Ольге-сан тебя искать?{/i}"
                    show dv smile pioneer2 at cright behind prologue_dream with dspr
                    mi "В ответ она просто отмахнулась, представляешь!"
                    mi "Сказала, что потом как-нибудь расскажет, что у неё дело какое-то незаконченное."
                    "Ставлю на то, что Двачевская тупо отмазывалась."
                    "Болтливость Мику отталкивает людей."
                    mi "{i}А что за дело? Срочное? Могу я…{/i}"
                    show dv laugh pioneer2 at cright behind prologue_dream with dspr
                    dv "{i}Нет. Это секрет!{/i}"
                    mi "{i}Ну Алиса-а-а! Мне же интересно. Ну расскажи!{/i}"
                    show dv grin pioneer2 at cright behind prologue_dream with dspr
                    dv "{i}А давай пари?{/i}"
                    dv "{i}Выиграешь у меня, и я расскажу, что за дело.{/i}"
                    mi "И достала карты."
                    mi "{i}Ой, а я не умею. То есть я никогда не пробовала, поэтому…{/i}"
                    show dv smile pioneer2 at cright behind prologue_dream with dspr
                    dv "{i}Не страшно!{/i}"
                    show dv laugh pioneer2 at cright behind prologue_dream with dspr
                    dv "{i}Не хочешь — научим. Не можешь — заставим!{/i}"

                    scene bg int_dining_hall_sunset
                    show mi smile pioneer at cright
                    with flash2

                    mi "Вот такая вот история."
                    show mi smile pioneer at cright with dspr
                    mi "Алиса пыталась меня по ходу игры научить, но я так ничего и не поняла!"
                    me "Ясно."
                    $ lp_dv += 1
                    me "А Двачевская — не такая вредина, какой выглядит."
                    stop music fadeout 3
                    mi "Алисочка очень хорошая. Просто её нужно получше узнать."

                "Игнорировать":

                    $ lp_mi -= 1
                    stop music fadeout 3
                    me "Ясно."
                    show mi sad pioneer at cright with dspr
                    pause(1)
                    hide mi with dissolve

                    #if not(final):
                    #    "Я отвернулся к другим столам, посмотреть, как играет кто-нибудь из моих потенциальных соперников."
                    #    "Мику по ряду причин в их число уже не входила." # это же промежуточные итоги, Мику вполне может ещё отыграться

            play music music_list["my_daily_life"] fadein 2

        elif alt_day2_current_rout_status == 2:                 # если Семён отыгрался
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            show mi smile pioneer at cright with dissolve
            "Мику нисколько не расстроилась из-за проигрыша."
            mi "Молодец, Сенечка, хорошо отбился."
            show mi upset pioneer at cright with dspr
            mi "Так, раз ты выиграл, теперь нас ждёт финальный раунд, верно?"
            "Уточнила Мику."
            show mi laugh pioneer at cright with dspr
            mi "Пускай мы товарищи, но поддаваться я не буду!"
            "Услышав впервые, я не придал этому особого значения и пропустил мимо ушей, однако…" # Возможен исход, при котором здесь "Сенечка" упоминается впервые. Лучше убрать эту строку вообще. ## Нет, здесь Семён отыгрался, значит, первый раз должна была выиграть Мику (см. alt_day2_current_rout_status == 3). Там Сенечка упоминается 2 раза.
            me "Мику, а почему «Сенечка»?"
            show mi shocked pioneer at cright with dspr
            mi "А?"
            show mi shy pioneer at cright with dspr
            "Изменение цвета лица обнаружено."
            "Не думал, что простым вопросом получится смутить нашу японку."
            show mi happy pioneer at cright with dspr
            mi "Потому что Семён слишком грубо и официально, а Сенечка звучит приятно."

        elif alt_day2_current_rout_status == 3:                 # и она выиграла первый раз
            show mi shy pioneer at cright with dissolve
            mi "Я победила?"
            me "Да."
            show mi happy pioneer at cright with dspr
            mi "Ура!"
            show mi smile pioneer at cright with dspr
            mi "Сенечка, ты только не переживай — в поражении нет ничего плохого."
            mi "Я тоже до конца не поняла, как играть в эту игру. Можно сказать, что мне повезло."
            me "Угу."
            show mi sad pioneer at cright with dspr
            mi "Ты всё-таки расстроился. Не переживай, поражение — тоже опыт."
            show mi smile pioneer at cright with dspr
            mi "Но я понимаю тебя. Я тоже расстроилась, когда проиграла Алисе в карты."
            th "Мику играла с Алисой в карты?"
            dreamgirl "А ты думал, что весь мир вертится вокруг тебя, и обитатели лагеря только и ждут, когда Его Величество появится на горизонте?"
            dreamgirl "У каждого своя жизнь, своя история, и она не начинается с твоим появлением, не обрывается с твоим уходом."
            dreamgirl "Нужна ли она тебе — вопрос важный, но отдельный."
            show mi serious pioneer at cright with dspr
            th "Тебе не кажется, что ты до черта умничаешь?"
            dreamgirl "Из нас двоих только я использую мозги по их прямому назначению."
            dreamgirl "А раз в нашем дуэте роль костыля для душевного инвалида выпала мне, вот тебе ещё один совет — хватит болтать с самим собой и поговори уже с девушкой."
            show mi normal pioneer at cright with dspr
            mi "Сенечка, всё хорошо? У тебя глаз дёргается."
            me "В порядке. Давай дальше."

        elif alt_day2_current_rout_status == 4:                 # и она отыгралась
            show mi surprise pioneer at cright with dissolve
            "Хафу долго всматривалась в карты и не могла понять очевидного."
            "К нам даже подошёл Электроник, утвердительно кивнув ей."
            show mi normal pioneer at cright with dspr
            mi "Я победила?"
            me "Да."
            show mi happy pioneer at cright with dspr
            mi "Ура!"

            if alt_result_dv_1_tour > 2 and alt_result_dv_semifinal > 2:
                show mi laugh pioneer at cright with dspr
                mi "Алиса! Вот видишь, я умею играть! Я смогла отыграться!"
                "Рыжая бестия за соседним столом аж покраснела."
                "На месте Алисы я бы не залился краской, а сделал вид, что не знаю Мику."

            show mi grin pioneer at cright with dspr
            mi "Ну держись, Сенечка! Сейчас я выиграю тебя!" # "Выиграю тебя" — так задумано или меняем на "обыграю"? ## задумано
            show mi smile pioneer at cright with dspr
            me "Ага, удачи."
            dreamgirl "Зря, она тебе понадобится."
            th "Сомневаешься в моих способностях?"
            dreamgirl "Я всё-таки одну голову с тобой делю. Так что не сомневаюсь — знаю."

# Ульяна
    elif alt_spr_my_rival == 'us':
        if alt_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            show us angry pioneer at cright with dissolve
            us "Почему ты не поддался мне?!"
            me "С чего бы это?"
            us "С того, что я ребёнок, а ты взрослый! Ты должен поддаваться!"
            me "С точки зрения закона я тоже все ещё ребёнок."
            dreamgirl "Почти встретивший третий десяток ребёнок."
            th "Цыц!"
            "Однако рыжую нужно как-то успокоить."
            "У неё аж венка на лбу набухла. Того гляди запрыгнет на стол и начнёт колотить меня."
            if herc:
                dreamgirl "А ты её «хоп!» — в медвежий захват — и броском назад!"
                th "Меня не для того учили, чтобы детей избивать!"
                th "Захвата за большой палец будет более чем достаточно…"
            me "Успокойся, это только первый раунд."
            me "У тебя ещё будет возможность отыграться, а с моей удачей шансы весьма высоки."
            show us dontlike pioneer at cright with dspr
            us "Смотри у меня, а не то…"
            if herc or loki:
                me "Не то что?"
                dreamgirl "Сколопендру тебе в штаны запустит, вот что."
                th "Мне так страшно, что уже поджилки трясутся."
            else:
                me "Не то что?.."
                "Я старался добавить в голос побольше уверенности, но получалось откровенно слабо."
                dreamgirl "Да брось, ты в самом деле перепугался мелкой девки?"
                dreamgirl "Ну засунет тебе сколопендру в штаны, и что? Смертельно?"
                th "Всегда ожидай худшее, чтобы радоваться лучшему."
            show us grin pioneer at cright with dspr
            if (counter_sl_7dl == 0) and dr:
                us "А то снова оболью!"
            else:
                us "Узнаешь!"
            us "Если не отдашь мне все лучшие карты, что у тебя есть."
            me "Идёт."
            dreamgirl "Серьёзно?"
            if loki:
                th "Может быть."
            elif herc:
                th "Посмотрю на её поведение."
            else:
                th "Рандом нам судья."

        elif alt_day2_current_rout_status == 2:                 # если Семён отыгрался
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            show us dontlike pioneer at cright with dissolve
            us "Нечестно!"
            if renpy.random.randint(1, 95) == 1:
                me "А ты задонатила на победу?"
                us "Чего, это как?"
                me "Пожертвование, мелкая."
                us "Не буду я тебе до… да… жертвовать."
                us "Ты же не больной, руки-ноги целы."
                us "Пожертвования тебе не нужны."
                me "Зря. В моём…"
                "Я осёкся."
                "Чуть не сказал Ульяне «в моём времени»."
                "В её же времени о таком не слышали, но наверняка пресекалось бы и считалось тунеядством."
                "Никогда не понимал таких людей, что в этом такого?"
                "Очередной вид заработка же."
                "Не всем же стоять по восемь часов у станка, есть бойцы интеллектуального фронта."
                dreamgirl "Этого милого светлого мальчика зовут Семён."
                dreamgirl "Ему срочно нужна ваша помощь!"
                dreamgirl "Он страдает от тяжелого и неизлечимого заболевания."
                dreamgirl "Он — ох…"
            elif loki:
                "Соблазн вернуть шпильку оказался слишком велик."
                me "Ну ты же сама говорила, что игра простенькая и только дурак не поймёт."
                show us angry pioneer at cright with dspr
                "О да, вздувшаяся венка на лбу рыжей стала бальзамом на душу."
                "А как только мелкая поколотит меня, возможно, ногами, он мне потребуется ещё и для тела."
                "К счастью, меня спас вовремя подавший голос Электроник."
            elif herc:
                me "Не всё в мире измеряется честностью."
                us "{i}Не всё в мире измеряется честностью.{/i}"
                "Передразнила Ульяна."
                show us grin pioneer at cright with dspr
                us "Жди честного таракана под подушкой."
            elif dr:
                th "Я выиграл по воле Рандома, а понятие честности к нему не применимо."
                dreamgirl "Скажи это вслух — и получишь заслуженный удар по коленке или таракана в суп."
                th "Вот поэтому я лучше промолчу."
                "Ульяна угрожала тараканами под подушкой или подкараулить и облить из ведра с водой."
                "Я молча кивал изредка поддакивая."
                show us normal pioneer at cright with dspr
                "В конце концов рыжая сменила гнев на милость."
                show us grin pioneer at cright with dspr
                "Но, если я каким-то образом выиграю ещё и в финальном раунде, меня ждёт…{w=0.5} что-то нехорошее."
                "Такие вот дела."

        elif alt_day2_current_rout_status == 3:                 # и она выиграла первый раз

            show us surp1 pioneer at cright with dissolve
            us "Вот это да! А я и не думала, что такое бывает!"
            me "Какое такое?"
            us "Ну как? Как можно так плохо играть? Игра же простенькая!"
            show us laugh pioneer at cright with dspr
            us "Только такой зануда, как ты, не поймёт."
            th "Зараза мелкая!"

            if (counter_sl_7dl >= 1) or dr:
                "И ведь как мне хотелось ответить что-то токсичное, но ведь глупо это, обижаться на ребёнка, правда?"
                dreamgirl "Внешность бывает обманчива. Взгляни на неё и себя и сравни."
                dreamgirl "Разница в возрасте несущественная."
                th "Ты на что это намекаешь?"
                "Внутренний голос ответил молчанием."

            else:

                if loki:
                    me "Может, тебя ещё раз водичкой окатить? Пыл поумерить?"
                    show us grin pioneer at cright with dspr
                    us "А ты попробуй догони!"
                    me "Я возьму не скоростью, а хитростью."
                    show us smile pioneer at cright with dspr
                    me "Вот будешь одна в домике, я тихонько подкрадусь сзади, и…"

                elif herc:
                    me "С витамином «Р» знакома?"
                    show us smile pioneer at cright with dspr
                    us "Нет! А что это?"
                    me "Продолжай в том же духе…"
                    "Рука легла на пряжку ремня."
                    me "…узнаешь."
                    show us grin pioneer at cright with dspr
                    us "Хорошо!"




        elif alt_day2_current_rout_status == 4:                 # и она отыгралась

            show us grin pioneer at cright with dissolve
            us "Молодец, Сёмка. Ты на пути к исправлению!"
            "Похвалила Ульянка."
            dreamgirl "Ты всё-таки дурак."
            th "Ну, может, оно и к лучшему."
            dreamgirl "Просто напомню: игра ещё не закончена."

# Шурик
    elif alt_spr_my_rival == 'sh':
        $ alt_day2_gambler_skill += 1                     # увеличиваем навык — Шурику без вариантов

# ============================================================= эксперименты Шурика
        if alt_day2_current_rout_status in [3,4]:                               # Если Шурик выиграл игру
            pass
        else:                                                                   # если Шурик проиграл игру
            if alt_day2_gambler_behavior == 'defense':                          # если Шурик защищался
                $ alt_day2_gambler_behavior = 'gamble'                          # смена стратегии
            elif alt_day2_gambler_behavior == 'gamble':                         # если Шурик рисковал
                $ alt_day2_gambler_behavior = 'defense'                         # смена стратегии
# =============================================================

        if alt_day2_current_rout_status == 1:                   # если Семён выиграл первый раз

            show sh surprise pioneer at cright with dissolve
            sh "Недооценил я тебя."
            me "Ну спасибо."
            show sh smile pioneer at cright with dspr
            sh "Даже при моей достаточной высокой вероятности победить тебе выпали карты, которые меня разгромили."
            "Он что, пытался высчитать, какие у меня карты?"
            "Рандом не щадит таких."
            show sh serious pioneer at cright with dspr
            "Шурик протянул мне руку в знак уважения."
            if herc:
                "Я ответил."
                show sh upset pioneer at cright with dspr
                "Когда пионер слегка поморщился, я понял, что немного перестарался."
                "Ещё подумает, что пытаюсь вывести его из игры."
                dreamgirl "А ты «не»?"
                th "Да какой в этом смысл? Мы же не в покер на деньги играем."
            elif loki:
                "Я всегда брезгливо относился к рукопожатиям и не стал отвечать."
                show sh normal pioneer at cright with dspr
                "Кибернетик на это лишь хмыкнул и пожал плечами."
            else:
                "Я неуверенно взял его за руку и поморщился."
                show sh smile pioneer at cright with flash_red
                th "Словно в тисках сжали."
                th "Он это специально, не иначе."
                dreamgirl "Нет, просто ты дрищ."


        elif alt_day2_current_rout_status == 2:                 # если Семён отыгрался

            show sh serious pioneer at cright with dissolve
            sh "Недооценил я тебя."
            th "Не только ты."
            me "Ну спасибо."
            sh "Даже при моей достаточной высокой вероятности победить тебе выпали карты, которые меня разгромили."
            "Шурик протянул мне руку в знак уважения."
            if herc:
                "Я ответил."
                show sh upset pioneer at cright with dspr
                "Когда пионер слегка поморщился, я понял, что немного перестарался."
                "Ещё подумает, что пытаюсь вывести его из игры."
                dreamgirl "А ты «не»?"
                th "А ты вообще помалкивай, предатель! Я тебе слова не давал."
                dreamgirl "Больно мне нужно твоё разрешение."
                dreamgirl "Впрочем, сейчас посмотрим, что это было: удача или ты действительно что-то умеешь."
            elif loki:
                "Я всегда брезгливо относился к рукопожатиям и не стал отвечать."
                show sh normal pioneer at cright with dspr
                "Кибернетик на это лишь хмыкнул и пожал плечами."
                dreamgirl "К победе по чужим головам?"
                th "Не думаю. Он настроен серьёзнее и имеет все шансы победить."
                dreamgirl "Значит, сдался."
                th "Нет. Просто так не проиграю — пусть выцарапывает себе победу."
            else:
                "Я неуверенно взял его за руку и поморщился."
                show sh upset pioneer at cright with flash_red
                th "Словно в тисках сжали!"
                "Уж что-что, а это я умею — при 99%% шансе вытянуть несчастливый билет."
                "Мои мучения в турнире могли уже закончиться."






        elif alt_day2_current_rout_status == 3:                 # и он выиграл первый раз

            show sh normal pioneer at cright with dissolve
            sh "Хм, а ведь сработало…"
            me "Что?"
            show sh surprise pioneer at cright with dspr
            sh "А?"
            show sh normal pioneer at cright with dspr
            sh "Да я попробовал применить формулы расчёта вероятности более выигрышной комбинации у противника в покере к этой игре."
            sh "Пришлось, конечно, кое-что поправить, но и полученного результата хватило понять, что карты у тебя не лучше."
            "Он что, просто высчитал это? Увидев не больше половины?"
            dreamgirl "Будь с ним осторожен. Он не так прост, как кажется."
            th "Я уже заметил. Ты очень полезен."
            th "Лучше бы подсказал, как против такого играть."
            dreamgirl "Собрался выигрывать?"
            th "Есть другие варианты?"
            th "Встать из-за стола и просто уйти мне не дадут. А поддаваться глупо."
            dreamgirl "У тебя всё равно нет шансов."
            th "Рандом мне судья, а не ты."

        elif alt_day2_current_rout_status == 4:                 # и он отыгрался

            show sh smile pioneer at cright with dissolve
            sh "Хм, а ведь сработало…"
            me "Да что ты всё считаешь-то?"
            show sh upset pioneer at cright with dspr
            sh "А?"
            show sh normal pioneer at cright with dspr
            sh "Да я пробую применить формулы расчёта вероятности более выигрышной комбинации у противника в покере к этой игре."
            sh "Приходится, конечно, кое-что править, но и при таких условиях результат даёт представление о твоих картах."
            "Не видя и половины, он предсказывает весь набор?"
            "Не верю. Мистика какая-то."
            dreamgirl "Кто бы говорил…"

# Женя
    elif alt_spr_my_rival == 'mz': # Ей скилл не повышается, потому что foolplay? ## Ну ды
        show mz normal glasses pioneer at cright with dissolve
        if alt_day2_current_rout_status == 1:                   # если Семён выиграл первый раз

            "Жужа даже бровью не повела."
            "Эмоциональный штиль. «Покерфейс»."
            "Даже досадно немного. Могла бы изобразить хоть подобие разочарования."
            mz "Что?"
            me "Жень, а как ты сюда вообще попала?"
            me "По тебе заметно, что ты не в восторге."
            show mz angry glasses pioneer with dspr
            mz "Сюда — это куда? В лагерь? В библиотеку? Турнир? Мир?"
            mz "Задавай конкретные вопросы, если хочешь получить конкретный ответ."
            "Тяжелый человек."
            if herc or loki:
                "И почему мне так часто встречаются именно такие?"
                dreamgirl "Подобное притягивает подобное?"
                me "Если у меня найдётся время, я зайду к тебе на чашечку чая, и мы поговорим о чём угодно."
                me "О вождях пролетариата, о полёте на Марс или «Мартине Идене» Лондона."
                show mz rage glasses pioneer with dspr
                me "Да хоть свои детские фото, где ты в пелёнках, покажи."
                me "А пока мне интересно третье."
                me "Сделай одолжение простому смертному и поведай свой секрет."
                "Я ожидал от Жужелицы всякого: что она вскочит и даст мне по морде, что она заорёт на весь зал."
                "Да даже, что она пожалуется вожатой и потребует отпустить её в медпункт, так как она получила психологическую травму, и ей теперь требуется отдых."
                show mz laugh glasses pioneer with dspr
                pause(.5)
                show mz normal glasses pioneer with dspr
                "А она улыбнулась."
                "Всего на миг, но я готов поклясться, что видел это."
                dreamgirl "Чудеса!.. Ой, чудеса!.."
                mz "Вожатая."
                mz "Пришла и отчеканила: отрядное мероприятие, присутствуют все, возражения не принимаются."
                me "Ох уж эта Ольга Лен…{w=0.3} Дмитриевна."
            else:
                me "Неважно."
                "Буркнул я."
                show mz normal glasses pioneer with dspr
                "До чего ж вредный человек."
                "У Жени проблем в общении побольше, чем у меня."
                dreamgirl "А ты попробуй раскрутить её на разговор."
                dreamgirl "Вдруг узнаешь её с другой стороны."
                dreamgirl "А потом она позовёт тебя на чай в библиотеку, а там, среди стеллажей, книги посыплются с полок под громкие сто…"
                th "Нет!" with vpunch
                show mz bukal glasses pioneer with dspr
                mz "Псих."
                "Фыркнула Женя."
                dreamgirl "Если ты думаешь, то что затрещина поможет избавиться от меня, очень ошибаешься."
                th "Бла-бла-бла! Я тебя не слы-ышу-у-у!"
                dreamgirl "Идиот…"

        elif alt_day2_current_rout_status == 2:                 # если Семён отыгрался

            show mz normal glasses pioneer with dissolve
            mz "Продолжай в том же духе."
            "Если б это от меня зависело."
            me "Ничего не обещаю, но постараюсь."
            mz "Угу, постарайся."
            hide mz with dissolve

        elif alt_day2_current_rout_status == 3:                 # и она выиграла первый раз

            show mz bukal glasses pioneer at cright with dissolve
            "Сама победительница первого раунда устало вздохнула."
            "Если ей настолько не интересно, зачем вообще соглашалась?"
            "Могла же прикрыться занятостью в библиотеке перед вожатой."
            mz "У меня что-то на лице?"
            "Вяло спросила она."
            th "Скорее — отсутствие."
            "Подумал я, отвечая:"
            me "Нет, я просто задумался."
            show mz normal glasses pioneer at cright with dspr
            mz "Ясно."


        elif alt_day2_current_rout_status == 4:                 # и она отыгралась


            show mz bukal glasses pioneer at cright with dspr
            if herc or loki:
                "Женя сокрушенно выдохнула."
            else:
                "У жужелицы было такое лицо, словно оно впитало в себя все муки мира."

            mz "Сделай одолжение — не облажайся в следующем раунде."
            me "Если б это от меня зависело."
            mz "От кого ещё это может зависеть?"
            mz "Только не говори глупости вроде «бога»."
            "Пренебрежение, чуть ли не с ненавистью в голосе."
            "Истинная коммунистка!"
            th "Или это что-то личное?"
            me "И в мыслях не было."
            th "Рандом — он не бог. Он выше."
            show mz angry glasses pioneer at cright with dspr
            mz "Вот и славно."

    show el normal pioneer far at left with dissolve
    if alt_day2_current_rout_status == 1:
        el "В этой игре победил Семён, счёт 1-0 в его пользу."
    elif alt_day2_current_rout_status == 3:
        if alt_spr_my_rival == 'sh':                            # Шурик
            el "В этой игре победил Шурик, счёт 1-0 в его пользу."
        else:
            el "В этой игре %(alt_name_my_rival_i)s побеждает и ведёт в партии со счётом 1-0."
    elif alt_day2_current_rout_status == 2:
        el "Семён выигрывает и сравнивает счёт в раунде."
    elif alt_day2_current_rout_status == 4:
        if alt_spr_my_rival == 'sh':                            # Шурик
            el "Шурик выигрывает и сравнивает счёт в раунде."
        else:
            el "%(alt_name_my_rival_i)s победила и сравняла счёт в партии."
    return

#-----------------------------------------------------------------------------------
# Результат КОНА
label alt_day2_summary_poker_round:
    if alt_day2_result_tour in [1,11,21]:                                                              # Если проигрыш в КОНЕ
        if alt_day2_detour_1_tour:                                                                     # если скипаем тур
            $ alt_day2_my_win = renpy.random.choice([1,0])                                             # рандомно выигрыш Семёна 0 или 1
    elif alt_day2_result_tour in [2,12,22]:                                                            # Если выигрыш в КОНЕ
        if alt_day2_detour_1_tour:                                                                     # если скипаем тур
            $ alt_day2_rival_win = renpy.random.choice([1,0])                                          # рандомно выигрыш соперника 0 или 1
    return

#-----------------------------------------------------------------------------------
# АНАЛИЗАТОР 1-го ТУРА
label alt_day2_1_tour_analizer:
    $ alt_table_no = 0                                                                  # № стола = 1 (начинаем с НУЛЯ в этом случае)
    $ alt_mstt = 0                                                                      # обнуляем глобальный счетчик таблицы
    call show_tournament_table                                                          #  показываем исходное положение ??? сортируем игроков ???
    $ alt_result_dv_1_tour = alt_get_result_dv(alt_day2_gamblers_1_tour, 8)             # а где там наша ДваЧе?
    pause(1)
    $ alt_random_box_1 = range(1,len(alt_table_winner)+1)                               # черный ящик 1 — список от 1 до длины победителей +1
    while alt_table_no <= 4:                                                            # перебираем столы от 1 до 4
    #результат, игроки, высказывания — по номеру стола
        $ renpy.block_rollback()                                                        # блокируем роллбак
        $ results_at_table,gambler_win,winner_remark,loser_remark = alt_declare_results_tables(alt_table_no, alt_day2_gamblers_1_tour)
        "%(results_at_table)s"                                                          # оглашаем результат за столом
        call show_tournament_table                                                      # переход по метке — вызов очередной фишки
        extend " %(gambler_win)s."                                                      # выводим в окно имя победителя
        $ a_c_i = 0                                                                     # счетчик фраз
        while a_c_i < len(winner_remark):                                               # пока счетчик фраз меньше их количества
            $ alt_gambler_saying = winner_remark[a_c_i][0]                              # кто говорит
            $ alt_gambler_remark = winner_remark[a_c_i][1]                              # фраза
            if alt_gambler_saying != None:                                              # если определено, от кого фраза
                alt_gambler_saying "%(alt_gambler_remark)s"                             # выводим её от лица говорящего
            else:                                                                       # если "от автора"
                "%(alt_gambler_remark)s"                                                # выводим фразу "от автора"
            $ a_c_i += 1                                                                # увеличиваем счетчик фраз
        call show_tournament_table                                                      # переход по метке — вызов очередной фишки
        $ a_c_i = 0                                                                     # счетчик фраз
        while a_c_i < len(loser_remark):                                                # пока счетчик фраз меньше их количества
            $ alt_gambler_saying = loser_remark[a_c_i][0]                               # кто говорит
            $ alt_gambler_remark = loser_remark[a_c_i][1]                               # фраза
            if alt_gambler_saying != None:                                              # если определено, от кого фраза
                alt_gambler_saying "%(alt_gambler_remark)s"                             # выводим её от лица говорящего
            else:                                                                       # если "от автора"
                "%(alt_gambler_remark)s"                                                # выводим фразу "от автора"
            $ a_c_i += 1                                                                # увеличиваем счетчик фраз
        $ alt_table_no += 1                                                             # следующий стол
    return

#-----------------------------------------------------------------------------------
# АНАЛИЗАТОР ПОЛУФИНАЛА
label alt_day2_semifinal_analizer:
    $ alt_table_no = 4                                                                  # № стола = 4 (начинаем с четвертого в этом случае)
    $ alt_mstt = 0                                                                      # обнуляем глобальный счетчик таблицы
    call show_tournament_table                                                          #  показываем исходное положение ??? сортируем игроков ???
    $ alt_result_dv_semifinal = alt_get_result_dv(alt_day2_gamblers_semifinal, 4)       # а где там наша ДваЧе?
    pause(1)
    $ alt_random_box_1 = range(1,len(alt_table_winner)+1)                               # черный ящик 1 — список от 1 до длины победителей +1
    while alt_table_no <= 6:                                                            # перебираем столы 5-6
    #результат, игроки, высказывания — по номеру стола
        $ renpy.block_rollback()                                                        # блокируем роллбак
        $ results_at_table,gambler_win,winner_remark,loser_remark = alt_declare_results_tables(alt_table_no, alt_day2_gamblers_semifinal)
        "%(results_at_table)s"                                                          # оглашаем результат за столом
        call show_tournament_table                                                      # переход по метке — вызов очередной фишки
        extend " %(gambler_win)s."                                                      # выводим в окно имя победителя
        $ a_c_i = 0                                                                     # счетчик фраз
        while a_c_i < len(winner_remark):                                               # пока счетчик фраз меньше их количества
            $ alt_gambler_saying = winner_remark[a_c_i][0]                              # кто говорит
            $ alt_gambler_remark = winner_remark[a_c_i][1]                              # фраза
            if alt_gambler_saying != None:                                              # если определено, от кого фраза
                alt_gambler_saying "%(alt_gambler_remark)s"                             # выводим её от лица говорящего
            else:                                                                       # если "от автора"
                "%(alt_gambler_remark)s"                                                # выводим фразу "от автора"
            $ a_c_i += 1                                                                # увеличиваем счетчик фраз
        call show_tournament_table                                                      # переход по метке — вызов очередной фишки
        $ a_c_i = 0                                                                     # счетчик фраз
        while a_c_i < len(loser_remark):                                                # пока счетчик фраз меньше их количества
            $ alt_gambler_saying = loser_remark[a_c_i][0]                               # кто говорит
            $ alt_gambler_remark = loser_remark[a_c_i][1]                               # фраза
            if alt_gambler_saying != None:                                              # если определено, от кого фраза
                alt_gambler_saying "%(alt_gambler_remark)s"                             # выводим её от лица говорящего
            else:                                                                       # если "от автора"
                "%(alt_gambler_remark)s"                                                # выводим фразу "от автора"
            $ a_c_i += 1                                                                # увеличиваем счетчик фраз
        $ alt_table_no += 1                                                             # следующий стол
    return

#-----------------------------------------------------------------------------------
# АНАЛИЗАТОР ФИНАЛА
label alt_day2_final_analizer:
    $ alt_mstt = 3
    call show_tournament_table                                                          # показываем исходное положение, сортируем игроков
    $ alt_take_tournament_winner = alt_day2_gamblers_final[0].take                      # Ник победителя
    if alt_take_tournament_winner == "me":
        $ alt_name_tournament_winner = "Семёна"
    else:
        $ alt_name_tournament_winner = alt_day2_gamblers_final[0].name['v']             #  Получаем имя победителя турнира

    $ alt_take_tournament_loser = alt_day2_gamblers_final[1].take                       # Ник проигравшего
    if alt_take_tournament_loser == "me":
        $ alt_name_tournament_loser = "Семёну"
    else:
        $ alt_name_tournament_loser = alt_day2_gamblers_final[1].name['d']              #  Получаем имя проигравшего в финале

    if alt_take_tournament_loser in ['me','sh']:
        $ alt_pronomen_final_loser = "он"
    else:
        $ alt_pronomen_final_loser = "она"

    $ winner_remark, loser_remark = alt_declare_results_final(alt_take_tournament_winner, alt_take_tournament_loser) # вызываем функцию на финал — фразы победителя, проигравшего — по их никам.

    show el normal pioneer at cleft with dissolve
    el "Итак, турнир окончен."
    "Вспомнил о своих обязанностях организатор."
    $ alt_mstt = 0
    el "Поздравляем нашего победителя — %(alt_name_tournament_winner)s!"
    play sound sfx_concert_applause
    call show_tournament_table                                                          # двигаем победителя
    pause(0.2)

    $ a_c_i = 0                                                                     # счетчик фраз
    while a_c_i < len(winner_remark):                                               # пока счетчик фраз меньше их количества
        $ alt_gambler_saying = winner_remark[a_c_i][0]                              # кто говорит
        $ alt_gambler_remark = winner_remark[a_c_i][1]                              # фраза
        if alt_gambler_saying != None:                                              # если определено, от кого фраза
            alt_gambler_saying "%(alt_gambler_remark)s"                             # выводим её от лица говорящего
        else:                                                                       # если "от автора"
            "%(alt_gambler_remark)s"                                                # выводим фразу "от автора"
        $ a_c_i += 1                                                                # увеличиваем счетчик фраз

    $ alt_mstt += 1
    el "А вот %(alt_name_tournament_loser)s сегодня немного не повезло; тем не менее, %(alt_pronomen_final_loser)s занимает почётное второе место."
    call show_tournament_table                                                      # прячем проигравшего
    pause(0.2)

    $ a_c_i = 0                                                                     # счетчик фраз
    while a_c_i < len(loser_remark):                                                # пока счетчик фраз меньше их количества
        $ alt_gambler_saying = loser_remark[a_c_i][0]                               # кто говорит
        $ alt_gambler_remark = loser_remark[a_c_i][1]                               # фраза
        if alt_gambler_saying != None:                                              # если определено, от кого фраза
            alt_gambler_saying "%(alt_gambler_remark)s"                             # выводим её от лица говорящего
        else:                                                                       # если "от автора"
            "%(alt_gambler_remark)s"                                                # выводим фразу "от автора"
        $ a_c_i += 1                                                                # увеличиваем счетчик фраз
    hide el with dissolve
    return

# --------------------------------------------------------------------------
# Подготовка перехода на ужин: — очистка слоя, разблокировка роллбэка
label alt_day2_prepare_transition_to_supper:
    python:
        renpy.scene('underlay')
        renpy.with_statement(dissolve)
    $ alt_who_how_plays_poker()                                                     # посмотрели, кто и как сыграл
    if alt_day2_gamblers_result['me'] <= 11:
        $ alt_my_rival_final.take = None
        if alt_day2_gamblers_result['me'] == 1:
            $ alt_my_rival_semifinal.take = None
    $ d2_cardgame_block_rollback = False
    return
