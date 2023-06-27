label alt_day2_begin:
    scene black
    play ambience ambience_int_cabin_day fadein 3
    "I woke up from a creak…"
    "You know, a really melancholic one, really streeeetchy."
    "The one that you can only hear from a lazily stretching girl."
    "And I couldn't be a fool, missing this opportunity, could I?"
    "Of course, I immediately turned around, without getting out from under the blanket, and lifted it so that a smaaaaaall hole formed."
    "Didn't manage to see a lot."
    "But what I did see was more than enough for me!"
    mt "Semyon, if you keep sniffing like that, I'll think you're having a heart attack."
    "The squad leader smiled, without even looking in my direction."
    "Heart attack or not, but seeing a girl only in panties and a pioneer shirt fastened with two buttons — excuse me, that'll get anyone a stroke."
    "She sat cross-legged on the bed and, again, diligently recorded something into her diary."
    mt "Sleep, you still have half an hour before getting up."
    mt "Unless…"
    "For a brief moment I saw the exact same smile that Viola bestowed upon me on Olga's face."
    mt "You're getting up?"
    "Woefully sighing over the irretrievably deceased morning eroticism, I turned away and closed my eyelids.."
    play sound sfx_7dl["mpbt"]
    pause(1)
    scene bg int_house_of_mt_sunset
    with blind_l
    play music music_list["my_daily_life"]
    "The sun was shining directly into my face, forcing me to sneeze."
    stop sound
    "Wonderful awakening, if you ask me!"
    th "…seems like I fell asleep."
    th "Damn, missed such a scene!"
    if alt_day_binder != 1:
        "Of course, everything is relative, but yesterday, for example, I opened my eyes in an unfamiliar bus."
        "As if that wasn't enough, I slept in my winter clothes, sitting in the sun. Nothing wonderful in how I felt afterwards."
    else:
        "Anything is better than head-to-head docking - in the literal sense of the word."
        "And then, as a morning excercise for the brain - a verbal attack from a restless Japanese girl."
    "I stretched on the sheet and groaned blissfully - I managed to sleep well!"
    "Here… I don't know."
    "Room that looks like a room. There aren't that many changes comparing to yesterday."
    "I carefully looked around squad leader's bed:"
    scene bg int_house_of_mt_sunset:
        zoom 1.0 xalign 0.5 yalign 0.5
        linear 4.0 zoom 2.0 xalign 0.8 yalign 0.6
    "Olga Dmitrievna already ran off with her leader affairs, giving me a couple minutes to conduct another reconnaisance mission."
    "Jauntily tossed blanket, socks on the back at the head, and on the other side - a huge, large, beautiful and extremely voluminous item of lingerie."
    "So, that's what a true pioneer should strive for?"
    with fade
    "I wonder if she cleans here herself? Or makes the pioneers?"
    "Wouldn't want to be in the role of always on duty in the house."
    scene bg int_house_of_mt_sunset at zenterleft
    with dissolve
    "On the other hand, forcing a girl with whom you are not in a relationship to clean up after yourself… Doesn't feel right."
    "Anyways, time to get up. I lowered a leg onto the floor…"
    show mt normal pioneer far with dissolve
    extend " And immediately put it back under the covers - Olga Dmitrievna entered the room."
    mt "Rise and shine, Semyon!"
    mt "Overboard morning is beautiful, weather forecasters threaten us with 30 degrees during the day, so it's a sin to lie in bed for too long."
    mt "We have a very strict routine here, approved by the best specialists. Sleep for at least eight hours, fresh air and mass events - everything for you to properly gain strength!"
    me "Waking up at eight?"
    "I couldn't hide the horror in my voice."
    mt "What's wrong with that? {w}Normal time. Take a walk in the chilly morning, wash up, exercise, attend the lineup — and you're practically at the breakfast."
    mt "You won't go bored, I promise."
    "Of course."
    mt "That's yours."
    "She threw a bundle on my bed."
    "Judging by the specific smell of baby soap, I have just been loaned bath accessories."
    mt "Come on, get up."
    hide mt with dissolve
    "She disappeared behind the door, and I was already starting to get up…"
    show mt smile  pioneer far with dissolve
    extend " As she reappeared again."
    if alt_day_binder != 1:
        mt "Oh, I almost forgot: I took your old clothes to the laundry, they will be returned clean and ironed in the evening. They don't fit the weather anyways."
        me "What am…"
        if herc or loki or (dr and (counter_sl_7dl >= 1)):
            mt "Slavya already brought your uniform."
            mt "Check the closet, the set is hanging there."
            me "Well no, I'm…"
            mt "If you're talking about the contents of the pockets - it's in the same closet."
        else:
            mt "If you're talking about the contents of the pockets - everything is in the closet."
    else:
        mt "Oh yeah, just so you know - I already retrieved your old wet clothes from Slavya and sent them to the laundry."
        mt "The coat is in the closet."
        mt "Contents of the pockets are in the nightstand."
    "It seems that the concept of private property is dismissed here as a bourgeois prejudice."
    hide mt
    "She fluttered out of the room, finally giving me the opportunity to get dressed."
    if dr and (counter_sl_7dl == 0) and (alt_day_binder != 1):
        "Luckily, I was already geared up yesterday, so I got used to my stupid appearance a little."
        "It was only the tie causing problems, but I tied it with a simple double knot and calmed down on that."
    else:
        "A short sleeve shirt and short pants? Feel yourself like a toddler, heh."
        "The uniform was brand new, the shorts were not loose, the shirt creaked with starch, the tie shimmered with red."
        if alt_day_binder != 1:
            th "Yeah, right, I'll put this on and immediately turn into a defective copy of Electronik."
            th "At least he has such a face that makes all questions about his efficiency disappear."
            th "What am I supposed to do with my sad face? Give up?"
            dreamgirl "Well? Right! Let's wrap ourselves in a lap sheet and walk around like Roman patricians."
            dreamgirl "Or just flaunt your underwear on the streets?"
            dreamgirl "Yesterday you introduced people to denim, today to Calvin Klein — glory to public education!"
            "After five minutes of considering my options, I realized that the alternative to everything else would be to go outside in one of Olga Dmitrievna's swimsuits. Why not, actually?"
            "I took the shirt in my hands and closed my eyes for a moment from a whole scattering of sunbeams jumping from gilded buttons."
            "Touching it… Hmm… I am generally allergic to synthetics, and I sweat wildly and itch if I wear synthetic things for a long time - some tactile skills have already developed."
            "Well, to the touch it was pure cotton, without any polyester garbage."
            th "Nice! I remember that I had two such shirts, with gilded buttons - a parade-out, and with modest plastic circles - an ordinary one."
            "I don’t think that local customs are very different, in any case, I couldn’t see gold buttons on anyone I met."
            "What does it mean? Olga Dmitrievna played a big joke on me."
            "Pioneer camp with pioneer children and a troll on the position of squad leader."
            "Spectacular combination."
            "The shirt was pleasantly cool, and the short pants were surprisingly fitting."
            "I was taught how to tie a tie. Now I'll…"
            "With a single careful motion…"
            "A tangled shapeless lump flew onto an unmade bed."
            me "Screw you!"
            "I made the bed, hanging the cunning red knot on the back of the bed, and left the house."
        else:
            "Yesterday I didn’t have too many alternatives to uniform - thanks to the red terrorist, I got completely soaked."
            th "And today…"
            th "Yup, no choice today either."
            "I sighed and began dressing."
            "True, the counselor changed the shirt from a daily one to formal, with gilded buttons."
            "I'm not picky, that'll do."
            "The recalcitrant tie did not want to be tied, so I gladly said goodbye to him and went outside."
    play sound sfx_open_dooor_campus_1
    pause(2)
    play sound sfx_close_door_campus_1
    scene bg ext_house_of_mt_sunset
    show mt smile pioneer
    with fade
    "Olga Dmitrievna was already waiting for me at the door."
    if alt_day_binder != 1:
        mt "Look, the washbasins are there. Wash up, and then go to the square."
    else:
        mt "Remember where the washbasins are? Go there, and then to the square."
    me "Square? Why?"
    mt "Mor-{w=0.2}ning {w=0.2}ex-{w=0.2}er-{w=0.2}cise!"
    mt "Exercising is necessary. A pioneer must always look good and be in shape!"
    me "Uhh… Whatever you say."
    hide mt with dissolve
    stop ambience
    scene bg ext_houses_sunset with dissolve
    "I shrugged my shoulders and trudged towards the washbasins, feeling her scrutinizing gaze with my shoulder blades."
    "She clearly knows something. You just need to spin her up into a conversation. But how?"
    if dr and (counter_sl_7dl == 0) and (alt_day_binder != 1):
        mt "Semyon, what is that abomination on your neck?"
        show mt normal pioneer with dspr
        me "Uh… A tie?"
    else:
        mt "Semyon! Where's your tie?"
        me "In the room. I'm not voluntarily putting on this noose."
        mt "Semyon, you have to. They won't let you in without a tie."
        scene bg ext_house_of_mt_sunset at zenterleft
        show mt normal pioneer
        with pushleft
        "I stopped and turned around."
        me "Even to the washbasins?"
        show mt laugh pioneer with dspr
        mt "Into the canteen - definitely."
    mt "You don't know how to tie a tie?"
    me "Somehow I didn't have to before."
    show mt surprise pioneer with dspr
    "I noticed the strange look she gave me and hastened to continue."
    me "Always wore ones with clasps!"
    show mt normal pioneer with dspr
    "She nodded."
    mt "It's okay, I'll teach you."
    mt "Go wash up, I'll wait for you here, then we'll go for exercises together."
    me "Looking forward to it."
    "I let in a little poison into my voice."
    scene bg ext_houses_sunset with dissolve
    mt "Are you angry because of the clothes?"
    mt "I, as the squad leader, couldn't just leave them dirty. Don't tell me I was supposed to wash them myself!"
    "I did not answer and turned behind the closest house - there was the path in the direction of a sadistic attraction with ice water and wobbly sinks."
    if alt_day1_cofront_sl_dv == 1:
        sl "Hello!"
        "A familiar voice came from behind."
        me "Morning…"
        show sl smile sport with dspr
        "I answered cautiously."
        th "She looks suspiciously content with life."
        if alt_day1_sl_keys_took == 2:
            th "Olga still hasn't given her the keys back along with a preventive lecture?"
        else:
            th "Haven't found the missing keys yet?"
        sl "What's up?"
        "I eloquently jerked my shoulder, from which the towel hung."
        me "Going jaw scrubbing."
        sl "Would you like to run with me? Since it's boring alone!"
        th "Not again…"
        "We barely got even yesterday, and she's trying to put me into debt again."
        "It seems like a beautiful girl has condescended to co-working, and now I should feel obligated."
        me "No, thanks."
        "I answered as politely as possible."
        sl "Shame! It's more fun together."
        me "Sorry, sport just isn't my thing."
        sl "Oh, okay then!"
        sl "See you at the square then!"
        hide sl with easeoutleft
        "And she ran off to somewhere."
        "I immediately felt more comfortable and relaxed."
        "There's something wrong behind her beautiful facade, I can feel it!"
    scene bg ext_washstand_day with dissolve
    "To be honest, I still don’t understand what’s the point of washing with ice water in the morning and in the evening, when you dip your hot limbs into ice, and your airways take on the size of a geometric point."
    "But as far as I know, no one has ever caught a cold in this way."
    "I guess the camp builders knew something I didn't."
    "Olga Dmitrievna, it seems, also knew something, since I was already seriously wondering what it would be like to wash my feet here in the evening."
    show blink
    pause(3)
    scene bg ext_washstand_day
    with dissolve
    "Wait. Hold up."
    "What legs? I was planning on leaving here!"
    dreamgirl "Uh-huh. Especially now, with clothes in laundry, dressed up like a textbook clown, except perhaps without the nose, you'll go very far and definitely achieve a lot."
    dreamgirl "Then it will turn out that there is no transport connection here, and it's half a thousand kilometers to the nearest settlement."
    "We'll have to put up with it, at least for this day. And then, just get to the clothes!"
    if alt_day_binder != 1:
        "The view was expected: several sink-fountains in the outskirts so that the pioneers do not arrange an unprompted day of Neptune, a row of taps in the center for those who wash themselves and a parallel row for everyone who wants to wet their feet."
    else:
        "Nothing changed since yesterday: several sink-fountains in the outskirts so that the pioneers do not arrange an unprompted day of Neptune, a row of taps in the center for those who wash themselves and a parallel row for everyone who wants to wet their feet."
    scene bg ext_washstand2_day at zentercenter
    with dissolve2
    play sound sfx_open_water_sink
    pause(1)
    play sound_loop sfx_water_sink_stream
    "I turned the valve, having prepared in advance for the fact that the water would be cold, and… The water that poured down wasn't cold, it was practically frozen!"
    me "A-a-a-a-a!" with hpunch
    "I generously splashed my face with ice and yelled again."
    "The scalding cold water took my breath away, and my teeth seemed to creak on their own."
    "But I achieved the effect - the world around seemed to be wiped with a damp cloth, the picture acquired contrast and some depth and clarity that was inaccessible before."
    "Whatever's pouring from the tap in my apartment doesn't hold a candle to this nightmare!"
    "Trying to move as quickly as possible, I took out soap from the package and quickly lathered my palms, then my face - in contrast to the water, the touch seemed hot."
    "A few moments later, and…"
    me "A-a-a-a!" with vpunch
    "It was only one handful, and you need three. At least."
    "Fingers already palpably cramped from the cold."
    th "At least one more!"
    me "A-a-a-agh!" with hpunch
    "The cold took my breath away again."
    "Here it is, a clear example of how much the party loves the younger generation. Everything for kids! Especially cold water."
    "With my teeth chattering, I reached into the package and took out a toothbrush, and a few moments later, a round plastic jar of toothpowder."
    me "Powder! I haven't seen anything like this in a very long time."
    "What is sold now in cosmetics, of course, is close in composition. But this smell…"
    "The further I got, the more I believed that this camp truly was a pioneer one."
    "Scooping up a little with a brush, I sent the abrasive into my mouth, trying not to think about what the rinse would turn into after brushing.."
    "From the ice water the teeth got crumpled, and frankly, in some places it actually hurt."
    th "Whatever, with the powder all problems will disappear on the way."
    stop sound_loop
    play sound sfx_close_water_sink
    pause(1)
    scene bg ext_house_of_mt_sunset at zentercenter
    show mt smile sport
    with fade
    "Throwing bath accessories into the house, I looked inquiringly at the squad leader."
    "She has already changed into some kind of sports uniform, but it looks like I will have to walk like a dumbass all day in a shirt with gold buttons."
    mt "Ready to exercise?"
    "She joyfully asked."
    me "Uh... No?"
    mt "Start running!"
    "She rushed towards the square, and I had no choice but to follow her."
    scene bg ext_square_sunset with dissolve
    "The square was already crowded. My squad almost fully gathered here, some completely unfamiliar guys were also visible. Although I immediately recognized the formation type."
    "Crowd against a leader, the usual for mass exercising."
    "Who would be the leader?"
    "Definitely not Olga."
    show sl smile sport with dissolve
    "The answer ran past me, flashing bare tanned calves."
    "She walked through the crowd and stood in front of us, feet shoulder-width apart, palms at her sides."
    th "Our activist, who else."
    "She studied the audience for a second, nodded to me, meeting my eyes, and raised her right hand in a pioneer salute:"
    sl "Good morning!"
    "The crowd muttered something incoherent in response and straightened up. Morning exercise started."
    "The same exercise I did roughly 20 years ago… Practically without any changes."
    "I allowed my body to remember all the swings with turns, and in the meantime I was looking for familiar faces."
    "Slavya rapturously exercised, enjoying the movements themselves, rejoicing in the sun and new day."
    hide sl
    show un normal sport far at cleft
    with dissolve
    "Lena waved her hands with restraint and generally kept aloof. Expected behaviour."
    hide un
    show us smile sport at fright
    with dissolve
    "Ulyana, on the other hand, exercised with such speed and vigor, that it seemed like she was going to fly straight up."
    show us grin sport with dspr
    "Seeing that I was looking at her, she stopped for a second and stuck out her tongue."
    hide us
    show dv sad sport at left
    with dissolve
    "Alisa frankly did not get enough sleep: for each swing of her hands, she answered with one stable yawn."
    if alt_day1_me_d3_dv_feed:
        "No doubt, she drank kefir all night!"
    elif (alt_day_binder != 1) and (counter_sl_7dl < 2):
        "Perhaps didn't believe me? Came back to check how things were going in the canteen?"
    show dv normal sport with dspr
    "Catching my eye, she shook her chin in greeting and retreated into herself."
    hide dv with dspr
    th "Nothing unusual, honestly."
    "I thought, waving my limbs, leaning in different directions and twisting my pelvis."
    th "All exercises are familiar, easy to do… Why don't people like exercising?"
    "I could be understood, euphoria was speaking in me."
    "I honestly expected that my dystonia would now break out, freeze my fingers, dizzy and darken my eyes, but the body turned out to be young and strong."
    "You could say that it did the exercises with pleasure."
    "Although I'm not sure if it's a pleasure I'd like to repeat."
    "After the sit-ups, those who wished ran away for a run, and a few minutes later Olga Dmitrievna approached me."
    "She already changed for the lineup."
    show mt smile pioneer with moveinleft
    mt "How do you like the start of a new day?"
    me "Seen better ones."
    mt "Oh, don't freak out. You'll love it here, just give us a chance and don't mind any bullies."
    th "As if anyone asked me."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_lineup:
    scene bg ext_square_sunset with dissolve
    play music music_list["get_to_know_me_better"] fadein 5
    "Someone took me by the elbow."
    scene bg ext_square_sunset at zenterright
    show sl smile pioneer at cright
    with dissolve
    "Slavya. Who has already inexplicably changed."
    sl "Let's go."
    me "Where?"
    show sl laugh pioneer with dspr
    sl "What do you mean «where»?"
    sl "Time for the lineup, we need to take our place."
    me "And why is this place bad?"
    sl "Because it's not ours!"
    scene cg d2_lineup
    with dissolve
    "She took me a few meters to the right, almost to the very podium, and stretched out into the front. Involuntarily, I followed her example, standing in a line next to her."
    "Having tried for a second to imagine myself as a real pioneer, I suffered a crushing defeat - my mind slipped and refused to see me in a permanent tie and shirt."
    "God, even when I worked in the office — I couldn't bring myself to take my sweater off."
    "This is not counting the fact that I'm too old to be one."
    "Willy-nilly, thoughts switched to much more pleasant matters."
    "I glanced sideways at Slavya, who was standing next to me."
    "This girl… She had already changed, but I remember her wearing her black uniform with white piping."
    "And her usual uniform, for that matter."
    "Hell, you could probably dress her in a coat and she'd still look great."
    "I was daydreaming a little, imagining Slavya, dressed in a long fitted fur coat with a hood, and then I was gently poked in the side."
    sl "Wake up, our turn."
    me "What?! What turn?!"
    sl "Let's go."
    "I literally felt the eyes of everyone around focus on me. It made my throat dry, and my legs became wooden."
    "The crowd itself is a pretty bad thing, but to be in the focus of its attention…"
    scene bg ext_square_sunset at zentercenter
    show sl normal pioneer at cright
    show mt normal  pioneer at cleft
    with dissolve
    "Fortunately, Slavya did not care about such things at all. She took me under the podium and left me there, and she herself went to the center of the square, where a lowered flag was already hanging on the flagpole."
    mt "I want to introduce you to a new member of our friendly family."
    "Olga Dmitrievna's voice, professionally staged, carried over the square without any equipment, blocking all the noise."
    mt "Semyon!"
    "I think I blushed."
    show sl serious pioneer with dspr
    "Or paled."
    "I don't know exactly. But something definitely happened to my face, as Slavya threw an alarmed look over her shoulder."
    mt "Semyon arrived at the camp only yesterday, and as the last guest, he receives the most attention. Therefore, today he raises the flag with Slavya."
    "I stood there, unable to move or even breathe properly. I was literally paralyzed."
    show mt normal  pioneer at cleft with dspr
    mt "What's wrong, go."
    show sl normal pioneer at cright with dspr
    "I continued to stand, completely frostbitten."
    ml "He doesn't want to!"
    "There was a cry from the crowd. Boyish voice, hardly anyone I know."
    ml "Let me do it instead of him."
    mt "There will be no substitutions. Semyon just needs a little more time."
    "That's true. About the time, I mean."
    "Vanishing so that nobody could find me would be even better."
    "Lord almighty, they're all staring!"
    "Don't they understand that I wouldn't move?! Turn around!"
    hide mt with fade
    "Fortunately, the ability to breathe has already returned to me, and after it the ability to move. I took two steps to the flagpole."
    sl "Come on, you raise it halfway, and then I'll continue."
    show sl smile2 pioneer at cright with dspr
    "Slavya reassuringly smiled at me."
    "I felt a sharp attack of gratitude and some kind of tenderness for this girl."
    dreamgirl "It's called Stockholm syndrome. And in ordinary life, you would run away after half an hour of knowing her."
    "And yet, I didn’t want to behave like a pig with a person who supports you simply because… Because she just can!"
    "So I shut up my inner skeptic and took hold of the steel cable."
    me "Alright."
    "The grease-coated wheels sang, spinning, and the cable went up, lifting the scarlet cloth, higher and higher, forcing you to raise your head after it, until only the sky and the flag remained in sight."
    hide sl with moveoutright
    "I stepped aside - we got to the middle of the mast - and the ascent continued."
    "This is the magic of the flag: when it goes up, everyone is watching. Even those who don't like it or frankly do not respect."
    "I saw how Dvachevskaya's nose turned up, how Ulyanka raised her chin, even the squad from which the last shout came - all unanimously followed the rising banner with their eyes."
    "And, finally, the peak."
    play sound sfx_7dl["eat_horn"] fadein 1
    "As if anticipating this, the tin horn blared the horn call sacred to any hungry pioneer."
    play ambience ambience_camp_center_evening fadein 1
    "Pioneers simultaneously turned right, and, after receiving Olga's go-ahead, moved in an organized formation towards food."
    "I almost followed them, but…"
    mt "And you, Semyon, I will ask you to stay."
    scene bg ext_square_sunset at enterleft
    show sl smile2 pioneer at right with moveinright
    show mt normal pioneer at cleft with dspr
    th "Can't have a day without surprises."
    stop music fadeout 3
    "I was still a little shaky after that nightmare, but I courageously pretended that everything was fine."
    "Although it didn't seem to work on Slavya. She looked at me puzzled and asked in a low voice:"
    sl "Olga Dmitrievna, maybe later…"
    mt "No «laters», he already lost a lot of time."
    sl "But he can barely stand on his feet, let me take him to the nurse?"
    mt "He'll get there on the way."
    "Olga cut her off."
    mt "In any case, getting to know the camp is required!"
    "Taking out a lined piece of paper from her pocket, the squad leader handed it to me."
    menu:
        "Slavya, will you accompany me?" if counter_sl_7dl == 2:
            $ lp_sl += 1
            $ karma += 10
            $ counter_sl_7dl = 3
            show sl grin pioneer with dissolve
            "Slavya winked at me."
            sl "Why not? {w}We'll start with the nurse."
            me "Uh… yeah. The nurse."
            sl "Olga Dmitrievna?"
            "The squad leader suspiciously eyed us both, then slowly nodded."
            mt "If you want to voluntarily escort him — I won't interfere."
            mt "But this does not exempt you from cleaning the square."
            show sl happy pioneer with dspr
            sl "It's okay, Semyon will help me. Isn't that right?"
            "The «clean up square in exchange for a beautiful girl accompanying you» deal looked fair enough to me."
            sl "Then give me the checklist, it'll be safer with me."
            "This, too, had to be accepted."
            "Beauty requires sacrifices!"
        "And what the hell is this?" if loki:
            me "A notice for a potato unloading shift?"
            "I folded my arms on my chest - the nerves slowly calmed down."
            me "Or have you already found me a job?"
            show mt smile pioneer with dspr
            mt "Walking around the camp, yeah."
            "She unfolded the paper:"
            mt "Look, there are several lines that you need to fill.."
            me "Where's the «go back to sleep» line?"
            mt "Will show up after lunch. And if you keep being rude, you'll have to cook said lunch, understood?"
            "I shrugged my shoulders and reluctantly took the paper."
            $ lp_dv += 2
            $ lp_us += 1
            $ karma -= 15
            "Two voices burst out behind me, and when I turned to look, something flashed in the direction of the canteen."
            "Something… red."
        "Visit and get the signatures. Got that" if not loki:
            $ lp_sl += 1
            sl "Oh, so you don't need an explanation?"
            show sl smile pioneer with dspr
            "The girl was delighted."
            me "Yeah, generally I'm not an imbecile, I understand a few things."
            "The experience of traveling to different camps quite nicely broadened the horizons in this regard."
            mt "There are four lines, but, of course, there are much more places."
            mt "You have to figure out what is most important to you, because you can’t do everything at once."
            "I glanced towards Slavya."
            show mt laugh pioneer with dspr
            mt "No, she doesn't do everything, despite how that looks."
            show sl smile2 pioneer with dspr
            sl "To be honest, I almost don’t go to clubs at all - I just don’t have time."
        "Everything was going so well…":
            show sl sad pioneer with dspr
            sl "Still feeling under the weather?"
            "Slavya threw a sidelong glance at Olga."
            me "Nobody has ever died from this."
            mt "That's right! {w}Walk around, you'll get better."
            "I was willing to bet that these two get along great in my absence."
            "And for some reason I became their stumbling block."
            mt "Feoktistova, stop looking at me like that — if you're that worried, you can personally accompany him."
            show sl serious pioneer with dspr
            sl "You know that I don't have the time for that…"
            show mt laugh pioneer with dspr
            mt "Yeah? Then you better decide what's more important — wiping newcomer's snot or doing something actually important."
            sl "I…"
            "She pondered."
            $ lp_dv += 1
        "Can I ask a question?" if herc:
            $ karma += 20
            "Olga nodded:"
            mt "Yeah?"
            me "Do I need to sign up anywhere, or do I just need to see everything on the territory?"
            mt "I want you to sign up!"
            if lp_sl >= 5:
                me "And if I want to help Slavya?"
                mt "Then you'll be helping Slavya!"
                show mt laugh pioneer with dspr
                sl "But if I’ll notice you shirking - I’ll write you off to a macrame club, just so you know."
            else:
                mt "I'm not just letting you walk around the territory for no reason!"
                "I had no intention of being on the territory beyond what was necessary."
                "But they didn't have to know that, did they?"
    if counter_sl_7dl != 3:
        show mt normal pioneer at center with dspr
        mt "One more thing: don't go alone - you'll walk longer."
        mt "Or should I get you a guide?"
        mt "Electronik, come over here."
        if alt_day_binder != 1:
            me "Aaaaagh!"
            "I grabbed my head."
            th "Not this guy again!"
        show el normal pioneer at fleft behind mt with dissolve
        el "Yes, Olga Dmitrievna?"
        "He held his hand out, which I successfully ignored."
        mt "Will you guide Semyon across the camp?"
        show el smile pioneer far with dspr
        el "Sure thing! Yesterday I…{w=.5}{nw}"
        me "Can I please decide on my guide myself?"
        "I asked very politely."
        me "Please."
        show mt surprise pioneer with dspr
        mt "Fine, if you say so. If you manage to convince anyone else - so be it."
        mt "Or maybe you'll do fine with Electronik?"
        me "No!"
        show mt smile pioneer with dspr
        mt "Alright, alright, go with whoever you manage to convince."
    mt "Oh and don't forget to visit the library - take a look at our resident artist."
    me "Why would I do that?"
    mt "A pioneer must develop a sense of beauty."
    "I shrugged and headed towards the canteen."
    stop sound fadeout 3
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_bf:
    play ambience ambience_dining_hall_full fadein 3
    play music music_list["everyday_theme"] fadein 5
    scene bg int_dining_hall_people_sunset_7dl with fade
    "Breakfast isn't any different from supper."
    "Although the pioneers buzzed noticeably quieter and sat noticeably more crowded."
    if alt_day_binder == 1:
        "Near the redheads, I noticed yesterday's polite girl."
        "She met my stare and smiled."
        "Fine, let her smile, as long as she doesn't start talking."
    "I looked for a free spot."
    "There were three such places at the tables of our squad: next to Slavya, opposite of Lena and in the corner by the window."
    if alt_day_binder == 1:
        "And also near the redheads. I didn't consider this option, period."
    menu:
        "Sit with Slavya":
            play music music_list["she_is_kind"] fadein 3
            $ alt_day2_bf = 'sl'
            $ lp_sl += 1
            scene bg int_dining_hall_people_sunset_7dl at zenterright
            show sl normal pioneer
            with dissolve
            "I noticed a couple of empty seats nearby and looked inquiringly at Slavya."
            show sl smile pioneer with dspr
            "The girl smiled and nodded."
            "Alrighty then. Feels nice when you're understood at a glance."
            "We had to leave for a second to drive away the attempting pioneers, and five minutes later we sat down at the window."
            "Breakfast like breakfast. Herculean porridge, gluetinous… Sweet! A couple of slices of white bread, butter, sausage plus cocoa."
            "Immediately setting the plate aside I glued my eyes to the glass."
            th "Real soviet cocoa! It's…"
            "And a second later, with a sigh of disappointment, I put down the glass."
            th "These… These… I don't even know which words to use! They screwed cocoa up by adding condensed milk! What the hell, man!"
            show sl smile2 pioneer with dspr
            "Slavya, who was watching my evolution from the sidelines, giggled quietly, seeing the abyss of disappointment on my face."
            sl "We banned it. After several people got allergies. That's why they dilute it now."
            "Uh-huh. As if that'll remove the allergen."
            "Cocoa is cocoa: you're either allergic to it, or you aren't. How the hell does condensed milk relate to this?"
            "I did not share my conclusions with Slavya, burying myself in a plate of porridge, especially since hers was already almost empty, and I also wanted to ask a number of questions."
            show sl normal pioneer with dspr
            sl "How's your first night?"
            "She asked, licking the spoon."
            "I hastily swallowed a lump of porridge."
            me "Don't remember anything, head hurts…"
            "I smirked."
            me "But it probably was fine - fresh air, nature, people…"
            sl "Yeah, I could see that. Yesterday you looked exhausted. And today a blush has already appeared on the cheeks, definitely not a shame to show you to people."
            me "You were going to show me to people?"
            show sl laugh pioneer with flash
            "I did not believe my ears, and Slavya laughed:"
            if (counter_sl_7dl <= 2):
                sl "Running around with a checklist doesn't count?"
                me "I was thinking more like an event of sorts…"
                show sl smile2 pioneer with dspr
                sl "Some sort of rout? Ball?"
                sl "Actually, tomorrow there will be disco, and…"
            else:
                sl "Of course I was going to! At least I'll take you to the square, and then we'll choose where to go first. And I still have to clean up there."
                "She was silent for a while, savoring the ungodly cocoa."
                "I also fell into my thoughts."
                scene black with fade2
                sl "…dancing! But we don't have many boys here, and slow dances are rare." with hpunch
                scene bg int_dining_hall_people_sunset_7dl at zenterright
                show sl shy pioneer
                show unblink
                with dissolve
                "Huh, she was saying something!"

            "Slavya lowered her eyes, then quickly looked at me, then lowered them back."
            sl "Maybe… You…"
            "I have already spoken about the direct Slavya, athletic, purposeful…"
            "And now I have a unique opportunity to meet Slavya… I don't even know.{w} Flirty?"
            if counter_sl_7dl > 1:
                "Just not like before."
            th "That's true. What is she, a robot or something?"
            if herc or loki:
                me "Alright. When's the ball?"
                if (counter_sl_7dl <= 2):
                    sl "Tomorrow!"
                else:
                    sl "I'm telling you, tomorrow!"

                me "That's it. {w}Consider yourself invited - you did ask for a dance with me."
                "I thought for a bit."
                me "But only a slow one! I don't get these paired fast dances of yourself!"
                sl "A slow one, yeah."
            else:
                me "I don't like dancing too much. And my dancing skills are…"
                sl "Come along anyways! It'll be fun, you'll see."
                me "Okay… I… I'll think."
                "I was embarrassed again and turned away under her searching gaze."
            "The rest of breakfast passed quickly, crumpled and silent."
        "Sit alone":
            scene
            $ renpy.show("bg int_dining_hall_people_sunset_7dl", at_list = [zentercenter], what = Noir("bg int_dining_hall_people_sunset_7dl", brightness = -0.4, saturation = -0.4))
            $ alt_day2_bf = 'me'
            "I ate in the shortest amount of time. There is no time to waste, gotta explore this place!"
        "Take the risk and sit with redheads" if alt_day_binder == 1:
            $ alt_day2_bf = 'dv_us'
            play music music_list["i_want_to_play"] fadein 1
            $ lp_dv += 1
            $ lp_us += 1
            scene
            $ renpy.show("bg int_dining_hall_people_sunset_7dl", at_list = [zenterleft], what = Noon("bg int_dining_hall_people_sunset_7dl"))
            show us smile pioneer at cleft
            with blind_l
            if alt_day1_me_d3_us_robbed:
                "Ulyanka winked at me and broke into a friendly smile:"
                us "Hey, newbie!"
            "I cautiously glanced at her and covered the plate with my elbow."
            "Hmm, I feel like I'll get a couple of good habits here."
            $ renpy.show("bg int_dining_hall_people_sunset_7dl", at_list = [enterright], what = Noon("bg int_dining_hall_people_sunset_7dl"))
            show us smile pioneer at left with moveinleft
            show dv grin pioneer2 at right
            with dissolve
            "Alisa jumped up - that polite girl with whom I had hoped to eat has left."
            "And sat down, surrounding me from the other side."
            dv "Why so serious?"
            "The redheads simultaneously nudged me and laughed as I let out a strangled moan."
            show us grin pioneer with dspr
            us "You seem smart enough."
            us "Wanna come with us?"
            me "With you?"
            "I knew both of them for less than a day, but this time was enough for me to guess."
            "Definitely should stay away from them."
            show dv laugh pioneer2 with dspr
            dv "Nah, he won't do - he doesn't have any guts after all!"
            me "Excuse me?"
            dv "You think I didn't see how you hung out with an activist at the canteen yesterday?"
            dv "And then you went in…"
            show dv shocked pioneer2 with dspr
            dv "Did you…"
            me "Stop."
            if alt_day1_me_d3_dv_feed:
                me "In case you suddenly forgot, after this, as you said, 'hunging out', I brought you something to eat!"
                show dv grin pioneer2 with dspr
                dv "Damn, you're dangerous!"
                show us laugh pioneer with dspr
                us "You hear that?"
                show us surp1 pioneer with dspr
                "She covered her nose and mocked me in a nasal tone:"
                us "As you said, if you suddenly forgot to bring food!"
            else:
                show dv grin pioneer with dspr
                dv "No way! How can you run to Olga Dmitrievna to complain then, how the girls offended you, called you bad words."
            me "Are you done?"
            "I asked politely."
            show us normal pioneer with dissolve
            us "Why do you ask?"
            me "No reason."
            "I twisted the plate on the table - there was still half the portion left in it."
            me "In case you aren't, I'll split this plate between both of your heads."
            play sound sfx_punch_medium
            with vpunch
            dv "Oh, he's pretty good!"
            "Alisa concluded."
            dv "Although a bit dumb."
            us "That's alright, I'll work on him."
            "They got up and left me alone."
            hide us
            hide dv
            with flash
            "Left me alone."
            "With porridge dripping down my neck."
            "Little shits."
            "How fortunate it is, that I'm a vengeful son of a bitch!"
            "Not a single bastard dodged!"
        "Sit with Lena":
            play music music_7dl["take_my_hand"] fadein 1
            $ lp_un += 1
            $ alt_day2_bf = 'un'
            if alt_day1_un != 0:
                "After yesterday's conversation, I thought that Lena was not completely disgusted with me."
                "Or well, I hoped it was that way."
            else:
                "Yesterday I didn’t have the courage to come up and say hello - I tell you what."
                "Maybe I'll work something out today."
            "I occupied a table and began waiting for an opportune moment."

            show un normal pioneer at center
            with dissolve
            "The seat across from her was empty, so I figured nothing bad would happen if I sat down."
            me "May I?"
            "She nodded without looking up from her meal."
            if lp_un < 2:
                show un normal pioneer with dissolve
                "Complete illusion of neglect."
                "Just in case, I even looked at my hand in the light - what if it suddenly became transparent?"
                "Didn't seem like it."
                me "Bon appetit?"
                "Another nod."
            else:
                show un shy pioneer with dissolve
                "Her cheeks lit up at the same time."
                me "Bon appetit?"
                show un smile pioneer with dissolve
                un "Thank you. You too."
                me "How was your sleep?"
                un "Uhhh… Wonderful."
                show un shy pioneer with dissolve
                "She got embarrassed again, and I tried not to think what could be the reason for this."
                me "I've had a great sleep too."
            "I didn't get a lot, limited myself to a couple of sandwiches and a cup of nasty cocoa."
            "Such a breakfast didn't stop me from talking."
            show un normal pioneer with dspr
            "Actually, I didn't eat so much as I stared."
            "There was something in Lena that made you, if not admire, then at least… I don't know. Smile at her, I guess."
            "This downtrodden look, this modesty, growing into an icy alienation…"
            "I've seen her look at people with that look. It doesn't have anything — {w}only green emptiness."
            "A familiar look. Familiar discrete behavior, when we are cheerful and playful with loved ones, and on the street we represent the front of a high-voltage shield."
            show un shy pioneer with dspr
            un "You look like…"
            "She looked inquisitively into my eyes, but immediately blushed."
            "Her gaze jumped embarrassedly along the walls, the table, the plates - anything, as long as it wasn't me."
            me "Like?"
            "She wiggled her fingers, searching for a definition."
            un "Strange…"
            me "I have very few friends here. Or rather, almost none. Only names…{w} However, I'm not ready to discuss this topic yet."
            show un surprise pioneer with dspr
            un "Why?"
            me "What do you mean why?"
            un "Why don't you want to discuss it?"
            me "Too heavy of a topic for breakfast."
            show un smile pioneer with dspr
            "I smiled."
            me "Let's discuss something else."
            me "For example, {i}you{/i}."
            show un shy pioneer with dspr
            "Lena looked at me in bewilderment."
            un "Me? What's there to discuss about me?"
            me "What, there really isn't anything?"
            "In response, she got embarrassed again and hid behind a cup of cocoa."
            "How long ago was it that you yourself sat on the other side of the barricades and mentally cursed those who are unable to read an elementary non-verbal sign «Screw off»!"
            "And now you! Yourself! Impose on her! The hell's wrong with you?!"
            un "…and what do you want to know?"
            "Finally, she realized that I wouldn’t leave her just like that, and decided that it’s easier to give the impudent what he asks for, rather than to explain why not."
            me "Oh, sorry. You don't have to answer such questions. Especially since we practically don't know each other…"
            show un normal pioneer at center
            with dspr
            un "Well, n-no… Everything's…"
            "She put her half-eaten breakfast on a tray and got up."
            show un shy pioneer with dspr
            un "I need to go. See you."
            me "See you…"
            hide un
            with dissolve
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_un_guide:
    scene bg ext_dining_hall_near_day with fade
    with dissolve
    play music music_list["so_good_to_be_careless"] fadein 1
    play sound_loop ambience_medium_crowd_outdoors fadein 2
    $ alt_day2_convoy = 'un'
    if herc:
        if alt_day2_bf == 'un':
            "She finished breakfast before me, and I had to hurry up a lot to catch up with her."
            "After all, I did ask her yesterday…"
            "And I definitely wanted to hear an answer!"
        "After breakfast, the girl was wandering to somewhere, looking thoughtfully at her feet, and I had to stomp louder than usual so as not to frighten her."
        show un normal pioneer with dissolve
        if alt_day2_bf == 'un':
            me "Look, I'm sorry if I said something wrong there at breakfast."
            me "I understand that I'm intrusive and clingy. I don't like people like that myself, if it comes to that. It's just…"
            un "You're not intrusive."
            me "Really? It looked like…"
            un "It's okay. I just don't really know what to say about myself."
        else:
            me "Hello!"
            un "G-good morning."
        "Today she looked much more confident than yesterday. In any case, I failed to see yesterday's expression of inexplicable fear in her eyes."
        "And that means…"
        me "I'm here about my yesterday's offer."
        me "Did you make a decision?"
        "She nodded."
        un "Yes, I think I can show you around the camp."
    elif loki:
        "I sat on the steel railing of canteen's porch and waited for Lena."
        th "She promised to think about my offer. Maybe she will agree? You never know."
        show un normal pioneer far with dissolve
        "Finally the door opened and she stepped out."
        "I hurried to jump off my perch and approached her."
        if alt_day2_bf == 'un':
            show un normal pioneer with dissolve
            me "Look, I'm sorry if I said something stupid at breakfast."
            me "I don't know what came over me. Let's try again, and this time I'll try to be less pushy."
            show un smile pioneer with dspr
            un "You aren't pushy."
            me "Really? I thought…"
            un "Really."
        else:
            show un normal pioneer with dissolve
            me "Hello, beautiful!"
            "I smiled."
            show un shy pioneer with dspr
            un "G-good morning."
        "Today she looked much more confident than yesterday. In any case, the indifferent cold, which frightened me so much yesterday, seemed to have disappeared.."
        "And that means…"
        me "Did you think about my proposal?"
        show un grin pioneer close with dspr
        "She lowered her eyes for a few seconds, and when she raised them…"
        show un smile3 pioneer close with dspr
        "They had no more shyness or indecisiveness."
        "She stood next to me and found my hand with hers."
        show un smile2 pioneer close with dspr
        un "What a nice day today."
        "I was lost for a few seconds at the sudden change in the girl's behavior, and she impatiently pulled my hand."
        show un laugh pioneer close with dspr
        un "Let's go!"
    else:
        "After breakfast Lena found me on her own."
        show un normal pioneer with dissolve
        me "Hello!"
        "I smiled."
        "She didn't reply, but stared intently into my face for a few seconds. Almost like Slavya yesterday."
        "And when I was already starting to get nervous, she suddenly asked in a very adult voice:"
        un "Y-yesterday, w-were you serious…"
        show un shy pioneer with dspr
        "She hasn't finished the thought."
        "Seriously - what? I arrived? Invited you to walk around the camp? Hit my foot?"
        "I can't stand unfinished thoughts."
        "She was waiting for an answer, blushing more and more."
        "And I wasn't feeling any better myself."
        "I don’t know what came over me - either the drunken night air, or a good mood…"
        "To simply invite a girl to an improvised date, but a date after all…"
        "Lena stood and waited for an answer, and suddenly I ran out of air in my lungs once more, it all just went to cool my flaming cheeks."
        "I didn't even have any strength to nod."
        hide un with dissolve
        "Lena sighed softly and turned around, almost left, when my suddenly stupor finally ended."
        me "Yes."
        "I quietly said, looking at her back."
        me "It's hard for me to communicate face to face, but I really want you to keep me company."
        show un grin pioneer with dissolve
        "She stopped at the door."
        un "Then let's go."
        "Said she and went outside."
        "As expected, she didn't even look at me."
        hide un with dissolve
    stop sound_loop fadeout 7
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_convoy:
    scene bg ext_dining_hall_near_day with fade
    with dissolve
    play music music_list["so_good_to_be_careless"] fadein 1
    play ambience ambience_camp_center_evening fadein 5
    if alt_day2_un_rej_convoy:
        "After an unsuccessful attempt to find a guide, I thought that I still had nothing to lose, so without much thought I chose who I would go with."
        "The obvious choice…"
    else:
        "I thought about who could be taken as a guide."
        if alt_day_binder == 1:
            "It is quite obvious that neither Ulyana nor that girl from infirmary (by the way, I still need to meet her!) weren't suitable for this role."
            "Who would it be then?"
        else:
            "Yesterday's tour with Electronik was completely useless in terms of getting to know the camp."
    menu:
        "Slavya":
            if alt_day2_un_rej_convoy:
                "Having received a reasonable refusal, I decided to try my luck with Slavya."
            else:
                "After a little thought, I settled on Slavya."
            "After all, she's the activist here, she probably knows a lot."
            if alt_day1_sl_keys_took == 1:
                "And I can hand over her keys while I'm at it."
            scene bg ext_dining_hall_near_day with fade
            "I intercepted the girl exiting the canteen."
            show sl normal pioneer
            me "Hello again!"
            sl "Hey!"
            me "Slavya, are you currently busy?"
            sl "Right now - no, not really. What did you want?"
            me "Do you want to walk around the camp? Show the new guy where everything is?"
            if lp_sl >= 5:
                $ lp_sl += 1
                $ lp_un -= 1
                $ lp_dv -= 1
                show sl sad pioneer with dspr
                sl "You see… There's a small problem."
                "Slavya suddenly got sad."
                sl "I would love to, but I still have to clean up the square."
                me "Oh… How long will it take?"
                "She shrugged."
                sl "I don't want to get out fast, I want it to be done right."
                sl "So as soon as I'm done…"
                "After apologizing again, she walked towards the square, leaving me alone."
                hide sl with dissolve
                "There were no other candidates."
                "Well, I'll have to go against squad leader's wishes and go alone after all."
                "Oh yeah, solo action is my forte."
                $ alt_day2_convoy = 'sl_prep'
            elif alt_day2_un_rej_convoy:
                show sl normal pioneer with dspr
                sl "She rejected you, yeah?"
                "The girl nodded understandingly."
                "I blushed."
                sl "Well, Lena is our unsociable child, after all."
                "After a little thought she shook her bangs:"
                sl "Sem, if you want me to help you faster, you have to also help me out in the square."
                me "Knew it!"
                me "But nooo, if only anyone would say: «Yeah! Of course! Let's go! No caveats here!»"
                show sl laugh pioneer with dspr
                sl "Why are you complaining? Don't help if you don't want to."
                $ alt_day2_convoy = 'sl_prep'
            else:
                sl "Sorry, I can't."
                me "Yeah?"
                "I wasn't hiding my grief."
                me "But why?"
                sl "Olga Dmitrievna asked me to help with evening events."
                me "Really? Well, that's quite unfortunate."
                me "See you soon?"
                "She waved her hand and ran away towards the squad leader's house."
                $ alt_day2_convoy = 'me'
        "Alisa":
            if dr:
                $ lp_dv += 1
            "I was scrolling through my options, dropping them one after another, before deciding on…{w} Alisa!"
            if alt_day1_me_d3_dv_feed:
                "She does owe me."
            elif alt_day1_cofront_sl_dv == 2:
                "Yesterday it seemed to me that despite all her cockiness, she wasn't such a bad girl."
            th "After wall, it's just a simple walk in the camp."
            th "Nothing strange could happen. Right? Right?"
            "That last question made me especially uncomfortable."
            "But since I took up the tug…"
            scene bg ext_dining_hall_near_day with fade
            if alt_day2_un_rej_convoy:
                "Having received a reasonable refusal, I decided to try my luck with Alisa."
            elif alt_day2_bf == 'dv_us':
                "Besides, she just told me on breakfast that I'm «not completely hopeless»."
                "I don’t know if this is a compliment or an insult, but the fact that she didn't completely ignore me is unequivocal."
                "I went out onto the porch searching for the red lightning bolt."
            else:
                "I didn't dare disturb the blazing girl during breakfast - I know by myself that when I'm hungry, I shouldn't be trifled with - I'd kill on sight."
                "So I quickly finished breakfast and, picking my teeth with a toothpick, took up an observation post on the porch."
            "And soon she showed up! Obviously hurrying somewhere, angrily looking around."
            show dv normal pioneer2 with dissolve
            "Usually she has that kid orbiting her, so now is the best chance!"
            "I jumped off the handrail and caught up with Alisa."
            if herc:
                me "Hey, redhead!"
                show dv angry pioneer2 with dspr
                dv "The hell did you just say?!"
                me "Oh, pardon me. I'm sorry. I was wrong, I will justify, correct and prove."
                me "Don't like being a redhead - how about I can call you something else? How about Alisochka? Lisa-Alisa? Any other options?"
                show dv normal pioneer2 with dspr
                dv "What do you want?"
                "She had already cooled down and was ready for constructive dialogue."
                me "Alisochka! You are my only hope! Save me, don't let me die in my prime!"
                "I shouted so that the pioneers passing by scaredly shied away."
                dv "Stop fooling around! What exactly do you want?"
                me "I would like to, if you are not too busy, invite you to a small rendezvous on the territory of this charitable institution!"
                show dv angry pioneer2 with dspr
                dv "Cuh?"
            elif loki:
                me "Good morning, beauty!"
                show dv angry pioneer2 with dspr
                dv "Fuck off."
                me "Hold up."
                me "Such a beautiful girl - and so angry.{w} How can you be this mad?"
                me "Maybe there's a lack of endorphins in your organism? Just tell me - I'll rob canteen of sweets. Do you want me to?"
                "She was stubbornly silent and continued to move with the inevitability of a locomotive."
                me "If you don't want sweets - maybe oranges?"
                me "Or I could give you my kompot at dinner? I don't mind!"
                show dv smile pioneer2 with dspr
                "Dvachevskaya was trying her hardest not to smile…{w} It wasn't working out well."
                dv "Why are you bothering me, huh?"
                "The storm had not yet passed, but the evil look from under her brows has been replaced by the usual mocking one, and the air no longer smelled of ozone."
                me "I want to invite you to a date."
                "She immediately stopped and… blushed?!"
                "Well, now I've seen everything!"
                show dv shy pioneer2 with dspr
                dv "What date, what the hell are you talking about…"
                me "Okay, okay, not really a date. More like a walk."
                dv "Guh?"
            else:
                me "Hey."
                "She didn't say anything."
                me "Alisa…"
                dv "What."
                "She said in an unbearably calm voice."
                "And this, this is Dvachevskaya?!"
                me "Can I ask you about something?"
                dv "No."
                "Well, I guess that's it folks."
                "I held my silence for a while."
                me "Even though… Ali…"
                show dv rage pioneer2 with dspr
                "She stopped and grabbed me by the collar."
                dv "Did I stutter?"
                "She hissed in a voice that wasn't her own."
                me "E-everything's… c-clear…"
                "I expected anything. {w}Anything except this fit of rage."
                if alt_day1_me_d3_dv_feed:
                    show dv rage pioneer2 close with dissolve
                    me "I thought we were friends."
                    "I spoke to her back with resentment."
                    show dv angry pioneer2 with dspr
                    dv "Friends? How did that happen?"
                    me "I need help."
                    dv "Help?"
                    "I shook my head."
                elif alt_day1_cofront_sl_dv == 2:
                    show dv rage pioneer2 close with dissolve
                    me "Strange, I thought you didn't leave 'your' people behind when they got into trouble."
                    show dv normal pioneer2 with dspr
                    dv "And how the hell are you «mine»?"
                    me "Well, technically not yours… But I did a good deed yesterday!"
                    dv "Which one?"
                    me "Saved your time, so you wouldn't have to break into the cant…"
                    "She immediately shut my mouth with a hand, so I didn't get to finish."
                    show dv angry pioneer2 with dspr
                    "Alisa threatened me with her eyes:"
                    dv "You're going to create that many problems, huh? Go on, shout even louder, so that the entire camp gets to hear it."
                    "I shrugged."
                    show dv normal pioneer2 with dspr
                    dv "Alright. You got me. What do you want?"
                else:
                    $ alt_day2_convoy = 'me'
                    return
            me "Take a walk around the camp, I'm telling you. I got the checklist. Want to accompany me?"
            show dv laugh pioneer2 with dspr
            dv "What, do I get to handhold you?"
            me "Handholding? Would you?"
            show dv normal pioneer2
            dv "No!"
            "She cut me off."
            dv "Anyways, I'm busy right now."
            me "I could help you. You know, I help you, you help me. Pioneers should help each other."
            dv "Oh, fuck you… Pioneer."
            "And so I went…"
            if lp_dv >= 3:
                $ lp_dv += 1
                $ lp_sl -= 1
                $ lp_un -= 1
                hide dv with dissolve
                "And then I heard:"
                dv "Musical club. In fifteen minutes. Don't be late."
                $ alt_day2_convoy = 'dv_prep'
            elif alt_day2_un_rej_convoy:
                $ lp_dv += 1
                hide dv with moveoutleft
                dv "Fine. Hold up."
                show dv normal pioneer2 with dspr
                dv "You'll help me, then I'll help you. Good enough?"
                "I nodded, hiding a satisfied smile."
                dv "Then I'll be waiting for you at the northern part of the camp, near the music club."
                hide dv with dissolve
                $ alt_day2_convoy = 'dv_prep'
            else:
                "Feeling spat upon, I turned around and left."
                if dr and (counter_sl_7dl == 0):
                    "As if she didn't have enough fun dousing me yesterday, she also had to mock me now."
                else:
                    "What did I do wrong?"
                "Red bitch."
                $ alt_day2_convoy = 'me'
        "Lena" if not alt_day2_un_rej_convoy:
            "After our conversation yesterday, Lena did not go out of my head."
            "I thought that walking around the camp together is a pretty good opportunity to get to know each other a little better."
            "Looking through the crowd of pioneers, I finally found the familiar face and, on instantly weakening legs, approached her."
            scene bg ext_dining_hall_near_day with fade
            show un normal pioneer at center with dissolve
            if alt_day2_bf == 'un':
                me "Sorry for ruining your breakfast."
                un "What?"
                me "You didn't finish eating and left. I thought maybe it was because of my stupid questions."
                un "They weren't stupid."
                me "Really? I just thought I somehow offended you."
                un "It's all good."
            else:
                me "Hello!"
                un "G-good morning."
                me "Good morning…"
            "I wouldn't say that there was some kind of hostility in her eyes. It was more like coldness."
            if herc or loki:
                "A slight but clearly expressed distaste, for which I personally do not see any explanation."
            elif dr and (counter_sl_7dl == 0):
                "I'm telling you, that redhead told her how she doused me yesterday, and now Lena despises me."
            show un normal pioneer at center with dspr
            "Not knowing how to deal with it, I decided to take a detour."
            if alt_day2_bf != 'un':
                me "Lena, can I have you for a few words?"
                "She silently nodded."
                "She didn't look away and looked me straight in the eyes, so that it even became a little uncomfortable."
            me "Are you busy? I just got this checklist… Gotta go around the camp… Collect… Signatures."
            "She attentively listened to me."
            me "If you wouldn't mind… Could you… Help me?"
            un "How?"
            "Of course, evaluating things from my spot was quite difficulty, but I definitely wasn't prepared for this Lena. She… was oppressing me."
            me "Did something happen? Have I offended you somehow?"
            un "No, it's not about you. So what kind of help were you talking about?"
            "I suddenly imagined a picture of this unsmiling girl leading me somewhere and showing me something.{w} All while looking like a martyr."
            th "Hell no."
            me "About none. I'm sorry."
            "She shrugged and followed me with her eyes."
            th "Oh well."
            hide un with dissolve
            $ alt_day2_un_rej_convoy = True
            jump alt_day2_convoy
        "I'll go alone":
            scene
            $ renpy.show("bg ext_dining_hall_near_day", at_list = [zentercenter], what = Noir("bg ext_dining_hall_near_day", brightness = -0.4, saturation = -0.4))
            "What am I, a kid?"
            "I'll manage on my own."
            $ alt_day2_convoy = 'me'
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_sl_guide:
    play sound sfx_open_door_1
    pause(1)
    scene bg ext_dining_hall_near_day
    with dissolve
    play ambience ambience_camp_center_day fadein 3
    pause(2)
    scene bg ext_dining_hall_away_day
    with fade
    pause(1)
    scene bg ext_square_day with dissolve
    play music music_list["everyday_theme"] fadein 3
    "Breakfast ended quickly, and not even a minute passed before I found myself plowed into socially useful work."
    dreamgirl "Stay closer to Slavya!"
    "The inner voice mocked me."
    dreamgirl "You'll be just fineeee with her!"
    th "Oh come on, it's just cleaning up the square."
    dreamgirl "Yeah, and it ain't your business!"
    "Either way, we were heading towards the square."
    me "Ahem-ahem!"
    "I cleared my throat, and Slavya, shuddering, came to her senses:"
    show sl normal pioneer with dissolve
    sl "Oh, you're still here? Sorry, I got lost in thoughts."
    me "It's okay."
    "I returned back her joke."
    show sl smile pioneer with dspr
    sl "You're vindictive, aren't you?"
    me "Not really. I just have a good memory."
    me "So why did you bring me here?"
    sl "Work! We need to deal with it fast, while there isn't that much dirt."
    me "Why?"
    sl "Disco! Would you want to dance on a dirty square?"
    me "Honestly I expected that it would happen in a club, or in any other building."
    "Dancing under open air couldn't be imagined even in my most horrendous nightmares."
    sl "Get to work, we don't have much time!"
    "Slavya handed me a broom, and hurried to the opposite side of the square."
    $ alt_day2_convoy = 'sl'
    $ list_voyage_7dl.append('cleaning_sl')
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_event_music_club1:
    scene bg ext_musclub_day with fade
    if ('library' in list_voyage_7dl) and ('medic' in list_voyage_7dl):
        "I wouldn't expect any surprises from the local art director."
        "Although after meeting the PMS-stricken librarian and luxurious vampiric nurse I wouldn't be surprised by anything."
    elif ('medic' in list_voyage_7dl):
        "I wouldn't expect any surprises from the local art director."
        "Although after meeting the luxurious vampiric nurse I wouldn't be surprised by anything."
    elif ('library' in list_voyage_7dl):
        "Like the library, the music club was on the outskirts of the camp."
        "Except unlike the library, which was protected from the camp noises, this was done to protect the camp instead."
        "I remembered my first rehearsals and shivered, personally imagining how twenty people would come, take their places and start playing."
        "I wouldn't expect any surprises from the local art director."
        "Although after meeting the PMS-stricken librarian I wouldn't be surprised by anything."
    if (counter_sl_cl == 1) and len(list_voyage_7dl) == 0:
        "Deciding to heed Slavya's advice, I went to the closest place."
        if alt_day_binder != 1:
            "Diocese of someone named Miku."
            "As I understood, it was the same Japanese beauty with whom I managed to not cross paths even once in a day."
    if not (alt_day2_convoy == 'dv'):
        "At first glance, the building gave the impression of some kind of lightness."
        "Maybe it's because half of the house was occupied by a huge terrace, maybe because two sides of the four in the «closed» half were taken by windows covering the entire wall."
        "I thought that it would be very nice to stay here for a while."
        "At least sit on the terrace."
    if (alt_day2_convoy == 'dv_prep'):
        if len(list_voyage_7dl) == 0:
            show dv smile pioneer2 at center with dissolve
            "Alisa already was here."
            dv "You're quick. Alright, let's go."
        elif len(list_voyage_7dl) == 1:
            "Alisa was sitting on the veranda, somehow cringing, looking hopelessly at the floor."
            show dv cry pioneer2 at center with dissolve
            "And my heart stung with some sharp tenderness and a forgotten feeling of remorse."
            "I went up the steps and quietly sat down beside her."
            if herc:
                me "Please, forgive me. I'm late."
                "The expression of her eyes, as if beaten, immediately changed to the already familiar arrogance... And well, from there it was a stone's throw to anger."
                show dv angry pioneer2
                dv "Where the hell even were you!"
                dv "The only thing you can be sent for is death!"
                "I liked Alisa more wheh she was like this."
                me "I was looking for the music club."
            elif loki:
                me "Hello, handsome. Finally found you."
                show dv grin pioneer2
                dv "Yeah, you weren't in a hurry."
                dv "Got some sleep?"
                show dv angry pioneer2
                dv "Where the hell even were you!"
                dv "Here I am, sitting here, waiting for him like an idiot, and he's walking somewhere else."
                "I liked Alisa more when she was like this."
                me "I'm telling you… I was looking for you. And so I did find you."
            else:
                me "Sorry, I'm late."
                show dv normal pioneer2
                dv "It's okay."
                dv "I already figured out that you're a retard."
                me "Retard?!"
                show dv angry pioneer2
                dv "Damn straight!"
                show dv rage pioneer2
                dv "Where the hell even were you!"
                dv "Where, I told you in intelligible Russian, did I say would wait for you?!"
                "I liked Alisa more when she was like this."
                me "Near the club…"
                dv "When?"
                me "In fifteen minutes… Alisa, please, forgive me. Okay?"
            show dv normal pioneer2
            "I looked ingratiatingly into her eyes, and she, not being able to stand it, snorted, calming down."
            if dr:
                dv "Oh well, what can you do with a dumbass like this."
            dv "Alright, let's go."
        else:
            "There was no one on the rendez-vous point Alisa designated."
            "I went up to the terrace in search of the girl, and my attention was drawn to a piece of paper pressed down by a bench."
            "I leaned over and picked it up."
            "There was a single word written on it in a pretentious girlish handwriting."
            "{b}JERK{/b}"
            $ lp_dv -= 5
            $ alt_day2_convoy = 'dv_rej'
            "Oopsie. Looks like we couldn't work it out with Alisa."
            dreamgirl "Whoa! How'd you figure that one out, genius?!"
            return
        dv "We need to move this..."
        "She tapped a steel box with a transparent top panel next to her."
        dv "To the stage. Can you do it?"
        if herc:
            me "Easy."
            "I estimated its weight."
            me "A cart would be nice… Anyways, it's ok. Are you in a hurry?"
            show dv laugh pioneer2
            dv "I'd like it to be done by today."
            me "Will do."
        else:
            "Alone I definitely wouldn't be able to carry it. It's surprising she could even lift it herself."
            "Having made a decision, I decided to quickly head to squad leader's house - there was something like a cart there."
            dv "Where are you going?"
            me "Wait for me!"
            with fade2
            "When I returned with the cart, I loaded the damn amp into it and got up, taking the weight with my hands."
            me "Lead the way!"
        scene bg ext_stage_normal_day with clock_r
        "After fifteen minutes of torment, chugging and sweating, I finally unloaded the damn amp onto the stage."
        show dv smile pioneer2 with dissolve
        dv "Great."
        dv "Let's go, yeah?"
        $ alt_day2_convoy = 'dv'
        with fade
    stop ambience fadeout 6
    return

label alt_day2_inmusic:
    if (alt_day2_convoy == 'un'):
        "Lena scratched at the door, quietly turned the knob and went in."
        "I followed her."
    elif (alt_day2_convoy == 'sl'):
        play sound sfx_knock_door2
        "Knocking with a delay, Slavya pushed the door and went in.."
        "I followed her."
    elif (alt_day2_convoy == 'dv'):
        "We came back to the starting point."
        "Without bothering with knocking, Alisa turned the doorknob and entered."
    else:
        "Climbing up two creaking steps, I went to the door leading to the «closed» part, and knocked."
        play sound sfx_knock_door2
        pause(1)
        if (alt_day2_convoy == 'dv_rej'):
            "Not a single sound came from within. I waited a few seconds and turned the knob."
        else:
            "Not a single sound came from within. I waited a few seconds and…"
            show dv surprise pioneer2 with easeinbottom
            with vpunch
            play music music_list["that_s_our_madhouse"] fadein 2
            "Collided with Dvachevskaya at the door."
            "Bang."
            "I was a little taller, so she got hit harder. Sighing, I hurried to pick up Alisa and take her to a nearby bench.."
            show dv angry pioneer2 with dissolve
            dv "Watch where you're going, you!"
            "She hissed, removing her hand from her forehead."
            "Between the eyes she had a clearly distinguishable bump. {w}Judging by where she was looking I obtained the exact same decoration."
            me "Come."
            "I offered her my hand."
            dv "What? Where?"
            me "We need to apply something cold to it. You don't want to walk around with a bump on your forehead until the end of your shift, do you?"
            dv "It's all your fault! If you would…"
            me "Mind you, I knocked. What were you even doing there?"
            show dv sad pioneer2 with dissolve
            "Did it seem like it, or have I managed to embarrass our boy-woman? {w}Hm… Interesting. {w}It's either connected to the club manager (I giggled wickedly as I pictured Alisa having an affair with an elderly musician) or the music.."
            "To instruments."
            dv "Not your business."
            "She wanted to get up and leave, but I already started wondering!"
            "I grabbed her hand."
            me "Alisa, don't be an enemy. Please tell me, what's up?"
            show dv normal pioneer2
            "She looked at my hand in surprise, as if it were some kind of exotic insect, and, carefully freeing herself, stood up."
            dv "That's. {w=.4}Not. {w=.2} Your. {w=.3}Business."
            "She said distinctly."
            hide dv with dissolve
            stop music fadeout 6
            "And left."
            "Oh well. I went up to the door and turned the knob."
    pause(1)
    play sound sfx_open_door_2
    pause(1)
    scene bg int_musclub_day with fade
    play ambience ambience_music_club_day fadein 1
    play music music_7dl["what_am_i_doing_here"] fadein 1
    pause(1)
    "I looked around and realized that I like it here."
    "A spacious room, framed portraits of Bach, Schubert and Liszt on the walls, a piano, a music stand for a vocalist, a microphone - people obviously sang here and did it with pleasure."
    "My gaze shifted further - from the drum set gathering dust in the corner to «Musima» without strings, table with a tape recorder, from which a thick cord led to the speaker."
    "Several shelves with musical literature and a metronome frozen in an end position."
    "I was about to go up to the piano and play something frivolous, when suddenly my eyes stumbled upon…"
    scene cg d2_miku_piano2 with dissolve
    if (alt_day2_convoy == 'sl'):
        "Slavya giggled."
    "There was a girl under it!"
    if alt_day_binder == 1:
        "The same one with which my acquaintance with the camp began!"
    "She almost completely hid under the piano, exposing only slender legs."
    "Seemed like she dropped something, and that something rolled under the instrument."
    "I followed the direction of her gaze. Harmonica."
    "The girl reached for the harmonica, arching her whole body, but still couldn't get it, and she had to get further and further under the piano."
    "I don’t know about her, but I personally would be scared. If this massive beast suddenly gives in and collapses… No, I can't look at this!"
    dreamgirl "I can thought!"
    dreamgirl "Check this out, striped panties!"
    "I went around the piano and, bending down, picked up the harmonica, handing it to the owner."
    scene cg d2_miku_piano with dissolve
    play sound sfx_piano_head_bump
    with vpunch
    pause(1)
    "She tried to straighten up, completely forgetting where she was, and hit the lacquered belly of the piano."
    mi "Ouch!"
    scene bg int_musclub_day with dissolve
    "I averted my eyes, pretending that I had just arrived - and definitely wasn't standing and unceremoniously staring at…"
    "She backed away and once more bent over like… like…"
    "Is she for real right now!"
    if (alt_day2_convoy == 'un'):
        show un smile pioneer at right with dissolve
        "Standing right behind me, Lena giggled softly as she watched my ears flare up."
        if ('medic' in list_voyage_7dl):
            "Just like in the infirmary, she obviously enjoyed situations in which I looked like an idiot."
    elif (alt_day2_convoy == 'sl'):
        show sl smile pioneer at right with dissolve
        "Standing nearby, Slavya secretly smiled into her fist."
        "And last but not least - from how embarrassed I was!"
    elif (alt_day2_convoy == 'dv'):
        show dv laugh pioneer2 at right with dissolve
        dv "Hey! Hey! Whip her!"
        "She pointed with her finger at what peeked out from under short skirt.…"
        "Dvachevskaya turned out to be in her repertoire - she burst out laughing and moved a little to the side - to watch how I would get out of the situation."
        show dv normal pioneer2 with dspr
    play sound sfx_brass_drop
    "I hit a very unfortunately positioned trombone with my elbow - judging by the numerous dents on the trumpet, I was not the first - and the instrument fell to the floor with a loud smash, splitting in two from the impact."
    show mi serious pioneer with dissolve

    mi "It's alright, people keep dropping it."
    show mi normal pioneer with dspr
    "If she's constantly under the piano - well, that's not surprising."
    if persistent.alt_binder:
        if alt_day_binder != 1:
            if persistent.mi_dj_true:
                "She finally straightened up, and I could hardly hold back an enthusiastic sigh."
                th "Wait… She's…"
                th "Hold the goddamn phone. Why am I waggling my tail and how do I know her?"
                th "I mean, of course I remember that she stared at me yesterday, but that's all there is!"
                th "And here I had an impression of an old acquaintance."
                th "I knew only one asian closely - and it sure as hell wasn't her."
                me "Greetings."
                "I smiled heartily - and she smiled so, honestly, sincerely, like an old acquaintance."
            elif persistent.mi_dj_bad:
                "Our eyes crossed - and I barely managed to suppress the desire to hide under a bench."
                "For some reason I saw Pulkovo, breaking undercarriage…"
                "And even in her eyes there was a splash of a half-forgotten pain."
                mi "Tell me… Why do I feel like I know you?"
                mi "I tried so hard to remember you yesterday, but I couldn't."
                "She tilted her head to the side, like a bird."
                "I shrugged."
            elif persistent.mi_dj_good_jap:
                th "Oh, here's a familiar face."
                "I wasn't good with names, but faces were a completely different story."
                "And I definitely saw this face somewhere else."
                "And we definitely were acquainted!"
                me "Hey! Remember me?"
                mi "I'm sorry?"
                "The girl tilted her head to the side, looking at me."
                mi "I've seen you somewhere, yeah… Have you ever been to Sapporo? Ah, what am I even asking, why would you be in Sapporo, especially where we could meet?"
                me "Well, not like I ever was there…"
                "I said, contemplating."
    me "I came here with a checklist."
    if alt_day2_convoy not in ('dv', 'sl', 'un'):
        $ lp_mi += 1
        mi "Are you without a guide?"
        "She absentmindedly asked."
        me "Uh…"
        me "Yeah, decided to go alone."
    "I handed her the paper."
    if not (persistent.mi_dj_true or persistent.mi_dj_good_jap):
        me "I mean, I wanted to say, hello."
        "After unintentional voyeurism my thoughts were in disarray."
    if alt_day_binder == 1:
        if alt_day1_me_d3_chase:
            mi "Ou, that's You."
            "She started."
            $renpy.notify('In Russian language you (1 person) and you (2+ persons) are different words, second variant could be also used as a polite pronoun.')
            me "Uh, No «You's»."
            mi "But I…"
            me "No."
            mi "...mean..."
            me "«You's»."
            show mi smile pioneer with dspr
            mi "As You say... {w}Oi, I mean, as you say."
        me "So, will you finally tell me your name?"
        show mi laugh pioneer with dspr
        mi "You're persistent, aren't you."
        show mi normal pioneer with dspr
        mi "But the man should introduce himself first, remember?"
        me "Sorry. {w}I'm Semyon."
        mi "Nice to meet you! {w}And my name is Miku!"
    else:
        mi "You're Semyon?"
        "She came up to me and, picking up the halves of the trombone, put the instrument back in its old place."
        "All while bending over, once more showing me…"
        "Ugh, someone will drop it again!"
        mi "Hey! I'm Miku!"
    $ meet('mi','Miku')
    $ alt_day2_mi_met = True
    me "Miku?"
    show mi smile pioneer with dspr
    mi "Yeah."
    show mi serious pioneer with dspr
    "She frowned for a second."
    show mi normal pioneer with dspr
    mi "For some reason, nobody believes that it's my real name! My mom's from Japan, and my dad is a Russian Engineer!"
    "She uttered the last two words with a distinctly pronounced capital letter, and I involuntarily smiled at her pride."
    "Being proud of your dad being an engineer… {w}That's worth a lot."
    "For some reason, anecdotes about impoverished engineers and robbers suddenly came into my head, who, instead of taking money from such hard workers, on the contrary, lent them three rubles."
    "I was silent, feeling a bit embarrassed about peeping, but the girl didn't seem to care at all."
    show mi happy pioneer with dspr
    mi "And this is my music club!"
    "She waved her hand around the room with her already familiar amusing pride and smiled."
    "I finally collected myself."
    me "Alright, calm down."
    "She nodded enthusiastically, and two incredibly long ponytails of aquamarine hair that floated following the movement of my head put me in a kind of trance for a split second. I kept staring."
    "A rather unusual hair color, a thin graceful neck and a figure of a teenage girl. If I had any doubts about her Japanese origin, after examination, they disappeared - and the name «Miku» wasn't looking all that fantastic anymore."
    show mi smile pioneer with dspr
    "Finally, she deigned to pay attention to the piece of paper that I had been holding out to her all this time."
    mi "Oh, were you sent with a checklist too?"
    show mi happy pioneer with dspr
    "She folded her hands so kawaii on her cheek that I couldn't hold myself back and smiled again."
    dreamgirl "«Kawaii»? Semyon, did you just say «kawaii»?!"
    dreamgirl "Maybe you should go out and touch grass? {w=.3}Take a shower immediately, maybe? {w=.3}Look at what she's doing to you!"
    mi "That's how they bully newcomers."
    th "Naaah, it's YOU who's bullying newcomers."
    mi "I'll sign it."
    show mi shy pioneer with dspr
    "She turned into a small tornado, throwing everything aside."
    mi "Come in."
    mi "I'll be right there."
    "And bent over again!"
    "I don’t know what goals she pursued, but she used the most dishonest methods to achieve them!"
    "Smiling with her eyes, she finally signed my unfortunate sheet."
    mi "I'm here almost all the time. Come in…"
    mi "Even if you don't want to sign up. And if you do…"
    show mi smile pioneer with dspr
    "She looked at me."
    mi "We're always glad to see you! Oh, I mean, I'm glad!"
    if (alt_day2_convoy == 'un'):
        show un smile pioneer at right with dissolve
        un "I love music… But I'm not talented enough for it."
        "She sighed."
        un "And you?"
    elif (alt_day2_convoy == 'sl'):
        show sl smile pioneer at right with dissolve
        sl "Music is so great! Too bad I never had enough time to take it seriously."
        "She glanced in my direction."
        sl "How do you feel about it? Do you like music?"
    elif (alt_day2_convoy == 'dv'):
        show dv normal pioneer2 at right with dissolve
        dv "Pffft. Yeah, you'll sign up here, and then you'll be practically buried in work."
        dv "Instead of music you'll be constantly rehearsing arpeggios and hymns in 1/8ths."
        show mi sad pioneer with dspr
        mi "That's not true! I always say that it's all about the creativity, and not technique!"
        dv "Uh-huh."
        dv "Either way, it's your decision."
    menu:
        "Sign up":
            $ list_joined_clubs_7dl.append('music')
            $ lp_mi += 1
            "And I smiled for the umpteenth time in the last two minutes. Couldn't help but smile."
            me "Why not. Sure, I'll sign up. Although, I haven't played in a long time."
            show mi happy pioneer with dspr
            mi "Great!"
            "She clapped her hands."
            mi "Let me just find the list…"
            play sound sfx_brass_drop
            with vpunch
            "She rushed back past the piano, knocking over a lone barrel along the way, took the book from the shelf and handed it to me."
            mi "Sign here, please. What would you like to play?"
            me "Generally speaking, I'm quite familiar with brass and wind instruments."
            "Looking sideways at the trombone, I jerked my shoulder."
            me "And I can play guitar a little."
            show mi smile pioneer with dspr
            mi "Wonderful! Absolutely amazing!"
            mi "Could you play something?"
            if herc:
                me "Maybe next time."
            else:
                me "If you'll get me a mouthpiece."
            show mi happy pioneer with dspr
            mi "Do you really know how to play?"
            "Miku was inexplicably happy."
            if herc:
                me "As if I have any reasons to lie."
            else:
                me "We all learned little by little… Get me a mouthpiece — I'll try to do something."
            "It was obvious that I couldn't squeeze anything serious out of myself, but…"
            if loki:
                "Perhaps this is a chance to start playing again, without choking on pain in glued alveoli?"
            show mi smile pioneer with dspr
            if not herc:
                mi "I'll get it for sure! I just have to go to the warehouse, I think they were there."
            mi "If you want, you can come after dinner, I'll try to be on time, then we'll play together!"
            mi "I'm here alone all the time. Or do you want me to teach you something else to play? Violin? Flute? I can do everything, it's true."
            show mi sad pioneer with dspr
            "She sighed."
            mi "Well, we don't really have a flute, but you didn't want it anyways, yeah?"
        "Don't sign up":
            me "Maybe next time."
    show mi normal pioneer with dspr
    th "You should rap, one-girl-orchestra. The whole wide-shouldered stage doesn't hold up a candle to you."
    if len(list_voyage_7dl) < 3:
        "I was inclined to attribute her strange antics to the embarrassment of the first meeting."
        "But she looked somewhat upset - as far as I could tell, having known her for a week without a year."
        me "Would it be immodest of me if I ask - did anything happen?"
        show mi normal pioneer with dspr
        mi "What? No. Nothing. It's just that I've lost something, I can't find it, and I'm a little upset about it!"
        me "What specifically?"
        mi "Well… In short, a braided bracelet. She means a lot to me."
        me "Kumihimo?"
        show mi shy pioneer with dspr
        mi "You even know things like that?"
        "Somehow she looked at me in new light."
        mi "Yeah. You know something?"
        "I shook my head:"
        me "No, but all girls knit their own baubles."
        me "And since you are a Japanese girl, you knit yourself a Japanese bauble."
        show mi upset pioneer with dspr
        mi "You… You're teasing me!"
        me "Oh did you just find that out?"
        "I didn't even think about hiding my smile."
        mi "You can't do it, that's dishonest and actually - we’ve barely known each other for ten minutes!"
        me "Sorry. I promise, if I see your bracelet somewhere, I will definitely return it."
        me "Can you at least tell me where you last saw it?"
        show mi normal pioneer with dspr
        mi "I wore it at home. Then I went to the beach. That is, not to the beach, to the the boats! I was thinking of taking a boat and going for a bit since no one ever comes."
        mi "But Olga Dmitrievna-san ordered me to sit in the club and wait for a newcomer - and to be sure to enroll him in a club!"
        if 'music' in list_joined_clubs_7dl:
            mi "It's great that you signed up by the way!"
            "Who would've guessed."
        else:
            mi "Have you changed your mind yet? About signing up, I mean?"
            "Her persistence was touching, but since I firmly decided not to sign up…"
        mi "So here I am, sitting here, all bored, no one comes to me, I already thought that you wouldn’t come either, and they just didn’t let me ride a boat out of spite!"
        "Miku was again carried away to the wrong steppes, but I understood the main thing - if I want to help her in her search, you can look next to her house and on the pier."
        me "Got that, thanks!"
        "I politely said goodbye."
        me "We'll meet again, right?"
        show mi smile pioneer with dspr
        mi "Of course!"
        "Miku exclaimed and, immediately forgetting about me, grabbed a music notebook - the genius had an inspiration."
        $ set_chibi_alt1('boat_station_alt1', '?')
    else:
        show mi smile pioneer with dspr
        me "I should go. Bye."
        mi "See you soon!"
        "The girl shouted, and, instantly forgetting about me, started scribbling something."
    stop ambience fadeout 2
    play sound sfx_close_door_1
    scene bg ext_musclub_day with fade
    pause(1)
    play ambience ambience_camp_center_day fadein 2
    if (alt_day2_convoy == 'un'):
        me "I can't say that I like {b}the entire{/b} art director."
        me "But the parts that I have seen…"
        show un laugh pioneer with dspr
        un "Miku is my roommate. So if you ever come in, at the same time you'll be able to chat with her."
        "She laughed again, apparently remembering the expression on my face in the course of contemplating what I should not have seen."
        me "Does she sit at the house like she sits here?"
        show un laugh pioneer with dspr
        un "No, only here."
        "I smirked and figured out where to go next."
    elif (alt_day2_convoy == 'sl'):
        me "I don't know about the rest of the camp, but your art director is something else!"
        show sl shy pioneer with dspr
        sl "Yeah, Miku is a bit eccentric. But please understand her too - she is alone in a semi-familiar country."
        "With her looks she definitely wouldn't get lost anywhere…"
        me "Nah, I mean, I like her."
        me "The parts that I've seen, anyways."
        show sl laugh pioneer with dspr
        sl "If you get closer to her, you'll know how good she is."
        th "How closer could we get? Directly in each other's insides?"
        "I chuckled and unfolded the map."
    elif (alt_day2_convoy == 'dv'):
        me "In other houses, dear guests are greeted with bread and salt…"
        show dv grin pioneer2 with dspr
        dv "Yeah, and here you got greeted with buns!"
        me "Let's keep going."
        show dv laugh pioneer2 with dspr
        dv "Right, not going to lie, that was pretty vulgar."
        "I smirked and planned my next move."
        show dv normal pioneer2 with dspr
    else:
        "The art director discouraged, disarmed and confused me. If anything, but this girl knows how to make an impression."
        "I could say for sure that I liked her!"
        "Right, we're done with music."
    if ('medic' in list_voyage_7dl) and (alt_day_binder != 1):
        "Our list of interesting people, consisting of vampiric nurse and Electronik, got expanded with a machine gun girl."
    elif (alt_day_binder != 1) or ('library' in list_voyage_7dl):
        "List of interesting people, currently consisting of Electronik, got expanded with a machine gun girl. What's next?"
    "I definitely like it more here!"
    "Not like in…"
    "There was a distinct click in my head, and a certain voice, which I would have difficulty identifying as internal - as it sounded painfully unpleasant - asked:"
    dreamgirl "Like where?"
    th "Like in my past life!"
    "The sun seemed to melt through the crust of ice, which covered me, and came close to the frozen heart."
    "For some reason, I suddenly wanted to laugh for no reason, open my arms and hug the whole world."
    "The same happiness, the existence of which I managed to forget - here it is, eat it with a spoon, take it!"
    "I was embarrassed by my own vehemence and returned from heavens to earth."
    "No laughs or hugs."
    "Anyways, I still have unfinished business."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_event_clubs1:
    if not alt_replay_on:
        if been_there_alt1() > 1:
            scene bg ext_clubs_day with fade
            th "Nope, nah, nuh-uh, that's enough! No more cybernetics for today!"
            return
    scene bg ext_clubs_day with fade
    play music music_list["eat_some_trouble"] fadein 2
    "One of the prioritized buildings on the list were clubs."
    if (alt_day_binder != 1):
        if counter_sl_7dl >= 1:
            th "Clubs… Wait, is that the same pretentious building I saw at the entrance with Slavya?"
        else:
            th "Something familiar… Wait, isn't that the house where I saw Ulyana with that locust?"
            th "Right, that's it!"
    th "I decided to visit our cybernetics."
    th "Maybe I can grab some headphones from them."
    "Wandering without music was pretty boring, and the damned silicone refused to stay in my ear."
    if counter_sl_7dl >= 1 and loki:
        "Worst case, at least I’ll steal a connecting cable and listen through an amplifier."
    else:
        "A few minutes later, I stopped at the clubhouse and smiled involuntarily, once again remembering that same locust."
        "Although, if you would compare it to that alien horror, the locust almost seemed harmless."
    "There was a sign on the door of the club with class schedules, which someone had already managed - and I can even guess who - to tear in half."
    "The only thing you could figure out was «checkers» — the next line was located along the tear line and could not be restored."
    "The club building did not inspire confidence neither with its shabby external appearance nor the windows garnished with metal bars in some places."
    "Although the number of cables, wires and pipes stretching towards here was awe-inspiring."
    "They're either building a rocket, or a cold fusion reactor."
    "I shook my head and took a step forward, but my eyes were drawn to an announcement hung over the work schedule."
    "It was simple: «Do not disturb», and so I doubted for a second whether it was worth bothering such busy people at all."
    "But the checklist clearly indicated these clubs as the first position. Oh well, what could happen."
    "Stepping on the first step, I realized that the conclusions about the quality of the building were premature - the porch boards did not creak, the doors looked shabby, but reliable, and on the railing hung a large closed padlock."
    if alt_day2_convoy not in ('dv', 'sl', 'un'):
        "After rattling the door for a bit, I entered."
    else:
        "The door wasn't locked, so we entered."
    play sound sfx_open_door_clubs
    stop ambience fadeout 2
    scene bg int_clubs_male_day with dissolve
    play ambience ambience_clubs_inside_day fadein 1
    "Well, I expected something like this."
    "A mess that a capable, but lazy, genius always calls «creative mess»."
    "Wires, coils, makeshift boards and switches lay everywhere in abundance."
    "There was some kind of peculiar machinery on the table, the name of which I did not know, but judging by the trembling wire arrow frozen in sector zero, it was some kind of measuring device."
    th "Oscillograph?"
    th "Who knows - it's not my forte anyways."
    "The owners were nowhere to be seen."
    if (alt_day2_convoy == 'un'):
        show un normal pioneer with dspr
        if loki:
            "Well, that doesn't matter anyways."
            "I was more interested in some kind of headphones or, at worst, just a 3.5mm jack, and I'd figure something out myself…"
        if ('library' in list_voyage_7dl):
            un "Shurik is still in the library."
            if 'nwsppr' in list_joined_clubs_7dl:
                me "Hold on! So by saying that he'll be {i}at the usual place{/i}, Shurik meant the club?"
                "Lena nodded."
                me "Hm… Makes sense. He definitely could be interested in cybernetics."
        else:
            un "Shurik's gone somewhere again…"
            "Thoughtfully said Lena."
            me "Shurik? Who's Shurik?"
            un "He's responsible here. And in the newspaper."
            un "He's probably there right now."
    elif (alt_day2_convoy == 'sl'):
        show sl smile2 pioneer with dspr
        if ('library' in list_voyage_7dl):
            sl "Looks like Shurik is still in the library."
            me "And how does he relate to this?"
            show sl smile2 pioneer with dspr
            sl "Well, he's the head of cybernetics club."
            if 'nwsppr' in list_joined_clubs_7dl:
                me "So by saying that he'll be {i}at the usual place{/i}, Shurik meant the club?"
                sl "Yeah!"
            sl "He and Electronik always circulate between library and here."
            show sl smile pioneer with dspr
            me "Oh, so that's how it is."
        else:
            me "Is it customary here to leave the door wide open and disappear?"
            sl "It's just Shurik. Can't blame him — he's working in two clubs at the same time."
            show sl normal pioneer with dspr
            me "Shurik? Who's Shurik?"
            sl "Head of cybernetics club."
            sl "And he also works on the newspaper. Electronik and him are probably in the library right now."
            me "I see."
        if counter_sl_cl != 0:
            me "Alright, where's our light show requisite?"
            show sl normal pioneer with dspr
            sl "Don't worry about it, I'll check everything myself."
            me "Oh, please!"
            sl "Ugh, fine."
            show sl shy pioneer with dspr
            "It seems that Slavya was not very pleased with remembering the demonstration of her mistake."
            "Even though I tried to cover her up as best as I could."
            "She's not me — I could just dust myself and gallop on."
            "She went to the closet and, looking for a bunch, separated the semicircular key with which she opened the storage of equipment.."
            sl "Easy thing."
            sl "You just need to take the garland out and plug it in."
            me "Does the color matter?"
            show sl laugh pioneer with dspr
            sl "Nope! We paint the light bulbs ourselves - with iodine and potassium permanganate, if I recall correctly."
            sl "If you want specifics you'll have to ask the boys."
            hide sl with fade
            "She plugged the garland into the outlet, and one of the bulbs, immediately flashing, went out for good."
            "The rest, economically launched through a starter for a fluorescent lamp, pretended to be a light show."
            "Or rather, it seemed so to me at first: in fact, four light bulbs were missing."
            "Slavya unscrewed them and put them away in a bag."
            show sl normal pioneer with dspr
            sl "That's all there was."
            sl "And now the most pleasant part of the work: we will try to put this whole thing back."
            th "Am I mistaken, or did her voice actually sound sarcastically?"
            "Nope, wasn't mistaken."
            "Once I happened to work as a packer - just to see what it is, nothing serious."
            "And that process was very similar to what we were doing now - it was necessary to put almost a kilometer long cable with light bulbs into a relatively small bag."
            "And only the presence of one, very correct in all aspects, girl right next to me allowed me to control myself."
            "Not a single swear word left my mouth."
            "But I really wanted to!"
            with fade2
            "But if you suffer for a long time, something will work out."
            "We finished this difficult task and sat down at the table trying to take a breather."
            me "Owners still aren't here."
            "I said lazily."
    elif (alt_day2_convoy == 'dv'):
        show dv angry pioneer2 with dspr
        if ('library' in list_voyage_7dl):
            dv "The four-eyed seemingly settled in the library."
        else:
            dv "And where the hell is this four-eyed?"
        me "Who?"
        dv "That one, what's his name… Shurik."
        if ('library' in list_voyage_7dl):
            me "Oh, he's the chief here?"
            dv "Who else?"
            me "Hm… Yeah, makes sense. He definitely could be interested in cybernetics."
            if 'nwsppr' in list_joined_clubs_7dl:
                me "Hold on! So by saying that he'll be {i}at the usual place{/i}, Shurik meant the club?"
                "Alisa grimly nodded."
        else:
            dv "He literally wears glasses. You can't mistake him for anyone else, he's the only one who does."
            dv "He's probably still stuck in the library."
    else:
        if ('library' in list_voyage_7dl):
            if 'nwsppr' in list_joined_clubs_7dl:
                "According to what was in the checklist I was looking for Shurik. So that's what he meant by {i}the usual place{/i}."
            else:
                "According to what was in the checklist I was looking for Shurik. Turns out he's also the chief here."
        else:
            "According to the checklist, the man I was searching for was Alexander, head of cybernetics club."
    "Although there was not enough time to go around the camp, I decided to wait so I could get an autograph on the list."
    if loki:
        "And until then, I could look around for what I was interested in."
        $ alt_day2_minijack = True
        if alt_day2_convoy not in ('dv', 'sl', 'un'):
            "Quickly convinced that no one would interfere with my archaeological excavations, I removed a cardboard box from the cabinet."
            "The search did not take long - using Murphy's law, I shook out the contents on the table and, in full accordance with the rule, the plug I was looking for was found at the very top of the pile."
            "Unfortunately, it was just a three-millimeter plug with a piece of wire - no nonsense, like headphones attached to it, was observed."
            th "Thanks for that, at least."
            "Putting the plug aside, I swept the junk from the table back into the box and set it back in place - on the cabinet."
        elif (alt_day2_convoy == 'un'):
            "Unfortunately both pairs of headphones I have found — one 'pair' had the left «ear» completely torn off, second pair didn't have a holding bow — wouldn't fit my needs."
            "But I managed to get a minijack, which means that the moment I get to any semblance of an amplifier…"
            "Lena silently watched my excavations, trying not to interfere."
        elif (alt_day2_convoy == 'dv'):
            me "Alisa!"
            show dv normal pioneer2 at center
            dv "What do you want?"
            me "You know what's a mini-jack?"
            dv "Huh?"
            me "Male plug, 3.5mm!"
            dv "Something familiar…"
            "She got lost in thought."
            me "Either way, I need it. Let's search!"
            dv "Why do you need it?"
            me "I just do! Will you help?"
            show dv smile pioneer2 with dspr
            dv "Fine! You can explain why later."
            me "I'll even show you!"
            "A few minutes of searching gave us two pairs of headphones - broken ones, several mono outputs and, finally, one sane mini-jack with a small supply of wire."
            me "Bingo!"
            "I lifted it above my head."
            show dv normal pioneer2 with dspr
        elif (alt_day2_convoy == 'sl'):
            show sl angry pioneer with dspr
            sl "Hey, what are you doing?"
            "Slavya asked angrily."
            sl "Why are you rummaging there without permission?"
            me "I need a plug. If I find it, I'll ask the owners. But while they're gone, I need to do something!"
            show sl dontlike pioneer with dspr
            "Slavya couldn't find a counterargument, so she fell silent, closely following me."
            "Finally I found what I was searching for - and right on time too."
            show sl normal pioneer with dspr
    else:
        if alt_day2_convoy in ('dv', 'sl', 'un'):
            me "For how long can he be gone?"
            if (alt_day2_convoy == 'un'):
                show un normal pioneer with dspr
                un "Who knows. But it's unlikely to be a long time - he would have to close the room up, Olga Dmitrievna has strict policies regarding that."
            elif (alt_day2_convoy == 'sl'):
                show sl normal pioneer with dspr
                sl "Shurik? About twenty minutes, no more, he constantly locks the club - as if something is stored here…"
                "She suddenly stopped."
                me "What?"
                show sl shy pioneer with dspr
                sl "Don't mind it. Something really important to him."
                show sl normal pioneer with dspr
            elif (alt_day2_convoy == 'dv'):
                show dv normal pioneer2 with dspr
                dv "How should I know? I don't talk to these idiots."
                me "You're very helpful."
                "I exclaimed sarcastically."
                "Alisa just nodded. Can't get her with that, I guess."
        "For the next five minutes, I looked at the contents of the numerous shelves. Finally, the agonizing wait was interrupted."
    show sh normal pioneer at right with dissolve
    if ('library' in list_voyage_7dl):
        "Behind I heard the sounds of footsteps, and then Shurik entered the room."
        if alt_day2_convoy in ('dv', 'sl', 'un'):
            sh "What are you two doing here?"
        else:
            sh "What are you doing here?"
        "He adjusted his glasses on the bridge of his nose with his trademark gesture."
        me "What-what… The checklist, remember?"
    else:
        "I heard the sounds of footsteps, and then a guy very similar to Alexander Demyanenko entered the room."
        $ meet('sh','Shurik')
        $ alt_day2_sh_met = True
        sh "Hello. Newbie. Semyon?"
        "He adjusted his glasses."
        "I nodded."
        if alt_day2_convoy in ('dv', 'sl', 'un'):
            me "Hey. You must be Shurik?"
        else:
            me "Hey. You must be Alexander?"
        "He nodded, holding out his hand."
        "His grip was firm, but also somehow distant."
        sh "You're here because of the checklist?"
        "He figured out."
        me "Mhm."
    if loki:
        "I hid the plug with a piece of wire in my pocket, trying to do it discreetly."
        if (alt_day2_convoy == 'sl'):
            show sl serious pioneer with dspr
            extend " While trying to ignore Slavya's angry stare."
            "Luckily, she didn't betray me."
            show sl normal pioneer with dspr
        me "So, will you sign it?"
        sh "Well… Give it here."
    else:
        "I timely remembered that I wanted to get a hold of something else here."
        menu:
            "Ask him about the plug":
                $ alt_day2_minijack = True
                me "I wanted to ask you about a cable."
                sh "Cable? What cable?"
                me "Male cable, 3.5mm."
                "He went to the table, where some cords, boards and capacitors were scattered in abundance, and, after rummaging for a minute, handed me an angled plug."
                sh "Good enough?"
                me "Yeah."
                "I rejoiced."
                me "Thanks."
                th "Now he will sign on the checklist, and we will part almost as friends.."
                me "Will you sign the checklist?"
                sh "Yeah."
            "Don't ask":
                me "Will you sign it?"
                sh "Give it here already."
    "Taking the paper, he turned it over in his hands for a while, as if not knowing what to do with it."
    "I was about to give him a pen when he put the paper aside and looked sternly at me."
    show sh serious pioneer at right with dissolve
    sh "Tell me, Semyon."
    if 'nwsppr' in list_joined_clubs_7dl:
        sh "Maybe, in addition to the newspaper, you will also sign up with us? {w}I know, I know, I'm too insistent, but think about it!"
    else:
        sh "How about signing up with us?"
    if (alt_day2_convoy == 'sl'):
        show sl normal pioneer with dspr
        sl "Shurik, can't these introductions wait until later? We just need to go around the camp."
        sh "It won't take long."
        th "Here we go again."
    elif (alt_day2_convoy == 'dv'):
        show dv angry pioneer2 with dspr
        dv "Of course! Now let's both join! And then we'll have Shuriks."
        dv "Do you really think that we came here to sign up in your mess?"
        show sh normal pioneer with dspr
        sh "Then why are you here?"
        "He adjusted glasses."
        show dv laugh pioneer2 with dspr
        dv "The checklist, you moron!"
        show dv normal pioneer2 with dspr
        show sh serious pioneer with dspr
        sh "Said moron has a name."
        sh "Shurik."
    elif (alt_day2_convoy == 'un'):
        un "Shurik… We're here for a different reason…"
    menu:
        "Why not":
            $ list_joined_clubs_7dl.append('cyber')
            if (alt_day2_convoy == 'dv'):
                show dv laugh pioneer2 with dspr
                "Alisa snorted."
                dv "You serious?"
                me "Well yeah, why not?"
                show dv normal pioneer2 with dspr
                dv "Uh-huh."
                "Judging by her voice, Dvachevskaya was somewhat disappointed with my decision."
                $ lp_dv -=1
            me "Although I don't really know anything…"
            show sh smile pioneer with dspr
            sh "That's okay, experience can always be acquired."
            "He opened a desk drawer and pulled out a huge book on which «CLUBS» was written in stencil, and, after flipping through a few pages, found the required one."
            sh "Now we just write you in…"
            sh "Done!"
            "He shook my hand."
            sh "Welcome to the club, cybernetic!"
        "You know…":
            "I hesitated."
            if 'nwsppr' in list_joined_clubs_7dl:
                "After the warm welcome that Shurik gave me in the editorial room, I didn’t want to have anything in common with him, at all."
            else:
                "Wasting time, sitting in the company of frenzied techies, while the summer is raging outside… Don't really want to."
            "It'd be better to read an interesting book."
            "Still, it was scary to offend him with an unambiguous refusal - what if he refuses to sign?"
            "It suddenly occurred to me that this is how bureaucracy grows, when for the sake of a meaningless signature people give you the right to twirl them as you please."
            "So I gave the most neutral answer."
            me "Listen, I'm sorry, of course, but I can't."
            if len(list_joined_clubs_7dl) >= 1:
                if ('nwsppr' in list_joined_clubs_7dl) and ('music' in list_joined_clubs_7dl):
                    me "I have already signed up for the newspaper. And I signed up with Miku too."
                elif 'nwsppr' in list_joined_clubs_7dl:
                    me "I have already signed up for the newspaper."
                elif 'music' in list_joined_clubs_7dl:
                    me "I have already signed up with Miku."
                elif 'soccer' in list_joined_clubs_7dl:
                    me "I've already signed up, and PE teacher would probably decimate me, if he ever found out that I preferred your club to football."
                elif ('volley' in list_joined_clubs_7dl) and (alt_day2_convoy == 'sl'):
                    me "I've already signed up, and PE teacher would probably decimate me, if he ever found out that I preferred your club to volleyball. Slavya probably also wouldn't like that."
                elif 'volley' in list_joined_clubs_7dl:
                    me "I've already signed up, and PE teacher would probably decimate me, if he ever found out that I preferred your club to volleyball."
                elif 'badmin' in list_joined_clubs_7dl:
                    me "I've already signed up, and PE teacher would probably decimate me, if he ever found out that I preferred your club to badminton."
            else:
                me "I haven't signed up anywhere yet, and I don't think I want to. {w=0.2}I'd rather take a look around camp first."
                sh "You think?"
                me "Definitely. It's my first day anyways, what's the rush?"
                me "There's still a lot of time, I'll think about it."
                sh "As you wish."
    "I awkwardly nodded at the paper."
    me "Can I go?"
    sh "Yes."
    "Shurik signed on the list and gave it to me."
    if 'cyber' in list_joined_clubs_7dl:
        sh "Come in when you're done - we will show you, we will teach you, we will give you a place. See you later!"
        me "See you!"
        "I waved to him and left."
    elif len(list_joined_clubs_7dl) >= 1:
        sh "It's a pity that you have already signed up, it's very interesting here, you know!"
    else:
        sh "Be sure to sign up for our club when you're done! We always welcome new members!"
        "And in my head to the beat of his last words sounded the Soviet anthem, so I hurriedly vacated the premises."
    play sound sfx_open_door_clubs_2
    pause(1)
    scene bg ext_clubs_day with dissolve
    play ambience ambience_camp_center_day fadein 2
    if 'cyber' in list_joined_clubs_7dl:
        "It is unlikely that I will be able to make a charger for my phone here, or at least a USB input for the player. But maybe I'll learn something useful?"
    else:
        th "How cunning! Everyone is trying to lure in a new initiate."
        "If not for the wonders of diplomacy, I'd have to sign up for sure…"
    stop music fadeout 2
    th "Alright, what's left?"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_event_camp_entrance1:
    if not alt_replay_on:
        if been_there_alt1() > 1:
            scene bg ext_camp_entrance_day
            th "I'm back here. There's still no bus."
            th "Boring, let's go back."
            return
    scene bg ext_camp_entrance_day with fade
    th "Still empty."
    "It has long been known that the strongest walls are actually the absence of said walls."
    "It would seem that it's really easy - just go along this highway. But as soon as one tiny fact emerges, this enterprise turns from an adventure into a farce."
    "The fact that from here to the nearest most seedy village you would have to go several hundred kilometers along the routes of secondary directions. Getting out of here? I don't think so."
    "How do I know that?"
    "I just do."
    th "It looks like I really have no choice. Gotta wait for the bus."
    "Or I actually don't have to wait for it, and I better start enjoying this unprompted summer vacation!"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_event_dv_us_house1:
    if not alt_replay_on:
        if been_there_alt1() > 1:
            scene bg ext_house_of_dv_day with dspr
            "This house was different from the others - it seemed to be cut down, not a single smooth line, everything was strict, straight, chopped."
            "And on the glass of the front door someone hung a Jolly Roger. I don't even need to think who would that be."
            "Doesn't seem like there's anything to do here."
            return
    scene bg ext_houses_day with fade
    "The scattered barrel houses evoked a sense of chaos, although on closer inspection it became clear that a landscape designer definitely worked here."
    "Only a person with experience and practice can so successfully build buildings into a deliberately uneven surface, almost without disturbing the centuries-old pines."
    "In some places, roots broke out of the ground and looked like blood vessels piercing the ground."
    "Just like back home… In summer… Back when I used to go to places beyond the local store."
    "Some shaggy pioneer with inflamed eyes got out of a neighboring house."
    "I myself see these every day. No worries, it's curable {w}with the simplest biting of a local cable."
    th "The only question is where this miracle of a minor managed to get so much Internet?!"
    "I turned away, being too embarrassed to look closely."
    "And then one house, which stood out from the rest, caught my eye."
    scene bg ext_house_of_dv_day with dissolve
    th "Pirate flag, heavy boots on the porch. Let me guess…"
    if (alt_day2_convoy == 'un'):
        un "Alisa lives here… With Ulyana."
    elif (alt_day2_convoy == 'sl'):
        show sl smile pioneer with dissolve
        sl "I think you've already guessed who lives here?"
        "Slavya smiled."
        "Of course."
    elif (alt_day2_convoy == 'dv'):
        show dv normal pioneer2 with dissolve
        dv "How'd you like my house?"
        me "Horrible!"
        "I honestly replied."
    pi "I wouldn't go there."
    th "Me too."
    me "I wasn't going to…"
    if (alt_day2_convoy == 'dv'):
        "The pioneer miraculously turned out to be nearby and cautiously glanced at Alisa.."
    else:
        "The pioneer miraculously turned out to be nearby and gave me a blank stare."
    "Just a kid, probably the age of Ulyana. Short, but with a mop of long unkempt hair."
    pi "Alisa and Ulyana live there."
    if alt_day_binder != 1 and (counter_sl_7dl < 2):
        "Hm. Well, that makes sense, considering they both were trying to break into canteen last night."
    if (alt_day2_convoy == 'dv'):
        dv "Alright, get out of here now."
        "She resoundingly flicked the kid, who, rubbing his forehead, has hurriedly left with all possible dignity."
        if alt_day1_us_shotted:
            th "I'm surprised she isn't aware of my accomplishments from yesterday."
        "I glanced at the redhead, and she impatiently shifted from foot to foot."
        dv "Are we leaving?"
        scene bg ext_houses_day with dissolve
    else:
        me "Alright. Hold on. THEY LIVE TOGETHER?!"
        th "If both beasts join forces - I'm done for."
        th "Nope, I'm not coming back here, never."
        scene bg ext_houses_day with dissolve
        "I turned to the pioneer, but he had already disappeared somewhere."
        th "All in all, certain brutality in the appearance of this house was more than understandable."
    th "Hm. Еhe pioneer's eyes were red. Where else could I see such eyes?"
    "Suddenly twilight came to mind.{w} And red-eyed internet addicts."
    "I looked around but nothing else caught my attention."
    th "I wonder, who else am I going to meet here?"
    $ alt_day2_dv_us_house_visited = True
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_event_dining_hall1:
    scene bg map_alt1 with dspr
    "What did Olga Dmitrievna say about schedule? If I want to eat that much, it’s easier to ask Slavya or Olga."
    "They're girls after all. They probably would have some snacks."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_event_sport_area1:
    scene bg ext_playground_day with fade
    play ambience ambience_soccer_play_background fadein 2
    play music music_list["went_fishing_caught_a_girl"] fadein 2
    if alt_day_binder != 1:
        "A quarter of an hour spent leisurely marching - and I came out to the already familiar football field."
    "Now that I had all the time in the world, I allowed myself to take a closer look."
    "It turns out that everything here was a little more complicated than a field with benches and one and a half metal bars."
    "No, the field itself, horizontal bars and bars have not gone away, but the devil is in the details, and this time new details have opened up to the eye."
    "First off, a fenced net court, equally suitable for both badminton and tennis."
    "A little further was a volleyball court, on which some girls I didn’t know were warming up."
    "The area was dominated by the vastness of an indoor gym for everyone who wanted to run in the rain or in winter, there were brick corners of showers nearby and, of course, toilets."
    "The field was occupied by some boys from the younger squads with the ubiquitous Ulyanka at the head, a shuttlecock was elastically thrown on the court - which means they also were from younger squads."
    "After standing for a while, looking for the PE teacher, I had to start thinking, since he definitely wasn't anywhere near my sights."
    "Obviously he's not at football, game's too spontaneous."
    "Training queens in badminton? Doubt it."
    "Volleyball? Maybe, but I don't see anyone there…"
    if counter_sl_7dl == 3:
        show sl normal pioneer with dspr
        sl "Boris Alexandrovich is lazing off again."
        me "Whoa, you know words like that?"
        show sl laugh pioneer with dspr
        sl "I didn't grow up in a tin can. {w}Actually speaking of cans… I think I know where I can find him."
        sl "Let's go."
        "She grabbed my hand and dragged me away."
    else:
        if ((alt_day1_sl_keys_took == 1) or (counter_sl_cl != 0)) and (alt_day2_convoy == 'sl'):
            us "Hey!"
            me "What do you want?"
            if counter_sl_cl != 0:
                show us grin sport with dissolve
                us "Got reamed by Olga Dmitrievna?"
                show sl normal pioneer at right with dissolve
                me "And how do you know?"
                "I squinted."
                us "HEH!"
                hide us with moveoutleft
                "Ulyana stuck out her tongue, cutely smiled and ran off."
                show sl sad pioneer with dspr
                sl "Now the entire camp's going to know."
                me "Is that bad?"
                sl "Not really. I'm just a little ashamed."
                "Ashamed because of such a small thing?"
            else:
                show us sad sport with dissolve
                us "You know Olga Dmitrievna was looking for you?"
                show sl normal pioneer at right with dissolve
                sl "No."
                "Cautiously responded Slavya."
                sl "What's up?"
                show us grin sport with dissolve
                us "How should I know? {w}Go and ask her!"
                us "If I remember correctly she was at the square last time I saw her."
                hide us with dissolve
                "Ulyanka ran to the bushes and fished out a ball."
                me "I'd first get a signature from PE teacher… Where is he, anyways?"
            sl "Let's go, uncle Borya always stays indoors."
        else:
            if alt_day1_us_shotted:
                play sound sfx_soccer_ball_kick
                extend " I sharply bent, letting a ball pass over me!"
                "From the football field half enthusiastically, half viciously came:"
                us "You ssssssssod!"
                show us angry sport at cleft with dspr
                me "Special delivery?"
                "I bowed, went to the curb and returned the ball to the game."
                me "Ulyana!"
                show us dontlike sport at cleft with dspr
                us "What?"
                "She murmured."
            else:
                "From the football field came a mischievous:"
                play sound sfx_soccer_ball_kick
                us "Newbie, catch!"
                if dr:
                    "But it was already too late."
                    "The ball reached its target." with hpunch
                    with flash_red
                    "I bent over, trying to take a breath."
                    "How did I even stay up is a mystery."
                    show us sad sport at cleft with dissolve
                    us "Hey, are you alive?"
                    me "Get… lost."
                    show us upset sport at cleft with dspr
                    us "Oh well, I'm worried about him, and he's snapping at me."
                    me "Shove your worries up your…"
                    show us grin sport at cleft with dspr
                    us "Where?"
                    "Oh how I wanted to actually say it!"
                    "The «stars» were still dancing before my eyes, but I finally managed to restore my breath and straighten up."
                    me "Ulyana!"
                    show us smile sport at cleft with dspr
                    us "Yes-yes?!"
                else:
                    "I barely dodged the ball flying at me."
                    "A little more, and I would've had the breath knocked out of me."
                    show us smile sport at cleft with dissolve
                    me "Kid, are you sane?!"
                    us "Oh come on. It's just a ball."
                    show us laugh sport at cleft with dspr
                    me "Someone definitely didn't get enough belt in their childhood."
                    show us grin sport at cleft with dspr
                    us "Who, me?"
                    "This red monster grinned."
                    us "I can't be spanked. I'm a girl!"
                    dreamgirl "A bad girl. And bad girls have to be punished!"
                    th "How do you even manage to pervert everything you touch?"
                    "The remark of the inner voice repulsed all desire to deal with the petty child."
                    me "Redhair!"
                    show us smile sport at cleft with dspr
                    us "What?"
            me "Where is the PE teacher, or his replacement?"
            show us normal sport with dspr
            us "Name, last name?"
            me "Anyone works. So where is he?"
            show us smile sport with dspr
            us "Asleep, probably. Look for him indoors, he sometimes sleeps on mats there."
            hide us with dissolve
            "For a change, I decided to listen to the information and moved towards the sports club. The door, on its well-oiled hinges, silently moved aside…"
    play sound sfx_open_door_clubs fadein 0
    scene bg int_sporthall_day_7dl with dissolve
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    play music music_list["went_fishing_caught_a_girl"] fadein 5
    if ((alt_day1_sl_keys_took == 1) or (counter_sl_cl != 0) or (counter_sl_7dl == 3)) and (alt_day2_convoy == 'sl'):
        "Slavya was right!"
    else:
        "Ulyana was right!"
    "In the far corner, squinting from the sun shining, the PE teacher was brazenly sleeping!"
    "I re-read the checklist — Boris Alexandrovich — came closer to the sleepyhead and tugged him on his shoulder."
    $ meet('ba','Sanich')
    me "Boris Alexandrovich!"
    ba "Mmmmm… Get lost."
    me "Boris Alexandrovich!"
    ba "Get off me!"
    "Without even waking up he turned to the other side and started sniffing again."
    th "And what am I supposed to do with him now? Squad leader probably wouldn't let me back into the house without a filled checklist, might even leave me to spend the night on the chairs amidst lilac bushes. That'd be romantic, no doubt, but wouldn't be very pleasant."
    "I looked thoughtfully at the fire shield, visible from here. On it hung a conical fire bucket."
    th "If I get some water…"
    if loki and (counter_sl_7dl == 0):
        th "Then it would be possible to arrange another extraordinary bathing for the natives."
    else:
        th "Then I could arrange a military wake-up call!"
    "And when I had almost made up my mind, mats creaked behind my back, and the person, on whom my cheerful and satisfying life depended, put his feet on the floor."
    "Waking up, he looked very gloomy and unfriendly, despite the fact that outwardly he was the same classic appearance that girls hung themselves on — straight Aryan nose, icy blue eyes and an anvil for a chin."
    "True icon of testosterone."
    show ba normal uniform with dissolve
    ba "Hey, pioneer. Whatchu want?"
    "He hooted."
    me "I… Here… Checklist."
    "I handed him a piece of paper, which the PE teacher, grimacing in disgust, picked up."
    show ba em1 uniform with dspr
    ba "The hell did you bring me?"
    "He crumpled the paper and tossed it away."
    ba "I'll sign it, and then what?"
    me "What?"
    ba "Here, see this?"
    "The physical education teacher belonged to endomorphs in physique, that is, he looked more fat than pumped up - but only until he strained his muscles."
    "His biceps with the size of my head suddenly swole up on his arm."
    ba "That's what you should strive for. Not for paper signing."
    me "You won't make a bodybuilder out of me in a single shift."
    ba "I won't. But I'll begin!"
    "In the last word, he stressed the second syllable."
    if (alt_day2_convoy == 'un'):
        ba "So that at least this badminton player didn't prefer someone stronger to you."
        me "Maybe she can decide that herself?"
        show un shy pioneer at right
        un "…"
        "The poor girl is bullied by everyone who wants to do so."
        ba "And she'll decide that if you are a hose, then you can only water the garden from you. Man must be stout!"
        show un normal pioneer at right
        me "Who would argue with that. A man always must."
    elif (alt_day2_convoy == 'sl'):
        ba "So that you'll be worthy of our clever beauty."
        ba "And what a disgrace it would be if she beats you on the bars?"
        show sl shy pioneer  at right
        sl "Boris Alexandrovich, if you want to scare away another pioneer…"
        th "I wonder, does «beating me on the bars» relate somehow to armwrestling?"
        show ba smile uniform with dspr
        ba "No way, kid. As for me bending him over — that's for his own good."
        show sl normal pioneer  at right
        me "If you're done haggling for me…"
        "I started hinting at something."
        "PE teacher looked at me as if it was his first time seeing me in his life."
    elif (alt_day2_convoy == 'dv'):
        ba "So that this redhead can rely on you."
        show dv smile pioneer2 at right with dspr
        dv "Rely?"
        me "In my opinion, for the latter, the carrying capacity is not critical."
        show dv laugh pioneer2 with dspr
        dv "That's what I'm talking about."
        "He got tired of listening to us and cleared his throat."
        show dv normal pioneer2 with dspr
    ba "You are a wimp now. And that I need to work with you. I understood correctly?"
    me "Right."
    "I answered dryly. I didn't like this guy's ratings."
    ba "Are you offended? Don't be."
    ba "Let's get you signed up somewhere. You want anywhere in particular?"
    show ba normal uniform with dspr
    me "Sign the checklist first, and then we'll see…"
    ba "Alright."
    "He bent down, picked up a crumpled sheet from the floor and drew something there."
    ba "Here you go."
    "I took the paper."
    ba "So we have football, volleyball and badminton. What's your choice?"
    if (alt_day2_convoy == 'un'):
        un "W-we can play together."
        "Lena offered."
        me "Together?"
        show un shy pioneer at right with dissolve
        un "Badminton."
    elif (alt_day2_convoy == 'sl'):
        sl "Join us for volleyball!"
        sl "We don't have any guys, but you wouldn't mind a female team?"
        "Actually I would mind. I know what kind of a shithole that could be."
        th "But Slavya's there…"
    else:
        "I could join Ulyana in her ball kicking escapades."
    menu:
        "Football":
            me "I'll kick the ball around."
            ba "Very nice! A man!"
            $ lp_us += 1
            $ list_joined_clubs_7dl.append('soccer')
        "Volleyball":
            me "I like jumping near nets."
            ba "Only girls are there. Although, you'll fit right in."
            if (alt_day2_convoy == 'sl'):
                "Slavya's there too. I'll be closer to her there."
                $ lp_sl += 1
            $ list_joined_clubs_7dl.append('volley')
        "Badminton":
            "I wasn't going to do sports. But this carcass, weighing 100kgs, looked at me, and, it seems like, he was preparing to devour me whole!"
            me "Badminton."
            show ba smile uniform with dspr
            ba "Bwa-ha-ha!"
            "Coach laughed, and suddenly stopped."
            ba "You serious?"
            me "Not everyone gets to break through walls with their head."
            if (alt_day2_convoy == 'un'):
                "He glanced at Lena."
                ba "I see. Nothing surprising here."
                ba "Pioneer! If I see you kissing on the court - you'll be running. {w}Twenty laps. Got that?"
                "I shrugged my shoulders without even turning around, already knowing that Lena had blushed again and was standing in a dumb stupor."
                $ lp_un += 1
            $ list_joined_clubs_7dl.append('badmin')
        "Nothing":
            me "Backgammon."
            "I answered and left the building."
    scene bg ext_playground_day with fade
    play ambience ambience_camp_center_day fadein 2
    if (alt_day2_convoy == 'un'):
        me "This guy is definitely something else…"
        show un smile pioneer
        un "Uncle Boris is a good guy, simply believes that everyone should be well developed."
        "She blushed a bit."
        me "«Well developed» — is harmonious muscles. What he wants is hypertrophia."
        show un laugh pioneer
        un "I'd look at you with muscles!"
        "So would I. Time, unfortunately, doesn't wait, so we have to keep going."
    elif (alt_day2_convoy == 'sl'):
        show sl smile pioneer with dissolve
        if (counter_sl_7dl == 3):
            me "This guy is something else…"
            sl "Ignore his behaviour."
            sl "But under his leadership, the football and volleyball teams took the first places several times!"
            me "Really?"
            show sl smile pioneer with dspr
            sl "Yes, last year first shift took gold in «Games-88»!"
            "I noted the year in my head for the future, and continued aloud:"
        me "Handsome man, huh?"
        "I looked at Slavya with a challenge, but she just smiled serenely in response."
        show sl laugh pioneer
        sl "Yes, Boris Alexandrovich is very eccentric. But I like a slightly different type."
        "I wonder what type is that?"
        me "Will you tell me?"
        show sl laugh pioneer with dspr
        sl "Nope. It's a secret."
        "Secret is a secret. I smiled and thought about my next destination."
    elif (alt_day2_convoy == 'dv'):
        me "I bet all the girls hang themselves on that bear."
        show dv smile pioneer2
        dv "How else would it be! Such a prominent man, with such cans. Why not to hang on him?"
        me "Ha-ha-ha. And you? Hanging on him?"
        show dv laugh pioneer2 with dspr
        dv "Of course, yeah. Wait for him to come out and we'll both be hanging."
        "I smirked and thought about my next destination."
    else:
        "After barely escaping from that bear and avoiding a couple of dozen push-ups, I allowed myself to take a breath."
        "Do they just hire people with their only criteria being «maximum trolling»?!"
        if ('medic' in list_voyage_7dl):
            "First Viola, now this guy…"
        me "I need to get out of here."
        "Where to though?"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_event_beach1:
    stop ambience fadeout 1
    scene bg ext_beach_day with fade
    $ alt_day2_beach_seen = True
    pause(1)
    play ambience ambience_lake_shore_day fadein 1
    "The beach was much wider, bigger and prettier than on the map."
    "The silvery sand only slightly shone in the sun, but it was decidedly impossible to look at the watery surface of the bay - the eyes began to water.."
    "Seeing the beach, I immediately wanted to take a dip - the day was hot."
    "I started taking the shirt off…"
    if (alt_day2_convoy == 'sl'):
        show sl serious pioneer with dissolve
        sl "Semyon, what are you doing?"
        me "I would like to…"
        show sl smile pioneer with dspr
        sl "I understand that you want to, but let's finish the detour first, shall we? Okay?"
        show sl smile2 pioneer with dspr
        sl "The water will warm up by noon! Let's go then!"
        "Sighing, I agreed."
        "Quarrelling with my charming guide definitely wasn't in my plans."
    else:
        show mt smile swim2 with dissolve
        mt "Hey."
        th "That's where she went… {w}to work!"
        show mt grin swim2 with dspr
        mt "I see you have already walked around the entire camp and got to know everyone?!"
        "She wryly smiled."
        th "That swimsuit fits her."
        me "Yeah, getting to know people, slowly."
        show mt normal swim2 with dissolve
        "Olga Dmitrievna incredulously shook her head."
        mt "Of course! And you're ready to present your checklist?"
        "And without letting me put in a word, she continued:"
        show mt angry swim2 with dissolve
        mt "Don't even dream about the beach until you meet everyone!"
        "Apparently it was her final decision…"
        "Crap! The water shimmered so amazingly in the sun, and the soft waves directly beckoned me!"
        "I remembered that I not once had been to a sea…"
        th "Although this isn't even a sea."
        me "I'll just dip once - and immediately go ahead with the list!"
        me "Promise!"
        show mt smile swim2 with dspr
        mt "Don't {w=0.2}even {w=0.2}dream{w=0.2} of it!"
        hide mt with dissolve
        "And, smiling, she went to the water!"
        th "What kind of camp is this? Corrective, right?!"
        me "Can you at least tell me the river's name?"
        "I yelled."
        "She just waved."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_event_me_mt_house1:
    if not alt_replay_on:
        if been_there_alt1() > 1:
            scene bg ext_houses_day with fade
            th "What am I doing here?"
            stop music fadeout 3
            stop ambience fadeout 6
            with fade
            return
    scene bg ext_house_of_mt_day with fade
    "I came to the house that was to be mine for these few days, and stopped…"
    "Didn't want to sleep. At all."
    th "What the heck? The sun, clean air - take it while you can!"
    th "I may have been sent with a checklist, but I can just walk around, right?"
    th "Guess I'll go do that then!"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_event_library1:
    scene bg ext_library_day with fade
    if alt_day2_convoy not in ('dv', 'sl', 'un'):
        "Estimating that the library is the closest from here, I turned there."
    else:
        "Estimating that the library is the closest from here, we turned there."
    "The path to the temple of knowledge reminded me of my city, of the inglorious struggle of the city authorities with bad asphalt."
    "And so they kept relaying it this and that way."
    "For some reason, the idea of not pocketing half the budget didn't occur to anyone."
    "So they ended up giving up and ordering tiles from the granite factory. Yes. Tiles. At the factory. At a price about twenty times higher (per square meter) than the asphalt pavement. How the story ended, I think everyone knows."
    "But here the tiling was still brand new, didn't have the time to wipe off and crack here and there, so it was a real pleasure to walk on it. Soon a small wooden building in the outskirts opened up to my eyes, where the sounds of camp life didn't reach."
    "There was a brick firehouse next to it in case a fire suddenly broke out in the library… Although I don't think this has saved a single library before."
    "Catching myself thinking that I had been stomping on the doorstep for several minutes, I pushed the door and entered the temple of knowledge."
    play sound sfx_knock_door3_dull
    pause(1)
    play sound sfx_open_door_1
    stop ambience fadeout 1
    stop music fadeout 3
    pause(1)
    scene bg int_library_day with fade
    play ambience ambience_library_day fadein 1
    "It was quiet, it smelled of book dust and drying glue."
    play music music_list["get_to_know_me_better"] fadein 1
    "With the exception of the abundance of Soviet symbols, everything here was the way I used to see in libraries - five shelves for the Great Soviet Encyclopedia, posters - or placards? - with calls to study, study and study again…"
    "Tables and chairs for those who want to read here, frivolous tulle on the windows, a sleeping librarian, a bureau with reader cards."
    "Stop."
    "I scrolled through my memory back and turned around."
    if alt_day2_convoy not in ('dv', 'sl', 'un'):
        "Right, I'm not alone!"
    else:
        "We weren't alone in the library!"
    "On the desk, assuming the «I'm not sleeping, I'm dealing with small details pose, was sleeping …{w} the librarian?"
    scene cg d2_micu_lib with dissolve2
    "She's fast asleep here!"
    scene bg int_library_day with dissolve
    if (alt_day2_convoy == 'un'):
        show un normal pioneer far at fright with dissolve
        if loki:
            "Deciding not to disturb the righteous dream of an employee of the intellectual front for now, I walked along the shelves."
            "A noise caught my attention and I moved on. As we went on, the noise became more orderly, a little later it broke into several parallel parts, until I realized that these were voices!"
            "Just coming from some extremely well soundproofed room!"
            me "Did you hear anything?"
            un "Yes… Shurik and Electronik are arguing about the newspaper again."
            "Lena whispered."
            me "You have your own newspaper?"
            un "Wall newspaper. Meetings are usually after lunch. I'm drawing."
            me "Whoa, I already want to see!"
        elif herc:
            "Hot breath scorched my ear, and I smoothly went crazy."
            un "Editorial office of the newspaper is in the storage."
            me "Papparazi?"
            un "Shurik, Danya and Electronik."
            "Seriously answered Lena."
            un "They all deal with organization for the most part."
            un "I draw."
            me "So you need a reporter? Well, we could try that. But you have to show your drawings to me!"
            show un smile pioneer far at fright with dspr
            un "Okay."
        else:
            un "Want to try being a journalist?"
            me "Newspaper?"
            "I remember, in a far, far away childhood, I did something like that… Maybe I should come back to my roots?"
            un "Yeah… The editorial is nearby. We can visit. Shall we?"
            me "Eh, let's go!"
    elif (alt_day2_convoy == 'sl'):
        show sl normal pioneer at fright with dissolve
        sl "Do you want to sign up for the newspaper? Tea and biscuits included!"
        me "What would I need to do?"
        show sl smile2 pioneer at fright with dspr
        sl "Work!"
        me "Let's at least see what kind of animal this is - a wall newspaper."
    elif (alt_day2_convoy == 'dv'):
        show dv normal pioneer2 at fright with dissolve
        dv "The boys come here after dinner."
        me "Why?"
        dv "Who knows? Maybe they're playing cards."
        show dv laugh pioneer2 at fright with dspr
        dv "Or court this grouch."
        me "Or drink tea with biscuits."
        "I froze up."
        me "Hush!"
        show dv surprise pioneer2 at fright with dspr
        dv "What?"
        me "Listen closely."
        show dv normal pioneer2 at fright with dspr
        dv "Someone's talking nearby."
        "We looked at each other."
        me "Let's go!"
    else:
        "Deciding not to disturb the righteous dream of an employee of the intellectual front for now, I walked along the shelves."
        "A noise caught my attention and I moved on. As we went on, the noise became more orderly, a little later it broke into several parallel parts, until I realized that these were voices!"
        "Just coming from some extremely well soundproofed room!"
    "I went to the door - the most trivial dark rectangle, upholstered in leatherette, and carefully pulled the handle."
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg int_editorial_day_7dl
    with dissolve
    "The hinges creaked softly, revealing my presence, and the arguing people instantly fell silent, turning in my direction."
    me "Greetings…"
    "I awkwardly gave my greetings."
    show sh normal pioneer far at center
    show el normal pioneer far at cleft
    with dissolve
    sh "Well, come in, if you already came. And close the door! Or Zhenya will take off our heads for the noise in the holy place."
    "I closed the door tightly behind my back and looked around."
    "In fact, it was something like a book depository with the possibility of conservation - a small nook with windows on profiles and a prehistoric monster as a central air conditioner."
    "«BK», — I read, looking closer. Famous brand."
    "Those present silently awaited my entry."
    if (alt_day2_convoy == 'un'):
        show un smile pioneer at fright with dissolve
        un "Well, here we are…"
        "She pointed to the canvas standing near the window."
        un "My workplace."
    else:
        show un smile pioneer far at fleft with dissolve
        "Lena also was there, taking a seat in a corner by the window and diligently drawing something. Catching my eye, she showed a hint of a smile."
        "I nodded and turned around to the others."
    if ('cyber' in list_voyage_7dl):
        if alt_day_binder != 1:
            "Shurik and Elektronik were seated nearby at a large table."
        else:
            "Nearby at a large table were the very only representatives of the stronger sex in the squad."
            th "If I understand correctly, the one with the glasses is Shurik, so his partner's name is Electronik."
            th "Is that really his name? Or is it some kind of nickname?"
        me "Hello again!"
        show sh serious pioneer far with dspr
        if (alt_day2_convoy == 'un'):
            show un normal pioneer at fright with dspr
        elif (alt_day2_convoy == 'sl'):
            show sl normal pioneer at fright with dissolve
        elif (alt_day2_convoy == 'dv'):
            show dv normal pioneer2 at fright with dissolve
        sh "Hello."
    else:
        "Most of the room was occupied by a table."
        if alt_day_binder != 1:
            "Behind it was Electronik and a guy subtly resembling Alexander Demyanenko."
            me "Shurik!"
            "I let out a shout."
        else:
            "Behind it were both representatives of the stronger sex in the squad - excluding, of course, me."
            "One was very reminiscent of the hero of Veltistov’s book, there was no doubt about it."
            "And in the other one you could recognize the hero of Soviet comedies."
            me "Shurik and Electronik?"
            "The blonde guy nodded."
        $ meet('sh','Shurik')
        $ alt_day2_sh_met = True
        $ meet('el','Electronik')
        show sh serious pioneer far with dspr
        if (alt_day2_convoy == 'un'):
            show un normal pioneer at fright with dspr
        elif (alt_day2_convoy == 'sl'):
            show sl normal pioneer at fright with dissolve
        elif (alt_day2_convoy == 'dv'):
            show dv normal pioneer2 at fright with dissolve
        sh "Shurik, yeah. Are you new here?"
        me "Why do you ask… {w}As if you weren't at the lineup."
    sh "Straight into the editorial office of our newspaper? Very responsible of you, good job. Now, tell us."
    me "Uhhhh… Tell what?"
    show el normal pioneer far at cleft with dspr
    el "Field news!"
    el "Tell us, why are you here?"
    "They looked at me so expectantly that I got flustered."
    me "I looked around, heard your voices, and…"
    sh "Alright. So. You got a good look in?"
    sh "Took part? And we should get back to work."
    show sh normal pioneer far with dspr
    "I thought about it. Journalists, usually, have a good score with the squad leaders and the authorities of the camp. {w}Maybe I could use that?"
    menu:
        "Sign up":
            me "Can I sign up?"
            $ list_joined_clubs_7dl.append('nwsppr')
            $ lp_un += 1
            sh "No. We don't have vacant places."
            me "Are you sure? As far as I can see there's two and a half people here. Who collects news then?"
            el "He is right. Not everyone can draw. Someone needs to work in the field."
            "Shurik pondered."
            sh "I don't think that's a good idea."
            if (alt_day2_convoy == 'un'):
                if loki:
                    show un serious pioneer far at fright with dspr
                    un "We really don't have enough journalists."
                elif herc:
                    show un normal pioneer far at fright with dspr
                    un "Maybe we can give him a test task?"
            elif (alt_day2_convoy == 'sl'):
                show sl serious pioneer at fright with dspr
                sl "Sasha, what's wrong with you? A person wants to help you work, and you're putting on airs here!"
                sl "Be more polite, otherwise I'll close your almshouse."
                th "Wow! Slavya, it turns out, can use her authority!"
                show sh upset pioneer far with dspr
                "The bespectacled guy wilted and continued much less confidently."
            elif (alt_day2_convoy == 'dv'):
                dv "It's kinda cute here!"
                show dv normal pioneer2 far at fright with dspr
                "Alisa looked around impudently."
                dv "I think I know where I'm going to be visiting during quiet hour from now on."
                show sh scared pioneer far at cright with dspr
                sh "What?!"
                show dv grin pioneer2 far with dspr
                dv "What? Squad leader doesn't come here, there's always somewhere to hide. Great place."
                show un shy pioneer far at fleft with dspr
                un "Maybe it's better to let them do what they want?"
                "Hesitantly suggested Lena."
                sh "Looks like we don't have a choice."
            else:
                if loki:
                    show un serious pioneer far at fleft with dspr
                    un "We really don't have anyone collecting info."
                if herc:
                    show un normal pioneer far at fleft with dspr
                    un "Maybe we can give him a test task?"
        "Don't sign up":
            me "Well, I won't be distracting you any longer."
            "I told them."
            me "Looks like you do not have enough space even without me. Arrividerci!"
            play sound sfx_open_dooor_campus_1
            pause(2)
            scene bg int_library_day with dissolve
            "I waved and went out of the vault back into the library."
            "And immediately froze."
            return
    me "Shurik, I won't bother you here, remember? I am a correspondent, so I will work there, outside."
    show sh surprise pioneer far with dspr
    "Shurik blushed a little - apparently, my words were not entirely appropriate - however, he quickly calmed down and began furiously throwing paper piles on the table in search of something incomprehensible."
    show sh normal_smile pioneer far at cright behind un with dissolve
    sh "Aha!"
    "There was a piece of paper in his hand."
    sh "Your task!"
    "Shurik looked at me triumphantly."
    sh "Every session, vacationers arrange a big concert on the day of amateur performances. Write about it."
    me "About what?"
    "Dumbfoundedly I asked again."
    sh "About self-activity! I already know a few people who are preparing, but I won't help you. Write one sheet, bring it to us and we will either issue it or rewrite it… Depending on how terrible your handwriting is… And then we'll paste it into the newspaper. That'll be our «high life» column. You got everything?"
    me "Got it…"
    sh "I'll be at the usual place, if you need me. Good luck."
    "It occurred to me that the four-eyed found an amazing way to get rid of me by giving me an impossible task."
    if (alt_day2_convoy == 'un') and dr:
        show un smile pioneer with dspr
    else:
        show un sad pioneer far with dspr
    "Lena looked at me sympathetically, and instead of the usual indifferent acceptance, a certain spark suddenly appeared inside!"
    "I don’t know what it was, anger, excitement or unwillingness to be pushed into the neck, but I grabbed a piece of paper and shouted: «Wait for the story!» — and jumped out of the room."
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg int_library_day with dissolve
    with fade
    return

label alt_day2_mz:
    scene bg int_library_day
    $ meet('mz','Librarian')
    mz "Who's yelling here?"
    "I heard a raspy voice."
    mz "If it's this damn Danya misbehaving again…"
    show mz normal glasses pioneer with moveinleft
    "A few seconds later, the same sleeping librarian appeared between the shelves."
    "Now that she was standing and being active, I was able to see her a little better."
    "Dark, shimmery, short hair, a funny swirl on top, reminiscent of a question mark in shape."
    "Eyes of a menacing yellow color, hidden behind glasses with an incalculable number of diopters."
    "Add an extremely grumpy facial expression, and here she is, - the librarian vulgaris."
    mz "Who are you?"
    "The voice matched her - creaky, with grumpy master notes."
    mz "Why are you in the library with no reader card? Why are you screaming?"
    "Her voice was rather sharp, and her tone was not pleasant at all."
    me "I…"
    mz "Come here."
    "She nodded to me and, without turning around, hurried to her place."
    th "Do they all either really don't care if I'm following them, or are they so sure of their own irresistibility?"
    "I froze on the spot, and then the librarian turned around with hostility."
    mz "Why are you standing there, keep walking."
    "We got out into the main room, where she, without further ado, extended her hand to me."
    mz "Give!"
    "I timidly held out my hand to her."
    mz "The other hand!"
    "They really hire psychos in libraries?"
    mz "Come on!"
    "Her tone was not very friendly, and she clearly wasn't going to wait."
    "I timidly held out my hand to her again, now the one with the checklist. The librarian took the paper and unfolded it on her desk."
    mz "Mhm. Newcomer, huh?"
    "I kept my silence."
    mz "And you need my signature."
    th "No, I'm here to learn drums."
    mz "Here."
    "She artistically signed and sent the sheet across the table in my direction."
    mz "Gonna register a card?"
    me "What?"
    show mz bukal glasses pioneer with dissolve
    mz "Will you register for a reader's card?"
    "Patiently, as if talking to a mentally retarded person, she explained."
    mz "Borrowing books, reading. Do you get it?"
    me "Ah… No. Don't need it."
    "It occurred to me that the works on Marxism-Leninism are somewhat different from what it makes sense to fill your head with in such weather."
    mz "Then I would rather not delay you."
    "The librarian said in a voice that brooked no objection."
    "I looked into the checklist again - the signature opposite the column read «Zhenya Z.»"
    $ meet('mz','Zhenya')
    me "I'm Semyon, by the way."
    if ('medic' in list_voyage_7dl):
        "This time I processed things faster and introduced myself at the end of the conversation, and not at the door."
    mz "Nice to meet you."
    "Her tone contradicted her words."
    hide mz with dissolve
    scene cg d2_micu_lib with dissolve
    "She rested her head on her folded arms and sniffled."
    mz "The door is right behind you."
    "Without opening her eyes, she indicated."
    mz "Don't mix it up."
    "Shrugging my shoulders, I went outside. It's better not to communicate with such pests. Let her keep sleeping."
    mz "Don't bother trying to slam the door. There's a stopgap."
    stop ambience fadeout 1
    stop music fadeout 2
    scene bg ext_library_day with fade
    play ambience ambience_camp_center_day fadein 1
    "Startled at how successfully the mischievous librarian guessed my intention, I hurried to leave this vile institution."
    if (alt_day2_convoy == 'un'):
        me "Guhhh, what a buzzkill!"
        show un smile pioneer with dissolve
        un "Zhenya's good… I don't know why she treated you like that."
        me "I know why though. It's because she's a buzzkill."
        show un laugh pioneer with dspr
        un "Well, there's your answer. Alright, let's go."
    elif (alt_day2_convoy == 'sl'):
        me "Guhhh, what a buzzkill!"
        me "Can't you just make do without spitting in other people's souls?"
        show sl smile2 pioneer with dissolve
        sl "Zhenya is good. Don't bully her."
        me "Me?! Bully?!"
        me "She herself can bully anyone she wants!"
        show sl laugh pioneer with dspr
        sl "Don't be upset, give her a chance. Alright, what do we have next?"
    elif (alt_day2_convoy == 'dv'):
        me "Guhhh, what a buzzkill!"
        show dv smile pioneer2 with dissolve
        dv "Yeah, she's a rare pest. Although it seemed like she liked you?"
        me "For the love of God, please no!"
        show dv laugh pioneer2 with dspr
        dv "Let's go! We still need to go to a bunch of places."
    else:
        th "Guhhh, what a buzzkill!"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_event_medic_house1:
    if not alt_replay_on:
        if been_there_alt1() > 1:
            scene bg ext_aidpost_day with fade
            th "Nope, I definitely don't have anything else to do here."
            return
    scene bg ext_aidpost_day with fade
    if (alt_day2_convoy == 'sl'):
        show sl serious pioneer
        sl "You didn't eat anything at the breakfast."
        "The girl scolded me."
        me "Excuse me, can't really stomach oatmeal right now."
        me "There's a clever word for that - acclimatization!"
        sl "Oh please! Well, since we're going past the infirmary anyways, let's at least show you to Violetta Cernovna."
        "I suddenly felt deathly chill from a massive herd of goosebumps running across my back when I heard that name."
        me "Uhhh… Maybe we shouldn't?"
        sl "We should!"
        "She grabbed my hand and dragged me along the path towards the infirmary."
        sl "You know how important it is to take care of your health! You don't save it from a young age, then you work for medicines all your life. So we're going to the infirmary, stop complaining."
        if alt_day1_us_shotted:
            "We almost reached the infirmary, but then…"
            dv "What, newbie, found yourself a babysitter?"
            show dv normal pioneer2 at right with dspr
            "A familiar hoarse voice rang out from behind."
            "Alisa."
            show sl angry pioneer with dspr
            sl "Dvachevskaya, what do you want?"
            "Slavya squinted with hostility."
            dv "What do I want? Nothing much. {w}Our hero screwed up a bit yesterday, you know. {w}And didn't clean up after himself. Not a pretty sight. {w}Unhygienic, even."
            if (counter_sl_7dl == 0) and (alt_day_binder != 1):
                sl "You were the one who tried to pour water on him yesterday!"
                "Slavya tried to reason with the hooligan, but she didn’t even listen."
                "I, myself, stood aside and, again surprised at myself, enjoyed the conflict. Although I vaguely suspected that my nose was at stake again."
                if loki:
                    dv "The showering - we ourselves forgot about it already. Yeah, we're guilty, shouldn't have believed any passing crooks. But the unsightly scene at the football field… Oh, no-no-no."
                else:
                    show dv surprise pioneer with dspr
                    dv "What does that have to do with this?"
                    "Alisa was surprised."
                    show dv smile pioneer with dspr
                    dv "I'm talking about the fact that someone yesterday gave Ulyana an acute attack of asphalt disease, due to which she spent half the night whining. Do you catch my drift?"
            else:
                sl "In the canteen Ulyana herself is to blame, it’s a pity Semyon didn’t catch her!"
                dv "Didn't catch? Oh, so he hasn't told you, has he?"
                "She grimaced."
                dv "So, our hero hasn't shared his adventures?"
                dv "Turns out he kind of did catch Ulyana yesterday."
                sl "Semyon, what is she on about?"
                me "Well…"
                "It's always hard to admit your own cruelty."
                me "I used alternative methods."
            show dv smile pioneer close at right with dspr
            "Dvachevskaya came around Slavya, who did not have time to react, and stood right in front of me, looking into my eyes."
            if alt_day_binder != 1:
                dv "You think you offend a kid and immediately become a hero, right? Could not catch up, so hit the back."
            else:
                dv "Or do you think that since you're big and strong you're allowed to do anything?"
            "She spoke in a calm voice, but mischievous imps danced in her eyes, and I realized that this whole scene was conceived solely for the purpose of teasing us."
            me "Are you her lawyer?"
            if dr:
                "I really wanted to look away, especially since it was extremely difficult for me to maintain eye contact with the girl."
            me "Came to negotiate?"
            dv "No. I came to say that if you are not a coward, then today, near the stage, we will discuss your behavior and draw conclusions."
            me "And if I'm a coward?"
            dv "Then we'll draw the conclusions without you. Oh, and believe me, you won't like them."
            "Dvachevskaya turned around and headed off. Without turning, waved."
            dv "Adieu, newbie. At the stage at six. Don't be late."
            hide dv with dissolve
            "Red-haired bandit wants a showdown with me because I gave her little friend a taste test of the nearest lawn. Yup, all is as it should be! Hope she doesn't bring an entire gang with her. I definitely won't stand a chance against multiple pioneers alone."
            show sl normal pioneer with dspr
            sl "Will you go?"
            me "Of course! Youth! When else do you throw hands!"
            "I can't just tell her that everything inside me is shaking from nervousness!"
    "After a little hesitation - I remembered yesterday's examination with a fondness - I knocked on a wooden door with a large window at the top."
    cs "Open."
    stop ambience fadeout 2
    play sound sfx_open_door_1
    pause(1)
    scene bg int_aidpost_day
    with dissolve
    play ambience ambience_medstation_inside_day fadein 3
    play music music_list["eternal_longing"] fadein 5
    show cs normal at center
    if (alt_day2_convoy == 'un'):
        show un normal pioneer far at fright
    elif (alt_day2_convoy == 'sl'):
        show sl normal pioneer far at fright
    elif (alt_day2_convoy == 'dv'):
        "Aware of nurse's reputation, Alisa decided to calm her rebellious habits a little - she even agreed to fix her uniform for a short time."
        show dv normal pioneer far at fright
    "So I came in. I mean, what else could I do?"
    "I definitely didn't need any medical services. Actually, even my tantrum from yesterday could be easily solved with the help of a single bucket of cold water."
    if alt_day_binder != 1:
        if loki and (counter_sl_7dl == 0):
            "Unfortunately, yesterday my quota has been fully donated to the redheads, so I had to work with what I had."
        elif herc and (counter_sl_7dl == 0):
            "Thankfully, I managed to escape that bucket yesterday… And stole the main culprit, at that."
        elif dr and (counter_sl_7dl == 0):
            "Well, I did get that bucket after all."
    else:
        "Unfortunately, I have managed to avoid that bucket."
    me "Um… Hel…"
    show cs normal far at center with dissolve
    "My throat went dry and I swallowed the end of the word. From behind a table in the back of the room, a short but extremely curvaceous, heterochromatic girl stood up."
    "For anyone else, it would look like some kind of ugliness, I guess. But here… For some reason, she looked like a predator, even if it was the caliber of a domestic cat, and, like with a cat, it was completely impossible to predict events with her."
    "She knew that, and shamelessly used it."
    cs "Well, hello there… pioneer."
    "If I tried to reproduce this smile, the grin would turn out to be the most obscene!"
    me "Greetings, V-Viola…"
    cs "Sit down."
    "I looked around the room."
    cs "On the couch."
    "I sat down."
    cs "Strip."
    "She evenly continued."
    me "Why???"
    cs "We'll be re-examining you. In case I missed something yesterday."
    show cs smile far with dspr
    cs "Well, what are you waiting for? For me to undress you?"
    "Judging by the expression of her eyes, that thought was very amusing."
    me "Uhh… Well I… Honestly… I feel great!"
    "I replied, constantly gulping."
    me "As for your medication… I don't need it. Yeah."
    cs "Your feelings don't matter."
    show cs shy with dspr
    cs "I have prepared an {i}individual{/i}…"
    "She said the last word in such a way that it sounded like a new pose from «Kamasutra»."
    cs "…course, especially for you."
    if (alt_day2_convoy == 'un'):
        show un shy pioneer far at fright
    elif (alt_day2_convoy == 'sl'):
        show sl shy pioneer far at fright
    elif (alt_day2_convoy == 'dv'):
        show dv shy pioneer far at fright
    me "I'm perfectly healt…"
    cs "Don't be like that."
    show cs shy close with dspr
    "She took another step, entering my personal space, and I involuntarily cringed at her intent, almost x-ray look."
    cs "What if you're in heat?"
    "I couldn't even react, and she already put her hand on my forehead."
    "I think it would be redundant to say that it was on fire."
    "I myself sat, red as a lobster, all covered with goosebumps from a mixed feeling of fright and enthusiasm."
    cs "See."
    "She removed her fingers and spoke in a deliberately languid voice."
    cs "You're on fire, pioneer. Strip."
    me "What?!"
    cs "Let's have a session of…"
    "She began, stretching every vowel."
    cs "…rubdowns. From my individual course."
    "She quickly reached out and undid the top button of my shirt."
    if (alt_day2_convoy == 'un'):
        show un laugh pioneer far at fright
        "I heard a soft laugh and turned around."
        "Lena, who was supposed to give me moral support, stood and giggled treacherously!"
        "In her eyes, I did not notice any anger, or embarrassment, or anything like that."
        cs "Remember that, pioneer. That's the only way you can deal with them."
        "Viola said partingly."
        un "I'll keep that in mind, doctor."
    elif (alt_day2_convoy == 'sl'):
        show sl tender pioneer far at fright
        sl "S-semyon, I'll wait for you outside, alright?"
        show cs smile close at center with dspr
        cs "Sit down, pioneer. Maybe you'll become useful in time?"
        sl "Why?!"
        cs "Who knows. Maybe I won't be enough, and we'll need extra hands."
        th "WHAT?!"
    elif (alt_day2_convoy == 'dv'):
        show dv surprise pioneer far at fright
        dv "You uhh… if you're gonna go all out, then…"
        dv "Can I just leave?"
        show cs smile close at center with dspr
        cs "Where are you going? Strip too."
        dv "Why?!"
        cs "To avoid any splashes on your clothes."
        dv "WHAT?!"
        cs "During rubdowns."
    me "Actually I'm… I'm, here!"
    "I mumbled, while hiding behind the paper."
    me "I was sent with the checklist."
    show cs smile close at center with dspr
    cs "But that wouldn't stop you from taking care of your health, would it?"
    show cs grin close at center with dspr
    show cs smile close at center with dspr
    "Winking at me, she moved even closer, so that our knees were almost touching, and… {w}Grabbed the list from my hands, bringing it closer to her eyes."
    hide cs with diam
    "Twirling the paper in her hands she turned around and went to the table. And I… What could I do? Allowed myself to breathe, that's what! Although it didn't last long."
    play music music_list["two_glasses_of_melancholy"]
    scene cg d5_cs
    with dissolve
    "The pen of the awkward nurse was very slippery and fell to the floor."
    "Clasping her hands, she bent down to pick it up, bending along the way like…"
    "Like I forgot how to breathe again, and for a moment recalled animes where the aroused characters get nosebleeds."
    th "I don't even know how to breathe here at this point, with my nose, mouth?!"
    "Viola returned the sheet back to me, and lightly directed me towards the exit."
    cs "Come back often… pioneer. To take care of your health, and, you know… Just to visit."
    "She velvety laughed, and I shuddered again."
    play sound sfx_close_door_1
    scene bg ext_aidpost_day with fade
    play ambience ambience_camp_center_day fadein 2
    if (alt_day2_convoy == 'un'):
        me "What the hell was that?!"
        show un smile pioneer
        un "And I thought you liked it."
        "I have never seen Lena like this - she had fun with all her heart."
        me "I think I almost got eaten."
        show un laugh pioneer
        un "You wouldn't be eaten whole. She'd leave your slippers intact."
        "I smiled and figured out where to go next."
    elif (alt_day2_convoy == 'sl'):
        me "So that's the doctors working here?"
        show sl shy pioneer
        sl "Don't be angry with Violetta Cernovna. She has a very difficult post…"
        "Which she seems to be enjoying a ton."
        me "Oh so that's where you brought me."
        me "I almost got eaten there."
        show sl laugh pioneer
        sl "You wouldn't have. You're a big guy."
        "I smiled and figured out where to go next."
    elif (alt_day2_convoy == 'dv'):
        me "Have you seen THAT?"
        show dv smile pioneer2 with dissolve
        dv "What? Performance «Pioneer Semyon in the role of the Valdai virgin»?"
        "Alisa smiled, re-tying her shirt."
        me "Grrr…"
        show dv laugh pioneer2
        dv "Oh, please… Just a bit of encroaching on innocence."
        "I smiled and figured out where to go next."
    else:
        "Escaping from the hellish house, I allowed myself to catch my breath and wipe the sweat from my forehead. This is not a nurse, this is some kind of embodied pioneer fantasy!"
        "I turned around and with a 'smart' face said through the closed door:"
        me "And my name is Semyon."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_event_estrade:
    scene bg ext_stage_big_day_7dl with fade
    "And then I didn't have anywhere to go - everything was filled out with signatures."
    "Even though they were in random places."
    if not ('sport_area' in list_voyage_7dl):
        "Instead of PE teacher's signature there was an entirely different one."
        "But, if I ever see him, I'll probably recognize him."
        $ meet('ba','Sanich')
        "I repeated his name in my head."
    "There was still a little time before lunch, so I decided to take a walk to the stage."
    if (alt_day2_convoy == 'dv'):
        "Valuable cargo from this morning still haunted me."
        "That's an entire free amplifier!"
        scene bg ext_stage_near_clear_7dl with dissolve
        "I climbed onto the stage and made a cursory revision of the equipment."
    else:
        "Since I decided to inspect the entire camp, it would be a sin not to see the center of local amateur performances."
        "Freshly planed boards smelled pleasantly of resin, and the shade inside beckoned to leave the sun."
        "Looking around - nobody was nearby - I went up to the stage."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_dubstep:
    scene bg ext_stage_normal_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    th "Control panels, speakers… Good equipment! I wish I could take it home…"
    th "Mic!"
    if alt_day2_minijack:
        if (alt_day2_convoy == 'sl'):
            "After walking around the stage for a bit, I couldn't bring myself to act a little under Slavya's searching gaze."
            th "Time for congratulations, long-eared Semyon?"
            dreamgirl "Hey, will you invite me to your wedding?"
            th "Screw you! I really like Slavya, but to talk about anything serious… After all, she's a girl."
            th "Ugh, quiet!"
            th "I mean, she's underage."
            dreamgirl "Can you tell her all of that face to face?"
            sl "Semyon, what are you doing?"
            me "I want to do something…"
        play sound sfx_click_1
        "I walked up and flipped the switch."
        $ lp_us += 1
        th "How long has it been since I last stood on the stage…"
        "I hit a few notes, listening to the acoustics of space, and then I laughed and waved my hand - what the hell, you ask?!"
        "Turning off the microphone, I patted my pocket, where the recently obtained minijack was, and headed towards the equipment."
        "If there will be a disco in the camp, the speakers will be taken from here. And I guess amplifiers too. So everything you need is here. And if not…"
        if (alt_day2_convoy == 'dv'):
            "In general, the stage made an impression! A huge half of the decagon hung like a tent over the main stage, three jupiters were placed under the very roof, and on a table near the far wall there was an amplifier we left there in the morning."
        else:
            "In general, the stage made an impression! A huge half of the decagon hung like a tent over the main stage, three jupiters were placed under the very roof, and on a table near the far wall stood… {w}Bingo! An amplifier!"
    stop music fadeout 3
    with fade
    return

label alt_day2_dubstep2:
    scene bg ext_stage_normal_day
    if (alt_day2_convoy == 'un'):
        $ lp_un += 1
        show un normal pioneer at fright with dspr
        un "What are you going to do?"
        me "I thought about singing for a beautiful lady, but my voice seems to be off."
        show un shy pioneer at fright
        un "But then…"
        me "That's why I decided to play!"
    elif (alt_day2_convoy == 'dv'):
        $ lp_dv += 1
        show dv normal pioneer2 at fright with dspr
        dv "Hey, what are you doing to my amp?!"
        me "Patience. You'll see everything soon."
        show dv angry pioneer2 at fright with dspr
        dv "But if anything happens to it…"
        me "Relax and enjoy!"
    "Then it wasn't even easy, it was elementary - plug in the player…"
    "…poke around the amp's inputs to find the signal input…"
    "…the speakers barely audibly hummed, and I turned up the volume."
    show us smile sport with dissolve
    us "Hey, what are you doing here?"
    "The small demon seemed to have played for long enough and now decided to pester me."
    play sound sfx_7dl["ghmm"]
    "I snapped my fingers:"
    me "Going to play music."
    show us laugh2 sport with dspr
    us "But the disco is tomorrow, you'll hear enough then."
    me "And I want today. I'm a music lover."
    show us grin sport with dspr
    us "You're a dumbass."
    $ alt_day2_us_dubstep = True
    "She climbed onto the speaker and, hanging from it, poked her hand into the socket of the phase inverter."
    me "You know what…"
    "I cranked amplifier's volume to the maximum."
    me "You'd better… Step away. From the speakers."
    show us normal sport with dspr
    us "Or what?"
    me "Nothing. It'll just be loud."
    us "It won't be that loud! Last disco I was directly near speakers, and nothing happened!"
    "How should I explain to her, that the only thing the bass guitar of some ensemble and the infrasound that I'm preparing to playback have in common… is…"
    "I don't know, that they're both related to music?"
    stop music fadeout 3
    "Well, yes, indeed, for a person who is not spoiled by foreign electronics…"
    "…brought up on vinyls…"
    play music "<to 27.83>" + music_7dl["polyhymnia"] fadein 3
    "…even the maximum volume of the sound will only cause slight displeasure."
    "But I have a very special surprise coming up!"
    show us dontlike sport with dspr
    us "Guhhhhh!"
    "She grimaced as if she had bitten off an unripe apple."
    us "Are you going to listen to classical music?"
    "She paused as she listened to the intro."
    show us laugh sport with dspr
    us "How low you've fallen."
    "Indeed, a violin part could be heard from the speakers, smoothly flowing into the male choir. Judging by the expression on Ulyanka's face, in her eyes I really fell below the bottom of the sea. However, this bothered me a little. What's more important is what will happen after the intro."
    me "Keep listening…"
    "I read a spinning «polyhymnia» label on the player's screen."
    "She'll never see this coming."
    us "I'm not going to listen to this crap…"
    "She had already turned to leave, and then the bass kicked in!"
    play music "<from 27.83 to 145>" + music_7dl["polyhymnia"]
    scene bg ext_stage_near_clear_7dl:
        linear 0.1 zoom 1.1 xalign 0.5 yalign 0.5
    show us surp2 sport with easeoutbottom
    with hpunch
    if (alt_day2_convoy == 'un'):
        show un surprise pioneer at fright with easeoutbottom
    elif (alt_day2_convoy == 'sl'):
        show sl surprise pioneer at fright with easeoutbottom
    elif (alt_day2_convoy == 'dv'):
        show dv surprise pioneer2 at fright with easeoutbottom
    "It wasn't Ulyanka who jumped - the whole world jumped!"
    "The sultry, red-hot air of the Soviet camp was stirred up by the viscous, thick basses of music that did not belong to this world."
    scene bg ext_stage_near_clear_7dl:
        linear 0.1 zoom 1.1 xalign 0.5 yalign 0.5
    show us surp2 sport with easeoutbottom
    with hpunch
    if (alt_day2_convoy == 'un'):
        show un surprise pioneer at fright with easeoutbottom
    elif (alt_day2_convoy == 'sl'):
        show sl surprise pioneer at fright with easeoutbottom
    elif (alt_day2_convoy == 'dv'):
        show dv surprise pioneer2 at fright with easeoutbottom
    "The kid bulged her eyes, and I understood her - after all, she jut got hit by a lively kilowatt of spectacular bass."
    "Three minutes of the most thorough combing of brains."
    "I closed my eyes and dreamed until the last chords of the track played."
    stop music fadeout 3
    play ambience ambience_camp_center_day fadein 3
    show us surp1 sport with dspr
    us "What the hell was that?"
    "She definitely was a little bit shaken up."
    me "It was my generation's longing for factory horns."
    us "Eh?!"
    if (alt_day2_convoy == 'un'):
        show un smile pioneer at fright with dspr
        "But Lena, it seems, managed to hear something, because interest was clearly shining in her eyes."
        un "Horrible music."
        "That was her only comment."
        un "Do you have any more?"
    elif (alt_day2_convoy == 'dv'):
        show dv smile pioneer2 at fright with dspr
        dv "Nice. Although too noisy for my taste."
        dv "You have anything with guitars?"
        "I thought for a bit."
        me "Yeah, I'll look."
    elif (alt_day2_convoy == 'sl'):
        show sl smile pioneer at fright with dspr
        sl "That was the strangest music I've ever heard."
        me "Where I come from, they dance to this kind of music."
        "I thought for a bit."
        me "Honestly, there are plenty of morons everywhere."
    elif (alt_day2_convoy not in ('dv', 'sl', 'un')) and ('music' in list_joined_clubs_7dl):
        $ lp_mi += 1
        show mi happy pioneer at fright with dspr
        mi "Whoa, that was great!"
        "Miku, who quietly crept up God knows when, yelled with delight from the bench."
        me "Miku? Where did you come from?"
        show mi laugh pioneer with dspr
        mi "The sensors detected seismic activity, so I went to check it out."
        me "Oh sorry, I didn't think…"
        mi "It's all right, Semyon, it's strange, but it's still music, I get it."
    "It was clear from Ulyana's face that nothing was clear to her."
    me "Music of the future."
    "I smirked."
    me "And get away from the speakers. There is an even more poignant thing coming up."
    us "Cool!"
    show us laugh2 sport with dspr
    "Enthusiastically said Ulyana."
    us "You have to let me listen to this cassette!"
    me "Cassette? What cassette?"
    us "The thing from which you were playing your noises right now? It's not a record, you don't have a record player here. I don't get it."
    me "Oh, this thing!"
    "I showed her my «walkman»."
    me "Four gigabytes of music for any situation."
    us "Gigabytes? How much is that in songs?"
    me "Around 1000 minutes with average quality."
    us "Gimme!"
    "She extended her hand."
    me "No." with vpunch
    "I slapped her hand."
    me "That's kind of my last memory of my homeland, and you want to take it away."
    us "Oh well."
    show us smile sport with dspr
    "She pouted and turned away."
    "Not for long. Evidently, although she may be naughty, but she's also very light and easy-going."
    us "Can you play your noises again?"
    me "What, you liked them?"
    us "Yeah!"
    "I played a few more electronic tracks - there were not very many of them, and all of them were time-tested. But, like any other owner of an audio device, I very soon realized that the mood for brain-blasting infrasound has gone somewhere. Then maybe…"
    play music "<from 17.7 to 56.77>" + music_7dl["splin"] fadein 1
    "The bass fell silent, they were replaced by a guitar pick, into which the voice of Sasha Vasilyev organically intertwined."
    if (alt_day2_convoy == 'sl'):
        "My attention was drawn to the movement on the benches, someone was sitting there. Unfortunately, once again I was against the sun, so I could not see who exactly."
        "But when «Splin» changed into «Scorpions», and those in turn changed into Manson, confirming the schizophrenia of my playlist, my viewer stood up and walked to the stage."
        show dv normal pioneer2 at cleft with dissolve
        show sl smile2 pioneer at fright with dspr
        sl "Well, this is… Pleasant."
        sl "Like a romance."
        "I smiled."
        me "To be honest it is one."
        dv "You do know that borrowing someone else's things is bad for your health?"
    elif (alt_day2_convoy == 'dv'):
        "A mask of contempt and skepticism dripped from Alisa's face like liquid wax."
        "It was easy to guess that she did not expect any good taste from me. And here came such a surprise."
        dv "Good music."
        "Alisa said in a neutral voice."
        me "Glad you liked it."
        dv "Are you done?"
        "She continued in the same neutral tone."
    elif (alt_day2_convoy == 'un'):
        "My attention was drawn to the movement on the benches, someone was sitting there. Unfortunately, once again I was against the sun, so I could not see who exactly. But when «Splin» changed into «Scorpions», and those in turn changed into Manson, confirming the schizophrenia of my playlist, my viewer stood up and walked to the stage."
        show dv normal pioneer2 at cleft with dissolve
        dv "Good music."
        "Alisa said in a neutral voice."
        me "Hello again."
        dv "Can you explain to me, who let you use my amplifier?"
        "She continued in the same neutral tone."
        me "Well, if it's YOUR amplifier… You probably know the answer."
        "I didn't miss my chances."
    elif ('music' in list_joined_clubs_7dl):
        "As it turned out, my music attracted more than one listener."
        "Alisa appeared from behind the stage."
        show dv normal pioneer2 at cleft
        show mi normal pioneer at fright
        with dissolve
        dv "You know that you shouldn't take other people's things?"
        if alt_day2_convoy not in ('dv_prep', 'dv_rej'):
            "Alisa asked."
            me "What, we don't have communal property here?"
            "I serenely smiled."
            mi "Alisa, please, just one more song! I know a lot about music, but all his songs are unfamiliar to me - and so strange!"
            dv "Only one more."
    else:
        "As it turned out, we had another listener."
        show dv normal pioneer2 at cleft behind us with dissolve
        dv "Touching someone else's things? Uh-huh."
    if alt_day2_convoy in ('dv_prep', 'dv_rej'):
        dv "I want you to turn it off. Now."
        show dv normal pioneer2 at left with moveoutleft
        "The girl said in an impossibly calm voice."
        "What's wrong?"
        me "Is something wrong?"
        dv "Do I need to remind you? About who and what he promised to do in the morning."
        "And then I realized!"
        "We were supposed to meet near the music club!"
        me "Sorry…"
        dv "I don't care. Turn the amp off."
        $ lp_dv -= 3
        stop music
        if ('music' in list_joined_clubs_7dl):
            show us sad sport
            show mi sad pioneer
            with dspr
        else:
            show us sad sport with dspr
        "I obediently flipped the switch."
        play sound sfx_7dl["eat_horn"] fadein 1
        "And then the horn rang…"
        if (alt_day2_convoy == 'dv_prep'):
            "Gotta treat my sclerosis."
        stop sound fadeout 3
        stop ambience
        return
    me "Yeah, I'm packing up already."
    "I was actually about to close up shop when Alisa, in a surprisingly low voice, asked:"
    dv "Wait. Let me listen to the end."
    "To say she surprised me would be a huge understatement! And she was not going to stop there, because at the end she added even quieter:"
    dv "Please…"
    me "Alright."
    stop music fadeout 3
    play sound sfx_7dl["eat_horn"] fadein 1
    "I started the music when the horn poured out signals for dinner."
    me "We should go."
    "I reached towards the switch."
    if (alt_day2_convoy not in ('dv', 'sl', 'un')) and ('music' in list_joined_clubs_7dl):
        show mi smile pioneer with dspr
        mi "Nuh-uh, we'll listen!"
        "Miku flared up."
        "And both redheads categorically agreed with her."
    elif alt_day2_convoy not in ('dv', 'sl', 'un'):
        "They both shook their heads."
        "Only now I noticed that Ulyanka fell into the same sacred trance as her older friend."
    else:
        "Heads shook unanimously."
        "It's amazing how they team up against me."
    th "Power of music?"
    if (alt_day2_convoy == 'un'):
        "I looked carefully at Lena and received an encouraging nod as an answer."
        "Oh well. Let's continue."
    elif (alt_day2_convoy == 'sl') and (counter_sl_cl == 1):
        show sl sad pioneer with dspr
        "Slavya looked annoyed and upset."
        me "What's wrong?"
        sl "Canteen duty. We ran all day, so I completely forgot about it."
        sl "Sorry, but I have to go."
        "I remembered the incident at the squad leader's house and suggested:"
        me "Maybe I should go with you? I'll help out however I can."
        sl "Nah, it's alright. See you."
        hide sl with dissolve
        "Waving to me, the girl left, leaving the prerogative of the host of request program empty."
        th "Hope she doesn't get yelled at by squad leader for being late."
    "The last chords sounded, and silence fell on the clearing."
    stop music fadeout 3
    me "We should go."
    "Finally said I."
    me "We'll be late for dinner."
    show us normal sport with dissolve
    us "Yes."
    "Ulyanka shrugged her shoulders, as if throwing off her stupor, and a few moments later she again turned into a meteor girl."
    show us smile sport with dissolve
    us "Disco-disco, Semyon made a disco!"
    me "That's tomorrow."
    us "Yeah, sure. Compare what's going to be there, to what happened just now."
    if alt_day2_convoy != 'dv':
        show dv smile pioneer2 at cleft with dspr
    me "C'mon, music isn't the main thing at the disco!"
    us "What is then?"
    dv "Making faces in the crowd!"
    "Alisa responded in my stead."
    if (alt_day2_convoy == 'sl') and alt_day1_us_shotted and ('medic' in list_voyage_7dl):
        "For a while, we just kept walking in silence, side by side."
        me "You're early today."
        dv "So are you."
        me "I didn't come here for that."
        show dv sad pioneer2 at cleft with dspr
        dv "Well, so did I?"
        me "How should I know."
        dv "What should you know here? Ulyana can't get off you now. And I don't really have any complaints about you… Let's just assume we've written off one of your screw-ups."
        "She smiled and, clapping Ulyana on the shoulder, rushed forward. And again, as then, there was neither impudence nor her inherent arrogance in her smile. Just an ordinary smile of an ordinary girl who for a few seconds forgot to wear a mask.."
        hide dv with dissolve
        us "Heeeeey, wait for me!"
        "I didn't chase them. No need to hurry, they won't eat my potatoes without me."
    stop sound fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_phone:
    scene bg ext_stage_normal_day
    play sound sfx_click_1
    "The switch on the microphone was in the same place - the usual slider with six palpable points."
    me "Ho!"
    "I yelled out without turning on the microphone, just to listen to the acoustics. It was amazing!"
    "It's been so long since I've performed in front of an audience. Other people's looks seem to entangle you and make you think about what you should never think about.!"
    "With what force must the calf muscle exert in order to take a step?"
    "How to keep your head straight so that it does not tremble?"
    "How often and how deep your breathing should be."
    th "What's the difference. You need to relax, the body knows everything much better than consciousness."
    "The only problem is that, in public, perverted mechanisms very often turn on in the body, giving the reins of control of the body to consciousness."
    play sound sfx_7dl["ghmm"]
    me "Ghmm…"
    "The microphone made a little noise, but my cough was reproduced clearly."
    th "Soviet technology and tube sound."
    "I chuckled and turned off the mic."
    "After walking around the stage for a bit, I stepped off and went to lunch."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_sl_hyst:
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_square_day
    with fade
    if ('sport_area' in list_voyage_7dl):
        show us normal sport with dspr
        us "Damn you're slow!"
        "Ulyana called us."
        us "Olga Dmitrievna already left!"
        us "Check her house!"
        "Thanking the girl with a nod, we headed to my house."
    else:
        "There was nothing to do on the square, and we were about to leave when we heard a voice."
        us "Hey, hey! Wait up!"
        play music music_list["i_want_to_play"] fadein 3
        show sl normal pioneer at cleft
        show us normal sport far at cright
        with dissolve
        us "Wa-it-for-me!"
        "We stopped and began to wait with interest for the approach of Ulyana."
        "Whatever was the reason for her hurrying - she looked extremely concerned."
        me "Waiting, waiting."
        me "What did you want?"
        show us laugh sport with dissolve
        us "I didn't want anything from you specifically! But Oldmitrievna is calling her!"
        "Ulyana wiped her forehead."
        us "Well? You got that?"
        me "Kind of."
        show us calml sport with dspr
        sl "Yes."
        us "So why are you still here? Allons-y!"
        hide us with easeoutbottom
        "She stamped her feet on us and took off in an unknown direction."
        me "Let's go see what she wants from us?"
        "Slavya nodded, although for some reason she clenched her fingers nervously."
        "I also had a few ideas what could happen, but…"
        "First things first!"
    stop music fadeout 3
    scene bg ext_house_of_mt_day with dissolve
    play sound sfx_knock_door7_polite
    "Slavya cautiously knocked on the door."
    mt "Come in!"
    play sound sfx_open_door_1
    pause(1)
    play music music_list["she_is_kind"] fadein 3
    play ambience ambience_int_cabin_day fadein 2
    scene bg int_house_of_mt_day
    show mt normal pioneer at cleft
    with dissolve
    mt "Oh, how nice that both of you are here!"
    mt "Slavya, I need the two of you to go down before lunch and check the lights at the cybernetics."
    sl "Olga Dmitrievna, there's a small problem…"
    mt "Everything is fine, Boris Alexandrovich will go to the city after dinner, he will return just in time for tomorrow's dances, he'll just buy whatever we need."
    $ meet('ba','Sanich')
    mt "Considering last disco a few light bulbs did not burn - it was a mess, they have to be replaced!"
    mt "Can you do it, okay? {w}I don't really have the time right now, gotta go!"
    show sl serious pioneer at right with dissolve
    sl "Olga Dmitrievna, you see…"
    show mt laugh pioneer with dspr
    mt "Don't even ask, I won't give you more people - the two of you will be enough."
    sl "Olga Dmitrievna, I don't have the keys!"
    "Finally, Slavya decided to come out clean."
    "She pulled her head into her shoulders, fearing the oncoming judgement."
    play music music_7dl["areyouabully"] fadein 3
    show mt angry pioneer with dspr
    mt "What did you just utter, girl?"
    "The leader began, quietly getting mad."
    show sl sad pioneer at fright with move
    sl "I don't have the keys. Lost them."
    mt "Semyon, get out, because the spectacle now will not be for the faint of heart."
    menu:
        "I have the keys!":
            "I shouted."
            "I just couldn't bear to keep silence."
            "I guess I really am a retrograde - I don’t know how to look at how a person is being drowned alive for no reason."
            "Even if this is a person like Slavya, who is constantly cuddling, and that's extremely suspicious!"
            "But suspecting someone is far from a reason to throw him to be eaten by a rabid squad leader."
            "So I, perhaps, will portray a hero - what if they kick me out of the camp and return home at public expense?"
            $ alt_day1_sl_keys_took = 0
            $ alt_day3_duty = True
            $ counter_sl_cl = 1
            $ karma += 20
            show mt shocked pioneer
            show sl surprise pioneer
            with dissolve
            "They simultaneously started to say something to me, then hurried, interrupting one another…"
            "Hell."
            "At least they could decide on the order."
            "Who's going to start beating me first?"
            "I went to the bedside table and, taking out a bundle, put it on the table."
            menu:
                "She dropped them yesterday during a fight with Alisa":
                    "Slavya looked at me with a look expressing anything but gratitude."
                    "Nothing. If I shit on a little on the red bitch, it will only make me happy."
                    mt "So, almost got into a fight with Dvachevskaya?"
                    "Olga wrote something down in her diary."
                    mt "Damn good helper she is, huh."
                    "Slavya's gaze became completely helpless, and I hurried to continue my performance:"
                    $ lp_dv -= 2
                "She probably dropped them yesterday":
                    th "More precisely, we both know when and during what."
                    "But something didn’t work out of me as a snitch - despite the fact that Slavya did not shy away from such methods of influence."
                    th "But I have a completely different morality - incomparable to yours."
                    $ lp_sl += 1
            me "I found them and then forgot to say anything about it."
            show mt angry pioneer with dspr
            mt "Oh, you forgot."
            "Putting her hands on her hips, she began."
            mt "Then I know a surefire way to help you with your sclerosis!"
            show sl serious pioneer with dspr
            sl "Olga Dmitrievna, I don't think…"
            mt "And sometimes you should, maybe you'll get a few more braincells that way!"
            sl "Apologies…"
            mt "If you're not responsible enough to hold the keys to everything in the camp, you should tell me and I'll find someone responsible enough!"
            show mt sad pioneer with dspr
            sl "Apologies…"
            "Olga noisily drawn out and drew air through her teeth.."
            mt "Semyon, you also know what you did and how it's called."
            "I nodded."
            mt "Alright, Feoktistova - starting from lunch and until the end of day - you."
            mt "Persunov - the entire day tomorrow."
            me "The entire day… what?"
            mt "Canteen duty. {w}And now get out of my sight, if I recall correctly you had to fill out something, ready to present?!"
            stop music fadeout 3
            play sound sfx_close_door_campus_1
            pause(1)
            scene bg ext_house_of_mt_day with dissolve
            play ambience ambience_camp_center_day
            "She kept screaming something else, but I could no longer hear it."
            "Slavyana pulled me by the hand into the street and led me along."
            show sl shy pioneer with dspr
            sl "Thank you for…"
            me "Don't flatter yourself. I didn't do it for you."
            show sl surprise pioneer with dspr
            sl "What?"
            me "I said everything. I do not want to set anyone up or allow anyone to be harmed by my action or inaction."
            me "Have you read Asimov? Laws of Robotics."
            "Slavya smiled."
            show sl tender pioneer with dspr
            sl "Either way - thanks. {w}Even if it doesn't mean anything to you."
            "I brushed it off:"
            me "I'm not interested in epic speeches - we still need to go around the camp, remember?"
            show sl smile pioneer with dspr
            sl "Yeah, I remember."
            me "So, if you really want to repay my kindness - you could keep me company."
            me "No, I'm not insisting."
            "Slavya smiled and took the sheet from me."
            if not ('music_club' in list_voyage_7dl):
                sl "Let's go to Miku first? It's the closest place to here."
            else:
                sl "We already visited Miku, and the closest places are the library and the infirmary."
                sl "We could go there, if you want."
        "Don't say anything and obediently leave":
            $ alt_day1_sl_keys_took = 3
            stop music fadeout 3
            scene bg ext_house_of_mt_day with dissolve
            "Those uninvolved probably shouldn't interfere with things like that."
            play sound sfx_open_door_2
            show sl sad pioneer with dissolve
            "Slavya came out ten minutes later, upset - but with a new key bundle."
            sl "Let's go?"
            "She called me."
            "I nodded."
            $ lp_sl -= 1
    stop music fadeout 4
    stop ambience fadeout 5
    scene black with fade
    return

label alt_day2_event_square_dunno:
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_square_day
    with fade
    me "Remind me, why are we back here?"
    show sl smile pioneer with dissolve
    sl "I don't know. I thought you knew."
    "I see."
    "We will be treating sclerosis. Definitely."
    "I pulled up the map."
    return

label alt_day2_event_square_1:
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_square_day
    with fade
    "Yesterday was a hectic day, I watched the girls exercising, and on the lineup I had a complete mental collapse due to my public performance. So Genda, despite the fact that he was the central figure of the camp, haven't had the chance to appear in my sights."
    "Time to make up for it."
    "I went up to the pedestal itself and stared thoughtfully at the bronze figure from the bottom."
    th "What kind of bird are you, Genda? Who were you displacing, defeating, defending?"
    "With such foppish glasses, you look like an intellectual and an intelligent. Imagining you in a dirty vest and peakless cap, with a rifle in your hands, honestly, does not work. Not your type."
    "So, some kind of inspirer? Another talker on an armored car? Practice shows that it is to such talkers monuments are usually erected."
    th "No, seriously, who the hell is this guy? I definitely don't remember anyone with that surname in any period our country's history."
    th "Did I actually end up in a parallel universe?"
    if len(list_voyage_7dl) > 1:
        "Nobody was here."
        if (alt_day2_convoy == 'sl_prep'):
            "Looks like Slavya finished cleaning and left."
            $ alt_day2_convoy = 'me'
        else:
            "I shrugged and unfolded the map."
    elif (alt_day2_convoy == 'sl_prep'):
        sl "Have you decided to help me?"
        show sl smile pioneer with dspr
        "Slavya came up to me, flashing a white-toothed smile."
        me "Something like that. Show me where to go, what to do, et cetera."
        show sl smile pioneer
        sl "Right!"
        "She went to the bench, where several whisks and a rake were already placed."
        sl "Alright, you start cleaning the left side and I'll clean the right side of the monument, then we'll meet on the other side!"
        me "Okay!"
        with fade2
        "Slavya didn't lie."
        "We actually did it quickly: in less than half an hour, we unloaded the last bag of garbage into a cart and looked around the battlefield."
        sl "And that's all. Thank you very much."
        sl "I'll try my best to do something for you too!"
        me "What?"
        show sl shy pioneer with dspr
        sl "I just want to repay your kindness."
        me "No thanks, I don't need such monetary relationships."
        me "If you want to do something…"
        "I thought for a bit."
        me "You can accompany me around the camp."
        me "It would be extremely useful to have someone I know with me, especially if that someone already knows everything here."
        show sl happy pioneer with dspr
        sl "My pleasure! {w}And let me add in one signature for you, so that your time wouldn't be wasted."
        "She took my checklist and signed in a free space."
        "I smiled and figured out where to go next…"
        $ alt_day2_convoy = 'sl'
        $ list_voyage_7dl.append('cleaning_sl')
    else:
        sl "Hey!"
        show sl smile pioneer at center
        "Slavya walked around and stood next to me."
        if (alt_day2_convoy not in ('dv', 'un')):
            sl "How's it going? Managed to do a lot of things?"
            me "Well, progress is definitely there…"
            "I answered evasively."
            sl "Can you help me clean up? There's not much here, together we'll get through it quickly."
        else:
            sl "How's it going? Visited a lot of places?"
            me "Well, progress is definitely there…"
            "I answered evasively."
            sl "Can you help me clean up? There's not much here, the three of us will get through it quickly."
            "She waved her hand in the direction of the formation site. After several dozen pioneers stood there, papers, candy wrappers and some other incomprehensible garbage suddenly appeared from somewhere."
        if loki and not (alt_day2_convoy == 'sl_prep'):
            me "Uh-huh."
            "I muttered."
            if (alt_day2_convoy == 'dv'):
                me "Why don't I spit a chewed carrot in your mouth?"
                show sl surprise pioneer with dspr
                sl "Huh?!"
                me "So you would smell like soap."
                "I continued in the same undertone."
                sl "Semyon, I don't know what I've done to you, but…"
                me "Slavya, I'll tell you once so I don't have to repeat myself later: waving a broom isn't my business."
                me "So — auf wiedersehen."
                $ karma -= 10
                $ lp_sl -= 1
                $ lp_dv += 1
            else:
                me "Sorry. Can't help you right now. Maybe after dinner?"
                show sl sad pioneer with dspr
                sl "I'll be busy after dinner."
                me "See ya then!"
            stop music fadeout 4
            stop ambience fadeout 5
            with fade
            return
        elif (alt_day2_convoy == 'un'):
            show un normal pioneer at left with dissolve
            me "Should we help Slavya?"
            "I asked the silently approaching Lena."
            un "There's still time…"
            "She said completely indifferently."
            un "I hope they don't make us raise the flag tomorrow."
            $ list_voyage_7dl.append('cleaning_un')
        elif (alt_day2_convoy == 'dv'):
            show dv angry pioneer2 at left with dissolve
            dv "What? Cleaning up?! Hell no."
            "She snorted and turned away."
            me "It's kind of wrong to force Slavya to work alone."
            dv "Oh, but she enjoys it."
            dv "If you want to clean - go ahead. Don't bring me into this."
            dv "Personally, {b}I{/b} don't want to raise the flag."
            "I looked at Alisa."
            "Thought for a bit."
            "Looked at Alisa again."
            "Sighed and grabbed the broom."
            $ list_voyage_7dl.append('cleaning_dv')
        else:
            $ list_voyage_7dl.append('cleaning_sl')
        "Slavya didn't lie, we actually got over it quickly, not even half an hour passed before we unloaded the last garbage bag onto a cart and examined the battlefield."
        show sl smile2 pioneer with dspr
        sl "That seems to be everything. Thank you very much."
        if not herc:
            th "Alright, exploiter."
        else:
            me "My pleasure."
        sl "I'll try my best to do something good for you too!"
        me "What?"
        show sl shy pioneer with dspr
        sl "I just want to repay your kindness."
        "I thought for a bit."
        me "Can you help me with this?"
        "I took the checklist out of my pocket and handed it to Slavya."
        show sl smile pioneer with dspr
        sl "Of course. I can sign here myself."
        "She took it and signed in a free space."
        sl "Here."
        me "Thanks!"
        "I put it in my pocket and planned my next move…"
    stop music fadeout 4
    stop ambience fadeout 5
    with fade
    return

label alt_day2_event_boat_station1:
    play ambience ambience_boat_station_day fadein 2
    scene bg ext_boathouse_day with fade
    if not alt_replay_on:
        if been_there_alt1() > 1:
            th "I didn't see the point in revisiting the boat station. I don't need any signatures from here, and time is running out."
            "However, I couldn't help but admit - the view from here is amazing."
            stop ambience fadeout 1
            play ambience ambience_camp_center_day fadein 1
            return
    "The pier is perhaps one of the quietest and most beautiful places in the camp."
    "I won’t be surprised if I find out that somewhere here there is some kind of Tree of Lovers or Swallow Rock - for meetings of various couples."
    "The place involuntarily sets in a romantic mood. Silence, the splash of water and the reflections of the sun, a hundred sunbeams jumping along the forest."
    "The pontoon part swayed lazily next to the concrete pier. {w}If you wanted, you probably could untie the pier and turn it into a floating headquarters!"
    "I sat down on the edge of the pontoon and thoughtfully looked at the surface of the water - somewhere fifty meters away a buoy curtain was hung so that the pioneers would not swim far."
    "And then - behind a whimsical bend that gives out a river in our reservoir, just a wide one, a floodplain containing two islands was visible."
    "In the narrow part, the floodplain was pulled together by a steel line of the railway, barely visible from here."
    "Now, by the way, a diesel locomotive was already hurrying somewhere along it, dragging a row of freight cars behind it, and the lulling syncopations of the clatter of wheels carried far across the calm water."
    "If you think about it… If you swim for a long, long time, further beyond the buoys, then perhaps there will be a way to jump into the freight train. Fortunately, they always slow down in the swampy areas…"
    "And then you get to leave by train to the closest city."
    "But that's only if I ever really need to escape from here."
    "Seagulls were lazily calling to each other, and the water was impossibly cold, clean and transparent."
    "By noon, it will, of course, warm up. The camp was specially made in the backwater so that the kids could bathe."
    "But I wouldn't go in right now."
    th "Maybe on a boat."
    if (alt_day2_convoy not in ('dv', 'sl', 'un')) and ('music' in list_joined_clubs_7dl):
        "Squinting from the bright sun, I noticed a strange glow on the far edge of the pontoons - where the boats were tied."
        show dn normal pioneer with easeinleft
        "At this time, some shaggy pioneer, about the same age as Ulyana, ran past me somewhere."
        hide dn with easeoutright
        $ reset_chibi_alt1('boat_station_alt1')
        menu:
            "Follow the pioneer":
                "If I understood correctly, the pioneer ran away somewhere to the square."
                "I'll go check it out."
            "Check the pontoons":
                scene
                $ renpy.show("bg ext_boathouse_day", at_list = [sdl_transform2], what = Noon("bg ext_boathouse_day"))
                "I took a walk to where the bridges broke right into the water - next to it, boats without oarlocks and oars were tied on iron chains."
                "My attention was drawn to one object that didn't belong here."
                with fade
                "Braided bracelet."
                "Beautiful. Exotic weaving, definitely not our orthodox macrame."
                "Here weaving is more likely to be done by hand, from beautiful narrow ribbons - probably even silky ones."
                "I grabbed the bracelet and put it in my pocket."
                $ alt_day2_mi_kumuhimo = 1
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_dinner:
    scene
    $ renpy.show("bg ext_square_day", what = Noon("bg ext_square_day"))
    with joff_r
    th "Hoooh. In this camp time passes either in years, or in seconds."
    th "Now, while I was busy, I didn't notice how the time had passed since breakfast."
    th "And I wasn't even involved in public matters!"
    "I wondered with horror what full-fledged acceptance into the ranks of the squad would result in. {w}But I really didn’t want to think about such matters on an empty stomach."
    th "Managed to get here in time!"
    if alt_day2_minijack and (alt_day2_convoy not in ('dv_prep', 'dv_rej')):
        me "Did we shut down power?"
        "I started worrying."
        show dv normal pioneer2 with dspr
        dv "Relax, four-eyed will turn off everything."
        me "Four-eyed?"
        show us smile sport at right with dissolve
        us "Shurik!"
        "Ulyana proclamed."
        us "You still haven't met him?"
        if not alt_day2_sh_met:
            me "Don't think so."
            us "Well, you won't ever confuse him with anyone!"
            $ meet('sh','Shurik')
            $ alt_day2_sh_met = True
        else:
            me "I did…"
        dv "Stop crying then and let's go eat."
    scene bg ext_dining_hall_near_day with fade
    stop music fadeout 3
    show mt smile  pioneer far with dissolve
    play music music_list["get_to_know_me_better"] fadein 1
    "Olga Dmitrievna, as befits the squad leader, was already guarding at the entrance, while looking suspiciously blooming and rested."
    "Yeah, we know their… Work."
    "Judging by the contented expression on her face, our Olechka plows without rest either on the beach or on the pier."
    "And all without a break. Piss easy job, huh?"
    mt "Well, Semyon, did you already meet everyone in the camp?"
    "She kindly smiled."
    "I went over every character I met today."
    me "Yeah, I met them. I met them alright!"
    "The checklist resembled an already incomprehensible brown something, however, the signatures on it differed quite clearly."
    "I proudly presented it to the squad leader, and she…{w=.3} just put it in her pocket!"
    th "Huh!? You mean I could just scribble some illegible garbage myself and that would work?!"
    "Oh, Olga Dmitrievna!"
    show mt laugh pioneer with dspr
    mt "What, did you actually believe me? {w}You should've seen your face!"
    "Laughing, she unfolded the paper and skimmed through the signatures."
    show mt normal pioneer with dspr
    if len(list_joined_clubs_7dl) > 1:
        mt "Oh, that's a pretty good run you did.{w} But are you sure you can visit all places where you signed up?"
        me "Anything wrong with that?"
        mt "Yeah, you won't have enough time for everything, so don't be greedy, choose one!"
        menu:
            "I'll have time for music and newspaper!" if (alt_day2_convoy == 'un') and ('music' in list_joined_clubs_7dl) and ('nwsppr' in list_joined_clubs_7dl):
                mt "Are you sure?"
                show un normal pioneer at left with dissolve
                "Lena, who stood next to me, nodded."
                un "He should manage."
                mt "In that case I'm leaving music and newspaper."
                $ list_clubs_7dl = ['music','nwsppr']
            "Newspaper" if 'nwsppr' in list_joined_clubs_7dl:
                me "I'll be writing then."
                "Olga nodded, marking the signature from the library."
                $ list_clubs_7dl = ['nwsppr']
            "Football, I guess" if 'soccer' in list_joined_clubs_7dl:
                me "As if there's anything better to do."
                mt "Okay then."
                "Olga nodded, marking Sanich's signature."
                $ list_clubs_7dl = ['soccer']
            "Volleyball?" if 'volley' in list_joined_clubs_7dl:
                me "I think I'll stay in volleyball club."
                mt "Closer to Slavya? {w}What a nice guy."
                "Olga nodded, marking Sanich's signature."
                $ list_clubs_7dl = ['volley']
            "Maybe badminton?" if 'badmin' in list_joined_clubs_7dl:
                me "Badminton. Gonna toss shuttlecocks."
                mt "Not a guy's sport, don't you think?"
                "I shrugged."
                me "I like it."
                mt "Whatever you say."
                "Olga nodded, marking Sanich's signature."
                $ list_clubs_7dl = ['badmin']
            "I'll stay in the music club!" if 'music' in list_joined_clubs_7dl:
                me "I like it best there."
                mt "Or you just like Miku?.. Alright, alright, shutting up."
                "Olga marked Miku's signature."
                $ list_clubs_7dl = ['music']
            "I'm all for cybernetics!" if 'cyber' in list_joined_clubs_7dl:
                mt "You sure?"
                me "Yeah."
                mt "Alright, then we're leaving cybernetics club."
                $ list_clubs_7dl = ['cyber']
        if (alt_day2_convoy == 'un') and ('music' in list_clubs_7dl) and ('nwsppr' in list_clubs_7dl):
            mt "That's how it is."
        else:
            mt "Everything else I'm crossing out!"
        "Olga sweepingly crossed out something on a piece of paper and hid it in her pocket."
        "For real this time."
        show mt smile pioneer with dspr
        mt "Alright! {w}Since you're done - it's time for dinner!"
        "She made room to let me into the canteen."
        hide mt with easeoutleft
        "I rushed in, completely missing her remark at my back."
        "Something about apologies?"
        "No idea what that was."
    elif len(list_joined_clubs_7dl) < 1:
        mt "Eh, falcon, why didn't you sign up anywhere?"
        me "And did you send me to meet the camp, or to sign up?"
        show mt laugh pioneer with dspr
        mt "You're pretty good! {w}Honestly I was just hoping that you'd find something to your liking."
        mt "But since you didn't want to sign up anywhere, you will have to spend your free time on social activities. Are you glad?"
        me "Very."
        "I muttered."
        "Unfortunately, Olga Dmitrievna had complete immunity to sarcasm, so she didn't even care."
        "She moved aside, letting me into the canteen."
        hide mt with easeoutright
        mt "I've got big plans for you!"
        "She yelled behind me."
        th "God, please no!"
    else:
        $ list_clubs_7dl = list_joined_clubs_7dl
        mt "I see you've decided to do something?"
        me "Eh, what something…"
        show mt laugh pioneer with dspr
        mt "Anything! To the canteen quickly - march!"
    play sound sfx_open_door_1
    pause(1)
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 3
    "It seems the pioneers were hungrier than usual today. In any case, there were less empty seats than at breakfast or even yesterday's supper…"
    if (alt_day_binder != 1):
        extend " That same one, with Malaysian cuisine."
    "There were a couple of empty seats next to the redheads."
    if (alt_day2_convoy == 'dv'):
        "At least after today's events they didn't seem all that bad to me. I probably could sit there."
    else:
        "But it's better to starve for a week than to risk sitting next to them."
    if (alt_day_binder == 1) and not 'music_club' in list_voyage_7dl:
        "And one more place was next to the girl which I promise myself to meet for the second day."
        "We keep having those strange encounters."
    elif 'music_club' in list_voyage_7dl:
        "There was also an empty seat next to Miku - it seems that the girl had a certain reputation in narrow circles."
        "She looked up at me and opened her eyes with interest - immediately becoming like the heroine of the anime so popular in her homeland."
        th "Spitting image of an anime girl!"
    else:
        "The last free seat was next to that very unknown girl who looked like an anime character - huge eyes, narrow chin, small mouth."
        "Considering that we had not met in two days, I was almost seriously ready to consider her a ghost in the uniform."
    "The only question is where do I sit to minimize the damage…"
    $ miku_menu = "With the anime girl"
    if 'music_club' in list_voyage_7dl:
        $ miku_menu = "With Miku"
    menu:
        "[miku_menu]":
            $ alt_day2_mi_dinner = 1
            me "Do you mind if I sit here?"
            show mi normal pioneer at center with dissolve
            play music music_7dl["what_am_i_doing_here"] fadein 5
            mi "Few people want to sit with me, it's so strange. But sit down, of course. Enjoy your meal!"
            me "Thanks. You too."
            if 'music_club' in list_voyage_7dl:
                "However I was already a bit late. Miku somehow managed to rival Ulyana in terms of food destruction speed."
                menu:
                    "Smile":
                        "I sat down and smiled at her."
                        $ karma += 10
                        $ lp_mi += 1
                        me "Bon appetit!"
                        mi "Thank you! I'm already finishing, sorry, we won't sit long."
                        "Indeed, I could already see the bottom of her plate."
                    "Shut up and sit":
                        "Gracefully giving her a look, I silently sat opposite of her."
                        "Long sessions of auto-training bore fruit, and I managed to level the sound of her voice to the background level."
                        "It's just some white noise. Just white noise."
                        "I'm on the seashore, it smells like fish and iodine."
                    "Sigh":
                        "I hope she won't ramble at least here?"
                        "After all, she must have some limit on her talkativeness!"
                        me "Miku."
                        mi "Yes, Semochka, you wanted something?"
                        me "Don't call me Semochka."
                        mi "But I'm just trying to be friendly!"
                        "She started flapping her eyes."
                        me "Have you ever heard this proverb: «When I'm eating, I'm mute and deaf»?"
                        dreamgirl "…cunning, fast, and devilishly sly."
                        mi "But that's boooooring!"
                        "I only rolled up my eyes."
                        $ lp_mi -= 1
                        $ karma -= 10
                        "Looks like she isn't even planning on shutting up!"
                        "I took out my earplugs and cranked the volume to the max."
                        th "What's on the menu today?"
                        th "Aha, monsieur Durst is offering to «break your fucking face tonight»."
                        "A very enticing proposal indeed."
                        "I laughed a little more, watching her silently move her lips - she really looked like a fish!"
                        "After that, it seems to have dawned on her that I simply am not listening to her."
                        show mi upset pioneer with dspr
                        "She immediately pursed her lower lip in an offended manner and, having collected the cutlery from the table, got up and left."
                        stop ambience fadeout 2
                        return
            else:
                if alt_day_binder == 1:
                    mi "And here we meet again, see!"
                    "She smiled."
                    mi "And before you run off again, my name is Miku, nice to meet you!"
                else:
                    mi "I saw you yesterday. You're new here, right?"
                    me "Yes… I was going around with the checklist, collecting signatures…"
                    mi "Seems like you didn't visit me. I'm Miku."
                $ meet('mi','Miku')
                $ alt_day2_mi_met = True
                "She extended her hand over the table, and I hurried to grab it."
                menu:
                    "Get to know each other better":
                        $ lp_mi += 1
                        $ karma += 10
                        me "Nice to meet you. And I'm Semyon."
                        me "You have really beautiful name."
                        me "Which one is it? Korea? Japan?"
                        show mi smile pioneer with dissolve
                        mi "Oh, you're the first one to guess! Everyone else just doesn't believe me."
                        me "I have always been attracted to the East. And Japanese girls are the most beautiful."
                        show mi shy pioneer with dspr
                        mi "Flatterer!"
                        "I laughed."
                        me "I'm not flattering, that's an objective fact."
                        me "Aaah…"
                        "I pretended to just realize it."
                        me "So it's a japanese name?"
                        me "Glad to meet you."
                        mi "You may be glad, but you still didn't visit me."
                    "Introduce yourself":
                        me "Semyon."
                        "I briefly responded. The last thing I need is this Asian woman sitting on my neck."
                        mi "I know that."
                        show mi laugh pioneer with dspr
                        "She laughed."
                        mi "I was waiting for you."
                "She seemed to freeze for half a second - I myself sometimes do this if I need to urgently «get off» from the current topic."
                "And shaking her head - I stared at the play of light in my hair - she suddenly said:"
            show mi smile pioneer with dspr
            mi "Potatoes are good. I like putting a cutlet in there, or something like that. Stir it, salt it up — mmmmm… Tasty! But fish — no! Don't like it. Although they say its rich in phosphorous. Like, you'll glow in the dark. Or is that good for your brain? I don't remember!"
            mi "I mean, I like it, but not like that! Well, that is, I probably like this one too. But they somehow came up with the most tasteless recipe! Boiling it! With eggs! Onions! And God knows what else. Is that even food?"
            me "I agree. Anyone who spoils food like this should be locked up in the house and fed with that fish for an entire year."
            "Turns out the machinegun girl can also say reasonable things. You just need to filter out the rest of her verbal noise."
            if alt_day2_mi_kumuhimo == 1:
                $ lp_mi += 1
                $ alt_day2_mi_kumuhimo = 2
                "Taking advantage of the hitch before the next burst, I took out a bracelet from my pocket and showed it to her."
                me "Yours?"
                show mi happy pioneer with dspr
                mi "Oh, Senechka, where did you find it, and I already thought that I had lost it completely, I was so upset!"
                me "Don't lose it."
                mi "I won't."
                "She clutched it so hard her fingers turned white, and then amazed me:"
                mi "Many thanks, Semyon."
                "She got up from the table and even tried to bow before I realized."
                me "Sit back!"
                "I started hissing."
                me "That's not how we do things here, you know that?!"
                mi "But…"
                me "You wouldn't want to embarass me by expressing your gratitude?"
                show mi upset pioneer with dspr
                mi "What? Of course not!"
                me "Then sit back down and eat!"
                "I cut her off."
                show mi smile pioneer with dspr
                "She giggled and returned to her place."
            mi "You are so evil! Or rather, not evil, but angry. It's probably from hunger. I'll make do with just soup, but you need more, of course."
            mi "You are so big. Do you want me to bring you more mashed potatoes? Or you'll probably be singing with your stomach. And then they will send you to the infirmary…"
            "Machine gun girl did what caused me to choke, — she got silent."
            "I lifted my shocked gaze from the plate to her."
            show mi surprise pioneer at center with dspr
            if alt_day1_un != 0:
                "Somehow she reminded me of Lena during my past attempts to get to know her."
            show mi shy pioneer at center with dspr
            $renpy.notify('«with little blood» - idiom, means «without making certain sacrifices».')
            mi "Not a single young man has managed to escape Violetta with little blood."
            if ('medic' in list_voyage_7dl):
                "I was forced to agree with her: I felt like I was raped after leaving the infirmary."
            if ('music_club' in list_voyage_7dl):
                th "For a lonely girl who constantly sits under the piano, she is suspiciously well-informed."
            else:
                "How does a girl practically living in music club know so much?"
            show mi upset pioneer at center with dspr
            mi "No, in no way am I accusing our doctor of anything, but her way of presenting her thoughts with ambiguities keeps even sick young men at a distance."
            mi "She once asked me to lend her a tape recorder for something. Do you know how?"
            show mi laugh pioneer at center with dspr
            mi "She asked me to give her my little thing, where all sorts of round things are inserted, can you imagine?"
            me "Oh, that's nothing."
            if ('medic' in list_voyage_7dl):
                me "Today, she wanted to hold a rubdown session looking at me like it was something obscene."
            else:
                me "Yesterday my head was spinning - so she arranged such a medical examination that I instantly forgot about all the headaches."
            "Miku had one remarkable ability - from the first seconds, it was as if I had known her all my life."
            "There was no longer any embarrassment or forbidden topics for us. I just relaxed and enjoyed the conversation."
            menu:
                "Can you tell me anything about Lena?":
                    $ lp_un += 1
                    show mi smile pioneer with dspr
                    mi "Lena?"
                    "Miku smiled, with undisguised sympathy, glancing towards the modest girl - she was surrounded by redheads on both sides."
                    mi "Yeah, we're roommates."
                    if (alt_day2_convoy == 'un'):
                        me "Yeah, I know."
                    else:
                        me "Oh?"
                        th "How do they even get along?"
                        mi "The squad leader said that we are creative people and should communicate closely, so we will get along."
                        "She answered my unspoken question."
                    show mi upset pioneer with dspr
                    mi "Why are you interested - you do like her, yes?"
                    menu:
                        "It's personal":
                            $ karma += 10
                            "I firmly said."
                            show mi laugh pioneer with dspr
                            mi "I understand. I won't insist."
                            mi "But I'll tell her that you were interested."
                            "I just groaned muffledly, already twice cursing myself for intemperance."
                        "Hard to say…":
                            me "I just met her yesterday, how should I know whether I like her or not?!"
                            me "I need time for that."
                            show mi smile pioneer with dspr
                            mi "And I only need one look. For example, on you."
                            me "And?"
                            mi "You're cute."
                            show mi laugh pioneer with dspr
                            "She laughed as she looked at my bewildered face."
                "Do you spend all your time in the club?" if 'music_club' in list_voyage_7dl:
                    $ alt_day2_mi_dinner = 2
                    $ lp_mi += 1
                    show mi sad pioneer with dspr
                    mi "For the most part, yeah."
                    "Miku felt a little sad, but after a few seconds she smiled again - apparently, her character was that light and easygoing."
                    show mi normal pioneer with dspr
                    mi "But I always have instruments at my side! I'm like your Rimsky-Korsakov, if by the night I suddenly see a melody, I can quickly go and play it."
                    me "You mean, by ear?"
                    th "Actually, that's how Pushkin wrote poetry…"
                    mi "Yes! I have a good ear, so I hum a melody and pick it up on the guitar at the same time! Or the piano, or some other instrument! I can do everything. I can teach you, if you want?"
                    "Apparently, such a base thing as writing said melody down, was despised by Miku."
                    show mi upset pioneer with dspr
                    if 'music' in list_joined_clubs_7dl:
                        mi "Oh sorry, you already signed up."
                        mi "What did you say you will play?"
                        if not ('music' in list_clubs_7dl):
                            me "Nothing, as it turns out."
                            show mi sad pioneer with dspr
                            mi "What? Why?"
                            me "Sorry Miku, but it turns out it was not meant to be."
                            "I briefly recounted to her the conversation with the squad leader at the canteen."
                            show mi cry_smile pioneer with dspr
                            mi "Well, nothing you can do."
                            "Even a fool could understand Miku was offended at the choice not being in her favor."
                            th "Gulped it down. Coped."
                            dreamgirl "Treated you with understanding. Don't mix those up."
                            "The inner voice corrected me."
                            show mi normal pioneer with dspr
                        else:
                            if herc:
                                mi "Guitar?"
                            else:
                                me "Someone promised me a mouthpiece, and then…"
                            me "We'll see how it goes."
                            "I evaded the answer."
                    else:
                        mi "Oh, I'm sorry, I must look intrusive."
                        me "No, it's okay, it's okay."
                        "I definitely didn't mind such intrusiveness."
                "Say goodbyes":
                    me "It was nice talking to you, Miku."
            me "I should go. Ran around the entire day, so I want to take a nap."
            mi "See you soon!"
            stop sound
            stop sound_loop
            stop ambience
            if ('music' in list_clubs_7dl):
                mi "Don't forget about the club!"
                mi "We'll start rehearsing as soon as you arrive."
            elif ('music' in list_joined_clubs_7dl) and not ('music' in list_clubs_7dl):
                show mi smile pioneer with dspr
                mi "If you change your mind or nothing works out with another club, come in anytime! I will always be glad to see you!"
                "I nodded briefly and left."
            else:
                mi "If anything, I'm always here, you're welcome to visit!"
                th "So obsessive…"
            hide mi with dissolve
            stop music fadeout 3
            stop ambience fadeout 2
            return
        "With Alisa" if (alt_day2_convoy == 'dv'):
            if alt_day2_us_dubstep:
                $ lp_dv += 1
                $ alt_day2_dv_dinner = True
                show dv normal pioneer2 at center with dissolve
                if herc:
                    me "Hello again. May I sit down?"
                elif loki:
                    me "Bon appetit, beauty. Free here, may I sit?"
                else:
                    me "C-can I?"
                "She looked at me."
                dv "Well, if you aren't bored of me…"
            else:
                "After some thought, I decided not to risk it."
                if alt_day1_us_shotted:
                    "Moreover, Ulyanka was looking at me so meaningfully…"
                    "I sat alone!"
                    with dissolve
                stop music fadeout 3
                stop ambience fadeout 2
                return
        "With Ulyana" if (not alt_day1_us_shotted) and (alt_day2_convoy not in ('dv_prep', 'dv_rej')):
            $ lp_us += 1
            show us smile pioneer with dissolve
            us "Bonappeetiitteee!"
            "Ulyana rattled, and I suspiciously looked into the plate."
            "Nope, no new life has been spotted."
            me "Thanks. You too."
            "Alisa snorted and turned away, pretending not to notice me."
    "Although from moving around the camp I had a brutal appetite…{w} What I saw in the plate literally crippled me!"
    "What the hell is this? I mean, no arguments about the soup, that's prepared according to a classic recipe. But the other dish! Fish boiled in some horseshit along with an egg and mashed potatoes? Anyone who cooks this should be locked up for a year and fed only with such food!"
    scene cg d1_food_normal with dissolve
    "Is it any wonder that dinner gave me an understandable lack of enthusiasm? Soup and kompot - is that even dinner?"
    scene bg int_dining_hall_people_day with dissolve
    "However, there is a way out of this situation as well."
    "If I can't eat, then I'll at least have my share of fun."
    "We used to do this in the camps, when the cooks prepared frankly shit food. The disaster recipe is quite simple — pour everything liquid into the empty glass from under the kompot, doesn't matter whether it was soup or liquified potatoes."
    "We throw on top of all the seasonings in the world in the form of that same fish, slices of bread and leftover soup."
    "Then — attention! — We cover the glass with a plate, and sharply turn the resulting construct!"
    "I touched Ulyana with my elbow, who was thoughtfully observing my actions."
    me "Ulya, let's bet!"
    if alt_day2_dv_dinner:
        show us sad pioneer at left with dissolve
    else:
        show us sad pioneer at center with dissolve
    us "What do you want?"
    "Ulyana asked sadly, rummaging through her plate. She doesn't seem to like the local cuisine either."
    me "Let's bet you won't tear the glass off the plate!"
    us "A glass? Yeah, that's easy."
    "She easily raised her glass of kompot."
    me "Ahhh, from the table any fool would be able to. Try from a plate!"
    "I placed the «cocktail» on the table and pushed it in her direction."
    me "Go ahead! You won't have the strength for it anyways!"
    us "Watch this!"
    "She reached out her hand, grabbed the glass, tugged, and…"
    play music music_list["glimmering_coals"] fadein 1
    show us angry pioneer with dspr
    if alt_day_binder != 1 and counter_sl_7dl < 2:
        "On this day, we switched roles, and I’m already laughing out loud from the door, and the most obscene cry is heard from the hall:"
    us " {b}SEEEEMYYYYYOOOOOOOOOON!{/b}"
    stop ambience
    hide us with dissolve
    hide dv with dissolve
    pause(3)
    scene bg ext_dining_hall_near_day with fade
    "I slipped past the squad leader, pretending that everything was fine, and only when I was on the porch did I allow myself to laugh heartily. This laughter was replaced by hysterical hiccups when an extremely pissed off fury jumped out onto the porch - all in mashed potatoes, fish, egg sauce!"
    show us dontlike pioneer with dissolve
    "Now I will be beaten, and very possibly kicked. Of course, not feeling the slightest desire to fall victim to small fists, I started from my place and ran. This time I was ahead, so we ran around the warehouse twice, once around the library.…"
    scene bg ext_warehouse_day_7dl
    play ambience ambience_camp_center_day fadein 5
    if alt_day1_el_followed == 1:
        "…and past the same meadow where Elektronik was hiding yesterday, with tall grass."
    else:
        "And past some meadow next to the warehouse building, literally overgrown with tall grass."
    show us angry pioneer at cleft with dissolve
    pause(1)
    show us angry pioneer at cright with move
    "Here Ulyanka could not keep up with me, she stumbled and would have flown to the ground if I had not had time to catch her. She hung in my arms, at times glaring hostilely from under of a piece of fish, and again I could not help laughing."
    me "Now that was fun."
    us "No it wasn't."
    "The potato-fish monster grunted, but involuntarily smiled."
    show us smile pioneer at center with dissolve
    us "How did you do that glass thing? Show me, ye?"
    me "Wash up, I'll tell you then."
    show us dontlike pioneer with dspr
    us "Washing up won't help, I need a full shower!"
    "She wiped her slippery hands with disgust."
    me "Let's go at least wash your face and hands."
    stop ambience
    scene bg ext_washstand_day with fade
    $ alt_day2_us_shenan = True
    play music music_list["everyday_theme"] fadein 5
    "Considering myself avenged, I decided to show a bit of nobility."
    play sound sfx_open_water_sink
    pause(1)
    play sound_loop sfx_water_sink_stream
    "I took Ulyanka to the washbasins and for a good half an hour rubbed off the stains, combed out her hair and controlled the process as a whole.."
    stop sound_loop
    play sound sfx_close_water_sink
    scene bg ext_houses_day with dissolve
    show us shy2 pioneer
    "We finished when the camp had already announced a quiet hour."
    me "Now we probably can take a nap?"
    show us surp3 pioneer with dspr
    us "You crazy? It's the best time for swimming!"
    "Ulyanka was indignant, all red from cold water."
    me "Didn't have enough water procedures?"
    us "You don't get anything! This is water procedures, and that's swimming!"
    scene bg ext_house_of_dv_day with fade
    show us normal pioneer
    $ alt_day2_dv_us_house_visited = True
    "We walked along the houses, and had almost reached the one indicated by Ulyanka - not semicircular, but a kind of trapezoidal one, with a Jolly Roger on the door, when Olga Dmitrievna came across us."
    show mt angry  pioneer at right
    "To say she was angry was an understatement."
    mt "Semyon!"
    "Putting her hands to the sides she began."
    mt "What's this, we already have Ulyana?"
    mt "I understand her, she's young, she wants to play. But you, you!"
    me "Why me."
    "I looked down, almost like when I was a child, and shut down."
    show mt rage  pioneer at right
    mt "The pioneers have already reported to me about your exercises with a glass. And you know what I'll tell you, Semyon - decent pioneers don't behave like that!"
    mt "You showed disrespect for a teammate, for the work of cooks and for the image of a pioneer in general."
    me "I didn't show anything. And besides, that's our personal business."
    mt "And cleaning up the nightmare that was left after you is also your own business? Alright. If I hear or see something related to both of you - and you'll be in deep. All clear? And now, march back to your houses, it's naptime!"
    hide us with dissolve
    hide mt with dissolve
    scene bg ext_house_of_mt_day with dissolve
    play ambience ambience_camp_center_day fadein 1
    pause(3)
    scene bg int_house_of_mt_day with hpunch
    play sound sfx_open_door_kick
    play ambience ambience_int_cabin_day fadein 6
    "Angry at the entire world, I went back to my house, slammed the door behind me and collapsed on the bed without taking off clothes. They'll get wrinkled? Who cares. Don't care. Let everyone see a true pioneer."
    "I was well aware that motives like «to spite my mom I'll freeze my ears» were obvious in my behavior, but what could I do."
    "I lay there for another ten or fifteen minutes, painstakingly pitying myself and plotting sly revenge, when there was a soft knock on the window."
    play sound sfx_knock_glass
    me "Who the hell… {w}is itching there."
    "Ulyanka stood there and smiled with all her thirty-two teeth, having already changed her soiled shirt for the usual scarlet T-shirt."
    me "What?"
    "I asked gloomily, preparing to continue indulging in existential suffering."
    us "Let's go."
    "She beckoned me."
    me "Where?"
    us "Let's go!"
    "She impatiently stamped her foot and then gasped, putting her hands to her mouth."
    "From the direction of the entrance to the house came the creaking of a chair. It looks like Olga is sunbathing while reading another ladies' novel."
    if (counter_sl_7dl == 3):
        "And it'd be better if I followed my original plan."
        "In the end, I understood perfectly well that, by definition, she would not drag me into anything good."
        "So I drew the curtains and, ignoring the indignant hiss, went to sleep."
    else:
        menu:
            "Do not agree":
                $ karma += 10
                me "Are you crazy?!"
                "I hissed."
                me "You didn't have enough reamings from Olga, come on, let's get some more?!"
                "Ulyanka looked at me somehow very offended. But I know all these tricks."
                "You're not fooling me."
                me "I won't go anywhere with you. Go to sleep."
                "Ulyanka seemed to be upset. She sighed, and hunched her shoulders as she walked away. And where did her usual enthusiasm go?"
            "Agree" if counter_sl_cl < 1:
                $ lp_us += 1
                $ alt_day2_us_escape = True
            "Threaten her with squad leader":
                $ karma -= 10
                "I glared at the source of my troubles, staring at me with blue eyes."
                me "Forget it. I'm not going with you."
                us "What? Why?"
                me "No reason. Get lost before I summon Olga."
                us "Dumbass."
                "And then she disappeared."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_grand_escape:
    scene bg ext_house_of_mt_day with fade
    "She thinks she's Cerberus, huh."
    "This determined my choice in favor of Ulyana, and I opened the window."
    "A few seconds later we broke through the bushes and entered the path."
    scene bg ext_houses_day with fade
    play ambience ambience_camp_center_day fadein 5
    show us smile sport
    me "Where are we going?"
    us "Let's…"
    show us laugh2 sport with dissolve
    "Ulyana looked into my eyes, and I really did not like the expression that I saw at the bottom."
    show us smile sport with dspr
    play music music_list["you_lost_me"] fadein 3
    us "Escape!"
    me "Escape?!"
    us "Yeah! Let me just run by the house, I'll take the necessary things."
    hide us with dissolve
    "In fact, we had already approached the house where Ulyana and Dvachevskaya lived."
    "She quickly retreated into the house, and it suddenly dawned on me - I remembered this look!"
    "It was with this look that my ex hyped me for completely crazy sex in the vestibule of an intercity train…"
    "It was with such eyes that we bungee jumped - first in pairs with an instructor, then in pairs together."
    scene bg ext_house_of_dv_day with dissolve
    "With those same eyes she yelled «hold my beer!», and then I sat by her bed for weeks while she got better."
    "That look could only mean one thing — {i}a woman deigns to go nuts, you are invited, attendance is required{/i}."
    show us normal sport bear with dissolve
    "Absorbed in thoughts, I shuddered when the door creaked again, and Ulyana appeared on the porch - she changed her shoes for sneakers and pressed a bag of sweets and a bear to her chest."
    "It was very funny, really. But I did not let a single feature of my face flinch - this picture was so touching and funny. So I swallowed all objections to her:"
    us "Shall we go?"
    "And just nodded."
    "We sat down in the next bushes, the girl from somewhere in her pocket took out a crumpled map of the camp - obviously torn from the information stand - and poked her finger, trying to figure out where and how to get out."
    scene bg ext_house_of_dv_day
    show us smile sport bear
    with dissolve
    us "I calculated everything."
    "She spoke in a strong voice."
    us "We'll leave through forest, at night. I deliberately stole more candy than usual to last longer. First we will eat them, then we will switch to grazing."
    me "You're holding the map upside down. {w}And there are almost no forests in the vicinity. There is a wooded wedge sandwiched between a field and a river, but... By the way, what was the river called?"
    us "I don't remember. We were told the name, but I forgot everything."
    "She bluntly admitted."
    me "In short, I see two escape routes - to the bus station, and there we cut a few kilometers along the secondary road before we get to the intercity route."
    show us sad sport bear with dspr
    us "We'll get caught! Think of something else."
    me "Something else is - here."
    "I pointed at the river."
    me "It occurred to me that we would be walking too long if the district center was really far away. Therefore forests, fields and roads disappear. What remains?"
    show us grin sport bear with dspr
    us "What?"
    me "Railroad!"
    "I lightly flicked her forehead."
    me "Think, head, I'll buy you a cap. The highway can go from nowhere to nowhere, the forests can be very large. But the railway always connects two settlements. So all we need is to get on the train."
    us "And how do we get there?"
    me "Easy. The main thing — we need to reach the Long Island, get close to the enbankment and wait. If I correctly determined island's type, which should be swampy, which means that the train will inevitably slow down. And that's where we…"
    us "Hop on!"
    "She screamed in delight."
    me "Be quiet, before the whole camp hears us."
    "I got out of the bushes and, looking around every minute so as not to meet Olga Dmitrievna, headed in the already familiar direction to the boat station."
    me "Alright, plan's mine - the details are yours."
    "I strictly looked at her."
    me "Don't let us down."
    show us sad sport bear with dspr
    us "What details?"
    me "Distract the ferryman or steal the oars, it's up to you. I will row. If there is anything to row with in the first place."
    us "Yessir!"
    "She saluted."
    stop music fadeout 3
    me "Off you go!"
    scene bg ext_boathouse_day with fade
    play music music_list["you_won_t_let_me_down"] fadein 7
    play ambience ambience_boat_station_day fadein 2
    "When I reached the pier, I signaled Ulyanka, sending her around, and I crossed the sandy shore on tiptoes and, trying to stay in the shade, shortened the distance to the gatehouse with short dashes."
    "Someone was clearly in the building, there was noticeable movement and a bright picture - TV."
    "Trying to breathe every other time, I went around the security room, looking around every second, crept to the very pier - and, crouching at the pontoon, I took out the stored paper clip from my pocket, straightened it and, shaking it, tried to bring the squiggle inside the lock."
    "The lock came across obstinate, with a larva on a spring, but I broke through worse - less than a minute later, when Ulyanka waved her hand at me from behind the pier building, I was already unwinding the chain."
    "At last the boat untied itself and danced on the water. A classic punt, the entire stability of which depends only on the weight of the riders."
    "Having estimated our total weight, I realized that it would be a hell of a trip, and pushed the boat along the pontoons, taking it out of the berthing area."
    "Ulyanka caught up with me halfway and deftly jumped to the stern bank, making the ship shake and dance."
    show us smile sport bear with dissolve
    me "Get in!"
    "I took the oars from her and, after a little hesitation, put them right on the edges of the boat - it was stupid to hope that Ulyanka would also steal the oarlocks."
    "An indignant, angry cry came from the shore - there some old man with a cigarette in his teeth jumped out onto the pier and ran, shaking his gray hair and hairy fists."
    me "Adieu!"
    scene cg d2_us_boat_escape_7dl
    with dissolve
    "I shouted and leaned on the oars."
    "It was hard to row, the body resisted such a load and said that it refused to work in this mode!"
    "First, the shoulders ached, then the forearms, back, neck. All this time, Ulyana was sitting across and eating sweets, putting the candy wrappers in her pocket."
    "As a result, when there were no more than fifty meters to the Long Island, everything in me hurt, so I abandoned the oars."
    us "Why did you stop rowing?"
    "She chewed on another candy and stared at me."
    me "No reason. Just got fed up."
    us "How?! But we escaped!"
    me "Yeah. And?"
    us "What part didn't you get? Keep rowing!"
    "She seemed to resent my stupidity."
    me "Maybe you'll row, for a change?"
    us "No. I'm not allowed to. I'm a girl."
    "I'd fucking tell you who you are."
    "A few minutes later, the blood circulation returned to its previous volume, and I, trying not to lean too much, smoothly sent our ship towards the island."
    "Another five minutes - and Ulyana jumped onto the sand. Following her, I also went in, housewifely pulling the boat deeper onto the shore and fastening it to a tree."
    us "What's next?"
    stop music fadeout 6
    scene bg ext_island_day
    show us normal sport bear
    with dissolve
    play ambience ambience_lake_shore_day fadein 3
    play music music_list["tried_to_bring_it_back"] fadein 7
    me "Next we wait for the train. Jump on it, and leave."
    us "I wish it would come faster."
    "She looked plaintively into the bag."
    us "I'm almost out of provisions."
    "I sat down on the ground and wearily closed my eyes. Looks like another daily quota of stupidity has been met. Well, that's pleasing."
    me "At least give me one."
    "I held out a shaking hand."
    us "Nuh-uh."
    "She greedily pressed the bag to her chest."
    "But, after a second she came to her senses and, out of generosity, pushed me a bag."
    "But I didn’t take much, I just wanted to try what my partner was so actively eating there."
    "«Rakovie Sheiki», as I thought. Although their name was a bit different — «Halvichnie», and the manufacturer was stated as «Red Banner named after Krupskaya confectionary factory»."
    "In short, you can't even use candy as a lead."
    "The whistle of a diesel locomotive rang through the water, and our ride carefully drove onto the bridge connecting the mainland and our island."
    me "Ulyanka."
    "I looked back. Leaning against my side, all sticky from sweets, Ulyana was sleeping peacefully."
    me "Ulyana! Get up!"
    scene cg d3_ussr_catched
    with dissolve
    us "What? Whatchu want?"
    "She reluctantly answered."
    me "Train! Get up."
    us "Train?"
    me "Yes! Let's move."
    scene bg ext_island_day
    show us normal sport bear
    with dissolve
    "We approached the very border of greenery, which surrounded large chipped granite, which served as a holding cushion for the paths."
    "I know that if you take two of these stones, you can strike a spark out of them."
    "And if you throw one stone under the wheels of a diesel locomotive, then the fragments can easily knock out an eye."
    "So I took one of the pebbles from my mischievous partner, who was clearly thinking about it, and dragged her a little further into the forest."
    me "We'll sit here until the locomotive passes. The ideal target is a covered wagon with a sliding door. But any other car will do just fine. Ready?"
    us "Yeah."
    "The girl answered a little tensely."
    "I carefully looked at her. {w}For her, escaping from the camp is an exciting adventure, which she will later talk about at school."
    "But for me? Maybe that's my only chance to break out of this place?"
    "Alright, sober up."
    scene cg d4_catac_us with fade
    play sound sfx_7dl["train_income"]
    "I sat in the darkest bushes, so that it was impossible to see me from the driver's cab, and counted the seconds."
    "We will have little time, although the train moves at a low speed, for us that speed may turn out to be excessive."
    "Therefore, it is extremely important to react in time."
    "The line of sight was three hundred meters, and the smoothly shaking train was in full view."
    me "I was told that no one can catch up with you. But you yourself - will you be able to catch up with the departing train?"
    me "Ready."
    "The distance to the train was reduced to one hundred meters."
    me "Set."
    stop music fadeout 3
    "Fifty meters."
    me "GO!"
    play music music_7dl["runaway"] fadein 3
    scene cg d2_us_trainhop_7dl at fast_running
    with flash
    "The train was going thirty or forty kilometers per hour, so I rushed out of the bushes parallel to its movement.{w} This will have to soften the tug if I catch on."
    "Much faster Ulyana had already run ahead and now, like me, she was looking for where to catch on."
    "And suddenly I felt like my leg painfully collided with something hard."
    th "Oh god damn it!"
    "The next second I was already flying nose first, screaming heart-rendingly:"
    me "!" with vpunch
    stop music fadeout 5
    play ambience ambience_forest_day fadein 5
    "Ulyana turned around and braked sharply."
    "It was a very rash decision on her part, because I immediately slammed into her, knocking the girl off her feet."
    scene black with flash
    us "Ow!"
    "She sprawled under me on the grass, whimpering in pain."
    "No matter how much I wanted to, I could not get up and relieve her suffering - I could hardly breathe myself."
    us "You… you…"
    stop sound fadeout 3
    "The last car of the train rushed past us, and the sound of the wheels faded smoothly into the distance."
    "The escape plan has completely and utterly failed."
    us "You ruined everything!"
    scene bg ext_island_day with fade
    "Finally, I managed to get up and roll to the side."
    show us cry2 sport with moveinbottom
    "Ulyana immediately jumped to her feet."
    "She almost did not suffer from the fall, limiting herself to only a fright and a couple of scratches."
    "Breathing slowly stabilized."
    me "Sorry. Damn this snag!"
    us "Should've looked where you went!"
    "Ulyana was ready either to burst into tears, or to beat me."
    show us cry sport with dspr
    us "We didn't escape because of you!"
    hide us with dissolve
    "I shyly averted my eyes."
    th "Did I really want to escape?"
    th "Our whole plan was idiotic from the start. Why did I sign up for this?"
    show us sad sport with dissolve
    us "What are we gonna do now?"
    me "Guerilla warfare in the woods. You haven't eaten everything yet, right?"
    show us dontlike sport with dspr
    "Ulyana angrily stamped her foot."
    us "Toodles! Let's go back!"
    me "Only if you'll be rowing."
    show us surp1 sport with dspr
    me "Let me catch a breath first…"
    hide us with moveoutright
    "But the little one has already lost all interest in me, joyfully staring at something in the bushes."
    play music music_list["memories"] fadein 1
    us "Strawberries!"
    th "And how do children manage to switch so quickly from universal suffering to simple human joys?"
    "Grunting and shaking, I rose from the ground."
    "Ulyana had already galloped ahead, and I had only to catch up with her."
    th "After all, mustn't I at least make some profit from this crazy trip?"
    with fade3
    "Having eaten strawberries to my heart's content, I blissfully stretched out under a tree."
    "From fatigue and heat, I began to fall asleep."
    show us dontlike sport with dspr
    us "And what are you doing here? Who will take us back?"
    me "You need to - you'll take us back. I'm just fine here."
    show us upset sport with dspr
    th "Oh, that's how little a person needs to be happy: outdoor activities, fresh vitamins straight from the bush and pleasant forest air."
    th "If only she also wouldn't whine under my ear…"
    "But it looked like she took offense and fell silent."
    hide us with dissolve
    "Or just decided to stoically wait for my strength to return."
    show blink
    th "I'll lie down for another ten minutes, and we'll be on our way."
    stop music fadeout 5
    th "If I'll fall asleep - Ulyana will wake me up…"
    pause(3)
    stop music
    play music music_list["orchid"] fadein 7
    "But I was awoken by Olga Dmitrievna's voice:"
    scene cg d3_us_library_4
    with dissolve
    mt "Semyon…"
    mt "Blushing because of what you did in the canteen wasn't enough, and now you also came up with an idea to escape?!"
    dv "Look at them being lovey-dovey."
    "Alisa's voice joined in."
    pause(3)
    "And I suddenly realized that I was not sleeping alone. Or rather, I wasn't sleeping quite by myself."
    "Having hugged me in the style of a cat, putting her arms, legs and stomach on top, Ulyanka sniffed sweetly on my shoulder, still sticky from sweets."
    "It got me awake in no time."
    me "Aaaaaaa!"
    scene cg d4_us_morning
    with dissolve
    us "Uuuuuuuu!"
    "Ulyana screamed, waking up."
    "And Olga Dmitrievna and Alisa stood over us and laughed insultingly."
    "Finally she started regaining her composure."
    scene cg d3_us_library_3 with dissolve
    us "What happened? Why are you screaming?"
    "Grumbled displeased Ulyana."
    me "Right now — nothing. But soon something will."
    "I «consoled» her."
    scene bg ext_island_day
    show mt angry pioneer
    with dissolve
    mt "Have you finished arguing?"
    "Olga, in her usual style, put her hands on her hips."
    me "Um… yeah, why do you ask?"
    "I got up, and somehow by itself it turned out that Ulyanka hid behind my back."
    mt "If you suddenly forgot, then I will remind you. What did I say would happen if you two become a problem again?"
    me "Hmmm? Scold and forgive us?"
    dv "Ha-ha-ha-ha!"
    show dv laugh pioneer far behind mt at right with dissolve
    "Seemed like Alisa was having the time of her life."
    "Olga squinted at the redhead, but said nothing."
    "I tried to make my face as innocent as possible."
    "However, Ulyana's hostile little eyes shining from behind her shoulder somewhat spoiled the picture."
    mt "No, my dears. This time you won't get off so easy. {w}This time I'm giving you proper punishment."
    show dv normal pioneer with dspr
    mt "You, Semyon, and you, Ulyana."
    "She poked her finger in our direction with relish, clearly enjoying it."
    mt "You're on canteen duty tomorrow. For the entire day!"
    $ alt_day3_duty = True
    show us sad sport bear at left
    us "As you say, Olga Dmitrievna."
    "Ulyana got sad. And no wonder, for her not to run for a day is akin to accepting that day going down the drain. What about me…"
    "Tomorrow will be tomorrow. How do I get out of here today? {w}No one will row for me…"
    "I furtively blew on the fresh calluses on my palms and followed the squad leader to the beach. Here the second boat was already visible, like mine, pulled out on the sand."
    "I looked inquiringly at Alisa, and she nodded at the squad leader."
    "What, seriously? Olga was rowing? There ain't no way I'm believing that!"
    "However, I had to believe."
    "After separating us - out of harm's way - the leader took Ulyanka into her boat, and left me alone with Alisa. Pushing the boats into the water, we rowed back."
    scene cg d2_dv_boat_day_7dl with fade
    play sound_loop sfx_rowboat_loop fadein 2
    play music music_list["everyday_theme"] fadein 3
    me "Tell me a secret, what are you even doing here?"
    if (alt_day2_convoy == 'dv'):
        dv "I was worried."
    else:
        dv "Ulyanka was gone for a while."
    "Alisa shrugged casually."
    dv "When I discovered that Ulyana had stolen sweets somewhere, this did not cause alarm - she has a whole palace on a tree in the forest."
    dv "But when I saw that she also took the bear… Well, when Olga approached me, I agreed without hesitation."
    "She sat like a guy, resting her elbows on her knees apart."
    if (alt_day2_convoy == 'dv'):
        dv "Semyon…"
        me "Yeah?"
    else:
        dv "Tell me, newbie…"
    dv "Is that really you were going to run away with the kid somewhere?"
    if loki or herc:
        me "I know I may have given myself the wrong impression."
        me "And I'm very sorry if I offended you in any way."
        "I could not hold it and raised my voice - so that from the neighboring boat, which was led by Olga, they turned to us."
        me "But you have to be a complete degenerate to go on such an adventure, especially with a little girl in your arms!!!"
        us "HEY! I'M NOT A LITTLE GIRL!"
    "I rolled my eyes:"
    me "Imagine it yourself - a little girl in sneakers with a bag of sweets and a bear."
    me "Where will she run away to? Well, we got to the island, look, what an adventure it turned out to be."
    "Dvachevskaya fell silent for a while:"
    dv "I worried about her. Thanks for not abandoning her."
    "I didn't believe my ears. Over the past few days, miracles have been pouring out like from a cornucopia, but the body is already used to reacting to surprises in this way."
    me "Did… You… Praise me?"
    dv "Yes. I'll even tell you a secret for this, just don't tell anyone."
    "She leaned towards me with the most conspiratorial look, and I leaned a little cautiously towards her."
    dv "Yesterday's raid was to feed her."
    "She nodded serenely at the nearby boat."
    menu:
        "Laugh":
            $ karma += 10
            me "I knew it."
            "I burst out into laughter."
            me "You both do things for a reason."
            $ lp_dv += 1
            $ lp_us += 1
        "Shrug":
            me "Anyway you missed out."
            me "That's that and this is this."
            dv "You're not mad?"
            me "Nah… She punished herself."
            $ lp_dv += 1
        "Get angry" if alt_day_binder == 1:
            $ karma -= 10
            "I couldn't find the right words."
            me "So, I, practically with my own hands, fed this little…"
            dv "What, now you wouldn't?"
            me "That's now."
            me "After introduction of a moratorium on insects in food."
    me "Ulyana is a very good girl…{w=.3} If you direct her energy in a constructive direction."
    me "But I never said this and I will deny it!"
    dv "As you say, Don Quijote."
    "Alisa laughed and did not utter another word until the end of the water trip.."
    scene bg ext_boathouse_day
    show dv smile pioneer2 at right
    show us normal sport bear at cleft
    with fade
    stop sound_loop
    stop music fadeout 5
    "We adventured and overslept, completely missing lunch, however, only I experienced some discomfort from this, having worked hard with oars today and almost got the same oar from the watchman towards the end."
    "Strength was spent, and there was no replenishment in sight. Well, I'll deal with it."
    scene bg ext_dining_hall_near_day
    show dv smile pioneer at right
    show us normal sport at cleft
    with fade
    "Having taken us back to the camp, Olga disappeared somewhere, yelling at us in the end - purely for preventive purposes."
    scene bg ext_house_of_dv_day
    with dissolve
    "So I had to, in order not to piss off the squad leader even more, take a walk home to the girls and change Ulyana into uniform."
    show us normal pioneer
    show dv normal pioneer at left
    with dissolve
    dv "Well, now what?"
    "Alisa looked at us."
    "I pointed my index finger up:"
    me "You hear that?"
    "Screams echoed throughout the camp."
    "And so we followed them."
    $ alt_day2_dv_us_house_visited = True
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_siesta:
    play music music_list["trapped_in_dreams"] fadein 3
    scene bg int_house_of_mt_day with dissolve
    "Deciding to spend time with feeling, with sense, with the arrangement, I opened the reader on the phone and, restoring the last bookmark, tried to immerse myself in the fictional worlds of Russian science fiction writers."
    "But the letters refused to form into words, and the words constantly fell out of the lines."
    "Three times I caught myself just moving my eyes through the text, absolutely not perceiving its content."
    "No, seriously, why would I read fiction, when something like this is happening to me!"
    "Sighing, I put the phone aside."
    th "It's good in the camp, they don't ask questions and don't want to ask. Even though it's weird too."
    if counter_sl_7dl < 2:
        th "Slavya stuttered something about 1989... Jesus, I'm almost thirty years old in the past!"
        th "But can she be trusted?"
        dreamgirl "Don't trust anyone. Not even yourself. You can trust me though."
        if not dr:
            th "Oh and we'll have a special conversation with you! Who the hell are you and why are you in my head? You a squatter? A brain slug from planet Slytherinus?"
    "Among other things, as far as I remember, you could be a pioneer until fourteen, and then you went to Komsomol."
    "Either I'm confusing something, or things are a little different here."
    th "Where even is «here»?"
    th "If this isn't the past, then what is it?{w} Another world?{w} Dream?"
    th "Oh right, Semyon's dream, who's dreaming about Semyon who is also dreaming."
    th "…"
    th "Nonsense."
    "Going back to the surrounding people, they're also quite interesting."
    "There are always predators blocking the road, there are always renegades who take apart nooks and crannies, and there is the so-called inert mass, which either unites in interest clubs or moves after a leader who does not disdain to accept the banner."
    "And somehow all of the above happened to end up in my squad."
    "In addition, some of their actions baffle me."
    "For example, the camp leader. Does she really not care that out of the blue she had a new pioneer in her squad?"
    "In winter clothes. During summer."
    "Something's definitely wrong here."
    "While thinking, I did not notice how I fell into a dream."
    if (alt_day2_convoy == 'un'):
        play music music_list["goodbye_home_shores"] fadein 3
        scene cg d3_un_forest
        show prologue_dream
        with fade
        "I dreamed of a forest."
        "And Lena."
        "I don't know where or how, but we've been walking along it for quite a long time, and the lights of the camp flickered like dim fireflies through a thin strip of forest."
        if dr:
            "The girl grabbed my arm so that it hurt, and whispered something fervently, begging, persuading as best she could - I needed to remember… Just don't forget."
        "She did not hang on me, did not fetter, but held on, clinging so that I could feel the frequent beating of her heart."
        "She clung to me not out of fear… But for an entirely different reason."
        "I led the girl, as they lead a partner in a dance, and with the final chords, the inevitable payment for a warm evening, I plucked a kiss from pliable lips."
        "And it was as if she opened her wings, straightened her shoulders and, opening her eyes towards the evening, swam in my arms, greedily, impatiently absorbing my attention."
        "I've never seen her like that. And I don't think I will."
        stop sound_loop fadeout 2
        stop ambience fadeout 2
    elif (alt_day2_convoy == 'dv'):
        play music music_7dl["sheiscool"] fadein 3
        scene cg d5_dv_island
        show prologue_dream
        with fade
        if alt_day2_us_dubstep:
            "The redhead in my dream looks like I remember her in that magical moment when her armor was pierced through with really good music."
            "And that's what all the really good songs are for. Their main task is to extract from our hearts and souls a smoldering coal and, albeit not for long, but inflate it to a state of flame."
        else:
            "Alisa looked incredibly calm and peaceful."
            "What a nice girl."
            "Although knowing her, I would say that it was rather the lazy calm of a well-fed predator."
            "The metaphor jumped out of the subconscious itself, followed by another…"
        "When your eyes sting with the touchingness of the moment, and you sleep three hours a day, because you create, you cannot help but create."
        "When you remember the seven digits of a number stronger than your own name."
        "A fantastic thing happened in a dream."
        "Alisa took my arm. And it wasn't all this cheap and superficial. Just an ordinary girl, a little insecure, but no less attractive for that."
        "We've never been this close before. And so I understand that this is a dream. Alisa needs someone who can subdue her, get used to and put up with all her idiosyncracies and, having gotten within striking distance… Just hug her."
        "And the girl is all scared and trembling. The girl has never had to lose or choose between true friendship and true love. And so she clings to the elbow so that her heart can be heard. Tears keep rolling and rolling from her eyes, unnecessary tears, making it doubly cruel."
        stop sound_loop fadeout 2
        stop ambience fadeout 2
    elif (alt_day2_convoy == 'sl'):
        play music music_7dl["unforgotten"] fadein 3
        scene cg d3_sl_dance
        show prologue_dream
        with fade
        "Slavya…"
        "Me and her… We…"
        "Are dancing?!"
        "God knows how many years I haven’t circled the girl in that very slow dance."
        "And here it's not even camplike in any slightest. One hand on the waist, the second - holds her palm. Almost waltzing."
        "She looks so sideways, and for the first time in all the time that we have known each other, I see indecision and even fear in her eyes."
        "She seems to know that I can bring a lot of pain. 'Cause the world I'm from is so full of it that we breathe pain, vomit pain, and stain diary pages with pain."
        "She's already inside me with rattling keys."
        "Why? Don't open other's heart, if you don't treasure your own."
        "There, under the burnt, scarred armor, hides something that will kill you, turn your life into either an eternal expectation or the remnant of someone's dream."
        "She doesn't care. She wants, she reaches out, and she gets that very half-dead piece of flesh, weakly trembling in her hands."
        "And now, she too, is guilty."
        stop sound_loop fadeout 2
        stop ambience fadeout 2
    elif (alt_day2_convoy not in ('dv', 'sl', 'un')) and ('music' in list_clubs_7dl):
        play music music_7dl["but_why"] fadein 3
        scene cg d5_mi_conv_7dl
        show prologue_dream
        with fade
        $ lp_mi += 1
        "I dreamed of a forest."
        "And Miku."
        "Why do I treat her so well?"
        if persistent.alt_binder:
            if persistent.mi_dj_good_jap:
                "As if I had already seen her somewhere, know her as an extension of myself."
        "Although our acquaintance took place in such a funny way, she seemed very nice to me."
        "But now Miku clung to me, it hurt, hard, and kept whispering and whispering."
        "I did not understand anything and stretched out my hand to stroke her hair."
        "And only after that I noticed that for some reason she was crying."
        "But the tears are almost imperceptible under the rain falling from the leaden sky."
        "And I hug her with all my might, I know something, something terrible."
        "And I don't want to let her go - it could very well be forever."
        "I shake my head and try to find some words to say something, important, irreplaceable, appropriate here."
        "Something that would console her."
        "Something that will let her know that it's okay."
        "But I can't."
        "Instead I turn around, and leave."
        stop sound_loop fadeout 2
        stop ambience fadeout 2
    else:
        scene anim prolog_1
        stop music fadeout 3
        play ambience music_7dl["ambience_safe"] fadein 4
        "I dreamed of random garbage."
        "It's like I woke up inside a dream and realized that I have no legs."
        "Or rather, they're there - but they're these two cotton logs, which are difficult to carry from place to place."
        "Carry one leg after the other from bed to wheelchair."
        "With effort, because they weigh almost half of my body, although they look frail against the background of hyperdeveloped arms."
        "Thanks to my father for helping to equip the apartment - railings stretched everywhere along the walls, making my lair subtly similar to a space station."
        "I'm like the heroine of Sandra Bullock - I drag myself jerking from brace to brace."
        "And like her, my biggest enemy is gravity."
        "The photocell reacted to the movement - with a quiet rustle, the coolers of the system unit reached the standard speed."
        "The most important thing is morning exercise. The most difficult, hateful and humiliating."
        "Toilet visit and water procedures."
        "Sometimes you just want to spit on everything and not go anywhere, get up early in the morning, roll up in a chair to the monitor and sit in front of the computer."
        "But when I won't be able to handle my own body - I won't be able to live."
        "Therefore, on my daily last journey, I grit my teeth, lifting myself, clinging to the first handrail leading to the place of humiliation."
        "Strange, terrible life. I have to work up bedsores on my sides, spitting at the ceiling and harassing my sister who nurses me."
        "And instead, I even manage to laugh heartily every day - after all, laughing every day is very important so as not to go crazy from the view outside the window."
        "I even manage to earn a little, although I wouldn't say they generously pay for my texts."
        "And all of this was provided to me by the Internet."
        "Synthetic reality. Surrogate."
        "A prosthesis for those who are handicapped."
        "Washing took half an hour, after which I returned to the chair and already anticipating how the whole world would open up before me on the other side of the monitor, I pushed the leading rims."
        with fade
        play sound sfx_bodyfall_1
        "And with a roar rolled on the floor, painfully hitting my knee."
    stop ambience fadeout 3
    stop music fadeout 3
    show blink with dissolve
    scene bg int_house_of_mt_day
    "Weird dreams."
    "The shorter they are, the more you actually sleep."
    "Although, perhaps, waking up simply cuts off all but the brightest, most memorable moments of sleep?"
    "Maybe I've been dreaming all this time that I'm walking somewhere or sweeping something."
    "And then - like a flash! Whatever that lingers in memory. All that's left is only to breathe and understand where such a picture came from in my head, and why it is there, and not some other."
    "I glanced at the lock. 5PM."
    "Naptime's over. Time to get up."
    play sound sfx_open_dooor_campus_1
    play ambience ambience_camp_center_day
    scene bg ext_house_of_mt_day with fade
    "I heard some noise, many voices seemed to be arguing about something."
    "After a while, my feet led me to the source of the noise."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_tournament:
    scene bg ext_dining_hall_near_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    play music music_list["sweet_darkness"] fadein 3
    with dissolve
    "Everyone I know was here - the senior squad almost had full attendance."
    show sl normal pioneer at left
    with dissolve
    "Slavya."
    hide sl
    show un normal pioneer at right
    with dissolve
    "Lena."
    if alt_day2_mi_met:
        hide un
        show mi normal pioneer
        with dissolve
        "Miku."
        hide mi
        show dv smile pioneer2 at left
        show us laugh2 pioneer at right
        with dissolve
    else:
        hide un
        show dv smile pioneer2 at left
        show us laugh2 pioneer at right
        with dissolve
    "I'm not even going to speak about the redheads."
    hide us
    hide dv
    with dissolve
    if not ('library' in list_voyage_7dl) or not alt_day2_mi_met:
        "There were a few unknown faces too."
    if not ('library' in list_voyage_7dl):
        show mz normal glasses pioneer at right with dissolve
        "For example, an unfamiliar girl with menacing yellow eyes."
        "The unpleasant effect of her gaze was slightly extinguished by glasses with thick glasses."
        "But only slightly."
        hide mz with dissolve
        "I pushed Ulyanka with my elbow:"
        me "Psst, Ulyanka, who's that?"
        show us smile pioneer at right with dissolve
        us "Where?"
        me "There, in glasses!"
        $ meet('mz','Zhenya')
        us "Aah… That's Zhenya. Our librarian. She sleeps in the library all of time."
        me "Sleeps?"
        us "Yeah! She sleeps, and Shurik and Electronik guard books for her."
        us "And keep pretending that they work in the newspaper."
        us "In my opinion, only Lena works there. She draws."
        me "Is that how it is? I see…"
        show us normal pioneer with dspr
        "I decided that I should approach and get acquainted with the last representative of the local bestiary, but Ulyana grabbed my elbow."
        me "What's wrong?"
        us "Better not. Zhenya doesn't really like people."
        me "Sociopath?"
        us "What?"
        me "Doesn't like people."
        me "Probably grumbles and growls all the time too."
        show us grin pioneer with dspr
        us "Ah! Yeah, that would be her!"
        show us dontlike pioneer with dspr
        us "And she also doesn't like when her books…"
        "Ulyana's face twisted."
        "It was clear that she is not on the best of terms with her.."
        show us upset pioneer with dspr
        us "No matter."
        "Redhead waved away."
        show us laugh2 pioneer with dspr
        me "A real buzzer, huh."
        "Ulyanka giggled."
        hide us with dissolve
    if not ('cyber' in list_voyage_7dl or 'library' in list_voyage_7dl):
        show sh normal pioneer with dissolve
        th "Wait, who's this?"
        us "Shurik, what's the commotion?"
        $ meet('sh','Shurik')
        $ alt_day2_sh_met = True
        sh "We'll tell you right now."
        hide sh with dissolve
    if not alt_day2_mi_met:
        show mi normal pioneer with dissolve
        "There was also that anime girl from the cafeteria."
        "I poked Ulyanka, who was standing right there, with my elbow."
        me "Ulyana, who's that?"
        "Pointing using only my eyes."
        us "You like her? That's her art director, her name is Miku. Yes, for real."
        $ meet('mi','Miku')
        "Noticing our discussion, the girl nodded."
        hide mi with dissolve
    if alt_day_binder != 1:
        show el normal pioneer with dissolve
        "And in the center of the whole flea market stood Electronik."
        el "No, no, there will be no automatic games or replays! We need eight participants to play the minimum playoffs."
        hide el with dissolve
    elif (alt_day_binder == 1) and not ('library' in list_voyage_7dl):
        show el normal pioneer with dissolve
        $ meet('el','Electronik')
        "And in the center of the whole flea market was some blond guy."
        "I saw him last supper."
        us "Cheeser, what if I lose? I can't lose!"
        el "First off, I'm not «Cheeser», I'm «Electronik», second, no rematches or replays."
        el "We need eight participants for the playoffs."
        hide el with dissolve
    show sh normal pioneer at fleft with dissolve
    sh "Maybe we'll recruit people from younger squads?"
    show sl normal pioneer at cright with dissolve
    sl "No. This is our squad's activity."
    hide sl
    hide sh
    show mi smile pioneer at cright
    with dissolve
    if alt_day2_mi_met:
        mi "Where's our new guy? Semyon. Senya?"
        "Miku spotted me and immediately ran off the porch, straight up to me."
        show el normal pioneer at left with dissolve
        mi "Come on, I'm looking for you, screaming here, and you're not responding."
        if ('music_club' in list_voyage_7dl):
            mi "And didn't come to the club either."
            mi "Did you forget or did you not want to?"
            me "Former."
            if (alt_day2_mi_kumuhimo == 1):
                $ alt_day2_mi_kumuhimo = 2
                if dr:
                    dreamgirl "Aren't you forgetting anything else?"
                    th "What do you mean?"
                    dreamgirl "Return her bracelet, you senile fuck."
                me "Speaking of which…"
                "Taking a wicker bracelet out of my pocket, I handed it to Miku."
                me "Your loss."
                me "Has been calmly waiting you at the pier."
                show mi happy pioneer with dspr
                mi "Oh, Senechka, you found it!"
                "She squeezed the bracelet so that her fingers turned white."
                "Looks like it matters a lot to her."
                show mi smile pioneer with dspr
                mi "Thank you so much, Semyon!"
                "She suddenly shouted, at the same time, traditionally for the Japanese, bowing."
                "I just felt how the eyes of those present crossed on us."
                if dr:
                    "I wanted to sink into the ground."
                    me "Stop."
                    "I shushed."
                    me "We don't do things here like that!"
                    "Thank God Miku stopped embarassing me and straightened up."
                else:
                    $ lp_mi += 1
                    me "You're welcome."
                    "I smiled at her."
                    "I just like her."
                    me "Don't lose it."
                    show mi cry_smile pioneer with dspr
                    mi "I won't!"
            else:
                mi "Don't worry, we are open every day. I mean, I. I mean, we. In short, it doesn't matter! Electronik! We have one new player here!"
        else:
            me "I just…"
            mi "Electronik! We have a new player!"
    else:
        mi "And here's our newbie! I'm Miku, hi, and you must be Semyon, right?"
        me "I just…"
        mi "Electronik! We have a new player!"
    $ alt_day2_mi_met = True
    hide mi
    show el smile pioneer at left
    show us laugh pioneer
    with dissolve
    if alt_day2_us_escape:
        us "You mean two!"
        "Of course, where would we be without Ulyana…"
        show dv grin pioneer2 at fright with moveinright
        dv "Three!"
        dv "Count me in."
    el "Well, that's nice. There are eight people, we can arrange a tournament!"
    me "Tournament."
    me "Thanks for asking for my opinion."
    hide dv with hpunch
    show us smile pioneer at cright
    us "Don't be so sour." with vpunch
    "Ulyana poked me in the back."
    us "It'll be fun, and I'll win everyone! Or will I wonner?"
    me "You will run."
    "I prompted."
    show us normal pioneer at cright
    hide el
    with dissolve
    me "And fall."
    us "Oh you…"
    hide us with dissolve
    "Everyone in this camp is so nice. And they are all so simple. Like twenty five cents."
    "A pioneer must help a friend, so you can shamelessly plow him into some incomprehensible tournament and be sure that he will not refuse. Mutual assistance, damn it!"
    me "At least explain what I got roped into."
    show sl smile pioneer with dissolve
    sl "A card tournament."
    "Slavya turned around."
    if alt_day2_us_escape:
        sl "We did not have enough participants, so you, Alisa and Ulyana are very timely!"
    show mt normal pioneer at right with dissolve
    mt "Card tournament?"
    "The theater of events was consecrated by the appearance of the squad leader."
    mt "Why was I not informed?"
    hide sl with dissolve
    show mt normal pioneer at right
    show el smile pioneer at left
    with dissolve
    el "Because this is a squad activity!"
    "Proudly exclaimed Electronik."
    el "I take full responsibility for conducting and organizing it!"
    mt "Alright, you'll organize and run everything by yourselves. Yourselves? You don't need me for anything?"
    el "Cards! Four decks and we know you have them!"
    show mt laugh  pioneer at right with dissolve
    "Olga burst into laughter."
    mt "You devils. How did you even know…"
    mt "But you yourself must understand: this is gambling, and gambling is prohibited in the camp."
    show el normal pioneer at left with dspr
    el "It's not gambling."
    "Fervidly explained Electronik."
    el "It's like a strategy! Almost like chess! I came up with it today."
    show mt smile  pioneer at right with dspr
    mt "Alright. I did agree to this…"
    "She nodded to me, beckoning, and held out a small carved key."
    mt "This is from my locker. There you will find cards…"
    show mt angry  pioneer at right with dissolve
    "She made the most pissed off face she could for a second."
    show mt normal  pioneer at right with dspr
    mt "Under your responsibility!"
    "I twisted the key in my fingers and hid it in the pocket of my shorts…"
    "And then slowly reared my head…"
    "It suddenly dawned on me that I now have to look for something in things - personal things! - a girl who is only slightly younger than the real me."
    show mt smile pioneer at right with dspr
    "Surprisingly, Olga just calmly smiled at me."
    th "It seems that this is what she meant when she said that neither she nor I would be embarrassed of her. We aren't children after all."
    "But either the blush or my slovenly appearance did not add weight to me in her eyes, because she turned away and said in an undertone:"
    mt "Or should I entrust this to Slavya…"
    th "Uh-huh, of course."
    "And then I felt so offended, so touched, that I could not resist and said:"
    menu:
        "I'll do it myself":
            me "What, you can't entrust anything to me…"
            if alt_day2_us_escape:
                mt "Yes, I can't! We'll discuss today's exploits later."
                "I blushed, but still found the strength to continue the argument."
                me "And I ask you not to drag this incident into this unrelated question. We're talking about cards."
                show mt smile  pioneer at right
                mt "Alright. Now's your chance. Use it."
            else:
                "And only then did I realize that again, now through my own stupidity, I got involved in something…"
            hide el
            hide mt
            with dissolve
            dreamgirl "What, proved everything to everyone, smartass? Roped in again for no real reason. Goof is a diagnosis."
        "We could go together…":
            me "Actually, we can go with her if you don’t trust me that much."
            $ lp_sl += 1
            $ karma += 10
            "And then I mentally slapped myself - wait, I was forced to do something against my will, again!"
            hide el
            show sl laugh pioneer at left
            with dissolve
            th "Moreover, they arranged it in such a way that I rushed to do it myself. Wow, you fucking psychos!"
            show mt laugh pioneer with dspr
            "It seems that these thoughts were quite eloquently written on my forehead, as Olga laughed and nodded to Slavya:"
            mt "Will you escort him?"
            sl "Of course, Olga Dmitrievna."
            "If Slavya had heels, oh, how she would flick them in a dashing way now!"
            hide mt
            hide sl
            $ alt_day2_walk = 2
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_walk_alone:
    scene bg ext_square_day with dissolve
    play music music_list["afterword"] fadein 1
    "Antokha understood that he had acted unwise, and that the sorceress wrapped him like a sucker…"
    "Keynote of the last few days in this camp."
    "And then we don’t understand - why was it in the USSR that there was such a strong pedagogical school?"
    "And why shouldn't she be, if the most ordinary squad leader twirls her pioneers as she pleases!"
    "So I decided to see what would come of this venture."
    scene bg ext_house_of_mt_day with dissolve
    if herc:
        "I had a lot of experience playing cards."
        "Although I preferred bullet and all kinds of holdem to all other options."
        "But, nevertheless, I prefer to do it out of love, and not at the order of the squad leader!"
        "I wonder, does she know that I can see through her?"
        th "Judging by the contented face, she knows. Moreover, he enjoys playing in the theater of one spectator."
        "Since yesterday, her behavior has puzzled me greatly - she settles me next to her, despite the fact that there are houses. She is not shy at all, lives nearby, sleeps nearby, and if I were a little less sleepy, I could peep a free striptease show."
        th "She acts as if…{w} As if we knew each other for a long time."
        th "It's as if we're closer than a regular pioneer and a squad leader can afford to be."
        "Maybe I remind her of someone?"
        th "In any case, this is another mystery, the answer to which I will have to find on my own."
        scene bg black with fade
    else:
        "I remember that in the camp we also loved to spend a couple of hours playing «Thousand»."
        "One guy marked the deck and due to this he constantly won."
        "Oh how the boys roughed him up when they found that out…"
        th "It is unlikely that the pioneers will beat me, but why not take a chance."
        th "Moreover, I was again dragged in without my consent."
        "I wouldn't say that I have extensive experience in this area..."
        "However, the number of those caught hot allowed me to draw some conclusions and even master a couple of techniques."
        menu:
            "Mark the cards":
                $ karma -= 30
                th "Just don't get caught."
                "Smiling, I threw the key to the locker in my palm and went into the house."
                $ alt_day2_walk = 1
            "Don't mark the cards":
                "Although in my case it's completely unnecessary."
                $ karma += 10
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_walk_sl:
    scene bg ext_square_day
    show sl normal pioneer
    with dissolve
    play music music_list["afterword"] fadein 1
    "Five minutes later we were walking through the sun-drenched square."
    "The heat subsided a little, and it was very pleasant in the shade of the trees."
    "Slavya was silent, as if lost in her thoughts, and I myself did not know where to start the conversation."
    "So for a while we walked in silence."
    "Children's many-voiced laughter came from the beach, and I looked in that direction with regret."
    "She seemed to guess where my thoughts were headed:"
    show sl smile pioneer with dissolve
    sl "Were you going to run off there today?"
    me "Why not?"
    if ('sports' in list_slavya_7dl) or (counter_sl_7dl < 2):
        me "Especially if your invitation is still valid, and…"
        show sl laugh pioneer with dspr
        sl "It's valid, of course."
        "Slavya smiled."
    sl "But not in the middle of the day. Everyone is constantly rushing there anyway, Olga Dmitrievna has to constantly be on duty there."
    show sl normal pioneer with dspr
    if ('beach' in list_voyage_7dl):
        th "Uh-huh. {w}Seen that, been there."
    else:
        "So that's where she constantly comes back so blooming!"
    me "No rest for the wicked, huh."
    sl "Yeah! She has a hard time already, and no one helps, and I…"
    "She suddenly cut herself off mid-sentence. And this time I understood absolutely nothing. What a pity."
    "For a while we moved side by side in silence, but the ice was already broken, and there was no longer any awkwardness in silence."
    show sl serious pioneer
    me "How's it like - to be squad leader's assistant?"
    sl "You want the details?"
    me "Yeah. {w}No. {w}Don't know. {w}Who do you have to be to be a helper and enjoy it?"
    me "It's like taking Ulyana's energy and using it for good deeds?"
    show sl laugh pioneer
    "She laughed at my metaphor."
    sl "Kind of, yes. But it's also important to just love helping people."
    sl "I’m helping the squad leader, doing exercises, sometimes lead the lineups, fiddling with the kids, playing sports with them…"
    show sl smile pioneer with dspr
    sl "They're so funny."
    "She smiled again."
    if not herc:
        show sl normal pioneer with dspr
        me "You are a ready-made frame for the Ministry of Emergencies."
        "I automatically reacted."
        sl "Ministry of Emergencies?"
        "I estimated the year the ministry was created and realized that I had missed the mark somewhat."
        me "Emergency response, you know?"
        "I was in a hurry to figure out replacement words."
        me "I don't know, DOSAAF… Firefighters, rescuers, like that…"
        show sl smile pioneer with dspr
        sl "Whoa!"
        "The girl's eyes lit up with enthusiasm. It seems that I have just deprived the USSR of one potential teacher. Or a doctor."
        sl "Do they take girls?"
        me "Why not? Service as a service, semi-civilian. Except you're there for life. Understand?"
        show sl smile2 pioneer with dissolve
        sl "All my life doing what I like - is it not a dream?"
        "She laughed and, dancing, turned around herself."
        sl "I used to think of becoming a local historian, ecologist, working in a museum or going to school as a teacher. To help people."
        sl "And here you tell me about rescuers. Helping people, huh?"
        me "Yeah."
        "It seems that someone was very carried away, and we urgently need to put them back on the sinful earth."
        me "But we were going to fetch the cards, remember?"
        scene bg ext_house_of_mt_day with dissolve
        "Slavya's cruising speed differed very little from the speed of sound - so moving around the camp usually took a matter of minutes."
        "I myself did not notice how we got to the house."
        show sl normal pioneer with dspr
        sl "I'll go get them?"
        "Receiving a nod, Slavya disappeared into the house."
        play sound sfx_open_dooor_campus_1
        hide sl with dissolve
        "And I was left alone - and I don’t know, unfortunately, fortunately, but not for long."
        "I did not have time to get bored, as the girl again appeared on the porch."
        show sl smile pioneer with dspr
        sl "I'm ready!"
        me "Then let's go."
        sl "We will definitely return to this conversation, you hear? You must tell me everything."
        "I shrugged."
        me "I must? Really?"
        sl "What?"
        me "Whatever."
        hide sl with dissolve
    else:
        "I cracked. Alertness, inertia towards people has gone somewhere."
        "Dunno why."
        "Maybe because I did not fully believe in their reality? It's like a dream."
        "And in a dream, everything comes to us easier and faster, without stupid rules and restrictions."
        me "As I said, we take the energy of Ulyana and let her do good deeds."
        me "As a child, you must have been a very active girl.."
        show sl laugh pioneer
        sl "Of course! Not a week went by that something didn't happen to me. It's that I don't have time to do stupid things right now."
        show sl normal pioneer at center   with dspr
        "She suddenly hid her smile and looked into my eyes."
        sl "What about you?"
        me "About me?"
        sl "Yeah. What kind of a bird are you, Semyon?"
        me "Penguin. A little lonely, but extremely proud."
        show sl smile pioneer with dissolve
        sl "The way it looks to me, you don't really like people."
        sl "You merely tolerate them."
        me "Honestly… True."
        sl "But why?"
        "And how do I answer you, my dear unintelligent girl?"
        "That I don't believe in people because they didn't live up to my trust?"
        "That I don't like them because ten people have enough meanness and dirt to make another flood without giving us the second Noah?"
        "Or tell about the life of a child who looks at the world with the same eyes as yours, with a soul where, as soon as the time has come, everyone who could only spat and trampled?"
        "Or maybe tell about how the colors of life and sparks in the eyes of people faded?"
        "I belong to the generation that survived the apocalypse. A quiet, calm apocalypse that happened in the hearts of people when they turned their eyes away from the sky towards the blue screens."
        "And I know what will happen to you, to every single boy who wants to be needed by the country, to every single girl who considers helping others to be the highest good."
        "Unlike my weedy generation, you are a stillborn generation."
        "Hell awaits you."
        "And that is why I have no right to take away your childhood from you and open my mouth here with revelations."
        me "Because… It's hard to explain. Let's just say…{w} That people did everything in their power to lose the remnants of my reverence."
        show sl sad pioneer at center with dspr
        sl "What about me?"
        me "You?"
        sl "You're talking to me."
        me "Not true. It's not me talking to you. It's you talking to me."
        me "Where I live, we barely would get a chance to have a word."
        me "Because a girl like you would… never pay attention to a young man like me. It's vulgar and banal."
        show sl serious pioneer at center with dspr
        sl "But that's simply not true!"
        "She shook her hair stubbornly."
        sl "You are an interesting guy, Semyon, and…"
        me "…and I belong to a circle where people like you do not exist by default."
        me "Slavya."
        "I sighed."
        me "Just trust me."
        me "You are a wonderful person and I am sincerely glad that you exist.."
        show sl surprise pioneer at center with dspr
        me "The only problem is that people like you are rare even in this ideal communist world of yours. I've never met anyone like you."
        "The always self-confident girl now looked like someone had hit her in the stomach full-swing."
        sl "What you're saying, Semyon…"
        sl "…is wrong and disgusting. We are pioneers, we will always support each other."
        me "Not «we», Slavya."
        th "There can be no «we», idiot."
        me "Let's stop talking. This topic is unpleasant to me."
        "Slavya nodded and obediently fell silent."
        "Seems like she got disappointed."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_ultim:
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_dining_hall_near_day with dissolve
    if alt_day2_walk != 2:
        "I returned with the cards to the canteen, where the tournament was supposed to take place."
    else:
        "We returned with the cards to the canteen, where the tournament was supposed to take place."
    show dv normal pioneer2 with dissolve
    "And on the porch, Alisa was clearly looking already bored."
    if alt_day2_walk != 2:
        "I pushed the door and…"
        "Slammed into an arm, blocking my path!"
    else:
        "Slavya walked past her with an absent look - and for some reason it seemed to me for a second that a certain spark had slipped between them."
        "There was a strong smell of danger in the air…"
        "I tried to slip after Slavya, but I stumbled upon Alisa's outstretched hand."
    show dv angry pioneer2 with dspr
    play music music_list["always_ready"] fadein 3
    dv "Where are we hurrying?"
    "She inquired venomously."
    play sound sfx_close_door_1
    "The closed door cut off everyone, leaving only me - against it."
    if alt_day2_us_escape:
        dv "Played enough with the kids, switched to older kids? Isn't it time to get out of the sandbox?"
        me "Alisa…"
    else:
        me "Alisa, what do you want?"
    "I sighed wearily, not trying to go further."
    "I would not have succeeded anyways - she stood between me and the door, and menacing notes clearly appeared in her tone."
    if alt_day2_walk == 2:
        dv "Running from one sandbox to another. {w}Helping, greasing up our activist…"
    dv "Hurrying, huh…"
    "The anger on her face was visible to the naked eye."
    dv "They said to bring the cards and off you galloped!"
    if loki:
        me "I didn't need to? You yourself wanted, beautiful? Should've said so, I wouldn't be offended. Let me take them back now, and then you yourself can go for them?"
    else:
        me "What's your problem?"
        me "First, nobody even asked for my opinion, I got - what do you call it - appointed. Responsible for card delivery."
        me "Second, again, why do you even care?"
    th "She won't get off. Is she jealous or something?"
    show dv normal pioneer2 with dissolve
    dv "Look at this perfect boy. You probably never even held cards in your hands."
    "Well you don't have to be a genius to figure this one out - she definitely wants something from me."
    "But what?"
    if loki:
        me "No, never. But I know they told me to start with diamonds!"
        dv "Ugh. Stop clowning!"
        me "But you were the first to start! You slowed me down, started calling names and taking on a show off. How vain."
        if (alt_day2_convoy == 'dv'):
            me "If you wanted to call me on a return date, you could've just said so."
            me "So, where and when?"
            show dv shy pioneer2 with dspr
    else:
        me "But I did."
        show dv smile pioneer2 with dspr
        "I grinned lazily."
        me "And definitely longer than you, rest assured."
        dv "You?"
        "She didn't seem to believe her ears."
        dv "Maybe you also think you're gonna win?"
        me "Be sure, I'll flatten all of you like first-graders. See you in the finals."
    show dv smile pioneer2 with dspr
    "And if before that Alisa was just playing, trying to probe me for weakness, now it seems that she is bogged down to the full!"
    "All those meaningful winks, twitching of the corners of the eyes…"
    show dv guilty pioneer2 with dspr
    "I was still reproaching myself for my intemperance, but she suddenly stopped laughing and asked, narrowing her eyes cunningly and even biting her lip in anticipation of something known to her alone:"
    dv "Wanna bet?"
    "She blurted out, looking sullenly."
    show dv smile pioneer2 with dspr
    me "Conditions?"
    "I frankly enjoyed the sight."
    "After the excitement washed away everything superficial from her, under the crust of rudeness, callousness and evil, there was a very pleasant mischievous girl, somewhat reminiscent of Ulyanka."
    th "Well, that explains how they get along!"
    "But about the bet…"
    dv "I bet on you losing!"
    th "Not a bad start. I wonder what she'll bet? Some scandalous rumor?"
    me "Hm… Well, I bet on you losing too."
    "I yawned."
    me "Not interesting. What are our rates?"
    dv "Our rates… If you win, I'll get off your case! And I won't ever bother you!"
    if loki and (alt_day2_convoy == 'dv'):
        me "Hey! We didn't agree on that. I can't take your bet!"
        dv "What? Why?"
        me "The answer is obvious:"
        "I burst out into laughter."
        me "Because I {b}don't want{/b} you to get off me!"
        dv "Is there anything you can take seriously?!"
        me "Okay, let's say I accepted your bet. And if I lose?"
    else:
        me "As if that ever bothered me… But let's continue."
        me "What happens if I lose?"
    if alt_day2_walk == 1:
        th "Only if she has her own markings."
    "It seems that Electronik wasn't exactly honest about the game being new."
    if herc or loki:
        "The excitement of Dvachevskaya turned out to be a very contagious thing - not even a minute had passed, and I was ready to bet anything! Thank God, Alisa saved me from stupid things by issuing her condition."
    else:
        "And Alisa was already stating her conditions."
    show dv smile pioneer2 with dspr
    dv "If you lose, then I…"
    "She thought about it, biting her lip again, smiling all the while, and blurted out:"
    dv "I'll tell everyone that you spied on me while I was changing… And…"
    show dv laugh pioneer2
    "This is where she burst out laughing."
    dv "…grabbed me in places!"
    if (alt_day2_convoy == 'sl') and ('medic' in list_voyage_7dl) and alt_day1_us_shotted and (not alt_day2_us_dubstep):
        me "What about the meeting later on?"
        dv "Meeting?"
        me "Yeah. You wanted to beat me up because I sniped your little girlfriend."
        dv "Forget about it."
        if alt_day2_us_escape:
            dv "Especially since… eh, don't bother."
        "She waived me off."
        dv "Bet comes first! So! Either we bet, or I'll tell everyone…"
    if loki or herc:
        "She looked at me triumphantly, and I was choked with exactly the same laughter."
        me "Literally everyone?"
        "Laughing, I asked."
        dv "Everyone!"
        "She seemed very pleased with herself."
        show dv smile pioneer2
        me "Sorry if something is wrong, but are you going to announce it on the lineup or catch every pioneer in the camp here on the square and report it personally? Like, so and so, Semyon spied and grabbed me."
        dv "I'll think of something."
        "She wryly smiled."
        menu:
            "Bet!":
                $ lp_dv += 1
                $ lp_un -= 2
                $ alt_day2_dv_ultim = 1
                show un cry pioneer at right
                show un normal pioneer at right
                with dissolve
                "I was about to answer, when Lena silently emerged from behind me."
                show dv angry pioneer2 at center with dspr
                dv "Whatchu want?!"
                show un scared pioneer at right with dspr
                un "N-nothing…"
                hide un with dissolve
                "Poor girl hurriedly disappeared in the depths of canteen."
                me "Alright."
                "I was suddenly taken with excitement, and I held out my hand."
                me "Ulyanka, break it."
                show dv rage pioneer2 with dspr
                dv "ULYANKA?!"
                "Alisa's eyes squared up. And when the bushes behind us crackled, and a smiling kid jumped out of there, Alisa was closer than ever to maiming her best friend."
                show us laugh pioneer at left with easeinbottom
                dv "You… You were eavesdropping?!"
                show us smile pioneer at left with dspr
                us "Why would I eavesdrop on you?"
                "The child waved away with a gesture clearly peeped from Alisa."
                us "Your arguing can be heard from anywhere in the camp!"
                us "I went to change, came back to see how things were going, and you're here yelling!"
                me "Will you break it?"
                us "Sure thing. I'll also add to the condition: you were also peeping on me."
                show us grin pioneer at left with dspr
                "She burst out laughing, and the palm hit from above, cutting our clutch."
                show dv angry pioneer2 with dspr
                dv "Good luck, to all of us."
                hide dv with dissolve
                "Alisa wished and vanished behind the door."
            "No bet!":
                $ lp_un += 1
                $ lp_dv -= 2
                $ alt_day2_dv_ultim = 0
                show un cry_smile pioneer at right
                show un normal pioneer at right
                with dissolve
                "Steps creaked behind us, and Lena passed by."
                "Trying to look at the floor, she tried to seep past us."
                show dv angry pioneer2 at center
                with dspr
                dv "Whatchu want?!"
                show un scared pioneer at right with vpunch
                un "N-nothing…"
                hide un
                with dissolve
                "Lena hurriedly went into the canteen."
                if (alt_day2_convoy == 'un'):
                    me "I don't know what she did to you, but she doesn't deserve to be treated like that."
                    dv "Not your business. Are we betting or not?"
                me "I ain't betting you."
                "I politely pushed her aside and went into the canteen after Lena."
                "Someday I will regret my actions. Perhaps Dvachevskaya will even tell everything that she thought up for herself there. That's her right."
                "But I won't have any of that."
            "So that it's fair":
                play music music_list["that_s_our_madhouse"] fadein 3
                $ lp_dv -= 10
                $ lp_un -= 5
                $ alt_day2_dv_ultim = 2
                $ karma -= 15
                show dv surprise pioneer2 close at center
                show un surprise pioneer at right
                with dissolve
                dv "What the hell are you doing, numbnuts!"
                show dv surprise pioneer2 far at center
                show dv angry pioneer2 far at center
                with dspr
                "She slapped my arms and quickly dodged to the side."
                dv "You're batshit insane!"
                show un scared pioneer at right
                with dspr
                me "What's wrong? You yourself said that I laid my hands on you! It'd only be fair that way!"
                "Lena appeared out of nowhere and hastened to sneak past us."
                un "I-I s-should go…"
                hide un
                with dissolve
                "And Dvachevskaya approached me with the clear intention of fighting."
                "Except I reacted just like the first time - stretching out my raking palms forward - just at the level of her chest."
                dv "If even once more you…"
                show dv rage pioneer2
                me "Oh come on, you just got grabbed by the chest. You lost anything?"
                show dv shy pioneer2 at center with dissolve
                "She stood like a poppy flower and definitely did not know what to do."
                "A normal girl would have slapped me a long time ago, I would have intercepted her hand…"
                "Well, of course, we would have gone to the second round."
                "But for this manwoman such matters were too dark."
                me "Now you can consider the bet to be on."
                "I took pity on her."
                me "Although you still owe me a peepshow."
                "Without allowing her to insert even a single word, I entered the canteen."
                "Pretty nice evening, huh!"
    else:
        $ alt_day2_dv_ultim = 1
        "The bastard enjoyed the moment!"
        "And I, seemingly, would have to pay a visit to our nurse - to at least get sedatives."
        me "What are you even saying?!"
        "But the redhead was already all in the grip of dreams about her future victory and did not pay attention to my babbling."
        me "But that's… that's not fair! You can't do this to me!!!"
        "Can she even hear me?!"
        dv "So you'll have to work hard."
        show dv grin pioneer2
        dv "Unless you want the entire camp to know our little secret!"
        hide dv with dissolve
        "And with a ringing laugh, pleased with herself, she ran up the stairs and disappeared into the canteen, slamming the door in goodbye."
        play sound sfx_close_door_clubs_nextroom
        th "God, what did I get myself into…"
        "I slowly and reluctantly followed her, repeating to myself:"
        th "Nobody will believe her. Nobody will believe her."
        "But I didn't even believe myself."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_supper:
    scene bg int_dining_hall_sunset with fade2
    play ambience ambience_dining_hall_full
    play music music_list["smooth_machine"] fadein 3
    "Since the tournament took quite a long time, Olga Dmitrievna announced that everyone was staying right there for supper."
    if alt_day2_gamblers_result['us'] == 22:
        "Ulyana began to scream that she would not have dinner without prizes..."
        "But she was quickly calmed down with a promise of prizes coming after supper."
        show mt angry pioneer with dissolve
        mt "And only to those who are going to behave!"
        "Squad leader stated."
        mt "Misbehavers will get nothing!"
        "Ulyana frowned, but nodded reluctantly and took her seat at the table."
        "After studying her for a few seconds, the leader finally waved her hand, calling the attendants and volunteers."
    "Slavya, Zhenya and a few other girls went to the kitchen to get food."
    "And Electronik, Shurik and a bunch of other kids began to arrange tables in their rightful places."
    play ambience ambience_dining_hall_full fadein 3
    scene bg int_dining_hall_people_sunset_7dl with dissolve2
    "Very soon everyone was already sitting and eating food."
    "And only I couldn't believe what happened to me…"
    "So I barely remembered this supper."
    "I don't think I ate anything…"
    with fade2
    "But even after supper people still weren't leaving…"
    play ambience ambience_medium_crowd_indoors_1 fadein 2
    "The atmosphere in the canteen became more and more tense - everyone was waiting for something."
    show mt normal pioneer at center with dissolve
    play music music_list["always_ready"] fadein 1
    "Then, finally, Olga Dmitrievna came out."
    show mt smile pioneer with dissolve
    "She looked very important now, but also pleased with herself."
    mt "Everyone! I am very pleased that you yourself were able to organize and hold this event."
    mt "You all did your best."
    "She involuntarily squinted in the direction of Ulyanka, who flashed a shit-eating grin."
    mt "Great job!"
    $ volume (0.7,'sound')
    play sound sfx_concert_applause fadein 1
    "Everyone clapped, stomped and screamed."
    pause(1)
    stop sound fadeout 1
    $ volume (1.0,'sound')
    "After waiting until the wave of enthusiasm subsided, Olga Dmitrievna continued:"
    mt "Therefore, as a reward for today's efforts, all today's tournament participants receive this prize!"
    "A reward for today's suffering, I'd say."
    "The door to the kitchen block swung open and two chefs came out carrying a huge strawberry cake!"
    th "Ha! A cake!"
    th "For an unsuspecting squad leader, she was surprisingly quick to find her bearings."
    "I looked at Olga Dmitrievna, standing next to me with the most cunning expression on her face."
    "Catching my eye, she winked at me."
    "Of course, squad activity, she didn't know anything."
    "Clowns!"
    "The fans screamed - and it is not clear what was more in their cry, either delight, or disappointment that they would not get the cake!"
    mt "Everyone else gets candy!"
    $ volume (0.9,'sound')
    play sound sfx_concert_applause fadein 1
    "And then everyone started screaming!"
    pause(1)
    stop sound fadeout 1
    $ volume (1.0,'sound')
    "Slavya has already cut the cake in half so that, together with Olga Dmitrievna, she could distribute it to the waiting pioneers as quickly as possible."
    if (alt_day2_gamblers_result['us'] == 22):
        "And Ulyana, still beaming with happiness after her epic victory, went up to the cake and…"
    else:
        "And Ulyana, suspiciously pleased after her crushing defeat, crept sideways to the cake, and…"
    stop music fadeout 1
    scene cg d5_cake with dissolve
    with vpunch
    play music music_list["that_s_our_madhouse"]

    "Dug into one of the pieces with her teeth, immediately snatching off half of the cream tower!"
    mt "Ulyana!"
    "Olga Dmitrievna screamed indignantly and tried to pull her away, but the kid was escaping and continued to bite and bite the cake!"
    "And as if that was not enough, she was still screaming something with her mouth full, splashing cream, crumbs and pieces of berries around:"
    if (alt_day2_gamblers_result['us'] == 22):
        us "TFHAFHT MFY CFAKFE! {w}I FWFOWFN!"
        "She swallowed and added:"
        us "And also…"
        mt "Yes?"
        "Olga Dmitrievna loosened her grip for a fraction - literally - of a second, and this was enough for Ulyana to bite off another piece!"
    else:
        us "I FHAFHD TFO FWIFN!"
        us "FWIFNW TFHE CFAKFE!"
        "The rest was completely undecipherable…"
        "Finally, she bit off a particularly large piece and fell silent for a while, trying to chew it."
        "During this time, the squad leader has already managed to pull her back."
        "This is how it remained in my memory - Ulyanka escaping, being pulled away by Olga Dmitrievna, Alisa on the other side of the table, condescendingly watching the scene, Lena next to me, judging by her finger stained with cream, who also managed to join the tasting."
    if alt_day2_gamblers_result['mi'] >= 21:
        "Miku, who had no less rights to the unfortunate confectionery, kept aloof."
        "She secretly laughed both at how the squad leader and Ulyana were fighting, and at how Lena and Alisa were already conducting a tasting while nobody looked."
        "And having laughed her fill, she caught my eye, winked and slipped away from the canteen."

    mt "Ulyana, you'll get it someday!"
    "Seeing what was left of the cake, the squad leader growled."
    "Because there actually wasn't much."
    "There were very few places where Ulyanka did not reach, less than half, so if you cut now for everyone, you will get tiny pieces."
    "But the kid had already chewed and could clearly express her thoughts."
    "She stomped again."
    if (alt_day2_gamblers_result['us'] == 22):
        us "I hold all rights to this cake! It's mine!"
        us "I won it!"
    else:
        us "It's all your fault! It's all because you weren't losing hard enough!"
        us "I had to win and get it! It's mine!"
    scene bg int_dining_hall_sunset
    show mt angry pioneer at center
    show us angry pioneer at cright
    with dissolve
    show us angry pioneer:
        linear 1.0 xpos 1.2
    "With these words, she grabbed the plate with the largest piece and rushed out!"
    hide us with dspr
    mt "Ulyana…"
    "The leader was darker than a cloud. And it seems that in all this drama, only I was quietly dying of laughter."
    "Everyone was standing around confused…"
    show mt smile pioneer with dspr
    "Having examined me, Olga at first reluctantly, but the further, the more, laughed, until at last she burst out laughing heartily."
    show mt laugh pioneer
    mt "Oh she'll get it from me!"
    if (counter_sl_7dl == 3):
        "And soon Lena and Slavya joined her laughter."
    else:
        "And I was thinking what to do…"
        menu:
            "Chase her! I can still save the cake!":
                $ alt_day2_us_cake = 1
            "Cake is doomed, no point in chasing…":
                "Evaluating my chances I decided against it."
                th "Oh well. That won't save the cake."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_sup2:
    scene bg int_dining_hall_sunset with dissolve
    play ambience ambience_dining_hall_full fadein 3
    if alt_day2_us_cake == 1:
        "Supper wasn't over yet."
    show mt normal pioneer with dissolve
    "A knife was brought from the kitchen, and we cut the leftovers so that everyone got a little bit."
    sl "Here…"
    show sl smile pioneer at right with dissolve
    "Slavya laid out small pieces on napkins and handed them out to those present."
    "Even I got a little bit."
    sl "It's yours, my friend."
    "She smiled and handed me my portion."
    me "Thanks, Slavya. You're wonderful!"
    "I smiled back. It seems that Slavya chose the best piece for me: it was bitten off just a bit."
    hide sl with dissolve
    "Maybe that's for the best."
    "Supper won't have to give up its place."
    hide mt with dissolve
    if alt_day2_gamblers_result['me'] == 22:
        pass
    else:
        show dv normal pioneer2 with dissolve
        "Passing Alisa touched me with her shoulder."
        show dv normal pioneer2 close with dspr
        dv "We should talk."
        "She offered."
        "I shrugged, and went after her."
        scene bg ext_dining_hall_near_sunset with fade
        show dv angry pioneer2 with dissolve
        stop ambience
        "A few minutes later we went out onto the porch, and Dvachevskaya instantly pounced on me. She seemed to be furious."
        play music music_list["awakening_power"] fadein 2
        dv "Was that on purpose? You did it on purpose, yeah?"
        "She flared her nostrils and was angry from the bottom of her heart. And the angrier she got, the more fun I had."
        me "Of course, on purpose. Don't you know it's customary to give in to ladies?"
        if alt_day2_dv_ultim == 1:
            dv "You promised! You said you'd play your best!"
        elif (alt_day2_gamblers_result['me'] < 12):
            dv "You didn't want to bet - to hell with you! But these moronic scenes, what is it at all?!"
        else:
            dv "When I offered you a bet, I did not think that you would behave like a ram!"
        "It seemed that a little more, and she would go to beat me with everything that came to hand, so I took a step back, reconcilingly putting my palms out in front of me."
        "She slowed down and stared at me questioningly."
        menu:
            "Calm her down":
                if herc:
                    me "Alisa, come on, let's just take a deep breath and calm down."
                    dv "You idiot!"
                    show dv sad pioneer2 with dspr
                    dv "You don't even know what you want!"
                    hide dv with dissolve
                    "She incinerated me with a look and fell into a subspace."
                    "And I stood on the porch for a long time and looked thoughtfully in the direction where Alisa had disappeared."
                else:
                    me "I don't get why you're so angry."
                    if alt_day2_dv_ultim == 1:
                        dv "We had a bet, and you ruined everything!"
                    "She gave me a contemptuous look."
                    show dv normal pioneer2 with dspr
                    dv "You really are a retard."
                    hide dv with easeoutleft
                    "And I stood on the porch for a long time and looked thoughtfully in the direction where Alisa had disappeared."
                if lp_sl >= 8:
                    "And while I was looking that way, I noticed Slavya heading off somewhere."
                    "She looked like she meant business."
                    menu:
                        "Chase her!":
                            "What am I, stupid? I wouldn't miss such an opportunity!"
                            th "Mysteria blonde, I'm coming!"
                            stop music fadeout 3
                            scene bg ext_square_sunset at zentercenter
                            show sl smile pioneer at cleft
                            with dissolve
                            sl "Where are we sneaking to?"
                            me "Oopsie…"
                            "At some point, Slavya just turned around and noticed me."
                            me "Uh… Well… I…"
                            show sl normal pioneer with dspr
                            sl "Okay, since you were spying on me anyways, let's just go together."
                            me "What?!"
                            sl "I need to do something important."
                            th "Of course…"
                            $ alt_day2_sl_chased = True
                        "Whatever…":
                            th "Eh, let her go, maybe she has a nest there."
                            "I shrugged."
                return
            "What's wrong?!":
                if loki and (lp_sl < 8) and (counter_sl_7dl < 3):
                    me "It's just, you know… I really, really, really immensely wanted to see… How you will carry out your threat!"
                    $ karma += 10
                    $ alt_day2_dv_chased = True
                    return
                else:
                    me "Don't you get that it was just an accident?"
                    dv "You were winking, I saw that!"
                    me "Why do you think so? Maybe I just got a speck in my eye."
                    dv "Ah, yes, a speck."
                    show dv sad pioneer2 with dspr
                    if alt_day2_dv_ultim == 1:
                        dv "Anyways, you lost the bet. Prepare for consequences."
                        me "And you're just going to tell them?"
                        "I didn't hide the fear in my voice."
                        dv "Yes!"
                        show dv laugh pioneer2 with dspr
                        dv "I wonder what will happen to you."
                        hide dv with dissolve
                        "Her laugh was angry and nervous. She stepped off the porch pushing me out of the way."
                        "I decided not to hold her up."
                    elif alt_day2_dv_ultim == 2:
                        dv "You think you can get away with what you did before the tournament?"
                        me "As if I care."
                        me "You have no proof and no witnesses."
                        me "And the squad leader won't even listen to your bush-inhabiting friend."
                        show dv rage pioneer2 with dspr
                        dv "Oh, you think you're the smartest, accounted for everything, huh?"
                        "I shrugged and turned around."
                        "I haven't found any new reasons to spend time on her."
                        me "Don't forget, you still owe me a peepshow."
                        "I lazily threw over my shoulder."
                        hide dv with dissolve
                        "She stepped off the porch pushing me out of the way."
                    else:
                        dv "Even though you did not accept my bet, I will still tell everyone everything. Prepare yourself."
                        me "But it's not true!"
                        "Is she really going to ruin my life?! Just like that? Because of some game?!"
                        dv "Who do you think everyone will believe?"
                        show dv laugh pioneer2 with dspr
                        dv "I wonder what will happen to you."
                        hide dv with dissolve
                        "Her laugh was angry and nervous. She stepped off the porch pushing me out of the way."
                        "I decided not to hold her up."
                    if counter_sl_7dl == 3:
                        "And while I was looking that way, I noticed Slavya heading off somewhere."
                        "She looked like she meant business."
                        "What am I, stupid? I wouldn't miss such an opportunity!"
                        th "Mysteria blonde, I'm coming!"
                        stop music fadeout 3
                        scene bg ext_square_sunset at zentercenter
                        show sl smile pioneer at cleft
                        with dissolve
                        sl "Where are we sneaking to?"
                        me "Oopsie…"
                        "At some point, Slavya just turned around and noticed me."
                        me "Uh… Well… I…"
                        show sl normal pioneer with dspr
                        sl "Okay, since you were spying on me anyways, let's just go together."
                        me "What?!"
                        sl "I need to do something important."
                        th "Of course…"
                        $ alt_day2_sl_chased = True
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_slot_us_try:
    scene bg ext_dining_hall_near_sunset at running with fade
    play ambience ambience_camp_center_evening fadein 1
    play music music_7dl["sneakupon"] fadein 3
    "Near the exit I suddenly felt a sense of deja vu…"
    scene bg ext_dining_hall_away_sunset at running with dissolve
    if alt_day_binder != 1 and counter_sl_7dl < 2:
        th "Yesterday I was chasing Ulyana in exactly the same way…"
    "Although something was different now…"
    "A pioneer uniform flashed in front of me, not that red T-shirt…"
    "And when I was already habitually preparing to turn to the sports ground, Ulyana ran in a completely different direction."
    "She was running to the forest."
    play sound_loop sfx_run_forest fadein 1
    scene bg ext_path_day with dissolve:
        linear 0.1 pos (5,3)
        linear 0.1 pos (5,0)
        linear 0.1 pos (-5,5)
        linear 0.1 pos (-5,0)
        repeat
    "And after a few steps we dived into the thickets, so I immediately lost sight of her."
    "Then I had to pursue her by the sound of crackling branches…"
    scene bg ext_path_sunset with dissolve:
        linear 0.1 pos (5,3)
        linear 0.1 pos (5,0)
        linear 0.1 pos (-5,5)
        linear 0.1 pos (-5,0)
        repeat
    "I've been chasing Ulyana for quite a long time…"
    "Evening descended onto the camp."
    "But stopping the chase was out of the question!"
    "I've already run too far and risked getting lost…"
    "And I hoped Ulyana knew the way back…"
    "Finally the noise ahead suddenly stopped…"
    stop sound_loop fadeout 1
    scene bg ext_playground_sunset_7dl with fade
    play sound_loop sfx_inhale fadein 1
    stop music fadeout 3
    "And a second later I, breathing heavily, went out to the sports grounds!"
    stop sound_loop fadeout 2
    if lp_us > 1:
        $ alt_day2_us_cake = 2
    else:
        "I looked around."
        "There was nobody here!"
        th "Where did she go?!"
        "I was literally a couple of meters behind, and she was gone!"
        th "As if she flew away…"
        "I stood still for a couple of minutes, waiting to see if she would show up from somewhere…"
        "But there was absolutely nowhere to hide on an empty football field."
        "So I'll have to put up with it."
        "I also shook my fist goodbye in the direction of the bushes where she could hide, and went back to the canteen."
    stop ambience fadeout 6
    with fade
    return

label alt_day2_eventEv_music_club1:
    scene bg ext_musclub_day with dspr
    if lp_mi >= 5:
        $ lp_mi += 1
        call alt_day2_slot_mi
    else:
        th "Don't want to interrupt her. I'll come back later."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_eventEv_clubs1:
    if not alt_replay_on:
        if been_there_alt2() > 1:
            scene bg ext_clubs_sunset_7dl
            th "The Young Technician's Club knows how to wait."
            stop music fadeout 3
            stop ambience fadeout 6
            with fade
            return
    play ambience ambience_camp_center_evening fadein 1
    scene bg ext_clubs_sunset_7dl with fade
    th "Hm. Closed. In the morning I thought they would be spending their nights here."
    th "Although, I won't need to assemble someone else's robot, thanks for that."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_eventEv_camp_entrance1:
    scene bg ext_no_bus_sunset with fade
    play ambience ambience_camp_entrance_evening fadein 1
    "I went out onto the road."
    "In the pink rays of the setting sun, it looked like a silk ribbon, stretching straight into the horizon."
    "I looked at it, sitting in the shade of a plaster pioneer and listening to the distant chirping of birds."
    th "It's really beautiful here!"
    "But soon it began to get dark, and I went back to the camp."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_eventEv_un_mi_house1:
    scene
    $ renpy.show("bg ext_house_of_un_day", what = Dawn("bg ext_house_of_un_day"))
    with dissolve
    play ambience ambience_camp_center_evening fadein 1
    if (alt_day2_convoy == 'un'):
        "During our tour, Lena pointed out where her house was located. And little wonder that after all my thoughts I ended up here."
        "What I wanted and what I counted on didn't matter, the most important thing - I'm here."
    else:
        "This house was located on the same street as ours with the squad leader, so in the dark, it would probably be very convenient to run from one house to another."
        "Not like it is in those camps that I'm used to, where if you don't make an appointment with the girl, you risk waking up her entire ward of twenty people."
        "I directly imagined a kind of Romeo in family shorts, patterned in «pink heart», with a rose in his teeth and rubber boots with a bottle of «three axes» behind the bootleg."
    if (lp_un >= 6) or ((alt_day2_convoy in ('dv', 'sl')) and (lp_un >= 5)):
        if loki:
            $ lp_un += 2
            call alt_day2_un_loki_date
        elif herc:
            $ lp_un += 2
            call alt_day2_un_herc_date
    else:
        "It was dark in the house, and if I expected to find someone here, I was very late."
        "However, I managed to notice Lena, dressed in a sports uniform, who was clearly heading somewhere."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_eventEv_dv_us_house1:
    scene bg ext_houses_sunset with fade
    play ambience ambience_camp_center_evening fadein 1
    "Either it seemed that way to me, or there were much more people in the camp in the evening than in the morning."
    "As soon as I appeared on the alley, the kids, playing between the houses, stopped and began to look at me in a strange way."
    "Glancing at myself, and, being unable to find anything new, I shrugged."
    kids "Attack!"
    "Suddenly they rushed to me with wild cries!"
    th "Shit! I need to run!"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_eventEv_dining_hall1:
    scene bg ext_dining_hall_away_sunset with dspr
    th "No thanks, supper was enough."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_eventEv_sport_area1:
    scene bg ext_playground_sunset_7dl with fade
    play ambience ambience_camp_center_evening fadein 2
    if lp_un >= 6:
        if dr:
            if alt_day_binder != 1:
                $ lp_un += 1
            call alt_day2_slot_un
        else:
            "I didn't find Lena here. I'll go see if she's in her house."
    else:
        th "Empty."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_eventEv_beach1:
    $ alt_day2_beach_seen = True
    if alt_day2_dv_chased:
        scene bg ext_dining_hall_near_sunset
        show dv rage pioneer2
        stop music fadeout 0
        play sound sfx_angry_ulyana
        with flash_red
        play music music_list["awakening_power"]
        "The last words came from empty air. {w}Being beaten wasn't a positive prospect for me, but after such words I would've hit myself on the back of the head for sure."
        scene bg ext_square_sunset at fast_running
        with flash
        "While I was moving my legs, it occurred to me that in this camp I was running as much as I had never run before. Every day, full force, long distances."
        "I also wondered if Alisa would immediately punch me in the nose when she caught up. That is, IF she catches up."
        scene bg ext_aidpost_sunset_7dl at fast_running
        with flash
        "She had every opportunity. And she didn't seem to want to miss them. However, compared to yesterday's race, this one was a little more merciful, after all, it wasn't me who was chasing someone today."
        scene bg ext_dining_hall_away_sunset at fast_running
        with flash
        pause(1)
        scene bg ext_square_sunset with dissolve
        "We ran under Genda's armpit, went around the warehouse, turned to the volleyball court."
        scene bg ext_volley_court_7dl with dspr
        "Technically volleyball-pioneerball court. The last game, which always strikes me with its liberality, was also played here. If it was possible to recruit at least three participants for each."
        "Crouching, I ran under the net and turned around."
        show dv angry pioneer2 with dspr
        stop music fadeout 3
        "I must confess, I love it! Dvachevskaya, although terrible in anger, was also terrible only by her deeds and reputation. But her appearance - god damn!"
        "I swerved to the left and she duplicated my move."
        "After that, I had only to smoothly slide past her, drawn by inertia, and run down the road. As it became clear to me in a minute leading to the beach."
        scene bg ext_beach_sunset with fade
        play ambience ambience_lake_shore_evening fadein 2
        "How long have I wanted to be here!"
        "But not under these circumstances!"
        "A generously poured sandy tongue crawled underfoot, forcing it to slip, and it was extremely difficult to run."
        "I took a few more steps and stood up, trying to catch my breath."
        "Heavy breathing on the right hand testified that Alisa also had to sweat. This could only make me rejoice."
        "I sat down on the sand and kicked off my shoes, threw shorts with a shirt on top, that damned noose-tie… {w}And with a run dived into the black water under the night sky."
        "Quiet, warm night."
        if (lp_dv > 3) and (alt_day2_dv_ultim == 1):
            call alt_day2_slot_dv
        else:
            "Having bathed, I gathered my clothes, and, after drying a little under the evening sun, I got dressed and went to the square."
            "Alisa seems to have lost interest in the pursuit. Well, or did she have some business."
            "Gotta think about what to do tonight."
    else:
        scene bg ext_beach_sunset with fade
        play ambience ambience_lake_shore_evening fadein 2
        if (alt_day2_gamblers_result['me'] == 22) and (alt_day2_dv_ultim == 1):
            call alt_day2_slot_dv
        else:
            "Been trying to get here all day! In this weather, the sweetest thing is to swim."
            "But now that I finally got here…"
            "Somehow it was no longer the same…"
            "Whether something is wrong, or something is missing, I did not know."
            "Turning around, I left the beach."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_eventEv_me_mt_house1:
    scene bg ext_house_of_mt_sunset with dissolve
    play ambience ambience_camp_center_evening
    "The house was occupied by the squad leader."
    "To tell the truth, after the morning session of peeping, I had such a healthy fear that Olga Batkovna would unleash her fury on me."
    "Thus, I used a supersecret move I learned here."
    play sound sfx_knock_door7_polite
    "I knocked!"
    mt "Come in!"
    "Olga replied from the inside."
    play sound sfx_open_dooor_campus_2
    pause(1)
    scene bg int_house_of_mt_sunset at zenterleft
    show mt smile pioneer at cleft
    with dissolve
    "Olga was sitting at the table, again writing something in her beautiful diary."
    mt "There you are, pioneer."
    "Her smile was kind and warm. {w}Such a good smile - which, in theory, has no place on the face of an adult."
    mt "How's your evening going?"
    me "Pretty boring."
    "I admitted."
    mt "Well…"
    me "What?"
    show mt laugh pioneer with dspr
    mt "Want me to say a thing after which your life will never be the same?"
    me "Uh…{w}You can try."
    mt "When you are embarrassed, your neck and the tips of your ears turn red."
    show mt normal pioneer with dspr
    mt "And when you're angry, your nostrils go like that of a bull."
    me "Nothing goes and nothing turns red!"
    "I screamed, hiding my neck and nose."
    show mt laugh pioneer with dspr
    mt "It looks like you're right - your ears are red and your nostrils are flared at the same time."
    mt "There's no embarassed anger, right?"
    dreamgirl "You're being teased again."
    th "Thanks, I know!"
    show mt normal pioneer with dspr
    mt "Sorry, couldn't hold it in."
    "Olga extinguished her smile and closed her diary."
    mt "Listen, since you don't want to walk around the camp, maybe you can help me?"
    menu:
        "Sorry, I'd rather take a walk":
            "Honestly after such an answer I was expecting a sharp reaction."
            "But Olga surprised me again - she understood."
            mt "I see."
            mt "If you meet Slavya on the territory, please send her to me."
            "I nodded and went out."
            play sound sfx_open_dooor_campus_1
            pause(1)
            scene bg ext_house_of_mt_night with dissolve
            "However, while I was walking, the time was already closing in on the night."
            "Nothing to do, had to move to the washbasins."
            stop music fadeout 3
            stop ambience fadeout 6
        "Okay":
            stop music fadeout 3
            "I answered cautiously."
            $ alt_day2_mt_help = True
            call alt_day2_slot_mt
    return

label alt_day2_eventEv_library1:
    scene bg ext_library_day with dspr
    $ alt_day2_random_val = renpy.random.choice([1, 2, 3])
    if alt_day2_random_val == 1:
        th "The library is probably closed…"
    elif alt_day2_random_val == 2:
        "I definitely didn't want to meet the librarian now…"
    else:
        th "Someone wants to read Kant before sleep?"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_eventEv_medic_house1:
    scene bg ext_aidpost_sunset_7dl with fade
    play ambience ambience_camp_center_evening fadein 1
    th "Nothing is hurting. What would I tell… {w}Viola?"
    if ('medic' in list_voyage_7dl):
        "I remembered the morning…"
    "And I didn't dare to go."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_eventEv_estrade1:
    scene cg d3_dv_guitar with fade
    stop music fadeout 1
    "At the very edge of the stage sat Alisa with a guitar at the ready."
    play music "<from 17.7 to 56.77>" + music_7dl["splin"] fadein 5
    "She purred something under her breath and melancholically plucked the strings."
    "The plucking was somehow familiar…"
    if alt_day2_minijack:
        "Splin? Seriously?"
        "Dvachevskaya, with a solo guitar, trying to figure out the chords of «Romance»?"
        "Some people definitely have a taste in perversion."
    else:
        "Sector Gaza? If I'm not confusing anything, they will only RELEASE this song later."
        "How does she know it?"
        dreamgirl "Actually, that's Splin…"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_eventEv_square1:
    scene bg ext_square_sunset with fade
    play ambience ambience_camp_center_evening fadein 1
    "Nothing has changed here since my last visit."
    "Same faces, same places."
    "Well, jokes aside, Slavya was here, sitting on the steps descending from Genda's pedestal."
    th "And how isn't she cold?"
    if (lp_sl >= 8) and ((counter_sl_cl == 1) or (counter_sl_7dl == 3)):
        "I thought as I approached her."
        me "Good evening."
        show sl normal pioneer with dspr
        sl "Semyon? Hello."
        "I don't know why she was so happy."
        "Although using common sense, it was not so difficult to guess."
        th "She's going to use me again."
        "I thought."
        "And I wasn't wrong."
        sl "Semyon, can I ask you about something?.."
        "She began."
        th "Oh who would've guessed."
        "That cheerful laugh again."
        "I never thought that I would act as an object of laughter for someone - and almost not be offended at the same time."
        sl "Let's go!"
        "She got up."
        me "And if I don't?"
        sl "Then you can refuse when we're there."
        me "Where is there?"
        sl "You'll see!"
        "Having lost all patience, she grabbed my hand and led me."
        call alt_day2_slot_sl
    elif counter_sl_cl != 1 and alt_day1_sl_keys_took != 2:
        me "What are you doing?"
        show sl sad pioneer with dspr
        sl "Looking for keys, damn them."
        if alt_day1_sl_keys_took == 1:
            me "Uh…"
            th "The ones I found yesterday?"
        else:
            me "Keys?"
        sl "I... Lost the bundle. Sorry."
        "She jumped up and ran away."
        hide sl with dissolve
        if alt_day1_sl_keys_took == 1:
            me "But I have them…"
            "I told the empty air."
            dreamgirl "Tell me, wasn't your grandfather Estonian by chance?"
            "There was nothing else for me to do here, so I went on to walk around the camp."
        else:
            "And I was once again amazed at the impressive monument."
            "Since lunch, the monument has not gone anywhere and still corrected his glasses…"
            th "How are you just not tired of standing here, poor fellow."
            if not alt_day2_dv_chased:
                th "Maybe I should share the cake with him?"
                menu:
                    "Why not?":
                        "…"
                        th "Mmm… Tasty!"
                        "The cake was amazing."
                        me "Want some?"
                        "Genda didn't reply."
                        me "Oh well, more for me."
                        th "Silence isn't always a sign of consent after all…"
                        $ alt_day2_cake = True
                    "He'll be fine without it":
                        th "I'll take another walk."
    else:
        th "Alright, I shouldn't disturb her."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_eventEv_boat_station1:
    scene bg ext_boathouse_sunset_7dl with fade
    play ambience ambience_boat_station_day fadein 1
    "Even though it was already evening, it was still warm."
    "The river flowed lazily, lulling the boats and the pier."
    if not alt_day2_dv_chased:
        th "Should I sit here and enjoy the cake?"
        menu:
            "Sure":
                "…"
                th "Mmm… Tasty!"
                "The cake was amazing!"
                $ alt_day2_cake = True
            "Not yet":
                th "I'd rather take another walk."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_dream:
    stop music fadeout 1
    scene bg ext_house_of_mt_night_without_light with fade
    play ambience ambience_camp_center_night fadein 1
    play music music_list["a_promise_from_distant_days_v2"] fadein 2
    if alt_day2_mt_help:
        "The clock struck midnight, there was nothing to do on the street, and I returned home."
    else:
        "It was already well after midnight when I finally reached the house that sheltered me."
    stop ambience fadeout 1
    scene bg int_house_of_mt_night2 with fade
    play ambience ambience_int_cabin_night fadein 1
    if alt_day2_mt_help:
        "Olga is in a meeting."
        "Teapot on the table."
        "Diary, wide open - come and read…"
        "I overcame the temptation with great difficulty."
    else:
        "Trying to move as quietly as possible so as not to…"
        "There was nobody inside."
        "Strange."
        "Or squad leaders are also people and also want to relax? Don't know."
        "In any case, there was no strength or desire to reflect on distant topics."
    if (alt_day2_date == 'mi') or (alt_day2_date == 'sl'):
        "I hastily shook off the sand on the porch, and, undressing, dived under the covers. Cozy, nice…"
    else:
        "I’m tired like I don’t know who, so I didn’t even think about washing - I just dived under the covers."
    "Thoughts wandered lazily somewhere outside my cranium."
    "Answers? There were no answers. And did I look for them, of course not."
    "I showed myself to the camp, looked at the camp itself, enjoyed the sun and carelessness, characteristic only of such places, remote from the ever-rushing civilization."
    "It's fair to say that I did things here that I never did in my old life…"
    "I lived."
    "There were things that surprised me too."
    if ('sport_area' in list_voyage_7dl):
        "Surprisingly bright reaction to the PE teacher's teasing - before, I would just shrug my shoulders and not waste time on this person."
    "Some kind of completely inexplicable mischief of mine, as if pestered by an indefatigable bright-red leech."
    if alt_day2_us_escape:
        "Our «escape»."
    if (alt_my_rival_final.take == 'un') and (alt_day2_gamblers_result['me'] < 22):
        "Tournament in which I, without expecting it, surrendered the game."
        "Just to please someone."
    elif alt_day2_gamblers_result['me'] == 22:
        "A tournament in which I, without expecting it, took first place."
    else:
        "The card tournament, that taught me that sometimes, winning isn't all there is to life."
    if (alt_day2_date == 'un') and dr:
        "Lena… Unsociable, modest, silent. I saw myself in her eyes. And the more touching it was «saving» her from an owlet, which caught her shuttlecock."
        "When she hid behind me, I realized that I would do everything to help and save this fragile creature."
    elif (alt_day2_date == 'dv'):
        "And this Alisa… Box with a double bottom. It seemed to me that we almost reconciled, almost became friends. A little more, and…"
    elif (alt_day2_date == 'sl'):
        "Slavya… {w}This girl never ceases to amaze me."
        th "Would I catch up with a person who turns his back on me like this?"
        th "Not really…"
        "But she did. {w}Because she is glorious."
        "I smiled at the way it sounded."
    elif (alt_day2_date == 'mi') and (alt_day2_mi_date != 2):
        "Miku… {w}At first, her manner of speaking led me to complete horror."
        "But now, after a little closer look, I even find her in a special way cute."
        "The main thing to remember is that where a normal girl is embarrassed and lowers her eyes, Miku chatters."
        "I wasn't looking for a normal girl either."
    elif (alt_day2_date == 'us'):
        "Ulyanka evoked a simultaneous desire to shelter, rescue, save - and strangle."
        if alt_day2_us_escape:
            "Her bag of sweets, a bear touchingly pressed to her chest."
            "Never had a younger sister, but if I did, I would like her to look like Ulyana."
        "Her performance with the cake…"
    else:
        if (alt_day2_date == 'mt'):
            "Surprisingly cozy, warm evening next to the squad leader."
            "Angry-angry, but as she thawed out, she turned out to be such a good person."
            "Albeit somewhat shameless."
        elif alt_day2_mt_help:
            "She made me do something again."
            "It seems that for our Olya I am the best mouse in a lab coat - a prototype for testing pedagogical techniques."
            "Doesn't look like I'm that against it though."
    "But, as the heroine of «Gone with the Wind» says: «I'll think about it tomorrow.»"
    if (alt_day2_date == 'us'):
        th "Ulyana…"
    elif (alt_day2_date == 'mi') and (alt_day2_mi_date != 2):
        th "Miku…"
    elif (alt_day2_date == 'sl'):
        th "Slavya…"
    elif (alt_day2_date == 'un') or (alt_day2_date == 'un_fz'):
        th "Lena…"
    elif (alt_day2_date == 'dv'):
        th "Alisa…"
    th "I'm so tired…"
    "I lay down comfortably, put my hand behind my head and closed my eyes."
    play sound sfx_open_dooor_campus_2
    show mt normal pioneer with dissolve
    "Almost falling asleep, I heard the door open and Olga Dmitrievna touched me on the shoulder."
    if (alt_day2_date == 'mt'):
        mt "Everything alright?"
        me "Everything except you leaving me on the porch…"
        me "I was sad and lonely…"
    else:
        mt "Well, how did you like your first day in the camp?"
        mt "Made any memories?"
        me "More than I expected… {w}less than I wanted."
    show mt smile pioneer with dissolve
    "I barely moved my lips, but she still heard and smiled."
    mt "Right, you should sleep."
    mt "Tomorrow will be a new day."
    hide mt with dissolve
    scene bg black with fade2
    "…"
    scene cg d1_end_of_day_7dl with dissolve
    "I fully agreed with her."
    scene black with fade2
    "And a second later I was fast asleep."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_slot_us:
    $ alt_day2_date = 'us'
    scene bg ext_playground_sunset_7dl with dissolve
    play ambience ambience_camp_center_evening fadein 2
    stop music fadeout 3
    "I looked around."
    "But there was not a single soul around!"
    th "Where did she go?!"
    "I was literally a couple of meters behind, and she was gone!"
    th "As if she flew away…"
    "I stood still for a couple of minutes, waiting to see if she would show up from somewhere…"
    "But there was absolutely nowhere to hide on an empty football field."
    th "Looks like I'll have to deal with the loss of the cake."
    "I also shook my fist goodbye in the direction of the bushes where she could hide, and was about to go back to the canteen, when a stifled chuckle was heard from behind."
    "I couldn't not recognize it!"
    th "Where did she come from? Fell from the sky, right?.."
    "I turned around and saw with horror how she…"
    stop ambience fadeout 1
    play music music_list["revenga"]
    if persistent.hentai_graphics_7dl:
        scene cg d2_us_soccer_sunset_7dl with dissolve
    play sound sfx_soccer_ball_kick
    "With a fervent laugh, she hit the ball that had come from nowhere, and…"
    "Flew straight at me!"
    "It's speed was insane - evading or rebounding wasn't possible!"
    "As if in slow motion, I watched the projectile fly towards me…"
    "And a second later, with a powerful blow, I was already knocked to the ground!"
    play sound sfx_soccer_ball_catch
    with vpunch
    scene bg ext_playground_sunset_7dl with dissolve
    play ambience ambience_camp_center_evening fadein 2
    th "Good that it hit my stomach and not anything lower…"
    "The impact took my breath away, which undoubtedly saved Ulyanka from the flow of swears against her."
    "But she wasn't even thinking of running!.."
    stop music fadeout 3
    th "How naive!"
    play music music_list["always_ready"] fadein 3
    show us laugh2 pioneer with dissolve
    us "Hey, why are you wallowing?"
    th "Let me… Breathe…"
    us "You've been chasing me for so long…"
    show us grin pioneer with dspr
    us "Ha!"
    "She grinned and showed her hands smeared with cream."
    us "There's no cake left!"
    us "You're late! You're late!"
    "She started running around and throwing a ball at me."
    "And I was finally able to breathe normally…"
    me "What did you do in the canteen?"
    me "Olga Dmitrievna will punish you tomorrow!"
    show us dontlike pioneer with dspr
    "Ulyana puffed up."
    us "You only have yourselves to blame!"
    if (alt_day2_gamblers_result['us'] == 22):
        us "I won, that was my cake, and you started cutting it up."
        us "Greeders!"
        "She flashed her eyes."
    else:
        us "You should've gave in!"
        us "It was me who supposed to win!"
        show us angry pioneer with dspr
        us "Me!"
        "She bit her lip."
    "And heartily slammed her hand on the ball."
    th "I hope she doesn't want to repeat that hit of hers…"
    if (alt_day2_gamblers_result['us'] == 22):
        me "But that was for everyone."
        me "Don't tell me you wanted to eat all of it yourself?"
    else:
        me "Maybe next time you'll be luckier…"
    "I said this to calm her down a little, but she understood it in her own way."
    show us dontlike pioneer with dspr
    if (alt_day2_gamblers_result['us'] == 22):
        us "Of course! My cake! Mine!"
    else:
        us "Next time I'll figure out how to beat everyone at once!"
        me "Sure thing."
    stop ambience fadeout 1
    stop music fadeout 2
    scene bg ext_playground_night with dissolve2
    $ night_time()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night fadein 2
    show us dontlike pioneer with dissolve2
    "While we were arguing, it was already noticeably dark on the site, and the first stars appeared in the sky."
    me "Are you going to ask for forgiveness?"
    show us angry pioneer with dspr
    "But Ulyanka only frowned even more."
    me "Let's go, you'll apologize and Olga Dm…"
    "She cut me off."
    us "I'm not going to apologize to anyone!"
    th "Now she looked like she was actually pissed off!"
    play sound sfx_soccer_ball_kick
    "Ulyana kicked the ball with all her might, and it flew away like lightning somewhere into the darkness…"
    th "Thank god that it didn't go to me…"
    play sound sfx_broken_dish
    with vpunch
    "Judging by the sound of broken glass, the target was the window of the indoor gym, standing nearby!"
    us "Oops…"
    show us shy2 pioneer with dspr
    "She said it so childishly that I even felt a little sorry for her…"
    th "Olga Dmitrievna wouldn't let that go easily."
    me "And what are you going to do now?"
    "But Ulyanka only shrugged her shoulders and said thoughtfully, picking her uniform with her finger."
    us "I'll just say that you broke it…"
    me "What?!"
    "At the same time, she blinked her eyes, as if she did not understand why I was so unhappy."
    show us surp3 pioneer with dspr
    us "What's wrong?"
    us "A boy should protect a girl…"
    show us calml pioneer with dspr
    "Then I remembered why I was chasing Ulyana."
    me "And the girl should blame the boy, yeah?"
    me "Come, just apologize to Olga Dmitrievna and…"
    show us laugh pioneer with dspr
    "I tried to take her hand, but she deftly dodged and jumped back to the bushes."
    $ lp_us += 1
    us "Olga Dmitrievna! Olga Dmitrievna!"
    "She mocked me."
    us "I'll show you tomorrow!"
    show us grin pioneer with dspr
    us "I'll show you all!"
    hide us with dissolve
    "And with these words she jumped back into bushes."
    th "What a day, huh?!"
    "There was no point in running after her."
    "I stood a little longer and went to my room, thinking about how I would justify myself if I was also accused of breaking glass…"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_slot_mi:
    $ alt_day2_date = 'mi'
    $ alt_day2_mi_date = 1
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_musclub_day
    with dissolve
    stop music fadeout 1
    "Miku made a lasting impression."
    "Perhaps she might seem noisy, hurried and even annoying to someone, but not to me."
    "I know this type of people. You just need to be able to listen to them - cutting off the water and attempts to leave along the associative chain to other thoughts."
    "And suddenly I was attacked by a kind of stupor - indifferent and senseless."
    "At the tournament, I still held on, and leaving the canteen - too… But even the Atlanteans have a limit of strength."
    "The stress of the day had drained me of what little strength I had left."
    "It turned out all the more surprising that I didn’t want to hide in the shell and quietly die there."
    "No. I was looking for aggravation."
    "Painful suffocation with a stream of words, torture through rhetoric - for someone nearby to talk, and talk, and talk."
    "I was looking for Miku."
    "She amazingly cheered me up in the morning."
    "How? That's a se-cret."
    th "She won't mind if I abuse her company a little, right?"
    th "When we met, she was delighted with a new face as if she had been day and night without getting out under her piano for weeks, devoid of any decent company.."
    th "Now she can talk to me!"
    "The club was closed… {w}What did I expect."
    "I, as a typical representative of the caste of losers, should have expected only such an outcome.{w} So screw me, no soul-saving brain drain for me."
    "I sighed, turned around and left."
    $ alt_day2_beach_seen = True
    scene bg ext_beach_sunset
    with dissolve
    play ambience ambience_lake_shore_evening fadein 3
    play music music_7dl["you_are_soul"] fadein 3
    "My feet took me to the beach. Fortunately, now there were no ubiquitous children around, squad leaders, attendants, and so on and so forth."
    "The direction to the right was blocked by the woods, so I shrugged my shoulders and moved to the left along the bank."
    "This direction was no worse than any other."
    "A breeze hit my right shoulder, my head was empty and somehow painful. Despite my hydrophobia, I have always had a very special relationship with water."
    "When they say that a person can look at the primal elements endlessly, I remember exactly water. Because personally, the fire does not cleanse my soul, and the earth with the wind - too."
    "But to sit on the bank and dissolve in the endless run of water jets…"
    "Even as a child, I loved to run away somewhere on the river and, after sitting to my fill, having indulged in stone skipping, I felt somehow renewed…"
    "But here it was not like that. Starting with the fact that the water did not calm me down, ending with the fact that absolutely flat smooth surfaces suddenly refused to jump on the water and please the eye with an even chain of rebounds."
    "I raised my hand to my eyes."
    "Fingers were trembling."
    th "Spectacular, now I'm shaking like a drunkard."
    dreamgirl "Now what? Did our retard suddenly realize something significant?"
    "For example, the fact that my old life ended somewhere."
    "From a gray dusty swamp, where only I was my own master, and would have lived, adding up an endless series of days for decades, the only significant event of which would be pressing the power button for the personal computer."
    "Well, or if everything is completely sad, and the computer does not even turn off, then my favorite page refresh key."
    if herc:
        "I have always been a hot-headed person, but over time I have learned restraint. And my rather calm reaction to the camp only confirmed this."
        "Despite the fact that life gave me a good pat, doing everything so that my inner core was worn to dust, indifference did not reign in my soul."
        "Even though I lost faith in people, but thanks to one fluffy lump I retained my humanity."
    elif loki:
        "I have always considered myself a cold-blooded person who does not give way to emotions even in force majeure circumstances. And my rather calm reaction to the camp only confirmed this."
        "Despite the fact that life has dragged me down a lot, the even and benevolent attitude towards the people around me was a matter of special pride."
        "Maybe this is not very correct, but calm. And quiet. Just too intimate for every person."
    elif dr:
        "I have always considered myself a calm and balanced guy. And my rather calm reaction to the camp only confirmed this."
        "Somehow never got by touched anything. Actually, even the ex-girlfriend fled, not least because I really didn’t feel anything."
        "Have I ever felt anything at all?"
    "Comparing with childhood, with dreams of romance and adventure, brought up on Dumas and Stevenson, Greene and Bulychev, I believed that all these bookish passions - they exist! You just have to dig deeper, look a little closer!"
    "Not to waste time participating in the play called 'love to the grave', where neither of the lovers feels anything - but to seek…"
    "It just looks like there's not much to look for."
    "No romance, no love, no passion, no blood vows."
    "There is dust, dullness and a panic fear of being left alone during declining years. That same treacherous fear, pushing by the arm and forcing you to take what they give."
    "And I'm so fucking tired of everyone seeing me as a backup option."
    "So what's the deal then? Why am I worried to the point of trembling in my hands, so that neither skipping stones, nor water, nor silence can save me?"
    "Is it my conscience?"
    "After all, I am, in fact, completely different. I have nothing to do with these children, nor with their state, goals, mentality, finally."
    "And although Olga saved me from the need to get out, dodge, lie, posing as a pioneer - is this not why I only feel more foul in my soul?"
    "For some reason Miku suddenly appeared before my eyes."
    "Well, yes, especially in front of this unfortunate Japanese girl, who is so dreary and lonely at her club that she is ready to communicate even with a retard like me."
    "And eyes, eyes, look at them - crazy, crazy. You look at them - and wow! - as if from a water slide, from fifteen meters down you fly! She doesn’t squint, she doesn’t frown, but all the same, she looks as if she is the kindest father Lavrenty Palych, and now you, the contra, will be crushed."
    "And that whole story is stupid, with the piano and the harmonica. She got up and brushed herself off, and I felt ashamed. As if it was her, and not me catching her sprawled like the letter «z» under the piano."
    "That's why it fouls and unbalances impotent anger, for unknown reasons."
    me "Damn japanese bitch!"
    "From a long silence, the ligaments do not have time to relax, and I seem to croak these words, and the wind carries them along the beach."
    "At the base of the skull a pricking, caused by someone else's presence. There was a tickling pressure between the shoulder blades, betraying a gaze. Works flawlessly with impressionable natures."
    "I didn't react. Even when the sand creaked behind me, betraying someone else's steps, I did not turn around, and continued to throw and throw unfortunate smooth surfaces, trying to knock out at least two skips."
    "What the hell…"
    "The throws were getting angrier and sharper, and there was less and less sense in them."
    "Finally, someone touched my shoulder."
    if persistent.mi_dj_true:
        menu:
            "I shrugged my shoulders in disgust":
                $ alt_hpt += 1
                $ alt_day2_mi_date = 3
                if (alt_day2_convoy not in ('dv', 'sl', 'un')):
                    $ lp_mi += 1
                "It seems that here not only private property is a bourgeois relic, but also personal space is an invention of impotent people from the Ministry of Health."
                show mi serious pioneer close at center with dissolve
                "Miku…"
                "She looked remarkably thoughtful and silent."
                "For some time, her gaze showed undisguised bewilderment, as if she expected to see me anywhere, but not here, but not for long - until the next moment. The eyelid dropped and cut off everything that I did not have time to ask. Next stop is the final one."
                mi "Are you alone here?"
                "I nodded."
                mi "You managed to become amazingly popular in two days."
                show mi normal pioneer close with dspr
                mi "During the half hour that I was walking here, Olga Dmitrievna, Slavya, Lena, Alisa and even Ulyana asked about you."
                mi "Maybe you shouldn't have left them? Irresponsible."
                "I didn't answer. Fuck the responsibility."
                "I wanted to say something weighty, important, cutting off further questions, but for some reason solid banalities climbed into my head."
                "And Miku is acting kind of strange, taciturn."
                show mi serious pioneer close at center with dspr
                "We sat on the sand and threw pebbles into the water. Then we found a good target - a black boulder sticking out of the water, covered with long growths of moss, and started throwing."
                "I was about three hits behind when Miku tossed the already gathered pebble to the side and lay down on the sand, throwing her hands behind her head."
                me "Has something happened to you? You are so strange now…"
                "I sat with my back to her, and the confession she began went entirely to my back."
                mi "Nothing happened. And it won't happen. You are a new person in my life, and while the travel companion effect is still alive, I want to use you as a vest. Can I?"
                "I shrugged."
                show mi angry pioneer close with dspr
                mi "Let's start with the fact that no one needs me. Even my great father and no less great mother are at home about five times a year, and their visits, God forbid, last for a couple of hours."
                mi "So I grew up as an obvious weed turned on the thirst for communication."
                mi "I never wanted to be alone."
                mi "Ne{w=0.5}ve{w=0.5}r."
                show mi serious pioneer close at center with dspr
                "She talked and talked, choking on words and hurrying to tell as much as possible before the listener left."
                "And there was no more of that compressor pressure in her voice when I met her in the music club. The stream of consciousness was replaced by the usual, slightly confused recitative of a monologue-confession."
                show mi normal pioneer close at center with dspr
                mi "There is nothing surprising in the fact that sitting at home constantly alone - and I couldn’t just leave the household and go outside for a walk - I earned myself a mania for communication."
                mi "I take every new person and talk to him and talk and talk until he gets sick of me. And then he leaves."
                "She fell silent."
                mi "And so will you."
                me "Well, that's up to me."
                "I stretched out on the sand next to her."
                me "Keep going."
                show mi shy pioneer close with dspr
                mi "I scared all my peers and friends - first on the other side of the Japanese border."
                mi "Then on this side."
                mi "Endless moving, constant change of people with whom I communicate, eternal stress due to the fact that peers can not stand communication with me."
                mi "They even talked about a boarding school, but, thank God, my father did not dare."
                show mi serious pioneer close at center with dspr
                mi "And there I turned 16, and here I am. In the hope that at least something will change here."
                mi "It's no secret to you that very special children have gathered here, Semyon?"
                show mi normal pioneer close with dspr
                mi "For example, look at Slavya, Electronik, me…"
                mi "We are all kind of progressive children… But in reality - we're outcasts."
                mi "And here, as if in a social experiment, we are - what will happen if we throw several freaks into one jar."
                me "Stop."
                "I objected as gently as I could."
                me "We are not freaks. Just stumbled upon each other."
                show mi cry pioneer close with dspr
                "Turning my head just to catch her eye…"
                "…I almost turned back."
                "That's where the feeling of being watched! The last few - a few? - minutes, it seems, she lay like that, staring blankly in my direction…"
                "And cried."
                "Tears, running non-stop over the elastic white skin, hissed, buried in the cooling sand."
                "I didn't know what to do."
                "Pity her - but how? {w}I don't know how to."
                "I don’t know any words of consolation, and the highest measure of pity for me has always been to let a person sob."
                "Moreover, it is not words that are needed here, but something else."
                "But what?"
                "So without inventing anything, I lay like a moron, looking into her wet eyes."
                show mi sad pioneer close with dissolve
                mi "And you tell me we aren't freaks…"
                "She sighed softly."
                mi "If you were already afraid of your own pity for a crying girl, so that your pupils are still shaking…"
                "Suddenly there was a bitter lump in my throat."
                me "I-I'm not afraid of anything… I just…"
                mi "Of course, you just. You just can't be sorry. You don't know how to love. All you have left is your breath. Replace it with the ticking of a clock and no one will know the difference."
                mi "The problem is that no one is trained in this wisdom in the camp. We - none of us - can't just be part of society."
                mi "Because smart books won't teach you that. {w}Only life will teach this - a normal, healthy life in the ranks of peers."
                me "I don't believe in that. It doesn't happen that we were specifically looked for."
                mi "Really? Remember your last relationship. If it ever happened, of course."
                mi "The feeling that everything is not real, pretend, with masks, dances and confetti. Does that remind you of anything?"
                me "…"
                mi "Simply because there's nothing. There is nothing in us. Because no one has ever put anything there."
                me "It must grow on its own…"
                show mi angry pioneer close with dspr
                mi "It mustn't, not for anyone!"
                mi "We are here the heralds of the future humanity - people without fear and reproach."
                mi "One thing I just do not understand - why is this camp here? Why all this beauty, these beaches, forests… {w}What for? If we still fail to appreciate it."
                mi "Wouldn't it be easier to just put us in concrete boxes and keep us there, feeding us with waste once a day?"
                "It seems that she began to drift, and I hastened to calm her down."
                me "But it's not true…"
                "I turned on my side and leaned on my elbow, thus being a little higher."
                me "About emotions."
                mi "True."
                "She bit her lip and looked up at me expectantly."
                mi "Not true? True…"
                "She whispered, and tears again beat their way down tear-stained cheeks."
                me "Nonsense."
                me "Please stop, or…"
                mi "Or what? {w}You'll tell the squad leader? {w}Complain to the director? {w}Take me to the nurse?"
                mi "Or you'll just abandon me here, on the beach? {w}The last thing you do damn well - the girls unanimously praise you!"
                "Here she, of course, went overboard."
                me "Worse."
                play music music_list["confession_oboe"] fadein 3
                show mi surprise pioneer with dspr
                if alt_day2_mi_kumuhimo == 2:
                    "I leaned over her, caught her wrist - the bracelet slightly scratched the pads of her fingers - and found her lips with mine."
                else:
                    "I leaned over her, caught her wrist, and found her lips with mine."
                "Due to a long lack of practice, straining where I should not have, I kissed her insistently and clumsily, and she kept looking through me, as if she did not see at all."
                "Finally, she realized what had happened, and, squealing, she pushed me away, rolled away on her own."
                show mi shy pioneer with dspr
                mi "What are you doing, crazy? You can't just pick up and kiss a girl right away! Maybe she is not ready, or thinks about something else, or even wants to be a little alone!"
                "She chattered and chattered, and I looked at her and smiled."
                me "Welcome back, Miku. I like you more this way."
                "She just waved her hand."
                mi "Of all the strange people in this camp, Semyon, you are the strangest!"
                "I nodded in agreement."
                me "We'll need to do this again someday."
            "I froze":
                $ alt_spt += 1
    if not persistent.mi_dj_true or alt_day2_mi_date != 3:
        "It seems that here not only private property is a bourgeois relic."
        show mi serious pioneer close at center with dissolve
        "Miku."
        "I turned away, preventing her from reaching her usual machine-gun speed."
        "Perhaps if I pretend not to notice anyone, she will play along? And leave me alone."
        "Of course not!"
        mi "Semyon? Hello! What are you doing here? All the girls asked about you there, they were looking for you, probably. Sometimes it happens to me that I want to hide somewhere where no one will find - but only for a while, just to get some rest."
        me "Then you should understand me."
        "I answered awkwardly."
        "I didn't want to be rude - she's still a girl, after all…"
        "It seems that she either did not understand the hints, or did not appreciate."
        mi "Are you alone here now? If you were with someone, you can just tell me not to interfere, then I'll leave and look for another place."
        me "I was alone. Until now."
        mi "So we'll sit together now?"
        show mi smile pioneer close with dspr
        "She clapped her hands and blossomed into a smile."
        if ('music_club' in list_voyage_7dl):
            mi "And I was waiting for you at the club, but you didn’t come and didn't come. And then Lena told me that she saw you somewhere nearby, and then you disappeared."
            me "Why would Lena care…"
            mi "I don't want to gossip, because I think that gossip is stupid and dirty, but still, these are my observations! Can I share my observations?"
            me "Maybe."
            mi "I think Lena liked you. That is, in the sense of how the guy liked, and not the way they say in Russian «don't like» and mean dislike."
            me "Miku, can you speak a little simpler? One thought, one sentence."
            mi "But am I speaking so incomprehensibly, when we lived in Japan, dad praised me for how I handle idioms, and here you criticize me. But criticism is always helpful. So what did you mean to say?"
            me "Too many thoughts in one phrase. I don't know which one I should respond to."
            me "You are fond of vocals - one phrase should contain one thought."
            show mi upset pioneer at center with dspr
            mi "But then you won't have time for everything!"
        mi "Actually, wait here!"
        hide mi with dissolve
        "She jumped up and ran away."
        th "Thank God! Chaingunner Miku redirected her own divine wind onto other targets."
        th "Although she wouldn't make a good kamikaze."
        dreamgirl "Well, she's not ramming you with herself, but rather with a word stream. {w}Maybe we should just quietly leave before she comes back?"
        th "No, I wonder where she ran away and why. Not to the toilet for sure."
        dreamgirl "Your call, dude, you might not have any other chances."
        th "Whatever."
        "Moreover, I finally began to get ricochets - scanty, miserable, for a couple of bounces - and yet!"
        "The pebbles creaked again behind me, and Miku stood beside once more."
        show mi normal pioneer at center with dissolve
        mi "Do you know what the Japanese say about flowing water?"
        me "I know. That's why I'm here."
        me "Where did you go?"
        show mi smile pioneer at center with dspr
        mi "I decided that it would not be superfluous to have some music on the evening beach."
        me "You're speaking in short sentences."
        show mi normal pioneer at center with dspr
        "She lowered her head."
        mi "I accept any help. It's better than sitting alone in a club, where everyone who comes to visit me is Alisa, whose guitar is out of tune, and Olga Dmitrievna - to pick me up to clean the area."
        me "And for how long have you been cooped up there?"
        show mi serious pioneer close at center with dspr
        mi "As long as we have been here - all two weeks. I get up in the morning, I sit in the club all day, and in the evening I come here."
        play music music_list["farewell_to_the_past_edit"] fadein 2
        mi "The most worthless time in my life. And my father so insisted, persuaded - they say, here, in the best camp in the world, is the only place where I can recover a little before the summer is over.."
        me "Recover?"
        mi "Study, performance, work, dancing… And loneliness."
        mi "I left one loneliness to fall into another."
        "She pressed the play button, and a song in Japanese poured out of the speaker."
        "Very good. If we were in my world, I would immediately ask to pass it to my player and listen the shit out of it."
        "Three minutes of playback - the format of the radio station - we were silent, each listening to their own."
        if alt_day2_mi_snap:
            mi "Uncle Borya said that the pictures would be ready by tomorrow. Will you get them?"
            me "Don't know."
            "I did not like to be photographed - non-photogenic, God forgive me."
            "But already completing the phrase, with some tenth instinct, I understood and twisted:"
            me "Rather, I wouldn't, if I would be there alone."
            me "And since we're there together - of course, of course."
            show mi smile pioneer with dspr
            mi "This is how you should respond to a girl."
            "She smiled softly, half in her own daydreams."
            "The song probably was the reason for that."
        "I liked the music, and Miku, judging by the sad eyes, was not listening to the most cheerful text."
        me "Beautiful song. What's it about?"
        mi "About a dream."
        "Simply replied Miku."
        me "Can you tell me anything about yourself?"
        me "I heard something about you, it seems that you are quite popular in the Land of the Rising Sun."
        show mi shy pioneer close at center
        with dissolve
        mi "Not exactly popular, here it would be more appropriate to say that I was lucky to be at the right time in the right place."
        mi "You have a similar show on TV called «Morning Star», where children, like me, show their talents."
        "I shrugged. With my love for TV, I could believe in the existence of such a show."
        me "I don't watch TV. But keep going."
        mi "There was a concert, a gala concert, where the best of us were pulled up to the required level and, depending on external parameters, they were given a ticket to showbiz. I was lucky to be born with a pretty face."
        "She rubbed her left cheek with displeasure, where a blush immediately flared up from the touch of her fingers."
        mi "Therefore, I was saved from the fate of a seiyuu. And then a thump, a power outage, and there aren't only the Japanese in the hall, there are also guests from other countries - they are panicking, rushing somewhere."
        me "And you?"
        mi "I was afraid too. Scary, scary, you know, makes you want to hide in a prompter hole and not get out of there - but I look over the spotlights at these faces, distorted by horror, and continue to sing."
        mi "The only thing I could do back then was sing, you know?"
        mi "I really did not want that the beautiful dress that we chose for a week, the hairstyle for which I had to sit still for more than an hour in front of the mirror…"
        mi "Even those unfortunate shoes with high heels…"
        "She stretched her leg forward, letting me admire the shoe with high solid heel."
        mi "And I didn’t want to just ruin everything by sobbing and running away from the stage, to the point I was trembling."
        mi "Moreover, the television center building was earthquake-resistant - me and Dad knew about this."
        show mi sad pioneer close at center
        with dissolve
        mi "I sang and counted the thumping beats."
        mi "And on the last line earthquake ended…{w} Well, I wasn't called anything other than «Daredevil Miku» at first."
        show mi smile pioneer close at center
        with dissolve
        mi "After that, life has turned - how do you say it in Russian? — into the golden dojo? Golden cage?"
        me "The last option is if you're talking about a well-fed life in seclusion."
        mi "Your «fidgets» at least communicate with each other. And what about a poor girl who has no one to even say a word to?"
        th "In such cases, the Internet can help. You can always find a partner."
        th "Unfortunately, you were born a bit too early for that."
        show mi angry pioneer close
        with dissolve
        me "You can talk to me, I'm right here."
        mi "You are remarkably patient for an unfamiliar pioneer. Usually they can't handle for more than fifteen minutes, and even then only while gritting their teeth."
        mi "Sometimes it seems to me that if there was no club, the squad leader would send me to live in the forest or on duty at the boat station - anything, just so as not to hear my chatter."
        show mi laugh pioneer close at center
        with dissolve
        "And what is the answer in such a situation? Yes, girl, you are a little obsessive?"
        "Or pretend that everything is fine and add another brick to the wall of lies that separates the girl from the real world?"
        me "Depends on what you want."
        me "I like the way you sound. Like a silver bell."
        me "And if your voice was to be put on music - that would be a song."
        show mi shy pioneer close at center
        with dissolve
        "I don’t have this all-destroying thirst for communication, which is inherent in any normal person, but even then, if they pull me out - those whom I have not yet completely dispersed from life - to a drinking party, and there is enough vodka…"
        "…I can talk for hours."
        "Especially if I was silent for a long time before."
        "Abundantly, noisy and annoying. Almost like Miku."
        "Perhaps on this basis, or maybe the fact is that the teenage hormonal background has finally knocked on the young body — {w}but I have felt a growing sympathy towards her."
        "Those sprouts that she sowed in my heart at our first meeting felt the sun and raised their heads."
        show mi normal pioneer close at center
        with dissolve
        mi "I don't want to be alone. Is that too much?"
        mi "I need a person who listens, speaks and understands me."
        me "Have you tried, I don't know, getting a boyfriend?"
        me "You're beautiful, talented, sociable… {w}There shouldn't be any problems."
        mi "Social gap, Semyon. Heard about it? I'm not perceived apart from a short skirt, wide sleeves and a microphone."
        show mi upset pioneer close at center
        with dissolve
        mi "Convenient if you want to hide your own feelings, but completely unsuitable for creating at least some kind of relationship."
        me "But here and now it doesn't exist."
        "I moved closer to her, so that our shoulders were almost touching."
        show mi upset pioneer close at center with dissolve
        me "Your father didn't lie to you when he said that here you can rest like you have not rested anywhere else."
        me "He just forgot to mention something - something that is natural for him as a person who grew up in the Union."
        th "And for you it remains a secret behind seven seals."
        me "The warmest memories, the most tender feelings and the best rest are impossible alone. You need someone to be by your side."
        me "Join the team, get a girlfriend or friend, start dating someone - of course that nobody would present this to you on a silver platter."
        me "You'll have to put in some effort."
        show mi serious pioneer close at center
        with dissolve
        mi "Effort? You mean that you need to go and communicate with other pioneers and - as the squad leader said - actively participate in the life of the camp?"
        me "Exactly. To become a part of the camp, you need to do it purposefully."
        show mi normal pioneer close
        with dissolve
        mi "What am I supposed to do then?"
        me "For starters - forget your previous life. {w}The camp is like a different universe."
        me "Ignore the haters."
        me "Hell, just spread out on the sand, realize that there will be no such evening and such stars anywhere else!"
        me "And let that evening in."
        "I settled down on the sand, throwing my hands behind my head and again tried to recognize at least the damn bucket of Ursa Minor."
        "And it seems that I got carried away too much, because when someone’s body stretched out next to me, and my shoulder got pulled away with the weight of a lovely head, I involuntarily shuddered.."
        show mi happy pioneer close
        with dissolve
        mi "I understand, Semochka."
        "She chirped."
        mi "Loneliness is inside, it is neither good nor bad, it just exists, and you can obey it, or you can just… Is it fine for me to be lying down on you?"
        th "What? Of course not. Get off my shoulder."
        mi "Is it fine?"
        "I winced as a strand of aquamarine hair tickled my nose."
        me "It's fine. Didn't anyone tell you that usually you shouldn't do these things!"
        mi "No."
        "Miku gave a depressingly honest answer."
        "She lifted her head and turned, looking into my eyes."
        mi "Sorry, I'll leave now."
        menu:
            "Put your head back":
                "She smiled and went back to my shoulder."
                me "It's just, you know, I don't want your judgments to be based on gratitude."
                mi "Never thought that I'd tell that to someone else."
                show mi laugh pioneer close at center with dissolve
                mi "But please shut up, okay?"
                mi "I'm peaceful and comfortable here, and you keep talking!"
                me "Comfortable?"
                "I'm terribly bony, and her skin is so delicate…"
                mi "Very."
                if persistent.mi_dj_good_jap or persistent.mi_dj_good_rf:
                    "And how could you have act differently after these words?"
                    "Bent index finger under the chin, throwing the girl back towards the seeking lips."
                    "We split the evening between us - and become one."
                    "She opened her eyes half a second after I broke contact."
                    "But kept silent."
                    "She just purred softly, tightening the hug."
            "Mhm":
                $ lp_mi -= 5
                $ karma -= 10
                $ alt_day2_mi_date = 2
                show mi sad pioneer close at center with dissolve
                "She sighed."
                mi "What's the reason for all this ranting, if you are the first one sending me off?"
                me "I didn't mean myself. Especially since we just met in the morning."
                dreamgirl "As if that matters."
                me "I just don't want any relationships right now."
                "I was spitting out bullshit, and I, myself, believe in it."
                me "It's just that there are still scars from the last one."
                mi "Unfortunate. But if you change your mind…"
                show mi normal pioneer close at center with dissolve
                me "I promise, you'll be the first to know."
    mt "Semyon! Semyon!"
    "The voice of the squad leader came from the side of the camp."
    "Overwhelmed by belated embarrassment, we synchronously sat down on the sand."
    "Silence hung over the beach."
    $ alt_day2_beach_seen = True
    scene bg ext_beach_sunset
    show mi shy pioneer close at center
    with dissolve
    pause(2)
    show mi smile pioneer close at center with dissolve
    mi "Thank you for the warm evening, Semyon, it feels as if something has changed today. And in the morning I was just sitting and thinking that for the rest of the time I would sit alone with dusty instruments."
    me "Well, it's not the last evening either."
    me "We can do it again later, if you want to."
    if alt_day2_mi_date == 2:
        mi "I will want to. But I have no certainty about you."
        show mi sad pioneer close at center with dissolve
        mi "I know this look. You're trying to be polite, but actually you're already tired of me."
        mi "I'm sorry, I didn't mean to be pushy."
        "She grabbed the tape recorder and almost ran away from the beach."
        th "Maybe I was too harsh on her."
        th "But being next to her at her peak of talkativeness is fraught with a complete removal of the brain."
    else:
        mi "Not only can, but we should!"
        "She just waved her hand."
        mi "You wouldn't mind if I considered this a date?"
        "I nodded."
        me "I think you're getting ahead of yourself there."
        mi "Me too! {w}But I need to reward myself somehow after those two weeks of suffering!"
        me "I'll try to come by tomorrow. {w}How's that for a reward?"
        "She smiled and, grabbing me by the elbow, allowed."
        show mi smile pioneer close with dissolve
        mi "Lead the way!"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_un_loki_date:
    $ alt_day2_date = 'un'
    $ counter_un_7dl = 1
    scene bg ext_house_of_un_day with dissolve
    play ambience ambience_camp_center_evening fadein 2
    "There was a very comfortable bench next to the house, forcing you to think that the house is inhabited either by someone leisurely…"
    "…or someone really popular!"
    "I chuckled at my mental gymnastics that swapped cause and effect."
    th "And in fact, well, who would have coped with a bent cast-iron bench weighing half a ton?"
    th "Just for the sake of waiting for their beloved girl, until she finally finishes powdering her nose?"
    th "Not funny."
    if not alt_day2_dv_chased:
        "In any case, I sat down on the aforementioned bench and, slowly eating the rest of the cake, began to wait."
    "It was hard to say what I was waiting for - maybe some sort of change, or maybe the moment when I finally had the courage to climb the porch and call a girl I knew for a walk «just because»."
    "In the sense of walking for the sake of walking, without masking true intentions with stupid 'camp-get-to-knows', checklists or patrolling routes."
    if alt_day2_us_escape:
        "She'll probably be, at the very least, unhappy because of my daytime pranks."
        "Especially considering the nature of spreading rumors."
        "After all, it was just a stranger who played with her, and the one who preferred her company to someone else is waiting under the door. Different things."
    elif (alt_day2_convoy == 'un'):
        "Daytime dream haunted me, and somewhere on the edge of consciousness, something had already calculated a hundred times that Lena had the most direct relation to it."
    "For a second it seemed to me that something flickered in the glass part of the door, but only for a second. It all happened too fast."
    "The sun was gradually setting, and very soon a door night light crawled out of the illuminated sector, followed by the entire balcony, along the glass part of the door…"
    "The silence, except for the background noises of the life of the surrounding forest - and consciousness had already learned to discard them - was absolute."
    scene
    $ renpy.show("bg ext_house_of_un_day", what = Desat("bg ext_house_of_un_day"))
    with dissolve
    if not alt_day2_dv_chased:
        "Finally, the cake was succesfully executed, but nothing has changed in the house."
    "Having complained a little about my bitter fate, I stuck earplugs in my ears and mindlessly flipped through the songs for about ten minutes.… Didn't want anything fast, gloomy songs didn't fit the mood. Even the already familiar rock didn't tickle my fancy."
    "I wanted something light, perhaps romantic."
    "Mindlessly jerking the navigation wheel, my fingers stumbled upon a half-forgotten melody…"
    "The melody of youth, the melody to which billions of hearts were broken - and exactly the same number were resurrected."
    "An old Chinese curse - and at the same time the greatest blessing. Wind of change."
    "I smiled warmly at the soul-warming memories, turned up the volume on my headphones, and old Klaus started talking about how he followed Moscow to Gorky Park…"
    "And I finally saw green alert guys in the window."
    "As I expected."
    stop ambience fadeout 1
    stop music fadeout 5
    $ night_time()
    $ persistent.sprite_time = "night"
    scene bg ext_house_of_un_night_7dl with dissolve
    play ambience ambience_camp_center_night fadein 1
    "Realizing that she was noticed, she gasped and hid, and I laughed softly."
    "Nothing happened for another couple of minutes, until she seemed to realize that I was not going anywhere."
    play sound sfx_open_dooor_campus_1
    show un shy pioneer
    pause(3)
    "The door creaked softly - the beauty left the palace."
    th "Finally!"
    me "Come closer, I don't bite."
    "I carefully rolled up my simple machinery and put it in my pocket, then deliberately carefully moved to the side and patted the bench next to me."
    me "As you might have figured out, you're not getting rid of me that easy."
    me "Although, you can try."
    show un serious pioneer at center with dspr
    un "What are you doing here?"
    me "Can't you see? I'm waiting."
    show un surprise pioneer with dissolve
    un "F-for m-me?!"
    "I looked around. Scratched head.{w} Looked around again."
    me "Looks like it!"
    "She looked shocked, to say the least."
    un "B-but…"
    "She looked down."
    un "W-why…"
    if (alt_day2_convoy == 'sl'):
        un "Slavya's probably waiting for you…"
    elif (alt_day2_convoy == 'dv'):
        un "Shouldn't you be with Alisa now?"
    else:
        un "Don't you have anything else to do?"
    me "But I'm here…"
    show un normal pioneer at center with dspr
    un "Yes."
    un "Now what?"
    if alt_day1_un == 4:
        me "I remember yesterday I asked you out on a walk. You don't want to?"
        un "But in the morning… We…"
        me "Out on a walk - I mean on an actual walk."
        me "Not like playing «fun starts» trying to visit every point before lunch."
        me "Anyways, I'm inviting you to an evening walk. Are you coming?"
    else:
        me "Want to take a little walk before sleeping?"
    un "O-okay… I'll be right back."
    "She disappeared into the house and returned a few seconds later - she threw a windbreaker over her shirt."
    un "You should also get dressed…"
    show un smile pioneer at center with dissolve
    un "It's chilly."
    me "It's alright."
    "I waved it off."
    me "Either way I don't have a jacket."
    show un surprise pioneer with dissolve
    un "What do you mean… At all?"
    "Should I tell her about my magical awakening?"
    if alt_day_binder != 1:
        "About my clowning near the bus?"
    "Hey, maybe she'll suddenly appreciate that?"
    me "It just so happened… that I came to camp… without anything packed."
    "I probably looked like an idiot right now. Although it does seem to be my know-how."
    show un smile3 pioneer with dissolve
    un "Let's go, you'll tell me along the way."
    play music music_7dl["take_my_hand"] fadein 4
    if (alt_day2_convoy == 'un'):
        "Now the very girl that she was in the morning suddenly surfaced in her - she cast aside all doubts and wholeheartedly trusted…"
        "Trusted who?"
        "Me?"
        "Seriously?!"
        "A man she's known for less than forty hours?"
        "If it would be me, I wouldn't even remember the name!"
    scene bg ext_houses_sunset with dissolve
    show un grin pioneer with dissolve
    "I suddenly felt very uncomfortable."
    "The game, the rules of which were clear and obvious to Lena, seemed like chaos to me."
    "You can't just trust someone like that! It's fraught, it's painful after all!"
    "And I can't even do anything. Because from this point onward, I don't belong to myself anymore."
    "I can't accept her trust because I don't know where I'll be tomorrow and what will happen to me."
    "And I can’t refuse, because I know - like who has cut himself is afraid of the blade - how devastating it is, {w}when you're told «no» in moments like these."
    me "It's as if you're taking revenge on me for something…"
    show un shocked pioneer at center with dissolve
    un "What?!"
    me "I'm saying - such an incident happened with my suitcase…"
    "Trying to get rid of painful thought, I was spitting out anything that came to my head."
    me "They confused it with an exactly same one on the station, just from a different direction. And so it went to another city."
    show un laugh pioneer
    un "What was in the other one?"
    me "Clothes! Except for a fat woman three times bigger than me. I mean, if the need arises, I could probably hide from rain under one of her raincoat blouses……"
    me "But I don't really want to."
    me "In short, I left everything as it is. I wrote the address, they promised me to return everything safe and sound within a week."
    "Lena laughed, imagining me sitting under a bush, and above me hanging a huge blue jacket the size of a tank case."
    "She shared with me and we laughed together as we slowly moved through the camp."
    "I was ready to swear that idle eyes are already watching us from the windows of the surrounding houses…"
    "…and that tomorrow there will be sideways glances in our direction. Who cares."
    me "Tell me, do you have any favorite places here?"
    show un smile2 pioneer with dissolve
    un "You mean a place where you can hide from everyone else?"
    "I nodded."
    th "Am I rushing things too much?"
    th "If she leads me into some nook and cranny and abuses me there, I will be the only one to blame."
    un "I like the island…"
    if alt_day2_us_escape:
        show un angry2 pioneer
        un "Not the one you and Ulyana tried to escape from… The other one."
        "That's some serious intelligence gathering!!!"
        me "How do you…"
        un "Know? Earth's full of rumors. About how the newcomer, without living here for a single day, decided to run away."
        "It looks like she really doesn't like this topic."
        "The only thing left to find out is where the problem lies - in the escape, or in the nuances."
        me "Sorry. I really shouldn't have run away."
        show un laugh pioneer at center with dissolve
        un "No, I don't mind doing stupid things. I just…"
        "She began to stutter, pronouncing the simplest words with difficulty."
        show un shy pioneer at center with dissolve
        un "…that it's me… and not…"
        "I felt her hand in the dark. She was already cool, and I did my best to warm her with the warmth of my own hands."
        "She shuddered again, as if I had not touched a hand, but something… intimate? Exposed nerve? Don't know…"
        me "I solemnly swear…"
        "I had to pause several times to clear my throat, catch my breath and collect my thoughts."
        "It seems that landslide shyness is somewhat contagious."
        me "…that the next time I decide to run away, swim across the river or go crazy in any other way - I will call you."
        show un smile pioneer at center
        "She smiled, apparently deciding to believe in my promise."
        me "Short one?"
        "She nodded."
        un "Closer one."
    me "Do you want to take a boat?"
    if alt_day2_us_escape:
        "My muscles groaned in protest, but I ordered them to shut up."
    un "No… Well, I do want to… But not today."
    me "Any others? Any other places where you can escape from the whole world and quietly come to your senses?"
    show un smile pioneer
    un "You said it so right…"
    "She fell silent again, biting her lower lip, obviously thinking about something intensely."
    "And I stood and waited for her verdict."
    "All my cynicism and all my callousness means nothing when the trust of a girl I hardly know becomes the measure of my own worth."
    "Can I be trusted?"
    "I know for sure that you can't. I don't trust myself and never did. Starting from trying to quit smoking, ending with that static nightmare where I drove myself into - all this is the work of my own hands."
    "But this girl was too important…"
    "I don’t know what she could see in me, and whether she saw it, or her earnest, to the point of self-denial, desire to let someone into herself is just a cry for help."
    "But I just couldn't fail her. Not now, never."
    "Finally she made up her mind and got up from the bench."
    un "Let's go. It's not far from here."
    scene bg ext_boathouse_night with dissolve
    "We went to the boat station, but Lena, instead of going to the bridges, took my hand and dragged me somewhere to the left along the coast."
    "There, about three hundred meters away, a small grove began, as if cut off by the very edge of the territory and access to the water."
    "It turned out to be a kind of arrow in which you can really hide, and no one will find you if you don’t want it yourself."
    scene bg ext_un_hideout_night_7dl with dissolve
    pause(2)
    play music music_list["confession_oboe"] fadein 5
    show un grin pioneer at center
    "We wandered along the sand at the very edge of the surf, where the flow of water had already dragged driftwood - just go, dry it out and you can burn fires."
    "Cooling water blew on the right, the breath of the camp going to sleep sounded on the left."
    "And we walked like children, holding hands, and smiled with doomed despair, and there was no turning back for us!"
    "All words lost their meaning."
    "I could no longer make out the features of her face, there was only a silhouette visible against the backlight from the boat station and the beach, but I guessed that she was also stealthily glancing in my direction."
    "Fifteen minutes - and above our heads the coniferous caps of freedom-loving southern pines are merging together, growing at random all over the area."
    "Soon we reached a clearing."
    un "Almost there."
    "Lena answered my silent question."
    "In the very middle lay three logs surrounding an old fire pit. I nodded questioningly in that direction."
    "She shook her hand."
    show un shy pioneer with dissolve
    un "N-not there… We need to go further. To water."
    "She pulled me by the hand, which she never let go until now, somewhere towards the shore."
    "There was a long hoot and squeal overhead, and she, screeching, hid behind me."
    play sound sfx_owl_far
    un "What was that?"
    "She asked stifledly."
    "And I smiled. Not evil or derisive, as one could before, having learned that one could be afraid of a simple owl."
    "It's just that this fright… Like everything Lena did… Was so cute!"
    "I carefully unhooked her whitened fingers from my shoulder."
    me "Have you never been here at night?"
    show un scared pioneer with dspr
    un "N-no…"
    "And what do I do with her?"
    "I quite seriously decided that it was her who was so fearless, took the unfamiliar young man into the night woods…"
    "And it turned out like this."
    un "I'm only here during the day…"
    un "Rarely…"
    un "When it's really, really bad…"
    "Something creaked overhead again."
    play sound sfx_owl_far
    scene cg d2_un_owlet_pioneer_7dl
    with dissolve
    "And Lena squeaked again, and hid behind me."
    dreamgirl "I don't want to serve as a prompter, but now is the best time to grab her in an armful and kiss."
    th "Shut up."
    dreamgirl "I'm serious. She is closer to you than she ever was. You don't even have to play duck and pout your lips."
    dreamgirl "You just have to turn around and…"
    "And why would I even listen to this inner fool!"
    un "Above… there's something scary? Right?"
    un "Please don't be silent… I…"
    "I wouldn't be silent, but my lips were kind of busy…"
    play music music_list["i_dont_blame_you"] fadein 1
    scene cg d2_un_kissing_7dl with dissolve
    "It all happened too fast - here we are, and she hides behind me…"
    "And here…"
    "She stood there for a few seconds, not understanding what had happened…"
    un "Mmmm…"
    th "What devil pulled me to turn around in this very moment?"
    dreamgirl "Heeey, dude! Nice! You did it!"
    "It looks like her legs gave way because I had to support her."
    "Or, maybe not…"
    "And then, quickly pushing me away, she herself took a step back."
    "Her cheeks were burning and her eyes were hostile."
    scene bg ext_un_hideout_night_7dl
    show un angry2 pioneer close
    with dissolve
    un "…"
    me "Look, I'm sorry, I…"
    me "I'm really…"
    "She stood and looked at my miserable attempts to get out."
    "Like her sinister alter ego named Alisa."
    "They take pleasure in leaving a man in the middle of a lake. And betting."
    me "I'm really sorry it turned out that way…"
    "She kept silent…"
    th "Stop lying, at least to yourself."
    me "You know… You can hate or despise me."
    me "But I lied."
    "I said it to the top of her head, because she, and so barely visible, stood with her head down."
    me "I don't know why one has to lie about things like these… Force of habit. Or that's how it is in normal society…"
    "I took in more air into my chest and, as if rushing down a hill, blurted out:"
    me "I regret nothing!"
    show un shy pioneer close
    "Now she'll be gone and will never speak to me again…"
    "Hell, she'll just hate me!"
    show un cry_smile pioneer close with dspr
    "She looked up, and this combination of tears and a smile was so touching that I, without any hesitation, took a step forward, hugging her."
    un "Say it again…"
    me "I regret nothing…"
    "And already being on my chest, she turned a little, and then bit me on the chin…"
    "And sighing in disappointment at my stupidity, she put her hand on the top of my head and pulled me to her."
    stop ambience fadeout 1
    scene cg d2_un_knees_7dl with dissolve
    me "The stars here… It's like a huge telescope above."
    "I was lying on a warm moss pillow, with my head on Lena's knees, and she, more so mechanically, rustled my hair with her fingers."
    un "Yeah. You won't see this in big cities…"
    "She's speaking as if she's not… By the way, where was she from?"
    me "You haven't told me anything about yourself yet."
    "She smiled."
    un "Then ask… I don't know what to tell you. Maybe if you ask questions…"
    me "Then tell me where you are from."
    un "Well… I'm from a small town of a hundred thousand people not far from here."
    un "I study at school, next year I plan to apply to the local Polytechnic University. Yeah…"
    "For some reason, the ear was suddenly very hurt by this 'polytechnic'."
    me "Hold on… What do you mean «Polytechnic»? Why?"
    "She shrugged."
    un "Gotta get an education."
    me "What about the education?!{w} I'm talking about your calling."
    "Lena looked inquiringly in my direction, and I hurried to explain."
    me "You love drawing."
    if ('library' in list_voyage_7dl):
        me "And, judging by the fact that you work in the wall newspaper, you draw well."
    else:
        me "And judging by what the squad leader says about you, you draw very well."
    "For some reason, it seemed very important to me that at least this girl did not waste this mediocrely given to her chance."
    un "Yes, but…"
    me "Don't bury your talent. {w}Apply to art, let them help you learn."
    un "But I'm not an artist…"
    "Lena weakly argued."
    un "I'm just… A drawer…"
    me "That doesn't matter. The main thing is that you are taught to do what you like and what you can do."
    th "O God Almighty, give her more lenient judges, an easier task and a simpler test!"
    me "Humanity will lose more if you work as a seamstress or a cook. After all, the best paintings are those that have not yet been painted."
    un "You talk like our classroom teacher."
    "She laughed."
    th "I speak as someone who had the same dream stolen."
    th "Perhaps now my destiny is to help you find yours."
    "The sweetest dream, the rosiest fantasy is to return to the years of childhood and youth, retaining all the experience and knowledge."
    "How would you act in this or that situation compared to who you have become?"
    "If you knew the consequences, what choice would you make?"
    "I opened my eyes and looked up into Lena's eyes from the bottom up."
    me "Just because I believe in you."
    scene bg ext_path_night
    show un smile pioneer close
    with dissolve
    "We were silent for a while, enjoying the warm summer night."
    show un shy pioneer with dspr
    "Upstairs, someone tossed and turned and hooted a few more times, but now Lena knew that I could protect her in case of anything, and she no longer shuddered."
    play sound sfx_owl_far
    "And I myself reveled in this role - a defender, a person behind whose broad back you can hide what is close and dear."
    show un surprise pioneer with dspr
    me "Close and dear…"
    un "What?"
    me "Well, we've been here a while… Let's start heading back."
    th "Otherwise we risk spending the night here."
    "Judging by what the girl's eyes said, this prospect did not frighten her."
    "Well, in a pair of two headless idiots, there must be one who will take care of both."
    me "Let's go. The last thing we need is catching a cold here."
    show un grin pioneer with dissolve
    "She reluctantly let go of my hand."
    un "What about…"
    me "Tomorrow. Day after tomorrow. Anytime. We have it now - our whole life!"
    "I could not stand it and burst out laughing from the ringing delight that overwhelmed me."
    "And she, as if understanding, walked beside, smiling mysteriously with her eyes alone."
    "This wasn't love yet. Not even romance."
    "It was someone who had the courage to say the right words in the right place."
    scene bg ext_house_of_un_night_7dl with dissolve2
    show un smile2 pioneer close
    "We went straight to her house, and stood for a long, long time, saying goodbyes."
    me "Will we meet tomorrow?"
    un "Yes…"
    me "I'll miss you."
    un "Me too…"
    hide un with dissolve
    stop music fadeout 3
    play sound sfx_owl_far
    "I stood for a while and, turning around, wandered towards home…"
    "Behind me, there was a clatter of heels on the steps, and I was hugged and kissed again."
    show un grin pioneer close
    un "Now, definitely, goodbye."
    hide un with dissolve
    "Lena ran away to the house, utterly pleased, leaving me alone with my road in the dark and thoughts on the topic - did I do everything right."
    stop music fadeout 3
    stop ambience fadeout 6
    return

label alt_day2_un_herc_date:
    $ alt_day2_date = 'un'
    $ counter_un_7dl = 1
    scene bg ext_house_of_un_day with dissolve
    "Night, street, lamp, pharmacy?"
    "In this new reimagining it sounded like «Cake, music, your house, bench»."
    "Opposite of Lena's house, I looked at a bench, as if transferred here from a city park."
    "Bent back, white paint, looks to weigh half a ton."
    "I don't even want to think about how they put it here. However, that's not what I'm here for."
    if ('nwsppr' in list_clubs_7dl) and (alt_day1_un == 4):
        "I remember that someone promised me something in exchange for my consent to work in a wall newspaper."
    elif alt_day1_un == 4:
        "I remember that someone was talking about some kind of joint activity. Given my idiocy, it's hard to imagine how I can be used for painting…"
        "Hmmm… As an easel mover?"
        "I definitely don't look like a model."
    "I didn't really hide when I followed Lena after dinner. She didn't go anywhere else, so now she's here."
    "I know that. {w}And she knows that I know. So on and so forth."
    "Brushing a few needles and a stray pinecone off the bench with my hand, I sat down and began to wait."
    if (alt_my_rival_1_tour.take == 'un') and (alt_day2_gamblers_result['me'] == 1):
        "It's possible she's mad at me for that game."
        "Or maybe not."
        "It seemed that she understood my motives."
        "And if she didn't…"
    elif (alt_my_rival_1_tour.take == 'un') and (alt_day2_gamblers_result['me'] >= 2):
        "I don’t know if she was offended by me for knocking her out of the tournament in the first round."
        "Or maybe she doesn't care. So far, she has shown either fear or embarrassment."
        "Some kind of obvious interest… Personally, I didn't see any."
    "I forbade myself to think about the bad."
    th "Maybe she was completely delighted, and now she is grateful to me - look how uncomfortable she was under the crosshairs of the views of the audience. Fear of the crowd as it is."
    if not alt_day2_dv_chased:
        "There was no more cake."
        "I looked at the napkin with regret, but there really was nothing else there."
        "Well, that means there are more reasons to hate Ulyana!"
    "The evening was warm and somehow peaceful, I threw my head on the headboard and stared at the evening sky."
    "So peaceful…"
    "Another fifteen minutes later, my patience snapped, and I got up from the bench."
    "Approaching the house, I climbed onto the porch and knocked softly."
    play sound sfx_knock_door3_dull
    scene bg ext_house_of_un_night_7dl with dissolve
    "No response."
    "I knocked again and, pushing the door, went in."
    stop ambience fadeout 1
    stop music fadeout 2
    play sound sfx_door_squeak_light
    scene bg int_house_of_un_night
    with fade2
    play ambience ambience_int_cabin_night fadein 3
    $ night_time()
    $ persistent.sprite_time = "night"
    play music music_list["confession_oboe"] fadein 3
    "Lena sat at the table and thoughtfully looked out the window."
    "She did not react at all to my knock, as if she was completely lost in her thoughts."
    me "Hey… Why are you alone in the darkness…?"
    show un scared pioneer with dissolve
    un "AH!"
    "She almost jumped out of her chair in surprise!"
    show un shy pioneer with dspr
    "And then suddenly she began to fuss, stir, shifting something on the table…"
    "I barely had time to see how, with an imperceptible movement, she hid something lying under her elbow between books, covering it with a box of paints lying here on top."
    me "Sorry, I didn't mean to scare you…"
    show un smile pioneer with dspr
    un "I-It's okay…"
    me "It's just that you're not coming out… Sitting here alone…"
    "I started, feeling either like a salesman, or just a jerk. Dvachevskaya was right in calling me a retard."
    me "So I thought…"
    "I stumbled looking for new words."
    me "This is wrong! Sitting alone on a night like this…"
    show un serious pioneer with dspr
    un "What do you mean?"
    if alt_day1_un == 4:
        me "Yesterday you told me that you like drawing…"
        me "And you also said you were ready to take the risk of doing it in my company."
        "Cheekbones cramped from the ambiguity of what was said, but it was too late to take it back."
        "Fortunately, the girl did not seem to notice this, as she did not react at all."
    else:
        me "You draw for the newspaper… That means you draw well?"
        show un smile pioneer with dspr
        un "W-well… I just draw."
        me "Already better than me."
    me "So, for tonight, I would like to ask you to…"
    "I paused."
    me "Show me your paintings."
    if ('library' in list_voyage_7dl):
        extend " I see paint here, there's an easel in the library… That means there is something to show, you do not draw stick men in a notebook with a pen after all…"
    else:
        extend " Olga Dmitrievna spoke of you as a very talented artist."
    "She calmly and sternly looked at me, waiting for the continuation."
    "And I suddenly realized that once again I was imposing on her. In such a situation, I would have already sent myself far and for a long time, but Lena turned out to have a much more solid reserve of patience, since she still hasn’t kicked me out."
    "And before I had time to move away from this thought and rush to apologize for my own annoyance, the next one flew after the first thought:"
    dreamgirl "For a good artist, each of his paintings is a personal experience. He lives the plot, draws conclusions, and then expresses everything on the canvas."
    dreamgirl "And let me ask you, why the hell are you climbing not just deep, but into the very depths of her heart?"
    dreamgirl "Did you earn this right?"
    dreamgirl "Or maybe the world doesn't suit you?"
    dreamgirl "She just started to open up and trust you… And you ruined everything. You dumb shit."
    dreamgirl "Would you also like to read her diary?"
    show un surprise pioneer with dspr
    un "What paintings? I just…"
    "She waved."
    un "It's all bad."
    "It was evident that the topic of conversation was painful for her."
    "Has anyone already looked at her drawings and criticized them to the nine hells? Well, it's an everyday thing, without criticism progress goes much slower."
    stop music fadeout 2
    "Alright, I need to urgently think of something before she closes up again!!!"
    me "Lena…"
    play music music_7dl["take_my_hand"] fadein 1
    "I tried to speak as softly as I could."
    me "That's not true…"
    if ('library' in list_voyage_7dl):
        me "I saw in the library, on the table… {w=.4}Your illustrations."
        me "Those were yours, right?"
        show un shy pioneer with dspr
        un "Yes…"
    else:
        me "And the squad leader praises you out loud, and - you will be surprised - Ulyanka."
        dreamgirl "Uh-huh. Ulyana wouldn't say shit."
        un "I don't know…"
    "She whispered."
    "Right now she looked like a personification of doubt."
    "And I perfectly understood her!"
    show un normal pioneer with fade
    "And I also understood very well that if I don’t chat her up now, I will not only never chat her up…"
    "I will also lose that little progress in our incomprehensible relationship with her."
    "And it is unlikely that she will ever let me close after that."
    th "Now we need to ask her as convincingly as possible not to be stubborn. While there is still a possibility."
    th "Or show mercy and move to another topic?"
    "To hell with that mercy."
    me "Listen… I understand that this is very personal. And if you don't want to share it with me, I'll understand too."
    me "Anyway, I'll try to respect your decision."
    me "But please understand: if you are an artist, you must exhibit yourself."
    me "Your works should be seen by people! All the feelings that you put into the pictures should be seen, appreciated and felt."
    me "I mean, don't bury talent in the ground. If you want to be an artist, be one. But then be it to the end."
    "Pathetic speech… Whom did I hope to convince with such proclamations…"
    show un serious pioneer close at center with dissolve
    un "What you're saying… It's so weird."
    "She thought hard and tried to find some counterarguments. Moreover, in the end she found them, and…"
    show un smile pioneer far with dissolve
    un "But you may be right."
    "…and mercifully kept them to herself."
    th "You're a saint…"
    "She put aside the book, under which a kind of sled-holder for sheets of whatman paper, laid with paints down, was found."
    un "Here… My art."
    "She turned over the first sheet and I gasped, closing my eyes."
    "My city was looking at me from a piece of paper. Snow-covered, gray and dull, for some reason it looked beautiful, coming out from under the girl's brush."
    "Does this mean that it was beautiful, I just didn't see it?"
    un "I just called it a city. Because I didn't come up with a name."
    "She helplessly shrugged."
    un "I just dreamt of it one day…"
    me "Fantastic…"
    "Advertising banners, 6x3 billboards, modern design trolleybuses, and…"
    "A light is on in one of the windows. But not a simple Soviet light bulb, but a dead blue light from the monitor, much more familiar and dear to the heart of any user."
    un "Yeah, it's a little fantastic… But I have the same view from my window…"
    me "I'd love to see it."
    show un surprise pioneer with dspr
    un "What?"
    me "The view… From your window."
    un "W-why?"
    show un shy pioneer with dspr
    "She seemed to have some pretty interesting thoughts in her head."
    me "Just because… Can't I?"
    un "You can… Maybe."
    "How else would you start dating a girl, if not from the view from her windows."
    "I felt uncomfortable. Doubly embarrassing because the owner of the house was also embarrassed."
    me "Sorry… I'm rambling again… Let's keep looking?"
    un "Let's…"
    play sound sfx_paper_bag
    "Putting the first painting aside, she flipped the next."
    "The camp was drawn here. But the angle…"
    "As if she was drawing on a boat."
    if alt_day2_us_escape:
        "Or from the very island where Ulyana and I tried to escape."
    "If there's one thing I knew about painting, it's that it requires certain calm."
    "Otherwise, why all these easels with tablets, if you could take and draw a picture on the go, not paying attention to the environment."
    un "Pier…"
    me "Yeah, I see. Is that your favorite place?"
    show un shy pioneer with dspr
    un "Not really…"
    "She got embarrassed, and I scolded myself once again."
    dreamgirl "Get a grip!"
    dreamgirl "Keep this in your empty head - you're treading on VERY thin ice."
    dreamgirl "And all your insignificant life experience will not help you here."
    dreamgirl "Because it's all completely different."
    "I'll need to write down a list of «forbidden» topics, which should not be brought up when talking to this girl."
    me "How did you draw it? Don't tell me you were on a boat?"
    un "No… I just saw this moment… And remembered."
    un "And then I drew it… From memory."
    me "You have an amazing memory!"
    "And as if I said something wrong, Lena turned and looked at me strangely."
    show un surprise pioneer with dspr
    un "Why amazing?"
    me "Memorizing the picture in every detail… I'm sure I'll go to the pier tomorrow and find every mooring ring, boat with a number, or window with cracked glass."
    "I have always been fascinated by creative people. No, I didn’t envy them, I wasn’t angry that God gave to them, but cheated on me. No. It's just that when someone does something well, I'm happy for them."
    "How happy I was now for Lena, seeing how she manages to express a thought, feeling, emotion."
    if  alt_day2_bf == 'un':
        show un shy pioneer with dspr
        un "You're looking so strangely now…"
        un "Like back on breakfast…"
    un "I told you they were ugly…"
    "And here the obvious fact reached my limited mind."
    "She needs a praise! Some kind of compliment…"
    th "It looks like the girl was not praised as a child."
    "And I don't mind praising her. Considering it's all true."
    me "Such nonsense. Listen to her, 'ugly'."
    me "I'd take half of those with me back home…"
    un "And the other half?"
    show un smile pioneer with dspr
    "She smiled slyly, and the smile literally transformed her sad face, filling it with some kind of inner light."
    me "I wouldn't take the other half."
    un "Why is that?"
    me "Because it would be selfish to take everything for yourself… People also need to admire something."
    un "You say it like…"
    "Whatman crunched softly under clenched fingers."
    "It seems that she again withdrew into herself, and I had to release the crippled canvases, gently and politely unbending her fingers."
    "Or at least try to…"
    "When our fingers touched we both flinched."
    "It suddenly occurred to me that this was our first contact. Peculiar achievement."
    "It also occurred to me that now we are all alone with her, sitting in a house, sitting close…"
    "I blushed and tried to sit farther as discreetly as possible. At least a little further."
    "But where do you move on a stool?"
    show un normal pioneer with dspr
    un "Something wrong?"
    "She looked at me carefully."
    "And the damn prompter clicked in my head again, saying that the distance to the girl’s lips did not exceed ten centimeters."
    me "E-everything… i-is fine…"
    if (alt_day2_convoy == 'un') and ('library' in list_voyage_7dl):
        "As then in the library, I felt her breath on my skin, I could feel the taste and smell."
        "The only question is, am I in too much of a hurry?"
    elif (alt_day2_convoy == 'me'):
        un "It's unfortunate that you didn't ask me to accompany you in the morning."
        "She said hoarsely."
        me "W-why?"
        "Thoughts rushed about, not giving out a single reasonable idea about how to behave correctly in this situation."
        show un smile pioneer with dspr
        un "Well… We could've walked."
    elif alt_day2_convoy in ('dv', 'sl'):
        stop music fadeout 0
        if (alt_day2_convoy == 'sl'):
            un "Tell me, why do you pay so much attention to me?"
            me "Because I'm interested in you…"
            un "But what about Slavya? I don't want to be the second stool in the house."
            me "Slavya… Slavya is just a good person. She was the first to show me kindness in a long time."
            me "I'm grateful to her for this, but this gratefulness… It's different."
        elif (alt_day2_convoy == 'dv'):
            un "You know… Me and Alisa, we grew up together."
            "I nodded my head in confusion, not understanding where she was getting at."
            un "You could say she was my first and best friend."
            me "Then what happened at the canteen?"
            show un serious pioneer close with dspr
            un "You don't get it. This is our personal etiquette, just between me and her.."
            me "Alright, I got it. She's your best friend. So?"
        un "In the morning you spend time with her… And then you run to me…"
        un "I want to know…"
        "Her voice got quieter and quieter until it was almost a whisper."
        un "Why do you do this?"
        un "Does communication with a taciturn girl mean so much to you?"
        "And how should I answer? Joking in the spirit of sitcoms, like, I'm friendly and can be friends with everyone? Yes, it will be a great end to the evening… Just my style."
        me "Yeah… It means that much."
        play music music_list["doomed_to_be_defeated"] fadein 0
        show un angry pioneer close with dspr
        un "Then go to her! {w}And I promise you a daily ration of communication in three words!"
        me "N-no… you don't understand… I wanted…"
        un "I {w=.3}don't {w=.3}care — what you wanted. Get out!"
        show un angry pioneer far with dspr
        "She jumped up from the stool and, going to the entrance, flung open the door."
        "As if she waited for something and made an inviting gesture."
        un "Come on! I'm waiting! Don't forget your th…"
        $ alt_day2_date = 'un_fz'
        dreamgirl "You once again confirm your reputation, Semyon Semenych."
        "Not daring to raise my head, I walked past Lena, literally feeling her eyes accompany me with open hostility."
        hide un with dissolve
        play sound sfx_open_door_kick
        "Hey guys, guess that's it."
        scene bg ext_house_of_un_night_7dl with dissolve2
        "I thought I heard a sob behind the rumble of a slamming door?"
        "…"
        with fade2
        "…"
        "However, this is none of my business. She showed me the door and I found it."
        "I should go to sleep before I mess something up."
        $ lp_un -= 10
        stop music fadeout 3
        stop ambience fadeout 6
        with fade
        return
    "It seems that it was possible to light a cigarette from my cheeks at that moment."
    "It suddenly occurred to me that Dr. Collider, with her magnificent forms, the manners of a burnt nymphomaniac and her cleavage to the navel, does not even stand close to this modest girl."
    me "It's late…"
    show un smile pioneer with dspr
    un "Yeah…"
    me "So, see you tomorrow?"
    "She glanced at her watch and laughed."
    un "See you today."
    "I reluctantly let go of her hand and wandered towards my house."
    stop music fadeout 3
    stop ambience fadeout 6
    return

label alt_day2_slot_un:
    $ alt_day2_date = 'un'
    $ counter_un_7dl = 1
    scene bg ext_playground_sunset_7dl with dissolve
    "In search of solitude, I wandered into the sports field."
    "It's been occupied all day with pioneers dusting the field, kicking the ball."
    "Now, when they were all still sitting in the canteen and absorbing those remains of the cake that Ulyana did not reach, it was absolutely empty and deserted here."
    th "That's the ticket!"
    "If I'm not confusing anything, all the sports fields are usually built on the outskirts, so the chance that the pioneers would be too lazy to get here in the evening was quite high."
    "And today a shitton of things has already happened."
    "For example, the entire show with Ulyana."
    "Tournament, that damned checklist…"
    "I carefully examined the gate and, climbing up the net, took a place on the crossbar."
    "And after a little thought, I completely settled down on a sagging net, finding myself in an impromptu hammock."
    "If you don't make any sudden movements, you could probably lay down here comfortably."
    scene bg ext_sky_7dl
    with dissolve
    stop music fadeout 8
    "And look at the sky, for example. In the absence of flowing water, the sky is not the worst object for meditation."
    "A blade of grass in the teeth, the mood is peaceful, the evening is bright. Now, if everyone leaves me alone, I might even be able to have a modicum of pleasure."
    "I had to smooth out perturbations in my psyche, {w=.4}which would be impossible in someone else's company."
    scene stars
    with dissolve2
    play music music_7dl["take_my_hand"] fadein 4
    "And then the stars peeped through the clouds as the sunset dragged the opaque blue dome behind it, exposing the black and blue inside, pinned with icy needles above the head."
    "What can be seen on the monitor screen or in another Hollywood craft will never compare with the real sky."
    "Because the real sky is alive."
    "And, like any other ideal interlocutor, it is unobtrusive."
    stop ambience fadeout 1
    $ night_time()
    $ persistent.sprite_time = "night"
    play ambience ambience_camp_center_night fadein 1
    "I tossed and turned in my hammock, trying to find familiar constellations."
    "I may not be the best astronomer in the world, but such noticeable things as the bucket of Ursa Minor, I would definitely know."
    "But it wasn't here. Or did the sky distort beyond recognition because of our southern latitude?"
    th "Or maybe I'm just stupid?"
    "Maybe I'm in the southern hemisphere? There, they say, the picture of the sky is completely different."
    "I threw my hands behind my head and stretched sweetly."
    "And my peripheral vision caught a new character."
    "I'm not alone, again?"
    "Should've expected that."
    "It was foolish to escape to some dark corner, considering I was constantly bothered by someone all day."
    "From top to bottom, the silhouette was difficult to read, but it was safe to say that he was not very tall."
    "And the proportions revealed that it was a girl."
    "She was standing at some angle to me, so I couldn't see clearly."
    "It took a long time to see the racket either, and I was surprised - playing in the dark like this? Isn't it scary to lose all the shuttlecocks?"
    "Although it seems that there was no need to fear this at all - during the swing, the girl constantly turned the racket at some intricate angle, due to which the blow fell casually."
    "The shuttlecock, of course, fell, and she, of course, stooped to pick it up. And each such tilt four ponytails jumped funny in the air…"
    "Lena. She's the only one here with hair like that."
    show blink
    "I was glad that I had taken a convenient observation point - no one sees me, but I see everything and, closing my eyes, tried to pretend to be a rag."
    "And in the air there were sounds of plastic hitting plastic."
    "Not a slap of an elastic mesh on a shuttlecock, but a plastic knock."
    scene stars
    show unblink
    "I tried to turn off the sounds and looked at the sky."
    "But the sky betrayed me. It was no longer open and alive - the way it is only when you are alone with it. Or together with a dear person."
    "And the irritation factor continued raping shuttlecock."
    "Hit."
    "Tilt."
    "Straighten."
    "Another hit."
    "I can't watch this!"
    scene bg ext_playground_night with dissolve2
    "I was trying to get out of the net in order to take away the unfortunate racket with a shuttlecock from the girl and yeet it somewhere far away."
    "But I didn’t take into account the fact that I was lying on a loose net on top of a football goal."
    "The net closed around me and rushed down!"
    "I didn't even have the time to get scared."
    "And my trap caught on something halfway, shaking me out and burying any hopes for a soft landing."
    play sound sfx_bodyfall_1
    with vpunch
    show un surprise sport with dissolve
    me "…mother… and his mother… and foremost those who didn't fix everything in place!"
    "I'm done, gentlemen of the jury."
    "I uttered the whole tirade from the ground, without even trying to get up."
    "Lena, with her jaw dropped, watched the fall of Semyon and, as if out of solidarity, a racket fell out of her hand."
    "The shuttlecock thrown up before my fall overcame the top point and rushed down."
    "No one paid attention to him, so he fell down next to the racket, damned he be."
    "And we formed a touching triumvirate on the fine reddish gravel of the football field - me, racket, shuttlecock."
    "The cover here is certainly not lawn. Well, at least it's not asphalt, for that matter."
    "Therefore, I did not receive any serious injuries, aside from my once again wounded pride."
    "I looked up and met the eyes of a girl."
    me "Lena? Oh. You heard all of it?"
    "Stupid question."
    "She stood in a dumb daze and I had to get up on my own."
    "And then, as if wanting to also witness my fall, the moon climbed into the sky."
    "The deadly pale light illuminated both my rumpled face and scratched fingers - and Lena."
    show un smile sport with dissolve
    "And either the reflection lay down that way, or something else - but I suddenly stared!"
    "Like a museum visitor I stood and stared… {w}Drowning in her eyes. And there definitely was something to drown in."
    "Her pupil occupied more than half of the iris - a reaction that any physiognomist can easily recognize as interest."
    "The reaction that delights lovers all the time."
    "And then - like a nesting doll: under a lively, but well-camouflaged interest, fear is hidden, under it are some experiences, the names of which I can’t find yet."
    "I'll find them, just give me time!"
    "I rewound my thoughts. Didn't someone say something about being scared?"
    th "I scared her!"
    "Well done, Semyon, you know better than anyone how to start a conversation with a girl."
    "We stood like that for a few seconds while I got up."
    me "Good nightning."
    "As courteously as possible I said."
    "You gotta start somewhere."
    me "Sorry for that tirade - things went a little worse than expected."
    me "Ghuh…"
    "Throat ached from dust in the throat."
    me "I was looking at the stars, and here you were…"
    dreamgirl "Ah yes, the epitome of eloquence."
    th "I did all I could!"
    me "And the net wasn't properly attached there. So, here we are…"
    "I tried to dust myself off, but it seems to no avail."
    show un normal sport far with dissolve
    "Lena nodded and took a step back, instantly hiding what I managed to read in a split second of eye contact behind a mask of shyness."
    th "She doesn't seem to be very happy with me."
    th "We are now in the same position of people whose privacy has been violated. Isn't it time to cooperate?"
    me "Look, Lena…"
    me "If you keep twisting your arm like this, you will never hit properly."
    me "And you'll break the shuttlecock."
    "Well, yes, if you hit a thing for a long time, it will break - a proven fact!"
    me "Just keep your hand steady, the racket is big, you won't miss!"
    "An abstract topic for conversation is what you need to make your counterpart relax."
    me "Let me show you."
    "I held out my hand, still afraid in my heart that Lena would misunderstand the gesture."
    th "In the end, if she starts hitting correctly, the noise from her will be exactly three times less, and I can return back to the hammock."
    "I glanced at the net, which swayed in a shapeless sack under the crossbar."
    th "Or… I won't be able to!"
    show un shy sport with dissolve
    un "Here. Just don't hit too hard, okay?"
    th "It seems in this situation she feels a little more confident than me?"
    "In any case, the fright from her eyes evaporated, leaving some other emotion in place. {w}I had a hard time figuring out which one. Moonlight took its toll, making familiar things unfamiliar and mysterious."
    "She picked up the racket along with the shuttlecock from the ground and handed it to me."
    "A racket with a hard plastic mesh - cheap children's toy. And a plastic shuttlecock to match her."
    th "Well, that shouldn't be hard."
    "I lowered my right hand with the racket clamped in it down and threw the shuttlecock in front of my face."
    "Waited for a bit."
    play sound sfx_tennis_serve_1
    "Strike!" with vpunch
    "The trajectory turned out to be quite nice!"
    "Both of us, with our mouths open, followed the flight."
    "Shuttlecock flew up about fifteen meters, reached the peak and, turning around, rushed down."
    "Of course, I didn’t hit perfectly, there was a certain difference, but there’s nothing to worry about, the error margin is a meter or two."
    "Unless it gets blown away by the wind."
    "And I belatedly remembered why I don't like this game at all!"
    "As soon as I thought about the wind, a gust came from nowhere and dragged the shuttlecock straight into the thicket!"
    show un sad sport with dspr
    "Lena stood with such a look that my conscience, rising from the ashes, attacked me."
    un "Oh well…"
    "It looks like she was seriously worried about some kind of shuttlecock."
    un "Boris Alexandrovich will scold me now…"
    un "And they won't accept me into team…"
    "Was she blaming herself for my mistake? Without even thinking about complaining to me?"
    me "No, he won't scold you! I'll go get it right now."
    "I’ll probably see a white shuttlecock against the background of black thickets, right?"
    stop music fadeout 4
    me "Wait here."
    "And already figuring out the search space in my mind, scattering it into squares, I headed towards the bushes."
    show un scared sport with dspr
    un "W-wait…"
    "Lena caught up with me and hesitantly touched my hand."
    me "What? Why?"
    un "There…"
    play music music_list["orchid"] fadein 4
    "Lena stuttered and looked away, noticeably turning pale."
    "Whatever she wanted to talk about, it frightened her clearly more than the pioneer who fell from above under her feet."
    un "THAT is there. The thing."
    "She whispered it in such a scared tone."
    "And I suddenly wanted to just hug this child and pat her on the head consolingly, hide her on my chest, where she would no longer be afraid of anything."
    me "THAT?"
    "I remember one «Thing»  — but the climate here should be too hot for it."
    me "Afraid of the dark?"
    "Lena shook her head silently. Yeah, what am I saying - she was here playing badminton alone, as she thought, on the field!"
    me "Stay here, don't go anywhere. I'll be right back."
    me "Okay?"
    "I smiled, trying to cheer up the girl, but it seemed that I was the one who needed to be encouraged."
    me "Wait for me."
    "The thing? That."
    "Wow, how two well-chosen words add to the atmosphere!"
    "I felt like Isaac Clarke heading for the bowels of «USG Ishimura»."
    "Or at least like Ellen Ripley, if you don't like videogames."
    "It seems that Lena realized that I would not refuse the idea of ​​going into the woods."
    "She thought for a bit."
    show un normal sport with dspr
    "And then she made up her mind and took my hand."
    un "Let's go together?"
    "Now it was my turn to be surprised."
    me "But there, you, uhh…"
    show un sad sport with dspr
    "She shrugged her shoulders and looked at me pleadingly. She didn't seem to want to be alone anymore."
    "Oh well, we're going together then."
    stop ambience fadeout 1
    scene bg ext_path_night with fade
    play ambience ambience_forest_night fadein 1
    "She kept a little behind, squeezing my hand with all her strength."
    "I had to grimace and endure. The girl showed trust, and trust must be justified."
    th "I hope it didn’t fall into some hole or hollow, or we'll be here all night."
    me "Why are you here so late at night?"
    "I decided to distract both of us with a conversation, since I, too, was already palpably uncomfortable."
    "Whatever «THAT» was — it definitely scared the shit out of Lena!"
    show un smile sport with dissolve
    "She smiled slightly."
    if (alt_day2_gamblers_result['me'] == 22) and (alt_my_rival_1_tour.take == 'un'):
        un "Well… Today I was lucky in cards. I thought I'd be lucky in badminton too."
    elif (alt_day2_gamblers_result['un'] in [2,11]):
        un "Well… I did make it to semi-finals today."
        un "So I thought - maybe I'll get lucky somewhere else?"
    elif alt_day2_gamblers_result['un'] >= 21:
        un "I got pretty far in the tournament."
        un "So I decided that today I will definitely succeed."
    show un sad sport with dspr
    un "I really want to get into the team, but Boris Sanich says that until I learn how to hit the shuttlecock…"
    $ meet('ba','Boris Sanich')
    "She sighed."
    me "I see…"
    show un normal sport with dspr
    "During the conversation we didn't notice how deep we went into the forest."
    "Despite that, I was leading us in the right direction."
    "Soon something white appeared against the background of dense dark greenery."
    "Shuttlecock!"
    "I reached out my hand and…"
    play sound sfx_owl_far
    show un surprise sport with dspr
    "Vshhhh!"
    un "EEEEEEEEEEEEEEEEEEEEEEE!!!!"
    scene cg d2_sovenok with dissolve
    "Yes! That's it! THAT!"
    "I flinched in surprise."
    un "It's THAT!"
    "That?!"
    "I looked around, half for cover, half trying to see the threat."
    "But Lena got ahead of me - she hid behind my back and clung to me with all her might."
    "I'm not sure, but it looked like she was there crying out of fear. In any case, I absolutely heard sobs."
    "And how significant was that she did not rush away with a screech, running in terror."
    "But she hid behind me!"
    "For me that's a fairly visible gesture of girl's predisposition towards me."
    "But uh, what am I supposed to do?"
    dreamgirl "She trusts you with her own safety, what more do you want? Grab her, she's all yours."
    th "Someone's yelling from the bushes, and you keep talking about women!"
    dreamgirl "They'll yell and stop. And Lena will now peel off from you, and…"
    "My eyes tingled from a feeling that I would find it difficult to define - there was something from tenderness, care, and from an incomprehensible pride in trust."
    if ('sport_area' in list_voyage_7dl):
        "This girl achieved what the teacher-bear could not achieve - she made me feel like someone strong."
        dreamgirl "Or wide enough, that also works."
    "A feeling that so far I have managed to experience a few times - and in all cases I had to test myself for strength."
    "A feeling of being needed."
    "And what was happening between me and Lena - in the face of danger…"
    "It was something more than the fear of a child hiding behind someone bigger. It was…"
    "…here the thought stopped - there was a reason why."
    play sound sfx_owl_far
    "There was a distinct gurgle above my head, and I looked up to see."
    stop music fadeout 3
    "Owl. Small, brown owl with a grumpy expression on its muzzle. An owlet, even."
    "That's who was yelling here! How does such a voice fit in such a small body?!"
    "It seemed to me that the hugging couldn't get any tighter, but Lena showed me new horizons, climbing almost under my shirt."
    th "A little closer and we'll both fall."
    th "I mean, I don't mind it, but…"
    "I ordered all my internal cockroaches, voices and other population of the head to shut up."
    "I felt with my back, which suddenly acquired a tactile sensitivity comparable to fingers, all the elastic girlish topology pressed between my shoulder blades."
    "The body grumbled and licked its lips, waking up."
    "A sweet scent wafted up to me from her hair."
    "And painfully I wanted to turn around and hug her, cuddle her up, swear that now everything will be fine, and I will be able to protect her from all the dangers that exist.…"
    "Almost to tears."
    "I bit my lip."
    play music music_7dl["take_my_hand"] fadein 4
    "I suddenly remembered a movie that I've seen a long time ago. More precisely, not the film itself, but a phrase from there."
    "A person, a healthy person, is selfish and incapable of inflicting pain on himself - limiters would interfere. Just for fun, try to bite yourself until you bleed."
    "And the final scene, where the hero stands with a bitten hand, and blood flows down his fingers."
    "And the salty trickle that splashed on my tongue, I didn’t even recognize at first as blood."
    "I managed to bite myself hard enough to bleed."
    "And I didn't feel like I was going crazy."
    th "But why can't I turn back now?!"
    "After all, I want it. I know it. And I’m ready to bet my salary for this entire year - she won’t repel me."
    "Because hiding on someone's chest is always safer than looking out from behind. It's a subconscious reaction."
    "Finally I managed to overcome the stupor and turn around."
    scene bg ext_path_night
    show un shy sport close
    with dissolve
    "Her lips were within ten centimeters away. Her breath was fresh."
    "I don’t know what she wanted, to push me away or to jump away herself, but it turned out to be something opposite - she just sagged on my hands, which were placed in time."
    play sound sfx_owl_far
    "And the owl hooted again!"
    "No longer thinking about running away, she clung to the only unshakable thing - me."
    show un scared sport close with dspr
    "At the same time, out of fear, completely unaware of what she was doing, she slashed on my forearm with her nails."
    un "THAT!"
    un "The thing!"
    me "Is that your thing?"
    "I inquired in a businesslike voice."
    me "I think we can handle this thing. Or at least let's try."
    "She hid her face in my shoulder."
    "I don’t know where this indescribable fear came from in her, but I had to spend another five minutes stroking, supporting and exhorting."
    me "Look for yourself, it's not a thing, it's just an owl!"
    un "Owl?"
    me "Yeah. Owlet. It's a good night out here, so here he is, humming with pleasure."
    me "There is nothing to be afraid of here. Let's take the shuttlecock and leave him."
    un "O-okay…"
    hide un with dissolve
    "I freed myself from her hands and, turning around, tried to get what we came here for."
    "Standing on my toes and stretching out my hand, I picked up the plastic plumage of the shuttlecock with my fingertips."
    "He easily succumbed and fell into the substituted palm."
    me "That's all there is to it!"
    show un surprise sport at center with dissolve
    "Lena stood with her hands pressed to her mouth and looked at me with incomprehensible admiration."
    me "So, do you need it?"
    "I had to remind her why we came here, before she finally relieved me of the unfortunate projectile."
    show un smile sport with dspr
    "I smiled at Lena and got a quiet smile in return."
    un "You're so brave…"
    scene bg ext_path_night
    with dissolve
    "Brave? For real?"
    "I'm anything but brave."
    play sound sfx_hiding_in_bush fadein 0
    scene bg ext_playground_night
    show un normal sport
    with dissolve
    "It occurred to me that if one day I had a wife and children, and they were taken hostage, as in all action films, I would just shrug my shoulders and experience absolutely nothing."
    "I'm a pretty good 'press any key' guy, decent at design, so as not to lose my pants, flying out of another job, I go with the flow THERE, in real life."
    "Just because nothing at all depended on a certain S. Persunov, with his unfinished degree."
    "And to fight for something to depend - you need to put in effort."
    "So life-swamp fluctuated like a kind of jelly, from where you could neither swim out nor dive to the bottom."
    show un smile sport at center with dissolve
    "And here, typically, you also have to go with the flow."
    "I raised my voice for the first time in seven years - and it was here."
    "For the first time I got really angry, scared, imbued and bit myself until I bled - in who knows how many years."
    "And nothing changed."
    "And as soon as the hands dropped, and the will to fight began to thin somewhere - this meeting happened."
    "The camp skillfully fed me incentives, not letting me turn sour or panic."
    "And no matter what goals the Demiurge pursued by pulling me here - I will tell him «thanks», if I ever meet him."
    if persistent.dv_7dl_tran_un:
        "I gave her the shuttlecock only when we got out of the bushes."
        me "Keep it safe, you hear me? Collective property, after all."
        "I was a little embarrassed, so I kept speaking whatever came to my mind."
        me "Why did you come specifically here?"
        un "It's just…"
        show un shy sport close with dspr
        un "I thought that if I find some secret place where no one would be."
        un "You would also come there."
        un "Because you…"
        if (alt_day2_gamblers_result['me'] == 22) and (alt_my_rival_1_tour.take == 'un'):
            un "I'm sorry that I… For screaming at you."
            un "I wanted a fair fight, but you…"
            un "I heard what Alisa told you on the porch, so…"
        "She had to pull words out of herself one by one."
        "Just a couple of minutes ago, after being rescued from a terrible beast, she cheered up and smiled, and now she was ready to cry."
        me "Lena…"
        show un serious sport close with dspr
        un "You're the only one who cared."
        me "But that's simply not true!"
        "Thoughts started rushing in and out. {w}Soviet Union. {w}Pioneers. {w}Slavya. {w}No. It can't be that nobody would care."
        un "That's why… I…"
        "She was in such a fever that I could feel it just standing next to her."
        un "I just…"
        me "What?"
        show un cry sport close with dspr
        un "…"
        "She exhaled convulsively - but that was too late."
        "Tears were already sliding down her cheeks like huge pearls."
        un "I thought that it'd be enough… {w}Like in «Onegin»…"
        "Sobbing, she replied."
        un "That observing would be enough. And it just…"
        un "I can see, I…"
        un "Why are you so close?"
        un "Why?!"
        "She babbled something else incoherently, but I did the only right thing that was possible."
        "Hugged her and pressed her to my chest."
        "At least tried to."
        scene cg d2_un_kissing_7dl with dissolve
        un "My…"
        me "Mmmm?!"
        un "…"
        "The touch was inexplicably familiar. I didn’t even have time to get scared - when the emptiness between us disappeared."
        "Lena pulled me to her and greedily dug into my lips."
        "She's shaking non-stop."
        me "…"
        "Her lips are salty from tears, and in the very corner, where she bit herself, blood has dried."
        "Scar to scar, blood to blood - why is there such a close connection between us?"
        "Soft, tender lips."
        "Her hair smells like grapefruit and her skin smells like simple baby soap."
        "Finally, she remembered that sometimes you need to breathe, and let me go."
        scene bg ext_playground_night with dissolve
        show un shy sport close with dspr
        "Or rather, she allowed me to raise my head, and she clung to me tighter than there, next to the owlet."
        un "Don't chase me away. Please."
        un "If only for a few more minutes."
        "Hiding in my arms from the horror of loneliness, it's so easy to lose your head and imagine something else other than what it really is."
        me "Lena…"
        un "I think too much about you. I breathe you too much."
        "She again lost her mind and looked through me somewhere into the sky."
        un "Semyon…"
        me "What?"
        un "Kiss me."
        "It's always easier to follow the already beaten path, right?"
        scene cg d2_un_kissing_7dl with dissolve
        "Lena clings to me and at some point freezes completely motionless."
        "Devilishly brave act."
        "Could I express my feelings like that?"
        "I already know the answer."
        me "Have you calmed down?"
        "A quiet nod in response."
        "She carefully released herself from my hands."
    else:
        "We went back to the field."
    scene bg ext_playground_night with dissolve
    show un normal sport with dspr
    "Lena short-sightedly raised her wrist to her eyes, where there was a children's watch on a wide strap."
    dreamgirl "She also has vision problems. Check this out!"
    dreamgirl "I just don't get this - are you simply lucky with blind women, or are you purposefully looking for them so that they don't have time to look at your face?"
    th "Yeah-yeah, keep mocking me…"
    show un smile sport with dspr
    "She looked up at me and smiled."
    if persistent.dv_7dl_tran_un:
        un "Thank you…"
        me "For what?"
        un "For not pushing me away."
    un "It's time to sleep. We should go."
    un "Good night!"
    hide un with dissolve
    "She turned around and ran to the houses."
    "It's a pity. I hoped we would take a walk together."
    if (alt_day2_convoy == 'un'):
        "Morning walk was definitely not enough for me."
        "I pondered, watching her leave."
        "And inside everything sang from the fact that tomorrow will be a new day."
        "And that means I'll meet her again."
    stop music fadeout 3
    play sound sfx_owl_far
    "From the thickets came another satisfied hoot."
    "I smiled and headed back home."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_slot_dv:
    $ alt_day2_date = 'dv'
    if not alt_day2_dv_chased:
        scene bg ext_beach_sunset with dissolve
        stop music fadeout 1
        play ambience ambience_lake_shore_evening fadein 2
        play music music_list["silhouette_in_sunset"] fadein 2
        "I've wanted to go to the beach for so long!"
        "But this crazy day twirled me in the cycle of its impossible events."
        "First the checklist…"
        "I recalled, not without pleasure, how I met the rest of the inhabitants of the camp…"
        "But that was in the morning."
        if not 'music' in list_joined_clubs_7dl:
            th "And I never signed up for the music club…"
            "Thought suddenly flashed in my mind."
        "And after dinner, so much happened that there was no time to remember about the beach!"
        th "But now it's all over… {w=.3}hopefully."
        th "I won the tournament! It's time to relax and celebrate!"
        th "And I was finally able, albeit in the very evening, to get to the shores."
        if alt_day2_us_escape:
            "The boat adventure doesn't count."
        "I looked into the distance."
        "The railway stretched like a string against a perfect sky."
        "Rolling, the waves sparkled and blinded the eyes so hard that I had to squint."
        "The sun slowly slipped below the horizon, painting the low clouds in all shades of pink, purple and orange."
        th "Like a child, playing with paint…"
        "But even though the sun was leaving, announcing the approaching end of the day, it was still warm."
        "Kinda hot."
        "I really wanted to jump into the water with a running start, and spread out on the waves, resting from the hustle and bustle of all sorts of experiences."
        "I took off my shoes."
        "What a bliss it is to feel how amber sand crumbles under your fingers, crunches and pricks your heels with small pebbles!"
        "During the day, the sun warmed it so much that even now it pleasantly burned my bare skin!"
        "I unbuttoned my shirt, slipping my neckerchief into my pocket, and involuntarily turned around before pulling off my shorts."
        "I'm a big fan of swimming, until the age of fourteen I actually suffered from a severe form of hydrophobia, and most of my baths were limited to lying on the water or dipping my feet…"
        "So splashing around like this - never actually happened."
        "And then I slowly began to enjoy it."
        "And then the usual, familiar story — slowly fading interest in absolutely everything."
        "The only depressing thing: I didn't have swimming trunks, so I'd just have to swim in my shorts."
        "Oh well, that'll do."
        if alt_day2_us_escape:
            "After the first stroke, the body protested a little - the daytime demarche was still making itself felt - but soon it got into the rhythm, and I swam towards the buoys."
        else:
            "I splashed a little, restoring the motor skills of the body, after which I laid down on the water and rushed towards the buoys."
        play sound sfx_water_emerge
        th "Haven't been in water for so long!"
        "Measuredly grabbing air, rhythmically moving my limbs, I moved in the water, not to say that I was a great swimmer, but I definitely wasn't swimming in the style of an ax for sure."
        play sound_loop sfx_swimming
    play ambience ambience_lake_shore_night fadein 2
    "Completely relaxed, I floated lazily and leisurely, thinking about what a busy day it was today…"
    stop music fadeout 1
    stop ambience fadeout 1
    stop sound_loop fadeout 1
    play sound sfx_shoulder_dive_water
    scene black
    with vpunch
    play music music_list["that_s_our_madhouse"]
    $ lp_dv += 1
    "And then I did what I should've never done - I lost sight of Alisa."
    play sound_loop sfx_underwater_dive fadein 1
    "And as it seems, she decided to keep me company."
    "A blow! Or rather, not even a blow, a push - immediately knocked my breath, and the rhythm, and everything in the world.."
    play sound sfx_shoulder_dive_water
    stop sound_loop fadeout 1
    "Dark water rushed into my nose, I panicked, flailing my hands, diving immediately for half a meter."
    "Drowning here would be extremely insulting, and I ordered myself to calm down."
    play sound_loop sfx_swimming fadein 1
    "Well, I got dropped a bit, happens to anyone."
    "Without air I can last at least a minute, as long as it's less than a meter to the surface. The brain without oxygen generally works without problems for two minutes, that's enough for walking to the bottom with a return trip."
    "The main thing is not to panic. Don't try to inhale or exhale."
    "Smoothly stabilize yourself and row up."
    "So, persuading myself, I surfaced and, grabbing the buoy, coughing and spitting out water, tried to catch my breath."
    scene cg d2_water_dan_night_7dl
    $ night_time()
    $ persistent.sprite_time = "night"
    show unblink
    with dissolve
    stop sound_loop fadeout 1
    play ambience ambience_lake_shore_evening fadein 2
    "Turning around in search of the offender, I found her almost right next to me."
    "She moved her hands lazily under the water, keeping herself afloat, and laughed."
    if alt_day1_me_d3_dv_feed:
        "…with a familiar mischievous laughter. Like yesterday! When she scared me outside the canteen!"
    "It seems that she was pleased with herself again and smiled with might and main."
    th "Revenge, right? Revenge…"
    me "You…"
    "Out of anger, I forgot to work with my feet and dived again."
    me "You! Pesky! Vengeful! Gal!"
    dv "What's wrong? I just sank you a little!"
    me "Not funny!"
    dv "Oh, no, no, no, it's very funny!"
    "She swam around the buoy, clearly amused by the situation."
    me "What if I would drown?!"
    dv "Well… I'd probably save you. {w=.5}Not sure."
    "That «probably» scared me the most."
    "I disengaged from the buoy and rowed back to shore, feeling my whole body literally pound from a surge of adrenaline."
    "Like a whale, I threw myself ashore just above the surf line and tried to catch my breath."
    $ alt_day2_beach_seen = True
    scene bg ext_beach_night
    "She was also breathing heavily after our dash."
    th "Wet sand stuck to me, the moon shone in my eyes, and next to me is the most obnoxious girl of the camp."
    th "Yup, I deserve that."
    "She came out of the water a little later than me and, not at all embarrassed, stood next to me and smiled."
    "And there was no threat or anger in that smile."
    if (alt_day2_gamblers_result['me'] < alt_day2_gamblers_result['dv']):
        dv "You swim better than you play cards!"
        "Uh-huh. In the style of a wild gopher."
        me "I was yielding!"
        dv "Yeah, yeah…"
    dv "Congratulations."
    if (alt_day2_gamblers_result['me'] < alt_day2_gamblers_result['dv']):
        dv "Just don't think I forgave you that screw-up in the canteen."
    "I flipped to my back."
    me "Drowning me wasn't necessary, you know."
    dv "Nobody drowned you. I just slapped you on the back."
    if alt_day1_me_d3_dv_feed:
        dv "Oh, right. Forgive me. I completely forgot how much of a wimp you are."
    stop music fadeout 3
    stop ambience fadeout 3
    "…"
    scene bg ext_beach_night with fade2
    play ambience ambience_lake_shore_night fadein 2
    "She laughed again and stood up, stretching."
    "Well, I wasn't made of metal either…"
    play music "<from 30.05 to 99.42>" + music_7dl["everlasting_summer_alice"] fadein 3
    scene cg d2_2ch_beach:
        pos (0,-1920)
        linear 10.0 pos (0,0)
        linear 2.0 pos (0, -250)
    "Paint generously rushed into my face, and I hastened to turn away."
    "Alisa's figure in a bikini was clearly outlined by the moonlight, and I suddenly thought that her words…"
    "That bet…"
    "It wasn't as crazy or stupid as it seemed at first glance."
    th "After all, there definitely was something to spy on!"
    "I smirked."
    th "And touch!"
    "Impossibly attractive sight."
    "I myself did not notice how I again caressed the graceful contours of her figure with my eyes."
    "In an orange swimsuit and with drops of water on her skin, she looked like a statue of a precious stone, a work of art."
    "What an eyeful."
    "She caught my gaze and winked."
    dv "You might not be as much of a retard."
    "The last word scarred my mind."
    "Seems like this bastard managed to hurt me. {w}Well, that's admirable."
    "As the first engineering rule states: if a thing is smashed for a long time, it will eventually break."
    "Dvachevskaya has been testing me for the second day already, and it is not surprising that she eventually started discovering gaps in my phlegm."
    scene bg ext_beach_night with dissolve
    "I sat up convulsively, covering my underwear with my hands, but she seemed not to notice anything…"
    show dv normal swim with dissolve
    me "Retard? Why do you keep calling me that?"
    show dv smile swim with dspr
    dv "And you aren't?.."
    "The end of the sentence hung in the air, and Alisa smiled slyly."
    me "What, does it look it?"
    show dv laugh swim with dissolve
    dv "Yup!"
    me "That's only how it seems."
    dv "And how are you going to prove that?"
    me "I'm not going to prove anything to you!"
    "That's where I got really angry."
    show dv normal swim
    dv "Ah, that's how it is."
    "She quietly stretched."
    "And stared into my eyes."
    "And I didn't take off mine. Somehow… Wasn't fast enough?"
    dreamgirl "Uh-huh, keep lying to yourself. {w}Just say if you didn't want to."
    dreamgirl "This cheeky girl managed to throw you off balance and make you feel something other than indifference and apathy."
    dreamgirl "Hell, you're practically obliged to pray and erect monuments to her!"
    "Compared to yesterday the night was really quiet."
    "Apart from the splashing of running water and a lone cricket playing a solo somewhere far away, all that broke the silence was the sound of my own breathing."
    "I’m sure I didn’t look the best, and Alisa’s eyes lost focus, as if she was looking not at me, but somewhere through, as if she didn’t see me or was completely immersed in some thoughts."
    if loki:
        "I'm not sure we'd achieve more intimacy than if we kissed."
        me "Hey, beauty, wake up."
        "I quietly called out."
    elif herc:
        "The old game of staredown? I wonder if she herself knows about what effect she has? Mmmm… That orange swimsuit!"
        me "Hey, Earth to Alisa, come back."
        "I waved my hand in front of her face."
    else:
        "I coughed softly to get her attention."
    dv "Huh, what?"
    show dv normal swim with dspr
    "She shuddered and shook off her entrancement."
    me "You were thinking about something."
    dv "No matter. Forget about it."
    "She picked the clothes."
    dv "Alright, see ya."
    hide dv with dissolve
    stop music fadeout 3
    "And exited the scene."
    "I was already completely softened and just wanted to see which way to crawl in order to put on…"
    "…"
    stop ambience fadeout 1
    play music music_list["that_s_our_madhouse"] fadein 1
    "And suddenly I realized that there was, in fact, nowhere to crawl! Evil Alisa stole my clothes!"
    "The bliss vanished, all the nonsense instantly flew out of my head."
    "I looked around, hoping I just hadn't noticed, and my clothes were somewhere, waiting…"
    "Nope."
    th "Alisa…"
    "And after that she is still surprised by my attitude towards her. She doesn't need to be teased, she needs to be whipped! With a belt directly applied to her soft parts!"
    "Thoughts swirled, considering my options."
    "Of course, I could tell everything to the squad leader, but the idea of walking around the camp in wet underwear did not entice me at all."
    "I imagined with my own eyes how it would look like - I, completely wet, with adhering sand, in wet undergartments, march along the path."
    "True gentleman, the only thing missing would be a monocle complete with a top hat."
    "Or I could break into her house… {w}But then her threats will actually acquire some semblance of credibility."
    "Think about it — a girl's house gets invaded by a guy only in his pants! For sure he's not there to read books."
    "Bitch! She thought of everything!"
    "In short, the redhead set me up in full. It came off, as they say, for all the millennia of deprivation and oppression."
    "This, however, does not answer the question of what to do right now. Revenge has firmly settled in long-term plans, but we need to think about the day ahead."
    "I only have one chance not to royally screw up, and it is not the biggest."
    th "Maybe she hasn't gotten far?"
    th "Then I can chase her and… {w=.3}Get my clothes back."
    "Run!"
    scene bg ext_beach_night at fast_running
    with dissolve
    pause(1)
    scene bg ext_square_night
    with dissolve
    play ambience ambience_camp_center_night fadein 3
    "Quickly running with wet heels barefoot on sand isn't really feasible, but I managed to give out good speed and very soon found myself under the reproachful look of Genda."
    me "What are you looking at."
    "I grunted gloomily to the figure, looking around in search of Alisa."
    show dv normal pioneer2 at center
    with dissolve
    "Surprisingly, she was here!"
    "Already changed, with the most bored expression on her face, she made it clear with all her appearance that she was tired of waiting until «this retard» will figure it out and reach her."
    dv "You took a while."
    "She said without turning in my direction."
    me "I hurried as best I could. Mademoiselle did not indicate the coordinates of the rendezvous, so I had to run a little."
    "I noticed a bundle of my clothes lying there, and immediately unwrapped it."
    "Nothing."
    "No soot, no toothpaste on the seams, nothing. Regular, slightly worn pioneer uniform."
    "I suspiciously looked at her."
    me "And how should I take this?"
    show dv guilty pioneer2 at center
    with dspr
    dv "You don't have to. I decided not to drown you any deeper."
    stop music fadeout 3
    me "Oh, you decided. Well, that's very kind of you. Thanks for not adding any «surprises» and returning everything as is."
    dv "You're welcome."
    show dv shy pioneer2 at center
    with dspr
    "She seemed embarrassed, but quickly coped with herself and, rising from the bench, headed towards the houses."
    dv "You really aren't that stupid."
    hide dv
    "Her voice reached me."
    "She disappeared into the night, and I remained standing in place as if struck by thunder."
    "Angry, aggressive, reckless and mischievous Dvachevskaya  - we have already seen this. We also saw Dvachevskaya embarrassed, thoughtful."
    "And now they let us backstage and let us admire the real Dvachevskaya."
    me "I'm touched. Thanks for the evening."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_slot_sl:
    $ alt_day2_date = 'sl'
    scene bg ext_no_bus_sunset with dissolve
    play ambience ambience_camp_entrance_evening fadein 1
    play music music_7dl["one_little_lone_cloud"] fadein 3
    $ lp_sl += 1
    "My head was spinning from the events occuring in the camp."
    "Too bright, too strong, too intense."
    "I already forgot when so many people surrounded me at once, excluding travel in public transport."
    "But there everything is different, there people are like in cocoons, pupated, dead; in their stupid tablets, in-ear headphones with super bass - they are not here, only the physical shell."
    "But here everyone is open. {w}Noisy."
    "With my soul, perhaps, I rested, but my psyche needed a definite reset."
    "Because even happiness must be taken in homeopathic doses, otherwise there is a risk of oversaturation."
    "Just like now."
    scene bg ext_camp_entrance_sunset_7dl at zenterleft
    show sl normal pioneer at cleft
    with dissolve
    "The loudspeakers overhead were despondently silent, the day was drawing to a close."
    "And I finally found myself a comfortable head angle, under which I didn’t twitch somewhere in the back of the head from snatches of laughter carried by the wind."
    "Next to Slavya it was quiet and peaceful."
    "Perhaps that is why I am in such a hurry to succumb and trust this girl already?"
    "Why not? She is a big person in the local hierarchy after all, capable of something - but no matter how I look, she's always alone."
    "It occurred to me that this may be due to the fact that when I don't see her whenever she isn't alone."
    "Olympiads or bathing children are probably also within her competence - but I myself shy away from such events."
    "So we see each other only in moments of forced loneliness."
    "The girl looked at a clock and said:"
    sl "The gates are scheduled for closing at twenty-two, but today I would like to do one more thing, so let's close early, okay?"
    me "Are… you asking me?"
    "I don't know why I clarified that."
    show sl smile pioneer with dspr
    "Slavya smiled."
    "That's also strange - there were no inviting notes in her smile that could be taken as her showing any interest."
    "But the heart still ached."
    sl "Who else?{w} Unless you have some other business?"
    show sl normal pioneer with dspr
    me "No, I don't have anything planned."
    show sl smile pioneer with dspr
    sl "Great! Help me out here."
    "Near the gate, in a shallow section of the pipe, designed to protect the contents from rain, an open heavy square lock hung on a nail, from which a forged metal chain went down to the ground."
    "Both the lock and the chain were covered with a rusty coating, but Slavya fearlessly took both of them - either not being afraid to get dirty, or not giving any importance to it at all."
    sl "Usually I'm the only one here constantly suffering."
    scene bg ext_entrance_night_clear_7dl with dissolve
    $ persistent.sprite_time = "night"
    $ night_time()
    "While we stood and chatted, the day was almost over."
    "A lantern lit up overhead, and in its light I saw the hinges on the doors - they should have been combined."
    "The girl quickly wrapped them in a chain, securing the ends with a lock."
    me "Can you reach?"
    show sl normal pioneer with dspr
    sl "Looks like… no, I can't. {w}Can you press on harder, I don't really have the weight for that."
    "I did as I was told, closing the doors completely and allowing Slavya to make one more coil."
    sl "Hup…"
    play sound sfx_7dl["gate_open"] fadein 0
    scene bg ext_entrance_night_clear_closed_7dl at zenterleft
    show sl smile pioneer at cleft
    with dissolve
    sl "All done!"
    "The spring in the lock predatory clicked, closing."
    "Pulling the lock, Slavya nodded in satisfaction."
    sl "Well done! {w}You know, a family of hedgehogs have settled nearby — if we don't lock up the gates, they'll definitely get in."
    me "Hedgehogs?"
    show sl laugh pioneer with dspr
    "I probably looked extremely confused, because Slavya merrily laughed:"
    sl "Have you never seen hedgehogs?"
    stop music fadeout 3
    me "I mean, I have."
    "Slowly I said."
    play music music_7dl["out_of_your_tier"] fadein 3
    me "I know what they are."
    th "As I thought."
    th "Now she will warmly thank me for the rendered assistance, show me to the gate, or even better - tell me where to go - and say goodbye."
    "That's… kind of annoying, I think."
    show sl normal pioneer with dspr
    "Being used was nothing new to me, and it's not like I didn't expect it from Slavya."
    "From the first day I met her, I recognized her as a manipulator, an eternal older sister and an activist."
    "So I just wondered where would my application point be."
    "For the first time I regretted not being mistaken."
    "It was a bittersweet feeling. {w}Hell - I caught myself thinking that most of all I hoped that she was different, and she had the magical morality of a person of Bulychev's future."
    th "Come on… Deceive me."
    "I asked in my mind."
    show sl sad pioneer with dspr
    th  "You, the bearer of the keys to everything in the camp, including my heart - what does it cost you?"
    "Slavya was silent, looking at me with a slight uncertainty in her eyes."
    me "Are we done here?"
    "I could no longer stand the silence."
    me "Where is the nearest emergency entrance?"
    "The voice was somehow wooden, official."
    sl "It's…"
    "Slavya pointed somewhere to the left."
    sl "There… You'll find it if you walk along the wall."
    "I nodded and, stooping, went."
    scene bg ext_path_night with dissolve
    "And Slavya had her business."
    "Deeds, deeds, very important - unlike one fool, who already had undeserved happiness on his head."
    "In the form of a second chance."
    if alt_day2_walk == 2:
        if herc:
            "I remembered our conversation on the square, my stupid speech about what my world is and why there is no place in it for such bright girls."
            dreamgirl "That's right - any society has its hierarchy."
            dreamgirl "Except, unlike the much more merciful Indian caste system, here the social elevator almost does not work."
            th "It does work."
            "Ruefully I tried to counter."
            dreamgirl "You don't have ten years to become some big name and buy her with prestige."
            th "I don't even know how much time I have."
        else:
            "I remembered our conversation on the square, my Freudian slip of the tongue about rescuers and a whole ministry of people who do give a damn about the lives of those around them."
            th "Oh, if only anyone would rescue me too…"
            "I thought sadly."
            th "Or at least killed me - quickly and painlessly."
            if loki:
                "For almost ten years I drowned, crushed and choked this blue and black abomination."
                "But it's still alive and kicking."
                "It rings with echoes of happiness and children's laughter, when one person stands before the inner gaze."
            else:
                "Because you can't."
                "There are things that are permissible - gratitude for being allowed into the house, fed and washed."
                "But you can't be impudent and demand something more."
                "You cannot ask - not even subconsciously dream! - that one day a smile addressed to me would look a little warmer than to everyone around."
            "Therefore, it would be more merciful and honest to simply stifle all criminal emotions in yourself now."
            "While they have only just appeared - this is the easiest way, like crushing a rose sprout with a heavy boot."
            "Almost doesn't hurt, if you don't manage to hit your fingers."
    else:
        "With a vague longing I compared this effervescent, active - alive! - girl with myself."
        "Should I even say that the comparison definitely wasn't in my favor?"
    "I angrily banged my fist on the wall along which I was moving."
    th "And does it even matter, this said time, if I seem to be going back to the person who started it all."
    th "Time gain? Oh, I'll know that «Doom» will be released in four years! {w}And I'll be able to waste ten extra years sitting before the monitor, hoorraaaaaaaaaay!"
    "All my fault."
    "Shouldn't have allowed myself to dream or hope for such things."
    "Not my field's berry, not my tier, not my level."
    "After saying the last words several times, I felt a little better."
    play sound sfx_bush_leaves
    scene bg ext_path2_night with dissolve
    "As if I dumped part of the unbearable burden of the loser on the ubiquitous fate."
    th "And we touched shoulders while closing the gate."
    "The shoulder was warm and soft. And this stupefying smell."
    if loki:
        "The top of Ksyusha's head smelled of plum shampoo and for some reason electricity, despite the fact that with her gorgeous hair she rightly disdained hats."
        "I loved hugging her, kissing her on the top of her head."
    else:
        "Once, when I had a girlfriend, I really liked to inhale the smell of her hair and kiss on the top of her head."
    "Kind of a fetish, I guess."
    "I caught myself thinking that I would not mind kissing Slavya that way."
    "I immediately gave himself a mental slap, knowing full well that I was behaving like a typical representative of the friendzone."
    "Trying to distract myself, I delved into memories."
    $ set_mode_nvl()
    if herc:
        "I'm twenty… White nights, I am sitting on the windowsill of my apartment overlooking the former church, from which the Soviet authorities made a swimming pool."
        "Over my head - the boundless, bottomless sky."
        "Court case ahead of me."
        "My arguments that I was the only breadwinner in the family, that my mother was sick, that I couldn’t, - I couldn’t! - were considered ineffective."
        "Military recruit training, hazing, monotonous everyday life…"
        "I returned from the army and found out that my mother was assigned to Skvortsov-Stepanov - from the generous hand of that same social worker who had to either get me a reprieve or take care of the recruit's mother."
        "You can take one tiny step."
        "And it all will go to hell."
    elif loki:
        "I'm nineteen - nothing to brag about: I'm an idiot."
        "Something in my lungs gurgles hoarsely when I breathe, stooping."
        "And I smoke in the transparent sky of St. Petersburg's white nights, sitting with my back in the window, dangling my leg into the street, welcoming the five-story void with my heel."
        "It's June, my birthday."
        "Ksyusha was right about something. Even her moron was somewhat right - except that I would not hire people, but beat the shit out myself."
        "Everyone is right, yes. Wherever you look. Not a single one to blame, all the victims."
        "But who would return me to Music?"
        "Smiling, I flicked my cigarette away…"
        "…and tipped over into the abyss."
        "The sky jumped towards me…"
    else:
        "I'm twenty-one, and I'm sitting in an open window, which I never changed to cheap plastic double-glazed windows."
        "Back leaning on the south edge of the rectangle, right leg hanging down, cigarette in teeth."
        "Doctor, doctor, give me this beautiful lilac one, and also that pink one with a long longitudinal line."
        "And some medical alcohol to drown my bleeding heart."
        "«Drotaverine Hydrochloride» — I read bright red letters on a transparent jar."
        "Spasmolytic. Painkiller."
        "Saving from pain."
        "If you have a headache. Or a toothache. Or something else."
        "Just eat a few pills by weight - and you're fine."
        "White from pain eyes with an almost absent pupil."
        nvl clear
        "It should be blue, as the sky."
        "And there should be a smile."
        "And love for the whole world - the golden color of her hair."
        voice "Why is everything so wrong…"
        "I read this question on the lips."
        "I keep eating painkillers."
        "But for some reason it does not help: probably the dose is insufficient."
        "Gotta eat more so they help."
        "If you eat enough, it will help relieve the pain."
        "I wonder if 200 of those would be enough?"
        "I tore off the lid along with the dispenser and, opening my mouth, poured all these cheerful sunny rounds into my throat."
        "Smiled crookedly and, having washed down with already warm absinthe, threw an empty jar at my feet - down from the fifth floor."
        "The jar jumped, hitting the ground, and from the open door of the front door immediately jumped out the driveway cat Maha, which we fed collectively with the entire porch."
        "Jumped, rolled…"
    stop music fadeout 3
    $ set_mode_adv()
    "That's when I looked beyond the other side for the first time."
    "Perhaps it would be worth staying there - I almost see no point in anything happening to me."
    "Even this fairy tale, even this magical gi…"
    sl "There you are!"
    show sl normal pioneer
    with dissolve
    play music music_list["forest_maiden"] fadein 2
    "I stopped and raised my head."
    "She caught up with me with a quick step, almost without disturbing the environment."
    "Fitting in perfectly, like being a part of it all - no wonder I haven't been able to notice her until now."
    sl "Why did you leave?{w} I kept calling you…"
    "The girl stood next to me, breathing easily.."
    me "Sorry…{w} I guess I've been thinking."
    me "Retreated into myself, and all that."
    th "That's it, the duty of courtesy is done, you can leave."
    sl "When you turned around like that and went - it felt like something cut me.{w} I thought you couldn't let go like that. I'm a fool, yes?"
    if loki:
        th "If only you knew…"
    th "Don't you have important business?"
    "I kept silent."
    "Still, her company really warmed me. {w}Even if it was reflected light - such suns cannot be, but shine."
    me "Slavya, don't you have anything better to do?"
    show sl surprise pioneer with dspr
    sl "What do you mean?"
    "She looked at me in surprise."
    me "You asked me for help, I helped you, that's all, thanks, I left. {w}Why do you keep pretending that you care?"
    me "Do you think I'll believe that?"
    "I myself did not know why I said this, but it was as if during these two days the abscess had completely filled up and burst, releasing all the dirt and filth outward, granting the tortured flesh a temporary, but still a cleansing."
    sl "Semyon, what are you…"
    show sl serious pioneer with dspr
    "She furrowed."
    sl "I just wanted to feed the hedgehogs a little, I thought you would come with me - and you ran away."
    if (counter_sl_cl == 1):
        me "I understand that you feel obligated that I covered you with the keys.{w} But it's just a return courtesy for yesterday's food."
        me "We're even and you don't have to force yourself to waste time on me anymore."
    else:
        me "Here's this one thing I don't get - why have you been running around with me for two days?"
        me "I know very well that you have a lot of things to do, and I… I only hinder everyone."
    show sl sad pioneer with dspr
    "I don't know which nerve I hit, but it definitely hurt - her eyes sparkled, and her voice even trembled a little:"
    sl "I don't know what's more disgusting: the fact that you tell me these things, or that you sincerely believe in them yourself…"
    me "But this is a normal communication pattern!{w} Everyone uses each other one way or another."
    "I understood that such things should not be said when such a beauty is nearby, and such a night is around."
    me "There's nothing bad in it.{w} I just don't want you to force yourself, that's all."
    sl "Semyon…"
    me "You're too good to be true.{w} And I like you too much."
    "The deed was done."
    "Organically - like everything that happens around Slavya."
    show sl normal pioneer with dspr
    "And she stared into my eyes - a long, searching look."
    "But not even a minute passed before she turned away."
    th "Who would've guessed."
    "I smiled bitterly."
    show sl tender pioneer with dspr
    sl "See."
    "Her voice was soft, gentle, like I've never heard before."
    sl "You should have just said it out loud from the start."
    show sl shy pioneer with dspr
    sl "And there would be no dirt on the soul."
    "She never looked in my direction, instead smiling dreamily and fiddling with her braid."
    sl "The most important thing is to be honest with yourself."
    sl "When you understand what's really in your heart, you don't push people away. {w}Just like now."
    sl "I no longer feel bad from you - you are not smiling yet, but that'll happen."
    me "Probably…"
    "Slavya finally raised her eyes to me."
    sl "Not probably, stupid Semyon!"
    "She took one step towards me."
    sl "I'm telling you - you will be smiling."
    show sl shy pioneer close with dspr
    "Another one."
    sl "Just stop doubting, stop lying to yourself."
    "And, finally, she took my hand."
    "Short-cut nails scratched my palm, casually drawing on it either a circle or some kind of apple."
    show sl smile pioneer close with dspr
    "I shuddered."
    me "You do realize that you're asking for too much?"
    sl "I'm not asking for everything at once."
    "Retorted Slavya."
    sl "I'm asking you to try."
    sl "Pouting like a mouse on grits is the easiest way."
    sl "And I like your smile."
    "And suddenly I realized that I've been smiling like a dumbass for a few minutes now."
    me "Yeah…"
    sl "And when you're calm."
    "She hugged me."
    sl "Stay like that."
    "She whispered."
    if herc or loki:
        "Slavya tried to move away."
        "But instead I caught her."
        show sl surprise pioneer close with dspr
        "Squeezed so hard that she exhaled in amazement."
        "And, finally, closed up my gestalt."
        "Her hair smelled of tar and lemongrass."
        "I touched them with my lips - so that she wouldn't notice anything."
        "And let her go."
    else:
        "I stood like a pillar, red, embarrassed."
        "So she had to take my hands and hug herself with them."
        "For some reason, she shuddered when my hands fell on her shoulders."
        sl "I'm not asking you to believe me."
        sl "But don't harden up."
        "She stroked my cheek and, easily freeing herself, took a step back."
    scene bg ext_backdoor_night_7dl
    show sl smile pioneer
    with dissolve
    "We came to the gate."
    "And from there…"
    scene bg ext_houses_night_7dl
    show sl smile pioneer
    with dissolve
    "We reached the houses."
    sl "That was a nice evening…"
    th "Yes, you managed to make it so."
    sl "Thank you."
    me "Why are you thanking me?"
    show sl smile2 pioneer with dspr
    sl "Try guessing!"
    me "I'll think about it tomorrow."
    "I muttered."
    sl "Then, see you tomorrow?"
    if ('sports' in list_slavya_7dl):
        me "What «tomorrow»? Someone promising me an evening on the beach!"
        show sl smile pioneer with dspr
        sl "And you haven't forgotten, huh."
        sl "You have swimming trunks?"
        me "Uh…"
        sl "Thought so. {w}Let's go, we'll get you state-owned ones."
        "…"
        with joff_l
    else:
        "The girl waved to me and ran away."
        hide sl with easeoutleft
        "And I froze, looking at the sky above my head, trying to calm my heartbeat and complete discord in my thoughts."
        "This girl seemed to have demolished all my protection levels, and for the first time in my life I was in no hurry to restore them."
        "For the first time in my life, I suddenly wanted to blindly - stupidly - trust."
        "Knowing full well that nothing good will come of it."
        "But be that as it may, I was - for the first time in a long while - inexplicably happy."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day2_slot_mt:
    scene bg int_house_of_mt_sunset
    show mt normal pioneer at cleft
    with dspr
    me "How?"
    play music music_7dl["lazy_olga"] fadein 3
    mt "Look here."
    "Out of nowhere came a plump pack of white cardboards with a stylized owlet on the edge."
    mt "Vouchers for the third shift, many children will come, you need to fill out the list. Can you handle it?"
    me "Nothing complicated, of course, but what are you going to do then?"
    show mt smile pioneer with dspr
    mt "You didn't get it yet?"
    mt "I'll lie down and read for a bit, of course."
    "And again, like a few hours ago, a voiceless cry flew into the sky:"
    th "Oh, Olga Dmitrievna!"
    dreamgirl "Oh, just you wait!"
    scene
    $ renpy.show("cg d2_mt_me_resort_afar_7dl", what = Dawn("cg d2_mt_me_resort_afar_7dl"))
    with dissolve
    "The work went smoothly."
    "It actually wasn't complicated…"
    "Under a typewritten «Pioneer camp «Sovyonok», were outlined guides, where I, in the most diligent handwriting, almost sticking out my tongue from zeal, transferred the data from the questionnaires."
    "Voucher number, issuing period — from August 4 to August 25, 1989."
    "Then last name-first name-date of birth-place of study-home address."
    "In Soviet Russia you don't go to camp, the camp comes to you."
    "For a pack of such vouchers, given for census to a lazybones like me, in my 21st century you could get a myriad of official penalties."
    "But here nobody gave a shit about your privacy."
    "And somewhere in the paper rubble at the twenty-seventh kilometer from the Black River, the ticket with my data is also stored - and will be stored for another ten years in accordance with the declassification regulations."
    with fade2
    "It could seem that it was all so easy, but for me, almost completely unaccustomed to using a pen…"
    "But she ain't going to make me complain that easy."
    "I glared at the squad leader angrily - and caught the look she threw at me over the top of the book."
    mt "What, you're tired?"
    "She asked in such a voice, as if the work of a clerk was a mere trifle."
    me "Of course not, how could you think that."
    "I chuckled."
    mt "Well then…"
    "She crossed her legs on the headboard and, tucking the elbow of her left hand under her head, again plunged into reading."
    me "I just can't figure out one thing - why you're messing around while I'm doing your job."
    mt "Semyon, don't be a bore, it doesn't suit you, you know?"
    me "I'd better be a bore than a slave, we aren't slaves, hear me!"
    dreamgirl "Here we go again…"
    dreamgirl "Stalin is gone! Stakhanov will no longer work! In Poland, Anna German won't sing us a new hit!"
    mt "Semyon, you're doing it the wrong way."
    "The girl smiled, placing the book on her chest."
    mt "First you need to get on a stool, remember how you used to recite poems in your childhood?"
    me "You've gotta be kidding me…"
    mt "Only a little bit. {w}Just teasing. {w}How much did you finish?"
    "I checked the list."
    me "Almost everything."
    mt "See, what a good guy you are."
    th "And then I jump up like that, my hand to my empty head and in my throat: «I serve the Soviet Union!», or whatever they do here?"
    dreamgirl "Communist party, communist party! {w}The plan is the law, the fulfillment is the duty, the overfulfillment is the honor!"
    th "Oh screw you!"
    me "Don't you think you can't trust a pioneer with such things?"
    me "It's personal information after all."
    mt "Ah, that's what was bothering you."
    mt "Don't worry."
    "She winked at me as she went back to reading."
    mt "I believe in you!"
    me "Olga! Dmitrievna!"
    mt "I see noothing, I heear nooothing, noothing! Will! I ever tell!"
    hide mt with dspr
    "Carelessly humming a song under her breath, she turned the page, pretending with all her might that she was resting alone."
    "And I returned to writing."
    play sound sfx_click_2
    $ persistent.sprite_time = "night"
    $ night_time()
    scene cg d2_mt_me_resort_afar_7dl with dissolve2
    "It got dark outside the window, so we turned on the lights."
    "It was already a matter of personal prestige - to finish off the unfortunate pioneers, starting with the letter «P»."
    "Last name, first name, age, place of study, address, phone."
    th "Last name, first name, age… {w}Oh, for what sins did I get this punishment."
    $ hvala_randomu_7dl = renpy.random.choice([1, 2])
    if hvala_randomu_7dl == 1:
        mt "That guy… Starts with «D», cross him out."
    elif hvala_randomu_7dl == 2:
        mt "Cross that one out, starts with «E»."
    "I suddenly felt the warmth of breathing on my cheek, and something warm pushed elastically into my shoulder."
    mt "They mixed it up again, he's banned."
    me "Why?"
    if hvala_randomu_7dl == 1:
        mt "Spectacularly screwed up last year — turned his house into a tavern, it stank so much that they had to air it for a week."
    elif hvala_randomu_7dl == 2:
        mt "Last shift, chased after Ulyanka, saying that she had been allowed for a long time, dragged some folder with documents with him, tried to present it as evidence."
    with fade
    "Olga took a pack of vouchers from the table and skimmed through."
    "She chuckled, took out one and threw it in front of me."
    $ hvala_randomu_7dl = renpy.random.choice([1, 2, 3])
    if hvala_randomu_7dl == 1:
        mt "This one, starting with «Y», cross him out too."
    elif hvala_randomu_7dl == 2:
        mt "Cross out those starting with «A». Both of them."
    elif hvala_randomu_7dl == 3:
        mt "And this ukrainian guy on «S» too."
    me "Why?"
    if hvala_randomu_7dl == 1:
        mt "Also a weird guy. Kept running around the camp, searching for an intercom."
        me "So what?"
        mt "Nothing. Stole the keys, yelled something about overtaking this facility and that some MTF got destroyed in the middle of the night, now he's yelling in a psychiatric dispensary."
    elif hvala_randomu_7dl == 2:
        mt "One almost... hang himself by accident... thrice. Second got mad about that someone spelled «scene» without capitalizing it so he almost beat that guy to death."
    elif hvala_randomu_7dl == 3:
        mt "He snuck into the cybernetics club and reprogrammed their robot so that it learned to whistle and… do something else. Cybernetics then fixed everything, but for some reason, after the corrections, the robot even forgot how to walk."
    me "As you wish."
    "Semyon was a very obedient boy, and another troublemaker was weeded out."
    "Olga was still standing, hovering over me a little, touching me - I froze."
    mt "Your ears are red again."
    scene bg int_house_of_mt_noitem_night at enterright
    show mt smile pioneer
    with dissolve
    "Reaching out her hand, she placed the kettle on the table and plugged it into the socket."
    me "Nom they didn't…"
    mt "How do you feel about tea at midnight?"
    "She had not an ordinary suitcase, but a stylish - black and red - travel bag."
    "From under the top cover of which she took out a bag of waffles and a tiny teapot."
    me "Is that even allowed?"
    show mt grin pioneer with dspr
    mt "Of course! Just be careful!"
    "The components of the future tea ceremony were in front of me on the table, surrounding the completed list and a pack of tickets next to it."
    mt "But you'll have to work a bit."
    me "Again?!"
    show mt laugh pioneer with dspr
    mt "Sorry, Syomchik - I would gladly take care of you…"
    "She glanced at the clock."
    mt "But duty calls - I have to ensure everyone is in bed."
    mt "I'll try to be quick, alright?"
    "She gave me a quick smile."
    "And, throwing on a windbreaker, fluttered out into the street."
    hide mt with dissolve
    "Even now I had to take care of our squad leader."
    "Worked for her - now make tea for her."
    "I caught myself thinking that I was smiling quietly and stupidly, as if this was not the first time I had it - as usual, comfortably, at home: grumbling at an unlucky girl, waiting for her at home with a cup of tea."
    scene
    $ renpy.show("cg d1_me_dahell_7dl", what = Sepia("cg d1_me_dahell_7dl"))
    show anim_grain
    with flash
    th "As if there was no panic at the mirror, no fear, fettering the chest…"
    "I relaxed and enjoyed a warm, cozy evening."
    play ambience ambience_camp_center_night
    play sound sfx_open_door_2
    pause(1)
    scene bg ext_house_of_mt_night_without_light
    with blind_l
    "She actually got done with it fast."
    "I barely had time to carry both glasses in forged glassholders to the street."
    "To the left of the stairs, where the faithful iron horse of our lazy leader stood, there was a very convenient place."
    "Worn even in appearance, covered with some kind of round marks."
    "In two of which both glasses fit perfectly."
    th "Porch."
    "The word suddenly appeared in my mind."
    "Place for your shoes, mushrooms, drying fish…"
    "And a cup of tea."
    "And when I sat down on the second step, this porch fit perfectly under my elbow…"
    show mt normal pioneer with dissolve
    mt "You're sitting without light again."
    th "Obviously. Without light. And without my neckerchief. And without any of my strength."
    "The step next to me creaked under the weight of Olga sitting down."
    "The girl stretched out her hand to the switch - but on the way she waved her hand..."
    "And gave up."
    th "Dmitrievna? More like, Lenivovna…"
    mt "Thanks for tea, Semchik."
    "She thanked me, unceremoniously leaning her shoulder against me."
    "And, noisily taking a sip, she put the glass aside, stretched out her legs and leaned back."
    "I swallowed as I watched er shirt tighten and turned away."
    mt "Wonderful tea."
    stop music fadeout 3
    me "And a good evening."
    mt "As it always is in this camp."
    play music music_7dl["wheres_wonderland"] fadein 3
    scene stars with dissolve2:
        zoom 1.1 xalign 0.5 yalign 0.5 subpixel True
        easein 200.0 zoom 2.5 rotate -10
    mt "And the sky is so vast."
    "She whispered."
    "And I heard."
    "As if I knew what and how she was saying."
    "Even the fact that I was stretched out on the steps next to her; staring at the living - breathing! - sky was something natural."
    mt "I gave you paperwork because I trust you."
    "Olga reported."
    mt "Because I think that I'll bring you along as a fellow squad leader some day."
    "She snorted."
    mt "But first of all, because when we are alone, your neck always turns red."
    me "It doesn't!"
    mt "You always funnily argue with that."
    "Her finger slid across the sky - first to the south, to a huge blue star."
    "Then down at a slight angle - to the southeast."
    "Sharp turn up, to the northeast, one more, one more…"
    mt "An uneven pentagon, noticeable only in these latitudes - remember what it's called?"
    me "Letter?"
    mt "That's right… I could have become an astronomer, watching how our Universe is marking time, but instead I went to work with children."
    mt "Although I never stopped loving just watching the stars sometimes."
    mt "What do you think, Semchik - is there anyone out there?"
    "I, remembering the Fermi paradox, shrugged my shoulders:"
    me "If there's anyone out there - then where are they?"
    mt "A villain with a vulgarity for any occasion."
    "Her laugh was sad, somehow regretful."
    if counter_sl_cl == 1:
        mt "Don't be angry about canteen duty."
        mt "I understand perfectly well that you just stood up for a pretty girl."
        mt "But I can't show forgiveness."
        me "Is that how it is? Why?"
        "She laughed again - this time more heartily."
        mt "Because you'll instantly start abusing it."
    mt "This is our last summer together, you know that?"
    "I vaguely shrugged."
    mt "And tomorrow you'll turn your «life walker» back on, and I won't keep up with you while you accumulate impressions."
    mt "So this might be our last chance to sit like this together."
    "Olga went to a sun lounger and dragged a foam pillow from there, which she arranged on the top step."
    mt "Want a piece?"
    "She smiled mischievously."
    "I froze and couldn't squeeze out a single sound."
    "Of course it could just be a game for her, but…"
    "Were there any limits?"
    mt "Don't want it? {w}What a proud young man."
    mt "Don't be afraid, I won't eat you, I won't even bite you."
    "Olga settled her head on the folded foam, looking thoughtfully into the sky."
    mt "Perfect time for fairy tales, right? {w}Wanna hear one?"
    "Without waiting for an answer, she began:"
    mt "About how once a stupid girl, yesterday's teacher graduate, had a fight with her superiors."
    "Her voice was getting quieter and more uncertain."
    mt "And she was sent to meet a bus that was carrying only one person."
    "I had to strain with all my might to hear individual words."
    "Moving closer to her was both scary and curious!"
    mt "A fairy tale about how you feel like you're disappearing - and there's nothing you can do about it…"
    "She got silent."
    "I myself was in some prostration from her revelations."
    mt "Your fear is vain."
    mt "We live in the same house, do you really think that it will surprise anyone that we are sitting on the porch together?"
    th "I'm afraid that someone will see us lying on the same pillow and cooing like doves."
    th "Because this time it can't be attributed to: «Well this is her first year, she doesn't know how to separate personal and professional matters»."
    mt "Like grandparents."
    "Olga smiled sadly again."
    mt "Why didn't you go anywhere today?"
    mt "There's no way not even a single girl got your attention?"
    menu:
        "How so?":
            $ alt_day2_date = 'mt'
            me "One did."
            "I finally confessed. {w}Firstly - to myself."
            me "It's all just like in the movies, see, my hands are trembling?"
            mt "That's just nerves. And you're breathing too fast."
            me "And my heart skips a beat when you're on my shoulder."
            mt "The tea is just too strong."
            me "We're together for a reason, maybe that's a sign?"
            mt "Someone read too many romance novels."
            me "For how long are you going to tease me?"
            mt "Why do I even worry about you…"
            "The girl sighed."
            "And, raising her head a little, she touched my cheek with her lips."
            scene bg ext_house_of_mt_night_without_light at zenterleft
            show mt sad pioneer at cleft
            with dissolve
            me "Oops!"
            mt "You know, if I would be three years younger - I would've definitely believed you."
            "She got up."
            show mt smile pioneer at cleft with dspr
            mt "You say the most irresistible things, you fucking flatterer!"
        "It didn't work out.":
            mt "Is that so? Eh, it's alright, you still have time."
            scene bg ext_house_of_mt_night_without_light at zenterleft
            show mt normal pioneer at cleft
            with dissolve
    mt "I should go."
    me "Meeting?"
    "I figured."
    mt "Yup.{w} Thanks for the tea."
    hide mt with dissolve
    "She silently departed, leaving me alone with the warm night."
    "With a calling, alluring, magical, warm night."
    "The perfect time for all your wildest dreams to come true."
    "Olga behaved very strangely, and I reacted just as strangely to her."
    "Does this mean we have a future?"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return
