label alt_day1_begin:
    play music music_7dl["areyouabully"] fadein 2
    play sound sfx_shoulder_dive_water
    scene anim_underwater
    show blackout_exh
    with fade
    "I suddenly realized that the entire world became pitch black water."
    "Maybe this is the same hell I was scared of so much."
    "Cold, darkness and complete lack of air."
    "And I so want to leave everything as is and throw myself into an endless freefall towards the bottom."
    "I had no more strength for resisting."
    "Movements became slower and slower…"
    "Soon I was moving straight down."
    with fade
    return

label alt_day1_bus_start:
    scene anim_underwater
    show blackout_exh
    with fade
    "And when I hit the bottom, I realized that I was just sleeping."
    $ volume (0.7,'sound_loop')
    play sound_loop sfx_cooling_engine_loop fadein 2
    if loki:
        "Roaring frost swapped out for searing heat."
        th "Seems like I went straight into my own personal hell."
        th "It's stuffy, dark and cramped in here."
        th "And pretty boring."
        "The strangest part was that there was no pain, — that tearing, burning feeling from the inside, when something burst inside me under the blow of a boot, disappeared forever."
        "Being completely bored out of my mind, I opened my eyes."
    elif herc:
        "Against my will, my hands reached out to check my face.."
        th "As if something is supposed to be there... A scar?"
        th "A cut?"
        "Nothing like that, the skin was even and clean."
        "Gotta get a grip."
        "I opened my eyes."
    else:
        "I doubled over trying to cough up wet bitterness."
        "I simultaneously wanted to breathe, and to spit out what was lazily swaying in my lungs as quickly as possible..."
        th "Wait. There's nothing in my lungs."
        "Breathing was easy and non-problematic."
        "It was just a little hot."
        "I opened my eyes."
    scene black with fade
    "And immediately met someone's gaze."
    scene cg d1_mi_bus_7dl
    show blackout_exh
    with flash
    "Interested stare. Like I'm some kind of exotic animal."
    th "A girl. {w}Cute one."
    "I noted mechanically."
    "The most logical thing would be to smile at her, but I've always had problems with that.."
    "I had a feeling I knew her."
    "We didn't actually know each other, but I swear I saw her somewhere."
    if dr:
        "Maybe on the monitor's screen?"
    "Maybe we met on the street?"
    "I mean, aquamarine eyes and hair of a shade that is referred to in print as «cyan», I would definitely remember them if I ever saw them!"
    "And that's not to mention the exotic outfit - a clear imitation of Soviet pioneers."
    th "Sorry sweetie, but you're a bit too old to be a pioneer."
    scene cg d1_mi_bus2_7dl
    show blackout_exh
    with dissolve
    "We looked into each other's eyes for a few seconds before she nodded and, after drumming up a rhythm on the glass with her nails, ran away.."
    scene white
    show prologue_dream
    with flash
    th "On the glass?"
    th "Wait, I'm in a bus?"
    th "But I definitely remember…"
    th "...I remember what?"
    "I definitely remembered that I got on the bus and went somewhere."
    "Whether I arrived was a separate question - from some point a black blind spot was gaping in my memory."
    scene cg d1_mi_dv_bus_7dl with flash
    "It was summer outside."
    th "{b}SUMMER?!{\b}" with vpunch
    "Not far from the bus, a second girl was waiting - a little taller than the first, also very beautiful, with copper-red hair that shone fieryly in the bright sun.."
    "«Cyan» girl ran up to her and said something quickly, quickly, waving her arms, while the redhead silently and a little condescendingly listened to her."
    scene cg d1_mi_dv_bus2_7dl with dissolve
    "Then answered something — and the «cyan» one laughed, somehow finely, crumbingly. As only Asians can."
    "All this time I've been sitting trying to get myself to move."
    th "I definitely wasn't crippled by paralysis, considering I managed to open my eyes!"
    scene bg int_bus with flash
    "Both girls left, leaving me alone."
    "A few moments later movement abilities were returning to me."
    "Finally I managed to turn my head."
    "Yup, that's definitely not the LiAZ I boarded."
    "Armchairs stretched in pairs along the cabin, freeing a narrow passage in the middle, reminiscent of regular Icaruses from my distant childhood.."
    "And I'll be damned if this ain't an «Icarus»!"
    show blinking
    "I collapsed into a chair."
    th "Eeeeeyup!"
    th "What the hell is going on?"
    th "Some painted Asians, redheads - and not even one went into the salon and helped the disabled."
    "It was unusually empty in my ears - the headphones fell out and were making a low noise somewhere on my chest."
    "Catching the escapees, I tried to put them in place, but they, without even stopping, instantly fell out.."
    th "Did they break?"
    th "Out of the frying pan into the fire."
    "Turning off the player, I headed to the exit."
    "For some reason, there was absolutely no fear - modern man is rarely surprised at anything."
    "And here the miracles have simply already chosen a quota, so all that remained for me was to listlessly state the amazing."
    "It would be better for my psyche anyways."
    "Noting that I was still flaunting my winter clothes—another item on a growing list of questions — I threw off my overcoat, out of place in this heat, and began to make my way to the exit.."
    scene bg int_bus:
        zoom 1.0 xalign 0.5 yalign 0.4
        linear 6.0 zoom 2.0 xalign 0.5 yalign 0.4
    with dissolve
    th "For how long was I sleeping that winter managed to end?"
    th "Or am I still sleeping?"
    me "Ow!" with flash_red
    "I pinched myself."
    "The pain sobered me up, but I still couldn't wake up."
    stop music fadeout 5
    stop sound_loop fadeout 2
    th "Welp, time for recon."
    "The door was open, so I climbed out without any interruptions."
    "And at the same moment, half-strangled panic reared its head again."
    $ volume(1.0,'sound_loop')
    stop music fadeout 3
    scene white with dissolve
    pause(0.5)
    scene bg ext_camp_entrance_day:
        xalign 0.5 yalign 0.5 zoom 1.15
        linear 0.2 zoom 1.2 xalign 0.5 yalign 0.5
        ease 0.05 zoom 1.0 xalign 0.5 yalign 0.5
    play ambience ambience_camp_entrance_day fadein 3
    play music music_7dl["dead_silence"] fadein 3
    "Because my eyes landed on a picture that haunted me all my adult life!"
    scene
    $ renpy.show("bg ext_entrance_night_clear_7dl", what = Dawn("bg ext_entrance_night_clear_7dl"))
    show anim_grain
    with touch
    "I couldn't remember when I first dreamed of those ball-painted gates."
    scene
    $ renpy.show("bg ext_entrance_night_clear_7dl", what = SS_com("bg ext_entrance_night_clear_7dl"))
    show anim_grain
    with blind_d
    "But I remembered them - in detail, in detail! - from the pegs on top, going further along the brick wall in both directions, as far as the eye could see, to the five-pointed star at the junction of the wings."
    "Although it was always night in my dreams."
    scene bg ext_camp_entrance_day
    with fulldiam
    "And now the day was in full swing."
    "Yes, and I was not in a dream now, but in the reality!"
    "I stood stumblingly, swallowing bitter saliva, rolling my eyes, rocking diligently out of phase with gravity."
    "Four exhales, two inhales, pulsating, ringing in my ears."
    scene black with flash_red
    "And snapped in half, turned inside out, praying for death as a deliverance from suffering - the roots of the hair hurt, the eyeballs, the skull from the inside…"
    "Not surprisingly, in a moment I found myself standing on all fours and looking at a brown puddle - the contents of the stomach - in the grass."
    scene bg ext_camp_entrance_day with fade
    th "Gotta get up."
    "I absentmindedly noted."
    scene bg ext_bus with dissolve
    "With great difficulty, I managed to crawl back to the bus and, sitting on the step, took out my phone from my pocket.."
    "Current time - 2 o'clock, the date — 19th of July, can't figure out the year though - it's showing up as zeroes."
    if dr:
        th "Doesn't matter, gotta call my mother."
        "The last called number."
        "No wonder, besides that one there were a few others."
    else:
        th "Gotta call someone."
        if herc:
            "Zinaida's number was the last on the list of calls."
        else:
            "In a different situation, I would have been surprised to see Ksana's number last in the call log, but now it didn't matter."
    play sound sfx_cellular_phone_error
    pause(3)
    me "What the…"
    "I took the receiver away from my ear and checked the reception quality, but instead of at least the minimum signal, there was a fat red cross on it - the operator’s signal was lost."
    me "{image=alt_KS_censor}" with vpunch
    "Profusedly cursing, I slammed my fist on the bus."
    "Modern man has other ways to shout to civilization, in addition to mobile phones."
    "I tried to check all of them."
    "However, numerous wireless networks in the phone were silent."
    "Even GPS, completely in the open!"
    me "God damn!"
    me "Is this a joke?!"
    stop music fadeout 4
    scene black with flash_red
    "A sharp pain in my temples was the last thing I felt before I fell into oblivion…"
    stop ambience fadeout 3
    with fade
    return

label alt_day1_firts_met:
    $alt_pause(1)
    scene black
    sl "…looking for him, and he's just sleeping here!"
    "A voice came from nowhere."
    "I swung my head around, trying to understand where was the voice coming from."
    play sound sfx_punch_medium
    with vpunch
    scene
    $ renpy.show("bg ext_bus", what = Noon("bg ext_bus"))
    show unblink
    play ambience ambience_camp_entrance_day fadein 9
    "And, after painfully smashing my head on the door, I opened my eyes."
    show sl pioneer shade with flash
    play music music_list["take_me_beautifully"] fadein 1
    "Because of the bright sun directly shining into my face, it was impossible to see who was talking to me."
    "But at least the contours of the figure - clearly female - could be distinguished."
    th "Now what, we're confirming the reputation of a loser again?"
    th "Didn’t even have time to move or go somewhere - and I already screwed up somewhere."
    "Amazing, isn't it?"
    "Woman, or girl? - she continued to say something in raised tones, waving her hands, but I hardly perceived her."
    "Everything swam before my eyes, the noise in my ears obscured the sounds, and I, trying to get up, convulsively grabbed the doorstep."
    sl "Are you okay?"
    th "No, stupid woman, I'm not okay! {w}What are these questions, did you overdose on Hollywood films?!"
    "As usual, I barked to myself."
    "Not a word left my lips - I swear! - but the girl took a step back, obviously shocked by something."
    "And I finally managed to take a good look at her face."
    scene
    $ renpy.show("bg ext_bus", at_list = [zenterleft], what = Noon("bg ext_bus"))
    show sl serious pioneer
    with dissolve
    "Definitely a girl, very young, very beautiful, at home I called such celestials and avoided their company with all my might."
    "Our social categories are too different, our social circles are too different."
    "If such an angel once descends to me, it is only because they need something from me."
    "Usually something directly involving my skills."
    if loki:
        "One already descended once -- I'm still having a hard time sorting that mess out."
    elif herc:
        "I may be dumb as an oak, but my computer skills were good enough, I could help if that was needed."
    else:
        "How many business cards, avatars and logos I stamped for free to such angels... Before I started to shy away from them."
        "And they get offended at you not wanting to help them!"
    "Together with other oddities, the presence of such beauty next to me did not add peace to me at all."
    "The reaction was expected: I was on guard."
    show sl normal pioneer with dspr
    sl "Did anything happen?"
    menu:
        "Did you want something?":
            $ lp_sl += 1
            $ karma += 10
            show sl smile pioneer with dspr
            sl "Ah, you spoke!"
            "I don't know why she was happy."
            "Seemed like here people didn't talk to her that much."
            th "Amazing achievement, not going to lie."
            th "Get to the point."
            show sl normal pioneer with dspr
            sl "Why are you so angry?"
            me "Everything's fine."
            "I replied, casually marveling at the unexpectedly high tone my throat exuded."
            th "Spectacular, the first thing coming out my throat is screeching."
            th "Can this first impression get any worse?"
            show sl smile2 pioneer with dspr
            sl "Please tell me! I'll try to help!"
            "The girl smiled irresistibly - so charmingly, openly."
            "It didn't defuse the situation, it only got worse."
            "That's right - the more sincere is the smile, the heavier the stone in the bosom."
            me "Everything's fine."
            "I repeated."
            sl "Yeah? {w}Well, alright."
            show sl normal pioneer with dspr
            sl "Olga Dmitrievna sent me to meet you, because the bus had already arrived half an hour ago, and you still hadn’t shown up on the territory."
            th "Olga Dmitrievna."
            "Name didn't ring any bells, hell, it could be some Bang Ding Ow — and I'd understand about the same."
            show sl smile pioneer with dspr
            sl "Squad leader."
            "She explained."
            "I remembered the first person I saw when I opened my eyes - that Japanese «rolly beauty» in pioneer form."
            "And my current interlocutor was dressed up in exactly the same way.."
            "White shirt, scarlet tie, and mid-thigh skirt. The only thing missing is the «I won’t forget Ilyich» tattoo for complete authenticity."
            th "Got it. {w}So let's write it down - we're playing pioneers, even the squad leaders were brought."
        "Ignore her":
            $ lp_sl -= 1
            $ karma -= 10
            $ alt_day1_sl_ignored = True
            show sl surprise pioneer with dissolve
            sl "Why are you so silent?"
            "She looked completely discouraged by my silence."
            th "I'll say «hello, dolly» to you, honest — how did it go, pioneer word? — as soon, as I can properly stand up."
            "I promised."
            "It suddenly became wet and cold under the nose - two paths of blood ran along the upper lip."
            sl "What the… You're bleeding?!"
            "Out of nowhere, a handkerchief appeared in her hands."
            show sl surprise pioneer close with dspr
            "She leaned forward, clearly intending to wipe the blood, but I pulled away."
            me "No need. Everything's fine."
            sl "How is this «fine»?"
            sl "You need to see a nurse."
            "At the same time, I didn’t feel very comfortable, as if I was doing a big disgusting thing to a positive person towards me."
            "But there's no way will I believe that she will be gratuitously positive towards a person like me."
            "I may be an infantile moron, but that won't happen!"
            show sl sad pioneer with dspr
            sl "Look, this isn't good, at all…"
            "She got upset."
            sl "Let me take you to the nurse."
            sl "What if you get worse on the way there?"
            "Oh, and now an irresistible female weapon will be used - female tears."
            "If I had any doubts that I was going to be used, they just fell off by themselves."
            sl "Let's go?"
            me "No need. I'm already feeling better."
            "Gathering my strength, I once again leaned on the step and stood up."
            "Still nauseous, but it's not fatal."
            me "See?"
            sl "Are you sure? Maybe I should escort you?"
            "The girl kept insisting."
            th "How stubborn is she going to be!"
            if loki or herc:
                "I frowningly wiped the blood with my sleeve and asked:"
                me "Don't you have anything better to do?"
                sl "I do, but…"
                me "Go do that then."
            else:
                "I silently wiped the blood with my sleeve."
                me "I'm feeling better already."
                "I reiterated."
            "Now I desperately needed solitude to come to my senses and comprehend the current situation, and this blonde is only interfering."
            show sl sad pioneer with dspr
            sl "Damn, your character is something else…"
    "From somewhere on the other side came a sound that I, straining my memory, identified as a horn."
    th "Right! Pioneer re-enactment!"
    "And she suddenly got worried:"
    if alt_day1_sl_ignored:
        sl "I'm sorry but I need to run."
        sl "There are things that no one but me can do."
        th "Who would've guessed."
        me "Alright."
    else:
        show sl normal pioneer with dspr
        sl "Listen, I would love to chat with you, but time does not wait."
        sl "I've gotta go, so much to do!"
        "And here we smoothly approach the delegation of authority."
        sl "And nobody else other than me is going to do things, so you'll have to be on your own, ok?"
    "The girl took out a piece of paper folded in four from her pocket."
    if alt_day1_sl_ignored:
        show sl normal pioneer with dspr
    else:
        show sl smile pioneer with dspr
    sl "Thought I'd see you off myself, but okay."
    "The unfolded paper turned out to be a map."
    scene bg map_alt1:
        zoom 1.2 xalign 0.5 yalign 0.5 subpixel True
        easeout 8.0 zoom 1.0
    with flash
    sl "Look, we are here."
    scene bg map_explain with fade
    "She pointed to a rectangle, signed in someone's beautiful handwriting as «parking» - there was a bold red cross."
    sl "And you need to go here - to Olga Dmitrievna's house."
    show sl smile2 pioneer with dissolve
    sl "You know how to navigate by map, right?"
    scene bg ext_bus
    show sl smile2 pioneer at cleft
    with dissolve
    "She smiled, as if negative response couldn't be possible for her."
    me "I'll try."
    sl "Great. {w}Let me offer you small advice."
    if alt_day1_sl_ignored:
        th "Well, what do you have there? Don't trust anyone? Or be kinder to people? Spit out something banal, you little shit."
        show sl serious pioneer with dspr
        "The girl shuddered again, as if catching my thoughts."
    else:
        me "What?"
    sl "You see, it's not the beginning of the shift now, you're very late…"
    show sl normal pioneer with dspr
    "She shrugged her shoulders, as if she suddenly chilled."
    "And I silently nodded - saying that, I understood, I was late for the beginning of the shift - to the camp? - and for free too."
    sl "And your clothes…"
    "She took a look at my jeans and sweater."
    if alt_day1_sl_ignored:
        th "Better than your pioneer forgery."
        th "So sorry that I was enrolled in your private club without anyone asking."
        th "You'll have to tolerate me now."
    else:
        "I nodded."
        "The clothes were not only out of season, but also attracted attention."
        th "Strange that this blonde isn't asking questions."
    $ alt_pause(0.7)
    me "And?"
    "I didn't last long - this pause clearly overstayed its welcome."
    sl "And the camp has its own traditions…"
    sl "Well, if you see a group of people with buckets - run. They're most likely after you."
    "Seemed logical enough to me: if we're re-enacting that age, we gotta do it properly, including «penalties»."
    me "Got that."
    "I nodded."
    show sl normal pioneer with dspr
    sl "I have to go now. Welcome to «Sovyonok», by the way!"
    if herc or loki:
        menu:
            "Bye-bye":
                $ karma -= 10
                "Now she will leave, and I will breathe a little more freely, and I'll at least be able to apprehend the situation."
                me "Uh-huh. Adios."
                th "I can't wait for this magical moment when I'll stop being squeezed and bothered."
                show sl smile pioneer with dspr
                "Apparently, my desire to be alone was written quite eloquently on my face."
                hide sl with easeoutleft
                "So she nodded, smiled and disappeared behind the gates."
                th "HALLELUJAH!"
                stop music fadeout 5
                "I put the map in my pocket and just enjoyed the silence for a few minutes."
                "Some kind of eight-millionth sense told me, among other things, that in the near future I would have vanishingly few such moments."
            "Won't I get lost?" if not alt_day1_sl_ignored:
                $ karma += 10
                $ lp_sl += 1
                $ counter_sl_7dl = 1
                me "You weren't sent without any reason…"
                sl "Actually, no…"
                "She pondered for a few seconds."
                "And then shook her head."
                sl "But you are also right - together we will get there much faster. Let's go!"
                "She grabbed my hand and pulled me along."
                "Ah, walking with a girl holding hands! What kind of romantic nonsense is this!"
                "As if you're four years old, you're singing «Kartoshka», and in the group a glass of jelly and a laughing grandmother-educator are waiting."
                stop music fadeout 5
                "I've already forgotten when was the last time I walked with someone like that."
            "Hold up!" if alt_day1_sl_ignored:
                $ karma += 10
                $ lp_sl += 1
                $ counter_sl_7dl = 1
                show sl surprise pioneer with dspr
                sl "What's wrong?"
                "I carefully chose the words, but instead of them there was an indistinct lowing."
                "That's what usually happens when you trample your own pride."
                me "Can you still escort me?"
                me "You weren't sent with no reason, after all…"
                show sl normal pioneer with dspr
                sl "Actually, no…"
                "She pondered for a few seconds."
                show sl smile pioneer with dspr
                sl "But you are also right - together we will get there much faster. Let's go!"
                "She grabbed my hand and pulled me along."
                stop music fadeout 5
                "Personal space and constraints definitely did not exist for this girl."


    else:
        menu:
            "Leaving so soon?":
                $ lp_sl += 1
                $ karma += 10
                $ counter_sl_7dl = 1
                "The girl nodded and almost turned to leave."
                "But it looks like my view was really pathetic, because she frowned and said:"
                show sl serious pioneer with dspr
                sl "You know what... Come on, I'll take you to the squad leader myself."
                sl "Just so I won't worry."
                "I was against that."
                sl "Great. Let's go! {w}By the way, I'm Slavya!"
                $ meet('sl','Slavya')
                $ alt_day1_sl_met = True
                "But my opinion was not taken into account."
                "She took my hand - the touch sent goosebumps down my shoulders of their own accord - and led me."
                "It was great to hold such a girl by the hand - hell - amazing!"
            "Off you go":
                $ karma -= 10
                me "Hope I won't get lost on the way."
                "I muttered."
                show sl laugh pioneer with dspr
                sl "Of course not! This isn't «Artek», it's not even «Caravella», our camp is really small, you'll figure it out."
                sl "Don't be offended, please, but I really have things to do."
                th "Come on, leave already!"
                stop music fadeout 3
                hide sl with dissolve
                "Nodding, she disappeared behind the gates."
    if (counter_sl_7dl == 1):
        scene bg ext_camp_entrance_day with dissolve
        "I froze up, again looking around the gate."
        show sl smile pioneer with dissolve
        sl "Why are you just standing there? Let's go."
        me "Uh... Umm…"
        th "You see, I've seen this place in a dream."
        th "You see…"
        "I wanted to beat my head against soft walls, yell, tearing my throat."
        "Give me haloperidol, chlorpromazine - anything to confirm that this is really not true.."
        if alt_day1_sl_ignored:
            show sl sad pioneer with dspr
            sl "Are you feeling ill?"
            "The pioneer asked, still concerned about my condition."
            me "I'm fine. Let's go."
            show sl normal pioneer with dspr
            sl "Alright… If you say so."
            "She pushed the gate, letting me through, and followed."
        else:
            show sl normal pioneer with dspr
            sl "Is everything ok?"
            "She asked."
            sl "You look scared."
            th "Of course I would be!"
            me "New places, new people…"
            "I answered ambiguously, but it seems to the girl that was enough."
            show sl smile pioneer with dspr
            sl "Don't worry. You'll like it here."
            "She pushed the gate, letting me through, and followed."
    else:
        play music music_list["trapped_in_dreams"] fadein 2
        "Left alone with myself, I sat on the bus step and breathed a sigh of relief."
        "I was always taught that before doing something, you need to understand whether it is necessary to do it at all."
        "Ideally, of course, it’s better to draw up an action plan in general, but it’s too early, there is little data, and I dismissed the plan suggested by the howling subconscious to grab my head and run in different directions as untenable."
        "I've had to find the answers to two eternal russian questions: «who dun it?» and «what do?»."
        scene bg ext_road_day with dissolve
        "Nature around raged with bright, rich tones, making you think about the poison swirling in the blood."
        "I heard that some drugs have such a side effect - you look at the world and see it as oversaturatedly bright."
        "It's like someone turned the color saturation slider to the maximum."
        "As a result, the view of the nature of central Russia resembled either the Amazon jungle or an impressionist canvas."
        scene bg ext_sky_7dl with dissolve
        "And the sky overhead was transparent, which only happens…"
        me "No, seriously?"
        me "Summer?"
        "I felt like the hero of Heinlein, who opened the treasured door."
        "Even though I couldn't remember any details."
        scene bg ext_road_day with dissolve
        "I racked my brain, and…"
        $ volume(0.1, 'music')
        scene bg black with fade
        "Temples twisted with pain, blood dripped from the nose."
        "But I didn’t care much, because memories poured from the past through the newly formed hole."
        stop ambience fadeout 3
        scene anim intro_14 with fade2
        play sound sfx_intro_bus_transition
        stop music fadeout 2
        $ alt_pause(3)
        scene anim intro_15 with fade
        $ alt_pause(3)
        scene anim intro_16:
            xalign 0.5 yalign 0.5 zoom 1.0
            linear 0.5 zoom 1.25 xalign 0.5 yalign 0.5
        $ alt_pause(3)
        play ambience ambience_7dl["int_silence"] fadein 1
        "I began to remember."
        "The urban landscape outside the window of LiAZ was replaced by a suburb, and then fields."
        "Even the road, at first flat and smooth, like a German autobahn, very soon turned into a shaky provincial secondary road."
        "What was before that? Think!"
        show anim_intro_recall:
            xalign 0.5 yalign 0.5 zoom 1.35
            linear 3.0 zoom 0.3 xalign 0.5 yalign 0.5
        pause(3)
        if loki:
            scene bg ext_winterpark_7dl
            show prologue_dream
            with flash_red
            with vpunch
            "A sharp, painful stab somewhere in my chest - I folded almost in half."
            th "Phantom pain?"
            "No, memories about something…"
            th "I was going somewhere, but whether I reached it - I don't remember."
            th "Instead I arrived here."
            "But where memory was powerless, the diocese of sensations began."
            "Chill. Frost. Pain in cracking bones."
            "Slowly fading consciousness."
            stop ambience fadeout 1
            scene bg ext_road_day with flash
            th "NO!"
        else:
            "The almost conquered pain returned, and I took the hint - apparently, there is something not very useful for the psyche."
            "As from a tooth shot through with pain, I recoiled from this part of the memory."
            "Not now. {w}Not yet."
            stop ambience fadeout 1
            scene bg ext_road_day with flash
        $ volume(1.0, 'music')
        play ambience ambience_camp_entrance_day fadein 3
        play music music_list["trapped_in_dreams"] fadein 3
        th "I'll remember it if I need it. {w}Now I have much more pressing matters."
        "I was sleeping, I know for sure - that girl came to me again and asked if I would go with her."
        "Here I am. {w}Turns out I did go."
        th "Who was she?{w} What would she need from me?"
        "Thoughts about her frightened away the pain, and drums was pulled from the temples."
        "It provided no answers, but at least it became easier to think."
        pause(1)
        scene bg ext_bus with dissolve
        th "Did she bring me here?"
        th "Just like that, after obtaining my consent, brought me here? {w}Is that even possible?"
        "The voice…"
        "It seemed to come from afar, and I could barely make out the individual words."
        scene cg d1_uv_2
        show prologue_dream
        with flash
        "Her lips almost touched my ear, and the warmth of her breath was both ticklish and pleasant."
        dreamgirl "«…remember…»"
        dreamgirl "«…egan…»"
        dreamgirl "«…ember…»"
        dreamgirl "«…promise…»"
        scene bg ext_camp_entrance_day with dissolve
        "I looked at the gates."
        "I really missed this curvy brown-hair in a short dress here."
        "Remembering the number of directions that I suggested to the girl to go instead of going somewhere, I shivered."
        th "If she'll remember them…"
        th "Wait, hold on."
        th "What will she remember? Whatever I told her in a dream?"
        th "Who will remember? The dream? The girl?"
        th "There definitely is a rational explanation for all of this."
        "This wasn't a good consolation, but there was no better one…"
        $ alt_pause(1)
        "More or less recovered, I went to the gate."
        "Whatever they hide, there are clearly those who know more about the environment than I do."
    stop music fadeout 4
    stop ambience fadeout 6
    return

