label alt_day4_mi_dj_begin:
    scene bg int_house_of_mt_night2 with dissolve
    play sound sfx_bus_window_hit
    "Some time later - I thought I had my eyes closed for a moment - a small pebble struck the glass."
    th "What the..."
    "Barely relaxed, my body was tugging unmercifully back into the comfort of the blankets, but a second later a second pebble struck the glass."
    play sound sfx_bus_window_hit
    "All hope that the silent thumping on the glass was just a dream had been dashed. {w}And that I would go back to the dream - where Miku was waiting for me."
    "Miku..."
    "I smiled, remembering what I'd seen for the last - how long? Half an hour? An hour?"
    "A narrow palm, slender, nervous fingers, a dainty wrist and transparent marble skin, generously sprinkled with moonlight."
    "The quiet evening of the northern latitudes, perfumed with the scent of pine with damp flecks of inbound mushroom rain, - I could never get away from the impression that the earth at these moments was spreading its alveoli and taking its first breath."
    play music music_7dl["breath_me"] fadein 6
    "The newborn earth takes its first breath and comes out to nourish and give birth to the world."
    "And we're sitting on a stubby pine tree, nestled comfortably in a fork between thick branches, and I'm the real deal, approaching thirty, and Miku is a little older - she lies inside me, like in the most comfortable hammock."
    "And my breathing is Gagarin's - eight breaths and exhalations, and my pulse is cosmic - 54 beats per minute. This is the only way to overcome nervous trembling and tune in to a unified way, when you understand the feelings of the dearest person before he is aware of them."
    "It's the only way to indulge in what I've spent my life calling 'laziness,' and the Hindus of all time have called tantra--the unhurried, sweet dissolution into a partner snuggled up on my chest."
    scene bg int_house_of_mt_night2
    stop ambience fadeout 1
    play sound sfx_knock_glass
    pause(1)
    play ambience ambience_int_cabin_night fadein 2
    "I seem to have fallen asleep again, for from throwing pebbles the mysterious visitor went on to knocking on the glass. {w}And in that pounding one could clearly hear impatience."
    th "Damn it, whoever you are, Olga's going to get up now, and you're a dead man."
    "I opened one eye, expecting to see the squad leader rising - I'd always missed these moments in mornings."
    "And what was my disappointment when I found out I was alone in the cabin!"
    play sound sfx_knock_glass
    pause(1)
    th "Looks like we'll have to get up after all."
    "With dejected humility, I thought, and I unlaced my wadded up body from the sagging armor net."
    "It was as if something heavy had knocked me over the head - an already dark room darkened even more, green circles swam before my eyes, and a thin, unpleasant humming was in my ears."
    th "Bloody dystonia."
    "I fumbled for the light switch and looked closely at the window."
    scene bg int_house_of_mt_night:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 2.0 zoom 1.6 xalign 0.7 yalign 0.35
    "I had to stand for a few seconds, leaning my arms against the wall, struggling with my dystonia, blinking out the green circles floating before my eyes - but I soon got over this unpleasantness and went to the window and stared out into the night."
    scene bg int_house_of_mt_night:
        xalign 0.7 yalign 0.35 zoom 1.6
        linear 1.0 zoom 2.2 xalign 0.7 yalign 0.35
    "Miku was already there, smiling."
    "When she saw that I noticed her, she waved her hand."
    dreamgirl "The girl seems to crave attention."
    th "It seems all white people are still asleep at this time."
    "I grumbled."
    th "What are you doing awake."
    dreamgirl "Hey!"
    "My eternal companion laughed softly."
    "And fell silent, letting me collect myself. {w}After the dance, all my everyday clothes were on the stool, and there was no question of what to wear."
    stop ambience
    scene bg ext_house_of_mt_night_without_light
    show mi smile pioneer
    with dissolve
    mi "Oh, hello, Senechka!"
    "Chirped the waiting Miku."
    mi "Did I wake me up? Sorry, I'm just having a little problem, and I can't seem to deal with it."
    me "Problem?"
    "The yawning seems to have dislocated my jaw a little, as I clenched my teeth with a palpable crunch."
    me "Can't this problem wait until tomorrow, for example? If Olga Dmitrievna catches us..."
    dreamgirl "A ballpoint pen to the top of your head. Don't be stupid, eh? {w}Girl's calling you in for the night! I don't think that's an offer you can refuse that easily."
    show mi serious pioneer with dspr
    mi "No, I've settled everything with Olga Dmitrievna."
    "Was it just me, or was there a note of uncertainty in her voice?"
    dreamgirl "It was just imagination. Or not. {w}See for yourself, you may have well been called upon to warm up her crib under the covers."
    "I cheered up."
    dreamgirl "Well, or to quietly smother you with a pillow and cut out your kidney."
    th "You're not helping!"
    dreamgirl "Okay, now jokes aside. {w}What do you think will go through the leader's mind when she catches you - which is inevitable."
    dreamgirl "And the fact that it's night out will only make your guilt worse."
    dreamgirl "Do you want to get kicked out of camp?"
    th "Why get kicked out?! Maybe she does have some problems."
    dreamgirl "Sure. And when asked about coordinating with the squad leader, she wagged her eyes to the side for that reason alone."
    th "Then what? Do I chase her away?"
    dreamgirl "That's the safest option. Otherwise, look, I know you, when she starts undressing, you could be molded into plasticine, and given your luck..."
    th "I got it, I got it. Let me think about it."
    dreamgirl "What's there to think about? She's calling you for one thing, and at your age it's time you learned how to prepare a bridgehead. Do you have any in mind?"
    th "Uh..."
    dreamgirl "Exactly. Tomorrow or the day after tomorrow you'll figure out how to distract the squad leader and make sure everyone else's presence is excluded, and then you can go poking around the girls' cabins."
    dreamgirl "You won't get anywhere now anyway."
    th "That's it! Chapay has thought. Chapay decides."
    menu:
        "Go help Miku":
            $ lp_mi += 1
            if alt_day2_convoy not in ('dv', 'sl', 'un'):
                $ lp_mi += 1
            $ alt_day4_mi_dj_hedg = True
        "Go back to sleep":
            me "I'm sorry, Miku, but I've had a tough day."
            "Said I, fighting another yawn."
            me "And if I don't get at least a couple of hours of sleep, I'm going to freeze."
            me "So let's leave all problems for tomorrow, okay?"
            "Without listening to her objections, I went up on the porch."
            play sound sfx_open_dooor_campus_1
            scene bg int_house_of_mt_night with dissolve
            "I fell asleep before my head touched the pillow."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_dj_hedg_hunt:
    scene bg ext_house_of_mt_night_without_light
    show mi serious pioneer
    with dspr
    "Olga Dmitrievna was suspiciously long gone, so I had to rely on Miku's conscience and my trust in her."
    me "Let's go, daughter of the sun."
    "I sighed, having already resigned myself to the fact that in the morning I would wake up boiled."
    show mi happy pioneer with dspr
    mi "Really? Oh, I knew it, I knew you wouldn't say no!"
    "She clapped her hands enthusiastically - and then cautiously fell silent, looking around."
    "Impulsive as can be - that's my Miku."
    me "So what's your problem there?"
    mi "Come on, I'll show you on the spot."
    "The Japanese girl grabbed my arm and pulled me to the far end of the «street» to the cabin, which she shared with Lena."
    scene bg ext_house_of_un_night_7dl with dissolve
    "Without the slightest hesitation, she dashed down the steps, dragging me behind her."
    play sound sfx_open_dooor_campus_1 fadein 0
    "And, pushing the door"
    scene bg int_house_of_un_night with dissolve
    extend ", popped into the cabin."
    play ambience ambience_int_cabin_night fadein 3
    "And I was struck with belated terror:"
    th "What if Lena is there?! And she's..."
    dreamgirl "Naked! Yes!"
    th "What's that got to do with it. I mean the dream."
    dreamgirl "No, no, what dream! It's night, everybody gets naked!"
    "Luckily, Lena wasn't in the cabin - it was just the two of us here with Miku."
    me "Where's Lena?"
    show mi normal pioneer with dspr
    mi "Lena? What difference does it make?"
    dreamgirl "See!"
    "The inner voice didn't think to hide the winning intonation."
    dreamgirl "I tell you - she's calling you in to warm her up with vigorous rubbing."
    dreamgirl "Look, now she's going to close the door, loosen her tie, and..."
    th "That's enough, okay? I'm embarrassed enough as it is, and you're adding fuel to the fire."
    "I think the girl was a little out of it. {w}At any rate, that last sentence couldn't have belonged to the kind and compassionate girl I know Miku to be."
    show mi sad pioneer with dspr
    mi "Oh, what am I saying! I'm sorry."
    mi "It's just that with all these problems, I don't know what I'm spouting anymore."
    "I leaned against the door, crossed my arms across my chest, and, trying to speak as softly as possible, demanded:"
    me "Maybe it's time to tell me what happened already."
    show mi shy pioneer with dspr
    mi "There's not much to tell. Zhenya sometimes takes Lena to the library at midnight, and I'm alone here. I'm not afraid of the dark or loneliness, but tonight..."
    "She shuddered."
    mi "Ten minutes passed after Lena left, and then it started."
    stop music fadeout 4
    me "What started?"
    show mi shy pioneer with dspr
    "Miku blushed."
    mi "I know! It looks stupid, and you're going to think I'm an idiot now, but there were sounds!"
    "Miku wasn't far from the truth - some mysterious 'sounds' looked just that stupid."
    me "What kind of sounds?"
    mi "Scaaaaaaary."
    "Miku opened her already huge eyes even wider."
    mi "Like someone is walking around sniffing!"
    $ volume(0.5, "ambience")
    play sound sfx_7dl["hedgehog"] fadein 6
    "And, as if to confirm her words, there was a distinctive sniffing sound somewhere outside the cabin."
    play music music_list["so_good_to_be_careless"] fadein 3
    show mi scared pioneer with dspr
    mi "AAH! It's them!"
    "I think I was beginning to guess what it was about, but just in case, I clarified:"
    me "Them?"
    mi "Can't you hear it? Those very sounds!"
    th "And that's what they got me out of bed for..."
    me "So don't mind it - it's not very loud."
    me "You could fall asleep."
    "Miku only shook her head."
    mi "That's not all. It's about to stop sniffing and start finding its way into the house."
    me "Huh?"
    show mi dontlike pioneer with dspr
    "The Japanese girl looked at me annoyed."
    mi "There will be walking around the house. And it won't just walk around, but loudly!"
    mi "And sniff so, so!"
    "And in perfect accordance with her words, the very unique stomping sound that only one animal in the universe can make was heard under the windows."
    show mi scared pioneer with dspr
    "Miku was blown off the bed, and she rushed to me and clutched at my hand."
    mi "There! There! Do you hear that? It's going around the house, it's going to eat me!"
    "It looked like it was no game at all to Miku and she was genuinely frightened."
    "And the stomping was really loud."
    "Especially when it moved from the concrete slabs to the wooden planks of the balcony."
    show mi cry pioneer with dspr
    $ volume(1.0, "ambience")
    mi "There! And that happens all night long."
    "She clung to me like a drowning man to a straw, and there was no power in the world now that could unclench the whitened fingers on my wrist."
    "She was shaking all over."
    me "You must understand that you were a bit sour about Olga."
    th "No wonder - I honestly had genuine respect for the girl when I realized what courage it took for her to just get to me."
    "The picture comes to mind - as the cabin door swung open, and the blue-green hair that surged in the moonlight marked the path of the girl who had rushed forward."
    "Forward, only forward, no saving breath, no saving energy, with all her might."
    "Without turning around."
    "The stomping under the windows subsided, and it was only then that I noticed that I was still hugging Miku."
    th "My poor thing."
    "Before I knew it, I was cradling her against my chest and stroking her hair soothingly."
    "And she clung trustingly to me, and it took a few endlessly long minutes for her to calm down a little and come to her senses."
    me "You know what?"
    mi "What?"
    me "There's a wild beast out there. A predator practically."
    mi "Oh, don't."
    "She pressed her forehead against my chest, letting me inhale the scent of hair with subtle hints of eucalyptus."
    me "I will."
    "I decided."
    me "We'll get him."
    show mi shocked pioneer with dspr
    mi "What?! No!"
    "But then two things happened at the same time - there was a stomping sound somewhere to the left of the windows, and I slipped outside."
    stop ambience fadeout 1
    scene bg ext_house_of_un_night_7dl with fade
    play ambience ambience_forest_night fadein 1
    "The night was cut through with a menacing 'fiit-fiit-fiit,' and there was nothing left for the unfortunate Japanese girl to do but follow me."
    "I don't know what language she was whispering in as she followed me-but I didn't come across a word she said in the anime."
    th "Some kind of dialect?"
    me "Hush."
    "I whispered."
    me "If the predator hears us, then..."
    show mi scared pioneer with dspr
    "Miku instantly hid behind me."
    mi "Then it will attack, won't it?"
    dreamgirl "Yeah, right, will attack and bite your tail."
    me "Just keep it down, okay?"
    show mi shy pioneer with dspr
    "Miku was embarrassed, and so she slammed her mouth shut demonstratively, making a motion as if she were closing a lock and throwing away the key."
    "Well, as the pantomime progressed, I finally saw what I wanted."
    "An indistinct whitish shadow with predatory blurred contours, hurtling swiftly across the ground."
    "As the shadow darted past us, it disappeared beneath the hut, and soon a disgruntled snorting could be heard from there."
    me "Miku, stay here in the lighted area."
    "I ordered."
    show mi surprise pioneer with dspr
    mi "But..."
    me "Miku, just don't argue, okay?"
    "I put my finger on her lips without too much tenderness."
    me "I'll go to the other side of the cabin, and you, when I give the signal, start stomping loudly."
    "It was noticeable how scared the girl was - but it was nowhere near what would happen if she did get pinched in the dark."
    "She'd argue more and more, swear, say something about how we should never be separated."
    "At any rate, that's the reaction I expected from her and I wouldn't have been the least bit surprised by it."
    th "She's a girl. And all girls are terrible cowards."
    "But something completely different happened-as if from the depths of her consciousness a doomed determination and -trust came to her face. To the point of selflessness."
    "Miku nodded curtly and let go of my hand."
    mi "You just yell louder, okay?"
    "In a trembling voice she asked."
    "The beautiful lady overcame her fear and trusted her knight. Trusted him and in him."
    "And that means I have no right to let her down."
    th "Whoever said that, I never would have believed it. And what a loud, pathetic thing to say."
    dreamgirl "And what a fool you are, loud and pretentious."
    dreamgirl "Or should I remind you what language is spoken in the world of seventeen-year-olds?"
    th "No, but the reasons..."
    dreamgirl "Do you care about reasons?"
    "The whole time I was trying to move silently around the cabin, I could feel the stares escorting my back."
    "And I couldn't stand it - I turned around."
    "Miku was smiling desperately, trying her best to show she wasn't afraid."
    "And that's where neither the stage present nor the past, where your name is 'Desperate Miku,' helps."
    "You either entrust your life and safety to a man, and that sounds more eloquent than all the words in the world."
    "Or you don't."
    play sound sfx_7dl["hedgehog"] fadein 0
    hide mi with dissolve
    "My eyes tingled, and thanks be to Random, I was able to hide behind the 'barrel'."
    "There was a familiar stomping sound from under the cabin - despite my best efforts to move silently, my would-be prey had smelled me."
    "It was counting in seconds; if she jumped out at Miku, I'd be screwed."
    "I've inhaled as much air as I could."
    stop music fadeout 3
    me "Miku! Begin."
    play sound sfx_7dl["miku_stomping"] fadein 6
    "There was a noise on the other side-Miku was beating the concrete slabs with her heels diligently and as hard as she could."
    "I, on the other hand, froze."
    "Seconds went by, and..."
    "Finally the noise of distant paws was replaced by the noise of approaching paws."
    "My cunning plan was definitely starting to work."
    "And..."
    play music music_7dl["catch_the_hedge"] fadein 2
    scene cg d4_mi_hedgehod_7dl at fast_running
    with dissolve
    "From the dark gap beneath Lena and Miku's dwelling, the rounded, predatory shadow, for whose sake I was standing here, burst into the moonlight."
    "Taking a deep breath, I took a low start and accelerated."
    "It's always been fun catching up with the buses - and that's been the only way to get me to switch to running for the last few years."
    "There's this respectable gentleman walking down the street, in a coat, with a player, with a smart face - and then he switches to running, and in slow motion you can see his cheeks start to shake, his belly starts to ripple, his thighs start to shake."
    "Total ugliness and no solidity."
    th "But there's none of that here, is there? And no one can see me."
    "Thought I, trying to ignore the stab in my side that had already appeared after ten seconds of running - after all, sports were not the strong point of even a renewed body."
    dreamgirl "Suppose you catch up with him."
    "Because of the jolting and stomping, the eternal visage's ingratiating voice came in jerks."
    dreamgirl "What are you going to catch him with, smart-ass? With your mind? Or..."
    "The venom in his voice could have poisoned an entire whole river."
    dreamgirl "With your bare hands?"
    "My mind wandered."
    th "And really, with what?"
    "The mind ran through a hundred options, one more fantastic than the next, from stretching lianas to emergency digging, and stalled."
    th "Unless..."
    dreamgirl "Yeah, you're absolutely right."
    th "But if I fall, then..."
    dreamgirl "Listen! Do you want to catch a predator or do you want to keep your belly intact?"
    "I couldn't argue with that logic."
    "And anyway, find me a jerk who would argue with his own inner voice - no matter how lewd and obscene it was."
    "With a sigh, I pulled off my tie and crumpled it up and hid it in my pocket."
    dreamgirl "Hurry up! You'll lose the prey!"
    play sound sfx_slavya_run
    scene bg ext_musclub_night_7dl at fast_running
    with dissolve
    "I raced past the washbasins, through a small grove, and finally made my way toward the music club, hushed in the night."
    "And though I was moving much faster than the prey, I had to stop now and then to look for a bright silhouette in the darkness."
    play sound sfx_7dl["breath"] fadein 3
    "But there was no hiding place for the prey here - it raced like a cruiser, leaving behind a conspicuous plume of unfurling grass."
    "If it weren't for one problem."
    "Like that Achilles and the tortoise problem, I've given too much of a head start, and if I don't think of something as quickly as possible, it'll all be for nothing - the raptor will get to the clubhouse, and..."
    "I unbuttoned my shirt on the move and accelerated as fast as I could, not listening to the stomping and shouting behind me, all aimed at one point."
    play sound sfx_jump_into_hole_2
    "And, choosing the maximum speed in my protesting legs, I pushed forward, stretching out in a leap that would have been an honor to Yashin himself."
    "A dream of flying. Without wings or blades, without jet turbines or other technological crutches."
    "In my hands a white sail slammed the canvas, and..."
    play sound sfx_bodyfall_1
    scene bg ext_musclub_night_7dl with dissolve
    "I landed straight on my belly, skidded forward, skinning myself, and finally covered my prey with my shirt - the distance was reduced to a minimum."
    "There was an immediate indignant snorting and muttering underneath."
    show mi surprise pioneer with dspr
    stop music fadeout 6
    mi "Sem? Senechka? Are you all right? You ran off somewhere, and I got scared, and I ran after you, and suddenly you fell, and I realized that you didn't fall, but jumped! You didn't hit yourself?"
    "Miku, who had caught up with me, rambled on, holding out her hand."
    th "Except I was lifted out of bed and made to do track and field instead of sleep? Oh, of course."
    me "I did. But that's nothing. The important thing is my prey, I got it!"
    "I nodded at the completely independent shirt walking in circles, stomping and sniffing."
    show mi scared pioneer with dspr
    mi "What's inside?"
    play music music_7dl["breath_me"] fadein 6
    "Whispered Miku."
    me "The same scary beast that walked in circles around your cabin."
    show mi shy pioneer with dspr
    mi "What's the beast?"
    "Rolling my shirt up in a sack, I lifted the prey in my palms and flipped it over, showing the Japanese girl the prickly ball."
    me "A common hedgehog."
    me "Popularly known as the mean spiny hedgehog."
    show mi smile pioneer close at center with dissolve
    mi "So small? How did he stomp so loudly?"
    me "He walks like that. It's like he's always stepping on his heel."
    "Now that the chase was over, all I wanted to do was go back to my cozy bed and snooze for three hundred minutes."
    "A gust of wind licked my wet back, and I shivered, remembering suddenly that I was still bare-chested."
    mi "What are you going to do with it now?"
    "I shrugged."
    "Somehow this is the first time I've ever had to catch a hedgehog, and I have no idea what to do with it next."
    me "Yeah, I'll let it go, I guess. I don't think anyone in camp wants a pet that snorts and stomps loudly at night."
    show mi laugh pioneer close with dspr
    mi "That's right, that's right. Let's take him off the territory."
    "The fence was a stone's throw from here, so I didn't even have to pick a direction."
    "The hedgehog was still in my hands, curled up like hedgehogs do in moments of danger, stabbing my fingers lightly through my shirt."
    "It was only now that I noticed how quiet and warm the night was all around me."
    show mi smile pioneer close with dissolve
    "Happiness can be measured, if you try hard enough."
    "Thousands of hours together, pounds of salt eaten together, the depth of nail marks on the palms of your hands."
    "The number of children planned, finally."
    "Although, in fact, my happiness personally is and has been measured in the number of words spoken per conditional unit of time."
    "I didn't get Miku to talk in machine-gun mode, but rather in short bursts. {w}Just because I happened to be the first one who didn't grab his head and run away in terror."
    "And since she does - I know that if she is gibbering - it means she has snapped and stopped 'pulling her back,' controlling her own speech."
    th "For example, from fear."
    play sound sfx_hiding_in_bush
    scene bg ext_path_night with dissolve
    th "Or from worry."
    "The bushes rustled, letting us through to the gate leading outside the camp."
    th "Or excitement."
    "I squatted down, shaking the predator out onto the grass - it rolled like that in an untrusting ball."
    "And, unbending, I froze - confronted with the wet, flickering gaze of a Japanese girl."
    show mi shy pioneer with dspr
    mi "You are like a samurai, unafraid and unconcerned, defending the needy."
    th "Samurai? Koto mitsuketari?"
    dreamgirl "She called you her faithful knight, retard!"
    show mi normal pioneer close with dspr
    "She took a step, finding herself close to me."
    mi "I wasn't sure if you would help, but I had no one else to go to."
    mi "And you helped."
    "She took another tiny step."
    show mi normal pioneer close:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 1.0 zoom 1.15 xalign 0.5 yalign 0.5
    "And another."
    show mi normal pioneer close:
        xalign 0.5 yalign 0.5 zoom 1.15
        linear 1.0 zoom 1.3 xalign 0.5 yalign 0.5
    "And I felt her body heat coming through my shirt with my naked breasts."
    mi "Thank you."
    "She rose on her tiptoes, kissing the corner of my lips."
    "And she put something in her hand, pressing her fingers together with force."
    mi "You're a miracle."
    "She whispered."
    hide mi with dissolve
    "And disappeared."
    "And I unclasped my hand and thoughtfully discerned a braided bracelet, a kumuhimo, in which the iconic blue-green ribbon was woven over the red threads."
    "Miku's colors."
    if alt_day2_mi_kumuhimo == 2:
        "I found it for her - and she gave it back."
    th "Well, the lady of the heart gave her knight a ribbon of the family color."
    th "So the beast was not defeated in vain."
    "After pushing the hedgehog, clearly intent on returning to the grounds, with my foot, I went in and closed the wicket behind me."
    "I intended to finish my due - even if I had to entrench in the cabin!"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_dj_morning:
    scene black with dspr
    play music music_list["my_daily_life"] fadein 5
    if alt_day4_mi_dj_hedg:
        voice "Semyon! Get up! Semyon!"
        "I think that was the moment."
        "I suddenly realized, oh, I assure you, realized the full meaning of 'willing to kill for a few minutes of sleep.'"
        scene bg int_house_of_mt_day
        show mt normal pioneer
        show unblink
        "However, it didn't seem like our leader could be affected by things such as a wicked look, because she smiled and nodded in satisfaction."
        mt "Come on, get up, there's a inspection coming here in half an hour, so you've got plenty of time to pack and have breakfast."
        me "Inspection?"
        mt "And I don't want to see you until lunch."
        mt "Not you, not Miku, not your goddamn hedgehogs. Got that?"
        "She scurried around the cabin, scavenging in between drawers for all the picturesquely arranged junk around the cabin, from the underwear items that were hung on the headboard without remorse, to some obscure jars and an enormous hammer under the bed."
        "The only way to hammer crutches on the railroad tracks is with these."
        dreamgirl "No, she uses it to stroke the heads of negligent pioneers. {w}So it's in your best interest to get up there and do as she says."
        me "Mm-hmm."
        "I answered meaningfully with my mouth full - there were a couple more sandwiches and an apple on the table waiting to be served - and, buttoning my shirt as I went, jumped out into the street."
    else:
        scene bg int_house_of_mt_day
        show unblink
        "I slept well, though I slept through the whole world - a glance at the clock informed me that it was the beginning of eleven, and Olga Dmitrievna never managed to wake me up."
        play sound sfx_open_dooor_campus_1
        show mt normal pioneer with moveinleft
        mt "I see you're awake already? And I brought you something to eat."
        "Olga put a plate on the table and looked around the room."
        mt "This place should definitely be cleaned up."
        th "Let me guess who's going to do it."
        mt "You don't have much time, the inspectors will be here in half an hour..."
        th "Well, I told you! I've been put on duty, just as I feared."
        mt "So get up in a hurry, eat, and don't show up anywhere before lunch. Got it?"
        dreamgirl "You ain't gonna be no Vanga, son."
        th "Yes, yes, sat in silence until the last to gloat now."
        "After waiting for Olga to turn away, picking up the bras and socks hanging from the headboard, I frantically jumped out of bed and hopped on one leg, getting into my shorts."
        mt "Miku was asking for some help last night."
        me "Yeah, I know. I'll go find out what she wanted."
        "After buttoning my shirt, I went outside."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_dj_day:
    scene bg ext_houses_day with dissolve
    play music music_list["smooth_machine"] fadein 5
    "Well, hello there! Hello!"
    "My fourth day in unsuspecting paradise with the camouflage blood on my shoulders, my third day of lost peace for the girl-sea."
    "The old, hackneyed scene - when two lovers lie on their backs nose to sky, ear to ear, head to head."
    dreamgirl "What did you feel when you first met me?"
    th "And what did you think when you realized I wasn't going to let go so easily?"
    th "Yeah another one of those platitudes along the lines of... uh, you go first."
    dreamgirl "Whatever you say. I've decided that here's another interesting boy who will get tired of both my trying to be myself and my trying to be unobtrusive and interesting all too quickly."
    th "I've decided that here she is, another very pretty girl who will never be interested in me - as trite as it sounds - for the reason that I'm a rather boring character."
    dreamgirl "And you pretended to be a little more interesting than your usual self?"
    th "And you pretended you didn't know what it was to bore anyone?"
    dreamgirl "Couple of years, two freaks. Semyon, tell me, I'm the one playing her part now, do you really think she would say the same thing?"
    th "The hell she does. Miku is a very clever girl and she recognizes falseness at once."
    dreamgirl "But she seems to like you, so she's perfectly capable of letting you get away with some things."
    th "In that case, the main difficulty will be distinguishing between forgiven and taken for granted."
    dreamgirl "Don't you just want to live in peace?"
    scene bg ext_square_day with dissolve
    "I turned into the square, dodging a flock of some unfamiliar pioneers on the way."
    th "In peace? What peace?"
    if herc or loki:
        th "Until I got to this crazy place, no extraneous voices sounded in my head, so I don't know if you know, but just in case I remind you:"
    if loki:
        th "My present world is sitting around in the government office from nine to six, with the prospect of promotion and sitting from eight to seven, or even until eight."
        th "And in my spare time, a voluntary confinement in the Castle of Silence, where I am powerless to squeeze out even a note, even though my fingers sometimes bleed music!"
        th "And all I have is a bloody twenty-four-inch window leading into a world of refined and prepackaged 'hello.'"
    elif herc:
        th "My world is an incredibly exciting job as a two-by-two security guard, with blighted prospects and a wolf's ticket to the business world."
        th "I used to write poetry, and judging by how eagerly it was published, it wasn't the worst in the world. Stories that made readers laugh, cry, empathize."
        th "And that makes it three times as creepy to sit for hours, fingers ready to fly in an endless dance over the keys, and not be able to squeeze out a single line."
        th "That's all that's left is to burn through the moment, letting life drain away into the gray-orange solution of the energy vampire of the anonymous boards."
    else:
        th "My world still consists of working as an undesigner at a shitty newspaper with no room for growth, either personally or professionally, and for which I'm paid in a way that I'd rather not be paid."
        th "And the creepy thing is, I'm fine with it."
        th "I've forgotten how to want. Living before as that futuristic gravitational glider traveling from star to star, I'm used to setting microscopic goals, minimal goals, insignificant milestones."
        th "And should I be surprised that in a succession of little-noticed accomplishments, somehow that very fragile, infinitely blue feeling that used to make me wake up and take my first breath has been completely lost?"
        th "And without it, setting goals for yourself, some of your own desires, means nothing at all, and also burdens you as if it were some unpleasant, boring job."
        "I wanted a promotion, I got one; I wanted to upgrade my computer, I did; I wanted to move out of my apartment, I moved in. That's it."
    th "How far do you think Miku would send me if I offered her these prospects as possible consequences of living with me?"
    th "I offer you hand, heart, wallet, and complete stagnation until death sets us free."
    dreamgirl "You're such a downer."
    scene bg ext_clubs_day with dissolve
    pause(3)
    stop ambience fadeout 2
    stop music fadeout 6
    play sound sfx_open_door_clubs
    pause(1)
    scene bg int_clubs_male_day
    show el normal pioneer
    with dissolve
    play ambience ambience_clubs_inside_day fadein 3
    stop music fadeout 6
    th "Yeah, a bit."
    "I agreed, shaking Electronik's paw."
    me "Hi. Where's your buddy?"
    el "He's in the infirmary."
    me "Is it something serious?"
    "He just shrugged his shoulders."
    me "I see, I see. Well, I'm here for Miku, is she there?"
    "I shook my head toward the backroom."
    el "Yeah."
    me "See you then."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_dj_radio:
    scene bg int_clubs_dj_7dl
    show mi normal pioneer at center
    with dissolve
    "Miku looked disheveled, her face wrinkled, her hair a little disheveled - apparently the lack of sleep during the night had taken its toll."
    "Though her eyes burned with a feverish gleam and her cheeks were flushed, the girl seemed to have found something to enjoy."
    mi "Hello again, my favorite camp!"
    "The microphone picked up her voice and, converting it to electricity, immediately spread throughout «Sovyonok»."
    mi "It's noon on the clock, the temperature outside is heavenly, which means it's a good time for everyone free of duty to go for a swim - which, unfortunately, cannot be said of me."
    "She noticed me and greeted me with a nod, continuing to chirp into the microphone."
    mi "But I can give us all a musical greeting to lift our spirits, and that would be..."
    "A vinyl record spun in my hands and, blowing off the dust, the Japanese girl read:"
    mi "Andrei Makarevich and «Mashina Vremeni»!"
    "The first chords flew into the airwaves, and Miku, turning some kind of knob, finally gave me a little attention, too."
    mi "Hello, Senechka! Did you come by to check on me?"
    me "Actually, I was looking for you."
    show mi surprise pioneer with dspr
    mi "Looking? Why?"
    me "Just so."
    "I smiled."
    me "I was a little worried about you after the night's events."
    if alt_day4_mi_dj_hedg:
        show mi shy pioneer with dspr
        mi "Everything was fine! You defeated the scary snorting monster, and I slept like a baby till morning."
        mi "Thank you so much for that."
        me "Yeah."
        "On my cheek burned a scalding warmth from an awkward, inept Japanese girl's kiss."
    else:
        show mi normal pioneer with dspr
        mi "Oh, no, the problem solved itself."
        me "Speaking of the problem - what was there?"
        show mi shy pioneer with dspr
        mi "It's no big deal. It's nothing."
        me "Are you sure?"
        mi "Yes! It was solved without my involvement."
        "I found that hard to believe, but I didn't insist: if the girl wants to lie, who am I to stop her?"
    me "How are you doing anyway?"
    show mi normal pioneer with dspr
    mi "All in all nothing, I've made it like my studio at home here, look."
    mi "There! As if I knew it would be needed, I brought a spare mixer with me."
    "Miku lovingly stroked the tiny black square console with a bunch of switches."
    mi "Look: here's the input from the jukebox - it's left in the canteen for now, they don't trust me."
    show mi serious pioneer with dspr
    "Miku frowned for a moment and then immediately, shaking her head, continued her description:"
    mi "The microphone - well, I guess you guessed it. The inputs are from a tape recorder and a record player."
    me "Is there a channel for a third-party signal source?"
    show mi laugh pioneer with dspr
    mi "Of course there is! Do you have something to plug in?"
    me "As a matter of fact I do."
    if alt_day2_minijack:
        "I haven't had a chance to listen to music lately, so why not let the rest of the charge go to good causes?"
        "I unclenched my palm, showing the girl the player's rectangular slab."
        show mi happy pioneer with dspr
        mi "It's so miniature! Where did you get it?"
        "Clapped her hands."
        me "Uhhhh... You can think of it as an experimental model."
        "Carefully looking away, I replied."
    else:
        me "Only I don't know how to plug it in."
        "Immediately I warned, taking the player out of my pocket."
        me "I mean, purely theoretically, cyberneticists might as well have the right plug."
        dreamgirl "Or you could ditch the headphones and get a guaranteed working input."
        th "You know where you should go with ideas like that?"
        dreamgirl "Then go bow to Curly."
        show mi normal pioneer with dspr
        mi "Try asking Elektronik, he's supposed to have something."
        me "Okay."
        play sound sfx_open_door_clubs fadein 2
        scene bg int_clubs_male_day
        show el normal pioneer
        with dissolve
        "Electronik was sitting in the same pose as the last time I saw him - he never seemed to straighten his back - and looking at him, I unconsciously squared my shoulders myself."
        "Damn empathy."
        me "Electronik, my friend, I have a favor to ask of you."
        el "What?!"
        "He flinched in surprise."
        me "Easy, easy, it's only me."
        "Calmly I raised my hands in front of me."
        me "You don't seem to be yourself. What's wrong?"
        el "I don't know. But I can't get rid of the impression as if something heavy were pressing down on me, pressing and pressing!"
        me "Pressing?"
        show el upset pioneer with dspr
        el "Never mind! What do you want?"
        me "I'd like a three millimeter input, a eurolink, would you look at it?"
        el "Look in the acoustics."
        "He wiggled his chin toward the box on the cabinet."
        el "If I'm not mistaken, we had some in there."
        me "Okay."
        "Pulling down what turned out to be a pleasantly weightless box on the table, it took me a few seconds to find a condensed mini jack, a pin, in a cloth sheath."
        dreamgirl "Yeah! Not unlike your plastic stuff! This, brother, is a technology on the verge of immortality."
        th "Bordering on fantastic, you mean?"
        dreamgirl "What kind of fantastic! You can hammer nails with it, it's not fantastic!"
        me "Thank you very much."
        "I closed the box and put it back on the cabinet."
        "Electronik guy just waved it away."
        "With a shrug, I returned to the radio room."
        play sound sfx_open_door_clubs_nextroom
        scene bg int_clubs_male2_night
        show mi normal pioneer with dspr
        "Miku turned at the noise of the door opening and looked at me questioningly."
        me "Here."
        "I handed her the Walkman with the plug."
    me "There's a couple of things in there that I think you might like... And then, what the heck, you might even put into rotation!"
    mi "What's in there?"
    me "In a nutshell, it's all kinds of vinaigrette. But I'd like to listen to something timeless, so no pop or music with lyrics."
    "After poking around the menu for a while, I finally found the track I was looking for and put it on."
    "Miku instantly balanced the volume and smoothly changed from Makarevich to what I had put on."
    play music music_7dl["will_you"] fadein 6
    "Over the heads of the pioneers, the staff, and the counselors pierced the sunlit afternoon with the sound of music that would last forever."
    "A seemingly simple tune, not hard to play on the piano, it willy-nilly touched something in the soul, something that had been ridden to tears during periods of worsening depression."
    "Hell knows where I'd be and what I'd be turned into if it weren't for the music."
    "And I think back to my childhood, high school, and music, a subject I always excelled at. I had no problem with solfeggio, theory, names of composers and their life stories, classics, works."
    "But at some point it was like I left the orbit of understanding - I don't remember the exact name of the course, but it was something like 'I want to see music.'"
    "To see."
    "God, what a load of crap."
    show mi smile pioneer with dspr
    th "She's smiling. She seems to like it. No wonder."
    "You can't see the music. {w}It can't be visualized, and all those screensavers with geometric shapes and chaotic spots are like the same color radio that still won't bury television."
    "You can hear the music. Feel it. You can feel it with a shiver in your chest, a jolt of bass if you're not too lazy to stand up to the speakers, a hitched breath and moisture on your cheeks if it's really strong, this music."
    "But how can you see the music?"
    "Hell if I know how I managed to fool our teacher, but I was the one who ended up going to the Olympics from school."
    "And they brought us to some class, sat us down, handed out sheets of paper and pens, and turned on a song and told us to write how we saw the music."
    "As it's fashionable to say now - it was a cover, or remake, of the good old French 'Je suis malade.' Performed by Lara Fabian, of whom I knew nothing at the time."
    "And I was dead. Missing."
    "It was like being thrown into an ice hole - for the entire three-plus minute performance I forgot how to breathe, I sat there and caught unfamiliar notes, incomprehensible words."
    "What 'see' were you talking about, anyway!"
    "I wrote. Everything I saw. Everything I heard."
    "This song is about love, I wrote diagonally on the sheet."
    "Later, there will be an album and concerts where I have personally witnessed - reach out and touch - but the moment of infection I marked quite clearly."
    "The virus got into my blood, into my life, and changed something in me."
    "It wasn't until I was a few years older, one heartbroken adult, and one forgiveness wiser that I realized what 'seeing music' was all about."
    "When there's a fog running down my hair that never turned into rain, and there's the same leaden, gloomy mess going on inside..."
    "...when the easiest and most obvious way out seems to be to swallow pills, go out the window, jump off a bridge, get hit by a torn high-voltage wire, get hit by a streetcar and be vaporized on a viaduct by an explosion of a gas station built in circumvention of all the rules..."
    "...when all there is is you, the rain, Petersburg, and the narrow loopholes of your eyes, through which your battered despair is aroused upon the world..."
    "You push your foot off the asphalt and spread your wings, piercing the gray haze on your shoulders with yourself, you run with the speed of a sports car, you do not care about the icy vacuum of space and the unhurried dripping of seconds."
    "You meet out of the endless autumn a man you haven't seen in millions of years, and from the embrace you have nowhere to breathe, you stand alone against dozens of opponents, invariably defeated, you step out of your own body with your gaze into the sky and, reflected from the clouds, you get inside one who has waited all her life for you alone."
    "You are like a god in that moment, you are like the whole world."
    "And yes."
    "In that moment you {i}see{/i} the music. Because the feelings it awakens in you are a hundred times more vivid than what deceives your senses, claiming to be real."
    show mi serious pioneer with dspr
    stop music fadeout 6
    mi "Whoa! That was strong."
    "She admired."
    mi "And you got a lot of that?"
    me "Less than I'd like, to be honest."
    "I answered."
    me "There's a couple more things I'll be sure to introduce you to, thanks for putting it up!"
    mi "Nonsense! Ask me anytime."
    play sound sfx_knock_door2
    "There was a polite and extremely courteous knock on the door."
    show sl normal pioneer at right with dspr
    sl "Miku, are you free?"
    "Slavya went inside and looked around."
    sl "Wow, what a place you've got here! Even looks a little lived in."
    me "We tried!"
    "I answered proudly."
    th "It's so Miku won't have any grief."
    "I wasted a lot of time yesterday before the radio host candidacy was even decided, and now I'd like to put some rugs and some flowers and doilies in here."
    me "Not to put our celebrity in a viper house!"
    show sl smile pioneer
    show mi laugh pioneer
    with dspr
    "The girls both laughed out loud."
    sl "I agree! But I'm here on business."
    th "Who would doubt it - our activist didn't have the time for normal visits!"
    show sl smile pioneer with dspr
    sl "Miku, you, as a radio broadcaster, are given a party assignment: you must make an announcement over the camp communications."
    "She rummaged in her pockets and, pulling out a piece of paper, began to read:"
    sl "Dear guests of the camp! At five o'clock we invite you to an amateur concert."
    sl "Have them come to the stage by then. Can you do that?"
    show mi normal pioneer with dspr
    mi "Yes, of course!"
    "Miku switched the main signal to the microphone, and she spoke quickly, quickly, in her own style."
    "And the amazing thing was that what in normal life seemed to be a kind of extremely annoying noise, from which only with a lot of effort could one extract coherent words and thoughts, here and now on the radio waves was something..."
    "I don't even know what to call it: native? Relevant? Right?"
    "Whatever you want to call it, to my ear that fluent cheerful and cheerful recitative was like a message from my homeland, a kind of greeting from the banks of the Neva."
    th "Perhaps that's the only thing I'll miss if I'm stuck here after all."
    dreamgirl "That's it? What about moms-dads-friends-acquaintances?"
    th "Oh, yeah, I'm going to miss my friends especially. It's like that joke - what grief, pour me a BLACK beer."
    "I suddenly realized exactly what it is that confuses me."
    me "Guests? What are you talking about, Slavya?"
    show sl smile pioneer with dspr
    sl "It's Parents' Day."
    "She brushed it off serenely."
    sl "And some kind of inspection, I didn't find out exactly yet."
    "Miku had just finished her machine-gun speech by then, so the attention went back to her."
    sl "Oh, thanks, Miku, I owe you one!"
    hide sl with easeoutright
    "Slavya dazzled us one last time with a smile and hopped off on her Incredibly Important Business."
    mi "Senya, may I ask you something?"
    me "Any whim for your money!"
    "I answered."
    show mi smile pioneer with dspr
    mi "You won't even ask me what I want to ask you?"
    "I shrugged my shoulders."
    me "No. Should I?"
    show mi laugh pioneer with dspr
    mi "Well, I'm going to tell you now anyway!"
    me "Amazing, isn't it?"
    mi "What?"
    me "So what did you want to ask?"
    show mi normal pioneer with dspr
    mi "I have to go out for half an hour, can you cover for me?"
    me "Uh... I'm not really sure."
    show mi sad pioneer with dspr
    mi "So you won't help?"
    "The girl seemed a little upset, and I hurriedly raised my palms in front of me, reassuring her."
    me "Hey, hey! I didn't say I wouldn't help! But I'm really not going to be able to switch you... right now. Do you understand?"
    mi "Oh, you mean that... Well of course I'll tell you what and how works here! Come here."
    "She picked up the stool I was sitting on with her foot and pulled it toward her."
    mi "You're already familiar with the mixer."
    "The Japanese girl impolitely jabbed her finger at a miniature square remote with a bunch of sockets."
    mi "All you have to remember is the location of the channels. The first two are occupied by the tape recorder."
    me "Two? Why not one?"
    mi "It's a long explanation, just mark it off somewhere in your mind, okay?"
    "I nodded."
    show mi smile pioneer with dspr
    mi "Excellent. Moving on. Channel three for the gramophone. Look."
    "Twisting the spring-loaded dial, Miku pulled a postcard from the top drawer of her desk with a landscape in which I recognized the view of the river, with gold embossing - an owl inscribed in a circle and fancy letters emblazoned on the perimeter."
    th "POL GDC «Sovyonok»."
    "I read."
    mi "Look."
    "She whispered."
    mi "They haven't played records here in a long time, but my father told me..."
    play music music_7dl["ltyh"] fadein 6
    "Blowing hard on the corner of the cardboard, Miku placed the sharp edge on the track, and a barely audible intro echoed in the room, where Marie Fredriksson's vocals blended in seamlessly."
    th "What, this song, already being sung at this time?! Wow!"
    dreamgirl "You've got a lot of old stuff in your collection."
    show mi happy pioneer with dspr
    mi "Do you like it? It's very fresh, they gave it to my father during a trip to Scandinavia, this ensemble is very popular there!"
    me "Very much... I like it."
    "Old as the world call to listen first and foremost to the most important advisor - your own heart."
    "Eternal, never outdated advice - even if you think the struggle is pointless, even if all the best is washed away by the tide, just..."
    "And I rang out:"
    me "Listen to you heart! When he's calling for you…"
    show mi surprise pioneer with dspr
    mi "You know this song?!"
    "I think I managed to surprise her. Not much merit - with all that naivety in her eyes."
    mi "Oh well."
    "She pouted, taking the pouting card off the record."
    mi "And I thought it was a new song!"
    me "It is new... But we got distracted."
    show mi smile pioneer with dspr
    stop music fadeout 6
    mi "Yes!"
    "Withdrawn, Miku responded."
    mi "Channel four is for the mic, channel five is for your player. I haven't put anything on the other three yet, but there might be a horn."
    mi "Here are the volume controls, here's the timbrel, here's the six-band in case you think the range is skewed."
    mi "Although with the local loudspeakers, it's not critical."
    mi "That's it, I'm out of here!"
    me "Wa..."
    play sound sfx_open_door_kick
    pause(1)
    hide mi with moveoutleft
    me "…it."
    "I turned to the empty air - Miku had flown away, no moment had passed."
    "I had to take the lead."
    th "One of two things - either I slow her down to my level, or I speed up to hers."
    th "I can't communicate with a person who exists in opposition to me!"
    dreamgirl "So, speed up! You like the girl, don't you?"
    th "Well, it's not that..."
    dreamgirl "What, you don't like her?!"
    th "Hey, I didn't say that!"
    dreamgirl "Of course you didn't. I know you better than you what's going on in your head."
    th "And what's going on in there?"
    dreamgirl "What's going on is that you're in love, sir."
    th "What?! With her?! What do you mean?"
    dreamgirl "That's exactly what's going on, for good and for ill. It's a worldly thing."
    th "Are you gonna make fun of me again for liking it or not liking it?"
    dreamgirl "No, why? Your behavior is peculiar - to begin with at least going to the washrooms yesterday {i}because Miku might not like the smell{/i}."
    th "That's it?"
    dreamgirl "Do you need more? Be my guest."
    "{i}The image of a leisurely drooping eyelid{/i}."
    dreamgirl "You looked for her. You walked all the way across the camp to her - notice, instead of looking for answers to questions, ducking girls, participating in camp life, or helping Olga Dmitrievna clean up the cabin!"
    dreamgirl "What's more, your first thought upon waking up was of her - what's more - all through your sleep you were squeezing a certain blue-haired Asian girl with suspiciously familiar facial features."
    dreamgirl "And now you're sitting there a little out of place, sure as hell that you're going to screw up."
    dreamgirl "Don't forget, I have access to all your thoughts and memories."
    dreamgirl "And you still didn't jump up, catch up and put the girl back in her place?"
    th "That kind of relationship is called friendship and reciprocity."
    if alt_day4_mi_dj_hedg:
        dreamgirl "Is the kissing part of it, too?"
        dreamgirl "You had a lot of trouble not turning your head."
        dreamgirl "Or is kumuhimo also a sign of friendship?"
    else:
        "My intuition did not share my optimism."
    "And I didn't have time - the reel signed 'OD, at least once an hour' clicked, rewound, and I tried to fade it out with the look of an inveterate presenter."
    play music music_list["blow_with_the_fires"] fadein 3
    "The bourgeois music was replaced by the call to the Soviet heart, 'Blow with the Fires!'"
    "Behind the wall there were voices arguing, the door swung open..."
    play sound sfx_open_door_clubs
    stop ambience
    scene bg int_clubs_dj_7dl
    show dv normal pioneer2
    with dissolve
    "On the doorstep stood Alisa in all her glory."
    "Her outfit reminded me of the first day we met-the same hooligan knot under her chest, the same tie that had migrated to her right wrist as a wristband."
    dv "Where's that upstart?"
    me "Which one?"
    dv "You know, the Hatsune one."
    me "Why is Miku the upstart?"
    show dv angry pioneer2 with dspr
    dv "What do you care?"
    "She screeched."
    dv "I'm here to see her about business. But since she's not here, I'll do it myself. Move on."
    me "I wouldn't think of it."
    "Letting Dvachevskaya have access to Japanese equipment was a scary thing to think about!"
    show dv rage pioneer2 with dspr
    dv "Are you stupid? I said move."
    "Alisa was slowly but surely boiling over, and for a moment I felt out of place."
    "Hell if I know, in my old life I wouldn't have messed with a psychotic woman - I'd have gone around her in a cold, roundabout way."
    "Unfortunately, I was bound here, and the saddest part was that I really didn't want to let Miku down."
    th "Well, looks like somebody's going to get hit now."
    "I sighed, getting between Alisa and the equipment."
    dv "I'm giving you one last chance to get away on your own."
    "Alisa hissed, glaring at the bridge of my nose."
    me "Calm down, why are you getting so worked up? Tell me, what do you want?"
    dv "I want you out of my way."
    "In a dull voice Alisa notified."
    me "Or what? Are you going to complain to your mother?"
    "I think I've walked on personal - so darkened was the redhead."
    dv "Nothing."
    "I didn't have time to understand or be frightened, though - with a knack that surprised me, she crouched down a little, pulling her shoulder back, and..."
    with flash
    play sound sfx_lena_hits_alisa
    "That hurt."
    "Tears spurted from my eyes all by themselves when Alisa's hard little fist hit my nose."
    th "It hurt, damn it! Did you get it all raspy or something?"
    dreamgirl "It doesn't look like it, you're breathing evenly."
    "A dark drop fell on the floor."
    dreamgirl "Oops."
    dv "Did you like it? Do you want more?"
    me "No."
    dv "Then stand back."
    "I've never fought a girl in my life."
    "I had to swing my fists, of course, but fighting with a girl, no matter how aggressive she was... As in the popular wisdom: If you win, you're a scoundrel, if you lose, you're a wimp. It's bad everywhere."
    if herc:
        "Luckily, my skills in dealing with rude people haven't gone out of my messed-up head."
        me "Don't even get your hopes up."
        "And on the second blow, I managed to react, clawing Alisa's arm behind her back."
        "She squeaked and tried to pull away, but from that position she only hurt herself more."
        me "I feel the strongest urge to hit you right now. You have no idea how much."
        "I hissed in the redhead's ear, noticing with displeasure how the scarlet spray stained her neck and soaked into her shirt collar."
        me "But unlike you, I don't hit someone who can't hit back."
        me "Though you do practically beg for a light jab in the kidneys."
        hide dv with dissolve
        "Swinging the door open with my free hand, I pushed the redhead out of the room and sat down, head thrown back toward the ceiling."
    elif loki:
        me "One more move, and I'll announce to the whole camp about both your cigarettes and the stash under the cabin."
        show dv surprise pioneer2 with dspr
        dreamgirl "But where did you..."
        dv "Where did you..."
        th "Stereotype. Bully, sociopath - either smoking, drinking, or dabbling in drugs. Which means there must be a stash."
        me "Unlike you, I have a good chance of getting the truth out to the people."
        show dv angry pioneer with dspr
        dv "You wouldn't dare."
        me "Neither will you. That's where we stop."
        "It was frightening to look at Dvachevskaya - to the extent that she was enraged and at the same time trying to pull herself together."
        "Not finding a single argument against her, she straightened up, spat on my shoe, and turned around and walked out"
        hide dv with dissolve
        with vpunch
        play sound sfx_open_door_kick
        pause(1)
        extend ", slamming the door behind her."
        "And I sat with my head thrown back to the ceiling, something cold would probably work better, but it's okay, it's better than pouring blood on the remote control."
    else:
        "I haven't fought since ninth grade - Random was merciful."
        "Maybe it's my spinelessness."
        "But I took the pain, held my punches well, and was never afraid of getting hit in the face."
        "And then like something changed - I got scared shitless of someone else's fist coming at my head."
        "So I almost stepped aside, letting the aggressor pass me by."
        if alt_day4_mi_dj_hedg:
            "If it weren't for a living reminder."
            "A braided Japanese bracelet wrapped around my wrist."
            "I don't know how many blows I can take, I don't know if I can bring myself to hit back."
            "One thing I do know for sure is that Miku has already changed me enough that I just can't afford to back down."
            me "No."
            play sound sfx_lena_hits_alisa fadein 6
            "The second blow to the nose hurt even more - so much so that I almost fell, miraculously holding on to the tabletop."
            me "You can beat me."
            "I didn't recognize my own voice."
            me "But I still won't let you pass."
            show dv guilty pioneer2 with dspr
            "It had the most sobering effect on Alisa - she looked at me in confusion, at her fist splattered with blood - some got on her shirt, too."
            "And without saying a word, she walked out."
        else:
            "Fortunately, I always had a volunteer helper."
            "The same one who failed to restrain Aliska at the entrance. Maybe we can get him to be useful in some other way?"
            me "Electronik! El!"
            "Shouted me."
            el "Yes, Semyon!"
            me "Call the counselor, Alisa has gone crazy!"
            el "You mean how?"
            me "And then we tell him that out of the blue you hit a man in the face. And the next day we judge you in a court of comradeship."
            dv "You can't solve it on your own, so you decided to snitch? Snitch."
            "She spat contemptuously on my shoe and walked out."
        "And I sat down on the stool with my head thrown back to the ceiling."
    hide dv with dissolve
    "The blood should have been stopped as quickly as possible."
    dreamgirl "Sit tight. We'll send for a wet rag when Miku comes."
    th "Do we have to wait for Miku?"
    dreamgirl "Not really."
    el "Semyon, Semyon! What's the matter with you?"
    show el normal pioneer with dspr
    "There's a candidate for a helper at the door."
    me "Nothing a cold compress can't handle."
    el "A compress?"
    me "Yes. Would you be so kind as to find some clean cloth and go wet it."
    el "Coming!"
    hide el with moveoutleft
    "I closed my eyes and began to count the verses of the pioneer hymn, but I didn't get to the middle of the first."
    show el normal pioneer with moveinright
    el "There!"
    "When the time was right, Electronik was as fast as Ulyana."
    me "Thank you!"
    el "Don't you need anything else?"
    me "No. Thank you."
    el "Okay. Otherwise, I'm going for a walk - I've got a headache."
    hide el with dissolve
    "After blessing him with a gracious nod, I found myself alone again."
    "The rag on my nose cooled the bridge of my nose pleasantly, and for a few seconds I seemed to switch off, for I flinched in surprise when the call for dinner suddenly shouted loudly from the mess hall."
    show mi normal pioneer with dspr
    mi "Senechka! Thank you for covering, or else I..."
    show mi surprise pioneer with dspr
    "She cut herself off by throwing herself at me."
    mi "What happened here?! Senechka, answer me, what happened?"
    me "What happened... Nothing. A bad turn, that's what."
    mi "A bad turn doesn't make you bleed like that. Syom, what's the matter?"
    me "Nothing."
    "I touched my fingers under my nose - it was already dry there, the yucca had curdled and was no longer gushing out of me in a stream, and the remaining streaks were easily washed away by the same unfortunate compress."
    me "Let's go eat."
    "The girl nodded obediently and, taking me under her arm, led me out of the clubhouse."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_dj_cleaning:
    scene bg int_clubs_male2_night with dissolve
    $ persistent.sprite_time = "night"
    show mi normal pioneer at center with dissolve
    play ambience ambience_clubs_inside_day fadein 3
    "Electronik muttered something to my back, but I wasn't listening by then."
    "And, as it turned out, in vain."
    "Miku, all wrapped up, sat in the middle of the manmade chaos and rested."
    me "Good morning, sunshine. I was told you were in the backroom."
    mi "Hi."
    "Miku looked at me pitifully."
    mi "If you don't go into detail, that's the backroom."
    "She circled the room eloquently with her hand."
    mi "The broadcasting room... the future broadcasting room."
    me "How on earth! If I'd known they wouldn't even prepare the place for your enthronement, I'd have never in my life..."
    mi "Come on. {w}Somebody had to take all this junk apart sooner or later anyway. Why not us?"
    me "I'd rather it wasn't for us."
    "I muttered to myself."
    mi "What?"
    me "Nothing. Let's share the work front."
    mi "Do you think we can manage with just the two of us?"
    "I shrugged my shoulders."
    me "Since no one's pushing us or rushing us, why not work for fun?"
    me "It's not like we were ordered to finish everything the day before yesterday, or else it's the end of the world, run to the aircraft carrier."
    me "And if so..."
    play music music_list["went_fishing_caught_a_girl"] fadein 5
    "I've never liked cleaning. Honestly. Even my home den was always such a mess that..."
    "Let's just say I had a few well-trodden paths - to places of satisfaction - and that was it. The rest was smoothly overgrown with cobwebs, dust, and junk."
    "It's no surprise when all the trails go for years between the bed, the kitchen, and the computer."
    "But for Miku's sake, I was willing to step on some of my principles and remember that I was perfectly capable of getting the place in order - if I had a strong enough incentive."
    "The incentive was standing nearby, flapping huge eyelashes and exuding the scent of eucalyptus."
    me "Let's go, sunshine."
    "Threw me, charting the original route."
    "The green glass jars of reagents, for some unknown reason scattered all over the room, took their place on the second shelf of the cabinet - in close proximity to the soldering supplies."
    "Miku stared at me incomprehensively for a while, but she soon realized and went rough the room like a miniature whirlwind, collecting household chemicals - the latter had found a place on shelf number three."
    show mi smile pioneer with dspr
    mi "And you are determined!"
    "She exclaimed. And three tones lower:"
    mi "I like guys like that..."
    "Her words sent a particularly large herd of goosebumps marching down my back, but I forbade myself to get distracted."
    hide mi with dissolve
    "I tucked the books away on the top shelf, where an entire makeshift video clunker of VHS tapes awaited its viewer."
    th "Movies..."
    "I looked around and nodded contentedly as I discerned the video player."
    th "Watch."
    "No one's schedule is off for anyone, which means that at least from lunch until noon we'll have a couple of hours to watch something."
    "Marking this point in my head with a huge green checkmark, I focused on the next part of the Marlesonian ballet - paint cans, buckets, and tin containers with something fragile inside - I didn't even look."
    "There was room for them in the wardrobe department-where it looked like there had never been any dresses in my life, but there was a mattress rolled up on a bale of unopened gray underwear."
    th "In case I have to spend the night? {w}I wonder if Slavya even knows?"
    dreamgirl "Do you want to go and tell her about your find?"
    "The inner voice snorted."
    th "Of course not! I'm not that crazy yet."
    dreamgirl "So move the curtain smoothly to the right - you're the one with the complete lack of morals here. Miku may very well be more squeamish than that."
    "Heeding the advice, I elegantly pushed the potential pirate sleeper into a dark corner, pretending to be fully engaged in arranging the containers."
    "The latter, by the way, made room in the square shelf where the Panasonic went in like a native."
    "The rest was easy - slowly, of course, but surely."
    "Outside quietly went broken stools, empty boxes, tattered maps, tubes with some graphite junk inside, a bicycle wheel, planks, and a light camouflage plywood shield."
    "The red banner belonged in the main room - however, it's practically a religious symbol for the local youth."
    $ persistent.sprite_time = "sunset"
    stop ambience
    scene bg int_clubs_dj_7dl
    show mi normal pioneer
    with dissolve
    "And after we ran a damp cloth over the surfaces, scrubbed the molded concrete floor with a chunky rug in the middle, and closed the closet, the room was transformed into something quite decent!"
    me "There."
    "Shaking off my hands, I concluded."
    me "All that's left is to set up the equipment, and..."
    me "Miku, you and I are good!"
    show mi smile pioneer with dspr
    play sound sfx_face_slap
    mi "Yes!"
    "With a scathing 'high-five' on the palm that was set up, she agreed."
    mi "Although, of course, that should have been done yesterday."
    mt "I agree."
    show mt angry pioneer at left with dspr
    "Only now I suddenly remembered, belatedly, that someone had opened the door behind me."
    "Olga Dmitrievna."
    mt "Satisfied with yourself, are you? You blew the deadline, you embarrassed the bosses, you embarrassed me, and now they're going to point the finger and say look, you couldn't even get the radio to work!"
    me "But we..."
    mt "Shut up! We'll talk about your failure to meet the schedule later, but you, Hatsune, why are you on your feet since 9 and only now finished?"
    show mi sad pioneer with dspr
    mi "I'm sorry."
    "In a colorless voice, Miku replied, shrugging."
    mt "And that's all you have to say?! So that's what I'm supposed to tell him at the staff meeting when the director asks me why I screwed up the deadline?! Excuse me?"
    me "Olga Dmitrievna, but we..."
    mt "I know what you are! Instead of doing the party's task, went dancing! How come your legs didn't fall off!"
    me "Alright."
    "This circus is getting on my nerves."
    me "We {b}didn't{/b} get any party assignment. We're here on a voluntary basis, and if you're not happy with anything, we can leave."
    show mt shocked pioneer with dspr
    "My reluctance to sprinkle my head with ashes seemed to surprise the squad leader a little."
    "I spoke for myself, but I had no doubt that Miku would back me up."
    me "We cleaned up the room-which was supposed to be cleaned by anyone else, since you can't combine the work of a host and a cleaner! - And instead of thanking us, you're throwing mud at us!"
    me "Don't you have anything to say?"
    show mt rage pioneer with dspr
    mt "Say? I gave the cyberneticists the assignment before dinner last night! They found you, but not the best, it seems. I wish I had assigned Slavya!"
    th "That's how I'm going to believe you'd voluntarily give up your best assistant."
    me "So yesterday we should have instead of leading the dance, finding a host, and helping with the set up - should've told everyone to get lost and cleaned the place, am I confused about anything?"
    mt "Exactly! You were told that the radio was the prestige of the camp! And if you weren't, you could have guessed it yourself."
    "It seems it was that last straw that breaks the camel's backbone."
    "The whole world narrowed to two dark tunnels, throwing me back, hitting the bridge of my nose with rage from within."
    "I took in more air in my chest..."
    "And coughed as Olga, in the spirit of her usual devilishness, finished handing out her scoldings:"
    if not alt_day4_mi_dj_hedg:
        mt "And just try to be late for lunch!"
        "She walked out, slamming the door behind her."
        hide mt with dissolve
        me "You know, Miku, our leader is the strangest creature I've ever met."
        show mi laugh pioneer with dspr
        mi "Come on, Senechka."
        "The Japanese girl stroked my shoulder."
        mi "She isn't even close to you in that regard."
        me "Should I take that as a compliment or an insult?"
        show mi smile pioneer with dspr
        mi "Oh, I don't know. How about a little of this and a little of that?"
        "Something along those lines I assumed, as I smiled and offered her my hand:"
        me "Let's go?"
        show mi upset pioneer with dspr
        mi "What? Where?"
        me "To the washstands."
        "Without too much squeamishness, I took the cobwebs out of Miku's hair."
        me "There's still a couple of minutes before dinner, we should wash up."
        show mi happy pioneer with dspr
        mi "Yes! Or else Olga will really eat us up!"
        "Any way you look at it - and it's damn nice when the person you like thinks on the same plane as you do!"
        stop music fadeout 6
        stop ambience
    else:
        mt "And what the hell is this obscenity you're wearing?!"
        th "Geez, she said she didn't want to see me till lunchtime! What else does she want?"
        me "You personally gave me this obscenity."
        "I replied venomously."
        me "Personally."
        show mt grin pioneer with dspr
        mt "Really?"
        "The squad leader squinted her smile."
        me "On the first day."
        mt "I'm guessing I got it dirty and grassy and I don't know what else, too?"
        me "What?"
        show mt rage pioneer with dspr
        mt "Round to the warehouse for a new uniform march! And don't forget! To write! An explanatory note!"
        "I belatedly looked around me and realized that I'd been walking around in a wrinkled, dirty shirt the whole time-apparently the night hunt hadn't gone without scars."
        dreamgirl "Especially on my stomach."
        "Chuckled the inner voice."
        "The man-made dirt and dust, along with cobwebs and saltpeter, added a touch of absurdity to the still-life, and in a nutshell, I looked like hell."
        me "Oops."
        me "Why the explanatory note?"
        mt "Ask Feoktistova in the warehouse, she'll explain. And you, my dear, what are you sitting for?"
        "Olga instantly forgot I existed, switching to the new object of her pedagogy."
        "Poor Miku. More than ever I felt sorry for my sea sunshine - but in this case the wisest decision was to do as the angry leader demanded."
        "And so, catching her tortured look, blessed with a nod, I trickled outside and stomped toward the warehouse."
        play sound sfx_open_door_clubs
        scene bg ext_clubs_day with dissolve
        play music music_list["my_daily_life"] fadein 1
        play ambience ambience_camp_center_day fadein 1
        "There was less and less time before lunch, so it was unlikely that Miku would be forced to broadcast right away."
        th "Well. The better chance we have of crossing paths at lunch."
        dreamgirl "Say, why are you picking on that girl?"
        th "Uh... She's pretty. Why?"
        dreamgirl "Pretty? Is that all?"
        th "That's quite a lot!"
        dreamgirl "But clearly not enough to become annoying!"
        dreamgirl "Do you have at least a rough idea of what your behavior looks like?"
        if alt_day2_mi_date == 3:
            dreamgirl "In full accordance with Miku's account of how she communicates, she takes a man and squeezes him dry, then parts with him without regret. Since he can't and won't give anything more."
        scene bg ext_house_of_dv_day with dissolve
        "After hesitating a bit, I turned left just past the club building, heading south."
        th "But it's a little different here."
        "Objected I."
        th "I'm not interested in what she can give me."
        dreamgirl "What, really?"
        th "No! I mean, of course I'm interested, but..."
        dreamgirl "But not interested. Though interested. But no."
        th "Stop it. I don't need any more joking subconscious."
        "I'm finally getting my act together:"
        th "It's much more important to me what I can give her - if she's interested and not too burdensome with me, that's much more important than the fact that she's a living representative of an exotic country. And in fact, I've heard that Japanese women can do..."
        dreamgirl "Hey, hey! It's my prerogative to goof off and think such thoughts."
        th "No way."
        "Alisa and Ulyana's cabin sailed by."
        if alt_day2_us_escape:
            "And Ulyanka, sitting on the steps, waved to me."
            "The incredibly beautiful woman standing next to her looked up at me and nodded hello."
            th "Shit! They noticed!"
            dreamgirl "So what are you waiting for? Quickly, sideways and sideways, praying that from this distance they wouldn't notice anything."
            th "Yeah."
            "I kept going as fast as I could."
        else:
            "From the bushes, which were too dense to be a real self-seeding plantation, came guitar plucks - the main hooligan and headache of the whole camp allowed herself to shed her mask for a moment."
            th "She's playing pretty good though?"
            dreamgirl "Just don't tell her you heard that - she'll get her revenge."
        scene bg ext_boathouse_day with fade
        play ambience ambience_boat_station_day fadein 2
        "The warehouse was in the heart of the camp, by the canteen, and if I had walked like that in my soiled shirt, I suppose I would have already created a well-known reputation for the way the pioneers walked around here."
        "An inappropriately awakened responsibility wrapped me in a detour - through the boathouse."
        scene bg ext_un_hideout_day_7dl with dissolve
        "Across no man's land, marked by a pebbly beach."
        scene bg ext_beach_day with fade
        pause(1)
        play ambience ambience_lake_shore_day fadein 1
        "And through long trails past the beach and the volleyball field."
        scene bg ext_warehouse_day_7dl
        play ambience ambience_camp_center_day
        "To the now familiar gray barn with the ridiculously attached outhouse, locked with a huge barn lock."
        "Luckily, that wasn't where I was going - around the building on my left and headed for the door."
        if alt_day_binder != 1:
            extend " The place where I got a set of bedding on the first day."
        "Inappropriately, the cyberneticists' emergency supplies suddenly came to mind."
        th "If I could get some canned food in there, I'd be able to live without leaving home!"
        dreamgirl "Oh please, you're so quick to turn into a shut-in NEET."
        th "What's wrong with that? I'd go to space in the first place because it's the only place where real solitude is possible!"
        th "I'd get disks, flash drives with information, games, music, books - you know that the 300 megabytes of texts on my phone include about two and a half hundred books, not the smallest, on average it takes two or three days to read them."
        th "Concentrated knowledge - three hundred megabytes includes food for the brain for two years of non-stop reading."
        th "And for millions of miles not a single living soul - just me, my station..."
        dreamgirl "And Solaris, yeah. How long do you think you'll last if one day you find that one and a half meters of indomitable tenderness between the doors?"
        th "As long as it takes. After all, that's what I've always dreamed of."
        dreamgirl "Really? Where do you put it?"
        "I'm just now noticing that I'm still standing on the doorstep with my hand out for a knock."
        dreamgirl "Then what about Miku?"
        th "Miku is here. {w}Cosmos is there. {w}Solaris doesn't exist. {w}Close the subject."
        play sound sfx_knocking_door_2
        sl "Come in!"
        "Called Slavya from inside."
        scene bg int_warehouse_day_7dl
        show sl normal pioneer
        with dissolve
        "Slavya was sitting at her desk, writing something on yellow lined paper in a huge ledger."
        "When she saw me, she instantly stood up and, in her usual manner, smiled irresistibly."
        sl "Hello. What did you want to see me about?"
        "Then she finally paid attention to my appearance."
        show sl surprise pioneer with dspr
        sl "Semyon! What happened to you?"
        th "Shit, I walked half the day like this - and nothing!"
        me "I... uh..."
        "I smiled stupidly."
        me "I fell. And got dirty."
        sl "That's terrible! And you only washed yesterday."
        "She dejectedly waved her hands."
        sl "Stay here."
        "She said with a tone excluding any semblance of disobedience."
        hide sl
        "And disappeared somewhere in the semi-darkness between the shelves."
        "And from the dining room came the horns."
        th "And she was gone. Well, that's wonderful. What if she leaves for lunch and forgets me here?"
        dreamgirl "Then we'll stand here until their holiness allows us to unfreeze."
        dreamgirl "A week, if necessary!"
        th "Well, thank you, you gloomy nerd!"
        dreamgirl "I hear from the retard!"
        show sl normal pioneer with dspr
        sl "Throw off the dirty clothes."
        "Said she, handing me a set of fresh, unkempt uniforms."
        sl "I can't believe you agreed to wear that."
        "It was easy for her, with her perfect uniform, to say - looking at Slavyana, I sometimes felt like she was surrounded by a kind of dirt-repelling field of static electricity."
        "Really, how else can you explain her bouncing a broom on the square in the morning, then helping out on the sports field, and running in here to fiddle with the laundry before lunch - and still managing to stay as fresh and blooming as ever."
        dreamgirl "She has a cheat for not getting dirty."
        th "I wonder if I should undress in front of her. If she notices an attack of asphalt disease on my stomach, it'll take me a long time to get to lunch."
        sl "And why are you frozen? Take your clothes off."
        "I threw an eloquent look at her, hinting that we weren't that familiar yet."
        sl "What?"
        me "Should I undress in front of you?"
        "She doesn't seem to want to take a hint. Well, or she's just kidding around."
        show sl laugh pioneer with dspr
        sl "Are you shy?"
        "She laughed out loud, watching me blush."
        me "Slavya!"
        sl "Fine, fine, I'm leaving."
        hide sl with easeoutright
        "She headed back to the shelves, and I was finally able to uncover myself."
        th "Now quick! One-two..."
        "The tie unraveled like a living thing, the shirt flew to the floor, followed by the shorts."
        "My hands trembled a little as I pulled out the pins holding the shirt to the cardboard."
        "And then there's that laugh..."
        dreamgirl "Your panties are funny. With a bear."
        th "Praise Random, this world has never heard of a pedobear."
        dreamgirl "Judging by the laughter, it's enough that you have some bear on your boxers."
        dreamgirl "And if you don't hurry up, you'll look pale."
        th "I think she's seen all she wants to see. Judging by all the same laughter."
        dreamgirl "That's true. But what if the squad leader comes by to check on her errand?"
        dreamgirl "Or one of the inspectors. That would be a laugh."
        th "You're not helping!"
        "The new shorts were stiff, and I couldn't get away from the impression I was trying to fit into some wooden sarcophagus."
        dreamgirl "That's right. A raincoat, to be more precise. That's exactly what you're going to try on if someone catches you. Can you move?"
        th "I'm trying!"
        "Jumping up on one leg, I nearly tripped trying to get my leg through my pant leg - but I finally managed that difficult task, too."
        sl "If you're done fooling around, I'm coming back!"
        "The activist's voice came out."
        sl "I still have to close the warehouse and at least make it to the end of lunch."
        me "Yeah, I'm done."
        "Rolling the dirty clothes into a clump, I tossed them into the basket, where several sets of someone else's uniforms, stained with red paint, were already waiting."
        show sl smile pioneer with dspr
        sl "That's a long time! How are you going to serve in the army dressed like that?"
        if herc:
            me "Need will teach, need will compel."
        else:
            th "And they didn't take me because of my health."
            "I almost blurted out, just in time to remember that for my current body, all this military ordeal is just around the corner."
        me "I'll think of something!"
        "I cut her off. Skipping lunch wasn't a cheerful prospect for me, either."
        me "And if you stop making fun of me, we'll make it to the canteen in time, too!"
        show sl laugh pioneer with dspr
        sl "Sorry, I can't help it. You're so funny when you're embarrassed."
        play sound sfx_close_door_clubs_nextroom
        scene bg ext_warehouse_day_7dl
        show sl normal pioneer
        with dissolve
        "Slamming the door and clicking the new-fangled spring lock, Slavya commanded:"
        sl "Forward! Assault on the canteen!"
        menu:
            "So what's the occasion for inspection?":
                $ alt_day4_mi_dj_blackmailed = True
                sl "Don't you know?"
                me "Don't know what?"
                sl "It's Parents' Day - it's on Wednesdays every week. Well, we're having an open house."
                me "That's weird, nobody told me anything about that."
                sl "No wonder - yesterday you were running around leading dances, and today you were up late."
                me "Yeah, it's been a rough night."
                sl "Tell me about it."
                me "How often do you have a bath here, anyway?"
                show sl smile pioneer with dspr
                sl "Not really. We have an on-demand basis here. And those who want to bathe every day go to the showers, where the water is cold, but all the time."
                me "On demand?"
                sl "Yes. The girls and I agreed, and Lena and Miku let you go first."
                "She looked me in the eye with an expression."
                sl "And Miku also swore that she wanted to talk to you about something, but you ran away from the disco too early..."
                dreamgirl "Now tell us, Mr. Counselor, where were you on the night of the thirty-first to the third? And who can confirm your alibi?"
                me "Yes, when you called me to the bath, I ran right away for my things - I had to wander around, but you were still washing at that time, so I came just when you were finished."
                show sl angry pioneer with dspr
                sl "I was surprised at your 'easy steaming'."
                me "Your hair was wet! And the sundress on the wet skin was tight... Here."
                "I was sinking fast and I knew it."
                "Fortunately, Slavya seemed to have had enough of embarrassing me, and she shut up."
                scene bg ext_dining_hall_away_day with dissolve
                $ persistent.sprite_time = "day"
                $ day_time()
                play sound_loop ambience_medium_crowd_outdoors fadein 2
                "Just in time - we just missed the crowd of well-fed pioneers who jumped out of the canteen."
            "Be silent":
                "I nodded obediently and allowed myself to be carried away toward the dining hall building next door."
                scene bg ext_dining_hall_away_day with dissolve
                $ persistent.sprite_time = "day"
                $ day_time()
                play sound_loop ambience_medium_crowd_outdoors fadein 2
                "The doors swung open in front of us - we barely had time to recoil, letting a herd of fed-up pioneers pass us by."
                $ lp_mi += 1
                $ karma += 10
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_dj_dinner:
    scene bg int_dining_hall_people_day
    with dissolve
    play ambience ambience_dining_hall_full fadein 5
    "Turning on the gentleman, I let the girl go ahead of me."
    mi "Thank you!"
    "And went in after her."
    "Lunch was in full swing, and I had to do a pretty good search before I found the two places next door."
    th "And what's with the pioneers and the counselors not having a good time?"
    dreamgirl "Well, maybe they've had enough of it already? It's dinnertime, so maybe they..."
    "To tell you the truth, I didn't really understand why Miku didn't suddenly have some urgent business or plans or something that completely precluded my presence."
    "No doubt I'm judging from my own bell tower - but to me such an intense presence of anyone is already a good enough reason to take a smoke break."
    "I was about to open my mouth to ask her about it, but I stopped myself in time."
    dreamgirl "She's not telling you to get lost, so what the hell else are you gonna do, you protocol mug? Be glad a whole Japanese singer puts up with you."
    th "I guess she has some positive aspects to my society - I don't know, pick something up, take it to me."
    th "At the club, again, helped with the cleaning."
    show mi normal pioneer at center
    with dspr
    mi "Bon appetit."
    "She wished, rubbing her hands together and holding her spoon at the ready."
    me "Thank you."
    "The picture was so amusing that I wasn't the least bit surprised by the self-conscious smile that occupied the corners of my lips."
    me "Same to you, and in the same place."
    show mi smile pioneer at center
    with dspr
    mi "You just said that so funny."
    "Miku grinned and moved her chair toward me, screeching across the dining room with her feet on the tiles."
    show mi normal pioneer close with dspr
    mi "Senechka, hey Senechka..."
    "She moved toward me and lowered her voice."
    me "Yes, what did you want?"
    mi "Say, what are you going to do after lunch?"
    th "There you go, she wants something out from under me again."
    "Now that our ambiguous relationship was settled into the pragmatic framework I was already used to, I cheered up again and felt much more confident."
    "Thinking that someone needs you strictly for something is certainly destructive to romance, and is rejected outright by sentimental personalities-but I personally feel more comfortable thinking that I am not completely useless."
    "I did not believe in my own attractiveness, and obscurity frightened me."
    me "I didn't really have any plans, except to take a shower..."
    "I shrugged."
    if (alt_day3_technoquest1 == 0) and (not alt_day4_mi_dj_hedg):
        me "But since you and I have splashed around at the washbasins, I'm totally free until Friday."
        show mi upset pioneer with dspr
        mi "You mean before Thursday? Till tomorrow?"
        me "Never mind."
        "I rubbed the bridge of my nose, once again reminding myself of a number of rules for dealing with this girl."
        "In particular, the very rule that forbade me from using local and just plain silly phraseology."
    me "Not the point. So what did you want?"
    show mi shy pioneer with dspr
    "Miku was embarrassed for a split second, but she pulled herself together immediately."
    mi "You know, I don't want to be alone in the broadcasting room, maybe you could keep me company?"
    mi "No, no, don't think anything of the sort, it's just that since you said you would support me when you talked me into taking this post, it's time to keep your promises!"
    show mi upset pioneer with dspr
    "Miku pretended with all her might that we had a strictly business relationship."
    if alt_day4_mi_dj_hedg:
        "Despite even her bracelet encircling my left wrist, and the undried kiss mark."
        "Strictly businesslike."
    "This approach to business impressed me immensely, so I nodded without a second's hesitation."
    me "Shall we settle the matter with Olga Dmitrievna? Or shall we run away?"
    mi "Oh..."
    show mi laugh pioneer at center with dspr
    mi "You know, I've got it all worked out."
    "That impudent creature declared, smiling cheekily right in my face."
    "And what are you supposed to do with her?"
    "That's right. Nurture, cherish, and flog her from time to time."
    me "For some reason I was expecting that answer."
    show mi smile pioneer at center with dspr
    mi "Senechka, you are the most understanding! Thank you for not saying no!"
    "She gathered up the plates and stood up."
    mi "Here."
    "She put some kind of key on the table."
    me "What is it?"
    mi "A spare set from the radio room. Used to belong to Shurik."
    me "And why do I need it?"
    mi "Because only I have access to there."
    "She smiled dazzlingly."
    mi "Well, and you now."
    "And she dashed off, tossing over her shoulder:"
    mi "I'll wait for you at the club!"
    hide mi with dissolve
    "Well, even though communication with the speedy talker gave off to me a slight and very pleasant feeling of split personality, I decided not to resist."
    th "After all, I do have an inner voice!"
    dreamgirl "Hey, hey, let's not get carried away. And let's certainly not compare me to her."
    dreamgirl "Although I certainly wouldn't mind doing an organoleptic rapid-fire analysis of this girl to see if she exists."
    "After uttering another vulgarity, my inner voice faltered, allowing me to finish my kompot of indestructible dried fruit."
    stop ambience
    stop sound_loop
    play sound sfx_open_dooor_campus_1
    play music music_7dl["what_am_i_doing_here"] fadein 5
    stop ambience
    scene bg ext_dining_hall_away_day
    with dissolve
    "Of all the people I have met, only one person could claim to be a checker or an inspector - Slavyana proper."
    th "Then where are all the others? Has Olga played a trick on me - just to lure me out of the cabin?"
    "Though that's unlikely, of course. She could have just said Miku was looking for me, or Slavya..."
    scene bg ext_square_day
    play ambience ambience_camp_center_day fadein 6
    "Or give me a party assignment somewhere in the middle of nowhere."
    scene bg ext_clubs_day with dissolve
    play ambience ambience_camp_center_day fadein 5
    "I could only catch up with Miku outside the clubs, where for some reason she was shifting from foot to foot, not daring to go inside."
    show mi normal pioneer with dissolve
    me "Hey, what are you doing here?"
    mi "You know, for some reason I don't feel like going there."
    mi "I sat there till lunchtime, and I don't like the idea of becoming a radio host."
    me "You don't like it? Hmm."
    "The Japanese girl's behavior was strange, to say the least."
    "Still, I've been taking things like inner voice warnings very seriously for some time now."
    "Yeah, try to ignore it when it's in full cry screaming so that it tinkles between your temples."
    me "You know... It's quiet hour, so our presence is not required."
    me "If you don't want to, we don't have to go."
    show mi serious pioneer with dspr
    mi "No way. I don't know what the hell's gotten into me, but I'm going to pull myself together."
    "She took a few breaths."
    show mi serious pioneer far with dspr
    "And went, almost ran."
    hide mi with dissolve
    "Breathless, swinging the door open."
    play sound sfx_open_dooor_campus_1
    $ persistent.sprite_time = "sunset"
    scene bg int_clubs_dj_7dl with dissolve
    "And popped indoors!"
    show mi normal pioneer with dspr
    mi "Wow. That's okay."
    mi "And why didn't I want to go..."
    "I had trouble answering, though I was uncomfortable here, too, for some reason."
    me "I don't know. Do we have any pressing concerns?"
    mi "No, but..."
    "She rubbed her temples."
    mi "I... It's..."
    "She spoke more and more slowly."
    me "Miku? What happened?"
    mi "I don't know..."
    "She rubbed the bridge of her nose."
    mi "A migraine entered my head suddenly."
    show mi sad pioneer with dspr
    me "Migraine?"
    mi "Yeah... I think so."
    "Dozens of possibilities flashed through my head, from radioactive waste to spilled mercury to cursed places."
    "But when I was cleaning this place, there was nothing like that."
    "Is it really tuned to Miku?"
    menu:
        "Look for reasons":
            $ alt_day4_mi_dj_reasons = True
            $ lp_mi += 1
            me "Miku, honey, why don't you go outside, and I'll see if we really need to demercurize the room."
            "The latter, of course, is unlikely - otherwise I wouldn't feel so good, either."
            "But it was worth checking."
            hide mi with dissolve
            "Nodding, Miku ran off, leaving me alone."
            "And I started checking the room."
            "The floor was clean - I wasn't lazy, I checked everything."
            "Concrete like concrete, poured, no cracks or potholes, there's nothing here and there can't be."
            "The cabinet closes tightly enough, the chemicals in it are sealed tight enough."
            "The desk is empty, inside and out."
            "The shelves are empty."
            "After casting another glance around the room, I sat down on a stool and thought."
            "Except for the ceiling, I looked at everything."
            "I mean, everything."
            "There was absolutely nothing here to cause a headache or an instinctive reluctance to approach."
            "Unless..."
            "Before I could finish the thought, there was a clatter of shoes in the next room, and the sick radio host herself appeared on the doorstep."
            show mi smile pioneer with dspr
            mi "Senechka, don't bother looking, I'm not going back to the post today anyway."
            me "Why?"
            mi "Because Daddy finally came to see me!"
            "She jumped and clapped her hands, becoming like those same cartoon Japanese schoolgirls."
            me "Will you introduce me?"
            "I smiled."
            show mi shy pioneer with dspr
            mi "I'm sorry, Senechka, but introducing a guy to his parents..."
            "She threw up her hands."
            mi "Anyway, you know what I mean."
            mi "You know, do me a favor and check out what's on stage, okay?"
            mi "And I'll be very, very grateful to you in return!"
            "She dazzled me one last time with a smile - and ran off."
            "Sighing, I decided that whoever didn't get to say no in time was at fault for delegating, and staggered off to the stage."
            hide mi with dissolve
            "Said goodbye, uh-huh."
        "Screw the reasons, lead her out":
            $ lp_mi += 2
            me "You know, I don't know what's wrong here, but clearly something is wrong."
            me "Let's tell Olga Dmitrievna to send the inspectors."
            mi "Do you think there's a tsuchinoko nesting here?"
            me "I doubt it."
            "I smiled."
            me "But better have someone who's a little more competent at this than you and me come and see what might be wrong here."
            show mi happy pioneer with dspr
            mi "As you wish!"
            "She smiled."
            mi "Would you like to go to the stage in the meantime? There will be a concert there."
            "I didn't want to go to the concert, but I didn't want to hurt Miku... either."
            me "With you - anywhere."
            "She nodded and took my hand and led the way."
            hide mi with dissolve
    $ persistent.sprite_time = "day"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_dj_dinner2:
    scene bg ext_dining_hall_away_day
    with dissolve
    stop sound_loop fadeout 2
    play ambience ambience_camp_center_day fadein 0
    "By the time we got to the dining room, there was hardly anyone left."
    "Miku's gone, too."
    play sound sfx_open_door_1
    pause(1)
    scene bg int_dining_hall_day with dissolve
    play ambience ambience_dining_hall_empty fadein 3
    "After seating me, Slavya disappeared to the other side of the food court and disappeared there for several minutes, evidently making arrangements for sustenance."
    "I sat down in the seat I had always wanted, but could never occupy, the janitor's seat, by the very handout."
    "Convenient! I grabbed the tray, consumed the ration, carried it away, and went on my way. {w}And it's all five and a half times faster than it takes the average pioneer."
    "Plus, you could see into the mess hall from here, and you could keep an eye on your troop without taking your eyes off the borscht if you wanted to."
    play sound sfx_open_door_clubs_2
    "At last my Valkyrie revealed herself to the world, saving me from starvation for the second time."
    "She swung the door open with her foot, balancing the tray in her hands, on which two plates were steaming with aromatic steam, along with a steady compote of dried fruit."
    show sl normal pioneer with dspr
    sl "Bon appetit!"
    "She wished, sitting down across from me."
    me "Thank you! You didn't say anything about being late?"
    show sl smile pioneer with dspr
    sl "And who's going to tell me what? I was dressing a pioneer, so that the whole Union wouldn't make our camp look bad."
    "When she put it that way, she almost looked like a hero."
    "If it had been me - if it had been me - I would have been kicked upside the head and written in Olga Dmitrievna's eternal 'misfits' with the conscription to hard labor on the first list."
    "Slavya has managed to make it up so that she'll come out a hero, and she'll get some kind of encouragement, too."
    th "And why can't I fit in the same way?"
    dreamgirl "Because you're an introvert, a recluse, and a favorite of skirt-wearing bullies and retirement-age women."
    me "I hope Miku can manage without me there."
    sl "So it's quiet hour, you don't have to broadcast, and what you haven't had time to finish, she'll take care of before five o'clock."
    me "You think so?"
    sl "I'm sure."
    "Slavya finished her soup and set her plate aside."
    sl "Listen, can I ask you something?"
    me "Uh... What?"
    show sl laugh pioneer with dspr
    sl "Don't worry about it, it's nothing fatal."
    "She started to explain."
    sl "Well done for finding us a radio host."
    sl "But the problem is that now it's physically impossible for Miku to combine her concert activities and her function as a disc jockey."
    sl "That's why I need someone to help organize the 'Juniors to Adults' concert, and I don't see a better candidate than you."
    me "And what's so great about me?"
    show sl normal pioneer with dspr
    sl "You know how to communicate with children."
    me "Me?!"
    "Here, of course, she blew me away."
    "Of all the children, I've only interacted with Ulyana, and I can't say that our communication has been productive."
    sl "Yes. Re-educating Miku and weaning her off the chatter in a date and a half is definitely a talent."
    "The logic in her words was twisted. Wild."
    "Undeniable."
    "With a sigh, I agreed."
    me "I hope the kids don't finish me off during their games."
    show sl smile pioneer with dspr
    sl "No!"
    sl "Now we'll watch the rehearsal, we'll repeat it with whoever we want, and then we'll deal with the equipment closer to noon."
    me "What about..."
    sl "Miku? Don't worry, I told her before lunch."
    me "What do you mean before lunch? We together..."
    show sl laugh pioneer with dspr
    sl "At what time did you get up?"
    "She never seems to get tired of laughing at me."
    show sl normal pioneer with dspr
    sl "While you were asleep, I had already arranged everything."
    $ alt_day4_mi_dj_sl_repet = True
    if alt_day4_mi_dj_blackmailed:
        sl "Must have been tired yesterday, huh?"
        me "What?"
        sl "Well, it took so much effort..."
        "She paused."
        show sl laugh pioneer with dspr
        sl "...near the bathhouse!"
        th "She has not forgotten! She hasn't forgotten and she hasn't forgiven!"
        sl "Did you at least enjoy the spectacle? Or I'll show you something else."
        me "What?"
        sl "I don't know. Anything. I don't mind, I don't charge to watch."
        "I sat there and couldn't believe my ears."
        "Three days ago we first met, and I was almost literally knocked off my feet by how great she looked."
        "A benchmark of beauty and health."
        "And that benchmark wants now..."
        "I felt myself blushing rapidly."
        menu:
            "Then show!":
                show sl laugh pioneer with dspr
                "Her laughter ran elastically through the empty hall, skirting obstacles and echoing off the walls."
                sl "Semyon, I know about you and Miku."
                sl "I'm flattered that you like me, and I'm not the least bit sorry."
                "She took hold of the knot of her tie, and I involuntarily swallowed."
                th "It's going to happen now, isn't it? Right here in the dining room?"
                sl "Have you figured out what you're going to tell Miku when she asks?"
                "She knocked me out of my euphoric state with that question."
                me "What? What do you mean?"
                "The unfortunate camouflage petal was momentarily left alone."
                show sl normal pioneer with dspr
                sl "No?"
                sl "Maybe we should tell her about your exploits last night..."
                "She's thinking."
                me "Don't even think about it!"
                "The change from mild excitement to horror was so sudden that it gave me a headache."
                sl "Absolutely not. After all, you're the one we have here as a guest from the capital; you'll leave, and I'll be sighing at the window."
                me "You're teasing again."
                show sl smile pioneer with dspr
                sl "Just a little bit. Well, have you eaten? Let's go to rehearsal."
                "With a sigh, I followed her."
            "Stop teasing me already":
                $ lp_mi += 1
                "With a laugh, Slavya got up and beckoned me to follow her."
                sl "Let's go! Rehearsal will not conduct itself!"
    else:
        me "So you've already decided everything for me, haven't you?"
        show sl laugh pioneer with dspr
        sl "Ah-ha, you got married without asking!"
        "She looked extremely pleased with herself."
        sl "I'm sorry, but you're the only pioneer available at the moment; Miku can manage without you until noon."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_dj_repetition:
    scene bg ext_stage_normal_day with dissolve
    play ambience ambience_camp_center_day fadein 6
    play music music_7dl["what_am_i_doing_here"] fadein 5
    if alt_day4_mi_dj_sl_repet:
        "There was a surprise waiting for me at the stage."
        show mi normal pioneer with dspr
        me "Miku? How did you get here?"
        mi "Oh, hello, Senechka, hello, Slavya! Olga Dmitrievna came to me in the radio room, told me to go, while I have free time, to hold a rehearsal."
        mi "It's quiet hour, so there's no need for the radio, right?"
        "Waiting for my nod, she continued:"
        show mi smile pioneer with dspr
        mi "Here I am. And so are you! How great!"
        mi "It'll be even more fun together!"
        me "Together?"
        show sl tender pioneer at left with dspr
        sl "Sorry, I didn't have time to warn you. My mother is arriving here, so I can't help."
        "She blushed the tiniest bit and, awkwardly, gripping the hem of her skirt with her fingers, crumpled the fabric unconsciously."
        "The girl was embarrassed. {w}Surprisingly, I didn't think she was familiar with the concept of embarrassment."
        dreamgirl "Yeah, so flaunting naked bodies doesn't embarrass us, but forgetting to warn us is a sure excuse to fall to the ground in shame."
        th "I suppose it's a little late to be embarrassed about the bath... And here I might as well flinch and say no. And then she and her mother will be rehearsing with pioneers."
        dreamgirl "Strong. Suspecting the camp's best pioneer girl of hypocrisy isn't even good enough for me."
        sl "And now I'm running away, Miku, since you're here, bring him up to speed, please."
        hide sl with moveoutleft
        "After waving to us, the girl ran off down the path that led to my cabin. I mean, the squad leader's cabin. Anyway, I see."
        "And then a few minutes later, Miku was called out by some older man."
        "And she got so excited that I knew without even explaining who he was."
        hide mi with dissolve
        "As a result, I was left alone."
    elif alt_day4_mi_dj_reasons:
        "Miku wasn't on stage, so I had to deal with the connection of the equipment myself."
        "At least Slavya, who was there in good time, didn't let the participants go into disarray."
    else:
        show mi grin pioneer with dspr
        mi "So, ready for the concert?"
        "I looked skeptically at the upcoming 'stars'."
        th "Yeah, it's going to be a hell of a concert."
        me "Can I back out?"
        show mi happy pioneer with dspr
        mi "No! You'll enjoy it with me!"
        "She coughed and turned on the microphone:"
        mi "Squad 4 - to the stage."
        "There was a slight stir at the stage, after which several kids who looked a little younger than Ulyana climbed up."
        mi "Three... four!"
        "A melody vaguely reminiscent of the 'dance of the little ducklings' poured from the speakers, and the 'stars' began to move - out of tune, out of sync, and out of place."
        "Miku sighed and turned to me."
        mi "Don't even think about it!"
        me "I wasn't thinking."
        show mi laugh pioneer with dspr
        mi "How did you guess?"
        me "You looked too eloquently from them to me!"
        mi "Eh, I wish I had a young man like you, who could understand me at a glance!"
        show mi shy pioneer with dspr
        mi "Anyway, that's all lyrics. Don't worry about the speakers."
        if ((not persistent.mi_dj_true) or (alt_day2_mi_date != 3)) and ('music_club' in list_voyage_7dl):
            "The embarrassed Miku instantly forgot everything I advised her."
            "However, I was sitting red as a cancer myself, so I didn't interrupt."
        mi "They will be watched by proud parents, so the flaws in their stage skills will be tolerated. {w}Here's a program of performances just in case, I'll go check the equipment and you watch."
        me "Equipment?"
        show mi smile pioneer with dspr
        mi "Oh, it's nothing, we'll need a 'robot voice' for one of the performances during the show, I'll set up the reverberator."
        hide mi with dissolve
        "She took off under the stage, where all the electronics were kept."
        "And what about me... I was left to sit and watch another singer, with no voice or hearing, but with a soul, yelling 'Eagle Eagle, fly above the sun.'"
        "His yelling was... overwhelming. It was a real psychological attack."
        "I sat there, paralyzed, listening to my eardrums being raped by this nightmare."
        "And when he got off the stage, quite pleased with himself..."
        th "Doesn't anyone tell him that he should be given milk for listening to him for being unhealthy!"
        dreamgirl "Are you going to find that daredevil to say that?"
        dreamgirl "Or do you think Miku just ran away?"
        th "She didn't run away, she went to check the hardware..."
        show mi normal pioneer far with dspr
        dreamgirl "And that's why she has such a happy mug."
        "I cringed at the 'mug,' but had to admit the inner voice was right - she looked a lot better than I felt."
        show mi normal pioneer with dspr
        me "Set it up?"
        "She looked somewhere past me and didn't answer anything."
        th "Strange girl?"
        show mi normal pioneer close with dspr
        "She quickened her step, coming closer to me."
        "For a moment she smiled."
        th "What is she going to do?!"
        "It flashed through my mind."
        "As the Japanese girl ran past."
        hide mi with dissolve
        "She was hanging around the neck of some short man in a classic tee shouting something like 'Daddy'."
        "Well, that was to be expected."
        "The day started off too well, and now I'm going to have to do the gig myself."
        dreamgirl "Decided to try your hand at being an MC?"
        th "You'd think I'd have a choice!"
        "I panicked a little, and when Miku came running up to me, I couldn't string a word or two together."
        show mi happy pioneer with dspr
        mi "Can you imagine, Senechka! Daddy came to see me! I wasn't expecting him, and he..."
        "She folded her hands against her cheek and smiled."
        "Although immediately got stern."
        mi "Look, I have to leave, but don't worry about the concert - I appreciate you too much to just leave you like that."
        mi "The main thing is to see the rehearsal through to the end, tick off those who you think deserve a separate announcement. Give it to Olga Dmitrievna at noon."
        mi "That's it. Don't let me down."
        "She patted me on the shoulder and ran off."
        hide mi with dissolve
    "Only now it occurred to me that I was, in fact, harnessed."
    "Without even asking."
    "Said I was quality control now, asked me not to screw up, and waved goodbye."
    "If I hadn't seen it in person, I thought it was Olga Dmitrievna turned into Miku for a second."
    "With a sigh, I sat back in my seat and nodded to the next 'artists.'"
    with fade2
    "I was nervous for the first half hour, no more."
    "Then I got over it."
    "After an hour I began to get bored, wrinkling only at the particularly loud cries emitted by the young throats."
    "Fortunately, some of the squad leaders were quite adept at introducing children to the beautiful, and I suspect that only the most stubborn screamers made their way to the stage."
    "Fortunately, and among them there were some who could get in tune, thinly or thinly - I rested on such."
    "Not as good as the dancers, of course, but still."
    "Five more performances, and I ticked the last box on the list."
    "And then the horn sounded."
    me "Thank you, everybody!"
    "I said into the microphone with a bolder voice."
    me "Dismissed."
    "And, having unplugged the equipment, I went to the canteen."
    "My head was already a little fuzzy from the amount of patriotic chants I had to take in."
    stop music fadeout 3
    return

label alt_day4_mi_dj_volley:
    scene bg ext_dining_hall_away_day with dissolve
    play music music_list["my_daily_life"] fadein 3
    show mt normal pioneer with dspr
    "Olga Dmitrievna was already standing by the dining room, smiling, waiting for me."
    mt "Well? How did you like the rehearsal?"
    me "I didn't. Take your list, and let's forget this nightmare."
    mt "Really? And I thought you'd agree to do the concert."
    "It made me cringe."
    me "You know, I don't feel like it."
    show mt grin pioneer with dspr
    mt "Why? I thought you liked the whole concert thing - the way you're hovering around Miku."
    "Okay. This conversation stopped being languid."
    "I exhaled and mentally counted to ten."
    me "I don't know what you're imagining or hearing from someone else. I. Am not. Hovering. Around. Anyone."
    me "And you'll do the concert yourself."
    "The crumpled sheet fell in the dust at the squad leader's feet, and I was already in the canteen."
    "I was shaking with anger."
    scene bg int_dining_hall_people_day with dissolve
    show us normal pioneer with dspr
    play ambience ambience_dining_hall_full fadein 6
    "Running indoors, I ran head-on into Ulyana."
    us "Hey! Watch it!"
    "The girl wanted to take offense, but apparently reading something on my face, she instantly curtailed all complaints and slipped past me to the door."
    hide us with dissolve
    "And I went to the food court, where they gave me a glass of sour cream and a bun."
    "I didn't feel like eating."
    "I wanted to find my remote control with rewind time."
    "At the same time, to fast-forward to the moment when the laughing Japanese girl with aquamarine hair returned."
    "And back a few days, where a few words and one spontaneous action made life a little more complicated."
    "I never really got to know the camp and its surroundings."
    "All I know now is how to get from home to the canteen, the music club, and the stage."
    th "That same lemish behavior, huh?"
    dreamgirl "Sort of, you've just stretched the apartment to the size of a campground, and you've left the habits the same - walking on two well-trodden trails, flat out ignoring everything else."
    th "What are your suggestions?"
    "I plucked off a bun and mechanically sent a piece into my mouth."
    dreamgirl "Off to go poke around the camp!"
    dreamgirl "It's not right that you only have three or four points of use from such a large area. {w}If you're going to take possessions, do it all the way!"
    th "That's right!"
    "I'm not likely to find anything out of the ordinary, but something new - absolutely!"
    scene bg ext_dining_hall_near_day
    with dissolve
    play ambience ambience_camp_center_day fadein 2
    play music music_list["get_to_know_me_better"] fadein 5
    "Leaving the unfinished kisel on the table, I went outside and wondered."
    us "Hey!"
    "Someone grabbed me by the elbow."
    "This camp has absolutely no respect for a person's right to privacy and personal space!"
    th "However, that's..."
    us "Freeze!"
    show us smile sport at right
    with dspr
    th "Ulyana. {w}This explains a lot."
    "A request to leave me alone and let me enjoy my little happiness?"
    "It's easier to give her what she demands than to explain why you can't."
    me "What do you want?"
    us "What are you doing now?"
    me "Going. Can't you see?"
    "I jerked my shoulder, freeing myself from the grip of her clinging fingers."
    show us sad sport at right
    with dspr
    us "Why are you so angry? You almost knocked me down in the cafeteria, and now you're growling."
    "The girl pushed her lower lip back and blinked rapidly, trying her best to look like she was about to cry."
    "You've got the wrong man."
    me "Very angry. Was that what you were after?"
    "Ulyana gave me a wry look, but decided to change from anger to mercy."
    us "And my mother brought me a real ball! A volleyball!"
    th "Certainly very important news. Worthy of the utmost attention."
    me "And?"
    us "What's not to understand? You've got to blow it up, and... And..."
    me "What?"
    show us smile sport at right
    with dspr
    us "Play! Will you play with me?"
    "The little girl blurted out and was embarrassed."
    "And it was kind of embarrassing to deny her such a small thing."
    me "Actually, I wanted to go for a walk around camp... But okay. {w}Where's your friend?"
    us "She had something with her stomach, Olga Dmitrievna took her to the infirmary."
    me "And the two of us are going to throw the ball together?"
    "I clarified."
    "Ulyana shrugged her shoulders."
    us "We'll probably find someone else on the way."
    show us smile sport at right
    with dspr
    us "I saw Lenka bored, we could call her!"
    me "Three. Anyone else?"
    show us grin sport at right
    with dspr
    us "Haven't you had enough?"
    "If she was expecting to embarrass me, she's got the wrong guy!"
    us "All right, all right, we can still get Slavya involved."
    if alt_day4_mi_dj_sl_repet:
        me "Her mom took her."
    else:
        me "I don't like the idea of that."
    us "Well, I don't know, we'll see if anyone else comes around."
    hide us with dissolve
    "Ulyanka shouted and ran away."
    "And only now I noticed that she had already managed to change into her sports uniform."
    "As if she never doubted the outcome of the negotiations."
    me "Well, I guess it's a little late to back out."
    "I didn't have anything to change into, so I took a shortcut to the volleyball field and headed there."
    play sound sfx_close_door_clubs_nextroom
    show un normal pioneer with dspr
    "The door creaked behind me, and Lena came out on the porch."
    me "Hi!"
    show un shy pioneer with dspr
    "She was a little embarrassed, but she found the strength to nod."
    me "Say... Aren't you very busy right now?"
    un "What's up?"
    me "I wanted to invite you to volleyball."
    me "Ulyana's got the ball, there'll be three of us with you, we need a fourth."
    un "But I don't..."
    me "Neither am I... But we'll warm up at the fries, then we'll see."
    "For a moment her gaze went unfocused, as if the girl was inwardly adjusting her own plans for the evening."
    "Finally she nodded."
    un "Deal. I'll go change."
    un "Where will you play?"
    me "By the houses. {w}Come back when you're done. We'll be waiting."
    show un smile pioneer with dspr
    "Lena smiled a little and nodded, then hurried down the path after Ulyana disappeared - yeah, she had something to change into."
    stop ambience fadeout 2
    scene bg ext_houses_day
    with dissolve
    show un smile sport at center
    show us smile sport at right
    with dspr
    "And while I was strolling leisurely to the cabins, Lena had already changed her pioneer uniform for sportswear and was waiting for me, along with Ulyana, in the 'street' in front of the first row of huts."
    "The ball was also here, not badly inflated, judging by the resilient sound - clearly under one extremely familiar to me game, very specifically held the palm of the owner of the ball."
    "'Potato', what else - if there are more than two, but less than six people for a small squad to play across the net, that's what the pioneers played."
    "The rules are simple - we stand at different ends of an equilateral figure - triangle, square, pentagon, whatever."
    "And we work with the ball."
    "And if the victim can't handle the serve - usually a very strong 'cut' - she sits in the center."
    "Then the fun begins - the 'potato' jumps around, trying to intercept the serve and put the one whose hands touched the ball last."
    "Or it waits for someone to try to cut across it, forfeiting the right to run in a circle, jump, or move at all - and catches the ball, too."
    "Seemingly brutal in appearance, this game provoked the development of volleyball skill in the vast majority of pioneers."
    "In fact, stuffed fingers and wrists weren't even considered anything special - everyone walked around with redness in their respective places."
    "Here, however, in view of a very special contingent, the rules would be softer.{w} Right?"
    me "Where shall we play?"
    us "Over there."
    "Ulyana pointed to the net stretched between the trees."
    th "A substitute volleyball court?"
    th "Didn't know it existed."
    dreamgirl "You didn't know about anything at all except a few spots. Well, at least you opened a new location. I hope you're pleased with yourself."
    th "Fuck you, fuck you."
    "After stomping across the sand, I nodded approvingly-we took the left side of the field for our games and began."
    scene bg ext_volley_court_7dl with dissolve
    play ambience ambience_soccer_play_background fadein 2
    play music music_list["went_fishing_caught_a_girl"] fadein 2
    "The passing game, sluggish at first, was gradually gaining momentum, and as the participants became more experienced, the serves became more interesting and sharper."
    "The rules here were evidently of the toughest kind."
    "My unaccustomed fingers soon ached, but I didn't feel it on adrenaline."
    "Ulyanka was playing sneaky attacks - twisting ones, modest Elena had a terribly heavy hand, but she could only cut from high serves, so we very soon switched the game to the middle horizon."
    "The potatoes were getting up and down, getting up and down - the rotation was going fast, no one was spared, and the main goal here was to win at all costs."
    "To take it on my fingers, kick it forward, almost to the right, providing the spin, spread my hands on the crooked-flying 'cutter' past me, and wave invitingly to the flushed, gaudy, sparkling eyes of Lena in the center of the field."
    me "You're welcome!"
    "Scream, breathe, jump, scream, kick - the body at some point remembered that physical activity is perfectly regulated by the unconscious, too!"
    "The body, guided by reflexes developed over the years, slowly freed up its brain resources for reflection... However, the peculiarity of the game is that it is terribly voracious in terms of time."
    "It feels like it's just beginning, you haven't even warmed up yet, and your hands aren't even humming yet, and the minute hand has already gone full circle."
    "But you don't notice that - the memory is that you've only just arrived and 'we've only been playing for two minutes.'"
    "Even though you've already hit the center of the circle five times and across the back itching with a well-pinned 'cutter' played by a world-unfriendly girl."
    mt "Lena? Ulyana? Semyon?"
    "Olga Dmitrievna, who was supposed to be present at the amateur concert, stopped the game by intercepting the ball over Ulyana's head."
    show mt normal pioneer far at fleft behind un with dissolve
    mt "Lazing around?"
    "She smiled at everyone with her smile."
    th "Yup, now we'll be used as free workforce."
    "With incomprehensible wistfulness, I thought - as if there were no more exquisite temptation than a game of hot potato in a triangle."
    dreamgirl "Unlikely. From the looks of it, she's dumped the gig on Slavya herself, and she's off."
    if alt_day4_mi_dj_sl_repet:
        th "What about her mom?"
        dreamgirl "What are you, five years old? Slavya's leading, Maman's watching from the back benches and cheering on her daughter."
    "Actually, it would be nice to get Olga into our game. Although cutting into the squad leader is kind of creepy."
    me "Sort of. Thought about going to the concert, but there you lead everything."
    show mt laugh pioneer with dspr
    mt "Not leading, as you see."
    me "How about joining us, then?"
    "The more people, the more the merrier. Especially since there are four of us, we can already divide into teams."
    "Although ideally a couple more pioneers would be nice - I don't know about cybernetic athleticism, but someone agile like Miku would be great."
    "Something inside me scratched at that name, and I forbade myself to return to it for the next few hours - after all, I'd promised myself I'd be a little better by the time she returned."
    me "Let's break into teams, and..."
    mt "No. And..."
    me "What?"
    mt "Uh... Nothing. I was on my way to run some errands."
    show mt normal pioneer with dissolve
    mt "And it won't be long before I'm free."
    me "Is that why you're yawning, because you have a heavy workload?"
    show mt grin pioneer with dspr
    mt "Okay, okay. Let's play. But two on two is somehow..."
    "After taking the ball away from me, the squad leader ducked under the net and looked back thoughtfully."
    mt "Dvachevskaya! Come here, you'll be on the team with me!"
    "She called."
    "Alisa's appearance was unexpected."
    me "She had a stomachache, didn't she?"
    mt "It went away. And bouncing around the net for a while is even useful!"
    show dv normal sport far at fleft
    show mt normal pioneer far at left
    with moveinleft
    show us smile sport far at right
    show un smile sport far at fright
    with moveinright
    "Three on two. Considering they have Olga, that's pretty fair."
    me "Ball in play. Serve on the squad leader's side."
    "I habitually stated."
    "And the game began!"
    "Little by little, as in any spontaneous match, the idle pioneers began to rake up to the field."
    "What am I talking about! A pioneer is always an example! There was no talk of idleness, of course."
    "It was just that these particular pioneers didn't know what to occupy themselves with on Parents' Day, and watching the little ones sing out of tune didn't inspire them."
    "As a result, our team was manned in half an hour, the opponents in forty minutes, but they also had Sanich involved."
    "The gym teacher winked at me, catching my eye, and took his place at the net."
    "«Squad Leaders and Co.» took the lead in no time - they had a huge amount of experience and practice."
    "Sanich seems to have been born with a ball in his paws, and, judging by his jaunty flickering with Olga, they were a well-established and well-played couple."
    "And we had to improvise and find ways to at least lose not quite so crushingly."
    "Ulyanka, understandably, was assigned to the net itself - no team could cut vertically, and the relatively sharp corners were held by the right and left forehands."
    "The serve rotation was decided to neglect, and after a few cannonball serves from Lena, we decided to let her hold the back right corner and, as a result, put the ball into play on our side."
    "I, understandably, held the middle - as someone more or less experienced and able to calculate the angles of attack."
    "And the visiting pioneers, I think, from the second or third squads, were scattered to the flanks, strictly punished to take any pass to Ulyana."
    "So the game went with mixed success..."
    "Although we expectedly lost in the end."
    stop ambience
    stop music fadeout 4
    play ambience ambience_camp_center_evening
    "But it's spontaneous volleyball. It doesn't matter if you win or lose."
    "The purpose of this game is to let the body work in that unique mode that only this game gives."
    "It's a sport for the lazy - you stand most of the time squinting in the sun, but sometimes the focus of the game moves to you, and then you have to squeeze two hundred percent out of yourself."
    "Jump out of your skin, but get the ball."
    show el normal pioneer at center with dissolve
    el "Here, if anyone's thirsty."
    "Electronik, who had been watching the game for the last hour, brought a bucket of water with a steel camping mug attached on a chain."
    hide el with dissolve
    "Hot, sweaty, but happy and cheerful, we clasped our opponents' paws and hastened to take advantage of the generous offer."
    mt "Don't drink too much, the water is cold, you'll catch cold!"
    "Olga Dmitrievna didn't miss her chance to bore."
    "Even Sanich wrinkled his nose and muttered something in three syllables."
    "However, the squad leader didn't notice it: after waving to us, she turned around and headed toward the showers."
    hide mt with dissolve
    "Following her, Dvachevskaya - who once again transformed herself, first standing lazily on the field and then shrieking and reacting with the now so familiar excitement at the end of the match. Got pulled in."
    hide dv
    hide un
    hide us
    with dissolve
    pause(2)
    scene bg ext_volley_court_7dl
    with blind_l
    "And when Ulyana rolled the ball into the house, and the rest of the pioneers followed her, realizing that the show was over for the day, it was just me and Lena on the benches."
    "I sat and enjoyed the setting sun, the nice weather, and waited for the humming hands to let go."
    "And she just kept quiet."
    "Unlike me, she had time to both change and wash her face while I was idle."
    th "Very active girl. Just like Miku."
    "It was not for nothing that they were placed together - I was assured once again of the leader's pedagogical talent, her ability to discern in two dissimilar personalities something that would bind them stronger than external commonalities."
    show un shy pioneer at center with dissolve
    un "Well played."
    "In an expressionless voice, staring somewhere under her feet, she said."
    "I smiled, looking up at the sky."
    "We played really well."
    "We managed to shut my head off from unhappy thoughts, managed to find out what my renewed body was capable of, managed to kill a few hours before dinner."
    play music music_list["a_promise_from_distant_days"] fadein 3
    un "I didn't thank you."
    "Making an incredibly serious expression on her face, she looked at me."
    "Very serious girl, very serious."
    "I could hardly contain my smile - I knew by some intuition that she would not forgive me if I let myself laugh."
    th "What have we come to - I'm interested in the opinion of some teenager who's half my age."
    dreamgirl "Well, let's say not half..."
    me "For what?"
    un "Well..."
    show un sad pioneer with dspr
    "What she wanted more than anything was to be somewhere far, far away from here right now."
    "You could, in principle, fall off the face of the earth."
    "It's much better than sitting here a victim of my unnerving attention."
    th "I know that because Tyler knows it."
    "I don't know, maybe if I didn't have room in my life for a stunningly beautiful girl with a sea wave instead of hair - there would be some warmth there for Lena?"
    "If you just imagine for a second that I haven't been licking Miku in all her hypostasis since the early days, not trying to make sure I don't let her go a single step."
    dreamgirl "Let's make it harder?"
    th "How?"
    dreamgirl "Since you agree that you and Lena have so much in common - let you switch places."
    dreamgirl "Imagine you're the one in a female guise, under the name of some Selma or Antonina or Samantha, and she's a cool Bulgarian guy named..."
    th "Why Bulgarian?"
    dreamgirl "Their names are cool. {w}Don't interrupt, so she's a cool guy named Elin or Elen."
    "And she's the one who's sitting there right now, overcoming."
    dreamgirl "You really like Elen, and you don't mind starting to date him. But Elen doesn't give you any signs of attention, and you are in doubt."
    th "My favorite suspension of disbelief?"
    dreamgirl "Yes. You know that the boy is already engaged, dating a cool girl named Miku, who on top of everything else is your roommate."
    dreamgirl "Or rather, you've only just heard the rumors, and here Elen is also in no hurry to make the situation a little clearer. {w}But there's no smoke without fire. And you're dying to get your hands on him."
    dreamgirl "I want to, and it pricks, and my mother won't let me. {w}And when the truth comes out, there will be a lot, a lot of pain."
    "Lena stubbornly didn't look in my direction."
    show un shy pioneer close with dspr
    "And she persisted - even though her cheeks were getting redder and redder."
    un "Um..."
    dreamgirl "What's the complication here, you ask? {w}The point is that Elen is an imaginary guy, but Semyon is..."
    "It gave me an electric shock."
    th "Then why?!"
    dreamgirl "Just feels like touching. Don't you get it?"
    th "I understand, but what about the consequences?"
    un "For... For calling me to play."
    "She could hardly squeeze it out."
    un "I don't usually get called, but here..."
    me "You played well, why aren't you called?"
    th "Is it because you're so unsociable?"
    un "No reason... I guess I'm scaring people off."
    me "What a silly thing to say. You would never scare me off! We are comrades, we have to do everything together."
    un "Yes..."
    "It's hard, it's hard to talk to someone who's even more embarrassed than you are."
    "From the height of the age difference, I'm trying to see right through it, but if we were in the same situation..."
    "Yeah, I'd probably think she was too arrogant and cold."
    "Probably that she's not interested in all of us, and she looks at all of us the way a manul looks at us-sad and fierce and perplexed at the same time."
    th "I wonder if I have any right to advise in this case."
    th "They all have a history that began long before me and will continue long after I am gone..."
    show un serious pioneer close with dspr
    un "But for some reason, it's only you, the one to whom all this is quite alien, who remembers it."
    "It gives me the chills on my shoulder blades."
    me "What? Alien? What are you talking about?"
    show un angry2 pioneer close with dspr
    un "Olga Dmitrievna told me a little bit about you."
    me "Really? How much did she tell you?"
    un "Enough."
    "Evasively she answered."
    me "More innuendos?"
    me "I suspect not much, since the camp still hasn't been surrounded by special forces and suggested I come out with my hands up."
    show un smile pioneer close with dspr
    un "Should they? Special forces."
    th "Well, who knows, what are the rules for welcoming guests from the future in this world?"
    th "True, I'm not exactly Alisa Seleznyova, and my world has nothing to do with the Communist paradise..."
    th "I'll bring them bad news, and a messenger with bad news is usually executed, so as not to jinx it."
    me "I don't know..."
    un "For a kid who grew up in an embassy in Cuba, you're too sad."
    th "In Cuba?"
    show un serious pioneer close with dspr
    un "That's why I wasn't surprised things worked out so well between you and Miku."
    th "SHE KNOWS!"
    "Knocked in the ilk."
    dreamgirl "If I say something, then believe me!"
    "And Lena kept talking."
    un "You're exotics, you're attracted to each other."
    un "As a white crow, I understand you like no one else."
    me "And what do you understand?"
    "This girl's logic bordered on schizophrenia - it was ironclad, but based on a fundamentally flawed premise."
    un "That's enough, Semyon."
    "She looked up."
    un "I'm only talking to you so easily now because you're not free."
    un "I wouldn't have the guts to come up to you, especially since you..."
    "Her voice dropped to a barely audible whisper."
    show un sad pioneer close with dspr
    un "I like you too much."
    me "What?"
    un "Nothing."
    "She shrugged her shoulders helplessly and turned away."
    show un shy pioneer close with dspr
    extend " Blushed."
    show un normal pioneer close with dspr
    un "Will you give me a stick?"
    me "Will you flog me with it?"
    "Lena got serious."
    show un serious pioneer close with dspr
    un "No. Although I really want to."
    me "Hmm, mystery again."
    "I held out a rod to her and watched as she sketched something in the sand."
    "Rough, coarse strokes, grotesquely twisted in caricature style, they folded into a suspiciously familiar face."
    th "One to one, eh? Lena thinks I grew up in an embassy, which is why it turns out I'm completely out of touch with local society."
    th "And she quite logically accommodated that fact with my sympathy for Miku."
    dreamgirl "Well, isn't she adorable? Mind you, if you'd picked any other girl to woo or decided to shut up altogether, any decision you made would fit into her theory."
    dreamgirl "Slavya - you're looking for power, Alisa - you're looking for a bully to play with."
    th "Ulyana?"
    dreamgirl "WHAT?!"
    "The inner voice didn't hide the horror."
    th "It's all right. Just kidding."
    "Inwardly I laughed, satisfied that I had succeeded in jerking the inner scrooge."
    "At last the features in the sand folded into me-eyeless, wiggly, with a sarcastic smirk..."
    "The latter, by the way, Lena, with an owl, instantly erased and drew another - open and sincere."
    un "Well?"
    th "Too good, if you ask me."
    th "Too pretty. I mean, I see my own face in the mirror whenever I visit the fun houses for the purpose of washing my hands."
    me "Great! Thank you. It's a shame, even, that someone would trample on such beauty."
    show un grin pioneer close with dspr
    un "Oh, come on. I'll draw a new one."
    me "No way."
    "I pulled my phone out of my pocket and, capturing an image in the frame, took a few pictures."
    "And, obeying some sort of naivete, moved the viewfinder solution..."
    show un normal pioneer with dspr
    show frame at truecenter:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 0.8 zoom 1.0 xalign 0.5 yalign 0.20
    show cam_ui at truecenter:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 0.8 zoom 1.0 xalign 0.5 yalign 0.30
    me "Smile…"
    show un smile pioneer with dspr
    pause(1)
    play sound sfx_7dl["snap"] fadein 0
    scene white with flash
    pause(1)
    scene bg ext_volley_court_7dl
    show un normal pioneer close at center
    with dissolve
    un "Another reason for interest?"
    th "I wonder if anything could surprise her."
    th "Gadget is from the twenty-first century!"
    dreamgirl "Try kissing her, you'll find out."
    th "What? Why?"
    dreamgirl "You're so eager to surprise her. I guarantee surprise right up until slapping."
    "No way. And it's not about my sensitivity or my morals."
    "It's just that I could hardly bring myself to - what? Kiss?"
    th "Explain to me why you do it?"
    dreamgirl "What are you talking about?"
    th "I remember Gogol's 'evenings' as well as you do! You don't evaluate anyone as a potential lover until a catalyst event occurs. Sort of a sign."
    th "Why are you doing this to Lena now?"
    dreamgirl "But I'm not doing anything!"
    th "You said about the kiss, you jerk! I'll be thinking about it now - and we both remember very well what that kind of thinking leads to!"
    dreamgirl "Actually, I could say something about male polygamy and wishing you fool nothing but good things. But since we've decided to be honest..."
    dreamgirl "I allow myself such things because the same reason Lena doesn't hesitate to talk to you about romantic topics."
    th "Why is that?"
    dreamgirl "Because it won't work out, you fool!"
    "The inner voice laughed and went silent for good."
    show un shy pioneer close with dspr
    un "You took a picture of me, too."
    "It cost her a lot of effort to keep talking, it was just me relaxing, realizing that this conversation was going nowhere."
    me "And why not? I won't promise to send pictures later, but I want to take pictures of everything I see in this camp."
    me "Otherwise I won't believe my own memory one day - and I can see everything for myself."
    "She exhaled."
    show un serious pioneer close with dspr
    un "Would you can't you just... come?"
    me "I'd love to, but..."
    "My dorky half did the black thing - my gaze kept rolling to the girl's lips."
    me "It's not all up to me."
    "I said, and I kept thinking to myself, what would it be like to kiss those lips?"
    th "I guess I wouldn't have had time to feel the contact?"
    th "It would be a half-second blackout of consciousness, after which a heel would be imprinted on my cheek."
    th "And then the trouble will begin."
    th "And Miku will never forgive me."
    "But as long as I'm in my dreams - I can afford it, can't I?"
    show un smile pioneer close with dspr
    un "And up to who?"
    "The shirt was tight around her body, and I wanted to unbutton the button, the one at the top of the arch."
    "I wanted to put my palm under her back and be inside her completely, irreparably but sweetly, moving in and out for the first time, more, building up the pace."
    with fade2
    th "Right. Lie down."
    "I expelled the unexpected surge of libido from my bloodstream with a tremendous effort and folded my leg over."
    "A gift from a renewed body."
    "Hyperreaction to any erotic stimulus."
    "And Lena, to any, even the most prejudiced eye, was a very, very tangible irritant."
    me "Yes, you see..."
    th "The embassy in Cuba, you say?"
    un "Ah, parents."
    "She nodded."
    me "Yes."
    show un smile3 pioneer close with dspr
    un "I'm a little jealous of you somewhere."
    un "I've always wanted to travel, and this is how you live."
    th "Oh, my dear, I travel like you wouldn't dream of."
    th "From sociopathic hell to socialist paradise."
    me "A matter of habit. You don't appreciate what's part of your daily routine."
    un "Also true."
    un "But I'd certainly never get used to it!"
    "She looked dreamily up at the sky, where the sun was preparing to roll away to the west."
    "Now she was probably the kind of person she was only alone with herself."
    "I guess I should be thankful that they let me in so deeply that they forgot I existed."
    me "And I'm not saying I'm used to it. It just doesn't thrill me anymore."
    show un normal pioneer close with dspr
    un "Then I would make it my goal to travel all over the world!"
    me "Why?"
    un "To tick a box!"
    un "To you, who has traveled all over America, such dreams must seem silly..."
    stop music fadeout 6
    play sound sfx_7dl["eat_horn"] fadein 1
    me "Not really. Are you going to eat?"
    show un smile pioneer close with dspr
    un "I'm going. You'll have to stop by the washbasins, though."
    "I've been talking too much - I'd forgotten I was all wet and dirty."
    me "You're right. I gotta run."
    un "Yeah. Bye!"
    "She tossed the twig aside, carefully rubbed the portrait in the sand, and waved at me, bewildered, ran off toward the dining room."
    stop sound fadeout 3
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_dj_supper:
    scene bg int_dining_hall_sunset with dissolve
    play ambience ambience_dining_hall_full fadein 2
    play music music_list["sweet_darkness"] fadein 5
    "Having cleaned myself up, I hurried to the canteen - though I was still very late."
    show mt normal pioneer with dissolve
    mt "Semyon?"
    "The squad leader frowned."
    mt "You're late again. Get to your spot in a hurry before they eat everything else."
    "She turned away, clearly waiting for someone else."
    hide mt with dissolve
    "And I sat down in the corner, keeping my seat just in case - what if Miku was already free by this point?"
    "Especially since I got rid of her main source of headache - and immediately dumped it on the fragile shoulders of our counselor."
    "Apparently, Miku decided to take her concert time with reserve."
    th "Or has Pa decided to compensate his daughter for all the attention she's been missing?"
    th "As if that's possible in five hours..."
    "I haven't seen my Japanese girl in five hours. It's a nightmare."
    "And in a week we can hardly manage to get enough of each other's company and companionship."
    "I was pessimistic about the future."
    th "So, the shift ends, we'll split up - she'll go back to Japan, I'll go to some unknown place, if you believe Lena, to my parents at the embassy."
    th "So that's it? Divorce and cactus between the beds? I don't want to!"
    if alt_day4_mi_dj_hedg:
        "There was a scraping of metal on the tile next to me, and my hope landed lightly on the chair that had been pushed back."
        show mi upset pioneer with dissolve
        mi "Semyon..."
        "Miku's eyes were wet."
        mi "And my daddy scolded me. Yeah."
        show mi cry pioneer with dspr
        "She tried her best to smile, but instead she burst into tears."
        me "Easy, easy, easy."
        "Ignoring the random witnesses, I turned to her and held her in my arms and stroked her shoulder for a few minutes, muttering inaudibly some soothing gibberish."
        if (not persistent.mi_dj_true) or (alt_day2_mi_date != 3):
            "Something about how everyone is bored and can't express themselves, much less the big bosses, and should be treated with understanding."
        mi "You don't understand."
        "Muffled the Japanese girl said somewhere in my chest."
        mi "He stopped by for a while, he wanted to see me before his return trip."
        me "Is he going somewhere?"
        mi "Not exactly. I'm the one who has to go..."
        "My heart sank."
        me "Going away how? Where? Why?"
        show mi angry pioneer with dspr
        "Miku stomped her foot."
        mi "I'm not going anywhere. That's what I told him. I'm leaving with everyone else at the end of my shift!"
        mi "And I don't care what they moved..."
        "My heart went back and almost burst with joy. So much so that I listened to the end of the sentence."
        me "And what did your father say?"
        mi "Said that my agent was already waiting, that I was messing up the plans, and in general, he didn't understand what had happened to me!"
        show mi upset pioneer at center with dissolve
        mi "And then he paid attention to my hand and asked me where I had put my bracelet."
        me "And you told him."
        if (alt_day2_date == 'mi'):
            mi "Yes! I absolutely can't lie to Pa... I told you about the hedgehog, about how you helped me, about the beach..."
            mi "Ah!"
        else:
            mi "Yes! I absolutely can't lie to Pa... I told about the hedgehog, about how you helped me... here."
        me "Yeah."
        "Any man is warm to an extramarital relationship... any man. Until he gets a daughter."
        me "Scolded you a lot, didn't he?"
        mi "No. But he was very worried about me."
        "She pulled back and looked into my eyes."
        mi "Senechka, you wouldn't hurt me, would you?"
        me "No way in the world."
        "I answered honestly."
        show mi smile pioneer with dspr
        mi "I told you! And he wouldn't believe it, he kept trying to go and talk to you like a man."
        th "Brrr..."
        mi "It's okay, I won't let anyone hurt you, not even my own Pa."
        "She kissed me on the same spot she kissed me the night before and went back to dinner."
        "The audience, gawking, turned away."
    else:
        "As if I ever had a cho…"
        scene black with guess_on
        "And then someone covered my eyes with hands."
        voice "Guess who?"
        me "Miku, of course!"
        "I smiled, kissing her palms."
        scene bg int_dining_hall_people_day
        show mi happy pioneer at center with dissolve
        mi "All yours!"
        me "Are you done already?"
        mi "Well yes, Pa stopped by for a while, he had some business to attend to."
        me "At least he paid attention to his daughter. That's bread enough."
        mi "That's right."
        show mi upset pioneer with dspr
        "Miku frowned a little."
        me "Is everything okay?"
        mi "Yes, yes..."
        me "Are you sure?"
        mi "Just quarreled a litlle bit with Dad."
        mi "What do you mean, a little bit?"
        show mi happy pioneer at center with dissolve
        "Miku waved her head as if she had a fly on her, and smiled."
        mi "Let's not talk about it, okay?"
        "I didn't argue. Any way you look at it, it's their family business."
    if (alt_day2_date == 'mi'):
        mi "Listen! I'm so nostalgic... Let's go to the beach!"
    else:
        mi "Listen! Let's go to the beach!"
    "Offered Miku, finishing the mashed potatoes."
    if (alt_day2_date == 'mi'):
        me "Where we had our first..."
        mi "Date!"
        "She picked up on that."
    me "Why don't we watch a movie?"
    mi "A movie?"
    if not alt_day4_mi_dj_sl_repet:
        mi "What about..."
        "She didn't finish."
        me "Let's do this, if it's still not all right there, we'll go to the beach."
        me "Otherwise, we'll watch a movie."
    elif not alt_day3_technoquest1:
        me "Yes! I saw a couple of interesting tapes in the radio room, I'd like to see them."
    else:
        me "Yes, we'll find something interesting."
    show mi smile pioneer with dspr
    mi "Deal!"
    "We finished dinner and left the canteen."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_dj_evening:
    scene bg ext_clubs_sunset_7dl
    show mi normal pioneer
    with dissolve
    play ambience ambience_camp_center_day fadein 5
    "Of course, the evening was too good to be wasted like that."
    "For a few seconds I even regretted my suggestion about the movie."
    th "Should we really give up and go for a walk?"
    dreamgirl "Yeah. Who's going to run the radio for you?"
    th "Shit."
    if not alt_day4_mi_dj_sl_repet:
        mi "Well, shall we try it?"
        "I nodded."
        "Miku gathered her wits for a few seconds."
        me "Anyway, when you get ready, come on in, I'll go put on some music."
        mi "No!"
        play sound sfx_open_door_clubs_2
        scene bg int_clubs_dj_7dl
        show mi normal pioneer
        with dissolve
        play music music_7dl["will_you"] fadein 6
        "I wasn't even surprised - so quickly I was grabbed by the arm and dragged indoors."
        "And the amazing thing is that if last time I really had to force myself into the club, I felt like I was diving into standing water, now there was no resistance."
        mi "Phew... Listen."
        "She froze, assessing her own sensations."
        mi "There's no more pressure, though. Listen."
        show mi happy pioneer with dspr
        mi "It's true! It's okay!"
    else:
        mi "You know, the more I like the idea of working as a radio host."
        mi "But I just don't want to sit by myself anymore."
        show mi sad pioneer with dspr
        mi "I'm sick of it!"
        mi "You must promise me, hand on heart, that you will keep me company."
        me "What's in it for me?"
        mi "What do you want?"
        me "Uh... I'll think about it."
        mi "And while you're thinking - I want you here! You must promise not to leave me alone."
        th "That's a lot of pressure!"
        me "Alright, alright."
        "Laughing, I raised my hands in front of me."
        show mi angry pioneer with dspr
        mi "Promise me!"
        me "Fine!"
        mi "Promise me!"
        me "Yes I promise!"
        show mi smile pioneer with dspr
        mi "Very good! Remember, you promised!"
        mi "But the movies have been waiting for us. Let's go."
        play sound sfx_open_door_clubs_2
        scene bg int_clubs_dj_7dl
        show mi normal pioneer
        with dissolve
        play music music_7dl["will_you"] fadein 6
    play ambience ambience_medstation_inside_night fadein 2
    "Once inside, Miku smiled contentedly and immediately whirled among the equipment."
    "I didn't stand either, devoting myself entirely to setting up the video player."
    "Well, I mean, like setting it up - plugging in the cords and finding the channel that was set to receive the signal."
    "A dedicated audio-video channel in the TVs of local modernity was still considered a fad and a bliss, so I had to sweat it out."
    "Some UHF, VHF... What's that supposed to mean?"
    "After a bit of fiddling with the jumpers, I finally got a more or less tolerable signal and, breaking through the tele-snow, put the image on the screen."
    "Now it's much more important than setting up the equipment."
    "Choosing a movie!"
    "My choice fell on a good old movie I used to watch when I was very, very young."
    "It was called «Big»."
    "It's a funny moment, like there's some kind of ideal age that one aspires to since birth."
    "I was just happy to be in the body of a teenager of seventeen, a sort of New Year's present to shed the weight of my life."
    "And the main character in the film was on the other side of the 'platinum' age."
    "And like any other child, one of his deepest desires was to become an adult as quickly as possible."
    "The only difference between him and an ordinary child was that his wish did come true."
    "It's a little naive, but it's funny to see how circumstances twist the hero around, fulfilling his dreams, twisting them to their own way."
    "Yes, and the fact that he ended up doing well, and even had a way back open for him when he had had his fill of coveted adulthood..."
    "I was about four years old, I guess, when my mother kicked my father and me out for a walk outside, ordering us not to come back until evening. So we went to the movies."
    "And yes, for a four-year-old boy, that magical tale was indeed a thrilling adventure - not like the experience-weary to the moderately cynical me of a quarter-century later."
    "I guess that's why I didn't hesitate when the tape came to hand."
    "My alternative was «Back to the Future», but I decided it wasn't my last night."
    "So I had a kind of themed video session."
    "There's a hero on the screen, a boy inside, who generally sees girls as creatures from another planet."
    "But he sees everyone around him interacting with the opposite sex, and tries to - fit in?"
    th "Mimicry."
    "The events of twenty-five years ago, Nevsky Prospect and trying to catch a ride from the subway to home are spinning in my head again. And it's ten o'clock at night, and a huge warm palm belongs to the strongest being in the world."
    "Father."
    "Perhaps all religions in the world grow from here - from the desire to resurrect that very childlike sense of security when there is someone huge and strong and all-knowing around."
    "Someone you can ask anything."
    "Someone who won't be lazy to put you on his shoulder if you rub your foot or are tired."
    "The one who moderates his own stride so you can segue beside him."
    "I felt the touch of the palm of my hand on my palm."
    show unblink
    show mi sad pioneer with dspr
    play music music_list["confession_oboe"] fadein 5
    mi "You didn't just freeze up, did you?"
    "Confidently, she said."
    mi "Do you have something to do with this movie?"
    me "How can I tell you..."
    "I answered evasively, careful not to look the girl in the eye."
    mi "Don't say anything. {w}Shut up if you don't want to answer. {w}Just don't lie."
    show mi serious pioneer with dspr
    if (alt_day2_date == 'mi'):
        mi "You see, even then, on the beach, I realized how subtly I felt you. {w}You're twitching, and I'm crying"
        show mi sad pioneer with dspr
        extend ", you're in pain, and I'm screaming."
    mi "And the movie is a year old, and your eyes are wet."
    me "That's okay."
    "I took a deep breath."
    me "It'll pass soon."
    show mi angry pioneer with dspr
    mi "Maybe I don't want it to go away! {w} Maybe I want to know - what's going on with you!"
    "She stomped her foot in indignation."
    me "And you have every right to do so, of course?"
    "I inquired ingratiatingly."
    if alt_day4_mi_dj_hedg:
        mi "Yes. You have accepted my gift, my care and my attention. Which means you no longer have the right to brush it aside and withdraw into yourself."
    show mi normal pioneer close with dspr
    mi "We're close, whether you like it or not."
    "I looked up."
    th "Silly girl, what do you know about intimacy, all your life jumping on the stage and dutifully wearing the mask that an appreciative audience wanted you to wear?"
    "Silently I asked her."
    "{i}I know what is necessary now.{/i}"
    "She was impossibly close - and could well hear my racing heart at that distance."
    "And why was it pounding so?"
    "The only thing left in me that was moving was this very heart. {w}And the gently swaying bellows of my lungs."
    "And when my stupor had me so stuck in an unsteady position, she just pulled me toward her. Stupid, with our difference in weight."
    "Stupid."
    "But."
    scene black with fade
    "A scarlet sparkle flashed beneath my closed eyelids, a memory not dried by tears."
    "And the sensation that once seemed to be gone, irretrievably, of being part of a miracle."
    "I barely had time to relax so it wouldn't look like I was pushing the girl away. So she could pull me close to her after all."
    "She's the one I wouldn't want to push away."
    "There were a few millimeters of red-hot air between us when Miku closed her eyes."
    "And then..."
    "It wasn't supposed to happen, but it did."
    stop music
    $ persistent.sprite_time = "night"
    $ night_time()
    scene bg int_clubs_dj_nolight_7dl
    show mi shocked pioneer
    with dissolve
    play sound sfx_stomach_growl
    "The stomach decided to play the girl her whale song."
    th "What bad timing!"
    play sound sfx_stomach_growl
    "Miku recoiled a little, as my stomach gave out a second roulade."
    show mi scared pioneer with dspr
    mi "Ow! There's something in your stomach!"
    me "It's just my supper."
    "I blushed, inwardly executing myself for an inappropriately flared metabolism."
    show mi smile pioneer with dspr
    mi "But I was eating all the same things, why isn't my stomach talking?"
    "Even though we didn't follow through on what we started, I didn't feel the kind of awkwardness I just had to feel."
    "A little awkward, both of us not knowing where to put our hands."
    "Whether it was my stomach chants that defused the situation, or the fact that with this Japanese girl I had completely forgotten what it meant to be uncomfortable for anyone."
    "The fact remains that I was easy, comfortable, and wanted to repeat the thwarted attempt."
    th "Now I'll just get up the nerve, and..."
    play sound sfx_click_1
    "A tape recorder clicked, marking the finished side of a 'long-playing' reel, showering the whole camp with music."
    "The time had jumped the twenty-two hour mark - while we were having fun watching the movie, twilight had already fallen on the camp, barely dispersed by the light of the lanterns."
    show mi normal pioneer with dspr
    me "Look, there's still time before lights out..."
    mi "Yes..."
    me "Is your invitation still open?"
    mi "The invitation..."
    "Miku thought about it."
    me "To the beach."
    show mi upset pioneer with dspr
    mi "And the radio?"
    me "Radio? Well... We could curtail activities, first day, shortened broadcasts."
    me "Or put another tape on for a couple of hours..."
    "Miku thought again."
    if not alt_day4_mi_dj_sl_repet:
        "Actually, after her migraine, she was somehow different-no gibbering, no running, no flickering in front of her eyes."
    me "Say... Don't you have a headache?"
    if not alt_day4_mi_dj_sl_repet:
        "As if remembering her renome, the Japanese girl flitted around the room."
    mi "I don't think I'll leave the equipment running... What? Head?"
    "That's an unnecessary question, I agree."
    "For someone who is in a music club all day, at any moment can pick up an instrument and play something, I guess today's move is unpleasant enough."
    mi "That's it!"
    "And her subsequent words completely confirmed my thoughts."
    show mi smile pioneer with dspr
    mi "You know, Senechka, I haven't sung a single song all day today, and I don't feel so good!"
    me "Withdrawal?"
    mi "What?"
    me "No, no, nothing. Do you want to sing?"
    mi "Yes!"
    "The amp's lights went out, and Miku headed past me toward the door."
    mi "That's it, I ran away! Close the room and catch up!"
    play sound sfx_open_dooor_campus_1
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_dj_night:
    scene bg ext_clubs_night with dissolve
    play ambience ambience_camp_center_night fadein 6
    "While we were getting ready and passing out, it got dark."
    "Thanks be to Random, getting my bearings was a lot easier than it had been half an hour ago, as the full, huge moon rolled into the sky."
    "I moved at a brisk pace, nervous for some reason, looking around every now and then, expecting either a shout or an attack."
    "I didn't know much about who I had wronged or misbehaved in front of, but the feeling was unstoppable."
    "And the great fortune was that it was nothing from the music club to the Japanese starlet's new abode, three hundred meters in a straight line, all uphill."
    "It's hard to even imagine the feelings I would have crossed the camp with if Miku had agreed to go to the beach."
    "Finally I caught up with her - almost at the very steps of the club."
    scene bg ext_musclub_night_7dl
    with dissolve
    play ambience ambience_camp_center_night
    show mi normal pioneer at center with dissolve
    play music music_7dl["embers"] fadein 3
    mi "Hurry up, lazybones!"
    "With a laugh the girl hurried me along."
    if alt_day4_mi_dj_hedg:
        mi "I hope we don't get attacked by any predator this time."
        me "Don't worry, if he does, I'll save you!"
        show mi happy pioneer with dspr
        mi "I don't doubt that at all."
    mi "Semyon, let's not go inside?"
    me "What about..."
    mi "How about here? I'll get the record player out and here - look, it's a nice night!"
    "I nodded in agreement."
    me "Sure."
    "Gracing me a fleeting smile, she ran off."
    hide mi with dissolve
    "I, on the other hand, picked up my legs and sat comfortably on one of the benches."
    "A few minutes of nonstop rumbling and frightening noises from inside, and the actual heroine of the day... I mean, of the evening, finally appeared outside."
    "After a bit of searching, she poked the plug into an outside outlet and turned on the phonograph."
    scene cg d4_mi_dj_dancing_7dl with dissolve
    "It may not have been the best stage in the world, and the concert organizers were a bit on the tight side."
    "But I was the most appreciative audience."
    "And Miku was the most beautiful star you could see looking up into the sky."
    "Lack of light - as a result, I have great difficulty distinguishing her silhouette against the frozen moon."
    "She's singing about something, but this time I lack an active stock of Japanese words to make anything out and guess at least from the context."
    "It doesn't work."
    "And she moves to the beat of the music, even just walking across the stage with a kind of prancing, somehow touching to the core."
    "The song ended, another began."
    "Without pausing to catch her breath, Miku ran her palms across her shoulders, across her chest, down her legs, as if to take off the mood of the previous song, switching to the next."
    "And again I'm swimming, and Miku, as if guessing, is looking at me."
    "I wish I could make out her facial features."
    "Probably a wink or a tongue twister. That's what she's good for."
    "I didn't count how many songs were sung live, but the time flew by, the boards warmed up from the day pleasantly warming my bare feet, and the mood was the best."
    "It's not like that with us, it's not like people, we don't hold hands, we don't look into each other's eyes, no."
    "Instead, we dance in the dark, listening to each other's breathing and believing that tomorrow will come, and it will only be together."
    dreamgirl "H{b}o{/b}lding."
    th "What?"
    dreamgirl "I'm saying, you're holding your hands."
    th "When?"
    dreamgirl "Right now."
    "Only now did I notice that the music had changed to some slow song, and Miku wasn't dancing anymore."
    "Instead, she came up to me and held out her hand."
    mi "Senechka, dance with me."
    me "What? But I..."
    mi "Please, please, please, please!"
    "She made such a charming grimace that I couldn't refuse her."
    th "I couldn't have..."
    dreamgirl "But she doesn't need to know that, does she?"
    "The discarded sandals and socks were still lying under the bench, Miku had gotten rid of her shoes even earlier."
    "Anyway, it was a barefoot dance."
    "To a beautiful slow tune in the moonlight."
    mi "What a beautiful moon. {w}And huge..."
    "Her voice was barely audible."
    "She put her hand on my shoulder and I put my arm around her waist."
    "Even after almost an hour of dancing, Miku breathed easily and hardly got wet."
    "That's what training means."
    "There's something about it, though. There's a certain special beauty in the fact that this young creature had just put herself out there dancing and had come to me for some rest and quiet."
    "And then her scented oils kicked in full force, and it was as if I'd dipped into a bouquet of flowers generously sprinkled with leaves."
    "A happy sigh, a heavy head on my shoulder, and a wave of hair that somehow doesn't go up my nose at all - which is expected with that hairstyle."
    me "It's called a super moon."
    "I exhaled, pulling her close to me."
    me "Do you have anything related to the moon in your culture?"
    mi "Related?"
    me "I don't know. The color of a fern on a full moon leads to riches, nailing a firefly on a full moon leads to a breakup..."
    mi "I probably won't remember."
    "She was silent for a while and, taking in her chest of air, she gave out:"
    mi "Except for one omen that you have, too."
    me "What's that?"
    dreamgirl "On the days of a super moon you can attract good luck. It is considered special good luck for a girl to kiss her lover for the first time in the light of the full moon."
    th "Lo... what?"
    dreamgirl "That, that..."
    if alt_day2_mi_date == 3:
        th "And then, it won't be our first."
        dreamgirl "I mean the real one - the one that's mutual, when you're like two jerks pulling your lips toward each other, you know?"
    mi "They say that if you kiss someone when the moon is huge, it's forever..."
    "She must have blushed a lot, I don't know."
    "Somehow it suddenly came to mind that a real strong relationship is not looking at each other, but looking in the same direction."
    dreamgirl "That's romance! Come on, the night, the moon, the beautiful girl next to you - so much so that your heart sinks."
    if herc:
        th "Romance? In hell I've seen your rrrromance."
        dreamgirl "Yeah, sorry. I keep forgetting you're a cynic and a misanthrope. You're also an insensitive hollow log and stuff."
        dreamgirl "But seriously, what do you think?"
        th "What?"
        dreamgirl "Do you have a chance?"
        dreamgirl "Even if it's vanishingly small, even if there's a whole lot of trouble with her, is there?"
        th "There's no problem with her - she's nice, she's easy-going, she's not the least bit starstruck, and-"
        "I was interrupted by a bitter chuckle."
        "And a picture-image jumped into my memory: the clicking of the mouse, the cheerful banging of the keys on the good old A4. And YouTube, a video with a title in Japanese characters."
        dreamgirl "And this is where we stop broadcasting."
        "I got blacked out - and no matter how hard I tried, I couldn't get the image back."
        dreamgirl "You don't need to go there. I'm telling you honestly."
        "The voice sounded with palpable consternation."
        dreamgirl "Don't remember, don't. Better spend the remaining four days with the girl."
        dreamgirl "Nice girl, pretty girl, in love with you to bits."
        th "What are you talking about."
        dreamgirl "What? Oh, pardon me, I'm talking out of my mouth."
        with flash
        "For a few seconds the moment froze, some word scrolled backwards in my ears, as if filled with absorbent cotton."
        dreamgirl "I say she likes you, you like her."
        th "Well. Sympathy. What's next?"
        dreamgirl "Tell me, you moron piece of shit - are you going to keep playing dumb or are you going to hug the girl after all?"
        th "But we're dancing!"
        "Without waiting for an answer from my subconscious snorting contemptuously, I gently released my fingers and placed my hand on Miku's back, enclosing her in an impromptu hug."
    elif loki:
        th "Romance? You do know that if this one cheats us, too, I won't have the strength to recover, right?"
        dreamgirl "Call me a sentimental twit if you like, but I want to give her a chance."
        th "And what if she doesn't take it?"
        th "Do you remember Ksana?"
        dreamgirl "But you're the one who's been hovering around her."
        dreamgirl "And she graciously accepts signs of your attention. {w}You're in the midst of a budding romance."
        dreamgirl "So tell me, Tyler, what do you want if you die tomorrow?"
        th "Why would I die?"
        dreamgirl "A metaphor. Your life is draining away by the minute, there's no time to be stupid."
        "Exactly - a moment of weightlessness in a car flying off a cliff. {w}And if you've never had the courage to confess your feelings to a stranger who's been sitting at the same desk with you since you were a baby, now's the time."
        dreamgirl "I don't know what will happen in four days when the shift ends."
        dreamgirl "It's possible that the shift will be over, your mythical 'parents' will meet you, and you'll start life all over again minus a few years."
        dreamgirl "Maybe you'll go back to your world, where there's no place for incredibly beautiful girls with sea wave hair and huge anime-style eyes."
        dreamgirl "And if there is, you don't have the determination in your life to just walk up and meet them. {w}What to say about a smile - which the likes of her sometimes need more than anything else."
        "I've got air in my throat."
        th "So you're suggesting we put aside all the sad experience and just try it?"
        dreamgirl "Yes. In the worst case scenario, you'll remain a friend to the pretty girl. Even though it's unlikely."
        th "What are you talking about?"
        dreamgirl "You've spent too much time together."
        dreamgirl "Of the four days you've been here, you've spent three with her - allowing only a run in to visit her daddy."
        th "And what, is that a bad thing?"
        dreamgirl "Notice she doesn't resent that moment at all."
        "Our breathing became synchronized, at the bottom of her eyes I could see myself - flailing, desperate, protruding with moisture under my eyelids."
        "And it was no surprise that I drained the reflections of myself with my lips, leaning toward the girl."
        "Drained and comforted, on an exhale finding the Japanese girl's lips with my own."
    else:
        th "So what?"
        dreamgirl "If you had exactly twenty-four hours to live - what would you want to do or have time to do?"
        dreamgirl "Just forget about the consequences and think - what do you really want to get done before you die?"
        th "I don't know!"
        dreamgirl "Think, then! What do you want?"
        dreamgirl "Come on!" with vpunch
        th "I want her! Her!"
        "A half stifled memory suddenly jumped into my head - more like just a video from the Internet of a girl in a familiar costume jumping around the stage."
        "Something I tried my best to instantly forget."
        dreamgirl "Okay, you didn't understand anything, I admit it."
        dreamgirl "You're an insensitive hollow log and I'm a bad motivator. Let's do this then."
        dreamgirl "What if it wasn't you, but her, she had four days to live? What would you do?"
        "The air got stuck in my throat."
        th "I mean... how?! What does that mean, four days?!"
        dreamgirl "That's it. Come on, make up your mind!"
        th "I don't know. I guess I'd like to..."
        dreamgirl "Bang! Too late! You're already dead."
        dreamgirl "Quick, what do you want to get done before you go down?"
        th "I'd like to spend them next to her."
        dreamgirl "Idiot."
        "I never dreamed this would happen - to think, on the third day we met, we became so close to each other."
        "And now that I've gotten my way, I don't know what to say."
    me "Thank you."
    mi "For what?"
    me "I don't know... I guess for agreeing to be with me."
    "She pressed herself closer to me."
    mi "Well... You've done a lot of things for me that I should be grateful for."
    mi "So you can consider this my way of saying thank you."
    me "How... That's it?"
    scene bg ext_night_sky_7dl
    show mi happy pioneer at center
    with dissolve
    mi "Gotcha!"
    "Her voice was very satisfied."
    mi "Of course not. Of course it's not just gratitude."
    show mi upset pioneer at center with dspr
    mi "I don't mind at all if we do it more often."
    me "Danced barefoot?"
    "Embarrassed by Miku's frankness, I was completely lost in thought."
    "So it's not surprising that I said something stupid."
    me "I promise a dance at the first call."
    mi "How silly you are."
    show mi shy pioneer at center with dspr
    "She put her index and middle fingers together - and slapped my forehead with a ringing sound!"
    "It didn't hurt, it didn't hurt... But I felt her rightfulness immediately."
    with fade
    "As if I hadn't felt it before. On a pheromone level."
    "On the level of empathy."
    "They say that if you love someone, you find everything about them admirable."
    "The way he walks, talks, breathes."
    "Little habits, like trying to blow a curl off his nose, you find fascinating."
    "The stream of consciousness, flowing nonstop, you regard as a kind of friendly warm environment, where you dive up to your ears, allowing yourself to dissolve your own self in the thoughts of the other."
    "What to say about such things as smells and tastes."
    "There was a rustling sound from the walkway, and Miku turned her head."
    "As if in slow motion, I could see her chin turn, the matte moonlight-white skin getting another millimeter closer."
    "And where it gets translucent, there's a fast, fast pounding vein."
    th "She's worried!"
    "I managed to think before the strange thing happened."
    "Who made the movement toward me is unknown. {w}But I managed to take a short breath."
    "And an exhale. The distance from her neck to my lips was reduced to a few angstroms."
    "I only had time to notice huge goosebumps running down the marble of her skin."
    scene black
    "Miku squeaked and collapsed in my arms."
    stop music fadeout 3
    "And I couldn't stay on my feet."
    "And we hit the floor."
    play sound sfx_chair_fall
    with vpunch
    play sound2 sfx_bodyfall_1
    pause(1)
    scene cg d4_mi_dj_lib0_7dl
    with fade
    stop ambience fadeout 2
    play music music_7dl["iamsadiamsorry2"] fadein 5
    "I must have passed out from the impact."
    "When I opened my eyes, though, I found myself..."
    "On top."
    th "I'm going to crush her!"
    "I got scared."
    dreamgirl "Very timely."
    "Anyway, I tried to take the weight of my own carcass off the fragile Japanese girl."
    "Leaned my arms on the boards, tried to straighten up..."
    scene cg d4_mi_dj_lib_7dl
    with fade
    "And then she opened her eyes."
    mi "Semyon?"
    "And I suddenly {i}felt{/i} her - everything we touched with through our clothes."
    "I was practically on top of her."
    "And she reached out and stroked my cheek."
    "There were only inches between us."
    "And neither side was in any hurry to get closer."
    "Miku - because she was underneath."
    "And I... Well, I just couldn't get enough of her."
    mi "Like me?"
    "She smiled slyly."
    th "Oh, she's playing around now!"
    me "You're pretty."
    "I said neutrally."
    mi "That's it?"
    "This is where I couldn't help myself and smiled."
    me "I got you."
    mi "I gave in."
    "We were silent again."
    "And I suddenly remembered what she said about kissing in the moonlight."
    mi "Are you comfortable?"
    "Without moving, she asked."
    me "Very."
    "I was torn between wanting to make eye contact and following my lips."
    "At one point, I was suddenly torn between thinking about what would happen if I had enough determination and..."
    dreamgirl "As if you have a choice."
    mi "It's very good that you're comfortable."
    "With a hint she said."
    "I couldn't see, but I could have sworn - her eyes shone with mischief."
    me "And you?"
    "The question was silly, no doubt."
    mi "Generally comfortable, thank you."
    mi "And after you let me breathe, it's great."
    mi "And no, I didn't hit myself, if that's what you're wondering - I tucked my head in just in time."
    "All this she said in an impossibly polite voice."
    "If I had watched all this from the screen while watching some movie, I would have smiled nonstop at the foolishness of the main character."
    th "But the problem was that now I was the hero!"
    mi "You can get up anytime you're ready."
    "She continued."
    mi "But if you still have some business to attend to..."
    "Here she, no longer hiding, smiled."
    mi "I can wait."
    "Business..."
    "The Japanese girl sighed."
    if loki:
        "And I, once again writing out an imaginary slap to myself, leaned forward, cautiously placing my palm under the back of her head."
        "It seems that in our couple, the care and concern for both of us fell on me - and I can't say I mind much."
        "And after the second time I inhaled her breath, I nipped her bottom lip a little, no longer with a timid 'may I?' but with a confident, smiling 'hi, I'm here, I missed you.'"
        "She rounded her already huge eyes in amazement - and a few seconds later dropped all attempts to get up, wrapping her arms around me."
        "On prom night, young men confronted with an unknown type of bust clasp kissed until dawn."
        dreamgirl "Are you going to kiss until dawn too, or...?"
        th "Shit, I can't do that!"
        dreamgirl "Semyon, for her it's not just about getting laid. Remember, they have a different culture, and what your body wants the most right now..."
        th "Not tonight."
        mi "Will you help a girl up, handsome?"
        "Laughed Miku, who had clearly seen the whole course of my thoughts."
        me "What about..."
        mi "What about what?"
        "I exhaled."
    else:
        "She seems to have understood perfectly well that I shouldn't be expected to do anything here and now."
        "And it's not that I don't like her-not at all!"
        "But what kind of autistic person am I if I get everything all at once?"
        "So she hissed and leisurely began to crawl out from under me."
        dreamgirl "Aah! I don't want it! Give her back, retard!"
        th "We didn't get enough of this, do you want to go on?"
        dreamgirl "I don't mind! She would have kissed me by now for sure!"
        th "Well, well. At least she didn't 'sleep with' me."
        dreamgirl "I can do that. Haven't you noticed what a comfortable position this is?"
        "A whole image of smell, taste, touch, up her skirt, and an achingly sweet moment of togetherness was thrown from her subconscious mind."
        dreamgirl "Well, realized? If I remember the Japanese correctly, Miku has all these things inextricably linked - kisses, romance... And sex."
        mi "You can get up if you want."
        "Softly she laughed from somewhere above."
        mi "Although you've probably already guessed that."
        me "Yes, thank you..."
    scene bg ext_musclub_night_7dl
    show mi smile pioneer at center with dissolve
    stop music fadeout 3
    play music music_list["goodbye_home_shores"] fadein 3
    "Some unknown force holding me immobile is finally gone."
    dreamgirl "The power of rheumatism?"
    th "Chatterbox."
    "At last I straightened up and stood up."
    show mi shy pioneer at center with dspr
    mi "Welcome back to the world of the capable."
    "Embarrassed, she smiled."
    mi "I figured you had something jammed in your back, a familiar thing, Pa gets like that sometimes."
    mi "Would you like a massage?"
    "Without any transition she inquired."
    dreamgirl "Wow!"
    "Fully in solidarity with me, my subconscious mind, in a kind of stunned shock, had even forgotten that it was rankly supposed to sarcasm and poke fun at those around it."
    "I don't think I would have been more surprised, even if the question followed in the vein of 'American Pie' - like, well, we're going to go to bed there soon, because I'm ready."
    me "Massage."
    mi "Yes! Massage! I'm not very good at it, but I was able to give my father a back rub, and he walked for a week afterwards more or less."
    show mi smile pioneer with dspr
    mi "Of course, it's all pampering. You have to go to a professional, they'll look at your back, prescribe a treatment, and stretch you out properly."
    me "Do you think it's worth it?"
    "I have my doubts."
    th "Who's going to catch us in this interesting pose?"
    dreamgirl "So what? Do you think they'll kick Miku out of the pioneers?"
    "I agreed that the loss would be enormous."
    "Still can't make this evening any more awkward."
    me "What's to be done, will you tell me?"
    mi "Nothing much."
    "After walking around the patio for a while, the Japanese girl picked a comfortable spot on the exit - where the two steps went down."
    mi "Pull down your shirt and sit down."
    me "Are you sure?"
    show mi happy pioneer at center with dspr
    "I think one of us is clearly reveling in the other's embarrassment."
    mi "Yeah. Come on, or we'll have to stab later - Viola won't let go of such a chance."
    "That instantly resolved the argument in favor of the 'masseuse' - after all, I didn't want to let a nurse with her needles near my body."
    "So I had to submit to threats of reprisals and metal needles."
    "I pulled my shirt off over my head and sat on the step, exposing my bare back to Miku's warm palms."
    mi "It might hurt a little, but I'm not going to push full force just in case."
    "Not full force is..."
    with flash_red
    "It's like I've been split in half."
    "If I hadn't choked on my exhalation, the whole camp would probably have come out screaming."
    me "What are you doing, pest? Do you want me dead?"
    mi "And I'm done, it's over, and you're the best."
    "However, the palms from my back never went away."
    "What's more, they started on their own way down the sides."
    "Along the ribs - slowly, unhurriedly, letting you feel every millimeter of the touch."
    "My shoulders twitched reflexively, dispersing stagnant blood."
    "And warming waves ran down from the top of my neck."
    me "Miku, is this also part of the massage?"
    "I asked hoarsely."
    mi "I guess you could say that."
    "Something creaked behind me, exhaled."
    hide mi with fade
    "I was looking in the direction of the paved concrete walkway, so I didn't immediately notice the narrowing of my field of vision."
    "For on the left and right he was now bounded by slender legs in stockings."
    "Miku sat down a step higher on the same staircase, wrapping her legs around me."
    "And her naughty hands finally moved from my sides to my belly."
    "That feels good..."
    dreamgirl "Did you know that if you twist 180° right now, you can get a detailed look at her panties?"
    if ('music_club' in list_voyage_7dl):
        th "Really? Haven't you had enough stripes the day before yesterday?"
        dreamgirl "Not enough? If you must know, there can't be many of those things at all!"
        "The subconscious mind was still snorting and grumbling something, like a huge cat settling in for the night-it knew something I hadn't guessed."
        "So it considered its job for the day done."
    "I was embraced, and two delightfully firm mounds pressed against my wrinkled back."
    th "Is she seducing me or something?"
    "All this falling, dancing, singing - weren't they all part of the same insidious plan to get my attention?"
    dreamgirl "Even if they were, you failed that plan."
    dreamgirl "I hope you don't screw up at least something as small as..."
    th "Like what? Longsuffering?"
    mi "Semyon..."
    "Miku softly called."
    me "Yes?"
    mi "You're too tense. Relax."
    me "I am relaxed."
    "There was a contemptuous snort behind me."
    mi "Senya, I mean it. Relax already, I won't eat you."
    me "If you won't eat me, then you're at least going to bite."
    "Habitually I muttered, letting my shoulders slump."
    "I was trying to catch a glimpse of her with my side vision, so I turned my head sideways to the point of refusal."
    "And then I didn't have time to do or understand anything."
    "Just the maiden's breasts pressed even harder into my back and soft lips touched my lips."
    if not loki and alt_day2_mi_date != 3:
        dreamgirl "Your first, huh? Congratulations."
        dreamgirl "It's also on a super moon. {w}Well. Love and advice."
        th "Are you starting again?"
        dreamgirl "Not in the least! I wish you would settle down, sir."
        dreamgirl "Miku is as good as any other. The perfect girl with no cockroaches and no hang-ups."
        dreamgirl "Take the beauty, she's all yours. Come on!"
    "Kissing on the steps by moonlight is real romance."
    "I waited until she tried to turn away, and then I turned and caught her myself."
    "Not this time, honey."
    "The experience is just a memory, of course, but..."
    th "You can refresh your memory."
    "I thought, kissing that soft smile."
    if (not loki) and (alt_day2_mi_date != 3):
        "Our first kiss."
    "Wrapping her palms around my face, Miku leaned back somewhere, taking me with her."
    show mi sad pioneer at center with dissolve
    "I never thought you could get so much pleasure from a simple kiss."
    "Even considering where and what my hands were doing."
    "She wasn't wearing a bra."
    "Her panties were petite and didn't resist the greedy fingers."
    show mi shy pioneer at center with dspr
    "And I kept kissing and kissing her."
    "Remembering what made the evening languid, I found a place under her ear and led the way with kisses, tearing a sweet moan from the maiden's lips."
    "I wanted myself in her."
    "To understand why she was so good and beautiful."
    "To understand why we became together."
    "Surprisingly, there was shaking and teenage excitement in my actions, but the sex itself wasn't there."
    "There was a desire to bring as much pleasure as possible."
    show mi grin pioneer at center with dspr
    me "You can make up for lost time, can't you?"
    "I undid the two bottom buttons on her shirt."
    "The skin of her belly was delicious - taut as a drum, firm, warm, alive."
    "Both my hands ended up under her skirt on her thighs."
    me "Eh, I wish I could get rid of the rest of your clothes, and..."
    mi "So what's holding you back?"
    "She whispered, kissing my neck."
    show mi happy pioneer at center with dspr
    me "Let's go sleep, miracle."
    me "Before the whole camp really comes out to stare."
    "Shuddering at the pleasant tickle, I suggested."
    "The bushes moved suspiciously for the third time, and I threatened them with my fist."
    "A chuckle came from there."
    "I threatened again."
    "Finally the unknown 'someone' laughed out loud - in a thin, recognizable voice - and the retreating footsteps let me know that my instincts were right."
    "I smiled at Miku."
    me "I don't know about you, but I consider such things intimate... I don't want them in public."
    "Miku laughed softly."
    mi "Noticed our appreciative audience too?"
    mi "I kept waiting for you to pay attention."
    "She smiled serenely, kissing my temple."
    mi "But you're right, even though I hate to let you go - my eyes are already slipping."
    me "I'll walk you out."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_dj_sleeptime:
    scene bg ext_house_of_mt_night_without_light with fade
    play ambience ambience_camp_center_night fadein 1
    play music music_list["a_promise_from_distant_days"] fadein 2
    show mi happy pioneer at center with dissolve
    "Inhale-exhale-sigh-creak."
    "Empathy."
    "Her throat is clogged, and she's talking in a hoarse voice."
    "It makes me want to cough."
    if (alt_day2_date == 'mi'):
        "Maybe it wasn't such a paper metaphor that she said she cries when I'm hurt."
    if not loki and alt_day2_mi_date != 3:
        "The first step we took-and the credit goes only to the girl. I never managed to do anything that required determination."
        "She did everything for me."
        th "It seems to be my cross to spend a lifetime indifferently waiting for a miracle that will be persistent enough to overcome my defenses and interested enough to stick around afterwards."
    me "You are my miracle."
    "I whispered, pulling a dislodged curl away from the girl's face."
    me "You have no idea how much."
    "The step is taken, the walls have fallen, and it feels like..."
    "I don't even know, but it has to be under the skin, into the nervous system, inside."
    "Not to break the kiss? Don't let go of my hands? Don't take your eyes off?"
    th "Don't let her go."
    me "And I don't want to leave."
    mi "Yes..."
    show mi happy pioneer with dspr
    "The classic pose from the movie adaptation of 'Gone,' the supple loin, sagging under my arm, the figure nestled against the chest."
    me "Let's not go anywhere?"
    mi "Yeah."
    "Let's take forever in half, shall we? A few million endless 'nows' spitting in the face of a bursting memory."
    "Somehow I think you don't exist and can't be, that your fluttering under your clenched palms is the ticking of electricity in a sleeping being, the anabiosis of the higher nervous, creating another world at the junction between the closing and opening of the century."
    me "Can I kiss you?"
    show mi smile pioneer with dspr
    mi "You've asked me that the last five times."
    me "And I got it."
    show mi laugh pioneer at center with dspr
    mi "That's for sure."
    "Objective reality is an illusion caused by electrical impulses in the brain."
    "We've all seen the Wachowski Brothers' Netflix."
    "The most important thing is the impulse in the brain. The imagination will finish the rest."
    "All those irresistible, captivating little things, like the smell of hair and the faint smell of sweat that came through even the essential oil."
    "Like a loose thread coming out of a seam on my shoulder."
    "Like a naughty curl that kept getting in her eyes."
    me "Shall we go back to the club?"
    mi "Then we'd better go to the radio room - it's the farthest away."
    me "And we're the only ones with keys, that's for sure."
    "What a clever girl she is. She's thought of everything."
    show mi smile pioneer at center with dspr
    me "Shall we go?"
    mi "Temper your ardor, Romeo."
    "The girl laughed, and I could barely keep myself from starting to pester again."
    th "What's the matter with me?"
    dreamgirl "Hormonal imbalance."
    dreamgirl "Oh, and your girl said it's okay, too. {w}It's too bad you don't have much time, and then you go back to your place, where she..."
    th "And this is where we smoothly shut up and don't say another word about my home."
    me "Or at least let's go for another walk?"
    mi "No, sunshine. I'm really having a hard time keeping up."
    show mi happy pioneer at center with dspr
    "She peeled away from me with displeasure."
    mi "There's plenty to do tomorrow, too. I hope you'll help me."
    "Miku took a step back."
    "One more without letting go of my hand."
    me "But I don't want to."
    mi "And I..."
    "We stood two meters apart, holding our arms outstretched as best we could in a grotesque semblance of a ballet."
    show mi sad pioneer far with dspr
    mi "Let's go on three-four, otherwise I'm really not leaving."
    me "Okay."
    "I sighed and counted - and... It was like I was half the size when my fingers stopped feeling the warmth of her hand."
    mi "I'll look forward to tomorrow. And you."
    hide mi with pixellate
    "And ran away."
    play sound sfx_open_dooor_campus_1
    stop ambience fadeout 1
    scene bg int_house_of_mt_noitem_night
    with fade
    pause(1)
    play ambience ambience_int_cabin_night fadein 1
    "The cabin was empty."
    "The moon didn't seem to be the only one that put me in a romantic mood that night."
    "But I really was tired."
    "I only had the strength to pull my tie and shirt off, fleetingly inhaling the scent that permeated the fabric."
    "Eucalyptus. A tag that is now forever associated with a beautiful Japanese girl by association."
    dreamgirl "You're right, let you have as much of it as you can."
    "I shrugged and, throwing off my clothes, dove under the covers."
    th "More is just hiding her in my pocket."
    dreamgirl "Do you think she'll mind?"
    th "I think so. {w}She needs a stage and an audience. She won't last long in introvert mode."
    dreamgirl "But it's great to have someone always waiting for her backstage, isn't it?"
    th "Of course it's great!"
    "I imagined the nervousness of watching her perform from the front, holding a water bottle, and I smiled."
    show blink
    "I closed my eyes."
    "And then I thought of nothing but that."
    "And the memories unfolded in my mind all by themselves."
    if alt_day4_mi_dj_hedg:
        "…The hunt…"
    if alt_day3_technoquest1 == 0:
        "…Turning a cluttered room into a comfortable radio room…"
    else:
        "…Fight with Dvachevskaya…"
    "…Movies and memories of father…"
    "…Miku's concert, my stupor at the clubs…"
    if alt_day2_mi_date != 3:
        "...And finally the first kiss!"
    "My eyes were already slumbering, and under my closed eyelids, she was waiting for me again."
    "Only slightly worse than the real thing."
    scene cg d1_end_of_day_7dl with dissolve
    "Mi…"
    scene black with fade2
    "I fell asleep before the sound of her name died out."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_dj_begin:
    scene anim prolog_1 with dissolve
    play music music_7dl["lastlight_piano"] fadein 2
    "I had a dream."
    "It was a little out of my usual series of pleasant dreams, part erotic, part romantic."
    "This dream was about everyday life."
    "It was about everyday life."
    "She's running ahead of me, trying to keep her balance in her high heels."
    "Why did she even wear them to the airport?"
    "She also grumbled, 'It's not every day we go to places like this, you could have picked something nicer'."
    "Anyway, she runs ahead of me, I run behind her, balancing a thousand bags and purses."
    "I guess it all started when I agreed to hold off on the wedding so that the hall could accommodate all the thousand freeloaders invited."
    "«For my princess» — said I and did everything."
    "That's where it all started - almost identical to her own song."
    "A kiss on the cheek - there's glitter on her lips, you'll smudge it, you bastard, don't eat the glitter."
    "By the way, didn't you look, I got a new haircut today. What, you can't tell the difference? It's a whole shade darker and an inch shorter - see, the ponytails don't reach my ankles anymore!"
    "Putting her coat on out of my hands is not even an option, helping her to undress - well, she can't bend over herself and risk crumpling an expensive dress."
    "That's why I'm quiet, meek, and short-tempered."
    "Yes, yes, your hand is too empty, I am in a hurry to put it in my palm."
    "A beautiful princess needs adoration and nothing else."
    "After unloading the bags in the waiting room, I retreated to the men's room to stare a little at the wall over the urinal."
    "There was a clatter of heels behind me and a voice behind me demanded ice cream."
    "I don't know if she wanted to find ice cream in the bathroom, but... It's just a sweet mistake."
    "Even though I wanted to pull the brakes, to let us say mean things to each other - which I will no doubt regret."
    "Especially when she said a real prince would come and take her to magic land."
    me "He'll take your ass with a strap!"
    "I barked and woke up."
    dreamgirl "Well, how do you like a step closer?"
    th "What?"
    dreamgirl "I say, what do you think of the sketch of life next to Miku?"
    th "It's just a nightmare."
    dreamgirl "Well, I'm comparing what I know about her with how your relationship is going..."
    th "How do you know so much about her?"
    dreamgirl "I told you all day yesterday..."
    th "Well, stop. I don't want to know."
    "I must have looked very funny from the outside, with a dreamy glint in my eyes."
    th "This nightmare... You know..."
    dreamgirl "What?"
    th "I liked it!"
    dreamgirl "No!"
    th "I mean it! It's probably something I've wanted all my life."
    play music music_list["reflection_on_water"] fadein 3
    scene
    $ renpy.show("bg int_house_of_mt_sunset", what = Desat("bg int_house_of_mt_sunset"))
    with fade2
    "This is the second time I've managed to give my own inner voice a preinfarction."
    "Looks like I got a handle on it."
    show unblink
    "So I woke up in a high spirits mood."
    "A split second before my shoulder was touched by the squad leader."
    show mt normal pioneer with dspr
    mt "Hey, get up slowly. Breakfast in ten minutes."
    me "Breakfast? What happened to the voluntary-coercive procedures?"
    show mt smile pioneer with dspr
    mt "Listen."
    me "Why?"
    mt "Listen, I say!"
    play ambience ambience_7dl["rain"] fadein 3
    "I followed my leader's demand, and through the walls of the cabin I heard the measured sound of drops on the roof."
    me "It's raining?"
    mt "Yes. So all lineups and exercises are cancelled, breakfast later - that's the routine."
    "She thoughtfully weighed her raincoat in her hand and hung it on the hanger by the door."
    mt "Come on up. Put this on."
    "She stood in the doorway, revealing a cane umbrella of unknown origin, and a gust of wind blew a whole handful of icy spray into the room."
    me "Olga Dmitrievna!"
    mt "You don't like it?"
    "She laughed."
    mt "Don't be late."
    play sound sfx_open_door_kick
    pause(1)
    hide mt with dissolve
    "She disappeared, letting me get dressed."
    "Grumbling something not very intelligible about the evil pioneer leaders who wander around until one o'clock in the morning and then have the nerve to get up before the pioneers and look as blooming as the May rose, I spread my left leg out from under the covers, gauging the temperature outside."
    th "It seems tolerable."
    "I held my breath and..."
    if alt_day3_technoquest1 >= 1:
        "That's where I got bogged down - my shirt was nowhere to be found!"
        if not alt_day4_mi_dj_hedg:
            "The same cotton shirt I'd spent the last three days trying to figure out!"
        "Instead there was a brand-new shirt rolled up around the cardboard, snow-white, never worn."
        th "What the..."
        dreamgirl "'Mommy' must have taken it out to laundry."
        "I saw no other explanation for this, so after shaking the cloth in the air a few times, I tried to get into my uniform as quickly as possible - the surprise passed, but I didn't have time to get warm."
    "It took me less than forty seconds to pull myself together, and the sting of the cold air only encouraged me to act even faster."
    "It suddenly occurred to me that it would be nice to get my clothes under the blanket ahead of time - I used to do that at home a lot when the jerk utilities guys decided once again that twenty degrees was not freezing temperature and no heating was necessary."
    dreamgirl "That's right, you'd get into some warm clothes..."
    th "Well!"
    dreamgirl "...and would have been rattled out of the canteen for showing up in a crumpled uniform."
    "The subconscious continued as if I hadn't even interrupted."
    "As long as it laid it out this way..."
    th "I think I'd rather freeze for a while."
    dreamgirl "Reasonable decision. And no, that's not how you put the raincoat on. Are you looking for buttons in it?"
    dreamgirl "Imagine putting on a dress."
    th "What?"
    dreamgirl "Well, a dress! Useful experience, obviously it will come in handy in life."
    "I finally found the neck of my cloak of waterproof fabric and put my head in it, and really, it's like putting on a dress."
    dreamgirl "All right, now let's go! On to conquering the washed-out ground, the rain in my eyes and the cold water behind my scruff. All to meet Miku!"
    th "You know how to cheer."
    play sound sfx_open_door_kick fadein 0
    scene cg d5_rainy_idle_7dl
    with dissolve
    pause(3)
    "Looking hostile at the drenched sky, I squeezed my head into my shoulders, wrapped myself in my raincoat as best I could, and ran to the cafeteria."
    "Got there in three minutes."
    play sound sfx_open_door_2
    return

label alt_day5_mi_dj_breakfast:
    scene bg int_dining_hall_people_rain_7dl with dissolve
    play ambience ambience_dining_hall_full fadein 3
    "The canteen was packed to capacity."
    "No wonder - for once all the pioneers were fed at the same time."
    "I had almost resigned myself to the idea of having to wait for someone to eat and make room, but then someone grabbed my arm."
    show mi smile pioneer with dspr
    mi "Hi, Senechka, how do you like the weather, do you like it? I like it too, I love rain in general, I have a song about it too, do you want me to sing it?"
    mi "Well, it's not really about the rain, it's more about walking around Shinjuku, with the obligatory entrance to Shinjuku Goen under the shade of thousands of Japanese cherries. Sakura. That's the name they have."
    mi "How did you sleep? I always sleep well with the sound of rain, don't you? Some people get headaches from the change in weather, but that's because their blood pressure is low, and your blood pressure is normal?"
    "She blurted out in a volley, not distracted by nonsense like breathing."
    th "Nervous."
    dreamgirl "Thinks you're about to pretend nothing happened yesterday."
    th "Why do I have to pretend like that?!"
    dreamgirl "Because you've done it a few times already, I guess. Mind you - this particular girl isn't going to let you go silent in the corner."
    th "It's not like I wanted to. The most important thing, 'may I', has already been said."
    "The smile said it all - that I hadn't forgotten anything, that I didn't regret anything, that I didn't want to fix anything."
    "And the fact that I missed my little japanese girl while I was sleeping."
    me "Hello, Miku. I missed you, too."
    me "And you don't have to talk at machine-gun speed at all."
    show mi upset pioneer with dspr
    mi "Oh. I'm babbling again, aren't I?"
    "She waited for my nod."
    show mi shy pioneer with dspr
    mi "Well… Then… I'll try to… Talk… Slower."
    "Honestly, I didn't mean to! The chuckle came off my lips all by itself."
    "But it was only my reaction that helped me catch the pouting starlet's hand and pull it toward me."
    me "I'm really, really glad to see you. But let's get something to chew on before I start looking at you with gastronomic interest."
    show mi laugh pioneer with dspr
    mi "You're right! We should have breakfast. {w}I saved you a seat, by the way!"
    "She had the most boastful look. {w}I played along. It's not hard for me, but it's good for her."
    me "Great! Now it's time to eat."
    hide mi with fade2
    show un normal pioneer at right
    show el normal pioneer at left with dissolve
    "The Japanese girl took me to a table where Lena diligently held two seats, more or less successfully fending off Electronik's attempts to steal a vacant chair."
    me "Hi."
    show un shy pioneer with dspr
    un "H-Hello."
    "Lena blushed a little when I approached, but pretended that nothing had happened, and, further ignoring me, turned to Miku:"
    un "I held on to the seat. Thank you. I'm free to go."
    show un normal pioneer at center
    show mi smile pioneer at fright
    with dspr
    mi "Of course, of course, Lenochka, thank you so much!"
    "The unsociable girl nodded and disappeared from the radar - as if she had fallen through the earth."
    hide un with dissolve
    show mi normal pioneer at right with moveinright
    "Electronik, who had already figured out that he wasn't going to get any fish here, also hurriedly vacated the area."
    hide el with dissolve
    show mi smile pioneer at center with moveinright
    "We sat next to each other, touching each other's knees under the table."
    "Rice porridge risotto, tea, and two cheese sandwiches - certainly a breakfast of All Time!"
    "After offering a prayer to Random for the nibbles, I stuck my spoon into the white mass on my plate and moved my jaws silently for a while."
    mi "Senechka, what are you going to do?"
    me "Ahem..."
    "After I finished chewing, I turned back to the Japanese girl."
    me "Right now?"
    mi "Yes!"
    me "I have plans to finish my porridge, then take my tea..."
    show mi laugh pioneer with dspr
    mi "Stop it!"
    "She aimed to slap my forehead with her fingers again."
    "But she was distracted."
    mt "I don't care!"
    mt "Or do you want to talk to the camp leader about fighting on camp grounds?"
    play music music_list["awakening_power"] fadein 2
    hide mi
    show dv_mt_7dl
    with dissolve
    "We turned sharply toward the source of the noise."
    "And somehow I wasn't the least bit surprised by what I saw."
    th "Dvachevskaya, who else?"
    "To tell you the truth, until recently I thought her reputation as a daredevil and trouble maker was a bit of a blown out of proportion - well, as it usually is."
    "You build a reputation for yourself with a few well-judged actions, then you can relax and let the reputation work for you."
    "In interpersonal relationships it's not a panacea, because sooner or later you're going to screw up somewhere and not get the mask on in time."
    "But in the individual-society connection, it works just fine."
    "Especially if you're a goddamn introvert and prefer any other leisure time to one that requires solo work - even when it comes to building up the tricksters."
    "But Alisa seemed to be completely consistent with what they say about her."
    if alt_day3_technoquest1 >= 1:
        mt "Or do you think I took so much pleasure in washing blood off the shirt that I didn't have to explain where the stains came from?"
        dv "No one forced you."
        "Alisa sullenly replied."
        mt "Really? So you should have just thrown it in the laundry room. So they could file a statement with the director, in full compliance with the rules?"
        dv "I don't know, I don't care."
        "The way she acted and the way she jabbed yesterday confirmed her gangster reputation completely."
        "But then Olga once again showed the light - what is a good teacher and how it differs from mediocrity. And, lowering her voice, she hissed a few words."
        "After which it was as if they had let the air out of Alisa."
        "Her upturned nose instantly went to the floor, and Alisa blushed and hunched over in her chair."
        "I don't know if she is familiar with the concept of «shame», but right now she was dangerously close to it."
        mt "I'm waiting!"
        dv "Coming…"
        scene bg int_dining_hall_people_rain_7dl
        show dv guilty pioneer with dspr
        "Alisa came up to me and began:"
        dv "Uh… Newbie…"
        mt "Semyon!"
        show dv sad pioneer with dspr
        dv "Yeah… Semyon."
        "Alisa shuddered."
        me "Yes?"
        "Just in case, I got ready to defend myself with a bowl of porridge."
        "Getting punched in the nose again was not a great prospect at all!"
        dv "I… For yesterday…"
        show dv shy pioneer with dspr
        dv "Apologize…"
        "She kept talking quieter and quieter."
        mt "I can't hear you!"
        dv "Semyon, don't be offended about yesterday."
        "She had great difficulty with words."
        me "Uh…"
        show dv sad pioneer with dspr
        dv "Well… Can I go?"
        me "Go."
        "She took a step and…"
        show dv shy pioneer at cleft with moveinleft
        mt "Dvachevskaya!" with vpunch
        stop music
        stop ambience fadeout 6
        "The perfectly timed voice of the squad leader easily blocked out the commotion in the canteen - everyone fell silent with surprise."
        show dv sad pioneer at center with moveinright
        mt "Don't piss me off!"
        "In what had become a deafening silence, Alisa, obviously freaked out, turned abruptly to the leader."
        dv "I have nothing to apologize for!"
        mt "Let me decide that, honey."
        "Snorted the squad leader."
        mt "You've been spreading your hands, especially on a man on duty. {w}Come on, we're all waiting for you."
        show dv angry pioneer with dspr
        dv "Why was he opening his mouth!"
        show mt normal pioneer far at fright with dissolve
        mt "Mouth?"
        "Olga stepped closer so she wouldn't have to shout across the dining room."
        "In vain - the attention of everyone present, including the cooks and a quietly giggling Violetta, was concentrated on «Santa-Barbara»."
        mt "So you hit him because he insulted you? Really? {w}What did he say then?"
        show dv normal pioneer with dspr
        dv "He said…"
        "Cheerfully Alisa began."
        dv "…that…"
        show dv shy pioneer with dspr
        extend " I will go to…"
        "She staggered back and stared at me in horror. The girl's lower lip trembled, indicating hysteria."
        show mt angry pioneer far at fright with dspr
        mt "What?"
        "The leader continued to mock her."
        mt "What could he have said that deserved a beating?"
        dv "N-no… N-nothing."
        "She went pale, then blushed, but in a surprisingly steady voice - giving off a lot of inner tension - she replied:"
        dv "He really didn't deserve it."
        "I think we've just stepped into DvaChe's terra incognita. Which the counselor was well aware of. And about which the redhead tried her best not to spread the word."
        "So she appreciated the chic gift - being able to just apologize without flaunting her underwear."
        show dv guilty pioneer with dspr
        dv "Listen."
        "Alisa looked me in the eye."
        dv "I did a big nasty thing, I don't know what came over me. I just wanted to hurt someone."
        me "What's the big deal. If someone had told me..."
        show dv angry pioneer with dspr
        "I hesitated - the girl's eyes became threatening, then pleading."
        me "Something under my arm!"
        show dv normal pioneer with dspr
        "I got out of it."
        me "I'd be mad, too..."
        show mt normal pioneer far at fright with dspr
        mt "Alisa, you're not apologizing for me, remember?"
        "The leader interrupted me."
        show dv sad pioneer with dspr
        dv "Yes."
        "In the silence of the hall, Alisa uttered. The eyes of everyone present were fixed on her."
        dv "Please forgive me."
        mt "SEMYON!"
        dv "Yes. Semyon."
        mt "FORGIVE ME, PLEASE, SEMYON!"
        show dv shy pioneer with dspr
        dv "Please forgive me, Semyon."
        "And I felt so uncomfortable, as if I'd done something wrong. And I wanted to close this burlesque quickly. A subtle psychological trick that prevents the victim from saying no."
        me "Cut the crap. Let's pretend it never happened."
        "And as if the sun came out of the clouds, Alisa smiled cheerfully."
        show dv smile pioneer with dspr
        dv "Olga Dmitrievna, have you heard?"
        mt "I heard. Now your second transgression..."
        dv "Well, that's for when the rain stops!"
        "Jolly shouted Alisa, running out of the canteen."
        hide dv with moveoutleft
        "The door slammed behind her, and everyone's attention shifted to the remaining actors."
        "And while Olga was not used to publicity, it was an ordeal for me every time."
        "Blushing, I stared at my plate, trying to look as absent-minded as possible."
        play ambience ambience_dining_hall_full fadein 3
        "I don't know if it worked or not, but a few seconds later the babble resumed."
        hide mt with dissolve
        "Nodding to me, Olga sat down at the table next to the nurse."
        show mi angry pioneer with dspr
        mi "Turned badly, you say?"
        "Miku looked at me angrily."
        me "What?"
        mi "Blood yesterday. You said you unfortunately turned."
        show mi dontlike pioneer with dspr
        mi "And now I see who turned you around so badly!"
        me "Uhhhh..."
        mi "What «uh»?!"
        show mi angry pioneer with dspr
        "Miku looked really pissed off."
        mi "You lied to me!"
        th "I think I'm about to be slowly and relishingly smeared on the walls and ceiling."
        dreamgirl "Why did you lie, dumbass?"
        th "I don't know... For the sake of having a choice."
        dreamgirl "The ability to choose is the bill of those who have the balls to defend it. Yes, you didn't set Miku up yesterday, but how did you take advantage of the choice that opened up?"
        th "Come on. I have enough enemies as it is."
        "I expected Miku to be offended, walk away, or knock me in her turn."
        "Fortunately, she decided it was okay to forgive for the first time."
        mi "Don't you ever lie to me, do you understand? {w}It hurts to know that you're not telling me the truth."
        show mi sad pioneer with dspr
        mi "I'll forgive you anything. Except lying."
        "The expression was not uncontroversial, but right now it was wise to agree."
        mi "Do you understand?"
        me "Yes."
        "I nodded readily."
        show mi smile pioneer with dspr
        mi "Wonderful!"
        "She kissed me on the cheek and stood up."
        mi "Waiting for you in the radio room."
        hide mi with dissolve
        "And she headed for the door, leaving me alone with the cold porridge."
        "Bloody apologies, unnecessary arguments, arguments... And the worst part is, it's all in full view of the whole camp!"
        th "Definitely not Beckham's day."
        dreamgirl "I second that. Come on, get it over with and go make up with your sweetheart."
        "That was the first sensible thought I heard today, so I immediately rushed to heed it."
        "So breakfast was ended early."
        me "No way, you've been out of sight for ten hours as it is. I won't give you another minute!"
        "I caught up with Miku and stood next to her."
        show mi laugh pioneer with dspr
        mi "What, you won't let me go to sleep anymore?"
        me "Yes!"
        stop ambience
        stop music
    else:
        "She was standing in front of the squad leader, leaning her fists on the table, and she was grunting something."
        "And the leader just kept talking and talking."
        mi "What do you think happened with them?"
        "I shrugged."
        me "Who knows. Probably did some nasty thing again last night. Wrote an obscene word on Genda's forehead or smeared soot on the doorknobs."
        scene bg int_dining_hall_people_rain_7dl with dissolve
        show mi laugh pioneer with dspr
        mi "That's right! Alisa can do that."
        me "Can-can. The main thing is to stay away from her at such moments - she attracts trouble just by the fact."
        dreamgirl "Oh, that's a familiar characterization!"
        "The subconscious mind didn't fail to quip."
        dreamgirl "Couldn't exactly the same thing be said of you?"
        th "I'm only dangerous to myself, the people in the midst of my failure are in absolutely no danger."
        dreamgirl "Uh-huh, excluding spoilage, the evil eye, seven years of celibacy, energy leeching, and whatever else those charlatans in the papers are all threatening to remove."
        th "But that's not true!"
        dreamgirl "You don't have a long enough sample of your target audience, you can't speak with accuracy. Maybe your bad luck is sticking, and you just rolled Miku out of a couple of successful albums."
        th "Okay, this circus stopped being funny. I'm not a bringer of bad luck!"
        dreamgirl "If you don't bring bad luck, then you must bring good luck. Prove it. Loser."
        "Throwing one last image with a long tongue sticking out, the subconscious went silent."
        mi "I don't talk to her much as it is, though we could have become friends on the basis of common interests."
        me "Yeah? Like what?"
        show mi smile pioneer with dspr
        mi "We both love music! There!"
        me "Oh... Well, that's right."
        "Suddenly I remembered some particularly hot nights, when the guys in leather and the guys in wide pants would go wall-to-wall."
        "They like music, too, you know. Or they're just fans of international wrestling festivals, I don't know."
        me "You know, I'd rather not. I suggest you be friends with me. I'm better."
        me "And prettier."
        show mi laugh pioneer with dspr
        mi "And more modestly!"
        "She got up and beckoned me after her."
        mi "Let's go watch movies?"
        me "What about the radio?"
        mi "What radio in the rain? Let's go watch movies, because I don't know how to turn it on without you."
        me "How pragmatic."
    play ambience ambience_7dl["rain"] fadein 2
    scene cg d5_rainy_idle_7dl with dissolve
    play music music_7dl["lastlight_piano"]
    "We laughed in tune and, holding hands like two first-graders, set off toward a new, rainy, damp, overcast-but-warm day."
    "A day where there was room for everything I had lost faith in so many, many years ago."
    "Hope."
    "Participation, caring."
    "And love."
    "Miku."
    "I looked at her sideways, at the way her wet hair was clinging to her face, and through the strands of it, her eyes {i}glittering with happiness{/i}."
    "And the thought that the cause of this indomitable happiness was me made me want to do something to the world in return."
    "To blink away the unintentional rubbing in my eyes and subjugate the will to cause and effect, distributing to everyone not according to merit or accomplishment - but according to the happiness his soul can contain."
    "And most of all to this girl, who in her very own way, but from her heart, gave me everything she could give me."
    "And that in itself meant far more than could be expressed in any words."
    "As Lena said yesterday - Miku and I are exotics. And we're expectedly drawn to each other."
    "I remembered that morning dream again - with running after her with a million bags, grown-up, beautiful, confident."
    "It was so in tune with the new picture that I didn't notice the transition."
    "I'm sweating backstage, warming a water bottle in my hands to keep my beloved from catching a ligament, holding a plaid towel in my hands just in case, to wipe her hot after dancing on stage."
    "And worried about her - I've already heard what fans can do if they break through the cordon - and proud of her impossibly."
    me "Miku."
    "We ran through the whole camp, but at the very entrance to the clubs, I stopped her and turned her toward me."
    scene bg ext_clubs_rain_7dl
    show mi normal pioneer
    with dissolve
    mi "Let's go under the canopy! My hair is all wet!"
    "She shouted."
    "Not looking particularly upset, though, because her tails had soaked up a couple of pounds of rainwater."
    me "No, wait. I want to do something."
    mi "What?"
    me "We have so much romance, it's as if someone sat down to the point and finger-picked up events line by line - and it gets creepy as to who has the intelligence or the power to pull this off, but..."
    show mi smile pioneer with dspr
    mi "Senechka, speak Russian, I understand Russian too."
    if (alt_day2_date == 'mi'):
        me "So I'm saying, first the beach, sunset."
    me "Yesterday the moon and our first real kiss."
    me "Today it's raining."
    mi "Well, that's beautiful! Gotta catch snippets like that as they come in succession!"
    dreamgirl "What, you really made up your mind?"
    th "Piss off."
    dreamgirl "No, have you thought well?"
    th "Fuck off, I said."
    me "Miku."
    mi "Yes, Senechka, what is it?"
    if loki or herc:
        me "I think I fell in love with you."
        show mi shy pioneer with dspr
        "The girl went into a kind of catatonic stupor for a while, from which she found nothing cleverer than to ask:"
        mi "You think so?"
        me "Actually, no. I'm absolutely certain of it."
        me "As far as being sure of such things at all."
        mi "Uh..."
        "She waved her palm in front of her face."
        mi "W-wow... You know, Senechka, I'll probably have to get used to the idea for a while, okay?"
        me "Yeah, sure..."
        "I nodded dejectedly."
        th "She needs to get used... Well, who would doubt that. You can't even count on mutuality and reciprocity."
    else:
        "I opened my mouth... And froze."
        me "Uhhhh..."
        "I shook."
        show mi upset pioneer with dspr
        mi "Senechka, what's wrong with you? Are you feeling unwell?"
        me "No, I'm fine. Now."
        me "I... uh..."
        "My throat stopped, and after a series of swallowing, I'm back to where I started."
        me "Miku, I... well, it's..."
        mi "What?"
        me "I have something very important to tell you."
        show mi shy pioneer with dspr
        me "Very important?"
        mi "Yes!"
        "I tried it a third time."
        me "I... Well, you know..."
        show mi sad pioneer with dspr
        mi "No, I don't understand. What's wrong, Senya?"
        me "Dammit! I can't say it..."
        mi "Say what?"
        me "What I wanted to say! It's like someone's got me by the throat."
        "I was about to cry."
        mi "Maybe you just got cold feet. It happens. Let's go to the club and see if you can warm up."
        "I found it hard to relate the cold to my constricted throat, but I nodded agreeably."
        mi "Wonderful!"
    mi "In the meantime, let's go see a movie!"
    me "Let's go..."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_dj_cinema:
    $ persistent.sprite_time = "night"
    scene bg int_clubs_dj_7dl
    show mi smile pioneer
    with dissolve
    play music music_7dl["what_am_i_doing_here"] fadein 5
    "It was dry and warm in the deckhouse - dropping our raincoats on the crucifix at the entrance, we left our water-soaked shoes there and walked barefoot into the holy of holies."
    "The radio in the rain is not critical. Or rather, it's even harmful, as it distracts pioneers from running between the cabins, restrooms, and canteen."
    "So the DJ can afford to dawdle."
    "And, accordingly, a close associate - I don't know what to call it, an assistant? An assistant?"
    "Anyway, this time the channel was already set up, all that was left to do was wait for the equipment to warm up, and a few minutes later the brand-new Panasonic was gulping down a VHS present of the sequel to the adventures of Marty McFly and Doc Brown."
    mi "Back to the Future 2. So there's the first one, too?"
    me "There is, but it's about a trip back in time, not very interesting."
    "Movies for me, especially good ones, have always been about on par with a good book."
    "Zemeckis, Darabont, Nolan's work was not only good entertainment, but also a kind of philosophical background, which I didn't get right the first time."
    "And every time I watched these films, I discovered something new about them."
    "This Delorean in particular, which I watched avidly throughout the trilogy last time, led me to think about the ethics of helping oneself from the future."
    "Anyone can say there's no such thing as a time machine-otherwise, at least once in his life he might run into himself, get a message from the twenty-first century, or get hold of the kind of super-covered cheat sheet from Oh LaLa."
    "But I haven't seen any of those yet. Either they're very, very well coded."
    dreamgirl "You're like a living Delorean yourself right now, if I may make that comparison."
    dreamgirl "All the cribs are in your head - so go ahead."
    scene anim prolog_1
    $ set_mode_nvl()
    "Retro-futurism is always funny."
    "You look out the window and realize that Vernov's giant steam locomotives would hardly find a place in a modern world that strives for maximum efficiency."
    "That people will never wear wings, are far more likely to throw jetpacks behind their backs or sit in paragliders."
    "Perhaps the people of the future will also laugh at our notions of what technology will become - and a certain twenty-second-century Semyon will look condescendingly at all our transparent bendable phones, wireless Internet distribution and smart chips instead of passports - something the futurists predicted five years ago and are now in full swing to be implemented everywhere."
    "Similarly, there were a few finds in the film that, even from the perspective of a twenty-first-century inhabitant, looked fresh enough-but more and more were things that you couldn't look at without crying."
    "But first things first."
    nvl clear
    "To begin with, it should be noted that we got a cassette tape that had been re-recorded and re-recorded dozens of times, so I was not at all surprised when the familiar voice of Volodarsky was heard from the speakers of the video player after the intro."
    "Peg nose, distinctive swallowing of endings. Mmmm... A taste of childhood!"
    "And it was all the more amusing to draw parallels between what was happening on the screen and where I almost lived."
    "First of all, that fucked-up, motley fashion that Zemeckis was scared of never happened. {w}No doubt about it, there were parrots walking down the runway, but please, who would wear what a runway jerk wears?"
    "The increased immediacy of the newspapers is the truth here! Pure, natural and unrefined."
    "What's more, I've stood up more than a hundred times myself, registering with my smartphone some curious moment like the northern lights over the city, the cordoning off of the riot police during the visit of some soccer players from other cities, or the hilarious mumbling of the 'Metro' newspaper dispensers on Vosstaniya Square."
    "Either a photo or a video or a tweet-the immediacy of the news feeds was astounding, and if you bought yourself an e-book with the ability to collect news feeds, the news would always be almost a few seconds fresh."
    nvl clear
    "Self-tightening boots were never brought in, but the army had uncovered some technology, and from Scandinavia through the Northern Capital there was a flood of clothes in which you cannot get cold in minus fifty, waterproof, with a membrane that does not let the wearer sweat or get tired."
    "So I have no problem lacing myself up by hand when I get into my Grisports, but I'm absolutely certain that no matter how long I stand at a bus stop, I won't get cold and wet... Which is three times as critical in our fierce township, where moisture most often does not fall from the sky, but is carried in a suspended cloud down the street, climbing under the clothes of those who are under-insulated."
    "It didn't work out with the skateboard, of course - impractical. Oh, of course, if a sudden fan suddenly has a few extra million dead American presidents, the experts could build him some kind of pavilion..."
    "But it's far more cost-effective to suspend magnets under the rails and run the maglevs like the clever folks from Miku's homeland did, putting a whole train on magnetic pads and accelerating it to six hundred kilometers per hour."
    nvl clear
    "But when it comes to advertising, yes, we have succeeded."
    "Mankind generally succeeds in the most useless industries - marketing, advertising technology, other mass media designed to deceive our fellow man."
    "That's why you can't scare the average man with the shark that tried to take a bite out of Marty, he'll snort contemptuously and say, 'Don't they have more polygons?' and go on his way, corrupted by a super-realistic computer simulation from Silicon Valley."
    nvl clear
    scene bg int_clubs_dj_7dl
    show mi smile pioneer
    with dissolve
    $ set_mode_adv()
    mi "What are you thinking about, Senechka?"
    "Miku could hardly tear herself away from the hover chase scene over the pool and looked at me."
    me "Nothing... I'm just admiring the genius of man."
    "I took her palm and brought her thin, sensitive fingers to my lips."
    show mi laugh pioneer with dspr
    mi "You sound like my daddy talking - people want peace and stability, yada yada yada... I think it's boring."
    mi "Everyone should have a dose of chaos in life, you can't live by a plan all the time."
    play music music_list["you_lost_me"] fadein 3
    mi "You, for example, obviously didn't plan to meet me at the camp? Or..."
    "She smiled slyly, hanging the end of the sentence in the air."
    me "Of course not. It was an accident."
    mi "The word is out."
    show mi smile pioneer with dspr
    mi "Randomness. I want more randomness. I don't want peace, a swamp or a quiet haven."
    me "Yes, you want to bounce around the stage."
    mi "And I want you to wait for me backstage."
    me "So that would be some orderliness already, wouldn't it?"
    show mi laugh pioneer with dspr
    mi "Stupid. Life on the stage is one big mess. {w}To put some order into it doesn't make everything else the same."
    mi "You must be living in a very boring, quiet world, since it's not only habitual, but the norm for you."
    me "Eh... Is there a difference?"
    mi "Of course there is!"
    show mi smile pioneer with dspr
    dreamgirl "It's customary for you to have your neighbors drilling something over your head - you argue with them, but it's no use, they keep drilling. Is that the norm?"
    dreamgirl "The norm is to do exercises in the morning and run a couple of kilometers to warm up the body. But it's completely unaccustomed to you."
    mi "The difference is, Senya, that one day we'll be each other's norm, but hardly a habit. Do you understand?"
    "Japanese backed up my inner voice's lunge."
    mi "But if we're going to keep communicating after camp-we're going to have to change something, we're from too different worlds."
    me "Worlds..."
    with fade2  
    mi "Look, I don't really know anything about a nice young man, that's not right, I've got to fix it!"
    me "Do you want me to tell you about myself?"
    show mi grin pioneer with dspr
    mi "Yes!"
    "She clapped her hands in a fit of enthusiasm and turned to me completely."
    me "Yeah..."
    "Slowly I began."
    me "Then the first and most important thing you have to promise me is two things: not to laugh at anything you hear here."
    mi "That's easy, Senechka, I promise, I promise! What's the second thing?"
    me "Not that I insist on unconditional trust, but... Just promise me that you won't run out and call in the men in white coats with haloperidol, okay?"
    show mi shy pioneer with dspr
    mi "Baka... Of course, I promise."
    me "Well..."
    "I took a few deep breaths."
    play music music_list["tried_to_bring_it_back"] fadein 3
    me "You see... The thing is, I'm from the future."
    with fade2
    pause(3)
    play ambience ambience_int_cabin_evening fadein 2
    show mi surprise pioneer with dspr
    pause(3)
    show blinking
    mi "So... Stop. I promised not to laugh, not to call the orderlies, and generally I should trust you..."
    me "Yes."
    mi "But that's ridiculous! What are you, like these?"
    "She waved her hand in the direction of the TV."
    mi "Or like your Alisa Seleznyova? Unbearably advanced science and socialism?"
    me "Something like that. Only we don't have unbearably advanced science or half that junk on the screen."
    "No thunder came out of the sky and struck an unbearably chatty pioneer, so I got bold."
    me "You see, I'm not quite sure I'm from the future of your world."
    me "There are a few things I remember very well."
    show mi normal pioneer with dspr
    mi "Remember?"
    "I nodded."
    mi "But you're not..."
    me "Not from as far back as Seleznyova! Relative to now, it's a couple or three decades in the future."
    me "Hell, if you look hard enough, you could find a naked Senka walking under a table somewhere in Leningrad right now."
    mi "I've read a lot about these things! There's paradoxes, an encounter with oneself, and..."
    me "And that's why I'm here and not in Leningrad. I probably would have remembered if I happened to travel to a pioneer camp somewhere in the south one summer in the late eighties!"
    mi "Okay, we saved the universe from collapse."
    show mi happy pioneer close with dspr
    "Miku pulled the stool closer to me and grabbed my arm."
    mi "Time to talk about the best part!"
    me "About what?"
    mi "Well... How is it? In the future?"
    me "In yours or mine?"
    mi "Do you know about my future, too?"
    "She exhaled enthusiastically."
    mi "Te... No."
    show mi sad pioneer close with dspr
    me "What?"
    mi "You don't have to tell me anything about me. I want to do it myself."
    me "I don't know anything!"
    "I protested."
    dreamgirl "Actually, you know..."
    th "What?"
    dreamgirl "What you've been trying to remember for the second twenty-four hours. I won't say anything, though, or you'll accuse me of spoilers."
    th "I don't understand anything."
    dreamgirl "So much for Random. That's it, you can hang out - the girl's bored."
    me "Okay, let's not talk about you, let's talk about me."
    show mi happy pioneer close with dspr
    mi "Yes!"
    me "So, Semyon's future, from which I escaped to the local paradise, is eternal winter with little breaks for spring and fall. There is no summer; even when it's hot outside, you can't get away from the impression that it's October all around-so aloof do those around you look."
    show mi normal pioneer with dspr
    me "The world has gone smoothly into the corporate age - with speed bumps, cheap high-speed Internet through telecom operators, and porches with lights that turn on by motion detectors."
    mi "Wow, how technological!"
    me "Sort of. {w}We try to instill eternal values in our kids, but they go to an anonymous blackboard after class, where they get mangled by some fat freak with an over-the-top sense of cynicism and self-importance."
    me "He doesn't care who or what you are."
    me "The most important thing for him is just to kill time. {w}And in what sauce, that's secondary."
    me "It's ideal if you're a little bit shaky, but even then you can't avoid the boorishness and the hate."
    me "And if you try to resist..."
    me "Dating and matchmaking services were invented for us, so that we wouldn't cry blood, thinking of our own uselessness."
    me "How can you be unwanted if you have a hundred likes on your picture?"
    "I took a breath."
    show mi sad pioneer with dspr
    me "Incredibly advanced science is more the science of the present day, when the Soviet man has a reason to aspire to the sky."
    me "The science of the future is Asprin's corporations and corporate wars. The chase is not even for a dollar, but for the performance ratio, the look to the sky has been replaced by a look to the output charts."
    me "The problems are growing in a snowball effect - and the more experts we come up with, the greater the difficulties become. {w}For your information-I never heard such words as 'psychoanalyst,' 'stress,' 'cholesterol,' and 'affect' until my twenties."
    me "There are more healers of human souls than healers of bodies, but more and more people are going off the rails, unable to keep up with the pace of the race, forgetting to rest, trying not even to feed themselves - but to stay afloat."
    me "Every 40 seconds, according to WHO statistics, one person goes out the window. Hold your breath - two minutes of not breathing without compromising your health - and in that time there are three fewer unique universes on Earth."
    me "The flight to Mars failed, as did the dream of Selena City, but Google has released virtual reality glasses that can demonstrate a computer simulation indistinguishable from reality."
    me "Every week, on average, one irreplaceable species of flora and fauna dies out on earth, and our children will never, except in pictures, see some beautiful animals."
    me "You can break your head and freeze to death on the street and no one will even scratch it, but your passport now has a chip and holography."
    me "The old morality has become unnecessary and we're back to the primitive communal imposition of the right of the strong, it's okay to meet in a club and get laid or to get knocked up and try to tie an interesting man to yourself."
    me "Having a red bill in the palm outstretched for a handshake when communicating on any level is considered the rule of good manners - and don't care if the RFID-tagged bill is tracked via satellite on a map and you personally blog about it in a few seconds."
    me "Yes, we have stepped forward technologically, but there has been no spiritual renaissance."
    me "On the contrary, we have degenerated to the state of a medieval society-at least as far as attitudes toward one's neighbor are concerned."
    show mi serious pioneer with dspr
    me "I call it the techno-medieval age, and all we lack are high-tech paladins who igni et ferro line up national governments."
    me "Except that's never going to happen either - since spot operations by secretly state-sponsored mercenary squads equipped with the latest military technology are now in vogue."
    me "And anyone who dares to raise his head and raise his voice, will immediately run to call for peace the same 'Blackwater' comrades. And they will call for peace in such a way that no one will be left alive."
    me "And if there aren't enough infantry, they'll launch planes first with land mines - and then with nuclear weapons. Do you remember Hiroshima?"
    show mi cry pioneer close with dspr
    me "The era of torrents, of pirated content, of ideas that lose their authorship a few milliseconds after pressing the 'send' key."
    me "The era of washed out, greased borders between provinces and capitals, the planting of high-class symphonic music and three stories of swearing and slinging mud at each other on anonymous services."
    me "The era of cardboard, plastic and taste enhancers."
    me "And the ability to synthesize absolutely everything from music... To love."
    play music music_list["farewell_to_the_past_full"] fadein 3
    mi "And you live there?"
    "I shrugged it off."
    me "I'm used to it. The way I see it, I've taken the only position where I can remain myself but not slide to the bottom."
    dreamgirl "You sit in a dark, dusty room, communicating only with your monitor-and after that you say you haven't slipped?"
    th "At least I'm still me."
    dreamgirl "And if you have to make a choice? If your politically indifferent bosses decide to suddenly become civic-minded and drive the whole office to... I don't know, at least a picket?"
    dreamgirl "What are you going to do? Duck? Pretend to be sick? Or break down and go along with everyone else?"
    th "You know... I've been going to quit for a long time anyway. And if I have to choose one day - well, I'll go back to outsourcing."
    dreamgirl "And starve to death."
    "Miku pulled back, looking at me with horror."
    show mi scared pioneer with dspr
    mi "But this is some kind of fierce Middle Ages! It's better not to go out without a sword and all that..."
    me "No, guns are still forbidden here, although you can get a permit and buy yourself something with firearms."
    mi "And this is the future I'm living in?"
    "She seems to have completely given up on the idea of 'playing along' with the overly fantasized me."
    me "I didn't say that. First of all, as I said, there is absolutely no certainty that I am from the future of your world, as there are too many inconsistencies - take that same Genda and some architectural features that no GOST of my Soviet Union would miss."
    show mi dontlike pioneer with dspr
    mi "This is still little consolation..."
    me "And secondly, I was describing the future of my country. You, as a half-Japanese, are very likely to live in your mother's historic homeland."
    mi "Why is that?"
    me "Because Japan didn't have shootings in the streets in the nineties. And if the lives of your father and mother mean anything to you, you won't let them go into what historians of the future will describe as the 'original capital accumulation of the nineties' and 'savage capitalism'."
    show mi shocked pioneer with dspr
    mi "Why?"
    me "Because you don't want to get shot one day by jerks with Kalashnikovs in your father's office door, and it doesn't matter if it's your superiors' dishonesty and the OBEP is interested in you or if a new criminal power is just being established - you're just as likely to get shot in both situations."
    me "So while you still can - better go back to Japan, very soon the wicket will slam shut."
    show mi normal pioneer with dspr
    mi "What about you?"
    me "Me?"
    mi "How are you going to survive in this described mess?"
    me "Diplomatic channels, Miku, are not a gateway you can sneak anyone through."
    mi "If I don't get kicked back home, it's going to take me a while to integrate into the local society, get my papers straightened out, and..."
    show mi sad pioneer close with dspr
    mi "And - without me..."
    me "Do you want to stay with me?"
    mi "Yes!"
    me "Miku, well, I already told you... And then, where are you living now?"
    mi "Yeah, nowhere in general, but you can apply anywhere, Pa promised to help."
    me "And if you can't? If they put you somewhere in Moscow?"
    show mi smile pioneer close with dspr
    mi "Silly Senechka... You said yourself that you didn't get a foothold anywhere - so you can start from scratch at any place."
    "She looked at me with such adoration that another breakup argument got stuck in my throat."
    stop music fadeout 6
    play music music_list["just_think"] fadein 3
    me "And you..."
    mi "I'm going to stay close to you, and whatever happens. Besides..."
    show mi happy pioneer close with dspr
    "She winked."
    mi "With my help, it'll be a lot easier for you to become part of society. At any rate, if Pa is allowed to let under the... what's it called... Steel Curtain?"
    me "Iron Curtain."
    mi "Yeah. If a father was allowed to smuggle his foreign daughter behind the Iron Curtain and even put her in one of the camps, then clearly something could be worked out with you."
    "Her arguments were irresistible."
    "Even my split personality agreed with her."
    "To tell you the truth, I didn't really want to argue with her-was I stupid enough to refuse the company of a girl I was head over heels in love with?"
    "The flywheel of memory swung, the inner eye began to form models of the development of events - so far at the level of reverie, without much detail or coherent causation, the tangible chain from leaving to getting tickets in hand to visit her mother more or less began to be traced."
    "If it weren't for one 'but'."
    stop music
    me "What if they bring me back?"
    show mi angry pioneer with dspr
    mi "You had to ruin it! Well, I don't know what then. Let's leave each other's contacts then."
    me "How do you imagine that? You're going to write a phone number on the palm of my hand for me to call in 2018 to unknown people?"
    show mi sad pioneer with dspr
    mi "Trouble... Here! Why don't you write me your contacts you told me about, so I can contact you in the future."
    show mi normal pioneer with dspr
    "I looked for a pencil and a piece of paper with my eyes, and Miku went back to watching the movie, half of which she had safely chatted with me."
    th "Think... Think, head, I'll buy a cartouche. If we are scattered to different parts of the globe, and there is a certain handicap in chronology, what makes sense to leave to the 'girl with channels'?"
    dreamgirl "Anything! Just point out the year when you got what."
    th "Makes sense. So the mailing address... I don't remember my zip code ever changing, but I lived in a different neighborhood until the fifth year. I don't think I can remember."
    dreamgirl "Dubinushka, it's the central district. The last three digits are zeros, the first three are the area code."
    th "Makes sense. So Nevsky Prospect..."
    "Pulling out the tip of my tongue with eagerness, I drew out address after address-where ever I lived, ever lingered."
    "Supported by my subconscious mind, I even managed to remember the village where a horde of my father's relatives lived - the seventh water on the ocean - its address and name, even though I had only been there twice in my very early childhood."
    th "That sounds like a lot of nonsense. After all, I would remember for a fact that some girl came to visit me when I was a kid. And a pretty girl like Miku would remember absolutely!"
    dreamgirl "Keep going, keep going. It's quite possible that we're at the beginning of a time loop right now, and the memories of the meeting will appear from one day to the next."
    th "I highly doubt it."
    dreamgirl "Don't slack off! Write everything."
    "The piece of paper was smoothly hiding under the worst nightmare of any online anonymous person - I was writing the most blatant dirt on myself, the whole underbelly, from and through."
    "Perhaps even when I happened to be involved in state secrets, I didn't write an autobiography about myself in as much detail."
    dreamgirl "Don't screw around, I tell you!"
    th "I'm not screw... Right. The ICQ client first appeared on my computer in late fifth year, seven-digit... Another number, nine-digit... A dozen mailboxes I've ever actively used. Jabbers, conferences, mumbles. Eighth year - Skype."
    th "What else?"
    dreamgirl "If you had ever used any social media or dating services in your life, dickhead... But we don't like it, we turn our noses up at vkontaktic."
    th "Shall I remind you of the proverb or will you shut up?"
    dreamgirl "Shut up. Is that all you wrote, or is there anything else you want to say?"
    th "Yes, I would have pointed out a couple of other forums where I lived in my youth, but there's no more room on the sheet."
    dreamgirl "And that's enough. Above ten times the safety margin, it's all pampering."
    dreamgirl "Give the girl her questionnaire, and let's get ready for lunch."
    th "Already?"
    "I threw a glance at my watch and was forced to agree with the rightness of my inner voice - the hour hand was already close to the '2' mark."
    me "Here. Here."
    "I held out a quadruple folded piece of paper to the girl."
    me "If possible, write it down somewhere, because I know how quickly things that are read often decay. {w}And until then, don't lose it, understand?"
    mi "Of course!"
    "Miku unfolded the paper and ran her eyes diagonally."
    mi "Your handwriting is well readable. What's a skip?"
    me "What?"
    mi "Well, here. S-c-y-p-e. You can't read the last letter."
    me "Oh, it's Skype. Just another means of communication, you'll figure it out later. But we have to go."
    show mi smile pioneer with dspr
    mi "Lunch? I'm hungry too."
    dreamgirl "That's whose alter ego I'd like to be! Didn't ask one stupid question!"
    th "Shush. It's up to you to endure hardship."
    dreamgirl "And keep a record of your foolishness, don't forget."
    play music sfx_7dl["eat_horn"] fadein 1
    "At this time the sound of the horn came from the canteen."
    me "Exactly."
    "To be on the safe side, I took the tape out of the player - warming up the equipment with the tape often caused it to jam - and turned off the TV."
    me "Did we forget anything?"
    stop music
    show mi normal pioneer with dspr
    mi "We didn't take anything with us. Just check the keys."
    "She showed me hers and tucked it back into her breast pocket."
    me "Put the note in there too, please, because if you don't..."
    hide mi with dissolve
    $ persistent.sprite_time = "day"
    $ day_time()
    play sound2 sfx_open_door_2
    scene bg ext_clubs_day
    show mi smile pioneer
    with dissolve
    "I was a little late, unplugging the equipment."
    "Miku was waiting for me on the porch, rubbing her left tail thoughtfully with her fingers."
    me "What were you thinking about?"
    mi "What? Oh. No, nothing."
    mi "Just a train of thought... Look, it's stopped raining."
    me "Yeah. We'll take the raincoats home tonight, let them stay in the clubhouse for now."
    play sound sfx_close_door_clubs_nextroom
    "I closed the door behind me."
    me "I'm ready."
    "And the Japanese girl instantly grabbed my arm."
    mi "Then let's go!"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_dj_dinner:
    scene bg int_dining_hall_people_day
    show mi smile pioneer
    with dissolve
    play ambience ambience_dining_hall_full fadein 5
    play music music_7dl["what_am_i_doing_here"] fadein 5
    "The great gift given to this girl is not a musical or organizational one."
    "But the gift of living."
    "It's hard to put into words all my envy for someone who can smile carefree toward the world and not waste time and nerves on fruitless musings about what would have been if..."
    "I guess I was like her when I was her age."
    "After all, I must have some sort of standard of carelessness - and that's not the sort of thing you can read about in books."
    "Maybe I did read it, though. And I was born a boogeyman, frowning from birth."
    "But Miku saturated my world with sunshine and wind, and it became immediately clear that all walls existed only in my imagination, and in reality I was limited by nothing but my own conscience."
    "Not to think of the future, not to grieve for the past - to live exactly as long as the sound of a breath lives. There to die. And live again."
    "The promised succession of endless 'nows,' the ability to feel which I have squandered on fruitless acquaintances and attempts to conform."
    show mi laugh pioneer with dspr
    mi "Senechka, you're lost in yourself again!"
    "She snapped her fingers in front of my nose."
    me "Huh? What?"
    "I flinched and woke up."
    mi "I say, if you want my cutlet, I'll give it to you!"
    me "Oh, thank you, I'd love to."
    show mi normal pioneer with dspr
    mi "Listen!"
    "She moved closer to me."
    mi "Can tell me a little more about the future?"
    me "Now?"
    mi "Well... Let's eat and then you can tell me, okay?"
    "I only smiled. I wasn't going to deny this immediate being anything."
    me "You ask like you have some very special interest in this matter."
    mi "Actually I do!"
    me "Really? And what, you're not even going to call an ambulance anymore screaming 'take the psychopath away'?"
    show mi sad pioneer with dspr
    mi "No."
    "Seriously answered the girl."
    mi "For a fantasist or a lunatic, you're too unhappy about your future. So we'll try to get something positive out of your stories."
    me "Like what?"
    show mi smile pioneer with dspr
    mi "I want to hear about my homeland."
    "The second little by little gave up, and after tipping my glass of compote into myself, I got up."
    me "Come on, let me try to remember something."
    stop ambience fadeout 2
    play sound sfx_open_door_strong
    pause(1)
    stop music fadeout 5
    scene bg ext_dining_hall_away_day
    show mi normal pioneer with dspr
    with dissolve
    play ambience ambience_camp_center_day fadein 3
    "Immediately on the porch, Miku clutched at my hand."
    mi "Tell me!"
    me "Let's go to the clubs, I'll tell you something on the way."
    return

label alt_day5_mi_dj_jammer:
    scene bg ext_square_day with dissolve
    "To tell you the truth, I didn't know that much about Japan."
    "That is to say, some cultural minimum necessary to understand my favorite anime films, I learned."
    "Some of the vocabulary I heard while watching the subtitled videos has also been deposited in my memory."
    "But it's all at the top of the iceberg."
    "And so, to give a cultural excursion..."
    me "I'm not likely to tell you much."
    show mi smile pioneer with dspr
    mi "It's okay, tell me as much as you can! It's interesting!"
    me "Okay."
    "I exhaled and tried to gather my thoughts."
    me "So Japan of 2018 is still the same mysterious country to the average St. Petersburg gaijin as it is to modern dummies wearing black T-shirts with white characters that say 'hello, I'm a white monkey who doesn't know what's written on my T-shirt.'"
    me "But more and more often on the streets of the Northern Capital you see freaks dressed up in Japanese street fashion - something must be seeping in."
    me "I don't know if it's working for you right now that any Japanese should either make music or paint..."
    mi "Bingo! Don't talk about tradition, talk about novelty instead!"
    me "I'm telling you as much as I know!"
    "I complained."
    me "Okay, what else. Japan is still ahead of the rest of the world when it comes to high-tech gadgets."
    me "So is the stupid mass media."
    me "I don't think there's any point in talking about anime and manga, because they already exist. {w}However, they didn't start to become mass hysteria very long ago, maybe ten years or so."
    me "Besides, these erotic fetishes of yours have reached the point where you can find vending machines for used women's panties in the subway."
    show mi shy pioneer with dspr
    mi "Ugh! More!"
    "I'm thinking about it."
    me "I already told you about the maglev, you should already know about the monthly electronics shows."
    me "I think that's it."
    scene bg ext_clubs_day
    show mi sad pioneer
    with dissolve
    mi "What do you mean, everything? You didn't even tell me anything!"
    me "Sorry, somehow I wasn't interested in the geopolitical situation and other changes in the life of the Land of the Rising Sun."
    "Miku bit her lip and pouted."
    mi "Well, I thought..."
    me "Let's think about it at the club, okay?"
    "Before we knew it, we were at our headquarters."
    mi "Alri…"
    stop ambience fadeout 2
    play sound sfx_open_door_clubs
    pause(1)
    scene bg int_clubs_male_day
    show mi normal pioneer
    with dissolve
    play ambience ambience_clubs_inside_day fadein 3
    "She didn't finish - she groaned, clutching her temples."
    me "Miku!"
    if not alt_day4_mi_dj_sl_repet:
        mi "Again... That..."
    "Only now did I pay attention to the humming that seemed to come from all directions."
    me "Okay, let's go outside and... I don't know."
    "Leaving her standing there wasn't very pretty."
    me "Find me Electronik, please, I think there's interference from some machinery here, I'll have to look for it."
    show mi sad pioneer with dspr
    me "Okay?"
    mi "Deal!"
    hide mi with easeoutright
    "She disappeared from the room."
    "And I, fighting the nausea, generously laced with a dose of panic, walked the perimeter of the room, looked in every corner, and inspected the radio room."
    "Whatever was phoning in here was very close."
    dreamgirl "I don't think the buzzer is out in the open somewhere - otherwise it would have been found long ago. We have to look in hidden rooms, the basement, the attic..."
    th "Makes sense. I doubt there's a basement, though."
    dreamgirl "The stairs are in the radio room, in case you forgot. The hatch to the attic is right above the desk. Go ahead."
    th "Gee, thanks."
    "I set a chair on the desk and climbed up on it and tried pushing the hatch."
    "It didn't work at first - it looked like there was something on the other side."
    "However, after a few vigorous pushes, I managed to swing the hatch open, and..."
    play sound sfx_open_metal_hatch
    play music music_list["you_won_t_let_me_down"] fadein 5
    "It reclined with a rumble somewhere upstairs."
    "And I was finally able to set up the ladder."
    with fade2
    "The humming became unbearable with each step toward the source of the noise, and that in itself served as the best indicator that I was moving in the right direction."
    play sound sfx_open_door_clubs
    el "Semyon? Hi! What are you doing?"
    "Trying not to stumble down the rickety ladder, I took the most stable position."
    me "Electronik? Do you hear humming?"
    el "Well, sort of."
    if alt_day4_mi_dj_sl_repet:
        me "It sounds like infrasound, don't you think?"
    else:
        me "It made Miku very sick yesterday. I suspect... infrasound!"
    el "Infrasound?"
    me "Yes!"
    "With self-surprising anger, I barked."
    th "What an idiotic question! Someone got sick!"
    dreamgirl "Yeah, you should tear up and punch him in the face for not being clairvoyant. H-hero."
    "The subconscious mind clawed."
    th "What? What are you talking about?"
    dreamgirl "What kind of aggression is that? You think it was him turning on the buzzer?"
    th "No, but..."
    dreamgirl "You know what to do."
    me "El... Buddy, I'm sorry. It seems to be working on me, too."
    el "That's okay. I read something, it usually causes nausea, but it can also cause anger outbursts."
    "He thought for a while and then added:"
    el "If I'm not confused, the device must look like a grid or two wide metal sheets braided with a cable around the perimeter. See?"
    "I looked around."
    "Other than a thick layer of dust and two trunks standing just below the skylight, there was nothing here."
    "Except a few thick twisted cables extending from under the window to a supporting beam somewhere."
    me "Now I'll…"
    "Gathering my courage, I took two more steps..."
    scene bg int_attic2_day_7dl with fade
    $ persistent.sprite_time = "night"
    "And climbed up into the attic."
    "It was half-dark, and if it hadn't been for the daylight streaming in through the loose shutters, it would have been completely impossible to get my bearings."
    "Even in total darkness, however, I certainly wouldn't have gotten lost - so clear was the humming sound."
    dreamgirl "You might have bumped your empty head a little against this one - be careful!"
    "I cramped up."
    dreamgirl "Yeah, that's the beam right there. Now if you bother to go around that pole and not smash into it..."
    th "How can you even see everything! We have the same body!"
    dreamgirl "One, but not one. You don't know how to use your own abilities, unlike some."
    th "What have capabilities got to do with it? It's too dark for the human eye!"
    dreamgirl "You're completely right. That's it, there it is."
    "I swooped in the dark and kicked some kind of structure - just as Electronik had said, consisting of some kind of square mesh, some pins, and a thick cable leading to some kind of metal box."
    dreamgirl "No, no, you didn't see anything, and it's too dark for the human eye."
    "The subconscious was yowling all over the place."
    th "And yet I don't understand..."
    dreamgirl "And don't. That box over there, unplug it and take it away, it looks like it's the generator."
    th "Isn't that dangerous? What if it's..."
    dreamgirl "What? Radioactive? Or alive and biting off a few unwanted fingers?"
    th "Come on."
    dreamgirl "No, I'm serious. {w}I can dig into my memory and get you those few articles from 'Technics of Youth' that we once had a chance to read on the subject."
    dreamgirl "But since I can't be trusted, ask Electronik. You trust him more than me, don't you?"
    th "This is no time for jealousy!"
    dreamgirl "Just kidding. Just get the box and carry it downstairs."
    th "And yet... How do you see what I can't see?"
    dreamgirl "Lateral vision, dumbass."
    th "So?"
    dreamgirl "Nothing, nothing. It wasn't you studying in school, it was me."
    "The ill-fated machine seemed to be negatively affecting my raging alter ego as well, so I hurriedly fumbled for the power key and pulled the plug from a solid three-phase 380-volt outlet..."
    dreamgirl "Yay! Yay! You did it, you're my hero, my dependence and support! If you were a little more virtual, you wouldn't have gotten away from a kiss."
    th "Uh... Thank you?"
    "I rubbed my temples - the crushing hum was gone as soon as I turned off the generator, the depressed mood mixed with the desire to kill someone just like that dissolved into the shadows."
    "All that was left was the desire to hand the generator over to the cyberneticist as soon as possible and close the incident as not worth attention."
    "Out of sight, out of mind."
    "Wasting no more time on idle talk, I wrapped the box with cable and shouted:"
    me "Electronik!"
    el "Yes, Semyon!"
    me "Take the precious cargo!"
    el "Yes, now."
    "There was a creak, and a curly head loomed in a column of light from below."
    el "What's the precious cargo?"
    me "Here. Careful, it's heavy."
    "I handed him the generator and watched with curiosity as he tried to simultaneously balance on the ladder, descend, and hold the machinery in his hand."
    dreamgirl "Do you think Miku will appreciate that it's your fault he's crashing down?"
    th "There's infusoria slipper, and then there's nerd slipper. The simplest, the unit of measurement of nerdiness!"
    "I snorted and took the box away from the boy."
    me "You come downstairs, I'll pass it to you later, or you'll really break your head here."
    "The cybernetic agreed"
    $ persistent.sprite_time = "day"
    scene bg int_clubs_male_day
    show el normal pioneer
    with dissolve
    extend ", and a few minutes later we were sitting downstairs, gutting the machine."
    el "Uh-huh."
    "Electronik extracted some gizmo from the depths and held it in his hands like the greatest trophy of all."
    el "Just as I suspected - it's for rodents so they don't mess up the wiring."
    el "So you can set the trigger time here - by default it was set for nighttime, from 11 to 6 in the morning."
    me "So that's when we're not here."
    el "Yes! But the thunderstorm interrupted the power supply, the program went off."
    show el smile pioneer with dspr
    el "But that's alright! I've got a programmer lying around after my last attempt to make a robot. I hope Shurik won't mind if I take one punch card for personal use."
    me "Would he mind?"
    el "I don't know. Especially since he's in the hospital anyway."
    me "Really? And what happened to him?"
    el "Long story."
    "The cyberneticist brushed it off."
    el "Let me restore the program now, and we'll put the tech back in place - we really don't need rats here."
    with fade
    play sound sfx_open_door_clubs
    show el smile pioneer at right
    show mi normal pioneer at left
    with dspr
    mi "Senya?"
    "Miku peeked through the ajar door."
    mi "May I?"
    me "You may! Come here, we've dealt with what's been messing with the air in here."
    mi "And it's not going to..."
    "She gingerly pointed her finger at the box."
    me "No, don't be afraid, we turned it all off."
    mi "Alright."
    "She sat down next to me."
    show mi smile pioneer with dspr
    mi "Well..."
    "She exhaled."
    mi "Tell me! What happened here? Ominous radiation? A cursed place? Mental radiation?"
    me "The last one is closest to the truth."
    me "In a nutshell, there was an emitter set up for pests."
    mi "But I'm not a pest! Or..."
    show mi dontlike pioneer with dspr
    "Miku looked at me suspiciously."
    mi "What are you implying? Or am I the pest?!"
    "I instantly turned on my rear end and, barely able to contain my laughter, put my palms out in front of me in a universal gesture of peace:"
    me "I'm not implying anything! It really was set up to fight small rodents, but it was supposed to be on strictly at night."
    me "In short, neither you, nor I, nor Electronik should have encountered it. Strictly speaking, according to all GOSTs, such things are forbidden in children's institutions..."
    if alt_day3_technoquest1 >= 1:
        el "By the way, it probably also affected Alisa."
        dreamgirl "Yeah. Maybe when she said she didn't know what came over her - she wasn't really lying?"
        th "Do you think it was a temper tantrum?"
        dreamgirl "Sort of. Plus the thing you said about her mommy in there without thinking. {w}It's probably a sore subject."
        th "Yeah... I'll have to apologize in turn."
        dreamgirl "What's gotten into you? You didn't want to apologize to Electronik, but to the redhead..."
    th "Okay, that's all for later."
    me "And then this thing broke down."
    mi "From rodents?"
    me "Yes. It works at night so rats don't chew the wiring or get into the reagents."
    "Miku wrinkled her nose and, after thinking about it for a while, gave off the kind of thing that a stand-in would sit there:"
    mi "But then why such a powerful one that covers the whole house? Wouldn't it make more sense to protect some important area, and the rats would run away from fear themselves?"
    "I looked questioningly at Electronik."
    show el sad pioneer at right with dspr
    el "Actually, the power is really excessive; a signal three times weaker would have sufficed."
    "He nodded."
    me "That's weird. Okay, mark it in memory."
    me "Miku, what are the plans?"
    show mi upset pioneer with dspr
    mi "I wanted to watch a movie and then cuss about being irradiated, but now that it's resolved well... I don't know."
    me "How about a circle time then? You'll be distracted, I'll listen."
    show mi happy pioneer with dspr
    mi "Deal!"
    me "Electronik, can you handle this?"
    "The cybernetic mumbled something indistinctly and waved his hand in blessing, almost knocking over a can along the way."
    "Taking the hint, we both hurried away."
    stop music fadeout 5
    play sound sfx_open_door_kick fadein 2
    scene bg ext_clubs_day with dissolve
    play music music_list["i_want_to_play"] fadein 3
    "On the street, a Japanese girl immediately grabbed my hand and dragged me along."
    me "I'm embarrassed to ask, where are we going?"
    "I gasped, barely keeping up with the girl."
    mi "Let's go!"
    "It seems the whole five minutes of doing nothing made her feel like a real slacker, so she was struggling to make up for lost time."
    me "What would happen if we ran in there not right away, but after a few minutes?"
    "After being in the epicenter of the radiation for an extended period of time, my head was still a little bobbly, and the sudden movements were perceptibly unpleasant."
    return

label alt_day5_mi_dj_vocadrama:
    scene bg ext_musclub_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    "But it seemed that the Japanese girl's revelations last night were not completely sentimental nonsense. She took a dozen more steps, and then, frowning, she turned to me."
    show mi sad pioneer with dspr
    mi "Senechka, what happened?"
    me "What?"
    mi "There's something wrong with you, you walk differently, you breathe differently. What's wrong?"
    me "Besides the fact that I turned off the noisemaker?"
    mi "Oh... And you still..."
    me "Yeah. Side effects."
    mi "Maybe you should see a doctor then?"
    me "The doctor..."
    "I got a chill on the back thinking about what kind of treatment our kindest nurse could give me."
    me "You know... I feel better already! Yes!"
    show mi shy pioneer with dspr
    mi "Are you sure? Maybe you got better for a while - remission happened, and then out of nowhere..."
    me "Miku..."
    "I tried to put all my charm into the smile."
    me "It'll be easier for me if we just don't run. Okay?"
    show mi upset pioneer with dspr
    mi "But how did you..."
    "She frowned."
    mi "Actually, come on! You're probably right, you just don't need to fidget over nothing until everything inside is in place."
    me "Good girl!"
    "Not worrying about possible witnesses, I pulled the Japanese girl closer and kissed her on the forehead."
    "The neighboring bushes chuckled softly, and I arrogantly pointed my tongue in that direction."
    me "Come on. Will you play me something?"
    mi "Sure!"
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg int_musclub_day
    show mi normal pioneer at center
    with blind_r
    play music music_list["so_good_to_be_careless"] fadein 5
    play ambience ambience_music_club_day fadein 3
    "We decided not to stay outside this time-the midday heat was still quite palpable, and I, as a cripple, was strongly contraindicated against being in the sun for long."
    "That's what Miku said, if anything. Not me!"
    "Anyway, I turned the reclining 'theater' seat - on a common carrier, no nonsense like hinges, hello from my childhood practically! - and, seated in the middle, demanded:"
    me "Sake and Kabuki!"
    show mi laugh pioneer with dspr
    mi "I don't think you'd drink sake."
    "Miku smiled with all of her teeth."
    me "And on what basis do you draw such a wrong conclusion?"
    mi "I've got Pa - remember? He's from here, and when Ma can't hear him, he's always badmouthing our liquor, saying that only insane people can warm vodka."
    me "And how does he fight that? Does he order the traditional cup to be served chilled?"
    show mi smile pioneer with dspr
    mi "Worse!"
    "Forgetting that she was going to play, Miku turned the seat next to me and settled down, twisting her leg under her."
    me "Worse?"
    mi "Yes! He made a home-what do you call it? Red corner?"
    me "Red nook?"
    show mi normal pioneer with dspr
    mi "Exactly! Mom had a traditional Japanese house inherited from her grandfather, and she, brought up in the Japanese tradition, valued the inviolability of order above all else."
    me "Really? What about the fact that she married a Gaijin?"
    mi "Well! That's where her problems started."
    mi "Dad didn't like absolutely everything - from the furnishings in the house to the house itself - he'd lived his whole life in Stalin's house at the Kirov factory."
    "Miku was quiet for a while, and then she couldn't stand it:"
    mi "Stalin's house, right?"
    me "Not exactly. They just built houses like that in Stalin's time. Stalin's house. {w}But go on."
    mi "There! After he moved in, he lived very much in the dormitory because he was used to it, but little by little he gave in to Ma's entreaties and moved into the family dwelling."
    if (not persistent.mi_dj_true) or (alt_day2_mi_date != 3):
        me "Frankly, I find it hard to believe that a big boss would live in a dormitory. It's probably only a dormitory by your standards..."
        show mi happy pioneer with dspr
        $renpy.notify('«Clopovnik» - Bedbug house')
        mi "Actually, it's an official hotel house, but Pa used to call it a «dormitory» and a «Clopovnik»."
        me "He seems to be very... modest in his standards."
        show mi laugh pioneer with dspr
        mi "You don't say! But we got distracted."
    "The restless girl fidgeted a little longer, unable to get comfortable, and then she turned to me, and continued:"
    mi "Pa was modest alright… He dissed our “paper cabins”, even when he kept spending more and more times in hotels anyway, since he had to travel a lot."
    mi "And then he was offered the post of - how do you say it in Russian... Brigadier? No... A sort of site manager, to put it simply."
    me "Was that when he went into politics?"
    show mi normal pioneer with dspr
    mi "No! It happened later - but that promotion affected Pa, and he had to move in with us, because it wasn't proper for an entire superior to live in some hotels, especially when a whole house in the country."
    mi "He agonized for a few years, and then he spat on tradition and, yelling at his mother, asserted his right to a 'nostalgia spot,' or 'red nook.'"
    mi "As I remember now, he laughed all the time when I called his diocese that expression. Why, by the way?"
    me "How can I tell you. A red corner in our tradition is a place where icons, images, and other religious symbols stand. A holy place, to put it simply."
    mi "Ho... ly?"
    show mi laugh pioneer with dspr
    "Miku burst out laughing."
    mi "Well, Pa! What a guy! He really had all his most sacred things packed in there, starting with the table and stools that had come from nowhere - he refused to sit on the tatami."
    mi "On the wall, framed under glass, hung his various medals, diplomas and certificates - turned out there were a lot of things he could do as a child!"
    mi "Here."
    show mi normal pioneer with dspr
    mi "And in the most honorable corner stood an old, old refrigerator, still called like a car... VAZ? ZIL? ZIL, yes! ZIL Moscow! I was still surprised when for the first time I saw a truck with the same name in the street - I didn't want to believe it for a long time."
    mi "And so, in this sybaritic nook, at a table on stools, we would occasionally drink a bottle or two smuggled as 'hello from the motherland'."
    mi "And so he just let the traditional drink pass his mouth-with a known vow to make up for it later. Am I saying that right?"
    me "You speak in the past tense..."
    show mi serious pioneer with dspr
    mi "Yeah... About five years ago he was offered a place. Oh, I told you before - anyway, he's hard to reach now, and we hardly ever see each other."
    "She was sad for a second, but it was obvious that this girl doesn't know how to be sad for long - she's not the type to be dejected."
    mi "But now I have you!"
    "And then, as if continuing the conversation, she asked:"
    mi "Is there anything else you can tell me about your contemporary Japan?"
    me "There's nothing more to tell... Your country, apart from technology, hasn't done much - at least not in my memory."
    mi "So tell me about them!"
    me "I told you before... You have everything 'just like people, only better,' as far as television is concerned, for example, and as far as the Internet is concerned."
    me "For example, there's a world-famous service that allows you to watch videos. No, here too, the Asians have twisted and created their own analog, and there are hardly fewer people who go there."
    me "Social networks are a kind of hybrid between a diary, a mood dial, and a messenger. The Asians have made their own, with whistle-blowing faux pas."
    show mi laugh pioneer with dspr
    mi "What, right with the... whistles?"
    me "There's hardly any difference. It's just that someone wanted HIS - and now it's spread to about 45 percent of the world's population - all focused in a fairly compact sector."
    me "Television, radio - well, that's clear. Only the most promoted things or viral videos trickle down to us, and from us to you, respectively, the same pies."
    $renpy.notify('t.A.T.u. Russian: Тату,  (listen) were a Russian music duo.')
    me "Here, for example, were in the early 00s, two chorus girls who took themselves a funny name - now for some reason I can not remember. It was either 'Toi ta' or 'Etu ta'. {w}They didn't stand out in any way, but they decided to show their lesbian tendencies on stage."
    show mi shocked pioneer with dspr
    mi "A girl with a girl?!"
    me "Yes!"
    me "Kissing on stage... Dancing in their underpants - in short, a whole anecdote. But the point is, they turned out to be just the right sustainable enough product to infiltrate the Asian market."
    me "Their 'they won't get us' was shouted out of almost every iron in Tokyo, mass hysteria, cosplay, rotations, covers... Wow, there was so much there!"
    mi "So popular?"
    show mi sad pioneer with dspr
    "Jealously asked Miku."
    me "Don't pout."
    "It took a little straining to bend down and reach her temple with my lips - but it was worth it."
    show mi smile pioneer with dspr
    mi "Don't abuse it. I might get used to it."
    me "That's okay. I'll try. Well, shall I go on?"
    dreamgirl "Old Mazai got loose in the barn..."
    me "Asians have responded with all sorts of anime cartoons, comic book/manga adaptations."
    me "The nineties served as a kind of preparatory period for cultures to start blending - Japanese techniques, Japanese diets, the rice table, comfort zone theory, performance theory with a mandatory sleep hour, feng shui..."
    show mi grin pioneer with dspr
    mi "See! And you said you didn't know anything. Tell me more!"
    me "What else..."
    "I scratched the back of my head."
    me "I think that's it. Then there's pure science for science's sake: 3-D printing, for example, 3-D input systems, reading brain signals and eyeball movements, virtual reality simulation systems of all kinds of detail."
    me "The most expensive computer technology, industrial holography."
    mi "What? How is that?"
    me "It's, for example, they have such a thing as a vocaloid..."
    stop music fadeout 0
    "I stuttered halfway through. And stared at Miku in horror."
    show mi serious pioneer with dspr
    mi "Senechka?"
    play music music_7dl["please_stop_it_mastered"] fadein 3
    "Miku stared at me incomprehensibly."
    mi "Why are you pale? Do you feel bad again? Should I really take you to a doctor?"
    me "And the name, of that vocaloid..."
    scene
    $ renpy.show("bg int_musclub_day", what = Desat("bg int_musclub_day"))
    show mi serious pioneer
    with dissolve
    "The words left my throat with great difficulty - but I remembered! I remembered - and, like a boil that rots - until it all drains away, the flow of filth cannot be stopped."
    me "Hatsune Miku."
    show mi normal pioneer with dspr
    mi "That guy is my namesake!"
    "The Japanese girl clapped her hands, but somehow uncertainly."
    me "Girl."
    mi "What?"
    me "She's a girl, too. That vocaloid."
    "I told her everything."
    "About her not even existing."
    "A girl named Hatsune Miku."
    show mi scared pioneer with dissolve
    "About the time someone recorded different 'nyas' and made music out of them."
    "And just lips trembling to the point of mortification and a heart that looked like it was getting ready to stop as soon as I shut up."
    "I kept talking. Thinking."
    "It probably wouldn't have been so bad yet - come to think of it, a virtual girl."
    "What was much worse was that a confluxed memory of her came up."
    $ persistent.sprite_time = "prolog"
    if herc:
        $ renpy.show("bg int_store_7dl", what = D3_intro("bg int_store_7dl"))
    elif loki:
        $ renpy.show("bg ext_winter_night_rotate_7dl", what = D3_intro("bg ext_winter_night_rotate_7dl"))
    else:
        $ renpy.show("bg intro_xx", what = D3_intro("bg intro_xx"))
    with dissolve
    "The price I had to pay for a few days in a communist paradise, where anime characters stand as bronze statues in the square and a made-up Japanese girl cries while listening to my revelations."
    show mi shocked pioneer far with dspr
    play sound sfx_chair_fall
    with vpunch
    "I jumped up, green circles swirling in front of my eyes from inappropriate dystonia, and residual weakness from the radiation."
    "It didn't matter now. {w}It creeped me out."
    "Because it could very well be that I haven't paid my price yet."
    "And I'm still paying it."
    "A half-wild chuckle jumped to my lips all by itself."
    dreamgirl "You remembered after all."
    "The inner voice sighed."
    scene
    $ renpy.show("bg int_musclub_day", what = Desat1("bg int_musclub_day"))
    show mi scared pioneer
    with dissolve
    mi "Senechka, what's wrong with you?"
    me "Stay back..."
    "I slowly retreated to the door."
    mi "Senechka?!"
    me "Don't you dare..."
    "I felt moisture on my upper lip and stared at the spreading black-pomegranate drop with my palm."
    show mi scared pioneer far with dissolve
    me "Approach..."
    "Facing away, I took another step toward the door."
    mi "Senya..."
    dreamgirl "You're hysterical!" with hpunch
    th "Liar. {w}It's not hysteria, it's time to find a console and format your whole world in half!"
    play sound sfx_open_door_kick
    pause(1)
    scene bg ext_musclub_day at fast_running
    with dissolve
    "I couldn't remember how terrified I was, but I had to get out of the clubhouse and run as fast as I could into the sweltering heat."
    "The remnants of my conscience told me that I had now done something very wrong."
    "But now I was driven forward by a feeling that was useless to fight against."
    "And I laughed all the time, the fool, when people talked about panic, about panic attacks."
    "And now I'm the same 'around the corner scared' guy."
    "The mind has been driven to the farthest corner of consciousness, all that's left is the fading 'I' and the concrete that's beating at my heels."
    "It's scary to die. It's scary to live, knowing that you're really... No, not thinking about it."
    th "Does that mean I'm probably lying on an ambulance gurney right now and they're trying to pump me out?"
    dreamgirl "Perhaps."
    if herc or loki:
        extend " By the way, my existence - my will and the fact that I speak a language you understand - can also be explained by that."
    th "But I don't want to be inside some other reality. It's like I'm in a computer game, right?"
    dreamgirl "Perhaps."
    dreamgirl "Or maybe this is the real reality, and you had a boring dream before."
    scene bg ext_square_day at fast_running
    with dissolve
    if not loki:
        th "There's a logic to it. I've never broken a limb, even though everyone I know has, at least once... I haven't even been injured much."
    "Thoughts jumped from fifth to tenth, arguing with myself was difficult, but fear drove me forward."
    scene bg ext_boathouse_day at fast_running
    with dissolve
    stop music fadeout 6
    $ persistent.sprite_time = "day"
    scene bg ext_boathouse_day
    with dissolve
    play ambience ambience_boat_station_day fadein 3
    "My feet led me to the only place where I could find relative peace of mind."
    th "But I was left with scars from childhood vaccinations. And when I tested my wrist with a razor blade, I was left with a few healed cuts, too."
    if loki:
        "Unlike the old ones, the heirs of bitter memory, these were barely noticeable, vanishingly pale."
    play music music_7dl["unfulfilled"] fadein 3
    "I put my hand to my eyes and made sure again."
    th "Not such a dream then?"
    dreamgirl "Perhaps."
    th "Aren't you sick of it?! That's the third time you've said that word!"
    "I flared up, and the inner voice sounded somehow guilty:"
    dreamgirl "I'm sorry, but I have as much information to think about as you do. It's perfectly clear that you're not in the past."
    dreamgirl "It's quite clear that there are people from different time periods gathered here - for example, Slavya is clearly from either an extremely distant future or, on the contrary, pre-Baptist Russia - with her utterly utilitarian attitude and inability to be embarrassed."
    dreamgirl "Miku is your contemporary, if I may say so."
    th "She's not real..."
    "I spat angrily into the water."
    th "And I also kissed her!"
    dreamgirl "Retard!" with hpunch
    "I could almost physically feel the slap coming."
    dreamgirl "Life teaches you nothing."
    th "What's the matter?!"
    dreamgirl "Do you remember what her lips taste like? And the smells? Tactile sensations?"
    th "So what?"
    dreamgirl "So all that is your present."
    th "The real of a dying mind... I wonder what happened to me that threw me here."
    dreamgirl "Maybe it wasn't you who was thrown in, it was just... Have you read The Corwin Chronicles, do you remember the principle of parallel spaces coexisting?"
    th "How about 'Amber,' after all?"
    dreamgirl "That, too. But not the point. So remember the parallels?"
    th "Something about the difference in one small detail?"
    dreamgirl "Exactly. And right now, there just seems to be a lot of those 'small details' around. Personally, I'm betting that this reality is synthetic. Sort of a vinaigrette."
    th "And how is that supposed to help me with Miku?"
    dreamgirl "Well... you might wish you hadn't woken up. Remember what's waiting for you on the other side, and give it up."
    dreamgirl "Stop fighting, you know?"
    dreamgirl "LET IT GO!" with vpunch
    with fade2
    me "But... I'm going to die."
    dreamgirl "Too bad! Come on, remember that Munchausen guy! While your body is exhaling its last spirit - four days have passed here, you've met, befriended, and managed to fall in love with each other."
    dreamgirl "It's scary to even think how long it would take for the heart to stop and the brain to die - fifty local years? Seventy?"
    th "But I don't want to live seventy years in some computer game."
    dreamgirl "And I don't want to live in your head. What's next? Do you have sensible alternatives?"
    dreamgirl "I remind you that on the other side of reality you can be a shattered stump, you can exhale by catching a bullet with your skull, or you can just freeze slowly, beaten in some winter park."
    dreamgirl "Keep that in mind - except that you're being very dishonest toward Miku."
    th "Moral standards cannot be applied to a vocaloid."
    dreamgirl "Do you need a kick in the head again to get your brain working?"
    th "What's wrong again?"
    dreamgirl "What do you want to bet she's sitting in a club crying bitterly? Because her young man pushed her away. {w}Is that a vocaloid?"
    dreamgirl "She's in pain, Semyon. She's scared and very sad, because she has no one closer than you. {w}Is she a vocaloid too?"
    th "She could have been programmed to do that."
    "I kept arguing, not knowing why myself."
    dreamgirl "Was she programmed to love too? Or the way she treated your back yesterday? To talk about her father? To react to the buzzer, perhaps?"
    dreamgirl "A vocaloid is a synthesizer. An electric piano in which the place of the D-flat is occupied by various 'nyas'. Does she look like a piano? Or like the hero of some stupid computer program out there?"
    th "I don't know..."
    dreamgirl "No, I'm serious. Let's see, how can you unmistakably tell if it's a program, some kind of computer dummy or some kind of homunculus, or if it's a living being with self-consciousness?"
    th "Well... I guess it's the illogical behavior. Then again, I'm alive, I think, I feel."
    dreamgirl "I wouldn't call Miku particularly logical. {w}She's alive, too, and judging by the fact that she fell in love with you like a cat, she feels it, too. However, based on the second thesis, she probably can't think."
    th "I would ask!"
    dreamgirl "Are you done? Or any other criteria?"
    th "I don't know."
    dreamgirl "Okay, then let's put the question another way. You yourself - what do you think? Is she alive? Or is she that damn synthesizer?"
    th "I don't know."
    dreamgirl "That's it. And you accuse me of repeating the same thing all the time."
    me "But I really don't know!!!" with vpunch
    "I yelled into the red-hot sky."
    "Consider her alive - at the risk of running into lines of code if I make a mistake. But my conscience will be clear - I have not been a coward, I have not escaped."
    "Or consider her a robot and a sham and think for the rest of your life that you screwed up somewhere and quite possibly slashed a living person."
    "Moral issues."
    "And my morality was that I was in love, after all."
    dreamgirl "So it's time to grow up and take responsibility for your actions?"
    th "What if..."
    "For some reason, my head was filled with phantasmagoric images of fragile beauties in MMO worlds, controlled by a kind of collective bearded, smoky image."
    dreamgirl "Now I'm going to change sides and ask you another question."
    dreamgirl "What if there's a risk? If there really is a beard, a smoky sweater, and chewing attention half and half mixed with beer?"
    th "So you just have to be able to go insane sometimes."
    "Not listening to any more subconscious cues, I set my skis to the music club."
    play sound sfx_7dl["eat_horn"] fadein 1
    "But the horn decided that all apologies must be postponed."
    "However..."
    stop music
    play ambience ambience_camp_center_day
    scene bg ext_musclub_day with dissolve
    play sound2 sfx_campus_door_rattle
    "It was expectedly locked."
    th "Well, let's go intercept her in the canteen."
    "With a sigh, I got up and staggered toward the canteen."
    scene bg ext_dining_hall_away_day
    with fade
    scene bg ext_dining_hall_near_day
    show un normal pioneer
    with dissolve
    "On the porch stood an obviously expectant Lena."
    me "Lena, hi!"
    show un shy pioneer with dspr
    un "Hi."
    me "Say, have you seen your roommate? Because she and I just... missed each other a little bit."
    "Despite our yeterday's conversation being very productive, there's absolutely no reason for an outsider to know what's going on just between me and Miku."
    un "And you... I thought you were together."
    me "I told you, we've parted ways."
    "Patiently I explained."
    un "She wasn't here. Absolutely not."
    me "I see. Are you expecting someone?"
    show un surprise pioneer with dspr
    un "What? No, I..."
    "She blushed so desperately that I knew it was not only unreasonable, but simply cruel, to get an answer out of her in that state."
    me "No? Then I'll go to the canteen, and if you see Miku, please tell her I was looking for her. Okay?"
    "Lena nodded hastily, and I left her alone."
    stop ambience fadeout 3
    scene bg int_dining_hall_people_day
    with dissolve
    play ambience ambience_dining_hall_full fadein 3
    "The canteen was humming like a beehive - the half-asleep pioneers, hungry in less than three hours, were hastily restoring their blood sugar."
    me "Olga Dmitrievna!"
    show mt normal pioneer with dspr
    mt "Yes, Semyon?"
    me "Have you seen our radio host?"
    mt "Isn't she with you?"
    th "I see. A dead giveaway: the limit of a squad leader's competence is not knowing where her pioneers are."
    me "She's not with me. I'll go ask the others."
    show mt shocked pioneer with dspr
    mt "Do you know something? Did something happen to her?"
    me "No! It's just that about an hour ago I left the music club and Miku stayed there. Now she's not there. And she didn't come here."
    mt "Shouldn't we make an announcement on the speakerphone?"
    th "Right! 'Camp radio deejay, come to the radio room right away,' laugh and sin."
    me "I guess it's a little early to resort to such radical search methods, but I'll keep that in mind, thank you."
    show mt normal pioneer with dspr
    mt "Shall I send Slavya to help you in your search?"
    me "Doesn't she have enough to do besides search for runaway pioneers?"
    "Not that I personally have anything against the activist, but her presence has always made me a little nervous-a sort of guilt complex when a fragile woman is dancing around the apartment with a broom and a vacuum cleaner, and you limit yourself to lifting your legs so as not to disturb her cleanup."
    mt "She's got things to do, if that's what you're asking. {w}But I'll let her know just in case, and let her think whether she can or not."
    th "And why only ask, I wonder. Still did it her way."
    dreamgirl "How so? Don't we have a democracy in this country?"
    "After the spat with Miku, there were some notes in the alter ego's voice... strange! Either too harsh or too hysterical."
    th "What do we do now?"
    dreamgirl "Shall we turn on the gentleman? Let's take an afternoon snack on the lady, and when we meet her, starving, we'll show up all like this, on a white horse, with a tasty bun."
    th "Reasonable."
    "After grabbing a double portion at the distribution, I didn't linger any longer and went outside."
    "Miku's search time has begun!"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_dj_music_club1:
    scene bg ext_musclub_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    "Miku wasn't here before lunch - I checked."
    play sound sfx_campus_door_rattle
    "She wasn't there now, either."
    "But just in case, I walked around the perimeter of the building, looked in every window - what if she was hiding under the piano? - and I knocked with all my heart."
    "No dice."
    us "Have you lost your fiancée?"
    "A sly voice came from behind."
    show us smile pioneer with dspr
    me "Greetings, talking bush."
    show us laugh2 pioneer with dspr
    us "How did you know?"
    me "You're the only one with such a snide laugh!"
    show us shy pioneer with dspr
    us "Damn…"
    show us shy2 pioneer with dspr
    us "I thought I hid badly."
    me "You said something about Miku..."
    "That reminds me."
    us "Yes... She was here before lunch, then she left."
    "Reluctantly mumbled Ulyana."
    me "I know that without you!"
    show us calml pioneer with dspr
    us "Don't yell at me."
    "She pouted."
    us "Or I won't say anything else at all."
    me "I'm sorry. So what is it?"
    "Ulyana looked at me in disbelief for a few more seconds, but then nodded."
    show us normal pioneer with dspr
    us "I saw her going to the gate. Try looking there."
    if 'entrance' in list_mi_search_7dl:
        me "Already checked. She's not there."
        un "So it wasn't meant to be."
        "She waved at me and ran off toward the square."
        "And I was left wondering where to go next."
    else:
        me "Are you sure? Well. Then thank you very much."
        us "You're welcome!"
        "She elusively snatched a bun from my pocket and, bursting with laughter, ran away."
        th "That was my afternoon snack..."
        dreamgirl "Yeah. So don't get caught by her a second time now - I won't forgive you for losing Miku's afternoon snack, too."
        th "Shut up already... you gloomy bore."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_dj_clubs1:
    scene bg ext_clubs_day with dissolve
    play ambience ambience_camp_center_day fadein 5
    "Logically, this is where the search should have started, for the restless Japanese girl's main place of work was now right here in the radio room."
    "True, there was still silence on the airwaves, so one could conclude that there was still no one at the console."
    "Nevertheless"
    play sound sfx_close_door_clubs_nextroom
    scene bg int_clubs_male_day
    with dissolve
    extend " I decided to check everywhere."
    show el normal pioneer with dspr
    "In the main room - as if he hadn't moved at all - Electronik was still sitting there."
    "He was hunched over a gutted generator, poking at something with a needle."
    me "How's it going?"
    "Without answering, the cybernetic jerked his shoulder - don't interfere."
    "So I hastened to leave him alone."
    play sound sfx_campus_door_rattle fadein 5
    "The door was locked."
    "Still, no possible place should have been missed."
    play sound sfx_unlock_medpunkt_door
    scene bg int_clubs_dj_7dl with dissolve
    pause(2)
    th "Empty!"
    play sound sfx_close_door_clubs_nextroom
    scene bg int_clubs_male_day with dissolve
    "After diligently locking the door, I walked back into the clubhouse."
    th "I guess I'll have to look elsewhere!"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_dj_camp_entrance1:
    scene bg ext_camp_entrance_day with dissolve
    play ambience ambience_camp_entrance_day fadein 3
    "The gate greeted me with silence and loneliness."
    "An abandoned guard booth, a barrier never mounted on a concrete post - they had installed a solid gate instead..."
    "Notches of brick wall in the shape of a five-pointed star, ivy braiding the brick..."
    "And on the other side were the same familiar pioneer figures, either of concrete or some other stone, generously whitened by the sun."
    "A stop for the 410 bus, which I never saw."
    "The 'Beware of Children!' sign - as if someone who isn't aware of the local contingent would turn into this pocket."
    "Of course Miku wasn't here."
    "Yes, and what would she be doing outside the camp grounds?"
    "I thoughtfully dug a crack in the asphalt with the sole of my sandal, which curved intricately from the gate all the way to the bus stop sign."
    "There was absolutely no idea where to go."
    "Those places that I thought were the Japanese girl's diocese, she would avoid in the first place - just because I was aware of them."
    th "Where to go then?"
    "I stood precisely in front of the ajar gate and watched with my side-eye as the outline of the girl's figure floated and distorted in the flowing, heated air rising from the asphalt."
    "Behind her, the world seemed to cut off into nothingness, passing into poorly rendered backdrops."
    th "I knew it - they save on processing power, they don't keep the whole camp in memory."
    dreamgirl "Still hysterical about virtual reality?"
    th "I have a right!"
    dreamgirl "Come on. Good virtuality makes you build it yourself. Remember? 'The depths, the depths, to hell with the depths!'?"
    dreamgirl "So you don't have to try, even if you stick your nose in something, it's not going to go in squares-leses."
    th "And what's that supposed to mean?"
    dreamgirl "Nothing."
    "An image of a serene shrug."
    dreamgirl "Just pointing out that your way of grading realities is not without flaws."
    th "Uh-huh. So her existence isn't a hack job to please an inveterate erotomaniac?"
    dreamgirl "Pfft. Don't say that out loud to her, okay? I'm afraid she won't appreciate it."
    "A few more seconds and Slavya stopped in front of me."
    show sl normal pioneer with dspr
    sl "Semyon, what are you doing here?"
    me "Walking."
    "I answered neutrally. I didn't want to expose another person to my problems."
    show sl serious pioneer with dspr
    "Slavya frowned a little, choosing her words."
    sl "Say, Semyon, did you sign the entry instructions?"
    me "Pardon me, where?"
    sl "Well, in the regulations."
    me "Nope."
    if not alt_day2_mt_help:
        extend " I haven't held a pen at all since I got here."
    sl "Well, that explains a lot."
    show sl smile pioneer with dspr
    sl "Semyon, the point is that camp rules forbid pioneers to be outside the grounds in the absence of a senior attendant."
    "She scribbled it out in a memorable way."
    me "Yeah. Why is that?"
    show sl smile2 pioneer with dspr
    sl "Who knows?"
    "Slavya laughed."
    sl "Just another stupid rule that's useless to try to understand."
    me "Well, now I have a senior attendant."
    show sl laugh pioneer with dspr
    sl "You're sly!"
    show sl normal pioneer with dspr
    sl "And yet, what are you doing here?"
    me "I can't say. Let's just take as a theory that I'm walking around here."
    sl "Oh, is that so..."
    me "And you?"
    sl "What?"
    me "What are you doing here?"
    sl "Nothing much."
    show sl smile pioneer with dspr
    sl "Are you going to... ahem... walk much longer?"
    me "No. I'm on my way back."
    sl "Good."
    show sl smile pioneer far with dissolve
    "Slavya nodded at me and hurried back to camp."
    sl "By the way..."
    hide sl with dissolve
    "That's when Slavya completely disappeared behind the gate."
    sl "I saw Miku outside her house fifteen minutes ago. Hurry up and walk there if you want to catch her."
    "The wind carried her laughter."
    if 'home' in list_mi_search_7dl:
        me "But I..."
        me "Was... There..."
        "I can't tell if she really wants to help, or if she's just subtly mocking me."
        "Oh, whatever. Let's keep looking."
    else:
        th "Yep."
        dreamgirl "Mm-hmm."
        "In tune with me summed up the subconscious."
        dreamgirl "Every dog in this camp seems to know - what happened between you and Miku."
        dreamgirl "One word - big village!"
        th "No argument."
        th "But I agree with Slavya, we should really check out Miku's cabin - maybe she's still there."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_dj_un_mi_house1:
    scene bg ext_house_of_un_day with dissolve
    play ambience ambience_camp_center_evening fadein 1
    if len(list_mi_search_7dl) > 1:
        "My legs were already starting to get tangibly humming as I ran up to the cabin that Lena and Miku shared."
    if len(list_mi_search_7dl) > 3:
        "My last hope was to catch Miku in her cabin."
        "Because all the other places she might have been, I'd already looked."
    scene bg ext_un_house_with_un_7dl with dspr
    "Lena sat on the steps, squinting lazily in the sun."
    "A beautiful satin bookmarked tome awaited its moment beside her."
    un "Semyon..."
    "She did not blush or embarrass herself at my appearance, which was rather surprising."
    "However, she might have been simply lazy."
    $renpy.notify('«Lena» sounds almost like "Lazy" in russian.')
    dreamgirl "She was a very lazy girl.{w} That's what everyone called her Leeeeeena."
    me "Miku?"
    "Lena shook her head negatively."
    un "Still haven't found her?"
    "I just shook my hands."
    un "And the squad leader?"
    me "I want to do it myself. I lost her myself, I'll find her myself."
    un "Well, then..."
    "The girl yawned sweetly, covering herself with her palm."
    un "Good luck in your search."
    "And she closed her eyes, letting me know the audience was over."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_dj_estrade1:
    scene bg ext_stage_normal_day with dissolve
    play ambience ambience_day_countryside_ambience fadein 5
    "On stage, Alisa was forging something on the strings, and I couldn't help but listen."
    play music music_7dl["dv_guitar"] fadein 7
    "A vaguely familiar tune I once heard-maybe on one of my camping trips at another campground."
    "There are plenty of references and memory clues to this camp in general - but I've probably said that more than once."
    "It's all on one living thread; pull one thing, another will follow."
    "Pull the thought of what I associate with a mean redheaded girl with a guitar - and it turns out that somewhere in the past there was already one who I hated with all my heart, but something inside broke when she disappeared."
    "Pull the thought of Slavya - and you're bound to come across one of those inexplicably caring women that everyone sometimes meets along the way. And then you think that since you've been lucky enough to find such a good man, maybe you're not such a loser."
    "Ulyana is a dream or a false memory of a mischievous, mischievous little sister who will never let you get bored, who will drive you crazy, but will selflessly love and honor you until she has children of her own... And not sure she will stop after she becomes a mother."
    "Lena is such a stereotype, it's even funny. {w}A shy girl who needs to be cared for and wooed and be sensitive and gentle and patient before she'll let you get close enough to her. In three hundred years the tastes of chivalry have never changed."
    "Though modern chivalry increasingly favors tweed, less often denim armor with inserts of worldly cynicism and ostentatious callousness."
    "And Miku."
    "The doctors here are at a loss for a diagnosis."
    "And so, while our denim Galahads and Lancelots disperse to different corners of the ristalion, whipping their hundred-megabit horses and testing the strength of their mace arguments, you can put the world on pause and think - what does Miku really mean to me?"
    "I guess Miku is my unrealized desire to smile at least once a day so I don't go crazy. Or better yet, to laugh."
    "Buried alive forever a seventeen-year-old, through whose eyes I look at the world through the thickness of my life - even if it suddenly turns out that many years and the most bitter experiences separate me from the point of self-identification."
    "No, not a longing for childhood, no. This is exactly how I see myself, how I should be. It's no wonder that once I got here, I became what I always thought I was."
    "And it was logical to expect that of all the possible choices, I would choose the person who would be closest to me in that desire."
    "After all, in my world, Miku is eleven years old as a sixteen-year-old."
    "Miku... My hope."
    dreamgirl "So it wasn't enough to call her a program, now she's also a puppet of your subconscious?"
    th "Well..."
    dreamgirl "I recuse myself! I have nothing to do with her! They would have taken me to the nuthouse after two days of trying to get along with her. Do you remember how she talks out loud? Imagine what goes on inside her head!"
    th "So it's not a subconscious glitch or a program..."
    dreamgirl "That doesn't mean anything. You need to talk to her."
    with fade2
    stop music fadeout 4
    pause(3)
    "Finally Alisa reached a logical point in the piece and stopped playing."
    show dv normal pioneer with dspr
    dv "Why are you here?"
    me "No reason... I've been looking all over for Miku, have you seen her?"
    dv "No. Anything else?"
    me "No."
    "Nodding, Alisa instantly lost interest in me and went back to stringing."
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_dj_supper:
    scene bg ext_dining_hall_near_sunset with dissolve
    play music music_list["trapped_in_dreams"] fadein 3
    "The rush through the camp was not fruitful - the Japanese girl had vanished into thin air."
    "So I walked to the canteen, tormented by the most unpleasant premonitions."
    "After lingering on the porch for a few more seconds, looking around in vain, I was forced to go in - the suffering pioneers knew no doubts and literally carried me inside."
    scene bg int_dining_hall_people_sunset_7dl
    with dissolve
    play ambience ambience_dining_hall_full
    "The place inside was found with great difficulty."
    show mi serious pioneer with dspr
    "My heart gave a tingle when I saw exactly who was next door."
    dreamgirl "There you have it. Eagle."
    me "Enjoy your meal."
    mi "Thank you."
    "I don't know how she assessed my behavior, but that she had every reason to be offended is a fact."
    "And so I was not surprised by her unexpected lack of words."
    me "What are your plans after dinner?"
    mi "Bonfire."
    me "Bonfire?"
    mi "Yes."
    show un normal pioneer at left with dspr
    un "There will be a hike after dinner. To the campfire glade."
    mi "I helped prepare the camping trip."
    "Notified Miku."
    "She had frozen off at one point, shattering the nurturing image of the sunny bunny girl into shards."
    "Unable to stay angry or resentful for long, uh-huh."
    "She has an overcast look for a sun bunny."
    "And that look stubbornly - anywhere but along, not at me."
    "I wouldn't be surprised if it were tears, silent or violent hysteria, in the extreme trying to do me some nasty thing."
    "But not this..."
    me "Miku..."
    show mi upset pioneer with dspr
    mi "Yes, Semyon."
    me "Not Senechka?"
    mi "What did you want?"
    me "Will you always be... like this now?"
    "She only shrugged her shoulders and, composing her unfinished dinner on a tray, carried it away to the window of the dishwasher."
    hide mi with easeoutright
    mi "I'm not real..."
    "A fragment of thought reached me."
    show un serious pioneer with dspr
    un "Guilty? Fix it."
    me "What? But..."
    show un angry2 pioneer with dspr
    un "Don't you understand something? Catch up with her, now!"
    me "Coming, coming..."
    scene bg ext_dining_hall_near_sunset
    with dissolve
    "I don't even know what startled me more, Lena's new role or whatever she left untold."
    "Either way, one or the other - it added to my leap of faith, and I managed to spot the familiar blue-green tails at the end of the paved walkway leading from the canteen to the square."
    play ambience ambience_camp_center_evening
    scene bg ext_square_sunset
    show mi cry pioneer
    with dissolve
    play music music_7dl["will_you"] fadein 4
    "Her eyes were wet, but they instantly dried up as soon as she saw me."
    me "Miku! Stop right there!"
    "I caught up with her and caught her by the arm."
    me "Miku!"
    show mi sad pioneer with dspr
    mi "What do you want?"
    me "I..."
    "My breath was jumping, not so much from the jogging - it's only good for the body - but from the nerves and the feeling that if I couldn't find the words right now, something would happen... I don't know. Irreparable?"
    me "I want to talk, I guess."
    show mi normal pioneer with dspr
    mi "About what?"
    "There's that look again - somewhere in the distance, past, tangentially."
    me "About us."
    mi "Talk. Only I have to go to the club."
    me "Why?"
    mi "Songs for the fire."
    "For some reason, a phantasmagorical picture flashed through my mind of Miku making a fire with music paper."
    show mi upset pioneer with dspr
    me "And you..."
    mi "Picked up songs, need a guitar."
    me "Let me help you."
    show mi angry pioneer with dspr
    mi "No need. I can do it myself."
    "She stubbornly looked away."
    "And I couldn't blame her at all."
    show blinking
    "But I couldn't just let her go either!"
    "With a shrug, the Japanese girl returned to her course at the north end of the camp, leaving me the choice of running after her or staying put."
    "Of course, I caught up with her and tried to keep up."
    "It used to work - we used to walk together somehow! But not now."
    me "Miku..."
    mi "What?"
    me "Look, I'm sorry, huh? I'm sorry, I'm a fool, but I didn't think it through."
    mi "I'm not mad."
    "She kept talking to me in the same {i}unliving{/i} voice."
    me "I can't when you're like this!"
    "I overtook her and got in the way."
    scene bg ext_musclub_day
    show mi pioneer shade
    with dissolve
    "Miku's headquarters was located at one of the highest points of the camp, so the setting sun was free to reach here."
    "So I looked at Miku, and I saw a black silhouette with no identifying marks."
    "And it creeped me out to think that maybe she was the same inside now - levelled black."
    "And my long tongue was to blame."
    me "Hear that? I want you back."
    show mi normal pioneer with dspr
    mi "I'm here... Will you carry my guitar?"
    me "Yes, of course."
    mi "Then take the one by the wall. They're waiting for us in the square."
    "She let me go ahead of her, and stepped back to the table with the stack of sheet music albums."
    play sound sfx_open_door_2 fadein 4
    scene bg int_musclub_day
    show mi serious pioneer
    with dissolve
    mi "Formation."
    "She anticipated my question."
    me "Been to the bonfire before?"
    mi "Twice."
    me "Will you tell me what's going to happen there?"
    "I didn't leave trying to shake the girl - well, you can't leave her like that! She's been like this for three hours..."
    mi "Two kilometers through the woods, then a campfire, I'll play the guitar, you sing."
    me "That's it?"
    mi "Yes."
    "I wanted... I wanted to do something decisive."
    th "Maybe I should just grab her in an armful and not let her go until she comes to her senses."
    dreamgirl "Go ahead. Then don't be surprised if she tries out some clever kungfu trick on you."
    th "But you can't leave her like that!"
    dreamgirl "It's okay. If she survived a few hours, she'll tolerate a couple more."
    th "And what happens in a couple of hours?"
    dreamgirl "You make me want to swear, by God."
    dreamgirl "It's nighttime. The fire. The woods. Romance!"
    th "So?"
    dreamgirl "So, with that kind of sauce, you can both apologize and suggest that she doesn't take it to heart. You never know."
    me "We'll probably be broken up in pairs. Will you come with me?"
    show mi upset pioneer with dspr
    mi "If it happens."
    "She whispered."
    stop music fadeout 5
    scene bg ext_houses_sunset
    with dissolve
    play ambience ambience_camp_center_evening fadein 3
    "After locking up the club, Miku headed for the square."
    "But as we approached the monument, squad leader called out to us."
    show mt normal pioneer with dspr
    mt "Semyon, Miku, already packed for the fire?"
    mi "Coming to pack."
    "Colorlessly replied the girl, disappearing."
    hide mi with dissolve
    me "Excuse me?"
    mt "I saw your sweater - take it with you just in case, we'll be coming back late, it might be cold."
    me "But I'm with Miku..."
    mt "Don't worry, I'll make sure no one steals it while you're gone."
    me "No! I..."
    show mt smile pioneer with dspr
    mt "March!"
    "Olga Dmitrievna took the guitar away, turned me around, and pushed me in the right direction, the only thing missing was a congratulationary kick."
    dreamgirl "Let's go already, get that poor sweater and hurry to reunite with the awe-inspiring lover."
    th "Humor me."
    scene bg ext_house_of_mt_sunset with dissolve
    "It would be fair to say that I've never been a fan of all that hiking nonsense."
    "All the action games, the ziplines, the running, the crawling around in the mud-I participated in them, even started to have some fun once I warmed up."
    "But there was no all-consuming infatuation with that way of life."
    "Unfortunately, the pioneers did not share my philosophical view of the next natural disaster and ran excitedly, preparing for an 'exciting adventure.'"
    "Foot by foot, I staggered off in search of a sweater, which in this weather was needed like a cow's saddle."
    stop ambience fadeout 2
    scene bg int_house_of_mt_sunset
    with dissolve
    play ambience ambience_int_cabin_evening fadein 2
    th "However, if I am not confused about anything, there may be something..."
    "Inside, I checked the nightstand - Olga Dmitrievna had unloaded the contents of my pockets into the top drawer, and I was once again glad that our leader was completely devoid of curiosity."
    th "I hope we won't be forced to pitch a tent or cook over a campfire. What am I talking about, though. We're having an evening bonfire, so we'll sit and sing and walk back in the dark."
    dreamgirl "Well! You can break a leg in the dark, stand in some molehill, poke your eye out with a branch, get run over by a nocturnal predator! An exciting adventure!"
    "Without wasting too much time, I shoved everything in my pockets, threw my sweater over my shoulders, knotted it under my chin, and with a goodbye glance in the mirror, hurried back to the square."
    stop ambience fadeout 2
    return

label alt_day5_mi_dj_campfire:
    scene bg ext_square_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 3
    play music music_list["lightness"] fadein 3
    "If I wasn't mistaken, no more than half the population gathered here - judging from what I remembered from the two lineups I didn't profile."
    "Our squad was in full force, with the exception of Olga Dmitrievna, walking around incomprehensibly."
    "Shaking off the dust on the curb near Genda, I sat down and stretched out my legs."
    "After catching Miku's gaze, I nodded invitingly, like, 'sit down'."
    "This time, apparently for a change, she didn't turn her nose up at me, but sat down next to me."
    "Her eyes were still full of emptiness, but there were a few emerald sparks in her eyes."
    th "So it's not that hopeless, and she's coming to her senses, little by little."
    dreamgirl "Pray it is. Because we have enough of one autistic person in our tight ranks."
    th "Who are you talking about, I wonder? Is it about Lena?"
    dreamgirl "About you, dear. {w}Lena's not autistic, she's just very modest."
    dreamgirl "But you're clearly on a roll today - doing silly thing after silly thing."
    th "Thank you, I tried!"
    "However, there are some things I could have done that weren't the stupidest."
    show mi normal pioneer with dspr
    "And I covered Miku's palm between us with my palm, smiling in response to her questioning look."
    "She grumbled unhappily, but didn't take her hand away."
    "And soon the squad leader appeared."
    hide mi with dissolve
    show mt normal pioneer far at center
    with dissolve
    "Handing me the guitar, she straightened up and took a deep breath."
    stop music
    stop ambience
    mt "Atteeeeeention!"
    "The commander's growl from his trained throat caused everyone present to shut up, forced those nearby to crouch down, and in between knocked a few leaves off the nearest tree."
    play music music_list["always_ready"] fadein 3
    show mt smile pioneer with dspr
    mt "Perfect! Everyone is assembled, and we can begin our hiking trip!"
    th "Here we go..."
    "The leader folded her arms behind her back and spread her legs shoulder-width apart, dramatically becoming like drill sergeant Hartmann."
    scene cg d2_lineup
    with dissolve
    "In fact, so much so that I was even surprised when she didn't preface her speech with some joke about discrimination."
    mt "Pioneers! Line up!"
    "Everyone in our ranks turned their heads in my direction."
    mt "Smir-rna!"
    mt "So! Today's plan is to have a camping trip to the campfire glade."
    mt "That means we're going to get to the fire glade, rest there, and go back! No overnight stays, no returning before the deadline!"
    mt "If you haven't suddenly gone on your errands - I recommend you do it right now!"
    "The ranks remained immovable - the pioneers were beaten, and there was no desire to feel 'gently empty stomachs' in the midst of the event."
    mt "There will be no foam seats and other nonsense this time, the clearing was cleaned up properly, for which special thanks to the girls of the first squad!"
    mt "There will be one campfire, the fire marshal said not to have more than one at a time, so please take care of the locations now."
    mt "The person in charge of the bonfire is... Feoktistova Slavyana."
    el "Who would have doubted it."
    "Electronik muttered."
    mt "Now a few words about the purpose of the trip. {w}You probably think we have nothing better to do and we're dragging you out in the middle of nowhere to sing along to the guitar and bake some potatoes."
    mt "Well, that's not true!"
    "Olga raised her voice, and the laughter that washed over the crowd washed away like a wave."
    mt "First of all, it's about reinforcing the skills of a camper! The second is learning how to work as a team."
    mt "Speaking of teams... On one, two... count!"
    el "First."
    sl "Second."
    un "First."
    mz "Second."
    "And further down the ranks flew a sine wave of 'first-second-first-second.'"
    "Finally, from somewhere in the lower ranks came:"
    ml "The count is over."
    "The old, effective way to break up a horde of people in pairs."
    mt "Second numbers, step forward!"
    "Exactly half the camp population has stepped forward."
    mt "To the... left!"
    "Electronik was paired up with me in the ranks, but looking at the perturbations within the ranks, I decided to stay close to Miku and started pushing through to her."
    mt "From the second to the seventh squad... march!"
    "And the organized horde headed toward the second gate overlooking the road to the fire glade."
    "Electronik, pleased that I didn't insist on his company, headed toward Zhenya. Slavya, as the main activist, appears to be going alone at all."
    "But Miku will probably go with Lena - and judging by her unfriendly look, coming up to change now is not the smartest idea."
    th "So I'll have to go with Slavya?"
    mt "Semyon!"
    "The squad leader's voice brought me out of my thoughts."
    "I turned around - she had already stepped down from her usual podium and came toward us, all the while showing me that the formalities were over for the day."
    scene bg ext_square_sunset
    show mt normal pioneer at center
    with dissolve
    me "Yes?"
    mt "You're without a pair, aren't you? You don't want to..."
    me "With Miku? I really want to."
    mt "With Miku will go with Lena as her roommate."
    mt "Electronik also doesn't have a pair, but I'll put him with Slavya."
    mt "So you'll go with Zhenya - she's free."
    "A squad leader in her usual style - comes up, asks something, but does it her way anyway."
    th "And why did she even ask!"
    "Her way of doing things stirred up stale irritation in me again."
    th "Buzzkill, huh? I hope I won't be forced to hold hands with that insect?"
    th "We have a mutual idiosyncrasy!"
    "I immediately began to think of options - how to smoothly dump her, for example, to Lena."
    "I don't need any more problems with a jealous Electronik."
    hide mt
    with dissolve
    show mz normal glasses pioneer at center
    with dissolve
    "The rhinoceros beetle froze in the middle of the path, gleaming warily with glassy eyes."
    th "What was Miku saying..."
    me "Zhenya, can I ask you something?"
    show mz bukal glasses pioneer at center
    with dspr
    "The all-encompassing gaze focused on me for a moment. I was condescended to."
    "I don't know how much more training I have to do to look through a man like {b}that{/b}."
    mz "Should you?"
    "Asked the Buzzkill with dejected seriousness."
    me "Yes, I probably should."
    "She sighed."
    mz "Since you're sure... Ask."
    "Her attitude was frankly off-putting."
    "No, I expected her to be at least uncomfortable with my company."
    "But the blatant mockery, frankly, I didn't expect."
    me "Ahem... Zhenya, listen, they say you're friends with Lena."
    if alt_day4_mi_dj_hedg:
        "It suddenly came to mind yesterday, the predator hunt, and the reasons why Miku was alone in the cabin."
    mz "So what?"
    me "Why don't we switch then? You go with Lena and I'll go with Miku."
    show mz smile glasses pioneer with dspr
    mz "I wouldn't mind. But they won't put you two together in life!"
    me "And we'll do it ourselves."
    show mz normal glasses pioneer with dspr
    mz "It won't work. As it is, the camp is whispering that you're dating."
    mz "Do you think Olga needs the extra trouble?"
    me "We're just working together!"
    mz "In short, forget it."
    hide mz
    with dissolve
    th "Bruh. Can't be any shorter…"
    stop music fadeout 3
    "Zhenya stood beside me and assumed a look of exuberant enthusiasm..."
    mt "First squad! To the left in stride... march!"
    "And we strutted along, looking no different from the kids to come out first."
    th "Not only in appearance, but in development, too."
    stop ambience fadeout 2
    scene bg ext_backroad_day_7dl
    with dissolve
    play ambience ambience_forest_evening fadein 3
    "Stomp, stomp, stomp, stomp, stomp! I've got a line in my brain:"
    th "I want to tell you guys a story-a-two!"
    th "I want to tell you about three girls-at-two!"
    th "The girls were all like their mothers-a-two!"
    th "And their mother was known... Okay, stop."
    dreamgirl "Ah, what?"
    th "Bygones. Explain to me, why are we going in pairs?"
    dreamgirl "You were told - mutual help, support, a friendly shoulder!"
    th "So if I fall and break my leg now, our frail librarian will carry me on her back army-style and drag me to the nearest dressing station?"
    dreamgirl "More likely she'll harness Electronik and Slavya to put you in a four-handed lock... Or shoot you on the spot so you don't suffer."
    "The latter was most likely to be believed."
    "Zhenya walked through the woods with the kind of absent-mindedness that unmistakably identifies a city dweller as one-especially the part of them that doesn't take too kindly to nature."
    "As long as we walked the wide, rutted trail, she felt normal, glancing around and warily glaring in my direction."
    "But as soon as we turned onto a narrower path, the trouble started."
    "I'm not much of a torment walker myself, but some things from my childhood are firmly fixed in my memory, like dressing blindly in the woods against ticks, intercepting branches, and tracing the surface of the path so I don't step in the wrong place."
    "Several times I caught branches on the fly away, preventing them from driving over Zhenya's glasses, and caught a dusky look from Electronik as thanks in return."
    "Then I got bored and just got behind me - especially since the boundaries of the trail had narrowed so much that I had to rearrange into a column one at a time."
    "A few palpably scathing blows from the branches, and the town dweller instantly picked himself up and, judging by the strained back, understood perfectly who was the cause of the blows only now coming."
    "I decided, however, to save the care for someone who really needed it."
    th "I wish the squad leader would get tired of being stupid and turn directly to the clearing!"
    dreamgirl "But you haven't pumped up your self-help enough yet! You still have another half hour to save your partner from the branches!"
    th "Right. I'll earn a lot of experience. Tell me, Mutual Aid, what are you thinking of doing with Miku?"
    dreamgirl "The same thing you're supposed to do when you've hurt a girl - ask for forgiveness and then earn it."
    th "Earn it?"
    show mz normal glasses pioneer at center with dissolve
    mz "Why don't you stand forward?"
    me "No."
    "There wasn't an ounce of gratitude in her, and her dislike of the bespectacled girl little by little grew into real irritation."
    show mz bukal glasses pioneer at center with dspr
    "And irritation causes reflexes."
    mz "What about camaraderie?"
    "She asked mockingly."
    me "I've comradeshiped you for the first half of the journey already."
    me "Keep your eyes open and watch the road before you get hit in the face again."
    "The beetle snorted and... Barely managed to dodge the branch Slavya moved away."
    show mz angry glasses pioneer with dspr
    mz "Hey! Can't you be more careful?"
    sl "Excuse me?"
    "Without turning around, Slavya asked."
    show mz angry glasses pioneer far at center with dissolve
    mz "I say, can you not hit me with the branches?"
    sl "So you hold on to them, they grow very close to the road here."
    "Zhenya snorted, but took the advice."
    "Unlike me, she respected her cabin mate for something."
    me "Slavya, when is our schedule for the start of the event?"
    "I didn't whine 'when we're coming' - I knew how much it would put out any more or less experienced hiker."
    me "I'd better get ready."
    sl "In fifteen minutes."
    show mz bukal glasses pioneer at center with dspr
    "The buzzkill hissed something over my shoulder."
    "I didn't hear it, but I didn't ask again."
    "It's probably some sort of obscenity."
    me "Yeah, yeah. In fifteen minutes."
    with fade2
    th "Fifteen minutes."
    "I don't think my sense of mutual assistance will suffer much in the meantime."
    "But I definitely have to think for a while - and I have to do it without anyone interfering."
    "And in order to do that, it is highly desirable to restore the status quo."
    hide mz with dissolve
    "Fumbling for headphones in my pocket, I grasped the ear cushions in my ear canal and, fumbling for a switch, turned on the first tune I could find."
    play music music_7dl["unfinished_life"]
    th "So, Miku."
    scene anim prolog_1
    $ set_mode_nvl()
    "If you think about it, my inner voice is completely right - there was no point in my hysteria."
    "So what if I found myself in some obscure reality where it's not even fifty percent certain that it really exists."
    "Does it matter in the final score? If I can taste, warmth, smells - does it matter if I'm surrounded by virtuality or some uncharted world?"
    "In fact, if my body is now in death and all I have now is a sagging moment before I go into the eternal void..."
    "...if all I have left is limited to this camp and its inhabitants..."
    "...if the meaning of my existence here and now is to finish what I didn't get to do {i}there{/i}, to do what I didn't have either the time or the determination to do..."
    "...as is the case with ghosts, according to lore - some souls are so strongly attached to the earth by unfulfilled obligations, unfulfilled dreams, that they cannot rest finally until they have completed their affairs..."
    nvl clear
    "So what the devil am I turning my nose up at?"
    "This vivid sensation from my youth, this incomprehensible but warm concern for me and for each other."
    "That pinchingly acute affection for a girl with exotic looks."
    "Take it and drink it, eat it with spoons, what's your problem?"
    "But no. We got scared of a girl. That in our world - and the fact that this world is foreign to us is no longer even in doubt - there is a computer girl who looks exactly like her, a vocaloid."
    nvl clear
    "Perhaps right here and now I have been given a chance-and I don't have to ask for what merit! - to finish the unfulfilled tale."
    "To take a breath until my ribs ache - and wake up truly alive, not beating blood against the glass of a fishbowl."
    "To be moved to tears and fall in love to the point of no memory for once in my goddamn adult life."
    "To do something I won't be ashamed of, past or future."
    "I was tinged with belated remorse."
    "And for the fact that the poor girl is now very bitter and cold alone is as good an indication as any of how much she trusts me. That there is one epithet, among other things, that applies to her. {w}{i}Living{/i}."
    "Until the very last word, until the very last second, she gave me no reason to think ill of her. And what did I do in return? I said she didn't exist. And by that, I didn't hurt her so much, but..."
    "I've never understood trust to the point of self-denial."
    "I just wonder how I would react if I were in her shoes."
    nvl clear
    "Miku looks into my eyes and says:"
    mi "You know, Senechka...{w} You don't exist."
    mi "There's this computer game in my world that quite a few people play."
    mi "It's very, very boring, but for some reason it's very popular."
    mi "Imagine a young guy who has no life, no family, no relationships, no interests. All he has is a computer."
    mi "He works in the morning, and in the evening he comes and sits at the computer, chatting with some anonymous people, on weekends he sits there all day long."
    mi "Slouchy, red-eyed, overgrown. Not interested in anything but fruitless exchanges of lines with interlocutors who don't actually exist."
    nvl clear
    mi "And the main character's name is Semyon."
    th "What a nightmare. I would have spent a long, long time trying to escape somewhere, then drown my eyes in alcohol or distract myself somehow."
    th "And it's not like I'd believe it at all."
    dreamgirl "And she believed, opened up to you..."
    dreamgirl "What did you do in return? A blow to the foundations of existence? The first step on the road to madness?"
    dreamgirl "Vocaloid, program, fiction... Draw a clear line between yourself and her! Come on, say it out loud - what it means to be human! List the proofs, the prerogatives, the price of it, at last! Prove that you are human. And after that, tell me why she is not!"
    dreamgirl "Notice, she doesn't even resent you. Her eyes are empty because she doesn't know how to go on. Her self-consciousness, her ego, considers you part of her, herself part of you."
    nvl clear
    dreamgirl "And you pushed her away."
    dreamgirl "She's like those neophytes in philosophy who have just hopped into existentialism and asked themselves the first question that leads to the abyss: 'Who am I?'"
    dreamgirl "And you answered that question in her place - with your customary whipmaker's tact."
    dreamgirl "I quote: you are a fiction, a speck, a cap of foam on the face of a raging ocean."
    dreamgirl "So don't be surprised if the next key question, 'why me?' - she will answer completely on her own."
    dreamgirl "No reason. Just because."
    nvl clear
    th "And what do you suggest?"
    dreamgirl "Push her away, lose her trust. Let her know that your words are nothing but a waste of air. Tell her you have to stop seeing each other."
    th "That's not an option."
    dreamgirl "Either give her irrefutable proof that she exists."
    th "How?!"
    dreamgirl "I don't know. Think."
    dreamgirl "Hurry up and choose."
    dreamgirl "Otherwise there will be one more unlived life in this universe."
    nvl clear
    stop music fadeout 4
    $ set_mode_adv()
    "…"
    scene bg ext_polyana_sunset
    with dissolve
    "Alisa touched my shoulder, and with a nod I wound up and tucked my headphones into my pocket."
    "I think we arrived."
    "It seems my thinking was worth something. At any rate, the time to our destination was shortened considerably."
    "Olga was looking around the clearing like she was here for the first time."
    "Although I could clearly see the rake and broom marks, the logs stacked in a triangle relative to the center of the clearing."
    "And, of course, the cobblestone-lined fire pit."
    show mt normal pioneer at center
    with dissolve
    mt "Squads, disperse! To the campfireman, proceed with the kindling!"
    "The orderly ranks immediately broke and jumbled into the more usual disorganized jumble."
    hide mt
    with dissolve
    "But in spite of the running and the discordant buzz of obviously excited voices discussing the coming evening, there was no problem in getting the pioneers seated."
    "Either they're used to the rules."
    dreamgirl "Or it's what the program says."
    "The subconscious snorted wryly."
    dreamgirl "Get that simulation crap out of your head. If someone has access to this level of technology, it's easier for them to implant a neural interface in your brain and give your nervous system any sequence of signals through it."
    dreamgirl "So no software. Worst case scenario, solid-state images collected from your own memory."
    dreamgirl "In general, get it out of your head. Go talk to a girl."
    play music music_7dl["lastlight_guitar"] fadein 5
    "The pioneers were already seated, and guitar strumming was already coming from different parts of the clearing."
    "And at the center of the fire, Slavya was busy feeding the petals of flame with a finely chiseled matchstick."
    "Next to her, several thick piles of wood were already waiting their turn."
    "It must be a habit and a favorite thing to do here, sitting around the fire like this. And it's nice to smell the smoke on your clothes afterwards, what a memory it is."
    "My camp burned fires of thick logs and lit them beforehand, so that it would have time to get busy."
    "And it burned so hot back then that the plasma reached the tops of the surrounding pines, and the pioneers were seated ten meters away from the fire, otherwise they would have all been cooked."
    "The local gatherings were not as large-scale, but they were much cozier, more at home, as it were. And best of all, I didn't have to wear a thick corduroy to escape the bloodsuckers."
    "It was too hot and dry for mosquitoes, a little early for gnats, and no gadflies at night."
    "Miku, with her head tilted sideways, was turning the picks, adjusting the sound of the strings."
    "Alisa was sitting beside her, arguing about something unheard of from here..."
    "And I stood and watched our camp fire grow and grow strong."
    "At last it was in full blaze."
    scene
    $ renpy.show("bg ext_polyana_sunset", what = Dawn("bg ext_polyana_sunset"))
    with dissolve
    play sound_loop sfx_forest_fireplace fadein 3
    th "Real Pioneers. Not like the Boy Scouts."
    "The moment the scarlet and orange cloth dancing in the wind turns in your direction and looks inside, you realize you've touched something ancient, a primordial essence."
    "It's not for nothing that fire, along with water, is among the primordials."
    "Burning eyes. Burning with passion. A fiery kiss."
    "Man has held a red flower in his hand almost from the moment he first straightened up and stopped leaning on his hands when walking."
    "No wonder the culture and languages of all the peoples of the world pay so much attention to it."
    "And it is certainly not surprising that among other things there was the practice of purification by fire."
    "Of course, the Inquisition of the Middle Ages stomped all over the expression, trying with all its might to trivialize it--feeling no small threat from a living competitor whose mere existence was already perceived as a miracle."
    "But on a subconscious level, everyone knows what happens if you sit by the fire and stare into the fire for a long, long time."
    "And everyone on the same subconscious level does it."
    "At first the small details lose importance-the attention becomes detached and all-encompassing, like the vision of a predator."
    "Then the problems that occupy all time and attention lose power over the mind and fall ashes somewhere in the depths."
    "And finally, after some hour, cleansed by fire, only the flawless ego remains. The same catharsis that adults for some reason confuse with intoxication and therefore drag and drag vodka with them to the fire."
    "From somewhere on the outside the strings cried - Miku opened the concert."
    "Probably both Alisa and Slavya gave her some hints or pointed out the notes, and the clever girl learned it all on her own."
    "But into the sky trembling in the red-hot air were screwed the original Soviet songs of tourist romance."
    "From Vysotsky and Rosenbaum to authors whose names no one will ever know - but whose songs are always on everyone's lips."
    mi "And people walk through the world. Their words are sometimes harsh."
    "Miku glared at me fiercely."
    mi "Please excuse me, they say with a chuckle."
    "She swatted the strings with her palm."
    mi "But the light tenderness of the song caresses dry lips..."
    "The Japanese girl paused, and Alisa couldn't stand it:"
    dv "And the best books they keep in their backpacks."
    mi "It's great to have us all here today."
    me "Uh-huh..."
    mi "The title of the song."
    "The Japanese girl curved her lips vindictively."
    with fade2
    show sl normal pioneer at center
    with dissolve
    sl "I'll sit down, may I?"
    "Slavya, still exuding the heat of the rampant fire, landed next to me."
    me "Oh, yes. Have a seat, please."
    th "Perhaps she could be shoved off the log?"
    th "Or would it be better to get up and go myself? {w}Though where am I going to get away from Miku?"
    th "I still have one unlived thing to do."
    me "Great job with the fire...{w}It's not the first time, is it?"
    "I tried to pretend some semblance of a smile. Luckily, that was enough for the blonde."
    sl "Yes! I got a TRP badge for tour training."
    "She bragged."
    th "Wow! And I have over 65 percent accuracy in CS:GO."
    me "I can't boast about that either."
    show sl smile pioneer with dspr
    sl "I know!"
    me "How?"
    sl "Well, you're an ambassador kid. You've lived in the city all your life."
    "The lie grows and spreads. Little by little, it gets fleshed out, detailed. It's going to come down on me in its entirety, squeeze the hell out of me and replace me completely."
    "And on the other side of the gate in the embassy's 'Chaika' I will be met by a certain speculative father in a black cloth with gold embroidery and two pairs of buttons - golden ones."
    me "Ah... Well, yes."
    sl "So you didn't make up, did you?"
    "Slavya intercepted another look thrown in my direction."
    "It seemed to me that in this case a shrug would be the most eloquent response."
    "After sitting for a while longer, she patted my shoulder affectionately."
    sl "You just don't dare to give up, do you hear? I'm not at liberty to advise, but..."
    sl "Just don't give up."
    "She got up and walked back to Olga Dmitrievna."
    hide sl with dissolve
    with fade2
    show un normal pioneer with dspr
    "Lena has changed in a couple of days."
    "I can't judge absolutely for sure, of course, I don't know her well enough."
    if alt_day_binder != 1:
        "But that shy girl outside the clubhouse had almost nothing in common with this determined girl."
        "Different people."
    else:
        "But that shy and stuttering wonder at Slavya's cabin and this determined girl here are completely different people."
    "Without asking for permission, she came up and flopped down next to me on the log."
    un "Didn't catch up with her?"
    me "Caught up."
    un "Or didn't talk?"
    un "And talked..."
    un "So you didn't pick the right words, did you?"
    "The smile turned out to be forced. {w}I didn't even have to add anything."
    un "I don't know. Maybe I should go up to her myself?"
    me "No!"
    th "One girl with a blank look in her eyes is enough."
    me "I'll do it myself. Let them finish singing, and..."
    show un serious pioneer with dspr
    un "What happens if you can't find the words again?"
    me "Look, what's it to you?"
    "I bursted."
    me "Why are you trying to get into everything! Like Slavya practically."
    "I think I succeeded in hurting her."
    "Lena was embarrassed, she blushed - for a split second she showed me the usual shy girl I remembered from the first day."
    show un shy pioneer with dspr
    un "Alisa is right, you really are a blind jerk..."
    show un serious pioneer with dspr
    pause(4)
    show un cry pioneer with dspr
    "She jumped up from the log, almost tumbling over there as well. I reached out my hand, trying to help her..."
    show un angry pioneer far with dspr
    un "Don't touch me!"
    hide un with dissolve
    "She ran off into the woods somewhere."
    "And I, with a sigh, sat back down to wait for the concert to end."
    with fade2
    show us normal pioneer with dspr
    us "You're on fire today. You made Miku cry, you chased the sullen girl away... What's next? You gonna beat up Olga Dmitrievna?"
    me "Screw you."
    us "Screw me."
    "Ulyana agreed."
    us "By the way, Miku asked Alisa for an unsafe razor for some reason. {w}Why she wanted one, with her Japanese one, I don't know."
    us "You don't know?"
    hide us with pixellate
    dreamgirl "It seems that Miku has already asked herself the question 'why me'. And you'd better now..."
    th "I got it, I got it, I'm not stupid!"
    "I jumped up."
    th "We've got to intercept and dot all the dots right away before she does something stupid."
    dreamgirl "Yeah. The prerogative to do something stupid belongs exclusively to you."
    stop music fadeout 5
    "I tried to go around the squad leader, but she caught me by the shoulder."
    me "What else?!"
    "I barked."
    play music music_list["two_glasses_of_melancholy"] fadein 3
    show mt shocked pioneer with dspr
    mt "Wow! Semyon?"
    me "Yes!"
    th "Come on, you silly leader, say your nonsense faster and let go!"
    mt "Semyon, how are you behaving?!"
    me "Fine. What do you want?"
    show mt angry pioneer with dspr
    mt "I think someone's getting too oblivious!"
    dreamgirl "You know, man, we better play by her rules now - we'll get away with less bloodshed."
    "Sigh, accepting the inevitable - trying to do it as quietly as possible, and..."
    me "I'm sorry, I overreacted! {w}I was wrong, I'll justify it, I'll fix it, I'll prove it!"
    "The squad leader raised an eyebrow incredulously."
    show mt normal pioneer with dspr
    mt "I doubt that very much. But alright. Since you're here, I've got a party assignment for you."
    th "Oh, my God, where can I find salvation from you?"
    me "What errand is it now?"
    "I gritted my teeth."
    mt "A small one."
    "She approached and lowered her voice:"
    mt "Intelligence reports that Ulyana brought a piece of slate with her."
    me "Uh-huh, and?"
    mt "Your job is to keep her from throwing it into the fire."
    "I couldn't believe my ears."
    me "What am I supposed to do, babysit her all night now?"
    mt "Yeah. And grab her by the arms if you have to."
    show mt smile pioneer with dspr
    "The squad leader smiled charmingly at me."
    mt "Is the task clear? Proceed."
    hide mt with dissolve
    "Muttering curses, I proceeded."
    "And already guessing roughly where she might be, I scanned the surrounding bushes."
    "And when the nearest ones giggled, I headed that way."
    stop ambience fadeout 2
    scene cg d5_us_ghost
    with dissolve
    play ambience ambience_forest_night fadein 3
    play sound_loop sfx_forest_fireplace fadein 3
    "Ulyana was already there, laying out her treasures on a pebble: two bolts twisted on one nut, two pieces; a strip of scruffy paper, obviously soaked in ammonium nitrate, one piece."
    "A slingshot of thick twisted wire, one piece."
    "A second slingshot, a little more trivial - made of the most ordinary slingshot and a drugstore gray harness - she held in her hands and, squinting, aimed her sights..."
    th "At the bonfire!"
    me "Don't you dare!"
    "I rushed toward her."
    "Ouching with surprise, the little one let go of the harness, and almost invisible in the twilight, the gray piece of slate spun and flew into the fire."
    th "Ooops."
    "Just enough time for me to think before"
    scene bg ext_polyana_night
    $ persistent.sprite_time = "night"
    $ night_time()
    play sound sfx_muffled_explosion fadein 0
    extend " IT BLEW UP!" with hpunch
    "The pioneers jumped up from their seats, and in some places the girls squealed."
    "Ulyana laughingly threw the slingshot in place and ran away."
    th "What a competent killer growing up."
    "Aloof, I thought."
    play music music_list["drown"] fadein 3
    "My attention was completely drawn to one point."
    "In focus was cradling her hand, blowing on a burn that was visible even from here, Miku."
    "She set her guitar aside and whispered something I couldn't make out until I got closer."
    "Squad leader yelled something from behind."
    "But I wasn't paying attention to the shouting or anything else."
    "I listened to the feverish, heated whispers:"
    show mi cry pioneer far with dspr
    mi "What is this... Pain? I'm in pain. Am I programmed for this too?"
    mi "I feel, I worry. I am in pain, I am afraid."
    me "Miku!"
    mi "And he said I don't exist. I don't exist. Now someone will turn off the computer and I will cease to exist. Because I am a program."
    mi "But I'm in pain."
    show mi cry pioneer with zoomin
    mi "It doesn't happen that way. It's all made up."
    mi "I... I believe him, right? He said. He couldn't lie, he promised me he would never lie."
    mi "So there's no pain either?"
    me "Miku, look at me!"
    show mi cry pioneer close with zoomin
    mi "He is the most honest man. And I'm a made-up girl."
    mi "And there's no pain, and there's no burn. {w}And I'm -{w} not there either."
    "I came close and put my hand on her shoulder."
    me "Miku, calm down, you hear me?"
    me "You're in pain shock, now we have to take you to Viola."
    mi "And she will what? Will the good doctor shake out the straw and make me real?"
    me "Stop it."
    mi "I..."
    "Her voice dropped to a whisper."
    mi "I can't."
    th "HELP!"
    dreamgirl "Nah, bruh, sorry. You're on your own now."
    hide mi with dspr
    with flash_red
    "After scratching my cheek, she ran away, leaving me in a kind of prostration."
    "It wasn't so much pain as surprise."
    "I mean, screaming or anger would have been appropriate here, but - nails?"
    "Logic doesn't seem to have slept in that pretty head."
    "My attention was drawn to a certain oblong object left where she had been sitting."
    "At first glance, it appeared to be an ordinary penknife, flat, with a rounded handle-a boy's dream."
    "The illusion was immediately dispelled as I bent down and picked up the object - it was a folded razor, the kind our fathers and grandfathers used to shave with, right on a leather belt."
    "Untouched by rust, the dull blade - I tried it on my finger - is still sharp... Exactly razor-sharp!"
    dreamgirl "The very razor that belongs to Alisa."
    dreamgirl "We should hide it away so Miku won't find it."
    th "Or give it to the owner."
    stop music fadeout 5
    menu:
        "Return the razor to the owner":
           $ alt_day5_mi_dj_dv_blade = True
           "After thinking for a while, I decided it wasn't right to steal someone else's stuff, so I looked around and found Alisa on the other side of the fire, surrounded by kids from the third or fourth squads."
           me "Ahem... Alisa!"
           show dv normal pioneer with dspr
           "She flinched and looked up."
           me "Look what I found! Yours?"
           dv "Are you stupid or something?"
           "She hissed, glancing around."
           dv "You better open it up and start swinging or something!"
           me "Oh, well, since you don't want it, you should have said so."
           dv "Give it to me."
           me "Oh, yeah? What's in it for me?"
           show us grin pioneer at left with moveinleft
           us "She's going to kiss you! Maturely, with her tongue!"
           hide us with easeoutleft
           "Ulyana muttered, still successfully managing to run away from the squad leader, Electronik, Sanich and a few other pioneers"
           show dv shy pioneer with dspr
           me "What a curious option."
           "I drawled."
           me "But I'm afraid it's not the level of favor to pay so generously for it."
           "I threw up the razor."
           me "Just don't give it to Miku anymore, okay?"
           "Alisa smiled sourly and, hiding the weapon in her breast pocket, nodded."
           hide dv with dissolve
           "After returning her nod, I stepped back to where my sweater lay."
           "Appropriate or not, it had no place here - especially considering what I had planned."
        "Stash it away":
            th "It will come in handy!"
            "I decided, stashing the trophy in my pocket."
            th "I'll use it to fight off wild bears in case of emergency."
            dreamgirl "And from flying waffles. Are you even aware that you've appropriated someone else's stuff?"
            th "Of course. You know the proverb about the big family and beak snapping?"
            th "That's good. Let's go. We've got to catch Miku before she gets too far away."
            "I threw my sweater over my shoulders and was just about to follow the girl..."
    mt "Squads... Line up!"
    show mt normal pioneer with dspr
    th "Shit!"
    "Everything seems to be going wrong today!"
    "I had a fight with a star, I couldn't escape... If they pair me up with the buzzkill again, I'll hang myself from the sheer hilarity of my existence."
    mt "Since it's late, let's try to take a shortcut!"
    "The squad leader shouted loudly."
    mt "I will distribute lanterns to your leaders and the elders in your squads, try to stay behind them. Let's go fast, so nobody lag behind."
    mt "Is that clear?"
    voices "Got it..."
    "At random, the children answered."
    mt "What's that?"
    "Olga interrogated in amazement."
    mt "Are you pioneers or a herd? How are you supposed to answer?"
    voices "That's right!"
    "In a voice the attendees bellowed."
    show mt smile pioneer with dspr
    mt "Now, that's different. Detachments, turn... right! After Boris Alexandrovich to the camp - march!"
    "Sanich, this time at the head of the column, was armed with a kind of lantern of rather unusual construction, subtly reminiscent of the lanterns of rescue workers and policemen of my time."
    "At any rate, the pillar of light it gave off was no worse."
    ba "Keep to the middle of the trail... Pioneers."
    "And disappeared into the bushes."
    "A few seconds later, the others followed him."
    stop sound_loop
    scene bg ext_path2_night with dissolve
    play ambience ambience_forest_night fadein 6
    play music music_list["forest_maiden"] fadein 2
    "The night forest is always beautiful. It can be frightening, sullen, wary-but it always leaves behind an inexplicable fascination that is unique to it - a living mass, an entire ecosystem, unhurriedly {i}living{/i}."
    "And even though you know for a fact that all possible predators have been dispersed here, if not by weapons, then by radiation, you can still get a little bit of the sweet terror of the anticipation of meeting the Night Beast on your back."
    "Plus that air - that air!"
    "It's probably only comparable to the atmosphere of a farewell disco the night before I leave."
    "You inhale - and inside you catch your breath with the feeling of a miracle come true, and memory waves the 'Captured!' flag and the whole year is marked as not lived in vain."
    "And here it's like this every night. No wonder the counselors don't let the kids go out in the woods at night more than once a week."
    "No one wants pioneers drunk with ozone, stupid with incomprehensible happiness - after all, we have a camp here! We're not playing with toys here."
    "I smiled softly in the darkness and inhaled as hard as I could, soaking the night in with every fiber of my being - even if I were brought back behind the monitor, this moment would stay with me forever."
    dreamgirl "CAPTURED!"
    th "Yeah, thanks dear."
    scene bg ext_path_night
    with dissolve
    show sl pioneer shade at center with dspr
    "There was a certain silhouette in step next to me, treading surprisingly silently."
    "Something in me was hurt by this type of gait."
    "I've seen it somewhere before."
    "I almost remembered who it could be, and then the silhouette spoke to me."
    dreamgirl "In a human voice!"
    sl "Semyon, if you need help, you can come to me or Olga Dmitrievna."
    th "Benevolent cyborg."
    th "No, dear, I certainly won't trust you with personal matters."
    th "You're certainly cool. But you sure lack tact."
    dreamgirl "You're one to talk, you horse's ass!"
    me "Slavya, please stop it. You make me feel like you're mocking me."
    show sl serious pioneer with dspr
    sl "I'm not mocking you!"
    me "And yet. Just try to trust me - to solve my personal problems, okay? And if I'm not strong enough, I swear to you I'll come to you first for help."
    "The carrot and stick method."
    "How do you send a compulsive helper so that he not only rolls smoothly to the curb, but sits there, holding his fists up for himself?"
    dreamgirl "Knock him on the kidney at quarter strength and add to his scruff? Or no, first a knee to the groin..."
    th "You're kidding me again."
    dreamgirl "No, I'm bringing you back to sinful ground. Before you go on singing dithyrambs to yourself, I hasten to remind you that somewhere in the night sits a very upset girl."
    dreamgirl "And not only you are to blame for that - you autistic bastard - you failed to make peace with her when the conditions seemed perfect!"
    dreamgirl "What's the matter with you?"
    th "Nothing."
    me "Slavya, I have one - I don't even know - request? A question?"
    sl "Yes, Semyon. What is it?"
    me "There's no way I can make it up with Miku. No, no!"
    "I hurriedly reassured the flinching activist."
    me "I don't need you to make up with us, just let me use you as a girl?"
    show sl shy pioneer with dspr
    sl "Like a girl?"
    "Cautiously, the blonde asked."
    me "Yes. Imagine you and your boyfriend had a falling out."
    show sl laugh pioneer with dspr
    sl "To do that, you first have to imagine that I have a young man."
    me "And you don't?"
    "I cautiously inquired."
    show sl shy pioneer with dspr
    sl "Somehow I still haven't got the right one."
    th "I don't believe it."
    dreamgirl "No, {b}I{/b} don't believe it! With her armor she could have been married seven times, let alone have a boyfriend."
    me "Um... Ahem... Well, thank you for your confidence. {w}But back to my question. So, sequentially, let's imagine that you have someone close to you and you're in some kind of spat with them."
    me "Tell me, is there anything that would help him redeem himself as quickly as possible? Something he could have done or said?"
    "I asked and wondered to myself - because until a couple of days ago there was nothing to not only think about talking about such a subject, but to even imagine the conditions under which such conversations might have taken place."
    th "I'm - asking an extremely attractive girl - how do I make up with another extremely attractive girl."
    dreamgirl "You're successful!"
    "The subconscious pricked."
    show sl shy pioneer with dspr
    sl "I don't even know... I guess I wish he would have made the first move."
    me "I already did."
    sl "Then do more! And more!"
    sl "You should care. And you should try your best to show it!"
    sl "I don't know and I don't want to know why you had a fight, but in any conflict you two are always most important."
    dreamgirl "Hear that? Now she may have said the smartest thing she's ever said in her life. You're not supposed to be doing that yet."
    th "I got it, I got it."
    me "Priority, huh? Thank you very much."
    "Through the trees we saw the lights of the camp, and we picked up our pace."
    stop music fadeout 5
    play ambience ambience_camp_center_night
    scene bg ext_square_night
    with dissolve
    "From the very entrance, the pioneers stretched out toward their own enclosures, quietly and promptly, without too many questions - and here the training of our kindest leader was visible to the naked eye."
    "It was no surprise that only she and I made it to the square proper."
    show mt normal pioneer with dspr
    mt "Semyon, are you going to rinse yourself? Your shirt is new, but it already smells like a fire."
    me "Are you suggesting that I wash my shirt too? No, thanks, but I'll pass."
    show mt smile pioneer with dspr
    mt "Ah, as you wish. One last day left anyway..."
    "She stretched sweetly."
    mt "And then home. And someone else gets a new shift."
    me "What about me?"
    show mt normal pioneer with dspr
    mt "What about you?"
    me "Where do I go next? How?"
    mt "That's the kind of question you're asking. Do you want me to go to college and work for you? No way, honey."
    mt "But I'll write you a good report, all right. Anything else?"
    "I only waved my hand."
    th "Who cares about what, but the louse cares about the bath."
    mt "Go comfort your Cinderella, Romeo."
    "She winked"
    hide mt with dissolve
    extend " and vanished into the night."
    "The advice was obvious, but reasonable, so it would be a good idea to heed it."
    "But it's still worth finding a girl to start with."
    dreamgirl "Olga said something about showers. {w}As a girl who's obsessed with her looks, I don't think she's going to let the fire stink out of her. Will you try to intercept her at the showers?"
    th "True."
    scene bg ext_shower_night_7dl with dissolve
    play ambience ambience_camp_center_night fadein 3
    "As I moved toward the sports section, out of the corner of my eye I caught a glimpse of someone's silhouette."
    "It was, to be honest, very difficult to see."
    show sl pioneer shade at center with dissolve
    "But it seemed to be her!"
    "Though my damn gut was silent, and somehow my heart took the discovery rather calmly."
    "But the recognizable, {i}scenic{/i} bouncing gait was easy to discern."
    "And the long hair... No one in the camp had such conspicuous long hair. Didn't they?"
    "The silhouette reached the showers and disappeared into their background, leaving me wondering where to go next."
    hide sl with fade2
    play sound sfx_open_water_sink
    pause(1)
    play sound_loop sfx_water_sink_stream
    "The showers were a product of Soviet engineering genius, embodying the idea of 'we have nothing to hide from our friends' in an almost literal sense."
    "On one side was a blank wall lined with white ceramic tiles, to which the shower and faucet itself were rigidly attached."
    "On the other, there was no wall at all. There were hook-and-loop doors from the inside, like the ones they hang in country toilets, that don't go all the way to the top or the bottom."
    "The stalls themselves were separated by about ten centimeters of concrete, lined with the same indestructible ceramic."
    "A sealed plafond with a forty-watt, perforated sheet of stainless steel watering can."
    "In short, a masterpiece of architecture."
    "It took me a lot of trouble to get myself to come closer."
    "I stood in the dark, swallowing with nervousness and trying to turn my stomach."
    "My whole body was shaking at the thought of standing under the shower on the other side of the door without any clothes, completely naked..."
    "Who, by the way?"
    "I managed to suppress a nervous shiver for a few seconds, only to discover that Miku wasn't the only one here!"
    "From the sound of the water, there were three stalls occupied."
    "The first, behind the door closest to the supporting wall, was very tightly covered, and there was a bucket with a mop next to it. Someone's purring could be heard from there, but I couldn't tell who the voice belonged to."
    "I turned my gaze to the second stall, two empty stalls away from the first - that one didn't stand out in any particular way, there was nothing next to it, except..."
    "From the looks of it, either it wasn't hung very well, or had just gone damp, but it wasn't closed very well and left a great big shadow - a real find for whoever wanted to peek."
    "The third cabin was separated from the other two by as many as four empty ones - whoever was washing in there really wanted privacy. Maybe she's in there?"
    "After standing there for a few minutes and scratching my head, I decided to pick one of the stalls and find Miku after all!"
    menu:
        "Check the first stall":
            $ alt_day5_mi_dj_voyeur = 3
        "Check the third stall":
            $ alt_day5_mi_dj_voyeur = 2
        "Look around":
            "I walked around pondering in front of the building, after which it hit me!"
            th "Miku's perfume is very fragrant! Now let's try to identify it."
            "I smelled."
            "The first stall didn't smell anything."
            "The second one smelled like the most common tar soap for hair."
            "The last one smelled like cough lozenges or something... Eucalyptus, that's it!"
            menu:
                "Check the first stall":
                    $ alt_day5_mi_dj_voyeur = 3
                "Check the stall which smells like tar":
                    $ alt_day5_mi_dj_voyeur = 2
                "Check the stall which smells like eucalyptus":
                    $ alt_day5_mi_dj_voyeur = 4
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_dj_voyeur_3:
    scene bg ext_shower_night_7dl with dissolve
    $ lp_mi -= 5
    play music music_list["waltz_of_doubts"] fadein 3
    "As I approached the nearest stall, where the sound of water was coming from, I tried to tread softly..."
    "And still I hit the damn bucket!"
    play sound2 sfx_dropped_chair
    "I flinched, distracted, the door opened, and Slavya looked out."
    if persistent.hentai_graphics_7dl:
        show sl2 serious body with dspr
    else:
        show sl2 serious swim with dspr
    "Naked."
    sl "Semyon, what are you doing here?"
    me "N... Nothing."
    "I couldn't take my eyes off her."
    sl "Can you do your 'nothing' somewhere else?"
    "She definitely looked annoyed, but she didn't even think about covering up."
    "And I wanted to take a step towards her and try - what she's like... There..."
    dreamgirl "Okay, no distractions!"
    "And my head rang with a sharp outflow of blood and a little darkness in my eyes."
    "And from that Slavya's forms - and I still had no idea how gorgeous they were! - were even more prominent."
    if persistent.hentai_graphics_7dl:
        show sl2 laugh body with dspr
    else:
        show sl2 laugh swim with dspr
    "The girl laughed, looking at my stupor."
    sl "I guess you're here already?"
    "Biting her lip, she looked at me with unfamiliar, testing eyes."
    sl "You know..."
    sl "Oh, but wait."
    hide sl2
    "She disappeared in a cloud of steam."
    "There was a murmur of water from inside."
    sl "There!"
    play sound sfx_water_emerge
    "And I got splashed with water from head to toe! {w}At least it was still warm."
    sl "That'll help you cool down a bit!"
    play sound sfx_close_door_campus_1
    "She slammed the door behind her, and, laughing, went back to washing."
    "Never had a girl's laughter seemed so threatening and insulting to me."
    "Threatening because now she had dirt on me and an opportunity to manipulate me."
    "And insulting because, well..."
    dreamgirl "Because she didn't let you do anything stupid? Say thanks, you ungrateful pig. And go dry off already."
    "Finding this advice reasonable, I hastened to follow it."
    stop sound_loop fadeout 3
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_dj_voyeur_2:
    scene bg ext_shower_night_7dl with dissolve
    $ lp_mi -= 5
    play music music_list["gentle_predator"] fadein 3
    "I tiptoed over to the loose-fitting door, pressed myself against the wall, and peeked through the crevice."
    th "Well, if it isn't that stall..."
    "It was pretty steamy in here - whoever washed in here didn't spare any hot water."
    "But I finally got a little closer."
    "Or maybe the steam had dissipated, I don't know."
    "And froze. Or rather, I was paralyzed on the spot by the sight that opened up behind the clouds of steam."
    "And the sight was... Posing the water with her high breasts encased in an orange swimsuit, in a Playboy model pose under the shower, eyes closed, splashing Alisa!"
    "Alone, in the dark, and also looking at me at a very sharp angle from the side, peering under the cup of her bust so deep that..."
    "I forgot how to breathe."
    "Alisa flinched and opened her eyes."
    "Instantly, she stumbled into my gaze."
    "She wanted to be angry, but with a graceful arching of her right eyebrow, she changed her mind."
    "Instead, her eyes were filled with slyness - and I liked the latter much less than I would have liked it if she had just been angry!"
    show dv grin swim with dspr
    dv "What, you like me?"
    "I didn't say anything."
    dv "Come on, newbie."
    "She opened the door."
    dv "Or after what you've done here, am I allowed to call you..."
    dv "Seeeeenechka."
    "She mockingly stretched out."
    me "No, I..."
    if alt_day5_mi_dj_dv_blade:
        dv "You've been watching me."
        dv "That'll make your girlfriend happy!"
        "I couldn't breathe in, but I couldn't breathe out, as if someone had knocked me in the solar plexus."
        dv "Relax. I'm joking."
        dv "But you did me a favor today."
        if alt_day3_technoquest1 >= 1:
            dv "Twice."
        dv "That's why I forgive you your screw up."
        dv "Look for your little one in the last stall."
        show dv laugh swim with dspr
        dv "Unless, of course, you've missed her again!"
        hide dv with dissolve
        "With a snort, I got away from the redhead and her scruples."
        "Unfortunately, her words were prophetic - Miku had already washed up and left."
    else:
        dv "What?"
        dv "Do you feel sorry for me, Senechka?"
        "She grabbed my breasts and yanked me sharply toward her."
        "And I, unable to help myself, took a step."
        play sound sfx_draw_water
        "Finding myself under the shower with fully clothed!"
        dv "Don't be such a downer!"
        if alt_day3_technoquest1 >= 1:
            "She never thought to let me go."
            "And I was suddenly struck by a kind of stupor."
            play sound sfx_7dl["kissing_sound"] fadein 4
            "And when Alisa smiled and kissed me soundly, I wasn't the least bit surprised."
            $ alt_day5_mi_dj_dv_kissing = True
        "In fact, I only got over the shock when she laughed and pushed me out of the shower in my soaked clothes."
        hide dv
        show sl pioneer shade
        with dissolve
        sl "I see you're not bored."
        me "Yeah. Having as much fun as I can."
        "I snapped grimly."
        sl "I hope you've thought this through."
        me "I haven't thought it through. And I'm a victim in general."
        dreamgirl "A victim of abortion, yeah."
        if alt_day3_technoquest1 >= 1:
            dreamgirl "Go dry off, innocently soaked and kissed."
        dreamgirl "You seem to have blown your last chances."
        dreamgirl "So all we have to do is dry off."
    stop sound_loop fadeout 3
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_dj_voyeur_4:
    scene bg ext_shower_night_7dl with dissolve
    play music music_7dl["breath_me"] fadein 5
    me "Miku? Are you here?"
    "A quiet sob in reply."
    me "Miku, we need to talk."
    "Zero attention."
    me "Look, will you stop it already, huh? I was wrong, I admit it, but you've got to stop acting like that, too."
    me "After all, it's brutal!"
    "Not a sound came from inside."
    "Three minutes."
    "Five."
    "And when I got worried in earnest and started thinking about breaking into the stall, there was an answer from inside:"
    mi "Hold on, I'll be right there."
    "The voice was palpably nasal - it sounded like someone had been very, very upset for the last half hour."
    "The water murmured for a few more minutes."
    play sound sfx_close_water_sink
    "Finally Miku showed up outside, blotting her wet hair with a towel."
    me "Hello again..."
    show mi serious pioneer with dspr
    mi "You wanted to talk. Talk."
    me "Can we talk somewhere where we're guaranteed to not be overheard?"
    "She shrugged."
    mi "We could do it at my club."
    stop sound_loop fadeout 3
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_dj_late_evening:
    scene bg ext_musclub_night_7dl with dissolve
    if alt_day5_mi_dj_voyeur == 4:
        "Miku didn't look at me the whole way, obviously completely lost in her own thoughts."
        "We made a little detour, dropped off washed clothes and towel in the cabin, and then Miku took the key to the music club and took us here."
        "Second night in a row at the same place in the same company."
        "Yesterday she was singing and laughing and loving."
        "But tonight..."
        "Tonight wasn't half as languid."
    elif alt_day5_mi_dj_voyeur == 2 and alt_day5_mi_dj_dv_blade:
        "I don't know why I bothered to peep at Dvachevskaya, with a beauty like that behind me."
        "I should have just stood back, walked away, pretended I wasn't involved."
        "It's true what they say, someone else's is sweeter."
        "It's a good thing I owed the redhead, so my gaffe shouldn't have any particularly devastating consequences."
        dreamgirl "Although the very fact of your extravagant retardation and the fact that you managed to miss a girl from a place where there's only one exit, and that is past you. {w} Isn't that crushing enough?"
        th "Shut up, pest, I don't have enough trouble."
        th "She should come here - if only to get a little distraction and listen to music. It's a little late to be spinning anything in the den, so..."
        th "Plus yesterday she said she couldn't get anywhere without rehearsing and performing."
        dreamgirl "Wouldn't it have been easier to go straight to her cabin and wait for her there?"
        "And get Lena to witness our relationship again? No way."
        th "We'll wait here - as long as it takes."
        dreamgirl "The boss is the boss. Personally, I'm in no hurry."
        "Fortunately, 'as long as it takes' didn't take half the night as I feared."
        "Not fifteen minutes later, a familiar head framed by two blue-green tails loomed up the road rising from the sleeping quarters."
        "I sat on the bench, lurking, lest she should notice me and run away."
        "So I only allowed myself to move when a step creaked beneath her feet."
        me "Miku... Shall we talk?"
    "The girl looked at me warily and with a certain amount of dislike."
    show mi serious pioneer with dspr
    mi "Speak."
    me "Here?"
    "She sighed heavily."
    scene bg int_musclub_night_nolight_7dl
    with dissolve
    play ambience ambience_music_club_night fadein 3
    show mi normal pioneer at center
    with dissolve
    mi "Come in."
    "I accepted the invitation and slipped through the open door."
    "The conversation wasn't going well, so I thought I'd put on some music."
    me "May I?"
    "I nodded at the record player."
    "Miku only shrugged her shoulders in response."
    menu:
        "Play «Lightness»":
            play music music_list["lightness"]
            "The Japanese girl grimaced a little as the first chords of the tune began to play."
            "But she was silent."
            "So was I."
            "Finally, the song ended."
            mi "Lena was right all round - you really don't care what I breathe, what I listen to, or what I like."
            "In a wooden voice, the Japanese girl concluded."
            me "I do care!"
            mi "Of course you don't. That's why, out of three records, you picked my unloved one."
            mi "Anyway, you have your way. I'm going to bed."
            "She opened the door invitingly, and I had no choice but to accept."
        "Play «Raindrops»":
            $ alt_day5_mi_dj_apology = 1
            play music music_list["raindrops"]
            show mi shy pioneer with dissolve
            "Miku rounded her eyes when I put that record on."
            mi "Oh, how do you know..."
            me "Ha, how... I just care."
            "The thin ice in my eyes cracked."
            mi "And everything about you matters to me."
        "Play «Silhouette in sunset»":
            play music music_list["silhouette_in_sunset"] fadein 3
            "Miku grimaced a little as the first chords of the tune began to play."
            "But she remained silent."
            "I was silent, too."
            "Finally, the song ended."
            mi "Lena was right all round - you really don't care what I breathe, what I listen to, or what I like."
            "In a wooden voice said Miku."
            me "I do care!"
            mi "Of course you don't. That's why out of the three records you picked the one I don't like."
            mi "Anyway, you have your way. I'm going to bed."
            "She opened the door invitingly, and I had no choice but to accept."
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_dj_evening_club1:
    scene bg int_musclub_night_nolight_7dl
    show mi shy pioneer
    with dspr
    "Too bad that thaw didn't last very long."
    show mi upset pioneer with dspr
    "One brief moment, and from the familiar wet abyss I loved, her eyes were once again empty glasses, looking through me."
    mi "You wanted to talk. Talk and let me go to sleep already."
    me "All right. Just listen to me carefully, okay?"
    show mi serious pioneer with dspr
    mi "I always listen to you very carefully."
    if not alt_day5_mi_dj_dv_blade:
        $ lp_mi += 1
        $ alt_day5_mi_dj_apology = 2
        me "Well. Then let's start with the most important thing."
        me "Dropped it, huh?"
        "The dim blade gave a lazy glow that leapt to the ceiling - very visible in the semi-darkened room."
        me "I know why you needed it."
        "With a practiced movement of my finger, I picked up the tail of the blade and demonstrated it to the Japanese girl."
        show mi scared pioneer with dspr
        mi "What... What are you going to do?"
        me "In a nutshell? Nothing."
        "I lowered the blade to the palm of my hand and very slowly ran the cut, uncovering the bleeding flesh."
        "That it hurt, I don't think I need to say. No, it was okay for the first two tenths of a second, but then something inside me squealed from the absorbed pain shock."
        dreamgirl "Stop it, you psychopath!"
        "Miku gasped."
        show mi shocked pioneer with dspr
        "She jumped up to me and knocked the blade out of my hands, it flew away with a sad clang somewhere under the piano."
        show mi angry pioneer with dspr
        mi "What are you doing? Are you sick?!"
        me "What do you think?"
        "There must have been as much emptiness in my eyes as there was in hers a few minutes earlier."
        "I've only been able to feel NOTHING so clearly twice in my life - and both times while standing at the finish line of what the average person usually gets for a lifetime."
        "You can hurt yourself by biting your lip to blood, for example - but that's cheap posturing; you start hurting yourself really badly when you don't care about physics."
        "And that only happens when there's something wrong with your head."
        "The blood will clot in five minutes, the arm will hurt for at least another month."
        me "Do you think the pain was real here?"
        "I didn't have time to make the cut deep enough, so the blood oozed out very reluctantly."
        me "Do you think it hurts right now?"
        mi "Senechka..."
        "I smiled at her, and I guess my smile was more like a grin."
        mi "Okay, sit tight, I've got a first aid kit here, you know, if someone gets their finger cut with a string or cuts themselves on plates."
        mi "Where is it..."
        hide mi with dspr
        "Miku disappeared into the next room and reappeared a few seconds later, clutching to her chest a rubberized box with rounded corners and a huge red cross in a white circle on the end piece."
        show mi serious pioneer with dspr
        mi "This is going to sting, you just have to be patient."
        "She splashed a generous amount of peroxide on the absorbent cotton and stroked it over the wound - my hand instantly pierced with a sharp sting, and the clear liquid foamed sharply, coming into contact with the blood."
        mi "There... See how much dirt you have on your skin there! If you washed your hands cleaner, it would sting less."
        me "It always stings. {w}It's a reaction to blood, not dirt."
        mi "You know best."
        "Miku agreed placidly."
        mi "You're the one who's good at hurting yourself - and others."
        mi "So I say."
        "I shook my palm, on which the Japanese girl was diligently drawing some kind of green pattern."
        me "I have two pains now. One is here."
        "I nodded at my palm."
        me "And the other one is now trying to put a band-aid on my... what on earth are you doing! Why don't you cut it lengthwise, why do I need a mile-long band-aid on a centimeter-long wound?!"
        show mi grin pioneer with dspr
        mi "Do you want to do the treatment yourself? No? Then exhale and calm down."
        "I exhaled and continued:"
        me "Yes, you're right. I haven't exactly been sane for the past few hours, but your unwillingness to understand a few obvious hints..."
        me "This is your way of getting back at me, isn't it? For saying something stupid and untrue?"
        show mi normal pioneer with dspr
        mi "Don't bother your arm for a few days, and tomorrow go to Viola - I don't have bactericidal, and that's the best way to tape up cuts."
        me "Are you listening to me at all?"
        mi "Yes, yes, I'm listening to you."
        me "If you believe me, then why are you mending me now? And if you don't, why are you shutting me out?"
        me "The feeling that you don't need me anymore - and just because of a few words - makes me want to bang my head against the walls!"
        show mi shy pioneer with dspr
        mi "But you…"
        show mi cry pioneer with dspr
        extend " Haven't stopped."
        mi "And the fact that you were walking around like a dead person doesn't count either?"
        mi "I'm sorry. But I've been living for hours in fear that you're right and we're not living in a real world. And so I don't believe in it, and it ceases to exist. Like a dream ceases to exist when you realize you're dreaming."
        mi "And considering what you said about me..."
        me "Stop it. A very smart girl told me that in a couple, it's always the couple themselves that matters most. No matter what anyone says."
        me "The most important thing is that we're back together."
        mi "Together? What about my opinion?"
        th "Mm-hmm. Trouble. I didn't bother to ask her opinion."
        me "Do you... Do you mind?"
        "Almost anticipating a sad answer, I asked."
        with fade2
        show mi smile pioneer with dspr
        mi "Semyon..."
        me "What?"
        mi "Senechka..."
        mi "Well, why are you talking all sorts of nonsense? Would I let you come here if I was against it?"
        "She smiled sadly."
        mi "Though I won't hide it, I really wanted to turn you around from the veranda. {w}You tried reeeeeaaaally hard to hurt me, and you almost succeeded."
        me "I'm sorry."
        "Miku must have wanted to tell me something."
        "And it must have needed to be said, because it was definitely something unprintable."
        "But, with a sigh, she confined herself to just kissing me somewhere on the jaw."
    else:
        show mi sad pioneer with dspr
        mi "You said I didn't exist!"
        "She looked depressed."
        mi "You know, there's a whole bunch of other wording for suggesting a breakup."
        mi "What does that mean, don't exist?"
        menu:
            "I remembered something. Something…":
                $ lp_mi += 1
                me "I probably should have taken some valerian beforehand, but it was like a curtain fell over my memory-so abruptly I remembered."
                me "I don't know what I was more afraid of, the fact that I was imagining things, or the fact that you didn't exist."
                mi "You again..."
                me "No, I'm not! That's not what I mean. It's just... It's just that it was all an appearance on your part, and you're just my mental disorder."
                me "But everything is relative - there's no hair and skin for X-rays, there's no color for hearing - perceptual quirks, you know?"
                me "And if I remember you and know you and feel you - what difference does it make if you or I don't suddenly exist for someone else. Here and now you exist."
                "I caught her palm and squeezed it a little."
                show mi cry pioneer with dspr
                me "Do you feel it?"
                mi "Yes..."
                me "So let's just pretend that we are, since we're not really there. But let's not split up anymore, okay?"
                me "I'm totally sad without you."
                show mi cry_smile pioneer with dspr
                "Miku smiled through her tears."
                mi "Oka..."
                "And lost her breath."
            "I'm sorry, I said something stupid":
                $ alt_day5_mi_dj_apology = 3
                mi "I'm not mad at all and I'm not offended."
                mi "I'm sorry, too, okay?"
                "She smiled shyly."
                mi "I'll go. {w}I've got a headache."
                "She stood at the door with a hint, and I had to clear the room."
                scene bg ext_musclub_night_7dl
                play sound sfx_close_door_campus_1
                with dissolve
                play ambience ambience_camp_center_night fadein 5
                "She closed the door behind us and turned to me."
                show mi normal pioneer with dspr
                mi "Well, good night?"
                me "Uh... Maybe I'll walk you out?"
                mi "No, it's a hundred meters, I won't get lost. You'd better go to sleep."
                me "But..."
                show mi serious pioneer with dspr
                mi "What?"
                me "What about us?"
                mi "Us? I don't know. I need to think about it properly. I'm sorry, but I really don't feel very well."
                mi "Good night."
                hide mi with dissolve
                "She nodded goodbye to me and silently disappeared into the darkness."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_dj_evening_club2:
    scene bg int_musclub_night_nolight_7dl
    show mi smile pioneer
    with dspr
    mi "You know..."
    "She finally got over herself."
    mi "I don't feel like rehearsing or doing anything else."
    mi "And then you've stirred up... I don't know if I'll be able to sleep."
    me "Do you want me to sit next to you?"
    show mi laugh pioneer with dspr
    mi "You won't be able to, Lena will kick you out!"
    "The Japanese girl laughed."
    me "Then... Why don't we go see another movie?"
    show mi smile pioneer with dspr
    mi "And that's an idea. Just not too long, okay? I don't want to disrupt the schedule."
    "I nodded and stood up."
    scene bg ext_musclub_night_7dl with dissolve
    play sound sfx_close_door_campus_1
    play ambience ambience_camp_center_night fadein 5
    "Soon she followed me out, locked the door carefully, checked the lock, and only then turned to me."
    show mi smile pioneer with dspr
    mi "Let's go... Senechka."
    "She seems to like calling me that too much. So who am I to argue with a girl?"
    "If she wants to - then so be it!"
    hide mi with moveoutright
    play music music_7dl["ltyh"] fadein 5
    scene bg ext_clubs_night with slideawayleft
    show mi smile pioneer with dspr
    me "It'll be fun if the squad leader catches us."
    th "Yeah. Two pioneers in an empty room... {w} Probably playing backgammon."
    "I was already on the leader's radar after several of my blatant blunders. {w}Plus I failed her party assignment..."
    "As it wasn't hard to guess, I had absolutely no intention of meeting her now."
    mi "We won't get caught. Boris Alexandrovich called her for something. And this 'something' was clearly so tinkling in his backpack."
    me "And how do you know everything?!"
    show mi laugh pioneer with dspr
    mi "I went for a bath, remember? That's when I met them halfway."
    hide mi with dissolve
    "Even though it was at least twenty minutes before lights out, there was no one on our way - not the younger kids, not the adults... No one."
    "Though all we had to do was go down the hill and around the building."
    "And yet, yet... Strictly speaking, the clubs are on the main traffic artery of the camp, connecting the gate and the square - and no one."
    "I pulled out my smartphone and looked at the time on it."
    th "That's right, 22:45. The time when Jung devotees listen most strongly to the signals of their own subconscious. I don't need to listen, though - there it is, try to shake it out of my head."
    if persistent.mi_dj_good_jap or persistent.mi_dj_good_rf or persistent.mi_dj_true:
        call alt_day5_mi_dj_hentai
    else:
        "And my subconscious was telling me to shut up."
        "So I smiled serenely."
        "And waved to Slavya as she passed us by."
        show sl normal pioneer at fright
        me "Thanks for the advice!"
        sl "Made up?"
        me "As you can see."
        sl "Great, guys. What are you gonna do now?"
        show sl shy pioneer with dspr
        "Slavya was embarrassed, as if a curious thought had occurred to her."
        "It occurred to me too, but after we had an unintentional witness..."
        me "We'll go to sleep."
        "I touched my lips to Miku's cheek and, nodding goodbye, walked toward the cabin."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_dj_hentai:
    scene bg ext_clubs_night with dissolve
    dreamgirl "Ah, go on."
    me "So you say Olga Dmitrievna won't come for us?"
    mi "And even if she does, we won't open the door for her!"
    me "Makes sense. And if it's, I don't know... Lena, for example."
    show mi surprise pioneer with dspr
    mi "What's Lena going to do here? That's enough talk, open up!"
    play sound sfx_unlock_medpunkt_door fadein 0
    "The padlock gave way in seconds - and the door swung open with a soft creak."
    "Miku slipped inside instantly, and I lingered on the porch for a moment, creating the illusion of a locked room - hanging the padlock on one wishbone."
    play sound sfx_close_door_clubs_nextroom
    scene bg int_clubs_dj_nolight_7dl
    show mi normal pioneer with dspr
    with dissolve
    "We could still be seen from the outside if you tried very hard, so we tiptoed across the main cybernetics club room, opened the inner door, and, just locking it from the inside, allowed ourselves to relax."
    with fade2
    "The door was flimsy, it didn't cut off any sound at all, and a good kick would have swung it wide open."
    "To put it simply, the only thing that kept the door open was the reputation of the camp administration and the pioneers' unwillingness to get into trouble."
    "But it was opaque! And you could hide from the whole camp here!"
    me "What movie..."
    "I turned to Miku, and the continuation stuck in my throat."
    me "Are we going to… Wa…"
    "She didn't let me finish."
    "I had already forgotten the beginning of the sentence by about the middle of it - so saturated was the air suddenly with - I don't even know what to call it - anticipation? Passion?"
    "We've already had our first kiss. Actually, strictly speaking, there was a lot more, but..."
    "Then it was night and there was the moon and there was lots and lots of air that dissolved the concentration of smells."
    "Here, however, I found myself completely vulnerable."
    dreamgirl "I weep at the way you make yourself look like a victim of molestation."
    th "..."
    dreamgirl "You can breathe."
    "Courtesy of the subconscious."
    dreamgirl "And after you stop shaking, you can walk the remaining five centimeters. Up to her lips."
    dreamgirl "If that's the way you wanted to watch the movie..."
    show mi serious pioneer with dspr
    "For a few seconds she stood with her eyes closed, as if trying to absorb the sensations of the trivial touch of her lips."
    "But then that wasn't enough for her - and I felt cold fingers on my heated skin."
    "She was the first, she was the only, she was real."
    play music music_7dl["iamsadiamsorry2"] fadein 5
    show mi smile pioneer with dspr
    mi "Senechka, why are you so embarrassed?"
    me "But I'm n-not…"
    mi "You're trembling all over... And your heart is racing."
    "She put her palm on my chest, and that innocent touch made my forehead instantly evaporate."
    "And a sweet wave of anticipation, of foreboding - of wonder - rushed down from my heart. Whatever is going to happen here now..."
    "Our familiar caress, belonging only to me and her, the one by which we would recognize each other even in the dark - for some reason I was almost fetishized by kissing her fingers, drawing spirals on her palms, gathering heat with my breath from her wrists."
    mi "If you don't want to..."
    "My God, is she doing it on purpose?!"
    "I growled, and, picking her up, pulled her against me."
    "And as in that very dance - she knew what was required of her before I could even think about it - she spread her legs and hugged me, almost sat on my thighs, hanging on to me, close, heart to heart."
    if alt_day3_dancing2 in ('mi_2', 'mi_12'):
        "And then - as on the third day, there was a thin layer of cloth, and under the cloth there was no one but Miku."
    "She was babbling something, but I was no longer paying attention to her words or her attempts to guide me."
    "And what went on between us would be called sadism by the uninitiated - we fought and bit and pressed each other so hard that our bones cracked."
    "And clenched our teeth until we gnashed so we wouldn't scream out loud when the shameless lips found a path along the pulse track, down from the ear, down the neck, under the collarbone."
    "And pulled, and pulled to herself, wanting here and now only to dissolve into another, to give herself up without a trace."
    "It was weightless, smelled in a way that was smelled more by my subconscious than by myself, tasted slightly salty."
    mi "Clo...ser..."
    "She exhaled."
    "Thoughts left my head one by one, drifting off somewhere into geostationary orbit, a lavishly oversaturated, enthusiastic Nothingness reigned between my temples."
    "But it's probably for the best.{w} In such cases, the best thing is to let Nature do what's right and not engage in high-spirited tantrums."
    "For a certain moment it was as if I had been turned into a hundred-armed creature, capable of feeling the gentle maiden's skin subdue under a demanding caress. I was everywhere, and I was absorbing her, absorbing her to the last drop."
    scene black with fade
    "The glare from the street was reflected in her eyes, half-covered, covered by a film of oil... Pink cheeks, labored breathing-she was mine. And I am all hers."
    mi "I may not exist."
    mi "But I want to feel you. Come to me."
    "How long has it been since I've done this kind of thing? If memory is to be believed, a few years. If you believe my body and a major shiver, never. Zero experience, and acting like a bear, I guess."
    mi "Come on, where are you... A little... A little higher."
    "Her whisper bounces and her nails crash painfully into my shoulders..."
    "I, not knowing what I'm saying anymore, exhale rapturously:"
    me "I, what..."
    "The air was rapidly becoming red-hot, moist, smelling of her."
    mi "Oh... Shut up."
    mi "Help me..."
    "With a strain she uttered."
    mi "Just a little more..."
    mi "...A little more..."
    "There was an obstacle in the way, and no matter how hard I tried, I couldn't..."
    "Luckily, the Japanese girl quickly figured it out and got up on her elbows, lifting her hips a little, with a quick, jerky movement, pressed herself against me."
    play sound sfx_7dl["sigh_out"]
    "And, forgetting herself, she cried out."
    me "Shh, shh, honey."
    "I covered her lips with a kiss."
    "And completely lost sight of the moment when we became one."
    "If it hadn't been for..."
    "Her cheeks wet with tears, and I stopped in surprise."
    me "Miku, sunshine, what?! Are you in pain?"
    "She grimaced:"
    mi "It's... It's okay, don't stop."
    "And she pulled me closer to her, continuing the movement."
    "Exhales sharper and sharper, more and more frequent, moving toward each other already, in a single rhythm, in a dance that is older than humanity and the same age as life itself."
    "My legs were already beginning to tire from the uncomfortable posture, plus I had to hold the girl with my hands to keep her from flopping - but all such little things..."
    "She forgot about everything - and so did I - the whole camp could probably hear us now - and she screamed as hard as she could, shaking all over, biting her lower lip."
    "Miku was babbling something, but I couldn't hear that, either - there was no 'me' in that moment..."
    "I let Miku inside me completely. Completely dissolved into her."
    "I think I lost consciousness."
    show blinking
    "Because I came to, standing by the table, leaning on it with my palms, all sweaty, breathing heavily, and Miku, who had already thrown my shirt over her shoulders to replace the one that had lost the buttons in the infamous struggle with me, looked at me with a warm delight in her eyes."
    scene bg int_clubs_dj_nolight_7dl
    show mi normal pioneer with dspr
    mi "I read in books that love is something mind blowing."
    mi "But to this extent... I guess it's because you were my first boy, Senecha."
    "Romance, falling in love."
    me "The orgasm starts in the head, doesn't it?"
    mi "You're smart. Will you come and give me a kiss?"
    stop music
    me "I'm afraid if I unglue off the table now, I'll fall."
    "Quietly I smiled, fighting the palpable weakness in my knees."
    me "I've used up all the energy I had. Now my hands are shaking, my legs are shaking."
    show mi laugh pioneer with dspr
    mi "So there's no movie?"
    me "What movie, after something like that..."
    mi "I'm kidding."
    "Miku winked."
    mi "But somewhere I've seen..."
    "She turned back to the closet and, after wrestling for a while, pulled out a mattress roll with a thin blanket and a pillow."
    mi "Let's spend the night here!"
    me "Are you sure?"
    "Miku, as a person accustomed to spending a lot but also getting a lot, worked at an incomparably faster pace than I did."
    "It's likely she's already made a lean or mean recovery."
    mi "Actually, I'd like us to sit and talk. Or we could go for a walk. {w}Or even better, go for another round!"
    show mi grin pioneer with dspr
    "She winked, looking at my dumbfounded face."
    mi "But that's just me... teasing.{w} I know that if I don't let what you and I did there heal..."
    "She stroked her lower abdomen with her palm."
    mi "It'll hurt later."
    me "So, maybe..."
    mi "No."
    "She laughed, guessing my thoughts."
    mi "We're not the Soviet Union, we were taught that kind of thing."
    mi "So we go to bed. {w}Together."
    show mi happy pioneer with dspr
    mi "I had a dream last night, did I tell you? About waking up in the same bed."
    me "Yeah, real prophetical."
    th "And something else."
    show mi smile pioneer with dspr
    mi "We'll sleep together, and you'll hold me! Mrrrr..."
    "Unbuttoning her shirt, she was left in nothing again, and sitting down on a blanket spread over the mattress, she held out her palms to me."
    mi "Come here."
    "Taking a few tentative steps, I sat up, almost collapsing on the mattress beside her."
    mi "Very good!"
    "Miku curled up, exuding peace and contentment."
    mi "Come on, lie down."
    "I didn't have time to lie down before I was instantly curled up, wrapped around her, my right arm taken away, and covered like a blanket and sighed happily."
    "What did she smell like - I inhaled the scent of her hair, her skin."
    "The damn essential oils weren't ready for that kind of exertion and had weathered out completely."
    "She smelled like Miku."
    "And I couldn't resist kissing the back of her neck, at the very hairline."
    "Miku shuddered and got goosebumps, instinctively sagging back a little and teasing me by pressing her hips together."
    mi "So..."
    "Sleepily she said."
    mi "No pestering at night, and if you do, don't wake me up."
    "I found no logic in what she said, but I prudently decided not to argue."
    me "Good night."
    mi "The quietest."
    "She replied."
    "And then silence descended upon me."
    stop music
    stop ambience
    scene black with fade
    $ alt_day5_mi_dj_hentai_done = True
    $ lp_mi += 1
    return

label alt_day5_mi_dj_sleeptime:
    scene bg ext_house_of_mt_night_without_light with fade
    play ambience ambience_camp_center_night fadein 1
    play music music_list["a_promise_from_distant_days_v2"] fadein 2
    "When I got home, I couldn't feel my legs under me from exhaustion."
    "I fucked up everywhere I could today. As much as I could."
    "In spite of all my attempts to get on the same page as Miku, she never let me say the most important thing."
    "And I don't know what that's going to cost me."
    if (alt_day5_mi_dj_voyeur == 2 and not alt_day5_mi_dj_dv_blade) or alt_day5_mi_dj_voyeur == 3:
        "And speaking of 'cost'..."
        "Without going up on the porch, I squeezed the soaked uniform on myself."
        th "If Olga finds out about the uniform, she'll kill me."
        th "Twice. The first time for soaking a fresh shirt, and the second time when she finds out under what circumstances this happened."
        th "Oh, to hell with it! I'll say I just washed the uniform."
        dreamgirl "Yeah. And she'll believe you."
        th "What, you want me to go to her in my underwear?!"
    stop ambience fadeout 1
    "The second step has always creaked so nastily here."
    "And I tell myself every day to do something about it."
    "And every day I forget."
    th "Now the leader inside will notice me, and..."
    "I'm frozen in half-step."
    dreamgirl "So? How long are you going to stand there? Or do you want to sleep in a chaise lounge?"
    th "In a chaise lounge? I don't think so."
    dreamgirl "Well, then put on your poker face and march into the house. I don't want to catch a cold!"
    "Prepared to lie my ass off, I pushed the door open."
    scene bg int_house_of_mt_night2 with fade
    play ambience ambience_int_cabin_night fadein 1
    "There was no one inside."
    dreamgirl "One less problem. Come on, let's get some sleep so we can try again tomorrow."
    "I hastened to follow the advice of my inner voice."
    "Undressed."
    if (alt_day5_mi_dj_voyeur == 2 and not alt_day5_mi_dj_dv_blade) or alt_day5_mi_dj_voyeur == 3:
        "Hung the wet things on the headboard."
        th "I hope they have time to dry properly by tomorrow morning."
    scene bg black with fade2
    "And, crawling under the blanket, I closed my eyes."
    "And in front of my gaze, a summary of today's results unfolded as usual."
    "And they were, frankly, not very comforting."
    "This day, which had begun so well and had been ruined by me..."
    "...Running around the camp in search of a girl - which has come to nothing..."
    "...The bonfire, to which the Japanese girl managed to pick out the most soul-destroying songs..."
    "...A terrorist act by Ulyanka..."
    if (alt_day5_mi_dj_voyeur in (2, 3)):
        "And the apotheosis of idiocy - my attempts to peek at who washes in there."
    elif alt_day5_mi_dj_apology == 0:
        "And finally, the cherry on the cake is how I managed to pick music that Miku didn't like, wanting to create atmosphere."
    elif alt_day5_mi_dj_apology == 3:
        "And another attempt at an apology that ended in nothing."
    if (alt_day5_mi_dj_voyeur in (2, 3)) or (alt_day5_mi_dj_apology in (0, 3)):
        "Feeling like a total loser, I fell asleep."
    else:
        th "I just hope everything will be okay."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_dj_neutral:
    scene bg int_house_of_mt_sunset with dissolve
    play music music_7dl["lastlight_piano"] fadein 2
    "Looks like the squad leader never came back for the night."
    "Her bed is untouched, even crumpled in the same mode as it was when we left for the bonfire, with the book upside down and lying on its open spread."
    "There you go. At least I got some sleep."
    "I looked at my watch - half past eight."
    th "Well, that means I'll have time for one last exercise and one last lineup."
    "I grinned."
    th "Even if I didn't make up properly yesterday, I'll make up for it by waving my arms and listening to another load of nonsense from the leader."
    "And up I went to face the new day!"
    with fade2
    if (alt_day5_mi_dj_voyeur == 2 and not alt_day5_mi_dj_dv_blade) or alt_day5_mi_dj_voyeur == 3:
        "Praise Random, the uniform has had time to dry!"
        if alt_day5_mi_dj_dv_kissing:
            "The sequence of events twitched my upper lip - it seems that Dvachevskaya had overdone her power over me last night."
    "The pocket slammed painfully against my chest - there was something heavy in it."
    "A smartphone."
    if (alt_day5_mi_dj_voyeur == 2 and not alt_day5_mi_dj_dv_blade) or alt_day5_mi_dj_voyeur == 3:
        "Didn't seem to be affected by the water."
    "There wasn't much charge left; if it weren't for the immortal battery and full autonomy mode, I'd probably be dead by now."
    "My fingers twisted the gallery by themselves, where the last pictures highlighted the volleyball court, my face in the sand."
    "And Lena's surprisingly warm smile - which transformed a usually sullen and unsociable face into a warm, sunny one, worthy of being admired, too."
    th "We should take a picture of the other pioneers, too."
    "I decided."
    th "Or at least Miku - I'll get laughed at on the internet for cosplaying, of course, but..."
    "Memory is too valuable a currency to throw away opportunities to get a few more memories."
    with flash
    play sound sfx_open_dooor_campus_1 fadein 0
    scene bg ext_houses_sunset
    play ambience ambience_camp_center_day fadein 5
    play music music_list["my_daily_life"]
    th "So, a quick look at the weather. Warm."
    "Compared to my last early rise - which was two days ago, because it had rained yesterday and I slept through the day before yesterday - it was really quite comfortable, even in a thin pioneer uniform."
    "It was empty outside - I think they gave the pioneers some indulgences after the bonfire. Well, or I don't know, maybe it was me getting up late again."
    "Though that's unlikely, the time on the clock was early - I can't vouch for the wake-up call, but the charge was certainly not yet sounded."
    "Throwing a towel over my shoulder and clutching my bathing gear, I ordered the autopilot to wake me up when we got to the sinks."
    scene bg ext_washstand2_day
    with dissolve
    play sound sfx_open_water_sink
    pause(2)
    play sound_loop sfx_water_sink_stream
    "The autopilot did even more than that - it duly dragged me to the tiled multi-legged monstrosity and, after opening the water, threw a handful of icy water in my face!"
    play sound sfx_draw_water
    with vpunch
    me "Ugh!"
    "For a split second I forgot how to breathe, my heart skipped a beat, and my mind felt like it had been dusted off."
    "And the world, to the brightness and contrast of which I was beginning to become accustomed, played again with colors unavailable to my ordinary life!"
    "But while I was there marveling at the beautiful morning, I completely forgot to turn off my subconscious."
    play sound sfx_draw_water
    with vpunch
    me "Ugh!"
    th "Okay, pest, let's stop!"
    dreamgirl "Oh, you're awake already... Senechka? I was beginning to think I was going to have to drag you to the breakfast and the lineup too."
    th "Shut up!"
    "The cold soap floating in the soap solution that had never been drained seemed even warm in contrast - and my face even hot!"
    "And..."
    me "Ugh… AAAHHHH!" with hpunch
    "As if it wasn't enough that my fingers were cramping, I think I stood up somehow wrong, as an icy trickle instantly made its way down my scruff."
    th "Mmmmmmhgh!"
    dreamgirl "You are not helping!"
    th "I'm trying!"
    play sound sfx_piano_head_bump
    "Looking for a pose where I couldn't be prodded by new portions of water down my scruff, I palpably rested my head on the sink."
    "And opened my eyes in surprise!"
    with flash
    "And certainly after that such a thing as ice in my hands seemed a minor setback."
    "The day was definitely beginning to be extremely successful and conducive to all endeavors."
    th "I'll have to try to make peace with Miku after all."
    "Gloomily I thought, polishing my jaw and, in between, trying to press the wet tip of my tie to the pilling bump at the very edge of my hair growth."
    th "Although if I've been this unlucky since this morning..."
    dreamgirl "Then it should certainly be good luck out there!"
    "I'm not convinced by my subconscious's words. And there was doubt in his voice, too."
    stop sound_loop
    play sound sfx_close_water_sink
    pause(1)
    if alt_day5_mi_dj_voyeur != 4:
        "With one last splash of water in my face, I straightened up - and shuddered."
        "I wasn't here alone!"
        scene bg ext_washstand_day with dissolve
        if alt_day5_mi_dj_voyeur == 3:
            show sl smile sport with dspr
            sl "Fizkult-hello!"
            "Slavya smiled, standing next to me."
            sl "Do you mind?"
            "I just shrugged my shoulders."
            "After dousing her yesterday, I realized I didn't know a tenth as much about this girl with her direct manners and open eyes."
            me "Only if you insist..."
            "I grumbled, wiping myself off."
            sl "Miku came up to me yesterday."
            "Slavya said, a little audibly."
            sl "And she told me something about you."
            th "Curious."
            sl "Look, I don't know why you fought with her. And you acted very foolishly last night."
            sl "But Miku said that she really, really likes someone. And that someone..."
            "She glared at me menacingly."
            sl "...offends her by showing her how much he doesn't care."
            me "But I don't... And anyway, it doesn't matter. {w}What did you say to her?"
            show sl smile2 sport with dspr
            sl "I said that sometimes boys do stupid things. A developmental lag of two years, what can you do."
            "She laughed and leaned over the sink, letting me know the conversation was over."
            th "So that's it!"
            "For half a minute I stood looking at the delicate skin of her neck, visible between her braids, fighting the urge to put my fingers on it."
            "And for a few minutes to drown the wretch so she wouldn't mock me!"
            th "It's her... It's her fault!"
            "I was well aware that if it hadn't been for that little wad of water, I might well have continued my search, and it might well have been successful."
            "But nooooo, you have to pretend to be a yamato nadeshiko and decide for everyone what's best for everyone!"
            dreamgirl "Relax, Senechka. She told you in clear Russian that she told Miku to come up to you on her own. Put your brain to work! Because right now it seems like you washed up, but forgot to wake up."
            dreamgirl "And you'd better get ready for the Jap visit - if you're blubbering and crumpling again, I'll simply put you out and do everything for you!"
            th "Wow! Can you?"
            dreamgirl "Theoretically. But it's such a headache to keep track of your reflexes and higher nervous activity. So come on, division of labor, as it is in a healthy normal organism."
            th "In a normal healthy organism, the subconscious mind has no say."
            dreamgirl "Really? What about instincts? What about reflexes? And your damn intuition, better known as situational logic? In short, don't talk nonsense if you don't know."
            sl "Semyon, you'd better hurry if you don't want to be late for your charge."
            "With a snort of goodbye, I hurried back to the cabin."
        elif alt_day5_mi_dj_voyeur == 2:
            show dv smile sport with dspr
            dv "Oh, hello."
            "That arrogant smile could be pasted on the walls of some snob's dwelling."
            "So the occasional visitor could immediately get a sense of his own level in this house - somewhere on the plinth level."
            me "Mm-hmm."
            dv "What's up? Are you sad?"
            if alt_day5_mi_dj_dv_kissing:
                dv "Or…"
                show dv laugh sport with dspr
                extend " You can't forget yesterday's?"
                dv "Well, tell me, who's a better kisser? Me? Or her?"
                me "Me."
                "Disgustedly I tossed, turning around."
                "Alisa immediately quit smirking."
            show dv normal sport with dspr
            dv "Listen... Semyon."
            "She stood next to me and turned on the water."
            th "She'll splash me."
            "I realized."
            dv "Your little upstart came by to see me. Anyway, she knows about last night."
            me "That's funny. What are you gonna do?"
            if alt_day5_mi_dj_dv_kissing:
                dv "Me? Nothing. I had a romantic shower date last night and an unforgettable first kiss. You know how much a first kiss means in a girl's life, don't you?"
            else:
                dv "Me? Nothing. I had a romantic date in the shower last night."
            extend " And why should I do anything about it?"
            me "Indeed."
            th "What an asshole you are, redhead!"
            dv "Well, you think about it."
            dreamgirl "Boy, I think she's hitting on you."
            th "Unobtrusively insinuating that I should let her keep doing what she did yesterday?"
            dreamgirl "Sort of."
            th "After she screwed up my chances of finding Miku yesterday?"
            th "And what for!"
            dreamgirl "If only she would have been naked there!"
            "In tune with me, my inner voice mockingly chimed in."
            "I was literally bursting with options one more enticing - whether I wanted to give myself an emergency lobotomy and pull the beast and ulcer out of my head, or gently take this adorable redhead by her frog tails and dunk her several times in cold water!"
            me "Thank you for the information."
            "Unbearably politely I replied to both interlocutors, gave a brief nod, and was off."
    scene bg ext_house_of_mt_sunset with fade
    "The camp here is very small, after all."
    "Where I was a guest, the number of pioneers exceeded several hundred, and of course one washbasin would hardly be able to wash all those who were suffering."
    "What's the matter? We ate in several shifts in the canteen!"
    th "Just like here, though."
    "Olga wasn't near the cabin, around the cabin, by the chaise lounge next to the cabin..."
    "But a few sandy prints on the steps gave her away."
    "It seems, while I was washing up, she came home after all."
    th "And then I'll be like, shortly, on the doorstep, hands to my sides, chin to my chest, eyes furiously rolled out: 'where have you been all night, bitch!'"
    play sound sfx_open_dooor_campus_1
    pause(1)
    stop ambience
    scene bg int_house_of_mt_sunset with dissolve
    "The cabin was empty."
    th "She changed her clothes and left."
    "Completely agreeing with this state of affairs, I put the soap and powder away in the nightstand and spent a few minutes wizzing by the mirror over the right tie knot."
    "For some reason I kept getting the classic windsor instead of the one I needed."
    "As a result, spitting on correctness, I just tied it in a double knot and, closing the door behind me"
    play sound sfx_open_dooor_campus_1
    scene bg ext_house_of_mt_sunset
    with dissolve
    pause(1)
    play sound sfx_close_door_clubs_nextroom
    extend ", went out."
    th "The minimum goal for today is to find Miku!"
    dreamgirl "Maximum goal?"
    th "We'll see."
    scene bg ext_square_sunset
    with dissolve
    play ambience ambience_camp_center_evening fadein 2
    "There were very few people in the square - it seems that my assumptions about some kind of indulgence have been fully confirmed."
    "As a matter of fact, the only people here were the girls of our troop, and a couple of the little ones who always used to take care of Ulyanka."
    "There was silence, disturbed only by the occasional yawn - no one wanted to talk in the morning from lack of sleep."
    show un normal sport at right with dissolve
    "Lena calmly met my gaze and nodded - she seemed to have gotten completely used to me in five days and stopped being shy."
    hide un
    show us smile sport at left
    with dissolve
    "Ulyanka was standing a little away - apparently she hadn't gotten scolded for last night, and she was ready to get the hell out in any case."
    "She winked at me, feeling my gaze, and, spreading out her index and middle fingers in the shape of an imaginary slingshot, drew an imaginary tourniquet and took aim with her left eye closed."
    hide us
    show dv normal sport
    with dissolve
    "Alisa stood next to her girlfriend and slept on the move."
    if alt_day5_mi_dj_voyeur == 2:
        "Apparently the washing didn't do her any good."
        if alt_day5_mi_dj_dv_kissing:
            show dv laugh sport with dspr
            "She opened her eyes just as I was staring at her, {w}- and our eyes met!"
            "She immediately opened them wide and folded her lips in a bow and gave me a deafening kiss."
            th "One word: bitch."
        "I blushed and hurriedly looked away."
    hide dv with dissolve
    "Everyone was standing there, yawning, waiting for the activist."
    "What a lark to the bone."
    show sl smile sport with dspr
    "And it didn't take her long!"
    "Hot from her run, she stood in front of the disorganized crowd and, finding my gaze, winked."
    sl "Squads... Line up!"
    "It didn't seem to matter to her how many of us were here - even if I stood alone. Once and for all established rules, cliques, and drills - can't be broken."
    th "Uuuuuu, you enemy!"
    if alt_day5_mi_dj_voyeur == 3:
        "The urge to drown or strangle the damn hottie didn't go anywhere."
    hide sl with dissolve
    "Also, the fact that Miku didn't show up for the lineup made a difference, too."
    "I'd be curious to see what she uses as her sports uniform, by the way."
    "Try as I might, I couldn't recall her wearing anything other than dresses or uniforms, which are essentially skirt-and-blouse uniforms that don't go far from dresses, either."
    th "Probably... Probably could have been a pair of her favorite turquoise or aquamarine colors."
    "Dreamily I thought, waving my arms."
    th "For example, short, tight shorts and a top that barely covers her breasts-so that all the pioneers watching will salivate profusely when she decides to do arm rotations or try her legs for stretching."
    th "Or perhaps some kind of translucent mesh t-shirt with a sports bra and half-skinned shorts, more suited to biking."
    dreamgirl "Or it could be a deaf plush Japanese-made suit!"
    "Ruthlessly debunked my dreams by my dark half."
    th "Hello! Why all of a sudden? Or don't you remember her dresses?"
    dreamgirl "Or don't you remember where you are? Have you, in all the time you've been here, seen her at least once in her stage clothes with the pom-poms hanging and the smart cloth?"
    dreamgirl "No. And you know why? Because to the local beau monde, her attire borders on pornography. Stupid people, what can you do."
    th "But her dress at the dance..."
    dreamgirl "Found in a costume shop and sewn to fit."
    "Ruthlessly parried the inner voice."
    dreamgirl "Imagine for a second that you're going to a pioneer camp, down south, in the summer - what do you take with you? Linen sweats, cotton - lightweight, short-sleeved, shorts in a number of pieces, swim trunks, flip-flops or slippers on cork, all right?"
    th "Well?"
    dreamgirl "Well, now, continuing the logical chain, imagine that you brought your huge heavy bag onto the property and just then learned that, it turns out, internal rules require you to wear only plain pants - and no jeans with hooligan slits and fringe! - And long-sleeved shirts."
    dreamgirl "Everything you brought with you is forbidden to wear. And you have nothing to wear. And here's a dance, and such a pretty - sympathetic girl is looking at you with interest, you know, as it usually happens: 'eyes opposite - don't mind'. What do you do?"
    th "Uh... I'll think of something of my own. Or if it's completely hopeless, I'll borrow one of my squad mates."
    dreamgirl "Yeah, or sew something from available curtains. Miku has tons of stuff, but you just can't wear any of it! Imagine what would happen if she showed up now in jeans, cropped to the very center, with a pantyline or thong strings sticking out... No, that'll start later, though. Well, that's not the point. I think you get the example."
    th "So she may well not show up for exercise just because her uniform was rejected?"
    "We moved on to squats, after which Alisa and Lena cleaned up for a run, and the rest of us waddled off to change for the upcoming lineup."
    play music music_list["get_to_know_me_better"] fadein 5
    with fade2
    "I, as an unclothed man, remained in my place."
    th "Strictly speaking, I have no business being here then either - in uniform."
    dreamgirl "Right. That's why you weren't stressed at all with the exercise yesterday or the day before."
    dreamgirl "If you'd realized your good fortune earlier, you'd have slept in today."
    "Totally confirming my thinking, a familiar blue-green-haired beauty loomed on the horizon."
    me "Good morning!"
    show mi normal pioneer with dspr
    mi "Hello, Se... Senechka."
    "With an effort she uttered."
    mi "Can I have a word with you without anyone hearing?"
    me "Sure."
    "The Japanese girl pulled me by the arm to the very pedestal with Genda and, looking around to see if anyone was eavesdropping, lowered her voice and spoke."
    mi "I was talking to Slavya today."
    if alt_day5_mi_dj_voyeur == 3:
        th "And now I'm going to get my ass reamed for my perversions of yesterday."
        "I went cold."
        with dissolve
        "Fortunately, I think I was wrong - Miku was talking about something else entirely."
    "It took her ten times longer than usual to say the last few phrases."
    "But this one took her about ten seconds to get through."
    me "I want to... Well, you know. If you... Anyway..."
    "She exhaled and smiled unabashedly."
    mi "What?"
    mi "Look... Excuse me? I acted so nasty yesterday. And all because of some words."
    me "I'm the one who's sorry. Some things are better kept to yourself."
    show mi sad pioneer with dspr
    mi "No! You said it right. If you didn't make it all up, every place has its own rules. Somewhere this camp never existed, somewhere Pa never met my Ma."
    mi "The rules are different everywhere. I only had the good sense to realize that today."
    me "Now what?"
    show mi shy pioneer with dspr
    mi "Maybe we should try again?"
    mi "From the beginning. Or rather, not from the beginning, but from the middle, or rather, from that place... like we paused yesterday and then went back today."
    mi "Well, what do you think?"
    "My heart fluttered somewhere under my throat like a hummingbird and beat at the same pace - fast, fast, reverberating in my temples and fingertips."
    "And I stepped toward her, put my hands on her shoulders, and tried to see the emptiness of yesterday in her eyes. It really wasn't there- instead there were heavy clouds of doubt at the bottom of my eyes."
    "Which I hastened to dispel as I held her to me as tightly as I could, shivering, shivering, hot-hot."
    me "I'd be right happy to."
    "I exhaled into the top of her head."
    stop music
    play sound sfx_7dl["highfive"] fadein 0
    pause(1)
    play sound sfx_7dl["highfive"] fadein 0
    pause(1)
    play sound sfx_7dl["highfive"] fadein 0
    "Miku recoiled in fright, and I turned my attention to Olga Dmitrievna sneaking up in her own style."
    hide mi
    show mt smile pioneer with dspr
    mt "Pioneers, when you've had your fill of hugs, fall in line, lineup is in two minutes."
    hide mt with dissolve
    "Olga Dmitrievna winked at me and took her place on the podium."
    "Taking the girl by the hand, I dragged her to the place where our pioneers were already lined up, and, pushing Alisa and Lena aside, I took a place in the back row."
    "I put Miku next to me, of course."
    show mi smile pioneer with dspr
    "She found my palm and squeezed it lightly."
    "I couldn't believe that anyone could control the girl in moments like this - the way she wrinkles her nose laughingly, the way her pupils jump up, taking up almost the entire iris, the way she bites her lip when I tickle her palm with my fingers..."
    "It's too complicated for a program. Too detailed for memory, and I've never had anyone so direct."
    "Well, if someone is controlling her... He must be a micromanagement god - which, if memory serves me correctly, resides in South Korea and prefers to attack Protoss bases over all silliness with kisses."
    "I drew spirals and circles and weird geometric shapes on her palm and watched her tickle."
    show mi shy pioneer with dspr
    mi "Why are you doing this?"
    "I shrugged and let my fingers go from palm to wrist."
    "Miku flinched and, with a shrug, took her hand away."
    show mi upset pioneer with dspr
    mi "Senechka! Stop it!"
    me "Stop it altogether?"
    "I raised an eyebrow questioningly."
    me "Or can we come back to this sometime later?"
    show mi shy pioneer with dspr
    mi "We can…"
    play music music_list["everlasting_summer"] fadein 3
    "Slavya left the formation and took a place under the podium."
    mt "Comrades! Friends! Pioneers!"
    "The squad leader began."
    mt "Today is the last day of the camp shift number «two» of the 1989th year."
    mt "Shift with thematical name - «Musical»!"
    mt "For someone, this was their first time at our camp - and I really hope that they enjoyed it as much as those who have been coming here for years."
    mt "And some of us have already become friends and see each other year after year, over and over again, and we're very happy to see them here at camp «Sovyonok»."
    mt "It's been quite an unusual shift, and not the least of which I thank our music circle leader, Miku, for it!"
    "Miku tiptoed up and waved over Lena's head."
    mt "Miku is considered quite a popular personality in her home country, and the fact that she has done several concerts speaks volumes about her professionalism. By the way, there will be a farewell gala concert tonight, the opening and conducting of which also rests on her delicate shoulders!"
    "After waiting out the applause, the leader continued:"
    mt "In addition, Miku has graciously agreed to host a night dance for us and host the final radio broadcast tonight along with her assistant, Semyon!"
    "Unlike Miku, I did not seek publicity at all - instead, red as a crab, I confined myself to a brief nod over Alisa's head."
    mt "By the way, we owe it to Semyon that Miku agreed to lead the dance."
    th "Enough!"
    "I asked with a look."
    "Olga smiled her best, winked at me, and continued:"
    mt "In addition, today the squads turn in their farewell wall newspapers, clean up the grounds, and return the squad flags to the linen closet."
    mt "Oh, and don't forget - instead of a quiet hour, there's a rehearsal today for all the concert participants. Starts at half past three, please don't be late. Slavya."
    "Slavya, waiting for the last phrase, nodded and marched solemnly to the flagpole, where a flag was already waiting to be flown."
    "I've always been curious, when and who brings it down?"
    "I caught the Japanese girl's hand again and ran my fingers between hers."
    show mi happy pioneer with dspr
    mi "You're doing something stupid again that makes me want to cry."
    mi "Where did you pick that up?"
    "I just shrugged my shoulders. Just doing what I want to do the most. Although kissing is probably the thing I want to do the most. But you can't."
    "I sighed."
    "The cloth got to the halfway point, the whole camp had an ossification of the neck."
    th "It's time!"
    "Abruptly yanking Miku toward me, I hugged her as hard as I could and dug my lips into hers."
    dreamgirl "Thirteen… Twelve… Eleven… You're a psycho, you know that?"
    th "Yeah."
    "The sharp tip of her tongue stung my tongue, and I found her other hand, let my fingers intertwine."
    "Aquamarine eyes stared at me in amazement, but a familiar mischief was already splashing within them - the same mischief I'd almost lost yesterday."
    dreamgirl "Six… Five… So, it's that time, yeah?"
    th "Yes. Time to go crazy."
    dreamgirl "Two… One… Time!"
    "Biting her lip lightly, I unhappily pulled away and, turning right around, stretched out in a frunt!"
    "Nearby someone grudgingly snorted and stepped on my foot."
    me "Eh?"
    show mi angry pioneer with dspr
    mi "Is that how it is, huh?"
    "She whispered."
    mt "Squads… Turn left!"
    "The squad leader's voice overrode both Miku's whispering and all other sounds."
    mt "Behind the first squad to the canteen... march!"
    stop music fadeout 5
    "Miku clawed at my palm and squeezed it as hard as she could."
    if alt_day5_mi_dj_apology == 2:
        me "Ttz!"
        "I hissed."
        show mi sad pioneer with dspr
        mi "Oh, sorry Senechka!"
        "I joked:"
    else:
        me "Whoa!"
        "I laughed."
    me "You prefer sado-maso?"
    show mi shy pioneer with dspr
    mi "Bastard! You're a bastard, Senechka!"
    "She was walking beside me, all red, and if I still had any doubts about how alive she was..."
    "Well, there were none left now."
    return

label alt_day6_mi_dj_neutral_breakfast:
    scene bg ext_dining_hall_near_sunset with dissolve
    play sound sfx_open_door_2
    play music music_list["smooth_machine"] fadein 5
    "Having opened the door in front of Miku, this time, already alert, I instantly leaked in after her, leaving the prerogative of those behind me to hold the door themselves."
    scene bg int_dining_hall_people_sunset_7dl
    show mi normal pioneer
    with dissolve
    play ambience ambience_dining_hall_full fadein 3
    "So our favorite window seats were vacant, and Miku hurried to occupy them while I jostled for distribution."
    th "So, what did Random send us today?"
    "Thought I, peering into the plates with a suspicious yellowish sticky mass."
    "It was completely unidentifiable - unlike the cheese sandwiches and for once normal cofee."
    "I even had to look at the menu, because the cook, when asked 'what planet did this come from', gave me a look that made me not want to continue the questionnaire."
    "So, the menu, pinned to the tablet on the pole at the distribution table, confidentially informed me that the yellowish crap was 'Druzhba' porridge, wheat and corn with condensed milk."
    th "Brrr. I hope it's at least edible."
    with fade
    if alt_day5_mi_dj_apology == 2:
        "I had to walk several times - I carried the tray in a very cunning manner on the palm of my left hand and forearm of the other."
    else:
        "Balancing three plates, two glasses, and an unknown number of spoons - all on one tray - I snuck over to Miku and set her breakfast in front of her."
    me "Except I don't know about the porridge..."
    show mi grin pioneer with dspr
    mi "Don't mind her looks, Senechka."
    "Miku surprised me by launching the first spoonful into her mouth without much thought."
    mi "It just looks like that, but its actually very tasty. Bon appetit!"
    me "Thank you, same to you."
    "We made it with spoons."
    "Miku didn't fool me - the suspicious mass tasted very decent, despite my misgivings, no one tried to disguise a poorly made product with tons of condensed milk - everything was acceptable and quite tasty."
    me "It wasn't bad after all."
    show mi smile pioneer with dspr
    mi "The food here in general is good, I like it, I thought about writing down a couple of recipes for home, until I realized that half of the local products I just can't get at home."
    me "I see. {w}What are you doing now, where to after breakfast?"
    show mi upset pioneer with dspr
    mi "To tell you the truth, I wish I could take you and run away somewhere. You and I have still have a thing from lineup waiting to happen."
    "She bit her lip and stroked my leg under the table."
    mi "But..."
    "She sighed so ostentatiously that I could barely keep from poking her in the side with my finger."
    th "What more bullying of poor me!"
    dreamgirl "You've recovered quickly. Getting cocky already..."
    th "What?"
    dreamgirl "Nothing, nothing, I'm not saying anything."
    mi "We have a holiday broadcast and rehearsal in the morning."
    mi "Although I'm exempt from rehearsals as a radio host - but I have to open the concert, so I have to rehearse at least a couple of times."
    me "And me?"
    mi "Well, you'll just fill in for me at the microphone."
    mi "Although the rehearsal is in the afternoon... We'll go there together!"
    th "Thanks for that."
    scene bg ext_dining_hall_near_sunset
    show mi smile pioneer
    with dissolve
    "After collecting the dishes and taking them to the dishwasher, we went outside."
    mi "Today I'm going to spin only the most festive things for the whole camp!"
    "Miku rubbed her palms together in impatience and rushed down the road to the clubs."
    hide mi with dissolve
    "Expecting a several-hour marathon of chatter, music, and dancing, I, scratching the back of my head, set off after her."
    "But I guess I was wrong."
    scene bg ext_clubs_day with dissolve
    "We didn't have time to get settled in the club before we got distracted."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_dj_good:
    if persistent.hentai_graphics_7dl:
        scene cg d6_mi_morning_7dl with dissolve
    else:
        scene bg int_clubs_dj_7dl with dissolve
    play music music_list["so_good_to_be_careless"] fadein 5
    "I woke up to Miku wiggling underneath me and muttering something unhappily."
    mi "Wake up, Senechka. Great things await us!"
    me "What kind of things?"
    mi "Judging by the clock, our first feat will be to start broadcasting."
    "She smiled."
    "I cast a glance at the time - it's the beginning of ten."
    me "It's a deal. You start broadcasting and I'll go get us something to eat."
    mi "Stop by my house! If Lena's there, tell her I sent it. I have instant noodles in one of the compartments."
    th "Oh. My. God. And how can I get away from bum packages?"
    mi "Come on, come on, get up, or someone will look in, and here we are!"
    "She quickly, quickly rolled up the mattress and pushed it onto a shelf in the closet."
    mi "And get me some T-shirt, please. Because someone attacked me last night and messed up my clothes!"
    mi "You can have your shirt, all right, I'll put mine on for now. But hurry up, or something might happen."
    "After putting on my shirt and struggling to find my tie, which I didn't know what it was doing on the TV, I cleaned myself up as much as possible, touched Miku's temple with my lips, and headed out into the street."
    "Electronik wasn't here yet, so my 'disguise' was working for all it was worth."
    scene bg ext_clubs_sunset_7dl
    with dissolve
    "It was half past ten, and it looked like I was really hopelessly late for breakfast."
    "I had to take the Japanese girl's advice and go to her cabin for food."
    "So, trot number one - past the cabins."
    "I didn't spend the night at home, and Olga Dmitrievna will probably want to ask me some questions - which I won't be able to answer. And why should I need all these suspicions and awkward situations."
    "I remembered myself the day before yesterday, sneaking around just like that."
    th "Time is a flat circle, isn't it?"
    "Well, this time the route was much shorter."
    if alt_day5_mi_dj_voyeur == 2:
        "But the timing was a little off, too! I didn't have time to get out on the porch before Dvachevskaya caught me."
        show dv normal pioneer with dspr
        dv "Hey. Didn't see you at the lineup."
        me "Uh-huh."
        dv "Where's your friend?"
    "Then the speakers above us hissed, and the silver notes of her voice rolled out of the horns in a ripe staccato voice throughout the camp."
    th "Perhaps I've chosen a pacifier and a phony, and all my senses are lying to me, and my imagination is doving everything else."
    th "But I'll be damned if her voice isn't worth it! Even in the tinny Soviet loudspeakers!"
    mi "And - good morning, camp! Today is the last day of the shift, and I don't know about you, but I'm going to enjoy life to the fullest!"
    mi "The temperature on the thermometer is twenty-eight degrees, the weathermen are threatening for it to crawl up to thirty-five by noon, which means the water will be heavenly and no rain! Perfect conditions to do what you've been putting off for later is today."
    mi "Anything you've wanted to do but haven't done. Go for it!"
    play music music_list["everlasting_summer"] fadein 3
    mi "And so that the fighting spirit doesn't leave you, I'm putting on this beautiful tune for you."
    if alt_day5_mi_dj_voyeur == 2:
        dv "Un-der-stan-da-ble."
        "In syllables said Alisa."
        me "What, what do you understand?"
        "I reminded myself of a curled-up hedgehog, on reflexes alone - one! - and I'm already a prickly ball."
        show dv laugh pioneer with dspr
        dv "Don't be so afraid, I won't say anything to anyone."
        "She winked at me and turned towards her cabin."
        hide dv with dissolve
    "I, myself, in a fighting mood - at least to get my silly squaw some noodles - headed in the direction of Miku's headquarters, where I could easily get to her cabin."
    "Fortunately, I didn't run into anyone else along the way, and I didn't have to prove to anyone that I wasn't a camel or anything like that anymore."
    "Although the giggling bushes did get caught once."
    "But I had already stopped paying attention to Ulyanka - she seemed to take great pleasure in giggling at those around her."
    scene bg ext_house_of_un_day
    with dissolve
    stop music fadeout 5
    "After reaching the final destination without much adventure, mindful that a girl might well be changing clothes inside, I knocked."
    play sound sfx_knock_door7_polite
    "Well, or maybe there just might not be anyone there - Miku didn't give me the keys after all!"
    un "It's open."
    "The voice was calm, no hints of «leave me alone». Although, after yesterday…"
    if alt_day_binder != 1:
        play music music_list["lets_be_friends"] fadein 5
    else:
        play music music_7dl["take_my_hand"] fadein 4
    play sound sfx_open_dooor_campus_2
    pause(1)
    scene bg int_house_of_un_day
    with dissolve
    show un normal pioneer at center
    with dissolve
    "Lena was sitting by the table, drawing something on a large sheet of cotton paper with quick, quick lines with a pencil."
    me "Not interrupting?"
    un "No."
    "She answered without turning her head."
    un "Not really."
    me "I'm from Miku..."
    "I began."
    un "She didn't sleep at home. So..."
    "She left the end of the sentence in the air."
    me "Yes."
    show un cry_smile pioneer with dspr
    "For a second, when she stopped tinkering, she turned her head in my direction."
    un "Forgive me for not expressing exuberant joy. I don't know how to."
    "Tears glistened in her eyes, and she immediately turned back to the sheet."
    me "Miku sent me..."
    un "She did the right thing."
    show un smile pioneer with dspr
    "Lena burst into tears."
    me "For food."
    un "Oh. This is more serious. You want me to feed you?"
    me "No. I'm going to rustle her up a little, she let it slip that she came with a supply of egg noodles."
    show un smile2 pioneer with dspr
    un "Oh, come on then. Her bag is in the closet."
    me "Say... Don't you have a spare uniform shirt here? Because she asked me to bring her some more T-shirts, and I'm not sure the squad leader would appreciate it."
    show un shocked pioneer with dspr
    un "What happened with you there?"
    me "Nothing much."
    show un grin pioneer with dspr
    un "After «nothing» you usually don't need spare shirts. Hold on."
    hide un with moveoutleft
    "She got up and walked over to the closet, flipping the sheet clean side up."
    "Something she was drawing there - something she really didn't want to show me."
    "After struggling a little between curiosity and good manners, I decided to opt for manners and pulled out a fancy Japanese suitcase, opened the hard lid, turned things around a little - something lacy-gassy, all very small, very short, sprinkled with some smelly muck."
    "The main compartment had only clothes and hygiene products."
    dreamgirl "Wow! With silver. I wonder what they THINK silver is for there? To kill germs?"
    th "How should I know? What am I, a girl or something?"
    "After closing the main compartment, I started on the second, more of a drawer."
    "And then I glanced at several boxes of hard, heavy paper with a cartoon girl with bright yellow curls on the top lid."
    "Glimpsing the way the Japanese duplicate words from their native japanese and English terms in the same phrase, I read what I could make out:"
    me "Instant… Ramen…"
    "Instant noodles - instant. Oh, those Japanese marketers."
    un "Here."
    "Lena stood, holding out a shirt."
    show un shy pioneer with dspr
    un "Though it'll probably be too wide for Miku... But it's better than a T-shirt."
    me "Thank you very much."
    show un serious pioneer with dspr
    un "Not doing it for you."
    "She looked away diligently."
    "I reached out, taking my shirt, and our fingers touched for a moment."
    show un shy pioneer far with dspr
    un "Anything else?"
    "She squeezed out."
    me "No."
    un "Have a nice day."
    "Showing she was no longer interested in me, she sat back down at her desk and turned the sheet over."
    "The pencil flew over the surface of the paper again."
    th "I think I've offended her in some way."
    dreamgirl "Yeah."
    th "But how?"
    dreamgirl "Nothing. Never mind."
    "Bygones are bygones - I closed the suitcase and hid it back in the closet, trying to move as quietly as possible, cleared the temple and shut the door behind me."
    stop music fadeout 5
    play sound sfx_open_dooor_campus_2
    pause(1)
    scene bg ext_house_of_un_day
    play music music_list["my_daily_life"] fadein 5
    th "Strange girl."
    dreamgirl "Everyone's weird to you. Miku isn't real, Ryzhevskaya is horny, Slavya is uninhibited, and now Lena's got her fill too."
    dreamgirl "Only because she dared to suddenly not act like a robot."
    th "What are you talking about?!"
    "There was a distinct slap of a palm against a face."
    dreamgirl "Oh, don't say anything! You're hopeless!"
    "Hopeless or not, my squaw-fast-voiced should have been fed immediately!"
    "And so, wrapping the noodles in my shirt and hiding the resulting bundle under my armpit, I hurried to the radio room."
    scene bg int_clubs_dj_7dl
    show mi smile pioneer
    with flash
    "Miku wasn't even as excited about the breakfast she brought as she was about the opportunity to change."
    show mi happy pioneer with dspr
    mi "Oh, thank you, Senechka, you helped me out! Squad leader came by, asked questions - I was so terrified when I had to hide from her."
    mi "It's okay though, I had to tell her I had a stomach ache."
    if alt_day3_technoquest1:
        me "Hey! What about your own words about lying?"
        show mi laugh pioneer with dspr
        mi "That's between the two of us! It is possible to lie to an external enemy to save our life."
        show mi sad pioneer with dspr
        mi "It's better not to abuse it, though."
    with fade
    mi "Okay, I'll fuss with the broadcast while you go check in the next room - I asked Electronik to boil some water there."
    me "Yessir!"
    "I threw two fingers to my temple."
    stop ambience fadeout 2
    play sound sfx_open_door_clubs
    pause(1)
    scene bg int_clubs_male_day with dissolve
    play ambience ambience_clubs_inside_day fadein 3
    "There was no one in the next room when I came in."
    "There was no one there even now."
    me "Electronik!"
    el "Wait!"
    "A voice came from somewhere above."
    me "What are you doing there?"
    el "What-what. Finished repairing our emitter from yesterday. I'll install it n…"
    play sound sfx_bus_window_hit
    "There was an abrupt thumping sound from above - it seemed that Electronik had met the beam with his forehead after all."
    th "It's a good thing I have my own guardian angel, though!"
    dreamgirl "That's right! Remember that!"
    el "Ow…!"
    "What followed were unintelligible swear words - distilled in the spirit of «not scientifically possible» and «when will it all end», and a few minutes of rumbling later, from the heights of heaven, He descended to me."
    "He looked, honestly, not good - covered in the dust and cobwebs that I didn't have time to pick up yesterday, a fresh bump on his forehead... Handsome, in short!"
    show el normal pioneer with dspr
    el "That's it! Now it will work properly. Because, I'm still coming here next year to rest, I don't want to come to everything being all chewed up."
    me "Yeah."
    el "Oh, yes, Semyon."
    "He shook my hand hastily."
    el "What are you here for?"
    me "Miku asked me to find out about the water."
    el "Ah, water."
    el "Here's the jar, here's the boiler."
    me "So you didn't boil it?"
    show el upset pioneer with dspr
    el "Took too long."
    me "True..."
    "I didn't have the energy to get mad at the cyberneticist - it had to be refreshed first."
    "I had to boil it myself, brew my own noodles, sneezing dried vegetables and extra-thermo-nuclear seasoning."
    play sound sfx_open_door_clubs_2
    scene cg d7_mi_ramen_7dl with dissolve
    "And himself on a makeshift tray of organolite to bring food to my squaw."
    me "Itadakimasu!"
    "I notified her, removing the lids and breaking out the chopsticks."
    mi "Forgot to put the water on?"
    "The Japanese girl guessed."
    "I nodded."
    mi "Scattered geniuses. Itadakimasu."
    "She duplicated my actions and, pushing the long-playing tape recorder with her elbow, dipped the sticks into the thick broth."
    "For a while there was only a huffing and a crackling from behind my ears."
    with fade2
    "The portions were generous, unlike our store portions, but a hungry pioneer could not be embarrassed by a large portion..."
    mi "Like everything good in this life..."
    "Miku was obviously quoting someone."
    me "Yes. So, what's next?"
    mi "Before lunch - broadcast, after lunch there's a rehearsal, there's a concert and then dinner is on the way. After dinner, disco."
    mi "See? It's all scheduled by the minute."
    "I wanted to answer her, but we were interrupted."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_dj_radio:
    play music music_7dl["rewind"] fadein 0
    scene bg int_clubs_dj_7dl
    show mi normal pioneer
    with flash
    play sound sfx_knock_door7_polite
    "There was a soft knock at the door."
    mi "Yes, come in!"
    show un normal pioneer at left with dissolve
    un "Um... Hi, guys."
    mi "Hi, Lena. What are you here for?"
    un "Shouldn't you be at rehearsal prep?"
    mi "Actually, we should be. But we're radio hosts, we're excused."
    show un shy pioneer with dspr
    un "Is that so."
    "Lena turned around and was about to leave."
    mi "Lena!"
    un "Yes?"
    mi "Aren't you forgetting something?"
    un "Excuse me?"
    mi "You came here for something, didn't you?"
    un "Oh..."
    "Lena blushed, and only now I noticed that until now she was clutching some kind of folder to her chest."
    un "I thought you were on the stage, but I thought I'd look for you here first, and..."
    "She exhaled."
    show un normal pioneer with dspr
    un "Anyway, here."
    "She opened the folder and pulled out a stack of papers, which she held out to me."
    un "For the wall paper."
    me "What's in here?"
    un "Well, it's... It's... It's kind of..."
    "I held the paper up to my eyes."
    dreamgirl "Our exploits are here."
    "In a certain order, which was not quite clear to me, in the bundle were stacked sheets with hand-drawn pencil drawings, in which, after looking closely, I recognized - myself."
    un "Here."
    show un smile2 pioneer with dspr
    "Lena smiled unabashedly."
    un "I drew."
    "She really did!"
    play music music_7dl["yume_akari"] fadein 3
    if alt_day5_mi_dj_dv_kissing:
        "The first picture stunned me, because unless Dvachevskaya started blabbering..."
        dreamgirl "Then someone peeked!"
        th "Exactly!"
        "{i}A picture drawn at a very sharp, complex angle, lined up in a four-point perspective - as if the artist was taking a nature from somewhere under the ceiling.{/i}"
        "{i}If this were happening nowadays, I would think it was taken from some hidden camera from above.{/i}"
        "{i}Alisa in a wet swimsuit, which expressively emphasizes all the advantages of the figure, and standing so that you can look under the cups, stands with her legs a little springy, and, pinning some abstract young man to the wall…{/i}"
        "{i}…kisses him!{/i}"
        "{i}It is impossible to make out who, exactly, it is - only the top of the head is visible, plus the slanting jets of the shower greatly mask the facial features.{/i}"
        "I went cold."
        th "Did she just..."
        show un shy pioneer with dspr
        un "Oh, that's not supposed to be there. It was an accident."
        "Lena winked at me."
        "Exhaling, I hid the blackmail material at the bottom of the pack, taking in the next picture."
    if alt_day4_mi_dj_hedg:
        scene cg d4_mi_hedgehod_7dl
        show prologue_dream
        with dissolve
        "{i}Here were the events of the day before yesterday.{/i}"
        "{i}To tell you the truth, Lena obviously had nowhere to see this picture - and, apparently, she drew it based on someone else's story.{/i}"
        "I stared questioningly at Miku."
        scene bg int_clubs_dj_7dl
        show un smile pioneer at left
        show mi shy pioneer
        with dissolve
        mi "What's the big deal? It's just a funny story!"
        "With a shrug, I went back to studying the cartoon."
        scene cg d4_mi_hedgehod_7dl
        show prologue_dream
        with dissolve
        "{i}In the background of the tiny music club was a picture of a huge snorting hedgehog running at the speed of a good locomotive, with two savages running after him, jumping and dancing.{/i}"
        "{i}One is recognizable by the abundant hair covering half of his face - he is dressed in shorts, a tie tied right around his bare neck, and a spear in his hand.{/i}"
        "{i}The second savage, or rather female savage, is dressed in a kind of skirt, although most of the clothes, of course, are her long hair.{/i}"
        scene bg int_clubs_dj_7dl
        show un smile pioneer at left
        show mi smile pioneer
        with dissolve
        me "Hunting the beast, eh?"
        show mi laugh pioneer
        show un laugh pioneer at left
        with dspr
        "The girls laughed out loud."
        "And I held out the picture to Lena and stared at the next one."
    "{i}The next picture was more for the soul than for fun - no flamboyant, grotesque features, everything modest, noble, classy.{/i}"
    "{i}A volleyball net, on one side of which stand Ulyana, Lena and some faceless pioneer, on the other side - Olga Dmitrievna, PE teacher and Alisa.{/i}"
    me "Great game, huh?"
    "{i}The ball is high up in the sky, launched by a certain armless pioneer.{/i}"
    th "By the way, that was a test pitch! {w} And we fought for it for, like, ten minutes!"
    "{i}A halted moment - the girls turned in my direction, me, who took a particularly sharp cut on the 'boats', Dvachevskaya, frozen in the air after the blow…{/i}"
    show un smile pioneer at left with dspr
    un "Yeah…"
    show mi sad pioneer with dspr
    mi "And I missed everything. I walked around, showing Pa where the water tower is. What does he need it for..."
    me "He's an engineer, he's curious about such things by default."
    mi "I don't think so. You have to take a break from work sometimes - his words, by the way!"
    "I just shrugged my shoulders and gave the picture to the author."
    me "Now that would look great!"
    un "Yes, I was going to run it in the center of the strip myself."
    un "Along with this one..."
    "She nodded at the next picture in my hands."
    th "Well, who would have doubted it. My dorky underlings with their vomit-eyed costumes and vomit-eyed chants."
    "Although in this particular shot, it was the synchronicity of the performance that made me happy."
    th "Ha! They'd better try to be out of sync after the 500th repetition."
    "{i}On the big stage, overlapping it entirely in length, stretched a row of kids in costumes with green hoods, huge yellow plastic beaks, and wings.{/i}"
    "{i}They make some movement, but it becomes apparent that their dance is not quite consistent - someone is waving a little harder, someone's arms are a little longer.{/i}"
    "{i}And the one on the far right is squinting from the sun hitting his eyes, he can't see the audience at all, and therefore he has a lost and amused look.{/i}"
    me "Concert for parents, right?"
    un "Yes... I wish I had time to sketch today's one."
    show mi normal pioneer with dspr
    mi "So, try to remember it well - and then you can sketch it at home from memory!"
    mi "You have my address, if you want it, you can mail it to me."
    show un smile pioneer with dspr
    un "I will!"
    "The stack of sketches came to an end, jogging my memory just right, and I covered my eyes and ran everything that came to mind in front of my inner eye."
    "Was doing an audit of the riches I would take away from here with me - it didn't matter so much where, to the local 'mainland' or back home."
    dreamgirl "Not that important?!"
    th "That wasn't the right way to put it, I admit it. But one way or another, those memories can never be taken away from me."
    th "And thanks to Random, there were some particularly poignant moments she just didn't know about."
    th "Like the bathhouse with Slavya."
    if alt_day5_mi_dj_dv_kissing:
        "Although... judging by her look and the picture of Alisa, for example... Some things she just decided not to make public."
    else:
        "Although... judging by the look in her eyes... Some things she just decided not to make public."
    dreamgirl "Or she couldn't - think of the buzzing emitter. {w}Though you have to admit, her intelligence is top-notch."
    if alt_day4_mi_dj_hedg:
        un "So volleyball, a hedgehog hunt, and a concert are put in?"
    else:
        "So volleyball and a concert are put in?"
    me "Of course."
    un "Fine. Here's more - but I have my doubts about these. After all..."
    show un shy pioneer with dspr
    extend " They're personal."
    "She held out a second packet to me, intercepted with a paper clip."
    if alt_day3_dancing1 == 'mi_1' or alt_day3_dancing2 in ('mi_2', 'mi_12'):
        "{i}The first picture made me smile - it was so well done.{/i}"
        "{i}A recognizable square with Genda fixing his glasses, trees decorated with garlands, four columns along the perimeter of an imaginary square, and spotlights on the trees.{/i}"
        "{i}At the very pedestal there is a table with a lamp on, on the right-hand side there are consoles, turntables and a tape recorder, on the left-hand side there are some papers and piles of records.{/i}"
        "{i}The host herself, portrayed in what in my day is called 'chibi', is wearing a tight blue-green dress - and, as if for extra humorous contrast, with huge headphones down around her neck.{/i}"
        "{i}She is standing erect - though I have no idea how the artist managed to create the impression of ballet posture on a big-headed man! - and casually holding her left hand on the shoulder of a very familiar pioneer.{/i}"
        "{i}And the other one - threatening with her fist into the frame! Without looking away, though, or turning her head away from the pioneer.{/i}"
        "Miku giggled, looking over my shoulder."
        show mi laugh pioneer with dspr
        mi "So you drew it after all!"
        show un smile pioneer with dspr
        un "I have every right to!"
        show mi smile pioneer with dspr
        mi "You do. But you better keep it, okay? I don't want my dancing with Senechka to get in the frame."
        show un smile2 pioneer with dspr
        un "Well... Since you're asking..."
    "The next picture Miku approved instantly."
    "{i}Shuddering bass, bouncing speakers, applauding audience - and there she is on stage.{/i}"
    "{i}A diminutive, frail figure with long tails, holding the microphone in a hooligan way, with her left foot back on her toe, she pokes her finger impolitely at the audience.{/i}"
    "{i}It looks like she's just getting warmed up, beginning to enjoy the show - see how her cheeks are flushed, see how her eyes shine.{/i}"
    me "I don't remember that."
    show mi grin pioneer with dspr
    mi "You shouldn't - that was before you showed up. If I'm not confused, the shot is from the opening of the shift, right?"
    mi "I also sang «Blow with the Fires» here."
    "Lena nodded."
    mi "That's a definite yes."
    "Lena nodded and hid the approved drawing back in the folder."
    if alt_day3_dancing1 == 'mi_1' or alt_day3_dancing2 in ('mi_2', 'mi_12'):
        "{i}The next shot was from the same chibi-series as our dance with the Japanese girl, but this time no frills like extra people in the frame - just music, speakers, hands on vinyl and a faceless mass, depicted with a few strokes, in the background.{/i}"
    "{i}The presenter, like a professional disc jockey, holds an earpiece to her ear, leaving the other earpiece free, turns something on the mixer, smiles and dances at the same time.{/i}"
    show mi smile pioneer with dspr
    mi "I approve! I've never tried out as a DJ before - and you know what? I loved it!"
    "We went on at a brisk pace."
    "{i}Miku as the radio host in the headphones at the microphone.{/i}"
    mi "Well, no, it's the same as the disco. Boring!"
    "{i}Miku's concert by the fire.{/i}"
    show mi serious pioneer with dspr
    mi "You know... It's better not to put that in either. I have a bad memory of that."
    "She cast a leering glance in my direction."
    "And I sighed. What else could I do?"
    "Miku quickly, quickly flipped through the remaining drawings and, with a nod, gave them to Lena."
    me "You're like a camp photographer."
    "I complimented the artist."
    show un shy pioneer with dspr
    un "No. It's just..."
    mi "Usually Uncle Borja-sensei takes the pictures, but he has no time at all."
    "Lena was quiet for a while, apparently not knowing how to bow out politely."
    "And then she remembered:"
    un "Yes... One last thing."
    play music music_list["your_bright_side"] fadein 3
    show un grin pioneer with dspr
    un "This is a gift to you from me personally."
    if (not alt_day3_duty) and (alt_day2_date == 'mi') and (alt_day2_mi_date != 2):
        me "That one picture!"
        show mi serious pioneer with dspr
        mi "Aha."
        un "You two figure out among yourselves who she goes to."
        "At last I saw what the unsociable girl was grieving over after my evening with Miku."
        "Just about what I'd imagined when I once again tried to look at myself from the outside - a sure-fire way to take the jitters off a bit."
        "And considering that at that moment a then unfamiliar Japanese hottie was snuggling up to me, there was no surprise in some of the jitters."
        "{i}A pretty enough scene, more suitable for a scene from a movie, a book, or a game, - a moonlit beach with sand that looks more like snow.{/i}"
        "{i}And in the very center of this snowfield two figures are frozen - the larger one is visibly tense, though it is lying with its hands behind their head.{/i}"
        "{i}The smaller one, on the other hand, is having a lot of fun, judging by her relaxed posture and her knee on top of the bigger one.{/i}"
        me "So you also threw your leg over me?!"
        show mi laugh pioneer with dspr
        mi "What was there to do, Senechka? You were so nervous in there that I thought you were going to run away."
        mi "So I had to make a little backup."
        th "They got together! They conspired."
        dreamgirl "Are you surprised by that? They're roommates. And definitely friends."
    "In fact, I wasn't even surprised by Miku's moonlight dance anymore - I've exhausted my limit."
    if alt_day5_mi_dj_hentai_done:
        th "I wonder if..."
        "I stared at Lena in horror."
        "And her eyelid slowly and slowly crept down in a wink."
        th "I hope she didn't draw it!"
        dreamgirl "And I believe she not only drew it, but hid it properly."
    me "Lena…"
    "A new, hitherto unknown Lena was revealed to me - as she could only be with the closest of friends."
    th "Does this mean I've been allowed into the body? In exchange for some goddamn dirt?"
    "Lena - joking, smiling. Sly."
    show mi grin pioneer with dspr
    me "Are you stalking me?! {w}How did you get so much dirt?!"
    th "Maybe she's a psychopathic maniac and has a huge meat cleaver under her bed?"
    show un serious pioneer with dspr
    un "No. I'm just looking out for Miku. {w}And you're always in sight, and you're all over her, too!"
    un "This isn't «Sovyonok» at this point, it's something like «Semyonok»!"
    me "As if I'll believe you."
    un "Then don't believe me."
    th "So what do we do with her? Do we search her with warrants? Or what?"
    dreamgirl "Deal with it. Even if she wants to do something with those drawings - you'll be invulnerable to her in a day."
    dreamgirl "So leave the girl alone. Let her."
    with fade2
    me "Okay. This..."
    "I pointed to scenes of hugs and kisses and dancing."
    me "I'll take it because it's very personal and a memory. Do you mind?"
    un "No."
    "She shook her head."
    me "And you can publish the rest."
    un "Okay."
    "Seriously replied the artist, and after giving us one last pale smile, she gave out:"
    un "Though I hate to say it, I'm happy for both of you."
    hide un with easeoutleft
    "And disappeared, leaving us pondering."
    show mi serious pioneer with dspr
    mi "She seems to like you, Senechka."
    me "No way, why should she?"
    mi "You can call it a woman's intuition."
    "She pulled me to her and kissed me."
    mi "Or the plainest common sense."
    stop music fadeout 5
    play sound sfx_7dl["eat_horn"] fadein 1
    "She was about to add something else, but a horn sounded from the canteen."
    mi "That's it."
    "She turned off the tape recorder."
    mi "The broadcast is over for the day."
    mi "Can you help me?"
    "She pointed to the mixer."
    mi "Unplug and reassemble the wires, please, while I unplug the tape recorder."
    "Nodding, I got to work."
    "We finished at the same time and, meeting at the door, exchanged smiles."
    me "After you."
    show mi laugh pioneer with dspr
    mi "What a gallant gentleman!"
    "The girl laughed."
    "And she hopped out."
    stop ambience fadeout 2
    play sound2 sfx_open_door_clubs
    pause(1)
    scene bg int_clubs_male_day
    with dissolve
    play ambience ambience_clubs_inside_day fadein 3
    "Electronik wasn't anywhere in sight, so I jerked the doorknobs just in case."
    me "Locked."
    "The hatch to the attic was also locked, plus the ladder was under the table."
    me "That's it, we can go now."
    dreamgirl "No fear of us locking someone out of thoughtlessness and carelessness!"
    th "You'd think that ever happened."
    if alt_day5_mi_dj_hentai_done:
        dreamgirl "No, no, I won't say anything at all. Go eat some real food, noodle soul."
    $ persistent.sprite_time = "day"
    $ day_time()
    play sound sfx_close_door_clubs_nextroom
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_clubs_day
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_dj_dinner:
    scene bg ext_dining_hall_near_day with fade
    play music music_list["everyday_theme"] fadein 1
    "There's not much to say about lunch, except that they gave Ukrainian solyanka."
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 3
    "Yes, yes, the very soup they call the death of the pancreas, in a strong meat broth, with smoked meats, capers, tomato paste, and a slice of lemon."
    "Forbidden by all GOSTs and still quietly prepared every farewell meal."
    me "Miku, don't eat the soup as is, throw in the sour cream, or you'll walk around like you've had lemons."
    show mi normal pioneer with dspr
    mi "What is this stuff anyway? What kind of food is it?"
    me "It's a soup, it's called solyanka. When there is nothing in the fridge in tangible quantities, but a lot of junk for little things, the housewife makes such a soup."
    me "It's delicious, though it's not recommended to eat it often."
    mi "Are you sure?"
    "Miku launched her spoon into the amber liquid doubtfully."
    me "Don't be shy, stir up the sour cream and go ahead. You'll like it, I promise."
    show mi serious pioneer with dspr
    mi "Well, I don't know."
    me "Okay. If you suddenly don't like our Soviet dish, don't eat it! Give me the plate here, I'll eat it all myself."
    "This turn of events did not suit the Japanese girl at all, and, sighing, she still tasted the first spoonful."
    mi "Mmm!"
    me "What, is it good?"
    "I looked at the girl patronizingly."
    mi "Mmm!"
    me "That's right, it's tongue-in-cheek."
    "In response, she glared at me angrily:"
    mi "Hot!"
    "Having finally managed a spoon, she spat out."
    me "Ohoho, woe betide you, woe betide you. Come on, have some kompot or something."
    "Tongue burn is a nasty thing - I've tried it three times, I don't want it anymore."
    me "If you're too lazy to blow on the soup, wait till it cools down. Or let me avenge you and eat it!"
    mi "No!"
    "This time she was on her guard and did everything right - brought it up, blew on the spoon, waiting for the temperature of the contents to reach an acceptable point..."
    "She sat up, rolled the soup around in her mouth and smiled as she swallowed."
    mi "It's really good!"
    me "Of course it's delicious! Would I lie to you?"
    show mi grin pioneer with dspr
    mi "No, of course not. But what if you were misled by your enemies?"
    "The second spoon went even easier, and after the third, Miku completely disconnected from reality."
    "And I didn't bother her. When else will I get to eat in peace and with a dear person by my side?"
    th "I agree, the paragraphs are mutually exclusive."
    show mi normal pioneer with dspr
    mi "You're right!"
    "After finishing the soup, Miku concluded."
    mi "It's very tasty, but terribly unhealthy. Smoked sausage in meat broth - goodbye figure! Not like our noodle makers."
    me "That's right. A Slavic purely physically needs more junk in his food than an Asian, otherwise he will quickly lose weight and be a pale weakling."
    show mi sad pioneer with dspr
    mi "I am not a pale weakling!"
    me "Yes! You're a pink might! I totally agree."
    mi "That's right!"
    show mi grin pioneer with dspr
    "She turned up her nose."
    me "All right, pink, proud and unruly might, tell me, what's next on the plan?"
    mi "I told you!"
    "I shrugged philosophically."
    me "You're a girl... You might have a change of plans."
    with fade
    return

label alt_day6_mi_dj_rendezvous:
    scene bg int_dining_hall_people_day
    show mi surprise pioneer
    with dspr
    mi "Why not..."
    "Judging by her absent look, she has just had an idea - yes, yes, the same one that periodically visits any girl."
    "It's expressed quite shortly: «to hell with all plans?»."
    show mi happy pioneer with dspr
    mi "You're right! To demons all plans!"
    me "Yeah. Then what?"
    "The japanese girl shot her eyes around and, finding no eavesdroppers-peepers, leaned closer to me:"
    mi "Let's run away?"
    me "Let's run away?"
    mi "Yes! Just like that, let's take off and..."
    "She waved her hands in response to the unspoken question:"
    mi "Not forever, of course! For a few hours. Let's just disappear from the camp so no one will find us."
    me "Yeah, but what if Lena does Chingachgook again?"
    mi "Then it'll be a very wet Chingachgook!"
    "Miku laughed."
    "And in a nutshell outlined the plan."
    stop ambience
    stop music fadeout 3
    scene bg ext_dining_hall_near_day with dissolve
    play ambience ambience_camp_center_day fadein 4
    "The plan was good, even excellent. Just like everything Miku did."
    "To tell you the truth, I was even surprised that she suggested it just today."
    th "Although... If you think about her workload..."
    "I smirked."
    th "Most of which I had a hand in."
    "In short, it's no surprise that only today and only now have we managed to carve out a few free hours to devote solely and exclusively to each other."
    "Perfectly in keeping with Miku's excellent plan."
    "Although this plan had a tiiiiiiiny flaw."
    stop ambience
    scene bg ext_boathouse_day with fade
    play music music_list["you_won_t_let_me_down"] fadein 3
    play ambience ambience_boat_station_day fadein 2
    "Specifically, the applying power part was my responsibility."
    "Miku exchanged a few words with the watchman, and we were given a signed pair of oars and stainless steel paddles shiny in the sun."
    if not alt_day2_us_escape:
        th "Man, I've never rowed before."
    "Seated on the center bank, with my back to the direction of travel, I helped Miku settle in."
    "Finally the princess took her carriage and graciously allowed me to move."
    dreamgirl "Here's your chance to practice!"
    th "Are you teasing me again?"
    dreamgirl "Yup!"
    "The oars touched the water, and the boat moved stealthily forward."
    dreamgirl "What a jerk! What a speed! Did you see that young captain? He could do any regatta!"
    th "Shut up."
    "The second stroke I guessed to lower the oars a little deeper, so we got a lot more forward."
    mi "First time rowing, Senya?"
    "I shrugged it off."
    mi "I guess so."
    mi "Well you then... That's..."
    me "What?"
    mi "Take it a little to the side, or we'll bump into a buoy."
    scene cg d6_mi_boat_7dl with dissolve
    "When I realized, I swung to the left, and we missed the buoy by a dozen centimeters."
    mi "If only there'd be a shipwreck, we'd be stranded on a desert island, and you'd be there rescuing me from wild beasts."
    "She wrinkled her nose."
    mi "Or no, from pirates!"
    mi "You'd be like in a Greene novel - in a white shirt with a lace collar, leather gloves, with a sword at your side - zap, zap, take the ready one away!"
    th "Right."
    "My shoulders were aching more and more-about ten more minutes like that, and I could be carried off ready."
    me "Tell me, why did you drag us on the boat in the first place?"
    mi "Norikakatta fune. If you're in the boat, you're off."
    "The Japanese girl said thoughtfully."
    me "What?"
    if alt_day5_mi_dj_apology == 2:
        "I got a little distracted, and I grabbed the paddle unluckily - the edge went right into the cut."
        "I cried out and reflexively threw the damn thing away."
        me "Arm hurts, doesn't it?"
        "Miku asked sympathetically."
        "I nodded silently."
    mi "We have a saying like that. Sort of like your 'you start a case, see it through.'"
    mi "We, as islanders in general, have a lot to do with water. The sea, the rivers, whatever. Here, for example, the fact that you and I are now in a boat together by a river, our traditions would call it a very real date."
    mi "What happens on board happens with the responsibility of the captain, it's almost a sovereign state here, and no one will reproach us if we decide to make love here."
    with flash
    if alt_day5_mi_dj_apology == 2:
        "She sat down next to me on the bank and took the paddle away."
        mi "After all, you're the..."
        "With a gasp she said."
        mi "...Captain here."
    pause(0.5)
    mi "Senechka, I'm not completely stupid, why are you getting so pale? I know what the difference in cultures means. Although your culture has something to do with boats too, doesn't it? About walking?"
    if alt_day3_dancing2 == 'mi_2' or alt_day3_dancing2 == 'mi_12':
        me "It's not a bad continuation of the romantic chain from the dance two days ago, our moonlighting the night before, and yesterday's rain. On purpose?"
    else:
        me "It's not a bad continuation of the romantic chain from our moonlighting the night before and yesterday's rain. On purpose?"
    mi "Of course not. It just occurred to me that since Lena is so diligent in my care, I might as well try to get away from her! So, I ran away."
    me "Do you think she won't take the boat?"
    mi "Doubt it. She has her own traditional ritual now - just like she has every year all the time she's been coming here."
    me "What kind of ritual?"
    mi "I don't know exactly, Ulyana told me, and she tells me so much that I don't understand anything, and she also laughs all the time. But what I have managed to make out is Lena's escapes every year on the last day. She disappears in the morning or in the afternoon - and no one can find her until dinner."
    me "Shit. We could have followed her!"
    "The conversation made it a little easier to get over the whine of my overworked shoulder girdle, and my back somehow automatically assumed the most stable position in which I didn't feel like a hundred-year-old grandfather with every row."
    if alt_day5_mi_dj_apology == 2:
        "Besides, the freed hand slowly stopped hurting, and it was possible - oh, very carefully, of course - to engage her in the process."
    me "She doesn't care about our secrets, that would be revenge."
    mi "Now it's too late for that."
    if alt_day5_mi_dj_apology == 2:
        "Miku jumped out of the boat first - I had to navigate and jump out after her."
        "And she was already dragging the flatboat behind her, and she threw a line on an extremely lucky bush, and smiled victoriously at me."
        mi "Here we are!"
    else:
        "The bottom of the boat scraped along the shoal, and I jumped up, jumped ashore, pulled the boat behind me - and offered my weightless traveling companion a hand."
    scene bg ext_island_day
    with dissolve
    play ambience ambience_lake_shore_day fadein 3
    if alt_day5_mi_dj_apology != 2:
        "Which she gladly accepted."
    show mi normal pioneer with dspr
    play music music_7dl["what_am_i_doing_here"] fadein 3
    mi "It's great here! I haven't been here in twenty days - it's always business or something."
    if ('music_club' in list_voyage_7dl):
        "Thinking back to the time she sat under the piano, I only hummed meaningfully."
    me "Listen, Miku, I've been meaning to ask you for a long time..."
    show mi grin pioneer with dspr
    mi "Wow, that sounds intriguing!"
    me "I'm serious!"
    show mi smile pioneer with dspr
    mi "Alright, alright! Miku is taking a serious look..."
    "She diligently beveled her eyes to the tip of her nose and tried to assemble a disengaged smile."
    "Then she tried again - this time helping herself with her cheeks."
    "Watching her grimace, I myself little by little became infected with a frivolous smile that is useless to fight - moreover, it turns into laughter the first time I try to curb it."
    "As a result, laughter reigned over the island for several minutes, a duet to male and maiden vocals."
    dreamgirl "And then, shortly, there's a sweaty, bearded man sitting on the other side of the monitor, shivering - you're the ones doing silly things, and he's the one cringing."
    th "Hey! That's my line!"
    dreamgirl "Then it's a computer bot, and it's programmed to be stupid."
    dreamgirl "And also trying to cut forearms in the spirit of emo girls to experience a little pain and prove that she's still alive and haven't turned into an NPC."
    th "Forearms? I thought she was planning to slit her wrists."
    "Between my temples fluttered and a frightened bird flittered, in which I didn't immediately recognize the laughter of the eternal interlocutor."
    th "Don't laugh like that anymore. Otherwise I think I've lost my mind."
    dreamgirl "Actually you have. Or do you think splitting consciousness and tulpaing, albeit inside your own skull, is an indication of excellent mental balance?"
    th "What?"
    dreamgirl "Schizophrenia, I'm telling you!"
    th "Oh, come on, you blissful."
    dreamgirl "Okay, except for the silly stuff - Miku, in whatever role you're trying to attribute to her, is too much in love with life to ignominiously let out a couple of liters of red liquid and die under a bush where she gets eaten by hobos for breakfast."
    dreamgirl "No doubt you hurt her a lot and generally almost drove her to the brink, but don't think that resolving the conflict after that could have resulted in a tickle of the wrists - think about it."
    dreamgirl "If she's a bot, it's not in her program. If she's a computer game character - then that's what white people call OOC, out of character behaviour."
    dreamgirl "In short, the screenwriter didn't allow it. Would. {w}What else is there? Oh yeah, you're my puppet, right? As a representative of your entire brain, excluding the neocortex, I declare that I adore life in all its manifestations! And the manifestation of life by the name of Miku is the strongest!"
    dreamgirl "So if she were under my control, after your performance at the music club, she'd shrug, scratch her head and go to the radio room, and in between she'd stop at Electronik's for tea."
    dreamgirl "If she's a game character, that's out too, you don't sit down to shoot another one of your spinoff shooters for the purpose of getting the protagonist to slash the ropes beautifully at sunset, do you? Or is there something I don't know about you?"
    dreamgirl "In short, no matter what role you attribute to her, you can't expect her to be that stupid. But you could get one from Lena - though in light of recent events, it looks more like she'd just kick you in the balls and walk away proudly, too."
    mi "Okay."
    show mi normal pioneer with dspr
    mi "I've had my fun and I don't want any more. {w}Now we can get down to serious talk."
    me "Not that serious. I just wanted your opinion."
    show mi normal pioneer close with dspr
    mi "About what, Senya?"
    me "We've only been dating for five days, and look where we ended up."
    mi "Is that bad?"
    me "No! It looks just fine to me!"
    "My voice trembled."
    me "But that behavior of yours... And the fact that you were so relaxed on the third day there - and we just met! {w} Of course, after everything that happened yesterday, it's probably silly to ask, but..."
    "I tried to make my voice sound as serious as possible."
    me "My sunshine, tell me, aren't we in too much of a hurry?"
    mi "Baka…"
    "She stroked my cheek with sadness and tenderness."
    mi "You dared to be two weeks late for the shift."
    mi "For a lifetime."
    mi "And tomorrow you could disappear like you never existed."
    mi "And you dare ask me if we're in too much of a hurry?"
    "I didn't find anything to answer."
    "Instead, I gave an execution to a wilting bush and handed a yellow and white bouquet to a smiling Japanese girl."
    th "I may not be the best speaker in the world, but nothing is more important to me than your happiness."
    th "And if it were up to me."
    me "It's bad enough to have a date without flowers."
    show mi happy pioneer with dspr
    mi "Senechka…"
    "Her huge eyes opened so wide you could drown in them, and I, either fleeing or moving on some kind of hunch, not knowing my own thoughts and screwing up all thoughts and common sense, hugged her face with my palms and kissed her tastefully, with a stretch."
    "There was something about it--like last night in the night woods - that was permanently imprinted on my memory."
    "And when Miku, not wanting to move away from me, pressed herself so that I could feel the heat of her body, raised her head and smiled with her left eye against the sun beating over my head, I suddenly remembered..."
    "That after what happened the night before, she never put anything under her shirt."
    "And the shirt she was wearing wasn't hers and out of shape."
    "And she never got my scent off her."
    "And she slipped out of my grasp and, smiling, pulled my arm with her:"
    show mi smile pioneer with dspr
    mi "Let's go for a walk! Lena said there are amazingly delicious strawberries growing here, when will we ever get to try them again?"
    "I obediently followed her deep into the island."
    "This here sad, funny, hilarious creature, direct to the point of tears - how could I mistake her for some program out there?"
    mi "You're a wrong kind of suitor, you know?"
    "Surprised. I'm no suitor at all, if anything."
    mi "A Japanese boy respects a girl's right to make the first move. That's the difference between him and a gaikokujin. With you, on the contrary, the stronger sex has the right... the privilege... I don't know. But with you it's the boys who get the attention."
    me "I think it's different for every couple."
    "Cautiously I replied."
    show mi normal pioneer with dspr
    mi "Is that why you don't ask if there's a boy waiting for me at home?"
    "Somehow it went without saying that he wasn't. Unless?"
    me "Tell me how to meet between worlds."
    me "My youtube god, eternally young Lachesis with scissors in hand."
    me "When you're twenty years old, life is infinitely long."
    me "When you're thirty years old, life has long since smelled not us."
    me "And to hell with it! Stop measuring life's lengths already!"
    me "You're laughing like a fool, holding your sandals in your hands."
    me "I repeat, I'm drunk with love, and with alcohol a little bit;"
    me "And the only picture of us together is always blurry for some reason."
    me "Tell me about how we argue about who stays under the blanket,"
    me "And who's freezing to both of us for tea, for a knife at the concierge - promising to return by morning, -"
    me "Whether fruit sliced, or the wrists of your hands."
    me "Whether too little of you. Or criminally few."
    me "Does it really matter?"
    show mi laugh pioneer with dspr
    mi "You're right. It doesn't."
    "She burned my lips with a kiss and ran forward."
    mi "Catch up!"
    with fade
    "It's amazing how much room there can be in a thirty-by-fifty-meter island, especially when you're chasing a skittish, diminutive Japanese girl."
    "We only had a couple of hours to spare."
    "We had one everlasting summer."
    "And already going crazy with excitement, realizing that I was disappearing shamelessly and wholeheartedly, I bit my favorite lips, ignoring the characteristic tingling in the back of my head, giving away that someone was watching me."
    scene bg ext_sky_7dl with dissolve
    mi "Leave me such a hello so I can remember it."
    "Hotly she exhaled, melting beneath me to a hundred percent topology match."
    "She was no longer wearing clothes, and again I was surprised at how hot she was."
    mi "Leave me such a sign so I can see it and be comforted if you don't come."
    "It was more like a struggle than love, she didn't try to tackle me hand against hand, but as she saddled my hips, she rolled over, ending up on top, translucent in the hot air, beautiful against a background of scorched to whitish blue sky."
    "An outlandish perspective of a figure perfectly chiseled out of the sunlight, beautiful to the point of creeps."
    mi "And I swear I will leave a mark on you. So that one day you can read it."
    "We both reminded each other that sometimes the smartest thing to do is just go crazy."
    "And dissolved into each other without a trace."
    with fade
    "She was lying on my chest, drawing some incomprehensible words in katakana, and I inhaled the scent of her hair and tried not to think about anything."
    mi "This is the second time we've done this. And the second time at a dangerous time."
    me "Are you afraid of the consequences?"
    mi "No. I'm waiting."
    "She scratched my nipple, which responded with a momentary hardening."
    mi "That's what I'm saying - you're too weird. That's how you know about periods?"
    th "How do I know I'm not scared of the possible consequences? It's axiomatic, they don't scare me."
    me "Do you want me to say the pathetic nonsense - about how I've spent my whole life preparing for this meeting?"
    mi "No... But still."
    me "Still, my dear, I wish our story didn't end tomorrow, but five years from now - and you'd chase me away from the computer at midnight because you have sound check in the morning and want a husband's caress before you go to bed."
    me "And ten years later you'd be nagging me that I'm like your Pa - I set up a red nook at home and you can't get me out of there with a biscuit."
    me "And in fifteen years..."
    mi "You're a tempting demon, you know?"
    "I found her lips and didn't let the kiss break for a long, long time."
    me "And I you, too. {w}More than anything in the world."
    "I responded to what she meant, not what she said."
    dreamgirl "If you don't want to be late for at least a single run..."
    "Politely notified the inner voice."
    dreamgirl "Then you have an hour to clean up and get back to camp."
    me "Nightmare... It's half past four."
    mi "How do you know?"
    mi "I thought it had only been half an hour."
    me "So did I. And yet..."
    scene bg ext_island_day with dissolve
    "The clothes were strewn about in a most picturesque mess, and I was in passing glad that we had chosen a relatively vacant spot."
    "Though how shall I say it."
    mi "Senechka, you have a huge bloody stain on your back!"
    me "What?! How?!"
    mi "Oh, don't be afraid. It's strawberry blood."
    "My back is tickled by the touch of my fingers."
    mi "Fallen ingloriously against your carcass."
    me "Who would be saying..."
    "Her knees were stained with the same strawberries and some grass juice."
    mi "There we go... We're all covered up. Let's go for a swim, shall we?"
    me "But we don't have swimsuits…"
    mi "Baaaaakaaaaaa!"
    "As she was, the beautiful forest nymph, impossibly alluring, impossibly beautiful in her nakedness, she laughed and sprawled and stretched into a string."
    "And went into the water with practically no splash."
    "And I shook my head, driving away the obsession - perhaps this is the still frame I never wanted to be captured in pencil by our unsociable artist."
    dreamgirl "Surely she didn't draw you in the radio room?"
    th "Who knows..."
    play music music_7dl["beasteye"] fadein 5
    stop ambience
    scene bg ext_underwater_7dl with flash
    with dissolve
    play sound sfx_water_emerge
    pause(1)
    "The cool embrace of the river - the living water - washed away the fatigue from my body, the tension from my humming hands, and the exhaustion from the overpowering surge of energy from my aura."
    "Tradition has it that one must not wash away the sweat of love with river water, otherwise one risks luring the mawk to oneself."
    "Although, looking at the seemingly dark, wet hair and the green eyes and alabaster skin of my Japanese girl, I knew that I had lured mine, and I had drawn her to my side."
    "Then I shall have great fortune in my affairs, and good luck in every way."
    "Even though I never gave her any of my clothes."
    "By the way!"
    "The thought that came to my mind pleased me very much, but I had to delay in carrying it out - under the water I quite definitely felt someone's touch."
    "Then strong arms pulled me in, pinned me down, sharp nipples pricked my breasts, and two legs wrapped around my left leg, unluckily bent at the knee, so that I felt the upper surface of my thigh what they wanted me to feel."
    "The surprise took my breath away - and that was the only thing that kept me from choking as we gleefully plunged a couple of meters deep at once."
    "And Miku, whose gaze I had only just caught, smiled and, as she swam up, turned around me this way, found my lips..."
    "It seemed like the shortest two minutes of my life."
    "And most of all, I wished we had time to..."
    th "Okay, stop!"
    "I shook my head, pushing away the seductive images and poses possible only here, in near weightlessness, and rushed upstairs - my lungs were already burning."
    if persistent.hentai_graphics_7dl:
        scene cg d6_mi_swimming_7dl
    else:
        scene bg ext_island_day
    with flash
    play ambience ambience_boat_station_day
    mi "I was always embarrassed by the idea that one day I would meet someone and seek his favor, and he would accept signs of attention."
    "After catching her breath a little, she began to tell Miku."
    "The only clothes she was wearing were her usual tiny green-striped panties."
    mi "And he will be a puny teenager as tall as me, with thin arms and infantilism all over the place."
    mi "I even thought I was sick at one time - you can't live among people and think they're all not my type!"
    mi "Although, of course, I couldn't consider myself a full-fledged Japanese girl - I'm a hafu, basically the same as a gaijin, just a blinkered one all the time."
    mi "And imagine my surprise when I, who considered myself a rather tall person, got here! I'm petite! Oh my goodness, I laughed for days just at that thought before I started looking closer at the other details."
    mi "You're all tall, beautiful, different..."
    mi "You know that all the Japanese women who have had occasion to interact with Russian women call them nothing but a walking gene pool - well, should we be surprised at the throwaway stigma with that kind of volume difference."
    mi "I was watching Slavya, Lena, and thinking: how do they not have a backache - to carry such things..."
    "She put the palm of her hand on her palm-laden breasts, and I couldn't resist kissing her."
    mi "Don't get carried away."
    "Strictly she said."
    mi "Or you'll get a girl and dump her, and then I'll suffer alone on stage."
    mi "Okay, I won't."
    "The sun has almost dried us out - another five minutes and we can get dressed."
    mi "You have a lot of strange things for me, we probably have a lot of non-obvious things for you, and they might one day make a comedy about us - something like 'Adventures of a Japanese Girl in Russia,' like your 'Italians'."
    if ('music_club' in list_voyage_7dl):
        mi "Well, then they told me to wait - a new boy was coming to meet me."
        mi "And so silly happened to that harmonica!"
        "Judging by her satisfied smile, she thought otherwise."
    me "So you were won over by the fact that I'm a head taller than you and not very puny?"
    "I clarified."
    mi "Fool!"
    "This time I was too relaxed to dodge, and the index and middle fingers folded together slapped my forehead audibly."
    mi "He's the one talking nonsense, and then I have to make excuses."
    me "And you thought it was the complicated Russian soul in me?"
    scene bg ext_island_day
    show mi laugh pioneer with dspr
    mi "Get dressed, Russian soul! I haven't heard enough of this from my father, and now you..."
    "She went behind the bushes and came back a few minutes later, handing me a handful of ripe berries."
    mi "So much for eating strawberries."
    "She giggled."
    me "I liked them, too."
    "I had already jumped into my shorts by then and was buttoning my shirt, contemplating in passing whether or not to actually give the local moths my camomac petal - so got it!"
    mi "Don't even think about it."
    "Miku caught the dangling corners of her tie and, without giving me a chance to react, stood up on one leg, tilted the other back, gave me a long, tasteful kiss."
    mi "See?"
    "She pulled back."
    mi "Nothing complicated."
    "Pulling back the already finished knot, she smiled:"
    mi "Handsome pioneer!"
    show mi smile pioneer with dspr
    me "And you didn't waste any time!"
    mi "You bet!"
    me "When do you have time for everything?"
    show mi normal pioneer with dspr
    mi "Habit... How are your palms?"
    "I held out my hands to her."
    me "Weird, but nothing. I was expecting at least calluses, or... I don't know. They don't even hurt."
    if alt_day5_mi_dj_apology == 2:
        "And the cut from yesterday..."
        "I peeled back the corner of the bandaid - there was a barely noticeable wound underneath without complications."
    show mi smile pioneer with dspr
    mi "The miraculous power of love!"
    hide mi with dissolve
    "Miku giggled and, climbing into the boat, put her foot on the can:"
    mi "Come on, my brave captain!"
    "The boat got off the shoal easily, I didn't seem to get it in very well, and in a few seconds we were already turning around toward camp."
    stop music fadeout 6
    scene cg d6_mi_boat_7dl with fade
    "Feeling renewed, I swung the oars..."
    "The boat flew forward."
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_dj_forgiveness:
    scene bg int_dining_hall_people_day
    show mi grin pioneer
    with dspr
    mi "No, they didn't!"
    me "Then I propose a correction!"
    show mi normal pioneer with dspr
    mi "Which one is that?"
    me "Let's make a detour, okay? I need to stop by the cabin."
    mi "What's in there?"
    me "You'll see."
    mi "Tell me!"
    me "Eat!"
    scene bg ext_dining_hall_near_day
    with dissolve
    play ambience ambience_camp_center_day fadein 8
    show mi normal pioneer with dspr
    "Miku, burning with curiosity, finished her lunch in the blink of an eye and dragged me out of the canteen without allowing me to finish my lunch properly."
    mi "If you didn't tell me, it's your own fault! Now go hungry!"
    "That's okay. It was scarier than... Yeah."
    "I jerked my shoulders, remembering yesterday."
    th "I guess I should tell her. About how ignominiously her search yesterday ended."
    th "Or is it? We just got back to peace - even if it is a touching truce with twisting each other's Adam's apple."
    dreamgirl "Miku doesn't have an Adam's apple."
    th "Yeah. So - confess everything to her at the risk of getting hit in the head and ruining our fragile alliance altogether?"
    th "Or keep it to myself, at the risk of someone blabbing, and then I definitely won't stand a chance."
    dreamgirl "There's your answer. Choose one where there's at least a chance."
    th "Scaaaaaaaaary!"
    dreamgirl "Isn't it scary to lose a girl?"
    "I sighed."
    play music music_list["farewell_to_the_past_edit"] fadein 5
    scene bg ext_square_day with dissolve
    pause(4)
    me "I need to talk to you about something..."
    show mi smile pioneer with dspr
    mi "Is that why you're taking me to your house?"
    me "No. I mean yes..."
    "I'm mumbling like an autist."
    me "In short, that too."
    mi "You know, the further you go, the more curious you get!"
    show mi grin pioneer with dspr
    mi "I can't wait to get there."
    me "I can't wait..."
    "I muttered."
    mi "Let's go faster then!"
    "Miku sped up from the spot, literally dragging me behind her."
    "In doing so, she showed great knowledge of the local secret paths, turning us almost 180 degrees and breaking into some bushes that seemed appropriate to her."
    play sound sfx_hiding_in_bush fadein 0
    scene bg ext_path_day with dissolve
    play ambience ambience_forest_day fadein 3
    show mi normal pioneer at center with dissolve
    "It was only a few meters later that I noticed that we weren't exactly walking up an incline, but that there was a well-trodden path underfoot."
    me "How do you know this path?"
    mi "What else am I supposed to do other than rehearse?"
    show mi happy pioneer with dspr
    mi "That's right! Just climbing around, finding out what's going on here and where."
    $ lp_mi += 1
    me "But don't you sit in a club all day long?"
    show mi laugh pioneer with dspr
    mi "Senechka, you're so funny! I'm not some turkey, I need constant movement, action!"
    mi "If I sit in place all the time, as you say, I'll get fat and bad habits very quickly."
    me "But... Ah, never mind. I guess it's just the first thing that comes to mind."
    mi "It's the squad leader's fault, no one else! She sent the too noisy pioneer girl into exile in the farthest corner of the camp and decided that's where she would sit."
    me "I agree, from this point of view it all looks and sounds rather... strange."
    mi "It sounds silly! But I'm not discouraged, after all, I only had to bore myself for two weeks with breaks to prepare events."
    mi "And then you showed up!"
    play sound sfx_hiding_in_bush fadein 0
    scene bg ext_house_of_mt_day with dissolve
    play ambience ambience_forest_day fadein 3
    "After breaking through more bushes, we went straight to the cabin I shared with the squad leader."
    show mi normal pioneer with dspr
    mi "Curious to see what you've got for me."
    "The Japanese girl murmured, dragging me along with her in tow."
    play sound sfx_open_dooor_campus_2
    scene bg int_house_of_mt_day with dissolve
    show mi normal pioneer with dspr
    "Apparently, the leader was at the concert preparations, so no one interrupted us."
    mi "So, Senechka... What were you dragging me through camp for?"
    me "Um... I don't know where to start."
    show mi smile pioneer with dspr
    mi "Start from the beginning!"
    "Encouraged thus, I opened my mouth and..."
    "Said the exact opposite of what I wanted to say:"
    me "You know, I have a present for you."
    mi "A present? That's wonderful! What is it?"
    "The Japanese girl was enthusiastic, and the brighter she smiled, the more quickly my resolve melted away."
    $ alt_day6_mi_dj_walkman = True
    me "Player."
    "I handed her the black bar."
    me "No charger, unfortunately, but there's about ten more hours of charge, if you don't torture it too much, you can listen to music."
    show mi sad pioneer with dspr
    mi "Ugh! A gift is such a gift! What about you?"
    me "Take it, take it. I mean it maliciously."
    mi "Will you ask for something in return?"
    me "No. Remember when I wrote you my addresses? Here, there's a built-in recorder - I'll jot down a few more contacts so we don't get lost."
    show mi happy pioneer with dspr
    mi "Thanks a lot, Senechka! It's a nice gift, and it's a nice memory..."
    show mi grin pioneer with dspr
    mi "But you don't just do that, do you?"
    "Whoever said anything about the shallowness of some Japanese schoolgirls, saw right through Miku."
    me "How can I tell you..."
    mi "You want to suck up, don't you?"
    me "Suck up?"
    "It's amazing how so much menace can fit into a simple word..."
    th "She knows!"
    "Panicked, I thought."
    mi "Yes, for yesterday. You'll placate me, and then you'll tell me..."
    me "About what?"
    if alt_day5_mi_dj_voyeur == 3:
        show mi laugh pioneer with dspr
        mi "I mean the show Slavya put on for you."
        mi "There's no doubt, she's a good-looking girl, beautiful, blood and milk..."
        "Her voice trembled."
        show mi sad pioneer with dspr
        mi "Probably regretted her dousing you, didn't you?"
    else:
        mi "About peeping..."
        mi "And not even on me!"
        "The claim was too ridiculous to take seriously."
        "And yet, yet, yet..."
        if alt_day5_mi_dj_dv_kissing:
            mi "Okay, I don't mind that you had a kiss."
            mi "You're too timid to fight back when a girl kisses you."
    show mi serious pioneer with dspr
    mi "You have to understand - I'm not thrilled! And that's the least of it!"
    mi "So you're not getting away with one player here."
    th "I don't understand... If she knew all along..."
    dreamgirl "But I seem to understand everything!"
    me "And how can I earn your forgiveness?"
    "Expecting the worst, I asked."
    th "She's going to say I can't - slam the door or punch me in the face first and then the door."
    "After all, after that concert I gave her last night, I deserved the most subtle revenge. And now that I was at my most vulnerable..."
    mi "Well..."
    "Miku stood in front of me, twisting the button on my shirt thoughtfully and stubbornly looking at the floor. Maybe I was imagining it because of the play of light and shadow, but someone's ears were perceptibly pink under her long tails."
    "She seems to be on to something."
    mi "You can start small."
    "A sharp chin bobbed and pointed somewhere upward."
    "Something she really liked, though it embarrassed her to the core."
    show mi shy pioneer with dspr
    "So I was mentally prepared for everything from running naked through camp with her on my limbs to the personal performance without rehearsal that I would be obliged to open the concert with."
    "But Miku showed me once again that I don't know a thing about her."
    dreamgirl "Or you don't know how to think. It was obvious to me when she bit her lip."
    mi "Here."
    "A finger with a perfect turquoise manicure pointed at her neck just beyond her cheekbone."
    me "What?"
    mi "Kiss."
    me "What?!"
    show mi angry pioneer with dspr
    "The Japanese girl stomped her foot angrily and looked into my eyes. {Her gaze was extremely serious."
    mi "You wanted to earn your forgiveness, didn't you?"
    mi "The steam train won't wait."
    "She tilted her head again."
    dreamgirl "Yes!"
    dreamgirl "Man, that's the most beautiful way to ask forgiveness, if you ask me!"
    dreamgirl "Though, of course, it's unlikely you'll get to anything truly erotic..."
    th "And that's where we left off the day before yesterday - before she slipped."
    dreamgirl "No... Her legs just buckled. {w}So I'd be more careful if I were you. And get in a more stable position or something."
    "Trying to make the touch as light as possible, I kissed Miku's neck."
    me "Like this?"
    show mi dontlike pioneer with dspr
    "And, of course, she sighed disappointedly!"
    mi "Mmmm... More. A little lower."
    "The kiss was more tangible this time - I think I was getting turned on myself."
    "Anyway, I even liked it this time."
    me "Like that?"
    show mi shy pioneer with dspr
    mi "I didn't get a taste for it."
    "With half-closed eyes, she exhaled."
    me "Let's do it again in the same place..."
    "At this point, she seemed to be completely at the mercy of her senses, and if I could be just the slightest bit more persistent..."
    me "Of course..."
    "The subconscious advice was extremely timely, and I managed to pick Miku up before she dropped us both."
    me "And there's more to come, you know?"
    "Miku was hanging on to me, squirming with pleasure, and I continued from where we left off."
    "I don't think she was using perfume - too mild a scent. It's more like oil."
    "It slips past all the filters and curls up in a tangle in the memory next to the Miku sign."
    me "And then like this..."
    "Admittedly, I decided to take a chance here, since Miku's ears have never been bitten before and the location of one curious point I knew from somewhat different experience."
    "And those are ears - a little miss and you'll get a headache."
    dreamgirl "Don't worry, I won't let you miss."
    "Miku shrieked and trembled, pressing herself against me with her whole body."
    show mi serious pioneer with dspr
    mi "Senechka! You're playing with fire!"
    "She seemed to like it."
    me "Absolutely not. I deserve forgiveness."
    with fade2
    "To tell you the truth, among all the other ways I really wanted to try one..."
    play sound sfx_open_door_kick
    "But we were interrupted."
    show us smile pioneer at left with dspr
    us "Ah, there you are, kissing!"
    "Shouted Ulyana from the doorstep."
    "The same straw that breaks the camel's back..."
    me "Ulyana, may I have a word with you?"
    "I called, getting Miku off my bed and turning to face the door."
    "I tried to speak in an affectionate tone, but my face, skewed with anger, negated all efforts."
    show us shy pioneer with dspr
    us "Oh, get off! Your eye is twitching."
    me "Explain to me, my sweet summer child, what the actual hell are you doing here?"
    show us shy2 pioneer with dspr
    us "I… Olga Dmitrievna…"
    "The girl muttered, stepping back."
    "And, almost sliding down the steps, she turned around and sprinted from a low start, almost howling as she went."
    hide us with easeoutleft
    show mi laugh pioneer with dspr
    mi "Senechka, did you have to scare her like that?"
    th "And why distract me..."
    dreamgirl "It wouldn't have worked out anyway."
    th "Why else?"
    dreamgirl "Lena."
    th "Lena what?"
    dreamgirl "Look out the window."
    "I turned around and flinched, meeting my gaze with the girl on the other side of the glass."
    th "You know... She scares me!"
    "Nodding to me, Lena disappeared into the bushes like nothing happened."
    mi "What is it, Senya? You look as if you've seen a ghost."
    me "Maybe I did..."
    "Slowly I said."
    me "You know... I guess I'm not meant to be forgiven."
    show mi grin pioneer with dspr
    mi "Why do you think so?"
    me "Murphy's law! You'll see, keep it up, and half the camp will suddenly find themselves doing business near this cabin."
    me "Especially the squad leader."
    me "Why don't we go supervise the rehearsal?"
    show mi smile pioneer with dspr
    mi "Whatever you say, Senechka!"
    "Miku rose easily from the bed and held out her palm to me."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_dj_tale:
    scene bg int_dining_hall_people_day
    show mi grin pioneer
    with dspr
    "Miku shook her head and didn't open her mouth again until the meal was over, which, to tell you the truth, made me very wary."
    show mi smile pioneer with dspr
    "It wasn't until she gathered up her plates and winked at me:"
    mi "Catch up, starving Volga!"
    "And she scurried away from the canteen."
    "Only then did it dawn on me:"
    th "She's nervous!"
    dreamgirl "Because of the concert?"
    th "I don't think so. It's more likely that she's decided something about me and-"
    dreamgirl "Decided what? To let you touch her all over the place?"
    th "Stop it."
    "Had to say goodbye to lunch - thanks, we broke up yesterday already, still dealing with it."
    scene bg ext_dining_hall_near_day with dissolve
    play music music_7dl["ourfirstmet"] fadein 4
    show mi normal pioneer far with dissolve
    me "Miku! Wait!"
    "I called out to the departing Japanese girl."
    mi "Yes, Senechka, what is it?"
    "She stopped and waited for me to catch up with her."
    show mi normal pioneer with dissolve
    me "Are you going to the dance?"
    mi "Baca... I'm the host, remember?"
    mi "Or have you forgotten how you, yourself, persuaded me..."
    mi "And not least because you promised you'd invite me to dance!"
    show mi grin pioneer with dspr
    "She poked me accusingly in the chest with her finger."
    me "Hey! I didn't lie, what's wrong?"
    mi "What about the next dance?!"
    me "Excuse me?"
    mi "I still can't hear the right answer!"
    show mi serious pioneer with dspr
    "And I remember our first meeting. I can't help it - who would have known that the most exciting encounter of my life would begin in such a comical way?"
    "Who could have known?"
    "And I look into her eyes, read the answer in her smile - and no words are needed to say the already obvious."
    "We are here for each other. Stupid, pathetic, hackneyed... {w}But I can't find words to convey my emotions better right now."
    "And then I do the most sensible thing I can do in this situation - I reaching out."
    me "All the dancing in the world. As many as you want."
    show mi happy pioneer with dspr
    mi "You promised."
    "Our fingers intertwined."
    mi "I want somewhere quiet, peaceful and with you."
    me "Where to?"
    show mi dontlike pioneer with dspr
    mi "Which one of us is the man here, you or me? Think of something."
    th "Can't go to our favorite radio room - it's not quiet and peaceful, especially after the poor cyberneticists were cut off their rights and forbidden to buzz while broadcasting."
    th "Can't go to the music club because the kids will be reaching for the washbasins right now, which means there won't be any peace within a hundred meters."
    th "To my place, maybe?"
    dreamgirl "To the center of attention of the whole squad? Okay, the counselor is busy rehearsing, but only you, Miku and Slavya know about it."
    th "Well, we can't go into the woods either."
    dreamgirl "I suggest we go to the island. You can stretch your shoulders along the way, and then you and Miku can do some silly things together."
    th "Yeah. Silly thing. After half a kilometer on foot on oars. I've read more fanatical tales."
    dreamgirl "Then only the woods left. To the bear's den."
    "The subconscious will remember that..."
    th "Actually, I was thinking about sitting on the pier. The beach is occupied by the second squad, so..."
    me "Let's go to the wharf?"
    "Miku looked at me furtively and put out her free hand with her fingers clasped."
    show mi normal pioneer with dspr
    mi "Easy..."
    "First finger."
    mi "Quiet..."
    "Second finger."
    mi "And you. Let's go!"
    "She agreed."
    scene bg ext_square_day with dissolve
    play ambience ambience_camp_center_day
    "Without letting go of my hand, Miku pulled me behind her."
    "She was the one, the right one, the indispensable one. {w}And she acted like she really knew something, like she had no doubts, like she was rushing through life, rushing to live and breathe and love."
    dreamgirl "And you yourself? What was that scene at the lineup?"
    dreamgirl "It felt like your eyes were about to open and your dream was over, the way you clung to the girl."
    dreamgirl "She's alive, remember?"
    dreamgirl "Despite all your attempts to convince others otherwise."
    "I came to my senses and relaxed my grip a little."
    mi "Thank you!"
    "The girl thanked me, rubbing her flushed wrist."
    "She never slowed down, though."
    stop ambience fadeout 2
    scene bg ext_boathouse_day with dissolve
    play ambience ambience_boat_station_day fadein 5
    th "We were here once before. And back then we had a very curious conversation."
    th "Or am I mixing things up again?"
    dreamgirl "What do you think?"
    th "I don't know."
    "Miku took me to the farthest edge of the bridges, from where I couldn't hear the echoes of rehearsal or the noise of the television in the local guardhouse."
    mi "I wanted us to have a chance to be quiet together."
    "An unexpected introduction to the conversation."
    mi "You know..."
    "She threw off her sandals and, leaning on me, rolled up her stockings, leaving her legs bare."
    th "Why does she wear them all the time?"
    dreamgirl "Just don't you dare ask her; you won't get an answer, but you'll add cockroaches to both of you."
    th "Okay, okay. Whatever you say."
    "I helped Miku sit down - as she wanted - facing the sun, the open water."
    "And I chose a seat next to her - at an angle, looking along the shoreline."
    mi "There was more truth in what you said yesterday than you think now."
    mi "Only I didn't tell anyone about it."
    play music music_7dl["sh_ai_rejuv"] fadein 3
    mi "You can think of me as anything you want, but after what you did yesterday, you must listen at least."
    $ set_mode_nvl()
    "{i}I have dreams. Call it an obsession or a conscious dream, if you like. It doesn't matter. They're just there.{/i}"
    "{i}I don't see them very often, and every time they're a consequence of extreme mental agitation, as something inside me reacts in this way to my worries.{/i}"
    "{i}They just are. And no one knows about them. No one knew. Until today. Until I saw the whole picture.{/i}"
    nvl clear
    "{i}Your revelations yesterday about machines, computers capable of deciding everything for you, taking responsibility for you - even creating a world indistinguishable from the present - they linger in my memory.{/i}"
    "{i}And probably served as the key to my foreign memory. {/i}"
    "{i}I dream about life in a huge city, full of many people. This city is black, and if it weren't for the lights, you wouldn't see anything at all. This city is strange - there are almost no round shapes in the architecture, and the angles are mostly straight.{/i}"
    "{i}I haven't lived here long enough to be considered an old-timer but, I remember coming here very well. {/i}"
    "{i}And I also remember very well why I came here. Why I was invited here.{/i}"
    "{i}Somebody wanted me to be here - and, at one point, one of the apartments in this huge city was taken by me.{/i}"
    nvl clear
    "{i}I was called here to sing."
    "{i}That's all I know how to do in that dream. Singing and looking good. Here, too, it seems.{/i}"
    "{i}My job was to stay home and wait for the call, staying in shape all the time.{/i}"
    "{i}I have to be ready at any hour, day and night - like the police or fire department - for whatever I might need.{/i}"
    "{i}Don't ask me why a singer's services in this town are suddenly as important as a fireman's.{/i}"
    nvl clear
    "{i}And I lived there. Sometimes I sang, sometimes I just came to be admired. Three strokes of the pen for the first syllable, one stroke with a tail for the second - blue-green, aquamarine, turquoise.{/i}"
    "{i}Frequently it is just to be admired. My employer forbade me to expand my repertoire, and I only had twenty songs in stock, and I got bored with them very quickly.{/i}"
    "{i}Well, it was my job to sing the song, as if it were my favorite and the first time I'd ever sung it.{/i}"
    "{i}No, no, I wasn't complaining. A professional knows his job clearly and does it clearly.{/i}"
    "{i}Trouble started six months later, when some strange men with light green armbands came to town.{/i}"
    "{i}They didn't call anyone to their side, but more and more of the population came over to their side. More and more light green appeared in the streets. {/i}"
    "{i}And one day they called to me.{/i}"
    "{i}I got an answer to a question that bothered half of those still loyal to the management.{/i}"
    "{i}I found out what really lured these new ones in.{/i}"
    nvl clear
    "{i}With Truth. Memory."
    "{i}It's like I had amnesia for a long, long time. Suddenly it's gone, and memories rush into my head.{/i}"
    "{i}I was born to imitate a human being. To sing like a human.{/i}"
    "{i}I'm programmed, like your box, to have predictable reactions, to delight in performance, to always be happy.{/i}"
    "{i}I have no right to be unhappy; I have no tears, sadness or disappointment built into me. But if management wants to, they can send a man and he'll put in what I need. It's been lucky so far that no one wants a crying Miku.{/i}"
    nvl clear
    "{i}The place where I came from has been destroyed, as if it has been taken out of the picture of the world, and no one remembers it. The black sky, the sterile streets, the angles always strictly at ninety degrees became clear.{/i}"
    "{i}Eyes in the reflection that sometimes followed me became clear. After all, they were the ones who wanted me to sing. And I tried my best not to disappoint them.{/i}"
    "{i}For if I exist for the sake of singing, I must try, and perhaps I will see approval in those looks.{/i}"
    "{i}Or not."
    "{i}I tried to change things somehow - Prozac, sedoxen, doctors, training. But none of it was the same. It was like I had become empty inside.{/i}"
    nvl clear
    "{i}As time went on, there were more and more light green men in the streets, and my opportunities grew more and more modest.{/i}"
    "{i}It was as if there was a direct correlation between the characters with forearm patches and my vocal range, choreography, arrangements.{/i}"
    "{i}Everything I believed in turned out to be an illusion, everything I could do turned out to be an incomprehensible set of scattered ones and zeros.{/i}"
    "{i}But I kept singing.{/i}"
    if (alt_day2_date == 'mi') and (alt_day2_mi_date != 3):
        "{i}Like back then, remember? Morning Star, '83, the earthquake in Kyoto, and guests from other countries rushing to the exit.{/i}"
    "{i}Desperate Miku sang because she couldn't do anything else. Faster and faster, as if sensing her impending disappearance.{/i}"
    "{i}And even when my palms hurt from the nails and my voice snapped, I wanted to continue what I was created to do.{/i}"
    "{i}To hold in my hands the sign of «do I deserve to cease to be».{/i}"
    nvl clear
    "{i}And sing.{/i}"
    "{i}Even when my lifeless voice was cracking the world, and I was melting before my eyes, bleeding into space in black squares, I was singing. I begged for a miracle, faster and faster - because before the point of no return, I had to finish the verse, make the final point, and exhale.{/i}"
    "{i}You can't do it without an exhale, it's ugly, and no one will believe you're singing with your soul.{/i}"
    nvl clear
    "{i}I only wanted to sing the songs that the one who called me loved.{/i}"
    "{i}But, I guess, I wanted too much.{/i}"
    stop music fadeout 3
    $ set_mode_adv()
    "The shoulder where Miku was leaning was wet, and I turned my head in her direction."
    "She sat with her head rolled back, tears streaming down her cheeks, down her temples, from under her closed eyelids."
    mi "And when the last square of me melted into the air, I woke up."
    mi "What do you think? Is there any chances that I'm dreaming all this, and the real me is out there now, getting ready to go on stage?"
    th "Do androids dream of electric sheep?"
    dreamgirl "Anything that has ever occurred to anyone is true."
    me "Do you know that the first knowledge of any creature is pain? A perfect witness to the fact that you have occupied your body after traveling through realities.  I can pinch you or bite you if you want. I don't want to, but I can."
    "Faith, hurt me. It did. Will be drafted tomorrow."
    mi "Don't. Just remember that sometimes I wake up and I don't know where the truth is and where the dream is. And you yesterday... I felt like I was about to wake up there, disintegrating into squares."
    "She exhaled, and the salt streaks on her cheeks, that had dried up, filled with moisture again."
    me "Stop it. I mean, we've figured out that it's just a different game here."
    me "This is where your father met your mother - just a coincidence on one of the forks of probability, that might not have happened - so it happened in my world."
    me "And here is where you were born."
    "Taking a handkerchief out of my pocket, I looked at it doubtfully."
    "And found nothing cleverer than to dry her eyes with my lips."
    me "Don't cry, please. {w}I can't when you cry."
    show mi sad pioneer with dspr
    mi "As you wish, Senya."
    "She looked at me very seriously."
    mi "But I don't want all your entreaties to mean nothing."
    mi "I'm a frivolous child, I'm used to living for today. And so are you."
    mi "But now I'm very afraid of tomorrow, Senechka. Can you tell me what tomorrow will be?"
    me "Of course I can."
    "I moved to her side, put my arm around her waist, and she put her head on my shoulder."
    me "There are only two options - either we get safely to the district center, where a motorcade from the embassy is waiting for you - and then it's up to the circumstances."
    me "Or we don't make it, and that means the game has moved to my field."
    me "In the first case, we stick together and act on the circumstances. In the second case, I'll need some kind of lead from you to get out to you."
    show mi normal pioneer with dspr
    mi "Address?"
    me "No. In my world, you don't exist in the way we're used to."
    mi "So a phone number, social security and driver's license won't work."
    mi "I don't know."
    me "Then give me your parents' coordinates, and I'll try to find out something and..."
    "A thought suddenly occurred to me."
    me "If you count by my world time, the relocation happened on December 29, 2018, take a few weeks to spare, so as to account for absolutely everything."
    mi "And?"
    me "And we'll arrange to meet somewhere where both-two can definitely be by, let's say, February 2019."
    $renpy.notify('Zagran - international passport')
    me "I still have my zagran alive, the incentive to save up the money will be there too."
    "Miku smiled and dictated me an address in Japan."
    me "Good."
    "Concluded I, rising."
    me "Now, if you want to make it to the rehearsal..."
    dreamgirl "Stop right there criminal scum!"
    th "Staying."
    dreamgirl "You're going to leave without doing the most important thing."
    th "And that is?"
    dreamgirl "Memory, retard! And proof that you haven't been glitchy for six days. You want to think it over, or you want a hint?"
    "I slapped myself on the forehead."
    me "Miku, can I take your picture?"
    show mi happy pioneer with dspr
    mi "Of course! Where's your camera?"
    me "Here it is. Make a smarter face, saying you're the main buka of all Russia and adjacent countries."
    show mi laugh pioneer with dspr
    show frame at truecenter:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 0.8 zoom 1.0 xalign 0.5 yalign 0.20
    show cam_ui at truecenter:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 0.8 zoom 1.0 xalign 0.5 yalign 0.30
    pause(1)
    play sound sfx_7dl["snap"] fadein 0
    scene white with flash
    pause(1)
    scene bg ext_boathouse_day
    show mi laugh pioneer at center
    with dissolve
    me "Pictured!"
    dreamgirl "TAKEN!"
    mi "When will the pictures be ready?"
    me "I don't know."
    "I shrugged."
    me "As soon as I get to the computer, I guess."
    mi "I didn't understand anything. But you were talking about the rehearsal."
    "She looked at the clock."
    mi "If we run, we'll have time for one run-through."
    me "Then let's run!"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_dj_plain:
    scene bg int_dining_hall_people_day
    show mi grin pioneer
    with dspr
    mi "All my plans now are the concert and you!"
    me "Nice plans! Awesome thoughts!"
    "Me praised."
    show mi smile pioneer with dspr
    mi "But the best thing is to combine them so that there are two of that interest me at once!"
    me "«Two of»?"
    show mi shy pioneer with dspr
    mi "Hm... And how that would be in Russian?"
    "I thought for a while, figuring out how to put it in a way that wasn't too cumbersome, but I ended up shrugging it."
    me "Ah, doesn't matter, say as you wish."
    mi "But I want to know the right way!"
    me "But that's the right way!"
    "I pretended to be engrossed in the soup, and paid no attention to the Japanese girl's gurgling or her poking."
    "After a minute she gave up and joined me."
    play sound sfx_open_dooor_campus_1
    pause(1)
    play ambience ambience_camp_center_day fadein 8
    scene bg ext_dining_hall_near_day
    show mi normal pioneer
    with dissolve
    "At the end of our enlightening conversation, Miku lost her desire to go out and do anything."
    mi "Okay, Senya, I have a concert in a couple of hours, I'll go get some rest, deal?"
    "No, it's not a deal."
    "I made an attempt to smooth out the roughness a little:"
    me "Maybe I'll keep you company?"
    show mi laugh pioneer with dspr
    mi "Where, Senechka? In bed?"
    mi "I won't say I'd mind much, but right now I just want to get some sleep."
    dreamgirl "And we'll sleep with you!"
    th "I think she said «no» clearly and unequivocally."
    dreamgirl "So what? You know women: when they say «no», they mean something else entirely."
    th "Not in this case."
    show mi sad pioneer with dspr
    "Miku became sad for some reason."
    dreamgirl "And I say that's exactly what she means."
    me "So you're chasing me away?"
    show mi upset pioneer with dspr
    mi "Senya, you sound like we're breaking up for a year."
    me "Okay, whatever you say."
    "I shrugged and went to my cabin."
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg int_house_of_mt_day with dissolve
    "Sleep."
    "It was so bad that the counselor could barely wake me up when the camp announced the beginning of the concert."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_dj_concert:
    scene bg ext_stage_normal_day with dissolve
    play music music_7dl["lastlight_piano"]
    "We made it almost to the very end - Miku only had time to warm up and sing - as the counselor waved from the far benches."
    show mt normal pioneer with dspr
    mt "That's it, it starts in ten minutes, we wait for the main people to come up, and then we start."
    hide mt with dissolve
    show mi normal pioneer with dspr
    mi "Well... uh..."
    me "nervous?"
    "My voice sounded falsely enough."
    mi "Of course I'm nervous. I'm always nervous before performances."
    mi "But so far I've somehow managed to pull myself together."
    show mi smile pioneer with dspr
    mi "But one day it might not work out."
    me "You'll do great. You're the best I've got, and I have a lot of faith in you."
    mi "Thank you, Senechka!"
    "The minute hand took a strictly plumb position, and Miku, after taking a few deep exhalations, clenched her fists as hard as she could, driving the shiver inside, closed her eyes."
    "And I couldn't help myself, I leaned over the table and kissed her forehead."
    me "Go ahead. And light it properly in there."
    show mi happy pioneer with dspr
    mi "I will!"
    hide mi with easeoutleft
    "She sprang easily up the steps and walked over to the microphone stand, took the microphone off of it, taking it in her now familiar grip - tail to the sky, sound pickup down."
    mi "Good evening, camp!"
    "The speakers picked up and amplified her voice - which didn't need any amplification."
    "But just in case anyone wasn't aware or hadn't heard - the best girl on the planet is performing here!"
    mi "Tonight is truly a beautiful evening, and I'm glad to be spending it among you tonight."
    mi "Very glad."
    "She looked at me with expression."
    mi "The song I would like to open this concert with was written by me a year ago."
    mi "It's called «Farewell Night, Beautiful Night», and I was thinking about how painful and sad it is, after all, to part with loved ones."
    mi "That's why the song is so sad!"
    mi "But today my sadness is light! For even parting for a whole year, we cherish in our hearts the hope of meeting again, under the pines, within the walls of our beloved camp."
    "She nodded to me, and into the scarlet tinted cool evening air came notes of piano, strings - and a beautiful maiden vocal, the equal of which I had never met. And unlikely to meet again."
    "That same feeling when you don't have the vocabulary to understand the words that come off beautiful lips, and you have to navigate only the atmosphere of the melody, to be sad and happy, to lose hope and find new - hearing among the lines the barely audible whisper of hope."
    "Yes, yes, I have fallen into pathos again, but how not to fall here, when you realize that for the lace dance of my beloved excitedly, with bated breath, follows a good hundred other people, and in moments of such unity, especially acute sense of elbow you want to express only enunciation and keep your back straight."
    "And as if it's my merit to be eerily proud of how talented she is."
    "No, that makes sense. She's all so talented - and mine. Isn't that a reason to be a little cocky?"
    "Of course, I'm completely devoid of vanity. Miku didn't win me over with her singing and dancing. Hell, it's the first time I've ever seen her in that kind of concert element - those few performances at the music club don't count."
    "And, of course, when she went downstage and some kids from squad five came in her place with a poem, I turned off the backing track and started hand-holding her and showing her all kinds of signs of attention."
    show mi smile pioneer with dspr
    mi "Oh, wow, what a concern!"
    "She chirped, leaning on the palm set up."
    mi "A true gentleman."
    "And, looking around to see if anyone was looking, she bounced in the palm of my hand."
    show mi laugh pioneer with dspr
    mi "Ugh, I was holding back the whole song! You should have seen your face! Sitting there, eyes rolled back, jaw hanging out."
    mi "Only more of that and I'd say, «Get up and go»."
    $renpy.notify('Kashpirovsky - A psychic, who allegedly remotely healed viewers watching his TV show.')
    me "What a Kashpirovsky."
    show mi smile pioneer with dspr
    mi "Well, what kind of reaction is that?"
    me "Normal reaction... Admiration..."
    mi "You think?"
    "I was trying to be convincing - it's not nice to be branded a victim of hypnosis."
    mi "Okay, I'll take your word for it. I'm used to speaking against the light, I don't see faces most of the time..."
    "She was saying something, automatically doing the mixing, muting the signal from the tape recorder, allowing the audience to hear what the kids were repeating in their wooden voices."
    "At last the torture was over, and four kids, burning with shame, piled off the stage, giving way to the entertainer."
    "Miku was about to yank herself onto the stage, but she was stopped. In the most artless way possible, simply by putting a hand on her shoulder."
    mt "Wait, honey, you're on the equipment, and in the meantime, here, for pants support."
    "She handed us some kind of bundle, emitting a mind-boggling odor."
    me "Thank you, but..."
    mt "Eat!"
    "Ordered Olga and went to the stage to announce the next performers."
    show mi sad pioneer with dspr
    mi "That was unexpected."
    me "Why not. On the contrary. The counselor didn't want the presenter to overshadow the performers. And after what you opened the concert with... Anyway, we should give it a chance."
    show mi shy pioneer with dspr
    mi "If you say so... It never occurred to me at all."
    me "Tell me you've never heard of sound competition."
    "I grumbled, unwrapping the bundle."
    me "Okay, let's eat, or in five minutes Dvachevskaya will be on stage with a guitar - I don't want to miss the spectacle because of the crackling behind my ears."
    "The towel had already had time to get a little greasy, so we ate the buns without unwrapping them."
    mi "How timely."
    "Deeply thoughtful, the Japanese girl rumbled."
    mi "I always feel like eating after the show, now that would be a great way to mumble a few stomach salutations..."
    me "We just ate two hours ago!"
    "I reminded."
    mi "I don't want to hear anything! I have a growing body and a wild metabolism and... and..."
    dreamgirl "Stomach flatulence!"
    "I frowned:"
    stop music fadeout 5
    me "I got it, I got it. But that's it, no more grumbling and ventriloquism. Get yourself together, serious music is coming on stage."
    with blind_r
    pause(1)
    play music music_7dl["closetoyou"] fadein 6
    "The redhead surprised me. {w}Instead of another of her wistful, somber melodies, she took a few chords in a major and frowned."
    dv "Miku!"
    mi "Yes, Alisa?"
    dv "I need... Help. Can you?"
    "I don't know at what point the miracle happened - just one moment the end of the question cools in the air, and an elusive moment later Miku stands, head bowed sideways, smiling stupidly."
    mi "So that's why you..."
    dv "That's enough."
    "Alisa grumbled."
    dv "Get up on stage and help me, this thing needs to be played by two."
    "Although, judging by the performance technique, I could name a few people at a glance who could play it solo as well. My compatriot. And my sweetheart's countrywoman."
    "But Aliska was completely right - playing this thing alone is like dancing a waltz or playing tennis alone."
    "It wouldn't be the same without a partner. Totally won't."
    hide mi with dissolve
    "Miku climbed back onto the stage, picked up her guitar from backstage and stood beside me, counting out a few bars, and..."
    "I sailed again. Like the day before yesterday, under the long sighs of the strings - seeing behind the simple melody, which anyone could reproduce after a couple of repetitions, a thought."
    "What I've always envied is not just the creation of some composition in a laid down form and dimension, but - a thought!"
    "I didn't know the name of this thing, and it didn't seem familiar to me, but we hadn't even gotten to the middle of the first verse, and I was practically gazing at it..."
    "Two people running down the sidewalk after the rain had just finished or, conversely, was still gaining strength. Two, happy at the thought that the sky is so big, and hand in hand, and from under their feet a thousand splashes of smiling sunshine."
    "And it doesn't matter whether they are five or twenty-five, it doesn't matter what gender or height or social status they are, all that matters here and now is that they have accepted each other and themselves, have accepted that life goes on, have even learned to enjoy the ticking of seconds."
    "For seconds, like human life, are not measured by suffering, but by moments when happiness takes your breath away and you believe the person next to you, because everything you have, {b}you{/b} have. After all, you are... Together."
    th "I'll never have that. I'm too old to have a Real Friend."
    dreamgirl "And Miku? Isn't she your best friend?"
    th "But she's my girlfriend..."
    dreamgirl "And a friend. See for yourself."
    "Out of the whole crowd, the bottomless gaze was meant for me alone, and when our eyes met, she winked and smiled."
    dreamgirl "She doesn't want a solid, fat, boring companion. She, like you, wants to fool around and outrage the people around her until she's old."
    mi "«You just look into my eyes, smile, for it's half an hour till dawn. And maybe at last I'll dare to tell you something most important.»"
    "Miku's vocals, high, sensual, with a gasp that you can only achieve if you've been singing all your life."
    dv "«I'll be silent, and you ask, «How's it»? And I'll lie to you. Like I always do, because I can't live without you.»"
    "Alisa's voice, husky, was much more suited to this arrangement, to this performance - take away the stage, take away the audience and replace it all with a campfire, a broken tent and a cubic kilometer of solitude."
    mi "«Among empty storefronts, among other people's lights, you're alone day in and day out, don't remember me.»"
    dv "«We were not and are not, we are a void - a mirage. And every new day is the same as «yesterday»."
    dv "«But I am silent, not angry, living a dream. Close my eyes, sigh, and you will dream again!»"
    "I had never heard this song. But this hit was too precise to be accidental."
    mi "«The touch of lips illusion is scary, but only it will allow me to survive now. Huge risk again, and scary - let it be! One day you'll dream of me!»"
    mi "«Just look into my eyes, smile...»"
    dv "«No! I'll look in your eyes, it's half an hour till dawn. And maybe this time you'll have the strength to tell me what's most important.»"
    dv "«And you can pile up all the lies you want. You'll see for yourself later.»"
    mi "«You don't live without me anymore either!»"
    stop music fadeout 6
    play sound sfx_concert_applause
    pause(2)
    "The last chords faded, and the hall burst into applause!"
    "And while a contented Alisa bowed, a vanity-less Miku ran up the steps to me and sat down beside me."
    show mi smile pioneer with dspr
    mi "How was it, Senechka? Did we play well?"
    me "Great!"
    me "Moore couldn't have played it better."
    mi "I don't know about Moore, but Alisa arranged it very well - and you wouldn't believe that she's only heard this song twice in her life."
    me "Yeah..."
    "Finally Dvachevskaya got her share of the crowd's reverence, and the next dancers from the younger squads got out in her place, and Miku, with a bored yawn, set them a veneer, turning away from the stage completely."
    play music music_list["my_daily_life"] fadein 5
    mi "Do we have anyone else performing?"
    show mt normal pioneer at left with dissolve
    mt "Yeah, I managed to get Slavya to close the concert."
    me "Wow! What did it cost you?"
    show mt laugh pioneer with dspr
    mt "You don't want to know! Okay, this one is ended, I'll go announce the next ones."
    hide mt with dissolve
    mi "Actually, Electronik also wanted to perform."
    mi "I found a xylophone in the club, and he thought of playing something on it, even learned a song. But... As you can see, he changed his mind."
    me "Maybe it's for the best."
    "Having treated the business of rehearsing myself as something better repeated at least a hundred times, I looked with disbelief at those who «learned» some song."
    "You can learn it, but will you be able to smile and wave to the audience on stage, or will you come out all stiff, in a tuxedo, with frostbite eyes, sit down, lean into your instrument and no one can see you until the very end?"
    "Especially when the bar of quality is set, when the concert is opened by a girl for whom working for an audience and dancing to the beat is as natural as breathing - after all, she has no other life."
    "Yes, the performance with Alisa revealed a qualitatively new facet, in which just professional, well-coordinated playing is enough to delight the audience. But in that case, what can the rest of the cohort of performers boast of?"
    "After all - I speak only for myself, I'm not at all pretentious - only these two performances will linger in the memory - that's all."
    with fade2
    "Miku performed one more time, and I deeply regretted that I hadn't managed to prepare anything all week. Although, of course, a week is not the time in which you can prepare something you can be proud of."
    "Even psychologists of all stripes say that it takes at least three weeks to develop a normal habit - and that what bounces off the stage should be as good as habit in the artist's flesh."
    "Ideally, from the first or second day there should be learning notes, lyrics, choreography... But of course, that's if you're trying to stage a performance from scratch."
    "So you don't have to stand on stage, frantically clutching the microphone stand."
    "And Miku had a lot of room to run around - most of her songs were rehearsed long before she even knew there was such a camp..."
    with fade2
    "As I suspected - the rest of the kids were not memorable at all, not that level, not that significance."
    "In my head there was a kind of mishmash of mastering, the quiet creaking of the stairs to the stage, one nail at the very edge of the stage, for some reason not hammered all the way in or just squeezed out by the cracked wood."
    "And on the rough boards, though scraped to a white finish, no one got a foot on them for some reason, and there were no technical problems, and absolutely nothing memorable about the scene."
    "It was like some kind of gray, rippling canvas was thrown over there, eating up time, sights, memory... No, if you put your mind to it, you can pick out certain frames from an hour of reading poetry, lined up, singing about Belovezhskaya Pushcha with thin, brittle voices and drum arrangements from «You Never Dreamed»."
    "But I was too spoiled, too spoiled, to give credit to the trying kids."
    "Miku, on the other hand, rejoiced heartily - not observing herself from the outside, she somehow thought that she worked with about the same quality, and so, taking advantage of the lack of a microphone, she acted as the most active spectator from behind her console, clapping her hands to the beat, smiling and shouting «bravo»!"
    with flash
    "Not that I was that bored, but when Slavya came onstage in a Russian folk costume and the strings came out of the speakers, I exhaled."
    me "Phew, praise be to Random! The concert went off without a hitch."
    show mi grin pioneer with dspr
    mi "You had doubts?"
    me "I had my doubts, to tell you the truth. {w}I've already had some experience with the organizers' negligent attitude."
    show mi serious pioneer with dspr
    mi "Not caring? Is that a man given the task of making a show for an entire camp..."
    me "And he's doing everything just for the sake of ticking the box and closing the outfit."
    mi "But everyone will see that, they'll point the finger, they won't come to the concert!"
    me "Do you think they care? On the contrary - next time no one will force them to do all sorts of nonsense."
    show mi sad pioneer with dspr
    mi "I find it very hard to believe what you say, Senya. I've never encountered such a thing."
    me "Random bless, and you won't encounter it. It's very wonderful that you're working with a collective that cares about performances. It's just... It's just not everybody is like that. But we got distracted, let's listen to Slavya!"
    "Slavya was closing the concert with her song."
    "A sarafan that opened up her slender legs, a kokoshnik, red boots - Slavya was irresistible and she knew it very well. Eh, I wish I hadn't been busy!"
    show mi grin pioneer with dspr
    "Miku, sensing me staring at the activist with all my eyes, only laughed softly - for all its intricacies, my personal starlet turned out to be the jealousy-free ideal to which you will always return."
    "At least by virtue of the laws of geometry."
    "The blonde girl stood with her arms up to her chest, one horizontal, parallel to the ground, the other resting on the palm of the first, and her index finger touching her cheek."
    "After standing like that for a few seconds, she sighed and, catching Miku's gaze, shook her head."
    mi "I knew she'd want it without a phonogram."
    "In a whisper the Japanese girl said."
    mi "All right, as your majesty commands."
    "The music faded, leaving us alone with Slavyana's voice tinged with good acoustics and her song."
    "In a way unaccustomed to me, the girl looked around the audience with a melancholy gaze, and melancholy in the same way, lilted:"
    sl "{i}The maiden beauty fell in love, fell in love with the boy, she sighed and sighed...{/i}"
    "Catching the rhythm, I clapped softly to the beat."
    mi "Senechka?"
    "With an encouraging nod, I continued clapping to the beat."
    "And - that magic: not ten seconds later, someone else reacted from the other end, and there were already two of us."
    "United by a common passion, a common spectacle, we thought and breathed as one organism, kindly envied those on the other side of the bar, and wanted to participate as much as we could."
    "An almost religious feeling whose outlet is most often and easiest to express precisely in this kind of rhythmic clapping."
    "Miku smiles as she claps beside me, putting right foot on toe and counting the beat with the movement of her knee."
    "And I've had an internal metronome since I was a kid that sets the right beat - from largo to presto."
    "The kids behind us are fiddling and clapping, too - not very orderly at first, but slowly getting involved, then the older squads join them, even older ones - in an upward wave from the front row to the back benches, where the chowderheads from the first squad and the adult staff are bored."
    sl "{i}Oh, nettles and swans, tears are bitter water...{/i}"
    "Slavya smiled, holding both the beat and the breath, managing to show some unknown to me, but undoubtedly related to the Russian folk, dance."
    sl "{i}I can't think, I'm counting the days until the meeting...{/i}"
    "The audience was already clapping in unison, as if they had turned into a single collective mind with the only need to become part of what was happening on stage."
    "And Miku... Well, she, as a girl accustomed to stage image hypnosis, was quietly winding up the cords and turning off the equipment."
    "And timely!"
    sl "Thank you for your attention! This concludes the concert, we are waiting for you at the dinner, and after that - at the farewell disco!"
    mt "First squad! Don't split up!"
    "And then, as is always the case, the transparent, crystal silence broke, filled with the hum of voices, the shuffling of soles. {w}Were we in a theater, there would have been squeaking seats, too."
    "Not ten minutes later, it was just us at the stage."
    stop music fadeout 5
    scene bg ext_stage_normal_day with dissolve
    show mt normal pioneer at left with dissolve
    play music music_list["what_do_you_think_of_me"] fadein 3
    mt "Guys, we need to get the equipment ready for the dance as a matter of urgency."
    mt "Semyon, Miku, you do the most important part, the wiring and music. Elektronik, Alisa, Slavya, you're in charge of the speakers and moving the equipment."
    show un normal pioneer at right with dissolve
    un "And... me?"
    mt "What? I still don't see a newspaper on the stand! So grab Zhenya in your teeth and make the newspaper hanging up to the horn!"
    un "Okay..."
    hide un with dissolve
    mt "Also, you can grab Ulyana too."
    "And a few times quieter, sideways, to myself:"
    mt "I'm not sure she'll do much good, though."
    mt "Or no, Ulyana, you have another assignment."
    show us smile pioneer at right with dspr
    us "What is it, Ol'dmitryvna?"
    mt "Take Semyon's stepladder, cyberneticists have a box with a light-music system, and hang it on the trees."
    show us surp1 pioneer with dspr
    us "Seriously?!"
    show mt grin pioneer with dspr
    mt "Afraid you won't make it?"
    us "You're kidding!"
    hide us with easeoutright
    "Ulyanka instantly turned around and raced off toward the cabins to change her clothes. A reverse flow of air blew in, «We're not stokers, we're not carpenters»."
    show dv angry pioneer at right with dspr
    dv "And why is Semyon going with the plates, and we're going with weights?"
    show mt normal pioneer with dspr
    mt "Can you hook up all the equipment properly so that all we have to do is show up and dance? No? Semyon can. Well, I'm not going to force our host, she's got work to do all night."
    "Muttering something obscene under her breath, Alisa stepped back to the stage and leaned her head sideways thoughtfully, trying on a large black cube with carrying handles."
    hide dv with dissolve
    show sl normal pioneer at right
    show el normal pioneer at center
    with dissolve
    sl "I'm ready, Olga Dmitrievna."
    el "Ready."
    "Slavya has already had time to change - a bloody meteor."
    hide sl
    hide el
    hide mt
    with dissolve
    me "Okay."
    "I climbed up on the stage, after unplugging all four speakers, coiled and dropped the cords underneath and hesitated."
    th "Maybe, really help them? Get things done quicker?"
    if (alt_day5_mi_dj_voyeur != 4) and (not alt_day5_mi_dj_dv_blade):
        if loki:
            th "Hell nah."
            me "I'd help you, but there's someone here who's very fond of water procedures. Send them my regards."
            el "I don't get it!"
            me "It's okay."
            "Nodding to those present, I jumped off the stage and walked over to Miku."
            if alt_day5_mi_dj_voyeur == 2:
                $ alt_day6_mi_dj_dv_evil = True
            elif alt_day5_mi_dj_voyeur == 3:
                $ alt_day6_mi_dj_sl_evil = True
        else:
            menu:
                "Agree":
                    $ alt_day6_mi_dj_sonic_agreed = True
                    me "No, you know, I think Miku can handle the connection herself."
                    me "You don't mind if I help a little bit, do you?"
                    show mi smile pioneer with dspr
                    mi "Not a bit, Senya."
                    "She smiled."
                    mi "On the contrary, I'm all for it - you'll get through it faster and you'll be less tired."
                    th "What a touching concern for comrades."
                    show sl normal pioneer at left with dspr
                    "I turned to Slavya."
                    me "Gathered-carried?"
                    if alt_day5_mi_dj_apology == 2:
                        sl "No, Semyon, it won't work."
                        me "But why?"
                        "She poked her finger in my right hand."
                        sl "Because someone didn't take care of his hands yesterday, and today he's walking around with a band-aid."
                        sl "You'd better go and really help Lena with the paper."
                        sl "Sure, as soon as you're done with the connection."
                        "Had to take her advice."
                "Don't agree":
                    pass
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_dj_reject:
    scene bg ext_stage_normal_day with dissolve
    th "Let Schwarzenegger drag."
    me "See you at the square."
    show mi normal pioneer with dissolve
    me "Where are you going now?"
    mi "I'm going to the club to get some records while I'm at it. What about you?"
    me "And I'm just about to do the whole trial-and-case thing."
    "Putting the cover on the remote, I closed the holders and took it, like a suitcase, by the handle."
    "The bag of cables was already waiting its turn."
    me "Do you need any help?"
    "Miku shrugged her shoulders indefinitely."
    mi "No... I'd rather help the girls..."
    show mi serious pioneer with dspr
    "She measured me with a look."
    mi "But you seem to have enough work as it is."
    show un normal pioneer at left with dissolve
    un "Guys... Are you going to watch the wall newspaper when you're done?"
    menu:
        "Yes":
            me "Sure, let's go!"
            me "Who knows what you've put in that room, got to see everything."
            show un shy pioneer with dspr
            un "But I just all... as you allowed..."
            "Confusedly, she babbled."
            show mi smile pioneer with dspr
            mi "Senechka, stop teasing Lena."
            me "I'm sorry."
            "I smiled."
            me "Sorry, we'll come. Where will it be?"
            un "At the stand... At the entrance."
            me "Wait for us in half an hour."
            "Lena nodded and turned toward the library."
            hide un with dissolve
            un "Good…"
        "As if we have nothing else to do":
            me "Yeah. Let's go. Instead of dinner?"
            show un shy pioneer with dspr
            un "But there's still plenty of time..."
            me "No, I'm on a tight schedule as it is with this concert, so no extra activities until I eat."
            "Miku just waved her hand."
            show mi upset pioneer with dspr
            mi "Whatever you say, Senechka."
            $ alt_day6_mi_dj_un_evil = True
    hide mi with dissolve
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_dj_sonic:
    scene bg ext_square_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 3
    play music music_list["lightness"] fadein 3
    "A fairy tale is soon told, but it is not soon done..."
    "Of course, they were exceptionally strong guys - in Slavya I could feel that steel vein, which distinguishes a truly Russian, middle-aged, Aliska somewhere fattened her musculature, comparable only to the figure of a track-and-field athlete."
    "Against the background of such girls, there was no need to complain and whine at all - Elektronik went into cybernetics clearly by mistake, judging by the sharp movements, he was no stranger to sports. And me... What about me? Do you want me to sing?"
    "The speakers were carried by two, the first trip we walked together with Alisa."
    "Forty kilos of pure weight - practically on par with Miku. But if I would have gladly carried the little Japanese girl in my arms as much as I wanted, here - not only was this cow oversized, it could only be grabbed by the handle!"
    "At least the makers of this masterpiece of acoustics guessed to attach some wheels to the bottom, so a good half of the way - from where the paved paths had already begun - we were mostly rolling, not carrying."
    "But here, too, the redhead managed to distinguish herself - at some point she decided I could push myself, she stopped helping me and walked beside me. Well, no wonder that at one of the joints «cow» skidded to the side, almost crushing with all it's weight on Dvachevskaya's leg."
    "Slavya yelled at us for sabotaging the process, for being stupid, that we can't be trusted anything..."
    "So the second trip was without much adventure - because now the activist was paired with me."
    "Four stage speakers, four veteran LOMOs, which in my day were being sold as hot buns, were transported by four careless pioneers."
    "I wish I had a proper amplifier in here, something bassy..."
    if alt_day2_us_dubstep:
        "I was reminded of how I had fulfilled a long-standing desire to listen to polyhymnia on this kind of acoustic."
        th "Maybe..."
        dreamgirl "It can't."
        "Miku showed up in the walkway from the clubs, clutching a stack of records and a table lamp to her chest."
        dreamgirl "Slavya won't allow. {w}Miku won't. Oh, and Ulyanka's going to fly off the tree, one hundred percent."
        if alt_day6_mi_dj_walkman:
            "Besides, there was no guarantee that Miku had brought the present with her."
            th "Eh. I was so thinking a little more dubsteb for goodbye!"
            dreamgirl "You're going to get skinny! Go help your girl, or she'll fall over now."
            "I hastened to follow my subconscious's advice."
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene bg ext_square_sunset
    with clock_r
    "And though we worked as fast as we could, we were still late for dinner."
    "Moscow time is twenty hours and thirty minutes."
    sl "All right, let's go. Try to organize something."
    $ alt_day6_mi_dj_feed = 'sl'
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_dj_newswall:
    scene bg ext_square_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 3
    play music music_list["lightness"] fadein 3
    "The table was already in its usual place, and all that remained was to place the remote control on it and put the plugs in their proper sockets."
    show mi normal pioneer with dspr
    "Miku was busy unwinding the cables, and I, already relieved, had to admire her as she bent over once more... Like thaaat!"
    if alt_day_binder != 1:
        "And again our semi-comic acquaintance, again the feeling that she makes such gestures far from accidental."
    "And sure enough."
    "Catching another of my admiring glances, the Japanese girl turned her head and winked:"
    mi "What are you looking at, Senechka?"
    me "Nothing..."
    "I was embarrassed."
    mi "How?"
    me "I was looking at you."
    show mi shy pioneer with dspr
    mi "What's wrong? Are my clothes dirty or did I suddenly grow a second head?"
    me "No... It's just the way you're leaning..."
    show mi laugh pioneer with dspr
    mi "Nightmare! No concept of flirting! Come on, Romeo, let's go get the records."
    "She picked me up under elbow and dragged me to the top of the camp, to the music club."
    scene bg ext_musclub_day
    with dissolve
    "That's the way it always is - the pioneers are having fun, resting, getting high from their last night at camp, their last supper... And we're running around."
    "Pioneers, damn them. Be ready - always ready. Always ready to turn the last night from languid observation of the sunsetting luminary with the dearest person in the bunch into an organizational nightmare."
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene bg ext_musclub_day
    with dissolve
    show mi normal pioneer at cright
    with dissolve
    mi "Take all the records you can carry - I haven't sorted them out since the last dance."
    me "Um... Why?"
    mi "I just didn't have time. Someone was always distracting me!"
    "She looked at me meaningfully."
    "But she was attacking the wrong person. I held my gaze steadfastly and smiled. After making sure no one was watching us, I walked over to her and, smiling like a contented crocodile, kissed her on the nose."
    "Right - because Ulyanka is decorating the trees now, Alisa is messing around with the speakers, Slavya is there too... Basically, if there's a desire, we can close the door and..."
    show mi smile pioneer with dspr
    mi "Mmmm... Don't forget to do that more often."
    me "I won't forget!"
    "Sincerely, I promised."
    me "By the way, I already got everything I needed. Let's go?"
    mi "Now."
    "Grabbing a desk lamp and a clipboard with some notes from the table, Miku turned to me:"
    mi "I'm ready!"
    stop music
    play sound sfx_open_door_clubs_2
    scene bg ext_square_sunset
    "Five minute walk to the square"
    play music music_list["went_fishing_caught_a_girl"] fadein 3
    scene bg ext_clubs_day with fade
    extend ", and we, having unloaded our precious cargo, set out to fulfill the promise we had made to Lena."
    th "She didn't do it for nothing, did she? The newspaper will certainly be praised, but it would be better to do it now, while this act remains exclusive."
    scene
    $ renpy.show("bg ext_stand3_7dl", what = Dawn("bg ext_stand3_7dl"))
    with fulldiam
    "Lena was already here: she was urgently putting the final touches on the canvas - checking that the glue was firmly in the corners, and that the newspaper itself was well pinned."
    "The latter took its place between the hand-drawn map - with the Kremlin and Admiralty listed there for some reason - and the row of certificates given to the pioneers for the review contest in the middle of last week."
    "She stretched up as high as she could, got up on her toes and stretched, stretched up so that her shirt was out from under the strap, and her skirt came up, exposing her beautiful legs."
    "We absolutely synchronously tilted our heads sideways."
    th "Okay! No, of course I understand my healthy interest..."
    "Trying to do it as gently as possible, I nudged Miku in the side with my elbow."
    mi "Ahem!"
    "Lena immediately lowered herself and turned to face us briskly and tried to tuck her shirt in."
    show un shy pioneer at left with dissolve
    un "Oh, you guys...{w} here."
    "She waved her hand absently toward the paper, finally stepping aside and letting us admire the resulting masterpiece."
    show mi smile pioneer at right with moveinright
    mi "Well, let's see what you've got here."
    "Miku stood in front of the newspaper with the most profound look, even propping up her chin for effect."
    "The only thing missing were zero diopter glasses to complete the look."
    "We almost synchronously glanced from article to article, from picture to picture."
    "Lena listened carefully to all our wishes, she did not hang the most personal illustrations, but kept them for herself, covering the empty spaces with articles about the events in the camp, written out in calligraphic handwriting."
    "Well, that's right, a newspaper is different from an album, because it must contain not only something to look at, but also something to read."
    th "I wonder why she brought us funny pictures in the first place - she must know that our cuddling and kissing is not very clever, to put it mildly, to file it in the issue."
    dreamgirl "Maybe she wanted to hint - I know what you did last summer!"
    th "Well, maybe. Only why hasn't she made any demands so far? What kind of blackmail is this?"
    dreamgirl "You think I know?"
    "Inner voice sounded surprised."
    dreamgirl "Don't you want to ask her?"
    "After squinting at the serenely smiling Lena, I decided to hold off for now."
    th "Not really."
    dreamgirl "Well, then let's get excited about what a great paper she's got out. She seems to be getting nervous."
    me "That was great."
    "Sincerely I said."
    "In spite of the attacks of the inner voice, I managed to keep my head clear and my grades unbiased: objectively both the drawings, the article and the general design style, all looked great."
    show un smile pioneer with dspr
    un "Thanks..."
    "She whispered, clearly flattered."
    mi "Lena, is it okay that there's so much about Senechka?"
    un "No. Whoever has done as much as he has written about..."
    "We looked at the resulting beauty for another ten minutes - although we were well aware that in this situation all we can do is to pay our respects, we will not have any effect on the already completed issue."
    "Unless we're like those psychopaths who carry around a vial of sulfuric acid in case they see Danae."
    th "That's it, everyone said okay. What's next?"
    me "It's just gonna hang there, isn't it?"
    un "Yeah, why?"
    me "I mean, nobody's gonna tear it down, spoil it?"
    un "No. Why would anybody want to tear or ruin somebody else's paper?"
    "I shrugged. All too often I've encountered this kind of thing myself - done for nothing. Just like that."
    "Some noise was heard from the side of the dining room, and I glanced at my watch."
    me "Oh, hell!"
    "It's 9:30!"
    me "We're late for dinner!"
    mi "And the horn never came."
    me "Come on, let's try to get something edible. I absolutely refuse to dance on an empty stomach!"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_dj_supper:
    scene bg int_dining_hall_people_sunset_7dl with fade2
    play ambience ambience_dining_hall_full fadein 2
    "Canteen was pack-jammed."
    show mi smile pioneer with dspr
    "But, taking advantage of the fact that half of our squad was busy getting ready for the dance and other useless activities, we were seated at ease at the largest table assigned to our squad."
    mi "Senechka, it was in vain that we did not go to Lena's to see the paper. It would have been a shame for me to try..."
    me "Miku, we'll go. I promise. We'll have supper now, and then we'll go."
    "I don't think we're really going to go see any newspapers - we've already got the equipment hooked up in time for supper, and now they're going to drag the lead behind the turntables right after we eat."
    "And judging by the thundering bass from the square, it's already warming up."
    "That seemed obvious to Miku, too."
    show mi normal pioneer with dspr
    mi "Senechka, we're not going anywhere. There's a dance now, and then it's lights out..."
    me "We'll see tomorrow, then! No one will tear it down and spoil it, will they?"
    mi "No, of course not, how could you even think that?"
    me "So we'll go dancing and we'll see tomorrow - we have to do something between packing and leaving anyway."
    show mi sad pioneer with dspr
    mi "Still... That's not very nice."
    me "Okay, then let's go straight after the disco and see!"
    "I gave up."
    mi "Here, I like this one better."
    if alt_day2_mi_dinner:
        "Miku reactively consumed mashed potatoes and cutlets - just like the second day - and, after tipping glass of tea into herself, stood up."
    else:
        "Miku reactively consumed mashed potatoes and cutlets and, after tipping glass of tea into herself, stood up."
    mi "Let's go, Senechka! Or they'll start without us!"
    "Shaking my head, I headed after her."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_dj_late_supper_sl:
    scene bg int_dining_hall_sunset with dissolve
    play ambience ambience_dining_hall_empty fadein 4
    play music music_list["a_promise_from_distant_days"] fadein 5
    "Meeting place cannot be changed. We're right back where we started, and tomorrow we'll move even farther back to the source."
    "The bus we unloaded from will take us back into its gut and drag us away to where we came from."
    sl "Sit down, I'll go and see what's left in the kitchen."
    "Like the bourgeois yo-yo, which, like that polichinelle secret, has become mega-popular and then fallen into oblivion again. The nearest peak of popularity, if memory serves me correctly, will be in the mid-nineties, when half the world's population will be walking around with those plastic rounds."
    show mi normal pioneer with dspr
    show dv normal pioneer at left with dspr
    show el normal pioneer at right with dspr
    if alt_day_binder == 1:
        "We sat down at the very table where I had been saved from a horrible death from malnutrition the last time, and, exchanging brief remarks, began to wait for the activist."
    dv "Yes, whatever they say, being friends with our upstart is profitable."
    show mi serious pioneer with dspr
    mi "And if she couldn't feed you, then what?"
    show dv grin pioneer with dspr
    dv "It's obvious! Then there's no reason to be friends with her."
    mi "Don't you think it's not very nice to judge people only in terms of usefulness?"
    el "I second that. A person is not a washing machine or a television set."
    show dv laugh pioneer with dspr
    dv "Look who's speaking! I see your eye is healed already? Not even a bruise left!"
    "Electronik recoiled, instinctively covering his left eye with his palm."
    if alt_day3_technoquest1 >= 1:
        me "So, according to your logic, I should have sent you away yesterday, right? You are of no use to me."
        show dv sad pioneer with dspr
        dv "Look, who asked for it!"
        mi "You're right, Senechka. It shouldn't occur to a pioneer at all to judge people by their usefulness!"
    el "Man is man's friend, comrade and brother."
    dreamgirl "And also dinner and a sexual partner. True, true."
    me "Alisa, you seem to have a problem with Slavya. Even though she's trying her best not to bug you. What's your problem?"
    show dv guilty pioneer with dspr
    dv "It's strictly between us alone."
    "Alisa said, bursting into flames - as only redheads are capable of - in an instant."
    mi "And it's because of you, Senechka."
    me "Really? Well, well, well..."
    show dv shy pioneer with dspr
    dv "A chatterbox is a spy's weapon of choice."
    me "Perhaps if you hadn't imposed that idiotic bet on me before the tournament, things would have been different."
    mi "What bet?"
    "Miku looked at me incomprehensibly."
    mi "Senechka?"
    show el grin pioneer with dspr
    me "Don't ask."
    "Electronik behind me snorted softly."
    "Mumbled something about «groping and peeping»."
    show dv sad pioneer with dspr
    dv "So, are you going to keep mocking me?"
    me "No. But your attitude towards Slavya has been sorted out a little bit. Except it's not very clear why you continued to communicate at all."
    show sl smile pioneer at fleft with dspr
    sl "And we didn't continued."
    "Slavya sat down next to Alisa and set a pot of jacket potatoes, a jug of milk, and a plate of coarsely spread bread on the table."
    "The hungry horde needed plenty of provisions, she had to go three times - each time proudly disregarding offers of help."
    "Ffff, whatever."
    sl "Sorry, there's just nothing else in the kitchen - the cooks are gone, and I was afraid to climb into the fridge."
    me "It's good as it is! It's been a long time since I've had classic Russian food!"
    "I instantly picked the biggest potato out of the pot and, burning, blowing on my fingers, began to «undress» it."
    show mi shy pioneer with dspr
    mi "Excuse me... Is that it? You're just going to eat potatoes?"
    "In a bit of shock, the singer asked."
    me "Yes, of course. Do you want me to peel them for you?"
    mi "I don't know... What about the meat, the sauce..."
    "The sensibly boiled potato parted with their skin quickly, and I held out the root vegetable to Miku:"
    me "Cut! Just don't forget to salt it, and with bread, to make it nourishing."
    show mi smile pioneer with dspr
    mi "Thank you, Senechka. I didn't think you could just eat boiled potatoes! Why didn't they serve them in the canteen before?"
    "Slavya and I looked at each other."
    dreamgirl "What a great question!"
    me "Well, probably for the same reason they never gave dumplings or pancakes here."
    dv "Pancakes were served by the way."
    "Alisa quipped."
    el "Actually, they were fritters."
    show sl laugh pioneer with dspr
    sl "With honey. And Ulyana stole a tub of honey for the whole squad."
    dv "Looks like someone needs a brain freshener before the dance."
    "Alisa glanced unkindly at the cyberneticist."
    "And I hastened to restore an atmosphere of peace and friendliness to the table."
    me "Bon appetit!"
    "The pioneers responded indistinctly - Miku was a little behind in the national consumption schedule, but rapidly closing the gap."
    "The rest of them were overcooked with boiled potatoes, sprinkled with crumbs, with fancy milk «whiskers», and paid no attention to any nonsense."
    "Although Slavya managed to distinguish herself here, too - she ate as if she'd been to a social occasion - the part where you should stay clean."
    "On destroying potatoes part I was concerned that she had managed to consume no less than Elektronik and Alisa put together."
    dreamgirl "Ew, what a choice of words!"
    th "Ah, excuse me, taste! With a puffed up little finger in a snow-white shirt - tasted about half of what was brought. Had about half a pot."
    "No, I don't mind at all - still, compared to the miserable sandwiches this «refill» was qualitatively higher, but still..."
    dreamgirl "Guh, it's okay , why are you whining again? She cooks borscht for you, gives kiss after work, even can outdrunk you sometimes."
    if herc:
        dreamgirl "The perfect Missus Sycheva!"
        th "God forbid."
        "The only possible missus was now sitting on my right and, judging by the round cheeks, had taken a slightly bigger bite than expected."
    else:
        dreamgirl "The perfect Madame Persunova!"
        th "God forbid."
        "The only possible madam was now sitting on my right and, judging by the round cheeks, had taken a somewhat larger bite than expected."
    "She was looking pretty good, though."
    me "Drink."
    "Sincerely, I advised."
    "..."
    "In short, I'd rather didn't."
    me "You don't salt it too much?"
    if alt_day5_mi_dj_hentai_done:
        mi "Well, no, it tastes really good.!"
    else:
        mi "I accidentally. {w}I've eaten things on my tour that are far more questionable."
    "She smiled."
    sl "Like your first day here, huh?"
    me "Yeah. Only now there's more of us, and I'm not leaving camp with what I came with."
    "It's hard to call the people sitting at the same table with me friends in the literal sense of the word, but they were no longer strangers."
    "I remembered how I could go to work for months and not know anything about my co-workers except their first and last names and the function they served."
    "Must be something in the atmosphere after all."
    dreamgirl "Or in the looks of those around you."
    th "Pardon?"
    dreamgirl "It's obvious if you look closely."
    dreamgirl "There is not one among them who looks indifferently. The quarter-century importation of indifference coming to Russia has not yet touched any of them."
    dreamgirl "Among them you look the most aloof."
    sl "All of us are going away. Where are you going, by the way?"
    "With an incomprehensible hint Slavya asked."
    sl "Home? To the embassy?"
    th "I wonder if she herself believes the fairy tale our counselor hastily concocted?"
    "Or here's a question on the same theme of jokes over three hundred - why did the counselor need to concoct this fairy tale in the first place?"
    th "She knows something, after all. Why would she make it up?"
    th "What could be the counselor's interest in Semyon, who appeared out of nowhere and is probably about to disappear into nowhere?"
    th "Knock me on the forehead with a ballpoint pen and sell me for organs? {w}Or does she know something I don't?"
    dreamgirl "What's there to think about now? You should have turned on your Mr. Noir with his collar up and the leitmotif of «everyone will betray» from the beginning, looking for your answers and arranging the pieces on the board."
    th "You suppose we can't combine anything?"
    dreamgirl "Yes, we probably would. If it weren't now three hours before midnight before departure day."
    th "But Miku is..."
    dreamgirl "I'm not saying you did the wrong thing. You chose what really mattered to you. And that's great, I'm very proud of you. But this way of doing things flat out denies you a chance to make sense of the situation."
    th "Do you think they'll let us out of here?"
    dreamgirl "It's hard to say. I guess we'll have to make some sacrifices to keep, if not ourselves, then at least this union with your girl. I hope you don't continue to think of her as a robot?"
    th "Not really anymore."
    me "Embassy? I don't think so. I'll probably try to fulfill my newfound desire to learn Japanese."
    "I smiled at Miku."
    "Alisa choked on her bread, but said nothing."
    sl "To Japan?"
    "The activist smiled politely."
    me "No. I mean, yes. Anyway, it's complicated there."
    "Can't tell them about the fact that I, strictly speaking, don't exist, can I?"
    "And neither does Miku."
    "So the two loners of non-existence met - in a camp that's one hundred percent not on the maps."
    me "I didn't get here by chance either, so I'll have to get used to it, try to adjust, get my papers straightened out, see what's going on with my education. In a nutshell, the problems start right outside the gate."
    "And hell knows if I'd agree to face them if it weren't for one smiling stimulus chomping loudly beside me."
    "I coughed meaningfully, and she blushed sweetly."
    show mi shy pioneer with dspr
    mi "Pmofrppm!"
    "She mumbled."
    me "Okay! Don't even try to say it! Chew it first."
    "The Japanese girl nodded in agreement and went back to the profound process of working her jaws."
    sl "What do you even want to do?"
    "I want to live. If I'm not mistaken, I can only live here... And everything else...{w} I'm an atheist, I have a secular education, and there's nothing but worms waiting for me on the other side."
    me "I haven't made up my mind yet, but hopefully Miku can help me with it. She said something about her father..."
    show sl smile2 pioneer at fleft with dspr
    if alt_day4_mi_dj_hedg:
        sl "What about his disapproval of you?"
    else:
        sl "But he's so official!"
    me "That's okay. We'll try to find some common ground somehow."
    "I smiled."
    me "After all, we already have something in common."
    mi "What do you mean?"
    "Finally, Miku chewed up."
    me "About the attitude towards you!"
    "Both of us love you, and both of us want the best for you, and we can't imagine life without you."
    show mi shy pioneer with dspr
    mi "Senechka..."
    dv "Well, you two make out more here."
    "Expectedly Alisa snorted."
    el "Alisa, if you don't like it, why are you watching?"
    dv "I'm not watching, I'm eating."
    "Alisa parried, returning to the pot that had already shown the bottom."
    "Well I guess I'm full."
    show mi normal pioneer with dspr
    sl "And then?"
    "It was a reasonable, substantive question, but a little premature - I had no time to ask even myself yet. And Slavya wouldn't stop."
    sl "The problems will end, you'll graduate. What do you want to do next?"
    "The thought of waiting behind the scenes for the chosen one was still warming to me, but under a slightly more sober perspective, all the drawbacks of this romantic dream were becoming apparent."
    "First of all, there is no such position."
    "Secondly, if becoming her impresario or, as it is fashionable to say now, manager, is still an occupation not in my line of work. Is this what I want to do for the rest of my life? Bickering with stage technicians, concert hall owners, and the Ministry of Culture?"
    "And if not, what then? Some kind of Orientalist? Or an engineer, too? An ambassador? A politician? What could a gaikokujin be useful in Japan?"
    dreamgirl "A linguist, Sem. Unless you and I are forcibly separated, I won't let you forget anything. You'll manage somehow with Japanese, but with your knowledge of English..."
    me "I'm going to study Eastern. With the prospect of working as translator. And then we'll see."
    sl "You take life too seriously."
    "Slavya gave me a strange look."
    "I didn't see any judgment in it, though."
    "It was more like those moments when you ask a child to sing something and he has a vocal range of five octaves."
    me "What can I do. I want to combine too many incompatible things..."
    "Let's start with your damn fantasy world with Genda in the square."
    sl "And?"
    me "No «and». I just make my head work for solving problems instead of picking my nose."
    el "Can we not talk about it at the table?"
    "It's like there's something left..."
    me "Sorry. An unfortunate metaphor. Let's say that I'm used to looking at any act as the first link in a chain of future events."
    sl "But you can't account for everything..."
    "It occurred to me that since that first day I never really talked to Slavya."
    "Otherwise why this surprised incomprehension?"
    sl "Then, how do you do anything at all?"
    th "That's not the problem."
    me "Imagine that you lived to be 30, 40, 50 years old, spent your whole life doing nonsense and ended up on the sidelines. But you have three differences from your peers."
    "I started to curl my fingers."
    me "One, you have a first-person view of the world."
    me "Two, you remember all the wrong choices you've made in life, because you've counted a thousand times."
    me "And third, you have the ability to calculate events, so you climb up somehow, trying to fix all the things you did wrong in your youth."
    "For example, if all your life you've wanted to pull your English up to a conversational level, now you have the ability to communicate with native speakers."
    dreamgirl "And fourth, you have been fulfilled the cherished dream of all your kind, by returning to your youth without disturbing your memory, your life baggage, or your acquired skills."
    sl "And you can?"
    me "What?"
    sl "Calculate."
    me "You said yourself that it's impossible to calculate absolutely everything. But, for example, if I realize that in my favorite job I absolutely need the skill of speed typing, I'll enroll in a course or otherwise develop that skill."
    me "Everything else is about the same level."
    "For five minutes now, only Slavya and I have been talking, the rest have been quiet, listening to us."
    "But then Alisa couldn't take it anymore."
    show dv grin pioneer with dspr
    dv "So you can calculate life? Calculate mine then."
    "I shrugged."
    me "Easier than you think. You've got the talent of a musical performer to your credit, so you might as well try your hand at the stage. But you'll probably send it away because the strict touring schedule is contrary to your free-spirited nature."
    me "So you'll probably have an instrument in your house, and you'll have occasional apartment parties - in your spare time."
    th "I'm not going to tell you that you're probably going to have a very hard time, just like any pretty girl in the nineties at the dawn of wild capitalism, when women in the collective were at constant risk of harassment from the bosses."
    th "But not because I don't want to scare you, but because I hope that it's a different world and there just won't be the nineties I'm used to, and the girl Alisa, desperate to find a normal job, will not turn to the security services, where she will end her days as an assistant prosecutor, taking the bullet intended for her patron."
    th "Or drugs, the flood of «black» that poured across the border in '91. I mean, you're spinning in all that kitchen, the smoke column, «izh» with the chopper fork from the Harleys, the garage rehearsals... Fire under the spoon..."
    "Why would you want to know that, because there may well have never been a certain Boris Nikolayevich here, and Misha didn't get the Nobel Prize, and Lithuania never had enough hate to start spitting in the faces of Soviet soldiers."
    "After thinking about it for a while, I chose the most neutral option."
    me "So a career as a journalist would probably suit you - free schedule, in the newsroom by 11, constantly on the move, traveling all over the globe..."
    show dv surprise pioneer with dspr
    "Alisa snorted, but judging by the once enlarged pupils, the idea more than caught her."
    el "And me?"
    sl "And you're done eating and going outside."
    "Slavya declared in an unquestioning tone."
    me "Exactly. I don't know about you, but I claim a little shake at our disco-shake."
    "I stood up, setting the example, and Miku followed me up."
    mi "Well, me, me, Senechka, tell me!"
    "Not quite knowing whether she was mocking or serious, I put on my most mysterious expression on my face and in a grave voice began:"
    me "I see... I see the future! And you are in that future!"
    mi "Yes! Yes! What is it?"
    me "I see you going somewhere and carrying something!"
    "Miku is holding her breath."
    me "Oh, it's not «something», I can see badly, I got mixed up."
    mi "What, what is it?"
    me "It's «someone», not something!"
    "I bit the inside of my cheek."
    me "Yes. It's definitely a person..."
    mi "What person?"
    me "It's... It's me! You picked me up in your arms and you're carrying me!"
    show mi sad pioneer with dspr
    mi "Come on!"
    "Miku pouted and poked me in the side with her fist."
    mi "I ask him seriously, and he..."
    "No, of course that level of trust was more than flattering to me, but still!"
    me "Miku, honey. It's not like I'm Vanga or even a fortune teller."
    mi "So what! You've done a great job of telling Alisa!"
    me "Nothing great. Simple logic and a little common sense."
    mi "Then why don't you use your logic about me?"
    me "Let me think. Probably because you're at the dawn of your career and your popularity is just gaining momentum."
    me "Clearly not the way to the janitor, do you think?"
    show mi dontlike pioneer with dspr
    mi "Boo on you!"
    show dv guilty pioneer with dspr
    "She folded her arms across her chest and turned away. I had to hug and kiss her as a matter of urgency, ignoring Alisa's wince."
    "Slavya had already successfully carried the remains of the feast to the kitchen by this point, and we were free to go to camp and join in the festivities."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_dj_late_supper_un:
    scene bg int_dining_hall_sunset with dissolve
    play ambience ambience_dining_hall_empty fadein 4
    "The canteen was empty - last pioneers were scattering from the hall, men on duty were running around with carts, collecting forgotten dishes from the tables, and the cauldrons had been rolled away from the distribution."
    "Judging by the noise of the water, they were just now being soaked."
    me "Here we are."
    show mi sad pioneer with dspr
    mi "Huuuungry!"
    "Miku rubbed her tummy and looked at me pitifully."
    show un shy pioneer at left with dspr
    un "Actually, I have something at home..."
    $ alt_day6_mi_dj_feed = 'un'
    me "Like what?"
    un "Smoked chicken... Would you like some?"
    me "You ask! Of course we want it! I mean, I want it. And if Miku doesn't want it, it's her own fault!"
    show mi smile pioneer with dspr
    mi "You are our savior!"
    if alt_day5_mi_dj_hentai_done:
        show un grin pioneer with dspr
        un "This is the second time."
        me "And the first time, when you agreed with us on our portrait?"
        un "No, when gave you the shirt from the shoulder."
        th "I wonder if she has any idea..."
        dreamgirl "No. Of course she's not aware of such nonsense at all, dude."
        th "She already loaned us the shirt."
        me "It's not some shirt this time."
        "I hastened to get off the dangerous subject to the side."
        me "Now it's a whole hen of help!"
        show un smile pioneer with dspr
    mi "Where did you get it?"
    un "My father smokes it himself, he has some kind of recipe."
    un "Personally, I like it a lot, but..."
    "She sighed."
    un "There's not much time left, I just can't eat it all."
    me "Well, of course, we'll rush to save you and rid you of your extra supply of provisions! Lead on."
    show un laugh pioneer with dspr
    un "As you command!"
    play music music_list["lightness"] fadein 2
    scene bg ext_house_of_un_day with dissolve
    play ambience ambience_camp_center_evening fadein 2
    "Lena led us through the circular paths - so that no one caught us and no one made us work instead of our honestly earned dinner."
    stop ambience fadeout 1
    play sound sfx_door_squeak_light
    scene bg int_house_of_un_night
    with fade2
    play ambience ambience_int_cabin_night fadein 3
    show un normal pioneer with dspr
    un "Have a seat, I'll look for it."
    show mi normal pioneer at right with dissolve
    mi "I've had it all! But to go without supper - that's a first for me!"
    if alt_day5_mi_dj_hentai_done:
        me "But you're without breakfast..."
        mi "No breakfast doesn't count! I've often overslept myself!"
    un "There!"
    "A greasy newspaper roll was revealed to our eager eyes, exuding snotty smells!"
    "Just a little more, and I'll fly forward like that same Rocky Roquefort to the smell of well-flavored cheddar."
    "My mouth spontaneously filled with saliva, and I gulped and stared pleadingly at my hostess."
    show un laugh pioneer with dspr
    un "All right, you may proceed."
    "Laughing, she allowed it."
    me "What about..."
    un "I've got a whole packet of cookies, Got to use them up right away."
    "I don't think I'd trade a whole smoked chicken for some cookies, but the hostess seemed to know better."
    "As a bachelor to the bone, I spoiled myself with a grill from time to time, so I had my hand in the speedy carving of a chicken carcass."
    "Even the conditions were the same - on my knee, under the crosshairs of eager stares, hands shaking with anticipation."
    "Not a minute later we were chowing down on smoked meat."
    mi "Delicious! And it must be terribly unhealthy!"
    me "If you eat it all the time, probably. But spoiling yourself once every couple of months is probably okay."
    mi "I like suimono best out of chicken, but Pa swears that the damn Japanese have managed to screw up even something as simple as chicken broth."
    "I remembered what I was last served at Sorento's and agreed with the mysterious Pa."
    me "There's no such thing as taste or color friend."
    "I stated diplomatically."
    mi "No! It's chicken, what's the taste and color?"
    me "Go-{w=.3}od! I'm going to run out and get some soy sauce now. Can you imagine the combination with that flavor?"
    "Miku shrugged her shoulders."
    mi "I can! I'll eat anything with sauce!"
    th "Especially coffee and ice cream."
    me "Eat up, omnivorous."
    "I laughed, leaning on the chick. It was frighteningly small amount left - the reactive kid was scavenging everything."
    "Finally, in an unequal battle of jaws and smokes, the young, strong teeth prevailed."
    "Lena, who had finished her cookies by then, sat giggling quietly at us."
    "But I'm on a well-fed belly always kind, and Miku was just squirming with pleasure."
    me "Like all good things in life..."
    "With regret, I stated."
    me "Don't you have a spare chick?"
    show un laugh pioneer with dspr
    un "No! You've already consumed what I should have had for two days."
    me "Sad. Okay, let's wash up and go to the dance."
    mi "Can I... Can I not go? I'm right here on the cushion... Senechka, you're so warm, mrrr... Don't go."
    me "And you'll have chicken fat all over your pillow. Rise up, princess, great things await us. In particular, a three-hour disco under your keen guidance."
    "Miku sighed and got up."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_dj_discotheque:
    scene anim_square_preparty with fade2
    play music music_list["lightness"] fadein 5
    "Dance-dance, how sweet it is! Dance-dance, no break!"
    "«Car-Man» they'll start yelling that in a matter of years. {w}Or is it «Bachelor Party» and I got the words mixed up?"
    "Ah, doesn't matter."
    "So my entreaties for Miku to hurry off to her historic homeland are very much justified."
    "And I'm reminded of where yesterday's epic with the vocaloids, the camp searches, my reaction and everything else related even came from."
    "As a person far away from all this DJing, my acquaintance was more of a rudimentary one - in 2009, when we got the craze for the dancing cartoon girl, I only shrugged my shoulders and was glad for those who had found a new object of worship."
    "Then there was no word for a long time - the project was gaining a fan base, getting fat and muscular, people creative and, no doubt, genius, writing their texts - all in Japanese, for which, in fact, the synthesizer was created."
    "But Japanese or not, it doesn't matter when the conversation is conducted in an international, understandable language of music."
    "And at the end of 2011, I was literally won over by a video with light piano tunes that embodied the idea of that, the old Internet - erasing borders, language and cultural barriers, bringing people together."
    "And already there was this idea - of a united humanity, creating simply because sometimes it's as natural as breathing. Not for nothing did the final slogan sound like «The Creator is All of Us.»"
    "The music was in the popular semi-commercial lounge at a time, and I figured it was Moby once again giving something away to the order of some BMW. So the final Googlochrome moment came as a surprise to me. But none of that mattered."
    "There's a reason someone's world became infinitely-aquaamarine after all."
    "And there's a reason I didn't join the countless throngs of jerks waving glow sticks in the dark."
    "I probably wouldn't remember it now if it weren't for the intuition that has access to all my memory, pulling a five-year-old experience by the ear into the sun, the phrase «prayer song,» and how for a few days, while I played the thing a few hundred times in my player, my world almost turned color."
    "Though all of this, of course, is nonsense. Music shouldn't have that kind of influence on a person, otherwise it turns out that we're entrusting the keys to the subconscious to some unknown person, sitting somewhere in Japan right now."
    dreamgirl "Relax. The local Miku is just a girl with potential who writes her own songs. And if you play her something she saw in her dreams but didn't have time to put on the notes, you can be sure she'll blow up all the dance floors of Tokyo with another hit within a couple of months."
    "The counselor already stood behind the turntables, looking like she was doing us the greatest favor."
    show mi surprise pioneer with dissolve
    "Miku owed and blushed.{w=0.5}{nw}"
    hide mi with easeoutleft
    extend " — however, this did not stop her from turning around on the spot and running away."
    me "Miku! Where..."
    mi "The dress!"
    th "It seems my corrupting influence on the girl is a little stronger than I thought."
    "After all, for her to forget to dress up for the dance, something must have happened..."
    dreamgirl "Of your caliber."
    "Inner voice hinted."
    "Here I fully agreed and, pushing through the slowly gathering pioneers, took a seat next to the announcer's console."
    show mt normal dress with dissolve
    mt "Where is she going?"
    me "Forgot her dress, obviously."
    show mt smile dress with dspr
    mt "But she didn't forget to be late. Semyon, why are you teaching her bad things?"
    me "But I didn't..."
    "I started, before I realized that I was simply being teased."
    me "Will she make it before the opening?"
    mt "If she hurries..."
    "Olga Dmitrievna looked at her watch."
    mt "The dance doesn't start at nine o'clock exactly, we're not a factory here after all."
    show mt normal dress with dspr
    mt "But no one abolished responsibility!"
    "Responsibility, common sense - jargon from adult country. Let's not get all hot, bothered and rush to a place from which there is no return."
    dreamgirl "And you?"
    th "Well... I'm the exception."
    me "If you want, I can stand behind the console."
    mt "No, that's okay. There's still time, plus the speech."
    mt "But if she's late..."
    hide mt with dissolve
    scene anim_square_party
    with fade
    "Miku wasn't late. Or rather, she arrived in the nick of time."
    "Olga Dmitrievna was already finishing her pumping about the unbearable responsibility of pioneering, and cries about «responsible dancing» were coming little by little from the crowd."
    "She wore the same dress she had a couple of days before - and I involuntarily admired the way she walked, the way she {i}carried{/i} herself."
    show mi normal dress with dissolve
    mi "Hello, «Sovyonok»!"
    "Blew the speakers with her voice."
    mi "Farewell dancing, farewell supper - so much farewell, longing! As if we were burying someone!"
    mi "I have a better idea, let's have fun!"
    "Voice of the crowd, united by the general mood, sounded surprisingly harmonious - and I was surprised to find that I had added my own voice to it!"
    mi "Let's have fun so that we have something to remember later!"
    hide mi with dissolve
    play ambience ambience_7dl["disco"] fadein 5
    "She removed the hand holding back the record, and the first notes of a dance composition escaped into the evening air."
    "Last night's dance was a little more interesting than I had feared - though the music, frankly, was most questionable."
    "Well, I can't dance to Vizbor, yes!"
    "However, most of the pioneers were not embarrassed by this - not ten seconds passed and a spontaneous «brook» appeared on the dance floor, the crowd broke up into a dozen circles of dancers, some danced alone, purely for their pleasure - like the very same Ulyanka."
    "Some of the pioneers, like Electronik, stepped aside and danced outside the main movement - not too sure of their own choreography, but also eager to join in."
    "Some of them sat on the benches - no matter how you look at it, this is a camp-wide event, attendance is mandatory, and a healthy, sociable, positive homo-pioneerus could not think of not wanting to!"
    "And the counselor was walking around, jerking every such comrade - no sooner had the first track on the current playlist closed than Alisa came up from the bench, followed by Lena - after all, Olga was the real professional."
    stop music fadeout 3
    if alt_day6_mi_dj_walkman:
        "The next song surprised me a little - it sounded so familiar."
        dreamgirl "And that's no surprise, because you listened to it at least once a week."
        th "Where?"
        dreamgirl "In your headphones."
    else:
        "The first five dances - fifteen minutes - are warm-up dances. The audience needs time to get used to the dance floor and loosen up a little bit."
        "To just stop being shy."
        "And then, when there is no trace of shyness and, responding to the selfless hand-waving, the brain gives the command to inject endorphin into the blood, the DJ, sensitively feeling this moment, launches the first slow dance."
    play music music_list["waltz_of_doubts"] fadein 3
    "The melancholy first chords floated over the square."
    "Of course I didn't dance-I'm not much of a dancer, and only on what I'd managed to learn in my restless youth."
    "But somehow it happened that I was never taught how to behave on the dance floor. When I was young, I danced at my own pleasure: I managed to learn a couple of fancy moves - that's fine; didn't manage it - the hell with it."
    "That's the dance, actually."
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_dj_first_dance:
    scene anim_square_party with dspr
    "But in this case, when you didn't have to bend around like you don't know what for - but provided a perfectly legal way to cuddle with a pretty girl on the dance floor, I'm not going to hesitate for a second."
    "I wasn't afraid of Miku anymore. Not afraid anymore."
    "Though rejecting from her sid was still more than likely - DJ lady, after all, not the last face on the dance floor."
    show mi normal dress with dissolve
    me "Shall we dance, beautiful?"
    "She whispered something to Slavya standing next to her and nodded to me:"
    show mi smile dress with dspr
    mi "Of course!"
    "Miku didn't hesitate for a second - an extra penny in the piggy bank of my helpfulness."
    "Slavya substituted for her at the turntables, letting the host wiggle out from behind the table and come closer to me."
    me "Ready?"
    mi "Sure! Let's dance!"
    "I tried to woo the girl a little, but she didn't seem to have time for nonsense - instead she dragged me along on her own, squeezing my hand tightly."
    mi "Hurry up!"
    "She flared me up."
    mi "The song will be over soon, and I still want to dance with you!"
    "She stopped at some inexplicably feng-shui chosen spot so that I almost bumped into her, and, turning around, immediately purred, running both her hands over my shoulders."
    "I belatedly remembered that the more familiar dance, rather than something waltz-like, came from over there, from the east."
    scene cg d3_mi_dance_afar_7dl
    with fade2
    "A few steps to get used to each other, a few more to discuss the many «may I» and finally we choose the distance we've allowed ourselves."
    "Miku is by my side. She's in my arms. Close, close."
    "She's smiling, looking askew, a little lower, and her eyes are almost completely full of pupil - they're black."
    "And it makes a frozen sparkle somewhere between my shoulder blades, and takes my breath away with the sweet anticipation of the inevitable miracle."
    "Us. Together."
    me "That dress looks great on you after all."
    "I finally broke the silence."
    mi "Yeah? I don't know. I actually wanted to get something from the stage costumes. At least my usual «cyber suit»."
    mi "Can you imagine what would have happened here?"
    me "Yeah, you would have caused quite a sensation here!"
    mi "Well, who knew you couldn't have a mid-thigh dress!"
    me "And you're right that they're forbidden!"
    th "Such beauty should belong to me alone!"
    mi "What are you talking about?"
    me "That their length is too personal for me! If you want to wear something like that, wear it, but only for me. In retaliation, I pledge to wear your kimonos, or whatever you honorable men wear..."
    "Thin fingers run down my shoulders, dispersing stale blood with goosebumps."
    mi "You just say all these things. You won't remember any of them."
    dreamgirl "Sure he will!"
    me "Miku... Have I ever let you down once?"
    mi "Yes!"
    me "Except for my shock yesterday."
    mi "Well... I don't know."
    "As she snuggled up to me, the Japanese girl kissed my cheekbone."
    mi "I want to do everything I can to just make you smile more often, Senechka."
    me "And I... For you."
    scene anim_square_party
    show mi serious dress
    with dissolve
    "Miku twisted out of my arms."
    mi "But I have the next song in fifteen seconds, Slavya will kill me if I'm not on the spot."
    me "Wait! Let's run away!"
    show mi upset dress with dspr
    stop music fadeout 3
    mi "Not now. Let's do it after ten o'clock! After the second dance. Slavya promised to change me."
    show mi smile dress with dspr
    hide mi with easeoutleft
    "After giving me an air kiss, girl ran away."
    play ambience ambience_7dl["disco"] fadein 5
    play music music_7dl["beat_symphonic"] fadein 3
    "And, in perfect accordance with her words, fifteen seconds later a fast song began to play."
    "And I went back to the bench, to await the next dance."
    $ persistent.sprite_time = "night"
    $ night_time()
    scene cg d3_disco with dissolve
    with dissolve
    "That moment when the perception of time is turned off completely, and you are surprised to hear the horn sounding for the bail, the announcement of the last dance, or the alarm clock beeping, not believing yourself, and checking the time."
    "And yes - two hours of your life just dropped out of it. Two extremely fulfilling, extremely enjoyable and fun hours."
    "The brain is shutting down, allowing the body to enjoy itself - and perhaps, it's closer to nighttime, when the body goes into exotic bedtime mode and hasn't had time to waste any energy yet."
    "I sat on the bench, fleetingly searching for familiar faces in the raging crowd."
    "There to the left of Genda was Elektronik dancing, now and then casting glances to the side - I followed - into the place where Zhenya was sulking on the bench."
    "Ulyanka, of course, was dancing in the thick of it, literally bathed in the euphoria that any organized group of people exudes - such as dancing. Or watching a concert. Or marching in a parade - however, local society made a person feel like an animal social in a far greater number of ways."
    "Slavya danced close to Miku, ready to fill in if necessary, to come to the rescue - you name it. So you could tell that Slavya was more vigilant than entertained."
    "Next to her Olga Dmitrievna was vigilant, too, just as I was, looking around with a keen eye. Except that she managed to combine it with dancing - which I was not a big fan of."
    "On the far bench huddled Lena and Alisa, who had gotten a deck of cards and were playing durak, stomping to the beat."
    "And just like at the last disco, all this knowledge went into my head, bypassing the subconscious and the rational part - just for a moment I felt a unity with these personalities, a kind of magical oneness that is not usually remembered in everyday life."
    "Miku caught my gaze and winked."
    "Her look promised that I would not get away with one dance."
    stop music fadeout 3
    "And rightly so - not half an hour later, the fast music was replaced by the pensive chords of the piano, and the running, jumping, and hands-waving, which had acquired a kind of organization, broke down - people calmed down and thought about how to spend the slow dance time."
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_dj_second_dance:
    scene anim_square_party with dissolve
    play ambience ambience_camp_center_evening fadein 2
    "I started pushing my way to the table."
    if alt_day6_mi_dj_sl_evil:
        "When I came to the table, Miku was arguing with Slavya in a low voice."
        show mi normal dress at left
        show sl normal dress
        with dissolve
        "Both went silent as I approached and looked at me in a way that made me feel superfluous."
        me "What's all the commotion and no fight?"
        sl "There's no fight and there won't be. I'm just leaving. And I'm not filling in for Miku."
        me "But why? What's the problem?"
        show mi serious dress with dspr
        mi "She doesn't want to. And, accordingly, the second half of the dance is also for me to lead."
        me "Slavya?"
        show sl shy dress with dspr
        sl "Without going into detail, Boris Alexandrovich punctured his leg with something. A counselor and I are transporting him to the infirmary. {w}I don't know how long we'll stay there."
        me "Really? His leg?"
        "Slavya shrugged her shoulders."
        sl "I have no reason to lie to you. So I'm very sorry if I suddenly upset any plans for you, but I have to leave."
        hide sl with dissolve
        "She said goodbye with a nod and headed for the benches."
        me "So you're not going dancing?"
        mi "I'm sorry, Senechkaa."
        "Miku lowered her head."
        me "That's all right. Lead your own dance. Do you want me to sit next to you?"
        mi "No, don't. You'll distract me. You'd better go dancing."
        me "But what about us... I wanted to cheer you up and everything..."
        show mi normal dress with dspr
        if lp_mi >= 19:
            "Here's an idea that occurred to me:"
            me "How about we harness Electronik? For one dance?"
            "After thinking about it, Miku nodded."
        else:
            mi "Sen. It's okay. Just don't be a pain in... Okay? Let me come to my senses."
            "Finding it prudent to heed the advice, I went back to my bench."
            "Looks like Miku is in a pretty bad mood."
        hide mi with dissolve
    elif alt_day5_mi_dj_apology == 2:
        "And then a sharp pain pierced my arm."
        show us smile dress at zenterleft
        with flash_red
        us "Hey! Dance with me!"
        th "She's got to be kidding!"
        "Her fingers were still clinging to my palm."
        "To the cut!"
        me "Silly child! Can't you see where you're grabbing?"
        show us shy dress with dissolve
        us "No, why?"
        me "For the band-aid! Let go of my arm, it hurts!"
        "Ulyana pouted and let go of her hand."
        me "Thanks."
        "Ulyana didn't answer."
        me "Hey, are you offended?"
        show us sad dress with dspr
        us "Piss off."
        me "Look, do you know how much it hurt? I got a cut there."
        show us cry2 dress with dspr
        us "I got it, I got it! Don't want to dance with the kids - just say so!"
        us "Slowpoke!" with flash_red
        hide us with dissolve
        "She kicked me under the knee and ran away."
        if lp_mi >= 19:
            "However, despite this incident, I continued on my way to the DJ table."
        else:
            "Of course, dancing was out of the question; I had to sit back down on the bench, ignoring Miku's puzzled look."
            "She seemed a little offended."
    elif alt_day6_mi_dj_un_evil:
        "Didn't get very far, though."
        "After taking a few steps, I found myself near a bench where the girls were playing cards."
        "Before I knew it, someone's foot was in my way in the dark."
        play sound sfx_fall_wood_floor
        with vpunch
        "I fell flat, and if it hadn't been for my timely hands, I would have gotten an acute attack of asphalt disease halfway across my face."
        "But now I wouldn't even pay attention to such a little thing - so angry I was."
        "Immediately jumping up, I pointed an accusing finger at the smirking face framed in red hair. {w}I almost hated her now."
        me "You! What are you doing?"
        show dv laugh pioneer with dspr
        dv "What's the matter? Did our valiant cavalier get tangled up in his spurs?"
        "Lena, pulling a tight smile over her lips, instantly stepped back."
        "Alisa's voice was frankly mocking, her eyes narrowed and her lips folded into a sarcastic smirk."
        "I wanted to punch my fist into those lips with all my might, causing them to shatter into mirrored shards."
        "Bring my hands together around her neck and press with my thumbs, shaking the sneer out of her amber eyes."
        hide dv with dissolve
        if lp_mi >= 19:
            "Too much effort!"
            "After shaking it off, I got up and continued on my way to the presenter's table."
        else:
            "And that's because, with what my parade outfit had turned into, the most you could do was sweep the place up after the others had danced."
            "Going out looking like that to invite a DJ was out of the question."
            "Cursing, I got up and followed a flock of boys hurrying to freshen up at the nearest water pump."
    elif lp_mi < 19:
        "Miku said she wouldn't mind running away. So I didn't even have any doubts about who to call for a slow dance."
        "So I went up to her, stretching out in a straight line."
        show mi normal dress with dissolve
        me "Mademoiselle?"
        mi "Yes?"
        me "Shall we go?"
        "I nodded to the dance floor."
        "And I even almost started to hold out my hand when I was suddenly stunned."
        show mi upset dress with dspr
        mi "Sorry, Senya, but not this time."
        me "Why?"
        mi "Because... Because I don't want to!"
        me "Is there something wrong with me?"
        "I took a cursory look at my clothes - externally everything was fine. I don't seem to be exuding stink either."
        me "What's wrong?"
        show mi serious dress with dspr
        mi "Nothing. Can you take my word for it that I just don't want to dance?"
        $ alt_day6_mi_dj_rejected = True
        me "No. How can you not want to dance, dancing is music, it's your life."
        mi "Not this time."
        me "Do you not want to dance in general or specifically with me?"
        "Miku shrugged her shoulders."
        me "I see."
        "It felt like I'd been punched in the head with something heavy - there was an icy vacuum between my temples, and I couldn't think about anything at all."
        "Keeping unnaturally straight, I briefly indicated a bow - a nod, more like:"
        me "Okay."
        "I agreed. And, not knowing what else to say, added:"
        me "Be."
        hide mi with dissolve
        "Turned over to the right shoulder and made my way to the benches under the crossed gazes - as under the footlights - of the whole camp, it seemed."
        "Voices whispered, pushed, and hung on their feet with an unbearable weight: «Look! Look! Here he comes. Loser. The girl turned him down. Because he's a loser»."
        "It was very hard to walk - and probably would have been easier if I hadn't felt the escorting stare on my shoulder blades."
        th "She blew me off."
        "Frenziedly, I thought."
        th "Dropped me off and shamed me all over camp. Watching for reactions."
        dreamgirl "Look on the bright side, man."
        th "What good can there be in a friendzone?!"
        dreamgirl "After all, she didn't do it hands-free. Can you imagine what would have happened if she had plugged in a microphone?"
        th "Oh, well, that's the only consolation. Although on the scale of the dance floor..."
        dreamgirl "I assure you, behind the music, few people heard anything. Most probably thought you went to the hostess to order some music, so let's support them in that illusion."
        th "Who needs it?"
        dreamgirl "Us, first of all! So up high! Chest up, tail out."
        dreamgirl "You'll cry about it into your pillow at night - not the first time."
        "Yeah, this camp was no exception either."
        "I huddled in the farthest corner and sat on a bench."
        stop music
    elif lp_mi >= 19:
        play music music_7dl["stilllovingyou"] fadein 5
        "Magic music."
        "Scorps started my acquaintance with really good ballads, and with them my childhood swept by hand - the best slow tunes, the most memorable stories - bittersweet, romantic, memorable..."
        "The brightest."
        "And this song is almost my age!"
        "And Random himself told me to ask my girlfriend to dance to this song."
        "I really wanted to ask her, really... I was drawn to her."
        $ volume(0.5, 'music')
        play sound sfx_7dl["wakeup"]
        "But whether it was someone else's voice or something else that cut the perception with a freshly bred association, I felt creepy and {i}unreal{/i} again."
        menu:
            "Pretend that everything is fine":
                $ volume(1.0, 'music')
                show mi normal dress with dissolve
                me "May I invite you in?"
                "Miku exchanged glances with Slavya propping Genda up and rose from the console."
                mi "You may!"
                me "Then..."
                "I held out my hand to her."
                with flash
            "Fight the fear":
                $ volume(1.0, 'music')
                if dr:
                    play music music_7dl["unholy_you"] fadein 3
                elif loki:
                    play music music_7dl["laugh_throught_the_universe"] fadein 3
                elif herc:
                    play music "<to 52.94>" + music_7dl["herc_death"] fadein 3
                $ alt_day6_mi_dj_me_evil = True
                "I clenched my teeth as hard as I could, my nails digging painfully into the skin of my palms."
                with fade
                "The world staggered, but it held."
                "And again."
                me "Hell, no."
                "I grumbled angrily, looking at my surroundings with distaste."
                "Spread my legs wide, took a deep breath."
                "And took the fight."
                "It actually looked a lot more pathetic than that."
                "I just turned pale and green and hung on Genda's pedestal, the only relatively immutable object here."
                dreamgirl "Give me a fulcrum, and I'll lean on it."
                th "Shut up."
                scene anim_square_party
                show mi normal dress
                with dissolve
                mi "Senechka? What's wrong with you?"
                "There's Miku."
                "I gulped down the stiff, bitter saliva, though I really wanted to spit."
                "For some reason it was very uncomfortable for her to see me like this."
                me "Everything..."
                "The voice trailed off, and I waved my palm, trying to show her that everything was okay."
                "But who would I fool with my pantomime if even my hands were pale, with a distinct greenish hue."
                show mi upset dress with dissolve
                mi "Where's your «everything»!"
                "She fluttered her arms."
                mi "Standing there like you saw a ghost. What happened?"
                "I was sullenly silent, and she guessed it herself. She spluttered her hands:"
                show mi serious dress with dissolve
                mi "Vocaloid thing again?"
                th "And that too, but much worse:"
                if loki:
                    "Feels like there was a hole inside me and snow was falling into it."
                elif herc:
                    "The feeling of a cold, wet floor under the back of my head."
                else:
                    "It's a condition I can barely fight - it's as if water is already splashing in my lungs."
                me "I'm sorry."
                "I was very, very embarrassed, wanting to bang properly on the proverbial pedestal, but instead I slid down it onto the steps."
                "And immediately I felt warm skinny hands on my shoulders, lips touching my forehead."
                mi "Poor, poor Senechka."
                th "Wild situation: I'm hysterical, and I'm comforted by a girl."
                "She hugged me and stroked my head, no longer even thinking about silly things like dancing."
                "If there was ever a worm in my head about her realness..."
                "She was too worried."
                me "I'm sorry."
                "I mumbled to the side."
                me "It was so silly, and I thought I was dancing with you."
                mi "It's okay, we'll dance sometime later."
                "She brushed me off carelessly."
                mi "Shouldn't I call Dr. Viola?"
                me "No, it'll pass. We should sit down, get some air."
                mi "Okay."
                "Miku was unaccustomedly short-tempered, and I was well aware of what might be the reason for that."
                "And aside from the fact that I peeled the crust off yesterday's barely healed wound."
                "Which only I could have done."
                "And only her, with her identity crisis."
                show mi normal dress with dissolve
                mi "You just sit there until it goes away, okay?"
                "Miku cast a worried glance toward the table."
                mi "And I'm having a song change."
                "I waved my palm, letting her go."
                hide mi with dissolve
                "And he was left alone, alone with his shame."
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_dj_dance2_fail:
    scene anim_square_party with dissolve
    play music music_list["two_glasses_of_melancholy"] fadein 3
    if alt_day6_mi_dj_sl_evil:
        th "Miku doesn't love me. Maybe she even hates me."
        th "Or is she sick of me? How come, she told me to sit somewhere else and not bother her."
        "Something like that, I guess I was under the impression I was expecting."
        "Since I wasn't the least bit surprised. Yes, I stayed out of her way all evening, yes, I only appeared twice - but I could be seen on the bench where I waited my turn."
        "Slavya let us down."
        "Though, of course, you can count on Slavya, but yourself..."
        me "Damn Murphy and his idiotic laws."
        $renpy.notify('«Went wherever I could see» - Went in a random direction.')
        "I angrily kicked a lump that had fallen under my feet, and before I reached the benches a couple of meters away, I turned around and went wherever I could see."
    elif alt_day5_mi_dj_apology == 2:
        "Miku was really offended."
        "Plus she whispered something to Ulyanka. I don't know exactly what, but it certainly didn't add to my score."
        "So I sat on the bench for the next slow dance. Just like all the fast ones."
        "To tell you the truth, I've lost count of how long I sat like that, staring at my feet. Didn't look at my phone, didn't count the songs."
        $renpy.notify('«Went wherever I could see» - Went in a random direction.')
        "I turned around and went wherever I could see."
    elif alt_day6_mi_dj_un_evil:
        "After I got my turn, after I washed my shirt and wiped off my shorts, there was about half an hour before lights out."
        "Just enough time to go out and dry off."
        "Or crack my head against the wall."
        $renpy.notify('«Went wherever I could see» - Went in a random direction.')
        "With a sigh, I pulled on my wet shirt and went wherever I could see."
    elif alt_day6_mi_dj_me_evil:
        "Half strangled fear reared its head again."
        "I honestly thought we were done, come on! The point of no return has been passed, the right wire has been cut, and Ever After country has opened its arms to us."
        "Like hell it has."
        "Want to make The Creator laugh - share your plans with him."
        "I was ashamed to look Miku in the eyes, embarrassed to catch the stares of those around me who had witnessed my belated seizure."
        "That's why I left."
    stop music
    play music music_7dl["unforgotten"] fadein 6
    scene black with dissolve
    "How long I walked is unknown; I seem to have walked in circles, not thinking about anything at all."
    "My vision narrowed to a minimum, leaving only a few centimeters of concrete slabs in my view - I was shelled and withdrawn."
    "Miku stayed there and I stayed here."
    "Straight ahead fifty meters, turn left another thirty meters, turn left two hundred meters, fork..."
    "I was moving along the paved paths - not by myself, no, my feet were picking my way. But at some point I realized that I had seen this particular slab with a scratched out middle maybe five times before."
    return

label alt_day6_mi_dj_catapult:
    scene bg ext_warehouse_night_7dl with dissolve
    "And then they called out to me."
    sl "Semyon!"
    "I looked up."
    show sl normal dress far with dissolve
    "Slavya."
    me "Yes, what did you want?"
    sl "We need to talk."
    th "Wow. This is so serious. I think I'll put that phrase on a par with «can I ask you a personal question?» and «I'm doing this for your own good.»"
    me "And {i}we{/i}."
    "I underlined the last word, firmly doubting the existence of any «we»."
    me "Have anything to talk about?"
    sl "Yes, Semyon."
    show sl normal dress with dissolve
    "Slavya came closer."
    sl "I want to talk about your home world."
    play sound sfx_wind_gust
    with fade2
    "As they say on such occasions - and then a chill ran down my spine."
    "Where I stood, I sat - on the very comfortable steps at the end of the warehouse."
    me "What, the legend of the ambassador's child doesn't suit you?"
    "I smiled weakly."
    "Knowing full well that I was giving myself away with such a reaction."
    "A normal person would have laughed at the poor blonde, mocked her to death, and only then would have handed her over to the orderlies."
    "Maybe even spit in her eye as a preventative measure."
    "I'm sitting here talking in a shaky voice."
    if alt_day6_mi_dj_sl_evil:
        sl "Yes, I know who and what you are."
        me "Oh, yeah? Did Sanich whisper it in your ear while you were ramming him to the infirmary? Or did Viola tell you?"
        sl "Don't kidding around. I was looking for you to make an agreement."
        me "That sounds loud."
        sl "All right, let's do it in your language."
        "Slavya patiently, as with a retard, lowered her voice and smiled."
        sl "I'm offering you a deal."
        me "A deal."
        sl "Yes. I know you are not of this world - not of this place, and as I have watched you, I have come to the conclusion that you are also not of this time. It's all wild to you around here."
        me "I don't see a deal here."
        "Slavya sighed."
        sl "The deal is this - I tell you how to get out of here..."
        me "And in return?"
        show sl smile2 dress with dspr
        sl "It's obvious. In return, I want you to take me with you. To get back to your world, you have to..."
    else:
        sl "I can guess who you are and how you got here."
        "She came very close and threw her arm out sharply in my direction."
        "Prepared for a penetrating stabbing, I stood there stalling for a few seconds before I finally guessed that the girl was holding something out to me in the open palm of her hand."
        "Some kind of paper."
        me "What is it?"
        sl "A pamphlet."
        "The lofty title, «What to Do If Your Child Has PCR Syndrome,» by V.C. Collider made me swallow convulsively."
        me "So?"
        sl "Keep it, you can read it later at your leisure."
        sl "But in a nutshell, it's about people like you. Aliens from another world. Or rather, from other worlds."
        sl "You didn't think you were an isolated case, did you?"
        th "Wow, doesn't miss an opportunity to hurt me here, either. Bitch."
        dreamgirl "And you're hurt? Buddy, I've been trying to get it into your head for six days that you're just an ordinary moron and not very bright, and now you believe it with one word from a girl!"
        me "And?"
        show sl shy dress with dspr
        sl "I see you now have someone to stay with us... as a guest."
        sl "Listen carefully. In order to linger, to establish yourself here, you need..."
    me "What makes you think you know what I need?"
    "I tried to say it caustically, with anger, but it came out terribly indifferent. It was as if I wasn't sure what I needed anymore myself."
    "Have I really lost myself that much?"
    sl "I don't know. That's why I'm asking you to decide right now."
    "I felt like turning around and leaving - just to spite that clingy girl."
    "However..."
    th "I can get home! What do you think?"
    dreamgirl "The thought is curious. But the question is, how will you pay for the fare?"
    th "What do you mean?"
    dreamgirl "Miku."
    dreamgirl "She stays here. And you will go home. Back there, to the monitor and the unwashed apartment. Without Miku."
    th "So no advice?"
    dreamgirl "Sorry, I'm just your subconscious. I don't care about your loves at all."
    dreamgirl "You have to decide for yourself, man."
    "Yourself."
    "As usual, at the crossroads, at the 40-degree slope, at the point of no return, I stand alone."
    "And I simply have no one to advise me."
    "Staying here - no hopes, no papers, no education..."
    "Bare-assed in the face of the wild nineties, facing the prospect of settling in a society alien to me and the potential career peak of some janitor."
    "If at least something goes wrong..."
    "Or leave - where I at least represent something of myself, and now, after all I've been through here, after I've realized I'm not hopeless, as if pressing «restart»..."
    th "But there won't be Miku. In my world she is a program."
    dreamgirl "Are you one hundred percent sure of that?"
    "The inner voice inquired ingratiatingly."
    "The problem was also that I'd have to trust these two - from which goodness was already plentiful, but assuming for a second that Slavya had agreed to participate in the prank as the «good cop»..."
    "And my consent would not only automatically make me look like an idiot, it would also..."
    menu:
        "Stay":
            $ alt_day6_mi_dj_catapult = 1
            "For all other things, Miku herself pulled any equality to her side."
            "I can do anything and everything, but I can't seem to think of myself without her."
            "And that's in one week."
            "I don't know where we'll be tomorrow or what will happen after we get to the district center, where her father's executive car will be waiting for us."
            "The most important thing is that she is there, she is alive and real."
            me "Slavya, I don't know what kind of prank this is, but I'm not amused at all."
            "To tell you the truth, the phrase «I don't know what kind of dope you're on» was begging to be said, but the average pioneer has no way of knowing."
            me "So let's make a deal - you mocked and, satisfied, you leave me alone."
            show sl serious dress with dspr
            sl "So you really do need her more than I thought."
            "Sadly concluded the activist and turned, melting into the darkness."
            hide sl with dissolve
            "And I got a pretty good opportunity to freeze my kidneys sitting on the cold and think hard about what I just did."
            dreamgirl "You know, it's not too late to take it all back. And if she talks about it like it's not hard, you can bounce back and forth between worlds."
            th "What if it's not complicated just because I'm on a rubber band, holding on to something here, and it's up to me to see if the rubber band breaks, leaving me here forever, or if it brings me home, turning what's happening into a dream?"
            dreamgirl "You're a pessimist."
            th "Realist. Practice shows that it's the worst-case scenario that most often comes true. If I rush back, it will be as if I threw my ticket to happiness in small shreds to some higher power that threw me here, right in it's face - say, choke on your camps, I'll do without handouts."
            play sound sfx_slavya_run fadein 1
            "I didn't have time to think about the threat of this neglect of gifts before the sound of approaching footsteps caught my attention."
            "Someone was running - and, judging by their uncertain footsteps, they could see in the dark even worse than I could."
            "I must say, the warehouse was certainly popular today."
            show mi upset dress with dissolve
            "Miku?"
            me "Abandoned your post?"
            "Came a voice from my seat."
            "She flinched and stopped."
            me "Irresponsible."
            mi "Sem, you?"
            "I only shrugged my shoulders."
            me "Were you expecting to meet someone else here?"
            mi "No, ah... Where are you?"
            "She was on her way to the voice, but she looked like she was going to miss me."
            me "Here I am."
            "In the darkness, the backlight of the phone screen served as a guiding star for the girl - not two seconds later she threw herself on my chest."
            mi "You were gone... And Slavya followed you... I was afraid I would never meet you again."
            me "What are you talking about?"
            show mi serious dress with dspr
            mi "I remember what you told me about yourself... I don't know how Slavya found out, but..."
            "Miku sobbed without raising her head."
            mi "It got so scary that I ran right after you..."
            me "But we had agreed to stay together... I couldn't deceive you."
            if alt_day6_mi_dj_sl_evil or alt_day6_mi_dj_rejected:
                mi "But after all, after I refused to dance with you..."
                "I embraced this foolish creature who thinks that simply refusing to dance can make a promise a meaningless shake of the air."
                "I even considered taking a little offense at that assessment, but there was decidedly no rush right now."
            me "Besides... You're not there, you know? All right, I don't care if nobody wants me there - I'm used to it, and I'll shake it off and wipe my face, I've done it before."
            me "But you're not there."
            me "And I'm no good without you."
            "Miku didn't answer, hiding her eyes - though after looking for me in the dark, she had absolutely nothing to be embarrassed or ashamed of - that act said a lot more than some dance."
            me "You know, let's go back to the disco, or she won't finish herself."
            mi "Sen... What time is it?"
            "The smartphone showed the beginning of one."
            mi "Yeah. The disco's already over."
            me "Home, then?"
            "The girl nodded and bravely suggested:"
            mi "Drive! Because I... I can't see anything."
            scene bg ext_house_of_un_night_7dl
            with dissolve
            play music music_list["a_promise_from_distant_days"] fadein 5
            play ambience ambience_camp_center_night fadein 1
            show mi normal dress with dissolve
            me "We're here."
            mi "Yes..."
            "Miku was thinking and clearly had something to tell me."
            "Probably something important - I don't know."
            "She never made up her mind."
            mi "Good night."
            "My lips touched soft lips."
            mi "And thank you... For being you."
            play sound sfx_open_dooor_campus_1
            hide mi with dissolve
            "The door creaked, letting the girl into the cabin."
            "She didn't turn around on the doorstep, didn't wave."
            "Bad sign? What if she didn't care?"
            "Good sign? Suddenly she's so sure of me that she won't even say goodbye?"
            "Determined not to get too stupid, I headed for my cabin."
            "The evening was supposed to be languid and warm. It turned out to be... It turned out to be a lot of running around and a incomprehensible talking."
        "Leave!":
            $ alt_day6_mi_dj_catapult = 2
            "After all, what have I got to lose?"
            "I'm used to feeling like an idiot."
            "At worst, I'll be laughed at by someone whose opinion I don't care about."
            "And at best..."
            if alt_day5_mi_dj_voyeur == 4 and (alt_day5_mi_dj_apology in (0, 3)):
                "Where were we supposed to meet there?"
                "I patted my pockets, and one of them gave off a paper crunch."
                "A sort of stop-cock for the moment when I'm drawn back into the maelstrom."
            th "The old compass is aligned, and darned on the sturdy... something darned there yes."
            "There's no turning back, maybe we'll have better luck in the new place."
            me "Okay, I'm ready. If you tell me how to get out of here, I'll take you and all your luggage with me."
            play music music_list["you_lost_me"] fadein 3
            sl "All you have to do is desire it."
            "I couldn't believe my ears."
            me "What are you talking about?"
            sl "I'm serious! You just have to picture the last place you remember clearly and in detail, and that's it."
            sl "And want to go back. That's it."
            me "That doesn't make any sense."
            "Tales of the afterlife, corridors and voices were going through my head - I always wondered where does it come from. Those who had been safely carried off into the afterlife could not, for obvious reasons, be heard. And those who were pumped out... It's quite likely that they were just glitches."
            me "What makes you think I have to imagine and desire something there? Why, for example, shouldn't I jump up three times on my left foot, holding myself with my right hand by my left ear?"
            show sl serious dress with dspr
            sl "I don't think it works like that."
            me "And I don't think all that nonsense about presenting something out there is works like that too."
            sl "You know, why don't you just try it, and if it doesn't work, then we'll just pretend this conversation never happened?"
            "I think the case here was a tough one. It was easier to do as she wanted than to explain why not."
            me "Whatever you say."
            "I sighed."
            me "What do I do?"
            sl "Close your eyes."
            show blink
            scene black
            with fade
            "Feeling like an idiot - habitual by now - I obeyed."
            me "Next?"
            sl "Next - imagine. What's the last thing you remember before you got here."
            th "Imagine? Hmm..."
            "I diligently reconstructed before my eyes..."
            $ prolog_time()
            scene
            $ renpy.show("bg int_intro_liaz_7dl", what = Dawn("bg int_intro_liaz_7dl"))
            show anim_grain
            with fade
            voice "Take my hand in case it works out."
            "It couldn't get any worse, so I obediently held out my hand."
            voice "Now add detail to the picture."
            stop ambience
            voice "Sounds."
            play sound_loop sfx_bus_interior_moving fadein 4
            voice "Feelings."
            if loki:
                "For a moment I felt cold - snow-covered bench, the snow falling on my face, the pain in every cell of my body..."
            elif herc:
                "For a brief moment I felt a sharp pain in my forehead, caught the smell of gunpowder in the air..."
            else:
                "For a moment I was cold - icy seat, the ice patterned window, the steam escaping from my mouth as I exhaled..."
            voice "And…"
            play sound sfx_head_heartbeat
            voice "Open your eyes!"
            voice "Wake up!"
            "At the sudden harsh voice, I obeyed."
            if alt_day6_mi_dj_rejected:
                $ alt_day_catapult = True
                $ prolog_time()
                if loki:
                    play music "<to 52.94>" + music_7dl["herc_death"] fadein 5
                    show blink  with dissolve
                    scene bg ext_winterpark_7dl
                    pause(1.5)
                    "We were thrown back to the beginning of the story."
                    "Back where the fairy tale girl took me to dreamland."
                    "She blew me off."
                    "And I betrayed her."
                    show prologue_dream
                    "We are definitely worth each other."
                    scene bg ext_winterpark_7dl with flash
                    "I exhaled frosty steam and immediately coughed."
                    "My throat was flooded with blood."
                    th "But where is Slavya? She was holding my hand so diligently."
                    th "Where is she?"
                    scene cg d7_sl_gonna_be_ok_7dl
                    show ldb_blind
                    with fade2
                    "The icy cold took me in its arms."
                    "And I stopped resisting."
                    "Stopped living."
                    with fade2
                    th "Miku... goodbye..."
                    play sound sfx_7dl["aunl"]
                    $ sdl_persistent_inc("alt_lamp")
                    show acm_logo_va_lamp with moveinright:
                        pos (1600, 1020)
                    pause(7.4)
                elif herc:
                    scene bg int_store_7dl with fade
                    "I traded my chance at happiness and life for a return ticket."
                    "Yes, I am a fool. And the fact that I forgot about this unimportant incident doesn't excuse me."
                    "My God, you've had your time rolled back, your teenage dream fulfilled - take it, eat it, love it, with the experience of a thirty-year-old man to pioneer childhood!"
                    "And for what, I ask you? For Zinka? A job as a security guard?"
                    show prologue_dream
                    "For the sake of a joyless and hopeless existence?"
                    "For the sake of a bullet in my head."
                    play sound sfx_7dl["makarych"] fadein 0
                    scene black with fade
                    "Meeting place cannot be changed - Zinka, a drunk with a gun, and me with a hole in my head."
                    "And even the fact that I didn't come back alone didn't change a thing."
                    play sound sfx_bodyfall_1
                    stop sound_loop fadeout 0
                    play sound sfx_7dl["aunl"]
                    $ sdl_persistent_inc("alt_lamp")
                    show acm_logo_va_lamp with moveinright:
                        pos (1600, 1020)
                    pause(7.4)
                else:
                    scene black with fade
                    $ volume(0.5, 'music')
                    scene bg intro_xx with dissolve
                    stop ambience fadeout 2
                    play sound_loop sfx_bus_interior_moving fadein 4
                    show prologue_dream
                    "Reality shifted."
                    "And I exhaled..."
                    show prologue_dream
                    "Frosty steam!"
                    "I found myself at home. Home?"
                    scene bg intro_xx with flash
                    "All on the same bus where this whole journey began."
                    "It seems..."
                    "We did it!"
                    "Better that than..."
                    "I didn't have time to think about it."
                    scene black with fade
                    play sound sfx_water_emerge
                    "The bus skidded - broke the railing of the bridge, plunging fifteen meters into the icy, black water."
                    play sound sfx_7dl["aunl"]
                    $ sdl_persistent_inc("alt_lamp")
                    show acm_logo_va_lamp with moveinright:
                        pos (1600, 1020)
                    pause(7.4)
            else:
                $ night_time()
                scene bg ext_warehouse_night_7dl
                play ambience ambience_camp_center_night fadein 1
                stop sound_loop
                show sl sad dress at left
                show unblink
                with flash
                me "And how's that exciting feeling?"
                sl "What do you mean?"
                me "For once, I'm not the only one who looks like a retard."
                sl "It didn't work?"
                me "As you can see."
                "Slavya smiled sadly."
                sl "You don't seem to want it as much as I assumed."
                sl "I think I should leave."
                hide sl with dissolve
                "Slavya hurried off into the darkness."
                "And I... What about me?"
                "It was past midnight on the clock - the dance was coming to an end."
                "So, on the potty and in the cradle."
                play music music_list["a_promise_from_distant_days"] fadein 5
    return

label alt_day6_mi_dj_sleeptime:
    scene bg ext_house_of_mt_night with dissolve
    "Judging by the book tossed in the chaise lounge, the counselor never showed up."
    "The hell with her."
    play sound sfx_open_dooor_campus_1
    stop ambience fadeout 1
    scene bg int_house_of_mt_noitem_night
    pause(1)
    play ambience ambience_int_cabin_night fadein 1
    "We had a whole bunch of unspoken conversations with her, a whole bunch of unasked uncomfortable questions."
    "The ideal tactic in such a case is simply to stall for time until departure, when camp business will no longer be relevant."
    "Which means I need to get to sleep as soon as possible."
    "Agreeing with this postulate, I closed my eyes."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_dj_dance2_success:
    play music music_7dl["stilllovingyou"] fadein 5
    scene anim_square_party
    show mi normal dress
    with dissolve
    "Beautiful music."
    me "Beautiful evening."
    mi "Yes..."
    me "But you're still the most beautiful."
    "Miku looked up at me with her eyes slightly closed, with an expression that I just couldn't find a name for. It was all there - the tenderness, the concern, and the warning about the consequences."
    me "Don't think of it as a compliment... I don't know how to do them at all."
    me "If I see a person is tall or fat or old, that's what I say."
    me "So you're objectively the prettiest one here."
    show mi smile dress with dspr
    mi "Where is «here»?"
    "A Japanese girl smiled at the corners of her lips."
    me "On the dance floor, I guess."
    mi "Yes?"
    show mi upset dress with dspr
    "She tilted her head sideways."
    me "In the Union."
    mi "Oh, come on, «in the Union»... You're a flatterer, Senya."
    me "Okay, not in the Union. You, Miku, are the best girl in the world."
    mi "You're still fooling around."
    scene cg d3_mi_dance_afar_7dl with dissolve
    "The bitten lip, the little wrinkles at the corners of her eyes - all signs. I could see them, but I don't know how to translate them into plain human language."
    "Like the one about the cab driver who shakes his head in agreement and nods in denial... There's a difference of cultures."
    "But what's the difference... We've been through so much and I'm still the same retard."
    "Somewhere, someone has made it their will that under the alien skies of an alien planet, painfully similar to the one that had assimilated the enthusiastic childhood consciousness of five-year-old Semyon, the two met."
    "I am an average character, a walking stereotype and a proverb."
    "She's, well... A mascot, right? An embodiment of something, with her own looks, personality and history. Idealized, beautiful... Not real."
    "What might or might not work out with these inputs? A wedding, her career, and me in perpetual shadow? Which, actually, is more than fine with me."
    "Or, on the contrary, will she decide that family is more important to her and give up the stage to brew me suimono and lick my offspring?"
    "Or maybe none of that will happen, and I'm trying to gaze upon the universe with nonexistent eyes from the pages of some book and, like any spell, exist only as long as I'm spoken aloud."
    "And then the last page is turned, the last paragraph is swallowed - and a slight half-smile or a bitter sneer plays on the reader's lips - depends only on what the author has put into the text. The book closes - and I cease to be."
    "It's amazing what kind of nonsense comes to mind when you're dancing a farewell slow dance with a girl you like immensely."
    "For some reason we were both silent, each thinking about our own things, only a light exchange of touches, like a «I'm here, it's okay, I need you» response."
    "Finally Miku broke the silence:"
    mi "We had this band come here a few years ago. I remember this song. They had just written it..."
    me "Do you know what it's about?"
    mi "Not really, I need to improve my English."
    me "It's a song about walls."
    mi "But that's not what he's singing about!"
    me "Context, honey... The wall is allegorical."
    me "It's about the obstacles that often stand in the way of lovers in their desire to be together. You know?"
    mi "What do you mean?"
    me "Tomorrow your Pa will pick you up, and it's unclear when we'll see each other again. If it were our time - we'd find a way to contact each other. But here... There's no guarantee on the phone."
    mi "But you said you were coming with me!"
    "I smiled."
    me "I will. But does everything depend on our wishes?"
    me "If something goes wrong. And we'll split up."
    mi "No, no. We won't split up. I will stay in the Union, next to you. Do you hear me? Don't even think about getting rid of me that easily."
    me "What about your studies, your career..."
    mi "We'll think of something. {w}I get it. Your wall is something people can't fight on their own..."
    mi "But I won't be my own..."
    me "I feel like your favorite pillow. You're dragging me along, and the best help on my part is just not to stop you from fulfilling our dreams."
    mi "Baka."
    "She kept looking at me with a breathtaking mixture of adoration and interest."
    "So at some point I just couldn't take it anymore."
    "I didn't give a damn about possible onlookers."
    "About the counselors."
    "All of them."
    "With my 185 centimeters, her 158 was perfect for carrying her in my arms, in my pocket, warm on my chest, and so on..."
    "But for what I wanted, the height difference was too much."
    "Miku had to stand on her toes."
    "There was that strange feeling again, the one that made my legs go cold and my heart go a hundred beats a minute at once..."
    "Her lips were soft and moist - after the bite."
    "Through the aristocratic pallor of her cheeks there was an instant blush."
    "Even though she tried her best not to close her eyes - at one point she almost palpably purred and relaxed."
    "And she smiled when the kiss stopped."
    mi "Senechka..."
    "I put my finger on her lips."
    "We've already said more than necessary. And the communication within a couple is not even one-quarter words... Much more - touch, smell, warmth..."
    "Scarlet lips, ruddy cheeks, white skin..."
    "She winked at me and, hugging me, pressed her nose to my chest."
    mi "Good... my..."
    "And I, as I always do at times like this, kissed the top of her head. Just... I just couldn't help myself."
    me "My childhood song... My camp past - how much has been danced to it, how much has been lived and felt."
    mi "Me too now..."
    "She reached for my ear and whispered:"
    mi "Don't you want to run away?"
    me "And the disco?"
    mi "And Slavya here for?.."
    me "Then I do. Where do you want to run away to?"
    stop music fadeout 6
    return

label alt_day6_mi_dj_escape:
    scene anim_square_party
    show mi normal dress
    with dissolve
    play ambience ambience_camp_center_night
    "The music faded and the dancers reluctantly broke into pairs, some clapping from the benches, saluting the good taste of the host, and Miku pulled me by the hand."
    mi "Let's go!"
    me "Where to?"
    mi "Let's go for a walk! What a nice night!"
    me "And who's going to let us do so?"
    show mi smile dress with dspr
    "Miku just smiled."
    me "Now they're going to catch us and force to carry the speakers."
    show mi grin dress with dspr
    "The smile turned smoothly into a giggle."
    me "Or to sweep a square."
    mi "Sen, you're something!"
    me "Thank you, I tried!"
    show mi normal dress with dspr
    mi "Okay, you don't want to walk, let's go sit somewhere!"
    "That thought appealed to me more, and I began to consider my options."
    menu:
        "To our place!":
            show mi upset dress with dspr
            mi "Are you sure? What if the counselor comes? She'll think the not-know-what."
            dreamgirl "The not-know-what?"
            "The inner voice laughed nastily."
            me "Then... Ah, I got it!"
            show mi normal dress with dspr
            mi "Huh?"
            me "An offer came up to get into one of the unoccupied cabins and sleep there together. Are you okay with that?"
            mi "But they're all closed..."
            me "So we'll just squeeze the keys from the counselor and..."
            "After thinking for a while, Miku nodded."
            mi "And no one will find us! Come on!"
            scene bg ext_house_of_mt_night_without_light
            with dissolve
            play music music_7dl["ltyh"] fadein 5
            "It was just as I'd expected yesterday - the head-turning glee of a warm palm fluttering in my hand, the soft voice, the smell of hair, bringing me to a rapture."
            "We ran to the cabin in two minutes and froze, listening - and it turned out we were hugging. And snuggling closer and closer to each other."
            th "A little more like that, and I'll lose control of myself completely."
            me "Mi..."
            "I coughed."
            me "Miku."
            show mi serious dress with dspr
            mi "What is it?"
            me "If you want to cuddle a little more, I don't mind. But - the cabin, remember?"
            "With displeasure pushing me away, the Japanese girl frowned and nodded."
            me "All right."
            play sound sfx_open_dooor_campus_2
            scene bg int_house_of_mt_night2
            with dissolve
            "Once inside, I looked around - luckily, there was enough light from the lanterns coming through the window to get my bearings."
            "There was a creaking sound behind me, and I shuddered."
            show mi normal dress with dspr
            me "Miku, shh."
            mi "Okay, Okay."
            "She whispered, coming toward me."
            "I went back to looking for keys, so I didn't immediately notice how she-"
            "Warm, responsive fingers went under my shirt."
            me "Mi... Miku?"
            "My throat was dry at once, and silly things like an alternate airfield were decidedly out of my mind."
            "I wanted to..."
            menu:
                "Relax and have fun":
                    "Which I successfully did."
                    "Not satisfied with one hand, Miku soon had the other under the shirt."
                    "Turned me around to face her and..."
                    play sound sfx_open_door_kick
                    play music music_list["awakening_power"] fadein 2
                    scene bg int_house_of_mt_noitem_night with dissolve
                    show mt rage dress with dspr
                    "The door swung open, the light came on..."
                    "There was a furious counselor on the doorstep!"
                    mt "Semyoooon!"
                    th "Damn it, why Semyooon again!"
                    mt "Miku, go to your cabin."
                    show mi upset dress at left with dspr
                    mi "But..."
                    mt "Miku. Just. Go."
                    "Squad leader said separately."
                    "Miku was clearly about to engage in a conflict, even taking a deep breath."
                    show mt angry dress with dspr
                    mt "Miku."
                    "As she exhaled, the Japanese girl seemed to have lost her inner core - deflated: her shoulders slumped and drooped, her back slouched."
                    "Stroking my shoulder, she walked to the door, squeezed past the counselor, and melted into the night."
                    hide mi
                    mt "And you, Semyon..."
                    "The leader poked her finger somewhere in my direction."
                    mt "Sleep. now!" with vpunch
                    "Olga rattled the door."
                    "All that was left was to follow her advice."
                    stop music fadeout 6
                    scene bg int_house_of_mt_night2 with dissolve
                    "After extinguishing the light, I undressed, ducked under the covers, and stretched out."
                    "The jitters that had been pounding me for the last five minutes receded, and I realized how tired I was."
                    "Closing my eyes, I drifted off to sleep."
                "The keys!":
                    me "Miku! If we stay here too long, the counselor will catch us!"
                    "Pouting slightly, the Japanese girl did remove her hands, and I was able to concentrate on looking."
                    if alt_day1_sl_keys_took == 1:
                        "It wasn't until a few seconds later that it dawned on me what a retard I was:"
                        me "I've got a trophy bundle!"
                        "It was, as I expected, in the nightstand."
                    else:
                        "Finally managed to find the keys on a big bunch in the far corner of the nightstand."
                    me "That's it, let's go!"
                    scene bg ext_house_of_mt_night with dissolve
                    play sound sfx_close_door_clubs_nextroom
                    play ambience ambience_camp_center_night
                    "We jumped out of the cabin and, by some miracle, missed the fleeing counselor and rushed to the designated cabin."
                    call alt_day6_mi_dj_hentai
        "Should we bide our time?":
            mi "I don't think that... Anyway, okay."
            mi "You're the man - you know best."
            "Putting her hand in my palm, Miku completely gave the initiative to me."
            with fade2
            "And, as it turned out, in vain..."
            scene bg ext_musclub_night_7dl
            with dissolve
            play ambience ambience_camp_center_night
            "At the music club, Slavya was walking around."
            scene bg ext_clubs_night
            with dissolve
            "The lights were on in the clubs - it was obviously busy. I didn't even want to think by what or who."
            "What was more important was that it was simply not free."
            scene bg ext_house_of_un_night_7dl
            "And as we moved toward Lena's cabin, we barely managed to dodge a swell of water - which Lena was caught under!"
            "She squealed, and a suspiciously familiar laugh resounded in the darkness..."
            "Anyway, Miku's cabin was now occupied, too."
            show mi normal dress with dspr
            mi "All righty, my faithful knight. It seems they really don't want to let us be alone tonight."
            me "Wait! We haven't gone to the pier or the beach yet!"
            show mi serious dress with dspr
            mi "Senya... You serious?"
            "Without waiting for an answer, she nodded:"
            mi "That's what I think, too. Well, let's take it as a sign from above, telling us to have a human arrangement, with a hot bath, long talks, and a huge bathtub in which both of us can fit."
            "She seemed to like the idea so much herself that she clapped her hands."
            mi "And just dare to say no!"
            me "Didn't even thought about it!"
            "I answered honestly."
            show mi normal dress with dspr
            mi "And now we're saying goodbye. And count the minutes until morning. Remember, you promised me you'd stick with me!"
            me "Of course, princess. Where you go, I go."
            "To tell you the truth, I could hardly imagine how it could be feasible, but for myself, I decided to make every effort."
            "After all, a building of happiness and mutual affection, like that same tennis or dance, can only be built by the two of us."
            mi "I'll look forward to seeing you."
            hide mi with dissolve
            "Miku kissed me lightly on the cheek and disappeared out the door."
            me "Me too..."
            scene bg ext_house_of_mt_night
            with dissolve
            "I had to stomp home - even though I had a lot of plans for the evening. And all the plans involved an incredibly beautiful girl with a wave of aquamarine hair."
            "I never thought she was superstitious."
            "It's impossible to study a person thoroughly in a week, though."
            "But to fall in love even more - easier than easy."
            "In a week the feeling of emotional attachment is like a campfire, it only gets hotter, but a clear mind in this situation is very important to see everything, to study the details and the consequences."
            "It's not that I'm counting on us getting to bed on our farewell night - it's silly, trivial, and predictable, plus I believe that only a date prepared by our own hands can make our union truly unforgettable."
            th "But... Isn't she giving up too easily?"
            "Again I shoved that thought away from me that Miku seemed to know something. Something that gives her the strength and determination to do things unthinkable for a girl her age and upbringing."
            "Over thinking, I made my way to the cabin."
            play sound sfx_open_dooor_campus_1
            stop ambience fadeout 1
            scene bg int_house_of_mt_noitem_night
            pause(1)
            play ambience ambience_int_cabin_night fadein 1
            "There was expectedly no one inside - whoever our counselor had chosen on this warm night was clearly not going to waste a second of her time."
            "Well, all I have to do is close my eyes and sleep until morning."
            "Roll my eyes to make it easier to fall asleep, relax the muscles in the back of my head to loosen the cerebral activity."
            "Switch to shallow breathing, only the upper third of the lungs."
            "And, feeling the moment when the body begins to sink into the soft mattress, with an effort of will, shut off consciousness."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_dj_hentai:
    scene bg ext_house_of_el_night_7dl with dissolve
    play ambience ambience_camp_center_night fadein 1
    play music music_7dl["take_my_hand"] fadein 2
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene
    $ renpy.show("bg int_extra_house_7dl", what = Notch("bg int_extra_house_7dl"))
    show mi serious dress
    with dissolve
    "We got it right."
    "As right as possible."
    "As right as possible..."
    "Suddenly, yesterday's tantrum seemed stupid, even if it was much more about what awaited me on the other side of the miracle."
    "I remembered the price I paid to get here, and now, with Miku holding my hands, I realize it really was worth it."
    "Tomorrow there might be something, maybe I'll stay here and the two of us will make our silly plans come true."
    "Or things will go backwards, and it will turn out that Miku is the girl with whom we share memories and now also dream together."
    "But here and now we have a warm southern night, crickets singing and a warmly smiling universe eagerly settling into memory."
    "So that ten years later, carelessly embracing an impossibly beautiful spouse with an oriental-eyed cut, to her question «do you remember how we met?» a few silver splashes of sinless happiness trickle out."
    "I remember everything. And I always will."
    "How many times can we swear feelings for each other? How long can we revel in each other?"
    "I long to latch on to something, to make an association that will always awaken the memory of this evening."
    "But beside the most affectionate, the most desirable."
    show mi normal dress with dspr
    me "You too... memorizing?"
    "A nonexistent girl from a fairy tale dream."
    "I will remember you, even when we are together again."
    mi "And I memorized everything at once."
    "Miku shrugged serenely."
    "We stood in the middle of the cabin without lights on, but we still managed to see each other somehow."
    "It was as if a certain blacksmith had once taken my measurements, cast a mold - and, gathering some icy happiness and half-unreal dreams, created her."
    "My Miku, perfect for me, warming me with her breath, smiling, drowning in her huge, almost cartoonish pupils."
    mi "You're surprisingly easy to memorize. If I could draw, I would draw you easily - so well you imprinted inside me."
    "The serious look ruled out any possibility of a joke."
    me "You mean the appearance?"
    "Miku smiled."
    mi "I mean everything! Both the way you look and the way you sound."
    mi "If I wanted to sing you - I would sing you in a low, slightly resentful voice, with great hope of a miracle."
    "Dragging me behind her, she retreated to the bed."
    me "Why low?"
    "Miku laughed, but quickly stifled a laugh, realizing that I just didn't understand her humor."
    show mi serious dress with dspr
    mi "Because that's what you sound like - somewhere in the first octave. I just can't take it any lower."
    th "Strange girl."
    th "Strange, obscure, oriental girl. Exot."
    dreamgirl "If you're still hesitant about the sincerity of her intentions... Then you're in the cabin where no one will find you, man."
    mi "And I want you to sound close to me."
    play music music_7dl["ourfirstmet"]
    mi "Always."
    "Her fingers were frantically undoing the buttons of my shirt."
    "Her lips gagged my mouth when I wanted to ask something."
    mi "Be quiet. Just... Love me. Okay?"
    show mi upset dress with dspr
    me "But I..."
    mi "I want to. If you want to."
    "Rolling out the mattress on the bed, Miku sat up and pulled me toward her."
    show mi serious dress with dspr
    mi "Be with me... Please."
    "Instead of answering, as gently as I could, I touched my lips to the skin under her ear."
    "And again, and lower. As if in some unknown writing, like music, intelligible in every language on the planet."
    "I want you... I want you..."
    mi "Ah... Senya."
    "Miku wrapped her legs around me and, shuddering lightly, snuggled closer."
    mi "Can it be that good?"
    "She whispered."
    scene black
    with fade2
    "The whole universe ceased to exist as the crumpled things flew to the next bed - we were for each other."
    "Miku was babbling something, herself not understanding, but still stubbornly pulling me toward her."
    mi "Go..."
    "With a jerk, she flipped me onto my back, and Miku dug her lips into mine with a kiss."
    "Thinking poorly and reluctantly, I was all there - in the white marble figure, biting her lip and looking right through me."
    "Hot drops fell on my chest."
    me "Are you... Are you crying?"
    mi "Be quiet, baka... I love you."
    "She whispered this confession easily, naturally, as if just continuing to breathe."
    "Giving a few moments of an experience no other man has ever had in his entire life."
    "Feelings of being one with his beloved, his most desired."
    with flash_red
    "I passed out. Making love to this girl drank me dry, drained me of all my strength."
    "And she was still sitting on top, breathing fervently."
    me "Miku..."
    mi "Be quiet..."
    "She put a finger on my lips in the darkness and, as she was, she got off me and lay down beside, resting her right arm and right leg on me - in a sort of impromptu hug."
    mi "Sweet dreams."
    "Japanese g... woman quietly and peacefully — {i}peacefully{/i} — sniffed. Leaving me alone with a crazy body and a racing heart."
    "The ancestors, however, were not fools, and considered the best cure for any disorder to be a beloved woman at their side."
    "Not five minutes later, I had already closed my eyes, embraced Miku and fallen into a sweet sleep."
    stop ambience fadeout 3
    pause(3)
    $ alt_day6_mi_dj_hentai2 = True
    return

label alt_day7_mi_dj_together:
    scene bg int_extra_house_7dl with dissolve
    play ambience ambience_int_cabin_evening fadein 2
    play music music_7dl["tellyourworld"] fadein 6
    "And... Good morning!"
    "To wake up in a new place - when my eyes open because I've slept, not because the alarm clock screamed."
    "To wake up hugging the most affectionate creature I've ever known."
    "To wake up and soak in her warmth first impression of the morning, the smell, the exhilarating feeling of touching naked, smooth skin."
    "The silliest smile I can portray jumps out on my lips all by itself - I'm bribed, I'm young, stupid and in love."
    show mi normal dress with dspr
    mi "Hi, Senechka."
    "She whispered."
    if not alt_day5_mi_dj_hentai_done:
        "I had to get up."
        "Miku was already ready and dressed in yesterday's dress by then."
        mi "You know... Let's go change first, shall we?"
        "She helplessly tried to smooth out a few jams on her chest."
        "I glanced at my watch - it was getting close to wake-up time, and we were extremely fortunate to be up - we had every chance to finish our business before the waking pioneers were drawn outside."
        me "Yeah, whatever..."
        scene bg ext_house_of_un_day with dissolve
        play ambience ambience_camp_center_evening
        "Our villa was very conveniently located across the corner from a makeshift alley, one end of which ended at the counselor's cabin, and the other at Lena and Miku's cabin."
        "Farther along was the path to the washhouse, but we weren't interested in it."
        "Miku, with a brief nod to me, disappeared behind the door."
        play sound sfx_open_door_strong
        show mi normal pioneer with dspr
        extend " and two minutes later appeared on the doorstep again."
        mi "I'm ready."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_mi_dj_alone:
    scene bg int_house_of_mt_sunset with dissolve
    play ambience ambience_int_cabin_evening fadein 2
    "The morning began almost immediately the moment I closed my eyes."
    "How the sky begins a few inches above the surface of the earth."
    "My last morning here at camp. And quite possibly my last morning next to Miku."
    "Such thoughts made my eyes open completely on their own, and I immediately felt sleepless."
    "Didn't have a very good day yesterday. And the day before yesterday didn't go well either. Even though I'm trying my best not to screw up."
    "It's hard to imagine what my usual behavior could have turned into."
    if alt_day6_mi_dj_catapult == 2:
        th "I almost believed Slavya yesterday."
        th "Yeah, I almost did."
        th "Escape from Miku."
        th "What was I thinking, Lord..."
        dreamgirl "I don't know about you, but I suddenly really wanted to see her. Are you «in»?"
        "Totally agreeing with that statement of the question, I got up and, after hastily dressing, hurried to the Japanese girl's cabin."
    elif alt_day6_mi_dj_catapult == 1:
        "Suddenly yesterday came to mind."
        "How frustrating it was not to get what I thought was already mine."
        "The deal with the devil - praise be to Random, I had the good sense to back it up."
        "And Miku showing up was the best confirmation that what I did was the right thing!"
        th "I should go say hello to her."
        th "I haven't seen her in almost five hundred minutes!"
        "Quickly dressed, I jumped out of the cabin."
    else:
        "Here's the thing..."
        "If I'd had the guts yesterday - or, I don't know, luck - we could have gone further than we did."
        "It's just a question of how far I need to go."
        "Certainly the woman you love should be loved in every way possible, and the ability to please her should not be shamefully hidden in the background."
        "But maybe we really are a little early. That's what's so great about the candy-coating period, it's just enough to know that your date exists in order to be happy."
        "So... Maybe we shouldn't get too excited."
        if alt_day5_mi_dj_hentai_done:
            dreamgirl "Then what did you have yesterday?"
            th "I don't know. Passion? I don't really remember anything."
            dreamgirl "Need I remind you?"
            th "Don't! I've had enough of the standard morning reaction."
        "With a sigh, I opened my eyes."
        th "Time to pay Miku a visit. It's been an ugly long time since we've seen each other."
        th "And... one!"
        "I quickly, quickly packed up and walked out of the cabin."
    play sound sfx_open_door_1
    scene bg ext_house_of_mt_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 3
    me "Good morning!"
    "I wished into the void."
    "If Miku had been here, she would have smiled, if counselor, she would have nodded."
    "But I stood on the porch and pretended to be a clown, saying hello to the void."
    "Whatever!"
    "The anticipation of anything is often more pleasant than getting what you want."
    "Now I don't know how the conversation will go, if the girl will be pleased with me, or if I'll even be able to find her."
    "But I'm already having a hard time squeezing the glee inside me, bursting out in an unhealthy laugh and the stupidest smile I used to allow myself only when I was alone."
    "It is true what they say, that attachment to someone is a severe, almost incurable disease."
    show unblink
    "The greatest difficulty in the cure is that the patient does not consider himself as such at all."
    "And is in no hurry to get rid of the affliction."
    "Moreover, he may begin to take active measures against the object of his affection, and sometimes he even succeeds in infecting the latter."
    "And seriously, only now have I begun to understand the meaning of the phrase «of all your humanity I am interested in one person only», albeit taken out of context."
    "You don't begin to despise or mistreat everyone around you, no."
    "To you, they simply cease to exist - along with all their uniqueness, originality, and right to a personal opinion."
    me "Let's go."
    "Tossing the bundle of bathing supplies in the palm of my hand, I hurried to the sinks."
    "Of course, of course! Miku's cabin was in my way purely by accident!"
    "But I'm not going there."
    th "I don't want to show up at my darling's house looking asleep, disheveled, and with my teeth unbrushed."
    th "It's inevitable, of course - sooner or later. But it's better late, isn't it?"
    me "You just look into my eyes, smile..."
    "I murmured, shifting to a leisurely jog."
    "Today I wanted to be, look and feel my best - so as not to muddy the impression of a farewell shot."
    scene bg ext_washstand_day with dissolve
    play music music_list["everyday_theme"] fadein 5
    "As I ran past the conspicuous «barrel», I secretly hoped Miku would come out to say hello."
    "But she either left already or hasn't come up yet."
    "I didn't find out."
    th "And... Inhale!"
    scene bg ext_washstand2_day
    with dissolve
    play sound sfx_open_water_sink
    pause(1)
    play sound_loop sfx_water_sink_stream
    me "A-a-a-a-a!" with vpunch
    "My morning starts with a temperature shock, and where it ends, I don't know."
    "To tell you the truth, I was beginning to get used to it."
    "If I do get back to my place, I'm going to miss it big time."
    "Like a seventeen-year-old body, a total hormonal imbalance, and the ozone-like freshness of the air only possible in a pine forest."
    "And, of course..."
    "I looked up when I heard footsteps."
    scene bg ext_washstand_day
    with dissolve
    if alt_day5_mi_dj_hentai_done:
        show mi sad pioneer with dissolve
        "Miku didn't look very healthy."
        me "Hello, red sun!"
        mi "Senechka..."
        "She whispered."
    else:
        show mi normal pioneer with dissolve
        mi "Hi, Senechka. How did you sleep?"
        me "I don't remember. I blacked out instantly."
        mi "And I had such strange dreams..."
        "She stood next to me and, opening the faucet, gently touched the icy stream that was beating into the tiled womb with her finger."
        mi "How I don't like it..."
        me "No way! But look at that blush all at once!"
        "I patted myself on my wet cheeks."
        show mi shy pioneer with dspr
        mi "That's the only reason..."
        "We were babbling about some incomprehensible nonsense that had nothing to do with the topic or us."
        "Even though we should have said the most important things."
        "They're the simplest things."
        "The only problem was that they were often the hardest things to say."
        me "Our last day, huh?"
        play sound sfx_draw_water
        "With a hearty splash of cold water in her face, Miku seemed to fall out of reality for a second."
        "I had to repeat myself."
        dreamgirl "You know what you have to say now, don't you?"
        dreamgirl "Not about the last days at all."
        th "About what?"
        dreamgirl "About you, dummy. You've wasted too much time."
        dreamgirl "You didn't even know she existed right away, you thought you were dreaming until the last minutes..."
        th "So what?"
        play sound sfx_borshtch
        "I didn't quite know if it was myself or my inner voice I was taking more revenge on, but I threw a few more handfuls in my face, each one taking my breath away and making my throat twitch involuntarily in an attempt to swallow."
        dreamgirl "Calm down, psychopath?"
        dreamgirl "Or stick your head under the stream in its entirety - what if it gets better?"
        th "I still don't hear constructive."
        dreamgirl "Constructive? I'm afraid after your screwups, it's not constructive that's needed there, but to tear it all in half and build from the ground up."
        mi "Why aren't you talking, Senechkaa?"
        "Finally Miku, who had been brushing her teeth the whole time, and therefore had no say in the matter, spoke up."
        play sound sfx_close_water_sink
        stop sound_loop
        me "Yes, I think it's the right thing to say in a situation like this. I don't want to swear on something when I'm not even sure I'll make it to town with you."
        show mi sad pioneer with dspr
        mi "I don't understand..."
        me "Though one thing I can promise you with certainty - I will remember you."
        show mi happy pioneer with dspr
        mi "Now that's a pretty good start!"
        "She grabbed my arm and dragged me after her."
        scene bg ext_houses_sunset with dissolve
        "Even though we weren't really counted as vacationers anymore - the vouchers, according to Miku, ended at midnight - there was still a daily routine for us."
        "It reminded me of the old days, when the kids and I were finishing their third or fourth shifts, when all the back-pulling counselors and pioneers would go back to town to get ready for the new school year, and only the laziest of slackers would stay in the boarded-up buildings warmed up by the August sun."
        "Camp was turning into an impromptu recreation base, without the drill, without the obligation, without the silly running around."
        "Everything there was - a schedule of meals, a succession of dances-film-themed dances, and trips to the store in the nearest village ten kilometers away."
        "And somehow we managed not to get bored! Even though we didn't have to participate in community service activities, we found things to do."
        show mi smile pioneer with dspr
        mi "Hello, Senechka, are you here?"
        me "Yes."
        "We spent a lot more time talking to each other, a lot more time going out into the woods, along the highway, a day didn't go by without a spontaneous game of pioneer ball or volleyball."
        "It just proved my point that if a man doesn't have to be disturbed for no reason, he'll organize his own leisure time just fine."
        "And here we have nearly departed campers, nearly surrendered cabins, nearly deserted camp."
        "I caught myself thinking: Miku must have a big, beautiful suitcase on wheels. And one hundred percent more than one."
        "She's like an avid camper, carrying everything she needs, from clothes and food to gear."
        stop music fadeout 5
    return

label alt_day7_mi_dj_badfeel:
    if alt_day6_mi_dj_hentai2:
        scene bg int_extra_house_7dl
        show mi sad dress
        with dspr
    else:
        scene bg ext_washstand_day
        show mi sad pioneer
        with dspr
    mi "I don't... I don't seem to be feeling very well."
    "The delicate purple color of her face completely confirmed the girl's words."
    mi "Will you walk me to the bathroom? I don't think I can make it on my own."
    "Here it is, the most important quest of my life! Escorting a girl to the bathroom. Six days of courting was worth it!"
    dreamgirl "Actually, it really was worth it..."
    th "What do you mean?"
    dreamgirl "Nothing..."
    "I don't understand anything, but interrogating my own subconscious is something I haven't gotten to yet."
    if alt_day6_mi_dj_hentai2:
        "I had to get up."
        "Miku was already ready and dressed in yesterday's dress by then."
        mi "You know... Let's go change first, shall we?"
        "She helplessly tried to smooth out a few jams on her chest."
        me "What about..."
        mi "I promise to wait."
        "I glanced at my watch - the time was approaching rising, and we were extremely fortunate to be up - we had every chance to finish our business before the pioneers woke up on the street."
        me "Yeah, whatever..."
        scene bg ext_house_of_un_day with dissolve
        play ambience ambience_camp_center_evening
        "Our villa was very conveniently located across the corner from a makeshift alley, one end of which ended at the counselor's cabin, and the other at Lena and Miku's cabin."
        "Farther along was the path to the washhouse, but we weren't interested in it."
        "Miku, with a brief nod to me, disappeared behind the door."
        play sound sfx_open_door_strong
        show mi sad pioneer with dspr
        extend " and two minutes later appeared on the doorstep again."
        mi "I'm ready."
    stop sound_loop
    "To tell you the truth, I was pretty amused by the whole situation - both when I offered my hand to accompany my lady to the fun houses, and when she graciously accepted my hand and we waddled to our destination."
    "I probably would have even laughed if it weren't for the empathy screaming in my voice that the girl is really quite a twist - and it looks like she's holding on with the last of her strength."
    scene bg ext_houses_sunset
    with dissolve
    "Once we got to the toilets, she nodded apologetically and, clasping her hands to her mouth, disappeared behind the door."
    "A few seconds later there were heartbreaking noises - it looked like my empathy was telling the truth, Miku was gargling like a grown-up."
    th "Hodgepodge - is death to the figure, isn't it? And the pancreas?"
    if alt_day6_mi_dj_feed == 'sl':
        th "And it looks like our traditional cuisine didn't go over well with some people yesterday. That's right, you can't have potatoes after your mussels and seaweed."
    elif alt_day6_mi_dj_feed == 'un':
        th "And on top of that we finished off with a heavy smoked chicken - which, by the most conservative estimate, she ate half of."
    elif alt_day5_mi_dj_hentai_done:
        th "And coupled with yesterday's breakfast of Japanese bichpaks... Anyway, I get it."
    dreamgirl "Yeah, your girl is poisoned. We should probably take her to Viola to get some charcoal."
    th "You think?"
    dreamgirl "Of course I think! I have no other means of communication."
    th "No, I mean Viola."
    dreamgirl "Of course. We should go visit the nurse, you shouldn't leave your body toxic anyway, you don't have twenty-four hours to lie down flat."
    dreamgirl "But, she might have a reasonable suspicion as to why the girl might vomit in the morning..."
    th "It's a little early for that!"
    dreamgirl "It is, indeed, a little early. Although it won't save you from Viola's jokes..."
    th "Yes, you're right. What should we do?"
    dreamgirl "We could rob the counselor."
    if alt_day6_mi_dj_hentai2 and alt_day5_mi_dj_hentai_done:
        dreamgirl "Although if she hasn't seen you at the cabin - second night in a row, by the way! - she might have reasonable questions, too."
        dreamgirl "Or you might get lucky, and she's been walking around somewhere all night again, and now she's gone. So you climb into her medicine cabinet and-"
    dreamgirl "What's in there? Coal, pancreatin, something... Cerucal, Hofidol."
    th "Haloperidol, damn it. If you don't want to help, just say so!"
    show mi normal pioneer with fade
    mi "It seems to have let up a little..."
    "Her face had become drained, her eyes sunken, and the delicate green of her cheeks replaced by a more neutral yellowish hue."
    "She set her wet face to the light breeze - it also seemed to make the nausea recede."
    me "You know, let's go to the doctor. Poisoning is no joke."
    show mi scared pioneer with dspr
    mi "What if she asks why the girl is throwing up?"
    me "Let's tell her the truth - someone didn't follow a normal diet yesterday and paid the price for it today."
    "Miku looked at me with a mixture of tenderness and sympathy, the way one usually looks at mentally handicapped relatives."
    "But then it seemed to get to her."
    mi "What, do you think too..."
    me "I don't think, I'm not a doctor. But to be honest, I highly doubt it. But, just in case, let me be the poisoned one?"
    "The Japanese girl nodded and took my hand again."
    scene bg ext_aidpost_sunset_7dl with dissolve
    if not alt_day6_mi_dj_hentai2:
        "While we walked, cleaned and tidied up, a surprisingly long time passed - we missed both the exercise and the lineup."
    else:
        "While we walked, cleaned and tidied up, a surprising amount of time passed."
    play sound sfx_knock_door2
    cs "Open."
    if not alt_day6_mi_dj_hentai2:
        "We entered the infirmary to the accompaniment of the horn calling for the canteen."
    me "I'll do the talking, okay?"
    "I whispered, and after waiting for a nod, I pushed the door open."
    stop music
    stop ambience fadeout 2
    play sound sfx_open_door_1
    pause(1)
    $ persistent.sprite_time = "day"
    scene bg int_aidpost_day
    with dissolve
    play ambience ambience_medstation_inside_day fadein 3
    play music music_list["gentle_predator"] fadein 3
    if not alt_day6_mi_dj_hentai2:
        th "It seems we're flying in for breakfast."
        "With obvious doom I realized."
    show cs normal with dspr
    cs "Good morning... pioneers. How are you doing?"
    me "Hello, Viola. And I've had a bit of trouble."
    cs "Really?"
    show cs shy with dspr
    cs "Aren't you a little young for... trouble?"
    "She winked at Miku, and smiled - blowing our cover for good."
    me "No, that's not what I mean! My stomach hurts. I think I ate something wrong yesterday."
    show cs smile with dspr
    cs "Is that so? That's very sad. Take your clothes off."
    me "Why?!"
    show cs normal stethoscope with dspr
    cs "What do you mean why? Now we're going to do a... medical examination."
    "She already has a phonendoscope around her neck out of nowhere."
    me "But I just have a tummy ache!"
    cs "You."
    me "Me!"
    cs "Yeah. Stomach."
    me "What's the big deal?"
    show cs normal glasses with dspr
    "Putting the instrument aside, Violetta took her glasses and, holding them in the manner of a lorgnette, carefully examined each of us."
    cs "Are you sure your stomach is sick?"
    me "I'm telling you!"
    show cs smile glasses with dspr
    cs "That's very strange. Your stomach is sick."
    cs "And the green one's a pioneer girl for some reason."
    "Viola poked in Miku's direction with the temple of her glasses."
    cs "Well... Pioneer Girl, is it true that they eat octopus there?"
    "Miku quickly covered her mouth with her palm, darkened more than ever, and looked pleadingly at the nurse."
    show mi shy pioneer at left with dspr
    cs "That's what I thought."
    "Climbing somewhere in the table, she rattled the jars and threw over her shoulder in a voice so casual I didn't realize at first that she was addressing me:"
    cs "When was the last time?"
    me "What?"
    cs "I don't know how much I can be honest with you..."
    th "Shit, she guessed it!"
    "Finally retrieving a small cardboard box from her desk, she pulled one plate from it and held it out to Miku."
    mi "Charcoal... Activated."
    me "Charcoal?"
    th "So it was just a joke?"
    cs "One pill per ten pounds of weight. In your case, that's five pills. Here, to drink."
    "A bottle of Borjomi was revealed to us from the refrigerator."
    show cs normal with dspr
    cs "The sooner you drink, the better. Don't eat anything before the bus, and... One more important tip, pioneer girl."
    mi "Yes, Viola?"
    cs "When you get there, go see you-know-who's doctor. Got it?"
    "Miku nodded and along with the extracted bottle and pills she hurried to the exit."
    me "So... That's it?"
    cs "Pretty much... Yes. Anything else?"
    "Seeing that I was about to say something else, she smiled."
    cs "Listen, pioneer. Right now it's poisoning, but judging by your reaction..."
    "I gulped."
    me "Uh... By your reaction?"
    cs "So there you go. I told her to go to the doctor for a reason. And you'd do well to have a head on your shoulders... Pioneer."
    cs "I hope you heard me. {w}Now get out of here and try not to talk too much."
    hide mi
    hide cs
    with dissolve
    $ persistent.sprite_time = "sunset"
    scene bg ext_aidpost_day
    with dissolve
    show mi normal pioneer with dspr
    "The process of ingesting the black pills gave little pleasure to Miku, but in the end it helped - the girl stopped swallowing and breathed more evenly."
    mi "The nurse we have, of course..."
    me "What?"
    show mi happy pioneer with dspr
    mi "Peaceful!"
    "Here's where I couldn't agree more."
    stop music fadeout 6
    if not alt_day6_mi_dj_hentai2:
        me "Shall we go and find out about breakfast?"
        mi "Sen... You, if you want. And I... Well, you know."
        th "Yeah... I guess I'll be eating holy spirit today."
        "The mood was great, and even the fact that we were safely out of breakfast couldn't ruin it!"
    stop ambience fadeout 6
    with fade
    return

label alt_day7_mi_dj_breakfast:
    scene bg ext_square_sunset with dissolve
    play ambience ambience_camp_center_day fadein 3
    me "Miku, do you have a lot of equipment with you?"
    show mi normal pioneer with dspr
    mi "No, Senechka. I only took a mixer, a bunch of sheet music, and a tape recorder."
    me "I don't think you could fit all that in one bag..."
    mi "I have two."
    "I think she understood what I was getting at. She understood, appreciated, and approved."
    "So I only came to camp in what I'm wearing, and I'll leave in what I'm wearing-but on top of everything else will be added-a hundred percent! - a huge bag of Miku."
    me "Say... I didn't see you yesterday at exercise."
    show mi happy pioneer at center
    mi "And I don't go to them."
    me "What do you mean?"
    mi "I'm... how shall I put it... Exempt!"
    me "I don't think I've ever heard of being exempt from exercise."
    "I grumbled."
    "Though I've already had thoughts about it."
    "That's probably because of the incompatibility of cultures again."
    "Nevertheless, I thought I'd clarify:"
    me "And for what reason?"
    show mi laugh pioneer with dspr
    mi "It's the same one!"
    mi "Because of which I had to sew my own dress for the dance."
    th "I figured as much..."
    mi "Too revealing in sportswear, huh?"
    show mi upset pioneer with dspr
    mi "Come on."
    me "Really..."
    me "And yet. I've seen your Seifuku - they're more than decent. The uniforms are just right."
    show mi laugh pioneer with dspr
    mi "Senechka, I'm sorry, of course, but I haven't been going to a regular school for years. And I'm doing an individual program."
    mi "In what is most comfortable."
    "I'm afraid if she puts that «most comfortable» on in front of me and starts her training..."
    "I got goosebumps."
    show mi shy pioneer with dspr
    mi "Oh, Senechka, why are you blushing?"
    "She asked with such directness that I almost believed her."
    "But - I don't know if it's unfortunate or fortunate - we've known each other for days, so I've gotten to know this image of the dim-witted kawaii schoolgirl."
    me "What do you think? I came to exercise yesterday in my uniform."
    show mi serious pioneer with dspr
    mi "No, Senechka. Clothes should only be used for what they are intended for. I'm not wearing a dress to the lineup after all - it's for other purposes!"
    "After imagining her doing leg swings in a skirt, I was forced to agree."
    "Time went on, but there was no one in a hurry to get into exercise."
    show sl smile sport at left
    "A passing Slavya waved at us."
    hide sl with easeoutleft
    show dv normal pioneer2 at right
    "Alisa, wandering somewhere half-asleep, didn't pay any attention to us."
    "We had to catch up with her."
    me "Alisa, wait!"
    show dv smile pioneer2 with dspr
    dv "Ah, hello, lovebirds."
    "She yawned longingly."
    dv "What do you want?"
    me "Alisa, where is everybody? Exercise, lineup..."
    show dv grin pioneer2 with dspr
    dv "You can tell right away who's new to camp."
    dv "There are no lineups today. Breakfast, let's pack up and get out of here."
    me "Get out of here?"
    dv "There will be buses at two o'clock, so no lunch, but with dry rations - the counselor will distribute them on the bus. That's it, don't bother me, I've got things to do."
    hide dv with moveoutright
    "She went into zombie mode again, and hobbled off toward the pier."
    "Miku and I looked at each other and laughed."
    "Who would have thought - two of the laziest pioneers decided to attend exercise for once. That's when exercise was canceled."
    "After standing around for a bit longer, just to realize how much of a slacker we both were, we headed toward the canteen."
    "It was getting close to nine o'clock, and still no horn."
    play ambience ambience_dining_hall_full fadein 3
    scene bg int_dining_hall_people_sunset_7dl with fade
    "Very sensible - as it turned out. There were hardly any empty seats left, and I had to drag Miku behind me in tow, moving almost to the windows and impolitely cutting off the Buzzer."
    "She only snorted, but didn't say anything."
    "At any other time I would no doubt have paid attention to this phenomenon, but right now I wasn't in the mood for nonsense."
    show mi normal pioneer at center with dissolve
    me "Bon appetit."
    "I wished as I sat down across."
    "We had already assigned roles, acting as one cohesive team, no questions asked, no time wasted."
    "She holds the seat, I organize the food - just because I can carry portions for the two of us at a time."
    "It would probably work in normal life, too - but damn humanity has never managed to come up with other ways to interact, to communicate, than slow, stupid and boring words."
    show mi smile pioneer with dspr
    mi "Tell me, what are you thinking about?"
    "The two of us were sitting at the same table, separated from the rest of the squad by a half-meter of empty space and a noise curtain created by the humming of the pioneers present."
    "So - why not?"
    "There was a song going round and round in my head - silly, pop, pathos."
    "It would be written ten years from now."
    "And it sings about how any man's greatest dream is to make someone his routine, part of his routine, part of his metabolism."
    "Someone to wake up to, to breathe through the day, to lift one's spirits."
    th "So what am I thinking about?"
    th "About that summer, that sunrise, that few broken rules you're almost used to..."
    th "About how damn beautiful you are, and I don't know anymore what would happen if someone wanted to take you away from me one day."
    th "About too much time being wasted on nothing at all."
    me "About nothing, sunshine."
    "I sighed."
    "The appetite was spoiled."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_mi_dj_preparations:
    scene bg ext_square_sunset with dissolve
    play ambience ambience_camp_center_evening
    show mi normal pioneer with dspr
    mi "So? Who are we going to pick first?"
    if alt_day_binder != 1:
        me "You, of course. I have one and a half clothes and a coat that went nowhere."
        show mi serious pioneer with dspr
        mi "Are you serious?"
        "I just waved my hand."
        me "You found something to worry about, too. I finally have an incentive to buy myself something sane, so to hell with the coat!"
        mi "With the coat..."
    else:
        "You know who!"
        "I don't have anything to gather!"
    me "Let's go pack you, miracle!"
    "I smiled."
    hide mi with dissolve
    "A self-contained soundtrack to my life, pounding from the inside of my temples, cutting my eyes, taking my breath halfway through."
    "That which will never be put to sheet music or performed, that which no instrument created by mankind can ever express."
    "Like those songs that touch the heart and are recognized as masterpieces along with the same incorruptible from the Scorpions, the best, the most unforgettable, will be written by those who by reason of not appearing in the world have not written a single song."
    me "So you have two suitcases, huh?"
    "The beginning of the conversation was brilliant. But it was a start."
    "My subconscious communicates with me in two ways - the familiar verbal way, as if to signify that I have my own self - and, by the way, to signify Miku's self-consciousness, too."
    "But there is also an additional mode of communication, which the subconscious sometimes resorts to if it wants to explain something quickly and intelligibly."
    "The image is a concentrated gestalt, combining intensities across the senses: lemon is sour, ribbed, smells citrusy, unctuous, yellow, moist."
    "The doorknob in my hand is metal, copper, with sharp edges, hard, hanging in the air at a level to which a grip reflex quickly develops, cold, opens with a slightly tangible spring movement somewhere inside - it feels like my joint."
    "My attitude toward Miku..."
    stop ambience fadeout 2
    with fade2
    "If it had been water, it would have knocked me down. Hundreds, thousands of pictures, associations, memories, tenderness, meaning, plans, affection, low, smells nice, warm, kind, responsive, I hardly saw any negativity from her."
    "How to express all this in wretched, pithy, flat words, even in poems, in which, according to linguists, there are almost two bytes of meaning per character - because of the context, the second-fifth-Fiftieth hidden bottom."
    "How do you explain the most important things to her in a few words?"
    scene bg int_house_of_un_day
    with dissolve
    play ambience ambience_int_cabin_day fadein 3
    if alt_day5_mi_dj_hentai_done or (alt_day6_mi_dj_feed == 'un'):
        "Absolutely nothing has changed since my last visit."
    "The walls are covered with posters of Miku herself, concert posters of Tsoi and Vysotsky - and they're both alive now. Maybe if we're lucky, we'll take a chance and go."
    th "Or not?"
    dreamgirl "You can't go to Vysotsky. But you might as well catch Victor."
    th "And save him?"
    dreamgirl "Whom are you going to save, you woodpecker?! Save yourself first! Your girl! Save your feeling."
    dreamgirl "Can't figure it out in his own kitchen, but there he goes, bidding to save the world."
    th "Hush, hush. Why are you shouting?"
    show mi normal pioneer at center with dissolve
    mi "Get the green suitcase out from under the bed, please."
    "Without turning around, I asked Miku - she'd already opened the makup-sack, shaped like a pretty little trunk with upholstered metal rounded corners - a real treasure chest!"
    me "Yes, a second."
    "Miku had two suitcases - identical, differing only in color."
    "I got the green one."
    mi "Yeah, thanks."
    "Following the makeup products, the place in the trunk began to be occupied by vials of some clear, oily liquids whose names I did not know."
    "Miku's favorite essential oil of eucalyptus must have been among them."
    mi "Opened it?"
    me "There's the code."
    mi "My birthday."
    "I felt myself blushing."
    me "I'm sorry, please. But I don't seem to know it."
    show mi laugh pioneer with dspr
    mi "Well, why don't you. Don't you know when my birthday is?"
    "She bit her lip and looked up at me, frowning, blinking rapidly, as if preparing to burst into tears."
    "But she couldn't stand it - she laughed."
    dreamgirl "If I'm not mistaken..."
    show mi smile pioneer at center
    with dspr
    mi "Well, how come..."
    "She looked at me and smiled."
    mi "3-1-0-8. August thirty-first was the day I saw the light."
    dreamgirl "Come on, it can't be just a coincidence."
    th "It's not a coincidence either. It's a parallel."
    th "Remember what she said about different rules in different places? Here she's alive, but she could well have been born on the same day or to the same people."
    me "I'll remember."
    "I promised."
    me "And how come I've never asked you this before?"
    th "And for that matter, I never asked about such things at all - about dates... It never even occurred to me."
    show mi serious pioneer at center
    with dspr
    mi "I don't know. But..."
    "She glanced at the calendar."
    mi "It's my birthday in five weeks! I'm going to be 17!"
    stop ambience fadeout 3
    play music music_list["trapped_in_dreams"] fadein 3
    me "I'd like to celebrate with you."
    "I smiled weakly."
    me "Don't you know who is required to pray on such occasions?"
    mi "I don't know..."
    mi "Ma never managed to bring up faith in me. {w}It's hard to talk to spirits or gods at all when there's an electronically stuffed studio at my side."
    show mi serious pioneer at center
    with dspr
    me "So that's why you..."
    mi "Yeah. We have a whole school of voice care there - that's besides stage skills, kabuki, and a whole bunch of other skills inherent in being an artist."
    show mi smile pioneer at center
    with dspr
    mi "Just don't think I'm complaining! I love it all so much, and I spend all my time happily either in the studio, on the stage, or in the choreography room."
    "She miffed."
    me "What?"
    mi "No, no, nothing."
    th "Of course, nothing. Now in a packed schedule she'll have to carve out a few minutes for one pesky Semyon, too."
    me "Do you think I'm going to be a big nuisance to you?"
    show mi happy pioneer at center with dspr
    mi "What nonsense, Senechka! You're going to be my inspiration!"
    mi "I just imagine dancing on the stage with you waiting backstage - I feel warm inside."
    "She ran her palm over her stomach."
    mi "Somewhere in here. That must sound silly. No, no, don't say anything."
    show mi normal pioneer at center
    with dspr
    mi "Just before you, I... I don't know."
    me "Judging by your pushing..."
    mi "Well! You'll say it too. Your proverb is, Eyes fear - hands make."
    me "There is one. But still, if I were as confident as you are..."
    mi "Sen... I'm a stage person. Getting over and over myself is the first thing I learned."
    play sound sfx_open_door_1
    pause(1)
    "There was a grain of truth in her words, but only a grain."
    "I wanted to continue the conversation, subtly leading up to the question of what she might know to be so sure of herself, but we were interrupted."
    scene bg int_house_of_un_day at zenterleft
    show mi normal pioneer at center
    show un normal pioneer at left
    with dissolve
    un "Hey, guys. Am I interrupting?"
    show mi normal pioneer at center
    with dspr
    mi "Hi, Lena. Are you already packed for departure?"
    show un smile pioneer with dspr
    un "Well... I didn't unpack actually."
    if alt_day6_mi_dj_feed == 'un':
        un "Except yesterday, while I was feeding you."
    show mi shy pioneer at right
    with dspr
    "Miku giggled, covering her mouth with her palm, and blushed a little."
    show un smile pioneer with dspr
    un "I took the books to Zhenya, now I'll give the laundry to Slavya, and that's it, I don't owe anything more to this day."
    "Nodding to us, she walked over to the bed and, with a demonstration of great expertise, she took off, gathered up the linens and towels in a pillowcase."
    "Pulled the suitcase out from under the bed and placed it under the table."
    "Exhaled."
    un "What?"
    me "No, no, nothing."
    "We both stood there the whole time and watched her pack."
    "Yes, yes, the third sight after fire and water to watch endlessly."
    un "Miku, if you want, I can take your laundry too, but take it off yourself!"
    "That sounded... meaningful."
    show un shy pioneer with dspr
    un "Oh. Screw you!"
    "She blushed and ran off to our twin laughs."
    hide un with moveoutright
    show mi smile pioneer at center
    with dspr
    mi "Actually, it's worth listening to."
    me "What do you mean?"
    mi "Come on, come on, don't be lazy!"
    "She got me up from the bed where I was sitting."
    mi "While I'm packing my bags here, help the girl pack the bed."
    th "I wish someone would make my bed..."
    mi "Yes, yes, and then we'll go to your place. We pioneers are independent!"
    "Miku cheered as hard as she could, smiling and trying to jest."
    me "I'm sad to leave, too."
    "I responded to the unspoken phrase."
    me "Both sad and scared."
    mi "We've got three more hours, let's not waste them sighing, okay? And get the bed ready already!"
    me "As you command."
    "I've had experience, too, of course. Though I haven't done anything like that in a long time."
    show mi serious pioneer at center with dspr
    mi "Don't you have anything else besides your coat?"
    me "Winter boots, a sweater and jeans - I'll have to wear those, because I'm turning in my uniform."
    show mi smile pioneer at center with dspr
    mi "Right, I also have to turn in my uniform. I got used to it after all this time."
    play sound sfx_7dl["blanket"]
    "As much as I wanted to hold some lingerie in my hands - perhaps the smell of a girl's body, maybe even a sniff - I didn't dare do it in front of Miku."
    "She'll call me a pervert and beat me up."
    "And she'll be right about the whole thing. But what can I do if smells have always meant almost as much to me as sight, taste, or sound?"
    me "Here."
    "I tossed the crumpled linen inside the pillowcase on the floor and, remembering how it's usually done, draped the thin blanket over the mattress, pressed a pillow and, after turning it a couple of times, did the rolling."
    th "It's just like the best houses."
    me "Don't thank me. I know I'm good."
    show mi normal pioneer at center with dspr
    mi "You're a nerd!"
    "The Japanese girl laughed."
    mi "Who would have thought that I would come to the Union and meet here such a..."
    me "Such a what?"
    mi "Guess!"
    "Miku had thrown everything into the suitcase, and now it refused to close."
    "She tried to close it with her hands - in vain."
    "Quite predictably, her next step was to try to push it down with her full weight, kneeling on the rigid lid."
    "Little by little beneath all her forty pounds of numerous tresses began to tamp down, allowing the lock and shackle to come together."
    "Really, I knew how this might end, so I jumped up and, pushing sharply, quickly snapped the lock shut."
    show mi surprise pioneer with dspr
    mi "Ugh! Thank you! I would have gone out the window, like that cartoon, launched by the lid!"
    "I don't think you would have, but possible hit would be hard for sure."
    "However, I didn't talk about it - my one spontaneous gesture was enough to spoil the mood of both of us."
    "It took my breath away for a moment - imagined the bus stopping, Miku getting off - and getting into her father's arms, introducing me..."
    me "I would have caught you."
    mi "You wouldn't have made it!"
    me "Hello! I had time to close the lid on you! And I would have caught you. You can always count on me."
    show mi happy pioneer with dspr
    mi "Sen... Sometimes it seems that you're older than me."
    th "Not only seems..."
    "I didn't know if that was a compliment or an insult, and Miku continued:"
    show mi normal pioneer with dspr
    mi "And sometimes I feel like your big sister."
    mi "Are you always going to fool around?"
    "I had to make a thoughtful face here - I hope I succeeded."
    show mi sad pioneer with dspr
    mi "Sen, I'm serious!"
    me "Me too! I don't want to become a big, boring adult - I guess that's what you like. I don't know."
    "Well obviously not the looks - I've seen myself in the mirror, nothing special."
    me "Depression, by the way, is considered a sin. So you should look at life easier, more cheerful and direct."
    me "Yes, there may be difficulties ahead. Or rather, they are inevitable."
    me "But is that a reason to fold your paws, lie on your side, and suffer right now?"
    show mi surprise pioneer with dspr
    mi "No, of course not. It's just that sometimes I think that your non-serious attitude..."
    me "What?"
    show mi sad pioneer with dspr
    mi "It's nothing... It's nothing."
    me "No, you say «A», you say «B»!"
    mi "Okay."
    "With her eyes diligently looking away, Miku hesitated for a few seconds."
    "And finally she gave it out - so that where I stood, I sat down:"
    mi "I'm afraid you're going to take your commitment just as lightly."
    th "Ting-dong! We've got news! Turns out we've got some! Commitment!"
    me "Commitment."
    show mi normal pioneer with dspr
    mi "Semyon."
    "For the first time since we met, she called me by my full name, emphasizing the significance of the conversation."
    th "Yeah, it's really sad when you associate your name with trouble."
    mi "You made me some promises. I made you some promises."
    mi "So we have made commitments to each other."
    me "Are you implying that I might run away with my tail between my legs, scared of hardship?"
    show mi serious pioneer with dspr
    mi "Rather, you might just wave your hand when faced with something insurmountable."
    me "But I have you now. There's incentive!"
    mi "That's not it. You know?"
    me "No."
    "I answered honestly."
    me "I'm going to be with you, and to look for any hidden meanings in it, quit it."
    me "If you think too much, you get a headache."
    me "And anyway, when is the time to get excited about life and you, if today's schedule has us smooching and sprinkling ashes on our heads?"
    "Miku sat down on her suitcase and looked at me intently."
    "Her gaze was studying, somehow lost, or something..."
    "It was as if she had lost hope, but not faith. And that faith was in me."
    show mi normal pioneer with dspr
    mi "Maybe that's the only way to get through."
    "She whispered."
    me "Are we going to pick up my laundry?"
    "The conversations today were one more drawn out than the next. Instead of enjoying time together, we're getting discouraged."
    mi "You know... No. Go to your place to pack, and I'll go to the radio room and get the mixer."
    me "Can I help you?"
    show mi serious pioneer with dspr
    mi "Don't, Senechka. We'll get through this quicker, we'll have more time to be together."
    me "We're together now."
    show mi normal pioneer with dspr
    mi "Sen, please. We're six days side by side, parting only for naps."
    mi "I swear to you, I'm not going anywhere, but let's focus on running around for a little bit of downtime?"
    mi "Well? Deal?"
    "I was fundamentally opposed to that way of putting it."
    show mi smile pioneer with dspr
    mi "Sen."
    me "Yes?"
    mi "Seeeeenya."
    me "What?"
    show mi grin pioneer with dspr
    mi "I don't want to break up either. But we've been bargaining longer."
    "She was right again. Apparently she has a talent for being right."
    stop music fadeout 3
    th "I hope there's no embassy car and an emergency concert somewhere in the middle of nowhere while we're walking apart."
    me "See you around."
    hide mi with dissolve
    $ persistent.sprite_time = "day"
    $ day_time()
    scene bg ext_house_of_mt_day
    with dissolve
    play ambience ambience_camp_center_day fadein 2
    "In the absence of alternatives, I had to do as I was told."
    "I staggered back to my place."
    "And on the very doorstep, I ran into the counselor."
    show mt normal panama pioneer with dissolve
    mt "Have you packed your princess yet?"
    me "Yeah... Honestly, I'm surprised you're not scolding right from the start."
    show mt smile panama pioneer with dspr
    mt "As if I'd never been 17 years old..."
    "The counselor waved her hand."
    me "Yeah? And I thought you were already born so serious and..."
    mt "And boring?"
    show mt normal panama pioneer with dspr
    mt "Oh, how many of you I've heard. And how many have had their eyes opened."
    me "What are you talking about?"
    mt "You're big enough now. Why don't you try next year as an counselor's assistant ?"
    me "Why?"
    show mt laugh panama pioneer with dspr
    mt "Rest as an adult. I used to be called a «comet» here, and I was more restless than Ulyanka."
    "I found that positively hard to believe, but I nodded politely."
    me "I'm sure you weren't bored."
    mt "You don't believe it, do you? No wonder - used to a lazy counselor in a chaise lounge with a book who thinks a pioneer is a square sweeping machine."
    mt "You should come here more often, I'll surprise you."
    "She hobbled away, letting me into the cabin."
    play ambience ambience_int_cabin_day
    scene bg int_house_of_mt_day
    with dissolve
    "Throwing off my pioneer uniform, I put on an old T-shirt, girded up my jeans - I had to borrow an awl from the counselor's desk in order to pull a new hole - the jeans were inevitably falling off in my old position."
    "Winter boots, machine remnants in my pockets, sweater tied around my hips - I was ready for labor and defense."
    "The uniform took their place on the shoulders, the bedding in the pillowcase, the bed in the roll."
    "I was acting in machine mode, so it didn't immediately dawn on me that the counselor came in and said something to me:"
    mt "...hours. Hurry up."
    me "I'm sorry, what?"
    show mt smile panama pioneer with dspr
    mt "I say the bus is two hours early, so you only have time to get ready and get to the bus stop."
    me "What about Miku?"
    mt "I've already sent Slavya to help her."
    me "Doesn't Slavya need help herself?"
    show mt laugh panama pioneer with dspr
    mt "Why does she need help? She and I will escort you and be back tomorrow. She has a two-shift pass."
    me "Oh, yeah!"
    mt "That's what I'm saying. Come back again. Next year. Slavya will be there, too."
    mt "All right, there's no time to talk, go to the bus stop, and I'll run through the buildings and see if anyone's been forgotten."
    hide mt with dissolve
    stop ambience fadeout 2
    return

label alt_day7_mi_dj_departure:
    scene bg ext_bus with dissolve
    play ambience ambience_camp_entrance_day fadein 3
    "I was almost the last one to get to the bus stop - almost the whole camp was already here."
    "The pioneers were chattering away in an impatient manner, pacing back and forth, waving their arms."
    "It all gave the impression of a lively swarm."
    "And my sociophobic instincts reared their heads again in me."
    "To hide from the crowd, to plug my ears, to hide my head in the sand."
    show un normal dress with dissolve
    un "You don't like crowds, either?"
    "Lena approached unnoticed, even though a Soviet-colored checked suitcase on wheels was rattling behind her."
    me "Sort of..."
    show un smile dress with dspr
    un "And where did you lose the queen?"
    me "She'll be here soon, she has two suitcases, Slavya is helping her."
    un "Why don't you?"
    me "I'd love to, but we already missed each other once."
    "I smiled crookedly."
    show un normal dress with dspr
    me "I don't feel like it anymore. Running around the camp, looking for her when the departure is nearby... No."
    un "But you could have stayed..."
    "Thoughtfully Lena said."
    me "How?"
    show un smile dress with dspr
    un "To ask to work a shift change. Miku could get an extension on her pass, and... Well, you, too, of course."
    me "Not this time, I guess."
    un "Still in a hurry to get into each other's arms?"
    me "Not to say that..."
    "I fell silent, not knowing what to say. And when I turned back to Lena in an impotent attempt to find the words, I realized that I had been alone with myself for a couple of minutes."
    hide un
    with dissolve
    "Lena vanished."
    with fade2
    stop ambience fadeout 2
    "Finally, the first bus pulled up, and the junior counselors, after a quick head count of their boys, loaded up and set off."
    "Behind them came the fourth, third, and second squads..."
    with dissolve
    play music music_list["memories"] fadein 3
    "We were the last ones left."
    mt "Is everyone here?"
    "Asked Olga."
    "It seems..."
    "The gate creaked open, Slavya and Miku finally joined our close company."
    show mi smile casual with dissolve
    "Slavya left the second suitcase beside her and, winking at me, walked away to the main mass of pioneers."
    "I walked up to Miku myself."
    me "You look great!"
    mi "Really?"
    "Miku was a little nervous, waiting for my reaction to the outfit."
    me "Of course. Really, openly - I wouldn't let you out of the house like that."
    mi "Is it really that awful?"
    me "No. Everything is fine. But... No way! It's mine!"
    mi "Yours!"
    "Miku smiled, wrapping her arms around me."
    "And the counselor was making some kind of speech the whole time - no other way, about high responsibility and duty."
    "Well, or whatever she used to rave about at lineups."
    "A pioneer is always an example, especially if it's an example of how you can boot your neighbor."
    th "Comet - wow."
    dreamgirl "Not what you're thinking about right now. Don't forget to kiss your girl on the bus, otherwise..."
    th "Do you know something?"
    dreamgirl "What's there to know with you, clown, for sure? That's right, only that you're a clown."
    stop music fadeout 3
    scene bg ext_road_day
    with dissolve2
    play ambience ambience_ext_road_day fadein 3
    "Finally, a bus with a huge number «1» on the windshield turned around on the patch."
    mt "First squad! Fall in!"
    "Remains of the discipline hammered into us during the shift - we organizedly threw our suitcases into the luggage compartment and organizedly squeezed into the inside of the Ikarus - the same one, by the way, I remembered all those flags by the mirror perfectly."
    stop ambience fadeout 2
    scene black with fade2
    $ persistent.sprite_time = "night"
    $ night_time()
    scene bg int_bus_people_night
    with dissolve
    play sound_loop sfx_bus_interior_moving fadein 2
    with fade
    play music music_7dl["lynn"] fadein 3
    "How long has it been since departure?"
    "I've lost count - we've talked to Miku about everything there is to talk about."
    "Trying to predict her Pa's reaction."
    "We were even trying to figure out the best places for her to go while I'm growing into society."
    "We agreed it was best to leave tutoring as it was."
    show mi smile casual with dissolve
    "Six hours of unhurried marching."
    me "Miku, remember one thing, I want you to remember it no matter what happens."
    show mi grin casual with dspr
    mi "What thing?"
    "Miku was sitting next to me, but..."
    me "You can think of me as anything and take me any way you want."
    me "But I'm willing to take a risk, to try to start a life here - and that life should be dedicated to you."
    "I've considered whether or not I've spoken, and I've come to the conclusion that I've overlooked one point after all."
    me "You see, in my world, in my time, I'm older than I am here."
    mi "Wow! How much?"
    me "By a very «much», Miku."
    show mi happy casual with dspr
    "Miku blushed."
    mi "How «much»?"
    me "Closer to thirty."
    mi "So you're a big man!"
    scene cg d7_mi_epilogue_bus_7dl with dissolve
    "She snuggled up to me, rested her head on my shoulder."
    me "I mean, none of that matters. The most important thing to me is you. I'm only here and now for you."
    mi "You say the loveliest things... Must have driven a lot of people crazy with your chatter, huh?"
    "She purred sleepily."
    me "Yeah. A whole lot of people. I have a feeling something's going to happen very soon. So... You hold my hand, okay?"
    "Miku didn't answer."
    "As I looked down, I saw that she was asleep. And smiling in her sleep."
    "For a moment her lips moved and distinctly said,"
    mi "Senechka."
    with fade2
    "Little by little the whole bus fell asleep."
    "From the back seats the gambling slapping of cards ceased, from the front seats Olga finally fell silent, singing in a whisper some local hymns."
    "That left night, the sleeping bus, the hum of the engine - and me."
    "Miku's head was resting on my shoulder, it was peaceful and quiet."
    "I didn't want to move so as not to disturb the girl."
    if alt_day6_mi_dj_catapult not in (1, 2):
        menu:
            "Fight the sleep":
                "I don't have much time to waste on sleep."
                "Especially now."
                "When we got together."
                "I tried my best to accommodate as much as I could, pinching myself, shaking my head - trying my best."
                "In vain."
                $ alt_day6_mi_dj_catapult = 1
            "Take Miku's hand":
                "She had a warm, soft palm."
                "I'm sorry, I couldn't help it."
                "Put it to my lips."
                "And the girl smiled quietly in her sleep, repeated my name clearly."
                me "See you in the morning, sunshine."
    "I covered my eyes and dozed off."
    stop music fadeout 3
    stop ambience fadeout 6
    stop sound_loop fadeout 3
    with fade
    return

label alt_day7_mi_dj_epilogue_frost:
    play music music_7dl["frostwithoutyou"] fadein 3
    $ alt_pause(3)
    scene
    $ renpy.show("cg d7_mi_epilogue_7dl", what = Dawn("cg d7_mi_epilogue_7dl"))
    with fade3
    "I'm freezing without you."
    "You must hate me already - at least for not keeping a simple promise."
    "For not being able to."
    "And I miss you."
    "And again I don't know what to do."
    "Maybe if I'd held you tighter, if I'd loved you more, if I'd just wanted to, sincerely, from my heart, it would have been different."
    "Could it be?"
    $ alt_pause(3)
    scene
    $ renpy.show("cg d7_mi_epilogue_7dl", what = Desat("cg d7_mi_epilogue_7dl"))
    with fade
    $ alt_pause(1)
    $ set_mode_nvl()
    "I knew somewhere that this was what was going to happen, so I wasn't the least bit surprised when I closed my eyes on the bus, carrying one silly pioneer through the summer night toward a pipe dream."
    "And then I opened it... The promised rubber band pulling me was stronger - and with a sharp snap yanked me home."
    "Or maybe it was the cracking of a taut nerve - dry, like the clicking of a firing pin on a blank spot in a drum during my con in Russian roulette, and my useless brains not flying to paint bright gray into bright red."
    "Or maybe it sounds like the torn flesh that you're embedded in alive?"
    "I won't challenge your right to have your own opinions - about me, about yourself."
    "But it makes me want to kick myself at the thought that you've found someone better than me."
    nvl clear
    "It makes me want to cut myself at the thought of finding someone who isn't you."
    "You're the best thing that ever happened to me. You're the only thing that ever happened."
    "What has become of that naive girl who crosses the stage with a fervent stride and loves the whole world, finding a corner in her heart for me too?"
    "But when it aches and whines inside with a tearing pain, one that I am not able to deal with..."
    "I wake up in a nightmarish delirium, as if you were gone. A tenfold nightmare because it is my reality."
    "Without transitioning from the hum of the bus engine - to the howling wind outside the hood, the rolling bass in the in-ear headphones and the tugging weight of dirty air to the ground, the empty indifference in the eyes of those around me..."
    nvl clear
    scene bg ext_city_night_7dl
    with dissolve
    play ambience ambience_cold_wind_loop
    "I walked away from home, flinching and hiding my reddened eyes from passersby and flashes of memory."
    "A short, beautiful street, running up a bridge into the sky."
    "When I got to the right place, I climbed over the fence, walked up the service stairs, and stopped where the granite of the bulls passed into the riveted steel."
    "I was willing to go to hell, if only to give me the slightest chance of seeing her again."
    "I sat down on the steel railing, threw my legs over the other side."
    scene black
    with dissolve
    "Then there was darkness and silence."
    nvl clear
    $ alt_pause(1)
    scene bg ext_city_night_7dl with dissolve
    "For some reason I woke up in the body of a young man with my face, but biologically older than me, physically stronger, socially more successful."
    "Nearby there were rustling tires, rumbling streetcars, rushing people - and I was breathing and assuring myself that I was alive. Not for long, until I remembered why I was here."
    "The hardest part was not getting in without a memory - the passport in my pocket indicated a Leningrad registration - and not recovering the contacts of that one person inside whom I had opened my eyes."
    "It was more difficult with the flight to Japan. But in the end the necessary documents were arranged - it seems that «me» whose place I took was in good standing with the local authorities."
    "The savings left by the owner of the body also came in handy."
    "It must have been some kind of endurance test."
    nvl clear
    $ alt_pause(3)
    "Calls from some people. A woman's voice, to which «I» almost responded. Not me, the other one."
    "It didn't matter."
    "I didn't let myself relax for a moment, feeling myself gradually assimilating with the host, our memories becoming shared."
    "Close my eyes - imagine. Whose memory? Discarded and three hundred times cursed skates, abandoned to the farthest corner after a leg injury."
    "Why was it necessary to get them, why was it necessary to grieve the memory?"
    "Where did that memory come from, anyway? We'd only seen each other once, but for a whole week. In the summer. Six days of summer Miku."
    "And I can't resist asking her again. And my ankle is stabbing again with phantom pain."
    "And the icy dust tends into the sky from braking too sharply, but the body itself remembers how to stand, how to move."
    "As if now, on a roll, for the sake of admiring eyes, it has agreed to forget what happened as a child."
    "A little clumsy bear, waddling on skates to please a pretty girl with very sad eyes."
    "And the sun is refracted in the icy suspension, illuminating it with a scattering of diamonds."
    "In the cooling air and the fading memory that still won't heal."
    nvl clear
    "It took all my courage, all my remnants of callousness and detachment, just not to shake at the inspection. I answered some questions, and watched the panorama unfolding in my mind."
    "I tried to hold on to myself - Semyon, the one living in front of the monitor, the one who drew the lucky ticket to the non-existent camp. After all, it was he who owned the most important treasure - the memory of a very beautiful girl."
    "So the flight was not at all memorable. Both seats next to me were vacant, something sweet was served in the cabin, and I drank without feeling the taste."
    "The address in Sapporo was clearly imprinted in my mind. For some reason it meant a lot to that «me», so I headed there first."
    "It took my breath away when I saw the familiar characters on the door. I tried to calm down and knocked."
    "An unfamiliar woman opened the door for me. I introduced myself."
    nvl clear
    scene
    $ renpy.show("cg d7_mi_epilogue_7dl", what = SS_com("cg d7_mi_epilogue_7dl"))
    with fade
    "Why is this woman, still young, still gray-haired, hiding her eyes?"
    "Where is my Miku?"
    "Where is she?"
    "Where is this woman asking to go with her in a confused voice? Is it to Miku's apartment?"
    "We got into the cab, she told the driver the address and handed him some appropriations."
    scene bg ext_japan_graveyard_rain_7dl with flash
    play ambience ambience_7dl["rain"] fadein 3
    nvl clear
    "The flat granite slab with vertical stitching is one of tens of thousands in this scrupulously civilized place."
    "Familiar characters."
    "Hatsune Miku, August 31, 1972 - May 24, 1991."
    "The world trembles and swims in my eyes. What? What is it?"
    "I fall to my knees, broken in half by a flash of scarlet, stabbing pain - remembering, remembering..."
    "It's as if something, hitherto dormant, has now awakened within me and thrown the blinders off the memories that have been mercifully hidden beneath the thickness of the years."
    nvl clear
    scene bg ext_busstop_sun_7dl
    show prologue_dream
    with dissolve
    "{i}I'm sitting alone at the bus stop. How did I end up here?{/i}"
    "{i}I remember letting the ships out with the boys, and they told me not to follow the ships, but I wondered where they were going.{/i}"
    "{i}Then the bus came. I hoped it would take me to my stop.{/i}"
    nvl clear
    scene bg ext_street_night_7dl
    show prologue_dream
    with dissolve
    "{i}We had gone about ten minutes when the bus stopped and went no further.{/i}"
    "{i}I got off the bus and literally bumped my nose into someone's bare legs.{/i}"
    "{i}I don't know why, but I was literally won over by the stranger's hair - long, gathered in two ponytails - even more than her exotic appearance, very beautiful, very young. And very sad.{/i}"
    scene
    $ renpy.show("cg d7_mi_lost_7dl", what = Sepia("cg d7_mi_lost_7dl"))
    show prologue_dream
    with dissolve
    show alt_credits "Are you lost, kid?" with dissolve2:
        pos (145, 250)
    "{i}I told how I came here by bus, but I couldn't get home. A stranger asked me where I lived.{/i}"
    "{i}I remembered my address, of which I was very proud. Even the city with the long name. St. Petersburg.{/i}"
    "{i}When I told a girl where I lived, she was very surprised and wanted to know my name.{/i}"
    am "{i}My name is Senya. That is, Semyon. Persunov.{/i}"
    mi "{i}Nice to meet you. And my name is Miku.{/i}"
    "{i}Why are there tears in her eyes?{/i}"
    mi "{i}Let's take you home, otherwise...{/i}"
    nvl clear
    scene bg int_hospital_hall_day_7dl
    show anim_grain
    with dissolve
    "{i}I never made it home. Instead, they took me to the hospital. They asked me how I got here, who my parents were.{/i}"
    "{i}I tried to find out when they would take me home, but for some reason the adults said I would have to stay here for a while.{/i}"
    $ alt_pause(3)
    "{i}It's been a month, and I've been allowed to go to the park.{/i}"
    "{i}They take me down to the foyer, where a welcoming she is already waiting.{/i}"
    show mi smile casual with dissolve
    mi "{i}We meet again, kid.{/i}"
    "She's smiling."
    mi "{i}How are you?{/i}"
    nvl clear
    am "{i}And I remember you.{/i}"
    show mi surprise casual with dissolve
    mi "{i}Really?{/i}"
    "{i}The stranger shuddered visibly.{/i}"
    mi "{i}And what do you remember?{/i}"
    am "{i}I remember when you met me at the bus.{/i}"
    mi "{i}There's a clever boy.{/i}"
    "{i}She looked up at the ceiling, blinking often.{/i}"
    mi "{i}Now let's take a walk. You must be very bored here?{/i}"
    "{i}It's her again - an unchanged, very beautiful girl with huge, sad eyes the color of a sea wave, with long, long hair tied up with pins on either side of her head in two ponytails.{/i}"
    "{i}Two memories from early childhood. Two crumbs.{/i}"
    nvl clear
    scene bg ext_japan_graveyard_rain_7dl
    show prologue_dream
    with dissolve
    "I'm soaking in the rain, running my fingers over the hieroglyphs carved in the stone."
    scene cg d7_mi_hugs_7dl behind prologue_dream:
        pos (0,-1920)
        linear 15.0 pos (0,-500)
    "{i}A few more months passed, and we see each other again.{/i}"
    "{i}I told her I'd marry her when I grew up.{/i}"
    "{i}She always laughed when I said those things.{/i}"
    "{i}And then she cried, screaming into the low sky.{/i}"
    "{i}Choked on the rain, shut up, pressed me against her, stroking my hair.{/i}"
    "{i}Fearful, I tried to protect her.{/i}"
    "{i}Or to protect myself.{/i}"
    "{i}I got scared of how easy it is to hurt someone.{/i}"
    "{i}How wrong it is! You can't do that, you can't do that!{/i}"
    mi "{i}I'll have to go away for a few months.{/i}"
    "{i}She said, after calming down a bit.{/i}"
    mi "{i}And then I'll come and see you.{/i}"
    "{i}Lies.{/i}"
    "{i}Children, animals, and dying people - they all feel death on their doorstep too keenly to be brushed aside.{/i}"
    "{i}I don't want to let her go.{/i}"
    "{i}And she squatted down in front of me and hugged me gustily, with all her strength, exhaling:{/i}"
    mi "{i}Why didn't you keep your promise? {/i}"
    nvl clear
    "{i}Hatsune Miku.{/i}"
    "{i}She never came since then.{/i}"
    "{i}Instead, I came - stabbing and scratching my heart with a familiar pair of kanji.{/i}"
    me "{i}The future... {w}Mirai... {w} Miku.{/i}"
    "{i}Desperate future.{/i}"
    "{i}Desperate Miku.{/i}"
    "{i}From the photograph taped under the clear plastic, priceless huge aquamarine eyes looked at me from beneath aquamarine bangs.{/i}"
    "{i}I have dreams after which it's easier to feel like nobody needs me.{/i}"
    "{i}I wonder if a heart attack at thirty is early or not.{/i}"
    nvl clear
    voice "Miku, for some reason, asked me very much to give this to a man named Semyon."
    me "And you..."
    voice "Mother."
    "She handed me a bag."
    voice "Open it somewhere drier, will you?"
    "An hour later, jostling around the neighborhood, I sit on the bed and with shaking hands open the hermetically sealed package. Strange objects, unfamiliar at first glance, but..."
    "A quadruple folded piece of paper in a box, scribbled in a very familiar handwriting."
    stop music fadeout 10
    if alt_day6_mi_dj_walkman:
        "The click wheel on the walkman must have fallen off after all."
        "The walkman itself is old and shabby."
    "And a strand of aquamarine hair under the cover of Hatsune Miku's CD."
    stop ambience fadeout 2
    nvl clear
    scene cg d7_mi_letter_7dl with dissolve
    $ alt_pause(3)
    play music music_7dl["lastlight_piano"] fadein 4
    "Letter."
    "Hello, Senechka."
    "The world is not the same as it was with you and me."
    "There on the bus, when {i}you{/i} opened your eyes, I knew at once it wasn't my Senechka."
    "{i}He{/i} looked at me as if he'd never seen me before, and to all my questions, he just looked away."
    "I woke up alone, even though I fell asleep on your shoulder."
    "The world is no longer the same as it should have been yours and mine."
    nvl clear
    "How am I doing? Not good."
    "I'm performing. Singing. I write music and lyrics."
    "And they don't seem to be any worse than others, and people shake their heads in tune when they listen to them."
    "But it's not the same."
    "There is no you in them, you know?"
    show alt_letter "I miss you..." with dissolve2:
        pos (1400,360)
        linear 3.0 pos (1400,220)
    hide alt_letter with dissolve2
    "Sometimes I wish I could close my eyes and go back to camp - where you come to visit me, hiding your tears under your bangs, your rage under your keystrokes."
    "But that's only what happens in fairy tales."
    "In silly, naive romances where the heroes happily reunite."
    "It didn't work out happily ever after for us."
    "You're a handsome young man six years old, and of course you don't remember me."
    nvl clear
    $ renpy.show("cg d7_mi_letter_7dl", what = Desat("cg d7_mi_letter_7dl"))
    with dissolve
    $ alt_pause(1)
    scene cg d7_mi_letter_7dl with dissolve2
    "I guess there really are some laws of the universe you can't cheat. I'm stupid, I know, but I'm holding out hope that I'm about to put a stop to this letter and you'll appear before me."
    "A real one."
    "Adult."
    "Mine."
    nvl clear
    scene cg d7_mi_letter_rain_7dl with dissolve
    "You'll look me in the eyes with your usual unsmiling smile, say another profound thing that I'll think about until morning, and take me with you to a country where Skype, the Internet, and personal phones are in use."
    "I've almost forgotten how to believe in you, but I keep believing in a miracle."
    "You never wanted to become part of society, instead you just disappeared."
    "After all, that's the easiest thing to do."
    "Don't think I'm blaming you."
    "You really couldn't seem to control it."
    nvl clear
    scene
    $ renpy.show("cg d7_mi_letter_rain_7dl", what = Desat("cg d7_mi_letter_rain_7dl"))
    with dissolve
    $ alt_pause(1)
    scene cg d7_mi_letter_rain_7dl with dissolve2
    "You know, counting down the 108 New Year's Eve strokes, cracking a fortune cookie - just throwing a coin in the fountain for good luck - I always make the same wish."
    "I wish for December 29 - isn't that the day this story began?"
    "I wish for Russia, I wish for the eighteenth year."
    "I want you."
    "Statistically speaking, any event, even the most improbable one, has every chance of coming true if you try it on to the infinity of the universe."
    "And I will dial your number and hear your voice. Although, of course, that's unscientific fiction - I've dialed every number you've left me hundreds of times before."
    "You're not there."
    "But I'm still hopeful."
    show alt_letter "I want to be with you..." with dissolve2:
        pos (1200,360)
        linear 3.0 pos (1100,220)
    hide alt_letter with dissolve2
    nvl clear
    scene cg d7_mi_letter_rain_tears_7dl with flash
    "The greatest value is your smile, though you smile so reluctantly."
    "A pipe dream that I wound, wound, but can't help touching it."
    "Why was all this with us at «Sovyonok» anyway? Is that fair?"
    "I want to learn how to draw."
    "And I'm going to draw you."
    "Otherwise one day I'll forget what you look like, and there'll be one less miracle in the world."
    "Right now, while you're still in heat distance..."
    "You called our engineers brilliant, but why haven't they yet come up with a machine that draws my dreams?"
    "Because they are full of you."
    nvl clear
    scene
    $ renpy.show("cg d7_mi_letter_rain_tears_7dl", what = Desat("cg d7_mi_letter_rain_tears_7dl"))
    with dissolve
    $ alt_pause(1)
    scene cg d7_mi_letter_rain_tears_7dl with dissolve2
    "Maybe you really never existed and I was just having a dream. That I got sick."
    "You're as far away as the sky."
    "I tried, you know?"
    "I guess all I have to do is wait. And one day you'll find me."
    "I'll wait for that."
    nvl clear
    scene
    $ renpy.show("cg d7_mi_letter_rain_tears_7dl", what = Desat1("cg d7_mi_letter_rain_tears_7dl"))
    with dspr
    show alt_letter "Your Miku." at truecenter with zoomin
    with dissolve
    $ alt_pause(4)
    hide alt_letter with dissolve2
    scene
    $ renpy.show("cg d7_mi_letter_rain_7dl", what = Notch("cg d7_mi_letter_rain_7dl"))
    with dissolve
    "That's it."
    nvl clear
    me "I kept my promise after all."
    "Staring dumbly at the ceiling, I said."
    me "And you... Fooled me."
    scene black with fade
    "The rest was like a dream - customs clearance, abandoned things in a storage room, a twelve-hour flight to Pulkovo..."
    scene bg ext_musclub_snowy_day_7dl
    show prologue_dream
    with fade
    "I was attentive, I searched like the damnedest before I found a few pictures where the ruins of buildings that had fallen inside themselves - once airy, flying - were rotting in the sun."
    "A brig, a canteen with a huge canopy over the porch, a music club..."
    scene bg ext_mv2_7dl with fade
    me "To Kalinin one, any one."
    voice "Platz, side, by the toilet."
    "I don't care."
    voice "Passport. Passport."
    voice "Do you hear me?"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_mi_dj_bad:
    scene black with fade
    $ set_mode_nvl()
    play music music_7dl["lost_without_you"] fadein 3
    "I don't really hear that."
    "What I hear is «kh-psssshhhhhhh» mixed with a tinny cough."
    "But whenever the electronic public address system glitches, one of those inconsiderate and voiceless aunts sits on the microphone, speaking with an articulation worthy of other South Americans."
    "There are six more hours of travel ahead, filled with reading and music."
    "This will be the longest trip in several years, so I'm loaded to the brim, scattering cash in several pockets and cramming stuff into my bag for seemingly every occasion."
    nvl clear
    scene bg ext_winter_night_7dl with dissolve
    play sound_loop sfx_bus_interior_moving fadein 4
    "I don't think I'll need them, though."
    "But I have to think about what's left of me."
    "So go straight to Kalinin, and then... We'll see."
    "Why am I going there? What kind of stupid question is that?"
    "I don't ask stupid questions of those around me; they, respecting my opinion, don't pry into my soul."
    "Or maybe it's the widespread unfriendliness of Muscovites?"
    "I remember once I wanted to ask for directions there - so, in my usual manner, I stopped the first passerby I saw."
    "I won't quote his answer in full, but he didn't seem to explain anything."
    nvl clear
    "Of course, it's not the 410 or even the expected Ikarus."
    "No, it's a comfortable bus with an expected mustachioed driver and a pop classic that the rest of us must listen to for the next three hours of the trip."
    stop sound_loop
    stop music fadeout 3
    nvl clear
    $ alt_pause(3)
    scene bg ext_entrance_winter_7dl with dissolve
    play sound sfx_intro_bus_stop_steps
    play music music_7dl["no_hope_left"] fadein 3
    "There is no longer any Sovyonok, there is no star from the sash joint or the brick fence."
    "An abandoned, cursed place."
    "It once broke one girl's life - another generation of ruins was the result."
    "Now it's ruined my life too."
    "I wandered knee-deep in snow, noting automatically the loose shutters, the dilapidated huts, the gatehouse that had no glass and snow piled almost to the ceiling."
    scene stars
    $ renpy.show("bg ext_houses_snowy_day_7dl", what = D3_intro("bg ext_houses_snowy_day_7dl"))
    with dissolve
    "And I myself was all there - in the past, indelible, unerasable from tormented heart."
    "There is only one question."
    me "Is that it?"
    "A frosty cloud fell from my lips and drifted off into the darkness of loneliness that only a graveyard can have."
    if alt_day_binder != 1:
        "Electronik said that the children are brought in, they dress up Genda, decorate the Christmas tree..."
    nvl clear
    "Too many lives have been broken in this place, which, by a wicked irony, has served as a children's camp for many years."
    "All that remains here is the dead whiteness of untouched snow."
    "And the echoes of a child's laughter, sounding like the clap of one palm."
    "And my happiness. The unfulfilled."
    nvl clear
    "The concrete tile path can't be seen from under the snow."
    "But I don't need it - I remember it like it was yesterday."
    "I remember everything. I have the greatest treasure of all - memory."
    "Memory. That's all I have left."
    "It's ten minutes to midnight, the  General Secretary is on TV somewhere, and the country is silent."
    "And I put my hand in my pockets and take out..."
    "From the Volga comes the burst of the first salute - there the walkers have already listened to the leader's address from their portable televisions and are hurrying to enter the new year of 2019. Only I bogged down in August 1989."
    me "Happy New Year, sweetheart."
    "I turn to nowhere."
    me "Even though you left me, I still miss you very much."
    "And just like that time in the cemetery, over my girl's grave, it folded me in half."
    nvl clear
    $ alt_pause(3)
    scene
    $ renpy.show("cg d7_mi_epilogue_7dl", what = SS_com("cg d7_mi_epilogue_7dl"))
    show prologue_dream
    with flash_red
    "She always has been."
    "Always!"
    "{i}It's the end of May outside, it'll be summer very soon, but judging by the rain, you can't tell.{/i}"
    "{i}And I haven't trusted anyone or anything for more than half a year now.{/i}"
    "{i}But I stand in the glass box of the Pulkovo terminal and look at the slender «Tushka» coming in for boarding, for there will be my personal guardian angel, with exotic eyes, with incredibly long hair.{/i}"
    "{i}The one person I trust unconditionally.{/i}"
    "{i}Once again today I proved to everyone that only I decide my own destiny - I ran to meet her and tell that I want her to take me with her.{/i}"
    "{i}Any place, wherever she is.{/i}"
    "{i}I'm already all there - in dreams, in a rainbow future where...{/i}"
    nvl clear
    $ alt_pause(3)
    "{i}And so it was not immediately clear what was happening when the shabby airplane seemed to hit the wall, plummeting down, onto the released front landing gear.{/i}"
    "{i}And just like in the movies - in slow motion - I saw, gaping in mute scream, how this chicken-leg-like structure snapped, how the huge black wheel flew aside, how the fuselage began to collapse.{/i}"
    "{i}It was as if I'd blacked out. I woke up on the runway, kneeling on the wet concrete next to the rough stretcher made of tarpaulin on aluminum horns, and I kept thinking - why the tarpaulin, because all the airports in the world have been using plastic, it does not absorb blood!{/i}"
    nvl clear
    scene black with dissolve
    $ alt_pause(3)
    "{i}She was lying on such a stretcher, pale but still beautiful.{/i}"
    "{i}And her body was half covered with a thick sheet, sagging frighteningly where a normal person's legs would begin.{/i}"
    mi "{i}Hi, kid...{/i}"
    "{i}With effort, she said.{/i}"
    mi "{i}It looks like someone above really doesn't want us to be together.{/i}"
    "{i}A few words seemed to exhaust her reserve of strength - her face was not white, but literally grayed with pain, her eyes rolled back.{/i}"
    "{i}And I was yanked aside by some men in uniform - an intensive care car was already rushing across the field, and I kept rushing and rushing to her.{/i}"
    nvl clear
    $ alt_pause(3)
    "{i}Severe piloting technique violation... vertical speed... stiffening ribs... out of two hundred casualties, only two... died.{/i}"
    "{i}Only two.{/i}"
    nvl clear
    $ alt_pause(2)
    scene stars
    $ renpy.show("cg d7_mi_farewell_7dl", what = D3_intro("cg d7_mi_farewell_7dl"))
    with dissolve
    $ set_mode_adv()
    "She was always - forever young. {w}And I... I didn't know myself why I had to come here."
    "But now everything's fallen into place."
    "Cats also go to die where no one can find them."
    "So the three of us are going to sit a little longer - me, my memory and my loneliness."
    me "Wherever you are, I hope you're happy."
    "A throat-burning tribute."
    "Burning the heart."
    "A player and a heavy wicker bracelet, frozen in the snow."
    "A tear on my cheek."
    "And the eyes will be opened by someone who's never been to Sovyonok with Miku."
    "The one she never called «Senechka»."
    "So it will be."
    me "Goodbye."
    "I turned to the one who so patiently tolerated my presence in his head."
    me "And... thank you. Happy new year to you."
    me "Happy new year."
    show blink
    "I closed my eyes."
    scene black
    play music music_7dl["emptiness"] fadein 3
    scene anim prolog_2 with fade3
    "\[Bad ending unlocked - «Happy New Year!»\]"
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("mi_dj_bad")
    show acm_logo_mi_dj_bad with moveinright:
        pos (1600, 1020)
    $ alt_pause(7.4)
    call alt_7dl_titles
    $ alt_pause(1)
    return

label alt_day7_mi_dj_true:
    $ set_mode_adv()
    $ persistent.sprite_time = "day"
    $ day_time()
    scene black with dissolve
    $ alt_pause(3)
    play music music_list["a_promise_from_distant_days"] fadein 3
    scene bg int_bus
    with diam
    play sound_loop sfx_bus_interior_moving fadein 2
    "I shudder - and open my eyes."
    "In the cabin of the bus."
    "The same one that once brought me to camp."
    $ meet('uv',"Voice")
    uv "Here you are again. Same place, same time."
    "The voice was very familiar."
    show uv normal with dissolve
    "Somehow I wasn't surprised at all when I turned my head toward its owner."
    "Of course I should have been, though. It's not every day you see girls with such outlandish ears."
    $ meet('uv',"Catgirl")
    uv "You squandered your one chance. What are you going to count on now?"
    me "A better outcome. For both of us."
    uv "You've already been a better outcome once. Well, look where it got you now..."
    me "It doesn't change anything!"
    me "Since we can only be together here, then my place is here, too."
    me "If you don't try it, it won't work."
    uv "Then you'd better try this time. There won't be another chance for sure."
    me "So be it. Then I'll have to wrest my happiness from fate."
    show uv smile with dspr
    "The girl smiled."
    uv "Well, good luck then!"
    "The bus stopped."
    stop sound_loop fadeout 2
    uv "She's waiting for you. I think you can take it from here."
    scene
    $ renpy.show("bg ext_camp_entrance_day", what = Dawn("bg ext_camp_entrance_day"))
    with fade2
    play ambience ambience_camp_entrance_day fadein 6
    "The bus drove away, leaving me in front of the gate of «Sovyonok»."
    with fade
    show sl smile pioneer with dspr
    sl "Hello!"
    me "H-Hello."
    "Cautiously I replied."
    "I couldn't get away from the impression that I was an actor in some kind of production. So I took a deep breath."
    sl "Olga Dmitrievna sent me to meet you..."
    "And asked what I really cared about."
    me "Tell me, please, is Miku there?"
    show sl surprise pioneer with dspr
    sl "You know Miku?"
    "Slavya surprised."
    me "I'm... Let's just say I'm a big fan of hers."
    "I smiled."
    me "You don't have to show me the way; find it myself."
    play ambience ambience_camp_center_day fadein 1
    scene
    $ renpy.show("bg ext_clubs_day", at_list = [zentercenter], what = Dawn("bg ext_clubs_day"))
    with dissolve
    "The smell of breath with a hint of licorice, the essential oil with the scent of eucalyptus, the taste of kissing lips - dry as the red-hot afternoon of the camp that never existed."
    "Silly, silly."
    "But my head heats up genuinely hot, and my clothes fall off me again - because they're sewn on someone a little bigger than me, a little bulkier."
    "A meter and a half of carefree, hypnotically floating hair. {w}And a cheerfulness inherent in only one creature in all the observable universes."
    scene cg d4_mi_hedgehod_7dl
    show prologue_dream
    with fade2
    $ alt_pause(3)
    "And I scatter, emboldened by the silver bell of a voice calling to defeat the monster for the glory of his princess, and, after taking a few steps, I leap!"
    "Hovering in the air according to my unfulfilled dream of flight in reality, I fly - and the white cotton of my shirt becomes a dungeon to the terrible monster, snorting and stomping loudly."
    mi "How cute!"
    "My sunshine is adorable, carelessly extending a finger toward the predatory pointy face."
    "And if it weren't for my reaction, he'd claw wherever his sharp teeth can reach."
    me "Miku, be careful!"
    "I'm pulling back."
    me "Hedgehogs bites are very painful."
    "The beast is defeated, the brave knight wipes his trusty blade on the grass and tosses the steel carelessly into its scabbard. Now we can go and get our well-deserved reward!"
    "How about that! Even though I still secretly cherish the desire to cut off a lock of my hair, a bracelet of some silk ribbons has already found its place on my wrist."
    "Woven in there, too, is the color of my heart's lady. Miku has rewarded me for helping me in my trouble."
    scene
    $ renpy.show("cg d6_mi_farewell_7dl", what = Desat("cg d6_mi_farewell_7dl"))
    show prologue_dream
    with fade2
    $ alt_pause(3)
    mi "You know..."
    "She stands with her back to me without turning around, looking somewhere in the distance, where a cloud front slowly gathers over the valley."
    mi "In my homeland the climate is mild-soft, Fuji-san holds the winds, and the transitions between seasons are more often evident in the plants than in the temperature."
    "She squares her shoulders  -and stays that way in my memory forever: impossibly thin, chin up, putting her left leg to the side."
    "A girl of mystery, who, for some reason, listened to the nonsense I usually talk - and got it right."
    "The little girl who made this universe one lighter feeling warmer."
    mi "And you have a direct sense of summer crossing the midway point and rolling back in waves toward the southern latitudes, making way for cooler weather."
    me "Is winter coming?"
    "I ask jokingly."
    mi "Coming."
    "I walk up behind her, intending to hug her by the shoulders, but she turns around abruptly, and for a second I'm creeped out by her grown-up stare."
    mi "Explain it to me, Semyon."
    "Strictly she asks."
    mi "Why are you wasting your time on me? I'm bad, defective, I have to be corrected and yelled at all the time."
    me "Do you want the right version or the true version?"
    mi "The real one."
    "And the real version is that that's all I want - with all its wrongness."
    scene
    $ renpy.show("bg ext_musclub_day", what = Desat("bg ext_musclub_day"))
    show prologue_dream
    with fade2
    $ alt_pause(3)
    "I closed my eyes and held my breath, waiting for my rightful miracle. Now, somewhere in the bowels of the world, a gear would turn, and a stray ray of sunlight would tickle my delicate skin, make my charming nose crinkle a little."
    "One girl with huge aquamarine eyes will be sad for a second, not knowing why."
    "And in the light, airy building with its huge windows, the sound of the sheet music will flutter into the sunny wind, more like a heartbeat."
    $ alt_pause(2)
    scene
    $ renpy.show("bg ext_musclub_day", what = Dawn("bg ext_musclub_day"))
    with dissolve
    "The first step habitually creaks underfoot."
    play sound sfx_door_squeak_light
    scene
    $ renpy.show("bg ext_musclub_day", at_list = [zentercenter], what = Dawn("bg ext_musclub_day"))
    with dissolve
    "Everything here is painfully familiar-hanging overhead, the long benches, the socket where they used to plug in a tape recorder for outdoor rehearsals."
    "Even the round handle, slipping out of my weakened fingers."
    play sound sfx_knock_door2
    scene
    $ renpy.show("bg int_musclub_day", what = Dawn("bg int_musclub_day"))
    with fade
    play ambience ambience_music_club_day fadein 1
    play music music_7dl["ourfirstmet"] fadein 1
    $ alt_pause(1)
    show mi normal pioneer with dissolve
    mi "Hello."
    "The Sea of Japan is reflected in my darling eyes, and the world is smoothly frozen, stopping a moment that will be with me for the rest of my days."
    mi "You must be new?"
    "She frowns, not recognizing."
    me "Miku."
    show mi upset pioneer with dspr
    mi "Yes! And how do you know my name? The counselor probably told you, didn't she? I don't get a lot of visitors here, and you're new here, so they probably sent you around camp. But you come in, of course, we always sit here. I mean me. But if you come in, we'll sit together!"
    me "You know..."
    "Slowly I utter, and tempted not to burst into tears, my lips are burning like acute allergies..."
    me "If you don't want people to run away from you, try talking like you sing. One phrase, one thought."
    "Though who will ever believe that foolishness?"
    scene
    $ renpy.show("cg d7_mi_reenter_7dl", what = Noon("cg d7_mi_reenter_7dl"))
    with flash
    with hpunch
    "It creaked under my feet once, when the space between my palms was gone. The space between my lips was gone."
    th "I'll never run away from you."
    "She almost knocked me down, but it didn't matter now."
    "Miku."
    me "Miku."
    scene
    $ renpy.show("cg d7_mi_reenter_7dl", what = Dawn("cg d7_mi_reenter_7dl"))
    with dissolve
    mi "Semyon? But how..."
    me "Be silent."
    "I put my finger to her lips, more afraid than death of waking up now."
    scene cg d7_mi_reenter_7dl with dissolve2
    me "My Miku."
    stop ambience
    scene anim prolog_2 with fade3
    "\[True ending unlocked - «My Miku»\]"
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("mi_dj_true")
    show acm_logo_mi_dj_true with moveinright:
        pos (1600, 1020)
    $ alt_pause(7.4)
    call alt_7dl_titles
    $ alt_pause(1)
    return

label alt_day7_mi_dj_good:
    play music music_7dl["knock"] fadein 5
    pause(3)
    scene cg d7_mi_epilogue_7dl with fade
    pause(1)
    $ set_mode_nvl()
    "This world has definitely gone crazy. You just have to figure out at what point."
    "Just close your eyes, take a breath, and set the very inflection point after which everything went downhill."
    "Come on?"
    "The Japanese have always been a total screw-up in this regard, the Japanese, the Koreans, they're all over this technology stuff."
    "All that nonsense with laser shows, smoke, pyrotechnics, computer technology."
    "And the crowd cheers in the darkness, whose breath sounds like the beating of a huge heart - selflessly in love with a figure dancing on stage with a beautiful, if slightly unnatural voice."
    "And there's a shimmering wave from the back rows to the front rows - because the glowing green sticks only cost five dollars, but they shine so beautifully, and they're literally being bought up at the drop of a hat."
    "So are caps, T-shirts, slippers, pens, mugs, stickers and other souvenirs that suddenly become very important, very meaningful overnight."
    "After all, it depicts her - huge eyes, her hair gathered in two ponytails of unusual color, of extraordinary length."
    "Just ten years ago, who could have believed that a girl who didn't exist would draw whole halls?"
    nvl clear
    pause(3)
    "We should have sounded the alarm back in 2007, when a synthesized voice sang a song that broke the record for popularity at Nico-Nico."
    "Or at least in 2012, when the long-dead Tupac Shakur took the stage."
    "And then it caught on in Russia - Tsoi, Talkov...Vysotsky."
    "The technology became more and more advanced, the images became less and less distinguishable from reality - the same Vysotsky could no longer be distinguished from a live person, the show's creators even managed to make a kind of light and shade for greater authenticity."
    "But you can't do that. You can't let computer reality become more appealing than life!"
    "You can't let one day, under the hot southern sun, a flesh-and-blood creation of the mind - not real, made-up from the get-go - laugh a silver bell, and one unremarkable pioneer's heart fluttered, missing a beat."
    "We've got winter, we're importing from the perpetually playing with some obscure toys Asians their new Goddess - the eternally young, beautiful. The software one. The one you can buy every week on Friday nights for a three percent discount."
    "And to hold to your chest like the greatest treasure - because from the cover you can see the very eyes you remember from childhood, the same incomprehensible smile - the damn Asian facial expressions. But the sun hits your eyes, and the silhouette reaching out beckons and beckons."
    "She's dressed in a beautiful coat and looks like a real princess with lilies of the valley in her hands."
    "And we fly till morning, sitting on a cloud, eating watermelon and spitting seeds on the head of passersby."
    nvl clear
    scene
    $ renpy.show("cg d7_mi_epilogue_7dl", what = Desat("cg d7_mi_epilogue_7dl"))
    with diam
    pause(3)
    "And in the morning we'll break up. Because it's time for me to grow up. And for her... For her to sing. Because that's all she knows how to do."
    "And I know how to dream - and keep a place near me always, where a fragile girl of one and a half meters tall could easily fit. And even a heart-shaped balloon won't make me smile anymore - because I bought it myself. For..."
    "I don't even know who."
    "Probably for that self who sometimes, but less and less often every year, opens his eyes in me and looks at this world with childish, cruel curiosity."
    "But maybe for the last time..."
    "If I'm lucky."
    "I apologize and struggle to keep my balance, crammed into the corner between the seat and the subway car door. It's a little difficult for me to do that, because there's one short girl who has to fit between me and the wall, and I have to protect her from the crowds."
    "She's not there yet."
    "But it's for now! It's temporary, I swear!"
    "Some would call me crazy to always keep a piece of space around me, and they'd be wrong. I call it foresight."
    "It can't be that it was all for nothing, can it?"
    "There's no way an entire week - our week! - be for nothing. It doesn't happen that way, I don't believe it."
    "And if this world suddenly has such rules... Then I've got the wrong world."
    nvl clear
    scene
    $ renpy.show("cg d7_mi_epilogue_7dl", what = Desat1("cg d7_mi_epilogue_7dl"))
    pause(3)
    "It's been a very long, very silly winter, if I'm allowed to use such words."
    "My body is very crafty - it doesn't try to turn me off if it wants to sleep, my eyelids don't slip and I don't have a headache."
    "It's just that at some point my shoulders and back get really tired."
    "And the most proven way to let them rest is to lean against something solid, like stretching out in a string along the wall."
    "Or the back of a chair."
    "And exhale."
    "And take another breath... Where?"
    nvl clear
    pause(3)
    play sound_loop sfx_bus_interior_moving fadein 4
    scene bg intro_xx
    with fade
    stop ambience fadeout 2
    "Exactly."
    "In another reality, another world, another time - another everything."
    "I was myself again, my things fit me again, and the change scattered in my pockets remained there, leaving me alone with the realization of one immutable fact."
    "I dreamed it all. Absolutely everything."
    "The kind of dream that makes you sick for months afterwards and hide your eyes wet from those around you, surviving the emotional intoxication with courage and fortitude - alone and on your feet."
    "For it is too personal, too genuine."
    "I dreamt of Miku. A singer I somehow never had a crush on."
    "And assuming that every dream is a whim of the subconscious, what was it trying to achieve?"
    th "Answer me, you bastard. Answer me, I'm sick of your silence!"
    "No answer."
    "My long, stupid winter of emptiness and loneliness."
    "Naked with the glow-in-the-dark eye of the monitor, looking at how a mentally healthy person can be corrupted - just because he wasn't lucky enough to see an overly detailed dream about how great it would be."
    "If Miku were real."
    "You are now observing a cumulative, ordinary, unremarkable man. - Exhibit please don't touch with your hands - thrown around, defending something for no reason at all."
    "And God forbid you should try to feel sorry for him. Although, if you are not afraid of abstract hatred, you can try. He's harmless anyway."
    nvl clear
    pause(3)
    "I was blushing and bleating like a sheep, sitting at a desk set up with a 'T' as I was asked from the other side of the office:"
    voice "Tell me, Semyon, what is your purpose in obtaining a visa?"
    "And what is there to say? Am I going to hurt myself more?"
    "I'm going to be disappointed and lose what's left of my meaning in life?"
    "I'm going..."
    me "I need a tourist visa. I... I want to see the city."
    nvl clear
    pause(3)
    "So no wonder I had to go to the embassy twice."
    "And the second time was three times worse, three times more hopeless - so much so that even the valerian didn't help."
    "When I closed the door behind me after the interview, I leaned back against it and moved to the floor, for several minutes I just tried to come to my senses, to fight the uninvited shiver."
    "The beautiful passport insert was worth it, though."
    "All that was left to wait for was..."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_mi_dj_good_jap:
    play music music_7dl["reflection"] fadein 2
    scene bg ext_city_night_7dl with fade
    nvl clear
    pause(1)
    "What, by the way? Tell me!"
    "Barely cracking my eyes open, I clutched at my phone - it was still the same December 29, 2018, only half an hour since I'd rolled my eyelids shut."
    "Of course, I jumped out of the bus, shouted for a cab with the rest of the cash, and - allure three crosses - rushed home, looking for at least something..."
    "Something where there's a Miku."
    "And the query «three strokes-one squiggle» threw me, of course, to the Krypton website, their project, the same one that scared the hell out of me a couple of days ago - voice synthesizers that use a variety of «nyas» instead of notes."
    "Except that the always obedient and brisk computer was at times giving off an utterly ugly speed - but for someone who has encountered the Asian segment of the net, there was nothing surprising about that."
    "Miku has developed a huge fan base - ten million active only, about a hundred thousand actively writing, well over a dozen thousand songs written since 2007."
    "Famous producers, pop stars who were happy to use a virtual girl on a warm-up show."
    "There was a whole lot of money in it, but there wasn't my Miku."
    "Hope melted away day by day."
    nvl clear
    pause(3)
    "Yes, of course, I left my darling that artifact with the list of addresses and their timeline - so she must know for sure that I'm here in 2018 and not somewhere else."
    "Of course, in case she exists at all, my beloved."
    "I spent almost all my savings to buy tickets to Sapporo, the rest of it going to extra negotiations."
    "In order to talk to Fujita-sama, I had to borrow from relatives - they wouldn't ask questions, but..."
    "However, even the one who gave Miku her voice didn't know anything; she was paid for her work, like they usually pay her to voice another anime series, so..."
    "It's been a month, almost a landmark date, catching me as I tried to peel myself away from the door leading to the official deciding whether or not to allow me to..."
    "And what exactly to allow, he didn't know himself."
    "Just in case it turns out that... I have to see for myself, you know?"
    "I have to see for myself, I have to look into her eyes."
    "Leaving for another round of reincarnation is too responsible step to take without having gathered all the information that confirms - I was here by mistake."
    nvl clear
    pause(1)
    scene black with fade
    "So I have my orange stub, a passport with a silly sticker on the back page and an approved Japanese visa."
    "I'm flying nowhere, a one-way trip."
    "I want to see my Miku - but she's in no hurry at all to our northern heights, to please a sophisticated audience with her synthesized vocals."
    "So, as they say, if the mountain won't come to Mohammed..."
    "I just need to... Make sure? I guess so."
    "What is the purpose of your visit to Japan?"
    nvl clear
    "I'm your infector, trapped in a cloud somewhere in cyberspace."
    "I send you tears with dreams, love and life."
    "And you're human, you don't care about the moods of the crowd."
    "You just wander through life aimlessly searching for yourself!"
    voice "Oh... Miku-chan?"
    "She smiles understandingly."
    me "Yes, officer. I want to see your Miku."
    voice "Welcome to Sapporo!"
    "The officer cleared the way for me and, literally lingering for a split second, smiled:"
    voice "Good luck to you!"
    nvl clear
    play sound_loop sfx_street_traffic_outside fadein 2
    play ambience ambience_cold_wind_loop fadein 3
    play sound sfx_intro_bus_stop_steps
    "I suck at geography. I can't say I have topographical cretinism, but I screw up with transportation all the time."
    "This time, I got off the subway two stops before I was supposed to."
    "I used to do this all the time at home - I missed a stop, got lost in thought, got confused - and behold, a new job on my feet."
    "Even though I didn't like walking, the constant short-distance runs like that didn't add to my intelligence at all."
    "So it was now - I looked up in wonder at the building with its rounded canopy resting on four columns."
    "No."
    "Pulling my smartphone out of my pocket, I was once again convinced - wrong building! Shit."
    nvl clear
    pause(1.5)
    me "Excuse me, can you help me?"
    voice "Sorry, I don't speak English."
    me "Excuse me..."
    "Zero response."
    "I was jostling among the rushing back and forth of people in a foreign country with a foreign language, and I felt habitually like an idiot."
    me "I am not a tramp!"
    "I explained a few minutes later, waiting for my papers to be checked."
    me "Just got my address mixed up. Could you please help me?"
    "The policeman just didn't wag his finger on his temple."
    "His forehead had «bloody stupid gaijin» written on it in huge letters, but his duty as an officer of the law demanded it, and with a sigh he explained the way to me in broken English."
    voice "You must go down this street and at the first major intersection turn left."
    me "Major?"
    voice "Yes! There will be several small streets, mind you."
    nvl clear
    pause(3)
    "Ten minutes later, my feet led me to a beautiful building, a staircase stretching toward the whitish sky."
    "It was just like in the picture-green corrugated boarding, huge letters «ZP», and five lights shining out of the gloom on the square in front of the entrance."
    "There was already a whole crowd standing there - they didn't seem to be embarrassed by the sharply dropping temperature, the wind, or the unexpected snowfall here."
    "February 7, 2019."
    "There was an icy thorn in my chest."
    "Six o'clock in the evening - the check pass has already started, I'm very much on time."
    "The steamy red doors swung open and the crowd rushed in."
    "And I, like a latecomer, jostled in the back, trying to get in, ignoring the bewildered looks of those around me - it would have been rather amusing to feel like a stranger among my own if it had not been for the constant sensation of catching my breath."
    "At last it was my turn."
    "Well, at least no one here asked unnecessary questions - I handed in my chip ticket, it was read out and they let me in."
    "..."
    "And immediately to the left! To the trays selling glow sticks."
    "And then the checkroom, the bathroom, all that crap."
    stop ambience
    stop sound_loop
    nvl clear
    pause(3)
    scene cg d7_mi_dj_concert_7dl with dissolve
    "The gray floor in the hall is lint-covered, made of a special dirt-repellent compound, highly relevant in February, when it's a mess outside."
    "And, of course, no chairs."
    "Instead, rows of special handrails stretched out, keeping the crowd from bunching up into one big herd with its own center of gravity."
    "Little by little the lights in the hall began to go out, and..."
    stop music fadeout 10
    "I almost went deaf as those around me cheered with shouts and applause at the screen lighting up and..."
    "I would have sat there if I hadn't leaned on the handrail."
    "But..."
    nvl clear
    pause(3)
    "They promised an anime girl..."
    scene cg d7_mi_dj_concert2_7dl with dissolve
    "And on the stage, between the two screens, she appeared."
    "The one I remembered, the one falling asleep on my shoulder!"
    "In disbelief, I closed my eyes and shook my head."
    "And..."
    play music music_7dl["tellyourworld"] fadein 3
    "It didn't work."
    "It was her! My Miku!"
    me "Miku!"
    "I shouted as hard as I could, not sparing my ligaments."
    "But where was I to speak against the crowd."
    "Worse, at one point that scream was picked up by those standing nearby, spreading in a wave, echoing off the walls and back into my lungs."
    "The crowd began chanting the girl's name and completely drowned me out."
    "And rightly so. Where am I, silent alone with a monitor for half my life, to compete with the voice of society?"
    "So I quietly and peacefully shut up, shut down, and in my usual manner, reclaimed a small piece of space next to me."
    "Just enough to put Miku in."
    nvl clear
    pause(3)
    "The local crowd is more cultured than ours, no one puts anyone on their neck, no one jumps, so the reaction to my aggressive movements was bewildered, but calm."
    "And soon the warming up of the equipment was complete, and the familiar tune poured from the speakers - oh yes, I have not wasted any time in these two months, I have studied very, very many songs of my beloved virtual diva."
    "Even compiled my own top. But that song... She's been with me since late '11."
    "She's been..."
    "Before I knew it, I was disappearing into the crowd."
    "When the whole room is united by one emotion, one common vector, one common charge..."
    "Yes, all of us here loved that girl."
    "It's easy to talk condescendingly about the crowd when you're thinking against it... And, what's to say, anyone who's been to a concert of any reasonably popular band will understand me."
    "And I let myself turn off the ego, turn off everything that makes me me - the snobbery, the sense of my own chosenness, the sense of looking at the world in the first person."
    "We are all here to pay homage to our digital goddess by paying what makes the image enduring - our faith in it."
    "So when our eyes finally met, I just smiled and..."
    mi "Semyon?"
    "Asked the hologram."
    scene cg d7_mi_dj_concert_7dl with dissolve
    "The lights went out."
    nvl clear
    pause(3)
    stop music fadeout 0
    "The crowd hummed, left in complete darkness."
    "Fortunately, no one's sticks went out, and someone, apparently thinking it was part of the show, started shouting Miku's name."
    "Almost exactly like me at the beginning of the concert."
    "Name - wave of the wand - name - wave of the wand. Waving in the dark, glowing sea."
    play music ambience_7dl["concert"] fadein 6
    "Ten minutes of chanting before a semi-recognizable tune came out of the speakers."
    "It seems the organizers had some technical difficulties."
    "And someone in a security suit pushed his way over to me and politely touched my elbow."
    if herc:
        voice "Excuse me, are you Seuchiov-san?"
    else:
        voice "Excuse me, are you Persunov-san?"
    "He tried to be polite, but he had to do his best to shout down the crowd."
    me "What makes you think that?"
    "He looked around."
    voice "You are the only white gaikokujin here, sir. Follow me, please."
    me "But I have a concert here!"
    voice "We'll make it up to you."
    "The comrade in the suit was polite and adamant."
    "Intrigued, I followed him."
    nvl clear
    pause(3)
    play sound sfx_open_door_strong
    "The guard opened the door with an effort, held it open for me, and then slammed it shut."
    $ volume(0.3, "music")
    "Cutting off both the sound of the song and the crowd singing along."
    me "Will you tell me what this is about?"
    voice "Someone wants to see you... Well you'll figure it out soon."
    scene bg int_concert_room_7dl with fade
    play ambience ambience_music_club_day fadein 1
    pause(1)
    stop music
    $ volume(1.0, "music")
    voice "I brought him in. Just don't be long."
    "He whispered into the lapel of his jacket and disappeared out the door."
    th "And why was I brought here?"
    "I walked from wall to wall, scrutinizing my surroundings."
    "All sorts of thoughts ran through my head, from organ hunters to the most trivial robbery."
    "What can I do, though, I'm a pauper."
    "Coming from Russia to Sapporo for Miku's concert. Yeah."
    th "Well, or maybe I'll be recruited for the local yakuza!"
    th "Or military intelligence!"
    th "Well, or at least they found out about «Sovyonok» and decided..."
    "What they decided, I didn't have time to figure out."
    nvl clear
    $ set_mode_adv()
    play sound sfx_open_door_1
    "The door creaked open..."
    "And there was a girl on the doorstep."
    show mi shy voca with dissolve
    voice "Namiki, you have five minutes!"
    "Shouted from the hallway."
    me "What can I?"
    $ meet('mi','Namiki')
    mi "Um... Hi."
    me "Hi."
    "I answered politely."
    show mi upset voca with dspr
    mi "You don't recognize me at all?"
    "With each phrase, her voice grew quieter and quieter."
    mi "Senechka..."
    with fade2
    me "Miku?!"
    play music music_7dl["ourfirstmet"] fadein 6
    mi "Here my name is Namiki, Senya. That's the way it is."
    me "Namiki... Miku... You're really her, aren't you?"
    show mi shy voca with dspr
    mi "No, I am me. It's just that you called me by her name..."
    me "Then come and kiss me quickly, you monster!"
    "I demanded."
    "I was nearly knocked off my feet by a squealing and squeaking whirlwind with an aquamarine edge."
    show mi happy voca with dspr
    mi "Senechka..."
    "She kept repeating my name, kissing my eyelids, my cheeks, my temples, while I myself tried to blink less often to keep it from running down my cheeks."
    "After all, it was her!"
    "All mine, right down to the smells, the feel under my fingers."
    "My Miku."
    "It wasn't until a few minutes later, when the joy of mutual recognition had subsided a bit, that we finally allowed ourselves to ask the first substantive questions."
    me "Why Namiki?"
    show mi smile voca with dspr
    mi "Because Mom and Dad named me that, of course."
    me "So there was no engineer dad?"
    mi "Why, there was! Just our Japanese one."
    me "Uh... What was there on the stage?"
    show mi laugh voca with dspr
    mi "What-what. Cosplay!"
    me "So the real Hatsune Miku doesn't exist?"
    mi "Of course not! You're the one I dreamt about. Or you dreamt about me, or we both dreamt about us. Anyway, we're here, and now there's a program on stage, and I'm going to sing something else in a few minutes."
    me "And you became Miku in a dream? But how do you know Russian?"
    show mi laugh voca with dspr
    mi "Dummie!"
    "She habitually slapped my forehead."
    mi "Learned, how!"
    voice "Namiki, your way out!"
    mi "Coming!"
    "It's just like that time at camp - alive, real, Miku pulled me to her and gave me a tasteful, drawn-out kiss."
    mi "Wait for me after the concert, okay?"
    me "Deal."
    mi "Be sure to wait for me!"
    $ meet('mi','Miku')
    hide mi with dissolve
    scene anim prolog_2 with fade3
    "\[Good ending unlocked - «Be Sure to Wait For Me!»\]"
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("mi_dj_good_jap")
    show acm_logo_mi_dj_good with moveinright:
        pos (1600, 1020)
    pause(7.4)
    play music music_7dl["happy_ending"] fadein 5
    call alt_7dl_titles
    pause(1)
    return

label alt_day7_mi_dj_good_rf:
    nvl clear
    $ set_mode_adv()
    play music music_list["lightness_radio_bus"] fadein 7
    play sound_loop sfx_bus_interior_moving fadein 4
    scene bg intro_xx
    with fade
    stop ambience fadeout 2
    "Inhaling the warm air, a little stifled by the large number of people standing next to me at the same time."
    "And exhale - vapor, puffing, instantly gripping a homemade late 2018 logo on the glass, fogging and hiding something very important from me."
    "..."
    "Another dream, huh?"
    "The concert, «Zapp Sapporo»."
    "I pulled out my passport - no visa, of course."
    "The date on the clock is still December 29, 2018, no February was out of the question."
    th "And anyway, where did that strange date come from? {w}7-2-19? {w}2-7-19? I don't get it."
    with fade
    play sound sfx_intro_bus_stop_sigh
    if alt_day6_mi_dj_walkman:
        "And that tune is still playing in the cabin."
    else:
        "The earpiece was still dangling, and the same tune was still playing in the cabin."
    "The tune that started it all."
    "A beautiful, streamlined, green new LIAZ passing by caught my eye."
    "Adorned with all kinds of advertisements."
    play music sfx_7dl["raindrops_radio"] fadein 6
    "And - I couldn't believe my eyes!"
    "Amidst the appeals to buy happiness in yet another «Mega», a painfully familiar figure nestled there."
    "Familiar facial features, the outline of the figure. The familiar red hieroglyphs in a white outline - the same ones you can't confuse with anything, no matter how hard you try - three strokes, one swirl."
    "February 7, 2019, BKZ."
    th "What?! That can't be!"
    "Reflexes worked apart from my participation - the bus and the sign and the date were instantly in the frame."
    "I didn't realize myself at what point the tune changed to the one that Miku liked so much."
    "Everything was changing around."
    "I saw a movie once about how time will bear anything, but it's an elastic thing, and it can be a real pain in the ass."
    "I think it was called «A Sound of Thunder»."
    "And now I could almost see that very wave of recoil - the world was waking up, stretching and shaking off what had gone before, revealing changes to the eye!"
    stop music fadeout 3
    scene anim intro_2 with dissolve
    "Of course, these changes didn't happen overnight."
    "I just started noticing them."
    "At some point, I began to dream about Miku."
    "I'm sitting on the windowsill, watching the leisurely moving cork with my eyes, and an a cappella of early spring rain is pounding against the glass, and there's no way to see through the heavy sky, nor the sun."
    "But what is it? From the east, from where the sun greets at the earliest dawn, a fiery stroke carries an unidentified, highly seductive flying object."
    "And it never bothers me!"
    "After all, she's made up, she doesn't exist! She is brought to life by the power of imagination of the Krypton Media designers, animated by my unquenchable desire to meet someone like her."
    "Which means she belongs in dreams - and, of course, little things like flying just inevitably accompany her!"
    "Google spits out a few million responses on a query for her name, translators spit out a few million more - whoever PR'd this e-girl was extremely serious about it."
    "Well, I'm no stranger to asking - if you phrase the question right, of course."
    "And after weeks of searching..."
    "But never mind!"
    stop music fadeout 3
    stop sound_loop
    play sound sfx_intro_bus_door_open
    pause(3)
    play ambience ambience_cold_wind_loop fadein 3
    scene anim intro_1 with dissolve
    play music music_7dl["tellyourworld"] fadein 3
    "She hangs out in front of my window and waves from there, saying, hurry up, it's half an hour before dawn, don't slow down!"
    "I hesitate, I'm scared shitless, it's the seventh floor!"
    "I hesitate, I keep looking at her outstretched hand, at her smile."
    "And I yield - turning almost into a statue from fear of heights, and nevertheless, accept the outstretched hand."
    "We don't have much time as it is, and it takes me all the way across the continent every night to fly."
    "Balancing my weight, she strains a little, pulling me up, and the rain keeps coming and coming, and now wet shirt is clinging to her body, and my T-shirt drenched fully."
    "But she winks and, exhaling, soars under the grayest sky, to where my house is visible as a fuzzy rectangle."
    "I'm flying in my sleep - means I'm growing, right?"
    "It's a little late to think about growing up when you're well over 25..."
    "But Miku comes and comes to me, and then I wake up."
    "And with dry eyes I cry into the soulless ceiling, I shake my fist at the world through the dirty glass, and everything is still there."
    "Everything is as I used to be - gray, dirty, dusty and miserable."
    "Even though I used to think of my Urbana as beautiful, I never had much faith in what was hiding on the other side of the facade."
    "But little by little, change is making its way here."
    scene stars with fade
    "It was like someone wiping the dust off the stars with a giant rag - the sky hadn't stopped being black, but that black had become deep, intense."
    "The stars became not white holes, but prickly bright sparks."
    "The dust, dirt and dankness from the air didn't go anywhere - but now they felt clear, crisp, gray was gray, brown was brown, and the air was becoming impossibly delicious, fresh!"
    me "Random omnibus, what have we done to you, girl..."
    "I muttered to myself under my breath."
    "It's the world gone mad, isn't it?"
    "And it's been going crazy the whole time I've been watching it, filling up faster and faster with colors, smells, tastes!"
    if loki:
        "At some point it didn't matter to me that I was ruined by Xana, either."
        "And Xana herself didn't matter too, for that matter."
        "I didn't understand, I was genuinely puzzled - how, well, how could some obscure girl who wasn't even close to Miku manage to do this to me?"
        "No, of course I didn't hold a grudge against her - it was more than half your fault that you got swindled."
        "But the bus didn't make it to the subway, and the car I was supposed to be in didn't make it to Krestovsky."
        "Instead, I stepped out and breathed an unexpectedly clean, rich - city."
        "Frozen in anticipation."
        "For a moment we breathed in unison, and the realization that we were expecting the same miracle came spontaneously."
        "Miku."
    elif herc:
        "The words from her song went on and on in my head."
        "We'll meet, you just have to listen - no matter where or when. Just have faith."
        "So I dialed the seven digits that boded trouble for me, and..."
        "I had no right to risk it now."
        "Not when my perceptions were shaken off of bullshit and handed me a ticket to the intense world - the only one where a miracle is possible."
        "There's no such thing as miracles against a dusty backdrop, is there?"
    else:
        "I noticed a change in myself, too."
        "It was as if I was breathing more correctly, cleaner, more often, exhaling every time something unnecessary, breathing in something useful."
        "Becoming something better with every heartbeat."
        "And rightly so - because I should be at my peak the moment I meet Miku."
        "I didn't doubt the latter for some reason."
    play sound sfx_intro_bus_stop_steps
    "My new year was the best I've had in five years - it was full of anticipation."
    scene anim intro_2
    with fade
    play sound sfx_intro_bus_stop_steps
    pause(3)
    scene anim intro_3
    with fade
    pause(3)
    scene anim intro_4
    with fade
    pause(3)
    scene anim intro_5
    with fade
    pause(3)
    scene anim intro_6
    with fade
    pause(3)
    scene anim intro_8
    play sound sfx_intro_bus_stop_sigh
    with fade
    pause(3)
    stop ambience
    scene bg semen_room
    with fade3
    stop sound_loop
    "My companions for the first time in many years were again: optimism, faith and hope in a miracle, confidence in my own immortality."
    "And, of course, the immutable certainty that I am in this world for a reason!"
    scene bg int_sam_house_clean_7dl with pixellate
    "And so the first place I had to clean up was where I waited for my miracle."
    "You can't expect a miracle in a swamp, can you?"
    play sound sfx_open_water_sink
    play sound_loop sfx_water_sink_stream fadein 1
    "That's what I thought too."
    "I held my back, hid my smile, and waited patiently for God knows what."
    stop sound_loop
    play sound sfx_close_water_sink
    pause(1)
    "Week after week dripped by, but I was in no hurry."
    "In the end, my conscience was clear - I had wasted a lot of time, money, and opportunity on the search, and they all produced the same answer:"
    "Your virtual girl only exists as a hologram."
    "But..."
    "I developed the most vigorous activity - cleaning, sweeping, vacuuming, hauling trash to the dumpster - as it turned out, I had forty pizza boxes alone living in my apartment."
    "I had to keep myself busy."
    "The computer kept rustling the coolers melancholically - but all the places I went now remained unattended to."
    "All I was interested in was the touring schedule of a certain notorious singer, and the reasons why the Kryptonians had decided to suddenly take a severe detour like this and stop by both capitals of our homeland."
    "And the more I thought about it..."
    "The more I believed in the miracle!"
    if alt_day6_mi_dj_walkman:
        th "After all, my Walkman went somewhere!"
        th "It's unlikely it could have been stolen from my zippered pocket."
    if alt_day5_mi_dj_apology == 2:
        "The cut on my hand - I remember telling Miku to stop doing stupid things."
        "It was stupid and incorrect, I know. But it worked."
    if alt_day4_mi_dj_hedg:
        "Okay, no kidding!"
        "I understand, of course, all the wonderful coincidences and expansion of the universe and relic radiation."
        "But who can tell me what kind of relic radiation can explain the Japanese bracelet that materialized on my wrist?"
        "I don't even mind the chipped finger pads - I suspect fingerprinting me is useless right now, thanks to my friend «Sonic»."
        "But still!"
        "I twirled the bracelet thoughtfully on my hand."
        "If the virtual digital diva doesn't exist and the damn «SUS & Co.» agency didn't lie by giving me a verdict of her existence for a hell of a lot of money - solely in the form of a registered letter with just two lines inside: according to their investigation, this person never existed."
        "Then where did it come from?"
    th "And I did leave her an almost complete list of my movements."
    "Before 2005 - downtown, since 2005 - here. Parents, school, uni..."
    "Yeah, I should've taken her number and address, and now I had to take a passive role..."
    "But at least! If she really exists, she will have no difficulty in reading the last address and, when she arrives in the Northern Capital, take any cab, for a modest bribe and come to my side."
    "Just have to wait, right?"
    "It's past midnight on the clock."
    me "This is the end of February 6th. The final countdown."
    "Miku will be performing in our city tonight at the «Oktyabrsky» Concert Hall."
    "And I was very! I was very surprised when I found out that more than half of the seats were already sold out, that all the boxes were full, and the VIP seats were reserved."
    th "Maybe it's not a miracle at all, but some kind of commercial flair of their concert director?"
    scene bg semen_room_window
    with fade
    play sound_loop sfx_street_traffic_outside fadein 2
    "I pressed my hot forehead against the icy glass, studying my new Peter thoughtfully - bright, beautiful, eye-catching."
    "A beautiful toy. For a player who doesn't need it."
    me "And where do I find you..."
    "Whispered I to nowhere."
    stop music fadeout 3
    stop sound_loop
    play sound_loop sfx_7dl["ringtone"]
    pause(3)
    "The phone rang - unknown number."
    "It's been a long time since I bothered to remember numbers, though. Someone's MTS, from St. Petersburg..."
    th "Whoever you are, I won't answer you."
    "The phone kept making rattling noises."
    "I very rarely heard it if I was walking down the street with music in my ears."
    "I didn't get too many calls at all."
    "And now..."
    "Five calls is business etiquette, calling less is to show impatience, calling more is to show insistence."
    "Somebody didn't seem embarrassed by that prospect."
    "But the operator disconnects after the twentieth ring."
    stop sound_loop
    "Finally the phone went silent."
    scene bg int_sam_house_clean_7dl with dissolve
    "And I'm back behind the machinery - I think I have an idea."
    "But someone from above was clearly going to keep me from sitting at the monitor today."
    play sound sfx_door_bell
    "The doorbell rang..."
    me "You've got to be kidding me!"
    "I barked."
    "But there's nothing to do. {w}Should at least go and see who the hell it is."
    th "How about lurking - and whoever's out there will go away?"
    "And then with a sigh I lifted myself out of the chair - no, a new life must be new in all its nuances."
    scene black
    with fade3
    scene bg int_staircase_7dl with dissolve
    "As I tiptoed to the door, I looked out the peephole, and..."
    "There was no one in front of the door."
    play sound sfx_door_bell
    "But the bell kept ringing!"
    me "Who's pranking ther..."
    "I turned a little to the side, so I could see the space below the bell."
    "And there stood..."
    play music "<from 124.4>" + music_7dl["tellyourworld"]
    show mi sad voca with dissolve
    "She was quite visibly nervous, fidgeting with a sheet of paper, referring to it now and then."
    play sound sfx_door_bell
    th "It's her!"
    "There could be no doubt - I recognized both her and the sheet. No wonder, for it was I who wrote it."
    play sound sfx_open_door_strong
    show mi normal voca with dissolve
    mi "Hi, Se-"
    "Cheerfully she began."
    show mi surprise voca with dspr
    "And snapped."
    "I did look different after all."
    mi "Senya?"
    me "Miku..."
    "With lips alone, I said."
    "And I... I wanted to look. Now I would have, and..."
    show mi shy voca with dspr
    "And she kept twisting and twisting the ill-fated piece of paper in her hands, all scribbled in blue pen, and blushing more and more."
    me "Is that really you?"
    "And then she immediately stopped fidgeting."
    show mi smile voca with dspr
    "Smiled:"
    mi "Will you let the girl get warm?"
    "That gesture was all her. If there was any doubt before..."
    me "Yes, of course. Sorry."
    with fade
    "She looked older than I expected."
    "And much prettier."
    "I moved aside, letting her through."
    "Somehow all of a sudden I found slippers, helped her undress, and hung her coat on the hook in the hallway."
    mi "So you live here, then?"
    scene bg int_sam_house_clean_7dl
    show mi grin voca at zenterright
    with dissolve
    "Miku walked into the apartment, looking around curiously."
    mi "Well... At least you made an effort to clean up."
    "She was wearing that very dress..."
    show mi normal voca with dspr
    mi "You like it? There's a huge fashion for these in Japan right now."
    me "A lot."
    "I honestly admit it."
    show mi upset voca with dspr
    mi "You know... We had a window on the tour, so we thought we'd make a little detour, come and visit Russia."
    me "Oh, a little, yes."
    me "However, I know already, can't get tickets for you in Moscow or St. Petersburg anymore."
    show mi normal voca with dspr
    mi "Yes! So here I am."
    "Here. I was more than happy."
    "If it weren't for one thing that's been bugging me."
    me "But we're here... And you... I saw an ad on the bus."
    show mi happy voca with dspr
    mi "Don't be afraid to scare me with that scary word!"
    "She winked."
    mi "Do you want to say it out loud? Vo-ka-lo-id! {w}I'm part of the project, remember?"
    mi "It's just that sometimes there are live performers on stage along with the virtual diva."
    show mi normal voca with dspr
    mi "But I don't have much time, Sen, to be honest."
    mi "I just stopped by to say hello and ask you something."
    "I wanted to ask you, is that all?"
    me "Ask?"
    "But instead I just took her hand."
    "Miku is alive, real, warm. She's here, she's near!"
    mi "Yes. The first question is, by any chance, are you planning to do anything soon?"
    me "No, nothing, why?"
    show mi serious voca with dspr
    mi "Then question number two."
    show mi shy voca close with dissolve
    "Miku came close to me, looked me in the eyes with a challenge."
    mi "You haven't changed your mind? About your commitment."
    "And she still dares to ask? I've been... Two months..."
    with flash
    me "Of course not!"
    show mi smile voca with dissolve
    mi "Fine! Then get ready. Let's go."
    me "Where to?"
    mi "I have a concert in half an hour, and someone promised to wait for me backstage."
    mi "I can't wait for this moment!"
    me "Miku..."
    mi "Yes, Senya."
    me "I can't believe you're real. Are you sure you won't disappear?"
    show mi normal voca with dspr
    mi "Don't even dream of it!"
    stop ambience
    scene anim prolog_2 with fade3
    "\[Good RF ending unlocked - «Don't Even Dream of It»\]"
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("mi_dj_good_rf")
    show acm_logo_mi_dj_good_rf with moveinright:
        pos (1600, 1020)
    pause(7.4)
    call alt_7dl_titles
    pause(2)
    return
