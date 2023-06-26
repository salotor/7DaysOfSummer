label ranger_scary_story:
    scene black with fade
    $ alt_pause(2)
    play ambience ambience_music_club_night fadein 1
    $ persistent.sprite_time = "night"
    scene bg int_library_night2
    show us normal pioneer
    with fade3
    "Вечер продолжался. На очереди был рассказ Ульяны."
    us "Моя история основана на реальных событиях."
    "Почти не улыбаясь, сказала она."
    me "Ага, как же."
    "Усмехнулся я."
    show us dontlike pioneer with dspr
    us "Не перебивай. Значит, дело было так."
    play music music_list['door_to_nightmare'] fadein 1
    scene bg ext_square_day with dissolve
    stop ambience fadeout 3
    $ set_mode_nvl()
    "Лет 20 назад приехал в наш лагерь генсек. Визит был, разумеется, с помпой: куча дядь в пиджаках, корреспонденты, иностранцы даже были. Каждому дали по пакету сладостей."
    "Среди ребят были брат и сестра, совсем махонькая. Брат попросил у генсека видеокамеру. Мечтал, знаешь, режиссером стать."
    "Вождь улыбнулся и сказал: жди ко дню рождения. Смех вожатых. Бурные и продолжительные овации."
    "Местная газета вся в снимках того визита – пионеры нарадоваться не могут: минута славы!"
    "А желание пацана было исполнено, как и обещал генеральный. Теперь он никогда ее не отпускал."
    "Следующее лето в лагере он всюду носился с камерой, снимал все подряд. Глазки горят, бегают, ищут хороший сюжет!"
    "Вожатые оценили талант юнца, даже вели разговоры с директором о создании кружка киносъемки. Вроде как договорились организовать."
    nvl clear
    scene bg ext_clubs_day with dissolve
    "Прошел еще год, снова приехал с сестрой. В рюкзаке – исписанные тетрадки. Сценарист взялся всерьез. В первый день ходил, тестировал."
    "Клуб режиссера открывался на 3 день, задержали поставку пленки."
    scene bg ext_square_night with dissolve
    "Накануне паренек решил снять пустой лагерь после отбоя. Сестренка захотела за компанию, ну и личиком в камеру посветить."
    scene bg ext_house_of_el_night_7dl with dissolve
    "Ходят, снимают. Вдруг у брата кончилась пленка, благо до дома было недалеко."
    "Сходив за ней, поспешил он назад."
    "И вдруг встал, застыв от ужаса."
    nvl clear
    scene bg ext_backdoor_night_7dl with dissolve
    play music music_list["orchid"] fadein 3
    "Сестра стояла у незапертых ворот. За ними виднелся огромный силуэт. Нечто страшное, исполинских размеров."
    "Огромное тело на тончайших ногах-прутьях. Мелкая голова с ведерко, но глаза! Переливаясь ядовитым цветом, как у рептилии, они косились на бедную девочку."
    "И что самое главное, они были человеческие. Ни лица, ни тела не было видно. Только глаза, горящие как фонарь."
    "То, что было дальше, произошло в считанные секунды. Нечто тряхнуло своими руками, и те, хватив сестричку, потащили ее к себе."
    "Удивительно, но она не издала ни звука. Будто, блин, верила существу! Чудовище кинулось в чащу леса."
    "Дальше брат-режиссер уже не видел – банально грохнулся в обморок."
    nvl clear
    scene bg int_aidpost_day with dissolve
    "Откачали его к утру. Орал как резанный, руками махал во все стороны."
    "Кое-как успокоили, хрен знает, что ему там наливали. Весь день валялся в палате, никого не впустил, кроме своего лучшего друга."
    "Потом он взял и пропал. Никто не видел, как он исчез."
    "Только его дружок проговорился, что-дескать брат ушел в лес искать сестру. Прихватил только камеру, фонарик и ножик перочинный – наивный балбес."
    "Приятель дал клятву пионера – не расскажу никому. Но когда по всему лагерю начали бегать вожатые, понял, что дело дрянь, и раскололся."
    scene bg ext_path_night with dissolve
    play music music_list["no_tresspassing"] fadein 3
    "В тот же вечер вожатая с физруком пошла прочесывать лес. Ходили два часа – ничего не нашли."
    "Вдруг заметили по земле неизвестные следы, ведущие к заброшенному лагерю. Следы непростые, мелкие, размером с ладошку."
    "И самое главное – отпечаток сам был похож на человеческую ладонь! Тут уже вожатую пришлось пытать нашатыркой."
    nvl clear
    scene bg int_mine with dissolve
    "Физрук усмехнулся, но по нему было видно, что ему не по себе. Взял ружье и полез в шахту."
    "Блуждал по ней до утра, чудом не заблудился. Ничего не нашел. Почти ничего – в пролете шахты нашлась камера брата."
    scene bg int_chief_office_rain_7dl with dissolve
    "Сели смотреть, что братец успел наснимать. В самый важный момент пленку зажевало, и досматривать пришлось кусками."
    "Неизвестно, что там было, но вожатой после этого вызывали скорая помощь. Физрук же весь поседел, а ведь войну прошел, всякое видеть пришлось."
    scene bg ext_square_day with dissolve
    "В лагере началась паника. Пригнали милицию, скорую."
    "Детей на ночь по домам закрывали на ключ. Хочешь в туалет – ведро в углу. Есть – в столовую при сопровождении вожатых."
    "Пошли слухи среди детей, что в лесу маньяк завелся, волки, НЛО – да что угодно, богатое детское воображение дорисует картину."
    nvl clear
    "Пригнали милицию, скорую. Милиционеров было море. Целыми днями прочесывали местность, ночевали в свободных домиках."
    "С опозданием кто-то догадался, что нечего тут детям делать, и всех быстро развезли по домам."
    "Милиция и в шахту залезла, да что толку? Оказалось, там туннели идут на десятки километров, коридоры путаются, часть шахты затопило и доступа к ней нет."
    "Стало понятно, что при любом раскладе дети навсегда сгинули. Пионера, давшего клятву, слушали без энтузиазма – так, напридумал, ерунда все это."
    "Камера в суматохе потерялась, улик нету, версия со следами ушла в тупик, пропажу детей сослали на несчастный случай. Бардак, блин."
    "Итог – пропавшие брат с сестрой, вожатая в психушке, целый лагерь детей пошел в отказ и ехать на следующий год не хочет. Натуральное ЧП."
    "Родители пропавших все отделы оббегали, даже генсеку писали – провалились как под землю. Обидно до мурашек."
    stop music fadeout 3
    $ set_mode_adv()
    scene bg int_library_night2
    play ambience ambience_music_club_night fadein 1
    show us normal pioneer
    with fade3
    me "Не понял. А куда камера делась-то?"
    play music music_7dl["will_you"] fadein 3
    us "У Ленки спроси, Семен. В тот злополучный год ее отец был одним из тех, кто этот лес осматривал."
    me "Кажется, эту историю пора заканчивать."
    scene bg int_library_night with dissolve
    "Сказал я и задул свечу."
    "В наступившей темноте краем глаза я заметил, что знакомые хвостики исчезли из клуба."
    scene ext_library_night with dissolve
    "Не придав этому особого значения, все разошлись по домам."
    scene bg ext_boathouse_alt_night_7dl with dissolve
    play ambience ambience_lake_shore_night fadein 2
    "Я же, решив напоследок сачкануть от принудительного отбоя, решил тайком прогуляться к реке."
    show un sad pioneer far at fleft with dissolve
    "Перемещаясь через тропинку, я увидел на причале так хорошо мне знакомую грустную девочку."
    "Кинув в реку что-то тяжелое, она посмотрела на полную Луну и тут же скрылась в противоположном направлении."
    hide un with dissolve
    $ alt_pause(5)
    jump alt_stories_start