label alt_day1_arrival:
    play music music_list["my_daily_life"] fadein 5
    play ambience ambience_camp_center_day fadein 0
    scene bg ext_clubs_day with dissolve
    "Behind the gate was... a pioneer camp."
    "What a twist, right?"
    "Everything is new, fresh. The concrete slabs that paved the path have not yet been beaten, although greenery has already managed to break through here and there."
    "And what has always amazed me in such places, — the houses inscribed in nature with amazing skill."
    "Centuries-old pines, undisturbed by anyone, landscape irregularities turned to decorations…"
    "On either side of the path were some small buildings that looked equally shabby, but the one on the right was tightly closed, and the door was completely replaced by a fire shield with hooks, conical buckets and a red fire extinguisher."
    "The building on the left was much more interesting."
    "Judging by the sign, this is the building of hobby groups. {w}Or, as the authors of that sign pretentiously stated, «clubs»."
    play sound sfx_open_door_clubs fadein 0
    pause(1)
    "More importantly, there was a girl."
    "Another beauty in this unsettling place."
    show un normal pioneer far at left with dissolve
    if (counter_sl_7dl == 1):
        "She smiled at my guide, but stumbled a bit when she caught my eye."
    else:
        "Except that, in contrast to the active stranger who was pushing me at the entrance, this one looked somehow depressed, wary."
        "And definitely was in no hurry to make contact."
        "Furthermore, she got flustered when our eyes met."
    show un shy pioneer far at left with dspr
    "She immediately looked down and blushed almost to tears."
    "I'm serious! Her eyes were glistening."
    if persistent.alt_binder:
        if persistent.un_7dl_good_ussr:
            "Her face seemed vaguely familiar, but for the life of me, I couldn't remember anyone with those features.."
            th "Yeah, I definitely wouldn't forget such beauty!"
            show un smile pioneer far with dspr
            "The girl looked down at the floor in embarrassment and smiled shyly…"
            th "Did she smile at me?"
            show un normal pioneer far with dspr
            "…and then, without detecting a response, she hid her smile, leaving me to wonder if it didn’t seem like it at all?"
    th "Why yes, this is how it all begins - first we arrive from winter on the «Icarus», then we sink at a speed of one affection per minute."
    th "And then, as usual, a cheerful house with yellow walls, polite orderlies and a shirt from Cardin with ties on the back."
    "I stood almost in the same stupor, also frozen, wondering whether to approach at the risk of scaring off or to give the initiative to her?"
    "Honestly, the most polite thing to do right now would be leaving."
    "I would be thankful to myself, if I ever ended up in a situation like this."
    th "But then why don't my legs work?!"
    show us grin sport far at right with dissolve
    play sound sfx_bush_leaves
    pause(2)
    play music music_list["i_want_to_play"] fadein 5
    show us grin sport at right with dissolve
    "The silence was becoming frightening, and I already decided to clear my throat in order to somehow break the silence, as we were interrupted."
    "Neighboring bushes crackled, and a girl jumped out onto the road!"
    "Short, in a scarlet T-shirt with a slogan «USSR» and with the muzzle of an eternally cheerful, happy and dirty little sister."
    show us grin sport far at center with move
    "Completely red hair, pulled together by two tails-rockets, a cute appearance, which was confidently spoiled by the abyss of slyness, splashing at the bottom of blue eyes!"
    "From a distance, she seemed very small and was definitely younger than everyone I had seen here before."
    if (counter_sl_7dl != 1):
        "I was about to stop giving a damn about the possible «bleatings» and go up to clarify the way on the map, when the new girl jumped up to the standing green-eyed girl and began to say something, waving her arms in the best Italian traditions."
    else:
        "I wanted to say or ask something, but I didn’t have time - the «red» jumped up to the girl and started talking about something, waving her arms excitedly."
    "She, in turn, was embarrassed, lowered her eyes and said nothing."
    if (counter_sl_7dl == 1):
        show sl normal pioneer at fright with dissolve
        sl "Ul-ya-na!"
        show us laugh sport far with dspr
        us "Aye-aye, boss!"
        "Sincerely smiled the kid."
        sl "Ul-ya-na!"
        "My guide spelled it out again."
        show us smile sport far with dspr
        us "Whaaaat…"
        show sl laugh pioneer with dspr
        sl "Don't pretend, you understand everything."
        show us sad sport far with dspr
        us "Killjoy!"
        "She pouted, unclenching her palm."
        "From there, something oblong, green, crackling on the fly instantly flew to the zenith."
        th "What the hell was that, a grasshopper?!"
        "The red-haired stamped her foot, showed us her tongue and disappeared."
        hide us with easeoutright
        "Green-eyed stood for a while, coming to her senses - apparently, she understood what she had just been saved from."
        play sound sfx_open_door_1
        hide un with diam
        "Then, squeezing out something unintelligible, she returned back to «Clubs»."
    else:
        "Interested, I took a step closer, trying to hear what they were talking about."
        show un normal pioneer at center
        show us laugh sport at right
        with dissolve
        "I would probably continue to watch their entertaining dialogue, but «USSR» suddenly took something out of her pocket and started shaking it in front of the other girl's face."
        "That something turned out to be a grasshopper. {w}No. A locust. A massive one!"
        "To tell you the truth, I'd be scared myself if someone poked something like that in my face."
        stop ambience fadeout 2
        scene cg d1_grasshopper with dissolve
        "And she didn't disappoint!"
        un "AIEEEEEEEEEEEEEEEEEEEEEEEEEEEEE!"
        "She screamed and immediately ran away somewhere."
        scene bg ext_clubs_day
        show us grin sport at left
        with dissolve
        "«USSR» winked and slyly smiled at me, proceeding to give chase."
        hide us with easeoutright
    stop music fadeout 2
    $ persistent.sprite_time = "day"
    $ day_time()
    hide un with dissolve
    play ambience ambience_camp_center_day fadein 3
    "Great start, what else can you say?"
    if (counter_sl_7dl == 1):
        "I glanced at my guide, but she smiled serenely."
    th "Alright... O-okay. {w}I understood and accepted the rules - pioneering, traditions, practical jokes and grasshoppers in a fist."
    th "Do I have to wear shorts too? Or someone will finally check the lists and fail to find me there, and return me back to my homeland with an apology?"
    "However, apparently, it is Olga Dmitrievna who does the checks."
    "Then, I'll have to get acquainted with her."
    if (counter_sl_7dl == 1):
        "The blonde impatiently tugged at my arm and I complied."
    else:
        "Sighing, I followed the runaway girl."
    scene bg ext_square_day with dissolve
    play music music_list["get_to_know_me_better"] fadein 3
    if (counter_sl_7dl == 1):
        "And strange, indistinct thoughts crept into my head by themselves."
        th "Girl."
        th "Pretty."
        "Not even pretty - I have never seen such beauty in reality, and on the screen I would have decided that it was photoshopped!"
        if loki:
            "Ksana probably could compare to her…"
            "But for this, she would have to lose five or six years, a magical age of «somewhere between 15 and 30»."
        th "Holding my hand… {w}I wonder, if we had the opportunity to get to know each other better, could we get something of a relationship?"
        "I didn’t really flatter myself at my own expense, my attractiveness bordered on the plinth, but anything can happen in the world!"
        show sl smile pioneer with dspr
        sl "You don't have to stare at the back of my head like that."
        "She laughed."
        sl "Now let's take you to the squad leader, and then we'll see."
        sl "Want me to show you around?"
        "Without waiting for my answer, she turned onto some kind of narrow path, and a few minutes later stopped near a conspicuous house."
        stop music fadeout 4
        stop ambience fadeout 6
        return
    else:
        "And after all, how brighter is this reality than mine!"
        "Now, comparing, it seems as if I had a colorless dream or I just made up everything that happened to me before the bus."
        th "False memory."
        "And what am I supposed to do now?"
        "Only now I began to understand that something absolutely incredible happened to me, it hit my nervous system, to the point of trembling in my hands, a rollback of everything I experienced."
    if not loki:
        "My girlfriend - when she still was - in our last quarrel called me a retard. {w}And now I think she had every reason to think so."
    else:
        "Ksana - long ago, when she still had the speaking rights in our relationship - constantly complained that I was too emotionally cold. {w}Like, it's because of this that she…"
    "So it’s not fearlessness that’s to blame for my calm perception, but the fact that it just didn't get it."
    "If I understood everything back then…"
    "I shuddered in disgust at the thought of a possible view of me rolling on the grass in a quiet hysteria.. Urgh."
    scene bg ext_houses_day with dissolve
    "Noticing small houses on the other side of the square, I turned there."
    "Well, it is not so important whether I conquered fear or did not understand that I should be afraid - I must behave with dignity and correspond to the high rank of the representative of my hometown."
    "I walked along the paved path, squinted from the sun and looked with interest at «barrels» — semicircular carcasses with one door and one window, covered with a sheet of corrugated iron."
    "That's too chic for pioneers. {w}Personally, I had to huddle in a barrack for forty people, divided into four bedrooms - girls in the left wing, boys in the right."
    "Therefore, I have a somewhat different opinion about the life of the pioneers from what I see here. {w}In any case, there are no dormitory bedrooms here, and that's already good."
    "Now, concerning the schedule…"
    play sound sfx_punch_medium
    with vpunch
    if (herc or loki) and persistent.dv_7dl_good_ussr:
        play music music_7dl["sheiscool"]
    else:
        play music music_list["that_s_our_madhouse"]
    "I did not have time to finish the thought - from a strong slap between my shoulders, I lost my balance and lost the remnants of my thoughts."
    me "What the…"
    dv "There he is! Found him!"
    if persistent.alt_binder:
        if persistent.dv_7dl_good_ussr and (not dr):
            "I staggered, but held my balance."
            "In the entire Universe there was only one person who could do that to me…"
            show dv smile pioneer2 close with dissolve
            "I turned around sharply and, surprised at myself, scooped up the squeaking pioneer in my arms."
            "For some reason, it seemed very appropriate now, very... right?"
            show dv shocked pioneer2 close with dspr
            dv "Hey, psycho! The hell are you doing?!"
            "She squealed from somewhere in my arms - without making, however, any attempts to get out."
            me "Things are getting better and better today!"
            "I exclaimed and finally released the redhead."
            me "Redhead!"
            show dv surprise pioneer2 close with dspr
            dv "What?"
            me "How I…"
            "I did not have time to finish - the highwaywoman, quickly regaining, grabbed my neck."
            show dv smile pioneer2 close with flash
        elif persistent.dv_7dl_rej_rf and (not dr):
            show dv laugh pioneer2 close with dspr
            "With some two-hundredth sense, I guessed what was going to happen now, and relaxed."
            show dv smile pioneer2 close with dissolve
            th "Hello again."
            "I thought, inhaling the familiar smell of skin - from somewhere in my past life.."
            th "I know you. I don't know how, but I know you."
            "Instead of the expected attempts to escape, I, on the contrary, moved closer to her as tightly as I could."
            th "And damn, am I glad to see you."
            "My neck hurt - after all, the girl was quite strong and did not hold back at all."
            "But that didn't worry me."
            "Since, from behind the veil of oblivion, the priceless name suddenly surfaced - inhale-smile-exhale."
            $ meet('dv','Alisa')
            th "Alisa."
        elif persistent.dv_7dl_bad:
            show dv smile pioneer2 close with dissolve
            "In my distant childhood it was called «deadlock» — and became popular after films with Steven Seagal."
            "I don't really know, how does some pioneer know that..."
            "But for some reason I remembered that I was once greeted in this way."
            "And it didn't end well."
            "So…"
    else:
        "I didn’t have time to react when my neck was caught in a grip that didn’t allow me to move or even breathe freely."
        "It was clear what this is fraught with, I already had the experience of being late."
        show dv smile pioneer2 close with dissolve
        "Squinting my eyes, I saw that a girl I already knew was holding me - it was her who was at the bus when I woke up.."
        "Strong, but, like all girls her age, weighing a little more than nothing. So what I could do…"
    if herc:
        $ lp_dv += 1
        dv "Come on, faster!"
        show us laugh2 sport far at right with dspr
        us "I'm coming, I'm coming!"
        "A child's voice, out of breath as if its owner was carrying something… {w}heavy?"
        th "Bucket!"
        "I figured it out."
        "Remembering what I was taught in class, I took a step back and grabbed the redhead by the waist."
        "And instead of proceeding to a painful hold, I just threw her over my shoulder…"
        "…and started running!"
        dv "HUH!"
        show dv surprise pioneer2 close at left with moveoutleft
        dv "What are you doing, psycho?! Let me go!"
        "She clearly did not expect such a reaction and pounded my back with her fists, trying to free herself.."
        "I smirked and accelerated."
        dv "You don't hear me, do you?!"
        scene bg ext_path_day
        show dv surprise pioneer2 at left
        with flash
        pause(1)
        play sound sfx_alisa_falls
        me "Then go!"
        "I managed to break away from the chase, and I put her on the ground."
        "Smiling broadly, I deliberately clapped my hands:"
        me "May I leave?"
        "The girl remained silent, apparently still in a slight shock, and I, taking the silence as a sign of consent, turned around and was about to leave…"
        us "GET HIM!"
        show us smile sport far at center with dissolve
        "There was a familiar childish voice. I turned around - she, puffing, diligently dragged a fire bucket with water."
        show us smile sport with dspr
        me "I like it here!"
        "I winked at the elder redhead and immediately skittered away, escaping from a petty terrorist with a bucket."
        hide us
        hide dv
        with dissolve
    elif loki:
        $ lp_dv += 1
        $ karma -= 10
        play sound sfx_punch_medium
        with vpunch
        me "Hey… {w}hh… {w}let me go, crazy… {w}You'll choke me."
        dv "That's okay!"
        play sound sfx_punch_medium
        with vpunch
        "The bandit holding me did not even think to loosen her grip.."
        me "I… {w}myself… {w}for being late."
        dv "Really? {w}You want to penalize yourself?"
        dv "Not lying?"
        "She hesitated, but it seemed to really wanted to see how a man pours water on himself from a fire bucket."
        play sound sfx_punch_medium
        with vpunch
        me "You'll… {w}catch me… {w}if… {w}I'm lying."
        dv "Alright."
        "She loosened her grip and nodded at the already familiar «USSR» dragging a red conical bucket filled to the brim with muddy water from a fire barrel.."
        dv "Our newbie wants to penalize himself! Let's give him this chance!"
        "She exclaimed and I finally got a good look at her."
        th "Damn, she's good!"
        "Red hair, not red like «USSR» had, but more copper-ish."
        "Amber - to redness - eyes, an expression of a certain arrogance - in general, I immediately recognized that in front of me was a real daredevil."
        us "Are you sure?"
        show us laugh2 sport at right with dissolve
        dv "No."
        "Elder redhead licked her lips."
        dv "But we'll catch him if he tries anything funny, yeah?"
        show us smile sport at right with dissolve
        us "Right!"
        us "Now I'll…"
        "I grabbed the bucket…"
        me "Second degree of embarassment!"
        play sound sfx_water_emerge
        "…and with one huge wave doused both at once!"
        $ lp_dv += 1
        show dv shocked pioneer2 at center
        show us fear sport at right
        with dspr
        me "How do you like my penalty?!"
        "I burst out laughing and, turning around, instantly dashed away."
        us "Liar! Get the liar!"
        dv "Get him!"
    else:
        $ lp_dv -= 1
        $ lp_sl += 1
        "I twitched with all my might."
        "Useless!"
        dv "Come on, faster!"
        show us laugh2 sport far at right with dspr
        us "I'm coming, I'm coming!"
        "A child's voice, out of breath as if its owner was carrying something… {w}heavy?"
        me "Aaaaagh… Let me go, you bastards!"
        "I thrashed, trying to escape, already realizing what was about to happen."
        "Useless!"
        show us laugh2 sport at right behind dv with dspr
        "The red-haired enemy only squeezed my neck harder, blocking the remnants of oxygen."
        play sound sfx_water_emerge
        pause(1)
        stop music fadeout 3
        "All that was left is to accept the humiliation."
        "Another humiliation in a new society. I wonder, what does love for people have to do with it?"
        dv "Welcome to the camp!"
        "An abandoned bucket crashed next to me, and the laughter faded away."
        "Laughter from two voices, twice as offensive due to the fact that they laugh at me."
        hide dv
        hide us
        with dissolve
        "Red bitches."
        "Life's over, o cruel world…"
        "What the hell is this: I, a large, healthy dumbass of almost thirty years, was twisted and doused with water by two juvenile slobs!"
        with fade2
        "I waved my hand and smiled."
        th "I'm guilty anyways."
        "There was an extremely promising bench nearby, where I landed, after squeezing a sweater on myself."
        play music music_7dl["so_cold"] fadein 3
        "Drying up!"
        "Fortunately, for such moments of imminent humiliation, I, as the superhero «Loser Man», had an anti-crisis kit.."
        "A little bit of self-loathing, a little bit of black humor and a sea of self-irony."
        "You just need to start comprehending dao."
        "Alone."
        "It is not surprising that I constantly get into all sorts of incidents in a new place.."
        "Probably, there is some special difference that allows some people to go through life carefree, with a smile, to love today - as it happens with the one who met me at the gate."
        "This very difference constantly puts other people in stupid situations - I don’t know how else to call what is happening."
        "It's good that I took off my coat, otherwise it would have been even worse, in a wet winter coat ... hurr…"
        "Although there was this stupid insect scene at the entrance, I have no doubt that pranks, especially such cruel ones, are infrequent here.."
        th "I'm just a loser."
        "Having plunged into the abyss of self-pity, I completely disconnected from objective reality."
        "So I flinched when I was pushed on the shoulder."
        show sl normal pioneer with dspr
        sl "Why are you still here?"
        sl "Haven't I told you…"
        show sl surprise pioneer with dspr
        "The girl gasped and put her hands to her mouth."
        sl "So they did douse you in the end?"
        sl "Why didn’t you save yourself, I warned you that they would want to!"
        sl "Poor thing…"
        "She somehow very naturally, very mechanically reached out to pat me on the head, and I just as mechanically dodged."
        th "You just ruined the Zen recovery process, stupid blonde.."
        "I thought angrily."
        th "What the hell are you doing with your pity, I don't need pity from an underage bitch!"
        show sl sad pioneer with dspr
        sl "You're angry again."
        "She sighed."
        th "And who's to blame for that?"
        sl "Stop being so hatefully silent!"
        "It seems that even her dam of patience has its own capacity limits.."
        me "I don't need pity from nobody. Leave me, I'll dry up and find my way to squad leader."
        show sl serious pioneer with dspr
        sl "Yeah? How?"
        th "Dumb or anything? Sigh, one word - blonde."
        th "You literally gave me the ma…"
        "I took out a brown something from my pocket, on which it was impossible to make out anything at all.."
        sl "Thought so."
        "She nodded."
        sl "But you can't walk in damp clothes, you'll catch a cold!"
        th "No thanks mom, I've had enough."
        sl "Come on, let's quickly introduce you to Olga Dmitrievna and look for something to change into for you. {w}Let's go!"
        "She jumped up and pulled me along."
    with fade
    return

