label alt_day4_dv_begin:
    scene bg int_aidpost_day with dissolve
    play ambience ambience_medstation_inside_day fadein 5
    play music music_list["my_daily_life"]
    "Дверь без стука распахнулась, и на пороге появилась Алиса."
    "Я еле успел прикрыться одеялом."
    show dv grin pioneer2 with dissolve
    dv "Ага! Вот ты где прячешься, трус!"
    me "Алиса, тебя стучаться никогда не учили?!"
    if alt_day3_dj == 'dv':
        dv "Неколя мне. Я тут с твоей подачи в эфире кручусь, еле время нашла, чтобы зайти."
        "Она выглядела довольной."
        me "Как оно в целом?"
        dv "Ты знаешь… А мне нравится! Оказалось чуть сложнее, чем я думала. Но интересно."
        me "Теперь будешь этим заниматься постоянно, Элис диджей?"
        "Она рассмеялась."
        dv "Разве что это когда-нибудь станет оплачиваемой работой."
    else:
        dv "Учили. Но так никогда ничего интересного не увидишь!"
        "Мне оставалось только вздохнуть от её детской непосредственности."
    me "Ты чего припёрлась-то?"
    "Неласково буркнул я."
    show dv surprise pioneer2 with dissolve
    dv "А не надо было?"
    me "Заметь — я этого не говорил."
    dv "Ага. Ты сделал такой вид, как будто я невовремя."
    me "Ладно, прости. Я просто только-только встал и у меня зверски болит голова."
    "Голова на самом деле не болела — просто было такое чувство, будто мне в голову налили воды, и мозг плавает внутри, периодически стукаясь о стенки черепа."
    me "Не знаешь, что вчера случилось?"
    "Она пожала плечами."
    dv "Я не знаю точно."
    if alt_day3_dj == 'dv':
        dv "Я вела эти ваши танцульки, все танцевали, потом кто-то что-то закричал, все куда-то побежали."
    else:
        dv "Я сидела на эстраде и подбирала лады под новую мелодию, когда с танцпола сделали объявление, где прозвучало твоё имя."
    dv "Я забеспокоилась."
    "Она дёрнула плечом."
    dv "Пошла вместе со всеми к клубам."
    dv "А там ты…"
    "Её голос дрогнул."
    dv "Не шевелишься."
    dv "Я в жизни так не пугалась, подумала себе всякого."
    dv "Хорошо, врачиха успела объявить, что ничего страшного не произошло."
    me "Ага. Ничего страшного, не считая того, что я навернулся на асфальт с верхотуры."
    dv "В общем, она мальчиков припахала, те сбегали за носилками и отнесли тебя сюда. Вот и весь сказ."
    dv "Да, и раз уж ты здесь всё равно бездельничаешь…"
    "Она вышла вон и вернулась с гитарой."
    if alt_day3_date == 'dv':
        "С той самой, на которой мы вчера пытались научить меня играть!"
    else:
        dv "Половины струн не было, пришлось самой натягивать. Цени!"
    show dv grin pioneer2 with dissolve
    "Она рассмеялась, глядя на моё лицо."
    dreamgirl "Ничего-ничего, мы когда её впервые увидели, тоже полчаса смеялись."
    me "Я прямо даже не знаю что сказать."
    show dv laugh pioneer2 with dissolve
    dv "Можешь начать со слога «спа»."
    me "Что?"
    dv "Потом слог «си»."
    "Ненавязчиво продолжила она."
    me "Ой, да, извини. Спасибо, конечно."
    show dv normal pioneer2 with dissolve
    dv "Да ничего, сама знаю, как это тоскливо — болеть. Так хоть руку набьёшь к конкурсу самодеятельности."
    if alt_day3_date == 'dv':
        me "Я всегда могу отказаться."
        show dv smile pioneer2 with dissolve
        dv "Можешь, конечно. А станешь?"
        "Я пожал плечами."
        me "Зависит от графика обучаемости."
    else:
        me "Конкурса? Какого конкурса ещё?"
        dv "С добрым утром!"
        dv "Вчера же не линейке говорили, что в пятницу будет смотр-конкурс самодеятельности."
        dv "Ты записан четвёртым."
        me "ЧТО?!!!"
        show dv laugh pioneer2 with dissolve
        dv "Какой энтузиазм!"
        dv "Ладно, чемпион, поправляйся!"
    "Она подмигнула мне и думала выскользнуть за дверь, но была остановлена окриком."
    me "СТОЯТЬ!" with vpunch
    show dv surprise pioneer2 with dissolve
    "Она выглядела удивлённой, но просьбе — пусть и выраженной несколько матерным тоном — прислушалась."
    dv "Ну чего ещё…"
    "Проворчала она."
    if alt_day3_dj == 'dv':
        dv "Меня и так радиослушатели заждались, а я тут с тобой лясы точу."
        me "Конечно, ты же пластинку на самый конец поставила."
        me "И выбрала, конечно, пятнадцатиминутку."
        show dv smile pioneer2 with dissolve
        dv "Нет, конечно!"
        me "Вот, значит, тогда и не торопимся."
    me "Расскажи мне, что там в лагере творится?"
    "Она пожала плечами и подошла ближе, усевшись на ближайшей койке."
    dv "Да ничего необычного. Разве что тебе может быть интересно, что сегодня родительский день."
    me "Какой?"
    dv "Ну, знаешь, когда дяди и тёти везут в лагерь копчёную колбасу, молоко и прочие весёлые продукты — подкормить умирающих с голода деток."
    me "Ты так говоришь об этом, будто находишься в стороне."
    dv "А я…"
    "Её глаза опасно заблестели."
    dv "Не важно, короче."
    me "И всё-таки…"
    "Она отвернулась в сторону и прочеканила."
    show dv guilty pioneer2 with dissolve
    dv "Эта тема закрыта."
    me "Хорошо-хорошо, как скажешь."
    "Я поспешил свернуться, пока опять не забрался на заминированную территорию."
    me "Давай тогда…"
    "Взгляд заметался по помещению — отпускать Алису решительно не хотелось!"
    me "Сыграем?"
    show dv smile pioneer2 with dissolve
    dv "Имеешь в виду, что я должна сыграть?"
    me "Не я же!"
    "С моим мастерством будет лучше, если я вообще инструмент в руки брать не стану."
    dv "А напрасно! Тебе надо практиковаться, иначе так ничему не научишься."
    me "Алиса, я вчера навернулся башкой об асфальт, и сейчас мой мозг напоминает сырую пористую губку. Как думаешь, способен я сейчас чему-нибудь научиться?"
    dv "Да ты и в обычном состоянии не слишком обучаем."
    "Она рассмеялась, однако взяла пару ладов."
    dv "Главное, чтобы врачиха не пришла."
    "Улыбнулась она."
    dv "Она говорила, что тебе нужен покой и сон."
    "Она тряхнула голосвой и затянула, удовлетворившись четырьмя тактами вступления."
    dv "И мёртвый месяц еле освещает путь, и звёзды давят нам на грудь — не продохнуть. И воздух ядовит как ртуть, и пусть не видно, где свернуть."
    me "И не пройти нам этот путь в такой туман…"
    "Подтянул я и задумался."
    th"Если я ничего не путаю, Хой выпустил пластинку с этой вещью аж в 96-м, но в народе оно к тому моменту гуляло крайне уверенно, кое-кто даже почитал её народным творчеством."
    th "Значит, допустимо предположить, что сейчас приблизительно 88-89-ый год?"
    th "И что мне это даст?"
    th "Даже если Двачевская и знает что-то из творчества Хоя, это ничего не значит."
    th "Да и какая мне разница-то? Если сейчас предперестроечное время то, например, дом, в котором я живу, в нынешний момент ещё даже не построили."
    "И идти тоже особо некуда — припереться к молодой матери — ей сейчас что-то около двадцати шести и заявить: «Я твой сына, люби и корми»?"
    "Я продолжал задумчиво смотреть на девочку, с удивлением замечая, как она краснеет под моим взглядом."
    dv "Чего уставился?"
    "Буркнула она."
    me "Так нравишься."
    "Просто ответил я."
    show dv shy pioneer2 with dissolve
    dv "Я.. чего?"
    "Она сделала вид, что не расслышала."
    me "Побуквенно повторить?"
    me "Или ты считаешь, что понравиться не можешь?"
    dv "Я не знаю."
    "Она совершенно потерялась, однако выучка была видна — пальцы сами перебирали струны."
    show dv shy pioneer2 with dspr
    dv "Семён, я должна тебе признаться в чём-то."
    me "Да? В чём же."
    dv "Понимаешь… Мне очень хочется быть с тобой рядом. Очень."
    "Я почувствовал, что стремительно краснею."
    "От кого-кого, а от нашей железной Алисы я такого признания ну никак не ожидал!"
    me "Ээээ… Я рад."
    dv "Подожди!"
    "Оборвала она."
    dv "Дай я доскажу, пока остатки решимости ещё есть."
    "Я кивнул."
    dv "Так вот, несмотря на всё моё желание… В общем, этот рут ещё не дописан. Такие вот дела."
    "С этими словами со спутника над Германией в нашу сторону ударил лазерный луч, стирающий память."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_dv_begin:
    scene bg int_aidpost_day with dissolve
    play ambience ambience_medstation_inside_day fadein 5
    play music music_list["my_daily_life"]
    if alt_day4_un_fz_companion == 'dv':
        "Я потянулся, улыбаясь солнечным лучам, бьющим мне в лицо."
        th "Вчера денёк был дикий. Просто дикий."
        th "Мало было того, что я навернулся с верхотуры вниз, мало было того, что я лежал в медпункте с сотрясением, а потом без зазрения совести сбежал."
        "Самым диким было вчерашнее поведение Алисы."
        "Она явила миру в лице меня уязвимое нутро, сама того не желая, и горе мне, если я когда-нибудь кому-нибудь осмелюсь заикнуться о том, что и Двачевская, оказывается, бывает слабой!"
        th "Не осмелюсь. {w}И не в страхе дело."
        th "Мне просто… Понравилось? Пожалуй, это самое справедливое и честное слово."
        "Мне невозможно понравилось видеть в Алисе девушку, заботиться о ней, подставлять сильное мужское, если потребуется."
        "Как жаль, что этот рут всё ещё не дописан!"
    with fade
    return