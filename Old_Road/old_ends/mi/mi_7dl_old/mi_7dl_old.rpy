﻿label alt_day4_mi2sl_transit2:
    stop music fadeout 3
    $ persistent.sprite_time = "day"
    $ day_time()
    scene bg ext_dining_hall_away_day with dissolve

    menu:
        "Герк":
            $ herc = True
        "Локи":
            $ loki = True
        "Дрищ":
            $ dr = True

    "Я вышел на улицу и, обернувшись, почувствовал, как от ужаса волоски встают дыбом на загривке."
    "Я не успел среагировать."
    "Никто бы не успел."
    "Очень трудно воспринять воплощающийся наяву кошмар и остаться при этом в трезвом уме."
    "А случилось то, что на выходе из столовой оказалась Мику — и что-то шепчущая ей на ухо маленькая дрянь."
    show mi serious pioneer at center
    show us dontlike pioneer at left
    with dissolve
    play music music_7dl["knock"] fadein 4
    me "Мелкая, ты опять лезешь не в своё дело!"
    "Я пытался заглушить криком собственный страх."
    "Ульяна вздрогнула и, отступив на два шага, заявила — с каким-то непонятным ожесточением:"
    us "Так ведь это и не твоё дело теперь."
    us "Ты же выбрал уже."
    us "Вот и катись к своему делу."
    "Она обожгла меня взглядом и, развернувшись, ушла, держа спину презрительно-прямой."
    hide us
    show mi cry pioneer at center
    with dissolve
    "А я повернулся к Мику — и вздрогнул, будто располосованный по живому конским волосом — столько потерянности и детского недоумения было в её глазах."
    me "Мику, я…"
    mi "Сёма, это правда?"
    me "…"
    mi "Но это же неправда, это совсем-совсем не может быть правдой!"
    mi "Я не верю в это. Это, должно быть, какая-то ошибка."
    mi "Это шутка!"
    "Она нервно-истерически рассмеялась."
    mi "Сёмочка, ну скажи им! Это же шутка, да?"
    "Необычная истерика, названия которой я не мог подобрать, и с которой сейчас не справились бы все объятья мира."
    mi "Это просто Ульяна так нехорошо и некрасиво пошутила, жестокий ребёнок."
    mi "Правда?"
    mi "Ты же не можешь вот так вот просто взять и…"
    "Её голос сорвался."
    mi "Сёмочка… Пожалуйста."
    mi "После всего, что ты сказал."
    "Она стояла и умоляла, не обращая внимания на катящиеся по щекам слёзы."
    "Меня рвало на части болью, чувством вины и раскаянием, равного которому я никогда еще не чувствовал."
    "Но я ничего не мог сделать. Язык примёрз к гортани, и руки мелко-мелко затряслись."
    mi "Неужели для тебя всё сказанное ровным счётом ничего не значит?"
    "Она всхлипнула."
    mi "Разве я для тебя пустое место?"
    "Я просто стоял придурком и не мог выдавить из себя ни слова."
    "Я — перехваченное дыхание Джека. Я — ледяной пот на его лбу."
    me "Прости меня."
    mi "Сёмочка, я ведь и не злюсь. Просто давай скажем, что это неправда? Пожалуйста."
    me "Я не могу тебе врать."
    mi "И наши чувства для тебя ничего не значат?"
    me "Чувства?"
    mi "Ты не видишь, глупый, что это я тебя люблю. Я, а не этот ходячий генофонд!"
    "Её голос упал до шёпота."
    scene miku_tears1_7dl with flash
    mi "Я, Сёмочка."
    "Её глаза затуманились."
    mi "Я…"
    scene miku_tears2_7dl with flash
    with dissolve2
    mi "Будь счастлив."
    mi "Прощай."
    "Она оттолкнула меня и бросилась бежать куда глаза глядят."
    scene white with flash
    th "Надеюсь, она не наделает глупостей."
    show mi_ru with dissolve:
        xalign 0.5 yalign 0.5 zoom 0.8
        linear 5.0 zoom 0.55 xalign 0.5 yalign 0.55
    dreamgirl "Глупостей за неё уже ты наделал."
    dreamgirl "Ты не только бревно бесчувственное, ты ещё и предатель."
    dreamgirl "Счастья тебе с этой колхозной коровой."
    hide mi_ru with dissolve
    "Она скрылась из виду, когда ступор, наконец, отпустил меня."
    "Я бежал куда-то, опираясь не то на интуицию, не то на какое-то чутье."
    "Бежал долго."
    "Пока не понял, что нельзя верить ни чутью, ни интуиции."
    "Я не догнал Мику."
    scene bg ext_path_day with dissolve
    "И теперь она потеряна для меня."
    "Я обнаружи себя где-то на задворках лагеря. Разумеется, Мику здесь не было."
    "Еле-еле сориентировавшись, я проломился сквозь кусты к тропинке, ведущей на площадь."
    th "Может, хоть там кто-нибудь видел её!"
    "Я скрестил пальцы в дикой надежде на чудо."
    th "Если я добегу туда быстро-быстро, и встречу кого-нибудь — он обязательно укажет мне, где искать!"
    scene bg ext_square_day with fade
    show mt normal pioneer
    with dissolve
    "Здесь уже стояла Ольга Дмитриевна и с затаённой тоской смотрела на то, как я, помятый и исцарапанный, приближаюсь."
    mt "Мику потерял?"
    mt "А вы разминулись."
    me "Ч-что?"
    mt "За ней отец из города вернулся, если поспешишь — можешь успеть застать её у ворот."
    me "Спасибо!"
    $ persistent.sprite_time = "day"
    scene bg ext_camp_entrance_day
    with dissolve2
    "Я бежал изо всех сил."
    "Я бежал так, что сухожилия расплавились в адское олово, а раскалённый воздух, кажется, оставил вечный ожог на моей глотке."
    "Я бежал, пока не свело ноги судорогой — и лёгкие, которые всю жизнь отказывались включить для меня второе дыхание, перенасытили кровь кислородом так, что у меня голова закружилась."
    "И тогда я побежал дальше."
    "Меня хранил мой ангел-хранитель, как и все одиннадцать лет моей жизни, что я нёсся по склону, всегда удачно ставя ногу между корнями сосен."
    "Здесь уже не было — ни машины, ни Мику."
    "Только пришпиленная к воротам бумажка с коротким адресом и подписью: Японское посольство в СССР."
    th "Адресат: небеса."
    "Последняя память о Мику."
    "На душе стало так же пусто, как и в тот вечер, когда мы с Мику сделали обоюдный шаг навстречу."
    play sound sfx_open_dooor_campus_1
    stop ambience fadeout 1
    scene bg int_house_of_mt_day
    with fade
    pause(1)
    play ambience ambience_int_cabin_night fadein 1
    "Не помня себя, я вернулся в ставший уже ненавистным домик и рухнул на кровать."
    "В случившемся виноват только я сам."
    "И только я сам понесу за это наказание."
    me "Дорогое небо…"
    me "Я был взвешен и найден слишком лёгким."
    me "Как тот самый текел. Так какого дьявола, дорогое небо?"
    "Я с вызовом уставился в тёмный потолок."
    $ prolog_time()
    if loki:
        show blink with dissolve
        pause(1)
        scene bg ext_winterpark_7dl with flash
        pause(1.5)
        "За свою глупость я заплатил сполна."
        "Как жаль, что некому предъявить оплаченный счёт."
        "Холод забрался под кожу, и сил хватило только на то, чтобы тихо улыбнуться."
        "Я дурак. И я очень виноват."
        "Надеюсь, в следующей жизни у меня будет шанс всё исправить."
        play sound sfx_7dl["aunl"]
        show achieve_ungood with moveinright:
            pos (1600, 1020)
        pause(4.4)
        with vpunch
        jump alt_stories_start
    elif herc:
        play music "<to 52.94>" + music_7dl["herc_death"] fadein 5
        "Ты можешь быть богом, воплощением счастья или ненависти. Истинно только одно."
        "Ты умрёшь. Весь вопрос — как."
        "Пока тебе двадцать, ты прожигаешь время под эгидой «живи быстро, умри молодым» — и всё равно до одури веришь в собственное бессмертие и возможность жить пятьсот лет и больше."
        "А потом проходит время, и ты понимаешь, насколько ты хрупок и смертен."
        scene bg int_store_7dl with fade2
        "Смертен волей глупого случая, смертен геройски во имя жизней близких, смертен от старости в пыльных объятьях пустой квартиры."
        "Память вернулась толчком."
        "Я оказался смертен ради какой-то бутылки водки.{w} И Зинаиды, которая уже отжила своё."
        "Возможно, если бы я наплевал на мать, и доучился бы — мне не пришлось бы рисковать жизнью ради спасения чьего-то имущества."
        scene black with fade
        "Возможно, в итоге мы всё равно все оказались бы здесь — я, Зинка и этот пьяный дурак с пистолетом."
        "Путешествие подошло к концу. Что ж. Это было прекрасное путешествие."
        "С самой прекрасной девушкой на свете."
        "Длиной в четыре дня лета."
        play sound sfx_7dl["makarych"]
        scene believe_in_pain with flash_red
        pause(2)
        play sound sfx_bodyfall_1
        stop sound_loop
        play sound sfx_7dl["aunl"]
        show achieve_ungood with moveinright:
            pos (1600, 1020)
        pause(7.4)
        with vpunch
        jump alt_stories_start
    elif dr:
        "Пора возвращаться домой."
        me "Я был признан негодным."
        scene black with fade
        $ volume(0.5, 'music')
        scene bg intro_xx with flash
        stop ambience fadeout 2
        play sound_loop sfx_bus_interior_moving fadein 4
        voice "Парень. Просыпайся."
        voice "Конечная."
        me "Что? А. Спасибо."
        "Как удобно садиться на одной конечной — и прибывать на другую конечную. Никогда не проспишь."
        "Дискретное перемещение между двумя точками."
        me "Какой, всё-таки, красивый сон."
        "Я машинально потёр запястье."
        "…и, подняв обшлаг рукава, нашёл свежую царапину — ту самую, что заработал в кустах шиповника, продираясь к площади."
        th "Так что, это был не сон?!"
        "Я не помню, что я там кричал, куда рвался — но водитель выставил меня вон из салона."
        "Ледяной корочкой на глазах — лицо, морозом на губах — имя."
        show mi cry pioneer at right with dissolve
        pause(0.3)
        hide mi with dissolve
        "Мику."
        scene black with fade
        stop sound_loop fadeout 0
        play sound sfx_7dl["aunl"]
        show achieve_ungood with moveinright:
            pos (1600, 1020)
        pause(7.4)
        jump alt_stories_start