label alt_day1_chase1:
    scene bg ext_square_day at fast_running
    with flash
    "The stomping behind my back did not stop, but being fueled by adrenaline I squeezed out of my legs a speed so fast, that I had not reached for a long time."
    "Laughing my ass off, I crossed the square in the other direction."
    "Waved to the bronze dunce…"
    scene bg ext_aidpost_day at fast_running
    with flash
    "…ran past some building with a flag."
    th "Red cross? Infirmary?"
    th "Now that's going to be relevant if I fail to outrun them!"
    scene bg ext_dining_hall_away_day at fast_running
    with flash
    "I accelerated."
    "Passed yet another building like a hurricane - it looked like the canteen!"
    scene bg ext_warehouse2_day_7dl with dspr
    "…and popped out right next to a warehouse."
    stop ambience fadeout 6
    stop music fadeout 6
    with fade
    return

label alt_day1_warehouse:
    scene bg ext_warehouse2_day_7dl with fade
    play ambience ambience_camp_center_day fadein 2
    th "Seems like I lost them."
    "It looks like I can hide from the chasers here. At least for the time being."
    "Looking for a more comfortable place, I plopped down on a bench, threw off my wet sweater and hung it on the fence."
    "I searched my pockets for cigarettes, but did not find them. Well, okay."
    th "I have this feeling that I've forgotten something…"
    th "The coat! My passport and a bit of money are in it! How could I forget it in the bus!"
    "However, after the warm welcome that they gave me in the camp, to be honest, I didn’t want to go anywhere."
    th "Gonna take a break."
    sl "Oh, and what are you doing here?"
    "I heard a voice, familiar to me by now."
    show sl surprise pioneer with dissolve
    play music music_list["take_me_beautifully"] fadein 1
    "From one of the sheds came the girl I met at the gate."
    "She didn't look as neat as before - her shirt was smeared with something."
    sl "I told you to navigate from the square to the houses, and where did you go?"
    menu:
        "Another coincidence?":
            $ karma += 10
            $ lp_sl += 1
            "I smiled."
            me "It seems that I'm tailing you now."
        "Well, something happened…":
            sl "Something?"
            "I shrugged."
            me "Don't bother."
    if alt_day1_sl_ignored:
        sl "How are you feeling? Better?"
        me "Well, as you can see, I'm here in front of you, and I'm not lying somewhere with my hands up."
        th "Even better - I was running."
        show sl smile pioneer with dspr
        sl "That's better."
        "The girl smiled."
        sl "Glad you're feeling better."
    show sl surprise pioneer with dissolve
    sl "Ah, I didn't introduce myself."
    show sl smile pioneer with dspr
    $ meet('sl','Slavya')
    sl "My name is Slavya! Actually, my full name is Slavyana, but everyone calls me Slavya."
    $ alt_day1_sl_met = True
    "She nodded approvingly."
    sl "You can call me that too."
    me "Alright."
    show sl smile2 pioneer with dspr
    sl "Wait for me a minute, okay? I need to do something else, and we will go to Olga Dmitrievna together."
    hide sl with dissolve
    "I nodded."
    "After these words, she again disappeared into the bowels of the warehouse, and I finally decided to take off my heavy winter boots, tie them with laces, as in childhood, to throw over my shoulder."
    "I spent the time before Slavya's return by thinking about the {i}pioneers{/i}."
    "For me most part, they all behaved in the highest degree normal: the girl who was frightened by locusts, the lively Slavya, those two bandits - they all behaved as it should be for children in a pioneer camp."
    "Traces of some insidious plot could not be found, as well as the sinister goals of the one who threw me here."
    "But they should have."
    "People don't just warp into summer out of winter."
    "Until now, I thought that this could only happen on the pages of a science fiction novel or in films, but now I myself have found myself in the epicenter of events.."
    "And it's not clear whether this happened with a certain purpose, the highest intention of which is not yet clear to me, or simply - at the behest of Random."
    sl "Shall we go?"
    show sl smile pioneer with dspr
    me "Let's go…"
    "I answered, grabbing my sweater off the fence."
    "Her attitude towards me... To tell the truth, I already forgot when someone just took care of me."
    "And that was making her attempts to help warm up my soul even more."
    th "It's all rather suspicious though, isn't it?"
    stop ambience fadeout 6
    stop music fadeout 3
    pause(3)
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_houses_day
    show sl normal pioneer
    with dissolve
    if herc:
        "A place that almost witnessed my disgrace."
        "To tell the truth, I did not expect such agility from myself!"
        "I would be lying if I said that I did not like the situation."
        me "Here they wanted to douse me."
        sl "Really? Who?"
        me "How should I know? Two redheads, one older, the other younger, both with tails."
        show sl laugh pioneer with dspr
        sl "Oh, so you managed to deal with Alisa? How?"
        me "I remembered that girls should be carried in arms."
        "I smiled."
    elif loki:
        "We made our way back to where I started my run to the beach."
        "The evil in the face of two red-haired vermin was overturned, and I could not help but to smile."
        sl "What are you smiling at, Semyon?"
        sl "Just don't tell me that you're smiling at me: you're not even looking at me."
        "There was also a conical red bucket lying around, which Slavya, shaking her head, picked up and hung on the hook of the nearest fire shield."
        me "I just know where this bucket comes from and why there is spilled water."
        sl "You know something?"
        me "Let's just say I did to other people what they wanted to do to me."
        show sl laugh pioneer with dspr
        "Slavya laughed softly and did not ask anything else."
    "We turned near the nearest house and, walking along an improvised street, ran into another house, the unusualness of which was immediately evident."
    stop music fadeout 4
    stop ambience fadeout 6
    with fade
    return

