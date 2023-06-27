label alt_day4_me_neu_dv:
    if (alt_day3_dancing2 == 'dv_2'):
        show dv normal pioneer2 with dspr
        "However, with my karma, it was no surprise that Dvachevskaya, collapsed in a deckchair."
    else:
        play music music_7dl["beth"] fadein 5
        scene bg int_extra_house_7dl with dissolve
        play ambience ambience_int_cabin_evening fadein 2
        "I woke up on a bare mattress, with a pillow under my head."
        th "Strange, could it be that I did that in my sleep? I have to get up immediately and get everything in order, or Olga Dmitrievna..."
        "I glanced at the bed next to me."
        "And sat down."
        "There was a roll composed of mattress, blanket and a pillow lying on a neighbouring bed. The squad leader's personal belongings were nowhere to be seen.{w} Neither were mine."
        "Fortunately, my memory woke up in time and I didn't have time to panic."
        th "So... I ceded my place to DvaChe yesterday, and slept in an empty cabin myself."
        th "And I think I even asked her to be my «lady of the heart»."
        "Now, after the fact, I was creeped out by the silliness of that conversation."
        "And the feeling that she hadn't said «yes» didn't let me go."
        "Okay, time to get up."
        "At a brisk pace, I pushed the door open."
        stop ambience fadeout 2
        play sound sfx_open_door_1
        $ alt_pause(1)
        scene bg ext_houses_day with dissolve
        "And went outside."
        show dv normal pioneer2 with dspr
    me "H-hello."
    "Try to pretend that I didn't notice her was stupid."
    "It remains to pretend that nothing happened yesterday."
    dv "We need to talk. {w}On the subject of yesterday."
    me "Yeah? Well, let's... Let's talk."
    show dv grin pioneer2 with dspr
    dv "Not here."
    "She beckoned me after her."
    me "Where to?"
    "I realized."
    dv "Well... We'll sit in my place, play guitar..."
    me "But I..."
    dv "I know. That's why I'm taking you as an apprentice."
    "She disappeared between the bushes, and I had no choice but to follow her."
    $ alt_day4_me_neu_date = 'dv'
    scene bg ext_path_day
    with blinds_l
    "After wandering through some obscure paths, we found ourselves on a small patch of trampled grass, surrounded by dense thickets."
    "Alisa instantly occupied the only log lying there, giving me the dubious honor of seeking for a place to sit on the grass."
    "Sighing, for lack of alternatives, I accepted her generous offer."
    "And then, just when I was about to sit down..."
    dv "Wait."
    show dv normal pioneer2 at center with dissolve
    "I stared at her."
    "Alisa rose easily from her seat - I looked away tactfully - and, apparently realizing the reasons for my embarrassment, smiled:"
    show dv smile pioneer2 with dspr
    dv "Since I am your sensei, you must do as I say."
    me "Sensei... Where did you learn such words?"
    show dv grin pioneer2 with dspr
    dv "I've been talking to Miku for two weeks you know."
    "The redhead smiled dazzlingly."
    show dv normal pioneer2 with dspr
    dv "So, apprentice, listen to my will."
    "Alisa studied me for a second, as if trying to make sure I was submissive, and then she nodded contentedly."
    me "So what do you want...{w} Sensei?"
    dv "You know what! If you want to learn to play the guitar, you need a guitar first."
    me "What do you mean?"
    dv "There's a guitar at my cabin. {w} I want you to..."
    "I see."
    me "Alisa, tell me...{w} Except that your cabin is one hundred percent closed..."
    show dv smile pioneer2 with dspr
    dv "Here you go!"
    "Alisa pulled out a flat key from her breast-pocket and tossed it to me."
    "I have to be glad that my usual crookedness cheated me this time, and I caught the metal cone."
    "The key still held the heat of her body, and I hovered for a second, figuring out what it was touching."
    dv "So stomp into the cabin, on the right hand is Ulyana's locker, the guitar is there."
    me "Not on the left?"
    show dv grin pioneer2 at center
    with dspr
    dv "If you're interested in the color and texture of my panties, you can go left."
    "She winked and wiggled her chin."
    th "And why can't I get rid of the idea that I was suggested to stick my head in the lion's mouth?"
    me "As you command, Master..."
    "I mumbled to myself under my breath."
    "My relationship with Alisa oscillated between the utterly utilitarian - on both sides - and a kind of romanticism that only manifested itself when we were alone."
    show dv smile pioneer2 with dspr
    dv "So I command. Go."
    me "So, if anything happens, I tell that you sent me?"
    "I moved sideways - just in case."
    dv "Wait! Let's go together! Just in case you decide to steal something else."
    stop ambience fadeout 2
    me "Last phrase was Unnecessary. {w}Okay..."
    scene bg ext_house_of_dv_day
    with dissolve
    $ alt_day2_dv_us_house_visited = True
    play ambience ambience_camp_center_day fadein 3
    show dv normal pioneer2 at center with dissolve
    "After circling around the cabin, we walked out to the porch."
    "A ray of sunlight somehow reflected off the glass in a peculiar way, forcing the skull on the flag to wink cheerfully at me."
    if not (alt_day2_dv_us_house_visited or alt_day2_us_escape):
        dv "Have you visited me and Ulyana yet?"
        me "Do you and Ulyana live together?"
        "Somehow it seemed logical to me to put the two biggest troubles together."
    stop ambience fadeout 2
    play sound sfx_open_dooor_campus_2
    $ alt_pause(1)
    scene bg int_house_of_dv_day with dissolve
    play ambience ambience_int_cabin_day fadein 2
    show dv normal pioneer2 at center with dissolve
    "Alisa nodded and beckoned me after her."
    "Compared to the nightmare inside, the squad leader's cabin was a model of order, it was cleaned at least sometimes."
    th "And now she's going to throw me on the bed, and..."
    "I mean, what else is there to do in the cabin while the whole camp has magically turned out to be eerily busy?"
    th "Of course, it's a little faster than I thought, but, «music bound us together»."
    "Alisa froze in the middle of the room, pondering intensely about something."
    "I cleared my throat."
    show dv surprise pioneer2 with dspr
    dv "What?"
    "She visibly flinched."
    show dv smile pioneer2 with dspr
    dv "Oh, listen...{w} I've got something...{w} Wait here!"
    hide dv with easeoutleft
    play sound sfx_close_door_campus_1
    "Without listening to my objections, she ran outside and slammed the door behind her."
    th "Did she run for product number two?"
    if alt_day_binder != 1:
        "I knew the fact that there's a Postinor or its analogues for emergency contraceptive in any camp's emergency medicine cabinet."
        "But are there any of «girls' best friends» here?"
    th "I wonder why I thought this was about sex in the first place?"
    "Hmm... Probably because a seventeen-year-old body thinks about it all the time."
    "Sexual energy is produced all the time, some periodically grounded, some preferring sublimation in the form of activity - thoughts on the subject haunt everyone's mind at that age."
    "And extremely often they overwhelm the feeble voice of reason."
    stop ambience fadeout 2
    play music music_list["always_ready"] fadein 1
    dreamgirl "Something is wrong!"
    th "What?"
    dreamgirl "Lift your brain from your balls area and turn on the process you dumbass."
    th "What process?"
    dreamgirl "Alisa needed something in cabin, then she abruptly changed her mind and ran off somewhere."
    dreamgirl "And locked you inside in the process."
    th "Locked?!"
    "I tried to open the door. {w}With the expected result."
    play sound sfx_campus_door_rattle
    "Locked!"
    dreamgirl "If you had worked at least a little harder to look around you, instead of acting like a pubescent teenager, this wouldn't be a revelation to you."
    th "So she locked me up.{w} I don't like where this is going..."
    "Pulling back a curtain's corner, I looked outside."
    "Squad leader, led by Alisa, was approaching rapidly to my location."
    "A trap!"
    if (alt_day3_dancing2 == 'dv_2'):
        th "And how could I have thought she wouldn't get even with me for yesterday?"
        th "Oh, you fool..."
    if loki:
        th "It's definitely love."
        "I grinned."
        "Actually, the fact that no one had tried to ride my hump so far was starting to scare me."
        "And a huge thank to Alisa for giving me back my lost sanity."
        "I should thank her properly now, but how?"
        "Green-bound notebook was peeking under the pillow."
        "When I opened it, I immediately caught sight of a structure peculiar only to..."
        th "Bingo! Dvachevskaya's diary!"
        "When I opened the diary to the last page, I read:"
        th "June 21, 1989, the newcomer turned out to be not as wimpy as I thought. Although he's still needs to be tested and tested, and he is already looking over that crazy. Uh, they're all the same."
        "Flipping back, I noted a few of the terrorist attacks performed by Alisa and Ulyana, ponderings and other things that girls like that usually write in their diaries."
        "That's a lot of dirt!"
        "I opened the notebook at the description of how someone threw a snake into the girls' locker room, and left it in the most conspicuous place."
        play sound sfx_open_window
        "Then, opening the latchbolts in the window, I got outside."
    elif herc:
        me "Oooh, you bastard."
        "Am I have a face of a country simpleton, or else why is everyone around me always trying to scam me, or take advantage of me in some other way?"
        th "So you're setting me up, huh?!"
        "I grabbed a rubber ball lying nearby and started walking around the cabin, coming up with an adequate explanation for the squad leader."
        "The countdown was ticking in my ears, and, as luck would have it, no bright ideas came to mind."
        "Anger at Alisa came over me with renewed vigor."
        "I threw the ball against the wall."
        play sound sfx_7dl["window_glass_break"]
        with hpunch
        extend ", and was horrified to see it fly through the window."
        th "Damn, now I'll have to take responsibility for damaging government property too!"
        th "Time to get out!"
        "I threw glass shards off the window, opened it with a sharp movement, and was gone."
    else:
        "I wanted to do something nasty in revenge, but, as luck would have it, nothing clever came into my head except the most trivial of escapes."
        "I fiddled with the latches for a while and got out."
        "I had to bang the window from outside to get it to fall into place - I hope no one heard me."
        "At least all traces of my stay in the cabin were well camouflaged."
        play sound sfx_open_window
    scene bg ext_house_of_dv_day
    with dissolve
    th "I wonder if it even occurs to her that she has done a mean thing?"
    if (alt_day3_dancing2 != 'dv_2'):
        "Not that I doubted her outstanding mental faculties."
        "They most certainly were non-existent."
        "But you've got to know what you should do and what you should avoid."
        "For example, consider those who are able to understand everything and hitting back."
    else:
        "Of course I was guilty to a certain extent, but not to that extent!"
        "There's no way I deserved such a humiliating punishment."
        th "So, redhead, you're gonna get what you deserve!"
    with fade
    "I missed the squad leader by just a few minutes."
    "If she'd caught me inside - even if I was locked up... I mean, even more so if I was locked up."
    show dv normal pioneer far at cleft
    show mt normal panama pioneer far at cright
    with dissolve
    dv "There, look! I got him and locked him up."
    with fade
    show dv grin pioneer far with dspr
    "As she swung the door open, she cheered:"
    dv "See?"
    mt "See what?"
    if loki:
        mt "Some notebook?"
        show dv scared pioneer far with dspr
        dv "What? No! No, no, no..."
        hide mt with ease
        "But the squad leader had already got inside and was back on the porch a few seconds later."
        show mt normal panama pioneer far at easeinleft
        mt "Fourteenth of July, thrown a snake to the girls' locker room. What a squeal there was!"
        mt "Fourteenth of July, evening, they wanted to turn on an idiotic movie, but a fork in the socket fixed it."
        show mt smile panama pioneer far with dspr
        mt "Wow, and I was told the wiring was leaking. {w}What a useful notebook."
    elif herc:
        show mt angry pioneer far with dspr
        mt "Broken window? I see, Alisa."
    else:
        hide mt with easeoutleft
        "The squad leader sneaked into the cabin and came back a few seconds later."
        show mt angry panama pioneer far with dissolve
        mt "There's nobody inside. What's that supposed to mean?"
    scene cg d4_dv_mt
    with dissolve
    if loki:
        "It seems that it was a critical hit - Dvachevskaya blushed, stared at the floor, and in a trembling voice asked:"
        dv "Give it back."
        mt "No way, honey."
        "Smiled Olga Dmitrievna."
        th "Brr, what a flesh-eating grin!"
        dv "Give it back...{w} Please. It's personal..."
        mt "Personal? Really?"
        mt "So leaving the camp without lights is personal? {w}No, it isn't. {w}I'll read everything and you'll get for everything."
        dv "No!"
        "Alisa tried to snatch the notebook from the squad leader, but she was on guard and put the trophy behind her back."
        mt "Get ready for trouble."
        "In an icy voice the squad leader said."
        "She already forgot that Alisa chased her across the camp for no reason."
        mt "For every one of your shenanigans."
    elif herc:
        "Alisa made a face like she was going to cry right now."
        "I can understand - such a setup was ruined. And by who? The main victim!"
        mt "Long story short, that's it, Dvachevskaya!"
        "Olga seems to be very angry."
        th "Now that anger could come down on my head. {w}Maybe with consequences..."
        dv "But...{w} I..."
        mt "You go now and look for Slavya, she'll direct you to our supervisor, tell him what to do."
        mt "More precisely, you'll politely ask him to fix what you broke."
        dv "But I didn't break anything!"
        mt "Yeah, and the window broke by itself."
        mt "I'll be sure to put that on your evaluation, too. You did it once, you can do it again."
        mt "Go! First you fix the window, then we'll think how to punish you."
        "Alisa seemed to start getting the spice of the situation."
        "And what my reverse card would do to her."
        th "The funny thing is that it didn't even occur to the squad leader that, maybe, Alisa wasn't lying."
        th "What an evil thing reputation is, after all."
    else:
        dv "No, I swear he was here, and I locked him up."
        "Alisa looked at the floor with the desperation of a doomed man and continued to argue."
        mt "Yeah. He was. You never told me what he might have been doing there?"
        "Olga was already sneering unabashedly."
        dv "He was stealing something, I told you."
        th "That's right. He was stealing your stale panties, that's for sure."
        dv "And I locked him up."
        mt "Why don't we go see what he stole, then? Before he fell through the floor?"
        dv "No!"
        dv "My place is filthy."
        mt "But we have to make sure he really was there! Let's go!"
        "Something seems to have been left in the cabin. {w}Something, what Alisa really didn't want the squad leader to find."
        "She blushed, then turned pale, looking at the ground, and said quietly:"
        dv "No."
        mt "No what?"
        dv "He wasn't there. I made it up."
        mt "Okay, I'm not going to ask you why you needed it, but one more time like that and you'll get a duty assignment. Do you understand me?"
        "Alisa nodded."
    scene bg ext_house_of_dv_day
    with dissolve
    show dv rage pioneer far at center with dissolve
    "Considering her duty here done, Olga left in the direction of the beach."
    "And Alisa remained."
    "A pity, of course. She seemed like a normal girl to me, but after a joint like that..."
    "After seeing the squad leader off, I stepped out of my hiding place."
    me "So that's the kind of thing you do? Lock someone in the cabin and set them up for good?"
    show dv surprise pioneer with dissolve
    "Alisa got beast-mad at me."
    if loki:
        show dv rage pioneer with dspr
        dv "You set me up!"
        "I shrugged it off."
        me "You wanted to do the same thing."
        dv "You would have been scolded, that's all! {w}And I now..."
        show dv smile pioneer with dspr
        "She thought for a while and glowered:"
        dv "Here! I've got it!"
        "She poked me in the chest with her finger:"
        dv "If it's your fault, it's your duty to fix it."
        "I didn't think it was my fault, but I was curious to follow her train of thought."
        dv "Since you're living with the squad leader anyway, steal the diary from her and give it to me."
        me "You still haven't told me why I'm going to do it."
        "I prolonged."
        show dv grin pioneer with dspr
        dv "Because you owe me one!"
        "Okay, it was all clear here. {w}The patient was hopeless, and the doctor said to go to the morgue."
        me "Forget it. {w}And stay away from me."
        show dv surprise pioneer with dspr
        dv "What?"
        me "What you heard. You know, I almost believed you."
        me "And today it turned out to be for nothing."
        me "But I have to admit, it looked very natural."
        "I tilted my head to the right and smiled with one lip."
        me "Bravo."
        "I turned and walked away, leaving a blushing Alisa behind me."
    elif herc:
        show dv angry pioneer with dspr
        dv "You bastard! {w}Because of you..."
        me "No, because of yourself.{w} Go fix that window now.{w} And you know what..."
        "Now I was closer than ever to hitting a woman for the first time in my life."
        show dv scared pioneer with dspr
        "And I think that intention was clear enough in my eyes - Alisa recoiled."
        me "I get turned out by people like you. That kind of thing."
        dv "What do you mean?"
        me "Think about it. {w} Think back."
        me "And stay away from me."
        "Lowering my voice, I hissed."
        me "Forever."
        "Bitch."
    else:
        show dv rage pioneer with dspr
        dv "You bastard!"
        stop music fadeout 3
        me "Bastard?!"
        th "So the fact that I didn't let myself be set-up makes me a bastard? {w}That logic..."
        play ambience ambience_camp_center_day fadein 3
        show dv smile pioneer with dspr
        "Alisa smile suddenly."
        if (alt_day3_dancing2 == 'dv_2'):
            dv "I got kicked out of the disco yesterday because of you, remember?"
            me "I remember perfectly. But somehow, it doesn't seem to me that I deserved a set-up, for which I can get registered as a sex offender!"
        else:
            dv "Did you bet with me?"
            me "bet?"
            dv "Cards."
            me "Ah... well, yes."
            if (alt_day2_gamblers_result['me'] < alt_day2_gamblers_result['dv']):
                dv "Bet, means accepted the terms."
                dv "You lost, and I told the squad leader how you harassed me in the cabin, and I locked you and ran away."
                show dv angry pioneer with dspr
                dv "You ruined everything!"
            else:
                show dv grin pioneer with dspr
                "She smirked."
                me "But I won!"
                dv "So what?"
                th "Oh, that's feminine spontaneity."
                dv "Like it was hard for you."
        me "Maybe I should also apologize now for the failed villainy?"
        "I politely asked. {w}You never know, we haven't reached the bottom of her stupidity yet."
        show dv sad pioneer with dspr
        dv "Screw you."
        hide dv with moveoutleft
        play sound sfx_slam_door_campus
        with hpunch
        "She slammed the door."
        "I had a few curses on my tongue, but I didn't yell anything after her."
        "I didn't want to talk to Dvachevskaya again at all. {w} Never."
        th "But I almost believed her..."
    play sound sfx_7dl["eat_horn"] fadein 1
    "A horn sounded just in time over the camp."
    "Since it's not worked off with music lessons, I'll have to look for other entertainment."
    "But it's better to do it with a full stomach."
    "I hurried to the canteen."
    stop music fadeout 3
    stop sound fadeout 3
    stop ambience fadeout 6
    return

label alt_day4_me_neu_aid:
    scene bg int_aidpost_day with dissolve
    play ambience ambience_medstation_inside_day fadein 3
    play music music_7dl["afraid_of_destiny"] fadein 3
    "For some reason I woke up not in my bed."
    th "Hey, this isn't even my cabin!"
    "Judging by the way the covering of my bed was sticking to my bare back, I was on something covered in leatherette."
    "After reconnaissance again, I was convinced that my first assumption was correct - I was at the infirmary."
    th "But what am I doing here?"
    "I scrolled through the events of last night.{w} And nothing from last night was associated with the kind of thing you wake up in the infirmary after."
    "Unless..."
    "The receding edge of the roof, the antenna, the slippery underfoot...{w} Fingers involuntarily reaching for the back of my head came across a thick layer of bandages and yanked away."
    th "Looks like I'm out of there after all. No wonder the cyberneticists refused to climb up!"
    th "Well. Since I'm all wounded, I'm entitled to rest, care and attention."
    th "And, of course, lots and lots of sleep!"
    show blink
    "On that optimistic note, I closed my eyes."
    scene black
    "For some reason I was not at all afraid of the possible consequences of hitting my head - something told me that if my arms and legs were moving, if I can get up, even at the cost of dizziness, I would be all right."
    "Seventeen-year-old body thinks it's semi-immortal for good reason, I'll get over it."
    if alt_day3_duty:
        "Although they tried their best to get me yesterday, dragging me on duty."
    elif (alt_day3_dj == 'mi') and (alt_day3_technoquest1 >= 1):
        "The speakers coughed, and a familiar voice echoed throughout the camp:"
        dy "Good morning, «Sovyonok» and its owlets. Moscow time is ten o'clock, the temperature is thirty degrees, swimming season is open!"
        dy "I want to say thank you to our pioneers - Semyon in particular, he's lying in the infirmary right now, so be sure to pay him a visit, friends and acquaintances - for this broadcast."
        "Miku saddled her horse - she probably didn't even know the difference, so she just kept gibbering and gibbering."
        "Man of the stage - if she felt like it, she'd probably sing for the whole camp."
        th "Can't say I mind it."
        if alt_day3_dancing1 == 'mi_1':
            "Thinking back on our dance, oh yeah, I was pretty damn okay with that."
    elif counter_un_7dl >= 3:
        "I can't be accused of lack of effort."
        "I saved the princess, fought the dragon... But the epilogue was... a little expected."
        "I must have written on my forehead... {w}«Friendship Only, no sillines allowed»."
        "Or maybe the point is, she didn't like me to begin with."
        "Unfortunately, it happens more often than I'd like, because I'm no Apollo, and I don't look like Paris, I've always consoled myself by saying that a man only needs to be slightly more handsome than a Pithecanthrope."
        "But compared to that same curly, pretty face of Electronic, it's easy to see why the local beauties turn their noses up at me."
    elif counter_mi_7dl == 2:
        "I was dreaming about a Japanese pop star. A little bit unrealistic, but what else could a popstar be, with her unearthly beauty?"
        "Even if you know  that half of the effect is due to makeup and stylists, and the other half to lighting and costume, it still gets you to the core when the gaze of her bottomless eyes is focused on you."
        "I dreamed of her bouncing across the stage and singing something, waiting for me to push myself closer to the stage, let the security guard recognize me, and climb up onto the stage beside her, squinting under the Jupiter light, nodding in response to her confession."
        "And I can't move - I'm bogged down in the crowd, bogged down in the floor, and, worst of all, I'm painfully reluctant to change anything in my life, for in my gut I know how catastrophic the extent of change would be if I only let Miku into my heart."
        "But she did pick out a nice suit for me yesterday. It's a pleasure to wear it."
        "It's a pity, I've made a mess of it. She probably won't trust me anything at all now."
    if (alt_day2_convoy == 'sl') and (not alt_day3_duty):
        "Maybe it's for the best that I fell."
        "After all, its time to stop the vicious practice of dragging a certain Semyon to the flag under the attention of the entire camp."
    if (alt_day3_date == 'sl'):
        "On the other hand, in my current state I wouldn't be able to play Stirlitz anymore, and possible conversations about myself would no longer be able to reach my eavesdropping ears."
        "Though I'm probably flattering myself-who needs to talk about me, except for the exchange of general information."
    play sound sfx_open_dooor_campus_1
    "I was pulled out of semi-consciousness by the distinct click of the door lock."
    cs "How is he?"
    "I could be drunk, sick or half asleep - but I already got the hang of recognizing this voice out of a thousand."
    "Our kindest doctor, master of embarrassing sciences."
    if counter_un_7dl >= 4:
        un "Tossing and turning, seems to be waking up."
        "The second voice belonged to a younger person, judging by the notes of uncertainty."
        un "Will he be all right?"
        "And I recognized it too - unmistakably."
        "After all, I was talking to it's owner almost all day yesterday."
        cs "He didn't hurt anything vital - flew down the wrong side."
        "The doctor chuckled."
        cs "Will you return the shirt to the pioneer?"
        un "Yes, but it's a little damp from the wash."
        th "What a delight - they sit with me, they wash me... What's next? Will they rake the s..."
        "I couldn't stand this thought and grinned."
        un "Syom... Eh... I think I'll go!"
        "The girl squeaked and darted away in the blink of an eye."
        "Heels tapped on the floor."
        play sound sfx_open_door_1
        stop music fadeout 6
        $ alt_pause(1)
        cs "Was it worth it to grin so obscenely...pioneer?"
    me "Good morning to you too."
    cs "Will you get up? Or..."
    "I hummed something in the affirmative."
    cs "Get up then, let's have breakfast."
    me "Get up?"
    play music music_list["everyday_theme"] fadein 5
    scene bg int_aidpost_day with flash
    cs "Here."
    "She tossed shirt and shorts over the folding screen."
    me "Thank you."
    if counter_un_7dl >= 4:
        "As Lena said, the shirt was just a little damp - cool in the morning heat. The shorts were also thoroughly cleaned and darned in... ahem... the most interesting place."
    "Trying not to think about the fact that someone hadn't bathed for decades and the most French scents came from clothes before they were brought into a divine form, I pulled on a uniform."
    show cs normal at center with dissolve
    "And revealed myself to the nurse."
    show cs smile with dspr
    cs "Well… Good morning. {i}Shall I inspect you{/i}?"
    "The nurse, again, managed to put a whole galaxy of meanings into the word «Inspect» - or maybe the point is {i}how{/i} she pronounced it - slightly stretching out vowels, arching her eyebrow."
    "One day I'll be immune to Viola's charm... Until then, I'll just trudge along."
    me "Don't you already..."
    "She smiled:"
    cs "You know... pioneer. Checkups are never too much."
    me "You're probably right."
    "I answered cautiously, not knowing what else to expect."
    "Viola seemed to revel in her own role."
    cs "Especially since I only looked at... not the most important parts."
    me "So?"
    cs "Well... head and..."
    show cs normal with dspr
    "She thought for a bit."
    cs "That's all."
    "Viola extended her index finger and bit her fingernail thoughtfully."
    cs "But what if you also have other... umm... organs damaged? Take off your clothes."
    with flash2_red
    show cs smile with dspr
    "I blushed, and a chuckle flew up to the ceiling like velvety lightning."
    cs "Just kidding... pioneer. Get your breakfast."
    "She nodded at the dinner pails still standing forlornly on the table by the door."
    cs "Bon appetit. It's airing until half past eleven, so get yourself away from the window."
    cs "And I'm - outside... pioneer."
    hide cs with fade2
    stop music fadeout 6
    return

label alt_day4_me_neu_aid_un:
    $ alt_day4_me_neu_date = 'un'
    scene bg int_aidpost_day with dissolve
    play sound sfx_open_door_1
    $ alt_pause(1)
    play music music_7dl["seven_summer_days"] fadein 3
    "No sooner had the door closed behind Viola than someone was on the doorstep again."
    th "I just laid down!"
    "I had to make an effort over myself and get up when an imperturbable voice called out:"
    voice "S-Semyon?"
    th "I certainly seem to be popular today."
    "Unfunny I joked, emitting an affirmative grin."
    "I'm alive, I'm well, I'm an eagle."
    "Coming down now, just let me deal with the dizziness."
    "I pushed the screen aside, outwardly showing no sign of weakness."
    show un shy pioneer with dissolve
    un "Y-you... I'm sorry to b-bother you, but..."
    "Stammering, the girl began."
    "Though it seemed, after yesterday's revelations, the road was straight, if not to the registry office, then somewhere in that direction."
    "What's embarrassing now?"
    me "You're certainly not bothering me."
    "I didn't expect her to be so frank. That's probably why I reacted so stupidly."
    "Didn't react at all, to be exact."
    show un normal pioneer with dspr
    "What could be easier - a girl you like asks you for help - so help her, for God's sake!"
    "Reach out your hand and smile, and she will respond to your smile, not out of sympathy, but out of simple human concern..."
    "And the world will be a little brighter."
    "Not my case."
    show un sad pioneer with dspr
    un "I... I'm g-g-going to leave!"
    me "What? But why?"
    un "I've... I've fixed your shirt for you."
    "She was silent, looking me in the eye. Silent too."
    me "What?"
    "Finally, I got tired of the silence and raised my voice."
    show un shy pioneer with dspr
    un "I... I was just thinking, well..."
    me "About what?"
    un "What, well... If you'd agreed to help yesterday..."
    "Her voice dropped to a whisper."
    un "You could have been safe and sound."
    un "Wouldn't have helped, but and... I'm being so silly. I'm going."
    me "Yes. See you soon."
    hide un with dissolve
    "She left."
    return

label alt_day4_me_neu_aid_sl:
    $ alt_day4_me_neu_date = 'sl'
    scene bg int_aidpost_day with dissolve
    me "Wouldn't I be in one piece?"
    dreamgirl "Wouldn't have to live and breathe... Where did that come from..."
    th "Calm down, Robertovich!"
    "Grunting, I scraped myself off the bunk and made my way outside."
    play sound sfx_open_dooor_campus_1
    $ alt_pause(1)
    scene bg ext_aidpost_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    "The day was in full swing."
    me "How long did I sleep...?"
    sl "Fourteen hours."
    show sl smile pioneer with dissolve
    "Slavya crept up in her favorite style - silently from behind."
    me "I'm strong asleep..."
    me "Are you here to see me?"
    sl "Yes, hello! Olga Dmitrievna asked me to give you a present."
    "Taking a kind of cloth out of her pocket, she straightened it out and put it on my head."
    me "Panama cloth? What do I need it for?"
    show sl laugh pioneer with dspr
    sl "So you don't scare people!"
    "The girl laughed."
    show sl smile pioneer with dspr
    sl "Our parents are visiting the kids, so you know..."
    me "And you decided to visit me instead of going to your parents? Thank you!"
    show sl shy pioneer with dspr
    sl "No. There's just a lot to do today, but I thought I'd stop by when I had a free minute."
    menu:
        "Still, thanks":
            "I looked at the girl with undisguised appreciation."
            me "No one else came, just you."
            me "I wish I could do something nice for you, too."
            show sl laugh pioneer with dspr
            sl "Then just don't refuse to help anyone who asks you!"
            $ alt_day4_me_neu_transit = 'sl_cl'
        "I see":
            "We were quiet for a while longer."
            "And I kept crumpling and crumpling the silly panama in my hands."
    show sl shy pioneer with dspr
    sl "Semyon, you'll probably stop respecting me completely, but I don't think I'll be able to sit with you."
    sl "Yes, I understand, and I didn't come this morning, and I didn't bring breakfast, and now I'm running off somewhere..."
    sl "Commission, remember?"
    me "Let me guess who they've got as a tour guide."
    show sl smile pioneer with dspr
    "She smiled embarrassedly."
    if len(list_clubs_7dl) >= 1:
        sl "At least you can go to the club you signed up for! {w}Wouldn't you like to try it?"
        "I shrugged."
        me "No, I want to sit on a stump and be bored."
        sl "Okey-dokey."
    else:
        sl "It's a pity you didn't sign up for clubs."
        sl "Why don't you try it after all? I think the guys would be happy."
        me "It's a little late for that."
        sl "Better late than never."
        me "Not always."
        sl "Alright, it's up to you."
    "She patted me on the shoulder and stood up."
    show sl smile2 pioneer with dspr
    sl "And I'll see you at lunch, okay?"
    me "If they let me go."
    "I grumbled."
    sl "And if they don't, I'll bring you lunch myself, okay?"
    "She talked to me like to a cranky child - an irresistible maneuver, I couldn't even resent her."
    me "Go ahead."
    hide sl with dissolve
    "After waving goodbye to me, the girl disappeared."
    th "Ohoho, my sins are grievous."
    "My head got a little dizzy when I tried to get up, but I got over it pretty easily."
    me "Viola?"
    show cs normal at center with dissolve
    cs "I heard everything. Go. Don't make any sudden moves... pioneer."
    "Don't make any sudden moves, the doctor knows best."
    hide cs with dissolve
    "She left."
    return

label alt_day4_me_neu_aid_generic:
    scene bg int_aidpost_day with dissolve
    "I was moping my oatmeal, pondering the bleak prospects ahead."
    "Today's entertainment for the ailing Semyon included picking his nose, spitting at the ceiling, and finally discharging his smartphone in reader mode - praise be to Random for leaving it in the cabin."
    "An abyss of imagination. And for that last one, there's no telling where I should go."
    us "HUH!" with vpunch
    play music music_list["i_want_to_play"] fadein 5
    "It hurt in the head when it hit between the shoulder blades."
    "Inappropriately, I was suddenly reminded of the ancient ad about 'everything changes when they come!'"
    me "Little cunt, didn't they tell you not to yank, shake or hit me?"
    show us laugh sport with dspr
    us "Yeah, they were raving about something. I wasn't listening."
    "She held out her hand to me."
    us "Let's go."
    me "Where to?"
    show us calml sport with dspr
    us "Weirdo-man. Are you going to sit in four walls while the weather is like this outside? Let's go for a walk!"
    me "I'm not allowed."
    show us smile sport with dspr
    us "You may. I'll allow it. Let's go."
    "Without listening to anything else, the weasel dragged me along."
    menu:
        "Let's go!":
            "I had to relax and let myself be dragged around the camp."
            $ alt_day4_me_neu_date = 'us'
        "No, I wanna be alone":
            show us dontlike sport with dspr
            us "Nerd."
            hide us with dissolve
            "After chasing Ulyanka away, I was left alone, and..."
            "I decided to look for the squad leader."
            $ alt_day4_me_neu_date = 'mt'
    return

label alt_day4_me_neu_us:
    if alt_day3_us_bugs == 1:
        scene bg ext_houses_sunset with dissolve
        show us smile sport with moveinright
        us "Hello!"
        "Out of nowhere Ulyanka suddenly jumped out of nowhere - I'll be honest - making me wince in surprise!"
        me "Hi. What are you doing here?"
        us "Walking. Is that against the law?"
        me "I heard your parents were called to the camp leader."
        show us laugh sport with dspr
        us "Yes! They have a lot to talk about! Are you free?"
        me "Depends on what purpose you're interested in."
        "Cautiously I replied."
        us "Let's go, I'll show you something!"
        me "Maybe we shouldn't?"
        show us calml sport with dspr
        us "Feet in hand!"
        "She commanded, grabbed my arm and dragged me after her."
    scene bg ext_square_day at running
    play music music_list["i_want_to_play"] fadein 5
    "In fact, if I'm going to continue to communicate with this weasel, I should get some practice in moving around the camp at high speed."
    "Since the little one was moving like a meteor, ignoring corners and, I suspect, going through them in some places."
    scene bg ext_houses_day at fast_running
    "I, having no such skills, of course, caught a full supply of cones, twigs, and walls."
    scene bg ext_boathouse_day at fast_running
    play ambience ambience_boat_station_day fadein 5
    "And so immediately heaped praise on Random as we made our way out into the open - the pier."
    scene bg ext_boathouse_day with flash
    "This is where Ulyana stopped:"
    show us smile sport with dspr
    us "Wait here."
    hide us with easeoutbottom
    "She disappeared into one of the locker rooms."
    "I wanted to meditate for a little while, the environment permitting."
    "But the little one only gave me a few minutes."
    "She came back into sight:"
    show us laugh sport with dspr
    us "And now - run!"
    "She grabbed me by the arm and sprinted from a low start."
    "I didn't have time to ask what was wrong, and I was right to save my breath."
    "There was a scream behind me, a sharp stench of burning plastic."
    scene bg ext_boathouse_day:
        pos (0,0)
        linear 0.1 pos (-5,-5)
        linear 0.1 pos (5,5)
        pos (0,0)
        linear 0.1 pos (0,-5)
        linear 0.1 pos (0,5)
        repeat (12)
    with dissolve
    "And so, without saying a bad word, I accelerated, trying to keep up the speed."
    with fade
    $ alt_pause(1)
    scene bg ext_square_day with dissolve
    play ambience ambience_camp_center_day fadein 5
    "A few more minutes of frantic running and we leaned against the pedestal of Genda, trying to regain our breath."
    show us smile sport with dspr
    us "You're pretty good! You run fast!"
    if alt_day2_us_escape:
        me "I almost caught up with the train, if you remember."
        show us grin sport with dspr
        us "That's right, almost!"
        "The march-throw wasn't too long, so my breathing had already come back to relative normal."
        me "If both had fish for lunch."
        us "You're a dickhead."
        "She concluded and sat down on the steps of the pedestal and stared dreamily at the sky."
    me "Now spit it out."
    show us surp2 sport with dspr
    us "What? I didn't do anything."
    "Even if we hadn't just run through the whole camp..."
    "The most sincere person doesn't have eyes that crystal honest."
    stop music fadeout 3
    me "Ulyana!"
    play music music_list["my_daily_life"] fadein 3
    show us dontlike sport with dspr
    us "Nerd…"
    me "I'm waaitiiing!"
    "I reminded her."
    us "It's no big deal, honest! {w}There's something I left behind, and it's been attempted."
    me "So what? I didn't hear the noise of a fight."
    show us laugh sport with dspr
    us "As if I'm going to get my hands dirty with the little ones. Smoke grenade!"
    "Judging by the smell, tennis balls in the newspaper."
    me "You little potato. {w} Did you at least get it?"
    show us grin sport with dspr
    us "Of course!"
    "A snake appeared out of nowhere in her hands and jumped right in my face!"
    $ volume (0.0,'music')
    $ persistent.sprite_time = "night"
    $ prolog_time()
    play sound sfx_scary_sting
    scene black with fade
    dreamgirl "…get over here!"
    dreamgirl "Scorpion wins."
    "What an utterly foolish doom - to pierce space-time, to survive, to adapt in the Soviet Union, only to die from the sting of some viper."
    "Loser karma in action."
    "..."
    "No, man, that's too much even for loser karma!"
    play sound sfx_face_slap
    "A hard slap in the face seems to have been handed out by someone in solidarity with me on this issue." with hpunch
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene bg ext_square_day
    show unblink
    play sound sfx_face_slap
    with vpunch
    "I got hit in the face again - from the other side."
    us "So big, a man, and you fainted like a little sissy from the fifth squad!"
    us "Get up, you hear? {w}Or I'll call uncle Borya and he'll give you mouth-to-mouth CPR!"
    "Such a prospect frightened me no small amount - and I intercepted her hand, not letting her give me a third slap, too."
    $ volume (1.0,'music')
    me "I'm alive, I'm alive."
    show us calml sport with dspr
    us "Yeah? You can't tell by the look of it."
    me "Careful!"
    "I suddenly remembered."
    stop music fadeout 3
    me "There was a snake on you!"
    play music music_list["i_want_to_play"] fadein 15
    show us laugh sport with dspr
    us "This one?"
    "A snake head appeared beside me, and I almost fainted again."
    "But, luckily, this time the reptile's appearance lost its novelty effect, and, after a closer look, I found that the creeper was basically dead."
    us "Well, well! {w} I wanted to show it to you, and you went - boom -, eyes in a bunch, and flapped sideways!"
    us "I've only read that in books, I thought the authors were lying."
    show us smile sport with dspr
    us "Look, that's great! {w}If it scared you, it's all the more so for the rest."
    me "What do you mean?"
    "I asked cautiously."
    us "Well..."
    show us grin sport with dspr
    extend " You're a retard!"
    "Ulyana said it with such childlike directness that I changed my mind about being offended:"
    me "Why would you think that?"
    show us laugh sport with dspr
    us "Since all this time you haven't talked to a single girl properly!"
    if lp_mi > 5:
        us "I thought you liked Miku, but it turns out you don't. {w}You prefer to cry in the corner by yourself."
    if lp_dv > 5:
        us "Honestly, at first I thought you were hitting on Liska."
        us "I've never been so wrong."
    if lp_sl > 5:
        us "Went after the boss, went... Turns out you didn't know what you were doing!"
    if lp_un > 5:
        us "So touchingly pecked at Tisha, I thought you'd have it like in the last... Oops."
        "She bit her tongue, but I didn't understand anything."
    if alt_day3_sl_bath_voy:
        us "I almost thought you were one of those... menlayers?"
        me "Who?"
        show us shy sport with dspr
        us "Well! {w}Who likes boys! {w}But when I saw you..."
        "Ulyana marked something ball-shaped in the chest area."
        us "...peeping, I knew you were normal."
        th "Well, thank you!"
        with flash_pink
        "I realized I was blushing."
        us "Just a retard!"
    me "Stop calling me names. {w}I'm not a retard..."
    show us laugh sport far with dspr
    us "You're just a slow gas!"
    me "Yeah, you could say that. {w}So you dragged me to insult you?"
    me "Or don't want to get hit in the head alone for setting fire to the locker room?"
    if alt_day2_us_escape:
        me "So keep in mind, there's no way in hell I'm going anywhere or doing anything!"
    show us normal sport with dspr
    us "No."
    "She cautiously approached and retrieved the dead viper from subspace again."
    us "I wanted to show you."
    me "Show you?"
    show us calml sport with dspr
    us "Don't interrupt! I found it at night, but it seems to have been dead for a long time. {w} It's starting to stink."
    me "And?"
    us "You have to save her somehow, don't you understand? You know how to..."
    show us upset sport with dspr
    extend " what's the right way... toxidermy?"
    me "Toxie... what?"
    "I see. How then..."
    "Ulyana looked pleadingly into my eyes:"
    show us normal sport with dspr
    us "Can you do something?"
    me "Uh-huh, I'm going to lay my hands down now, and..."
    "I snorted and turned away."
    if counter_un_fz >= 1:
        "And then a familiar gatehouse next to the path to the pier caught my eye."
    else:
        "And then the gatehouse next to the path to the pier caught my eye."
    "Or rather, not the gatehouse itself, but the see-through second story with the fish hanging from it."
    me "I got it!"
    show us smile sport with dspr
    us "Yay! {w}What exactly?"
    me "We're going to dry it up."
    dreamgirl "We'll salt it and eat it. {w} Yum, almost like a chick."
    "I nodded at the gatehouse."
    me "You distract the watchman, I'll get in."
    if counter_un_fz >= 1:
        me "Almost like yesterday."
    show us dontlike sport with dspr
    us "Why you?"
    me "If you think you can do the cutting and gutting better than me, you're welcome."
    "I think that's where the little one got the creeps - she stared in horror at the snake corpse still hanging in her palm."
    show us upset sport with dspr
    us "You mean..."
    me "Yes."
    "Ruthlessly I continued:"
    me "Guts, liver, heart."
    "She turned a little green."
    me "Stomach - with a half-digested mouse!"
    show us fear sport with dspr
    us "Aaaah!"
    hide us with easeoutleft
    "She instantly shoved the bastard to me and dashed off toward the gatehouse."
    "And I, chuckling, followed her."
    scene bg int_attic_7dl with dissolve
    play ambience ambience_boat_station_day fadein 2
    "The attic smelled of salt and fish."
    "And, of course, the near water."
    "So for a second, when I closed my eyes and listened to the cries of the seagulls, the muffled splash of water, and the wooden clatter of boats against the decking, I could imagine that I was aboard some ancient schooner, and under my palm rested the steering wheel polished by thousands of touches."
    "Okay, well, that's for later, my goal..."
    "The searching gaze stumbled over the knife stuck in the deck."
    if counter_un_fz >= 1:
        "Yesterday's knife suffered a rather disappointing fate, so the boatman must have put a new one here."
    "Not that I have much experience gutting a variety of creepers, but if I can handle a fish, I can handle a snake."
    "That was... Nasty. That's all it was."
    "After scraping off the lighter snake remains, I rolled them in a bag of salt and hung them in a far, dark corner."
    th "I hope no one finds them."
    if counter_un_fz >= 1:
        "After our adventure yesterday, this place is full of my footprints, to which, moreover, today's footprints have been added."
    else:
        "Although the chain of footprints in the dust that stretched from the skylight to where I was now, hinted that it was extremely rare for anyone to come here."
    "I had to spend a few minutes erasing my traces."
    scene bg ext_boathouse_day with dissolve
    "No one was waiting for me downstairs."
    "I mean, no one at all."
    "But I sensed someone's presence."
    show us normal sport far at voy_left with dspr
    "Someone was nearby!"
    hide us with easeoutleft
    me "Gotcha!"
    "I thought Ulyana looked out from behind the gatehouse, but I wasn't sure."
    show us smile sport far at voy_left with moveinleft
    "And the moment I turned around"
    hide us with easeoutleft
    extend ", she disappeared!"
    show us smile sport far at voy_left with moveinleft
    $ alt_pause(2)
    hide us with easeoutleft
    $ alt_pause(1)
    "There was a stomping sound."
    show us laugh sport at voy_right with moveinright
    "And Ulyana looked out from the other side of the gatehouse."
    me "Stop being silly!"
    show us normal sport at center with moveinright
    us "You took a long time."
    "Did someone say 'nerd'?"
    "Did someone say 'a new limit of nonsense for the day is available'?"
    "I was finally condescended to!"
    me "No, I wasn't really disgusted."
    "I replied and tossed the snake innards in the trash."
    me "Did you distract the boatman?"
    us "Yes! I locked him inside."
    me "You... what?! Unlock him now!"
    if counter_un_fz >= 1:
        me "He's got a grudge against us. He might recognize us!"
    show us laugh sport with dspr
    us "Already! {w}He didn't notice anything anyway, just watched his stupid box."
    us "Did you do it?"
    me "Yeah. It'll hang for a couple of days and will be done."
    us "Will you take it off later?"
    me "No, I'll get it for myself and eat it."
    play sound sfx_7dl["eat_horn"] fadein 1
    show us dontlike sport with dspr
    "She pouted and stomped her foot:"
    us "Ah so! I..."
    show us shy sport with dspr
    us "Hey, that's not fair! You can't make fun of me!"
    me "Why so?"
    show us dontlike sport with dspr
    us "Because I'm a kid!"
    me "Let's go eat, kid!"
    "Without paying her any more attention I headed towards the canteen."
    stop music fadeout 3
    stop sound fadeout 3
    stop ambience fadeout 4
    return

label alt_day4_me_neu_mt:
    scene bg ext_polyana_sunset with clock_r
    play music music_list["into_the_unknown"] fadein 3
    play ambience ambience_forest_day fadein 3
    $ alt_pause(1)
    ".{w=.3}.{w=.3}.{w=.3}"
    "Okay, no kidding."
    "I didn't know where to look for her."
    "No, I mean, it was expected to see her at the beach or the boat station."
    "But she wasn't there."
    "Although that's probably an attempt to hide, too, similar to her attempt."
    scene bg ext_beach_day
    show prologue_dream
    with fade
    "So I checked the beach first."
    "Knowing perfectly well that it was useless. {w}Fine. {w}But I checked it out."
    "It's such a nice day, too."
    scene bg ext_boathouse_day
    show prologue_dream
    with fade
    "The children's screams made my temples stiffen, so I went to the boats."
    "I didn't get my hopes up much, it's just that it's rarely crowded."
    scene bg ext_adductius_7dl
    show prologue_dream
    with fade
    "From the dock my attention was caught by a lonely tree with a swing, and I headed there."
    scene bg ext_old_building_day_7dl
    show prologue_dream
    with fade
    "Then the old building..."
    scene bg ext_camp_entrance_day
    show prologue_dream
    with fade
    "Then down the path to the gate."
    "And since I checked one gate, I went to the other."
    "I remembered there was a fire glade nearby."
    scene bg ext_polyana_sunset
    show prologue_dream
    with fade
    "I didn't think I'd meet the leader here."
    "But I did meet her."
    "I think it's because we're thinking in the same direction."
    stop music fadeout 7
    "Olga sat with her back to me, feeding the tiny fire with scraps of some papers."
    scene bg ext_polyana_sunset with dissolve
    "They were important even in appearance - typewritten, glittering with seals."
    "I was about to call out to her, but a familiar red book flashed in the air. And I froze."
    "And the flames were already devouring the stamps of residency, military duty, age..."
    "Finally, the last piece of paper flew into the fire."
    play music music_7dl["wheres_wonderland"] fadein 3
    "I went over and sat down next to her."
    me "Olga... Dmitrievna?"
    "I've never seen her like that."
    "Her voice trembled for some reason."
    show mt normal pioneer with dspr
    mt "It's you…"
    "Being a gifted educator-psychologist is a God-given good thing."
    "Unfortunately, it imposes certain limitations."
    "For example, you can never reveal your soul to anyone else."
    "Because every action you take is looked upon as an attempt to manipulate those around you."
    "Just like now."
    "She sits hunched over, dropping her exuberant head, and I look at her and try to figure out exactly what strings she wants to pull this time."
    "How exactly she wants to affect."
    "She smiled weakly."
    "Without moving her gaze away from the fire."
    if alt_day3_dj == 'dv' or not alt_day3_technoquest2:
        me "Olga Dmitrievna... {w}Slavya was looking for you."
        me "Asked me to give you this list, said you'd know what to do with it."
        mt "What is it? {w}Another letter? {w}Give it here."
        "She crumpled up the sheet without looking and threw it into the fire!"
        "It burst into flames like gunpowder, burning instantly."
        show mt smile pioneer with dspr
        mt "Here's another 'there was no sadness' burned."
        me "What are you doing?!"
        mt "Relax, nobody will know anything."
        me "Except for Slavya, who sent me to you!"
        show mt grin pioneer with dspr
        mt "Really? Wow. Well, what can you do, if you were in such a hurry you lost the paper and didn't bring it to me."
        me "..."
        "She smiled smugly and winked at me - like, I'm not going to snitch on my leader, am I?"
        me "And anyway... Olga Dmitrievna?"
        mt "Hmm?"
        me "You're squad leader."
        show mt sad pioneer with dspr
        mt "Ah."
        "Undefinedly she said, continuing to stare into nowhere."
        mt "That's right, yeah? {w}I'll always be Olga DMITRIEVNA for you."
        mt "And you're just another pioneer to me."
        mt "Really?"
        mt "And I'm just a squad leader. That's all."
        "She fell silent and looked away."
    "Silence."
    "The paper was burning fast. {w}There was just so much of it."
    me "What are you doing here?"
    show mt normal pioneer with dspr
    mt "Ever wondered about death?"
    me "Excuse me?"
    mt "There are about five billion people on earth, it's impossible to meet and know absolutely everyone."
    if (alt_day2_convoy not in ('dv', 'sl', 'un')):
        $ counter_mt_7dl += 1
    mt "That's why documents are so important."
    mt "You live, and you have a document giving you the right to do so."
    mt "If you don't have papers, you don't have rights. {w}You can't even die. {w}You can't."
    show mt smile pioneer with dspr
    mt "It's great, isn't it?"
    mt "I have a paper. {w} And you don't have any more."
    mt "I just killed you."
    "She pointed her index finger in my direction and squinted her left eye."
    show mt grin pioneer with dspr
    mt "Bang. {w}You're dead."
    me "What are you talking about?"
    show mt smile pioneer with dspr
    mt "Oh, I'm sorry. {w}You're not dead. {w}You just don't exist anymore."
    me "So that really was my passport?!"
    "I screamed, jumping up."
    show mt normal pioneer with dspr
    mt "Of course. {w}I burned everything. {w}The money I tried, but I couldn't do anything about coins."
    mt "So I buried them."
    "What surprised me was the apathy with which I took it."
    "Probably because I was completely preoccupied with inventing a way to get her back to camp."
    "And it's not just that Slavya is stitching up there alone."
    "Not only that."
    "Olga Dmitrievna looked lonely and sad - as if she had burned something important along with my papers."
    me "Why did you do that?"
    mt "Will you try to take my word for it, that it was necessary?"
    me "And my passport, my passport, why did you burn it?"
    "I sank down on the log beside her and stared dejectedly into the burning fire."
    show mt smile pioneer with dspr
    mt "I don't like the idea of you being six years older than me."
    me "How do you know?"
    "Instead of answering, she shook a check in front of my nose - Yandex.Money card deposit, December 21, 2018."
    th "Who knew?"
    "And she threw the check, along with the rest of the paperwork, into the fire."
    me "And that was enough."
    "It wasn't a question."
    "So she just nodded."
    me "Okay. {w}There's no me. {w}I don't exist. {w}What next?"
    mt "The usual. {w}When my shift's over, I'll take you home, and then we'll see."
    me "What's all this for, then? {w}Couldn't you have taken me home {b}with all my papers{/b}?"
    mt "No. {w}The bus might be stopped for a document check."
    me "And I don't have any."
    "The papers burned out for good."
    "And for some reason I didn't care at all: I, hysterical, suddenly realized for a split second that it was only now that everything was right."
    "The squad leader stood up and held out her hand to me."
    mt "Welcome aboard… Semyon."
    mt "Don't be so sad about your passport. {w}We'll think of something."
    me "You mean you escaped from the camp, abandoned your post - all to burn papers?!!"
    mt "No, of course not. {w} I had some business to attend to, and I just left for a minute."
    me "Olga Dmitrievna!"
    show mt laugh pioneer with dspr
    mt "Oh, fine, for ten minutes."
    show mt smile pioneer with dspr
    "She showed me her tongue."
    "Grown-up woman!"
    "I shook my head reproachfully."
    play sound sfx_7dl["eat_horn"] fadein 1
    "And from the direction of the camp came the call for lunch."
    mt "Alright, let's go."
    "Turning on her heels, Olga hurried toward camp."
    "Not a word more about the strange conversation."
    stop music fadeout 3
    stop sound fadeout 3
    stop ambience fadeout 6
    return

label alt_day4_me_neu_home:
    scene bg int_house_of_mt_sunset with dissolve
    play music music_list["timid_girl"] fadein 5
    "Fourth day on the front lines. The squad leader had already left, leaving a thermos and a paper bundle on the table."
    if alt_day3_dj == 'dv' and alt_day3_dancing2 != 'dv_2':
        "I listened: I couldn't hear any music from the street."
        th "So those knuckleheads couldn't fix the radio. Well, I did everything I could!"
        th "It's a shame, of course, that Dvachevskaya never got the job..."
        dreamgirl "Yeah, and you would've ran around as her assistant too!"
        th "No way!"
        "I undoubtedly liked Alisa, but not so much that I'd feel bad about missing out on an opportunity to spend time with her."
        th "And anyway, not all is lost! I can't imagine how much more there will be at this camp."
    "Judging by how well I felt, I finally got a good night's sleep."
    "And judging by the clock..."
    "The smartphone clock read eleven o'clock."
    th "Oh. That makes sense then."
    "I got my feet off the bed."
    th "What on earth got into our zealous squad leader that she wouldn't even wake me up and toss me into morning exercises?"
    th "Maybe she's sick?"
    dy "Parents of Sidorova Ulyana, please come to the camp director's office."
    th "Parents?"
    th "Parents' Day!"
    if (alt_day3_dancing2 != 'dv_2'):
        "I got dressed in a hurry and jumped out into the street."
        th "If Olga's relatives come too, and she brings them here..."
    else:
        th "I hope Alisa isn't tattling to her relatives about Semyon, who ruined her career as a DJ..."
        "I didn't want to meet the redhead right now!"
        "So I hurried out of the cabin, looking for shelter."
    stop ambience fadeout 2
    play sound sfx_open_door_1
    $ alt_pause(1)
    scene bg ext_house_of_mt_sunset with dissolve
    if (alt_day3_dancing2 != 'dv_2'):
        "I didn't want to think about it."
    return

label alt_day4_me_neu_un:
    $ alt_day4_me_neu_date = 'un'
    scene bg ext_houses_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 3
    play music music_7dl["will_you"] fadein 3
    "We left the house when all the lights went out..."
    "In fact, there were no lights at all."
    "Neither did the pioneers."
    "The street greeted me with utter desolation - except for the loudspeakers purring somewhere in the very far background, it was quiet and lonely all around."
    me "And where have all the pioneers gone?"
    "With a clever look I asked the empty air."
    "No answer."
    "With a sigh, I staggered off to wash my face."
    scene bg ext_house_of_un_day with clock_l
    "After washing, I walked home at a leisurely pace, and only my heightened hearing in the total silence allowed me to hear some kind of argument in raised tones."
    "Clearly not from our cabin."
    "And from where?"
    "Upon listening, I determined with precision that it was Lena and Miku's cabin."
    "An argument between the leader and Lena."
    un "I want Semyon, and I don't want you prying into the pioneers' private affairs."
    mt "It's my business, too."
    un "Why should it be?"
    mt "Girl, you're forgetting yourself. I'm still your squad leader."
    un "Since when are squad leaders the vice police?"
    "Snorted Lena in response."
    mt "Always have been. I'm telling you again, stay away from Semyon."
    un "I guess I'll decide for myself how and who to stay away from. You don't mind, do you?"
    "Mockingly she stretched out."
    mt "You don't understand something, so why don't you just listen to me and don't make trouble."
    un "Offer declined."
    mt "I see. We are deaf to the voice of reason, then."
    mt "Then listen carefully."
    "Does it seem that something concerning me personally is about to be said? Well, well, well..."
    "I walked up close to the cabin and turned into a listening ear."
    mt "...a mental disorder. He doesn't remember anything that happened last year."
    mt "And you want to take advantage of his helplessness for your own silly worries."
    mt "Don't you realize how bastardized that looks?"
    un "..."
    un "You think I don't know that?!"
    "Lena's voice broke into a scream."
    mt "What?"
    un "Do you think I'm blind and deaf?"
    "The leader clearly stammered, digesting the new data."
    mt "You do realize that everything you had last year is irrelevant to him, don't you?"
    un "Yes, and I don't care!"
    un "Don't try to pretend to understand our relationship with him!"
    "I decided it was time to step in."
    "The floorboards creaked under my footsteps, and the door swung open."
    play sound sfx_open_dooor_campus_1
    $ alt_pause(1)
    scene bg ext_house_of_un_day at zenterright
    show mt laugh pioneer at cright with dissolve
    mt "Here he is, by the way."
    me "Uh... Greetings."
    show mt normal pioneer at right with move
    show un shy pioneer at left with dissolve
    "After the squad leader appeared on the porch, Lena carefully peeked out from behind her shoulder."
    un "H-Hello."
    mt "Semyon, we want to ask you a question."
    me "Listening extremely carefully."
    "I importantly nodded."
    mt "Look carefully at Lena."
    me "With pleasure!"
    "I replied, causing another flash of embarrassment to that one."
    me "Is that the whole question?"
    mt "No."
    mt "Tell me... How long have you known this girl?"
    if lp_un >= 10:
        "Obviously, this is a test. The right answer was on the surface."
        "But will I be able to play the part to the end?"
        menu:
            "A few years now":
                show mt shocked pioneer with dspr
                "The leader froze, shocked by my answer."
                mt "You mean, you..."
                "Her voice broke off."
                "I stood there, not understanding her reaction."
                "Continuing to smile stupidly."
                show un smile3 pioneer with dspr
                un "See?"
                "The girl's eyes sparkled victoriously."
                show mt normal pioneer with dspr
                "To the squad leader's credit, she pulled herself together very quickly."
                mt "Well, if that's the way it went..."
                un "How?"
                show mt angry pioneer with dspr
                mt "No matter."
                "Cut off the leader, finally calming down."
                mt "It's parents' day, and there's a committee going around camp."
                mt "Tikhonova, has your parent already left?"
                show un normal pioneer with dspr
                "Lena nodded."
                mt "Then I don't want to see you or him before dinner."
                mt "If you're so smart, you'll find something to occupy your cavalier."
                show un shy pioneer with dspr
                un "B-but..."
                mt "Is that clear?"
                show un normal pioneer with dspr
                un "Yes."
                mt "I dare not delay you any further. By the way, Semyon, there's something for you back at the cabin, pick it up later."
                hide mt with easeoutbottom
                "Reported Olga Dmitrievna and flew away."
                "Lena stood for a while longer, looking thoughtfully after her, until I broke the silence with a tactful cough."
                un "Yes, keep you busy."
                "After thinking for a while, the girl suggested:"
                un "Come up to the sports ground in twenty minutes, o-okay?"
                me "Do you want me to bring anything?"
                un "N-no, I've got everything on me."
                stop music fadeout 3
                scene black with fade2
                $ alt_pause(2)
                play ambience ambience_camp_center_day fadein 3
                scene bg ext_tennis_court_7dl
                show un normal sport
                with dissolve
                "It took me half an hour to get to the playground - somebody's kind soul decided to provide the starving pioneer with sandwiches and smoked chicken."
                "And I have a rough idea what kind of soul it was - green-eyed, in a sports uniform, hugging her figure nicely."
                "Lena, who knows where she got the sporting equipment, was minting the shuttlecock over and over again, hitting it sharply and jerkily."
                if dr and (alt_day2_date == 'un'):
                    "And she was hitting much more confidently than the day before yesterday."
                me "That was fast."
                "I smiled."
                show un shy sport with dspr
                "Lena was already habitually embarrassed, but not as shattered as I was used to - she didn't even miss the shuttlecock."
                un "Will you join me?"
                "The girl waited a while and, apparently finding the conversation exhausted, continued chasing."
                me "To the game?"
                "The height of intellectual expression."
                show un normal sport with dspr
                un "Y-yes... The tennis players are resting today, so..."
                me "Oh, I see."
                "What a conversation."
                show un shy sport with dspr
                un "D-don't you want to?"
                "Lena, still red, stared diligently past me."
                me "May I?"
                "Her smile could have been the model illustration for the word 'insecure.'"
                "But the girl swung her racket extremely eloquently."
                "Apparently that should be taken as permission."
                "I stepped onto the court and, choosing my racket according to weight and comfort, took a seat on the red gravel."
                un "Here we go!"
                play music music_list["went_fishing_caught_a_girl"] fadein 5
                show un smile sport with dspr
                "And just where did the shy pioneer girl go."
                un "First serve!"
                "'Sharapova's' eyes lit up with excitement."
                "From the first serve, Lena let me know she was very determined."
                play sound sfx_tennis_serve_1
                "The underage badminton player had a very heavy arm, and it was often necessary to get the shuttlecock out of impossibly difficult situations, almost jumping like a goalkeeper on a goal."
                "That is, instead of an aristocratic game, it was an extremely exhausting action, forcing you to give it your all."
                show un smile sport with dspr
                un "One-zero in my favor! Give me the shuttlecock, my serve."
                "It wasn't even a question of giving in - I just wanted to keep it level myself!"
                "Lena was flexible enough to respond to any of my serves, luckily my arms were still long enough."
                "Even managed to win back a few points by cutting a few 'candles' over the very net."
                "But we ended up in slightly different leagues."
                "As it turns out, badminton isn't one of those activities that turns out well from the first second, either."
                "Experience counts here, too."
                show un smile2 sport with dspr
                un "Get it together. You don't want to lose to a girl, do you?"
                "Feet shoulder-width apart, half-bent, racket frozen in right hand, ready to fend off a full 360 degrees attack."
                un "Because I don't need a giveaway."
                "No shyness at all. {w}All that nonsense, like embarrassment or awkwardness, is left on the other side of the fence."
                "I guess that's the way Lena is only alone with herself... Or with her closest friends."
                "It wasn't that I didn't appreciate the trust she gave me."
                "But she drove me around like she wanted to."
                "The gap was getting wider. I couldn't breathe anymore, my hands were shaking a little from the oxygen intoxication, my eyes were getting darker."
                "And I kept wanting to spit the gooey saliva, but it was kind of embarrassing in front of the girl."
                "So I braced myself and braced myself, yawning serve after serve, until it came from the other side of the net."
                show un smile sport with dspr
                un "Game."
                "Lena smiled at me, looked me in the eye..."
                show un shy sport with dspr
                "And immediately I flinched, flinched, blushed - I remembered what our relationship was like."
                un "Thanks for playing."
                me "Y-yes..."
                th "Go away already, at last, and let me spit!"
                un "See you later."
                hide un with dissolve
                "As if she'd heard the mental message, she put her racquet on the stand and, with a nod, headed for the court."
                play sound sfx_7dl["eat_horn"] fadein 1
                "Meanwhile, from the canteen came the ever memorable 'take the spoon.'"
                "And I felt suddenly how hungry I was."
                $ alt_day4_me_neu_transit = 'un_7dl'
                stop music fadeout 3
                stop sound fadeout 3
                return
            "For four days, why?":
                pass
    "I stared at Olga Dmitrievna perplexedly."
    me "Is this some kind of incomprehensible test?"
    show un cry pioneer with dspr
    pause(.3)
    hide un with moveoutright
    "Lena's eyes gleamed, and she darted past the leader, exhaling, and ran down the steps..."
    play sound sfx_close_door_campus_1
    $ alt_pause(1)
    "Gone."
    "And we're alone."
    show mt normal pioneer with dspr
    mt "Not a test, it's just that the pioneer has got it into her head that you've known each other a hundred years."
    me "I wonder why."
    mt "I have no idea myself. Nobody said anything about a hundred years."
    mt "Well, I don't have time to talk to you now, I'm running away."
    me "Where to?"
    hide mt with dissolve
    mt "Business, business!"
    "It echoed."
    return

label alt_day4_me_neu_mi:
    play music music_list["my_daily_life"] fadein 10
    scene bg ext_houses_sunset with dissolve
    "I barely managed to open the door{w=.3}{nw}"
    play sound sfx_body_bump
    scene white with flash
    extend ", as I bumped into someone on the doorstep." with vpunch
    voice "Ow!"
    scene bg ext_houses_sunset
    show mi sad pioneer
    with dissolve
    "I saw Miku holding her head on the doorstep."
    mi "My mother told me to knock when you came in..."
    "She mumbled to herself."
    me "I'm sorry, that was too harsh..."
    "I'm not finished."
    show mi smile pioneer with dspr
    mi "It's okay, I've got a whole bone in there anyway."
    show mi sad pioneer with dspr
    "She tapped her head - and it looks like she hit a bump."
    mi "Ow!"
    me "Maybe you should go to the infirmary."
    show mi smile pioneer with dspr
    mi "Yeah, it hurts and it leaks. Sem, really, that's enough. I'm actually here for you."
    mi "Leaks?"
    "I shrugged."
    if alt_day3_dj == 'mi':
        "She looked wrinkled and tired."
        me "Did something happen?"
        mi "What? Oh, nothing."
        me "Miku!"
        show mi upset pioneer with dspr
        mi "DON'T YELL AT ME!"
        "She immediately looked back at me guiltily."
        mi "Oh. I'm sorry. It's just the lack of sleep."
        me "Did someone disturb your sleep?"
        show mi shy pioneer with dspr
        mi "How do you know?"
        me "Actually, I was kidding."
        mi "I wasn't!"
        "Miku told me about 'something' that was making strange noises at night and stomping around her cabin."
        "That she was scared, so she couldn't sleep a wink until morning."
        me "It must have been a hedgehog."
        me "Why didn't you call for help?"
        mi "I didn't dare... It doesn't matter now. I'm here about something else."
    if counter_mi_7dl == 2:
        mi "Has your suit gone anywhere yet?"
        "I shrugged."
        me "Yeah, it's hanging in the cabin. Why?"
    mi "Today's the day no one comes to see me."
    mi "I want to clean up a little. And I'll take care of the costumes while I'm at it."
    mi "Will you help?"
    me "Why not?"
    show mi happy pioneer with dspr
    mi "Great!"
    if counter_mi_7dl == 2:
        mi "Then grab the suit and let's go."
    else:
        mi "Then let's go!"
    $ alt_day4_me_neu_date = 'mi'
    scene bg int_musclub_day with clock_r
    play ambience ambience_music_club_day fadein 3
    show mi normal pioneer far at left with dissolve
    "We've been seriously busy cleaning for a couple of hours."
    if counter_mi_7dl == 2:
        "Or should I say, I did the cleaning, while Miku diligently cleaned and ironed and tidied up my new clothes in every way."
        "I was diligently playing Mary Poppins with a mop and a bucket and rags."
    else:
        "I was playing Mary Poppins with a mop, bucket and rags."
    stop music fadeout 5
    "The boardwalk was easy to clean, but the dust on the horizontal surfaces was a problem."
    "There were too many of those horizontal surfaces."
    me "What's that?"
    play music music_7dl["but_why"] fadein 3
    "I picked up an A4 sheet of paper from the windowsill, from which a fragile, impossibly beautiful image of someone had been torn out in nervous, jagged strokes."
    me "She looks like Lena."
    show mi upset pioneer at center with dissolve
    mi "Don't touch!"
    "Miku snatched the drawing out of my hands."
    mi "It was Lena who forgot, and she really, really doesn't like it when someone touches her drawings."
    me "Forgot?"
    "I shook my head in doubt."
    me "This thing is too beautiful to just be forgotten."
    show mi shy pioneer with dspr
    mi "Couldn't play along with the girl!"
    me "Excuse me?"
    show mi normal pioneer with dspr
    mi "Couldn't just be normal without turning on the smartass mode."
    "She sighed:"
    mi "She didn't forget."
    me "You stole it?!"
    show mi dontlike pioneer with dspr
    mi "No! How could you think that!"
    mi "I just asked Lena to sit in the club, to keep an eye on the place, since no one was coming to see her tonight."
    mi "And she saw you and ran away."
    show mi happy pioneer with dspr
    "Miku sighed dreamily."
    mi "Always running away when she sees you. Very shy."
    me "So, who's the girl in the picture? She looks like Lena, but it's definitely not Lena."
    show mi upset pioneer with dspr
    mi "This..."
    "It was with great difficulty and regret that Miku reversed her own talkativeness:"
    show mi shy pioneer with dspr
    mi "I'm sorry, Senya, but it's not my secret."
    me "You mean you won't tell?"
    show mi normal pioneer with dspr
    "The Japanese girl shook her head negatively."
    mi "Then I'll ask her myself!"
    me "And get a scandal for touching her drawings."
    show mi smile pioneer close with dspr
    "Miku took my hand and squeezed my fingers lightly:"
    mi "Don't, Sen, don't open this subject. {w}Why would you?"
    stop music fadeout 5
    "I immediately melted and smiled stupidly."
    show mi smile pioneer far at left with dissolve
    "After assuring myself that I was no longer running to make a revolution, Miku took the sheet to the shelf where the sheet music stood in a row and placed it between the albums."
    play music music_list["everyday_theme"] fadein 5
    show mi smile pioneer at center with dissolve
    mi "Here, and no one will sweep it on the floor, and you can find it."
    me "I demand contribution!"
    show mi shy pioneer with dspr
    "Miku blushed:"
    mi "Right now? But we barely know each other, no, of course I'm not that strongly against it, but you have to hold out for a while, otherwise it'll devalue everything..."
    dreamgirl "Counter-what are you demanding there?"
    "A nasty chuckle from the inner voice."
    me "No, that's not what I meant!"
    "I was confused myself when I realized exactly what Miku had heard."
    me "I mean, I demand satisfaction."
    dreamgirl "I don't think you fixed anything."
    show mi shocked pioneer with dspr
    "Miku, mouth ajar, looked at me with some kind of {i}new{i} expression on her face."
    if loki:
        me "Look, stop bitching!"
        show mi laugh pioneer with dspr
        mi "I'm sorry, but you're so funny embarrassing!"
    elif herc:
        me "I suppose words like 'satisfaction' are going to be misunderstood by you too?"
        show mi smile pioneer with dspr
        mi "A little bit!"
        me "You like to mock me, don't you?"
        "She smiled, and she got adorable dimples on her cheeks."
        mi "Sorry, I didn't mean it."
    else:
        me "But... But... But..."
        dreamgirl "You may remain silent."
        "The inner voice burst into laughter."
        dreamgirl "Anything you say will be used against you in the morgue!"
        show mi laugh pioneer with dspr
        mi "Uh… h… Calm down, Senya…"
        "Through laughter Miku squeezed out."
        mi "I get it."
    show mi smile pioneer with dspr
    mi "So what do you want?"
    me "I'm thinking that maybe the three of us could get together somewhere after lights out and have a good time."
    mi "I don't think Olga Dmitrievna would agree."
    me "And we... We'll say we have an upcoming performance! And maybe we'll prepare something!"
    "I've been fascinated by the idea myself."
    me "We could do a hit song, like Butusov or Tsoi or something."
    show mi smile pioneer with dspr
    mi "I'm interested! What's in it for you?"
    th "She's not as naive as she pretends to be."
    me "I told you, it's a contribution."
    mi "A threesome?"
    "Her eyes gleamed with slyness again."
    me "Yes!"
    mi "Senya, you tell me honestly - do you like my roommate?"
    mi "I won't tell anyone!"
    "I have raised my eyes to grief."
    me "Do you have to look for subtexts? {w}It doesn't occur to you that I just want to..."
    show mi grin pioneer with dspr
    mi "I heard that! {w}To drink tea in good company and ask silly questions."
    me "Shit, if you don't want to, you don't have to!"
    show mi upset pioneer with dspr
    mi "No, that's not what I meant..."
    play sound sfx_7dl["eat_horn"] fadein 1
    "Our conversation was interrupted by the sound of the horn."
    "I was glad it did, because I had no desire to continue the conversation."
    me "Alright, Miku. I'll be going."
    hide mi with dissolve
    mi "Yeah... Oh, I didn't thank you for helping me clean up!"
    scene bg ext_musclub_day
    with dissolve
    play sound sfx_close_door_1
    "But I've already made it outside."
    th "And I want to be mad at Miku, and I can't."
    dreamgirl "You should be mad at yourself first. You say stupid things, and then you get offended."
    th "I what?!"
    dreamgirl "I know you like Miku. Why don't you call her in for tea, how long are you going to beat around the bush?"
    dreamgirl "Now she'll think you're trying to hit on Lena. The shift isn't endless, so you'll sleep it off until you leave."
    th "Like that's the most important thing."
    dreamgirl "What's important? Eating and sleeping? Go eat then, that's the only thing you're good at."
    return

label alt_day4_me_neu_sl:
    scene bg ext_house_of_mt_sunset with dissolve
    "No one seems to be bothering me today, disturbing me, dousing me, forcing me to be on duty and loading me with other unpleasant things."
    "Nice!"
    "I sank into the chaise lounge and, throwing my arms behind my head, stretched out and moaned blissfully."
    show sl normal pioneer with dissolve
    sl "Still lazing around?"
    me "Mmmm... how about that. What a bliss!"
    show sl smile pioneer with dspr
    sl "Bummer."
    "Slavya chided me."
    me "Why 'bum' all of a sudden? I have an unscheduled Children's Day. So quick, everybody, protect me from worries and troubles."
    show sl laugh pioneer with dspr
    sl "Chatterbox."
    "Slavya laughed - and then she got serious:"
    show sl normal pioneer with dspr
    sl "I've been looking for you. You owe me some favors."
    me "What's that?"
    sl "Remember when you went with the checklist and where you signed up? So..."
    hide sl with dissolve
    "She nodded and disappeared from sight."
    sl "Mind you, I'm going back in half an hour!"
    if len(list_clubs_7dl) < 1:
        me "What if I didn't sign up anywhere?"
        "With a clever look I asked the empty air."
    "Well, what do I... I shouldn't ruin the mood by swearing over such nonsense."
    "After thinking for a while, I decided to take refuge in the temple of knowledge."
    th "Reading's not a bad way to kill time, either."
    "If my memory serves me right, the last dozen pages of 'Young Technician', which you'd find in any library, were always devoted to good fiction."
    "So it was here."
    scene cg d2_micu_lib with clock_r
    "Zhenya was true to her habits - you could probably carry out half the library past her, and hell if she'd wake up."
    "So I tiptoed over to the coffee table, which was laden with thick stacks of 'Novel Newspaper', and pulled out a box of copies of 'UT'."
    "I had to act with care and circumspection."
    "At one point the librarian moved, and I froze in a cold sweat."
    scene bg int_library_day with dissolve
    "Fortunately, the threat had passed, and I, having chosen the freshest issues - judging by the smell of casein that had arrived this year - dragged them off to the reading corner."
    "The chair was ugly, inexplicably pretentious, upholstered in some moth-eaten velvet, and in the most important place squeezed almost to the floor."
    "So I neglected the safe stools and chairs and climbed into the chair with my feet."
    "A pioneer seat wouldn't lie."
    "Nothing much happened for a couple of minutes, and I even started to read about the incredible adventures of some boy abducted by aliens."
    "But then someone blocked the sunlight."
    "I looked up."
    show sl normal pioneer at center with dissolve
    "Slavya? Hmm. I seem to be popular with her today."
    if max(counter_sl_7dl, counter_sl_cl) > 2:
        th "Although after the beginning of our communication it is not surprising."
    else:
        dreamgirl "Well, yeah, first time in three days you've graced her with more than a few words."
    me "Yeah, did you want something?"
    sl "Yes."
    me "Is something wrong?"
    sl "Not that..."
    me "So something happened."
    show sl smile2 pioneer with dspr
    sl "Eh..."
    "She smiled weakly."
    sl "Must be great being you and knowing everything."
    sl "Especially when something happens."
    "Her voice sounded thoughtful."
    me "Slavya, you're dodging the question!"
    show sl shy pioneer with dspr
    sl "Oh, I'm sorry. I just thought that you, since..."
    "She cut herself off."
    sl "Well, I guess I'd better be going."
    me "Wait a minute!"
    "Without getting up from my seat, I caught her hand."
    me "Let's make a deal - you tell me what happened, and I promise I won't say a word to anyone."
    "She took a deep breath."
    sl "It's actually none of your business."
    sl "It's not mine either, for that matter."
    "Surprised at how quickly she surrendered, I let go of my hand - which she removed behind her back with visible relief."
    sl "Olga Dmitrievna handed out instructions, everything works fine without her."
    sl "I just had a question and she's nowhere to be found."
    show blinking
    me "And you don't have time to look for her."
    "I took the hint."
    sl "I'm sorry. I don't get along with these parents."
    show sl smile2 pioneer with dspr
    sl "Like children, honestly!"
    voice "Where's our escort?"
    "A man's voice came from the street."
    menu:
        "We'll see":
            show sl dontlike pioneer with dspr
            stop music fadeout 3
            "Slavya was clearly unhappy with my answer, but without saying anything, went back to the tour."
            hide sl with dissolve
            "And I went back to my books."
            us "Hello, Syomich!"
            show us smile sport with easeinright
            "The floorboards creaked - the red meteor stopped next to me, turning into a short girl with paired spike tails of an impossible scarlet color."
            me "And good day to you, too."
            us "I missed you very much, too!"
            "Trustingly she informed me."
            us "All night long I've been spinning and suffering. Let me show you something."
            me "What?"
            us "Come on, why are you like a small kid?"
            "She grabbed my hand and dragged me along."
            $ alt_day4_me_neu_date = 'us'
        "Alright, I'll go look for the squad leader":
            hide sl with dissolve
            stop music fadeout 3
            "After chasing Slavya away, I was left alone, and..."
            "I decided to look for the leader."
            $ alt_day4_me_neu_date = 'mt'
    return

label alt_day4_me_neu_dinner:
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 3
    "Lunch crept up as usual - unexpectedly, but very casually."
    "In honor of my visiting parents, the cooks had splurged on a strange delicacy - a sweet soup of apricots and rice."
    "I seriously feared for my health if I were to taste this something generously poured on plates."
    "Fortunately, the failed experiment in soup was more than compensated for by the lazy stuffed cabbage rolls, which I had gorged myself on, hoping to dull my hunger a little."
    stop ambience
    play sound sfx_scary_sting
    with flash_red
    with vpunch
    mt "Chin up, Semyon! If you keep sitting like that, the guests will think we keep using whips as punishment!"
    play ambience ambience_dining_hall_full fadein 3
    play music music_list["smooth_machine"] fadein 3
    show mt laugh pioneer with dspr
    "The compote spurted treacherously from my nose. Through my coughing tears, I glared angrily at the giggling squad leader."
    th "Noooo, we mock the pioneers differently!"
    th "We sneak up from behind while they chew!"
    dreamgirl "Cheer up, Semyon!"
    dreamgirl "If you keep being so dramatic, the voice in your head will think you're emo!"
    mt "Anyway, I was wondering, what are you going to do during quiet hour?"
    th "Uh-oh..."
    dreamgirl "Uh-oh!"
    show mt smile pioneer with dissolve
    "Olga smiled predatorily, looking at my puzzled face."
    mt "Don't worry, I won't ask you out - there's too much to do today."
    mt "It's just that on parents' day we need to show at least a semblance of a routine, so you can't wander the grounds today."
    me "And on the other days I could, couldn't I?"
    show mt angry pioneer with dissolve
    with vpunch
    pause(0.3)
    me "Ouch!"
    "It's a legitimate thing to get hit on the top of my head with a rolled-up panama."
    mt "I'm not forcing you to sleep, you're an adult. But try to find something to do that doesn't draw too much attention."
    show mt normal pioneer with dissolve
    mt "Remind me, what club did you sign up for?"
    if 'music' in list_clubs_7dl:
        me "The music club."
        mt "That's great. Miku could use some help rehearsing the concert for Parents' Day!"
        th "I'm not much of a helper..."
        th "The only thing I can do is be a part-time microphone stand, and not without a chance of screwing up."
    elif 'cyber' in list_clubs_7dl:
        me "The cybernetics club."
        mt "Great. I think there's definitely something to work on there."
        th "Yeah, especially for someone whose entire technical background consists of Asimov books..."
    elif 'nwsppr' in list_clubs_7dl:
        me "The wall newspaper."
        mt "That's great. You can write a whole article about Parents' Day during the quiet hour."
        th "Well, wait, is there something else to do?"
        th "That wasn't the deal!"
        me "Well, if we get inspired..."
    elif ('soccer' in list_clubs_7dl) or ('volley' in list_clubs_7dl) or ('badmin' in list_clubs_7dl):
        if 'soccer' in list_clubs_7dl:
            me "Football."
        if 'volley' in list_clubs_7dl:
            me "Volleyball."
        if 'badmin' in list_clubs_7dl:
            me "Badminton."
        mt "Great. Boris Alexandrovich will give you the inventory."
        if 'badmin' in list_clubs_7dl:
            th "Will he also give me a partner? Or do I have to wave my racket around for two hours for no reason?"
        else:
            th "Yeah, along with a team. And the opposing team as well!"
    else:
        me "I haven't had a chance to sign up yet..."
        mt "Then I suggest you check out the library. With an interesting book the time will fly by!"
        th "Cool!"
        th "I've been wanting to reread 'Capital' for a while now, but I never got the chance..."
    mt "So it's a deal. Now finish your meal and march out!"
    hide mt with moveoutright
    th "The woman had no worries..."
    th "However, she won't check to see if I've done her most important errand, will she?"

    with fade3
    "The stuffed cabbage rolls alone were too little for my growing body, so I got up from the table as I sat down - hungry."
    "I wouldn't say it bothered me."
    "After all, they always offered something relatively edible for noon. And then it wouldn't be long before dinner..."
    "All that remained to be decided was whether I would heed the sound advice of my dear and beloved squad leader, or seek alternative entertainment in the old fashioned way."
    if len(list_clubs_7dl) == 0:
        "I didn't feel like dragging myself to somewhere I would be loaded with work, so I didn't hesitate and headed out..."
        $ alt_day4_me_neu_escape = True
    else:
        menu:
            "To clubs!":
                "I didn't want to drag myself somewhere where I could potentially be harnessed, but I wanted to get a scolding from Olga even less. So I sighed and went off to socialize in a pleasant collective."
            "Escape!":
                $ alt_day4_me_neu_escape = True
                "I didn't feel like dragging myself to somewhere I would be loaded with work, so I didn't hesitate and headed out..."
    stop ambience fadeout 6
    stop music fadeout 6
    return

label alt_day4_me_neu_sport:
    play music music_list["went_fishing_caught_a_girl"] fadein 3
    scene bg ext_playground_day with fade
    play ambience ambience_soccer_play_background fadein 2
    "After lunch, as you know, comes the siesta. Our formidable gym teacher's 'afternoon' lasted about all day, so there was an unrealistic chance of finding some kind of ball and hitting the gym wall for two hours at a time, imagining someone unpleasant in its place."
    dreamgirl "Dude, you're freaking me out."
    dreamgirl "Have you looked at your watch? And the sun?"
    if (alt_day3_technoquest2) and (alt_day3_dj != 'dv'):
        dreamgirl "The nurse is certainly a nice lady, but I don't think you'll impress her with a simple sunstroke."
        dreamgirl "You need at least an open fracture!"
    else:
        dreamgirl "If you want to play the great martyr so much and doom yourself to a horrible death, I suggest drowning. It'll be quicker and much less painful."
    th "What would I do without your advice..."
    "But contrary to my expectations, parents and pioneers were scurrying around the playground. There was an awning on the porch of the covered building, which, judging by the dust and creases, was clearly not meant to escape the sun."
    th "Wait, aren't the kids supposed to be snoozing peacefully in their beds right now?"
    dreamgirl "I could ask you the same question."
    "Anyway, there was clearly something going on here, and that something didn't look enticing at all. I turned around and hurried to get away, but I was stopped by a loud shout:"
    ba "Hey, deputy!"
    th "Deputy?!"
    th "The tent didn't seem to help. The old man's definitely got a bigger bump on his head than mine!"
    ba "Come here, I said!"
    "I did not know what the consequences of disobedience were, but I did not want to find out. After counting to ten in my head, I turned around and staggered toward the gymnasium porch."
    show ba normal uniform at fright with dspr
    "Under the makeshift tent stood a table, densely littered with black and white photo cards. Between the two poles that held the flimsy structure in place were strings of cords, lavishly hung with flags."
    "But on closer inspection, the flags turned out to be photographs. These were the pictures the honored guests were staring at while their offspring explained to them what was going on in the pictures, trying desperately to shout over each other."
    if alt_day2_mi_snap or counter_sl_cl >= 5:
        th "I'd forgotten there was a staff photographer at camp. He took a lot of pictures during the shift!"
    else:
        th "And I wondered why he was strutting around the canteen with a camera during the tournament. So he's a staff photographer, too?"
    th "Oh, what a mess I'm in..."
    "Sanich nodded at me to come closer."
    ba "We're having a photo fair, and I can't be here all day - I have things to do."
    "I could hardly keep from snickering. Our gym teacher had the most pressing business of all - hiding in the covered building from the scorching sun."
    ba "So I'm assigning that task to you."
    "He waved his broad paw in the direction of the photo table."
    ba "Parents will choose cards of their children hanging over the table. Your job is to find copies among those on the table, slip them into envelopes, and give them to the parents."
    me "Why is it so complicated? Why can't you just take the pictures off the ropes and give them to the parents?"
    show ba smile uniform at fright with dissolve
    ba "Too easy!"
    "The gym teacher grinned."
    ba "Marketing, have you heard the word? No pictures above the table, no one will be interested."
    "Obviously, he just wanted to show off his work to as many people as possible. But I didn't say that out loud, of course."
    ba "So keep your face simple and go ahead. Otherwise your sour face might make your parents think someone died in our camp!"
    hide ba with moveoutright
    pause(0.1)
    play sound sfx_close_door_clubs_nextroom
    "Clapping me on the shoulder with all his might, Sanich disappeared in a familiar direction: behind the gymnasium door. I shuddered at the crowd at the table."
    th "Maybe I should run away quietly, before anyone sees?"
    th "They'll find the right pictures themselves, they're not little kids anymore. And the tent's too old for anyone to want to steal it..."
    "But the memory of the encouraging pat on the shoulder was too fresh for the instinct for self-preservation to kick in. With a heavy sigh, I stepped toward the table."
    th "May each one be rewarded according to his deeds!"
    voice "Can I have these pictures?"
    voice "I'll have that one!"
    voice "And I'll have those three!"
    th "I wonder if our esteemed photographer is at least paid for his consumables."
    th "I'm a cynical bastard brought up by capitalism, but I don't believe that Sanich would spend his own money on all this beauty, and give it away for nothing!"
    "Sneakily I glanced at the pictures I stuffed in the envelopes."
    if alt_day2_mi_snap:
        th "I wonder if there's a picture of me and Miku in here together."
        "But either Miku had been here before me, or the gym teacher hadn't had time to develop the last pictures - the cards mostly showed little kids I didn't know."
    th "How much I've missed..."
    "Sometimes I caught a glimpse of familiar faces. I saw Slavya dancing at the disco, or Miku galloping across the stage, or Alisa clutching her guitar with a serious expression, just like a local rock star."
    "Ulyana flashed more often than the other squadmates: probably because of her age she did not suffer from the typical teenage worries about 'did I turn out well?' and joyfully jumped under the lens of a gym teacher at every opportunity."
    "I once again pushed aside a picture of her proudly posing with a volleyball on the beach."
    th "There was a time..."
    th "If a man in my day had tried to take a picture of a child in a bathing suit, it would have raised howls to the skies. But here it's all right, hanging there in the midst of all the other camp memories, smiling all over."
    "The pile of pictures on the table was melting fast."
    th "There's a certain charm to the black and white photos. Perhaps an understatement?"
    th "When you look at Lena's photos, you wonder what color her hair is. And only if you know her personally can you say with certainty: it's..."
    play music music_list["awakening_power"] fadein 3
    voice "That's it, you're screwed!"
    voice "Ooh!"
    "Startled by the surprise, I looked around for the source of the noise. A couple of feet away from my 'stand', two boys about ten years old were clashing."
    if herc:
        me "Knock it off!"
        "To the indignant whispering of my parents, I rounded the table and sprinted toward the brawlers in two steps."
        me "Boys, break it up!"
        "But the boys didn't think to respond to me. Their parents clearly weren't here, which meant only one thing: at the command of someone else's stern shout, the fight wouldn't self-liquidate."
        "And my patience was far from iron!"
        me "Where are you? In a camp or in a juvenile detention center?"
        "Roughly grabbing both of them by their shirt collars, I pulled the boys apart with ease. But in their fervor they didn't think to pay any attention to me."
        play sound sfx_punch_medium
        with vpunch
        voice "I'll kill you!"
        play sound sfx_punch_washstand
        with hpunch
        voice "Get off me, idiot!"
        "I shook them both sensibly. One of the parents shrieked indignantly."
        play sound sfx_thunder_wood
        with vpunch
        with hpunch
        pause(0.3)
        play sound sfx_angry_ulyana
        me "Quiet!"
        "I barked, causing the boys to instantly shut up and stop lashing out."
        me "What troop? Who's your squad leader?"
        "The boys didn't answer, continuing to sniff softly and glaring angrily at each other."
        me "Are you deaf?"
        "I was about to shake them again, but I heard heavy footsteps behind me. The brawlers stared fearfully behind me."
        show ba evil uniform with dissolve
        ba "Let the kids go!"
        play sound sfx_wind_gust
        $ volume(0.5, "music")
        "Now it wasn't just the boys who were scared. A chill ran down my spine."
        "I obediently unclasped my hands, but the children stayed where they were, as if they'd been pinned to the ground."
    else:
        th "Do I have instructions for situations like this?"
        th "I don't recall."
        "I looked apprehensively at the fighting men. The parents were wailing and begging the children to disperse, but clearly the adults weren't related to the couple - the kids wouldn't do something like that in front of Mom and Dad."
        voice "Break them up already!"
        th "I don't know anything, I can't hear anything!"
        "I didn't want to get hit over the head for exceeding my authority, so I chose the optimal strategy, code-named 'my house on the edge'."
        "Stay back and don't interfere."
        th "They'll figure it out without me. They're boys, they have fights on a schedule at least three times a day!"
        show ba evil uniform with dissolve
        ba "Stop this at once!"
        "Jumping out of the covered enclosure like the devil out of a snuffbox, Sanich was already hurrying toward the young troublemakers. The boys had expectedly obeyed the gym teacher's menacing bass, and were now standing still, waiting for payback."
        ba "What's all the commotion around here?"
        voice "He drew a mustache like Hitler's on my picture!"
        voice "It's his own fault! He's been teasing me all shift!"
        ba "I don't care which one of you is the instigator. Tomorrow you'll both be on canteen duty!"
        ba "Maybe in a day of working together you'll learn to negotiate instead of swinging your fists."
        ba "Dismissed!"
        $ volume(0.5, "music")
        "The boys were blown away. The parents left, too, traitorously leaving me alone with the angry bear."
        "Sanich looked at me menacingly."
    show ba normal uniform with dissolve
    stop music fadeout 3
    if herc:
        ba "Well, they're brainless, but what are you doing?"
        ba "It's not pedagogical to hit kids. That's why I'm not flogging you right now, but I'm trying to teach you that that's no way to break up a fight!"
        "I shuddered. There was something... military about Sanich."
        me "Sorry, sir, I overreacted."
        ba "That's right!"
    else:
        ba "Didn't have the heart to call me?"
        me "I didn't think about it..."
        ba "What's your head for? Got anything in it?"
        "Sanich shook his hand."
    ba "All right, help me get all this off and get out of here. You're as much use as a goat's milk."
    hide ba with fade
    "The tent, the table, and the rest of the pictures we had cleaned up in the shortest possible time. Obviously, we wanted to get rid of each other's company as soon as possible."
    th "The character of our gym teacher, of course..."
    th "I'll never set foot here again!"
    $ alt_day4_me_neu_ba_duty = True
    $ volume(1.0, "music")
    stop ambience fadeout 6
    stop music fadeout 6
    return

label alt_day4_me_neu_cyber:
    play ambience ambience_camp_center_evening fadein 5
    scene bg ext_clubs_day with fade
    play music music_list["so_good_to_be_careless"] fadein 2
    "At the doorstep of the cybernetics club, I slowed down."
    th "Maybe I should just leave?"
    th "No, really, what am I going to do in the company of two nerds?"
    dreamgirl "Wow, now we're talking!"
    dreamgirl "You're not a nerd: you're an activist, a humorist, the life of the company, and just a handsome man!"
    th "But I'm..."
    th "I am..."
    dreamgirl "..."
    th "..."
    "With a heavy sigh, I pulled the door handle."
    play sound sfx_open_door_clubs
    stop ambience fadeout 2
    scene bg int_clubs_male_day with dissolve
    play ambience ambience_clubs_inside_day fadein 1
    show el smile pioneer with dissolve
    el "You came after all!"
    "Electronik rejoiced at me as if I were his own, jumping up from his seat."
    if alt_day3_technoquest2:
        hide el
        show sh normal pioneer far at fright
        with dissolve
        pause(0.3)
        show sh serious pioneer far at fright with dissolve
        pause(0.1)
        hide sh with dissolve
        "Shurik, for his part, nodded at a loss, then stared again at the book in front of him. Judging by the cover, far from technical content."
        th "So they're just reading Strugatsky here and having high-minded conversations about a utopian future, artificial intelligence, and extraterrestrial technology?"
        th "Well, there's a chance we'll get along!"
        show el smile pioneer with dissolve
        "Deciding not to distract our important boss, I turned to Syroezhkin."
    else:
        me "Where's our leader?"
        show el sad pioneer with dissolve
        el "In the hospital wing. I just came from there - visited him this afternoon."
        el "If he gets worse, Viola will take him into town for a checkup, but he hopes to be back for the rest of his shift."
        "Not that I'm much concerned about the goggle man's health, but his premature demise would definitely spoil the relaxed atmosphere of this camp."
        "I looked questioningly at Syroezhkin."
    me "So, bring me up to speed. What are we working on, what's the status of development, any progress, what are we aiming for?"
    show el smile2 pioneer with dissolve
    "Electronik pointed with the most contented face to some kind of device shaped like a truncated cone."
    el "There! This is our primary task for today."
    el "A task of paramount importance. If we fail, our club will be abolished and we'll all be stripped of our commendation!"
    th "It's rough out there, though..."
    th "Wait, stop!"
    me "But that's a coffee grinder!"
    show el grin pioneer with dissolve
    el "Oh, you're good with technology!"
    "Not a trace of sarcasm flashed in his tone."
    el "Viola brought it in this morning. Told me to have it fixed by tonight, or else..."
    th "Yes, yes, they'll close down your little shithouse and you'll be broomed up your ass..."
    "It seems there was only one person in this camp who could appreciate the peculiar humor of our stray nurse."
    dreamgirl "I guess you appreciated it when she examined you on the day of your check-in!"
    th "I was caught off guard!"
    me "And what ended up happening to the coffee grinder?"
    show el normal pioneer with dissolve
    el "That's what we have to find out. I haven't found anything strange yet."
    el "It's going to take some time to fix, too..."
    if alt_day3_technoquest2:
        show sh serious pioneer at fright with dissolve
        "I cast a questioning glance at Shurik, but he was staring at his book, stubbornly ignoring his surroundings. He didn't seem to take Viola's threats seriously, unlike his partner."
        hide sh with dissolve
    me "Well, let's see what's going on here."
    hide el with dissolve
    "I sat down at the table, pulled the coffee grinder toward me, and started twirling it in my hands with a smart-ass look, as if that might get me closer to understanding the cause of the malfunction."
    el "The wire is all right, there's no loose wire anywhere. The mechanism is intact, spins as it should, but for some reason refuses to start."
    th "Shut up!"
    th "You're stopping me from making obvious assumptions!"
    "It was a familiar grinder, a similar machine in my mother's kitchen."
    "I had used it a couple of times at most: by the time the caffeine addiction set in, I had long since lived apart. And I preferred instant coffee - why go to all that trouble?"
    th "I only remember how difficult it was to get the lid protrusion into the right groove the first time to start this infernal machine!"
    "I looked under the lid - not so much out of curiosity as to appease Electronik standing over my soul."
    th "It can't be..."
    th "If it were that obvious, Syroezhkin would have figured out what was wrong with her in a matter of minutes!"
    me "Uh, El... Serega, there's a piece broken off."
    show el surprise pioneer with dissolve
    el "Where?"
    th "No way, he hasn't realized?"
    me "It starts when you press the lid, doesn't it? Give me something hard and thin!"
    "I started the mechanism with an outstretched screwdriver, looking at the stretched face of Electronik with superiority."
    th "Has he never seen a coffee grinder in his life?"
    if alt_day3_technoquest2:
        show sh serious pioneer at fright with dissolve
        th "At least Shurik should have guessed!"
        show sh normal pioneer at fright with dissolve
        pause(0.3)
        hide sh with dissolve
        "Shurik looked at the sudden source of the noise without much interest, then stared at the book again."
        th "Does he even care what's going on here?"
    show el grin pioneer with dissolve
    el "So it works!"
    "With undisguised relief exhaled Syroezhkin."
    me "You need to build up the chipped lever, and then the grinder will function properly again."
    th "I'm good! I'm a hero! I saved the cybernetics club from being shamefully shut down!"
    th "Where's my pie?"
    dreamgirl "On the shelf. Check behind that bottle of acetone over there!"
    play sound sfx_knock_glass
    pause(0.2)
    play sound sfx_knock_glass
    pause(0.2)
    play sound sfx_knock_glass
    "I was distracted from my jubilation by a sudden knock on the glass."
    show el normal pioneer with dspr
    play sound sfx_knock_glass
    pause(0.2)
    play sound sfx_knock_glass
    pause(0.2)
    play sound sfx_knock_glass
    "And then another one after that. And another."
    show el think pioneer with dissolve
    el "What's that? Birds?"
    th "Yes, yes, we have two birds with red plumage..."
    dreamgirl "There are more than seven people in the camp, you dolt. Those must be the Syroeyezhkin groupies from the younger squads!"
    th "You think he has groupies?"
    dreamgirl "Have you heard of sapiosexuals?"
    "The knocking went silent, and I turned Electronik."
    me "Did you happen to have a date with anyone?"
    show el scared pioneer with dissolve
    el "A date?"
    "The guy almost choked."
    el "What does that have to do with..."
    stop music fadeout 0.5
    $ volume(0.5, "sound")
    play sound sfx_7dl["window_glass_break"]
    $ volume(1.0, "sound")
    show el shocked pioneer
    with hpunch
    pause(0.3)
    play music music_7dl["genki"]
    "It was cut short by the sound of flying glass."
    el "Aah!"
    if (alt_day3_technoquest2):
        show sh surprise pioneer at fright with dissolve
        sh "Aah!"
        "Both cyberneticists jumped up from their seats and stared fearfully toward the broken window."
    dreamgirl "Is this World War III?"
    dreamgirl "Let's go loot!"
    "Now there was no doubt in my mind as to who was standing outside the window."
    me "Everyone stay where you are! Starting a counter-terrorist operation."
    play sound sfx_close_door_1
    scene bg ext_clubs_day at running with dissolve
    play ambience ambience_camp_center_evening fadein 5
    "I leaped out of the clubhouse like a bullet, not listening to Electronik's timid objections."
    th "The little bugger runs fast, but she's dressed too conspicuously."
    th "That's all right, I'll shove her stones up her..."
    scene bg ext_path2_day at running with dissolve
    "Behind the clubhouse there was an inconspicuous path, the most obvious retreat for the raunchy Ulyana."
    scene bg ext_washstand_day at running with dissolve
    stop music fadeout 4
    "Indeed, a bright red stain of her trademark T-shirt flashed by the corner to the washbasins."
    me "Kid!"
    scene bg ext_washstand_day with dissolve
    show us smile sport far with dissolve
    pause(0.2)
    show us smile sport with dissolve
    play music music_7dl["everyday"] fadein 2
    "To my greatest surprise, the girl slowed down and turned toward me."
    "When I reached her, panting and puffing, she smiled broadly with the most contented look."
    us "I thought I couldn't reach you!"
    us "Now, straight to the point..."
    me "Slow down with the points! Don't you want to apologize for your shenanigans first?"
    show us sad sport with dspr
    "I glanced sternly at the momentarily downcast girl."
    show us upset sport with dissolve
    us "Well, what are you starting..."
    "She glared at me frowningly."
    show us dontlike sport with dissolve
    us "Will you take me to the squad leader?"
    "She looked like I was her last ally, but at the most responsible moment, I stabbed her in the back without a second thought."
    th "Do they have a course in psychological manipulation as part of the school curriculum?"
    th "If it does, it's a very working course..."
    me "I won't. But will you at least explain to me why you're doing this pogrom?"
    show us normal sport with dissolve
    us "I had some business with you."
    show us grin sport with dspr
    us "But I don't think you'll go for it, you don't have the guts!"
    th "That's where you're screwed, honey!"
    th "I don't go for dares. Too old for that."
    $ girls_list = ('dv', 'un', 'mi', 'sl')
    $ lp_max = max( [eval('lp_'+w) for w in girls_list] )
    $ max_who = [w for w in girls_list if eval('lp_'+w) == lp_max]
    $ max_who_id = max_who[0] if lp_max > 5 and len(max_who)==1 else ''
    th "Although if on your place was{nw}"
    if max_who_id == 'mi':
        extend " Miku…"
    elif max_who_id == 'dv':
        extend " Alisa…"
        dreamgirl "…the window would definitely be intact!"
    elif max_who_id == 'sl':
        extend " Slavya"
    elif max_who_id == 'un':
        extend " Lena…"
    elif max_who_id == '':
        extend "…"
        dreamgirl "…skinny, pale little chick!"
    me "I don't have time for your nonsense. I have a window to fix behind you."
    show us surp1 sport with dissolve
    us "So you won't turn me in?"
    th "Where am I going to go..."
    "I looked at Ulyana sternly."
    me "But remember, little one: you owe me a debt."
    th "And you won't get away with it with a gingerbread in the canteen!"
    dreamgirl "And you..."
    th "Hussars, silence!"
    show us grin sport with dissolve
    us "Deal."
    hide us with moveoutright
    "With a cheerful wink, Ulyana galloped off toward the cabins, leaving me utterly confused."
    th "So what did she want from me in the end?"
    dreamgirl "You don't understand! There must be mystery in a woman!"
    th "If only there had been a woman..."
    "All that was left was to go back to the club."
    stop music fadeout 3
    stop ambience fadeout 2
    scene bg ext_clubs_day with dissolve
    play sound sfx_open_door_clubs
    pause(0.7)
    scene bg int_clubs_male_day with dissolve
    play ambience ambience_clubs_inside_day fadein 1
    show el surprise pioneer with dissolve
    play music music_list["take_me_beautifully"] fadein 3
    "When I opened the door, Electronik standing by the window jumped up, almost dropping the glass on the floor."
    me "Where did you get the glass?"
    show el normal pioneer with dissolve
    el "Yeah, we had it in the back room. Did you find out who it was?"
    me "The boys in the junior squad made a slingshot and tested it on our wall. I couldn't catch them, but I'll be able to identify them if I can."
    "Without blinking an eye, I lied."
    th "I wish I knew what joy I had in covering up for Ulyana!"
    "Without an answer, I rushed to Syroezhkin's aid. There was not much time left before the end of the quiet hour."
    scene bg int_clubs_male_day with joff_r
    show el smile pioneer with dissolve
    el "Well, nothing seems to be noticeable."
    if (alt_day3_technoquest2):
        show sh normal pioneer at fright with dissolve
        "Shurik, as I supposed, stood by helplessly the whole time that Electronik and I were fiddling with the ill-fated glass."
    me "Yeah. Only how are we going to explain to Viola that we failed her party assignment?"
    show el smile2 pioneer with dissolve
    el "Ah, don't worry about that! I fixed it while you were running."
    if not herc:
        th "I wish all problems in life were solved this way: you ran, waved your fists, shook the air in vain, and in the meantime everything has already been done for you."
    else:
        th "As usual, I was extremely helpful. It seems to be my burden to do the wrong things in the wrong places."
    me "Well, now that the tasks are over, let's go have an afternoon nap."
    th "I hope that was the first and last time I've ever been driven to their club!"
    $ alt_day4_me_neu_us_debt = True
    stop ambience fadeout 6
    stop music fadeout 6
    return

label alt_day4_me_neu_music:
    scene bg ext_musclub_day with dissolve
    play ambience ambience_camp_center_day fadein 5
    play music music_list["everyday_theme"] fadein 5
    "Standing on the porch of the music club, I reached for the doorknob, but something kept bothering me."
    if alt_day4_me_neu_date == 'mi':
        th "Should I even go to her after what I said this morning?"
        th "She'll turn me around and send me straight to Lena, so it won't be a problem!"
    else:
        th "I didn't want to learn the basics of music, nor did I want to show that I already knew how to do something. Listening to Miku babble for two hours, even less so."
    th "But I need somewhere to pass the time before dinner, and not get caught by the squad leader. This place is quiet and deserted..."
    th "Perhaps even too quiet for the abode of our machine-gun girl!"
    play sound sfx_medpunkt_door_open
    "I tried to open the expectedly locked door."
    th "Well, at least I tried."
    th "Now I can in good conscience blame it on the procrastinating supervisor and go to bed!"
    dreamgirl "Have you forgotten what day it is?"
    th "In fact, I don't remember what day it was yesterday either! Sorry, they don't have calendars here."
    dreamgirl "Parents' Day, you idiot! What happens on Parents' Day?"
    th "Inedible lunchtime munchies?"
    "Inner voice mentally hid his face in his palms."
    th "Okay, I get the hint. Do you think they're rehearsing on stage?"
    dreamgirl "No, in your cabin. That's why the squad leader sent you away!"
    scene bg ext_stage_normal_day with dissolve
    "By my conservative calculations, it was about five minutes until quiet time, so I had enough time to make it to the stage."
    th "If Miku isn't there, then I give up!"
    scene bg ext_stage_big_day_7dl
    show mi normal voca far
    with dissolve
    "But Miku was on stage alright. Not alone, but in the company of a raging crowd of kids, and what's interesting is that they were all from the younger squads."
    th "Yeah, it's not like it's such a status event that the first troop is stressed out. Maybe I should get out of here before it's too late."
    show mi grin voca far with dissolve
    mi "Senechka!"
    th "And no, it's too late."
    if alt_day4_me_neu_date == 'mi':
        th "Doesn't she even resent me?"
    hide mi
    show mi grin voca with dissolve
    "Miku jumped up to me in three jumps, and her face lit up as if she'd seen a bag of presents instead of a scowling uncle mimicking a pioneer."
    mi "Senechka, you have no idea how timely you are! We have so little time to rehearse, and the kids can't get organized; I can't do it all by myself..."
    if alt_day4_me_neu_date == 'mi':
        th "Oh, I wish she resented me!"
    else:
        th "What this camp knows first-rate is how to make full use of a lucky manpower!"
    me "I understand the task. What should I do?"
    mi "Entertain those who aren't performing somehow, and preferably in a way that they don't make any noise!"
    th "Do I get a clown nose?"
    dreamgirl "You have one of your own. Check your pockets!"
    me "I'll try."
    show mi happy voca with dissolve
    "Miku glowed, completely ignoring my sour face."
    mi "Thank you so much, I don't know what I would have done without you!"
    "She turned to the crowd of performers and, to my great dismay, shouted:"
    show mi normal voca with dissolve
    mi "Children! All of you who are not performing now, go to Semyon! I'll call you one by one!"
    hide mi with dissolve
    stop music fadeout 4
    "With a sense of accomplishment, Miku fluttered onto the stage, and I was left alone with a couple of dozen eyes glaring at me."
    scene bg ext_stage_normal_day with dissolve
    me "Well, kids..."
    if herc:
        play music music_7dl["anglegrinder"] fadein 3
        me "Listen to me. Those who are waiting their turn sit quietly like mice and watch their comrades perform."
        me "Those who have already performed sit on the bench and wait for an afternoon snack. With their mouths closed."
        me "Got that?" with vpunch
        "One of the boys jumped. I gave the brat a stern look."
        me "Did I say something funny?"
        "The boy was embarrassed and tried to hide behind the backs of the other kids."
        me "Ten push-ups! Now!"
        th "If such disciplinary methods work among the big foreheads, they certainly should among the little ones!"
        "The boy was in no hurry to do push-ups."
        dreamgirl "You have no power here!"
        th "No way! I'll teach them how to obey their elders!"
        me "Are you deaf? I got your ass!" with hpunch
        me "Or should I call Boris Alexandrovich to supervise the process?"
        "The pioneer, blushing with anger, obediently lowered himself onto the grass and began to do push-ups. The other children watched the process in complete silence."
        th "I think that's what Miku asked me to do..."
        dreamgirl "And I think she asked you to entertain them, not to haze them!"
        th "All's fair in war. Can you imagine entertaining children without them making noises?"
        dreamgirl "A game of silence?"
        "It was a good idea, but it was too late: the hapless boy had finished his push-ups, and now the kids were staring at me like rabbits at a boa constrictor. There was no way I could let it go now."
        me "If there are no more fun-loving kids, we settle on the benches and wait for the leader's command to go to the stage. Any questions?"
        stop music fadeout 5
        "There were no questions."
        "For the entire two hours of the rehearsal I stood by the stage, frowning at the children. Even if they did talk, they did it as quietly and inconspicuously as possible."
    elif loki:
        play music music_7dl["carefree"] fadein 3
        me "Did you know you're in for a surprise today?"
        kids "Surprise?"
        kids "What surprise?"
        kids "And when? When is the surprise?"
        th "If I had known, I would have shared it with you!"
        me "Quiet!"
        "With a conspiratorial lowering of my voice, I continued:"
        me "The surprise awaits only those who will sit quietly for the entire rehearsal. I'm telling you this in confidence..."
        "I gave the kids a mysterious look. They stopped talking and moved closer so they wouldn't miss anything important."
        me "You're so wanted, and I shouldn't have told you about it, but it would hurt me if any of you didn't get the reward because of your own stupidity. So not a word to anyone!"
        "Demonstratively pressing my finger to my lips, I took a step back."
        me "Do we have a deal?"
        "The children cheerfully nodded. To my great joy, in silence."
        me "Then take your seats on the benches and be good!"
        "I myself sat down behind everyone else so as not to let the intrigued children out of my sight."
        dreamgirl "Do you really think such a cheap trick will work?"
        th "No. But it was worth a try!"
        "Contrary to my schizophrenic fears, the trick worked, and just like that: not only did the kids not make any noise, but they also shushed the restless ones who tried to talk."
        th "Wow, it's just like that experiment where the prisoners in the prison were assigned as wardens..."
        dreamgirl "Your pedagogical methods are amazing!"
        dreamgirl "Just don't forget that you have to surprise them at the end of the rehearsal so they don't get upset and disrupt the concert. Have you figured out how you're going to get out of it?"
        th "You're insulting!"
        stop music fadeout 3
        "The minnows had patience until the end of the rehearsal. I didn't need more than that, though."
    else:
        play music music_7dl["groovie"] fadein 3
        "I was silent, looking back at the children in confusion. They, in turn, lost interest in me almost instantly, and went on doing what they had been doing before I arrived - babbling."
        th "Now what am I supposed to do with them?"
        dreamgirl "Get it together, wimp! Show them who's in charge!"
        me "This is a very important rehearsal, so try to be quiet, okay?"
        "The kids ignored me, continuing to chatter loudly inside their little companies. I coughed expressively, but again it had no effect."
        me "So, that's it. Let's play the silent game!"
        "No one was willing to play. I felt panic gripping me."
        th "They don't listen to me at all!"
        dreamgirl "They're kids! Just offer them some trinkets in exchange for silence."
        th "But I don't have anything!"
        dreamgirl "Well, think of something. What do you need your head for?"
        me "Who wants to ride on my back?"
        "The kids were quiet for exactly one second, only to turn and rush over to me, shouting at each other."
        kids "Me! I want it!"
        kids "Me first!"
        kids "No, me!"
        me "Quiet!"
        me "I'll only ride for those who sit quietly and wait their turn to perform. Deal?"
        me "So sit on the benches and keep your mouths shut! Those who behave, I'll give you two rides."
        "The stunt almost succeeded: the kids did settle on the benches. They didn't stop talking, but they were a lot quieter than before my impromptu ride."
        "And I..."
        with fade
        scene bg ext_stage_normal_day at running
        kids "Go, big turtle!"
        "A girl of about eight, sitting on my hump, waved a branch menacingly. I was doomed to grope around the benches."
        th "At least they don't weigh much. I hope that kid Ulyanka's age won't be tempted by the opportunity to sit on the back of a goofball a couple of years older..."
        stop music fadeout 3
        scene bg ext_stage_normal_day with fade2
        "By the end of the quiet hour, my shirt was soaking wet and my shoulders felt almost wooden."
    play music music_list["she_is_kind"] fadein 3
    show mi normal voca far with dissolve
    mi "Thank you all for the rehearsal, you were great!"
    if dr:
        th "How I've been waiting for those words!"
    mi "Now run along to lunch, and don't be late for the concert: you all still need to change into your costumes!"
    hide mi
    show mi smile voca with dissolve
    "Jumping off the stage, Miku came straight to me."
    mi "And thank you again, thank you very, very much! All the kids were so well behaved, and how did you manage to handle them?"
    if loki:
        play music music_7dl["genki"] fadein 3
        kids "Where's our surprise?"
        dreamgirl "So what's the plan there?"
        me "Ask Miku!"
        me "Miku, don't you remember that you promised your kids a surprise?"
        show mi surprise voca with dissolve
        "The girl's eyes rounded, and I struggled to contain a typically villainous giggle."
        mi "What su…"
        me "Good luck!"
        scene bg ext_stage_big_day_7dl at running
        "I ran as fast as I could from the stage, laughing out loud. Miku shouted after me resentfully, and the little ones swarmed her, waiting for a reward for good behavior."
        if alt_day4_me_neu_date == 'mi':
            th "It seems I can forget about forgiveness..."
        else:
            th "I seem to have made another enemy..."
        th "Who cares, though? That was fun!"
        $ alt_day4_me_neu_mi_resentment = True
        stop ambience fadeout 3
        stop music fadeout 3
        return
    stop music fadeout 3
    if herc:
        me "I've been reading the literature on pedagogy in my spare time. You know, some methods work quite well!"
    else:
        me "Better not ask..."
    scene bg ext_dining_hall_near_day with fade3
    play music music_list["smooth_machine"] fadein 2
    $ alt_pause(1.01)
    show mi smile pioneer with dissolve
    mi "I think the concert will go great! The main thing is that the kids don't forget that Slavya is dancing between the cat song and the metallophone solo, because they always get confused with the order of the exit."
    if alt_day4_me_neu_date == 'mi':
        "If I should have talked to Miku about this morning's incident, I couldn't have found a better time."
        me "Miku, listen... About Lena and everything..."
        show mi surprise pioneer with dissolve
        "The girl waved her hands in fright."
        mi "What are you, Senechka, you do not have to justify yourself to me! It's none of my business at all!"
        me "I didn't mean to make excuses! It's just that I didn't mean it that way..."
        show mi shy pioneer with dissolve
        mi "I'm going to run to lunch, or I won't have time to change. Thanks again for your help!"
        show mi shy pioneer far with dissolve
        $ alt_pause (0.3)
        hide mi with dissolve
        "Miku rushed forward, leaving me confused once again."
        th "She wouldn't even listen to me!"
        dreamgirl "You know, I understand her very well."
        th "Fuck you!"
        "I followed Miku, angry at myself for my own stupidity."
        th "Why did I even say anything about Lena?"
    else:
        me "Is Slavya performing, too? Then why wasn't she at rehearsal?"
        mi "She asked me to relieve her because she's been with guests all day anyway, she hasn't had a minute to spare."
        th "Slavya is deliberately slacking off on social activities? Well, well, well..."
        show mi shy pioneer with dissolve
        "As if anticipating uncomfortable questions, Miku hurried off abruptly."
        mi "I have to eat faster so I have more time to prepare, so no offense, but I'm running!"
        show mi shy pioneer far with dissolve
        $ alt_pause (0.3)
        hide mi with dissolve
        "She ran toward the dining room. I shrugged and followed."
        th "Well, we all have our secrets..."
    stop ambience fadeout 6
    stop music fadeout 6
    return

label alt_day4_me_neu_nwsppr:
    scene bg ext_library_day with dspr
    play music music_list["get_to_know_me_better"] fadein 5
    "It was habitually deserted outside the library."
    th "I wonder if there's anyone alive here at all."
    th "Buzzkill, of course, is napping - not at work, but in the cabin. She hasn't been seen doing anything else."
    th "The cyberneticists are probably writing another essay on the great Soviet science, if they're not busy in their main club. But something tells me that the paper is not at the top of their priority list."
    th "But Lena..."
    if alt_day4_me_neu_date == 'un':
        th "I wouldn't want to be alone with her. These morning stunts of hers I frankly didn't like!"
    elif alt_day3_un_fz_neu_transit:
        th "I don't think she wants to see me after last night's dance."
    else:
        th "Lena doesn't look like the kind of person who would be happy to have company."
    "I went up to the library porch with a sigh."
    th "Okay, if Lena happens to be in the newsroom alone, I'll prudently leave her alone and crawl into a far corner with a book. We're both tactful people, so we won't inconvenience each other."
    play sound sfx_close_door_campus_1
    scene cg d2_micu_lib with dissolve
    play ambience ambience_library_day fadein 2
    "The grumpy librarian was snoozing quietly at her desk. With a fleeting mimicry of her face, I opened the door of the newsroom."
    scene bg int_library_day with dissolve
    th "No-bo-dy."
    th "They're all being fed around here for nothing? What about your debt to the Party?"
    dreamgirl "When do you plan to pay yours back?"
    if herc:
        th "As soon as I find out who and what I owe for this whole circus!"
    elif loki:
        th "And I don't remember owing anyone!"
    else:
        th "There you go again..."
    "Whatever my colleagues were doing now, they clearly weren't going to come to the newsroom. And that meant that I had the unique opportunity to spend two hours with Buzzer under one roof."
    dreamgirl "And for free, too!"
    stop ambience fadeout 1
    scene bg int_editorial_day_7dl with dissolve
    play sound sfx_close_door_1
    "As I slipped into the newsroom, I shut the door quietly behind me and looked around cautiously."
    th "So now I have access to all the secret material collected during this shift! What are the authorities hiding from us?"
    "There was exactly nothing of interest in the room. There were scraps of paper in the cardboard box that served as a trash can, brushes drying on the windowsill, and a rolled-up piece of cotton in the corner."
    "The place had obviously been cleaned before I got here, for I found not even a hint of any written notes. Not that I was that interested in what cyberneticists were writing their papers about, but my bored brain demanded at least some nourishment."
    th "An independent experiment found that modern man, deprived of access to news feeds and other information garbage, goes into withdrawal on the fourth day."
    th "I wish I had a couple of threads intravenously right now..."
    th "Though what the hell, I'm up for Pikabu too!"
    dreamgirl "How low the Russian nobility has fallen..."
    "Walking another lap around the editorial office, I stopped at the shelves with books."
    th "Well, what have we here?"
    th "Handbooks on writing party texts? A copy of textbooks from the journalism department of the local pedagogical institute? A bunch of erotic novels?"
    "But on the shelves, apparently, were books from the main section of the library that had lost their presentable appearance."
    th "Boring..."
    stop music fadeout 6
    if alt_day4_me_neu_date == 'un':
        th "If Lena were here, I'm sure I'd have figured out how to get close to discussing that weird scene this morning. And without the motivation of her sullen face, I don't even want to try."
    elif alt_day3_un_fz_neu_transit:
        th "Although there is some suspicion that if I had caught Lena here - there would have been no stone left unturned from the library!"
        dreamgirl "I bet that would have been exciting!"
    else:
        th "If at least Lena were here, this place would be a lot less depressing."
        dreamgirl "Do you think dullness multiplied by dullness gives fun?"
    play music music_7dl["take_my_hand"] fadein 6
    th "Speaking of Lena: isn't that her album?"
    "I grabbed the puffy album off the shelf, looking back at the door to the reading room just in case."
    th "I guess it's not nice to look at other people's drawings without asking..."
    th "But the album is in the common area, so whoever wants it can look at it. And anyway, how do I know it's Lena's?"
    dreamgirl "But you do know that."
    th "I'm just making an assumption. And now we're going to test that assumption!"
    play sound sfx_open_journal
    "Sitting on the windowsill next to my dried brushes, I opened the album carefully, as if trying not to leave fingerprints at the scene."
    th "Every creator puts a piece of his soul into his work. But a young creator can inadvertently leave his whole self on the page."
    th "What do I even know about Lena?"
    if (alt_day4_me_neu_date == 'un') or (alt_day2_date == 'un'):
        th "Much more than I'm entitled to. Much less than I would like to."
    else:
        th "Yeah, pretty much nothing."
    "Everything in this place smelled of book dust and, just a little, of herbarium forgotten between the pages of old books. But each page took me to more and more corners of the camp, filled with its own smells, sounds, colors."
    "Filled with life and someone's happy childhood, which very soon will remain only on wrinkled watercolor sheets."
    $ set_mode_nvl()
    play sound sfx_7dl["page_turning"]
    scene bg ext_playground_sunset_7dl with fade
    "A sports field where sketchy figures are frozen in their sketchy game of ball. But if you know who that red T-shirt belongs to, the figure slowly fleshes out, takes on volume and comes to life, and the cheeky face draws itself a snide grin."
    play sound sfx_7dl["page_turning"]
    nvl clear
    scene bg ext_beach_day with fade
    "The beach and the serene blue sky, beneath which ripple the colorful patches of towels on the golden sand. And two golden braids that at once remind me of the care of one stranger who somehow cares about the frowning newcomer."
    play sound sfx_7dl["page_turning"]
    nvl clear
    scene bg ext_musclub_day with fade
    "The music club veranda, light and airy, just like the figure that froze in a perpetual dance on its steps. And if you squinted hard, you'd think she'd fly off the steps and run straight to you to share all the nonsense that's going on in her head."
    play sound sfx_7dl["page_turning"]
    nvl clear
    scene bg ext_square_sunset with fade
    "A square in the morning sun, where bright colored specks are doing their exercises. There's only one orange speck standing to the side, and if you stare at it long enough, it's bound to show you its tongue and make an angry face."
    $ set_mode_adv()
    scene bg int_editorial_day_7dl with dissolve
    "Pencil, watercolor, pastel. If properly mastered, these tools can tell a story far better than the most tricked-out movie camera."
    "And Lena knew them well enough to make me want to be part of the story left behind by an ever-sad girl in a shabby, forgotten album."
    play sound sfx_7dl["page_turning"]
    "As I turned the next page, I shuddered." with vpunch
    th "Self-portrait?"
    "No, the girl on the scrapbook looked like Lena only at first glance. She had completely different eyes, a different hairdo, and even the touching harelip had nothing to do with our young artist."
    if alt_day4_me_neu_date == 'mi':
        th "That's right! She was the one in the drawing Miku took from me!"
    th "But who is she, and why does she look so much like Le..."
    play sound sfx_fall_wood_floor
    with vpunch
    play music music_7dl["yume_akari"] fadein 3
    "A rumble in the next room made me jump. I tossed the album aside fearfully, glancing apprehensively at the door."
    mz "For crying out loud!"
    th "Someone decided to blow up the library?"
    th "Given the local security system, no wonder he succeeded!"
    "Facing an enraged Buzzkill was not smiling at all, but curiosity once again proved stronger than I was. I cautiously looked out from behind the newsroom door."
    scene bg int_library_day
    show mz bukal glasses pioneer with dissolve
    mz "How many times have I asked the carpenter to fix it..."
    "The librarian was squatting beside a mountain of piled books, and her spirits were obviously not good. I cleared my throat quietly."
    show mz rage glasses pioneer with dissolve
    mz "What are you doing here?"
    th "The calamity didn't get to sleep long at her workplace..."
    me "I'm here, actually... They sent me to the club on a voluntary basis, and there's nobody here."
    show mz angry glasses pioneer with dissolve
    mz "Then you should help instead of standing like a pole!"
    if not herc:
        th "No, you grumpy bugbear, you either ask nicely, or deal with your own problems!"
        "Thought I, before obediently approaching the grumpy girl, cautiously pressing my head into my shoulders."
    else:
        "I walked up to the angry girl in three steps."
    me "What happened here?"
    show mz bukal glasses pioneer with dissolve
    mz "Shelf."
    "She nodded at the sagging board."
    mz "It doesn't hold up on the right side. I usually prop it up with the Soviet Encyclopedia from below, but recently some smart guy had the urge to read it!"
    th "If I had been given three tries to guess the smart guy's name, two of them would have gone unused."
    mz "She somehow lasted a couple of days without it, but lo and behold, she collapsed again."
    dreamgirl "Gravity:shelf - 1:0!"
    me "Is there anything similar to an encyclopedia in size?"
    mz "If there was, I'd have had it propped up the first day yet."
    me "Then maybe some books to put on the row of books below?"
    show mz angry glasses pioneer with dissolve
    "The buzzkill flashed her eyes in my direction, but, to my great surprise, she didn't yell."
    th "What happened to 'you think you're the smartest one here?' and all that?"
    th "Hasn't she really figured it out?"
    mz "Hold the shelf."
    "With a heavy sigh, I lifted the corner of the board. Zhenya began to construct a support of books."
    me "You're an interesting girl, Evgeniya."
    show mz rage glasses pioneer with dissolve
    "The librarian erupted, almost dropping another book on the floor."
    mz "What kind of silly innuendo is that?"
    me "You don't know the word 'please' or 'thank you.' Are you and Dvachevskaya related, by any chance?"
    show mz shy_angry pioneer glasses with dissolve
    "With a contemptuous snort, Zhenya continued to stack books on the newly installed shelf. But it was obvious from the fleeting expression on her face that I had succeeded in embarrassing her."
    th "She certainly doesn't have everyone at home."
    th "Well, the whole camp suffers from it to one degree or another. But even Alisa, a bully, isn't much friendlier than this beetle!"
    hide mz
    with fade2
    "In four hands we quickly put the fallen books back in place. Zhenya still didn't utter a word."
    th "And what is one supposed to say after such awkward scenes? Did you do a good job? Always happy to help?"
    dreamgirl "What are your plans for tonight?"
    th "No, that's just the sort of thing you definitely shouldn't say to such a stroppy lady if you care about your..."
    play sound sfx_7dl["eat_horn"] fadein 1
    "A horn was heard from outside."
    show mz bukal glasses pioneer with dissolve
    mz "Lunch time."
    hide mz with moveoutleft
    "She drove off so fast, I didn't have time to say a word."
    th "Though I didn't feel like it..."
    $ alt_day4_me_neu_mz_newspaper = True
    stop ambience fadeout 6
    stop music fadeout 6
    return

label alt_day4_me_neu_curl:
    play music music_list["into_the_unknown"] fadein 3
    scene bg ext_house_of_mt_day
    with dissolve
    "Almost home already."
    "The bike was just standing there, unneeded."
    "So I saddled up in a flash."
    "It was surprisingly easy to regain my half-forgotten riding skills."
    dreamgirl "Well... You're no Bob Petrella, of course, but that's the kind of thing you should have remembered."
    th "Bob what?"
    dreamgirl "Spin the pedals..."
    "..."
    "It did get a little skidgy on the turns, though."
    scene bg ext_houses_day with fade
    play ambience ambience_camp_center_day fadein 5
    "And had to turn sharply into the bushes when the squad leader came out from the side of the canteen into the square."
    play sound sfx_hiding_in_bush
    "That was close."
    if alt_day2_us_escape:
        show us laugh2 sport
        pause(0.25)
        hide us
        th "Of course..."
    dreamgirl "Full steam ahead!"
    "Just in case."
    "In case Olga wants to take a walk."
    scene
    $ renpy.show("bg ext_admins_day_7dl", what = Noon("bg ext_admins_day_7dl"))
    with dissolve
    "I made a detour through the administration building, through the showers."
    scene bg ext_musclub_day
    with dissolve
    "Sneaked through the path to the music club."
    scene bg ext_clubs_day
    with dissolve
    "And - down the slope, toward the building of the clubs, where the cyberneticists didn't seem to toil for a day."
    scene bg ext_camp_entrance_day
    with dissolve
    play ambience ambience_camp_entrance_day fadein 3
    "To the exit of the damn camp."
    "There was no one at the gate, as usual."
    "Then no one will be able to stop me."
    scene bg ext_road_day
    with dissolve2
    play ambience ambience_ext_road_day fadein 3
    "The pedals spun easily, and I picked up a decent amount of speed."
    show ftl_anim
    with Shake((0, 0, 0, 0), 3.0, dist=10)
    "The wind was blowing in my face, the sun was shining sideways."
    with Shake((0, 0, 0, 0), 3.0, dist=10)
    "The mood was great - the kind of mood a fugitive needs."
    with Shake((0, 0, 0, 0), 3.0, dist=10)
    hide ftl_anim with dspr
    show blinking
    "For some reason, though, I feel like..."
    "I yawned."
    show blink
    $ alt_pause(2)
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day4_me_neu_day_us:
    $ counter_us_7dl += 1
    scene black with dissolve
    play music music_list["tried_to_bring_it_back"] fadein 7
    play sound sfx_open_dooor_campus_2
    $ alt_pause(1)
    play ambience ambience_int_cabin_day fadein 2
    play sound sfx_face_slap
    with hpunch
    "Today is what we will call the great day of beating."
    "How much more can you do that!!!"
    "I was brought to my senses by a tangible slap on the cheek." with hpunch
    "After shaking my head, I came to my senses a little."
    scene bg int_house_of_dv_day
    show us dontlike sport
    show unblink
    "I was lying on the bed and Ulyana was sitting next to me."
    "Very, very annoyed!"
    if alt_day2_us_escape:
        us "So that's what your plan was?"
        "She flicked my forehead."
    me "Where...am I?"
    us "At my house."
    "She answered."
    me "And how did I..."
    show us angry sport with dspr
    us "How-how. With your feet."
    us "You came, said something like «{b}kid{/b}, get lost» and fell."
    me "Gee..."
    "I rubbed my bruised forehead."
    me "Did I really say that? {w}Doesn't sound like me."
    me "Is that why you're so angry?"
    play sound sfx_face_slap
    with hpunch
    show us cry2 sport with dspr
    us "No, not because of that!"
    "Ulyana screamed."
    "She hit me again."
    play sound sfx_face_slap
    with hpunch
    me "Sto…"
    play sound sfx_face_slap
    with hpunch
    "And again!"
    me "Stop hitting me!!!"
    play sound sfx_face_slap
    with hpunch
    "I intercepted her hand."
    me "What happened?"
    show us dontlike sport with dspr
    us "Nothing! You didn't call me!"
    "She stomped her foot angrily."
    me "How do you imagine that? {w}Was I supposed to announce on the radio?"
    us "I don't know. You were supposed to!"
    us "We had to run away together! {w} Get out, you bastard!"
    "She started pushing me out of the cabin."
    us "Get out, you cheating bastard!"
    "And when I tried to resist, she kicked me in the shin good and proper."
    dreamgirl "Why don't we beat her up?"
    th "Right, and we'll be guilty of manslaughter."
    th "No, I'm out of here."
    "After dodging another push, I jumped out into the street."
    play sound sfx_open_door_kick
    scene bg ext_house_of_dv_day
    with dissolve
    play ambience ambience_camp_center_day fadein 3
    "It wasn't until I ran a very decent distance that I discovered something was missing."
    play music music_7dl["genki"] fadein 3
    "The phone."
    "I definitely remember it was in my pocket, and the only way it could have fallen out was..."
    "Shit."
    "But it's probably not safe to go back in now, is it?"
    "Like I have many options."
    "I'll have to take my chances!"
    play sound sfx_knock_door2
    "I knocked."
    me "Ulyana, hello? {w}I'm coming in."
    "She didn't answer, apparently she was busy with something."
    "Or sulking. For my wicked betrayal."
    "It'll be funny if she's waiting for me to apologize."
    stop ambience fadeout 2
    play sound sfx_open_dooor_campus_2
    $ alt_pause(1)
    scene bg int_house_of_dv_day
    with dissolve
    play ambience ambience_int_cabin_day fadein 2
    "Without waiting for an answer, I opened the door."
    us "Wait... {w}Not now! {w}You jerk!"
    "It's too late."
    show us angry swim with dissolve
    us "I told you to wait!"
    "I looked around."
    "And I found the phone lying on the nightstand with the screen down."
    "Apparently, Ulyana was thinking of playing with it later."
    "After quickly checking the charge level, I breathed on the glass and wiped the phone on the fabric of my shirt on my stomach."
    me "It's great they didn't put legs on the phone."
    me "You're too young to have toys like that."
    "I hid it in my pocket."
    show us shy2 swim with dspr
    "Unlike Ulyana, who for some unknown reason blushed and pressed her hands to her chest, I felt calm and confident."
    "And the little one seemed to be getting ready to fall through the ground."
    me "That's it!"
    show us shy swim with dspr
    us "Hey!"
    us "Don't you want to do anything?"
    "Do?"
    "Her body language told me that she wanted to hit me again."
    "So I took a polite step back."
    me "I don't want to. {w}You've already beaten me enough."
    "What the hell else does she want from me? {w}You can't punish twice for one thing!"
    show us angry swim with dspr
    us "I SAID, AREN'T YOU GOING TO APOLOGIZE, ASSHOLE?!" with hpunch
    "She yelled."
    me "For what?"
    "From my genuine surprise, Ulyana froze, and then slowly and slowly crumpled the top of her swimsuit in her fist."
    us "Are you stupid? Can't you see a girl is changing?!"
    us "Or were you born in a cave?!"
    "Now I see why she got so worked up."
    "But «the girl»…"
    "I looked her over carefully."
    "Her face looked like a bumpkin, and in her forehead the burning star of several strands of scarlet hair only emphasized it."
    "The attractiveness of the level of..."
    dreamgirl "The ground."
    me "A girl? Dressing up?!"
    show us fear swim with dspr
    us "You... You... You... What are you looking at?!"
    me "I'm looking for a girl."
    us "What?"
    me "The one who's changing. {w}You hid her?"
    me "Alisa, huh?"
    "I looked closely at Ulyana."
    th "About the sex features - well, I'll obviously have bigger breasts."
    th "So there must be another girl here."
    me "Or are you talking about yourself?"
    "I cocked my head and burst into the most retarded laugh I could."
    dreamgirl "Okay. I think this is the point."
    th "Yes."
    th "That's the one."
    show us cry2 swim with dspr
    play sound sfx_angry_ulyana
    "The fourth degree of humiliation."
    us "I'LL KILLLLLL YOUUUUUUU!" with vpunch
    "The room was slowly filled with steam."
    "Coming from Ulyana's ears."
    with flash_red
    "Something heavy flew at my head."
    stop music fadeout 3
    stop ambience
    scene bg ext_house_of_dv_day with pushleft
    play sound sfx_close_cabinet
    $ alt_day2_dv_us_house_visited = True
    "Laughing, I flew out of the cabin and slammed the door behind me."
    return

label alt_day4_me_neu_day_mt:
    scene bg ext_sky_7dl
    show unblink
    play music music_list["smooth_machine"] fadein 5
    "I woke up lying in the grass for some reason."
    "Looking up at the sky for some reason."
    "Though a few seconds ago I was trying..."
    "Tried to..."
    mt "You owe me a new bike."
    "Politely informed me the squad leader."
    "With a grunt, I scraped myself off the ground."
    me "A bicycle?"
    mt "Yes, in return..."
    "She nodded at the eight-shaped object lying nearby, in which with a little imagination one could make out the frame, the pedals, the wheels..."
    mt "Will you buy a new one, or..."
    "She took a pause."
    "And I, finding myself in this situation, was confused."
    "In my old life I had successfully managed to maneuver between all sorts of loans and mortgages."
    "Somehow, in spite of the fact that everyone around me was in debt like silk, either gangster or loan debt, I managed to live within my means."
    "And to 'get' into money all at once was pretty unexpected."
    me "What do you mean?"
    scene bg ext_adductius_7dl
    show mt grin pioneer
    with dissolve
    "Olga sat next to me on the curb."
    mt "There are plenty of ways to pay off debts."
    mt "Like..."
    me "Uh... Work it off?"
    show mt smile pioneer with dspr
    mt "Well, there you go."
    "She got even closer."
    mt "You know how it is. {w}Relax, why are you getting so tense."
    "She laughed."
    mt "I'm not going to ask anything supernatural of you."
    mt "But you know, a bike is a pretty useful thing."
    show mt smile pioneer close with dspr
    "And she sat down so that our shoulders were almost touching."
    "Beautiful, mature, and in every sense correct, Olga Dmitrievna was doing something incomprehensible."
    show mt sad pioneer close with dspr
    mt "There you go again."
    "She's upset."
    mt "And you're thinking in the wrong direction again."
    me "Excuse me?"
    show mt smile pioneer close with dspr
    mt "Nothing."
    scene bg ext_camp_entrance_day
    show mt normal pioneer
    with flash
    "Olga stood up and held out her hand to me."
    show mt normal pioneer close with dspr
    "And when I took advantage of her help, she was very close for a split second."
    mt "That's right, you work it off, and we're even."
    me "So what do I do?"
    "For some reason, obscene pictures kept popping into my head."
    show mt smile pioneer close with dspr
    mt "It's kind of nice that you've set yourself up, I won't have to talk you into it now."
    me "What are you talking about?"
    "I was beginning to lose patience."
    show mt laugh pioneer close with dspr
    mt "Relax, I won't make you dig potatoes."
    mt "But I need an assistant for the third shift."
    "I got a little tingle in my chest."
    me "So I'm not going with the pioneers?"
    show mt normal pioneer with dspr
    mt "No, you will."
    mt "And tell your parents that you want to be a squad leader's aide more than life."
    mt "Or you don't have to go, you can just buy me a new bike."
    th "It's weird that nothing hurts."
    "Judging by the condition of the bike, I've had an adult accident."
    me "Ahem... What about Slavya?"
    show mt smile pioneer with dspr
    mt "What a touching concern. {w}But two assistants are better than one, right?"
    "I know that type of person."
    "They always keep you in a state of misfit, and you don't even think about running away or turning on disobedience."
    "The only countermeasure is absolute nihilism."
    "Unfortunately, not really my repertoire. {w}Nobody would believe that I could give a damn to that extent."
    mt "You'll like it, I promise."
    "The squad leader interpreted the lull in the conversation in her own way."
    "And I didn't try to change her mind."
    "Anyway, there's an escape in town - if you're really desperate."
    "And I nodded in agreement."
    me "Good. You can sign me up."
    mt "Excellent. {w}But if anything, shh."
    "She pressed her finger to her lips."
    mt "You volunteered as a test subject... {w}Volunteered."
    "Somehow that was important to her."
    "And I nodded again - for some reason the possibility of feeling like an accessory to some leader's plans tickled my nerves nicely."
    "I even turned up my nose a little - not because we're spies or anything, but because a grown-up, proper girl would trust something to a goofball like me."
    mt "And now..."
    show mt grin pioneer with dspr
    "Her voice lowered, and there was a velvety tone to it."
    "And I got goosebumps swirling down my spine."
    me "Yeah?"
    show mt grin pioneer close with dspr
    "She came closer to me and smiled carnivorously."
    mt "Take the bike to the warehouse... Volunteer."
    $ alt_day4_me_neu_mt_volonteer = True
    "Shieeeeeet!"
    show mt laugh pioneer close with dspr
    hide mt with easeoutleft
    "Not listening to the mocking chuckle, I turned around and wandered toward the mangled vehicle."
    stop music fadeout 3
    return

label alt_day4_me_neu_lunch:
    if alt_day3_technoquest2 and (alt_day3_dj != 'dv'):
        scene bg int_dining_hall_people_day with dissolve
        play ambience ambience_dining_hall_full fadein 3
        "Violetta was waiting for me in the canteen."
        show cs normal with dissolve
        cs "Hello again... Pioneer. {w}How's your head?"
        "I remembered that I'm actually performing as an invalid today."
        "Surprisingly, it didn't make me uncomfortable at all."
        "I shrugged my shoulders:"
        me "Not bad, I guess."
        cs "Not bad is good."
        "Uncomprehendingly, Violetta said, and rummaging through her pockets, pulled out a key:"
        cs "I'm going home now, I have to pick something up there. Wait for me in the infirmary, will you?"
        me "And you're just going to give me the key like that?"
        cs "Why not? {w}You're not going to cause any trouble... Pioneer?"
        show cs smile with dspr
        "Her smile was very, very, very affectionate."
        me "Uh... No."
        "I swallowed."
        cs "Then wait for me in the infirmary, we'll see how you're doing."
        hide cs with dissolve
        "After giving me a wink goodbye, the nurse teleported away."
        stop ambience fadeout 2
        scene bg ext_aidpost_day with dissolve
        play music music_list["my_daily_life"] fadein 5
        "There was nothing to do, so I had to do what she said."
        "Besides, the board would be very unhappy if they knew the medical station was closed for no good reason."
        th "Oh, what was that now? {w} Did the local Kashpirovsky open another responsibility chakra in me?"
        "Apparently, the water in the decanter wasn't easy."
        play sound sfx_open_door_clubs
        scene bg int_aidpost_day
        with dissolve
        "I grinned, unlocked the door, and threw my white robe over my shoulders and made a smart face."
        "For the first five minutes I puffed up, puffed up my cheeks, and acted like an important bird."
        "Tired of it."
        "I found an '80s fashion magazine on my desk, and out of curiosity, I tried to flip through it."
        "But these color combinations... {w}I could literally feel my brain cells committing suicide one by one as I read this nonsense."
        with fade
        th "It seems that even in the local active reality, I manage to remain a sideline cheerleader."
        "I summed up dejectedly and went out on the porch from nothing to do."
        play sound sfx_open_door_1
        $ alt_pause(1)
        scene bg ext_aidpost_day with dissolve
        "There were pioneers, Octobrists, parents in pioneer uniforms rushing somewhere..."
        "I wish I could learn a little independence. {w}At least not to wait for valuable instructions in order to occupy myself with something."
        "A talent I am deprived of."
        th "What's that noise?"
        "From somewhere on the right, from the 'hill,' came the distinctive bass rumbles."
        dreamgirl "There's a concert the kids are putting on for their parents."
        dreamgirl "And Viola's watching them."
        "That means it's a very long time before she 'picks up something important at home' and comes to relieve me of my unintentional duty."
        dreamgirl "Sometimes I think Olga and Viola went to the same pedagogical school."
        dreamgirl "At any rate, they are equally virtuoso at puzzling pioneers!"
        play sound sfx_open_door_clubs
        $ alt_pause(1)
        scene bg int_aidpost_day_apple with dissolve
        th "It's not hard for me."
        dreamgirl "Yeah. {w} But if you paid a little more attention to some girl..."
        th "You sound like you have a vested interest in that!"
        "The answer to me was a quiet laugh."
        dreamgirl "Actually, there is some interest."
        stop music fadeout 3
        dreamgirl "By the way, want an apple?"
        th "What?"
        play music music_list["mystery_girl_v2"] fadein 3
        "And then I noticed that something in the infirmary had changed!"
        "A big, beautiful green apple appeared on the table out of nowhere."
        th "Where did it come from?"
        "It's hard, it's green, it smells like an apple."
        "I rubbed the fruit on my sleeve."
        "It tastes..."
        play sound sfx_7dl["apple_bite"]
        "Like an apple!"
        scene bg int_aidpost_day with dissolve
        dreamgirl "And you ate it so easily. {w} What if it's poisoned?!"
        th "Nah, I wiped it off."
        dreamgirl "You can't get rid of poison just by wiping it on your sleeve!"
        th "So it was poisoned?"
        "I have all available sorbents and antidotes at my disposal. {w}It was delicious, by the way."
        dreamgirl "You've gotten too careless!"
        if lp_us >= 9:
            dreamgirl "It sounds like you're the one who's being corrupted by the little one."
            th "HANDS OFF THE LITTLE ONE, ON THE TABLE, WHERE I CAN SEE THEM!"
            th "And before you start throwing around incomprehensible words like 'lolicon,' I hasten to remind you that she's the only one who's even said hello to me since this morning!"
        dreamgirl "Or maybe it's enchanted, and now you'll sleep for three hundred years until you're kissed by a mustachioed prince."
        th "Was it poisoned or not?"
        dreamgirl "...{w=0.5}No."
        dreamgirl "This was supposed to be a joke like the choice from 'The Matrix' - an apple and a Wunderland in one palm."
        th "And on the other..."
        dreamgirl "Well, look on the table."
        "On the lonely vial, in contrasting, easy-to-read font, it said 'Xanax.'"
        dreamgirl "You wake up in your bed and, coping with a hangover, believe what you want to believe."
        "The longer I communicated with my inner voice, the more I doubted that it was even {i}my{/i} voice."
        th "A porn movie plot, man - I have to find myself a girl and do something obscene with her, otherwise this world is doomed, right?"
        dreamgirl "Something like that."
        dreamgirl "Actually, the over-all purpose of this place was to make you - us - a little bit better. {w}Motivate."
        stop music fadeout 3
        th "You screwed up."
        dreamgirl "We screwed up."
        with flash_red
        me "Ow!"
        "The hairs on the back of my neck hurt."
        show cs normal with dspr
        cs "Healing is going well."
        "She took some kind of tube out of her pocket and squeezed some yellow paste onto her finger."
        me "Violetta Cernovna!"
        "It seems that while I was 'hovering,' chatting to myself, she managed to get close."
        cs "Viola... Pioneer. {w}I don't want to feel like a grandmother, I'm not even forty."
        me "Really?! I thought you weren't even thirty."
        show cs shy with dspr
        cs "Now that's just rude flattery. {w}Tilt your head."
        "I think I pinched my scalp a little when I flopped - where the ointment touched my skin, I felt a pretty bad burning sensation."
        cs "You get the pills from the squad leader, take them for two more days, I won't keep you in the infirmary - not good for the face of the camp."
        "With the filigree precision of great experience, she sliced a few pieces from a roll of band-aid and, having constructed a kind of mold from gauze, absorbent cotton, and these same pieces, placed it on the back of my head."
        cs "Refrain from sudden movements, physical exertion and bending over for at least a couple of days."
        cs "And give me the robe."
        me "So is the concert over yet?"
        "I inquired, taking off the robe and returning it to the rack."
        cs "Not quite. It hasn't even started yet."
        me "I see. Well, can I go now?"
        show cs normal with dspr
        cs "Yes. {w}You can go."
        "I turned to leave."
        cs "Yes, by the way, pioneer."
        "She called out when I got as far as the door."
        me "Yes, Viola?"
        cs "Did you see if I left an apple in here somewhere?"
        with flash_red
        "I blushed."
        me "N-no! {w}You must have left it at home!"
        play sound sfx_open_door_kick
        $ alt_pause(1)
        scene bg ext_aidpost_day with dissolve
        "And accompanied by the laughter of an inner voice, flew out into the street."
        play ambience ambience_camp_center_day fadein 3
        play music music_list["get_to_know_me_better"] fadein 5
        scene bg ext_dining_hall_near_day
        with fade
    else:
        scene bg ext_dining_hall_near_day with joff_l
        play ambience ambience_camp_center_day fadein 3
        play music music_list["get_to_know_me_better"] fadein 5
        "In the blink of an eye, I stepped out onto the porch and hovered for a few seconds, wondering where to go."
    us "Hey, psst!"
    show us smile sport at voy_right with dspr
    "There was a painful bump in the back."
    hide us with easeoutright
    us "Rookie!"
    us "Are you deaf or something?"
    scene bg ext_dining_hall_near_day:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 0.5 zoom 1.25 xalign 0.75 yalign 0.5
    show us smile sport at right
    with dspr
    me "Are you going to call me a rookie all the time now?"
    "The joke has gone on long enough, to be honest."
    "And I didn't come here to be mocked, either."
    me "I have a name, too, you know?"
    show us surp1 sport with dspr
    us "Name?"
    if lp_us >= 9:
        "She didn't seem to sulk for the cabin scene anymore."
    me "Yes!"
    "I barked."
    show us surp2 sport with dspr
    us "No{w=.2} freaking{w=.15} way!"
    us "What is it?"
    "She asked it with such an innocent look that I just waved my hand."
    me "What did you want?"
    show us smile sport with dspr
    us "Let's play volleyball?"
    "For a split second I imagined the picture of Ulyana being shot by one particularly strong cutter, and I shook my head."
    me "I don't think that's a good idea."
    us "You're slacking off anyway!"
    me "It's none of your business. {w} Go play with Alisa."
    show us normal sport with dspr
    us "Her stomach hurts! Ah..."
    show us shy sport with dspr
    "She seems to have blabbed about something she shouldn't have."
    dreamgirl "On the other hand, it shows that the local pioneers are more or less alive after all!"
    dreamgirl "Otherwise, all the way around it feels like we're in some dollhouse where perfect people don't get sick and don't go to the bathroom."
    me "So go sit with her instead of fooling around."
    "I reasonably suggested."
    show us dontlike sport with dspr
    "Ulyanka frowned."
    us "Do I look like a suicider?"
    me "Exactly."
    show us grin sport with dspr
    us "You do it! {w}And I'll get my revenge for you later."
    "Sure! I'll..."
    "When I saw the squad leader creeping up, I hesitated and nodded."
    "This activist has enough of a conscience to put me in another social activity."
    th "After all, you can leave the game when you get bored."
    me "Okay, let's play!"
    us "Here you go."
    "She threw me a crumpled ball."
    mt "Ulyana, what are you doing here?"
    show mt normal pioneer
    show us normal sport
    with dspr
    us "Ol'dmitryvna, give the newcomer..."
    me "Semyon!"
    us "...pump, please!"
    "Ulyana continued as if I hadn't interrupted her."
    show mt angry pioneer with dspr
    "The leader frowned briefly."
    mt "Actually, I wanted you to help me supervise the children's concert."
    menu:
        "Concert? We're in!":
            show mt normal pioneer
            show us dontlike sport
            with dspr
            us "Hey! I didn't agree."
            me "You volunteered... Oldfag."
            show us calml sport with dspr
            us "There goes my game."
            "She took the ball away from me."
            us "Bi... Big, stupid bi..."
            "She mumbled."
            show mt laugh pioneer with dspr
            mt "Ulyana?"
            us "Well, what else?"
            "The little one raised her head."
            "She was still sulking a little."
            if alt_day3_duty:
                mt "Remember last day's duty?"
                us "Uh-huh, we're always on duty now."
                if alt_day2_us_escape:
                    us "We just ran away once…"
            else:
                us "I know I can't say no."
                us "But I'm not going to pretend like I like it!"
            mt "That's not what I mean."
            "Waved off the leader."
            mt "But it is in my power to reward my helpers."
            us "What are you going to reward us with? The best reward is a new job, I know you."
            me "I think I can guess."
            show mt grin pioneer with dspr
            "Olga put her finger to her lips and beckoned us behind her."
            "I unobtrusively cleared my throat."
            me "Uhh... Olga Dmitrievna."
            mt "What, Semyon?"
            me "What is there to do?"
            mt "You'll see there. Nothing complicated."
        "Let's play volleyball instead!":
            $ alt_day4_me_neu_volley = True
            $ counter_us_7dl += 1
            if 'volley' in list_clubs_7dl:
                $ counter_mt_7dl += 1
            show us dontlike sport with dspr
            pause(.3)
            show us normal sport with dspr
            "Ulyana started to argue, but she stopped herself mid-sentence..."
            "She seems to have resigned herself to the fact that we have already been put in charge, responsible and important."
            "Of course, it never occurred to her to call Olga into the game with us."
            "So my mushroom move surprised her a little."
            me "And you're with us."
            "I repeated as the silence lingered."
            mt "Semyon, haven't you heard? {w} I have a concert."
            me "Not you, but the pioneers who aren't even in your troop!"
            show mt normal pioneer with dspr
            "Olga was still in doubt."
            me "Besides, won't the rest of the administration be there?"
            show mt sad pioneer with dspr
            mt "On the other hand..."
            "She muttered to herself."
            mt "Maybe Borya will finally learn to be independent."
            me "Excuse me?"
            "I think I misheard her."
            "Someone just called the gym teacher..."
            show mt normal pioneer with dspr
            mt "Okay."
            "She nodded."
            "I think I managed to talk her down."
            mt "Where shall we play?"
            me "Hoooraay!"
            "The squad leader grimaced, and I hurriedly turned down the volume."
            me "Let's throw a little ball on the concrete, shall we?"
            mt "Deal. {w}Go change, I'll pump up the ball."
            mt "Meet me at the concrete in fifteen minutes."
            "After a handshake, Ulyana and I parted ways."
    stop music fadeout 3
    stop ambience fadeout 6
    return

label alt_day4_me_neu_concert:
    scene bg ext_stage_near_clear_7dl with dissolve
    me "Uh-huh."
    "With the exception of our ragtag squad - an age when they're already 'too old' to dress up in a captain's tunic and sing children's songs - the whole camp was already here."
    "And all this sea of excitement we must in some mythical way 'control.'"
    me "Olga Dmitrievna..."
    "Under the dagger-shot exchange of stares, I felt myself nailed to the ground."
    show mt smile pioneer with dspr
    mt "Relax, Semchik. {w}They're more afraid of you than you are of them."
    mt "Just stand about in the middle and keep an eye on them-if anyone gets sick or starts acting up..."
    me "Take them out of the hall?"
    "I guessed."
    show mt normal pioneer with dspr
    mt "No way! {w}You're not an educator, you have no right to touch children."
    me "Then why am I here?"
    "I was upset."
    mt "You must see me, Viola and Boris all the time: and if anything happens, let us know."
    mt "Ulyana, this concerns you too!"
    show us dontlike sport at left with dspr
    us "I don't want tooooo…"
    "Mumbled the girl."
    show mt laugh pioneer with dspr
    mt "Come on, run to the far side, the concert's about to start!"
    scene bg ext_stage_big_clear_day_7dl with dissolve
    play ambience ambience_camp_center_day fadein 3
    stop music fadeout 3
    "The leader was right - the music purring in the speakers faded, and Miku jumped out onto the stage."
    play music music_list["always_ready"] fadein 3
    mi "Good evening, friends!"
    "She smiled - professionally, practiced - but from the heart."
    "I caught myself smiling back at her."
    dreamgirl "Charisma!"
    "Vigorously dropped the subconscious."
    mi "Your children will be performing for you tonight, they are very excited, but they have worked very hard preparing these performance for you."
    mi "So please support them!"
    if loki:
        me "Uh-huh. And whoever claps quietly won't get to return next year."
    else:
        th "Unfortunately, the dialectic doesn't work here."
        "For some... 'artists'... the number of rehearsals doesn't solve anything."
    mi "I declare the concert 'From Children to Adults' open!"
    mi "Daniil Sumarokov, second squad, solo on metallophone."
    th "Amateur performance."
    "The way you look at an audience from the stage is always different from the way you look at an artist from the audience."
    "It's like the sound of your own voice - to you your voice always sounds at least good, but once you record it..."
    "So I now had an exclusive opportunity to appreciate what a nightmare I might have looked like as a kid."
    "Clutched at the microphone, bulging his eyes, shaking, not even dreaming of dancing."
    "And he was yelling in a wooden voice!"
    "And that's just the ones who sang!"
    "And there were those who had a bear on their ears, not just trampled on their ears, but slept over."
    "Those, on the other hand, came out to the microphone with their eyes blown off and yelled so much that the poor sound producer had to muffle the signal from the microphone by half."
    "Fortunately, there were no incidents on my 'profile' - the pioneers sat still and quiet."
    "Although I don't think it was us, with our complicated faces circling the auditorium."
    show dv normal pioneer with dspr
    if alt_day4_me_neu_date == 'dv':
        "A new actor I noted with displeasure."
        "That's whose face, or rather whose face I'd love to forget."
        dv "There you are."
        "I ignored her."
    else:
        dv "Hi."
        "Nodded Alisa, standing next to me."
        me "What are you doing here?"
        "Dvachevskaya looked a little embarrassed."
        dv "Ulyana... She disappeared somewhere."
        me "While your stomach was hurting?"
        show dv shy pioneer with dspr
        dv "What? What are you talking about?"
        me "I was told by Ulyana that you had... Mmmm!"
        "I couldn't continue as I was gagged with my palm."
        show dv angry pioneer with dspr
        dv "You should have shouted about it even louder, or the whole camp wouldn't have known yet."
        "She was covering my mouth with her left palm, and her right one was already clenched into a fist."
        "And only the fact that the entire available contingent might witness the beating cooled her ardor a little."
        me "I'm sorry, I said without thinking."
        "Alisa agreed:"
        show dv normal pioneer with dspr
        dv "Yes, you'd do well to learn to think."
        "Apparently, finding the conflict exhausted, she let me go."
        "I silently retreated a step, trying not to lose what little dignity I had left."
    dv "I'll be here on duty with you."
    dv "There's nothing to do anyway, parents all around."
    "I continued to remain silent."
    dv "So here I am. {w}Are you happy?"
    me "I'm going to cry from happiness."
    dv "Hey! What? Are you offended?"
    th "How did she know..."
    me "Are you on duty? {w}Then be on duty. You can't dawdle here."
    hide dv with dissolve
    "Pouting, Alisa went to the back rows, where she shouted loudly at the pioneers, who were clapping against the beat."
    "Then my attention was attracted by some stirring in the rows at Ulyana's side - two pioneers were arguing about something in high tones."
    "The blond one, the smaller one, had tears in his eyes. He grabbed his opponent by the chest, looking on with mocking sympathy."
    "Actually, this sort of thing should be handled by Boris Alexandrovich!"
    "And where is the fat man now, when he is so needed?"
    "I looked around confusedly."
    "Violetta was sitting next to some girl, holding that one by the wrist, apparently counting her pulse."
    "The gym teacher was nowhere to be seen at all. How did that big carcass manage to get lost in the crowd?"
    "Ulyana looked at me confused."
    "I looked around for the squad leader."
    "Olga Dmitrievna was telling off some pioneer."
    "Sensing my gaze, she nodded at the arguing, suggesting that I try to resolve the situation myself."
    menu:
        "Interfere":
            $ counter_mt_7dl += 1
            if herc:
                "I crunched my knuckles."
                dreamgirl "Ho-ho! Are you going to smack the kids?"
                th "No, but I'll slap them if I have to."
                dreamgirl "Ai-yi-yi-yi! The squad leader will scold you!"
                "I grinned."
                th "She approved!"
            else:
                th "Well, if the bosses have given the go-ahead..."
            "Both participants in the skirmish were half a head taller than Ulyana and heavier anyway."
            "After thinking for a while, I rounded the benches and approached Ulyana."
            stop music fadeout 3
            if loki or herc:
                show us upset sport with dspr
                us "I told you nothing good would come of it."
                "She grimaced."
                play music music_7dl["areyouabully"] fadein 3
                me "It's okay, go find the PE teacher, wherever he's climbing."
                us "What about these?"
                me "I'll deal with them."
                show us smile sport with dspr
                us "Thank you!"
                hide us with easeoutleft
                "She instantly drifted away."
                show al angry pioneer at cright with dissolve
                "And I got close to the arguers and, remembering my school days, barked:"
                show al dontlike pioneer at cright with dspr
                me "OPPA!" with vpunch
                $ meet('al',"Kid")
                "The brawlers froze in surprise, breathing heavily, looking at each other with anger, with hatred."
                al "What about him!"
                "Shouted the younger boy."
                "The other only grinned."
                me "Why don't we step aside and try to figure out what's going on?"
                me "Where are your parents?"
                show al angry pioneer with dspr
                ml2 "He doesn't have any!"
                "Mockingly stretched out the other one."
                ml2 "He's from an orphanage!"
                "I unclenched my fist with an effort. {w}Beating the little freak won't solve the problem."
                me "Let's go, I said."
                "However, the pioneer didn't look scared or at all alarmed."
                ml2 "Do you even know who my mother is?"
                "With a poorly concealed sense of grandeur, he muttered."
                me "I don't give a single shit."
                hide al with dissolve
                "I grabbed his arm and dragged him away from the benches."
                voice "Where are you taking my son, kid?"
                "I looked back - some strange woman was already rushing toward us."
                "Fat, unpleasant, and subtly similar to her gimlet."
                $ meet('voice',"Mommy")
                me "Are you his mother?"
                "I asked."
                voice "Yeah, why?"
                me "Why didn't you stop your son when he was bullying a comrade?"
                voice "Let Antosha play, childhood comes only once."
                "Chemically she stretched out."
                voice "And besides... That loner won't complain to anyone. He ain't got nobody."
                "Brrr. I thought I'd moved on from that!"
                me "And when did orphans stop being human?"
                "Quietly I asked, unknowingly squeezing the gopher's shoulder with my fingers."
                voice "I pay taxes so they have something to eat in their brothels. {w} Are you done? We're going to see a concert."
                "Dressed. {w}Fed. {w}Spitting on others."
                "I really wanted to bang their heads together."
                me "Almost. I need a last name to write a report to my supervisor about the fight."
                me "You know, violation of the rules, we need to properly process the early closure of your son's voucher."
                voice "What kind of fight, it's just Antosha..."
                "Apparently, there was the same smug expression on the little shit's face."
                show al angry pioneer
                with flash
                play sound sfx_lena_hits_alisa
                $ alt_pause(1)
                with vpunch
                "Because the second kid couldn't take it - took a short swing and punched, almost poking the offender in the nose."
                al "You can throw me out then, too!"
                "And ran away."
                "That one whimpered instantly, and, breaking free, ran up to his mother, and ducked into her."
                hide al with dissolve
                stop music fadeout 3
                "Olga Dmitrievna ran up and asked me something, but I couldn't hear anything."
                "I was pounding with anger."
                $ meet('voice',"Voice")
                with fade
            else:
                play music music_list["doomed_to_be_defeated"] fadein 0
                show us normal sport with dspr
                us "What shall we do?"
                me "Distract Olga Dmitrievna, let her take care of what's more important."
                us "But we can't!"
                me "But we have to. {w}The gym teacher is nowhere to be found."
                show us normal sport with dspr
                us "Fine."
                hide us with dissolve
                "The little one shook her head doubtfully, but obeyed."
                "And I, pushing my way toward the fight, intercepted the moving hand and yanked it lightly toward me."
                me "Let's step back and talk."
                "Without listening to objection, I dragged the brawler behind me."
                me "What are you waiting for? Follow me."
                "I threw over my shoulder."
                "Olga was already waiting for us - and handing both boozers to her, I took a breath."
                "There, however, the drama was just picking up steam."
                "Olga reprimanded both of them for a while."
                "After which some unpleasant, overweight woman approached her."
                "Apparently a mother."
                "With a look of the highest favor, the 'august person' turned to the leader."
                "Honestly, if I'd been treated with such contempt - I wouldn't have stood for it."
                "But the squad leader was no slouch either."
                "Soon after letting one pioneer go, she turned around so that she was facing a woman and a boy."
                "And began to say something."
                "And as the squad leader spoke, the identical sallow fish faces grew pale and pale."
                "Because of the concert, I could only make out scraps."
                mt "Forgery... Hatsune... ambassador... forget both love and money..."
                mt "...non-exempt. Do we understand each other?"
                "Unexpectedly clear, she asked."
                stop music fadeout 3
                "And at the synchronized convulsive nod, she laughed nonchalantly:"
                mt "That's great! {w}Have fun, it's a holiday!"
            "The whole time Alisa just stood there looking at us, not trying to interfere."
        "Ask Alisa for help":
            "I quickly, quickly walked over to Alisa and said in a low voice,"
            me "If you want to help, now's the time."
            "And after thinking about it, I added:"
            me "Just don't you dare press the pioneers or get your hands dirty."
            me "We're here to keep order."
            me "Don't confuse us with the punishment squad."
            show dv normal pioneer with dspr
            dv "Or what?"
            me "Or else I'll tell Olga Dmitrievna that you're sabotaging the concert."
            dv "Go ahead. {w}Snitch."
            me "I warned you."
            hide dv with dissolve
            "I returned back to my position."
    with fade
    play music music_list["she_is_kind"] fadein 3
    dreamgirl "What a bastard she is."
    if alt_day4_me_neu_date == 'dv':
        th "I didn't think she had the nerve to come up to me."
        dreamgirl "After that setup?"
        dreamgirl "Apparently, that's all right for her."
    th "That's not my problem."
    th "Her difficult childhood and adolescence don't bother me."
    dreamgirl "Yeah, you have the universal weapon of cheap escapism."
    th "Are you against me now, too?"
    "The inner voice grinned."
    dreamgirl "Schizophrenia sucks. {w}The sad holiday that's always with you."
    th "Implying that if I weren't so stubborn with my principles..."
    dreamgirl "Not implying. I'm speaking plainly."
    me "And if I don't like her?"
    "I grumbled."
    show us smile sport with dspr
    us "Then don't get married!"
    "Poked me from somewhere on the side."
    "And I felt the corners of my lips begin to part against my will."
    "Ulyana had the most positive effect on me."
    "And why isn't she about five years older!"
    play sound sfx_7dl["eat_horn"] fadein 1
    show us normal sport with dspr
    us "No."
    "The redhead answered."
    me "What?"
    us "I say no."
    us "I'm not going out with you."
    me "Aaah!"
    with flash_red
    me "What are you talking about!"
    me "What makes you think that?"
    show us laugh sport with dspr
    us "Because I don't want to go out with you!"
    me "No, I... Oh, man."
    "I just waved my hand."
    "She got me."
    me "Let's go to supper, little girl."
    "Pioneers, in orderly groups, were heading for the canteen."
    stop music fadeout 3
    stop sound fadeout 3
    stop ambience fadeout 6
    return

label alt_day4_me_neu_volley:
    scene bg ext_houses_day with dissolve
    "I was the first to arrive at the place, since I had nothing to change into."
    "As a matter of fact, I went straight here after we were assigned a rendezvous."
    "Ulyanka came after me next, and after sitting around for a while, she got bored."
    "After thinking for a while, she decided to amuse herself in the only way available - by tossing cones with my back."
    "Thump!" with vpunch
    "There's a painful thump in the back."
    "Thump!" with hpunch
    me "Hey, what are you doing?"
    us "What-what, throwing cones at you, didn't you notice?"
    us "You're a retard!"
    me "Stop it!"
    "Thump!" with vpunch
    "My patience... has burst!"
    show ftl_anim with vpunch
    "I bent down and, picking up all the cones that had fallen next to me, launched back into the small one."
    hide ftl_anim
    "She screeched and hurried to hide behind a thicker pine tree."
    "But you can't fool me - her 'rockets' completely de-masked the redhead, so, trying to tread silently, I moved to bypass my opponent's position."
    "And..."
    show mt normal sport at zenterright with dissolve
    mt "Having fun?"
    "Thump!" with vpunch
    "The last cone flew into my forehead!"
    show mt normal sport at fright with moveinright
    show us grin sport with dissolve
    us "I won!"
    play ambience ambience_7dl["volley"] fadein 2
    play music music_list["went_fishing_caught_a_girl"] fadein 2
    show mt smile sport with dspr
    mt "Let's play, winner!"
    "Olga slammed the ball hard."
    "Yeah, she pumped it up good."
    show un normal sport at left with dissolve
    un "Um... Olga Dmitrievna?"
    mt "It's good that you're here, Lena. {w}You'll be on the team with me."
    "Beach volleyball..."
    "It's going to be a lot more than that!"
    scene bg ext_volley_court_7dl with dissolve
    "We spent the first few innings assessing opponents and mates."
    "Hit. Pass. Strike. Cut. Take it on the folded palms and send the ball with a candle in the sky..."
    "Ulyana was good backup, except she wasn't worth putting in front of the net because of her height."
    "But she was fast, and sometimes it looked like a hundred-armed creature was on the court."
    us "Hey, rookie, don't sleep!"
    "The little one took out another impossible ball and passed it to me, and I took advantage of my bouncy nature to push the ball over the net, letting it fall on the other side of the field."
    show mt smile sport at fleft with dissolve
    mt "What a bug you are!"
    "Olga held out in admiration."
    th "In battle, as in love, all means are good."
    mt "Dvachevskaya!"
    "Suddenly the squad leader shouted."
    mt "Don't pass by!"
    dv "I won't, my stomach hurts."
    "Alisa brushed it off."
    mt "That's okay, since you're running, you can play, too. Get on the other side of the net."
    "Disgruntled Alisa, gritting her teeth, obeyed."
    mt "Come on, come on, don't cackle! {w}Exercise is good for you!"
    show un smile sport at fleft
    show mt normal sport at left behind un
    show ba normal uniform at cleft behind mt
    with moveinleft
    show us smile sport at fright
    show dv normal sport at right behind us
    with moveinright
    "Also, the leader successfully caught the zombie-looking gym teacher wandering somewhere and put him up against the net."
    "Three on three."
    dreamgirl "They came together. Wave and stone, Verse and prose, ice and flame. Not so different from each other."
    "The inner voice amused itself as it wished."
    dreamgirl "Survival of the fittest!"
    th "Will you stop it already?"
    dreamgirl "Do you think so?"
    th "I'm sure."
    dreamgirl "All right. {w}Then..."
    scene bg ext_volley_court_7dl with dspr
    show blackout_exh
    play music music_7dl["anglegrinder"] fadein 3
    scene cg d4_volley_rage_7dl with flash
    with vpunch
    $ alt_pause(1)
    show dv_us_volley with vpunch
    $ alt_pause(1)
    show volley_fight at truecenter with zoomin
    with vpunch
    $ alt_pause(3)
    ba "Ball in play. The pitch is on the squad leaders' side."
    scene bg ext_volley_court_7dl with flash
    "Sanich barked, blowing his whistle."
    "And - there it is! The game is on!"
    show un smile sport at fleft
    show mt normal sport at left behind us
    show ba normal uniform at cleft behind mt
    with moveinleft
    show us smile sport at fright
    show dv normal sport at fright behind us
    with moveinright
    "Today we're finally going to find out who's the strongest in this camp!"
    "Olga went to the spot and sent the ball to our side with a slap shot."
    me "I'll take Sanich; Alisa, Lena is on you!"
    "Dvachevskaya nodded and moved to the left flank, mirroring Lena's position."
    "The gym teacher winked at me, catching my eye, and took the spot at the net opposite me."
    dv "Lena!"
    un "W-what..."
    "Olga just cut to the left, and Ulyana once again showed the world the wonders of teleportation."
    dv "There's a spider on you!"
    un "AHHH!!!" with vpunch
    show un shocked sport with dspr
    un "Where!"
    "Lena shrieked and bounced awkwardly in place, trying to shake herself off at the same time."
    dv "Here!"
    play sound sfx_7dl["volley_hit"]
    "And Alisa, rising in a leap of almost a kilometer, pounded the ball almost vertically down the other side of the net."
    scene bg ext_volley_court_7dl
    with fade
    "Unfortunately, we lost anyway."
    stop ambience
    stop music fadeout 4
    play ambience ambience_camp_center_evening fadein 3
    scene bg ext_volley_court_7dl with flash
    "The match was bad."
    "That's because the squad leaders cheated."
    "They couldn't win fairly."
    "Cheaters!"
    play music music_list["get_to_know_me_better"] fadein 5
    "But... You don't wave your fists after a fight."
    "I had to shake hands with my opponents. {w}Even though they were crooks."
    "After squeezing hands of crooks on the opposing side, we dejectedly vacated the square we were occupying."
    "It was immediately occupied by the pioneers, inspired by the friendly match."
    with fade
    el "Hey!"
    "There was a tinny thud from the side of the benches."
    scene bg ext_volley_court_7dl:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 0.3 zoom 1.15 xalign 0.5 yalign 0.5
    show el normal pioneer at center
    el "Folks, if anyone is thirsty, please help yourselves."
    "Electronik, who had been watching the game for the last hour, brought a bucket of water with a steel camping mug attached on a chain."
    hide el with dissolve
    "Of course, such an offer was a sin to refuse!"
    "I got in line."
    mt "Get ready for dinner, if anyone wants a shower, I'll go make arrangements for the water to be warmed."
    "Alisa and Lena instantly followed the squad leader."
    hide mt with dissolve
    hide dv normal sport with dissolve
    hide un
    "And Sanich, having sucked half a bucket in one fell swoop, hunched over again and wandered back to his den."
    "Bear, the strong, the hairy one."
    hide ba with dissolve
    "It's just me and Ulyanka left."
    show us sad sport with dspr
    me "Aren't you going to shower?"
    us "What's your purpose in wondering..."
    "Sluggishly she parried."
    me "I'll turn off the hot water supply there."
    us "Ah..."
    "She stopped talking."
    me "Did you steal and eat a kilo of lemons somewhere?"
    me "Is that why you're so sour?"
    show us angry sport at center with dspr
    us "They cheated!"
    "Ulyanka stomped her feet."
    me "Yep. They were giving in badly."
    us "There! Only you understand me."
    us "Let's teach them a lesson, shall we? {w}Next time they'll play fair!"
    me "Come on! How?"
    show us grin sport with dspr
    us "We'll think of something!"
    me "Then meet me at the infirmary after dinner!"
    "She was moving away too fast, so a Doppler-extended bass reached me."
    hide us with easeoutleft
    us "Deeeeeeaaaaaaaaaal."
    "One hundred percent, she went for a swim."
    "Now, while all the parents haven't been kicked out of camp yet, the squad leaders are kind-hearted."
    th "Should we follow her example?"
    if alt_day3_sl_bath_voy:
        "Or should I visit the bathhouse today, too?"
        "Though, of course, you can't expect yesterday's aperitif to the meal."
    "After thinking it over a bit, I went to the bathhouse and took the line right behind some girl from the second unit."
    "The window was for twenty-one hours, and I suddenly had plenty of time."
    "All that was left to do was to think of something to occupy it with."
    stop music fadeout 3
    stop ambience fadeout 6
    return

label alt_day4_me_neu_supper:
    scene bg int_dining_hall_people_sunset_7dl with dissolve
    play ambience ambience_dining_hall_full fadein 3
    play music music_7dl["shehasgone"] fadein 3
    "We're young, and we're going to live our lives to the fullest."
    "Behind the bars in the asylum."
    "Oddly enough, it was a young, sunny day."
    "Really warm."
    "But there's still no happiness."
    "And it's not even that they tried to ruin my mood a couple of times today."
    "After all, I've always believed that beauty with flaws is better than beauty without flaws."
    "Otherwise you can't get away from the feeling that you're looking at a work of art, dating a statue or living in a museum."
    "Or maybe I've just begun to more or less understand those around me, and for me their being is no longer a cloudless sky."
    show sl smile pioneer at right with dissolve
    "Slavya is smiling habitually, but she holds her back as if she were standing on the parade ground."
    "She's tense, and I remember perfectly well that work doesn't stress her."
    th "Had a fight with her parents?"
    hide sl with dissolve
    show mi sad pioneer at left with dissolve
    "Miku's eyes are wet."
    "She's a superstar and an artist, of course. {w}But she's still very young, and she doesn't hide her emotions very well. The diagnosis is the same: family problems."
    if (alt_day2_date == 'mi') and (alt_day2_mi_date != 3):
        th "Whoops. {w}How do I know she's a superstar?"
        th "How did it suddenly come to my mind?"
    hide mi with dissolve
    show un serious pioneer at cright with dissolve
    "Lena... Well, this one's a bulbous girl, you can't tell her apart."
    "I can't say she was upset - more like discouraged about something."
    "As if she'd been dreaming about something all her life, and the dream that came true either didn't come true in the right way, or, much worse, was boring."
    th "What do I know about her? {w}She's... Well, she loves..."
    if alt_day2_date == 'un':
        th "Solitude."
        th "Lonely places."
        if loki:
            th "Kissing. {w}Ah and oh, where are my seventeen years!"
        else:
            th "Pretending to be weak, even though you're actually very strong."
    elif ('library' in list_voyage_7dl):
        th "Drawing, seems like."
        "Not sure, though."
    th "Well... Maybe reading? I saw her with a book the first day."
    "With a starting point, the analysis looked a little more fun:"
    th "So she's reading a book and she gets really hooked on it."
    th "And then it turns out to be the only book in the series, and that's great!"
    dreamgirl "This story has a bad ending. {w}After getting to the end of a beloved series, she buys the latest book to complete the series."
    dreamgirl "And realizes that the author is worn out, frayed, and no longer in fairy tale land."
    hide un with dissolve
    show us sad sport with dissolve
    if alt_day4_me_neu_volley:
        "Ulyanka frowned at the match and was going to take vicious revenge."
    else:
        "Ulyanka was also upset about something."
        show us surp1 sport with dspr
        "Although, when she intercepted my gaze, she couldn't help herself - she pressed the thumbs of her spread palms to her ears and shook her head."
    hide us with dissolve
    "In short, a depressed mood prevailed in the dining room."
    "So much for the long-awaited reunion with loving relatives."
    if alt_day4_me_neu_volley:
        "Only our leader looked fresher and better-looking."
        "That's what moderate exercise combined with a shower does!"
        "So I finished my meal in a hurry and got up."
    else:
        "Olga Dmitrievna also looked wrinkled and dejected."
        scene bg int_dining_hall_people_sunset_7dl with dissolve
        "The pioneers and the parents rolled her into the asphalt."
        "For some unknown reason, the lion's share of the burden of pleasing the committee was somehow placed on the shoulders of the first squad leader."
        "It's because we have the least number of pioneers."
        "So she was still babysitting these teenagers in their forties after the concert, catching everyone around camp and escorting them to the comfortable bus."
        "She didn't even flinch habitually, noticing that Ulyana was out of shape."
        th "I wonder if I had come here in jeans, would she have tolerated it, too?"
    stop music fadeout 3
    stop ambience fadeout 6
    return

label alt_day4_me_neu_reward:
    scene bg int_dining_hall_sunset with dissolve
    play ambience ambience_dining_hall_empty fadein 3
    "After sluggishly nibbling on her dinner, Olga rose and, looking around in a shifty way, disappeared into the dining room staff quarters."
    "She had been gone for quite some time."
    "The pioneers had already dispersed, leaving only Ulyana and me at the table."
    show us smile sport with dspr
    us "What are you going to do now?"
    me "Solve a difficult problem."
    show us surp3 sport with dspr
    us "Which one?"
    me "I'll be figuring out whether to lie on my left side or my right."
    show us laugh sport with dspr
    us "Come on!"
    "She got up."
    me "Kid, wait for me on the porch, will you?"
    us "Why would I do that?"
    me "I'll get something good. {w}Want some?"
    show us surp1 sport with dspr
    us "You want to rob the canteen? {w}I'll go with you! But I call dibs on the candy!"
    me "I'm not going to rob anything!"
    "I cut her off."
    me "And you're not going anywhere with me."
    me "Just wait for me on the porch and I'll get you something, all right?"
    "She got sad."
    us "If being an adult is being a boogeyman like you, I don't want to grow up!"
    show us normal sport with dspr
    us "Fine, I'll wait."
    hide us with dissolve
    "After the little one left, I had to wait another ten minutes before Olga Dmitrievna finally appeared from the kitchen."
    show mt normal pioneer with dspr
    mt "You guessed it, didn't you?"
    me "You bet I did!"
    if alt_day3_duty:
        me "I knew from yesterday that the camp had ice cream."
    show mt laugh pioneer with dspr
    mt "Okay, since you're so smart - here's a portion for you and Ulyana and Alisa, don't you dare eat it all yourself! I'll ask them!"
    "Sounds to me like Dvachevskaya didn't deserve her portion, but I held back my objections and nodded silently."
    show mt normal pioneer with dspr
    mt "That's it, I don't owe this day anything anymore."
    me "Are you going to disappear again?"
    mt "I have every right! {w}And woe to whoever finds me!"
    hide mt with dissolve
    "Nodding goodbye to me, she disappeared out the door."
    with fade
    "Carefully separating the paper from the ice cream mass, I made a few adjustments to the recipe for the ice cream, then put the patches back in place."
    stop ambience fadeout 3
    play sound sfx_open_door_1
    $ alt_pause(1)
    scene bg ext_dining_hall_near_sunset
    show us normal sport
    with dissolve
    play ambience ambience_camp_center_evening fadein 3
    "Ulyana, luckily, was here."
    me "Hey."
    show us dontlike sport with dspr
    us "You took a long time!"
    me "But here!"
    "I handed her the ice cream."
    show us surp1 sport with dspr
    us "Ice cream!"
    "I froze and held my breath."
    "It didn't take long for her to toss the paper and gulp down the treat."
    "I gulped."
    show us smile sport with dspr
    us "It was worth the wait!"
    play music music_7dl["genki"] fadein 3
    me "Uh-huh…"
    th "She's actually eating that!!!" with vpunch
    show us laugh sport with dspr
    us "Why are you staring at me like that? {w}What's the big deal about eating ice cream?"
    "She was staring at me in bewilderment."
    us "Delicious ice cream. Chocolate chip."
    "Chocolate chip, yeah..."
    me "No, don't think I'm scolding you."
    me "But don't chew it, are you off your palm tree?"
    show us dontlike sport with dspr
    "Ulyana blushed with anger."
    "She even seemed to shake a little."
    "I didn't think she could be hurt by such a ridiculous thing."
    "But that's not what I'm interested in."
    "That 'special' ice cream I made for Dvachevskaya - where is it?"
    "I specifically made sure - by sneezing all over the canteen - that the secret ingredient was the one."
    "Then I took three popsicles and brought them out here."
    "I gave one to Ulyana, I kept two."
    me "Like a monke…"
    show us angry sport with dspr
    "Boom!" with Shake((0, 0, 0, 0), 0.3, dist=50)
    "The ice cream hit me right in the face!"
    "And I caught it mechanically, not letting it fall."
    "And, wiping my forehead, I licked my fingers."
    me "…"
    play sound sfx_angry_ulyana
    me "…"
    with flash_red
    me "Aaah, aaah, aaah..."
    me "Aaah! Please!"
    "It was a bee hive!"
    with flash_cyan
    "A supernova explosion."
    "The fire in my mouth couldn't be put out by anything."
    show us fear sport with dspr
    us "…What…"
    "Ulyana exhaled briefly, looking at my torment."
    show us surp3 sport with dspr
    "And for some reason she blushed."
    "Even more so."
    show us shy2 sport with dspr
    "Somebody normal would have called 911 a long time ago and entrusted me to the professionals, but..."
    show us shy sport with dspr
    "She blushed and blushed..."
    "As if she saw something incredible..."
    "Unbelievably..."
    show us fear sport with dspr
    us "Ew!"
    us "You jerk!"
    us "You licked it! Give me yours now, you bastard!"
    me "And you were biting, but..."
    show us angry sport with dspr
    us "Mouth to mouth. {w}Foo! Yuck!"
    me "Stop it. {w}I'm not the type to finish after a girl or anything like that."
    me "Do I look like a hunter for..."
    with fade2
    me "Indirect kisses."
    dreamgirl "O-oh."
    me "That's it. {w}I understand. {w}I'm sorry. {w}I didn't mean it."
    "The broom in Ulyana's hands did not contribute to my mental equilibrium."
    "Or rather, it was not even a broom, but an entire missile complex with the means to capture, guide, and hit the target repeatedly."
    "And this complex turned in my direction, beeping, capturing the target..."
    "The small one's eyes read 'GUILTY' in jumbo letters."
    "I barely dodged the broomstick thrown at my head."
    "And lost everything I had in my hands."
    "Including my ice cream!!!"
    "But there was no time for that now."
    "Ulyana picked up a metal scoop and, judging by the way she was holding it, she wasn't going to hit me with the plane at all."
    "Terrible weapon!"
    "And I did the only thing I could in such a situation."
    "I courageously {w} ran."
    scene bg ext_dining_hall_away_sunset at running
    with zoomin
    th "Why didn't she notice some of the changes in the recipe?"
    "Rattled in my head."
    us "Aaaagh! Come here!"
    "Barked the little girl running after me."
    show us angry sport far at left with dissolve
    "And she just earned herself an extra serving."
    "What was most infuriating and hurtful was that she probably wouldn't even know the difference between the two."
    "I tried to stifle the thought that maybe the little one had set up this farce on purpose to get my ice cream portion."
    stop music fadeout 3
    return

label alt_day4_me_neu_pirate:
    scene bg ext_square_sunset with clock_r
    play music music_7dl["sneakupon"] fadein 3
    "I spent half an hour hiding in the bushes from an enraged Ulyanka."
    "And I was very sad that someone had eaten my hard-earned prize."
    scene bg ext_dining_hall_near_sunset with dissolve
    "Unbelievable, but true! The same portion that almost smashed into my forehead was still lying there, carefully transferred to the bench."
    "Though it had thawed considerably, there was hardly any pepper left."
    th "Well, at least there's something!"
    "The place to eat the spoils was the most convenient, and I was about to start eating."
    "And then I noticed a strange silhouette!"
    show mi happy pioneer far with dissolve
    mi "Pum-purumm-pum-pum!"
    th "Miku?"
    "With an expression of boundless happiness on her face, the Japanese girl crept somewhere toward the back of the canteen."
    me "What's going on?"
    "I decided to follow her."
    mi "Nya-nya-nya…"
    "She was purring to herself, not paying attention to what was going on around her."
    "A couple of yards to the corner, she squatted down and peered out carefully."
    me "…"
    scene bg ext_dining_hall_backroad_day_7dl
    show mi happy pioneer
    with dissolve
    "I got closer."
    "And apparently, somehow, I gave myself away."
    show mi scared pioneer with dissolve
    mi "Huh?"
    hide mi with easeoutbottom
    "She instantly noticed me and turned around."
    me "Miku!"
    show mi dontlike pioneer with dspr
    mi "Oh-oh-oh-oh-oh-oh-oh!"
    me "Miku, what are you doing?"
    show mi upset pioneer with dspr
    mi "Alright! Not a word to anyone!"
    "She pressed her finger to her lips and glanced around."
    "I guess she was figuring out how to fool me."
    "But you got the wrong guy."
    me "Don't you dare lie to me!"
    mi "I'm not lying to anyone, come on, Senechka, my father told me today that their construction worker lied and had to reassemble an entire section of the bridge!"
    "Right."
    "I think it's gonna take a while."
    show mi upset pioneer at right with moveinright
    "I correctly pulled her aside and looked out myself."
    scene bg ext_warehouse2_day_7dl
    show sl normal pioneer far
    with dissolve
    "By the little house, set aside, most likely, for the temporary storage of non-perishable food, Slavya was doing something."
    hide sl with moveoutleft
    "Finally, she finished her business and, looking around in a cooing manner, set off."
    mi "Let's go!"
    stop music fadeout 3
    "A few seconds of fiddling with the locks…"
    scene bg int_attic2_night_7dl with dissolve
    "We found ourselves inside."
    "The unique opportunity to learn a few of our perfect girl's secrets was pleasing to the soul."
    "However, it didn't bother Miku in the slightest."
    "She walked purposefully toward the depths of the room."
    mi "Senya, come here!"
    "She called in a strained whisper."
    "I approached."
    "And finally learned the activist's terrible secret."
    play music music_7dl["beasteye"] fadein 3
    scene cg d6_sl_puppy_7dl
    with dissolve
    "In a huge nest of rags, on the floor, surrounded by boxes of canned food, powdered milk, and vacuum packs, a tiny, lop-sided puppy was cowering!"
    "Snow-white, with a prominent black nose and button eyes."
    "More like a bear or a plush toy."
    "Woof!" with vpunch
    "He cocked his head and barked at us."
    mi "Samoyed."
    mi "No."
    "Seriously answered Miku."
    mi "It's a dog."
    th "And how did she hide him for so long?"
    mi "A puppy. {w}How cute!"
    "How'd she just sneak him in?"
    mi "It was left over from the first shift."
    mi "I wish I could..."
    "The Japanese girl sighed with undisguised envy."
    mi "Eh. I was never allowed to have a dog either."
    me "But I guess it's forbidden to keep them on the grounds?"
    mi "That's why you won't say anything to anyone."
    scene bg int_attic2_night_7dl
    show mi smile pioneer
    with dissolve
    "I saw something sinister in the friendly smile of the Japanese girl, and I hastened to agree."
    me "But to hold a dog like that..."
    show sl normal pioneer at left with dissolve
    show mi normal pioneer at right with moveinright
    sl "I cared for him until his eyes opened."
    "Slavya came up unnoticed."
    sl "Once the second shift ends, I'll take him to town to find an owner."
    me "What about..."
    sl "It's all right."
    "The puppy caught something in the air and crawled toward us on his belly, wagging his tail in a funny way."
    "Slavya seems to have noticed something, too."
    sl "Okay, Semyon."
    "She turned me around by the shoulders and gave me a gentle nudge away."
    show sl normal pioneer far at cleft
    show mi normal pioneer far at cright
    with flash
    sl "You seemed to have things to do."
    sl "And eat your miserable ice cream already, Pirate is worried!"
    me "Pirate?"
    "Looks like someone got a little sour about caring..."
    "With an obedient nod, I hurried away."
    play sound sfx_close_door_campus_1
    $ alt_pause(1)
    scene bg ext_dining_hall_near_sunset with dissolve
    "And as I found myself outside, slamming the warehouse door, I caught myself smiling stupidly the whole time."
    th "So, then, the first day she..."
    dreamgirl "Yes. {w}Hurried to Pirate."
    dreamgirl "After all, an unfamiliar pioneer isn't exactly helpless, but a puppy..."
    "Marking the event as definitely positive in my invisible memory book, I decided to walk around camp and finish off the wretched ice cream."
    stop music fadeout 3
    return

label alt_day4_me_neu_square:
    play music music_list["trapped_in_dreams"] fadein 3
    scene bg ext_square_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 3
    "I went out into the square and sat down on a bench."
    "Evening."
    "This hectic day is winding down."
    "Though I do feel a little lost, because I've never really gotten close to anyone."
    "Except to get to know the camp a little better, make friends with the little one, and stop thinking Lazybones was evil."
    if alt_day4_me_neu_volley:
        "Ulyanka promised to come soon, but until then, again, I have to think of something to occupy my stupid head with."
    th "There's no doubt that Olga is going to be puzzled by something."
    th "In fact, the squad leader explicitly hinted that after dinner she was going to have a little rest, and woe to whoever finds her."
    "The batteries in the appliances are inexorably running low."
    "So, no music or reading."
    "After sitting and sighing some more, I realized I couldn't drag it out any longer."
    "Got up."
    "And went to wander around the camp."
    stop ambience fadeout 3
    return

label alt_day4_me_neu_map_medic_house:
    play ambience ambience_camp_center_evening fadein 2
    play music music_list["goodbye_home_shores"] fadein 3
    scene bg ext_aidpost_sunset_7dl with dissolve
    "After fifteen minutes of aimless wandering, I stopped at the infirmary."
    scene bg ext_aidpost_sunset_7dl:
        align (0.45, 0.6)
        zoom 2.0
    with dissolve
    th "All roads in this camp lead to the lair of the horny nurse..."
    th "I wonder what would happen if I knocked and asked in a languid voice to examine me?"
    dreamgirl "I'm afraid, buddy, you'll be prescribed a couple of cc's of bromine intramuscularly. And that's in case you're really lucky."
    th "And if I'm very unlucky?"
    play sound sfx_medpunkt_door_open
    $ alt_pause(1)
    show cs doubt at right with dissolve
    "The nurses' station door creaked open, and I jumped in horror. Viola looked out and gave me a worried look."
    cs "Came to complain, pioneer?"
    "I could hardly contain a sigh of relief within me."
    th "Oh yes, I'm sick and dying..."
    me "There's nothing to complain about, really."
    th "Except for mortal ennui, but I don't think Viola can find a cure for that."
    dreamgirl "A controversial statement..."
    show cs grin at right with dissolve
    "After making sure I wasn't planning on fainting, the nurse nodded contentedly. But instead of returning to her business, she glanced around and gave me a conspiratorial wink."
    cs "I see you still haven't found something to put your hand to?"
    "Though the question was perfectly innocent, Viola's intonation made me blush from head to toe."
    th "Is she making fun of everybody like that, or am I her favorite?"
    show cs smile at right with dissolve
    cs "Come on in, pioneer. Help two bored ladies brighten up the evening."
    th "Two?!"
    "Whatever Viola was going to offer, it clearly didn't bode well for me. But it was too late to run away in shame-she opened the door with an inviting gesture, and I obediently stepped into the infirmary."
    th "She wouldn't jump on a poor defenseless pioneer in front of a witness..."
    th "She's not going to pounce, is she?"
    play sound sfx_medpunkt_door_open
    $ alt_pause(1)
    scene bg int_aidpost_sunset_7dl
    play ambience ambience_medstation_inside_night fadein 3
    show ka normal pioneer at cright
    with dissolve
    if alt_day3_un_fz_work == 'dv':
        "On the couch sat the red-haired leader of the second troop, who I already knew."
        th "Well, that makes sense now!"
        th "They have a closed club of girls who like to troll the kids. Now Olga's coming too..."
        ka "Oh, it's my little helper!"
    else:
        "On the couch sat a redheaded girl, who looked the same age as Olga. I think I caught a glimpse of her in the dining room."
        ka "Oh, our honorable latecomer!"
        th "Ope... latecomer?"
        $ meet('ka', "Katyushka")
        ka "My name is Katyushka. And you don't have to introduce yourself, you're already a celebrity!"
    me "Greetings."
    th "And what are they up to?"
    play sound sfx_close_door_1
    "Viola shut the door and nodded at my couch."
    show cs smile at left with dissolve
    cs "You take a seat, pioneer."
    "I cautiously crouched on the edge of the couch, glancing sideways at the mocking leader."
    me "Why don't you tell me what's going on here?"
    cs "Nothing much. Just spending a nice summer evening."
    "In her hand, as if out of nowhere, a deck of cards appeared - too big for standard playing cards."
    show cs laugh at left with dissolve
    cs "And we were just short of one person to play poker. Borya... that is, our esteemed PE teacher, as always, turned away under the pretext of urgent matters."
    cs "Fortunately, some have plenty of free time. Do we need to explain the rules?"
    th "As I recall, the first rule of children's camp is no gambling on children's camp grounds!"
    me "Mmmm...I think I'm pretty much familiar with them."
    show ka smile pioneer at cright
    "Katyushka laughed out loud."
    ka "Well, what a lucky catch!"
    th "Yes, he's the seamstress, the reaper, and the poker player..."
    dreamgirl "You should marry a man like that!"
    show cs normal at left with dissolve
    cs "Then help me organize the space, pioneer. Take that couch over there and move it closer to us."
    th "Eh, and here I thought at least someone saw me as an interesting person and not a free and unreliable longshoreman!"
    "While I was dragging the couch (obviously chosen to be the gaming table), Viola pulled out a gray box from the small and inconspicuous nightstand in the corner."
    cs "Let's consider you a trustworthy man. I don't show my arsenal to many people..."
    "She opened the box, and I gasped in amazement. In the box were neat stacks of poker chips - the real ones, like from a Las Vegas movie."
    th "And where did she get all this stuff from in a run-down pioneer camp? Maybe the rich patients were generous with such a gift."
    th "Well right, it's not just candy and cognac to thank the esteemed doctor!"
    stop music fadeout 3
    "Deciding to think seriously about it sometime at my leisure, I tried to focus on the game."
    play music music_list["eternal_longing"] fadein 3
    show ka normal pioneer at cright with dissolve
    cs "Katerina, distribute the chips. I'll be the dealer in the first round, then we'll go around the circle. The small blind is five."
    "Viola pushed her chair up against the couch and began lazily shuffling the cards. I pulled a handful of chips toward me and put a fiver up front."
    th "We're not playing for money, are we?"
    "I glanced uneasily at my unperturbed opponents. I've rarely been lucky in gambling."
    dreamgirl "You'd better think about what you're going to pay back if it's for money after all!"
    show ka grin pioneer at cright
    ka "Don't be so nervous, Semyon!" with hpunch
    "Katushka elbowed me in the side with outrageous directness."
    ka "If the camp leader comes here, just run and hide in the isolation ward!"
    "Throwing an angry look at the squad leader, I rubbed my ribs."
    me "And you!"
    show ka shy pioneer at cright with dissolve
    ka "What about me?"
    me "You're slacking off, that's what!"
    show ka grin pioneer at cright with dissolve
    "The girl giggled merrily. She didn't seem to be offended by my words."
    ka "My pioneers are decent people. They don't need a babysitter."
    if alt_day3_un_fz_work == 'dv':
        th "Yes, yes, so decent that they want to run off into the woods at the first opportunity!"
    cs "Handing out cards."
    show cover:
        align (0.11, 0.2)
        zoom 0.25
    with dissolve
    pause(0.3)
    show cover as cover2:
        align (0.01, 0.2)
        zoom 0.25
    with dissolve
    pause(0.3)
    show cover as cover3:
        align (0.81, 0.2)
        zoom 0.25
    with dissolve
    pause(0.3)
    show cover as cover4:
        align (0.91, 0.2)
        zoom 0.25
    with dissolve
    pause(0.3)
    show 1_ussr:
        align (0.15, 0.7)
        zoom 0.25
    with dissolve
    "I grabbed the first card off the couch in a jiffy and looked at it cautiously."
    th "Ace of hearts. Not good, but if no one has anything..."
    show 2_utan:
        align (0.25, 0.7)
        zoom 0.25
    with dissolve
    "The second card was a deuce of spades, not surprising with my karma. I had two choices - to shamefully fold and give up the small blind, or to bluff."
    "Viola, meanwhile, had an indifferent face and laid out a ten. After hesitating, I moved another five to my blind."
    th "I can always get out of the game, there's plenty of chips left. It's too early to give up before the flop!"
    th "And judging by the fact that no one has raised, my opponents have no pairs in their hands. That's all right, we'll get through!"
    cs "My knees are aching today. It's for rain."
    show 7_uvao:
        align (0.55, 0.7)
        zoom 0.25
    with dissolve
    pause(0.3)
    show 5_2ch:
        align (0.65, 0.7)
        zoom 0.25
    with dissolve
    pause(0.3)
    show 8_uvao:
        align (0.75, 0.7)
        zoom 0.25
    with dissolve
    "In a steady voice Viola said, laying out three cards on the couch table. My position became even more unenviable: the seven of clubs, the five of diamonds, and the eight of clubs stared at me."
    "I pursed my lips in annoyance, but immediately I remembered and made a face like a brick. But my fleeting disappointment did not go unnoticed."
    ka "Don't take it personally, pioneer: if you don't get lucky in the first round, you'll get lucky in the next!"
    "Barely restraining myself from mouthing off to the annoying squad leader, I put out a ten. Viola sniggered regretfully."
    cs "Kids today don't have the guts to play big. What will they do to the country in ten years?"
    "Now I had to hold back an already gloating laugh."
    th "Oh, Mistress Doctor, you better not know what awaits this country in two years!"
    show ka smile pioneer at cright with dissolve
    ka "You just have to set the right example for them. Raise!"
    "Katushka put out a yellow chip with the number 50 on it. I fidgeted nervously on the couch."
    th "No, I'm not falling for that."
    th "I'm only going to lose twenty. It's unpleasant, but bearable. After all, this is my first poker game in God knows how many years, and with my karma, getting lucky on the first hand would be like raining in the middle of the Sahara."
    cs "Leveling."
    "Sending the blue chip to the bank, Viola cast a dispassionate glance at me."
    cs "Pass, pioneer?"
    "Feeling myself blush with anger, I prepared to dump my cards on the table, but instead for some reason put up two green chips of twenty-five, snatching back my ten."
    show cs smile with dspr
    "The nurse gave a satisfied chuckle."
    cs "Now I see the fighting spirit. Turn!"
    show 11_uvao:
        align (0.85, 0.7)
        zoom 0.25
    with dissolve
    "Jack of clubs on the table."
    th "Damn them all!"
    show cs normal with dspr
    "It was almost impossible to determine the position of my opponents."
    "Katyushka was clearly having fun, but I couldn't tell if it was the lucky cards in my hands or Viola's mini-bar, which I glimpsed in the nightstand."
    "Viola, on the other hand, was sitting there with a dispassionate face-as befits a good poker player."
    th "I can't pass now, I'll be ashamed of myself. The only thing left is to bluff..."
    "I didn't know how to bluff, and I could tell by the shaking hand I used to throw a black hundred into the pot."
    show ka normal pioneer at cright with dissolve
    ka "He's a fast learner!"
    me "Hey!"
    me "I'm actually still here, in case you forgot."
    ka "It's not hard to forget - you sit there pouting and keeping quiet. You should at least talk to the ladies!"
    th "Oh yes, I've wanted to discuss the ethical treatment of pioneers in this camp for a long time, but I never got the chance!"
    me "How long have you been working here?"
    "I asked, so as not to look like an offended little boy."
    ka "This is my first shift here."
    "The squad leader matched my bet."
    show ka smile pioneer at cright with dspr
    ka "So if I break any rules, it's purely out of ignorance!"
    me "Ignorance doesn't master..."
    ka "Booooring!"
    cs "Leveling."
    "Viola has advanced two yellow chips."
    cs "Well, gentlemen and ladies, river."
    show 1_utan:
        align (0.95, 0.7)
        zoom 0.25
    with dissolve
    "The last card was the ace of spades."
    dreamgirl "Wow, victory is in our pocket!"
    dreamgirl "The winning strategy is this: Grab the bank and get out of here as fast as you can. Then you can cash out in the district center."
    th "A pair in hand is better than nothing. Now I've got to make them believe I have at least a straight!"
    "With a winning grin, I put up three chips of fifty."
    ka "Raise!"
    "Two more chips of a hundred fell into the pot."
    th "Oh shit!"
    cs "Raise."
    th "Really?"
    show ka laugh pioneer at cright with dspr
    "Katyushka laughed when she looked at me."
    ka "Oh, they won't take you to the Moscow Art Theatre, no way!"
    show ka smile pioneer at cright with dspr
    th "Well, there's no point in passing up now. To die with a song!"
    "I doomedly put another hundred in the pot."
    cs "Reveal!"
    dreamgirl "No, we'll show our cards after everyone else has shown theirs."
    "Shamefully placing my cards on the couch, I muttered quietly:"
    me "Pair."
    hide cover3
    show 9_2ch:
        align (0.81, 0.2)
        zoom 0.25
    with dissolve
    pause(0.3)
    hide cover4
    show 10_ussr:
        align (0.91, 0.2)
        zoom 0.25
    with dissolve
    ka "Straight!"
    "The overly cheerful squad leader had a nine of diamonds and a ten of hearts on her hands."
    th "I see. She wasn't so happy for nothing..."
    th "Well, I'll have you know, the happy redhead is a pass before the flop."
    show cs grin with dissolve
    "Viola smirked triumphantly with just a corner of her lip."
    hide cover2
    show 10_uvao:
        align (0.01, 0.2)
        zoom 0.25
    with dissolve
    pause(0.3)
    hide cover
    show 9_uvao:
        align (0.11, 0.2)
        zoom 0.25
    with dissolve
    cs "Straight flush."
    show ka surprise pioneer at cright with dspr
    "My jaw dropped involuntarily as the nurse turned over her cards-the nine and the ten of clubs."
    th "That's not fair!"
    th "She was handing out cards - she cheated, anyway!"
    dreamgirl "Ulyana, calm down, you'll get your cake too!"
    "While Viola was raking in the whole pot, I was frantically thinking through my strategy for the next hand."
    stop music fadeout 3
    th "I can't bluff, so I'll play fair. Well, if that's possible with a cheating nurse and drugged squad leader!"
    play music music_list["sweet_darkness"] fadein 3
    scene bg int_aidpost_sunset_7dl with fade2
    show cs serious at left
    show ka normal pioneer at cright
    with dspr
    "Honestly, having passed the next two rounds, I watched with a sour face as the bank wandered from Viola to Katushka and back again. On the fourth hand two queens came into my hand, and half of my remaining chips went to the pot, because the third queen was already lying on the table..."
    show cs grin at left
    show ka laugh pioneer at cright
    with dissolve
    cs "Flush." with vpunch
    th "Aaah!"
    ka "Pull yourself together, pioneer! We're going to rip you to shreds!"
    me "You'd think I'd have a say in this!"
    "I grumbled back angrily. I'd given up on my face by the third round."
    show cs laugh at left with dissolve
    cs "You'd better think about how you're going to pay if you lose."
    th "Pay up?!"
    "I picked up my cards with trembling hands. The feeling of imminent defeat clung vilely to me, depriving me of the ability to think logically."
    show ka normal pioneer at cright with fade2
    me "Straight!"
    "I glanced victoriously at Viola. Katyushka had passed as early as the second round of bidding, which gave me some hope."
    th "After all, I didn't have any chips left at all. There would be an upside to losing, too: for instance, I could get away from this casino!"
    show cs grin at left with dissolve
    cs "Royal flush." with vpunch
    stop music fadeout 4
    th "What kind of kiosk charged this deck?!"
    play music music_list["glimmering_coals"] fadein 5
    "Viola raked up all my chips and stared at me mockingly."
    cs "I hope you have something to offer us, pioneer?"
    me "Uh..."
    th "I wonder if they'll settle for a canteen gingerbread?"
    show ka smile pioneer at cright with dissolve
    ka "Well, you can be socially useful."
    if alt_day3_un_fz_work == 'dv':
        ka "I know you like to help those in need!"
    ka "Like waking up my pioneers in the morning for the rest of my shift..."
    show cs doubt with dissolve
    cs "Then he'll be free in the afternoon, I suppose? I still have so many unfilled magazines..."
    show cs laugh at left
    show ka laugh pioneer at cright
    with dissolve
    "The women laughed in sync, and I felt myself starting to boil."
    th "No way!"
    th "Laugh, laugh, laugh, before I rat you out to the camp commander!"
    "But the very thought of snitching on Viola inspired unparalleled horror."
    th "I'm going to snitch on her, and she's going to look me over..."
    "I couldn't deny it any longer: I was in trouble."
    show cs serious at left with dissolve
    cs "You know though, pioneer..."   
    cs "There's one thing I can get you to do."
    "I didn't like Viola's tone of voice. {b}Not one bit{/b}."
    cs "Right now put the couch back and get out for a walk. Fresh air is quite useful before bedtime."
    th "Is she serious now?"
    cs "Well, we'll trade your card debt for non-disclosure, all right. Silence is gold. Ain't that right, pioneer?"
    "Nodding like a chump, I jumped up from my seat and dragged the couch to the far corner of the infirmary."
    ka "Drop in again when you've missed me!"
    th "Yeah, keep your pocket wide!"
    th "I'll never set foot in this infirmary!"
    play sound sfx_medpunkt_door_open
    scene bg ext_aidpost_night with dissolve
    play ambience ambience_camp_center_evening fadein 1
    "I ran out the door, to the delighted laughter of my tormentors, and ran to the cabin, out of harm's way."
    $ alt_day4_me_neu_cs_debt = True
    stop ambience fadeout 3
    stop music fadeout 3
    return

label alt_day4_me_neu_map_cyber1:
    scene bg ext_clubs_sunset_7dl with dissolve
    play music music_list["your_bright_side"] fadein 2
    play ambience ambience_camp_center_evening fadein 2
    "Just a few days ago I had absolutely no problem with loneliness. What can I say, I didn't even notice it!"
    "It's hard to be lonely when you have all your friends at arm's length: forums, YouTube, torrents with endless gigabytes of shows and movies, and, in the very worst case, a stack of years of proven games."
    "Here, away from my cluttered desktop and a couple of decades before cheap and fast Internet, loneliness began to stifle as soon as the locals stopped circling me."
    th "You get used to a good thing fast, though..."
    "I took my smartphone out of my pocket and looked dolefully at the last percentage of charge."
    "I unlocked it to reduce the brightness in a vain attempt to delay its imminent demise, but found it was already at zero."
    th "If only the battery were removable, I might have invented something under the guidance of the cybernetic brothers..."
    th "But wait, why am I not accounting for them?"
    th "Just in case, what if the future luminaries of Soviet science manage to solve my problem?"
    dreamgirl "Great idea."
    dreamgirl "Just imagine: summer, sunshine, nature, beautiful girls dapper, and you are sitting in a secluded corner and frantically playing “match 3”…"
    dreamgirl "Spectacular!"
    th "I don't have this game at all!"
    th "Or do I?"
    th "Well, being a security guard is a lot more than that..."
    "I shook my head vigorously, as if trying to shake my split personality out of it."
    "The younger girls in the squad who ran by looked at me warily, and I felt myself blush."
    th "Maybe I should lie about having a bug in my ear."
    th "Oh, come on, that's ridiculous!"
    th "Why do I have to justify myself to them all? To my schizophrenia, to those girls!"
    stop ambience fadeout 1
    scene bg int_clubs_male_sunset with dissolve
    play sound sfx_open_door_1
    play ambience ambience_clubs_inside_day fadein 1
    "I sighed and entered the clubhouse."
    "Electronik sat alone, hunched over an ugly structure of wires and hardware."
    play sound sfx_close_door_1
    show el surprise pioneer with dissolve
    "He flinched at the creak of the door, almost dropping the soldering iron on the floor."
    show el smile pioneer with dspr
    el "Oh, Semyon!"
    if alt_day4_me_neu_us_debt:
        el "You're just in time! I just need some advice on a wiring diagram..."
        me "No offense, but I'm not good at wiring diagrams. I can tell a light bulb from a resistor, of course, but nothing more."
        me "You'd better ask Shurik. By the way, where is he?"
        show el normal pioneer with dspr
        el "In the cabin. His head hurts."
        "A little disappointedly threw Syroezhkin."
        me "I actually came for advice myself."
    else:
        show el smile2 pioneer with dspr
        el "What brings you here?"
        "I looked around the clubhouse in the highly irrational hope that Shurik was hiding in a closet somewhere."
        "For some reason the bespectacled man gave me more confidence in matters of fine technique."
        me "Yeah, I just need a little help."
        show el normal pioneer with dspr
    "I took a smart out of my pocket and held it out to Electronik."
    me "Have you seen anything like that?"
    show el think pioneer with dspr
    "Syroezhkin cautiously took the phone and began to twirl it in his hands."
    "A bad light flashed in the cyberneticist's eyes."
    show el serious pioneer with dspr
    el "Where did you get that from?"
    me "So you saw it?"
    show el normal pioneer with dspr
    "He looked at me incredulously."
    el "No, but there were rumors... It's got no buttons at all!"
    show el think pioneer with dspr
    "Electronik gently unlocked the screen and whistled. Then he awkwardly poked the screen with his finger."
    show el smile pioneer with dspr
    el "It's reacting!"
    show el serious pioneer with dspr
    "He exclaimed rapturously and stared at me again. There was no trace of his former joy."
    el "Where did you get that?"
    me "It was a gift from a, um... good acquaintance. I don't think you know him, and I think he'd like to remain incognito."
    th "What am I even saying?"
    "Dragging the wonder of technology to Syroezhkin for inspection was definitely a bad idea. But it was too late to back out."
    me "Anyway, it's a reader. For electronic books. Except I forgot the charger for it at home."
    me "Do you think there's any way to charge it with improvised means?"
    show el angry pioneer with dspr
    el "Electronic books!"
    "Electronik let out a nervous chuckle and looked at me very seriously."
    "In another situation I would have found his look amusing, but I wasn't in the mood for fun."
    el "Semyon, do you realize that this level of technology... It's unthinkable!"
    show el serious pioneer with dspr
    el "I don't know who your mysterious acquaintance was, but if I were you, I'd get rid of that thing. You realize it might have something to do with..."
    "He looked back toward the window, as if someone might have been eavesdropping on our conversation, and barely whispered:"
    el "...with military defense?"
    "I was taken aback."
    th "Of course, it's a natural distribution of technology in any state: first the military, then ordinary mortals to play with."
    th "And to see such a device as a smartphone in a camp where water is boiled in a jar..."
    th "Yeah, I'd have questions if I were him, too."
    me "Come on, this thing's two years old and the KGB have never come to my door."
    th "Although if Syroezhkin snitched to someone, anything could happen!"
    me "Better help me figure out how to charge it."
    show el think pioneer with dissolve
    "Electronik looked at the phone again, frowning his eyebrows in concentration."
    el "Is it battery operated or does it have an accumulator?"
    me "Accumulator. Unfortunately, it's not removable."
    show el think2 pioneer with dspr
    el "I'd like to take it apart, of course…"
    show el normal pioneer with dspr
    el "May I?"
    me "Uhh…"
    "On the one hand, Electronik obviously knew more about technology than I do."
    "On the other hand, thirty years of difference in technology could have had irreversible consequences if he had tampered with the inside of a smartphone."
    th "He might not hit it with a sledgehammer, but who knows what other nasty things might come into his bright head?"
    me "It would be better to charge it through the plug. Look closely, see if there's anything similar on hand."
    show el think pioneer with dspr
    "Syroezhkin pulled a flashlight from the depths of his desk and stared intently at the connector for the charger for several minutes."
    el "I'm afraid there's nothing like it. I've never seen one of those in my life!"
    th "That's not surprising. In a world that doesn't even have USB, there's hardly anything resembling micro-USB around."
    show el sad pioneer with dspr
    "He threw a glance at the clock, and the young cyberneticist's face became even darker than before."
    el "You know, here's a thought, though. Have you heard about the old camp?"
    me "No."
    show el laugh pioneer with dspr
    "Syroezhkin glowed."
    el "Well, here's the big secret... there's an abandoned bunker under this camp. I think you might find the right plug there!"
    "I snickered skeptically."
    me "And this bunker is just plain abandoned?"
    show el normal pioneer with dspr
    el "Well…"
    "Unsurely stretched out Electronik."
    el "Almost nobody knows about it. Shurik and I were going on an expedition there last week, but we had to postpone it because of the storm."
    me "And how did you find out about it?"
    show el grin pioneer with dspr
    el "Military secret!"
    "With a sly look the cyberneticist threw in."
    show el sad pioneer with dspr
    "But when he met my stern gaze, he bowed his head again."
    el "Well, there are such rumors in our camp. And no one knows how to get there."
    th "Oh, I love that kind of problem!"
    th "Go there, I don't know where, bring this, I don't know what. Brilliant!"
    me "Sounds dubious. Maybe there's still a way to make a charger out of the materials at hand?"
    "Electronik glanced at his watch again."
    el "I'm not sure..."
    show el smile2 pioneer with dspr
    el "How about this: if you don't find anything in the bunker, come back tomorrow morning - we'll figure something out!"
    "He's blatantly trying to get me to leave."
    "Not to say that Syroezhkin was obliged to take care of my problems, but resentment still rolled up to my throat."
    th "I wonder where he's going in such a hurry."
    dreamgirl "I'll let you in on a secret: most people have social contacts. Do I have to explain what that is, or can you remember the definition from Wikipedia?"
    dreamgirl "He's got a date, you jerk!"
    th "Yeah, sure. Just wait for him to build an effeminate robot..."
    "However, I never found a convincing argument to get Electronik to postpone his date and throw all his energy into the task of charging, so I politely nodded and walked out onto the porch."
    stop music fadeout 2
    $ alt_pause(1.5)
    play sound sfx_close_door_1
    scene bg ext_clubs_sunset_7dl with dissolve
    play music music_list['dance_of_fireflies'] fadein 2
    play ambience ambience_camp_center_evening fadein 1
    "It was beginning to get dark outside."
    th "I wish I knew where this old camp was..."
    "The easiest thing would have been to go back to the clubs and check with Electronik, but just the thought of going back made me cringe."
    "Not that I was so afraid of appearing clingy, rather the opposite: I feared that from such an excess of attention Syroezhkin would suddenly decide that we were friends now."
    "Well, I wouldn't want that, because with his habit of sticking his nose in, my legend of a gift from some mysterious acquaintance would quickly fall apart."
    th "I'll find out where this old camp of yours is. Or I'll find someone who does!"
    "Toward the gate, looking around, strode three boys of Ulyanka's age."
    "Without a second's hesitation, I moved toward them."
    me "Hey, kids! Help an old man, if you please!"
    show dn normal pioneer
    show tn normal pioneer at right
    show al dontlike pioneer at left
    with dissolve
    "They reluctantly turned around."
    show dn dontlike pioneer with dissolve
    "The shaggy kid who walked ahead of the trio looked at me strangely, and in the red sunlight his eyes seemed just as red."
    dn "What do you want?"
    "He asked with ill-concealed irritation."
    me "Have you heard anything about the old camp?"
    show tn dontlike pioneer
    show dn upset pioneer
    with dspr
    "The boys looked at each other."
    dn "What do you care?"
    me "That's where I have to go. It's a party assignment, you know?"
    "I nodded expressively toward the clubs."
    me "I need parts for the cybernetics club."
    show dn dontlike pioneer with dspr
    "The shaggy one squinted suspiciously."
    dn "So why don't you ask the club leader for directions?"
    me "He doesn't know himself."
    "Without blinking an eye, I lied."
    show dn unsured pioneer with dissolve
    "The boy hummed, thought for a moment, and then waved his hand toward the turnoff to the junior cabins."
    dn "When you get to the fence by the junior cabins, there's a gate that's open. There's a path behind it - go straight ahead."
    me "And then?"
    show dn normal pioneer with dspr
    dn "And then you'll see."
    hide dn
    hide al
    hide tn
    with dissolve
    "Threw the shaggy kid, and the boys continued on their way, oblivious of my existence."
    "The pioneer's vague instructions did not inspire hope, but there was no choice."
    "Besides, a half-forgotten sense of excitement, tickling my nerves and rousing my nervous system, was suddenly awakened."
    "Now I was no longer a grown-up Semyon trying to charge my smartphone for a few hours of solitary fun, but a pioneer Semyon who wanted to have an adventure on his ass while everyone else was busy doing things."
    th "No, these woods are obviously sprayed with something illegal to use, possess and distribute!"
    th "I know in my brain that I won't find any wire in this time, but I want to see the bunker!"
    stop music fadeout 2
    $ alt_pause(1)
    scene bg ext_backroad_sunset_7dl with dissolve
    play ambience ambience_forest_evening fadein 1
    play music music_7dl["nowyouseeme"] fadein 1
    "I successfully made it to the gate, encountering on the way only a handful of kids playing classics near one of the cabins."
    "If any of the counselors were watching them, they were doing so sitting in the bushes in camouflage."
    "Behind the fence the promised path was revealed, and I walked briskly into the woods."
    "Night was getting ready to fall, so there was little time to find it."
    th "I wish I knew how far is the camp..."
    stop ambience fadeout 1
    scene bg ext_path_night with fade3
    play ambience ambience_forest_night fadein 1
    $ night_time()
    "Once again I seriously regretted that in four days I had not learned exactly nothing about this place."
    th "Okay, geography is too suspicious to ask questions about, but legends like that bunker are a normal interest for a person who came to the camp for the first time."
    th "But on the other hand, how would I know about it?"
    th "Would I have sat down with a certain Slavya in the canteen and asked her where I could see the ghost of the camp counselor who hanged herself from unrequited love?"
    th "I'm too old for that sort of thing. That's the kind of stuff the old boys feed to twelve-year-olds, not to big-headed kids who have to be in the army in a year."
    "Although, there were worse stories in the army than the undead counselors and the abandoned bunkers."
    scene bg ext_path2_night with dissolve
    "It got dark fast, and the excitement quickly gave way to the quite rational thought that it was time to go back."
    th "That damn old camp isn't going anywhere overnight, and the bunker certainly isn't..."
    th "If it's even there."
    th "What about it?"
    "But my innate stubbornness wouldn't let me abandon my idiotic scheme halfway through."
    "Cursing and stumbling over dry branches, I continued my pointless and merciless journey toward my semi-mythical goal."
    "Suddenly something strange, foreign glimmered ahead - too bright for the night forest, albeit flooded with bright moonlight."
    dreamgirl "Yay, a corpse of a counselor!"
    dreamgirl "We have enough room in our inventory to take it, don't we?"
    stop music fadeout 4
    stop ambience fadeout 4
    "But the strange object was only a concrete slab."
    "And behind it there was another, and another..."
    scene bg ext_old_building_night_moonlight with dissolve
    play music music_list["sunny_day"] fadein 1
    play ambience ambience_forest_night fadein 1
    "And so I, like Ellie on the yellow brick road, walked out along the concrete slabs toward the dilapidated barracks."
    "The sight, it must be noted, was eerie - a two-story building surrounded by an overgrown playground looked like the kind of place where horror heroes definitely shouldn't go, lest they die a stupid and painful death."
    "However, it was foolish to expect a place called “old camp” to look like an amusement park."
    play sound sfx_open_metal_hatch
    "Somewhere in the distance a swing creaked, and I flinched involuntarily."
    "It was as if the temperature had dropped five degrees, and the night sounds of the forest had increased dramatically in volume."
    th "Though I realize that the mystical devilry exists only in my sick imagination..."
    th "But that makes it even scarier!"
    play sound sfx_wind_gust
    "The sight of the abandoned barrack in the ominous moonlight finally buried what was left of my enthusiasm, though I searched frantically for objective reasons to get away from the place."
    "Fortunately, the reasons were plentiful."
    th "It's almost bedtime, I don't want to get a kick in the teeth from my dear squad leader."
    th "And what am I going to find in this darkness? Without a flashlight, my chances of finding the famous bunker are slim to none."
    th "And anyway, I don't want to break my leg here..."
    play sound sfx_owl_far
    with vpunch
    $ alt_pause (0.3)
    dreamgirl "We got it already!"
    dreamgirl "Get back to camp before the ghost of the counselor comes out to get some air."
    th "Who «we»? I'm the only one here..."
    th "Ay, go to hell!"
    scene bg ext_path2_night with dissolve
    show bg ext_path2_night at running with dissolve
    play sound sfx_run_forest
    "I sighed irritably, and I turned and raced toward the camp, a little faster than I wanted to."
    "I'm sick of making excuses for my schizophrenia, though."
    th "That's who's not going to tell anyone anything anyway!"
    stop music fadeout 3.5
    stop sound fadeout 2
    scene bg ext_houses_night_7dl with joff_r
    play ambience ambience_camp_center_night fadein 1
    pause(0.5)
    "When I got to camp, the younger squads were scurrying back and forth, slamming the cabin doors loudly."
    "Fortunately, none of their squad leaders paid any attention to the errant pioneer, who clearly stood out from their charges."
    th "So mission accomplished: I'm in camp."
    th "Now - to sleep before I go somewhere else!"
    $ counter_mt_7dl -= 1
    $ counter_us_7dl -= 1
    $ counter_me_neu_answers = 1
    stop ambience fadeout 2
    return

label alt_day4_me_neu_map_admin_house1:
    play ambience ambience_camp_center_evening fadein 2
    play music music_list["smooth_machine"] fadein 3
    $ renpy.show("bg ext_admins_day_7dl", what = Desat("bg ext_admins_day_7dl"))
    with dissolve
    "At the administration building I slowed down, looking around."
    th "In all four days at camp, I never once saw anyone enter or leave this building."
    th "And why wasn't I even sent here the day I checked in? Wasn't I supposed to sign papers or something?"
    dreamgirl "And how many documents did you sign before you came of age, dumbass?"
    dreamgirl "That's the kind of thing parents do, and the pioneers have only one concern: getting to the canteen on time."
    th "But in that case, who signed the papers for me?"
    play sound sfx_open_door_strong
    show bb normal casual with dissolve
    "The iron door of the building creaked open, and a middle-aged man in a light-colored shirt and linen pants stepped onto the porch."
    "He reached out and covered his eyes with the palm of his hand, like a visor, looking somewhere in front of him."
    "I'd never seen him before: not in the canteen or on the ruler. But judging by his clothes, he wasn't some kind of a laborer."
    "It was the camp director himself standing in front of me."
    th "I wonder if they deliver food directly to his office."
    "Oddly enough, that was the only thing that interested me."
    "I regarded him indifferently, though in the old days such an important figure would have sent a tangible chill down my spine."
    "And the director finally noticed me, and nodded politely."
    bb "Semyon, I presume? We've been waiting for you, we thought you wouldn't make it."
    "Now I finally flinched - as even the most exemplary pioneer should when suddenly confronted by his superiors."
    th "How does he even know my name?"
    dreamgirl "And you think there's a whole bunch of you in the middle of the shift, falling on his head?"
    th "Makes sense. But it's still kind of weird..."
    me "Mm..."
    "I hesitated, not knowing what to do in such a situation."
    "On the one hand, the director didn't ask me any question, but on the other, ignoring him would have been extremely impolite."
    show bb smile casual with dspr
    "But he suddenly smiled cheerfully, obviously sensing my confusion."
    "And that smile struck me as more of a bad sign than a good one."
    bb "You're not doing anything, are you?"
    me "Actually, I'm..."
    bb "Come in for tea. Tell me how your... acclimatization is going."
    th "What?!"
    play sound sfx_open_door_2
    "I really wanted to believe I'd misheard, but the director swung the door to the building open with an inviting gesture."
    "Some sixth sense literally shouted that I should deny it with all my might and get out of here, but I froze in a stupor."
    th "I wonder if it's okay to drink tea with the principal here."
    dreamgirl "Relax, man. He's offering you tea, not candy and puppies, so his interest in your person is purely platonic."
    dreamgirl "And let's be honest: you're pretty old..."
    "There was still not a soul around, so the hope of a miraculous rescue by a counselor or at least someone I knew was melting by the second."
    th "Okay, don't panic - it's just a conversation with a nice uncle. Nothing bad is going to happen, right?"
    dreamgirl "Yeah, especially if you manage not to slip up and make it look like you're no pioneer!"
    "The split personality chuckled maliciously, and I seriously wished I could give him the middle finger."
    stop music fadeout 3
    "I stepped onto the porch and staggered after the principal."
    $ alt_pause(1)
    scene bg int_admins_7dl with dissolve
    play sound sfx_unlock_door_campus fadein 1
    play ambience ambience_int_cabin_evening fadein 3
    play music music_list['you_won_t_let_me_down'] fadein 2
    "The administration building smelled of dust and sun-heated paint on the wooden window sills."
    "The director led me down a narrow corridor past closed doors and booths with faces of people unknown to me."
    "At one door the director stopped, and I furtively glanced at the sign."
    th "“Trofimov.A.M. Camp director”"
    th "They should've at least written his name fully!"
    play sound sfx_unlock_door_campus fadein 1
    $ alt_pause(1)
    scene bg int_chief_office_rain_7dl with dissolve
    "As I slipped into the office, I looked around cautiously."
    "The director's office was... the director's office. Cabinets of files and a heavy desk as an island in this sea of bureaucracy."
    th "It must be no fun to sit around fiddling with paperwork while outside every second someone is running around, laughing and generally enjoying free life and plenty of free time."
    dreamgirl "I guess for consolation he makes everyone paint benches every week."
    dreamgirl "Or peeling potatoes. You never know what fetishes he has!"
    show bb normal casual with dissolve
    bb "Take a seat."
    "The director nodded to a chair across from his chair, and I dutifully landed on the edge."
    "The chief himself threw a boiler into a jar of water and pulled out two cups and a crumpled cardboard box of sugar from an inconspicuous cabinet."
    show bb smile casual with dspr
    bb "How do you like it here? Aren't you homesick?"
    "The question sounded most innocent, but I tensed. Fingers of my hand involuntarily clenched on the edge of the table."
    me "I haven't really missed anything yet."
    th "I wish I had something else to miss!"
    th "Or who."
    th "But I'm not going to miss her for sure!"
    bb "That's good. There's nothing for a young body to do in the city this time of year."
    me "Excuse me, how..."
    show bb normal casual with dspr
    $ meet('bb', "Alexei Maximovich")
    bb "Alexei Maximovich."
    "He scattered the brew in the cups and poured water over it - suspiciously fast-boiling."
    bb "Our kettle is broken, so we boil it the old-fashioned way. But, in my opinion, it tastes even better that way."
    "He put the cup in front of me and sat down across from me, watching my face with interest."
    me "Thank you."
    "I said and pulled the mug toward me."
    th "He didn't slip anything in there, did he?"
    dreamgirl "I bet on the bromine. Your bets?"
    show bb smile casual with dspr
    bb "So, Semyon, so you like it at camp?"
    th "I don't remember saying that, but..."
    me "Yeah. It's fun. And the people are nice."
    th "I guess that's what a decent pioneer should say."
    th "Maybe with a little more enthusiasm in voice, but let's chalk it up to excitement - it's not every day you get invited to small talk with such important people!"
    bb "Did you get along with your peers? After all, you arrived quite late, fitting into an already close-knit group - not an easy task!"
    th "With Olga? Well, with varying success."
    th "Yes, and if there was still some team here, there's nothing to talk about cohesion!"
    me "Well... I seem to have been well received."
    "Alexei Maximovich nodded satisfied."
    show bb normal casual with dspr
    bb "Don't think I'm just questioning you."
    bb "We've had late pioneers come to us before, we have experience."
    "He put subtle pressure on the word “late”, and the cup in my hand treacherously shook."
    bb "We've had all kinds of accidents, including unpleasant ones. That's why it's so important to me to know that you're okay."
    "The director took a sip of his tea and looked thoughtfully into the distance."
    bb "Camp is an amazing place, I'll tell you a secret. It's like a resting place, but it's also like a whole life."
    bb "Some people just live it every day, accumulate impressions, make friends and sometimes enemies."
    bb "They don't think about the fact that it doesn't last forever, and they enjoy life."
    bb "And some people take things more sharply, closer to the heart than they should."
    "He grimaced, like he remembered something unpleasant."
    bb "But all good things come to an end one day. This shift, for example, is coming to an end, and soon everyone will be going home."
    bb "So enjoy this carefree time as much as you can, and if possible, don't do anything stupid!"
    "I squeezed a smile out of myself, as befits a young man of my years after a touching senile admonition."
    stop music fadeout 0.7
    show bb serious casual with dspr
    pause(0.1)
    play music2 music_7dl["dead_silence"] fadein 1.5
    "But the director didn't smile back - his face suddenly became extremely serious, and he looked me straight in the eye for the first time all evening."
    show bb serious casual with dissolve
    bb "I'm not asking you to do much, Semyon. Just keep the ages of your squadmates in mind."
    bb "And try to keep your head clear of any important questions."
    "It no longer sounded as sweet and friendly as all his past speeches about carefree summers and happy childhoods."
    "It wasn't even a subtle hint."
    "A direct instruction to stay out of the way."
    th "Here we are..."
    "I stared at Alexei Maximovich, unable to move. My throat was seized with icy terror."
    th "He knows!"
    th "He knows who I am!"
    play sound sfx_head_heartbeat
    "My heart was pounding so frantically that I could almost feel it in my ribs."
    "My body tensed, ready to snap and run in any direction I wanted, just to get away from here."
    "But my gut told me it was too late."
    "That there were already uniformed men standing under the door, just waiting for the conditioned signal to grab the fugitive."
    dreamgirl "And now the ominous lightning will flash outside the window!"
    stop music2 fadeout 1.5
    play sound sfx_thunder_wood
    show bb normal casual
    with flash
    stop sound fadeout 2.5
    dreamgirl "Wheeeee!"
    "But the director sipped from his cup as if nothing had happened."
    show bb smile casual with dspr
    bb "Well, I'm glad you're having fun at camp."
    "His tone was friendly again, as if a moment ago he wasn't trying to intimidate me at all."
    "He seemed to have lost all interest in me, and it was the perfect moment to retreat."
    "I pushed the nearly untouched cup aside."
    me "Thanks for the tea, but I have to go. Olga Dmitrievna asked me..."
    show bb normal casual with dspr
    "The director nodded understandingly."
    bb "I'm not holding you. Enjoy the rest of your vacation!"
    hide bb with dissolve
    "After muttering something unintelligible in farewell, I dashed out of the office and rushed to the exit. I needed some fresh air."
    play ambience ambience_camp_center_evening fadein 2
    $ renpy.show("bg ext_admins_day_7dl", what = Dawn("bg ext_admins_day_7dl"))
    with touch
    $ alt_pause(1)
    scene bg ext_square_sunset with dissolve2
    play music music_7dl["nowyouseeme"] fadein 1
    "It wasn't until I reached the square that I allowed myself to catch my breath."
    th "What the hell was that?"
    dreamgirl "Tea. Black, I think."
    dreamgirl "And no sugar. You must have been too embarrassed to put it in."
    "I didn't share the fun of my schizophrenia at all."
    th "If he knows who I am and how I got here..."
    th "Who else knows?"
    dreamgirl "What makes you think he knows?"
    dreamgirl "I bet that was such veiled advice to think about contraception!"
    th "What contraception? I haven't even made friends with any girls, let alone any other things?"
    dreamgirl "Well I'm sorry, I don't think there's a note in your file about autism."
    dreamgirl "Or maybe you're one of those? I'm not implying anything, but Syroezhkin seems to be available..."
    th "Screw you!"
    "The altercation with the inner voice and the fresh air calmed me down a bit."
    "I sat down on the bench and exhaled."
    "Here in the square, where everything had already become familiar, the headmaster's office and that strange conversation seemed something unreal."
    "But the sticky tang of fear was darkening the warm summer evening considerably."
    th "Okay, the girls are understandable..."
    th "But what were the important questions he was talking about?"
    scene bg ext_square_sunset:
        align (0.57, 0.55)
        linear 2.0 zoom 2.0
    "There were many questions, except that I couldn't formulate any. My wandering gaze stopped at the pedestal."
    th "Genda, for example. Who is he, anyway?"
    th "Former camp director? That's a lot of honor to put up a monument!"
    th "Local Party official? I don't remember if the Soviet Union used to put up monuments to just anyone."
    th "And you can't ask anyone - they'll take you to Viola, and then..."
    "I shuddered." with vpunch
    "There was, however, one way to find out without drawing too much attention to myself."
    "Rising from the bench, I moved toward the library."
    stop music fadeout 3
    stop ambience fadeout 1
    $ alt_pause(1)
    scene bg int_library_night2 with joff_l
    play music music_list["your_bright_side"] fadein 2
    play ambience ambience_library_day fadein 2
    "The library was open. Zhenya, contrary to my expectations, was not asleep with her face in the table, but was sitting with a magazine of some kind."
    dreamgirl "Eh… Not «Playboy»."
    dreamgirl "But that would've been interesting."
    "The librarian grudgingly glared at me over the pages."
    show mz bukal glasses pioneer with dissolve
    mz "The hell are you doing here?"
    th "She's being soooo nice!"
    th "No wonder it's empty all the time."
    if alt_day4_me_neu_mz_newspaper:
        th "Even though we're not strangers anymore..."
    me "Zhenechka, sweetheart, help me out!"
    show mz angry glasses pioneer with dissolve
    th "I knew it would work!"
    "Blushing with anger, the girl jumped up from the table."
    mz "I'm not your..."
    me "Since you're up anyway, help me find something on recent history. At least I'll prepare a little for the exams, anyway, this camp is green with boredom."
    mz "Look it up yourself, you're not a kid!"
    "I clucked my tongue."
    me "Uh-huh, let's put it that way. Sleeping on the job, neglecting duties, being rude to visitors..."
    me "Shall I continue?"
    pause(0.3)
    hide mz with moveoutright
    "Grudgingly muttering to herself, Zhenya pushed back her chair and headed for the far shelves."
    th "At least some pluses from this party husk - the right books are always at my fingertips. I can hardly imagine having something like that in a modern camp."
    show mz bukal glasses pioneer with dissolve
    mz "Here."
    hide mz with dissolve
    "I struggled to grasp the weighty book, which almost flew into my face."
    "If Zhenya was disappointed, she didn't show it."
    dreamgirl "Add “negligent treatment of government property” to your complaint."
    me "Thank you from the bottom of my heart."
    "I bowed low and hurried away before she threw something else at me."
    stop music fadeout 3
    "Throwing off my sandals and climbing into a chair with my feet, I opened the table of contents."
    $ set_mode_nvl()
    play music music_list["trapped_in_dreams"] fadein 3
    $ alt_pause(3)
    play sound sfx_7dl["page_turning"]
    "Chapter I. Nazi Germany's attack on the USSR. The collapse of the Blitzkrieg."
    "§1. On the eve of the war."
    "§2. Beginning of the war."
    "§3. The country mobilizes."
    "§4. The battle for Moscow."
    "§5. The tragic days of 1942."
    $ set_mode_adv()
    th "Nothing unusual so far. Same familiar story."
    "I ran my eyes to the end of the table of contents."
    $ set_mode_nvl()
    play sound sfx_7dl["page_turning"]
    "§22. Foreign Policy of the USSR."
    "§23. Tendencies and contradictions of socio-economic development."
    "§24. Contradictions in the political and spiritual life of society."
    "On the Road to Renewal."
    $ set_mode_adv()
    th "This way I won't find anything until morning. Gotta change my approach."
    "I've reached the subject index."
    "Genda, Ulyan Igorevich 111."
    th "What a name…"
    th "It would be funny if Ulyana's ideological-party parents named their daughter after this character!"
    "Opening the right page, I ran my eyes over the text."
    "There was a little footnote at the end of the chapter, and from a faded black-and-white photograph Genda was looking at me sternly."
    $ set_mode_nvl()
    "Prim. Ikari, Gendo (1899 – 1946) (second. Genda, Ulyan Igorevich (1946 — present day))"
    "Japanese scientist who led a Japanese-Soviet group that investigated experimental technology to repair the damage left by the war."
    "In an unsuccessful experiment, Ikari was erased, and the research was halted by agreement between the Soviet and Japanese authorities."
    $ set_mode_adv()
    "I stared at the page in confusion. I reread it again to make sure my eyes weren't deceiving me."
    th "What do these “prim.” and “second.” mean? What do you mean - was erased?"
    "All that was clear was that nothing was clear. I turned the page back and began to read the beginning of the chapter."
    $ set_mode_nvl()
    "§15. Restoration of the Destroyed Economy."
    "State of the national economy. Transferring it to a peaceful course."
    "The damage done to our country by the aggressors was enormous. During the war the Soviet Union lost a third of its national wealth."
    "Many of the country's largest enterprises were destroyed."
    "The Soviet state began to rebuild them during the war, as territories occupied by the enemy were liberated."
    "But it was only after victory that reconstruction became a priority."
    nvl clear
    $ set_mode_adv()
    show mz bukal glasses pioneer with dissolve
    mz "The library is closing."
    "Zhenya squeaked over my ear. I shrugged."
    th "Fine. I'll finish it before I go to bed!"
    me "Put that book on me, and I'll go."
    show mz angry glasses pioneer with dissolve
    mz "I won't write it down. You don't have a library card."
    me "So make one!"
    show mz rage glasses pioneer with dissolve
    mz "Are you deaf?"
    mz "The library is closing! Right now!"
    th "Damn you, you grumpy hag!"
    hide mz with dissolve
    "After giving the librarian the most murderous look I could muster, I defiantly slammed the book shut and shoved it to the nearest shelf."
    "I hoped she didn't notice that I'd furtively bent the corner of the page during the spectacle."
    th "I'll finish it tomorrow. I don't have anything important to do..."
    "Once again I bowed to the disgruntled Buzzer and hurried out of the library."
    "And now that there's no fun left to be had, it's time for bed."
    $ counter_mt_7dl -= 1
    $ counter_us_7dl -= 1
    $ counter_me_neu_answers = 1
    scene bg int_library_night with dissolve
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day4_me_neu_map_boat_station1:
    scene bg ext_boathouse_sunset_7dl with dissolve
    play ambience ambience_boat_station_day fadein 5
    "It's just a pier."
    "You can sit here or you can go on."
    menu:
        "Relax on the pier":
            $ alt_day4_me_neu_boat = True
            play music music_list["reflection_on_water"] fadein 3
            "After thinking about it for a while, I decided to have an evening alone with the waves and the sunset."
            "Not a bad option, if you put it that way."
            "Dropping my shoes and socks, I set them by the rail and sat down on the edge of the pontoon and dipped my feet into the water."
            "The water was warm, hardly felt."
            "The water was healing; it took away unnecessary, dirty memories, leaving perception cleanly washed away."
            "One could imagine that someone needed you."
            "That you walk day in and day out."
            "The same routes."
            "You see, there are things that you are powerless to influence, and some call these events meta, some call them inevitable milestones."
            "And you call it life."
            "And if you live from day to day..."
            "Drenched in rain collecting water, you put the dried, no man's, forgotten home flowers left behind after the owners moved away, under the spray."
            "You help an old vendor lift a keg of kvass or a scoop of ice cream that she just can't lift."
            "You give a homeless dog half your dinner."
            "And to a family of beggars begging for a small penny for education, you empty your pockets of all the cash, leaving yourself only for travel."
            "You live."
            "You become a part of life."
            "And methinks."
            "And one day the dog will give birth to puppies, a pretty girl will take the place of the grandmother ice cream maker, and six months later you'll be modestly married in the local registry office."
            "And in the pauper family, one of the girls will be missing, the one, the battered one, with the quivering pupils."
            "And there will be a tingle in your chest from the wrongness of what is happening."
            voice "Mama, look, they made uniforms for us!"
            "The voice is familiar, but... You've heard it a thousand times, telling you 'bless you...'"
            "And you turn around and see her, clean, washed, in her uniform and with her satchel."
            "She's going to first grade today."
            "And you realize that you are life now."
            "Because one is not rich if one has a lot of money, but if one can give a lot."
            "And you don't have to get anything in return."
            "You're already getting a lot more, something no money can buy."
            "Emotions."
            "You are witnessing the beginnings of fragile happiness."
            "So live."
            show blink
            "I don't know how long I meditated like that before I was brought back to sinful ground by a strange sound."
            "The boards creaked behind me, and I became wary."
            $ persistent.sprite_time = "night"
            $ night_time()
            scene bg ext_boathouse_night
            show blackout_exh2
            show un modern shade close
            show unblink
            "A short silhouette sneaked past me to the boats, and only a pair of ponytails revealed its owner, Lena."
            "With the dexterity of a skilled hostess, in a few seconds she opened the lock on the chain and tossed a bundle under the can, which turned out to be oars."
            "Moved into the watercraft herself."
            hide un with dissolve
            if persistent.alt_binder and dr and (alt_day2_date == '') and (counter_dv_7dl == 0) and (alt_day3_dj != 'dv') and (alt_day1_sl_keys_took in (1, 3)):
                "I watched in silence as she settled into the boat, and suddenly something foreign, phantom, a prick of conscience, belonging not to me but to someone else, surged in my chest."
                th "You can't let a girl go alone on such a dangerous journey!"
                "Said someone else's forgotten voice in my head."
                show bg ext_boathouse_alt_night_7dl with dissolve
                "And I picked up my sandals, like on autopilot, and slapped my bare feet on the cold planks."
                show un surprise pioneer with dspr
                show un surprise pioneer:
                    linear 0.5 xpos 0.5
                    linear 0.025 xpos 0.505
                    linear 0.05 xpos 0.495
                    linear 0.05 xpos 0.505
                    linear 0.05 xpos 0.495
                    linear 0.025 xpos 0.5
                    linear 0.5 xpos 0.5
                "Lena flinched and almost dropped her oars as soon as she heard the noise."
                show un shocked pioneer with dissolve
                "She raised her head and stared at me with ill-concealed horror."
                me "Is there any room for me?"
                "I asked so calmly, as if it were normal for me - to break into personal space, and yet to impose my company on a person who clearly expected privacy."
                th "But why doesn't that seem wrong to me?"
                show un sad pioneer with dissolve
                un "I…"
                "The girl averted her eyes and shook her head."
                "I felt stupid."
                me "Sorry. If I'm unwanted..."
                show un shy pioneer with dissolve
                un "No, it's okay!"
                "Suddenly Lena blurted out, still studiously avoiding looking in my direction."
                "In the darkness, I could hardly make out the features of her face, but I was willing to bet the last percent of my smartphone's charge that it was crimson."
                "I really wanted to leave and not continue this parade of awkwardness I'd arranged, but retreating would have looked even more idiotic than my attempt to follow Lena."
                play sound sfx_boat_impact
                scene cg d5_un_boat_7dl with dissolve
                "So I stepped carefully into the boat and pulled the oars out from under the can, trying my best not to touch Lena in the process."
                me "Where are we going?"
                "Lena shrugged her shoulders indifferently. She still didn't look at me, studiously studying the glare of the moonlight on the water surface."
                th "Well, here we are..."
                "I pressed the oars - what else could I do?"
                "Lena was still looking at the water, and her face took on an almost peaceful expression."
                th "And she wasn't afraid..."
                if lp_un > 3:
                    th "It's not to say we haven't exchanged a word in those four days, but it's one thing to have a camp where you're always surrounded by people, but it's quite another to have a tiny boat in the middle of the water that cuts you off from safe territory."
                else:
                    th "Sailing for who knows where with a stranger she knows nothing about."
                    th "And with no way to escape at any moment - unless she's hiding from me a swimmer's degree."
                th "And I'm pretty sure no living soul knows about her sudden water trip. I doubt very much that even the careless Miku would let her neighbor go out into the unknown at night."
                th "But who can tell her, this delicate artist's soul?"
                th "Maybe she's just hunting for references of the night scenery. You never know what unexpected angles might come from the water."
                scene bg ext_island_night:
                    align (0, 0.6)
                    zoom 2.0
                show blackout_exh2
                with dissolve
                "I looked around. Over the black silhouettes of the trees the warm lights of the camp lanterns spread faintly, and the thickets of grass by the water were an icy blue in the moonlight."
                "And it almost made me feel bad that I could never keep those colors on canvas. This contrast of the man-made, alien to these landscapes, and the real, beyond human control."
                th "Or maybe it's a kind of escape. Here, on the water, the camp ceases to seem real."
                th "It's like we weren't there at all. It's as if all that really matters is the boat gliding down the river, the splash of water, and the distant, distant whoosh of owls somewhere deep in the woods."
                th "And the moon, which serves as our beacon in the pitch black of night."
                dreamgirl "Do you speak Russian well?"
                th "Eh?"
                "An inner voice burst into the stream of consciousness so suddenly that for a second I stopped paddling."
                dreamgirl "Ask her why the hell she wanted this adventure. She's sitting across from you, if you haven't forgotten."
                "I got confused. I liked guessing much better - that way I didn't feel awkward about our silence."
                "But Lena was the first to break the silence."
                show un normal2 pioneer with dissolve
                un "What were you doing on the pier?"
                me "Well... sitting around."
                "Explaining why I was doing that seemed like an impossible task."
                show un smile pioneer with dissolve
                "Lena chuckled."
                un "You're weird!"
                me "You're one to talk!"
                "I bit my tongue, afraid that my answer would offend the girl, but she seemed to cheer up more than ever."
                "Now it wasn't the same Lena who flinched at every rustle."
                "It was a new Lena, unknown to me, who was studying my face with curiosity and was not the least bit embarrassed to catch my return look."
                if not alt_day2_us_escape:
                    me "Are these boats guarded at all?"
                else:
                    me "There's a local watchman here."
                "As if by accident I threw."
                show un smile2 pioneer with dissolve
                un "The boatman is already asleep at this time. So if we dock very quietly, he's not likely to find out about our sortie."
                "Judging by the confidence with which she spoke of it, such an adventure was not the first time for her."
                me "What a horror!"
                "I clucked my tongue condemningly, struggling to suppress a smile."
                me "You won't believe this, Mistress Squad Leader, but we have a vicious rule breaker in our camp!"
                un "Why is your first thought about snitching, Semyon..."
                un "We're in the same boat now!"
                show un laugh pioneer with dissolve
                "After looking into each other's eyes for a second, we laughed quietly."
                "And once again I caught myself thinking that everything was too easy. The sleeping boatman, the lousy castle, the invitation to join, and even this conversation."
                "It all felt so right and regular that it felt like something...alien."
                stop music fadeout 4
                "Because it simply couldn't happen in my life."
                scene cg d5_un_boat_7dl with fade2
                play music music_7dl["breath_again"] fadein 3
                "Lena dangled her hand over the side and began to trace patterns on the faint waves with her fingers."
                "I couldn't help but marvel at the virtuosity of her hand."
                th "They say that the most beautiful fingers are given to pianists. But there is hardly more movement and life in them than in the fingers of an artist."
                scene bg ext_island_night:
                    align (0, 0.6)
                    zoom 2.0
                with dissolve
                show un smile3 pioneer with dissolve
                un "And yet, why were you all alone?"
                un "Wasn't there anyone you wanted to spend the evening with?"
                "She tilted her head sideways, smiling slyly. I felt my mouth dry up."
                th "She's not... referring to herself, is she?"
                show un smile pioneer with dissolve
                un "There is, after all, Slavya. She'll always think of something to do, don't you doubt it!"
                th "Ye-e-e-ah, she's sure to have an extra broom!"
                un "She's kind, and she's got a heart of gold. Just like her braids."
                if not (('sl' in alt_day3_dancing1) or ('sl' in alt_day3_dancing2)):
                    un "You could just ask her to dance - I'm sure she'd be very pleased."
                me "Mmm... I'll think about it."
                th "And why is she suddenly matchmaking me? I'm not completely hopeless: I don't throw myself at people, I don't sit in clubs all day, I talk quite coherently..."
                show un smile2 pioneer with dissolve
                un "And Miku? I think it's impossible not to like her."
                if alt_day4_me_neu_volley:
                    un "You should see how she literally glows on the inside when she goes on stage!"
                else:
                    un "Have you seen the way she was doing the concert? I mean, she literally glows from the inside out when she's on stage!"
                un "Only she's very lonely. I can't split into two clubs to talk to her more, but you could stop by and see her."
                me "I'm kind of a music guy... I like to listen more than perform, to be honest."
                show un grin pioneer with dissolve
                "Lena laughed."
                un "Then you should go to Alisa! She can't live without music!"
                un "She has a complicated character, of course, but I think you'll get along. She only seems prickly, but in fact she's almost kinder than Slavya."
                show un laugh pioneer with dissolve
                "The girl made scary eyes and half-whispered:"
                un "Not a word to her about what I said! I planned to live to the end of this shift."
                "I couldn't stand it and laughed softly. This new Lena made it very easy for me."
                "This Lena was taking away all my anxiety, and next to her I felt like a living person and not a vestige of society that no one would ever get their hands on."
                "But a strange sensation kept me awake."
                "A feeling of deja vu."
                th "Why does she even tell me about the other girls?"
                th "I didn't even ask. And I certainly didn't show any interest in anyone at camp."
                stop music fadeout 3
                me "What about you?"
                "I asked without any hindsight."
                $ volume(1.3, "music")
                play music music_7dl["not_alone"] fadein 3
                show blackout_exh2
                show un sad pioneer
                with dspr
                un "Me?"
                "Lena flinched. All her gaiety vanished in a flash, and the familiar Lena, the one I knew at camp, was looking at me."
                "Slightly frightened, embarrassed, and ready at any moment to snap and run away where no living soul could find her."
                "And I admired this Lena with a kind of mad pleasure."
                "Such a Lena was much dearer to my heart."
                show un smile pioneer with dissolve
                un "Well, I…"
                un "I'll always be ready to give my friendly advice!"
                "She smiled, and a sickening feeling of guilt squeezed my throat with sticky fingers."
                "Guilt for opening my mouth at all and asking a question I didn't want an answer to."
                th "But why do I even care?"
                th "What's the big deal, a bad joke. Who knew it would hurt her so much?"
                scene cg d5_un_boat_7dl
                show blackout_exh2
                with fade2
                "Lena fidgeted nervously, as if trying to take up as little space as possible."
                "She pulled her hand out of the water and glanced at her watch, squinting blindly."
                un "Lights out soon. We have to get back."
                "I nodded silently and picked up the oars, letting the current carry us back."
                "To the camp, where our walk will be but a dream. An obsession quickly washed away by the daily grind, the bright sunshine, and the children's laughter."
                "To a camp where that cheerful Lena who chatted casually with some loser never existed, as if the two of them could have anything in common."
                "We reached the dock in complete silence. Lena was looking up at the night sky with her head slightly thrown back, while I was drilling the bottom of the boat with my eyes."
                th "I'd rather have spent my evening in complete solitude."
                th "The devil dared me to go near her!"
                dreamgirl "Try to stop getting worked up and start enjoying the moment."
                dreamgirl "What a nice evening!"
                "And that was the biggest oddity of an already unreal evening."
                "My schizophrenia has never cheered me up. I'd even say its primary function was the opposite."
                th "Is this your new way of bullying?"
                dreamgirl "No. You're the one mocking yourself."
                dreamgirl "Or maybe your girlfriend is right and we just need to find you a date."
                th "She's not my girlfr…"
                show bg ext_boathouse_alt_night_7dl with fade
                "The boat docked with a quiet thud."
                "I climbed out onto the wooden planking under the mournful splash of the water and held out my hand to Lena. She barely touched it, as if my palm were a red-hot iron, and fluttered out onto the dock, stealthily adjusting her skirt."
                me "Do you need help carrying the oars?"
                show un serious pioneer with dissolve
                "Lena quickly shook her head."
                un "I can take it from here."
                hide un with dissolve
                "She turned away and leaned over the boat."
                un "But thank you for offering."
                "I heard a barely audible whisper."
                scene bg ext_boathouse_night
                show blackout_exh2
                with dissolve
                "I hurried to get out of here. There was too much weirdness in this place - more than I could handle."
                th "Home. To sleep."
                th "And preferably stop feeling."
                "But I knew in my heart that the latter was something out of the realm of the impossible."
                $ counter_mt_7dl -= 1
                $ counter_us_7dl -= 1
                $ counter_me_neu_answers = 1
                stop music fadeout 3
                scene bg ext_square_night with dissolve
                play ambience ambience_camp_center_night fadein 3
                "I had already reached the turnoff to the cabins when suddenly I was called out."
                play music music_7dl["out_of_painkillers"] fadein 5
                mi "Senechka!"
                th "You're the last thing I need right now!"
                show mi grin pioneer with dissolve
                "Reluctantly, I turned around and stared expectantly at Miku, galloping happily toward me. She had an impressive-sized case in her hands."
                mi "Senechka, can you help me? I wouldn't ask you, but it's really, really urgent!"
                me "Well, since it's really-really..."
                show mi happy pioneer with dspr
                "The girl immediately gave off the most charming smile she could."
                mi "Will you drop my costume off at my cabin? I'd leave it at the music club, but I'm such a mess that if I leave it there I won't be able to find it by the next concert, and then I'll have to perform in one of those horrible costumes from the warehouse..."
                show mi shocked pioneer with dspr
                me "Okay. Give it here."
                "Abruptly I cut off her flow of speech."
                th "Maybe in another situation I wouldn't mind chatting with Miku, but my social resources are exhausted for today."
                show mi dontlike pioneer with dspr
                "Miku became resentfully silent and slipped the case into my hands."
                show mi normal pioneer with dspr
                mi "My cabin is over there! You have to go to the last row, turn left, and walk all the way to the end."
                me "And the number?"
                "I clarified just in case."
                mi "Thirteenth. I know you're a little afraid of it, that's what Lena told me when they checked us in..."
                show mi smile pioneer with dspr
                "I flinched and stared frightened at Miku, but the girl only smiled understandingly."
                mi "Don't worry, it's all silly superstition: Lena said this shift was definitely doomed, but nothing bad happened!"
                th "That's how it is!"
                if (alt_day2_convoy == 'un') or (alt_day2_mi_dinner == 1):
                    th "And what was I thinking when I said yes?"
                    th "About how cool it would have been to meet Lena nose-to-nose after she almost pushed me off the dock?"
                else:
                    "I remembered Lena's insistence on getting me off the pier."
                    th "Who knew I was going to get such a catch?"
                show mi upset pioneer with dspr
                "Suddenly Miku stepped toward me, stood on tiptoe, and whispered with the most serious look:"
                mi "What you should really be afraid of is the number “four”..."
                "I couldn't stand another half an hour of her chatter, and I didn't want to cross paths with Lena. I held out my hand with a martyred expression."
                me "Alright, give me the key, and I'll go. Lights out is just around the corner."
                dreamgirl "What, you won't even ask our star where she's rushing off to at this late hour?"
                th "It's none of my business. I have enough problems of my own."
                play sound sfx_keys_rattle
                "The key fell into my palm."
                show mi normal pioneer with dspr
                mi "Leave it on the table, and you can throw the costume on my bed."
                "I think Miku tried to bow, but she yanked herself back in time."
                show mi smile pioneer with dspr
                mi "Thanks a lot, Senya!"
                scene bg ext_house_of_un_night_7dl with dissolve
                play ambience ambience_ext_road_night fadein 3
                "After forcing out something resembling a friendly smile, I almost ran toward the unfortunate cabin."
                if (alt_day2_convoy == 'un') or (alt_day2_mi_dinner == 1):
                    "The lights weren't on, which meant Lena hadn't had time to take the oars out yet."
                else:
                    "The lights inside the cabin weren't on."
                scene bg int_house_of_un_night with dissolve
                play sound sfx_open_door_clubs_2
                play ambience ambience_int_cabin_night
                "With trembling hands I opened the door, skipped into the cabin without turning on the light, threw the costume on one of the beds, put the key on the table, and just as swiftly left the cabin."
                scene bg ext_house_of_un_night_7dl with dissolve
                play ambience ambience_ext_road_night fadein 3
                play sound sfx_close_door_1
                th "Now - to sleep, before some other extremely urgent task falls on me!"
            else:
                "A few seconds more, and the boat was silently out on the big water."
                "And to the series of mysteries of Sovyonok, I added Lena, who had run away to nowhere."
                "Marking this 'secret material' in my memory, I got up and headed home."
                stop music fadeout 3
                "I had great things waiting for me and a warm blanket."
        "Move on":
            "I don't think anything out of the ordinary is going to happen here."
            "With a shrug, I turned and left."
    $ volume(1.0, "music")
    stop ambience fadeout 3
    return

label alt_day4_me_neu_map_me_mt_house1:
    scene bg ext_house_of_mt_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 3
    "The cabin stood lonely, sad and abandoned."
    "A place where people go to sleep so they don't have to spend the night in the open air."
    th "Still, there are certain disadvantages to deputies, too."
    th "Olga never really lived here - as soon as she tried to relax, some Slavya would always find her."
    th "So the cabin was empty."
    stop ambience fadeout 2
    scene bg int_house_of_mt_backpack_sunset with dissolve
    play sound sfx_unlock_door_campus
    $ alt_pause(1)
    play ambience ambience_int_cabin_evening fadein 2
    "As I entered the cabin, I stopped at the doorstep."
    "Only now that I was in my own fortress, when I didn't have to rush off somewhere, did I realize how exhausting it is to be {i}fully involved{/i} in the life of a squad or a camp."
    "Little wonder that Olga was trying to shirk her duties by any means necessary."
    "But she wasn't here now."
    "She's probably run off to a wild beach somewhere behind the grounds, blazing a campfire, watching the sunset..."
    with dissolve
    "On the back of the chair was a surprisingly familiar navy blue backpack with a print of a footprint."
    "My «grizzly» from my reality… And why am I not surprised?"
    "As for the rest of the room..."
    "Effortlessly stifled worry reared its head again."
    th "It's a girl's house! {w}A girl's house is always full of surprises!"
    "I looked around the table"
    scene bg int_house_of_mt_backpack_sunset:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 1.0 zoom 1.25 xalign 0.5 yalign 0.65
    extend ", nightstand"
    scene bg int_house_of_mt_backpack_sunset:
        xalign 0.5 yalign 0.65 zoom 1.25
        linear 2.0 zoom 1.15 xalign 0.9 yalign 0.45
    extend ", shelves."
    scene bg int_house_of_mt_backpack_sunset:
        xalign 0.9 yalign 0.45 zoom 1.15
        linear 0.8 zoom 1.35 xalign 0.85 yalign 0.75
    "My attention was drawn to the very diary where Olga had written her notes on my first day here."
    th "Should I take a moment and look?"
    menu:
        "Of course I should look!":
            $ alt_day4_me_neu_mt_diary = True
            $ karma -= 20
            if alt_day3_dancing2 == 'me_2':
                $ counter_mt_7dl += 1
            if persistent.mt_7dl_good:
                $ counter_mt_7dl += 2
            "Grabbing the blue book in a leatherette cover, I pulled back my chair and sat down at Olga's side of the table."
            "And opened it."
        "Rummage through the backpack":
            $ alt_day4_me_neu_us_backpack = True
            show backpack at truecenter with dissolve
            "Not that I mind playing a little pervy maniac and going through the squad leader's things."
            "But not when anyone could walk in."
            "And there's no self-respect, either."
            "So let's do something a little more pressing."
            "Let's see what assets we have and what we can do with them."
            scene
            $ renpy.show("bg int_house_of_mt_sunset", what = Dawn("bg int_house_of_mt_sunset"))
            show backpack_tiny
            with dissolve
            "I sat down on the bed and pulled the backpack out into the light."
            "Not much had changed since the last time I wore it at home."
            "It was still the same triangular leech bag with one shoulder strap over the right shoulder, made of blue water-repellent fabric."
            "In the very center of the backpack was a print in the shape of a boot print, the emblem of the manufacturing company."
            "And, of course, the rubberized seams, airtight zippers, and other definitely-needed urban tricks without which carrying a couple of books and a tablet charger is unthinkable."
            "I opened the zipper and shook out the contents of the backpack on the bed beside me, making a cursory revision:"
            "Cards, a deck in a plastic box, one piece."
            "Knife-herder, popularly called 'Swiss' - one piece."
            "A roll of kapron cord and a bunch of different kinds of carabiners."
            "Universal non-extinguishable matches - a box, fishing hooks - six pieces in a plastic box, a shapeless piece of lead - for sinkers."
            "Two sets of keys."
            "Wallet - empty."
            if alt_day4_me_neu_date == 'mt':
                "Yeah, well, my cash, along with my documents, was burned by our kindest leader."
            "A real survival kit."
            "I wish I had a micro-USB charger to go with it, that would be great."
            th "Was the camp supposed to be disbanded after Parents' Day and I'd settle in the woods?"
            "And crowning the whole bunch was a small bag of candy."
            "'Start', I read on the package."
            "I put it in my pocket, just in case it came in handy."
            "And, having scattered all the aforementioned junk in the pockets of my backpack, I hid it back under the bed."
            if alt_day4_me_neu_date == 'us':
                "And then I noticed Ulyanka rushing out the window."
                th "Where is she going, I wonder?"
                "I decided to follow the girl."
            stop music fadeout 3
            stop ambience fadeout 3
    with fade2
    return

label alt_day4_me_neu_us_candies:
    scene bg ext_square_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 3
    play music music_list["so_good_to_be_careless"] fadein 5
    "You never know."
    "She might be up to some mischief."
    "Better safe than sorry, as they say."
    "I tried to move stealthily, without drawing attention to myself."
    "But the girl was walking purposefully, seemingly unaware of anything around her."
    "She was heading north."
    "Past the cabins."
    scene bg ext_houses_sunset with dissolve
    "Reaching the last 'street,' she surprised me by turning toward the squad leader's cabin again."
    th "Walking in circles?"
    th "No way, nonsense."
    "I decided to keep watching."
    "And, as it turns out, for good reason."
    scene bg ext_house_of_mt_sunset with dissolve
    "A little before the seventeenth cabin, Ulyana turned and broke into the bushes - apparently there was a path there, a little obscure one."
    "Already more afraid of losing sight of her than of being detected, I increased my pace."
    "Ulyana kept stubbornly ignoring me - she was almost running."
    "Until she went outside the grounds - there was a small ajar gate in the brick fence, and the girl took advantage of it."
    scene bg ext_path_sunset with dissolve
    play ambience ambience_forest_evening fadein 3
    "And that's where my reflexes played a cruel trick on me."
    "I tried to close the gate behind myself, but instead..."
    play sound sfx_open_metal_hatch
    us "Ah!"
    show us fear sport with dspr
    "She jumped up on the spot and turned in my direction."
    me "Calm down, just calm down."
    "I replied, feeling like the best ghost in the world."
    me "It's just me."
    show us dontlike sport with dspr
    us "You!"
    us "What do you want?"
    if alt_day4_me_neu_volley:
        me "I'm just walking around."
        "I shrugged."
        me "Thinking of a treacherous revenge plan."
        us "Well, go think somewhere else! {w}You can't be with me."
    else:
        us "Apologize for the ice cream?"
        show us calml sport with dspr
        "She turned away."
        us "I won't forgive you, don't even think about it."
    me "What if I give you candy?"
    $ counter_us_7dl += 1
    us "Candy?"
    show us normal sport with dspr
    us "Why didn't you say so in the first place! Come on."
    "I obediently handed her the bag."
    us "Why so little?"
    "She stared at me suspiciously."
    us "Tell me, did you eat half of it yourself?"
    "I nodded."
    me "Of course. {w}Well, am I forgiven?"
    us "Oh, wait a minute. I'll see if they're poisoned."
    dreamgirl "Don't worry, precious, the neurotoxin in this candy is not subject to organoleptic analysis."
    th "What, who, where?"
    dreamgirl "No color, no taste, no smell, you dumbass!"
    th "So they're poisoned?!" with vpunch
    "An image of a man holding his head appeared out of nowhere in my mind."
    "While my subconscious and I were picking at each other, the little one managed to unwrap some candy and put it to good use."
    me "What do you think?"
    show us smile sport with dspr
    us "Goog!"
    "She mumbled, chewing hastily."
    us "You know, you're not hopeless."
    "Concluded the redhead."
    th "And eventually the two of us fell in love..."
    th "And then we started dating..."
    th "No, that's bullshit, I can't imagine that."
    "I shook my head, pushing the nightmare away."
    me "That's it now?"
    us "That's it. Off you go. I need to get into my secret hideout, and I can't do that with strangers walking around."
    hide us with dissolve
    "After swallowing the 'stranger,' I turned around and walked out of there."
    "But I held a grudge!"
    stop music fadeout 3
    stop ambience fadeout 3
    with fade2
    return

label alt_day4_me_neu_us_guards:
    scene bg ext_path_sunset with fade2
    play ambience ambience_forest_night fadein 3
    play music music_list["no_tresspassing"] fadein 1
    "And before I knew it, I was lost."
    "I mean, for a while I was walking like a basset, picking directions and turns without fail."
    "But a big body has its disadvantages."
    "So I got lost."
    "Lost."
    "The sunset forest was already not much different from the night forest, so I froze in place, rightly afraid to move or go anywhere in my condition."
    "I don't want to poke my eye out with a twig or break my leg."
    "Anyway, the disposition is fun and amusing: The target is missed, and I'm frozen in the darkness of nowhere."
    "It's time for me to hoot and holler, 'peeeeeeeoooopleeeeeee'!"
    "I was getting some air in my chest when I stumbled upon a faint glimmer of flame directly ahead."
    "Motionless, warm - like the window of a house where the kitchen is nervous and waiting for you to come home from school or work."
    me "Thank you."
    "I mumbled."
    me "Thank you."
    "Barely visible light - I thought I would have to walk and walk, covering my face with my elbow and carefully touching the ground in front of me with my foot before I stepped."
    "But it wasn't frightening at all."
    "Fortunately, the cost of the issue was in only a few dozen yards."
    $ persistent.sprite_time = "night"
    $ night_time()
    scene bg ext_polyana_night with dissolve
    "The trees parted, and I came out into a tiny clearing, in the very center of which a kerosene lantern shone on a stump."
    "Beside it lay an ordinary flashlight, for the occasion of its uselessness turned off."
    "It was wrapped around the side of the reflector with a t-shirt."
    show dn normal pioneer with dissolve
    "The owner of said shirt was standing right there."
    show al normal pioneer at left
    show tn normal pioneer at right
    with dissolve
    "So did his two buddies."
    "I realized that I owed my symbolic salvation to them."
    "Not for the fact that they're standing there now, grimacing, holding hands and trying their best not to let any outsiders through."
    "Not for the fact that by their behavior they best explain that I'm on the right track."
    "Not at all."
    me "Thank you."
    show dn upset pioneer with dspr
    dn "Tonik, put the lamp out."
    "Instantly, a hitherto nameless boy in a dress shirt, with red, permanently tired eyes, oriented himself."
    "Thank you for giving me a light: tiny and unfaithful - it did lead me out of wandering in the darkness."
    "A symbol of hope."
    "And then the kerosene light went out, leaving only a tourist flashlight wrapped in a T-shirt: turned on, it gave an unfaithful but really cozy yellow light."
    "Finished with the formalities, Curly turned to me again."
    dn "What did you forget here?"
    me "Forgot?"
    "The most important things we always say as if in jest."
    "So no one will guess how much it really means."
    "How important, for instance, is it to me that a jaunty red-headed little thing doesn't get into trouble - who knows those pioneers?"
    me "I forgot..."
    show al dontlike pioneer with dspr
    "Carelessly I repeated."
    me "I'm just walking. {w}Is that against the law?"
    show dn dontlike pioneer with dspr
    dn "Then you'd better walk away from here."
    "Cut off the leader without making any attempt to give way."
    me "You'd keep your mouth shut, wouldn't you?"
    show tn smile pioneer with dspr
    "Tenderly I asked."
    "They were hiding something so diligently..."
    "And the more diligent they were, the more curious I became."
    "Maybe there's nothing exotic there. {w}Just boyish secrets, like pretty pebbles or cards or homemade knives."
    "But what's that got to do with Ulyanka?"
    "And I'd swear she's gone into the bushes behind the backs of these 'guards'."
    "Very, very far behind was the race in the twilight, the frantic panting and some incredible flair that suddenly woke up out of the blue this evening."
    "Pierced - breached - by a chest of intangible, yet no less tangible obstacles in the way."
    "It was like I was running the Olympic steeplechase, jumping and jumping - until I got lost, inertia skipping one of the turns."
    "It was weird, scary, and scary-excited: getting lost within three meters of the campground was something I'd never experienced before, and the experience was therefore fresh and exhilarating."
    "And yet, they are so jealously guarding this something..."
    "And they look at me as if I were irrelevant and completely useless here."
    with fade2
    "What's much worse is that I feel my own irrelevance here."
    "It's like I'm peeking at something that's not meant for me and has nothing to do with me."
    dreamgirl "Should we spit, blow, and walk away quietly?"
    th "Why would I?"
    dreamgirl "Look, I certainly don't mind peeping at nude pioneer girls and expressing topology..."
    dreamgirl "But she's fourteen, what do you need her for anyway?"
    th "For starters, she owes me a tiny, but still a debt."
    dreamgirl "Spit it out."
    th "Easy."
    "I didn't argue."
    th "But this situation has piqued my curiosity."
    dreamgirl "Spit on your curiosity, too."
    th "Why do you keep saying 'spit' and 'spit'? Are you a camel?"
    if alt_day2_us_escape and (counter_us_7dl >= 4):
        $ counter_us_7dl_px = 1
        if loki:
            "Perhaps I should simply break in on one nerve and see - what is such a terrible secret the young guards are guarding."
            "That was a bad idea. So, of course, I decided to give it a try."
            "A little to the left of center, here the guards don't make direct eye contact, and therefore will give weakness when I snap out of my seat."
            th "On your mark..."
            "I half crouched down, getting ready to jump out of my seat..."
            "Sensing something wrong, the pioneers tensed up."
            "And..."
            "Waving my hand, I laughed:"
            me "You're so silly."
            show dn upset pioneer with dspr
            dn "Silly or not, we won't let you through."
            me "I don't need to."
            me "I remember this place perfectly, I'll just come back here tomorrow and see it all for myself."
            "I winked at the main goofball:"
            me "Or are you going to post guards here tomorrow too?"
            show dn unsured pioneer with dspr
            "Their leader was embarrassed, but relaxed-apparently he believed that I wouldn't try to discredit him."
            "And I won't."
            "Pushing the lantern to the side, I sat down immediately on a stump and offered the guards candy, which they proudly ignored."
            "Finally, asked the question that really interested me."
            me "Why are you burning the lantern if you've got a light?"
            show dn normal pioneer with dspr
            dn "We need a bright light."
            "After hesitating, the boy reported."
            dn "We need a lighthouse."
            me "A lighthouse? {w}For what?"
            dn "Are adults all that stupid?"
            "Asked the boy condescendingly."
            dn "What else is a lighthouse for? To point the way."
            me "That's right."
            "I agreed."
            me "Thank you."
            dn "For what?"
            me "For showing me... the way, too."
            dn "You don't look lost."
            me "And yet."
            with fade2
            "After a moment's silence, I inquired:"
            me "Is the camp that way?"
            "After guessing the direction, I waved my left hand."
            "The boy nodded, his guard, relaxed, were already sitting nearby, chopping something in the dark with knives."
            th "How do they even see anything"
            me "Do you point the way every day?"
            dn "We try. Only we don't get to take the lamp every day - the watchman scolds us."
            me "I knew it wasn't yours."
            show dn dontlike pioneer with dspr
            dn "He doesn't need it! He has an electric spotlight! He could do it himself..."
            "Hotly the kid started to object, but instantly pulled himself together."
            show dn normal pioneer with dspr
            "Dryly continued."
            dn "We do it because it's the right thing to do."
            "Without speaking, the other two boys, who hadn't uttered a word until now, also nodded."
            "Amazing unanimity."
            me "In fact, I think if you've helped at least one person, it's not all for nothing."
            me "Like me today. So you didn't just burn for nothing."
            dn "A forest beacon? {w} What kind of nonsense is that?"
            me "Which one?"
            dn "Haven't you figured it out by now?"
            me "Is there water somewhere?"
            dn "Listen."
            "And I heeded the advice."
            "Only now realizing what had been confusing me all along."
            play ambience ambience_boat_station_night fadein 3
            "Invisible in the darkness, somewhere very nearby, damply breathed Big Water."
            "Not that unbearable and cutting off man's inability to grasp the infinity that awaits on the shores of seas and oceans."
            "No, it was different here."
            "Simpler... And somehow more poignant."
            me "Hmm. Curious. {w} Are there ships on our river?"
            dn "Of course. Sometimes they even honk back if you go out on the headland with a lantern."
            tn "But that's where Tisha lives, she always drives them away."
            me "Is Tisha a cat?"
            show dn grin pioneer with dspr
            dn "What cat? It's Tikhonova. Lena."
            me "What are you? The three of you chased me away, and you listen to her?"
            tn "Try not listening to her. She knows how to make you go away."
            me "I can do that myself."
            dn "You can't do it the way she does it. And you won't be able to."
            with fade2
            me "How does the squad leader let you go?"
            dn "We're not little kids. {w}We watch out for each other."
            dn "And we need a lighthouse. It's a dark night."
            "And there was some strange rightness in his words."
            th "And if we were back in Karelia, his efforts would have been in vain."
            th "The nights there require fire just to keep warm."
            th "What would they do there?"
            "An ostracized thought suddenly occurred to me."
            me "Yes."
            "I answered."
            me "Yes."
            me "Only you shouldn't have just put the lamp there. There has to be movement."
            me "So the captains know they're being met by someone alive. Do you understand?"
            me "So that..."
            hide dn with dissolve
            "I marked a lucky tree standing nearby and climbed about halfway up it."
            "Found a branch looking in the right direction, and called out:"
            me "Hey! That's where you can hang your lantern if there's no strong wind."
            me "And... Oh, what's that?"
            stop music fadeout 5
            "At the very edge of my line of sight, a glowing blur drifted leisurely in the darkness."
            "No matter how hard I tried, I couldn't think of what it could be."
            dn "Come down."
            "It came from the ground."
            with fade2
            show dn normal pioneer with dspr
            "When I came down, all three of them were in the same places they were when I came out of the woods."
            play music music_list["a_promise_from_distant_days"] fadein 5
            "They were tense again - like string, like thin fishing line."
            "But this time there was no anger in their tenseness, nor was it against me."
            me "What happened?"
            dn "We consulted. And decided to let you through."
            "Unwrapping the shirt, the hitherto nameless little man gave me the lantern:"
            dn "You'll give it back when you're in camp, okay?"
            "I nodded."
            me "Why the change of heart?"
            show dn smile pioneer with dspr
            dn "I don't know."
            "He shrugged his shoulders serenely."
            dn "Looks like you're not hopeless."
            me "Tthhhhhhhhhanks."
            dn "You take this road further, be careful down there, watch the slope so you don't slip - you could hit yourself very badly."
            dn "Stay on the right side, if anything, grab the roots, they're strong there."
            dn "You'll ask Ulya what to do later."
            dn "Questions?"
            "I smiled."
            me "What's your name, Comrade Sergeant?"
            show dn dontcare pioneer with dspr
            dn "Danya."
            $ meet('dn', 'Danya')
            "Seriously he replied."
            dn "And this is Alka and Tonik."
            $ meet('tn', 'Tonik')
            $ meet('al', 'Alka')
            "The white-haired heads bobbed in sync."
            dn "That's it, go."
            scene bg ext_path2_night with fade2
            "As the thicket closed behind me again, a strangely familiar, barely audible horn sounded from somewhere in front to my left."
            "In which I, digging in my memory, identified the horn of a motor ship."
            me "Indeed, there are."
            "I noted, shining a light under my feet: the descent was extremely steep."
            "Two hundred meters of braindead slalom, and darkness in southern latitudes comes quickly and capitally."
            "I don't know why I signed up for this in the first place."
            "I don't know why Ulyanka needed to walk here at the risk of breaking her neck?"
            "I don't know anything."
            "Nothing."
            scene bg ext_seashore_7dl with dissolve
            "Muttering curses to myself, stumbling and slipping every now and then, a few minutes later I managed to make it all the way to the bottom."
            "From here the water was no longer only audible - water could be smelled."
            "Our river must have made a turn somewhere around here, that's why the shore was so close."
            "Two hundred yards is the price of admission."
            "But what interested me most was that glowing spot."
            th "What could that be?"
            "To the left of the slope down to the water, far into the creek are the pier bridges, old, crooked, barely visible in the remnants of light from the receding sun."
            "It was closer there, and I, wondering either about flying saucers or animal luminescence, stepped onto the creaking boards."
            "You could see the stain a little more detail from here."
            "It looked like they were water Chinese lanterns or something."
            "Amazing, really, that they don't go out or sink in that kind of wind."
            show us fear sport far with dissolve
            "One of the boards creaked under my foot especially hard, and a certain half-dark silhouette nearby shrieked in Ulyanka's voice, rushed to run, but stumbled, and..."
            me "I've got it!"
            "I shouted, grabbing at the familiar T-shirt - black in this light."
            "Ulyana froze, forgetting to move and - just in case - breathe."
            "So I slowly but surely dragged her back to the bridges."
            dreamgirl "You're sharp."
            dreamgirl "Like Steven Seagal."
            th "Shut up."
            "The T-shirt was made of something incomprehensible, so there was no guarantee that it would hold the weight."
            "But..."
            show us cry sport close with dspr
            "Ten seconds, and the girl is standing next to me."
            "She was shaking, either from the cold or from fright."
            "So it made perfect sense to hold her and try to calm her down."
            me "It's all right, you hear? Everything is..."
            show us sad sport with dspr
            us "Syomich, you scared the hell out of me!"
            "She broke free and retreated half a step."
            us "And what are you doing here?"
            me "I came to see it..."
            hide us with dspr
            "I turned my head toward the unknown glow and froze again."
        else:
            "I was distracted from my thoughts by the rustling of the bushes, and the one who had brought me here came into the clearing."
            show dn normal pioneer at fleft with dspr
            show us dontlike sport with dspr
            us "What's going on here? You!"
            "Ulyana instantly oriented herself, poking me in the chest with her finger."
            us "What the hell were you stalking me for?"
            me "Me? {w}Stalked?"
            us "No, sniffed me out. {w}What do you want?"
            me "What are you doing here?"
            us "None of your business. {w}Any more questions?"
            me "That's how it is?.. {w}So, after all the good I've done for you!"
            show us calml sport with dspr
            us "Nice try. Are you done?"
            me "Yes."
            "I realized that any further negotiations would go nowhere."
            "Whatever they're doing, they're just going to shut everything down now, and I won't see anything."
            show dn dontlike pioneer at fleft with dspr
            dn "Then get the fuck out of here."
            "The pioneers here were greyhounds - that's a fact."
            "No one was afraid of seniority or power - nothing."
            "As if they owned the situation now."
            "It was useless to saddle the insolent; it would have looked like an awkward attempt to save face, and everybody understood that."
            me "Watch your language."
            "I politely offered."
            dn "Or what?"
            me "Nothing."
            "Ignoring the boy who had started to say something, I turned to Ulyana:"
            me "Little girl, if you're going on the run with these people, don't let them make you the main mommy."
            show dn surprise pioneer at fleft with dspr
            show us normal sport with dspr
            dn "On the run?"
            "The same boor asked with interest."
            "Ulyana brushed it off - she was thinking intensely about something."
            show us smile sport with dspr
            us "Okay."
            "She made up her mind."
            us "You can pass."
            us "I don't think you can help. {w} But you probably won't mess up much."
            show dn upset pioneer at fleft with dspr
            dn "Ulya!"
            show us normal sport with dspr
            us "Don't flare your nostrils, it's with me."
            show dn dontlike pioneer at cleft with move
            "The boy jumped up to Ulyanka and talked fast and fast, waving his arms."
            "I could hear only scraps of words and names, but I caught the essence of the complaint: I was accused of being too old."
            "Mirya himself (the leader of this gang before Ulyana) told them not to let the adults in."
            "They only spoil everything."
            "But Mirya was about seventeen years old himself."
            "I grinned: if the kids knew how old I really was..."
            us "You're forgetting the fact that he was able to find us. {w}I guess we can give him a chance."
            dn "Knowing how carelessly you walk, no wonder."
            show us dontlike sport with dspr
            us "Whatever. Don't be silly - you know very well I had nothing to do with it."
            "She gave a short order to the guards, and they parted, letting me through the thicket on the path."
            hide dn
            hide al
            with easeoutleft
            hide tn
            with easeoutright
            scene bg ext_seashore_7dl with dissolve
            "And I realized suddenly where that faint, trembling glow was coming from. It wasn't a sunset, not a reflection in the clouds."
            "The thought that they could have somehow hidden it from me now seemed ridiculous."
            "And how, I wondered, could they hide this sight - a huge spot of light was drifting unhurriedly across the standing, black surface of the sunset pool - shivering, breathing..."
            "Alive."
    else:
        show dn surprise pioneer with dspr
        dn "Or what?"
        "With incomprehensible enthusiasm the kid asked me."
        dn "Are you going to beat me?"
        dn "Or will you kill me to get through?"
        me "Fool, I..."
        "I started, and in a moment I realized the reason for the boy's enthusiasm as he stood across from me, clenching his fists and staring sideways."
        th "It's just a game to him!"
        "I gasped."
        th "Just..."
        scene anim prolog_1 with dissolve
        "For a moment our eyes met again - his reddish whites glittered with a very bloody glow - and I realized suddenly!"
        "That the lantern was not even a lantern at all - but the scorching southern sun, which heated the dry plateau."
        "Despite the fact that the cliffs were blasted straight into the sea by a steep precipice, here, fifty meters away, it was dry and sultry."
        "And the road dust creaked underfoot."
        "There was absolutely no access to the sea - because there the ferry was departing for the horizon, barely moving from overload, and there were wails and screams over the water."
        "Perfect target for a howitzer - you can shoot straight ahead with almost no adjustments for wind."
        "The only thing that prevents the corps from fixing and deploying the cannons is a chain of young men in the service cloth with greaves and galloons."
        "Junkers, cantonists, cadets..."
        "They knew that they would not leave this plateau on their own feet."
        "But they also knew that if they wavered, they would open fire on the departing ferry."
        "That is why they stood now, not daring to tremble, in spite of the pointing nozzles of the guns, the dust, or the heat."
        "Admiring their own valor, and with this admiration they are blocking the unceasing fear, whispering that it is wrong to be thirteen and under the cannons..."
        "The one in charge, a little taller than the others, gray-eyed and dashing, stood with his head bowed stubbornly, seeking my gaze."
        "And I should spit on all the glances, and wave my hand, giving the order."
        "But how can one without one last look?"
        with flash
        "The moment our eyes met, and I saw that vaguely familiar bloody glow again, that's what it was all about."
        "The whole squad deployed here, all of us, suddenly realized what we were worth."
        "Realized who we really are."
        "I looked around at the odd ranks of riflemen and infantry."
        "It creeped me out to see what I was really doing."
        "With guns, with sabers - at the boys."
        "Is this what I read and dreamed of in Goncharov and Turgenev?"
        "Was that what I was prepared for?"
        "Was I even prepared?"
        "Were I?"
        "Then why did they prepare such a... nothing?"
        scene bg ext_polyana_night with fade
        show dn surprise pioneer with dspr
        "Eye contact was gone, and I was back in the same clearing in a confrontation with the three guardsmen."
        "Now the word no longer seemed so euphemistic and mocking."
        "Because these were ready to stand to the end."
        "But it didn't make any sense."
        "Curly used his most terrible weapon."
        "Which means I won't be able to do anything stupid like walk past them for a very long time."
        "I was going to have to get along with the scariest thing of all - the utterly frank and unsightly truth about myself."
        if loki:
            "Musician, poet... nothing."
            "Spent four days to... do nothing."
            "To maintain the status quo."
            "Spitting in the face of a higher power in retaliation for a gift."
            "The memory of the events leading up to the transfer came back at once and suddenly."
            "One can't help but wonder if I was worth such a miraculous rescue."
            "Some people are just meant to one day die ignominiously."
            "Maybe I'm one of them."
        else:
            "A passionless amoeba, as my subconscious once aptly dubbed me."
            "A man who, even in the most wonderful place in all observable universes, chose to behave as he was used to."
            "That is, no way."
            "I'm only interested in my solitude and my computer."
            "Wouldn't it be great if they moved him along with me?"
            "Wouldn't it be nice to just stop thinking?"
            "Feeling sorry for myself."
            "It would have been nice to die."
        "I had to get over the truth."
        "I - have no purpose"
        "No purpose."
        scene bg ext_path2_night with dissolve
        "As I turned around, I felt the muscles at my temples relax and my spine lose its rigidity."
        "Slouching and exhaling, I staggered back to the camp, in the meantime automatically locating it."
        "That's right, there's no way I could have been one of those young men in that confrontation at the forgotten plateau."
        "Because standing with your back to the cliff requires a simple condition."
        "One must be human."
        "Not my case."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day4_me_neu_us_launch:
    play music music_7dl["thousand_of_pixies"] fadein 3
    scene cg d4_us_stardust_7dl with dissolve
    me "What is this?"
    "I exhaled reverently."
    if loki:
        us "That's just..."
        "Ulyana brushed it off, settling back down on the very edge of the pavement."
        me "What?"
        us "A custom."
        us "But you'd better get out of here..."
        me "Is there something wrong with me?"
        us "No, but..."
        us "Mockery and mistrust. You'll ruin everything."
        me "That's just silly. I got here, remember? Convinced that bodyguard of yours."
        me "You have no reason to be afraid of me."
        "Ulyana shook her head negatively."
        us "I'm not afraid of you. Rather, for you."
        me "But what can happen?"
        with fade2
        us "Nothing."
        "She sighed."
        us "And that's the saddest part."
    else:
        us "Is there a difference?"
        "An answer came from behind, and Ulyana came out on the dock beside me."
        "She was holding a simple ship, carved from a piece of pine bark, with a steeply curved leaf sail."
        "Its only difference from ordinary ships was a short, thick candle, the back of which was clipped onto the ship's mast."
        "A match flickered, a flame was born--there were three more in line at the tiny fire on the shore, waiting their turn."
        me "It seems to me that..."
        us "It seems."
        "Squatting down, the girl gently lowered the little boat onto the water, turned her nose toward the glowing spot, and gave it a gentle nudge."
        "And another tiny spark headed toward the huge speck of light. There were already at least a hundred more like it."
    us "A thousand Flares."
    me "A thousand... Flares. So?"
    us "That's it."
    "She looked at me with bewilderment."
    us "Do you need anything else?"
    us "Where we're going, it's impossible to leave, to run away, to leave. No way."
    us "But there is a solution."
    me "Flares."
    us "Them."
    if loki:
        us "These are the ones."
        "She waved her hand, pointing to the shivering morass."
        us "They'll probably drift to a creek. And that's a good thing."
        me "Why?"
        us "There's a chance!"
        us "Not a single one has ever sailed downstream - I don't know why."
        me "Strange."
        us "That's what I think too."
        us "And it's the same on the beach."
        us "You see?"
        "I nodded mechanically."
        us "That's the same thing. I've tried everything. Even hijacked a catamaran once."
        scene cg d4_us_stardust_7dl with dissolve
        us "But now, since you're here."
        us "Help us?"
        me "But how?"
        "Instead of answering, Ulyana turned away and stared pensively at the flotilla moving farther and farther away."
        us "Remember - in the beginning was the word."
        me "Why are you getting into religion?"
        us "What's religion got to do with it?"
        "She snorted."
        us "I want your word first."
        me "To no one and never."
        us "I don't care even if it's the Pope. It's more important to me that you don't drop everything midway. Do you understand?"
        me "I promise."
        "After hesitating, she continued:"
        us "We're not the first ones to run «Searches» here."
        us "Before me was Mirya, and before him someone else."
        us "We're all looking for the same thing."
        me "A way to escape from the camp?"
        us "Idiot."
        "She scolded me spitelessly."
        us "This is a special place. There's almost nowhere else like it. And you make jokes."
        me "What makes it special?"
        us "You'll find out one day."
        us "But yeah, you can't just leave here either. Although you've already tried. Yes."
        me "Then what about the groceries, the parents?"
        us "They're different. It doesn't work with them."
        me "What's different?"
        us "Adults."
        me "And me?"
        "Ulyana shrugged her shoulders."
        "From her point of view, it already made sense here."
        "And this... big one doesn't know why or where he's going."
        us "You're an adult. Too old."
    else:
        us "I've tried, and more than once. Tried launching them from different places."
        me "But we..."
        us "I'll go look for them tomorrow."
        "Reported the girl."
        us "I've tried everything I can."
        scene cg d4_us_stardust_7dl with dissolve
        us "It's all coming back."
        me "Coming back?"
        us "Except the water."
        "She nodded."
        us "It comes from somewhere and goes somewhere."
        us "So she's found a way."
        "She rose, keeping her eyes fixed on the drifting flotilla of a thousand lights."
        us "And I will find it."
        me "Is that why you said I was too old?"
    "An allusion to the fact that as one grows older one stops believing in oddities?"
    "Isn't it because one is protected by a Fairy Tale until one is fourteen, while one believes in the Fairy Tale itself?"
    "Anyone would be able to name a few instances from his early childhood when what happened could not be called anything other than a miracle - happy coincidences, omens, encounters..."
    "Ulyanka is at her highest point; she is almost out of circulation."
    "Another year, maybe a year and a half, and that's it."
    "A young lady who is interested in all sorts of adult things will see the light."
    "And she will be irretrievably lost to the fairy tale."
    th "It's not about age, it's about growing up."
    us "And you're not?"
    me "No."
    us "Convince me. Make a Flare."
    me "May I?"
    us "Why not?"
    "Rummaging through my pockets, Ulyanka handed me a piece of pine bark and a knife."
    me "And really... why not."
    "There was nothing difficult about making a ship for me."
    "Except I did it too long ago last time, so I might have forgotten some of the details."
    "But it seemed to be all right, I returned the knife and the formed hull to her, catching the girl's approving glance."
    "With the mast on top, the keel on the bottom, the new lighter was about to set sail."
    if loki:
        "Ulyana held out a candle torch to me."
        us "Attach it to the mast."
        me "Why?"
        "Instead of answering, she tapped my forehead:"
        us "Are you stupid? It's a Flare!"
        me "Yes, of course."
    else:
        me "What's down there?"
        us "The quarry. That's probably where they all get stuck."
        me "Badly launched?"
    "Silent again. Ulyanka held out her hand:"
    us "Finished?"
    "Receiving what she demanded, she took the ship in her hand and, holding that one out over the water, began:"
    us "Melt-melt, away you left, my friendly gale!! {w}Help us find our way elsewhere!"
    me "What's that?"
    "Waving it off, she continued."
    us "Melt-melt, away you left, my windy flare. {w}So I'll meet someone somewhere."
    "With that last word, she let go of the ship - I didn't have time to notice when a tiny petal of flame took over the mast - and it rushed down!"
    scene black with dissolve
    "I squeezed my eyes shut, preparing myself for the fact that the splashing water was about to flood the flame because of a bad landing, and I would not have the same as those who had created the flotillas."
    scene cg d4_us_stardust_7dl with dspr
    "But only a soft chuckle was my answer."
    "When I opened my eyes, I saw a ship drifting leisurely."
    "The flame on its mast was alive and would not go out."
    us "This is the Guidance."
    "Pronounced it with a capital letter."
    us "You have to ask the Flare to find the way."
    me "And it will find it?"
    us "One Flare doesn't have much power. {w}But when there are many, they can do some things."
    me "Really?"
    us "Really."
    "She looked at me strangely, but when she realized she was looking into my eyes, she was embarrassed, looked away."
    us "You'll figure it out for yourself."
    me "What does it take to understand?"
    us "Launch your own Flare. By yourself, all by yourself."
    me "Just launch it?"
    us "Why complicate it?"
    us "Light a candle, recite the guidance, and ask him to find his way. {w}He'll do the rest."
    with fade2
    "She rose, keeping her eyes fixed on the drifting flotilla of a thousand lights."
    us "And tomorrow we'll have to find them to take the next step."
    us "If you don't want to look, that's okay, I'll find them myself."
    if loki:
        me "What if I want to?"
        us "No."
        me "No what?"
        us "You don't want to."
        me "How do you know?"
        us "It's just..."
        "She looked away."
        "And I suddenly realized a very obvious fact:"
        th "She's afraid of jinxing it."
        "Well, of course she is."
        th "That's why she doesn't wish, that's why..."
        "I tried to put it in the most neutral tone possible."
        me "Let's go back to the subject again tomorrow, then..."
    else:
        "She stared at the smoldering sunset, and I couldn't think of anything but to mutter:"
        me "That's all you're going to find."
        us "What do you mean?"
        me "It's not about the ships, is it? It's about who launches them."
    scene bg ext_seashore_7dl with dissolve
    stop music fadeout 3
    play ambience ambience_boat_station_night fadein 3
    show us sad sport with dissolve
    "They were silent again. Ulyanka twitched her shoulder."
    us "You'll go."
    us "You go yourself tomorrow, check it out, I have nothing to do with it."
    us "...imagining things..."
    "And she was right about everything."
    "That's what it really was, and nothing revolved around the girl with the red hair."
    "Nothing and nobody."
    "And nothing would happen if I went to the quarry tomorrow alone and Ulyana went back to camp now."
    "Only..."
    "I imagined that we would separate now, me to the camp, her to her unknown business. And we'll go further and further apart..."
    "The word 'forever' reeked of raw cold, it hurt and was impossibly uncomfortable, despite all logic and fairness."
    me "I won't."
    "I exhaled."
    show us normal sport with dissolve
    us "Why?"
    me "Because I..."
    "My mind wandered, searching for a better argument."
    me "I don't know the way!"
    if loki:
        us "Ask Tisha."
    else:
        us "Ask Lena to take you there. She knows."
    me "Are you serious?!"
    us "What's the big deal? {w}Fine, I'll go."
    "Ulyana was covered with large goosebumps."
    us "It's cold."
    hide us with dissolve
    me "I want you to come with me."
    "I mumbled helplessly into her back."
    if loki:
        "Ulyana flinched, but did not turn around."
        "Using the candle's lamp as a source, she waved to the guardsmen standing above, and they instantly lit the lantern, lighting the way."
        show us normal sport with dspr
        us "Are you coming?"
        us "Or are you going to sit?"
        me "Coming."
        us "Then hurry up, we don't have much time."
        hide us with dspr
        scene bg ext_path2_night with dissolve
        "Mired in wet grass and mud and clay, she hurried upstairs, leaving me no choice but to follow her."
        "And as I walked, trying to put my feet straight and cling tight, all sorts of fairy tale damning things came into my head, about age, about the camp being an enchanted realm."
        "By the time we both climbed up, the sky had finally darkened."
        "And we, accompanied by an honorary escort, headed back to camp."
    else:
        "My back straightened for a moment - and then immediately relaxed."
        "There was no way I could check to see if I was imagining things, or if I really wasn't being heard."
        "And for some reason I didn't want to ask."
        "Without another word, she waved to the waving 'guardsmen' nearby and, bogging down in the clay, hurried up the path, where she was met."
        "A minute and I was alone."
        scene bg ext_path2_night with dissolve
        "With a sigh and one last glance at the burning flotilla, I turned to face the slope and began to climb up."
        "The time was close to ten o'clock. Just a little more, and Slavya would close the gate."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day4_me_neu_map_dining_hall1:
    play music music_list["your_bright_side"] fadein 5
    scene bg ext_dining_hall_away_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 2
    "As soon as all the pioneers had gone about their business, I decided to take a seat on the huge porch of the mess hall."
    "It was very quiet and peaceful."
    "And on the bench you could comfortably sit and take a nap."
    "And there's no way in hell anyone would have seen me from the square or anywhere else."
    "A loner by nature, I needed at least brief portions of solitude."
    "You can't completely change a man's character in three days."
    "It's been known for a long time that you can break a habit in at least six weeks."
    "In camp terms, two non-stop shifts."
    "If I don't go crazy from having someone around all the time."
    "So..."
    "I rocked from heel to toe, figuring out how tonight might go."
    menu:
        "Relax on the bench":
            $ alt_day4_me_neu_mt_dream = True
            $ counter_mt_7dl += 1
            th "What's there to think about though? Water doesn't flow under a rock."
            show blink
            "I stretched out on the bench and covered my eyes."
            "I'm having a siesta - and let the world wait!"
            scene anim prolog_2 with dissolve
            "Eyes closed, pupils rolled back..."
            play music music_list["sparkles"] fadein 3
            show blackout_exh
            $ meet('mt','Girl')
            "I stood on the doorstep of the store, staring at myself in confusion."
            "It was one of those stores that seemed to have sunk irretrievably into oblivion with the cheapening of the Internet."
            "All these «555», «CD-DVD-MP3», «disk rentals» and others."
            "Who would want to spend money on a knowingly pirated product when you can get about a thousand times more at home for the same money?"
            "But, man! If there will be such sellers here, I'll gladly come here more than once, and not even ten times!"
            "I was shoved in the shoulder by someone scowling and walked past me into the store."
            me "Excuse me."
            "I stopped looming on the doorstep and got out of the way of traffic."
            "It suddenly dawned on me what it was, besides the archaic nature of this kind of store, that caught my attention."
            "The decorations."
            "Instead of the now-familiar bright pictures on the CD covers, most of them were just gray boxes with some kind of abbreviations."
            "Finally, the saleswoman broke free and approached me."
            show mt normal dress with dissolve
            mt "Greetings."
            show mt smile dress with dspr
            "Professionally she smiled."
            mt "How can I help you?"
            me "Yes I, you see... {w}Say, what about all those disks?"
            "Unintentionally lowering my voice, I asked."
            show mt normal dress with dspr
            mt "Oh, that's... That's user scenarios."
            me "I'm sorry, what?"
            show mt smile dress with dspr
            mt "In youth slang, they are modifications for games."
            me "And you sell them?"
            mt "We only sell them!"
            mt "Visual novel modifications sell especially  well."
            "She turned the turntable with difficulty, and I squinted at the mottled digital-letter mush."
            me "«9НЗ»? «БГ»? «ХВП»?"
            "Confused, I read."
            me "And what is all this?"
            show mt normal dress with dspr
            mt "It's okay, people who come here usually already know exactly where to go and what code to ask for."
            me "And they go and buy the modification on the disk?"
            mt "Yes."
            me "But why do they need it?"
            "The saleswoman looks like she knows something, so for some reason I'm not at all embarrassed to ask her that question."
            "Why not? Find out from the salesman what it is that makes his product so appealing."
            mt "You see..."
            mt "It often happens that a promising game doesn't turn out as great as the fans wanted."
            mt "In the case of 'novels' it's most often the story that's the problem."
            mt "That's when people start making their own plots."
            me "Plots? In mods?"
            me "Really? A work written by an amateur?"
            "To tell you the truth, I've always thought of mods as a kind of foul play, where the user just changes the rules of the game to suit themselves."
            mt "Yes. And very often they are not inferior, but even superior to the original."
            "I found that hard to believe."
            "It was hard to believe that someone who had been doing his own, unrelated game-building business until now, would suddenly sit down and do better than professional developers."
            mt "Or even more often it happens that the game succeeds, and fans have a hard time saying goodbye to it, and the developer refuses to write a sequel, or its creation takes a very long time."
            me "It's already called the English word 'fanfiction,' and I have more faith in that."
            "I picked up."
            mt "Right. {w}Some may still be canonized and counted as DLC in their lifetime."
            me "But in any case, there's hardly anything really noteworthy there."
            me "The story, and not a bad one, either... In modifications."
            show mt smile dress with dspr
            "The girl listened with a smile to my fervent speech."
            me "Maybe one day I'll go completely crazy and decide to read something like this."
            me "But for now, I'm not some crazy-ass otaku to disappear into it all."
            mt "By the way, our store is raffling off a prize - one of the discs has an address where you can pick it up."
            "Smiles the saleswoman."
            me "And what's the prize?"
            show mt normal dress close with dspr
            mt "Can't you guess?"
            stop music fadeout 3
            scene black with fade
            with vpunch
            "She was wearing a set that even my contemporaries weren't ashamed to wear-black, satin-colored, breast-puffed, with a frivolous heart cut out a little away from the most interesting place."
            me "You know..."
            mt "What?"
            me "Don't you think..."
            "In two breaths I exhaled, reluctantly pulling away from her lips."
            me "That your underwear is too erotic... For a pioneer camp..."
            mt "I don't think so."
            "She covered her eyes and listened to where and what my lips were doing."
            mt "I don't usually wear that."
            "Common sense? Hello?"
            "Reason, consciousness, consequences? Hello?"
            "Hidden in a far corner and not a peep when things come to..."
            "Or is the body concerned?"
            stop music fadeout 3
            scene bg ext_seashore_7dl with dissolve
            $ persistent.sprite_time = "night"
            show mt pioneer shade with dspr
            play music music_list["silhouette_in_sunset"] fadein 3
            mt "So I'm your leader, you're my mentee."
            mt "Is that right?"
            "She says it again, a little audibly, more to herself."
            "Silence."
            "We just got out of the water, and I couldn't get a tooth out of the cold."
            "Why do you always have to have an inconvenient conversation at the most inconvenient time!"
            "Was she waiting for something?"
            "Maybe..."
            me "You... That's not true."
            "I stood up."
            "Took a breath in my chest."
            "I exhaled."
            me "Anyway, there's, like..."
            mt "I see..."
            "She's looking away."
            me "No! I don't..."
            mt "What?"
            me "I... I can't do that!"
            "I flopped down next to her on the ground."
            "And looking somewhere in the same place she's looking, I finally said."
            me "I really like you."
            "Like a trigger - the word is spoken, and I realize it really is."
            "The subconscious mind is much wiser about some things than the smart guy above, it understands instantly who is really cool to be around."
            "With whom time flies, and you always want to go back."
            "Unless it's another invasion of privacy."
            "And my loneliness cried."
            me "Besides... I found you, but you never told me what the grand prize was there."
            "Silence."
            "I have a bad feeling about this."
            "Very bad."
            "The girl sighed with a look of forgiveness."
            mt "It's complicated."
            mt "And I was still hoping to be happy when I heard the confession."
            me "A confession? I was just..."
            dreamgirl "You just told her that you like her."
            th "Long time no see."
            "But here, yes, that's right. {w}Even without pulling the owl on the globe, you could call it a confession."
            "And it doesn't look like she's pretending."
            "She even seems to be blushing a little-though I can't see in the darkness anymore."
            mt "At least I'll know you care about me."
            "There you go."
            "The circus closes, the canvas tent folds up, the arena is dismantled, and all that's left on the ground is a littered trampled area."
            "That area is me."
            "One idiot's theater, fuck's sake."
            mt "You look depressed. Did I say something wrong?"
            me "No."
            mt "Does something hurt?"
            "My heart must be hurting."
            "Myocardial infarction, nine millimeter scar."
            "I'm curious, why do soldiers shoot themselves in the heart?"
            "She stroked my cheek."
            show mt normal swim with dspr
            mt "Don't get sour, Semchik."
            $ meet('mt','Olga Dmitrievna')
            show blinking
            $ persistent.sprite_time = "sunset"
            scene bg ext_dining_hall_near_sunset
            show mt sad pioneer
            with flash
            mt "Semyon..."
            me "No, I'm telling the truth!"
            "Shouted me."
            me "I really like you!"
            show mt grin pioneer with dspr
            mt "Wow... What frankness."
            "Smiled Olga, sitting next to me on the bench."
            "And I suddenly realized I was awake."
            "What..."
            with flash2_red
            "I'm blushing."
            "I'm so busted!"
            me "I didn't... You..."
            show mt smile pioneer with dspr
            mt "Is that so? We're not on a first-name basis anymore?"
            "The squad leader smiled softly."
            show mt normal pioneer with dspr
            mt "Yes, I realized it was a dream."
            mt "It would be foolish to hope that you remembered everything."
            me "Excuse me?!"
            show mt smile pioneer with dspr
            mt "Forget it. Just thinking out loud."
            me "But... {w}Ah... Okay. How did you find me?"
            show mt grin pioneer with dspr
            mt "I know you better than you think."
            "The squad leader smiled."
            mt "I've got a little errand for you."
            mt "Just a little one."
            "Nuh-uh. {w}The more the leader tends to underestimate her workload, the {b}bigger{/b} the trouble awaits on the other shore."
            me "But Ooooolga Dmitrievna!"
            "I mouthed."
            mt "What happened?"
            me "You were on your way to rest!"
            show mt sad pioneer with dspr
            mt "Yeah, I'll get some rest with you..."
            "She sighed."
            show mt smile pioneer with dspr
            "But then she smiled:"
            mt "I'll do this one thing, and then I'll go straight to rest!"
            "Uh-huh, five hundred pioneers have been busted in her rest."
            mt "Don't distract me!"
            mt "Go find Alisa and Miku."
            mt "Tomorrow we have a bonfire on the schedule, so we have to get ready properly."
            mt "I've already given you foam and potatoes, but what's a bonfire without a guitar."
            me "So get some songs ready with them, huh?"
            show mt laugh pioneer with dspr
            mt "You're so understanding."
            "Olga laughed and stood up."
            show mt laugh pioneer far with zoomout
            me "Olga Dmitrievna!"
            show mt smile pioneer far with dspr
            mt "What?"
            "Dropped the leader - she seemed to be all caught up in rainbow dreams of vacation."
            me "Where should I look for them?"
            mt "Ah. On the stage, they're supposed to clean up there after the concert."
            hide mt with dissolve
            "She waved me off and ran away."
        "Better look for answers":
            "There was nothing interesting here, and I didn't want to earn bedsores for nothing."
            "I'd better go wander around the camp some more."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day4_me_neu_map_estrade1:
    scene bg ext_stage_big_sunset_7dl with dissolve
    play music music_list["your_bright_side"] fadein 5
    play ambience ambience_camp_center_evening fadein 2
    "Miku and Alisa were tidily tidying up cables, unplugging equipment, and dragging the used props back to the back of the stage."
    "And while it was clear that Miku was a bread-and-butter operator, we could only guess at the reason Alisa had taken up the broom."
    "Remembering the third thing to look at endlessly, I succumbed to the impulse and settled down on the bench to meditate."
    "Unfortunately, they were finishing up, so I couldn't sit for long."
    show dv normal pioneer2 at right with dspr
    dv "How long have you been sitting?"
    "Finally, Alisa noticed me."
    me "Just got here."
    if alt_day4_me_neu_mt_dream:
        me "Olga Dmitrievna asked me to find you and remind you to prepare some songs for tomorrow's bonfire."
        show mi normal pioneer at left with dspr
        mi "Good evening, Senya!"
        "Nodded the Japanese girl."
        mi "And I remember about the fire, so now I was going to go to the club after cleaning up and rummage through the songbook there."
    else:
        show mi smile pioneer at left with dspr
        mi "Hi, Senya! Came to see us?"
        "Smiled Miku."
        mi "We're all done now, so you can't help anymore."
        th "What a pity!"
        "I could hardly contain a smile."
        mi "Actually I'm lying though!"
        mi "It's a busy day, it's all gone out of my head."
    mi "Alisochka and I have to remember some campfire songs, even the ones we sang last time. {w}Do you know any campfire songs?"
    "She stunned me."
    "After thinking for a while, I nodded."
    show mi happy pioneer with dspr
    mi "Great! {w}Three heads are better than two, maybe you can remember something we don't know."
    "The prospect of frantically learning a new song didn't scare this girl one bit."
    show dv grin pioneer2 with dspr
    dv "Oh, I didn't know you two had such a warm relationship."
    dv "I thought about asking you to help me and Ulyanka somewhere, but now that you have such a bond..."
    show dv laugh pioneer2 with dspr
    dv "I dare not interfere with your happiness."
    if alt_day4_me_neu_date == 'dv':
        me "No, thank you."
        me "I'm surprised you have the nerve to come up to me after this morning."
        show dv smile pioneer2 with dspr
        dv "Hey, are you offended?"
        dv "What are you, Nadia girl for ten tomans? {w}Cry some more then."
        show mi upset pioneer with dspr
        mi "What happened this morning?"
        me "It wasn't pleasant this morning."
        dv "Locked him in the cabin, made a joke."
        dv "And he whimpered like a fifth grader."
        "Miku stared at me with some sort of morbid curiosity, and a word from English, either 'bally' or 'bully,' suddenly popped into my head."
        "And, fleeing from the despair that overwhelmed me, I blurted it out."
    if not (counter_us_7dl_px == 1):
        menu:
            "Let's go prepare songs!":
                $ alt_day4_me_neu_mi_songs = True
                $ counter_mt_7dl += 1
                "Hell no, I'm not helping her. A squad leader's order is a squad leader's order!"
                show dv angry pioneer2 with dspr
                "After muttering something unprintable, Alisa rattled the back room door and slammed the padlock shut and inquired:"
                dv "So are we coming or what?"
                hide mi
                hide dv
                with dissolve
            "Dvachevskaya, if anything…":
                $ alt_day4_me_neu_dv_help = True
                $ counter_us_7dl += 1
                dv "It's going to be okay, Ulyana and I have a plan."
                "She winked:"
                dv "And you don't have to shake like that, it won't hurt you in any way."
                me "What should we do?"
                dv "Come here first."
                hide mi
                hide dv
                with dissolve
    else:
        me "Let's go prepare songs!"
        $ alt_day4_me_neu_mi_songs = True
        $ counter_mt_7dl += 1
        "Hell no, I'm not helping her. A squad leader's order is a squad leader's order!"
        show dv angry pioneer2 with dspr
        "After muttering something unprintable, Alisa rattled the back room door and slammed the padlock shut and inquired:"
        dv "So are we coming or what?"
        hide mi
        hide dv
        with dissolve
    return

label alt_day4_me_neu_songs:
    play music music_list["she_is_kind"] fadein 3
    scene bg ext_musclub_night_7dl with clock_r
    play ambience ambience_camp_center_night fadein 3
    "By the time the trial was over, dusk had fallen on the street."
    "So we got to the music club when the only light was the moonlight."
    me "Shall we sit here?"
    "I suggested, not really hoping the girls would agree."
    "But I didn't want to go indoors on a night like this."
    show mi upset pioneer at left with dissolve
    if alt_day4_me_neu_date == 'mi':
        "Miku looked at me questioningly - apparently this morning's events were still fresh in her mind."
        "But she didn't say anything."
        "For which I was grateful."
    mi "What about us then..."
    me "Let's just turn on the lightbulb for now, so you don't miss the strings, and then we'll see."
    me "Maybe what we already remember will be enough to fully form a program of performances."
    show dv normal pioneer2 at right with dissolve
    dv "I don't like this oaf, but I'll take it."
    dv "It's hot and stuffy in there, let's just sit here."
    mi "If you say so."
    "Unsurely stretched Miku."
    hide mi with easeoutleft
    play sound sfx_open_door_1
    "And, instantly out of sight, rattled the instruments."
    show dv shy pioneer2 with dspr
    "Alisa immediately took on an independent look and even opened her mouth to begin to say something..."
    "And immediately closed it."
    "I stared at her diligently as if she were nothing."
    "No wonder she mingled."
    "Confused, she looked away, and, not knowing where to put her hands, she stared at her feet."
    "And I, barely able to contain a satisfied chuckle, literally reveled in the awkwardness of the moment."
    "I love, really love, such moments of awkward silence."
    play sound sfx_open_door_1
    show mi smile pioneer at left with dspr
    "And then Miku popped out of the club to lighten the mood."
    "Oh, too bad. When else will I be so embarrassed!"
    mi "I'm sorry, it took me so long - I couldn't find a guitar for Senechka, too."
    "She handed Alisa the instrument."
    me "Why me?"
    "Miku was staring at me with interest."
    show mi laugh pioneer with dspr
    mi "How are you going to remember the songs?"
    me "How, how... I'll sing and you play."
    th "Really, it's more and more specific songs that come to mind."
    dreamgirl "Aliska will definitely appreciate them!"
    "I smiled."
    th "And how Olga will appreciate them! {w} It'll probably be the first time in her practice that she decides to flog a pioneer."
    me "Alright, let's try to remember something."
    show mi smile pioneer with dspr
    mi "We need at least a dozen songs."
    me "How many do you have now?"
    mi "About five, I guess, let's remember. {w} And you? {w}Will you sing?"
    stop music fadeout 3
    scene cg d4_mi_guitar_moon_7dl with dissolve
    "Miku got ready and stared at me questioningly."
    "And I was silent. I was uncomfortable for some reason."
    mi "Or you don't want to?"
    "She smiled understandingly."
    play music music_list["farewell_to_the_past_edit"] fadein 3
    mi "Aaand!"
    "She took the first chord."
    me "Yes, yes, now."
    "A couple of breaths to overcome the embarrassment, and:"
    me "Both sad and funny... Spinning memories. What was, is gone, and tomorrow is parted."
    me "Give me your hand for a long separation. Smile from the heart, write down the phone."
    dv "I know this one, but it's not suitable for a fire."
    me "Then..."
    "The second song was even easier."
    me "We simply have nothing more to lose - everything will be remembered at the terrible trial. {w}This night lay like that pass, beyond which hope is fulfilled."
    "To the picking chords Miku was joined by Alisa - no wonder she knew the lyrics:"
    dv "It's just that the living is lived for nothing - not for nothing, but that's not the point, you know..."
    "Another song, another... Socialization has many faces, and besides participating in camp life, there must be that sometimes."
    "Just as in the life of any pack sometimes both wolves and red flags are vital, so a loner sometimes can't do without a campfire, vodka, and the knowledge that everyone around him is now looking at smoldering embers in the same way."
    me "And men walk through the world, their words are sometimes rude... Please excuse me - they speak with a sneer."
    mt "But the sweet tenderness of song caresses their dry lips - And the best books they keep in their backpacks!"
    "Apparently we were singing quite loudly, for despite the rather late hour and remoteness, pioneers began to pull up along the paths."
    th "As if they hadn't seen enough at the concert."
    "With withering irritation I thought."
    "The last chords, and..."
    me "That's the end of our concert..."
    voice "Hey, do one last one!"
    "Asked a voice out of the darkness."
    "I had no choice, so I had to give in."
    me "The last one."
    "Rummaging through my memory, I pulled out one - a finger-slicing, glass-like sculpture."
    me "It's not for the fire. But since you asked..."
    if loki or herc:
        me "A black mask hides the face, but it does not hide the eyes. A finger on the trigger - who knows, God or the devil for us."
        me "The dot on the map, the roar of the plane, a friend's parting glance."
        me "Who knows, God or the devil - and who will come back..."
    "Alisa, Miku - here syncopated, in tact - like a waltz."
    th "Eh, I hope I'm not the cause of chronoclasm - unlike the questionable date of writing 'lyrics', this one was written by Butusov in '95 is absolutely accurate."
    me "You take off your evening gown, facing the wall... And I see fresh scars on your back, smooth as velvet."
    me "I want to cry out in pain - or forget myself in my sleep."
    me "Where are your wings, {w}that I liked so much."
    "After the guitar died down, silence descended on the camp."
    "Our unwitting spectators seemed to have forgotten how to breathe."
    "You asked for it, I had nothing to do with it."
    me "That's it. The performers are so tired they're hungry and there's no place to spend the night. The concert is postponed until tomorrow's bonfire."
    scene bg ext_musclub_night_7dl
    show mi smile pioneer at cleft
    show dv normal pioneer2 at right
    with dissolve
    "The girls outlined a playful bow."
    show mt normal pioneer at fleft behind mi with dissolve
    mt "If you do the same tomorrow, I'll present you with an award."
    me "Thank you. Raising the flag, I presume"
    show mt smile pioneer with dspr
    mt "How did you guess that?"
    me "Yeah, I guessed it. {w}Girls, how many songs?"
    "Miku raised her fist with her finger pressed to the side:"
    mi "Eleven!"
    me "That's great! {w}Let's call it a night - I'm going to bed!"
    stop music fadeout 3
    return

label alt_day4_me_neu_prank:
    play music music_list["i_want_to_play"] fadein 5
    scene bg ext_aidpost_night
    show dv normal pioneer2 at left
    with fade
    "After saying goodbye to Miku, Alisa led me through the center of the camp to the lonely, darkened cabin of the infirmary."
    "It occurred to me that no one in this camp is capable of moving at a normal human pace."
    th "What fun it would have been if Dvachevskaya and I had thought of going out. {w}I would be like, 'Redhead, let's go for a walk on the pier.'"
    th "And she would be like: 'Alright!' and in the rhythm of a sprinter-record holder in 19.8 seconds from the square to the pier!"
    me "Are you in a hurry?"
    if counter_us_7dl > 1:
        us "Yes!"
        if alt_day4_me_neu_volley:
            us "In case you've forgotten!"
            me "I haven't forgotten anything."
        show us smile sport at right with dissolve
        "Ulyana emerged from the darkness, clutching triumphantly some kind of bag in her hand."
        dv "Is that it?"
        "Ulyana nodded."
        me "What is it?"
        us "You'll see!"
    else:
        dv "Yeah, I have something to do."
        dv "I'm going to step aside for a minute, and you wait for Ulyanka and tell her to wait for me."
        me "I hope this isn't a setup..."
        "I grumbled."
        show dv laugh pioneer2 with dspr
        "Alisa soulfully clapped me on the shoulder."
        dv "Relax! You're my ally today, and I don't make fun of allies."
        me "What a relief."
        "I sneered."
        dv "That's it, wait."
        hide dv with dspr
        "Alisa disappeared into the darkness."
        "Leaving me alone."
        "And she was gone for much longer than a minute!"
        "I had already had time to walk, to sit, I even considered lying down - though I wanted more than anything to just ignore the 'deal' and go home to bed."
        "But I decided to give the Redhead a chance."
        "So..."
        with vpunch
        play sound sfx_scary_sting
        "There was a noise behind me, and..."
        "Someone tapped me on the back."
        scene bg ext_aidpost_night:
            xalign 0.5 yalign 0.5 zoom 1.0
            linear 0.3 zoom 1.15 xalign 0.75 yalign 0.5
        $ alt_pause(1)
        scene bg ext_aidpost_night:
            xalign 0.75 yalign 0.5 zoom 1.15
            linear 0.8 zoom 1.2 xalign 0.75 yalign 0.35
        show us smile sport at right with dspr
        us "Huh, what are you doing here?"
        me "Guess!"
        "Man, both of them have exactly the same jokes!"
        "And they affect me in exactly the same way: I really want to punch both in the ear."
        me "Alisa asked me to wait here for you while she's out there somewhere."
        show us dontlike sport with dspr
        us "I knew Aliska would sneak into the infirmary without me!"
        "Right. Hold the phone."
        me "She... what?"
        show us shy sport with dspr
        us "No, no, it's nothing! You're hearing things."
        scene bg ext_aidpost_night
        show us shy2 sport at right
        show dv normal pioneer2 at left
        with dissolve
    play music music_list["eat_some_trouble"] fadein 3
    dv "Let's go!"
    hide dv with easeoutright
    "She ran off somewhere again."
    "And Ulyana and I ran after her."
    "What else could we do?"
    scene bg ext_clubs_night with dissolve
    "As it turned out a little while later, Alisa was aiming for the cyberneticists."
    "There was a light on in the room, but I cautiously scouted through the barred window and saw no one."
    show dv normal pioneer2 with dspr
    dv "Stand guard."
    "Alisa ordered and disappeared again."
    hide dv
    me "But I'm... Hey!"
    me "What, am I going to be used as wordless draught power all the time now?"
    "Asked me of the night."
    show us smile sport with dspr
    us "But at least it's not boring! Why are you like that!"
    with hpunch
    "She poked me lightly in the side."
    us "Give me a boost, I want to see what she's doing there."
    me "What about standing 'on guard'?"
    us "It's all right, they won't get here before halfway, so come on, don't slow down."
    "I don't know what she was talking about, what Alisa was talking about, or what they needed from the cyberneticists."
    "But just in case, I chased away the thought that explosives could be made from more than just saltpeter."
    "So I dutifully put my back up and equally dutifully held the little one on my weight until Alisa showed up to disperse us into the bushes."
    hide us with dissolve
    dv "That's it, now we wait."
    "She pointed her thumb and froze again - if you don't know who you're looking for, you'll never get a good look at her!"
    "I hope our disguise is just as good."
    "Well, or that they won't use select gamekeepers against us, who are much better at finding than everybody else at hiding."
    "Anyway, after the time changed to half past twelve at night on the phone, the pioneers pulled past us."
    show el normal pioneer with moveinright
    "First came Electronik."
    hide el with moveoutleft
    show mz normal glasses pioneer at left
    show sl normal pioneer at right
    with moveinright
    "Behind him is the amazing and incomprehensible tandem of Buzzkill and Slavya."
    hide mz
    hide sl
    with moveoutleft
    show mi normal pioneer at right
    with moveinright
    "And, to conclude the evening, Miku."
    hide mi
    with dissolve
    "All that was missing was Lena and Shurik and the squad leader."
    "But it seems they decided not to wait for them."
    "Electronik had already poured water into the jar and set the kettle on, ignoring the fact that the jar wasn't very clean."
    "And it was eerily strange and unusual to sit here in the bushes while the pioneer blossom was out there drinking tea after lights out!"
    "Not that I'm jealous of them - but, man, I want to get involved too!"
    "Alisa intercepted my gaze, winked, and shook her head toward the window, saying, 'Keep watching'."
    "And the pioneers got right down to tea - the aromatic beverage brewed in a twist from the elephant tin, pouring noisily into the cups they had set up."
    "And so the first takes a sip, the second..."
    "Candy and cookies appear on the table out of nowhere - that's right, no one wants to muffle water just like that."
    "But, unfortunately, that's when Alisa's surprise went off."
    "The first to blush was Miku, as the lightest in the matched company - apparently the amount of 'surprise' was too much to for her specific weight."
    "She pressed her hands to her mouth, sweat rising on her forehead."
    "Muttering something, she shot out into the street and ran somewhere up the road."
    "After her, the rest of the tea party also succumbed to the effects of the chemistry."
    "Not ten minutes later, absolutely every pioneer in the club ran past us."
    "And Alisa, on the right of a winner, immediately set up a robbery!"
    "Quickly, quickly grabbing what her raking hands could reach, she jumped out of the clubs and, abruptly throwing: 'follow me,' and rushed off!"
    "We had no choice but to follow her."
    $ alt_day2_dv_us_house_visited = True
    scene bg ext_house_of_dv_night
    show dv normal pioneer2 at left
    with dissolve
    play sound sfx_7dl["breath"]
    me "I didn't expect you to be so vulgar, to be honest."
    "Trying to catch my breath, I squeezed out."
    "We galloped from the scene of the special operation to a little clearing not far from Alisa and Ulyana's cabin."
    "There, we divided up the captured goods."
    dv "Vulgarities?"
    me "That was laxatives, wasn't it?"
    me "That's how they ran to the bathroom."
    show dv laugh pioneer2 with dspr
    show us laugh sport at right with dspr
    us "Ha ha ha! That's why that joke will never get old."
    dv "I agree!"
    "Alisa clapped the palm that was set up."
    dv "Why are you looking wolfish?"
    me "So you both think you did something funny?"
    show dv grin pioneer2 with dspr
    dv "We didn't?"
    me "No!" with vpunch
    extend " This is humor below the belt! It's for the lowest type of people."
    show dv laugh pioneer2 with dspr
    dv "U… Ulyana, you hear that?"
    "Through her tears, Alisa moaned."
    dv "We… We… We're the lowest people."
    "Apparently my face was eloquent enough, for for the next few minutes the girls were incapable of anything but the worst kind of laughter."
    show dv smile pioneer2 with dspr
    show us smile sport with dspr
    dv "Oh, geez, oh thank you, that was funny."
    "I think Alisa's stomach started hurting again - this time from laughing."
    us "It's not laxatives."
    "At last Ulyana took pity on me."
    us "The usual sweatshop medicine."
    us "The reaction's just - you saw, red face, sweaty, tense."
    dv "If they weren't such prudes, they'd just tell each other what was going on."
    dv "But since it's so important to them to 'save face'..."
    "She lifted the cookie jar over her head."
    dv "Let them drink their tea that way!"
    hide dv
    hide us
    with dissolve
    "I, shaking my head, headed off to sleep."
    dv "Hey, newbie!"
    "Redhead called out to me."
    show dv normal pioneer2 with dspr
    me "Yes?"
    dv "Not a word to anyone, understand?"
    "I shrugged."
    "It seemed self-evident to me."
    show dv smile pioneer2 with dspr
    dv "You really aren't that retarded."
    me "Thank you."
    "And I was gone for good."
    stop music fadeout 3
    return

label alt_day4_me_neu_sleeptime:
    if alt_day4_me_neu_mt_diary:
        scene bg int_house_of_mt_noitem_night with dissolve
        "After destroying all traces of my activities in the cabin, I returned to my half."
        "The main thing is that Olga doesn't notice anything."
        "I have as long to live here as I've ever lived."
    elif (alt_day4_me_neu_date == 'us') and (alt_day4_me_neu_us_backpack) and (counter_us_7dl_px == 0):
        scene bg ext_house_of_mt_night_without_light with fade
        play ambience ambience_camp_center_night fadein 3
        play music music_7dl["shehasgone"] fadein 3
        "The house stood lonely and abandoned."
        "About as much as I felt."
        "Incomprehensibly dreary, as if I'd tried to prove myself better than I was - and I'd been caught by the hand and rubbed my nose in all my flaws and vulnerabilities."
        "Though why 'as if,' when exactly that's what happened?"
        "When I responded to a straightforward offer to be human for even a fraction of a second by just scrambling away with my tail between my legs."
        "Shaking my head, I fumbled for the key in my pocket."
        play sound sfx_open_dooor_campus_2
        $ alt_pause(1)
        scene bg int_house_of_mt_night2 with fade
        "I needed solitude now more than ever."
        "Once inside the house, I quickly threw off my clothes and wrapped my head in a blanket."
        "I had one more night to live and figure out what to do tomorrow."
        stop music fadeout 3
        stop ambience fadeout 3
        with fade
        return
    else:
        scene bg ext_house_of_mt_night_without_light with fade
        play ambience ambience_camp_center_night fadein 3
        play music music_list["a_promise_from_distant_days_v2"] fadein 3
        "Home, sweet home!"
        "Oh, I mean, a place to sleep!"
        dreamgirl "How are you, villagers?"
        th "Come on! I'm already confused myself."
        "Anyway, tomorrow will be a new day."
        play sound sfx_open_dooor_campus_2
    stop ambience fadeout 2
    scene bg int_house_of_mt_night2 with fade
    play ambience ambience_int_cabin_night fadein 3
    "Which means what?"
    "That's right!"
    "It means there's more to look forward to tomorrow."
    "Throwing off my clothes, I crawled under the blanket and closed my eyes."
    "The camp was adjusting to me."
    "Everyone gets the reality they deserve and created."
    "If I'd tried to get close to any of the girls, my mind would probably have been full of engaged romance."
    "But instead I chose a much more attractive opportunity."
    "I chose an affair - with the whole camp!"
    "And it was already beginning to arouse me."
    if counter_us_7dl >= 4:
        th "I befriended Ulyana…"
        if counter_us_7dl_px >= 1:
            "Was allowed into the holy of holies."
    elif counter_mt_7dl >= 2:
        th "Finally befriended Olga…"
    if alt_day4_me_neu_mt_diary:
        "Although I was a little embarrassed about reading the squad leader's diary..."
        "But there's such interesting stuff in there!"
        th "I'll definitely take the time tomorrow and read some more!"
        "I promised myself."
    th "How tired I am..."
    "I got comfortable and relaxed."
    scene cg d1_end_of_day_7dl with dissolve
    "And a second later I was asleep."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day4_me_neu_mt_diary_vol1:
    scene bg int_house_of_mt_backpack_sunset with fade
    $ set_mode_nvl()
    "If you open the book in a normal, human way, more than half of it is just organizational records."
    "That's right, the squad leader does the teaching, notes interesting pioneers and plans activities."
    "It's not the first year she's been going here, there's a lot of notes."
    "But if you turn the diary over, open it from the other side..."
    nvl clear
    $ alt_pause(3)
    "{i}The last entry read:{/i}"
    "{b}July 21st, 1989{/b}"
    "Some secrets about him were revealed today."
    "I can't say I like them."
    "Can't say I don't want to make a couple of scenes of him trying to communicate with his peers... Ha! Peer girls!"
    "But that's right. He's a pioneer and I'm a... I'm a squad leader."
    nvl clear
    $ alt_pause(3)
    "Something not meant for other people's eyes is brought to our attention."
    "A chronicle of restlessness, anxiety and sadness."
    "The thoughts of a man confused and not half as sure as he looks."
    th "That's interesting! I'll have to read it more carefully!"
    "I peeled the notes back to where they began and began to read."
    nvl clear
    play music music_7dl["take_my_hand"] fadein 3
    $ alt_pause(3)
    "{b}June 10th, 1986{/b}"
    "Well, hello, old friend."
    "Today is the opening of the shift - and my first day as a squad leader."
    "How strange, I've been coming here all my life to rest, and now..."
    "The pioneers in the squad are interesting - kids of athletes, artists. They're a stellar bunch."
    "But I don't like them. I have something to compare it to."
    "Oh. That last one wasn't very professional."
    "Anyway, I'm going to work, not cry about my fate."
    "I'm a squad leader!"
    "It's like changing years, a few weeks later you still write the old date out of habit."
    "And I salute the girls walking past me with a UML diamond on their chests."
    "Now I'm one of them. I have the same badge myself."
    "Olga Comet's time is over, now she's replaced by the boring Olga Dmitrievna."
    "It even makes me a little sad."
    nvl clear
    play sound sfx_paper_bag
    $ alt_pause(3)
    "{b}July 2nd, 1986{/b}"
    "That's the end of the first shift."
    "There was a lot of fun and sad."
    "But the fun was the most. I was wrong to fear that I wouldn't be able to do my job as a leader."
    "Although, of course, it wasn't all smooth sailing."
    "When Antipka was caught outside the hulls of the second troop, where he was running to his Zinka, I had to take responsibility."
    "Who wouldn't?"
    nvl clear
    "Now we have to wait for the headache when we get to town."
    "I don't care. Nyutka said something like this happens every year."
    "It can't be helped, they're not really kids anymore, they're teenagers, and they're already interested in the opposite sex."
    "They're already sitting on their suitcases waiting for the bus, it's closing time for the first shift."
    "And I'm locked in here writing."
    "{i}A few lines are crossed out so that you can't make it out.{/i}"
    "…can't wait for the second shift."
    nvl clear
    play sound sfx_paper_bag
    $ alt_pause(3)
    "{b}July 5th, 1986{/b}"
    "Nyutka said that usually between the first and second shifts they give a week for a shift change."
    "The caretakers and staff have to go through the camp, pick up lost and forgotten things, put things in order, and put the place in the mood."
    "No one wants to check into a place that looks abandoned."
    nvl clear
    play sound sfx_paper_bag
    $ alt_pause(3)
    "{b}July 16th, 1986{/b}"
    "Yesterday we celebrated exactly the middle of summer."
    "Today the camp director woke me up in the morning to meet a guest from Cuba."
    "As a result, instead of laying down and sleeping during nap time, I'm standing at the bus stop like a fool."
    "And just when I was about to run out of patience, I was ready to spit and leave - a bus pulled up to the camp gate."
    "I expected anything, but a whole bus for one pioneer..."
    "An important person wanted authenticity?"
    nvl clear
    play sound sfx_paper_bag
    $ alt_pause(3)
    "{b}July 22nd, 1986{/b}"
    "The second shift is coming to an end."
    "It's been a lot more interesting than the first."
    "Not least because of the new guy."
    "He's the son of some big shot at the embassy, if I'm not mistaken."
    "But he doesn't get cocky, doesn't act like everyone around him owes him everything."
    "Cheerful, knows a whole bunch of interesting stuff that he enjoys talking about."
    nvl clear
    "But I had to work for a few days to get him to thaw out a little."
    "I had to remember everything I learned in pedagogy."
    "And, you know, diary... It was worth it."
    "And now we're standing at the bus stop, waiting for our bus."
    "And I don't know what's gonna happen next."
    "{i}On the margins is a non-believable drawing of a tiny Ikarus, rolling toward the horizon, and a girl in a dress and a hat, looking after it.{/i}"
    "I've made friends with all the pioneers, and they're splitting up."
    "And I still have a whole shift to do with complete strangers - to re-establish contact and pick up the keys."
    "Instead of my friends, instead of my favorites, there will be new faces."
    "For the first time, I wondered if I had chosen the right profession."
    nvl clear
    play sound sfx_paper_bag
    $ alt_pause(3)
    "{b}July 23rd, 1986{/b}"
    "Yesterday I put the pioneers on the bus."
    "Today I cried like an idiot all day."
    "And in three days there's another run."
    nvl clear
    play sound sfx_paper_bag
    $ alt_pause(3)
    "{i}Next came several pages, the notes on which were completely unreadable.{/i}"
    "{i}Apparently, Olga tried time after time to go back and write about her thoughts and experiences.{/i}"
    "{i}And every time it failed, there was always something she didn't like.{/i}"
    "{i}Finally, there were lines that could be made out.{/i}"
    "{b}December 25th, 1986{/b}"
    "Agreed to a winter run. Why not?"
    "Of course, for decency's sake I asked if I couldn't cram into my two-bedroom superior and sit quietly there over the winter break."
    "But these are games that no one but newcomers to our profession has been paying attention to for a long time."
    "Especially since the camp was indeed a magical, soul-healing place."
    nvl clear
    play sound sfx_paper_bag
    $ alt_pause(3)
    "{b}December 27th, 1986{/b}"
    "My first winter shift."
    "The mood is festive!"
    "But it was a little spoiled by the fact that none of my summer 'old-timers' came."
    "Too bad, it's always nice to see a familiar face in a new place."
    "But it's all just work, just work."
    "I've been seeing a psychologist for a month anyway, drumming into me the difference between professionalism and parenting."
    "When the kids leave, don't tear up like they're going away to a foreign land forever."
    nvl clear
    "They're just coming home."
    "And you can always have a reunion night, a little fireside party for the squad or the whole camp."
    nvl clear
    play sound sfx_paper_bag
    $ alt_pause(3)
    "{b}January 1st, 1987{/b}"
    "In honor of the first of January, camp got up at ten o'clock, and for some reason I hadn't slept since the morning."
    "So at seven o'clock, when I realized I couldn't stand lying under the blanket for even one more minute, I got up."
    "The sun wasn't even hinting at sunrise yet, so I had to navigate the street lights."
    "I walked out to the gate."
    "For some reason I remembered the summer, the second shift, when I, an entire squad leader, had been made to run and meet the bus at quiet hour."
    "And I couldn't believe my eyes when the horn blew from the road and the Ikarus pulled up to the bus stop."
    nvl clear
    "Tell me I'm dreaming..."
    "Tell me it's just a silly dream."
    "And from the front seat comes up he, the Incredibly Important Rookie."
    "A little older, a little bigger in the shoulders, still impossibly embarrassed."
    "And you know, Diary, I think this winter break is going to be a lot nicer than I thought it would be!"
    nvl clear
    play sound sfx_paper_bag
    $ alt_pause(3)
    "{b}January 9th, 1987{/b}"
    "I don't remember shit."
    "Until the transport arrived, I lay there, leaving all the trouble of camp to Slavya."
    "Lord... I'll never drink so much again."
    nvl clear
    stop music fadeout 3
    $ set_mode_adv()
    $ persistent.sprite_time = "night"
    $ night_time()
    scene bg int_house_of_mt_night
    "I didn't have time to read anything else - the steps creaked under someone's footsteps, and I hurried to put the diary back where it belonged."
    "Taking on a bored look, I looked out the window."
    "And dusk had already fallen on the camp."
    th "Wow! It's great to read."
    play sound sfx_knock_door7_polite
    $ alt_pause(2)
    me "Come in!"
    stop ambience
    play sound sfx_open_dooor_campus_1
    show sl normal pioneer with dspr
    sl "And Olga Dmitrievna..."
    "Slavya appeared at the door."
    "I shook my head:"
    me "I'm sorry, she was gone all evening."
    sl "Really? Well... I'll be off then. {w}Good night."
    if not (alt_day4_me_neu_volley or counter_un_fz_mt_transit == 3):
        sl "About what was in the warehouse..."
        "I smiled."
        me "I'll be as dumb as a grave."
        me "See you tomorrow."
    hide sl with dissolve
    play sound sfx_close_door_campus_1
    "Yes, it's time to go to bed."
    scene bg int_house_of_mt_noitem_night with fade
    "Whether I like it or not, the day has come to an end."
    if counter_un_fz_un_route >= 4:
        "I shook Lena up a little bit, and even helped her start learning to believe in herself."
        "At least, I hoped I had."
        "Something told me, though, that she'd do just fine without me."
        "She had someone to rely on."
    return

label alt_day5_me_neu_morningdream:
    play music music_list["sparkles"] fadein 3
    scene stars with dissolve
    "At night I dreamt of a great flotilla of Flares drifting downstream."
    "And among them was one of mine."
    "Somehow I knew it - I must have sensed the temperature or the scent."
    "Or the mood."
    "So when a strong gust of wind tore the Flares away from the ships, I was not at all surprised that of the myriads of fireflies rushing into the sky, one unmistakably found me and sat in the palm of my hand."
    scene anim_digi with dspq
    "He was warm and bright yellow, like a barely hatched chicken, trustingly flattering to the palm of my hand and was like God - full of love."
    me "Melt-melt, away you left..."
    "Barely audible, I muttered, barely touching, stroking the baby with my finger."
    me "my friendly gale..."
    voice "Rr…"
    "The yellow ball rolled like a chick on my palm, leaving a faint flickering trail behind it."
    "Its touch was slightly tickling, warm-as if you were still asleep, but the sun needed to wake you up right now."
    "And it strokes your cheeks with its caressing rays, lavishing you with freckles and a smile."
    "I couldn't help smiling myself as I watched the businesslike movements of my new acquaintance."
    "He, on the other hand, rolled around, thought for a while, and jumped up and landed strictly in the center, hitting it hard."
    stop music fadeout 4
    play sound_loop sfx_head_heartbeat fadein 2
    "My hand was burned by the concentrated sun, light splashes flew in different directions, and I woke up with a shriek."
    scene bg int_house_of_mt_night2
    with dissolve
    play ambience ambience_int_cabin_night fadein 3
    "My heart was pounding like mad, my temples were pounding, and the sticky sweat made the sheets uncomfortably flush against my body."
    "And yet it was peaceful here."
    me "And what were you afraid of, you fool?"
    "I asked myself in a whisper."
    "It was a deep, deep night."
    "Olga, in a short nightgown, was asleep on the next bed, spread out, shoved the blanket aside and mumbled something in her sleep."
    "I got up, readjusted the blanket, and froze for a split second: the sight was familiar, somehow, a testament to the fact that everything in the world goes according to its own laws."
    "This is how it should be: a warm, silent night and the sharply outlined lips of a girl whispering in the moonlight..."
    mt "my friendly gale..."
    stop sound_loop
    "Suddenly the squad leader said and fell silent."
    "The secret of me and Ulyanka was becoming a Polichinelle secret."
    "But somehow that didn't spoil it at all."
    "It was as if people, once held hostage to the miracle going downstream, lost the right to sneer or cynicize it."
    "And so I had nothing at all to fear."
    "I shut the window so it wouldn't blow, and went back to bed."
    "It didn't bother me that it all happened in total darkness - I'm a St. Petersburger, and our nights are always bright, so I've learned to get my bearings."
    "The fact that it wasn't in St. Petersburg came to me much later."
    "It was when I, wishing with all my might to go back to the place where the yellow ball dives into my palm, fell asleep."
    stop ambience fadeout 3
    return

label alt_day5_me_neu_begin:
    play music music_7dl["too_quiet"] fadein 3
    play sound_loop ambience_7dl["rain"] fadein 5
    scene
    $ renpy.show("bg int_house_of_mt_sunset", what = Desat("bg int_house_of_mt_sunset"))
    with dissolve
    "When I opened my eyes, I thought I was wrong about the time I woke up."
    "It was too dark outside the window."
    "But the empty bed of the squad leader and the measured thumping of the slope of the 'loft' left no room for doubt."
    me "Rain."
    "A sleepy throat creaked."
    "Rain."
    "A radical change in the image of the barbie house."
    "Not that I wasn't ready for them..."
    "To begin with, at least, yesterday's change in the leader's behavior."
    if not alt_day4_me_neu_volley:
        "Yes, and an ugly scene by the stage..."
    "The further I went, the more diligently they tried to convince me that the world around me was not the most perfect and living by often incomprehensible rules, but alive and breathing."
    "Real."
    "'The first matrix represented a digital paradise on earth where no one ever got sick or died. It fell apart.'"
    "Okay, we'll take note."
    "The note by the mirror read: 'Raincoat in the closet, boots there too, no exercise or lineup, go straight to breakfast.'"
    "Beautiful, rounded letters, giving away the owner's educator."
    th "They must have a special course in legible writing at the school. {w} Or is legible handwriting a prerequisite for admission?"
    "Or maybe it's because a future teacher is born to write only beautifully and nothing else?"
    "I shook my head, pulling myself out of the recursive jungle, and took the squad leader's suggestion."
    play sound sfx_open_door_1
    $ alt_pause(1)
    scene bg ext_houses_rainy_day_7dl with dissolve
    "And it was pouring outside!"
    "So I wrapped myself in a tent bag as best I could and ran to the canteen!"
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_breakfast:
    play music music_7dl["raindrops"] fadein 5
    play ambience ambience_dining_hall_full fadein 5
    scene bg int_dining_hall_people_rain_7dl with dissolve
    "I and all my friends were in the canteen, and soon we'll be here, too - we can't change the place."
    "In spite of the tangible relaxation of the regime due to the rain, the seats were barely half full."
    "Only Ulyana, Miku and the ubiquitous Slavya were there."
    "The latter would not have been deterred from eating even by an earthquake, I suppose."
    "It's funny how in four days I began to call unfamiliar pioneers 'ours.'"
    "It's funny that in that time it never occurred to me to do something really drastic, with the aim of guaranteed extradition from blessed territory."
    th "For instance, it might well have been possible to blow up Genda!"
    dreamgirl "That's right, let's make an explosive out of activated charcoal and someone's mother."
    "Half-asleep, the voice of my split personality sounded hoarse somewhere beneath the vaults of my skull."
    dreamgirl "And send our bronze benefactor to Pluto."
    th "You're still sarcastic."
    dreamgirl "Not really. {w}But before you crawl into a corner again, I'd like to remind you of something."
    if alt_day4_me_neu_mt_diary and alt_day4_me_neu_volley:
        dreamgirl "You've kind of formed a triangle of attention here with Ulyanka and a fellow leader in the main corners."
        dreamgirl "What do you think?"
        "I wondered."
    elif alt_day4_me_neu_mt_diary:
        dreamgirl "We didn't finish one interesting thing yesterday."
        th "And?"
        dreamgirl "I'll give you a hint: you'll feel uncomfortable reading a girl's diary in her presence."
        th "No dumber than a steam locomotive. {w}What do you suggest?"
        dreamgirl "She's probably got a whole bunch of stuff to do, so why don't you call in some soil just in case?"
        th "Yeah, and in between getting plowed for the public's benefit? Sheesh."
    elif alt_day4_me_neu_volley:
        dreamgirl "You and Ulyana were up to something yesterday... {w}Wouldn't you like to discuss the details?"
        th "I don't think that's a good idea."
        th "If anyone sees us together..."
        "I shook my head."
    else:
        th "What exactly?"
        dreamgirl "I got a bird on my tail here that the total departure of the second shift is scheduled for the twenty-fifth of July. The day after tomorrow."
        th "What bird is that?!"
        dreamgirl "Oh my God, why does everyone get normal people and I have to share a skull with an unobservant hysterical girl?"
        "My gaze slid, against my will, to the duty schedule conveniently hanging neatly on the same column I was propping up, waiting for my turn to hand out."
        "There, in between, apparently scattered in pairs over the cabins, were the names of the men on duty from our squad."
        "And they were listed until the 24th of July. That is, until tomorrow."
        "The next cell was filled with red paste, boldly, diagonally: «DEPARTURE»."
        th "Now the most important question has been decided: whether they'll let us out of here alive."
        "I grinned."
    "There were plenty of empty seats, so you could even choose who to share breakfast with."
    if (counter_un_fz_mt_transit == 3):
        "At the last moment, Lena strode past me sleepwalking to the distribution area."
        "She got herself a couple of buns and made herself at the window."
    $ volume (0.5,'music')
    $ volume (0.5,'ambience')
    menu:
        "Sit with Lena" if (counter_un_fz_mt_transit == 3):
            "I was on my way to the girl, but Slavya promptly took her place next to me."
            "All I had to do was shrug my shoulders."
            th "They've got their own girl things going on there. I'm not likely to make them happy with my face."
            "Sighing, I decided not to crowd into their company and sat in the lurch, alone."
            $ alt_day5_me_neu_candle = 1
        "Sit with Ulyana" if alt_day4_me_neu_volley:
            $ volume (1.0,'music')
            $ volume (1.0,'ambience')
            show us normal pioneer with dissolve
            me "Hey."
            if (counter_un_fz_mt_transit == 3):
                $ counter_us_7dl += 3
            else:
                $ counter_us_7dl += 1
            "I've decided that since we're brothers on the same side now, I don't have to fear any more sneaking around on her part."
            "Naive, of course, but what if?"
            us "Oh, it's you."
            "The girl showed no enthusiasm. {w}Well, I didn't insist."
            me "Observant, Sherlock. {w}You were found in sauerkraut?"
            us "Huh?"
            me "I say if babies are found in cabbage, you were found in sauerkraut?"
            show us sad pioneer with dspr
            us "Funny."
            "Her facial expressions contradicted her words."
            me "Look, why are you so kind and affectionate?"
            "I couldn't stand it."
            us "The rain."
            "The little one answered briefly."
            if counter_us_7dl_px == 1:
                me "That's it?"
                us "That's enough for me!"
                "She looked at me like I'd said something stupid."
                "But really - what's the point of getting so discouraged over some rain?"
                dreamgirl "After all, it can't go on forever."
                th "That's right."
                show us dontlike pioneer with dspr
                us "It's good for you, you're the squad leader's favorite."
                us "And they tell me to go and do what they tell me to do again. I hate it!"
                me "Oh, please... You're not in a resort, this is camp."
                show us upset pioneer with dspr
                us "And I didn't ask to be here at all!"
                me "What difference does it make? Asked or not, you have to do what the leader says, otherwise it won't be camp, it'll be a mess."
                "I caught myself thinking that I spoke in words not at all inherent."
                "What's the matter - I've never even had such thoughts before!"
                show us sad pioneer with dspr
                us "That's exactly what I was talking about."
                "Nodded the girl."
                us "You don't even have to do anything to get it your way."
                us "Suck it up, stick it up... Favorite!"
                me "Me?"
                us "Who else, me?"
                show us calml pioneer with dspr
                us "No one is forcing you to do anything. If you don't want to go to the candle, you come up and they'll let you go!"
                me "And why would I want to do that?"
                show us normal pioneer with dspr
                us "You don't need it! But that's not the most important thing!"
                us "The opportunity!"
                "She was hardly burning with the desire to get up after breakfast and run out in the pouring rain to find out the fate of her flotilla."
                "But there was a certain envy in her for my hypothetical ability to mimic and get some perks."
                "Though I didn't believe in that mimicry myself one bit."
                "It's simple, isn't it?"
                "If I knew how to bend and flex - I wouldn't have been sitting at home for the last few years."
                "I'd be socializing, developing..."
                "Lived."
                if loki:
                    "And I did not seek rest in unfulfilled revenge, which is what ultimately destroyed me."
                else:
                    "There, among people! In a society of living, real people."
                    "Who, like me, can surf the Internet, but prefer real speech and a firm handshake to all other ways."
                "Bullshit."
                "It doesn't work that way."
                me "I don't have the option."
                "I shook my head."
                me "You don't understand that I don't have any indulgences, I'll be told something and I'll just as obediently go where they send me and do as I'm told."
                show us smile pioneer with dspr
                us "Have you tried it?"
                me "No, but..."
                show us grin pioneer with dspr
                us "Then don't say anything! Try it first."
                me "You think so?"
                us "Go! Oldmitrievnaaaa!"
                "She waved her hand, attracting the attention of our grandsire."
                show mt normal pioneer at left with dissolve
                mt "Kids, after breakfast, everyone gather at the cybernetic club!"
                "The squad leader announced, towering over our heads."
                mt "There will be a squad candle, attendance is mandatory!"
                me "Ahem... Can I ask you a question?"
                show mt smile pioneer with dspr
                mt "You can! But just be careful."
                me "Can I... It's... Well..."
                mt "Why are you embarrassed, like you're asking to go to the toilet? Speak clearly and distinctly!"
                "Immediately the leader went into teacher mode."
                "Oddly enough, it helped me instantly to pick myself up and come to my senses, too."
                me "I'd like to be excused from the candle."
                "Clearly and distinctly informed me."
                me "I don't really want to take part in it, so please allow me..."
                show mt normal pioneer
                show us laugh pioneer
                with dspr
                mt "The squad event is one for all!"
                mt "The only excuse is sickness! Are you sick?"
                me "No."
                th "Yes. I have an acute degree of sociophobia. Let go of me, auntie!"
                mt "Then you have to be there."
                "I shifted my gaze to Ulyana, as if to say, 'See.'"
                "And then she continued."
                mt "Although if you ask me to..."
                show us surp1 pioneer with dspr
                mt "I can assign you something else."
                show us grin pioneer with dspr
                hide us with easeoutright
                "The little one winked at me and jumped out from behind the table."
                show us smile pioneer at right with moveinright
                us "Can I, can I?"
                show mt angry pioneer with dspr
                mt "No. The errand is for Persunov only. And I expect you in half an hour at the candle."
                show us sad pioneer with dspr
                mt "March!"
                hide us with dissolve
                "Ulyana, upset, staggered away."
                show mt normal pioneer with dspr
                "And Olga turned directly to me."
                mt "So your task is as follows..."
                $ alt_day5_me_neu_candle = 4
            else:
                "She made a ziggurat out of the porridge for a while, the consistency of the latter allowed it, and then, spitting, she put the plate aside:"
                show us normal pioneer with dspr
                us "Have you changed your mind yet about yesterday?"
                me "About revenge on the crooks?"
                "I grinned:"
                me "How could I, Random have mercy."
                show us smile pioneer with dspr
                "It seems to have lifted her spirits a little."
                if alt_day4_me_neu_date == 'us':
                    us "Do you think it's dry?"
                    "She asked a strange question."
                    me "What 'dried out', it's raining outside."
                    show us normal pioneer close with dspr
                    us "No, I'm not talking about that."
                    "She lowered her voice."
                    us "I mean the snake. {w}It would be very useful!"
                    me "I don't think so. First of all, it's been too little time, and second of all... It's raining!"
                    "Ulyana nodded understandingly."
                show us smile pioneer with dspr
                us "Look."
                "Generalissimo Sidorova squared her unstretched shoulders and straightened up to her full five feet and cap:"
                us "Tonight the plan was to have some kind of celebration, and in the evening, at the bonfire, an award ceremony. {w}But because of the weather there won't be any awards."
                me "So there's a whole bunch of time to get ready before tonight?"
                me "Where do we start?"
                us "You, specifically, don't! {w}Your job will be to keep the crooks busy and keep them from screwing things up."
                me "When do you want to do everything in general?"
                us "At the bonfire, of course! Or a little after it."
                me "So I won't even..."
                "Upset me."
                show us grin pioneer with dspr
                with vpunch
                us "Hey, don't get sour!"
                "Good spirits were rapidly returning to Ulyana."
                us "If you don't know anything, you won't be able to tell anything when you get caught and tortured."
                "Her 'when' instead of 'if' sounded very interesting."
                me "Thank you for your confidence!"
                "But it was useless to think of trying to get the little one through with sarcasm."
                show us laugh pioneer with dspr
                "She laughed again and clapped me on the other shoulder."
                sl "Ulyana, don't interfere with Semyon's eating."
                us "Your task will be to fight the enemy's counter-intelligence! That's what you do."
                hide us with easeoutleft
                "Showing her tongue in the back of a turned away Slavya, Ulyana dematerialized."
                "And I what?"
                "What. Sighed and, gathering up her dishes, took them to the sink, what."
                $ alt_day5_me_neu_candle = 1
        "Sit with Miku":
            $ volume (1.0,'music')
            $ volume (1.0,'ambience')
            show mi smile pioneer with dissolve
            mi "Oh, hello, Senechka, how are you? You've been a bit groggy this morning, haven't you slept well? I usually get that from the rain."
            "In one word she uttered."
            "I smiled:"
            me "Hello to you too, machinegun girl!"
            show mi upset pioneer with dspr
            mi "But what kind of machine gun am I?"
            "Miku chagrined."
            show mi shy pioneer with dspr
            mi "I'm all for a peaceful solution to any problem, and you call me a weapon! It's even kind of insulting, you shouldn't do that, and... You're kidding."
            "I, no longer holding back, smiled:"
            me "I'm sorry, I couldn't help myself."
            show mi smile pioneer with dspr
            "The sun peeked out from behind the clouds - for a split second even the rain subsided. {w}Miku smiled."
            if alt_day4_me_neu_date == 'mi':
                mi "For some reason I can't sulk at you, even though I know in my mind that you say some pretty hurtful things."
            if alt_day4_me_neu_mi_songs:
                show mi normal pioneer with dspr
                mi "But I wanted to remind you of our last night."
                "I ran diligently through the events in my memory and stopped at..."
                mi "You mean the songs?"
                show mi smile pioneer with dspr
                mi "That's right! {w}I really liked some of the songs you remembered yesterday, can I get you to write me some lyrics and help me pick out some music?"
                "The possibility of escaping from the leader's custody warmed my soul."
                dreamgirl "And it would just be the two of you there, can you imagine? {w}Maybe you'll have something there! Yes! Imagine that!"
                th "You are strictly forbidden to take Miku in portions over homeopathic!"
                th "You're beginning to express yourself exactly like her."
                "I'm thinking about it."
                "Tortured rhetoric didn't seem like such an attractive pastime..."
                th "On the other hand, if she doesn't talk and does strictly what she called me to do, we might well get along and even get along under the same roof."
                me "You know, let's do that!"
                "Heartily, I nodded."
                show mt normal pioneer at left with diam
                mt "I'm afraid it won't work."
                "The squad leader approached in her usual manner - silently stepping out of subspace somewhere behind me."
                show mi upset pioneer with dspr
                mi "But why? What about the evening performance, Olechka Dmitrievna, you said you would help me!"
                "Miku shifted her gaze from me to the squad leader at a loss."
                show mt smile pioneer with dspr
                mt "I didn't say I'd give you my most trusted pioneer for the day, did I?"
                "Olga grinned."
                mt "I promise to keep him occupied only until lunchtime - and then let him decide for himself what he wants to do."
                show mi sad pioneer with dspr
                mi "Well..."
                "It seems a few more hours of watching the rain to the keyboards didn't inspire the active Japanese girl one bit."
                me "What do you need?"
                "I winked encouragingly at Miku."
                show mt normal pioneer with dspr
                mt "There's a campfire planned for the morning."
                "The squad leader shrugged her shoulders serenely."
                mt "And I need someone to help me get ready. {w}My choice was you. Any more questions?"
                "Without waiting for any continuation, she headed for the exit."
                hide mt with moveoutleft
                mt "In ten minutes at the clubs."
                "I threw an apologetic look at the saddened Japanese girl and followed the squad leader."
                $ alt_day5_me_neu_candle = 2
            else:
                show mi smile2 pioneer with dspr
                th "There's something about you that almost shuts down my powers of reasoning."
                "Thoughtfully I conclude."
                me "So what did you want?"
                show mi shy pioneer with dspr
                mi "Me? {w}But you're the one who sat with me."
                "She even stopped gibbering with surprise."
                mi "Don't confuse me with yourself!"
                "I shook my index finger admonishingly."
                me "I'm the one who never wants anything from anyone - and you, without blinking an eye, swallowed a grudge. {w}So you want something from me."
                me "What do you think of my deductive powers?"
                show mi laugh pioneer with dspr
                mi "Almost Sherlock Holmes!"
                "A little chuckle from a Japanese girl."
                if alt_day4_me_neu_date == 'mi':
                    mi "But you helped me clean yesterday, and..."
                    me "No! Don't even think about it."
                    show mi sad pioneer with dspr
                    mi "Listen to me!"
                show mi normal pioneer with dspr
                "Miku was quiet for a while, forming a request."
                mi "Olechka Dmitrievna asked me to help for tonight - to pick up the repertoire and so on. {w}Can I ask for your help?"
                me "Uh... Camp songs?"
                show mi smile pioneer with dspr
                mi "Yes! {w}Well, will you help?"
                "If she's saying it that way..."
                "I nodded and opened my mouth."
                mt "Of course she will."
                "Olga dropped her cold, wet palm on my shoulder."
                show mt normal pioneer at right with moveinright
                mt "But first he will help {b}me{/b}."
                show mt angry pioneer with dspr
                "Olga pinned me down with a look."
                mt "Isn't that right?"
                "I shuddered."
                me "Y-yes... I mean, yes! You first!"
                show mi shocked pioneer with dspr
                mi "Senechka, are you..."
                me "It's okay."
                "My tone contradicted the words."
                show mt smile pioneer with dspr
                mt "I need someone to run a toy library for the kids. {w}Guess who I gave that responsible assignment to?"
                "The squad leader smiled irresistibly."
                me "Is it really Alisa and Ulyana?"
                "If I'm gonna play the fool - then I'm going to do it to the end!"
                show mt laugh pioneer with dspr
                mt "Ha-ha-ha, Semyon, you're such a joker!"
                show mt normal pioneer with dspr
                extend " No."
                mt "Don't go anywhere from the canteen, give you games and pioneers."
                hide mt with dissolve
                "Without waiting for my answer, the squad leader evaporated."
                $ alt_day5_me_neu_candle = 3
        "Sit alone":
            $ volume (1.0,'music')
            $ volume (1.0,'ambience')
            "I have decided that I will continue the blessed tradition of the solitary meal."
            "You have to eat thoughtfully, or you won't."
            "More distractions. What the hell!"
            if alt_day4_me_neu_mt_diary:
                $ counter_mt_7dl += 1
                if (counter_un_fz_mt_transit == 3):
                    $ counter_mt_7dl += 2
                show mt normal pioneer with dissolve
                mt "Semchik, are you busy?"
                "Without waiting for an answer, Olga, still smelling of rain, plopped down next to me."
                "She looked wrinkled and sullen, and the carefully chewed exhaust suggested that the leader had not been bored during the night, oh, not bored."
                me "Olga Dmitrievna, what are you going to do before dinner?"
                "I'm casting my fishing rod."
                show mt smile pioneer with dspr
                mt "Are you going to ask me out?"
                me "No! But..."
                show mt laugh pioneer with dspr
                mt "Okay, just kidding."
                mt "I think I'll write off a couple of cookies and tea in the kitchen and hold a meeting in the clubs."
                "Suspiciously easy she replied."
                "And then immediately explained the reason for her accommodativeness:"
                mt "And one pioneer would be a good help to me in that!"
                me "Slavya?"
                show mt grin pioneer with dspr
                "Olga hummed{w=0.5}{nw}"
                show mt sad pioneer with dspr
                extend ", but then she grimaced and took a sip from a cup of something resinous, which has no place on a pioneer table."
                mt "In short: finish it, don't leave, we'll go to the warehouse for provisions."
                dreamgirl "Eh, cried our reading!"
                show mt normal pioneer with dspr
                mt "And then to the clubs. You got it?"
                "Clenching her fist, apparently as an illustration of what awaits me in case of escape, she got up with a grunt and wandered to the staff tables, from where Violetta Cernovna was already watching us."
                hide mt with moveoutleft
                $ alt_day5_me_neu_candle = 2
            else:
                "As the saying goes, nothing was foreboding..."
                "And woe to that which shall foreshadow!"
                "I gave a particularly affectionate glance to Slavya, who wanted to sit down next to me, so I had won my right to a quiet meal in full."
                "And it wasn't that I was nasty and bastard, I just got myself up, but I forgot to wake me up."
                "And I felt a little boiled."
                "Nothing you couldn't handle for three hundred minutes on a full stomach, though."
                dreamgirl "Once you've eaten, you can sleep, and once you've slept, you can eat!"
                th "You speak the truth!"
                "I grinned, and after finishing my last sandwich, I got up."
                "My pillow was waiting for me!"
                $ alt_day5_me_neu_candle = 1
    stop music fadeout 2
    stop ambience fadeout 3
    play sound sfx_open_door_1
    $ alt_pause(1)
    scene bg ext_dining_hall_near_rain_7dl with dissolve
    return

label alt_day5_me_neu_rain:
    scene bg ext_square_rain_day_7dl with fade
    play music music_7dl["are_you_there"] fadein 3
    "Sometimes I can stop and freeze in a moment of a soul flying down from the balcony - like a cry for help or a plea for attention."
    "Though I've never wanted other people's attention."
    if herc:
        "And I understand perfectly well that there will never be a Sychev street, a Sychev serum, or even any celestial body named after me."
    else:
        "And I'm well aware that there will never be a Persunov street, a Persunov serum, or even any celestial body named after me."
    "Because to the sound of dubstep, it's so convenient to lead an unsightly existence, jumping from matter to energy level - and back - a few million times in an instant."
    "It's not scary to die when you realize that everything will be left exactly the same after you - opportunist logic, yes. {w}But realistically the universe doesn't even have to collapse, occupying the resulting vacuum."
    "Since behind the sheen of joy or the murky flicker of indifference, under the thin film of happiness, under the arrogant gaze from all my one hundred and eighty-five centimeters... There's nothing there."
    "Once upon a time I tried to tell those around me that: to take them all by the Adam's apple and whisper in their ear soulfully: 'You're lying, little dove, you're not there, why are you fooling around?'"
    "But rather than toil counting the birds..."
    if loki:
        "I may have been influenced by the story after which everything went downhill - a story about human stupidity and the inability to simply listen to the voice of reason."
        "After all, she called me."
    elif herc:
        "I guess I was so influenced by the military and my mother's death, after which I realized that I couldn't be sure of my future, that people didn't care about other people."
        "There is no justice."
    elif dr:
        "One day, kneeling next to the warm plastic side of a cooling 'Renault' and watching the rain wash away the blood, I turned to myself."
        "And asked myself the question I've always tormented those around me with."
    "It's pretty painful: at twenty-three to twenty-five to realize that you're absolutely no worse than the people around you, and no better than them. You're the same."
    "And the only difference yours is that you're looking at the world in first person."
    if alt_day5_me_neu_candle == 1:
        "All my life the rain has had the most depressing effect on me."
        "Especially when you're in camp and there's less and less time to rest."
        "And you're sitting indoors at a long table with joystick tails stretching across it, and on the screen, Kabal is finishing a ten-punch combo, and you get elbowed in the side so you don't get cocky."
        "Or standing under the visor, the gurgling tobacco of that cheap cigarette quietly crunching behind you, and the rhyming lines successfully laying to the tapping of the water, and you holding your palm at the very edge of the visor and maneuvering between the falling drops like a racer."
        "More often than not, though, it's Keiko Matsui in her headphones, the soft damp tapping on her hood, and the inexplicable happiness of being alone against the whole world."
        "Here we are now: well aware that no one can see me, I smiled heartily and hurried back to the cabin."
        "To sleep."
    elif alt_day5_me_neu_candle == 2:
        "I've never been a particular fan of the Soviets or the Soviet regime."
        "But I have to admit that the Party knew how to manage people, even without direct brainwashing by the mass media."
        "It's just called a little different now, propaganda, psychology of the masses."
        "Pedagogy."
        "And the clearest example of this is that I don't even think about sulking at our squad leader, who, without wasting much time trying to persuade me or try to change my mind, somehow cleverly put me in charge."
        "And here I am, unsociable, sullen and unkind - rushing to help our lazy and harmful squad leader."
        "I caught myself smiling. In anticipation."
        me "Olga."
        "I pronounced with one lip."
        th "Bitch."
    else:
        "I was almost to the checkpoint when a thunderous voice came from behind me:"
        mt "Semyon!"
        show mt angry pioneer with easeinright
        "That's right, our kindest squad leader honored me with her attention."
        me "Ah... Hello, Olga Dmitrievna!"
        "I waved to her."
        me "How are you doing, how's your mood?"
        "I prudently decided not to ask about the children."
        mt "Listen, you're the sneakiest bug I've ever met."
        show mt normal pioneer with dspr
        "After thinking for a while, she changed from anger to mercy."
        mt "But that doesn't exempt you from your party assignment."
        me "Hmm... And if I don't?"
        show mt smile pioneer with dspr
        mt "Then you'll have a very different conversation."
        "The squad leader smiled cheerfully."
        "And that smile made me feel really uncomfortable."
        mt "Around the circle to fulfill the party assignment - march."
        show mt smile pioneer close with dspr
        "As on the first day, she was there and turned me in the right direction and gave me a gentle nudge, hinting at the eternal Soviet 'if you can't do it - we'll teach you, if you don't want to - we'll make you.'"
        hide mt with dissolve
        "With a sigh, shoulders slumped, and a look of universal sorrow, I staggered off in the direction indicated."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_arrest:
    play ambience ambience_7dl["rain"] fadein 3
    play music music_7dl["to_the_sunrise"] fadein 3
    scene bg ext_clubs_rain_7dl
    show mt normal pioneer at zenterleft
    with dissolve
    mt "Katerina found them yesterday before lights out, returning from behind the camp grounds."
    "The girl reported, waving her hand toward the porch, where I noticed the familiar figures."
    "I knew that our meeting yesterday was by no means our last."
    "Not at all."
    me "Hello."
    show mt smile pioneer at left with moveinleft
    show dn dontcare pioneer at zenterright
    with dissolve
    if loki:
        "Danya waved silently at me as we went up on the porch and squeezed their warm company a little."
    else:
        "So the nameless kid nodded to me like an old acquaintance."
    show al normal pioneer at fright
    show tn normal pioneer
    with dissolve
    mt "It's good that you know each other."
    if dr:
        dn "We don't."
        show mt normal pioneer with dspr
        mt "Really? Well, let me introduce the second squad's headache."
        mt "We have Ulyana, and they have Daniil."
        $ meet('dn', 'Danya')
        dn "Danya."
        "He held out his hand, which I immediately shook."
        "The other two guys, as it turned out, were named Alka and Tonik."
        $ meet('al',u"Alka")
        $ meet('tn',u"Tonik")
    mt "Well, here's the situation: this isn't the first time they've been caught running away, but the rules are strict."
    "Danya shook the blade of grass clenched in his teeth, as if to underscore the rigidity of the rules."
    mt "It is strictly forbidden to leave the camp without an escort!"
    mt "That's why they are punished today."
    me "I see. And how are they punished? They won't go to the candle?"
    "To tell you the truth, it didn't seem like such a terrible punishment to me."
    "What's the matter, I'd gladly allow myself to be punished in the same way!"
    show mt laugh pioneer with dspr
    mt "Semyon-Semyon..."
    "The girl shook her head."
    mt "Did you hear yourself?"
    mt "One candle does not limit the life of a camp."
    me "I guessed as much."
    "I reported it."
    mt "After camp activities, by about noon we'll all gather in the canteen, as we usually do in the rain, bring a TV, plug in the VCR, watch a movie."
    th "What?!"
    mt "I thought you knew."
    "Smiling, she continued."
    mt "That's why I was so surprised you volunteered to punish yourself."
    show mt normal pioneer at left
    show dn sick pioneer at right
    with move
    "Danechka showed with all his appearance an attitude toward both movie candles and camp rules."
    mt "They are punished for a cause."
    mt "And you..."
    me "Can I recuse myself?"
    show mt laugh pioneer with dspr
    mt "No!"
    "She laughed."
    mt "You know what you're talking about."
    show mt smile pioneer with dspr
    "Rummaging through her pockets, she pulled out a key:"
    mt "It's eleven o'clock, the clubhouse is at your disposal until lunchtime - so I don't see or hear anyone. Any questions?"
    "I shook my head."
    mt "Then adios! They promised to put on 'Irony of Fate' tonight, so good luck to you boys."
    hide mt with dissolve
    "After waving goodbye to us, the squad leader left."
    me "Let's go!"
    stop music fadeout 3
    "I commanded, unlocking the heavy padlock."
    stop ambience fadeout 4
    scene bg int_clubs_male_rain_7dl with fade2
    play music music_7dl["my_only_hope"] fadein 3
    "We sat down on the stools that were available, looking at each other warily."
    "I on one side, and my... subordinates on the other."
    "Just as it happened yesterday."
    "They already had their own folded, melded link, capable of standing up to anyone-just because they were together."
    "A confrontation."
    me "Are you in town together, too?"
    "I asked just to say something."
    show dn normal pioneer with dissolve
    dn "Yep. Battle Star."
    "Danya's answer was unclear."
    me "There are three of you."
    "I noted."
    show dn smile pioneer with dspr
    dn "Also Ulya."
    me "Four."
    dn "And... You don't know him, anyway."
    "They're down for a conversation. That's not bad."
    me "Battlestar."
    "I said again."
    show dn unsured pioneer with dspr
    dn "Yes."
    me "Now there's four of us, so that makes for a weird star, too."
    dn "Yes. It's Japanese. It's called a shuriken."
    "We're silent again."
    with fade2
    me "It's like we've been exempted from candle, but it's also like we have our own."
    "Both of Danya's orderlies nodded warily, revealing their own opinions for the first time."
    me "Then how about some tea?"
    show dn smile pioneer with dspr
    dn "Is there any?"
    me "As far as I know our cyberneticists, there definitely should be."
    me "So get up, look for a boiling pot, a can, water, tea, cookies - anything you can find!"
    $ meet('tn', 'Tonik')
    tn "You can't do that."
    "He who, with some effort, I recognized as Tonik, spoke up."
    me "You can."
    me "Even arrested men are entitled to bread and water!"
    "The boys laughed and gyrated around the room."
    scene
    $ renpy.show("bg int_clubs_male_day", what = Dawn("bg int_clubs_male_day"))
    with joff_l
    "A few minutes later, everything we needed was found."
    "And this time we weren't seated the way we were at the beginning."
    "It was as if I wasn't allowed into their company in any way."
    "And it wasn't that it embarrassed me in any way - fiddling with the little things didn't make me feel at all."
    "But these... they were different."
    "Self-sufficient, whole, not dependent on anyone or anything."
    "They didn't have the stiffness of children, the swagger of backyard hooligans, nothing like that."
    "There was a certain wariness of people looking out for the perfect stranger who had decided to cut into their usual world - that's true."
    "But I guess Ulyanka's trust turned out to be the best recommendation?"
    "Or the fact that I didn't act the way squad leaders usually do, counting only by the head."
    show dn smile pioneer with dissolve
    dn "We saw the sand barge off yesterday."
    "Danya reported, sipping his tea."
    dn "The captain was waving from the bridge, smiling. So it was for a reason, wasn't it?"
    me "People usually put beacons for that purpose."
    dn "It's a pity they don't do that with us."
    dn "A lighthouse needs a keeper."
    dn "I'd like to be a keeper of one."
    me "Why?"
    show dn sad pioneer with dspr
    dn "It makes me sad to think that people could help ships but don't."
    me "Does it matter?"
    show dn smile pioneer with dspr
    stop music fadeout 4
    play ambience ambience_clubs_inside_day fadein 1
    dn "Very!"
    dn "Only water finds the way, and those who walk on it."
    me "The way where?"
    play music music_7dl["uneven_me"] fadein 3
    show dn normal pioneer with dspr
    with fade
    dn "For our star, it all started with Mirya three years ago."
    me "The one I don't know?"
    "Danya nodded and continued:"
    dn "He was the one who found the place where things go right, took us there the first time."
    dn "But he was like you that year - seventeen years old, so he never came back."
    dn "And we can't find our way any farther on our own."
    dn "No way."
    me "How did you get caught just outside the territory, we were walking together?"
    "Danya waved his hand lightly."
    dn "Katushka is kind, if it wasn't for Olga, she would have scolded and forgiven."
    dn "But as it is, I have to do my time."
    me "Anyway, as long as it's raining, there's nothing to do."
    dn "Nothing to do."
    "Danya nodded accordingly."
    "And, looking suspiciously out the window to see if anyone was looking, he casually asked:"
    dn "Have you seen the dream about the Flares?"
    me "I have."
    "I answered honestly."
    me "I woke up with a burned palm."
    "The boys looked at each other, and then Alka, who had apparently been chosen to be the herald of the star's will, asked:"
    $ meet('al', 'Alka')
    al "Will you go to the quarry this afternoon?"
    me "What if it rains?"
    tn "It won't."
    "Tonik said in a solid bass voice."
    dn "You can trust him, he can sense the weather like nobody else."
    me "He'd better sense trouble."
    show dn normal pioneer with dspr
    dn "What's there to smell - it's always around."
    dn "At the end of the shift they'll write in the report about 'slacking off and systematic violation of the regime'."
    "In a nasal voice Danya said, and I knew he was mocking someone."
    me "Then why..."
    tn "You can't do otherwise."
    "Tonik explained seriously."
    al "We've already had our star broken because of Mirya."
    me "What about him?"
    al "Never mind. So will you go?"
    me "I will."
    "I answered."
    play sound sfx_open_door_clubs
    $ alt_pause(1)
    "The door clicked softly, and, letting in a sheaf of splashing, Electronik appeared on the doorstep."
    show el smile pioneer at left with dissolve
    el "Sitting down, prisoners?"
    "He asked cheerfully."
    me "Uh-huh."
    el "They sent me for the TV."
    el "We're going to watch a movie now. Are you coming?"
    me "No."
    "I answered for everyone."
    me "We're prisoners."
    show el grin pioneer with dspr
    hide el with moveoutleft
    "With a skeptical chuckle, Electronik disappeared into the back room, and came out a few minutes later, heavily laden with a television set, a video double."
    "On top of the TV were several videotapes of movies, all wrapped up in a huge piece of polyethylene film."
    "After bowing jokingly to us at the door, he went outside."
    me "Why are you so indifferent to movies? Isn't it interesting?"
    "Asked me as the door behind Electronik slammed shut."
    show dn smile pioneer with dspr
    dn "No. It's just that you can't go to the movies with Tonik."
    me "Why is that?"
    th "Says he eats popcorn noisily, laughs?"
    me "Is he being uncivil?"
    show tn smile pioneer at left with dissolve
    tn "No, I'm being very, very quiet."
    dn "Only he has his own opinion about what should happen on the screen."
    me "So?"
    show dn normal pioneer with dspr
    dn "No, nothing."
    "Danya bristled again, fending off his curls like barbs."
    "Like I'm trying to get into a place where I'm not supposed to be again."
    tn "Let him see."
    "Judiciously stated Tonik."
    tn "It's not like I'm sorry."
    "Rising from his stool, he walked over to a place littered with pieces of solder, soldering irons, plastic parts, screwdrivers, and other junk, and pulled out a very large magnifying glass on a tripod."
    tn "You can do that without spoiling anyone's mood."
    dn "Here we go."
    "Danya shook his head."
    "But obediently he found both a big piece of vatman paper and a black cloth."
    "Long, long wizarded over them, then set the resulting construction to the magnifying glass already fixed on the window sill, placed a box beside it:"
    dn "Look..."
    "And I looked."
    scene
    $ renpy.show("bg ext_clubs_rain_7dl", what = Desat("bg ext_clubs_rain_7dl"))
    show anim_grain
    with dissolve
    "It's like being a child with loneliness, darkness, and a slide projector, the heat of whose lamp makes you wary of moving away, but you can't help but keep turning the film's knob."
    "There, on the whitewashed wallpaper, is an action unfolding - with a capital letter - that takes you along, leaving both time and nonsense like sleep or hunger beyond perception."
    "A world of filmstrips and slides, almost as good as books in terms of dissolving into itself."
    "There was only one flaw in all this beauty."
    "Short-lived."
    "The lamp died, and I couldn't understand why I couldn't give up on a world that was better than mine in so many ways."
    "I just couldn't."
    "So I kept coming up with new ways of reading."
    "But eventually I settled on reading directly from the tape because I had enough power of vision."
    "But all this was a kind of prelude to what I found in my quest to bring the action to life on the wall."
    "One day I took some lenses with a correction tube, shook all the unnecessary stuff out of the projector, and pointed the viewfinder's solution into the weeping gray sky and looked up to where the lamp had always been."
    "I wanted to see what the lamp saw while it wasn't working."
    "I was then piously convinced that all things have a life of their own when their owner is distracted or asleep."
    "So I wasn't surprised to see the sky, the piece of glass with the drips running down it, and the cathedral in the distance."
    "Except that it became all unaccustomed, the water flowing upward."
    "But at that point my tapes had almost run out, and the library had only Chekhov's Pieces left, so..."
    "I plunged into a world turned upside down."
    "And I'm in it now."
    "The scent of asphalt relaxing after the heat, the rumble of the wind in the yard-well, and the silence of solitude wafted into the air."
    "On the gray side of the box, an image shuddered: water droplets flowed upward, gray clouds filled the entire bottom of the box."
    "I myself shuddered at the thought-feeling concentrate that surfaced in my mind, {i}rapport{/} whipping there that a nasty weakness appeared in my knees."
    "So immediately I hastened to remind myself that I'm a big, senior..."
    me "So what's the big deal? Projection."
    "I stated dismissively."
    "And Danya and Alka looked at me with such pity that I immediately regretted my words."
    "I'm big and older... and a fool. Who needs my disregard here?"
    dn "You watch, you watch."
    "Nodded Danya."
    "And I stared into the box, on the side of which something unexpected was going on."
    "For starters, the rain that had been coming down there the whole time suddenly began to subside."
    "Even though the downpour that had been pouring outside didn't think it would stop."
    "Then the clouds parted, freeing the box, the moon rose on the floor..."
    "A few minutes later, under the leaden gray clouds, a broken, dusty road rushed to the horizon, and a tiny LIAZ was scrambling diligently down the same road to the horizon."
    "It slowed down at the dilapidated stop, opened the doors as if listening in."
    "It suddenly occurred to me that perhaps this bus had ridden here all its life, and all its life it had stopped at this very stop, picked up its old passenger, and rushed on."
    "Those who have known each other all their lives are willy-nilly very close, either by friendship or hatred, and now that the passenger is gone, the bus is very sad to clamber and clamber on."
    "Alone."
    "I shrieked and accidentally kicked, defocusing, the image, to the point where I felt cold and stuffy."
    "The image shuddered, a pertinent and logical perspective of rain magically superimposed on a running bus flashed, something red flashed, a pile of snowflakes flew into the frame on the right, and..."
    dn "What are you doing, put it back!"
    "Muttering an apology, I put the box back in place, twisted it around for a better view, looked closely."
    "It was as if someone had pressed rewind, everything unnaturally, twitching, moving in complete dissonance."
    "Something ran forward like a bus, but the willows nestled by the ditch, on the contrary, swayed in the wind, clearly blowing in reverse."
    "The highway changed to the already familiar asphalt parking pocket framed by the outstretched silhouettes of power line towers, but there too the invisible storm was raging."
    "The oblique threads of rain smeared to a hatch across the entire field of the film, the bus changed to another, more touristy-looking one, the picture changed back to the view out the window, and for a second I thought it was over."
    "But no."
    "It was different. And the rain was different."
    "For a second, a structure fell upward, very much like an antenna."
    "The door ajar, and a raincoat-wrapped girl with very familiar ponytails stepped off the porch."
    "She looked thoughtfully down at where the antenna had fallen from, then at her watch, and, shivering, wrapped herself up tightly, hurried back indoors."
    "Sanich walked with his back to the front with his camera, lurching in the wind."
    "Two guys in khaki shirts, a little older and a little younger, rode their bikes."
    "Soon the storm subsided, and the sun that had peeked out from behind the clouds hid behind the horizon again."
    "It went dark."
    "And a few seconds later, raindrops were streaming up the box again."
    scene bg int_clubs_male_day
    with fade2
    tn "That's all."
    "Tonik reported."
    me "Ah... What was that?"
    show dn smile pioneer with dspr
    dn "Tonik is screwing around again."
    "With difficulty lifting the tripod, he put the glass back on the cybernetic table."
    al "That's why you can't take him to the movies."
    al "If he thinks there's something wrong happening on the screen..."
    show dn smile pioneer with dspr
    dn "We won't ask you to keep quiet about it. You know how it is."
    me "No one will believe me?"
    show dn grin pioneer with dspr
    dn "But you can try."
    th "No, thank you. I don't need to be called a psycho."
    "Something told me that Tonik's gift, like my ability to approach the moon as a child, was completely controllable, and in the case of the men in white coats, he would just be surprised and no miracle would occur."
    me "Where did he learn?"
    tn "Always knew."
    stop music fadeout 5
    play sound sfx_7dl["eat_horn"] fadein 1
    play sound2 sfx_open_door_clubs_2
    $ alt_pause(1)
    show mt smile pioneer at zenterright with dissolve
    "Our conversation was interrupted by the horn blaring from the bell just above the porch, and by Olga Dmitrievna appearing."
    mt "On the occasion of dinner the prisoners are granted an early amnesty!"
    "Cheerfully she shouted, peeking through the door."
    mt "Semyon, you're on control to make sure these wogs wash their hands and don't get lost on the way to the canteen."
    me "Roger."
    "I nodded."
    mt "See you in the canteen then!"
    hide mt with easeoutright
    "Tossing me the key to the lock hanging there, Olga vanished."
    "And I, still shaking my head and trying to remember what was happening, nodded at the door to the trio who had already taken their seats at the table."
    me "Do you need a special invitation? To the dining room, march!"
    "Giggling about something of their own, the trio squeezed past me through the door and drifted into the slowly subsiding rain."
    $ counter_us_7dl_px = 2
    stop music fadeout 4
    stop ambience fadeout 3
    stop sound_loop
    return

label alt_day5_me_neu_gaming:
    scene bg int_dining_hall_rain_7dl with blinds_r
    play music music_7dl["gonna_be_ok"] fadein 3
    play sound_loop ambience_medium_crowd_outdoors fadein 2
    "In the canteen I was extremely glad that I didn't have to argue with the squad leader about my sudden assignment."
    "Otherwise I would have had to set it all up, wipe it down, and so on..."
    "I made a note to repay today's duty kindness."
    me "That's exactly who I need... Electronik!"
    show el normal pioneer with moveinright
    "The cybernetic flinched and pulled his head into his shoulders."
    el "Why? I'm nothing, I'm nothing at all!"
    "He mumbled. {w} I waited patiently for his monologue about sick fish and a hamster without food to end."
    el "Ah, Semyon, it's you..."
    "It came to him with some delay."
    me "I need help setting up the tables, I can't do it alone."
    el "But I... Oh, well..."
    "The guy obediently followed me and grabbed the first table indicated."
    "Only now did I notice one interesting thing:"
    me "Where's Shurik?"
    th "Now they'd give him a rag and send him away - he'd be useful."
    show el sad pioneer with dspr
    if alt_day3_technoquest2:
        "Electronik guy was embarrassed:"
        el "Yeah, see, here's the thing."
        "His eyes darted from side to side."
        el "It just so happens that Shurik... uh... well, he, well..."
        me "Yeah?"
        show el normal pioneer with dspr
        el "He disappeared yesterday."
        me "Uh-huh, and?"
        el "And this morning he was found asleep on the porch of the infirmary."
        el "Violetta took him away and put him to sleep in her isolation room."
        el "That's the story."
        "Try as I might, I couldn't find anything criminal in the guy's story, but he looked like he'd blabbed some military secret to me."
        me "I see."
        dreamgirl "Brilliant answer!"
        th "Shut up!"
        me "Just don't tell anyone else, okay?"
        "I could hardly contain my laughter."
        me "I'm alright, I'm a grave and never to anyone. You can trust me."
        dreamgirl "Calm down. You've got tables to haul."
        "Electronik nodded."
    else:
        el "They took him to the hospital."
        me "Is it serious?"
        th "We don't need a quarantine for some lousy whooping cough..."
        "With incomprehensible anger I thought."
        el "He's got a cut."
        "The cyberneticist turned away."
        el "On his arm. It's deep. Took him to surgery to stitch it up."
        "He didn't seem to be too keen on the subject."
        me "Was he going to..."
        el "Yes."
        show el serious pioneer with dspr
        el "You didn't want to help us."
        "Electronik got serious."
        el "We had to do it ourselves - me and him, we're both terrified of heights."
        el "Anyway, industrial accident. And let's drop the subject."
        th "Well, if it's really bad, we'll definitely be informed. I guess."
        "He sighed."
        show el sad pioneer with dspr
        el "And I was so hoping to finish assembling our project after all!"
        me "Which one?"
        show el upset pioneer with dspr
        el "Uh... Never mind."
        "He's chickening out."
        me "No, seriously?"
        show el normal pioneer with dspr
        el "Sorry, Semyon, but no. It's not my secret, I can't tell you."
        "He looked extremely sad that he couldn't tell me everything, but I didn't insist."
        el "I'm sorry."
        "For some reason he repeated again."
    "Little by little, the tables moved around the perimeter of the room, and the long benches along them allowed the little ones to be seated as the rules of the game demanded."
    el "So you're going to be watching the little ones this time?"
    me "Uh... Obviously."
    el "You see..."
    show el smile pioneer with dspr
    el "Last time it rained, Alisa sat with them..."
    me "And?"
    "I grinned, imagining the possible extent of the destruction."
    th "The canteen survived, though. {w}And even the walls were in place."
    me "How did it all end up?"
    el "The whole squad had to clean up - and even dinner was postponed for half an hour."
    th "I can imagine!"
    me "So what happened?"
    "Electronik guy shrugged his shoulders:"
    el "Basically, got into the game vault, took out the marbles boxes..."
    me "...let me guess!"
    "For a split second I even wished I had started dating the redhead."
    me "You're having a capitol war?"
    el "Capitols?"
    me "Water balloons, huh?"
    "He nodded."
    me "That's what I say - capitos. {w}An old children's game."
    "I didn't bother telling him about the fact that we used to throw capitoches from the twelfth floor."
    "It might have damaged his fragile childlike psyche."
    with blinds_l
    "In the meantime, we finished and Electronik, waving off, has departed on his own business."
    hide el with dissolve
    "Apparently, putting together his secret project that he wasn't allowed to tell anyone about."
    me "I wonder what it could be?"
    "I muttered under my breath, wavering between another dorky craft and a porn magazine."
    with fade2
    "Okay, all of that can wait. Right now the most important thing is to survive until lunch."
    show mt normal pioneer far with dissolve
    mt "Did you manage? Well done."
    show mt normal pioneer with dspr
    "Olga Dmitrievna left her raincoat at the entrance and came up to me."
    mt "You don't have to worry about the younger ones, they know the order of the toy library."
    me "Then why am I here?"
    "Since everyone here is so all-knowing."
    show mt smile pioneer with dspr
    mt "So you don't get bored and get bored out of your mind."
    "She winked."
    mt "Come on, let's get you some games and let's start entertaining our little ones."
    me "Shall {i}we{/i} start? {w}Are you determined to keep me company?"
    show mt grin pioneer with dspr
    mt "Don't get your hopes up."
    mt "Unlike you, I've got a whole bunch of big-headed brats to think about, all of them as tall as me."
    me "Poor you, poor you."
    "I pretended to sympathize."
    show mt smile pioneer with dspr
    me "And you work without rest, and the pioneers do not obey, and everything in general is bad."
    show mt grin pioneer with dspr
    mt "Yes, pity me, pity me!"
    play sound sfx_keys_rattle
    "With a giggle, Olga planted a bunch of keys in her palm and, catching a transom key in the air, opened the heavy wooden door with it."
    th "I wonder why these games are kept in the canteen?"
    "When I was a pioneer, we had a separate building for that - combined with the video room and the camp director's office."
    "And the arcade didn't work on an ad hoc basis, but every day."
    th "No staff?"
    show mt normal pioneer with dspr
    mt "Your job is to hand out the chips and boxes to be signed and make sure the kids don't scuff them somewhere... i.e., that everything is intact. Understand me?"
    "Meanwhile, the leader was explaining, pulling boxes of games and chips from the shelves."
    me "Nothing complicated."
    "I nodded understandingly."
    mt "There are decks of cards for Monopoly and Capture, and all players will have to sign for them - a collective responsibility."
    mt "I think you can handle the rest."
    me "I will."
    mt "There's also a record book."
    "There used to be 96 sheets in it, but since then the lion's share of them have been scattered to the winds like cranes."
    "Or airplanes. Letters of happiness. You never know..."
    mt "And a pen. Red for cards, blue for general notes. Let them sign in front of you, I know them."
    "In the pocket on my chest turned out to be a two-color Soviet pen with red and blue flat buttons."
    mt "Every time they try to steal it away."
    "The squad leader complained."
    mt "You might as well tie it to the book with a rope."
    me "That's also a thought."
    "Accordingly, I nodded, remembering the modern post office and Sberbank branches - though the pens were successfully taken away from there, too, if desired, despite the fact that they were attached to the counter."
    "A few minutes and we are greeted by an enthusiastic buzz of voices."
    "The kids are clearly bored."
    "And they don't have a 'Sega' or at least a video player with Van Damm movies."
    "And, unlike me, they weren't self-sufficient enough to pick up a book and shrug off their surroundings."
    "Which means give them social interaction all over the place!"
    "No wonder the Capitol Wars are so popular here."
    "Or like computers - when I was in school, we had an old 486 that you could play 'Flash' or 'Fatman' or 'Doom' on, but in general the computer lab was only popular with geeks."
    "But once our sponsors brought us the Pentiums with the first 'Quake', set up a local network, and then someone was able to play the first game over TCP/IP..."
    "In short, another prime example of how much man needs to interact with his environment."
    "These kids will be graduating high school when the first part of the Flynn Taggart saga sees the light of day."
    "They'll probably be the ones whose modems will get heated during fragmatches and whose eyes will forever take on a reddish hue."
    "And I envy them in some ways - they're so unspoiled and unspoiled by the benefits of civilization."
    "Fortunately, I had a notebook, a pen, and a few scattered thoughts in my head."
    if 'nwsppr' in list_clubs_7dl:
        th "Perhaps we can sneak them in under the guise of an article, since the most prying one is temporarily out of the game?"
    hide mt with dissolve
    "After jokingly bowing out, Olga gladly bade me farewell, leaving me to be torn apart by the crowd of minors."
    "Though, judging by their wary glances, the wariness was mutual."
    me "All right, kids."
    "I dumped the games on the table."
    me "Everyone knows the order, in order, come up and sort out the games."
    me "For the big games, come up in batches at once. Is everyone clear?"
    "At a glance, a few pioneers stepped out of line and, stepping aside, murmured about something."
    me "Oh, hello."
    "A red-eyed pioneer I know."
    pi "Hello, I'd like to play checkers."
    me "And you'll play checkers?"
    "I'd sooner believe that Dvachevskaya reads!"
    pi "Yes!"
    me "You can't lie at all. Sign here and march to the corner table so the checkers don't get scattered all over the room."
    pi "Thank you!"
    "He glowered and, signing off in the signatures column, took the future machine-gun battery behind him."
    "When you're a kid, you look at most adult inhibitions as something personal."
    dreamgirl "Well! They forbid you to play Bouncers because they hate you and want to ruin your mood."
    dreamgirl "And when they chase you to brush your teeth, that's them getting revenge for something!"
    th "Something like that!"
    "Besides the familiar boy with the Chapaev battery games, I didn't know anyone else here, so the line moved fast."
    "Not a few minutes later, all the pioneers had sorted themselves out on their desks, leaving me alone with a checkered piece of paper and a blue pen."
    dreamgirl "So... Hello, my beloved Marfa Matveyevna!"
    th "Isn't that Katerina?"
    dreamgirl "Don't be a gung ho. In general, it's funny when you type faster than you write it by hand?"
    "Funny, of course. I was even taught the basics of shorthand once - if necessary, with a little refresher skill, I could very well put thoughts down on paper at the same speed as they are spoken."
    th "I mean, normal people spell!"
    dreamgirl "That's right! Know your place and don't even try to shorthand our Japanese razzle-dazzle beauty!"
    show blink
    "I closed my eyes and exhaled."
    stop sound_loop fadeout 6
    stop music fadeout 3
    $ alt_pause(2)
    hide blink
    mt "How's it going?"
    "I flinched."
    scene bg int_dining_hall_rain_7dl
    show mt normal pioneer at right
    show unblink
    th "Olga snuck up on me."
    mt "So how's it going?"
    me "Slowly."
    "I shrugged."
    mt "Finish your writing, it's lunch in an hour, we have to set up the tables."
    me "And who's going to set them up?"
    show mt grin pioneer with dspr
    mt "Sem Semych, aren't you up to the task of engaging the pioneers?"
    "The squad leader smiled encouragingly."
    me "You asked for it."
    "I slammed the table, demanding attention."
    me "Comrade pioneers, thank you for visiting our establishment, and now I need four volunteers to set up the tables before lunch."
    "The answer to me was a wary silence."
    "No surprise there."
    me "Are there no volunteers?"
    "Silence."
    me "Anyone?"
    with fade
    show mt laugh pioneer with dspr
    play music music_list["so_good_to_be_careless"] fadein 5
    "Olga couldn't stop laughing."
    "The whole time we were setting up the tables, she was laughing and laughing."
    "I really wanted to tell her to shut up, but I'm afraid she wouldn't appreciate it."
    mt "Gee, Semyon."
    "Wiping her laughing eyes with the corner of her tie, she finally let it out."
    "Only now did I notice that she was no longer wearing the ugly raincoat she'd been sporting all morning."
    "Looks like it's stopped raining."
    th "For the sake of completeness, it would be nice if someone would stop laughing."
    show mt smile pioneer with dspr
    "I threw an oblique glance at the squad leader, and she jumped again."
    mt "You're the worst teacher I've ever met."
    "She finally managed to share a stifling laugh."
    mt "Volunteers... From the pioneers..."
    me "What's wrong with that?"
    "I snapped."
    me "Should I have forced them?"
    show mt normal pioneer with dspr
    mt "No, it's okay. I thought you were going to play some game or something to motivate them, and you... Eh, Sem Semych."
    mt "Okay."
    "She looked over the work front, which was already almost completely mastered."
    "And just in time - Lena peeked cautiously into the canteen:"
    show un shy pioneer far at fleft with moveinleft
    un "E-excuse me, I..."
    mt "It's okay, Lena."
    "The squad leader waved her hand."
    mt "You can start setting up, we're almost done."
    me "I should never have signed up for this questionable event in the first place."
    "I grumbled."
    mt "Don't be sour."
    "Olga clapped me on the shoulder."
    mt "And - thank you for your help!"
    show mt smile pioneer with dspr
    hide mt with moveoutright
    "After giving me one last smile and nodding to Lena, who was studying us, the squad leader retreated."
    "And then dinner arrived."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_along:
    play music music_7dl["beth"] fadein 3
    scene bg ext_houses_rainy_day_7dl with dissolve
    play ambience ambience_7dl["rain"] fadein 3
    if loki:
        "I love the rain. {w} It always feels so good to breathe in the rain..."
        "When you can breathe a few liters of liquid grace into your chest and dissolve the bitterness for a while."
        "The same bitterness that has been a familiar companion since the moment the door slammed shut behind the one miracle whose scent stained my shirt..."
        "To cover my ears with Olafur, to let symphonic music into my troubled soul, and to set my tears to the sky."
        "To walk through damp, gray streets, bridges, embankments, through passers-by and dream of death - and dare not die."
        "I'm an atheist, which means there's nothing waiting for me on the other side."
        "And that suits me fine."
    else:
        "It's like I brought my Petersburg with me for a while."
        "There's nothing special about just water falling out of the sky - it's just a meaningless atmospheric precipitation that doesn't even put me in the mood."
        "Except that the pressure makes it sweeter to sleep."
        "But this rain was mine."
        "As familiar as the thick raincoat that every St. Petersburger has been supplied with since birth."
        "And periodically one can spread it in a foreign land and turn the surroundings into the best place on earth."
        "Let it be for a little while, for some hours."
        "But even that is enough to grit your teeth and get on with your life."
    play sound sfx_open_door_clubs_2
    $ alt_pause(1)
    scene
    $ renpy.show("bg int_house_of_mt_day", what = Rained("bg int_house_of_mt_day"))
    with fade
    "Dropping my raincoat and shoes on a coat rack by the entrance, I staggered barefoot to the bed and plopped down there."
    dreamgirl "Sleep?"
    "A voice in my head yawned infectiously."
    "The offer is certainly tempting."
    stop music fadeout 3
    "But I had less and less time left in this promised land."
    "I could sleep later. I think my life will give me more than enough of this unique opportunity."
    stop ambience fadeout 3
    play music music_7dl["promise_to_meet_you"] fadein 3
    "But now that I'm here, I need something to occupy myself with while it rains."
    "Like reading something. I had my smartphone handy."
    "A strange, unfamiliar book opened up."
    "I've never read one of those, I doubt it would have had a place on my e-book shelf - fleeing the horror of loneliness, I filled my phone memory exclusively with humorous fantasy and sci-fi."
    "Except that the old records are becoming the norm. And what used to be hilarious to the point of being funny isn't even a smirk anymore."
    "I guess before, before all those gadgets, that feeling would have been a lot sharper and more frequent-when out of a pile of lead-laden, casein-smelling daydreams comes something that cuts to the blood, and you remember it a year later to reread it."
    "And you don't find it."
    scene anim prolog_2
    with dissolve
    "Because there never was this book."
    "Just as there aren't most of the people on the other side of the LCD screen."
    "They are invented by your communication-hungry mind, given the brightest features and let live."
    "For the sake of one less woe in the stream of bile. If only temporarily."
    "At least for eight years, imagine a companion. A companion."
    "Make up a story for her, happiness, meaning, surround yourself with her image, fall in love with her."
    "Then jump into 'night fifty-six', fall asleep, hide from my own uselessness in an imaginary world."
    "Not for long. Ten, many - fifteen years."
    "And open my eyes one day to someone else's ceiling, realizing I've been lying to myself all this time."
    "That you're a goddamn cheater who got his hands on the world's console."
    "And you close your eyes as if you were in all places at once."
    "You slash your black leather jacket against the two hundred kilometers of November wind on your way to the capital."
    "You cry, hiding your tears behind your long hair and forehead against the glass, staring impatiently at the snow-white airliner that never comes in for boarding, thinking you couldn't leave - like that."
    "You see the black-painted metal door being pulled up from various corners by figures in body armor, shouting over radios, and on the captain's clipboard an unofficial order to 'take no one alive.'"
    if loki:
        "You growl with hatred, knowing full well whose child's fatherhood you are now breastfeeding and hiding your eyes from someone who mistakenly thinks otherwise."
    if herc:
        "You scream in despair, realizing that the person closest to you in the world is slowly dying alive in four walls, and you are powerless to help him."
    else:
        "You count the moments, watching the Renault skidding on the wet asphalt, and you are powerless to do anything because your damn body is incapable of functioning at the speed where you found yourself only out of desperation!"
    "How the nicotine cuts into your soul on an empty stomach at four in the morning."
    "How doomed it is to realize that you have no chance of getting out of here alive and well, since you can't live several lives at once, even if most of them are purely virtual, taking place solely in your head."
    "And you want to throw it all to hell, because you can already see the lights of Moscow through the windshield, and the plane is coming in for a landing, and the spark hisses, coming up on the bickford cord to the loops."
    play ambience ambience_int_cabin_day fadein 3
    stop music fadeout 3
    play sound sfx_knock_door7_polite
    $ alt_pause(1)
    "My self-condemnation was interrupted by a knock on the door."
    scene
    $ renpy.show("bg int_house_of_mt_day", what = Rained("bg int_house_of_mt_day"))
    with dissolve
    me "Yes?"
    "I retorted."
    play sound sfx_open_door_1
    $ alt_pause(1)
    show un shy pioneer with dspr
    un "H-Hello."
    "I waved back."
    un "I-It's..."
    "She mumbled."
    un "About the c-candle to say..."
    me "What?"
    show un sad pioneer with dspr
    un "C-candle's n-n-now."
    "Stammering, with difficulty, the girl squeezed out."
    un "In the clubhouse."
    "Ohoho, my sins are grievous."
    "I struggled to peel myself off the pillow and squinted at the girl without much sympathy."
    me "Attendance is mandatory, isn't it?"
    "It'll be easier and quicker if I help her before she burns up here from embarrassment."
    "Lena nodded convulsively."
    me "Okay. I'll be there."
    "I'll have to say goodbye to the idea of snoozing."
    "Lena nodded again convulsively and ran off."
    play sound sfx_open_door_strong
    hide un with easeoutleft
    with diam
    th "I'm not going back to sleep. No, I won't."
    dreamgirl "Or will I?"
    th "I won't."
    dreamgirl "Well, what if I do?"
    "Coaxing took a few minutes."
    "And the subconscious almost won."
    "The reluctance to set poor Lena up turned out to be the decisive weight on the scales."
    th "Strange, of course. {w}I've never cared for such things before..."
    "For sleep is sacred!"
    with fade
    "Putting on my slightly dried sandals and raincoat, I followed Lena."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_cndl:
    if alt_day5_me_neu_candle == 2:
        scene bg ext_clubs_rain_7dl with fade
        play sound sfx_open_door_clubs
        $ alt_pause(1)
        scene bg int_clubs_male_rain_7dl with dissolve
        "Olga let me go ahead of her and wizarded with the lock for a while."
        me "Is something wrong?"
        "I asked, stifling perfectly logical fantasies in such a situation."
        show mt normal pioneer with dspr
        mt "How can I tell you..."
        "She waved her hand toward the door."
        mt "It's a little jammed in there, you have to lift the door to get it to close properly, otherwise it'll slam."
        th "That's what I thought."
        dreamgirl "Hey, don't take my job!"
        me "Got it. So what do you want me to do?"
        if alt_day3_technoquest1 >= 1:
            "Nothing has changed here since my last visit."
            "It feels like no one has come in here since then."
        "Still the same table, littered with boards, wires, and radio junk, from which the cyberneticists never built their secret project."
        mt "To begin with, bring the cups. Now, how many do we need..."
        "She cocked her eyebrows thoughtfully at the bridge of her nose."
        mt "Sasha's out, so nine in all."
        me "What about him?"
        "Without much interest I asked."
        if not alt_day3_technoquest2:
            show mt surprise pioneer with dspr
            mt "Haven't you heard?"
            show mt normal pioneer with dspr
            mt "He climbed up on the roof yesterday to fix the antenna, but he couldn't hold on and fell. He rode all night with Violeta Cernovna to town and back, now he's sleeping it off."
            th "Wow! Camp Darwin Award!"
        else:
            mt "A strange thing happened. He disappeared last night and came back this morning."
            mt "He was found asleep on the porch of his cabin."
        if herc and (counter_me_neu_answers == 1):
            $ volume(0.0, "music")
            play music2 music_7dl["unholy_you"] fadein 3
            "I looked warily at the counselor."
            me "By any chance, did he go to the old camp?"
            show mt sad pioneer with dspr
            "Olga shuddered and frowned."
            mt "By chance he did."
            mt "Do you know anything about this?"
            "Her unaccustomedly serious tone sent shivers down my spine."
            th "And why the sudden interest?"
            me "Nothing much. I just heard from... locals that there's such an interesting location."
            show mt normal pioneer with dspr
            "The squad leader's serious face just disappeared."
            mt "Not that interesting."
            th "Now I definitely doubt it!"
            stop music2 fadeout 3
            $ volume(1.0, "music")
        else:
            th "People live!"
        mt "Alright, wait here for a bit."
        hide mt with easeoutleft
        "Olga, with a nod to me, went into the back room."
        "There she rattled, rattled with something."
        if persistent.mt_7dl_good:
            "And a few seconds later she came out, carrying in her hand a glass bottle of some kind of green drink."
            show mt smile pioneer with easeinleft
            mt "Get the dishes, time for a health drink."
            me "What's that?"
            "I squinted suspiciously at the liquid."
            show mt laugh pioneer with dspr
            mt "Tarhun! If you don't want it, don't drink it; more for me."
            "One didn't want to argue with that logic, and the two glasses were found in no time."
            show mt normal pioneer with dspr
            mt "Well, prozit!"
            "The squad leader acted like she had absinthe in her glass, not harmless soda."
            th "Showing off."
            "I thought serenely."
            "And slammed the glass down in a gulp."
            me "Cheers!"
            "I bowed jokingly."
            show blackout_exh with fade
            "Wanted to bow out."
            "Something fiery heated, slashing, enveloping jumped down my esophagus, grabbed my chest, my temples - my face must be very red right now."
            th "Oh, she's laughing now."
            "Had time to think."
            "But I haven't had time to look yet."
            "Gravity decided to change its vector - it hit me several times against the ceiling and then sent me into the nearest wall..."
            $ renpy.show("bg int_clubs_male_day", at_list = [sdl_transform3], what = Noir("bg int_clubs_male_day"))
            play sound2 sfx_bodyfall_1
            scene black
            with flash
            play music music_7dl["no_hope_left"] fadein 3
            $ persistent.sprite_time = "night"
            $ night_time()
            "It sounded like a pillow stuffed with absorbent cotton."
            "I felt as if I'd been hit on the head with something heavy."
            "Or drunk with a high level of sulphuric oils..."
            th "And this darkness in my eyes... I've heard that methyl alcohol can make you blind!"
            "I panicked, I tried to rub my eyes and I couldn't!"
            th "Paralyzed?"
            "The inner voice was sensibly silent."
            th "It's probably a little late for that, but I'll never drink so much again."
            "My eyes were slowly getting used to the darkness, and I could even see a thin streak of light coming from somewhere on the side."
            "And the paralysis was due to the fact that someone had tied me to something. {w}Not permanently, of course, leaving a certain amount of freedom."
            "But one that just didn't make my limbs swell - and I could feel a gag in my mouth."
            "Meanwhile, a strange, irregular noise was coming from somewhere on the side, which the buzzing head finally recognized as conversation."
            "Conversation."
            th "Well, of course... We're having a candle right now. And I'm sunbathing here."
            "I tugged as hard as I could, trying to free myself, even mumbling something."
            "In vain."
            "Whoever was tying me up knew what he was doing."
            "Another tug, another..."
            "I was like this for two minutes before I got sick."
            th "What did that bitch drug me with?"
            "I thought wistfully."
            th "And why?"
            "It was strange and creepy to see the pioneers talking serenely about something behind the wall while I lay here and couldn't move or raise my voice."
            "And all I had to do was count the passing moments."
            "I didn't notice myself falling asleep again."
            "And this time I woke up in the cold."
            with dissolve
            scene bg int_clubs_dj_nolight_7dl with fade
            "And the blissful sensation of having nothing in the way of the tongue."
            me "Olga... Dmitrievna?"
            mt "Yes?"
            "She asked from the darkness above my ear."
            me "Why is it so dark in here?"
            mt "You know... The light bulb's blown out."
            me "How did I get here..."
            mt "Don't you remember? You drank one extremely curious drink."
            "It was impossible to tell from the sound of her voice where she was."
            me "And why did you tie me up?"
            mt "Because I could. I can't?"
            scene
            $ renpy.show("bg int_clubs_dj_nolight_7dl", what = SS_com_r("bg int_clubs_dj_nolight_7dl"))
            with dissolve2
            "Her laughter made us involuntarily think that we were alone here, that civilization was miles away, and suddenly something happened..."
            "Olga leaned over me."
            show mt smile_g pioneer with dissolve
            "And now I was really getting scared."
            mt "Don't you know not to drink unfamiliar drinks in unfamiliar places?"
            "She leaned over me so that I could feel her breath and the heat coming from her skin."
            me "Now what?"
            "I asked."
            mt "Haven't you guessed yet?"
            "Her hands rested on my chest. That's why it was so cold - my shirt was unbuttoned, and there was a palpable breeze coming from somewhere on the side."
            "The manicure, meeting almost no resistance, dug into my skin, and my soft lips touched."
            "Pressed tighter - I gasped in surprise, first from the kiss and then from the pain as she bit my lower lip with all her might."
            "My mouth filled with blood almost instantly - she bit it."
            "And it wasn't so much the pain as it was the nightmare of what this woman might actually want. No matter how you spin it, I was completely at her mercy."
            "I couldn't even close my mouth of my own free will."
            "I just closed my eyes helplessly when the tip of someone else's tongue ran across the wound."
            "Another bite, to the tears."
            "More nails under the skin - on my stomach."
            "Perhaps I was secretly waiting for this - so when the skin at the base of my neck touched wet lips, I lifted my chin and turned around to make her more comfortable."
            me "Who would have thought..."
            me "My squad leader is a vampire."
            hide mt with dissolve
            "I said it because I had to say something."
            mt "That's stupid. I don't drink blood, silly. I'm interested in something else."
            me "What?"
            mt "The same thing as always."
            "Boringly she said."
            mt "Life."
            "The belt buckle snapped, surrendering under her onslaught, my shorts along with my shorts went somewhere down."
            mt "What's funny, you ask that every time you find yourself here."
            mt "Don't you feel sorry for a little time for your leader. {w}You're always fighting back like I want to cut you up."
            "She could see in the dark like a cat. Or maybe it was her glowing eyes."
            "But she found my innermost part unmistakably."
            "Reached there."
            show blink
            "And I closed my eyes."
            stop music fadeout 3
            $ persistent.sprite_time = "sunset"
            $ sunset_time()
            scene bg ext_clubs_rain_7dl
            show mt normal pioneer
            with flash
            me "Oh, you know what, I don't think I will."
            "I politely declined."
            mt "Suit yourself."
            "The squad leader shrugged."
            mt "Let's get the chairs then, the candle opens in ten minutes."
    scene bg int_clubs_male_rain_clean_table_7dl with flash
    play ambience ambience_clubs_inside_day fadein 3
    play music music_7dl["what_if"] fadein 3
    "If you consider our camp as a state, then Olga Dmitrievna might well have been a tsarevna."
    "Or the Grand Duchess."
    "Because the superiors were out there somewhere, crawling around on a thunderous front, nonthreatening, influencing as much as possible."
    "And our Duchess had a coronation gown, white, camouflage, with ruby inlays (I won't tell you how much it pissed me off when I learned that rubies and sapphires are trivial aluminum oxides)."
    "True, our princess prefers a banal panama hat instead of a monomakh hat - but that doesn't make it worse, does it?"
    "Already all the chairs had been set up, the heating element in the jar was forming bubbles, and a tin box of tea was fragrant next to it."
    if alt_day5_me_neu_candle == 2:
        th "How great that we all…"
    else:
        "Already all the pioneers had gathered - the last one was me, and almost under my arm ran Lena."
    "Of course, the entourage was also present - in the person of Generalissimo Feoktistova, the faithful chain dog of the squad leader, the gray cardinal and a KGB agent in one person."
    "Summer is a little life. And camp is a tiny state."
    "Someone's home, at the entrance of which, according to the rules of etiquette and basic politeness, along with dirty shoes and outerwear were supposed to leave the troubles and problems inherent in life on the mainland."
    "That's why it was so good to rest in such remote places, because you discretely, dramatically changed everything that was going on and forgot about what was waiting for you On The Other Side."
    "And for the second twenty-four hours I couldn't get rid of the impression that I'd done something wrong or taken a wrong turn somewhere."
    "And that's why I stopped recovering."
    "It's as if I had forgotten something, and now it's oppressing and oppressing."
    if counter_mt_7dl > 3:
        "Or is it that the leisurely cycle of thoughts-about nothing and everything all at once-turns toward our evil and harmful squad leader?"
    "I felt annoyed. In the rain, I desperately need my living space."
    "Instead, I was grabbed by the soft spot and dragged to sit where there would be a lot of noise, chatter, stale air, and prying eyes."
    th "Why am I here?"
    "I thought wistfully, looking around."
    "The pioneers looked pleased with themselves and the company of those around them. They would hardly notice if I now smoothly..."
    mt "Semyon, sit next to me!"
    "The squad leader successfully prevented me from celebrating my cowardice."
    "Bitch."
    "I squinted at Miku sitting serenely next to me - who didn't care at all about the crowd."
    th "She must have talked Lena into coming, too."
    "Thought to myself."
    "The one thing we had in common with the sad girl - a dislike of all these kinds of gatherings - I cherished enormously."
    th "Now she'd be sitting in her cabin, reading."
    if 'library' in list_voyage_7dl:
        th "Or she would be drawing."
    "What else could a girl her age be into?"
    "Alisa was hardly particularly happy, either - she and Ulyana were set back far away, and you couldn't even buy them with tea."
    scene bg int_clubs_male_rain_clean_table_7dl
    show mt smile pioneer at zentercenter
    with dissolve
    "And our omnipotent woman, smiling in the affectionate way, smiling, looked over her charges, and I felt a little uncomfortable when her green eyes met mine."
    "Even though I knew perfectly well that it wasn't the eyes she was looking at, but the bridge of her nose, a man is such a brute that a straight look is hard on him too, especially if you're a girl in your twenties, with a pedagogical degree under your belt and not yet able to {i} dislike {/i} the people around you."
    mt "So it's half past twelve and we open our candle."
    "Olga lit a short, thick candle and, after letting it accumulate a bit of transparent, tear-like, melted wax, poured some onto a saucer, set it down in front of her:"
    mt "The candle will be the same as last time. Does everyone remember the order?"
    "After waiting for scattered nods, Olga nodded to Electronik, and he lowered the curtains, plunging the room into semi-darkness."
    $ persistent.sprite_time = "night"
    $ night_time()
    scene
    $ renpy.show("bg int_clubs_male_rain_clean_table_7dl", what = Desat1("bg int_clubs_male_rain_clean_table_7dl"))
    show mt normal pioneer
    with dissolve
    th "The candle is lit by the one whom everyone believes. Or at least the one whose candidacy raises the least questions."
    th "Lena, Miku, and the redheads are out. Slavya will be rejected by Alisa. Electronik will turn him down himself. That leaves only the squad leader."
    "Carefully holding the saucer with the candle - if the one goes out, the candle will end prematurely - Olga began:"
    mt "It is said that during the Candle, a little ray from the candle reaches out to each person sitting."
    mt "Mironova Olga. Squad leader. What I remember most was the arrival of one latecomer."
    "The pioneers murmured softly, smiling, clearly understanding who they were talking about."
    mt "The best moment... I think the best moment was the last dance."
    if alt_day3_us_bugs == 1:
        "She wagged her finger at Ulyana."
        mt "In spite of someone else's attempts to spoil the mood a little."
    mt "Proud that you have learned to work as a team after all, even if not always willingly and with song."
    mt "Unhappy that none of you ever started dating anyone. Only I didn't say that. Everything that happens on a candle stays on a candle."
    "She handed the saucer to Slavya."
    hide mt
    show sl normal pioneer
    with dissolve
    sl "Slavyana Feoktistova. Assistant to the squad leader in the second shift. Most of all I remember the arrival at the camp. I knew a lot of people from the camp, some from school. It was nice to see everyone again."
    sl "The best moment I think the last candle - for a long time I wanted to talk to someone heart-to-heart, looking into the fire."
    sl "Worst moment..."
    if alt_day3_technoquest2 and (alt_day3_dj == 'dv'):
        sl "Probably the fact that the radio never worked."
    else:
        sl "I guess I could call that moment the accident with the roof the day before yesterday."
        if alt_day3_technoquest2:
            "She glanced in my direction."
    sl "Proud to be friends with all of you!"
    "Dvachevskaya muttered something, but didn't say anything out loud."
    sl "Unhappy that you never became friends with each other."
    "She held back a sigh as the petal of flame fluttered on the wick, and carefully handed the saucer to Miku."
    hide sl
    show mi normal pioneer
    with dissolve
    mi "Hatsune Miku…"
    "…"
    hide mi
    show un normal pioneer
    with dissolve
    un "Tikhonova Lena…"
    hide un
    show us normal pioneer
    with dissolve
    us "Sidorova Ulyana…"
    hide us
    show el normal pioneer
    with dissolve
    el "Syroezhkin El… Sergey."
    hide el
    show dv grin pioneer2
    with dissolve
    dv "My name is Batareikina Glunya. The thing I remember the most was when they gave us potatoes in the canteen."
    dv "That was the best moment in camp."
    dv "I lie, though. Here's the best moment."
    "She blew a short blow and blew out the candle."
    dv "That's it, I'm here, I've sat here, give me the keys."
    "She demanded of Miku."
    "The latter handed Alisa the bundle at a loss."
    hide dv with dissolve
    "And a second later, Dvachevskaya evaporated."
    stop ambience fadeout 3
    "The silence in the room thickened."
    show mt sad pioneer with dissolve
    mt "Calm down, just calm down."
    "Mumbled Olga."
    mt "Hitting children is uneducational."
    show us calml pioneer at left with dspr
    us "But she put out the candle, what do we do now?"
    stop music fadeout 3
    "Ulyana looked expectantly frustrated - if it had been even a little drier outside, she would have gone out to play ball, that's all."
    "But here and now, since an entire squad leader condescends to entertain you..."
    hide us
    show el normal pioneer at right
    with dissolve
    el "Guys, we have a video player in the back, why don't we watch something?"
    "Electronik suggested."
    mt "Like what?"
    dreamgirl "'Emmanuelle', of course! Or better yet, 'Caligula,' with the obligatory incarnation of real life reigning on the screen."
    "Laughed the inner voice."
    show el upset pioneer with dspr
    el "Uh, well..."
    "Electronik scratched the back of his head."
    el "We've got 'Guest from the Future' on four cassettes over there. Will you watch it?"
    "Olga threw a glance at her watch and, with a sigh, allowed it:"
    mt "Fine, bring it."
    hide mt
    hide el
    with dissolve
    "Asking Slavya for help with his eyes, Electronik pulled a TV set with a built-in player into the room where the squad had gathered, blushing for some reason, he looked for a long time for the right tape, but finally, on the screen the TV snow was replaced with a familiar picture from his childhood..."
    play music music_7dl["wonderful_faraway"] fadein 3
    "And Ulyana, for some reason in a whisper, said:"
    show us normal pioneer with dissolve
    us "By the way, it's Alisa's favorite movie."
    th "Probably because it's starring her namesake?"
    "Anyway, by her behavior, she deprived herself of such an opportunity. Glunya is."
    "I glanced at the door, expecting, as if expecting Alisa to knock timidly now, apologize for her behavior, and sit quietly in a corner."
    "But it was easier to believe that the camp director would show up at our candlelight with cake than it was to believe in the redhead's shameful return."
    th "Why don't we just screw them all? What am I, worse than her, after all?"
    th "The film's good, of course, but to be stuck in the same room with my favorite squad for hours on end..."
    menu:
        "Escape":
            $ alt_day5_me_neu_candle_escape = True
            return
        "Look for answers" if counter_me_neu_answers == 1:
            $ counter_me_neu_answers = 2
            $ counter_mt_7dl -= 2
            $ counter_us_7dl -= 2
            return
        "Stay":
            th "Where will I go in such a downpour, though? Sleep in the cabin?"
            th "The idea is undoubtedly not a bad one, but putting on a raincoat again and walking through puddles... It's too much gesture to satisfy my whimsical 'won't and don't'."
            "I sighed and stared at the screen again."
            scene
            $ renpy.show("cg d5_me_Alisa_7dl", what = Noir("cg d5_me_Alisa_7dl"))
            show anim_grain
            with dissolve
            "For as long as I can remember, I've always been fascinated by the way Soviet authors managed to do touching retro-futuristic storytelling."
            "There wasn't too much action, but it was so memorable, so ingrained in my blood, that for weeks 'The Beautiful Far Away' was on my tongue."
            "I am not even talking about the mass hysteria around Natasha Guseva, who played the lead role in the film - this type of appearance was very fashionable then, even hairdressers cut hair 'like Selezneva' without any explanations."
            "The tale told by Kir Bulychev and adapted by Arsenov has become a symbol of the mid-to-late eighties for me, a time that was not prosperous in every sense, but..."
            "At any rate, that time managed to produce those who sit around me now and, with their mouths half open, listen to the saga of the fairy-tale girl from the future."
            "With a wink, Olga got out from behind the table and headed outside."
            $ persistent.sprite_time = "day"
            $ day_time()
            if alt_day5_me_neu_candle == 2:
                stop music fadeout 3
                play sound sfx_open_door_clubs
                $ alt_pause(1)
                play ambience ambience_7dl["rain"] fadein 3
                scene bg ext_clubs_rain_7dl
                show mt smile pioneer at zenterright
                with dissolve
                mt "So, how was your evening?"
                "Smiled the squad leader."
                "There was still a little drizzle outside, but overall it wasn't the nightmarish downpour the new day greeted us with."
                me "Morning, you mean?"
                "I was sorely missing a cigarette or some other magical toy that allowed a smoke between me and the person I was talking to - in either sense."
                "I guess if a flame had gotten to me, it would have been easier - the flame acts as the best interlocutor - and I would have been able to say something."
                "But mean Alisa spoiled the event and evaporated."
                mt "Morning, evening... We'll have another bonfire here - and woe to whoever wants to tear it down!"
                "She threatened the invisible enemy with her fist."
                mt "Have you chosen with whom you will go?"
                me "You ask it like it's a slow dance invitation level decision."
                show mt normal pioneer with dspr
                mt "Maybe so..."
                "Thoughtfully, Olga stretched out."
                mt "Maybe so. {w}If you don't make up your mind, you come with me."
                "She thought."
                mt "Or with Zhenya."
                me "With Zhenya?!"
                "I wasn't hiding my horror."
                show mt laugh pioneer with dspr
                mt "I knew you'd like it!"
                me "I'd rather be with you then."
                "I realized what I'd said and hastily bit my tongue."
                "Fortunately, the squad leader didn't notice the subtext."
                show mt normal pioneer with dspr
                mt "Don't rush your decision, you have until dinner to change your mind, there's plenty of time."
                mt "I'm going to check on the men on duty."
                "For some reason she reported."
                mt "Make sure this place is cleaned up before dinner, will you?"
                th "And for some reason asks for me and not Slavya."
                th "Does she really believe in me?"
                dreamgirl "And now she's going to burden me beyond all measure? {w}Oh, those exciting prospects!"
                hide mt with dissolve
                "And she drifted away behind a shroud of rain."
                "Leaving me alone with my thoughts."
                play sound sfx_open_door_clubs
                $ alt_pause(1)
                scene
                $ renpy.show("bg int_clubs_male_rain_clean_table_7dl", what = Desat1("bg int_clubs_male_rain_clean_table_7dl"))
                with dissolve
                "After sighing for a while about my grievous sins and my lack of smoking, I went back to the club."
                "To watch."
            else:
                "Nodding to her, I made myself comfortable."
                "There were four DVD images of the pirated edition back home, once downloaded but never seen."
                "Couldn't watch it alone, for crying out loud."
                "Like most movies of my childhood, including b-movies of the 'Kickboxer' level."
    stop music fadeout 3
    stop ambience fadeout 3
    stop sound_loop
    return

label alt_day5_me_neu_cndl_esc:
    scene
    $ renpy.show("bg int_clubs_male_rain_clean_table_7dl", what = Desat1("bg int_clubs_male_rain_clean_table_7dl"))
    play ambience ambience_clubs_inside_day fadein 3
    show mt normal pioneer with dissolve
    "I glanced over at Olga. The squad leader sat hunched over her shoulders, staring frowningly at the screen."
    "Yeah, I don't envy her, of course. Once in a shift, she finds time for her pioneers, and they're such a nuisance to her!"
    "The thought that it was a particular pioneer who did the dirty work, I brushed it off carelessly."
    if counter_mt_7dl < 3:
        "Even though what Alisa had done was ugly, I couldn't bring myself to feel sorry for the leader - I had too many questions about her approach to her duties."
    "I grabbed my raincoat from the coat rack and quickly ran outside, silently shutting the door behind me."
    stop music fadeout 3
    $ alt_pause(1)
    $ volume(1.0, "sound_loop")
    play sound_loop ambience_7dl["rain"] fadein 3
    scene bg ext_clubs_rain_7dl
    with dissolve
    th "So point one, 'escape,' has been successfully accomplished."
    th "What's next on the plan?"
    dreamgirl "Did we have a plan?"
    th "Well, yes!"
    th "Escape from the candle and..."
    if lp_dv > 5:
        th "...and try to find the redhead!"
        "Can't say I was that eager for her company, and she hardly dreamed of spending the rest of her time with me before dinner."
        if alt_day4_me_neu_date == 'dv':
            "No kidding, after last night's scene at her cabin, this meeting was threatening to end up in a fistfight!"
        "But she was fun to be with on those rare occasions when we managed to cross paths."
        if alt_day4_me_neu_mi_songs:
            th "And anyway, we had a good time together last night and even managed not to fight. Although Miku was with us..."
        th "Fine, it is what it is. It's no big deal if she chases me away. I'm going to sleep it off."
        th "When else will such a great opportunity arise?"
        "I gathered my courage and walked confidently down the path toward the music club, carefully avoiding the puddles."
        scene bg ext_musclub_rain_7dl with touch
        "But as soon as I was on the wet veranda, my doubts crept back into my head."
        th "What if she's crying out there?"
        dreamgirl "Did someone hurt her?"
        dreamgirl "Or is Dvachevskaya your Turgenev's young lady, who gets so bad from bad weather and lack of love experiences that she urgently needs to go to the waters for treatment?"
        th "No, but..."
        if alt_day4_me_neu_date == 'dv':
            th "And anyway, what makes you think she has no love feelings?"
            dreamgirl "Oh, don't project!"
            dreamgirl "She clearly made it clear yesterday that she doesn't put you in the middle of anything. Still going to convince yourself that she just has a shitty sense of humor and violence is her love language?"
            th "..."
        play sound sfx_knock_door7_polite
        "I didn't want to argue with my inner jackass. I sighed and knocked on the door, but there was no answer."
        th "Doesn't want to see anyone?"
        dreamgirl "Stop chewing your snot!"
        dreamgirl "She can't hear you, you fool! It's raining on the roof!"
        dreamgirl "Or do you just want to stand and look at the gloomy forest in the distance and think about the subtleties of the redhead's mental organization?"
        play sound sfx_open_door_strong
        $ alt_pause(1)
        scene bg int_musclub_rain_7dl
        with dissolve
        $ volume(0.5, "sound_loop")
        play music music_7dl["tellyourworld"] fadein 3
        play ambience ambience_music_club_day fadein 3
        $ alt_pause(2)
        $ volume(0.2, "ambience")
        show dv surprise pioneer at cright with touch
        "I involuntarily rolled my eyes and sharply opened the door. I didn't even care what Dvachevskaya would say about my visit - I just didn't have the energy to be alone with my schizophrenia."
        "Alisa, sitting on the windowsill with her guitar, gave me a surprised look."
        show dv angry pioneer at cright with dissolve
        dv "What are you doing here?"
        "Her eyes flashed hostilely in the half-light."
        dv "Did the Hat send you?"
        "I could hardly suppress a chuckle."
        th "Yes, that mademoiselle will kill a messenger regardless of the content of the news..."
        me "No. I escaped from there myself."
        "I threw off my cloak and tossed it on an orphaned chair in the corner."
        me "You've ruined Olga's life, and now she's sitting there grieving. And instead of her, Syroezhkin is entertaining the crowd."
        show dv normal pioneer at cright with dissolve
        "Alisa hummed indifferently, but an almost phantom expression of smugness flashed across her face."
        dv "How's that? Telling jokes? Or shows card tricks?"
        me "Can he?"
        "To tell you the truth, I didn't know anything about Electronik. Well, apart from random and insignificant facts, like the fact that he was afraid of heights and of single females."
        dv "I have no idea. So what did they come up with there?"
        me "If you'd stayed, you'd have found out."
        stop music fadeout 2
        show dv angry pioneer at cright with dissolve
        dv "Oh screw you!"
        play music "<to 43.1>" + music_7dl["dv_guitar2"] fadein 3
        "Alisa snorted contemptuously and, defiantly turning away, began to slowly pluck the strings."
        th "Nice conversation..."
        show dv normal pioneer at cright with dissolve
        "I scrambled around the piano and sat down on a nearby window sill. Dvachevskaya was silently plucking the strings, not paying any attention to my movements."
        "I knew how to play the silent game, but I didn't really want to. After all, I could sit in silence on the candle as well, only there I was entitled to entertainment."
        me "New song?"
        dv "Huh?"
        stop music fadeout 1
        "Alisa stopped playing abruptly."
        me "What you were just strumming. I can't recognize the tune."
        me "So you're a future rock star?"
        show dv grin pioneer at cright with dissolve
        dv "What's it to you? Do you want an autograph beforehand?"
        me "That would be nice. Except I didn't grab my notebook with me..."
        "I defiantly patted my pockets."
        me "Will you sign my chest?"
        dv "Asshole."
        show dv smile pioneer at cright with dissolve
        play music "<from 44 to 102>" + music_7dl["dv_guitar2"] fadein 1
        "Alisa threw in an even tone, but she couldn't hide her smile. She started playing her tune again."
        th "It's like we switched roles: I'm teasing her, and she's pretending to be deadly bored with the whole thing."
        "I turned away from the redhead and looked around the room with wandering eyes."
        th "There's enough instruments here for a small orchestra, but there's only one room. I wonder if all the club members play together, or do they rehearse in the surrounding bushes?"
        dreamgirl "Especially the one who plays the piano."
        th "What?"
        dreamgirl "What?"
        me "Why don't you tell me why you ran away?"
        show dv sad pioneer at cright with dissolve
        dv "I'm sick of these candles. It's the same thing every time."
        me "What, did you want each one to be a theme festival?"
        stop music
        play sound sfx_7dl["strings_drops"] fadein 1
        show dv angry pioneer at cright with dissolve
        dv "Oh, as if you understand!"
        "Dvachevskaya slammed the strings, making them rattle."
        dv "I go to camp every summer. I don't even have to imagine what another Slavya and another Syroezhkin will say."
        if alt_day3_dj == 'dv':
            me "And you, then, are a destructive element?"
        else:
            me "So you're not like them?"
        me "Did something no one expected you to do. Clever!"
        show dv angry pioneer at cright with dissolve
        dv "Are you here to lecture me?"
        "Alisa couldn't stand it. I shrugged indifferently."
        me "Well, you aren't talking to me. I have to entertain myself somehow!"
        dv "What am I, a circus dog?"
        me "Do you know how to jump through a hoop?"
        show dv rage pioneer at cright with dissolve
        pause(0.5)
        show dv rage pioneer at center with move
        play sound sfx_piano_head_bump
        show dv rage pioneer:
            linear 0.5 xpos 0.5
            linear 0.025 xpos 0.505
            linear 0.05 xpos 0.495
            linear 0.05 xpos 0.505
            linear 0.05 xpos 0.495
            linear 0.025 xpos 0.5
            linear 0.5 xpos 0.5
        "Dvachevskaya jumped up from the window sill and rushed toward me, but was successfully stopped by an obstacle called the piano."
        show dv angry pioneer with dissolve
        dv "What a bastard you are!"
        if alt_day4_me_neu_date == 'dv':
            dv "Are you trying to punish me for yesterday?"
            "I waved my hands conciliatorily."
            me "Come on! You were punished for yesterday without my involvement!"
        me "Instead of shouting and waving your fists, you'd better tell me how you ended up in the music club in the first place."
        show dv normal pioneer with dissolve
        dv "I didn't."
        "Suddenly Alisa spoke quietly."
        dv "I'm not a member of the music club. And Miku gives me the keys because she just can't refuse."
        dreamgirl "Interesting... We'll keep that in mind."
        "I mentally rolled my eyes and ignored my schizophrenic retort."
        me "You're not in a club, but you're going to perform at a concert?"
        if alt_day4_me_neu_mi_songs:
            me "You're getting ready to sing at the bonfire, too... You're altruistic!"
        show dv tired pioneer with dissolve
        dv "Who cares?"
        "There was silence between us."
        th "Aliska is very quiet today."
        th "That's not good..."
        show dv think pioneer with dissolve
        dv "Miku is the first normal club leader."
        "Unexpectedly said Alisa."
        dv "When I was very young, there was a nice man here. But I hardly remember him - I wasn't interested in music at all back then."
        dv "There were a couple more, but I don't remember them either. And they didn't stay here long either, they did one shift a summer at the most."
        dv "For the longest time the music club was run by Antoha. He went for three summers for sure. I didn't get along with him right away, and I didn't want to go to his club on principle."
        show dv normal pioneer at cright with dissolve
        "Alisa sat on the windowsill again, placing her guitar beside her."
        dv "Last year he was kicked out for drinking. Or rather, for a relapse."
        "For some reason she added."
        "I got up from the uncomfortably narrow windowsill and sat down on the floor. Alisa reflexively closed her legs, though from my position it was hard to see anything that would reflect unflatteringly on her maiden honor."
        play music "<from 44 to 102>" + music_7dl["dv_guitar2"] fadein 1
        "The conversation ended again, and Alisa went back to playing the guitar I had so obsessively distracted her from."
        th "I wonder if this rain will ever stop?"
        th "That would be great if on days like this everyone was allowed to sleep as much as they could..."
        th "Missing the canteen won't be convenient, but we can think of something."
        th "Something..."
        show blink
        $ alt_pause(2)
        stop music fadeout 1
        stop sound_loop fadeout 3
        scene bg int_musclub_day
        show dv angry pioneer at cright
        show unblink
        dv "Are you going to lunch or not?"
        me "Huh?"
        "I looked at the angry Dvachevskaya in surprise."
        show dv angry pioneer at center with dissolve
        dv "Okay, if you don't want to do it, fine."
        "She took a step toward the exit, but immediately turned around."
        dv "No, get out, though. I have to close the door."
        "With difficulty I got up from the floor and stretched myself out. After sleeping in such a perverted position, my body was aching unbearably."
        "I waddled past Alisa and out the door."
        scene bg ext_musclub_verandah_day_7dl with dissolve
        th "I should think of an excuse for Olga..."
        th "However, I'm used to solving problems as they arise."
        "With that in mind, I hurried off to lunch."
        $ volume(1.0, "sound_loop")
        $ volume(1.0, "ambience")
        play ambience ambience_camp_center_day fadein 2
        scene bg ext_dining_hall_near_day with fade
        $ persistent.sprite_time = "day"
        $ day_time()
        play music music_7dl["what_am_i_doing_here"] fadein 2
        show mt angry pioneer with dissolve
        "But on the porch an angry Olga Dmitrievna was quite naturally waiting for me."
        mt "Won't you tell me where you've been for the entire quiet hour?"
        me "Asleep."
        "I answered honestly."
        me "I had a headache, so I..."
        show mt rage pioneer with dissolve
        mt "Yeah? Where did you sleep?"
        "Olga didn't seem to be satisfied with my answer."
        mt "I went looking for you in the cabin, but, as you might have guessed, I found no one there!"
        me "So I went out for a walk when the rain stopped."
        show mt angry pioneer with dissolve
        "The squad leader gave me a hard look. Obviously, she didn't know exactly what to pick on in my shaky story."
        show mt normal pioneer with dissolve
        mt "Fine, we'll talk later. March to the canteen."
        "I quickly rushed past her, hoping that Dvachevskaya, who had come up, hadn't heard our conversation."
    else:
        "This, alas, was the end of my ingenious escape plan."
        th "This is a stupid situation. I can't go back now!"
        th "Maybe I should go to the infirmary on some pretext? I'll provide an excuse for Olga, too..."
        if alt_day4_me_neu_cs_debt:
            "Though the memory of yesterday's embarrassing defeat quickly caused me to abandon this dubious venture."
        else:
            "Except that swapping the company of passive teenagers for that of a too-much-active nurse sounded like a very dubious plan."
        "With a heavy sigh, I wrapped my raincoat tightly around me and staggered toward the cabin."
        play music music_7dl["unfulfilled"] fadein 3
        scene bg ext_house_of_mt_rain_7dl with dissolve
        $ volume(0.5, "sound_loop")
        play sound sfx_open_door_1
        $ alt_pause(1)
        scene
        $ renpy.show("bg int_house_of_mt_sunset", what = Desat("bg int_house_of_mt_sunset"))
        with dissolve
        $ volume(0.2, "ambience")
        play sound sfx_close_door_1
        "The cabin greeted me with emptiness, darkness, and dampness. I grimaced as I threw off my water-soaked raincoat."
        th "The last thing I wanted to do in the morning was to get out of here. Now that I have no other choice, the last thing I want to do is stay here."
        th "That's the way a man is-always wants what he can't have. And better yet, something that's out of reach."
        if herc:
            th "Once upon a time I longed only for one thing: for one bastard to answer for mutilating my mother."
            th "Of course, I didn't want to sit with my mother at the time-not that I cared about her. I didn't want to go to classes, I had better things to do."
            th "Only in the army did I realize how much I needed to be near my mother. How much more pleasant it was to sit at lectures than to spend countless hours in combat training."
        elif loki:
            th "Once all I dreamed of was Ksana, and nothing else mattered to me."
            th "And when, after figuring things out in the entryway, she walked into my apartment, I felt truly happy for a moment: a man who didn't need anything else."
            th "Had I known then that I still had something to lose..."
        else:
            th "I don't remember at what point in my life I began to wish only that everyone would leave me alone."
            th "Didn't bother calling, didn't text, disappeared from my contact list, allowing me to finally drown in my loneliness."
            th "But when my dream came true, I was suddenly desperate for someone to burst into my life, even with the most trivial 'hello, how are you?'..."
        th "Only it's no use thinking about it all now. I've got a new life on the horizon..."
        th "I've already managed to screw it up."
        if alt_day4_me_neu_date == 'mi':
            th "Everything seemed to be working out fine with Miku, but no, I end up getting a turnaround. Because being loser is a way of life."
        elif alt_day4_me_neu_date == 'dv':
            th "Everything seemed to be working out fine with Alisa, but no, I end up getting a turnaround. Because being loser is a way of life."
        elif alt_day4_me_neu_date == 'un':
            th "Everything seemed to be working out fine with Lena, but no, I end up getting a turnaround. Because being loser is a way of life."
        elif alt_day4_me_neu_date == 'sl':
            th "Everything seemed to be working out fine with Slavya, but no, I end up getting a turnaround. Because being loser is a way of life."
        elif alt_day2_mt_help:
            th "Everything seemed to be working out fine with Olga, but no, I end up getting a turnaround. Because being loser is a way of life."
        elif lp_us >= 5:
            th "Everything seemed to be working out fine with Ulyana, but no, I end up getting a turnaround. Because being loser is a way of life."
        else:
            th "I've spent almost a week in the company of the friendliest and most open-minded people, and I still shy away from every person I meet. And one day they'll get bored with me, and then I'll be all alone again."
        play sound sfx_bed_squeak1
        "I stretched out on the bed and stared up at the beveled ceiling. Thinking was slow and lazy, as if damp air had crept through my nostrils into my skull box and made my thoughts swell with moisture like book pages."
        show blink
        "My eyes closed on their own. The sound of the rain was soothing, washing away not only the dust from the paths, but the melancholy that had overtaken me again."
        stop music fadeout 2
        stop ambience fadeout 3
        stop sound_loop fadeout 3
        $ alt_pause(2)
        play music music_list["sparkles"] fadein 3
        voice "Catch up!"
        $ set_mode_nvl()
        "I was racing down the wet path behind some girl. My body was at its limit, but there was no way I could reach the right speed."
        "She was farther away, but I could just as clearly hear her mocking voice:"
        voice "What, you're not strong enough?"
        voice "Or have you lost your way?"
        "Gritting my teeth, I continued my pointless pursuit. Somehow I knew this girl had what I needed."
        "Her ringing laugh was annoying. She knew I'd never catch up with her, but she wasn't about to slow down."
        voice "I'm not running anywhere."
        "Cheerfully she threw."
        voice "I'm here, look!"
        nvl clear
        "I stopped and looked around, but she was nowhere to be found."
        if persistent.alt_binder:
            if herc and (not alt_day3_technoquest2):
                voice "Climb higher, and then you'll see!"
                "But there wasn't any high ground around here."
                me "How can you climb up here?"
                voice "Who said it's necessary to climb here?"
            elif (loki or dr) and (alt_day1_sl_keys_took not in (1, 3)):
                me "I can't see you!"
                "The girl laughed again."
                voice "And what did you want to see when all you're looking at is the keyhole?"
                voice "You have to open the door first!"
            else:
                voice "You just ran the wrong way."
                me "Where were you supposed to go?"
                voice "As if I should tell you everything!"
        else:
            voice "You just haven't learned how to see right yet."
            me "You've got to be kidding me!"
            me "How can you see wrong?"
            voice "Well..."
            "It's like she's thinking."
            voice "When you see, but not the whole picture!"
        me "What am I supposed to do now?"
        voice "Wake up!"
        me "What?"
        nvl clear
        $ set_mode_adv()
        mt "Wake up!" with vpunch
        play music music_list["your_bright_side"] fadein 3
        play ambience ambience_int_cabin_day fadein 2
        $ volume(1.0, "ambience")
        $ volume(1.0, "sound_loop")
        scene bg int_house_of_mt_day with dissolve
        $ alt_pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        show mt angry pioneer with dissolve
        "The dream was gone: the squad leader hovered menacingly over me, and I remembered that I hadn't thought of an excuse for my infamous escape from the candlelight vigil."
        mt "Would you care to explain why you're sleeping in the cabin during a squad event?"
        me "And you?"
        show mt rage pioneer with dissolve
        "Without thinking, I blurted out. Olga, who was already not in the best of spirits, came dangerously close to berserk mode."
        mt "How are you talking to me?"
        if loki or herc:
            "I grimaced at her scream and lazily out of bed."
        else:
            "Her shout made me jump out of bed in an instant."
        th "Okay, we have to say something sensible before she gets violent."
        th "I'll have no problem beating her hand-to-hand, but what's in it for me..."
        me "I got a headache."
        "I just said the first thing that came into my head."
        me "The change in the weather, I guess. The TV only made it worse."
        show mt normal pioneer with dissolve
        "Olga's gaze softened a little."
        mt "Was it so hard to warn me?"
        "I shrugged it off."
        me "Yeah, you know, after what happened at the candle..."
        th "I didn't want to get caught in the heat of the moment!"
        me "Anyway, I didn't want to upset you."
        if counter_mt_7dl >= 3:
            show mt laugh pioneer with dissolve
            "Olga suddenly chuckled."
            mt "What a gentleman!"
            "She quickly pulled herself together, though, and hid the smile."
        else:
            show mt sad pioneer with dissolve
            "Olga looked at me incredulously."
            mt "My whole squad is one frustrating thing..."
            "Quietly she muttered. And before I could get a word in edgewise, she continued in a louder voice:"
        show mt normal pioneer with dissolve
        mt "Go to lunch already!"
        "Deciding not to tempt fate and see how long the squad leader had changed from anger to mercy, I rushed to the door."
        play sound sfx_open_door_1
        scene bg ext_house_of_mt_day with dissolve
        play ambience ambience_camp_center_day
        "Just as I jumped out on the porch, I was surprised to find that it had already stopped raining."
        th "Yay, now there's so much to do!"
        dreamgirl "Like what?"
        th "Like stuffing my stomach. And then it's up to the circumstances!"
        "I reached out and hurried towards the canteen."
    stop music fadeout 3
    stop ambience fadeout 3
    stop sound_loop
    return

label alt_day5_me_neu_day_answ_h:
    scene
    $ renpy.show("bg int_clubs_male_rain_clean_table_7dl", what = Desat1("bg int_clubs_male_rain_clean_table_7dl"))
    play ambience ambience_clubs_inside_day fadein 3
    show el normal pioneer at right with dissolve
    "I quietly walked over to Electronik sitting on the stool and gently put my hand on his shoulder."
    me "Serega, we need to talk."
    show mz bukal glasses pioneer at fleft with dissolve
    "I invited him to step away with a nod, noticing the unhappy stare of Buzzer."
    show el sad pioneer at right with dissolve
    "Electronik quietly sighed, and followed me to the backroom door."
    hide mz
    show el sad pioneer at center with dissolve
    me "You heard about Shurik?"
    show el normal pioneer at center with dissolve
    "It was hard to imagine circumstances in which he wouldn't have been aware, but I decided to start my entreaties with a strong argument. Syroezhkin nodded, and his eyes lit up with interest."
    me "So, I suggest we go to that bunker now. Something ain't right here."
    show el surprise pioneer at center with dissolve
    el "Now?"
    "He cautiously glanced first at the TV, then at Olga Dmitrievna."
    show el sad pioneer at center with dissolve
    el "Can't this wait until evening?"
    me "What evening? After dinner there's quiet hour, and then they'll think of something else to do. And right now nobody's going to search for us for sure."
    el "But what about the squad leader…"
    me "Say that you're going to infirmary, and I'm going to be escorting you there. And we'll think of something later!"
    dreamgirl "I'm afraid to even imagine what you'll think of…"
    me "Oh, and also: can you grab a couple flashlights?"
    stop music fadeout 3
    $ alt_pause(1)
    play sound_loop ambience_7dl["rain"] fadein 3
    play music music_7dl["unsettling"] fadein 3
    scene bg ext_clubs_rain_7dl
    with dissolve
    stop ambience fadeout 3
    $ alt_pause(2)
    scene bg ext_houses_rainy_day_7dl with fade
    show el upset pioneer with dissolve
    "Ten minutes later we were already waddling through the puddles towards the gate."
    el "I don't like this idea…"
    "Electronik was muttering."
    el "I'm sure you're just winding yourself up. Surely he got lost in the forest, so he came only in the morning."
    me "And he just lay down on the porch? He's got some interesting habits then."
    el "Come on, he probably just was tired!"
    scene bg ext_path_rain_7dl
    show el sad pioneer
    with diam
    "I didn't answer and silently continued, tightly clutching our only flashlight: Syroezhkin couldn't get any more."
    th "I'd be as skeptical if I was on his place though. After all, he's not the one who ended up in the past, losing a dozen years in process!"
    scene bg ext_path2_rain_7dl
    show el sad pioneer
    with dissolve
    me "Why was this camp closed in the first place?"
    el "A very unpleasant story happened there. Someone from the teaching staff hanged himself."
    th "Yeah, so we'll have to deal with the ghost of a counselor. And I was hoping to get off easy!"
    el "Rumors are different every year: now about a nurse, now about a counselor. But there was definitely a death, so it's not just a scary story for the younger squad."
    el "And the next year the new «Sovyonok» has already opened. And how did they get it built so quickly?"
    th "Wow! So I'm not the only one who has a sense of the strangeness of everything going on!"
    el "Part of the pedagogical staff moved to the new camp, the director, for example. Boris Alexandrovich was there for sure, he once compared us to the pioneers of those days at the exercise..."
    show el serious pioneer with dissolve
    "Electronik frowned, obviously doing some calculations in his mind. He was obviously comparing dates."
    me "Shouldn't the director have been asked to step down for that incident?"
    el "Well, he was. Alexei Maksimovich was his deputy at the time."
    th "Wow!"
    th "It turns out that the camp has not only a director, but a whole deputy as well!"
    th "How come nobody saw them?"
    dreamgirl "Syroezhkin has seen them, he even knows them by name and patronymic. Or do you need more witnesses?"
    th "Syroezhkin knows a lot of things..."
    th "About line-up rotations, for example. How would an ordinary pioneer know that?"
    stop music fadeout 3
    th "However, if his parents or older siblings went to that camp, it's not surprising."
    play music music_7dl["nowyouseeme"] fadein 3
    scene bg ext_old_building_day_rainy_7dl
    show rain_overlay
    with dissolve
    "We reached the old camp quickly - we were driven to it by a rather unpleasant rain, though it was warm in summer."
    "In the daylight the barrack didn't seem so ominous anymore, and the only unpleasant feeling was the black hole instead of the door."
    th "Was it even there yesterday?"
    th "How did Shurik and I get separated then, if it wasn't?"
    dreamgirl "It was dark, idiot! That whole barrack looked like one big black hole then."
    show el normal pioneer with dissolve
    "Electronik stopped cautiously a few meters from the makeshift entrance."
    el "Are you sure we should go in there?"
    "His apprehension was beginning to annoy me."
    me "Let's go already! At least there won't be any rain and wind!"
    "I clapped Electronik on the shoulder and stepped resolutely toward the enclosure."
    $ volume(0.5, "sound_loop")
    scene int_old_building_night with dissolve
    play sound sfx_open_door_squeak_2
    "The enclosure was untouched, apart from a broken door. The thickness of the layer of dust on the floor confirmed that we were one of the first visitors."
    "The layer of dust on the windows made it so dark inside that I turned on the flashlight immediately. It wasn't hard to trace Shurik's movements of yesterday by the patterns of the paths on the dusty floor."
    "At one point the chain of footprints went forward and broke off."
    show el normal pioneer with dissolve
    me "I think it's this way."
    "I nodded to Electronik standing behind me and followed Shurik's footsteps."
    show el sad pioneer with dissolve
    el "Creepy place."
    "He said, cowering and looking around."
    el "Is that a hatch?"
    scene cg d4_hatch_night_7dl with dissolve
    "He pointed suddenly to the floor. It was hard not to notice the trapdoor - Shurik had obviously opened it yesterday."
    th "Breaks down doors, lifts trapdoors... Does he go to the local gym in addition to his club?"
    me "I'd better look for something to hook it up with."
    "I looked around, and my eye caught a decrepit chair with metal legs."
    th "Well, I don't think anyone wants it, so let's not call it vandalism..."
    play sound sfx_7dl["crash_wood"]
    "The seat and the back crackled, and I proudly shook the loot in front of the frightened Syroezhkin."
    me "Stand back, just in case - who knows where it'll bounce off..."
    play sound sfx_fall_metal_door
    $ alt_pause(1)
    scene cg d4_hatch_night_open_7dl with dissolve
    "Electronik obediently ran to the exit. I pushed the homemade lever, and the hatch swung open easily, creaking angrily and raising a column of dust. The government raincoat became pathetic to look at."
    "A rusty metal staircase led to what looked like a shallow basement. I tried to look at the corners of the basement, but from my position there was little to see."
    me "I've got the flashlight, so you go in first."
    th "Let's check to see if the steps are rotten!"
    "Electronik looked at me pitifully, but he went into the hatch. Clutching the lantern tighter, I cautiously climbed in after him."
    stop sound_loop fadeout 2
    scene int_catacombs_entrance with dissolve
    show el sad pioneer with dissolve
    "But before us was not a cellar, but a tunnel going into the unknown: the lantern's power was not enough to see where it ended."
    me "Looks like the rumors about the bunker were definitely not unfounded."
    th "And if that tunnel doesn't lead to it, I don't know what to think about the whole damn thing anymore!"
    "Electronik sighed again pitifully, but I ignored it."
    "We moved down the tunnel, and my body signaled that we were going down a slide. The tunnel went deep underground."
    me "How did you even know about the bunker?"
    show el normal pioneer with dissolve
    el "Well…"
    "He stammered."
    el "Ulyanka told everyone on the first day."
    me "And you believed her? Ulyanka?"
    el "Well, you know, she and her friends looked all over the place, so you can trust them!"
    "However, there wasn't much confidence in his voice."
    th "It's interesting: Syroezhkin knows the circumstances of the closure of the old camp, and Ulyana knows that there was a bunker under it..."
    th "They keep a good eye on their pioneers here!"
    "But it was to my advantage, so I did not complain aloud."
    scene int_catacombs_door
    show el smile pioneer
    with dissolve
    el "Look!"
    "Joyfully exclaimed Electronik, pointing to a door that I could see perfectly well without him."
    hide el with dissolve
    play sound sfx_metal_door_large_close_basement
    "I shoved the flashlight to him and tried to open the door. It was hard, but it gave way the first time."
    stop music fadeout 3
    th "Thanks to the four-eyed, he cleared the way for us!"
    scene int_catacombs_living
    show el normal pioneer
    with dissolve
    play music music_7dl["ambience_safe"] fadein 3
    "Behind the door was a bunker - a real bunker. A few minimalist iron beds, a wall of electronic devices, and a row of lockers."
    th "Strange bomb shelter. If it was built for the needs of the old camp, it's obviously not big enough: even if you consider that children need far less space than adults, it can't even hold a dozen!"
    th "Something's not right here..."
    dreamgirl "But look at all this scrap metal!"
    dreamgirl "We're rich! Fabulously rich!"
    me "Listen, Sergei..."
    "I followed my partner's gaze and noticed a second door open wide in the very corner."
    me "Do you think Shurik opened it too?"
    show el think2 pioneer with dissolve
    el "I don't know..."
    "Sluggishly Electronik replied. It was as if he hadn't heard my question at all."
    th "Shouldn't he be squealing with delight and running around the bunker right now, happily pocketing everything that isn't screwed and welded on?"
    me "Sergei, is everything all right?"
    el "Yes."
    th "Although, why am I... The guy's overexcited."
    th "It's not every day we get into bunkers."
    me "Anyway, you don't want to go in there. Let's go look for the wire."
    hide el with dissolve
    "After turning off the flashlight, I began to study the local monuments of radioelectronics. All the devices looked like something from an institute laboratory - as Soviet and heavy in appearance."
    th "Yes, to find a micro-USB here is something of a fantasy. It's probably extremely anti-scientific."
    th "However, no one knows what's in these lockers..."
    "I was about to search the lockers, when something very out of place caught my eye. In the corner next to the lockers was a dark gray safe."
    "I leaned closer and tentatively tugged on the handle. The safe did not open as expected."
    "As far as my experience with code locks showed, they were easier to break. Regular use of the buttons, especially the metal ones, tended to make them glossy, making them stand out from the rest."
    "The next step was simple combinatorics. At the worst, it took two minutes to find the code, given an unlimited number of attempts."
    "With this safe, however, it was more complicated. Apparently it had been in use for a long time, and the code had been changed regularly - all of its buttons were equally worn."
    th "This way I'll be here till the end of my shift trying to open it..."
    me "Sergei, do you happen to know how to pick locks?"
    stop music fadeout 3
    "The answer to me was silence."
    me "Serega?"
    play music music_7dl["sammy"] fadein 3
    "I turned around frightened."
    $ persistent.sprite_time = "night"
    scene bg int_catacombs_entrance
    show d4_cat_door_frame
    with dissolve
    "Electronik was nowhere to be found. But the second door, which was open, told me eloquently where he might have gone."
    th "Damn it!"
    "A sense of responsibility for his evil head came out of nowhere and made me jump up and rush out of the bunker with a flashlight at my side."
    hide d4_cat_door_frame
    with fade
    "The second door led to a shaft. After a quick look around, I dared to guess that it was as abandoned as the bunker itself."
    "A noise was heard to my left, and I rushed in without a second thought, lighting my way with a flashlight."
    show el normal pioneer with dissolve
    "As expected, Syroezhkin didn't get very far."
    me "Serega, what the hell are you doing here?"
    "But he didn't respond to my shout, and neither did the lantern light. He continued to walk quickly into the depths of the mine."
    "I rushed forward, circled him, and stopped in front of him, blocking the way."
    me "Are you deaf?!"
    show el surprise pioneer with dissolve
    "I barked. Electronik blinked rapidly."
    el "What happened?"
    me "I should be asking you that!"
    "Electronik's uncomprehending look made my back break into a cold sweat."
    th "I mean, he started acting weird back in the bunker..."
    "But there was no time to think about it."
    me "Let's get out of here!"
    show el scared pioneer with dissolve
    "Grabbing the frightened Syroezhkin by the arm, I rushed to the entrance to the bunker, stumbling over rocks and cursing to myself, first the rocks, then my wayward companion, then myself."
    stop music fadeout 3
    scene int_catacombs_living
    show el surprise pioneer
    with fade
    play sound sfx_fall_metal_door
    "It wasn't until I slammed the door to the bunker that I exhaled."
    play music music_7dl["unsettling"] fadein 3
    me "And what was that?"
    el "I don't know."
    me "He doesn't know!"
    play sound sfx_metal_door_large_close_basement
    with vpunch
    show el scared pioneer at right with dissolve
    "I slammed my fist angrily against the unfortunate door. Syroezhkin frightenedly bounced to the beds and slowly settled down on the corner of the nearest one."
    me "Did you realize how dangerous it was to climb into the mines without a flashlight?"
    me "Hell, screw the flashlight! It's basically dangerous!"
    show el upset pioneer with dissolve
    "Electronik was ready to cry."
    me "A soil collapse and good riddance. And we'll be lucky if it collapses from below instead of above!"
    "I took a breath, leaning my forehead against the cold door. The fear was slowly letting go."
    th "I should have gone alone. The locals are giving me nothing but trouble!"
    show el sad pioneer with dissolve
    el "I really don't know why I went there."
    "Quietly said Syroezhkin."
    el "I looked behind that door, and... it was like something pulled me, you know?"
    me "What do you mean «pulled»?"
    el "I don't know. It just felt like I had to go that way."
    "He waved his hand, pointing in that direction."
    me "You're not sleepwalking?"
    show el surprise pioneer with dissolve
    el "I don't think so."
    th "No, you can't blame it on sleepwalking if you want to. I was only distracted for five minutes; he couldn't have fallen asleep in such a short time."
    th "Which means there's some hell going on, and Shurik's in the infirmary for a reason."
    "As much as I'd like to deal with the safe, I couldn't leave Electronik here. There's no telling where he might be dragged again!"
    me "We've got to get out. I hope this door opens from the inside..."
    stop music fadeout 3
    $ alt_pause(2.1)
    scene bg ext_houses_rainy_day_7dl
    show el sad pioneer
    with fade3
    play ambience ambience_7dl["rain"] fadein 3
    $ volume(0.5, 'ambience')
    play music music_7dl["let_me_down"] fadein 3
    "Slowly the fading rain washed away the traces of our adventure. Electronik was walking quietly, pensive, and I could understand him."
    th "Still, there is something here that defies any rational explanation. And the more I think about it, the more I'm convinced of it."
    th "Maybe it wasn't a bomb shelter at all."
    th "But what? And more importantly, why was it built?"
    dreamgirl "You left out the most important thing."
    dreamgirl "So, a riddle: how was the bunker different from anything you've seen in the dungeons?"
    th "Lots of things. But most importantly, there was a light on."
    "And that could only mean one thing."
    th "It's still being used. But if you couldn't get there through the old camp before our series of marauding raids, then there must be another way."
    "My thoughts went back to the safe."
    th "If the bunker is still in use, then the hypothetical contents of the safe take on even more significance."
    th "There's just one problem: the safe is locked!"
    "However, I did have an idea..."
    show el think pioneer with dissolve
    el "And what shall we say to Olga Dmitrievna?"
    "…but first it was necessary to deal with the immediate problems."
    me "Here's an idea, the idea is this: you go to sleep in your cabin, I'll go to Shurik's bunk. We'll tell Olga that you had an urgent need to lie down, and you fell asleep. I was waiting for the rain to subside, and I accidentally fell asleep myself."
    me "What do you think?"
    show el serious pioneer with dissolve
    el "I think it sounds like a complete screw-up."
    "Honestly answered Syroezhkin."
    stop music fadeout 3
    me "That's wonderful."
    th "The purest truth tends to sound like a total bullshit, so we can't help but be believed."
    stop ambience fadeout 2
    $ persistent.sprite_time = "day"
    $ day_time()
    show bg int_house_of_el_day_7dl
    show mt angry pioneer at left
    show el sad pioneer at right
    with joff_r
    play music music_list["your_bright_side"] fadein 3
    "Not fifteen minutes later, Olga flew into the cabin."
    $ volume(1.0, 'ambience')
    show mt rage pioneer with dissolve
    mt "Went to the infirmary, huh!"
    show mt angry pioneer with dissolve
    me "Olga Dmitrievna, we were really going that way!"
    "I tried to squeeze out as sleepy a voice as possible."
    me "But Sergei got dizzy, and we stopped here for a while."
    show el normal pioneer with dissolve
    el "And fell asleep!"
    "Excessively chipper for having just woken up, added Electronik."
    dreamgirl "Good thing your genius plan didn't involve sleeping in the same bed!"
    "Olga gave both of us a stern look."
    mt "Okay, we'll talk later. Go to lunch now!"
    "I didn't need to be persuaded. After our foray I was ready to eat a bull."
    th "Riddles are riddles, but lunch is on the schedule!"
    return

label alt_day5_me_neu_day_answ_l:
    scene
    $ renpy.show("bg int_clubs_male_rain_clean_table_7dl", what = Desat1("bg int_clubs_male_rain_clean_table_7dl"))
    play ambience ambience_clubs_inside_day fadein 3
    "I furtively looked around."
    show mt normal pioneer with dissolve
    "Olga was sitting in a daze, trying to comprehend what happened."
    show mz bukal glasses pioneer at right with dissolve
    "Buzzer blankly stared at the screen. Everyone else just watched the movie."
    hide mz
    hide mt
    with dissolve
    th "Since the main task of our librarian is to chase people away from books with all her might, it is best to go and read them in her absence!"
    play sound sfx_keys_rattle
    "I fumbled in my pocket for a bunch of keys, which I had thoughtfully brought with me this morning." 
    th "So I have about three hours. All that's left is to sneak out of here."
    stop music fadeout 3
    stop ambience fadeout 3
    $ alt_pause(1)
    play sound_loop ambience_7dl["rain"] fadein 3
    scene bg ext_clubs_rain_7dl
    with fade
    "It wasn't a hard thing to do. You'd look like a martyr, grab your stomach, ask the counselor tearfully, and then they wouldn't expect you back anytime soon."
    play sound sfx_close_door_1
    "I slammed the door of the clubs and walked through the puddles toward the library."
    show bg int_library_rain_7dl with joff_r
    $ volume(1.0, 'ambience')
    $ volume(0.3, 'sound_loop')
    play ambience ambience_library_day fadein 2
    "Finding the right key in the pouring rain was a challenge, but I managed to get into the library. I threw off my raincoat and rushed to find the book I'd left behind yesterday."
    th "So, the shelf by the window... third from the left, I think." 
    th "Aha!" 
    "I grabbed my textbook off the shelf and found my bookmark from yesterday. As I sat down on the window sill, I searched for the fragment where I'd been interrupted by the Buzzer."
    play music music_7dl["comfortable_mistery_4"] fadein 3
    $ set_mode_nvl()
    "{i}The damage done to our country by the aggressors was enormous. During the war the Soviet Union lost a third of its national wealth.{/i}"
    "{i}Many of the country's largest enterprises were destroyed. The Soviet state began to restore them during the war, as territories occupied by the enemy were liberated.{/i}"
    "{i}But recovery only became main priority after the victory.{/i}"
    "{i}Even during the war, a Soviet-Japanese group of scientists conducted experiments on accelerated damage repair, but full-scale research began only after victory. The experiment ended in 1947 due to the erasure of its leader, Gendo Ikari.{/i}"
    "{i}The country was faced with the choice of the path of economic development. In February-March 1946 Stalin returned to the slogan he had advanced shortly before the war: the completion of the construction of socialism and the beginning of the transition to communism.{/i}"
    "{i}In his opinion, the war only delayed the fulfillment of this task.{/i}"
    $ set_mode_adv()
    "I read the paragraph to the end, but once again found myself stumped. It was all perfectly ordinary text from an ordinary history textbook, but this experiment…"
    th "I don't remember anything like that in the history of the USSR. And I have never heard such a word as “erased” used in the address of a man!"
    "After flipping through the next few paragraphs, I closed the textbook with a sigh. Nothing more was said about the experiment involving the Japanese scientist." 
    th "We should dig into some science-pop literature!" 
    th "If there is such a thing, of course, Soviet science-pop..." 
    "I tossed the book on the windowsill and started pacing the shelves, trying to understand what I should be looking for and where it might be." 
    "My eyes fell on a box that was on one of the shelves. It was a stack of magazines." 
    th "Aha!"
    th "There must be some 'Science and Technology' in there, and I'm sure it says what the hell it is!"
    "I unloaded all the stuff I found in the drawer onto the table next to the window. I pulled up a chair, pulled back the curtain that was stealing the scarce light, and began to read."
    "All the notes were of no interest. No erasure was mentioned in them."
    "After an hour of searching, I didn't even read the notes anymore - I swallowed the headlines cursorily and leafed on without interest. I had little hope that I would find anything worth reading in the folders."
    "{i}Tamagotchi: a Japanese toy with Soviet technology{/i}"
    play sound sfx_7dl["page_turning"]
    "I turned the page and froze, blinking confusedly."
    th "What?.."
    play sound sfx_7dl["page_turning"]
    "Cautiously turning back the page, I realized I was not mistaken."
    th "And what does it say? That all this time the Tamagotchi was just a copycat of the legendary egg-catching wolf from Electronics?"
    $ set_mode_nvl()
    "In 1980, scientists from the USSR reconstructed the circuit of an electronic device obtained by contact with a PCR. The device did not interest Soviet scientists: it turned out to be a simple children's toy."
    "It was decided to pass this circuit to our comrades in Japan. As you know, Japanese industry is famous for being highly technological, and the Japanese are famous for their love of technological knick-knacks, so the comrades appreciated our gift."
    "And so, seven years later, a Japanese factory began producing them - Tamagotchi. It's a small plastic toy, shaped like an egg. Inside it lives a virtual pet that the player has to take care of."
    "Next year, the USSR plans to buy the technology for Tamagotchi toys from Japan in order to improve it later."
    $ set_mode_adv()
    "I did some simple calculations in my mind."
    th "If tamagotchis were on the market when I was eight... Were they really that outdated?"
    th "And why had I never heard that they were developed in the USSR?"
    "A quick reread of the note caught my eyes for an unknown acronym."
    th "PCR?"
    th "Sounds like something bad and particularly dangerous."
    "As I sat down on my desk, I stared into the darkness of the library, feverishly trying to figure out what wasn't adding up to my picture of the world."
    th "All those tamagotchis from my childhood must have been Chinese. Japanese toys would hardly have cost a penny."
    th "But why would China mass-produce toys that were produced ten years ago?"
    th "Came back into fashion and demand increased?"
    "All this required a good deal of thought. I decided to take the unfortunate note with me so I could study it later."
    stop music fadeout 1
    stop sound_loop fadeout 5
    play sound sfx_open_door_kick
    with vpunch
    "But as soon as I ripped the page open, the door to the library rattled open."
    show mz angry pioneer glasses at right with dspr
    play music music_list["revenga"] fadein 3
    mz "You! What are you doing here? Did someone say you could...?"
    "Buzzer's gaze stopped on the filing in my hands. I was still sitting there with the page half torn off in my hand."
    th "Detonation in three… two…"
    show mz angry pioneer glasses at right with dissolve
    mz "Get your hands off it! Looter!"
    "The librarian threatened to go ultrasonic, so I hurriedly threw the filing on the table, raised my hands and slowly got up from the table."
    mz "May I never see your foot in here again!"
    th "Damn, what a shit time you came in!"
    show mz angry pioneer glasses at center with dissolve
    "I gritted my teeth and walked past the Buzzer. She glared angrily in my direction, but I only grimaced back."
    hide mz with dissolve
    th "As if I need you!"
    stop music fadeout 3
    th "And without your help I can come here anytime."
    play music music_list["your_bright_side"] fadein 3
    play sound sfx_close_door_1
    scene bg ext_library_day with dissolve
    play ambience ambience_camp_center_day fadein 1
    "The sun was already shining outside as if nothing had happened, blinding the pioneers coming out of various corners with its glare."
    th "And that complicates things..."
    "However, it was too early to despair. There was just one thought floating around in my head that didn't seem to want to take shape."
    play sound sfx_7dl["eat_horn"] fadein 3
    "At the sound of the horn, I staggered towards the canteen on autopilot, throwing all the resources of my brain into making sure I didn't miss the thought."
    scene bg ext_dining_hall_near_day with dissolve
    $ persistent.sprite_time = "day"
    $ day_time()
    "So the confrontation with the counselor on the porch was a surprise to me."
    show mt angry pioneer with dissolve
    mt "And where were you?"
    me "In the restroom."
    show mt normal pioneer with dissolve
    "Olga looked at me with suspicion."
    mt "All this time?"
    me "Well, if you're interested in the details..."
    show mt sad pioneer with dissolve
    "The counselor raised her hands conciliatorily."
    mt "You should go to Viola's. Maybe you shouldn't have lunch at all."
    me "And let's find that out experimentally!"
    show mt normal pioneer at cright with dissolve
    pause(0.2)
    hide mt with dissolve
    "Rolling her eyes, Olga stepped aside, letting me into the canteen."
    return

label alt_day5_me_neu_day_answ_d:
    scene
    $ renpy.show("bg int_clubs_male_rain_clean_table_7dl", what = Desat1("bg int_clubs_male_rain_clean_table_7dl"))
    play ambience ambience_clubs_inside_day fadein 3
    show un normal pioneer with dissolve
    "I found Lena with my eyes. She was sitting with her legs tucked under her chair and her fingers interlocked, staring blankly at what was happening on the screen."
    "Our walk yesterday, and Lena's strange behavior in the boat, came to mind again. Now that the memories of last night were washed away by the unaccustomed rain of the place, I was beginning to doubt the reality of what had happened."
    scene bg ext_island_night:
        align (0, 0.6)
        zoom 2.0
    show blackout_exh2
    show un smile2 pioneer
    show prologue_dream
    with dissolve
    th "Lena, who laughs and pokes fun at me, as if she's known me all my life..."
    th "It's like I've known her before myself!"
    scene
    $ renpy.show("bg int_clubs_male_rain_clean_table_7dl", what = Desat1("bg int_clubs_male_rain_clean_table_7dl"))
    show un normal pioneer
    with dissolve
    "I really wanted to talk to someone about this, so that my thoughts would stop whirling around my head, preventing me from picking out anything concrete."
    hide un with dissolve
    "Lena wasn't an option. I couldn't find the strength to approach her again, and she didn't seem the least bit interested in conversation."
    "Olga would hardly respond to my inquiries about her squadmate. {w}Slavya didn't seem like a gossipy girl. {w}Miku hardly talked to the squad any more than I did. {w}Talking to Ulyana was expensive."
    "I didn't even consider the cybernetic brothers and the Buzzer as potential informants."
    "That left Alisa, and she was extremely fortunately in her seclusion in the music club."
    th "Well, if she doesn't throw a guitar at me for an extremely untimely visit, then there's a chance of finding out something about Lena."
    "The squad leader turned her head slightly as I began to pull on my raincoat, but almost instantly turned her back to the screen."
    th "And rightly so. I don't know what kind of things I have to do..."
    stop music fadeout 3
    $ alt_pause(1)
    play ambience ambience_7dl["rain"] fadein 3
    scene bg ext_clubs_rain_7dl
    with dissolve
    "I slipped out of the clubs and staggered through the puddles toward the music club."
    scene bg ext_musclub_rain_7dl with touch
    pause(0.9)
    play sound sfx_knock_door2
    "The weather didn't allow me to peek through the windows to see if Alisa was there, so I had to bang on the door loudly, hoping for an answer."
    dv "Who's there?"
    play sound sfx_open_door_1
    pause(0.5)
    "Alisa barked angrily before swinging the door open. She glared at me frowningly, as if I were an enemy of the people."
    dv "Did the Hat send you?"
    me "No one sent me!"
    me "I'm on business."
    "Dvachevskaya looked at me incredulously, but she let me in."
    play sound sfx_close_door_1
    stop sound_loop fadeout 3
    $ volume(0.2, 'ambience')
    $ alt_pause(1)
    scene bg int_musclub_rain_7dl
    show dv normal pioneer at cright
    with dissolve
    play music music_7dl["breath_me"] fadein 3
    dv "And what's the big deal?"
    "She leaned against the windowsill, arms crossed over her chest. I threw off my raincoat on an idle chair and leaned against the piano."
    me "You're Lena's friend, aren't you?"
    th "If you can call it friendship, of course..."
    show dv dontlike pioneer at cright with dissolve
    dv "What's that got to do with you?"
    "That's the reaction I expected. Alisa didn't seem like the kind of person who would gossip about her friend with some scoundrel, either."
    "But she, unlike all the other candidates, had a chance to talk."
    me "You see, I have this strange feeling that I've met her before. That's what I want to understand..."
    show dv grin pioneer at cright with dissolve
    "Alisa chuckled before I could finish. There was a triumphant expression on her face, like she was about to throw a pissed-off 'I told you so!'"
    dv "And you're early this year!"
    me "Excuse me?"
    "Alisa's phrase sounded strange, and I didn't understand what exactly in it I wanted to pick on."
    show dv smile pioneer at cright with dissolve
    dv "Come on, remember, you fool!"
    dv "A bench near the gate. Winter."
    show dv dontlike pioneer at cright with dissolve
    "I stared at her incomprehensibly. Alisa frowned and gave my face an examining look."
    dv "Nothing comes to mind?"
    "I shook my head."
    th "What does she want from me?"
    show dv tired pioneer at cright with dissolve
    dv "You say you only knew Lena before?"
    me "Maybe I did. I'm not sure about that myself."
    show dv sad pioneer at center with dissolve
    dv "That sucks."
    "She sat cross-legged on the floor, propped her head on her fist, and stared at herself with a frown."
    dv "Thing is, I don't know a damn thing about what you two had!"
    me "We didn't have anything!" with vpunch
    "I shouted and fell silent."
    "The phrase came out of my mouth automatically, and the sound of it was definitely familiar to me."
    th "Not that I often denied having a relationship with anyone, though. Probably because I rarely interacted with more than one person over a long period of time."
    show dv smile pioneer with dissolve
    dv "Oh, come on!"
    "Alisa smiled broadly, throwing me an almost predatory look."
    th "I seem to remember an important rule: the phrase that nothing happened removes all suspicions - after it the interlocutor is absolutely sure that something happened..."
    dv "Come on, did you dance at the disco?"
    stop music fadeout 2
    show dv soft_smile pioneer with dissolve
    dv "And you didn't write a single letter to her afterwards, scoundrel?"
    play music music_7dl["areyouabully"] fadein 3
    show dv shocked pioneer with dissolve
    "Suddenly she became silent and pale."
    dv "Wait a minute!"
    show dv angry pioneer with dissolve
    "Alisa jumped up from the floor and stood across from me, clenching her fists angrily."
    dv "It's not because of you she..."
    "The girl inhaled noisily, as if resisting the urge to immediately punch me in the face. I instinctively retreated along the piano cover."
    me "This is the first time I've even been to this camp!"
    me "If I've ever seen Lena, it certainly wasn't at camp."
    show dv normal pioneer at cright with move
    "Narrowing her eyes, Alisa took a step back. She seemed to have changed her mind about getting into a fight."
    th "I wonder what they had going on here?"
    th "And why does Alisa think it's my fault?"
    dv "I don't think so."
    dv "I never saw you in Kalinin, except for the first few days after the shift. You didn't come to the Union for secret meetings with her, did you?"
    th "Kalinin? Tver' or something?"
    th "I didn't think anyone would give me the current location!"
    "However, the questions only increased."
    me "To the Union? Where do you think I was supposed to come to the Union from?"
    "Dvachevskaya flinched and took another step away from me."
    dv "Are you completely coo-coo?"
    show dv dontlike pioneer at cright with dissolve
    "She shook her head, and there was a grimace of either squeamishness or pity on her face."
    dv "Forgetting things like these already..."
    stop music fadeout 3
    "Now it seemed to me that it wasn't Alisa who was talking gibberish, but that I was very much mistaken."
    play music music_7dl["raindrops"] fadein 3
    dv "Okay, I'll give you one last chance."
    show dv shy pioneer at right with move
    "Alisa stepped away from the window for some reason, and her face disappeared into the gloom of the room."
    dv "This year's winter shift. Farewell disco."
    "Even in the semi-darkness you could see how red her face had turned."
    dv "White dance. “At Dawn”, Alliance."
    "No matter how hard I tried to concentrate, Alisa's words did not want to make any sense to me."
    show dv tired pioneer at right with dissolve
    "Alisa looked up at me timidly, and when she saw that I hadn't changed my face, she straightened up and snickered contemptuously."
    show dv normal pioneer at center with dissolve
    "And I thought a look of relief flashed across her face."
    "She was definitely confusing me with someone else, but confusing me with such confidence that I myself began to doubt that I hadn't been here in the winter."
    th "But I really wasn't!"
    show dv sad pioneer at center with dissolve
    "With a heavy sigh, Alisa turned away from the window."
    dv "I don't think you've ever met Lena. You mistook her for someone very similar."
    "She spoke quietly and unaccustomedly serious. I felt for the first time that the constant threat of a slap in the face that I usually felt around Alisa was gone."
    th "And what was I hoping for?"
    "There were questions on my tongue about Lena's looseness yesterday during our water trip, but for some reason I didn't want to ask Alisa."
    "It was as if I was afraid that with each retelling, this memory would thin until it finally blended into my memory with the unsightly background of my life's routine."
    "And I wanted to keep it."
    "Because it seemed important. It hit me like a pebble in my shoe."
    show dv normal pioneer at center with dissolve
    dv "If you don't mind, I'll keep rehearsing."
    show dv normal pioneer far with dissolve
    "Alisa said it in such a tone that I didn't dare object. She started strumming, and I wandered lazily around the small perimeter of the music club."
    th "And yet, it's strange."
    th "It's like I remember Lena, it's like Alisa remembers me..."
    th "It's like we all have different input data and can't put them together."
    "I stopped at the window, sat on the narrow window sill, and pressed my forehead against the cold glass."
    stop music fadeout 3
    "The view out the window was blurred by the texture of the rain streaming down the surface of the glass. As I stared into the blurry blackness of the forest, my eyes closed before I knew it."
    show blink
    $ alt_pause(1.2)
    scene bg ext_city_night_7dl with fade3
    $ alt_pause(1.2)
    play music music_7dl["clonidine"] fadein 3
    play sound sfx_7dl["grom"] fadein 1
    show rain_overlay with flash
    $ alt_pause(1.2)
    $ volume(0.8, "music")
    $ volume(1.2, 'ambience')
    $ set_mode_nvl()
    "The rain never thought it would stop."
    "It's practically an integral part of this city. Even my native St. Petersburg seems like a beach resort compared to London."
    "The water ran down the flashing red headlights that stained it red."
    "A river of blood."
    "That blood pulsed, flowing onto the pavement, dissolving into its blackness."
    "Dissolved to merge with the bright yellow light from the headlights of a car pulling up with a sign «{font=scenario_alt/pics/fonts/FlupperDejaVuSans.ttf}ecnalubmA{/font}» on the windshield."
    "The rain never thought it would stop. And something inside me snapped."
    "It was like I was finished."
    "I'm gone."
    "I no longer exist!"
    "Everything on which my identity had been built was gone from my memory forever."
    "Memories flowed in a pulsing stream of blood through the flashing headlights. I knelt in a deep puddle and watched the water drain away..."
    stop ambience fadeout 3
    stop music fadeout 8
    $ set_mode_adv()
    $ volume(1.0, 'ambience')
    $ volume(1.0, "music")
    scene bg int_musclub_day with fade
    play ambience ambience_music_club_day fadein 3
    $ persistent.sprite_time = "day"
    $ day_time()
    "…on the glass of the music club window."
    "I straightened up, rubbing my stiff neck."
    show dv smile pioneer close with dissolve
    dv "Woke up?"
    me "What happened?"
    "Everything around me was kind of weird and wrong."
    show dv normal pioneer close with dissolve
    dv "It's stopped raining, dumbass!"
    th "That's right! It's sunny again!"
    "All that reminded me of the rain were the drops dripping slowly down the glass, falling from the leaves of a tall tree."
    show dv grin pioneer close with dissolve
    dv "And if we hurry, we'll have time to see the rainbow, so move it!"
    "My lips involuntarily stretched into a smile."
    show dv surprise pioneer close with dissolve
    dv "What's with you?"
    "Distrustfully asked Alisa."
    me "Never thought you'd be interested in such… sentimental things."
    show dv dontlike pioneer with dissolve
    "Dvachevskaya rolled her eyes."
    dv "I've seen that rainbow in my grave! The horn was already on for lunch!"
    "Now that was a more serious argument."
    play sound sfx_close_door_1
    scene bg ext_musclub_verandah_day_7dl with fade
    play ambience ambience_camp_center_day fadein 2
    show mt angry pioneer with dissolve
    play music music_list["your_bright_side"] fadein 3
    "But instead of a rainbow on the porch of the music club, Olga Dmitrievna was waiting for us in person."
    mt "And what did you two do here?"
    th "Well, personally, nothing!"
    th "After all, I left the candle without a performance!"
    show dv angry pioneer at fright with dissolve
    dv "Rehearsed."
    "Through gritted teeth, Alisa hissed."
    dv "The concert is tomorrow."
    show mt rage pioneer with dissolve
    mt "If you keep talking to me like that, you won't be on it tomorrow!"
    show dv sad pioneer at fright with dissolve
    dv "As if I care!"
    "Quietly whispered Alisa. But her head bowed guiltily."
    show mt angry pioneer with dissolve
    mt "And you, Semyon?"
    th "What's your excuse?"
    me "I just wanted to see how Alisa was doing..."
    th "Shit, that doesn't sound as good as I want it to sound!"
    th "All that's left to do to complete the picture is to blush from head to toe. And sweat at the same time."
    mt "Did you forget that we had a squad event?"
    me "Sorry. It won't happen again."
    show mt normal pioneer with dissolve
    "Olga threw an angry look at us."
    mt "March to the canteen!"
    th "I see, all the nicest conversations are after the meal."
    hide mt
    hide dv
    with dissolve
    "I rounded the counselor and raced toward the canteen. I wanted to forget my distressing dream and fill my head with something else."
    "Like food."
    th "Still, I eat in this head more often than I think."
    th "Though it's possible that's what kept me from going crazy."
    dreamgirl "Buddy, I don't want to upset you..."
    th "Shh!"
    scene bg ext_dining_hall_near_day with dissolve
    "I ran to the canteen and stood in a noisy line. I managed to put the bad thoughts aside for later."
    th "Set aside for later..."
    th "For which time?"
    return

label alt_day5_me_neu_dinner:
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 3
    play music music_list["everyday_theme"] fadein 5
    if counter_us_7dl_px == 2:
        "After I had driven the trio to lunch and reported to the Lenivovna on my epic quest, I looked around my land."
        "And noticed there was a shortage of people!"
        "I mean, the usual faces were there, but there was someone missing!"
        "In particular, the redhead duo was not here."
        "Catching a questioning look, I turned around."
        "Danechka pointed to the seat that Ulyana usually occupied and raised an eyebrow questioningly."
        "I shrugged indefinitely and turned back to the squad leader."
        me "Excuse me, Olga Dmitrievna."
        show mt normal pioneer with dspr
        mt "Don't look for Liska and Ulyana."
        "She warned off questioning."
        me "And why?"
        show mt angry pioneer with dspr
        mt "Ask them when you meet them!"
        me "But Oolga Dmitriieevna! What happened?"
        show mt normal pioneer with dspr
        mt "That's all right. They screwed the entire event up."
        "The squad leader shrugged, and it suddenly dawned on me how tired she was in the middle of nowhere."
        mt "Saying nasty things to me and the others, ruining my mood."
        mt "I don't understand... Is it simply impossible for some people to live in peace?"
        me "And you left them without lunch?"
        mt "No. But demanded that they apologize to the collective if they wanted to be in it."
        mt "Their answer you see for yourself."
        menu:
            "But that can't be that way!":
                $ alt_day5_me_neu_us_stores = True
                "It somehow didn't occur to me that, despite my feisty behavior, I could be punished for it like this."
                "Just because there was too much of that in my past."
                "It was too familiar and natural to sound 'no lunch today' instead of reprimand and pedagogy."
                "A kind of half-forgotten creepiness reeked from the voice of memory that sounded in my mind."
                "Squinted eyes, head bowed sideways."
                "And indifference, oceans of indifference, splashing on the other side of the glass pupils."
                th "Has this world been visited by filth, too?"
                "I asked the emptiness with uncharacteristic pathos."
                th "Has the export of spite already begun?"
                show mt sad pioneer with dspr
                mt "You think I don't understand?"
                mt "But how do you influence them? Do you know?"
                mt "Can't use the belt after all."
                mt "It makes me sick to my stomach that they're walking around hungry somewhere."
                me "So just feed them?"
                mt "You can't. Either their pride or their hunger. Wait here."
                "And went away."
                hide mt with dissolve
                "The door to the food pantry slammed shut."
                "I nodded at one more look from Danechka, smiled at Miku, who had broken away from her plate."
                "Anyway, did my best not to feel awkward, standing alone looming over the chewing pioneers."
                "Still attracted attention, though."
                show mt normal pioneer with dissolve
                "In the fancy bag with the owl print she handed me, you could make out the outline of some buns and cookies if you wanted to."
                mt "Humanitarian aid to the starving."
                show mt smile pioneer with dspr
                "Olga smiled for a second."
                show mt grin pioneer with dspr
                mt "Don't tell anyone I helped you, okay?"
                mt "I'm already having authority issues with these thugs."
                "Nodding, I picked up the bag and headed for my seat - it wasn't a good idea for me to be without lunch, either."
                show mt normal pioneer with dspr
                mt "Freeze."
                me "Anything else?"
                "Olga Dmitrievna thought for a moment, then continued:"
                mt "Take the provisions to us, and send your girlfriends there as well."
                me "Why?"
                show mt smile pioneer with dspr
                mt "You'll have tea, have a chat. I don't want any dry-humping in my territory."
                mt "Is that clear?"
                me "That's right."
                mt "Dismissed."
                hide mt with dissolve
                "The soup was already cold, but hunger is known to be the best condiment."
                "I spooned up and for a few minutes I ceased to exist for this universe."
            "What if they apologize?":
                mt "You can try to persuade them."
                mt "Maybe you can do what I couldn't?"
                "She said it with such skepticism in her voice that it was clear it was fiction."
                "Unscientific."
                "With a guilty look at the distracted Danya, I went back to the table."
    else:
        if alt_day5_me_neu_candle == 3:
            "After hesitating a bit, I headed for the table that our child and youth pop star had occupied."
        else:
            "Alisa was not in the canteen. She seems to have rightly feared the leader's wrath."
            "Or maybe she was too busy... {w}what could she be doing there?"
            "She wasn't just demanding keys from Miku, was she?"
            "So, after hesitating a bit, I headed over to the table that our child and youth star was occupying."
        "Although, of course, she's going to talk like a slingshot again..."
        me "Hi, may I?"
        show mi normal pioneer with dissolve
        mi "Oh, Senechka, hello!"
        show mi smile pioneer with dspr
        "Her face spread into a smile that could only be described as carnivorous."
        th "Another one willing to ride on someone else's neck?"
        "And I can't say no to anyone - the motto of our coats of arms, the burden of our humps."
        dreamgirl "Maybe she's just happy for anyone who doesn't run away from her in terror."
        show mi smile pioneer with dspr
        "After getting to know our Miku machine-gun-girl better, I was inclined to consider this version of events as well."
        mi "Senechka, hey Senechka."
        "The Japanese girl tilted her head sideways in an amiable way."
        "And made puppy dog eyes."
        show mi sad pioneer with dspr
        if alt_day4_me_neu_mi_songs:
            th "Let me guess..."
            "And I wasn't wrong."
            mi "You're free now, aren't you? You mean I can borrow you for a couple of hours now?"
            th "What am I to you, a ruble, visionary girl?"
            "Not out loud, of course, not out loud."
            "But I moved cautiously away - what if she has a Japanese-made myelophone?"
            "I don't want to get into an argument with someone if I can't compare the cultural differences - I've been there, I've been burned, I know."
            me "You're calling me to your chants?"
            show mi smile pioneer with dspr
            mi "Please, please, please, please! You remembered so many interesting songs yesterday, I want to play some of them tonight for sure!"
        else:
            mi "Sen, hey Sen, can I ask you something?"
            me "It depends on the request."
            "Cautiously I replied."
            mi "Could you help me with something?"
            me "With what?"
            if alt_day4_me_neu_date == 'mi':
                mi "Well, you left yesterday when I didn't finish cleaning up, and there's heavy stuff like a xylophone..."
                mi "Will you help me?"
            else:
                mi "You see, tomorrow we have a concert... And some of the instruments that need to be carried to the stage are too heavy! I can't lift them, and I don't want to force the performers to do it, or they might strain themselves!"
        if len(list_clubs_7dl) != 0:
            menu:
                "Help Miku":
                    "After sighing a little for the sake of compassion, I agreed."
                    "No matter how much I lied to myself, the fact remained that I liked this immediate miracle, and the time I spent with her was not the saddest thing in the world."
                    me "Where are we going, to the club?"
                    "Miku shook her head hastily, hastily swallowing an undercooked cutlet:"
                    show mi smile pioneer with dspr
                    mi "No, no! Wait for me by the canteen, please, I have to run to the stage first."
                    "Nodding, I got up and went to wait for the Japanese girl on the porch."
                    $ alt_day5_me_neu_mi_help = True
                "You know…":
                    me "Yeah, you know..."
                    me "Actually, I've got some things to do in my club. Sorry, I can't do it."
                    th "Well, I can, but I don't really want to."
                    th "Let her look for another fool."
                    if 'music' in list_clubs_7dl:
                        show mi grin pioneer with dissolve
                        "Miku suddenly smiled slyly."
                        mi "Senechka, have you forgotten what club you're in?"
                        th "Oops."
                        th "This is awkward."
                        me "Excuse me, sensei!"
                        "I bowed low, almost dipping my hair into a glass of kompot."
                        me "Ready for any errands you may run."
                        $ alt_day5_me_neu_mi_help = True
                    else:
                        show mi sad pioneer with dissolve
                        "Miku sighed sadly, and for a second I was ashamed of my lies."
                        th "Well, it's too late to back out now."
                        th "I just have to figure out what kind of business I'm in right now..."
                        $ alt_day5_me_neu_mi_help = False
        else:
            "After sighing a little for the sake of compassion, I agreed."
            "No matter how much I lied to myself, the fact remained that I liked this immediate miracle, and the time I spent with her was not the saddest thing in the world."
            me "Where are we going, to the club?"
            "Miku shook her head hastily, hastily swallowing an undercooked cutlet:"
            show mi smile pioneer with dspr
            mi "No, no! Wait for me by the canteen, please, I have to run to the stage first."
            "Nodding, I got up and went to wait for the Japanese girl on the porch."
            $ alt_day5_me_neu_mi_help = True
    stop music fadeout 3
    stop ambience fadeout 3
    play sound sfx_open_door_1
    $ alt_pause(1)
    return

label alt_day5_me_neu_cyber_sh:
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_clubs_day with dissolve
    "Sleeping in the cabin would have been more pleasant than languishing in the company of cyberneticists, but as luck would have it, I didn't want to sleep. That's why I was standing on the doorstep of the clubhouse."
    if alt_day4_me_neu_us_debt:
        th "I hope Ulyana wasn't following me this time..."
    "Sighing heavily in advance about the next two hours of my life that threatened to go to waste, I opened the door."
    play music music_list["i_want_to_play"] fadein 3
    stop ambience fadeout 2
    play sound sfx_open_door_clubs
    play ambience ambience_clubs_inside_day fadein 3
    $ alt_pause(1)
    scene bg int_clubs_male_day with dissolve
    show el surprise pioneer at left
    show sh surprise pioneer at right
    with dissolve
    "The cyberneticists turned their heads to me in sync, and I realized that seeing Shurik in the workplace was a pretty unfamiliar sight."
    if not alt_day3_technoquest2:
        th "Damn, they healed him quickly - he's as good as new!"
    elif herc and counter_me_neu_answers > 0:
        "Of course, I wanted to immediately throw myself at him with questions, but the tense atmosphere in the room made me slow down."
    else:
        th "What a lucky man, sleeping till lunchtime!"
    me "What's the news, people?"
    "Both cyberneticists went pale as soon as I opened my mouth."
    dreamgirl "{i}Oh my{/i}!"
    dreamgirl "I think we're redundant here..."
    "I looked from one to the other, but they never saw fit to say anything."
    "Electronik was diligently hiding something behind his back. Shurik looked at me puzzled, as if he were trying to figure out whether to get rid of such a witness."
    if herc:
        me "What have you done here?"
    if loki:
        me "What, did anyone die here?"
    else:
        me "What, did anything happen?"
    show el shy pioneer with dissolve
    el "Well, we've got..."
    "He hesitated and looked hopefully at Shurik. He adjusted his glasses and coughed expressively."
    show sh serious pioneer with dissolve
    sh "We've got a difficult situation here."
    dreamgirl "Alright, pregnancy is off the table…"
    "I shuddered and tried to push my schizophrenia away from this already awkward scene."
    show el normal pioneer with dissolve
    el "Well, someone dropped off one thing at our club. And we don't know what to do with it."
    th "I wonder what it is that scares them so much?"
    th "Judging by their acrophobia, it must be at least a trampoline!"
    "I shrugged."
    me "So leave it in a prominent place - if anyone needs it, they'll take it away."
    show el sad pioneer with dissolve
    "Electronik shook his head sadly."
    el "That's the problem: you can't leave it out in plain sight!"
    "He looked out the window, as if he feared we might be overheard."
    if herc and counter_me_neu_answers > 0:
        th "Paranoia seems to be his hobby."
    show el shy2 pioneer with dissolve
    el "See for yourself!"
    "I was expecting anything from a bottle of vodka to a pack of 'rubber product №2', but Electronik held out to me..."
    me "Mother of God!"
    if not (counter_un_7dl == 6 and (persistent.un_7dl_good_ussr or persistent.un_7dl_good_rf)):
        th "I haven't seen one of these in ages!"
    th "What a rarity... I wonder if the models are domestic?"
    th "And why only someone decided to get rid of them?"
    el "Stop staring! You only have one thing on your mind."
    th "Us?!"
    "I looked at Shurik with respect."
    th "And here I was thinking that Syroezhkin wasn't the most hopeless of their botanical tandem. Well, the silent maelstrom has once again revealed to our gaze the choicest devils!"
    show el scared pioneer with dissolve
    "Electronik snatched the deck of cards out of my hands and cowered wary at the door."
    dreamgirl "This guy is clearly on our karma level. He's waiting for a setup from everywhere!"
    th "I think he's just paranoid. Making such a fuss over some deck of cards with mild erotica!"
    dreamgirl "You had that erotica on every other pole, and the kid's got milkmaids in kerchiefs and other party comrades not of the first freshness. Understand the man!"
    dreamgirl "And he'll probably get a lot more than just a finger in the air for that..."
    me "Now, tell me more. How did they get to you in the first place?"
    show el think pioneer
    show sh normal pioneer
    with dissolve
    "Shurik scratched the back of his head thoughtfully."
    sh "Started to clean up, and the deck fell out from behind one of the boxes. One of the younger ones must have planted it."
    el "Or DvaChe!"
    me "Where would she get one of those?"
    dreamgirl "Really, she doesn't look at all like someone who has cards with erotica in them!"
    show el scared pioneer with dissolve
    el "How should I know?"
    show el scared pioneer at fleft with move
    pause(0.5)
    show el scared pioneer at left with move
    "It seems that Syroezhkin was really nervous. He put the deck in his pocket and started pacing along the window."
    th "Maybe he just wants to steal the deck, but he's embarrassed in front of us."
    dreamgirl "Or maybe it was his stash, and he's ashamed to tell Shurik?"
    "I looked closely at Electronik. His panic really seemed excessive for such a trifling situation."
    "I couldn't suppress a chuckle. Electronik turned around and looked at me suspiciously."
    show el serious pioneer with dissolve
    el "Is it…"
    el "Yours?"
    "Whispering, he clarified."
    th "Either he's a good actor, or he's really too nervous..."
    "The first was hard to believe, so I could only believe the second."
    me "No, not mine."
    "I glanced around at the second suspect. Shurik was standing, leaning against the workbench, staring intently to the side, rubbing his chin."
    th "He did not react vigorously, not particularly worried. According to a witness - he was looking at the cards with interest."
    th "Creating the illusion of seeing them for the first time?"
    th "We need to ask some leading questions..."
    me "Do you have any idea when they appeared there?"
    sh "They definitely weren't there the day before yesterday - that's when I put the box there. So it was either yesterday or today."
    th "Opa, he's got the details worked out already!"
    th "All that's left is to get his fingerprints..."
    dreamgirl "And the whole camp's fingerprints, too, for the purity of the experiment. That's enough of that, Sherlock!"
    dreamgirl "You'd better help people."
    me "Maybe we should just throw them away."
    "Electronik stopped and turned to me, lips pressed together. There was a clear inner struggle in his eyes."
    show el think pioneer with dissolve
    el "It might be better, but..."
    sh "It's a pity!"
    "Helped him comrade. Both immediately stared at the floor, as if embarrassed to admit even to themselves that the cards had at least... aesthetic value."
    th "They do have a heart, though!"
    th "I thought they were some kind of retarded people. Or just autistic."
    me "Okay, then there's another option."
    me "You could bury them."
    show el think2 pioneer with dissolve
    "Syroezhkin looked up at me incomprehensibly."
    el "Why?"
    show sh serious pioneer with dissolve
    sh "And most importantly, where and how?"
    "Joined Shurik."
    me "I don't know where!"
    me "By a fence somewhere, in the bushes."
    th "You don't use them for their intended purpose anyway, you morons!"
    me "All you need is an airtight jar, preferably an iron one. And a shovel."
    me "If anyone asks, we bury the time capsule. That's it, it's guaranteed not to be touched."
    show sh normal_smile pioneer with dissolve
    "The cyberneticists were silent, pondering my idiotic plan. Shurik finished processing the data first and nodded approvingly."
    sh "We'll find a jar. But the shovel..."
    show el smile pioneer with dissolve
    el "We've got plenty of that, too!"
    "Suddenly, Electronik smiled cheerfully."
    el "You were given a key to the warehouse! Haven't you turned it in yet?"
    show sh serious pioneer with dissolve
    "Shurik frowned puzzledly, but his face quickly cleared. He got up and poked around behind one of the cabinets, and I spotted a big nail with the key to the storage room dangling orphaned on it."
    th "This place isn't exactly a safe hiding place. Is it a bad aura or something?"
    "Electronik, meanwhile, pulled out a dilapidated iron tea can from the depths. A deck of cards fit perfectly in it."
    "The cyberneticist shoved the jar under the table somewhere."
    el "Great, now for the shovel!"
    me "Serega, what are you doing?"
    "I defiantly tapped my knuckles on my forehead."
    me "Are you suggesting we run across the camp with a shovel?"
    show sh normal_smile pioneer with dissolve
    sh "Semyon is right. Let's bury the jar next to the warehouse then!"
    stop music fadeout 2
    th "It's not for nothing that everyone says that bespectacled people are smarter!"
    scene bg ext_warehouse_day_7dl with joff_r
    play ambience ambience_camp_center_day fadein 2
    play music music_7dl["runaway"] fadein 3
    play sound sfx_hiding_in_bush
    "Moving through the bushes by running and shushing each other loudly, we finally made it to the warehouse."
    el "But let's make it quick."
    el "I still wanted to figure out that schematic before we left..."
    play sound sfx_open_dooor_campus_2
    scene bg int_warehouse_day_7dl with dissolve
    "Shurik had just finished fiddling with the lock, and we broke into the storage room. I grabbed the first shovel I could find from the pile of equipment along the wall."
    me "All right, colleagues. Half the job is done!"
    stop music fadeout 3
    scene bg ext_warehouse_day_7dl with dissolve
    pause(0.4)
    show mt surprise pioneer with vpunch
    pause(0.4)
    show el surprise pioneer at fleft
    show sh surprise pioneer at fright
    with dissolve
    "I joyfully jumped out into the street and froze, almost knocking Olga Dmitrievna down."
    show mt normal pioneer with dissolve
    mt "And what are you doing here?"
    play music music_7dl["genki"] fadein 3
    me "We… Uhh…"
    "Saying that we were taking something of the club's utensils to the warehouse was interfered with by the shovel in my hand."
    "And my brain, as luck would have it, threw up images from action movies, where the main character in a similar situation hit the hapless witness over the head with a shovel and ran off."
    th "All that remains is to tell the truth."
    me "We're going to bury the time capsule!"
    mt "Really?"
    show mt smile pioneer with dissolve
    "Olga looked at us with surprise, but her lips quivered in a slight smile."
    mt "Why just the three of us? You should have called the whole squad!"
    "Behind my back, Electronik swallowed noisily."
    me "You know, I didn't have time to get everyone together..."
    th "Shit! Our genius plan is starting to fall apart!"
    me "So we wrote a letter, as if from the whole camp."
    if ('library' in list_voyage_7dl):
        me "There's a reason why guys work in the editorial office of the wall newspaper, isn't there?"
    show mt surprise pioneer with dissolve
    "Olga looked at me and my fellow campers with confused eyes."
    mt "Well, since it's from the whole camp, I need to read the letter before you bury it."
    show el scared pioneer with dissolve
    el "We wouldn't write anything bad!"
    "With ill-concealed despair exclaimed Electronik. I nodded vigorously, nervously clutching the handle of my shovel."
    me "You don't think we're trying to set you up, do you?"
    show mt angry pioneer with dissolve
    "Now the leader looked wary."
    mt "You don't want to, of course. But there are certain nuances you're unlikely to know about, so the time capsule from the whole camp has to pass an edit from the management."
    th "It smells like kerosene."
    th "And since that's the case, let's move on to the emergency plan..."
    me "RUN!" with vpunch
    scene bg ext_square_day at running
    with dissolve
    "I threw the shovel on the ground and ran as fast as I could toward the square. A few seconds later, Electronik and Shurik came running after me."
    mt "What kind of tricks are these?"
    "Olga shouted after us, but I didn't think to stop."
    scene bg ext_boathouse_day at running
    with dissolve
    "I turned sharply to the left at the square and almost bumped into a lamppost. Syroezhkin kept up, but Shurik went straight ahead, toward the clubs."
    th "What a fool!"
    th "That's the first place they'll look for him!"
    if herc:
        "But turning around and running after him was pointless. He wasn't pulling the weight of a track and field athlete to make it through the second sprint anyway."
    if loki:
        "It didn't concern me, though."
        th "I am not me, and the jar is not mine!"
    else:
        th "But how can I help him?"
        th "That's right, I can't."
    scene
    $ renpy.show("bg ext_boathouse_alt_day_7dl", what = Noon("bg ext_boathouse_alt_day_7dl"))
    with dissolve
    show el scared pioneer with dissolve
    stop music fadeout 3
    "At the pier, I stalled. Syroezhkin stopped beside me, one hand brushing damp hair off his forehead, the other clutching the ill-fated can."
    play music music_7dl["everyday"] fadein 3
    el "I think we're in trouble."
    me "Mm-hmm. And if we don't get rid of the can, we're in deep trouble."
    "I slumped down on the slightly damp planks after the morning rain and leaned into the water."
    show el think pioneer with dissolve
    el "Do you think we can hide it here?"
    "As you might expect, it was impossible to hide the cards under debarcader without at least a piece of rope or wire."
    me "I don't think so. And we don't have much time to invent a hiding place."
    me "You never know who else is going to show up here!"
    th "For example, an angry Olga."
    th "What if she's an expert runner?"
    show el sad pioneer with dissolve
    "Electronik looked sadly at the jar and closed it tightly with a stealthy movement. Apparently, he knew without words what our only option was."
    el "Well, at least we got a look..."
    "He muttered, then shoved our shameful cargo to me."
    el "I'm not good with long-range throws."
    th "Or, to put it in Russian, 'hand doesn't go up'."
    "I rose to my feet and took aim, clutching the can."
    th "Throwing The One Ring into the volcano wasn't hard, they said..."
    me "Fire!"
    play sound sfx_7dl["splash"] fadein 1
    with hpunch
    pause(0.4)

    "The can flew five meters before gurgling sadly in the water. Electronik sighed quietly."
    "And I suddenly found myself laughing. And not even because of the sad Syroezhkin, but because of the whole situation."
    th "I didn't think I'd be doing this at my old age..."
    el "Will you help with the cleaning? We don't have much left, we'll be done by noon!"
    "Electronik quickly recovered from the loss of such a valuable relic, and I even envied his ability to switch."
    me "I'll help, of course!"
    th "We've got to somehow secure ourselves an indulgence in case the squad leader gets angry!"
    scene bg int_clubs_male_day with joff_l
    play ambience ambience_clubs_inside_day fadein 3
    show mt angry pioneer
    show el normal pioneer at fleft
    show sh normal pioneer at fright
    with dissolve

    "While cleaning up, a brilliant excuse for the leader was born in my head all by itself, so we were ready when, near the end of the quiet hour, she deigned to come to our clubs."
    mt "Okay, so you have two minutes to explain what the hell was that!"
    me "We wanted to make fun of the junior squad."
    "I started, and I glanced over at Electronik. He picked up on that:"
    show el smile pioneer with dissolve
    el "We wrote a note on behalf of the hanged squad leader, and we were going to give them a map that they could use to find her stash."
    "Judging by the look, non-verbally questioning «are you idiots?», Olga believed us."
    show mt rage pioneer with dissolve
    mt "It's very pioneer-like to make fun of the younger ones!"
    mt "Okay, I could understand Semyon, but you!"
    th "Hey!"
    dreamgirl "Hey!"

    mt "Sasha, you're the oldest in the squad!"
    show sh upset pioneer with dissolve
    mt "And you, Sergei! I thought you were done with this kind of pampering!"
    show el sad pioneer with dissolve
    th "Whoa!"
    th "So wasn't Electronik always such a goody two shoes?"
    show mt angry pioneer with dissolve
    "The squad leader pursed her lips, obviously pondering whether we should be punished. But, fortunately for us, a horn was heard in the distance."
    show mt normal pioneer with dissolve
    mt "Okay, we'll talk later. Go to eat!"
    if herc and counter_me_neu_answers == 2:
        th "What a long talk we'll have by the end of the day!"
    "The boys and I hurried out of the clubs under Olga's gaze."
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_clubs_day with dissolve
    th "And the clubs are really fun!"
    $ alt_day5_me_neu_clubs_cyber = True
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_nwsppr_sh:
    $ alt_day5_me_neu_nwsppr = True
    play music music_list["two_glasses_of_melancholy"] fadein 1
    play ambience ambience_camp_center_day fadein 1
    scene bg ext_library_day with dissolve
    th "I wonder what the editorial staff of the wall newspaper does, anyway?"
    th "No, I understand that they draw wall newspapers, but in honor of what? There's absolutely nothing going on in this camp!"
    th "No Neptune Day or Robber Cossacks. We have three and a half clubs that our squad runs themselves!"
    th "They write every day about how we got potatoes in the canteen?"
    voice "Get out of my way!"
    "Some boy about twelve years old shoved me and dashed past me without even apologizing."
    voice "Andrei! Come back here! Have you forgotten where you're supposed to be?"
    "The boy was followed by his squad leader. I backed off the path and kindly let her pass, not wanting to be knocked down."
    me "Funky orders around here."
    stop ambience fadeout 1
    $ alt_pause(1)
    play sound sfx_close_door_campus_1
    scene bg int_library_day with dissolve
    play ambience ambience_library_day fadein 2
    "I muttered and went into the library."
    "Of course, I could have easily spent those two hours in the cabin, but Olga was there, and she always had some work for me to do. So it didn't seem like a bad idea to sit through a quiet hour at the club."
    th "At best I'll sit and read a book in the corner, at worst... {w}sit and read a book in the corner."
    stop music fadeout 3
    if loki and counter_me_neu_answers > 0:
        th "For example, I'll do a better study of the material I recently found. Better yet, I'll look for a medical reference book!"
    else:
        th "It's not the worst thing to do. Just wish there was something else to read..."
    "Buzzkill was absent from her workplace, either asleep in her cabin, or she went completely insane from her recluse and running off to live in the woods."
    play music music_7dl["yume_akari"] fadein 4
    "But from behind the uncovered door of the newsroom someone was singing softly."
    th "Gee! Your Miku is being broadcast here and there!"
    dreamgirl "What makes you think it's Miku?"
    th "Then who is it?"
    "There weren't many options, though. I coughed and knocked expressively on the door."
    scene bg int_editorial_day_7dl with dissolve
    show un smile pioneer with dspr
    pause(0.5)
    play sound sfx_knock_door2
    pause(0.5)
    show un surprise pioneer with dissolve
    pause(0.5)
    show un shy pioneer with dissolve
    un "Semyon!"
    "Lena immediately fell silent and turned to me, trying desperately not to look in my direction."
    me "And here I am..."
    "I didn't notice myself starting to hide my gaze. For some reason I felt uncomfortable around Lena."
    if alt_day4_me_neu_date == 'un':
        th "On the one hand, we're not strangers anymore..."
        th "But on the other hand, that's the reason we least want to look at each other!"
    elif alt_day4_me_neu_transit == 'un_7dl':
        th "And I was beginning to think we were getting along!"
    elif alt_day3_un_fz_neu_transit:
        th "I don't think we ever spoke from that idiotic scene at the dance..."
    else:
        th "Lena is even more unsociable than me, and it blows my mind every time!"

    me "Need any help?"
    un "Huh?"
    me "Help. I'm signed up for the wall newspaper, remember?"
    show un shocked pioneer with dissolve
    un "Yes, I'm... I'm almost done!"
    "Desperately exclaimed Lena and waved her arms, showing me with all her looks how much she didn't need my help."
    if dr and counter_me_neu_answers > 0:
        "It was so unlike Lena on the boat yesterday that I was once again taken aback."
        th "I never understood what it was, but..."
        th "But that makes what's happening now even weirder!"
    play sound sfx_close_door_clubs_nextroom
    scene bg int_library_day with dissolve

    "I had no choice but to politely bow out and shut the door."
    if dr and counter_me_neu_answers > 0:
        "Of course, it's a shame that I can't talk to her. But on the other hand, what am I going to ask her?"
        th "“Hi, Lena. You know, you've been giving me some strange feelings lately.”"
        th "“Do you happen to know what this might be about? Stop doing that, if possible, please.”"
        th "“Thank you in advance!”"
        "The whole thing sounded frankly unhealthy. I shook my head and moved toward the bookshelves."
    elif loki and counter_me_neu_answers == 2:
        th "Maybe I can dig up something else!"
        th "Just don't let the buzzkill come back - she's not likely to be encouraged by my presence here!"
        "I went to the shelf, where the box of trimmings stood."
    elif loki and counter_me_neu_answers == 1:
        th "Since I'm not welcome in the club, at least I'll finish that book!"
    else:
        th "Okay, don't let her think I'm imposing. I offered to help her at all, just as a courtesy!"
        th "Well, I came here to read!"
        "I went to the shelves with the firm intention of finding something readable."
    stop music fadeout 3
    play sound sfx_open_door_kick
    "But before I could even see the spines of the books, the door to the library swung open menacingly."
    if loki and counter_me_neu_answers == 2:
        play music music_list["revenga"] fadein 1
        show mz bukal glasses pioneer with dissolve
        mz "You!"
        "Breathing noisily, Zhenya threw her finger up, pointing belligerently at me."
        show mz angry glasses pioneer with dissolve
        mz "You're at it again!"
        mz "Are you trying to spoil my property again?"
        me "Keep quiet, you're in the library!"
        show mz rage glasses pioneer with dissolve
        "I sneered. The buzzkill shut up and stared at me with her eyes bulging."
        me "And anyway, I didn't spoil any property. I was just reading."
        th "Well, maybe I did spoil a little..."
        th "But it's none of her business!"
        mz "You've made a mess of everything in my library!"
        mz "You made me miss half my lunch because I was putting everything away!"
        me "That's too bad."
        me "So can I just go through and keep reading? I think that's what the library is for."
        "Zhenya's nostrils fluttered dangerously."
        mz "Get. {w}Out." with vpunch
        mz "And fast, or I'll ask Olga Dmitrievna where you got the keys."
        "Coldly threw the buzzkill and slowly headed to her desk. I mimicked her back and walked out of the library, unsuccessfully trying to slam the door goodbye."
        stop music fadeout 3
        play ambience ambience_camp_center_day fadein 1
        scene bg ext_library_day with dissolve
        th "That goddamned stopgap!"
        th "She certainly knows how to blackmail..."
        "I couldn't refuse the keys. Only they were now allowing me to poke my nose where the camp director highly discouraged."
        "And I had one thought. But it had to wait until tonight."
        "So I staggered doomfully back to the cabin. To sleep."
    else:
        play music music_7dl["carefree"] fadein 3
        show mz bukal glasses pioneer with dissolve
        mz "What are you doing here?"
        me "I tried to get a job in the club as an assistant, but my candidacy was rejected at the first interview."
        show mz smile glasses pioneer with dissolve
        "Zhenya looked at me thoughtfully, and suddenly (for the first time since we met!) she smiled."

        mz "Then you can help me."
        "...Except I didn't like that smile a whole lot!"
        if alt_day4_me_neu_mz_newspaper:
            th "Does she think I'm her faithful knight now, rushing to her aid at any moment?"
        else:
            th "Here I am, hiding from work in a quiet corner..."
        show mz normal glasses pioneer with dissolve
        mz "See those books?"
        "She nodded toward the pile of shabby books piled on the far shelf."
        mz "They need to be taken to storage. They've lost their marketability."
        th "Cool! How many are there? Give or take a hundred?"
        th "At least ten weighted runs. Why didn't anyone tell me that the editorial office of the wall newspaper cares so much about the physical fitness of the pioneers?"
        "I sighed heavily and took the first bunch."
        mz "What's the second hand for? You take two and I'll take one."
        th "Damn, this quest is getting harder."
        th "What's next? Is she going to tell me to walk to the warehouse blindfolded?"
        dreamgirl "Or jump on one leg!"
        show mz bukal glasses pioneer with dissolve
        "But under the stern gaze of the librarian, I obediently took the second bundle. The thin twine hurt my fingers, and now and then I intercepted the bundle."
        "Zhenya was cleverer - she just took her bundle in her hands, resting her chin on it."
        me "Lead the way. I have no idea where this warehouse of yours is."
        play sound sfx_open_door_kick
        play ambience ambience_camp_center_day fadein 1
        scene bg ext_library_day with dissolve
        show mz normal glasses pioneer at left with dissolve
        "The librarian kicked the second door open, and we stepped out onto a path that could not have been seen from the side of the path."
        me "A secret door to Wonderland?"
        mz "Not such a secret door to the warehouse."
        th "Alarm! It's not only alive, it's trying to be funny!"
        mz "Why take a detour when the warehouse is in a straight line from the library?"
        th "Indeed. The smart man won't go uphill..."
        scene bg int_warehouse_day_7dl with joff_l
        "The warehouse was nothing of interest. Besides mountains of discarded uniforms and sets of yellowish linens, it was piled high with folded waders, deflated soccer balls, and a box of faded Christmas toys."
        "We walked back and forth in silence, piling bundles of books into a corner of the warehouse and back again. To my relief, we made it in just three trips."
        scene bg int_library_day with joff_l
        play ambience ambience_library_day fadein 2
        mz "Inventory always falls on my shift!"
        "Zhenya snorted as I gallantly held the door for her."
        if alt_day4_me_neu_mz_newspaper:
            me "Isn't this the first time you've worked here?"
            show mz surp1 pioneer glasses at left with dissolve
            "Zhenya looked at me in surprise."
            mz "It's the second year. Don't you remember?"
            if dr and counter_me_neu_answers > 0:
                th "What are they all saying!"
                th "As if my evil doppelganger came here last year."
            me "No. Should I?"
            show mz bukal glasses pioneer with dissolve
            "Zhenya pursed her lips in displeasure and hummed."
            mz "That's what it looks like..."
            "She threw it into the void, then turned back to me."
            show mz normal glasses pioneer with dissolve
            mz "Would you like some tea?"
            me "What?"
            mz "Tea. Black."
            th "Is she serious now?"
            "Offering tea looked even less believable than a PE teacher deciding to call me to a moonshine tasting in the next village."
            if herc:
                "I will, thank you."
            elif loki:
                "Go ahead."
            else:
                "Well, if you don't mind..."
            th "Well, if she's offering, why not?"
            th "She wouldn't put a handful of cyanide in my tea!"
            stop music fadeout 3
            th "She wouldn't, right?.."
            play music music_7dl["carefree2"] fadein 3
            "Zhenya turned on the kettle on the windowsill next to her desk and began scattering the brew into cups stashed on the same windowsill."
            me "And why did you decide to work as a librarian?"
            mz "Because I need community service credentials."
            "Calmly replied Zhenya."
            th "Really? Just need credentials?"
            th "What about beating your chest and yelling about how much you're committed to community service?"
            th "Too pragmatic for a country built on ideals!"
            me "What are they for?"
            "It was only after voicing this question that I realized how it sounded. I was frantically thinking about how I would justify this caveat while Zhenya poured boiling water into cups."
            "But the girl, to my surprise, looked at me... with understanding?"
            mz "They give you an advantage in admission."
            mz "And I really need to get in. And preferably to another city."
            "I whistled, pushing my cup closer to me. Zhenya didn't even offer sugar."
            me "Aiming for the capital?"
            show mz bukal glasses pioneer with dissolve
            mz "I don't care where, as long as it's far away from our little town!"
            me "You don't like it that much?"
            "It was hard for me to imagine a situation in which I would agree to leave Petersburg for at least a month."
            mz "What's there to love about it? It's gray, dreary, filthy."
            mz "You wouldn't understand."
            th "I don't understand it?"
            th "Dullness, dreariness and filth are the three pillars on which my hometown stands!"
            me "There are other ways to leave, after all. A job, for example. Or marriage."
            show mz sad pioneer glasses with dissolve
            mz "Where am I going to work after school?"
            "Zhenya sighed sorrowfully. She ignored the thought of marriage."
            me "Well... I don't think know, maybe as a house painter."
            mz "I'm not tall enough to be a house painter."
            "Either in jest or in earnest, the girl said."
            mz "Nothing for tea, sorry. It's the end of the shift, after all."
            me "I'm not that hungry..."
            "I took a sip of my tea, looked around, put the cup down, and stared at my feet. The conversation was clearly not going well."
            me "And yet, why the library? You could have taken over any club, after all."
            show mz normal glasses pioneer with dissolve
            mz "It's quiet here, and nobody touches me. Except at the beginning of the shift when everyone decides to get a library card just in case."
            me "Did it ever come in handy?"
            show mz smile glasses pioneer with dissolve
            "Zhenya smiled - almost friendly this time."
            mz "Yes. When someone takes a nap in the infirmary, the comrades immediately come running for a book."
            "At this point she reminded me more of Slavya, in love with her job, than of the gloomy Buzzer, forever asleep in the library."
            mz "Or in the rain, when all activities are canceled. If it rains all day, there's a line at the library."
            th "And yet the time when technology didn't allow you to carry multimedia entertainment in your pocket was charming in its own way."
            "I immediately imagined the smell of old encyclopedias that kids pored over while making a report for class. Or university textbooks under the lonely desk lamp of a student's room, heralding a sleepless night before an exam."
            th "Information is better absorbed when it can be touched."
            th "I can hardly remember a single page of Wikipedia out of the million I read aimlessly, but I can easily retell the contents of almost every paper book I've read."
            th "Could it be that Zhenya is one of those people who sees books as her romance?"
            th "You don't have to love reading to do that. It's just enough to love books themselves, as a kind of idol, and to be in awe of them."
            th "And she certainly looks like the kind of person who would tear her head off for a bent corner of a page."
            show mz normal glasses pioneer with dissolve
            "My list of ideas for small-talk was exhausted, and Zhenya was not eager to keep the conversation going. We finished our tea slowly, lazily, and in complete silence."
            mz "Will you wash the cups?"
            th "Nothing in this camp comes without a catch. Even the most ordinary tea."
            hide mz with dissolve
            "Out loud, I did not resent it. Thanks to this tea party, I managed to do the impossible - to see a human being in our buzzkill!"
            th "For that, it's not a sin to help with the dishes."
            with dissolve
            stop music fadeout 3
            play sound sfx_7dl["eat_horn"] fadein 1
            "Just as I put the clean cups on the windowsill, a horn sounded outside the window."
            show mz normal glasses pioneer with dissolve
            mz "Go. I still have to kick Lena out and lock up."
            "I didn't disagree."
            hide mz with dissolve
            th "We didn't even go to the canteen together yet!"
            th "I'm afraid to imagine what kind of rumors that would create..."
            dreamgirl "And Syroezhkin would have challenged you to a duel in the canteen in front of the whole camp."
            th "What's he for?"
            dreamgirl "..."
            dreamgirl "Go eat already. That's what your head's for."
        else:
            show mz bukal glasses pioneer at left with dissolve
            "She collapsed in her chair, crossed her arms on the table, and collapsed on them with her face."
            th "I suppose she no longer needs my help..."
            th "The side quest has been completed, and the NPC has returned to his usual location."
            th "Only where is my reward?"
            th "And how do I see how much experience I got?"
            hide mz with dissolve
            "Deciding not to bother her anymore, I cautiously crept over to the bookshelves."
            if loki and counter_me_neu_answers == 1:
                play music music_7dl["red_lights"] fadein 3
                th "I think I left the book here..."
                "I stared at the shelf, but the familiar spine was not there."
                th "Maybe the rearrangement on the shelves was due to getting rid of old books?"
                "But my search was in vain: the textbook was not on the adjacent shelves or on the adjacent racks."
                "There was only one hope left."
                me "Zhenya, do you remember you gave me a textbook yesterday? The history book."
                me "Did you put it somewhere else?"
                show mz bukal glasses pioneer at left with dissolve
                mz "I wrote it off. It had already fallen into disrepair."
                me "What?" with vpunch
                mz "It's dirty, torn in two places. It's also got some pages bent."
                "That was a punch below the belt."
                me "Can I get it out of there?"
                show mz angry glasses pioneer with dissolve
                mz "No way!"
                "Snorted Zhenya, turning away to the window."
                mz "I've already given the camp leader a list of books that need to be replaced."
                th "What a bastard!"
                hide mz with dissolve
                "However, no one prevented me from going to the warehouse on my own-slave's keychain was still in my possession. Unless to do it now..."
                th "I'll do it tonight."
                th "Something tells me it's not a good idea to break into the warehouse in broad daylight."
                "I grabbed some Strugatsky books off the shelf and sat down in the corner."
                th "I don't want to stay in the buzzkill's lair, but I want to go anywhere else even less."
                th "At least this way I'll remember the letters..."
            else:
                th "As expected, the selection of Soviet fiction here is rich. Should I reread something by Strugatsky?"
                "My fingers froze on the spine of 'The Dead Mountaineer Hotel'."
                th "Oh, I don't think I've read that one. Isn't that a good enough excuse?"
                "I sat down in one of the chairs and opened the book."
            stop music fadeout 3
            show blink
            $ alt_pause(1.5)
            play sound sfx_7dl["eat_horn"] fadein 1
            show unblink
            hide blink
            "Horn tore me away from the book at the moment when Olaf was discovered dead."
            th "All right, I'll finish it in case I need to hide from party errands again in a quiet and inconspicuous corner!"
            "I put the book back in its place without even bending the corner."
            "The afternoon meal interested me more than the butler's exposure."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_sport_sh:
    $ alt_day5_me_neu_sport = True
    play music music_7dl["carefree"] fadein 3
    scene bg ext_dining_hall_near_day with dissolve
    play ambience ambience_camp_center_day fadein 1
    "To be honest, I wasn't going to any club. The plan was to say goodbye to Miku on the porch and go quietly to sleep in my cabin."
    "But the set-up came from nowhere."
    show mi smile pioneer at left with dissolve
    mi "Uncle Borya-sensei!"
    show ba normal uniform at right with dspr
    "Miku joyfully waved to the gym teacher, who had decided to appear near the canteen at such an inopportune time."
    mi "And Semyon is just coming your way!"
    stop music fadeout 3
    "Either Miku was very stupid, or, on the contrary, too smart (and, on top of that, too vindictive)."
    show ba em1 uniform at right with dissolve
    play music music_list["gentle_predator"] fadein 3
    "Sanich was staring at me as if he was seeing me for the first time."
    ba "I don't remember calling him."
    ba "Well, if you need something, let's go, wimp."
    show mi laugh pioneer far at left with dissolve
    pause(0.3)
    hide mi with moveoutleft
    pause(0.3)
    "Miku smiled cheerfully goodbye and galloped toward the stage.{w} I looked confused at the gym teacher."
    show ba em1 uniform at center with dissolve
    me "Well, you know, I actually…"
    show ba em1 uniform with dissolve
    ba "No talking!" with vpunch
    "He nodded his head toward the path, as if ordering me to follow him, and slowly moved forward."
    show bg ext_dining_hall_away_day at zentercenter with dissolve
    ba "Actually, I have a case for you myself."
    th "That doesn't exactly sound like something fun..."
    ba "When are you going to take the normatives?"
    me "Normatives?!"
    "I braked so hard, it was like the ground cracked under my feet."
    show ba smile uniform with dissolve
    "The gym teacher turned around, and there was a slight smirk on his face."
    ba "What, did you think you were in a fairy tale?"
    ba "You're in the sports club! At the end of the shift there's a test to see how well you've done."
    me "But I've only been in the club for four days!"
    if alt_day4_me_neu_ba_duty:
        th "And all I did in that club was volunteer work without pay!"
    else:
        th "And I didn't even go to a single class!"
    ba "It doesn't matter."
    ba "You signed up for a class? You did. Then I'll be charged for you, too."
    me "So write down any numbers you want from scratch!"
    show ba rage uniform with dissolve
    "Sanich turned to me so sharply that I almost bumped into him." with vpunch
    ba "Teach me here how to do my duties!"
    th "It's enough to do them to begin with..."
    show ba normal uniform with dissolve
    ba "Got a sports uniform?"
    if alt_day3_un_fz_neu_transit:
        "I had the uniform, but it had obviously lost its marketable appearance."
    "I shook my head, and Sanich waved his hand."
    ba "All right, you can pass as is, you won't die."
    show bg ext_square_day at zentercenter with dissolve
    th "You've got to be kidding me!"
    dreamgirl "Why don't we complain to the squad leader?"
    dreamgirl "Say, Oldmitrina, the gym teacher we signed up with is making us do something in his club!"
    th "Oh, screw you!"
    th "I just wasn't expecting this kind of voluntary-forced order."
    dreamgirl "Really, that's the last thing you should expect in a Soviet pioneer camp!"
    play ambience ambience_soccer_play_background fadein 2
    show bg ext_playground_day at zentercenter with dissolve
    "We walked out into the expectedly empty stadium. The endless glare of the puddles made me squint as hard as I could."
    "Sanich took a stopwatch out of his pocket."
    ba "First, a warm-up run of three thousand meters. I suggest you keep up the pace."
    me "Don't you have somewhere to write down my results?"
    show ba em1 uniform with dissolve
    "The PE teacher frowned, obviously figuring out my intention to leave."
    ba "My memory's good, so don't worry about it."
    ba "From this line, fifteen laps of track four. And if you try to cut back, I'll give you fifteen penalty squats for every time you leave the track!"
    show ba normal uniform with dissolve
    ba "On your mark!"
    "I stood up at the start without a care in the world. Literally everything said it was a bad idea, from my unused body to the sandals on my feet."
    ba "Ready!"
    th "I don't want to get my feet wet in the process and run my face into the asphalt!"
    $ volume(0.5, "sound")
    play sound sfx_7dl["whistle"] fadein 1
    scene bg ext_playground_day at running
    "But I had no choice, so I rushed forward as soon as the sharp whistle sounded."
    $ volume(1.0, "sound")
    th "What did Murakami say in his book about running?"
    th "I think it was something about how running helped him quit smoking."
    th "Although I seem to have quit just fine without running!"
    if alt_day3_dancing2 == 'dv_2':
        th "Well, discounting that cig of «Belomor», which I yoinked from Dvachevskaya."
    "I hadn't thought about it before, but it was the fifth day since I'd given up the nicotine monster."
    "Maybe that's why my lungs weren't burning yet, when my left side started tingling."
    th "Only eight!"
    th "Shit, it felt like I'd already run too much, but I'd only made it half!"
    "I reached the tenth lap on my last breath, but Sanich's menacing yell kept me going."
    play sound_loop sfx_heavy_breathing fadein 1
    "On the twelfth lap my eyes went black.{w} On the thirteenth lap I could no longer feel my feet. {w}I reached the fifteenth lap with the distinct feeling that I was going to fall flat and die at the finish line."
    scene bg ext_playground_day with dissolve
    show ba smile uniform at fright with dissolve
    ba "Eighteen minutes and six seconds!"
    "I stood there, folded in half and breathing heavily, so I couldn't look at the gym teacher's angry face if I wanted to."
    stop sound_loop fadeout 2
    ba "I don't even have turtles like that in the third squad!"
    ba "You're as bad as I am Thumbelina. {w}All right, get ready for the 100-meter dash!"
    th "Why..."
    "My tongue was sticking to my palate, my whole body was sweating and hurting unbearably, but I made it to the start and somehow regrouped for the race."
    th "Okay, the main thing here is to move your legs and arms, and breathe as much as possible in the process."
    th "At the very least, you can imagine running to the cash register at 10:56 p.m. with a bottle of booze."
    $ volume(0.5, "sound")
    play sound sfx_7dl["whistle"] fadein 1
    scene bg ext_playground_day at running with dissolve
    $ volume(1.0, "sound")
    "On the whistle I took off and even picked up a good pace, but by the middle of the way my body seemed to have stopped listening to me, becoming wooden, unyielding, and slow."
    scene bg ext_playground_day with dissolve
    "By the finish line I still managed to pick up speed again, but the lean expression on Sanich's face indicated that he was once again unhappy with my results."
    show ba rage uniform with dissolve
    ba "Sixteen and two!"
    ba "You're not much of a runner. People like you are the first to be eaten in the woods by wild beasts."
    show ba normal uniform with dissolve
    "He squinted his eyes, like he was remembering something."
    ba "Now let's go to the crossbars."
    scene bg ext_playground_day:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 2.0 zoom 1.5 xalign 0.55 yalign 0.55
    with dissolve
    th "We passed running in wet sandals. Next on the program: pulling up on the wet bar!"
    dreamgirl "Genres: drama, tragedy, school, yaoi."
    th "Uh-huh, and also..."
    th "Wait a minute!"
    ba "Alright."
    "Sanich patted the pole of the tallest bar to get my attention."
    ba "You pull up smoothly, no jerks. Don't wriggle your torso like you're an earthworm."
    ba "One, two, three! Go!"
    th "One…"
    th "Two…"
    "After running, the pull-ups no longer seemed like an impossible task, but on the twelfth I realized that my arms refused to bend. I struggled to unclench my numb fingers and landed painfully on the wet sand."
    show ba em1 uniform with dissolve
    ba "It's not bad, but it's still weak."
    ba "Pull yourself together, snot-nose! Any girl in your squad could kick your ass!"
    if herc:
        th "Like I'm going to fight them!"
    elif loki:
        th "Well, I'd argue that..."
    else:
        th "As if that's a secret!"
    ba "Now let's go to the gym. We could have done it here, but you're wearing a uniform."
    th "Well, thank you!"
    play sound sfx_open_door_clubs fadein 0
    scene bg int_sporthall_day_7dl with dissolve
    show ba normal uniform at fleft with dissolve
    ba "So that leaves the bench bend, the long jump, and the abs."
    dreamgirl "What about wrestling classes?"
    "The extremely unpleasant image of Sanich in latex popped into my head, and I had a hard time stifling the nausea in my throat."
    th "Well, there's not much left!"
    th "If I live to see noon, I can safely call myself a lucky man..."
    "In the coolness of the covered enclosure I felt instantly better. The dryness in my mouth became tolerable, my breathing evened out, and even my feet stopped hurting."
    "But Sanich wasn't going to give me a break."
    show ba smile uniform with dissolve
    ba "Take off your shoes and get on the bench!"
    "I scrambled up onto the bench, trying not to slip on the smooth layer of paint."
    ba "You bend over and reach with your toes toward the floor. Keep your knees straight, don't bend or arch back."
    "It sounded a lot easier in words than in practice. I couldn't even reach the edge of the bench."
    ba "Pinocchio, that's what you are!"
    "Sanich tapped the wall in a picturesque way."
    if 'soccer' in list_clubs_7dl:
        ba "We can't even put you on the gate!"
    elif 'volley' in list_clubs_7dl:
        ba "What is the most important thing in volleyball? Softness and smoothness of movement!"
    else:
        ba "You'll break in half when you reach for the shuttlecock!"
    ba "Now you hold your legs in place with the same bench and do torso lifts. On my signal you start, on my signal you finish."
    th "You should at least give out a mat on such an occasion..."
    "I doomedly lay down on the cold boards and shoved my feet under the bottom rung of the bench."
    ba "One, two..."
    $ volume(0.5, "sound")
    play sound sfx_7dl["whistle"] fadein 1
    $ volume(1.0, "sound")
    "To the deafening echo that amplified the already obnoxious sound of the whistle, I began to pump my abs."
    th "For how…"
    th "Long…"
    th "Can this…"
    th "Go on?"
    $ volume(0.5, "sound")
    play sound sfx_7dl["whistle"] fadein 1
    $ volume(1.0, "sound")
    "At the next whistle blowing, I stretched out blissfully on the floor. Sweat was streaming down my face and my hair could have been wrung out."
    ba "Thirty-four. Just short of the standard."
    show ba normal uniform with dissolve
    "Sanich put the stopwatch in his pocket and glanced at his wristwatch."
    ba "Well, the hell with the long jump. I've got a briefing session coming up."
    me "So did I pass the standards?"
    stop music fadeout 1
    ba "Ah…"
    play music music_list["eat_some_trouble"] fadein 3
    show ba smile uniform with dissolve
    ba "There are no standards, you wimp. It's a prank from the good grandpa Sanich."
    th "What?!"
    me "Ah... but..."
    me "Why?!"
    ba "So you don't hang around."
    ba "And anyway, at your age you shouldn't be such a wimp!"
    ba "So you can get at least a silver badge by the next shift!"
    th "I hope this is the first and last time I'm going to this boot camp!"
    ba "Now get out, or I'll lock you in the gym until noon."
    hide ba with dissolve
    "I scraped myself off the floor with difficulty and hurriedly ran out of the indoor building. I had only one wish: to hide from PE teacher and his hilarious pranks."
    scene bg int_house_of_mt_day with diam
    play ambience ambience_int_cabin_day fadein 1
    "Olga found me lying on the bed, moaning softly."
    show mt surprise pioneer with dissolve
    mt "And where have you been all the quiet hour?"
    me "In the club..."
    "Pitifully I stretched out."
    show mt sad pioneer with dissolve
    mt "Boris Alexandrovich?"
    "It was as if sympathy was heard in the squad leader's voice."
    show mt smile pioneer with dissolve
    mt "Let me guess, you did the standards?"
    me "Exactly."
    "But instead of splashing her hands and feeling sorry for me, the squad leader laughed wryly."
    show mt laugh pioneer with dissolve
    mt "Oh, his jokes about latecomers..."
    th "So I'm not the first one caught?"
    "The realization that there was another sucker was as comforting as ever. I even found the strength to get up and sit on the bed."
    show mt smile pioneer with dissolve
    mt "Go to lunch already, labor and defense hero!"
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_us_melancholy:
    scene bg ext_square_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    play music music_7dl["ask_you_out"] fadein 3
    "A peaceful smile played on my lips as I left the canteen."
    if alt_day5_me_neu_us_stores:
        "The squad leader really turned out to be a worldly woman who cared what happened to her subordinates."
        "And all that was left to do was to throw provisions into the cabin, find the redheads, and try to help them a little."
    else:
        "And even though I can't help the starving redheads now, I can try to talk them into just apologizing - whatever they've done."
        "That's the easiest thing to do - say you were wrong."
        "Isn't it?"
    "I guess you could call it inexplicable joy."
    "Happiness even-when you're walking, smiling, and everything in your life is ho-hum."
    "But there was a certain inexplicable sadness mixed in with that joy, whether it was something that hadn't happened or... I don't know."
    "The most important thing is that people really care about each other."
    "How, it turns out, not much I need to not feel bad."
    scene bg ext_houses_day with blind_l
    "Now I could let myself relax and remember the fairy tale into which the red-haired girl had willy-nilly drawn me, without unnecessary suffering or remorse."
    "Flares, the escape, the roads..."
    if alt_day5_me_neu_us_stores:
        "Moved along the paths to my cabin, the future tea-party spot, and smiled, silly-silly."
    "Waved to the rushing boys at the quarry - I'll be there for sure, but a little later."
    if alt_day5_me_neu_us_stores:
        play sound sfx_open_door_strong fadein 0
        scene bg int_house_of_mt_day with dissolve
        "Piled the future feast on the table in the cabin, got tea, sugar, and cups from the nightstand..."
        play sound sfx_open_door_1
        $ alt_pause(1)
    scene bg ext_house_of_mt_day with dissolve
    "And went on my way."
    th "Now I'll just find those two."
    "I didn't admit to myself how important it was for me to just do the right thing now."
    if alt_day5_me_neu_us_stores:
        "To feed the two afflicted."
    "Inhaled, and..."
    stop music
    stop ambience
    $ persistent.sprite_time = "night"
    $ night_time()
    scene
    $ renpy.show("bg ext_house_of_mt_day", what = Desat1("bg ext_house_of_mt_day"))
    with dspq
    "Coughed."
    play music music_7dl["laugh_throught_the_universe"] fadein 3
    "In my young, alien, not mine, warmed by the warm Soviet sun, heart knocked diligently persecuted longing."
    "A blow to the heart, to the head - from within splashing blue-black drops."
    "The world was hazy for a moment, and when I opened my eyes, blinking away the tears as I struggled to straighten up, I found that everything around me was..."
    "The familiar."
    "What seemed to have been abandoned a hundred years ago in the freezing streets of my home metropolis, along with those who had always given a damn about me."
    if loki:
        "Along with those who killed me so diligently that they succeeded in the end."
        me "Ksana..."
    "And everything seemed to be in its place: the ornate cabins, the lounge chairs, the bent bicycle."
    "Even the round prints where one of the cups left on the table would fit perfectly."
    "But the pink lenses on the eyes look like they've come apart."
    "And we all know that pink lenses always only shatter inward."
    "Always."
    with fade
    "It was as if the thing from which I had been running so diligently had sprung up and, extending a clawed paw through the edges of the unfulfillable, pulled me back."
    "To the 29th of December, 2018."
    th "Why did I end up here?"
    if loki:
        "Clinging to something I have nothing to do with anymore?"
        "Trying to beg forgiveness from those to whom I've done nothing but avenge?"
        "Carrying music to souls when you yourself are forced to shake with pain in the hallway?"
        "That's the way to find a teacher."
        "And those who have already destroyed me once need only finish what they started-and never think of me again."
        "I'm twenty-nine now, and I've had it all."
        "It's all behind me now..."
    else:
        "Computers that basically don't care who's working on them?"
        "The bosses at work who will find a replacement for me in less than a week if one day I snap and die?"
        "A bleeding memory that throws me into unconsciousness whenever rain happens and a short melodious name sounds?"
        "And when the broken pulse breaks, who will just remember that such a man once lived?"
        "Somehow it wasn't scary at all, like you don't get on the edge when you realize your run is over and you can't squeeze a foot of space out of you no matter how hard you try."
        "You're finished."
    "If anyone needed me, it was probably Ulyanka."
    "And her team."
    "Though it's completely unclear why."
    "But if there was Mirya... So I can be replaced in their foolish search, too?"
    "In spite of her request to do everything to the end."
    "What, that's what I can help her with?"
    th "What are you for to a girl who might well be able to find something so fantastic that you just don't belong with all your pettiness and ordinariness?"
    th "Are you nurturing the hope of following her?"
    th "Seek political asylum in the land of the eternal fairy tale?"
    th "Who needs you there?"
    th "A fairy tale can't last forever, and you're not... seventeen, she thinks."
    th "You're there, and the door is in your forehead."
    scene
    $ renpy.show("bg ext_houses_day", what = Desat1("bg ext_houses_day"))
    with dissolve
    th "Drooling, hysterical, worthy of a fifteen-year-old fool who has read Sartre."
    "I summoned all my cynicism and indifference to just keep from hysterics."
    "I crossed our street at a brisk pace, jumped out onto the next street, where the huts of the second squad stood."
    scene
    $ renpy.show("bg ext_square_day", what = Desat1("bg ext_square_day"))
    with dissolve
    "From there I left under the menacing gaze of Genda."
    "I measured and paced the surprisingly deserted and ruthless camp."
    "A few minutes ago it had seemed like a miracle incarnate, the quintessential place I'd always wanted to go."
    "But now it was becoming obvious - I had nothing to do with it at all; this camp was made for entirely different people."
    "And it will be wonderful even when I stop seeing it."
    "The clap of one palm, the sound of a tree falling in a desolate taiga."
    "Founded in 1947 by those whose children and grandchildren will one day come here."
    "Moved from its old place to a new one in 1974."
    "Names, thoughts, photo albums in the camp warden's office - huge annals of the memory of a summer I don't belong to."
    "It was as if I had stolen not only a train ticket to happiness from someone, but also my papers to be allowed into the place."
    "And now it's up to me to either go and live someone else's dreams or turn into someone... who isn't me."
    scene
    $ renpy.show("bg ext_backdoor_day_7dl", what = Desat1("bg ext_backdoor_day_7dl"))
    with dissolve
    "Outside the south gate, I sat down on a chopped deck and thought."
    me "Alright."
    "Accordingly, I nodded to myself."
    me "The camp had nothing to do with it at all."
    me "Neither did the pioneers."
    me "Then who's to blame for me feeling so bad right now?"
    "I felt weird and wrong talking to myself out loud, but I needed it now."
    "Just to voice the questions."
    "Because it sounded too creepy to answer them."
    "It was all my fault, and mine alone."
    if loki:
        "Played it out, loved it, lived it out. Did everything I could, taught as many children as I could."
        "No, of course, not everything and not everyone. Worse."
        "My music has always been stronger than me; it has never allowed itself to be cowardly, for who needs it to be so cowardly and cowardly and deceitful?"
        "No, my music has always sounded loud and honest."
        "And that is perhaps the only thing that could have justified me and given me life."
        "Even when all seemed lost and there was no turning back."
        "And yet, on the edge, I managed to break through there, into that incredible space that sounded in my soul with the rumblings of Grieg and Brahms."
        "Managed to see what sincerity, friendship, faith - the memory of a childhood you never had - looked and sounded like."
        th "You lived it as a well-tuned instrument would sound, no longer able to produce even a couple of sounds yourself."
        th "But here's the problem. Ulyana."
        th "What has she got to do with your music?"
    else:
        "I would like one day to write something that would be worthy of my time here."
        "So that I could read it before I die and pass away happy, certain that I couldn't do any better in this life."
        "And all my attempts to create anything - weren't they tiny steps on the road to 'Sovyonok'?"
        "All those pompous and pompous heroes in whom I believed more strongly than in other people, who acted in ways I myself never dared."
        "And now, as the boring game with me as the protagonist comes to an end, I suddenly find myself here, wildly, insanely lucky."
        "Where everything is the way I've always dreamed it would be."
        "Where the leitmotif of what happens is always the word 'right.'"
        "I convinced myself that once I really had the perseverance and patience to finish one of the jobs to the end, and now I just dream about it."
        "But where there."
        "A hitch."
        "I could never think of anyone like Ulyana or Danechka."
        "It was wild to me to see the links acting as a united front."
        "I didn't believe in those who were willing to go and stand to the end-and this despite the fact that half of my heroes could boast of doing just that!"
    "So it's not a made-up world, not a made-up world at all."
    "And I should be glad that I was given a ticket to a place where I don't deserve to be."
    "Because I don't know how it is — {i}there{/i}."
    "Where I closed my eyes for the last time."
    "But any tale must and will be finished."
    "And it's better not to take someone else's seat in someone else's compartment, but to go out and turn in your ticket and papers to the lost and found."
    "At least that's more honest."
    "Having convinced myself of that decision, I got up and walked back to camp."
    "We'll have to catch a shuttle bus to the district center, and then we'll deal with it, since there's no way to get out of here on our own."
    "And go home."
    scene
    $ renpy.show("bg ext_square_day", what = Desat1("bg ext_square_day"))
    with dissolve
    "And home…"
    if loki:
        "At home, music in headphones, a hard-boiled pipe, and five-hundred-ruble whiskey from the nearest «Pyaterochka»."
        "Just because I can't fall asleep any other way."
        "I haven't been able to sleep for eight years."
        "What's next?"
        "A palm waving at the head of the department who's got my breath all over her throat?"
        "Friends from the scattered vigilante cell - their lives are by no means over since that office collapsed."
        "No, I keep teaching their kids music."
        "So their fussy and annoying sympathy, their attempts to get me out in public, and then, during another exacerbation of my depression, their cowardly 'well, will you make it to class yourself, son?'"
        "Then quite logical with a history of coronary-ischemic and an official pine coffin?"
        "Why would they want me there?"
        "Why would they want me here?"
    else:
        "People who only know my name and «call this guy if the computers don't work»?"
        "The mother who remembered I existed about a year ago?"
        "Or the dystonia I never remembered."
        "It's a very handy thing."
        "You can lie on the bed for a long time, then jump up abruptly, run to the doorway and throw your hands on the overhead doorjamb, stretch out and crouch properly..."
        "And find myself regaining consciousness on the floor with a broken nose."
        "I hope one day I'll hit myself properly and fail to regain consciousness."
        "But I keep coming and coming."
    stop music fadeout 3
    play music music_7dl["more_than_alive"] fadein 3
    scene
    $ renpy.show("bg ext_clubs_day", what = Desat1("bg ext_clubs_day"))
    with dissolve
    $ alt_pause(1)
    show dn normal pioneer with dissolve
    "I was walking past the clubs when a boy I already knew turned out of there."
    dn "Oh."
    me "Hello again."
    "I waved."
    me "Where did you lose your guards?"
    dn "They're waiting."
    me "What?"
    dn "When I come back, of course."
    dn "We go together, we don't leave each other behind."
    dn "Now they let me go and get a knife."
    me "And what was your knife doing there?"
    show dn unsured pioneer with dspr
    dn "It fell out while we were sitting there!"
    me "Really?"
    "Danya nodded sedately."
    me "I see."
    "A little confused I replied."
    "And with gratitude."
    "I suddenly remembered something very important."
    me "Say, do you want me to give you my knife?"
    show dn surprise pioneer with dspr
    dn "But you need it yourself, how will you cut ships?"
    th "I won't. {w}And I'm too old for all that."
    me "That's all right."
    me "Wait!"
    play sound sfx_open_dooor_campus_1
    $ alt_pause(1)
    scene
    $ renpy.show("bg int_house_of_mt_day", what = Desat1("bg int_house_of_mt_day"))
    with dissolve
    "Leaving Danya at the clubs, I jogged to the cabin and pulled a red pencil case with a recognizable quadrilateral star inscribed in a circle out of my backpack."
    th "Like a link for four people."
    "Sadly I smiled."
    th "That'll be their mascot, for the whole company."
    scene
    $ renpy.show("bg int_house_of_mt_day", what = Dawn("bg int_house_of_mt_day"))
    with dissolve
    "I felt like I was doing something right."
    "How the gray muted fog was disappearing from my eyes, how the summer sun was warming again."
    "The camp again was becoming a place where I belonged."
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene
    $ renpy.show("bg ext_clubs_day", what = Dawn("bg ext_clubs_day"))
    show dn normal pioneer
    with dissolve
    play ambience ambience_camp_center_day fadein 3
    "And when I went back to the clubs and handed Danya a present, things were pretty much the same."
    if alt_day5_me_neu_us_stores:
        "I suddenly remembered that I never fed and talked to Ulyana and Alisa."
    else:
        th "Unless the redheads stay hungry."
    "But that's all right, they'll be up in an hour, and then it won't be long before noon."
    "They won't starve."
    if alt_day5_me_neu_us_stores:
        th "At the very least, they'll climb into the cabin and eat something there."
        th "Bon appétit to them."
    scene bg ext_boathouse_alt_day_7dl with blinds_l
    play ambience ambience_lake_shore_day fadein 1
    "It's time, it seems..."
    "The river smelled damp, and from across the beach came the shouts and tinkling laughter of those who spit on their routines and made up for a rainy morning."
    "Somewhere nearby was a brig, a boat shed, boats..."
    "But here, in this place, I was all alone."
    "It felt right."
    "The sun winked at me, encouraging me."
    "And for a moment I could see through my surroundings to a more familiar picture."
    "The cold city, the asphalt in ice and the feathery snowbird passersby flying through the sullen sky on their way."
    "I don't know why I'm there, but I'm even more irrelevant here."
    "So..."
    "Suddenly a retrospective of my life, here and there, flashed before my eyes."
    "But I realized that it's essentially up to me."
    stop ambience
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    scene bg int_intro_liaz_7dl with dsps
    play sound_loop sfx_bus_interior_moving fadein 1
    "I'll jump up from my seat on the bus, push the button and yell at the driver until he drops me off at the subway."
    "And thousands of people will wash everything I don't need with the indifference of water, leaving me clean and alone again."
    "And this is the perfect state to start all over again."
    "Because that's what I like to do: start from scratch."
    "And then what happens?"
    "Obviously!"
    if loki:
        "I'll get confirmation from the conservatory that my papers have been accepted and my exams have been passed."
        "And I'll start my studies in the brass department, and in a few months I'll rent an apartment in the Nevsky district."
        "I'll get a part-time job at 'Hali', and I'll wink at Tash on my way home from work."
        "I'll atone for my sins and help people."
        "But I won't let anyone else in. It hurts too much."
    else:
        "There will be a home, there will be a warm yellow light in the window, a place where you are welcome and welcome."
        "Where else can you believe in people and people."
        "And life experience is enough, praise the randome, only for short poems about life and love."
        "There will be my huge soup tureen waiting in the kitchen: English tea, with bergamot and lemon, and the gray but so beloved dawn is knocking at the windows again."
    "I'm back!"
    "Did you miss me?"
    "Now, one last tug, Khrushchev, fourth floor - seven times eleven steps."
    "Stomp-stomp-stomp."
    me "It's time to go home."
    "I smiled."
    me "I'm coming."
    "The world froze, opening toward me the door back to the bus seat."
    "Something in my chest froze, too."
    "How can it be, I've got it all planned out!"
    "And I'm walking: stomp, stomp, stomp."
    "It didn't immediately dawn on me that it wasn't imaginary me going somewhere, but the stomping of my sandal heels was going on behind me with a machine-gun boom."
    us "Semchik! Don't you dare, you idiot, don't you dare!"
    $ persistent.sprite_time = "day"
    $ day_time()
    scene bg ext_boathouse_alt_day_7dl with vpunch
    "Ulka jumped at me with a spurt, knocking me down."
    "Her breathing was labored and ragged, as if she'd run across the camp."
    stop sound_loop
    play ambience ambience_boat_station_day fadein 0
    "She ran very fast."
    "Yeah, couldn't have imagined a more unfortunate time."
    "I'm almost home."
    stop music fadeout 3
    show us cry pioneer with easeinleft
    with vpunch
    us "Don't you dare... You can't!"
    play music music_7dl["promise_to_meet_you"] fadein 3
    "With difficulty she squeezed out."
    me "And where did you come from so beautiful?"
    show us cry2 pioneer with dspr
    us "Don't you dare! I told you, you can't just walk out of here. You can't!"
    me "How would you know?!"
    show us shy2 pioneer with dspr
    us "I just know."
    us "Just step away from the water."
    "She grabbed me by the arms and pulled me toward the pontoon bridges swinging on the water."
    us "You promised me you'd go all the way! Promised me!"
    show us normal pioneer with dspr
    extend " And you…"
    me "And you ran off somewhere while I was with your guard."
    me "What have you been up to?"
    us "Preparing."
    me "For what?"
    show us shy pioneer with dspr
    us "To interfere with you..."
    me "To interfere with what?"
    us "To do this. You're like a child, not to be left for a moment."
    us "You can't go there. If you could, I'd tell you!"
    me "And how do you know so much about me?"
    us "From the camel!"
    "Ulyana snorted, still clutching my arm and dragging me toward the shore."
    show us upset pioneer with dspr
    us "Why did you even agree and go to the pier yesterday if you were going to do all that nonsense?"
    me "Let me go, I'm not going to drown myself!"
    scene bg ext_boathouse_day
    show us normal pioneer
    with dissolve
    "I rumbled when we got ashore."
    us "Honestly?"
    me "I swear."
    us "And never at all?"
    me "What am I, a fool, to drown myself? Why would I?"
    show us sad pioneer with dspr
    us "Promise!"
    me "I promise, what's the big deal?"
    show us angry pioneer with dspr
    us "How else can I be with you if you're acting like a fool?"
    me "What fool?"
    "I was outraged."
    me "I am quite responsible for my actions!"
    show us normal pioneer with dspr
    us "I can see that."
    me "And anyway, I can do what I want, nobody tells me what to do!"
    show us sad pioneer with dspr
    us "You can't."
    "Vigorously dropped Ulyana."
    us "You have no right."
    me "Why?!"
    show us smile pioneer with dspr
    us "You promised."
    me "So?"
    us "Promised twice. Yesterday and today."
    us "Is your word worth something? Or was it for nothing that I believed you yesterday?"
    "This is where she caught me in the act."
    me "No! But..."
    show us normal pioneer with dspr
    us "You don't want to..."
    "Slowly she began."
    us "Refuse..."
    "What an asshole, huh?"
    "What am I supposed to do with her?"
    "I can't just say something like: «Yes, my word, I want - I take it, and in fact go play somewhere else»."
    "It's not that she won't forgive me."
    "I'll get over it somehow."
    "I."
    "I can't forgive myself."
    "And just to say something, I muttered:"
    me "And Tonik was showing me a movie today. They're sad that you left them and went to spoil the candle to your squad."
    me "So much for being a role model."
    show us normal pioneer with dspr
    "Ulyana endured it without blinking an eye."
    us "I don't go searching without them."
    us "And they without me."
    us "We are all waiting for you alone."
    me "What about Danya's dream of becoming lighthouse keeper?"
    us "What's that got to do with it?"
    me "Nothing to do with that."
    "I sighed and turned away."
    "The sun was still high, but little by little the shadows were getting longer and longer, and the peace and tranquility of my soul was growing."
    "If only it were not for one spoiling toad."
    us "There's a bonfire tonight."
    me "Will you explain to me why you need me?"
    "I asked deafly."
    me "I'm the oldest, I don't believe in any of your nonsense."
    us "So what?"
    show us smile pioneer with dspr
    us "No one is forcing you to believe."
    us "But you took the first step. So now you {b} must{/b} take the next."
    me "And where will that step be?"
    us "To the quarry! Remember?"
    me "To the quarry?"
    "I sighed."
    me "Alright. Lead me then."
    show us laugh pioneer with dspr
    us "No. Yourself! All by yourself!"
    me "How am I going to find my way?"
    show us normal pioneer with dspr
    "Ulyana looked at me like I was stupid."
    "It was more than obvious to her to solve problems of this kind."
    stop music fadeout 3
    us "Okay, look. Now you go to the gate, next to it there will be a stand with a map..."
    stop ambience fadeout 3
    return

label alt_day5_me_neu_us_career:
    scene bg ext_stand3_7dl with fade
    play ambience ambience_camp_center_day fadein 3
    play music music_list["into_the_unknown"] fadein 3
    "I'm not so sure that no one noticed me - but there was no yelling, that's a fact."
    "Nor was there any attention paid to my person."
    "Not at all, for all the time I stood there studying the map of the unknown master, not only did no one look at me - no one even walked by me!"
    "And that was extremely strange."
    "Even considering that it had been a long and thoroughly silent hour around camp."
    stop ambience fadeout 2
    scene bg ext_path_day with dissolve
    play ambience ambience_forest_day fadein 3
    "Be that as it may, the crowns of the native forest once again closed overhead, I headed down the path on my way to the Unknown!"
    scene bg ext_sandpit_day_7dl with dissolve
    "And I was extremely surprised when instead of the expected tiny clearing, which on the map was marked as a 'Rest', my eyes from behind a parted forest appeared a huge hole!"
    "Not a ravine, but rather even a quarry! The almost steep vertical walls gave away this product of human activity headlong."
    "Even though the edges and slopes of the quarry had long since been taken over by young undergrowth, and the sand was no longer visible because of the ubiquitous moss and coniferous cushion underfoot."
    "There were older trees along the edge of the hole, so the picture was funny and touching - like a kindergarten where the adults tend and protect the little ones from the hostile world around them."
    "The very edge of the slope had been wisely and providentially fenced off by wooden railings - the patch turned out to be a sight to behold."
    "I walked over to the railing and leaned against it, looking thoughtfully at my surroundings."
    "It was quiet here, empty. Good."
    "Even though Ulyanka wasn't here either, I suddenly felt like just standing there and resting."
    "My attention was caught by some noise or knocking somewhere to my right."
    "So, ignoring the cries of my instinct for self-preservation, I pulled away from the fence and went to see what was there."
    "Somehow it was very calm somewhere inside - some kind of understanding that no one here would ever want to hurt me."
    "Where it came from, I didn't really understand."
    scene bg ext_path2_day with dissolve
    "A blur of light flashed through the thicket, and I picked up the pace."
    "But I didn't catch up."
    "I couldn't."
    "Or maybe I was dreaming about it - it happens, doesn't it?"
    "But from here you could see with the naked eye the work of some creep that had mutilated the bark of a pine tree."
    "And for what, you ask?"
    "A miserable crooked heart with a big plus in the middle."
    "The John Doe didn't have time to leave any names or initials or callsigns, so he was trying to get away faster."
    "With a shrug of my shoulders, I decided not to waste time searching and chasing."
    "Something, looming at the edge of my vision for a while, caught my attention."
    "I turned my head in that direction and saw a similar heart there."
    "Only here no one had time to interrupt the sculptor."
    "There was a note in the heart: «Zhenya»"
    th "Could this be our Buzzer? It can't be. I'm sure there have been a dozen of them around here."
    "I ran my fingers over the dried, healed scratches on the bark, and glanced automatically to the next tree."
    "The next tree had a heart on it again - but with a different inscription, and it wasn't nearly as smooth."
    "It was the same on the third tree. The fifth, the tenth..."
    "Looks like more than one generation of romantically inclined vandals have been here."
    "What is this? A pilgrimage site?"
    th "Or just a local shrine, a camp site?"
    show dreamgirl_overlay with blind_d
    dreamgirl "You could say that. This place is called «Forest of Memory»."
    "There seems to be considerable significance attached to this place in camp folklore."
    "So let's not be worse than others, and..."
    if loki:
        scene cg d5_un_carrier_7dl with dissolve
        "When I came out again to the edge of the quarry with the railings, I found that I was no longer alone here."
        "A silhouette stood out brightly against the darkening forest, clearly visible from my position, so I decided to change my habits and not pretend as if I didn't exist."
        me "Hello."
        "I said hello with a tense back and a mop of thick, purple-tinted hair."
        me "Have you seen Ulyanka?"
        scene bg ext_sandpit_day_7dl
        show un surprise pioneer
        with dissolve
        un "H-Hello."
        "Lena flinched, seeming a little startled by the surprise."
        un "No, I didn't."
        me "Mind if I bore you?"
        show un shy pioneer with dspr
        "She moved her shoulder indefinitely and hid her eyes:"
        un "As you wish."
        me "Thank you."
        "Honoring this as permission, I walked over and stood beside the momentarily stiffened girl."
        "I didn't really feel like talking, so instead I decided to look around."
        "The concave slope at this point was fortunately shaded by a row of pine trees, and a wooden railing protected me from falling off the steep edge."
        "A little farther away the shade ended, so the lone pine just above spread out loosely and with all its appearance embodied vitality and vitality."
        me "It's beautiful here."
        un "Yes..."
        me "Do you come here often?"
        un "No."
        "Now we're talking. I grabbed at the heated railing, which someone's idle hands had already chopped up with hundreds of names, thousands of hearts."
        "One, especially the deep one, caught my attention involuntarily, and I ran my finger through its curves mechanically."
        un "Uh… S-Semyon?"
        "Unabashedly asked Lena."
        me "What?"
        un "Y-you d-don't know, how this quarry is called?"
        "Continuing to stammer just the same, Lena asked."
        me "Do quarries have names?"
        "I shifted my gaze from the forest panorama to the girl standing next to me, and her cheeks immediately flared."
        un "Y-yeah… Maybe, you're right."
        "The heat-soaked silence over the slope has once more thickened."
        me "Why do you ask that?"
        show un smile pioneer with dspr
        un "Well..."
        "Lena smiled unabashedly."
        un "The quarry has no name, yes."
        un "But the forest... The Forest of Memory."
        th "How do you know, shaman?!"
        dreamgirl "Secret!"
        me "Didn't see anything like that on the map."
        show un normal pioneer with dspr
        un "It can't be on the maps."
        "She waved her hand toward the horizon."
        un "Neither can that highway."
        me "Why is there a highway here?"
        "As far as I remembered, there were no roads near the camp at all, and the only one leading here ended at the gate."
        un "I don't know."
        "In a slightly bolder voice she answered."
        un "But it's not on the maps either."
        me "I see. Why is the forest called that?"
        show un smile pioneer with dspr
        un "Don't you know?"
        "Shyness and shyness were slowly receding, leaving me alone with the real Lena."
        "And the present Lena was not afraid to laugh or be surprised."
        "Now she smiled and looked at me like a fool."
        "And there was nothing threatening or insulting about her most slightly condescending smile."
        "Just... as if I should have known something, a matter of course, since I was here and I was asking questions."
        me "Not at all."
        "I answered honestly."
        un "The Forest of Memory is called that because it helps people remember. {w}That's all."
        me "That's all?"
        un "Yes. You come here and if you want to remember something hard and fast, you carve a name or a letter here."
        "She pointed to the railing."
        un "Although some people carve on trees."
        me "Vandals. Barbarians!"
        show un normal pioneer with dspr
        un "That's the custom."
        "She faded."
        un "It wasn't my idea. I'll go, okay?"
        hide un with dissolve
        "She turned and walked away. And in the place where she had just stood, right under her arm, you could make out two freshly carved symbols - an arrow and the letter 'D.'"
        un "Also, you can't get here if you don't know the way, or someone won't show it."
        "A gust of wind blew through my mind."
        me "What mystics."
        "And I've always been skeptical of mysticism."
        "After picking at the arrow aimlessly, I looked around and staggered up the path: in the branches of an isolated pine tree I noticed something familiar, with a camouflage cast."
    else:
        "There was a piercing whistle from the side of the pit, and a scarlet T-shirt flashed through the trees."
        me "There's the hero of the day... no tie."
        "I summed up and hurried down toward the destination of my journey."
    stop music fadeout 3
    scene bg ext_sandpit_day_7dl with dissolve
    me "Hey."
    "I called out, stopping by the tree."
    play music music_list["i_want_to_play"] fadein 5
    show us normal sport far with dissolve
    if loki:
        us "Did you talk to Lenka? She's always so serious."
        us "Reads too much, woe from wit."
        me "You think so?"
    show us normal sport with dissolve
    "Ulyana has already changed into a sports uniform, a bit more comfortable for climbing trees."
    us "So?"
    me "What were you doing there?"
    us "You think that's your business?"
    me "No. But..."
    us "That's what I think."
    us "I'm going."
    me "Wait! I wasn't just looking for you."
    us "And why would you do that?"
    us "You'd better feed a starving child!"
    me "I'm sorry, Olga was watching at lunch, so I..."
    "I hesitated, wondering if I should ask the little girl such a question, but she shifted impatiently from foot to foot, and I decided:"
    show us normal sport with dspr
    me "Is it true you can't get here if you don't know the way?"
    us "Why can't you. You got in."
    me "Ulyana!"
    us "Did you know the way?"
    me "I didn't."
    show us dontlike sport with dspr
    us "So why are you asking me stupid questions then!"
    "The kid got angry."
    us "Are you done?"
    me "I guess..."
    hide us with dissolve
    "Indeed, it would have been foolish to hope."
    "There was nothing to do here, so I went away."
    "But I didn't get very far."
    "There was a creaking, rustling sound behind me, and a guilty voice called:"
    show us shy sport far with dissolve
    us "Hey, newbie!"
    me "Grrrrr!"
    us "You really can't get in here unless you know the way, or unless someone leads you here."
    me "I don't believe that."
    show us normal sport at left with dissolve
    us "For nothing. Lena knows this rule, that's why she, as long as she goes here, sometimes comes here, and no one but me and my guard can find her."
    me "And how did you get here?"
    "I didn't slow my stride, so Ulyanka had to tap her feet with twice as much frequency."
    "Fortunately, it didn't seem to bother her at all."
    me "If you can't get in here."
    us "In different ways. Some were brought here by «oldies»."
    me "Did Alisa bring you?"
    "I didn't hold back my sarcasm."
    "It was so wild and implausible - Dvachevskaya setting up a secret cabin in the woods - that my tongue scratched across my thoughts."
    us "No."
    "Ulyana paid absolutely no attention to the sarcasm."
    us "She doesn't know about this place."
    me "I see. So someone from the 'Guard'?"
    us "I brought them here."
    me "You're already completely lying. I didn't know the way, and nobody brought me he…"
    show us angry sport at center with moveinright
    with flash_red
    me "OW!" with vpunch
    "I regretted the words as soon as they left my throat, but it was too late - the toe of her shoe had already neatly jammed right into my shin."
    "OW-OW-OW!"
    "I was jumping up and down on one leg, trying to blink away the unsolicited tears, so I couldn't hear what Ulyanka was cursing at me."
    "Though her face was rather angry."
    us "…on't tell you. Look it up yourself then!"
    "I made it out when my hearing came back to me."
    me "What do you think you're doing? Do you even know how much it hurts?!"
    show us smile sport with dspr
    us "I know, of course."
    "Nodded the little one."
    us "My daddy taught me, said that if a boy is very stupid, it will add to his brain for a few minutes."
    dreamgirl "Intelligence Buff +25%%!"
    me "You know where you should go…"
    "My leg was sore, but I've had most of the experience."
    us "I won't go. Did you launch a Flare with me yesterday?"
    me "Suppose so."
    us "There's your answer."
    me "What's the answer?"
    show us calml sport with dspr
    us "Stupid."
    "The girl started looking at my other leg with exaggerated attention."
    us "I mean, how could you get in here."
    me "Surprise me."
    show us normal sport with dspr
    us "This is the first time I've been here this way."
    me "How?!"
    us "What are you nervous about?"
    "She was surprised."
    us "I thought you weren't interested."
    me "I'm not nervous."
    "Barely suppressing the urge to strangle the bitch, I replied."
    me "It's just that you either tell me or I'm off."
    show us dontlike sport with dspr
    us "What's the hurry..."
    us "Let's go, it's not far."
    show us normal sport far with dissolve
    with fade2
    "Finding a barely visible path, she hurried down the slope, not turning around to see if I was following her."
    "And rightly so - what should she worry about, since she had aroused my curiosity."
    "Her path was down to the bottom of the quarry."
    "It was securely concealed by the bushes from prying eyes - from above, from below, or from anywhere: the ravine, almost completely filled with rainwater, could only be seen when one was on its bank."
    "Pulling the bushes apart, Ulyanka exclaimed:"
    show us laugh sport far with dspr
    us "Yoo-hoo! I told you so! I told you!"
    me "What the..."
    "I didn't finish."
    play ambience ambience_lake_shore_day fadein 3
    scene bg ext_lake_day_7dl
    with fade2
    "All of our last night's Flares ended up... here. Every damn ship."
    "The candles had burned out and extinguished, so there was no fear of a possible forest fire."
    "Where they came from, however, is unclear."
    "They were just here, swaying leisurely in the waves that came out of nowhere, looking as if they'd accomplished their task, but praise us quickly."
    "Apparently, the initial request-to find 'a way out' - was fulfilled exactly."
    us "I told you so! They found the way out, I told you!"
    me "You dragged them all over here?"
    th "And when did you manage to..."
    show us dontlike sport with dissolve
    us "I wasn't dragging anything!"
    "She suddenly got insulted."
    us "I told you: Flares will find a path."
    me "And how did they find it, I wonder? I don't see a river or even a stream."
    us "I don't know. And I don't advise you to find out."
    show us normal sport with dspr
    "Ulyana went around the edge of the ravine and, guided by some intuition, fished the boat out of the water."
    "The candle on it had already burned out, covering the deck with a thick, uneven layer of wax."
    us "And you got here because you decided to look for the Flare. So he helped you."
    me "I see."
    "I didn't hide the sneer."
    me "I mean, we were looking for that quarry yesterday. Right. Where you can't get to if you don't know the way."
    show us calml sport with dspr
    us "Fool. We were looking for a way. Did you expect Flares to take you right where you wanted to go?"
    me "I didn't expect anything."
    us "There, shut your mouth. Any path consists of steps. We've done the first one. Now we'll make the second."
    show us normal sport with dspr
    us "Well, shall we ask again?"
    "Thoughtfully suggested the girl."
    "I shrugged."
    me "I don't really believe that. You or someone else just picked up and moved all the ships here."
    dreamgirl "Bread and sparrow are best friends!"
    th "What?"
    dreamgirl "Well, you're as smart as breadcrumbs, and you have the brains of a bird."
    th "Are you still going to insult me?"
    dreamgirl "What else is there to do with you? Or do you think somebody had nothing better to do than haul those ships a bunch of miles?"
    dreamgirl "For what? To give you a hoax?"
    dreamgirl "Don't flatter yourself, dolt."
    "Ulyana didn't say anything at all - she just looked at me like I was absolutely insane."
    "A knife, a candle, and a piece of pine bark were revealed to the world."
    me "Where do you get so many candles?"
    us "Don't distract me."
    "Without stopping to work, the little one gasped."
    if dr:
        me "Why isn't the quarry on the maps?"
        "I didn't keep my mouth shut."
        show us calml sport with dspr
        us "Because crooked dummies drew those. That's it, shut up."
        show us normal sport with dspr
    "The girl's got her knife working fast."
    "She's good at it - one and done!"
    "It didn't take two minutes for the familiar shape of the flare-ship to stop in the child's palm."
    show us normal sport with dspr
    us "Are you going to?"
    "She asked."
    me "What?"
    "Ulyana rolled her eyes."
    us "I don't just want to launch a boat."
    me "Okay. But why me?"
    show us smile sport with dspr
    us "Well... maybe you can do even better than me."
    me "I think I'll pass."
    show us normal sport with dspr
    us "Then scram."
    "The girl pushed me aside and mumbled quickly and quickly about the windmill girlfriends and other members of the local fairy tale bestiary."
    play sound sfx_water_splash
    voice "Pluh."
    "Phlegmatically, Flare responded, and, guided by the only rules he understood, pointed his nose somewhere to the northwest{nw}"
    if loki:
        extend ", towards that very same highway."
    else:
        extend " and rocked on the waves."
    me "There's nothing there!"
    "I pointed to the overgrown reeds on the opposite shore of the makeshift lake."
    me "What in such a puddle is your boat supposed to find?"
    show us sad sport with dspr
    "No answer again."
    "I guess I hurt her. Or did I?"
    me "Look..."
    "My reward was a frown."
    me "Will you give me the knife?"
    us "Why?"
    me "I'll... I'll make me a boat, too."
    show us normal sport with dspr
    us "Flare."
    me "Him. Will you give it?"
    us "What about the Guidance?"
    me "Whatever."
    "I waved."
    with fade2
    "Apparently, at this point I had already realized that from this point onward nothing should surprise me."
    "Even the phantasmagorical nature of the picture - a tandem of two living - breathing - Flares separating and floating in the opposite direction from the hundreds of flames stuck in the bushes."
    me "Melt-melt, away you left..."
    us "You can't touch someone else's Flare."
    us "It's like a cross: you take other people's troubles on you. And you can't use your old one twice."
    "The girl explained."
    me "Then why did you take the first ship from me?"
    us "Just showed you how to do it right. You take it from here."
    us "One light, one search."
    me "Do you think he'll take us anywhere else?"
    "I looked skeptically around the resulting pond. It wasn't hard to get around if you wanted to."
    us "It will take us somewhere else, stop asking stupid questions."
    hide us with dissolve
    "Cut off the girl."
    "And, turning around, she hurried toward the camp."
    "I had no choice but to follow her."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_us_caught:
    scene bg ext_sandpit_day_7dl with dissolve
    play ambience ambience_forest_day fadein 3
    play music music_list["get_to_know_me_better"] fadein 5
    "We fell silent, she, obviously bored by the harshness, and I..."
    "It suddenly occurred to me that she didn't really need me."
    "Anything she wanted, she could have done completely on her own."
    "Even go where she needed my help."
    "It just would have taken a little longer in her case."
    "That's why I kept quiet."
    "I thought I was about to cross a certain line, and Ulka, little Ulka, would look me in the eyes with her adult gaze, behind which I couldn't see her bonyness or the unsmoothness of a sprawling teenager."
    "And she'll say something like, 'Thank you, I'll take it from here.'"
    "And I felt suddenly that I really didn't want to cut the tale in half."
    "Maybe I didn't deserve it at all, though."
    "Didn't deserve it?"
    "That's why I flinched when I heard it."
    us "You... Please don't resent me."
    th "Resent her? Right, you're confusing me with someone else."
    th "I'm the one who has to behave with the utmost discretion now, lest you flinch and blow the whole gambit."
    "That's why I kept quiet."
    us "Okay?"
    "I shrugged."
    show us normal sport with moveinleft
    us "Semyon?"
    "She overtook me and got in the way."
    me "You really haven't forgotten my name. That's funny."
    us "Well... I'm embarrassed to call you by your name for some reason. Like it's not allowed."
    me "You can't..."
    us "I'm used to Danya not usually asking stupid questions, and this is all new to you."
    show us grin sport with dspr
    us "It's your own fault!"
    "That's not a bad lunge."
    me "What did I do wrong?"
    us "Why are you so big and grown up? Like you can't stop acting like such a big man."
    us "That's why I forget myself. And big men can't come in here!"
    me "Whatever you say."
    "I sighed."
    us "You're offended after all."
    me "Am I supposed to be happy about that?"
    show us calml sport with dspr
    "Ulyana flashed her eyes and stomped her foot:"
    us "You were the very first one to come! {w}And yesterday! {w}And you were able to launch the ship, and..."
    "'It's all a huge hoax', I almost said, but instead I heard:"
    me "I guess it's more important to me than even you."
    show us surp1 sport with dspr
    us "Why?"
    me "I'm not sure exactly. But it seems to me that all these tiny steps are necessary in order to eventually come out on some kind of road."
    show us normal sport with dspr
    us "It just seems to you."
    me "Anyway, I'm used to not abandoning fellow travelers."
    me "Even if they deserve it."
    "Said it and instantly repented."
    "Like a punch, asshole. Handled the girl, it's called."
    show us sad sport with dspr
    "It was as if they had let the air out of Ulyana, and she hung her head."
    us "I wasn't going to..."
    me "You were."
    us "No! I didn't prepare for nothing!"
    me "I don't believe it."
    us "And I don't leave fellow travelers behind either!"
    me "There's a first time for everything."
    me "Especially since I'm a grown man, embarrassing you and generally useless."
    us "I didn't say that!"
    me "Disdain is enough for me. That of yours, that of your guard. But that's all right, I put up with it."
    me "You may have suffered because of your quest - but it's not my fault! So I don't know what you're sulking about."
    "After circling Ulyana, I returned to the path to the camp."
    scene bg ext_backdoor_day_7dl
    with fade2
    us "You're the one... sulking."
    me "I don't have a reason?"
    "Ulyana was silent again, diligently looking only and exclusively at the approaching southern gate."
    "A few minutes later she reluctantly squeezed out:"
    us "You do."
    me "That's just it."
    us "What am I supposed to do, shoot myself for something I haven't done yet?"
    me "No. But..."
    me "I just don't know what I'm needed for anymore."
    show us sad sport with dissolve
    us "You are needed! I... Well, do you want me to apologize?"
    me "Maybe you'll also offer to punish you in some way?"
    show us surp1 sport with dspr
    us "And so I will!"
    "The girl's on fire."
    mt "Hell no, I can handle that myself!"
    play music music_list["awakening_power"] fadein 0
    show us fear sport with dspr
    hide us with moveoutleft
    "The voice of the squad leader came to us."
    show mt angry pioneer with dissolve
    "And before us they appeared."
    "Trouble in the flesh."
    "Actually, it wasn't just the tone that was unpleasant, it was also the first question:"
    if alt_day5_me_neu_us_stores:
        mt "And what is it that we forgot behind the territory?"
    else:
        mt "Semyon, I sent you to handle the riot, not to lead it!"
    "Here I felt the irritation and annoyance of the girl hiding behind my back."
    "After all - she has such an important mission, and here are adults... with their nonsense."
    "So I, obeying rather an inner impulse, stubbornly looked at Olga sideways:"
    if alt_day5_me_neu_us_stores:
        me "Taking a walk, don't you get it?"
    else:
        me "I didn't find Alisa, but I looked after Ulyana."
    mt "Really?"
    mt "I don't remember letting you go."
    me "Probably because we didn't even ask you to go? Ulyana, go, it's my fault, I'm to be punished."
    show us surp1 sport at left with moveinleft
    us "Yes?"
    "She was happy."
    us "Then I..."
    show mt rage pioneer with dspr
    mt "STOP RIGHT THERE!" with hpunch
    show us sad sport with dspr
    "The gym teacher looked out of the gate for a second and then hid."
    show mt angry pioneer with dspr
    mt "Alright."
    "The squad leader started."
    if alt_day5_me_neu_us_stores:
        mt "You will be punished with supper for unauthorized leaving the territory."
        me "Well, you don't get punished with food."
        mt "Any other objections?"
        show us surp1 sport with dspr
        us "Can we not get punished?"
        mt "Of course you can! You, Ulechka, have behaved so well! And you did the best in front of your parents yesterday, didn't you?"
        show us sad sport with dspr
        us "N-no, but..."
        mt "That's why you lose your supper, and you, Sidorova, also lose your bonfire."
        mt "I won't let you ruin this event!"
    else:
        mt "Persunov - you are without supper."
        me "But you said yourself..."
        "Weakly I protested."
        show mt normal pioneer with dspr
        mt "So you found everyone, negotiated an apology, and generally did as I asked?"
        "I hung my head."
        show mt angry pioneer with dspr
        mt "No! Instead, you ran off in the middle of nowhere, making your leader look all over camp for you!"
        mt "You think that's normal?"
        "There was a thin-thin squeak in my ears - a sure sign of impending rage, after which I will no doubt regret everything that is about to be said and done."
        me "I think you are too harsh!"
        "I began."
        me "And you have no right..."
        show mt smile pioneer with dspr
        mt "Aaah, harsh?"
        "Unexpectedly Olga smiled."
        mt "Maybe you think you could have done better?"
        "Such a question had not occurred to me."
        "But Olga was already carried away:"
        show mt angry pioneer with dspr
        mt "In that case, I'm giving you one more chance to prove yourself!"
        mt "Sidorova!"
        show us shy2 sport with dspr
        us "I..."
        mt "I'm not going to get an apology for the candle, am I?"
        mt "Then we'll consider it a relapse."
        show us surp1 sport with dspr
        us "What?"
        mt "For screwing up candle and leaving the territory you forfeit supper and the campfire."
    show us cry2 sport with dspr
    us "Hey, you can't do that! That's not fair!"
    "The girl argued."
    show mt normal pioneer with dspr
    if not alt_day5_me_neu_us_stores:
        mt "And you, Persunov, are put in charge."
        mt "Let's see how you do as a squad leader."
    mt "Now get back inside!"
    if alt_day5_me_neu_us_stores:
        me "But that's not fair! You can't punish twice for one thing!"
        show us normal sport with dspr
        "I was indignant, ignoring Ulyana's attempts to get attention."
        "It's not that I want to stand up for anyone, it's just that this way of putting it hurt my heightened sense of justice, which I don't know where it came from."
        me "Then punish me, too! I left, too."
        mt "That's good."
        "My demarche didn't seem to upset the leader one bit."
        mt "I was just thinking about who I could get to keep an eye on the punished one while we all made a fire."
        mt "You two keep an eye on each other."
        show us calml sport with dspr
        us "Hey!"
    show mt angry pioneer with dspr
    mt "I don't understand, why are you still here? March to the grounds!"
    hide mt with dissolve
    "With a sigh, we staggered back to camp, encouraged by the parting shouts of the squad leader."
    stop music fadeout 5
    stop ambience fadeout 3
    return

label alt_day5_me_neu_us_punishment:
    play music music_list["smooth_machine"] fadein 5
    play ambience ambience_camp_center_evening fadein 3
    scene bg ext_square_sunset
    show us angry sport
    with dissolve
    us "Well, I'll tell that Olechka Dmitrievna... Ugh!"
    "The girl wagged her fist in the middle of nowhere."
    "She walked around and was angry, and pissed."
    "She stomped her feet and resented and booed."
    "And I smiled and squinted at the sun."
    "We sat on the bench - this was our resistance headquarters."
    if alt_day5_me_neu_us_stores:
        "Though I was little concerned about starving to death - I remembered suddenly that I still had supplies from lunch in the cabin!"
        "Although I should have given half of them to Dvachevskaya, but first, she had supper, and second, she was about to have baked potatoes!"
        th "It'll be all right."
    else:
        "Despite all the shouting from the squad leader, Ulyana never changed back into her pioneer uniform."
        "Instead, she climbed into the cabin and pulled out a couple of caramels, which she fraternally shared with me."
        "I remembered that the leader was bound to have a supply of sweets, so that if she got really hungry, she could have a little piece of light."
    "And even though everyone else had left, leaving us practically alone here, I felt no anxiety or envy."
    "No, I was just glad - of the summer, of the setting sun."
    "Even Ulyanka's booing."
    "We hadn't spent much time together, but we'd become friends and bonded over each other."
    "And the inexplicable things that appeared, like Tonik's abilities and the Lights and stuff from the land of childhood, only tied us even tighter together."
    me "That's what you're getting worked up about, isn't it?"
    "Lazily watching the pioneer column move away, I asked."
    me "Is there honey on this fire?"
    show us normal sport with dspr
    us "No, but how - they're all there, even the guards."
    me "What cause for sadness."
    show us smile sport with dspr
    us "No, if you think about it that way..."
    us "Here's interesting, too! Even a thousand times more interesting!"
    th "It depends on the mentality."
    "I, as a self-sufficient person, was perfectly capable of entertaining myself."
    "But what's Ulyanka to do?"
    me "What is it?"
    us "Don't you get it? They left us a whole camp! You can do what you want!"
    "I shrugged."
    "It didn't seem so great to me. It just didn't bother me particularly."
    show us normal sport with dspr
    me "I don't get it."
    us "You're a nerd, Semich. It's a whole big country - you can only play hide-and-seek all day here."
    me "And you want to play hide and seek?"
    show us grin sport with dspr
    us "Yes!"
    me "It occurs to me that all these rules of yours are made up by nobody knows why."
    us "Normal rules!"
    "Declared Ulyana."
    us "They've never let us down yet."
    me "Yeah, is that why you've been doing nothing all shift?"
    show us dontlike sport with dspr
    us "We aren't doing nothing, do you know where we even started?"
    "I didn't know. I didn't want to know."
    me "It won't get any worse. Worst case scenario, we'll just find those ships where we left them."
    "I was dying to believe in the warm magic of these places, the Inexplicable hovering at the very edge of perception, but..."
    "After all, you can't take the experience away-and my inner cynic demanded solid tangible proof of any fiction, otherwise reacting to it as grandmother's fairy tales."
    me "We'll just go and see, that's all."
    show us laugh sport with dspr
    us "Yes, now they won't punish us with supper when they catch us, they'll shoot us right away!"
    me "Are you coming?"
    show us smile sport with dspr
    us "You ask! Of course I am!"
    scene bg ext_lake_sunset_7dl
    play ambience ambience_boat_station_night fadein 3
    with fade
    "Needless to say, our Flares were gone."
    "And all the others, too."
    "No matter how hard I tried, no matter how hard I shined my flashlight, no."
    "There was nothing."
    "And I was only more convinced that either something unusual was going on here, or I was being played around in the most banal way."
    show us normal sport with dspr
    us "Looks like Danka's already been here."
    "Thoughtfully reported the little one."
    me "Did he take the ships?"
    us "No, of course not!"
    "She looked at me with indignation."
    me "Then where did they all go?"
    us "Same place where did yours go! You didn't take your Flare, did you?"
    me "No."
    us "Neither did they."
    me "What do you mean?"
    show us smile sport with dspr
    us "The owner found the Flare, so he has completed his task. He is no longer needed."
    me "And?"
    us "And that's it!"
    me "So where did the ships go?"
    us "That's it! They did what they were made for! That's why they're gone."
    me "Where did they go?"
    us "Gone!"
    me "Gone where?"
    show us sad sport with dspr
    us "Rrrr... Leave me alone. I'm sick of you, you nerd. I know where my yesterday's went, and tomorrow I'll know where my today's went."
    me "Will you find him?"
    us "No. I'll just find out. How you knew how to get out here. {w}Because you knew where your Flare went."
    me "But I didn't..."
    "Here I thought it smart to shut up, since I really did go out to the quarry on a hunch."
    us "Yeah. Shall we go looking for the Flares tomorrow?"
    dn "Say yes."
    "A familiar voice came to us, and the inseparable trio of links came ashore."
    show us normal sport at left
    show dn normal pioneer at zenterright
    show al normal pioneer at fright
    show tn smile pioneer
    with move
    dn "Come with us?"
    show us smile sport with dspr
    us "Yes! You said yourself it couldn't get any worse."
    me "What are you doing here?"
    show dn smile pioneer with dspr
    dn "We ran away from the fire."
    me "Just like that?!"
    "I wasn't hiding my horror."
    me "You're going to get your ass kicked by the squad leader again! And how did you get here through the woods?"
    us "You're hopeless after all."
    "Ulyana shook her head."
    us "Don't you realize you can't get lost now?"
    me "No."
    with fade
    me "Okay, we've looked at the ships - they're gone. Now the second question: what do we do next?"
    play sound sfx_stomach_growl
    show us upset sport with dspr
    us "Eat something."
    "She sighed."
    us "I'm hungry. We're out of candy."
    hide dn with fade2
    "Danya, shaking his head guiltily, took a step back and vanished into the darkness."
    if alt_day5_me_neu_us_stores:
        me "Do you really want to?"
        show us sad sport with dspr
        "Ulyana nodded and looked at me pitifully:"
        us "You don't have anything?"
        me "As a matter of fact..."
        show us surp1 sport with dspr
        me "I do!"
        "I finished to the delighted squeak of a girl."
        me "There's still some stuff in the cabin from lunch. It's just getting a little stale."
        show us smile sport with dspr
        us "Bullshit war, let's use it all for good deeds!"
        us "Where do you have it?"
        "She jumped up and pulled me with her."
    else:
        "I sighed."
        me "Don't have anything."
        me "Although I can offer tea."
        show us sad sport with dspr
        us "What's that water to me, a gut punch to the head!"
        $ counter_us_7dl_px = 3
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_us_full:
    scene bg ext_backdoor_sunset_7dl with fade2
    play ambience ambience_forest_evening fadein 3
    show us smile sport with dissolve
    play music music_list["tried_to_bring_it_back"] fadein 3
    us "Hurry up, hurry up!"
    "If we walked relatively calmly for the first half of the way, we approached the cabin on the run."
    stop ambience fadeout 2
    scene bg ext_house_of_mt_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 3
    "Grabbing the key right out of my hands, Ulyana rushed to unlock it, then hid inside with a gesticulation."
    "Shaking my head, I followed her."
    play sound sfx_open_dooor_campus_1
    $ alt_pause(1)
    scene bg int_house_of_mt_sunset
    show us smile sport
    with dissolve
    "By the time I got to the cabin, Ulyana had already gutted the bag."
    "I only caught the moment when she had finished sculpting a bachelor sandwich out of the available wealth: maximum harmful substances per unit bite."
    "And gnawed into it!"
    us "Ummmm!"
    "I didn't understand anything, and just in case, I clarified:"
    me "Is it good?"
    show us calml sport with dspr
    us "Some wet ones."
    "With difficulty chewing, she responded."
    me "They're with butter and tomatoes, what did you want?"
    us "Why are they stale? Is there anything to drink?"
    me "Stale because it's from lunch. I was supposed to bring them to you and Alisa and try to reconcile you and the squad leader."
    show us angry sport with dspr
    us "And you didn't say anything?! You're such a bug!"
    "Ignoring her remark, I poured water into the jar and threw the boiling pot in."
    "It made me hungry, too."
    "Especially after last night's robbery, I remember having a couple or three pieces of candy left over, too."
    us "And the bread was sliced awkwardly, in huge chunks!"
    me "So break them in half."
    us "And this cheese."
    "The girl went on booing."
    "I raised my eyes to grief, trying not to say something harsh."
    me "You don't like cheese?"
    show us shy sport with dspr
    us "...I do."
    "Reluctantly replied the kid."
    me "Then chew and don't perform."
    show us dontlike sport with dspr
    "Angrily flaring her teeth, Ulyana nevertheless followed my instructions."
    "By the time the boiling water arrived, we had consumed three sandwiches - one of which I won back only at the cost of biting my fingers."
    "Three tomatoes, two cucumbers, a few slices of bread with cheese and sausage - everything a growing body needs!"
    show us calml sport with dspr
    us "Nothing else?"
    me "No. Say thank you for that, too."
    "With a sigh, she stroked her stomach:"
    us "Well, at least something. Hey, will you pour me some tea?"
    me "I will."
    "I couldn't help smiling as I watched her pour four spoonfuls of sugar into her glass."
    me "Aren't you getting anything sticky anywhere?"
    show us normal sport with dspr
    us "No. And give me the candy, I need it more."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_us_hideandseek:
    play music music_7dl["breath_me"] fadein 3
    scene bg ext_square_sunset with joff_l
    play ambience ambience_camp_center_night fadein 3
    me "Was it delicious?"
    show us normal sport with dissolve
    us "Uh-huh."
    me "What should you say?"
    us "Not enouuuugh!"
    me "Thank you very much."
    us "Also, I'm bored. Will you cheer me up, comrade squad leader?"
    me "Why a squad leader?"
    show us smile sport with dissolve
    us "You're in charge of me, so be strong! You're a squad leader now!"
    me "I don't even know what to offer you..."
    show us laugh sport with dspr
    us "I do!"
    hide us with dissolve
    stop music fadeout 2
    $ persistent.sprite_time = "night"
    $ night_time()
    scene bg ext_square_night with fade
    play music music_7dl["sneakupon"] fadein 3
    "I was a lot smarter this time than last time."
    "This time I climbed up the pedestal and hid behind the bronze leg of our all-arounder."
    "Not that I tried my best to hide."
    "Still, the chaser was Ulyanka again - she ran very fast, but she couldn't hide at all."
    "Constantly giving herself away with a giggle from the bushes."
    with fade
    "But I gave in to her, little by little -, she was very sad if she couldn't find me."
    "The molten July evening flowed smoothly into the cool, flower-scented night, which made me want to laugh and do silly things."
    "Maybe romantic things, too."
    "Holding hands, there. I don't know."
    "I'm playing hide-and-seek instead."
    "Stupid? I don't know, I wouldn't say!"
    "Especially since the wind was now and then blowing bits and pieces of sound, stirring and stirring up something half-forgotten."
    "Then the sound of water splashing would form a chord familiar from childhood."
    "Then the echo of Ulyana's laughter."
    us "You fool, your feet are looking out from behind the bench!"
    "And immediately - stomping toward the infirmary, where our wand was standing: a menacingly red fire shield, the twin brother of the one that hung in front of the clubs."
    "And I couldn't tell if I was imagining it, or if Ulyanka really had already caught someone."
    "It seemed to me that Ulyanka's voice and laughter were getting closer and closer, so it did not seem, so it did not seem."
    th "Hush, I think it's her."
    "My intuition was right - the familiar tapping of heels came from the gate, and Ulyana was out on the square."
    "From the other side, so that the bronze leg was reliably hiding me from the waterwoman."
    "Ulyanka flushed and looked very pleased."
    "And here her chic tails, so as not to interfere with her running, she put them back and chipped them off."
    "The short shorts gathered up and skewed amusingly, the once white, now gray socks rolled down to her sandals."
    "I froze, listening to her frequent breathing."
    "I peeked out from behind the shelter for a moment - Ulyana was standing sideways to me, turning her head and licking her lips."
    "Everything in her blue eyes - the excitement, the excitement... And the confusion."
    us "Where'd you go, Syomische?"
    "I couldn't stand it and chuckled."
    "Thereby, of course, completely disguising myself!"
    "Ulyana jumped up and down."
    show us laugh sport with dspr
    us "Aha, Syomich!"
    show us laugh2 sport with dspr
    us "Gotcha!"
    show us laugh sport close with move
    "She rushed toward me!"
    "And it was as if I were frozen, waiting for her to come closer..."
    "So that when she got close enough, I could take a step and push off..."
    hide us
    "...jump over her!"
    "...land badly and, crouching on my bruised leg, run toward the infirmary, ignoring the indignant 'hey' behind me."
    scene bg ext_square_night at fast_running
    with dissolve
    "There was never a moment's silence of stomping behind me, but it sounded strange enough."
    "But I wasn't distracted by nonsense at that moment."
    "I tried with all my might not to be tainted!"
    scene bg ext_aidpost_night at fast_running
    with dissolve
    "We didn't run on slabbed paths and even just treaded 'speedwalks' were squeamish."
    "No, there was some special delight in breaking through bushes, piercing through branches, and leaping over the airy roots of pine trees."
    "I didn't even try to get the turnip out of my hair anymore, and my shirt had long since taken on a delicate shade of salal."
    "The stalks whipped at my face, got in my eyes, and Ulyana kept stomping and sniffing behind me."
    "It wasn't until the finish line, when I caught my foot against my leg and flew toward the saving shield, that I suddenly realized what had been confusing me all this time."
    "Got it!"
    stop music fadeout 3
    scene stars with dissolve
    "A small hand immediately clapped on my shoulder."
    us "Got... cha!"
    "Ulyanka exhaled, falling down beside me."
    play music music_7dl["melancholy_sun"] fadein 3
    "I sat down, checked my pocket with my phone, automatically - didn't crush it, didn't bump it."
    "No, it's all there."
    "Ulyana sat down next to me, too, gleaming with her eyes, smiling:"
    us "I got you! I got you!"
    me "It wasn't particularly hard. I twisted my ankle."
    us "I know."
    me "Is that why you gave in?"
    "She opened her happy eyes and nodded eagerly."
    "And she did! Knowing the way she ran, it wouldn't have been hard for her to catch up with a waddling invalid!"
    "But I almost made it to the bailout, so..."
    me "That's not fair. You're a crook."
    us "And you're not? Jumping over me is fair? Syomische-cheatishe!"
    "I looked around: by the shield, Alka and Tonik of the trio that joined us in the process were playing knives."
    "Ran away from the fire, my ass."
    me "Didn't you catch Danya?"
    us "You'll catch him yet."
    "Ulyana grumbled - she didn't like the idea at all that anyone could run any slower than she did."
    me "And where did you see him last?"
    us "On the wall next to the music club."
    me "Didn't catch him."
    scene bg ext_aidpost_night
    show us normal sport
    with dissolve
    us "How?"
    "Ulyana rose from the grass, shaking herself off."
    "Giggled as she looked at me:"
    us "You have a streak across your belly. Green."
    me "Whatever."
    "I lightheartedly brushed it off."
    me "Let's all go get him together then."
    us "I'm not going. The wall is two meters, I can't jump that high."
    me "You give up?"
    "I trolled her."
    show us sad sport with dspr
    us "Yeah, I guess so."
    us "I'm tired."
    "As I noted above, she was much worse at hiding than she was at running."
    me "Then scream."
    "Ulyana looked at me angrily, but obediently gathered more air in her chest and began:"
    us "Danka, come out! That's it, you win, I give up!"
    "No answer."
    "Only laughter coming from somewhere in the square."
    us "Help me, will you?"
    "We looked at each other and smiled:"
    voices "Dan-ka, come out!"
    "No answer again."
    us "I don't want him to fall off that wall."
    "Said Ulyana anxiously."
    "From across the square came hysteria instead of laughter, and Danka appeared in the clearing."
    show dn grin pioneer at left with dissolve
    "He was in his usual disheveled state, but, unlike me, he didn't have grass stains or turnip marks on him."
    us "Danka, you big lug, where have you been climbing?"
    dn "You, Ulka, are great at looking, of course."
    show us calml sport with dspr
    us "Great at looking!"
    dn "And I was next to Syomich! Lying behind a bench, looking at the stars..."
    us "Grrrr, how these benches are already for me! I can't take it anymore."
    dn "But that's what I found!"
    "The boy boastfully tossed a bright yellow tennis ball in his hand."
    dn "Someone must have lost it."
    us "At least someone got lucky today."
    "Unhappily snorted Ulka."
    dn "No more?"
    "Ulyana shook her head."
    show us normal sport with dspr
    us "I don't want any more."
    us "I wish I could go swimming now."
    "The boys looked at each other."
    dn "Then we'll be summarily executed for sure."
    dn "So let's go and pretend we're tired and go to camp early and not get scolded."
    dn "Catch!"
    "He threw the ball to me."
    hide dn with dissolve
    al "See you tomorrow."
    "Politely said goodbye Alka before the trio melted into the darkness."
    show us normal sport at center with move
    us "Well, what do you say, Syomische?"
    "I thoughtfully scratched my belly - rimmed it while I was sliding - and reported:"
    me "Why not?"
    us "Aren't you going to be a nuisance?"
    us "Never got a chance to swim at night this year."
    us "And you're kind of the oldest."
    show us smile sport close with dspr
    "With a smile, she stepped closer."
    us "You will forbid me."
    "Took my hand."
    "And, of course, I forbade it. All at once."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade2
    return

label alt_day5_me_neu_us_warm_evening:
    scene cg d5_us_rendezvous_7dl with dissolve
    play music music_7dl["someone_like_you_guitar"] fadein 3
    me "I thought I was trusted."
    us "What does trust have to do with it?"
    th "Indeed..."
    me "I'm not going to the boathouse, I'm telling you right now - I heard there are ice-cold springs."
    us "You're a nerd, Syomich!"
    "Smiling, Ulyana pulled me with her."
    us "How can you do that? Always thinking and worrying about something. Like an old grandfather."
    th "Compared to you, I'm very much and..."
    me "Where to, then?"
    us "I'll show you!"
    "She was leading me somewhere, not to the pontoons at all, not to the river."
    "And I spoke out sort of jokingly, but also hiding my bewilderment:"
    me "Ul, are you going to swim in the woods or the quarry?"
    "Instead of answering, she twitched her shoulder, though she never let go of my hand:"
    us "There are so many places to hide! And you keep looking into the woods."
    "I snickered:"
    me "Who's to say... Nakhimov, damn it."
    us "No, I don't drive fleets. Shit."
    "That last word was clearly not in my direction."
    "No, there was a creek crossing the path here and, judging by Ulyana's disgruntled look, there was something posing as a bridge."
    "Yeah, it floated away."
    us "The rain must have washed it away."
    "Annoyingly, the girl confirmed my conclusions."
    "I went to the shore, squatted down, took the icy water in my palms."
    "Really icy."
    "But delicious, clear - even in the dark you could see the pebbles at the bottom."
    me "Will you jump over it, sportswoman?"
    "Ulyana squinted at me and, nodding, sat down, gripping the strap of her sandal..."
    with fade
    "And I leaped up, picked her up in my arms, and our touching tandem, accompanied by gushing squeals and laughter, forced its way across the creek."
    "The lanterns didn't reach here, the moon was barely visible through the tangle of branches, but the distinct blush I was able to make out."
    "I wasn't imagining it, was I?"
    "Laughing, I crossed the icy water in two steps, fearing only to stumble or slip."
    "But Random had mercy."
    scene bg ext_un_hideout_night_7dl
    show us surp3 sport
    with dissolve
    us "You're crazy, Syomich, as it is, crazy!"
    "Ulyanka exhaled to me, once again finding herself on solid ground."
    us "What if you would've dropped me?"
    me "You would have fallen on me, big deal."
    show us laugh sport with dspr
    us "I would have crushed and flattened you!"
    me "Is that why you squealed?"
    us "You're a fool, Syomische."
    "We still haven't gone over the fence, so technically Olga Dmitrievna wouldn't have anything to scold us for."
    "However, I doubted they could find us so quickly if anyone went back to camp now."
    "However, my temple and cheekbone could already feel the freshness of the big water."
    "And the path turned, climbing between the roots of the pines."
    me "To live with the wolves, that's the way to go."
    show us normal sport with dspr
    us "I thought you were older and..."
    me "More boring?"
    show us smile sport with dspr
    us "Smarter."
    me "You're a hard person to please."
    "Ulyanka ran up easily and, grasping one of the stubs, held out her palm to me:"
    us "Grab on, there's clay, it's slippery!"
    "But I ignored the outstretched hand."
    "I didn't need another fall just yet."
    show us normal sport with dspr
    us "And we're here!"
    scene bg ext_un_hideout_night_7dl with dissolve
    play ambience ambience_lake_shore_day fadein 3
    "She ran to the water, bogged down in the already damp sand."
    us "Swim, swim, swim!"
    "She ran to the edge of the water, threw off her sandals and socks and slapped her bare feet on the water."
    "When I caught up with her, I stood next to her where it was drier."
    "Having entertained herself a little in this way, Ulyana turned to me:"
    us "And you picked me up so deftly. Great experience?"
    me "Oh, yeah. It happens, you know, I wake up in the morning - and then carry the girls in my arms!"
    us "You're a ball-buster."
    me "Who calls me names..."
    us "I'm asking him seriously, and he..."
    "After muttering something, she went back to where her shoes were left and, quickly dropping her shorts and T-shirt, she jumped into the water in her swimsuit."
    "Something there was clearly directed at me, but I couldn't hear it."
    stop music fadeout 4
    "And wisely I didn't ask her again."
    play music music_list["silhouette_in_sunset"] fadein 3
    "The girl had her own concerns and interests."
    "A few minutes later, hesitating, I stripped down to my swim trunks myself and took a running dive."
    "But when I dived out, the first question that met me on the surface was:"
    us "Do you think they'll think we're... well..."
    "She smiled broadly."
    me "Don't worry. I've been friends with girls before."
    dreamgirl "Oh, monsieur, you are a great entertainer!"
    th "Shush."
    "Ulyana dove in, and for a couple of minutes, while she tried to grab my heel and I fought back, we had no time for conversation."
    "At last the air ended, and the mischievous eyes opened again over the water."
    "Wet hair was pooling around my face, and it looked funny and cute."
    us "And how? How did it end?"
    "The girl asked curiously."
    me "Nothing. Evil parents separated us."
    us "Tragedy..."
    "She hypocritically sympathized with me."
    "Though the touchingness of the moment was spoiled a little by the wave that splashed Ulyanka's nose and open mouth - apparently she wanted to say something."
    "Instead she had to spit it out."
    us "It's a very nice place."
    us "It's almost like the Forest. Except there are still people here sometimes."
    me "And Lena?"
    us "Why do you suddenly think of her?"
    if loki:
        me "I met her at the quarry, remember?"
        me "Actually, at first I thought she was in your company."
        us "No. She has her own story."
        us "A long and unpleasant one. You can ask her later."
    else:
        me "Who else but you is looking for all sorts of nooks and crannies and playing guerrillas there?"
    us "If you swim a little farther to the cape, there's a good place, logs, you can make a fire."
    me "Yes, we were deprived of a fire, let's make our own."
    us "What's the big deal?"
    me "Got any matches?"
    "I asked just for the sake of saying no."
    us "I do."
    "Wrong answer."
    me "Save them for tomorrow, for the long haul."
    us "Bo-ri-ng!"
    "She mouthed off and sailed away from me."
    us "If being big and grown up is to be so boring... I guess I don't want to grow up."
    with fade
    "She was still sulking and shivering in the wind on the beach, so it was only natural to give her my now-soiled shirt as a towel."
    "And then to put my arm around her shoulders, warming her up."
    "So the two of us were chumming on the beach while the other pioneers were having fun, making bonfires, eating potatoes, and singing songs with a guitar."
    me "Aliska had completely abandoned you."
    "Ulyana moved her shoulder."
    us "I'm very comfortable for her. I don't demand attention, I don't make silly conversations."
    us "And most importantly, I take up space. That way she would have been given someone else instead of me."
    us "Not as handy."
    me "But you have your guard."
    us "And you, if you don't run away."
    me "Can't run away from you, I suppose. Look how you knocked me down."
    "Ulyana giggled."
    "She looked disgustedly at the steam locomotive hurrying somewhere, laboriously pulling the cubes of cars behind her."
    us "Too bad we couldn't get away then, couldn't we?"
    me "Yes."
    us "Really, I don't know what we would have done? Here, we ran away, we left. And then what?"
    me "Is that you?"
    "I smiled. She was still shaking and her skin was in big goose bumps, so she pressed herself sideways against me."
    me "What's with the grown-up and boring questions?"
    me "After all, there are hitchhikers."
    us "Who?"
    me "People like that. They hitchhike without a ruble in their pocket."
    us "And... Do they succeed?"
    "Ulyana yawned silently, and if I hadn't hugged her, I wouldn't have noticed."
    me "It's up to anyone. Let's go to camp, ours will be back soon."
    me "And you're almost asleep already."
    "When I got up myself, I got her up, too."
    "Something fell out of her pocket and rolled toward the surf."
    us "A ball!"
    "Jumping forward, she picked it up, cradled it like the greatest treasure."
    me "And what do you need it for?"
    show us smile sport with dissolve
    us "I don't know. It's just yellow, it's beautiful."
    me "That's it?"
    "A slight nod of the head."
    scene bg ext_seashore_7dl with dissolve
    "And in the finally blackened blue sky, the stars were peeping out."
    "As if it were October, the most starry time."
    "Ulyana tossed and tossed a bright yellow tennis ball in her hand."
    me "I guess I should give it to the gym teacher."
    show us normal sport with dissolve
    us "I wouldn't think of it."
    me "But it's new. Or someone's parents brought it to someone."
    us "It's my trophy."
    me "...Why do you want it?"
    us "I... I don't know. You could throw it somewhere."
    me "Like what?"
    us "Can you take it to the moon?"
    me "To the moon? I don't think so."
    us "Can you at least take it to the debarcader?"
    me "There? For sure."
    show us laugh2 sport with dspr
    us "Come on!"
    me "Are you sure? It's a good ball."
    us "Throw it."
    "A short run, a swing - all textbook, at a forty-five-degree angle to the horizon - the ball whistled into the twilight."
    show us surp1 sport far with dissolve
    "With a shriek of delight, she galloped after it."
    "Something inside me snapped."
    me "ULYANA!!!"
    show us surp2 sport far with dspr
    us "Yes?"
    "She froze on the edge of the cliff and looked back at me, not understanding anything."
    me "Are you completely crazy?! Get away from there at once!"
    "She obediently moved away from the edge, looking at me."
    me "I'll get a few bald spots with you!"
    show us normal sport with dissolve
    us "But there... Eh! I don't feel like getting undressed again."
    "She yawned again."
    me "And don't. You won't find it in the dark."
    show us sad sport with dspr
    us "Isn't it dark? Like under the blanket..."
    me "It is. It's dark under a blanket."
    us "And warm. It's as cozy as home."
    "Her eyes were closing, and it occurred to me that she wouldn't make it to camp so sleepy."
    "Unless I dunk her in that cold creek?"
    th "I will."
    "I promised myself."
    stop ambience fadeout 3
    return

label alt_day5_me_neu_us_hungry:
    scene bg ext_lake_sunset_7dl
    show us sad sport
    with dissolve
    play ambience ambience_boat_station_night fadein 3
    play music music_7dl["rewind"] fadein 3
    "The poor child sat there looking at me pleadingly."
    "And there was nothing I could do to help her."
    "And it's not that I'm greedy or callous."
    "It's just that I really had nothing, well, nothing at all."
    me "You robbed me yesterday anyway."
    "Said I, recalling the contents of my homeland's stash."
    me "Well, at least there'd be candy now."
    show us calml sport with dspr
    us "Oh, don't remind me!"
    "She wrinkled her nose."
    us "I'm in trouble, too."
    me "Your parents came to see you yesterday, didn't they?"
    show us sad sport with dspr
    us "They're strict."
    "Ulyana sighed."
    us "They think that since the unit is supposed to have so many kilocalories, then they shouldn't break the regime."
    me "The unit?"
    show us smile sport with dspr
    us "Uh-huh. Grandpa's an officer, Dad's an officer."
    us "Mom might be happy to bring some goodies, but she's strictly forbidden."
    me "What did they bring you, then?"
    show us shy sport with dspr
    us "Volleyball."
    "Ulyana was embarrassed."
    us "And I begged Tisha for some sweets; she doesn't eat them anyway."
    us "And so... Little things."
    me "I have a fishing line and a sinker."
    show us angry sport with dspr
    us "Oh, yes."
    "Ulyana put out her thumb."
    us "I'm quite the fishmonger."
    us "And I don't think you're any better."
    me "I don't know."
    "I answered honestly."
    me "I haven't tried to fish here yet, maybe someone will bite."
    show us surp1 sport with dspr
    us "Are you serious?"
    "She pressed her palms to her cheeks and began to stare at me with exaggerated interest."
    me "What's wrong?"
    us "Nothing is wrong!"
    show us smile sport with dspr
    us "Only a man like you would suggest that we go fishing..."
    "Here she lost her mind and looked at me demandingly."
    me "What?"
    if alt_day4_me_neu_date == 'us':
        us "Attic, where you hung hang my snake!"
        me "Bad idea."
        "I shook my head."
        me "First of all, stealing isn't very pretty per say."
        show us normal sport with dspr
        us "It's not stealing, it's humanitarian aid!"
        us "I'm a growing organism, if I die of hunger, you'll know."
        me "And secondly..."
        "I continued as if she hadn't interrupted me."
        me "You won't eat dried fish, you'll just get a stomach ache."
        me "Or do you want to eat your snake?"
        show us dontlike sport with dspr
        "Judging by the slightly green face, that wasn't an option the girl had considered."
        me "So forget it."
        me "And if you don't care about morality at all, you'd better rob your squadmates: someone must have had something to eat."
        show us fear sport with dspr
        us "You what! You can't! Take from your own!"
        "The girl looked at me in utter horror."
        "Though I suppose one more day of this hunger strike and even that could be negotiated."
        "Moral standards are shaky, they only work if you're fed, your feet are warm and your nose is full of tobacco."
    else:
        us "Are you sure you'll be able to catch anything?"
        me "How would I know? I've never fished here."
        me "What if there aren't any fish here?"
        us "You've got to think of something! You have to."
        me "Why should I?"
        us "Because you're a man!"
        me "Yeah. So?"
        show us sad sport with dspr
        us "Not 'so'! A breadwinner! You have to feed a weak woman."
        me "Not a bad start."
        "I appreciated."
        me "What's next? Are you going to sit down and dangle your feet?"
        show us surp1 sport with dspr
        us "I won't dingle. Oh, I mean, I won't dangle... Oh, screw you!"
        us "Anyway, your job is to feed me."
        me "Right. I'm on my way."
        "This consumerism kind of pissed me off, but I decided to make allowances for my age."
        th "And the fact that she's a {i}woman{/i}, yeah."
        show us cry sport with dspr
        us "But I want to eaaaaaat."
        "The girl got upset."
        me "Eh. Me too."
    stop music fadeout 5
    "The mood was slowly slipping into the very real minuses."
    play music music_7dl["temptation"] fadein 3
    "If only five minutes ago I was ready to believe that everything would work itself out,"
    show us sad sport with dspr
    extend " right now I believed that less and less."
    "The prospect of going to bed hungry was in full swing."
    "And it didn't scare me at all - the experience of going to bed on an empty stomach had been a full-blown one in my life."
    "What I wouldn't have wanted was for the little one to have that kind of experience."
    show dn normal pioneer at zenterleft
    show us normal sport at left
    with move
    dn "Hungry?"
    us "Hungry."
    show dn grin pioneer with dspr
    dn "I know."
    "Danya got excited."
    dn "That's why I left early. Alka, Tonik!"
    show al normal pioneer at right
    show tn smile pioneer
    with dissolve
    "The boys standing off to the side also came over and, turning out their pockets, managed to pick up as many as four baked potatoes."
    tn "Not God knows what, of course. But it's something."
    me "Thank you for that!"
    "I thanked them when I realized that the boys wouldn't get a kind word from Ulyanka."
    "Women's gratitude in all its glory!"
    show dn normal pioneer with dspr
    dn "Here's the salt."
    "Danya held out a matchbox."
    dn "I can't help you with anything else, I'm sorry. In the canteen said they'd make sure no one threw food around."
    me "Where'd you get the other one?"
    show dn smile pioneer with dspr
    dn "Katushka."
    "Smiled the boy."
    dn "She said she wouldn't, and I'm skin and bones."
    dn "So eat up, and see you tomorrow!"
    hide dn with dissolve
    "He waved to us and disappeared into the darkness."
    hide tn
    hide al
    with dissolve
    "Following him, with nods of goodbye, the other two boys disappeared."
    "And Ulyana, looking thoughtfully after them, shook and shook her head."
    "But her thoughtfulness did not prevent her from consuming her treats."
    "So much so that I only got one potato."
    show us normal sport at center with move
    us "You know what occurred to me, Syomich?"
    "She shared as the crackling behind my ears began to subside."
    me "That we had a good time, and it's time to sleep?"
    show us smile sport with dspr
    us "I'm not full! In fact, I've been hungry since breakfast."
    me "Still insisting on going fishing?"
    show us grin sport with dspr
    us "No."
    play music music_7dl["runaway"] fadein 3
    "Slowly she began."
    us "I suggest we go and get in the dining room."
    me "That's a fresh idea."
    "I responded skeptically."
    me "And the best part is, it's so working."
    show us smile sport with dspr
    us "Get lost, you nerd! It can't get any worse than our current punishment!"
    if alt_day_binder != 1:
        "I found that hard to agree with."
        "On the other hand, she and Alisa have been trying to pull off the same feat for no more than four days."
        "They didn't succeed, of course."
        "But they didn't get anything for it either!"
        "So..."
    us "There must have been something left over! So let's go."
    me "You know, there's a suspicion that it definitely can get worse."
    show us surp2 sport with dspr
    us "So what? Are they going to shoot us?"
    us "Or will they put us on duty again?"
    show us surp3 sport with dspr
    us "I'll even settle for that now. Let's go! We'll be quiet and quick."
    us "One and done!"
    "It sounded like she was talking me into some kind of mischief, and not at all into innocent entry into a locked room."
    "And I break down like a virgin on the first date."
    me "And the risk?"
    us "Risk is a noble thing, and you always want to eat! Don't slow down, Syomich!"
    us "Soon ours will go back, there's no time! Get up!"
    "She jumped off the bench and grabbed my hand and pulled me along."
    play music music_list["eat_some_trouble"] fadein 3
    me "No. That's a bad idea."
    show us angry sport with dspr
    us "Look, if you..."
    me "You don't understand!"
    "I interrupted."
    me "We can't just get in there!"
    show us dontlike sport with dspr
    us "And who's going to stop us?"
    me "Crooked hands?"
    show us surp1 sport with dspr
    us "Uh… What?"
    me "What I said."
    "I mocked her."
    me "You see, there's no one in our touching couple who has the talents of a professional thief."
    "I could have picked some lock, not a very difficult one, but she had no reason to know about it."
    me "You, for instance, can you open a lock with a paper clip?"
    us "It's easy! I saw it in a movie!"
    show us surp2 sport with dspr
    me "There's all kinds of crap in the movies!" with vpunch
    "I barked."
    me "Only a kid like you would believe a stupid movie story!"
    us "Hey, I'm an adult!"
    me "Very mature."
    "I brushed it off."
    me "Listen to my command!"
    me "Turn around, and to my house, march!"
    show us smile sport with dspr
    us "Do you think there are keys to the canteen."
    me "I think if there are any, it's in there."
    us "Why?"
    me "Because Slavya."
    "Started to curl my fingers."
    me "She has keys to everything in camp, including other people's suitcases."
    us "What?"
    me "A joke of humor. Anyway, she sure didn't drag them with her into the woods."
    me "And she wouldn't leave a treasure like that in her cabin - not her style."
    if alt_day1_sl_keys_took in (1, 3):
        "I purposely didn't mention that I still have something useful lying around in my stuff from day one."
    show us laugh sport with dspr
    us "Can you make it simpler for dumb people?"
    me "Simpler? Run to the cabin!"
    stop ambience fadeout 3
    return

label alt_day5_me_neu_us_robbery:
    scene bg ext_house_of_mt_sunset with dissolve
    "As we ran, it got darker and darker around us."
    "And the stomachs were clinging tighter and tighter to my spine."
    "Ulyana was right about starving to death."
    "Otherwise, hell, I'd be leading our resistance headquarters."
    play sound sfx_open_dooor_campus_2
    $ alt_pause(1)
    play ambience ambience_int_cabin_night fadein 2
    scene bg int_house_of_mt_night2
    with dissolve
    if alt_day1_sl_keys_took in (1, 3):
        "I left Ulyana outside so she wouldn't peek."
        "And I headed straight for the nightstand, where, next to the backpack my parents had sent me, there were..."
        me "Bingo!"
    else:
        "Leaving Ulyanka standing guard, I made my way resolutely to the leader's quarters."
        "No keys were seen on the shelves and table."
        "Nor next to the bed."
        "There were only two places left to look - the private nightstand and the squad leader's private locker."
        "I glanced at Ulyana peering out from behind the door-she nodded encouragingly."
        th "If the leader finds out I've been going through her personal things..."
        dreamgirl "Sekir-bashka-carachoon! Hello and die!"
        th "Oh, thanks, that cheered me up!"
    play sound sfx_keys_rattle
    $ alt_pause(1)
    "With a satisfied nod, I shoved the bundle into my pocket."
    play sound sfx_click_1
    $ alt_pause(1)
    scene bg int_house_of_mt_night2 with fade
    "And with a flick of a switch, went outside."
    play sound sfx_open_dooor_campus_2
    $ alt_pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    scene bg ext_house_of_mt_night_without_light
    with dissolve
    play ambience ambience_camp_center_night fadein 3
    us "Well?"
    "A voice from the lounger asked."
    us "Any good news?"
    "While I was looking for my keys, it got really dark, so I only had to rely on the voice and the flashlight, which I never gave back to the squad leader."
    me "Ta-da!"
    "I threw up the bundle:"
    me "Let's go! On to the conquest of the canteen!"
    "Ulyana giggled and, jumping out of her chair, set off at a brisk pace in the direction indicated."
    stop music fadeout 3
    "I headed after her."
    play music music_list["glimmering_coals"] fadein 5
    "And the further on, the more nervousness was in the girl's gait."
    "She was well aware that it was at least illegal what we were doing."
    "But was she afraid of the squad leader?"
    "The glorification at the lineup?"
    "Characterization?"
    "It didn't seem so to me."
    "A far more plausible guess to me was that she was very much afraid that her folks would find out what she was doing here."
    "Afraid, but she keeps doing it anyway!"
    dreamgirl "Probably just going off the rails, you know?"
    "I nodded, picking up the pace myself so I wouldn't lose sight of the little one."
    dreamgirl "All year long she's smart and beautiful and a good girl, but she's gassy inside!"
    dreamgirl "And now, all she has to do is feel a little slack in the hand clutching the reins, get a little out of control, and voila!"
    th "But then how could they have become friends with Dvachevskaya?"
    "The question was a reasonable one - of all the people I recognized in that camp, Aliska looked the least like someone capable of pretending and fitting in."
    dreamgirl "So it makes sense: most likely they were introduced and befriended by the same Olenka."
    th "Of course, I'm not belittling her pedagogical merits, but making friends?"
    dreamgirl "What's wrong with that?"
    dreamgirl "They have something in common."
    th "Love of bullying your neighbor?"
    dreamgirl "That too."
    dreamgirl "But I'm more about their reluctance to pry into someone's soul - and let someone in as well."
    dreamgirl "And you can do mischief just fine without having to have a grueling conversation."
    scene bg ext_dining_hall_away_night
    with fade
    us "Get a move on, Syomych!"
    "Shouted Ulyana, turning onto the path to the canteen."
    us "We have a lot to do and no time at all."
    us "So schneller! Schneller!"
    scene bg ext_dining_hall_near_night at zenterright
    show us normal sport at zenterleft
    with dissolve
    "A moment and she leaped onto the porch and stomped impatiently there in anticipation."
    us "Run, run!"
    "She hurried me up."
    "Finally, I climbed up on the porch, went to the door, and taking a bundle out of my pocket, began to pick up the necessary key."
    play sound sfx_keys_rattle
    "A couple of minutes under flashlight light - there were plenty of keys, and most of them resembled each other like twin siblings."
    "But patience and work, as they say..."
    play sound sfx_open_door_strong
    scene bg int_dining_hall_night
    with dissolve
    play ambience ambience_int_cabin_night fadein 3
    "I didn't have time to take a couple of steps before Ulyana slipped through the door ahead of me."
    show us laugh2 sport with dissolve
    us "Hooray-hooray-hooray! And now for the food!"
    "I hurried after her, but I forgot one minor factor."
    stop music fadeout 3
    "Or rather, it used to be insignificant, but lately it's been playing more and more strongly."
    "I'm talking about luck and karma, if anything."
    scene
    $ renpy.show("bg int_potato_storage_7dl", what = Notch("bg int_potato_storage_7dl"))
    with dissolve
    play music music_7dl["genki"] fadein 3
    "There was nothing in the food room itself, the stoves were out, the boilers were washed and, upside down, standing on the stoves, preparing for tomorrow."
    "So I decided to pay a visit to the bakery compartment to see if there were any orphaned humpbacks and whatnot."
    "And it just so happened that the way there was past the sink."
    with fade
    "After taking a few steps on the wet floor, I was convinced that I could walk here, as long as I was careful and didn't..."
    us "Stand aside! Bread, I'm coming!"
    "A red meteor rushed past me, squeezed under my elbow."
    "And the push didn't seem to be very strong."
    "But, as it turns out, I don't need much on this floor."
    "I don't know who mopped the floor like that, or I'd be sure to express my gratitude to him... manually when I met him."
    "But somehow, feeling like the elephant in the china shop, I turned around, trying in vain to get a grip on the air and stay on my feet."
    "In vain."
    "The only thing I could get my hands on was a frame shelf on which the plates were drying."
    "And, of course, that shelf was not at all meant for pioneers to hang on."
    play sound sfx_7dl["plates_broken"] fadein 1
    "Ta-ra-ram!"
    "On the slippery tiled floor came a jumble of me, spoons, and plates."
    "The latter, of course, in pieces."
    dreamgirl "Lights out, dry the oars."
    us "Hey, hey!"
    "In sight above me appeared the familiar shorts and scarlet t-shirt."
    us "Are you alive, Syomich?"
    th "I wish I were dead."
    "I sluggishly stated, climbing out of the shrapnel."
    "And only straightening to my full height, I jabbed an accusing finger at the embarrassed girl."
    me "You!"
    us "Well, me, so what?"
    show us sad sport with dissolve
    me "Listen here, you walking calamity..."
    us "Yes?"
    "Innocently the monster fluttered her eyelashes."
    me "Did you at least get some food?"
    me "If we're going to get killed anyway, at least let's not get killed in vain!"
    show us shy sport with dspr
    us "Just a little bit."
    us "Cheese, sausage, cookies, a couple of buns. Not enough."
    us "We should look in the bread store."
    me "We should."
    "I agreed."
    "It wasn't worth the fare for the cracked crockery."
    "And just as I was about to offer to split it all up and eat it already, I heard a surprised voice from the entrance:"
    sl "Oh, guys, what are you doing here?"
    "And trouble showed up."
    play music music_list["doomed_to_be_defeated"] fadein 3
    show us surp1 sport at right
    show sl surprise pioneer far at zenterleft
    with dissolve
    sl "Why did you sneak into the canteen without asking?!"
    "The activist exclaimed."
    "Unlike Ulyana, who immediately rushed to prove something and explain, I stood tiredly and watched them argue."
    "That's it. I no longer have the strength to argue or make excuses."
    "Eat. And sleep. In any order you want."
    show us normal sport with dissolve
    us "I bet you're full and satisfied, aren't you! And we should starve?!"
    show sl serious pioneer with dspr
    sl "That's no reason to break into the canteen, much less break plates!"
    sl "You could have just apologized!"
    sl "Wait till Olga Dmitrievna finds out."
    mt "I already did."
    "I got a frosty terror between my shoulder blades at the sound of that voice."
    show mt angry pioneer far at zenterleft behind sl
    show sl normal pioneer at center
    show us fear sport at right
    with move
    "As usual, the squad leader came up quietly from behind."
    "Yeah, trouble never comes alone."
    mt "Do you want to explain yourself?"
    "She asked in a murderously even tone."
    show mt angry pioneer at left with move
    mt "Persunov? Sidorova?"
    "Shit. I haven't been scolded like that since high school."
    mt "Okay, you'll clean up the splinters now, that's out of the question. But with what are you going to feed the pioneers tomorrow?"
    mt "Palms?"
    show us surp3 sport with dspr
    us "But I didn't do it on purpose!"
    "Pouted Ulyana."
    "I didn't say anything."
    "I had nothing to say. And nothing to pay with for the purchase of new plates either."
    mt "Right!"
    "The squad leader, shaking her head, looked at me with pity:"
    mt "Tell me, Semyon - how am I supposed to trust you now?"
    mt "Can't you be trusted with anything at all?"
    "I kept sullenly silent."
    show us surp2 sport with dspr
    us "Oldmitryevna, don't scold him alone. It's us together."
    show mt rage pioneer at left with move
    mt "I'll figure out who to scold and how to scold, okay?"
    "The leader barked so that Ulyana jumped on the spot."
    show us dontlike sport with dspr
    us "But…"
    show mt angry pioneer with dspr
    mt "You have separate demand, since you're just a kid! Why do you think you get away with so much?"
    mt "But Semyon... I thought you were a mature and responsible man."
    mt "Look at how you defended her before the fire. I guess you were wasting your breath."
    show mt sad pioneer with dspr
    "She sighed."
    show us sad sport with dspr
    "Ulyana stepped back to me and grabbed my hand."
    us "Scold us together! And we'll answer together, too."
    show mt angry pioneer with dspr
    mt "Sidorova, is there something you don't understand? Everyone will get their scolding, don't worry."
    "Olga Dmitrievna noticed a certain object glittering on the floor."
    mt "Slavya, pick up the keys and give Persunov everything he needs for cleaning."
    if alt_day1_sl_keys_took in (1, 3):
        "Slavya measured us with a suspicious look, obviously acknowledging her bundle, but said nothing."
    "The leader turned to Ulyana."
    mt "And with you, Sidorova, there will be a separate conversation."
    hide mt
    hide us
    with dissolve
    stop music fadeout 5
    show sl normal pioneer at center with dissolve
    sl "The floor probably won't need rewashing."
    "Slavya said thoughtfully as we walked away from the scolding leader."
    sl "Come on, I'll give you a broom and a dustpan."
    play sound sfx_open_door_clubs_2
    $ alt_pause(1)
    return

label alt_day5_me_neu_us_cleaning:
    play music music_7dl["thousand_little_things"] fadein 3
    scene
    $ renpy.show("bg int_potato_storage_7dl", what = Notch("bg int_potato_storage_7dl"))
    with dissolve
    "She took me to a nook where there were brooms, scoops, and several tin buckets with wire handles."
    show sl smile pioneer with dissolve
    sl "You know, I'm used to the fact that Ulyana and Alisa are always coming up with some tricks."
    sl "But you... You look so serious, so grown-up."
    me "Laugh, laugh."
    "I grumbled."
    sl "I wouldn't dream of it."
    sl "Anyway, look, you put the big pieces in a bucket with your hands, then you put them in a jar in the backyard so no one gets clipped."
    sl "And the smaller ones, you pick up with a mop. But just be careful not to get anything stuck between the tiles. Can you do that?"
    me "Thank you. I'll try."
    scene bg int_dining_hall_night with dissolve
    "Having properly equipped myself, I went back to Ulyana."
    show us sad sport with dissolve
    "She sat alone, and her face was thoughtful."
    me "Did you get scolded?"
    show us dontlike sport with dspr
    "Ulyana reluctantly nodded."
    "I don't know what the squad leader's words were, but they got our catastrophe down."
    me "What are you sad about? Getting kicked out of camp?"
    show us surp3 sport with dspr
    us "Spit on it, you dumbass!"
    "Ulyanka tapped superstitiously on the bench she was sitting on."
    me "Then what?"
    th "You're like those Manhattan girls, you can't be beaten with a shovel."
    show us sad sport with dspr
    us "What difference does it make?"
    "Great. Very frank and trustworthy."
    me "If you don't want to talk, fine."
    "I shrugged, squatted down and started picking up the biggest shards of plates in a bucket."
    scene bg int_dining_hall_night
    with fade
    "Ulyana grunted for a minute more, thinking..."
    "And then she joined me."
    "What touching solidarity."
    show us sad sport with dspr
    us "Oldmitrievna promised to tell my parents everything, if there's a problem with me tomorrow."
    me "So?"
    show us dontlike sport with dspr
    us "And she has a whole list of all my 'sins,' as she said."
    "She sighed."
    me "Not vindictive, then? Doesn't remember evil, but she writes it down?"
    "Ulyana smiled unhappily."
    show us sad sport with dspr
    us "And I can't promise anything! I'll have to run away again tomorrow."
    us "Woohoo."
    hide us
    with fade
    "After picking up the bucket of splinters, Ulyana went outside."
    th "Looks like this isn't her first incident with the plates, is it?"
    "Experience is the son of mistakes, yes..."
    th "She even knows what to do and how to do it, it's so familiar, so ordinary..."
    "I, on the other hand, left alone, worked with the mop, sweeping away the tiny things in the dustpan."
    "I had a lot to think about."
    with fade
    "But not for long."
    "I expected that Ulyanka, like any other child, would avoid physical labor in every way possible and go outside with a bucket for at least half an hour."
    "But I had already forgotten that Ulyanka was no ordinary child."
    "Far from ordinary."
    show us shy2 sport with dissolve
    us "I'm done."
    "I nodded."
    us "Want me to help you clean up?"
    "Thank you. I'm just finishing up."
    me "Do you often have to be on canteen duty?"
    show us normal sport with dspr
    us "It depends. But once a week for sure."
    "Calmly, as if resigned to the inevitable, the girl replied."
    me "Have you ever tried just being nice?"
    show us shy2 sport with dspr
    us "Have you ever tried standing only on your left foot and breathing only with your belly?"
    me "Uh... What?"
    "This is where I got a little lost in her line of reasoning."
    show us surp3 sport with dspr
    us "No, you haven't tried it? You should definitely try it."
    "She winked."
    me "Why?"
    show us grin sport with dspr
    us "You won't know unless you try it."
    "I obeyed and stood obediently on my left leg for a full minute, breathing with my belly."
    "All the while Ulyanka was sweeping up the remains of the splinters."
    "I felt like an idiot."
    me "So?"
    "I asked after a minute."
    me "I stood, I breathed."
    us "Can you live like that all the time?"
    "She asked curiously."
    "After thinking about it, I shook my head."
    me "No. It bothers me. Constantly thinking about how to stand, how to breathe."
    show us smile sport with dspr
    us "Yup-yup. Same with me! I can't {b}act{/b} nice. I'm not a senberrarn!"
    me "Saint Bernard."
    us "What difference does it make?"
    me "You said..."
    "I waved my hand."
    show us normal sport with dspr
    "By this point, all traces of the disaster had been successfully swept away, and Slavya showed up at the door."
    show sl normal pioneer far at left behind us
    sl "Finished? Good."
    sl "I'm just on my way to close the gate, so I'll close up here, too."
    "And I asked with incomprehensible irritation:"
    me "Slavya, doesn't it annoy you...?"
    sl "What?"
    me "Being so right?"
    sl "Well..."
    "Slavya wondered."
    sl "Have you ever tried to breathe only with your stomach..."
    show us grin sport with dspr
    hide us with easeoutleft
    "I looked at the little one, but she held her tongue and slipped out of the room."
    me "I didn't. I'm going to bed, sweet dreams."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day5_me_neu_us_sleeptime:
    play music music_list["a_promise_from_distant_days_v2"] fadein 2
    play ambience ambience_camp_center_night fadein 1
    if alt_day5_me_neu_us_stores:
        scene bg ext_house_of_dv_night with dissolve
        "When I reached the redhead's lair, I could not feel my legs under me from fatigue."
        "My arms were aching from the weight, my back was aching."
        "But I stoically endured and did not allow myself to disturb the girl's sleep in any way."
        play sound sfx_open_door_1
        $ alt_pause(1)
        scene bg int_house_of_dv_night with dissolve
        me "I wonder if my forehead says 'ride here'?"
        "I grumbled, extremely gently unloading the sleeping Ulyanka onto her bed."
        me "Why is everyone taking advantage of me like this?"
        "Not the kind of interlocutor from whom I could find answers to such questions."
        "So I covered Ulyana with the covers, tucked the corner, and tiptoed out the door."
        "My crib and, no doubt, the sweetest dreams awaited me."
    else:
        scene bg ext_house_of_mt_night_without_light with fade
        "Yeaaaah..."
        "Today was... It was something else."
        "Maybe I should have acted differently?"
        "Or at least consider the consequences of my own actions a little bit?"
        "But that's the thing, isn't it, that surprising is what makes life really interesting!"
        "Is that what would happen if I thought of something to feed Ulyana?"
        "Everything would have been within the norm."
        "We would have gone for a walk around camp, done some pranks-anything."
        "No, instead we broke into the mess hall and cracked a couple dozen plates, which we cleaned up before lights out."
        "Good for us?"
        "You bet."
    scene bg ext_house_of_mt_night_without_light with fade
    me "How tired I am."
    "I muttered, not hitting the keyhole with my key."
    me "And how damn happy I am."
    play sound sfx_open_dooor_campus_1
    $ alt_pause(1)
    scene bg int_house_of_mt_night2 with fade
    play ambience ambience_int_cabin_night fadein 1
    "Finally, the unruly door gave way, and I, rubbing my eyes and yawning momentarily, wandered to the bed, throwing off my clothes right onto the floor."
    me "And now..."
    scene cg d1_end_of_day_7dl with dissolve
    "The events of the day were unfolding before my eyes, fast, fast, like a rewind."
    "Or like that very movie that Tonik showed."
    "I wish I could do that."
    "Or at least dream the dreams I want to dream."
    stop music fadeout 5
    stop ambience fadeout 3
    return

label alt_day5_me_neu_mi_estrade:
    scene bg ext_dining_hall_near_day with dissolve2
    play ambience ambience_camp_center_day fadein 3
    play music music_list["reminiscences"] fadein 3
    "Three things you can't think of worse - waiting, hoping, and catching up."
    "I can't say Miku's request piqued my curiosity all that much, but after all, it could be called some sort of impromptu date, couldn't it?"
    "You could, couldn't you?"
    "Dreams of people, of their tiny happiness pouring from the sky and washing away the caked crust of alienation and indifference from their faces."
    "Of course, I couldn't say I had any serious feelings for Miku, but..."
    "Maybe it was just that I never took the word 'like' seriously enough, and I never had any trouble telling a person I liked that."
    "I {i}liked{/i} Miku — although I was tempted to write it all off to her artistic charisma and say that it's her professional thing to like it."
    "In reality... Nope."
    "It's not about the smile at all."
    "And it's not about being able to hold yourself."
    "Behind the impenetrable armor of positivity and openness to the world, I unmistakably saw in her a reflection of myself - rebellious and desperately seeking escape from loneliness."
    "And so I continued to sit and wait for her on the bench, even though no one was holding my hands or handcuffing me to the radiator."
    "Because Miku was interesting."
    show mi normal pioneer with dissolve
    mi "Oh, Senechka, did I take too long?"
    "I shook my head."
    mi "I'm sorry, please, I got held up in the canteen, it turns out it's my and Lena's shift today, and I didn't know, so forgetful of me!"
    "She held out her narrow palm to me:"
    mi "Are we going?"
    "I nodded."
    scene bg ext_stage_big_day_7dl
    with blinds_l
    $ alt_pause(1)
    if (counter_un_fz_mt_transit != 3) and (not alt_day4_me_neu_volley):
        "Nothing has changed here since yesterday."
    me "So why are we here?"
    if alt_day4_me_neu_mi_songs:
        me "Or are you going to pick up a tune on the piano?"
    show mi normal pioneer at zenterleft
    mi "You see, Senechka, yesterday there was a concert, and after it the stage was left - you see how it is."
    mi "So..."
    if alt_day4_me_neu_mi_songs:
        mi "Wait, please, I'm going to make a quick run, I have a mop in the back room, and then we'll get the right equipment - I need it for rehearsals - and we'll go, okay?"
        "She's started picking up her talking pace again."
        me "No way."
        "I really like work."
        "I could watch someone work for hours."
        "But now for some reason I couldn't bring myself to sit and watch Miku swing a mop alone."
        "And that's not to mention the wet benches!"
        me "Do you have a second mop there?"
        show mi smile pioneer with dspr
        mi "But you don't have to, I just wanted to do everything at once, and you would have waited just a bit longer!"
        "Miku's pace of speech doubled from embarrassment."
        "So I just put my palm on the top of her head and put my finger to my lips in an eternal gesture of «shush»."
    "She went to the back room, from where a few minutes later she pulled out a couple of rough implements like a 'mop' and a scoop that looked more like a sharp weapon."
    if (counter_un_fz_mt_transit != 3) and (not alt_day4_me_neu_volley):
        "About the same thing Ulyanka hunted me with yesterday after exchanging ice cream."
    show mi normal pioneer with dspr
    mi "Well, shall we begin?"
    show mt normal pioneer at cright with moveinright
    mt "We'll have to start a little later."
    "Notified the silently approaching leader."
    "I'll be a creep - she's practicing that step! {w} And Slavya has caught it from her, too!"
    show mi shy pioneer with dspr
    mi "What do you mean?"
    mt "A little change in plans."
    "Words of joy to the heart of any outsourced professional! And the higher the completion rate, the greater the joy."
    "Fortunately, I haven't even started yet, so I reacted completely calmly:"
    me "And what's that?"
    show mt smile pioneer with dspr
    mt "Oh, don't worry, I won't make you carry anything heavy."
    mt "I need a helper on the beach while it's quiet hour, I need to get the place cleaned up after the rain."
    me "What about Slavya?"
    "Makes perfect sense."
    mt "Slavya's got the square and the administration building, there's already something for her to do."
    me "What about Miku?"
    mt "She'll somehow manage on her own. Are you coming?"
    "Impatiently she asked."
    me "Uh..."
    "On the one hand, I {b}could really{b} tell the leader to screw off, and I wouldn't get anything for it - because Miku really can't do it alone."
    dreamgirl "On the other hand, the opportunity on the beach, not a dirty stage."
    $ volume (0.5,'music')
    $ volume (0.5,'ambience')
    menu:
        "Leave with Olga":
            $ volume (0.9,'music')
            $ volume (0.9,'ambience')
            $ counter_mt_7dl += 1
            $ alt_day5_me_neu_mt_voyeur = 1
            "The sun finally warmed up, forcing me to decide in favor of working in the cold."
            me "Miku, I'm sorry, but since the leader says..."
            show mt normal pioneer with dspr
            mi "It's all right, Senechka, I understand when it's needed."
            "Waved the girl off, putting the second mop against the wall."
            mi "You go ahead, it'll just take a little longer, but I'll get through it, I always do!"
            "Feeling a prick of conscience, I turned around and hurried off after the squad leader."
            stop ambience fadeout 3
        "Stay and help Miku":
            $ volume (0.9,'music')
            $ volume (0.9,'ambience')
            me "Excuse me, Olga Dmitrievna."
            "Penitently I looked."
            me "But it looks like Miku really won't manage her alone."
            me "Perhaps if you had sent me a replacement..."
            show mt normal pioneer with dspr
            mt "Well."
            "Olga somehow gave up right away without even trying to change my mind."
            "It was as if the question had been asked purely for the sake of ticking a box."
            "And so the box is checked, the recipient has given up, we're winding down, moving on to a new place."
            mt "I think I'm going to get Dvachevskaya involved."
            "Mumbled Olga to herself as she walked away."
            mt "She seemed eager."
            hide mt with dissolve
            me "Dvachevskaya?!"
            "I couldn't believe my ears."
            show mi smile pioneer with dspr
            mi "You shouldn't! {w}Alisochka is very good at getting along with children, they listen to her for some reason."
            me "What do children have to do with it? I was asked to clean the beach."
            show mi laugh pioneer with dspr
            mi "And you believed that? {w} Funny Senechka, didn't even see that she had a swimsuit under her shirt."
            mi "She went to bathe the kids and was hoping you'd keep her company."
            me "She wasn't really hoping."
            show mi normal pioneer with dspr
            mi "Well... I don't know what happened there that you're so shy with each other, but it was definitely an invitation to swim, not to pick up stumps on the beach."
            show mi grin pioneer with dissolve
            "Miku put her paws to her cheek in feigned amazement at my understatement."
            mi "You're getting attention, Senechka! It's obvious!"
            "And I brushed it off."
            "Whatever. As if I need any more headaches."
            me "So what's with our front of work?"
            "I asked."
            show mi normal pioneer with dspr
            mi "Now, now..."
            "Taking some kind of list out of her pocket, she studied it for a while, then poked her finger into the far corner of the stage, where something incomprehensible was sunning itself between the piano and the table under a gray cover."
            mi "The xylophone, it turns out, was here. Good, we won't have to carry it, so we'll mark it off!"
            show mi shy pioneer with dspr
            "She looked at me confused."
            mi "I think we really only came here to sweep up."
            "She pulled her head into her shoulders so guiltily that I just laughed and waved:"
            me "Let's go! We'll start early, we'll finish early."
            hide mi with fade2
    stop music fadeout 3
    return

label alt_day5_me_neu_mt_beach:
    $ alt_day2_beach_seen = True
    scene bg ext_beach_day with dissolve
    play ambience ambience_lake_shore_day fadein 3
    "The camp squad leader is like a screaming non-human from the other side of the abyss who has no right to personal happiness or free time."
    "She's good at it."
    "But who says she likes it?"
    "It was just the two of us on the beach-the pioneers had a quiet hour and preparations for tomorrow's gala."
    play music music_7dl["wheres_wonderland"] fadein 3
    "Who says that a person who goes to work with the younger generation is limited to that?"
    "And if you think about it a little bit, get your head involved - words, innuendos, 'Just a squad leader, huh?' and a bitter chuckle on her tired lips."
    "Basically, Olga has no one to say a word to, she's all like Danko, has no right, shouldn't and can't, and basically just like that - cramming in with Viola and Sanich under wine and cards until four in the morning, when everything inside is already completely charred."
    "And again, foolishly, as always belatedly, to realize that any man his strongest pain is silent, that Olga is also a girl, and she does not want to force the pioneers, but twenty-five kilos under her belt, seven cubic kilometers of solitude and a bonfire until morning..."
    "To have a worthless horizon and no one's songs - but the sleeping bag is warm, and you recover more in a night than you did the whole summer before, because there's someone around who feels you're an extension of yourself."
    "But today is different. {w}Today I'm ready to drown myself in happiness just by being near you - it's hard to separate my own emotions from Olga's tenderness."
    th "Hello... They say you have no loved ones at all."
    th "Like hell I'll ever say it out loud."
    th "But don't be sad, please!"
    "As if sensing my gaze, she winked."
    show mt smile pioneer with dissolve
    mt "Well, did you get away with it, you bum?"
    me "But you took me away!"
    mt "Well..."
    "Pouted the girl."
    mt "You could well have refused and said Miku couldn't handle it, and it was your duty as a pioneer..."
    show mt laugh pioneer with dspr
    "That's when she couldn't stand it and laughed."
    mt "You should have seen your face, Sem Syomich. {w}Sometimes I think you have no sense of humor at all."
    mt "Okay, I'm going for a swim."
    "And with a turn of events pulled the knot of her tie:"
    mt "Are you coming? {w}Or will you guard my things?"
    me "But..."
    show mt smile pioneer with dissolve
    mt "That's what I thought. {w}Shouldn't even have asked - you always say no."
    "The shirt settled to the sand with a quiet rustle, beautiful, slender legs stepped over the fallen skirt..."
    show mt normal swim2 with dissolve
    mt "Somehow you're always so embarrassed to swim with me."
    "She was wearing a swimsuit that was so tight around her body that if she'd been naked, I don't think I could have seen more."
    dreamgirl "She's got quite a diet! Balanced! Look at the shape she's got."
    "Approvingly the voice quipped."
    "And threw at me the image of Olga in a swimsuit - and then without."
    mt "You must be afraid I'll eat you!"
    show mt laugh swim2 with dspr
    mt "All right, my humble one, guard the stuff, maybe you'll think about it some more."
    hide mt with dissolve
    "She waved to me and ran off to the pontoons."
    if alt_day4_me_neu_mt_diary:
        "As to an old acquaintance."
        "Which, according to her diary, I was."
        th "What am I supposed to do with that?"
        dreamgirl "Nothing. Look, watch the pretty girl."
        dreamgirl "Look how she runs. {w}Fast..."
    else:
        "I suddenly remembered that she was rumored to be here more than once."
        "That perhaps she is an old-timer, and knows all the plots with huts in the trees better than the local pioneers."
        "Looking at the way she was running along the now dried up planks of the swimming hole, the way she habitually put her foot down and didn't look around, I was inclined to believe those rumors."
    "Faster and faster and faster..."
    "Somehow strange - right in her path was just the edge of a pontoon with a tubular fence painted green."
    th "It's not like she's going to..."
    "I didn't have time to think it through."
    "The hitherto unnoticed gray box, modestly nestled in a corner, was the first step."
    "The top rail of the railing - the second."
    "The sky - the third."
    "An impossibly beautiful girl in a dark swimsuit took a running dive into the sky."
    th "And she loves someone, too."
    "For some reason that thought made my heart prick with a sharp needle of jealousy."
    if not alt_day4_me_neu_mt_diary:
        "As if I had any rights to her..."
        dreamgirl "You do though?"
        "But... There's this feeling from somewhere, isn't there?"
        "Like we have a story of our own - or at least with whoever our leader so diligently takes me for."
    if alt_day3_dancing2 == 'me_2':
        "Though her guessing was too much in the ten..."
    "Olga went into the water cleanly, hardly causing a splash."
    dreamgirl "She stole you from the chores and dragged you to swim and guard her things."
    dreamgirl "Don't tell me you believed the nonsense about cleaning the beach: look at it - it's sterile clean."
    "After a little swim, she lay on her back and, lazily paddling, spread her arms and legs in the shape of a 'star'."
    th "What for, then?"
    dreamgirl "The same reason why people eat together in some «Sorento», even though for the same money they could eaten their fill at home."
    th "Italian cuisine?"
    dreamgirl "Your head is Italian. {w}To spend time with you, you dumbass!"
    "I shook my head, watching the squad leader drifting lazily through the waves."
    "I wish I could believe the exhortations of my split personality. But I couldn't figure out what it was that interested me about our beautiful, lazy Olga."
    if alt_day4_me_neu_mt_diary:
        "Especially since she has a story of her own three years long that I'll be sure to finish."
        "Some important newcomer with whom I am united in the manner of arriving."
        "I froze."
        th "So she knows something?"
        $renpy.notify("this is an idiom of soviet era, the actual painting is Solovyev's «Monks»")
        dreamgirl "Repin's painting «Arrived». Nerd, it was obvious from day one."
        th "But..."
        "It was unpleasant to realize that the interest I'd mistaken for possibly romantic turned out to be strictly business."
        "Ah... To hell with it. {w}This unties my hands - conscience, nibbling me for reading other people's diaries, has been successfully strangled and dissolved in a vat of sulfuric acid."
        "And I don't have to pretend anymore and look away when I come across a particularly tempting angle."
        "It's silly to deny that she's an extremely attractive native. {w}And so all this flirtatiousness is inappropriate, to say the least."
        dreamgirl "You mean...?"
        th "Yes! I like her, so I'll stare!"
    else:
        th "Do you think she has some romantic interest in me?"
        dreamgirl "I think she has some interest. {w}But hardly romantic."
        if alt_day3_dancing2 == 'me_2':
            dreamgirl "Although she did say some silly things to you during your slow dance."
        else:
            dreamgirl "If she had - she would certainly have asked you to dance the white dance at the last disco."
            "There was logic in those words."
        th "But then what's the interest?"
        th "What could be so special about me in Olga's eyes, since she didn't hesitate to race an entire bus for me alone and abandoned her squad to her fate?"
        "I pondered, poring over and discarding options."
        "And, as luck would have it, none of them seemed credible enough to be accepted unanimously."
    "I was so deep in thought that I flinched in surprise when a wet palm shook my shoulder."
    show mt normal swim2 with dissolve
    mt "Daydreaming again, Syomich?"
    "She winked."
    me "Eh..."
    mt "Eh, eh!"
    "Olga mocked me."
    mt "Have you thought about going for a swim yet?"
    "I shook my head negatively."
    show mt laugh swim2 with dspr
    mt "I knew it."
    "She laughed."
    mt "Okay, I'm going to run and change, and then we'll take a quick run down the beach, and then it'll be noon soon. {w}How's that for a plan?"
    "Waiting for my nod, she smiled and picked up her bag from the sand beside me-I could feel its freshness on my cheek-and headed toward the cabins."
    stop music fadeout 3
    hide mt with easeoutleft
    dreamgirl "Hey, man?"
    "A second later, an inner voice inquired ingratiatingly."
    th "Huh?"
    dreamgirl "Come on... Tell me, aren't you thinking what I'm thinking?"
    th "What are you thinking about?"
    dreamgirl "That very thing, that!"
    th "I don't like that idea..."
    scene bg ext_shower_day_7dl with blinds_l
    th "I really don't like it!"
    "Tracks in the sand led to a third stall, so I had as many as three options - an abyss of variety!"
    $ volume (0.5,'music')
    $ volume (0.5,'ambience')
    menu:
        "Peep through the door":
            $ volume (0.9,'music')
            $ volume (0.9,'ambience')
            "But no sooner had I come close than I heard a muffled giggle from behind me, and I shuddered to give up the idea."
            "Ulyana, my personal demon child, who sometimes wants to be cruci-kicked. Or crucified? In short, to do something nasty."
        "Go around the back":
            $ volume (0.9,'music')
            $ volume (0.9,'ambience')
            "As I walked, the stirring in the stall stopped, and the squad leader's voice called out:"
            mt "Semyon? Where are you? Why did you leave the things?"
        "Climb into the neighbouring stall" if counter_mt_7dl >= 4:
            $ volume (0.9,'music')
            $ volume (0.9,'ambience')
            $ counter_mt_7dl += 1
            $ alt_day5_me_neu_mt_voyeur = 2
            "Any one was fine - if I knew a little bit about boy psychology."
            "I chose the first one."
            stop music fadeout 4
            "And…"
            play music music_list["eternal_longing"] fadein 2
            if persistent.hentai_graphics_7dl:
                scene cg d5_mt_redress_7dl with flash
            else:
                scene black
            "My bet was right - after a few seconds of searching, I saw a small crack in the wall separating the cubicles, and peeked through it."
            "And just in time! Just in time!"
            "Olga Dmitrievna's swimsuit was very interesting."
            "A very interesting button-up."
            "If I had known..."
            "I swallowed my saliva audibly, watching the halves creep down her shoulders, leaving a smooth border of untanned skin, lower and lower."
            "Shoulders like a swimmer's, with the collarbones clearly visible under the sheer skin, making the already beautifully shaped breasts look even more adorable."
            th "I've only seen that in movies on adult websites!"
            dreamgirl "No, well, it's silicone."
            "Unapologetically said the schizophrenia."
            dreamgirl "Look at her nipples sticking up! There's no such thing in nature."
            th "Olga doesn't even exist in nature, she's in a stall, not in nature."
            "Delightful tummy."
            "Nice hips."
            dreamgirl "Ah… Mi belle…"
            "Stepping over her swimsuit, Olga took a towel and began to wipe herself off."
            "And it was great, after all, that my peep show spot was noticeably below the level of the leader's eyes - she would have noticed!"
            "Finally, she turned around so I could see the best part, too."
            th "Where would I get the strength."
            "The excitement darkened my eyes, and all I wanted to do was climb over the wall..."
            "A little more and I risked discharging just watching the squad leader, who put her foot on the bench and wiped the inside of her thigh, going lightly on..."
            "As if mocking or feeling my gaze with her back, Olga deliberately took her time getting dressed: socks, panties, bra."
            "Finally, it came to the uniform."
            "When she finished dressing, Olga turned in my direction - I swear she couldn't see me, no way!"
            "And, stretching out, she winked seductively!"
            dreamgirl "She spotted us!"
            "And very, very slowly she began to fold her towel into her bag."
            dreamgirl "Chance!"
            "As always, communicating inside my own skull box, I tore my sutures on the fly - the eternal interlocutor's line was still in my head, and I had already turned around and popped outside."
            scene bg ext_beach_day with flash
            "Fortunately, neither my nor her belongings had gone anywhere - they were lying modestly on the sand, waiting for their owners."
    stop music fadeout 4
    show blinking
    $ alt_pause(1)
    scene
    $ renpy.show("bg ext_beach_day", what = Noon("bg ext_beach_day"))
    with flash
    "The squad leader came up a few minutes later, very satisfied with something."
    "I don't even want to think about what!"
    show mt smile pioneer at zenterleft
    with dissolve
    mt "Well, Sem Semich, since you refused to swim, let's do what we came here to do."
    if alt_day5_me_neu_mt_voyeur == 2:
        dreamgirl "And she's not too lazy to undress again!"
        th "What are you talking about?"
        dreamgirl "Didn't you come here to fornicate?"
        th "In a way."
    "I hovered a little, driving away the delightful pictures of myself and the squad leader in some way engaged, but the evil Olga mercilessly ruined all my reveries:"
    mt "Yesterday was parents' day, so all the neighborhood bushes are definitely littered with papers and wrappers."
    th "I knew nothing would just happen!"
    show mt laugh pioneer with dspr
    mt "Why so gloomy, pioneer?"
    "The leader laughed."
    mt "Don't you want to love your homeland so much?"
    th "You know, I kinda don't..."
    show mt normal pioneer with dspr
    mt "I understand. {w}That's why I don't require you to do the work for the entire duty squad."
    mt "Our business is the beach. {w}Walk around, make sure there's not much litter, and if you find it, send it you know where."
    me "Where?"
    mt "To the company - to the bushes!"
    show mt smile pioneer with dspr
    mt "And if anything: I never told you that."
    hide mt with dissolve
    "She winked and went to the far edge of the beach - to where our squads usually lived."
    "Quite logically leaving the main load to me!"
    th "Well, Olga Dmitrievna!"
    "With a sigh, the slave went off to do his duty."
    if alt_day5_me_neu_mt_voyeur == 2:
        "Although, if anyone asks me, it was totally worth it!"
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_mi_help:
    scene bg ext_stage_big_day_7dl with joff_r
    play music music_7dl["ourfirstmet"] fadein 3
    "Is half an hour of hard work with a mop and dustpan a lot or a little?"
    "On the one hand, it's no big deal."
    "On the other hand... I've never cleaned my house that well, even though my apartment was about half the size of this scene."
    "I'm pretty lazy. Like most computer hermits like me, I prefer all other leisure activities to sitting motionless for hours in front of a monitor."
    "It started out innocently enough - first 'for the glory of Kane', tiberium, harvesters..."
    "The story of a New York cop who, because of revenge, became as much a monster as the men who murdered his family."
    "Calculation of action points on the limitless Wasteland and a primed explosive in someone else's pocket."
    "Everything could have been paused, stepped away from the monitor, sat, thought, smoked, lived."
    show mi normal pioneer with dissolve
    mi "Senechka, don't sweep hard, you're tossing all the trash into my half!"
    "Miku complained."
    me "Oh, sorry."
    hide mi with dissolve
    "The monotony of work willy-nilly led to thoughts, to memories, leaving the body to perform mechanical actions."
    "Then online, MMOs, statistics, sales-clients that differed from each other only in the color and shape of their emblems."
    "Then the anonymous message boards - I've been rolling downhill for the last few years until I'm at a place where there's nowhere else to fall."
    "As a result, even the very toys I used to pray for and wait for a sequel are now not as exciting as they used to be, movie rentals, honestly stolen from torrents, often don't even launch."
    "So far, I've only managed to hang on to my last outlet."
    if loki:
        "As long as music isn't an empty shell, as long as I'm willing to listen to my favorite songs until they're in tatters, there's still hope for me."
        "And Miku is proof of that."
    else:
        "Stories. I read a lot, I write a lot."
        "And as long as I manage to feel something or convey something in my lyrics - I still have a way out of this swamp."
    "And here we have what's called 'shock rehab' - you can't go back to your bad habits for lack of opportunity."
    "Starting with cigarettes - excluding the occasional speculative urge to chug, which acts more as a trace of my old habit - and ending with Internet addiction."
    "Especially since there's an incentive to become a better person, looking at me with huge, wobbly eyes."
    "Or at least get a grip on the mop and feign enthusiasm."
    "Working side by side, we got through it pretty quickly - you could put the pioneers on right now, microphone in their teeth - and go!"
    show mi normal pioneer far with dissolve
    mi "I think that's it, Senechka!"
    "Miku echoed from somewhere on the other side of the stage."
    mi "Uh-huh. And now the best work reward ever... A new job."
    play sound sfx_open_door_clubs_2
    $ alt_pause(1)
    scene bg int_musclub_day with blinds_r
    play ambience ambience_music_club_day fadein 3
    me "Cleaning up again, right?"
    show mi smile pioneer with dspr
    if alt_day4_me_neu_mi_songs:
        mi "No, there's nothing critical here."
        "Quickly the Japanese girl smiled, checking in passing the degree of cleanliness of the window sills and the lacquered side of the piano."
        mi "You promised me something else. Remember?"
        me "Songs, huh?"
        "Miku nodded and dragged me along."
    else:
        mi "You like to walk around the house with a rag, I see."
        "Smiled the girl."
        mi "I guess when you move into your own apartment, it'll be clean and tidy all the time."
        dreamgirl "Yeah. That's exactly how it's going to be."
        show mi normal pioneer with dspr
        mi "But my point is different: Olechka Dmitrievna said this isn't the first time you've gone to camp, is it?"
        me "In a way, yes."
        "Cautiously I answered."
        me "What's the matter?"
        mi "Perhaps you know some pioneer songs? Or campfire songs with a guitar? {w}And I've been assigned as a music director, and I don't know much except what Alisa showed me."
        me "Why don't you know?"
        if ('music_club' in list_voyage_7dl):
            show mi serious pioneer with dspr
            mi "I told you before, have you forgotten? My dad is Russian, but we lived in Japan."
            mi "Although I speak good Russian, no one taught me these things."
        else:
            show mi shy pioneer with dspr
            mi "Didn't you pay attention to my appearance and name?"
            "I shrugged."
            me "I've seen Buryats and Kalmyks. And the name... even Dazdraperma sounds much more exotic."
            show mi smile pioneer with dspr
            mi "How funny!"
            "Smiled Miku."
            mi "Now, no one in the camp believes that I'm from Japan either. But I really am!"
            me "The costs of living in a multinational state, I guess."
            mi "My dad is from the Union, but we lived in Japan the whole time."
        me "So how'd you end up here?"
        show mi shy pioneer with dspr
        mi "It was dad's idea - he said I had to try to live a little the way he was used to."
        th "Feel the great Soviet sovok?{w} I guess he doesn't like his daughter!"
        "There must have been a look of pity and sympathy on my face as Miku hurried on:"
        mi "In my homeland, I am considered a hafu - a half-breed. It's not as offensive as being a gaijin - an outsider - but it's not pleasant either."
        show mi normal pioneer with dspr
        mi "In particular, no one was in any particular hurry to be friends with me or trust me. You can't blame them, tradition, after all. But..."
        "She sighed:"
        mi "And I want companionship, too. So Pa bided his time until I was fourteen and started preparing my papers."
        mi "And here I am."
        mi "Some things, of course, he taught me, I read a lot of books about the Soviet Union, watched movies and talked to my father's acquaintances, but, you know, some things can only be learned on the spot."
        mi "Like songs."
        mi "And the boys you have here..."
        "Miku smiled especially warmly, but immediately, after realizing it, she picked up her guitar:"
        mi "Well? Will you help me learn some songs for tonight's bonfire?"
        "And I smiled. I couldn't help smiling at Miku."
        "It's too bad, of course, that we didn't have a romance - and it's probably a little late to change things now."
        "But the mere fact that she exists is enough to justify my getting into this fantastic place."
        with fade2
        stop music fadeout 3
        "Because I, as has been said, have a pretty easy attitude toward expressions of sympathy - and I really like Miku."
        "And therefore I easily and gladly agreed."
        play music music_7dl["lastlight_piano"] fadein 3
        "Now that would have been great if this hike had turned out to be an overnight camping trip, with tents set up with no system and a campfire in the middle of it."
        scene cg d4_mi_guitar_club_7dl
        with touch
        "And tin mugs of something strong are walking on their hands, and the squad leaders are not angry today, they don't chase you to bed, they sit and sing songs themselves."
        "And the eastern edge of the sky is already like Nouveau Bujolais - tart and bright, smelling of unfulfilled dreams and unfinished good fortune."
        "And to have the guitar close by, and the girl with the long hair turned into an indistinguishable silhouette against the stars, and it is eerie and sweet to drive away the thought that you look the same now too, and only your indecision separates you from the moment when..."
        "Two silhouettes lean leisurely one toward the other-just like in the movies with that damn rrromance. And the world is born with the miracle of a new love."
        "Or not."
        "Song after song - Okudzhava, Vysotsky, Mityaev, Galich..."
        "Miku would ask back the words and demandingly repeat and repeat the melody, time after time, until she was satisfied. And then she nodded contentedly - and started a new song."
        me "The hour of farewell has come..."
        "I look at her lips, the way she breathes and moves. It's called the fancy word 'plasticity,' though I've preferred good old-fashioned 'grace' all my life."
        "Miku was a very graceful girl."
        me "And he put his arm around our shoulders."
        "Nodding to the beat, she greedily absorbed the new rhyming lines - not noticing already how close we were sitting to each other."
        "How much I want to do what the words of the song say-just hug."
        "Something is bound to happen, unpleasant, inappropriate - it will scare away the magic of the moment. But here and now we were almost in love."
        "She into the new music and the breath of soul felt in the words. And I in her."
        mi "Remember this hall and this warm evening..."
        "The Japanese girl purred."
        "Two silhouettes..."
        "Slowly stretching one to the other..."
        th "And the day after tomorrow I'll go nowhere, leaving behind nothing but a memory."
        "Suddenly I realized."
        "And I looked away, I looked away."
        "I can't, I can't, I can't."
        "Who'd have thought that another man would have given his soul to be in my situation?"
        "More than once I've read all kinds of books about people stranded on foreign shores, and I've wondered how much better off they are there, freed by conscience and circumstance from everything that binds the hands of the natives."
        "What's a conscience for if you disappear tomorrow?"
        "To twist an affair, to coax, to lure somewhere secluded, where with a cross and a pestle to coax the intolerant girl into something more."
        "And disappear the next day, go home or go to the next story station."
        th "And why am I not an unprincipled bastard? This is heaven for a man with no moral brakes."
        "Grimly I thought."
        scene bg int_musclub_day
        show mi sad pioneer
        with dissolve
        mi "Senechka, what happened?"
        "Sensitively Miku reacted."
        mi "You're all sad and turned away. The song is sad, isn't it?"
        me "Yeah."
        "Turning away, I answered."
        "With a sharpened sense of trouble I realized that I might now say something that could make my existence very difficult."
        me "Yeah."
        play sound sfx_7dl["eat_horn"] fadein 1
        "Fortunately I was saved from a more detailed interrogation by the blaring horn, so I hurriedly got up and escaped."
    stop music fadeout 3
    stop sound fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_lunch:
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_empty fadein 3
    play music music_7dl["sky_feather"] fadein 3
    "One of the redeeming qualities of schedule moments was that you could hide behind them if you didn't want to keep doing what you were doing."
    "Unpleasant conversations and cleaning up the grounds are quite among the unloved activities."
    "Some people take a cigarette or sip from a glass (also a habit of having important conversations at the dinner table), some people cover their eyes and lean back in their chair."
    "And we poor pioneers have no choice but to pretend to 'see nothing, hear nothing,' and hurry off to the best establishment on the planet."
    "Today they fed me gingerbread, big and square and luscious enough that it was absolutely impossible to consume it without milk."
    "Though everything, of course, is relative - after watching the little brat greedily shoot her eyes after eating her portion, I smiled and gave her half."
    show us smile sport with dspr
    us "Shpashibo."
    "She mumbled with her mouth full."
    "I brushed it off."
    if alt_day4_me_neu_volley:
        "In spite of the trouble that went along with this girl, for some reason I liked doing all sorts of nice little things for her."
        "Maybe it was because I'd been alone in the family all my life, and I wanted a little sister."
    "As a result of today's events, I never went for a swim."
    if alt_day5_me_neu_mt_voyeur == 2:
        "And going to the beach with a squad leader somehow completely failed to combine with swimming."
        "You'd think, what's wrong with going swimming with a pretty girl?"
        "But no, it doesn't work."
    "So I watched the camp's main quest generators sneakily, and only when they disappeared behind the doors did I allow myself to exhale."
    th "It seems that bathing (or rather, dipping my feet in the water, if I can't find swimming trunks again) is turning from a speculative perspective into a very real one!"
    "By that point, Ulyana had completely finished working her jaws and lightly kicked me under the table:"
    show us normal sport with dspr
    us "Hey, psst!"
    me "Huh?"
    us "Are you busy right now?"
    me "Uh-huh. Deciding whether to lie on my side or roll over on my back."
    show us laugh sport with dspr
    us "Heh! Do you want to know a secret?"
    me "Just like that?"
    "I asked suspiciously."
    show us smile sport with dspr
    us "No, of course not! {w}You're the one who shared an afternoon snack with me as my best friend."
    "It sounded like an inept attempt to get me into trouble."
    "But I thought I was still in control."
    me "Okay. {w}What's the secret?"
    show us normal sport with dspr
    us "Slavya is dating someone!"
    me "No way!"
    "I mean, she's certainly a wow-girl with all the right stuff in all the right places, but..."
    "I'm used to camp relationships usually not being very hushed up - in my camping days, the first couples held hands after the first camp disco."
    "Maybe it's just a different mentality here."
    me "And with whom?"
    show us laugh2 sport with dspr
    us "How should I know? {w}But she's been out of the territory this morning, and she came back out of breath."
    me "Maybe she's running around out there."
    "I reasonably surmised."
    me "She's an athlete."
    show us laugh sport with dspr
    us "You fool, Senka!"
    "Ulyana laughed."
    us "Where is she going to run in her uniform? It's not by the rules, you can't-can't-can't!"
    me "I see. Well, we were gossiping."
    "I started to get up."
    show us normal sport with dspr
    us "Wait!"
    me "Huh?"
    us "Let's..."
    "Ulyana looked around furtively to see if anyone could hear."
    us "Let's follow her and see who she's with?"
    me "Follow her? {w}You mean you and me?"
    show us calml sport with dspr
    us "Do you have something against my company?"
    "She frowned."
    me "Not really, but what about your friend? {w} You're having a spat, aren't you?"
    show us sad sport with dspr
    us "No way."
    "Ulyana waved her hand."
    us "When she heard about tomorrow's concert, she wouldn't let go of her guitar - she kept repeating something."
    me "And you decided to use me as a battery-operated comforter?"
    "I quipped."
    us "You don't mind, do you?"
    "I thought for a moment."
    "Being Ulyana's friend, besides being guaranteed not to get bored, also means this: a willingness to always stick your head up in case either of you messes up."
    "After figuring it out this way and that, I decided that two deaths couldn't happen, so I nodded:"
    me "All right, let's go. {w}Just be quiet."
    if alt_day2_sl_chased:
        me "She's very sensitive to surveillance, she spotted me once."
        show us laugh sport with dspr
        us "I won't get caught, don't worry."
    stop ambience fadeout 3
    play sound sfx_open_door_1
    $ alt_pause(1)
    scene bg ext_square_day with flash
    play ambience ambience_camp_center_day fadein 3
    "Fortunately, while we were bickering with the little one, our object of surveillance had not managed to get far - we had reached the square when the conspicuous golden braids flashed on the other side of it."
    show us surp1 sport with dissolve
    us "There she is! {w}Carefully, after her!"
    "And she took off at such a fast pace that it was hard for me to keep up."
    "It seems that 'carefully', from Ulyana's point of view, would fit perfectly with definitions like 'stomping like an elephant'."
    show bg ext_backdoor_day_7dl
    show us smile sport
    with dissolve
    "So when we reached the gate, through which Slavya came through, I picked up the pace and clapped the girl on the shoulder:"
    me "W-wait!"
    "I exhaled."
    show us normal sport with dspr
    us "What? {w}Hurry up, she'll get away!"
    me "If you keep stomping and sniffing like that, she'll get away for sure!"
    "For the time being we were masked by the noise of the camp, but now we should have exercised reasonable caution."
    stop music fadeout 3
    "Ulyana looked at me unkindly, but heeded the warning."
    stop ambience fadeout 3
    return

label alt_day5_me_neu_sl_secret:
    scene bg ext_path_day with dissolve
    play ambience ambience_forest_day fadein 3
    play music music_7dl["sneakupon"] fadein 3
    "So we left the camp stealthily and much more quietly than we moved around the grounds."
    "I've never felt much need to stick my nose into other people's lives, for the same reason I hated all kinds of reality shows like 'Barn 2,' where people built things, though without using building materials."
    "But now a kind of inexplicable excitement has gripped me."
    "Maybe it's Ulyana's fault and cause - or maybe it's my unwillingness to give up and show that I'm too old and stupid and fat for such adventures?"
    "Or was it because I really wanted to poke around in the activist's closets for a while and find a few skeletons in there?"
    "Anyway, she was moving ahead, fast enough that we had to keep up the pace, too."
    show us normal sport with dissolve
    us "You'll see, she definitely goes out on dates."
    "Unlike me, out of breath after a couple of minutes of racing, Ulyana felt comfortable, she wasn't even out of breath."
    us "And they're there..."
    "The girl wondered."
    show us shy sport with dspr
    us "Kissing! There!"
    me "Kissing. So?"
    "I shrugged my shoulders: I didn't see any crime in it, try as I might."
    show us shy2 sport with dspr
    us "Don't you get it?"
    "Ulyana blushed."
    us "They're kissing!"
    me "So?"
    "She only waved her hand."
    show us normal sport with dspr
    us "Ah, you're still clueless, you won't understand a thing."
    "My imagination helpfully pictured Slavya kissing."
    "She was kissing, though, for some reason, with Ulyanka - and this added a certain spice to the picture - but even so, I couldn't understand what was so special about it."
    "With a shrug, I shut up, trying to save my breath."
    "I was beginning to get a little tired."
    "Unfortunately, both of the female bitches seemed oblivious to fatigue and continued cruising through the woods, gaining momentum."
    "As if it were a matter of honor for Ulyana to be sure to catch up with Slavya, and for the latter, on the other hand, it was vital to break away from uninvited guests."
    "I wondered:"
    th "Doesn't she guess that she kind of isn't alone?"
    th "And if so, couldn't it be that she was luring us somewhere on purpose?"
    show blinking
    scene bg ext_path2_day
    show blackout_exh2
    with dissolve
    $ alt_pause(1)
    play ambience ambience_forest_day fadein 1
    play sound sfx_7dl["breath"] fadein 3
    "That's it, the hobo's dead."
    "It took me about fifteen minutes of this spurt, and then my legs refused to listen."
    "My side stung and my eyes went dark."
    "I leaned against the nearest pine tree and breathed hoarsely, trying to regain my breath."
    th "No hiding from this pain, green circles in my eyes, ah, take me to the field and fucking shoot me..."
    "Ulyana, who had run forward, slowed down, turned in my direction, then in the direction of Slavya, who was leaving, then in mine again..."
    "'Dammit', I managed to make out in the movement of her lips."
    show us dontlike sport with dissolve
    us "Well, why are you standing up? She's getting away!"
    "Unkindly she encouraged."
    "A tremendous struggle of curiosity and reluctance to leave a comrade with the naked eye could be read on her face."
    "Fortunately, a sense of camaraderie prevailed. {w}Otherwise she would have abandoned me in the unknown woods."
    "And they would have found me five years later, lost and feral."
    me "I-I-I c-c-c-an't-t-t…"
    "In three breaths, I exhaled."
    "My mouth was filled with sticky, viscous saliva, and my heart seemed about to escape right through my ribcage."
    show us grin sport with dspr
    us "What a wuss you are."
    "Ulyana stood in front of me with her hands at her sides and looked up mockingly."
    us "How can you carry your bride in your arms into the house if you can't run through the woods?"
    "Somehow inexplicably I caught the twisted logic in this girl's words."
    "And I shrugged it off."
    "Now I didn't feel like stalking or revealing secrets anymore."
    "The program «lie down and die» sounded pretty good right now."
    "I wanted to sit up, but I was immediately grabbed by the arm and brought back to an upright position:"
    show us upset sport with dspr
    us "You what?! You can't sit down if you're that tired, it's bad for you!"
    me "Ah..."
    "Now I wasn't even capable of arguing."
    hide blackout_exh2
    show blackout_exh3
    with dissolve
    "All I can do is stare blankly at the images my mind picks up from the bottom of the well."
    "Yes, to obediently follow the orders of a flighty maiden who has decided to have an unscheduled 'Zarnitsa' without the possibility of tearing off her shoulder straps."
    "So I peeled away from the tree and walked leisurely beside the girl."
    "It can't get any worse. It can't get any worse. It can't get any worse..."
    "We walked like this for a few more minutes, and Ulyana frowned more and more, until she finally got tired of it."
    show us angry sport with dspr
    us "What an asshole you are, rookie!"
    "She said."
    me "First of all, I had nothing to do with it."
    me "Second of all, try to remember my name. My name is Semyon."
    show us sad sport with dspr
    us "If it weren't for you, we wouldn't have lost her."
    me "What's the problem?"
    "The path was under your feet, move forward."
    us "What if there's a fork?!"
    me "Then we'll think!"
    "I cut it off."
    hide us with dissolve
    "Ulyana sulked and turned away, angrily knocking down leaves from the surrounding bushes with a twig."
    with blinds_l
    "She jinxed it."
    "It wasn't ten minutes before we came to a place where the path diverged in two directions at once."
    show us normal sport with dspr
    us "Well, smartass? Are you going to think?"
    "The girl looked at me condescendingly."
    "I shrugged."
    "The right side of the path was well-traveled, trampled - it was obviously used more often."
    "Most likely some pioneer object of interest there, like a blueberry patch or a quarry or some interesting clearing."
    "Unlike the left, which was almost overgrown with grass and barely readable - that direction didn't seem to be much in demand."
    "So it's pretty obvious where Slavya was headed for her hypothetical date."
    $ volume (0.5,'music')
    $ volume (0.5,'ambience')
    menu:
        "Left":
            $ volume (0.9,'music')
            $ volume (0.9,'ambience')
            $ counter_us_7dl += 1
            $ alt_day5_me_neu_sl_voyeur = True
            us "What a fool."
            "Ulyana commented."
            "But she obediently went where I pointed."
            "And the fact that I was right became evident in a few minutes."
            "The sound of splashing water could be heard from behind the trees, a breath of fresh air, and a few steps later we emerged on the shore of a forest lake."
            scene bg ext_lake_day_7dl with dissolve
            play ambience ambience_lake_shore_day fadein 3
            "And immediately recoiled back as Slavya stood some fifteen meters away."
            us "That way."
            "Ulyana hissed, pointing to the bushes with a glance."
            "And immediately, making an example, she flopped down on her stomach and crawled forward."
            "I crawled after her. What else could I do?"
            "For a moment, though, it seemed to me that Ulyana froze."
            "There was something unnatural about her posture."
            stop music fadeout 5
            "So I quickly, quickly crawled up and cautiously looked out of the bushes."
            play music music_7dl["kiss_you"] fadein 3
            scene cg d5_us_sneakpeak_7dl
            with dissolve
            us "Senka, don't look!"
            "She tried to cover my eyes and mouth with her palms at the same time."
            "It wasn't very comfortable, lying next to me, but she did what she could."
            "She had to roll over on her side to do it -s he froze for a moment as the bushes rustled and Slavya on the shore grew wary."
            "Too late. I've already seen what has made our little one so tense."
            "And she had inexorably piled on top of me."
            "But in the end what happened was that we assumed a sort of sandwich position."
            "I was lying on my stomach, hiding in the grass, and Ulyana, like that same cat, threw her arms and legs over me."
            "The girl was warm herself; I could feel it with my bare shoulder through her T-shirt."
            "Like all the curves of her figure - where we were touching."
            "And it was extremely appropriate as Slavya undressed."
            "Or rather, she's already undressed. She just threw her shirt on, alarmed."
            "Ulyana's left palm was on my forehead instead of my eyes, her right one on my lips."
            "So we both saw the shirt slip from Slavya's shoulder, from under her loose hair down onto the clean river sand, leaving the girl completely naked."
            "Picking up more air in her chest, she took the first step."
            "One more."
            "And with one last flash of her naked buttocks, she dove in."
            us "Senya, why are you so hot?"
            "For some reason Ulyana asked in a tense voice - I confess that for a few seconds I forgot she even existed."
            us "And you're shaking all over."
            "Because why not?"
            "I've always been interested in the limits of sensitivity and sensuality."
            "So I pulled my lips out into a tube and kissed the palm still covering my mouth."
            "And judging by the tense, stunned look on the little one's face, she felt and understood perfectly."
            "She blushed, but she didn't pull away."
            us "We've gotten to that level of relationship, haven't we? Kissing the hand?"
            "The girl was trying to make a joke, struggling more with her own embarrassment."
            us "You wish I was her, don't you?"
            "She bit her lip and wanted to say something, but I shook my head."
            us "Then what?"
            "Now the most logical thing would have been to turn to her and hug her without saying a word."
            "But my natural reaction to a bathing Slavya, I'm afraid, would give Ulyanka bruises on her stomach. If I try to hug her."
            "So I smiled with one eye and reached out with my right hand and stroked her head, mussing her hair a little."
            us "What?"
            "Finally figured out to set me free girl."
            me "No regrets. Otherwise I'd have had to peek at you without your panties on. {w} Now that's below average fun."
            "I winked."
            "Ulyana imagined that picture and blushed thickly again."
            with vpunch
            us "Fool!"
            "She slapped my forehead lightly and rolled away."
            "All the while peacefully swimming, Slavya suddenly turned around in the water and looked directly in our direction."
            "It suddenly occurred to me that she might have known about the stakeout since the camp."
            "She just didn't see fit to react."
            "And I could understand her - unlike me, who shirked responsibility by all means, Slavya accepted everything she was told to do."
            "And did."
            "I guess she doesn't get a chance to pamper herself at all."
            "Even though she seems to enjoy all this fuss unspeakably."
            "And in the few moments she manages to squeeze out, find herself in the crosshairs of peepers."
            "But here and now, she seems intent on declassifying the unfortunate voyeurs."
            "So purposefully she swam to the shore where her clothes lay, and, still not the least bit embarrassed, began to dress."
            "All this time I continued to remain in a kind of stupor, watching the nudity disappear under the cloth, and Ulyana, too, remained sullenly silent for some reason."
            "Perhaps it was upsetting to her that there was no dirt on Slavya - except the stuff you can make with a camera."
            "Maybe it was my childishness with the palm kissing."
            "I can't speculate about what's going on in that head."
            "Especially in moments like this, when a boy with a girl's name suddenly looks like a girl."
            "Who acts like a girl and is quite logically interested in all the silly things that girls her age are interested in."
            "Though she hides it cleverly - the effect of her upbringing, apparently, always around people much older than her."
            dreamgirl "And then this one person picks her up and starts touching her in different places with his lips."
            dreamgirl "And doesn't even think about where those places might be, or what kind of contagion that face just got on his lips."
            th "Eh, like what?"
            dreamgirl "At least the fact that she just wiped the ground with that palm. Basically, you licked the ground, do you like it?"
            th "Really? {w}Jupiter, you're angry..."
            dreamgirl "And anyway, she's too close. {w}You have healthy reactions, and a moderately malleable way of realizing them nearby."
            th "What are you implying, you child molestor!"
            dreamgirl "That if she doesn't get off your back, a perfectly logical urge will come to you... {w}Oop, there it is."
            stop music fadeout 3
            us "How long are you going to lie there?"
            "I froze."
            us "Or do you want her to catch you?"
            "Her whisper sounded above my ear, the warmth of her breath tickling my skin, causing goose bumps."
            "And I almost imagined myself turning and touching the lips almost touching my ear."
            "And so I ordered myself to freeze even harder."
            us "Let's go before it's too late!"
            "«Before it's too late» was about fifteen minutes ago, when I realized exactly what Slavya was going to do on the lake, and in what way."
            "Then there was another «before it's too late», before Ulyana got on my back."
            "And now it's too late."
            "I won't be able to get up and straighten up like this."
            "Or rather, I can, but... No, I can't."
            us "To hell with you."
            "The girl hissed and disappeared into the bushes behind me."
            play sound sfx_bush_leaves fadein 0
            scene bg ext_path2_day
            with dissolve
            sl "What's going on h…"
            show sl2 surprise pioneer at zenterleft
            extend " Semyon?!"
            "Marveled Slavya."
            me "Hey."
            "I murderously dropped my head on my crossed arms."
            th "I'm done for."
            "Only I could have gotten myself into such an idiotic situation."
        "Right":
            $ volume (0.9,'music')
            $ volume (0.9,'ambience')
            us "What a fool."
            "Ulyana commented."
            "But she obediently went where I pointed."
            "Didn't even whine about it."
            "Only kicked me once. But that's such a small thing, isn't it?"
            play sound sfx_bush_leaves
            scene bg ext_polyana_day with flash
            "Especially since half an hour later we came out into some big clearing."
            if alt_day4_me_neu_date == 'mt':
                "Yesterday, though, I came out here in a slightly different way."
                "But the actors were the same this time, too."
            "Olga Dmitrievna was sitting on one of the logs, staring thoughtfully into the fire."
            "Hearing our footsteps, she raised her head:"
            show mt normal pioneer at zenterleft
            mt "Semyon, Ulyana."
            "She nodded at us."
            mt "Slavya said she'd find helpers to clean up, but I didn't think she'd need so many people."
            me "Uh, well..."
            "Ulyana wanted to object to something, but I stepped on her foot."
            "Especially as the leaves rustled behind our backs again, and Slavyana got out into the clearing."
            show mt normal pioneer at left with moveinleft
            show sl normal pioneer at right with dissolve
            sl "Are you here to work?"
            "She wasn't surprised."
            sl "Good."
            "Ulyana groaned."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_supper:
    scene bg ext_dining_hall_near_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 3
    "Nothing particularly fatal happened."
    "The price of indulgence for an individual sinner is a properly scrubbed fire pit, the boulders returned to their homeland - to where they were washed or rolled out of."
    if not alt_day5_me_neu_sl_voyeur:
        "Even though my sin is stepping out of the territory."
    "And, of course, dirty hands and face."
    "Which Ulyana scrubbed away with a very special voluptuousness."
    if alt_day5_me_neu_sl_voyeur:
        "She definitely was taking vengeance."
        "I didn't mind that type of revenge, though."
        "The main thing is to dodge successfully when space is lost between us."
        "I really didn't like the thoughts that visited me in the woods, so I was seriously contemplating the option of going to Viola for some kind of sedative."
        th "After all, I'm thirty-something, not seventeen!"
        dreamgirl "Your body thinks otherwise."
        "The inner voice grinned."
    play sound sfx_open_dooor_campus_1 fadein 0
    scene bg int_dining_hall_people_sunset_7dl with dissolve
    play ambience ambience_dining_hall_full fadein 3
    dreamgirl "Who are you going to sit with?"
    "I looked around: there were two empty seats next to Alisa and one by the aisle at the small table."
    $ volume (0.5,'music')
    $ volume (0.5,'ambience')
    if counter_us_7dl >= 5:
        menu:
            "Sit alone":
                pass
            "Sit with Alisa":
                $ volume (0.9,'music')
                $ volume (0.9,'ambience')
                play music music_list["my_daily_life"] fadein 3
                "Dragged along by the restless Ulyana, I made my way to the table, where Alisa was proudly devouring some sea creature alone."
                me "It's Thursday, isn't it?"
                show us normal sport at left with dissolve
                us "Huh?"
                me "There' fish."
                "We sat down next to Alisa, who squinted at us with ill-concealed curiosity:"
                show dv normal pioneer2 with dspr
                dv "I see you two are getting along already?"
                th "Ah shit, here we go."
                "Suddenly I realized."
                "And almost got it."
                show dv smile pioneer2 with dspr
                dv "You've kissed already, huh?"
                show us surp3 sport with dspr
                us "What are you talking about?"
                "Screamed Ulyana."
                show dv grin pioneer2 with dspr
                dv "No? {w}You walk together so touchingly."
                dv "You probably hold hands, too, when no one's looking?"
                me "We hold legs."
                "I snapped."
                show us shy2 sport with dspr
                "And Ulyana didn't seem at all prepared for a pig of that size."
                "And from a friend, too."
                "She continued to sit and blush silently."
                show us calml sport with dspr
                "It's obvious: if it had been me, Electronik, or anyone else she didn't hold the same piety for, he would have been sitting with a plate on his head and a fish by the scruff of his neck."
                "But Alisa managed to surprise her friend."
                "And she sat there wondering what to say in such a situation."
                "Ulyanka, usually quick-tongued and quick-witted, didn't know what to say."
                "Or rather, judging by her tightly pressed lips and frowning eyebrows, she had several options."
                "But even her intelligence was enough to know that it was not worth punishing playful children by beheading or firing squad."
                show us upset sport with fade
                "Once again Captain Retard comes to the rescue!"
                "You couldn't say my actions were anything right."
                "Or at least thoughtful."
                "Just watching the unfolding scene of humiliation and mockery of my fellow man, 'on the fool' suggested:"
                me "I can't understand it, Dvachevskaya: are you jealous?"
                stop music fadeout 3
                show blinking
                $ alt_pause(2)
                "There was silence over the table."
                "So dense and palpable that even the pioneers from adjacent tables shut up for a second and turned in our direction."
                show us sad sport with dspr
                us "Then take him away, I don't need him!"
                "Ulyana jumped up from the table."
                us "Since you love him so much!"
                play sound sfx_dropped_chair
                "Something heavy fell to the floor with a rumble."
                play music music_list["doomed_to_be_defeated"] fadein 0
                "And before any of us could react, the squad leader was already standing next to us!"
                show mt normal pioneer at right with dissolve
                mt "So, what's going on here?"
                "And with surprising speed she bent down, picking up the object from the floor."
                "It turned out to be a piece of slate roof."
                "We used to throw that into the fire if we wanted it to blow."
                show mt angry pioneer with dissolve
                mt "And whose is this?"
                "The leader frowned."
                mt "Ulyana, is it yours? Or Alisa's?"
                th "What a lovely thing."
                "A thought flashed through my head."
                th "How events or fates can turn in just a few seconds."
                "If Alisa hadn't mocked her friend and pissed her off, the situation would have been a little less touchy."
                "But here Ulyana has an awesome opportunity to retaliate for everything she's said at once - by simply framing her friend."
                "Although they can't be friends after that."
                show dv guilty pioneer2 with dspr
                show us dontlike sport with dspr
                us "It's..."
                "The little one started. {w}And I froze."
                "Alisa, too, was watching the unfolding situation with interest - and I'm sure she was having exactly the same thoughts as I was."
                us "Well, let's say mine."
                "She grimaced."
                "Still, she was better and more dignified than her bitchy friend."
                stop music fadeout 3
                show mt rage pioneer with dspr
                mt "So you decided to ruin another event again?"
                "The leader furied up:"
                mt "Okay, spit it out now, what else you got there!"
                show us calml sport with dissolve
                us "I don't have anything."
                show mt normal pioneer with dspr
                mt "Ul-{w=.3}ya-{w=.3}na!"
                show us shy sport with dspr
                us "Oh."
                scene bg int_dining_hall_sunset
                with fade
                play music music_7dl["old_kiss"] fadein 3
                "I guess even now Ulyana would be able to say no, run away, or do something else in her spirit. {w}Something like that."
                "But the leader seized the moment and used it to the best of her ability - she managed to get several slingshots, ball bearings, a box of sulfur match heads, and who knows what else out of the little one's pockets."
                "Even in my unprofessional opinion, the confiscated stuff was enough to confidently sabotage anything at all."
                show mt normal pioneer with dissolve
                mt "Are you sure that's it?"
                "Clarified the squad leader as another piece of slate - slightly smaller than the first one - landed on top of the whole pile of potential instruments of crime."
                show us sad sport at right with dissolve
                "The girl reluctantly nodded."
                mt "Are you sure?"
                "Alisa, who was watching the circus, couldn't stand it."
                "Perhaps her conscience tortured her. {w}Or maybe I just have too much faith in people."
                "And it's just a matter of some kind of human solidarity or gratitude."
                "Anyway, she got up and added some more strange objects to the existing pile, the purpose of which was unclear to me."
                "The squad leader frowned, meaning she understood a little more about it than I did. {w}And she understood perfectly well what the long strips of crumpled newsprint were for, for example."
                show dv normal pioneer2 at left
                dv "Now that's everything."
                show mt grin pioneer with dspr
                mt "Dvachevskaya?"
                show dv angry pioneer2 with dspr
                dv "Oh {image=alt_KS_censor} already."
                "Alisa muttered something unprintable and pulled out a half-empty packet of «Magna» from her back pocket."
                show mt surprise pioneer with dissolve
                mt "You also smoke?!"
                dv "Only when I drink."
                "Snapped the redhead."
                show mt smile pioneer with dspr
                mt "Now I believe that's everything."
                mt "But no one guarantees that you won't try something different."
                show dv shy pioneer2 with dspr
                dv "My honest word isn't enough for you?"
                show mt laugh pioneer with dissolve
                mt "No. And if Ulyana gives that word as well, I'll be very worried."
                show us shy2 sport with dspr
                us "Hey, I'm still here."
                mt "Maybe we should get Semyon to keep an eye on you..."
                "The redheads synchronously measured me with dismissive glances and smiled:"
                show dv smile pioneer2
                show us smile sport
                with dissolve
                us "Sure!"
                dv "I don't mind!"
                show mt normal pioneer with dspr
                mt "Who would've thought."
                "The girl rubbed her chin thoughtfully, then held up her index finger with a 'Eureka!'"
                mt "Let's simplify the task a little: Alisa is in charge of Ulyana, and Ulyana is in charge of Alisa."
                mt "If anything happens at the bonfire, it's both your fault."
                show us calml sport with dspr
                us "Hey, that's not fair!"
                mt "It's all fair. {w}You're friends, aren't you? Then start helping each other out already."
                show dv grin pioneer2 with dspr
                dv "And if anything happens, then what?"
                mt "I'll send you to sleep in the bathhouse tonight for starters."
                "The squad leader smiled broadly, watching the smug smirk slip smoothly off the redheaded elder's face."
                mt "And then we'll see. {w} Adieu."
                "Turning around, she headed for the exit."
                hide mt with dissolve
                us "Hey!"
                "Somehow stupidly wailed Ulyana."
                us "What about Semyon?"
                show mt normal pioneer far at right with dissolve
                mt "What Semyon?"
                us "Isn't he going to be responsible for anyone?"
                show mt laugh pioneer far with dspr
                hide mt with dissolve
                "Olga laughed and went outside."
                "It seems the answer was obvious."
                return
    $ volume (0.9,'music')
    $ volume (0.9,'ambience')
    "Still pouting a little at Ulyanka for the woods, I pretended not to notice her gaze, and strode over to the freestanding table."
    th "When I'm mute, I drink and eat. Sly and fast. And devilishly cunning."
    dreamgirl "Say what?"
    th "Ah..."
    "I said it again and laughed."
    "Anyway, while I've been running around trying to find myself three and a half minutes to pick my nose proudly alone, life hasn't stood still."
    "Kinders, in between, had already set up for tonight's bonfire."
    "Apparently there were some rules governing this moment."
    "Or maybe it was all about the end of the shift, and no one would want to combine the unpleasant with the useless - i.e., the last day and the return from the hike."
    "Anyway, the overnight hike I'd been secretly hoping for wasn't going to happen."
    "Too bad."
    "In my incomplete five days here, it became quite obvious that the people working here are not fanatics."
    "Even the seemingly dedicated to USSR leader turned out to be of the category of people who believe that 'you can't, but if you really want to, you can.'"
    th "Maybe it all turned out to be that I finally started treating them the way I should have from the beginning?"
    th "Like people?"
    th "Although it was much easier to think of each individual character as just a garishly painted gouache on cardboard backdrops with three and a half appropriated lines."
    th "Without life, plot or character."
    "And it's eerie to think that each of them is destined to have a story that's more individual than even a fingerprint."
    "And if you try to absorb them into yourself and at least a couple of percent fit together like pieces in a puzzle, it's easier to slit your wrists, because you have to take for granted and let it sink in that you're no better than any of them."
    "Even if they're just faceless extras in a story that will fade from your memory faster than the echo of the clap of one palm will fade."
    "Even if you are alone in a crowd of happy children."
    show dreamgirl_overlay with dspr
    "This is why there is inspiration, when per square meter of space the concentration of uniqueness exceeds the capacity of reality."
    "And then lines are laid down that are better warned of in advance."
    "To absolve oneself of all responsibility for coincidences, accidental or malicious."
    "But most of all, for the influence those lines may have."
    "Even if it's the influence level of a question over your shoulder: 'And don't you get tired of writing black stuff?'"
    mt "Semyon, don't sleep!"
    "It could have been Miku, Alisa, Slavya, Lena. Or even Zhenya."
    "Yes, even Ulyana."
    "I would breathe their presence in my life and maybe even manage to come alive again."
    show mt normal pioneer with dissolve
    mt "I won't disturb."
    $ counter_mt_7dl += 1
    "It wasn't even a question, but a statement."
    "Across from me the squad leader came down and winked at me."
    play ambience ambience_medium_crowd_indoors_1 fadein 3
    scene bg int_dining_hall_sunset at zenterleft
    show mt normal pioneer with dissolve
    mt "How's it going, Syomich?"
    if counter_mt_7dl > 5:
        "And that turned out to be Olga."
        "A big grown-up aunt."
        if alt_day4_me_neu_date == 'mt':
            "Who burned my papers from The Other Side and didn't ask me where they belonged."
            "And from the looks of it, not the first time she's done it."
        "We have some history."
        "But Olga, for some reason, is in no hurry to share it."
        "And myself, no matter how hard I try, I can't remember anything about her."
        "Rest assured, I certainly wouldn't forget if such an angel came into my life!"
    me "Sour."
    "The hostess is a bitch, the pie is rubbish, the cutlets are horse meat too..."
    mt "Syomich, I have another party assignment for you."
    "Seriously said the leader."
    me "Again?!"
    "I groaned."
    th "What's today, a special event to run up my neck?"
    me "My hands are already dropping."
    "My left arm has fallen along my body, demonstrating the extent to which they are drooping."
    show mt smile pioneer with dspr
    mt "Don't be so sour!"
    "Olga poked me in the shoulder."
    mt "Don't you know? The best reward for a job is a new job?"
    "That would make sense if I was a hero in some RPG."
    "Lots and lots of quests in the name of a clogged experience gauge, piles of levels, and swag for plus thirty percent on craftiness."
    me "What have you got there?"
    show mt grin pioneer with dspr
    mt "Don't you have any idea?"
    me "I don't know and I don't want to know!"
    "Long brown hair, a face with very correct features and huge green eyes."
    "And she looks so frowny."
    mt "Mmmmmoooooo…"
    me "What?"
    th "Can I better hide somewhere? And my thoughts in passing about unicums and clever working men."
    me "Let Slavya work, she gets off that."
    mt "Mmmoooooooo…"
    "The leader moo'ed again."
    show mt laugh pioneer with dspr
    mt "You're mooing like a calf, Syomich."
    "Finally, unable to stand it, the squad leader laughed."
    "She seemed to take genuine pleasure in begging me to... What, by the way?"
    me "What do you want me to do?"
    "I got cautious."
    show mt smile pioneer with dspr
    mt "There! That's the right attitude!"
    "Olga clapped me on the shoulder again."
    mt "That's the way to approach things."
    mt "Don't go far after dinner, okay? I'll need some help from you."
    me "But what do I have to do?!"
    "I exclaimed desperately."
    mt "You'll see."
    $ alt_day5_me_neu_potato = True
    "Nodding to me, she got up."
    stop music fadeout 3
    return

label alt_day5_me_neu_evening:
    scene bg ext_square_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 3
    play music music_list["lightness"] fadein 3
    "It was almost nine o'clock when the fed up and lazy pioneers scarcely gathered in the square."
    "It was obvious that no one wanted to go anywhere."
    "Or rather, couldn't."
    if alt_day5_me_neu_potato:
        "And my situation was also exacerbated by a sack of potatoes, which 'from now until the campfire is your best friend and mother.'"
        "The squad leader's words, not mine."
        "And for some reason I couldn't refuse."
        "Damn."
    th "I could pretend that my stomach hurts."
    dreamgirl "Say that the meat for dinner was non-kosher, and now you have a full purge."
    th "And go read there, like. {w}Or just lie on the bed."
    "Just walk around the camp."
    "If I'm right in my assumptions, it'll be a mass event - that is, for everyone without exception."
    "And for some reason I really wanted to walk around the camp alone, feeling like no one-no one was around."
    show mt normal pioneer with dissolve
    mt "Squads… Atteeention!"
    "She barked in a way that scared me a little."
    mt "On the first-second, count!"
    hide mt with dissolve
    me "No obligation and no ideological bullshit..."
    "I muttered to myself, diligently complying with the requirements of the regulations."
    "Everything was good about the Soviet Union in terms of opportunities to integrate into society, a child was trained from childhood to be able to work as part of a team."
    "But this regulation..."
    "The vehement denial of religion, the mass conversion of churches and cathedrals into cultural centers and swimming pools..."
    "As a result, communism took on the features of what it had been so diligently exterminating - the old story of enemies being closer than brothers."
    "I'm talking about those ties, symbolism, formation training, and a whole bunch of completely useless things in everyday life, all the purpose of which is to make man act as a collective being."
    th "Pure religion. It even has its own temples. And Saints. Like Joseph Vissarionych. Or was he not here?"
    "I squinted at the bronze dork with glasses."
    th "They don't put up monuments to just anybody, do they?"
    with fade
    "I was paired with Electronik."
    if alt_day5_me_neu_candle == 3:
        if (counter_un_fz_mt_transit == 3) or alt_day3_technoquest2:
            "To my great envy concerning Shurik, who was pulling his thighs so hard in the infirmary."
        else:
            "To my great envy concerning Shurik, who looks like he's going to skip all this volunteer work successfully."
    th "No, let's get sick, shall we? Stomachache? Or cough properly?"
    "I tried that."
    "Didn't come out very well."
    "Somehow unnatural."
    show el normal pioneer at left with dissolve
    el "Hey, are you okay? {w}How are you feeling?"
    "Yeah, it's not much of an accomplishment to fool that one."
    "If only Olga Dmitrievna was as gullible."
    me "It's all right."
    "I brushed it off. {w}I don't want you to show off my acting talents in front of all the honest people."
    "I suppose Ulyana wouldn't be the least bit embarrassed by such a role - this one would be perfectly capable of coughing up a mechanical injury and then wheeze in a most natural way."
    th "Not the price I'm willing to pay for the chance to walk around the camp alone."
    me "Choked on poison."
    show el surprise pioneer with dspr
    el "What?"
    me "Nothing."
    "I made an effort to straighten myself out."
    me "I choked on my saliva when I thought of baked potatoes."
    hide el with dissolve
    "Electronik nodded understandingly and just as understandingly disappeared into the background, not bothering me anymore."
    me "This way, the evening won't be so awful."
    "I cheered up."
    th "If he stays out of my way, we'll get along just fine."
    th "I guess so."
    "The rest of the pioneers I knew paired up the same way they lived."
    "Apparently they really got used to each other during those three weeks, some of them even became friends."
    "Slavya and the Buzzer were talking peacefully about something, giving me a chance to see the beetlewoman in her natural habitat while she still had her thorns out."
    "It turned out to be quite a sane creature, even a little cute."
    "Lena and Miku were whispering softly about something, giggling now and then."
    "The mutual lapping was even more noticeable here - too far down the sociability scale were the extremes."
    "Miku stopped gibbering and learned to adjust the volume. Lena stopped mumbling like a mute."
    "Normal human communication - too bad it won't be like that with me, since I'm self-conscious and shut up before I can talk to anyone."
    "It makes sense with the redheads; they've known each other for years, by all accounts."
    th "Stomp-stomp…"
    stop music fadeout 3
    "Mechanically turning left along with everyone else, I staggered toward the gate."
    stop ambience fadeout 2
    scene bg ext_path_sunset with dissolve
    play ambience ambience_forest_evening fadein 3
    "The camp was built by prudes."
    "And planned by them."
    "So while our squad leader assured us that we were 'building character' and trying to 'get stronger in the fight' and various other ways to foster a sense of camaraderie, something else was actually going on."
    "Because I don't know about everybody else, but I was a little distracted by the people around me."
    "At first they pissed me off by yelling, rightly asking in response to remarks: 'You said don't yell - not in the woods. I'm in the woods.'"
    "Then with a game of gunfighting with cones."
    "Gritting my teeth, I put up with that, too."
    th "Maybe that's the incipient sense of camaraderie."
    "I talked myself out of it."
    th "It just manifests itself differently in everyone."
    "And you don't have to go up to a rambunctious pioneer who hit you in the forehead with a bump and punch him in the nose in retaliation."
    el "Semyon, why are you so gloomy?"
    me "Eve-ry-thing's fi-ne!"
    "I gritted my teeth."
    me "Just great."
    th "The point of camping is not to kill your comrades as you try to get to abstract point B."
    th "But it would be great if it was the Wild West, and every freelance shooter always had a few forty-four caliber lead salutes at the ready."
    th "They wouldn't be throwing cones then."
    scene bg ext_backroad_day_7dl with dissolve
    if alt_day5_me_neu_potato:
        "It got a lot worse when we stretched out on the narrow path in a column of one."
        "Electronik was panting and stepping on my feet behind me, and Alisa was hissing about something in front of me."
        "What a pleasure."
        "I really wanted to catch up with the squad leader and put that sack of potatoes on her head."
        "I wanted it so bad!"
        "I was dreaming, imagining in detail what she would look like in her new hat."
    else:
        "I cheered up a little, though, when Boris Alexandrovich, standing at the head of our column, turned off somewhere from the wide path on which we could walk in pairs to a path noticeably narrower."
        "We had to line up one at a time."
        "So no one was in the way, catching my eyes or asking where I was staring."
        "Ahead of me stomped Dvachevskaya in her belly-tied shirt and skirt, stretched so tight that if you wanted to, you could see everything you wanted to see."
        "There I was, peering."
    scene black with fade
    "And got so immersed in this activity that when Alisa stood up abruptly, I didn't have time to hold back my step and braked into her with all my might."
    scene bg ext_backroad_day_7dl
    show dv angry pioneer2
    with flash
    dv "Hey, watch where you're going!"
    me "Sorry! You stopped too fast!"
    me "Why, by the way?"
    show dv smile pioneer2 with dspr
    dv "You looked at my ass so much you lost track of time, didn't you? {w}We've arrived!"
    "Trying to hide my flushed cheeks, I carefully peeked out from behind Alisa's shoulder."
    "Indeed."
    "We arrived."
    return

label alt_day5_me_neu_campfire:
    scene bg ext_polyana_sunset
    show mt normal pioneer
    with dissolve
    mt "Squads, disperse!"
    "Commanded the leader."
    "And the pioneers took their places in an orderly fashion."
    "The order here was worse than at supper in the canteen."
    play music music_7dl["lastlight_guitar"] fadein 3
    "I've been here before today, and nothing has changed since then."
    "A relatively circular clearing, with several long logs lying around its perimeter, forming an irregular polygon."
    hide mt with dissolve
    "The geometrical center of this polygon was on the smoked stones of the fireplace, which I had to carry and put back in place today."
    "There were already some logs with a pile of kindling in the middle."
    "All you had to do was strike a match and light it all up."
    "And, as usual, our Miss Infallible was back on the rock."
    "Shaming the Boy Scouts, in one practiced move away from herself, she struck a match..."
    play sound_loop sfx_forest_fireplace fadein 3
    "And the flame was born."
    th "Well, I guess that's it."
    "Thought to myself."
    th "Usually with a campfire it just starts - cleaning up the area, finding stakes, which are always in short supply for some reason, preparing the bivouac."
    "Then the chef gets on the pots and pans while we get the missing pegs in the woods and surprise the fish for the morning's soup."
    "And at the same time a pan of potatoes and mushrooms is hauled off the coals, black - no bottom in sight - tea comes up, and from the tents already set up, natives in track suits stretch to the stirring smells."
    show sl normal pioneer with dissolve
    sl "How's it going?"
    "After standing around the fire for a while, Slavya came over to me and sat down next to me."
    me "A little sorry...{w} that it's incomplete, this camping trip."
    "I confessed."
    sl "Yes?"
    "Slavya turned out to be an understanding girl."
    sl "We were going for a few days in the middle of the shift, but we never got around to it."
    sl "Did you go yet?"
    me "You ask!"
    "I shared with her my thoughts on where and how I see myself doing a normal hike."
    me "And at night, when the younger kids go to their tents, you can get a guitar and a bottle of something strong."
    show sl serious pioneer with dspr
    sl "I don't like alcohol."
    "Slavya wrinkled her nose."
    sl "Life has to be seen in all its glory - what it really is."
    "I shrugged."
    me "Sometimes it's vital for perception to loosen the brakes a little."
    show sl smile2 pioneer with dspr
    sl "And I - don't need to!"
    "Slavya realized that sounded like bragging, and she blushed a little."
    me "You may be right."
    "Compared to the place I thought of as my home, the air itself here was such that it was sometimes intoxicating without any wine."
    "Especially if the mood was the same."
    me "But to describe in words the experience of sitting with someone like that by the fire at night... It's useless."
    "Slavya smiled and stood up:"
    sl "I wish I'd had the chance. Don't miss it."
    hide sl with dissolve
    "She stroked my shoulder and stepped back to the squad leader, speaking softly to her."
    th "And now I was alone again."
    th "The squad leader didn't seem to care about me anymore either."
    "I looked around. The pioneers around me were busy minding their own business."
    if counter_me_neu_answers > 0:
        th "It seems like a good time to clarify something..."
    else:
        th "Maybe I should just get out?"
    menu:
        "Time to leave!":
            $ alt_day5_me_neu_campfire_choise = 1
            th "And really, what's to waste time on here?"
            stop music fadeout 5
            if loki:
                "I glanced around to make sure the leader and Slavya were busy. There was no one else to bother me, so I moved quietly toward the path."
            elif herc:
                "A scheme of tactical retreat was instantly formed in my head, but it came out so idiotic that I just got up and walked toward the woods, not the least bit worried about my escape being noticed."
                dreamgirl "Tough guys don't look at explosions!"
            else:
                "Trying not to cross my eyes with anyone, I cautiously rose from the log and began slowly retreating into the darkness."
            stop sound_loop fadeout 1
            play ambience ambience_forest_evening fadein 3
            scene bg ext_backdoor_night_7dl with joff_r
            play music music_7dl["unsettling"] fadein 3
            "I entered the camp without hindrance - no one thought to close the gate after all the pioneers had gone to the bonfire."
            th "Come in whoever you want, take whatever you want..."
            dreamgirl "We don't have anything to take!"
            dreamgirl "There's only one rich guy who trumpets his imported equipment, but he doesn't take his eyes off it day or night."
            th "And I'm not trumping anything!"
            if herc and counter_me_neu_answers > 0:
                th "I bragged once..."
                th "Electronik is about to write a denunciation on me!"
                dreamgirl "Why would he?"
                th "Because my face is very suspicious."
            "In fact, there was no good reason to close the gate. There were no settlements in the area, and there were no wild animals in the local forests."
            play ambience ambience_camp_center_evening fadein 2
            scene bg ext_square_night with dissolve
            th "So I'm in camp."
            th "But what am I going to do with the time left before lights out?"
            "I hadn't really thought about that when I decided to run away. I figured out where I could go in search of adventure."
        "Continue looking for answers" if counter_me_neu_answers == 2:
            if loki:
                "Looking around cautiously again, I got up from the log and slowly retreated into the thicket of the forest. Out of sight of the pioneers sitting by the fire behind the nearest tree, I turned and raced toward the camp."
            elif herc:
                "I got up from the log and stared into the darkness, trying to fumble for familiar shapes."
                "I needed to talk to Shurik about his trip to the bomb shelter."
                "Walking between the timbers, I stared at the pioneers. The smoke made my eyes sting, and I couldn't find the bespectacled one."
                "But his colleague was not far from the impromptu choir that Miku had gathered around her, strumming her guitar."
                me "Have you seen Shurik?"
                show el shocked pioneer with dspr
                "Syroezhkin broke away from his contemplation of the fire and turned to me, his eyes rounded fearfully."
                el "Shurik?"
                th "So panicked, as if I were sandbagging him in the warehouse after his shift for underdelivering Shurik!"
                th "How well that stuff from the mine shanked him in the brain!"
                show el think pioneer with dissolve
                el "And he didn't go to the bonfire."
                me "What do you mean, he didn't go?"
                el "Viola wouldn't let him go. Said he'd better stay in the cabin for a while."
                hide el with dissolve
                "I nodded to Electronik, and my gaze slid to the path to the camp."
                th "There may be no other way to get him to talk, so we have to act now."
                dreamgirl "What's the problem with approaching him tomorrow in the canteen?"
                th "Privacy is necessary for this conversation. I don't think he'll want to talk about it in front of prying ears."
                th "There was definitely something strange going on in that bunker. He couldn't help but feel it."
                dreamgirl "But you didn't feel anything yourself!"
                th "Let's say he didn't experience anything strange there either. {w}But then why did he open the second door, didn't come back from camp until morning, and didn't get even a single bolt out of the cherished bomb shelter?"
                "My split personality had no argument for that, so I moved silently toward the path, skirting the timbers around the perimeter."
            else:
                "I rose quietly from the log and found Olga Dmitrievna with my eyes. She was talking to Viola about something, occasionally glancing at Ulyana, who was twirling nearby."
                th "And now, as long as she can't see..."
                "I turned around and walked quietly but confidently toward the forest path."
            stop sound_loop fadeout 2
            stop music fadeout 2
            stop ambience fadeout 2
            $ alt_day5_me_neu_campfire_choise = 2
            $ counter_me_neu_answers = 3
        "Stay for a while longer":
            $ alt_day5_me_neu_campfire_choise = 3
            th "What am I supposed to do in the camp, though?"
            th "Do you want me to paint Genda pink?"
            "I made myself comfortable and stared into the fire."
            th "After all, all this camping is also necessary for ephemeral communion with nature. So here I sit, melding with the log - in short, successfully accomplishing the task at hand."
            show ka smile pioneer with dissolve
            ka "Are you homesick, pioneer?"
            "I was plucked out of my stupor by the leader of the other squad."
            if alt_day3_un_fz_work == 'dv':
                "And that was definitely the squad leader I least wanted to cross paths with!"
                ka "Your fiancée must have left you!"
                "I glanced over at Alisa strumming her guitar by the fire."
                me "Uh-huh. She left me for Miku."
                show ka laugh pioneer with dissolve
                ka "What morals of today's youth!"
                "She laughed and nodded her head at me."
            elif alt_day4_me_neu_cs_debt:
                "The hairs on the back of my neck involuntarily moved."
                th "Did she remember the card debt?"
                "It was as if Katushka had read my mind:"
                show ka laugh pioneer with dissolve
                ka "Don't worry, I won't charge you any money."
                "She winked, enjoying my confusion."
                ka "I'm here for something else."
            else:
                me "No, I guess not..."
                "I couldn't tell if I'd seen her before."
                th "Looks kind of conspicuous..."
                dreamgirl "Buddy, you can hardly tell me now what color the dishes you eat out of every day are."
                dreamgirl "So your powers of observation are not to be relied upon."
                show ka laugh pioneer with dissolve
                ka "That's good."
                "She rubbed her hands together pretty good, and I sat back down, just in case."
                $ meet('ka','Katyushka')
                ka "My name is Katyushka. And I have a proposition for you."
            show ka normal pioneer with dissolve
            ka "Let's go to my pioneers, since all your own have abandoned you!"
            "That sounded pretty hurtful."
            th "And I wasn't abandoned!"
            th "I left myself!"
            "Katyushka held out her hand to me, and I reluctantly rose from the log."
            th "I haven't sat here with the children yet!"
            th "Why on earth would I follow her?"
            "But curiosity overpowered me, and sitting alone was too... defiant."
            stop music fadeout 2
            scene bg ext_polyana_sunset with dissolve
            $ alt_pause(1.5)
            play music music_7dl["someone_like_you_guitar"] fadein 3
            show ka smile pioneer at fleft with dissolve
            ka "Boys, make room! I've brought a comrade from the first squad to join us."
            show dn normal pioneer at center
            show al normal pioneer at right
            show tn normal pioneer at fright
            with dissolve
            "I landed awkwardly on the space I had vacated on the log, glancing around at the children."
            "The children, who turned out to be Ulyanka's peers, were in turn staring at me."
            th "And this squad leader is a master at integrating newcomers into a close-knit team!"
            ka "Anyway, kids, this is Semyon. Semyon, these are the kids."
            if (not alt_day3_un_fz_work == 'dv') and (not alt_day4_me_neu_cs_debt):
                th "Gee, I'm a local celebrity!"
            ka "Semyon, have you been to Sovyonok before?"
            me "No, I haven't."
            "The prolonged introduction scene made me feel even sillier for my taste."
            show ka happy pioneer with dissolve
            "Katushka smiled happily."
            ka "Then maybe the old-timers can tell you something about the camp?"
            th "No thanks, I know where the canteen is without them!"
            me "You know..."
            "I looked around nervously, but there were no escape routes on the horizon."
            $ meet('voice','Pioneer girl')
            voice "Can I tell you about the ghost of the squad leader?"
            "Joyfully volunteered a girl who looked a little younger than Ulyana."
            show ka smile pioneer with dissolve
            ka "Of course! Semyon, you have strong nerves, don't you?"
            if herc and counter_me_neu_answers == 2:
                "After our morning hike to the bunker and the gossip from Syroezhkin, this legend didn't seem like a regular camp tale to me."
            me "Alright, go on!"
            voice "Anyway, there was a squad leader at the old camp. And her fiancé worked there too."
            voice "But her fiancé left her and she hanged herself. Right in the middle of Parents' Day!"
            voice "After that, the old camp had to close because the ghost of that squad leader wandered there. {w}They say she kills boys in their sleep!"
            th "No, well, that's too much. It was almost believable until the last sentence!"
            dreamgirl "And really, what would be wrong with a harmless ghost?"
            dreamgirl "On the contrary, a cool attraction. This hole would be more popular than Artek!"
            $ meet('voice','Pioneer')
            voice "It wasn't a squad leader, it was a nurse!"
            "Some boy interrupted the narrator."
            voice "And she didn't have any fiancé, her brother died!"
            if herc and counter_me_neu_answers == 2:
                "It was foolish to hope to get any clues in this story. Even its original version, which might have contained some truth, was already lost among the many free interpretations."
            voice "I know there was a bunker in the old camp where they did experiments on people!"
            me "And no one ever noticed that?"
            voice "They did once, and then the camp was shut down. Three kids went missing during that shift, and no one ever found out what happened to them."
            me "Maybe they were killed by the ghost of a squad leader?"
            voice "The nurse!"
            "The boy pouted and stared into the fire."
            show ka happy2 pioneer with dissolve
            ka "Has anyone heard the legend of the stone?"
            th "I certainly haven't..."
            "But everyone else also shook their heads in bewilderment.{w}"
            show ka grin pioneer with dissolve
            extend " The squad leader squinted slyly."
            ka "It is said that once there was a stone in this forest that granted wishes. {w}But then it disappeared without a trace."
            voice "And where was it?"
            show ka smile pioneer with dissolve
            ka "Right here!"
            "She circled the campfire meadow with her hand."
            ka "That's why we always go here at the end of our shift. {w}In the hope that the dust from this rock will grant all your wishes for the rest of your shift."
            "The legend sounded beautiful and quite organic to this place, but something told me that Katushka had made it up as she went along."
            $ meet('voice','Pioneer girl')
            voice "Do you know about the quarry?"
            "Another girl joined the storytellers."
            voice "There's a magic quarry in the woods. You can't go there by yourself, you'll never find it, not even with a map."
            voice "Only someone who has been there once before can lead you to the quarry."
            $ meet('voice','Pioneer')
            voice "It's all nonsense!"
            "Quietly muttered the chubby kid sitting next to me."
            voice "I found that quarry myself last year, without a guide."
            $ meet('voice','Pioneer girl')
            voice "There's also the Forest of Memory next to this quarry. Anything you leave there, you'll remember for the rest of your life!"
            me "Only if it's something very expensive, and then I'll be strangled by a toad for the rest of my life."
            "I quipped. The girl frowned."
            voice "Fool! Leave a message!"
            me "And what, all these Petyas-plus-Mashas from the local trees then got married? Or will they just remember each other for the rest of their lives?"
            dreamgirl "Stop ruining the kids' party, nerd."
            dreamgirl "They don't believe any of this nonsense themselves, but it tickles the nerves."
            dreamgirl "Don't ruin the atmosphere on the role-playing server!"
            "The narrator sulked and turned away resentfully. The other children were quiet, too, staring at the crackling embers in fascination."
            hide ka
            hide tn
            hide dn
            hide al
            with dissolve
            stop music fadeout 3
            "A familiar red T-shirt flashed from the other side of the fire, and my relaxed mood immediately faded away."
            play music music_7dl["shappihn"] fadein 3
            th "In less than five days I have firmly learned that where there is Ulyana, there is trouble. And if there's no trouble during the whole hike..."
            scene cg d5_us_ghost with dissolve
            play sound sfx_bush_leaves
            "In stealth mode, I got up from the log, walked around the fire, and crept up on Ulyana, huddled in the bushes."
            me "What, hiding from the smoke?"
            "The girl frightenedly stepped aside, and the piece of slate she was holding in her hand flopped to the ground."
            dreamgirl "Wow, we could have had fireworks here!"
            us "What are you..."
            scene bg ext_bush_sunset_7dl
            show mt angry pioneer at right
            show us fear sport
            with dspr
            play music music_7dl["areyouabully"] fadein 3
            "She didn't have time to finish: the squad leader appeared from behind the bushes, and that certainly didn't bode well for us."
            mt "And what's the meeting all about?"
            th "I don't want to become an accomplice..."
            "Either Olga had a built-in night vision function, or she already knew perfectly well what Ulyana was planning to do without it, but she identified the unfortunate piece of slate in literally seconds."
            show mt rage pioneer at right
            show us upset sport
            with dspr
            mt "Sidorova!"
            "The leader's angry gaze shifted from the little one to me."
            show mt angry pioneer at right
            mt "Semyon, come back to the fire. Ulyana and I are going to have a serious talk."
            "In an unobjectionable tone she said."
            show us sad sport with dspr
            "Ulyana turned to me with horror. There was a desperate plea for help in her eyes, but I just shook my head and walked away obediently, leaving the girl to Olga's predation."
            if herc:
                th "She deserved it herself. What fun it would have been if she'd knocked someone's eye out!"
            elif loki:
                th "I certainly like the little one, but not enough to put my head on the line for her!"
            else:
                th "I don't need any unnecessary showdown - with all due respect to Ulyana!"
            scene bg ext_polyana_sunset with dissolve
            play music music_7dl["lastlight_guitar"] fadein 3
            "I took up one of the free logs and stared into the fire, almost instantly putting the shenanigans of the redheaded junior out of my mind."
            "Soon Slavya brought me my potatoes and a matchbox of salt."
            "Not French delicacies, of course, but..."
            "Ulyana, who had been punished for a crime she had committed, sat on her own, her lips trembling with resentment."
            "Ulyana was deprived of her potatoes for her behavior."
            th "God, what idiotic punishment is this?"
            "Flashed through my mind."
            stop music fadeout 3
            $ volume(0.5, 'ambience')
            th "Olga, of course, should have made it clear to Ulyana that throwing a slate into a fire is a traumatic thing to do."
            th "But I think that's too much."
            menu:
                "Give your potatoes to Ulyana":
                    $ karma += 25
                    $ counter_mt_7dl += 1
                    $ counter_us_7dl += 1
                    $ alt_day5_me_neu_us_potato = True
                    play music music_7dl["there_you_are"] fadein 3
                    $ volume(0.9, 'ambience')
                    "It wasn't that I felt guilty about punishing the little one, or trying to apologize to her."
                    "But I was so uncomfortable and embarrassed by the situation she was in that I found myself unable to sit still."
                    th "Old Semyon, where are you, hello?"
                    "I scolded myself."
                    "And I got up."
                    me "Hey."
                    show us sad sport with dissolve
                    us "What do you want?"
                    "I got a dejected look from that perpetual shooter."
                    "And I was convinced once again that leaving children without food is a highly questionable punishment."
                    "You can't deprive a child of a good thing just because she thinks with the same place she's sitting on."
                    me "You want one?"
                    "I held out my potato to her."
                    "The one I just peeled and salted while scalding."
                    show us upset sport with dspr
                    us "What about you?"
                    "I shrugged."
                    us "And you're just going to give it away, aren't you?"
                    th "If Ulyana was angry at me for betraying her, the aroma of the baked potatoes displaced all her resentment at once."
                    "I smiled."
                    show us normal sport with dspr
                    if persistent.us_7dl_good:
                        us "All right, you talked me into it. I'll let you kiss me on the cheek."
                        us "But don't get cocky!"
                        "I blushed."
                        me "Are you going or not?"
                        us "Date?"
                        me "Potatoes!!!"
                        show us laugh sport with dspr
                    else:
                        us "Just remember, I'm not going out with you anyway!"
                        me "Fine! Fine!"
                        "I put my palms out in front of me."
                        me "If you don't want to go out with me, don't go out with me. Do you want some potatoes?"
                        show us smile sport with dspr
                    us "Come on, of course!"
                    "She instantly grabbed the treat."
                    "And..."
                    me "What else?"
                    th "Let's get this skit over with already, and I'll go back to sitting on the log?"
                    th "I'm uncomfortable with the thoughts that arise in the heads of those watching us!"
                    show us shy2 sport with dspr
                    us "I can't do it like that."
                    show us laugh2 sport with dspr
                    "When she broke the potato, she took the bigger piece and left the smaller one for me."
                    us "That's better! {w}Family sharing!"
                    hide us with dissolve
                    "With a grin, I ate my half and went back to the log."
                    show mt smile pioneer far with dissolve
                    "And on the way intercepted a wink from Olga Dmitrievna."
                    hide mt
                    show sl smile pioneer far
                    with dissolve
                    "And the approving thumb of Slavya."
                    hide sl with dissolve
                    stop music fadeout 3
                "She'll do fine without it":
                    $ volume (0.9,'ambience')
                    "With a shrug, I consumed the treat as intended."
                    "After all, I'm a growing organism, I need it more."
                    "And to the wailing conscience, I made a fist and told it to shut up."
                    "I don't need the little one to come within five yards of me at all."
                    "Practice shows that's enough to stay out of the storm."
            $ persistent.sprite_time = "night"
            $ night_time()
            scene bg ext_polyana_night with dissolve2
            play music music_7dl["nowyouseeme"] fadein 3
            "The fire burned down for good, everyone ate some potatoes and sang a little under guitar."
            "Mission accomplished?"
            "As if answering my words, Olga stood up and commanded:"
            show mt normal pioneer with dissolve
            mt "Squads! {w}According to numbers and height for the way back to camp - line up!"
            "Here was where the shape of the clearing became clear - having risen at once, the pioneers appeared as if they were once again on an improvised lineup."
            "So all that was left to do was to turn around and head for the hell of it according to the chain of command."
            "An evening, no better or worse than any other."
            stop sound_loop fadeout 2
            stop ambience fadeout 2
            scene bg ext_path_night with dissolve
            "Although this one was dedicated to that which I had so diligently buried on distant shelves in the recesses of my memory."
            "And the further away, the better."
            stop music fadeout 3
            "Because there's no going back to the past, no matter how happy it was."
            ".{w=.3}.{w=.4}."
    return

label alt_day5_me_neu_map_house_dv1:
    play ambience ambience_camp_center_night fadein 2
    scene bg ext_house_of_dv_night with dissolve
    "I pulled up in front of the Jolly Roger flag cabin, ominously grinning in the pitch darkness."
    if alt_day2_dv_us_house_visited:
        th "Opa. The Abode of the Redheads."
    else:
        "I had no doubt about the fact that this house was inhabited by Her Redheadedness and Redhead Jr."
    if alt_day1_sl_keys_took not in (1, 3):
        th "Write 'Alisa is a fool' on the door?"
        th "I wish I had anything to write with!"
        "I looked around, but I couldn't find any potential writing objects."
        th "I remember Olga had a ballpoint pen on her desk..."
        th "But that's just not decent somehow. And the circle of suspects would be narrowed down to just me."
        "Such a tempting idea, how to make a mess of Dvachevskaya, had to be discarded."
        "I turned around and walked away."
    else:
        play music music_list["so_good_to_be_careless"] fadein 3
        th "I wonder if there are keys to other people's houses in my bundle."
        play sound sfx_keys_rattle
        scene bg int_house_of_dv_night_no_light_7dl with dissolve
        queue sound sfx_open_door_1
        "By a short search it was determined that there was. The door with Jolly Roger behind the glass creaked miserably and opened."
        dreamgirl "Yay, looting!"
        dreamgirl "You're going to steal her panties, aren't you?"
        th "Don't get the size wrong. Otherwise you'll have to prove to your comrade major that you talked to a frog..."
        dreamgirl "Buddy, you're really bad, if you don't have enough material to estimate the size of her..."
        th "I don't give a shit about her panties!"
        play sound sfx_close_door_campus_1
        "I angrily slammed the door in the vain hope of silencing my inner voice with this gesture."
        "It was impossible not to take advantage of such a fabulous opportunity to mess with Dvachevskaya. But there was only one question left..."
        "What would surprise her?"
        "It is unlikely that Alisa was afraid of bugs - otherwise she would not get along in the same house with the little one. The glue on the doorknob was too trivial and, unfortunately, not targeted."
        "I didn't want to ruin any government property either, so all the options of unscrewing doors and cutting up sheets were off the table, too."
        dreamgirl "Let's give her a love note in Miku's name!"
        "No way. She might get excited..."
        "And then I almost slapped myself on the forehead at the thought."
        th "Snake!"
        play ambience ambience_camp_center_night fadein 2
        scene bg ext_house_of_dv_night with dissolve
        "Not much time had passed since yesterday morning, and this morning's rain was hardly conducive to drying the snake carcass that Ullianna had captured, but the thought was already beginning to form a simple plan of action in my head."
        dreamgirl "Do you seriously think the little one didn't brag about her prey to her girlfriend before carrying it to you for cutting?"
        th "And who knows her. What if she isn't?"
        th "Maybe she picked up that snake to scare Dvachevskaya."
        if loki:
            th "Well, I guess for all my merits I have the same rights to this snake as Ulyanka."
            th "And in our business, early bird gets the worm."
        elif herc:
            "It was a little embarrassing to deprive a child of such joy."
            th "But if all goes according to plan, Ulyana will also enjoy the spectacle to come!"
        else:
            th "I'll have to remember to watch out not only for Alisa, but for her girlfriend as well, starting tomorrow."
            th "I don't think she'll forgive me for privatizing her carcass!"
        "Barely rubbing my hands together with joy, I dashed toward the pier."
        scene bg ext_boathouse_night with pushright
        play ambience ambience_boat_station_night fadein 2
        "There was no light on in the boatman's cabin, which gave hope of going unnoticed."
        if dr and counter_me_neu_answers == 1:
            th "Although he didn't catch me and Lena last night..."
            "I was surprised to realize that I had completely forgotten about that strange evening."
            th "I'll certainly think about it tomorrow..."
            th "There's still a lot to do today!"
        scene bg int_attic2_night_7dl with dissolve
        "I climbed up to the attic almost without a problem, except that I almost fell over when I tried to catch a shadow on the wall of the gatehouse."
        th "Now if I could just find out where I put the bastard. Can't see a thing!"
        "Shining the phone at me, I moved almost at random toward the corner where I had left the snake carcass to grease yesterday."
        "Only a miracle helped me make my way to the other end of the attic and back without hitting a single piece of junk piled there or waking the boatman with my actions."
        "Clutching the snake's tail with two fingers in an unconscious attempt to minimize contact with such a vile and smelly substance, I cautiously climbed out the skylight onto the roof."
        scene bg ext_boathouse_night with dissolve
        "Going down with only one free hand was determinedly impossible, so I threw the already three times defiled body down, praying it wouldn't slide off the wet planks into the water."
        dreamgirl "Wow, Worms, but in real life!"
        "Carefully jumping down onto the planks, I picked up the snake and moved toward the cabins."
        play ambience ambience_camp_center_night fadein 2
        scene bg ext_house_of_dv_night with pushleft
        "It was just a matter of stuffing the snake's remains with something to give it a more realistic shape, to put it in a conspicuous place."
        dreamgirl "Wow, there will be screaming!"
        th "Yeah. The whole camp will listen!"
        dreamgirl "No, I mean what kind of sounds you're going to make stuffing your surprise."
        th "There you go!"
        if loki:
            "Finding a decent-sized burdock, I wrapped it around the snake skin and began to stuff it with bunches of grass, helping myself with a small branch from a nearby bush."
        elif herc:
            "In a foolish attempt to prove something to my inner voice, I grabbed the snake skin tighter, squatted down, and began stuffing bundles of grass into the future scarecrow."
        else:
            "Spreading the snake skin on the grass, I held the tail in place with one branch while I pushed the grass bundles inside with the other."
        "There was nothing to fill the hole, from which the grass protruded profusely, so I could only hope that the shock would hide the details for at least a few seconds."
        "After another inspection of my unconvincing snake substitute identical to the natural one, I made my way to the redhead cabin."
        scene bg int_house_of_dv_night_no_light_7dl with dissolve
        "I identified Alisa's bed by the large size of the bathing flip-flops lying by the nightstand."
        th "Apparently, cleaning is not on Dvachevskaya's list of hobbies..."
        if alt_day1_chase:
            "However, clean in this camp was only the unoccupied cabin in which Slavya fed me."
        else:
            th "Though it's not for me to show off when it comes to cleaning."
        "Turning the lantern screen to full brightness, I took a close look around the cabin."
        th "I can't see the window sill, the nightstand is covered in junk, so is the desk..."
        "But the bedspread on Alisa's bed, which had been pulled down during the day, temptingly revealed the best place to put a pseudo-snake."
        th "There's no way she could miss it!"
        "I laid out the carcass of the snake on the pillow, trying to curve it into as natural a pose as possible."
        "After I removed the excess grass from the pillow, the picture did become frightening."
        stop music fadeout 3
        th "Ugh, I wish I could see her face!"
        scene bg ext_house_of_dv_night with dissolve
        play ambience ambience_camp_center_night fadein 2
        play sound sfx_hiding_in_bush
        "Locking the door with the detached key, I crouched in the dark bushes across from the house, waiting for the show."
        play music music_list["eat_some_trouble"] fadein 3
        with dissolve
        "And it didn't take long for the show to come on."
        "I hadn't sat in ambush for fifteen minutes when the sleepy hum of voices was heard at the other end of the camp."
        "Alisa and Ulyana showed up at the cabin quickly, just as I thought they would. The little one whispered something in the older one's ear and galloped on down the path."
        th "Whoa!"
        th "Would our little brat really miss such a sight?"
        th "She's going to strangle herself for that later!"
        with vpunch
        "But fortunately for Ulyana, Dvachevskaya reacted quickly. A loud screech that almost made even my ears prick up was heard a moment after she flicked the switch."
        show dv scared pioneer at left
        show us normal sport at right
        with dissolve
        dv "Viper!"
        "She jumped out of the cabin like she was scalded, nearly knocking down Ulyana, who rushed to her screams."
        show dv shocked pioneer with dissolve
        dv "There's a viper in my bed!"
        "Alisa almost cried. Concerned pioneers gathered around her, warily looking under their feet, as if Alisa had declared a great invasion of snakes on the camp, not a single specimen in her cabin."
        "Only the little one dared to scout the situation. She peered cautiously into the cabin, instinctively recoiled, but still managed to force herself to examine the motionless snake."
        stop music fadeout 1
        pause(0.5)
        show us smile sport with dissolve
        play music music_7dl["genki"] fadein 3
        us "That's just a carcass!"
        us "That's the snake the new guy gutted yesterday!"
        th "Oops."
        "But I didn't think about the fact that Ulyanka knows the origin of this artifact."
        th "I think it's time to get out of here..."
        hide us
        hide dv
        with dissolve
        "Taking advantage of the fact that Alisa was distracted by the pioneers who were rushing into their cabin, eager to see the carcass, I retreated into the thicket and raced toward my cabin."
        th "A merry day awaits me tomorrow!"
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_map_shed1:
    play ambience ambience_camp_center_night fadein 2
    scene bg ext_warehouse_night_7dl with dissolve
    "I stopped and gazed into the indistinct outlines of the warehouses, barely lit by lanterns."
    dreamgirl "Why do I hear police assault music?"
    th "As if there's anything to rob here..."
    th "Wait a minute, what's even in here?"
    if not (alt_day4_me_neu_volley or counter_un_fz_mt_transit == 3):
        th "Well, apart from the dog that Slavya and Miku are hiding here."
    if alt_day1_sl_keys_took not in (1, 3):
        "Trying to peek through the keyhole at the contents of the warehouses in the pitch black was a pointless exercise."
        th "You're welcome!"
        th "I don't really need your skis and buckets!"
        "I turned and walked away."
    else:
        play sound sfx_keys_rattle
        "In the pocket of my shorts a bunch of keys jingled encouragingly."
        th "Now we'll find out!"
        if not (alt_day4_me_neu_volley or counter_un_fz_mt_transit == 3):
            "I went around to the warehouse that housed the puppy and started going through the keys to the next one after it."
        elif loki and alt_day5_me_neu_nwsppr:
            "I don't think I have time to go through all that pile of books right now, so I went around to the warehouse where Zhenya and I had unloaded the books, and started going through the keys to the next one after that."
        else:
            "I randomly chose one of the similar-looking warehouses and started going through the keys."
        play sound sfx_open_dooor_campus_1
        scene black with dissolve
        play ambience ambience_int_cabin_night fadein 2
        "Pretty soon the door clicked shut, and I peered in with interest. As expected, I didn't see a thing."
        th "Yeah... I hadn't thought of that."
        if loki:
            th "It's no big deal, though. Like anyone cares what's going on in the warehouse!"
            "I calmly flicked the switch."
        elif herc:
            "Fair enough, figuring that if anything happened I would be able to escape quickly, I found a switch on the wall."
        else:
            "I looked around, and only seeing no sources of light other than the streetlights nearby, turned on the lights."
        scene bg int_wardrobe_mirror_7dl with dissolve
        play music music_7dl["lazy_olga"] fadein 3
        "Chaos is what this warehouse looked like from the inside. Every square centimeter was covered with different colors, highlights, textures..."
        th "And this place looks like it's really fun for New Year's Eve!"
        "The carnival costumes, carelessly piled around the perimeter of the room, were clearly 'out of season' - pastel-colored snowflakes sticking out here and there."
        "As I closed the door behind me, I looked around the warehouse with an enchanted gaze, and some unknown force pulled me forward, closer to the piles of junk."
        th "Grandma's tower!"
        "Right in the middle of a shabby box of Christmas toys stuck out a forgotten artifact from the Soviet era-a clock tower on top of a Christmas tree. My grandmother once gave me one of these, and my joy that New Year's Eve was boundless."
        th "How many good memories ordinary things can give us."
        th "Would I have been as happy about any other memory of my grandmother? Hardly."
        th "But this watchtower without Grandma makes no sense either. {w} To be quite frank, it's ugly and only spoils the tree."
        dreamgirl "Should I start taking notes?"
        th "Huh?"
        "I almost dropped the ill-fated tower from my hands: an inner voice caught me off guard."
        dreamgirl "Wasn't that the abstract for your autobiography?"
        dreamgirl "{i}Semyon: the story of the man who overcame teenage hormones{/i}"
        dreamgirl "Although, no, that's not exactly accurate.."
        dreamgirl "{i}…who overcame teenage hormones with extraordinary retardation!{/i}"
        th "Hey!"
        th "I'm just getting too old for teenage hormones!"
        dreamgirl "Go on, go on, justify yourself!"
        "The inner voice chuckled. I waved my hand: arguing with it was pointless."
        scene bg int_wardrobe2_mirror_7dl with dissolve
        "I turned around and saw the cracked full-length mirror just outside the warehouse door."
        th "I wonder who broke it, and what misfortunes now haunt it?"
        dreamgirl "You, when you opened the door. Misfortunes don't haunt you, you're their middle name!"
        th "Screw you!"
        "I looked at myself in the heavily dust-covered mirror. I smoothed and ruffled my hair, straightened my tie, straightened my back, frowned, made a grimace."
        dreamgirl "Put on a beard, too!"
        th "Why, that's a thought!"
        scene bg int_wardrobe_mirror_7dl with dissolve
        "A Santa Claus costume was found in one of the canvas bags nearby. The beard was tangled in all directions, climbing up my nose and mouth and causing unbearable itching, but it looked just gorgeous."
        dreamgirl "And that pirate eyepatch over there!"
        "The blindfold turned out to be a little short for me, but with difficulty I secured it to the back of my head."
        th "Yo-ho-ho-ho!"
        th "Now I've got to find a tank top!"
        "I gutted another sack in search of something exotic."
        me "Your Highness, I brought you a dragon head!"
        "I shook the ugly mask of the unidentified reptile in front of the imaginary princess."
        "I wore cardboard knight's armor dangling, held on by nothing but honesty, and in my hand I clutched a wooden sword with a cracked handle."
        dreamgirl "Ah, what a hero you are!"
        "Beeped the inner voice, playing along with my idiotic performance."
        dreamgirl "I suppose you rescued the treasure from the dragon's cave, too?"
        me "Of course, your highness!"
        "After digging through one of the boxes, I found something that looked like a small casket."
        dreamgirl "Oh, it's my father's treasure! Open it quickly!"
        "I obediently opened the casket. Inside were three river stones of different colors and shapes."
        dreamgirl "Once upon a time my father's fiancée ordered him to bring her the three artifacts just in time, or she would order him to be beheaded."
        dreamgirl "But my father loved his fiancée so much that he was willing to run around the whole earth just to do her bidding!"
        me "Such a romantic story, my lady..."
        dreamgirl "Not at all, my hero, it is very sad."
        me "But why?"
        "The inner voice fell silent for a second, and it seemed to me as if something invisibly changed in the surroundings."
        dreamgirl "Oh no, here they come! Please go away!"
        th "Are you serious right now?"
        dreamgirl "Seriously, you dumbass! The pioneers from the campfire are coming back!"
        "Feeling inexplicably relieved that my schizophrenia had returned to normal, I hastily left my costumes and props in bags, turned off the lights, and slipped out of the warehouse."
        stop music fadeout 3
        scene black with dissolve
        pause(0.5)
        play sound sfx_close_door_1
        play ambience ambience_camp_center_night fadein 2
        scene bg ext_warehouse_night_7dl with dissolve
        "Fortunately, I had the wit to unhook the warehouse key from the bundle. I closed the door and walked slowly toward my cabin."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_map_medic_house1:
    play ambience ambience_camp_center_night fadein 1
    scene bg ext_aidpost_night with dissolve
    "The flag over the roof of the first aid post was ominously white in the darkness. After a moment's hesitation, I headed there."
    th "The infirmary is known to contain hydroperitone and analgin. I could think of some interesting things to do with them!"
    if alt_day1_sl_keys_took not in (1, 3):
        th "I wonder if Viola locks the door when she leaves."
        "It was foolish to hope otherwise: the door turned out to be locked."
        th "Well, I'll get back to that idea later."
        "I came down from the porch and walked away from the infirmary."
    else:
        "The door to the infirmary was expectedly closed, but I was extremely fortunate to have brought with me a miracle keychain to everything in this camp."
        play sound sfx_keys_rattle
        th "It's just a matter of picking the right key!"
        play sound sfx_unlock_medpunkt_door
        scene bg int_aidpost_no_light_night_7dl with dissolve
        play ambience ambience_int_cabin_night fadein 2
        "It wasn't so easy in the dark, but an endless number of attempts later, the lock clicked, and I sneakily stepped into the nurse's frighteningly quiet lair."
        play music music_list["silhouette_in_sunset"] fadein 3
        "I didn't dare turn on the light, so I lit up the screen of my smartphone, which was living its last minutes, and went through the drawers."
        dreamgirl "I wonder what she has in that nightstand over there?"
        "The nightstand did indeed look a bit foreign to the exemplary medical office interior."
        play sound sfx_open_cupboard
        "Squatting down, I turned the screen brightness to maximum and opened the nightstand door."
        dreamgirl "Mother of God!"
        "I was blinded for a second by the cold glare of the glass, but after blinking slightly, I was forced to agree with my schizophrenia."
        th "Ho{w=0.5}-ly{w=0.5} shit!"
        "The nightstand turned out to be a mini-bar, and a pretty solid one at that. Perhaps a little too substantial for a run-down provincial camp."
        th "Where did Viola get it, and with what money?"
        "It was quite obvious that outside the camp gates Dr. Viola, known for her lewd jokes, was turning into the serious and important big shot Violeta Cernovna."
        th "Except who is she really?"
        "A chill ran involuntarily down my spine."
        "I didn't want to think about anything outside the camp. It was like I'd found my comfort zone, where I could pretend like everything going on was completely normal."
        th "It's like your whole body is shielding itself from stress by focusing on what it can digest."
        th "Whether it's soap operas or other time-killers, which modern man has many times more than he can consume in a lifetime."
        th "Yes, it distracts, it masks your stress behind a screen of flying marathon series, but it doesn't get rid of it. You have to eliminate the source of the stress."
        th "In my case, not even the source is clear. I simply have nothing to hold onto!"
        th "And that uncertainty is probably what scares me the most."
        if loki:
            "My gaze slid involuntarily to the translucent bottle, which glittered more than any other."
            th "I wonder if Viola would be too upset to find it missing?"
            th "I don't think so. She's still got a full bar!"
            th "And anyway, the best for the children."
            "Putting all doubts aside, I grabbed the bottle I liked from the bar."
        elif herc:
            "The lump of anxiety that came over me made me unbearably thirsty. I looked regretfully at the luxurious contents of the mini-bar."
            "It didn't take me long to bargain with myself."
            th "Well, if I take something open..."
            "Grabbing one of the bottles, I slammed the door - out of harm's way."
        "I had portwine in my hands."
        th "It hardly resembled the slop we drank when we were students."
        th "That's lucky!"
        dreamgirl "It's not very pioneerish to bruise alone."
        th "Who do you suggest we call?"
        th "Cybernetics?"
        if alt_day5_me_neu_clubs_cyber:
            th "No, they're not bad guys, but they're definitely not drinking buddies."
        th "Slavya, so she can broom me across the square right away for suggesting that?"
        th "Why don't you go straight to the squad leader?"
        dreamgirl "Listen, that's a good idea..."
        th "No way!"
        if loki:
            th "And anyway, I found that bottle first!"
        elif herc:
            th "I'm a big boy now, and I'm independent. I can do it myself."
        play sound sfx_close_door_1
        play ambience ambience_camp_center_night fadein 2
        scene bg ext_aidpost_night with dissolve
        stop music fadeout 3
        "After extinguishing the smart screen, I went out onto the porch and locked the door."
        "It was foolish to assume that this could save me from being discovered missing, but it gave me some confidence that I wasn't leaving too much of a trail."
        "All that remained was to choose a place for cultural solitary drinking."
        th "The beach? Very cinematic, but mosquitoes are not conducive to a romantic mood."
        th "The athletic field? Those benches looked pretty good, but I didn't see Sanich on the fire, so you shouldn't go there."
        th "The square? Why, at least I'll be in Genda's company, and not like a complete alcoholic alone to bruise..."
        th "Although if I run into anyone else... to hell with it!"
        "I walked around the infirmary building, but my eye caught the ladder against the wall."
        th "Aha. Idea!"
        "Setting the ladder sturdier, I clutched the bottle under my armpit and deftly climbed to the top."
        play music music_7dl["vale"] fadein 3
        scene stars
        with dissolve
        "The roof of the infirmary overlooked the roofs of the cabins, which occasionally flashed among the treetops."
        "I opened the bottle and took the first sip."
        th "And someday these trees will be deemed an emergency hazard and cut down. The stumps will be uprooted so they don't make the children involuntarily sad about the dead trees."
        th "And maybe there won't be any children here by then. The Union will collapse, the factories will close, and the pioneer camp 'Sovyonok' will weep."
        th "Savvy entrepreneurs will either turn it into a tourist camp, or they'll settle workers here who will illegally saw the local forest."
        th "And the children who are now singing songs of friendship around the campfire will grow up, but instead of their carefree college years, they will see the collapse of everything they have considered dogma since the day they were born."
        th "And the best years of their lives will see a struggle for survival from which not all their friends and acquaintances will emerge unscathed."
        th "And maybe they themselves..."
        "I didn't want to think about that."
        "I put my hand on the bottle once more. The lanterns in the distance had already begun to blur and fade, causing a slight dizziness with their excessive brightness, and my thoughts seemed to have become softer and more malleable."
        th "It's not the right view from here after all."
        th "Why else would I feel like the whole world is upside down?"
        "I squeezed my eyes shut and easily imagined the world turning upside down. My stomach gave out a pitiful spasm at that."
        "Attempting to get my thoughts back on track was to no avail: my head felt as if it had exploded, letting all thoughts out."
        th "Here we go..."
        th "I'm losing my mind again."
        th "And I didn't even drink that much."
        "The young body I'd been given with my uniform and tie was clearly not resistant to my usual booze. But the good thought..."
        th "How am I going to get down?"
        "The ladder, on which I had great difficulty in focusing, floated away treacherously, merging with the general stream of smeared colors."
        th "I'll think about it when I want to go down, though!"
        "I tilted my head back. Staring into the starry sky was a little easier."
        th "You could imagine I was underwater."
        th "Those blurry dots are jellyfish. Or flashlight fish."
        th "If you try to look at them, they get scared and hide, leaving only their short glowing tails."
        th "All but the moon. She, the lord of this kingdom of the sea, is not going to run away anywhere."
        th "It's like she's trying to talk to me, but I don't understand her at all..."
        dreamgirl "It's not the moon, dumbass."
        stop music fadeout 3
        dreamgirl "It's the kids from the bonfire coming back!"
        th "Oops."
        scene bg ext_aidpost_night with dissolve
        "Putting the bottle along the drainpipe, I walked down the rickety ladder with unexpected dexterity, even for myself."
        th "And now, before anyone sees me..."
        play music music_7dl["viola"] fadein 3
        cs "And since when did a rock climbing club open here, pioneer?"
        show cs smile far with dspr
        "As if in slow motion, I turned to face Viola, instinctively inhaling deeply, so as not to breathe in her presence for as long as possible."
        "Because of this unsophisticated manipulation, I turned around silently - and it was a fatal mistake."
        show cs normal far with dissolve
        cs "What, you didn't even make up a story about saving a cat?"
        th "Oh, shit! That would have been the perfect excuse!"
        "Sensing something wrong, Viola stepped forward."
        show cs dontlike with dissolve
        cs "Breathe, pioneer."
        "My ears were almost smoking with embarrassment as I obediently exhaled into the nurse's twisted face."
        cs "What are we going to do with you?"
        if alt_day4_me_neu_cs_debt:
            show cs grin with dissolve
            "She suddenly hummed thoughtfully."
            cs "You know, you didn't tell anyone about our little get-together last night. That shows you're a reliable companion."
            cs "So go to bed and I didn't see you."
            th "Is she talking about cards or something?"
            dreamgirl "Buddy, you're not known for clairvoyance even sober, but now..."
        else:
            dreamgirl "Do you know what that looks like?"
            th "At the most opportune moment to bring in a flüggeheimen?"
            dreamgirl "Hey! You're taking my bread!"
            show cs serious with dissolve
            cs "I'll wait for you in my office after breakfast. Now go to bed."
            $ alt_day5_me_neu_cs_debt2 = True
        show cs normal with dissolve
        cs "Turn around and face the wall and pretend to be asleep. Olya won't notice."
        "With a barely perceptible nod, Viola turned around and walked leisurely toward the porch.{w} I couldn't think of any words of thanks, so I just raced toward home before the nurse changed her mind."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_map_boat_station1:
    play ambience ambience_boat_station_night fadein 3
    scene bg ext_boathouse_alt_night_7dl with dissolve
    play music music_7dl["carefree2"] fadein 3
    "There was a particularly beautiful view of the moon from the pier."
    th "It was as if some enchantment was at work in this place."
    if dr and counter_me_neu_answers == 1:
        th "Last time on this same pier, Lena transformed herself from a sullen and unsociable person to an open and cheerful little girl for a good hour."
        th "This time I feel like I'm not even in a watercolor sketch, but in a Disney princess cartoon!"
        th "It's as if Lena is about to emerge from behind those bushes, singing a love song..."
        th "Why Lena, though?"
    else:
        th "It's a picture I want to keep. Not as a photograph, which cannot capture a fraction of the beauty of the picture, but in its entirety, with the sounds of the night, with the cool breeze, with the rough railing of the pier."
    "I walked forward and took a closer look at the gatehouse. The lights in the windows were not on, not even from the tentative television."
    if dr and counter_me_neu_answers == 1:
        th "Why not repeat yesterday's adventure?"
    else:
        th "Why don't I play a little pirate?"
        th "Yoo-hoo-hoo!"
    dreamgirl "Did you bring oars with you in your pocket?"
    "I didn't bring oars, of course. But the boat idea seemed so tempting that I couldn't stop my imagination."
    th "I could get on the boat and pretend I was in a drive-in and watching a Tarkovsky film."
    th "That'll do for fifteen minutes!"
    "Not to say it was the best idea for entertainment for the evening, but checking out the possibility of making it technically happen became something of an unbreakable duty."
    "I chose the boat moored closer to the pier than the others, and stepped cautiously on it with one foot..."
    "…and expectedly lost my balance!" with vpunch
    th "Oh, for crying out loud!"
    "Bouncing back quickly, I looked cautiously at the ominously swaying boat."
    dreamgirl "What did you expect, going down to the boat and not holding on to anything?"
    "That remark was very valid, but instead of heeding it, I let out a wounded ego."
    th "I bet I go down in the boat off the pier without any insurance?"
    dreamgirl "What's the bet?"
    th "Nothing. Just for sport."
    dreamgirl "What's the interest in betting without a bet?"
    dreamgirl "It's like watching soccer because you like watching the ball fly across the field."
    th "Isn't that what soccer is for?"
    "The boat, meanwhile, had almost leveled out. I took in more air in my chest and began a second attempt to conquer the riverboat, feeling more and more senseless and absurd with each passing second."
    th "But that is no reason to stop what I have begun!"
    "My foot is firmly anchored in the boat. This time I had absolutely no problem keeping my balance."
    th "Now it's just a matter of gently transferring the rest of my body weight..."
    play music music_list["you_lost_me"] fadein 3
    "It all went wrong the moment I got my other foot off the pier. There was still a chance to turn back, but I didn't give credit for the sense of danger that came over me."
    "And now that there was no turning back..."
    me "Aah!"
    play sound sfx_water_emerge
    with vpunch
    "With a loud splash I flopped into the water, rattling the bow of my boat on the bow of the boat next door."
    th "A fairy-tale performance!"
    th "I think I'm going to get all ten from the judges."
    dreamgirl "When did you have time to sign up for the clown contest?"
    th "I... Hey!"
    "After catching my breath after the fall and brushing my wet hair off my forehead, I quickly assessed the situation. The water was icy, so I wanted to get out as quickly as possible."
    voice "Hey! Who's screwing around there!"
    th "You're the only thing missing to complete the picture!"
    "I swam quickly to shore, gritting my teeth and mentally cursing the awake boatman."
    "After traveling through all the coastal vegetation, my uniform was pitiful to look at."
    th "I don't care, though. There's no way I'm going to dry off in the half hour I have left before lights out."
    "I jumped out of the bushes and ran toward my cabin, squelching loudly with my wet sandals."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_map_cyber1:
    play ambience ambience_camp_center_night fadein 1
    scene bg ext_clubs_night with dissolve
    "At the doorstep of the clubhouse I stopped."
    th "And what am I supposed to do here?"
    if alt_day1_sl_keys_took in (1, 3):
        th "Steal a couple of bolts? That's a little shallow."
        th "And, to be quite frank, rather pointless."
    else:
        th "Climb on the roof? No, thank you!"
        th "Sawing down the porch step? That would be fun!"
        th "Except everything that could potentially serve as a saw is stored behind this very closed door."
    th "Well, I'd better spend my time on something more productive."
    stop ambience fadeout 3
    return

label alt_day5_me_neu_map_playground1:
    play ambience ambience_camp_center_night fadein 1
    scene bg ext_playground_night with dissolve2
    "The only thing that changed on the playground was the lighting: it wasn't a popular place during the day either."
    th "So, how about a lap to make you sleep better?"
    if alt_day5_me_neu_sport:
        th "No way! I've met my annual limit of physical exertion in one quiet hour, and I'm not going to do such disgusting things anymore!"
    else:
        th "Lazy...{w} And running around in sandals is questionable fun."
    th "I'd better look for something else to do."
    stop ambience fadeout 3
    return

label alt_day5_me_neu_map_beach1:
    play music music_list["silhouette_in_sunset"] fadein 2
    scene bg ext_beach_night with fade2
    play ambience ambience_lake_shore_night fadein 2
    "At the turn onto the beach, I stopped for a second and gazed into the darkening water surface."
    th "The water must be still warm..."
    th "Just right for a swim!"
    "I kicked off my sandals and strode forward on the cool and damp sand."
    if alt_day2_beach_seen:
        th "And why am I here so rarely?"
    else:
        th "And why didn't I go to the beach before?"
    "The quiet splash of the water split my eardrums, adapted to the silence of the night. I tossed my sandals on the sand and began to untie my tie."
    if alt_day2_beach_seen:
        dreamgirl "Just don't swim too far. There's no one here to call for help!"
    else:
        dreamgirl "I hope you at least know how to swim..."
    "I stuffed my tie in my shirt, which I rolled up into a roll, put it on my sandals, and put four folded shorts on top of it."
    if alt_day2_date == 'dv':
        th "There's hope this time no one steals my stuff and makes me walk around the camp in my underpants!"
        dreamgirl "Come on, you loved it!"
        dreamgirl "All the girls must have been staring at you when you walked past their cabins!"
        th "There's nothing funny about that!"
        dreamgirl "Nerd!"
    stop music fadeout 1
    $ alt_pause(1)
    play music music_7dl["breath_me"] fadein 3
    "A warm wave licked my fingers as I stepped close to the water. The moon's path on the dark surface seemed to invite me to step onto it and step somewhere beyond the horizon, to the place where the pictures of space from the children's encyclopedia inhabit."
    $ volume(0.5, "sound")
    play sound sfx_water_emerge
    "I entered the water easily, comparable in temperature to the air. Taking a deep breath, I pushed off and swam forward."
    $ volume(1.0, "sound")
    scene bg ext_underwater_7dl with dissolve
    "My body paddled obediently with the current, and my thoughts became a single stream, swiftly carried forward by the barely perceptible waves."
    "And a sudden calmness poured over my body, as if all my anxiety of the last few days had ceased to matter."
    "I rolled over onto my back, squared my shoulders and covered my eyes."
    th "Whatever happens always happens as it should, and only for the best."
    th "And whatever I came to this camp for, it wasn't all for nothing."
    th "After all, spending a week in a sunny land after a dank winter St. Petersburg is already a gift."
    "The moon was shining so bright that its cold light shone through my eyelids."
    th "I wonder what will happen to me next?"
    th "Maybe I'm forever stuck in the perfect version of the Soviet Union, where uniforms are strictly sized and ready to be issued at any moment, and the cutlets in the canteen consist mostly of meat."
    th "But where did I come from?"
    if alt_day4_me_neu_mt_diary or alt_day4_me_neu_us_backpack:
        th "Some unknown parents I have here."
    else:
        th "If I'm in a pioneer camp, my parents must have exiled me here."
    th "But who are they?"
    if herc:
        th "I don't think the one who is my mother here has anything in common with my deceased mother."
        th "Yes, and my stepfather isn't here either - otherwise why does everyone call me by my old last name?"
    else:
        th "Maybe this version of me doesn't even have them divorced..."
    "Frightened by the coming flood of questions, my brain began to press hard for an alternative."
    th "What if I travel to different worlds now?"
    th "We'll go to town at the end of the shift, and I'll fall asleep and wake up on another bus. And I won't be in a pioneer camp, but in a military unit."
    th "A week later, when they take us to the exercises, I'll fall asleep on the bus again and open my eyes... on the 'Moscow-Sochi' bus."
    th "On the way to a sanatorium with paid accommodation and meals..."
    dreamgirl "How quickly you get used to good things!"
    th "What else does a man need to be happy?"
    th "They feed you, they give you a bed, they entertain you, they show you beautiful pioneer girls, and it's all for free!"
    th "Sounds like heaven on earth."
    "I turned around and started paddling in the opposite direction."
    th "What if..."
    th "What if this is heaven?"
    th "I died, and now I'm going to endlessly dwell in pioneer camp, slipping around in shorts and getting a scolding from the squad leader."
    th "I must have lived a sinful life to be given such a dismal purgatory."
    th "One concert, one card tournament, one campfire. And that's in less than five days!"
    th "In normal camps, that's a one-day program!"
    dreamgirl "But how much free time!"
    th "If only there were something else to do with it..."
    stop music fadeout 3
    scene bg ext_beach_night with fade2
    "I got ashore and was immediately covered in gooseflesh."
    th "There seems to be a catch in the ascetic idea of giving up the towel: it only works when the midday sun is blazing from the sky!"
    "Gritting my teeth and hardly restraining myself from lying down on the sand and curling up, I waddled to a log in the distance and sat on it to dry off, resisting the shivers that were beating me."
    th "Night swimming is for the strong of heart, after all. Or for those who are willing to lug a pile of towels and a set of warm clothes to the beach."
    dreamgirl "Look at that, he's whining again!"
    th "I'm not whining, just talking!"
    "There was nothing to object to my split personality, so I sank into the blissful silence of the night, broken only by the splash of water and the clatter of my teeth."
    th "In any case, as soon as I leave the camp-the hastily created comfort zone will disappear, and I will have to adapt to the hostile new environment one way or another."
    th "But that's how long do I have to pretend to be a carefree person?"
    dreamgirl "Don't think about it."
    dreamgirl "Thoughts of the imminent end bring its coming closer."
    "For the first time, my schizophrenia gave me sound advice instead of lewd jokes. I was so taken aback that for a few moments all thoughts flew out of my head."
    "But I was brought to my senses by the muffled sound of a crowd of children returning from the bonfire."
    th "It's time to wrap up my evening hydrotherapy and go to bed."
    "Hastily pulling my clothes over my slightly damp body, I rushed toward the square, tying my tie as I went."
    stop ambience fadeout 3
    return

label alt_day5_me_neu_map_library1:
    scene bg ext_library_night with dissolve
    play ambience ambience_camp_center_night fadein 1
    if not (loki and counter_me_neu_answers == 1):
        "I stopped at the library."
        if alt_day1_sl_keys_took in (1, 3):
            "How about stealing a couple of volumes of Marx's writings? That would be a fun prank."
            "Too bad, of course, no one would appreciate it. Because no one would notice."
        else:
            "I'd love to put a 'don't go in, you'll die' sign on the door, but I don't think I can make one out of acorns and matches."
        "So I'll have to find something else to do."
    else:
        "I froze as soon as I saw the library."
        th "This is my chance to finish that book!"
        if alt_day5_me_neu_nwsppr:
            th "No, I'll have to go to the warehouse for that, though."
            th "Except how am I ever going to find it in that pile of bundles? It's going to take me a long time!"
            th "I guess that's not the case. And if that's the case, I don't see the point in going back to it."
            "I turned on my heel and walked away."
        else:
            play sound sfx_open_door_1
            scene bg int_library_night with dissolve
            play ambience ambience_int_cabin_night fadein 2
            play music music_7dl["deep_inside"] fadein 3
            "I picked up the key to the library in a matter of minutes. Turning on the light was going to draw unwanted attention to myself, so I armed myself with my smartphone screen turned to maximum brightness."
            th "I'll just steal the book and take it back to my cabin. I can always come up with something convincing there!"
            th "I remember exactly what I left the book..."
            th "Here."
            "I stared at the bookshelf like a sheep at a new gate, trying to figure out what had changed in just a day of my absence."
            "Not to say that I was a master at remembering all sorts of insignificant little things in the setting, but the bookshelf clearly didn't look the same as it had on my last visit to the library."
            "This shelf I remembered from the row of books with blue spines in the center of the shelf. But now that same row has moved to the lowest shelf."
            th "Looks like there's been a serious rearrangement."
            "This was also eloquently indicated by the fact that the ill-fated textbook was nowhere to be seen."
            "I sighed, trying to calm down and pull myself together."
            th "Couldn't that creep have rearranged the whole library just to make my life harder?"
            dreamgirl "How many years of teaching combinatorics..."
            th "What?"
            dreamgirl "Nothing-nothing."
            "Anyway, I had no intention of backing down from my goal. I lowered the brightness slightly to conserve energy, and began to methodically inspect the shelves."
            with dissolve
            "…"
            "It all turned out to be useless. It was as if the book had evaporated."
            th "Damn you!"
            th "Spent an hour crawling around, sniffing the dust, and I didn't find a thing!"
            scene bg ext_library_night with dissolve
            play ambience ambience_camp_center_night fadein 1
            "I wanted to knock over a couple of racks out of anger, but I forced myself to go outside and take a few breaths of fresh air to clear my head."
            th "Okay, okay. Tomorrow I'll go to the Buzzkill and make her get that book out of the ground for me!"
            "In the distance, the voices of the pioneers returning from the bonfire could be heard."
            th "It's time to think of an excuse for the squad leader..."
            th "But first it wouldn't hurt to just get out of here!"
            play sound sfx_close_door_1
            "I hurriedly locked the library door and rushed to my cabin."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_evening_answ_h:
    play ambience ambience_forest_evening fadein 3
    scene bg ext_path2_night with dissolve
    play music music_7dl["comfortable_mistery_3"] fadein 3
    th "I wonder, if the bunker is still in use, by whom exactly?"
    th "Viola?"
    "Thoughts of her luring naive pioneers who had lost their minds from the hormones that hit their heads into a dark, dark bunker and conducting totally inhumane experiments on them involuntarily popped into my head."
    dreamgirl "In a latex suit?"
    th "In a latex suit..."
    "I felt a heat rush to my ears."
    th "Oh, for fuck's sake!"
    th "The question is really important."
    "But no one I knew looked at all like a person who climbed the mines at night."
    th "Except Sanich... He sleeps all day instead of herding pioneers on the playground!"
    dreamgirl "He's got the wrong kind of build. In the event of a collapse, his chances of getting out are extremely low."
    th "Camp director, maybe?"
    "I hadn't thought about the fact that I'd never seen the headmaster before: he wasn't at the lineups, and I didn't see anyone in the canteen who looked like a big shot."
    th "In fact, it would be quite logical to assume that he was the one visiting the bunker."
    th "And that all the contents of the safe are just campy, off-limits business."
    "But this undeniably convenient version raised too many questions."
    th "For example, why the hell drag important documents to such a hard-to-reach place?"
    th "Couldn't they have put the safe right in the principal's office?"
    "Though I didn't consider myself an expert in twentieth-century household objects (much less in such details as coded safes), my gut instinct told me that that safe in the bunker was old enough for the late eighties."
    th "I can still at least somehow understand if it was used in the old camp days. Yes, it's a long walk from the office in the barracks to the bunker, but life in general back then was no picnic."
    th "But to use it to this day..."
    "My gut told me that if there was anything important in the safe, it had been there since the old camp was closed."
    th "That wouldn't be so bad, though. There's something strange about this closure."
    th "It's like something doesn't add up in all this information."
    scene bg ext_backdoor_night_7dl with dissolve
    "The camp fence loomed ahead, and I belatedly realized that I had no idea which cabin Shurik lived in."
    th "How hard could it have been to leave him in the isolation ward so he wouldn't escape?"
    th "Because he loves doing it here!"
    dreamgirl "And that's why they left him all alone in the camp? Interesting..."
    th "What are you implying?"
    "I froze for a moment at the realization: Shurik is not alone in camp."
    th "But who's guarding him?"
    "I definitely saw Viola at the fire. Olga, even more so. All the squad leaders must have been in their squads."
    "Of the adults here, only the proverbial director, the cooks, and..."
    dreamgirl "Sanich!"
    dreamgirl "I wonder if we're going to play hide-and-seek with him or play catch-up?"
    "I grimaced and cautiously stepped into the camp grounds."
    stop music fadeout 3
    pause(0.5)
    scene bg ext_houses_night_7dl with joff_l
    play ambience ambience_camp_center_night fadein 2
    "The grounds were perfectly quiet, except for the crackle of nocturnal insects, the rustle of leaves, and the distant screech of an owl. As expected, I didn't see the gym teacher walking around the gate."
    "It didn't take long to find the right cabin: it was the only one with a light on. The abode of the cyberneticists (and I was sure that the rabbit brothers shared one cabin) was located not far from the square."
    "After another look around for Sanich patrolling the area, I rushed to the cabin, jumped up on the porch, and impatiently knocked on the door."
    play sound sfx_knock_door2
    sh "Yes?"
    "Shurik responded in surprise."
    "Taking it as an invitation, I unceremoniously barged into the cabin."
    play sound sfx_open_dooor_campus_1
    scene bg int_extra_house_7dl with dissolve
    play ambience ambience_int_cabin_night fadein 2
    play music music_7dl["let_me_down"] fadein 3
    "The head of the cybernetics club was lying on the made-up bed, clutching an open book in his hands."
    me "I'm sorry to be so abrupt, but this is an important conversation."
    show sh normal pioneer at right with dspr
    "Shurik sat down on the bed and put a book on the nightstand, pages down. I sank down on the bed across from it."
    sh "Is this about the bunker?"
    "Trying not to think about what Electronik had told him about our trip, I nodded affirmatively."
    me "Did you notice anything strange about the bunker?"
    show sh serious pioneer with dissolve
    "Pulling down his glasses and nervously rubbing the bridge of his nose, Shurik stared somewhere in the direction of his neighbor's nightstand."
    sh "The size. A very small bomb shelter for a pioneer camp."
    sh "And for miners, too, if it was built for everybody at once."
    me "That's really weird. Do you think that..."
    show sh smile pioneer with dissolve
    "Shurik's glasses gleamed ominously in the dim light of the lamp."
    sh "This bomb shelter is a transit point!"
    "Even I was taken aback."
    me "Between what and what, sorry?"
    show sh normal_smile pioneer with dissolve
    "But my interlocutor didn't seem to notice my skepticism. His gaze was absolutely serious."
    sh "Between the surface and what's in the mines."
    "A chill ran down my spine - not so much from his words, but from the confidence that wafted from him."
    me "You were drawn to the mines, too? Is that why you opened the door?"
    show sh normal pioneer with dissolve
    "Shurik shook his head."
    sh "No. I opened it because I expected to see an extension of the bunker behind it."
    me "But saw the mine, yes."
    me "Don't tell me you went in to explore it!"
    sh "I didn't intend to go very far. I just wanted to see what it looked like!"
    th "He's got a bad head, that's all."
    th "He wanted to see, you see..."
    dreamgirl "Who wouldn't at his age?"
    dreamgirl "It's a real mine! It's like in the pictures!"
    me "And how did you get out of there?"
    show sh serious pioneer with dissolve
    sh "I should first explain how I got in there..."
    "With a heavy sigh, Shurik finally looked up at me."
    sh "There, in the mine, I suddenly felt like going forward. And it scared me."
    sh "I didn't understand the reason for that desire, so I started to resist and went backwards. But at that point I had gone so far into the mines that I couldn't go back to the bunker."
    sh "So I wandered through the mines until I found a strange basement. And from it were stairs to the surface."
    th "All in all, it's no surprise that there are several passages to the mine."
    th "Except that none of this clears anything up!"
    me "So, where did these stairs lead to?"
    sh "You won't believe it: right into the square."
    "I could almost physically feel my face sliding down."
    sh "And in the middle of it, too. The grating I took off was right behind Genda's pedestal."
    th "How convenient it all turns out!"
    th "Only, how often does one use this crawlspace?"
    me "What do you think it was?"
    sh "If I knew it myself!"
    show sh normal pioneer with dissolve
    "He suddenly looked me straight in the eye for the first time in our entire conversation."
    sh "Electronik couldn't resist, could he?"
    "I shook my head."
    me "It was like he was in a trance. Walking along, unresponsive to light and voice."
    show sh upset pioneer with dissolve
    "Shurik frowned even harder and began to study the boardwalk mosaic on the floor again."
    sh "See, that's just mystical! I can't find a scientific explanation for it!"
    "His shoulders slumped down."
    th "Yeeeah, I went to clear the situation up alright..."
    "I had to do something to distract Shurik, who was immersed in thoughts of a strange entity beckoning pioneers to him."
    me "And yet, on the subject of the bunker..."
    show sh normal pioneer with dissolve
    sh "Sergei was talking about your military devices."
    "The bespectacled man said in a perfectly calm tone, but he fidgeted nervously on the bed."
    me "They're not military!"
    me "And what makes you think there's more than one? I only showed Syroezhkin one smart!"
    show sh surprise pioneer with dissolve
    sh "Smart?"
    th "Ugh!"
    me "Smart reader. An e-book reader."
    show sh normal pioneer with dissolve
    "The word I invented sounded delusional, but solid and convincing. Except that Shurik still looked at me with suspicion."
    sh "Can I see it?"
    "After a second's hesitation, I still handed the phone to the future luminary of Soviet science."
    show sh serious pioneer with dissolve
    "Shurik looked at the smartphone long, closely, and with great interest. He even took a flashlight out of the depths of his nightstand to examine all the connectors."
    sh "Hmm..."
    "The cybernetic turned off the flashlight and stared at the extinguished smartphone screen again."
    sh "You're not going to tell me how you got it, are you?"
    me "Sorry, but I can't."
    sh "I would assume that whoever gave it to you is a PCR."
    th "What the hell is that?"
    show sh normal pioneer with dissolve
    "But no sooner had I opened my mouth than Shurik perked up."
    sh "The bonfire is over."
    "Indeed, the voices of the children returning to their homes could be heard more and more clearly from behind the window."
    hide sh with dissolve
    "I got out of bed. As much as I wanted to get anything more out of Shurik, I should have gotten out of here before Electronik returned."
    "But just at the door, I turned around."
    show sh normal pioneer at right with dspr
    me "Do you know what year they closed the old camp?"
    sh "Seventy-fourth."
    me "Thanks, buddy. Good night."
    scene bg ext_houses_night_7dl with dissolve
    play ambience ambience_camp_center_night fadein 2
    "I slipped out the door and hurried to my cabin. I had to think hard about what I'd heard."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_evening_answ_l:
    play ambience ambience_forest_evening fadein 3
    scene bg ext_path2_night with dissolve
    play music music_7dl["ofrust"] fadein 3
    th "It's great to have you all here today..."
    th "There's hope I can find something before lights out!"
    "During the day I managed to remember a conversation with my own schizophrenia about documents. And something told me that my papers in the infirmary should be quite interesting."
    "It got dark in the woods, and I could hardly make out the path beneath my feet."
    th "Ehhh, I should have made myself a torch before I went into the woods... How do you start a level again in this RPG?"
    dreamgirl "Yay, we're about to die!"
    th "Why should we?"
    dreamgirl "We'll fall into a hole or something blindly. Or we'll get lost and go live in the woods, and we won't be able to get food and we'll starve to death..."
    th "Oh, don't make a big deal out of it!"
    dreamgirl "And mind you, we're not even a group of girls from a sports camp whose bus fell off a mountain. We won't have anything to eat at all!"
    th "Since when do you speak for us?"
    dreamgirl "My survival instincts speak for me. They tell you to rally if you're lost in the woods."
    show bg ext_path_night with dissolve
    th "We are not lost!"
    "The moon peeking out from behind the clouds was proof of that: in its light the path to the camp was clearly visible."
    th "It's hard not to notice the place where a herd of children walked..."
    scene bg ext_backdoor_night_7dl with dissolve
    play ambience ambience_int_cabin_night fadein 2
    $ alt_pause(1.2)
    scene bg ext_houses_night_7dl with dissolve
    play ambience ambience_camp_center_night fadein 2
    "It took much less time to reach camp alone than the same distance in formation."
    th "Another proof that during any evacuation one should ignore all instructions and rush to the exit at full speed!"
    "The deserted area of the camp looked eerie in the light of the dim lanterns. I looked around just in case and hurried to the infirmary."
    scene bg ext_aidpost_night with dissolve
    "It took a while to find the keys. The task seemed impossible in the pitch black, but after an endless number of attempts, the lock clicked, letting me in."
    play sound sfx_unlock_medpunkt_door
    scene bg int_aidpost_no_light_night_7dl with dissolve
    "It was dangerous to turn on the lights, but I couldn't see anything at all, so I had to forget about the conspiracy."
    scene bg int_aidpost_night with dissolve
    stop music fadeout 3
    th "Except where does she keep her pioneer documents?"
    play sound sfx_open_cupboard
    play music music_7dl["unsettling"] fadein 3
    "I jerked open the first drawer, but it contained swollen medical journals. The second revealed the inventory logs."
    "I squinted cautiously at the compartment with the keyhole in the desk, and opened the third drawer."
    th "Now that looks like what I need!"
    "I flipped through the thin books, trying to figure out what pattern they were arranged in. The alphabetical version fell apart quickly, so I pulled some cards from the farthest row."
    th "Syroezhkin, Feoktistova... it's getting close!"
    "I grabbed another medical card and involuntarily flinched as I turned it over."
    "{i}Persunov Semyon Semyonovich{/i}"
    "{i}May 4, 1972.{/i}"
    th "Well, no, it certainly has nothing to do with me. I was born in…"
    th "This year, which in itself sounds wild. The birthday mismatch is just the cherry on the cake."
    "I chuckled nervously, suppressing the panic in me, and examined the medical card carefully. There was indecipherable writing at the bottom, and it clearly wasn't supposed to be there."
    "{i}Under the personal supervision of Collider V.C.{/i}"
    th "What?!"
    "It made me uncomfortable to think that I was being watched the whole time. And given the specific behavior of our nurse..."
    "I began frantically leafing through the card, but then my hand involuntarily hovered, gripping the pages tightly."
    "It was about what I expected, though I didn't fully understand it."
    th "{i}PCR syndrome{/i}, in the same broad medical handwriting on my medical records."
    "The puzzle in my head was beginning to take shape."
    th "What a fool I am!"
    th "The phone, the player... anachronisms in this deeply soviet era. And I brought them into this world."
    th "Some PCR brought tamagotchi technology about ten years ago. It couldn't have come from that time in any other way!"
    th "And in my medical records it says «PCR syndrome». What a miraculous coincidence!"
    th "So she knows who I am?"
    dreamgirl "Also, this affliction has a name. Know what I mean?"
    th "Is this... normal?"
    th "It's not just happening to me?"
    "That thought made me breathe a little easier. On the one hand, the embarrassing revelation of my unsuccessful attempts to behave as normally as possible did not add to my spirits. On the other, if doctors are aware of such cases..."
    "I leaned over my medical records, trying to pick out just a little more information."
    th "My blood type is the same as mine, but the Rh factor doesn't match..."
    "The journal almost fell out of my hands."
    th "It wasn't me!"
    "The silence in the infirmary was beginning to weigh on me. I inhaled noisily, realizing that I hadn't done it since a good minute."
    th "All right, take it easy."
    th "Gotta weigh it all up and think it over. So, what do I have at this point?"
    th "There are people called PCRs. They bring all sorts of contrived gimmicks from the future, and the locals take them out and copy them."
    th "And I fit that definition pretty damn well, as documented in my medical records."
    th "But then why didn't they rip me off?"
    th "Why does everybody pretend I'm a regular pioneer and not a big-headed stump who showed up from the future?"
    "I imagined the smiles of Slavya, Miku, and Ulyana, the grunts of Olga, the grimaces of Alisa, the timid nods of Lena..."
    th "Did they really know who they were dealing with all this time?"
    th "They knew, but they kept smiling and nodding and making faces!"
    "It was hard to believe. I could understand Slavya's pretense, Miku's pretense, but Alisa and Ulyana certainly didn't seem like people capable of playing the part for long."
    th "Yes, the redheads would have published a volume of jokes about hapless time travelers on the first day and recited it during every trip to the canteen!"
    "With a heavy sigh, I stared at the records again, hoping to find something else entertaining."
    play sound sfx_open_door_1
    show cs dontlike at fleft with dissolve
    play music music_7dl["sorrow"] fadein 3
    "The sound of the door opening made me jump up like a scalded man."
    cs "I don't remember leaving a deputy in my place before I went."
    "Viola's tone was icy, but I was already too numb to react."
    "The nurse slid her gaze over the medical records I was still clutching in my hands, and understanding flashed in her eyes."
    me "Violetta Cernovna..."
    show cs serious with dissolve
    cs "All your questions later, pioneer. After mine."
    cs "In the meantime, I have a casualty to deal with."
    hide cs with dissolve
    "She helped the curly-haired boy from Ulyana's friends up on the porch and waddled to the couch."
    th "Honestly, I don't give a damn about that kid!"
    me "No, you explain it to me!"
    me "What is this body? Where did it come from? Why don't he and I have the same blood type?"
    show cs angry at fleft with dissolve
    "I jumped up from Viola's chair, where I had been sitting motionless the whole time. She slowly turned to me and looked at me in a way that made me feel three heads below her."
    cs "Sit where you were sitting and wait exactly two minutes."
    show cs normal with dissolve
    "Viola sat the boy on the couch and leaned over the medicine box. The boy gave me the occasional concerned look, but remained silent."
    "Once again I sank back into the chair and stared unseeingly at the ajar door to the isolation room."
    th "If they don't answer my questions now, I'll give them hell!"
    th "I will not be fed any more lies and endless evasions. I've got facts on my hands that you can't just turn your back on!"
    "I waited patiently for Viola's designated two minutes to pass. She still fiddled with the medicine box, never once speaking to the boy on the couch."
    me "Time is running out, Violetta Cernovna."
    show cs grin with dissolve
    cs "And I'm just about ready."
    show cs grin at center with dissolve
    pause(0.5)
    show cs grin close with dspr
    with flash_red
    pause(0.5)
    "She pulled up the sleeve of my shirt with a quick movement and stuck the syringe into the top of my shoulder. I flinched, but I couldn't get a word out of surprise."
    show cs serious close with dissolve
    cs "If you twitch, the needle will break and stay inside. It's not a pleasant experience, I don't recommend it."
    th "Is this the end?"
    "My shoulder whined painfully, and I sat there, unable to move."
    show cs normal with dissolve
    cs "Now sit down. If you get dizzy, go to the isolation ward and lie down."
    show cs normal at fleft with dissolve
    cs "Okay, pioneer, show me your leg."
    hide cs with dissolve
    "Viola seemed to have lost interest in me. It was the perfect excuse to escape, but I had nowhere to run."
    th "The whole camp administration will be on Viola's side, which means they are the enemy. There's no point in going to them for help."
    th "And the stuff she injected me with, there's no way to get it out."
    play sound_loop sfx_head_heartbeat
    "The world began to blur a little. One part of me was panicking and searching for a way out of the situation, while the other part was accepting of what was happening."
    th "Oh, shit..."
    $ renpy.show("bg int_aidpost_night", what = Grayed("bg int_aidpost_night"))
    with guess_on
    "My body suddenly became sluggish, infirm. I felt how physically difficult it was to remain in a sitting position."
    th "To bed. But how can I sleep when all around are enemies?"
    "Behind the ajar door of the isolation room, the headboard of the bed gleamed invitingly."
    th "Though enemies must sleep, too..."
    show blink
    $ alt_pause(1.0)
    "I blinked and felt my eyelids unwilling to reopen."
    cs "Come, pioneer."
    "Viola jerked me out of my chair and led me somewhere. I was already struggling to keep my eyes from crashing into the walls."
    cs "Lie down. I'll give you a blanket without bedding, so you don't get your clothes dirty for nothing."
    "Viola's voice came from somewhere far away."
    "I fell into a blissful and pleasant sleep, but a disturbing thought still tried to break through the tranquilizer veil in my head:"
    th "What will happen to me next?"
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_evening_answ_d:
    play music music_7dl["deep_inside"] fadein 3
    play ambience ambience_forest_night fadein 3
    scene bg ext_path2_night with dissolve
    "As expected, no one noticed me leaving."
    th "Well, at least I got away. The rest is nothing."
    dreamgirl "What, even the night forest where you can't see a thing?"
    "It really was a most unpleasant circumstance. I slowed down so I wouldn't inadvertently turn off the barely visible path."
    th "Oh, well, we didn't have long to walk to the fire glade. So there's just no place for me to get lost before I get to camp!"
    dreamgirl "And the bears? You think a crowd of pioneers didn't wake them up?"
    th "Don't be ridiculous. Where would bears come from?"
    dreamgirl "From the woods, of course."
    dreamgirl "They're very fond of settling next to military units or campgrounds so they can steal provisions from them. What makes a camp any less attractive?"
    th "There are children here. No one would let wild animals near a place where children live."
    dreamgirl "Comfort yourself."
    "A nasty giggle from my schizophrenic self. I twitched and staggered forward."
    "But the self-influence had already set in motion the processes of perceptual distortion. In the silence of the night I heard, now and then, heavy footsteps, hoarse breathing, and muffled growls."
    "Each time I just shuddered and continued on my way, stubbornly looking under my feet."
    play sound sfx_owl_far
    "But when the distinctly non-phantom owl whooshing sounded in the distance, I froze in a stupor."
    $ renpy.show("bg ext_path2_night", what = Dawn("bg ext_path2_night"))
    with dissolve

    "As if owls were to be feared. And it was not at all about the recently rewatched «Twin Peaks»."
    "It was like it was a signal that I had to run off at full speed to save someone."
    th "Then why aren't my legs listening to me?"
    $ volume(0.5, "sound")
    play sound sfx_7dl["white_noise"] fadein 4
    $ renpy.show("bg ext_path2_night", what = Desat("bg ext_path2_night"))
    with dissolve
    th "Why can't I move, but I can only look... {w}look and feel my helplessness!"
    dreamgirl "Buddy, wake up!"
    scene bg ext_path2_night with dissolve
    "I opened my eyes and realized that I had settled down on the damp and cold path. A large shiver was beating me."
    "It was reminiscent of the seizures I suffered a few years ago."
    show prologue_dream with dissolve
    $ volume(1.0, "sound")
    "Seizures, when my body was numb, my heart was heavy, my legs were shaking, my hands were trembling, and my head was torn from the inside out."
    "During one of these attacks, a strange voice spoke in my head for the first time."
    dreamgirl "Buddy, wake up!"
    "I raised crying eyes to the long extinguished monitor."
    dreamgirl "Come back to reality!"
    hide prologue_dream with dissolve
    dreamgirl "Come back to reality!"
    th "It's all right. {w}I'm here."
    "After somehow shaking off the wet sand from my shorts, I continued on my way to camp."
    scene bg ext_backdoor_night_7dl with dissolve
    "I entered the territory cautiously, frightened of every shadow."
    "On the one hand, all the pioneers and their counselors were sitting on the bonfire. On the other, I had absolutely no recollection of whether the same Sanich was with them."
    "Or the camp director. There must be a director here, right?"
    "The thought that flashed through my head threw me into a stupor."
    th "What if right now someone is going through the cabins to check on them?"
    dreamgirl "You're so paranoid!"
    dreamgirl "They confiscated all the vodka from the pioneers on the day of arrival. There's nothing to check."
    play ambience ambience_camp_center_night fadein 2
    scene bg ext_houses_night_7dl with touch
    "It was hard to argue with schizophrenia. I looked around and hurried toward Lena's cabin, trying to avoid the streetlight."
    th "Not that I was full of hope of finding anything interesting there, but I have no other ideas!"
    th "Lena herself is not very contactable, her surroundings are of no use..."
    dreamgirl "But her underwear is sure to be very informative!"
    th "I don't care about her underwear!"
    scene bg ext_house_of_un_night_7dl with touch
    "I stood outside Lena's cabin, frantically fumbling with my trembling hands for the keys. I heard the phantom heavy footsteps again, in which my frightened brain identified the gym teacher this time."
    "And this time it was much scarier..."
    play sound sfx_open_dooor_campus_2
    scene bg int_house_of_un_night with touch
    play ambience ambience_int_cabin_night fadein 2
    $ volume(1.1, 'ambience')
    stop music fadeout 3
    "Another key clicked into the keyhole. I pulled the doorknob, feeling how much my palms were sweating."
    "Half of Lena wasn't too hard to identify. Whereas Miku's half was a real chaos, with things covering every available surface, Lena's was an order of magnitude smaller, and laying as neatly as possible."
    "It was mostly sketchbooks. Among them lay orphaned the book she had been reading on the square the day I came to camp - «Gone with the Wind»."
    th "I wonder if it's a library book, or did Lena bring it with her?"
    th "Wait, why am I even thinking about this?"
    "It was scary to turn on the light, so with a sigh I crushed the toad that was strangling me, unlocked my smartphone, and turned up the brightness to illuminate myself with the screen."
    play music music_7dl["devastated"] fadein 5
    play ambience ambience_int_cabin_night
    "The albums all looked the same, and only one looked a little more shabby than the others. The paint was frayed in places, and the pages looked a little too swollen."
    th "That's where we'll start!"
    "This album, as it might have seemed, Lena devoted herself entirely to portraits."
    "On the sheets flashed girls in school uniforms, frozen in easy and graceful poses. Occasionally they were diluted with adult faces, none other than teachers."
    "The pictures in the album suddenly changed. From silhouettes hanging in the air, they suddenly became full-fledged narrative sketches."
    "Green, sunshine, serene blue skies and bright red patches of pioneer ties."
    "Lena came to camp."
    "The portrait reappeared. It was a beautiful girl unfamiliar to me, holding a banner."
    th "It must be a scrapbook from last shift!"
    "I peeled back a few pages and only confirmed my hunch. The girls in the drawings - probably classmates - looked a year or two younger than Lena."
    "But at some point the colors disappeared from the album. The landscapes, shaded in simple pencil, looked bleak, as if before an impending storm."
    "One page had been torn out, as evidenced by the jagged edge sticking out between two sheets."
    "And from the next page, a girl who looked a lot like Lena was looking at me."
    if alt_day4_me_neu_mz_newspaper:
        "The same girl I saw in her scrapbook at the library."
    th "Could it be her sister?"
    "The girl in the drawing looked sad, and the picture itself was executed in twitchy, thick strokes."
    "It was as if Lena wanted to finish this drawing as soon as possible."
    "And I knew how much she hated such drawings."
    "Even though I didn't know how I knew that at all."
    "I turned another page, and my heart skipped a beat."
    play sound sfx_head_heartbeat
    "The picture returned colors, albeit in barely discernible watercolor strokes. Even a simple layman like me could see how much soul had gone into this work - it was evident in every stroke of the pencil, in every stroke of the brush."
    "On a large flat rock in the woods sat a pioneer with his elbows in his knees and his eyes staring off to the side. And that pioneer looked just like me."
    th "Maybe she only continued to draw in that sketchbook now."
    th "Lena might have abandoned it just after the drawing she hated..."
    th "Okay, stop! Why did she suddenly decide to draw me in the first place?!"
    "I studied the drawing again, hoping to discover my own mistake, but there could be no mistake: the drawing was either me or my twin brother lost as a child."
    th "Even if she drew it on this shift - doesn't one have to pose for that kind of work?"
    "Even the expression on the pioneer's face in the drawing added to the questions. I could never have imagined myself with that expression."
    "It certainly never belonged to me."
    "I was about to turn the page, when suddenly a tiny inscription in the corner of the sheet with either my portrait or not my portrait caught my eye."
    "{i}24.07.88{/i}"
    "For a good minute I drilled this date with my eyes, trying to comprehend what I saw."
    "And then, like a blinding flash, the memory of this morning flashed through my mind."
    show bg int_musclub_rain_7dl
    show dv grin pioneer at cright
    show prologue_dream
    with dissolve
    dv "Come on, remember, you fool!"
    dv "A bench near the gate. Winter."
    dv "This year's winter shift. Farewell disco."
    scene bg int_house_of_un_night with dissolve
    th "Alisa didn't confuse me with anyone else. She really saw me."
    th "But why don't I remember anything about it?"
    th "And why this “me” doesn't look like me at all?"
    "I closed the album and put it back."
    th "It's decided: tomorrow I'll go up to Lena and ask her directly if we've seen each other before."
    th "I don't think she'd hide it if she knew I was remembering something..."
    "The muffled voices of the pioneers could be heard from the street."
    th "Gotta get out of here!"
    "I ran around the room in a panic, rushed to the window and tried to open it, but at the last moment I decided it wasn't too late to just sneak out the door."
    stop music fadeout 3
    play sound sfx_open_door_1
    "But the door swung open before I could reach it."
    mi "Senya?"
    show mi surprise pioneer with dissolve
    "Miku looked at me in surprise, clapping her eyes incomprehensibly."
    me "And here I am..."
    th "Really, what am I here?"
    dreamgirl "Planned to sell the star's underwear to speculators!"
    show mi dontlike pioneer with dissolve
    "The realization came to Miku abruptly. In a second, the Japanese girl stretched out in a string and clenched her fists angrily."
    mi "You! You climbed into the girls' cabin, you pervert!"
    mi "Senya, I was sure you weren't like that, but you..."
    "In my brain I knew that from the outside it looked exactly the way Miku described, but my inner resentment demanded that we dot our I's and cross our T's."
    me "Miku, understand, I'm here because of Lena!"
    play sound sfx_angry_ulyana
    show mi angry pioneer with dissolve
    mi "Because of Lena?"
    "The girl seemed to be getting worked up. Her nostrils flared dangerously, and her eyebrows almost closed on the bridge of her nose."
    mi "And you think I won't stand up for my friend?"
    show mi rage pioneer at cleft with move
    "Miku stepped to the side and pointed to the door in a picture. A sense of shame barely allowed me to move, but I moved toward the exit as fast as I could."
    mi "And don't you dare go near Lena!"
    play sound sfx_close_door_1
    scene bg ext_house_of_un_night_7dl at zentercenter
    play ambience ambience_camp_center_night fadein 2
    show un sad pioneer close
    with dissolve
    pause(0.3)
    "But I couldn't fulfill this demand of Miku's: I slammed the door behind me and came face to face with Lena."
    th "Has she been standing here the whole time?"
    dreamgirl "Had every right to. This is the porch of her cabin, by the way!"
    $ volume(0.4, "music")
    play music music_7dl["clonidine"] fadein 3
    me "Lena, I..."
    th "Am very sorry?"
    th "Acted like an asshole?"
    th "Still don't know where I've seen you?"
    show un serious pioneer close with dspr

    "Lena looked up at me, and I couldn't bear to look at her."

    "Her gaze was direct, judgmental, and very, very disappointed."
    $ renpy.show("bg ext_house_of_un_night_7dl", at_list = [sdl_transform7], what = SS_com("bg ext_house_of_un_night_7dl"))
    "That painful needle finally ripped the crust off a long forgotten and festering wound, letting all the pain out at once."
    pause(0.6)
    scene bg ext_city_night_7dl with flash
    pause(0.6)
    $ volume(0.9, "music")
    play ambience ambience_7dl["rain"] fadein 3
    play sound sfx_7dl["grom"] fadein 1
    show rain_overlay with flash
    $ alt_pause(1.2)
    $ volume(1.2, 'ambience')
    $ set_mode_nvl()
    "There's still the screeching of the brakes in my ears. {w}I'm on my knees in the rain and I'm afraid to look up."
    "The ambulance came five minutes ago, and I don't want to hear their medical report."
    th "If I don't hear it, it won't be true."
    th "If I don't see her again, I can live as if nothing happened."
    th "I'll just stand here and watch the water run down the flashing emergency headlights."
    "But they stick a cotton ball with smelling salts under my nose and ask me something loudly. {w}Somebody grabs me under the arms and lifts me up."
    "I can feel where they are taking me, and my whole gut is screaming, aching, demanding me to turn and run immediately. {w}But alas, my basic reaction to stress is 'freeze.'"
    "My passport is torn from my stiffened fingers, the policewoman tries to find out who I was to her, and my world has narrowed to a single purple stain spreading across a white sheet."
    "The paramedic is smoking, wrapped in his raincoat, his partner shouting something into his cell phone."
    "They don't save her. {w}They covered her with a sheet."
    "My Lena. {w}The Lena I didn't save."
    "Who I forgot so I wouldn't accidentally picture her disappointed and judgmental face and put my hands on myself."
    $ set_mode_adv()
    stop music fadeout 3
    stop ambience fadeout 2
    $ volume(1.0, 'ambience')
    $ volume(1.0, "music")
    scene black with dissolve
    $ alt_pause(3.5)
    play ambience ambience_camp_center_night fadein 2
    un "Semyon!"
    show bg ext_house_of_un_night_7dl
    show un shocked pioneer
    with dissolve
    play music music_7dl["sorrow"] fadein 3
    "I opened my eyes, coming back to reality. My body was sprawled out on the steps, and breathing was very difficult."
    un "Are you okay? Do you need to be taken to the infirmary?"
    me "I'm fine."
    "I mumbled, gingerly rising to my feet."
    me "I'm just dizzy."
    show un sad pioneer with dissolve
    "Lena looked at me incredulously."
    un "But you were squirming all over... Shaking..."
    un "I thought you were having an epileptic fit!"
    "I couldn't look at Lena like before. {w}I couldn't look at her any other way."
    th "She looked just like her!"
    th "And that pioneer in her album... A copy of me?"
    "Unable to lift my eyes to the girl again, I nodded and turned away."
    hide un with dissolve
    me "Good night."
    "I literally ran toward the cabin in the vain hope that my exuberant thoughts would not catch up with me."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_map_fail:
    scene bg ext_houses_night_7dl with dissolve
    play music music_7dl["unfulfilled"] fadein 2
    play ambience ambience_camp_center_night fadein 3
    "Deciding not to press my luck anymore, I sighed heavily and staggered back to the cabin."
    "And what had I ever hoped for? That the deserted night camp would turn out to be an amusement park?"
    "I looked wistfully at the dark and lifeless barrels without the bright yellow light in the windows and shook my head."
    "What a big room of horrors, indeed. But the range of scarecrows here is poor: they didn't even bring a creepy clown..."
    dreamgirl "What do you mean they haven't brought it in? He arrived five days ago!"
    th "Oh, they forgot to ask you!"
    dreamgirl "Chill out, man."
    dreamgirl "I'm certainly sorry for your wasted evening, but it's not my fault you're in trouble."
    th "You are one of my troubles!"
    dreamgirl "Or perhaps you are one of mine?"
    th "No, Mr. Black King, I don't buy your tales!"
    scene bg ext_house_of_mt_night_without_light with fade
    play ambience ambience_camp_center_night fadein 1
    play sound sfx_open_dooor_campus_1
    "I swung open the door to my cabin and froze on the porch in indecision."
    th "Wouldn't it be better to hole up in the bushes and blend in inconspicuously with the others when they returned?"
    th "What would be the point of that, though? Olga will probably count everyone before she chases the units back to camp."
    stop ambience fadeout 3
    $ alt_pause(1)
    scene bg int_house_of_mt_night2 with fade
    play ambience ambience_int_cabin_night fadein 1
    "Finding these excuses quite convincing, I went into my lodgings and collapsed exhausted on my bed without even turning on the light."
    th "It's eben a day, huh..."
    "I didn't feel like thinking about it, though, as if my psyche was still digesting an unusually large volume of impressions."
    "Smart was still showing signs of life, so I was tucked away in one of a dozen unread books, not even intending to retain what I'd read in my head."
    stop ambience fadeout 3
    stop music fadeout 3
    return

label alt_day5_me_neu_sleeptime_map:
    scene bg int_house_of_mt_night2 with fade
    play ambience ambience_int_cabin_night fadein 1
    if alt_day5_me_neu_map_points < 3:
        "Olga burst into the cabin and flicked the switch, just as I was about to fall on the bed."
    else:
        "Pretty soon the muffled voices of the pioneers could be heard in the distance."
        th "That was fast, though. The mosquitoes must have eaten them."
        "But I wasn't happy for long: an enraged Olga flew into the cabin, turning on the lights."
    play music music_list["awakening_power"] fadein 3
    play sound sfx_open_door_kick
    scene bg int_house_of_mt_night with dissolve
    show mt angry pioneer with dspr
    mt "And what do you call that?"
    me "Ah?"
    "I stretched out in a sleepy voice."
    "I couldn't think of anything cleverer to say than a headache, so I decided to play the drowsy, uncomprehending sufferer."
    if alt_day5_me_neu_candle_escape:
        dreamgirl "How believable! Second headache of the day."
        dreamgirl "Not unless it's from an overabundance of oxygen and an acute lack of gray matter for a normal excuse."
    if alt_day5_me_neu_map_ivent == 'dv':
        mt "Beh!"
        mt "What the hell did you do in Alisa's cabin?"
        me "Where?"
        show mt rage pioneer with dspr
        "The effort with which Olga restrained herself from giving the most obvious answer was evident to the naked eye."
        mt "So you don't know why she's running all over the camp screaming that she's going to kill you?"
        if lp_dv < 0:
            me "Well, we don't get along very well..."
        elif lp_dv < 5:
            me "I have no idea. We don't talk to her that often, so I haven't yet grasped all the subtleties of her soul."
        else:   
            me "Oh, don't mind that, it's just a friendly prank."
        show mt normal pioneer with dspr
        "Olga frowned and gave me an attentive look. I rubbed my eyes with a silly expression, convincingly (in my opinion) playing off the sudden awakening."
        mt "All right, you can figure it out for yourselves then."
        th "That's it?"
        "I looked at the leader in disbelief, stopping my act in a moment."
        th "So she doesn't know about the snake?"
        dreamgirl "So you can turn in the little one later? Keep your pocket wide!"
        "That was reassuring - at least now there was only one side to wait for the blow."
        show mt angry pioneer with dspr
        mt "And don't make such a happy face: I'm still waiting for the story of why you left the bonfire."
    else:
        show mt angry pioneer with dspr
        mt "You went AWOL from the campfire! Alone! Through the dark woods!"
        mt "What kind of antics are these, Semyon?"
    play music music_list["silhouette_in_sunset"] fadein 3
    "I lowered my head guiltily: in our short acquaintance with Olga, I had learned that this gesture inevitably led to an early pardon."
    me "The smoke gave me a headache. I went to the path to get some fresh air, but it didn't get any better."
    me "So I decided to go to camp and lie down."
    show mt sad pioneer with dspr
    mt "Couldn't you have warned someone?"
    mt "Even Violetta Zernovna - she had analgin with her."
    th "Wow, they were getting ready for this trip!"
    th "I hope someone also brought a backpack with canned food. Just in case."
    me "I hadn't thought of that..."
    dreamgirl "Oh, now that sounds plausible!"
    mt "Consider this my last warning about your arbitrary behavior. Next time, be kind enough to let me know of all your movements."
    th "Does that mean I have to go to the bathroom, too?"
    "But all I said out loud was:"
    me "I'm sorry, it won't happen again!"
    dreamgirl "That's true. We'll do better next time!"
    show mt angry pioneer far with dspr
    "Olga pressed her lips together angrily, but did not continue her lecture. She turned and stepped toward the door."
    mt "I'm on my rounds. You have five minutes to wash your face and go to bed."
    mt "Time's up!"
    stop music fadeout 3
    hide mt with dissolve
    if alt_day5_me_neu_map_points < 3:
        th "That's lucky, of course. She's in a good mood, isn't she?"
        if alt_day5_me_neu_map_ivent == 'dv':
            th "Although a vendetta from the redheads would be far scarier than anything the lady leader could come up with..."
    else:
        "I didn't think I deserved even this reprimand, but the feeling of relief still came in a relaxing wave as soon as the squad leader left the cabin."
    scene cg d1_end_of_day_7dl with dissolve
    "Deciding not to waste time, I rushed to the washbasins, hastily brushed my teeth, threw off my Pioneer uniform, and climbed into bed."
    th "Or else our Olenka's mood will change..."
    show blink
    "I was half-asleep when the squad leader returned. And judging by the fact that after that I fell into a deep sleep, her mood had not changed."
    stop ambience fadeout 3
    return

label alt_day5_me_neu_sleeptime_answ_d:
    scene
    $ renpy.show("anim prolog_5", what = Desat1("bg ext_houses_night_7dl"))
    with fade
    show anim_grain
    play music music_7dl["snatch"] fadein 3
    "I walked to my cabin without knowing the way."
    th "Lena.{w} Lena.{w} Lena."
    th "Lena..."
    "My classmate.{w} My friend.{w} My sharp knife in my heart, my stone in my soul, my main nightmare."
    th "I scream in my sleep because I didn't manage to utter a sound that day."
    th "Because no matter how much my mind runs from it, the unconscious rising from its depths scrolls the sheet-covered body on the pavement time after time as the weakened mind breaks through the shroud of sleep."
    $ alt_pause(1)
    $ renpy.show("bg ext_house_of_mt_night_without_light", what = Desat("bg ext_house_of_mt_night_without_light"))
    with dissolve
    $ alt_pause(1)
    $ renpy.show("bg int_house_of_mt_night2", what = Notch("bg int_house_of_mt_night2"))
    with dissolve
    "Without turning on the lights or undressing, I collapsed on the made bed."
    show un normal pioneer tr1 with dissolve
    th "But then why is she here? Is it a reincarnation?"
    th "A lot of things can be written off as that, like that drawing in her scrapbook, dated eighty-eight."
    hide un with dissolve
    th "But Alisa? I didn't know anyone like her!"
    th "Yes, and she remembers me being at this camp, not some mythical event in St. Petersburg where we might have inadvertently crossed paths."
    th "This is all completely abnormal!"
    th "Although my being in this camp, come to think of it, is not what you might call normal either..."
    $ renpy.show("bg int_house_of_mt_night", what = Desat("bg int_house_of_mt_night"))
    show mt angry pioneer
    with dissolve
    "I didn't even notice the squad leader come into the cabin until she flicked the switch."
    mt "Do you want to explain yourself?"
    me "I don't feel well."
    "I threw up, hearing my voice as if through thick water."
    show mt shocked pioneer with dissolve
    "I obviously didn't look good, because Olga's face instantly changed."
    mt "What's going on with you?"
    me "Dizzy. Nauseous. There's a strange feeling that what's going on around me is unreal."
    dreamgirl "Are you an idiot?"
    dreamgirl "You're about to be taken away by a psychiatric ambulance!"
    th "I could use one. My head is about to split open from all the things I've realized!"
    "However, I couldn't tell you exactly what I realized yet."
    show mt sad pioneer with dissolve
    mt "Please close your eyes, breathe in slowly, and count to ten."
    show blink
    "Her voice sounded frightened but firm. I rolled over onto my back, obediently closed my eyes, and inhaled."
    th "One… two… three…"
    stop music fadeout 3
    scene bg int_house_of_mt_night
    show unblink
    show mt scared pioneer behind unblink
    with dissolve
    play ambience ambience_int_cabin_night fadein 1
    pause(0.3)
    "When I opened my eyes, the world around me almost stopped muddying."
    play music music_7dl["exodus"] fadein 3
    show mt sad pioneer with dissolve
    mt "I'll go get Viola. Don't worry, I won't be long!"
    mt "In the meantime, lie still and try to breathe steady."
    mt "Shall I turn off the light?"
    "I shook my head as hard as I could."
    hide mt with dissolve
    play sound sfx_close_door_1
    th "In the darkness, the pictures in my head seem to be more real. It's as if they manage to trick the brain when it's deprived of one of its senses, and pretend to be real."
    th "It's as if this whole camp is my fantasy, just to avoid seeing the rain-soaked street of London again, where the slender streams of the waves are disfigured by a blurring red stain."
    th "But this Lena... she's real!"
    th "She's still matchmaking me to her friends, still thinks that no inhibitions are in order if you really want to, still draws, still with the same silly ponytails..."
    th "But then who died in my arms in London?"
    play sound sfx_open_dooor_campus_1
    show cs serious with dissolve
    "The door swung open again."
    cs "Bad, pioneer?"
    "Her tone was not at all as mocking as usual."
    cs "Pioneer? Can you hear me?"
    me "Yes. I'm conscious. It's just..."
    show cs serious close with dissolve
    cs "Don't worry. You just need to sleep."
    pause(0.2)
    with flash_red
    pause(0.5)
    $ renpy.show("bg int_house_of_mt_night", what = Desat1("bg int_house_of_mt_night"))
    with dissolve
    "She pulled up the sleeve of my shirt and stabbed a syringe in my shoulder."
    show cs serious close at left
    show mt sad pioneer close at right
    with dissolve
    mt "Another early exit is the last thing we need now…"
    show cs normal close with dissolve
    cs "Don't be so nervous, Olya. The guy's fine, just a little emotional turmoil."
    th "A little!"
    show blink
    "The tranquilizer worked quickly. Thoughts were still whirling around in my skull, but my consciousness was drifting farther and farther away from them."
    "It was as if it were falling smoothly into an endless sea gorge, sinking into absolute darkness."
    dreamgirl "You're here, man. You're in camp."
    dreamgirl "Just remember you're here."
    th "I'm here..."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_me_neu_sleeptime_answ_h:
    scene bg ext_house_of_mt_night_without_light with fade
    play ambience ambience_camp_center_night fadein 1
    play sound sfx_open_dooor_campus_1
    $ alt_pause(1)
    scene bg int_house_of_mt_night with fade
    play ambience ambience_int_cabin_night fadein 1
    play music music_7dl["sky_feather"] fadein 3
    "I slumped into the cabin and turned on the light purely out of inertia, not concentrating on the action. My thoughts were spinning feverishly in my head, not wanting to make a logical progression."
    "Sinking down on the bed, I pressed my shoulder blades into the wall and closed my eyes."
    show blink
    th "So access to the bunker from the camp is a lot easier than I thought."
    th "That makes it much more likely that the safe holds something relevant and explanatory..."
    th "Wait, what is it supposed to explain anyway?"
    dreamgirl "At least the fact that the bunker exists."
    dreamgirl "Maybe there's information in there about why Syroezhkin was mooning and the bespectacled man was getting out of the mines all night."
    th "Except, what's in it for me? How does it explain my getting into this camp?"
    scene bg int_house_of_mt_night2
    show unblink
    "I opened my eyes and stared at one of the posters above Olga's bed."
    th "Though if there's something fishy going on with this whole camp, who knows?"
    th "Maybe my getting in had something to do with that mystical entity that summons the pioneers to the mines?"
    "The only hope was that my idiotic assumption with the code might have been correct."
    th "Everybody likes simple passwords..."
    play music music_list["revenga"] fadein 3
    play sound sfx_open_door_kick
    scene bg int_house_of_mt_night with dissolve
    show mt angry pioneer with dspr
    "The door swung open unexpectedly, causing me to jump out of bed."
    mt "And what was that, Semyon?"
    th "Yes, it was silly to expect her to walk in with a happy smile, whispering: 'Coo-coo! There's our Semyon!'"
    me "Excuse me. I found out Shurik was alone in camp, so I thought I'd keep him company."
    me "I should have asked you to leave first."
    show mt rage pioneer with dspr
    mt "Yes, you should have!"
    "She stared at me menacingly, as if contemplating whether to execute me or pardon me."
    mt "Don't you think you've been leaving events too often for the company of your friends?"
    mt "I'm very glad you two are getting along, but you can't be friends at the expense of squad cohesion!"
    "I lowered my head guiltily, feeling inferior to my squad leader."
    th "What kind of friendship is there!"
    th "More like collective meddling in trouble at our leisure."
    stop music fadeout 4
    me "I'm sorry. It won't happen again."
    show mt angry pioneer with dissolve
    mt "I hope so!"
    show mt normal pioneer with dissolve
    mt "Go wash your face and go to bed. And just try to keep anyone company on the way!"
    scene bg ext_house_of_mt_night_without_light with fade
    play music music_7dl["lth"] fadein 3
    play ambience ambience_camp_center_night fadein 1
    "Olga went out, and I took the soap and followed."
    th "I'll go to the bunker first thing tomorrow. And if the safe doesn't work out..."
    scene bg ext_washstand_night_7dl with dissolve
    "I rinsed my mouth and straightened up over the washbasin, staring sullenly into nowhere."
    th "...then I'll be sure to find another way to find out what the hell is going on in this camp!"
    scene bg int_house_of_mt_night2 with joff_l
    "After turning out the light, I unmade the bed and started to take off my uniform."
    th "I'll go out after breakfast. I hope I get some sleep..."
    stop music fadeout 4
    $ renpy.show("bg int_house_of_mt_night", what = Notch("bg int_house_of_mt_night2"))
    with dissolve
    "But contrary to my expectations, I fell asleep almost as soon as my head touched the pillow."
    stop ambience fadeout 3
    return

label alt_day5_me_neu_sleeptime_drunk:
    scene
    $ renpy.show("bg ext_house_of_mt_night_without_light", what = Noir("bg ext_house_of_mt_night_without_light", -0.2))
    with fade
    show anim_grain
    play music music_7dl["ambience_safe"] fadein 3
    play ambience ambience_camp_center_night fadein 1
    play sound sfx_open_dooor_campus_1
    $ alt_pause(1)
    $ renpy.show("bg int_house_of_mt_night2", what = Noir("bg int_house_of_mt_night2", 0))
    with fade
    play ambience ambience_int_cabin_night fadein 1
    "Random alone knows how and by what means I reached the cabin. The portwine had robbed me of my ability to orient myself adequately in time and space."
    th "And my short-term memory has been affected, too..."
    $ renpy.show("cg d1_end_of_day_7dl", what = Noir("cg d1_end_of_day_7dl", -0.2))
    with dissolve
    "I thought, lying in bed without the slightest idea of how I ended up in it."
    pause(0.3)
    $ renpy.show("cg d1_end_of_day_7dl", what = Rained("cg d1_end_of_day_7dl"))
    with touch
    pause(0.3)
    $ renpy.show("cg d1_end_of_day_7dl", what = Noir("cg d1_end_of_day_7dl", -0.2))
    with touch
    "I rolled over onto my back and immediately regretted it, because the beveled ceiling instantly floated, as if it was about to collapse on me."
    th "So, what was Viola saying?"
    th "Turn to the wall?"
    "I curled up and tried to get as close to the wall as possible, but I was moving with the bed for some reason, and I didn't pay attention to the nasty creaking right away."
    dreamgirl "The pioneers passing by must be thrilled!"
    "Finally I tucked my nose into the worn wallpaper and tried to steady my breathing."
    play sound sfx_open_dooor_campus_1
    pause(0.5)
    "The sound of the door opening sounded as if through the water column, and even the light on didn't bother me in the least."
    mt "Semyon!"
    mt "Violeta Cernovna said you got sick at the bonfire. Are you all right?"
    th "So, Viola advised me not to answer her..."
    with vpunch
    mt "Semyon?"
    "The touch on my shoulder didn't make me flinch only because my brain was too drunk to process such little things and trigger unconscious reactions."
    "I tried to breathe evenly, but not enough to keep Olga from smelling the alcoholic ombré. She wasn't going to sit with me for long, though."
    "The light in the cabin went off, and the door slammed again."
    th "Viola got me off the hook?"
    if alt_day4_me_neu_cs_debt:
        th "That's what card debt means!"
        dreamgirl "But it's you who owes it, not her!"
        th "I pay it by my silence!"
    else:
        th "Apparently, she just vitally needs my help tomorrow..."
        dreamgirl "I wonder what she's missing in this boring place with a predominantly female staff..."
        th "Hussars, silence!"
    scene black with fade
    "I pulled myself up, snuggled my face into the pillow, and closed my eyes blissfully."
    th "The main thing is not to accidentally roll over onto my back before the leader falls asleep..."
    stop ambience fadeout 3
    stop music fadeout 3
    return

label alt_day5_me_neu_sleeptime_wet:
    scene bg ext_house_of_mt_night_without_light with fade
    play ambience ambience_camp_center_night fadein 1
    play music music_7dl["melancholy_sun"] fadein 3
    "I got to the cabin in a bit of a chill."
    th "Yeah, it's not a good time for a swim."
    th "Neither is the place. The cold springs, damn it!"
    stop ambience fadeout 3
    play sound sfx_open_dooor_campus_1
    $ alt_pause(1)
    scene bg int_house_of_mt_night2 with fade
    play ambience ambience_int_cabin_night fadein 1
    "Relieved to shed my clammy, cold sandals, I stepped onto the cold planks of the evening and made my way to my abode, leaving wet footprints behind me."
    "The sandals will dry in the morning in the sun.{w} I'll hang my clothes on the chaise longue-if another unscheduled rain doesn't fall, I'll have something to wear to the ruler."
    "The wet knot of my tie gave way with difficulty, and my wet shirt fell to the floor, followed by my water-weighed shorts."
    th "Great, now just hang this stuff up and..."
    dreamgirl "Have you decided to stay kidneyless or give the little one a lavish joke topic for the rest of the shift?"
    th "And really..."
    with dissolve
    "The last piece of clothing flew to the floor, and only then did I feel like an idiot in the extreme."
    th "I wonder if Olga will run away on her own, or will she put me in another cabin?"
    dreamgirl "Yeah, she'll give me a sheet to cover my shame and send me to the other end of the camp."
    dreamgirl "All the girls at the farewell disco are yours!"
    "I somehow wiped myself with an official towel, brushed the wet hair off my forehead, and wrapped the same towel around my waist."
    th "Well, at least now you can get out before people come up..."
    dreamgirl "What was embarrassing you before? There wasn't a soul around!"
    th "What if there's a gym teacher in the bushes?"
    dreamgirl "You make it sound like something bad."
    "The noise of the crowd returning from camp caught up with me immediately as I rested my tie on the back of the chaise longue. I flew into the cabin, hastily dismantled the bed, and dove into bed, pulling the blanket up to my chin."
    th "Maybe you'll get away with it."
    th "Just in case Olga was so run over from the day she wouldn't even notice my shape on the chaise longue?"
    "There was little hope: I'd escaped the fire as it was, for which I certainly wasn't going to be patted on the head."
    "But life, as always, had prepared the worst-case scenario for me."
    play music music_list["glimmering_coals"] fadein 3
    mt "Semyon!"
    play sound sfx_open_door_kick
    scene bg int_house_of_mt_night with dissolve
    show mt angry pioneer with dspr
    "Olga almost pulled the door off its hinges, and her instinct for self-preservation whimpered pitifully, demanding that she immediately hide with her head under the blanket."
    mt "Before I approached the cabin, I still had hope that the boatman had mistaken some boy from Katerina's troop for my pioneer!"
    show mt rage pioneer with dspr
    mt "But you!"
    "I felt myself unknowingly pulling the blanket higher and higher. The angry look from the squad leader made my eyes run desperately for escape from imminent punishment."
    th "And what am I going to tell her?"
    th "That I argued with my schizophrenia?"
    dreamgirl "And also, mind you, lost that bet!"
    "Olga was silent for a minute, waiting for my reaction."
    me "Yes I..."
    if herc:
        me "My bad, I did something stupid. It won't happen again."
        th "...comrade senior squad leader!"
    elif loki:
        me "You are..."
        me "You've got it all wrong!"
    else:
        me "Sorry. It was an accident..."
    mt "You should at least get out of bed when you talk to your elders!"
    "I glanced cautiously at Olga, distinctly feeling my face turn red."
    th "Doesn't she realize that I'm..."
    dreamgirl "What if she understands perfectly well?"
    if counter_mt_7dl < 5:
        th "That's even worse!"
    else:
        th "You think that'll please her?"
    "With a sigh, I sat up on the bed, still holding the blanket."
    me "I'd love to, Olga Dmitrievna, except that the party didn't issue me a spare set of underwear."
    show mt surprise pioneer with dspr
    "Now it was the leader's turn to blush."
    mt "Alright, sit down..."
    "She turned away and pretended that she was suddenly extremely interested in a sock sticking out of the closet. However, Olga pulled herself together quickly."
    show mt normal pioneer with dspr
    mt "Where were we?"
    play music music_list["silhouette_in_sunset"] fadein 3
    show mt angry pioneer with dspr
    mt "Ah yes, on your antics!"
    dreamgirl "Didn't we stop on your underwear?"
    mt "Well, I've had enough!"
    if alt_day5_me_neu_candle_escape:
        mt "Walked out of a squad event without telling anyone!"
    if alt_day5_me_neu_clubs_cyber:
        mt "Stole a shovel from the warehouse to make fun of kids!"
    mt "Went outside the camp without permission, and he took Ulyana along!"
    th "Who took who!"
    show mt rage pioneer with dspr
    mt "Ran away from an all-camp activity and walked alone through the night woods!"
    mt "You've been fooling around at the boathouse!"
    mt "What if you go down with angina tomorrow?"
    "The probability of that happening was non-zero, so I was horrified to imagine the rest of my shift in Viola's company."
    th "Eh, I'd rather drown myself!"
    me "I'm fine! I'm not even cold!"
    show mt angry pioneer with dspr
    "The squad leader gave me a stern look and a threatening sneer."
    mt "I hope so, because tomorrow you're on cafeteria duty!"
    if alt_day3_duty:
        th "What, again?"
        th "I peel potatoes there more often than Ulyana now!"
    show mt normal pioneer with dspr
    mt "Now go to sleep - it's been five minutes since lights out!"
    stop music fadeout 3
    scene bg int_house_of_mt_night2 with dissolve
    "She flicked the switch and left me alone."
    th "It was an amazing day! And how it ended..."
    scene cg d1_end_of_day_7dl with dissolve
    "Thinking in advance of the early wake-up, I rolled over and tucked my nose into my pillow."
    th "Oh, well. Who knows if I'll still come down with angina..."
    stop ambience fadeout 3
    return

label alt_day5_me_neu_sleeptime:
    scene bg ext_square_night with dissolve
    play music music_list["a_promise_from_distant_days_v2"] fadein 2
    play ambience ambience_camp_center_night fadein 3
    "By the time we reached the camp, it was already deep night."
    "Dark, alive."
    "As it is only in the south."
    "And the whole time we were walking, I couldn't help thinking that with every step I was casting a shadow over the past of the unfulfilled."
    "It was as if I had done something mundane instead of doing something useful and important."
    stop ambience fadeout 3
    "And yet, still..."
    scene bg ext_house_of_mt_night_without_light with fade
    play ambience ambience_camp_center_night fadein 1
    "I had a little more time before Olga finished her rounds."
    stop ambience fadeout 3
    play sound sfx_open_dooor_campus_1
    $ alt_pause(1)
    scene bg int_house_of_mt_night with fade
    play ambience ambience_int_cabin_night fadein 1
    "Everything here was the same."
    "Kettles, thermoses, Olga's laundry hanging on the back."
    if (counter_mt_7dl >= 7) and (alt_day5_me_neu_mt_voyeur != 0):
        "And the diary."
        if not alt_day4_me_neu_mt_diary:
            th "Mmm, it was a lot easier to hold back last time."
            "I closed my eyes and forcibly forced myself to look away."
        if persistent.mt_7dl_good:
            menu:
                "Go read the diary":
                    $ alt_day5_me_neu_mt_diary = True
                "Wait for the squad leader at the porch":
                    $ alt_day5_me_neu_mt_hentai = True
        else:
            $ alt_day5_me_neu_mt_diary = True
        return
    "I undressed, feeling displeased that I smelled smoke all over the place."
    th "All right, tomorrow's the last day, you can't breathe before you die, we'll wash and shave and put on clean clothes like before a fight."
    "In the meantime..."
    play sound sfx_click_2
    scene bg int_house_of_mt_night2 with fade
    "Guté nacht, camp."
    scene cg d1_end_of_day_7dl with dissolve
    "Silently sending an unprintable word to the ceiling, I closed my eyes and relaxed."
    if alt_day5_me_neu_sl_voyeur:
        "And as I was about to fall asleep, I heard the door creak open and a squad leader walk in."
        mt "Sem?"
        me "U?"
        "Sleepily I asked."
        mt "So will you tell me where and why you and Ulyanka went?"
        "Wasn't surprised at how she figured us out."
        "I wasn't surprised anymore."
        "And, yawning widely, he said:"
        me "We... mmm... followed Slavya."
        mt "Really? Why?"
        if counter_us_7dl <= 4:
            me "This... mmm... Information is secret."
            "Olga laughed softly."
            mt "Okay. Go to sleep, secret agent."
            "She tucked me in with a blanket and walked out of the cabin."
        else:
            $ volume (0.5,'music')
            $ volume (0.5,'ambience')
            menu:
                "We wanted to know where she went":
                    $ volume (0.9,'music')
                    $ volume (0.9,'ambience')
                    "Olga laughed softly."
                    mt "Curious Varvara... All right, go to sleep."
                    "I completely agreed with her and in a few seconds I was asleep."
                "We thought she had a guy there":
                    $ volume (0.9,'music')
                    $ volume (0.9,'ambience')
                    mt "Yes? And when did you realize it wasn't like that?"
                    me "When she started taking her clothes off."
                    "Olga laughed out loud."
                    "Really, immediately she covered her mouth and shut up."
                    mt "Okay, go to sleep."
                    "The offer was extremely constructive, and I gladly took it."
                    $ counter_us_7dl += 1
    return

label alt_day5_me_neu_mt_retrib:
    scene bg int_house_of_mt_night with dissolve
    if alt_day4_me_neu_mt_diary:
        $ counter_mt_7dl += 1
    else:
        $ counter_mt_7dl -= 2
    "The pull was at the level of an irresistible order."
    play sound sfx_open_dooor_campus_1
    "Just in case, I shut the door tightly and sat down to read."
    $ set_mode_nvl()
    play music music_7dl["take_my_hand"] fadein 3
    $ alt_pause(3)
    "{b}June 10th, 1987{/b}"
    "Hello again, old, but no longer kind, acquaintance."
    "Sometimes I feel like throwing you away as the thing that reminds me of most of my troubles."
    "Or foolishness."
    "Ran almost ahead of the locomotive, rushing to camp."
    "Ran, fool."
    "And he didn't come."
    "Even though he promised."
    "Bastard!"
    "{i}The page is dripped with ink.{/i}"
    "It's good that Slavya unloads me a little."
    "It's a pity she's only here for one shift."
    nvl clear
    $ alt_pause(3)
    "{b}July 5th, 1987{/b}"
    "Saw off the old shift, picked up the new one."
    "Nothing interesting."
    "The kids are rolling away to a state of total stoicism."
    "But my heart is still empty."
    "He never came."
    nvl clear
    $ alt_pause(3)
    "{b}July 16th, 1987{/b}"
    "He's arrived! He's here! Hooray!!!"
    "{b}July 16th, 1987. Added in the evening.{/b}"
    "And... he didn't recognize me."
    "He did it on purpose? Right?"
    "Only the fact that there were kids looking at us kept me from wanting to throw a tantrum on him there, too."
    nvl clear
    $ alt_pause(3)
    "{b}July 20th, 1987{/b}"
    "Trying to have a heart-to-heart talk only led to more awkwardness."
    "He really doesn't remember anything."
    "Nightmare."
    nvl clear
    $ alt_pause(3)
    "{b}July 23rd, 1987{/b}"
    "Parents asked me to look after their offspring for a week in town."
    "I put him up in my apartment for the duration of the shift, no harm done."
    nvl clear
    $ alt_pause(3)
    "{b}August 4th, 1987{/b}"
    "Parted amicably, promising to see each other at the end of the year."
    "He'll be able to afford it!"
    "I rode back to camp with a heavy heart."
    nvl clear
    $ alt_pause(3)
    "{b}January 1st, 1988{/b}"
    "From what I understand, he never arrives on time."
    "So I didn't even bother."
    "I met him at the gate while the camp slept off after the festivities."
    "We're together again. I think it's great!"
    nvl clear
    $ alt_pause(3)
    "{b}January 9th, 1988{/b}"
    "As we drove back, we figured out how we wouldn't lose our memories."
    "Of funny incidents: in the third squad someone got so sick that we had to move the pioneer girl from there to the only available seat."
    "To our bus."
    "It's not hard to guess who exactly was transferred. Ulyanka, of course."
    "A seat was found next to Alisa from the second one, and with a heavy heart I put Ulyana next to her, expecting a fight or bullying."
    "But... From there all the way there was laughter and some lively negotiation."
    "I think I've made a big friendship for someone. Great."
    nvl clear
    $ alt_pause(3)
    "{b}June 7th, 1988{/b}"
    "I only write here when I'm at camp."
    "The rest of the time, it's like I forget the diary exists."
    "Although it can be sad in the fall and spring."
    "But I can always plunge into work and forget everything."
    "Luckily, this time it looks like I won't have to spend as much time on chores."
    "I wonder if he'll be here next shift."
    "Also, Aliska the Accident came in with Ulyana."
    "I still laugh about how 'wild' she came in the winter."
    "Nightmare and horror!"
    "Alisa... What can you do?"
    "What's more, she doesn't seem to be interested in anyone but Tikhonova and Sidorova."
    nvl clear
    $ alt_pause(3)
    "{b}July 16th, 1988{/b}"
    "You can't change the place."
    "And again he's late for his shift."
    "And once again the people I wanted him to meet are leaving camp!"
    nvl clear
    $ alt_pause(3)
    "{b}July 20th, 1988{/b}"
    "Parents' Day."
    "I'm in no hurry to get closer."
    "Again he doesn't remember me, and my arms are tired of gluing my heart together."
    nvl clear
    $ alt_pause(3)
    "{b}July 22nd, 1988{/b}"
    "He asked me to dance and complained that his head was a mess."
    "He'd swear he remembered me, but..."
    "It seems like what he and I were doing back then on the bus - it's working!"
    "He calls it by some strange word, either 'durdu' or 'dordu' and giggles like a lunatic."
    "But at least some of our memories together have been saved and preserved."
    "Let him pay so much attention to that quiet girl from the second squad."
    "After the dance we went to my cabin."
    "He turned out to be all grown up."
    "God, his kiss makes me dizzy."
    "Don't freak out! Remember, I'm a squad leader, he's a pioneer, seven years apart!"
    nvl clear
    $ alt_pause(3)
    "{b}July 23rd, 1988{/b}"
    "Departing again."
    "His father asked to take his son in again."
    "My God, what kind of family do they have there that they can't meet their son from camp?"
    "But I don't feel sorry."
    "It may not be as I thought it would be."
    "There's a lot of unneeded secrets around here..."
    "With that memory you're an invalid. How can you make a scene of jealousy to someone who won't even remember you in six months?"
    "I don't know."
    nvl clear
    $ alt_pause(3)
    "{b}January 1st, 1989{/b}"
    "I met the New Year alone."
    "In the company of Georgian tea and oatmeal cookies."
    "New Year's Eve is dismissed at two in the morning, but I left at midnight, fusing all my duties to Nyutka."
    "It's good for her, let her have her fun."
    "And I had to get up at nine to meet the Mercedes, which is inappropriate in our village."
    "And him."
    "His family seems to be getting more and more prosperous."
    "If only they wouldn't spoil my boy."
    nvl clear
    $ alt_pause(3)
    "{b}January 9th, 1989{/b}"
    "The old 'durdo,' it turns out, was called 'Durden'. Tyler Durden - I think my Syomich had encountered something like that once before."
    "That's why, apparently, he agreed."
    "Is it right to say that we gave the boy a split personality?"
    "But now he does remember me."
    "It's the same old promises, promises..."
    "And I know I'll be alone again, and I'll be thinking about nothing in an empty apartment."
    "I can't wait for summer!"
    nvl clear
    stop music fadeout 3
    $ set_mode_adv()
    "Over my shoulder someone sighed."
    "And I looked up painfully slowly."
    show mt sad pioneer with dspr
    "Olga looked strangely quiet and depressed."
    mt "You have no self-respect at all, do you?"
    "So much so that I froze, for some reason continuing to hold the suddenly slippery diary book in my hands."
    "My thoughts flashed, tossing up pictures of reprisals, one scarier than the next."
    "Most tangibly, for some reason, the hammer under the bed and something to do with the bathhouse appeared."
    show mt normal pioneer with dspr
    mt "Put other people's things back from where you took them."
    "Still in the same unbearably even voice she continued."
    "It would have been foolish to fight in such a situation, so I did as she commanded."
    mt "It's a good thing you don't have anything here."
    "I misunderstood what the squad leader said."
    "And she added something that made my chest sharply cold:"
    mt "You'll move out sooner."
    me "But... But..."
    if (not herc) and (not alt_day3_technoquest2):
        mt "Shurik is in the hospital now anyway. {w}You'll stay with Electronik."
    else:
        mt "Shurik will still be in the infirmary until we leave. {w}You'll stay with Electronik."
    "In a kind of stupor over the lack of reprisals, I nodded mechanically, rolled out my winter clothes mechanically, and unloaded the contents of my pockets."
    "I couldn't shake the thought that something irreparable was happening."
    "And now might be a good time to fumble for a red or blue line on the dialogue wheel and give an over-the-top speech about how worried I was about her or something like that."
    "Somewhere out there this thought turned a few times, formed and got under my heart: I like Olga!"
    th "Extremely like her! Something has to be done, you can't leave it all on a note like that!"
    "I have gathered air in my chest:"
    me "Olga Dmitrievna, I've wanted to tell you for a long time that..."
    show mt smile pioneer with dspr
    mt "You don't have to say anything now."
    "She shook her head."
    mt "Go to bed. Tell Electronik I put you in Shurik's place."
    "And quickly, quickly kicked me out the door. I didn't even have time to add anything."
    stop ambience fadeout 3
    play sound sfx_open_dooor_campus_1
    $ alt_pause(1)
    scene bg ext_houses_night_7dl with dissolve
    play sound sfx_close_door_campus_1
    "The strange thing is that all the time Olga has been trying to sandbag me, she's been doing it somehow... through force or something?"
    "As if she should, supposedly, but didn't want to?"
    "Anyway, I dutifully went to the Electronik's dwelling."
    return

label alt_day5_me_neu_mt_tea_party:
    scene bg int_house_of_mt_night with dissolve
    play music music_7dl["neon_fever"] fadein 3
    if (alt_day2_date == 'mt'):
        "My actions completely copied me from a sample of myself three days ago."
        $ counter_mt_7dl += 2
    else:
        "I acted as if on a hunch."
    "Simple logic, simple understanding of the order of things."
    "The jar should be in the nightstand, with the boiling pot next to it."
    "A square tin box of tea on the next shelf, next door to glasses in tin cup holders."
    "For some minutes, while one very pretty girl races her wards around the camp, wiping unsolicited longing from her eyes."
    "And I don't know how to comfort her, or say the right thing."
    "But I can pour tea and smile."
    "Perhaps that's what she needs?"
    stop ambience fadeout 3
    scene bg ext_house_of_mt_night
    show mt sad pioneer at zenterleft
    with dissolve
    mt "Sitting?"
    "Tiredly she muttered."
    "She looked dejected and pensive."
    if alt_day4_me_neu_date == 'mt':
        "Just like yesterday, when I found her."
    "Walking, hunched over, hands down - completely exhausted."
    "Maybe she just needs someone she'll always meet in the same place and once again tell herself the world is still solid and hasn't gone crazy."
    "She sank heavily onto the step beside me, lowering her head onto the carefully tucked pillow I'd already dragged away from the chaise lounge."
    hide mt with dissolve
    mt "Would it be an abuse of power if I asked you to massage my shoulders?"
    "Looking nowhere, she inquired."
    "I froze."
    "In spite of how close we'd started to get over the last few days, there was still a certain chain of command between us."
    "And now I'm offered not to give a damn about her."
    "To wave my hand - and perhaps never again be able to go back to where it all started."
    "Besides, massaging a girl's shoulders..."
    "I gingerly lowered my palms to her shoulders and, squeezing a little, moved them in different directions."
    mt "Harder."
    "Without opening her eyes, Olga said."
    "I squeezed a little harder."
    mt "Sem Semych, I know very well the power with which you can massage shoulders."
    mt "Don't be lazy."
    me "But then you have to turn around."
    mt "Yeah?"
    "The girl opened her eyes and straightened up on the step next to me."
    "Our eyes were flush."
    mt "Like this?"
    "I was paralyzed again."
    mt "Or..."
    "She smelled like a campfire, half-weathered perfume, the natural scent of skin, maddening."
    "And her eyes were bottomless, like the sky above our heads. Witchy."
    "It's well known - to fall endlessly into the abyss you must take the first step."
    "Even if someone pushes you in the back to do it."
    "Even if..."
    "Soft lips, soooooooft."
    play sound sfx_open_door_kick
    $ alt_pause(1)
    scene bg int_house_of_mt_night2
    "Olga kissed me frantically, then grabbed me and pulled me into the cabin."
    "And as soon as the doors slammed shut behind us, shirts and ties fell to the floor... And all this without interrupting the greedy, hot kisses, as if getting to know each other all over again after a long separation."
    "Olga turned out to be a very sturdy girl; now, embracing her, I realized that despite all her laziness, her figure was precisely athletic."
    "And so I had no trouble picking her up in my arms and taking a few steps toward the bed."
    "In the darkness I could only navigate by my sense of memory and space, and it did not fail - two steps later I lowered the precious cargo onto my bed."
    "There was a soft squeak of armor netting, a soft shriek from the girl as I unmistakably found the thin strip of cloth and ran my fingers under it."
    "Pulled it down as she undid her own bra."
    "For a moment, the moon peeked through the window, bringing out of the darkness a sight worthy of any artist's brush - a beautiful girl responsive to my touch."
    if alt_day5_me_neu_mt_voyeur == 2:
        mt "And what's more, how you sniffed, how you sniffed."
        "The girl giggled."
        mt "Like now."
    mt "I know you're allergic to latex and rubber, so you know what to do."
    me "What?"
    mt "I'm on a cycle, I'm not allowed. Do you understand?"
    me "Whatever you say."
    "It was silly to refer as 'you' someone you'd just undressed and were about to bring to orgasm."
    "I had to talk her out of it before she spread her legs slightly apart, finally letting me into the holy of holies."
    "And that's where my lips immediately went."
    "Where, it turns out, I'd been striving for all the time I'd been living next to her."
    "She twitched and moaned softly as I ran my tongue over her for the first time."
    mt "How I missed it, Lord..."
    "She exhaled, pulling me close to her."
    "Opening everything towards me, as if trying to absorb the caresses I generously dispensed."
    "One minute... One more... Until her tart taste was replaced by a slightly different, astringent one."
    "And the tongue I teased her with as I went inside was as deep as I had ever managed before."
    "A short cramp ran down the slender legs around my neck, and an incomprehensible mooing came from somewhere above."
    "Olga grasped my pillow with her teeth and fought the urge to moan with all her might. Or scream. Or I don't know."
    "She was getting up on the bridge and trying to get away from me."
    "But where there. Not today."
    "Today she's completely at my mercy."
    "Today..."
    "Before I could think, I was pulled up, pulling down my shorts in between."
    mt "Inside…"
    me "What?"
    mt "Enter…"
    me "But…"
    mt "Enter me."
    "The squad leader roared at my incomprehension."
    mt "COME ON! FUCK ME!"
    th "What the fuck."
    "Well, you don't have to ask me twice."
    "By this point I was so horny I was going to smoke if she roused me a bit more."
    mt "Just ah-careful!"
    "I was instantly at the entrance and, meeting almost no resistance, rushed inside."
    "Narrow. Elastic. Sweet."
    "That's where I've been going the whole time I've been here."
    "I picked up a very fast pace right away - Olga cried out and wrapped her legs and arms around me, trying to wiggle."
    mt "Only you..."
    "She seemed to be trying to remind me of something."
    "I didn't remember what."
    "And I didn't care. The girl smelled lust, she wanted me. And I wanted her."
    "So a few seconds later, when her body was riddled with orgasm again and I was squeezed so hard it almost ripped off the most important part, I loosened my grip."
    "And discharged."
    "A million volts through my spine, happy sobs and an incredible feeling of pressure down my belly."
    "For a few seconds I stayed in that position, fervently breathing, until she clapped me on the shoulder and tried to pull me down."
    mt "I told you - not in me."
    mt "Do you even understand the risk?"
    "The risk? Oh, the risk I understood."
    "Because the withering libido had flared up again."
    "And I, at first timidly and then with more and more desire, moved inside her."
    "Olga moaned, but somehow unconvincingly."
    "It was as if we had been waiting for this for so long."
    "And then, finally."
    "Her scent made me dizzy, and intimacy, even up close, in the way that's possible between two loving people, wasn't enough."
    "It didn't spoil the mood even that I showed myself to be the ultimate self-lover, thinking only of my own pleasure."
    stop music fadeout 3
    scene black with fade
    $ alt_pause(1)
    scene bg ext_houses_night_7dl
    with dissolve
    "It was already three in the morning when I went to sleep at another house, yielding to this woman's strange demand."
    "I was a little shaky from fatigue and lavishly distributed strength, but I was still smiling stupidly and happily."
    "Be that as it may."
    me "I'm needed."
    "With one lip I said."
    "And pushed open the door to the cabin."
    return

label alt_day7_me_neu_bad:
    play music music_7dl["seven_summer_days"] fadein 3
    scene
    $ renpy.show("bg ext_camp_entrance_day", what = Grayed("bg ext_camp_entrance_day"))
    show anim_grain
    with dissolve
    play ambience ambience_camp_entrance_day fadein 3
    if loki:
        "Well, I stayed true to myself."
        "And my reality became exactly what I had worked so hard to create."
        "And so I got the reality... {w} that I deserved."
    elif herc:
        "The story didn't start and end the way I wanted it to."
        "But that's a familiar phenomenon to me."
        "No, I didn't end up a fatalist, but I had no choice but to go with the flow."
        "At the speeds life flashed past me, clinging to the banks was useless - it would tear my limbs out by the roots."
    else:
        "I close my eyes and have that dream again."
        "I've been dreaming it for so long, it's become such a familiar part..."
        "that I couldn't imagine myself without him."
        "They say you must grow up, you must stop dividing the world discretely into good and evil, into black and white."
        "I already grew up once, thank you."
    scene bg int_liaz
    show blackout_exh
    with dissolve
    play ambience sfx_intro_bus_engine_loop fadein 3
    "Things change so much when you stop watching."
    "Didn't look toward the girls - they stopped showing interest."
    th "As if I'd ever been interesting at all."
    if (loki or herc):
        "Didn't look in the direction of the squad leaders... It's complicated, all in all."
    with fade
    "But I remembered their clear, lucid look, directly contradicting the postulate that we age from birth."
    "No."
    "Miku, Alisa, Slavya, Lena, and Ulyana didn't look like model pioneer girls and honors students."
    "Or rather, they didn't."
    "For all the eternal perfection of the same Slavya or the feisty Alisa, there was something in their gaze that was all-encompassing."
    "Capable of making them forgive the coming whims and pranks."
    "And it cannot be considered their ordinary state, at all."
    "Feisty, humble, fidgety, lazy - different."
    if loki:
        "But I saw in Alisa's eyes the reflection of a starry sky."
    elif herc:
        "And I envied whoever they would one day decide to join their life's journey with."
        "Funny and sad, funny and serious - they looked at the world with the eyes of a baby."
    else:
        "But it was the slight recklessness in Katushka's gaze that made me act unusually, completely uncharacteristic of me."
        "Resolutely."
    "So it was possible to drown in their eyes."
    "If you show a little attention and patience."
    "Then that mischievous twinkle in their eyes would be for me. There's nothing hard about it."
    "And this world is like a girl, it too laughs mischievously, drags you by the hand to show how the cat has calved, how red the sunset is, and over the smooth river our conversations echo distantly."
    "And the scent of the fire in my hair, and the taste of my lips, and the warmth of my fingers..."
    "It will all be mine, if you want it just a little bit."
    th "Won't it?"
    "And I didn't know the answer."
    "Because I didn't want anything."
    "Because the endless blue of the lakes in my eyes and the whisper of the wind in my voice were no longer for me."
    "The young world resented inattention, as any girl would have done."
    "Even though it is accepted that the 'world' is male and, according to the beliefs of pantheism, the deity is a polygendered being altogether."
    "But this world took offense - like a girl to inattention."
    $ volume (0.5,'ambience')
    "That's why the soft murmur of the engine was replaced by a low hum."
    show blink
    "A steady, measured hum, causing machine drowsiness."
    "Either by the clatter of wheels or by the noise of crowds of passers-by scurrying in and out."
    "I tried to listen, to identify this sound, its belonging, for it clearly had nothing to do with Olga Dmitrievna's cottage, where I had fallen asleep after last night's disco."
    "Nor did it have anything to do with the elevator I was dreaming about."
    th "What could it be..."
    "The easiest thing would be to open my eyes and look around, but I'm sleepy, I'm so sleepy."
    if loki:
        "The cost of living alone is that your schedule flies off incredibly quickly."
        "You stop sleeping at night, you build your schedule so that you wake up before you go to work, nothing more."
    else:
        "I couldn't remember the sound, but I remembered the smell."
        "Dusty chocolate."
        "The smell of an endless day ten years long."
        "It doesn't taste any different either, my sweet swamp."
    "The hardest thing is giving up social media."
    "I don't even know what's harder, quitting smoking or quitting social media that turns you into a night dweller."
    "But I never quit smoking - I guess the answer is obvious."
    "But then, when you've had your fill of loneliness to the point of nausea and snotty green, falling asleep as the scarlet tints the east, she'll come to you."
    "She will hold out her hand again, she will call to you again."
    scene bg int_liaz
    $ renpy.show("bg int_sam_house_clean_7dl", what = D3_intro("bg int_sam_house_clean_7dl"))
    with fade
    "It's like I'm sitting in my favorite spot on the sill, leaning my head against the icy glass, and laughing people with beautiful faces and burning eyes are whizzing by on the other side."
    "I'm sitting on the windowsill while life whizzes by, you can sleep until your final stop."
    "Especially since I have an unlimited ticket."
    "Life is a path from birth to death."
    "A long jump."
    "A journey."
    "Except other people get off at their stops, and I get crazy."
    if loki:
        "I can't explain the Ksalisa story in any other way."
        th "She probably wouldn't have left me, would she?"
        "Though she might well have kicked me in the head for being indecisive."
        "But surely she would never..."
        th "She promised to make the world a better place, so she took away her own right to meanness and cowardice."
        "And I... I chickened out."
    elif herc:
        "And here I did."
        "I could fight if I knew what I was fighting for."
        "I wasn't fighting for myself at all. I couldn't."
        "So I took a deep breath..."
    else:
        "How else to explain the trite story of childhood friends who never got anywhere, I don't know."
        "After all, it's a hackneyed story!"
        "I've watched so many silly Chinese cartoons, read so many books with this hackneyed plot... How come I ended up a victim of something like this?"
        "Or rather, not even that. I became a powerless observer of such things."
        "It's been a long time since we've been gone, and it just keeps raining."
        "She had green eyes, dark hair, knew how to hug and look up with mute adoration."
        "A fool would have guessed."
        "I was stupider than a fool."
    stop music fadeout 1
    scene bg intro_xx
    show unblink
    $ volume (1.0,'ambience')
    play music music_7dl["shib_mono"] fadein 1
    "And opened my eyes."
    "On an empty bus, to a vaguely familiar tune from the land of childhood memories."
    "I was getting somewhere, going somewhere..."
    "I think I even talked to someone."
    "Oh, right!"
    stop music fadeout 3
    show blinking
    "As I blinked my eyes out, I realized that I was indeed on a bus, and not much time had passed since I had closed my eyelids."
    play music music_7dl["last_hope"] fadein 3
    "At most ten minutes."
    "But it felt like a much, much longer time had passed."
    "And I was having a hard time remembering why I'd gotten on that bus in the first place."
    if loki:
        "I got a call from my longtime love, my beautiful bitch with the frostbitten eyes."
        "And in a frantic voice she asked me to come because she couldn't take it anymore."
        "She can't."
        "How many times I've rehearsed this situation in my head, I can't count!"
        "She'll call and I'll swagger and arrogantly condescend, sneer, mock."
        "But I'll forgive her in the end anyway."
        "I'm still too bad at being angry and hateful."
        "Still think she's an angel sent down to me that I just don't deserve."
        "So there's no way I'm letting her go this time!"
        "Even if it's been ten years, even if we're both not the same, I don't care!"
        "That's the way it's going to be!"
    elif herc:
        "It was just an ordinary shift a few days before the holidays."
        "A day in two, a day in three... That's right, if it hadn't been for that pneumatics scene, I would have had every chance of being on duty on New Year's Eve, too."
        "And no, it didn't bother me at all."
        "When there's no one to celebrate the holidays with, they're not much different than weekdays."
        "The only difference is that they can pay you more for the holidays - half the rate."
        "Yes, a bonus from a tipsy host, like last year."
        "I guess you could say I had some warm feelings about the holidays."
    else:
        "They dragged me out on a part-time job for a small penny."
        "This organization owed something to my mother through the seventh hands, so it periodically threw me different means of earning money."
        "So the call that plucked me out of the window sill route could probably be considered a financial gift from the muther."
        th "I should call her, thank her."
        "Distantly, I thought."
        "A penny for New Year's Eve, so that a nauseating salad bought at some 'Spar' could live in the fridge, and a bottle of green fairy."
        "Caring, my ass."
        "I wish they'd thrown me a chance to go back and make things right."
        "But nothing like that is going to happen, of course."
    "Next stop is mine."
    "As always, I got up early - there were no people in the cabin, I wouldn't have had to push through, but habit is habit."
    "I froze on the back deck, watching the bus slowly climb the hump of the Volodarsky Bridge."
    if dr:
        "Predatorily grinned in anticipation."
    "And I felt something strange on my face."
    "Unusual, unfamiliar."
    "A long stubble, or rather an almost beard, on the face of a seventeen-year-old pioneer."
    "Indeed, what an outrage it is to have a bearded pioneer, isn't it?"
    if dr:
        th "Here, if the bus gets a good speed, it will perform such a pas de trois on the ice that we will all end up in the water."
        th "Death in three... Two..."
    else:
        th "What, it would seem, has the pioneers got to do with it?"
    "And suddenly, out of the corner of my eye, I caught a face that was cuttingly familiar."
    "Just the tiniest bit wrong in features, bottomless eyes..."
    "A stamp of inevitability on the forehead."
    if loki:
        show dv smile winter
        pause(.1)
        hide dv with dissolve
        me "Alisa!"
        "Shouted I, waving my arms."
        "Where did she come from?"
        "I didn't know."
        "What's much worse, I didn't know how I knew her!"
        "She wasn't a childhood friend, an acquaintance of acquaintances, or in any other way appearing in my life."
        "And yet..."
        "But too late."
        "With the engine humming bassily, the bus raced past the girl, faster and faster, hurrying down the hump of the bridge, turning out toward the subway station and spitting me out toward my dream."
        "But Alisa."
        th "Well, I walk up to her - what do I say?"
        th "'Hi, I saw you in my dream'? What vulgarity."
        "If she ever really was, this girl here in the scarlet fitted coat, stubbornly stomping across the foot of the bridge, she never promised me that she would be with me."
        "No. Only to make the world a better place."
        "So..."
        "All I have to do is wait for improvements to come to me, too."
        "In the meantime, there's something I have to do."
        stop ambience fadeout 3
        "Nodding to myself, I waited until we arrived at Lomonosovskaya and, with my head pressed into my shoulders, ducked into the cozy, warm lobby of the subway."
        scene bg int_excalator2_7dl
        with fade
        "Ducked into the warm embrace of inevitability."
    elif herc:
        me "You?"
        "No way, no way."
        "The emerald glow from the gray faces, the gray streets."
        "The only color around."
        "How could she, my sweet, humble girl, be here?"
        "Because to believe in her existence is to automatically believe that everything that happened to me was real."
        "And it never was."
        "Never."
        "I didn't get a tan, I didn't get a burnt hair, I didn't soak in the scent of the southern night, more intoxicating than any wine."
        "Didn't believe in people again."
        "It was still the same me, the old unkind Semyon with the stubble and two suspended sentences."
        "The girl who looked like Lena met my gaze, flinched, blushed, turned awkwardly, slipped..."
        "When she came up again, the bus had long since climbed the hump of the bridge."
        "And there was nothing."
        "There was nothing."
        "Just the shift waiting ahead, cigarettes on an empty stomach, and a frosty morning at five o'clock."
        "That was all I could count on."
        "The loss of hope."
        stop ambience fadeout 3
        "And inevitability, awaiting me ahead."
    else:
        me "K-Katyushka?"
        show ka smile casual
        pause(.1)
        hide ka
        "Yes, the familiar look, the familiar curve of the lips."
        "But..."
        th "Wasn't I dreaming of all this?"
        th "Wasn't the camp just a fantasy of an eternally sleepless me?"
        me "Katyushka..."
        "Just a moment's glance, a flash of recognition..."
        "And then we are whistled away in different directions without mercy or a chance to meet again."
        "That's the way it's always been."
        "Even if you start your life journey hand in hand with someone else."
        "No matter how hard you try afterwards, no matter how you tear your ligaments and tendons trying to keep him by your side, your non-simultaneous time will break every bone in your body, but in the end it will take everything."
        "For it is written on your birthright to sit behind a monitor, head bowed to the left, drinking and, embarrassed, crying for the unfulfilled."
        "And the bus goes far, far away, and the distance gets longer and longer, and..."
        "They had the same spring in their eyes and their smile was soft-soft."
        "I groaned and slammed my fist against the door sash."
        voice "Hey, kid, what happened?"
        "Immediately the driver responded."
        "He only took his eyes off me for a few seconds, and that was enough."
        "The bus rolled on the ice, twisted, swirled..."
        scene bg int_intro_liaz_7dl
        with fade
        "And I, clinging to the handrail, didn't even smile, but grinned - wildly, defiantly."
        stop ambience fadeout 3
        play sound sfx_shoulder_dive_water
        "My inevitability was waiting for me."
    scene anim prolog_2 with fade3
    "\[Bad ending unlocked - «Inevitability»\]"
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("me_neu_bad")
    show acm_logo_me_neu_bad with moveinright:
        pos (1600, 1020)
    $ alt_pause(7.4)
    call alt_7dl_titles
    $ alt_pause(1)
    return