label alt_day4_beach_night_mi:
    stop ambience fadeout 2
    $ persistent.sprite_time = "night"
    $ night_time ()
    scene bg ext_beach_night
    with dissolve
    play ambience ambience_lake_shore_night fadein 2
    show mi normal pioneer at center with dissolve
    "Ночь между тем вступила в полные права — на небо выкатилась луна, огромная, занимающая чуть ли не половину неба."
    mi "Луна какая огромная."
    "Томно заметила Мику."
    me "Суперлуние. {w}Для тех, кому мало целой ночи."
    dreamgirl "Как трогательно! Расскажешь ей про альбедо и прочие, несомненно уместные в отдельно взятом «здесь и сейчас» вещи?"
    th "А чё не так-то? Пусть знает, какой я умный!"
    dreamgirl "Как утка."
    dreamgirl "Пофорсить перед девочкой дело святое, но надо и честь знать — не лезь туда, где плаваешь."
    th "Ума палата? Тогда что мне ей сказать?"
    dreamgirl "Да уж не про суперлуние явно!"
    dreamgirl "За руку её возьми. Или обними за талию и медленно и печально опускай руку, пока не окажется внезапно, что за бедро обнимаешь."
    dreamgirl "И говори. Да что угодно, господи."
    dreamgirl "Расскажи ей о себе что-нибудь, из последних нескольких лет, вспомни смешные ситуации."
    "Я поморщился."
    dreamgirl "А, да, прости. Дохлый номер. Не про то же ей рассказывать, как ты горбился перед монитором, ради разнообразия нажимая то F5, то контрол+эр."
    dreamgirl "Про игрушки, распродажи на Стиме тоже лучше не рассказывать. Как и про препресс."
    dreamgirl "Чувак, ты скучное чмо, ты в курсе вообще?"
    th "Ты. Не. Помогаешь."
    dreamgirl "Ладно, попробуй тогда её на откровенность вызвать. Раз ты такая посредственность."
    "Мы сидели и смотрели на огромную луну и на звёзды."
    "И если бы не мой психоватый голос — то ли совесть, то ли гормоны, то ли здравый смысл, то ли всё сразу — то я бы так и занимался ерундой, вместо того, чтобы приобнять девочку."
    show mi happy pioneer at center with dissolve
    me "Мику, а можно нескромный вопрос задать?"
    mi "Ммм… Зависит от того, насколько он нескромный."
    me "Мне просто хочется узнать о тебе чуть больше."
    show mi upset pioneer at center with dissolve
    mi "Я всё ещё не услышала вопроса, ты меня зачем уговариваешь?"
    mi "Или это и правда нечто непристойное?"
    "Мы оба неосознанно прибегли к тому приёму, какой использовали в первое наше свидание — мы смотрели куда угодно, только не друг на друга."
    "Хотя и есть поговорка о том, что настоящая связь возможна только с тем, кто смотрит не на тебя, а в одну с тобой сторону."
    "Собственно, этой поговорке мы могли бы послужить неплохой иллюстрацией."
    show mi shy pioneer at center with dissolve
    "Мы чувствовали друг друга на уровне тепла."
    "Закрыв глаза, плечом чувствуя плечо, рукой руку. Я всю жизнь считал себя самым завзятым аудиалом, при этом, таким сугубым — отсюда и увлечение музыкой, например, сделавшее меня меломаном."
    "Информация, которую я воспринимал ушами, всегда впереди была остальных органов чувств — курение заглушило нюх и вкус, а зрение слишком долго пичкали серыми картинами."
    "Думаю, вывод о том, что я ненавидел прикосновения, сделать нетрудно."
    "И единственным спасением во время поездок в метро для меня — было заткнуть уши затычками и включить что-нибудь, чтобы басом до среднего уха доставало."
    "Но здесь я как будто получил бесплатный сброс всех систем организма — я очень остро чувствовал запахи, а опираясь на опыт человека, побывавшего в отношениях, мог отследить и отделить запахи интересного толка от обычных бытовых ароматов."
    "Пища здесь как будто сдабривалась глутаматом натрия — настолько явственно ощущались все грани вкуса, в полном согласии с пословицей «когда я ем, я глух и нем», превращая меня в кинестетика на время употребления пищи."
    "Рыба в яйце в обед второго дня — исключение."
    "Невероятно, невозможно яркие краски мира я отметил ещё в первый день, сходя с автобуса."
    "И вот здесь я сижу, обнимая дорогое мне существо, и мне не нужно глаз для того, чтобы понять её настроение и с высокой точностью определить выражение лица."
    "Больше того, она же, как человек сценический, всегда может спрятать эмоции под масочкой — но не существует масочки для языка тела."
    "И подающаяся под руку спина — как кошка, которая хочет, чтобы ей ещё и левый бок погладили, право слово! — говорит куда больше всех слов и мимики."
    "Если бы я ей не нравился — спина была бы окостеневшая, каменная."
    "И хотелось общаться в эти моменты — взахлёб, вперехлёст, будто упиваясь друг другом — словами, касаниями, взглядами."
    "А я сидел и {i}ощущал{/i} её — внутренней стороной руки, бедром, боком."
    "Дурацкое аудиальное восприятие мира, раскладывающее даже самую волшебную музыку на отдельные дорожки."
    "Мику звучала как дорогой, профессиональный концерт для скрипки с оркестром в исполнении Лондонского Симфонического. {w=.4} Исключая некоторую болтливость — идеальный, отточенный до последнего ангстрема образ."
    "От эфирного, эвкалиптового запаха волос до гордой посадки головки."
    me "Ты платье вчера из костюмерной вытащила, так радовалась…"
    "Сказал я, не поворачиваясь."
    me "Неужели у тебя платья хуже?"
    show mi upset pioneer at center with dissolve
    mi "О нет, нисколечко. Есть даже парочка по-настоящему красивых."
    me "Так в чём же тогда дело?"
    "Она хихикнула."
    mi "Не поверишь."
    me "Ну?"
    mi "Слишком откровенные! {w} Я приехала в лагерь в спортивном костюме — Па сказал, так будет практичнее, а я спорить не стала."
    mi "Костюм и правда хорош, плюшевый, бордовый, мой любимый цвет."
    mi "А добравшись, в первые же полчаса переоделась — ещё думала, почему это Лена на меня так странно смотрит."
    me "И?"
    mi "И устроила фурор в столовой, заявившись туда в коротком платье!"
    "Я не видел, но готов был поклясться — её глаза сияли озорством."
    mi "Это надо было видеть — все разговоры смолкли, и внимание ребят скрестилось на мне."
    mi "Ну а я что, я иду и наслаждаюсь."
    me "Разве вожатая тебе не разъяснила о форме?"
    mi "Знаешь, как-то удавалось разминуться с ней весь день, так что впервые после летучки я встретила её в той самой столовой."
    me "Так, а что с ними? Разрезы? Декольте? Прозрачные вставки?"
    show mi laugh pioneer at center with dissolve
    mi "Длина подола!"
    mi "Как сказала мне Ольга Дмитриевна — «чтобы немедленно пошла и надела что-нибудь, чтобы хотя бы срам прикрывало!», и до той поры не пускала меня в столовую."
    "Я позволил руки съехать ещё ниже по бедру."
    me "Что, платье было настолько короткое?"
    mi "Чуть-чуть длиннее."
    "Рука опустилась ещё ниже."
    me "Настолько?"
    "Мику кивнула, потаённо прислушиваясь к тому, чем это заняты мои пальцы."
    "А ничем они не заняты. Лежат просто. Примус починяют."
    me "И что, у тебя {i}все{/i} платья такой длины?"
    mi "Из красивых — да. Есть парочка в пол, но они чёёёооорные!"
    me "Ага. А тебе нравится бордо?"
    mi "Ну, ещё серые, знаешь, как замша. Ещё сине-зелёный."
    show mi smile pioneer at center with dissolve
    mi "Хотя об этом ты, наверное, уже догадался."
    stop music fadeout 5
    play music music_list["trapped_in_dreams"] fadein 3
    "За нашей неспешной беседой мы и заметить не успели, как луна вскарабкалась чуть выше по небосклону, и прозрачный лунный свет озарил пляж."
    "Немного повернувшись, я смотрел на изящные, тонкие черты лица Мику."
    "Они будто обострились, получили дополнительное измерение чёткости, и вместо хрупкой юной девушки из-под пушистых ресниц на меня строго взирал взрослый, пусть и маленький, человек…"
    mi "Потому мне пришлось искать себе платье для танцев вне моего гардероба."
    me "А что с платьями «в пол»?"
    show mi shy pioneer at center with dissolve
    mi "Говорю же — черные! Плюс крой у них… Больше на кимоно похожий."
    "Я представил себе Мику в кимоно на танцплощадке, зажигающей под саунд от «Boney M»."
    th "Или их не было тогда?"
    dreamgirl "Как это не было?!"
    "Ошалевшее от моей наглости подсознание как крышкой люка по кумполу стукнуло меня единым эйдетическим образом."
    "{i}Совсем другой лагерь. Исколотые пойманным ёжиком ладошки. Во рту вкус советского лимонного пирога — в котором от лимона только корка, горькаяяяяя! Немного саднит сгоревшие плечи — не надо было засыпать на пляже. И доносящийся из рупора задорный биток, под который половина населения подпевает: «Daddy! Daddy cool!»{/i}"
    dreamgirl "Совсем ошалел, что ли?!"
    dreamgirl "Самые тёплые воспоминания под сомнение ставить. Между прочим, сравни интенсивность воздействия на органы чувств там и тут."
    th "Похоже. И?"
    dreamgirl "Да нет… Так, ничего."
    me "Поправь меня, если я ошибаюсь, но там ткань такая интересная."
    mi "Да. Сквозь неё всё чувствуется так, будто бы её нет. У тебя так сердце заколотилось, я даже испугалась, как бы плохо не стало."
    show mi happy pioneer at center with dissolve
    mi "Всегда приятно знать, что ты на кого-то действуешь так."
    th "Как выстрел из «Пустынного Орла» в упор? Это да."
    "Я хотел было ответить что-то резкое в своём обычном духе, но тут ладонь девочки легла мне на губы и без лишней нежности придушила эпитет."
    mi "Псст, тихо!"
    "Зашипела она."
    th "И как это она услышала, интересно? Шаги по песку? У девочки из музыкального клуба экстрасенсорное восприятие?"
    "Будто отвечая моим мыслям, сзади раздались шаркающие шаги, потом что-то грохнуло — видимо, в потёмках, кто-то обо что-то крепко стукнулся."
    "Прилагающийся матерок был тому свидетельством."
    "Дёрнув меня за рукав, Мику одними глазами указала на дающий причудливую сетчатую тень забор из сетки-рабицы."
    "Я кивнул и мы, пригибаясь, пробежали туда."
    "Тень здесь была погуще — усевшись между деревьев, мы могли наблюдать за всем пляжем, при этом не рискуя быть обнаруженными."
    me "И от кого мы здесь ныкаемся?"
    mi "Ну вот, кто там сверху шёл…"
    "Она прижала палец к губам — впрочем, если бы я её не обнимал, так и не заметил бы — тьма здесь была воистину из разряда «глаз выколи»."
    hide mi with fade
    "Вскоре под чьими-то подошвами захрустела галька — наш неожиданный визитёр явно не горел желанием общаться с кем бы то ни было и сходу направился влево — к тому самому отпугнувшему меня леску."
    "В свете звёзд тяжело было разглядеть, кто это — удалось только понять, что это кто-то невысокий, и него хвостики, задорно торчащие в разные стороны."
    "Я было подумал на Лену, но, блин, это с равным успехом могла быть и Алиса!"
    "Их впотьмах не разберёшь. Даже на ощупь."
    dreamgirl "Хе-хе. Не «даже», а {b}тем более{/b} на ощупь. Ты сейчас свою Мику отличишь только потому, что у неё бёдра узкие и грудь небольшая. {w} А если попытаешься разобраться между этими фигуристыми красотками…"
    "Очевидно, что Алисе в лесу ловить было нечего, поэтому за рабочую приняли версию, что это Лена, направившаяся сычевать в лесок."
    th "Может, она там трупы прячет."
    "Волосы Мику щекотали мне нос, и я сдерживался изо всех сил, чтобы не чихнуть."
    "Я правда пытался!"
    "Даже почти придушил чих, выпустив наружу непонятный звук, больше похожий на хлопок ладонью по подушке."
    "Силуэту, впрочем, хватило и этого — он подскочил на месте и заоборачивался в поисках источника шума."
    mi "Тихо ты."
    "Не обнаружив никого, таинственный незнакомец втянул голову в плечи и быстрым шагом продолжил путь."
    play music music_list["goodbye_home_shores"] fadein 3
    "И вскоре исчез."
    "Я было собирался выдохнуть, перевести дух или хотя бы расправить плечи, но меня опять сцапали за рубашку и пригнули к земле."
    "Нет, возмущаться не хотелось, но всё-таки!"
    "Впрочем, заслышав очередной скрип со стороны входа на пляж, я притих."
    th "Пляж сегодня определённо пользуется популярностью! И что это они сюда паломничество наладили — на ночь-то глядя?"
    "Нет ответа. Да и откуда бы."
    "Луна, до поры прячущася где-то за облаками, на секунду выглянула, осветив знакомое каре и хохолок вопросительным знаком."
    show mz normal glasses pioneer at cright with dissolve
    "Жужелица. Ей-то какого рожна здесь надо?!"
    th "Неужели купаться намылилась?"
    "И верно, намылилась."
    th "Мда… И что, ради этого меня Мику тут к земле пригибает? Во имя сомнительной чести лицезреть столь же сомнительные прелести этого книжного жука?"
    th "Вот уж не было печали."
    "В отличие от первого гостя, библиотекарша двинулась вправо — туда, где дно речки было достаточно пологим, а к поверхности не подходили ледяные ключи — чем славилась лодочная пристань."
    "Купальней, надо полагать, она не прельстилась — как же, там же пионэров купают!"
    "И непонятно было, что мешало ей в течении дня самостоятельно прикрыть лавочку — куда всё равно никто не ходит — и выбраться искупаться, пока солнце ещё жарит."
    "Гарантированно лучшие ощущения!"
    "Или она плавать не умеет?"
    "А может, стесняется?"
    hide mz with dissolve
    "Она сбросила одежду и, оставшись в купальнике, медленно зашла в воду."
    "Даже в темноте было заметно, что её ощутимо трясёт."
    me "И мы что, ради этого…"
    mi "Сёмочка, помолчи, пожалуйста."
    "Моих губ в темноте коснулось что-то влажное и мягкое."
    th "И как она в темноте видит, куда целовать?!"
    me "Почему?"
    mi "Кажется, это не конец."
    "И снова не ошиблась. Наше вечернее вуйар-шоу набирало обороты!"
    "Подтверждая мою теорию о том, что сегодняшний пляж приобрёл статус места паломничества для чудиков всего лагеря, в обозримое пространство вывалился Электроник!"
    "Притом, вывалился так удачно, что его приметные кучеряшки и лицо с по-детски огромными глазами мгновенно, как софитом, высветил лунный свет."
    show el normal pioneer at center with fade
    th "Что, этот тоже купаться?"
    th "Или он сюда с романтическими целями?"
    "Может, у него здесь свидание с первой фигурой?"
    "Я приготовился к тому, что он повернёт налево."
    "А он, опровергая все мои домыслы, сделал то, чего от него я точно ожидать не мог!"
    "Заприметив мелькающую над водой головку с приметным упрямым вихром, он, пригнувшись к земле, пробежал до входа на понтоны и, спрятавшись там в тени, замер."
    th "Да он больной, что ли?!"
    "В жужелице эротики примерно столько же, сколько в нижней трети дубовой двери. Последняя предпочтительнее в силу того, что не издевается над собеседником."
    "Может, он перепутал?"
    "Захотелось подняться и, подойдя к заблудшему сыну человеческому, взять под локоток, указать направление."
    "Не, фигу. Он сидел на мостках и, скорчив самую несчастную физиономию, вздыхая, наблюдал за тем, как библиотекарша, трясясь, брызгает на себя остывшей уже водой."
    "И что-то лепетал. Глаза у него были одухотворённые."
    play music music_list["a_promise_from_distant_days_v2"] fadein 3
    th "Стихи, что ли, читает?"
    dreamgirl "Я вас любив. Любов ще, бути може, в душів моєї згасла не зовсім. Але нехай вона вас більше не тривожить — я оглушив…"
    th "Ну дальше-то, дальше продолжай! Ханжа!"
    "Мику, для которой мои размышления не были тайной, прыснула и, затыкая рвущийся наружу справедливо возмущённый вой, развернула меня к себе и впилась в мои губы своими, в этот раз не останавливаясь на простом соприкосновении."
    "В этот раз она, похоже, была настроена посерьёзнее, так как прикосновения острого язычка я почувствовал, не успев даже прийти в себя от её напора."
    dreamgirl "Ух ты, мы хотим с языком?"
    dreamgirl "Пустишь-не пустишь?"
    th "Что за дебильные вопросы."
    "Я старался дышать носом, так как рот был занят. В частности, пытался подловить её язык, кончик, там, где чувствительнее всего."
    "Она не уступала ни миллиметра, в результате у нас получилось эдакое рестлинг-шоу, где она, спустя минуту, признала собственное поражение."
    "Целоваться на пляже под светом луны — настоящая романтика."
    "Целоваться, насмотревшись за тем, как придурковатый мальчик наблюдает за страшненькой хамкой — извращение."
    th "Нет, ну надо же! И где она так навострилась языком орудовать?"
    th "На учебных пособиях, никак?"
    th "Помидорах-яблоках, э?"
    me "Ты маньячка."
    "Прошептал я, оторвавшись от неё ещё через пару минут."
    me "Чёртова извращенка."
    "Она хихикнула и обвила мою шею ладошками."
    "Кажется, её и правда заводит вся эта ситуация."
    mi "Господи, ну кто бы подумать мог, что Электроник…"
    "Она с трудом сдерживалась, чтобы не расхохотаться в полную силу."
    "А между тем, действо разворачивалось!"
    "Жужелица, накупавшись и намёрзшись, выбралась на берег и промокала буркала полотенчиком, а Электроник раз, наверное, в пятый, пытался встать и подойти."
    "Он злился, сопел, сжимал кулаки и бессильно бил себе по коленям, пытаясь совладать с собой."
    "Тщетно. Ему отчаянно недоставало решимости.{w} И нужен был какой-то знак, что-то типа непристойного жеста с небес — приглядишься, а это просто облака так удачно встали!"
    "Чем хорошо рядом с водой — источник шума невозможно определить. На секунду мне подумалось, что это где-то у нас здесь треснула ветка или что-то в этом духе."
    "Нет. Шум донёсся аккурат из того самого леска, куда ушёл первый визитёр."
    play music music_list["meet_me_there"] fadein 5
    "А Электроник, сидящий на иголках, весь взведённый, подскочил и, действуя на кураже, всё-таки сделал то, зачем пришёл — двигаясь на деревянных негнущихся ногах он подошёл к уже одевшейся библиотекарше."
    "Мы оба превратились в слух."
    show el serious pioneer at cleft with dissolve
    show mz normal glasses pioneer at cright with dissolve
    el "Эээээ…"
    "Старательно проблеял Электроник."
    "И ещё раз."
    el "Ээээ…"
    show mz angry glasses pioneer at cright with dissolve
    mz "Сыроежкин? Ты какого чёрта тут забыл?"
    "Само очарование."
    "Потенциальная владелица сорока кошек и нуля мужчин на склоне лет."
    show el upset pioneer at cleft with dissolve
    el "Женя, я…"
    mz "Что?"
    el "Я спросить хотел."
    mz "Для этого обязательно надо было приходить сюда? Я в библиотеке целый день рядом с тобой сижу, что ж не спросил?"
    el "Чужие уши. Особенно эта…{w=.5}нелюдимка."
    show mz bukal glasses pioneer at cright with dissolve
    mz "Ладно. Чужих ушей нет, нелюдимки нет. Что надо?"
    el "Женя, а ты…Ты помнишь, что в пятницу прощальная дискотека?"
    mz "Разумеется, помню. Ты меня об этом спросить хотел?"
    el "Нет. То есть, да. То есть…"
    "Он набрал в грудь воздуха и как в холодную воду рванулся на остатках тающей храбрости:"
    el "Женя, а ты пойдёшь на танцы?"
    mz "Нет, конечно."
    "Спокойно ответила жужелица, поправляя очки."
    mz "Что ж я, дура, время тратить на танцполе. У меня и так дел полно."
    th "Какие это дела, интересно? Она весь день спит, всю ночь читает или не знаю, что там делает."
    show el sad pioneer at cleft with dissolve
    el "А может… Всё-таки… Пойдёшь?"
    mz "С чего б? Тем более, что там и танцевать не с кем."
    el "Со мной…"
    "Его голос сел окончательно."
    el "Потанцуешь со мной?"
    show mz shy glasses pioneer at cright with dissolve
    show el scared pioneer at cleft with dissolve
    "Покраснели оба. Синхронно отвернулись. Но если Электроника выдавали дрожащие плечи и неестественно выпрямленная спина, то жужелицу, похоже, всё это откровенно раздражало."
    th "Вот больная. Ей парень в чувствах открывается, а она…"
    "А она жгла."
    mz "Помести в свою пустую голову одну простую мысль. Уж найди место, постарайся."
    mz "Я не пойду с тобой танцевать. Ни на прощальной дискотеке, никогда. Даже если ты будешь последним мальчиком на земле."
    show el surprise pioneer at cleft with dissolve
    el "Но п-почему?"
    th "Да какого хрена она творит?! Она же сейчас ему комплексов на всю жизнь надарит!"
    "В его голосе явно слышалось какое-то надрывное смирение."
    el "Я же…"
    mz "Вот именно. Ты же."
    mz "Ты нескладный и неуклюжий дурак. Я не хочу, чтобы меня видели рядом с тобой. Поэтому развернулся и шагом марш в корпус. По лагерю объявлен отбой."
    el  "Ладно."
    "Он старался держать хвост пистолетом, но эту осанку, эти жесты я узнаю из тысячи. Сюжет, которому больше миллиона лет. Слова народные, музыка народная. «Ему отказали». Исполняется в неизвестно какой раз."
    show el normal pioneer at cleft with dissolve
    el "Будь."
    th "Совершенно верно. Не здорова или счастлива — а просто будь."
    "Он выглядел раздавленным. {w}И я прекрасно его понимал."
    hide el with moveoutleft
    "Весь как-то съежившись, он пошёл, не совсем понимая, что с ним происходит."
    "Тоже знакомо. Первые несколько часов чувствуешь себя так, будто тебе надели на голову кастрюлю и как следует влупили по ней половником — в голове пусто и звонко."
    "Показалось, или глаза жужелицы блеснули в лунном свете?"
    "Показалось. У такой бессердечной твари и слёзные железы-то, наверное, отсутствуют."
    "Просто отблеск от очков."
    stop music fadeout 5
    hide mz with dissolve
    "А несколько минут спустя, выждав интервал, исчезла и она."
    "Некоторое время мы просто сидели молча, до боли сжав пальцы."
    show mi dontlike pioneer at center with dissolve
    mi "Как это больно, всё-таки."
    "Наконец, сказала Мику."
    mi "Я просто смотрела, и мне плохо стало. Представляю, каково Электронику… {w} Бедный мальчик!"
    "Дело-то привычное. Не он первый, не он последний."
    me "Евгения, конечно, по-свински поступила. Электроник ничем не заслужил такого отношения."
    mi "О чём ты говоришь?"
    me "О том, как она, не выбирая выражений, в грязных сапогах прошлась по ребёнку, открывшему ей душу."
    me "У меня в жизни мнооого таких деятелей было, прежде чем я огородился пулемётами и провесил колючую проволоку."
    show mi sad pioneer at center with dissolve
    mi "Сёма, ты что такое говоришь-то? Ты разве не видел, как плохо было Жене прогонять Электроника? Она же плакала, когда он ушёл."
    me "Крокодиловыми слезами разве что."
    mi "Неправда, она очень тепло к Сыроежкину относится. Только очень-очень этого боится."
    mi "Не все же такие как ты — способные совершить поступок там, где это требуется."
    "Я покачал головой."
    me "Гораздо хуже то, что Эл теперь очень нескоро будет способен на ещё один поступок. Ты не видела, как он себя заставлять пытался?"
    show mi sad pioneer at center with dissolve
    me "А она уничтожила его. Молодец, задание выполнено."
    "Мику отрицательно покачала головой, но спорить не стала, изобразив вид «ты мужчина, тебе виднее»."
    "Молчание затягивалось, и срочно требовалось что-то сказать."
    me "Хорошо здесь."
    mi "С тобой — да."
    me "И хватит уже об Электрониках и библиотекаршах."
    "Японка молча кивнула и закрыла глаза."
    show mi shy pioneer at center with dissolve
    "А я молча поцеловал её в макушку — всё-таки, спустя сутки — и притянул к себе поближе."
    "Мы знакомы всего третий день."
    "Мы знакомы больше, чем целую жизнь."
    "Пальцы сами чертят на песке её имя."
    "И нет такой цены, которую я не готов заплатить за то, чтобы никогда не отпускать рук."
    mi "Ты такой правильный, что жутко становится."
    mi "Дома у меня девочек учат, что проявление внимания — полностью их прерогатива. И тот рубеж, где ты меня постоянно останавливаешь, рано или поздно должны пройти все."
    show mi grin pioneer at center with dissolve
    me "Рано или поздно. Но лучше вовремя."
    mi "Вовремя? Вовремя — это сейчас, Сёма."
    mi "Я знаю свои силы и свои желания."
    mi "И я тебя как воздух буду впитывать сутками."
    me "Имеешь в виду, что не выпустишь меня из-под одеяла даже водички попить?"
    mi "Даже водички…"
    "Шепнула она, целуя меня в шею."
    show mi happy pioneer at center with dissolve
    me "Пойдём баюшкать, чудо."
    "Содрогнувшись от приятной щекотки, предложил я."
    "Она не выглядела ни разочарованной, ни расстроенной — значит, мои подспудные предположения о том, что она таким образом проверяет меня на прочность, подтвердились."
    me "А на родине у тебя первый же мальчик, с которым случилась обоюдная симпатия, с удовольствием бы затащил тебя в постель."
    mi "И именно потому мне ни разу даже в голову это не пришло."
    "Она безмятежно улыбнулась, целуя меня в висок."
    mi "Но ты прав, хотя мне и жутко не хочется тебя отпускать — глазки уже слипаются."
    me "Я провожу тебя."
    stop ambience fadeout 3
    stop music fadeout 3
    pause(3)
    jump alt_stories_start