label alt_day1_mod_tan:
    scene bg ext_house_of_mt_day with fade
    show sl normal pioneer
    with dissolve
    play music music_list["smooth_machine"] fadein 2
    "The house was funny - the kind children usually draw: triangular, with one door."
    "It, and the lilac bushes conquering space for themselves, formed into a still life of amazing beauty, worthy of the brush of any artist."
    th "Or was it a landscape?"
    sl "What are you waiting for? Let's go!"
    if alt_day1_sl_met:
        "Slavya brought me out of my thoughts."
    else:
        "I was brought out of my thoughts."
    with fade
    if (counter_sl_7dl == 1):
        if herc or loki:
            "Then a thought came into my head that I probably should have voiced…"
            "At least out of courtesy!"
            me "Ahem…"
            "I furrowed."
            me "It's not like I'm insisting."
            me "But we haven't introduced ourselves, yes?"
            show sl laugh pioneer at center with dissolve
            "She burst into laughter."
            sl "You're right, sorry."
            sl "I'm Slavyana."
            $ meet('sl','Slavya')
            $ alt_day1_sl_met = True
            me "Got it."
            "I shut up."
            "And was silent for a long time."
            "Until the girl's patience ran out."
            show sl serious pioneer with dspr
            sl "Aren't you going to say 'nice to meet you'?"
            th "How wonderful."
            th "It is nice, or is it?"
            me "Uh. Yeah."
            "I agreed."
            show sl shy pioneer with dspr
            "After waiting a bit, the girl waved her hand - apparently, she realized that I'm hopeless."
        play sound sfx_knock_door7_polite
        pause(2)
        mt "Open!"
        if herc or loki:
            sl "Everyone in the camp calls me Slavya."
            sl "Just in case you're interested."
            "Without waiting for my answer, she pushed the door, and I had no choice but to follow her."
        stop ambience
        play sound sfx_open_dooor_campus_1
        play ambience ambience_int_cabin_day fadein 1
        scene bg int_house_of_mt_noitem_day_7dl
        show mt normal pioneer
        with dissolve
    else:
        if dr:
            "My escort, not giving me much time to think, dragged me along."
            show us laugh sport at left with dissolve
            "Passing at the door…"
            "I barely held myself back trying not to swear."
            hide us with easeoutleft
            sl "Don't worry, now, now…"
        else:
            "We already were ready to knock and enter…"
            "But we heard unfamiliar voices from the inside."
            mt "Don't you dare mock Lena, understood?!"
            voice "Olga Dmitrievna…"
            mt "Do you understand!?"
            "Squad leader's reaming someone."
            "The picture is as old as the world, and it is twice as pleasant that someone else is being scolded."
            if herc:
                "There were a couple of sun loungers laid out in front of the house, and I immediately climbed into one of them, grabbing an extremely well-lying cone along the way."
            else:
                "There were a couple of sun loungers laid out in front of the house, and I immediately climbed into one of them, hiding from the sun.."
            if alt_day1_sl_met:
                "Slavya sat down in the other one and calmly smiled in response to the questioning look.."
            th "Looks like the squad leader is exceptionally busy. However, judging by the childish voice that I hear… Nothing surprising."
            play sound sfx_open_door_kick
            with vpunch
            show us smile sport at right with dissolve
            "A moment later, the door swung open and a girl in a «USSR» T-shirt jumped out."
            if herc:
                th "Target acquired."
                "I knew the pinecone would come in hand."
                "Projectile landed straight in the middle of her back."
                show us dontlike sport at right with dspr
                us "Hey! What's wrong with you?"
                "She looked at me resentfully."
                me "Didn't overstrain yourself with water carrying?"
                us "Uuuuuuu…"
                hide us with moveoutright
                "She scratched her back and, looking at me badly, ran away.."
            elif loki:
                "I recognized the victim of the showering immediately and winked at her. She just frowned in response. Clearly she's up to some mischief."
                me "Hey, shortstack! How's the water?"
                show us dontlike sport at right with dspr
                us "…"
                hide us with moveoutright
                "She turned around and disappeared behind the houses."
            play sound sfx_open_dooor_campus_1
            show un normal pioneer far at left with dspr
            "The other girl exited not too long after."
            th "Lena, I think?"
            if persistent.alt_binder:
                if persistent.un_7dl_good_ussr or persistent.un_7dl_good_rf:
                    "I somehow instantly decided that it would be her. {w}Don't know why."
                    "Maybe because that name would fit her perfectly."
            sl "Lena, don't pay any attention to her and she'll get off you."
            $ meet('un','Lena')
            "Slavya gave her words of encouragement."
            if persistent.alt_binder:
                if persistent.un_7dl_good_ussr or persistent.un_7dl_good_rf:
                    th "Look! What did I say?"
            else:
                th "Lena, huh. Alright. Nice to meet you."
            un "I didn't…"
            show un normal pioneer at left with dspr
            "She took a couple steps and noticed me."
            show un shy pioneer at left with dissolve
            "…and immediately stopped talking."
            "It seems like I embarassed her."
            "Blushing, the girl stared at the ground and tried to get out of sight as quickly as possible."
            hide un with moveoutleft
            "And I turned around and followed her with a thoughtful look."
            th "I wonder, is it just her, or is it my bad influence?"
            show sl normal pioneer at center with dspr
            sl "We're being waited, let's go!"
        play sound sfx_knock_door7_polite
        pause(2)
        mt "Open!"
        stop ambience fadeout 5
        play sound sfx_open_dooor_campus_1
        pause(1)
        play ambience ambience_int_cabin_day fadein 1
        scene bg int_house_of_mt_noitem_day_7dl
        with dissolve

    "Inside, the house looked exactly as expected: two beds, a table, chairs, a couple of cabinets and a poster with the incomparable Jean Marais as Fantômas."
    "Nothing supernatural, although in terms of the messiness this house could easily rival my apartment."
    show mt normal pioneer far with dissolve
    "Near the window stood a girl about my age reading something in a diary."
    "And, of course, like all the other representatives of the fair sex that I met here, nature did not deprive her of either face or figure."
    th "The only pleasing thing - I will be dying in the company of beautiful ladies. If I will, of course."
    show mt normal pioneer with dspr
    mt "Ah, here you are."
    if dr and (counter_sl_7dl != 1):
        "She looked at my clothes skeptically and shook her head.."
        mt "Got doused, I see. Okay, Slavya will pick something up for you. Drop the wet clothes."
        "Going to the closet, she rummaged around and found an oversized T-shirt - obviously from a store for very large people - and threw it to me."
        mt "Wear this for now."
        th "What about pants?"
        me "Mhm…"
        mt "Sit here for now. Slavya, get him forty-sixth.. no, forty-eighth size would be better."
        "Nodding, the girl took out a notebook from her pocket and diligently entered my measurements there."
        "And the T-shirt really turned out to be dimensionless - I wiped myself with the offered towel and, having put it on, found myself as if in a huge nightgown."
    else:
        mt "The bus came about an hour ago, where were you all this time? Don't tell me you were sleeping?"
        me "Um… Well, yeah."
        mt "Alright, sleepyhead."
    show mt smile pioneer with dissolve
    mt "My name is Olga Dmitrievna, and I am your squad leader."
    $ meet('mt','Olga Dmitrievna')
    mt "You seem like you're already familiar with Slavya."
    mt "She is my assistant, so if any questions arise — you can ask her."
    show sl smile pioneer at right with dissolve
    if alt_day1_sl_met:
        "Slavya smiled."
    else:
        $ meet('sl','Slavya')
        $ alt_day1_sl_met = True
        "Aforementioned assistant smiled."
    "Apparently they thought it was very funny. Well, I decided to play along."
    me "Squad leader, right. And I'm, apparently, a pioneer?"
    show mt angry pioneer at center with dspr
    mt "Don't twist words."
    mt "You are now a part of the squad; thus, I must make an exemplary pioneer out of you."
    me  "Oh please, would you look at me."
    "Frankly, I started scoffing already."
    me "Do I look like a pioneer?"
    show sl normal pioneer at right with dspr
    "Olga was silent for a couple of minutes, thoughtfully studying my face, and, as if that wasn't enough, Slavya also walked around me."
    sl "Please correct me if I'm wrong… But you do look like one."
    mt "I think so too."
    me "Alright, girls."
    "I decided to curtail this amateur performance."
    me "You joked, I laughed, show's over."
    show sl serious pioneer at right with dspr
    sl "You're rambling. Should I go get the nurse?"
    mt "Good thinking, Slavya. Please bring doctor Viola here."
    show sl surprise pioneer at right with dspr
    "Slavya reacted strangely to the word «doctor» — looked sideways at the squad leader and raised her eyebrow in a silent question."
    "But, without waiting for an answer, went out into the street."
    hide sl with dissolve
    me "What doctor Viola?! Are you all out of your mind here? Stop it, it's not funny anymo…"
    "I stopped when Olga crossed the room with two quick steps and, taking me by the shoulder, turned me to the mirror."
    stop music fadeout 3
    me "Oh…"
    me "…my…"
    me "…fuc…"
    play sound sfx_open_cabinet_2
    play music music_list["revenga"] fadein 3
    scene cg d1_me_dahell_7dl:
        pause 0.5
        linear 0.05 pos (-5,-5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (5,5)
        linear 0.05 pos (5,0)
        linear 0.05 pos (0,0)
        linear 0.05 pos (-5,-5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (5,5)
        linear 0.05 pos (0,5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (-5,-5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (5,5)
        linear 0.05 pos (0,5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (-5,-5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (5,5)
        linear 0.05 pos (0,0)
    with dissolve
    "I refused to believe what I saw in the mirror."
    "A comrade of eighteen years old looked out from under the bangs, as if slightly reduced relative to the real me."
    "And here I was wondering why my pants were falling off, why my boots didn't sit right…"
    "Riddle of the earplugs was, too, solved instantly."
    "There was just a sheer trifle left. To realize…"
    me "IS THAT ME?"
    scene bg int_house_of_mt_noitem_day_7dl
    show mt normal pioneer at center
    with dissolve
    "The ceiling swirled and began to fall back."
    show blinking
    pause(3.5)
    me "I don't know what you did to me, but give me back - myself! You! I…"
    play sound sfx_punch_medium
    with vpunch
    scene anim prolog_1
    with fade3
    "Finally, the floor jumped up and with all its might hit me on the troubled head."
    pause(3)
    stop music fadeout 5
    mt "Slavya, when is Violetta Cernovna coming?"
    sl "In five minutes, Olga Dmitrievna. She said she needs to grab some medicine."
    mt "If only she would be faster."
    "I shook my head and tried to get up."
    "Unfortunately, my strength completely left me, and all I could do was stare blankly at the ceiling.."
    scene bg int_house_of_mt_noitem_day_7dl with dissolve
    "I felt someone gently squeeze my fingers."
    sl "Please don't worry, okay?!"
    sl "I already called the nurse. She is the best here, she will instantly put you on your feet."
    cs "Pioneer, do not console the boy, it can damage his self-esteem."
    "There was a new voice in the room."
    "Oh, we have a new actor here. The local bestiary shines with variety."
    "So, who will it be?"
    scene bg int_house_of_mt_noitem_day_7dl with dissolve
    show mt normal pioneer far at left
    show sl normal pioneer far at right
    with dissolve
    play music music_list["eternal_longing"] fadein 5
    show cs normal with dspr
    cs "Violetta Cernovna Collider."
    show cs grin with dspr
    show cs normal with dspr
    "She winked."
    cs "But you can just call me {i}Viola{/i}… pioneer."
    $ meet('cs','Viola')
    show cs normal close with dspr
    "Her hands quickly ran over my body, checking reflexes, lymph nodes, breathing… Althought I could swear she… she was sexually harassing me!"
    show sl angry pioneer far at right with dspr
    "I blushed deeply. And Slavya, seeing my reaction, seemed to have guessed something and looked suspiciously at the nurse."
    sl "Violetta Cernovna, what can you say about Semyon's condition?"
    cs "A regular healthy pioneer. Slightly overheated, add in acclimatization."
    cs "Let him sleep for a couple of days and avoid the sun."
    "Viola summed up, waving a cotton swab with ammonia under my nose." with vpunch
    cs "When he comes to his senses, give him some broth to drink - I will arrange so that the kitchen prepares separately for Persunov."
    if herc:
        th "Persunov? How does she know my old name?"
    cs "In the evening he can have kefir and a couple of buns."
    cs "And no early wakeups. Isn't that right… pioneer?"
    show cs grin with dspr
    show cs normal with dspr
    "She looked at me meaningfully and winked again."
    me "Right. That's harmful for me."
    "When she finished her inspection, she gave me another meaningful look, so I hurried to straighten my T-shirt - and disappeared through the door."
    stop music fadeout 3
    hide cs with dissolve
    show sl normal pioneer at right with dspr
    mt "Perfect. Semyon, once come to your senses - march to the warehouse."
    mt "Get yourself a mattress and bedsheets. A pioneer must take care of his own bed."
    "I looked at Slavya."
    sl "I'll meet you there!"
    "Convinced that nothing threatened my health, Slavya smiled and followed the nurse."
    hide sl with dissolve
    show mt normal pioneer at center with dspr
    mt "I should also go."
    mt "Settle down here for now, we'll find you a place later."
    mt "Supper's scheduled to be later in the evening, don't forget about that."
    me "Uhhh… What about that broth?"
    mt "Make your bed first, then go to the canteen."
    "Squad leader stated categorically."
    mt "Will you manage?"
    me "I'll try."
    mt "That's good. See you when it's supper."
    hide mt with dissolve
    "She fluttered out the door after Slavya."
    me "Where do I carry the clothes?"
    "I asked the void. With a completely expected result."
    if dr and (counter_sl_7dl != 1):
        "My damp things took over the closet and a couple of hangers, so I was left only in the leader's T-shirt - not the best outfit, but much better than walking around soaking wet."
    else:
        "I successfully lost the coat on the bus, so it was up to the sweater - I immediately got rid of it, hung it on the back of the bed, and took off my shoes, vowing to myself either to get proper shoes for the weather, or to go barefoot."
        "I stayed in a single «Indigo Denim» T-shirt and wondered if it would be too provocative to wear such things in the Soviet camp."
        "After a moment of thought, I decided that a T-shirt would be more appropriate in the summer than a sweater. Even with the bourgeois inscription on the chest."
        th "In the end, the little one over there in the USSR shirt runs around, and everything's fine. How am I worse? I will commune the masses to woven cotton."
    stop music fadeout 4
    stop ambience fadeout 6
    with fade
    return

label alt_day1_elektron:
    scene bg ext_houses_day with dissolve
    play music music_list["everyday_theme"] fadein 3
    "Well, I can look for answers to questions on a full stomach."
    "As in the very proverb about the fact that a Russian on an empty stomach does not want to think or do."
    "And if it's full - he can't."
    "I was walking along the path, and someone called out to me."
    el "Hey!"
    "I looked back."
    show el normal pioneer with dissolve
    "Wow, the first male creature that I managed to meet."
    "A disheveled guy with a scattering of small freckles. Classic mid face."
    "We already have a Semyon, which means either Vasily or Sergey, yup."
    if dr and (counter_sl_7dl != 1):
        el "You forgot to put on pants!"
        "He shared with me."
        me "That was intentional."
        "I gloomily noted."
        show el surprise pioneer with dspr
        el "Yeah? Alright then."
        "He shook his head thoughtfully, but then immediately stood up straight:"
        show el normal pioneer with dissolve
    el "Hello!"
    "He stretched out his hand."
    el "Nice to meet you, I'm — Electronik! {w}A real one. You can call me that."
    "A real Electronik. {w=.3}Of-{w=.3}god damn-{w=.3}course. {w}And under his shirt he's hiding a power plug."
    "Cosplayer, right? The Russian land is not scarce with idiots."
    $ meet('el','Electronik')
    me "Got it…"
    el "Ulyanka also calls me Syroezhka."
    "Judging by the disgruntled expression on his face, he categorically did not like this nickname."
    th "You know, that's pretty accurate. You'd have to try hard to find a shroom like him."
    el "That's my last name. Syroezhkin."
    me "Yeah, thought so. You just… don't worry, okay?"
    "Unfortunately, his handshake was firm enough that I didn't have time to take my hand away. And he has already switched to a new topic."
    el "How can I not worry? We need to bring you bedding, and show so much more in the camp to you. Let's go, faster."
    "He turned to the right and, not looking to see if I was following him, rushed towards the square."
    el "Is it true that you came in winter clothes?"
    if dr and (counter_sl_7dl != 1):
        me "What, does it look like that?"
        "I responded sarcastically."
        el "Not really."
        show el serious pioneer with dspr
        el "Ulyanka gossiping again!"
        "He honestly replied."
        me "Ulyanka?"
        el "Small, red, mischievous!"
        me "Ah, her."
        show el normal pioneer with dspr
        me "Listen more to this leech."
        "I was not too comfortable in a makeshift mini dress, which affected my sense of humor."
    else:
        "I examined myself carefully. T-shirt, jeans, barefoot…"
        me "Nah, lies and slander."
        el "That's what I thought too! This is Ulyanka spreading gossip again!"
        me "Ulyanka is the one that…"
        el "Small, red, mischievous!"
    if (counter_sl_7dl == 1):
        el "She, in general, has little credibility, but girls can believe."
    else:
        el "She says you came in a sheepskin coat, sweared and behaved disgustingly."
    if dr and (counter_sl_7dl != 1):
        el "I don't think you should be led through the square like this."
        me "I agree!"
        el "We'll take a roundabout route then?"
        me "I agree to that too!"
    with fade2
    pause(2)
    play ambience ambience_day_countryside_ambience fadein 3
    scene bg ext_warehouse_day_7dl with dissolve
    "After a couple of minutes, we were already approaching a gray shed with a huge gate on the front side."
    show el grin pioneer with dspr
    el "Don't think it's just like that on the outside. Inside there is isolation and everything is clean. After all, there’s not only bedding, there’s also all kinds of inventory, and skis, and balls ... Yeeeeah."
    me "Skis? What, there are also winter shifts?!"
    show el serious pioneer with dspr
    el "I wasn't that lucky yet."
    show el smile pioneer with dspr
    el "They say it's a lot of fun here on New Year's Eve. They dress up Genda, they bring a Christmas tree from the land, a huge blue one!"
    show el sad pioneer with dspr
    el "Oh I wish I could see this."
    me "Eh, you'll manage eventually."
    "He had already begun to frankly annoy me with his chatter, so I hastened to remind him of the purpose of the walk."
    me "Lead to the castellan, or whoever is in charge of your beds."
    "We walked around the building and approached the wide open door."
    scene bg int_warehouse_day_7dl with dissolve
    "Through it one could see a semi-dark room with three-story wooden shelves, on each of which lay rolled-up mattresses; the filling was a pillow wrapped in a thin woolen blanket."
    sl "Oh, hey guys, hold up. I'll come out soon."
    pause(1)
    show sl shy sport at center
    show el normal pioneer at left
    with dissolve
    "A few minutes later, a disheveled and blushing Slavya appeared from behind the shelves, tugging at her clothes."
    el "Uhhh… Do you want to tell us something?"
    "Electronik carefully inquired."
    "I stood in a stupor, as I always did, when I accidentally found myself drawn into other people's secrets."
    show el normal pioneer at left with dspr
    if dr and (counter_sl_7dl != 1):
        "However, now there were much more pressing issues."
        "I looked expressively at Slavya, and she handed me a package:"
        sl "If it will suddenly press somewhere, contact me: I will surely exchange."
        me "Thanks!"
        sl "Take beddings too - take it to Olga Dmitrievna for now, then to wherever she'll lodge you."
    else:
        me "I definitely don't understand something. Could you just bring me here and…"
        sl "…And control the broth handout, the issuing of uniforms, the ironing of the shirt, the setting for allowance and a whole bunch of other subtle moments?"
        show sl laugh sport with dspr
        "Slavya laughed when she saw my eyes square up."
        me "Oops…"
        sl "Apology accepted. Grab any bed you like."
        me "Okay."
        sl "I'll iron out the form and put it in order, but for today use your civilian clothes, alright?"
        "I responded with a nod."
    show sl surprise sport at center with dspr
    sl "Oh, almost forgot!"
    sl "What's your foot size?"
    me "45."
    show sl normal sport at center with dspr
    "Slavya looked at me strangely.{w} More accurately, at my feet."
    "Well, what did you expect? At my…"
    th "Shit!"
    th "Currently I'm way younger than my real self, how can it be 45th?"
    th "Though it doesn't look like much has changed."
    hide sl with dissolve
    "Noticing my confusion, Slavya, without waiting for an answer, disappeared behind the shelves{w=0.5}{nw}"
    show sl smile sport at center with dissolve
    extend ", and a minute later returned with a pair of sandals."
    "Anything's better than walking barefoot."
    "Even if there are no drunken tourists throwing broken glass into the grass, there are always bumps and pebbles that are somewhat unpleasant to step on with bare feet."
    sl "Try these. If they don't fit, I'll get another pair."
    th "Picked by eye?"
    sl "And don't wear socks yet. Put them on after you wash your feet."
    th "Thanks, mom."
    "However, Slavya's eye turned out to be trained - the sandals were just right."
    "Without socks, of course, the sensations were not very pleasant: feet stuck to the soles, and I will probably rub off a heel, but it's still better than barefoot."
    me "Thanks, Slavya."
    sl "Have fun!"
    hide sl with dissolve
    scene bg ext_square_day with dissolve
    if dr and (counter_sl_7dl != 1):
        "A few minutes later, having changed and put myself in order, I got out into the street, where Electronik was already waiting."
        "He seemed to be itching to continue the tour."
    else:
        "A few minutes later, having dropped off the bed in the squad leader's house, I was already moving towards the square."
    stop music fadeout 4
    stop ambience fadeout 6
    with fade
    return

label alt_day1_meeting:
    scene bg ext_square_day
    show el normal pioneer at left
    with dissolve
    play music music_list["get_to_know_me_better"] fadein 3
    play ambience ambience_camp_center_day fadein 3
    el "Let's start the tour from the square. There are all our sights, Genda and…"
    me "And?"
    "I skeptically raised an eyebrow."
    el "And…"
    "He looked lost{w=0.5}{nw}"
    show el laugh pioneer at cleft with dspr
    extend " — and suddenly lit up."
    el "And — Lena!"
    el "Look, Semyon. Lena!"
    show un normal pioneer far at cright behind el with dspr
    th "I wouldn't argue, Lena — is a quite prominent girl. But calling her a landmark…"
    "I stifled a laugh."
    me "Does she know what you just called her?"
    el "Of course."
    show el laugh pioneer far with dspr
    show un surprise pioneer far with dspr
    "He jumped up to the girl and started chattering."
    el "Lena, hello! This is the new guy! Say hello."
    $ meet ('un', 'Lena')
    with fade2
    th "And what is she supposed to say?!"
    "Thoughts rushed around in panic."
    me "Hi."
    me "We already know each other, kind of."
    show un shy pioneer far with dspr
    un "Yes…"
    "She looked up from her book for a second, looked at me, and immediately, blushing to her ears, hid behind the book, trying her best not to notice our presence.."
    "I smiled involuntarily: that's how much her behavior resembled my own."
    "But nah, I won't blush — I'm too old for that."
    "But in general, the attempt to hide from the interlocutor is close and understandable to me."
    show cg d1_me_dahell_7dl with dissolve:
        alpha 0.5
    "However, judging by the picture in the mirror, my old age remained on the frosty streets of the city."
    hide cg
    show el normal pioneer far
    with dspr
    el "Ok, let's go further, there are still a lot of sights waiting."
    "That's all, folks!"
    "It seems that it was enough for Electronik to say hello to a person to consider him almost a friend. {w}And then there's me, who forgets the name of a person five seconds after it was spoken."
    show el normal pioneer with dspr
    me "It was nice to meet you, Lena!"
    "I shouted over my shoulder, carried on by the indefatigable guide."
    "Lena shuddered and, although it seemed fantastic to me, she blushed even more."
    hide un with dissolve
    with fade2
    me "So, what other sights are on our seeing menu?"
    el "Hold on, hold on…"
    scene bg ext_dining_hall_away_day
    with dissolve
    "We were already approaching a new object of interest. As it was easy to guess from the squattish outlines, in front of us was the canteen."
    el "And here we have…"
    me "Yeah, I already figured it out. We intake organic foods here."
    if (counter_sl_7dl != 1):
        "The red-haired bandit was here and reacted to the last remark with a restrained chuckle."
    else:
        "On the porch stood a girl with red hair, pinned into two tails. She accepted my flat witticism approvingly and even grinned."
    "Apparently, my jokes from Evgeny Vaganych are going to be fairly popular."
    scene bg ext_dining_hall_near_day
    show el normal pioneer close at right
    show dv normal pioneer2 far at left
    with dspr
    el "And that is…"
    "Electronik switched to a whisper that only the deaf would not hear."
    el "Our Alisa. She's always in a bad mood."
    $ meet('dv','Alisa')
    "A fire girl, splashing girl…"
    me "She's that mad?"
    el "No, she's just…"
    stop music fadeout 3
    stop ambience fadeout 3
    el "Her last name is Dvachevskaya, but if you try calling her «DvaChe»…"
    pause(3)
    play music music_list["awakening_power"] fadein 2
    show dv angry pioneer2 far at left with dspr
    dv "What the hell did you just say?"
    show dv angry pioneer2
    show el scared pioneer close
    with dspr
    "Alisa immediately jumped off the porch and started heading our way."
    el "Uhhh… Alright, you're on your own now!"
    hide el with dissolve
    me "What?"
    "I asked air with an excessively 'smart' face."
    "Electronik has already vanished, and I, for some reason, froze up and watched my imminent demise approach."
    menu:
        "Run after him":
            $ alt_day1_el_followed = True
            stop music fadeout 3
            "Deciding that it was better not to tease the geese, I ran after Electronik and soon caught up with him."
            scene bg ext_warehouse_day_7dl
            with dissolve
            play ambience ambience_camp_center_day fadein 2
            "After a little thought, he sharply turned in the direction of the warehouses…"
            "…and, not reaching them, jumped straight from the path into the thick grass."
            "I, struggling with the laughter choking me, hid nearby."
            "Alisa, completely pissed off, rushed along the path without looking around and disappeared behind the warehouse."
            "After waiting a few minutes to calm down, Electronik breathed a sigh of relief and got out of the grass."
            show el smile pioneer with dspr
            el "Well, seems like we lost her."
            "His look left much to be desired. Looks like diving into the grass didn't go as planned."
            el "She thinks she knows where to look for me. Now she will turn to the club will try to ambush me there. And I won't go there.{w} Too dangerous!"
            "I already guessed what could come out of being ambushed by Dvachevskaya, so I nodded sympathetically."
            el "Oh well, we just need to survive until supper, and then we'll be out of the woods. {w}At least I think so."
            "He looked with displeasure at his clothes stained with herbal juices."
            el "Urgh, dirtied my clothes. Alright, go somewhere by yourself, and I'll clean up in the meantime. See you at supper."
            stop ambience fadeout 2
            hide el with dissolve
            "After a little thought, I went to the side, where I heard elastic blows on the ball.."
            "Looks like they are playing football."
        "Do nothing":
            $ karma += 10
            $ lp_dv += 1
            show dv angry pioneer2 close at left with dspr
            "Coming up to me, she gave me a particularly evil look from her arsenal."
            dv "Oh, we'll also talk with you alright!"
            if loki and (counter_sl_7dl != 1):
                me "What, you'll bring me another bucket?"
                $ karma -= 10
                "With a laugh, I dodged a hand that flashed in the air."
                show dv rage pioneer2 close at left with dspr
                "She spat out of anger and, turning around, rushed off after Electronik."
            elif herc and (counter_sl_7dl != 1):
                me "Liked the ride?"
                $ karma += 10
                "I was ready to grab the impudent girl, and it seems that she read this intention in my eyes."
                show dv rage pioneer2 close at left with dspr
                "She spat out of anger and, turning around, rushed off after Electronik."
            else:
                me "Who? Me? I didn't do anything."
                if dr and (counter_sl_7dl != 1):
                    "I mumbled."
                    "After the impromtu shower, I didn’t want to mess with the redhead at all."
                else:
                    "I shrugged."
                    "Other people's problems definitely didn't concern me."
                    "I added a smile to the gesture.{w} Somehow it looked guilty."
                "Without honoring me with an answer, Dvachevskaya rushed after Electronik."
            stop music fadeout 5
            hide dv with dissolve
            with fade2
            th "Apparently, no one will bother me, and the time before supper can be devoted to blissful idleness."
            "I randomly chose a direction and went to the side where elastic blows on the ball were heard - they were obviously playing football there."
    stop music fadeout 4
    stop ambience fadeout 6
    with fade
    return

label alt_day1_soccer_d1:
    scene bg ext_playground_day
    with dissolve
    play ambience ambience_soccer_play_background fadein 2
    play music music_list["went_fishing_caught_a_girl"] fadein 2
    "Some time later, I reached the place I was looking for, and, sitting on one of the benches standing around the perimeter of the field, stared thoughtfully at the field."
    "The match was in full swing, and I couldn't help staring."
    "Once upon a time I was good at handling the ball, but my priorities never included sports."
    "Children briskly rushed around the field, but even from the constantly moving crowd, one stood out - the fastest, most restless."
    "Oh, I immediately recognized the red-hair."
    if (counter_sl_7dl == 1):
        "That's true!"
        "Slavya didn’t let her do dirty things - but you have to release the energy somehow."
    else:
        "She messed up, played pranks and with a pure soul and a clear conscience went to play football."
    scene bg ext_playground_day with dissolve
    "The ball rolled under my feet, and I, taking it on my foot, fired it back."
    play sound sfx_soccer_ball_kick
    th "Oh well… Not my best shot."
    show us laugh sport far with dissolve
    us "Hey, you!"
    "The girl shouted."
    if (counter_sl_7dl == 1):
        "I think Slavya called her Ulyana."
    else:
        "I think her name was Ulyana - if Electronik didn't lie to me."
    $ meet('us','Ulyana')
    us "Let's play!"
    "I pondered."
    th "Eh, why not?"
    if (counter_sl_7dl == 0) and dr:
        "Dirtying new uniform…"
    else:
        th "On the other hand, playing in sandals and warm trousers…"
    me "Maybe next time!"
    show us dontlike sport with dspr
    us "You're boring!"
    "After verbally flattening me, she went back into the game."
    hide us with dissolve
    "I got off the bench and, for a change, drew attention to the bars standing right there."
    scene bg ext_playground_day:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 2.0 zoom 1.5 xalign 0.55 yalign 0.55
    with dissolve
    "Not too long ago a certain word was popular - «workout», meaning the most trivial thing - love for hanging at the metal bars."
    "After watching a couple of videos on YouTube, I even began to hang on my horizontal bar in the yard, but quickly abandoned this idea."
    "But before I wasn't that bad! I need to see what kind of body they slipped over to me and whether it is able to pull itself up at least a dozen times."
    "Fingers, unaccustomed to loads, did not want to fit correctly."
    "Then the center of mass drifted somewhere."
    "Finally, yelling at myself, I jumped up and hung on the bar, keeping my back straight, and…"
    "One!"
    "Two!"
    "Three!"
    us "Four! Five!"
    with dissolve
    "An entire chorus rang out behind my back."
    if herc:
        "Startled in surprise, I nevertheless continued pulling up until I stopped at ten."
        scene bg ext_playground_day at zentercenter
        show us smile sport
        with dissolve
        us "What, that's it?"
        me "That's all that's needed!"
        me "Although you can always climb up and convince me otherwise!"
        play sound sfx_7dl["eat_horn"] fadein 1
        "Realizing that I wouldn't give in that easily, the girl wanted to return to the game, but she was interrupted by the horn."
    elif loki:
        th "Twenty five, fucking hell."
        th "What, found yourself some free entertainment?"
        "I instantly unclenched my hands and jumped to the ground."
        me "Show's over."
        "I bowed."
        show us dontlike sport with dspr
        us "Lazybones, that's who you are."
        if (counter_sl_7dl != 1):
            me "Keep calling me names and you're in for another shower!"
        play sound sfx_7dl["eat_horn"] fadein 1
        "The girl wanted to say something else offensive, but she was interrupted by the signals of the immortal «grab a spoon and grab some bread»."
    else:
        play sound sfx_punch_medium
        "Startled in surprise, I unclenched my hands and flopped to the ground." with vpunch
        us "Guhhhhh…"
        "The unnoticeably pulled up fans hummed disappointedly."
        scene bg ext_playground_day with flash
        th "They'll give me a heart attack at this rate."
        "I thought dissatisfiedly as I got up."
        show us smile sport with dspr
        us "Going to continue?"
        me "I won't. You haven't got your tickets."
        show us laugh sport with dspr
        us "And you don't look like a clown to me."
        th "Little asshole."
        th "As if happiness is in the number of pull-ups."
        play sound sfx_7dl["eat_horn"] fadein 1
        "I was just about to tell the redhead what I think of her and where she should go when the horn was sounded."
    show us grin sport with dspr
    us "Race to canteen! Last one's a rotten tomato!"
    hide us with dissolve
    "The children roared and, pushing, rushed towards the dining room."
    pause(1)
    if alt_day1_el_followed:
        th "Electronik didn't come."
        th "Maybe he won't come after all?"
        "It is true what they say: remember the sun - here is a ray."
        "I was about to leave, when Electronik ran up to me."
        show el smile pioneer with dspr
        el "Aaaaah. You did wait for me. Well, good. Let's go to the canteen before they eat everything!"
        "We headed to the canteen. Thankfully, I now knew where it was."
    else:
        "And I slowly followed them."
    stop sound fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day1_supper:
    scene bg ext_dining_hall_away_sunset with dissolve
    "Visiting the washbasins along the way and rinsing our hands with water that was cold to the point of aching fingers, we went into the dining room."
    play ambience ambience_dining_hall_full fadein 3
    scene bg int_dining_hall_people_sunset_7dl with fade
    "Well... A canteen's a canteen."
    "Long tables for twelve people lined up against the walls, tables a little shorter on the other side of the aisle so that the waiters with carts can get close and serve or clear the table."
    "Tiled walls and floor, stainless steel chairs and speakers on the ceiling in case it rains outside."
    "Small tables stood apart, apparently for the staff. Behind one of them, I saw a curvy girl about my age."
    show cs normal far at right with dissolve
    dreamgirl "Previous."
    th "What?"
    dreamgirl "Your previous age."
    if dr:
        th "Oh god, not you again…"
        dreamgirl "Did you miss me?"
    else:
        th "Who the hell are you?"
        dreamgirl "Your intuition, dumbass."
    "Looking closer, I recognized her as the nurse who examined me."
    th "Violetta, I think?"
    show cs smile far with dspr
    "Viola nodded in greeting."
    show mi serious pioneer far at left with dissolve
    "Place right next to her was occupied by that same «cyan» girl."
    show mi normal pioneer far with dspr
    "She quickly smiled at me, catching my gaze, and returned to her plate again."
    th "So she wasn't a dream?! {b}Cool{/b}!"
    th "I wonder how this camp treats turquoise-dyed hair?"
    hide cs
    hide mi
    with dissolve
    show mt normal pioneer at cright with dissolve
    mt "Semyon, do not stand like a pillar, otherwise you will be left without supper."
    "I flinched in surprise."
    "Squad leader crawled up completely unexpectedly to me."
    if dr and (counter_sl_7dl != 1):
        "Olga glanced at me from head to toe, slightly adjusted the collar, and nodded contentedly."
        show mt smile pioneer at cright with dissolve
        mt "Now you look like a proper pioneer."
        if d3:
            dreamgirl "Heh, beeroneer."
        else:
            dreamgirl "Heh, pioneer."
    show mt normal pioneer at left with move
    mt "Let's see, where would be a good place for you…{w=0.5}{nw}"
    show dv normal pioneer2 at right with dissolve
    show mt angry pioneer with ease
    extend " Dvachevskaya, stop right there!" with vpunch
    "She grabbed the red lightning bolt, rushing to the promised mashed potatoes with a cutlet, out of thin air."
    show dv surprise pioneer2 with dspr
    dv "Now what?"
    mt "What are you wearing?"
    dv "Uhh… My uniform?"
    if loki:
        if (counter_sl_7dl != 1):
            "I suppressed a chuckle - after the incident at the entrance to the camp, Alisa changed clothes, but she did it in her own way."
        "An unbuttoned shirt, knotted at the stomach, showing the absence of all unnecessary items of clothing underneath, a pioneer tie tied at the wrist."
        "This is how a true pioneer should be."
        mt "Fix your form, now!"
        show dv grin pioneer2 with dspr
        dv "Pffft… As you say."
        "She slowly pulled the knot of her shirt…"
        hide dv with dissolve
        show mt normal pioneer with dspr
        me "Turn back to the wall, good grief!"
        "I snapped."
        me "Or you'll interrupt supper for half the camp."
        dv "What didn't they see there…"
        show dv normal pioneer at cright with dspr
        "Alisa followed my advice and, having adjusted her uniform, sat down on the other side of the aisle, casually giving me sidelong glances."
        hide dv with dissolve
    elif herc:
        "My chuckle caught the attention of both the squad leader and Alisa. And if the first, judging by the laughing eyes, perfectly understood what I was playing at…"
        "…the latter took everything at face value."
        show dv grin pioneer2 with dspr
        "She put her hands on her hips and stretched coyly, emphasizing with a knotted shirt what she wanted to emphasize."
        me "It seems that someone confused the dining room with a rural disco…"
        show dv shy pioneer2 with dspr
        "I whispered, but for some reason half the dining room heard that."
        "Dvachevskaya blushed…"
        th "Whoa, even she knows what shame is?!"
        hide dv with dissolve
        "…and jumped out of the canteen, incinerating me with a look for the second time today."
        show mt normal pioneer with dspr
        me "Hope I didn't say anything unnecessary."
        show dv normal pioneer at right with dspr
        "Alisa returned half a minute later, having already adjusted her uniform and even partially smoothed out the wrinkle from the knot."
        "Giving me a very bad look, she took her place."
        hide dv with dissolve
    else:
        "I suppressed a laugh. It seems that the concept of uniform for Alisa was fundamentally different from the generally accepted."
        "An extremely provocatively worn shirt, held only by a knot just below the chest, a tie tied like a wristlet around the wrist, and two red lightning tails."
        "Gee, I wonder what's wrong with my uniform?"
        "That's exactly how a true pioneer should be."
        mt "Fix your form, now!"
        show dv grin pioneer2 with dspr
        dv "Pffft… As you say."
        "She slowly pulled the knot of her shirt…"
        show mt angry pioneer with dspr
        mt "Alisa!"
        dv "What?!"
        "Olga Dmitrievna thought a little and waved her hand."
        show mt normal pioneer with dspr
        show dv normal pioneer2 with dspr
        mt "Whatever, just go."
        hide dv with dissolve
    show mt normal pioneer with dspr
    mt "Alright, now we have to deal with you."
    "The squad leader led me to a couple of tables that, apparently, belonged to my squad, and, after a moment's thought, pointed to an empty seat next to the small redhair."
    mt "You'll be sitting here."
    me "Olga Dmitrievna, I have a stupid question."
    "I turned to the squad leader, realizing that sitting next to the small demon will have consequences."
    "Yes, and the recommendations of the kindest doctor Viola should also be followed."
    mt "Save all stupid questions until after supper. Sit down, let's eat."
    "Thus, the squad leader answered where she saw all these recommendations."
    "Apparently, I have exhausted the quota of stupid actions for today. Since there was nothing better to do, I had to sit down."
    "In the end, what's the difference with whom to sit, if the contents of the plate are more important to me, and not the environment."
    hide mt with dissolve
    show us smile sport with dissolve
    us "Hey, hey!"
    me "What do you want?"
    us "Why didn't you play with us?"
    if (counter_sl_7dl == 0) and dr:
        me "Didn't want to dirty my clothes."
    else:
        me "I had wrong clothes."
    us "What, were you going to play with your clothes?"
    mt "Ulyana, don't bother him."
    $ meet('us','Ulyana')
    "The squad leader made a remark."
    us "Fine, sit down and eat."
    show us grin sport with dspr
    hide us with dissolve
    "She winked and I turned to my plate."
    "Only to find out that the cutlet was gone!"
    "Putting two and two together, and taking her reputation into account, I turned to her."
    show us smile sport with dissolve
    us "You snooze - you lose."
    me "You little…"
    menu:
        "Demand the cutlet":
            $ karma += 10
            $ lp_us += 1
            "I looked menacingly at her and held out a plate."
            if loki:
                me "Ulechka, my sun. Let's not do anything stupid and return the cutlets to their owners, yes?"
                me "Or else these mashed potatoes will be on your head!"
            elif herc:
                me "Kid, don't be stubborn and return what you took."
            else:
                me "Ulyana. The cutlet. {w=.6}NOW."
            us "I don't even have it, look!"
            "She pointed to her plate, where there was less than half the potato portion and, of course, not a single cutlet."
            me "You… Ate…"
            show us normal sport with dspr
            us "Hold on."
        "Grab her plate":
            $ karma -= 10
            "A single sharp movement of the hand - and I have one more plate."
            show us dontlike sport with dspr
            us "Hey! Give it back! That's mine!"
            me "You snoozed and loosed, though?"
            us "Well, that's fine."
            "She folded her arms on her chest."
            us "Feel free to choke on these mashed potatoes. There are no cutlets."
            me "What do you mean there are none?!"
            "I stuck my nose into the plate to make sure that Ulyanka's words were true."
            "And in fact - there were no cutlets."
            me "Kiddo, don't you know that eating other people's cutlets is not only unhygienic, but also dangerous?"
            show us surp1 sport with dspr
            us "What?"
            me "I'll slap you, that's what!"
            show us smile sport with dspr
            us "Don't be so upset, we'll organize something now."
        "Ignore":
            $ lp_sl += 1
            $ karma += 10
            "I stoically ignored the provocation and began to eat mashed potatoes."
            show us sad sport with dspr
            us "Oh…"
            "Ulyana seemed to be upset by the loss herself."
            show us normal sport with dspr
            us "Don't be so upset, we'll organize something now."
    hide us with moveoutright
    "She instantly grabbed my plate and was gone."
    "Wonderful. In one supper, I lost both meat and garnish."
    dreamgirl "Did anyone tell you that you're an idiot? Life is full of pain."
    show us grin sport with dissolve
    "A few minutes later, Ulyanka returned with a new portion."
    us "Feast!"
    "She placed food in front of me."
    us "And remember my kindness!"
    hide us with dissolve
    me "Thank you very much!"
    "I thanked from the bottom of my heart, noting with the corner of my mind that the girl had already disappeared somewhere."
    th "She isn't as bad as I thought she was!"
    th "OK. The most important thing right now is proper and healthy nutrition."
    "The fact that I hadn’t eaten anything since morning made itself apparent, and I heartily poked a cutlet with a fork, getting ready to make my favorite dish mixed out of meat, mashed potatoes and peas out of the splendor on a plate."
    scene cg d1_food_normal with dissolve
    pause(1)
    "I was about to bite off the blessed fragrant piece of meat, when I suddenly noticed stirring on the plate."
    scene cg d1_food_skolop with dissolve
    play sound sfx_dropped_chair
    "Looking down at my plate, I jumped back, launching the chair against the wall."
    me "Jesus Christ, is this thing alive?!!"
    play music music_list["awakening_power"] fadein 2
    play sound sfx_suspence_bang
    scene cg d1_food_skolop:
        zoom 1.0 xalign 0.5 yalign 0.5
        linear 1.0 xalign 0.6 yalign 0.8 zoom 2.0
    pause(1)
    th "What is this, a centipede?! Alien larva?! Some other alien bastard?"
    play sound sfx_body_bump
    "I plopped down on the tiled floor with a scream."
    scene bg int_dining_hall_people_day with fade
    "The unknown creature unhurriedly turned around and, choosing a direction, accelerating, rushed…"
    "…straight at me!"
    me "AAAA-AA-A-A-A-a-A-A-A-Aa-A-a!"
    play sound sfx_chair_fall
    with vpunch
    "With a loud cry, I took a running start, moving exclusively on all fours, and even succeeded until I finished with the back of my head hitting the wall."
    "And the alien menace kept chasing me!"
    play sound sfx_punch_washstand
    with vpunch
    "Jokes are jokes, but for my hungry mind it turned out to be too much."
    "{i}And everyone will be rewarded according to his sins!{/i}"
    me "{b}ULYAAANAAAAAAAAAAAAA!!!{/b}"
    stop ambience fadeout 1
    stop music fadeout 2
    pause(1)
    "In the silence that suddenly descended on the canteen, my cry was especially loud."
    "And, judging by the contented giggle that flew from the door, it reached the ears of the addressee."
    show us laugh sport with dspr
    play music music_7dl["genki"]
    "But when she saw the expression on my face, she burst out laughing at the top of her voice!"
    us "Ah-hah-aha-haha-haha-ahaha-ha!"
    hide us with easeoutright
    "The red meteor rushed through the doors, rightly taking a head start."
    if (counter_sl_7dl == 1) and (lp_sl >= 3):
        "I suddenly felt someone's hand on my shoulder, and the voice, which I had heard only a barely perceptible muttering all this time because of anger, broke into intelligible words.."
        menu:
            "She'll get away!":
                "Tossing the hand away with a single motion, I charged ahead."
                "The little shit won't go unpunished!"
                $ karma -= 10
            "Now what?!":
                $ lp_sl += 1
                $ counter_sl_7dl = 2
                "I turned around abruptly."
                "Slavya was standing next to me, and all the other girls were a little further away."
                "Slavya was saying something to me in a cooing voice, but I managed to catch only the very end."
                show sl normal pioneer with dissolve
                sl "…attention! {w}She pisses off everyone like that! Tests that way."
                me "Even me?"
                "I spoke with great difficulty."
                show sl smile pioneer with dspr
                sl "And how are you different?"
                "She took out a piece of paper from her pocket and, deftly catching the centipede with it, sent it out the window."
                sl "Sit, I'll bring you something to eat."
                me "Why?"
                "I suspiciously stared at her."
                show sl laugh pioneer with dspr
                sl "You're asking questions like that! Aren't you hungry?"
                me "Hungry."
                sl "Yeah. {w}Come on, sit."
                hide sl with dissolve
                "She rode off to the kitchen, leaving me alone."
                "By that time, all of us had already managed to finish the meal, except that the red-haired Alisa was in no hurry."
                if dr:
                    show dv smile pioneer2 with dissolve
                else:
                    show dv smile pioneer with dissolve
                dv "You think she'll slip something in?"
                me "Hard to say."
                dv "And if she will - what will it be?"
                me "Gah, get off me, it's already bad enough as is."
                if dr:
                    show dv laugh pioneer2 with dissolve
                else:
                    show dv laugh pioneer with dissolve
                dv "Would you look at him, what a sissy!"
                "Alisa jokingly saluted to me with a fork and stood up."
                dv "Have a nice whatever-it-will-be, watch your plate."
                hide dv with dissolve
                "Having sowed confusion in my soul, the redhead withdrew."
                me "God damn!"
                "I swore."
                sl "Is something wrong?"
                "Slavya, emerging from the kitchen, put a plate in front of me."
                me "Well, no…"
                "I stared at the plate."
                me "Wow! And why am I so honored?"
                sl "Humanitarian aid to the hungry! But only for the first time!"
                "In the plate, in addition to mashed potatoes and peas, there were as many as three cutlets!"
                show sl happy pioneer with dspr
                sl "And no centipedes, mind you!"
                me "Let's see…"
                "I grumbled, turning the cutlet."
                show sl laugh pioneer with dspr
                sl "You can also look in the peas! And in mashed potatoes - maybe their headquarters are there?"
                "She burst out laughing."
                sl "Eat, I'll clean up in the meantime."
                hide sl with fade
                "And while I was sitting at the table and munching on a very tasty dish, Slavya managed to run somewhere to the door, get a rag and a bucket out of there, after which, without hesitation, she set about collecting plates and cutlets."
                "he squatted down and, having wet a rag, wiped the floor, checking the plates - not one, by the way, cracked or broke."
                "She did this so quickly and with pleasure that I was involuntarily embarrassed:"
                me "I could do it myself…"
                sl "Oh please."
                "Slavya pushed a curl behind her ear from her flushed face and winked at me."
                sl "Don't tell me you want to clean up more than you want to eat?"
                me "And you?"
                sl "And I already ate."
                "At the same time, the girl looked so pleased, as if she didn’t volunteer to clean up, but won no less than a million in the lottery."
                me "Uh.. Thanks."
                sl "Yeah, yeah, keep eating."
                "When she finished cleaning, she smiled at me and went outside."
                "By that time, I had not managed to consume even half of the serving."
                dreamgirl "Yes, this cutie is definitely worth staying close to."
                dreamgirl "At least you won't go hungry!"
                "Agreeing with this thought, I continued munching."
    stop music fadeout 4
    stop ambience fadeout 6
    with fade
    return

label alt_day1_meeting2:
    play sound sfx_open_door_clubs_2
    pause(1)
    scene bg ext_dining_hall_near_sunset
    with dissolve
    play ambience ambience_camp_center_evening fadein 6
    play music music_7dl["what_am_i_doing_here"] fadein 3
    "By the time I stepped out onto the porch of the canteen, evening was already clearly setting in."
    "That evening, summer, warm, which even smells completely different."
    "The sun no longer fries, but still warms, and thus the mood becomes complacent and relaxed."
    "However I still could not understand on what rights I am here."
    "If I'm a guest of honor, then why do I not remember the welcoming procession?"
    "And if I got here by mistake - then where are the screams «get out of here, boy»?"
    "I definitely don't understand anything."
    scene bg ext_dining_hall_away_sunset
    with fade
    "On the right hand, just around the corner of the dining room, several boys of about fourteen were squatting, looking intently at the ground.."
    "One of them swung and with a perfect movement drove something into the ground.."
    th "Knives?"
    "Intrigued, I stopped and looked closely."
    "They instantly reacted:"
    show al dontlike pioneer with moveinbottom
    show dn dontlike pioneer at left
    show tn shy pioneer at right
    with dissolve
    al "Wanted anything?"
    me "Nope, just walking around."
    al "Uh-huh."
    "He nodded briefly to his friend, who immediately hid the knife in his pocket."
    "Straightening up, they looked at me with an extremely patient, expectant look."
    "Seems like they weren't in a hurry."
    "Neither was I."
    show sl normal pioneer at fright
    with fade
    "We would have stood like this for a long time, if not for the extremely timely arrival of Slavya."
    "She looked refreshed - it seems that she had time to wash after cleaning."
    sl "And what are you doing here?"
    dn "We are leaving. And your friend is staying."
    show sl smile pioneer with dspr
    sl "Friend?"
    "I shrugged."
    hide al
    hide tn
    hide dn
    with dissolve
    "Apparently, considering their mission accomplished, the trio of boors retired."
    show sl normal pioneer at center with move
    me "At least you're a lot friendlier to me than these kiddies."
    show sl serious pioneer with dspr
    sl "Yeah, people rarely trust each other. {w}But I also come bearing good news!"
    me "People trust each other more often now?"
    show sl laugh pioneer with dspr
    sl "Nope! {w}But I have a free hour, so I'll be happy to spend it with you."
    show sl shy pioneer with dspr
    sl "Oh, no, I mean, I wanted to say something else!"
    "Embarrassed, she looked even more charming - which only aggravated my distrust of her."
    me "Spend an hour with me… {w}I like the sound of that!"
    show sl smile2 pioneer with dspr
    sl "I can work as a guide if you haven't seen the whole camp yet."
    "I carefully counted all of today's waypoints and shook my head:"
    me "Today I saw the square, the squad leader's house and the sportsground. {w}Well, and your warehouse, of course."
    me "Can I ask you a question? What's your actual job here?"
    sl "No, I'm not officially the castellan, if that's what you mean.."
    sl "But ours got sick, so this week I'm replacing her."
    me "How did you even agree…"
    show sl happy pioneer with dspr
    sl "I volunteered. {w}Anyone else would probably fail anyways."
    sl "So what do you think? Want me to work as your guide?"
    if dr:
        dreamgirl "Better work with your body parts."
        th "Look who suddenly woke up."
        dreamgirl "Alright, alright, I'm sleeping."
    me "If you have nothing better to do… Let's try!"
    show sl smile pioneer with dspr
    sl "Excellent! So, what we have on the agenda: the stage, a infirmary, clubs and a beach."
    me "Beach!"
    show sl sad pioneer with dspr
    sl "Hmm, no, we'll have to cancel the beach for now - junior teams currently have gymnastics there."
    me "They do it in water or something?"
    sl "No, but the PE teacher forbids anyone to be on the pontoons while classes are in progress, so it won't do."
    me "Then our choice consists of 3 options?"
    show sl normal pioneer with dspr
    sl "You can add sports field so that it's an even number. {w}I love even numbers!"
    me "Urgh, why."
    show sl smile pioneer with dspr
    sl "It's just that even numbers are prettier!"
    me "Alright."
    sl "I would advise the sports field, the pioneer must be athletic!"
    me "Or the music club - the pioneer must be musical?"
    "The girl nodded."
    me "Or even the infirmary - the pioneer must be healthy!"
    show sl shy pioneer with dspr
    sl "Teasing me!"
    me "Sorry…"
    sl "It's okay."
    sl "It's just that I actually do some sports too. {w}And I do music, and I also sing!"
    th "If you don't praise yourself…"
    sl "What do you like to do?"
    me "Lying down."
    show sl laugh pioneer with dspr
    sl "Oh, Semen, you're such a kidder!"
    th "I'm not joking."
    sl "So, where are we going?"
    "Laughing, the positive girl asked from all sides."
    while len(list_slavya_7dl) < 2:
        play music music_list["smooth_machine"] fadein 3
        scene bg ext_square_sunset
        with dissolve
        play ambience ambience_camp_center_evening fadein 6
        menu:
            "To the scene" if not 'estrade' in list_slavya_7dl:
                $ renpy.block_rollback()
                $ list_slavya_7dl.append('estrade')
                me "The pioneers are forced to perform there, yes?"
                show sl laugh pioneer with dspr
                sl "Not really forced, no!"
                me "You're going to tell me they volunteer?"
                show sl smile2 pioneer with dspr
                sl "What's wrong?"
                sl "Our people love to perform."
                th "Uh-huh, of course I believe you."
                sl "Well, shall we?"
                "I nodded."
                "We slowly set out somewhere to the north."
                sl "No, of course, not everyone loves the audience, I understand that."
                sl "But we don't force anyone!"
                if loki:
                    "I still remember my first times on stage."
                    "It was very annoying."
                else:
                    "I perfectly remembered how hard it was to force myself to go on stage."
                me "You can't kick someone else out onto the stage otherwise than with a kick."
                show sl normal pioneer with dspr
                sl "No, it's different here."
                scene bg ext_stage_big_sunset_7dl
                with dissolve
                "When we went up to the stage, the sun had already shifted so that because of the rays hitting my eyes, I really could not see the structure itself."
                "The only thing I caught was a kind of canopy over the stage."
                me "Why the canopy?"
                show sl normal pioneer with dspr
                sl "The public opinion is split on this."
                me "Oh really?"
                sl "Yeah! Some believe that this is for performances in case of rain."
                me "But then it would be necessary to take care of the soaked spectators."
                "I pointed out."
                sl "That's true! There's also another theory."
                sl "According to her, the roof is for the sun. {w}So that bright light does not interfere with performers."
                me "Which one of these theories you support?"
                show sl smile pioneer with dspr
                sl "The first one!"
                sl "Under the stage itself there is also a utility room where all sorts of wires, plugs and the like are stored."
                me "And if the roof isn't there it'll be flooded."
                "I thoughtfully continued."
                me "That makes sense!"
                sl "Wanna get on the stage itself?"
                me "Can I?"
                sl "Of course! {w}Unless you're were planning to break something?"
                me "Never even crossed my mind!"
                sl "Let's go then!"
                scene bg ext_stage_big_sunset_7dl:
                    linear 1.0 zoom 1.2
                "We had to go across the perimeter of bench square - I still could hardly see anything in front of me."
                with fade
                "And as it turned out later, I also managed to miss someone on the stage…"
                stop music fadeout 5
                show sl normal pioneer close with dissolve
                sl "Shush."
                "I wanted to ask something, but I found an index finger on my lips."
                sl "Can you hear it?"
                "I listened in."
                play music music_7dl["tellyourworld"] fadein 3
                "And only now I heard a barely noticeable, on the very verge of perception, sound."
                "Or rather, not even a sound, but a whole melody, which someone's fingers confidently brought out."
                me "Wow!"
                "I admired in a whisper."
                me "Who's this mysterious talent?"
                show sl serious pioneer with dspr
                sl "I have several candidates in mind, but you know what?"
                me "What?"
                sl "I don't want to know who it is."
                me "But I do!"
                "I took a step, but Slavya, like an hour ago, again held me by the shoulder."
                sl "Really, you shouldn't."
                me "But why?"
                sl "Because no matter how beautiful the melody is, you should not chat with the musician."
                sl "Because that will end that melody."
                me "And it's a beautiful one."
                show sl smile pioneer with dspr
                sl "Yeah. Very."
                sl "I am always so happy when I hear how someone can convey emotions, joy, happiness with a simple sound of strings! Hope for the future."
                sl "What about you?"
                me "And I... I don't know."
                me "I can't separate this tightly woven tangle of experiences inside myself."
                sl "But you do feel something?"
                me "Most of the time I'm ashamed."
                show sl surprise pioneer with dspr
                sl "Why?"
                me "Eyes sting, like you want to cry. {w}Do men cry?"
                show sl smile2 pioneer with dspr
                "Slavya drew me to her and patted me on the top of my head."
                sl "Yeah, men don't cry."
                sl "And some mysteries…"
                me "Yeah… they just have to stay as they are."
                "And it doesn't matter who is playing there. What matters is how he's playing."
                stop music fadeout 3
                "We stood for another ten minutes, listening, until the unknown guitarist finished, and only then tiptoed away."
                stop music fadeout 6
                pause(1)
            "To infirmary" if (alt_day_binder != 1) and not 'aidstation' in list_slavya_7dl:
                $ renpy.block_rollback()
                $ list_slavya_7dl.append('aidstation')
                me "Although I would prefer the beach."
                show sl smile pioneer with dspr
                sl "I would too, believe me?"
                sl "But if there's nowhere else to go…"
                me "Is that the only way to water?"
                sl "No, there is also a boat station, but swimming is prohibited there."
                me "And the reason?"
                sl "Cold springs are beating down there, it's very easy to get cramps."
                show sl shy pioneer with dspr
                sl "Although I never got one."
                me "Maybe I also won't?"
                show sl smile pioneer with dspr
                sl "No, let's better go where were going."
                me "Ahh… Happiness was so close."
                "A soft giggle answered me."
                scene bg ext_aidpost_sunset_7dl
                with fade
                "On the way, I saw the very same boors who were near the canteen."
                me "Psst, Slavya!"
                "I tried to draw her attention, without drawing children's."
                show sl normal pioneer with dspr
                sl "We're here."
                me "Nah, it's not about that. {w}Who the hell are they?"
                "Of course, it was impolite to poke a finger, but as if I cared about politeness."
                show sl smile pioneer with dspr
                sl "Them?"
                me "Yeah."
                sl "It's not just them, they're guardsmen."
                me "Thanks, I didn't understand a thing."
                show sl smile2 pioneer with dspr
                sl "You already know Ulyana, and so, these are her guardsmen. Best friends and part-time security."
                me "Well, it looks like they suck at their job."
                "I doubted."
                me "Where is their subject of protection?"
                show sl happy pioneer with dspr
                sl "Running around somewhere, probably. {w}Or raiding the canteen - the only thing she ate for supper were your and her's cutlets."
                me "That's what she deserves."
                show sl serious pioneer with dspr
                sl "Hey you can't say that!"
                me "Oh, and planting insects in people's plates is allowed?"
                sl "Still! Don't lower yourself to her level."
                me "If only anyone would lower themselves to mine…"
                hide sl with dissolve
                "I heartily spat and turned away."
                "The guards are the guards. Fuck them."
                with fade
                "Seems like we were noticed."
                "But this time, nobody was going anywhere."
                "And it seemed like it was obvious enough."
                "In any case, after five minutes of negotiations and internal meetings, they left us alone."
                "Better that way."
                me "You know what I suddenly remembered…"
                show sl normal pioneer with dspr
                sl "Yes?"
                me "Our kindest doctor - or a nurse? In general, her manner of conducting examination."
                sl "Do other doctors do anything different?"
                me "She makes you strip! And touches!"
                show sl laugh pioneer with dspr
                sl "Yeah! {w}Other doctors do the exact same."
                me "But it's not like that!"
                sl "Like how?"
                "I got confused and fell silent."
                show sl smile pioneer with dspr
                sl "Alright, alright."
                "Apparently, having giggled enough, the girl decided to take pity on me."
                sl "It's just the way she speaks. And behavior. Pay no attention and she will quickly get off your case."
                me "Oh, and her harassment? That's not worth mentioning?"
                "Slavya serenely shrugged her shoulders."
                sl "Yeah, she did. Go submit a case to court if you want to."
                me "I can't believe you said that."
                show sl happy pioneer with dspr
                sl "I didn't say that. It was her who did."
                play sound sfx_open_door_1
                pause(1)
                "Our fascinating conversation was interrupted by the creak of the door, and a figure in a gown appeared on the porch of the infirmary."
                show sl surprise pioneer with dspr
                "Slavya gasped and instantly fell silent."
                me "What's wrong?"
                sl "You know, we should leave now, yeah?"
                me "What happened to your speech about behaviour and such?"
                sl "Yeah, yeah, let's go already!"
            "What are 'clubs'?" if not 'clubs' in list_slavya_7dl:
                $ renpy.block_rollback()
                $ list_slavya_7dl.append('clubs')
                show sl normal pioneer with dspr
                sl "This is the place where we shooed Ulyana, remember?"
                me "Oh, that's where a beautiful girl was."
                sl "A beautiful one, yeah."
                me "And what did Ulyanka have in her hands?"
                show sl smile pioneer with dspr
                sl "Most likely, some kind of beetle or cricket - Lena is terribly afraid of them."
                me "What, she just scares her friend like that?"
                "My opinion of the carefree child was noticeably shaken."
                me "Knowing Lena…"
                show sl serious pioneer with dspr
                sl "Of course, I try to prevent pranks, but I don't always have time."
                scene bg ext_clubs_sunset_7dl
                show sl normal pioneer
                with dissolve
                sl "Well we're here. {w}How do you like it?"
                "Nothing has changed since my last visit here."
                "So I told my guide."
                show sl smile pioneer with dspr
                sl "Well, will you take me to dinner and movies or not?"
                me "I'm sorry, what?!"
                show sl laugh pioneer with dspr
                sl "I'm saying tonight is practically a date."
                me "Definitely not a date!"
                show sl tender pioneer with dspr
                sl "Are you sorry or are you embarrassed?"
                me "Is that necessary?"
                show sl serious pioneer with dspr
                sl "Of course not. {w}It just seemed funny."
                me "Slavya... Have you had at least one date?"
                show sl shy pioneer with dspr
                sl "That's a se-cret!"
                "We laughed in unison."
                with fade
                me "Actually, what is here?"
                show sl normal pioneer with dspr
                sl "In general, there are many different clubs recorded here, but usually it's just the boys lodging here."
                me "What boys?"
                sl "You'll see tomorrow!"
                sl "I don't want to spoil the surprise."
                me "The boys… Then what was Lena doing there?"
                sl "Who knows. {w}We could go and ask?"
                me "What? No! NO!"
                "As if in response to my words, the girl prepared to turn around and drag me towards Lena - wherever she was."
                show sl smile pioneer with dspr
                sl "Okay, as you wish."
                me "Maybe she had some business there."
                sl "Or she was sent there for some reason.{w} If you're really that curious, you can always ask."
                me "Aren't you interested?"
                sl "Well, not particularly."
                me "You look completely uninterested."
                show sl laugh pioneer with dspr
                sl "Kind of. {w}I have a few topics that are interesting to me to the point of shivering, but I can easily put up with everything else."
                me "Really? {w}And what would these topics be?"
                show sl smile2 pioneer with dspr
                sl "I'm afraid it's not the right time to talk about this topic."
                me "If you say so."
                "The most logical reaction to such a remark would be to pout and turn away."
                "But it seems that this is exactly what Slavya expected from me."
                "So if I would have acted «logically», I would feel dumb."
                with fade
                sl "Had a look around?{w} Let's go back?"
            "Sports grounds?" if not 'sports' in list_slavya_7dl:
                $ renpy.block_rollback()
                $ list_slavya_7dl.append('sports')
                show sl normal pioneer with dspr
                sl "Yes, football, volleyball courts... you've been there, remember?"
                me "I was. {w}But maybe there's anything interesting going on there?"
                sl "I doubt it. {w}Football championship ended last week, and volleyball one will be held on the beach the day after tomorrow."
                me "The beach again."
                sl "Yes, again."
                me "Then, maybe we should go there?"
                show sl serious pioneer with dspr
                sl "I already told you that… {w}I see. You're joking."
                me "How else am I supposed to have fun if I was deprived of a chance to swim in the evening?"
                show sl normal pioneer with dspr
                sl "If you want, I'll ask for tomorrow - we'll go together in the evening?"
                me "What, I'll just be let go?"
                sl "You will."
                "The girl just answered, and I immediately understood that she would be let go."
                me "Don't forget!"
                sl "I never forget anything."
                scene bg ext_playground_sunset_7dl
                with dissolve
                "It took a long time to get to the field - about twenty minutes at an extremely leisurely pace."
                "Why leisurely?"
                "It's just that we constantly strayed into different paths, attempts to cut off and similar topographical pranks."
                if herc:
                    "Slavya gave the impression of a kind girl, but with her own mind."
                    "She rejoiced in this world, and the world rejoiced in return for her."
                    "But I understood too well how easily she would hurt, as soon certain limits were crossed."
                    "Not physically, but…"
                    "It seemed to me that she simply had not yet grown up to the bar, after which all this romantic nonsense begins to matter."
                    "And therefore, any romantic claims of guys can be answered with quite logical bewilderment in her eyes: «why?»."
                    "And how are you supposed to answer that question?"
                    "That's why I did not consider her as a girl, despite neither the gorgeous figure nor the beautiful face."
                    "'The guy', a pleasant conversationalist, just a kind person."
                    "Not a girl."
                    "Nope."
                elif loki:
                    "She tried to stir me up, make me laugh in places, but…"
                    "Yes, in any, even the most wonderful story, there is that «but», which holds everything together."
                    "And in our case, I acted as that conjunction."
                    "I did not believe Slavyana for a second, not one iota, not one gram."
                    "Too casually she inspired and motivated."
                    "This means she lives it as she breathes - naturally, without thinking about anything."
                    "Especially about consequences."
                    "Therefore, I ruthlessly uprooted and trampled the sprout of interest awakening somewhere in my chest."
                    "For this interest was like those very motivations - artificially caused, using several well-established techniques like shooting eyes."
                    "It only took me once to understand how dangerous an interest of this kind can be."
                    th "So this time - you missed. {w}Your charms are just laughter for me."
                    th "The distance suits me perfectly."
                else:
                    "Slavyana reminded me of my mother."
                    "The person who dragged his family all his life."
                    "In everyday life, she was simple, a frivolous and excellent joker."
                    "But as for everything else… The need taught, the need forced."
                    "The saddest thing is probably that this same «everything else» happened frustratingly often."
                    "Much more often than the evenings when we made tea together in the kitchen and played palindromes."
                    "I had to sigh, collect papers with textbooks and retire to my room, and in the morning listen to the schedule of important things for the whole day."
                    "Even with shopping trips and homework time."
                    "An easy man, from whom circumstances formed a man of power."
                    "That's why I set apart my mom in slippers and a plush apron (very soft!) and mom-tyrant."
                    "I specifically missed the plush mom."
                    "And exactly that plush I just saw in Slavya."
                    th "Better not fall in love."
                    dreamgirl "You think you'll manage?"
                    th "Oh, I have vast experience with that."
                "Slavya felt a look in her back and turned around."
                show sl normal pioneer with dspr
                sl "Did something happen? {w}Your stare tensed up."
                th "You're paying attention even to that."
                me "Yeah, I think while we were walking, everything ended."
                show sl smile pioneer with dspr
                sl "Not really. {w}Look."
                "I followed the light wave of her hand - in the tennis box you could see several figures playing something."
                sl "Shall we?"
                hide sl with easeoutright
                "The girl ran forward, and I had to accelerate to keep up."
                "Despite the fact that the territory of the camp turned out to be much smaller than I feared, it would still be extremely annoying to get lost in some nook and cranny.."
                scene
                $ renpy.show("bg ext_tennis_court_7dl", what = Dawn("bg ext_tennis_court_7dl"))
                with dissolve
                sl "Ulyanka is playing football again."
                me "In a tennis court?"
                "I went closer to the net and took a closer look."
                show sl normal pioneer with dspr
                sl "Looks like it. Although that's not exactly football."
                me "That's a square."
                "I agreed."
                "Good old fun for four players."
                "Although, when I got a little older, it was changed to throwing a sock with sand - what was it called there? Nosox?"
                dreamgirl "Sox."
                th "Yeah, right."
                with fade
                "The left side of the court with quadratic markings was occupied by Ulyana and those same three boors from the canteen."
                me "They're here again."
                "I mumbled with displeasure."
                sl "Oh come on. {w}They don't touch you, you don't touch them… Ulyana!"
                show sl normal pioneer at left with move
                show us normal sport at right
                with dissolve
                us "What?"
                sl "Why are you playing with a football ball on the court, you want to break something?"
                show us dontlike sport with dspr
                us "We won't break anything. {w}Second squad already left, so there's not enough people."
                show us laugh2 sport with dspr
                us "Hey, wanna join us?"
                show sl laugh pioneer with dspr
                sl "No thanks, I'm not particularly good at football."
                show us laugh sport with dspr
                us "We all aren't very good, but three by three is already better than two by two."
                us "Newbie?"
                "There was a tightly stretched chain-link between us, so she looked me straight in the eyes without any embarrassment."
                "But on the other hand, it was even funny."
                "She did something nasty, and as a result, she herself was left without dinner."
                "So kindness begets kindness."
                me "Don't really want to. {w}Especially with you."
                show sl serious pioneer with dspr
                sl "Semyon!"
                show us dontlike sport with dspr
                us "What does that mean, huh?"
                me "Don't want to play with you. {w}Let's go, Slavya."
                show us laugh2 sport with dspr
                us "Hey, are you two dating already? Already? {w}A couple?"
                us "Damn you're quick!"
                show sl smile2 pioneer with dspr
                sl "Yeah, let's go."
                "We waved goodbye to the little tease and left."
            "Don't really want to go anywhere":
                $ renpy.block_rollback()
                if len(list_slavya_7dl) == 1:
                    show sl normal pioneer with dspr
                    sl "You sure?"
                    "The girl glanced at the sky - still quite bright."
                    sl "There's still a little time, but if you're in a hurry…"
                    me "I'm in a hurry."
                    show sl smile pioneer with dspr
                    sl "Well, in that case, it's time for me to run. {w}Bye!"
                else:
                    $ lp_sl -= 1
                    show sl sad pioneer with dspr
                    sl "Well, if you don't want to…"
                    sl "Then I leave you here. You will find the way to the squad leader from here, yeah?"
                    me "I will."
                    show sl normal pioneer with dspr
                    sl "See you soon then!"
                $ list_slavya_7dl.append('deny1')
                $ list_slavya_7dl.append('deny2')
                "Slavya waved her hand at me and ran away, leaving me alone."
                hide sl with dissolve
                stop music fadeout 6
                stop ambience fadeout 6
                return
        if len(list_slavya_7dl) <= 1:
            scene bg ext_square_sunset
            show sl normal pioneer
            with dissolve
            sl "Where to now?"
    $ lp_sl += 1
    $ persistent.sprite_time = "night"
    $ night_time()
    scene bg ext_square_night
    show sl normal pioneer
    with dissolve
    "While we were walking, the sky had already completely darkened, and deep shadows lay between the pines."
    sl "Well, looks like that's it."
    "Slavya looked at her watch."
    sl "Today my free time is over, it's time to run on business."
    sl "Will you find your way from here?"
    me "To where?"
    sl "To squad leader's house!"
    me "Ah... yes. I will."
    "Slavya smiled at me again."
    me "Thanks for the walk."
    sl "No, thank you. See you soon!"
    hide sl with easeoutleft
    "She ran away leaving me in the square."
    stop music fadeout 4
    stop ambience fadeout 6
    with fade
    return

label alt_day1_chase:
    scene bg ext_dining_hall_near_sunset with dissolve
    play ambience ambience_camp_center_day fadein 2
    play sound_loop sfx_run_forest fadein 1
    play music music_list["went_fishing_caught_a_girl"] fadein 2
    if (((counter_sl_7dl != 1) and (not dr)) or alt_day1_el_followed):
        "For the umpteenth time in this crazy day I ran through this strange camp."
    th "The little shit jumped out with a lead of ten meters… But that won't save her!"
    "I jumped out on the porch and looked around."
    "On the path to the square, a low shadow flickered and disappeared around the bend."
    "At the same time, bushes crackled in the southeast somewhere towards the direction of the football field."
    menu:
        "Run towards the square!":
            scene bg ext_square_sunset at running
            th "H-ow mu-ch ca-n you r-un!"
            "The legs feed the wolf, but today I run way more than I feed."
            "For the whole day I haven't even drank water, where could the power come from. And then there was this bastard."
            "I haven’t figured out very well what I’ll do with Ulyana when I catch up with her, but I'm sure it will be very slow and painful."
            stop ambience fadeout 1
            scene bg ext_path_sunset at running
            pause(1)
            play ambience ambience_forest_day fadein 1
            play sound sfx_7dl["breath"] fadein 3
            "Having run through the entire camp, I began to realize that somewhere I missed the victim."
            scene bg ext_path_sunset with dissolve
            "I stopped, angrily hitting a tree with my fist, and, bending over, tried to catch my breath."
            if alt_uvao_active:
                call alt_day1_uvao_ch1
                pause(1)
            stop ambience
            stop sound_loop
            return
        "Run towards the football field!":
            scene bg ext_dining_hall_near_sunset at running
            "The fact that I chose the right direction became clear after barely ten seconds."
            "Red «USSR» T-shirt flickered among the greenery as a sore spot."
            "And I increased my pace, ignoring the indignantly aching legs."
            scene bg ext_playground_sunset_7dl at running
            "However, it would not be possible to ignore them for a long time, and I felt that a little longer - and I would start to slow down."
            "Not enough speed, not enough lung power."
            "Unfortunately, the little demon in the scarlet t-shirt didn't seem to get tired and only picked up the pace."
            "By the time I ran out onto the field, she had already passed halfway and was now moving at full speed to the rescue."
            "I looked around in desperation, and my eyes stumbled upon an extremely lucky ball."
            stop ambience fadeout 3
            stop sound_loop
            menu:
                "Kick it":
                    scene bg ext_playground_sunset_7dl with dissolve
                    $ karma -= 10
                    $ alt_day1_us_shotted = True
                    me "Trying to run, are we?"
                    "I literally reveled in gloating."
                    me "Oh no you don't!"
                    "I took a short run, hit hard, sending a round projectile strictly between the shoulder blades of the fugitive."
                    if herc and (counter_sl_7dl != 1):
                        "Straight into the same place I hit her with a pinecone a few hours earlier."
                        th "Seems like my appearance is a wind of changes to her."
                    "My leg ached from such an unrighteous attitude, but I didn’t care about such nonsense."
                    play sound sfx_soccer_ball_kick
                    us "AHHHHH!"
                    "Ulyana was literally blown off her feet and, burying her nose in the grass, was dragged forward a couple of meters.."
                    me "Don't fuck with this pioneer!"
                    "I bowed to the imaginary tribunes and with all possible dignity withdrew."
                "Don't kick it":
                    $ lp_us += 1
                    $ karma += 10
                    "Ulyana vanished from my view."
                    "I continued the pursuit for some time, until my lungs begged for mercy."
    stop music fadeout 2
    stop ambience fadeout 3
    with fade
    return

label alt_day1_headshot:
    scene bg ext_path_sunset with fade
    play music music_list["smooth_machine"] fadein 1
    "Muttering a prayer of departure for an untimely late dinner, I headed wherever my eyes looked."
    $ persistent.sprite_time = "night"
    $ night_time()
    scene bg ext_camp_entrance_night
    with fade2
    "When it was already completely dark, I ran into the familiar gate with a five-pointed star."
    "How strange it is when the driveway near the camp is combined with a bus stop."
    scene bg ext_no_bus_night with dissolve
    play ambience ambience_camp_entrance_night fadein 3
    th "I know from experience that no one will ever stop transport for the sake of camps, which means that either the private sector, or a village, or an enterprise are needed."
    "Gotta think now…"
    "Having plucked a blade of grass, I had a bite of juicy greens and, sitting right here on a concrete curb, began to sum up the day. Resigned to going to bed without dinner."
    th "Not the first time."
    "The driver who drove us here, for all the time of my travels around the camp, never met me on the way."
    "Unfortunate. I had questions for him."
    "This means that he most likely lives somewhere nearby."
    dreamgirl "Or drove off to Wonderland on his bus."
    "Or, if we really go into devilry, it could well be that the bus was completely without a driver."
    "Either way I'm stranded. Gotta survive here."
    "Right. Let's leave everything until tomorrow."
    "I got up and walked towards the gate."
    stop music fadeout 4
    stop ambience fadeout 6
    with fade
    return

label alt_day1_nocatch:
    scene bg ext_path_sunset with fade2
    "The time was already late, and I did not want to do something in the dark at all."
    th "If I didn’t mix up anything, then here you can go to the clubs…"
    th "What if I get lost? That would be an apotheosis of the loser."
    scene bg ext_clubs_sunset_7dl
    with fade
    play ambience ambience_camp_center_evening fadein 2
    "In the dark, especially from the rear - try to recognize the building that you saw once in your life."
    "Fortunately, my intuition did not disappoint and the path led me exactly to the club building."
    if (counter_sl_7dl == 1):
        "I didn't even look there today. Maybe there it will be possible to at least figure out where I landed."
        play sound sfx_knock_door7_polite
        pause(2)
        "I knocked on the door."
        "Zero attention, a pound of contempt."
        play sound sfx_campus_door_rattle fadein 5
        "Pulling on the door, I found a closed lock that had not been noticed until now."
        th "Oh well."
        "I concluded."
        "And, thinking, I decided to take a walk to the gate."
    else:
        "To the same place where I met Lena and Ulyana…{w} with a locust."
        "It was hard to draw conclusions from that, huh…?"
        "Shouldn't have taken food from the hands of a little bastard."
        "Anyways, she either likes me, or not."
        "And either promises biiiiiiiiiig problems."
        "Startled by the pictures that came to mind, I walked towards the gate…"
    stop music fadeout 4
    stop ambience fadeout 6
    with fade
    return

label alt_day1_slavya_saviour:
    play music music_list["sweet_darkness"] fadein 3
    scene bg ext_camp_entrance_night with dissolve
    play ambience ambience_camp_entrance_night fadein 3
    show sl pioneer shade with dissolve
    "Someone was already standing at the gate."
    "I was startled."
    me "Who's there?!"
    th "My nerves are already bad enough. And then there are these… Silhouettes!"
    "I thought about where to get cigarettes."
    "The Chinese brand «Tsyuzye» would also work, I'm not picky."
    "Considering I don't even have mine - they left along with the bus."
    voice "Finally I found you!"
    "A familiar voice."
    voice "I saw you chasing Ulyana."
    show sl smile pioneer with dissolve2
    "The interlocutor went out under the light of a lantern, and I finally saw with whom I had the honor speaking."
    show sl smile2 pioneer with dspr
    "Slavya."
    if alt_day1_us_shotted:
        th "I wonder how much she knows…"
        sl "Didn't catch her?"
        "I stood there for a few moments in silence."
        me "Well… Kind of."
        show sl smile pioneer with dissolve
        sl "That's not surprising. Nobody can. You're not the first one."
        "It's alright, you can run away from a man, but you can't run from his revenge."
    else:
        "I sullenly stared at the asphalt."
        th "Is she also going to mock me now?"
        sl "Didn't catch her?"
        me "No."
        "Surprised by her participation, I melted a little."
        me "Lost her… somewhere."
        show sl smile pioneer with dissolve
        sl "That's not surprising. Nobody can. You're not the first one."
        "It's alright, Earth isn't big…"
    "And then it suddenly dawned on me."
    me "Were you looking for me?"
    sl "Yes."
    me "Why?"
    sl "You must be hungry? Considering you missed supper."
    play sound sfx_stomach_growl
    "I wanted to read her an angry and proud rebuke in the spirit of «don't treat me like a child», however, the dreamy whale song of the stomach said everything that was needed."
    show sl laugh pioneer with dissolve
    "Slavya laughed again."
    sl "Let's go, we'll feed you."
    th "Yeah. It's that simple, let's go and feed."
    "Not that I was strongly opposed, but I didn't believe in charity.."
    me "But what about the schedule and all that? Canteen is closed."
    sl "We'll think of something."
    "The girl laughed."
    me "And what can you think of, I wonder?"
    "I grumbled."
    th "Feeding one hundred thousand suffering people with three loaves, as if you were a torrent tracker?"
    show sl normal pioneer with dissolve
    sl "You grumble like an old fart!"
    "The girl snorted."
    sl "Shall we go?"
    me "Yeah, sure. Thanks."
    "It was a sin to refuse such an offer."
    scene bg ext_square_night with dissolve
    "By the time we got to the square, it was already completely dark."
    "And Slavya, for some reason embarrassed, said:"
    show sl shy pioneer with dissolve
    sl "Look, it looks like the canteen won't do."
    th "Oh, who would've doubted, Ms. Chatterbox."
    sl "I completely forgot - it's a sanitary day there, so, most likely, absolutely everything was thrown away."
    sl "Sorry…"
    me "Uh-huh…"
    hide sl with dissolve
    "I turned around and headed back."
    with fade2
    "But didn't get far."
    sl "Wait!"
    "She ran after me."
    show sl sad pioneer with dspr
    sl "You didn't even finish listening, where you're running like that?"
    me "To sleep."
    "Not that it was so pleasant to sleep on an empty stomach."
    "But there wasn't anything unpleasant either."
    sl "I just wanted to say that I have something left from the last parental day, if you won’t disdain."
    th "Charity it is."
    me "A freebie is a freebie."
    "If they give — take, if they hit — run."
    show sl smile pioneer with dspr
    "Slavya smiled and led me to the houses."
    "Her house, which she shared with some unknown to me Zhenya, was located on the second street, and to get there, one had to go past the canteen."
    stop music fadeout 3
    scene bg ext_dining_hall_away_night
    with dissolve
    play sound sfx_alisa_picklock
    "There was some noise coming from the canteen. Judging by the concentrated panting, someone was trying to get inside."
    scene bg ext_dining_hall_near_night
    with dissolve
    if herc:
        "Habit is second nature."
        "I still did not understand what I was doing, as I opened my mouth and took in more air into my chest."
        "There is one psychological trick that works great with shoplifters, and now I…"
        "But Slavya was faster."
    else:
        "At any other time, I would have passed, trying not to draw too much attention to myself."
        "In the end it's just none of my business."
        "No, I'm serious! If theft thrives in your camp, you should not throw dogs on pioneers who did not want to get involved with a criminal element."
        "Unfortunately, Slavya thought otherwise."
    play music music_list["doomed_to_be_defeated"] fadein 3
    scene bg ext_dining_hall_near_night at zenterleft
    show sl serious pioneer at cleft
    with flash
    sl "Hey!"
    "She yelled."
    sl "What are you doing here?!"
    "The silhouette on the porch shuddered, stirred strangely — and fell apart into two uneven halves."
    show dv angry pioneer2 at cright
    show us fear sport at fright
    with dissolve
    "It was a pair of redheads."
    "Two people I've been warned for about five times today to stay away from."
    "And so, instead of heeding the warning, I…"
    "Ulyana looked a little scared, but Alisa immediately took the bull by the horns:"
    dv "Why are you so noisy, you upstart?"
    if dr and (counter_sl_7dl != 1):
        dv "OH, you also came with your boyfriend!"
        show sl angry pioneer with dspr
        "Slavya frowned, but did not respond to Dvachevskaya's attack."
        dv "Didn't catch a cold, newbie?"
        me "No."
        "I dryly answered."
        show dv grin pioneer2 with dspr
        dv "See, everything's fine, everyone's healthy!"
        show dv angry pioneer2 with dspr
        extend " And now, take him by the hand and get out!"
        sl "Alisa, do you understand that if you do not stop now, I will have to tell the squad leader?"
        show dv rage pioneer2 with dspr
        dv "Damn snitch…"
    else:
        dv "Don't be afraid, your flag won't run away from you, thanks everyone, get out!"
        show sl angry pioneer with dspr
        "Slavya frowned."
        sl "Alisa, do you understand that if you do not stop now, I will have to tell the squad leader?"
        "I was tactfully silent somewhere on the periphery."
        show dv rage pioneer2 with dspr
        dv "Oh so you're also a snitch…"
    "The redhead hissed, clenching her fists."
    dv "This is very good - I've been thinking all day about beating the shit out of someone."
    menu:
        "Dissuade Alisa":
            "The evening was getting too languid, and I found it necessary to break into the conversation."
            me "Maybe you don't know that they kick out of the camp for fighting?"
            show dv angry pioneer2 with dspr
            dv "And you're her cadger, huh?"
            "What a touching attempt to piss me off."
            if herc:
                me "I don't mind fighting. I don't mind leaving here either."
                me "But to throw someone else under the bus - that's childish. Considering that there's actually nothing in the canteen."
            else:
                me "Yes, call it however you want, but if anything, I will be a witness that you started the fight, and Slavya defended herself."
            show dv surprise pioneer2 with dspr
            dv "What's even attracting you so hard to this blonde?"
            if (counter_sl_7dl != 1):
                $ karma += 10
            $ lp_dv += 2
            me "Her name is Slavya."
            show sl surprise pioneer with dspr
            if herc:
                dv "Is there actually nothing there?"
                "Alisa ignored me, turning to Slavya."
                show sl normal pioneer with dspr
                sl "Sanitary day."
            hide dv
            hide us
            with dissolve
            "Dvachevskaya exhaled something through her teeth and, waving to Ulyana, melted into the twilight.."
            $ alt_day1_cofront_sl_dv = 2
            show sl normal pioneer with dspr
            sl "Listen, thanks for sticking around.."
            "I brushed it off."
            "As if I did anything."
        "Cover up Slavya":
            if (counter_sl_7dl == 1):
                $ karma += 10
            show sl surprise pioneer far at fleft with dissolve
            "I pushed Slavya behind my back."
            "Not that some kind of heroism started speaking in me, but there was a good opportunity to pay off all the debts at once."
            "So that I wouldn't be looked at as if I borrowed money later on."
            dv "You wanna go in her stead?"
            "The redhair relaxed."
            me "Why not?"
            me "You don't care about expellment from the camp? Neither do I."
            "I wasn't a masochist, but it is unlikely that she will be able to do major damage to my renewed carcass."
            show dv grin pioneer2 with dspr
            dv "As you say."
            me "And before everything starts, I will say one last thing: there is actually no food in the canteen. Even if you do manage to break in now, you will leave hungry."
            show dv surprise pioneer2 with dspr
            dv "What? Why?"
            sl "Because everything was tossed out, and new shipment is only coming tomorrow. {w}Sanitary day, you know."
            "Alisa considered the correctness of Slavya's words and gritted her teeth."
            "Then she sipped something obscene and, waving her hand to Ulyana, disappeared into the darkness."
            hide dv
            hide us
            with dissolve
            "And Slavya stood in front of me, looking angrily into my eyes."
            show sl angry pioneer at center with dspr
            sl "You shouldn't have!"
            "She told me."
            me "And you shouldn't have let the situation evolve into conflict!"
            "I lashed out in response."
            me "What kind of assistant are you that allows one red-haired hooligan to turn herself around like that?"
            $ lp_sl += 2
            $ karma += 20
            $ alt_day1_cofront_sl_dv = 1
            sl "I would've solved everything myself…"
            "She stubbornly shook her braids."
            me "By fighting?"
            sl "No! I would have…"
            me "You would, you would… {w}Do you really want to quarrel with me because I resolved the situation?"
            show sl shy pioneer with dspr
            sl "Sorry. Looks like I really got a little carried away."
    stop music fadeout 3
    "The girl once again went up to the porch and checked the lock."
    "It was closed: it seems that the bandits managed to achieve little before we scared them off."
    sl "It's all good."
    "She reported."
    sl "Shall we go? There isn't much time left before sleeping."
    "The conflict situation muffled the impulses of the belly a little, but now they have returned in full."
    "I hastily nodded."
    play sound sfx_open_door_clubs_2
    pause(1)
    scene bg int_extra_house_7dl
    with dissolve
    play music music_list["a_promise_from_distant_days"] fadein 5
    stop ambience
    me "So, this is your house?"
    show sl normal pioneer with dspr
    sl "Not really."
    "She looked at me repentantly."
    sl "It's just that Zhenya is in my house, and I don't know how she will look at your late visit."
    "She took out a package from somewhere in the closet, tied with tight twine."
    if dr and (counter_sl_7dl != 1):
        scene cg d1_sl_dinner_pi_7dl with dissolve
    else:
        scene cg d1_sl_dinner with dissolve
    sl "Here, - sausage, smoked meat, a little bit of onions. All that's left."
    me "Delicioooooous!"
    "A palpable, sonorous roulade of the stomach fully confirmed my words."
    sl "I don't have anything to drink though, is that okay? Aside from water, I mean…"
    "Anything would work at this point, so I didn't complain."
    sl "Bon appetit."
    me "Thanks."
    th "They probably trashed the broth too."
    "I thought sadly, diligently distracting myself from the special, {i}inquiring{/i} look the girl gave me."
    th "Sanitary day… Guh."
    sl "What's wrong?"
    if dr and (counter_sl_7dl != 1):
        scene cg d1_sl_dinner_0_pi_7dl with dissolve
    else:
        scene cg d1_sl_dinner_0 with dissolve
    sl "You somehow look sadder."
    me "You know, I thought that I could throw the centipede out of the plate, and then eat it all."
    me "And if you think about it, then the centipede also works as meat!"
    "Slavya laughed."
    sl "Good attitude."
    me "Maybe. I don't really understand what I should do."
    th "But everyone around diligently convinces me that I am in my place, there was no mistake — please enjoy the summer, {i}siiiiir{/i}."
    sl "Then maybe you shouldn't do anything."
    "The girl smiled willingly and often. {w}Though it didn't devalue her smile for some reason."
    "Perhaps because every smile was from the heart, sincere and honest?"
    sl "Your real life will only begin tomorrow, but for now enjoy the calm."
    if dr and (counter_sl_7dl != 1):
        scene cg d1_sl_dinner_pi_7dl with dissolve
    else:
        scene cg d1_sl_dinner with dissolve
    "Slavya leaned her elbows on the window sill and looked thoughtfully out the window, listening to the night reigning behind the glass."
    "And I was ready to swear - she understood her, every sound, every rustle."
    th "Aren't you, dear, the real Mistress of the Copper Mountain?"
    "I studied her profile, not forgetting to work with my jaws."
    th "Dueling was forbidden by the highest edict, but the clanging of swords was heard every night - or something like that."
    "And her Gray Cardinal Majesty turned to me and at one moment destroyed the magic of the moment, puffing out her cheeks and depicting me chewing."
    th "Oh good, another fun lover. Even though she's a bit more mature than others."
    "I don't know why, but it warmed my soul."
    "Not an infallible golden paladin without fear and reproach, not an ideal instrument of order, but a lively, warm girl who simply liked everything to be in order and everything to work."
    if dr and (counter_sl_7dl != 1):
        scene cg d1_sl_dinner_0_pi_7dl with dissolve
    else:
        scene cg d1_sl_dinner_0 with dspr
    me "Was mocking me necessary?"
    "I inquired."
    sl "Of course not."
    sl "You didn't like that? Sorry."
    me "Well, no…"
    sl "Sometimes I feel like I understand people's feelings before they show them.."
    "She shared."
    sl "And today you've been looking at me all day as if you expect some kind of dirty trick from me."
    sl "You can't be like that."
    me "How can I be then?"
    "Doubting, Slavya wound a curl around her finger."
    sl "Somehow… Not like that. {w}I don't know."
    me "Tell me when you figure that out."
    "We were even after the scene at entrance to canteen. Even a little bit more than that."
    "That's why I relaxed a little, even allowed her to delve into my emotions."
    me "Because it's the easiest thing to say «no»."
    sl "I mean, here, in this place, - people are all honest."
    sl "That's why I love this place so much, it's beautiful, calm and you don't have to think about things like trust - as it goes without saying here."
    "It seems that this conversation took me far, far away, not at all where I wanted to go."
    sl "You are worried."
    "That was said with an affirming tone."
    me "What? Why?"
    sl "You're too focused on chewing."
    me "Sorry…"
    sl "Don't mind it."
    if dr and (counter_sl_7dl != 1):
        scene cg d1_sl_dinner_pi_7dl with dissolve
    else:
        scene cg d1_sl_dinner with dissolve
    sl "Sorry, today I had to run so much, I didn’t have time to show you around the camp."
    me "You did send Electronik though. We managed."
    if dr and (counter_sl_7dl != 1):
        scene cg d1_sl_dinner_0_pi_7dl with dissolve
    else:
        scene cg d1_sl_dinner_0  with dspr
    sl "Oh really?"
    "She smiled so brightly that I, embarrassed, hid my eyes."
    me "Who knows? It's my first day here, maybe I've missed something."
    sl "Alright, and what did you see today?"
    me "In order?"
    sl "Yes."
    me "Alright."
    "I scratched the back of my head."
    me "First landmark - Genda, then Lena, after her - canteen, evil Alisa and a football field."
    sl "What about the beach?"
    me "Somehow didn't happen."
    sl "You definitely should go there."
    sl "What kind of summer is this, without swimming even once?"
    sl "Be sure to go. Or if you want, we could go together?"
    me "Together? {w}I'm all for it!"
    "The naturalness and ease of Slavya smoothly burnt out my annual stocks of embarrassment and frankly already frightened me when it suddenly occurred to me what was formed in the process of chewing."
    "Maybe everything is as it should be for them?"
    "Maybe this world is incomprehensible and frightening only for me, but for them it is…{w} home?"
    "Perhaps I was thrown into the past - although I do not remember such a past, and Genda, for that matter.."
    "And one wonders why the hell should they - the same Slavya, for example - be embarrassed by an unfamiliar pioneer, if they are sure that this pioneer also looks at them with the same positivity?"
    me "Can I ask a stupid question?"
    sl "No."
    me "I really need to!"
    sl "Fine. What's your question?"
    me "What year is this?"
    sl "That's really a stupid question. Don't you know that yourself?"
    me "I'd like you to say it… If that's not too hard."
    sl "Easy."
    scene bg int_extra_house_7dl
    show sl smile pioneer
    with dissolve
    "She stood up."
    sl "1989th year from the birth of Christ."
    sl "Was this supposed to be some sort of a check?"
    me "Well no. Just trying to calculate the age of one of my acquaintances."
    sl "Really? And how's that going?"
    me "The way it's going is that he is now crawling in a diaper, slobbering his T-shirt, and everything in his life is wonderful."
    show sl laugh pioneer with dspr
    sl "So it's good when your acquaintances and friends are doing great!"
    me "Mhm."
    th "Especially if it's one {i}very{/i} special acquaintance."
    if herc:
        th "With last name Sychev."
    elif d3:
        th "With last name Abrikosov."
    else:
        th "With last name Persunov."
    sl "Are you done eating?"
    "I showed her the empty bag."
    sl "Then let's go, I still have to close this house."
    stop music fadeout 3
    play sound sfx_open_door_strong
    pause(1)
    scene bg ext_houses_night_7dl at zenterleft
    show sl normal pioneer at cleft
    with dissolve
    play ambience ambience_camp_center_night
    sl "Well, that's it. Will you find the way to Olga Dmitrievna yourself? She will figure out where to lodge you."
    "I nodded, estimating that the squad leader's house should be on a parallel street."
    "But I wasn't in a hurry to meet her yet."
    "It would be nice according to the law of Archimedes after a delicious dinner as part of an evening exercise…"
    "I waved to Slavya, who was looking for something in her pockets, and left."
    "Didn't look like she noticed me leaving."
    stop music fadeout 4
    stop ambience fadeout 6
    scene black with fade
    return

label alt_day1_lena:
    scene bg ext_square_night with dissolve
    play ambience ambience_camp_center_night fadein 6
    play music music_7dl["someone_like_you_guitar"] fadein 3
    if counter_sl_7dl < 2:
        "I sat down on a bench and once again scrolled through my head everything that happened to me today: from the morning awakening to the ambush at the canteen."
    else:
        "I sat down on a bench and once again scrolled through my head everything that happened to me today."
    "And no matter how hard I tried, no matter how I thought about it, I could not find any malicious intent in the actions of those around me."
    if (counter_sl_7dl >= 1):
        "Slavya, of course, could seem somewhat intrusive."
        "But it had more to do with her demeanor."
        "She was just like that. Without any stones in the bosom."
    else:
        "Even the two red-haired bandits acted only for their own amusement and did not pursue any evil goals."
        "Nobody was interested in my death, internal organs or my bank account."
    th "The bus, the camp, the girls…"
    if alt_day_binder != 1:
        if dr and (counter_sl_7dl != 1):
            "After cleaning the silicone ear pads with my shirt, I was just about to introduce the local world to the latest achievements of electronic music, when suddenly my attention was attracted to a quiet rustle from a nearby bench."
        else:
            "After cleaning the silicone ear pads with my T-shirt, I was just about to introduce the local world a little to the latest achievements of electronic music, when suddenly my attention was attracted to a quiet rustle from a nearby bench."
    else:
        "The player was still somewhere else along with my clothes."
        "Eh, there's nothing to do, I'll have to get used to the silence."
        "I relaxed and threw my hands behind my head, but out of the corner of my vision I caught some movement from the other side of the square."
    stop music fadeout 3
    "A girl. {w}Reading a book."
    pause(1)
    scene cg d1_un_book0_7dl with dissolve
    play music music_7dl["take_my_hand"] fadein 4
    th "Lena."
    "She was not so much reading as sitting with her eyes closed and silently saying something."
    "As if she was reciting what she just read."
    "Or daydreaming."
    th "A magical girl in a magical land."
    if (persistent.un_7dl_good_ussr or persistent.un_7dl_good_rf) and dr:
        dreamgirl "Take a closer look. {w}Do you really not recognize her?"
        th "What do you mean? I know her name is Lena…"
        dreamgirl "You moron, she's the splitting image of…"
        th "Yeah?"
        dreamgirl "Mother of your children!"
        th "Damn, fuck off, you filthy monster."
        dreamgirl "Ok, ok. Chill out. Better go and say hello - today you haven’t exchanged even a few words."
    else:
        "Beliving in miracles is a very valuable skill."
        "I don’t know if I could put the book down and daydream about some wonderful adventures and countries."
        "But why wouldn't I ask her about it?"
        "At least about what kind of book impressed her so much."
    "I got up from the bench and froze in thought."
    "On the one hand, I did not want to interfere, but on the other…"
    "At least I should greet her."
    if persistent.un_7dl_good_ussr or persistent.un_7dl_good_rf or persistent.un_7dl_bad:
        menu:
            "Don't come close":
                th "And what will I say to her?"
                if alt_day_binder != 1:
                    "I finally cleaned my earplugs and flavored the warm evening with percussive guitar riffs."
                    "Nice!"
                else:
                    "I don't know either."
                    "Thus - we sit here and keep calm."
                "After sitting for a while, the girl got up and left."
                "Nice going, me!"
                stop music fadeout 4
                pause(3)
                return
            "Come over to her":
                pass
    $ alt_day1_un = 1
    $ lp_un += 1
    "I came closer to her."
    if (alt_day_binder == 1) and not alt_day1_me_d3_chase:
        "Hearing my footsteps, the girl raised her head."
        scene bg ext_square_night at zenterleft
        show un shy pioneer at cleft
        with dissolve
        un "Oh."
        "She smiled shyly."
        un "Y-you scared me."
        "Digging in her pockets, she took out a flat object and handed it to me."
        un "H-here…"
        me "Phone! Where did you get it?"
        un "On the square…"
        un "You might have dropped it."
        "The phone was clean, not scratched, and there were no greasy streaks on the screen."
        "She didn't seem to understand what it is and how to deal with it."
        me "Many thanks."
        "I put the phone in my pocket."
    else:
        "The girl continued to dream, not paying much attention to me."
        me "Ahem."
        "Zero attention, a pound of contempt."
        me "Lena, I think?"
        "Silence."
        th "Wow, she's ignoring me."
        "I noisily cleared my throat."
        me "Hello. What are you reading?"
        scene bg ext_square_night at zenterleft
        show un surprise pioneer at cleft
        with dissolve
        "Overflowing with surprise she somehow jumped up."
        me "Oh… Sorry."
        "I tried to smile reassuringly."
        me "I didn't want to scare you."
        show un shy pioneer with dspr
        un "It's okay…"
        "A blush, instantly covering her cheeks, was noticeable even in the semi-darkness."
    me "What are you reading?"
    "Right. What else do you ask a girl with a book?"
    "She lifted the book from her lap and showed the cover."
    $ alt_day1_un_talk = True
    "On a dark background, it was written in white script: «Gone with the Wind»."
    "I smiled."
    "Rrrromance, what else."
    scene bg ext_square_night
    show un normal pioneer
    with dissolve
    menu:
        "Nice book":
            $ lp_un += 1
            $ karma += 10
            me "You have a very good taste."
            "The Internet generation knows a little bit of everything and knows nothing really."
            "But I can at least give out a couple of quotes."
            me "Scarlett O'Hara. I will think about it tomorrow."
            me "People only care more about those who give them worries."
            un "A person cannot move forward if his soul is corroded by the pain of memories."
            show un shy pioneer with dspr
            "She picked up, and immediately, embarrassed, lowered her eyes."
            me "Wonderful book."
            un "Yes…"
            "She closed the book and set it aside."
            me "Leaving so soon?"
            un "Yes… I'll go to sleep."
            menu:
                "Let her leave":
                    $ karma += 10
                    me "Goodnight."
                    un "Goodnight."
                    hide un with dissolve
                    "She got up from the bench, hesitated for a second, and then walked away."
                "Hold her up":
                    $ alt_day1_un = 2
                    $ lp_un += 1
                    $ karma -= 10
                    me "Wait!"
                    "I was desperately looking for words, realizing that she's going to leave now!"
                    "The girl hesitated uncertainly, but remained in place."
                    me "Besides Mitchell, what else do you like to read?"
                    "Didn't come up with anything smarter, but at least something."
                    un "Well… I read different books."
                    "She was quite for a while."
                    un "What about you?"
                    me "Me?"
                    "Indeed, what about me?"
                    "Tell her that for the last couple of years I have been reading from smart a golden collection of humorous fantasy of zero in three hundred books?"
                    "Or try to remember Bushkov, Golovachev, Bulychev - they seem to have already worked at that time?"
                    "Ah, to hell with it!"
                    me "You know, somehow I can't choose one genre. Adventure, fantasy, other fiction. {w}Can't really give any names."
                    un "Any recommendations?"
                    me "I recommend the Strugatskys. The older I get, the more facets I discover in their work. A definite recommendation."
                    un "Fiction?"
                    "She suddenly got quiet."
                    show un sad pioneer with dspr
                    un "Don't like fiction."
                    me "Not just fiction, but socio-philosophical fiction!"
                    me "Hell, take «Ugly Swans» for example — what's that one about?"
                    me "About some school and indigo children? About superpowers?"
                    me "No, it's about people! How people behave when they find themselves in unusual situations."
                    un "Never heard about that book."
                    me "No way, it was published in the late sixties."
                    show un normal pioneer with dspr
                    "Obviously this was the wrong topic to talk about. {w}Or the wrong person."
                    "So, we need to urgently change the subject before they take me for experiments as an alien from the future!"
                    me "Not the point. They have a lot of interesting stuff there.."
                    un "Alright…"
                    show un serious pioneer with dspr
                    un "I'll leave, okay?"
                    if alt_day_binder != 1:
                        me "Yeah."
                        "Automatically looking at the time on the smart screen, I reacted."
                        me "It's getting late…"
                        "She stared at the phone in my hand, wanted to ask something, but changed her mind."
                    else:
                        "I waved to her."
                        me "Thank you!"
                        show un surprise pioneer with dspr
                        un "…"
                        me "For not refusing to take me to the squad leader today."
                        if alt_day1_chase:
                            me "And for catching the thief."
                        show un shy pioneer with dspr
                        un "…"
                        $ lp_un += 1
                        with fade
                        show un smile pioneer with dspr
                        un "You're welcome."
                    un "Goodnight."
                    me "Sweet dreams."
                    hide un with dissolve
                    "She disappeared into the darkness, and I sat for a long time and looked thoughtfully in the direction in which she had gone."
                    th "It seemed to be nothing special, a typical image of the most ordinary shy pioneer. But…"
                    "But… Lena firmly took her place in the list of trump cards that the camp played against my old life."
                    "How is it in that song... I look at her back - there is nothing in her. There is nothing in her. There is nothing in her."
                    stop music fadeout 4
                    stop ambience fadeout 6
            return
        "Change the topic" if alt_uvao_active and alt_day1_chase_uvao:
            call alt_day1_uvao_ch2
            pause(1)
            return
        "What's the plot?":
            me "Never read it. They say it's ladies' fiction…{w=.7} Even though I don't really understand what that means."
            me "Is it interesting?"
            un "In some places."
            if herc:
                $ karma += 10
                $ lp_un += 1
                me "You're not very talkative. I like it."
                me "Forgive me my impudence, but if I may ask…"
                me "What are your hobbies besides books?"
                show un shy pioneer with dspr
                "Lena got embarrased."
                un "Different… things…"
                "She whispered reluctantly."
                me "Different… Can you do those different things together?"
                un "What?"
                "She raised her eyes with a silent question to me."
                me "Together… Well… {w}Together!"
                me "Do you get it?"
                un "I understand."
                "She whispered."
                th "Here and now, mademoiselle, let me offer you my friendship, a shoulder and my vest."
                th "Agree, mademoiselle. And this uncomfortable universe will have one more happy bright person."
                th "Even a simple «yes» will do. After all, happiness is the same holiness, you are in harmony with the whole world from being happy."
                th "I don't claim to want holiness, I just want you to be my friend. At least for a start."
                th "And then… Who knows."
                show un smile pioneer with dspr
                un "Drawing."
                "She finally broke the silence."
                un "I like drawing. And we can do it together."
                "I'd love to see that. Although…"
            elif loki:
                $ lp_un += 1
                me "I'm not a big fan of reading. I prefer action."
                me "But, if you'll recommend something to me…{w} I'll hear you out."
                th "While you're young, the word «love» still seems holy and unused."
                th "And admitting to a person that you like him can often turn your life around."
                th "First we think about what it might mean."
                th "Then we think why we can like someone."
                th "Although this is the simplest thing - they just do. No reason."
                th "And then the irreparable happens, and the person takes a place in our thoughts."
                th "So you can call me a bastard, but I like you. And I don't know what to do about it."
                th "Therefore, I cast a glance at the sky and, amiably squinting at the gentle stars, I say:"
                me "You know… I like you…"
                me "It's my first time… {w=.3}sorry for being rude."
                show un shy pioneer with dspr
                un "…"
                th "I just confess to you, and now this is our common problem."
                me "I'm not rushing you to conclusions. Just… If once you feel lonely…"
                th "Well done. Invited the girl to sit next to you in the canteen."
                th "What's next? Offer her to drink tap water and ride the subway?"
                un "It's so…"
                me "I understand."
                "Her words, opinion suddenly became inexplicably important and weighty. I wanted to hear what she would say in response…"
                "It doesn't matter if it's positive or negative. What matters is that communication continues."
                if (alt_day_binder != 1):
                    "From the moment we met at the gate until now."
                    "And that tomorrow, the day after tomorrow and - for however long we will stay here?"
                else:
                    "Although, of course, we met so stupidly - there, at Slavya's house."
                "I don't want communication to end."
                un "I must… I need to think."
                me "But not too long. Will the night be enough?"
                "She fell silent again, but after a while she turned in my direction."
                un "I think that'll be enough."
            else:
                $ lp_un += 1
                me "Mitchell. Hm… About…"
                "I cleared my throat. For some reason, the simplest words were very difficult to pronounce. I, an inveterate cynic, did not have control over the tongue to ask if the book was about love."
                me "It's… um… about war, yes?"
                un "About people."
                "And about how some don't know what they want."
                "Well, at least that's an honest enough answer."
                "And yet, what can you talk about with a girl whom you see for the second time in your life, and for the first time you saw a few hours before?"
                "I know more than two thousand stupid jokes, anecdotes and routine phrases. I can mock a person for hours and never repeat myself."
                "But one has only to start talking about something that concerns me personally, some kind of relationship - and I hide in my shell, where a bottle of vodka and a gun are already waiting for their turn.."
                "And I don't blame you for anything, and I won't blame you if you refuse. I imagined myself in your place: someone unfamiliar broke into the house and claims my favor and attention."
    with fade2
    "She was getting ready to leave when I stopped her with a question."
    me "Lena, can I please ask you about something?"
    show un normal pioneer with dspr
    un "About what?"
    menu:
        "Could you tell me a little about the camp?" if (counter_sl_7dl == 2):
            $ alt_day1_un = 3
            me "I've been running all day today, I didn't really see anything."
            me "Maybe you could suggest some places for me… Where I could… Well…"
            th "The hell is wrong with me?!"
            me "What would you suggest?"
            show un shy pioneer with dspr
            un "I enjoy reading. {w}L-library is my favorite place."
            me "Hm… Slavya didn't show me the library."
            "Lena shuddered, but immediately pretended that nothing had happened."
            un "That's n-nothing, you'll have to go across the entire camp tomorrow."
            me "Why?"
            show un normal pioneer with dspr
            un "Checklist."
            show un smile pioneer with dspr
            "A meteor with infinitely long tails swept past, muttering a song from Winnie the Pooh under their breath, and Lena involuntarily smiled."
            me "Oh, who's that?"
            un "M-my neighbour."
            "With tenderness that surprised me, the girl answered."
            un "She is the m-most unusual p-person. {w}Tomorrow you'll definitely m-meet."
            me "Why not now?"
            show un serious pioneer with dspr
            un "B-because she ran off already."
            me "True."
            un "I'll go, o-okay?"
            "She still stuttered a little and, judging by her appearance, could hardly sit still."
            "I had to let her go."
            show un smile pioneer with dspr
            un "T-thanks."
            me "We'll chat again tomorrow?"
            hide un with easeoutbottom
            "Lena shuddered and vanished as if she had never existed."
        "Will you keep me company?" if (counter_sl_7dl != 2):
            $ alt_day1_un = 4
            $ lp_un += 1
            me "I'm new here. Don't know anything."
            un "…"
            "The only thing remaining was to add «Yeeeaah» — and you can alcoholize a freak in the same cabinet of curiosities with other freaks."
            me "I would like to explore the camp better. {w}Figure out where to go. What to do."
            un "…"
            me "If it's not hard for you… Could you…"
            "I take a deep breath like before diving into deep cold water."
            me "Could you keep me company."
            show un shocked pioneer with dspr
            un "I… But…"
            "She ran out of air, and I carefully waited for her to take a breath."
            un "You… you want me to show you… around?"
            show un shy pioneer with dspr
            me "That's exactly what I'm asking for."
            "I can't tell her that I just want her to keep me company."
            un "W-well… I don't know…"
            me "Please, if it's not too hard for you?"
            "The brakes loosened momentarily from the drunken night air, and I hurried to put the first nail in the coffin."
            me "I just want to spend some time with you. Just chat, understand?"
            show un smile pioneer with dspr
            "She blushed again, but this time she looks somehow… Different?"
            th "According to body language, she doesn't mind my company at all."
            me "So, what will you say?"
            un "I don't…"
            me "Wait! Do not rush to refuse! I beg you."
            me "Think at least until tomorrow, and tell me your answer. Okay?"
            "Still hiding her eyes, the girl closed the book."
            un "Okay."
            hide un with dissolve
            "She rustled colorlessly and melted into the twilight."
        "Please don't be angry at me":
            me "It's my first time here."
            show un sorrow pioneer with dspr
            un "First time?"
            "Lena measured me with a transparent look."
            un "O-okay."
            "The girl got up, looked into my eyes, apparently about to say something."
            "But got flustered, looking away."
            hide un with dissolve
            "She exhaled convulsively and melted into the night."
            th "What's with her?"
            if dr:
                dreamgirl "How should I know?"
                dreamgirl "You look like you have a score together."
                th "What score?"
                dreamgirl "Keep close to her, and maybe you'll know."
    stop music fadeout 4
    stop ambience fadeout 6
    with fade
    return

label alt_day1_sleep:
    scene bg ext_square_night with dissolve
    play music music_7dl["melancholy_sun"] fadein 3
    "Evening. Warm, kind, mine."
    "Perhaps today everything happened not as I planned, not as I wanted."
    "But that doesn't matter!"
    "It just means I'll have something to do tomorrow."
    if alt_day_binder != 1:
        "I didn’t get to know everyone by far - take, for example, that Japanese girl."
        if counter_sl_7dl != 2:
            "Or the mysterious Zhenya."
    else:
        "I didn’t meet so many people, I didn’t even get to know everyone in my squad."
        "I'm sure there's still a whole bunch of interesting personalities here."
        "But all of that is going to be tomorrow. Now I need to work on a lodging for the night.."
    if alt_day_binder != 1:
        if (counter_sl_7dl == 2):
            "Slavya clearly described everything to me - where to go, whom to ask and who, in special cases, to beat on the neck."
            "Fortunately, this time the future victim was clear - our kindest squad leader Olga Dmitrievna."
            me "Slavya…"
            "I looked to the sky and smiled at the sound of the name."
            me "Sla-vya. Slav-nya…"
            th "Gotta stay close to her."
            "There are people-suns who simply do not know how not to shine, and a swarm of fans always winds around them."
            "And here I seem to be lucky to find a nugget that has not yet understood its stunning appeal."
            th "I'll warm my frozen fingers and soul a little - and to hell with it."
            "The decision has created itself."
            th "Falling in love with her is not only fraught, but also illegal."
            dreamgirl "Why?"
            th "She's a pioneer."
            dreamgirl "Dumbass. {w}What would you know…"
            if alt_day1_un == 3:
                "From a distance again came the song of Winnie the Pooh."
                th "Lena's roommate seems to be pretty interesting."
                dreamgirl "Like everyone else in this camp."
                "I consequentially remembered everyone I happened to meet today, and nodded in agreement."
        else:
            $ alt_day1_sl_keys_took = 1
            "I had already rounded the monument to the bronze dunce with an incomprehensible name or surname, when suddenly my attention was attracted by a metallic sheen."
            th "What's this…"
            "I came closer and picked it…"
            th "Ownerless keys?"
            th "Our activist must have dropped them."
            "We were just standing right here when Slavya called out to the thieves at the canteen."
            th "Or not?"
            "I thought about how she opened the door of the house where they fed the hungry Semyon, and decided that it looked like it was simply open…"
            me "How she managed to lose them - they're just that important."
            "I picked up the artifact and put it in my pocket."
            "I'll have to find Slavya and give them back."
            "Or not?"
            "She fed me in a different house, so I can only guess approximately where she lives."
            "Deciding that knocking on all the houses in a row is not a reasonable idea, I went on about my business."
            show mi pioneer shade far with easeinleft
            "And I didn’t even pay attention to someone’s silhouette with long tails to the ground, skipping past me somewhere towards the dining room, singing some song in the voice of Winnie the Pooh, I didn’t even pay attention anymore - I was tired."
            hide mi with easeoutright
            "And only the wind brought «pum-purum-pum-pum», and then everything went silent."
    scene bg ext_houses_night_7dl with fade
    "The night was quiet, the pioneers seemed to have dispersed, and in the darkness only the bright squares of the windows of their houses were visible.."
    "And from above all this - warm stars smiled."
    scene bg ext_house_of_mt_night
    with dissolve
    "I made my way to a familiar house and knocked on the door."
    play sound sfx_knock_door2
    pause(2)
    mt "Open!"
    play sound sfx_open_dooor_campus_1
    scene bg int_house_of_mt_noitem_night
    show mt smile pioneer far
    with fade
    pause(1)
    play ambience ambience_int_cabin_night fadein 1
    "And so I entered."
    "Olga Dmitrievna smiled affably at me."
    if alt_day_binder != 1:
        "She was sitting on the right side's bed, writing down some thoughts in a solid-looking leather-bound notebook."
    else:
        "As in our first meeting, Olga wrote something in her diary."
    "Definitely about a newcomer who walks until late and makes the best pioneer of the squad babysit him!"
    "I was about to say something, but she cut me off with a gesture and pointed to the next bed, where there was a rolled mattress and bed linen."
    show mt normal pioneer with dissolve
    mt "Sit."
    "She kept writing."
    mt "Of course, you have a whole bunch of questions. But let's leave the exciting quizzes for tomorrow."
    me "But what about…"
    mt "Calm down."
    "She interrupted me."
    mt "That doesn't matter right now."
    "She thoughtfully looked at me."
    if (alt_day_binder == 1) or (dr and (counter_sl_7dl == 0)):
        mt "Slavya dressed you, it's good, so you won't go naked."
        mt "We'll get you everything else, don't worry."
    else:
        mt "I see you haven't brought anything."
        mt "Don't worry, we'll get you something. We have everything you need here."
        if herc or loki or (dr and (counter_sl_7dl >= 1)):
            mt "Slavya will provide you with uniform tomorrow."
    me "But I'm not…"
    "My timid protests forced her to put down her pen and look sternly into my eyes."
    mt "We all here are «not»."
    mt "You will sleep where you sit, you can start making your bed."
    me "What?!"
    "I got flustered."
    if alt_day_binder == 1:
        th "Yes, I remember, Slavya said something like that, but I did not pay attention."
        th "Because well, a squad leader can't really live with a pioneer!"
    mt "You're a big boy, no point in being conscious of me."
    "Her eyes were green, devilish, and some kind of spring compressed in the back of my head was gradually unraveling, no longer being afraid of splattering those around me with the contents of my skull."
    "Oh well, had to make the bed."
    show mt smile pioneer with dspr
    "And when I was done, she smiled knowingly."
    mt "Goodnight."
    play sound sfx_click_2
    scene bg int_house_of_mt_night2 with dissolve
    "She flipped the light switch."
    if alt_day1_sl_keys_took == 1:
        "And I started to take off my pants, when suddenly something rang in my pocket."
        th "Right, the keys of our handywoman."
        "I thought about it."
        menu:
            "I'll return them to Slavya personally!":
                $ lp_sl += 1
                "It's not that I want to please her somehow."
                "But it would be interesting to do a good deed."
                "The squad leader will definitely scold her."
                "For no good reason — we all make mistakes."
                "Having made a tacit agreement with myself, I put the keys in the nightstand, undressed and dived under the covers."
            "Hand over the keys to the squad leader":
                me "Olga Dmitrievna."
                $ alt_day1_sl_keys_took = 2
                mt "Yeah, what?"
                me "I found keys on the square."
                me "I think Slavya dropped them."
                mt "Really? Put them on the table, I'll return them tomorrow."
                th "And ream her ass, so she stops scattering the keys everywhere!"
                "I heard almost distinctly."
                "I hummed in agreement, left the keys on the table, folded my clothes and ducked under the covers."
    "I was terribly worried today for the day."
    "In fact, so much so that I expected insomnia."
    scene cg d1_end_of_day_7dl with fade
    "But the moment I finished the logical chain and closed my eyelids - I fell asleep."
    stop music fadeout 4
    stop ambience fadeout 6
    scene black
    with fade
    return
