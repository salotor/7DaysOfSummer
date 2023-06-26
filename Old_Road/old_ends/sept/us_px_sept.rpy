label alt_day7_us_px_sept:
    play music music_7dl["nap_one"] fadein 3
    scene bg ext_adductius_7dl with dissolve
    play ambience ambience_7dl["town_day"] fadein 5
    $ meet('dv', 'Она')
    "Она нашла меня одного, брошенного на качелях, спросила, почему я один."
    "А что я могу ей сказать?"
    "Я один потому, что никому не нужен?"
    "Потому что не знаю, куда пойти?"
    "Вот и молчал."
    "В кармане было целых пять рублей, я был богат и в любой момент, проголодавшись, мог сбегать за мороженым или даже молочным коктейлем."
    "Я был самодостаточен."
    "Но почему-то было плохо, так плохо…"
    "Такой вот фокус."
    with fade
    "Она попрощалась и ушла — высокая, красивая, с чистыми глазами, в которых было одно лишь спокойствие и любовь."
    "Я решил во что бы то ни стало дождаться её, потому провёл весь вечер и часть ночи на качелях, отбивая их у соседской малышни."
    "Почему-то казалось, что если я уйду, она меня потеряет."
    "Потеряет!"
    play ambience ambience_7dl["rain"] fadein 6
    show rain_overlay
    with dissolve
    "А под утро пошёл дождь, холодный, мокрый и зябкий."
    "Я тщетно прятался от него в карманы шортов, втягивал голову в плечи и весь дрожал."
    "А она не шла."
    "Было не столько мокро, сколько обидно."
    "Она же такая хорошая. Я так надеялся на неё!"
    "Вот и…"
    "Я уже совсем отчаялся, а пятёрка в кармане размокла. День не удался."
    with fade2
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    "И уже когда покатилось к горизонту Солнце, а углы зданий размылись в подступающих сумерках, на детской площадке, разбрызгивая лужи и разбрасывая красную крошку, появилась она."
    "Сначала сквозь калитку вплыл огромный чёрный зонт, потом появились серые нубуковые сапожки."
    "И громкий, на всю площадку «ах»!"
    "Она бросилась ко мне, встала, безжалостно портя обувь в луже, посмотрела на меня."
    "Передёрнула плечами, затянутыми в тонкую джинсовую ткань, видимо, посочувствовала."
    show dv normal winter with dissolve
    dv "А ну, пошли со мной."
    am "Нет. Я не могу. Я просто хотел вас увидеть ещё раз, а мне надо домой!"
    dv "Домой? Где твой дом?"
    am "Я… Я не знаю."
    dv "Вот и пошли."
    am "Нельзя ходить с незнакомыми."
    dv "Нельзя, да."
    dv "Ну, хотя бы зонтик возьми. Мокнуть нельзя, простудишься!"
    "Она вручила мне зонтик, улыбнулась, а мгновенно промокшие яркие волосы беспорядочно облепили лицо."
    "Светлая ткань курточки мгновенно потемнела, промокла."
    "Но её, похоже, это не волновало нисколько."
    dv "Ещё увидимся!"
    hide dv with diam
    "Она помахала мне и побежала к калитке."
    "А я ахнул про себя: как же так? Нельзя же! Она промокнет вся, простудится!"
    "И из-за меня?"
    "Сам я был уже давно мокрый насквозь, но не обращал на это внимания."
    am "Эй, постойте!"
    "Я спрыгнул с качелей и бросился вслед за ней."
    show dv normal winter with dissolve
    dv "Что такое?"
    am "Мокнуть нельзя, вы сами говорили!"
    dv "Но кто-то из нас будет под дождём. Я потерплю."
    dv "А ты весь продрог."
    am "Нет! Нельзя! Вы же сами простудитесь!"
    "Я толкнул ей зонтик, который она вовсе не спешила брать."
    am "Да возьмите же!"
    dv "Хорошо. Я возьму зонт."
    dv "Но в обмен на услугу."
    am "Какую?"
    dv "Я живу здесь недалеко. Проводишь девушку до дома?"
    am "Так нельзя же с посторонними!"
    dv "Тогда я буду мокнуть. Пока!"
    scene bg ext_townscape_ph_day_7dl
    show rain_overlay
    with dissolve
    "Она махнула мне рукой и зашагала по улице."
    "А я догнал её, раскрыл зонт над нами обоими."
    "Мы шли по улице ещё полчаса, прежде чем закончились эти большие многоэтажные дома, и начались маленькие домики, на один-два этажа, где жили по одной семье в целом доме."
    "Один из таких занимала и она."
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg int_mt_sam_room_7dl
    show dv normal winter
    with dissolve
    dv "Вот, мой дом. Спасибо, что проводил!"
    "Она не обратила внимания на зонтик, открыла ключом дверь и оставила её нараспашку."
    "Зашла внутрь."
    "А я, боясь и одновременно страстно желая оказаться в тепле, несколько минут стоял там."
    "Прежде чем решился."
    "Изнутри пахло чем-то непонятным, откуда-то доносились приглушённые голоса."
    "Я не сразу понял, что это телевизор."
    dv "Закрой за собой!"
    "Крикнула она, услышав мои шаги."
    dv "Оставь мокрую обувь у порога и проходи в ванную."
    dv "Умеешь газом пользоваться?"
    am "А… У-умею."
    dv "Я так и думала. Я сейчас."
    stop ambience fadeout 6
    with fade
    play sound sfx_open_water_sink
    pause(1)
    play sound_loop sfx_water_sink_stream
    "Где-то что-то пыхнуло, полилась вода."
    dv "Иди!"
    show dv smile dress with dissolve
    "Она стояла в ванной и приглашающе улыбалась."
    dv "Смотри — здесь мыло, вот мочалка. Одежду всю брось на полу, походишь пока в моём халате, пока я не придумаю тебе что-нибудь на замену."
    hide dv with diam
    "Я плохо понимал, о чём она говорит, потому что сомлел в тепле, но дождался, когда она уйдёт, послушно сбросил одежду и полез в ванну."
    stop sound_loop fadeout 6
    "Помывшись, я нашёл её на кухне, где она что-то делала у плиты."
    scene bg int_mt_sam_room_7dl
    with dissolve
    dv "Вот, смотри. Газ зажигается этой щёлкающей штукой, макароны и прочее будут на нижних полках, чтобы ты мог достать, главное, не забывай солить воду, если захочешь себе что-нибудь сварить."
    dv "Всё понял?"
    am "Да…"
    dv "Хорошо. А то кухарка я — так себе. {w}Зато у меня есть пицца! Ты как насчёт пиццы?"
    "Я не знал, что это такое, но на всякий случай кивнул."
    "И сделал это совсем не напрасно, потому что пицца…"
    "Мне было бы вкуснее, если бы не закрывающиеся глаза и озноб, который не закончился даже после горячей воды."
    with flash2_red
    dv "Ты красный… Ты весь горишь."
    "Она потрогала мой лоб."
    dv "Так и знала. Досиделся под дождём."
    show blink
    pause(1)
    scene black
    "Я хотел что-то сказать, но глаза сами по себе закрылись."
    "Всё дальнейшее я помнил только урывками."
    "Телевизор, какой-то дядя в белом халате и шапочке с красным крестом."
    "Очень вкусный чай с мёдом и лимоном и очень кусачие горчичники."
    "И тепло."
    "Кровать была с периной, я тонул в ней и не понимал, где заканчивается сон и начинается явь."
    "Просто боялся, чтоб она меня не прогнала."
    scene anim prolog_1
    with fade
    "А потом однажды понял, что варю что-то в кастрюльке."
    "Понял, что она рисует что-то в очень красивом альбоме на скрепке-пружинке и объясняет мне, как правильно и ровно вести линию."
    "А заснув, почувствовал что-то, почти забытое — поцелуй в висок."
    "И, не разлепляя век, улыбнулся:"
    am "Мама."
    scene bg int_mt_sam_room_away_7dl
    with dissolve
    "Через две недели, перед тем, как она убегала на работу, я сделал растворимый кофе нам двоим."
    "Сделал глоток и спросил:"
    am "Почему ты спасла меня?"
    "Я не помнил ничего."
    "Но откуда-то знал, что у меня есть… должна быть мама."
    "Должен быть дом."
    "А я помнил только крики, почему-то гудящую голову и привкус соли на губах."
    show dv smile dress with dissolve
    dv "Пожалела."
    am "Не верю."
    dv "Почему?"
    am "Ты отдала мне зонтик, а сама пошла мокнуть."
    am "Нельзя кого-то так сильно жалеть."
    show dv shy dress
    with dspr
    "Она покачала головой, посмотрела куда-то в сторону и тихо улыбнулась:"
    dv "Потому что меня однажды некому было спасать."
    dv "Я поняла, что если кого-то встречу, как я — то не пройду мимо."
    show dv guilty dress
    with dissolve2
    dv "Я однажды была как ты, а теперь…"
    "Я сел на пол у её ног и положил голову ей на колени."
    "Она от удивления отдёрнула руки, вздохнула."
    "И положила ладошку мне на голову. Погладила волосы."
    scene anim prolog_1
    play ambience ambience_7dl["tv"] fadein 3
    with fade
    "Так с тех пор и пошло."
    "Я ждал её дома, улыбался и готовил что-то, что мог, если только она не готовила пиццу."
    "Никогда не говорила, откуда она узнала это странное блюдо."
    "Но было вкусно, очень вкусно."
    "Потом мы устраивались на ковре, она что-то читала, а я смотрел в экран или тоже читал."
    "Чувствовал её ладонь у себя на волосах и верил в то, что этот мир не чёрен."
    play sound sfx_door_bell
    scene bg int_opened_door_7dl
    with dissolve
    "Пока однажды в дверь не раздался звонок."
    "Она пошла открывать, из прихожей донеслись грубые голоса, и её."
    "Напуганный."
    "Я бросился в прихожую, готовясь её защищать!"
    "А там стоял какой-то дядя в тёмно-серой форме и о чём-то говорил."
    "Вскоре в двери показались ещё двое."
    "Лязгнул металл, и она обернулась:"
    dv "Держись, слышишь? Я обязательно вернусь!"
    "Хлопнула дверь."
    "Я остался один."
    "Стёк вниз по стене, прижимая руки ко рту, пытаясь сдержать крик отчаяния."
    "Потому что вспомнил!"
    "Вспомнил, как однажды ко мне, туда, где я раньше жил, приходили такие люди!"
    "Так же говорили и кричали, так же лязгал металл."
    "Их тоже увели."
    "А я забыл."
    "Забыыыыл!"
    play sound sfx_open_door_kick
    pause(1)
    scene bg ext_townscape_ph_day_7dl
    with flash
    play ambience ambience_ext_road_day fadein 5
    "Когда я выскочил на улицу, машина с синей полосой уже таяла вдали."
    "А до меня почему-то никому дела не было."
    show prologue_dream
    with fade
    "Два дня я молчал и смотрел телевизор."
    "Готовил пересоленные макароны и пережаренные котлеты, стоя на табуретке у плиты."
    "Два дня выбрасывал их в ведро у плиты, даже не попробовав."
    "Я ждал, вздрагивал от шума на улице, выбегал к двери встречать."
    "А её всё не было."
    stop music fadeout 3
    scene bg ext_road_winter_7dl
    show prologue_dream
    with dissolve
    play ambience ambience_cold_wind_loop fadein 3
    "Между тем, на улице стала зима."
    "Мне захотелось выйти на улицу."
    "Вещей моего размера не было, кроме тех самых шортов с помочами и футболки."
    "Холодно, в этом нельзя выйти на улицу, никак нельзя."
    "Я сделал то, на что никогда бы раньше не решился."
    "Полез по шкафам."
    "И среди зимних вещей, которые я мог бы надеть, обнаружил записку."
    "Пыльную, мятую, видимо, она там лежала уже очень давно."
    play music music_7dl["fyrsta"] fadein 5
    $ set_mode_nvl()
    "Малыш."
    "Если ты читаешь эту записку, значит, всё пошло совсем плохо, совсем не так, как я хотела."
    "Но с первых же секунд, когда я увидела тебя на качелях, я видела в тебе себя — ту, которой однажды некому было помочь. {w}А когда вернулась, был дождь."
    "Я подумала, что нельзя тебя такого оставлять!"
    "Люди не любят друг друга, они равнодушны и так воспитывают своих детей, и продолжается это всё по кругу, раз за разом."
    "Меня так старательно делали равнодушной, ты бы знал. Но чем хуже мне становилось, тем сильнее я верила в то, что если мне однажды дадут шанс…"
    "Я разорву этот круг, сделаю не так, как учили и воспитывали. {w}Всё будет иначе, и, может быть, это и поможет однажды миру стать лучше."
    "Даже если со мной после этого всё будет совсем плохо."
    "Мы оба знаем, что я тебя спасла, но наши законы называют это похищением."
    nvl clear
    "Даже если тебе некуда было идти, не к кому возвращаться."
    "Я должна была сдать тебя в милицию, чтобы они решали твою судьбу."
    "Видишь, какая штука… Я узнала про твоих родителей, про то, что их арестовали, а ты сбежал."
    "Мой долг был сдать тебя в милицию. {w}Иначе меня будут судить, накажут."
    "Не за то, что ребёнок один сидит на качелях под дождём, а за то, что ты забираешь его домой, ведь не можешь пройти!"
    "Похищение."
    "Киднэппинг."
    "Преступление."
    nvl clear
    "И, знаешь, малыш… Я не боялась!"
    "Я ни секунды не боялась, пусть и понимала, чем это может быть опасно для меня и тебя."
    "Но я не могла тебя просто сдать. {w}Потому что там, куда ты отправился бы из милиции, тебя никто и никогда любить не будет."
    "А ты так в этом нуждался."
    "Потому я приму наказание, суд — что угодно."
    "Надеюсь лишь что однажды, как мы уже привыкли, я буду читать и гладить тебя по волосам."
    "Алиса."
    $ set_mode_adv()
    "Бумага почему-то набрякла и стала прозрачной."
    "Глаза начало резать, а нос покраснел и распух, как будто я снова простудился."
    "Только дело было совсем не в этом."
    "Дело было в том, что…"
    stop music fadeout 5
    with fade
    play music music_7dl["brim"] fadein 3
    scene bg ext_khruschevka_day_7dl
    with dissolve
    play ambience ambience_7dl["town_day"] fadein 3
    "На следующий день в дом пришла какая-то девушка чуть младше моей… а кого?"
    "Я даже не знал, кем мне была Алиса."
    "Мамой? Старшей сестрой? Кем-то большим?"
    "По-своему, по-детски, я души в ней не чаял."
    with fade
    "Она долго требовала от меня, чтобы я сказал, куда увезли её подругу, но я не знал!"
    "Я не мог сказать!"
    "Что хуже всего, я не мог ответить на простой вопрос: если её увезли — почему меня оставили?"
    "Это же я причина того, что она… Ну…"
    "Только поняв, что каши со мной не сваришь, Ульяна приказала мне ждать и убежала куда-то."
    "Вернулась только вечером, зато сразу с целым тючком зимней одежды."
    us "Я не могу позволить, чтобы из-за глупости дураков в погонах умер от голода ребёнок."
    "Так она сказала."
    "А сама-то! Сильно старше была?"
    with fade
    "Так или иначе, она заперла дом на ключ, взяла меня за руку и увела за собой."
    "Привела в какой-то странный дом, где на полу были квадратные плитки из линолеума, нас встретила добрая тётя в милицейской куртке, расстёгнутой, а под низом у неё был свитер с оленями."
    "Добрая — потому что напоила нас чаем, накормила бутербродами и уложила спать на диване."
    "А наутро за мной пришли."
    "Две недели в страшном, кошмарном месте, и если бы не Ульянка, каждый день прибегавшая ко мне поболтать сквозь рабицу, иногда передать конфету…"
    "Я бы не выдержал, наверное: потерять близкого человека, а потом очутиться здесь?"
    "Такого испытания никто не заслуживает."
    with fade
    "В один вечер Ульяна сказала мне, что уговорила своих, чтобы они стали собаками."
    "Или как-то так."
    "Но на следующий день за мной пришла Ульяна и её родители."
    "Я официально Сидоров теперь, у меня есть старшая сестра с самыми красивыми красными волосами и улыбкой, чем-то похожей на ту, что я запомнил у Алисы."
    with fade
    "С тех пор прошло довольно много времени."
    "Ульяна никогда не рассказывала о том, что стало с её родителями, лишь иногда сквозь зубы роняла что-то про стирание и глупого младшего."
    "Я не знал, что это значит, но понял, что у неё, как и у меня, никого из родителей просто нет."
    "Зато есть старший брат, которому отказали в опеке, из-за чего ей пришлось идти в другую семью."
    "Хорошую семью. Особенно папка хороший. Викентий Викторович. Дооообрый."
    "Я подружился с ребятами во дворе, с «гвардией»."
    "А Антон, старший брат Ульяны, постоянно приезжал с учёбы, катал нас на своём громыхающем и плюющемся «Иже» с вилкой, как у «Харлея-Дэвидсона»."
    scene bg ext_railbridge_sunset_7dl
    with fade
    "Мне уже больше не десять."
    "Да и ей не восемнадцать."
    "Но на улице закатно-солнечно и пахнет липой, воздух вокруг почти жаркий, а мы сидим, не двигаясь, наблюдая за тем, как неторопливо отходят в сторону крашеные шаровой краской ворота, и на пороге стоит она."
    "Некрасивая, маленькая, с шрамом на скуле и неукротимым пламенем в глазах."
    "Моя. Самый дорогой человек в жизни."
    "Она вышла и некоторое время стояла, смотря в небо, дыша и не двигаясь."
    "А потом я не выдержал и выскочил из мотоциклетной «люльки» и закричал, замахал руками!"
    am "Алиса! Алиска, мы здесь!!!"
    us "Лиска!"
    "Она неверяще посмотрела на нас, а потом побежала, спотыкаясь, глупо и нелепо размахивая руками."
    "Налетела вихрем, целуя, прижимая к себе и счастливо смеясь."
    "Солнце блеснуло медью в волосах, в радужке снова поселилось то самое спокойствие и любовь, ради которой мы и прожили всё это время."
    "Отблеск познакомившего нас лета."
    play sound sfx_7dl["aunl"]
    show acm_logo_us_px_sept with moveinright:
        pos (1600, 1020)
    pause(2)
    jump alt_stories_start