label alt_day3_begin:
    scene bg black
    show prologue_dream
    with fade
    play music music_7dl["prologue_1"]
    "Today I dreamed of something strange."
    scene bg int_sam_house_clean_7dl
    show prologue_dream
    with fade2
    "Dark room, four bulb chandelier under the ceiling, but, considering that plafonds were overgrown with dust, this light source is used quite rarely."
    "Prefer others."
    scene cg d3_fag_room_7dl
    show prologue_dream
    with fade2
    "For example, that very same, flat, twenty four inch, with «Night light», in order to not disturb sore eyes even more."
    "And there is someone sitting next to it! Someone familiar, shaggy, bushy, gloomy."
    "Fingers lay on WASD by themselves, despite that video games not too much honorable here, just to kill some time."
    "Computer on the left, armies, even mountains of empty botles, pizza and sushi boxes — last is mostly here just to impress some rare guests."
    scene cg d3_fag_room_7dl:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 2.0 zoom 1.5 xalign 0.5 yalign 0.35
    show prologue_dream
    "Is this really me?!"
    me "This bleak, wretched being, hunched over the monitor, with chin resting in the left hand, this is... me?!"
    "I refuse to believe what I see."
    "No, there were problems in my life of course, I've seen them, I knew them, I'm not denying that."
    "But never, you hear me, never it was so bad!"
    "This is not me! {w}No. {w}Not me."
    "I can't, I don't want to be - IT!"
    scene cg d3_fag_room_7dl:
        zoom 1.5 xalign 0.5 yalign 0.35
        linear 8.0 zoom 3.0 xalign 0.4 yalign 0.15
    show prologue_dream
    "So, relax, catch breath."
    "I am in the camp, right? In the camp."
    "With pioneers?"
    "And with Olga Dmitrievna."
    play sound sfx_knocking_door_outside
    dreamgirl "Oh yeaaah?"
    dreamgirl "Don't you tell me then, what cities did you pass to get there? Or you are from the city named City, from the street named Street."
    "And again, I am asking my inner voice to shut up."
    play sound sfx_knocking_door_outside
    "My thoughts were interrupted by an impatient knocking at the door."
    me "What? Who's there?"
    "Those were not my words, but this hairy creature that took my chair."
    voice "Nobody. Stop playing the fool, Semyon."
    "Someone responded from other side of the door."
    voice "I know you hear me."
    me "Leave me alone. I did not do anything."
    "It seems like he cowered and tried to crawl under the system unit."
    voice "How's that, you didn't."
    "Voice seemed impatient and even menacing."
    voice "Then who did? Me, huh?"
    me "I DIDN'T DO ANYTHING! LEAVE ME ALONE!!!"
    stop music fadeout 3
    play sound sfx_intro_bus_transition
    pause(2)
    scene anim intro_15 with fade2:
        zoom 1.5 xalign 0.5 yalign 0.35
        linear 0.4 zoom 1.5 xalign 0.4 yalign 0.15
    pause(3)
    scene bg black with fade
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    pause(1)
    scene bg int_house_of_mt_day with blind_r
    play ambience ambience_int_cabin_day fadein 1
    if alt_day3_duty:
        show mt angry pioneer at center
        if counter_sl_cl == 1:
            mt "I don't want to hear anything. {w}You said you find the keys, and didn't hand them."
            mt "Happy? Now you on duty at the canteen."
            if (alt_day2_date == 'mt'):
                "I frowned, and Olga laughed out loud:"
                show mt laugh pioneer with dspr
                mt "I knew you'd fall for it!{w} The image of the dumb squad leader, huh? This joke would never gets old."
        else:
            mt "Shouldn't have played Frog-traveler yesterday."
        "She stated and gave me towel with all the things I needed wrapped in it."
        mt "Now go wash yourself, you don't have much time, you still need to go to the canteen."
        if not ((alt_day2_date == 'sl') and ('sports' in list_slavya_7dl)):
            mt "Swimming trunks are in the nightstand, if you want to go swimming — when you finish your duty!"
            if (alt_day2_date == 'dv'):
                me "What?"
                mt "Your marathon in wet pants was quite funny, I must admit. But this should be first and last time."
        "Understanding that arguing with squad leader is pointelss, I lazily scraped myself off the floor, dress up and got out straight into the fresh morning!"
    else:
        show mt sad pioneer with dissolve
        mt "Semyon! Semyon! Calm down! It was just a dream."
        "She was seriously scared."
        show mt normal pioneer with dspr
        "But calmed down immediately when I came to my senses."
        mt "I thought of waking you up, but since you've awakened yourself..."
        show mt smile pioneer with dspr
        "She gave me an eloquent look, and I realized that I sit in front of her only with my pants on."
        if not ((alt_day2_date == 'sl') and ('sports' in list_slavya_7dl)):
            mt "Swimming trunks are in the nightstand, if you want to go swimming — should be your size."
            if (alt_day2_date == 'dv'):
                me "What?"
                mt "Your marathon in wet pants was quite funny, I must admit. But this should be first and last time."
        if loki:
            me "What are you looking at, Olga Dmitrievna?"
            "I asked with interest, not even trying to cover myself."
            show mt grin pioneer
            mt "Good morning."
            "With those words she left the cabin giving me an opportunity to dress up."
            hide mt with dissolve
        elif herc:
            "Morning reaction was expected and few seconds of shame over and above compensated blushed cheeks of squad leader."
            show mt surprise pioneer
            me "Seen enough?"
            "I laughed."
            "In this kind of situation either men dresses or woman undresses. Highly doubt that we have second variant here."
            mt "Oh, I was going to woke you up... but as I see you've already..."
            "Her eyesight slided somewhere down."
            me "As you can see, I am already ready."
            "in every single possible meaning of this word."
            me "Can I dress up please?"
            hide mt with dissolve
            "Like in a far boyhood I clenched my asscheeks — there was no other way to get into my shorts."
            "Door slammed behind me, and I couldn't help but grin. Who's embarassed now, huh."
        else:
            "Instantly blushed, I covered with blanket laying nearby."
            mt "Blushing as a schoolgirl."
            "Squad leader didn't lose a chance to tease me."
            me "Olga Dmitrievna!"
            show mt laugh pioneer
            "She laughed."
            mt "Okay-okay, I'm leaving."
            "Door slammed behind her."
            hide mt with dissolve
    hide mt with dissolve
    scene bg ext_houses_sunset
    with flash
    play ambience ambience_camp_center_day fadein 3
    play music music_list["timid_girl"] fadein 3
    me "Uh!"
    "I yelled."
    "Temperature dropped during nighttime, shreds of fog were hanging between the trees."
    "Combined with not rised sun yet we get wet-cold disgusting feeling, and shorts with cotton T-shirt didn't help that too much."
    if alt_day3_duty:
        "Since I was relieved of morning exercise and lineup, I left my neckerchief at the cabin, deep beneath my pillow, and happy with that I quickened to the brass-tiled monster."
        "Pioneers were nowhere to be seen, seems even omnipresent Slavya is only waking up right now."
        "Bliss! For the last 48 hours I wasn't able to be alone. Already started to forget how it feels."
    else:
        "Since I was able to expel squad leader from the cabin, I, of course, «forgot» my neckerchief on my bed and quickened outside."
        "Yes. Wash up."
        "Few pioneers walked past me following Shurik in the line, who seemed to have the best autopilot out of them:"
        show dv normal sport at right
        show mi normal casual at left
        show un normal sport at center
        with dissolve
        "Alisa... Lena... Miku..."
        hide dv
        hide mi
        hide un
        with dissolve
        if (alt_day2_date == 'un'):
            "Hold up!"
            "I caught up with the processing and walked near them."
            me "Psst! Hey! Hello!"
            "I whispered."
            show un smile sport
            un "G-good morning..."
            "She seemed not so self-confident... Even after yesterday. However that was understandable."
            me "Didn't sleep well?"
            un "Is that so noticable?"
            me "Maybe I am not the greatest person here, but I was expecting at least «Hello» from you... and you just walk like a zombie."
            me "If I didn't come up you wouldn't even have noticed me."
            show un shy sport with dissolve
            un "S-sorry, I've got lost in thoughts."
            me "Yea."
            me "I hope you'll have time to think about whatever you want by breakfast."
            "I winked at her and separated myself from the caravan - now it would be time for screaming, and the last thing I wanted was to yell in Lena's ear."
            hide un with dissolve
        elif (alt_day2_date == 'un_fz'):
            "Lena gave me an expressive look and turned away."
            "I did not have time to notice, but it seems that she blushed a little."
            th "That was an awkward scene that came out yesterday. It's like I'm really guilty of something to her."
            "Alisa paid no attention to me at all."
            "Apparently, morning was by no means her favorite time of day."
            th "With that kind of yawn a mouth can be torn!"
            dreamgirl "How do you know? Maybe she's trained!"
            "I chose not to answer the giggling inner pervert. Without him, life was not a sugar."
            sl "Good morning!"
            show sl smile sport with dissolve
            "If there’s anyone who’s definitely not going to lose heart, it’s her."
            "Slavya just caught up with the sleepy procession, looking as if she has enough energy to last an entire year."
            "I difficultly suppressed an envious sigh."
            show sl laugh sport with dissolve
            sl "Cheer up, Semyon! We don't need you to fall asleep with your face in porridge at breakfast!"
            hide sl with moveoutright
            "She laughed out loud and ran forward."
            "I flapped my hand at her – crazy, what did I expect?"
            "There was no other explanation to why she was in such a good mood in the morning."
        elif (alt_day2_date == 'sl'):
            "I, being in approximately the same state, wandered after them."
            sl "Hello!"
            "A disgustingly cheerful voice came from behind."
            "Slavya."
            show sl smile2 sport with dissolve
            "I turned around."
            me "Morning to you..."
            sl "Why so sad? Didn't sleep well?"
            me "Uh-huh."
            "I replied bluntly. {w=.4}I didn't want to speak or smile. {w=.4}And even sun was almost burning through my eyes..."
            sl "Don't be late to morning exercise. And, Semyon..."
            me "Yes?"
            sl "Don't forget, dances are today."
            if alt_day2_bf == 'sl':
                sl "And you promised me something."
                "I rolled my eyes. {w=.4}Oh my God. Yesterday it was so easy to promise, who knew that today it would be necessary to keep the promise!"
            else:
                sl "And I really hope to see you there."
                th "And I will dance, yeah..."
            show sl laugh sport with dspr
            sl "Okay, I won't bother your awakening anymore."
            "She laughed and ran forward."
            hide sl with dissolve
        elif (alt_day2_date == 'dv'):
            "It seems that Alisa was even colder than me, since she did not even begin to tie her hooligan knot under her chest, but walked, ruffling and clasping her shoulders."
            "I caught up with her and touched her on the shoulder."
            if loki or herc:
                me "Hello Beautiful! How is your nothing?"
                show dv surprise sport with dissolve
                dv "What?"
                me "What's not!"
                "I laughed."
                me "How is it going?"
                show dv normal sport with dspr
                dv "Sleep."
                "She answered quitely."
                me "That's a good point. I like it. Let's go then?"
                dv "What? Where?"
                me "This bench looks no worse than the others. We can do here."
                dv "What are you even talking about?"
                "Alisa began to boil, while all the other members of the cavalcade, who understood what I was getting at, secretly giggled."
                me "Sleep of course! {w=.4}And we can even warm each other!"
                show dv angry sport with dspr
                "She stopped."
                dv "You'd better go to the {w}washstands."
                "She turned up her nose, dropping down:"
                dv "Pervert!"
                "At this point everyone seems to be laughing. The morning seems to be done."
            else:
                dv "Hi..."
                show dv normal sport with dissolve
                "She muttered sleepily."
                "Didn't sleep enough. Definitely got tired dragging my clothes around."
                me "Uh-huh."
                "We walked side by side for a while."
                me "What plans for today?"
                dv "Survive."
                "Short and to the point. I nodded:"
                me "Wise. {w=.4}And more specifically?"
                dv "Survive till breakfast."
                "Waking up, her voice was even more hoarse than usual. I walked and smiled at her sounds."
                dv "What's so funny?"
                "She asked languidly."
                me "It's easy to survive till breakfast. It's harder to not fall asleep later."
                dv "What do you want?"
                me "I don't need checklists or anything like that today..."
                show dv shy sport with dspr
                dv "I'm going to play the guitar. You can come too if you want."
                me "Exactly what I was planning on doing!"
                "I smiled and, nodding, increased my pace."
        elif (alt_day2_date == 'mi') and (alt_day2_mi_date != 2):
            "After yesterday, I didn't want to bother Miku. {w=.4}Something seemed to be holding me back and not letting me go."
            "Unfortunately, she had already noticed me and, coming closer, grabbed my hand.."
            show mi laugh casual with dspr
            mi "Here you are! And I kept wondering if you were awake or not. It's good that I woke up, the morning is good, though it's cold, but it's nothing, right?"
            "The machine gun girl fired up her cartridge belt and returned to her usual rate of fire."
            mi "And yesterday you left so unexpectedly, and I kept thinking about what you said..."
            show mi shy casual
            extend " and what you did."
            "The girls present exchanged meaningful winks."
            "It seems that what happened yesterday on a completely deserted beach suddenly became public."
            "As if, besides us, our whole squad was present there."
            me "Chatterbox is a godsend for a spy."
            mi "Do you think I told them? {w=.4}It's not me, honest-honestly, really-really, that's..."
            show mi serious casual at center with dissolve
            "She lowered her voice."
            mi "Picture."
            me "Picture? What picture?"
            mi "Yesterday, after the beach, I came to the cabin, and there Lena was sitting and crying. And on the table is a simple picture, drawn in pencil. And on it was you.{w=.5} We. Well, you understand…"
            "Wow. Has anyone seen us long enough to even draw us? How did I not noticed that?"
            show mi smile casual with dissolve
            "The answer was simple and continued to chatter."
            mi "I wanted to say about yesterday - I'm not very used to such signs of attention, in Japan men are much more restrained in showing emotions, so I feel dizzy, and I don't really understand what to do."
            me "Miku... it was {b}you{/b} who showed emotions, not me..."
            show mi serious casual with dspr
            "She went silent."
            if loki or herc:
                "I took her by the hand."
                me "Yesterday you swore at loneliness. {w}Lack of attention."
                me "We will eradicate them."
                me "And since you like me, I'll try to make you a company."
                show mi laugh casual
                mi "I am in. And after that?"
                me "We'll see."
            else:
                "I was also silent. What else could be said?"
                "A few minutes later we reached the washbins and fled to different sinks."
    scene bg ext_washstand_day with dissolve
    if alt_day3_duty:
        play sound sfx_open_water_sink
        play sound_loop sfx_water_sink_stream fadein 1
        me "A-a-a-a-a!"
        "I greeted the morning camp."
        "The water was even colder than yesterday, and I seriously considered leaving one sink full overnight. Let it warm up a little."
        me "A-a-a-a!"
        "Another handful of ice flew into my face,behind someone muttered sleepily:"
        us "Well, could you please stop yelling, my head was already hurting... now this."
        show us sad sport
        "I turned around and found Ulyanka behind me."
        "She stood over the sink with a displeased face and closed eyes."
        if counter_sl_cl == 1:
            me "What kind of typhoon got you up so early?"
            us "Duty."
            "She creaked."
            th "There was no sadness..."
            me "So, we are on duty together."
        me "Didn't slept well?"
        us "Uh-huh."
        "She was back in her Soviet polo shirt and corduroy shorts."
        me "That's because you ate an entire cake!"
        "I pointedly raised my finger."
        me "Sugar overdose!"
        show us normal sport
        us "Oh, screw you."
        play sound sfx_open_water_sink
        play sound_loop sfx_water_sink_stream fadein 1
        "She unscrewed the faucet handle and cautiously touched the water with her fingertips."
        "And suddenly an idea came to my mind."
        "Ulyanka is all such a fidget, nimble and cheerful. But one question can only be answered experimentally."
        "I held my hand under water until I felt the cold turn into pain - for ten whole seconds."
        show us fear sport with easeinbottom
        "And then, having crept up to the small one from behind, I put my hand behind her scruff!"
        us "EEEEEEEE-EEEEEEEE!" with vpunch
        "She can!"
        "She definitely can! {w}I mean, scream."
        us "You! You! You..."
        "She was trying to catch her breath, looked unkindly and planned something clearly unkindly."
        "And I didn't even have time to react - she instantly jumped to the tap, unscrewed it at full power, and spreading her thumb and forefinger, pressed the skin between them to the tap, leaving a small gap for the water to exit."
        play sound sfx_draw_water
        "A steep water arc stretched in my direction!"
        "I barely managed to jump sideways. More sideways! Until I thought of hiding on the other side of the washbins."
        us "You are crazy!"
        "Ulyana stated."
        if counter_sl_cl == 1:
            us "Not only did you not let us get into the dining room, starving a child, but now you also want to freeze her like a Thing!"
        else:
            us "Not only did you want to run away yesterday, now you want to kill me!"
        me "That's not true! Achtu..."
        play sound sfx_water_emerge
        extend " Pfu!"
        "I peeked out from behind the tiled side to object, and immediately received a decent portion of ice-cold water right in the face."
        show us laugh sport
        us "A-ha-ha-ha-ha!"
        "The petty one burst out laughing, and, considering herself avenged, she returned to where she started."
        play sound sfx_open_water_sink
        play sound_loop sfx_water_sink_stream fadein 2
        "Yes! She had absolutely no intention of washing herself with such water! Instead, she again turned the jet down to a minimum and continued to touch it with her fingers."
        me "Little one, what are you doing?"
        us "It's like you can't see it yourself. {w}I'm touching the water."
        me "May I know why you're touching it?"
        us "Stupid man. It's been known for a long time that if the water is too cold or too hot, you just have to let it flow a little."
        me "It doesn't work here."
        us "In the city, so it works, but not here? Why?"
        me "Because it's not a city, little one! The water here is taken from a local river, and there it is - you can go touch it - about the same temperature!"
        "Somehow I had a strange feeling."
        "As if Ulyanka is mocking me in some incomprehensible way. {w}But in what way?"
        stop sound_loop
        play sound sfx_close_water_sink
        us "Well, okay. Then I won't wash at all I guess."
        "She turned off the water, and rolled everything she had time to lay out in a towel."
        play sound sfx_close_water_sink
        me "Okay. Don't wash your face. Just do it quickly, please. Okay?"
        stop music fadeout 3
        play sound sfx_7dl["wakeup_horn"] fadein 5
        "Above the camp, the still low signals of the pioneer horn trumpeting Up were heard."
        me "Eight. We need to be at the canteen."
        show us dontlike sport
        us "Crap! Don't remind me! It's all because of you!"
        "I couldn't believe my ears."
        me "Because of me?! And why is that may I ask?!"
        if counter_sl_cl == 1:
            us "Because you snitched on me and Alisa, I know!"
            me "Wow, what an accusation! {w}Why did they put me on duty then?"
            us "Because you're a dunk!"
            "She cut off."
            me "Great. So you got punished because I snitched on you, and me for being a dunk?"
        else:
            us "Because you escaped poorly!"
            me "So, the fact that you overdose with the cake, that you didn’t get enough sleep, and that we are now going to the canteen to hunchback, is solely my fault, right?"
        show us smile sport with dissolve
        stop sound
        us "Well, you finally got it! {w}Okay, I don't hold a grudge against you, a klutz is a klutz."
        play music music_list["what_do_you_think_of_me"] fadein 3
        "I was about to say something sharp and in general to stop the little girl, so that she would think a little - to whom she was saying what, when she added:"
        if counter_sl_cl == 1:
            us "And most importantly, all for nothing!"
            us "We didn't even got our food that night!"
        else:
            us "The next escape will do as I say!"
            me "Next escape?! Are you serious?"
            us "But of course! Let's go through the woods this time!"
        me "Oh, screw you."
        "I packed my things and headed for the house."
        if counter_sl_cl != 1:
            us "Hey, whats wrong? You don't want to escape anymore?"
        hide us with dissolve
        "She was shouting something at my back, but I had already left."
        scene bg ext_houses_sunset with dissolve
        "Pioneers slowly swayed and prepared for a new day."
        show sl smile2 sport at center with moveinright
        "Slavya resiliently ran past me, giving me a fleeting smile."
        "The dew-soaked uniform was tight around her in all the right places, I forced myself not to stare after her."
        if (alt_day2_date == 'dv'):
            "She wanted to stop and chat, but, apparently, she remembered something - blushed a little and drove off towards the square."
        hide sl with moveoutleft
        "Alisa, Lena and Shurik walked past me in the «Zombie» mode."
        show dv normal pioneer at left
        show un normal pioneer at center
        show sh normal pioneer at right
        with moveinleft
        "It seems that it was useless to try to get through to them, since they did not react to the greeting in any way."
        hide dv moveoutbottom
        hide un moveoutbottom
        hide sh moveoutbottom
        show mi smile pioneer
        with dissolve
        "Miku, whom I had not seen since yesterday, on the contrary, was already vivid, cheerful and extremely active:"
        mi "Hello, Semyon!"
        mi "I wanted to say good morning, but you look so sad that I thought it might not be good for you at all, so I chose something neutral!"
        "She spoke in one word."
        me "Hi Miku. How did you sleep?"
        mi "The best! I found a bug under the blanket that was wiggling its whiskers in a funny way and was trying to escape, so I caught it and released it."
        mi "And Lena squealed so much at the sight of him! She is so strange, isn't she? The beetle, maybe, wanted warmth..."
        show us normal sport at right with dissolve
        show us grin sport at right with dspr
        "Or maybe it's not the desires of the beetle, but the pranks of one red-haired youngster..."
        hide us with dissolve
        "She was saying something else, but I safely ignored everything, again lost in my own thoughts."
        if 'music' in list_clubs_7dl:
            mi "Anyway, after ten o'clock I'll be waiting you for the first rehearsal!"
        else:
            mi "I really hope you'll be there too!"
            me "Wait..."
            "Sorry, I'm a little lost. What are you talking about?!"
            me "Excuse me, but «there» is where?"
            show mi laugh pioneer
            mi "At the disco! Be sure to come!"
        "She concluded and, with a dazzling smile, jumped off towards the washbins."
        "And I had no choice but to go to the canteen - the food will not digest itself and the pioneers will not be fed by themselves."
        "I want to say that in all normal camps they switched to a self-service system a long time ago, but this is clearly not our case."
        "The local pioneers will crucify me if they come to breakfast and find no food on the tables."
        "Well, or maybe not crucified, but simply maimed. In any case, you should hurry."
        "Ulyanka, even though I have a head start, will still be at the dining room earlier."
        scene bg ext_dining_hall_away_sunset with dissolve
        "Sharp cries were already heard from the square, counting the rhythm of the exercises, and I didn’t even want to, whether I’m glad or not that I’m not swinging now along with all my arms, legs and other limbs."
        "An absolute plus is that they are now standing in the cold, and they still have a lineup. And a minus... {w=.3}Yes, most likely, they will force me to peel potatoes!"
        stop sound
        stop sound_loop
        stop ambience
        scene bg ext_dining_hall_near_sunset with dissolve
        play music music_list["get_to_know_me_better"] fadein 5
        "Of course Ulyana managed get bored while waiting for her to be launched to a work facility, she did not even remember about dousing on the washstands."
        show us smile sport
        us "Took you long enough. Did you bring the keys?"
        me "No. And how do I even suppose to get them."
        me "Our entrance is on the other side."
        us "I somehow didn't think of that."
        "She confessed and immediately turned around to run further, if only I hadn't put my hand on her shoulder and turned her around."
        "She took two steps and rested against me before it dawned on her that she was moving, to put it mildly, in the wrong direction."
        show us surp1 sport
        us "Oi, and what are you doing here?"
        "I sighed and mentally forbade myself from dreaming of strangling this petty source of trouble. No one will appreciate it."
        me "That's it, cut the jokes, now we quickly cover, clean up and scatter before lunch."
        us "Nuh-uh.{w} At dinner yesterday, the menu for today was posted, there will be mash again, so…"
        me "We're peeling potatoes. So, we better work together then. Sooner we start..."
        scene bg int_dining_hall_sunset with fade
        "We walked around the perimeter of the canteen and knocked from the staff entrance, where food trucks usually drive up - by the way, never seen them arrive."
        play sound sfx_knock_door7_polite
        pause(1)
        "We were studied for some time through the glass door, and finally the lock clicked, unlocking."
        voice "Helpers arrived, huh?"
        "The big lady in a white suit and apron smiled. The cook, it seems."
        "Ulyanka wanted to say something, but I quickly rubbed her back and smiled as politely as I could:"
        me "Of course, helpers! Always wanted to see the insides of a kitchen!"
        voice "Wow, what a well-mannered young man. Thats your chance to see of course."
        play sound sfx_open_door_2
        scene bg int_dining_hall_day with fade
        "We were ushered into the holy of holies, past the utility rooms, right into the hot heart of the kitchen, where huge aluminum cauldrons were already gurgling on the melted stoves, spreading the smell of rice porridge and cocoa around them."
        "I looked longingly at some drier woman, who, with us with a practiced movement, opened a can of condensed milk and knocked it over into a pan with cocoa."
        "Ulyanka didn’t care at all about this - after looking around a bit, she immediately found an ownerless dressing gown and threw it on herself, immediately turning into a kind of ghost."
        show us laugh sport at center with dspr
        "The dressing gown was five sizes larger, and she completely drowned in it."
        "There was laughter from behind - it seems that the cooks have already managed to appreciate all the benefits of Ulyana's stay here.{w} It remains only to keep her busy before her destructive tendencies spoil the first impression."
        me "So where do I start?"
        voice "Ah, yes, simple. Washing hands."
        me "That's understandable. What's next?"
        voice "Arrange the glasses on the tables according to the number of chairs, take the teapots and pour the cocoa."
        me "That'd be easy."
        "After rinsing my hands, I drove a cart to the distribution and unloaded everything I needed onto it."
        "The work went quickly and quickly. Egoza and a hooligan, Ulyanka turned out to be an indispensable assistant - like everything she did, she gave herself entirely, working from the heart and as quickly as she could."
        scene bg int_dining_hall_people_day with dissolve
        "So we set the tables for the junior squads quickly, even having time to have a little fun with a normal human coffee in the back room before the doors opened and launched the first pack of hungry pioneers into the canteen."
        "We didn’t serve the senior squads, such was the agreement between the camp administration and the canteen employees - the latter were tired of the fact that the seniors constantly did not want to eat anything."
        "As a result, the senior squads were now completely self-servicing."
        "Needless to say, this found the most lively response in the ranks of the pioneers. Nobody forced you to take what you are not going to eat."
        "Well, in any case, if you managed to come in with your squad. Otherwise, the leader could well have taken a portion for you, as, for example, it was yesterday, when I was confronted with the fact that «You should eat it and I don't care»."
        "I found myself standing leaning against the wall and smiling paternally as I watched the hungry pioneers occupy the tables and quickly work with spoons, consuming the cooked food."
        if (alt_day2_date == 'un'):
            if loki:
                "And I gave the same fatherly look to Lena, who appeared in my field of view, to which she, unable to resist, stuck out her tongue at me."
                "Almost like Ulyanka yesterday."
                show un laugh pioneer
                un "Good morning, or are you still sleeping?"
                me "slpn."
                "I grunted, dissatisfied with the fact I being mocked."
                un "Come on, let's eat someone!"
                "Not listening to my objections, she grabbed my arm and dragged me to the distribution."
            else:
                "It seems that I was too deeply immersed in thoughts, because I reacted to Lena who appeared before my eyes from nowhere, involuntarily shuddering."
                show un smile pioneer
                un "Good morning."
                "She smiled, pleased with the effect."
                me "My god! Don't scare me like that."
                un "Are going to eat? Or..."
                show un shy pioneer at center with dissolve
                "...She don't have anyone to eat with. I guessed."
                me "Let's go."
                "Taking a tray from the table, we took a turn at the distribution."
        elif (alt_day2_date == 'sl'):
            "Slavya, as usual, approached silently and stood beside me."
            show sl normal pioneer at center
            sl "And this is the picture I see every day."
            if alt_day2_walk == 2 and not herc:
                sl "By the way, I was thinking about what you said yesterday. About the rescuers."
                me "And?"
                "I asked blankly."
                sl "It seems to me, that the highest form of help would be saving lives."
                me "And you won't miss it..."
                "I waved my hand pointedly."
                show sl laugh pioneer
                sl "I will, of course! But I think that every person has his own place. And I seem to have found mine."
            me "Well, at least someone will be in they place. Let's go eat?"
            "We took our turn at the distribution."
        elif (alt_day2_date == 'dv'):
            "Probably, my smile was really stupid, since the already familiar tap on the shoulder was accompanied by a hoarse laugh."
            show dv smile pioneer2
            dv "Let's go eat, wUiter!"
            "Dvachevskaya was in her repertoire and, not listening to my objections, dragged me to the distribution"
        else:
            "So I shuddered when Ulyanka heartily slapped me on the back."
            show us smile sport
            us "Don't sleep, you'll freeze!"
            "I nodded meaningfully."
            us "Let's go, sleepy head!"
            "She grabbed my hand and dragged me to the distribution, in the meantime pushing away those who had already managed to get in line, all saying:"
            us "On duty! On duty! Feed us out of turn!"
        return
    else:
        play music music_list["my_daily_life"] fadein 2
        $renpy.notify('Meeting Place Can not Be Changed - Movie name.')
        "Here we are again, Meeting Place Can not Be Changed."
        "I shivered in advance, anticipating how the cold passes through the skin and muscles, reaches the bones, ache in the joints. And if you also brush your teeth…"
        show blinking
        "I have to do everything quickly, otherwise I won't get it together."
        "I held my breath, and..."
        scene bg ext_washstand2_day
        with dissolve
        play sound sfx_open_water_sink
        pause(1)
        play sound_loop sfx_water_sink_stream
        me "A-a-a-a-a-a!" with vpunch
        "Absorbed by the struggle with numb limbs, I forgot about everything, and, as it turned out, in vain."
        "I have already said that it was quite damp outside, plus the feeling of ice water."
        "What is now lacking for happiness?"
        "Correctly."
        scene bg ext_washstand_day with dissolve
        "I've always imagined how my body fights the cold."
        "It speeds up the metabolism, kicks the liver for more energy, the skin gets goosebumps, lifting the hairs that hold the layer of warm air."
        "The skin is starting to get warm... Warm! It's getting hot."
        "And now someone has put an icy palm on this hot skin!"
        me "A-a-a-a-a!"
        "Icy moisture, coming into contact with my hot skin, hisses and evaporates, clouding the surroundings with white steam."
        "I, like the first day, understand."
        "I WILL F...!"
        play music music_list["eat_some_trouble"] fadein 2
        if (alt_day2_date == 'dv'):
            show dv laugh sport with dissolve
            "Alisa stood nearby, leaning her hand — wet! — on the tiled wall."
            "Looks like she was shaking with laughter."
            dv "Ha-ha-ha!"
            "She wiped away her tears."
            dv "Sorry, I couldn't resist."
            "The pioneers present here exchanged puzzled glances."
            "The only exception was Lena, who seems to have guessed everything."
            "And I, in the meantime, I took such a tangible portion of water in my palms - I didn’t even feel the temperature from anger! - And carefully poured everything on the top of the laughing girl."
            hide dv with dissolve
        else:
            me "ULYANAAAAA!"
            "Even without turning I already knew — who!"
            show us laugh sport with dissolve
            us "Gi-gi-gi!"
            "Seems like she found her entertainment for today."
            "I restrained."
            "Didn't started to scream at her."
            "I just poured water into a soap dish and carefully poured it down her collar."
            "You definitely should have seen how she beats me!"
            if (alt_my_rival_semifinal.take == 'us') and (alt_day2_gamblers_result['me'] >= 21):
                "Even compared to yesterday's beating, it was brutal."
                if loki:
                    "Just at one fine moment, tired of enduring the beatings, I grabbed her across the torso, pressing my hands to her sides, and several times shoved her head under the still pouring water."
                else:
                    "Actually, this time I didn’t sit and wait. I stepped back in time and, putting my hand on her forehead, waited a few minutes until she got tired of swinging her limbs in the air."
                    "Yes, my arms are longer. And yes, I shamelessly use them."
            hide us with dissolve
        stop sound fadeout 3
        stop sound_loop
        scene bg ext_house_of_mt_day at fast_running
        with dissolve
        "A little chase to disperse the blood."
        "And, running into the cabin, slam the door and lean against it, breathing a little."
        scene bg int_house_of_mt_day with dissolve
        "Small fists immediately hit the plywood from the other side."
        if (alt_day2_date == 'dv'):
            dv "YOU BETTER OPEN THIS DOOR YOURSELF!"
        else:
            us "OPEN UP, YOU, PEST!"
        "Yeah, gimme a sec to spread out a red carpet."
        "I took a breath and opened my eyes..."
        "Only to find out that, as it turns out, I'm not alone in the cabin!"
        if persistent.hentai_graphics_7dl:
            scene cg d2_mt_undressed with dissolve
        else:
            scene black
        play music music_list["awakening_power"] fadein 0
        "Olga Dmitrievna was facing the mirror..."
        "She was changing!"
        if persistent.hentai_graphics_7dl:
            scene cg d2_mt_undressed_2 with dspr
        mt "Semyon?"
        if (alt_day2_date == 'dv'):
            "I shot out of there like a bullet, in the middle of the movement I catched Alisa and dragged her away!"
        else:
            "I shot out of there like a bullet, in the middle of the movement I catched Ulyana and dragged her away!"
        scene bg ext_house_of_mt_day with dissolve
        if (alt_day2_date == 'dv'):
            show dv surprise sport at cright with dissolve
        else:
            show us calml sport at cright with dissolve
            us "Hey! What are you doing?"
        "I glared angrily at the reason that I once again goofed."
        "What am I? Really. What am I?"
        "Where did I make a mistake, which she considered for permission to beat me and bully me in every possible way?"
        "Or do you need permission for such things?"
        stop sound_loop
        show mt angry sport at cleft with dissolve
        "Olga appeared on the porch, and I angrily threw a hand, which, I just noticed, I was still squeezing."
        if (alt_day2_date == 'dv'):
            me "Alisa... by definition, we can't have a peace, can we?"
            dv "Peace? If I wanted peace, I would lie under the bed. Shake it up!"
        else:
            me "You little... I will get punished again... and again because of you."
        if (alt_day2_date == 'dv'):
            "I think I really looked furious as Alisa took a step back."
        else:
            show us sad sport with dspr
            us "Wha me gain?!"
            "She protested."
            me "Nothing."
        mt "Semyon, would you mind to explain your behaviour?"
        "It seems, she was quite angry."
        if (alt_day2_date == 'dv'):
            me "Alisa."
        else:
            me "Ulyana."
        me "If I recall correctly, we have a morning exercise right?"
        "She nodded."
        me "Then start runinnnng!"
        "And we ran."
        stop music fadeout 5
        scene bg ext_square_sunset with dissolve
        play ambience ambience_camp_center_day fadein 3
        "Morning exercise was same as yesterday, only difference that now I didn't find myself alien compared to everyone else."
        if (alt_day2_date == 'un'):
            show un smile sport at center with dissolve
            "Lena, just like yesterday, indifferently waving her hands, smiled in response to my nod."
            "And she seemed to cheer up a little. {w}Seriously?"
            "I don't want to become a catalyst person. After all, I don't know how long I'm here, I don't want to give groundless hopes."
        elif (alt_day2_date == 'sl'):
            show sl smile sport at center with dissolve
            "Already usually active, today Slavya literally was shimmering with some kind of energy, colloquially called enthusiasm. In terms of the degree of liveliness in the performance of some exercises, she could now seriously compete with Ulyanka."
        elif (alt_day2_date == 'dv'):
            show dv smile sport with dissolve
            "After winking with Alisa, we took a place on the side and began to engage in nonsense. We started with the «wave»."
            "I picked up a bump from the ground, and, making sure that no one sees, I launched it into the leaning Ulyanka."
            show us dontlike sport at left with dissolve
            "She instantly straightened up and gave me a suspicious look. Well, what about me? I took on the most innocent look that I could."
            "I could not much it seems, so I did not convince anyone, and my own throwing projectile flew at me. I did not remain in debt, and Alisa joined in."
            "Everything was in use - cones, small pebbles, in the meantime they robbed the green rose hips - everything to the front!"
            "Slavya wisely did not pay attention to us, since it is not known what the attempts to reason with us would have resulted in."
        else:
            "While there wasn't much of a difference overall, it was more of a matter of mood."
            "I gradually began to get involved in social life, to feel like a part of something."
            show us grin sport at right with dissolve
            "Ulyanka."
            hide us with moveoutright
            show sl smile sport at left with dissolve
            "Slavya."
            hide sl with moveoutleft
            show un smile sport at right with dissolve
            "Lena."
            hide un with moveoutright
            show dv smile sport at right with dissolve
            "And even the red-haired bandit Dvachevskaya."
            hide dv smile sport with moveoutright
            "All of them treated me kindly, humanly, and for a fraction of a second, with an absolutely inexplicable instinct, I almost managed to smell that elusive thing that had gone out of my life, leaving an empty shell near the monitor to smolder."
        scene bg ext_square_sunset with joff_r
        play music music_list["get_to_know_me_better"] fadein 5
        "Finally, the sports ordeals were completed, and it was decided to move from the health part to the administrative part."
        "To put it simply, to the lineup!"
        show sl smile sport with dissolve
        "Today Slavya acted exactly the same as yesterday - she took my hand and took me to our place, despite even the indignant look that certain someone gave us both."
        if (alt_day2_convoy == 'sl'):
            sl "I didn't forget."
            "She whispered."
            me "What are you talking about?"
            sl "Your help, of course."
            sl "But just saying thank you wouldn't be enough."
            "Of course, girl, my torment in the square wasn't enough."
            sl "That's why... You raise the flag again today!"
            me "What? No! No, don't even think about it."
            "She laughed."
            sl "I didn't think so, it was a decided fact yesterday."
            sl "Okay, get ready, bye, I'll run and change."
        hide sl with dissolve
        "We again stood almost under the very stands, however, the difference was already in the fact that after yesterday my face was more or less familiar to the crowd, and they periodically winked at me, made faces and simply nodded approvingly."
        "There was only one question left."
        "Who are all these people, and what the hell do they want?"
        "Little by little, the square filled with people, and I curtailed my torments and, like yesterday, switched to spiritual food."
        "To put it simply, I went into a half-memory, half-dream…"
        if (alt_day2_date == 'un'):
            if loki:
                "I remember the forest insofar as it is much more strongly imprinted in my memory what my inner commentator has done."
                "Although now, after the fact, I understand that everything that idiot in my head has said…"
                "It all led to the current, extremely pleasant consequences."
                dreamgirl "You're welcome, dear."
            elif herc:
                if (alt_day2_date == 'un_fz'):
                    "Yesterday Lena behaved very peculiarly."
                    "It would seem that everything started so well - and boom!"
                    "I could not comprehend the logic of some women even if I wanted to."
                else:
                    "Yesterday's impromptu exhibition of Lena's work... It's hard to say whether it was what we both expected, or if we should have spent less time painting and more each other..."
                    "In any case, I do not regret my decision. Thanks to it, I realized that everything is much more complicated with this camp than it seemed at first glance."
            else:
                "Yesterday's completely unusual, but this did not become unpleasant sensation when my back touches... touches... mmm..."
        elif (alt_day2_date == 'dv'):
            "A retrospective of the threats, the conclusions, the pictures taken, and something else jumbled up in my sick imagination."
            "Yesterday's bet with such conditions that any other girl has already burned out of shame a hundred times."
            "The problem is not even that Dvachevskaya is not any other."
            "The problem is that with her physique, gossip takes on the features of a documented fact."
            show cg d2_2ch_beach with dissolve:
                alpha 0.5 pos (0, -250)
            "I once again imagined before my eyes a cheeky muzzle, a blade of grass bitten in the corner of the mouth, desperate and ruthless eyes..."
            "A chiseled neck with a dimple, orange strings holding the upper part of the swimsuit, holding on to the developed shoulder girdle ..."
            hide cg with hpunch
            "And I forbade myself to think about it. I don't want to glow with my «natural reactions» in front of the entire lineup."
        elif (alt_day2_date == 'mi') and (alt_day2_mi_date != 2):
            "One thing can be said about Miku - exotic. Like a pinch of cayenne pepper, which adds fire to any dish."
            "Actually, I was always attracted to Japanese girls, there was something in them that resonated inside with sweet languor and a premonition of something incredible."
            "Damn, I even had to date with one Asian. {w}However it was a little and not for long."
            "But what was there was enough to guarantee the experience."
            "I recall that from a girl's point of view, too decisive actions are automatically regarded as an confession of feelings."
            th "So, by offering her a shoulder and talking abstractly about a possible relationship, I somehow confessed to her... sympathy?"
            th "Love? A person you first met a few hours ago?"
        else:
            dreamgirl "This camp is a pristine preserve of unscared beauties."
            dreamgirl "Do you remember that show in the cabin? {w}Olga in the bare minimum of clothes, hmmm... Shouldn't have jumped out, but offered her to zip up where it's tight."
            if (alt_day_binder != 1) and (counter_sl_7dl == 0) and (herc or loki):
                dreamgirl "Or do you remember our activist? {w}Didn't you notice how tight the shirt is on her top ninety-six?"
            dreamgirl "Explain to me why you’re being such a limp-dick?? {w}If you don't like bigger or older girls, try this red lightning..."
            dreamgirl "Well, or..."
            if (alt_day2_date == 'un_fz'):
                th "Yeah, after yesterday that «or» is already enough..."
            th "Just shut up. You're my perverted ego, not the other way around. {w}So we're looking away now..."
            th "Looking. Away. I said!"
            th "From Dvachevskaya's shirt to a wild rose bush."
            show dv grin pioneer far at right with dissolve
            "Alisa noticed the look and winked with both eyes."
            hide dv with dissolve
        "And by the way lineup is already started!"
        if (alt_day2_convoy == 'sl'):
            sl "Let's go?"
            "I swallowed the objection. They don't seem to matter at all."
            sl "Let's go."
            "Just like yesterday, other people's views entwined me, someone else's attention hung on my legs like pound weights, and the old disease broke out again, forcing me to feel every muscle and guide them consciously - as a result, wooden and awkward, with trembling and pain. "
            "I'm not afraid of the crowd. {w}I hate it."
            show sl normal pioneer at cright
            show mt normal pioneer at cleft
            with dissolve
            "Slavya, either enjoying it, or completely indifferent to the streams of attention, with a cheerful, slightly skipping step, she crossed the square and froze on the right side of the podium, from where Olga was already reading a thanksgiving."
            mt "Today we want to encourage our new family member, Semyon, who not only successfully joined the team, but also showed respect for other people's work, order and rules. {w}He volunteered to be an activist's assistant and cleaned the square."
            mt "Note! On the very first day! Someone has a lot to learn from Semyon."
            me "So that's how grateful you are."
            "I hissed at Slavya."
            "She didn't raise an eyebrow."
            sl "I knew you'd like it."
            mt "Semyon! Go!"
            "The events of yesterday were vaguely remembered, and, to tell the truth, they looked more like an unexpired nightmare."
            "Now I realize how merciful memory is. {w}She didn't retain half of her impressions."
            show sl serious pioneer with dspr
            mt "And today Semyon is encouraged by raising the flag! Second time in a row! Honor and glory!"
            hide mt with dissolve
            "I took three steps on unruly legs and stood near the flagpole"
            show sl smile pioneer with dspr
            "Slavya stood next to me, smiling softly."
            dreamgirl "Actually... Notice the shape and size of her pupils. She seems to be feeling guilty. She just can't figure out why."
            dreamgirl "Look, if you want to talk her into something stupid, act now!"
            th "On the lineup?!!!"
            dreamgirl "Don't be a retard, dumbass! No one will hear you now, take advantage of the situation!"
            "I gave her a hateful look."
            "She was embarrassed and averted her eyes."
            show sl shy pioneer at cright
            sl "Lets do it, like yesterday."
            "She made her way, passing me to the cable."
            hide sl with dissolve
            "And this time I didn't feel any gratitude. {w}If I'm not a fool - and she wasn't a fool - She should already understand the size of the pig she slipped me."
            th "Damn me if I would help her anytime again."
            "I was well aware that I was lying to myself. {w}That I could not refuse, looking into those eyes, that I would grumble, grumble and bargain, but as a result I would melt and do everything as she wanted."
            "As I said, this girl picked up a universal code for me and sculpted what she wanted out of me."
        else:
            "This time, no one bothered me, and I was able to go deep enough into dreams - so much so that I even shuddered when Slavya, who was getting out of the lineup, hit me with her shoulder."
            "She didn't linger at the stands, instead going straight to the mast."
        "The flag was silently raised and everyone, like yesterday, like many days before, followed him with their eyes."
        "And at such moments I wanted to give myself a vow to become, if not better, then at least purer."
        "After all, purity of thoughts is the first step towards self-improvement."
        "And it seemed shameful to think about what could have happened if... {w}In the USSR, there really was no sex, there was love."
        play sound sfx_7dl["eat_horn"] fadein 1
        "My thoughts were interrupted by the sound of a horn, and this time I moved along with the squad."
        show mt smile pioneer at fleft with dissolve
        "Olga descended from the podium and smiled in response to my questioning look."
        "It seems that she no longer held a grudge for the scene in the house."
        show mt normal pioneer with dspr
        mt "Semyon, free time until lunch. Do you want to look for some outfit for the evening?"
        "I looked over the uniform."
        me "What's wrong with my form?"
        mt "Weeell..."
        "She thoughtfully looked somewhere into the sky, as if reading clues in small print on the clouds."
        show mt smile pioneer with dspr
        mt "People usually try to dress up better for dances. After all, the event doesn't happen every day."
        me "Come on."
        "I snorted."
        me "The fact that pioneers on the dance floor are dressed up in dresses and trouser pairs does not overwrite the fact that they are still pioneers."
        show mt normal pioneer with dspr
        mt "As you wish. In any case, this does not exempt you from attending the event."
        show sl smile pioneer with dissolve
        sl "I think Semyon will have someone to dance with anyway."
        if alt_day2_convoy == 'sl':
            "Slavya laughed a little tensely - apparently, her conscience still tormented her for the way she treated me."
        elif alt_day2_bf == 'sl':
            "Slavya laughed - clearly hinting at my yesterday's promise."
        me "Yes, yes. Can I go consume something now?"
        show sl laugh pioneer
        show mt laugh pioneer
        with dspr
        "Now they both laughed and allowed me to go into the canteen."
    stop sound fadeout 3
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_bf:
    play ambience ambience_dining_hall_full fadein 3
    play music music_list["everyday_theme"] fadein 3
    scene bg int_dining_hall_people_sunset_7dl with fade
    "The dining room was noisy, crowded and uncomfortable. Everything was the same as always."
    "I took myself a portion and stopped, choosing where to sit."
    if alt_day2_date == 'sl':
        call alt_day3_lp_checker(alt_dater = sl)
        if counter_sl_7dl == 3:
            $ lp_sl += 1
            "Although, what am I even considering? With Slavya of course!"
        else:
            "Although there was nothing to think about - since Slavya was still standing nearby."
            "The place next to Slavya is one of the safest places in the camp... If you have nothing against publicity, of course."
        show sl normal pioneer with dissolve
        me "Bon apetit!"
        sl "Thanks."
        "It seems that she, for some unknown reason, suddenly felt uncomfortable and was silent for ten whole seconds, not even smiling."
        show sl smile pioneer with dspr
        "Finally, she managed to control herself and, as a starter gesture, smiled, leaning slightly towards me."
        "And she sat down like that... like that! I «lost myself» again. Nightmare. If not for my young body, which is controlled mostly by hormones, I would avoid the company of this girl like fire."
        show sl smile2 pioneer with dspr
        sl "Semyon..."
        me "Hm?"
        "I forced my eyes away from what she emphasized with the pose and tried to make eye contact. Not for long, but already a good start."
        "In general, it is difficult for me to communicate with a person, looking him eye to eye, and even more so with those who do not understand a different style of communication."
        show sl shy pioneer with dspr
        sl "Do you want to go to the beach today?"
        me "To the beach?"
        if ('sports' in list_slavya_7dl):
            sl "Yeah, we'll continue yesterday's bussines."
        else:
            sl "Yes. I haven't had many opportunities lately. Moreso I prefer to swim in..."
            sl "In other places."
        me "Swim? That's all?"
        me "Something hard to believe."
        show sl smile pioneer with dspr
        "She smiled shyly."
        me "Do you need help at the beach?"
        "I guessed."
        "She nodded, blushing in the proccess."
        menu:
            "Deal":
                $ alt_day3_date = 'sl'
                $ counter_sl_cl = 2
                me "Catch you up on that."
                "I impolitely pointed my finger at her."
                show sl normal pioneer with dspr
                sl "That's even better!"
                if alt_day3_duty:
                    me "Give me just an hour, I'll finish at the canteen."
                    sl "It doesn’t in rush for me, don’t overwork too much, an hour and a half is at your disposal."
                    "I finished with cocoa and stand up from the table.{w} I've had an epic quest of cleaning the canteen awaiting me."
                else:
                    me "See you after breakfast."
            "Nah, that'll not work":
                me "Sorry, not today."
                "I looked away."
                show sl normal pioneer with dspr
                sl "Well..."
                "She smiled helplessly and shrugged her shoulders as if startled."
                sl "I understand, sorry."
                "The rest of the breakfast passed in deathly silence."
                $ lp_sl -= 1
                $ karma -= 10
        return
    menu:
        "Sit with Lena":
            call alt_day3_lp_checker(alt_dater = un)
            if (alt_day2_date == 'un_fz'):
                "The place next to Lena was empty."
                "I was about to move towards her, but something stopped me."
                th "This is a bad idea."
                th "I'll just embarrass the girl if I sit next to her"
                "No, I was really wondering what caused that outburst of jealousy last night, but now was clearly not the best time to sort things out."
                "There are a lot of people here, so it's impossible to talk calmly."
                th "I'll only spoil Lena's appetite with my mug."
                th "No, we'll save all the talk for later!"
                "And I hurried to take the vacant table by the window."
                "He was just out of the girl's line of sight, which was good for both of us."
            else:
                "I decided to sit down with Lena, especially since she clearly didn't mind my company."
                "To be honest, I blamed the atmosphere of the place. Not on the air, but on something that lives in it, giving spirit and idea to this whole pioneer world, something without which this place would look like scenery."
                "And that's why it was much easier to communicate and do things that are completely unusual for me personally."
                "In Lena, I saw my thirst for loneliness, and she also gave me a clue - you can be alone and together. After all, just being alone is not an end in itself. The goal has always been to enclose something personal."
                "I slowly finished off the rice porridge, casually glancing at the girl:"
                show un smile pioneer at center with dissolve
                un "You've been looking at me like that for three days now..."
                me "Is that bad?"
                un "Very. Bad."
                "Her voice dropped to a whisper."
                un "I can get used to it."
                un "And then it will be very, very bad for me if someone - let's not point the finger - will no longer try to look a hole into me."
                me "Was that a threat or an offer?"
                show un laugh pioneer with dspr
                un "And you can't decide? Do you want me to choose for you?"
                "I shook my head."
                me "Can everything be spontaneous? I like surprises."
                if (alt_day2_date == 'un'):
                    un "Maybe so... Tell me, what are you going to do after breakfast?"
                    me "Either go to the clubs where I signed up, or..."
                    show un normal pioneer with dspr
                    "I froze when I saw her eyes darken."
                    me "I mean, I wanted to say... that I would like to spend time with you."
                    "Feeling like a complete henpecked, I replied."
                    show un laugh pioneer with dspr
                    un "Wonderful!"
                    "She smiled and, leaning across the table, whispered:"
                    un "Pick me up from the library in thirty minutes, okay?"
                    menu:
                        "Agree":
                            $ alt_day3_date = 'un'
                            $ counter_un_7dl = 2
                            if not ('library' in list_voyage_7dl):
                                me "What's in there?"
                                un "There's a wall newspaper editorial office in the book depository."
                                me "A whole newspaper?"
                                un "Yes. The boys are arguing, Zhenya is sleeping. And I am working."
                                un "Steal me from there, okay?"
                            me "Of course."
                            show un smile pioneer with dspr
                            hide un with dissolve
                            "She smiled gratefully in response and, having collected the dishes, got up from the table."
                            if not alt_day3_duty:
                                "I followed her up and left the dining room."
                        "Refuse":
                            me "Sorry, not today."
                            "I smiled guiltily."
                            show un serious pioneer with dspr
                            un "Its okay."
                            un "I understand."
                            un "Forgive me too."
                            hide un with dissolve
                            "She instantly picked up her half-eaten breakfast for the second time and got up."
                            if not alt_day3_duty:
                                "I followed her up and left the dining room."
                            $ lp_un -= 1
                            $ karma -= 10
                else:
                    show un serious pioneer with dspr
                    un "I'm afraid you won't like this surprise at all."
                    un "You look so good next to her."
                    me "Next to who?"
                    if (alt_day2_date == 'sl'):
                        un "To Slavya..."
                    elif (alt_day2_date == 'dv'):
                        un "To Alisa..."
                    elif (alt_day2_date == 'mi'):
                        un "To Miku..."
                    else:
                        un "Forget it."
                    "She suddenly stiffened sharply and, picking up the tray, got up from the table."
                    hide un with dissolve
                    "I followed her up and left the canteen."
        "Sit with Slavya" if counter_sl_cl == 1:
            call alt_day3_lp_checker(alt_dater = sl)
            if (alt_day2_date == 'un_fz'):
                show sl normal pioneer with dspr
                "Yesterday Lena made a scene of me because of Slavya."
                "But it seems like aggravating is the only thing I'm really good at."
                "In any case, sitting next to Slavya seemed like a bad idea to me already at the moment when my arse sank onto the bench."
                th "Though you really don't know."
                "Lena gave me a look full of indifferent contempt and turned away."
                "She really doesn't seem to care."
                "And this means that you should not continue to try to break through the wall with your forehead."
                sl "Hi. How are you?"
                me "Nothing new since morning."
                show sl smile pioneer with dspr
                sl "Stability is good too! What are you going to do today?"
                me "I don't know."
                th "Darn fresh cuts?"
                sl "Listen, yesterday I heard here that you and Lena…"
                "I have lifted up my eyes."
                show sl laugh pioneer with dspr
                sl "What a funny reaction!"
                "Slavya laughed."
                sl "But in general, is it true or not?"
                me "No. I am absolutely free and belong only to myself."
                show sl smile pioneer with dspr
                sl "That's so beautiful!"
                me "I'm sorry, what?"
                sl "Oh."
                show sl shy pioneer with dspr
                sl "I wanted to say - why haven't you found anyone interesting to make friends with yet?"
                me "That's how I am, so unsociable."
                "After all, this cannot be called a lie in the strict sense of the word. After all, if Lena rejected me, I really am free."
                sl "Listen, maybe we'll go to the beach? No, no, don't think about it, you have to referee a volleyball match there, but I'm physically unable to do it."
                "I didn't want to go somewhere where there would be crowds of people."
                me "Sorry, another time."
                sl "Well. a pity. {w}I'll try to find another helper."
                "She answered, standing up from the table."
                hide sl with dissolve
                if not alt_day3_duty:
                    "A few minutes later, I got up, wondering what to do."
                    stop ambience fadeout 5
                    scene bg ext_dining_hall_near_sunset
                    with fade2
                    "So without inventing anything, I got out into the street and, aimlessly studying the dining room building, turned around and wandered to the gate."
            else:
                "Although there was nothing to think about - since Slavya was still standing nearby."
                "The place next to Slavya is one of the safest places in the camp... If you have nothing against publicity, of course."
                show sl smile pioneer with dissolve
                me "Bon appetit!"
                sl "Thank you."
                "It seems that she, for some unknown reason, suddenly felt uncomfortable and was silent for ten whole seconds, not even smiling."
                "Finally, she got over herself and, as a starter gesture, smiled, leaning slightly towards me."
                "And I sat down like that ... like that! I swam again. Nightmare. If it weren't for my young body, which is controlled mostly by hormones, I would avoid the company of this girl like fire."
                show sl smile2 pioneer with dspr
                sl "Semyon…"
                me "Hm?"
                "I forced my eyes away from what she emphasized with the pose and tried to make eye contact. Not for long, but already a good start."
                "In general, it is difficult for me to communicate with a person, looking him eye to eye, and even more so with those who do not understand a different style of communication."
                show sl shy pioneer with dspr
                sl "Do you want to go to the beach today?"
                me "To the beach?"
                sl "Yes. I haven't had many opportunities lately. Moreso I prefer to swim in..."
                sl "In other places."
                me "Swim? That's all?"
                me "Something hard to believe."
                show sl smile pioneer with dspr
                "She smiled shyly."
                me "Do you need help at the beach?"
                "I guessed."
                "She nodded, blushing in the proccess."
                menu:
                    "Deal":
                        $ alt_day3_date = 'sl'
                        $ counter_sl_cl = 2
                        me "Catch you up on that."
                        "I impolitely pointed my finger at her."
                        show sl normal pioneer with dspr
                        sl "That's even better!"
                        me "Give me just an hour, I'll finish at the canteen."
                        sl "I'm not on the rush, don't overwork too much, an hour and a half is at your disposal."
                        "I finished with cocoa and stand up from the table.{w} I've had an epic quest of cleaning the canteen awaiting me."
                    "Nah, that'll not work":
                        me "Sorry, not today."
                        "I looked away."
                        show sl normal pioneer with dspr
                        sl "Well…"
                        "She smiled helplessly and shrugged her shoulders as if startled."
                        sl "I understand. I'm sorry."
                        "The rest of breakfast passed in deathly silence."
                        $ lp_sl -= 1
                        $ karma -= 10
        "Sit with Alisa":
            call alt_day3_lp_checker(alt_dater = dv)
            if (alt_day2_date == 'un_fz'):
                show dv normal pioneer2 with dissolve
                "Lena completely froze me yesterday, so frankly, I was afraid to get close to her."
                "So the choice was between Miku and Alisa."
                "Sighing, I sat down with Alisa, ignoring the deliberately indifferent look Lena gave me."
                th "For God's sake. {w}If you want to show contempt, do it."
                th "Only I'll recuse myself at this vanity fair."
                "Dvachevskaya chewed slowly, looking at me, and if not for yesterday's events, such attention would have been at least pleasant."
                "Finally, she couldn't take it anymore."
                dv "Quarreled?"
                me "Huh?"
                show dv smile pioneer2 with dspr
                dv "Guh. {w}You both look like your grandmothers died. Quarreled?"
                me "In order to quarrel with someone, there must be some kind of relationship with them. {w}And there is none."
                "Alisa only pursed her lips in disbelief."
                dv "Anyway, listen. {w}I'm going beyond the camp area. You can join if you want."
                me "And who else would come?"
                show dv laugh pioneer2 with dspr
                dv "Me and you, you and me. Is that not enough?"
                "After thinking for a bit, I shook my head."
                me "Sorry, no. I'm not in the mood right now."
                dv "Your choice."
                "She replied as she got up."
                hide dv with dissolve
                if not alt_day3_duty:
                    "A few minutes later, I got up, wondering what to do."
                    stop ambience fadeout 5
                    scene bg ext_dining_hall_near_sunset
                    with fade2
                    "Since I didn't come up with anything, I got outside and, after aimlessly studying the canteen building, turned around and wandered to the gate."
            else:
                "After some thought, I chose a seat next to Alisa."
                "Three minutes later, she leaned closer to me and whispered:"
                show dv smile pioneer2 with dissolve
                dv "Don't want to be part of those foolish events, and I'm going to run away. Are you with me?"
                me "I'd be right happy to."
                "I paused and looked for Olga to go away."
                me "But where?"
                show dv grin pioneer2 with dspr
                dv "I think to take a guitar and rush to a small rock."
                me "Small what?"
                dv "Ah... You probably don't know. Here, next to the camp, there are small and large rocks. To the small one we usually go on hikes, burn fires, all that."
                me "It's far, isn't it?"
                dv "Forty minutes on foot."
                show dv smile pioneer2 with dspr
                "She narrowed her eyes."
                dv "Think you can handle it?"
                menu:
                    "Easy!":
                        $ alt_day3_date = 'dv'
                        $ counter_dv_7dl = 1
                        me "Better make sure you don't drop your guitar."
                        "I grumbled."
                        me "I'll take care of myself somehow."
                        show dv laugh pioneer2 with dspr
                        dv "That's a deal."
                        if alt_day3_duty:
                            me "I think you understand that... I'm on duty. I need to at least clean and sweep this place after breakfast."
                            dv "That's ok, I will definitely not deprive you of such joy. Come to the stage after your «Duty» we'll go from there."
                        else:
                            dv "Wonderful. So, I'm waiting for you at the stage, from there we'll stomp."
                        "It seems that everything related to Dvachevskaya begins with the stage. I nodded thoughtfully and suddenly caught Lena's interested look."
                        show un scared pioneer far at left with dissolve
                        me "I think someone heard us."
                        "I nodded towards the unexpected listener."
                        show dv angry pioneer2 with dspr
                        me "Let's not make a scene here."
                        me "We discuss details at the stage."
                        show dv normal pioneer2 with dspr
                        dv "Okay."
                        "She took a deep breath, calming down.."
                        dv "I will go. Meet where we agreed when you're done here."
                        hide dv with moveoutright
                        "Alisa got up and left the dining room without giving Lena even a glance."
                        show un normal pioneer far with dspr
                        stop music fadeout 3
                        "And she suddenly got bored and reluctantly stuck a spoon into the rest of the porridge."
                        play music music_list["goodbye_home_shores"] fadein 3
                        show un shy pioneer far with dspr
                        "She looked up and shuddered, meeting my questioning gaze. {w}Turned away."
                        "I shrugged. It seems that this girl is not very contactive. Although she is keenly interested in others, she is in no hurry to demonstrate that interest."
                        "Maybe it makes sense to approach her yourself and talk?"
                        "Yep, now. As soon as I stop bleating and blushing..."
                        "Why am I like that by the way?"
                        "If you keep in mind that in a situation where we - well, just imagine! - will communicate, it should be equally embarrassing for both of us."
                        show un serious pioneer far with dspr
                        "It is so? And this means that in order for the dialogue to move from the stage of pulling words with pliers to a constructive phase, we need?"
                        "What...? They don't teach that on the internet."
                        "On the word «internet» i've remembered my morning dream, starring me-spectator and me-/b/-tard."
                        "Maybe this is how my subconscious signals that it is ready to rebuild itself on its own and rebuild me as well?"
                        "Something like a reassessment of life values ​​and a new prioritization."
                        "Although it’s unlikely... My fear of changes is strong enough: I probably wouldn’t be able to get married, I would run away from the altar - I really don’t want to change the picture of things that is already familiar to me."
                        "All this I thought, looking at Lena and nodding in time with my thoughts."
                        show un shy pioneer far with dspr
                        "And she was ready to fall straight through the ground - almost like me on the lineup yesterday!"
                        "Here it would be necessary to show misanthropic solidarity, {w=.4}instead of shaking my head and looking at her like an exhibit at an exhibition!"
                        "I glanced at the girl again - this time guiltily - and saw that she seemed to have already finished her meal and was hastily leaving the canteen, trying not to meet my eyes."
                        hide un with dissolve
                    "Sorry, but no":
                        me "Sorry, another time probably."
                        "I smiled guiltily."
                        show dv normal pioneer2 with dspr
                        dv "Well..."
                        "She sighed."
                        dv "It was foolish to expect something from you."
                        hide dv with moveoutright
                        "She got up and walked out of the canteen without even taking the dirty dishes away with her."
                        $ lp_dv -= 1
                        $ karma -= 10
        "Sit with Miku" if (alt_day2_mi_date != 2):
            call alt_day3_lp_checker(alt_dater = mi)
            if (alt_day2_date == 'mi'):
                show mi happy pioneer with dissolve
                mi "Sem, come here!"
                "She waved her arms with all her enthusiasm, calling for me."
                "That's who really doesn't care about public opinion."
                "And by the way our foolishness with her on the beach has already become public!"
                if (not alt_day3_duty):
                    "Damn, someone even drew a picture of us, Miku wouldn't lie about that."
                "The only question is why I, usually hostile to other people's attention, and, like any other sociophobe who feels it burning and tickling under the skin, suddenly did not pay attention to the fact that I was being closely examined?"
                th "What's the matter?"
                th "Is it that I was watched by someone who knows those principles very well, because they themseves is like that?"
                "And from such shyness, the only one that came to mind."
                me "Miku, can you tell who the artist just by looking at a drawing?"
                show mi normal pioneer with dspr
                mi "Not sure. Firstly, there can always be an imitation for the style of work, and secondly, in the completed work, the lines and strokes always look different than on the sketch."
                me "I just have a suspicion that the picture you were talking about belongs to the pen of Lena herself."
                show mi surprise pioneer with dspr
                mi "Yea-ah?I didn't even think about that! Or rather, I thought that we were settled next to Lena because we are both creative people, but it would be more logical to settle me with Alisa then, since we are both musicians."
                me "Do not rush. You were settled with Lena not only because of the creative streak in each of you. It's not the criteria of resettlement that we are interested in. Just remember all the work of Lena that you had to see - if, of course, you had to, and..."
                "Then I remembered something:"
                me "Maybe you still have that drawing?"
                show mi shy pioneer with dspr
                mi "No, sorry. I didn't think it's that important."
                th "Is evidence important in a case? The correct answer - depends for what side."
                me "Okay, there's nothing we can do about it. {w}Let's work with what we have."
                "I looked into her eyes."
                me "Do you remember what the drawing looked like? Was it similar to other works of your neighbor."
                un "Yes, it was."
                "There was a voice from above. Looks like we've been listened for some time."
                "I raised my gaze."
                show un serious pioneer at left with dspr
                me "And?"
                un "What?"
                me "Don't want to tell us something?"
                un "Tell what?"
                me "Is it your drawing or not?"
                un "Even if it's mine. What's the matter?"
                me "Nothing, really. It’s just that now we don’t have to rack our brains in search of a source of gossips."
                me "But to be honest I didn't expect something like that from you."
                show un evil_smile pioneer with dissolve
                un "Still waters..."
                show un normal pioneer with dspr
                un "Okay, I won't distract you anymore. You seem to have something to discuss."
                hide un with dissolve
                mi "She is right, now the pioneers won't leave us alone, eliciting details."
                me "Let them try. I already have my own ways of «talking» with such curious people."
                "The main thing is that Viola should not be dragged into this case - this woman seems to know how to disturb anyone!"
                mi "I'm in the club now, and you? Will you go?"
                menu:
                    "Of course":
                        $ alt_day3_date = 'mi'
                        if alt_day3_duty:
                            me "Just let me finish my duty first."
                            mi "Excellent!"
                            show mi smile pioneer with dspr
                            mi "I'll sweep the club in a meantime then!"
                            mi "Will be waiting for you!"
                            "She quickly finished off the remnants of breakfast, and, instantly delivering a tray to the dishwasher, disappeared behind the doors."
                        else:
                            me "Of course."
                            show mi happy pioneer with dspr
                            mi "Excellent! Will be waiting for you in a half an hour!"
                            me "Maybe we can go together then?"
                            mi "We can. But firstly I need to do something that Olga Dmitrievna asked me for."
                            me "Knowing Olga... I'll be there sooner than you it seems."
                            "She laughed and left the canteen."
                            "And I, having hesitated between a full-fledged healthy diet and the company of a girl, chose a girl after all."
                    "Sorry, but...":
                        me "Maybe tomorrow? I have plenty of things to do today."
                        "I smiled guiltily."
                        show mi upset pioneer with dspr
                        mi "Oh, I understand."
                        "She hunched over."
                        mi  "Yesterday wsas magical evening when dreams come true."
                        mi "And today Cinderella got her pumpkin confiscated because of her debts."
                        show mi sad pioneer with dspr
                        mi "Too bad that our fairy tale happened to be so short"
                        "She turned and left the canteen. Something suddenly stinged in my chest."
                        "Something alive, which was completely dissatisfied with the thought, impossible in its cruelty. — «And you will not see her anymore»."
                        $ lp_mi -= 1
                        $ karma -= 10
                        "I finished my meal and left the canteen."
            else:
                show mi smile pioneer with dissolve
                mi "Hi!"
                "She looked disgustingly fresh and cheerful."
                "Frankly, I was afraid to sit next to such an active girl, especially considering that I was completely square-headed after my sleep."
                "Too bad, I didn't had a choice."
                "I had to eat as is."
                show mi smile pioneer with dissolve
                mi "Syom... why are you soo gloomy?"
                "She stretched out"
                me "Don't call me that."
                "I muttered grimly."
                mi "I wrote a new song, do you want me to sing it?"
                me "Right here?!"
                "Now she got me scared!"
                show mi laugh pioneer with dspr
                mi "Of course not! I don't even have an instrument."
                mi "Come to the club after breakfast, will you?"
                "I shrugged."
                show mi smile pioneer with dspr
                mi "Be sure to come. You will be my dearest listener."
                "It seems that she put a little more meaning into this word than is expected."
                "Otherwise, why did I blush and tried to hid in my plate?"
                me "I... Cough-cough... I'll think about it."
                mi "I will be waiting!"
                "She once again dazzling smile and got up from the table."
                "I followed her up and left the canteen."
                $ alt_day3_mi_invited = True
        "Sit with Ulyana" if (alt_day2_date == 'un_fz') and not alt_day3_duty:
            label alt_day3_bf_us:
                show us normal sport with dissolve
                "To my high astonishment, Ulyana was sitting alone."
                "Alisa was discussing something with Miku at the next table, and the topic of their conversation obviously did not worry the little fidget too much."
                "Memories of how Ulyana loved to add notes of Chinese cuisine to the regular dishes, which slightly take away the desire to sit next to her, but common sense suggests that this is the right decision."
                th "In the end, to be jealous of me for a little one - you need to be a noble pervert!"
                dreamgirl "Yah? You think she's small?"
                th "Very small. A meter and a half tall, nigh non-existent sex appeal, and instead of love in her brain, an awl up her arse."
                dreamgirl "This is fixable. Whe she'll grows up a little - you will bite your elbows that you missed such a madam!"
                dreamgirl "And in general, while she's still a child, she can be customized. At the end you will get the perfect girl.{w} Why are you so slow-witted?"
                th "We'll talk when she'll grow up."
                th "And anyway, back off! You ruin my appetite."
                show us laugh2 sport with dspr
                us "Newbie, it seems you are a local Don Juan?"
                show us grin sport with dspr
                "I almost dropped the tray from my hands."
                me "What are you..."
                if (alt_day2_convoy == 'sl'):
                    us "Yesterday morning you dated Slavya, in the evening you visited Lena, and today you decided to switch to me?"
                elif (alt_day2_convoy == 'dv'):
                    us "Yesterday morning you dated Alisa, in the evening you visited Lena, and today you decided to switch to me?"
                "Oh my god, as if everything else wasn't enough. They are all crazy!"
                show us laugh sport with dspr
                "Looking at my dumbfounded face, Ulyana laughed out loud, causing Alisa and Miku to look around at our table."
                us "Sit down already, do not stand like a pillar!"
                "I obediently sank into a chair and began to sip cloudy cocoa in large gulps."
                "I could expect such tricks from Alisa, but certainly not from Ulyana."
                show us smile sport with dspr
                us "But I'll warn you right now: you're not my type. So don't count on anything!"
                show us laugh sport with dspr
                "Splashes of cocoa, on which I had safely choked, sprayed the entire table."
                with vpunch
                "Some of them also hit Ulyana, which, however, did not prevent her from rolling with laughter."
                me "Fie on you! Why is it that every time I sit down to eat with you, something goes wrong?"
                show us smile sport with dspr
                us "And the fact that maybe it's you hasn't crossed your mind?"
                "I chose to swallow this joke and silently buried my face in the plate."
                "The porridge here was excellent - not like the one that we had in the military."
                th "All the best for the kids, as they say."
                show us normal sport with dspr
                us "Listen, are you busy after breakfast?"
                me "Have you thought about asking me out on a date? I'm not your type, remember?"
                show us dontlike sport with dspr
                us "Of course not! What are those thoughts? With you - and on a date?"
                "Ulyana pretended to vomit into a bowl of porridge."
                show us normal sport with dspr
                us "There is something I need to do."
                "She got a little more serious."
                us "And I don't mind your help."
                th "What is this, I wonder? Steal cutlets from the canteen?"
                me "And then again to receive a scolding from Olga Dmitrievna? A tempting offer to say the least."
                show us smile sport with dspr
                us "And I can tell everyone that we went on a date. With that we will support your reputation as a womanizer!"
                me "No thanks. I think I have other things to do."
                show us shy2 sport with dspr
                "Ulyana looked at me so plaintively that I felt ashamed."
                us "But pleaaaasee!"
                th "What a difficult child!"
                th "After all, I understand with my brain that I don’t owe her anything, and she’s probably up to some kind of dirty trick, but how can I refuse?"
                th "Literally a cat from «Shrek»! I'll be unable to sleep if I drop her now."
                menu:
                    "Agree":
                        $ counter_un_fz = 1
                        me "And what do I get from that?"
                        show us grin sport with dspr
                        "Ulyana shimmered."
                        us "You can't be so mercantine! Pioneers should help each other!"
                        me "Its mercantiLe, you, ignorant!"
                        "I lightly slapped the girl on the forehead with a spoon."
                        show us calml sport with dspr
                        "She grimaced."
                        me "So what needs to be done?"
                        show us grin sport with dspr
                        us "Come to the pier, and I'll tell you there."
                        show us smile sport far with dspr
                        "The girl winked at me and jumped out from behind the table."
                        "She whispered something to Alisa, who was sitting nearby, and rushed to the exit from the canteen."
                        hide us with moveoutleft
                        "Of course, she left the dirty dishes on me."
                        th "That's what you get for being good to others. They sit down on your neck with the legs hang down!"
                        "I took both trays to the sink and looked around. The canteen was almost empty, and Lena was gone."
                        th "I'll have to try to talk to her as soon as I get a free minute."
                        th "I hope Ulyanka doesn't kill me with her assignment."
                        "An inner voice chuckled as if amused by my hopes."
                        "Well, I signed up for this myself."
                    "Refuse":
                        "No, I won’t allow you to twist ropes out of myself."
                        me "How about you do something useful to a society? {w} Maybe you want me to hand you to Slavya?"
                        show us sad sport with dspr
                        "Ulyana frowned sharply."
                        us "Well, I don't need anything from you. I can manage everything myself."
                        "Sitting next to her after that was uncomfortable."
                        hide us with dissolve
                        "For half a minute, stuffing the remnants of porridge into myself, I left the canteen, trying not to notice Ulyana's gaze drilling into my back."
                        dreamgirl "Well, you're an asshole! Spoiled the mood of the child in the morning!"
                        th "And rightly so.So she won't run into trouble."
        "Alone":
            if (alt_day2_date == 'un_fz') and not alt_day3_duty:
                "While I was thinking about my daily business, the last empty table was occupied by three pioneers from the younger group."
                th "Well shoudn't be so slow!"
                "I had no choice but to move to the nearest free place - next to the little one."
                jump alt_day3_bf_us
            else:
                scene
                $ renpy.show("bg int_dining_hall_people_sunset_7dl", at_list = [zentercenter], what = Noir("bg int_dining_hall_people_sunset_7dl", brightness = -0.4, saturation = -0.4))
                "Deciding that I can fool around at any time, but food should be consumed in a calm atmosphere, I decided to eat alone."
                "In a few minutes my plate was empty - it looks like I got really hungry after that night!"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_bf_duty:
    play ambience ambience_dining_hall_empty fadein 3
    scene bg int_dining_hall_day with dissolve
    "And after another ten minutes, the hall was empty - the pioneers were criminally good at destruction of food suplies!"
    scene bg ext_dining_hall_near_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    "I went outside and intercepted Ulyana, who was thinking of running away:"
    play music music_list["i_want_to_play"] fadein 5
    show us sad sport at center
    $renpy.notify("Vladimir Kuts - a Soviet long-distance runner")
    me "Come on, you, Kuts! We need to finish the morning nightmare first - and you can go wherever you want."
    us "Meh..."
    "She got upset."
    show us smile sport
    us "And I didn't want to ran away at all! I thought I'd go for a jog while you're having breakfast there!"
    me "Of course-of course!"
    me "But there the tables are not wiped and the floor is unswept. {w}Waiting, you know?"
    "She nodded and went into the hall ahead of me, immediately grabbing a mop:"
    scene bg int_dining_hall_day with dissolve
    us "I will be sweeping from the other side, and you - from this! Let's roll!"
    me "Wait, where are you going? {w=0.4}Tables first, everything else later."
    show us dontlike sport
    us "Ugh... I don't want tables. {w}There is always something left. {w}Especially after the minors!"
    "Here we are witnessing an escalation of age-based chauvinism, gentlemen, please move away from the cage."
    me "You can't help it, such is the bitter bread of the duty officer."
    me "Yes, and after that we are not free yet remember? We'll go to…"
    show us calml sport
    us "Peel potatoes..."
    "She sighed and suddenly lost all her enthusiasm."
    "And really, who would like a reward for cleaning an entire canteen - in the form of an opportunity to peel potatoes for the entire camp?"
    me "Hmmm.. {w}Slavya?"
    show us normal sport
    us "What?"
    me "Slavya would love to be here right now. {w}There is so much opportunities to use foolish hands and head. {w}To sweeping the floor for example."
    us "You called Slavya foolish?"
    me "No, I called hands and head foolish. {w}Get moving, I wouldn't want to spend the night here."
    "She only snorted and threw off her grief, returning to the status of a red tornado. {w}She did everything in good faith, and it took me a lot of trouble to move in the same rhythm with her, so when half an hour later we clapped palm on palm, meeting in the middle, I felt like a driven horse."
    "At least a canteen was clean."
    voice "Oh, you already finished?"
    "Was heard somewhere from the kitchen."
    voice "Alright! Our machine is already finished. Come here."
    show us normal sport with dspr
    us "You come here!"
    "Ulyanka mimicked. It turned out unexpectedly funny."
    "The kitchen itself was also shining here - apparently, the children were not allowed in. They were cleaning on their own."
    play ambience ambience_7dl["elevator"] fadein 2
    "Huge stoves crackled as they cooled, in the back room - judging by the abundance of taps, it was dishwawing room - the boilers were already drying out, and most of the workers had left."
    "There was only that same cook whose name I forgot to ask, and now it was completely embarrassing to do so."
    us "What is this buzz?"
    "Ulyanka asked casually hiding behind my back."
    voice "That's our machine, don't mind it."
    play sound sfx_open_door_1
    pause(1)
    scene bg int_potato_storage_7dl with dissolve
    "With these words, cook unlocked the door, and a metal monster appeared to our eyes, clanging its mouth and vibrating as if it is ready to fly away any second!"
    voice "Potato peeler."
    "She said proudly"
    voice "One of the newest models."
    us "And what are we doing here then?"
    show us sad sport with dspr
    me "We will hunt for 'eyes'."
    me "Because «Newest potato peeler» cannot do that."
    "I grinned."
    voice "You got it right! That's good, don't have to explain anything."
    "She looked around the room, wondering what offer to us, then dusted off a chair and pointed to it."
    voice "Littl{b}e{/b} one will sit here. And for you I’ll figure out a stool or a box."
    voice "Knives on the table, fill one of the cauldrons a third full with water and get to work."
    voice "When you're done, tell me, I'll come in and take the job. Is everything clear?"
    show us smile sport with dspr
    us "Roger, cook-ma'am!"
    voice "Not just a cook, but a chef! I'll be back soon. Boy, you can start working while standing. If you want."
    "She left the kitchen, leaving us alone."
    me "Tell me, did you have to peel potatoes in the past?"
    stop ambience
    show us dontlike sport with dspr
    us "Are you seriuos? I am fourteen already!"
    me "I don't see any connection here. I'm asking about potatoes, not vodka or cigarettes..."
    "I thought about how to put it more clearly."
    me "So you had to peel potatoes?"
    us "Of course! What did I just tell you?!"
    me "And how about for a hundred people at once?"
    us "No, not for hundred. But the only difference is that there is just more of it right?"
    me "Not exactly. Firstly, we work with already processed tuber, and secondly, there is really much more of it."
    me "So you better drop that cleaver that you're trying to take, and pay attention to a more modest knife."
    "I took a small knife from the table, checked its sharpness and handed it to my partner:"
    me "Less movements, faster process. Let's get started?"
    "Ulyana nodded and grabber the first potato."
    "And I filled a nearby tank by a third and put it in the middle, deciding to stand until they brought me something where I could nestle."
    "It seemed to me that the scope of work is not too extensive, in any case, it's not five full tanks, as in the years of my youth."
    th "Yeah... Well also, there is just the two of us instead of four..."
    "Soon the cook came, and put yet another cauldron under the belly of the machine, thereby doubling the volume of what must be done."
    "By the way, she brought me some kind of dirty wooden box - either from under oranges, or from under tarragon. In short, it was acceptable."
    scene cg d3_potato_1_7dl with dissolve
    "I cursed soundlessly and, sitting on the box, plunged into the monotonous, brain-cleansing process of gouging out the eyes which the rough surface of the centrifuge had not reached."
    "Ulyanka sniffled, giving me a sidelong glance, but it seems she realized that I was not able to entertain her."
    "And quieted down."
    with fade
    "Not for long though, for half an hour roughly."
    play music music_list["went_fishing_caught_a_girl"] fadein 5
    us "Hey! Don't you sleep there!"
    "She threw a small potato at me and hit right in the forehead."
    "I stared at her in surprise."
    me "What are you doing, you, little..."
    us "I'm bored!"
    "Certainly she declared."
    us "Let's go crazy!"
    menu:
        "Certainly, no.":
            if counter_sl_cl >= 1:
                me "Go, but without me."
            else:
                me "We already got crazy yesterday, you see where we ended up?"
            us "You turned on the old fart mode again."
            "She pouted and looked at me with displeasure."
            $ karma += 10
        "Go crazy!":
            me "Any suggestions then?"
            $ lp_us += 1
            us "Noooo! I gave you the idea, rest is on you!"
            $ karma -= 5
    us "Actually! Acting like a slipper-bore."
    me "Me? A slipper-bore?"
    "I didn't believe my own ears."
    us "You! You're whining about being punished again and that you are so miserable."
    us "By the way, I'm here with you! {w}Didn't ran away! {w}Appreciate it!"
    "She picked up a freshly cut peel from the floor and threw it at me. Well, at least not a potato, like last time, thanks for that."
    "To appreciate that I did not throw a potato - a marginal note."
    me "What to appreciate?"
    "I peeled off the peel from my cheek."
    me "The fact that you're throwing all sorts of dirt at me?"
    "I didn't finish — another 'eye' was flying at me.{w} More after it."
    "Ulyanka did not let me do anything, suddenly turning into a machine-gun battery, destroying the enemy."
    "So is it any wonder that after the fifth hit in the face, the neighboring nation opened a counter-fire?"
    "I roared, scooped up a whole pile of potato remains from the floor and shot them at the redhead."
    "She laughed enthusiastically and, flying off the chair, raised it so that it turned out to be a good cover spot, from where she continued to water me with an incessant stream of potato skin, gouged out eyes and the devil knows what else."
    "I had to hide behind a box, and there, of course, the cover area was much smaller, so in the end I was fired all over."
    play sound sfx_open_door_2
    voice "And what are you do..."
    play sound sfx_bus_window_hit
    "Voice from behind did not finish."
    scene cg d3_potato_2_7dl with dissolve
    "I left the line of fire at the wrong time, so the last volley went ... Yes, to the cook, who else."
    "At the wrong time, she decided to go and check on us."
    voice "Well, Ulyanka..."
    "Woman strained, wiping herself with an apron."
    "But for some reason she didn't swear. {w} Apparently, she already knew that it was useless."
    voice "Bandits! Finish up and get out of here."
    play sound sfx_close_door_campus_1
    "The door slammed behind her."
    us "Shall we continue?"
    "Recklessly offered Ulyana as soon as the door closed."
    me "No. Let's finish already."
    "The little one was about to pout again, but I was faster."
    me "There's not much left, look."
    "She looked into the remaining cauldron. Indeed, there was no more than a quarter left... Which we persuaded in less than fifteen minutes."
    scene bg int_dining_hall_day with fade
    show us laugh sport
    us "Finally!"
    "She put the knife aside and dusted off her hands, the skin already wrinkled from the dampness.."
    me "Yes. We made it."
    us "It was a tough fight."
    me "Calm down, you will be rewarded for it. Do you want to raise the flag on the lineup tomorrow?"
    show us normal sport
    us "Feh, it would be better if they gave me candies!"
    me "By the way, about…"
    us "No, I already checked. {w=.3}Empty. {w}They hid it!"
    me "Let's go at least report on the work done."
    "We found the cook in the kitchen, where she consumed coffee with some, judging by the smell, freshly baked buns."
    "To our «We finished!» she gestured to join the tea party, but for us it was already enough water for today."
    voice "How picky..."
    "Cook bustled."
    voice "They don't want tea, and it's not good to let them go empty handed."
    "She thought for a moment. Then suddenly she sparkled."
    voice "Yes! We just had a few ice creams left from the last session."
    voice "Do you guys like ice cream?"
    show us surp2 sport
    "She blurted out in response to the enthusiasm with which we nodded and, rattling the keys, went to the refrigerator, from where she gave Ulyana and me a glass of ice cream."
    show us surp3 sport with dissolve
    voice "You sure you don't want a cup of tea? At least you get warmed up."
    us "No thank, cook-ma'am"
    "Ulyana said politely."
    us "Just let us go..."
    "The cook burst out laughing and pointed at the door."
    voice "Go ahead. Just don't come so early to set dinner. Fifteen minutes is enough."
    "We looked at each other and, nodding, went out into the hot morning, eating each of our ice creams at the same time."
    pause(0.5)
    play sound sfx_open_door_clubs fadein 0
    scene bg ext_dining_hall_near_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    show us smile sport with dissolve
    us "And I have chocolate!"
    "Ulyana boasted."
    me "Everyone has chocolate!"
    "I laughed."
    me "They both are out of the same box."
    us "Well, what if! And anyway, I have the most chocolate!"
    me "Okay, you have the most chocolate."
    "The girl's unspent energy welled up from her, and I hurried to increase the distance separating us."
    if 'music' in list_clubs_7dl:
        me "Okay, I'll depart, Miku is still waiting for me."
        if alt_day2_date == 'un_fz':
            "I was sure that to load the little one with my personal troubles is a deliberately ungrateful undertaking."
        elif alt_day3_date != 'mi':
            "For some reason, I did not want to talk about who and for what reason was actually waiting for me."
    else:
        me "I'll go, I need to do something else at a cabin, the squad leader asked."
    me "Let's meet here at fifteen minutes before two, okay?"
    us "Yes!"
    "She turned around and ran. Judging by the direction - again to play football."
    me "Don't forget!"
    "I yelled at her back."
    hide us with dissolve
    us "Thanks, mom!"
    "She yelled back without turning."
    "I smiled at her last words and moved towards the square."
    if alt_day3_date == 'un':
        if 'music' in list_clubs_7dl:
            "Was Miku waiting for me or not is another deal, for now I have a more important target."
        else:
            "Squad leader would be surprised to know that she asked me of something."
        "I smiled and sharpened my skis towards the library."
    elif alt_day3_date == 'sl':
        if 'music' in list_clubs_7dl:
            "Miku, of course, is a pretty girl. But now I have a much larger forms of work waiting for me."
        else:
            "Housework, of course, is a useful thing, but I prefer other kind of work - pretty one, with golden hair."
        "I grinned and turned in the direction of Genda, since all paths lead to him."
    elif alt_day3_date == 'dv':
        if 'music' in list_clubs_7dl:
            "If Alisa heard me say that Miku was waiting for me..."
            "I shrugged my shoulders and forbade myself from counting the number of potential corpses."
        else:
            "Squad leader, huh? Universal excuse."
    elif alt_day3_date == 'mi':
        "The funniest part is that Miku was actually waiting for me. Except for a slightly different purposes."
        "So it's decided. The goal is a music club!"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_event_music_club1:
    scene bg ext_musclub_day with fade
    play ambience ambience_camp_center_day fadein 1
    play music music_7dl["tellyourworld"] fadein 4
    if alt_day3_date == 'mi':
        call alt_day3_morning_mi
    elif alt_day3_mi_invited:
        "I went to the door of the club and was about to knock, but at the last moment I stopped."
        "I hardly know Miku. Now she will sing for me, and I will be embarrassed all this time."
        "I'd better get out of here before anyone sees me."
    else:
        "The music club has been closed, and closed badly."
        "Perhaps there was someone inside, but the handle did not turn, and no one was in a hurry to open it for me."
        "I stood for a while, trying to hear something. {w}Then, not wanting to disturb, I left."
        "For some reason, I did not dare to knock."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_morning_mi:
    scene bg ext_musclub_day with dspr
    "Although in my ordinary life I could easily spit both on promises and on the most honest promise - justifying myself by giving it on the spur of the moment, but in this camp, incomprehensible and frankly disturbing changes began to occur in me."
    "This applies to just this promise. I suddenly started to care if I kept my promise, or if I forgot, if I stuff my head with something else, or just ignore it. I suddenly started to give a damn about the opinions of others."
    "Well, not everyone, of course ... Olga, Lena, Alisa, Ulyana, Slavya ... And also Miku."
    "Therefore, as soon as I had a free minute, I hurried to where I promised to go - to the music club."
    "I promised Miku. I don't care that I have no idea what I'll do there. The promise must be kept."
    dreamgirl "Especially the promises made to such a girl. Have you seen her pastorals? Ah-oh, where are my seventeen years!"
    th "Damn pervert. Where did you even got that word from... Pastorals."
    "I grunted and headed down the path towards the already familiar «flying building»."
    "And if when I turned here from the square, I was determined to at least see this girl and say «hello» to her, then with each new step my determination melted, until it dried up completely somewhere half a step before the cherished door."
    "Thoughts again swept in a panic."
    "What am I going to tell her? What am I going to do? Or what are WE going to do? Damn it. What if she gets something wrong, like it always happens with me?"
    dreamgirl "Stop suffering, monster. You'll have time to cry some more when she kicks you out. IF she kicks you out."
    "Some kind of music was coming from the house, and, distracted by it, I suddenly felt a kind of light-light push in the back. Nothing serious, but he made me take the missing step."
    "Trying to keep my balance, I put my hands out in front of me and somehow - it came out by itself - I leaned against the door. It turned out to be unlocked."
    stop ambience fadeout 2
    play sound sfx_open_door_2
    pause(1)
    scene bg int_musclub_day with dissolve
    $ persistent.sprite_time = "day"
    play ambience ambience_music_club_day fadein 3
    "There really was music playing in the club!"
    "Scattering the instruments around the perimeter of the hall, Miku was spinning in some kind of dance unknown to me, managing to sing at the same time!"
    "She threw off her shoes, leaving her in stockings ... I suddenly realized that these were not knee-high socks, but real stockings! A fetish for any healthy men. Where did she manage to get them in the USSR?!"
    "Not otherwise, the heritage of her historical homeland."
    "She seems to have noticed me at the corner of her eye, as she nodded at me and went back to her dancing."
    "I'm not very strong in languages ​​- in fact, only with English I managed to get to the conversational level - but it was definitely Japanese. You can’t confuse the structure with anything."
    "A Japanese girl, sitting alone in a music club, sings songs of her homeland."
    "Is it any wonder that she rejoices in every new face!"
    "Finally, the music died down, and she, going to the tape recorder, took away the plastic case of the tape cassette. Judging by the fact that the plastic was transparent, the cassette turned out to be Japanese."
    "I would be embarrassed to feed OUR equipment with such a tape. It reacts to everything Japanese only from a gastronomic point of view."
    show mi smile pioneer with dissolve
    mi "Hi, Semyon! Glad you stopped by."
    me "You dance great! Do you have your own choreography?"
    show mi shy pioneer with dspr
    mi "Uuh, what are you saying. They put a separate for each performance I have."
    me "And how many performances do you have?"
    "She shrugged."
    mi "Normal concert program, 100 minutes."
    me "And you don't get bored?"
    show mi happy pioneer with dspr
    mi "Are you kidding! Such things cannot get boring."
    "She glared at me."
    show mi serious pioneer with dspr
    mi "If you're talking about stars, you should probably understand that status puts up even bigger walls than anything else. {w}You communicating with a person you don't know who he is listening to, you or the stage person he is in love with."
    if alt_day2_mi_date != 3:
        mi "However, we already talked about this yesterday, I mean I talked about it, but I think you understand what I mean."
        me "We talked yes... {w}Anyway, would you like to give me an autograph?"
        show mi happy pioneer with dspr
        mi "Here you are teasing me now, but no one has teased me for a long, long time, as if I were a robot or something like that."
    me "I don’t know how to behave with the stars, so I speak to you as to the girl first of all."
    show mi smile pioneer with dspr
    "I winked and was rewarded with a quick smile."
    mi "You're very cute, I hope this doesn't change in the future..."
    me "Okay. But you owe me a song!"
    mi "I just sang one."
    me "Compared to a hundred minutes, one song is like nothing at all. {w}Sing something you love, maybe not even from your own program."
    "She thought for a moment and nodded."
    mi "Yes, there is one song that I've always wanted to sing on a stage... It's a pity that the rights to it belong to not the best people."
    "A little hesitant, she took out another plastic case, which showed a very similar girl with azure hair styled in two incredibly long tails that defy gravity and provocatively stick out in different directions."
    "Apparently, the nature of the Soviet audio equipment was known to her firsthand, as she once again looked inquiringly at me."
    "I smiled encouragingly."
    me "Light it up!"
    stop music fadeout 6
    "Realizing that it was not so easy to get rid of me, she sighed and took the tape recorder by the handle."
    show mi normal pioneer with dspr
    mi "There's not enough space here, let's go to the veranda."
    scene bg ext_musclub_day with fade
    "We stretched the extension cord, she put the tape recorder on a bench and, throwing off her shoes, stood in front of me, on the wooden floor, remaining only in her stockings."
    play music music_7dl["outer"] fadein 3
    "The first chords of some semi-familiar song began to play..."
    "It was obvious that it was pop, almost from the first bar, but that it would be Japanese pop was a surprise to me."
    "Miku seemed to relax and stopped looking for words, grabbing air in the wrong places, and even those moments where fast pronunciation was required were made to her somehow very relaxed... "
    "Apparently, Japanese was still her first language."
    "All the dashes, the moments where it was necessary to sing the words quickly, she performed flawlessly, without losing either breath or pace."
    "I didn’t notice at what point the music carried me away so that I began to automatically beat out a rather complex rhythm with my foot and shake my head to the beat, while Miku herself, it would seem, had already forgotten about where and what she was!"
    "She flew over the stage like a feather, half-closing her eyes and devoting herself entirely to the music she performed, and I, albeit belatedly, but pricked with a sharp needle of jealousy - in the heart of this person, music will always come first."
    "But let it be. I'll be satisfied with such a plot. I smiled and watched the polished pas, developing into a kind of constantly moving dance pattern. You can see that they staged it with love and attention to details."
    "Finally, the last riffs were played, the last snare fell silent, and I, without restraining my delight, jumped up, clapping my hands."
    stop music fadeout 14
    me "It's unbelievable! I can listen to that all day!"
    mi "You liked it?"
    "She did not hide the pleasure of praise, despite the professional level of the performance and the behavior on stage, which shows how hard it is to get the tickets to her concerts. But she surely knew how to light it!"
    me "Very much."
    "She seemed to exhale, from a fluffy girl who had just flown over an impromptu stage, she again turned into an ordinary lively girl of exotic appearance."
    mi "That's it, I perform here... Sometimes."
    "I helped her wind up the wires and bring in the equipment. Except for a shadow that I caught out of the corner of my eye, and which disappeared as soon as I turned in that direction, nothing witnessed the incredible concert."
    stop ambience fadeout 2
    play sound sfx_open_door_2
    pause(1)
    scene bg int_musclub_day
    with dissolve
    play ambience ambience_music_club_day fadein 3
    "Door closed behind us, we are alone now."
    show mi smile pioneer at left with dspr
    me "So, what's next?"
    if herc:
        "I asked exaggeratedly."
        mi "You've said you can play guitar. Will you show me?"
        "After some hesitation, I agreed to take the guitar, and my fingers fell on the chords of the only song that I knew."
        "I stretched my fingers and got ready to play - at that moment the front door slammed. {w}A new character appeared in the club - Alisa."
        show dv normal pioneer2 at right with dissolve
        play music music_7dl["lyrics"] fadein 3
        "It's too late to be embarrassed now, I already took the first chord."
        "She was about to say something, but froze in the doorway, throwing incredulous glances at the instrument in my hands."
        "I spoke more than sang, casting glances at Alisa:"
        me "A cigarette flashes in the darkness... {w}The wind threw ashes in my face..."
        "I delayed the last quarter, but for some reason I did not wait for a response."
        me "Dvachevskaya!"
        show dv shy pioneer2 at right with dspr
        dv "I won't!"
        show dv shy_smile pioneer2 at right with dspr
        "She laughed embarrassedly."
        dv "I don't even know the lyrics!"
        me "Well, of course, Dvachevskaya and doesn't know SUCH a song."
        me "Tell your stories to someone else!"
        "I picked up a few more chords and went on:"
        me "And the charred filter on my fingers left a bu-u-u-u-urt."
        show dv smile pioneer2 with dspr
        "She waved her hand, laughed and, with a twinkle in her eyes, continued:"
        dv "The door opened with a creak of steel... You're coming, you're mine now."
        "And we continued in unison:"
        me "I feel a pleasant shiver from head to tooooe!"
        show mi grin pioneer at left with dspr
        "Miku who joined was a surprise, but more louder lyrical-hooligan song gets the more pleasure you'd get:"
        me "Forget about everything with me! This night will seem like a dream to us! I'll take you and hug you like my own daughte-e-e-e-e-er"
        "And there was something in it, as if in the miracle of the camp where I was lucky enough to appear, another miracle decided to look at the light - a piece of childhood, running on sandstone and coniferous needles and air, tasty as cold water, and life that smiles affectionately holding you in its arms."
        "And it was somehow understood that there would never be another day like this, or an impromptu concert, and even more so - this will never happen again with me. And it became terribly envious of the one who will be lucky enough to tame Dvachevskaya."
        "And in his honor there will be fire in the eyes from under the bangs, and all the elemental passion that finds an outlet only in boyish tricks."
        "Fortunately, my fate is no worse. Except that its elemental power is spent all in chattering songs, and for me personally it leaves solid albeit a bit too verbose conversations."
        stop music fadeout 2
        "I slapped the strings."
        me "Good times... I had no doubt that you, Alisa, well known of «Sector's» performances, but you, Miku?!"
        show mi laugh pioneer at left with dspr
        mi "What's wrong with it? A good song, a bit sad though."
        dv "Yeah, the song's not bad. And I'm here for... for..."
        "She thought, apparently, I somewhat discouraged her with my «Welcome»."
        dv "Here! I went for the guitar. Did you finish it?"
        mi "Yes, give me a sec.."
        "The girl went to the far wall, half of which was blocked by the piano, and started rattling with something."
        hide mi with dissolve
        show dv grin pioneer2 at center with move
    else:
        "As far as I remember she promised me something."
        show mi shy pioneer with dspr
        mi "Sen... Listen."
        "She was embarrassed and looked away from me."
        "This is usually the behavior of people who somehow let down a loved one - and, moreover, have not yet lost the remnants of conscience."
        me "What? {w}Didn't manage to get it?"
        mi "Managed, but..."
        "She reached into her pocket and, after a bit of digging, revealed to the world represented by me..."
        show mi normal pioneer with dspr
        "She must be kidding."
        "Or not."
        "She was holding a white plastic mouthpiece in her hands."
        me "And there is nothing better?"
        "I took the plastic in my hands for the purpose of studying."
        me "Although this is not the worst I've seen."
        show mi shy pioneer with dspr
        me "Even despite the fact that some dog gnawed it, can still be somehow usable."
        me "But, damn it, what are you going to do about the fact that the trombone and your trifle do not have the same diameter?!"
        mi "So you won't play?"
        me "I can't, rather."
        me "What you brought is from a pioneer horn, you know, one that can only play C and G?"
        me "In the trombone, it dangles like... well, I just can't."
        mi "Well woooo…"
        show mi upset pioneer with dspr
        "The girl thought for a moment and then sparkled:"
        mi "And I saw a horn in Alexei Maksimovich's office! Although, he is a little rumpled."
        "She unconsciously glanced at the trombone."
        mi "Do you want me to bring it? Will you play?"
        show mi grin pioneer with dspr
        "Turning around on one leg, Miku pretended to be ready to «run and carry»."
        me "And what shall I play for you? Pioneer dawn? {w}Without valves I won't be able to squeeze out anything more serious than signals."
        "Miku frowned, but stubbornly shook her head."
        mi "At least that! I want to listen, and then what if you will become a bugler!"
        "Holy, holy! As if I have nothing other to do, how to get up before everyone else and become the object of collective pioneer hostility."
        dreamgirl "It's a possibility to take revenge on especially gifted comrades. Dvachevskaya, for example, huh?"
        dreamgirl "Just imagine, you come out so fresh, cheerful! You stand right under her windows and - fortissimo! - you start «wake up, wake up! Whoever is sleepin, we'll beat'em!»"
        dreamgirl "Imagine how great it will be!"
        th "Yeah, before a random shoe hits my head."
        "Cynically, I did not react to the provocation."
        show mi laugh pioneer at left
        mi "Senechka, you slept off your face! Are you really that afraid of the audience?"
        me "I'm not afraid of the audience, I'm afraid of tomatoes that audience can throw."
        "Miku dismissively dismissed my objections:"
        mi "Sit here, I'll be right back!"
        me "Eh..."
        mi "Don't you dare go anywhere!"
        "She instantly vanished."
        hide mi with flash
        pause(1)
        play sound sfx_close_door_1
        "Door slammed and I remained alone."
        "But, unfortunately not for long."
        play sound sfx_open_dooor_campus_1
        show dv grin pioneer2 with dissolve
        dv "Where did she run off to?"
        me "Straight forward."
        "I answered. Didn't want to speak."
        "Silence reigned in the room for a couple of minutes."
    dv "Hey, hey!"
    "Alisa lowered her voice."
    dv "So you're Miku's new boyfriend? Everyone's talking about the beach."
    me "If everyone says so, then you should too, be as everyone."
    "I was somewhat embarrassed by her shamelessness, but I decided to play the same game."
    me "Are you interested in the details? How, in what positions and how many times? Or will you remember that it's impolite to climb into someone else's life, especially if you are not invited?"
    show dv shy pioneer2
    dv "Hey, what's wrong! I was just asking."
    "It seems I had especially menacing look, as she took a step back and pouted."
    dv "You should understand, things like this don't happen often in our camp. Everyone is interested."
    me "It's a shame you don't have «MTV» here, damn voyeurs."
    dv "What?"
    "It seems that Alisa did not understand anything, but Miku saved me from further questions."
    show dv sad pioneer2 at cright with moveinright
    show mi smile pioneer at cleft with moveinleft
    if herc:
        "Finally she stepped out into the world with an electric guitar in her hand."
        mi "Here, take it. The strings are new, you can adjust them for yourself."
        dv "Thank you!"
        "Alisa grabbed a guitar, waved her hand and ran away."
    else:
        "She burst into the room, clutching to her chest not a horn, but rather a bugle."
        mi "Here! Will you try it?"
        "I looked at the acquisition skeptically, but didn't argue."
        "I stuck the mouthpiece into the pipe, put it to my lips, took a lot of air into my chest, and ..."
        with flash_red
        "The resulting sound was neither euphonious nor in the least proper."
        me "Haven't played in a while."
        "I explained."
        me "Now one more time."
        dv "Oh, you know, I guess I'll go... I've got things to do."
        "Without giving us a chance to put in a word, Dvachevskaya vanished."
    hide dv
    show mi normal pioneer at center
    with dissolve
    mi "What were you whispering about?"
    me "Looks like you and I are both now... stars of sorts."
    mi "Are you talking about the beach? Well... People are curious."
    me "They shouldn't care."
    mi "We're in a pioneer camp... Everyone has something to do here. There is no other entertainment."
    "She got upset."
    show mi angry pioneer
    mi "Thats why I always sit here, and where my yesterday's thoughts come from... That's all because of things like this."
    me "Don't be afraid."
    "I put my hand on her shoulder."
    me "Now there are two of us. And it's always more fun together."
    return

label alt_day3_event_clubs1:
    scene bg ext_clubs_day with fade
    play ambience ambience_camp_center_day fadein 1
    "The club was closed. Weird."
    if 'cyber' in list_clubs_7dl:
        "And why, one wonders, I signed up for this?!"
    else:
        "And that means only one thing - most likely, they haven't come here at all yet."
    "If my memory serves me, both cyberneticians can be found in the editorial office of the newspaper."
    "Whether I need it - is an entirely different question."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_event_camp_entrance1:
    scene bg ext_camp_entrance_day with fade
    play ambience ambience_camp_center_day fadein 1
    "My path to this camp began with the gate. So taking them as a starting point is not a bad idea."
    "I stood in front of the gate, remembering..."
    if (counter_sl_7dl == 0) and (alt_day_binder == 0):
        "Ulyanka and her locusts!"
    if alt_day2_date == 'sl':
        "Slavya and our magical encounter in the forest."
    if counter_sl_7dl < 2:
        "At least the way she took me by the hand from here on the first day and fed!"
    "In my world, no one would care."
    "Thank God I'm not in my world."
    stop ambience fadeout 3
    with fade
    return

label alt_day3_morning_un_fz:
    scene bg ext_boathouse_day with dissolve
    play ambience ambience_boat_station_day fadein 3
    play music music_7dl["carefree"] fadein 3
    "When I went out to the pier, Ulyana was already sitting on the gangway, dangling her legs in the water."
    "The glare from the water surface was blinding, and I almost stumbled over the thickets near the shore."
    show us dontlike sport with dissolve
    "The girl turned around hearing my quiet swearing."
    us "You slowpoke! I thought I was going to die from sunstroke while waiting for you!"
    me "Sorry, someone had to clean up after you.{w} And anyway, not everyone was born with a motor in their..."
    show us upset sport with dspr
    us "Blah, blah, blah, whining again, what are you, seventy years old?"
    show us normal sport close with dspr
    "I sat down next to Ulyana and put my feet in the water."
    "I don't know if it was a very strong current, but the water turned out to be much colder than expected."
    me "So what are we going to steal?"
    us "And what makes you think that you need to steal?"
    me "Me? Aren't you on the raid WITH me, honey?"
    show us grin sport close with dspr
    us "Don't you dare! Of course I am, and moreover, my role is the most responsible."
    "Ulyana looked around and whispered conspiratorially:"
    show us smile sport close up with dspr
    us "Long story short, I need a knife. Mine broke yesterday."
    us "I'll distract the boatman, and you'll steal his knife!"
    "I whistled."
    "I certainly did not expect such a turn."
    me "Won't you reveal the secret, why the hell do you need it?"
    us "This is the tenth matter."
    show us grin sport close up with dspr
    us "Look, I already studied everything: he has a toolbox under the table, on which there is some kind of logbook."
    us "The knife must be there!"
    "She was thoroughly prepared for the case."
    me "Okay, my task is clear. How do you plan to distract the boatman?"
    us "Easy!"
    hide us with dissolve
    "I didn't have time to open my mouth, as she began to pull off her T-shirt."
    "From surprise, I froze in a stupor, but my inner voice seemed to be in ecstasy."
    dreamgirl "Maybe, well, damn that knife? We can join the entertainment too!"
    "But there was no entertainment."
    show us normal swim with dissolve
    "Ulyana had a swimsuit under her clothes."
    us "I'll steal a boat, and when the boatman rushes after me, I'll jump into the water and swim away."
    us "You should have enough time to find the knife and get out of there."
    us "Is the plan clear?"
    me "Sir, yes, sir."
    show us laugh swim with dspr
    "Ulyana laughed happily."
    show us normal swim at fleft with move
    "She jumped onto the walkway and rushed barefoot to the bushes, holding her clothes crumpled in her hands."
    show us smile swim at center with move
    "After hiding her clothes in the bushes, she returned to me."
    stop music fadeout 4
    us "Hide around that corner of the cabin for now."
    us "Just don't flash in front of the windows!"
    scene bg ext_boathous_day2_7dl with fade2
    play music music_7dl["sneakupon"] fadein 3
    "We've taken our starting positions."
    "I stood around the corner of a wooden house, crouching, while Ulyana, meanwhile, was untying the boat."
    "Judging by the movements of her lips, the task was not an easy one: I read at least three unprintable expressions from them."
    "At last she overcame the knot and pushed the boat away from the dock."
    "Awkwardly jumped into it, causing the ship to sway quite a bit."
    th "I hope she won't fall off of it sooner than needed..."
    "After pulling the oar from the bottom, the girl began rowing it clumsily."
    "I covered my eyes with a loud pop in order to not witness this circus."
    th "Yeah, she won't get far with only one oar intact."
    dreamgirl "I dare say both oars will weigh more than she does. I don't think she's a master of sports in rowing, dummy!"
    "The boat was only a few meters away from the pier when the slap of the oar on the water caught the attention of the boatman."
    "He rushed out of the cabin, shaking his fist."
    $ meet('voice','Boatman')
    voice "Hey, turn back! Hooligan!"
    "As soon as she heard him, Ulyana dived under the water like a fish."
    "The boat rocked dangerously again, threatening to capsize."
    "I realized it was time to act."
    "I didn't had much time: for a boatman to catch and tie up the knot was a trifling matter - the rope from the boat was still lying on the walkways."
    scene black with fade
    stop ambience fadeout 4
    "I slipped into the cabin and looked around."
    "The table, on which the logbook for those who took the boat lay, was found in the corner of a small room. The toolbox was indeed under it."
    "I rummaged through the drawer nervously, but I couldn't find the damned knife."
    "And anyway, how did Ulyana have such an unshakable confidence that it was there?"
    "I got up and looked out the window."
    "The boat was already in place, and the man was just finishing tying a knot."
    "I just hoped he would take more time to tighten it up."
    "Suddenly my eyes fell on the open drawer of the desk."
    "Without much hope, I looked inside."
    "Bingo!{w} Inside was a knife and a skein of twine."
    "I grabbed the goods and rushed to the exit, but heavy steps were heard outside the door."
    th "Damn it, I'm stuck! I don't even have time to open the window!"
    "The exit was found in the corner of the gatehouse: a wooden staircase leading to the attic."
    "Taking a knife in my teeth, I confidently climbed up."
    scene bg int_attic_7dl with dissolve
    "I didn't have any ideas about what to do next, but I absolutely didn't want to be catched by the boatman."
    "Further, come what may - he will come out eventually!"
    th "That's it, Ulyana, better start running! You owe  me a weekly supply of cutlets for this!"
    "Judging by sounds downstairs, the boatman turned on the TV."
    th "Yeah, he's obviously not going to leave the cabin until lunchtime. Have to be patient."
    "I looked around in search of a place where I could fall, and inadvertently I touched the fishing rods standing by the hatch with my elbow."
    play sound sfx_7dl["crash_wood"]
    stop music fadeout 1
    pause(2)
    "Never thought it would be that loud."
    "Heart.exe has stopped working."
    play music music_7dl["anglegrinder"] fadein 3
    voice "What's that sound? Hey, you, bandits! Get out of there!"
    $ meet('voice','Voice')
    "The stairs creaked heavily, and I darted around the attic like an animal in a cage."
    "There was only one way out: a small window on the roof."
    "Cussing Ulyana and her grand schemes with all the words that I only knew, I fought furiously with the window in the process."
    "I had to put the knife in my pocket - not safe, but what else could I do?"
    play ambience ambience_boat_station_day fadein 3
    scene bg ext_boathouse_day with flash:
        xcenter 0.5
        ycenter 0.5
        zoom 1.9
    "I got out exactly at the moment when the boatman's angry face appeared from the hatch."
    "Hissing in pain, I crawled along the roof, burning myself with the hot metal."
    "There were two options for retreat: either jump into the water (which I categorically did not want), or bypass the roof around the perimeter and dive onto the walkaway from the entrance."
    "Estimating how fast the boatman would get there, I actively worked with my limbs."
    th "Probably, I look like a cockroach right now. What a show for Ulyana, sitting in the bushes!"
    "After reaching the opposite side of the roof, I swiftly jumped onto the catwalks before I could even properly group myself.{w} A fatal mistake."
    play sound sfx_body_bump
    scene bg ext_boathous_day2_7dl with vpunch
    "My legs buckled, and I rolled head over heels on the heated wooden planks."
    with flash_red
    "Right thigh suddenly burned with sharp pain."
    me "Oooh, damn it! There's a knife in there!"
    "There was no time to inspect the damage, and I rushed from the pier with all my might."
    scene bg ext_boathouse_day
    show us normal sport
    with dissolve
    "Already dressed Ulyana joined me on the footpath."
    us "Did you get it?"
    me "Cut it, private! Run!"
    stop ambience fadeout 3
    scene bg ext_boathouse_day with flash
    show ftl_anim with Shake((0, 0, 0, 0), 4.0, dist=10)
    scene bg ext_square_day with flash
    show ftl_anim with Shake((0, 0, 0, 0), 4.0, dist=10)
    stop music fadeout 5
    scene bg ext_aidpost_day with flash
    play ambience ambience_camp_center_day fadein 2
    pause(2)
    "We just stopped at the infirmary."
    "Lungs was as if they completely dried up, and every breath brought pain."
    show us sad sport with dspr
    "Ulyana felt much better."
    th "It's okay, when the old age creeps up - you'll be dying even harder! "
    "I though malevolently."
    show us smile sport with dspr
    us "So?"
    "She circled impatiently around me, causing a burning desire to strangle her."
    "She doesn't know, damn it, what I had to go through!"
    "I put my hand in my pocket and hissed: my fingers touched something sharp."
    "What I pulled out of my pocket turned out to be bloodied pieces of a knife."
    show us surp2 sport with dspr
    "Ulyana gasped with disappointment."
    "I carefully laid the wreckage on the ground and looked at the injured leg."
    "There was a crimson stain on the shorts."
    show us sad sport with dspr
    "Cursing through my teeth, I pulled up my pant-leg: the cut was not deep, but it bled notably."
    "You should have at least treated it with peroxide."
    us "Come to me, I have some green!"
    me "Ulyana, we're standing next to the infirmary. Why not just go to Viola?"
    show us shy sport with dspr
    "Ulyana hesitated."
    us "Well... she'll ask where did you get that and..."
    me "Yes, I won't betray you, don't worry. Get out of here so that there are no unnecessary questions."
    show us dontlike sport with dspr
    "But she suddenly stood up."
    us "No, no! You're crippled because of me, which means I'm responsible for you now!"
    us "Let's go! I'll explain to Viola what happened."
    "That statement scared me more than any scratch."
    hide us with dissolve
    play sound sfx_open_door_1
    "Ulyana opened wide the door of the infirmary."
    us "Violetta Cernovna, we're..."
    "She faltered, and I, looking inside, immediately understood the reason."
    scene bg int_aidpost_day
    show un surprise pioneer far at right
    show us surp2 sport
    with dissolve
    play ambience ambience_medstation_inside_day fadein 2
    play sound sfx_close_door_1
    play music music_list["what_do_you_think_of_me"] fadein 2
    "There was Lena sitting at a table instead of Viola."
    "Our presence took her by surprise.."
    show us normal sport with dspr
    un "Viola will be away for a couple of hours, and I'm standing in for her. What do you have…"
    "She noticed a stain on my thigh and a blood-stained arm."
    show un shocked pioneer far with dspr
    "It was hard to tell if she was pale or green, but she clearly did not like the sight."
    show un serious pioneer far with dspr
    un "Take off your shorts."
    dreamgirl "Like this right away? Maybe we can at least send the small one out first?"
    un "And you, Ulyana, bring new shorts from the warehouse. These need to be washed."
    dreamgirl "See, she understands me even without words. And you're stupid even with direct instructions!"
    play sound sfx_open_door_1
    hide us with dissolve
    play sound sfx_close_door_1
    "Ulyana disappeared behind the door, leaving me alone with Lena."
    "I had no choice but to obey Lena's orders and undress."
    hide un with dissolve
    "Lena turned away and began to look for something in the drawers."
    "I sat down on the couch and began to watch the girl with curiosity."
    "Obviously, it was not the first time for her to fill in for Viola."
    un "How long ago did you hurt?"
    "Lena's voice sounded calm and indifferent."
    show un sad pioneer with dissolve
    "But when she turned to me, her face was filled with ill-concealed anxiety."
    me "Fifteen minutes ago. Fell on something sharp."
    show un serious pioneer with dspr
    "Lena frowned."
    un "You don't need to lie to me. The shorts are intact on the outside."
    "She squatted down next to me and soaked a piece of cotton in hydrogen peroxide."
    me "Let's put it this way: I signed up for a very dubious venture, and now I'm reaping the rewards of my actions."
    "The liquid hissed at the wound."
    "I gritted my teeth to keep myself from hissing too."
    dreamgirl "Do you want to look like a hero in the eyes of that girl? Well, well."
    th "I just don't want to scare her. She's afraid of blood. Or hurting someone."
    un "It looks like a knife cut. Are you seriously running around with a knife in your pocket?"
    th "For a regular girl you know too much about cuts..."
    me "Don't tell anyone about this, please. We got this knife with not very legally ways."
    show un surprise pioneer with dspr
    "Lena looked at me in surprise and picked up a tube of some kind of ointment."
    un "And why?"
    menu:
        "Ulyana asked...":
            $ counter_un_fz_un_route += 1
            $ lp_un += 1
            me "I think she wanted to do another dirty trick."
            show un smile pioneer with dspr
            un "And you volunteered to help?"
            "Lena smiled unexpectedly."
            "Given how neutral she was trying to keep up until then, this action surprised me a bit."
            me "Well, you know, whatever a child would enjoy..."
            un "And there was nothing else for you to do?"
            if (alt_day2_convoy == 'sl'):
                th "If you want to ask why I don't spend time with Slavya, don't be shy!"
            elif (alt_day2_convoy == 'dv'):
                th "If you want to ask why I don't spend time with Alisa, don't be shy!"
            th "I'd be right happy to disprove your theories that I'm a a ladies' man."
            "But I didn't say that out loud, of course."
            me "Well, yes."
            me "Everyone has their own business, but I didn't want to crowd into someone's company. And at least it brought benefits to the child."
            th "At least I tried. Although the knife is broken!"
            show un shy pioneer with dspr
            "Lena was embarrassed and did not answer, continuing to treat my wound with ointment."
        "This is a secret":
            $ counter_un_fz_old_road += 1
            me "Very forbidden secret."
            "Lena looked at me in surprise."
            me "But one day I will definitely initiate you into it!"
            th "When I myself find out what this secret is. Ulyanka never told me!"
            show un smile pioneer with dspr
            un "Two idiots you are."
            "She muttered it so quietly that I could barely catch her words."
            "But it was hard to disagree: if anyone had told me a week ago what I would do here, I would have laughed in his face."
    play sound sfx_open_door_1
    show us smile sport far at fleft behind un with moveinleft
    show un normal pioneer with dspr
    play sound sfx_close_door_1
    "The door opened, and Ulyana rushed into the infirmary, proudly brandishing new acquired shorts."
    "I was willing to bet anything, that she stole them without anyone knowing."
    "Just because it was Ulyaana.{w} She just can't do things otherwise.{w} Or maybe she didn't want to."
    me "Didn't they teach you how to knock? I'm not dressed here, actually."
    show us grin sport at fleft with dissolve
    us "Come on! You're not shy about Lena!"
    me "Lena is a doctor, and doctors aren't those who you should be shy with."
    "I bit my tongue not to add  «the doctor is a sexless being». That would have been too much."
    show un shy pioneer with dspr
    "Lena blushed and reached for a bandage."
    show us normal sport at fright with move
    "Ulyana sat on Viola's chair and examined my wound."
    us "Yeah, it isn't so bad after all. Just broke the knife for nothing!"
    me "Well, thanks. Did you expect me to cut off my leg?"
    show un normal pioneer with dspr
    un "I have a knife."
    show us surp2 sport with dspr
    "Ulyana and I simultaneously turned our heads towards her."
    "None of us really expected this."
    un "Hunting knife. Father gave it to me."
    un "I can lend it to you if you promise not to lose it."
    show us laugh sport with dspr
    us "That was unexpected! Thanks!"
    th "So this is what happens, I climbed in the attics in vain and maimed myself for nothing?"
    th "Okay, my fault - who knew Lena had a knife."
    th "I don't understand one thing - why does she need it in the camp?"
    show us normal sport with dspr
    "Lena tightened the bandage on my leg."
    "I got up and took the shorts brought by Ulyana."
    show un smile pioneer with dspr
    un "In the evening, remove the bandage and treat with peroxide. It should be dry by morning."
    me "I don't even know how to thank you now. You are my savior!"
    show un shy pioneer with dspr
    "The girl looked away in embarrassment."
    un "Well, I..."
    play sound sfx_7dl["eat_horn"] fadein 1
    "She was interrupted by the sound of a horn."
    "With all this running around, I didn't even notice how it was already time for dinner."
    show us smile sport at right with move
    "Ulyana jumped up from her chair."
    show un normal pioneer with dspr
    us "That's it, I made sure you didn't die - my job here is done. And I still want to eat something!"
    play sound sfx_open_door_1
    hide us with dissolve
    play sound sfx_close_door_1
    "She ran out of the infirmary, leaving Lena and me alone again."
    "I was already dressed and went to the door, watching the girl with my peripheral vision."
    "She took the key from the table and turned to me."
    un "You know, yesterday I was a little…"
    "She hesitated."
    show un sad pioneer with dspr
    un "Just, sorry. I..."
    me "Ah, forget it. Nothing bad happened so."
    "Lena nodded uncertainly."
    me "So that's great."
    me "Let's go quickly to the canteen, otherwise Ulyana will gobble up everything!"
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day3_event_dining_hall1:
    scene bg map_alt2 with dissolve
    if alt_day3_duty:
        dreamgirl "Why are we even here, didn't have enough of your «duty» yet?"
        dreamgirl "Anyway you have lunch and dinner ahead of you, you will still have time to run around with the cart."
    else:
        "There was absolutely nothing for me to do in the canteen. Become a volunteer assistant on duty? No thanks."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_event_sport_area1:
    scene bg ext_playground_day with dissolve
    if ('sport_area' in list_voyage_7dl):
        "Gym teacher was nowhere to be seen, and football field was empty too."
    else:
        "Football field was empty."
    "Noticing movement in the mesh box, I got curious and approached."
    "There, Ulyanka and several boys from the younger squads were enthusiastically playing «Square»."
    if ('soccer' in list_clubs_7dl) or ('volley' in list_clubs_7dl) or ('badmin' in list_clubs_7dl):
        "And why, one wonders, did I sign up for the club yesterday?"
        "To train alone?"
        "Well, damn them. I'd better go for a walk around the camp."
    "Determining not to distract them from what was no doubt important, I turned around and left."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_event_beach1:
    $ alt_day2_beach_seen = True
    play ambience ambience_camp_center_day fadein 1
    play music music_list["take_me_beautifully"] fadein 5
    if alt_day3_date == 'sl':
        call alt_day3_morning_sl
    else:
        scene bg ext_beach_day with dissolve
        play ambience ambience_lake_shore_day fadein 3
        "The beach was not crowded, and Olga Dmitrievna, who was unfortunately present here, cut off all plans for a possible swim."
    stop sound fadeout 3
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_morning_sl:
    scene bg ext_square_day with fade
    $ counter_sl_cl = 3
    if counter_sl_7dl > 0:
        if not ((alt_day2_date == 'sl') and ('sports' in list_slavya_7dl)):
            "Like on the first day, Slavya grabbed my hand and dragged me along."
            "First, to the house, where they gave me black tight swimming trunks, more reminiscent of family boxers."
            "And then, of course, to the beach."
        else:
            "As on the first day, Slavya grabbed my hand and dragged me to the beach."
    else:
        "While giving my consent, I did not think at all that it automatically means that she would now grab my hand and drag me to the beach!"
        "No, I, in general, do not mind. But what about the general morality?"
        "Foreplay?"
        "A chance to haggle maybe? No?"
        "For Slavya, the canons of morality were something that could be neglected if desired."
        "And desire was now."
        "Ignoring the staring pioneers, she just took me in an armful and dragged me where she wanted."
        "That's who will never have problems with gossipers. Because she magically coexists with a desire to help her comrade and a disregard for public opinion."
    $ alt_day2_beach_seen = True
    scene bg ext_beach_day with dissolve
    play ambience ambience_boat_station_day fadein 2
    "In less than five minutes, I was already assigned to the case, treated kindly with attention and provided with the most valuable instructions."
    "Do not stand under the sun, do not wet your head, do not shout loudly."
    "Uh... thanks, cap?"
    sl "Semyon?"
    show sl serious swim at center
    "Is it just me, or her swimsuit became transparent?"
    sl "Semyon? Semyon, are you all right?"
    "Except for the fact that I'm slowly drifting away..."
    me "For the most part, yeah. So what are we going to do?"
    sl "Volleyball!"
    show sl smile2 swim with dissolve
    sl "Today is the junior beach volleyball championship and I would like you to referee the boys' matches while I judge the girls."
    me "Isn't it the other way around?"
    sl "Other way around..."
    "She seriously thought."
    sl "No, it won't work the other way around."
    me "But why?!"
    show sl laugh swim with dspr
    sl "Besides the fact that you won't be able to focus at all?"
    me "Please."
    sl "If a girl gets hurt, I can take her to the infirmary, I'll have enough strength. But in case of boys it could be not enough."
    me "Reasonable."
    "I had to admit she was right."
    me "When do we start?"
    sl "Oh, yes, soon already."
    "She nodded at the groups of pioneers with squad leaders at the head slowly gathering towards the beach."
    sl "They will play from the second to the fifth squads, that is, there will be three matches in total, each with 15 cans, the deployment is normal, in three touches, you can cut only past the player, in case of a cut on the player, removal from the field by two cans. It seems nothing forgot."
    show sl smile swim with dspr
    "She grabbed the whistle from her neck, hanging there on a string, and handed it to me."
    sl "Boys seem to pull up earlier, so you be the first to judge."
    "She nodded at a highly suspicious structure, resembling a hybrid of a stepladder and a plastic chair from a football field."
    sl "You can climb up there. If your balance is right, of course."
    sl "Although it's better not to, I guess."
    show sl laugh swim with dspr
    "She laughed at my questioning look."
    sl "It swings! I try to dig it down a bit every day, and the juniors blow it up every day. That's how we wage war... with varying success."
    "However, for myself, I have already decided that better no to climb anywhere."
    sl "That's it, good luck!"
    "She waved at me and disappeared at the other end of the beach, doing another - no doubt - important things."
    hide sl with dissolve
    "Because of the early sun, I had to stand with my back turned to the water, so the players, not finding anyone on the usual edge, crowded into several groups, because of that it was possible to attract their attention only with the help of a whistle."
    "Well, I blew, with all my might."
    "The ball jumping inside the whistle rattled a trill on my ears, nerves, made present pioneers to jump, and pleased the gym teacher who came to a visit."
    show ba normal uniform with dspr
    ba "Well, you have a good damn breather, son!"
    ba "You should be a swimmer."
    ba "By the way, you're on the volleyball team now, you know?"
    me "Explain please..."
    ba "You're judgin'? Judgin'. You know how to play? You do."
    show ba smile uniform with dspr
    ba "Plus a certain pioneer was asking for it."
    ba "You are in the team now, that's it."
    hide ba with moveoutleft
    "He turned around and headed towards the pontoons with a clear step. Expectedly accompanied by a whole cohort of girlish glances."
    "And I threw off the obsession trying to make me straighten my stooped back, straighten my downcast shoulders and stick out my sunken chest."
    th "What the hell!{w} I love myself even like that!"
    me "Ball in play."
    "I commanded."
    me "Team 2 against team 3. {w}Left, right?"
    "Having picked up the sword lilly under my feet, hid it in my right fist behind my back - where the captain of the third squad immediately poked..."
    "The ball was taken by the third squad, the side of the field - by the second, turning the rivals with their backs to the sun."
    "At first I didn’t believe it, I asked twice, but then, having estimated the time, I realized that if the teams had more than two games, then very soon the sun would go sideways, giving the flankers an unhindered attack diagonal."
    "This was not critical for the third squad: with a mercifully installed 180 cm net, they almost did not cut - they were not tall enough."
    "But they bet on defense and did not lose it."
    "Inevitably losing to their opponents in experience, arm length and height, they took their toll with their speed and well-coordinated play and attacks."
    "Therefore, the innings played out slowly, and it was already ten hours past the clock when I finally blew the final whistle."
    me "With a gap of three points, the team of the second squad wins."
    "A logical outcome. We too have never, ever been able to defeat the elders. {w}Life is cruel, even as a child."
    "Teams buzzed offendedly - it seems they liked to play with each other."
    me "No, lads, vacate the area! There are other people who want to play."
    "Someone young, apparently, from the third squad, decided to recoup for the defeat. Well, he decided to recoup at someone else's expense I should say."
    "I just went to the ball to pick it up - as bare feet flashed in the air, and..."
    play sound sfx_soccer_ball_kick
    extend "Ball flew far away into the bushes."
    "Cussing, I figured out a possible way to the ball and, crackling branches like a bear, crawled to get it."
    scene
    $ renpy.show("bg ext_shower_day_7dl", what = Noon("bg ext_shower_day_7dl"))
    with dissolve
    "Breaking through the bushes, I found myself in a small clearing surrounded by growth bushes, in the dense thickets of which was the ball."
    "I took it from the bushes and climbed to the exit."
    scene bg ext_beach_day with dissolve
    "The following contenders for the Sovyonok volleyball cup have already gathered on the volleyball court - a trifle of the fourth and fifth squads."
    "Age ten and under, with such a high net, they won't even make a poignant moment."
    "Well, anyway, the process of watching the ball crossing the net back and forth gives a certain pleasure."
    "The ball was already there, I picked it up under my arm and again brought the whistle to my lips."
    me "Squads, line up!"
    me "Championship of the camp in volleyball among boys. The team of the fourth is playing against the team of the fifth. Left or right?"
    ml "Left!"
    me "Fourth choice. Field or ball?"
    ml "Field!"
    "Understandable, Understandable. {w}You won't be able to cut, but you can use the sun to your advantage."
    "Although I don't think that the little ones have much experience in bullying the enemy team, but still, the morning sun hitting the eyes is a tangible head start."
    "Whistle!"
    me "Ball in play! Fifth squad starts!"
    "The game has begun."
    "…"
    show blinking with dissolve
    "…"
    "As expected, the fourth easily rolled out the fifth."
    "Well, in the final, they also successfully failed against the second one."
    "When you're a child, a difference of even one year is a big matter."
    "I wouldn't even bet, it's so predictable..."
    "I looked at my watch - one pm..."
    if alt_day3_duty:
        "I hope Ulyanka will come. I don't want to work alone at all."
    return

label alt_day3_event_library1:
    scene bg ext_library_day with fade
    play ambience ambience_camp_center_day fadein 1
    if counter_un_7dl == 2:
        call alt_day3_morning_un
    else:
        "After standing near the library a bit, I didn't dare to go inside."
        if 'nwsppr' in list_clubs_7dl:
            "Moreover, I did not complete Shurik's task yesterday."
        elif 'library' in list_voyage_7dl:
            "Moreover, after the warm reception from the buzzkill..."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_morning_un:
    scene bg ext_library_day with fade
    $ counter_un_7dl = 3
    play music music_list["you_won_t_let_me_down"] fadein 7
    "It's time to rescue the princess from the dragon's lair."
    "While the dreaded predator sleeps, blowing steam from its nostrils from time to time, I must sneak past it and free my betrothed!"
    "I have a sword and courage - more than enough!"
    dreamgirl "A bit of intelligence wouldn't hurt too..."
    th "Shush. I studied the enemy's disposition - the buzzkill is again chopping the countertop with her forehead, so it's quite possible to get past."
    "Inside, you need to divert the attention of two mercenaries guarding the most important treasure."
    "But how to do it without attracting the dragon's attention?"
    "The decision came almost instantly."
    "Window!"
    "That's right! It, like in all book depositories, is sealed up tightly, and if you get close at the right angle, you can go unnoticed!"
    "I froze and listened - quiet. Just what I need."
    "Go!"
    "I ducked to the ground and, trying not to stick my head out from behind the green fence, I rushed around the building."
    dreamgirl "Get down, oaf! They'll see you!"
    th "No they won't!"
    "After getting past the windows that go directly from the reading room, I came to a blank wall, in which there was a single window."
    "Next stage of the plan! Ideally, it would be nice, of course, to use paint, but..."
    "Under this window was loose sandy soil, the inscriptions on which could preserve very well."
    "I picked up a stick lying there and, after some thought, began to write."
    "Pulling out the tip of the tongue out of zeal, I diligently drew."
    "Shurik + Electronik = lo…"
    "Perfect!"
    dreamgirl "Lord, this is so stupid! Couldn't think of anything worse?"
    th "Shush.."
    "I picked up a small stone and threw it at the window."
    "Zero attention. Too quiet, they might not have heard."
    "Okay."
    "I took a larger stone and launched it, this time aiming at the wooden frame."
    "On the other side of the wall, something immediately rustled, someone chuckled muffledly, and, a few more seconds later, doubled stomps were heard."
    "And so our brave heroes went on to fix grammatical, syntaxical, and, most likely, genetical issues of the author."
    "My turn now!"
    "I again rushed around the building, and, crouching around the corner of the firehouse, tracked where Shurik and Electronik rushed."
    "A minute later, the buzzkill followed them."
    "Hooray!"
    "The dragon has left its perch and gone to sack the nearby villages. Its mercenaries are also busy solving problems on the personal front."
    "Now you can climb into her lair and pull out the most important treasure from there, languishing in the most closed corner."
    "I ran through the library on tiptoe and pushed the door very gently."
    stop ambience fadeout 3
    scene bg int_library_day with dissolve
    $ persistent.sprite_time = "day"
    play ambience ambience_library_day fadein 3
    pause(2)
    play sound sfx_open_door_2
    pause(1)
    scene bg int_editorial_day_7dl
    show un scared pioneer
    with dissolve
    "The door creaked softly, letting me in."
    "I just hoped the dragon didn't set a bunch traps, and all I had to do was take the treasure."
    show un shocked pioneer with dissolve
    "The treasure, armed with a scoop, hid behind the easel and looked towards the door."
    me "Princess! Hey, princess!"
    show un surprise pioneer with dissolve
    "I called in a slightly strained voice."
    me "Come on, let's rescue you from this sad place."
    "I stood at the door and held out my hand to her."
    me "Hurry, the buzzkill and its minnows are already back! Do you want to be saved or not?"
    show un laugh pioneer with dspr
    "Shuttering, she put her hand into mine..."
    "And we ran!"
    stop ambience fadeout 3
    stop music fadeout 7
    play ambience ambience_camp_center_day fadein 1
    scene bg ext_library_day
    with dissolve
    "I ran, saving my breath and preparing to repel the attack from all sides at once."
    "Lena... Well... I don't think she saw where she was running at all."
    scene bg ext_houses_day with dissolve
    "Finally, we stopped, after running far enough from the dragon's lair."
    show un grin pioneer with dissolve
    un "Of all possible ways, you chose the stupidest one."
    "She said strictly."
    un "Was it difficult to just walk in and ask?"
    "She tried to speak strictly. However, mixed with laughter, it didn't sound very impressive."
    "I shook my head."
    me "The dragon wouldn't let you go. And her assistants are bad guys too!"
    show un smile pioneer with dspr
    play music music_list["eat_some_trouble"] fadein 3
    un "Well well...."
    "She finally stopped laughing."
    un "You just stole me!"
    me "Not stole, but saved!"
    th "And now I'll take you somewhere where we'll live not-long and not-happy."
    me "What are we going to do now?"
    un "Actually, I was planning on painting a little bit. And if you would took me as a normal human being."
    show un serious pioneer with dspr
    "She frowned."
    un "Then we could take an easel with us with paints and brushes."
    un "And now, well..."
    if loki:
        un "And I've already have an idea for a drawing since yesterday."
        me "What's the idea?"
        un "Ah, your yesterday's story..."
        un "About how you hide in the forest under a huge pink blouse from the rain."
        me "But where were we going?"
    elif herc:
        un "And I've already have an idea for a drawing since yesterday."
        me "What's the idea?"
        un "I want to draw... you."
        "She was embarrassed and turned away, plucking a bush of bird cherry that was unluck enough to be there."
        me "Me? So draw, what's the problem?"
        "She was even more embarrassed."
        un "No, not like that... I want to draw you..."
        "At this point, she seems to have run out of air, because she was completely silent."
        me "So what's the problem? Do you think I'm refusing to pose?"
        un "That's not the problem. The problem is that…"
        th "I don't understand this girl. It's a simple thing to pose for a portrait. Other than staying still, there's no problem at all!"
        th "Why is she so shy? It's not like she's going to draw me naked!"
        th "Or..."
        "I broke off my thoughts and looked suspiciously at Lena."
        me "And in what form do you want to draw me?"
        show un surprise pioneer with dspr
        "She finally bloomed with a poppy color and even tried to leave - if I had not caught her by the hand."
        me "You don't want to draw me naked do you?"
        "She shook her head."
        un "No… {w}Actually, I'm already doing it."
        "After that I didn't have anything to say."
        me "Most importantly, don't show them to your roommate. {w}She'll blow them all over the world."
        me "Where were we going again?"
    un "Maybe we should come back for…"
    "She began timidly."
    "I shook my head."
    if herc:
        me "Not now. After lunch. Or tomorrow. In any position and degree of emancipation."
    else:
        me "We've already escaped, so..."
    show un smile pioneer with dspr
    "I smiled, caught her smile in response and commanded:"
    me "Let's go!"
    scene bg ext_path2_day
    show un normal pioneer
    with dissolve
    "It was not difficult to get through the camp - in the morning everyone was businesslike and hurried about their business."
    "I just had to make a more serious face, so as not to pester with questions, and drag Lena along with me."
    "Therefore, we got to the woods quickly, from where we began to coordinate further movements."
    me "Are we going somewhere or just walking?"
    "I asked."
    un "Actually, I wanted to go to the quarry and paint a little there, but since you forbade it..."
    "She spread her hands in an international «your fault» gesture."
    me "So let's go to the quarry! You probably already know the way there. And I didn't see anything apart from the camp for those three days. "
    if alt_day2_us_escape:
        un "You forgot the railroad and the islands."
        "Seriously she reminded me."
        me "I didn't forget. They just don't count."
        show un surprise pioneer with dspr
        un "W-why?"
        th "Because I was there without you, how do you not understand?"
        if loki:
            me "I promised that if I go crazy, it's only in your company. So everything before that doesn't count."
            me "Though I don't quite remember the grove yesterday."
            "I hinted with expression."
            me "I'd love to go there again. Refresh the experience."
            show un shy pioneer with dspr
            un "Wh-what?"
            me "To remember, get it? I remember Sovyonok, but everything else..."
            "Looks like if things don't work out between us, she'll be the perfect target for some harmless jokes."
            me "Take my words a little easier, okay?"
            "I sighed."
            me "I just wanted to make it clear to you that I'm ready to repeat everything that happened yesterday repeat it today, and even tomorrow, if necessary."
            un "Y-do you want here?.."
            me "Why not? We're not doing anything reprehensible..."
            show blink
            "I don't know why, but I closed my eyes. Never closed before, but now closed."
            scene bg ext_path2_day
            show unblink
            "And when he opened it - groaned softly and almost took a step back."
            show un cry pioneer with dspr
            "Fully reflecting my posture, she stood opposite, and from under the closed eyelids, drops rolled down her cheeks."
            "I touched her on the shoulder, trying to be as gentle as possible."
            show un laugh pioneer close with dspr
            "And she, opening her eyes, uttered some completely wild cry, and in a second she was on my neck!"
            un "Yahoooo!!!"
            "She screamed, completely unconcerned about bystanders."
            un "Not a dream! It was real! Not a dream!"
            dreamgirl "Looks like someone's roof is coming off?"
            th "Not only someONE's I guess..."
            "Reasonably, I remarked."
        else:
            me "I didn't really have time to «feel» them."
            "Of all the treasures that I received as a reward for slaying a dragon, the most precious one now walks beside me, holding my hand."
            "This treasure is doubly valuable because one day, she, tired of waiting for me to ripen, she just came and said «this is all mine»."
            "I can't say for her, but for me personally, everything became crystal clear yesterday, from the very moment when..."
            if herc:
                "...something sparked between the fingers convulsively clenched on the paper and the soothingly outstretched palm."
            else:
                "When she, not knowing where to look for help and protection, just hid behind my back, cuddling up as if she had no one closer to me and dearer."
    else:
        un "Are you interested in anything in particular?"
        me "First, the quarry."
        "I smiled."
        me "Haven't jumped into the sand for a hundred years."
    show un smile pioneer with dspr
    "This time, she herself found my hand and clung to it."
    "Looks like I'm staked and fenced off. Unexpected, right?"
    dreamgirl "And if you weren't retarded, you could even claim a warm bed tonight."
    th "Shame on you, pervert. We got it clean and platonic."
    dreamgirl "Oh really? So you're sayin that you would refuse her certain offer?"
    th "Hey, hey! Let's not twist my words! I said that now the soul is more important."
    dreamgirl "Have you even noticed that both her sizes are 90, both top and bottom?"
    dreamgirl "It’s so soulful there that it’s tearing up to the heels."
    "Inner vulgar laughed vilely and fell silent."
    scene bg ext_path_day
    show un smile pioneer
    with dissolve
    me "What are you even doing at the quarry by the way?"
    "I strongly doubt that she, with a screech, jumps from eight meters to the heaps of sand below."
    un "I was - walking, dreaming there before now... And there is lingonberry, not much though."
    me "Now?"
    un "Well, now I..."
    show un shy pioneer with dspr
    un "Now... I have you."
    "A simple phrase that unlocks the heart."
    "And who, if not me, should know what it really takes to say these five words."
    "I smiled softly."
    me "It doesn't hurt us anyway, does it? The fact that we have each other."
    show un normal pioneer with dspr
    un "What?"
    "Spending time together, spending it only on what you really want - on the most precious person in the world."
    "Here she is walking beside me smiling, but she is the whole world. A huge universe. Reality, if you'd like."
    "There, under half-closed eyelids, you can see the reality in which we have become each and other - for each other."
    "I'm learning all night to think about her less than once a minute."
    "And I almost succeed by the morning but I wake up with her name on my lips."
    "I close my eyes - there she is, I inhale the air - and there is her smell."
    "Instead of answering, I took out a cell phone from my pocket, where the last note was the following:"
    "{i}Where memories ripple with bitterness... I habitually leave a part of my heart. It's just that I hate you so much, Because I'm poisoned with you.{/i}"
    show un serious pioneer with dspr
    "She managed to read the quatrain. {w}Her lips moved, pronouncing the last word, trembled…"
    "Suddenly, I didn’t feel like explaining anything at all... Especially since a sandy slope was already visible through the trees."
    me "Lena."
    "I stopped and turned her around to face me."
    me "You know, I rarely made wishes in the past even when most people do - under falling stars, on New Year's Eve surrounded by namesakes, and other... circumstances."
    me "But in those moments when I wished... I think I wished to meet you."
    me "Now it's just a trifle left - make a wish so that I can take you with me, to where I will return sooner or later."
    show un smile pioneer with dspr
    un "Can't you just stay here?"
    un "I need you here..."
    me "If I am offered this option, I will agree without hesitation!"
    me "I'm feeling alive only where you are."
    "Embarrassed by the sudden revelation, I crumpled up the conversation."
    un "And what if not?"
    me "Then find me! I will leave you all the addresses where you can find me, all the contacts who may know me. Just find me."
    show un serious pioneer with dspr
    un "Good. I won't let us get lost."
    "She answered seriously."
    "Despite the conversation, it didn’t lead us to anything in the end - only when we came to the camp, I received an order to close my eyes - although I still peeped - and she, standing on tiptoe, kissed me on the cheek."
    hide un with dissolve
    "I am being friendzoned? Really? Friendzoned?!"
    "In the evening there will be another chance to straighten the rut. But I don't like the symptoms ALREADY."
    "Sighing, I directed my steps towards the local temple of gluttony."
    return

label alt_day3_event_medic_house1:
    scene bg ext_aidpost_day with fade
    play ambience ambience_camp_center_day fadein 1
    if ('medic' in list_voyage_7dl):
        "I stopped a few meters from the porch."
        "Then I resurrected in my memory every detail of what the local bone breaker had done to me."
        th "No, not again definitely!"
        "Trying to move on tiptoe, I turned around and hurried out of the infernal house."
    else:
        "Nothing interesting here."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_event_estrade1:
    scene bg ext_stage_big_day_7dl with fade
    play ambience ambience_camp_center_day
    if alt_day3_date == 'dv':
        call alt_day3_morning_dv
    else:
        $ alt_day3_dv_guitar = 1
        if alt_day2_minijack:
            "Remembering yesterday, I decided to give myself another session of loud music and went to the stage."
        else:
            "Because of boredom I decided to visit the stage."
        "Unfortunately, it was already occupied."
        "Even from a distance, I heard the lead guitar tormenting the air, tearing it apart with a sharp sound with almost painful splashes at the peaks."
        "Alisa."
        "She lowered her head so that her faces could not be seen, and diligently built a harmonic sound, putting note by note into the key of the future song."
        "Finally, she tossed her hair in satisfaction, as if putting a dot in a musical phrase, and fluently played the resulting fragment, frozen in a strange position, with her ear to the guitar, nodding in satisfaction."
        "And I sat quiet, did not dare to interfere."
        "I have always liked people who can take a few notes and build such a sequence out of them that they will express the experience completely, down to the last thought."
        "And now I was present at the birth of a new melody. So I was in a certain sense in awe."
        "Finally Alisa finished."
        show dv normal pioneer2 far with dissolve
        dv "You've been here for quite a while, huh?"
        "She asked in calm voice."
        "I nodded."
        if loki:
            dv "Do you want to try? To play."
            "I swallowed noisily."
            me "Will I be able to even?"
            show dv smile pioneer2 far with dspr
            dv "It's not that hard. I'll show you."
            me "I don't really get why..."
            "I sighed."
            me "But I'll try."
        else:
            show dv smile pioneer2 far with dspr
            dv "So why are you sitting like a poor relative?"
            "She flashed a quick smile."
            show dv normal pioneer2 far with dspr
            dv "Sit down here, the stereo is best heard here."
        show dv normal pioneer2 with dissolve
        me "You're kind of weird today."
        "I said thoughtfully."
        if herc and (alt_day2_date == 'un'):
            show dv shy pioneer2 with dspr
            "She was embarrassed and looked away."
            dv "Thoughts of Lena gives me no rest."
            dv "You went to her cabin in the evening, rumors are already creeping around the camp."
            dv "I... I have a bad feeling about this."
        elif (alt_day2_date == 'mi'):
            dv "I'm thinking about you and Miku..."
            if alt_day2_mi_date == 2:
                me "She wanted to walk with me under the same umbrella, and I said there wasn't enough space."
                dv "I'm sorry, what?"
                me "Japanese allegory...  «To walk under the same umbrella» in everyday life means to date."
            else:
                dv "What is it like? Kissing on the beach. Sounds almost like the title of a snotty melodrama."
                dv "And what is it like, to see a person for the first time in the morning, and in the evening..."
            "She waved her hand."
        else:
            dv "Rumors are spreading around the camp. About you."
            me "And what do they say?"
            "I got interested."
            dv "Things."
            "Alisa answered evasively."
            "Things. What things, I wonder? About my wardrobe or about yesterday..."
            me "What do you think?"
            "She shrugged."
        "I paused and was about to leave when she called out to me."
        show dv sad pioneer2 with dspr
        dv "Hey!"
        "I turned around slowly."
        dv "Did you like the song?"
        "Noticeably worried, she asked."
        me "Honestly? I haven't heard the whole thing yet. Just a little bit."
        dv "Would you like to listen to the whole thing then?"
        me "You're unlikely to play right now, you're still in the process of..."
        dv "Well... yes! But in the evening... In short, if you want to hear full song, I'll be waiting here in the evening. Will you come?"
        menu:
            "Of course":
                $ alt_day3_dv_guitar = 2
                $ lp_dv += 1
                me "Who am I to refuse such invitations?"
                me "What time?"
                dv "Right when disco starts."
                "Somehow I wasn't surprised that this girl at least dislikes what the local country club called dancing."
                me "So you won't dance?"
            "Sorry, I can't.":
                me "But there's a disco tonight! Aren't you coming?"
                dv "Pfff, what am I supposed to do there? Stare at morons or act like morons while waving my arms to the weird music?"
                me "There's not only weird music. There's also slow music."
                dv "Uh-huh, that's a good excuse to snuggle up on the dance floor."
        "She upset me with such statements."
        if lp_dv > 7:
            me "That's a pity, you know."
            dv "What?"
            me "That you are... well, that you don't like dancing."
            me "If you were there, I would definitely invite you to dance."
            show dv shy pioneer2
            dv "Get that nonsense out of your head."
            "In a quiet voice, separately minting words, she said."
            dv "Don't expect to get through me with such nonsense, I'm not fourteen years old already."
            me "And not thirty either. I'm serious about dancing."
            "It took me only three days to guess that Dvachevskaya - what a surprise - was a girl."
            "Not in the sense of chastity, but in the sense of belonging to the ladies."
            "And now this thought haunts me."
            "However, what kind of bridges can be built between souls with diametrically opposed interests?"
            "Music? Co-indulgence? Beauty in the most primordial sense of the word, from stars and sunsets to nude swimming?"
            "She quieted down, as if thinking, I stood at the same spot, and the surf roared in my ears."
            "It was so calm and empty that I was surprised to hear my own voice."
            me "Well, if you somewhat change your mind - my invitation is still valid... for dancing."
            hide dv with dissolve
            "Then he turned around and left."
            "Like any other sympathy, it should not wander inside, risking to vanish any second."
            "It needs to be shared, exhaled. That's what is right, and that's when something sincere and real is possible."
            "And I walked, feeling my back burning between the shoulder blades from the gaze behind, and did not turn around, did not turn around I said!"
            "Even if nothing happens, at least I've done my best."
        else:
            me "I get it."
            "I held out."
            me "Okay. In that case, I won't bother you anymore."
            "Waving to her, I left this inhospitable place."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_morning_dv:
    scene bg ext_stage_big_day_7dl with fade
    $ counter_dv_7dl = 2
    if alt_day3_duty:
        show dv sad pioneer2 with dissolve
    else:
        show dv normal pioneer2 with dissolve
    "Alisa was here."
    if alt_day3_duty:
        "And instead of the perky, mischievous creature familiar to me, to which I had already managed to become attached, another facet of Alisa opened up to my eyes - Dvachevskius saddius."
        "She hunched on the edge of the stage, her legs hanging down, and melancholy plucked the strings of an acoustic guitar, playing something not familiar to me, but undoubtedly extremely sad."
        me "Hello pretty girl!"
        "I stopped at a distance so as not to distract her from the music."
        "She seems to have noticed me."
        dv "Oh, it's you."
        "She said blankly."
        me "Uh… yes. Were you hoping to meet someone else?"
        dv "Not really..."
        "She continued to pluck the strings, but I still couldn't see her eyes through her bangs."
        "It was impossible to determine in what mood she was by her voice. And she did not want to be imposed at all."
        me "I hope I'm not too late."
        "I said carefully."
        dv "No. Just three hours."
        "I glanced at my mobile and grabbed my head."
        "My mother is a woman... Half past eleven already!"
        dv "Uh-huh. I'm sitting here waiting for you like an idiot. {w}And you're playing childish war games in a meantime."
        me "What? What war games? I n-not…"
        dv "Ah, cut it, you are not, you are yes. You were peeling potatoes, you were playing war games, doesn't matter already, really."
        "She slapped the strings with her palm and put the guitar aside."
        show dv normal pioneer2 close with dissolve
        "She jumped off the stage and came closer to me."
        if ('medic' in list_voyage_7dl):
            "Not as close, of course, as Viola did yesterday, but still enough to make me feel uncomfortable."
        "I could feel the warmth of her skin, the smell of her breath, and that electric sensation that portends big trouble."
        show dv smile pioneer2 close with dspr
        "She held out her hand to me, and I involuntarily closed my eyes."
        dv "There is no other way of dealing with Ulyana anyway."
        show dv laugh pioneer2 close with dspr
        "She laughed because of my reaction. "
        dv "She turns any business into a circus."
        "Alisa quickly removed the remaining potato skin from my hair and shaked it in front of my nose."
        dv "And that's why you are still here and not at the infirmary."
        "She tossed the pelt aside."
        dv "We don't have time to go out. {w}So I suggest we move to the music club."
    else:
        dv "While you were doing you business, I changed my mind. I don't want to go to the rock today."
        "Yeah. When someone says they want something, and then they don't want it, they probably want it, beg for it."
        me "It's up to you, even though I'm curious. Then what are we going to do?"
        dv "Let's go visit Miku!"
    me "Yesterday you didn't want to..."
    dv "I don't want to now either. But I have business with Miku. And I heard you can play guitar a little."
    me "Kind of..."
    dv "{i}'Kind of'{/i} is enough."
    "Another scene from the sitcom - me as a tough guitarist who barely learned three thieves' chords, and two girls who seem to know music at the level of, if not a professional, then a very, very decent amateur performer."
    "I hesitated..."
    me "I haven't played in a while..."
    dv "It's not scary."
    "She was already moving towards Miku's hideout, and I had no choice but to follow her."
    dv "We'll explain and show you."
    "Yeah, and if you don't want to, we'll force you. I know Alisa's methods of persuading the recalcitrant."
    if alt_day3_duty:
        "In any case, I have no choice, I already screwed up so well with these potatoes. I have to be calm and do what they say."
    scene bg ext_musclub_day with fade
    play ambience ambience_music_club_day fadein 1
    play music music_list["so_good_to_be_careless"] fadein 1
    show dv smile pioneer2 at cleft with dissolve
    me "And anyway."
    "I caught up with her and tried to start a conversation."
    me "What are we going to do?"
    show dv surprise pioneer2 with dspr
    dv "Didn't I tell you?"
    dv "Play!"
    me "What are we going to play?"
    dv "Music, of course."
    me "Programmer style answer. Thank you for giving me a whole nanosecond of your time."
    "She didn’t understand anything, although didn’t ask questions - we had already entered the terrace, and Miku was taxiing towards us, for some reason extremely concentrated, looking at her feet and not paying attention to anyone."
    show mi smile pioneer at cright with dissolve
    show dv smile pioneer2 at cleft with dissolve
    dv "Hol' up! Where do you think you going?"
    "Alisa grabbed her by the hand."
    mi "What's the matter?"
    show mi happy pioneer with dspr
    "She looked up and rejoiced."
    mi "Alisa, Semyon! It's good that you came! I came up with a new song here! Do you want to listen?"
    show dv normal pioneer2 with dspr
    dv "Now!"
    "Alisa cut it of instantly."
    me "But why n..."
    "I started, but then a graceful heel fell on my sandal toe and pressed down with all its might, forcing me to shut up."
    dv "Look, next time. We're here on business."
    mi "I'm listening."
    "Miku pocketed her keys and pushed open the door."
    mi "Come in, don't be shy."
    stop ambience fadeout 2
    play sound sfx_open_door_2
    pause(1)
    scene bg int_musclub_day with dissolve
    $ persistent.sprite_time = "day"
    play ambience ambience_music_club_day fadein 3
    "Alisa did not fail to take advantage of the offer. And then, inside, she went to what we seemed to have come for - an electric guitar."
    show dv normal pioneer2 at cright with moveinright
    dv "Here!"
    "She took a few chords, and, grimacing, immediately reached for the tuning pegs, adjusting the strings."
    dv "What did you do with the instrument, you, fiend?!"
    show mi smile pioneer at cleft with moveinleft
    mi "That's what we agreed upon - changed the broken string, didn't touch anything else."
    mi "I know that sound is an individual matter for each musician, so I didn't touch anything. You would be offended if I decided to tune the guitar."
    dv "That's right... But how did the rest of the strings get out of tune?!"
    show mi dontlike pioneer with dspr
    "Miku turned away and shrugged."
    show dv angry pioneer2 with dspr
    dv "Uh... That's what «let the goat into the garden means». Fine, I'll readjust it then."
    "For a few more minutes she did something with the guitar, until she achieved some relatively tolerable sound."
    dv "Hey, Miku!"
    mi "Yea?"
    "The girl turned mistrustfully."
    dv "Semyon and I want to play something. But it would be better if we were a trio. How's that sound?"
    show dv normal pioneer2 with dspr
    show mi normal pioneer with dspr
    mi "With a great pleasure!"
    "She shimmered!"
    "She ran to the piano, where the guitar was, as it seems like, being used as a dust collector, taking a couple of chords, nodded."
    show mi happy pioneer with dspr
    mi "I am ready!"
    dv "Great!"
    "Alisa looked at her skeptically."
    dv "Didn't forget anything?"
    mi "No! I took everything into account, and I picked a guitar because I don’t know what we will play ..."
    show dv laugh pioneer2 with dspr
    if herc or loki:
        me "I still need an instrument, you, dummie!"
        "I laughed."
        me "Or in your cool band I am assigned the role of a vocalist?"
    else:
        dv "Give him a tool, dummie."
        "Alisa burst out laughing."
        dv "How will he play?"
    show mi sad pioneer with dspr
    mi "Ah, of course, an instrument."
    "Miku scanned the drum deposits and looked at me searchingly:"
    mi "Maybe you..."
    me "Forget about it."
    "I shook my head. Of all the tricks of drumming, all I learned was to tell the difference between a hat and a snare."
    me "I don't even know how to approach them."
    mi "A pity. We could use a drummer."
    mi "Well then."
    "She looked at Alisa."
    mi "Don't you want to give him your guitar?"
    show dv normal pioneer2 with dspr
    dv "No."
    mi "Your choice."
    "Miku nodded accommodatingly and rattled with her instruments again."
    "She didn't even think of giving me her own guitar."
    "That's expected. I wouldn't give it either."
    "Finally, her search was crowned with success, and with the victorious «Ta-dam!» she brought to light an acoustic guitar without half the strings."
    me "Um... how should I play this?"
    show dv smile pioneer2 with dspr
    dv "What's wrong? You'll be a nice bassist."
    me "Very funny. Miku, do you have spare strings?"
    show mi smile pioneer with dspr
    mi "Of course!"
    me "How long will it take?"
    mi "Me? Not long at all. The instrument is yours, and you have to suffer with it now."
    me "Thank you."
    "I could not resist to mock them."
    me "You and Alisa deserve each other."
    "Under the strict guidance of the girl-orchestra and the red-haired guitarist, I managed to fix the strings in the shortest possible time. and before lunch we managed to strum a little, playing along."
    "Well, to «strum»."
    "At first Miku grimaced, took the instrument away from me and twisted the pegs for a long, long time, then Alisa took the guitar and also tried to adjust the sound to match her own instrument..."
    "As she said, «so that they don't go to the neighbors»."
    "I didn't understand what she meant, but she probably knows better."
    "Even though neither of them even used a tuning fork as a standard of sound, focusing solely on their own ear, I seriously doubted that we would ever achieve the perfect sound."
    "In any case, the guitar fell into my hands again, and the ordeal began with the placement of fingers, selection of chords and other things which were completely out of my depth."
    "In the end, Alisa's patience snapped, and, looking at her watch, she said in a tone that brooked no objections:"
    if alt_day3_duty:
        dv "So, time for someone to go to the canteen to their duty and stop torturing my unfortunate ears."
    else:
        dv "It's time to end this nightmare. It looks like we offended this instrument more than we wanted to. Put it where you got it. Careful. And let's go."
    if 'music' in list_joined_clubs_7dl:
        me "I told Miku right away, I'm more into brass... Trumpet, viola, baritone... Yes, even on this unfortunate trombone I can manage something. And on the guitar..."
        mi "Let's learn then!"
        "Miku said confidently."
        mi "Especially since it's amateur day on Friday, and you need a performance."
    else:
        mi "Almost forgot! We have an amateur performance day on Friday, and Semyon needs to prepare a performance."
    me "Me? Performance?!!!"
    show dv laugh pioneer2 with dspr
    "I was seriously considering running away at this point."
    me "I don't remember signing up for anything like this!"
    show mi happy pioneer with dspr
    mi "Nevertheless, you are listed as an applicant."
    "Miku showed the schedule of performances and pointed there with her finger. On the fourth line was my name."
    me "Aaaaaah!"
    play sound sfx_open_door_strong
    scene bg ext_musclub_day with fade
    "I yelled and ran out of this lair of people who hate me."
    "A harmful laugh was heard from behind."
    "I think I can guess who signed me up!"
    dv "Don't forget! Same place, after lunch!"
    "Alisa's voice came from behind."
    return

label alt_day3_event_square1:
    scene bg ext_square_day with fade
    "Everything was the same at the square - Genda, benches, flags."
    "Unlike yesterday, Slavya wasn't here, which means no one can indoctrinate me into an extraordinary cleaning... {w}With flag hoisting as a reward."
    "Shrugging my shoulders, I turned around and walked on."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_event_boat_station1:
    scene bg ext_boathouse_day with fade
    play ambience ambience_boat_station_day fadein 3
    "It was quiet and peaceful here."
    "Unlike the beach, this access to the water did not seem to be popular - maybe due to the fact that a stern, old, boatman sat here ..."
    "Maybe it's because the springs that found their way out near the surface, which, among other things, also power our water systems."
    "To put it simply, it was uncomfortable and cold here."
    "Although for everyone who wanted to pump up their arms or legs a little, punt boats and catamarans were available."
    "I leaned on the railing, releasing the memory..."
    "Here, we are on a walk with my father ... Or rather, he walks himself, and I ride on his neck."
    "Now I understand that his height is below average, and even I, with my unfortunate meter eighty-five, overtake him ... And then it seemed to me that he was the biggest, the strongest ... "
    "After he started a new family in another city, I stopped thinking like that."
    "But that will be a little later. In the meantime, I was riding on his shoulders, and everything around was so exciting - from slowly falling maples to the frozen mirror of ponds, in which Venus and Apollo flaunted with their heads thrown back."
    "He bargained for a couple of minutes with the ticket attendant - she didn’t want to let «pot-bellied trifles» into transport, and for some reason my father got into his head that it was vital for him to give me a ride on a catamaran."
    "He looked into the eyes of the usher and in his voice, almost purring, gave an irrefutable argument:"
    voice "Don't be mean, honey. The kid might never get the chance."
    "And as if he knew. Since then, I have never, never sat on a catamaran, despite the fact that I perfectly remember what an intoxicating feeling it is when the muscles of the elements holding us sluggishly roll under something ligher than water."
    "At first there were no opportunities, then time ... Now desires."
    "Father then uncorked the «72» as soon as we moved away from the shore, but he took only one sip."
    "He himself, as if frozen, looked lostly at the water, then at the sky."
    "He left three days after, and mother forbade his name from being used in the house."
    "Here you have a special relationship with water and catamarans."
    "For me, they will always be the harbinger of the worst news."
    "From the beach came the clapping of the ball and gambling children's yells."
    "It seems that Slavya is babysitting some juniors again. It seems that she likes it."
    "A Godly teacher."
    if loki:
        "It's a pity, of course, that she was sparked with this stupid idea of ​saving lives."
        "Life can only be saved by raising it on your own."
    "After standing still a little, I turned around and returned back to the camp."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_dinner:
    scene bg ext_dining_hall_away_day with dissolve
    play ambience ambience_camp_center_day fadein 1
    pause(1)
    if alt_day3_duty:
        play music music_list["i_want_to_play"] fadein 1
        "Dinner was indeed approaching, and Ulyana and I ended up at the canteen room at about the same time."
        show mt normal pioneer at right with dissolve
        "Olga Dmitrievna was waiting for us here, it seems, she was very nervous, glancing at the elegant heart-shaped watch on her wrist."
        "When she saw us hurrying, she breathed a sigh of relief, however, immediately hiding that behind the mask of an angry and enraged squad leader:"
        show mt angry pioneer with dspr
        mt "Where were you dallying?! {w}Dinner is in twenty minutes!"
        show us smile sport at left with dissolve
        us "Not our problem!"
        "Ulyana looked into the eyes of the squad leader brazenly and with a challenge."
        us "We were told to come at fifteen, but we came at twenty!"
        us "You should praise us!"
        show mt surprise pioneer at right with dspr
        mt "I? What are you..."
        me "Of course! It's thirteen minutes for a regular pioneer. And for us it's fifteen!"
        show us laugh sport at left with dspr
        us "Considering that ten minutes out of fifteen we'll be lazying off!"
        "The little one blurted out, and the squad leader, unable to resist it, laughed."
        show mt laugh pioneer at right with dspr
        mt "Alright, quick ones. {w}Wash your hands and let's go."
        me "Come... what?"
        mt "I decided to help you, what's wrong?"
        "She seemed so surprised that I believed her for a whole second - she really, wants to provide all possible assistance to the plodding pioneers."
        me "I don't think you can help..."
        stop music fadeout 2
        "I frankly doubted that she would find a place in our small tandem, but it was interesting to see."
        play sound sfx_open_door_2
        pause(1)
        scene bg int_dining_hall_day
        show us dontlike sport
        with dissolve
        play music music_list["that_s_our_madhouse"] fadein 3
        "We went into the canteen, and then I realized how she was going to help!"
        "She went to the distribution, talked about something with the cook, took a cup of tea, and, sitting at the table reserved for administration, sat and looked at how we work."
        "Well, yes, as I already said, it is natural for a person to observe the primary elements almost endlessly - how water flows, how fire burns... And how others work."
        us "Most importantly, don't overwork yourself..."
        me "Your help is invaluable! I really don't know what we would do without you."
        mt "Here! Appreciate it, pioneer!"
        show us upset sport with dspr
        "Olga raised her finger importantly, and Ulyana snorted and muttered something about the fact that some people don't work, but yell the most."
        "Fortunately, the squad leader didn't catch the line, and the redhead managed to avoid a legal stick."
        "Meanwhile, we had already run around half of the dining room, scattering compote and saucepans with soup - the younger squads were already rushing into the dining room, despite the fact that there was still no sign of a horn."
        scene bg int_dining_hall_people_day with fade
        play ambience ambience_dining_hall_full fadein 1
        "We stuffed these with the same soup, placing a stack of plates on each table, as a warning to the squad leader - if you can't hold back the children - feed them yourself."
        "I had to work quickly, without being distracted by stupidity, and I was completely absorbed in the process: running around with a cart, {w}arranging plates, {w}turning over raised chairs where possible, {w}setting up benches so that the kids could sit down."
        "Finally, we worked through the last table, and like the horn of the Valkyries, taking the fallen warriors to Valhalla, a signal was heard from the door for dinner."
        play sound sfx_7dl["eat_horn"] fadein 1
        "Next stop - full stomach!"
        if (alt_day2_date == 'dv') and (alt_day3_date == 'dv'):
            "As at breakfast, Dvachevskaya grabbed me by the elbow and dragged me to her table to eat, otherwise I would have been sitting in some kind of incomprehensible devastation on a bench, forgetting why am I even here now."
            stop sound fadeout 3
            show dv smile pioneer2 at left
            dv "Let's go eat, Mother Teresa!"
            "She laughed as she picked me up from the bench."
            dv "Or you'll fall asleep hungry."
            stop music fadeout 3
            me "Thanks."
            "From the bottom of my heart I thanked the red-haired benefactor."
            "Olga Dmitrievna splashed pickle on the plates, passed the plates to pioneers, and for several minutes only sipping reigned in the room with the sound of spoons hitting bottom of the plates."
            "That's right, in real life there is a place for troubles and a place for dinner. Having thrown off the numbness that had attacked me for the second time after working in the canteen, I suddenly felt that I was brutally hungry, and the ice cream that the chefs lent me - I didn’t even share it with Alisa - was obviously not enough."
            "Finally, the soup was wrinkled. Ulyanka and I finished, and we fell off the table with our stomachs full."
            if herc:
                dv "Looks like you're in a disabled position right now and there's no point in dragging you anywhere?"
                "Alisa winked."
            else:
                dv "I was thinking of taking you out into the sun to bask, but you seem to be incapacitated right now."
                "Alisa smiled."
            play music music_list["eat_some_trouble"] fadein 2
            show dv laugh pioneer2 at left
            dv "Anyway, I don't want to wait another half an hour for you, so I'll help you and Ulyana clean up."
            me "You?! Voluntarily?!"
            "It seemed to me that I misheard. No, of course, we are friends but..."
            show dv grin pioneer2 at left
            dv "Well... Not exactly voluntary. And certainly not for free."
            "She smiled mischievously."
            stop ambient fadeout 3
            "I chose not to think about what might be behind that smile."
            "Alisa is like that after all, you can expect anything from her."
            "With the involvement of new hands the cleaning process went even faster. Although at the first - and at the second - glance those hands didn't have the zeal for public work."
            "The inner Petrosyan again quipped, saying that a lazy person does everything at once in good conscience - so as not to redo it later - and quickly - in order to deal with this quickly."
            "Although there were..."
            show us smile sport at right
            if alt_day2_us_shenan:
                me "Drop that!"
                "I had to bark at Ulyanka to stop."
                "One of the plates had the same construct as the one I built yesterday - it looks like the earth is full of rumors."
                th "Children absorb information about bad things catastrophically quickly."
                me "If I'd pick it up right now..."
                "I carefully carried the plate to the dishwasher window as gently as I could and put it there - to the company of several more of these «cocktails»."
                us "Cool! You didn't show me yesterday!"
                me "There is nothing to show... You pour it and turn it over. You see, even random pioneers could do it."
                us "I'll definitely try it in the evening!"
                me "…and will clean it yourself? You're on duty, remember?"
            "At this point, Alisa had just finished smearing the dirt on the floor and, having collected a few dust particles on a dustpan, solemnly put the tools in a corner."
            dv "I'm done, and you?"
            me "We too!"
            play sound sfx_open_door_2
            pause(1)
            scene bg ext_dining_hall_near_day with fade
            show us grin sport at right
            us "Okay, I need to go."
            hide us with dissolve
            "The little one waved her hand and disappeared in the direction of the beach."
            show dv sad pioneer2 at center with moveinright
            dv "You know..."
            "Alisa strangedly looked at me."
            dv "Ulyanka has really grown attached to you these days. What are you going to do about it?"
            me "Uh... Nothing? Why should I do something about this?"
            play music music_list["farewell_to_the_past_full"] fadein 3
            dv "Didn't occur to you that she is an impressionable girl, tender age..."
            "I narrowed my eyes suspiciously."
            me "Dvachevskaya, what are you talking now, or is this someone's corrupting influence?!"
            "I'm ready to bet that behind of what Alisa was saying to me just now, Olga Dmitrievna's ears looked out. ."
            "Olga is also a «good» fellow too. As if it’s not clear that if you attached up to someone once, it’s useless to resettle you - you will still be attracted to each other!"
            show dv shy pioneer2 with dissolve
            "She was embarrassed, but didn't look away."
            dv "I'm really worried about her and I'll tear anyone who offends her."
            me "I'm already afraid!"
            "Laughing, I raised my hands in front of me."
            me "But I'm not going to offend her. You heard."
            "I lowered my voice and Alisa was forced to come closer."
            me "She ordered! {w}That's right! {w}That the next time we escape the camp, we'll do as she says."
            show dv laugh pioneer2 with dissolve
            dv "Are you going to run away again?"
            "Alisa burst out laughing."
            dv "Today's duty is not enough for both you, is it?"
            me "Personally, I'm not going to. But shhh, keep quiet about it."
            dv "And how are you going to jump off? {w}At the last moment from the departing train?"
            me "No, that's unethical."
            "I shook my head."
            me "But I have a few ideas on this subject. You, most importantly, should play along with me."
            "She thought."
            show dv normal pioneer2 with dissolve
            dv "Okay. But no nonsense."
            me "No nonsense!"
            "I solemnly promised."
            me "Everything will be according to the mind, honor and love!"
            show dv grin pioneer2 with dissolve
            dv "Clown."
            dv "Did you forget about the club? Will be waiting for you there. Pull yourself up."
            "As if cutting off something, she abruptly turned around and hurriedly headed towards the music club."
            hide dv with dissolve
            "After sitting on the bench for a while and sighing that no one appreciates me and doesn’t give me rest, I got up and trudged after her."
            $ lp_dv += 1
            return
        else:
            "Dvachevskaya sat down next to Ulyanka, so it was definitely haram to go there - well, to hell, both of them!"
            "I looked around for a free spot:"
            stop sound fadeout 3
    else:
        play sound sfx_open_door_2
        pause(1)
        scene bg int_dining_hall_people_day with dissolve
        play ambience ambience_dining_hall_full fadein 5
    stop music fadeout 3
    with fade
    menu:
        "Sit with Lena" if not ((alt_day2_date == 'un_fz') and (counter_un_fz == 0)):
            if (alt_day2_date != 'un_fz'):
                play music music_list["reflection_on_water"] fadein 3
                call alt_day3_lp_checker(alt_dater = un)
                if counter_un_7dl == 3:
                    "It turns out that the recipe for becoming necessary is extremely simple - you just need to get a person to do what they hate."
                    show un smile pioneer with dissolve
                    "And turn it on yourself."
                    "While I'm peeling off the many layers of protection from an onion-like whirlpool girl, surrounded by imaginary phobias, restrictions, and mistrust, I, willy-nilly, am getting a little better myself."
                    "Anyway, simple dialogue no longer gives me the anxiety that it used to. And I don't wait for people to finally stop bullying and wasting mine and their time."
                    me "Not busy?"
                    un "No."
                    "Perhaps I rush too much, but it seems that she really enjoys me!"
                    "How she perked up, her eyes sparkled, her shoulders straightened ... "
                    "Although I don't think there's anything serious on her part."
                    "It seems she left everything that held her back before in the cabin under two mattresses,."
                    dreamgirl "You should decide on yourself first, «supporter»."
                    th "What's wrong with me?"
                    dreamgirl "You like her, right?"
                    th "Well…"
                    "I would probably blush if the dialogue was aloud. However, I probably blushed anyway."
                    "She took the glass in her hand and tapped it lightly with the spoon, listening to the tone."
                    th "W-well, yes! I like her!"
                    dreamgirl "Then why are you reflected in her eyes either like a big teddy bear that she wants to take and squeeze from an excess of feelings..."
                    dreamgirl "Or like a divorced girl's Sunday visiting dad."
                    dreamgirl "Is this the relationship you want from this girl?"
                    th "Of course not! Brrr... {w}I don't want to be a friend. {w}I'm not happy with that."
                    dreamgirl "She thinks otherwise."
                    dreamgirl "Have you thought about being her human-catalyst?"
                    "In the five minutes that I sat, looking thoughtfully at her, she managed to wriggle all over. And by Ulyanka's surprised remark she reacted with arrogantly turning up her nose."
                    dreamgirl "Did you notice how she liberates herself in your company? Mind you, not for you tho."
                    show un smile2 pioneer with dspr
                    dreamgirl "You serve as an anchor for her, relying on which she can afford to indulge, shock others and enjoy life to the fullest."
                    dreamgirl "I hate to say it, but it looks like you're really becoming her friend."
                    show un normal pioneer with dspr
                    "She seems to have noticed how stern my look is, because she immediately stopped messing around and looked into my eyes."
                    un "You aren't eating anything again."
                    "Alarmed, she said."
                    me "Thanks mom, I'm full."
                    "I answered automatically."
                    un "Something happened? You look like you've been disappointed in some way."
                    "Probably because something like that happened."
                    me "I'm just trying to find the boundaries between a guy and a girl relationship. To really separate the romantic part from the friendly part."
                    show un serious pioneer with dspr
                    un "Oh, when you're done, tell me. There's more than one volume written on this topic, but maybe you can do it."
                    me "Lena, and if without giggles. Put your hand on your leg, and say."
                    "She chewed on the cutlet and looked at me questioningly."
                    me "Is there something you don't like about me as a boyfriend?"
                    show un surprise pioneer with dspr
                    "It seems that she was glad that she chewed. Since such a question would have choked for sure."
                    un "Wh-what? What are you talking about?"
                    me "I'm sorry... This is not a canteen conversation. Let's talk after lunch, okay?"
                    "She nodded, still staring blankly."
                    me "What are you going to do after lunch?"
                    show un shy pioneer with dspr
                    un "I wanted to draw."
                    "She emphasized the last word."
                    me "Okay, I'll pick you up at the library and help you get everything you need."
                    me "I hope you don't have to carry the easel too far?"
                    show un smile3 pioneer with dspr
                    un "No, I'll draw with a tablet."
                    me "Then it's a deal. Meet me at the library."
                    $ counter_un_7dl = 4
                    stop music fadeout 2
                    stop ambience fadeout 2
                    with fade
                    return
                else:
                    me "C-can I?"
                    "Confused, I asked."
                    show un shy pioneer with dissolve
                    un "Yes."
                    me "Bon appetit!"
                    "Deliberately cheerfully I said."
                    un "Thanks."
                    "Well, that's a dialogue for sure."
                    "I began to think about topics that could be discussed with this girl, when she suddenly broke the silence."
                    un "Tell me, are you going to dance today?"
                    me "I'm not really a big fan of rural discos."
                    show un sad pioneer with dspr
                    "She was visibly sad."
                    me "However, that doesn't mean «no»..."
                    me "And if I have an incentive..."
                    un "Incentive?"
                    "She looked at me."
                    me "Yes. For example, if you'll be there."
                    show un shy pioneer with dspr
                    "I blushed again - and so did she."
                    un "I don't know."
                    "She whispered."
                    un "I can't."
                    me "Me too. We can study together."
                    show un smile pioneer with dspr
                    "She smiled shyly at my questioning look."
                    un "Let's try."
                    stop music fadeout 2
                    stop ambience fadeout 2
                    with fade
                    return
            else:
                play music music_list["reflection_on_water"] fadein 3
                "Lena kept a little aloof, but there was not that much tension in her as in the morning."
                "I stood behind her in line for distribution."
                me "Can you take a seat for me please?"
                show un sad pioneer with dissolve
                "The girl shuddered and turned around, as if she wanted to make sure that I was talking to her."
                "We made eye contact."
                "I couldn't understand why there was so much sadness in her eyes every time she looked at me."
                "You can't say that she was cheerful and provocative in those moments when I had the opportunity only to watch her from afar, but I had a strong feeling that I spoiled her mood with my very appearance."
                th "What the hell am I doing?"
                th "Better not to say anything."
                un "Okay."
                hide un with dissolve
                "Seizing her tray, she disappeared among the crowd of pioneers."
                "I absentmindedly selected some of the offered food, looking after her."
                "The best solution would be to leave her alone."
                "Let the girl forget about my existence and not give unnecessary reasons for sadness."
                "But I have already expressed my desire to sit with her."
                "Maybe it didn't make her too happy about it, but I made a kind of a promise."
                "And to break it would be disgusting."
                show un normal pioneer far with dissolve
                "When I found among the tables the one at which Lena was sitting, she stirred the soup with a spoon without much enthusiasm, constantly looking around."
                th "I wonder if she hopes I'll change my mind, or is she afraid I won't come?"
                show un shy pioneer with dissolve
                me "The day started out great today."
                "I put my tray on the table."
                me "I wonder what I should expect next?"
                dreamgirl "Are you hinting to her that she would hide you somewhere from the evil and cruel reality in the face of Ulyana and the squad leader?"
                dreamgirl "It is desirable that this place be quite secluded. Her cabin is ideal if her neighbor is accommodating."
                th "I'm not implying anything! Just trying to make small talk."
                un "There's going to be a ball tonight. I think we'll all be involved in the preparations."
                "Ball? I already heard something about it, but I didn't know any details."
                show un normal pioneer with dspr
                un "We're the senior squad."
                "She didn't show much enthusiasm for it."
                me "You don't like that?"
                un "What exactly? Dances or preparations for them?"
                me "Both."
                show un smile pioneer with dspr
                un "I'm willing to help with the organization if asked. Clean up the square, or put up garlands."
                show un normal pioneer with dspr
                "She pushed her bowl of soup away from her without touching it."
                un "But I don't like dances themselves. I can't dance."
                "Yes, it was quite difficult to imagine Lena jumping to Modern Talking (or what usually plays here? Pugacheva?)."
                me "I'm not a fan of antics to music either. Do we have to go to the disco even?"
                mt "Not only do you have, but you must!"
                show mt normal panama pioneer at fright
                show un shocked pioneer
                with dissolve
                "Olga Dmitrievna crept up so unexpectedly that I involuntarily squeezed the spoon with a grip convenient for hitting."
                "You can't scare people like that!"
                "Lena stared fearfully at my hand clutching the spoon."
                "Noticing this, I relaxed - I don't want to acquire a reputation of a paranoid schizophrenic."
                show mt grin panama pioneer
                show un surprise pioneer
                with dspr
                mt "If you try to shirk, I'll punish you."
                th "Yeah, the totalitarian regime in this camp is thriving."
                th "Maybe I'll be reprimanded tomorrow at the lineup for not being funny enough during the disco?"
                me "Maybe we can make a deal?"
                show un normal pioneer with dspr
                "I jokingly suggested."
                show mt smile panama pioneer with dspr
                mt "Okay."
                "Quite unexpectedly, the squad leader agreed."
                "Is it possible that sympathy is not alien to her?"
                mt "You will now go to Slavya, and she will entrust you with some organizational work. Extra hands will not hurt."
                show mt grin panama pioneer with dspr
                "Olga smiled slyly."
                mt "And in gratitude for this, I will, so be it, let you not dance at the disco, just sit on the bench!"
                "Of course, what else could I expect from her."
                "I began to have a strong feeling that our squad leader chose the profession of a teacher solely for the purpose of trolling naive children."
                me "Olga Dmitrievna, your generosity knows no bounds!"
                "She giggled."
                show mt smile panama pioneer with dspr
                mt "Cut that flatter! Finish the food and go make yourself useful for your Motherland!"
                hide mt with dissolve
                "The squad leader was about to leave, when she suddenly turned back to us."
                show mt normal panama pioneer at fright with dissolve
                mt "Take someone to help you."
                mt "It's more fun to work in a team, and you need to be supervised!"
                show un sad pioneer
                hide mt
                with dissolve
                th "Well, thanks for your confidence!"
                "I finished the soup and pulled the cooled second dish toward me."
                "Lena looked a little confused."
                un "It's strange that she didn't ask me for help."
                "Really weird."
                "Apparently, our squad leader had a special fad «spoil Semyon's life», which always forced her to dump any assignments to me."
                "Although if Lena was so eager to work, I could call her as a partner."
                th "Or is it still not worth it?"
                th "I was planning to stay away from her, in order to not unnerve her."
                th "And now what, I hope to dump the squad leader's assignment to a girl? I will not add reputation points for myself by doing this."
                me "Maybe she doesn't want to distract you from your newspaper work?"
                show un normal pioneer with dspr
                un "Hardly. I'm done with the drawings, but otherwise I'm of little use."
                me "Then you definitely deserve a rest! You spent the whole morning in the infirmary, didn't you forget?"
                show un shy pioneer with dspr
                "Lena was confused."
                un "Yes, not all morning of course, but a couple of hours before lunch. And then for all this time there was only one visitor."
                "An amazing, however, coincidence - Random sent me my ridiculous wound at the very moment when Lena was on duty at the infirmary."
                "I've never been a fatalist, but there was definitely something funny about these twists of fate."
                show un smile pioneer with dspr
                "Lena finished her compote and got up from the table."
                un "Think I'll go."
                me "Yeah."
                show un normal pioneer with dspr
                hide un with dissolve
                "I actively started grinding with my jaws. Didn't want to get a scolding from Olga Dmitrievna for eating too long."
                $ counter_un_fz = 2
                stop music fadeout 2
                stop ambience fadeout 2
                with fade
                return
        "Sit with Slavya":
            call alt_day3_lp_checker(alt_dater = sl)
            play music music_7dl["yume_akari"] fadein 5
            if (counter_sl_cl == 3) and (alt_day2_date == 'sl'):
                "It might seem incredible, but - Slavya has become even prettier compared to what she was at breakfast."
                "She seemed to absorb the sun of the beach, the freshness of the water and the admiring attention of those who looked at her."
                show sl smile pioneer at center with dissolve
                sl "Beach is incredible! It's a pity though that there are a lot of people right now."
                sl "Well, how do you like the morning match?"
                "I shrugged."
                me "A match is a match - I killed time, and that's okay."
                show sl smile pioneer with dspr
                sl "That's good! At least you basked a little - look how pale you are."
                me "It's aristocratic pallor."
                show sl laugh pioneer with dspr
                sl "A little tan wouldn't hurt!"
                sl "You look like you came here straight out of winter!"
                "That was a critical hit..."
                me "Anyway, I'm not going out in the sun again today - I'm afraid I'll peel off."
                sl "Listen, maybe then..."
                me "What?"
                dreamgirl "Wait for it, wait for it, wait for it..."
                dreamgirl "New quest in three... two..."
                sl "I have to deal with garlands for the dances."
                "I nodded slowly."
                sl "Well, in the meantime, I need to be on duty in the boss's office - answer phone calls, sort photos into albums, and so on."
                show sl shy pioneer with dspr
                sl "Do you want to come with me?"
                "I shrugged."
                if alt_day3_duty:
                    me "If you insist. {w}Catch me at the administration building in half an hour, I need to finish cleaning first."
                else:
                    me "Sure. You can go now, I'll catch up later."
                "Slavya nodded, got up and left."
                hide sl with dissolve
                $ counter_sl_cl = 4
            else:
                "Looks like there's a free spot near Slavya."
                "Which I hastened to take."
                show sl smile pioneer with dissolve
                sl "Hi, Semyon!"
                me "Ahem… Yes. Hello."
                me "Bon appetit."
                "Her enthusiasm was discouraging. She almost jumped with delight because a whole Semyon sat next to her?"
                show sl normal pioneer with dspr
                sl "Did something happen?"
                "She extinguished her smile, and the room suddenly became exactly twice as dark."
                me "No... I just can't get used to your cheerfulness."
                if loki:
                    me "You're all shining like the sun. If I knew a suitable candidate, I would say that you fell in love."
                    show sl dont like pioneer with dspr
                    sl "Come on!"
                    "She snorted and pretended to pout. Not for long, though."
                    show sl smile pioneer with dspr
                    "Even a couple of minutes couldn't pass, and here she is smiling again."
                else:
                    me "Some kind of inexplicable, I'd say."
                    sl "What is inexplicable here? We have this camp, this sun, beautiful weather and good people around."
                    sl "Even you, despite the fact that you are pretending to be a boo."
                    "I almost choked on my soup."
                    me "You think I'm a good person?"
                    "Here she managed to surprise me."
                    show sl smile2 pioneer with dspr
                    sl "Of course! You never refuse to help, even though you frown so funny when someone approaches you."
                    "And what now? I explain to her that it's easier for me to do as they want me to, so that they left  me alone faster?"
                    "Okay, let it be in the power of delusions. Moreover, these delusions are the sweetest."
                sl "What are you going to do after dinner?"
                me "As usual, a fervent rotation from the left side to the right."
                me "And if I get tired, I'll sleep."
                sl "Can you help us to organize the disco?"
                show sl smile pioneer with dspr
                sl "We need to deliver equipment and records to the square. Can you help?"
                $ alt_day3_sl_invite = True
                me "Why not. Just remind me after the lunch."
                show sl laugh pioneer with dspr
                "She laughed and nodded as she stood up from the table."
                hide sl with dissolve
            return
        "Sit with Miku" if (alt_day2_mi_date != 2):
            show mi happy pioneer with dissolve
            call alt_day3_lp_checker(alt_dater = mi)
            if alt_day3_date == 'mi':
                play music music_7dl["what_am_i_doing_here"] fadein 3
                mi "Senechka, I saved a seat for you!"
                "With all the enthusiasm of a young Japanese emancipe, she waved her arms and showed concern for her chosen one..."
                "For me."
                "She seems to have come to terms with the gossips creeping around the camp."
                "And I, it seems, will have to get used to the fact that she call me «Syoma», «Senechka» and the devil knows how else."
                th "As if I care about random pioneers opinions."
                me "Have a nice one!"
                mi "Thanks!"
                show mi smile pioneer with dspr
                "She blurted out and we both smiled."
                me "Are you aware of today's dances?"
                mi "Yes! I was at the last disco, I danced a little. But they play strange music there, it's not very convenient to dance to it."
                "Well, yes, yes, this is not 180 BPM, under which the sleeves floating in the air look so trump."
                me "I have to confess to you..."
                "I leaned closer and lowered my voice with a conspiratorial air."
                me "I cannot dance. By «cannot» I mean «at all»."
                me "Maybe you could teach me a bit..."
                mi "You want me to give you a dance lesson?"
                show mi laugh pioneer with dspr
                "She burst out laughing, and I, frowning, moved away."
                "She is laughing at me again!"
                me "If you don't want to, just say so."
                show mi surprise pioneer with dspr
                mi "Senya, what's wrong? {w}Senya? Are you offended? Don't be offended, you know yourself, sometimes I don't understand what I'm talking about."
                mi "Give me a discount on this. I just thought you wouldn't ask."
                me "So you agree?"
                "The smile returned to the face."
                me "I mean, will you teach me how and where to put my legs and all that?"
                show mi shy pioneer with dspr
                mi "Of course! You have to dance with me tonight."
                "Actually, I was hoping to make it a surprise!"
                "Though, if I'm not mistaken, there should be white dances, and then my surprise is seriously threatened."
                me "Actually... Yes! I wouldn't want to act like an elephant and trample your feet."
                "She laughed."
                me "And again, why are you laughing?"
                mi "Just don't start pouting again, I'm not evil, I just imagined you trampling on my feet."
                th "I'm asking her for help and she's having fun."
                th "One day her «imaginations» will become bitter reality."
                show mi normal pioneer with dspr
                me "So…"
                mi "Yes! Yes-yes-yes! Come to the club after dinner, I'll look for suitable music."
                me "Suitable?"
                mi "I have a whole rotation for dancing, I need to look for something slower."
                me "Okay, so we've agreed."
                "With all the chatter, I completely forgot about lunch. It's already cold."
                "Sighing, I grabbed the spoon."
                $ counter_mi_7dl = 1
            else:
                play music music_list["so_good_to_be_careless"] fadein 3
                me "Can I?"
                show mi normal pioneer with dspr
                "She looked at me strangely and nodded."
                th "I don't seem to be very welcome here."
                "We ate in silence for a while."
                mi "Semyon."
                "I almost choked."
                "Machine gun girl decided to save ammo and land single shots?"
                "I looked up from my plate. Miku patiently waited for my answer."
                me "Yes. What's the matter?"
                mi "The disco is today, you remember?"
                if alt_day2_bf == 'sl':
                    me "Ye, Slavya told me about something like this yesterday..."
                else:
                    me "Heard something like that on the lineup, yeah."
                me "What's the matter?"
                mi "Will you go?"
                menu:
                    "Why not":
                        $ karma += 10
                        me "I don't mind dancing."
                        me "Even if I don't dance, I'll at least listen to music."
                        me "But I suppose you're interested for another reason."
                        show mi shy pioneer with dspr
                        mi "Actually, yes. I want to invite you."
                        "I nearly choked on my soup again."
                        me "What... uh... uhm... this is very... unexpected!"
                        "Who would have thought that she would ever pay attention to me!"
                        "Although... If you remember what's going on in her music club..."
                        me "Okay. I don't mind. Only problem is that I don't have fancy clothes..."
                        dreamgirl "Nor the ability to dance. Everything else, in general, is there, yes."
                        th "Shut up."
                        mi "That's okay, we'll get you something from the stage wardrobe!"
                        mi "Looks like there were some decent shirts and pants. You won't go dancing naked, I can promise you that."
                        "That's right... Now she'll invite me to her place, and tomorrow we'll be hearing gossips from all around the corner. Not that I care."
                        if (alt_day2_date == 'un') or (alt_day2_date == 'un_fz'):
                            "The only thing that Lena can get something wrong."
                        elif (alt_day2_date == 'sl'):
                            "Slavya will understand. I promised her a dance, Think it will be more pleasant for her to dance with a handsome boy."
                        elif (alt_day2_date == 'dv'):
                            "The main thing is not to draw Dvachevskaya's attention, she will eat me alive for such tricks."
                        else:
                            "After all, it's a pretty good excuse to… ahem… get close, huh? Or what do alphas of all stripes call it?"
                        me "Okay, agreed. Where should I go and what should I do?"
                        mi "Come to my club after dinner, we'll see there. At the same time, we can also improve your dancing skills."
                        "I blushed to the very ears and diligently nodded, masking embarrassment."
                        $ counter_mi_7dl = 1
                    "I can't":
                        $ karma += 5
                        me "Yeah, you know. I don't seem to mind. But..."
                        "My voice dropped to a whisper."
                        me "I can't dance."
                        show mi surprise pioneer with dspr
                        mi "You don't know how at all?!"
                        "She looked shocked to say the least."
                        "It's understandable. In the current situation, in the Soviet Union, dancing was one of the necessary links between the sexes. {w} No dancing - no courtship - no relationship."
                        "And what should I tell her? That the apotheosis of my choreography is antics under the progressive house and melancholy trampling under the «Slowyes»?"
                        "Well, I had some stage choreography skills, but I didn’t want to use them here at all - firstly, there was no confidence in this body and its reflexes, and secondly ..."
                        "Let's say I didn't want to feel like an idiot. I've been doing this way too often lately."
                        me "I'm not completely hopeless. Just that i've been taugh other kind of dances."
                        mi "That's okay. I'll teach you!"
                        me "You?! How?!"
                        show mi smile pioneer with dspr
                        mi "Well, I'm an art director after all."
                        "She smiled mischievously."
                        mi "We'll think of something."
                        mi "And dress you up as well."
                        "Why does it seem to me that she feels much more enthusiastic about future choreography lessons than your humble servant?"
                        me "Since you say so..."
                        mi "It's decided! Come to the music club after dinner, we'll see what you can do."
                        $ counter_mi_7dl = 1
                    "Don't want to":
                        $ lp_mi -= 1
                        $ karma -= 10
                        $ alt_day3_mi_rejected = True
                        me "I'm sorry, but no."
                        me "I don't feel like grimacing in the square to some weird music, or watching a few dozen idiots like that."
                        show mi angry pioneer with dspr
                        mi "What are you talking about, Semyon?!"
                        "She seems to be angry."
                        mi "Dancing is an opportunity to communicate without words, to relax and have a good time."
                        mi "Have we offended you in some way? Where does this aggression come from?"
                        me "No aggression. Just not a fan of that sort of thing."
                        me "Plus I don't really like feeling like a jerk waving my arms."
                        me "I'm sorry."
                        "I didn't want to be rude, to be honest."
                        "I even wanted to apology already."
                        "But we've been interrupted unexpectedly."
            show sl normal pioneer at right with dissolve
            show mi normal pioneer with dspr
            sl "Guys, sorry, do you mind?"
            "Slavya stopped next to the table."
            if not alt_day3_mi_rejected:
                mi "Hi, Slavichka, are you aware of today's dances?"
                "Miku chirped instantly."
                mi "I'm choosing a good suit for Senechka, it will be beautiful, beautiful!"
                show sl smile pioneer with dspr
                sl "I'll definitely check it out!"
                "The girl smiled coquettishly."
            sl "Are you busy right now?"
            mi "No, I was going to go home to change clothes and take a dip once since I hadn't time for this in the morning!"
            sl "Swimming? Good, good... And you, Semyon?"
            "I shrugged."
            me "No specific plans. What do you want?"
            sl "Me? Ah..."
            "The activist thought for a while, and then, apparently deciding that we could be trusted with important information, she brought it to our attention:"
            sl "I'm talking about today's dance - I need a couple of volunteers for loading-unloading operations."
            sl "And, Miku, no! You can't even this time!"
            show mi upset pioneer with dspr
            mi "Blah-blah-blah."
            "She rolled her eyes to the bridge of her nose."
            mi "Don't do this, don't do that. And you don't even have authority on me!"
            show sl smile2 pioneer with dspr
            sl "Okay, Miku."
            "Slavya smiled."
            "It seems that this was not the first time this squabbling took place and it was a real pleasure for both sides."
            sl "I promise I'll save the biggest and heaviest thing for you personally."
            sl "But for now, you'd better go to the club after you swim, and take care of the program for the evening."
            show sl normal pioneer with dspr
            sl "And I'll take Semyon - if no one minds."
            me "Not that I mind but..."
            "I answered evasively."
            mi "I don't mind, of course! In the meantime, I'll figure out the music for today's disco."
            if alt_day3_mi_rejected:
                me "I can help, just tell me where to go and what to do."
                sl "Very well! {w}Let's start from the stage, where we will have to deal with the equipment, and then according to the circumstances."
                sl "Are you sure you're coming?"
                me "I'll try, at least."
                "It seems that Miku was not at all hurt by my behavior - but now I myself was already terribly uncomfortable being next to the person whom I had just been rude to."
            else:
                me "Maybe I want to take a dip too..."
                show mi shy pioneer with dspr
                mi "So let's go. Its not urgent right?"
                "Slavya nodded in agreement."
                sl "There's still a plenty of time, but I would like us to finish by six o'clock - I have a tiny business for that time..."
                "I nodded in agreement - it seems that they refuse to get off my neck, it's easier to agree than to explain why not for half an hour."
            hide sl with dissolve
            "Slavya nodded and ran out of the canteen, finally allowing me to finish my completely cold soup."
            show mi serious pioneer with dspr
            mi "Don't even think about how to escape!"
            if ('music' in list_clubs_7dl) and (alt_day3_date not in ('dv', 'mi')):
                mi "And moreover..."
                mi "Why didn't you come to the club in the morning?"
                me "Yeah, you know..."
                mi "Nevermind, just don't forget the main thing this time!"
            "Miku said sternly, guessing my thoughts without any problem."
            mi "We need to help! The site will not prepare itself."
            "Fairly considering that it's up to me to decide, I stopped the argument."
            return
        "Sit alone":
            if alt_day3_duty:
                scene
                $ renpy.show("bg int_dining_hall_people_day", what = Noir("bg int_dining_hall_people_day"))
                with dissolve
                th "I don't seem to have made much progress in terms of socialization relative to where I was taken from."
                "However, in silence one eats tastier and sleeps sweeter."
                "In a matter of minutes, I swept up what was offered to me and, lay in wait for Ulyanka - this time she was going to sneak away for sure!"
                "She went out so stealthily ..."
                "That's probably why my question, put right in front of her ear, scared her."
                me "Where are we going, I wonder?"
                show us smile sport
                us "And I… I got my hands dirty! And I was going to wash them."
                me "You can wash them in the bucket."
                "I remained adamant."
                me "First clean the floor, then all the nonsense."
                show us sad sport
                us "Uooohhh."
                "Only she sighed and, with all her appearance depicting unearthly suffering, returned back to the canteen."
            else:
                scene
                $ renpy.show("bg int_dining_hall_people_day", at_list = [zentercenter], what = Noir("bg int_dining_hall_people_day", brightness = -0.4, saturation = -0.4))
                "Everything that happens in the camp - it remains behind the doors of this institution."
                "I come, take a plate and sit down - and for several minutes I seem to not exist in this reality."
                "At home, I usually ran to smoke if I wanted to take a break in conversation, work, life. Just turn off my head and stand in silence, slowly pitching some alien «Winston»."
                "Here I have neither the opportunity nor the desire to smoke: it seems that the body I got was completely unfamiliar with nicotine, so there was no physiological withdrawal."
                "And about psychological... you can suppres it with food."
                "Lunch flew into the bowels of my stomach with a whistle, leaving no trace. It seems that I did not eat enough, I had to stand for the addition."
                "In any case, I calmed down, relaxed and rested."
                "That's it! Eat, now you can return to socially useful activities."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_eventAf_clubs_technoquest:
    $ alt_day3_technoquest0 = True
    scene bg ext_clubs_day with fade
    play ambience ambience_camp_center_day fadein 1
    play music music_list["i_want_to_play"] fadein 3
    "The door was wide open and voices were coming from inside."
    "Voices arguing, and, moreover, extremely recklessly."
    "I listened and in one of the voices, without surprise, I recognized Shurik - this frame is still a brawler when the question concerns his club."
    "It was logical to expect a second debater - only Slavya constantly encroaches either on the square or on some other resources single-handedly grabbed by cybernetics."
    sh "I repeat once again, until we clean up this unfortunate closet, there will be no radio in sight!"
    stop ambience fadeout 2
    play sound sfx_open_door_clubs
    pause(1)
    scene bg int_clubs_male_day
    with dissolve
    play ambience ambience_clubs_inside_day fadein 3
    show sh rage pioneer at left
    show sl angry pioneer at right
    sl "So clean it up!"
    sh "Yeah, but who will work in the wall newspaper? Ulyana or this retarded newcomer?"
    "Then he noticed me and immediately backed away, mumbling something like: «Damn newcomers»..."
    "It seems that he was not afraid to get hit into his tambourine."
    "Or he hasn't been beaten in a very long time."
    me "Shurik."
    if herc:
        "In a penetrating voice I began."
        me "Have you ever had your nose broken?"
        show sh scared pioneer at left with dissolve
        "He backed even more actively, and in his eyes flashed a belated realization of what he had just done."
        me "So, my dear stupid friend - as you can see, I'm not ashamed to tell you this right to your face. After all, you did the same thing."
        me "We have freedom of speech here, don't we?"
        me "If I find out again that you are talking about me or anyone else in the same derogatory tone — but behind their back! — I solemnly promise you that I will break your nose."
        show sl scared pioneer at right with dissolve
        sl "Semyon, what are you talking about?! Why are you intimidating your friends?"
        me "Not a single intention!"
        "I yawned long and sweetly."
        me "Just made a gentlemen's agreement between a friend and a friend."
        sl "That's what you call it?"
        me "How could it be otherwise? We are all here for the truth! And those who are not for the truth will get something in their face."
    else:
        "I raised an eyebrow questioningly."
        me "I don't think I did anything bad to you personally. {w}How did I deserve such marks?"
        sh "You see?"
        "He snorted and gritted his teeth."
        th "From the very beginning it was necessary to put yourself. Whoever opens his mouth - in his tambourine."
        "True, I have not been able to play a «tambourine» for a very long time ..."
    me "Why are you arguing here?"
    show sl angry pioneer at right
    sl "You see, those... cybernetics... theorists! Are not able to do the simplest thing they've been asked to do."
    me "What's a simple thing?"
    sl "There was a big storm here two days before you arrival, and it looks like a branch damaged the antenna. We need to fix it."
    me "I'm no help here. Sorry."
    sh "Actually, you could be useful."
    show sh serious pioneer at left
    me "Tell me more."
    sh "First, you need to get some tools from the stockroom and see which ones might come in handy."
    show sl laugh pioneer at right
    sl "And clean up there at the same time!"
    sh "We can tidy up there ourselves, the only slight problem is to drag heavy things from there."
    me "Such as…"
    sh "Well, for example, a video deuce, a computer and an aquarium."
    "Listed Shurik."
    sh "Electronik and I tried together, but it didn't work."
    sh "Maybe you can do it."
    sh "Well?"
    menu:
        "Easy!":
            $ karma += 10
            $ alt_day3_technoquest1 = 1
            scene bg int_clubs_male2_night with dissolve
            if herc:
                "I don’t understand what was difficult for our cybenematics to pull out, but I alone coped with each of the aforementioned items, unloading them in an artistic pile on the table between the oscilloscope and jars of vitriol."
            else:
                "I had to sweat for sure, in some cases I even had to involve Shurik with Electronics. However, as a result, I managed and even earned a whole mug of cold fruit drink."
                "And where did they get it, I wonder?"
            "Cleaning didn't take long - most of the rubbish was sorted out in less than half an hour."
            "I frankly did not understand why they did not do the same thing themselves - they would have done it three hundred times already."
            "And then I remembered my own bachelor lair…"
            scene bg int_clubs_male_day
            hide sh
            show sl smile pioneer
            with dissolve
            sl "Semyon, thank you! You've helped me out again!"
            "I, not accustomed to praise, was embarrassed, looking at the floor."
            me "Nonsense. Nothing complicated."
            sl "That's nothing to you."
            sl "And for those fools..."
            "She cast a disapproving look at the ashamed cyberneticians."
            sl "Even turned out to be too much."
            "I nodded and left the clubhouse."
            "I did the hardest part, I hope they can do everything else themselves."
        "No":
            "As if I have nothing else to do, other than to help some random cybernetics."
            "I shook my head and left the clubs."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_eventAf_clubs_ladder:
    scene bg ext_clubs_day with fade
    play ambience ambience_camp_center_day fadein 1
    play music music_list["i_want_to_play"] fadein 3
    if alt_day3_technoquest1 == 0:
        th "And what am I doing here?.."
        with fade
        return
    "I have been here before, of course, but it will not be superfluous to chek again."
    play sound sfx_open_door_clubs
    pause(1)
    scene bg int_clubs_male_day
    with dissolve
    play ambience ambience_clubs_inside_day fadein 0
    show el smile pioneer
    el "Ah, it's you again."
    el "Have you come to help again?"
    "I nodded."
    $ karma += 10
    el "Excellent! The next thing we need is to get a ladder to replace our old one - it's already completely broken."
    el "You can ask a gym teacher for a stepladder, but he is reluctant to communicate with those who are not enrolled in sports clubs."
    el "Or you can borrow a wooden ladder from Olga Dmitrievna. The ladder is stored in the house next to you."
    $ alt_day3_technoquest1 = 2
    el "Who will you go to?"
    if herc:
        me "To gym teacher."
        scene bg ext_playground_day with fade
        play ambience ambience_soccer_play_background fadein 2
        play music music_list["went_fishing_caught_a_girl"] fadein 2
        "On the football field, as usual, someone was chasing a ball, the gym teacher himself was here too."
        "Plucking up the courage, I approached."
        me "Er… Hello. {w}May…"
        ba "May."
        "Without turning in my direction, he replied."
        ba "Sit."
        me "No, I..."
        show ba em1 uniform with dissolve
        "Finally, he honored me with his attention."
        ba "Ah, it's you. Why?"
        me "Rumors tell that you have a ladder."
        ba "Indeed. But who told you that I'll give it to you?"
        if ('soccer' in list_clubs_7dl) or ('volley' in list_clubs_7dl) or ('badmin' in list_clubs_7dl):
            me "Hello, please! Are you refusing to help your own pupils?"
            "He took his eyes off the game and stared at the bridge of my nose for a few seconds."
            ba "Ah, yesterday's skinny. I remember."
            ba "Why are you not on the field?"
            me "So I'm... Um... fixing the radio. I need a ladder. To make running more fun."
            ba "Radio, you say?"
            "He thought about it and nodded."
            ba "It's important, ye. Okay, here's the key for you, give it to your squad leader later, she'll report to me."
            ba "Climb into the indoor area, just behind the doors on the right. And watch out for the makiwara."
            "He winked and lost interest in me."
            "Indeed, there were no difficulties, I took the weightless aluminum stepladder and took it to the cyberneticists, having received all the possible «praises» and offers to run in for a glass of tea."
            return
        else:
            "Cunning fat man. He thinks that now he has caught me, and I will enroll in his almshouse."
            "With a soft sign."
            me "Camp leader?"
            ba "Pass. Try again."
            me "Olga Dmitrievna!"
            show ba smile uniform with dspr
            ba "Olka?"
            "He laughed heartily."
            ba "Of course she can tell me. And I might even listen to her. But you're not even close to those topics, pioneer."
            show ba evil uniform with dspr
            ba "Get out of here and don't waste both of our time."
            "I stood as if drenched in slop."
            th "This walking pile of fat just mixed me with shit, just because he wanted so."
            "The teaching staff here, of course, shines."
            "The only question now is what to do."
            "It seems I have no choice. I'll have to bow to Olga Dmitrievna."
            "I turned around and wandered away from the sports ground, feeling Boris's mocking look with my whole back."
    else:
        me "To squad leader."
    scene bg ext_house_of_mt_day
    with dissolve
    play music music_list["smooth_machine"] fadein 5
    pause(1)
    play sound sfx_knock_door7_polite
    pause(1)
    mt "Come in!"
    play sound sfx_open_door_clubs
    pause(1)
    scene bg int_house_of_mt_day
    show mt normal pioneer far at center
    with dissolve
    "Hearing my request, she just nodded and handed me the key:"
    mt "It's really heavy. Can you handle it?"
    "I shrugged."
    me "I'll have to try!"
    me "Thank you!"
    "I hurried to leave the house until the squad leader remembered that it was, in fact, a sleepin hour!"
    scene bg ext_houses_day with dissolve
    "The ladder really turned out to be in a house next door."
    "She lay between the beds and intimidated me with her appearance alone!"
    "I mean, no matter what they made it for, they made it ten times more durable than it should be!"
    "Even though it looked heavy, it turned out to be three times heavier!"
    "I grunted and with one movement pulled this solid structure into the light of day."
    "The most difficult thing is done, and to drag it away is an easy task for any weakling."
    "Which, by the way, I no longer felt like - still, to cope with such a thing!"
    "Then it was all a matter of time - for more than half an hour, puffing and drenched in sweat, I dragged this damn cow around the camp."
    "And as a result, was rewarded with a glass of ice-cold cranberry juice!"
    "And where did they get it?"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_eventAf_music_club1:
    scene bg ext_musclub_day with fade
    play ambience ambience_camp_center_day fadein 1
    if counter_dv_7dl == 2:
        call alt_day3_day_dv
    else:
        "Looks like something's going on here..."
        "Anyway, don't want to get in the way."
        "I turned around and, trying to step silently, retired."
        "I definitely don't want to volunteer at some local session."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_day_un_fz:
    scene bg ext_dining_hall_near_day with dissolve
    play ambience ambience_camp_center_day fadein 2
    play music music_list["so_good_to_be_careless"] fadein 2
    "I went out onto the porch and stretched."
    "After dinner, there was no desire to work, but shirking in a house where an angry squad leader could suddenly appear at any moment was not a good idea."
    "Yes, and I was ashamed, to be honest. When your entire squad is working hard, rest is unlikely to bring joy."
    "I looked around."
    "The younger pioneers, worn out by the sun and food, crawled along the paths towards the houses."
    "Leaning on the railing, I figured out who to bring to work in my modest company."
    menu:
        "Bring Lena":
            $ alt_day3_un_fz_work = 'un'
            $ counter_un_fz_un_route += 1
            $ lp_un += 1
        "Bring Slavya" if (alt_day2_convoy == 'sl'):
            $ alt_day3_un_fz_work = 'sl'
        "Bring Alisa" if (alt_day2_convoy == 'dv'):
            $ counter_un_fz_dv_fake_date += 1
            $ alt_day3_un_fz_work = 'dv'
            $ counter_un_fz_old_road += 1
            $ lp_un -= 1
            $ lp_dv += 1
    return

label alt_day3_day_un_fz_un:
    scene bg ext_dining_hall_near_day with dissolve
    "Lena was free for sure."
    "If I understood correctly, she didn’t like laying around doing nothing, so it was still worth taking the risk and calling her."
    "After all, I wanted to make sure she didn't hold any frivolous grudges against me."
    "Yes, and it was difficult to communicate with her, but, somehow, insanely interesting."
    "The ever sad artist girl looked like a riddle that I really want to solve."
    "There was something exciting about her that kept me from just passing by every time I saw her."
    "I wanted to talk to her, I wanted to see that she is not afraid of me."
    th "But who am I to get at her? Why would I want to pull her out of her shell?"
    "I couldn't honestly answer that question for myself."
    "Perhaps the whole point was that I saw myself in her - the same lonely and withdrawn person, whose closet is already bursting with countless skeletons. A dam that is about to burst."
    "How many times have I dreamed that there was at least someone who could understand me?"
    "I did not demand love for myself, no - such as I am not destined to find it."
    "But I needed a friend, a true friend who could handle any outburst."
    "Who will not turn away in disgust when soul abscesses open up and ooze with fetid, rotten thoughts, consisting only of bitterness and resentment."
    "And I felt needed by Lena. Even if she doesn't fully realize it."
    scene bg ext_library_day with dissolve
    "I hesitated near the library."
    "I didn’t have much confidence that Lena was here, and I didn’t really want to meet the buzzkill."
    play sound sfx_open_door_1
    "I was about to turn around towards her house when the library's heavy door creaked."
    show un normal pioneer with dissolve
    "Lena."
    show un sad pioneer with dspr
    un "What are you doing here?"
    "She cringed, as if frightened by her own question."
    me "I'm looking for you."
    show un shy pioneer with dspr
    un "Why?"
    me "What do you mean why? And who will bring benefit to the Motherland?"
    show un sad pioneer with dspr
    "Lena's face for a moment took on such a disappointed expression that I wanted to reduce everything to a joke and leave."
    "Apparently, I overestimated her industriousness, and in a quiet hour she was going to indulge in Morpheus, and not run with a broom around the square."
    show un normal pioneer with dspr
    un "We need to help, true.{w} Let's go to the square then?"
    "I nodded and we silently walked down the shady path."
    scene bg ext_houses_day
    show un normal pioneer
    with dissolve
    "I felt ashamed again."
    "From the outside, I probably looked like an excessively obsessive boyfriend."
    "At the same time, a suitor who simultaneously flies after half of the camp, just in case nothing works off here."
    "But I didn't dare to talk about it."
    "You never know, maybe I just imagining things, and Lena has completely different thoughts on this matter. I'll only make a fool of myself."
    me "Actually, if you wanted to take a break, you don't have to hang around with me."
    me "I don't think there's too much hard work ahead of me that I can't do it myself."
    un "If you're against my company..."
    th "How the hell did you come up with that idea?"
    me "Lena, I called you myself!"
    show un shy pioneer with dspr
    hide un with dissolve
    "She turned away from me."
    me "I just suddenly thought that they didn’t bring you on purpose. Because you are already overworked."
    show un smile pioneer with dissolve
    un "Well I wouldn't say that I am overworked."
    un "On the contrary, I often do not know where to put myself. And so at least there will be some work."
    scene bg ext_square_day
    show un normal pioneer with dissolve
    "We've come to the square."
    "Cyberneticists were dragging a heavy speaker, drenched in sweat, and Slavya led the process."
    "Judging by how tensely she held her hands, she was ready at any moment to pick up the speaker in case the future luminaries of Soviet science dropped it."
    th "Slavya-Terminator? Something new!"
    "However, as soon as she noticed us, the activist gave some command something to the guys and went to meet us."
    show sl normal pioneer at right with dissolve
    sl "Are you here to help?"
    "We nodded."
    show sl smile pioneer at right with dspr
    sl "That's wonderful! Take the garlands, then take the ladder from the warehouse and bring it here."
    sl "Lena, do you have any idea where the box with the garlands is?"
    un "Same place where it was last time?"
    sl "Exactly. Then I guess you shouldn't have any trouble."
    hide sl with dissolve
    "Slavya approached the broom lying near the monument."
    hide un
    show sh upset pioneer far at left
    show el sad pioneer far at right
    with dissolve
    "Cybernetics, meanwhile, installed a speaker and, with not the most happy faces, dragged themselves somewhere towards the stage."
    hide el
    hide sh
    with dissolve
    th "Obviously, in order to bring another speaker."
    dreamgirl "Elementary, my dear Watson!"
    scene bg ext_dining_hall_backroad_day_7dl
    show un normal pioneer
    with dissolve
    "Lena and I went to the warehouse."
    "Through all the way, she was silent, again convincing me that it would be better for me to go on this task alone."
    scene bg ext_warehouse2_day_7dl with dissolve
    "Lena opened the door, letting me in."
    "She herself hesitated, adjusting the clasp on her sandals."
    scene bg int_warehouse2_day_7dl with dissolve
    $ volume(0.3, 'ambience')
    "I looked around for the ladder."
    "There were some boxes in front of it, and I looked inside one of them.{w}It contained Christmas decorations."
    "I pushed it aside, clearing the way to the ladder."
    stop music fadeout 4
    play sound sfx_cellar_open
    "Lena, meanwhile, went inside, closing the door behind her with a bang."
    un "Ouch!"
    show un shocked pioneer with dissolve
    "I quickly turned to her."
    "Because of this move, the wound on my leg reminded of itself, and I grimaced."
    me "Got hit?"
    show un sad pioneer with dspr
    un "No, I just... accidentally closed the door."
    me "What?"
    un "It's locked now!"
    "Lena's voice trembled."
    un "The latch fell. You can’t close it so abruptly, but I ..."
    "It seems like she can start panicking any second now."
    hide un with dissolve
    play sound sfx_campus_door_rattle
    "I went to the door and tried to push it."
    "The door didn't budge as expected."
    play sound sfx_campus_door_rattle
    "I pushed harder."
    un "If you break it we'll get scolded very hard!"
    "Judging by the voice, Lena was on the verge of bursting into tears."
    "Because of some stupid closed door?"
    th "Or because she was locked in the same room with an unpleasant idiot?"
    play music music_list["confession_oboe"] fadein 4
    th "Well..."
    "I congratulated myself."
    th "... wanted to talk to a girl - here's your chance."
    th "Now you can even drag her soul into the light with tongs - she won’t run away anywhere."
    show un sad pioneer with dissolve
    un "I fear confined spaces..."
    "She whispered quietly."
    "I took a cautious step towards her."
    me "Don't worry, we'll think of something. And Slavya knows that we are here. She will get us out."
    hide un
    show un_grasp_7dl
    with vpunch
    "And then Lena, bursting into tears, threw herself on my neck."
    "I was taken aback - such a turn was so out of my picture of the world that had developed in recent days that I had no idea how to react to it."
    un "I'm scared... I'm so scared!"
    "I clumsily stroked the girl's head, not daring to hug her back."
    me "There's nothing to be afraid of.{w} I'm with you."
    th "Though maybe that's what scares her."
    dreamgirl "Of course, she jumped on you because she is scared of you!"
    "Lena continued to sob."
    "In the meantime, I was thinking about ways to get out of the trap in which we found ourselves."
    un "If only you knew how scared I am to be locked up like this, with no way out. Its almost like it's getting hard for me to breathe!"
    me "It's claustrophobia. I'll open the window now - and we'll get out."
    stop music fadeout 6
    hide un_grasp_7dl
    show un cry pioneer
    with dissolve
    "I gently pulled away from Lena and planted her on the old mats piled in the corner."
    "I, myself, went to the only window opposite the door."
    un "Because when you can't leave your cage, you're completely helpless."
    play music music_7dl["lunar_anguish"] fadein 4
    un "You can hit the walls, knock on the door, yell until you're hoarse - the locks outside won't fall."
    th "She was often punished by being locked in a room? Why such gloomy thoughts?"
    "The piles of rubbish under the window were catastrophic."
    "Full of thoughts about what eternal torments should suffer one who was in charge of this warehouse, I began to move the boxes and bags to the side, trying not to break anything."
    un "It seems that there are possibilities outside of this cage that you didn't know existed before."
    un "And now you're ready to give everything for them - arm, leg, heart - just to escape!"
    "I finally got to the window."
    un "And you also know that there, outside the walls, there is life that flows calmly and without you, as if you are such an insignificant grain of sand for the Universe that you play absolutely no role."
    un "And you start to wonder if it's even worth taking a place in this life if you don't mean anything to it?"
    "Three coats of paint over the shutters made it doubtful that this window had been opened at least once in the last few years."
    un "That's why I'm afraid of being locked up. And I'm also afraid of not making the most of my opportunities when I'm free."
    "The dusty window handle, lying on the windowsill, did not want to attach itself properly."
    show un sad pioneer with dspr
    un "And when I have even a tiny bit of hope, I believe in it with all my heart. I grab every chance like a drowning man grab a straws."
    "To be honest, the meaning of Lena's monologue did not reach me."
    "I knew her and her biography too little to understand what exactly prompted the girl to such despair."
    "I could ask directly, but that would be tantamount to hitting a fragile porcelain service with a sledgehammer."
    "She was in pain, and she poured it out on me, the first person who was in the right place at the right time."
    "And if she did not begin to speak in detail, preferring to go around all the corners that could make the still unhealed wounds bleed, then I did not intend to cling to her with questions."
    me "This will pass. Everything will pass. Take a deep breath and imagine that all this is no longer important."
    show un serious pioneer with dspr
    play sound sfx_body_bump
    with vpunch
    "Lena looked into my eyes so seriously that I involuntarily recoiled back, hitting my back against the massive window sill."
    th "No, I'm definitely a nerd. The girl pours her heart out to me, and I answer her like she's a little schoolgirl whining about a bad grade in geography!"
    me "Just trust me. I don't know why you're the way you are now. I can't put your shoes on and go the way you did before we met."
    me "But any pain recedes sooner or later. Don't force it."
    "Lena's lips quivered."
    show un sad pioneer with dspr
    un "But how can I let it go when the reminder of it..."
    stop music fadeout 2
    "She was interrupted by a shout from outside:"
    show un surprise pioneer with dspr
    sl "Lena! Semyon! Are you in the warehouse?"
    me "Yes! Can you open the door please?"
    play sound sfx_cellar_open
    show sl serious pioneer at fleft with dissolve
    "The latch turned with a creak, and an angry Slavya entered the room."
    show un shocked pioneer with dspr
    "Lena jumped up from the mats, as if stung."
    sl "I thought you fell asleep here!"
    me "Sorry, the door slammed shut. You know, calling for help was pointless."
    me "I tried to open the window, but..."
    show sl normal pioneer at fleft with dspr
    "Slavya softened."
    sl "It won't open. The handle is broken and a piece of it is stuck in the frame."
    "I glanced angrily at the handle, which I still clutched in my palm."
    "There was indeed a noticeable chip at the end of it."
    show sl serious pioneer at fleft with dspr
    sl "Lena, I told you a hundred times - don't slam the door!"
    play sound sfx_campus_door_rattle
    show un sad pioneer with dspr
    sl "The latch has become loose, and Boris Alexandrovich still hasn't found time to fix it."
    "Slavya wanted to add something, but instead she just waved her hand."
    sl "Semyon, take the ladder and let's go. We'll decorate the square after lunch."
    scene bg ext_warehouse2_day_7dl with dissolve
    $ volume(1.0, 'ambience')
    "We left the warehouse."
    "Slavya threw the latch on the door and began fiddling with the padlock."
    show sl normal pioneer with dissolve
    sl "Didn't you take the garland?"
    me "They're not here, no?"
    show sl serious pioneer with dspr
    "Slavya frowned."
    sl "They're in the club building. Didn't Lena tell you?"
    show un shy pioneer at fright with dissolve
    "Lena embarrassedly picked the dusty path with the toe of her sandals."
    un "I thought we'd pick it up on the way back."
    play sound sfx_7dl["pup_bark"]
    show sl normal pioneer at fleft
    show un normal pioneer at center
    with fade
    "As we passed one of the sheds, I stopped and listened."
    me "Is it just me, or is there a dog barking somewhere?"
    "Lena shrugged."
    un "I don't know, I can't hear anything."
    show sl smile pioneer at fleft with dspr
    sl "It's just you."
    "Slavya supported her."
    sl "There are no dogs here."
    scene bg ext_dining_hall_backroad_day_7dl with dissolve
    play music music_list["my_daily_life"] fadein 3
    "Dragging the ladder was extremely inconvenient."
    "I had practically no problems with the control of an unaccustomed body, but the coordination was a little lame, and for several times a day it backfired on me."
    show sl normal pioneer with dissolve
    sl "I will explain everything to Olga Dmitrievna. She won't scold you."
    hide sl with dissolve
    "I realized that Lena and I could look like we were worried about a failed assignment."
    "In fact, we were thinking about something completely different."
    th "I wonder if Lena regrets dumping her worries on me?"
    dreamgirl "Don't you understand?"
    th "What was I supposed to understand?"
    dreamgirl "She locked you in there herself. She stopped at the door for a reason, didn't she?"
    dreamgirl "And obviously for a reason dragged you straight to the warehouse, and not for a garland?"
    th "Some kind of nonsense. And why does she need it?"
    "But the inner voice only giggled in response."
    show un sad pioneer with dissolve
    "I looked at Lena - she walked with her head down, and it was impossible to tell from her that she was pleased with our conversation."
    th "Did she expect me to react differently?"
    scene bg ext_clubs_day with dissolve
    "We had to make a detour through the clubs so that Slavya took the ill-fated garland."
    "In terms of common sense, the route should have been built differently, but who am I to argue?"
    scene bg ext_square_day_party_7dl with dissolve
    "When we dumped our luggage on the square near the monument, Olga Dmitrievna jumped out of nowhere."
    show mt angry panama pioneer at cright with dissolve
    mt "Were you lounging around again?"
    "Her tone didn't bode well."
    show sl normal pioneer at cleft with dissolve
    sl "Olga Dmitrievna, the door to the warehouse slammed shut again. I already told Boris Alexandrovich..."
    mt "Which smart guy slammed it?"
    show un sad pioneer at fleft with dissolve
    "Lena cringed under the leader's icy gaze."
    me "It's me. It just happened by chance."
    "I threw up my hands."
    me "Didn't know about the features of this door. I promise to be careful in the future."
    un "Semyon tried to pull us out."
    "Lena said softly."
    un "But the window didn't open either."
    un "Excuse us, please."
    show mt normal panama pioneer at cright with dspr
    "Olga turned away."
    show sl smile pioneer at cleft with dspr
    mt "Oookay, come along. Lunch is about 5 minutes from now."
    show mt angry panama pioneer at cright with dspr
    mt "But don't be lazy after the lunch! Hang up the garlands and you can go back to your clubs."
    "We nodded and hurried to the canteen until the squad leader came up with another job for us."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_day_un_fz_sl:
    scene bg ext_dining_hall_near_day with dissolve
    "If anyone in this camp knew exactly what to do, it was Slavya."
    "The activist seemed to take on more responsibility than the lazy squad leader."
    "So I went to the square without much thought."
    scene bg ext_square_day with dissolve
    "Slavya to my surprise, I did not find her there."
    scene bg ext_square2_day_7dl
    show mt normal pioneer far
    with dissolve
    "On the other hand, Olga Dmitrievna was sitting on a bench not far from Genda, fanning herself with a Panama hat."
    th "Looking for anyone who wants to hide from party assignments? Well, well."
    th "Yes, Olga, we know your passion for work."
    th "I'll bet all the remaining charge on the smartphone - now she will scold me for idleness, and then she will go to wallow with a book in a sun lounger."
    "The squad leader noticed me."
    mt "Are you looking for Slavya?"
    "Her voice sounded surprisingly calm."
    "She apparently wasn't going to lecture me."
    mt "She is at the stage with Serezha and Sasha. They went to fetch the speakers."
    mt "You can wait here for her. I think the two boys will do just fine."
    th "Wow! Did she just let me lazy around for a bit?"
    show mt normal panama pioneer far with dissolve
    "Olga rose from the bench with a sigh."
    mt "I'm going to check what music they chose for the disco."
    show mt smile panama pioneer far with dspr
    mt "It would be unfortunate if tomorrow someone tell their parents how they wriggled to some obscene songs."
    show mt grin panama pioneer far with dspr
    "Olga giggled."
    mt "But I haven't told you that!"
    mt "It is not pedagogical to share the subtleties of our work with the pioneers."
    hide mt with moveoutright
    "She walked off towards the music club, leaving me confused."
    "I watched her go, thinking that sometimes I act like the rebellious teenager that I now appear to be."
    "I am biased towards the squad leader and her idiotic assignments, I accuse her of laziness, I am angry that she does not meet my expectations."
    "And I completely ignore the fact that she is also a living person."
    "A person who is pressed by responsibility, a person who walks under someone else's direction."
    "Who has almost no power or right to speak, being only one step higher in the hierarchy than me and all other pioneers, and is forced to think and act only on orders from above."
    "But something told me that she thinks completely differently."
    "And that gives her even more trouble than all of us put together."
    scene bg ext_square_day
    show sl normal pioneer far at fright
    show sh upset pioneer far at center
    show el normal pioneer far at left
    with dissolve
    "In the meantime, a procession appeared on the horizon: cyberneticians, who were dragging with difficulty a heavy-looking speaker, and Slavya, coordinating them."
    sl "Be careful, Seryozha! There is the curb behind you!"
    el "Yes, I see!"
    "He turned around, nearly dropping the speaker on his foot."
    show sl sad pioneer far at fright with dspr
    "Slavya sighed."
    "But then she noticed me and nodded, as if saying «wait»."
    hide el
    hide sh
    hide sl
    with dissolve
    "And I sat down on the bench watching the show."
    "The speaker was installed, and sweaty cyberneticians with mournful faces trudged back towards the stage."
    "Slavya went to me."
    show sl normal pioneer with dissolve
    sl "You, I assume, also came to help?"
    me "Anything for the Motherland!"
    "I proudly performed the pioneer salute."
    show sl serious pioneer with dspr
    "The girl frowned."
    sl "Don't joke like that, Semyon. It's not the kind of jokes pioneer should say."
    me "What makes you think I'm joking?"
    show sl laugh pioneer with dspr
    "Slavya laughed."
    sl "Well, I know you! It's not your style - don't argue!"
    me "It's okay for you to grumble. Anyway, any tasks?"
    show sl smile2 pioneer with dspr
    sl "Go to the warehouse and get a ladder to start with."
    sl "Warehouse is oooover there."
    "She waved her hand somewhere in the direction of the canteen."
    if (counter_sl_7dl != 1):
        show sl laugh pioneer with dspr
        sl "You and I ran into each other there on your first day at camp, remember?"
        "The girl laughed."
        me "Yeeah."
    show sl serious pioneer with dspr
    sl "Ladder is in the shed with the number «1» on it. It's open, I have the lock."
    sl "Don't mix them up!"
    "For some reason she added, looking sternly at me."
    show sl normal pioneer with dspr
    th "I wonder what I can find in the rest of the sheds to be so worried about it?"
    dreamgirl "You don't want to know."
    dreamgirl "All who found out are now lay lifeless in those shed."
    th "Tell me another joke, smart guy."
    dreamgirl "Okay. A man bought a hat..."
    th "Okay, just shut up!"
    sl "And I'll help the guys carry the speakers. Otherwise, they'll stumble along the way!"
    sl "And then let's go get the garlands from their club. Don't go alone, or you'll be looking for it there for half a day!"
    th "Those cryptic instructions again: don't go here, don't go there!{w} Is she hiding a meth lab in there?"
    dreamgirl "Put your mop away Slavya..."
    scene bg ext_warehouse2_day_7dl with dissolve
    "Mentally asking my inner interlocutor to go... himself, I went in the direction indicated by Slavya."
    "The ladder turned out to be heavy and extremely inconvenient to transport."
    "I almost broke a window trying to get the damn inventory out of the warehouse."
    th "At least its not speakers. They will obviously be heavier!"
    scene bg ext_square_day_party_7dl with dissolve
    "Slavya was already waiting for me on the square, leaning on a broom near the monument."
    th "That's right, a witch. She'll turn me into a frog and fly away, laughing out loud."
    th "And there is no one to disenchant!"
    th "Some people hate me even in my human form, and others don't care about me."
    th "Unless Ulyana, who is in debt for the morning events..."
    dreamgirl "Is that so? Did you finally heed my advice?"
    th "No, go away."
    "Slavya helped me carefully put the ladder on the ground."
    show sl normal pioneer with dissolve
    sl "Now for the garlands!"
    scene bg ext_clubs_day with dissolve
    "At the club building, she suddenly stopped."
    show sl normal pioneer with dissolve
    sl "You know, I didn't see you anywhere this morning. {w} Nor Lena."
    sl "You two are..."
    "Why was she suddenly so interested in such topic?"
    me "Lena was on duty at the infirmary post. And Ulyana and I... long story short, we spent time together."
    show sl serious pioneer with dspr
    "Slavya frowned."
    sl "Did you tell her to steal the boat?"
    "Huh."
    "So, authorities already informed?"
    "I wonder if the boatman also reported about the robbery of the cabin?"
    me "No. I mean, not really. It's a complicated story."
    sl "So take the trouble to explain!"
    me "Why? You seem to know everything already."
    show sl normal pioneer with dspr
    "Slavya sighed."
    sl "Semyon, the boatman told this only to me so far. Because he couldn't find Olga Dmitrievna."
    sl "And if tomorrow Ulyana's parents find out about this, then she will definitely be punished."
    sl "This isn't her first prank, and its far from the most innocent of all Ulyana has done during this shift."
    show sl serious pioneer with dspr
    sl "She could have damage camp's inventory or, God forbid, hurt herself!"
    me "But nobody got hurt. Why worry?"
    sl "Besides, Semyon, she can be escorted out of the camp before the end of the shift!"
    "I froze."
    "It was hard for me to imagine myself in the place of a child who is forcibly pulled out of this celebration of life, cutting off all the fun at once."
    "But it was humiliating to say the least."
    "Well, no. {w} I'm a fool myself - then why Ulyana is the only one to blame?"
    me "We had a bet and she lost. Her task was to steal the boat."
    show sl surprise pioneer with dspr
    "Slavya sighed in astonishment."
    sl "Did you even think with your head when you asked her to do this?"
    me "No."
    me "Honestly, sometimes I feel like I'm using my head only for eating."
    show sl angry pioneer with dspr
    "The girl looked at me sternly."
    sl "You will confirm that Ulyana is not guilty if you are asked about it by Olga Dmitrievna or the boatman?"
    me "Of course!"
    show sl serious pioneer with dspr
    "Slavya relaxed a little and let me inside the club building."
    play sound sfx_open_door_clubs
    scene bg int_clubs_male_day with dissolve
    play sound sfx_close_door_1
    play ambience ambience_music_club_day fadein 1
    "A little rummaging in the corner, she put a box with a garland on the table."
    show sl normal pioneer at right with dissolve
    sl "Check if it works. I'll look for spare parts in the meantime."
    sl "It's just that there was a power surge at the last disco and everything went out. Some of the bulbs might have burned out."
    hide sl with dissolve
    "The girl continued, stepping back into the corner."
    "I took the tangled garland out of the box."
    "At the bottom, a short, cut-off skein was found, on which several light bulbs dangled alone."
    "I've got a stupid idea."
    "Looking around, I quickly found scissors on one of the tables."
    "Checked the blades - they are sharpened properly."
    "I furtively turned to Slavya - she was still digging among the boxes."
    "A minute of manipulation, and the false bulbs were cleverly hidden behind my left palm."
    "Scissors were ready too."
    me "Slavya, do you want to see a magic trick?"
    sl "What magic trick?"
    show sl normal pioneer at right with dissolve
    "She turned around, and with a straight face, I snapped the scissors, cutting the bulbs off."
    show sl scared pioneer at right with dspr
    "Slavya screamed in horror:"
    sl "This is a new garland! They just brought it this winter!"
    "Yeah, I expected a less violent reaction."
    "Before she ran to beat me, I made a couple of mysterious movements over the cut garland with my right hand, lowered my hands under the table for a second, dropping the remnants of the cut wire on the floor, and pulled the ends of the garland with force."
    "Ding!"
    "A pair of light bulbs, unsuccessfully colliding during my manipulations, crumbled into small fragments with a ringing sound."
    "And I, like a fool, stood with a whole garland in my hands."
    me "Oops."
    show sl normal pioneer at right with dspr
    sl "Look what you did..."
    "The girl sighed, and a look of relief appeared on her face."
    sl "I'm glad I found spare bulbs."
    "She didn't seem particularly angry, which was good news."
    sl "Change the broken ones while I clean the glass, magician."
    hide sl with dissolve
    th "More like a clown than a magician. The kind that makes you laugh by their stupid antics on the stage."
    "I picked up some tweezers and sat down on the table, carefully removing plinths with remnants of broken glass from the garland."
    "Slavya, meanwhile, was sweeping the floor."
    "As soon as I replaced the damaged light bulbs and was ready to go, Slavya screamed."
    sl "Ouch!"
    show sl sad pioneer far with dissolve
    me "What happened?"
    "She didn't answer, just grimaced and put the edge of her hand into her mouth."
    show sl sad pioneer with dissolve
    "I put the garland in the box and jumped up to the girl."
    "Slavya showed me her palm, removing it from her mouth. {w} A trickle of blood immediately ran down her pinky."
    show sl normal pioneer with dspr
    sl "I didn't notice the shard on the table and leaned on it."
    sl "It's okay."
    me "No, it's not!"
    me "We have to check if there's any glass left in the wound. Give me your hand."
    show sl sad pioneer with dspr
    "I carefully probed her hand a centimeter away from the cut, and Slavya squeaked."
    me "I'm afraid we can't do anything ourselves. There are tweezers here, but I don't see any antiseptics."
    me "And some clean bandages, too. Let's go to the infirmary!"
    sl "No..."
    me "Yes! And no objections!"
    me "Let's go, we'll return for garlands later."
    play ambience ambience_medstation_inside_day
    scene bg int_aidpost_day
    show sl normal pioneer at left
    show cs normal
    with fade2
    "This time, Viola herself was at the infirmary."
    "She examined Slavya's cut skeptically and, pulling on her gloves, pulled out a tiny shard of green glass from the wound."
    show sl sad pioneer at left with dspr
    "The girl whined."
    cs "That slob has a bad influence on you. Before, you didn't come here much...{w=1} infrequently."
    "Viola bandaged her hand quickly and professionally."
    show sl smile pioneer at left with dspr
    "Slavya looked at her with gratitude."
    show cs smile with dspr
    cs "Now get out of here."
    cs "And next time, if you get another bleeding because of him..."
    cs "Well, you'll figure it out yourself."
    "We flew out of the infirmary like bullets."
    play sound sfx_open_door_1
    play sound sfx_close_door_1
    scene bg ext_aidpost_day
    show sl shy pioneer with dissolve
    with dissolve
    play ambience ambience_camp_center_day
    sl "What she was talking about?"
    "Slavya, blushing to the tips of her ears, muttered."
    me "Not a single guess. Some medical puns maybe."
    "I mumbled in a distant voice."
    scene bg ext_houses_day
    show sl normal pioneer
    with dissolve
    "Then I remembered something."
    me "Why did you ask if I was with Lena this morning?"
    "Slavya hesitated."
    sl "Well, I just haven't seen both of you, so I thought..."
    me "You haven't seen Ulyana either."
    sl "Well, you know, she always disappears somewhere."
    sl "She has company in the second squad, so we don't keep a close eye on her."
    me "And for me you do, huh?"
    show sl serious pioneer with dspr
    sl "Semyon, why are you so nervous about this question?"
    me "I don't know.{w} Just trying to figure out where I should expect another jealous scene."
    show sl normal pioneer with dspr
    "Slavya shook her head."
    sl "Don't get mad at Lena. You just seem to remind her of someone."
    me "Not the love of her entire life, I hope?"
    "I tried to laugh it off."
    show sl scared pioneer with dspr
    "The girl gloomed."
    show sl angry pioneer with dspr
    sl "Get this conversation out of your head.{w} And don't bring it up in front of Lena!"
    scene bg ext_clubs_day with fade2
    "Slavya disappeared behind the doors of the clubs, leaving me to ponder her words on the porch."
    th "What about me? I'm fine."
    scene bg ext_square_day_party_7dl with dissolve
    play sound sfx_7dl["eat_horn"] fadein 1
    "We brought the garland to the square just to the sound of the horn."
    show sl normal pioneer with dissolve
    "Slavya sighed."
    sl "Well, we'll hang it up after lunch."
    th "Unless, of course, Olga hangs us before then."
    "But I just nodded, and we silently walked to the canteen."
    stop music fadeout 3
    stop ambience fadeout 6
    stop sound fadeout 1
    with fade
    return

label alt_day3_day_un_fz_dv:
    scene bg ext_dining_hall_near_day with dissolve
    "I noticed Alisa hurrying somewhere."
    "So she was the indispensable partner that I needed so much!"
    scene bg ext_dining_hall_away_day
    show dv normal pioneer2
    with dissolve
    play sound sfx_punch_medium
    "I caught up with her and patted her on the shoulder."
    show dv angry pioneer2 with dspr
    "The girl jumped up and glared at me belligerently."
    dv "What do you want?"
    me "How about to do some work for the good of the Motherland?"
    show dv laugh pioneer2 with dspr
    "Alisa burst out laughing."
    dv "What else!"
    dv "Look for other fools. I have things to do."
    me "What kind of things?"
    show dv normal pioneer2 with dspr
    dv "And for what purpose are you interested?"
    me "Well, what if you need help with them?{w} Maybe things are so important that cleaning the area for the disco can wait?"
    show dv surprise pioneer2 with dspr
    "Alisa stared at me blankly, trying to determine if I was speaking sarcastically, intending to enlist her in community service at any cost, or if I really wanted to crowd into her company."
    "I grinned."
    me "So what? Do you need help?"
    show dv normal pioneer2 with dspr
    "Dvachevskaya hesitated, but still chuckled rather."
    dv "Let's go, little helper!"
    scene bg ext_musclub_day
    show dv normal pioneer2
    with dissolve
    "We came to Miku's abode, and I looked inquiringly at Alisa."
    me "What are we going to do here? Sorting records for the disco?"
    dv "Are you all right? We have a bigger mission!"
    show dv laugh pioneer2 with dspr
    dv "We will sit in the cool and wait for the lunch!"
    "For some reason, I wasn't surprised at all."
    me "Does Miku mind?"
    show dv normal pioneer2 with dspr
    dv "No."
    if 'music_club' in list_voyage_7dl:
        dv "On the contrary, she will be delighted - she hasn't had so many people since the day you came to sign the checklist."
        me "That was yesterday."
    else:
        dv "On the contrary, she will be delighted - she hasn't had so many people since the day when juniors came to her with their checklists."
        me "And how long ago was that?"
    dv "Uh, what's the matter even?"
    dv "Most importantly, Hat won't reach us here.{w} Let's go already!"
    stop music fadeout 9
    scene bg ext_musclub_verandah_day_7dl
    show dv normal pioneer2 far
    with dissolve
    "But before she had time to take hold of the doorknob, it became clear that Olga Dmitrievna had a different opinion about where and whom she could reach."
    show dv surprise pioneer2 far with dspr
    play music music_list["awakening_power"] fadein 2
    mt "...and this is also not needed. You can put everything else."
    mt "And don't forget to pick up at least a couple of slow dances!"
    show dv shocked pioneer2 with dspr
    "Footsteps were heard, and Alisa jumped away from the door in a panic."
    dv "Run!"
    hide dv with moveoutleft
    scene bg ext_musclub_verandah_day_7dl with vpunch
    scene bg ext_musclub_day with pushleft
    "Grasping my arm, the girl rushed over the verandah railing, and I jumped awkwardly after her. Landing pulsed with a dull pain in the bandaged wound."
    "We rushed towards the nearest bushes..."
    scene bg ext_backdoor_day_7dl at running
    with dissolve
    "...ran to an inconspicuous gate behind them..."
    scene bg ext_path_day at running
    with dissolve
    "...and finally jumped out onto the forest path hiding behind it."
    "Alisa did not think to slow down, and I was already tired."
    scene bg ext_path_day with dissolve
    play sound sfx_7dl["breath"] fadein 3
    "Breathing heavily, I stopped, leaning my hand against the trunk of a tree."
    stop music fadeout 5
    me "Can't... run... anymore..."
    play ambience ambience_forest_day fadein 2
    scene bg ext_polyana_day with dissolve
    play sound sfx_fall_grass
    "The hand treacherously slipped, and I fell into the bushes behind the tree."
    us "Holy f…"
    show us fear sport at left with moveinleft
    "Frightened Ulyana jumped out from behind the bushes."
    show dn shocked pioneer with dissolve
    "Following her appeared the swirling top of some boy."
    "He looked to be about her age."
    th "What a twist!"
    me "Were you kissing there?"
    "Stupidly I asked."
    show us shy2 sport
    show dn dontlike pioneer
    with dspr
    "Ulyana blushed so that her face almost merged with the T-shirt."
    hide us
    hide dn
    show al dontlike pioneer at right
    show tn dontlike pioneer at fright
    with dissolve
    "Following the couple, two more boys crawled out of the bushes."
    dreamgirl "You see!"
    "My inner voice laughed triumphantly."
    dreamgirl "You see, this girl has a great future ahead of her!"
    dreamgirl "She picked up three guys at once. And you, fool, were whining about her! Now sit down and repent."
    "I did not want to repent somehow."
    hide tn
    hide al
    show us normal sport
    show dn dontlike pioneer at right
    with dissolve
    dn "What are you doing here?"
    "The swirling pioneer asked us unfriendly."
    show dv normal pioneer2 at fleft with dissolve
    dv "We have the same question for you. We're hiding from the Hat. And you?"
    dn "That's none of your business!"
    show us calml sport with dspr
    "Ulyana grabbed his hand in warning."
    "In her other hand, I saw a hunting knife."
    th "Apparently, she already visited Lena."
    "The situation was getting more and more interesting."
    "From the outside, it looked like kids in the bushes were performing satanic rites."
    dreamgirl "Yeah, that's right. There were five of them when they left the camp!"
    show dv angry pioneer2 with dspr
    dv "Little one, if you'll be like that, I'll tear your ears!"
    "Alisa grinned."
    dv "Do you remember last year..."
    show us dontlike sport with dspr
    us "Alisa, please, don't start!"
    "Ulyanka stood in front of her friend, shielding the boy."
    show us normal sport with dspr
    us "Let's do this: we go for our business, you go for yours. No one seen each other, no one knows each other."
    show dv normal pioneer2
    show dn sad pioneer
    with dspr
    "I didn't expect such sane thoughts from Ulyana."
    "I mentally praised the girl."
    me "Alisa, let's go. We're not their squad leaders - let them entertain themselves."
    show dn scared pioneer
    show us surp2 sport
    show dv surprise pioneer2
    with vpunch
    play music music_list["awakening_power"] fadein 2
    voice "Danyaaa!"
    "There was a voice from somewhere behind the fence."
    "The children were terrified."
    dn "As if anything else wasn't enough..."
    us "What are you waiting for? Let's get out of here!"
    show dn normal pioneer
    show dv normal pioneer2
    show us normal sport
    with dspr
    "She suddenly turned to me."
    us "Hold her!"
    "And, after a moment's pause, she added:"
    show us shy2 sport with dspr
    us "Please."
    "Apparently, the voice belonged to the squad leader of these blockheads."
    "I categorically did not want to be caught outside the territory, even if not by Olga."
    "I was also bursting with curiosity."
    "What are they doing here that they don't want to catch the eye of the squad leader?"
    me "Okay. I'll hold her."
    "I squinted."
    me "But only if you explain to me what so secretive you were doing here."
    show dn dontlike pioneer
    show us surp2 sport
    with dspr
    dn "Stay away from us!"
    me "Is that so?"
    me "When you need help - you immediately run to me. When you asked to explain why I am substituted - immediately into the bushes?"
    me "Then no.{w} Deal with your problems yourselves."
    me "I'm already in trouble this morning because of your adventures."
    "Ulyana thought frantically."
    "In the end, she shook her head."
    show us sad sport with dspr
    us "Okay, you win - I'll tell you. But not now!"
    me "Catch you on that."
    hide us
    hide dn
    with dissolve
    "Swirling one looked at me gloomily, and they rushed off into the distance along the path."
    "Alisa and I looked at each other."
    "The gate creaked."
    dv "What are we going to do? Are we going to run away too?"
    stop music fadeout 2
    me "I have a better idea."
    show dv surprise pioneer2 close with vpunch
    play music music_list["i_dont_blame_you"] fadein 1
    scene cg d3_dv_kiss_7dl with flash2
    "I grabbed Alisa in an armful, pressed her against a tree and kissed her."
    "From surprise, she did not even begin to resist - she just went limp in my arms, her eyes wide open."
    pause(1)
    ka "Here you are!"
    stop music fadeout 1
    scene bg ext_polyana_day
    show ka shy pioneer at right
    with dissolve
    play music music_7dl["genki"] fadein 3
    "I pulled away from Alisa and turned to the squad leader."
    "She coughed in embarrassment."
    ka "Excuse me."
    show ka smile pioneer with dspr
    ka "I was looking for my slobs, but found you instead."
    show dv shy pioneer2 at left with dissolve
    dv "Um, we did nothing..."
    "Alisa was still in shock from what had happened, but from the outside it might have seemed like ordinary embarrassment, quite natural for such a situation."
    show ka laugh pioneer with dspr
    "Squad leader laughed."
    ka "Oh, as if I don't understand!"
    show ka smile pioneer with dspr
    ka "Just tell me, did you happen to see three boys around fourteen years old somewhere around?"
    me "No, no one was there. We've been here a long time, so..."
    ka "I see. I never can guess where they're hiding."
    "The woman sighed."
    ka "And what should I do with you now? Go and pass you to Olga Dmitrievna?"
    dv "Maybe... don't?"
    "Alisa was so embarrassed that even I felt sorry for her."
    show ka grin pioneer with dspr
    "Squad leader smiled contentedly.{w} A little too contented."
    "I've seen that expression before from..."
    ka "That's great!"
    ka "Let's just say I borrowed you from her for an errand."
    show dv surprise pioneer2 with dspr
    "... from her unbearable colleague."
    show ka smile pioneer with dspr
    ka "Follow me!"
    show ka grin pioneer with dspr
    ka "And just try to get lost along the way - I'll go and gossip to your artistic director that you are kissing here!"
    show dv shy pioneer2 with dspr
    "I shuddered."
    "Miku will crack this open to anyone who wants to listen!"
    "And this wisher will certainly be Lena - I had no doubt about that."
    "What else can the girls talk about in their house after lights out?"
    me "What's your name?"
    "I decided that addressing the squad leader solely with «excuse me» and «sorry» would be extremely impolite."
    "Besides, then we had to report to Olga about where we were hanging around the whole sleepin hour."
    $ meet('ka', "Katushka")
    show ka smile pioneer with dspr
    ka "Katushka, just call me Katushka."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    pause(1.5)
    scene bg ext_dv_hideout_day_7dl with dissolve
    play ambience ambience_camp_center_day fadein 2
    play music music_7dl["everyday"] fadein 2
    "She led us to a small area behind the cabins where the arm-training equipment was located."
    "The place was so well hidden that I never noticed it."
    dreamgirl "Maybe Satanic rites are their squad creed? Look, there's a circle already."
    dreamgirl "Now she will undress you and Alisa, lay you among these logs, and..."
    th "Why are you so itchy today?"
    show dv sad pioneer2 at left with dissolve
    "Alisa, it seems, has already moved on from the shock, and now she looked at me somehow unkindly."
    hide dv with dissolve
    "The only task left is to understand, it's because of the kiss or because she was still plowed to work."
    show ka smile pioneer with dissolve
    ka "Today, after the disco, I want to light a candle. We need to prepare the squad place a little."
    ka "So go to the warehouse and bring some old blankets here."
    ka "After dances, everyone will be wet as mice - don't want someone to catch a cold."
    show ka grin pioneer with dspr
    ka "And let's live it up - lunch is in half an hour!"
    scene bg ext_houses_day
    show dv normal pioneer2
    with dissolve
    "Alisa and I trudged towards the warehouse."
    dv "And what was that?"
    me "Party task from the leader of the second squad. Bring blankets."
    show dv rage pioneer2 with dspr
    dv "Don't pretend to be idiot!"
    "Dvachevskaya flared up."
    dv "I'm talking about what happened in the forest!"
    me "Ah, are you talking about this?"
    me "Ulyana wanted Katyushka to be distracted - I distracted her.{w} And you helped me a lot."
    show dv angry pioneer2 with dspr
    dv "Couldn't you have consulted with me beforehand? I don't like this kind of «distraction maneuvers»!"
    me "Sorry, didn't have time to strategize."
    me "And anyway - you portrayed the embarrassed girl so well that I almost believed it myself!"
    show dv laugh pioneer2 with dspr
    "Alisa suddenly burst out laughing."
    show dv smile pioneer2 with dspr
    dv "Just don't expect love to the grave! Otherwise, Lenka will be offended!"
    me "Not that I'm going to the grave anytime soon."
    "I grumbled."
    me "And anyway, what does Lena have to do with it?"
    show dv normal pioneer2 with dspr
    "The girl instantly grew serious."
    dv "Semyon, are you really retarded? Can't you see how she..."
    "Alisa sighed and waved her hand."
    dv "You won't understand anyway."
    scene bg ext_warehouse_day_7dl with dissolve
    "Aaand we got to the warehouse."
    play sound sfx_open_door_strong
    "Alisa slipped inside to get away from the conversation, but I didn't mean to let her slip off the subject so easily."
    me "So what about her?"
    "I followed."
    play sound sfx_open_door_strong
    scene bg int_warehouse_day2_7dl
    show dv normal pioneer2
    with dissolve
    dv "Nothing!"
    dv "Since you still don't understand, it's better for you not to know."
    "The blankets were on one of the shelves along the wall."
    me "I see that she doesn't like me very much, and yesterday she accused me of hanging around with you, but I can't understand what's the matter?"
    me "Today we chatted quite normally!"
    show dv surprise pioneer2 with dspr
    "I think I blurted out too much - Alisa's eyebrows crept up in amazement."
    dv "No, you're really an incorrigible idiot!"
    show dv normal pioneer2 with dspr
    "She took some of the blankets in an armful and went to the exit."
    hide dv with dissolve
    dv "You'd better not bother yourself with this.{w} And if you keep pester me with questions, I'll punch you in the forehead!"
    "I had no choice but to pick up the remaining blankets and go after her."
    scene bg ext_square_day_party_7dl
    show mt angry pioneer at left
    show ka smile pioneer at right
    with clock_r
    "Katyushka handed us over personally to Olga, praising us for our responsibility and willingness to come to the rescue."
    "Our squad leader wasn't too pleased, but she didn't grumble."
    mt "Since you are such great helpers that two of you were enough even for another squad, you will definitely be fine with decorating the square after the lunch!"
    show mt grin pioneer at left with dspr
    "She laughed wickedly."
    mt "Okay, go ahead - you deserve it!"
    "Alisa and I did not hesitate and ran to the canteen building - in a race, without saying a word."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_day_dv:
    scene bg ext_musclub_day with dspr
    $ counter_dv_7dl = 3
    show dv normal pioneer2 with dissolve
    "Alisa was already here, she walked impatiently past the door, now and then looking in the direction of the path from the canteen."
    "My luck was that I came from the square, which means she couldn't see me."
    "Moving on tiptoe, I crept closer to her left and patted her right shoulder."
    "Of course, she immediately looked in my direction!"
    show dv smile pioneer2 with dspr
    "She tried not to show it, but I noticed how delighted she was."
    "For a moment, my soul felt so warm, warm... Until I remembered why I was here."
    me "What are we going to do?"
    "I asked with caution."
    show dv grin pioneer2 with dspr
    dv "Like you don't know."
    "She walked behind me and politely pushed me, prompting to cross the doorstep..."
    scene bg int_musclub_day with fade
    play sound sfx_open_door_clubs
    play ambience ambience_music_club_day fadein 1
    $ volume(0.5, "music")
    play music music_7dl["outer"] fadein 3
    "Some kind of music was playing in the club - I saw a Soviet cassette spinning in the tape recorder, one of old, unkillable kind - although the music from there sounded the most modern!"
    "We quietly, so as not to creak the door, turned the handle and opened it, and then heard..."
    "A sparse beat - 170-bpm - punctuated by guitar riffs and female, almost childish vocals:"
    mi "…saa paati no jikan da yo!…"
    "And then guitar hacks, vaguely reminiscent of a set of dubsteps and other electronic heresy on my player, that I smuggled into this world."
    stop music fadeout 5
    "Miku spotted us out of the corner of her eye and instantly rushed to the tape recorder."
    "She turned off the music and turned to us, already smiling."
    show mi smile pioneer with dissolve
    play music music_list["my_daily_life"] fadein 3
    mi "Guys, finally you came, otherwise I already thought that you had changed your mind and would not come, but I was so upset, I thought about leaving already, I decided, here, a song..."
    show mi normal pioneer at cright with dissolve
    show dv smile pioneer2 at cleft with dissolve
    "Her breathing was smooth, as if she hadn’t just jumped like a goat all over the room in outlandish, Japanese choreography! At the same time, if my hearing didn’t lie to me, she also managed to sing..."
    me "Your voice is amazing..."
    show dv grin pioneer2 with dspr
    dv "And what did you thought? She's a star in her homeland, after all."
    "Alisa looked so proudly, as if it was her merit."
    dv "Young talent."
    show mi shy pioneer with dspr
    mi "You are exaggerating…"
    "Miku was confused."
    mi "I'm not a star, it's just that someone else likes my songs. And that's good."
    show dv smile pioneer2 with dspr
    dv "Your songs are good, but we are here for another thing. Teaching, remember?"
    "Alisa nodded at me."
    mi "I remember, of course! I also tuned the guitar for him, now it should sound good!"
    me "Are we going to play here or go outside?"
    show mi normal pioneer with dspr
    mi "Do you want to sit on the veranda?"
    show mi grin pioneer with dspr
    mi "I don't mind, but there the music stand is constantly blown away by the wind, it falls, and the notes fall, and I don't see anything!"
    show dv sad pioneer2 with dspr
    dv "What notes, Miku!"
    dv "Remember his level of play."
    "That's the hallmark of DvaChe - she swears and humiliates you, but you still feel grateful for her protection."
    "Maybe it's her unique superpower!"
    "I looked gratefully at Alisa, who saved us a few minutes in negotiations, and, grabbing the guitar by the neck, dragged it outside."
    scene bg ext_musclub_day
    with dissolve
    play ambience ambience_camp_center_day fadein 3
    show mi normal pioneer at cright with dissolve
    show dv normal pioneer2 at cleft with dissolve
    play music music_list["she_is_kind"] fadein 3
    "We sat down on the benches standing right there and started the lesson."
    "Have I already told you that I'm a music lover?"
    "So, after this lesson, I was ready to hate everything that was at least remotely reminds me of guitars!"
    "No, I remember the costs of learning to play the trumpet, for example - your lungs develop like a mountain dweller, and you lose the ability to get a second wind while running."
    "There is no need to talk about constantly chapped lips, and this is besides the fact that the degree of your usefulness is determined only and exclusively by the elasticity of the working surface of your lips."
    "With the guitar, everything turned out to be much sadder."
    "At first, my shoulders writhed due to an unusual pose, then my back ached - I couldn’t stoop, the instrument interfered. And as a result, my fingers buzzed. And then they started to hurt!"
    show dv laugh pioneer2 with dspr
    "Alisa just chuckled, watching my torment, and again and again explaining some common truths for her."
    "Miku acted here as a visual aid, purring something under her breath and plucking the strings in the background. And I felt like an absolute stupidity and mediocrity."
    "No, I remember very well that the training schedule for twenty-five years is very different from the seventeen-year-old young man that I looked like, but even then - in order to solidify some basics, I had to repeat five or six times!"
    show mi smile pioneer with dspr
    show dv normal pioneer2 with dspr
    "Finally, Alisa realized that traditional ways of teaching are useless, and decided to turn to non-traditional pedagogy."
    dv "Alright."
    "She quickly formed a certain chord."
    dv "Repeat."
    "I repeated."
    dv "Next."
    "She pressed another chord, about a fourth higher."
    "Nothing complicated either - I repeated this too. And even the third!"
    dv "Now listen."
    "She reproduced the progression of chords that formed into some minor melody."
    dv "Repeat."
    "I tried - it didn't work out very well..."
    "I tried again... {w=0.3}and again... {w=0.3}and again..."
    show dv angry pioneer2 with dspr
    dv "Listen, you can't be so stupid!"
    "She looked frowningly. And suddenly she caught herself."
    dv "Though why am I even saying this…"
    "She turned away."
    dv "You really are untalented."
    dv "If a bear stepped on the ear of some, in your case that bear spent the night in that ear."
    me "What!"
    me "I, - if you want to know, - studied! I was taught all this!"
    show dv grin pioneer2 close with dissolve
    dv "Taught how to miss the modes?"
    "She mocked me."
    me "No! Solfeggio, and musical notation, and intervals."
    dv "Looks like the teaching went wrong."
    dv "It's just a waste of time. You have no talent for music."
    me "Is that so?!"
    "I got seriously turned on. {w}At the same time, knowing full well that I was being manipulated - I still was unable to stop!"
    me "I just need to get used to it, then I'll play this unfortunate tune!"
    dv "No. You won't."
    show dv laugh pioneer2 close with dspr
    "Her eyes sparkled with mischief."
    me "Bet!"
    "I remembered yesterday."
    me "If I can play the tune in ten minutes, then you owe me something!"
    dv "Owe?"
    me "Yes! For example... Eh. If I play, then you will come to the disco with me!"
    "I thought a little."
    me "And put on a dress!"
    dv "Owe, you say..."
    "She laughed."
    dv "And if you don't?"
    me "I'll play!"
    show dv smile pioneer2 close with dspr
    dv "And if you don't?!"
    me "Place your bet already!"
    dv "I'll up the ante. If you do well, I owe you a kiss."
    "I startled."
    me "Real one?"
    dv "But of course... And if you lose..."
    me "I'll play it, don't worry."
    "I already mentally figured out how to intercept the guitar in such a comfortable way."
    dv "Well, if not... Then..."
    show dv laugh pioneer2 with dspr
    show mi happy pioneer with dspr
    "Alisa thought, and, like yesterday, burst out laughing."
    dv "Then you'll be the one to put on the dress!"
    me "What?! No!!!"
    dv "Why not? Come on! We've made a bet!"
    me "I cannot agree to these terms."
    dv "Is that so?"
    show dv smile pioneer2 with dspr
    dv "Maybe a kiss then?"
    me "What do you mean?"
    dv "If I lose, then I'll kiss you. If not, then you... kiss..."
    show dv laugh pioneer2 with dspr
    dv "Her!"
    "She pointed at Miku."
    me "No!"
    dv "Uh you've tired me, shut up!"
    dv "Miku, are you following?"
    show mi laugh pioneer with dspr
    mi "Easy!"
    dv "Yes! Now, start playing!"
    "It seems that my beloved tormentor has already decided everything for herself again."
    "As did Miku, who seemed to take great pleasure in taking part in the process of humiliation."
    "And I tried!"
    "Then again!"
    "Once again!"
    show blinking
    pause(3)
    dv "Well…"
    "She sighed."
    dv "Miku!"
    scene bg ext_musclub_day
    show mi sad pioneer close at center
    with dissolve
    mi "Yeah, a moment."
    "The Japanese girl put her guitar aside and stood up."
    "She was clearly heading towards me!"
    stop ambience fadeout 2
    stop music fadeout 3
    pause(1)
    play music music_list["gentle_predator"] fadein 3
    mi "Don't move, I'll be quick."
    "She promised as she approached."
    "I jumped up!"
    show mi sad pioneer close
    scene bg ext_musclub_day:
        linear 0.1 pos (-5,-5)
        linear 0.1 pos (0,0)
        linear 0.1 pos (5,5)
        linear 0.1 pos (0,5)
        linear 0.1 pos (5,0)
        linear 0.1 pos (0,0)
    show mi sad pioneer with dissolve
    me "Do not come any closer! No!"
    dv "Semyon."
    "Alisa growled unhappily. It seems that she herself was no longer enthusiastic about the idea, but decided to follow the rules to the end."
    dv "You can't escape it anyway. {w}Give it up."
    me "I don't want to!"
    show mi angry pioneer at left
    show dv sad pioneer2 at right
    with dissolve
    me "I'll try again!"
    show dv normal pioneer2 with dspr
    dv "Semyon..."
    "Thoughts ran in search of a way out."
    "What should I do? Run away from the girls os not the best idea? {w}Or?"
    "They know everything about kung fu in Japan, she'll will break me, and..."
    "I preferred not to think about what would come next, but on the run, puffing and sniffing, I found the necessary modes by force and, already squeezed into a corner, put my guitar in front of me:"
    me "Stop!"
    show mi happy pioneer with dspr
    "Miku stopped and tilted her head thoughtfully."
    "Remember how I said that something upset her?"
    "Forget it!"
    "The Japanese girl blushed, bit her lip and was amazingly beautiful like that, almost catching her prey!"
    "I was embarrassed and hid my eyes, hoping that Dvachevskaya would not intercept it and interpret it her own way."
    me "Here!"
    "With trembling fingers, I found the modes and, with a sin in half, performed the same melody!"
    show mi smile pioneer with dspr
    mi "You're smartie, Semyon!"
    "Miku pressed her folded hands to her cheek in a gesture of approval."
    mi "I didn't doubt you one bit."
    dv "I didn't believe it until the very end. {w}Although he suggested the bet idea himself. I wanted to stake something more extreme."
    show dv smile pioneer2 with dspr
    "I didn't listen to her anymore."
    "Fingers, which until the last moment felt like wood, suddenly gained some sensitivity, mobility, and crystal clarity of modes, their order, suddenly became completely obvious."
    "At the very moment when I not only heard something in someone's performance, but heard a melody somewhere inside myself."
    "Already more confident, I let my right foot go for a walk, counting the tempo, and in a relaxed mode played the melody again."
    dv "Hmm... It's still a long way from a satisfactory result, but already much more confident."
    "Reluctantly concluded Alisa."
    show dv grin pioneer2 with dspr
    "She put down her own instrument and stood up, stretching."
    if alt_day2_date == 'dv':
        "And I suddenly remembered how she looked, not in a pioneer uniform - albeit with a hooligan knot under the chest - but in a swimsuit, with wet skin..."
    "Stop, don't get distracted! Don't act like a horny teenager turned on the basis of constant toxicosis!" with hpunch
    show dv laugh pioneer2 with dspr
    "The last remark for some reason caused a skeptical smirk."
    "I remembered the reflection in the mirror. Internal sensations. The way the body responds and sings from the action."
    "Hmm... Actually, I'm sort of a teenager now. Physically, at least, and one hundred percent hormonally, too!"
    dv "You surprised me."
    dv "That's why I'm inviting you to a mini-concert on the stage tonight."
    me "How mini is that?"
    show dv guilty pioneer2 with dspr
    dv "You and me."
    "She frowned."
    dv "Or do you want to gather an entire stadium?"
    me "No. I'm more than satisfied with this kind of audience."
    show mi sad pioneer with dspr
    mi "So you're not going to the dances, are you?"
    "Miku was surprised."
    mi "How so?! All the guys should be there!"
    if alt_day3_mi_rejected:
        me "Miku, I think I made myself clear enough at dinner."
        me "I'm not interested."
        me "And apparently Alisa too."
    show dv normal pioneer2 with dspr
    dv "Good luck with the dancing guys. The main thing is that you don't involve us in this."
    me "Olga will say that the event is public, and everyone should be obliged. At least just to be present."
    dv "Let her find us first."
    "Alisa grinned."
    dv "So? Are you coming over tonight? Or…"
    "She flashed quotation marks in the air."
    dv "Are you going to dance with the girls?"
    show dv smile pioneer2 with dspr
    menu:
        "Invite her":
            me "And can I. Invite {b}you{/b}?"
            show dv laugh pioneer2 with dspr
            dv "What? Ha-ha-ha-ha!"
            show dv normal pioneer2 with dspr
            dv "No."
            me "But I wanted to..."
            dv "No."
            $ lp_dv += 1
        "I'll come":
            me "I'll come of course."
            "I shrugged."
            me "I'm more interested in you than dancing to someone else's music."
            mi "But the best tapes will be there!"
            "It seems that Miku was in charge of the playlist - she rushed to protect her charges."
            me "What? Maisky Lai with Yurochka Ushatalov? Or some Antonov-Vizbor-Korengluk?"
            show mi angry pioneer with dspr
            mi "And what's wrong with them!"
            me "Everything."
            "I nodded to Alisa."
            me "It's decided, wait for me on the stage tonight."
    "I didn't think twice."
    "All other arguments were just a splurge on the most important thing - Alisa will not be at this disco!"
    "It’s not that I don’t know how to dance at all, I rather don’t like it. Moreover, the last time I danced was five years ago, and it was to wild broken rhythms, when the boys and I rolled out several sheets of hardboard on Malaya Konyushennaya and danced heartily."
    "I don't think those dances would be appropriate with a playlist presented here."
    "And this means that half the time I will stand and pick my nose... Maybe I will invite someone for a slow-motion, which is like the smaller part. Bceuase if it wasn't the people will not have time to «break away»."
    show dv sad pioneer2 with dspr
    dv "And you, Miku?"
    "For a second it seemed to me that Alisa was dissatisfied with something. However, after the Japanese girl's negative answer, she blossomed again."
    mi "No, I'll definitely go to the disco! I like to dance, and it's not often here."
    dv "Okay."
    dv "Well, we're off. Thanks for the lesson."
    "I nodded, furtively blowing on my bruised fingers."
    mi "Come back anytime you want!"
    mi "And you, Semyon, I'm waiting for you tomorrow, in the morning or in the afternoon, we will repeat everything you learned today!"
    me "What?"
    "I scared seriously."
    me "Everything?!"
    show mi laugh pioneer with dspr
    mi "Well, not arguing of course..."
    mi "But you have to memorize indicated chords. You will perform with them."
    hide mi with dissolve
    show dv smile pioneer2 at center with moveinleft
    "With these words, she took the guitar from me and disappeared behind the door, leaving me with an open mouth to assimilate what was said."
    dv "Shut your mouth."
    "Alisa flicked my chin."
    dv "Or you'll catch a fly."
    me "Uh-huh…"
    "I was slowly coming to my senses."
    me "Once again, who signed me up? For the contest."
    show dv grin pioneer2 with dspr
    dv "I did."
    "Alisa replied serenely."
    dv "What's the matter?"
    me "Nothing..."
    if loki:
        "The fingers curled themselves into a suffocating gesture, and I reached for her neck."
        me "Noooooothing..."
        show dv scared pioneer2 with dspr
        dv "Hey-hey, psycho!"
        "She jumped back two steps at once."
        dv "What are you think you doing?"
        me "Want to strangle you... So that you don't torment nor me nor yourself."
        show dv laugh pioneer2 with dspr
        "She hurried to put something immovable between herself and me."
        dv "What are you saying? I wish for the better! You're so modest, you would never have guessed."
        "She grinned mischievously."
        dv "And now there's a solo number! So{b}t{/b}gn!"
        "She highlighted the letter «t»."
        me "Straaaangle…"
    else:
        me "You are the most hostile foe, Dvachevskaya..."
    "I leaned helplessly against the roof support column and sighed."
    me "Alisa, I didn't do anything bad to you."
    if (alt_day2_gamblers_result['me'] < alt_day2_gamblers_result['dv']):
        me "And even purposfuly lost to you at cards yesterday. Why are you doing this to me?"
    me "Why, just why?"
    dv "For being kind to me."
    "She got up on the other side of the column and seemed to lean her back against it."
    dv "That's it. You were kind and I tamed to you."
    dv "Like Saint-Exupery, remember?«{i}We are responsible for those we tame{/i}»."
    show dv smile pioneer2 with dspr
    me "But we are not responsible for those who we didn't have time to tell the to f..."
    "I muttered under my breath."
    dv "What?"
    me "Nevermind."
    me "So you, then, because I did a good deed for you, will never forgive me now?"
    dv "Something like that. You and I are kind of friends now..."
    show dv shy pioneer2 with dspr
    dv "Which means..."
    play music music_list["your_bright_side"] fadein 5
    me "Kind of?"
    "I chuckled."
    me "The Friend Zone grows and expands. {w}And it's so sad that none of them have ever met a guy like me."
    dv "Are you delirious again?"
    "In tone she answered."
    me "No but..."
    me "Tell me, Alisa, has it ever occurred to you that friendship isn't the ultimate dream of a single young man like me?"
    dv "Are you suggesting we could date?"
    "She laughed sadly."
    dv "That wouldn't work out."
    me "What? Why?"
    dv "Lena."
    me "Lena what?"
    dv "I see how you look at her, how you react to her image of a fragile, embarrassed girl."
    dv "Don't you want to hug, comfort, tame and take her home at last?"
    show dv sad pioneer2 with dspr
    "I didn't have anything to say."
    if lp_un >=3:
        "Because until the very last word, Alisa was right, and although I did not want to admit it to myself, I had long been looking for an opportunity to get a little closer to Lena."
        "But damn it! It's a normal reaction!"
        "A healthy reaction for a boy to a sad girl, is to console, support, or at least show concern."
    else:
        "Because Alisa was fundamentally wrong: for all the time spent in the camp, I had practically no contact with Lena."
        "At lest, no more than with the rest of the pioneers, including the redhead herself."
    th "Girls always just need a reason to be jealous."
    dreamgirl "What does jealousy have to do with it, dumbass? Either the girl will check you for lice, or she has a full wagon and a small cart of complexes."
    dreamgirl "Which, if you get close, is up to you to sort out."
    dv "And now she's all such a resentment, everyone look into her mouth trying to guess her desires."
    dv "And you know what's next? She'll say no - she can't do that to her best friend."
    dv "And she will take away the chance of both the sympathetic fool and his best friend, whom no one pays attention to, because she is either too self-sufficient, or simply lost somewhere on the background."
    dv "Didn't it ever occur to you, looking at her and me, that we are, in general, both loners and are constantly in the same boat?"
    me "No. You look like you don't need anyone..."
    show dv normal pioneer2 with dspr
    dv "Does she look like she needs everyone? Or is it all your speculation and initiative?"
    "She chuckled."
    dv "I don't mean to say she's bad, or that she is acting, although there's something to that."
    show dv guilty pioneer2 with dspr
    "Her voice broke and she fell silent."
    dv "So let's not spoil our beautiful friendship with some kind of relationships."
    "She sniffled."
    dv "You have what I look for in people - you are perfect as a colleague, friend, comrade in mischief... But not a boyfriend. I'm sorry."
    "And I again stood and grabbed the air with dead lips."
    th "How so... Did I do something wrong? Or did I say something? Or was I again extremely politely pointed out that I should know my place?"
    if herc:
        me "And if there was no Lena?"
        "I finally broke the silence."
        me "If you didn't have this paranoia of yours that she wants to take all your toys - what would you say then?"
        dv "Then... I don't know what you think of me or how you feel about me in general."
        dv "Even though this conversation gives a couple hints..."
        dv "Maybe I'd take the risk... Try..."
        me "Try what?"
        "There was a sleepin hour in the camp, and the hot sun scared away both birds and insects, so a ringing, strained silence reigned in the hot air. And only because of this I could hear a barely audible answer:"
        dv "Something else..."
        show dv sad pioneer2 with dspr
        "I unstuck from the column and walked around it, finding myself in front of Alisa. Her eyes were dry, her gaze wandered somewhere in the heavenly heights and was so dreamy..."
        me "It was enough for you to just say what's bothering you."
        "I suddenly felt that I was inexplicably angry, about the same as when I found out that I had already been signed up for an amateur concert."
        me "And we would find a solution. Together, you know? Any relationship is mutual."
        "I caught her eye."
        me "Your problem is not so much about Lena, but the fact that you decided everything for everyone a long time ago! {w}You gave me the role of a klutz, a retard, who fell under someone's charm and could only drool."
        me "That's it, ticked the box, turned the page? Answer!"
        show dv guilty pioneer2 with dspr
        "She looked away."
        me "Well, I'm not some kind of check mark. I don't know all the nuances of your relationship with Lena, but if you would bother to at least a little believe in me..."
        me "...not even in me - in yourself!"
        me "Half your problems would have been solved by now!"
        "I sighed, cooling down."
        me "I am afraid we can't be friends."
        "I said it as evenly as I could."
        me "Because you don't give indulgence by handing out roles, or second chances for those who suddenly don't fit the yardstick."
        me "I think it's a high price to pay just to shake your hand once a day."
        me "Buddy."
    elif loki:
        me "So you want to play and run, but you don't give a shit about relationships?"
        dv "Relationships? You're playing this «relationship» yourself like you want to get big and smart faster."
        dv "I'm sorry, but I won't play this game with you."
        th "Evaluate everything in terms of games?"
        th "How can you be so childish?!"
        me "And if I say it's…"
        dv "What?"
        "It's hard for me. Don't push it."
        "Why do such conversations always occur when there is no strength for them?!"
        "It's not fair, it's not fair!"
        me "Not a game."
        "I went around the column and stopped in front of Alisa."
        show dv shy pioneer2 with dspr
        me "What if all of this is serious?"
        show dv smile pioneer2 with dspr
        dv "In three days? For two of which you were afraid of and hated me..."
        dv "Very funny."
        me "I'm a very bad friend, Alisa."
        me "Sorry."
    else:
        "What else could be said here?"
        "Try our airlines «Rooftop - Asphalt»?"
        "Use only our, trusted, time-proof, casein heart-glue?"
        "A testament written with a sharp feather, like an inkwell, dipped into a bleeding ego."
        "No, it doesn't hurt anymore. My shins and knees are already stuffed, and I put the block that protects my head and groin almost automatically."
        "Curl up as an embryo, releasing a secret with cyanogen chloride into the world."
        me "Understood."
        hide dv with dissolve
        "Turning around, I waved my hand."
        me "You could tell right off the bat that I don't qualify."
        me "Good."
    scene bg ext_square_day
    with dissolve
    play ambience ambience_camp_center_day fadein 5
    "Elvis left the chat."
    "I went out under the scorching sun, and without turning around, wandered aimlessly."
    "Oh no, I wasn't angry at all."
    "I’ll quietly strangle someone, and I’ll immediately become cheerful and healthy. Whats wrong with her"
    "Now she pretends to be a feminist, declaring that she absolutely doesn’t need anyone, then suddenly it turns out that she does, but he does not pass through the competitive selection - because, you see, she has already thought of everything for him."
    "Typical female logic: she came up with it herself - now she is offended by it!"
    "Looks like she's got more cockroaches in her head than me..."
    stop music fadeout 3
    return

label alt_day3_aftermath:
    if alt_day3_duty:
        scene bg ext_dining_hall_away_day with dissolve
        stop ambience
        "The clock showed half past four, which means that soon it will be possible to get hold of some trifle at the canteen - praise to God that they are not force us to serve a lunch."
        "Even the smallest pioneer will be able to pick up a bun and a glass of kefir, then return the dirty dishes to the sink. They are probably taught this."
        if alt_day2_us_shenan:
            "I decided, just in case, to check the canteen for the presence of «cocktails» after dinner made me take the matter of duty more seriously."
            "Practice shows that children learn all sorts of abominations and stupidities in the «seen once - remember for a lifetime» mode."
            "I chuckled, remembering how I intercepted Ulyanka, who was about to splatter again with the remnants of someone's dinner."
        scene bg int_dining_hall_day
        with dissolve
        play ambience ambience_dining_hall_empty fadein 3
        show us normal sport at center with dissolve
        "Ulyana was already here, chewing something intently."
        me "What are you eating?"
        "I asked."
        "She just waved in the direction of the distribution. There was an aunt already familiar to us, who smiled at me."
        voice "If you come to help we don't need it at a time. Unless you run through the tables later, if they suddenly got dirty somewhere."
        "I was a little skewed by her popular style of speaking, but for a piece of Viennese pastry I was ready to endure not only that."
        "I nodded, and, taking a still hot bun, went to Ulyana's post and sat down next to her."
        me "Hello to the attendants!"
    else:
        if not (alt_day2_date == 'un_fz'):
            scene bg ext_square_day with dissolve
            "The clock has marked the end of the quiet hour, which means you can move freely around the camp."
            "But where to go?"
            "For lack of a better option, I listened to the voice of the stomach and went towards the canteen - in the foreseeable future, lunch was promised there."
        stop ambience fadeout 2
        scene bg int_dining_hall_people_day
        with dissolve
        play ambience ambience_dining_hall_full fadein 3
        show us normal sport at center with dissolve
        "There were not many people, it seems that not everyone has woken up yet. Although Ulyanka was already sitting here and, swinging her legs, ate the Viennese muffin, unwinding it around the circumference."
        "I ate it myself, I know - that way it tastes better."
        me "Hello little one."
    us "Hi."
    "She stared at me. And for some reason I felt so embarrassed that I hurriedly chewed the bun and turned around:"
    me "Why are you hypnotizing me? Did I suddenly grow a second head?"
    us "No."
    play music music_list["trapped_in_dreams"] fadein 3
    if (counter_un_fz == 2):
        if (counter_un_fz_dv_fake_date == 1):
            show us smile sport with dspr
            us "Thanks for covering us."
            me "You said yourself that a pioneer should help a pioneer, didn't you?"
            us "Thanks anyway. How did you distract Katyushka, by the way?"
            me "Some things are better left untold."
            show us normal sport with dspr
            "I calmly continued to chew the bun under the gaze of Ulyana."
            me "So, will you tell me the secret of your illegal activities?"
            show us grin sport with dspr
            us "Not now. There are extra ears all around!"
            "She finished her kefir in one gulp."
            us "You'll find out later!"
        else:
            show us grin sport with dspr
            us "I think about when you pounce on me with questions."
            me "When I eat, I am deaf and dumb."
            "I mumbled with my mouth full."
            me "Fast and fabulously cunning!"
            show us laugh sport with dspr
            "Ulyana giggled."
            us "So you don't care why I needed a knife?"
            me "What, you no longer need it?"
            show us smile sport with dspr
            us "I already took it from Lena."
            me "Well, why?"
            us "That's something I can't tell you yet."
            us "There are a lot of people here, and this is a terrible secret!"
            th "Damn you!"
            show us laugh sport with dspr
            "Seeing my sour face, Ulyana began to smile."
            us "Calm down, you'll find out soon enough!"
        hide us with moveoutleft
        "She rushed out of the canteen, leaving a dirty glass on the table."
        "It seems to have become a tradition to clean up after her."
        stop ambience fadeout 6
        play sound sfx_open_door_1
        pause(1)
        scene bg ext_dining_hall_away_day with dissolve
        return
    else:
        "She suddenly shook her head seriously."
        us "You look like you was hit with a sack. Did you have a fight with Alisa, or what?"
        me "Even if so."
        "I suddenly bristled even for myself."
        me "So what?"
        us "Nothing."
        "Ulyanka became sad and, turning to the table, was picking a hole in the oilcloth with her finger."
        us "She'll walk around sad later because of that: won't get mad or play. Alisa, though big, is stupid sometimes, so don't offend her."
        "I choked on a muffin and coughed for a while, trying to get my breath back."
        me "Hurt? She herself can hurt whoever you want..."
        us "I heard. But still, she goes around like a rooster, and in the evening she even grieves sometimes. I see that, console her all I can, but I can't help her. She needs someone her age, and preferably a boy."
        th "How would you know, youngster? Aren't you too small for such reasoning?"
        "I chuckled as I followed her thought."
        us "Don't you grin, or do you think that if she is swearing and being impudent, then she's the same for the soul?"
        "I had no delusions on this score. It is impossible to be rude to others and to yourself."
        "I had some doubts, and then I decided that it wouldn't get any worse. After all, Ulyanka is Alisa's best friend. Maybe, at least, through her it will be possible to somehow convey the idea."
        me "She said I'd leave her as soon as someone wags their tail."
        us "Someone - Lena?"
        "The little one wasn't surprised at all."
        me "How do you know?"
        "She waved her hand."
        show us sad sport with dspr
        us "They been like this since childhood."
        us "Everyone is pecking at Lena, because of this, Alisa is completely upset and completely insecure."
        us "She doesn't believe that she can be needed."
        me "Good old inferiority complex. big-headed psychologist would be useful here."
        us "Or a psychiatrist. They should cut contact with between each other altogether, so that both of them would have less headaches."
        show us angry sport with dspr
        us "But no! They «grew up together»!"
        "Ulyana was clearly mimicking someone."
        me "What should I do?"
        show us normal sport with dspr
        us "Are you asking me? I'm a fourteen-year-old girl, and I have no right to give you advice."
        me "Are you suggesting I ignore what she says?"
        us "Woman's talk."
        show us smile sport with dspr
        with dissolve
        "She smiled."
        us "Ignore half, divide the other by two. Then decide yourself."
        show us smile sport with dspr
        "She smiled mischievously, the flow of wisdom from a fourteen-year-old girl was interrupted, replaced by a more familiar image of a mischievous fidget."
        us "But i'm telling you again - if you hurt Alisa, I'll put bugs in your slippers.{w} I have one."
        if alt_day3_us_bugs == 2:
            "I gasped."
            me "I told you to let them go!"
            us "Be-be-be, that's how I listened to you."
            me "I still had to tell Olga Dmitrievna everything."
            us "So you didn't tell?"
            "I shook my head."
        if alt_day3_us_bugs == 1:
            me "Yes, I know!"
            "I scratched my right palm, which is still itchy from the crowbar."
        else:
            me "Bugs?"
            us "Yes! I caught them the whole quiet hour!"
            show us laugh sport with dspr
            "She took out a matchbox from her pocket and brought it to my ear. From there came a multiple, extremely menacing rustling, belonging to more than a dozen chitinous paws."
            me "Oh f... Why do you need so many?"
            "I asked."
            us "Secret!"
        "She looked at my wary face and laughed."
        us "Don't worry, I won't spill them on your plate. They're for someone else."
        me "It would be interesting to know..."
        if alt_day3_duty:
            "I muttered and turned away - the first wave of pioneers was entering the canteen."
            "Our squad was among the first."
            show mt smile pioneer at right with dissolve
            mt "How's your duty?"
            "The squad leader stopped next to us."
            me "Goes well with your prayers. {w}After your invaluable help at dinner, the morale of the team has risen to unprecedented heights!"
            mt "That's the spirit."
            "She laughed, and I looked behind her elbow..."
            "Alisa was gone."
            me "And… ahem… Dvachevskaya? Won't come for lunch?"
        else:
            "Without much interest, I muttered - just to say something."
            "Meanwhile, other pioneers followed me."
            "Soon, Olga Dmitrievna also appeared, judging by her slightly wrinkled face, she was sleeping through the whole quiet hour."
            show mt normal pioneer at right with dissolve
            mt "Semyon, where were you during quiet hour?"
            me "Rehearsed with Miku and Alisa... Then I went here."
            "I was talking, and in a meantime was looking out for familiar «Lightning tails»."
            me "We missed each other a little, did you happen to see her?"
        mt "She said she had a headache and went to the infirmary. Why are you asking?"
        show us normal sport with dspr
        us "It's just weird. She never skipped a meal."
        "Ulyanka helped me out."
        us "Maybe she really got sick."
        "We know this disease. It is called - one moron is so unpleasant that we do not want to see him, and even agree to sacrifice the unfortunate Viennese muffin for this."
        "In the end, I was offered friendship - I must appreciate, and not come forward with demands for more."
        th "Really, what do I, personally, did to deserve this «more»?"
        if alt_day1_me_d3_dv_feed == 1:
            if (alt_day2_date == 'dv'):
                th "Kefir-buns and coop bathing?"
            else:
                th "Kefir and buns?"
            "Awesome value."
        "I can still remind about yesterday's bet."
        "I automatically looked after the squad leader and again stared at the table, immersed in my own thoughts."
        hide mt with dissolve
        show us grin sport with dspr
        us "You're screwing up again."
        "Ulyanka nudged me with her elbow and winked slyly."
        us "Do you think she needs you this way?"
        me "The problem, my dear girl, is that she doesn't need me any way. Neither this nor that."
        show us laugh sport with dspr
        us "Still, you're strange: sometimes you act like you're older than all of us, and sometimes you do and say such stupid things."
        me "The cost of parenting."
        show us normal sport with dspr
        us "Stupidity."
        "She snorted and got up."
        if alt_day3_duty:
            us "Let's go check the tables."
            "I nodded and trudged to the other end of the hall."
        else:
            us "Finished? Let's go."
            me "Where?"
            us "It's up to you to decide. Or are you going to live in the canteen now?"
            "I shrugged indifferently."
        stop music fadeout 3
        "I didn’t feel like doing anything anymore - as if all the energy filling me had suddenly disappeared from my internal energy reservoir."
        play music music_list["silhouette_in_sunset"] fadein 3
        "And that feeling returned, from which I fled into this little world - gray hopelessness, when you don't want anything and don't need anything."
        "An old acquaintance enters the soul, habitually strokes the subdued instincts on the heads - like purebred dogs - sits down in the most comfortable chair and lights up."
        "Did I expect to get rid of her by simply running away into the summer?"
        "For some three days?"
        "When you're past a quarter, you can no longer change so quickly, discarding old prejudices as they become obsolete."
        "Even learning to be a person who cares is already a huge job, and at my age it is doubly difficult because of the inertia of the psyche."
        "What's the most foul thing about my position is the overestimation of all life milestones in negative direction."
        "Each victory means half as much to me, and each defeat sounds twice as crushing."
        "And you get into this vicious circle of the absence of any stimulation, and you sink deeper and deeper, because even in order to stay afloat, you need to spend energy. But where can you get it?"
        if alt_day3_duty:
            scene bg int_dining_hall_day
        else:
            scene bg ext_dining_hall_away_day
        with dissolve
        "I was well aware that now I am in ideal greenhouse conditions, a kind of spherical vaccum example from a textbook about socialization - to be locked on the same ship with a dozen beauties for an indefinite period."
        "Let's replace the ship with a camp, and leave the beauties, only cut their years to the level of teenagers with all the consequences. And lock the hero along with them."
        "The ideal situation. As the only relatively sane representative of the stronger sex, the hero is simply obliged to communicate with girls and make contact with them, get closer, and they, in turn, have not yet gained either worldly experience or worldly cynicism, therefore they are open and ready to communication."
        "This truth as old as the world about consciousness-defining being."
        "Let's pull it a little for convenience, and we get the following..."
        "I began to bend my fingers, counting those with whom I have zero chances not only to get along, but simply to meet:"
        scene anim prolog_1
        with fade3
        stop ambience fadeout 3
        show un normal pioneer at cleft with dissolve
        "Lena is an intellectual."
        "I don't go to libraries and museums, so there's no chance."
        show un normal pioneer far at cleft with dissolve
        show dv normal flipped at cright with dissolve
        "Alisa is a girl-fire, a person of creativity."
        "It's concerts, sessions and clubs. {w}Where, again, I don't go."
        show dv normal flipped far at cright with dissolve
        show sl normal pioneer at fright with dissolve
        "Slavya - Shoigu in a skirt."
        "We have completely different habitats."
        show sl normal pioneer far at fright with dissolve
        show mi serious pioneer at fleft with dissolve
        "Miku is another person of creativity, moreover, eastern and a star."
        "No chance."
        show mi serious pioneer far at fleft with dissolve
        show us laugh sport at center with dissolve
        "Ulyanka is a hyperactive source of trouble."
        "These I dropped from my life in the first place, because they carry a serious threat to my familiar little world."
        "These people can - and what's worse, they want to - pull me out of my lair, shake me up and not let me drown in my cozy swamp."
        "And it must have happened that I was locked on the same ship with just such girls."
        show un serious pioneer far at cleft with dissolve
        show dv grin pioneer far at cright with dissolve
        show sl angry pioneer far at fright with dissolve
        show mi upset pioneer far at fleft with dissolve
        show us normal sport far at center with dissolve
        "And it had to happen that I, as usual, messed up everything. Maybe I should have agreed to Alisa's offer of friendship?"
        hide un with dissolve2
        hide dv with dissolve2
        hide sl with dissolve2
        hide mi with dissolve2
        show us grin sport with dissolve2
        hide us with dissolve2
        "Yes, but the thing is that friendship will not work out for us."
        "And a touching truce with knives at the throat will not work either."
        "For a person who got so close, I have two roles - either nearby or in the forest. And I seem to have decided everything for myself a long time ago."
        "The only problem is that I decided for myself, and put Alisa in front of this as a fait accompli. Quite her style by the way."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_nightmare:
    scene anim prolog_1 with dspr
    "My head is already buzzing with thoughts. We need to put the world on pause and let this whole pile of thoughts ferment a little."
    if alt_day3_duty:
        "While dreaming, I did not notice how I had already wiped all the tables."
        scene bg int_dining_hall_day
        "Time to get outside."
        "But it's scary. {w}What if she's there? {w}On the street. {w}What if she's waiting? {w}Or we'll meet by chance."
        "What eyes will she look at me with? {w} What will she think?"
        "Solid questions, none of which can be answered speculatively. Actions are needed. And doing them is about as scary as going outside."
        show us normal sport
        me "Ulyana, look outside, tell me, is there anyone there?"
        show us calml sport
        "She was surprised, but she complied with the request."
        us "No, nobody."
        me "Thank you."
        "I exhaled and jumped outside."
        hide us with dissolve
        play sound sfx_open_dooor_campus_1
        stop ambience fadeout 1
        scene bg int_house_of_mt_day
        show unblink
        with fade
        pause(1)
        play ambience ambience_int_cabin_day fadein 1
        "Stealthily, I crossed half of the camp, and, hiding in the house, threw myself on the bed, crossed my legs and stared at the ceiling."
    else:
        scene bg ext_house_of_mt_day with dissolve
        "While reflecting, I did not notice how my legs themselves led me to my house."
        "My house... That's how people disappear. First they scream, fight, then they resign... And as a result, they can no longer live."
        "I had a hard time imagining life after «Sovyonok»."
        play sound sfx_open_dooor_campus_1
        stop ambience fadeout 1
        scene bg int_house_of_mt_day
        show unblink
        with fade
        pause(1)
        play ambience ambience_int_cabin_day fadein 1
        "I went into the house, and, as I was, fell on the bed, threw my legs on the metal back and stared at the ceiling."
    th "W-well. Hm, maybe my problem is that I rush things too much? We know each other only for three days in the end."
    "..."
    th "However, in this regard, my dad once issued a pearl like «a girl decides whether she will give or not give in the first minutes of communication»."
    th "Rough, but generally true. So it's not about timing."
    th "And not about Lena."
    th "{i}And not about my retardation{/i} — That's a surprise — {i}even not about that!{/i}"
    dreamgirl "What then? If isn't in that you put her before the fact that you don't need her friendship and it's impossible at all? And didn't offer anything in return."
    dreamgirl "You were afraid to tell her what you think - about her, about you, about everything in general."
    th "Oh, don't start it please? In my memory, many novels have been ruined by inappropriate confession."
    th "People have fun together, it's easy, they are friends of souls and organisms - why spoil the perfect picture with romantic nonsense?"
    dreamgirl "You yourself said that here are not adults and cynical aunts of your age, but children. Only adults can afford to be friends with organisms appropriately and burdenlessly - who are too infantile to turn to their family, but they already itch in the right places ."
    dreamgirl "And children tend to dream. About romance, pure feelings and moonlit nights so that everything inside breaks with cold and delight."
    dreamgirl "No one is forcing you to go to her with a marriage proposal, but at least you must act honestly and confess your sympathy."
    show blinking
    play music music_list["torture"] fadein 5
    "Shut up, inner voice. I will decide myself what and to whom I owe."
    with dissolve
    "Insensibly to myself, I, again, fell into a dream."
    scene cg d3_fag_room_7dl
    show prologue_dream
    with fade2
    "I dreamed again of my lair, dark and gloomy, illuminated only by the light of the monitor."
    scene cg d3_fag_room_7dl:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 2.0 zoom 1.5 xalign 0.5 yalign 0.35
    show prologue_dream
    "In the tray, the text message icon was glowing orange."
    "I opened Skype and seemed to continue the conversation, which did not end at all."
    scene cg d3_fag_room_7dl:
        zoom 1.5 xalign 0.5 yalign 0.35
        linear 8.0 zoom 3.0 xalign 0.4 yalign 0.15
    show prologue_dream
    "Have you tried anything at all?"
    "You were confronted with the fact again, and you fell on your back, showed everyone your belly with shouts like «Surrender»?"
    "You love to argue so much! You broke thousands of peaks for reasons far less compelling. What happened? You chickened out?"
    "You could do the elementary thing - say that it's all nonsense. That all the models that worked before you don't work with you."
    "Could, in the end, just ignore everything that was said and continue to dig in the right direction."
    "You don't care that much?"
    "So careless?"
    if alt_day2_us_escape:
        "The gates are open. Get out."
    else:
        "So the train runs every day... Get in and get out of here."
    stop music fadeout 3
    dreamgirl "Do you want to... Do you want to wake up here and now?"
    dreamgirl "You'll wake up completely at home, in your apartment, in front of this very monitor."
    "Awakening in three… {w}two…"
    menu:
        "Wake up":
            $ alt_day_catapult = True
            scene black
            $ prolog_time()
            if herc:
                play music "<to 52.94>" + music_7dl["herc_death"] fadein 5
                "The past is a gaping wound."
                "Your only hope for salvation is to turn around and meet it face to face."
                "But it's like kissing the lips of your dead lover."
                "They are cold and hide an icy darkness within them."
                scene bg int_store_7dl with fade
                "We agree to die for the sake of those we love, for the sake of those who can live after us."
                "What am I dying for?"
                play sound sfx_7dl["makarych"] fadein 0
                "The bullet, which began its journey three days ago, has finally arrived at its destination."
                scene black with fade
                "It's been a long and wonderful journey."
                "With a length of three days of summer."
                play sound sfx_bodyfall_1
                "For a person who does not even have anything to flash before his eyes on the doorstep to non-existence."
                stop sound_loop fadeout 0
                play sound sfx_7dl["aunl"]
                $ sdl_persistent_inc("alt_deep")
                show acm_logo_va_deep with moveinright:
                    pos (1600, 1020)
                pause(7.4)
                scene black
                show gameover
                with gopr
                with vpunch
                return
            elif loki:
                play music "<to 52.94>" + music_7dl["herc_death"] fadein 5
                "Hatred is measured by the amount of anger and rage."
                "You can turn away and run from the past, but it always catches up with you."
                "And the only chance is to hide inside one of the respite from the inevitable."
                "Pretend to be frozen in stasis."
                scene bg ext_winterpark_7dl with dissolve
                pause(1)
                show spill_red
                "But the sweetest illusion does not negate the nightmarish truth."
                "One day you will die too."
                "Consciousness floats in muddy water, painfully pounding against the walls of the vessel, rushes out, cries with blood and delirium."
                scene black with fade
                "And the strength that should have remained in order to at lest get onto the path where at least someone will be able to find me..."
                "I don't have it."
                play sound sfx_bodyfall_1
                "They all went into creating a colorful, voluminous illusion of a summer where I've never been before."
                stop sound_loop fadeout 0
                play sound sfx_7dl["aunl"]
                $ sdl_persistent_inc("alt_deep")
                show acm_logo_va_deep with moveinright:
                    pos (1600, 1020)
                pause(7.4)
                scene black
                show gameover
                with gopr
                with vpunch
                return
            else:
                "The broken psyche could no longer withstand the stress."
                "And when at least something stable appeared on the horizon, I desperately rushed there."
                scene anim prolog_1 with fade
                $ volume(0.5, 'music')
                play music music_list["lightness_radio_bus"] fadein 7
                "And he opened my eyes in the bus No.410."
                scene bg intro_xx with flash
                stop ambience fadeout 2
                play sound_loop sfx_bus_interior_moving fadein 4
                scene bg black with fade
                "Only to have time to see how the colossal bus hovers over the edge of the abyss, tears the metal of the barriers like tissue paper."
                "To see how we are dragged forward, scattering the cars we meet along the way like toy models."
                "And how an endless one and a half seconds of weightlessness later, we sideways hit the surface of dirty black water."
                play sound sfx_water_emerge
                $ sdl_persistent_inc("alt_deep")
                show acm_logo_va_deep with moveinright:
                pause(3)
                scene black
                show gameover
                with gopr
                return
        "Do not wake up":
            me "No. No? No!"
            stop ambience fadeout 1
            scene bg int_house_of_mt_day with dissolve
            with fade
            pause(1)
            play ambience ambience_int_cabin_night fadein 1
            "I jumped up on the bed, clutching at the air with my hands. I was scared to death."
    "And suddenly I realized that I had already become a part of this place."
    "Even if it will not work out with Alisa, I belong to the local «here» and «now». I like it here! And I don't want to leave this palce and I don't intend to."
    "But still, it's better to work out though."
    "I decided to find the girl and explain everything to her."
    play sound sfx_7dl["eat_horn"] fadein 1
    "Unfortunately, my plans were not destined to be fulfilled - I heard a horn signal from the outside and grabbed my head."
    if alt_day3_duty:
        th "Ulyana will kill me! I'm late for duty!"
    else:
        th "Wow, I was asleep for too long! And I have a lot more things to do!"
    "As I went outside rubbing my rumpled face and trying to straighten out the folds of the uniform a little, I rushed towards the canteen."
    stop sound fadeout 3
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_un_fz_dream:
    scene bg ext_square_sunset3_7dl with dissolve
    "We decorated the square in just twenty minutes."
    if alt_day3_un_fz_work == 'un':
        "Slavya let Lena go - the task remained trifling, and the two of us were quite enough to complete it."
    elif alt_day3_un_fz_work == 'dv':
        "Slavya let Alisa go - the task remained trifling, and the two of us were quite enough to complete it."
    "I dragged the ladder from tree to tree and threw the garland supplied by Slavya onto the branches."
    "It must be looking good at night."
    show sl smile pioneer with dissolve
    sl "Thank you for your help!"
    "I just shrugged."
    sl "What are you planning to do now?"
    me "I'm going to lie down. Somehow I couldn't manage to do this during the quiet hour."
    "Slavya nodded."
    show sl normal pioneer with dspr
    sl "Good. I'll report to Olga Dmitrievna that we're done."
    "She nodded towards the ladder."
    sl "Put it behind the fire shield, please."
    sl "It makes no sense to carry the ladder to the warehouse - anyway, after the disco, the garlands needs to be removed."
    hide sl with dissolve
    "The activist left and I grabbed the ladder again."
    "Thoughts in my head were lazily sticking together into a mess. For some reason my mood got worse."
    "It would seem that today was so rich in events that I simply did not have time to indulge in melancholy."
    "And now I was too exhausted physically to mourn my plight with due diligence."
    "But I did not feel the joy and satisfaction due to me for all my today's labors."
    "I trudged to the cabin with the firm intention of sleeping."
    scene bg ext_house_of_mt_sunset with dissolve
    "To hell with dinner, to hell with the disco."
    "From the excess of impressions, I was almost physically sick, and I just wanted to climb into a corner where no one would touch me."
    "Turn off your head and heart for a little while."
    play sound sfx_close_door_1
    scene bg int_house_of_mt_sunset with dissolve
    "Olga was not in the cabin, and I collapsed on the bed, burying my face in a cool pillow."
    "Breathed noisily: it smelled of the sun, grass and light dampness, so characteristic of wooden houses."
    th "No doubt than after each session, the bed linen is taken outside to air out."
    th "Good disinfection method, though!"
    "However, I was not squeamish. It's better not to think about party-owned things - to whom they belonged before you."
    "And about people too."
    if alt_day3_un_fz_work == 'sl':
        "Here Lena, for example, mixed me in her head with some of her acquaintances, attributing to me all the sins thereof."
        "And now I have to wash off what I did not do."
    "With these thoughts, I fell asleep."
    stop music fadeout 3
    with fade2
    scene black with fade
    pause(3)
    if (counter_un_fz_old_road == 2):
        call alt_day3_un_fz_dream_road
    else:
        call alt_day3_un_fz_dream_un
    scene black with fade
    pause(2)
    play sound sfx_7dl["eat_horn"] fadein 1
    pause(1)
    scene bg int_house_of_mt_sunset with fade
    play ambience ambience_int_cabin_evening fadein 2
    "I was awakened by the sound of a horn calling for dinner."
    "For the first few moments I struggled to understand where I was, and then abruptly jumped out of bed."
    me "What a dream that was!"
    "I shook my head, clearing all remnants of the strange dream from my thoughts."
    "My stomach growled."
    play sound sfx_close_door_1
    scene bg ext_house_of_mt_sunset
    show mt surprise pioneer
    with dissolve
    play ambience ambience_camp_center_evening fadein 1
    "Leaving the house, I ran into Olga Dmitrievna."
    mt "I've been looking for you all over the camp! What were you doing here?"
    me "Sleeping."
    "Honestly I confessed."
    show mt angry pioneer with dspr
    pause(1)
    show mt smile pioneer with dspr
    "Olga frowned, but then waved her hand."
    mt "Go eat already, sleepyhead!"
    "She slipped past me into the house, and I shrugged my shoulders and moved towards the canteen."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day3_un_fz_dream_road:
    play music music_7dl["devastated"] fadein 3
    scene bg ext_path2_day
    show prologue_dream
    with dissolve
    $ counter_un_fz_dream_road += 1
    "...Can't run anymore!"
    am "Why me?! Why?!"
    "Sharp grass hurts the legs."
    "One shoe is lost, but I can't turn around and go after it."
    "Because they will kill me. They will laugh at me, mock me."
    "And if anyone intercedes, - and the squad leader definitely will- they will make fun of me."
    "Because I'm different."
    scene bg ext_sandpit_day_7dl
    show prologue_dream
    with dissolve
    "The path underfoot gives way to sand."
    "Strength finally leaves me, and I fall on dry clay."
    "Painfully."
    "Sobs come out of my chest against my will."
    "Yes, and from whom to hide them here?"
    am "Why?"
    "I hate them, I hate them even more than my parents."
    "And why this stupid camp?"
    "If they wanted to get rid of me so much, they could send me to the sea. To Artek."
    "To people like me, and not to these embittered, beggarly ragamuffins, ready to attack in a pack on anyone who is even a little different from them."
    am "I hate you, do you hear? I hate you all!"
    "I won't leave here.{w} I won't leave until I starve to death here.{w} Let them search with helicopters."
    "I used to think that I had everything I could wish for, but now I understand that my only dream is impossible."
    "Become normal. An ordinary boy from an ordinary family. Like the one who beat me up."
    "The sobs begin to choke me again."
    am "{b}WHY?!{\b}" with vpunch
    stop music fadeout 3
    return

label alt_day3_un_fz_dream_un:
    play music music_7dl["devastated"] fadein 3
    scene bg int_mt_sam_room_away_7dl
    show prologue_dream
    with dissolve
    $ counter_un_fz_dream_un += 1
    "Without much interest I leaf through a magazine that I found on the shelf."
    "Olga is sitting on the bed at my feet."
    "The phone rings in the hallway and she leaves."
    "Comes back in a few minutes. She's shaking."
    show mt scared dress2 behind prologue_dream with dissolve
    mt "This is a nightmare."
    hide mt with dissolve
    "She falls on the bed and drops her face into her hands."
    "A sticky fear wraps around my throat, preventing me from breathing."
    mt "She cut her veins. Can you believe it? Because of us!"
    "Her voice breaks into a squeal, and I can't even move to hug Olka."
    "My throat is dry."
    am "She… she…"
    mt "Alive."
    "She exhales through sobs."
    mt "In the hospital. But alive."
    "I finally hug her. {w} Silence."
    "Olga is crying at the top of her voice."
    show mt scared dress2 behind prologue_dream with dissolve
    mt "I have to come for interrogation tomorrow."
    am "Me too?"
    mt "I don't know. Only if she told about..."
    "She leans into my shoulder."
    mt "What have we done?"
    am "She did it herself. We have nothing to do with it, Olya."
    "I say it out loud because I want to believe it myself."
    am "It's not our fault."
    stop music fadeout 3
    return

label alt_day3_supper1:
    scene bg int_dining_hall_people_day with fade2
    with dissolve
    play ambience ambience_dining_hall_full fadein 2
    play music music_list["afterword"] fadein 3
    if alt_day3_duty:
        show us laugh sport at left with dissolve
        "She was already rushing with a cart between the tables and gave me a sidelong glance."
        us "Slacker."
        "That's all she said."
        "Swallowed. What else was left for me? {w}Slacker I am."
        "I quickly rinsed my hands and, grabbing another cart, started serving tables from the other side."
        "I had to serve the already seated pioneers, so I had no time for conversations - had to rush like a shuttle - back and forth."
        "Ten walks, maybe a little more - enough to cover almost all the junior squads."
        show us grin sport at left with dspr
        us "I knew that you would break loose in the evening."
        "The little one winked."
        me "Why?"
        us "Isn't it obvious? Because I was going to, too."
        show us laugh sport with dspr
        "She laughed at my dumbfounded face."
        me "And who would be on duty then?"
        us "That's what I thought. {w}You can't be trusted with anything, not even arranging the plates. {w}I had to take it upon myself and save the situation."
        "It was she who was definitely quoting someone now. But who? The quote is already very familiar."
        hide us with dissolve
        stop ambience fadeout 2
        scene bg int_dining_hall_people_day with dissolve
        play ambience ambience_dining_hall_full fadein 3
    "Alisa didn't come, I had to sit next to Ulyana."
    "All the time of dinner, her place was empty, and like a ill tooth, it constantly attracted attention."
    "I looked there probably ten times before I noticed Olga Dmitrievna marking the arriving pioneers."
    show mt normal pioneer at right with dissolve
    me "Good evening. What about Alisa? Still not back from the infirmary?"
    mt "No, she just has indigestion. The doctor prescribed a pill and forbade her to come to dinner."
    un "Alisa?"
    show un surprise pioneer at left with dissolve
    "Lena turned around in surprise."
    un "But I just…"
    show mt angry pioneer at center with moveinleft
    "After the squad leader's glance, information seems to have died right in the girl's throat."
    "I also didn't dare to clarify and hurried to finish dinner as quickly as possible."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_un_fz_dinner:
    scene bg int_dining_hall_people_sunset_7dl with dissolve
    play ambience ambience_dining_hall_full fadein 2
    play music music_list["your_bright_side"] fadein 2
    "When I entered canteen, the pioneers were already banging their spoons with might and main, talking loudly."
    "I grimaced: the canteen was by no means the quietest place in the camp, but this was the first time I had seen such bedlam."
    "Lena was sitting in the corner by the window."
    "The place opposite her was occupied by the buzzkill, so idea of ​​sitting next to the girl had to be discarded."
    "We made eye contact."
    "Lena looked worried, and as soon as she noticed me, she looked away."
    "It even seemed to me that she was looking at the librarian with some annoyance."
    th "We still haven't talked to each other about yesterday."
    dreamgirl "You shut her up yourself, forgot? Now guess what's on her mind."
    "The inner interlocutor did not even try to hide the malice with which his words oozed."
    "After all, Lena wasn't mad at me - that was obvious."
    if alt_day3_un_fz_work == 'un':
        "I couldn't explain why she threw herself on my neck otherwise."
    else:
        "Although these vague hints of those around me definitely strained me."
    show us normal sport with dissolve
    "I sat down with Ulyana, specially arranged at the table so that Lena fell into my field of vision."
    show un shy pioneer far at fleft with dissolve
    "We stared at each other for a moment again, and the girl blushed, pretending to examining something above my head."
    hide un with vpunch
    us "Are you going to dance?"
    me "Huh?"
    "Ulyana distracted me from watching Lena by kicking me under the table."
    show us grin sport with dspr
    us "Hey! Are you going to the disco?"
    me "Yeah. Just let me iron my tuxedo."
    us "Hey, I'm serious!"
    me "Do you think I'm kidding?"
    show us normal sport with dspr
    me "Have you ever seen a self-respecting gentleman without a tuxedo at a ball"
    "Ulyana just fluttered her eyes in confusion."
    me "That's right."
    show us smile sport with dspr
    "The girl squinted slyly."
    us "If you can't find a tuxedo - I have a great idea for how you can brighten up your leisure time!"
    me "Whom do you want to rob this time?"
    show us dontlike sport with dspr
    us "Come on!"
    "She began to get angry."
    if alt_day3_un_fz_work == 'dv':
        us "I, by the way, want to return the debt. For help with Katyusha."
    else:
        us "I've promised to explain why I needed a knife."
    me "Wow!"
    me "So what, you'll just take it like this and tell me everything?"
    "Ulyana laughed."
    show us grin sport with dspr
    us "Of course not! That would be too easy!"
    show us smile sport with dspr
    us "Instead of the dances, come to the stage tonight if you wish."
    us "We're going to tell stories."
    "Sounded surprisingly enticing."
    "Anything is better than jumping around the square to the music."
    show un sad pioneer far at fleft with dissolve
    "And then I picked out Lena with my eyes again. {w} She looked at me in bewilderment."
    th "Why does that look bother me so much?"
    hide un with dissolve
    "If you think about it, my tactics of communicating with Lena drastically changed since morning."
    "Then I was firmly convinced that I should stay away from her, because she can not stand me."
    "Right now, I had absolutely no idea what to do with her."
    th "She'll see a hole in me."
    "No, in the morning I, of course, was stupid."
    "So shrugging off the conversation when the girl was ready for it was the highest faux pas on my part."
    "Maybe she was going to explain why she acted so strangely?"
    th "I can't sleep until I know."
    me "I'll think about it."
    show us grin sport with dspr
    us "That's good!"
    hide us with dissolve
    "Ulyana wanted to jump out from behind the table, leaving her plates on me, but I beat her to it."
    "Chuckling to myself, I went to take my tray to the sink, feeling like a winner in this war."
    th "Though something tells me that only the first battle has been won."
    th "The real war is yet to come!"
    "Ulyana grumbled something with displeasure, scurrying after me with her rattling tray."
    th "The main thing is that there is no catch in her evening's undertaking."
    pause(1)
    stop ambience fadeout 2
    scene bg ext_dining_hall_near_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 1
    "There was about half an hour left before the disco, and with nothing to do, I trudged into the cabin."
    "I didn’t have anything to change into, and I didn’t see the point in it - in front of who should I flaunt?"
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day3_un_fz_dance:
    scene anim_square_party with dissolve
    play music music_list["lightness"] fadein 3
    "I sat down on the bench, looking around."
    "The area really looked good - apparently, our efforts were not in vain."
    "People actively gathered, but there were few who wanted to dance. Nobody wanted to start first, afraid to look stupid."
    "Out of the corner of my eye, I noticed how the girls from the junior squad were looking at me, whispering about something."
    "Having caught my eye, the girls jumped and fled somewhere to another corner of the square."
    th "As if they have nothing else to do!"
    dreamgirl "Would you take a closer look at them, slow-witted! You see how they attract your attention?"
    dreamgirl "And dressed up in dresses. Well, just a feast for the eyes!"
    th "Do you think I look like a fan of snotty eighth graders?"
    th "No, let them go and fool Syroezhka instead."
    th "He would've like this."
    show ka laugh dress at right
    show al sad pioneer at center
    with dissolve
    if alt_day3_un_fz_work == 'dv':
        "But Katyushka did not falter - she forcibly pulled one of her pioneers onto the dance floor, laughing fervently."
        "The boy seemed ready to fall through the ground, but this technique worked: the rest of the pioneers joined the dancers."
    else:
        "Meanwhile, a leader from another squad forcibly dragged one of the junior pioneers onto the dance floor, laughing fervently."
        "It definitely broke the ice that bound the rest - the children began to dance, forgetting about past embarrassment."
    hide ka
    hide al
    with dissolve
    th "Thank God Olga does not practice such pedagogical methods!"
    "I looked out for Lena among the dancers, but it seems that she was not at the square."
    "I clenched my fists in annoyance: and why, one wonders, did I drag myself here?"
    "We should have stuck to the original plan and hide somewhere in the bushes."
    "Get alcohol from the infirmary, dilute kompot from the cafeteria, and spend a fine evening in the pleasant company of your split personality."
    dreamgirl "Do you really think so well of me? I'm flattered!"
    th "No, that was a joke. Shut up."
    show sl normal dress close with dissolve
    sl "Don't like dancing?"
    "Slavya sat on the bench next to me."
    me "Uh-huh. Listen, have you seen Lena?"
    show sl serious dress close with dspr
    "The girl get worried."
    sl "She's around here somewhere. Why would you?"
    th "None of your freaking business, dear."
    me "Does it matter?"
    show sl normal dress close with dspr
    sl "No, but..."
    if alt_day3_un_fz_work == 'sl':
        sl "I told you, you remind her of an old friend."
        sl "Anyway, doesn't matter."
    sl "I think if she wants to dance with you, she'll let you know."
    "I started to boil."
    "I certainly did not order family psychotherapy."
    me "I don't want to dance with her!"
    show sl surprise dress close with dspr
    "Slavya recoiled, staring at me in astonishment."
    me "I'm not going to dance with anyone at all. I need to talk to her."
    show sl sad dress with dspr
    "The girl sighed and rose from the bench."
    sl "She's over there in that corner."
    hide sl with dissolve
    "And she left, dissolving again on the dance floor."
    "She looked drooped."
    th "And rightly so. Don't stick your nose in other people's business."
    show un sad dress far at right with dissolve
    "Lena really stood by the tree where Slavya pointed."
    "She looked out for someone among the dancers, fingering the folds of her dress."
    show un surprise dress far at right with dspr
    "And I was hardly surprised when she almost jumped when she saw me."
    th "She was waiting for me, huh. Well then."
    th "Things turned out much worse than I thought."
    show un shy dress at center with dissolve
    me "Hi."
    me "Nice dress."
    "Why do I start with these trifling compliments?"
    "I should shut up and leave, but it's better to immediately blurt out what I can't convey to her since last night."
    "Just tell her that, and forever cross out all the looks she throws at you."
    "Kill her pride now so you don't break her heart later."
    un "Thank you."
    th "That was a nice conversation."
    me "Don't like dances?"
    un "Why? I like it."
    un "I just don't want to dance."
    stop music fadeout 6
    me "Likewise."
    show un smile dress with dspr
    "Lena smiled shyly at my intonation, imitating the Chief from the cartoon about Koloboks."
    dreamgirl "Did you come to entertain her or talk to her?"
    play music music_7dl["shape_of_my_heart"] fadein 4
    show un shy dress with dspr
    "I didn't even have time to open my mouth, as the composition, sounding from the speakers, changed to a smooth melody."
    th "Slowey! Everyone jump into the nearest trench!"
    "But there were no trenches nearby."
    "Only Lena, who froze, timidly looking at me."
    th "That's what they call «getting stuck». What should I do now?"
    "Lena was obviously waiting for an invitation to dance."
    "Yes, but the dance was not part of my plans for Lena in any way - the situation was already deplorable."
    menu:
        "Suggest a walk":
            $ counter_un_fz_un_route += 1
            $ alt_day3_un_fz_walk = True
            me "If you don't want to dance - let's go for a walk?"
            "Lena shrugged her shoulders in confusion."
            un "Okay."
            "And we left the square, trying not to draw too much attention to ourselves."
            stop music fadeout 4
        "Call to hang out with Ulyana":
            $ counter_un_fz_old_road += 1
            $ alt_day3_un_fz_stories = True
            me "You know, I was invited to an interesting event today..."
            show un normal dress with dspr
            un "Alisa?"
            "Somehow too sharply Lena blurted out."
            me "Well, why Alisa?"
            th "Are there no other people in this camp?"
            me "You like mysteries, don't you?"
            un "All people are curious by nature."
            "Somehow the girl shrugged her shoulders vaguely."
            me "Then let's go, something interesting is waiting for us."
            th "Wish I knew what exactly…"
            show un serious dress with dspr
            un "Are you sure I'd be welcome where you invite me?"
            "I didn't know that either, but I waved my hand with confidence."
            me "Oh they will be! Let's go already, otherwise we'll miss everything."
            "And we quietly slipped away from the square into the darkness."
            stop music fadeout 4
        "Invite to dance":
            $ alt_day3_un_fz_neu_transit = True
    return

label alt_day3_un_fz_evening_walk:
    scene bg ext_boathouse_alt_night_7dl
    show un smile dress
    with dissolve2
    play ambience ambience_boat_station_night fadein 2
    play music music_7dl["dance_with_me_piano"] fadein 2
    "The path we chose led us to the pier."
    "I sat down on the walkway, gesturing for the girl to sit next to me."
    "It was kind of weird."
    "A quiet splash of water, echoes of music coming from the square, the light of the moon, a girl nearby - and no romance."
    "It just wasn't there, that's all."
    th "Apparently, I'm getting too old for this. You won't get through me with this."
    th "Here it is, your happiness, at a distance of the width of two palms - take it."
    th "But I don't need it, this happiness."
    th "And she doesn't need to either."
    th "But she doesn't know about it yet."
    me "Tell me, Lena, do you have a dream?"
    show un normal dress with dspr
    un "Are you sure you want to know about it?"
    me "No. I'm pretty sure I don't."
    me "I didn't ask for details, but for availability."
    show un smile dress with dspr
    un "Every person has it."
    "Lena smiled shyly."
    un "Isn't they?"
    show blink
    "I closed my eyes, letting the mysterious night sounds fill all the space in my head."
    "It allowed the words to flow without my knowledge, without overloading them with inappropriate seriousness."
    th "Is it possible to talk to her seriously? Guess she got all the stupid things in her mind."
    th "At least I'm comfortable with believing she has."
    $ volume(0.1, "sound")
    me "I don't have one."
    play sound sfx_water_emerge
    "A quiet splash was heard - Lena lowered her legs into the water."
    me "The water is cold here. You'll catch a cold."
    $ volume(1.0, "sound")
    un "What's the difference? If I'll catch a cold, If I won't catch a cold - no one in the camp will care about that."
    un "Maybe Viola'll scold, that's it."
    me "Do you live for yourself or for others?"
    scene bg ext_boathouse_alt_night_7dl
    show un smile dress close
    show unblink
    with dissolve
    "I opened my eyes and looked at Lena."
    "Her face was so close that I could feel the girl's uneven breath on my cheek."
    th "Stupid. Small and stupid."
    th "Nothing better than Ulyanka."
    un "To be honest, I don't even know what I'm living for."
    if alt_day3_un_fz_work == 'un':
        me "But what about those opportunities that you decided not to miss from now on?"
        un "I'm trying. But I'm not ten years old anymore to believe in fairy tales."
        un "And I understand very well that not everything in this world depends on me."
    pause(1)
    stop music fadeout 9
    me "Do you want another fairy tale?"
    scene stars with dissolve2
    "I lay down on the walkway with my hands behind my head."
    "Lena, after hesitating a bit, lay down next to me."
    "My outstretched elbows kept her from getting too close to me."
    "The girl put her hands on her stomach and turned her head towards me."
    un "Just not too sad."
    "I chuckled."
    me "The saddest part of any fairy tale is that what happens in it turns out to be just fiction."
    me "My... father told me this story when I was eight."
    play music music_7dl["unforgotten"] fadein 2
    pause(1)
    $ set_mode_nvl()
    "There are dreams that will never come true."
    "If you dream of becoming fabulously rich, then there is a one in a million chance that you will succeed."
    "If you want to win the love of a person, then one day fate will give you a sign. Or send a new love."
    "Power, connections, public adoration - these things just seem unrealizable. In reality, it's just that not everyone uses their chance to get them."
    "Another thing is dreams that have no place in this world. To return long-gone loved ones. To correct the past. To grow up as a different person."
    "For such, a fate does not give any chance."
    "But there are worlds that are like ours, like two peas in a pod. Worlds where the course of history went differently, and those things that are impossible here are quite real there."
    "And if you desire something that is present in other worlds strongly enough, then you will definitely find The Road leading to your dream."
    pause(1)
    $ set_mode_adv()
    scene bg ext_boathouse_alt_night_7dl
    show un sad dress close
    with fade
    un "But how one can find it?"
    "Lena whispered."
    "She froze as she listened to my story and hardly breathed. She hung on every word greedily."
    me "By launching The Flare."
    me "One Flare has little power, but when there are many, they can show you the way."
    un "And you tried?"
    un "Did you look for this Road?"
    me "No."
    me "When I believed it, I didn't need anything that I couldn't get in my world."
    me "And when my dreams became unrealizable, I stopped believing."
    un "And that's why you don't have a dream anymore?"
    me "Yes."
    "She looked into my eyes with such hope that I had to struggle not to look away."
    th "I'm ashamed. I'm madly ashamed in front of you, you know?"
    th "I came here with you to ask you to put all the stupid things about me out of your head, but instead I fill it with new ones."
    me "But that doesn't mean I don't want anything."
    un "And what do you want?"
    me "I want you to smile."
    me "So that you don't think about things you can't influence.{w} Live at last."
    me "And didn't try to look for depth where there isn't any."
    show un cry_smile dress close with dspr
    un "But if I don't care about depth? If I don't want to know what's really behind the shell?"
    un "It's self-deception, I know. But it allows me to not feel the pain that has almost grown into my skin for many months."
    show un cry dress close with dspr
    "A tear rolled down the girl's cheek, hanging like a silver bead on the tip of her nose."
    "I reached out and gently rubbed it with my thumb."
    me "Don't let anyone fool you.{w} Especially yourself.{w} It hurts a hundred times."
    me "Living a lie just seems like a no-brainer."
    me "In fact, you will always see the truth in everything that surrounds you."
    me "And it will painfully scratch your cozy cocoon of self-hypnosis and outright deceit, and one day it will completely tear it apart."
    me "And all of it's thorns will pierce you at once, forever destroying any belief in anything good."
    me "After this, one ceases to trust one's own shadow."
    hide un with dissolve
    "Lena closed her eyes."
    "I really wanted to feel sorry for this poor stupid girl, from whom a cruel adult takes away - by force - her faith in a miracle, forcing her to contemplate a disgusting, unbearable reality."
    "Hug, caress, console. But I just can't comfort her like that."
    "She'll misunderstand."
    "Only thing is left, is to continue to convince the girl that miracles do not happen."
    show un cry_smile dress close with dissolve
    un "There are many things I would like to change."
    un "Fix things that never depended on me."
    show un angry2 dress close with dspr
    un "Then why can't I find the damn Road?{w} My desires aren't strong enough?"
    un "I lost three people close to me. It wasn't my fault."
    me "Because it's a fairy tale, Lena."
    me "A stupid story my stepdad used to tell me when my mom was sick and I was afraid she was going to die."
    show un normal dress close with dspr
    un "Stepdad?"
    th "That didn't go well."
    th "I shouldn't have lied to her."
    me "As you can see, each of us was left by loved ones."
    "I smiled bitterly."
    me "But these are natural things that need to be endured."
    me "You can't regret all your life about something that didn't come true or about something that was irretrievably lost."
    me "You need to find the strength in yourself and just live."
    show un cry_smile dress close with dspr
    un "And to smile?"
    "Her lips trembled."
    me "And smile."
    scene stars with dissolve
    "I turned away and looked up at the night sky."
    "Away from the light sources on earth, the stars seemed particularly bright. Inviting."
    "It was as if they were those guiding Flares that winked at us from the depths, as if trying to say:"
    "{i}Everything you're looking for is already there. You're just looking in the wrong place.{/i}"
    "{i}Stupid, stupid people. In the endless pursuit of happiness, you never find it.{/i}"
    "{i}And we are just observers who are not allowed to meddle in your petty affairs.{/i}"
    "Lena's head was close, very close to mine."
    "But the girl's thoughts hovered somewhere far away, where fairy tales still exist, and grumpy old Semyon is not able to get to them and convict them of lies."
    "Your whole life is a lie. But your lies are naive, while mine are straightforward and rude."
    "I can see right through mine."
    "And you almost believed in yours."
    stop music fadeout 7
    scene bg ext_boathouse_alt_night_7dl
    with fade2
    "We lay in silence."
    "All sounds have died down - it seems that the dances are over."
    "Which meant we had to go."
    "It was a pity to destroy this fragile moment of balance. {w} It was terrible to think about what awaited us tomorrow."
    "But all the charm of such charming evenings was precisely in their transience."
    show un sad dress close with dissolve
    me "Let's go, let's go. Lights out soon."
    un "Yes..."
    "I got up from the bridge and held out my hand to the girl.{w} She took it hesitantly."
    with fade
    scene bg ext_houses_night_7dl
    show un normal dress close
    with dissolve
    play music music_7dl["take_my_hand"] fadein 3
    play ambience ambience_camp_center_night fadein 3
    "From the pier we came to a footpath."
    un "You know, I understand that you said all this just because you wanted to console me, but…"
    me "Not at all."
    me "I really want you to feel better."
    me "Because I'm just like you."
    "Lena stopped."
    show un smile dress close with dspr
    un "Not true.{w} You are strong."
    un "I wish I could think like you."
    un "And the main thing is to believe in it like you."
    me "You can do it."
    me "I know you can believe anything."
    me "If you don't want to believe in yourself, believe in me.{w} And I'll definitely teach you."
    scene bg ext_house_of_un_night_7dl with dissolve
    "I accompanied Lena to her house."
    show un sad dress with dissolve
    "In parting, she gave me a sad look."
    me "Are you going to lose heart again?"
    show un smile dress with dspr
    "Lena smiled."
    un "No. Now I won't."
    show un smile dress far with dissolve
    "She went up to the porch."
    show un laugh dress far with dspr
    un "Honest Pioneer!"
    me "Good night."
    show un smile dress far with dspr
    un "Good..."
    hide un with dissolve
    "She disappeared behind the door, cutting off the end of her sentence."
    "Perhaps she added something else? {w} That I was never to know."
    stop music fadeout 2
    stop ambience fadeout 2
    with fade
    return

label alt_day3_un_fz_evening_stories:
    scene bg ext_houses_night_7dl with dissolve
    "On our way, Lena did not ask questions, although I almost physically felt how she was bursting with curiosity."
    scene bg ext_stage_normal_night with dissolve
    play ambience ambience_camp_center_evening fadein 2
    play music music_list["goodbye_home_shores"] fadein 3
    "Finally we got to the stage."
    show un normal dress with dissolve
    un "And where are those who are waiting for you?"
    "That would have sounded like a mockery if there wasn't so much anxiety in her voice."
    th "Is she afraid that I'll rape her here?"
    dreamgirl "Quite the opposite. Afraid you won't."
    me "Calm. Secrets never lie on the surface."
    hide un with dissolve
    "I moved along the stage, and Lena had no choice but to follow me."
    "The grass rustled underfoot, and the sounds from the square were almost lost in the chatter of nocturnal insects."
    "It was definitely one of the things that made me love the nights so much. The special silence of the night."
    "Not a total lack of sound, but heightened background noises that don't make you feel so alone."
    show us laugh sport with vpunch
    us "Boo!"
    "Satisfied Ulyana jumped out from around the corner."
    play sound sfx_bodyfall_1
    hide us with vpunch
    "Unfortunately, my reflexes played a trick on me: I myself did not understand how, with a deft grip, I knocked the girl over on her face into the grass, putting her right hand behind her back."
    us "Oi! What are you doing, you idiot?!"
    "Her luck that this body was not as nimble as my real one: I managed not to break anything for her."
    me "Don't scare me!"
    show us sad sport with dissolve
    "Ulyana jumped up and looked at me resentfully."
    "Her loyal bodyguards ran out at the noise, and their faces did not promise me anything good."
    hide us
    show al dontlike pioneer at center
    show tn normal pioneer at fright
    show dn normal pioneer at cright
    with dissolve
    dn "What happened?"
    hide al
    hide tn
    hide dn
    show us normal sport
    with dissolve
    us "Nothing."
    "Ulyana wiped her nose, soiled in the ground."
    us "I tripped."
    show un normal dress at fleft
    with dissolve
    "And then she noticed Lena, stomping around in indecision behind me."
    us "Did she forget something here?"
    show un shy dress at fleft with dspr
    un "No, I am... I'm leaving already."
    "I prudently grabbed her hand, and the girl flinched."
    th "Yeah, after such a scene, I would also be afraid that they would poke me in the face in the ground!"
    me "She's with me."
    me "Well, let's start our evening of amazing stories, shall we?"
    th "They have a lamp over there, just right."
    show dn upset pioneer at right with dissolve
    "Curly frowned."
    dn "You shouldn't have brought her."
    "Lena was even more embarrassed, trying to hide behind my back, but she didn't let go of my hand."
    me "Either we join you together, or we leave together.{w} Questions?"
    "Ulyana waved her hand."
    us "Settle down."
    scene bg ext_backstage_alt_night_7dl with dissolve
    "There was indeed a lamp by the door behind the stage.{w} An oil lamp."
    th "Not doubt that they also stole it somewhere. A rarity, after all!"
    "The boys sat down on the logs lying around here."
    "Ulyana settled down on a stump."
    "Lena and I occupied the remaining log."
    stop music fadeout 6
    "An awkward silence fell."
    pause(2)
    me "So, who will start?"
    dn "Tisha."
    "I carefully examined all the boys, trying to determine which of them is Tisha."
    show un normal dress at fleft with dissolve
    "But to my amazement, Lena spoke up."
    play music music_list["trapped_in_dreams"] fadein 2
    un "I've had strange dreams since last year."
    un "I see a city I've never been to. People in strange clothes that no one has ever worn."
    un "This city is full of neon lights, so cold I'm cowering for warmth."
    show un sad dress at fleft with dissolve
    un "But that doesn't help."
    un "In the eyes of the inhabitants of this city, too, neon."
    un "It burns right through me, reminding me that I'm a stranger in this city."
    un "I don't belong there."
    show un cry_smile dress at fleft with dspr
    un "And I'm trying to draw it, but I can't."
    show un normal dress at fleft with dspr
    un "There are no such bright colors to convey this neon."
    un "There is no such cold emptiness in our world that it can be portrayed."
    "Lena fell silent, looking at the light dancing in a kerosene lamp."
    th "My city in her drawing..."
    th "That explains a lot."
    th "But it raises more questions than it answers."
    show dn smile pioneer at cright with dissolve
    "Curly nodded approvingly."
    show dn normal pioneer at cright with dspr
    "Something so inexplicable flashed across his face, and I realized: he trusts us."
    "Not just Lena. {w} Both of us."
    dn "Now you, Ulyana."
    hide dn
    hide un
    show us normal sport at cleft
    with dissolve
    "The girl tilted her head to the side."
    us "There are some dreams that won't come true."
    us "Dreams of things that simply don't exist in our world."
    us "Things we've lost forever, things we never had."
    us "But they are by no means impossible. They have come true a long time ago.{w} But not here."
    me "They came true in worlds that are like two drops of water similar to ours."
    me "But the course of history in them went a little differently, and what was impossible here became an ordinary reality there."
    show al normal pioneer at center
    show tn normal pioneer at fright
    show dn surprise pioneer at cright
    show us surp2 sport at cleft
    show un surprise dress at fleft
    with dissolve
    "Five pairs of eyes stared at me in amazement."
    me "And if one's desire is strong enough, he can find The Road to these worlds."
    "This story was told to me by my stepfather a long time ago. Almost in a past life."
    "I believed in it when I was little, but then it was not useful to me."
    "I didn't have any wishes that couldn't be fulfilled."
    "Years passed, and the story was lost in memory, like slingshots and old books in a box that forever drove off to the country house."
    "And unfulfilled desires accumulated."
    "But the thing is, that faith in miracles, characteristic of naive childhood, is gone."
    "And what was then a trifling task, turned into anguish about how things could have turned out differently."
    "After all, at the age of eight, I knew exactly how to find The Road."
    show dn normal pioneer at cright
    show us normal sport at cleft
    show un normal dress at fleft
    with dspr
    us "In order to find it, one must launch a guiding Flare."
    me "One Flare has little power, but when there are many..."
    dn "...they will show the way."
    scene bg ext_backstage_alt_night_7dl with fade
    "No one asked me questions."
    "They didn't want to ruin the magic of this moment as much as I didn't want to."
    "After all, only here and now there is a fairy tale."
    "She's translucent, like morning mist over a river."
    "Blink, and she's gone."
    "Where there was that fog, routine life, far from fairy tale, boils and rings."
    "They are beautiful in their omnipotence."
    "There exists goodness and justice, and evil will always be punished."
    "But there are no good endings in real life."
    show us sad sport
    show dn normal pioneer at right
    with dissolve
    "Ulyana wanted to say something, but Curly put his hand on her tense fist."
    "We looked at each other."
    "This boy was not as simple as it might seem at first glance."
    "There was a secret in him, inaccessible to the townsfolk."
    hide us
    hide dn
    with dissolve
    "And these kids lived that mystery for as long as they had the chance."
    "After all, adult life has not yet taken away from them the right to believe in a fairy tale."
    "We are so different, but we all dream of finding our own way."
    "The path that is not chosen."
    "He finds you himself when the time comes."
    "Those kids have already set foot on it."
    "And Lena, it seems, too."
    stop music fadeout 2
    with fade
    scene bg ext_house_of_un_night_7dl with dissolve
    play music music_7dl["take_my_hand"] fadein 2
    "We walked silently to Lena's cabin."
    show un sad dress with dissolve
    un "Do you believe it?"
    "She asked, as if afraid of what she might hear in response."
    me "It doesn't matter.{w} What matters is whether or not you believe it."
    show un smile dress far with dissolve
    "She turned to me, standing on the porch."
    un "It will be easier for me to believe if I know that you don't think it's stupid."
    th "What you're talking about is called religion."
    me "Don't think about what others think."
    me "Find your path. Find the Flare that will guide you."
    me "Good night."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day3_un_fz_dance2:
    scene anim_square_party
    show un shy dress
    with dissolve
    th "So why are you looking at me like that?"
    th "You have no idea what kind of person I am."
    th "You only see me as the boy who so unexpectedly stirred up life in the camp just by his appearance."
    th "Could that be enough to fill your head with romantic nonsense on just the third day of dating?"
    "My momentary pause completely knocked me out."
    "To continue the conversation, as if nothing had happened, I was unable to."
    me "Uh…"
    th "That's it, now she definitely thinks I'm a cretin who hesitates to ask her to a dance because he's head over heels in love with her."
    dreamgirl "So take it and call her - it's ucanny how easy it is!"
    me "Shall we dance?"
    th "What the hell are you doing?"
    dreamgirl "I'm sorry, I hate to see you dumbying."
    dreamgirl "Come on by yourself."
    th "Well, you're a vile creature!"
    un "Okay..."
    "Lena stepped towards me in indecision, and I had no choice but to clumsily put my hands on her waist, shifting from foot to foot."
    "But quite unexpectedly, Lena clung to me, forcing me to sigh convulsively."
    scene cg d3_un_dance with dissolve
    "She hugged me like it was the last time."
    "She pressed her whole body, as if she was hoping to penetrate my skin."
    "My hands remained limply at her waist."
    "I didn't want to respond to that convulsive hug."
    "So strange and desperate, like she was afraid I was about to dissolve."
    "I distinctly felt her forms resting against my chest."
    "Her thighs pressed against my crotch. And her body responded treacherously well to these stimuli."
    "Lena's hands slid down my back, sending an electrical charge through my spine."
    "A dull growl stuck in my throat."
    "My body wanted Lena. {w} I didn't."
    "I was about to pull away, but I didn't have time."
    play music music_list["doomed_to_be_defeated"] fadein 3
    mt "What the hell are you two doing here?!"
    scene anim_square_party
    show mt angry dress at right
    show un sad dress close
    with dissolve
    "Olga jumped out like the devil out of a snuffbox, and just in time to catch us in this obscene pose."
    th "Well, coulnd't you find another moment?"
    "Lena shuddered, but didn't let me go."
    show un surprise dress with dissolve
    "I took her by the shoulders and gently pushed her away from me."
    me "We dance. It's a slow dance, isn't it?"
    show un sad dress with dspr
    mt "And {i}this{/i}..."
    "The squad leader grunted venomously."
    mt "...you call a dance?"
    me "Let's not get hysterical, Olga Dmitrievna."
    "My orderly tone was not to the liking of the squad leader."
    mt "How are you talking..."
    me "I'm a well-mannered person, in the end."
    me "The lady stood and missed without a gentleman - I invited."
    me "And there's no need for drama here."
    me "We will not run into the forest to indulge in love pleasures."
    "I looked expressively at both."
    me "Because there is nothing between us, whatever you see in our dance."
    stop music fadeout 1
    show un surprise dress
    show mt shocked dress at right
    with dspr
    pause(2)
    play music music_7dl["danceagain"] fadein 3
    th "At least they should both understand."
    th "One will spare me a lecture on sex education, and the other will save me my baseless sighs."
    th "It's rude, but it's much more correct than giving the girl false hopes."
    if alt_day3_un_fz_work == 'un':
        th "As if that scenery at the warehouse wasn't enough - Now she also climbing me in public."
        th "If a person does not understand non-verbal hints, then you need to speak directly."
    "Let her better take offense at me than later at herself, remembering whom she looked at with such adoration at her seventeen."
    "Even if I reciprocate, I won't bring you anything but disappointment, you stupid girl."
    "And you're lucky I didn't answer."
    show un cry dress with dspr
    "Lena turned pale, looking at me in fear."
    "She seemed unable to process what she heard."
    "I was ready for any outcome - for hysteria, for slaps in the face, for a loud scandal."
    hide un with moveoutleft
    "But what happened, I certainly did not expect: she took off - so quickly that I did not have time to say a word - and disappeared somewhere among the trees."
    "Olga and I looked after her dumbfounded."
    mt "Don't you think you're a bit over the top?"
    me "Don't you think you're not minding your own business?"
    "I turned angrily to the squad leader."
    me "I would have told her all this myself, without your kick. But only much softer and in a more suitable environment."
    show mt rage dress at right with dspr
    mt "You don't even know what are you talking about!"
    "She suddenly flared up."
    mt "We already had one incident last year that started out the same way."
    mt "Guess who was in it?"
    show mt angry dress at right with dspr
    if alt_day3_un_fz_work == 'sl':
        "Ah so that's what it is.{w} Now puzzle is whole."
    me "You don't have to continue. I already can guess."
    me "So what do we do now?"
    show mt sad dress at right with dspr
    "Olga drooped, and in a second she turned from an experienced squad leader into a confused schoolgirl."
    mt "I don't know. I hope she's old enough to understand..."
    me "I'll go look for her."
    "Without much hope, I said."
    "Olga looked away somewhere in the direction of the dancers."
    mt "I don't think you should."
    mt "But if you do find her, try not to make things worse."
    stop music fadeout 4
    "And I went to where Lena ran away a couple of minutes ago."
    $ alt_day2_beach_seen = True
    scene bg ext_beach_night
    with fade2
    play ambience ambience_lake_shore_evening fadein 4
    "But in two hours of searching, I only trampled the soles of my sandals."
    "I didn't manage to find Lena in the end."
    stop ambience fadeout 3
    return


label alt_day3_un_fz_sleeptime:
    scene bg int_house_of_mt_night with dissolve
    pause(1)
    play sound sfx_close_door_1
    pause(1)
    play ambience ambience_int_cabin_night fadein 4
    if alt_day3_un_fz_neu_transit:
        play music music_7dl["unfulfilled"] fadein 2
        show mt sad dress with dissolve
        "When I came home, Olga was already there."
        "She sat on the bed, still undressed, clutching her notebook."
        mt "Didn't manage to find her?"
        "I shook my head."
        mt "I guess it's for the best."
        show mt normal dress with dspr
        "The squad leader looked at me carefully, barely hiding the panic in her eyes."
        mt "If you don't want to mess things up, don't try to talk to her."
        me "I think I've said enough today."
        "Olga got up."
        "Her hands were trembling a little."
        mt "I'm going to go check. I hope Lena has already returned home."
        play sound sfx_close_door_1
        hide mt with dissolve
        "She left."
        "In the current situation, I could only empathize to her."
        th "She's a teacher, and any emotional outbursts of the pioneers are her concern."
        th "And the pioneers are already almost adults, though not too wise because of this. They throw out such tricks that it won't take long to turn gray."
        "There was, of course, the share of my fault in Lena's escape too. "
        "But in the end, the root of the evil was in her fertile imagination."
        "But I was still ashamed. In front of her and in front of Olga."
        scene bg int_house_of_mt_night2 with dissolve
        play sound sfx_click_2
        pause(1)
        scene cg d1_end_of_day_7dl with fade
        "I undressed and climbed into bed."
        "I was afraid that I would not fall asleep after what happened, devouring myself mentally for all the sins, but I was wrong."
        "I was knocked out as soon as I closed my eyes."
        "Ahead was a new day full of disappointments."
    else:
        play music music_list["a_promise_from_distant_days_v2"] fadein 2
        show mt angry dress with dissolve
        "Olga was already waiting for me in the house, and she was far from being friendly."
        mt "Would you mind explaining where you were during the dances?"
        me "At the dances."
        "I answered boldly."
        "After all, I really went there."
        me "If you don't believe me, ask Slavya."
        show mt rage dress with dspr
        mt "Don't you lecture me on who to ask and what to ask!"
        "She loomed over me angrily."
        show mt angry dress with dspr
        mt "Toward the bed, now. We'll talk in the morning."
        hide mt with dissolve
        play sound sfx_close_door_1
        "And, bypassing me, she went out the door."
        scene bg int_house_of_mt_night2 with dissolve
        play sound sfx_click_2
        "I had only to obey - the day really turned out to be hectic, and I was notably falling off my feet."
        "Morning adventures with Ulyana and reconciliation with Lena at the infirmary..."
        if alt_day3_un_fz_work == 'un':
            "Lena's revelations at the warehouse."
        elif alt_day3_un_fz_work == 'dv':
            "Our scenery in the forest with Alisa."
        elif alt_day3_un_fz_work == 'sl':
            "And my unfortunate trick with the garland."
        "Ball, where I spent twenty minutes at most..."
        if alt_day3_un_fz_stories:
            "And a forgotten fairy tale from my childhood, which, as it turned out, is known here too."
        scene cg d1_end_of_day_7dl with fade
        "And that weird dream before dinner that I couldn't even remember."
        th "But I still haven't solved the main problem - what to do with Lena?"
        th "She believes all sorts of nonsense now."
        th "Perhaps they can occupy her more than I can?"
        "With this ludicrous hope, I fell asleep."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day3_eventAf_un_mi_house1:
    scene bg ext_house_of_un_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    if counter_mi_7dl == 1:
        call alt_day3_day_mi
    else:
        "It was not too clear why legs had brought me here."
        "But after standing for ten minutes, I understood."
        me "We'll treat sleepwalking, my friend. Yes."
        "Then turned around and quietly left the scene..."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_day_mi:
    scene bg ext_house_of_un_day with dissolve
    $ counter_mi_7dl = 2
    play music music_7dl["genki"] fadein 3
    "And some people said that love is a fog that dissipates with the first ray of reality."
    "But the hell it'll dissipates now."
    "Whether my fog has too much surface tension."
    "Whether that wise talker just gave out stupidity in a beautiful wrapper."
    dreamgirl "Who said love?"
    th "Not me, obviously."
    "I chuckled."
    th "To see our Japanese diva in a swimsuit..."
    dreamgirl "Better in a negligee!"
    th "Shame on you, vulgar."
    dreamgirl "So you're refusing, right?"
    th "What do you mean?"
    dreamgirl "In the same sense that our Miku is getting ready for a bath, right?"
    th "That's right."
    dreamgirl "And on the occasion of the heat, she has a window in the house wide open, right?"
    th "Also true."
    "I nodded, still not very well understanding where the voice of my libido was driving."
    dreamgirl "Not driving anywhere but you can go and look at it!"
    th "No, I can't do that."
    dreamgirl "Are you impotent or orthodox? Hey, up there, why did they slip me a defective bore!"
    dreamgirl "Feet in hand and march behind the house!"
    th "Get off, brute, or I'll eat bromine!"
    dreamgirl "Okay, okay! Although I can't believe you willingly turned down this opportunity!"
    th "I said..."
    dreamgirl "Yes, yes, no need to repeat twice, no need to repeat twice."
    dreamgirl "I have another idea!"
    th "No, I've had enough of your ideas."
    dreamgirl "Just listen! {w}Since you refuse to peep on Miku because you have ethereal experiences and all, maybe then..."
    "The inner voice took a threatrical pause pause."
    th "What?"
    dreamgirl "Peep on her neighbor?"
    with vpunch
    dreamgirl "Ha ha, you should have seen your face! No, I'm talking about something else: let's connect high technologies to the cause!"
    th "Meaning?"
    dreamgirl "I mean, you have a camera on your phone."
    dreamgirl "Here, use it - you will not peep, and you can look at the same time... If you want."
    dreamgirl "And the locals won't hit you in the jaw if they catch you hot - because they don't know what this thing is."
    th "Categorically..."
    dreamgirl "Refusing?"
    th "No. Why not?"
    "I took my phone out of my pocket and checked the battery level."
    "I really liked the idea - if you put aside the thought of some dishonesty..."
    "But to hell with doubts! I've been arguing with myself for a good five seconds now, the girl could well have changed clothes in this time!"
    "On my toes, I go to Miku's cabin, bending around it along the left edge - where the squad leader would not even be able to «accidentally» notice me."
    scene bg ext_path2_day with dissolve
    play sound sfx_hiding_in_bush fadein 0
    "Under the windows of the girls, some bushes grew wildly, which I would find it difficult to name."
    "Their small foliage made almost no noise when in contact with the skin, so there was nothing to stop the amateur voyeur from climbing where I wanted and doing what I wanted."
    "Voices came from the house, something rustled - it seems that no one noticed me."
    "Wonderful."
    "My chance."
    "Having fired up the video, I raised the phone over my head and, focusing on the picture in the viewfinder, began to catch a sharper frame."
    "True, while it was all possible with difficulty - I was too low, I was afraid to come closer and managed to curse this idea three times."
    "But water wears away stone."
    "I just need to be patient."
    play sound sfx_hiding_in_bush fadein 0
    "And then I froze - behind me the bushes began to move."
    "If I hadn't been so energized, I would never have felt this."
    "But somehow no one was in a hurry to shout and catch me by hand."
    "On the contrary - from the warm breath the hairs on the neck stood on end, and someone asked in a whisper:"
    stop music fadeout 3
    voice "How is it?"
    "And then two things happened at the same time:"
    "The camera finally caught focus - and showed me that only Lena was sitting in Miku's cabin and mumbling something under her breath over a book."
    "I think it was her muttering that I took for conversations."
    "And at the same time, I turned around and saw the one who had so successfully sneaked up on me."
    "And it turned out to be..."
    with vpunch
    play sound sfx_scary_sting
    show mi smile swim with dissolve
    me "Miku."
    play music music_7dl["ourfirstmet"] fadein 3
    mi "Shhh."
    "She pressed her finger to her lips and, trying to step more quietly, began to get out of the bushes, dragging me along with her."
    $ alt_day2_beach_seen = True
    scene bg ext_beach_day
    show mi angry swim
    with dissolve
    play ambience ambience_lake_shore_day fadein 3
    if lp_mi > 2:
        mi "Only the fact that you have done a lot of good for me does not allow me to slap you in the face."
    else:
        mi "I should crack your forehead, Senka. {w}But not now."
    "She was silent all the time that we walked to the beach, and only throwing her clothes on the sand, she deigned to open her mouth."
    "And to tell you the truth, Miku's silence scared me more than anything she'd ever said."
    mi "But that doesn't mean I'll hold back if I catch you next time!"
    mi "Just think about it, and she told me in the morning that you are such a good boy!"
    "On the last line of thoughts, I seem to have pulled away a bit."
    me "Who?"
    show mi sad swim with dspr
    mi "Who-who! Yesterday you was talking all about how to behave correctly."
    mi "And today you're peeping on Lena!"
    "She got hotter and hotter."
    "If she just beats me, it won’t be so bad, but if she starts screaming now..."
    "Which is why..."
    me "But I didn't want to peep on her..."
    show mi normal swim with dspr
    mi "Senechka, don't take me for a fool. I'm from Japan, not from a country of fearless idiots."
    mi "Why, do you think, at the quiet hour, you were under the girl's window?"
    "I sighed."
    "I'm not getting right of word today definitely."
    "Then I have to take it myself."
    mi "And I also decided that since Lena liked you - and she speaks dismissively of almost all of our acquaintances, that is, there is something good in you too, and you..."
    me "I wasn't peeping on her, but on you!" with vpunch
    show mi shocked swim with dspr
    "Miku froze."
    show mi shy swim with dspr
    mi "W-what..."
    "Stuttering, she repeated."
    "I spread my arms and lowered my head."
    me "Sorry, if anything. But I planned for you to be there, not..."
    "Miku took a deep breath."
    "Exhaled."
    "Then I thought about saying something, but I forgot that the air was over."
    "In short, in any other situation, I would have had a lot of fun watching both of us."
    "Unfortunately, it wasn't funny at all."
    show mi surprise swim with dissolve
    mi "But I am..."
    "She automatically stroked something round in the bust area."
    "Greatly in excess of her own topology."
    me "And yet."
    me "Sorry."
    "Now the inner voice's trickery no longer seemed like a tickling adventure."
    "In all its unsightly beauty, this Act appeared before me."
    dreamgirl "I wonder if that's what you'd call it, if your trick worked."
    "Weakly parried the preoccupied alter ego."
    show mi smile swim with dspr
    mi "Well, in that case... I guess I can forgive you."
    "The girl said thoughtfully."
    mi "But only under the promise - that there's no more such peeping, is it clear to you?"
    "I readily nodded."
    mi "I was more worried about my friend, but since it doesn't concern her..."
    "She threw a towel at me."
    mi "Watch over my things while I bathe... delinquent."
    hide mi with easeoutleft
    "And laughing she ran to the water."
    stop music fadeout 3
    with fade2
    "I went swimming, after all."
    "Fortunately, Miku turned out to be quick-witted and did not report to Olga Dmitrievna about my encroachments."
    "Though I think she had every right to."
    "However, now I've fallen into some kind of addiction."
    "And she started to use this addiction!"
    "First as a porter, a fly-catcher and a drink-carrier."
    scene bg ext_square_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    "Then - a camp-escort and a porch-waiter."
    "And as a result of all the ups and downs, having wahed, wiped and changed Miku's clothes (this time she was on the alert and shouted at me, as soon as the porch creaked), we ended up at the door of her possessions."
    scene bg ext_musclub_day with dissolve
    "For some time she hesitated, choosing whether to send me under Slavya's command - to carry all sorts of heavy things."
    "I had to use the forbidden jutsu - puppy-eye-jutsu."
    "And she couldn't resist."
    "Trembled and agreed:"
    show mi normal pioneer with dspr
    mi "Okay, so be it - first we'll try to dress you, and then we'll make you work."
    me "Thank you, Mistress!"
    "I bowed politely."
    mi "That's good. Wait for a while here, I'll call."
    hide mi with dissolve
    "She disappeared behind the door."
    "And about fifteen minutes later, her voice came from the club:"
    mi "Senechka, come in!"
    scene bg int_musclub_day with fade
    play sound sfx_open_door_clubs
    play ambience ambience_music_club_day fadein 1
    play music music_list["what_do_you_think_of_me"] fadein 5
    "Miku herself was not in the room."
    "I looked around."
    "A pioneer's uniform lay in a heap on the piano. {w} A female pioneer's uniform. I hope this one is not for me?"
    mi "Senya, wait a bit, I'm here!"
    "Miku's voice came from somewhere behind the piano - it looks like she has a props room there, among other things."
    play sound sfx_brass_drop
    "Suddenly there was a terrible roar from there, and I recoiled in horror."
    me "Miku? Miku! Are you okay?"
    "For a while nothing happened, and I decided to check - how are things?"
    "On unruly legs, I took a few steps and..."
    mi "Yeah!"
    mi "Well, how do you like me?"
    show mi normal dress with dissolve
    "She jumped out from behind the door, smiled at me and, rising on her toes, took a few steps, turned around the axis and stared at me with a kind of dumb question."
    "A very beautiful dress to match the color of her hair, the color of her eyes, as if an extension of her body - and you can't say that this beauty was sewn in the Soviet Union!"
    mi "Look what beauty I dug up!"
    me "No words. Very, very."
    show mi smile dress with dspr
    "I shook my head, and Miku, clearly pleased with the compliment, broke into a smile."
    mi "Is fits well, doesn't he?"
    th "If you ask me, anything will look good with your figure."
    me "Fits...{w} Yes, well...{w} Suits you well..."
    show mi shy dress with dspr
    mi "Thanks!"
    show mi serious dress with dspr
    "Miku shot her gaze at me."
    mi "Let's go get you something fancy, or..."
    "She paused."
    show mi grin dress with dspr
    mi "Maybe let's see what you are capable to?"
    "Again, these incomprehensible hints. She asks with an air as if she will not watch my dances, but... Let's say dances of a different kind."
    show mi smile dress with dspr
    me "Let's start with the dance. There might be no suitable things for me."
    mi "As you wish...{w} But what if there's something! And suitable for you."
    "The art director was a person who was passionate about everything, and the chance to earn a part-time job as a costume designer made her notoriously excited."
    "I sighed."
    me "As you say. Let's go try something."
    show mi happy dress with dspr
    mi "Hooray!"
    "She was delighted and almost jumped with anticipation of what she would do to me now."
    "Girls love to play with dolls."
    "Even if this doll's name is Semyon, and it's a year and a half older than you."
    mi "I'll just change back, wait. Otherwise it seems a crime to me to climb dusty things in such luxury."
    "I thought the same, so I silently nodded."
    scene bg int_musclub_day with dissolve
    "She ducked into the props room and was quiet there for a few minutes."
    mi "Mmm... Syom?"
    me "Yes."
    "I stood with my back to the door and stared out the window, carefully not thinking about the fact that a very, very pretty girl is now undressing on the other side of the wall."
    "Here she puts her hands behind her back, loosening the zipper, and the dress with a quiet silk rustle flows down to her legs, exposing roundness of the most pleasant proportions, a flat tummy and..."
    "Okay, that's enough. That's not what we came here for."
    mi "Semyon!"
    "Persistently repeated Miku."
    me "Yes? What is it?"
    mi "I can't find my uniform."
    mi "Look, please, is there anything like it next to you?"
    "I automatically glanced at the piano."
    "Well, yes. Actually."
    me "I see something."
    "I replied after a small pause."
    mi "Very good! Take it and give it here, please."
    mi "Just don't peek, I know you!"
    me "As if I need it very much."
    "I blushed, as that was the first thought that came to me."
    "The shirt, the cut-out skirt - all this still kept the warmth of the girl's body, and I could hardly resist not to inhale the smell."
    "Anyway, we'll dance together later. {w} And I'll have enough of it as well."
    me "Who are you taking me for?!"
    "Opening the door and diligently looking to the side, I held out the uniform somewhere into the darkness."
    mi "For a healthy boy with healthy desires?"
    "Despite the fact that she laughed at me, her laugh was neither threatening nor hurtful."
    me "I do have healthy desires... But that's no reason to mock me."
    show mi grin pioneer with dspr
    mi "And I'm not mocking you."
    "She changed and went out, holding the dress already hung on a coat hanger."
    mi "Where to attach it now..."
    "She thought for a moment and, shrugging her shoulders, hung the hanger right on the music shelf."
    show mi happy pioneer with dspr
    mi "I definitely won't forget it there!"
    "I was suddenly belatedly embarrassed by the situation."
    "Supposedly «forgotten» uniform where I absolutely notice it, the completely shameless changing - it all looked like an attempt either to embarrass me... "
    "Or to provoke."
    "But to what?"
    "The ideas in my head were the most fantastic. Although the idea that I might be interesting to Miku as... who, by the way?"
    if (alt_day2_date == 'mi'):
        "A young man or, as they say in the West, a boyfriend?"
    else:
        "An object for sexist jokes?"
    "One of the last flashed in my head."
    stop ambience
    me "Let's go dress me up now?"
    "I tried to add courage to my voice. If this girl dresses me up as a pimp... I can't even scold her."
    show mi shy pioneer with dspr
    "She seems to have recognized the direction of my thoughts and tensed up quite a lot."
    "To offend a person is not a difficult task. Here's to give him a chance..."
    "With a sigh, I decided to give Miku a chance."
    "Does she have good taste?"
    mi "Do you have any wishes?"
    me "Nothing special.{w} I just want to look worthy of a lady. {w}At least not a felt boot from the village."
    me "A shirt, some trousers, boots - or whatever is in fashion right now..."
    show mi happy pioneer with dspr
    mi "It'll be bright enough. Stage costumes, after all."
    "She looked thoughtfully over my body, figuring out the proportions and sizes."
    "Then she shook her head, using her hypno-hair - and I stared at her once again - it seems that she decided something."
    mi "No, I'm sure I won't find anything good there alone."
    mi "So we'll have to search together."
    me "Correct me if I'm wrong. Are you suggesting that I now climb into that dim room with you and stir things up there?"
    mi "Yes. What is it?"
    if (alt_day2_date == 'mi'):
        $ lp_mi += 1
        me "Well, nothing, in general. But if someone comes here while we're there..."
        show mi shy pioneer with dspr
        "She looked at me with barely concealed excitement, putting her hand to her mouth."
        mi "Then..."
        "She drawled encouragingly."
        me "Then they'll think we've decided to not limit ourselves with only beach hugs."
        "She fell silent."
        show mi sad pioneer with dspr
        mi "And would you want to..."
        "She began hesitantly - and immediately fell silent, blushing."
        me "What?"
        mi "Limit..."
        me "And about this..."
        "Feeling my cheeks begin to glow, I hurried to finish the sentence."
        me "You'll know when we're done with the costumes."
        show mi happy pioneer with dspr
        mi "Catch you on that!"
    else:
        me "They can think of anything..."
        mi "Don't you care?"
        me "I may not care. But I don't like baseless rumors."
        "She paused, as if speaking the words to herself."
        show mi laugh pioneer with dspr
        mi "And if they're not baseless?"
        "Even though she seemed to be smiling, her voice was barely audible."
        me "You ask such questions..."
        show mi normal pioneer with dspr
        mi "Is it hard for you to answer?"
        me "So... yes. It's hard."
        "I couldn't look her in the eyes."
        "Especially knowing she's looking at me with a calm, searching look."
        "Feeling like a bug on a pin, I muttered,"
        me "But they're baseless."
        me "We don't even..."
        show mi sad pioneer with dspr
        mi "Whose fault do you think it is?"
        "I shuddered and turned away, completely embarrassed."
        "Hopefully now that she's achieved her goal, she's happy?"
        me "Now, if you've had enough to scoff at, should we start looking for a costume?"
    stop music fadeout 4
    "She pointed to the door invitingly."
    "And we're in."
    scene
    $ renpy.show("bg int_wardrobe_7dl", what = Desat("bg int_wardrobe_7dl"))
    with flash
    $ persistent.sprite_time = "night"
    play sound sfx_open_door_clubs
    play ambience ambience_music_club_day fadein 1
    scene bg int_wardrobe_7dl with dissolve2
    play music music_list["so_good_to_be_careless"] fadein 6
    "And ended up in costume heaven!"
    me "Look how much is here!"
    "I picked up the shako standing there from the floor, and, brushing off the dust from the scarlet sultan, put it on my head."
    me "Good?"
    show mi laugh pioneer with dissolve
    mi "Wonderful!"
    "She laughed."
    mi "Looks like something from «War and Peace» was staged here, that's all left after."
    me "Actually, there's a whole klondike!"
    "The glance ran along the long plank shelves, barely lit by a forty-watt light bulb - some paints and fabrics do not tolerate bright light at all."
    show mi normal pioneer with dspr
    mi "Boo!"
    "I turned around and shuddered."
    "Miku found the head of a dragon, or just a poorly made rooster, and after putting it on, she walked in my direction, waving her arms."
    mi "I'm a terrible Godzilla! Break houses! Eat fish!"
    "She was about to say something else, but it looks like dust got in her nose and she sneezed."
    "I hastened to remove the props from her."
    "Under the mask was a smeared with dust, but utterly pleased face."
    me "You should at least dust off what you're wearing, miracle."
    mi "I forgot that dust could be inside too."
    "She laughed, and suddenly something inside me jumped in response in sync with her laugh."
    "It's like the channel has been changed and Miku has gone from being a chatterbox of laughter to something desirable..."
    "Although, maybe the reason for this was the look - both alluring and confusing on the soiled face."
    "I found a clean handkerchief in my pocket – I don’t know why they gave it to me, apparently it’s part of the uniform – and I took it out, drooled and tried to clean the most noticeable stains on her cheeks."
    if (alt_day2_date == 'mi'):
        "Only to find her close, in my hands in a few seconds."
    else:
        "She endured the first touches, and then, grimacing, took a step forward, being close, practically in my hands."
        "And somehow I immediately remembered what I was thinking when she changed clothes."
    show mi shy pioneer close with dspr
    "I almost started bleating, apologizing and..."
    dreamgirl "Shut up."
    th "What?!"
    dreamgirl "Just shut up."
    th "What the…"
    dreamgirl "Shutupshutupshutup."
    "The place where the voice was born, as if descended from the throat somewhere down, either into the stomach, or into the lungs, and I purred with a voice that surprised myself:"
    me "Are we already dancing?"
    me "What about the clothes?"
    mi "But we didn't find it. And in general - to hell the clothes!"
    me "Even this one?"
    "I twisted lightly, making more contact. The shirts rustled against one another."
    me "Miku?"
    mi "Yes..."
    me "If you fall asleep now, I won't have time to dance or dress up."
    "I cleaned her forehead, and, satisfied with the result, I nodded."
    show mi happy pioneer with dspr
    mi "You are so cuuuute."
    "And she muttered something under her breath."
    show mi smile pioneer with dspr
    "And it's like a wall has fallen between us."
    "With Miku, it was easier for me before than with the other girls - perhaps the experience of communicating with Asian women affects, and I know what to expect from them - but now everything has changed."
    "Laughing, we walked, turning everything upside down in our path, through the wardrobe, playing out different scenes - from Pierrot and Cipollino to Kibalchish and Hamlet."
    "She lived on the stage and accepted new opportunities to reveal herself with great gratitude."
    "And I... And what about me? For me it was fun and easy to be with her. Like never before with anyone else."
    mi "I suggest taking the shirt from the bullfighter's suit and rip off all the frills from it."
    "She was walking through the warehouse and one of the hangers caught her eye."
    mi "Yes! Here are pants for you. Now we..."
    "She dragged me to a full-length mirror on the wall and, in a voice that brooked no objection, ordered me to try it on."
    "I was confused."
    me "Miku, can you turn your back at least?"
    show mi normal pioneer with dspr
    mi "I'm not watching anyway, change clothes now."
    me "When you changed clothes, I was standing outside the door, have respect!"
    "I was indignant."
    show mi laugh pioneer with dspr
    mi "And whose fault is that?"
    "She again turned on her crazy eyes and studied me point-blank."
    me "But you yourself said not to peep..."
    show mi normal pioneer with dspr
    mi "And you took it and listen, right?"
    mi "You are cuuute."
    show mi happy pioneer with dspr
    me "You told me already."
    me "Will you let me change? Get out, I say!"
    show mi surprise pioneer with dspr
    mi "Don't be shy."
    "Looks like she wasn't going anywhere at all!"
    "I tried to start again."
    me "Miku, listen... What we're doing is already indecent! The two of us are in some dark room, all alone."
    me "And you telling me to undress? What if Olga Dmitrievna comes in?"
    dreamgirl "Ask her to hold the candle."
    me "So. I won't undress in front of you just like that."
    me "If you want to undress me, I can play strip poker, nothing more. Now, get out!"
    show mi sad pioneer with dspr
    "She frowned, as if coming to her senses."
    mi "Yes, okay, I got carried away, sorry. I'll wait for you, come out when you're done, okay? In the meantime, I'll get the iron and board, we'll have to iron your clothes."
    hide mi with dissolve
    "Judging by the renewed speed of pronunciation, the state of mind is stabilized."
    dreamgirl "What a jerk."
    "I unfastened the strap on my shorts and, trying to act as quickly as possible, pulled them off, cursing with my inner voice in between."
    dreamgirl "If a girl wants to see you perform a striptease, all you should be interested in is on a pole she wants or just in the middle of the room."
    dreamgirl "Maybe you don't know, but you just got a token of trust. You blew it, though, so it doesn't matter."
    th "What are you talking about again?"
    dreamgirl "The girl practically confessed to you that she wants to see you unmasked. Do you need more proof of affection?"
    "I swallowed."
    "This is all..."
    if (alt_day2_date == 'mi'):
        "Although after beach events it's, pretty much, logically correct."
    else:
        "Well, she wanted to, but what have I got to do with it? Maybe she's just too lonely."
    dreamgirl "Yeah. She's lonely. You don't. And you didn't imagine her body, and you didn't want to put your nose in her shirt. And you don't like her of course."
    "Here I again did not find anything to answer."
    scene bg int_wardrobe2_7dl with dissolve
    "In the dark, I missed the sleeves and trousers several times, {w}so I didn't pay attention to a sneeze somewhere in the dark."
    me "God bless."
    "I wished to someone unknown in the darkness."
    "Wait..."
    me "Miku?!"
    show mi laugh pioneer with dspr
    "It seems that she did not intend to go anywhere - she just took a comfortable place."
    mi "Thank you!"
    me "Miku, what did I ask you?"
    mi "Not to watch? {w}Well, I didn't. I observed!"
    "And deciding to strike me on the spot with logic, she added:"
    mi "In case something happened."
    with dissolve
    "Well done, of course. But I'm physically unable to undress in front of a strange girl."
    dreamgirl "Stranger? And who's to blame?"
    "My subconscious quoted someone."
    show mi normal pioneer with dspr
    with dissolve
    me "You missed everything, didn't you?"
    "She stood up and, coming up behind me, put her hands on my shoulders."
    mi "Actually..."
    "Her breath pleasantly tickled my neck, and I shuddered involuntarily."
    mi "I heard."
    mi "Each."
    mi "Of your."
    mi "Words."
    show mi happy pioneer with dspr
    "She pulled up my shirt, straightened it over my shoulders, and the black fabric played in the dim light."
    "The shirt was really chic. It came with a red torero sash, but I thought it was too much outrageous for the ball."
    "She turned me around.{w} And after running her eyes over the clothes, she nodded in satisfaction."
    mi "Handsome. That's it, now you can undress."
    me "Maybe you could at least this time come out?"
    "I inquired caustically."
    "She just shrugged her shoulders in annoyance."
    mi "Do you care? Everything I wanted, I've already seen. So don't be shy."
    "I shrugged my shoulders and, thinking that it was really zero difference now, took off my shirt."
    show mi sad pioneer at center
    with dspr
    mi "Achoo!"
    me "You don't seem to have a reaction to dust, but an allergy to naked me."
    "I found this idea funny enough to share with Miku."
    "She said nothing, and I, squinting my eyes, saw through the mirror how she, sticking out the tip of her tongue from zeal, was writing something in a notebook."
    stop music fadeout 2
    play sound sfx_open_door_1
    mt "And that's for the best!"
    "Voice from the door was heard."
    pause(1)
    play music music_list["doomed_to_be_defeated"] fadein 0
    th "O-o!"
    "At the door, she stood."
    "Olga Dmitrievna!"
    scene bg int_wardrobe_7dl
    show mt angry pioneer at right
    with dissolve
    "Murphy's first law - if something bad can happen, it will happen."
    "Murphy's second law - even if something bad cannot happen in any way, it will definitely happen."
    "I seemed to look at myself from the side - a shirtless young man in unbuttoned trousers."
    "There's a girl next to me..."
    "I glanced - in a half-open shirt."
    "In a dark room with no windows."
    "What can a squad leader think, who by no means was supposed to be here?"
    "That's right. That's what she thought, because the first thing she looked at was my trousers."
    mt "Semyon..."
    "She started. And I was covered in perspiration, already imagining a list of problems that I'll have soon - but oh well — already appeared!"
    show mt rage pioneer with dspr
    mt "So you signed up for a music club? And you're rehearsing?"
    "Here Miku recovered from tetanus."
    "It seems that absolutely the same picture came into her head, since she almost pushed me away or almost rushed away herself - in any case, she outlined the course of movement."
    show mi laugh pioneer with dissolve
    "And then she pulled herself together and laughed her unearthly silvery laugh."
    mi "What a twist!"
    show mi sad pioneer with dspr
    mi "And how they say, «oops»."
    "She burst out laughing again, ignoring the squad leader's angry look."
    "And she was still filled with blood, a few more seconds - and she would tear me to shreds!"
    if (alt_day2_date == 'mi'):
        mt "I heard about the events at the beach yesterday, but I thought I'd let you guys figure it out."
        mt "You are adults, reasonable people. You should already be able to understand what is more important to you."
        mt "But you, Semyon... Was it not enough for you?"
        "I was sullenly silent."
    mt "In the backroom?"
    mt "In the dark."
    mt "Yes..."
    "Miku seemed to be trying to get a word in, but the squad leader didn't give her the chance."
    show mt angry pioneer with dspr
    mt "I see you've picked up the suit. Here, take care of it."
    "She looked over at me."
    hide mi with dissolve
    show mt rage pioneer at center with moveinleft
    mt "As for you... Quiet hour in the camp, march to bed!"
    stop ambience fadeout 2
    "After exchanging a wink with Miku, I turned and walked out of the props room."
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_musclub_day with dissolve
    $ persistent.sprite_time = "day"
    "Having carefully closed the door behind me, I went out onto the veranda, and from there onto the path leading towards the square."
    "Despite the ambiguity of the situation, I did not build particularly gloomy forecasts for the future."
    hide mt
    with fade
    "She never caught up with me either in the square or at the cabins."
    "«She» who? Well, neither."
    "First, I'm wondering why the squad leader suddenly darted to go to the club for the first time in the last few days?"
    "Secondly, Miku's unexpected activity in the closet."
    "Are these items related?"
    scene bg ext_house_of_mt_day
    with dissolve
    play ambience ambience_camp_center_day fadein 3
    th "If someone snitched on us, then who? And why did he ran to the squad leader?"
    th "Although if it's someone like Slavya, there's no question of why. That's right, and that's it."
    "I understood Olga: Almost naked pioneer, quantity: one. Female disheveled pioneer, quantity: one. A secluded nook, quantity: one."
    dreamgirl "They probably climbed in and undressed to learn the scales."
    stop ambience fadeout 2
    stop music fadeout 5
    "It is unlikely that we will be severely punished or banned from communicating. But the situation is still unpleasant. It is doubly unpleasant because the scenario unfolded in a way that I would never have allowed it to unfold in my old life."
    "Public and personal for me are the extremes of the social scale. I won't let anyone into myself and I won't get inside anyone. And if I have an affair, then only I and my chosen one will know about it."
    "And there certainly won't be much gossip about how a newcomer crucified one pretty artistic director on the sand."
    scene bg int_house_of_mt_day
    with fade2
    play music music_list["your_bright_side"] fadein 5
    th "Either Miku set it up herself so I wouldn't overdo it."
    dreamgirl "Did you see her eyes? In this context, only bondage games and pink handcuffs could turn out to be «superfluous»... And that's not even a fact."
    show mt angry pioneer with dissolve
    "The door slammed behind me, Olga entered the house."
    "It seems that she had time to cool down a bit, because she didn’t start yelling from the doorstep, but, with a short nod, threw:"
    mt "Spew it out."
    "Spew what? Of course, give me a sec..."
    me "Miku didn't tell you anything?"
    mt "I'm interested in your version of events."
    me "You know, I feel like a jerk way too often in this camp. Let's not this time."
    me "You told me to dress, you saw the rest."
    me "Think of the rest yourself... To the extent of depravity."
    "It seems that the unwillingness to cooperate was written on my forehead quite clearly, since Olga, having doubts, said:"
    show mt normal pioneer with dspr
    mt "Sleep for now, we will decide what to do with both of you after lunch."
    play sound sfx_close_door_campus_1
    hide mt with easeoutright
    "She went outside."
    if alt_day2_us_escape:
        "And, like yesterday, she creaked a deck chair, settling there with a book."
    th "She's cerberating me again. It's just a matter of who and from whom."
    th "If she wants to protect me from something, then it's understandable. I'm new here, I don't know anything, and so on."
    th "What if it's the other way around?"
    th "What if she's the one in the camp trying to save something FROM ME?"
    th "Something only available during quiet hours?"
    "The logic was lame on both legs and head, but, in the absence of alternatives, I left this version as a working one."
    "Anyway, after lunch, I'll have to check on Miku."
    "With this thought, I smiled, imagining a girl in front of my eyes..."
    "And passed out."
    scene bg black
    with fade3
    stop ambience fadeout 3
    pause(3)
    "I seem to be sleeping too much. Six hours has always been enough for me to do everything about everything."
    "And here, I not only sleep eight hours a night, but also a mandatory quota during the day."
    me "Do you really want to spend your best years under the covers! On a pillow! Without pants!"
    "Wake up voice was hoarse."
    "I got up and, going out onto the porch, stretched."
    "The mood was great!"
    scene bg ext_house_of_mt_day
    with dissolve
    play ambience ambience_camp_center_day fadein 3
    "Until I remembered - what preceded sleep."
    "Someone snitched to the squad leader on us, and she didn't let the situation go beyond the bounds of decency."
    "Although what am I talking about. Miku, if I remember correctly, did not allow herself anything extra. Only thing she did is playing coquetry."
    "Compared to the thermonuclear Dr. Collider - pampering."
    "Looking around - Olga was nowhere to be seen - I was about to run away when I suddenly saw her returning from some distant cabins."
    show mt normal pioneer with dissolve
    mt "Woke up? Good. Let's have lunch now."
    "I didn't answer anything. The questions that haunted me before going to sleep resurfaced in my mind."
    "In short, I myself did not notice how I suspiciously squinted in her direction."
    "Earned a questioning look, embarrassed, blinked guiltily and turned away."
    "Where else would you master the subtle art of unobtrusive interrogation of a squad leader."
    me "Olga Dmitrievna."
    mt "Yes?"
    me "Explain to me my status here. What am I, a prisoner? Arrested? Exiled?"
    show mt grin pioneer with dspr
    mt "Prisoner?"
    show mt laugh pioneer with dspr
    mt "I knew you could say things but..."
    me "Then explain to me all these restrictions in movement and communication with others."
    mt "There are no restrictions."
    me "Yeah. And you didn't drag me out of the club by the hand."
    mt "It is still unknown who dragged whom from there..."
    "She shook her head and gave me a wary look back."
    mt "And why wouldn't you explain what were you doing there with Hatsune?"
    me "You saw it yourself, we were changing clothes!"
    mt "That's right. You're undressed, she's undressed. You were changing. Side by side. In the same room."
    me "Of course. What did you think?"
    if loki or herc:
        th "It seems that she can be successfully hurt if you hint that it's her thoughts are vulgar, and everything around is crystal honest and clean."
    show mt shocked pioneer with dspr
    mt "And what was I supposed to think?"
    "Well, no, the Jewish joke does not work with me, it's useless to answer a question with a question."
    menu:
        "Miku is innocent":
            me "And that's should be more clear to {b}you {/b}. What you're {b}supposed to think{/b}."
            me "You are a teacher, you were taught, including what you should think. Here are all the cards."
            if not herc:
                $ karma += 10
            $ lp_mi += 1
        "Apologize":
            if herc:
                $ karma += 10
            me "I'm really sorry you saw something reprehensible in this situation."
            "I muttered, looking at the floor. I was ashamed!"
            me "But there was nothing."
            me "Just a stupid misunderstanding."
            show mt grin pioneer with dspr
            if (alt_day2_date == 'mi'):
                mt "What about your beach performance?"
                me "It was necessary. She was very sick. Worse even than it usually for me."
            me "I wouldn't forgive myself."
        "Threaten":
            $ karma -= 10
            "I sighed."
            me "Olga... Stop acting like a jealous wife."
            show mt surprise pioneer with dspr
            me "If there was something between me and Miku - the tenth thing."
            "I raised my eyes to the sky. Lazy cumulus clouds floated there. Those fluffy ones come from childhood."
            me "And you're going to have to take my word for it anyway, otherwise what do your stupid rules require? A public trial?"
            me "Picture the picture:"
            me "Pioneering movement against Semyon and Miku. A case of depravity."
            me "How will you look into the eyes of a girl later? What if it turns out that you are infallible - you made a mistake?"
            show mt angry pioneer with dspr
            mt "What are you..."
            me "Nothing. Wrap this circus already."
            "How tired I am of all this."
            me "If {b}you{/b}, of course, don't mind."
            "I glanced at the squad leader. She stood bewildered, helplessly clenching and unclenching her fists."
            me "Olga Dmitrievna."
    show mt normal pioneer with dspr
    "She sighed."
    mt "Mind you, you didn't win."
    mt "I still have the authority to ruin your life thoroughly, Semyon."
    mt "But I really don't have the right to ruin a girl's life. You're right about that."
    me "So we forgot?"
    show mt smile pioneer with dspr
    mt "Till the first warning."
    "She smiled."
    "I took under an imaginary visor and headed towards the canteen."
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_musclub_day
    with dissolve
    "Miku was nowhere to be seen at lunch, and I decided to look if the light is on in the club in case she never left there."
    "Even from a distance, I heard the piano sighing melancholy about something. Someone was playing inside. And playing with dedication."
    "Not daring to break the moment, I went around the club from the side and cautiously looked through the window."
    "At the piano, swaying to the beat, sat Miku, with furiously sparkling eyes, not looking at the keys, she seemed to be weaving some kind of lace from the notes, releasing all her anger into the unfortunate twelve modes."
    "I expected everything. Comfort in someone's company, tears, self-pity."
    "But I couldn't even imagine this. And, like in the morning, I reminded myself that for this girl, music will always come first."
    "Both angry and happy."
    stop ambience fadeout 2
    play sound sfx_open_door_2
    pause(2)
    scene bg int_musclub_day
    with dissolve
    play ambience ambience_music_club_day fadein 3
    play music music_7dl["shehasgone"] fadein 4
    "She was sitting with her back to the entrance, so she didn't notice me."
    "I plucked up the courage to open the door, trying to do it silently and, going up to the girl, put my hand on her shoulder."
    "She flinched, whirling around sharply, almost staggering to the side."
    show mi cry pioneer with dissolve
    "Noticed that it's just me - and surpsingly... {w}bursted into tears."
    th "Why do you constantly strive to dilute dampness..."
    "In some panic, I thought."
    "But she's still crying. And today she won't forgive if I stand and wait until everything resolves. It won't resolve."
    show mi cry pioneer with moveinbottom
    "Unless I suddenly disappear. Forever. Just like I appeared here."
    "Raising her from the bench turned out to be not difficult, and the first step, the most logical and expected, is to warm her on the chest, stroking her head and whispering something semi-conscious in her ear, making it clear that I am here."
    "I never knew how to do this, and I feel embarrassed about it. Maybe she was right when she said that if nothing was sown in us, then simple human participation, the ability to regret and encourage, will not grow."
    "Maybe we really are all the same here - unsociable, loners. People who, for various reasons, were rejected by society."
    "And society gave us a second chance, gave us the same loner as friends, partners, playmates. And, perhaps, even lovers."
    "She shuddered convulsively for a few more minutes, breathing hotly somewhere in my armpit, and I suddenly caught myself thinking that, it turns out, I was so very comfortable."
    dreamgirl "Congratulations. You just felt yourself needed."
    dreamgirl "The first step on the path to the abyss has been taken."
    me "Miku, come on, my dear, what are you really. Evil squad leader and morons-pioneers, no big deal."
    me "Forget it. They aren't worth your tears."
    mi "Really?"
    show mi cry_smile pioneer with dspr
    "She raised her tear-stained eyes, and I suddenly realized that I would not be able to, I would not forgive myself if one day I would lie to them."
    me "Really."
    show mi sad pioneer with dspr
    mi "Why do you need me? You left so easily when you were taken away..."
    me "It's hard for me to say exactly why. But that I need you is absolutely certain."
    show mi shy pioneer close with dspr
    "And she, suddenly embarrassed by the closeness, hid on my chest, quite obviously thrilled, giving me the opportunity to communicate with the back of her head."
    me "I had to yell at the leader so she let me go..."
    "I suddenly realized that I was standing, hugging a girl, who was far from being indifferent to me. That I was inhaling the scent of her hair, reeking of eucalyptus."
    "And that I really want to touch the top of her head with my lips."
    "Unbearably want."
    th "I hope she get it right."
    show mi happy pioneer close with dspr
    "I reached out immediately to embody what I wanted."
    "And then she turned again, settling herself comfortably, raised her head with her eyes half-closed with pleasure..."
    mi "Tha..."
    "In general, neither I reached the top of her head, nor she finished speaking."
    "It suddenly seemed to me that I would never learn to dance today."
    show mi smile pioneer with dissolve
    mi "Thanks, for returning..."
    "With obvious reluctance, she said, pulling away from me."
    mi "But we still have a whole bunch of things to do."
    stop music fadeout 6
    "She nodded at a hanger that I hadn't noticed before. My new suit for the evening was already there."
    "Brought into a divine form, it seemed even better than in a dim closet."
    me "Thank you."
    me "Looks really cool."
    "I glanced at the dress hanging next door."
    me "Though not as great as your dress."
    "She blushed at the praise."
    mi "And I picked up the music."
    show mi upset pioneer with dspr
    mi "Shall we dance?"
    "Her voice trembled."
    "And what could I answer?"
    me "Of course."
    "I said."
    play music music_list["raindrops"] fadein 3
    show mi normal pioneer close with dissolve
    "She gave me her hand and led me to the middle of the hall."
    "Some semi-familiar melody burst out from the tape recorder, and, having half-remembered how to properly hold my hands during the dance, I put my arms around her waist and drew her to me."
    show mi laugh pioneer close with dspr
    mi "Not so close, Syom."
    show mi normal pioneer close with dspr
    "She shrugged her shoulders as she counted out the intro."
    th "Hold your back, don't slouch, breathe quietly, don't lean close to your partner, don't screw up with the direction of rotation, make eye contact only if she pull away herself."
    "The subconscious rumbled."
    dreamgirl "I suggest we just shut up and enjoy the dance. We seem to be doing pretty well."
    "In fact, I did not notice how the first verse of some swedes passed, and we smoothly trampled to the chorus."
    mi "You're doing well you know!"
    show mi smile pioneer close with dspr
    "Her eyes were shining."
    show mi sad pioneer close with dspr
    mi "And you're not a bear.{w} Well, maybe just a little bit."
    me "What? Why?"
    "I hardly emerged from the sweet dope."
    mi "Because you don't have to hold me that tight."
    show mi laugh pioneer close with dspr
    mi "I'm all for it though. But we can't dance like that."
    me "I'm sorry..."
    "I blushed and loosened my grip."
    me "Listen, is this a must? Well... these dances."
    "I didn't mind dancing with Miku at all. {w} But doing it in front of all those people..."
    show mi smile pioneer close
    with dspr
    mi "What about it?{w} Are you shy?"
    "I nodded grimly."
    mi "You shouldn't. I'll tell you what - at the dances, everyone around - is shy."
    "She looked into my eyes and smiled in a new way, with a hint, with a promise."
    mi "They're scared to start dancing because no one wants to feel like the first fool on the dance floor."
    mi "They are afraid to dance with all their hearts, as they are afraid that there may be someone who will point a finger at them and laugh nastily at their dancing technique."
    mi "And they are terrified of the moment when they will dance, and the leader will suddenly put on such music that they personally cannot dance to."
    me "That's right..."
    show mi happy pioneer close with dspr
    mi "Here, relax. Dancing should be fun, don't go to the dance floor as if it's your job. Otherwise... Otherwise, you just won't be able to go there one day. Because you're too old or too tired."
    mi "And now you are pulled by the hand, and you shake your head. Because you know that it will be not so pleasant here anymore. So, another piece of childhood has died in you."
    mi "And there is not much of it, you should never rush to become an adult. Dance while you're young."
    me "What about your performances? Concerts."
    "She smiled mischievously."
    show mi smile pioneer close with dspr
    mi "I never considered them my work for a day."
    mi "It's like a disco where you dance for everyone - and they jump on the other side of the police barriers, and there is such energy in the air that you walk around drunk with happiness for a week."
    mi "And here you can afford to indulge and turn off your head, as if you yourself go down into the crowd."
    "The music ended a long time ago, and we all stood, slowly unhooking our hands."
    me "And if the environment is trying to squeeze it out of you? Life itself. If it turns out that no one needs it and never was?"
    "She laughed."
    mi "It means you don't need that kind of life."
    show mi normal pioneer close with dspr
    "Finally, with a click of a disconnected playback, we were told that the cassette was over."
    hide mi with dissolve
    "Sighing, Miku walked over to the tape recorder and rearranged the tape."
    "De Burgh blared over the speakers, and we returned to a melancholy trampling."
    scene bg int_musclub_sunset_7dl with fade2
    $ persistent.sprite_time = "sunset"
    "We danced until supper, and even the horn could barely reach the pair of clouded minds, impatiently and voraciously communicating. Minds that suddenly found each other."
    "I would hesitate to call it falling in love. It's more like that ecstatic feeling when you find someone who is an extension of you."
    "Or like in that stupid theory that every person has his own half, without which he is incomplete and flawed."
    show mi shy pioneer with dissolve
    mi "Okay."
    mi "You're probably already quite tired of me."
    me "I don't..."
    "She waved her hands,"
    mi "I don't want to hear anything! Let's go feed you before you faint from hunger."
    mi "Otherwise, there will not be enough strength for the actual dancing."
    "Here I certainly agreed with her."
    "We turned off the equipment, closed the clubhouse and slowly headed towards the canteen."
    return

label alt_day3_eventAf_dining_hall1:
    scene bg ext_dining_hall_away_day with dissolve
    play music music_7dl["carefree"] fadein 5
    "Ulyanka did not go far from the kitchen - she was standing almost near the very door, diligently looking for something under her feet."
    me "Q."
    "I approached from the left and patted her on the right shoulder."
    if alt_day3_duty:
        show us normal sport with dissolve
    else:
        show us normal pioneer with dissolve
    us "Quack."
    me "What are you doing?"
    us "And for what purpose are you interested?"
    "Ulyanka asked suspiciously."
    me "Just curious."
    "And I want to be aware if I suddenly become the target of another prank."
    "Forewarned is forearmed!"
    us "Do you promise not to tell anyone?"
    if alt_day3_duty:
        show us smile sport with dspr
    else:
        show us smile pioneer with dspr
    me "Give you my tooth on that!"
    us "Bugs!"
    me "Bugs what?"
    us "Catch!"
    me "But why?!"
    if alt_day3_duty:
        show us calml sport with dspr
    else:
        show us calml pioneer with dspr
    us "What do you mean «why»?"
    us "Do you even know how many things you can do with bugs!"
    if alt_day3_duty:
        show us laugh sport with dspr
        me "Yeah, yeah, Miku told me about one of those today."
        me "Thing."
    else:
        show us laugh pioneer with dspr
    us "Yes! It's a pity you didn't see this handsome man! Bug-stag, the size of a little finger!"
    us "Lena was screaming so loudly that I could hear it even at my cabin!"
    if alt_day3_duty:
        "I involuntarily imagined this picture - Miku holding a huge beetle in her palm, and Lena screeching nearby."
    me "And who do you want to make yell today?"
    "She grinned meaningfully."
    if alt_day3_duty:
        show us grin sport with dspr
        us "As if you don't know it yourself!"
        me "Me?!"
        "She shook her head."
        us "One more try."
        me "Who the hell?!"
        us "Well, think! Who is the most evil and bad adult aunt?!"
    "I gasped, guessing."
    me "No. You won't!"
    us "Actually..."
    "She shook the matchbox next to her ear."
    us "The start has already been made."
    us "It's up to you to decide whether to join the army of vengeance or go snitching around."
    menu:
        "Go and snitch":
            $ karma += 10
            $ lp_us -= 1
            $ alt_day3_us_bugs = 2
            me "Ulyana, I don't like it at all."
            "I said in a didactic tone."
            me "You must stop this immediately!"
            if alt_day3_duty:
                me "What, today's duty is not enough for you? Do you want more?"
                me "It's going to hit us both."
            if alt_day3_duty:
                show us upset sport with dissolve
            else:
                show us upset pioneer with dissolve
            "She frowned and said nothing."
            me "So, I'll go and tell everything to Olga Dmitrievna."
            if alt_day3_duty:
                show us dontlike sport with dspr
            else:
                show us dontlike pioneer with dspr
            me "You have time to disperse the bugs while I'm on my way to her house, after which you'll get a big kick."
            "I smiled wickedly."
            me "I won't get ricochet again this time."
            if alt_day3_duty:
                show us angry sport with dspr
            else:
                show us angry pioneer with dspr
            "Not listening to her yells, I turned around and left the dangerous territory."
        "I don't care":
            me "Do what you want, jeez."
            "I shrugged."
            me "Just don't drag me into this."
            if alt_day3_duty:
                show us upset sport with dspr
            else:
                show us upset pioneer with dspr
            us "Go ahead!"
            us "Nerd."
            "Not listening to her yells, I turned around and left the dangerous territory."
        "I'm in!":
            me "What a stupid questions you ask!"
            me "Of course I'm in!"
            $ karma -= 15
            $ lp_us += 1
            $ alt_day3_us_bugs = 1
            if alt_day3_duty:
                show us laugh sport with dspr
            else:
                show us laugh pioneer with dspr
            us "Great!"
            us "So, now let's go to the square and start fishing there."
            scene bg ext_square_day with fade2
            me "Anything special required?"
            if alt_day3_duty:
                show us smile sport with dspr
            else:
                show us smile pioneer with dspr
            us "You! Like a man!"
            "I was about to blush, but Ulyanka looked calmly and did not think to be embarrassed."
            me "Is that in what sense?"
            us "What do you mean «what sense»?"
            if alt_day3_duty:
                show us normal sport with dspr
            else:
                show us normal pioneer with dspr
            us "You're a man, so you must be strong."
            us "I saw a couple of slabs with ants, so there are insects under them."
            "She nodded at the fire shield."
            us "Get a hook or a crowbar and let's go."
            "I followed her instructions, and we went to the podium, from where Olga Dmitrievna usually reads her pathetic appeals in the morning."
            "The crowbar turned out to be a plump piece of iron, faceted with a square for greater grip, painted in disturbing red."
            "Apparently, from time and weather, the paint peeled off, and instead of a nice tool in my hands, I had a sad uglyness, mixed with rust and peeling red paint."
            "And, as addition, very heavy too."
            me "I hope we are not going to poke around at the center of the square?"
            if alt_day3_duty:
                show us calml sport with dspr
            else:
                show us calml pioneer with dspr
            us "I may have a stupid face, but I'm not stupid at all!"
            if alt_day3_duty:
                show us normal sport with dspr
            else:
                show us normal pioneer with dspr
            "She seems a little offended."
            us "Watch the slabs."
            us "I've been here since morning and checked."
            us "You see, this elevation is lined on all sides. And from the side of the bushes, where no one walks, too!"
            "Well, yes, the eternal perfectionism of a domestic builder."
            "It's a pity that it has sunk into oblivion along with perestroika."
            us "No one will see us there!"
            us "Anyway, look."
            "With the toe of her sandal, she traced a cross on the ground about two inches from the edge of the slab."
            us "So, you stick your stick here - make sure the edge is sharp, flat is not good."
            us "And then you hang on the other end, dropping down to pry off the slab."
            us "If I were heavier or stronger, I could do it myself."
            "She spread her hands in disappointment."
            us "But there seems to be a need for a man."
            if alt_day3_duty:
                show us laugh sport with dspr
            else:
                show us laugh pioneer with dspr
            us "So, get to work!"
            "And we got to work!"
            "The heavy crowbar sank into the sand, easily piercing through the turf."
            "I tried on and hung, trying to get it closer to the ground."
            us "More even! More even!"
            me "I'm trying! Stay out of my arm."
            "At the cost of a few calluses and a crushed leg, I finally figured out how and what to do, so it didn't even took three minutes for the first slab to be turned over."
            "And she gave the richest catch!"
            "I barely managed to jump back when some ants with wings, spiders and other vile creatures splashed from the fallen concrete road in all directions!"
            us "Oh, what a beauty!"
            "Ulyanka clapped her hands and, plucking a plantain leaf growing right there, rushed to catch especially disgusting-looking insects."
            "No, she was disdainful of woodlice and ants. She was more interested in various kinds of chitinous reptiles."
            "I stood at a distance and cautiously watched how Ulyanka, bursting into laughter, catching another threatening creature and puts it in a matchbox, from where a chorus of squeaks and rattles can already be heard."
            "Whatever Olga Dmitrievna did to Ulyanka, it seems that she decided to take revenge in earnest!"
            if alt_day3_duty:
                show us normal sport with dspr
            else:
                show us normal pioneer with dspr
            "It can be seen that the girl had remarkable experience in hunting insects!"
            us "That's it, I'll fan all the bastards now, and you can put it back."
            "«Hakuna Matata» suddenly started playing in my head."
            me "Is that all?"
            us "Of course not! I'm not leaving here until the boxes are full."
            "Does that mean at least two more such slabs?"
            "I was glad that she was not forcing me to catch them."
            "Well, that's right! Division of labor, as in all normal enterprises."
            us "Don't sleep!"
            "A sharp shout brought me out of my thoughts."
            us "Here's the next slab."
            "She drew a cross on the ground again."
            "..."
            scene bg ext_square_day with fade
            "When we finished, my back was buzzing and my crowbar-trampled limbs ached."
            "Actually, everything was hurting!"
            "I never thought that turning over some stones could be so hard!"
            "They, however, turned out to be not three, as I expected, but five - but even this turned out to be enough to callous my palms and thoroughly tint them with rusty red."
            "Which didn't seem to rub off!"
            "Hope it was worth it..."
            if alt_day3_duty:
                show us smile sport with dissolve
            else:
                show us smile pioneer with dissolve
            us "All right! We finished here!"
            us "Thanks!"
            "She waved and ran away, leaving me the last slab and a heavy crowbar."
            hide us with dissolve
            "Sighing, I put the concrete product in place and dragged the crowbar to the shield."
            "That's where Olga Dmitrievna caught me."
            show mt normal pioneer with dissolve
            mt "Semyon, where are you taking the crowbar?"
            "She asked suspiciously."
            me "Somewhere... To the fire shield."
            "Reluctantly, I answered. I have no strength left at all."
            mt "I see. Hmm."
            "She thought about it. The logic of my answer seems to have confused her."
            "She attacked the wrong one!"
            mt "And from where?"
            "She got her bearings quickly."
            me "From the ground, Olga Dmitrievna!"
            "I replied caustically."
            me "For a second it seemed to me that there was no place for a crowbar on the ground."
            me "Though if you think otherwise..."
            mt "No, no!"
            "She waved her hands."
            mt "Bring it. It's just not clear..."
            "She thought about it, but shook her bangs, apparently forbidding herself to waste time on incomprehensible questions."
            mt "Next meal is in ten minutes. Don't be late."
            hide mt with dissolve
            "She was out of sight, and five minutes later, putting the inventory back on the hooks, I followed her."
            "I wanted to eat terribly!"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_eventAf_admins1:
    scene bg ext_admins_day_7dl with dissolve
    play music music_7dl["ltyh"] fadein 5
    play ambience ambience_camp_center_day
    "Former good boy, former friend, loved-lover, former dreamer, former, former..."
    "I was sitting on a bench near the administration building, and most of all I wanted to just get up and leave."
    "I'm serious."
    "My instinct told me almost in plain text that if I stayed here a little longer, I would pass the point of no return."
    "After which everything will be different."
    "One day I decided to myself that I do not need people, that a smile is needed only in order not to go crazy, and that everyone is lying."
    "The story is short, but explainable and understandable - nothing frightening."
    "And people who were photoshopped alive in such a way that sometimes it was painful to look at their beauty, I reacted to them like they're pieces of furniture: with approximately the same interactivity."
    show sl normal pioneer with dissolve
    sl "Sitting?"
    th "Wow! How could you tell?! {w}Shaman, I guess."
    "I nodded."
    "Now that I have the time to understand myself and put my thoughts in order, I managed to return the already familiar ironic attitude to everything."
    "Including their own spiritual torments."
    "Events lined up in a single sequence: from acquaintance at the gate to yesterday's unintentional hugs."
    show sl smile2 pioneer with dspr
    sl "I'm sorry, I use you like this all the time."
    "The girl smiled shyly."
    sl "But according to the rules, it is necessary to be on duty together, and I have no one else to ask."
    me "Is that so? {w}What about the others?"
    sl "Miku is stuck at the club - she has a concert tomorrow, she needs to sort out all the details - I almost don't touch her."
    sl "Lena draws a wall newspaper."
    sl "Alisa is with her - she doesn't participate in her parents' concert, she is preparing for a gala performance, she is silent about the details, but she says that it will be bangers."
    me "And Ulyana?"
    show sl laugh pioneer with dspr
    sl "And I don't trust her!"
    "The girl answered with depressing honesty."
    play sound sfx_open_dooor_campus_2
    pause(1)
    scene bg int_admins_7dl with dissolve
    "With her magic bundle, she first opened the administration building,"
    play sound sfx_open_dooor_campus_2
    pause(1)
    scene bg int_chief_office_day_7dl at zenterleft
    extend " and then the door to the office of the head of the camp."
    show sl normal pioneer at cleft with dissolve
    play ambience ambience_int_cabin_day fadein 3
    "And I finally ended up in the holy of holies."
    "An office is like an office - it seems that they are all made according to the same patterns."
    "Dominating the room, of course, is a huge table with a sheet of plexiglass in the entire tabletop, under which various newspaper clippings, shift plans and five-minute notes (as a rule, the most stable long-livers)."
    "On the left hand in a small recess sits a phone - I picked it up - seems to be working."
    sl "It's internal."
    "Slavya understood my thoughts correctly."
    sl "We wanted to connect an external phone, but something didn't work - I don't know about the whole story."
    sl "So you can only call among the camp."
    show sl smile pioneer with dspr
    sl "Such a useful device."
    me "Where can you call?"
    "Slavya wrinkled her forehead funny, remembering:"
    sl "To the infirmary, to the boat station, to my warehouse and, it seems, to the canteen. {w}Looks like that."
    me "Yeah, the abyss of usefulness."
    "I snorted, regretfully giving up on the idea of ​​calling the president of the world and demanding that I be returned to my homeland."
    "Although regarding current year, the issue of returning became rather ticklish."
    "After moving from the center of St. Petersburg, I lived in a sixteen-floor building, which was built in the early 2000s."
    "That is, as you might guess, at this time my skyscraper had not even been built yet - there was nowhere to return."
    "Unless to see relatives? In St. Petersburg. {w}Oh, yes. It's still called Leningrad here."
    "The next item worthy of attention was a huge modular wardrobe, to which Slavya immediately went."
    sl "Semyon, not for service, but for friendship..."
    me "Yes?"
    "There was a stool next to the closet and, judging by Slavya's look, it was necessary to get to the top."
    hide sl with dissolve
    "Sighing, I perched on the stool."
    th "I wish it was the other way around!"
    dreamgirl "Yeah. She'd be like that on a stool, and you can see everything, and you're, like, support her, and she lose her balance."
    dreamgirl "And you catch her, and in flight you can even touch different places - anyway, in the end, the winner is rewarded: a kiss from the rescued blonde!"
    dreamgirl "A classic of the genre!"
    th "Erotic fantasies."
    me "Why not yourself?"
    "I shared the thoughts of the inner voice."
    me "You yourself said in the morning that you can't lift a boy."
    "I opened the doors - and for a good couple of minutes I fought with the photographs, albums, bags, Christmas tree tinsel and other paraphernalia of the life of a pioneer camp that fell from there."
    sl "I'd be happy to."
    "Laughter came from below."
    sl "Who doesn't like being caught in arms?"
    sl "But, unfortunately, I can't get there - you would have to lift me up."
    me "Don't go on, I get it - you don't trust me that much yet."
    sl "Semyon!"
    me "That's it, I'm silent."
    with fade
    "I almost personally imagined how the girl sits on my shoulders, I unbend, we are trying to catch the balance, and under the palm of the girl's tender skin."
    "I shook my head, driving away the obsession."
    "Incredibly attractive obsession, not gonna lie."
    me "So why am I here?"
    "I asked, finally having won a decisive victory on both fronts: in the war with the contents of the closet, and in the difficult battle with my own libido."
    sl "Look to the right, please: there should be a stack of blank albums - give them to me."
    sl "And next to them is a box with the Roman numeral II on it. See?"
    "A few minutes later we sat on the floor, surrounded by albums and pictures."
    show sl smile pioneer with dspr
    sl "Photos are taken by Uncle Borya - he has a trained eye."
    if alt_day2_mi_snap:
        sl "All pictures in albums - his work."
    else:
        me "Gym teacher? Really?"
        sl "What surprises you? {w} In the old albums, all the pictures are his work, he must have learned something during this time, right?"
    me "Everything is how much?"
    sl "Well, since the camp was founded in 1974. {w}Imagine, I was nothing years old at all then, and he was already taking pictures of the pioneers."
    show sl laugh pioneer with dspr
    sl "Not while forcing them to make an extra twenty circles around the field for some kind of fault, of course."
    show sl normal pioneer with dspr
    sl "Here are the pictures he took this shift."
    "Slavya said, taking out a thick pack of cards from the box."
    sl "Uncle Borya is very greedy for such things, he thinks that all the good moments should be captured. {w}And since the album is not infinite, we have a very responsible task ahead of us."
    "The album already said: «Sovyonok, II shift, 1989», apparently, someone had already prepared the albums in advance."
    stop music fadeout 3
    sl "We have to choose - what will go into the album, and what will go to Uncle Borya's home archive."
    hide sl with dissolve
    "The first 100 photos, tied with rubber bands, were related - funny but true - to the first three days."
    "Check in - the pioneers who poured out of the bus, dressed for the time being, whoever is in what they want."
    play music music_list["farewell_to_the_past_full"] fadein 3
    "The photos were in black and white, which only added to them some inexplicably warm charm."
    "Here's Lena - in a rather daring dress that reveals her upper back, stands holding a suitcase in front of her and blushes for the camera, and it looks both funny and cute."
    "Here is Alisa and Ulyana - laughing, pleased with something, giving each other «high-five»: a yonger one in her usual T-shirt, an older one in a separate sports uniform that she wore yesterday while exercising."
    "But Slavya - in a sarafan."
    me "Oh, what a beauty!"
    show sl shy pioneer with dspr
    sl "Flatterer!"
    me "No, really! Very beautiful. What is that on the dress by the way?"
    show sl smile pioneer with dspr
    sl "If you don't skip the evening dances, you'll see it yourself, and I'll tell you!"
    me "Got it!"
    "I shook my finger at her and went back to studying the photographs."
    hide sl with dissolve
    "And here's one - torn in half, but lovingly glued together with casein glue."
    "Did I say Lena's dress was daring? {w}Whoo, how wrong I was."
    "The photo was of Miku."
    me "How did they even let her off the bus in this?!"
    sl "What?"
    "Slavya looked over my shoulder, and for a moment I inhaled her breath, felt the warmth of her cheek next to mine."
    sl "Ah… {w}That scandalous dress!"
    sl "She got off the bus in a T-shirt and shorts like Ulyana! {w}The dress she wore to dinner."
    sl "You know what reaction was."
    "I shook my head and put the photo back in future home archive."
    "Although there was a terrible temptation to quietly and peacefully privatize the ownerless picture."
    dreamgirl "So let's do it! Tell her that a Tyrannosaurus rex flew past the window, and while she looking away, hide it under the belt."
    "Out of thirty shots on the first day, the high court in the person of me and Slavya recognized only six as suitable - which the girl immediately fixed in the album."
    "The work was not very hard, and it turned out to be easier than it seemed at first glance: it was enough to sift out the photoes that did not have cropped faces, backs, grimaces - and put the photoes suitable for the album next to Slavya."
    with fade
    "So it was not surprising that after half an hour of such mechanical work, I got a little bored."
    "And quite logically decided to brighten up the time with a conversation."
    me "Slavya, can you tell me something about yourself?"
    show sl normal pioneer with dspr
    sl "Meaning?"
    "I felt myself blush."
    "I hate to be in this situation - when a girl does not understand you."
    "Girl you like."
    "Yesterday's heavy boot wasn't heavy enough, apparently."
    if alt_day2_walk == 2:
        me "Remember, yesterday we were talking about what it's like to be a squad leader's assistant."
    else:
        me "You see, in the evening, while I was trying to escape from you, I realized that I had thought out God knows what for you. {w}I don't know anything about you."
    "I clarified."
    show sl serious pioneer with dspr
    sl "Meaning?"
    "She frowned."
    sl "I'm not against it, but I'm not going to tell you my whole life!"
    me "I don't think that's such a bad idea."
    "I chuckled."
    me "But we really don't have that much time... If only by the fire, in the evening with a guitar..."
    show sl smile pioneer with dspr
    sl "By the way! {w}The day after tomorrow there will be an evening bonfire."
    me "Oh, one more thing I always expect from camp. {w}But we kind of drifted off topic very smoothly!"
    "I shook my finger at her."
    me "Let's do this: what you think is necessary to say - imagine that we are completely, completely unfamiliar (especially since this is true) - and you need to tell the most necessary about yourself."
    me "Imagine a big room."
    "I looked around the head's office."
    me "There's a table in the middle. {w}And two chairs on either side of it."
    "Except for the head's chair, there were two chairs on either side of the table."
    me "We had never seen each other before, we didn't even know we existed."
    me "And..."
    show sl smile2 pioneer with dspr
    sl "Oh..."
    "Sorting the photoes of the second day of the session - publicly recognized day of turmoil - she sighed."
    sl "Okay, let's try."
    sl "Hi! My name is..."
    "I discreetly clicked the record key and placed «walkman» between us so that not a single word is lost."
    sl "I'm from the district center, located nearby, I ended up in the camp when there was distribution of vouchers between teachers - one went to my father."
    "Slavya's voice was like a lullaby - it was so even and pure. Not a single aggressive note, unevenness or insincerity."
    sl "This is not my first time here, this year I wanted to bring one of my younger brothers, but dad decided to give the second ticket to Lena's father, so she is also here - not the first time either."
    me "One of?"
    show sl laugh pioneer with dspr
    sl "And there are seven of us, like in a fairy tale. {w}I'm exactly in the middle, the fourth."
    sl "Although in the family I'm constantly playing the role of the second mother..."
    sl "After moving to the city, she began to give lessons at preparatory courses for children of five or six years old, helping them get used to school, so she comes home late, at eight o'clock - you know, by that time you have to feed everyone."
    show sl sad pioneer with dspr
    sl "I've never been spoiled by attention - that is, when there are nine people at home, it's never lonely, of course, but mom just wasn't enough for all of us."
    sl "So I was looking for myself."
    sl "First in studies. {w}Then in social activities."
    sl "And then some family life."
    me "And now?"
    me "I'm surprised you left your extended family to your parents!"
    show sl happy pioneer with dspr
    sl "Don't slander them, they're good! And now they're on vacation, so my brothers will be taken care of."
    sl "And I'm taking care of the whole camp - it's like something alive, you know?"
    "Her eyes sparkled - it seems that for a long time there was no understanding listener."
    "Especially on a topic about which she, it turns out, was ready to rant for a long time, without repeating herself and not getting lost in particulars."
    stop music fadeout 3
    with fade
    "I almost did not listen to what Slavya says - will listen to the recording again, if necessary."
    play music music_7dl["shape_of_my_heart"] fadein 3
    "I listened more to the sound of the voice."
    "Looking at how she behaves."
    "For a while it seemed to me that she was with me all so sweet-beautiful-good because she needed something from me."
    "The ugly duckling complex."
    "A little later, albeit with her most active help, I survived this complex."
    "But in that case, the question of her kindness remained open."
    "Her eyes are full of sympathy and adoration - but not because I am me."
    "But because I am also part of the world around me."
    "That's all."
    "That's..."
    "What has been spinning in my head all this time has finally formed into a final thesis."
    th "It's just that she has an emotional threshold five times higher than mine."
    show sl normal pioneer with dspr
    th "Where it has a neutral mark, I've been jumping for joy for a long time."
    th "Where she walks and smiles at people, I usually walk around with an unsociable face and look at everyone as if they were nothing."
    "I once again realized the depth of the abyss that separates me from these girls."
    dreamgirl "That's not what you're should be thinking."
    th "Yes, that is. I took her friendliness as something personal - and she spews it like caviar."
    dreamgirl "Not, it's not. {w}You need to think about how you can completely turn her friendliness on yourself."
    th "Exactly. {w}Propose to her: {w}«Come on, will you forsake the whole camp and babysit me alone?»"
    "Slavya cut herself off in mid-sentence."
    sl "Again, huh?"
    me "What?"
    show sl serious pioneer with dspr
    sl "You promised me you wouldn't shut in yourself anymore!"
    me "I promised to try."
    "I cracked up."
    me "I tried it. {w}It didn't work out very well."
    show sl normal pioneer with dspr
    sl "Can you tell me what's wrong?"
    th "Yeah. Give me a second, and I'll tell you everything."
    show sl smile pioneer with dspr
    sl "Semyon... Syom."
    "She put down a stack of photos from the day of Neptune and caught me by the shoulder."
    sl "Well please, tell me what's the matter?"
    th "You matter. {w}You got too close."
    "Her voice was unusually low and... velvety, or what?"
    show sl shy pioneer with dspr
    sl "Syom."
    show sl tender pioneer with dspr
    extend " Syoooomushka."
    "She tilted her head to the side."
    sl "Pleeeeease."
    "Oh, who would have known how embarrassed I felt right now!"
    "And it seems that I shouldn't speak - I just forgot how I allowed myself to blurt out too much yesterday - and it's impossible to be silent."
    th "I wouldn't leave. I'd sit and rub the rim of the glass or the ring."
    th "And looked at the neck, collarbone, throat, shirt collar - but not in the face."
    "Memory, what are you doing to me..."
    me "Nothing."
    "I couldn't look her in the eyes."
    sl "Semyo-on!"
    "To complete the picture, it was not enough for her to crawl up to me and start tickling."
    "And then only to ventilate oneself through the window, choking on caustic hatred, breaking it with rings against the dirty glass, on the other side of which there was a man with the bright eyes of a dreamer."
    "Because I can not."
    me "Nothing."
    th "I really want her to adore me, pamper me and take care of me..."
    "Because I dare not."
    play sound sfx_open_door_kick
    pause(1)
    scene bg ext_admins_day_7dl with flash
    "I exhaled convulsively and ran out of the office."
    "Jumped out outside."
    "It was unbearably cutting to stay in the room where my mute cry for help hung like a transparent smoke."
    "Where the worst thing was that she heard this scream and understood why it sounds."
    "Slavya shouted something from the window, but I no longer paid attention to it."
    "I knew perfectly well how it would all end."
    "Diligently strangled and strangled unnecessary emotions in myself - but it did not work while she was around."
    "I need vodka to the point of nausea and loneliness, to the howl of a wolf."
    "Otherwise, I will fall upon her with all my weight, with all my far-fetched problems, incomprehensible demands and ruthless expectation of a miracle."
    "Is it conceivable that a person takes up so much space in one's head? {w}On the third - just think! Third! - day of acquaintance."
    scene bg ext_square_day with dissolve
    "Is it conceivable that an adult, long over twenty-five, behaved like a hysterical fool?"
    th "What's wrong with me?!"
    dreamgirl "Nothing. {w}Roll. Roll."
    th "Bottle on the freeway?"
    dreamgirl "Is it scary to admit to yourself that your young body controls your wise mind?"
    dreamgirl "Is it scary to understand that you yourself have gone not far from him in development, from your body?"
    dreamgirl "So roll. Roll. {w}Clog your head with sunflower husks, hide somewhere under a bench."
    dreamgirl "Do you have a place in mind where you can hide...{w} from yourself?"
    th "But what should I do?!"
    play sound sfx_7dl["eat_horn"] fadein 1
    "A horn sounded from the direction of the dining room."
    stop music fadeout 3
    dreamgirl "Half past five in the evening."
    $ counter_sl_cl = 5
    if alt_day3_duty:
        dreamgirl "What to do?"
        dreamgirl "Go on duty. It's time for lunch."
    stop sound fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_sl_postlunch:
    play music music_7dl["tilltheend"] fadein 3
    scene bg int_dining_hall_day with dissolve
    "The lunch passed in a blur."
    if alt_day3_duty:
        "I kept silent, never sat down at the table, constantly on my feet, on the run - feeling an inquiring, probing look on me."
        "And constantly tripping over it."
        "So when the lunch was over, I breathed a sigh of relief."
    scene bg ext_dining_hall_near_day
    with dissolve
    "When I went peddling, I used to close all the windows and doors, take out the SIM cards from my cell phone, turn off the Internet, turn off the electricity and, sitting in the dusty twilight, pumped up wormwood tincture until my face began to acquire the same pale green color."
    "At one time, a girl introduced me to absinthe..."
    if loki:
        "Who ruined the rest of my life. And why here is an equivalent replacement, I wonder?"
    elif herc:
        "Almost becoming Sycheva - that's a paradox."
    else:
        "Who I don't remember for some reason."
        "I remember gentle touches on the face, brown eyes, dimples on the cheeks - abruptly, in features."
        "That's it."
    "At one time, I tried to get outside a little - and each such trip could charge me with mood for a month ahead."
    "I literally was drowning in a good mood - a paradox! {w}Everything is bad at home, the salary is barely enough to pay utility bills, and I'm happy."
    "I had nothing and I didn't need anything - a couple of hundred for travel, a pack of cigarettes and some cheese puff in the supermarket."
    "But time went on."
    "I was getting old alive, looking for reasons not to be with people at first, then not to do anything at all."
    "What's the matter... I've even stopped doing self-development."
    "Once upon a time I was so warmed by the idea of ​​becoming smarter than yesterday, stronger, more logical, more interesting every day."
    "To write a text, and six months later read it, be horrified and rewrite it so that it takes your breath away."
    "The incentive to prove something first of all to yourself."
    scene bg ext_dining_hall_away_day at zexitleft
    with dissolve
    "Sunk into oblivion, like everything that was before."
    "And it's not about some great misfortune."
    "Just one day, as if the clockwork toy ran out of wind, the spring got tired, and the wheels refused to roll further through life."
    "I don't know...{w} Maybe if I'd once met a girl like Slavya along the way, I'd still be rushing over the pavement at the speed that only a cloudless mood and well-laced shoes can give."
    dv "Are you hiding from Feoktistova?"
    show dv grin pioneer2 at cleft with easeinright
    "There was a mocking voice from behind."
    "I shuddered:"
    me "How did you know?!"
    "Alisa. Of course. I could almost visibly sense the impending trouble."
    show dv smile pioneer2 with dspr
    dv "And what is there to know - it's clear as it is, you hid from her behind the column for the whole lunch, like a fool on the bride."
    dv "Did you have a fight or..."
    "Here she lowered her voice:"
    dv "Did you confess your love to her?"
    me "Redhead!"
    show dv laugh pioneer2 with dspr
    dv "How violently you react!"
    "She burst out laughing."
    dv "Did I guessed right?"
    dv "Did you confess your love to her? Are you lovers now?"
    "I chose to ignore her."
    dv "Hey, what's wrong?"
    th "Woodweed Stupid."
    dv "Are you offended?"
    th "No, I'm just ecstatic."
    show dv normal pioneer2 with dspr
    dv "Well, in vain, I'm better... {w}Feoktistova for ten hours!"
    me "Where?!" with vpunch
    "I jumped up on the spot, ready to run in different directions at once."
    show dv laugh pioneer2 with dspr
    dv "Got you!"
    me "Go, you know where!"
    "I felt myself boiling over."
    dv "You shouldn't have ruined our blondie. {w}She's not your field."
    "Alisa chuckled."
    "She seemed to be more amused than frightened by my outburst."
    dv "I'll go before they say I'm bullying newbies."
    dv "And if you want to hit on her - think for yourself what you're worth."
    stop music fadeout 3
    hide dv with dissolve
    th "Wow."
    "I looked after her, and then myself went where eyes looked."
    stop music fadeout 3
    scene bg ext_camp_entrance_day with dissolve
    play ambience ambience_camp_entrance_day fadein 3
    "And they looked, again, towards the exit."
    "Looks like, despite all the enticements of the local communist paradise, the wolf continued to look into the forest."
    "Such an ungrateful creature human is."
    if alt_day_binder != 1:
        "Except for the bus that was missing somewhere, dragging my coat into the unknown distances, everything was the same here."
    "The raging greenery of acid shades, the bottomless blue sky and the air floating from the heat, streaming up over the asphalt in streams."
    "Everything was like that in this crazy world, everything was normal and on schedule."
    "Only I was knocked out, a dirty stain on the carpet."
    play music music_7dl["silent_angel"] fadein 3
    "I raised my hand to my eyes - I saw this gesture somewhere, either in a movie, or in some kind of game."
    "Not a bad gesture to make sure I still have control over reality and that my limbs are not too late to respond to brain signals."
    "And only I was convinced that I had successfully escaped from the whole camp, from all the obnoxious bullying redheads, from the painfully understanding blondes and from the evil squad leaders, who only give... "
    play sound_loop sfx_far_steps fadein 1
    "I heard someone's footsteps."
    "And groaned."
    "Who would doubt - they won't let me be alone today."
    "Perhaps if I ran somewhere in the woods and ran for a long, long time..."
    "And even that's not a fact."
    stop sound_loop fadeout 4
    "The gates creaked, and to my eyes appeared..."
    show sl smile pioneer with dspr
    me "There's no getting away from you at all, is it?"
    "I muttered."
    "Smiling. She smiles all the time."
    "And the eyes are blue-blue."
    "I wonder how she does it? {w}I'm ready to lay my left finger on the fact that no one saw me while I was trudging here."
    sl "Poor, poor Semyon."
    show sl smile pioneer close with dspr
    "She sighed as she sat down next to me."
    "Again I was overwhelmed with an incomprehensible, hard to express feeling - as if I had fallen under a warm gust of wind, or the sun peeked out through the clouds."
    "She got along with everyone on a subconscious level - that's probably why Dvachevskaya so diligently stayed away from her, rightly fearing to fall under the charisma."
    sl "Tossing about, doubting, afraid."
    me "What does it all mean?{w} How did you find me?"
    show sl smile2 pioneer close with dspr
    sl "Yesterday... When I hugged you..."
    dreamgirl "She put a «beacon» on you!"
    th "Yah. Not that level of technology yet."
    dreamgirl "And what if - she's interdimensional KGB agent and now she's enlisting you to give up the secret of «Coca-cola»."
    sl "And today, when over the shoulder..."
    sl "I don't know."
    "She smiled."
    sl "It's just that now I can put myself in your place - understand what I would do if I were you."
    dreamgirl "Electrosense? Pfft, let's get back to the «beacon» hypothesis? {w}They're at least scientifically explainable."
    th "The ability to think like another person is also scientifically explained."
    "Slavya was in her repertoire again: sweet, kind, charming."
    "I couldn't rise my hand to do what I wanted most of all - to strangle her properly and interrogate according to the laws of wartime."
    "I tried to console myself with the thought that, on occasion, I can strangle Dvachevskaya instead."
    me "Not bad, Sherlock. What's next?"
    sl "You ran away so suddenly, like I did or said something bad."
    sl "I wanted to apologize if so."
    me "And that's why you were looking for me?!"
    show sl happy pioneer close with dspr
    sl "I think you should live in peace with your surroundings. {w}And you tried so hard to pretend you don't exist, so I decided to not find you behind that pillar."
    sl "I decided to talk later and without witnesses."
    $renpy.notify('Mario Francis Puzo - was an American author, screenwriter, He is known for his crime novels about the Italian-American Mafia.')
    th "Wow, spoke up almost like Puzo's hero!"
    dreamgirl "Watch out, she can get «Tommy» out!"
    show sl serious pioneer close with dspr
    sl "Semyon, you're probably tired of me worse than bitter radish."
    sl "But I just want to remind you - dance today. {w}And you promised me a dance."
    sl "Don't run away, please."
    "Brrrr. {w}No matter how simple the local gray eminence wants to look like, she could see right through me."
    sl "I'll be sad without you."
    "Slavya comfortably poked her forehead into my shoulder and looked frowningly with her blue headlights, shining through."
    sl "And we don't have boys, and the ones we have don't want to dance. Well? Will you stay?"
    me "No."
    "I grumbled."
    me "I'll drop my slippers and a pedestrian to the local district center. {w}How far is it, by the way?"
    show sl smile pioneer close with dspr
    sl "Three hundred kilometers."
    "Slavya was already smiling."
    sl "Are you really going?"
    "And now try figure her out, is she joking or asking seriously?"
    me "Yes. I'm tired of you. {w}All you do is make me feel stupid."
    sl "Sorry."
    "She sighed."
    show sl shy pioneer close with dspr
    sl "I'm ashamed to admit, I'm a little embarrassed about you, like, I didn't do anything bad to you, but I'm embarrassed."
    sl "Now you'll leave, and I won't understand anything."
    "Well, what should I do with her?"
    th "And what, damn it, freedom, equality, brotherhood..."
    "The donkey was angry today, he found out that he is a ram."
    th "And I, instead of tearing the hair on my head and running around, trying to understand who tested the time machine on me, I sit and try to breathe every other time, because only two layers of shirts divide us..."
    show sl normal pioneer with dspr
    "Slavya recoiled, as if reading my thoughts."
    "And I regretfully followed her with my eyes, such a warm, sweet, affectionate..."
    sl "But maybe you'll change your mind?"
    show sl smile2 pioneer with dspr
    sl "Or let's go together? Like in the song: «if it's a long, long, long, if it's a long walk», remember the words?"
    "I laughed as I felt the awkward paralysis that had shackled my body for the past two hours crumble away."
    "Next to Slavya, it turned out to be either honest or hostile."
    "And all this would be the same as to hit with a fist on these ideally shaped lips, to shred the happiness splashing under the eyelashes."
    "Of course, I heard about idiots that splash hydrochloric acid on canvases, but unfortunately or fortunately, I was not one of them."
    me "I'm not going anywhere."
    "I confessed, realizing that I was saying much more than the words meant."
    "Almost tangible context."
    th "She really bewitched me?"
    "Because it can't be at first sight, can it?"
    "It can't."
    "Yes?"
    show sl smile pioneer with dspr
    sl "Well, if you don't want to run anywhere, why don't we go to the camp?"
    sl "I have one more task for you, you love them so much."
    "And here she definitely scoffed!"
    "But with such a sincere look."
    "And so touchingly stretching out her hand to me."
    stop music fadeout 10
    menu:
        "If you insist..." if counter_sl_7dl == 3:
            "You would have to be the last idiot to refuse."
            "How else?"
            $ counter_sl_7dl = 4
            $ lp_sl += 1
            stop ambience
            play music music_7dl["carefree"] fadein 3
            scene bg ext_stage_big_day_7dl
            show sl normal pioneer
            with dissolve
            me "Who would doubt..."
            me "I won't take your word for it anymore - you'll make me work again."
            show sl laugh pioneer with dissolve
            "A certain stir was already planned on the stage - and two speakers, turned off, were already waiting in the wings on the edge of the stage."
            me "Yeah. Them?"
            show sl normal pioneer with dspr
            "Slavya nodded."
            "Moreover, for her, it was something normal that she would also carry heavy things."
            "Involuntarily, you begin to believe that she grew up in a male surrounding."
            sl "Well, let's go?"
            "Ohoho, heavy sins of mine..."
        "Task?" if (counter_sl_cl == 5) and (counter_sl_7dl != 3):
            me "Can I consider?"
            sl "There's nothing to consider! Let's go!"
            me "Good. But then don't be surprised if I get down or blue."
            show sl happy pioneer with dspr
            sl "We'll survive this trouble! {w}Let's go!"
            sl "Great deeds await us!"
            $ counter_sl_cl = 6
            $ lp_sl += 1
            "About what those great deeds were, I realized only when I got to the stage."
            stop ambience
            play music music_7dl["carefree"] fadein 3
            scene bg ext_stage_big_day_7dl
            show sl normal pioneer
            with dissolve
            me "Who would doubt..."
            sl "We need to move the speakers to the square. Can you help?"
            me "As if my consent matters."
            "I grumbled as I grabbed the edge of the speaker."
        "Maybe later?":
            me "I'll sit for a little longer.{w} I have some things to think about, but all arrangements stand."
            me "Okay?"
            show sl normal pioneer with dspr
            "The girl's smile faded, but she nodded in understanding."
            hide sl with dissolve
            "And no longer annoying me, she disappeared behind the gate."
            "And I allowed myself to move only when it was half past seven on the clock."
            "And went."
            if alt_day3_duty:
                "On duty."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_eventAf_me_mt_house1:
    scene bg ext_house_of_mt_day with dissolve
    play sound sfx_open_door_clubs
    pause(1)
    scene bg int_house_of_mt_day with dissolve
    "Sleeping seemed like a great idea to me."
    "And let the whole world wait."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_eventAf_library1:
    scene bg ext_library_day with fade
    play ambience ambience_camp_center_day fadein 1
    if counter_un_7dl == 4:
        call alt_day3_day_un
    else:
        "There's nothing interesting here."
        "Quiet hour!"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_day_un:
    scene bg ext_library_day with dspr
    play music music_list["get_to_know_me_better"] fadein 5
    $ counter_un_7dl = 5
    "In the same place."
    "I again, as in the morning, stood at the library building and lazily wondered if I should go there."
    "I didn't want to see the bespectacled beetle. Both bespectacled beetles."
    "The mushroom gave me a headache."
    "And I'll have to deal with them."
    th "Perhaps we could arrange another distraction?"
    dreamgirl "You haven't been hit for your previous maneuver yet, do you want to aggravate the situation?"
    th "But I'm sick of talking to these characters!"
    dreamgirl "Be patient. You don't want to upset Lenochka."
    th "Ass-hole."
    "Sighing, I pushed the door open and went in."
    scene bg int_library_day with fade
    show un smile pioneer with dissolve
    "Lena was already waiting for me inside."
    "On the table was a square leather bag with a strap, which, apparently, contained all the things necessary for the artist."
    "This, and even a tablet to draw on your knees - and only a beret is not enough to get the look of a real French artist."
    un "You've come? Good."
    un "Take paint, brushes, but be careful."
    show mz bukal pioneer at left with dissolve
    mz "What do we have here now, a dating house?"
    "The raspy voice of a buzzkill came from behind."
    "Looks like she woke up."
    "And Lena did something that surprised me."
    show un rage pioneer with dspr
    un "Not your " with vpunch
    extend " Freaking " with vpunch
    extend " Business!" with vpunch
    "In three steps she barked - so much that even I sat down."
    th "Here's a quiet girl for you."
    show un shy pioneer with dspr
    un "Oh, I'm sorry, did I scare you?"
    "She smiled guiltily."
    mz "So, if Olga asks tell her you went kissing right?"
    "It seems that the buzzkill does not understand simple hints, even expressed in the most obscene form."
    "We'll have to explain in a human way."
    me "If Olga asks, say you were asleep."
    me "And if rumors spread around the camp, we'll know who to call to account."
    me "You were looking for something with your face on the tabletop. Here, get busy!" with vpunch
    "I yelled."
    "Lena in the background chuckled."
    "We flew out of the library."
    play sound sfx_open_door_kick
    scene bg ext_library_day with dissolve
    show un laugh pioneer with dissolve
    un "Semyon."
    un "Is there anything you can do to keep this from being a comedy?"
    me "Why?"
    "I was surprised."
    me "I love hearing you laugh."
    me "That alone would be worth turning everything into a farce."
    show un smile pioneer with dspr
    un "You understand that Zhenya will be offended by us?"
    me "It's her fault!"
    "I folded my arms across my chest."
    me "She disliked me from the first look, now she's paying for it!"
    "Lena just shook her head."
    "This time, she did not grab my hand with her palm - after all, the dimensions are incomparable. It's also hot, hold someone's hand in such weather."
    "Instead, she hooked her index finger on my little finger and walked for a while, enthusiastically swinging the resulting hitch."
    "She seemed to like the feeling, because she nodded with a «we walk like this» look from now on."
    me "You and I walk like juniors, holding hands."
    "I noticed. The bag was noticeably heavy, but I didn't want to complain."
    show un grin pioneer at center with dissolve
    un "But you are jun, and I'm jun."
    un "Life is to be enjoyed, not to walk around with a serious and intelligent expression on your face."
    me "A couple of days ago, you thought otherwise."
    "Cautiously, I remarked."
    scene bg ext_warehouse_day_7dl with dissolve
    "This time we did not run away anywhere and chose a warehouse as a place for drawing - especially since it was quite picturesque here, and two extremely convenient steps ran down from the warehouse itself."
    show un serious pioneer with dissolve
    un "I was different a couple of days ago."
    "Lena nodded in agreement."
    un "There was no one to smile at. And to rejoice, for that matter."
    me "Now there is?"
    "She looked at me meaningfully."
    "I held my gaze. Thoughts from lunc suddenly resurfaced in my head."
    "Shaking off the stair, I sat down myself and nodded invitingly to the girl:"
    me "Let's chat?"
    show un normal pioneer with dspr
    "She nodded, sitting next to me, somehow strangely, on the side, hugged me, looked for a more comfortable position and finally calmed down."
    un "So what did you want..."
    me "About us, probably..."
    "I said thoughtfully."
    me "We had a magical morning, but the way it ended and what happened at lunch made me think about one thing..."
    "I took a break, but Lena seemed to be full of patience, because not a word, not a single gesture hurried me."
    "Specially checked if she fell asleep - no, she sits cuddled up and listens to the sounds of my voice."
    un "Go on."
    me "Where I come from, there is a concept of the friend zone. In the vast majority of cases, this means excommunication from the commissar's body for the most far-fetched reason. Moreover, the applicant may have the most positive qualities."
    me "There's even a phrase — ah, I wish I had met a guy like you."
    me "I may not be the strongest physiognomist or sign reader, but your behavior, your very posture and jumpy reaction to the fact that I exist - as if they say that you perceive me as something native."
    me "But not close."
    show un shy pioneer with dspr
    un "Mmm... Is that even possible?"
    "She inquired softly."
    me "Actually, anything is possible."
    me "I just wanted to tell you that it's too late to turn the wheels - friendship won't work for me, you know?"
    "She seems to have smiled."
    un "Stupid. Don't you realize that you can be friends with someone you like at the same time?"
    me "I would like to believe."
    "I shook my head."
    un "Doubly stupid."
    "She got her fingers under my shirt and melancholy drew some patterns with her nails right on the skin."
    show un laugh pioneer with dspr
    "I twitched all over from the tickling, and she laughed in response."
    if loki or herc:
        play music music_7dl["lunar_anguish"] fadein 4
        show un normal pioneer with dspr
        "And suddenly she calmed down, sobbed, all leaning towards me."
        un "Friend - how much is in this word? Someone with whom you feel easy and good."
        un "Maybe it's the one who didn't turn away from you when everyone else just left?"
        un "Why do you need a hysterical me when you have a lot of those who are better, softer and more accommodating?"
        if lp_mi >= 4:
            un "Miku - and I know how you like her. From the first moment you met. Remember?"
        elif lp_dv >= 4:
            un "Alisa.. I see how you look at her."
        elif lp_sl >= 4:
            un "This stupid Slavya, who, well, absolutely does not understand anything and does not want to understand."
        "I was about to say something, but she dug her nails into my skin."
        un "Be quiet. You don't know anything."
        un "An unfamiliar, pure boy who seems to have been brought here from the snowy streets of a much scarier and crueler world."
        un "I've been watching you since the first day, from the first minute."
        un "How you walk, move, breathe."
        un "I catch your reflections in the glass and the sound of words in the hot air."
        un "You are not of this world, you are what was given to me, either as a reward or as a punishment."
        un "One way or another, but you are my chance to break out of this vicious circle into which I have driven myself."
        un "A shy girl, staring at the floor, unable to do anything but hide behind a plate or easel."
        un "And it rarely one can think that I might want something, just scatter, for example, all worries in dark corners and expose myself to the vast sky."
        un "Imagine that there, above, is the ocean, just waiting for a person to stop forbidding himself to dream."
        un "And the first dreamers set off towards the sun, with heads full of light, with hearts full of fire."
        un "Perhaps there will be a place for me one day."
        "She sighed convulsively again, almost sobbed, and I, a little discouraged, did not find anything better to do than put a hand on her shoulder and stroke her soothingly."
        "And she continued her feverish whisper, as if afraid that a drop of unspent anguish would remain inside and ferment, degenerating into something... ugly."
        "Unexplained emotions never give birth to beauty."
        un "Sometimes I draw these pictures, and they tear and crumple them, calling me a schizophrenic, unable to draw something really beautiful."
        un "But how am I unable?"
        show un cry pioneer with dspr
        "She looked up at me."
        un "If I managed to draw you?"
        un "Draw and disappeared."
        if lp_mi >= 4:
            un "I took you away from that Japanese girl because you are mine. All mine."
        elif lp_dv >= 4:
            un "I took you away from Alisa because she doesn't need anyone. And you are mine."
        elif lp_sl >= 4:
            un "I took you from Slavya because you are mine."
        if loki:
            un "Because without you, I can only bite my fingers into the blood and measure the pain with hours until the moment of our next meeting."
        un "And you are saying «frinedship»."
        "She fell silent and clung with all her might, as if I really could now dissolve in the hot air."
        un "And you come, confident, looking cheerful and ruthless, and I can't stand your look, it's so physically heavy."
        un "And your actions - illogical, chaotic, incomprehensible to anyone - line up in some kind of pattern, as if you live thousands of lives at a time, choosing only the options you like and discarding unnecessary and bad ones."
        un "It's like you can play back every choice you make and arrange events the way you want."
        un "I dare not come any closer, because I might be in one of the realities you discarded."
        un "And I don't want to be discarded. I want to be where you are."
        dreamgirl "Nice dialogue."
        dreamgirl "Why did you make the girl cry, you monster?"
    else:
        show un shy pioneer with dspr
        un "I don't even know how to react to what you're saying."
        un "On the one hand, of course, I'm flattered by how much I mean to you."
        un "But your distrust..."
    dreamgirl "Of course, it is critical for you that she considers you as a romantic object."
    if loki or herc:
        dreamgirl "But you can pick better words, right?"
    me "Forgive me."
    show un cry_smile pioneer with dspr
    un "For what?"
    me "For everything."
    me "For this stupid talk."
    me "For doing everything not right and straight up wrong."
    me "I've read a bunch of books about love. But it didn't help."
    me "I don't even know how to court you."
    show un smile pioneer with dspr
    un "Try asking a girl out for a dance."
    "She whispered."
    un "For a walk - somewhere."
    un "Tell her about yourself, ask about her."
    me "Almost all of that seems to be ready."
    me "The only thing left is the dance."
    me "Do you want to dance tonight?"
    if alt_day2_bf == 'sl':
        "True, I promised one dance to Slavya, I'll definitely go with her on the second one."
    "She shook her head."
    un "I don't want to."
    me "H-how? But why?"
    me "You said it yourself..."
    show un grin pioneer with dspr
    un "I want now."
    me "Y-Are you serious?"
    "Thought that the two of us will now be dancing together in the backyard of some warehouse in the very center of nothing, for some reason was both amused and seemed utterly romantic."
    stop music fadeout 3
    me "Give me a sec then."
    "I pulled out a bar of «walkman» and clicked rewind in search of the scorpions that hadn't finish yesterday."
    me "Here…"
    "I gave her an earpiece."
    me "Here's what you need to stick in your ear."
    un "Really?"
    "She resignedly took the earpiece and reproduced the sequence of my actions, trying to put the earpiece tighter."
    play music "<from 115.69 to 204.63>" + music_7dl["scorpions"] fadein 3
    "This song was the same age with me. I took my first breath when Klaus Meine rocked the world with guitar picking on this particular piece."
    show un shy pioneer with dspr
    "She shuddered when the first chords hit her eardrum, but in a few seconds she got used to the sound and quietly crept in my hands, listening to the sounds of the masterpiece."
    scene cg d3_un_dance_7dl with dissolve
    "One hand on her waist, the other holding her hand. Skin to skin, breath to breath."
    "We're dancing in an overgrown laundry warehouse yard. Two freaks. Two puppets with immortal souls."
    "Not moving but feeling - how is it there, on the other side of someone else's chest?"
    "Does anything beats back?"
    "And smile at what beats."
    "Little by little we begin to sway, getting used to each other, moving our feet in a whirl of a slow dance that has not undergone major changes in fifty years."
    "Unless in the nineties, the second hand stopped looking for the partner's hand and confidently took a place either on the back, or... hmm..."
    un "You have so much beautiful music."
    "She whispered."
    un "You must live in a very beautiful world."
    un "A place that can produce such beauty cannot be ugly."
    "It can, it definitely can."
    "The whole history of the world tells us that it is only through pain that the most beautiful pictures, the most touching songs and the most fascinating stories are born."
    "From Petrarch with his Laura."
    "To Maine."
    "And that's why I'll never tell her about it."
    me "So your world is even better than mine."
    "I whisper back, chalking out the words with one breath."
    me "Since it was able to create you."

    pause(10)
    stop music fadeout 3
    scene bg ext_warehouse_day_7dl
    show un smile pioneer
    with dissolve

    cs "Here you are."
    "There was a familiar voice from behind."
    show cs normal at right with dissolve
    "Lena reluctantly pulled away and looked in the direction of Viola who had disturbed us."
    me "Yes, Viola, were you looking for us?"
    cs "Something like that."
    cs "I was looking for the camp's two most reclusive kids."
    cs "No wonder I found them {w}- one in the arms of the other."
    "I wanted to reply that it was none of her business."
    "But she said with a seriousness that surprised me - even without her usual ambiguities:"
    cs "I would like to ask you for help."
    cs "Both."
    me "Yeah, what is it?"
    cs "Medicines will be brought in by the evening, and they should be scattered on the shelves and accounted for."
    cs "Also in the top left drawer of the desk, you'll find something that will ease headaches for both of you."
    me "Analgin?"
    show cs smile close at right with dissolve
    "She laughed."
    cs "Oh yes. Something like that."
    "She looked at us again."
    cs "So... pioneers?"
    cs "Would you help me?"
    menu:
        "Help":
            $ karma += 25
            "I looked at Lena and, waiting for a barely perceptible nod in return, nodded myself."
            me "Yes, we will help."
            show cs normal close at right with dissolve
            cs "I knew you would agree."
            "For some reason, she winked at Lena and said something incomprehensible:"
            cs "Great job, girl. You learn instantly."
            show un shy pioneer with dissolve
            "Lena blushed hotly, but didn't answer. Didn't even explain."
            "It's her business."
            $ alt_day3_un_med_help = 1
            $ counter_un_7dl = 6
            "I looked at the clock - it was time for dinner."
        "Do not help":
            me "Sorry, Viola, we can't today."
            show un normal pioneer with dissolve
            "I mumbled something indistinct about the fact that Olga Dmitrievna asked for help and all that."
            "Viola stood and with an all-understanding look shone through me."
            cs "Well, a pity."
            "She said, referring to Lena for some reason."
            cs "Bad luck."
            "She also just shrugged her shoulders. She looked upset for some reason."
            "On the clock, the time is close to dinner."
            $ alt_day3_un_med_help = 2
    return

label alt_day3_eventAf_estrade1:
    scene bg ext_stage_big_day_7dl with fade
    play ambience ambience_camp_center_day fadein 1
    if alt_day3_dv_guitar >= 1:
        "The stage is definitely popular these days."
        "Alisa has been playing music here since morning."
    elif alt_day3_dj in ('dv', 'mi'):
        "I've been here quite often."
        return
    else:
        "Even from a distance, I could make out several figures standing next to the covered stage."
    show sl normal pioneer at right with dissolve
    show un normal pioneer at left with dissolve
    "Lena. Slavya."
    "According to logic, only Ulyanka and our two cybenematics are missing here."
    "Slavya was uttering something to Lena, apparently instructing, as she stood half-turned and nodded, looking somewhere down."
    "Finally, Slavya finished, asked something - apparently, if she understood everything - received an affirmative nod and released the victim."
    hide un with dissolve
    "Lena walked past me, as usual, looking directly at her feet, and I finally got to the hero of the occasion:"
    if alt_day3_sl_invite:
        scene bg ext_stage_big_day_7dl
        show sl normal pioneer
        with dissolve
        me "You called and I came."
        me "What can I do for you?"
        show sl smile pioneer with dspr
        "Slavya smiled."
        "An amazing girl - how natural it seems for her to help someone, hence she is so pleasantly surprised by the help of someone else."
        "I know this type of people - they usually grow up in very large families."
        sl "You could... What are you thinking about?"
        "It seems that my lost appearance knocked her off."
        me "I just thought that you must have a huge number of brothers and sisters. It would be great to see them."
        show sl shy pioneer with dspr
        "She was embarrassed, as if I had climbed into someone else's territory, and hurried to return the conversation to a more familiar course."
        sl "So you want to help with dancing?"
        "I nodded."
        $ lp_sl += 1
    show sl normal pioneer at center with dissolve
    me "Let the dance begin!"
    show sl laugh pioneer with dspr
    "Looks like I had the most zealous appearance, as the girl laughed."
    if alt_day2_bf == 'sl':
        sl "Let's assume that you won't run from dancing anyway. You promised."
    sl "It remains only to make sure that the dances themselves will take place."
    show sl normal pioneer with dspr
    sl "We'll need equipment, records, and get Miku to work as a disc jockey today instead of dancing."
    if counter_mi_7dl == 1:
        "The last part of the task was my favorite."
        me "Is it that «help with setting up dance floor»?"
        "Slavya smiled back."
    else:
        show sl smile pioneer with dspr
        "It seemed to me somewhat dishonest, but Slavya probably knew better."
    me "Are you sure Miku will agree? She's a girl, she'll probably want to dance too."
    sl "Miku? No!"
    show sl laugh pioneer with dissolve
    sl "She tried dancing to our music once."
    sl "Got all whined up. She said that in her homeland such music is played in restaurants in order to drown out conversations at other people's tables."
    show sl normal pioneer with dspr
    "Slavya hid her smile - it seems, despite the comic content, the topic did not amuse her very much."
    sl "If Miku suddenly wants to dance, we'll look for another host."
    sl "As a last resort, I'll stand behind the turntables myself."
    dreamgirl "Oh-la-la, Slavyana-deejay blows up the dance floors."
    me "Maybe it's better to ask someone who definitely won't dance?"
    if counter_dv_7dl >= 3:
        sl "Do you have a candidate?"
        me "Not really. But I heard that Alisa Dvachevskaya hates dancing. Maybe if you put her in the lead..."
        sl "How do you know everything?!"
        sl "But you're right! So at least she'll be with the squad it will be better than if she runs away to swim again or locks in the cabin with a guitar."
    else:
        sl "Alisa for example?"
        me "What about Alisa?"
        show sl laugh pioneer with dspr
        sl "She doesn't like dancing! She thinks they're just antics."
        "In some ways, Dvachevskaya is even right."
        "In some, but not in every."
        show sl smile pioneer with dspr
        sl "A good candidate to be a camp DJ, right?"
        if dr:
            "I nodded."
            me "Maybe you're right."
        else:
            me "Not necessarily."
            me "Maybe Dvachevskaya won't like the local music."
            sl "You're right about that."
            "Slavya agreed."
    sl "In general, I leave everything on your conscience - either persuade Dvachevskaya to lead our dances, or negotiate with Miku."
    sl "Can you do it?"
    "I shrugged."
    me "Probably no more difficult than collecting signatures with a slider."
    show sl laugh pioneer with dissolve
    sl "You're right. Okay, I'll wait for you with the results of the negotiations."
    menu:
        "Miku":
            $ lp_mi += 1
            call alt_day3_day_mi_dj
        "Alisa":
            $ lp_dv += 1
            call alt_day3_day_dv_dj
    if alt_day3_mi_dj_fale:
        call alt_day3_day_dv_dj
    if alt_day3_dj == 'mi':
        return
    if alt_day3_dj != 'dv':
        scene bg ext_stage_big_day_7dl with fade
        play ambience ambience_camp_center_day fadein 1
        me "The negotiations were short lived."
        if alt_day3_dv_dj_fale:
            me "Simply put, Alisa refused. What do we do?"
        else:
            me "Simply put, I did not find Alisa."
        show sl sad pioneer with dissolve
        "Slavya, who was standing on the stage with a bunch of wires, frowned."
        sl "Not good…"
        sl "Have you tried talking to Miku?"
        if not alt_day3_mi_dj_fale:
            "I shook my head."
            show sl angry pioneer with dissolve
            sl "Then ask her, please! We have no other options at all!"
            th "Like there's more to it..."
            hide sl with dissolve
            "Deeply sighing, I mentally set myself up for the next persuasion."
            $ alt_day3_dv_dj_fale = True
            call alt_day3_day_mi_dj
        else:
            me "I tried. Not an option either."
            "Slavya sighed."
            show sl upset pioneer with dissolve
            sl "Nobody wants to lead a disco, really?"
            "I just shrugged - as they say, I did everything that was in my power."
            sl "Okay. Thanks for at least trying."
            hide sl with dissolve
            "She left the stage and retired towards the square. And all I had to do was shamefully return to the cabin in order to get some sleep."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_day_mi_dj:
    scene bg ext_musclub_day with fade
    play ambience ambience_camp_center_day fadein 3
    "Whatever one may say, but Miku scared me much less than the red-haired wretch Dvachevskaya."
    "That's why I decided to take the path of least resistance."
    if counter_mi_7dl == 1:
        "Especially since this is another reason to see a beloved Japanese girl."
        "Because I know those annoying, gloomy, with dumbosis - they draw things in the morning, and in the evening, they read out loud about Miku's persistent visitor."
    else:
        "Moreover, Lena should be there - some kind of moral help at least."
    stop ambience fadeout 2
    play sound sfx_open_door_2
    pause(1)
    scene bg int_musclub_day with dissolve
    play ambience ambience_music_club_day fadein 3
    show mi smile pioneer at right with dissolve
    show un normal pioneer at left with dissolve
    "Lena already was here."
    if counter_mi_7dl == 1:
        mi "Halo again!"
        "Miku was delighted as if Madonna visited her club on tour."
        mi "Have you finished helping out yet? Come to learn how to dance?"
        mi "Now, I'm almost free. I need records here."
        mi "Or..."
        "She threw a thoughtful look, first at me, then at Lena."
        mi "Maybe put you in a pair? Both will learn?"
        show un shy pioneer at left with dissolve
        "No!"
        "Almost simultaneously, Lena and I answered."
        me "I'm here for another reason actually!"
        "I hurried to put in my two cents before something else was decided for me."
    me "Slavya said that you take the local dances rather coolly."
    me "So, would you like to lead?"
    show mi normal pioneer at right with dissolve
    show un normal pioneer at left with dissolve
    mi "The DJ doesn't dance. Why should I go to the dance if I won't dance?"
    if (alt_day2_mi_date != 2) or alt_day3_dv_dj_fale:
        menu:
            "You will dance. I'll personally invite you":
                "I promised easily."
                "Miku smiled, clearly intrigued."
                me "Just watch the rotation, and I'll provide you with company and dancing, I promise. {w}Plus a new experience as a DJ..."
                me "You have a chance to try."
                show mi normal pioneer at right with dissolve
                mi "Well, I don't even know. Somehow unusual."
                me "Come on, Miku!"
                "I insisted."
                me "It's just another way to express yourself. You've never tried it, how can you know if you like it or not if you've never tried it?"
                "She hesitated."
                me "No one bothers you to go and dance yourself while the song is playing!"
                show mi shy pioneer at right with dissolve
                mi "Okay! I'll try!"
                me "Should I convey your consent to Slavya?"
                mi "N-no... Yes! Pass it on."
                $ lp_mi += 1
                $ alt_day3_dj = 'mi'
                $ alt_day3_dv_guitar = 0
                pause(1)
                scene bg int_musclub_day with fade
                "And she returned to the conversation with Lena, from which I distracted both."
                show mi normal pioneer at right
                show un normal pioneer at left
                with dissolve
                mi "Which specific records are you interested in?"
                mi "I have a lot and don't even ask, I'll not give you everything."
                show mi smile pioneer at right with dissolve
                "She smiled and held out three."
                mi "Here's your starter."
                stop music fadeout 2
                "It would be better, of course, something modern..."
                "But Toto Cutugno or some other Celentano will work too at last."
                me "Start your songTs."
                "I made a go-ahead, getting ready to sing «Suzanne»."
                call alt_day3_dj_music
                stop music fadeout 3
                stop ambience fadeout 6
                with fade
                return
            "Maybe you're right" if not alt_day3_dv_dj_fale:
                pass
    else:
        me "Actually, you might be right."
    me "You're a creative person, you probably need to dance."
    me "I'll try to persuade Dvachevskaya."
    un "I don't think she'll agree..."
    show un shy pioneer at left with dissolve
    "Lena whispered, immediately embarrassed:"
    un "Oh. I said it out loud."
    show mi smile pioneer at right with dissolve
    mi "About Alisa, you have a good point! She is probably in her cabin right now, playing the guitar."
    mi "There is a certain craving for the public in her, which she diligently strangles in herself."
    "I haven't finished."
    me "And with you..."
    "I pointed my finger at Miku."
    me "Dance with you!"
    show mi grin pioneer at right with dissolve
    "She broke into a smile."
    mi "Oh, what a brave boy."
    mi "Have you heard, Lena? Syomochka himself invited me!"
    "I gritted my teeth, but said nothing."
    "Looks like she was proud of that fact even more than me!"
    me "Okay, if that's the case, I'll go and persuade another candidate."
    "Politely bowing to the girls, I left the room."
    $ alt_day3_mi_dj_fale = True
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_dj_music:
    scene bg int_musclub_day
    show un normal pioneer at left
    show mi smile pioneer at right
    with dspr
    menu:
        "Listen to «Lightness»":
            play music music_list["lightness"]
            "Not a fountain, of course, but it seems that this kind of music is in fashion now."
            "We stood with Lena and listened to music, Miku looked at us and smiled."
            jump alt_day3_dj_music
        "Listen to «Raindrops»":
            play music music_list["raindrops"]
            show mi happy pioneer at right with dissolve
            mi "A very good stuff!"
            mi "Really, I don't know how to dance to it. But the guys on the dance floor did it!"
            "We stood with Lena and listened to music, Miku looked at us and smiled."
            jump alt_day3_dj_music
        "Listen to «Silhouette in sunset»":
            play music music_list["silhouette_in_sunset"]
            show un smile pioneer at left with dissolve
            "Hearing the first notes, Lena began to smile."
            un "What a good song..."
            show un surprise pioneer at left with dspr
            un "Oh."
            "She pressed her hands to her mouth, deciding this time to remain silent until victorious."
            "We stood with Lena and listened to music, Miku looked at us and smiled."
            show un normal pioneer at left with dspr
            jump alt_day3_dj_music
        "Choose music!":
            mi "What music do you want?"
            menu:
                "Choose «Lightness»":
                    $ lp_sl += 1
                "Choose «Raindrops»":
                    $ lp_mi += 1
                "Choose «Silhouette in sunset»":
                    $ lp_un += 1
            mi "Great taste!"
            mi "Do not forget, Semyon, you invited me!"
            mi "Oh, how exciting!"
            "She pushed us out of the club."
            mi "Come again."
            "Lena and I went back to the stage."
            stop ambience fadeout 1
            scene bg ext_stage_big_day_7dl with fade
            play ambience ambience_camp_center_day fadein 2
            play music music_list["i_want_to_play"] fadein 2
            me "This is…"
            me "Yes."
            "Lena and I arrived early enough, and I managed to catch the final act of the performance called «fragile Slavya and her carrying capacity»."
            th "May I live like this!"
            "Together with Ulyanka, they tilted the heavy «LOMO» to the edge of the stage, where they left it hanging over the edge a little."
            "Then Slavya ran down, and Ulyana pushed from above - right into the substituted hands."
            "I already wanted to rush to help out when a huge black box hung over a short girl, threatening to drive her into the dust up to her ears."
            "Late!"
            "Slightly staggering from the weight, she took the speaker in her arms and smoothly lowered it to the ground."
            show us normal pioneer at left
            show sl normal pioneer at right
            with dissolve
            me "Slavya, you're just a bodybuilder!"
            me "The biceps are probably stronger than our Gym teacher has!"
            "She tried to hide her embarrassment under laughter."
            show sl smile pioneer with dspr
            "It won't work. If you are Schwarzenegger, then you are Schwarzenegger forever."
            show sl normal pioneer with dspr
            "And does she - like that! - even needs help?"
            "Yes, she is able to sack everything herself, even if we also sit on top!"
            "Though she didn't seem to think so."
            sl "Can you help? We need to drag them to the square."
            if loki:
                if (alt_day2_date == 'sl'):
                    me "You do know that I'm doing this under duress, don't you?"
                    dreamgirl "She was a very bad girl... She did everything under duress: durex for dad, durex for mom..."
                    "I winced."
                    th "That's it, good humor is over, vulgarity and consumer goods have begun?"
                    dreamgirl "Can't even say a word now! Carry the loudspeakers... march!"
                else:
                    me "Yea, right. Now I have to carry speakers for her."
                    me "What if war suddenly starts, and I'm tired."
                    "I shook my head."
                    me "Let Schwarzenegger carry it around. I've got a lot to do already."
                    "For some reason, Slavya didn't look surprised. {w}I don't even know why."
            else:
                "I lifted my slack jaw, then allowed myself to nod."
                "And we dragged these heavy speakers until our faces went blue, to hell with them!"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_day_dv_dj:
    scene bg ext_house_of_dv_day with dissolve
    play ambience ambience_camp_center_day fadein 1
    $ alt_day2_dv_us_house_visited = True
    "Finding Alisa wasn't that easy."
    if counter_dv_7dl >= 2:
        "First of all, I looked into the music club, but found only Miku there. She didn’t know where Alisa had gone - as they say, she was but swam away."
        th "She didn't had enough patience to wait for me!"
    else:
        "I looked into this cabin first of all, but it was locked, the windows were dark, and not a sound came from inside."
    "I had to run around the entire camp - from the canteen to the gate."
    "And it is quite expected that either no one saw her, or they did, but - «she left literally five minutes before you»."
    "I, already desperate and not hoping for anything, sat down on her porch and thought."
    stop music fadeout 2
    th "Where could she go? The guys said something about the old camp, did she really..."
    if alt_day3_technoquest1 >= 1:
        "No, I will search for her outside the territory until evening!"
        "So there was nothing left but to go to Slavya and shamefully admit defeat."
        return
    play music music_7dl["dv_guitar"] fadein 7
    "My attention was attracted by the barely audible guitar picks coming from the other side of the cabin."
    $ renpy.show("bg ext_dv_hideout_day_7dl", what = Noon("bg ext_dv_hideout_day_7dl"))
    with dissolve
    "Looking around to see if anyone was watching, I went around the cabin and, focusing on the sound, moved along a barely noticeable passage in dense bushes."
    "Alisa sat with her back to me and melancholy plucked the strings, holding her head suspiciously familiar!"
    "Usually I hold my head like this when the smoke eats my right eye."
    "Nearby lay a pack of «Magna», pressed to the ground with a steel «Zippo» square."
    "She smokes?!"
    me "Locomotiving, Dvachevskaya."
    "I concluded."
    show dv sad pioneer2 at right with dissolve
    "For some reason, she didn't look scared or angry - and in fact, even in my time, the kids were very afraid of getting caught with a cigarette!"
    "More like annoyed, like a person who has been distracted from an unnecessary task, which, nevertheless, must be completed."
    me "Ay-ya-yay, how unpleasant. Such a smart, beautiful girl - and she smokes! What will the squad leader say?"
    dv "Will send you to Brazil."
    "Without stopping the party, Alisa retorted."

    if alt_day3_dv_guitar == 2:
        dv "Almost finished the song. If you don't change your mind..."
    if counter_dv_7dl >= 2:
        show dv smile pioneer2 at right with dissolve
        "She gave me an expressive look."
        dv "I don't like being kept waiting."
        th "Really, it didn't come out very well. I kind of promised her, but I..."
        me "Sorry. There were just some unforeseen circumstances."
        show dv sad pioneer2 at right with dissolve
        if loki:
            $ lp_dv -= 3
        elif herc:
            $ lp_dv -= 2
        else:
            $ lp_dv -= 1
    "She looked at me doubtfully, as if she didn't know if I could be trusted."
    "And I, without further ado, picked up a pack from the ground, took out a cigarette with my lips and, rolling the wheel against my palm, lit it, stretched it out, puffed on it..."
    "Oh, strong, damn it!"
    show dv shocked pioneer2 at center with dspr
    "I blinked away unbidden tears and only then did I see Dvachevskaya's square eyes."
    dv "Do you smoke?!"
    me "Wanted to ask you the same question."
    "Clearing my throat, I said."
    show dv normal pioneer2 with dissolve
    dv "Well, its pretty clear about me, an unstable element, all that."
    me "And I... I smoked in a past life. Where I come from."
    dv "And how long you..."
    stop music fadeout 5
    me "Since I was fourteen, I think."
    "I finally reconciled the mucous membranes with the throatwretcher and, trying to take shallow puffs, sent the perfect ring flying, and another one through it."
    "She thoughtfully watched me, and there was something in her eyes... Such..."
    dv "You showed up at a very strange time."
    "She said thoughtfully."
    dv "I know everyone here, and I can make judgments about everyone. But not about you. You're a dark horse."
    me "More like alien among my own kind. I came here to ask you to take part in the life of the squad."
    show dv grin pioneer2 with dissolve
    dv "Dancing? No. I already said I'm not going to go waving my arms like an idiot."
    me "Not exactly dancing. I want to invite you to host the dance."
    show dv surprise pioneer2 with dissolve
    "I think I managed to surprise her."
    dv "Host? Rearrange records?"
    me "Actually, run the whole disco - put on records, watch the rotation, announce the white dance, and so on."
    show dv normal pioneer2 with dissolve
    dv "I don't like this idea very much honestly."
    me "Relax. It's like playing, performing on stage, only the instruments are pre-recorded songs. The quality depends not only on them, but also on your stage skills."
    if (lp_dv >= 9):
        show dv smile pioneer2 with dissolve
        "I don't know if I convinced her or not, but she put out her cigarette and got up."
        dv "Okay! I'll go. But if something goes wrong..."
        "I even became interested."
        me "What could be «wrong»?"
        dv "I don't know! You manage to cause trouble just by being here."
        dv "I'm surprised that the squad leader hasn't caught us here yet - she'll think up something for herself, I guarantee."
        "For a second, it seemed to me that by «something» Dvachevskaya means an invitation to dance from certain boy."
        "What a shame it would be if a boy invited her, but she couldn't dance!"
        th "Now that this topic has come up, I suddenly really want to ask this particular girl to dance."
        "It seems that she is all as harsh as Chapai."
        me "So, I convey your consent to Slavya?"
        show dv angry pioneer2 with dissolve
        dv "So you're from that prick..."
        "Perceptibly seething, she hissed."
        "And I sighed."
        if alt_day3_dv_guitar == 2:
            me "No, I'm on my own."
            show dv normal pioneer2 with dissolve
            me "Of course I wish to hear the finished version of that song."
            me "But I also wish you weren't alone."
            me "And it makes me extremely sad to know that you're sitting here alone and tearing those innocent strings."
            dv "Why do you even bother."
            "It doesn't seem like she's going to let a person get any closer than a certain distance."
            me "I won't tell you. It's as secret as this pack. Put it away, by the way."
        else:
            me "Alisa, why are you angry, huh?"
            "I asked plaintively."
            me "Actually, I was the one who suggested you as host."
            show dv surprise pioneer2 with dissolve
            dv "You?"
            me "You can do it, I believe in you."
            "I think I managed to shock her because she just waved her hand."
        show dv normal pioneer2 with dissolve
        dv "Go already... mass-entertainer."
        hide dv with dissolve
        "She disappeared in the cabin."
        "I smiled and ran on about my tasks. And there were a lot of them!"
        $ alt_day3_dj = 'dv'
        $ alt_day3_dv_guitar = 0
        "..."
        stop music fadeout 3
        scene bg ext_stage_big_day_7dl with fade
        play ambience ambience_camp_center_day fadein 1
        show sl normal pioneer with dissolve
        sl "She agreed? That's great!"
        "Slavya was just finishing winding up some thick wires."
        sl "Thank you very much!"
        me "Do you need any more help?"
        show sl laugh pioneer with dissolve
        "I asked with a hope, poorly concealed in my voice, that she didn't need it. Slavya smiled."
        sl "No, not yet. You can rest!"
        hide sl with dissolve
        "I was not slow to take advantage of this permission, heading towards my haven - to sleep."
    else:
        show dv tired pioneer2 with dissolve
        $ alt_day3_dv_dj_fale = True
        dv "Think I'll pass."
        th "What?!" with Shake((0, 0, 0, 0), 0.3, dist=50)
        dv "It's all long, boring... And anyway, I have my own things to do!"
        me "But..."
        "I didn't have enough air in my lungs to fully express my indignation."
        th "It turns out that I was crawling on my belly in front of her and humiliated myself so that she just took it and refused?"
        dreamgirl "Dude, you just asked her, she just refused - what is the reason for your indignation?"
        th "That's right, that «just asked» in the case of Dvachevskaya is already full humiliatio!"
        me "Why don't you just want to try?"
        "I did not lag behind the girl. She had already removed the guitar in a case and threw it behind her back."
        show dv normal pioneer2 with dissolve
        dv "Because I'm not the least bit flattered by the idea of ​​entertaining these suckers all night!"
        hide dv with dissolve
        "And, with all her appearance showing that the conversation was over, Alisa went around the cabin and hurried somewhere along the path."
        th "Quest failed."
        th "With this character's refusal, the thread of prophecy is severed. Restore a saved game to restore the weave of fate, or persist in the doomed world you have created"
        "So I slurped my way back to the stage."
        "..."
    return

label alt_day3_supper:
    scene bg int_dining_hall_people_day with fade2
    play ambience ambience_dining_hall_full fadein 2
    play music music_list["smooth_machine"] fadein 3
    "Canteen was pack jammed."
    if (counter_mi_7dl == 2):
        "A buzzkill instantly sat next to Miku, and began to reprimand something to her."
        "It seemed indecent to me to drive her out of the place by force, especially since I managed to just notice a convenient place in the corner - the cyberneticists had just taken off from there, freeing the whole table for my sole use."
        "I sat down and, looking at Miku, began to eat dinner."
        "The anticipation of something grandiose was seething around."
        "Not otherwise, a joint concert of U2 and Eric Clapton."
        "Although, in fact, a rural ball under the Christmas tree garlands hung on the trees."
        "I doubt they even have a strobe."
        "Anyway, with my optimistic thoughts, I completely ruined my appetite and left the canteen one of the first."
        return
    show dv normal pioneer with dissolve
    "Alisa,"
    hide dv with dissolve
    show sl normal pioneer with dissolve
    extend " Slavya…"
    hide sl with dissolve
    if (counter_un_7dl < 5):
        show un normal pioneer with dissolve
        extend " Lena…"
        hide un with dissolve
    extend " And everyone else were here already."
    "Except for Olga Dmitrievna. She, along with other squad leaders, was on the square, doing an extremely useful thing - hanging garlands."
    "Thank god that she is not involved in the dance program or any other organizational issues."
    "I looked around the canteen again."
    "Probably the only time everyone got together on time."
    if (counter_un_7dl >= 5):
        "Except me and Lena."
    else:
        "Except me."
    if (counter_sl_cl >= 5):
        "I was hoping to sit down with Slavya, but she was dragged away by some friends from other squads."
        "Sighing, I took a free table for four people - the cybernetics had just risen from there - and got to dinner."
    elif (counter_mi_7dl >= 2):
        "I wanted to sit with my Japanese girl, but a buzzkill caught her by the hand and seated her at the table, in the only free seat."
        th "Damn insect! Killed half the pleasure of dinner!"
    elif (counter_un_7dl >= 5):
        "Having exchanged a wink with Lena, we sat down at a free table, and, without saying a word, pushed the free chairs deeper under the table."
        me "You know... You're fine!"
        "I laughed."
        me "If you already understand me almost with half a word..."
        show un smile pioneer at center
        un "Unfortunately, not with half a glance..."
        un "Then I would have come up on the first evening..."
        me "May I ask what number I have on your score book?"
        show un smile3 pioneer at center with dspr
        un "First... And the only one. I won't dance with anyone else."
        me "Got your word for it."
        show un smile pioneer with dspr
        "Lena smiled and winked at me."
        th "Hourglass man. She's been shy and afraid of me since morning."
        th "In the afternoon, she takes me to the end."
        th "In the evening, her embarrassment disappears."
        "I could not admit to myself, but for some reason I was wildly excited and turned on by such a cocktail!"
        "Finished, I got up and nodded goodbye."
        me "Well, See you at the dance?"
        un "Bye..."
        hide un with dissolve
    else:
        "I sat down at a free table. But no one even paid attention to me."
    "Virtually no one spoke. There was an almost palpable atmosphere of excitement."
    "Everyone was in anticipation of dancing."
    stop ambience fadeout 6
    with fade
    return

label alt_day3_supper2:
    scene bg int_dining_hall_sunset with fade
    show mt normal pioneer with dissolve
    if alt_day3_duty:
        mt "That's it, the last push. {w}Only cleaning left, and you can consider yourself free."
        me "Uh... Okay."
        hide mt with dissolve
        if not (alt_day2_date == 'un_fz'):
            "Using the right of the duty officer, I climbed into the bins of the Motherland and filled my pockets with food at their expense."
            "I don't know what I was guided by, but I decided to listen to the voice of intuition."
        show us normal sport at center
        us "You'll mop the floor yourself.{w=0.4} I can't lift that bucket."
        "She kicked a small pail of suds."
        me "As you say. Then the tables are yours."
        "Already played in tandem, we walked in two lanes: first, she - leveling tables, turning chairs and pushing benches, then I - wiping the floor with a damp cloth and setting the furniture in place."
        sl "You're doing great!"
        "Delighted the voice from the door."
        "I turned around."
    else:
        mt "Now you have half an hour of free time. If you have any urgent business, do it. I'm waiting for everyone at the square."
        "I nodded."
        if counter_dv_7dl == 3:
            "Olga seems to know something, but she is in no hurry to speak."
            "She didn't respond to my questioning look."
            "But I managed to stock up on food a little - intuition told me that it would not be superfluous."
        hide mt with dissolve
        show us smile pioneer with dspr
        us "Let's go!"
        "Despite the fact that the day turned out to be eventful, as well as the promises of a wonderful evening, I was suddenly attacked by an incomprehensible tetanus."
        "With my luck, I'll get into tricky situations even in something as innocent as dancing."
        dreamgirl "Negative thinking? Come on-come on, bring troubles."
        th "A lot of help from you..."
        "Sighing, I forced myself to rise."
        "Anyway, you won't be able to sit in the canteen until the end of your days."
        sl "Good evening!"
    show sl normal pioneer at left with dissolve
    "Slavya."
    "She does not smile, which is rather unusual, but looks friendly and even with some challenge."
    if (counter_sl_cl >= 5):
        sl "Semyon, should I wait for you, or are you really not going to run away?"
        "No, right now, for sure - this was a joke! The red light came on!"
        me "I promised."
        "I grumbled."
        me "And I know the value of my word."
        show sl smile2 pioneer with dspr
        sl "I'll still check it out!"
        "She nodded to Ulyana and went outside."
        "As I understand it - to wait me on the porch."
        hide sl with dissolve
    else:
        sl "Do you remember about dances?"
        "She started."
        if alt_day3_dj == 'dv':
            me "Of course I am. I even found a DJ for this dances as you told me."
        elif alt_day3_dj == 'mi':
            me "Slavya, I haven't forgotten about it for a second since lunch. Do you remember who recruited DJ?"
        else:
            me "Remember, this isn't the first time someone asked."
            "I grumbled."
        sl "Are you coming?"
        us "Of course I will! {w=.4}And as for my slow friend... that's complicated."
        if alt_day3_dj == 'mi':
            "I shrugged my shoulders - after Miku's offer to study in trio..."
        elif counter_mi_7dl == 2:
            th "Yeah, and that's why I made arrangements with Miku today for a costume and a couple of dance lessons."
        sl "Complicated?"
        us "It looks like he either doesn't want to or doesn't know how to dance."
        show sl serious pioneer at left with dissolve
        sl "It doesn't matter."
        sl "Dancing is a collective event. The whole squad must be present, no exceptions."
        "She paused and suddenly asked:"
        if counter_dv_7dl == 3:
            sl "Is it true that you and Dvachevskaya almost got into a fight? Miku told me, she heard your argument..."
            me "This is our own business."
            "I cut it."
            sl "Perhaps. But you should be at the dance."
            "Slavya answered me in tone."
            sl "I don't know about Alisa, she always ignored such things..."
            th "So the law is not applied to  Alisa, but with me, everything is not lost yet, right?"
        else:
            sl "You don't want to go?"
            if (counter_un_7dl >= 5):
                me "Are you kidding? Of course I want to!"
                th "I'm about to dance with the most beautiful girl in the camp."
                dreamgirl "Yeah. And she just can’t wait for you to hug her with dirty hands, snuggle her up with that unwashed for three days, smelly body..."
                th "Or I won't come..."
            elif alt_day3_dj in ('dv', 'mi'):
                me "Are you kidding? {w}I'll come at least for the sake of making sure that my labors are not in vain!"
                th "Not to mention my intention on inviting one extremely pretty girl to dance."
                dreamgirl "Yeah. And she just can’t wait for you to hug her with dirty hands, snuggle her up with that unwashed for three days, smelly body..."
                th "Or I won't come..."
            else:
                me "I... What if I don't come?"
                sl "A reprimand for ignoring the will of the majority, I think."
                "Yea, with checkmark in the thorax."
                "She stuttered."
                sl "Don't you want to dance yourself?"
            if alt_day3_duty:
                show us dontlike sport at center with dspr
            else:
                show us dontlike pioneer at center with dspr
            "Ulyanka snorted nearby - it seems that the same thing came to her, albeit belatedly, as to me."
            me "I'll think about it."
            if alt_day3_duty:
                "I answered evasively and, grunting, picked up the pail."
                show us normal sport at center with dissolve
            else:
                "I answered evasively."
                "At the end, it's none of her business whether I'm at the dance or somewhere else."
            show sl normal pioneer at left with dissolve
    if alt_day3_duty:
        us "Good job."
        "Ulyana summed up indifferently, throwing her robe on a hanger standing at the door."
        me "The best."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_dance_dance:
    scene anim_square_preparty with dissolve
    play ambience ambience_camp_center_evening fadein 2
    play music music_7dl["lonesome_shepherd"] fadein 7
    if (counter_un_fz == 2):
        show el normal pioneer far at cleft
        show sh normal pioneer far at cright
        with dissolve
        "On the square, I saw cybernetics, arguing about something animatedly."
        show el smile pioneer far with dspr
        "Noticing me, the Electronics enthusiastically waved his hand at me, hoping to attract attention."
        hide el
        hide sh
        with dissolve
        "I turned away, pretending not to notice the gesture."
        th "I've had enough of work today, let me be free at last..."
        "Don't expect anything else from them - they'll plow you even worse than Olga."
        "And I, turning from the square onto the path leading to the cabins, hastened to get out."
        stop music fadeout 2
        stop ambience fadeout 2
        return
    "During the time we filled our stomachs, the squad leader did a very good job!"
    "I wouldn't say that the square was unrecognisable, but in general it all looked much more decent than I feared."
    "Although I was skeptical about the idea of ​​outdoor dancing."
    "I sat on a bench not far from the black «LOMO» cubes purring «Shepherd» and whistled a tune when two cybenematical blockheads approached me."
    show el normal pioneer at cleft
    show sh normal pioneer at cright
    with dissolve
    me "Hello."
    "I shook hands with both theorists and stared at them questioningly."
    if alt_day3_technoquest1 >= 1:
        "After all the good I've done for them, it's reasonable to expect them to come to me now in case of any inconveniences."
        th "Well, well! I seem to be considered the second Slavya! Or the second Slavya?"
    me "What can I do?"
    el "We're not sure yet."
    me "So?"
    sh "Well, there is one problem."
    me "And?"
    el "We're not sure if we can solve it, or if we need your help."
    me "And you want to enlist it in advance?"
    th "Amazing."
    sh "Kinda."
    "Shurik nodded."
    show sh smile pioneer at cright with dspr
    me "Maybe you could at least bring me up to date?"
    "They both giggled in embarrassment."
    if alt_day3_technoquest0:
        el "You already know. About antenna."
        show el normal pioneer at cleft with dspr
    else:
        sh "Yes, we want to set up a radio in the camp. It broke shortly before your arrival."
        show sh normal pioneer at cright with dissolve
    "Their embarrassment looked clearly unhealthy. It seems that they are either both afraid of heights - and work at the top is inevitable, if we are talking about radio."
    "Or..."
    me "What's the catch?"
    show el upset pioneer at cleft with dspr
    show sh upset pioneer at cright with dspr
    el "Well, you see..."
    "The freckled cybernetician's eyes darted."
    me "You're afraid of heights."
    "I concluded confidently."
    show el serious pioneer at cleft with dspr
    el "Not that's definitely not the point!"
    if herc and (alt_day3_technoquest1 >= 1):
        me "Then you don't have enough strength to drag any piece of iron upstairs."
    "They shook their heads in unison."
    me "Something else?!"
    "Why am I not surprised..."
    show sh serious pioneer at cright with dspr
    sh "The radio used to play in relay mode."
    sh "And then Olga Dmitrievna told us that since we are responsible for the hardware, we must make announcements, and the horn is on us, and the music program should be new every day."
    if dr:
        dreamgirl "Remind you something, huh?"
        "I thought about it."
        th "Freelance? Or greedy boss?"
        dreamgirl "Last."
        dreamgirl "Don't you remember how they wanted to define you, at your last place, as a designer, system administrator and webmaster at the same time... And that's not counting the main field of activity."
        dreamgirl "A-ha-ha! Here they are, the origins of the eternal Russian bungling of those in power."
    me "You should have refused. Disc jockey is a serious profession that requires full dedication."
    el "Yes! Maybe then you will explain it to her? And we still need to draw a wall newspaper!"
    me "I haven't had to mediate yet. Pieces, guys. Not for any money."
    show sh surprise pioneer with dspr
    sh "How's that even."
    "Shurik looked a little discouraged by my refusal."
    show sh serious pioneer at cright with dspr
    sh "So you won't help us?"
    $ volume(0.8, "music")
    if alt_day3_un_med_help == 1:
        "I remembered that Lena and I actually promised to work at the infirmary."
        me "No, guys. Sorry. Some other time."
        "They hesitated a little more, until it dawned on them that I would not change my decision."
        hide el
        hide sh
        with dissolve
    elif alt_day3_dv_guitar == 2:
        me "No guys, I'm sorry, I have other things to do."
        "If I don't show up for Alisa's mini-concert, she may well be offended."
        "Which I really don't want."
        "They looked at me in bewilderment, but I had already exhausted the limit of explanations and just waited for them to finally leave."
        "Finally it dawned on them that I had said everything, they hesitated and left."
        hide el
        hide sh
        with dissolve
    else:
        me "I didn't say that. But I'm not going to be your lawyer or anything."
        me "I can help you find a radio host or technical stuff."
        me "But just one thing."
        me "Interested?"
        show sh normal pioneer at cright with dissolve
        if alt_day3_dj in ('dv', 'mi'):
            sh "Of course!"
            show el normal pioneer at cleft with dspr
            show sh normal pioneer at cright
            with dissolve
            me "That's agreed. I'll look for a disc jockey for you, while you pick the equipment."
            me "Don't forget to provide a place for a person! They need to work somewhere!"
            if alt_day3_technoquest1 >= 1:
                el "You helped to dismantle the closet today, we will get them there!"
            else:
                el "We seem to have a spare room."
                el "Just need to throw everything out of there."
                "He looked at me."
                el "Can you help with that?"
                "I shrugged."
                me "Now?"
                el "I would like to!"
                me "And we'll dispatch Shurik to go and look for DJ?"
                "I asked with a hint, and I was instantly left behind."
            el "The soundproofing is good there, no one will break through the window."
            "They quickly said goodbye to me and set off on their undoubtedly important cybernetic business."
            hide el
            hide sh
            with dissolve
            "I didn't even ask them if they would go dancing - such odious individuals consider it a crime to waste time hitting boards with their heels."
            "Well, I have a responsible party assignment."
            "Recruitment for the needs of the local broadcast network."
            if alt_day3_dj == 'mi':
                "To be honest, coming up for the second time in a day with the same request was, to put it mildly, not too modest."
                "But since I made a promise..."
                "And I waved to a passing Miku:"
                show mi normal pioneer at center with dissolve
                me "Miku, wait! Miku! We have to talk!"
                "She stopped and looked at me questioningly."
                mi "Yes, Syomochka. It's about the suit?"
                if counter_mi_7dl == 2:
                    me "No, actually I wanted to see you."
                    me "The suit won't run away anywhere, and I have not much time to just look at you."
                    show mi shy pioneer at center with dissolve
                    mi "Well, that's where the unfortunate girl can't resist."
                    me "But it's true!"
                    mi "Okay, tell me what you wanted?"
                    "Until now, I have denied Miku's clairvoyance, so she managed to surprise me."
                    "I diligently typed air into my chest and for ten seconds I tried to formulate a request."
                else:
                    me "A suit? What suit?"
                    show mi laugh pioneer at center with dspr
                    mi "For dancing, of course. You don't want to go in that!"
                    "I looked at myself. I seem to look decent. White top, black bottom. Down to the knee only though, but that's okay."
                    me "No, I'm for another."
                    mi "Maybe we'll try to dress you?"
                    me "You don't have to dress me."
                    "I barely wedged myself into the stream of consciousness."
                me "I wanted to offer you a permanent DJ post."
                mi "Seriously? Oh, how interesting."
                me "As dances go, see if you like all this cuisine, and if you like it, then we will appoint you as a radio host at the local station."
                show mi serious pioneer with dissolve
                mi "What about my club?"
                "I delicately kept silent about the fact that her club hardly has one person, and continued to persuade:"
                me "No one takes it away from you! If you want to play something, the main thing is to turn off the microphone so that unrehearsed things do not get on the transmition. Play as much as you want!"
                mi "Okay! I'll think about it, see how I like it at the dance tonight."
                me "Thank you!"
                "I thanked the girl from the bottom of my heart."
                me "You are amazing!"
                "She smiled at me and ran away. Apparently, on her musical business."
                hide mi with dissolve
                "And with her, I followed up too."
                "I had things to do."
                scene bg ext_washstand2_day with dissolve
                pause(4)
                play sound sfx_open_water_sink
                "Running along the road to the washbins, I hooted for several minutes, exposing my body to ice water, but at the end I stated with satisfaction that now at least I smell decent."
                "There was nothing to wipe off with - I had to use the shirt somewhat for inappropriate purpose."
                play sound sfx_close_water_sink
                "Therefore, the wet fabric gave simply unforgettable sensations, sticking to the body."
                "Forcing to quicken as soon as the legs allowed!"
                scene bg ext_house_of_mt_sunset with dissolve
                play sound sfx_open_dooor_campus_1
                stop music fadeout 2
                stop ambience fadeout 2
                return
            elif alt_day3_dj == 'dv':
                stop music fadeout 3
                scene bg ext_house_of_dv_night
                with dissolve
                "The search for Alisa, I decided to start again with her cabin and did not lose much."
                "This time no one tortured the guitar, making the unfortunate instrument cry."
                "But the light was on in the house, and from there voices were heard in raised tones."
                "I knocked and, after waiting for some unintelligible «boo-boo-boo», opened the door."
                play sound sfx_close_door_campus_1
                scene bg int_house_of_dv_night with dissolve
                play music music_list["so_good_to_be_careless"] fadein 3
                "It's amazing how even a small amount of recognition transforms a person."
                "Where have the sloping shoulders gone, the hunched back, the indifferent acceptance in the eyes mixed with an arrogant squint."
                "None of this happened. Dvachevskaya was actively sitting on the floor, hugging a huge square box with records with her legs - she was preparing a concert program, nothing else."
                "Periodically, she took out one record from the box and, shaking the vinyl out of the paper case, handed it to Ulyana, she then started the turntable."
                "Most of the music collection has already been shelved - judging by the unorganized pile, discarded."
                "On the contrary, the handful of approved music was not so large and, according to the most optimistic estimates, was unable to provide music for the entire event."
                show dv normal pioneer at cleft with dissolve
                show us smile dress at cright with dissolve
                dv "It's you? Come in."
                "She gave me a curt nod and returned to her fascinating occupation."
                us "What did you do to my friend, pest? Now she doesn’t play around, she doesn’t go crazy. Just sits and listens to music."
                if alt_day2_minijack:
                    "She squinted suspiciously."
                    us "You gave her your bandura, didn't you?"
                    show dv laugh pioneer at cleft with dspr
                    me "No way. And she wouldn't listen to that."
                    dv "Well, I would listen to some things. Like how the lamp isn't on. I'd like to pick up the tabs."
                    dv "Can you plug your toy into the turntable? There's a five-pin jack for the input."
                    stop music fadeout 2
                    me "Why not."
                    play music "<from 17.7 to 56.77>" + music_7dl["splin"] fadein 1
                    "I got the mini-jack out of my pocket and, after a bit of fiddling, got the player to play «Splin»."
                    dv "Good stuff!"
                    "Alisa nodded approvingly."
                    dv "What's the band, and what's the song called?"
                    me "The song's called «Romance», but I forgot the band."
                    "The last thing I need to blurt out right now is something like «oh they don't exist in your timeline yet»."
                    show dv think pioneer at cleft with dspr
                    "And Alisa looked at me so thoughtfully, so thoughtfully... I'd bet she liked me - if I wasn't sure she didn't!"
                    "Dvachevskaya can only like violence!"
                    dv "Really sounds like «Splin»."
                    "My jaw was pulled sharply down somewhere."
                    th "How does she..."
                    show dv concent pioneer at cleft with dspr
                    "Alisa continued to study my face thoughtfully. I swallowed frantically."
                    th "Is this really that old of a band? This is ridiculous!"
                    "But the redhead's intense gaze didn't encourage much thought."
                    me "Alis, you, ahem."
                    me "If you keep staring at me like that, I'll think I messed up again."
                    show dv laugh pioneer at cleft with dissolve
                    dv "I wonder what would happen if all this junk..."
                    "She generously circled the vinyl piles with her hand."
                    dv "...would be left here and I arranged dances with your toy."
                    "When I considered the prospect of blowing the rest of the player's charge, I got a little scared."
                    stop music fadeout 1
                    me "It won't work. There's not much charge left. And there's no place to charge."
                    play music music_list["so_good_to_be_careless"] fadein 3
                    show dv smile pioneer at cleft with dissolve
                    dv "That's how we get the cyberneticists involved! It's about time they worked their fill."
                    me "I'm afraid the technology is too complicated for cyberneticists. It's not like you're using a homemade amplifier in vitriol."
                    dv "So you're saying no to a girl?"
                    "Her eyes laughed."
                    me "I'm sorry, but I'll say no. Not the kind of thing I can give so easily."
                    "And then a thought occurred to me."
                    me "However... We can make a deal."
                    show dv normal pioneer at cleft with dissolve
                    dv "Come on! What kind of deal?"
                    me "I'll give you the player and even explain how to use it - and we'll pick a few tracks from there. But only a few! We won't replace the whole disco."
                else:
                    "As if in spite of Ulyana's words, Dvachevskaya turned off the player."
                    dv "Damn, this junk is no good!"
                    me "What's wrong with the music?"
                    show dv angry pioneer at cleft with dspr
                    dv "Everything!"
                    "Alisa pointed her hand at the stack with the fewest records."
                    dv "This is the best there is, but it's not enough for the whole disco."
                    th "Right off the tongue."
                    show us grin dress at cright with dspr
                    us "I think the penultimate one was great. Take it."
                    show dv surprise pioneer at cleft with dspr
                    dv "That horror?!"
                    "Sincerely marveled the senior redhead."
                    show us dontlike dress at cright with dspr
                    us "You're the horror yourself. It's a normal song."
                    hide us
                    hide dv
                    with dissolve
                    th "Is it just me, or does it smell like kerosene?"
                    dreamgirl "I don't think so. They're thick as thieves. It's normal for them to talk like that."
                    dreamgirl "By the way, I have an idea how you can get the redhead to like you and save the whole camp from dancing to '70s hits. Want one?"
                    if dr:
                        th "As if I need her favor..."
                        "Mentally I muttered."
                    elif loki:
                        th "Go ahead."
                    elif herc:
                        th "Sure."
                    dreamgirl "Give her your Walkman."
                    "After weighing the prospect of blowing the rest of the player's charge, I got a little scared."
                    th "It won't work. There's not much charge left. There's nowhere to charge it."
                    th "Besides, I don't have a plug, and I won't let you shred the headphones."
                    dreamgirl "So get the cyberneticists involved! It's about time they worked off the content."
                    th "They might have the plug, but I'm afraid the technique is too complicated for them. It's not like they're trying to etch homemade amplifiers in vitriol."
                    dreamgirl "So you won't help a girl?"
                    "Sneeringly inquired the inner voice."
                    me "Hmm..."
                    show dv normal pioneer at cleft
                    show us normal dress at cright
                    with dissolve
                    dv "Why are you humming? Give me a hand!"
                    "Turns out, while I was having a conversation with my inner voice, my girlfriends started going through the 'junk' stack."
                    me "Decided to compromise?"
                    show dv angry pioneer at cleft with dspr
                    dv "What else is left there?"
                    th "There's something left."
                    me "Alisa, I want to propose to you."
                    if (lp_dv >= 9) and (not loki):
                        show dv grin pioneer at cleft with dspr
                        dv "Isn't it a little early?"
                        me "Stop grinning. I'm serious."
                        show dv normal pioneer at cleft with dspr
                        dv "Really? Alright, let's hear it."
                    else:
                        show dv normal pioneer at cleft with dspr
                        dv "Well, well, well?"
                    "I took the player out of my pocket and handed it to Dvachevskaya."
                    "She took it and turned it thoughtfully in her hand."
                    dv "And what is it?"
                    me "Music."
                    "The redhead grinned and gave the player to Ulyanka."
                    show us surp2 dress at cright with dspr
                    dv "Here."
                    hide dv with dissolve
                    "And she kept going through the box."
                    th "What a bitch."
                    us "Wow! What is that? I've never seen that before."
                    me "It's called player."
                    show us normal dress at cright with dspr
                    "I pointed to a bar of 'Walkman.'"
                    me "Four gigabytes of music for all occasions."
                    show dv surprise pioneer at cleft with dissolve
                    dv "A giga... what?"
                    me "Simply put, about a thousand minutes of sound with average quality."
                    me "But it's better to hear it once."
                    "I took the player from Ulyana and plugged in the headphones."
                    show dv grin pioneer at cleft
                    show us smile dress at cright
                    with dspr
                    me "Here, put one in each ear."
                    "The girls obediently did as commanded."
                    "Although I noticed a strange suspicion in Dvachevskaya's eyes."
                    th "Expecting some kind of mischief? That, dearie, is more your department."
                    stop music fadeout 1
                    "Ulyanka, on the other hand, was interested."
                    play music "<from 17.7 to 56.77>" + music_7dl["splin"] fadein 1
                    show us surp2 dress at cright
                    show dv surprise pioneer at cleft
                    with dissolve
                    "I chose a song that I thought DvaChe would like."
                    "And I didn't miss it."
                    "A mask of contempt and skepticism dripped off Alisa's face like liquid wax."
                    "It wasn't hard to guess that she wasn't expecting any good taste from me. And here's such a surprise..."
                    show dv normal pioneer at cleft with dspr
                    dv "Good music."
                    "In a neutral voice, Alisa reported."
                    "Looking at that face, I couldn't hide a smile."
                    me "Glad you liked it."
                    $ lp_dv += 1
                    stop music fadeout 3
                    pause(2)
                    "After scrolling through a couple more songs for clarity, I paused playback and said,"
                    play music music_list["so_good_to_be_careless"] fadein 3
                    me "That's it, the mini-concert is over."
                    show us laugh2 dress at cright with dspr
                    us "Cool!"
                    "Ulyana marveled."
                    us "I want that thing for myself. Give it to me!"
                    show us sad dress at cright with dspr
                    me "No!" with vpunch
                    show dv laugh pioneer at cleft
                    show us dontlike dress at cright
                    with dspr
                    us "Well, please, I didn't feel like it."
                    "Said a very mature girl named Ulyana."
                    "I turned to Alisa."
                    show dv normal pioneer at cleft with dspr
                    me "So my conditions are simple."
                    me "I'll give you the player and even explain how to use it - and we'll pick a few tracks from there. But only a few! We won't replace the whole disco."
                    us "Hey, why is she allowed and I'm not?"
                    me "Because."
                    "Ulyanka showed me her tongue."
                    us "Greedy beef, salted cucumber."
                    hide us with dissolve
                    "And turned away."
                    show dv laugh pioneer at cleft with dspr
                    "Alisa giggled, and got back to business."
                dv "So, what about in return?"
                me "And in return, you'll spend one day on the new radio as a host!"
                show dv shocked pioneer at cleft with dspr
                dv "Radio? But that's for the whole camp..."
                me "Yeah. Pretty much the same as today, except you have to sit there all day. Will you try?"
                show dv guilty pioneer at cleft with dissolve
                dv "A whole day is a lot."
                me "Anyway, I'm not pushing. Tonight you'll see how you're doing, and if you like it then we'll have an Alice DJ."
                show dv normal pioneer at cleft with dissolve
                show us smile dress at cright with dissolve
                us "Sounds like that idiot's name in the book you have under..."
                show dv angry pioneer at center with moveinright
                "Ulyanka did not finish - for some reason, alarmed Alisa instantly rushed to her friend and clamped her mouth shut!"
                show us normal dress at cright
                show dv normal pioneer at center
                with dspr
                dv "Silence."
                "I didn't understand anything, it's probably some kind of internal showdown. I don't know. It's none of my business."
                show us calml dress at cright with dspr
                me "So, Alisa? Shall we make a deal?"
                "She thought, never letting go of Ulyana, who was madly rolling her eyes."
                me "You won't let your friend out? She'll suffocate."
                dv "This one? No... she's like a cockroach, you can't kill it even with crowbar. And she breathes with her nose."
                "She didn't seem to be too warm at the prospect of being locked up, short-circuited, with cybenematics all day, but the desire to listen to something else of that kind won out."
                dv "Good. Give me your toy."
                me "Not so fast. Briefing first. Let Ulyana go now, she won't spill your secrets."
                show dv normal pioneer at cleft with moveinleft
                show us smile dress at cright with dspr
                "Ulyana nodded quickly, and Alisa, narrowing her eyes in disbelief, nevertheless let go of her friend."
                dv "Okay. So where should I click here?"
                "I sighed and brought up a list of songs on the screen."
                "Industrial, soundtracks and lounge fell away automatically - no one here can dance to this."
                "There is at least a couple of playlists with foreign junk from the eighties."
                "Actually, that's where the main sample was."
                "The listeners turned out to be grateful and initially intended to rotate almost one hundred percent of the material they listened to, but I cooled their ardor a bit by reminding them of the agreement and the reasons why I'm so greedy."
                scene bg ext_house_of_dv_night with fade
                play sound sfx_close_door_1
                "Long story short, after half an hour we finished compiling the dance program and moved towards the square, where the equipment was already waiting."
                "I've provided the host for tonight and tomorrow. Mission accomplished! I've earned a lot of experience and now I'll level up for sure."
                with dissolve
            stop music fadeout 1.5
            pause(1)
            scene anim_square_party with dissolve
            play music music_list["lightness"] fadein 5
            voices "Dance! Dance!"
            "The crowd chanted."
            show mt smile dress at center with dissolve
            "Olga Dmitrievna picked up a microphone and began the evening:"
            mt "Good evening, dear friends!"
            mt "It's Tuesday, which means dance night."
            mt "And today we have something very special for you."
            mt "I want to introduce you to the person whose music you will be dancing to today."
            "She extended her hand towards the console."
            if alt_day3_dj == 'mi':
                mt "Miku!"
                hide mt with dissolve
                "Miku just nodded. She was wearing a beautiful aquamarine dress that matched her hair, and huge headphones looked pretty funny on her."
                show mi serious dress with dspr
                "Looks like I wasn't the only one who couldn't help smiling at her curious appearance, because the squad leader suddenly frowned."
                "But you can't get a person of the stage with such nonsense as laughter. She raised her hand and, smiling at us, waved."
                mi "Hello everyone! As the first song, I would like to put something light and kind as today's night."
                "She removed her hand that was holding a disc, and notes of the intro to «Lightness» floated through the evening air - the same composition from the club."
                "Everyone screamed and clapped their hands - apparently, the song was already familiar and beloved here."
                "Holding the headphones with one hand, she spun around, bending, and then Ulyana could not stand it anymore - she rushed under the very speakers and waved her hands to the beat."
                show us laugh dress at right with dissolve
                us "Dance, people!"
                "Evening started!"
                hide mi
            elif alt_day3_dj == 'dv':
                mt "Alisa!"
                "Going to the turntables, Alisa nodded in a businesslike manner."
                "Judging by her face, the attention of the public for her was not quite new, but - not the most frequent experience for sure."
                "Although embarrassing her was more difficult than it seemed - she had already shaken out the first vinyl disc from the slightly tattered sleeve, put it on, smoothly turned up the volume."
                "As soon as the «postman Valera» went to full volume, she instantly stopped the second turntable and rushed to conjure with the player - we agreed to put something from my collection as the third track."
                "Ulyanka did not wait for her friend and rushed to dance."
                if not alt_day2_minijack:
                    "A panting Electronics just ran up to the redhead, proudly waving a wire over his head. I breathed a sigh of relief."
                    th "At least some use for that bastard!"
                    "I told him about the need for a wire about five minutes before the dance began. Remembering the mess that reigned in the monastery of young technicians, I almost began to feel sorry for him."
            return
        sh "There's no point in leading if there's nothing to lead."
        sh "We'll come to you later, okay?"
        sh "We want people to dance, so no one will bother us."
        "I shrugged."
        me "As you say."
        el "See you soon then!"
        hide el
        hide sh
        with dissolve
    "I heard a whole bunch of opinions about such independent dances. Like, it's both dumb and bad, and it happens that everyone is huddling along the walls."
    "But all my life I was lucky that either I came when someone was already dancing, gaining infrasound to the very ears."
    "Either I myself, having run and fed enough courage during the day, with loud cries rushed through the opening doors and took my favorite place, not far from the elevated pulpit, where the leader sat with her «Technics»."
    "But if what I think will play here, things will be very bad for me."
    "I can dance to «Kamarinskaya» even - though it depends on the amount of vodka."
    "But to «Yuri Antonov», for example, my limbs categorically refuse to dance!"
    "I'm used to the fact that you can only listen to music of this kind, and for dancing there are several other directions."
    "Anyway, there's still some time, before the dance, that could be spent walking."
    scene bg ext_house_of_mt_sunset with dissolve
    "I got to the cabin and pushed the door."
    stop music fadeout 2
    stop ambience fadeout 2
    with fade
    return

label alt_day3_makeup:
    play sound sfx_open_dooor_campus_1
    scene bg int_house_of_mt_sunset with fade
    pause(1)
    play music music_list["trapped_in_dreams"] fadein 3
    play ambience ambience_int_cabin_night fadein 1
    if alt_day3_dv_guitar == 2:
        "I remember that Alisa promised me to arrange a concert. Maybe it's better to see her than to waste time at the square?"
    "Oh, these dances..."
    th "Here again, they will be dishonored, and the one feel dumb will be me."
    "I went to clean myself up."
    if alt_day3_dv_guitar != 2:
        "Perhaps skip it?"
    if counter_dv_7dl == 3 and (not alt_day3_duty):
        "I unloaded the supplies in the cabin and, standing in front of the mirror, critically examined myself."
    elif counter_dv_7dl == 3:
        "I stood in front of the mirror and critically examined myself."
    elif counter_mi_7dl == 2:
        "Miku hung the suit hanger on the doorknob, so all I could do was look smarter and feel good. I hope I can do it."
        "I changed and stared at myself in the mirror."
    else:
        "I went to the mirror and stared skeptically into the eyes of the reflection."
    if counter_mi_7dl == 2:
        scene cg d3_me_mirror_bordo_7dl with dissolve
    else:
        scene cg d3_me_mirror_white_7dl with dissolve
    "Height meter eighty-five - not bad."
    "However, thinness and stoop successfully hide from five to ten centimeters, so with DvaChe, for example, which is only seventy-five, we were looking eye to eye."
    if herc:
        "The shoulders are narrow - especially compared to what they have become in the military."
    else:
        "The shoulders are narrow - a phenotype, even horizontal bars did not contribute to their expansion. However, one summer I happened to work on the construction of a house ... "
    "The chin is narrow, weak-willed. The lips are the same, but the slightly larger lower one speaks of a capricious and windy temper. The nose is classically even."
    "Eyes...{w} None. Not memorable at all."
    "I took two steps back and focused on the big picture, the image."
    "This faceless something, with not the most attractive appearance and charisma, tending to the negative - can it inspire at least some interest?"
    "Personally, it seemed to me that it could not. I did not like myself, clearly."
    "I would probably even hate myself - if it didn't require such strength."
    if counter_un_fz == 2:
        "It made Lena's obsessive looks in the canteen even weirder than they were."
    me "I don't like you, freak. {w=.3}And it's definitely mutual.."
    play sound sfx_close_door_1
    pause(1)
    scene bg ext_house_of_mt_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 6
    "I said to the reflection and, slamming the door, went out into the street."
    "I remember I was invited somewhere."
    if counter_un_fz == 2:
        "I went outside, greedily breathing in the evening air."
        "It was still too bright for the scary stories Ulyana suggested."
        "And anyway, I wasn't entirely sure I wanted to go there."
        th "Maybe we should just forget them all. It would be nice to just walk around the camp and clear my head."
        "When all the people are gathered in one place, the empty corners become many times more tempting."
        "There was something masochistic about knowingly avoiding imaginary fun like that, reveling in being alone where you're sure not to get caught."
        "Sitting in the shadows, listening to the laughter and shouting, and comforting yourself that you haven't joined the herd."
        "It's at times like this that being unsociable and melancholy becomes a point of pride rather than an unfortunate hindrance to painless integration into society."
        th "Come to think of it, what are all these activities for anyway?"
        th "To open children's eyes to their priorities in life?"
        "I've long speculated that introversion is not realized in those moments when you're sitting alone and feeling good."
        "Full awareness and acceptance of it happens just when you don't feel the rush of energy being in an emotionally charged crowd."
        "You could have gone and watched Slavya and the cyberneticists dancing in the square, giggling gloating fist-pumpingly at how silly they looked."
        "But the wharf, the warehouses, or even a lounger in front of my cabin-any secluded spot would have been preferable."
        "And yet the thought of Lena kept me going. The conversation had to end."
        "Would she be at the disco? Hardly."
        "She said she didn't like dancing."
        "But she didn't have the kind of egregious defiance that was beating out of the redhead tandem."
        "I couldn't imagine her disobeying the counselor's instructions to attend the event on a mandatory basis."
        "With those thoughts in mind, I went to the square."
    stop music fadeout 3
    with fade
    return

label alt_day3_dv_lf:
    scene bg ext_house_of_mt_sunset with dspr
    "Maybe she's there now?"
    scene bg ext_stage_big_night with dissolve
    "It turned out to be closer to the stage than I had hoped."
    "In any case, I did not have time to muster up the courage."
    "And last but not least, this was facilitated by the guitar performance of «Blow with the fires», which I heard almost from my own cabin."
    "Someone was sitting there and playing."
    "Although why «someone»? I already know for sure."
    "It's just a matter of whether she'll be happy with my dubious company."
    play music music_7dl["dv_guitar"] fadein 7
    "I climbed up on the stage."
    scene bg ext_stage_big_night with dissolve
    $ persistent.sprite_time = "night"
    $ night_time()
    $ lp_dv += 1
    "She was playing some unfamiliar, but extremely sad tune."
    "The guitar in her hands sang and cried, giving out a sound that the instrument seemed unable to give out."
    if alt_day2_minijack and (alt_day2_convoy != 'dv'):
        "Alisa was completely absorbed by playing, and did not pay attention to those around her, which allowed me to get closer and sit in the same place where she sat yesterday."
    else:
        "Alisa was completely absorbed by playing, and did not pay attention to those around her, which allowed me to get closer and sit in the most convenient place."
    "She kept playing and playing, I sat and was afraid to move, to frighten away the magic of the moment."
    "Finally, the last chord was screwed into the air, and the girl, pressing the strings with her palm, exhaled sharply, as if someone had pierced an inflatable ball - all somehow shrinking and hunched over."
    play ambience ambience_camp_center_evening fadein 2
    show dv guilty pioneer2 at center with dissolve
    if (alt_day2_date == 'un_fz'):
        dv "Evening."
        "I nodded."
        dv "Why did you come?"
        "I shrugged,"
        me "Don't go dancing. I can see monkeys at the zoo."
        stop music fadeout 3
        show dv smile pioneer2 with dspr
        "Alisa slapped the strings with her palm and smiled."
        dv "What a warm attitude!"
        me "I mean, they don't have anything I could like them for, they don't like me either. So I'd better go and see what I'm really interested in."
        show dv grin pioneer2 with dspr
        dv "So how is it?"
        me "You're playing great. Can you play anything else?"
        dv "No, the concert is over."
    else:
        dv "You've come."
        stop music fadeout 5
        "She calmly remarked."
        me "Yes."
        "I decided to answer in the same style."
        show dv sad pioneer2 with dspr
        dv "Why?"
        me "You called."
        dv "Only that?"
        me "That's enough for me."
        "I stretched my legs out on the bench in front of me and rested my hands on the back bench, relaxing in the makeshift «chair»."
        me "You promised to play a song of your own making."
        show dv shy pioneer2 with dspr
        dv "You just heard it."
    "She answered blankly."
    me "Well…"
    "I sighed and got up."
    me "Since the concert is over..."
    hide dv with easeoutright
    "I turned around and was about to leave, when a surprisingly plaintive word suddenly flew into my back."
    show dv guilty pioneer2 at center with dissolve
    dv "Wait..."
    me "Yes?"
    "I turned around."
    me "Did you want something?"
    if (alt_day3_dv_guitar == 2):
        show dv shy pioneer2 with dspr
        dv "Would you like to try?"
        play music music_list["get_to_know_me_better"] fadein 5
        me "Well, I'm not very good at music..."
        if loki:
            "For some time already."
        dv "It's easy here, look."
        "It seems there was her interest here."
        "I don't know what she's up to - but I don't really like it. Maybe leave before it's too late?"
        "I hesitated, looking at her. From Dvachevskaya so far, without exception, I have only had trouble."
        "So maybe it's worth breaking the vicious cycle? Get off the train before it accelerates?"
        th "Or?"
        show dv normal pioneer2 with dspr
        dv "Hey!"
        me "What?"
        dv "Don't fall asleep."
        me "Yes, I'm not sleeping, I..."
        dv "Meditate with your eyes open. So, are you going to try?"
        me "Play?"
        show dv angry pioneer2 with dspr
        dv "Rrrrr. Yes, play. Will you?"
        me "I don't know. But show me then, for starters."
        show dv normal pioneer2 with dspr
        "She nodded and pressed the first chord."
        "..."
        scene cg d3_dv_scene_2 with fade
        "String picks floated into the night air."
        th "Now that she's holding the strings like this..."
        me "Looks like nothing complicated."
        dv "Well, you, most importantly, take the first chord, and then the third down, well, it's easy to guess."
        "Yes, indeed, I ran and guessed. A man who held a guitar in his hands exactly one and a half times in his life."
        me "Eh... But I'm not promising anything."
        scene cg d3_dv_scene_1
        with dissolve
        "First chord with wooden fingers."
        "And hitting the strings with sausage fingers."
        "Even the guitar seems to take constant practice."
        dv "Oh..."
        me "Don't groan, wait."
        dv "Come on, come on."
        "She giggled softly."
        me "Just haven't played in a while."
        "It was like I was apologizing for something. What nonsense!"
        me "Let's try."
        "Wooden fingers woodenly hit the strings, woodenly moved out of the mode."
        "The guitar made a sound that sounded more like a hungry cat meowing."
        me "Is your guitar out of tune?"
        dv "You are the one who is out of tune. Give it back!"
        scene cg d3_dv_scene_2
        with dissolve
        th "Yeah, it's easy to prove your superiority where you're obviously stronger."
        "She took the guitar away and fluently played a chord progression."
        "Apparently, taking pity on my already well shaken self-esteem, she did not play the solo, which she was tormenting just at the moment when I approached."
        me "I hope at least one of us enjoys the process."
        dv "If you stop raping the guitar and do it humanly, we'll both enjoy it."
        "She played again and looked at me questioningly."
        dv "Do you understand everything?"
        me "Uh..."
        scene cg d3_dv_scene_1
        with dissolve
        "It was quite logical to expect that nothing worked out for me."
        "You can't replace practice with sheer enthusiasm. Practiced hands are needed here, otherwise nothing will work."
        th "Self-realization at my expense."
        "I thought with unexpected anger and, forgetting about what I was doing at all, I even depicted some semblance of what Alisa was showing."
        stop music fadeout 3
        th "Suddenly."
        play ambience ambience_camp_center_night fadein 2
        scene bg ext_stage_normal_night
        show dv normal pioneer at center
        with dissolve
        dv "Didn't overstrain?"
        "I sipped the unprintable under my breath."
        show dv laugh pioneer with dspr
        "And Alisa, hearing the end of the tirade, laughed heartily."
        dv "Don't even think about it. I won't let you do that with my guitar."
        me "Yeah. {w}You prefer much creepier stuff."
        show dv smile pioneer with dspr
        dv "It's okay. You're not as hopeless as I thought."
        dv "We'll make a guitarist out of you sometime."
        me "Really? Oh thanks, I've been dreaming all my life, trembling with anticipation."
        show dv normal pioneer with dspr
        dv "Take your time. You still need to straighten your arms."
        "Looks like Dvachevskaya had a built-in immunity to sarcasm."
        dv "And this will be the most difficult!"
        me "The hardest part will be getting me to repeat this experience again."
        "I got up and dusted off my pants."
        show dv laugh pioneer with dspr
        dv "Giving up already? I just thought you weren't a wimp."
        "Her childishly naive attempts to constantly manipulate others seemed to be obvious only to me."
        "And at first they made me laugh."
        "Now they cause nothing but irritation."
        th "Looks like I've been called here solely and exclusively as a victim of ridicule."
        me "Anyway. I'll go dry."
        show dv surprise pioneer with dspr
        dv "What?"
        me "From the stream of slop that was poured on me here."
        show dv laugh pioneer with dspr
        dv "Are you offended, or what? You should be offended at yourself for having hook-hands."
        me "If the last sentence was a substitute for an apology, then it's extremely bad."
        me "Good night. It would be better if I went to the dance to disgrace myself. At least no one was going to mock me there."
        "And what's next, then? A beautiful gesture was made, leaving, go away?"
        "Further experience suggested adding the offender to the black lists and ignoring it in all possible channels."
        "It's a pity, in real life this is impossible. That's who I would love to turn off from my own life."
        show dv grin pioneer with dspr
        dv "Are you really offended?"
        show dv surprise pioneer with dspr
        dv "Seriously?"
        "Looks like it dawned on her that she really said something wrong."
        me "How did you know?"
        "I once again slipped into sarcasm - completely useless against this girl."
        dv "You're upset and you're going to run somewhere."
        th "What a deduction, Sherlock!"
        me "I hope you, at least, enjoyed this stupid evening."
        hide dv with dissolve
        "I turned around and moved out of the place."
        "I've had enough for today."
        "Alisa said something to me in the back, but I was no longer going to waste time and nerves on her."
        me "You are the worst thing I've ever seen in my life."
        "I hissed under my breath."
    elif counter_dv_7dl == 3:
        dv "Why are you... so."
        "It seems that she was embarrassed by my behavior. And yet I was not going to make life easier for the person who decided everything for me."
        me "What are we talking about now?"
        "I asked politely."
        me "If it's about music, then you promised to play a song."
        me "You played, I listened, and we, satisfied with each other, scatter in our caves. Thanks for the warm evening."
        dv "No."
        show dv sad pioneer2 at center with dissolve
        "Due to the darkness that descended, her face was almost impossible to see, I had to focus only on silhouette."
        dv "I'm talking about our conversation."
        me "Yeah. Let me guess: you think you did the right thing, and I'll thank you later for that?"
        show dv normal pioneer2 with dspr
        dv "No."
        "She shook her head again, and her voice dropped to a whisper."
        dv "I... {w}I wanted to say I'm sorry."
        me "Sorry for wasting your time?"
        me "Don't worry about that, I won't bother you anymore."
        "I myself do not know what kind of demon possessed me, but it was definitely an extremely cruel and venomous demon."
        "Alisa endured that too. She just shuddered and cringed, as she did at the club."
        dreamgirl "What are you doing, you moron?!"
        dreamgirl "The girl asks you for forgiveness, but you turn up your nose?"
        dreamgirl "Do you have too many alternatives?"
        th "You're not my conscience. Be quiet."
        dv "No, I..."
        me "You..."
        "Encouragingly I continued."
        "It was clearly indispensable without encouragement - the girl had to make great efforts to just continue the conversation."
        "But it still wasn't enough."
        dv "...sorry for everything I said to you."
        "You could see how hard it was for her to apologize."
        dv "I was wrong."
        me "No, you were absolutely right: we shouldn't have ruined a beautiful friendship with all this romantic crap."
        me "Your only blunder is in Lena: we haven't exchanged even a couple of phrases for three days with her."
        show dv shy pioneer2 with dspr
        if alt_day1_un != 0:
            dv "What about the first day then?"
            "Her voice was dangerously balanced between tears and whispers. Although it is unlikely that a girl like Alisa would sob. Too strong, too independent."
            dv "I've seen you spud her."
            "And here I could not stand it."
            me "Spud?" with hpunch
            me "Is that what it's called now?"
            show blinking
            me "Alisa... Just one question: proverb about a dog in the manger is in use here?"
            show dv guilty pioneer2 with dspr
        "She didn't say anything."
        "Looks like there's no point in talking any further."
        me "That's all I wanted to know."
        hide dv with dissolve
    $ alt_day3_dv_guitar = 3
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_dv_reunion:
    scene bg ext_houses_night_7dl with dissolve
    play ambience ambience_camp_center_evening fadein 3
    "I finally turned around and left, leaving Alisa alone with her stupid thoughts, idiotic jealousy and unfounded claims."
    "And guitar picks continued to spin in my head..."
    play music music_7dl["deadman"] fadein 3
    "Night camp is different every time."
    "On the first day, it was warm, a little intimidating and in some ways even languid."
    "In the second, I seemed to wake up, and everything was bright, so bright..."
    "Today, a slightly tart cinchona taste of wormwood-disappointment is added to everything."
    "Music is heard from behind the trees, the pioneers danced to it, shouting something."
    "Couples are already visible in the alleys, at the water column there was already a line of several boys dancing so that their shirts were soaked through."
    "In first line order, they put their heads under the stream of icy water, hooted in delight and bounced back."
    "For some reason, my legs took me to the warehouse."
    scene bg ext_warehouse_night_7dl with dissolve
    if alt_day1_el_followed:
        "The lips themselves formed into a smile when I remembered how Electronic and I hid here from the wrath of Dvachevskaya."
    "I drove away in my memory everything that connected us, everything that we experienced and could remember together."
    "And the night meanwhile entered into full rights, a bottomless black sky opened up overhead."
    "The stars were overhead, today some are especially faded and inexpressive..."
    "...and I suddenly realized that, in fact, they were ready to let me go."
    "Apparently, I did not justify someone's hopes, apparently, I really am hopeless."
    "I just have to make a clear request - and I'll wake up at home, with my nose on the keyboard."
    "On the left hand the moon rose, and I, turning in its direction, took a full chest of air."
    "And spoke:"
    scene bg ext_warehouse_blurry_7dl
    "Reality shuddered as it absorbed my words."
    me "Please… please. I really want to go home. Let me Lea..."
    scene black
    $ prolog_time()
    with fade2
    if loki:
        show blink
        scene bg ext_winterpark_7dl
        with dissolve
        pause(1.5)
        "I paid full price for my stupidity."
        "What a pity that there is no one to present the paid bill."
        "The cold got under the skin, and the strength left was enough only to smile quietly."
        "I'm a fool. And I'm very guilty."
        "Hopefully in my next life I'll have a chance to make things right."
        play sound sfx_7dl["aunl"]
        $ sdl_persistent_inc("alt_deep")
        show acm_logo_va_deep with moveinright:
            pos (1600, 1020)
        pause(4.4)
        with vpunch
    elif herc:
        play music "<to 52.94>" + music_7dl["herc_death"] fadein 5
        scene black with fade
        "Just one day, the door to summer opened and let out someone who was hopeless even by the standards of the land of dreams."
        "And whatever the blind spot in my head turns out to be, I'm sure it's still better than an unfulfilled dream."
        "An unfulfilled red dream with huge amber eyes."
        "Time to go home."
        scene bg int_store_7dl with fade
        "You accept the rules of the game. You forget who you are and what you are."
        "For what?"
        play sound sfx_7dl["makarych"] fadein 0
        "My cold city is waiting for me, the cold streets and the ruffled indifference of passers-by-birds running somewhere."
        scene black with fade
        "I don't know anything else, Since this is my home."
        "It's time for this journey to end."
        "Wonderful journey."
        "With the length of three days of summer."
        play sound sfx_bodyfall_1
        stop sound_loop fadeout 0
        play sound sfx_7dl["aunl"]
        $ sdl_persistent_inc("alt_deep")
        show acm_logo_va_deep with moveinright:
            pos (1600, 1020)
        pause(4.4)
        with vpunch
    else:
        scene bg int_intro_liaz_7dl with fade
        stop ambience fadeout 2
        "All this is just a frosty dream of a loser who has frozen over the wheel."
        "Almost a song."
        "Hussar, almost perched on the wall."
        play sound_loop sfx_bus_interior_moving fadein 0
        pause(2)
        scene black with fade
        $ volume(0.0, "music")
        stop sound_loop fadeout 0
        "You could already see the bulk of the bridge ahead."
        "The thought came to mind that it would be curious - what would happen if the bus fell down?"
        "Not scary, not creepy, not interesting. Just languidly curious."
        play sound sfx_7dl["aunl"]
        $ sdl_persistent_inc("alt_deep")
        show acm_logo_va_deep with moveinright:
            pos (1600, 1020)
        pause(4.4)
        with vpunch
    stop music fadeout 3
    stop ambience fadeout 6
    scene black
    call screen alt_timer
    if alt_day_catapult:
        "I opened my eyes."
        scene gameover with gopr
        $ sdl_persistent_inc("alt_qte_fail")
        if persistent.alt_qte_fail >= 5:
            play sound sfx_7dl["aunl"]
            $ sdl_persistent_inc("alt_victim")
            show acm_logo_va_victim with moveinright:
                pos (1600, 1020)
        pause(3)
    return

label alt_day3_dv_stayhere1:
    $ counter_dv_7dl = 4
    if persistent.alt_victim and not persistent.alt_qte:
        play sound sfx_7dl["tousche"]
        play sound2 sfx_concert_applause
        $ persistent.alt_qte = 1
        show acm_logo_va_qte with moveinright:
            pos (1600, 1020)
        pause(9.4)
    else:
        play sound sfx_7dl["aunl"]
        $ sdl_persistent_inc("alt_qte")
        show acm_logo_va_qte with moveinright:
            pos (1600, 1020)
        pause(3)
    with vpunch
    stop music
    scene bg ext_warehouse_blurry_7dl with flash
    $ volume(1.0, "music")
    stop music fadeout 4
    play music music_list["what_do_you_think_of_me"] fadein 3
    "The icy embrace reluctantly let me go."
    "Something hot dripped on the shoulder, straight through the shirt."
    scene bg ext_warehouse_night_7dl with dissolve
    "I did not have time to get scared, and patiently waited for what would happen next."
    me "Someone decided to use me as a break?"
    "Lazily I threw over my shoulder, and from there only sniffing and ragged breathing could be heard."
    "Finally I was able to turn around."
    show dv cry pioneer2 at center with dissolve
    "Alisa."
    "Crying Alisa."
    "I think now she will bury me as a witness to her own shame."
    show dv cry pioneer2 close with dissolve
    "But instead of recoiling, she clung even tighter."
    me "What happened?"
    "I inquired neutrally."
    "Yet the voice faltered a little, and this hesitation told the waiting ear much more than all the words in the world."
    dv "I c-don't..."
    "She was hysterical or something like that. I'm not very good at dampening female tantrums, so all I had to do was outline some kind of hug. And wait."
    "But not very strong ones, or she could think about something again."
    me "What?"
    "Exactly I asked."
    show dv guilty pioneer2 close with dissolve
    dv "Forgive me. Please."
    "Here, of course, she surprised me."
    me "For what?"
    me "You didn't say anything that went against your beliefs."
    me "And you have to live in peace with yourself. I know that for sure."
    dv "That's not true... I want to, but I'm afraid."
    me "Afraid that you might feel something?"
    me "Well, this is a passed stage - you have already shown that I do nothing but annoy you."
    show dv sad pioneer2 close with dspr
    dv "That's not true."
    "She shook her head."
    dv "You don't know what you're talking about."
    me "I talking exactly what I was either told directly or made to understand today."
    me "I'm not exactly a retard."
    "I chuckled."
    me "Though you certainly think otherwise."
    dv "I'm afraid that one day I'll wake up and you're gone."
    "She seems to have calmed down, at least enough to let go of her shaking."
    show dv guilty pioneer2 close with dissolve
    "I allowed myself to smile."
    me "If you're afraid that someone will take your toys, sooner or later it will happen."
    me "And since you've calmed down, let's go wash up, and then we'll think."
    dv "O-okay."
    stop ambience fadeout 2
    "She sobbed and in the dark, while no one see us, took me by the arm."
    scene cg d5_dv_island with dissolve
    play ambience ambience_forest_night fadein 3
    "That was difenetely not what I was expecting!"
    "After all of today's boyishness. After this stupid conversation, from which I only understood that I is more valuable as an ally and playmate than..."
    "And suddenly such signs of attention!"
    "Of course I didn't hesitated about myself - after all, I was already seventeen once."
    "My attractiveness fluctuates between zero and negative values."
    "So I'm physically unable to arouse any feelings."
    "Atleast, at seventeen, I certainly was unable."
    "I tried to free my hand, but Alisa only made it worse by pressing her whole body against it."
    "Blood rushed to my face as I felt the heat of her body through the thin shirt."
    "I don’t know how comfortable it was for her to walk, but suddenly my legs seemed to have become wooden."
    scene bg ext_washstand_night_7dl
    with dissolve
    play music music_list["sweet_darkness"] fadein 3
    play ambience ambience_forest_night fadein 3
    us "Tili-tili-dough, bride and groom!"
    "Was heard from washbins."
    show us laugh dress with dissolve
    "In the darkness stood a short figure, however, I recognized it by two missile tails."
    me "Ulyanka, why are you wandering around in the dark?"
    "I didn't respond to the mocking."
    "Alisa also kept silent, it seems, entrusting me with the reins of power."
    us "Wanted to make sure you were really tili dough."
    show us normal dress with dissolve
    us "Why do you need it, I can't understand. You can't stand each other, but you seem to be even worse apart."
    hide us with dissolve
    play sound sfx_open_water_sink
    play sound_loop sfx_water_sink_stream fadein 1
    "She waved her hand and disappeared into the darkness, giving me the opportunity to wash the sobbing Dvachevskaya."
    "The water was ice cold, as always, and I also threw a couple of handfuls of water in my face to cool my burning cheeks a bit."
    "After what Alisa did..."
    "...Ulyanka blessed us, well, wow!"
    stop sound_loop
    play sound sfx_close_water_sink
    show dv normal pioneer with dissolve
    dv "I'm finished."
    "She was still shaking a little more after the scene at the warehouse, plus cold water. And I had nothing to warm her with... "
    "Anyway, she straightened her shirt in an impotent attempt to keep warm."
    me "Good."
    "I found her hand."
    me "Let's go then."
    "I pulled her along, leading her to the houses."
    scene bg ext_houses_night_7dl with dissolve
    show dv surprise pioneer with dissolve
    dv "What? Where?"
    me "For starters, to my cabin."
    show dv shy pioneer with dissolve
    dv "What, right away?"
    "I shrugged."
    me "Why wait? Personally, I find it most convenient there."
    dv "Well... I don't know... What if Olga..."
    "She was confused."
    me "Why, you think she doesn't understand or something. It's a young thing after all."
    "I lowered my voice."
    me "Don't be afraid. We're fast. Op - and it's done!"
    show dv shocked pioneer with dissolve
    dv "..."
    me "Knowing you, we'll make it fast."
    "I think I embarrassed her enough to feel vindicated."
    me "And in general, doctors do not recommend doing such things before sleep. They say it's harmful."
    me "But you haven't eaten anything since dinner. Let's go!"
    show dv shy pioneer with dissolve
    "The way she flared up was noticeable even in the light of the moon."
    th "How lovely."
    dreamgirl "Congratulations boy, you just passed your entrance exam to Dr. Violetta's school."
    dv "Well... I whistled some candies from Ulyana."
    "Finally getting over herself, she confessed."
    scene bg ext_house_of_mt_night with dissolve
    play sound sfx_open_dooor_campus_1
    pause(2)
    stop ambience fadeout 1
    scene bg int_house_of_mt_noitem_night with fade
    pause(1)
    play ambience ambience_int_cabin_night fadein 1
    if alt_day1_me_d3_dv_feed:
        me "And I cooked dinner for you, modestly, but anyway."
    "I opened the door, letting her in."
    if alt_day1_me_d3_dv_feed:
        me "Buns and kefir. Everything I found."
    show dv smile pioneer far at center with dissolve
    dv "Now I owe you even more."
    if alt_day2_date == 'dv':
        "She smiled without her usual arrogance - almost like then, on the beach."
    "She didn't hesitated much, gobbling up with such an appetite that I also start feeling hungry."
    "I didn’t get it though - her teeth clattered dangerously close to the outstretched hand{nw}" with vpunch
    extend ", and I hurried to hide the limb."
    "I smiled and sat on the bed watching the girl eat."
    "Another five minutes of hard work with the jaws - and she fell off the table full."
    me "That's good. Now let's talk."
    play music music_list["tried_to_bring_it_back"] fadein 3
    show dv sad pioneer at center with dissolve
    dv "About what?"
    "She looked up, not feeling too comfortable tête-à-tête with the half-familiar guy in the cabin."
    me "Yes, yes, exactly what you thought - about you and me. {w}As the Americans say, about girlfriends and boyfriends."
    show dv guilty pioneer with dspr
    "She blushed, it seems, understanding me somewhat wrongly, to which I hastened to remark:"
    me "Not really about that, although I like your way of thinking."
    dv "What then..."
    "She was completely embarrassed."
    me "I'm going to feel like an idiot, but this looks like it's for business."
    "I crawled closer to her and, taking her hand, looked into her eyes."
    me "Usually it should happen spontaneously, but... Dvachevskaya, what do you think about becoming my girlfriend?"
    show dv shy pioneer with dspr
    "She was even more embarrassed."
    dv "I... don't know how to."
    me "Don't know? {w}I don't know either. Somehow I've never had to be someone's girlfriend before."
    dreamgirl "Cretin, what are you talking about?!"
    th "I figured a little comic relief wouldn't hurt."
    dv "No, I'm saying I haven't dated anyone yet."
    me "I get it. {w=.2}Well, we all learn little by little, something and somehow."
    dv "So what do I need to do?"
    me "First, stop being embarrassed. And then..."
    stop music fadeout 4
    hide dv with dissolve2
    "I was silent for a while, thinking about... what then really... "
    me "Enjoy life and each other's company. To the best of our ability."
    "Finally I've found it."
    play music music_list["farewell_to_the_past_edit"] fadein 5
    me "What a good night!"
    me "Let's go for a walk?"
    "She didn't answer."
    me "Alisa?"
    "I turned in her direction."
    if alt_day2_us_escape:
        "Hmm... It seems that I am so boring that all female creatures in the foreseeable space, when I approach, experience an irresistible desire to sleep - starting with Olga, ending with Ulyanka and Alisa."
    else:
        "Hmm... It seems that I am so boring that all female creatures in the foreseeable space, when I approach, experience an irresistible desire to sleep - starting with Olga, ending with Alisa."
    "Feared ahead for a year ahead, the young body resorted to the easiest way to recover from stress - deep sleep."
    "Smiling, I picked her up and carried her to the bed, went outside, where I took a fancy to the lounger, tumble a bit, getting comfortable, and closed my eyes."
    scene black with fade2
    "After a while, the fabric of a nearby deck chair creaked, taking someone else into its arms, for some reason in a whisper a female voice asked:"
    voice "Sleeping?"
    me "Yeah. A proper ending to a tantrum."
    voice "So you with her didn't..."
    me "No, we didn't fight much."
    "I pretended not to take the hint."
    me "Just washed, fed, and she fell asleep herself."
    voice "Wow..."
    "The voice sounded surprised."
    voice "In my memory, you are the first one who managed to tame Dvachevskaya."
    me "It was enough just to stop lying to myself."
    voice "I wish I could learn this..."
    scene bg ext_house_of_mt_night_without_light with dissolve
    stop ambience fadeout 1
    show un modern shade close at right with dissolve
    "The lounge creaked again, with the background of stary sky, four tails flashed..."
    show un smile dress close at right with dspr
    me "Lena?!"
    "I gasped."
    un "And who did you expect?"
    "She asked slyly."
    un "Olga Dmitrievna maybe?"
    me "Maybe her too. {w}What are you doing here?"
    un "The nurse asked me to help at the infirmary, since I'm not dancing anyway."
    un "Just freed. But if you need some valerian..."
    me "No thanks."
    "I found myself thinking that it is surprisingly easy for me to communicate with this girl."
    "As if there hadn't been several days of mutual embarrassment."
    "And it seems twice as easy for her because the darkness hides her faces."
    show un smile3 dress close with dissolve
    un "Take care of her. She doesn't know what miracle she is. Don't hurt her."
    me "What about…"
    if (herc or loki):
        un "Our conversation before the tournament? This is our internal relationship."
        show un laugh dress close with dissolve
        "She laughed."
        un "Looks shocking, I understand."
    else:
        un "What, hesitate because of her behaviour? Ignore it."
        show un smile2 dress with dspr
        un "It's not the real her, I know."
    me "No, I'm talking about something else. About her mania - she's afraid that you want to take away all her toys."
    "I stumbled."
    me "Including…"
    show un smile dress close with dissolve
    un "You?"
    "She was sitting close, very close, I could see every hair in her ponytails, a gleam of moonlight in her eyes... The look involuntarily attracted to her lips."
    un "And fight her later? Well, she can imagine things, of course."
    un "You is her.{w} It's mutual, so I won't even bother."
    un "Good night."
    hide un with dissolve
    "And like Ulyanka, she melted into the darkness."
    show blinking with dspr
    "I closed my eyes again and, it seems, fell asleep, because I didn’t feel the transition between turning off my consciousness and the beginning of such an unkind shaking by the shoulder."
    show mt smile dress with dissolve
    "It was Olga Dmitrievna, and she did her best to look angry."
    "Which, however, did not go well with a satisfied expression on her face."
    show mt normal dress at center with dissolve
    "But the dress she was wearing was rocking, and I involuntarily followed all the curves and bulges before I realized that she was telling me something."
    mt "...skipping group events, huh?"
    mt "Sitting in an unclear place, doing an unclear things. By the way, why exactly here?"
    me "There's Alisa."
    "I replied in monosyllables."
    mt "And she is..."
    me "Sleeping."
    show mt normal dress at center  with dissolve
    "I don’t know what thought came into the squad leader's mind, but she suddenly became embarrassed and stopped asking questions for a while, went up to the porch, opened the door ajar and looked thoughtfully at the girl sleeping in my bed."
    mt "I won't ask how she got here."
    mt "But you'll have to spend the night on an unmade bed."
    hide mt with dissolve
    pause(1)
    show mt normal dress at center with dissolve2
    "She again went to the cabin and brought back a bunch of keys, exactly like those Slavya sowed when she fed me."
    mt "On the next «street», pay attention to the «barrel» with the emblem near the door, it's also noticeably off the ground."
    "She made a stern look."
    mt "For the first and last time, I hope."
    me "Me too."
    "I sighed."
    me "I like sleeping in my bed."
    show mt smile dress with dissolve
    "Olga suddenly giggled:"
    mt "I'm imagining her face in the morning tomorrow. I'll definitely wake her up myself."
    me "You're a terrible person, Olga Dmitrievna. It's possible to become a stutterer that way!"
    mt "That's okay, maybe she'll learn how to not lose her cavalier next time."
    show mt smile dress with dissolve
    "I blushed."
    me "We don't..."
    mt "Yeah, I know what you don't..."
    mt "Half of the camp is already talking about how Syoma and Aliska were making out at the handwashers. Gossips."
    "She spat that word out like a dirty word."
    mt "And I think, that the main thing is that everything is fair."
    "She pointedly glanced in my direction."
    mt "And for love."
    "I just sighed, and, getting up, went to my temporary place to spend the night."
    hide mt with dissolve
    scene anim_square_party with dissolve
    play ambience ambience_camp_center_night fadein 2
    sl "Semyon! Semyon! Wait."
    "I turned around."
    show sl normal dress with dissolve
    "Slavya, with some sack in her hands."
    th "Another help for the needy?"
    me "What do you want?"
    sl "Well, I heard that you are moving temporarily. So I'll give you a pillow for now, soap and a towel."
    show sl smile dress with dissolve
    sl "By the way, the bathhouse was heated today, so if you want to have a proper wash, I can take a queue for you."
    "After estimating how long I hadn't washed normally, I nodded in agreement."
    me "Sure, why not. Thank you."
    show sl smile dress with dspr
    sl "Good."
    "She smiled and waved her hand towards the woods."
    sl "Follow the path, go past the grove, and you'll come out just right. Don't miss."
    "She smiled and after handing me a pillow with bath accessories, left."
    hide sl with dissolve
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_choose:
    play ambience ambience_camp_center_evening fadein 1
    play music music_7dl["lonesome_shepherd"] fadein 5
    scene anim_square_party with dissolve
    "Finally, the evening gained momentum, and the DJ delighted those present with the first novelty."
    "With slow one - Which is strange."
    menu:
        "Dance with Lena" if not (alt_day2_date == 'un_fz'):
            call alt_day3_lp_checker(alt_dater = un)
            if alt_day2_bf == 'sl':
                $ lp_sl -= 1
            $ alt_day3_dancing1 = 'un_1'
            play music music_list["silhouette_in_sunset"] fadein 3
            "I didn't really understand how you could dance to what the host was spinning, but I stayed out of the way."
            "I preferred to crouch down in a corner and listen to the music."
            "All the more so because through the half-dark square, between the twilight, dispersed only by the light of the garlands and the glow of the light cannon, I occasionally caught Lena's gaze on me."
            show un shy dress far with dissolve
            "I couldn't tell if it was an interested look, or if it was just stumbling over me as part of a routine scouring of my surroundings."
            "But I could feel him on me, and that made something tingle inside."
            "Some kind of rapturous chill of either foreboding or unintentional sympathy for a beautiful girl with a sad look."
            show un normal dress far with dspr
            th "You should know, my dear, the armor-penetrating capabilities of your influence."
            "I glanced sideways at her, avoiding direct contact with her with all my might, and it took all my resolve to take the first step toward her."
            "And so I stepped, and her gaze immediately fixed on me."
            show un serious dress with dspr
            "As I walk on, I feel my back grow stiff and my shoulders slouch, as my knee crunches and my foot sinks awkwardly."
            "How my chin sinks too low, and the breeze that comes in plays in the inappropriate hairs on the top of my head."
            "It's been a long time since I felt as uncomfortable as I did during those ten steps."
            "And she sat on the bench and listened to the music with pleasure, glancing occasionally at my approach."
            me "Shall we dance?"
            "I clicked my imaginary heels together, hiding both my insecurity and my fear of very likely rejection behind my reckless appearance."
            if counter_un_7dl >= 5:
                "The fact that we had just agreed to a dance didn't change matters at all."
                th "I haven't been put in her ball book after all."
            dreamgirl "Calm down, retrograde. And smile at the girl, or she'll think you're inviting her to a funeral."
            show un shy dress with dspr
            "At last she made up her mind and, with a slight nod, stood up, holding my hand."
            scene cg d3_un_dance with dissolve
            "I guided her as I guided the greatest treasure, carefully, reverently, afraid to break or damage it."
            "And she walked to the middle of the dance floor and turned and looked at me questioningly."
            me "What's next? Next is the dance!"
            "Her hands lay down on their own, the right way, the right way, and all she had to do was accept the rules and follow them."
            "The first step in rhythm, the second as it comes."
            "The third is in tune with the breath."
            "And it's always one for two."
            "She is silent, not so much embarrassed as simply not knowing what to say during the dance. {w}Well, it looks like I'm handling tonight."
            me "You have a terrific dress."
            "I started from afar."
            "All the more reason why the hostess is just as good."
            un "Really?"
            me "Of course. I never lie."
            dreamgirl "Except just a little bit."
            if loki:
                me "But that doesn't mean you're the prettiest one here!"
                me "I'm okay too!"
            elif herc:
                me "Actually, I'm very lucky!"
                un "What?"
                me "I managed to invite you before anyone else did."
            "She smiled unabashedly and nodded, relaxing a little."
            "At least her back wasn't so stiff under her fingers anymore."
            "I came within breathing distance and whispered confidentially:"
            me "I'll tell you a secret. I'm not really a very good dancer."
            me "But you seem to inspire me to forget what I'm not good at."
            "She smiled quietly, without raising her eyes."
            me "And I don't much care for dancing either."
            me "But I like it a lot now, for some reason."
            me "Would you like to repeat our dancing experience again?"
            if alt_day3_un_med_help == 1:
                un "But we... Infirmary, remember?"
                me "Big deal. There's still time."
                "I feel bad reminding her of the scene in the warehouse yard, but she seems to understand."
                un "If that's the point... I agree."
            else:
                un "I'm sorry, but no. We'll have to leave."
                "I wasn't hiding my chagrin."
                me "On second thought? Maybe there's still a possibility?"
                if loki or herc:
                    un "Well..."
                    "She clearly hesitated."
                    un "Unless it's just one more dance."
                else:
                   un "Sorry. No."
            "The rest of the dance passed in a meaningful silence."
            "The very one that is only possible between two people who have something to be silent about."
            "The music ended, and we reluctantly let go of our hands."
        "Dance with Lena" if (alt_day2_date == 'un_fz'):
            "I looked for Lena among the dancers, but she didn't seem to be in the square."
            "The girl seems to have found something else to do, or she's good at hiding."
            "I sat back down on the bench and watched other people squirming on the dance floor."
            "All day I never got to talk to Lena and dot my I's."
            th "Well, it's probably for the best."
        "Dance with Miku" if (alt_day2_mi_date != 2) or alt_day3_dv_dj_fale:
            call alt_day3_lp_checker(alt_dater = mi)
            if alt_day2_bf == 'sl':
                $ lp_sl -= 1
            $ alt_day3_dancing1 = 'mi_1'
            stop music fadeout 1
            pause (1)
            play music music_list["lightness"] fadein 5
            if alt_day3_dj == 'mi':
                "Fully in the role of disc jockey, Miku stood at the turntables, watching the sound, in some places even creating a kind of transitions and overlaps, as if she were the forerunner of future DJ schools."
                "She looked so wonderfully-cheesy-a little, fragile girl with beautiful hair gathered in two long ponytails and huge headphones."
                "And it was suddenly obvious to me - whoever and whatever I was looking for before - I found it here. There it is, standing there, speeding up the next hat to the one that's already sounding."
                me "Hello, beauty! Dancing?"
                show mi normal dress with dissolve
                mi "Trying!"
                "Without taking her headphones off, she shouted."
                "I pointed my fingers at the headphones, and she immediately pulled them off her head with an owl."
                show mi smile dress with dissolve
                mi "Did you want something, Senechka?"
                me "I wanted to ask you to dance."
                "I've already put up with all the 'Syomas' and 'Senechkas' in the world - as long as she would be smiling."
                "She bloomed."
                mi "Sure, let's go!"
                "She took me under her arm, and I took her out on the dance floor."
            else:
                "The choreography - even the disco choreography - in Japan is still very different from what we in Central Russia are used to."
                "As renowned individualists who value the intimate zone above all else, they even dance in a way that takes up more space than, say, their fellow Union dancers."
                "And they certainly won't do as these barbarian Russians do: stand in a circle and, encouraging each other with a fervent look and a fancy knee, see who can do what."
                "Those who are good at it go in the circle, and those who are not good at it learn what they learn."
                "Miku's dancing was more like a kind of street ballet - with a certain discount to the local flavor. Disjointed hand and footwork, lots and lots of jumping..."
                "All in all, it came as little surprise that when another voice shut up yelling about high banks, and the bass notes singing of light floated across the concrete - she was alone."
                "Not for long, though - I immediately jumped up to her and suggested, in a sharply seated voice:"
                me "Shall we dance, beautiful?"
                show mi normal dress with dissolve
                mi "Of course!"
                "She grabbed me by the hand and dragged me out onto the floor."
            if counter_mi_7dl == 2:
                scene cg d3_mi_dance_close_bordo_7dl
            else:
                scene cg d3_mi_dance_close_7dl
            with dissolve
            me "You've outshone everyone tonight, both in your dancing and your dress."
            "I wasn't the least bit slanderous."
            "It's so easy to pay a compliment when it's the truth."
            if counter_un_7dl >= 4:
                "Though it's unlikely these compliments would have pleased one quiet girl."
                "But I preferred not to think about it."
            mi "Honestly?"
            me "Honestly couldn't be any more honest. The moment I saw you, I knew right away who I was dancing with tonight."
            "She smiled a little embarrassed."
            if counter_mi_7dl >= 1:
                dreamgirl "Come on, now ask her if she wants to go to the club after the disco, and there in the prop room..."
                mi "You look great too."
                me "Thanks, I'm trying."
            else:
                mi "Too bad you didn't come in today, we could have picked out something nice for you, too."
            if loki:
                me "But that doesn't mean you're the prettiest one here!"
                me "I'm okay, too!"
                "She laughed silently."
            "We danced for a while without saying a word."
            "Personally, I'm enjoying the moment - relatively good music, girl in hand..."
            mi "Sem..."
            "She whispered."
            mi "I understand that I'm sympathetic to you and I appreciate the trust you're giving me - but just a little farther away, okay?"
            if lp_mi >= 5:
                mi "Because I already know you better than I would if I saw you naked."
                "I laughed, not even thinking about moving away. Worse yet, I held her tightly against me."
                if (alt_day2_date == 'mi'):
                    me "And that's after the beach! Everyone around here already thought what they wanted anyway."
                    mi "What they thought is their own business."
                mi "Your proximity distracts me! {w=.4}A little farther away. {w}Or I'll step on your foot."
                "What a scary threat."
                "Making a frightened face, I hastily retreated half a step."
            else:
                "I instantly flashed and pulled away as best I could."
                me "I'm sorry..."
                me "I wondered..."
                mi "It's okay, I even liked it. But it's distracting from the dance."
                "She giggled softly in my ear, and I realized how timely I had moved away."
            "The music ended, and we reluctantly let go of our hands."
            scene anim_square_party
        "Dance with Slavya":
            call alt_day3_lp_checker(alt_dater = sl)
            $ alt_day3_dancing1 = 'sl_1'
            stop music fadeout 1
            pause (1)
            play music music_list["raindrops"] fadein 3
            show sl smile dress with dissolve
            "Slavya jumped up and down with all those weird tunes, but for her, the evening wouldn't be languid enough without the obligatory slow dance."
            "I suspect if I hadn't made it first, she would have announced an extraordinary 'white' dance."
            if counter_un_7dl >= 4:
                "Although I kept thinking that maybe this dance should have been given to someone else."
                "But I preferred not to think about it."
            me "Shall we dance?"
            "She hadn't yet recovered her breath from the previous dance, so it seemed like she was reacting to me like that."
            "And it was as if her shoulders were spreading by themselves, and huge goosebumps were marching down her back in columns."
            show sl smile2 dress with dissolve
            "She's wearing a gray-blue dress, more like a sundress, up to mid-thigh, with an interesting ornament of obviously plant origin."
            "It looks so light that it seems transparent, and I found myself trying to look through it to see if I could see anything."
            me "Your dress is something!"
            "I admitted."
            me "It's a good thing you don't wear it every day."
            me "Otherwise it would be impossible to work or rest. Just relax and there you are, beautiful."
            show sl laugh dress with dissolve
            if ((counter_sl_7dl == 4) or (counter_sl_cl == 6)) and (lp_sl >= 12):
                sl "I promised to show it - here I am!"
                "Smiled the girl."
                sl "But only, I hope this time you don't run away and leave the girl alone on the dance floor."
                me "Touché. {w}This bad move is too classic, too predictable."
                me "It's different if she ran away..."
                scene cg d3_sl_dance with dissolve
                sl "Don't even dream of it!"
                "She took my hands in hers, placed one at her waist and grabbed the other, so that there was no point in thinking about running away."
                sl "We're going to dance - I want it!"
                th "And again, go figure out in what sense those wishes work for her."
                "Basically, if you know a person even a little bit, the eye gets used to the way they behave, their facial expressions, their reactions."
                "And any appearance of unnaturalness can be discerned-if you're observant enough."
                "Miss. {w}It just doesn't work with Slavya."
                "She was making eye contact with me the whole time she was dancing."
                "And it was really, really bad."
                "Because basically, the only way I could get my ego down to the floor was with a look like that."
                "I mean, I was quite admitting that there were people who vitally needed direct eye contact during intercourse."
                "But Slavya hasn't shown herself to be such a person so far."
                th "Has she been adjusting to me?"
                "Probably only her hypnotic influence could explain the fact that after a few seconds of obscuration I found myself much closer to her than before."
                "Except for the fact that my hands weren't seeking warmth on my partner's back, the dance was still the same, which I had already become accustomed to in a couple of minutes."
                "Except that we danced it at the distance I was used to from the camps - and that's not a 'pioneer' distance at all."
                "And I guess that made us stand out from the crowd."
                "All the while I was cowardly averting my eyes, letting my gaze bounce over the pioneers dancing nearby, Miku frozen behind the turntables, Olga Dmitrievna smiling and shaking her head in time with the music..."
                "I saw that there was something wrong. {w}That we weren't dancing right."
                "But I guess it was a little late to overdo it, wasn't it?"
                "Especially since Slavya had already successfully coped with herself and stopped blushing like a poppy."
                "And somewhere she was even beginning to enjoy herself. {w}I don't know. I guess."
                "Because the very next second my ear was scorched with hot breath:"
                sl "Semyon, hello?"
                "It seems that somewhere something has finally checked out, and we're tuned into the same frequency."
                "I, even without being able to see, {i}knew{i} that Slavya was smiling."
                "And her smile is a light-bright one."
                me "Yes?"
                sl "You don't have to be afraid of me."
                th "Ah, yes, there are reasons, you know."
                "Even though I was forcibly forcing myself to relax and not bone up, I was still perceptibly nervous."
                sl "You just have to tell me that it makes you nervous, and I'll back off."
                me "No."
                th "Nervous. {w}But it's not something I'm willing to give up."
                "A second later I felt her head on my shoulder."
                with fade
                "And after a minute and the song was over.{w} But I didn't seem to notice that at all."
                "Slavya was still basking on my chest, a few millimeters farther away than up close."
                "But just enough to feel the beat of life on the other side."
                "It wasn't until now, when I stopped cycling myself, that I realized how fast her heart was beating."
                stop music fadeout 3
                pause(1)
                scene bg ext_square_night_party
                show sl shy dress
                with dissolve
                play ambience ambience_7dl["disco"] fadein 3
                "Quick, quick."
                "The girl bit her lip and looked into my eyes as she pulled away."
                "Again."
                th "When will she ever get tired of embarrassing me?"
                me "Thanks for the dance."
                "I unclasped my hands, forbidding myself to think about what it might mean..."
                "I said, forbidding myself to think!"
                "Miku moved the record."
                show sl normal dress with dspr
                sl "Will you go to the next one?"
                me "We need to survive to see the next one."
                "I answered evasively."
                me "I'm going to go get some air, okay? {w} My head's a mess."
                "Slavya nodded and let me go."
                hide sl with dissolve
                "And I, seeking salvation from a maddened heart and unsolicited thoughts, decided to turn to the primordial force."
                stop ambience fadeout 1
                $ alt_day2_beach_seen = True
                scene bg ext_beach_night
                with dissolve
                play ambience ambience_boat_station_night fadein 3
                "To water."
                play music music_7dl["your_life"] fadein 3
                th "Why does it happen this way?"
                if (counter_sl_7dl == 4) and (counter_sl_cl == 5):
                    "I thought things might have been the beginning of some kind of warm experience, of sympathy."
                    "And me?"
                    th "Am I going crazy?"
                "It's all so strange, almost inexplicable from any point of view."
                "And yet there are."
                "For example, Slavya's almost mystical ability to find me wherever I hide."
                th "Yes, it's certainly no use playing hide-and-seek with her."
                "There was no way I could figure out how it worked."
                "So all I had to do was accept the fact that if I crawled into a far dark corner now, sooner or later the girl would get worried, and..."
                "Right. She'll find me anywhere."
                "The question is whether I want to be found."
                "Or maybe I want this farce to be over, and for the ever-increasingly busy mind-numbing blonde to finally get back to square one."
                "After all, the closer a man gets, the more power you give him over you."
                "He can hit harder than an outsider, scarier than a betrayal."
                "Although betrayal is probably not about Slavya?"
                "Though I've only known her for three days."
                "Who knows what skeletons are out there in the dusty closets?"
                with fade
                "And if I keep sitting here, somebody else is sure to find me."
                "People like to leave the dance to get some air, even if it's an open-air dance."
                "And it draws such young, romantic people..."
                "That's right, where there's a splash of waves and a moonlit path."
                "I imagined Slavya and some abstracted man in a pioneer uniform racing to find me, and I snorted."
                th "What a popular personality."
                dreamgirl "Thinking back on how you were canvassed after dinner - at least one more candidate is sure to be found."
                dreamgirl "How about going back to the dance? It's noisy, but there's no one yanking on the bench."
                "I wondered."
                menu:
                    "Stay on the beach" if counter_sl_cl == 6:
                        $ counter_sl_cl = 7
                        if loki:
                            th "Isn't one single time ever enough?"
                            "Like a moth, I burned myself on the candle so much that I burned almost completely."
                            "And the scarred desire for a miracle, it turns out, didn't die at all."
                            "There it is, the miracle, in a sundress with Ouroboros, smiling blue-eyed, and one cannot help believing in its sincerity and purity."
                        else:
                            "I've been feeling silly all day today, acting silly and thinking only and exclusively silly things."
                            "It's as if I've really turned seventeen again, and the nightlight stays on by the bed until morning, and line after line lays down in straight lines, telling the world why it's beautiful."
                            "A mood of poems, fairy tales, and the obligatory fulfillment of the most cherished wishes."
                            th "The world. You are beautiful."
                            th "Because you have Slavya."
                        "I exhale into the humid night air, listening to the surf beating beneath my feet."
                        "I don't seem to have succeeded in smothering the unnecessary?"
                        th "Also that dance, of course. {w} Of course, Slavya didn't say anything or push me away - though she should have."
                        th "After all, the pioneer distance was invented for a reason."
                        "But her smell, her warmth, her voice."
                        dreamgirl "Gave up and swam?"
                        th "What to do? {w}It's not like there's anywhere else nearby where you can so conveniently escape to on canteen duty."
                        dreamgirl "And you yourself haven't already? No?"
                        "I sighed sorrowfully."
                        "Even though she seems to be the one who's been running after me all three days and coaxing me not to be a boogeyman, it looks like we'll be switching roles very soon."
                        "Unless something happens to save me."
                        dreamgirl "Luck saving throw! Oop!"
                        th "Lucky rescue, where are you? Hello?"
                        "There was a creaking sound of sand under footsteps behind me, and a hand rested on my shoulder."
                        show el normal pioneer with dspr
                        el "Good evenightning."
                        "The cybernetic nodded to me."
                        th "You're the one who's going to help me out!"
                        "I rejoiced, however, hiding a triumphant smile."
                        me "El, buddy! What brings you here?"
                        "The boy raised an eyebrow questioningly - I don't know how to do that - but obediently answered:"
                        el "Remember the conversation after supper?"
                        me "So you needed my help?"
                        "He nodded."
                        me "Then lead the way!"
                        $ alt_day3_technoquest2 = True
                    "Let Slavya find me" if counter_sl_7dl == 4:
                        $ lp_sl += 1
                        $ counter_sl_7dl = 5
                        "Maybe I'll get lucky and her instincts will fail her."
                        "I headed down the beach, trying to leave the noise of the dancing behind me."
                        "I didn't want to be there, I didn't want..."
                        "I was more attracted to be alone with my own thoughts."
                        scene bg ext_boathouse_night
                        with dissolve
                        "My feet led me to the hulking bulk of the debarker that lurked over the black water."
                        "He, too, looked dejected and lonely, and I felt a kind of solidarity for him."
                        me "It's quiet here..."
                        "The gatehouse was dark and blind - whoever was there was either asleep or absent."
                        "Which meant the way was open."
                        "Walking along the pontoons to the building itself, I turned right - there, fenced off by railings, was a narrow path over the water itself, leading to an observation deck."
                        "The building hid me from the shore, which meant that this was where I was going to stay."
                        stop music fadeout 5
                        "I stepped back to the farthest edge and, drawing in the air hard, I finally let go of the tension that had been building up inside."
                        "I exhaled the bitterness and inhaled the past."
                        $ set_mode_nvl()
                        play music music_7dl["exodus"] fadein 3
                        if herc:
                            "My childhood ended strangely and reluctantly."
                            "I'm six, my mother bought me a nice blue school uniform, steamed it and hung it on the hangers in the closet."
                            "She even pinned her old Illyich badge on the lapel."
                            me "What a beauty!"
                            "It's a little big for me, but I like it so much-I put it on, sneak a tie I found among my parents' things, and spend hours spinning in front of the mirror, happy to see how great I look."
                            "Except my mother doesn't look cheerful."
                            "And then my father comes and takes me for a ride on a catamaran, where he tells me that he's found someone he loves, someone he needs."
                            "And it boggles my mind how that's possible."
                            me "And me?"
                            "Pathetically I ask."
                            "Father sips from the uncorked bottle and looks away."
                            nvl clear
                            "I'm ten. Some foreigners took over our school, and it was with their light hand that the computer class was equipped with brand-new Pentiums to replace the outdated 386s."
                            "How everyone was in love with computer science!"
                            "The first 'Quake' network matches, the first victories that inspired me to go to the club."
                            "First humiliation from those who spent the day and night on the DM6."
                            nvl clear
                            "Thirteen years old. For three years I've been sulking at my stepfather for signing me up for the orchestra, so now instead of cartoons at six o'clock I have to go to the Children's and Youth's Art Center and spend hours there playing a tedious half-military repertoire."
                            "And my breath? It's gone completely out of breath."
                            "Steadily, twice a year, chapped lips."
                            "Except we have a city championship, and there are two groups coming from our house - the orchestra and the pop singers."
                            "One girl was lost, and I looked for her for a long, long time, and I found her..."
                            "She was a year older than me, but a little shorter, ugly, big mouth with lipstick glitter, huge eyes lined with black pencil, making the look very expressive."
                            "My heart was ticking, skipping a beat."
                            "And I suddenly realized that maybe what I was doing wasn't so bad, since I could meet people like that."
                            nvl clear
                            "Eighteen years old. Freshman year, first attempt at living on my own."
                            "My stepfather was in the hospital with an 'officer's' disease, so I worked part-time and sent some of the money to my mother, who, on a nervous breakdown, began to give up on her own."
                            "And again the library as a symbol, again the meeting."
                            "Fragile, short, with transparent skin, transparent gray eyes, staring naively when she took off her glasses; catching every word and snuggling with her unfailing 'adore.'"
                            "I used to joke to myself about it - I'm lucky to have blind babes. Apparently, those with normal eyesight can't be interested in me a priori."
                            "And I'm a romantic, I write poetry, and I can see the beautiful things."
                            "But there's less and less of the beautiful every year..."
                            "And then there's that accident, my silly and naive games of Pinkerton, the army, funerals..."
                            "What about that girl?"
                            "I don't even remember her."
                        elif loki:
                            "When you're six years old, life seems simple and straightforward, it's full of bright colors, and you don't see what you don't want to see."
                            "I still firmly believe that I will become a cosmonaut or at least a famous football player."
                            "I shout 'Only Yashin, only Dynamo!' even though I myself, of course, am a fan of the Blue and White Blues."
                            "I have all the chances, right? All of them. I kind of feel where the ball is going and I'm not afraid to fall at all, that's why I take all the shots my father shoots."
                            "I didn't realize then that he was hitting at quarter strength, and my peers didn't know which side to approach the ball from yet."
                            nvl clear
                            "I'm eight, it was the elementary school football championship today, and I was saving the goal as best I could."
                            "I really felt like Yashin! Training with my dad didn't go to waste."
                            "Except that one bounce came back with such terrible pain in my knee that I barely made it to the end of the match."
                            "I was kept on my feet by the hubris and the enthusiastic look in a pair of green eyes."
                            "We lost 2-1, and my father took me to the trauma room, where they put some weird thing on me and forbade me to even go near the ball."
                            voice "Don't you dare whine! You are a man! If you can't do something, try your hand at something else!"
                            voice "You're only eight years old! You can learn anything!"
                            me "Like what?"
                            voice "Anything at all!"
                            "The radio in the kitchen played a horn, and my father nodded in that direction:"
                            voice "At least music! Do you want to sign up tomorrow?"
                            "I wanted to."
                            nvl clear
                            "I'm sixteen, today's my first performance - eight years have not been in vain, I already represent something as a trumpet player."
                            "I also met an old acquaintance of mine in the medical center, where I went for a checkup..."
                            "I slipped her a counter-ticket to the palace at the Anichkov Bridge, and she promised to be there and cheer for me as hard as she could."
                            "Football was forgotten, but I wasn't really interested in it anymore."
                            "I was drawn to what was awakening inside, responding to the call of an instrument, what sometimes spilled out on to the music stand in melodies that only I understood."
                            "I am dressed in a white shirt, black pants, patent leather shoes. And an impenetrable self-confidence."
                            "I look myself in the eye for a few seconds and, after taking a deep breath, walk out of the costume shop."
                            "I'm only interested in first place."
                            nvl clear
                            "Eighteen. Second year at the Conservatory, I've got a great future ahead of me!"
                            "There's a whole world waiting for me, ready to fall at my feet."
                            "I can do anything!"
                            "Everything!"
                            "Unless I go into space... I can't. Well, never mind!"
                            voice "How much longer are you going to hang around the mirror? Let go."
                            "I'm shoved aside before I can trace the platinum, thick cap of hair, from under which I can see only a graceful nose and chubby lips."
                            "It pricked me somewhere that if her eyes were the same as my old friend's, I'd fall in love and get married!"
                            "Her eyes turned out to be blue."
                        else:
                            "Panting and sweating with terror, I climb a wet tree whose branches come close to the cozy yellow rectangle of the window."
                            me "My love is on the fifth floor, almost where the moon is..."
                            "I'm balancing on a branch, but it's scary, eerie, and it's already too high below."
                            "Hugging the branch with my legs, I crawl forward until I'm close, close enough to see a girl sitting at a table with a disproportionately large head in a bandage, leaning over the table and typing something out."
                            "I knock softly, and the girl, shuddering, turns away from the drawing, looks in my direction, huffs, and, jumping up, swings open the window."
                            "Dragging me into the room."
                            voice "You... You're crazy!"
                            me "Yes."
                            "I'm seven, and I've grown terribly attached to this poor girl, become her best friend since her sister."
                            nvl clear
                            "The concert organizers wanted to make me sing with a backing track, they were naive."
                            "I've got a pretty good voice, plenty of hours of practice on wind instruments, which, though I've never been interested in, have done me good, too."
                            "After all, I've always despised those 'veneer' artists who can't pump up the hall with their voice."
                            voice "The performer is Semyon Persunov! The song is 'How Glorious are the Evenings in Russia'!"
                            "I go on stage and disappear."
                            "This song seems to be made for me, for my voice, my cords, my memory."
                            "I remember all the good things in my life, and I put that into singing."
                            "So when I finish, the audience stands, chanting, 'Se-myon! Se-myon!"
                            "My fifteen minutes of fame."
                            "Fifteen minutes in fifteen years."
                            nvl clear
                            "Pride is a mortal sin. I understand that very clearly now."
                            "And it's not that there's someone up there in heaven threatening me with a fist and sending me to hell, no."
                            "It's just that snobbery and arrogance is a real pain in the ass."
                            "When it came time to choose, I left behind music, singing, poetry - everything. I chose LITMO because I found myself very interested in programming, seemed to have an aptitude for it."
                            "At that time, no matter what I was doing, I had an aptitude for everything."
                            "Just don't have a dream the night before about a little brown girl in a short dress."
                            "Our team traveled to foggy Albion, where they defeated their archenemy from Silicon Valley in a tense match."
                            "Except... Why did I decide to take the girl I seem to have been climbing a tree window to all my life? Why? Why...?"
                            "I'm nineteen, and as I look at the metal casting box, I realize that for some reason I don't want anything else. Words have been spoken, tears have been shed, there's no getting back what's been lost."
                            "And it turns out I've missed so much, walking around like a narcissistic peacock..."
                        nvl clear
                        "It only got worse after that. Worse."
                        "Like a slope, I rolled farther and farther away from who I started life with."
                        "Time stretched on, people slowly drifted away, leaving me lonely, unwanted and completely self-sufficient."
                        "Until it all became one endless day, interspersed with wakes and blackouts."
                        stop music fadeout 3
                        $ set_mode_adv()
                        with fade2
                        sl "Relaxing?"
                        show sl normal dress
                        with dissolve
                        play music music_7dl["deep_inside"] fadein 3
                        "Angel? Omnipresent, omnipresent..."
                        sl "Am I interrupting?"
                        me "It's hard to say. Would you mind?"
                        show sl smile dress with dspr
                        sl "You may look like a boor, but I can see that you are not a bad person, Semyon."
                        me "The cock praises the cuckoo."
                        "The river was carrying its black waters slowly past us, and Slavya, gazing, asked as if to herself:"
                        "What is it that oppresses you?"
                        "I was silent."
                        sl "Will you tell me, Semyon?"
                        me "No, I won't."
                        show sl upset dress with dissolve
                        "There is one thought that is very dull in its triviality."
                        "Only one's own can betray. Strangers can't do it."
                        "And the closer I let someone close to me, the more personal questions I answer, the... In short, it's clear without further ado."
                        sl "I can see there's something bothering you, you don't want to relax."
                        me "What bothers me is that what bothers you is what bothers me."
                        "And so on."
                        show sl sad dress with dspr
                        "A quiet sigh, a nod - I definitely upset and discouraged the girl with my rebuke."
                        sl "Why are you so..."
                        me "How?"
                        sl "Rude."
                        me "How else can you do it when you don't understand normal words?"
                        "And it's not that I want to be alone - thank you, I've had my fill."
                        "I just don't want people I've known for a week to get inside me."
                        show sl normal dress with dissolve
                        sl "I couldn't... you know, be like you."
                        "Confessed the girl."
                        me "Neither could I, as a matter of fact."
                        sl "You couldn't?"
                        me "I can't."
                        th "Blind man to deaf man dialogue, damn it."
                        show sl dontlike dress with dspr
                        sl "But you live somehow!"
                        me "Who told you that?"
                        sl "Today I saw you smiling."
                        "Slavya pointed it out to me."
                        sl "And yesterday, too."
                        th "An achievement, no doubt."
                        "If she says something along the lines of 'if you smile, you live,' I'll be totally disappointed in her."
                        sl "And I promised you, remember?"
                        me "That I would smile? I remember."
                        sl "I'm not very good at it yet if the person doesn't help me."
                        sl "But I'm trying very hard!"
                        if (alt_day2_walk == 2) and not herc:
                            sl "Rescuer! That sounds!"
                        else:
                            sl "I think I'm going to work with kids when I grow up."
                        me "And I'm the first test subject, I presume?"
                        show sl upset dress with dspr
                        sl "You're closing up again."
                        me "I don't really like being dissected alive!"
                        "I barked."
                        me "Maybe it's okay for you to have people reach with dirty hands up your skirt, but I'm used to people around me respecting my right to personal space a little bit."
                        show sl happy2 dress with dspr
                        sl "That's right. You'd better get mad. Yell at me if you want to."
                        sl "Just don't shut yourself off again."
                        me "Will you get off?"
                        "I jumped to my feet and staggered toward the pontoons."
                        "And Slavya followed me."
                        me "You can't pry into the soul of a man who hasn't asked you to. It's unfair and, I'm sure, against the law."
                        show sl shy2 dress with dspr
                        sl "But I want to help!"
                        "Slavya kept up with me."
                        me "Do you know where the road is paved with good intentions?"
                        me "Yeah, that's where. In two rows, in little bricks."
                        show sl surprise dress with dspr
                        sl "Where to?"
                        "Slavya asked perplexedly."
                        "I grabbed my head."
                        th "Who did I mess with...?"
                        me "Don't you know that saying?"
                        show sl normal dress with dspr
                        sl "That's the first time I've heard that."
                        me "To hell! The road to hell is paved with good intentions!"
                        "I shuddered."
                        "It suddenly dawned on me that there was silence all around, interspersed only by the splash of water, and I was shouting at the top of my lungs."
                        me "It doesn't matter. {w}Besides, you're not a doctor to help in a qualified way, so you'd better stay out of it. You'll only hurt yourself."
                        me "You're not a doctor, are you?"
                        th "That's it, get out! Go on, then. I can't, have no right to get attached to you."
                        th "I remember all too well how all my attachments end for me as a loser man."
                        me "Not a board-certified psychiatrist capable of highlighting all my cockroaches?"
                        me "Or maybe you're a psychic who can read people's minds?"
                        show sl sad dress with dspr
                        sl "No."
                        "Slavya looked at me seriously."
                        me "Then by what right?"
                        sl "By right of memory."
                        "Uncomprehendingly she answered."
                        me "I thought so. I dare not delay."
                        show sl laugh dress with dspr
                        sl "And you couldn't."
                        "I sighed and tried again, first:"
                        me "Slavya, I'm tired of people and want to be alone. {w}Why can't you leave me alone?"
                        show sl grin dress with dspr
                        sl "Yes, because I'm worried about you, stupid Semyon."
                        th "Stupid. Of course you are."
                        me "And since when does worrying about someone give you rights over that person?"
                        sl "It always has."
                        me "Oh, has it?"
                        sl "Always-always."
                        show sl smile dress close with dissolve
                        "Slavya came closer and took my hand."
                        sl "There's some kind of breakdown in you, a tear."
                        sl "Yes, I'm not a doctor, I'm not an esculapian or a psychic. But I can see that you can be helped just by someone being around you."
                        th "Being around? That only works with people in love."
                        "And we, however we are..."
                        "However, her words created turmoil in my head, sparked a whole cohort of thoughts, one more beautiful than the next."
                        me "You're there for me.{w} How do you help?"
                        show sl smile2 dress close with dspr
                        sl "It's simple. How can't you understand?"
                        sl "You don't keep quiet, you don't withdraw into yourself, and you stop disturbing a wound that is long overdue to heal."
                        me "Sooner or later I'll be alone anyway. You can't piss me off all the time."
                        show sl normal dress close with dspr
                        sl "I can't."
                        "Slavya nodded placidly."
                        sl "But tonight you'll be a little better, a little warmer, you'll go to bed knowing that I'm thinking of you."
                        "The music in the background has finally died down - the disco has come to its logical conclusion."
                        sl "And anyway, isn't it wonderful to know that there's someone besides Mom and Dad who cares about you?"
                        th "It's wonderful, of course it's wonderful. But what if I just woke up right now?"
                        th "Have you thought about that, you obnoxious girl? {w}How would I feel if I became attached to you, and one day I just realized you never existed?"
                        me "Not really."
                        sl "You're just not used to it."
                        sl "But you'll find out for yourself when you just go to sleep - something's changed."
                        sl "And tomorrow you'll wake up a little bit, but a different person."
                        "I'm not so sure of myself."
                        show sl smile2 dress close with dspr
                        sl "I know this because I see you changing."
                        sl "And change is always painful."
                        th "Oh, who better than me to know that."
                        me "You're so smart, aren't you Einstein by any chance?"
                        "I asked wryly."
                        show sl happy dress close with dspr
                        sl "That's what I was talking about. {w}You're kidding. So something's gotten a little better already."
                        sl "Shall we go?"
                        "She held out her hand to me."
                        me "Where to?"
                        sl "I'd like to ask you to dance, but the dance is over."
                        sl "So I guess tomorrow? Time for bed?"
                        show sl smile dress close with dspr
                        sl "Will you walk the girl home?"
                        "And I obediently accepted the palm."
                        stop music fadeout 3
                        stop ambience fadeout 3
                        "I liked Slavya. And me?"
                        "She must have liked me?"
                        scene bg ext_square_night_party2
                        with dissolve
                        play ambience ambience_camp_center_night fadein 6
                        play music music_7dl["ask_you_out"] fadein 3
                        "When we returned to the square, all the pioneers had already dispersed."
                        "It was empty and quiet and lonely."
                        "The light and music lights, for which Sanich had brought some bulbs from town to replace them, were not on."
                        "Didn't hum the speakers, economically wrapped in polythene."
                        "Looks like even without Slavya, the camp can take care of itself."
                        show sl smile dress
                        with dissolve
                        sl "Too bad you left, one dance is very little after all."
                        me "But we talked."
                        show sl laugh dress
                        with dspr
                        sl "Yeah, we chatted alright!{w} I chatted, and you kicked back with all your paws."
                        me "And the tail."
                        sl "And the tail."
                        show sl shy dress
                        with dspr
                        sl "Don't think I'm hitting on you."
                        me "I wasn't."
                        me "I knew right away that I disgusted you."
                        show sl laugh dress
                        with dspr
                        sl "You're inimitable!"
                        scene bg ext_houses_night_7dl with dissolve
                        "Over our conversation we went out into the street, in the far corner of which was Slavya's cabin."
                        show sl normal dress with dissolve
                        sl "You go from extreme to extreme."
                        sl "Are all boys so capricious?"
                        me "No, just me."
                        th "Perhaps it's because I stopped being a boy years ago?"
                        "I suddenly caught the smell coming from my shirt, quite expected for a third day without a shower in the sun."
                        me "Better tell me, how's the washing and laundry here?"
                        me "Olga Dmitrievna gave my things to the laundry, is there a separate day here?"
                        show sl grin dress with dspr
                        sl "Yes, we usually had a bath day on Sundays, you just arrived then, but you ran off somewhere, so you could have washed up from the road."
                        sl "And you can take your clothes to the laundry when they get dirty, they'll wash them all in an hour."
                        me "So I have to walk around like an unwashed pig?"
                        show sl serious dress with dspr
                        sl "No. The bathhouse has been heated for today, really, that's where the girls have to go today, but I can take a seat for you."
                        me "Isn't that too inconvenient?"
                        sl "I'll just wash faster so you have enough time, that's all."
                        sl "Do you know where the bathhouse is?"
                        me "No."
                        "I answered honestly."
                        sl "Good, then listen..."
                    "She won't get me on dances":
                        "After all, I obviously have nothing to catch on with Slavya or anyone else."
                        "And I don't need their sassy pity at all."
                        "Thinking that, I cheered up and hurried up the sandy road."
                        "It won't get any worse than this."
                        "Then it will only get better!"
                stop ambience fadeout 6
                stop music fadeout 3
                return
            else:
                sl "Flatterer!"
                me "Not in the least. I'm telling it like it is - you're the centerpiece of the dance floor."
                dreamgirl "Yeah, and imagine there's nothing under that dress..."
                th "Hussars, shut up."
                show sl happy dress with dissolve
                sl "I didn't think you had it in you."
                "And I haven't whispered in her ear yet..."
                me "What can I do?"
                sl "Ay, don't pretend. I know that when you men do that, it means you want a girl to..."
                "She didn't get to the end of what she thought men might want from a girl before I finally got to her ear and said in a clear voice:"
                me "What are you, young lady, all I want from you is a dance, and that..."
                "Here already I did not finish - the tickling reached my nerve knots, and Slavya laughed, pushing me away a little."
                if alt_day3_sl_invite:
                    me "Actually, I'm a victim of circumstances."
                    me "I came to a strange place, and everyone here is so kind."
                    me "And you're beautiful, too. It doesn't take long to get confused."
                else:
                    sl "The next dance is mine! Wait for it for sure."
            if alt_day2_bf == 'sl':
                $ lp_sl += 1
            "The music ended and we reluctantly let go of our hands."
            hide sl with dissolve
        "Invite Alisa" if (alt_day3_dj == 'dv'):
            call alt_day3_lp_checker(alt_dater = dv)
            if alt_day2_bf == 'sl':
                $ lp_sl -= 1
            $ alt_day3_dancing1 = 'dv_1'
            show dv smile dress at center with dissolve
            "I walked over to the incendiary Aliska and tapped her politely on the shoulder."
            dv "WHAT?!"
            "She shouted cheerfully."
            "I pursed my lips, pretending to say something, and she took off her headphones."
            me "Great, you're no longer attached to that shaitan machine. Let's go."
            "I impatiently held out my hand to her."
            dv "Where to? I've got another program here!"
            me "To dance! I want you to dance with me!"
            "Separately I repeated."
            me "To invite you. Understand?"
            show dv smile dress at center with dissolve
            dv "No!"
            "She abruptly yanked away the palm that I almost - almost! - grabbed."
            me "But why?! Do you feel sorry?"
            "She hid her hands behind her back."
            dv "I don't want to, that's all!"
            me "I disgust you so much that you don't want to dance with me..."
            "I was still finishing the sentence when suddenly it was as if a mirror had been hung in front of me and I was able to look at myself objectively."
            "And quite possibly, by the way, unpleasant."
            "Personally, if I were a girl, I wouldn't dance with myself in my life."
            "But Dvachevskaya shook her head!"
            "So I have a chance?"
            dv "Because I've never danced. Got it?"
            "Clearly she said."
            me "So what's next? Be a girl, after all, let me lead and woo you."
            "She shook her head."
            if counter_un_7dl >= 4:
                dv "Why did you come up? Don't you know who you're supposed to invite?"
                "She looked at me in a way that made me swallow all objections."
            else:
                "We bickered for a few more minutes before the slow jam was over."
                "I made a hurt face, stuck out my lower lip, and glared at the angry Aliska!"
                me "I hope you're at least a little ashamed."
                "I rebuked. And walked away. I'll go call again at the next medley!"
            hide dv with dissolve
        "Dance with nobody":
            $ alt_day3_dancing1 = 'me_1'
            "Music here, is good of course. But I still don't want to dance."
            "What am I, sick, or what?"
            th "Loneliness is everything."
    stop music fadeout 1.5
    pause(1)
    if (alt_day2_date == 'un_fz'):
        scene cg d3_disco_no_un_7dl with dissolve
    else:
        scene cg d3_disco with dissolve
    play music music_list["lightness"] fadein 6
    "The disco was gaining momentum!"
    "With some surprise, I saw cybernetics on the dance floor."
    "What they portrayed could be called a dance with a very big stretch."
    th "They got sick or what?"
    if (alt_day2_date == 'un_fz'):
        "But Lena wasn't there anymore."
    if alt_day3_dj == 'dv':
        "Alisa had discovered her talent as a master of ceremonies, and she was going full throttle, literally glowing with the energy that was overwhelming her!"
        "Just a little more and she'd be dancing herself!"
        "If the song lacked rhythm, she would add it from the next record, adjust the speed where necessary, add the right timbre - in short, she behaved in a way that made me praise myself once again for not overlooking the talent!"
        "I caught her eye and gave her a thumbs up."
        me "You did good!"
        "With one lip I said."
        dv "You're a fool yourself!"
        "That's what she replied."
        "Dvachevskaya is a bitch. But she's great!"
    elif alt_day3_dj == 'mi':
        "Miku acted like she was born with a turntable in her hands. My goodness, what she was doing with it!"
        "I'm not really big on the whole DJ thing, but the obvious things like mashups, like smooth mixing and playing with volume, were done flawlessly with her fingers, creating an added element of showmanship."
        "I didn't expect anything else from the brilliant Japanese girl, though."
        "For a moment she stepped away from the turntables and, holding an earpiece to her right ear, danced around the set."
        "I caught her gaze and held up my thumb."
        me "Good girl!"
        "Without even trying to shout over the speakers, I said. {w}She'll read my lips, I don't doubt her."
        "She winked back at me and went back to her technique."
    "..."
    with fade
    return

label alt_day3_dance_dance2:
    scene anim_square_party with dissolve
    if alt_day3_un_med_help == 1:
        show un smile dress at center with dissolve
        if alt_day_binder != 1:
            $ lp_un += 1
        "Lena touched my shoulder."
        un "Well, shall we go?"
        if herc or loki:
            "She seems to have lost what little courage she had in her back in the afternoon, when she whispered her strange confession in a confused voice."
        "I smiled and nodded."
        hide un with dissolve
        stop music fadeout 3
    elif (alt_day3_us_bugs == 1) and (alt_day3_dancing1 != 'un_fz'):
        stop music fadeout 1.5
        pause(1)
        show us smile dress at center with dissolve
        play music music_7dl["genki"] fadein 3
        "I was still completely at the mercy of a languid evening, when my mood was extremely impolitely spoiled - someone step on my foot."
        "Ulyanka. Who else."
        us "Well, let's do some crimes?"
        "Smiling, she tossed a matchbox in her hand."
        "And I suddenly remembered - what's in there!"
    else:
        "Someone touched my shoulder."
        show el normal pioneer at center with dissolve
        el "Shurik sent me, he said that everything is ready for the decisive breakthrough."
        if alt_day3_technoquest1 >= 1:
            me "Don't sit on my neck. I helped you already."
            "He shrugged."
            el "I'm sorry, but it looks like we can't do without you."
        me "And by decisive breakthrough, you mean I'll have to breakthrough and you'll be idling?"
        "He's a little embarrassed."
        el "Uhh... A little different, but..."
        if (alt_day3_dj == 'mi') or (lp_mi > 7):
            show mi normal dress at cleft with easeinleft
            mi "I'm sorry, boys, but I'm taking Semyon!"
            "Chirped Miku, leading me away."
            "I didn't even have time to object."
            return
        elif (alt_day3_dj == 'dv') and (lp_dv < 9):
            me "Did I find you a DJ? Yes, you did. Isn't that a lot of work for one night?"
            show el sad pioneer with dissolve
            "Electronik looked away in embarrassment. He didn't seem to have any arguments prepared for persuasion."
            me "You can take it from here. I have faith in you."
            hide el with dissolve
            "Syroezhkin left, and I sat down on the bench, waiting for another slow jam."
        else:
            menu:
                "Help them":
                    if alt_day3_dj == 'dv':
                        $ alt_day3_technoquest2 = True
                        show el normal pioneer at cleft
                        show dv normal dress far at cright
                        with dissolve
                        "I looked back at Alisa, who was deftly turning over another record in her hands. Her face was..."
                        th "Spirited?"
                        "It was hard to explain, but there was an unparalleled sense of rightness about what was happening. It was as if something had been wrong all along, and now..."
                        "Now Alisa was in her rightful place."
                        th "I don't want to help these knuckleheads at all. But that nasty girl, why not?"
                        show el smile pioneer at cleft with dissolve
                        hide dv with dissolve
                        "I nodded, causing a slight look of bewilderment on Electronik's face."
                        me "All right, lead the way."
                        show dv smile dress far at cright with dspr
                        "As I glanced around the dance floor one last time, my eyes met Alisa's."
                        show dv soft_smile dress far at cright with dissolve
                        $ alt_pause(0.5)
                        show dv smile dress far at cright with dissolve
                        extend " She winked at me and immediately went back to her Walkman."
                        hide dv with dissolve
                        th "I think I'm doing everything correctly."
                        stop music fadeout 3
                        scene bg ext_clubs_night
                        show sh normal pioneer at cleft
                        with dissolve
                        play ambience ambience_camp_center_night fadein 3
                        "Outside the clubhouse, Electronik left me and Shurik on the porch, ducking inside. Since I had absolutely no idea what to talk about with the future luminary of Soviet science, I had no choice but to sit on the porch, my face contemplative."
                        "A ladder leaning against the roof was already at the ready."
                        if herc:
                            th "It looks sturdy, it'll hold my carcass for sure."
                            th "But is the surface flat enough so that it won't go sideways at the most interesting point?"
                        else:
                            "The mere thought of climbing up a loose and narrow ladder gave me a bad feeling inside."
                        th "I get the impression that all the inhabitants of this camp are conspiring to ruin me!"
                        show el normal pioneer at cright with dissolve
                        "Electronik came flying out of the club, almost tripping over me. He was clutching a green canvas bag in his hands."
                        el "The tools are here."
                        "Clumsily, he reported, handing me the equipment, {w}and with a sigh I rose from the stairs."
                        show el think2 pioneer at cright with dissolve
                        el "Please don't drop anything. At the end of the shift we'll have to pay for underdelivering..."
                        me "I know, I know."
                        "I brushed it off."
                        me "But how am I going to carry it? In my teeth?"
                        show el serious pioneer at cright with dissolve
                        el "There's a carbine there, you can hook it on your belt."
                        show el normal pioneer at cright with dissolve
                        el "We'll hold the ladder, don't worry!"
                        th "I wish I had your optimism."
                        "I thought enviously."
                        th "You've got a good thing going on - you've got solutions for every situation in life, and you'll stay on the ground too!"
                        "I clicked my carbine. There was less and less desire to climb to the roof."
                        show sh serious pioneer at cleft with dspr
                        "Meanwhile, the cyberneticists have already taken their positions by the stairs."
                        dreamgirl "Don't drift, buddy!"
                        dreamgirl "Even if you spend the rest of your shift in the infirmary with a broken spine, you'll be doing it to good music."
                        th "Well, thank you!"
                        th "Now I'm definitely not going anywhere!"
                        "But there was nothing to do - I had already called myself a shroom, so all I had to do was climb in. In my case, though, the basket was the less and less secure roof of the clubhouse."
                        play music music_list["you_lost_me"] fadein 3
                        hide el
                        hide sh
                        with dissolve
                        "I stepped cautiously up the stairs. Even in the low light, I could see the whiteness of Syroezhkin's knuckles, and that was the least bit reassuring."
                        th "What is the phenomenon called when one subscribes to frankly dubious schemes because of a desire to please one rarely harmful woman?"
                        dreamgirl "Cherchez la femme?"
                        th "Exactly."
                        "By some miracle I climbed up and clung to the rough slate with my hands."
                        th "And if tomorrow Aliska says she's changed her mind, her red head will be off her shoulders!"
                        "Pulling myself up, I finally put my foot on the slate. The sole of my sandal immediately slipped treacherously downward, making my heart crumble in my heels."
                        el "Everything alright?"
                        "Barely suppressing the urge to swear at him with a three-story swear word, I blurted back:"
                        me "Completely!"
                        el "Then move to the auditory window, there must be a cable somewhere!"
                        "That's easy to say, move! I couldn't even move."
                        if herc:
                            "It was a little better than lying in a foxhole, but that's the thing, a little."
                        elif loki:
                            "Sure, there have been situations in my life where the blood in my veins has literally mutated into stone, but that doesn't make it one bit easier."
                        else:
                            "I've probably never been so scared - one wrong move, and..."
                        "But I had to continue what I'd started - there were no more stairs under my feet, which meant there was only one way to go. Up."
                        "As soon as I reached the roof ridge and grasped it tightly, my body regained its mobility. The stupor was gone, though I was a little dizzy-I'd barely been breathing the whole time."
                        el "What is it?"
                        "Electronik's impatient shout literally urged me to accidentally drop a tool or two on his head. But that would require letting go of the horse, and I wasn't yet prepared to take such risks for moral satisfaction."
                        "Slowly treading on the slate, I moved toward said skylight along the roof."
                        me "I see the cables!"
                        el "Great!"
                        "Electronik came to life, apparently already frightened that I had fallen asleep."
                        el "Now find the antenna and see what's wrong with it."
                        "I didn't risk taking out the flashlight, so all I had to do was squint and hope that my body would turn off my night vision under stress."
                        "And, to my pleasant surprise, my eyes accustomed to the darkness fairly quickly fished out an antenna stretching along the ridge. The cause of the malfunction was discovered even more quickly - a thick looking branch lying right on top of the cables in the middle of the roof."
                        me "Hey you down there!"
                        th "Landlubbers, I almost added."
                        me "Watch out, a branch is about to fly at you!"
                        "Of course, you could have dodged it and flung it over to the other side, but its current location coincided remarkably well with the desire to nail those two. I moved across the roof again - this time much more confidently."
                        play sound sfx_hiding_in_bush
                        "A little sleight of hand and the branch flew down,"
                        play sound sfx_bus_window_hit
                        extend " rumbling down the slates. The thought that my carcass could have been in its place made me dizzy again."
                        sh "Ow!"
                        th "Did it not occur to those knuckleheads to step back?"
                        "I examined the antenna for damage. I couldn't say that even with a set of the Cybernetics club's best tools it was within my competence to fix anything, but it was still worth assessing the damage."
                        "And the cause of the breakdown was ridiculously simple-a fallen branch had ripped out a plug, quite serviceable at first glance."
                        th "Nothing bad would happen if I put it back, would it?"
                        "Without waiting for my schizophrenia to kick in, I plugged the plug back in. I didn't get an electric shock, which was a good thing - it had gotten pretty damp in here by evening."
                        "After tugging the plug to be sure, I nodded in satisfaction."
                        me "Hold the ladder!"
                        el "Have you made it yet?"
                        me "Did the best I could."
                        sh "Shall we check it out first?"
                        th "No way!"
                        th "Get me down to the ground, and then check whatever you want!"
                        "I didn't want to die heroically. The only thing I wanted was to set my feet on solid ground and go straight to the square, where I would get my well-deserved reward: a dance with a hottie. And maybe I'll even get a whole kiss..."
                        me "I'm coming down!"
                        "I stated unequivocally, letting go of the visor. My heart went down again - no one said it would be easy, of course, but my knees trembled a lot more than they had half an hour earlier."
                        "Just don't look down... just don't look down... just don't..."
                        "When I felt only air beneath my foot, I dug my fingers into the slate with all my might."
                        me "Damn it..."
                        el "Left!"
                        play sound sfx_hiding_in_bush
                        "The stairs swayed slightly under my sharp lunge."
                        th "I hope you cry on my grave, you redhead..."
                        "It was only by grasping the top of the stairs that I remembered how to breathe."
                        th "Another incredible quest passed. And it's at least level eighty!"
                        show sh normal pioneer at cright with dissolve
                        show el normal pioneer at cleft with dissolve
                        play sound sfx_uliana_jumps_down
                        "I jumped to the ground, shaking off my soiled palms. The cyberneticists let go of the unfortunate ladder with visible relief."
                        el "Shurik, turn on the radio. Let's see if it works."
                        hide sh with dissolve
                        "The boy nodded confusedly and moved toward the porch. I sat down tiredly on the grass."
                        th "If it doesn't work now, at least send the gym teacher tomorrow!"
                        th "Or Slavya - she's always on the spot."
                        dreamgirl "And what about your chivalrrrrrous desire to give a girl a dream?"
                        th "Or maybe it's not her dream at all. What if she's dreaming of a bouquet of daisies?"
                        play sound sfx_7dl["phone_feedback"] fadein 0
                        "The reproducer on the roof hummed sharply, making me cringe. Electronik, on the other hand, glowed."
                        show el smile pioneer at cleft
                        el "It works!"
                        th "As if no one noticed!"
                        "The noise stopped, and Shurik peeked out of the club."
                        show sh normal pioneer far at cright with dissolve
                        sh "Good."
                        "I got up off the ground."
                        me "Well, if that's all for today's errands..."
                        show el grin pioneer at cleft with dissolve
                        el "Thank you so much! We couldn't have done it without you."
                        "He didn't throw his arms around me, thanks for that. I nodded back."

                        me "I think I'll go and dance. So long."
                        "And I walked hurriedly toward the square."
                        scene anim_square_party with dissolve
                        play music music_list["raindrops"] fadein 3
                        $ alt_pause(2)
                        show mt smile dress far with dissolve
                        mt "Thank you all, it was a wonderful evening!"
                        if (alt_day3_dancing1 == 'dv_1'):
                            "Olga was broadcasting into the microphone as I almost squeezed through to the turntables."
                        show mt normal dress far with dissolve
                        mt "Announcing the last dance!"
                        hide mt with dissolve
                        th "Medley?"
                        "I thought hopefully. It would be just the perfect ending to my heroic evening!"
                        "But Random only chuckled in response to my aspirations, and from the speakers came the upbeat beats of another dance song - too mediocre to identify."
                        th "All right, redhead, today's your lucky day."
                        th "But I'm not getting off that easy!"
                        show dv normal dress at cright with dspr
                        "Alisa was busily stacking the records, glancing occasionally at the player. She had enough charge for an entire disco, and she wisely alternated between the wonder device and the records she was used to."
                        show mi normal dress at cleft with dspr
                        "Miku was fidgeting beside her, already clutching a stack of records in her hands. She noticed me first."
                        show mi smile dress at cleft with dissolve
                        mi "Semyon, where have you been all this time? You gave such a wonderful thing to Alisa, with such music, didn't you want to listen to it yourself?"
                        th "Of course I did. But they forgot to ask me..."
                        me "I was fixing the radio."
                        show dv smile dress at cright with dissolve
                        "The redhead arched an eyebrow incredulously."
                        dv "So what, I'm a staff camp DJ now?"
                        me "Well, if you want to make way for someone else..."
                        show mi scared dress at cleft with dissolve
                        "Miku instantly waved her arms - too actively, in my opinion."
                        show mi grin dress at cleft with dissolve
                        mi "No, no, I still have a lot to do at the club, and I have to get ready for the concert! Only Alisa can do it, she's so good at it, you should see her!"
                        me "I didn't doubt that for a second."
                        show dv surprise dress at cright with dissolve
                        "Alisa was embarrassed under our questioning stares."
                        dv "And what are you staring at me for?"
                        show dv soft_smile dress at cright with dissolve
                        "She made an impenetrable face, carefully pretending not to understand our hints."
                        th "But what hints were there? We're telling her straight out that we want her and only her as a DJ!"
                        hide dv
                        hide mi
                        with dissolve2
                        stop music fadeout 3
                        $ alt_pause(1)
                        play music music_7dl["lonesome_shepherd"] fadein 3
                        "The track ended, and Alisa turned off the equipment. The crowd on the dance floor whirred indignantly, not wanting to go to the sidelines."
                        th "The ball is over, the Cinderellas are off to turn into pumpkins. And Alisa..."
                        if lp_dv < 11:
                            "And she was on her way to me."
                            show dv normal dress with dissolve
                            dv "Here you go."
                            "In my palm, she slipped the Walkman. I was confused, my mouth hanging open stupidly."
                            me "But I gave it to you!"
                            show dv dontlike dress with dissolve
                            "The girl crinkled nervously."
                            dv "Come on! That thing must not be cheap."
                            dv "And why would I need it without an amplifier?"
                            th "But... but..."
                            me "That'll come in handy for the broadcasts!"
                            "With poorly concealed despair in my voice, I exclaimed."
                            show dv normal dress with dissolve
                            dv "I don't want to sit in the radio room for the rest of my shift. {w=1}Today was interesting, of course, but every day like this..."
                            "She shook her bangs and clapped me on the shoulder." with vpunch
                            dv "In short, someone else will be found for sure. So long."
                            hide dv with dissolve
                            "And Alisa walked away, leaving me completely broken and miserable, with a stupid Walkman in my hands."
                            th "And it was my own fault. I imagined things..."
                            th "Who knew I'd only imagined the sympathy from Alisa?"
                            th "She didn't ask me to crawl on the roof and fix the radio, after all!"
                            "Putting the Walkman in my pocket, I staggered doomfully back to the cabin. I didn't want to stay in the square, where everything reminded me of my shameful defeat."
                        else:
                            "And she had already picked up the last stack of records and moved to follow the departing Miku. I froze, not wanting to let her go just yet."
                            if (alt_day3_dancing1 == 'dv_1'):
                                th "After all, she owes me a dance."
                            me "Redhead!"
                            show dv normal dress with dissolve
                            "Alisa turned around. I opened my mouth to say something, but the words stubbornly failed to come to mind."
                            "In desperation, I slipped my hand into my pocket."
                            me "Here."
                            show dv shocked dress with dissolve
                            "The girl squinted in disbelief at the headphones I held out."
                            dv "Why do I need them?"
                            me "This player doesn't have a speaker."
                            show dv surprise dress with dissolve
                            dv "What?"
                            me "Music, I say, won't play without them!"
                            "With her chin on the records, Alisa took a clump of wires from my palm and slipped it into her pocket."
                            show dv shy dress with dissolve
                            dv "Thank you."
                            th "Was it just me, or was there something like embarrassment on her face?"
                            hide dv with dissolve
                            "Deciding that was the end of our dialogue, she hurried to catch up with Miku. I shoved my hands in my pockets and followed her with a glance."
                            "Never before have I so much as wanted a man to just listen to music. {i}My{/i} music."
                            th "It's only natural to be happy when your tastes match up with someone you like."
                            "And somehow I was sure that she and I would be the same."
                            show sl normal dress with dissolve
                            sl "Semyon?"
                            th "It seems that the quests are not over for today..."
                            "The speakers stood orphaned in the middle of the square, and hinted with all their appearance that it would be a good idea to remove them."
                            "After pondering my escape plan for a second, I sighed heavily and turned to the activist."
                            sl "Where did you get so messed up?"
                            me "I was running an important party errand."
                            "From the corner of my eye, I assessed the damage done to my shirt during the mission - even in the darkness you could see the rich gray, almost black stripes."
                            show sl smile dress
                            sl "You could use a bath. We've got a heated sauna today!"
                            th "That's a good idea!"
                            th "Otherwise I won't be able to get away from any assignments - they'll find me by smell."
                            sl "Should I take get you a place in the queue?"
                            show sl smile2 dress with dissolve
                            "I nodded cheerfully, and Slavya smiled."
                            sl "From the cabin you follow the path toward the second gate, there will be the bathhouse. You won't miss it."
                            hide sl with dissolve
                            "With these words we went our separate ways."
                            th "I wonder if Alisa will go to the baths."
                            dreamgirl "Do you want to whip her with a broom for all the wrongs she's done?"
                            th "Yeah. And pour a bucket of water on her head!"
                            "Although the thought of being in the bathhouse with the redhead made me need a ladle of water myself."
                            th "What a bastard! I can't even think about her!"
                            "With a deep sigh, I went to the cabin to get a towel."
                    else:
                        if alt_day3_dancing1 == 'sl_1':
                            if (counter_sl_cl >= 2):
                                $ lp_sl += 1
                            sl "Good decision."
                            show sl smile dress at right with moveinright
                            "Smiled a stealthily approaching Slavya."
                            sl "You make me respect you!"
                            th "I'm going to regret this..."
                        me "That's enough. Let's go."
                        $ alt_day3_technoquest2 = True
                    stop music fadeout 3
                "Stay":
                    if (alt_day3_dancing1 == 'un_fz'):
                        hide el with dissolve
                        "Electronik left upset, and I sat down on the bench."
                        "Fast dancing never worked for me."
                        "And the only girl with whom I wanted to dance slow dances ran away in tears."
                        "Sighing and considering the options, I got up and trudged after the cybernetics."
                        "My path lay in the direction of the clubs."
                        th "At least I'll be in business."
                        $ alt_day3_technoquest2 = True
                    elif alt_day3_dj == 'dv':
                        me "Did I find you a DJ? I did. Isn't that a lot of work for one night?"
                        show el sad pioneer with dissolve
                        "Electronik looked away in embarrassment. He didn't seem to have any arguments prepared for persuasion."
                        me "You can take it from here. I have faith in you."
                        hide el with dissolve
                        "Syroezhkin left, and I sat down on the bench, waiting for another slow jam."
                    else:
                        $ girls_list = ('dv', 'un', 'mi', 'sl')
                        $ lp_max = max( [eval('lp_'+w) for w in girls_list] )
                        $ max_who = [w for w in girls_list if eval('lp_'+w) == lp_max]
                        $ max_who_id = max_who[0] if lp_max > 5 and len(max_who)==1 else 'nobody'
                        call expression 'alt_day3_max_lp_{}'.format(max_who_id)
        if not alt_day3_technoquest2:
            scene anim_square_party with dissolve
            "Soon, the fast music was again replaced by a plucking of the strings, and the people around began to look at each other in search of a dance partner."
            "And, of course, I also decided not to deny myself the pleasure of cuddling a girl to romantic music."
    with fade
    return

label alt_day3_max_lp_dv:
    "I looked him over."
    me "You're kind of weird. Go already."
    show el sad pioneer with dspr
    el "But you..."
    "Boy protested."
    me "Go, I said. Find another fool."
    $ alt_day3_lp_route = 3
    stop music fadeout 3
    with fade
    return

label alt_day3_max_lp_un:
    show un normal dress at right with dspr
    me "Actually, I was going to invite Lena..."
    "I hesitated, watching her make her way over to me."
    un "Go."
    "She seemed to catch the end of the conversation."
    me "Really?"
    show un smile dress at right with dspr
    un "Of course."
    "She smiled."
    un "Still have work to do in the infirmary."
    $ alt_day3_lp_route = 1
    "I sighed and agreed with her."
    me "You got it."
    "I nodded to Electronik."
    me "Lead the way, wherever you were going."
    $ alt_day3_technoquest2 = True
    stop music fadeout 3
    with fade
    return

label alt_day3_max_lp_mi:
    me "I've still got to dance with Miku tonight."
    $ alt_day3_lp_route = 4
    stop music fadeout 3
    with fade
    return

label alt_day3_max_lp_sl:
    me "No way, I still have to dance with Slavya."
    $ alt_day3_lp_route = 2
    show sl sad dress at left with moveinleft
    sl "Semyon! How can you say that!"
    sl "I had a much better opinion of you, and you don't want to help your comrades!"
    me "But what about our dance... {w}What's the matter, are they burning?"
    show sl serious dress with dspr
    sl "Semyon!"
    me "Okay, okay, Mom, I'm sorry, I'm on my way."
    $ alt_day3_technoquest2 = True
    stop music fadeout 3
    with fade
    return

label alt_day3_max_lp_nobody:
    me "I'll dance, I guess."
    stop music fadeout 3
    with fade
    return

label alt_day3_choose2:
    scene anim_square_party with dissolve
    play music music_list["raindrops"] fadein 3
    if ((alt_day3_dj == 'mi') or (lp_mi > 7)):
        jump alt_day3_miku_dance_2
    if alt_day3_dj == 'dv':
        call alt_day3_lp_checker(alt_dater = dv)
        $ alt_day3_dancing2 = 'dv_2'
        th "Now I won't let Dvachevskaya get away from me!"
        scene cg d3_dv_alice_dj80_7dl with dissolve
        "After avoiding the awkwardly stomping pioneers on the dance floor, I went straight to the DJ booth. {w}Alisa was fiddling with a record, obviously getting ready to play the next track."
        scene anim_square_party with dissolve
        show dv normal dress far at center with dspr
        me "Gotcha!"
        show dv smile dress at center with dspr
        "She hummed, looking up at me."
        dv "Well, what are you doing here?"
        "I looked up with a picture of my eyes."
        me "What do you mean what? To dance with you, madam!"
        "The corner of the girl's lip twitched grudgingly."
        show dv dontlike dress with dissolve
        dv "I won't dance! How many times can you stick it to me?"
        me "What's it to you, is it pathetic?"
        "I could tell by the look on her face that the jokes were over. She didn't want to dance, and she wasn't going to."
        "And in a good way I should have raised the white flag and politely bowed my way out, but..."
        th "If I backed out now, I would fall forever in her eyes. How could I ever talk to her after such a shameful backpedal?"
        "Alisa left me no choice."
        th "It's hit or miss!"
        if herc:
            me "Why are you breaking down? Let's go, I said!"
        elif loki:
            me "Who are you trying to fool? I can see in your eyes that you want to!"
        else:
            me "Let's go already, Alis!"
        show dv angry dress with dspr
        "I grabbed her hand and pulled her along. I certainly didn't expect that..."
        show dv angry dress close with dissolve
        stop music
        play sound sfx_7dl["window_glass_break"]
        with flash_red
        "...that I'm going to get hit in the head in no time!"
        play music music_list["awakening_power"] fadein 2
        show dv rage dress with dissolve
        "Shards of vinyl rattled softly on the concrete. I jerked back, letting go of an equally dumbfounded Alisa."
        show dv rage dress at cright with dissolve
        "She was breathing heavily and staring at me with undisguised anger, still clutching the shard of record in her hand. {w}The curious pioneers stopped dancing as they watched the show unfold before their eyes."
        show mt angry dress far at cleft with dissolve
        show mt angry dress at cleft with dissolve
        "In the meantime, an enraged Olga Dmitrievna was already rushing toward us."
        show mt rage dress at cleft with dissolve
        mt "Dvachevskaya!"
        show mt angry dress at cleft with dissolve
        "She hissed, shoving me aside."
        show mt rage dress at cleft with dissolve
        mt "What the hell have you done here?"
        show mt angry dress at cleft with dissolve
        "Alisa threw another unpleasant look in my direction."
        show dv angry dress at cright with dissolve
        dv "Nothing. I'm having a disco, don't you see?"
        show mt rage dress at cleft with dissolve
        mt "You don't do disco anymore! How do you handle the equipment?"
        show mt angry dress at cleft with dissolve
        mt "Get out of here!"
        hide dv with moveoutright
        "After muttering something unprintable through her teeth, Alisa tossed the shard of vinyl on the ground with force and turned around, heading sharply away from the square. She didn't look back, though I stared after her."
        th "What a shame! What a shame!"
        "I wanted to be in the place of that wretched record the girl had smashed on my head. Just to be blown to pieces, so I wouldn't have to feel that shame."
        th "And why did I even go to her? To make myself look like a tough guy?"
        th "You did, good for you!"
        th "Gave a girl something she liked to do, and then took it away from her. What could be better than that?"
        show mt normal dress at center with dissolve
        "Olga gently pushed me away, getting behind the turntables."
        mt "And we'll talk to you afterwards!"
        "I read her murderous whisper on my lips."
        hide mt with dissolve
        "I turned around to walk away in shame, but the squad leader called out to me again."
        show mt normal dress at center with dissolve
        mt "Semyon! Get your toy."
        "She nodded at the Walkman, lying orphaned next to the stack of records."
        mt "It might get lost again."
        "After everything that happened, I didn't even want to look at it. It was, after all, my gift to Alisa..."
        "Except she wouldn't accept it now."
        "Once again cursing myself for my idiocy and my self-confidence, I slipped the player into my pocket and staggered to the nearest bench. All I had to do was wait for the fucking disco to end."
        hide mt with dissolve
        $ lp_dv = lp_dv//2
        stop music fadeout 3
        with fade
        return
    menu:
        "Dance with Alisa" if alt_day3_dancing2 != 'dv_0':
            call alt_day3_lp_checker(alt_dater = dv)
            $ alt_day3_dancing2 = 'dv_0'
            "Alisa never came. It looks like I'll either have to look for another candidate, or sit alone."
            jump alt_day3_choose2
        "Dance with Slavya" if not ((counter_sl_7dl == 4) or (counter_sl_cl == 6)) and (lp_sl >= 12):
            call alt_day3_lp_checker(alt_dater = sl)
            if alt_day3_dancing1 == 'sl_1':
                $ alt_day3_dancing2 = 'sl_12'
            else:
                $ alt_day3_dancing2 = 'sl_2'
            if (counter_sl_cl == 2):
                "A string has been strung between us."
                "A mystery, even a bitter one, may bring people together - or it may divide them."
                "But I cherish the hope that I did not dislike Slavya completely."
                "For it was with her that I confronted her in the very middle of the dance floor, smothering the remnants of indecision."
                "This dance is rightfully mine."
                sl "Lost the girl, pretty boy?"
                "There was a mocking voice over my shoulder."
                show sl normal dress at center with dissolve
                if alt_day3_dancing1 == 'sl_1':
                    "She was still wearing the same dress as our last dance. But it sat on her... Different?"
                    "Maybe it was crumpled, maybe it was the hot, wet body that made it look like a glove-but it was hard to look away."
                me "I lost the person I wanted to dance with."
                sl "How could you do that?"
                "Her eyes reflected the light of the spotlights and the color music, but under the damp veil you could see pain, participation, and even some hint of tenderness."
                "The eye apart from facial expression can express anything. It is enough just to give up the inner monologue, to stop thinking in separate words and switch to emotion."
                me "It wasn't my fault."
                "I seriously said, extending my hand to her in an inviting gesture."
                me "I was looking for a person, and I found a goddess."
                "An unearthly laugh - to goosebumps and a skipping motor kick - was my answer."
                scene cg d3_sl_dance
                with dissolve
            else:
                "Slavya doesn't seem to mind dancing. Though I probably wouldn't have had the heart to ask her this time."
                "But then it just so happened that she came up herself."
                show sl smile dress at center with dissolve
                sl "Shall we dance?"
                me "Shall we dance?"
                "We said it at the same time and laughed at the same time."
                "Unbeknownst to me, the jitters that had plagued me for the past two hours receded, leaving me with a sense of music and an unconcealed interest from this sweet girl with huge blue eyes."
                me "What?"
                with dissolve
                "She looked up questioningly, all of herself somewhere else."
                "And her dress is so... So. It somehow manages to hang on some thin rope, and having our height difference, you can see the most interesting angles."
                "She shrugged."
                sl "That's okay."
                me "Are you sure?"
                sl "Absolutely."
                me "Did I do something wrong?"
                "She laughed."
                sl "Stop it. That's my personal problem, there's no way it's your fault there."
                "I nodded in agreement, and for the rest of the dance we danced in silence."
            hide sl with dissolve
        "Dance with Miku" if (alt_day2_mi_date != 2) or alt_day3_dv_dj_fale:
            label alt_day3_miku_dance_2:
            call alt_day3_lp_checker(alt_dater = mi)
            scene anim_square_party:
            if alt_day3_dancing1 == 'mi_1':
                $ alt_day3_dancing2 = 'mi_12'
            else:
                $ alt_day3_dancing2 = 'mi_2'
            if alt_day3_dj == 'mi':
                show mi serious dress with dissolve
                me "Dancing with the most beautiful DJ on the planet - isn't that charming?"
                mi "I think you're the pretty one."
                show mi smile dress with dspr
                mi "And a flatterer."
                mi "It's just a matter of guessing what you're trying to accomplish."
                mi "There's an idiom, I don't know how it's Russian. When a boy invites a girl to the hot springs."
                "I get it."
                me "We call it a super intimate relationship."
                me "Intimate."
                if counter_mi_7dl == 2:
                    scene cg d3_mi_dance_afar_bordo_7dl
                else:
                    scene cg d3_mi_dance_afar_7dl
                with dissolve2
                mi "How intimate?"
                "She snuggled up close."
                mi "Like this?"
                "And smiled slyly at the way my breath caught."
            else:
                show mi serious dress with dissolve
                "To tell you the truth, I was very much afraid that Miku would turn me down. She seemed distracted and upset."
                "She perked up, though, as soon as my hands wrapped around her waist."
                mi "Put your palm a little higher, please."
                show mi normal dress with dissolve
                "She smiled contentedly."
                mi "Yes, right this way. Thank you."
                "On the very spot where all white people usually have their bra clasp."
                "Its absence raised fair questions, and the thought suddenly crossed my mind that there was a girl dancing with me now with nothing under her clothes."
                "She moved her hip, cutting off the doubt."
                if counter_mi_7dl == 2:
                    scene cg d3_mi_dance_close_bordo_7dl
                else:
                    scene cg d3_mi_dance_close_7dl
                with dissolve2
                "Fine!"
                "If she was going to make fun of poor me, she did a great job of it!"
                "I tried three times to collect my courage, cleared my throat, and otherwise tried to get over my stupor."
                if alt_day2_convoy in ('dv', 'sl', 'un'):
                    "Oh, how I was jealous of that creep from my dream last night!"
                    "With his determination, he'd feel right at home here."
            if counter_mi_7dl == 2:
                scene cg d3_mi_dance_afar_bordo_7dl
            else:
                scene cg d3_mi_dance_afar_7dl
            with dissolve
            "A dance is like a conversation."
            "We get to know each other differently-some just need a fleeting glance, a twitch of the pupil, or a raised eyebrow - all those micro-gesture - to approach and smile."
            "Some need something more tangible-at the very least, to introduce themselves, to shake hands, to exchange scent markers."
            "Well, for young people, there's always a dance."
            "There are two or four layers of clothing between us, even if one partner is in a nude dress, but the distance is a distance of heat, and I breathe out at the same time as her, hearts beat in the same rhythm, and even thoughts converge."
            "It is not without reason that they say that dancing couples are much stronger than romantic couples, for it is easier for them to align themselves to the familiar and childhood favorite rhythm of the tango than to try to maneuver in the stormy sea of mutual incomprehension."
            "I know that Japan has completely its own dances, which are nothing like ours."
            "I know that putting anything under a kimono is a sign of bad taste."
            "Miku adapted very quickly to our realities and took great pleasure in the fact that she had not been inculcated with the corkiness of a Soviet child, who until the age of eighteen sanctimoniously considered the friendship of organisms something to be ashamed of."
            if dr:
                "{i}I met one such open-minded person simply through the Internet. In one of the chat rooms, spinning in the background a stream of endless hellos, while I was typing another sheet of text, suddenly a nickname stabbed me in the eye.{/i}"
                "{i}Sterlet.{/i}"
                "{i}It sounded so obscene that I couldn't stand it, laughed - switched to the tab.{/i}"
                "{i}And yes - this nickname really had nothing to do with fish, it was a synthesis of 'bitch' and... I see, in short.{/i}"
                "{i}Then a New Year's Eve exchange of phone numbers, and an invitation to go out.{/i}"
                "{i}And I couldn't think of anything smarter than to ask her to the disco.{/i}"
                "{i}And that was it, I simply disappeared for several endless hours-from the moment I met her from the escalator at Narvskaya until the morning when she very reluctantly let go of my hand.{/i}"
                "{i}She wasn't tall - about Miku's height - but favored a short braid with a razor-sharp bottom cut, blue-black hair, a pupil that seemed to occupy the entire iris, and an exotic eye shape.{/i}"
                "{i}I remember her gait, a bit of a crawl when she was thinking or embarrassed about something, or a skip when she was in a light-hearted mood.{/i}"
                "{i}And so a fidgeting kid comes up to me, unmistakably recognizing me from the crowd, slips his hand and tells me her name - «Ryoko».{/i}"
                "{i}In the first few hours we didn't say a couple of words to each other - and at the same time we told each other many times more than a word would ever be able to tell.{/i}"
                "{i}Me, trying to come to my senses, her, trying to figure out what the big guy wanted from her in the first place... We chatted incessantly in the Internet, constantly finding new topics for conversation.{/i}"
                "{i}In fact, after splitting up in the morning, we met in the messenger window the same evening and chatted again until dawn, washing each other's bones and laughing about the silly, awkward date. {/i}"
                "{i}It took me a couple of months to get over her stupid way of sticking honorifics to my name - although, it would seem, having studied photography in Russia, she could have gotten used to our forms of address a long time ago. Semyon-san, come to think of it.{/i}"
                "{i}Needless to say, we decided to give each other another chance?{/i}"
                "{i}March was over, April had begun, and Ryoko was freezing outside Lenexpo, clutching a ticket with a half-faded stamp in her pocket to an exhibition of traditional Japanese interior design. {w}Meanwhile, I was being taken away by ambulance with a fever of forty.{/i}"
                "{i}At the end of May we switched places, and this time we got lucky.{/i}"
                "Miku was silent, almost purring, smiling enigmatically and looking in a way that took your breath away, pulling you into the sea of those laughing eyes."
                "She was so close that she could rub her cheek against her cheek like a real cat herself - and several times she took advantage of the opportunity."
                "{i}I intercepted her right after her discharge and took her to Peterhof for City Day, where our fragile friendship went to waste - after all, it's so hard to resist and not kiss a girl when she's exposed to the fountain and trembling in her arms, trying to keep warm.{/i}"
                "{i}Our first one. Until now, I had assumed it was silly, cardboard, and just a touch of skin. What mystery could there be in some trivial kiss, I beg you.{/i}"
                "{i}Our first intimacy - and again, instead of the expected mindless entanglement of bodies, aimed only at orgasm, something incomprehensible turned out... And exciting.{/i}"
                "{i}Although we both tacitly decided that we liked kissing much better. That's who we were, strange people.{/i}"
            mi "What's on your mind, Senechka?"
            "I whispered to Miku."
            me "It's hard to say... Probably about how you're too pretty and I'm too stupid."
            if dr:
                "{i}By my birthday, Ryoko was nineteen and in her final year.{/i}"
                "{i}The decade was coming to an end, another financial drama was brewing in Asia, and we were saying goodbye, and we couldn't get enough of it before we said goodbye.{/i}"
                "{i}It's true what they say: you can't breathe before you die. {w}We promised to keep in touch and not let go of each other's fingers, and she even cried softly somewhere, though she didn't show it to me.{/i}"
                "{i}And left.{/i}"
                "{i}We actually wrote and called every day, hung on the line for hours, paid some wild phone bills, before we discovered Internet telephony.{/i}"
                "{i}Ryoko smiled into the webcam, waved at me, sent me pictures of the city, and demanded the same from me in return.{/i}"
                "{i}We didn't keep our promise.{/i}"
            mi "What nonsense you say, Senechka. You're not stupid!"
            mi "You're very clever and very handsome."
            me "That doesn't make me smart..."
            "I would have spread my hands if they weren't hugging a Japanese girl."
            if dr:
                "{i}At first we started limiting communication.{/i}"
                "{i}Then stopped get in touch every week.{/i}"
                "{i}And, little by little, we stopped communicating at all. That's it - quietly and modestly, without any pretensions or arguments.{/i}"
                "{i}Why that happened, I don't know.{/i}"
                "{i}But it's only thanks to Ryoko that I give meaning to the most ordinary dance far more than anyone else does.{/i}"
            scene cg d6_dance_alt_7dl with flash
            "I thought it was amazing how relaxed she was - her upbringing, after all, means a lot at that age."
            "But still, she was in too much of a hurry."
            "So I politely led her to the bench and hurriedly took my leave."
            if dr:
                "The memories that came back buried the whole mood."
            "Maybe tomorrow... If she doesn't mind."
            if (alt_day2_date == 'mi') and (alt_day2_mi_date != 3):
                "Desperate Miku. I hope she's really desperate enough not to see my behavior as a lack of interest."
            else:
                "And here... Here's her completely inexplicable determination in her actions..."
            "It's as if she knows something that gives her the determination and strength to go over the asphalt roller in the shortest way possible."
            dreamgirl "Why, don't you like the fact that this time it's you and not you who's getting paddled?"
            dreamgirl "Try to relax and enjoy it."
            th "Like I have a choice."
            dreamgirl "There's always a choice. You can just chill out like you usually do."
            dreamgirl "Just think hard - what do you really want?"
        "Dance with Lena" if (alt_day3_dancing2 != 'un_0') and (alt_day2_date != 'un_fz'):
            if (herc or loki):
                call alt_day3_lp_checker(alt_dater = un)
                if alt_day3_dancing1 == 'un_1':
                    $ alt_day3_dancing2 = 'un_12'
                else:
                    $ alt_day3_dancing2 = 'un_2'
                if lp_un >= 5:
                    show un shy dress with dissolve
                    "She spent the whole beginning of the dance thinking about something, then glancing at her watch."
                    me "I may not be the smartest person on earth, but you're clearly expecting something."
                    un "More like late."
                    me "Where to?"
                    if alt_day3_un_med_help == 0:
                        un "You see, Viola asked me to help her do something in the infirmary."
                        un "I don't dance anyway, so I agreed."
                    elif alt_day3_un_med_help == 2:
                        un "You refused to help at the infirmary, so I have to work there."
                        un "Alone."
                    scene cg d3_un_dance with dissolve
                    "She threw me a quick, furtive look."
                    un "And here you are."
                    me "What about me?"
                    un "Dancing."
                    "Her voice went completely blank, so I had to read the word on my lips."
                    "I smiled."
                    me "I can only speak for myself. But I'm doing something I really like tonight."
                    me "If it wasn't you - the pleasure wouldn't be half as much."
                    "She was embarrassed and, not knowing where to put her eyes, covered them."
                    "The smile on her lips, however, was the most contented."
                else:
                    "For the whole dance she was silent."
                    "I was silent, too - at first not knowing what to say."
                    "And then-as I gasped at her trusting gesture-she laid her head on my shoulder at one of the turns and sighed so happily."
                    "I can only speak for myself, but I think that was the moment when all explanation and words would have been superfluous."
                    "To my light handshake she responded with her own."
                    "And from a 'pioneer' distance she took a step forward, being so close that our nervous systems seemed to have become one."
                    "At any rate, the slight jitters we had were one for two-that I know for a fact."
                    "And instead of the cold night air, I suddenly inhaled her scent-a tart one, with faintly sweet notes coming from her hair."
                    "The smell of clean-washed skin that had just warmed up from being active."
                    "Something that excites and drives lovers all over the world - if, of course, they've had time to shower before they get directly to the action."
                    "I can't guarantee anything, though - my knowledge on this subject is mostly purely theoretical."
                hide un with dissolve
            elif alt_day3_dancing1 == 'un_1':
                $ alt_day3_dancing2 = 'un_0'
                "I thought about inviting Lena again, but no matter how I looked for her, I couldn't find her anywhere. Nowhere."
                "Is she gone already?"
                "I had to resign myself to looking for someone else."
                jump alt_day3_choose2
            else:
                $ alt_day3_dancing2 = 'un_0'
                "I thought about dancing with Lena, but she's gone somewhere."
                "My luck, my luck."
                "I had to resign myself to looking for another candidate."
                jump alt_day3_choose2
        "Dance with nobody":
            $ alt_day3_dancing2 = 'me_2'
            "This time Slavya gave me the most promising look. Then she got up and walked over to me."
            show sl smile dress with dissolve
            sl "Come on, let's dance?"
            "She held out her hand to me."
            if counter_sl_7dl >= 4:
                me "I wouldn't mind, but my head is buzzing for some reason."
                show sl serious dress with dspr
                sl "Maybe see a doctor? Violetta Cernovna was around here somewhere."
                me "No, I'll just sit, it will pass by itself."
                me "Because of the music, I guess."
                show sl normal dress with dspr
                sl "I understand."
                sl "Well, I won't interfere. {w}You know where to find me if you change your mind."
                "Waving goodbye to me, the girl left."
                hide sl with dissolve
            else:
                "I shook my head."
                me "Nope."
                sl "But why?"
                me "Not why."
                "I clearly answered."
                me "I don't want to, that's all."
                "She turned away and left."
                hide sl with easeoutleft
                "Looks like she's offended."
                th "Holy-Holy-what a grief..."
                "I said to myself in the voice of brownie Kuzya."
            "Having defended the sacred right to the opportunity to hide in a dark corner, I immediately took advantage of it."
            "The problem with any freaking dance is that the kids don't want to hear the music."
            "They want to LISTEN to it. And for this they need at least a kilowatt of output power."
            "And with that kind of power, even the aforementioned problems with bass delivery ceased to be such."
            "Hiding from the local rural folklore would not have been possible even under three pillows with blankets."
            "Because the basses got you even there."
            "Painted with oil - Semyon is sitting in a house, holding on to a square head, and a self-tapping screw, from some «Free bird» from early Makarevich, is screwing in from above."
            if alt_day3_dj == 'dv':
                "Although Alisa's taste wasn't bad, and she was playing some pretty decent stuff on the sly, you couldn't get a hundred percent of the rotation with my playlist."
                "I caught her gaze and pointedly told her to release the device - I needed it."
                "After an evening of torment I need catharsis, which means there's no getting around Marilyn Manson."
            elif alt_day3_dj == 'mi':
                "The hope was for Miku to at least bring something sane back from Japan."
                "Not in vain."
                "I somehow didn't notice that there was no tape recorder on the host's table, which meant that all the dancing came entirely from records. And a girl like Miku wouldn't have filled her luggage with vinyl."
            "There was a bitter lump in my throat, as always, when they try to forcibly put me in the crowd."
            "I, damn it, am not a strain, to painlessly infect!"
            "I do not want to and will actively oppose."
            "Finally the nightmare ended and the squad leader looked at me with meaningful look."
            show mt smile dress far with dissolve
            mt "It was a great evening, thanks to the host!"
            "She was glowing with pleasure."
            if (alt_day2_date != 'mt'):
                th "What a mare."
                th "Parted."
            mt "The last slow dance is announced. The white dance."
            mt "Ladies invite gentlemen."
            show mt normal dress far with dspr
            "Holy s..."
            "I have planned Genda as my last hope."
            "I'll hide behind him and wait it out. Offending Slavya again is not in my plans - maybe it, suddenly, didn't reach her last time."
            mt "Semyon, don't run away. You will dance with me."
            th "Did she announce this to the whole camp?!"
            "She put the microphone aside and, like an icebreaker through hummocks, headed in my direction!"
            "Mother! Mother! Mother!"
            dreamgirl "That's what called «smoothly flushed», huh?"
            show mt normal dress with dissolve
            "She came up to me and, taking me by the shoulder, turned to the dance floor."
            mt "Let's go... Semyon."
            mt "You wouldn't say no to a girl, would you?"
            if alt_uvao_active:
                call alt_day3_uvao_ch3
                pause(1)
                if alt_day3_uvao_spotted:
                    return
            scene cg d3_mt_dance_7dl with dissolve2
            mt "Especially after all that has happened."
            th "WHAT HAPPENED?"
            me "I remind you that it was you who moved me into your cottage."
            me "It's not my fault I fell out of bed this morning."
            mt "Syom..."
            mt "Don't make a fool out of me."
            mt "I can see your reactions. And I remember everything."
            mt "But if you want to keep playing the innocent pioneer..."
            "She lightly snagged her claws on my ribs, and the sweet tickle made me jerk all over."
            mt "I like this game, too."
            dreamgirl "Wow, that's the erogenous zone I didn't know about!"
            dreamgirl "How does she know?!"
            th "Do I know?!"
            if (alt_day2_date == 'mt'):
                mt "Are you arguing with your inner goon?"
                "I could barely catch my jaw, and she laughed."
                mt "You always have that funny divergence in your pupils at times like that, like you can't see me anymore."
                mt "But you're right, if I do what I want now, it's going to be hard to maintain my reputation as the perfect leader."
            else:
                mt "Just don't yell at the whole camp again about how your squad leader is hitting on you."
                mt "You never know..."
            scene anim_square_party
            show mt smile dress
            with dissolve
            "The dance was over, and I hurried away from the wild leader."
            mt "Semyon, what's wrong? Semyon?"
            show mt shocked dress with dissolve
            "Then she seemed to get it, as she groaned and pressed her palm to her mouth."
            mt "So you don't remember anything?! Really?"
            mt "And I'm coming to you with revelations. Nightmaaaaare!"
            if (alt_day2_date == 'mt'):
                show mt smile dress with dissolve
                mt "That's okay, you'll remember soon enough."
                mt "By the way, thank you for your help last night."
                "Touching my cheek with her lips, she dissolved among the dancers."
            else:
                "She was embarrassed and hurried to disappear into the screaming crowd."
            hide mt with dissolve
            "Yeah... A squad leader with her cool stories and screaming pioneer morons."
            "What a delightful combination."
            "Before the evening became even more languid, I hurriedly turned around and hid in my own cabin."
    stop music fadeout 3
    with fade
    return

label alt_day3_disco_past_d2:
    scene anim_square_party with dissolve
    play music music_7dl["lonesome_shepherd"] fadein 3
    "The disco was coming to a smooth end."
    if (alt_day3_dancing2 != 'dv_2'):
        "What I can say for sure is that it was a success!"
        "No, I may not have been the best dancer or anything like that."
        "But I - all of a sudden - loved it!"
        "In a way I haven't in a long time."
        "Did I really manage to get away from that adulthood and boredom when you don't know why you're going to the dance floor?"
        "I'd like to believe so. At least for the time I'm here."
    if alt_day3_dj == 'mi':
        "Miku didn't let me down. I believed in this girl from the first moment I met her, and she's lived up to that trust."
        "I hope that one day I will find a plastic CD case on the counter, decorated with an image of a miniature girl with strange-colored hair, arranged in two ponytails."
        "And it says, 'Master Mix by Miku.'"
    "Last chords played, and Olga took the microphone:"
    scene anim_square_party
    show mt smile dress
    with dissolve
    mt "Thank to the host, thank you all for a wonderful evening!"
    "She didn't hide her pleasure."
    mt "I hope it won't be the last."
    mt "And on that note I announce..."
    show mt normal dress with dissolve
    "Everyone buzzed offendedly, and Olga laughed."
    mt "Alright, alright. The last dance. And then there's an lights-out for Sovyonok."
    hide mt with dissolve
    "Everyone yelled, and I was surprised to find that I had added my jubilant voice to the chorus of other voices."
    if (alt_day3_dancing2 != 'dv_2'):
        "We danced our last dance like it really was the last dance of our lives."
        "The acclimatization went well. I became part of the camp."
        "Part of these strange people who believe in a brighter tomorrow and in each other."
    "I'll never be like that. But at least I can join their ranks."
    "And root for them of the bench."
    "Slavya stopped nearby."
    show sl normal dress with dissolve
    sl "You don't dance."
    "I nodded."
    me "I suddenly realized how far away I am from all of you."
    me "And how much I envy you all."
    "I smiled absently at her, shaking my head to the beat."
    show sl smile dress
    sl "Oh, I completely forgot."
    sl "They heated the bathhouse. If you want, I can take queue for you."
    sl "Are you going to bathe?"
    me "Of course! Thank you so much!"
    sl "That's good. When you get ready, ask Olga Dmitrievna, she will explain how to get there."
    hide sl with dissolve
    "She smiled and melted into the darkness."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_technoquest3:
    scene bg ext_clubs_night with dissolve
    play ambience ambience_camp_center_night fadein 3
    show el normal pioneer at cleft
    show sh normal pioneer at cright
    with dissolve
    if (counter_sl_cl == 7) and (alt_day3_dancing1 == 'sl_1'):
        "Electronik led me down a short path to the clubhouse, where a friend of his was already crumpling on the porch."
    else:
        "Both cyberneticists were already standing at the door, waiting for their personal messiah. Me."
        "Both, however, flinched in sync as I stepped out of the darkness into the illuminated sector in front of the porch."
    me "This must be something very important."
    me "If you're pulling a man away from a dance, there must be a good reason."
    if (counter_sl_cl == 7) and (alt_day3_dancing1 == 'sl_1'):
        "About the fact that they essentially saved me from unnecessary worries, I did not inform them: a true master is devoid of pride."
    else:
        "I didn't tell them that I'd been more of a drag at the dance, waiting for all that strange dancing to strange music to end."
        "There's no need for them to know."
    me "Okay, gentlemen, where do we start?"
    show el smile pioneer at cleft
    show sh surprise pioneer at cright
    with dissolve
    "Electronik poked his friend in the side with his elbow:"
    el "I told you he'd come!"
    "Shurik looked surprised, to say the least."
    if alt_day3_technoquest1 >= 1:
        "Apparently, he thought that after I cleaned their pantry for them, I'd send them away for a long time."
        "And he wasn't too far from the truth."
        if alt_day3_technoquest1 == 2:
            "Backroom... Ladder... Now to climb the roof."
            "The apotheosis of caring for two helpless pioneers will only be the immediate adoption of one of them."
        "I had no idea what or where it went wrong or how it happened, but it looks like I do have an extremely definite reputation at camp."
        "Which makes one half of the camp quietly despise me, like Dvachevskaya, for instance."
        "And the other half wants to sit on my neck and hang down. And that's where we get to the goddamn theorists."
    show sh normal pioneer with dspr
    me "So are you going to outline my work site, or are we going to chat on the porch?"
    el "On the roof."
    me "Yeah."
    if alt_day3_technoquest1 == 2:
        me "Guys, one question."
        me "I didn't have time to ask this afternoon, I was running."
        me "Don't you have an attic or another exit to the roof that you're making me run with a ladder?"
        sh "Actually, there really aren't any other exits."
    else:
        me "And there's no chance of doing everything from the attic, of course."
        sh "No. But we got a ladder."
        if herc:
            sh "Can you help me put the ladder up?"
            th "Oh, yeah, sure. Help me put up the ladder for myself."
            th "I should probably be thankful that they didn't make me do it myself."
            th "Alone."
            "Panting and sweating, we lifted the heavy wooden ladder and put it on the roof."
            sh "Well, good luck."
        else:
            "He went to the club and pulled out a lightweight aluminum stepladder."
            sh "Here."
            "He put up the ladder and made an inviting gesture."
    me "What, just like that?"
    "I didn't hide my horror."
    me "What if I fall down there in the dark?!"
    show el grin pioneer at cleft with dspr
    el "You won't. There are two lanterns to light everything."
    me "Why didn't you smartasses go up there yourselves?"
    "Both of us looked at each other, and kept silent."
    th "Looks like they're really afraid of heights. Or there's a hornet's nest. Or... I don't know."
    el "Wait a minute."
    "Electronik handed me a green canvas purse with something rattling in it."
    show el smile pioneer at cleft with dspr
    show sh normal pioneer at cright with dspr
    me "And what's in there?"
    "I wasn't even going to look inside. An unnecessary object on a ladder is fraught with the risk of flying off it."
    if alt_day3_technoquest1 >= 1:
        me "All the junk we swept out of the closet today?"
    else:
        me "Something that wouldn't help if I decided to be a hero?"
    show el normal pioneer at cleft with dspr
    el "There are tools in there! Screwdrivers and wrenches and stuff if you need them."
    me "And where should I put it?"
    show el upset pioneer at cleft with dspr
    el "So that's uhh... attach it to the belt, there's a carbine."
    show sh upset pioneer at cright with dspr
    sh "And try not to lose them up there. This is the best we've found."
    "Oh, how I wanted to send them up there themselves. To keep an eye on their own junk!"
    me "Don't worry, I won't lose it."
    "I gritted my teeth and took the first step, testing the ladder for strength."
    show el serious pioneer at cleft with dspr
    el "I'll hold you up!"
    if alt_day3_technoquest1 >= 1:
        me "Are you strong enough?"
        el "It's a ladder. Enough!"
        "He stood next to me, grabbing the ladder with both hands."
    "A little stability really can't hurt."
    me "Can you at least tell me roughly what's up there?"
    sh "Unknown. The transmitter is directly in the attic, so it's unlikely to be damaged. The rest we'll have to look at."
    show sh serious pioneer at cright with dspr
    sh "Good luck."
    play music music_list["you_lost_me"] fadein 3
    me "Here we go, with a prayer."
    "I took the second step."
    dreamgirl "Good luck. I wish you don't snap your neck for some unknown good."
    th "If only there were more sensible alternatives."
    th "Maybe Slavya. Slavya would have no problem with that."
    if (counter_sl_cl >= 5):
        dreamgirl "Where's she going to go, you fool? {w}I'll give you a hint, she didn't climb up on the stool in the camp leader's office because she wasn't afraid to show you her underwear."
        dreamgirl "If you'd drooled a little less and observed the situation, you'd have realized that the girl had a phobia."
        dreamgirl "Fear of heights, panic attacks."
    dreamgirl "So you're a hero. Yes. {w}You'll be lying all broken and in a cast, but the camp will have its own radio."
    dreamgirl "And who knows - maybe you'll get lucky, and Slavya will even stop by to say, 'Thanks, you're a real friend.'"
    dreamgirl "FriendЪ! Not a weenie."
    "So in this now familiar mode of internal dialogue, I didn't notice I took the third and fourth steps-so much so that my hands could have grabbed the roof by now."
    hide el
    hide sh
    with dissolve
    me "I hope it's really worth it."
    el "It's worth it, of course! We'll have our own radio! Isn't it exciting?"
    me "Very."
    play sound sfx_hiding_in_bush
    "The ladder went sideways somewhere, rattled against the steel..."
    "And I clung to the edge, barking:"
    me "Hey, you hooker-hands! Hold the ladder properly!"
    "My legs suddenly felt like cotton and my heart was pounding somewhere in my throat."
    el "Shurik, get to on the other side!"
    "Shurik seemed to obey his friend, because the balance that had been lost was restored."
    sh "I got it!"
    me "'It won't be hard,' they said."
    if alt_day3_technoquest1 >= 1:
        extend " 'Just cleaning out the backroom,' they said."
    else:
        extend " 'Just to get the radio up and running,' they said."
    "If I throw up in fear now, it will all end up on the two idiots below."
    "After calming my heartbeat a little, I took another step, and..."
    "Hooked on the roof! Climbed!"
    "I sat down right on the wet iron and breathed deeply and deeply for a few seconds, coping with my fear."
    "Oh, this fucking extreme."
    el "Semyon, how are you?!"
    me "Safe and s..."
    "I swallowed."
    me "Sound. You don't have to hold the ladder yet."
    sh "We're down here if you need anything!"
    "If - what? All I need now is to switch places with someone."
    "Finally I got over the body shaking and got up very carefully."
    me "Where do I go?"
    el "To that slope! There's an auditory window there, and there should be a cable running from it."
    "Very timely information, thank you."
    "Slipping up by the second, I moved upward, lingered a little at the roof ridge, looking for the aforementioned window, and headed up there."
    "There really was an abundance of cables."
    "They were laid in a sort of crude sort of conduit, a thick bundle of them going under the window, but covering the whole empty space, so that there was no fear of flooding in a rainstorm."
    "It took a while to find the antenna, but I managed that task as well."
    "I traced its direction with my eyes and noticed that about midway up the roof it was pinned by a thick, dry branch."
    me "Just don't fall over, just don't fall over."
    "I preferred to walk on the ridge - at least here I could react and sit down quickly. Especially since you can reach the crash site from here, too."
    "Swinging the branch, I pushed it aside."
    me "Look out!"
    play sound sfx_hiding_in_bush
    "With a tinny rustle the branch drove across the roof and went off into the darkness"
    play sound sfx_bus_window_hit
    extend " where it rattled and hit the ground."
    "From the looks of it, it's weight was enough to just rip the plug out of the socket."
    "Nothing hard, didn't even need tools."
    "I lifted the plug off the roof and, driving it into the socket, wiggled it around a bit, testing it."
    me "Folks, go check it out! Is it working?"
    el "Now!"
    "There was a stomping sound underfoot,"
    play sound sfx_open_door_clubs fadein 0
    play sound sfx_7dl["phone_feedback"] fadein 0
    extend " the rumble of the slammed door..."
    "The nearest tinny loudspeaker suddenly blew, and I almost toppled right over from where I was sitting."
    me "Are you trying to cripple me? You can't scare me like that!"
    "There was a stomping sound beneath my feet again, and the darkness in Electronik's voice echoed:"
    el "Everything works, Semyon, thank you! You can come down."
    th "Aha. Now for the fun part."
    stop music fadeout 3
    "Trying not to think about how I was going to descend, I staggered toward the stairs."
    "However, providence had already taken care of the descent."
    "Under my foot a dark blur flashed an unnoticed leaf. Slippery from the evening dew."
    "And before I could even be frightened, I splashed awkwardly, losing what little balance I had left."
    scene bg ext_clubs_night:
        zoom 1.75 xalign 0.5 yalign 0.15
        linear 10.0 zoom 1.0 xalign 0.5 yalign 0.45
    play sound sfx_7dl["mpbt"]
    with flash
    "Time froze."
    "I didn't have time to be surprised or frightened. I didn't even have time to exhale."
    "I just watched the edge of the roof move away from me."
    if herc:
        "I didn't have time to react or relax in anticipation of the blow."
    play sound sfx_chair_fall
    with flash_red
    scene black
    "The earth blew the spirit out of me."
    pause(1)
    pause(3)
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_mt_scare:
    scene anim_square_party
    show us smile dress
    with dissolve
    us "Ready for revenge for years of oppression?"
    "I burst out laughing."
    me "What do we need to do, narodovolec?"
    us "I need her to take the box."
    us "There was an idea to do a slow dance with lights, but only Alisa has a lighter."
    me "What if you give her something to set fire to?"
    us "Candles on the cake? I ate the last yesterday, haven't heard of any new ones since."
    "I thought about it."
    me "Alternatively, you can just leave it somewhere in a conspicuous place - where the squad leader will definitely find it!"
    me "On the plinth of Genda, for example."
    me "Or in the toilets on the windowsill - there is a hundred percent hit. But then half the people will not see the show."
    "We thought a little more and came to the conclusion that, indeed, the best option would be to just leave it on an open space."
    "But how can we make sure that it is not intercepted by someone before us?"
    me "Seems like I'll have to put myself in front."
    "Her eyes shone."
    show us laugh dress with dspr
    us "Thanks you!"
    "I shrugged and took the match box."
    hide us with dissolve
    "Now the most important thing is to make the face more serious. Harder."
    "The slow dance comes in handy too. Let her think that the young pioneer wants to invite the squad leader and quietly conduct a comparative quick analysis of her topology with the topologies of the other girls."
    "I walked past the monument to Genda, accidentally leaving match box there - the menacing rustle from there significantly reduced in intensity, but was still audible."
    "I went to the squad leader."
    show mt smile dress at center with dissolve
    play music music_list["eternal_longing"] fadein 5
    me "Dancing, Olga Dmitrievna?"
    "She silently extended her hand to me, and while moving to the center of the dance floor, accompanied by an approving whistle and hooting, I involuntarily reacted quite expectedly - straighten the last third of the spine, shoulders and back."
    "As a result, the seemingly large squad leader turned out to be slightly shorter than me, and I could see her crown with a funny «asterisk» twisted clockwise."
    th "Identifies the owner as lazy but adventurous, as long as they are not too dangerous."
    th "I wonder if she'll find this prank dangerous?"
    "I allowed myself a smile and leaned into the squad leader's ear."
    me "Olga Dmitrievna, is it true that fireworks are planned for this evening?"
    show mt smile dress with dissolve
    mt "Not true. Again, probably, Ulyanka got firecrackers somewhere and wants to do it legally."
    me "Oh this Ulyanka."
    "I sighed, not to say that it was completely feigned. Unlike the red dirty trick, I personally now risked a lot - including the integrity of my sanity. When such forms are found under the forearms, enclosed in the most elastic content... "
    "The head involuntarily begins to work in a slightly different mode. And the idea of ​​​​that, ahem... to amuse the owner of those forms with such an extravagant method, does not seem so good anymore."
    stop music fadeout 4
    dreamgirl "Syoma, exhale and relax your buttocks. It's a hormones tricking you."
    me "So, what she was doing there at the monument with a matchbox was not sanctioned by anyone?"
    play music music_list["eat_some_trouble"] fadein 2
    mt "Matchbox?! Damn it. Last time, she and Alisa failed to make gunpowder because the sulfur was bad. And if they have it now..."
    hide mt with dissolve
    "She, not listening to my protests that the dance should be finished, immediately took off my hands and quickly walked towards the pedestal."
    "I grinned widely, catching Ulyanka's eye and sticking out my thumb."
    "After fifteen seconds, a girl's scream was heard in the night... smoothly turning into a scream of hatred."
    mt " {b}ULYANAAAAAAAAA!!!{/b}"
    show us grin dress with dissolve
    us "What are you waiting for? Run!"
    "And we ran!"
    hide us with moveoutright
    stop ambience
    "We ran as if we were being chased by all the demons with the Satan at their head."
    "However, given the strength of the squad leader's anger, the threat could hardly be considered less."
    "I slipped several times on the evening dew and almost earned myself an asphalt disease - saved myself at the cost of shrugged palms and a shirt smeared with grass."
    scene bg ext_boathouse_night with dissolve
    play ambience ambience_boat_station_night fadein 3
    play sound sfx_7dl["breath"] fadein 9
    "Jumping onto the pier, I stopped, taking a breath."
    "Ulyanka was already jumping off somewhere in the dark, and I wandered along the walkways to the far corner of the pontoons - I chose this place on the first day."
    "For a while I stood alone, calming my breath and relaxing, and then the boards behind me creaked, betraying someone's steps, and someone's voice said:"
    stop sound fadeout 4
    voice "Having «fun» again."
    "Judging by the tone, it was a statement, not a question."
    th "What can you do. Such is the mudflow."
    "I shrugged my shoulders without making a sound."
    voice "Okay, Ulyanka is a darling - she's supposed to be so because of her age."
    voice "But you, Semyon. You're an adult boy."
    "The intonations were familiar, but they didn't fit the voice."
    "I turned around."
    show sl smile dress with dissolve
    me "Slavya."
    "She nodded."
    sl "Unlike Olga Dmitrievna, I know exactly where to look for you."
    "She said it with such a hint that I couldn't help but feel embarrassed."
    me "You were looking for me?"
    sl "It's not like... I just saw you slipped a few times. I thought that if you don't need medical help, then a bath at least."
    me "Bathhouse? What an interesting thought!"
    "She smiled."
    sl "Yes. Because the showers are broken, there is nowhere to wash well, except to swim all the time."
    sl "So are you going?"
    "I nodded."
    sl "Very well, then I'll hold your turn for a while. Go get ready."
    sl "From the house you will go along the path towards the second gate, there will be a bathhouse. Don't miss it."
    "She waved to me and ran away."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_med_un:
    play ambience ambience_camp_center_night fadein 3
    play music music_list["goodbye_home_shores"] fadein 3
    scene bg ext_aidpost_night with dissolve
    "After a few promising looks from Slavya, I realized that the nearest white dance would be my benefit."
    "And I didn't want to dance with anyone but Lena."
    "So her reminder even made me kind of happy."
    dreamgirl "The pioneer Semyon had fallen in with the hungry females and is absolutely in demand."
    dreamgirl "So, Semyon, do you feel like an alpha?"
    "Actually, I'm more than enough attention from just one girl... The others at this point are just annoying for some reason."
    dreamgirl "Really? And I've got information from your adrenal glands - they claim you're lying."
    th "I'm lying?!"
    dreamgirl "You bet you are."
    dreamgirl "The sorority girl has bigger boobs, the Japanese girl has such a sag at the back - you can tell right away that she'll prefer the rodeo pose to all the others."
    dreamgirl "Dvachevskaya's figure is the standard of fitness, remember her musculature?"
    th "What's boobs and figure got to do with it, you lustful bitch?"
    dreamgirl "That's because those girls are more promising in terms of producing offspring. Do you get it?"
    dreamgirl "And this slut has nothing but romance. But that seems to be enough for you, you're drooling down to your belly."
    dreamgirl "Get it together!"
    "I shuddered and followed the advice of my inner voice."
    "Especially since we're almost there."
    scene bg ext_aidpost_night
    with dissolve
    play ambience ambience_camp_center_night fadein 3
    "The squat infirmary building was barely lit in the dark, and only the fact that I'd been here a few times before kept me from bumping into a corner."
    "That, and the fact that Lena caught my arm at the last moment, saved me from getting hurt again."
    "She seemed to see much better in the dark than I did, so I slowly turned around and said,"
    me "Tell you what. You go first. I certainly enjoy the role of protector and all that, but not when I can't see anything."
    "She chuckled discreetly, and I went for the sound."
    scene black with fade
    play sound sfx_open_door_2
    "Something clicked a few times in front of me-apparently the key was turning, and then the daylight bulb flared up with a quiet hum."
    "At last I can look around!"
    scene bg int_aidpost_night with flash
    $ persistent.sprite_time = "day"
    play ambience ambience_medstation_inside_night fadein 3
    show un normal dress at center with dissolve
    if 'medic' in list_voyage_7dl:
        "Right from the entrance, I cast a glance at the file cabinet-table that Viola had been working at the last time I came in."
    else:
        "Straight from the entrance I cast my gaze to the chart table."
    "Did she say something about the top left-hand drawer?"
    "About some kind of headache remedy?"
    if alt_day_binder == 1:
        "I suddenly remembered exactly what was in the box."
        "Miku opened it, and there's..."
        "I suppressed a chuckle."
    else:
        "But I don't have a headache! And then it didn't."
        "Okay, first things first, everything else later."
        "Lena, too, seemed to remember the nurse's words, but she didn't insist and, judging by the questioning look, left the initiative to me."
    th "Well, then, let's get to work."
    me "So where do we start?"
    "She silently pointed to a whole pile of boxes, randomly stacked on the other side of the medical screen."
    "Yeah... When it came to help, I assumed a somewhat more modest amount of work."
    me "And... where to?"
    un "Probably to the closet."
    "She pointed to the previously unnoticed medicine cabinet."
    "I found it hard to believe that the contents of a dozen large boxes at once could fit into such a small cabinet."
    "But Lena seemed to have a better view."
    "Not the first time, huh?"
    show un smile dress with dspr
    "She smiled and nodded silently."
    me "Let's go!"
    "She held out a piece of paper and pen to me, but I defiantly folded my arms across my chest:"
    me "You're going to be the scribbling part. With my terrible handwriting, I'll ruin it."
    "She hesitated for a second, as if she didn't really trust me on such things, and then nodded."
    "I suppose she believed in my powers? Eh, I wish I could do the same now!"
    show un normal dress with dspr
    "I gutted the boxes, pulled out the contents-all these sterile packages of bandages, absorbent cotton and gauze, some ampoules, the ubiquitous band-aid, a whole box of brilliant green, and the same amount of iodine."
    th "It is clear that pioneers get asphalt sickness more often than constipation, but where does such a quantity go!"
    "The iodine described could have painted all my acquaintances in two coats ... and there would still be leftovers for silly things."
    "Lena would write out the records in the inventory book and tell me where to scatter what had already been described."
    "The lion's share of all medical junk was nestled in the depths of the cupboard, which was bottomless!"
    "The work was proceeding apace, and I began to realize that had we worked separately, we would not have completed the present volume by midnight."
    th "Violetta Cernovna seems to know something that I do not."
    un "Semyon..."
    show un normal dress with dspr
    me "Yes?"
    "I got a little distracted from the monotonous process and smiled at Lena."
    "The girl was in no hurry to answer. Instead, she stared into my eyes somehow very seriously, as if deciding something for herself."
    th "After what she told me at the warehouse, it's too late to decide anything. Everything is already decided!"
    "I'm here. Isn't it hard to guess?"
    show un shy dress with dspr
    un "What are we going to do when we're done?"
    "I threw a glance at the clock - there was still plenty of time before lights out, the whole contingent is in the square now, trying to break through the concrete with their heels."
    "And that means we're all alone with her!"
    show un normal dress with dspr
    me "I don't know."
    "I shrugged."
    me "Any requests?"
    if alt_day3_duty:
        me "We can get into the cafeteria and steal some ice cream. How about some ice cream?"
        "She shook her head."
    un "M-maybe we could go for a walk?"
    me "Let's go for a walk, sure. Or did you think after a day like this we'd say goodbye and run away?"
    show un shy dress with dspr
    un "I don't know."
    "She whispered."
    un "What do you want?"
    "To tell her how I was standing at the information booth after breakfast this morning, wondering where else but the library and my own cabin I could find her?"
    "Is that the kind of thing you're allowed to say?"
    me "I don't know. I didn't get a chance to dance, and I'm not too fond of it either. So I still have my strength."
    stop ambience fadeout 6
    return

label alt_day3_un_cards:
    scene bg int_aidpost_night
    show un normal dress
    with dspr
    "After a little silence, she suddenly looked around - as if anyone could see us."
    show un normal dress far at left with move
    play sound sfx_close_cabinet
    "...She went to the door and locked it."
    show un normal dress far at right with move
    "And, pushing back the top drawer by the nurse's desk, she made an inviting gesture."
    show un normal dress at center with move
    stop music fadeout 6
    "I went over and peeked."
    "Nothing out of the ordinary - handkerchiefs, papers, medical cards... Stop!"
    "A rectangular object was discovered beneath the paper piles, which showed a proudly standing mamzelle in her most defiant attire and face."
    me "Cards."
    un "Yes..."
    play music music_list["eternal_longing"] fadein 2
    me "With chicks!"
    show un shy dress with dspr
    "She squinted at me, and I hastened to correct myself:"
    me "I mean, with girls."
    dreamgirl "Ahhhh, naked women cards!"
    me "Do you want to play?"
    un "I don't know. I'm not very good at cards...{w} Are you?"
    me "I know a few games. Thousand, there, hold'em. Buru, again."
    un "I'm only good at fools."
    un "And then there's this one... The one Electronik invented."
    dreamgirl "I hope she understands! That {b}those{b} cards are only played at strip?"
    th "Judging by the look, she understands perfectly! What's more, she's not at all frightened by the prospect of losing."
    un "Will you have one?"
    "I estimated the remaining work front and shrugged it off."
    "There really was only about ten minutes left to do. And judging by the way the attendants' corner lit up, Viola clearly wasn't going to be back anytime soon."
    "But just in case, I decided to be clear. So there'd certainly be no loose ends."
    me "You do realize these are not cards of interest, don't you?"
    show un surprise dress at center with dspr
    "She bloomed like a poppy flower again."
    un "I would play..."
    "And yet, keeps insisting!"
    me "All right, whatever you say. Let's call it a day then and play."
    "She smiled and dulled her eyes, hiding the gleam of excitement behind them."
    dreamgirl "Hehe, man! It looks like you're about to get undressed!"
    th "We'll see who gets naked."
    show blinking
    "In anticipation of the game, in no time at all we had dismantled the remaining box and, locking ourselves inside, sat down on the couch."
    show un smile dress at center with dspr
    un "Well, gambler, are you ready to lose?"
    me "Of course I am. I can't wait to see you in your very best underwear."
    "She threw her head back and laughed freely, as if the rest of the restraints that still remained in place had just blinked away and lost their materiality."
    "She covered her eyes and quickly, quickly dealt six cards at a time."
    "Game on!"
    "We argued a little over the stakes, but decided that for fairness it was worth setting a certain order without the possibility of a winback."
    "To put it simply, you can't win back, it's only negative."
    "We both seemed to wonder what the other's clothes were hiding."
    $ alt_day3_un_strip_pool_sp = 5
    $ alt_day3_un_strip_pool_un = 5
    $ alt_name_my_rival_r = "Lena's"
    $ alt_whose_first_move = 'player'
    $ alt_day3_gambler_behavior = 'gamble'
    $ alt_day3_gambler_skill = 3

    with fade
    call alt_day3_un_strip_play
    if alt_day3_un_strip_pool_sp == 0:
        call alt_day3_card_lose
    elif alt_day3_un_strip_pool_un == 0:
        call alt_day3_card_won
    return

label alt_day3_un_strip_play:
    menu:
        "Play!":
            if alt_whose_first_move == 'player':
                $ alt_whose_first_move = 'rival'
            else:
                $ alt_whose_first_move = 'player'
            $ INVISIBLE = False
            python:
                dialogs = {
                                (0, 'win','jump'):'alt_day3_un_strip_play_win',
                                (0, 'fail','jump'):'alt_day3_un_strip_play_fail',
                                (0, 'draw','jump'):'alt_day3_un_strip_play_draw'
                            }
                generate_cards_alt('bg int_aidpost_night', dialogs)
                rival = CardGameRivalWiseUsual(un_avatar_set, u"Lena, strip game", alt_day3_gambler_behavior, alt_day3_gambler_skill)
            $ alt_hint_poker = alt_hint_poker_contractual
            jump cards_gameloop_wise_alt
        "Give up!" if persistent.alt_day3_card_lose:
            $ alt_day3_un_strip_pool_sp = 0
            return
        "Win!" if persistent.alt_day3_card_won:
            $ alt_day3_un_strip_pool_un = 0
            return
        "Check the bets":
            "I took a quick look at myself and my opponent."
            if alt_day3_un_strip_pool_sp == 5:
                "Things were going more than great! I had a full set of clothes."
            elif alt_day3_un_strip_pool_sp == 4:
                "All in all, things are going pretty well. I said goodbye to the shirt, but I still have the rest."
            elif alt_day3_un_strip_pool_sp == 3:
                "The shirt was followed by the shoes, and I was left with only two items of clothing."
            elif alt_day3_un_strip_pool_sp == 2:
                "I could smell the foreboding of loss in my back. I had to say goodbye to the shorts; there was only one thing left."
            elif alt_day3_un_strip_pool_sp == 1:
                "Finita la comedy. I sat across from Lena in underwear and tried to pretend not to notice her stare."
            if alt_day3_un_strip_pool_un == 5:
                show un smile dress with dissolve
                "Lena was fully dressed and watching me with a smile."
            elif alt_day3_un_strip_pool_un == 4:
                show un smile dress with dissolve
                "Lena has so far gotten away with only her shoes."
            elif alt_day3_un_strip_pool_un == 3:
                show un smile swim with dissolve
                "Interesting moment! Dangerous, I would even say. She put the dress on the line and lost."
            elif alt_day3_un_strip_pool_un == 2:
                if persistent.hentai_graphics_7dl:
                    show un shy body close with dissolve
                else:
                    show un shy swim close with dissolve
                "Ugh! The prospect was breathtaking! She stayed in just her panties and played with her left hand against her chest."
            elif alt_day3_un_strip_pool_un == 1:
                if persistent.hentai_graphics_7dl:
                    show un shy body with dissolve
                else:
                    show un shy swim with dissolve
                "The situation was clearly not in Lena's favor. She was sitting in front of me completely naked, and I was drooling and moping."
            hide un with dissolve
            jump alt_day3_un_strip_play

label alt_day3_un_strip_play_fail:
    scene bg int_aidpost_night with dspr
    if alt_day3_un_strip_pool_sp == 5:
        $ alt_day3_un_strip_pool_sp = alt_day3_un_strip_pool_sp - 1
        "I smiled and pulled my shirt off without regret. Should I have regretted it?"
        jump alt_day3_un_strip_play
    elif alt_day3_un_strip_pool_sp == 4:
        $ alt_day3_un_strip_pool_sp = alt_day3_un_strip_pool_sp - 1
        "The sandals followed the shirt. Take them!"
        jump alt_day3_un_strip_play
    elif alt_day3_un_strip_pool_sp == 3:
        $ alt_day3_un_strip_pool_sp = alt_day3_un_strip_pool_sp - 1
        "It was hard to part with my shorts. But card debt is a sacred thing, so I took off my poor shorts."
        jump alt_day3_un_strip_play
    elif alt_day3_un_strip_pool_sp == 2:
        $ alt_day3_un_strip_pool_sp = alt_day3_un_strip_pool_sp - 1
        "No, I can't believe how she undressed me! I blushed like a crab and, covering myself with what I could, quickly pulled off my panties, leaving me in what the mother had given birth to."
        jump alt_day3_un_strip_play
    elif alt_day3_un_strip_pool_sp == 1:
        $ alt_day3_un_strip_pool_sp = alt_day3_un_strip_pool_sp - 1
        return

label alt_day3_un_strip_play_draw:
    $ show_cards()
    "No one's lucky, we're playing again."
    jump alt_day3_un_strip_play

label alt_day3_un_strip_play_win:
    scene bg int_aidpost_night with dspr
    if alt_day3_un_strip_pool_un == 5:
        $ alt_day3_un_strip_pool_un = alt_day3_un_strip_pool_un - 1
        show un smile2 dress with dissolve
        "Shoes flew into the corner."
        "It seems that defeat only inflamed the girl."
        hide un with dissolve
        jump alt_day3_un_strip_play
    elif alt_day3_un_strip_pool_un == 4:
        $ alt_day3_un_strip_pool_un = alt_day3_un_strip_pool_un - 1
        show un grin dress with dissolve
        "After a little hesitation, she put her hand behind her back..."
        "She turned her back to me, as if in a flash."
        un "Unbutton it, please."
        hide un with dissolve
        jump alt_day3_un_strip_play
    elif alt_day3_un_strip_pool_un == 3:
        $ alt_day3_gambler_skill += 1
        $ alt_day3_un_strip_pool_un = alt_day3_un_strip_pool_un - 1
        show un smile2 swim with dissolve
        "She seems to have realized that I was serious, because the slyness in her eyes was suddenly over the top."
        un "Come on, winner."
        "She turned her back again."
        un "Take the trophy."
        "With trembling fingers I undid the clasp, suddenly remembering that in some circles it is considered special chic to undo this nightmarish hook-and-loop device with one hand - in a few seconds."
        if persistent.hentai_graphics_7dl:
            show un surprise body close with dissolve
        else:
            show un surprise swim close with dissolve
        "She was left in just her panties."
        hide un with dissolve
        jump alt_day3_un_strip_play
    elif alt_day3_un_strip_pool_un == 2:
        $ alt_day3_gambler_skill += 1
        $ alt_day3_un_strip_pool_un = alt_day3_un_strip_pool_un - 1
        if persistent.hentai_graphics_7dl:
            show un angry2 body close with dissolve
        else:
            show un angry swim close with dissolve
        "Throwing an angry look at me, she rose slightly, without taking her left hand off her chest, and in one elusive movement she lowered the last item of clothing."
        "...on her thighs..."
        "...sat herself down..."
        "...and pulled on, putting her foot on her leg in between."
        "...past her knees, down to her shins."
        if persistent.hentai_graphics_7dl:
            show un laugh body close with dissolve
        else:
            show un smile2 swim close with dissolve
        "I sighed convulsively, and, laughing, she took off her panties in one motion and threw them immediately to the floor."
        un "This is my last chance to get even."
        un "I'm not just going to give up!"
        hide un with dissolve
        jump alt_day3_un_strip_play
    elif alt_day3_un_strip_pool_un == 1:
        $ alt_day3_un_strip_pool_un = alt_day3_un_strip_pool_un - 1
        return

label alt_day3_card_lose:
    scene bg int_aidpost_night with dissolve
    if alt_day3_un_strip_pool_un > 3:
        show un smile dress with dissolve
    elif alt_day3_un_strip_pool_un == 3:
        show un smile swim with dissolve
    else:
        if persistent.hentai_graphics_7dl:
            show un smile body with dissolve
        else:
            show un smile swim with dissolve
    "Yeah, that girl rolled me like she wanted to."
    if (alt_day2_gamblers_result['un'] >= 21):
        "I didn't expect anything else from the finalist, to be honest."
    else:
        "I don't know why she didn't show much class yesterday - today she was beastly."
    "She laughed softly, and I smiled back embarrassed."
    me "Congratulations. You won. You really won."
    un "What do we do next?"
    dreamgirl "Oh, I've got a couple of Deutsche Cinéma-inspired options."
    dreamgirl "Don't you want to try it? The girl doesn't seem to mind."
    th "Calm down, you horny monster."
    "I smiled at Lena."
    me "I don't know."
    "She threw another look at me, as if doubting... And threw a form at me."
    if alt_day3_un_strip_pool_un > 3:
        show un laugh dress with dissolve
    elif alt_day3_un_strip_pool_un == 3:
        show un smile2 swim with dissolve
    else:
        if persistent.hentai_graphics_7dl:
            show un laugh body with dissolve
        else:
            show un smile2 swim with dissolve
    un "Get dressed... loser!"
    $ persistent.alt_day3_card_lose = True
    $ lp_un += 1
    return

label alt_day3_card_won:
    scene bg int_aidpost_night with dissolve
    if persistent.hentai_graphics_7dl:
        show un sad body close with dissolve
    else:
        show un sad swim close with dissolve
    "She couldn't win back."
    "I wouldn't have let her."
    if persistent.hentai_graphics_7dl:
        show un grin body close with dissolve
    else:
        show un smile2 swim close with dissolve
    "And she thought and, laughing, took her hands off my chest."
    "My jaw landed on the floor with a clang."
    un "Well, have you seen enough?"
    "In a slightly nervous voice she said."
    "Is she the one shy of me? Really?!"
    dreamgirl "There's an opinion that she's shy of whoever stops by all of a sudden. The door though locked, but the windows..."
    un "Can I get dressed now?"
    me "Do you feel like it?"
    "She shrugged."
    un "For some reason I'm not embarrassed of you at all."
    dreamgirl "Sem, if you have an overwhelming desire to provide an individual demographic outbreak, now is the time."
    th "You're a fool, aren't you? Of course I have an overwhelming desire. But, hell, I'm a hell of a lot older than she is. Plus, she's underage."
    dreamgirl "Do I remind you of the age of consent?"
    th "Don't. I'm not stupid."
    if alt_day3_un_strip_pool_sp < 4:
        "She was getting a little chilly, judging by how chilly she was hugging her shoulders."
        me "Wanna come? Warm up?"
        "I nodded at my shoulder with a hint."
        me "Or will you get dressed?"
        un "I guess I'll get dressed."
        "She gathered her things and unwrapping her dress, in a quiet voice she added:"
        un "I wish we were at my place. I'd have gone..."
    $ persistent.alt_day3_card_won = True
    return

label alt_day3_post_strip:
    stop music fadeout 10
    play ambience ambience_medstation_inside_night fadein 3
    scene bg int_aidpost_night with dissolve
    if (persistent.un_7dl_good_ussr or persistent.un_7dl_good_rf) and (alt_day3_un_strip_pool_un < 4):
        "I gave her the clothes, and in the meantime I decided to look into the place where my sister had advised us to look."
    else:
        "By a sequence of actions I decided to look where the nurse had advised me to look."
    "The left upper drawer of the office was full of gray paper bags."
    "On the side that was visible, except for the three letters, there was nothing else listed."
    th "OTK? So the Union is responsible for quality?"
    "I took one bag, turned it over, and my eyes slid over the letters on their own."
    play music music_7dl["viola"] fadein 3
    "Beneath the stylized image of a working factory, it read 'Bakovsky Republican Rubber Products Plant.'"
    "Product No. 2. GOST 4645-81."
    show un shy dress with dissolve
    if (persistent.un_7dl_good_ussr or persistent.un_7dl_good_rf) and (alt_day3_un_strip_pool_un < 5):
        "Lena had already cleaned herself up and looked over my shoulder."
    else:
        "She stealthily walked over and stood next to me, reading over my shoulder."
    un "Rubber product number two? Isn't that..."
    if loki:
        me "Yeah, that's right. Viola's pretty good, huh?"
        me "That's really half the headache."
    elif herc:
        me "What else did you expect from our nurse."
        me "At least she didn't slip me a tube of lubricant and a funny video."
    else:
        un "From the kids, right?"
        "I nodded silently, feeling my tongue freeze to my throat again."
        "The sister is a fool. I realize, of course, that carnal relations are the essence of love, but, man, it's got to be some time. And not two days!"
        un "I don't know what to say."
        "Neither do I."
        "You could see she wanted to cry and laugh at the same time from the awkwardness of the situation."
        me "Stupid doctor humor."
        me "Don't hold it against the idiot, she must have been born old."
    "The associations are not difficult to continue. From 'Imnotlikethat' to the biting lip and the uterine-throat 'Here. Take your clothes off!'"
    "The girl tasted the erotic context, the girl liked it."
    show un surprise dress with dspr
    un "What do you think about..."
    "What do I think? Oh, just that it's against the law for someone to pry into the pioneers' private affairs."
    "Apparently Viola considers the discipline of sexual relations to be as delicate a matter as whipping."
    me "I'm allergic to latex."
    "Automatically rolled off the tongue."
    me "Though it's synthetic, I guess."
    "She stared at me with interest."
    show un smile dress with dspr
    un "So you..."
    me "Hey, hey, I didn't say anything like that!"
    "I waved my palms in front of me in a panic."
    un "What interesting details about our silent Semyon."
    me "There aren't any details. And anyway..."
    me "It's very personal."
    show un laugh dress with dspr
    un "Oh, absolutely!"
    un "But I, for one, don't know if I'm allergic to latex. How do you know?"
    show un normal dress with dspr
    if loki:
        "I laughed."
        me "Trying it on! Like Cinderella tried the slipper."
        me "It might've came in handy!"
        un "And?"
        show un serious dress with dspr
        "I shook my head."
        me "It didn't."
    "I realized that I was still twirling the unfortunate bag in my hands, and I hurried to put it back in the drawer."
    "Lena accompanied the articles with an interested look. She seemed to be thinking about taking a few to spare, so I hastened to react:"
    me "Looks like we're done here? Let's go?"
    show un smile dress with dspr
    un "Let's go."
    "She went to the door and turned the key and opened it."
    "Still, she didn't lie much when she said she was a child."
    "Played with the idea and discarded it, having played with it."
    show un laugh dress with dspr
    "Suddenly she laughed."
    me "Still laughing..."
    un "Why not. Your face is so..."
    me "What face?"
    un "Funny."
    me "Yes?..."
    show un smile dress with dspr
    un "The dumbest question you could ever ask. Well, shall we go?"
    me "Where?"
    "She hesitated between wanting to tap me in the forehead and her usual reaction to the cluelessness of others, and I rushed to her aid."
    me "You mean the dance?"
    show un shy dress with dspr
    un "What about. But if you don't want to-"
    "She instantly froze and blushed."
    dreamgirl "Indeed! What a load of crap she's come up with. Dancing to her! Maybe I should carry her in my arms. Take your clothes off!"
    th "You fucking piss me off. One more line like that, and I'm gonna eat bromine, okay? I'll find it."
    dreamgirl "I'll shut up now."
    me "Remember the first day we met? I said then that I didn't care what I did as long as you kept me company."
    me "If that ever changes, I'll tell you."
    th "Got yourself out of it, huh?"
    "She just stood there at the door like she was ready to accept my decision."
    "So it made perfect sense to go over and give her a hug."
    me "Really, no music this time. Is that okay?"
    show un normal dress with dspr
    stop music fadeout 3
    un "It's okay."
    stop ambience fadeout 3
    scene bg ext_aidpost_night with dissolve
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night fadein 3
    "We left the infirmary and, after locking it, stopped to confer - where we could go so they wouldn't find us, at least for a while."
    if loki:
        me "Maybe to your favorite place again?"
    elif herc:
        me "Maybe to the folds again?"
    else:
        me "Maybe to the sportsground again?"
    show un normal dress with dissolve
    "She shook her head negatively."
    un "Shall we go to the pier? It's beautiful there now."
    "And no one's just going to go down there."
    "You can't deny that girl's logic!"
    me "That makes sense. Let's go."
    "She immediately clawed at my little finger. It seemed to delight her to the point of some completely incomprehensible squeak."
    "We decided to take a little shortcut, going around the square on a path through the sparse thicket, so that we wouldn't meet anyone for sure."
    me "That's the way we're going to walk now, isn't it? Like this, by the little finger?"
    show un shy dress with dspr
    un "I'm sorry, don't you like it? S-sorry..."
    play music music_list["waltz_of_doubts"] fadein 3
    scene cg d3_un_forest
    with dissolve
    un "Let's do this the grown-up way then, on the arm?"
    "That girl was both funny and hilarious."
    un "We'll walk like big guys, huh?"
    "I laughed."
    me "Less discretion, I was just asking."
    me "I'm comfortable walking by my little finger, too-you're so tiny."
    un "I'm not tiny!"
    play sound sfx_tree_branches
    extend " Oh, mommy."
    "She's got her hand in my arm again."
    me "Not tiny, yes."
    "I stopped, and, turning to her, I hugged her."
    me "There, I hugged you, and now you'll be looking for a way out for two days."
    "She laughed a little audibly."
    "And I heard the splash of playing water."
    stop ambience fadeout 2
    scene bg ext_boathouse_night with dissolve
    play ambience ambience_boat_station_night fadein 3
    show un normal dress with dissolve
    "I took her by the hand and led her out into the beautiful night."
    "From the sky beneath our feet a silver moonlit path. {w}Like a spotlight catching an actor on stage, it focused the whole world's attention on us."
    "On me."
    "And the girl, snuggled up in some completely inexplicable impulse, dancing madly to the sound of the waves."
    if herc or loki:
        "As if I could really peel back the decisions and prefer her to something else."
        "How could I?"
        "This world, whichever way you turn it, simply has nothing of equal value to offer in exchange for this evening, the moon and Lena dancing to the beat of my heart and the rustle of the surf."
    stop ambience fadeout 2
    show un smile dress with dspr
    un "You're so serious now. Sometimes I feel like I don't know you at all."
    un "And the look in your eyes, as if you know you won't be here long - so you rush to live and breathe what time you still have left."
    "She put her hand on my shoulder."
    "Found my hand with her right hand and intertwined her fingers."
    scene cg d3_un_dance
    with dissolve
    "Soon, too, I succumbed to the allure of the moment, swaying involuntarily to the beat of the impromptu music of the words, the pulse, and the charm of the night."
    un "You've been fooling around all day today, acting like a little kid."
    un "And I suddenly realized that it is not shameful, not shameful to behave just the way I want to."
    un "If you want to sing a song, jump up and down, or make faces at others, do it, be a little more spontaneous."
    me "People might not understand."
    un "But that's their problem, isn't it?"
    "I'm so sick of this one-armed pose."
    "I didn't answer and, releasing my left hand, put it on the girl's back."
    "We're going to dance the way I'm used to... The way my heart is used to."
    "Lena proved to be a very clever girl - and almost instantly accepted the rules of the game, placing her palms on my shoulders where they were most appropriate."
    "How appropriate they turned out to be a few seconds later, clutching at the back of my head, pulling me closer."
    if loki:
        "The magic of the second kiss is that you don't fully believe the reality of the first."
    "I rarely ever close my eyes if I'm kissing someone I love - at least that was the case during my few romances."
    "And she wouldn't close."
    "We looked at each other and communicated with touching lips, pulling away only when the oxygen deprivation in our ears subtly hummed."
    un "Okay..."
    "I nodded silently."
    "And she resumed her monologue."
    un "The most appealing and the most disgusting thing about you is that you are obligatory for my thoughts to come true."
    un "Like with these foolishnesses. I understand that a man must smile at least once a day to keep from putting a bullet in his temple."
    un "I understand that sometimes you just have to let your emotions out - in tears, creativity or laughter."
    un "But I look at the indifferent faces of those around me and realize that - I can't."
    un "Even if it's bad and hurts a lot - I can't. And when the supply of bitterness inside reaches the check mark..."
    "I was silent, circling her in a dance, and it was eerie and cold how much her thoughts were like my own."
    "A man who disinhibits, who serves as the very point of force, whose very presence allows me to laugh and breathe."
    me "I can't promise that I will be there tomorrow, either. I can't guarantee even the next few seconds."
    me "But while I'm here - I don't want to let go of my hands."
    me "That's all I can say with accuracy, and all I can promise."
    un "That's enough already."
    me "For what?"
    "She put her head on my shoulder and remained silent."
    dreamgirl "A little mystery, you could have guessed it yourself. The girl asks for at least some assurance in return for generally everything she has or ever will have."
    "Mitchell, Burnett, Green... Right, what they could grow in a young head, even adjusted for the high IQ."
    "A girl wants romance, wants absolutes applied to feelings. And I... Man, even now I'm not a hundred percent sure I'm really feeling anything, and I'm not pretending to myself."
    dreamgirl "Just like with any other illness. Until you twist, you sit in front of the monitor, feeling like the latest faker."
    "A star is falling from the sky."
    me "A shooting star. Make a wish while it's falling."
    dreamgirl "A few grams of solid matter heated by friction in the dense layers of the atmosphere. What does that have to do with a wish?"
    th "Cheap kitchen cynicism of a know-it-all in a tank top and sweatpants with bubbles on his knees."
    th "The epitome of the 'consume, work, die' idiom."
    th "But don't you die yet. You'll come in handy when I've gone soft, and I'll be smacked in the face, stupid! - by throwing me back into my own world."
    un "I don't think there was any camp or town before you. That I made it all up to somehow justify my existence."
    me "Also, you drew me. And I didn't manage to turn the page with the story where you are. I couldn't get my hand up."
    "She huddled into me, as if afraid that I was really about to disappear."
    un "No past, no present. I make no plans, my psyche does not accept them."
    un "But it's sad and ridiculous to panic that I don't know how I'm going to let go of my hands now and spend a few hours without you."
    un "I just don't know. I can't imagine."
    "I kissed her instead of answering."
    th "After all, it is possible to run a marathon without unhooking the arms, after all. How much more time do I have here? Hours? Weeks?"
    "I closed my eyes."
    "And I remember my own deals with fate, where the stakes were always something extremely important and necessary."
    "Twelve years old was my first crush. I called her a cat for her funny face and cunning eyes."
    "For three years, I've been mashing reality, paying the price of time and missed opportunities."
    "Such stupid coincidences - two kids on the streets of a metropolis, the chance of meeting again is zero."
    "Zero? Yep."
    "We met at one of the children's concerts, and that's where this whole catastrophe started."
    "First performing on the same stage, then performing together, then for a duet - I never decided to develop the obvious and unconditional mutual interest into something more."
    "We even got into the same camp! And the first shift we slept in different quarters, but still saw each other every day, and the second shift we ended up in the same squad."
    "It got to the ridiculous point where we slept across the wall and could knock on the door or send romantic notes through the post office if we wanted to."
    "I never once knocked on that wall."
    "Fifteen years old - crush number two, details have faded from memory, she’s a year younger than me, and we joked about how we’re each other’s imaginary friends."
    "We're rehearsing a song together, and I don't need a microphone to sound on par with her quiet soft voice."
    "And I'm getting rhyming lines for the first time - and half of them are written with her face in front of my eyes."
    "And somehow I wasn't surprised that when they took me away in the ambulance with a fever of forty, she was the first one who rushed to see if I was dead."
    "True, when she left the hospital, she kissed a man I had seriously considered a friend. It's just a matter of life."
    "There's a 'do not disturb' sign on my soul."
    "Isn't that why I twitched now, like I was hooked, seeing the all-consuming emotion in those huge green eyes?"
    "The perfect combination, after all-I've always liked brunettes, and I've had a soft spot for green-eyed people all my life."
    "Perhaps this is the swan song of a tired heart. From here on, all that's left is to take what's given. Or to be rash."
    show blink
    stop music fadeout 3
    play ambience ambience_boat_station_night fadein 3
    me "It seems to me that I..."
    mt "Semyon! Semyon, where are you?"
    "Fool. You're in the way. Hide back in that hole you've been in for the last few hours."
    scene cg d3_un_dance
    show unblink
    "I reluctantly open my eyes."
    mt "Semyon!"
    "Negative Luck characteristic in action."
    "We're standing so densely that we could be mistaken for a single silhouette."
    th "We could try to hide."
    th "Though where would one hide on a dock?"
    scene bg ext_boathouse_night
    with dissolve
    show un normal dress
    with dissolve
    "I hope she doesn't come ashore. There's no need for that."
    "The silhouette is perfectly visible in the moonlight, and if it suddenly disintegrates into two separate people..."
    me "Shh... Maybe we'll get away with it."
    show un smile dress with dspr
    "Lena nodded silently, and her eyes were so intense and joyful. Crazy."
    show un smile dress close with dspr
    "I don't know what got into her, but before I knew it, her hands were all over my shirt."
    th "What is she doing?! We'll have a hard enough time if they catch us!"
    th "And if it's in such an interesting situation..."
    "However, I think all my furious thoughts without even moving from my seat for some reason."
    "I erupted like a match, all twitching from the tickling caress."
    "This did not go unnoticed, for the girl in my arms charmingly bit the corner of her lower lip and with redoubled enthusiasm began to climb with her fingertips and claws where she shouldn't have been!"
    "And all this to the accompaniment of our bad counselor's yelling."
    me "You're crazy. Do you know that?"
    stop ambience fadeout 3
    show un smile2 dress close with dspr
    un "Yes..."
    me "At least wait for the leader to leave!"
    un "That's the best part!"
    play ambience ambience_forest_night fadein 3
    "Why do I only get crazy women?"
    "Why can't there be a quiet, modest woman, eyes to the floor, wings bang-bang-bang - peace and quiet in the house?"
    "I grinned, remembering my first impression of Lena."
    "Actually, she was supposed to be the quiet one. But something went wrong, and it turned..."
    show un laugh dress close with dspr
    "Soon the counselor's voice faded into the darkness, and Lena, laughing, burrowed into my lips in a greedy, demanding kiss."
    "Quiet. Modest."
    "She tickled my sides with her unsophisticated manicure, just the way she wanted."
    "She dispersed all the heat reserves from my muscles with herds of goosebumps."
    "And only an inexplicably platonic crush - the same one that kept me from seducing Lena in the infirmary - allows me not to show my true attitude when the pads of someone else's fingers move over living skin."
    un "It's so nice to go crazy with you."
    "She was young, content with life, and drunk with love."
    un "We should do this more often."
    "She bet blind on a stranger - and lost."
    "Lena. Said her name was Lena."
    show un smile dress with dspr
    un "Come on, I'll walk you to your cabin."
    un "Or should we ask Miku to spend the night at the club?"
    me "Stop it. Just stop it."
    "My head hurts. Local reality seems to have jumped on the wrong tracks somewhere that it should have."
    me "Even medicine in large doses is poison. And satiety for each other is a hundred times more dangerous."
    me "You'll get sick of me. Very quickly. Especially since I'm not a very interesting person."
    "She was ready to argue every phrase I said, letter by letter, word by word. But she kept quiet."
    "That's right, you have to leave something for tomorrow, too."
    scene bg ext_house_of_mt_night_without_light
    play ambience ambience_camp_center_night fadein 2
    show un grin dress with dissolve
    play music music_list["a_promise_from_distant_days"] fadein 5
    "Soon we reached my cabin and for a long, long time we didn't want to separate."
    "Hungry touches of hands, lips, glances-it seemed impossible to satiate this raucousness with anything..."
    "It was helped by the creaking boards behind me and Olga looking out at the fire."
    mt "Semyon, you?"
    "She inquired."
    "She had to look out of the lighted place into the darkness, so she couldn't see me."
    me "Me."
    mt "So come on in."
    "She hid in the cabin, and I had to take myself away by force."
    me "Good night."
    show un grin dress with dspr
    un "Sweet dreams."
    hide un with dissolve2
    "Lena smiled at me goodbye and ran away."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_bath_voyeur:
    scene bg ext_bathhouse_night with dissolve
    play ambience ambience_forest_night fadein 3
    $ alt_day3_sl_bath_voy = True
    "It turned out to be easy to find a bathhouse. It looked more like a hut than a place where you can cleanse your body and thoughts."
    "In any case, the thick smoke billowing from the chimney ruled out ambiguity."
    "It remains to figure out who is there now."
    "So you won’t end up with embarrassment - as if the stupid things that happen to me without my will are not enough, now let's also goof off, climbing into a busy bathhouse, yes..."
    if counter_sl_7dl == 5:
        "I already forgot what Slavya was talking about, something about the queue."
        "I should check to see if I can come in."
    else:
        "The windows where the light was on were foggy, but from time to time a silhouette flickered in them, and I, moving closer, tried to see who it was. If it's a boy, then everything is fine, but if..."
    "Belatedly, I realized what I was doing when the condensate on the glasses dripped down, and the blurry contours formed into a girl's figure!"
    stop ambience fadeout 2
    if persistent.hentai_graphics_7dl:
        scene cg d3_sl_bath_unplaited_7dl with flash:
            xalign 0.5 yalign 0.5 zoom 1.15
            linear 0.5 zoom 1.0 xalign 0.5 yalign 0.5
    else:
        scene black
    play music music_list["waltz_of_doubts"] fadein 3
    "Slavya! Oh, mother!"
    "I bit my fingers. Of course, she promised me to hold the line, but, damn it, I didn't think she would do it this way!"
    dreamgirl "And how was she supposed to? Sit in the dressing room and not let anyone in?"
    "And, in strict accordance with the laws of the genre, naked. Well, there can be no others in the bathhouse."
    "I swallowed noisily and stared at her. It's... It's..."
    dreamgirl "A real peep show! You put 25 cents in the chute and the curtain opens, and there..."
    dreamgirl "Well, how is it, in general? Move your lustful thoughts, it's hard to see!"
    dreamgirl "And let me know, what are you staring at? Have you ever seen naked women?"
    "About five years ago. And then..."
    if ((counter_dv_7dl == 4) or ((alt_day3_dj == 'dv') and (alt_day3_dancing2 != 'dv_2'))):
        dreamgirl "OK. Well, what do you say about the fact that you and Alisa..."
        th "Me and Alisa is different."
    elif counter_un_7dl >= 5:
        dreamgirl "OK. Well, what do you say about the fact that you and Lena..."
        th "Me and Lena is different."
    elif counter_mi_7dl == 2:
        dreamgirl "OK. Well, what do you say about the fact that you and Miku..."
        th "Me and Miku is different."
    dreamgirl "Ah, yes, that's understandable. You have a good taste, sir."
    dreamgirl "Would you like to come in then?"
    dreamgirl "Rub something for her... inside or outside."
    "There was a scurrilous chuckle in my head, I tried to turn away - but I couldn't!"
    "The body responded instantly! And the only thing it was willing to exchange this spectacle for direct tactile contact."
    "Actually, electricity has already walked through the body, waking up all the necessary mechanisms, and if someone caught me in the state I was now..."
    "There was no one around, and no one interfered with my enjoyment of the visual feast."
    "Not for long."
    "At some point, she, startled, froze - as if bumping into my eyes."
    "And frighteningly slowly began to turn..."
    "Towards the window!"
    "I recoiled in horror."
    with fade
    "All right, time to go."
    "I have to... I said I «have» to! Go!"
    "Almost by the hair, I dragged myself away from the window."
    scene bg ext_bathhouse_night with blind_l
    with dissolve
    play ambience ambience_forest_night fadein 3
    "Meanwhile, the light in the room went out, and, judging by the creaking of the boards, Slavya finished washing and went out into the dressing room."
    show sl2 normal dress with dissolve
    "Five minutes later, she went outside and breathed in the night air with pleasure."
    if (alt_day3_dancing1 == 'sl_1') or (alt_day3_dancing2 in ('sl_2', 'sl_12')):
        "Slavya was in the same dress in which she danced with me."
        "The only difference was that this time it was put on wet skin, and therefore the imagination worked at full capacity!"
    else:
        "She was wearing an interesting sarafan dress, high opening slender legs, judging by the absence of extra folds, it was put on straight over what was washed."
        "I involuntarily stared, realizing that I had never seen Slavya before without her ubiquitous braids."
    show sl2 smile dress with dissolve
    "Then she noticed me sitting on a bench."
    sl "Semyon, how long have you been here?"
    "Ask if I saw you from all angles? The answer is yes."
    me "Right here, maybe five minutes."
    "I confessed honestly."
    me "With a light breeze!"
    "That's right, before that, I was in a slightly different place."
    sl "Thank you."
    "She stretched, and the dress, worn over wet skin, outlined in relief what was supposed to be outlined, and I hurriedly put the towel on my knees."
    sl "It's so good, after the bath!"
    sl "Do you have anything to wash with? If not, I can give you a washcloth."
    "I again had a picture before my eyes - where was the washcloth and what she saw there - I urgently ordered the body to calm down."
    me "N-no, thanks."
    "I thanked."
    me "I have my own."
    sl "Semyon, you're kind of weird."
    me "Wh-what kind of?"
    "I grunted stifledly."
    sl "Tense, or something..."
    me "I don't..."
    show sl2 laugh dress with dissolve
    sl "Syom."
    "I looked up and met her gaze, full of some demonic slyness."
    sl "What, were you peeping?"
    "It didn't seem to bother her at all."
    sl "Really?"
    "There was nowhere else to blush, and I seriously thought about falling through the ground."
    me "I didn't..."
    sl "Yes? I have other information."
    show sl2 smile2 dress close with dissolve
    "She came closer and, reaching out her hand, put it on my shoulder."
    "The girl stood a little longer, thinking about something, and then shook her head."
    sl "I'm going to sleep. Sweet dreams."
    me "Ah... yes."
    "I followed her with my eyes, all in the power of that magical moment when she..."
    hide sl2 with dissolve
    "Going into the bathhouse, I first of all poured half a scoop of cold water and knocked it over myself, yelling out loud. For good."
    if counter_dv_7dl == 4:
        "And anyway, I have Alisa."
    elif counter_un_7dl >= 5:
       "And anyway, I have Lena."
    elif counter_mi_7dl == 2:
        "And anyway, I have Miku."
    "After washing, I gave the room to Miku and Lena, I thought about... {w} And almost dragged myself away from the log building by force."
    th "I need to sleep. Sleeeeeep!"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_mi_7dl_init:
    scene bg ext_admins_night_7dl with dissolve
    play ambience ambience_camp_center_night fadein 3
    play music music_list["a_promise_from_distant_days"] fadein 2
    "There was hardly any of the inherent hum of the bass near the administration building."
    "My favorite state is when you can hardly hear anyone anymore, but you still feel..."
    dreamgirl "Chad of cooties?"
    "The inner goofy man servilely offered an option."
    "With a hum, I agreed with the option offered."
    th "Harsh, of course, but generally true."
    "The side effect, the aura, the outward mood - you could call it whatever you wanted, but something in my life was definitely lost when I stopped going to camps and sullenly huddling in the corners at discos."
    "The worst thing, perhaps, was that attempts to repeat the foray into, for example, the clubs of my Northern Capital, produced exactly nothing."
    "On the camp dance floor everyone knows each other, is familiar, has seen each other - in the city, the crowd is a disjointed broth of people clustered by acquaintances."
    "That's why it's not the same, at all."
    "The bench was already a little damp from the evening dew, so I spent some time sitting down."
    "Inhaled deeply..."
    show blinking
    scene black
    pause(2)
    voice "You're sitting alone again."
    "Someone's voice chided me."
    "It sounded in low tones, dangerously close to a whisper, and so there was no way I could pick out a possible... host? Mistress?"
    "Probably the hostess."
    "Guys usually don't have to explain anything - the right to leave the dance floor is respected by all."
    me "That's that."
    voice "Don't you like dancing?"
    me "I do."
    "The confession just rolls off the tongue."
    me "But I like it as a performance, as a performance I have to watch."
    me "But to participate... I'm sorry."
    voice "You're weird after all."
    "I was clapped on the shoulder, and a moment later I realized I was alone."
    "Another fail-safe instinct."
    "Everyone praises computers for multitasking, for their ability to handle a hundred things at once."
    "But what's the point if you're not too multitasking?"
    "Some clever person would think to chastise Caesar and other amateurs for parallel writing, talking on the phone, and so on."
    "But where do these amateurs have room for conscious reflection on anything, who's to tell me?"
    "It's all on the surface, circling the water, bouncing the pebble-coin."
    "And Miku doesn't get out of my head."
    "Though I've been tailing her for two days now. They're about to mock her."
    "Pointing fingers."
    dreamgirl "The boy and the girl were friends, the boy treasured his friendship..."
    dreamgirl "And he didn't think of falling in love, and didn't know until now that he would be called the silly word 'suitor'!"
    dreamgirl "Remember the bourgeois? Soon you'll be poked the same way, too."
    "No, I wasn't really intimidated by anyone pointing a finger at me."
    "Not very pleasant, of course."
    "But nothing fatal."
    "The other thing about Miku..."
    if alt_spt > 0:
        "She really isn't very well-adjusted to life, is she?"
        "To think that to win her unconditional trust, it was enough just to treat her like... a human being?"
        "Not to look with admiration or appreciation or whatever, as absolutely everyone in my old world was accustomed to."
        "The dreaded mystery of smiling at the person you like, which was never given to me, has finally come to pass."
        "I guess it's true-just waiting for the right time and the right person."
        "Daredevil Miku. Near whom you can allow yourself to lead a little more courageously and honestly than you've allowed yourself before."
    else:
        "It's true what they say, there are devils in the still waters."
        "Now, in retrospect, I realize that, strictly speaking, she was the one who was meeting me, for she was the one I saw first when I opened my eyes."
        "But either the sight of the 'vision-girl' was too out of place, or my poor head was incapable of perceiving the wonders supplied - and she was forgotten until the moment I came to meet her."
        "And looking at the empty-headed chatterbox without any depth of thought in her transparent gaze, how could I have guessed the passions raging on the other side of her aquamarine eyes?"
        "A girl. Pretty. A little out of my type, but we don't argue about them."
        "Kind, cheerful and funny. A little gibberish, a forgivable flaw when you first meet her."
        "And when you look inside..."
        "I haven't had much experience with friendship, but for some reason I wanted to be someone Miku could at least trust."
        "No one deserves that kind of loneliness."
    "I was interrupted from my thoughts by loud voices coming from outside the infirmary."
    "Taking a deep breath, I got up and went to reconnoiter."
    stop music fadeout 3
    scene bg ext_aidpost_night
    with dissolve
    "The disco was winding down, so the chance of bumping into pesky pioneers was minimal."
    "But I could see a couple of silhouettes scurrying past me."
    "And who would have guessed."
    show cs normal at left
    show us calml dress at right
    with dissolve
    "Ulyana Bat'kovna and Violetta Cernovna."
    me "Did something happen?"
    "I went out into the lighted spot under the lantern."
    "Ulyanka flinched in surprise, and Viola did not move an eyebrow."
    "She waved her hand to keep in the keel, and continued on her way."
    hide cs with dissolve
    show us normal dress at center with dissolve
    "There was nothing to do - I had to take the offer. Curious!"
    me "Hey kid, what's the matter?"
    "I asked in a whisper."
    us "Nothing. Four-eyed starred from somewhere, hit his head, no brain damage."
    me "Huh?"
    "It didn't immediately dawn on me that the girl was joking."
    "After all, why would a fourteen-year-old have a penchant for black humor?!"
    show us smile dress with dspr
    us "Beh! Faster, rookie, or you'll miss it."
    "She picked up her step as she leveled with Viola, letting me know that the conversation was over."
    scene bg ext_clubs_night
    with dissolve
    play music music_list["door_to_nightmare"] fadein 4
    "Our way was toward the gate."
    "Or should I say, toward the club building."
    "As we approached, there was a group of pioneers and pioneer girls already standing there, talking animatedly about something."
    "There was a ladder leaning against the roof, and little by little I began to guess."
    "And when I saw the awkwardly spread out figure..."
    if persistent.mi_7dl_good_star or persistent.mi_7dl_good_human:
        "It was the books I read or the movies I watched, but I couldn't get rid of the persistent feeling of deja vu."
        "I was watching it from a distance, realizing on some level that I was to blame for what had happened."
        "Namely, my inflexible selfishness is partly to blame for Shurik now lying there after a brief flight from the roof."
        "Why he got up there is a separate question."
        "But according to the basic rules of the game, I was supposed to dance at the disco, after which I successfully went to the clubs and pretended to help."
        "Instead, however, I am snatched right out from under the recruiter's nose by a raving Jap hottie and dragged to dance on."
        "And so Viola, too, instead of torturing level forty in Xonix and indulging in herbal tea, sits on her knees, cursorily examining the unconscious bespectacled man."
    "In the blue light of the street lamp, the blood seemed black, and I absent-mindedly marveled at it."
    "Until it suddenly occurred to me that if it was coming out of his head..."
    "Ah, no."
    "I took a closer look: in addition to the bad landing, Shurik had managed to cut his own arm."
    "And Violetta kept wiping and wiping his forehead, saying something."
    "Completely ignoring the cut hand, completely ignoring those around her."
    "In the meantime, there was already a puddle of water coming out of the cut."
    ba "Okay, pioneers, I'm only interested in one thing."
    show ba normal uniform with dissolve
    "The gym teacher appeared out of nowhere - in his unbreakable tights looking like a totalitarian Superman parody."
    "Somehow no one asked what right he had to hang around here and ask uncomfortable questions."
    ba "Who was here from the beginning and saw everything?"
    th "He's... Interviewing witnesses?"
    dreamgirl "What surprises you?"
    dreamgirl "In the USSR, the service was nothing like ours - prestige."
    dreamgirl "So it's no surprise that our Boriska is from some militia, and comes here on vacation."
    ba "Did Trofimov manage to do something on the roof or..."
    cs "Boris, are you even normal to ask such questions?"
    "Violetta was indignant, shaking off her stupor in an instant."
    "She took another look at her ward, aghast at the cut."
    "That's where her bag came in handy, as the nurse fussed over the wounded man."
    show ba evil uniform with dspr
    ba "Mind your own business, Violeta Cernovna. And I'll mind my own."
    "He interrupted the nurse and looked around again at those present."
    show el normal pioneer at fleft with dspr
    el "Boris Alexandrovich, I... Yeah. I've been here from the beginning."
    "Electronik pushed forward and stood beside me."
    "Looked at the blood dripping under his comrade and, swallowing loudly, turned away."
    ba "Did you see everything?"
    show el upset pioneer with dspr
    el "Actually, I participated."
    "Confusedly explained Electronik."
    el "We had to check the antenna on the roof - remember the storm when Olga Dmitrievna went into town?"
    "After waiting for a nod, Electronik continued."
    show el normal pioneer with dspr
    el "So, we decided to climb upstairs and see if there was anything we could fix."
    show el upset pioneer with dspr
    el "But I didn't know I was so afraid of heights!"
    "Electronik blushed, but stubbornly continued the story:"
    el "So Sasha decided to climb himself."
    th "Why are Viola's hands shaking, I wonder?"
    "She put the bandage on hastily, without hesitation - but her fingers were still shaking."
    "Barely noticeable; if I hadn't expected to see it, I wouldn't have noticed it at all."
    "Especially at night."
    "Especially from a meter and a half away."
    show el normal pioneer with dspr
    el "He didn't have time to do anything - he only made it to the edge of the ladder."
    el "Looks like he lost his balance, tried to grab the edge of the roof..."
    ba "I see."
    "Sanich took a step back."
    ba "Thank you for your service, and I have one call to make."
    us "Uncle Borya, can I help?"
    "Surprised Ulyanka."
    ba "Later, {b}kid{/b}."
    hide el
    hide ba
    with fade
    stop music fadeout 3
    "He disappeared into the darkness before anyone could stop him."
    play music music_list["just_think"] fadein 6
    "The nurse just waved her hand."
    "At her suggestion, Shurik had already been moved to a flat place, but..."
    "She kept doing something with the bespectacled man's wound - the head just needed to be stabilized."
    "But in vain."
    "Even someone as far removed from medicine as I was understood: if the blood was coming through the bandage - we were in deep shit."
    "Little by little, the pioneers began to disperse - not so much to sleep, but to the admonishing kicks of the squad leaders."
    "In the end it was just the three of us: me, Viola and Shurik."
    cs "Olga, do you have a cigarette?"
    "Nurse asked the void."
    "Oh, also Olga."
    mt "Do you even, do you think..."
    show cs normal with dspr
    cs "I think, Olya, I think."
    cs "Sometimes you have to act on circumstances. {w}And they are such that I lack the competence to do something about this wound."
    show mt surprise dress at left with dissolve
    mt "You mean..."
    cs "Yes. To a doctor. Someone who knows what to do in cases like this. Not..."
    "She glanced at me and then mouthed off."
    show mt normal dress with dspr
    mt "Semyon, why are you still here?"
    "I shrugged:"
    me "I have a feeling. That I'm about to be useful."
    "And Viola nodded in time with me:"
    cs "Alexander will have to be driven to town. And I can't do it alone."
    mt "Why don't we harness Boris?"
    "Sister shook her head negatively:"
    cs "We need someone of similar size - and not afraid of blood, like some."
    cs "In short, there's a candidate, no recusal."
    mt "But I have to write you permission to leave..."
    "Heavy sigh, eyes of grief:"
    cs "You write retrospectively. Well? The pioneer won't wait."
    "No one was interested in my opinion on the matter."
    "But how could I pass up an opportunity to legally drive into town? That's right. I couldn't."
    stop music fadeout 3
    "Although, as it turned out, I wasn't the only one who couldn't."
    show mi normal pioneer at fright with dissolve
    mi "Oh, Senechka, I've been looking all over for you, you..."
    "Miku has already had time to change her clothes and tidy herself up."
    "As if yesterday's revelations hadn't happened - still the same cheerful child."
    "With a heightened degree of talkativeness."
    show mi surprise pioneer with dspr
    "She stopped talking when she saw Shurik lying on the grass."
    mi "What happened here?"
    "In a sing-song voice the trouble asked."
    mt "Nothing you should know."
    "The leader answered glumly, deliberately looking at the watch on her wrist."
    mt "It's almost bedtime, you'd better go to bed."
    mi "But I..."
    show mt smile dress with dspr
    mt "Hatsune, do you have trouble hearing?"
    "Affectionately smiled the squad leader."
    show mi upset pioneer with dspr
    mi "I hear well. Very much so, Olenka Dmitrievna. Stop talking to me like a child."
    show mt normal dress with dspr
    mt "In that case, maturely, feet in the air and to the bunk!"
    "Harped the squad leader."
    cs "Although, I could use another helper."
    "Thoughtfully, Viola brooded behind our backs."
    "The leader gasped at her friend's treachery."
    show mt angry dress with dspr
    mt "Did I say something someone didn't understand?"
    show mi dontlike pioneer with dspr
    mi "You heard that, help is needed."
    mi "It's enough that you locked me alone in the farthest corner!"
    me "Olga Dmitrievna?"
    show mt rage dress with dspr
    mt "I said it all."
    mt "I won't let Hatsune go anywhere!"
    mt "I answer to the committee and her father personally with my head for the girl's life and health."
    menu:
        "And for conscience, too?" if herc:
            $ alt_day3_mi_7dl_donor = 1
            $ alt_hpt += 1
            show mt normal dress with dspr
            mt "You mean?"
            me "Olga Dmitrievna, you have just stated in public that Shurik's life and health mean less than Miku's."
            "I squinted my eyes and looked her point-blank in the eye."
            me "Did you really mean it?"
            show mt normal dress with dspr
            mt "You all know exactly what I mean."
            "She hastily crossed her arms over her chest."
            mt "No."
            show mi angry pioneer with dspr
            mi "Semyon is right. I can't allow you to act like I'm something special just because you promised someone something."
            mi "You have no right to detain me by force."
            "She held her head up high."
            mi "I'm coming!"
            hide mi with dissolve
            "She stepped back to me with a passing nod."
        "Why don't you let her choose for herself?" if loki:
            $ alt_day3_mi_7dl_donor = 1
            $ alt_hpt += 1
            "I was surprised to hear my own voice."
            me "You may not be aware of it, but according to the laws of her own country she is considered old enough."
            show mt normal dress with dspr
            mt "Old enough for what?"
            "I was embarrassed."
            me "For instance, to get married."
            show mt angry dress with dspr
            mt "Let her marry when she goes home!"
            mt "In the meantime, I decide..."
            show mi angry pioneer with dspr
            mi "No. It's not up to you."
            "The Japanese girl straightened to her full one hundred and sixty centimeters and looked up at the squad leader from below."
            mi "Forgive my insubordination, Olga Dmitrievna-san."
            mi "But I really would feel bad if-"
            "Her voice broke, so I guessed rather than heard:"
            mi "If it's like home here, too."
            show mi rage pioneer with dspr
            mi "I don't want it to be like that anymore."
            mi "I'm a human being, not a puppet!"
            hide mi with dissolve
            "Without listening to objection, she picked up the torn chevron from Shurik's shirt from the ground and, hiding it in her pocket, walked back to me."
            "I suddenly realized that I was immensely proud of this girl."
        "Olga Dmitrievna, I'll keep an eye on her" if dr:
            $ alt_day3_mi_7dl_donor = 1
            $ alt_hpt += 1
            "I promised."
            me "My word of honor. I'll make sure everything's okay so no one gets in trouble."
            "I grinned ingratiatingly."
            me "You may not believe Miku, but believe me."
            show mi smile pioneer with dspr
            mi "Us!"
            "Miku bravely hid behind my back, but I could feel the warmth of her breath on my neck."
            "I smiled and nodded."
            "The psychology of negotiation: we're friends, we're warm to each other. Come on, smile."
            "And Olga smiled."
            show mt grin dress with dspr
            mt "But if even a hair falls from her head..."
            "Her smile grew even more affectionate, and I involuntarily swallowed."
            "But I agreed with that, too."
            "Now I was willing to go along with anything as long as they let us go!"
            "My gut told me we were doing something very right and important."
            "One minute and we were seated in the cabin."
            "Shurik slept in the back, next to me - he was secured so he wouldn't shake too much during the ride."
            "I made myself comfortable and allowed:"
            me "Let's get going."
        "So I have to go alone?":
            $ alt_spt += 1
            mt "Together. You and Violetta can handle it."
            show mi angry pioneer with dspr
            mi "But I want to help!"
            "Suddenly the Japanese girl's eyes flashed."
            mi "You can't make me go against my principles!"
            mt "Hatsune!"
            mi "You can't treat life and health like that!"
            show mt normal dress with dspr
            mt "I can."
            "Calmly replied the leader."
            mt "The more people are hurt by the thought of you being sick, the more important your health is."
            mt "Shurik has Violetta Cernovna and Semyon. They will take care of him."
            mt "And imagine how many people would be upset if {b}something happened to you{/b}."
            "It sounded like our trip was going to get dangerous."
            mt "Are there enough fingers to count?"
            "The voice is soft, ingratiating. Gentle."
            "And there's no negativity behind that voice, just holy rightness - yes, indeed, many, many people, very many people would be upset if anything happened to Miku."
            "And when the Japanese girl got it - she shook."
            "Broke down."
            show mi upset pioneer with dspr
            "Backed away."
            "She looked down at the floor, blushed, and whispered in a confused whisper, shaking small and small."
            show mi cry pioneer with dspr
            mi "Please forgive me, Olga Dmitrievna-san. I am a fool, I am such a fool."
            "She sobbed."
            mi "But I so wanted to be useful!"
            mt "You will be much more useful in your place. By the way!"
            "The leader looked at her watch."
            mt "It's still fifteen minutes until lights out - will you have time to put the equipment away?"
            hide mi with dissolve
            "Miku nodded, hesitating, and, dragging her feet, disappeared into the darkness."
            mt "And you, I dare not hold up."
            "Nodded Olga."
            "After which all I had to do was open the door next to Viola and climb into the stuffy womb of the Volga."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day3_sleeptime:
    play ambience ambience_camp_center_night fadein 1
    play music music_list["a_promise_from_distant_days_v2"] fadein 2
    if alt_day3_uvao_spotted:
        scene bg ext_house_of_mt_night_without_light with fade
        "The house welcomed me with peace and quiet. Olga Dmitrievna was neither inside nor on the way."
        pause(1)
        stop ambience fadeout 1
        play sound sfx_open_dooor_campus_1
        scene bg int_house_of_mt_night2 with fade
        "I lay down on the bed and tried once again to combine everything I saw and understood into a more or less whole picture."
        "The picture did not add up, but it was felt that someone's cat ears were sticking out of everything that was happening."
    elif counter_dv_7dl == 4:
        scene bg ext_house_of_el_night_7dl with dissolve
        pause(1)
        play sound sfx_open_dooor_campus_1
        scene bg int_extra_house_7dl with dissolve
        "Having reached the place of temporary lodging for the night, I rolled out the roll lying here, put down the pillow kindly lent by Slavya and, stretching out to my full height, allowed myself to relax."
    else:
        if (lp_un >= 12) or ((lp_un >= 11) and (counter_sl_7dl == 1)):
            scene bg ext_house_of_mt_night_without_light with fade
            play ambience ambience_camp_center_night fadein 1
            "It was a beautiful day, it was a beautiful evening."
            "And somehow in this life appeared a person that all of this was arranged and built for."
            "It didn't just happen, did it?"
            "One would hope so."
            "There was something about us from day one, something that made me catch sight of her in the dining room, wait by her side, and seek her company by hook or by crook."
            "And if..."
            "My attention was drawn to a silhouette flickering by the front door."
            show sl normal pioneer with dspr
            "Slavya?"
            me "What are you doing here?"
            "Demandingly I asked."
            me "And how long have you been here?"
            sl "Quite a while."
            "Lips parted, girl."
            sl "I'm here to see you."
            dreamgirl "Wow! Isn't it a little early? For the third day?"
            me "Oh, yeah? Well... What can I do for you?"
            sl "I won't be long."
            th "Probably with your stupid dancing again."
            if (alt_day2_bf == 'sl') and (alt_day3_dancing1 != 'sl_1'):
                "I should have invited her - even if it wasn't entirely of my own free will."
            me "I'm listening."
            "I couldn't be accused of being unfriendly - after a busy day, I couldn't feel my legs under me."
            sl "It's about your relationship with Lena."
            th "Yeah."
            th "I guess this is a good time to roll your eyes and bark that it's none of her damn business?"
            th "Or 'she's an activist, she's allowed'?"
            sl "I've seen the way you two look at each other."
            sl "And I have to say I completely approve of your choice..."
            "She stumbled halfway through, apparently unable to find a relatively innocuous epithet."
            sl "Uh... I mean, you two deserve each other."
            me "Thank you. Is that all?"
            show sl shy pioneer with dspr
            sl "Not really."
            sl "I came to say this:"
            show sl serious pioneer with dspr
            sl "Lena may seem like a battered, quiet girl out of this world-and she is. {w}But she's not alone."
            me "What does that mean? Is she seeing someone? Is that what you wanted to tell me?"
            sl "No, no! I'm talking about the fact that she's not alone - and we, all of us who have known her for years, will do everything we can to keep her from crying. {w}Do you get the hint?"
            me "No."
            if loki:
                me "Didn't anyone ever tell you that it's not very ethical to hold a candle to someone else's relationship?"
            sl "I basically said it all. If you hurt her, you'll have to deal with me and the other girls."
            dreamgirl "I'm scared piss and shitless, how horrifying."
            if loki:
                "I was amused by her touching childish belligerence."
                "For some reason she reminded me of a hen, sticking up for her chicks."
                "And if so, what was the point of explaining to her that, after what happened to me, I would cherish Lena as I had never cherished anyone before?"
                "Maybe that weird girl on the bus is right."
                "Maybe this really is my only chance?"
            me "Is that everything now?"
            show sl smile pioneer with dspr
            sl "Yes!"
            sl "Sweet dreams. And think about what I said."
            th "There was no sadness."
            stop ambience fadeout 1
        scene bg int_house_of_mt_night2 with fade
        "When I reached the cabin that had already become my home, I took off my clothes."
        if counter_mi_7dl == 2:
            "Still trying not to crumple a chic shirt and very good trousers."
        elif (alt_day3_dancing2 == 'dv_2'):
            "After today's scene on the dance floor, I wanted to hide under the covers as soon as possible and sit there until the end of the shift."
            th "Well, how could you not understand that it's better not to touch Dvachevskaya!"
            "After counting to ten, I calmed down and sighed, forcing myself to think about anything but the evening embarrassment. And I, surprisingly, succeeded."
    "Thoughts flowed lazily and measuredly."
    if alt_day3_duty:
        "...My today's duty..."
    if counter_un_7dl >= 3:
        "My morning pranks in the library, with a whole dragon and an enemy army."
        if (counter_un_7dl >= 5) and (herc or loki):
            "Resulted in an afternoon hike with a touching explanation."
            if counter_un_7dl == 6:
                "A headache pill that wasn't what I thought it was."
                "Our dance."
                "...Lena..."
    if counter_sl_cl >= 3:
        "A trip to the beach turned into an opportunity to find out what the girls think of me."
        if counter_sl_cl >= 5:
            "A touching story of one who is becoming closer and dearer to me."
    if (alt_day3_date in ('dv', 'mi')) and (alt_day3_dj != 'mi'):
        "...Miku's concert..."
        if counter_dv_7dl >= 3:
            "...and her still, hunting me..."
            if counter_dv_7dl == 4:
                "...Our performance with Dvachevskaya, enchanting in its stupidity, about who does what and why..."
                "...Amazing frankness and openness of a sad girl with purple hair..."
    if counter_mi_7dl == 2:
        "Both stupid and funny situation in the dressing room."
        if (alt_day3_dancing1 == 'mi_1') and (alt_day3_dj != 'mi'):
            "Dance lessons..."
        if alt_day3_dancing2 == 'mi_2':
            "...Evening dance. We are both in magnificent outfits, and involuntary pride that she is so beautiful."
        "Stupid scene with a squad leader who thought exactly what she should have thought."
    if alt_day3_technoquest1 == 2:
        "Run around with that radio."
        "And stairs."
    if (alt_day3_dj == 'dv') and (alt_day3_dancing2 != 'dv_2'):
        "And one mischievous girl to the gnashing of teeth, who from now on will fill this camp with music..."
        "{i}My{/i} music."
        th "She'll listen to it, won't she?"
    if alt_day3_dj == 'mi':
        "Japanese girl in huge headphones behind the turntables."
    if alt_day3_dv_guitar == 3:
        "Evening with a guitar."
    if alt_day3_us_bugs == 1:
        "The bugs that Ulyanka and I caught and slipped to the evil squad leader."
    if alt_day3_sl_bath_voy:
        "...Scene in the bathhouse..."
    if alt_day3_uvao_spotted:
        call alt_day3_uvao_ch4
        pause(1)
    "...The day was quite eventful..."
    "With this running around the camp, with all this business, I was so tired that..."
    "With the last thought I fell asleep."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return
