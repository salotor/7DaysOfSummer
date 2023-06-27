label alt_day4_dv_dj_morning:
    scene scenery with dissolve
    play music music_7dl["what_am_i_doing_here"] fadein 3
    "I dreamed of something..."
    "I clutched at fuzzy images, trying to grab at least a grain of that wonderful dream - so pleasant and amazing that I wanted to stay there to live - but it kept slipping away, treacherously dissolving with every second."
    "I definitely dreamed something, didn't I?"
    scene black with fade3
    play ambience ambience_int_cabin_evening fadein 2
    mt "…parents, so don't wander around during quiet hour!"
    me "Ah?"
    "I must admit, I missed all of the squad leader's instructions, hunting for the remnants of my interesting dream."
    scene bg int_house_of_mt_day
    show unblink
    with dissolve
    $ alt_pause(0.5)
    show mt smile pioneer with dissolve
    mt "Beh."
    show mt grin pioneer with dspr
    mt "Go wash up already, sleepyhead!"
    "Grabbing my bag of washing supplies, I hurried out the door."
    play sound sfx_open_door_clubs
    scene bg ext_house_of_mt_sunset with dissolve
    $ alt_pause (0.5)
    scene bg ext_houses_sunset with dissolve
    $ alt_pause(1)
    play ambience ambience_camp_center_day fadein 2
    th "What a good morning! But something's missing..."
    th "Where's the much-vaunted radio that I needed to crawl on the roof yesterday, risking breaking my neck?"
    "A man of a very respectable age was walking towards me, and two little girls were hanging on his arms, like monkeys."
    "They vied with each other trying to tell something, furiously shouting over each other."
    th "They're kind of the same. Twins?"
    dreamgirl "Oh please - just namesakes!"
    "Trying to make sense of the response of my schizophrenia, I continued on my way towards the washstands."
    th "Anyway, who is this guy? And these…"
    "I just noticed in the distance two women leaving the cabin closest to the square."
    th "…what are they doing here?"
    dreamgirl "Parent's day, dumbass! Were you even listening?"
    "That really explained a lot."
    "Well, who could deal with urgent matters when a much more attractive prospect loomed on the horizon - gutting packages of goodies brought by relatives?"
    th "It's understandable: Dvachevskaya doesn't look like a workaholic anyway, and if there's a good reason to sneak away from work..."
    th "But if I don't hear the camp radio station after breakfast, I'll be pissed off!"
    scene bg ext_washstand_day with dissolve
    "A clown fiesta seemed to be happening at the washstands."
    "It seems that in the morning everyone was in a hurry to quickly meet relatives, so hygiene issues were relegated to the background."
    if herc:
        play sound sfx_7dl["punch_stone_to_bushes"]
        "I deftly dodged a pinecone launched by Ulyana - she started a shootout with the boys from the younger squad."
    else:
        play sound sfx_7dl["blanket"]
        "A pinecone flew into my back painfully. I turned around in search of the source of the projectile and found Ulyana with a handful of cones in her soiled palm."
        "With her free hand, the girl shook her fist at the boys from another squad, who were hurrying to take cover behind the washstands."
    show us grin sport with dissolve
    me "Hey kid! Is your aim off?"
    show us laugh sport with dissolve
    us "Beh-beh-beh!"
    hide us with moveoutright
    "Posing out her tongue at me, the girl deftly circled around me, catching up with her opponents."
    "I just shook my head and leaned over the faucet, out of habit cautiously touching the water with my pinky."
    th "And what do I hope for? For a boiler to suddenly materialize in the camp overnight?"
    play sound sfx_open_water_sink
    play sound_loop sfx_water_sink_stream fadein 1
    "So the only thing left to do was to grit your teeth (as far as possible while trying to brush them) and proceed to the daily morning torture."
    $ alt_pause(1.2)
    stop sound_loop fadeout 1
    "When I finished, almost all the pioneers disappeared, including Ulyana and her comrades."
    "I had to hurry so as not to get scolded for being late for exercise."
    scene bg ext_houses_sunset with dissolve
    th "How strange it all is..."
    th "Just a couple of days ago I was grinning skeptically at the whole circus, but today I almost feel like a part of it."
    th "Is it really worth just doing something useful, and I immediately became for these people... one of their own?"
    dreamgirl "Do you remember {i}for whom{/i} did you do this useful thing?"
    th "These are unrelated things!"
    th "I was given a task - I completed it. The redhead had nothing to do with it!"
    dreamgirl "But you thought of her first anyway. Do you know what it's called?"
    th "I wasn't…"
    "I stopped on the path, sadly stating the fact that I have to justify myself to my own schizophrenia, proving to it that I ran around the camp and fixed the radio at all for the redhead."
    th "Okay, for the redhead! But just to see her face when she realizes she's working for the benefit of the entire camp!"
    "Rejoiced at this interesting lead, I hurried forward."
    th "And if she is also trusted to raise the flag on the lineup..."
    th "She'll definitely explode out of anger!"
    stop music fadeout 4
    $ alt_pause(1.5)
    scene bg ext_square_sunset:
        zoom 1.05 xpos 0.5 ypos 0.48
        align (0.5, 0.5)
    with dissolve2
    play music music_list["everyday_theme"] fadein 3
    show sl smile sport far with dissolve
    "Meanwhile, a real mess was going on in the square: parents, along with the pioneers, were preparing to do exercises, and I could only envy their enthusiasm."
    "Olga rushed like a meteor between discordant rows, trying to arrange everyone so that everyone could see Slavya conducting the exercises."
    "I looked in vain for Alisa in the crowd, but either she got lost among the adults, or she preferred to spend the morning in a close family circle, and not in the square."
    th "She's not going to entertain her folks all day, is she?"
    "I had almost no doubt about this: Dvachevskaya did not at all resemble a person who, for happiness, had to walk arm in arm with her mother, gossiping about incredibly exciting camp events."
    sl "Hands on the belt, feet shoulder-width apart!"
    "Ulyana, despite the impressive difference in height, was in the same line with me."
    hide sl with dissolve
    "I pushed away the gaping mustachioed man, getting closer to the small one."
    me "Ulyana!"
    show us dontlike sport at right with dissolve
    us "What do you want?"
    "Reluctantly, the girl was distracted from the exercise."
    "She, unlike the others, did not slack off during the exercises, receiving sincere pleasure from what was happening."
    me "Where's your girlfriend?"
    show us smile sport at right with dspr
    "Ulyana narrowed her eyes cunningly."
    us "What, are you worrying?"
    show us grin sport with dspr
    us "The sun doesn't warm without her, the birds don't chirp so sweetly?"
    "I could hardly resist giving her a flick."
    show us laugh sport with vpunch
    me "I'm not worried!"
    "My flushed cheeks probably told otherwise."
    me "Just wondering how she managed to sabotage the exercise. Maybe that's what I want too!"
    th "Great, just great. First my split personality, now petty…"
    th "Who next will I start proving that I have no interest in Dvachevskaya?"
    th "Electronik? Buzzer?"
    sl "Bend forward! One, two, three, four!"
    hide sl with dissolve
    show us normal sport at right with dissolve
    us "You can't do that."
    "Ulyana exhaled, straightening her back."
    show us upset sport with dspr
    us "She's lying in the infirmary."
    us "Belly."
    hide us with dissolve
    "Glancing at me expressively, the girl again reached out with her fingers to the toes of her sneakers."
    "I chuckled."
    th "C'mon! I forgot that stuff happens."
    th "One point for the fact that this camp is not a figment of my sick imagination, but a very real place."
    dreamgirl "Or your imagination is so sick that you yourself generate a failure even in a fictional fantasy utopia!"
    th "Thank you, one point for my insanity."
    th "Although your mere presence cannot be blocked by any arguments in favor of the reality of what is happening!"
    stop music fadeout 3.5
    scene bg ext_square_sunset:
        zoom 1.05 xpos 0.5 ypos 0.48
        align (0.5, 0.5)
    with fade3
    play music music_list["so_good_to_be_careless"] fadein 3
    "Exercises ended, and the pioneers fled to the houses - to change clothes."
    "I instead went to Olga."
    show mt normal pioneer close with dissolve
    me "Olga Dmitrievna, I wanted to ask you…"
    show mt angry pioneer close with dspr
    mt "Ask after breakfast."
    "She replied with a frown as she looked at the crowd that was gathering towards her."
    th "I can imagine her horror - as if she didn't have enough of her slobs, and they also handed over twice as many new ones!"
    th "And if our own at least could navigate the territory…"
    me "Yes, I was just talking about breakfast and wanted to..."
    show mt normal pioneer close with dspr
    mt "In eight minutes. Or are you so hungry you can't stand it?"
    me "No!" with vpunch
    "The parents closest to us looked at us with interest."
    show mt angry pioneer close with dspr
    "Olga gave me a displeased look, as if I were an extremely inconvenient hindrance."
    me "Can I take breakfast to Alisa?"
    mt "That's not necessary."
    mt "Breakfast will be brought to her by Violetta Cernovna."
    "And, lowering her voice to a whisper, she hissed:"
    show mt grin pioneer close with dspr
    mt "And don't cling so hard to me! It's indecent!"
    show mt smile pioneer close with dspr
    "I obediently recoiled, raising my hands in conciliation."
    hide mt with dissolve
    "The squad leader, as if having forgotten about my existence, was already kindly talking about something with two elderly women."
    th "No, I heard, of course, that women's cycles are synchronized, but to that extent..."
    th "Is the whole camp going to be thrashing around soon?"
    "I cringed, imagining Ulyana tearing off Electronik's head."
    "The sight was creepy."
    sl "Semyon!"
    show sl normal pioneer far with dissolve
    "Slavya, already changed back into the normal clothes, was hurrying to me."
    show sl normal pioneer with dissolve
    "Coming up, we slowly headed towards the dining room."
    me "It's going to be a fun day today."
    "I said, not knowing how to start a conversation with her."
    show sl smile2 pioneer with dspr
    "The girl smiled."
    sl "Yes, I'll be giving the parents a tour around the camp until the dinner."
    show sl happy pioneer with dspr
    sl "Have you been assigned anything yet?"
    sl "After all, you did a great job of helping us all out yesterday by fixing the radio!"
    show sl smile2 pioneer with dspr
    th "Uh-huh."
    th "Does this mean I'm listed in the leader's notebook as a responsible pioneer whose humpback can be ridden for the rest of the shift?"
    "But I didn't say that out loud, of course."
    me "I don't think my job is going to get away from me."
    "I answered evasively."
    play sound sfx_7dl["eat_horn"] fadein 3
    scene bg ext_dining_hall_away_sunset with dissolve
    "Our conversation was interrupted by the sound of the horn."
    scene bg ext_dining_hall_near_sunset with dissolve
    play sound2 sfx_pat_shoulder_hard
    with vpunch
    "I happily jumped onto the porch, but Slavya grabbed my elbow."
    show sl serious pioneer with dissolve
    sl "Semyon, let the kids go ahead!"
    "I looked longingly at my parents, who rushed into the dining room as if the kids were the last thing they were interested in."
    "But there was nothing to do - under the strict supervision of Slavya, I did not dare to move a single step forward."
    th "With friends like that, you don't need enemies..."
    th "You will starve to death!"
    show sl normal pioneer with dspr
    "But the girl either took pity, or decided that the canteen was already overcrowded, and let go of my elbow."
    show sl smile pioneer with dspr
    sl "Alright, let's go already!"
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day4_dv_dj_breakfast:
    stop ambience fadeout 1
    scene bg int_dining_hall_people_sunset_pp_7dl with dissolve
    play ambience ambience_dining_hall_full fadein 1
    "There were never enough empty seats in the dining room, and today there was an acute shortage at all. I was already looking for a place on the windowsill in the corner, where a tray would fit comfortably, when a sleepy pioneer rose from the table closest to me."
    "Without a second's hesitation, I unceremoniously pushed the onlooker aside, plopping down on the vacant chair..."
    un "Ah!"
    play music music_7dl["take_my_hand"] fadein 2
    show un shocked pioneer with dissolve
    "…and only at that moment discovered that the place opposite was occupied by Lena. She was clearly not too happy with my company - the fright on the girl's face bordered on panic."
    th "Maybe I just showed up too abruptly?"
    show un sorrow pioneer with dissolve
    "I consoled myself, stealing a glance at Lena. She was already blushing, hiding her eyes in her plate."
    me "Bon appetit!"
    "I decided to give up on courtesy and not ask if she had any objection to my company. Even if she did, there were no other empty seats in the dining room."
    "Lena muttered something softly in response, stirring her porridge with a spoon. Deciding that this foreplay was over, I started eating."
    un "Good weather today…"
    me "Do you want to ask me out on a date?"
    show un close_eye pioneer with dissolve
    un "I… No!"
    "Lena shuddered and turned away, almost crying."
    un "I mean…"
    th "I'm on a roll today!"
    th "Yet another woman is already reacting abnormally to me. And it hasn't even been an hour since I woke up!"
    me "I'm kidding, Lena. Relax!"
    show un sad pioneer with dissolve
    "But the girl did not think to relax, fidgeting nervously in her chair. It seemed that at any moment she was ready to break loose and run away wherever her eyes looked."
    th "We must urgently save the situation!"
    menu:
        "Ask about Alisa":
            $ alt_day4_dv_dj_un_dv_question = True
            $ lp_dv += 1
            me "Who do you usually hang out with, if it's not a secret?"
            show un surprise pioneer with dissolve
            "Lena looked at me in surprise."
            un "Well… With everyone, kind of."
            show un normal2 pioneer with dissolve
            un "Why do you ask?"
            th "Really, why?"
            me "Getting witness statements. I recruited a camp radio DJ yesterday, you know, and the DJ started his first day of work by taking a break."
            "At least Lena didn't look like she was about to desert the battlefield anymore. Still not looking at me, she shrugged."
            show un sad pioneer with dissolve
            un "If you want to know my opinion about Alisa, then I can hardly help you. I don't know the current Alisa well."
            th "The current one? Has she been patched for FreeBSD?"
            un "But I can say for sure: if she really gets interested in something, she will go in this matter to the bitter end."
            show un shy_smile pioneer with dissolve
            "Lena smiled shyly."
            un "And she seemed to like DJing."
            me "I thought so too."
            "I finished my porridge and began to spread the butter on the bun with the back of a spoon."
            me "So you've known each other for a long time?"
            show un normal2 pioneer with dissolve
            un "Since childhood. We are in the same class."
            th "The answers you give are, of course, extremely exhaustive!"
            "The words from Lena had to be pulled out literally with tongs."
            me "And has she always been like this?"
            show un serious pioneer with dissolve
            un "Like what?"
            "Lena asked in bewilderment."
            th "How to put it mildly..."
            me "Unbearable."
            show un grin pioneer with dissolve
            "The girl giggled softly."
            un "That's that and this is this. But since you've already decided to get involved with her..."
            show un normal pioneer far with dissolve
            "She rose from the table, grabbing her tray."
            un "...then I advise you to be patient."
            "Awkwardly stomping on the spot, Lena nodded her head, as if apologizing."
            un "I'll go. I've got work to do at the newspaper."
            me "Yeah."
            hide un with moveoutright
            stop music fadeout 5
            th "So, I just realized that I didn't understand anything!"
            th "I found out a long time ago that Lena doesn't like me too much, but I know firsthand about Dvachevskaya's bad temper."
            th "Not very informative conversation!"
            dreamgirl "You didn't ask too much."
            "The inner voice pricked me."
            dreamgirl "Did you really expect that in response to such stupid questions, she would give you a full biography of your girlfriend, including the name of the teddy bear she sleeps with?"
            th "I didn't expect anything!"
        "Ask about books":
            $ karma += 10
            if not alt_day1_un_talk:
                me "You like to read, don't you?"
                "I blurted out to fill this awkward moment with something. Lena finally looked up at me."
                show un shy pioneer with dissolve
                un "A bit. How did you..."
                me "I saw you with a book recently, so I thought..."
                th "Great. Now I look not only like a clown, but also like a scary stalker!"
                me "What did you read, by the way?"
                show un normal pioneer with dissolve
                un "Gone with the Wind. I don't know if you've heard of it - it's more for girls."
            else:
                me "By the way, did you finish Gone with the Wind? Did you like it?"
                "I seized on this recollection as well as I could, like a drowning man at a straw."
            show un sad pioneer with dissolve
            un "To be honest, I haven't finished reading it yet. There was no time, you know: either work in a newspaper, or a tournament, or dances…"
            "Lena, who began to speak without a tremble in her voice, again buried herself in her plate."
            show un serious pioneer with dissolve
            un "Sorry for complaining."
            "I waved my hands in panic:"
            me "It's okay!"
            me "Actually, I asked you myself, remember?"
            show un close_eye pioneer with dissolve
            $ alt_pause (0.5)
            show un serious pioneer with dissolve
            "The girl nodded briefly without raising her head."
            me "So, a newspaper, you say? What are you doing now?"
            th "I hope she didn't find my tone too accusatory?"
            un "We are making a big wall newspaper for Parents' Day. More precisely, we are finishing it."
            "Lena sighed."
            show un normal pioneer with dissolve
            un "We were told on the last day that we needed to add some material, so I'll do that now."
            "There was no enthusiasm in her voice."
            th "Doesn't she like it? Then why did she sign up?"
            "However, the time spent here was enough to understand: the party assignments in this camp were not subject to discussion by ordinary pioneers. The party said - it is necessary, the pioneer answered - yes!"
            th "They put the girl in the hands of the bypass on the very first day and said: 'you won’t sign up at least somewhere - line up against the wall, firing squad will deal with you!' And she, completely desperate, chose the one closest to her in spirit from the offer."
            th "After all, you can hide from everyone in the library, reading in its most secluded corners. Silence, dust and pleasant company of the Beetle - a paradise for an introvert."
            "Lena put all her dishes on a tray."
            show un normal pioneer far with dissolve
            un "I'll go. There's not much time left before dinner."
            me "Good luck!"
            hide un with moveoutright
            stop music fadeout 5
            "The girl left, leaving me to finish the meal alone."
            th "How do you even talk to her? She's so withdrawn, it's like..."
            dreamgirl "It's like you're dealing with yourself? I know it's hard for you!"
            "I ignored the venom in my inner interlocutor's tone."
            th "Oh well! After all, I have other things to worry about besides being a reclusive girl."
        "Ask about Lena":
            $ karma -= 10
            $ lp_dv -= 1
            $ alt_day4_dv_dj_un_quarrel = True
            me "You know, I'm already starting to get used to the current life. {w=1}It's like I didn't come three days ago, but spent the whole shift with you."
            stop music fadeout 3
            play music music_7dl["are_you_there"] fadein 2
            me "You're in this camp for the first time, right?"
            show un surprise pioneer with dissolve
            "Lena froze, slowly raising her eyes to me."
            un "N…no."
            "She squeezed out, as if trying to suppress a stutter."
            show un close_eye pioneer with dissolve
            un "Why… why do you ask?"
            "I shrugged."
            me "Just to keep up the conversation. Besides..."
            "I did not have time to finish. Lena jumped up from her chair, as if stung."
            show un angry pioneer far with dissolve
            un "And I don't want to talk to you!"
            hide un with moveoutleft
            "She rushed to the exit of the dining room, leaving her tray with a practically untouched breakfast on me. I watched her dumbfounded."
            th "And what did I do wrong again?"
            stop music fadeout 5
            dreamgirl "Are you sure it's you?"
            "I was no longer sure of anything."
            th "No, I suspected that Lena had some kind of cockroaches in her brain, but for it to be this bad…"
            th "Maybe I stink? Can't be it, I just showered yesterday."
            "Sniffing my uniform furtively, I found no reason to run away from me."
            th "Well, okay, she can be angry all she wants! I guess I thought up all sorts of things…"
            th "I have things to do."
    "I finished my cocoa in one gulp and moved to the exit from the canteen. A grandiose plan was born in my head…"
    stop ambience fadeout 3
    return

label alt_day4_dv_dj_alise_free:
    play music music_7dl["sneakupon"] fadein 2
    scene bg ext_aidpost_day with dissolve
    "I made my way to the infirmary in a roundabout way, trying not to attract the attention of either the pioneers, or their parents, and even more so the squad leaders."
    th "Even if the redhead can't do anything right now, someone has to entertain her!"
    th "Viola probably won't let me in, but I don't remember needing to ask for her permission?"
    play sound sfx_tree_branches
    "I emerged from behind the bushes, examining the situation near the infirmary."
    "Relative to everything I've seen before, this place could be called the quietest in the entire camp."
    th "Yeah, the candy-eating kids will be pulling up here around lunchtime. So get going!"
    th "Now or never!"
    scene bg ext_aidpost_day:
        xcenter 0.8
        ycenter 0.3
        zoom 1.9
    with dissolve
    "In a half-bent state, I ran to the wall of the infirmary. I pressed my back against it tightly and began to slowly move towards the window."
    play sound sfx_punch_medium
    "A branch crunched under my foot, and a cold sweat ran down my back." with Shake((0, 0, 0, 0), 0.3, dist=50)
    if herc:
        th "Private Pile! stop panicking!"
    else:
        th "Don't panic!"
    "I carefully looked into the nearest window and immediately recoiled: Viola was sitting at the table and making notes in some kind of weighty-looking journal."
    "Gathering my courage, I approached the glass again, peering deep into the doctor's office. The couch was expectedly empty."
    th "That makes sense: there must be an isolated room here, right?"
    "Bending down again, I ran around the perimeter of the building and peered through the window from the other side."
    "More precisely, I tried to look: by all the rules of decency, it was hung with a thick white curtain."
    th "Well, nothing, and not such obstacles were taken by storm!"
    "I caught myself on the window sill and began to crawl along the glass, trying to find an angle from which the inside of the isolator could be seen."
    "Having peeled off almost all the paint from the window frame with my palms, I nevertheless found a thin gap between the curtain and the wall."
    th "Yeah! I see something red..."
    "If my eyesight did not fail me, then Alisa was lying on the bed farthest from the window, her face turned to the wall."
    $ volume(0.2, "sound")
    play sound sfx_knock_glass
    extend " I gently tapped on the glass."
    "No reaction."
    $ volume(1.0, "sound")
    play sound sfx_knock_glass
    "The second time I knocked more insistently. Nothing new - the same lack of at least any action on the other side of the glass."
    me "Is she sleeping there, or what?"
    stop music fadeout 4
    cs "Pioneer!"
    "I froze in the same stupid position in which I stood before: with my feet on the ledge of the foundation, doubled up almost in half and squeezing the shabby window sill with my fingers."
    play music music_list["eternal_longing"] fadein 5
    th "Looks like I've been spotted…"
    dreamgirl "No shit?"
    show cs doubt glasses with dissolve
    "Viola, who was standing at the corner, looked at me with interest, twisting the bow of her glasses in her hands."
    th "That's it, I've got it: now they'll write me down as perverts, they'll take away my already undeserved tie, and at the same time they'll prescribe bromine intramuscularly three times a day!"
    "But the doctor suddenly raised her head and beckoned me with her hand."
    show cs normal glasses with dissolve
    cs "Follow me."
    "It was simply impossible not to obey the demand expressed in such a tone. I shamefully left my post at the window and trudged after Viola."
    me "Sorry, I didn't mean..."
    dreamgirl "Are you going to make excuses like a naughty boy?"
    th "I am a naughty boy to her!"
    show cs shy glasses with dissolve
    cs "Oh, I see. You might not mean it, but your hormones…"
    "She closed her eyes and shook her head."
    cs "Trust me, pioneer: sometimes they do such tricks that you get tired of blushing. I don't know - I don't work the first shift here, I've seen everything."
    scene bg int_aidpost_day with dissolve
    play sound sfx_medpunkt_door_open
    play ambience ambience_medstation_inside_day fadein 2
    "We entered the infirmary and I closed the door behind me, not too tightly, in the vain hope of escaping."
    me "But it's not what you think!"
    "I started blushing without any tricks."
    me "They just told me that Alisa was sick, so I..."
    show cs laugh with dissolve
    "Viola raised an eyebrow, expressing extreme interest with all her appearance."
    cs "…came to save her from the clutches of the evil doctor? Rescue her from the infirmary and run into the woods?"
    "She chuckled softly."
    show cs smile with dspr
    cs "And I already thought that there was no place left in our mortal world for real feelings!"
    th "Actually, that was my backup plan!"
    me "Please stop making fun of me."
    "I grumbled."
    "Having realized that Viola was not too strict, I stopped being afraid."
    me "How is she?"
    stop music fadeout 1
    play music music_7dl["dead_silence"] fadein 3
    show anim_grain
    with touch
    show cs normal close with hpunch
    "The nurse, who had already sat down at her desk, suddenly stood up, taking a few steps closer to me."
    "I shamefully backed away to the door, retreating from her serious gaze."
    $ renpy.show("bg int_aidpost_day", at_list = [sdl_transform7], what = SS_com("bg int_aidpost_day"))
    show cs serious close
    show anim_grain
    with dissolve
    cs "There are things, pioneer, that it's better not to know about. You're better off yourself, trust me!"
    cs "There are mysteries that no one will ever know the answers to, and we can only wander in ignorance like blind kittens."
    "Her demonic multicolored eyes almost devoured my flesh."
    cs "One thing is for sure: it's better not to get involved in it. While it may look harmless, it's actually an unpredictable and extremely hungry dragon."
    cs "And many daredevils who defied the inevitable fell into the jaws of that terrible dragon. They were eaten alive by their own stupidity."
    show cs serious with dissolve
    "I retreated further and further in tiny steps."
    th "What is she even saying?!"
    stop music fadeout 3.7
    cs "So if you think you can handle it…"
    scene bg int_aidpost_day
    show cs normal at cleft
    with flash
    "Viola stepped aside and waved her hand towards the isolator's door."
    play music music_7dl["carefree"] fadein 5
    cs "Go ahead, wake up your pioneer."
    cs "The painkillers should be working by now, so get out of here."
    show cs grin with dissolve
    $ alt_pause(0.1)
    show cs normal with dissolve
    cs "Fresh air and moderate physical activity would be pretty good for her right now."
    show cs doubt glasses far at cright with dissolve
    $ alt_pause(0.2)
    show cs doubt glasses_through far with dissolve
    "Leaving me even more perplexed than before, the doctor sat down again at the table and pulled the magazine toward her."
    th "Screw her!"
    th "I'm not stepping back into this infirmary ever again!"
    "Not wanting to stay in the same room with the crazy Viola anymore, I hurriedly slipped into the room."
    play sound sfx_medpunkt_door_open
    scene bg int_refinery_day_7dl with dissolve
    "Alisa still sniffed peacefully on the unmade bed right in her uniform, curled up."
    "And I would even be touched by her serene face and childishly parted mouth, if not for..."
    th "Fixing that damn radio last night, which she should be working on now instead of taking a nap!"
    me "Redhead!"
    "I shook her lightly on the shoulder."
    "Alisa muttered something displeased, burying her face in the pillow."
    me "Redhead! Get up!"
    dv "Get off!"
    "She grumbled, rummaging around the bed for a blanket."
    if herc:
        stop music fadeout 3
    "That was starting to piss me off."
    if herc:
        play music music_list["revenga"] fadein 3
        th "Hold on, I'll wake you up alright!"
        "Having grasped the two ends of the bedspread, I sharply pulled it towards me."
        show dv shocked pioneer at left with vpunch
        dv "Ahh!"
        "Dvachevskaya tried to jump up, at the same time clutching the mattress."
        "She stared at me for a couple of seconds, then…"
    elif loki:
        "I noticed a small plastic watering can on the windowsill."
        "Checked - it turned out to be almost full."
        th "Just what you need for a pleasant awakening!"
        stop music fadeout 4
        "Putting aside my disgust, I took a sip of the nasty warm water straight from the spout, returned to the bed, and..."
        play sound sfx_water_splash
        $ alt_pause(0.3)
        show dv shocked pioneer at left with vpunch
        play music music_list["revenga"] fadein 3
        dv "Ahh!"
        "A fountain of spray in the face made Dvachevskaya jump so sharply that she almost slammed her forehead into me."
        "I prudently recoiled away from her bed."
        show dv angry pioneer at left with vpunch
        dv "Did you go completely crazy?"
    else:
        th "I wonder if she's ticklish?"
        dreamgirl "There's only one way to find out."
        show dv shocked pioneer at left with vpunch
        "Dvachevskaya squealed, writhing, as if in a frying pan, but I did not even think of retreating."
        show dv shocked pioneer at left with vpunch
        dv "Stop!"
        th "Ohoho, she's ticklish alright!"
        "Only when she finally sat down on the bed, fighting off me along the way, did I put my hands behind my back in a conciliatory way and moved away from the bed."
    "For the fact that a pillow will fly straight into my head, I was quite ready - at least mentally."
    "So I moved from defense to attack faster than the girl expected."
    show dv surprise pioneer at left with dissolve
    dv "Jerk! What are you doing?"

    play sound sfx_7dl["blanket"] fadein 0
    with vpunch
    hide dv
    scene cg d4_dv_alise_falls_7dl
    with dissolve

    "She managed to shout before we crashed onto the bed."
    th "Now I literally caught the DJ for us. All that's left is to drag him to the workplace by force…"
    "Still not fully understanding what was happening, Alisa looked angrily into my eyes."
    "Fortunately, the position for this was very convenient - I crushed her with all my weight on the bed, leaving the girl no opportunity to move."
    th "No one has gotten this close to me in a long time - how many centimeters between us?"
    th "And how soon will she realize what I've done and start to breaking out?"
    scene bg int_refinery_day_7dl with dissolve
    play sound sfx_open_door_squeak_2
    "The door opened."
    show cs normal at right with dissolve
    cs "Pioneer, I said that the girl needs {i}moderate{/i} physical activity!"
    show dv shy pioneer at left with dissolve
    "I jumped out of bed as if scalded. Alisa, blushing no less than me, got up after me, trying to fix her clothes along the way."
    show cs smile at right with dissolve
    cs "March to indulge in physical activity on the street - I don't need a mess here!"
    "Under the nurse's mocking gaze, we hastened to retreat."
    stop music fadeout 4
    hide dv
    hide cs
    with dissolve
    scene bg int_aidpost_day with dissolve
    $ alt_pause(0.5)
    play sound sfx_medpunkt_door_open
    scene bg ext_aidpost_day with dissolve
    $ alt_pause(0.5)
    show dv angry pioneer
    with dissolve
    play ambience ambience_camp_center_evening fadein 1
    play music music_list["i_want_to_play"] fadein 5
    "As soon as the door slammed behind us, Dvachevskaya instantly turned to me, clenching her fists."
    "Her cheeks were still on fire."
    dv "What were you doing there?!"
    "I braced myself for the chase."
    me "Woke you up. You're actually a busy person today!"
    show dv tired pioneer with dissolve
    "Alisa frowned, and her determination to beat me seemed to subside a little."
    dv "What are you talking about?"
    me "This camp needs a DJ! And I remember you just agreed to be one yesterday. Or am I confusing something?"
    show dv normal pioneer with dissolve
    dv "Of course you're confusing!"
    "The redhead snorted."
    dv "I only agreed to become a DJ if I liked hosting the disco. Who told you that I liked it?"
    me "Don't be stupid, Dvachevskaya. I was there and saw everything with my own eyes - you almost smiled with pleasure!"
    me "Besides, I heroically fixed the radio yesterday risking of my neck, remember?"
    me "So now you can safely get to work!"
    scene bg ext_houses_day with dissolve
    "I moved towards the square, dragging the girl with me."
    "She obviously hesitated."
    show dv normal pioneer with dissolve
    dv "What am I going to do there? Change records from morning to night?"
    me "You can still announce breaking news if you want."
    me "Comrades, pioneers, urgent news! {w=1}Today, on July 22nd, Alisa Dvachevskaya from the first squad overslept morning exercises, and Sergei Syroezhkin from the first squad choked on potatoes at dinner!"
    show dv angry pioneer with dissolve
    "Redhead started riling up again."
    dv "You know what? Shove those news up your…"
    show dv surprise pioneer with dissolve
    "A procession of parents passed us, looking around with interest."
    "Slavya marched at its head, along the way telling something to the onlookers who came in large numbers."
    "Alisa and I, as if on command, shut up, seeing off the dear guests of the camp with our eyes."
    me "Will it be like this all day today?"
    show dv normal pioneer with dissolve
    dv "Yup. Until the evening."
    "The situation seems to have definitely playing in my favor."
    me "So wouldn't it be best to hide from them all in the radio room?"
    show dv grin pioneer with dissolve
    "Dvachevskaya chuckled."
    dv "I can always just go into the woods."
    "I winced."
    me "Feeding mosquitoes and soiling your uniform with damp earth?"
    me "Don't be stupid, Dvachevskaya! You only get a chance like this once in a lifetime - to control the soundtrack of an entire camp!"
    th "I feel like the more I talk her into it, the more reason she has to say no."
    "But Alisa, it seems, decided to surprise me."
    show dv laugh pioneer with dissolve
    "Raising her head, she grinned."
    dv "Okay, let's go! Let's show these old farts what kind of music the young people prefer these days!"
    dreamgirl "You know what's going to happen to both of you?"
    th "So be it!"
    th "Did I expect anything else when I went to invite her to the DJ post yesterday?"
    "So I happily rubbed my hands in anticipation of something interesting."
    "Alisa's lit eyes filled me with inexplicable courage."
    me "So, let's go to cybernetics?"
    show dv smile pioneer with dissolve
    dv "Let's drop by my cabin first. We need to get your trinket."
    me "But you will completely deplete the battery!"
    dv "So what? The cybernetics will come up with something!"
    dv "They are being fed for a reason, yeah?"
    "I was about to say that two young technicians would not be able to deal with a complex device that was at least fifteen years away in their world, but…"
    th "After all, it was my gift to her. So let her do as she pleases!"
    stop music fadeout 3
    hide dv with dissolve
    scene bg ext_house_of_dv_day with dissolve
    play ambience ambience_camp_center_day fadein 1
    play sound sfx_close_door_1
    "At Alisa's cabin, I was left sitting on the porch while the redhead ran inside."
    play sound sfx_open_door_1
    "As soon as the door slammed behind her, it immediately swung open again."
    show us smile sport with dissolve
    play music music_list["eat_some_trouble"] fadein 3
    us "PE-hello!"
    "Ulyana was in sportswear, and she was full of energy."
    show us laugh sport with dissolve
    us "Found your love? Congratulations!"
    "I rolled my eyes."
    me "Little one, you better worry about your love life. Where's your boyfriend?"
    show us normal sport with dissolve
    us "Did you overwork on the exercises today, or what? What boyfriend?"
    me "At which you threw cones in the morning. Your fiancé."
    show us dontlike sport with dissolve
    "The girl shuddered and blushed - but not from embarrassment, but from anger."
    us "What kind of fiance is he to me?!"
    me "The real one."
    me "Didn't you know that if a girl runs after a boy with the goal of throwing something at him, then this is the first and most sure sign of falling in love?"
    "I could hardly contain my laughter, and it seems that water could be boiled on Ulyana's head."
    show us angry sport with dissolve
    us "You…"
    me "Tili-tili dough!"
    me "Alisa, did you hear? Ulyanka has a boyfriend!"
    "By all indications, I went too far: the girl stood red, clenching her fists in desperation."
    us "Fool!"
    hide us with moveoutright
    "Instead of hitting me properly, Ulyana took off and sped off somewhere towards the pier."
    th "No way, was I right?"
    "Although I was a little ashamed, I couldn't stop laughing."
    play sound sfx_open_door_1
    show dv normal pioneer with dissolve
    dv "What's so funny?"
    "Alisa looked out of the house, clutching the player in her hand. Headphones also stuck out of it, tangled in such a solid nest."
    me "Nothing. I had a nice conversation with your neighbor, and let her go. She, you see, is in a hurry for a date."
    dv "With Dan'ka? I wonder how long ago they started calling joint dirty tricks dates?"
    "Alisa chuckled."
    "I shrugged my shoulders and climbed off the porch."
    me "Well, is it time to take over as a DJ?"
    stop music fadeout 5
    stop ambience fadeout 3
    return

label alt_day4_dv_dj_radio_event:
    scene bg ext_clubs_day with dissolve
    $ alt_pause(0.5)
    play sound sfx_open_door_clubs
    $ alt_pause(1)
    scene bg int_clubs_male_day
    show el normal pioneer at left
    show dv normal pioneer2 at right
    with dissolve
    play ambience ambience_clubs_inside_day fadein 3
    play music music_list["get_to_know_me_better"] fadein 3
    "In the clubhouse we found Electronik. His looked very rumpled."
    th "Did he get tired at yesterday's dances or something?"
    show el smile pioneer at left with dissolve
    el "Oh, Semyon, Alisa!"
    el "Took a long time. I've already decided that you've changed your mind about the radio!"
    show dv angry pioneer2 at right with dissolve
    show el scared pioneer at left with dissolve
    "Alisa glared at him unkindly, forcing the guy to sink his head into his shoulders."
    dv "Well? Where do we go?"
    show el serious pioneer at left with dissolve
    "Syroyezhkin waved his hand towards an inconspicuous door in the corner of the room."
    el "The radio room is there. I was just going to clean up there in the morning, but there was one force majeure..."
    show dv normal pioneer2 at right with dissolve
    show el smile2 pioneer at left with dissolve
    "He smiled guiltily."
    el "Yesterday, along with the radio, a rodent buzzer started working. It usually turns on at night, but it seems that the settings reset due to a thunderstorm, so it was, to put it mildly, unpleasant to deal with."
    el "Head hurts just terribly if you stay around for a long time!"
    show el think2 pioneer at left with dissolve
    "Grimacing, Electronik continued:"
    el "So I've been trying to turn it off all morning. Just finished."
    th "At what frequency should the buzzer work so that pioneers fall down from its influence?"
    el "You settle down there, equip everything as you like. And I, probably, should go to the infirmary."
    show el think2 pioneer at left with dissolve
    "He got up from the table and, throwing a wary glance at Alisa again,{w=.5}{nw}"
    hide el with moveoutleft
    extend " slipped out of the room."
    $ alt_pause (0.5)
    me "Well, let's hope it's not so…"
    play sound sfx_open_door_clubs_nextroom
    scene bg int_clubs_male2_night
    show dv normal pioneer2 with dspr
    $ volume(0.2, 'ambience')
    "Dvachevskaya already opened the door."
    me "…bad."
    "The whole kennelish room was littered with all sorts of junk, which either did not fit in the warehouse, or they were too lazy to bring it there."
    th "Yeah, it's going to be a big cleanup!"
    dv "You know, if you dump it all in that corner over there..."
    "Without much confidence in her voice, Alisa drawled, looking around the mess that opened before her."
    me "Perhaps we'll do that."
    "I agreed."
    me "Let's do the rest at the quiet hour."
    show dv think pioneer2 with dissolve
    "The girl grimaced."
    dv "Why? It won't be long before this shift is over. We can just drop off it to the next one!"
    me "Do you want to spend the whole quiet hour in the house?"
    me "You won't be able to walk around the area - parents should look at the ideal daily routine. The radio won't work either - that's why it's quiet hour."
    "I grabbed the first box on the rickety chair."
    me "So go ahead, Dvachevskaya! The sun is still high!"
    show dv normal pioneer2 with dissolve
    "Pushing the last box into the corner, Alisa sat down on a chair, throwing the player in her hands."
    dv "Get the wires over here - let's throw them a disco in broad daylight!"
    th "When did she sign me up as her errand boy?"
    scene bg int_clubs_male_day with dissolve
    "But still not daring to quarrel with Alisa, I obediently went to the abode of cybernetics for a plug."
    "As I expected, after the dances they did not have time to put it far, so the cable was found in a matter of seconds."
    scene bg int_clubs_male2_night with dissolve
    me "Here you go."
    "The girl grabbed the plug from me and, with a surprisingly familiar movement, stuck it into the player, after which she began to fiddle with the amplifier."
    if alt_day2_minijack:
        "To my envy, she got through this much faster than I did the day before yesterday."
        dv "Done!"
    "She turned the volume control."
    dv "Go check it out, does it work?"
    $ volume(2.0, "music")
    play music music_7dl["hurricane"]
    "And without any warning, turned on the first track that came across!"
    th "Armageddon has arrived."
    th "The earth will now open, and all of us, poor sinners, will fall into the depths of hell."
    me "Lower the volume!"
    "I cried pleadingly."
    me "You're gonna blow glass all over the camp!"
    show dv laugh pioneer2 with dissolve
    $ volume(0.7, "music")
    "Dvachevskaya turned the volume down to half, giggling happily."
    dv "Oh."
    dv "I didn't know it would be so powerful!"
    "Judging by her pleased face, she was not the least bit ashamed."
    scene bg ext_clubs_day with fade
    "Just in case, I looked outside."
    "The loudspeaker fixed on the roof of the clubs reproduced the Scorpions quite harmlessly, but a group of parents standing nearby and their guide almost crossed themselves."
    th "Heh, after such a sonic bomb!"
    show sl angry pioneer far with dissolve
    "Slavya frowned as soon as she saw me."
    "I winked at the activist and hurried away before she unleashed an angry mob on me."
    hide sl with dissolve
    scene bg int_clubs_male2_night
    show dv smile pioneer2
    with dissolve
    me "If your goal was to give someone a heart attack, then congratulations - it looks like Viola will have more work today."
    show dv laugh pioneer2 with dspr
    "Alisa leaned back contentedly in her chair, her legs up on the table."
    th "Well she's gonna fall off soon!"
    dreamgirl "And what kind of views will open after that..."
    dreamgirl "Maybe she needs a little push?"
    show dv smile pioneer2 with dspr
    dv "So what, I just have to press the buttons every three minutes?"
    "Alisa asked in a bored tone."
    me "I can make it easier for you."
    "I dragged another chair - fortunately, the clubs were empty - and sat next to the redhead, taking the player from her."
    me "Look, we can make a playlist like yesterday before the disco. Then you can put it on playback and go about your business with a clear conscience."
    th "Until, of course, until the player finally dies. Then you'll suffer with records!"
    me "Let's say this is going to be a daytime broadcast. Something quite upbeat, but unobtrusive."
    "I opened my 80s playlist."
    me "Why are you just sitting there? Help me choose!"
    "The redhead moved closer to me, peering over my shoulder at the screen."
    show dv normal pioneer2 close with dissolve
    dv "These two - definitely not."
    "She pointed at Madonna's tracks."
    dv "Add this one."
    "She approved Floyd's ”Money”."
    "ABBA, Queen, Bee Gees –  everything that would not cause sharp rejection in an inexperienced Soviet listener flew into our “daytime broadcast”."
    stop music fadeout 7
    "The playlist turned to be, according to my approximate calculations, about three hours long."
    th "It's a bit much, but we're completely free until lunchtime."
    th "How long until it, by the way?"
    show dv tired pioneer2 close with dissolve
    $ volume(1.0, "music")
    play music music_7dl["yume_akari"] fadein 3
    "I was knocked off my mind by another yawn of Alisa."
    me "Let me ask, what have you been up to all night when you're dozing off now?"
    dv "Listened to music."
    show dv closed_eyes pioneer2 close with dissolve
    "The girl folded her hands on the table and lay down on them with her cheek, closing her eyes."
    "My heart skipped a beat."
    th "So she listened after all!"
    "Of course, I was not going to share this joy with her. If I did she'd start getting suspicious thoughts..."
    "But just sitting and watching her sleep was questionable entertainment."
    "Maybe there were perverts in the world who liked to spy on sleeping girls, but I certainly was not one of them."
    th "I should shake her up somehow!"
    menu:
        "Make fun of her":
            $ alt_day4_dv_dj_radio_scoff = True
            $ lp_dv += 1
            me "Want me to sing you a lullaby?"
            dv "Huh?"
            show dv soft_smile pioneer2 close with dissolve
            "Dvachevskaya opened one eye, looking at me suspiciously."
            me "Maybe even rock you around?"
            stop music fadeout 5
            show dv shocked pioneer2 close with dissolve
            "I took a step to her."
            "Alisa straightened up, cautiously pressing herself into her chair."
            dv "You wouldn't da…"
            play music music_list["revenga"] fadein 3
            "But I couldn't be stopped!"
            show dv scared pioneer2 close:
                linear 0.5 xpos 0.5
                linear 0.025 xpos 0.505
                linear 0.05 xpos 0.495
                linear 0.05 xpos 0.505
                linear 0.05 xpos 0.495
                linear 0.025 xpos 0.5
                linear 0.5 xpos 0.5
                repeat
            dv "Ahh!"
            "The girl squealed when I tore a chair off the floor and began to rock it."
            me "Hush, little baby, do not say a word…"
            th "Guh, she only looks skinny!"
            show dv shocked pioneer2 close:
                linear 0.5 xpos 0.5
                linear 0.025 xpos 0.505
                linear 0.05 xpos 0.495
                linear 0.05 xpos 0.505
                linear 0.05 xpos 0.495
                linear 0.025 xpos 0.5
                linear 0.5 xpos 0.5
                repeat
            "Alisa did not move, looking at me with eyes full of horror. To be honest, I myself was afraid that at any moment I would lose my balance - my hands were already trembling."
            th "It's too late to retreat - all you can do is keep moving forward!"
            th "Actually, it's more like spinning around with your load in place."
            me "Don't you lie on the ed…"
            "I noticed the wire under my foot with peripheral vision much earlier than I had time to react to it with my body. Perhaps that is why I was not at all surprised by the fact that my position began to abruptly turn into a horizontal one."
            play sound sfx_chair_fall
            hide dv
            with vpunch
            scene black with flash_red
            scene bg int_clubs_male2_night
            show unblink
            with dissolve
            stop music fadeout 4
            me "Are you alive?"
            "I croaked - the air was knocked out of my lungs by a blow to the floor."
            th "And for the second time in a day, we're in a stupid position, except now she's on top."
            dreamgirl "Changing positions regularly is good!"
            dreamgirl "Brings, so to speak, variety to the process..."
            show dv angry pioneer2 with dissolve
            play music music_7dl["what_am_i_doing_here"] fadein 3
            dv "You're such an idiot."
            "Alisa snorted as she got up off me."
            "In the process, she - on purpose, I was sure of it! - painfully kicked my stomach with her knee."
            me "Glad to try!"
            "I lifted my thumb up and began to slowly lower it, whistling a tune from the second Terminator."
            "Redhead broke down and laughed out loud."
            show dv laugh pioneer2 with dissolve
            dv "After this, you definitely won't fall asleep!"
            play sound sfx_knock_door2
            $ alt_pause(0.2)
            play sound sfx_open_door_clubs_nextroom
            "There was a delicate knock on the door of the radio room before it opened slightly, revealing the swirling head of the Electronik."
            show el normal pioneer at fleft with dissolve
            el "Nice job, Ali…"
            "He noticed me lying on the floor and pinned down by the ill-fated chair. A thumbs up hardly added clarity to what was happening."
            show el surprise pioneer at fleft with dissolve
            el "Is everything alright?"
            "Dvachevskaya grinned impudently."
            show dv grin pioneer2 with dissolve
            dv "Definitely. Close the door on the other side and stop spoiling the working atmosphere!"
            th "Working atmosphere? Now I know how it's called!"
            show el sad pioneer at fleft with dissolve
            el "Actually, I wanted to invite you to dinner. For some reason, the horn didn't work because of the music, so…"
            show el upset pioneer at fleft with dissolve
            "He awkwardly nodded his head."
            el "Are you coming or not?"
            dv "You don't have to wait for us - we know the way to the canteen."
            hide el with moveoutleft
            "Glancing at me again - I was ready to swear that sympathy slipped through his eyes - Syroezhkin hastily retreated, leaving Alisa and me alone."
            "While I was grunting, dusting myself off and getting up, the girl had already turned off all the equipment, disconnected the player from the amplifier and carefully put it in her pocket."
            "And for some reason I was flattered that she did not want to part with him."
            th "I'm getting too sentimental in this camp!"
            dreamgirl "I suggest you check if you hit your head while playing Hercules."
            dreamgirl "Sentimental feelings for a redhead are pure masochism!"
            me "Let's go. If the parents are still here..."
            show dv soft_smile pioneer2 with dissolve
            dv "They'll eat everything clean, no doubt about it!"
            hide dv with MoveTransition(1.5, leave=offscreenleft)
            "Alisa winked at me, running out of the closet."
            dv "Keep up, slowpoke!"
        "Ask her opinion on the music":
            $ alt_pause(1)
            me "So, how do you like the songs?"
            "As neutral as possible, I asked, trying not to betray my curiosity to the full."
            dv "Fine."
            "Alisa answered lazily without opening her eyes."
            dv "A lot of old junk, sure, but it's fine."
            th "Junk?"
            th "Did she only listen to the disco playlist?"
            "It was not like Alisa. It seemed to me that she liked the good old rock. She liked Splin, after all!"
            th "And she knows about it from somewhere..."
            me "And what junk were you listening to there?"
            show dv think pioneer2 close with dissolve
            dv "These Germans… I don't remember, really."
            show dv sad pioneer2 close with dissolve
            dv "Get off me, let me sleep!"
            show dv closed_eyes pioneer2 close with dissolve
            th "Modern Talking?"
            dreamgirl "Definitely not Sabaton."
            "Inner voice chuckled."
            th "They're Swedes. Germans – Powerwolf."
            dreamgirl "What's the difference? No one can tell them apart anyway!"
            "I leaned back in my chair, staring absentmindedly ahead of me."
            th "You know what's the weirdest thing about this?"
            dreamgirl "I know, of course."
            dreamgirl "You're locked in a cramped closet one on one with a pretty girl, and what are you doing in such a comfortable and pleasant situation? That's right, nothing!"
            dreamgirl "Tell me honestly, are you impotent?"
            th "Oh, listening to you - I should have been throwing myself at everything that has a breast size other than zero from day one!"
            dreamgirl "Well, throwing yourself at the PE teacher wouldn't be necessary..."
            dreamgirl "But don't get distracted! You like her, dumbass!"
            dreamgirl "Are you planning to do something about it or not?"
            "I looked at the peacefully sleeping Alisa."
            th "What to do about it? She doesn't accept courtship!"
            if (alt_day3_dancing1 == 'dv_1'):
                "Her refusal to dance with me yesterday was a direct confirmation of this. But this morning in the infirmary…"
            else:
                "But what happened in the infirmary this morning…"
            th "We behaved no better than Ulyana, who throws cones at the object of her sigh. But it was... fun?"
            th "Probably."
            dreamgirl "Are you also going to cone..."
            play sound sfx_open_door_clubs_nextroom
            "The closet door swung open."
            el "Alisa!"
            show el shocked pioneer at fleft with dissolve
            "I turned to Syroezhkin, who had entered. He froze with his mouth open, obviously not wanting to personally wake up the disaster, while it was quietly sniffing, drooling on the table."
            me "What happened?"
            "Quietly I asked."
            show el normal pioneer at fleft with dissolve
            el "Dinner."
            "Electronik answered succinctly."
            el "The horn didn't work. I'm running around, gathering everyone."
            hide el with dissolve
            "I nodded my thanks, and the guy hurried off. I had to pick up the redhead again."
            me "Alisa!"
            show dv concent pioneer2 close with dissolve
            dv "Huh?"
            "She asked sleepily, raising her head. There was a red dent on her cheek."
            me "Let's eat! You'll get enough sleep in the afterlife."
            show dv concent pioneer2 with dissolve
            "Alisa reluctantly got up from the table and began to turn off the equipment."
            dv "Imagine this, I dreamed about that song..."
            show dv think pioneer2 with dissolve
            "She wrinkled her forehead, trying to remember something."
            me "Which one?"
            dv "From the movie. Where everything exploded at the end!"
            th "Great description. And most importantly - very colorful!"
            "I could immediately name about a dozen, and this is without options from the twenty-first century."
            show dv normal pioneer2 with dissolve
            "Alisa waved her hand."
            dv "Okay, I'll find it later! Let's go eat already."
            hide dv with MoveTransition(1.5, leave=offscreenleft)
            "She slipped the player into her pocket and left, leaving me with no option but to follow her."
    $ volume(1.0, 'ambience')
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day4_dv_dj_lunch:
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 2
    "Thanks to a broken horn in the canteen today it was suspiciously quiet. The people were only pulling up when we arrived, and the line for the distribution consisted only of the most hungry."
    th "Not at the call of the horn, but at the call of the stomach!"
    show dv sad pioneer with dissolve
    dv "And what's this?"
    "Alisa grimaced, nodding at the vat of soup, from which the cook generously poured an incomprehensible substance into plates. It smelled... peculiar."
    voice "Fruit soup. Come in, don't delay the queue!"
    show dv sad_smile pioneer with dissolve
    "Giving the redhead a plate of lazy cabbage rolls to boot, the cook reached for the next plate - for me."
    "I just grinned at Alisa's lean face."
    th "I don't think this will be any worse than my first attempts at cooking on my own. Still looks nicer than a charred potato!"
    show dv normal pioneer with dissolve
    dv "Let's go to Ulyanka, she just sits alone."
    "Alisa nodded towards her friend. I looked longingly at an empty table nearby."
    th "I'm afraid that after my morning concert, the little one won't limit herself to just centipedes. She obviously has a rich fantasy."
    "But the redhead had already placed her tray in front of Ulyana, so I had no choice but to land next to her."

    play music music_list["my_daily_life"] fadein 5
    show dv normal pioneer close at right with dissolve
    show us angry sport close at left with dissolve

    "The girl glared at me as she leaned over her bowl of soup."
    show us grin sport close at left with dissolve
    "However, her bad mood dissipated suspiciously quickly, and she winked fervently at Alisa."
    us "That's what you did today! Literally a bomb!"
    th "Yeah, it really should have looked like an explosion..."
    show dv grin pioneer close at right with dissolve
    "Dvachevskaya grinned proudly."
    dv "I'll show them some more fun - they'll rock!"
    us "Were you playing everything from his trinket?"
    show us surp1 sport close at left with dissolve
    "Ulyana's eyes, after an affirmative nod, lit up oh, how bad..."
    us "Do you have it with you?"
    show dv normal pioneer close at right with dissolve
    "Alisa took out the player from her pocket, showing it to the kid."
    show us smile sport close at left with dissolve
    "She squirmed happily in her chair."
    us "So why don't we shake them up now? With this nasty..."
    show us upset sport close at left with dissolve
    "She pushed apricot soup away from her in disgust."
    us "…you could choke on it, and if you do the same trick as in the morning…"
    show us laugh sport close at left with dissolve
    us "And what, do we have speakers hanging in the canteen for no reason?"
    "I rolled my eyes. The little one seemed to me much more resourceful in matters of dirty tricks."
    th "Scare people with a sonic screamer for the second time this day?"
    th "Wouldn't it be nice to put on a hymn there to get everyone up and ruin dinner..."
    "However, I didn't have the USSR anthem on my player."
    show us smile sport close at left with dissolve
    us "Well, why are you sitting like stumps? Gimme your thing!"
    menu:
        "Agree":
            $ lp_dv += 1
            th "It's a stupid idea, but who's going to ask my opinion?"
            th "I'm not sure that the little one has even a rough idea of how to connect to these speakers. Especially since we don't even have a wire with us!"
            me "Go ahead. Just mind that all the implementation is on you."
            me "And the consequences too!"
            show us laugh sport close at left with dissolve
            "Smiling broadly, Ulyana snatched the player from Alisa's hands. She was busily pressing the buttons - she definitely remembered something from my briefing yesterday! - and was about to jump out from behind the table, but suddenly she frowned."
        "Dissuade her" if herc:
            $ karma += 5
            me "You won't succeed, don't even try."
            show us sad sport close at left with dissolve
            "Ulyana frowned."
            us "Why do you think that?"
            me "There's only a couple of minutes of charge left. Turn it on and it will immediately shut down."
            me "Check it out yourself!"
            "The girl grabbed the player from Alisa's hands and began to randomly press all the buttons. Her face immediately turned sour."
        "Refuse":
            th "I'm not going to participate in nonsense!"
            me "Kid, eat your soup and don't show off. Enough hooliganism for today, which can be pinned on me and Dvachevskaya!"
            show us dontlike sport close at left with dissolve
            "Ulyana showed me her tongue."
            us "Ugh, what an old grump you are!"
            show us grin sport close at left with dissolve
            "And then she snatched the player from Alisa, winking slyly at me!"
            th "Oh you…"
            "I was about to get up and take it away by force, but Ulyana, who managed to randomly poke all the buttons, disappointedly slammed the player on the table."
    show us calml sport close at left with dissolve
    us "It doesn't work!"
    us "Blinked and turned off. You bastards!"
    show dv surprise pioneer close at right with dissolve
    "Alisa and I looked at each other in bewilderment."
    me "I told you it was almost out of power."
    show dv sad pioneer close at right with dissolve
    dv "And what does that mean?"
    "Alisa drawled."
    dv "Do I have to manually change records now?"
    "I threw up my hands."
    me "Nothing in life is easy. Didn't you know?"
    show dv angry pioneer close at right with dissolve
    "The redhead flared up."
    dv "Oh no, I definitely didn't sign up for slave labor!"
    me "Come on, Dvachevskaya, you'll like it. It's not an all-day activity: three hours in the morning, three in the evening."
    me "If you want, we can get a second player, and then I'll teach you how to do such tricks with sound that you'll go home as a professional DJ!"
    th "Assuming records are still around somewhere outside of this camp."
    show dv normal pioneer close at right with dissolve
    "Huffing incredulously, Alisa pushed the plate with the second away from her."
    dv "No, it's absolutely impossible to eat this disgusting thing."
    show us smile sport close at left with dissolve
    us "Give it here!"
    "Ulyana grabbed a plate of lazy cabbage rolls right from under my nose. With anguish, I looked at the missed extra dose of calories with my eyes."
    show us grin sport close at left with dissolve
    "Noticing this, the little one winked."
    us "Early bird gets the worm!"
    "And, leaving me no hope of intercepting a portion, she actively worked her jaws."
    me "If you're done with your meal, then let's go. We still have some cleaning to do."
    hide us with dissolve
    show dv normal pioneer with dissolve
    "Alisa silently finished her kompot and got up from the table. We dragged our dishes to the sink."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day4_dv_dj_silent_hour:
    show bg ext_dining_hall_near_day
    show mt angry pioneer
    with dissolve
    play ambience ambience_camp_center_day fadein 2
    play music music_list["everyday_theme"] fadein 2
    "At the exit from the canteen, it was as if squad leader was waiting for us on purpose."
    mt "Alisa, is there anything you want to explain to me?"
    show mt normal pioneer with dissolve
    th "What should she explain?"
    th "She wasn't instructed on how to operate all this equipment. You could at least say thank you that the radio went off at all!"
    show dv angry pioneer at fleft with dissolve
    dv "Technical problems."
    "Alisa grunted. She was not a bit ashamed!"
    show mt angry pioneer with dissolve
    "Olga frowned."
    mt "One more failure like this and the camp DJ post will be free again!"
    show mt normal pioneer with dissolve
    mt "Now let's go to the cabins! Quiet hour starts in ten minutes."
    show dv normal pioneer at fleft with dissolve
    me "We need to clean up the radio room, Olga Dmitrievna. During the time the camp was without a radio, it managed to turn into a shed."
    me "You should've seen the kind of shi…"
    show mt angry pioneer with dissolve
    "The squad leader gave me a stern look, and I coughed tactfully."
    me "…mess. Absolutely impossible to work!"
    show mt normal pioneer with dissolve
    mt "Fine, go do that. {w}As long as I don’t see or hear you until afternoon!"
    hide mt with dissolve
    $ alt_pause(0.5)
    show mt normal pioneer far with dissolve
    "We had already moved a couple of meters from the porch when Olga called us again."
    mt "Semyon, your parents gave you a present. You can pick it up at the cabin."
    hide mt with dissolve
    th "Parents? What nonsense!"
    "Alisa interpreted the confusion on my face in her own way."
    show dv smile pioneer with dissolve
    dv "Do they think you're starving here?"
    me "Huh?"
    dv "You haven't even spent three days here, but you already have some goodies!"
    show dv laugh pioneer with dissolve
    "She snorted."
    dv "Like, the kid will die on canteen grubs!"
    me "Come on, you!"
    "I felt myself blushing."
    th "To appear to Dvachevskaya as a sissy - could I have imagined a more epic failure?"
    th "Besides, I have no idea where my parents came from!"
    "But the redhead suddenly got serious."
    show dv dontlike pioneer with dissolve
    dv "In general, I'll tell you something: things like these should be appreciated."
    show dv dontlike pioneer at center with move
    hide dv with dissolve
    "And without another word, she hurried forward under my surprised gaze."
    me "Wait, Dvachevskaya!"
    show dv angry pioneer far with dissolve
    "She turned around, frowning in annoyance."
    dv "What else?"
    me "Let's drop by my place first? We still need to see what kind of a gift there is - maybe it's something edible."
    show dv sad pioneer with dissolve
    "Alisa seemed to shrink, averting her eyes to the side."
    dv "Didn't eat enough at dinner, did you?"
    me "I'm full, and you? You haven't even touched your food, and you overslept breakfast."
    show dv sad_smile pioneer with dissolve
    dv "Don't worry about it. I'll live until lunch."
    play sound sfx_stomach_growl
    "But the loud rumbling in her stomach said otherwise."
    show dv guilty pioneer with dissolve
    "Sighing heavily, Alisa was forced to admit her defeat."
    dv "Then get moving - you've got to get there before nap time starts!"
    stop music fadeout 3
    stop ambience fadeout 3
    with fade

    scene bg int_house_of_mt_backpack_day with dissolve
    play sound sfx_unlock_door_campus
    $ alt_pause(1)
    play ambience ambience_int_cabin_day fadein 2
    play music music_list["trapped_in_dreams"] fadein 3
    "Hung on a chair by my bed was a battered and all too familiar backpack. My good old 'Grizzly', like an affectionate greeting from a past life."
    th "Well, this is clearly something foreign to these places - such only began to appear in the markets in the mid-nineties. And this one also looks exactly like mine."
    scene bg int_house_of_mt_day
    show backpack at truecenter with dissolve
    "The characteristic wear on the strap spoke of this directly, leaving no reason to doubt."
    "I did not find anything other than a backpack that could resemble the notorious gifts."
    th "Okay, we'll deal with this later. Time to get out before Olga reams our ass!"
    play sound sfx_open_door_1
    $ alt_pause(1)
    scene bg ext_house_of_mt_day with dissolve
    show dv normal pioneer2 at cright with dissolve
    "Alisa was waiting for me on the porch, looking around nervously. The prospect of meeting with the squad leader for no particular reason clearly did not smile at her."
    "We hurried to the clubs, overtaking the sleepy pioneers trudging to their houses."
    scene bg ext_clubs_day
    show dv smile pioneer2 at cright
    with dissolve
    dv "Okay, at least after lunch we can do something normal - I've wanted to show you one place for a long time..."
    me "What happens after lunch?"
    "I interrupted her."
    show dv normal pioneer2 at cright with dissolve
    dv "A concert for parents. {w} The kids will sing and dance, but that's none of our business."
    me "But don't you play the guitar? You could…"
    dv "Couldn't."
    "Cut off by a girl."
    dv "Mine didn't come - why grimace then?"
    "And, without letting me continue, she flung open the doors of the clubs."
    stop music fadeout 3
    play sound sfx_open_door_clubs_2
    scene bg int_clubs_male_day with dissolve
    play ambience ambience_clubs_inside_day fadein 1
    show el normal pioneer at left
    show sh normal pioneer at right
    with dissolve
    show el shocked pioneer with dissolve

    el "What, radio also works during quiet hour?"

    "Electronik asked dumbfounded."
    show sh upset pioneer with dissolve
    "Him and Shurik were sitting at the table, bending over some kind of a blueprint. Seeing Alisa, the bespectacled man tensed up no less than his curly-haired friend."
    show dv laugh pioneer2 with dissolve
    dv "Don't worry, I won't bite you."
    "Alisa promised not in a very soothing tone."
    dv "We're here to clean up that trash you left in the radio room."
    me "Let's not interfere."
    th "At least we'll try. With this Dvachevskaya, you can never predict the beginning of trouble!"
    dreamgirl "Is she really the problem? I thought you were the one who caused all the trouble today."
    th "But only under her evil influence!"
    play sound sfx_open_door_clubs_nextroom
    scene bg int_clubs_male2_night
    show dv normal pioneer2
    with dspr
    $ alt_pause(0.4)
    play sound sfx_close_door_1
    play music music_7dl["thanks"] fadein 3
    "We squeezed into the closet, closing the door behind us. Alisa put the now useless player on the table and looked around."
    dv "To throw it all out the door, and then let these nerds figure out what they need and what they don't."
    show dv smile pioneer2 with dissolve
    "She dreamily closed her eyes."
    dv "It's better to just burn it. We were planning a fire tomorrow…"
    hide dv with dissolve
    show backpack at truecenter with dissolve
    play sound sfx_7dl["backpack"]
    "In the meantime, I plunged into the depths of my backpack in search of the promised gifts. {w}Only the contents did not in any way resemble the usual cookies and pies in such cases."
    "In addition to some very useful items in the camp - such as a brand new deck of cards and a folding knife - some rather strange finds were found in the backpack: a box of camping matches, fishing hooks, lead weights and two sets of keys."
    "Under all this stuff, there was a purse and a bag of sweets lying around. That's what I needed!"
    hide backpack with dissolve
    me "Come on, Dvachevskaya."
    "I handed the candy to the girl."
    me "Not a lot, of course, but we don't barge ourselves, sir."
    show dv laugh pioneer2 with dissolve
    dv "Apparently, I got excited about the starving child - you are not spoiled much!"
    hide dv with dissolve
    "Alisa snorted, but took the sweets very willingly. {w}I was about to put away the backpack with all its useless contents, but then something clicked in my head."
    show backpack at truecenter with flash
    "I used to have a habit of carrying wires with me in case of any unforeseen situations. In times of still turbulent youth, it helped out more than once."
    if herc:
        "Only now the wire was not there and could not be - Maha ate it when she was still small. But the adapter…"
    else:
        "Only now the wire was irretrievably lost a couple of years ago, and I definitely remembered that I never bothered to put a new one. But the adapter…"
    "I put my hand hopefully into an inconspicuous pocket in the very corner of the small compartment."
    hide backpack with dissolve
    me "Well, Mr. DJ, congratulations, you can safely continue to mess around until the end of the shift!"
    show dv shocked pioneer2 with dissolve
    dv "What are you talking about?"
    "Alisa mumbled with her mouth full. She already managed to cleanly destroy the sweets."
    "I proudly lifted the found adapter above my head. The plug was slightly bent, but at first glance it was not critical - you could straighten it with your hands."
    th "As a last resort, I'll ask the cyberneticians. They must know at least something!"
    show dv normal pioneer2 with dissolve
    dv "What is this? A new player?"
    th "Finally, at least someone memorized this word! Unlike everyone else going “thing”, “toy”, “trinket” - no respect."
    me "Better - charger for the old one."
    show dv think pioneer2 with dissolve
    "Alisa looked suspiciously at the adapter in my hand."
    show dv smile pioneer2 with dissolve
    extend " And then suddenly chuckled happily."
    dv "There are no free sockets here, so we'll have to push our dear neighbors."
    scene bg int_clubs_male_day:
        xcenter 0.8
        ycenter 0.3
        zoom 1.9
    with diam
    "Electronik kindly provided us with a place to charge next to the windowsill. Out of the corner of my eye, I noticed a kettle and a muddy two-liter jar nearby."
    th "They're definitely spending time here nicely!"
    if 'cyber' in list_joined_clubs_7dl:
        th "It might even be worth taking a look at them. Of course, if there are cookies in the work plans."
    else:
        th "If I knew that they are chasing tea here, maybe I would sign up for them."
        th "Probably not, though. My time is worth a lot more than a potential bag of cookies!"
    scene bg int_clubs_male2_night
    show dv concent pioneer2 at cleft with dissolve
    with diam
    "After making sure that the player was charging, I returned to the closet with a clear conscience. {w}Alisa has already managed to make a frantic activity there, dragging bundles of old newspapers to the exit."
    show dv normal pioneer2 at cright with dissolve
    dv "And why is this here, one wonders, this waste paper? So it collects dust?"
    "I stealthily glanced at one of the top newspapers. It was already noticeably yellowed Komsomolskaya Pravda, dated 1980."
    "Unable to resist, I grabbed it and unfolded it with interest."
    play sound sfx_paper_bag fadein 0
    "{i}“A walk in the biofield? A report about a meeting with a person who has a gift of nature that has not yet been unraveled”{/i}, read the headline on the page I opened. I briefly read the text - the article was about Juna, the most famous charlatan of the entire Union."
    th "And they also say that there was no obscurantism in the purely atheistic USSR!"
    show dv laugh pioneer2 close at center with dissolve
    dv "Have you signed up to be an archaeologist?"
    "Dvachevskaya grunted, looking over my shoulder."
    dv "Oh, isn't that the crazy aunt who declared herself queen of the Austrian people?"
    show dv think pioneer2 with dissolve
    dv "Or Arabian… Eh, I don't remember!"
    show dv normal pioneer2 with dissolve
    dv "Another scammer. {w}Earlier, these fortune-tellers screamed at every turn about their superpowers, there was no way to avoid them."
    me "Gypsies, or what?"
    dv "Yeah. And those of them who weren't gypsies diligently pretended to be."
    show dv smile pioneer2
    play sound sfx_punch_medium
    with hpunch
    "Alisa kicked me in the side."
    dv "Stop messing around already! Who was screaming the loudest about wanting to get out of here?"
    "It was difficult to argue with Dvachevskaya, so with a sigh I threw the newspaper to the others and set to work on the boxes in the corner."

    scene black with clock_r
    $ alt_pause(1.0)
    scene bg int_clubs_male2_night
    show el normal pioneer at fleft
    with clock_r

    el "You didn't find a soldering iron there, by any chance?"
    "Electronik poked his head into our closet."
    me "We didn't."
    th "But when we will find it, we'll definitely shove it up your..."
    show dv normal pioneer2 at cright with dissolve
    dv "This one?"
    "Alisa asked, taking out a soldering iron from another box."
    show el normal pioneer at left with move
    el "Yeah, that one! I…"
    "Syroezhkin exclaimed delightedly, stepping forward."
    dv "Catch."
    stop music fadeout 1
    $ renpy.show("bg int_clubs_male2_night", what = Notch("bg int_clubs_male2_night"))
    with dissolve
    $ alt_pause(0.9)
    play sound sfx_7dl["dropw"]
    with vpunch
    with flash
    "The reaction time of the guy was clearly so-so - in a second, the soldering iron crashed to the floor, breaking into two parts."
    show bg int_clubs_male2_night
    show el sad pioneer at left
    show dv normal pioneer2 at cright
    with dissolve
    el "…was going to repair it now."
    "Electronik said in a fallen voice, looking in confusion at how the sting falls into a wide gap in the floor."
    play music music_list["you_lost_me"] fadein 3
    "I felt ashamed."
    th "Why does she act like that with them?"
    th "Why do you have to bring trouble to everyone around you?"
    "Over the past few days, I have become accustomed to Alisa's antics, and some of them even began to find amusing, but the despair on the face of a cybernetics who tried his best to help us..."
    th "This is too much!"
    "I squatted down and peered through the gap."
    me "Not very deep. Do you have a ruler or something to pick up?"
    hide el with moveoutleft
    "The guy nodded dejectedly, picked up a wooden handle that had not had time to roll back from the floor and left. I glared angrily at Dvachevskaya."
    show dv normal pioneer2 at center with dissolve
    me "And why the hell, excuse me?"
    show dv grin pioneer2 with dissolve
    "She just shrugged."
    dv "What's wrong? He asked for a soldering iron - I gave it."
    dv "It's his own fault for being such a bungler!"
    me "There's reason for hazing around here!"
    show dv angry pioneer2 with dissolve
    "I barked. Alisa bared her teeth."
    dv "And what do {b}you{/b} know about hazing?"
    if herc:
        me "More than you, brat!"
    else:
        me "That I won't let it happen in my presence, got that?"
    show dv scared pioneer2 far with dissolve
    "Alisa staggered back in fear. It was not surprising - I was very, very angry."
    show dv guilty pioneer2 far with dissolve
    dv "You don't understand jokes at all…"
    me "It's you who doesn't understand if breaking someone else's property is just a joke to you!"
    me "Seryoga helps us here, rushes with us, and you..."
    hide dv with dissolve
    "I turned away so as not to soften at the sight of a confused Alisa."
    th "No! If no one could restrain her before, and she's so unrestrained, then it's time to put an end to this."
    me "In short, if you're going to continue to act like a pig with people who want to do something good for you, then you and I are not gonna get along."
    "I expected anything - an indifferent silence, which means that I am free, angry cries, and at least a fight - but not a quiet and drawn-out sigh!"
    show dv sad pioneer2 far with dissolve
    stop music fadeout 3
    dv "I really... overdid it."
    "Alisa squeezed out of herself, as if stepping on her own throat. Her eyebrows converged on the bridge of her nose, and her eyes drilled into the wooden floor."
    th "Overdone is not the right word!"
    me "Can you at least apologize?"
    "I inquired caustically."
    show dv angry pioneer2 far with dissolve
    "Alisa is back in her usual berserk mode."
    dv "Here's another one!"
    "She snorted. Her eyes gleamed angrily in the twilight of the radio room."
    dv "I didn't ask to be lectured!"
    th "Okay. Realized it was her fault - thanks for that."
    me "I leave it up to you."
    show dv angry pioneer2 far at fleft with dissolve
    hide dv with easeoutleft
    "Alisa shrugged her shoulders indifferently, grabbed two bundles of newspapers and headed for the exit."
    play music music_7dl["midday_reverie"] fadein 3
    show el sad pioneer with moveinleft
    "A few seconds later, Electronik poked himself into the closet again - with a half-meter metal ruler in his hands."
    el "Couldn't find anything smaller."
    me "Come on, it'll do."
    "I took the ruler away from him and bent over the damn crack again."
    me "Listen, about Alisa..."
    show el upset pioneer with dissolve
    "Electronik waved it off."
    el "Never mind. I understand everything, they all have such habits, so it's silly to be offended."
    me "What kind of {b}all of them{/b}?"
    show el surprise pioneer with dissolve
    "The guy belatedly bit his tongue. {w}The expression on his face conveyed in all colors a single word."
    "”Oopsie”."
    show el normal pioneer with dissolve
    el "Ask her yourself."
    "In the meantime, I just fished the sting out of the floor and handed it to Electronics. He nodded gratefully."
    el "Thank you very much!"
    me "And yet..."
    show el upset pioneer with dissolve
    "Syroyezhkin looked at me pleadingly."
    el "I can't talk about it! What if she doesn't want you to know?{w=1}{nw}"
    play sound sfx_angry_ulyana fadein 1
    show dv rage pioneer2 far at fleft with dissolve
    dv "Knew about what?"
    "There was a serious threat in Alisa's voice."
    show el shocked pioneer far
    show dv rage pioneer2 at fleft
    with dissolve
    "Electronik huddled into a ball, hastily moving away from the door."
    el "Nothing. I'm leaving, I won't disturb you!"
    show el scared pioneer far at cleft with move
    $ alt_pause(0.2)
    show el scared pioneer far at left with move
    $ alt_pause(0.2)
    show el scared pioneer far at fleft with move
    $ alt_pause(0.2)
    hide el with moveoutleft
    th "If his goal was to intrigue me, then he did a great job, needless to say."
    dreamgirl "Don't you understand yet?"
    th "Not you too..."
    show dv normal pioneer2 at center with dissolve
    dv "Settled with crazy people!"
    "Alisa spat, picking up the last bundle of newspapers. And this time I almost agreed with her."
    scene bg int_clubs_dj_7dl
    show dv tired pioneer2 close
    with fade
    $ volume(0.7, "music")
    "With our joint efforts, the closet has finally acquired a reasonable form."
    th "Not the coolest radio station in the world, of course, but now you can at least turn around here calmly, without fear of falling down or tripping over something."
    if alt_day4_dv_dj_radio_scoff:
        "I prudently hid the wires under the table, mindful of the morning incident.."
    th "It would be nice to sweep here too, but there is no moral strength left for this. I believe same goes for my partner too."
    stop music fadeout 3
    $ volume(0.5, "sound")
    play sound sfx_7dl["eat_horn"] fadein 3
    $ volume(1.0, "music")
    "Just as I leaned back in my chair and breathed a sigh of relief, a horn blew from the roof above our heads."
    show dv smile pioneer2 close with dissolve
    "Alisa's face lit up."
    dv "I thought nap time tonight would be endless!"
    $ volume(1.0, "sound")
    show dv smile pioneer2 with dissolve
    hide dv with moveoutleft
    "Happily jumping up, she rushed to the door, not even turning around to me. I grinned, following her."
    th "Maybe she's so angry from hunger?"
    dreamgirl "Or something else."
    th "Oh yeah…"
    dreamgirl "Did you notice that she was taking the papers out on the porch too long?"
    th "Shush!"
    th "There must be a mystery in a woman."
    "Sliding my chair back, I hurried after my squad comrades - after all my body clearly lacked just one plate of cabbage rolls at dinner."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day4_dv_dj_afternoon:
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 1
    play music music_list["get_to_know_me_better"] fadein 2
    show dv normal pioneer at left with dissolve
    "The dining room was noisy again, as it had been in the morning. I thought with annoyance that it would be a good idea to break the speakers before the end of the day."
    show mi smile pioneer at right with dissolve
    mi "Alisa!"
    "Happily, our artistic director called Alisa, who was chewing a gingerbread next to me."
    show mi grin pioneer with dissolve
    mi "Alisa, do you remember that I signed you up to perform for today? You just weren't at the rehearsal, so I was surprised..."
    show dv surprise pioneer with dissolve
    "Dvachevskaya choked, splashing Miku and me with kefir."
    dv "What the hell? I didn't agree!"
    mi "What do you mean you didn't agree?"
    show mi surprise pioneer with dissolve
    "Miku muttered in amazement.."
    show mi dontlike pioneer with dissolve
    "After thinking for a second, she frowned:"
    mi "{cps=*1.5}I met you this morning, even before exercises, and asked if you hadn't changed your mind about the performance, and you said “yeah”, so I…{/cps}"
    show dv dontlike pioneer with dissolve
    dv "No need to twist my words here! First, I said “yeah, just back off”. And secondly - I didn’t even hear what you were asking there."
    show mi sad pioneer with dissolve
    "Miku looked like she was about to cry. She looked at me in confusion for support."
    th "Here, again, someone wants to make me guilty."
    th "What about me?"
    me "What, you'll lose something, or what, if you sing one song to them?"
    th "I don't mind!"
    me "Let's get together, about the grasshopper! There's a grasshopper in the grass..."
    show dv surprise pioneer with dissolve
    dv "Are you crazy? What grasshopper?"
    me "The one they all expect to hear at the camp concert."
    "I nodded towards the table occupied by the lively parents."
    me "Is it possible to perform something else here?"
    show dv laugh pioneer with dissolve
    "Alisa snorted, looking at me like I was an idiot."
    dv "Of course you can! I played Kino at the last concert!"
    th "Oh, how easy it is to manipulate her!"
    me "Are you embarrassed because of parents? Are you afraid that they won't let you join the Komsomol?"
    show dv normal pioneer with dissolve
    dv "Hell no! I'm not afraid of anything!"
    show mi grin pioneer with dissolve
    mi "So you're still going to perform?"
    "I looked at Miku with annoyance: well, how did she get in at the wrong time! Alisa grunted again, crossing her arms over her chest."
    show dv dontlike pioneer with dissolve
    dv "No. And don't even try to persuade me - I don't want to, so I won't."
    show mi sad pioneer with dissolve
    "On the one hand, I have always respected the right of another person not to do what he absolutely does not want to do, but on the other... "
    th "This is Dvachevskaya!"
    th "Making her do something is a matter of principle!"
    th "Lever number one - challenging her - didn't work."
    me "Well, now Miku will have to explain to Olga Dmitrievna why someone will perform twice because of you..."
    th "Lever number two: guilt."
    show mi normal pioneer with dissolve
    mi "{cps=*1.5}I won't have to, she doesn't even know that Alisa has agreed to perform. I've been running around in the morning, reminding everyone about the rehearsal, that I completely forgot to warn her!{/cps}"
    "Miku didn't seem too eager to help me drag Alisa to the concert."
    th "Then there is only one last lever left. But here I have to go all-in!"
    me "Even so? Then it's no wonder you still hope Alisa performs."
    show dv surprise pioneer with dissolve
    show mi surprise pioneer with dissolve
    "I chuckled, catching the surprised looks of the girls on me."
    mi "What's wrong with that?"
    me "The squad leader will never let her on the stage. I'll bet you anything that if you approach her now, she will turn you around and send you to hell."
    dv "You think so?"
    show dv smile pioneer with dissolve
    "Alisa smiled wickedly."
    dv "And what are you willing to offer if I suddenly get released on stage?"
    me "Whatever, just ask. And if I'm right..."
    "I squinted at the redhead appraisingly."
    me "In that case, you'll kiss Miku. Deeply."
    show dv shocked pioneer with dissolve
    show mi shocked pioneer with dissolve
    "The eyes of both rounded like five-ruble coins."
    show dv angry pioneer with dissolve
    "Alisa was the first to come to her senses while Miku blushed."
    dv "You… you…"
    show mi shy pioneer with dissolve
    mi "Pervert!"
    show dv angry pioneer far
    show mi shy pioneer far
    with dissolve
    "Smiling charmingly, I took a step back, preparing to flee in advance."
    me "Your bets, ladies?"
    dv "I'll figure it out later."
    "Alisa hissed."
    dv "And don't expect you to be able to sneak away. Otherwise, I'll give you..."
    "She defiantly cracked her knuckles."

    dv "Let's go, Miku!"
    me "Practice?"
    "I inquired sarcastically after them."
    show dv rage pioneer far with dissolve
    "Alisa gave me the middle finger without even bothering to turn around."
    hide dv
    hide mi
    with MoveTransition(1.5, leave=offscreenleft)
    $ alt_pause(0.5)
    th "It's done!"
    dreamgirl "Aren't you afraid she'll ask for something equally extravagant in return?"
    th "It's okay. What can a hooliganish, but still strictly brought up girl in the union, offer me?"
    dreamgirl "Well, well. Prepare for the worst, mate."
    dreamgirl "Maybe she will take note of your desire?"
    th "Like I don't mind kissing Miku!"
    dreamgirl "And Electronik?"
    th "But somehow I didn't think about it..."
    dreamgirl "You don't do that very often."
    "Drinking the rest of the kefir, I hurried to the exit. In the end, I could still win this stupid argument!"
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day4_dv_dj_concert:
    scene bg ext_stage_normal_day with dissolve
    play music music_list["went_fishing_caught_a_girl"] fadein 3
    play ambience ambience_camp_center_day fadein 3

    "At the very stage, I realized that the jig was up: I seemed to have lost the argument."
    show mt normal pioneer far at cleft
    show dv normal pioneer far at right
    with dissolve
    "Dvachevskaya, who was discussing something with Olga, noticed me and narrowed her eyes cunningly."
    hide mt with dissolve
    show dv normal pioneer at right with dissolve
    "Nodding her head, the squad leader waved her hand towards the stage and retired to the seats for the audience, while I moved straight to the redhead."
    show dv laugh pioneer at right with dissolve
    dv "Well, are you ready for a shameful defeat?"
    me "Always ready!"
    "I saluted, as any decent pioneer should be after such words."
    show dv smile pioneer at right with dissolve
    "Alisa chuckled."
    dv "Are you going to give up just like that? {w}Won't you try to trick me, ruin the concert, or at least get indignant, after all?"
    "I threw up my hands."
    me "Surrender? I felt like I'd already won."
    show dv surprise pioneer at right with dissolve
    dv "Huh?"
    "Dvachevskaya stared at me with incomprehension. {w}I giggled nastily."
    me "Redhead, you've already lost by agreeing to perform. I think as a consolation, I can do some dirty tricks that you ask me to do."
    "She finally started realizing that the game was rigged from the start."
    show dv angry pioneer at right with dissolve
    dv "You bastard! You thought it was so easy with me, didn't you?"
    show dv normal pioneer at right with dissolve
    "She was obviously frantically looking for a way to turn this situation in her favor."
    dv "Yes, I {w=1}was going to perform at that idiotic concert myself!"
    me "Yes, yes, of course. That's why you asked me out on a date instead this morning!"
    show dv angry pioneer at right with dissolve
    dv "That was a joke, cretin."
    dv "I don't go dating!"
    th "You'd think they call you often!"
    "But I didn't say it out loud, of course. My goal was to defeat her in a morally honest way."
    me "Just admit it: you're too gambler to continue to stick to your line when you're being offered a bet."
    show dv rage pioneer at right with dissolve
    dv "I'm not a gambler!"
    me "Prove it. I bet you can't?"
    play sound sfx_punch_medium
    with vpunch
    with flash_red
    "She kicked me hard on the knee, making me curl up with a hiss."
    dv "Don't joke with me."
    show dv normal pioneer at right with dissolve
    show dv normal pioneer far at right with dissolve
    hide dv with dissolve
    $ alt_pause(0.2)
    "Alisa spat out and, proudly tossing her head, retired to the stage."
    "Still grimacing from the pain in my knee, I trudged to the audience seats. Our small squad sat at the very end, yielding all the best positions to the kids and their relatives."
    show sl upset pioneer with dissolve
    sl "Semyon, did something happen?"
    "Slavya asked worriedly, noticing the painful expression on my face."
    me "It's okay. I'm trying to come to terms with the fact that I'll never be led by an adventure road again."
    stop music fadeout 5
    show us smile pioneer at fright with dissolve
    $ alt_pause(0.3)
    show us normal pioneer at fright with dissolve
    $ alt_pause(0.3)
    hide us with dissolve
    "Ulyana, who was sitting nearby, narrowed her eyes suspiciously, but lost interest in me almost instantly."
    show sl normal pioneer close at right with move
    "I sat down on the bench next to the activist."
    show sl dontlike pioneer close at right with dissolve
    play music music_7dl["unforgotten"] fadein 5
    $ volume(0.8, "music")
    sl "Have you seen Alisa?"
    me "Crossed paths recently."
    "I muttered, rubbing my knee."
    me "Why?"
    show sl sad pioneer close at right with dissolve
    sl "It's just that I'm afraid that if she goes to perform, it will end badly!"
    sl "After her morning joke, you can expect anything."
    me "What joke, Slavya? She didn't even know how to handle all that equipment."
    show sl normal pioneer close at right with dissolve
    sl "She knew."
    "Calmly said Slavya."
    sl "The radio room has the same amplifier as yesterday at the dances."
    show sl dontlike pioneer close at right with dissolve
    sl "One grandfather almost got sick!"
    "She added indignantly."
    me "She just didn't check the volume before turning on the music. {w}It's was a misinput."
    show sl upset pioneer close at right with dissolve
    sl "No, Semyon."
    "The girl shook her head."
    sl "You just don't know Alisa too well.{w} Sometimes I think doing nasty things is the meaning of her life."
    me "Just think - in the camp people sometimes change not for the better. Still, there is less control: parents are far away, teachers too, and here you are only for three weeks..."
    show sl serious pioneer close at right with dissolve
    sl "We've been in the same class since childhood."
    show sl upset pioneer close at right with dissolve
    $ alt_pause(0.2)
    sl "So no, she's always been like that. {w}She was and still is."
    sl "I'm not turning you against her, but..."
    th "But you do. {w}And you know that very well."
    me "Alisa is what she is. There won't be another."
    me "So please stop complaining about her to me. {w}Are you embarrassed to say it to her face?" 
    show sl sad pioneer close at right with dissolve
    stop music fadeout 5
    "Slavya lowered her eyes."
    $ volume(1.0, "music")
    sl "Sorry."
    hide sl with dissolve
    "At that, I decided that our conversation was over, and silently stared at the stage."
    th "Let's see what they will surprise us with..."
    play music music_list["your_bright_side"] fadein 5
    "One could only be surprised at how professionally Miku led the concert. The performances of the children left much to be desired."
    "I was already starting to nod off when the perky voice of the presenter brought me back to reality:"
    mi "And now Alisa Dvachevskaya, the first squad, is performing for you!"
    $ volume(0.7, "sound")
    play sound sfx_7dl["applause_someone"] fadein 1
    "A little perked up, I joined in the quiet applause."
    stop sound fadeout 3
    "Meanwhile, Alisa pulled a chair onto the stage and moved the microphone towards it. Miku set up the tripod of the second microphone, placing it at the level of the guitar."
    "It seemed that the redhead was absolutely up to the light, look at her or not - if she was nervous, then she did not show it with any movement or look. I began to seriously envy her."
    th "Is she really that used to performing in public?"
    "The preparations were completed, and Miku hurried off the stage. Alisa, however, bent over the strings, clutching a plectrum in her hand."
    stop music fadeout 1
    scene cg d4_dv_concert_7dl with dissolve2
    play music "<from 45>" + music_7dl["piknik"] fadein 3
    "I recognized the melody from the very first chords. And involuntarily smiled, as if I had met an old and good friend in the subway car."
    th "Could I have expected anything else from Alisa?"
    dv "{i}Night rustles overhead like a vampire's black cloak{/i}"
    dv "{i}We're passing by - these games are not for us{/i}"
    dv "{i}Let someone else fight in the arms of darkness{/i}"
    dv "{i}We are free and clean, we pass by{/i}"
    "Some of the parents in front of me shook their heads in displeasure and whispered softly, but the majority watched the girl's performance with interest. Olga, walking along the rows, anxiously watched the reaction of the audience."
    th "Worried about getting kicked for letting unauthorized music on stage?"
    th "But still she let Alisa perform. And that's about something, yes."
    "However, I did not notice much discontent among adults. It was not surprising - the redhead played masterfully."
    th "She sings pretty well too. I didn't know she had such a strong voice!"
    dv "{i}Here I am, haha, it hurts my ears{/i}"
    dv "{i}Wouldn't mind laughing{/i}"
    dv "{i}Just as long as there's light in the sky{/i}"
    dv "{i}Until night falls{/i}"
    play sound3 sfx_concert_applause fadein 1
    stop music fadeout 3
    scene bg ext_stage_normal_day with dissolve

    "Having finished playing, Alisa stood up and gave a short nod to the audience. They answered her with thunderous applause - including me."
    th "She's good, after all!"
    th "This music suits her so well..."
    stop sound fadeout 3
    "But still, something inside did not allow me to fully enjoy the performance of the redhead. I seemed to feel something false in it."
    $ volume(1.0, "sound")
    "Albeit well, albeit talented, but she played absolutely not from the heart. There was no life in it, which I so expected to hear."
    th "Maybe she wanted to do something else, but Olga wouldn't let her?"
    th "But she obviously didn't learn «Picnic» at a music school!"
    play music music_7dl["areyouabully"] fadein 3
    "Loud screams from somewhere behind me pulled me out of my thoughts."
    show us dontlike sport at right with dissolve
    voice "Psychotic fool! Maniac!"
    voice "My mother will…"
    show us angry sport at right
    hide us with moveoutright
    "Behind the benches were boys about Ulyanka's age. She herself was running somewhere towards the library."
    "I unceremoniously got up from my seat and walked towards them."
    show sl scared pioneer close at right with dissolve
    sl "Semyon, stop!"
    "Slavya tried to grab my hand. The girl looked frightened."
    sl "Don't ruin the concert!"
    me "What if something happened to Ulyana? Why the hell would I care about a concert?"
    show sl dontlike pioneer close at right with dissolve
    sl "Ulyana was there?"
    show sl dontlike pioneer at right with dissolve
    "Frowning, Slavya got up after me. Trying not to draw attention to ourselves (as far as possible, given the unceasing swearing right behind the audience seats), we moved to the scene."
    voice "It hurts!"
    "One of the boys was whimpering, sitting on the grass and holding his nose with his hand. Blood oozed in thin streams through dirty fingers."
    "Another boy, curly-haired and red-eyed, fussed beside him, trying to lift him, but the victim stubbornly kicked back, wriggling and throwing his comrade's hands off his shoulders."
    show sl angry pioneer at right with dissolve
    sl "What happened here?"
    "Two boys, standing a little further away, looked at the activist unkindly, apparently deciding to remain silent to the last. I could not stand it:"
    me "What did you do to Ulyana?!" with vpunch
    "My shout made all four turn around."
    show dn dontlike pioneer with dissolve
    dn "Nothing. You shouldn't get involved…"
    voice "It's all her!"
    "The boy with the broken nose sobbed."
    voice "She hit me! Reptile!"
    voice "I didn't do anything to her!"
    show ka normal pioneer at left with dissolve
    $ meet('ka', "Squad leader")
    ka "There you are! Why are you again…"
    show ka angry pioneer at left with dissolve
    "The girl who came up to us stopped abruptly when she saw the boy sitting on the ground."
    ka "Anton, are you getting into fights again?"
    me "Is that their squad leader?"
    "I quietly asked Slavya. The girl nodded, pursing her lips."
    voice "She hit me first! It's her fault!"
    show mt angry pioneer close at fleft with dissolve
    mt "You two - march to your seats."
    "There was a hiss right in my ear. Olga was furious."
    me "But Ulyana…"
    mt "I'll deal with Ulyana myself. Have you forgotten where you should sit?"
    hide dn
    hide ka
    hide mt
    with dissolve
    stop music fadeout 8
    show sl sad pioneer at center with dissolve
    "Slavya sighed heavily and took my hand, almost dragging me back to the audience benches by force."
    me "I don't trust this kid!"
    "I grumbled, trying to rein in my anger."
    me "It's unlikely that Ulyana would attack just like that!"
    play music music_7dl["fyrsta"] fadein 3
    show sl normal pioneer at center with dissolve
    sl "She wouldn't."
    "Slavya answered calmly."
    sl "But don't worry about her - she won't let herself be hurt."
    me "Yeah, who would have doubted."
    hide sl with dissolve
    "And I had to look again at the inept dances of the children from the younger squad."
    th "How I wish it wasn't Slavya, but Alisa. She certainly wouldn't be idle and hide her head in the sand!"
    dreamgirl "Do you think she would have finished off the boy?"
    th "Who knows? Maybe she would have."
    "I was disgusted by my own inaction. And even more disgusting - to realize that someone else in my place would not be confused."
    th "Especially if that someone is Alisa."
    th "By the way, where is she? Why didn't she return to the audience after the performance?"
    "Somehow belatedly, I thought that she could well be sitting behind the stage, but I didn’t dare to go and check. You never know - they will notice, they will start asking questions... "
    th "And I don't care: they scold them, they don't scold them. But I don't want to set others up."
    "So I stared blankly at the stage, praying that this orgy would end soon."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade3
    return

label alt_day4_dv_dj_dinner:
    scene bg int_dining_hall_people_sunset_pp_7dl with dissolve
    play ambience ambience_dining_hall_full fadein 1
    play music music_list["so_good_to_be_careless"] fadein 3
    "I was one of the first to slip into the dining room, without waiting for Alisa. After all, it would be a much more gentlemanly act to take her place, rather than stomp at the doors of the music club while she puts the guitar in place."
    th "Besides, tagging along right now is not a good idea. You never know when she needs to go to the infirmary?"
    th "And knowing Dvachevskaya, she won't tell about her illness even at gunpoint. Why embarrass her once again?"
    "I kept a close eye on the entrance to the dining room, waiting for the girl. Every creak of the front door made me shudder involuntarily."
    dreamgirl "You're just some kind of maniac."
    dreamgirl "You could humanly warn her after the concert that you will reserve a place for her, but no - you will sit on pins and needles and stare at the door!"
    th "Yeah, make her laugh at me?"
    th "Like, look, what a knight, scared away all the starving children for me?"
    th "By the way, here they are..."
    show el normal pioneer at left
    show sh normal pioneer at right
    with dissolve
    el "Can we sit here?"
    me "No. Taken."
    show el sad pioneer at left
    show sh upset pioneer at right
    with dissolve
    hide el
    hide sh
    with dissolve
    "The cyberneticists looked at each other in bewilderment and trudged off to look for another table. An inner voice giggled disgustingly."
    dreamgirl "It'll be hilarious if she doesn't sit here."
    dreamgirl "Or do you think knocking your kneecap out is such an interesting form of flirting?"
    "I was vexedly thinking about where to send my schizophrenia this time, I did not notice how someone's tray crashed in front of me."
    show dv normal pioneer close with dissolve
    dv "Well, gambler, ready for my wish?"
    $ alt_pause(0.5)
    window hide
    with flash_pink
    window auto
    "Heart joyfully jumped in the chest, as if doing a somersault."
    th "She's not mad at me after all!"
    me "Whatever the lovely lady desires."
    "I smiled broadly, feeling like a cross between a feeble-minded child and a March cat."
    show dv grin pioneer close with dissolve
    "Alisa, who had already filled her mouth, looked up thoughtfully somewhere."
    dv "I hfavfent cfame up wif anyfin yet."
    "She mumbled."
    "In a familiar environment, I would probably grimaced in disgust, but now Dvachevskaya evoked in me only a feeling of some kind of shameful tenderness."
    dreamgirl "What a pig, just lovely!"
    th "You just don't understand!"
    me "Well, I can wait."
    show dv normal pioneer close with dissolve
    "The girl silently devoured her food."
    "I was wondering how I could persuade her to some kind of joint activity this beautiful evening."
    th "She kind of promised to show me some place in the camp this morning, but something tells me it's best not to remind me."
    th "Damn it made me joke about a date!"
    me "Do camp gigs always suck, or is it just on Parent's Day?"
    "I asked to say at least something."
    show dv laugh pioneer close with dissolve
    dv "Always."
    "Alisa suddenly chuckled."
    dv "Didn't you like my performance?"
    th "Dvachevskaya asking for compliments? This is something new!"
    me "Why? All of Miku's performances were amazing!"
    me "Well, one more number was quite… passable."
    show dv think pioneer close with dissolve
    me "The ears did not curl up into a tube - and thanks for that."

    show dv surprise pioneer close with dissolve
    $ alt_pause(0.3)
    show dv angry pioneer close with dissolve
    $ alt_pause(0.3)
    show dv rage pioneer close with dissolve
    $ alt_pause(0.3)

    "Watching her face change was pure pleasure!"
    me "I'm kidding, redhead. You really do sing well."
    show dv normal pioneer close with dissolve
    me "Still, this event was so much of a clown fiesta that a few good songs won't save it."
    me "If the most vivid memory of a concert is a fight, then what was this concert for at all? It would be better to arrange fights without rules, take bets..."
    show dv surprise pioneer close with dissolve
    dv "What fight?"
    me "Ulyana broke some boy's nose and ran away. {w=1}And now she's probably on the run somewhere in the Caribbean."
    show dv dontlike pioneer close with dissolve
    "Alisa looked at me like I was a complete idiot, furrowing her brows angrily."
    dv "Are you saying she missed dinner?"
    "I threw up my hands helplessly."
    me "Well, actually, I wanted to catch up with her, but it was too late. You yourself know very well that she runs fast."
    show dv dontlike pioneer with dissolve
    dv "We need to find her now!"
    "Exclaimed Alisa, rising from the table. I jumped up hastily, grabbing my tray."
    me "Do you think something will happen to her?"
    dv "Yes. For example, she'll be hungry again by nightfall, and we'll have to break into the canteen again!"
    hide dv with moveoutright
    "The girl hissed and almost ran to carry her tray."
    th "Well, you wanted an evening with a girl - get it and sign it."
    th "And the fact that we spend it looking for another girl is the little things in life!"
    th "But without fish, as they say..."
    "Smiling mirthlessly, I went out onto the porch."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day4_dv_dj_us_search:
    scene bg ext_dining_hall_near_sunset with fade3
    play music music_list["reflection_on_water"] fadein 3
    play ambience ambience_camp_center_evening fadein 1
    show dv normal pioneer with dissolve
    "Alisa rushed out of the dining room a minute after me, clutching something in her hand."
    me "Stolen cutlets?"
    "I joked. The girl chuckled."
    show dv laugh pioneer with dissolve
    dv "Yes, and there was no need to steal - they gave it away themselves. The little ones were eating candy all day today, and now they are sitting there, picking at the plates."
    "She proudly lifted two cutlets sandwiched between slices of bread."
    th "Crazy Soviet hamburger?"
    show dv normal pioneer with dissolve
    dv "Let's go before she starves to death!"
    me "What about the radio?"
    show dv concent pioneer with dissolve
    "My question made Alisa wince."
    dv "To hell with it, with this radio! We lived well without it for almost a week..."
    me "No, that's not how things are done."
    "I crossed my arms over my chest, leaning on the dining room porch with my shoulder."
    me "Now we'll put music on the air, and then we'll go wherever we want. Nothing bad will happen to Ulyana if she gets her cutlets ten minutes late."
    show dv angry pioneer with dissolve
    dv "That's what you think!"
    "Alisa boiled up in a second."
    show dv guilty pioneer with dissolve
    dv "If Ulyana's friends find her earlier than us, we won't catch them until nightfall!"
    "I just shrugged."
    me "Then leave food for her at your cabin. Is it that hard?"
    show dv angry pioneer with dissolve
    $ alt_pause(0.3)
    show dv sad pioneer with dissolve
    "Dvachevskaya gave me a stern look, but quickly averted her eyes to the side."
    dv "I won't rest until I know what that boy did to her, you know?"
    th "Or someone is just looking for an excuse not to hang out in the radio room all evening."
    me "Let's turn on the music and let's go. Yeah?"
    me "I don't want you to get screwed for shirking work. Who would be better off if you both got locked up as punishment?"
    if alt_day3_duty:
        me "Or even worse - forced to peel potatoes in the kitchen?"
    if herc:
        me "Let's go already! The sooner we start, the sooner we'll be free."
        "I grabbed Alisa by the hand and dragged her by force towards the clubs."
    else:
        me "So now we move at a pace to fulfill our pioneer duty to the camp. Forward!"
        hide dv with dissolve
    "I moved towards the clubs without even looking back - as if I knew that Alisa would already follow me."
    stop ambience fadeout 3
    scene bg int_clubs_male_sunset with blinds_l
    "Oddly enough cybernetics weren't in their abode."
    th "Did they get sick or what?"
    dreamgirl "Or they remembered that they were actually sexually mature males and started peeping at the girls on the beach."
    th "Did you see them? What girls?"
    dreamgirl "Blonde, unsociable, hafu - even your dear squad leader!"
    dreamgirl "Not everyone loves the thrill as much as you."
    show dv normal pioneer with dissolve
    th "I wouldn't say Alisa is such a thrill."
    if loki:
        th "Seen better ones…"
    dreamgirl "That's only until she kicks you above your knee…"
    hide dv with moveoutright
    "Alisa carefully put the sandwich on the table, removed the player from the charger and ran to the radio room. She fumbled there for a minute - I did not follow her - and music hummed peacefully over the roof."
    show dv normal pioneer at right with moveinright
    dv "Three hours of music, you say?"
    "Alisa asked, looking out of the closet. I nodded, and the girl breathed a sigh of relief, hurrying to the table for provisions for the petty one."
    show dv normal pioneer far at cright with move
    dv "We'll have enough time then..."
    dv "What's that?"
    show dv smile pioneer far at cright with dissolve
    "She bent down, looking somewhere under the table. When she surfaced back, her face shone with contentment."
    dv "Look what I found here!"
    "A heavy package of gingerbreads fell on the table next to the hamburger. I whistled."
    th "I knew they had a boiler here for a reason!"
    th "It's really not good to drink tea without anything. I wouldn't be surprised if they had a whole theater buffet here at the beginning of their shift!"
    dv "Now Ulyana will definitely not fall asleep hungry."
    "No matter how pleasant it was to find something edible in the bins of cybernetics, it was difficult to drown out the thin squeak of conscience somewhere above the ear:"
    th "It's their gingerbreads!"
    th "We won't steal other people's food, will we?"
    "But Alisa apparently decided that we would, busily arranging cutlets in one hand and a bag in the other."
    me "Listen, I understand that you want to feed Ulyana, but don't you think it's too much?"
    show dv grin pioneer with dissolve
    "Dvachevskaya just snorted."
    dv "Yeh, they throw tea parties once a week with the whole squad. More precisely, almost everyone - they don't even bother with inviting those who they don't like, fucking upstarts!"
    dv "Ulyanka and I are garbage for them, you see. It's a pity to spend extra sweets on such!"
    show dv smile pioneer with dissolve
    "She smiled mischievously when she saw my frown."
    dv "Apparently, you didn't receive an invitation either? They're going to gather here today, after lights out."
    th "Well, that makes a big difference."
    th "If gingerbread is already designed for our squad... Then we're part of the squad too, right?"
    me "Then let's go faster before they find it missing!"
    show dv soft_smile pioneer with dissolve
    $ alt_pause(0.5)
    show dv smile pioneer with dissolve
    $ alt_pause(0.2)
    hide dv with moveoutleft
    stop music fadeout 3
    "Cunningly winking at me, Alisa was the first to jump out the door."
    $ renpy.show("bg ext_camp_entrance_sunset_7dl", what = Dawn("bg ext_camp_entrance_sunset_7dl"))
    show dv normal pioneer
    with dissolve
    play ambience ambience_forest_night fadein 1
    play music music_list["goodbye_home_shores"] fadein 3
    "She led me to the gates of the camp."
    me "And where are you going to look for Ulyana?"
    dv "In the treehouse. She always sits there when she's feeling down and no one is around."
    "Alisa seemed to straighten herself up in mid-sentence."
    show dv angry pioneer with dissolve
    dv "Just try and talk about that to Hat!"
    "I rolled my eyes."
    me "Dvachevskaya, who do you take me for?"
    if herc:
        me "By surrendering comrades, we endanger my own neck. Do I need it?"
        me "That's what I thought."
        th "And considering the fact that redheads can come up with some terrible revenge…"
    elif loki:
        me "So me and you steal gingerbreads together, scare grandfathers with loud noises, sabotage quiet hour, and you want to suspect me of snitching?"
        me "Well, well."
    else:
        me "In my life I would never have thought to pawn you or Ulyana. You will beat me later!"
    show dv smile pioneer with dissolve
    dv "I'm watching you!"
    "Alisa narrowed her eyes suspiciously. Her tone, however, was quite friendly."
    show bg ext_backroad_sunset_7dl with joff_r
    "We didn't go far from the camp, no more than a kilometer along the path along the fence, giving a sharp turn near the river."
    me "Did Ulyana and her friends build this house?"
    show dv normal pioneer with dissolve
    dv "It's been here for a long time. Ever since the time when the Hat rode was as a pioneer."
    th "Wow!"
    dreamgirl "Didn't you know that your squad leader was also a pioneer?"
    dreamgirl "You seem a lot younger than you think."
    th "Oh no! It's just so weird to feel like this place has its own past and its own mysteries..."
    show dv concent pioneer with dissolve
    dv "I don't know exactly who built it - I was in the junior squad then, and the elders turned their noses at us."
    dv "At first, everyone was terribly interested in what they were doing there, but then somehow it became all the same, to be honest."
    dv "There were rumors on every shift that there was a whole tree palace in the forest, but no one could ever find it."
    show dv normal pioneer with vpunch
    "Alisa braked sharply."
    dv "It's over there. See the cross?"
    "Indeed, there was a barely noticeable mark on the bark of a huge southern pine, well covered with a green down of moss. It was simply impossible to notice it by chance."
    dv "There are steps on the side of the trees. Climb forward!"
    me "Why…"
    dreamgirl "Because, dumbass! She's in a skirt. Embarassed."
    dreamgirl "Or do you want a rejuvenating spa treatment in the form of washing with the blood of virgins?"
    "I was jolted."
    th "Perhaps I will refrain."
    "Alisa unceremoniously put the cutlets in a bag with gingerbread, tied it in a knot and clamped it in her teeth, after which she again nodded impatiently towards the tree."
    hide dv with dissolve
    "And I climbed up a pine tree, carefully checking each plank driven into the trunk for strength. Soon I noticed a green camouflage net stretched between thick branches."
    "Whoever arranged this secret place - really did a good job!"
    $ renpy.show("bg ext_tree_house_sunset_7dl", what = Dawn("bg ext_tree_house_sunset_7dl"))
    with dissolve
    "I climbed onto the bulky flooring - and how did no one notice it? - and offered my hand to Alisa."
    show dv guilty pioneer with dissolve
    stop music fadeout 3
    dv "It's too quiet."
    "She muttered as she straightened her skirt."
    dv "Did they get here earlier?"
    show dv guilty pioneer far with dissolve
    "The redhead peered through the makeshift window, cupping her hands over her eyes, then smirked."
    show dv smile pioneer with dissolve
    dv "Of course she's sleeping!"
    "I involuntarily laughed."
    me "Did she really run so much during the day?"
    dv "No. That's how she fights hunger."
    dv "It doesn't always work, though."
    "Cutting down on all fours, Alisa climbed into the house through a small door half the height of a child's height. I wanted to look away ..."
    th "But it's not my fault! They looked there themselves!"
    "Taking a deep breath and mentally counting to five, I followed."
    scene bg int_tree_house_sunset_7dl:
        zoom 1.3
    show us upset sport at cright
    with dissolve
    play music music_7dl["fatest"] fadein 3
    "The little one was curled up in a pile of some rags in the corner, as if she had made a nest out of it. It looked like old blankets - probably stolen from a warehouse."
    dv "Ulyana?"
    us "Huh?"
    "The girl answered sleepily."
    me "Get up, we brought you food!"
    me "Supper in bed, so to speak."
    show dv normal pioneer at cleft with dissolve
    "Alisa had already sat down on the floor and was untying the package. Ulyana perked up noticeably."
    show us surp2 sport at cright with dspr
    us "Well, well! I already thought that I would have to climb into the canteen again at night!"
    show us smile sport at cright with dissolve
    "She happily grabbed the cutlets extended by Alisa and began to chew. I, while nobody was looking, pulled one gingerbread out of the bag - the small one did not suffer from a lack of appetite, and any conscript soldier would envy her speed of eating."
    dv "So what's the whole escape circus about?"
    "Alisa asked when Ulyana finished with the cutlets and began to lick her dirty fingers. The little one grimaced."
    us "Well, Antokha again..."
    us "You know. Sore subject."
    show dv sad pioneer with dissolve
    "Dvachevskaya frowned."
    dv "Did he do something to him?"
    dv "How many times I asked you: don't ask for trouble! If anything - call me, I'll tell him a couple affectionate words..."
    th "What are they going on about?"
    "I looked puzzled at one and then the other, trying to understand what kind of secrets they have here. But the girls seem to have completely forgotten about my existence."
    show us sad sport at cright with dissolve
    us "You wouldn't have succeeded."
    "Ulyana shook her head."
    us "Today he complained to his mother that he had to be in the same squad with... {w=1}{b}them{/b}, who disgust him, you see. And she promised that she would resolve this issue."
    us "That Alka will no longer be given a ticket to a good camp."
    show dv angry pioneer at cleft with dissolve
    dv "What a fucking asshole!"
    "Alisa strained through her teeth. Whatever Ulyana was talking about infuriated the redhead in earnest."
    dv "I've seen a lot of them. They were just not ready to give a damn about us."
    dv "{i}There is nothing to feed our own, but these people eat at our expense!{/i}"
    "Alisa mimicked someone."
    "I looked at her stupidly and had no idea what to do. Obviously they were not going to explain anything to me."
    show dv rage pioneer at cleft with dissolve
    dv "But getting into a fight right in front of his mother is no brainer at all!"
    "Suddenly Dvachevskaya became stern."
    dv "Who would stand up for you here, huh? {w=1}You're all to blame for them!"
    show dv normal pioneer at cleft with dissolve
    dv "You should have waited, fool!"
    show us shy sport at cright with dissolve
    "Ulyana blushed deeply, staring somewhere out the window."
    us "I didn't mean to hit him. It was... accidental."
    us "He's been teasing Danya and me for a long time, but today he's crossed all the lines."
    $ meet('dn',"Danya")
    show us angry sport at cright with dissolve
    "The girl glared angrily at me."
    us "I'm tired of listening to this nonsense!"
    "I began to look at the wooden ceiling with interest, pretending that I had nothing to do with what was happening."
    dn "Ulya! Are you there?"
    show us smile sport far at cright with dissolve
    "Hearing the boy's scream, Ulyana jumped up. The anger from her face evaporated in a second."
    us "Okay. Thanks for the bread and salt, but I still have things to do."
    dv "Blow out of here already! Get Antokha out of your head, I'll deal with him again tomorrow, understand?"
    hide us with dissolve
    "The little one nodded and crawled to the exit of the house. {w} With a sad look, I followed the bag of gingerbread that Ulyana took with her when she got out."
    show dv normal pioneer at cleft with dissolve
    "Alisa and I looked at each other."
    me "And what was…"
    dv "Forget it."
    "Dvachevskaya waved it off."
    dv "Let's go to the beach. I want to clear my head a bit."
    hide dv with dissolve
    scene
    $ renpy.show("bg ext_tree_house_sunset_7dl", what = Dawn("bg ext_tree_house_sunset_7dl"))
    with dissolve
    "I obediently got out of the house after her - what else could I do?"
    show anim_grain
    th "And she leads me somewhere again, without even asking if I want to. Like a dog on a leash: she twitches a little to the side, so you can immediately pull, squeezing his neck and cutting off oxygen."
    th "Here's a dog trudging after his mistress, blindly and helplessly. Afraid of falling behind and getting lost. Afraid of being left without oxygen."
    th "But I really want this. I want to be with her, listen to all her hurtful jokes about me and get punched in the face for trying to answer her something."
    th "And when did I become such a masochist?"
    if herc:
        th "Professional deformation after the military?"
    elif loki:
        th "Stockholm syndrome after relationship with Ksana?"
    else:
        th "Always have been, probably."
    th "What about Alisa? Why does she need this?"
    th "Okay, this morning - I helped her sort out the player. After lunch, I subtly asked for help with the cleaning. And now?"
    th "What's her point in letting some bum have his fun?"
    "Perhaps she was just bored. I did not notice that she had friends in the camp besides Ulyana, but she was always running around in the company of her mutts from the second squad."
    th "So, I ended up in Dvachevskaya's entourage on a residual basis? Well, well, an incredible achievement!"
    th "Being slightly better than cybernetic nerds is enough to not look completely hopeless. It's good that the background here is favorable for at least some integration into society."
    th "Otherwise I would have to...{w=0.6}{nw}"
    hide anim_grain with dspr
    dv "Careful, idiot!" with hpunch
    "I nearly fell off the tree from Alisa's sharp cry. The girl was already standing on the ground, arms crossed over her chest."
    me "Well, why yell like that?"
    dv "And who's to blame for not looking at what's under your feet?"
    "I absentmindedly noted that I almost put my foot past the step."
    $ renpy.show("bg ext_backroad_sunset_7dl", what = Dawn("bg ext_backroad_sunset_7dl"))
    with dissolve
    play sound sfx_uliana_jumps_down
    extend " However, at such a height, this oversight would have been fraught with only a couple of scratches, so I calmly jumped onto the grass."
    dreamgirl "Park-o-o-o-ur!"
    dreamgirl "Now have you impressed the girl enough to feel worthy of her?"
    "Not waiting for me, Alisa rushed somewhere along the path. I stamped my feet, wondering if it would be better for me to leave, but something inexorably pulled me along."
    th "What have I become?"
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day4_dv_dj_date_on_the_beach:
    scene bg ext_un_hideout_night_7dl with fade2
    play ambience ambience_lake_shore_night fadein 2
    play music "<to 77.0>" + music_7dl["redemption"] fadein 3
    "The sky was almost black by the time we reached the water. {w}The pleasant cool breeze from the direction of the river was really soothing, and for a second it even seemed to me that all my far-fetched worries about Alisa were simply ridiculous and inappropriate."
    th "After all, what's the difference, why and why are we here now?"
    th "The only thing that matters is that Alisa is with me. Nearby."
    th "And she — hopefully! — needs it as much as I do."
    show dv closed_eyes pioneer close at cleft with fade3
    "Alisa sat down on the log and closed her eyes. She rubbed her forehead with her left hand, grimacing tiredly."
    "I sat down next to her - not too close, so as not to embarrass her."
    me "Do you have a lighter with you?"
    dv "Why do you need it?"
    me "We should make a fire before we get eaten by mosquitoes."
    show dv sad pioneer close at cleft with dissolve
    "The girl opened her eyes, looking somewhere at the horizon."
    dv "That's true. We only need to get some branches…"
    hide dv with dissolve
    "For about ten minutes we crawled along the grass along the wild beach, collecting everything that in the dark could be mistaken for dry wood. The silence was broken only by a rare curses from Alisa whenever she stumbled upon the roots of a bush sticking out of the sand."
    th "I wish good parents would put some marshmallows for me..."
    th "And what kind of parents are they anyway?"
    "In the afternoon, I didn't have time to really think about this question, nor the strength to wonder why someone handed me my own backpack. And there was no doubt that it was mine."
    "I always went out of the house with it, but on the bus I woke up without him. And before the bus..."
    show prologue_dream with dissolve
    "Frozen in place, I strained my memory, trying to pick out at least something from what happened before awakening at the gates of the camp, but my brain seemed to be gently covered with fog every time the events of the last day in the familiar world reached their borders."
    th "But I was definitely going somewhere, right?"
    th "If waking up on the bus wasn't a surprise to me, then I definitely was."
    hide prologue_dream with vpunch
    stop music fadeout 3
    dv "Did you fall sleep there?"
    me "Coming!"
    scene cg d7_dv with dissolve
    play music music_7dl["breath_again"] fadein 3
    "We returned to the log that Alisa had chosen, and began to build our simple fire in front of it. I glanced furtively at the girl: she was still out of sorts, but her determination to kill everyone around her clearly lessened."
    "Only after making sure that the dry grass smolders evenly and is not going to go out from the slightest breath of wind, I landed on a log with a sense of accomplishment - this time a little closer to Alisa."
    "Just a couple of centimeters, but still..."
    dv "Nothing changes in this camp. It gets weepier and sadder every year."
    "Alisa said, thoughtlessly looking into the fire."
    me "How long have you been coming here?"
    dv "Consider that for all of my conscious life. I've been here when the Hat was in a senior squad, can you imagine?"
    "It was hard to imagine, even though I honestly tried."
    me "And what was she like?"
    dv "Completely different.{w} Very reminiscent of Ulyana."
    dv "Her and Mirya, her brother, were the stuff of legends. I was in the 4th squad back then, a little older than a fry, but still a brat. {w=1}We all dreamed of being like that when we grew up."
    dv "That we will also hooligan to our heart's content, but they will still love us and not punish us for anything. {w}And she and Mirya sometimes arranged such things that I am still amazed: how were they not expelled from the camp then?"
    me "What did she do?"
    "I asked with interest. It was never superfluous to get dirt on your favorite squad leader!"
    dv "Broken our camp's exemplary check, for example. The glued bench joke is old and quite innocent, but when the asses of the party's bigwigs get down on that bench..."
    "Alisa fell silent expressively."
    dv "As you can imagine, our camp has not yet been recognized as a model one."
    "I myself did not notice how I smiled: after all, people were never born adults and boring."
    me "For some reason, all my life I thought that leaders like Slavya become squad leaders."
    "Having stirred the fire with a long branch, Alisa grunted."
    dv "Seriously? And how do you imagine it?"
    dv "Do you think anyone would listen to this upstart?"
    me "I don't know. She can be quite strict sometimes."
    dv "So what, does this strictness make you do what she wants you to do?"
    dv "When she starts talking in front of me, all I want is for her to shut up and never touch me in her life."
    me "Have you been like this since school?"
    $ renpy.show("bg ext_un_hideout_night_7dl", what = Desat("bg ext_un_hideout_night_7dl"))
    show dv dontlike pioneer close at cleft
    with dissolve
    "The hostile look in my address spoke very eloquently about the fact that this topic should not have been brought up."
    dv "So you've had time to gossip?"
    "Alisa asked caustically."
    dv "I wonder what she told you? Not much, I suppose, if you're still willing to talk to me."
    me "We didn't gossip!"
    "I boiled."
    me "She came in and complained about how you misbehave, and I..."
    show dv angry pioneer close at cleft with dissolve
    dv "And you?"
    "Her eyes narrowed angrily, and a cold smile froze on her lips."
    me "Told her to fuck off. I don't care what others think of you."
    dv "That's how it is."
    "Alisa drawled. On her face, I clearly saw doubt."
    dv "So you're not prejudiced?"
    me "Absolutely not inclined."
    show dv normal pioneer close at cleft with dissolve
    $ volume(0, "music")
    dv "I'm an orphan."
    show dv sad pioneer close at cleft with dissolve
    $ alt_pause(0.3)
    show dv closed_eyes pioneer close at cleft with dissolve
    $ alt_pause(0.3)
    show dv sad pioneer close at cleft with dissolve
    $ alt_pause(0.5)
    show dv normal pioneer close at cleft with dissolve
    "She blurted it out so abruptly that I was taken aback."
    $ volume(1.0, "music")
    th "So that's what it all means!"
    th "That's exactly what Syroezhkin was talking about this morning!"
    th "I could have guessed before - from snippets of phrases, from habits..."
    dreamgirl "Do you think in prejudices?"
    th "Sometimes it's inevitable."
    th "But that doesn't mean I do care!"
    "Here, of course, I was kind of lying. I couldn't helpbut worry."
    show dv dontlike pioneer close at cleft with dissolve
    dv "Well, why are you silent? You won't even feel sorry for me?"
    me "Is that what you want?"
    show dv tired pioneer close at cleft with dissolve
    "Alisa shrugged."
    dv "No. There are enough compassionate people without you."
    dv "And what's there to regret - I've been living in a foster family for almost nine years."
    show dv sad_smile pioneer close at cleft with dissolve
    dv "A lot of people were less lucky."
    show dv normal pioneer close at cleft with dissolve
    dv "I ended up in the hospital back then, with a concussion. And my people took me right out of the ward - they hoped, apparently, that I was re-educated there."
    dv "But old habits can't be erased, after all, I grew up in an environment that we usually call unfavorable from birth. {w}So don't expect me to apologize for being the way I am."
    me "And you think I'm going to treat you differently now?"
    "Now it's my turn to snort."
    me "I hang out with you because you're never boring. Because when you're around, I feel like I still want to live."
    me "I don't care about your past, Alisa, but you yourself."
    show dv dontlike pioneer close at cleft with dissolve
    dv "Really?"
    "The girl arched an eyebrow."
    show dv angry pioneer close at cleft with dissolve
    dv "I don't advise you to use such words. {w=1}You don't know me at all."
    th "Is she… scared?"
    "It was very clear. A person who has not had anyone close for a very long time, who has literally grown together with the idea that in this world he is alone against everyone, will never believe in empty chatter, even the most sincere one in the world."
    th "Is that why she told me everything?"
    th "So that if I decide to leave, I do it right away, without letting it get attached to me so that it hurts."
    me "But I would like to know everything you have to tell me."
    show dv smile pioneer close at cleft with dissolve
    dv "From such a statement of the question, all thoughts have disappeared from my head."
    "The girl chuckled."
    scene cg d7_dv with dissolve
    th "Plays with me. Taunts me."
    th "Waiting for a trick, a joke. An uncomfortable question, for which she will have every right to spit in my direction and never speak to me in her life."
    th "Just to get rid of this paranoid waiting once and for all!"
    me "Then tell me about the camp. What was it like before?"
    dv "Yes, the same, perhaps. Except that the grass was greener and the sun shone brighter."
    dv "I also thought it was only going to get more and more fun. {w}You know, I've always hated those stupid relay races and all the clowning that little kids are forced to do."
    dv "The senior squads are exempt from this. At least that's how it is in this camp."
    dv "They used to do such things here - you will laugh. And this year they recruited a whole squad of brats, as if on purpose!"
    "Alisa spat into the sand."
    dv "I remember when Mirya was a pioneer here, on the last night of his shift, he hung a bucket of water over Uncle Borya's house."
    me "Was that his last shift at camp?"
    dv "If only!"
    dv "That day Uncle Borya overslept, and they sent to wake him up... {w}guess who?"
    me "Could it be Mirya himself?"
    "The redhead laughed."
    dv "If only! The Hat, in person."
    dv "The scream was such that it's hard to imagine a better wake-up call. {w=1}Mirya then hid from her with the girls in the house. {w}Under my bed."
    "I wiped tears from my eyes from laughter."
    th "And I thought we had a madhouse on this shift!"
    dv "Then I was already in the fourth squad, and a year before that, when I was eight, there was such a scandal..."
    dv "Some couple from the second squad fled into the forest at night, right after lights out. They returned by dawn, and the gates were closed for the night. Well, they climbed over the fence."
    dv "And that girl was clumsy, she ran into a pin while she was climbing. Not much, they didn't even take her to the hospital - but she ate standing up in the canteen for the next two days."
    dv "The whole camp then teased her: 'Irka - hole in the ass.' Then she decided to run away from the camp - she could not stand the shame. At night she knitted a sheet and a blanket cover, climbed out the window... "
    $ renpy.show("bg ext_un_hideout_night_7dl", what = Desat("bg ext_un_hideout_night_7dl"))
    show dv laugh pioneer close at cleft
    with dissolve
    me "Wait a minute, what sheets?"
    "I interrupted Alisa."
    stop music fadeout 1
    me "All the houses here are one-story! And there are no pins on the fence."
    $ volume(0.6, "music")
    play music "<from 15.0>" + music_7dl["time_lapse"] fadein 5
    show dv sad pioneer close at cleft with dissolve
    "The girl broke off, and her eyebrows crawled to the bridge of her nose."
    dv "No, I exactly remember..."
    dv "I used to go with children from the orphanage!"
    me "Weren't you adopted at eight?"
    "Alisa shrugged her shoulders in annoyance."
    show dv think pioneer close at cleft with dissolve
    dv "At eight. Wait, that was at..."
    "She opened her mouth, but then closed it again."
    show dv angry pioneer close at cleft with dissolve
    dv "What difference does it make when that was?"
    "She blurted out in annoyance."
    dv "A hundred years has already passed, I don't remember!"
    show dv angry pioneer at cright with move
    "Rising sharply from the log, she began to furiously cover our almost burned-out fire with sand."
    show dv angry pioneer at center with dissolve
    dv "It's time to go to the camp. The music is already over, I suppose."
    th "What's wrong with her?"
    dreamgirl "And Viola warned you in the morning..."
    th "Okay, if that's the case. But it's still weird."
    th "Doesn't like to remember things related to the orphanage?"
    dreamgirl "Or doesn't like being caught on something."
    th "On what?"
    $ volume(1.0, "music")
    stop music fadeout 3
    stop ambience fadeout 3
    $ renpy.show("bg ext_path_night", what = Dawn("bg ext_path_night"))
    with dissolve
    play ambience ambience_camp_center_night fadein 2
    "We silently walked to the camp. I did not dare to start a conversation, and Alisa, too, was not eager to break this strange silence."
    th "I'm walking on a knife edge again."
    th "Can anything be normal with this girl?"
    dreamgirl "Do you want my opinion on this?"
    th "No."
    dreamgirl "It can't. And it's not about the girl!"
    "I ignored his causticity, inhaling noisily. It was about ten minutes to the camp."
    play music music_list["goodbye_home_shores"] fadein 2
    scene bg ext_clubs_night with fade3
    "Lights were on in the clubhouse."
    th "Yeah, here comes the secret tea party!"
    th "I wonder if they've found the missing gingerbread yet?"
    scene bg int_clubs_male_night_7dl
    play sound sfx_open_door_clubs_2
    show el normal pioneer at fleft
    show mz normal glasses pioneer at right
    show un normal pioneer at cleft
    "Elektronik, Buzzer and Lena were sitting at the table."
    show un shy pioneer at cleft
    with dspr
    "The latter, seeing us with Alisa, hastily looked away."
    me "Good evening, gentlemen! Boiled the water yet?"
    show mz angry glasses pioneer with dissolve
    show el shy2 pioneer with dissolve
    "The librarian frowned, and Syroezhkin blushed deeply, trying not to look me in the eyes."
    th "What, they won't even offer to join out of politeness? Dvachevskaya was right, we're not welcome here."
    show dv normal pioneer with dissolve
    dv "Don't panic, we're here just to turn off the equipment."
    dv "We won't covet your cookies!"
    play sound sfx_open_door_clubs_nextroom
    scene bg int_clubs_dj_nolight_7dl with dissolve
    "The music was no longer playing, so Alisa simply pulled the plug out of the player, turned off the amplifier and flopped down in a chair, exhausted."
    me "So how's your first day as the camp's DJ?"
    show dv tired pioneer with dissolve
    dv "To be honest, I expected it to be more fun."
    "The redhead confessed."
    dv "But thank God it's not being too troublesome!"
    th "It's not troublesome yet. I'm afraid that soon our kind leader will have questions about the sloppiness of our radio broadcasts."
    th "Anyway, why do I call them 'ours'?"
    th "What do I have to do with this? Alisa was appointed as the DJ!"
    th "I'm just hanging around, looking for an excuse to be with her. But it seems to be making progress."
    show dv normal pioneer close with dissolve
    dv "Gotta go to bed."
    me "Want me to see you off?"
    show dv angry pioneer close with dissolve
    dv "No."
    "Somehow Alisa blurted out too sharply."
    dv "There are no wolves here, I'll find the way myself."
    show dv normal pioneer with dissolve
    show dv normal pioneer at fleft with move
    "She rose from her chair, pushing it sharply, and hurried to the door."
    dv "Bye."
    me "Good night to you too."
    "I muttered in confusion."
    hide dv with dissolve
    play sound sfx_close_door_1
    th "Oh, those girly things…"
    th "Mood swings like this will drive me to my grave!"
    scene bg ext_clubs_night with diam
    "Trying not to think about what so suddenly spoiled our beautiful and cozy evening by the fire, I followed - to sleep."
    show sl normal pioneer with dissolve
    "Walking out I bumped into Slavya."
    show sl dontlike pioneer with dissolve
    "She frowned when she saw me, but I nodded at the bag of cookies in her hands with a mocking smirk, causing the activist to blush."
    show sl shy pioneer with dissolve
    me "Have a nice tea party."
    hide sl with dissolve
    "And, without letting her say a word, pushed the girl in the doorway, getting out."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day4_dv_dj_sleeptime:
    scene bg ext_house_of_mt_night with fade3
    play ambience ambience_camp_center_night fadein 1
    play music music_7dl["melancholy_sun"] fadein 3
    "Olga was already waiting for me at the house, and the expression on her face did not bode well."
    show mt angry pioneer with dissolve
    mt "Would you mind telling me where you and Dvachevskaya have been for the entire evening?"
    me "What makes you think I was with her?"
    show mt smile pioneer with dissolve
    mt "Little bird told me."
    "The squad leader smiled venomously."
    mt "I went into the radio room three times and it was empty. Do you have any thoughts on this?"
    me "But the music was playing."
    "I grumbled."
    show mt angry pioneer with dissolve
    mt "It could be pioneers from the fifth squad. The DJ's post suggests announcements and a program."
    show mt normal pioneer with dissolve
    mt "This is a serious and responsible position!"
    th "And that's why you gave it to Alisa..."
    me "Was there any briefing? Any assignments, recommendations for work?"
    "The best strategy, it seemed to me, was the offensive."
    me "We were simply given a radio room and told: “Now we have a radio in the camp!“"
    me "What were we supposed to do?"
    show mt angry pioneer with dissolve
    mt "That's why I've been looking for you all evening!"
    "Olga was not going to give in."
    mt "Okay, Alisa hasn't been feeling well since this morning, and I didn't have time for instructions, but just like that, leaving your post like that!"
    mt "What if the equipment went haywire? What if you needed to make some urgent announcement?"
    "She gave me a menacing look."
    show mt normal pioneer with dissolve
    mt "Tomorrow you will have instructions and tasks. Just you try to disappear again!"
    mt "And now march to wash and sleep! Lights out was ten minutes ago."
    me "Remind those gathered in the clubs about this."
    show mt sad pioneer with dissolve
    "I caustically spat it out."
    hide mt with dissolve
    extend " Olga pursed her lips and walked away without deigning to answer me."
    play ambience ambience_int_cabin_night fadein 2
    scene bg int_house_of_mt_night with dissolve2
    play sound sfx_close_door_1
    "When I entered the house, I immediately collapsed onto the bed. The idea of dragging myself somewhere else didn't sit well with me, so I made out the bed and turned off the light."
    scene bg int_house_of_mt_night2 with dissolve
    th "It turned out to be a strange day. {w}He was spinning around Alisa, not moving a single step, but what kind of person she was, he still did not understand."
    th "And how did I manage to fall in love with the most difficult girl in this camp!"
    dreamgirl "Finally admitting it?"
    th "What should I hide now?"
    th "I made it clear to her that I wasn't going to be left behind. She didn't show any obvious displeasure about it."
    th "So now we are..."
    th "Colleagues."
    "With a sigh, I pulled the blanket up to my chin. It seems that the squad leader secretly signed us both as DJs, so I had plenty of reasons to spend time with the redhead."
    th "But are these enough reasons to get close to her?"
    "I didn't know that. She was prickly, angry and didn't suffer from an excess of conscience at all."
    "And that's what fueled my excitement!"
    th "Tomorrow I..."
    show blink
    th "Tomorrow…"
    scene cg d7_dv
    show prologue_dream
    with dissolve
    "My eyelids were closing heavily, and my mind was drifting somewhere far away."
    "Where Alisa laughed warmly and sincerely in the firelight."
    stop ambience fadeout 3
    stop music fadeout 3
    with fade
    return

label alt_day5_dv_dj_morning:
    scene black with dissolve
    $ volume(0.5, 'ambience')
    play ambience ambience_7dl["rain"] fadein 4
    th "I hate getting out of bed when it's raining outside..."
    th "In this weather, you can either sleep sweetly or stare aimlessly out the window at how the roofs of skyscrapers hide behind a gray curtain of tiny drops. There are no other options."
    scene
    $ renpy.show("bg int_house_of_mt_sunset", what = Desat("bg int_house_of_mt_sunset"))
    show mt angry pioneer
    show unblink
    play music music_7dl["raindrops"] fadein 2
    "But the stubborn squad leader did not share my position at all."
    mt "Quickly march to wash, five minutes left before breakfast!"
    mt "Today you have a big task ahead of you, so take the trouble to clean yourself up and gain strength."
    me "What task?"
    show mt normal pioneer with dspr
    play sound sfx_bed_squeak2
    "I got up reluctantly and sat up on the bed, my fingers smoothing my tousled hair."
    show mt smile pioneer with dspr
    mt "I'll only tell you after you've washed up."
    "Olga giggled."
    th "Doing something in the pouring rain? Brrr, what an abomination!"
    me "You know, I was just thinking... {w}I think I'm handsome enough without washing."
    show mt angry pioneer with dspr
    mt "Don't mess around here!"
    play sound sfx_put_sugar_cart
    "She angrily threw the raincoat she'd been holding in her hand at me."
    mt "Waiting for you in the cafeteria."
    hide mt with dissolve
    play sound sfx_close_door_1
    "As soon as the door closed behind her, I got out of bed with a sigh and began to put on my wrinkled uniform."
    th "Looks like it's time to start learning how to fold neatly."
    if herc:
        dreamgirl "Didn't they teach you that in the military?"
    elif loki:
        dreamgirl "You don't even have to try. We haven't known each other for very long, but something tells me you're untrainable."
    else:
        dreamgirl "Are you joking, or what? Remind me how many times you tried to accustom yourself to perform the simplest actions, and how did it usually end?"
    th "You're the last thing I need right now…"
    play sound sfx_open_door_1
    $ volume(1.0, 'ambience')
    scene bg ext_house_of_mt_rain_7dl with dissolve
    $ alt_pause(0.6)
    play sound sfx_close_door_1
    play sound2 sfx_7dl["eat_horn"] fadein 1
    "Putting on a raincoat, I rushed to the washbasins already to the sound of a horn calling on the pioneers to work their jaws."
    "I really did not want to go on some responsible task from the dear leader on an empty stomach."
    stop sound2 fadeout 2
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_dv_dj_breakfast:
    scene bg int_dining_hall_people_rain_7dl with dissolve
    play ambience ambience_dining_hall_full fadein 4
    play music music_list["everyday_theme"] fadein 3
    "I squeezed into the dining room with difficulty: blaring loudly, the whole camp crowded around the table closest to the exit and was in no hurry to fight for food at the distribution."
    show us dontlike sport far at right with dissolve
    us "Give it back!"
    "Ulyana, of course, was in the thick of things - scattering some pieces of paper on the floor, the girl was catching up with a boy of ten years old in appearance."
    show sl serious pioneer far with dissolve
    show us sad sport far with dspr
    sl "Stop! You'll have time to write everything, get in line!"
    th "Write what? We have an unscheduled election for a new camp director?"
    dreamgirl "More like for a sacrifice for the evening fire."
    hide us
    hide sl
    with dissolve
    "Suppressing my curiosity, I quickly walked to the empty distribution."
    th "Everything that happens will be reported to me already, but grabbing an extra plate of porridge is now much more interesting."
    show mi normal pioneer far at left
    show dv normal pioneer far at center
    show el normal pioneer far at right
    with dissolve
    "After getting a full tray of food, I turned around and noticed the second strange thing that morning: Alisa was sitting at the same table with Miku and Electronik."
    th "Gee! She's being rewired every day, isn't she?"
    "However, the redhead's face was so sour that it was not difficult to guess: she was dragged into this company, clearly not of her own free will."
    hide dv
    hide mi
    hide el
    show mt normal pioneer at cright
    with dissolve
    "And my guess was immediately confirmed, because Olga, who was standing at the end of the distribution, was just waiting for me."
    mt "Semyon, follow me!"
    "I obediently trudged behind the squad leader to that very ill-fated table."
    hide mt
    show mi laugh pioneer at fleft
    show dv normal pioneer:
        xcenter 0.40 ycenter 0.50
    show el normal pioneer at cright
    with dissolve
    "Miku happily waved her hand at me, Electronik nodded reservedly, and Alisa muttered something inarticulate."
    show mi smile pioneer with dspr
    show mt normal pioneer at fright with dissolve
    mt "So, guys, as you already know, today I have chosen you as the hosts of the radio show “Hundred questions for an adult”."
    th "Do I even know about this?"
    dreamgirl "Looks like you know now."
    show mt angry pioneer
    show el surprise pioneer
    with dspr
    mt "Now the whole camp will write notes with questions, and then we will seat everyone here and listen."
    show dv guilty pioneer
    show mi shocked pioneer
    show el upset pioneer
    with dspr
    "She gave all the newly minted hosts a stern look, but in particular she lingered on Alisa and me."
    mt "I strongly advise everyone to watch their language!"
    mt "You're adults now, and you should understand that children expect answers to their questions, not fiction or jokes!"
    show mt normal pioneer with dspr
    mt "You can also make musical pauses between responses to catch your breath."
    show mi normal pioneer
    show el sad pioneer
    with dspr
    "I cautiously looked at the crowd at the table: two boys a little younger than Ulyana grappled in the battle for the pen, some threw several notes at a time, and the queue for clean papers seemed endless."
    "Our new listeners had a lot of questions."
    show dv normal pioneer with dspr
    me "And what if we don't manage to answer everything?"
    show mt normal pioneer with dspr
    mt "It's okay."
    mt "Just close your eyes to outright nonsense and don't waste time asking questions like 'why is the water wet?' Focus on what you can definitely answer."
    show mi happy pioneer with dspr
    "I looked around our humble team."
    "only Miku, full of enthusiasm and determination, looked worthy to carry out the broadcast."
    th "I wonder, on what basis did Olga choose the hosts?"
    th "Alisa is understandable, she's like our DJ. Electronik, perhaps understands the technical sciences."
    th "Miku just knows how to talk, well, she can talk about music. What am I to them?"
    th "Looking after the redhead?"
    show mt smile pioneer with dspr
    mt "Okay, eat and get going to the radio room!"
    hide mt with dissolve
    "She left and we all looked at each other."
    show dv sad pioneer with dspr
    dv "And what kind of fly bit her in the morning?"
    el "I don't know. It's probably because of the rain..."
    "Curly guy did not smile at all at the thought of sitting in the same room with Dvachevskaya for three hours."
    "She, in turn, with all of her appearance expressed solidarity with Electronik."
    show mi smile pioneer with dspr
    mi "Come on, isn't that great?"
    "Miku was practically glowing."
    show mi laugh pioneer with dspr
    mi "Just imagine how wonderful it is - we will tell everyone about what they are really interested in!"
    show mi surprise pioneer with dspr
    "She broke off, looking at our sour faces."
    show mi dontlike pioneer with dspr
    mi "You're all old and boring!"
    me "Why are we old?"
    dreamgirl "So you agree with the second point?"
    show dv sad_smile pioneer with dspr
    dv "Miku is the youngest in our squad, except for Ulyana. So no wonder an awl's pricking her…"
    show el scared pioneer
    show mi surprise pioneer
    show dv surprise pioneer
    with dspr
    el "Will they ever stop?"
    "Syroyezhkin in a panic looked at the box with the notes, which had already formed such a good hill and threatened to fall out of it."
    show el sad pioneer with dspr
    "I ate more porridge - the sooner we get out, the less work we have to do."
    me "By the way, who will be the main host?"
    "I inquired casually."
    show dv normal pioneer with dspr
    dv "Miku, of course."
    dv "She has a boneless tongue."
    show mi upset pioneer with dspr
    mi "And someone happens to have bones in theirs?"
    show mi serious pioneer with dspr
    "Miku began to run her tongue over her mouth with a stupid face, obviously trying to find the bones in it."
    dreamgirl "Oh!"
    dreamgirl "It's like..."
    th "I can see it myself!"
    "I buried my eyes in a glass of cocoa, so as not to invent too much for myself."
    show el normal pioneer with dspr
    el "Have any of you ever hosted anything?"
    "Cautiously asked Electronik."
    "Even though he tried to keep calm, the trembling spoon in his hand gave him away."
    show mi normal pioneer with dspr
    mi "On the radio - no, and I had to give concerts only here, in the camp. But one day I was invited to a TV show ..."
    th "That's it, now we won't get out of here for a long time."
    "Mentally turning off the sound in my head, I stealthily glanced at Dvachevskaya."
    "Alisa was unusually quiet today."
    "She silently chewed on a roll with a missing face, point-blank not noticing Miku's chatter."
    dreamgirl "She'll have enough time to babble before the shift ends."
    dreamgirl "Now she has a serious and responsible job - to announce the air temperature twice a day!"
    dreamgirl "Or what does the radio host do in the camp? Saying hello?"
    show mi shy pioneer with dspr
    mi "...and then during the concert, flowers fell under my feet, can you imagine? It was insanely pleasant, and maybe even romantic, but then I almost hurt my forehead!"
    me "Is everything finished?"
    "I asked forcefully."
    show el smile2 pioneer with dspr
    "Syroezhkin looked at me gratefully, grabbing his tray and rising from his chair."
    show mi sad pioneer with dspr
    "Miku sighed."
    mi "And I also remembered this..."
    show dv dontlike pioneer with dspr
    dv "You'll tell us on the way. Let's go before our letter box cracks at the seams!"
    th "Shouldn't we just send it all to the trash and mark it as spam?"
    hide el
    hide dv
    hide mi
    with dissolve
    "Meanwhile, the box was already overflowing."
    "An unfamiliar squad leader was dragging a boy of nine years old by the hand."
    $ meet('voice', "Squad leader")
    voice "Kolya, enough! You've already written five questions!"
    $ meet('voice', "Voice")
    pi "But Anna Leonidovna, I still have a question about the phone…"
    show dv angry pioneer at left with dissolve
    dv "The shop's closing!"
    show dv angry pioneer at center with move
    "Screamed Alisa, pushing the rest of the children away from the table."
    "They parted reluctantly, looking longingly at the remaining empty papers."
    th "Did they really hope we could handle THAT MANY questions?"
    hide dv with dissolve
    "I slipped the box into my bosom, sheltering it from the rain."
    "Our procession advanced to the clubs."
    stop ambience fadeout 3
    stop music fadeout 3
    return

label alt_day5_dv_dj_dvachcast:
    scene bg int_clubs_male_rain_7dl with dissolve
    play music music_7dl["carefree"] fadein 3
    $ volume(0.5, 'ambience')
    play ambience ambience_7dl["rain"] fadein 1
    "Throwing raincoats on the table, we headed to the radio room."
    play sound sfx_open_door_clubs_nextroom
    scene bg int_clubs_dj_7dl with dissolve
    show el normal pioneer at fleft
    show dv normal pioneer
    show mi normal pioneer at right
    with dissolve
    "Electronik kindly brought in two more chairs while Alisa fiddled with the microphone."
    th "It's good that we bothered to clean up here!"
    th "Don't have to sit on each other's heads."
    me "What time should we start broadcasting?"
    mi "Twenty minutes to ten, when everyone has already finished breakfast. But for now, you can put on music and start sorting questions."
    "I put the box of notes on the table next to the microphone."
    "The top papers, despite all my efforts to shelter them from the rain, got wet anyway, so without a twinge of conscience I crumpled them into an armful and threw them into an empty box next to the table."
    show mi shocked pioneer with dspr
    "Miku's eyes widened."
    mi "Semyon, what are you doing? What if there was something really interesting for those who asked?"
    mi "Is it possible to just take and throw away someone's work?"
    me "Yup."
    "I shrugged indifferently."
    show mi dontlike pioneer with dspr
    me "Whoever really wants to get his answers will find them himself."
    "Through the noise of the rain, the music was barely audible - Alisa turned on something from the repertoire of the Kino group."
    dv "Toss all nonsense in the trash immediately."
    "The redhead stated peremptorily as she pulled the first note out of the box."
    dv "What is the name of the back of the knee?"
    show el think pioneer with dspr
    el "Good question."
    "Muttered Electronik."
    show el think2 pioneer with dspr
    el "Really, how's it called?"
    show el normal pioneer with dspr
    dv "It's not."
    "Snorting, Alisa crumpled up the paper and tossed it into the drawer."
    dv "What else do we have?"
    show mi upset pioneer with dspr
    mi "How would you say 'You' in Korean?"
    "While the Japanese girl was frowning, remembering the right word, I snatched the note from her and threw it away - out of harm's way."
    show el serious pioneer with dspr
    el "Looks like it's time to start."
    "Electronik interrupted us."
    me "But we didn't even sort the questions!"
    show el normal pioneer with dspr
    dv "We'll figure that out as we go."
    show mi shy pioneer at center
    show dv normal pioneer at right
    with move
    "Alisa moved the microphone towards Miku."
    th "To hell with the moderation - all the pioneers here seem to be decent people, perhaps even a little intelligent. But shouldn't we first discuss our broadcast plan?"
    th "Prepare an introduction, describe what and when which of us does?"
    show mi happy pioneer with dspr
    "However, the artistic director did not bother with such trifles."
    "She gleefully grabbed the microphone with both hands and smiled charmingly: apparently, she has not yet got used to not being a voice for her audience without a pretty picture."
    show mi laugh pioneer with dspr
    mi "Good morning, Sovyonok! To everyone who is still eating, bon appetit!"
    mi "It's raining outside, but don't let it cloud our day - there's so much more to come!"
    mi "A hike awaits us in the evening: a forest, a fire, a guitar... Romance!"
    el "And potatoes."
    "Electronik prompted in a whisper."
    show mi smile pioneer with dspr
    mi "And potatoes, of course!"
    mi "I think many of you consider this the best part of any hike."
    show mi happy pioneer with dspr
    mi "You know how I love potatoes baked in a fire, I would only eat them, but Pa always said that the diet should be varied, otherwise I'll get vitamin deficiency..."
    show dv dontlike pioneer with dspr
    "Alisa covered her face with her hands and mumbled something abusive under her breath. Electronik giggled nervously, lowering his eyes to the floor."
    me "Let's get down to business, Miku!"
    "I shushed."
    show mi surprise pioneer
    show dv normal pioneer
    with dspr
    mi "Ah!"
    show mi shy pioneer with dspr
    mi "And now, when you are all gathered in our large and cozy dining room, we have prepared a radio program for you so that no one gets bored!"
    mi "A hundred questions for an adult!"
    "There was an awkward pause."
    show mi serious pioneer with dspr
    mi "Alisa, why didn't you include any music as an intro?"
    "Miku whispered, covering the microphone with her palm."
    show dv normal pioneer with dspr
    "The redhead shrugged apathetically."
    dv "You didn't ask."
    show mi angry pioneer with dspr
    mi "But that was obvious!"
    show mi shocked pioneer with dspr
    "I snatched the mic from Miku, barely able to keep from rolling my eyes."
    th "With hosts like that, we won't even get to the questions. Even more so to the answers..."
    show dv smile pioneer with dspr
    me "Today, pioneers from the first squad answer your questions: Alisa Dvachevskaya, the main DJ of our radio!"
    show mi shy pioneer with dspr
    me "Hatsune Miku, art director!"
    me "Sergey Syroezhkin, uh…"
    show el smile2 pioneer with dspr
    if ('library' in list_voyage_7dl):
        me "Editor of the camp newspaper and member of the cybernetics club!"
    else:
        me "The future luminary of our homeland's science!"
    if herc:
        me "And Semyon Sychev, deputy DJ and…"
        "I cut off."
        th "Damn, I have a different last name here!"
        dreamgirl "Smart thought comes after?"
        "I looked around, but no one paid attention to my oversight."
    elif loki:
        me "And yours truly, Semyon Persunov!"
    else:
        me "And Semyon Persunov… that's me!"
    "I pulled the first piece of paper out of the box:"
    me "So, the first question we have from Anatoly: {i}What's for lunch today?{\i}"
    th "It seems that Olga said something about such questions, something about immediately sending them to the furnace?"
    "The microphone was immediately snatched out by Alisa."
    show dv normal pioneer with dspr
    dv "If Anatoly was able to write this question, then I believe that he can also read."
    dv "Meal schedule hangs on a column at the very beginning of the distribution. Consult it at your own leisure."
    dv "The next question we have is from…"
    "She pulled out a note."
    dv "…Yarik from the fourth squad."
    show dv surprise pioneer
    show mi surprise pioneer
    with dspr
    dv "{i}Do beavers eat wood?{\i}"
    dv "Ummm..."
    "She furrowed her brows and pursed her lips, giving us a questioning look with a hint of panic."
    dv "Well…"
    show el serious pioneer with dspr
    el "Not really wood, more like its bark."
    show dv smile pioneer
    show mi normal pioneer
    with dspr
    "Syroezhkin joined, taking the microphone from Alisa."
    show el smile2 pioneer with dspr
    el "But I don’t advise you to do this, otherwise you will end up in Dr. Violetta’s office!"
    show el normal pioneer with dspr
    el "Next question…"
    show el smile pioneer with dspr
    extend " wasn't actually a question!"
    show dv normal pioneer with dspr
    el "A mysterious stranger from the first squad asks to include the song 'Still Loving You'."
    show el normal pioneer with dspr
    me "We'll make sure to include it in the playlist during the music break."
    me "In the meantime, a question from Yura from the second squad: {i}Why do girls always go…{\i}"
    "I coughed in a futile attempt to mimic some sort of censorship."
    me "{i}…together?{\i}"
    th "What an asshole!"
    show mi sad pioneer with dspr
    mi "Because it's very sad to be alone! As one famous song said - 'if you set out with a friend, if you set out with a friend, the road is merrier'..."
    "Miku chirped, even without looking at the note."
    "It was for the best: if she saw the missing word, she would certainly be embarrassed."
    th "Or worse, she'd at least open the eyes of mankind to the terrible truth."
    "Of course, I was also worried about this mystery of female nature, but for such tricks on the air, our heads would certainly fly off our shoulders faster than the fifth squad takes up all the seats in the dining room."
    show mi smile pioneer with dspr
    mi "And the next question we have from Liza from the fifth squad: {i}Why does water fall from the sky as snowflakes in winter, and not hail?{\i}"
    hide el
    hide mi
    show dv normal pioneer close at right
    with dissolve
    "While Electronik happily talked about the crystallization of water in the clouds, I turned to Alisa."
    me "For now, you can start collecting all the songs that will be ordered from us into one playlist. For starters, Scorps."
    dv "Uh-huh."
    "Alisa didn't look very cheerful."
    th "That's understandable: we've been busy working since the morning, and even without the opportunity to slip away, like last night."
    th "But it's still kinda... weird?"
    th "Yes, she should shine - so much room for jokes and practical jokes! So many opportunities for ambiguous and ambiguous answers!"
    th "Why does she show with her whole appearance that she only wants to be left alone?"
    th "Have you been listening to music all night again? Or is your stomach hurting again, and you couldn't get to the infirmary post because of the bad weather?"
    me "Are you all right?"
    "I asked softly, leaning close to the girl's ear."
    show dv guilty pioneer close with dspr
    "She shuddered."
    dv "Yeah. I mean…"
    show dv tired pioneer close with dspr
    "Frowning, Alisa again buried herself in the player."
    dv "I didn't get enough sleep again, and the Hat was impatient to put on this show from the very morning!"
    me "I understand. I was as surprised as you are."
    show dv normal pioneer close with dspr
    "The girl looked at me strangely, but said nothing."
    show el normal pioneer at fleft
    show mi normal pioneer
    show dv normal pioneer at right
    with dissolve
    el "{i}Why do boys fight so often?{\i} Polina, 4th squad."
    show el think2 pioneer with dspr
    el "Uh…"
    "Syroyezhkin scratched the back of his head."
    show el normal pioneer with dspr
    el "Well, I personally have never fought, but you should know: fights are bad!"
    show dv angry pioneer
    show el surprise pioneer
    with dspr
    dv "Idiot."
    show dv angry pioneer at center
    show mi surprise pioneer at right
    with move
    "Alisa hissed, throwing the player aside and snatching the microphone from him."
    dv "Boys fight because that's how they show their strength and stand up for their right to be the leader."
    dv "The leader must be the strongest, as he is responsible for everyone he leads."
    dv "He will protect them, he will make decisions."
    show dv normal pioneer with dspr
    dv "Among adults, those who are smarter or more cunning become leaders, but kids don't care about such subtleties. Everything is measured by their courage and strength of fists."
    me "But it's not worth fighting anyway!"
    show dv dontlike pioneer
    show el normal pioneer
    with dspr
    "I added, without much effort taking away the microphone from the raging Alisa."
    th "That's what she was talking about yesterday. The things that can't be eradicated from her are not smoking and rude speech."
    th "It's the kind of understanding of life that kind house kids like Electronik will never get."
    me "And now - a musical pause! A track for a beautiful stranger from the first squad!"
    show dv normal pioneer with dspr
    "Alisa turned on the music and cut off the microphone, and we all breathed a sigh of relief."
    show el upset pioneer with dspr
    el "Do you think we're doing okay?"
    "There was no confidence in his tone."
    show mi smile pioneer with dspr
    mi "Yeah, at the beginning we messed up a little because we didn't have time to prepare, but now it's much better."
    "Miku nodded approvingly."
    show el sad pioneer with dspr
    mi "And the interesting questions have started coming, and they ask to play music... Like on a real radio!"
    show el normal pioneer with dspr
    "She handed me three more song order notes."
    "I gave them to Alisa."
    me "Add them to the queue?"
    "The girl nodded and turned to the player."
    show mi happy pioneer with dspr
    "Miku stared at me and Electronik with curiosity, dreamily closing her eyes."
    mi "What do you think, who from our squad asked to play this song? It's usually played as a slow dance, so it's almost a declaration of love!"
    "Syroyezhkin shrugged his shoulders."
    el "Maybe Slavya?"
    dv "For our scribbler to listen to this? Definitely not."
    "Snorted Alisa, not looking up from the player."
    show el smile pioneer with dspr
    el "Then probably Zhenya?"
    "Syroezhkin asked with some incomprehensible hope in his voice."
    show mi smile pioneer with dspr
    mi "Zhenya never goes to the dances, definitely not her. Probably Lena!"
    show el normal pioneer with dspr
    th "True - who else would it be, Ulyana?"
    "I pulled another question out of the box, read it briefly and crumpled the paper, sending it to the box with the rest of the 'spam'."
    th "What the hell is this shit."
    $ hvala_randomu_7dl = renpy.random.choice([1, 2, 3, 4, 5])
    if hvala_randomu_7dl == 1:
        th "Where does the giant crab robot come from in the camp? Have they eaten henbane, or something?"
    elif hvala_randomu_7dl == 2:
        th "And that one I think I should report to the authorities, call your Gen. Sec. a DICKtator is a bit too much even for me."
    elif hvala_randomu_7dl == 3:
        th "Although I would advise to not vent in front of the cameras, even if they're off."
    elif hvala_randomu_7dl == 4:
        th "Everyone has long known that rocking is more legal than stoning, but it is unlikely that the author of the question had this in mind…"
    else:
        th "«Daddy won't read me the Bible before bedtime, what should I do?»... What? Isn't the USSR a deeply atheistic country? Also... Is Gabriel even a russian name?"
    "The track came to a smooth end and we got tense again - you could expect anything."
    show mi grin pioneer with dspr
    mi "Well, friends, we are back on air and continue to answer your questions!"
    if herc:
        "I pulled a random question out of the box."
        th "Well, that was to be expected..."
        "With a stone face, I passed the note to Miku."
        show mi shy pioneer with dspr
        "She hesitated and, blushing deeply, immediately thrust the paper to Alisa."
        show dv surprise pioneer with dspr
        "Her eyes widened."
        play sound sfx_hatch_drop
        show dv angry pioneer
        show el surprise pioneer
        with dspr
        "She unceremoniously slammed her hand on the table in front of the Electronik. Now the note was right in front of him."
        dv "Answer!"
        "She commanded in a tone that brooked no objection."
        stop music fadeout 3
        "Electronik obediently nodded and took the ill-fated note."
        show el scared pioneer with dspr
        play music2 music_list["always_ready"] fadein 3
        el "Where do babies come from?"
        "Only after voicing this question, Syroezhkin choked and coughed, looking around at us in a panic."
        "It was starting to dawn on him how deep he was."
        th "It seems that he never learned to read to himself in ten years at school..."
        show mi grin pioneer
        show dv laugh pioneer
        with dspr
        "Alisa and Miku chuckled at the same time."
        show el sad pioneer with dspr
        "The girls were getting ready for the show and I didn't laugh with them just out of male solidarity."
        show el serious pioneer with dspr
        "Sighing convulsively, Electronik suddenly changed dramatically in his face."
        "He became calm and focused, as if he was going to speak at a party meeting."
        show dv surprise pioneer
        show mi shocked pioneer
        with dspr
        el "I'll be brief."
        el "You know, just the other day I was at the infirmary, had a conversation with Viola, she is a very competent specialist."
        el "So, we discussed, in particular, this issue - we talked about the current situation with education on this topic in the camp. She also spoke about her plans for the future - to hold a whole lecture about it."
        show el angry pioneer with dspr
        el "Of course, first of all, she was concerned about the problem of interest. The question of the reaction of parents was no less acute, but I can assure you that all these problems can be solved and we will make every effort to solve them in the very near future."
        el "This also applies to the topic raised in your question."
        show el normal pioneer with dspr
        "Determining that he had given a sufficiently exhaustive answer, the Electronik exhaled noisily, pushing the microphone away from him."
        show mi normal pioneer with dissolve
        "It was hard not to be amazed at his ability to answer simple questions with amazing accuracy and succinctness."
        dreamgirl "Maybe he just doesn't know himself?"
        th "I wouldn't be surprised if that's true."
        show dv guilty pioneer with dspr
        "Alisa looked somewhat disappointed - she clearly expected Syroezhkin to be confused and ineptly babble something about sexual pleasures."
        show mi normal pioneer at center
        show dv normal pioneer at right
        with move
        "Miku has already pulled out the next question."
        mi "Sasha from the third squad asks: {i}How do music, movies and cartoons become popular?{\i}"
        show mi smile pioneer with dspr
        mi "What a good question!"
        "Japanese cheered up."
        mi "Often good art does not need advertising and promotion, because the audience itself does it: someone liked it, he enthusiastically told his friends about it, and those friends told their friends, and so on ad infinitum."
        show mi upset pioneer with dspr
        mi "Of course, if you're just playing the guitar in a hallway, you're unlikely to become very famous, nothing is created without money, a venue for performances, and the investment of the efforts of many people."
        mi "But if something really good is being created, it will only take a little to make it a hit: performances in small bars, or a self-published manga with a circulation of a couple of hundred copies."
        show mi normal pioneer with dspr
        "Miku took a breath. She seems to be in the mood to chat for a very long time..."
        show mi dontlike pioneer with dspr
        mi "And sometimes bad things are created that literally get shoved the audience down the throat: they advertise at every step, pay radio stations and TV channels for broadcasts, the creators ask for all kinds of TV shows to once again remind themselves of themselves."
        show mi angry pioneer with dspr
        mi "It's terrible because people still don't like being forced to watch and listen!"
        mi "Creators only need money, which they will have anyway - after all, their “creation” is on everyone's lips, which means people will buy it!"
        play sound sfx_hatch_drop
        show el surprise pioneer
        show dv laugh pioneer
        with dspr
        "Angrily banging her fist on the table, the artistic director shook her head."
        mi "It's not a fair way, and no one likes it, but unfortunately the 'aggressive advertising' still works. So things become popular... in many ways."
        show mi sad pioneer with dspr
        mi "But it would be enough just to make them good!"
        show el smile2 pioneer
        show dv smile pioneer
        with dspr
        me "Maybe you can answer the next one?"
        "Quietly I whispered to Alisa."
        me "Miku can talk endlessly, and we still have a whole box of questions."
        show dv normal pioneer at center
        show mi dontlike pioneer at right
        with move
        "Alisa strained something through her teeth, but took out a note from the box."
        dv "Next question: {i}Is it true that Violetta Cernovna's eyes are different colors because one of them is glass?{\i}"
        show mi surprise pioneer
        show dv grin pioneer
        with dspr
        dv "What nonsense? Our doctor's second eye is not glass, everyone has known about this for a long time."
        show dv smile pioneer with dspr
        dv "It's electrical."
        show el surprise pioneer with dspr
        dv "Delicate tool, the latest development of Soviet scientists - specifically for doctors."
        "I could hardly contain my laughter - Alisa knew how to improvise."
        dv "With it, Viola can take the temperature of patients, see the number of germs on her hands, and, they say, she can even tell how much a person has left to live."
        dv "But the most important thing..."
        "Alisa lowered her voice to a whisper."
        show dv grin pioneer with dspr
        dv "This eye has an X-ray built into it. It allows her to examine patients without undressing - she can see everything anyway!"
        show el scared pioneer
        show mi shy pioneer
        with dspr
        "But this joke was not appreciated by our colleagues - Electronik turned pale, and Miku, on the contrary, blushed."
        el "I mean, every time she comes to our clubs..."
        show mi scared pioneer with dspr
        mi "What a nightmare! She seemed such a decent person to me!"
        "The cybernetic and the artistic director looked at each other in fear."
        mi "From now on we don't go to the infirmary until the end of the shift!"
        el "And in the canteen we sit as far as possible!"
        show el shy2 pioneer
        show mi shy pioneer
        show dv laugh pioneer
        with dissolve
        "Silly giggling, I reached for another note."
        "Surely I should have contributed to the madhouse we've made here?"
        "The next question was from Alex..."
        th "Alexandr?"
        th "Alexey?"
        th "Writes like a chicken paw! Probably plans to be a doctor when grows up."
        me "Can a sleeping pill dart instantly knock you out, like in action movies?"
        show dv surprise pioneer
        show el normal pioneer
        show mi surprise pioneer
        with dissolve
        th "This question is right up my alley - I wouldn't say that during the service I became such a room Rambo, but I know for sure about such frank nonsense!"
        me "It can't. It's all made up for show."
        me "First of all, sleeping pills and tranquilizers don't work instantly, so the only way to fall from a dart like this is if it hits your leg while you're running."
        show dv normal pioneer with dspr
        me "Secondly, it would be an extremely ineffective weapon even if it really worked like in the movies: think for yourself, why do you need to put an enemy to sleep who will attack you again when he wakes up?"
        show mi smile pioneer with dspr
        me "Even if you want to capture him alive - for interrogation, for example - it's much safer to just shoot him in the legs."
        me "But in a boring reality, such darts are used to trap wild animals. They really are much easier to transport or heal when they are out."
        "My comrades listened to me with undisguised interest."
        th "It's hard for people to live without the Internet - no way to check the facts for authenticity."
        th "It's amazing how anyone ever came up with the idea that these scenes in the movies might not be true?"
        stop music2 fadeout 3
        with fade3
        play music music_list["get_to_know_me_better"] fadein 3
    elif loki:
        show mi smile pioneer at center
        show dv normal pioneer at right
        with move
        stop music fadeout 3
        mi "And we have a question from Alka from the second squad: {i}What should be done with underpants?{\i}"
        show mi smile pioneer
        show el surprise pioneer
        show dv surprise pioneer
        with dspr
        play music2 music_7dl["genki"] fadein 2
        "Our faces with Electronik and Alisa simultaneously stretched out."
        dreamgirl "Freudian slip?"
        th "At least someone in the cafeteria will have a laugh. I hope Miku doesn't get too embarrassed..."
        show mi grin pioneer with dspr
        "But Miku didn't think to be embarrassed!"
        mi "Well, you know, the essence of the matter is a bit difficult to understand, so I can only give general recommendations."
        show mi serious pioneer with dspr
        mi "Firstly, they need to be changed at least once a day, and preferably twice - in the morning and in the evening."
        show mi normal pioneer with dspr
        mi "Secondly, you need to choose only underwear made of high-quality cotton: synthetics can cause discomfort, and pure lace rubs a lot..."
        show dv normal pioneer with dspr
        th "Looks like we'll be locked in this closet for the rest of our shift."
        show el shocked pioneer with dspr
        el "What is she even saying?"
        "Syroezhkin whispered in horror. His cheeks were filled with color."
        "Alisa just chuckled."
        dv "Pretty good advice."
        show el shy2 pioneer with dspr
        dv "Does anyone have a notebook? I'll write it down."
        show mi normal pioneer with dspr
        mi "And be sure to have a few black or just dark ones to avoid unpleasant situations on certain days."
        show mi grin pioneer with dspr
        mi "Oh yeah, and never wash them with your socks!"
        with hpunch
        show mi surprise pioneer
        show el normal pioneer
        with dspr
        me "Thank you, Miku."
        stop music2 fadeout 6
        "I said with pressure, taking away the microphone from the Japanese girl."
        show dv smile pioneer with dspr
        me "It was very interesting and informative."
        show mi normal pioneer with dspr
        play music music_list["i_want_to_play"] fadein 2
        me "{i}Whose life is more important - a man or a dog?{/i}, asks Stas from the third squad."
        show dv normal pioneer with dspr
        me "Of course, the life of a man!"
        th "Although it certainly depends on the person. There are some people when you compare them with a dog is humiliating."
        th "Humiliating for a dog, of course."
        me "Of course, every owner is attached to their pet as their own, and it is perfectly normal to perceive them not as animals, but as part of the family."
        show el smile2 pioneer
        show dv grin pioneer
        with dspr
        me "But at the same time, one should remember that there is nothing more valuable in the world than human life."
        show mi smile pioneer with dspr
        me "No one deserves to die, neither man nor dog."
        me "But, for example, running out onto the highway trying to catch a runaway pet is the peak of stupidity!"
        show dv normal pioneer with dspr
        me "Risking your life is only worth it in the most extreme cases. And if the risk is not justified, then you will only ruin yourself over some trifle."
        me "Yes, you can tell me that I'm a fool, and that the life of your pet is not some trifle, but I will answer: your life is certainly not a trifle for those who love you."        
        show mi happy pioneer with dspr
        dreamgirl "Why are you all of a sudden bursting into such high-flown speeches?"
        dreamgirl "Have you ever been traded for a dog?"
        th "Uh-huh. A very particular bitch!"
        show mi smile pioneer
        show el serious pioneer
        with dspr
        el "And now a question from Syoma from the fourth squad: {i}They say that the more trees, the more oxygen in the air...{\i}"
        show el laugh pioneer with dspr
        el "To some extent, it's true!"
        el "{i}…and it's very good for health. Why don't they build air processing factories that will increase the amount of oxygen in the atmosphere?{\i}"
        show el smile pioneer with dspr
        "Syroezhkin's eyes lit up."
        el "Very interesting question!"
        show el smile2 pioneer with dspr
        el "Oxygen makes up just over twenty percent of the air we breathe."
        show el serious pioneer with dspr
        el "But, as you know, everything is a poison and everything is a medicine. Only the dose makes a medicine a poison and a poison a medicine."
        show mi shocked pioneer with dspr
        el "An excess of oxygen is just as harmful to the body as its lack. There is even such a thing as 'oxygen poisoning'!"
        show el think2 pioneer with dspr
        "The face of the cybernetic suddenly flashed with thoughtfulness."
        el "Although if we assume for a second that at the stage of formation of our planet the ratio of gases in the atmosphere would have been established differently, then how much it would have changed the development of all existing life!"
        show el smile pioneer with dspr
        el "Just imagine: the organisms of all living things would have to adapt to a higher oxygen content, and people would look completely different."
        show dv angry pioneer with dspr
        el "That is, if they'd managed to emerge as a species at all, of course."
        th "Whoa. Looks like someone just invented sci-pop podcasts."
        show el serious pioneer with dspr
        el "We would have, for example, tiny noses and much smaller chests, because we wouldn't have to breathe so often."
        el "Maybe we would breathe the same as now, just all the other organs would adjust to the increase in oxygen entering the body!"
        show dv angry pioneer at cleft
        show mi surprise pioneer at cright
        with move
        play sound sfx_punch_medium
        show el surprise pioneer
        show mi dontlike pioneer
        with dspr
        "Alisa roughly pushed him with her elbow, and Electronik came to his senses."
        show el normal pioneer with dspr
        el "In a word, it would be a completely different world. And ours does not need more oxygen, although sometimes it is very useful to go out into nature!"
        show mi normal pioneer at right with move
        show dv normal pioneer at center with move
        dv "So next question: {i}What do a crow and a desk have in common?{\i}"
        show dv dontlike pioneer
        show mi upset pioneer
        with dspr
        "As soon as she voiced it, Alisa frowned and twisted her mouth."
        dv "These bastards!"
        "I read her lips."
        "For some reason it became funny."
        th "Of course, there are some good answers to this riddle, but I won't tell her. Let her brainstorm - this is a useful activity."
        th "But Alisa couldn't find the right answer. Let's see what ours can do..."
        show dv sad pioneer with dspr
        dv "Actually, I'm not quite sure how it was possible to not understand this until now. It's obvious!"
        "The redhead tried in vain to play for time, looking at us in despair."
        "Miku herself was sitting with a thoughtful face, Electronik just shrugged his shoulders, but I..."
        "I smiled wickedly."
        me "So tell them, since it's obvious!"
        show dv angry pioneer
        show mi laugh pioneer
        with dspr
        "Giving me the middle finger, Alisa turned back to the microphone."
        show dv normal pioneer with dspr
        dv "Context matters here. Everyone remembers at what point the Hatter said this riddle? At tea time, right."
        show mi normal pioneer with dspr
        dv "It's quite logical that they don't drink tea at the desk. They do their homework and other boring things behind it."
        show dv think pioneer with dspr
        dv "If, say, you bring a cup of tea to the desk, then you won't be able to do business. You will be distracted by tea."
        "It was difficult to follow the thread of her reasoning, but I held on for now."
        show dv grin pioneer with dspr
        dv "And what is the name of the phenomenon when you are distracted from important matters by something else?"
        show el normal pioneer at left with move
        "Alisa sustained a theatrical pause with such an air of importance that the Electronik moved forward, as if he was afraid to miss something brilliant."
        show dv laugh pioneer with dspr
        dv "{i}Counting crows{\i}!"
        show el surprise pioneer
        show dv smile pioneer
        show mi surprise pioneer
        with dspr
        dv "See how simple and logical everything is?"
        me "Yeah, and most importantly - intuitive."
        "I muttered."
        th "I've never heard such nonsense in my life!"
        dreamgirl "What did you expect?"
        th "That's true. At least she didn't tell the questioner to go to hell - thanks for that!"
        show el normal pioneer with dspr
        el "Don't you think it's a little... not consistent with any cause-and-effect relationships?"
        "Cautiously asked Electronik."
        show dv angry pioneer
        show el sad pioneer
        with dspr
        dv "See if I care!"
        "Alisa snorted in annoyance."
        dv "Everyone gets the answers they deserve!"
        stop music fadeout 4
        show el normal pioneer at fleft
        show mi normal pioneer
        show dv normal pioneer
        with joff_r
        play music music_list["everyday_theme"] fadein 3
    else:
        "Alisa already pulled out one of the notes."
        show dv smile pioneer with dspr
        dv "Oh, familiar handwriting."
        "She chuckled."
        "I looked over her shoulder, reading the question."
        "The author, apparently, decided to remain anonymous, but it was not difficult to identify him by his red face and large jumping letters."
        stop music fadeout 1
        show dv surprise pioneer with dissolve
        play music2 music_list["that_s_our_madhouse"] fadein 4
        me "Well, here I can give some good advice!"
        show dv angry pioneer with dspr
        dv "Hey, give it back!"
        hide mi
        hide el
        show dv angry pioneer close
        with dissolve
        "I jumped out of my chair, grabbing the microphone from the table and dodging Alisa, who was trying to take the note away from me."
        me "Our listener, who wishes to remain anonymous, asks: {i}How do I get a boy to like me{\i}?"
        show dv rage pioneer close at left with move
        me "Actually, it's not that hard."
        show dv rage pioneer close at cleft with move
        me "Remember, my little redhead friend..."
        show dv angry pioneer with vpunch
        "I deftly dodged Dvachevskaya's fist."
        me "First of all, throw a heavy and large pinecone at him. Aim for his head so that he quickly realizes that you are showing him signs of attention!"
        show dv angry pioneer close with dissolve
        me "Then make an unforgettable impression on him - you can, for example, break the nose of someone else in his presence."
        "Bending down again so that I wouldn't get hit in the ear, I jumped back to the other corner of the closet, as far as the length of the wire allowed." with hpunch
        me "Well, don't forget that a woman should have a mystery, so after your performance, disappear from sight for two hours - let him get nervous and look for you!"
        show dv rage pioneer at veryclose with dissolve
        "Finally, Alisa caught up with me, and before my knee met her sandal again, I could only blurt out:"
        me "That's it, you're gorgeous! Get your dress ready for the next dances, you're already invit..."
        hide dv
        show mi scared pioneer at center
        show el upset pioneer at fleft
        with flash_red
        me "AAAAAAAAAAAAAAHHHHH!"
        show el sad pioneer with dspr
        mi "Thanks to Semyon for the very precise instructions!"
        "Miku intercepted the microphone, trying to drown out the sounds of my shameful beating with her voice."
        show mi angry pioneer with dspr
        mi "Seems like some people started doing them right away!"
        stop music2 fadeout 6
        show dv angry pioneer at right with dissolve
        dv "The hell did you say?"
        show el surprise pioneer close with dissolve
        "Alisa got distracted enough for me to crawl away and hide behind the dazed Electronik."
        play music music_list["get_to_know_me_better"] fadein 3
        show mi normal pioneer
        show dv normal pioneer
        with dissolve
        mi "And the next question we have is from someone named N. from the second squad: {i}Is it true that in the future robots will replace live singers?"
        show el normal pioneer close with dspr
        mi "Actually, I don't think it's possible. How can a robot evoke any emotion in the listeners, even if they create a perfect voice for it?"
        show mi smile pioneer with dspr
        mi "And even if he is completely indistinguishable from a person, then what will he sing about? About numbers and the dim fire of screens?"
        show el normal pioneer at fleft
        show mi upset pioneer
        with dissolve
        mi "The robot will never have feelings, which means it will never talk about something important to the listener."
        mi "A robot will never be loved the way a live performer is loved. After all, people come to concerts not to listen to music, but to feel the artist live!"
        show mi serious pioneer with dspr
        mi "Therefore, artificial creations will never supplant the musicians."
        "Either Miku thought about it too, or she was simply offended by even the very idea that she could be replaced with a conditional Vocaloid."
        th "Artists are so vulnerable."
        show mi normal pioneer with dspr
        "Electronik already retrieved microphone."
        el "{i}What is the way the Great Crystal works?{\i}"
        show el smile pioneer with dspr
        el "Oh, Krapivin! I respect this!"
        show el laugh pioneer with dspr
        el "First, we need to figure out what this Crystal is. Imagine an infinite smooth rod. This is the first approximation."
        el "And now the same rod, but faceted like a pencil, and the number of faces is infinite. Each face is its own world."
        show mi upset pioneer with dspr
        show el serious pioneer with dspr
        el "And this rod is closed in a ring of infinite radius. The ring is closed with a rotation by one face, so we get a polyhedral Möbius surface."
        "I stopped understanding him around the point with the ring."
        "Miku folded her hands in concentration - apparently, she was trying to visualize all the nonsense that Syroezhkin was spitting out."
        show el normal pioneer with dspr
        el "And these faces are not smooth, but are themselves divided into separate ones... sub-faces, perhaps, along the axis of this former rod. And each sub-face is its own world."
        show dv angry pioneer with dspr
        el "From each subfacet we can get through the Edge to the neighboring subfacet, sometimes we can go diagonally through the Node."
        el "When moving from edge to edge, the conditions of existence change, the universes are different..."
        show dv rage pioneer at cleft
        show mi surprise pioneer at right
        with move
        show el surprise pioneer with dspr
        dv "We get it, you read it!"
        play sound sfx_punch_medium
        show el upset pioneer
        show mi dontlike pioneer
        with flash
        "Alisa slapped Syroezhkin on the head with an encyclopedia she got from god knows where."
        show dv angry pioneer with dspr
        dv "No one here is interested in your retellings of Krapivin!"
        show dv angry pioneer at center with move
        dv "What do we have next?"
        "The girl snatched the question out of the box."
        show dv normal pioneer
        show mi upset pioneer
        with dspr
        dv "{i}Why can you only drink alcohol at the age of twenty-one?{\i}"
        show el normal pioneer with dspr
        dv "I don't get it either, to be honest."
        "Alisa shrugged her shoulders."
        dv "Probably because they don't sell it until you're twenty-one?"
        show mi dontlike pioneer at cright with move
        "Miku hissed something in displeasure right into her ear, and the redhead grimaced."
        dv "Well, because it's bad for children - if you drink a lot in childhood, you will become an ugly, feeble-minded midget."
        el "What if it's a little bit?"
        show dv smile pioneer with dspr
        dv "Then you probably won't. Don't they just say that you should drink in moderation?"
        th "A measure, as you know, is twenty-four liters..."
        show mi shocked pioneer at right with move
        mi "So, you can still drink a little?"
        "Miku looked at us in fear."
        show mi shy pioneer with dspr
        mi "Don't get me wrong, I don't abuse, but sometimes after concerts, Sakishita-san would let me have a drink..."
        show el surprise pioneer
        show dv surprise pioneer
        show mi surprise pioneer
        with vpunch
        me "Quiet!"
        "I snatched the microphone from them before they said anything else."
        me "No one should drink at any age!"
        show el normal pioneer
        show dv dontlike pioneer
        show mi smile pioneer
        with dissolve
    me "And now - a musical pause! Especially for Roma from the second squad, the song 'Diamond Roads' is playing!"
    "I abruptly turned off the microphone, almost tearing it out of the amplifier - my hands were shaking so much."
    me "Do you think we can go and pack our bags now?"
    show dv smile pioneer with dspr
    dv "Come on, it's not as bad as you think."
    dv "At least there were no strong curses, which can already be considered a success!"
    show mi sad pioneer
    show el think pioneer
    with dspr
    "Alisa's malevolent optimism was not shared by anyone."
    mi "If only the questions weren't so stupid..."
    "Sadly drawled Miku."
    mi "Now it doesn't seem to me that everyone is so interested in learning something new. Most of them just scoff!"
    me "What did you think? They're children."
    "I consoled the girl."
    show el normal pioneer with dspr
    me "They understand that we will not answer the most interesting questions, so they write all sorts of nonsense."
    show dv sad pioneer with dspr
    dv "What are the interesting ones?"
    dv "About what their parents do in the bedroom at night?"
    "Alisa looked at us all gloomily."
    show dv guilty pioneer with dspr
    dv "I don't know about you, but I personally think that everything we do here is a waste of time."
    "Not to say that I knew Alisa that well, but these words from her lips sounded somehow... unnatural?"
    th "Shouldn't she have been much ruder?"
    th "Worst case scenario, just slam the door and walk out, leaving us to deal with these damn questions?"
    "But the girl just sat with her arms crossed over her chest, and stared into the corner behind me, as if she was already indifferent to everything that was happening."
    hide mi
    hide el
    show dv guilty pioneer close
    with dissolve
    "I moved my chair closer to her."
    me "If you don't want to participate in this, then don't worry: if I tell the squad leader that you feel bad..."
    show dv angry pioneer close with dspr
    dv "I can do it myself."
    "Alisa cut off."
    dv "I don't think I ever wanted to participate in anything, but no one gave me a choice."
    "She looked at me so angrily, as if I were the source of all her troubles and misfortunes, and I again felt the same strange feeling as at yesterday's concert."
    "Incomparable awareness of the falseness in what Alisa was doing."
    th "Yesterday she performed with talent, but without soul. Today she responds cheerfully and provocatively, but does not take any pleasure from it."
    th "What turned upside down in your world during these days that you stopped burning inside?"
    th "The way you were at the last disco, the way you met me the first day..."
    th "Where did that Alisa go?"
    mi "Maybe we should continue?"
    "Shyly asked Miku as they played the last chords."
    play sound sfx_open_door_clubs_nextroom
    show dv surprise pioneer close with dspr
    "But before she could reach out to the microphone, the door to the radio room swung open."
    hide dv
    show cs smile
    with dissolve
    "Viola, who was standing at the doorstep, looked at us mockingly."
    cs "If you are wondering how our honorable audience reacts to your performance, then I can please you: they are delighted."
    show cs normal with dspr
    cs "As for your dear leader... It's not so simple."
    "I felt my heart sink into my heels."
    cs "Actually, she sent me here to help you choose interesting questions."
    th "Thank God she didn't come here on her own. Our heads would fly off our shoulders, oh how they would fly!"
    hide cs with dissolve
    "But Viola, sitting on a chair in the corner with a box in her hands, also did not add coziness to the atmosphere."
    show el scared pioneer at fleft
    show mi shy pioneer
    show dv normal pioneer at right
    with dissolve
    "We looked at each other: Electronik was completely horrified, Miku chewed her lower lip in embarrassment, and Alisa only sneered contemptuously, buried in the player."
    cs "Here are four questions for you. Can you handle it?"
    show mi normal pioneer with dspr
    th "In less than two hours of our stream, we already have a moderator, a stable audience of a hundred people and claims from the local Roskomnadzor."
    th "I wonder when we will start donating?"
    show el sad pioneer with dspr
    "Syroezhkin cautiously took the notes from the doctor's hands."
    if herc:
        th "Did he really believe Alisa's e-eye nonsense?"
        dreamgirl "Maybe it's not so crazy after all?"
    show el normal pioneer at left with move
    el "We're back on air, Sovyonok! And we've got a question from Dasha from the fifth squad: 'What should we do if we are forced to read boring and uninteresting books at school?'"
    stop ambience fadeout 3
    show mi smile pioneer at center
    show dv normal pioneer at right
    show el normal pioneer at fleft
    with fade
    "The broadcast has entered a calm and dreary course."
    "Viola actually chose harmless questions that any well-read sixth grader could easily answer."
    th "So we're going to die of boredom here..."
    mi "...that's why you need to forgive your offenders, and not try to take revenge on them."
    el "…that's how Newton came up with the idea of gravity."
    dv "...and then you can perform on stage without worrying about having an audience."
    "Alisa is right. What we're doing now is pointless nonsense."
    "It's just that the leader was too lazy to bother with a normal event, and she happily pushed the task of entertaining the whole camp onto her unlucky pioneers, sincerely believing that they would do an excellent job of it."
    "Especially mean-tongued Alisa and ignorant of the local culture of Miku, of course!"
    hide mi
    hide el
    show dv sad pioneer at right
    with dissolve
    "I looked longingly at the redhead."
    "She was sitting at the table, resting her head on her folded hands, and looked bored at Miku, who was talking about the singing installation."
    show dv sad pioneer close with dissolve
    me "Do you think we'll have to do it again after lunch?"
    "I whispered."
    show dv guilty pioneer close with dspr
    "Alisa pursed her lips."
    dv "Unlikely."
    dv "Kids won't last even 3 hours listening to our chatter, and losing an entire day for that... They will howl!"
    show dv closed_eyes pioneer close with dspr
    "She closed her eyes wearily."
    dv "If it stops raining by noon, I'll steal a boat and run away from here."
    me "I can sit on the rows!"
    show dv smile pioneer close with dspr
    "Smiling, Alisa sat up."
    show dv normal pioneer at right
    show cs normal at center
    with dissolve
    dv "Violetta Cernovna, how much time is left before lunch?"
    cs "Half an hour. You'll love this question!"
    "The doctor handed the note to the girl, and I peered in curiously."
    th "Is it possible to learn how to play the guitar without a music school? Andrey, third squad."
    hide dv
    hide cs
    with dissolve
    "While Alisa was talking about how difficult it is to pick up chords by ear, I again stared at the ceiling."
    th "Why do I feel so disappointed?"
    th "Perhaps if Alisa and I were alone here, she would act the same way as before?"
    dreamgirl "Just deal with it, dude, you're screwed."
    th "What?"
    dreamgirl "Did she do anything these days to show her sympathy for you?"
    th "But she doesn't chase me away!"
    dreamgirl "Because what good is it to her? The girl is lonely, and you literally follow her, trying to entertain and amuse her in every possible way."
    th "And what do you offer me?"
    dreamgirl "Do something she'll really be grateful for. Signing her up for a nerd job and a bag of candy doesn't count!"
    dreamgirl "Now, if you get her some vodka..."
    th "Stop talking nonsense! Alisa isn't like that!"
    dreamgirl "What is she like?"
    dreamgirl "You drew a beautiful picture in your head in three days, and now you are surprised that everything is not as simple as it seemed at first glance."
    dreamgirl "If you wanted fun and light-hearted pranks, you could have chosen a small one."
    th "I didn't want this!"
    th "Or..."
    cs "Oh, let me answer that question."
    show cs smile at cleft with dissolve
    cs "“Is it true that there are pills that make sad people happy again?“"
    th "Yeah. Only for the storage and distribution of such pills you can go far away and be sad for a long time..."
    cs "It's true that there are such pills. But they don't make people happy instantly."
    cs "Some people may lose the ability to enjoy life - their bodies simply do not produce substances that are responsible for this very joy."
    cs "In this case, they are prescribed drugs that help them learn to live fully again. Antidepressants."
    show cs normal with dspr
    cs "The issue is that they only work after many doses, and cumulatively. Often, patients take them for more than one year, and doctors look after them all this time."
    cs "There is no and never will be joy in pills. Don't bother yourself with stupid things and have fun until boring adult worries fall on you."
    "Alisa chuckled and I gave her a blank look."
    th "Doesn't trust medicine, or is it just because of her age that she thinks depression is an invention of slackers?"
    hide cs
    show mi smile pioneer
    with dissolve
    "Miku took the microphone from Viola and glanced at the clock in the corner of the radio room."
    mi "And that concludes our transmission!"
    show mi cry_smile pioneer with dspr
    mi "Sorry we didn't get to answer all your questions, but don't worry, you still have a lifetime ahead of you and you'll learn a lot!"
    show mi smile pioneer with dspr
    mi "And now the last song. Thank you for being with us!"
    show mi normal pioneer with dspr
    "Miku exhaled noisily as she leaned back in her chair."
    mi "I never thought that working on the radio could be so difficult. And there were four of us, and Violetta Cernovna also helped..."
    show cs smile at left with dissolve
    "The latter chuckled as she rose from her seat."
    cs "I guess you don't need my help anymore. Unplug your gear and head for the canteen, pioneers!"
    hide cs with dissolve
    "At the very doorstep, Viola turned around, her eyes flashing."
    show cs serious at fleft with dissolve
    cs "Mind what you say in the future. Who knows where it will take you..."
    show mi shy pioneer with dspr
    play sound sfx_close_door_1
    hide cs with dissolve
    if herc:
        "Alisa turned away, carefully pretending that the doctor was not addressing her."
    show el sad pioneer at fleft with dissolve
    el "Okay, let's face it: it was awful."
    "Syroezhkin muttered doomedly as soon as the door closed behind Viola."
    me "It could have been worse. If instead of Viola, a PE teacher came here..."
    show el scared pioneer with dspr
    "Electronik twitched."
    el "No, I'm never signing up for this again!"
    show dv angry pioneer at right with dissolve
    dv "Me too. Even if they kick me out of the camp!"
    th "Well, wow - does Alisa agree with Syroezhkin in some way?"
    th "No other than the rain outside turned into a meteor shower!"
    show mi sad pioneer with dspr
    "Miku looked at them in frustration."
    mi "But what about the 'first pancake lumpy'? Shouldn't we do better next time?"
    show el normal pioneer with dspr
    me "Hopefully the quality of our broadcast tonight will ensure there won't be a next time."
    dv "Guh?"
    me "I'm saying Olga won't let us touch the microphone again."
    me "So keep your nose up, redhead! Until the end of the shift, you'll be spinning songs and doing nothing."
    show dv smile pioneer with dspr
    "Gleefully chuckling, Alisa got up from the table."
    dv "If that's the case, then we could have done worse! We obviously overdid it."
    show el surprise pioneer
    show mi upset pioneer
    with dspr
    "I laughed, catching the puzzled looks of Miku and Electronik."
    me "Let's go eat before the Hat thinks of leaving us without dinner as punishment!"
    $ volume(1.0, 'ambience')
    stop music fadeout 3
    return

label alt_day5_dv_dj_lunch:
    scene bg ext_clubs_day with dissolve
    play sound sfx_open_door_clubs
    play ambience ambience_camp_center_day fadein 2
    play music music_7dl["everyday"] fadein 3
    "When we left the club building, the sun was already shining brightly in the sky, glaring disgustingly at the eyes on all wet surfaces."
    show el smile2 pioneer with dissolve
    el "It's good that the rain is over!"
    "Electronik didn't just cross himself, squinting indignantly at the bright light."
    el "After a quiet hour, we can finally get back to business."
    show mi sad pioneer at right with dissolve
    "Miku looked a little upset."
    mi "Bad weather, it turns out, brings people together... Can't we get together as a whole squad without rain?"
    th "You can, dear, of course you can. But for some reason you don't invite Alisa and me!"
    "I thought, grinning evilly."
    show dv smile pioneer at left with dissolve
    "Alisa threw a sly look at me - she clearly shared my thoughts."
    scene ext_dining_hall_away_day
    show dv smile pioneer
    with dissolve
    me "There are only two things I want right now."
    dv "Soup and second?"
    me "Seeing Hat's face..."
    "I made a face of horror and lowered my voice to a whisper."
    me "...and to become invisible so that I never cross paths with her!"
    show dv grin pioneer with dspr
    "Alisa snorted, tossing her head in defiance."
    dv "What will she do to us? At most, confiscate the microphone."
    dv "She herself asked us to do this…"
    show dv normal pioneer with dspr
    "The girl stopped mid-sentence, noticing the formidable figure on the porch."
    scene bg ext_dining_hall_near_day
    show mt normal pioneer at right
    show dv normal pioneer at cleft
    with dissolve
    "Olga was waiting for us, pursing her lips and crossing her arms over her chest."
    mt "Congratulations on your first radio broadcast. First and last."
    me "Were we that bad?"
    show mt laugh pioneer with dspr
    mt "No."
    show dv surprise pioneer with dspr
    "Olga suddenly giggled, making us all look at each other in bewilderment."
    mt "There aren't any rains in the forecast for the rest of the shift, so I won't have to blush for you anymore."
    show mt smile pioneer with dspr
    "She smiled warmly, though the sly sparks still danced in her eyes."
    mt "Actually, you were great, thanks to everyone for the work!"
    mt "Go ahead and eat, I've covered it for you."
    hide mt with dissolve
    "Still unable to figure out what the catch was, our humble crew and I slipped into the dining room."
    stop ambience fadeout 1
    scene bg int_dining_hall_people_day
    show el think2 pioneer at right
    with dissolve
    play ambience ambience_dining_hall_full fadein 2
    el "She's not angry?"
    "Electronik asked stupidly, looking suspiciously at the door."
    show dv angry pioneer
    show el surprise pioneer
    with dissolve
    dv "Haven't you seen it yourself? She's happy with everything, fool!"
    "Alisa looked somewhat annoyed, and I understood her perfectly."
    show el sad pioneer
    hide dv
    with dissolve
    th "Just think - say something stupid live, go to the canteen, as if you're going to be executed, and receive only gratitude from your strict warden..."
    th "What a humiliation this must be for Dvachevskaya!"
    hide el with dissolve
    "A bunch of younger children had just finished their meal, and Alisa promptly grabbed her tray from the squad leader's kindly set table and plopped down into the vacant seat."
    "I shrugged guiltily and sat down next to her, leaving Miku and Syroezhkin alone."
    th "They are, of course, not bad guys, but I have to admit: they exhausted me a lot in the morning. I want a simple human meal in peace and quiet."
    show dv guilty pioneer with dissolve
    me "Bon appetit."
    dv "Uh-huh."
    "The redhead wearily sipped her soup, looking down into her plate."
    dreamgirl "Well, now it's just the two of you. Has she cheered up a lot?"
    th "She was just exhausted by the broadcast. I'm not in the mood to talk right now either!"
    dreamgirl "Well, well. Then why didn't you sit alone, you poor exhausted thing?"
    dreamgirl "Do you want to admire a nice picture?"
    th "As if there's anything shameful about it."
    dreamgirl "Absolutely nothing. She's not ashamed to slurp in your presence."
    th "I don't understand what you want from me?"
    dreamgirl "For the gifted, have you ever shown her that you like her as a girl?"
    dreamgirl "And you know you didn't. So don't expect her to be a telepath."
    "The annoying voice died out, and I again began to stealthily study Alisa."
    "Since yesterday, the red-haired beast has changed."
    "It was guessed not so much in what and how she said - rather in her lowered shoulders and an absent-minded look, which now and then faded into the void behind my back."
    if lp_dv >= 16:
        th "Maybe I should take the player away from her at least for the night?"
        th "She will drive herself into a coffin with these lack of sleep, and I will jump after her!"
    else:
        th "Have I gotten so sick of her these days that my company alone makes her yawn?"
    me "What are you planning to do during quiet hour?"
    "I inquired unobtrusively."
    show dv normal pioneer with dspr
    "Alisa shuddered, raising her dry red eyes to me."
    dv "What's supposed to be done. Sleep."
    hide dv with dissolve
    "She put all her dishes on a tray and got up from the table without honoring me with another word."
    "I looked after her for a long time, but the girl never turned around, as if completely forgetting about my existence."
    dreamgirl "What did you say about women and riddles?"
    th "Doesn't matter. But the lack of any coherent answers is starting to frankly piss me off!"
    dreamgirl "So go and ask - they don't take money for asking."
    th "In case you haven't noticed, Alisa doesn't seem very eager to have a heart to heart talk."
    dreamgirl "So you should find someone more talkative while she is sleeping. Why pull a cat…"
    us "Boo." with vpunch
    show us laugh sport with dissolve
    us "Seen Alisa?"
    if herc:
        "It cost me a lot of effort not to crack a small one on the head with a glass - sometimes the reflexes reminded me of themselves at the wrong time."
    else:
        th "Is sneaking up from behind a tradition in this camp?"
    me "She's in her cabin. Gone to sleep."
    show us upset sport with dspr
    "Ulyana, emerging from under my left side, twisted her face."
    us "The circumstances are extremely unfortunate."
    if loki:
        me "What circumstances?"
        show us grin sport with dspr
        us "I'll tell you if you come to the square!"
    show us smile sport with dspr
    hide us with moveoutleft
    "She gave me a cheeky wink before rushing to the door."
    "I just twisted my finger at my temple, as if Ulyana could see it."
    th "As soon as the older one stopped playing dirty tricks, how did the younger one start working for two?"
    th "Well, it's definitely not going to end well!"
    "I finished my kompot and got up from the table."
    "I had to decide where and how to kill a quiet hour."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_dv_dj_map_house_dv1:
    scene bg ext_house_of_dv_day with dissolve
    play music music_list["reminiscences"] fadein 3
    "If I wanted to talk to Alisa, then something inside told me that this was not the best time."
    "Since the morning she was in a very bad mood, so I risked finding myself with my head bitten off a second after I open my mouth in her presence."
    dreamgirl "Is that why you're sitting on the steps of her cabin right now?"
    th "That's why."
    "There were no sounds from inside, which was somewhat reassuring."
    "Or unnerving?"
    th "Okay, now or never!"
    th "If I don't get off the street, the squad leader who catches me will have too many questions that will be much harder to answer than the morning ones from the pioneers."
    play sound sfx_knock_door2
    $ alt_pause(0.2)
    "I knocked delicately on the door, expectedly getting no answer."
    me "Alisa?"
    play sound sfx_open_dooor_campus_2
    scene bg int_house_of_dv_day with dissolve
    play ambience ambience_int_cabin_day fadein 2
    "Sighing deeply, I went into the cabin - it was too late to retreat."
    scene cg d5_dv_sleep_7dl with dissolve
    "The redhead lay on her bed, curled up and facing the wall."
    "As I expected, in her hand she squeezed the player, and plugged her ears with headphones."
    th "Also listens to, I suppose, some Green Day - it's just right for her age!"
    "Alisa's eyes were closed, but a barely noticeable crease between her eyebrows indicated that the girl was not sleeping."
    stop music fadeout 5
    "I carefully sat down on the edge of the bed."
    th "Maybe to hell with it?"
    th "I'll just go to bed and not disturb her."
    play music music_7dl["uneven_me"] fadein 4
    show cg d5_dv_sleep2_7dl with dissolve
    "But Alisa opened one eye and frowned a little harder when she met my eyes. She pulled out one earpiece."
    dv "What do you want?"
    "Well, what could I say to that?"
    me "Nothing."
    me "I didn't want to sit in the cabin for the entire hour. Would you mind if I stayed here with you?"
    dv "Only if you're not afraid to hear me snore."
    show cg d5_dv_sleep_7dl with dissolve
    "She closed her eyes again and moved closer to the wall, as if inviting me to lie down next to her."
    show cg d5_dv_sleep_together_7dl with dissolve
    "I rested my head warily on the edge of the pillow, still unsure if I was doing the right thing."
    "A shiver ran through my body as Alisa's warm fingers found my palm."
    show cg d5_dv_sleep_together2_7dl with dissolve
    "I barely suppressed a gasp of astonishment, but she only shoved the second earpiece into my hand, after which she crossed her arms over her chest, resting her elbow on my side."
    show cg d5_dv_sleep_together3_7dl with dissolve
    "I squinted at her calm face - fortunately, the girl's closed eyes allowed a little to admire this rare moment of peace."
    th "She seems so independent and indifferent to everything that surrounds her, but at the same time, the pain that she carries with her all these years is visible to the naked eye."
    th "And why did she start whipping over the edge today?"
    dreamgirl "Don't you think you're making this up yourself?"
    dreamgirl "Knowing that a person has had some shit in the past, you begin to involuntarily see his reflection in everything connected with this person."
    dreamgirl "Baader-Meinhof phenomenon, have you heard of this?"
    th "Then why did she react so strongly yesterday to my offer to feed her?"
    dreamgirl "It was embarrassing to take food from what she called a mama's boy."
    dreamgirl "Don't try to see more than what you're shown. It could end up being pretty bad."
    dreamgirl "Think things up, and then get disappointed when you don't find them."
    "Radiohead howled peacefully in the headphones, and the sun outside the window seemed to have faded."
    th "It's more boring than I ever thought, just lying next to the girl you like."
    "Alisa had already stopped tossing and turning, and I could hear her quiet sniffling."
    "Through the shirt, I felt the heat from her shoulder, and even distinguished a barely perceptible steady heartbeat."
    th "Or is it my own?"
    "She was so close - right next to me, and I could easily touch her cheek with my hand if I had a modicum of more determination."
    th "It sucks to feel that way, not being able to touch someone that makes you feel like you're insane, your knees are shaking."
    th "And this feeling is not only about physical interaction. Literally everything related to Alisa is saturated with it. Every breath, every look, every word that I utter in her presence."
    th "It's like she's surrounded by thorn-studded stalks, and any attempt to get close cuts me sharply, leaving a painful, bleeding wound."
    th "After that, the stems will only intertwine tighter, hiding her from my eyes and forever depriving me of the opportunity to admire Alisa at least from afar."
    "The girl shifted, nuzzling my shoulder."
    "I easily, barely touching her skin with my fingertips, removed a strand of hair that had fallen over my eyes."
    th "I wonder which one of us is acting seventeen now?"
    "I chuckled softly, closing my eyes and trying to drown out the thoughts in my head with the music."
    "Yes, only dull motives most opportunely contributed to these senseless walking around the bush."
    th "Damn it, I can't even think about getting close to Alisa!"
    "Millimeter by millimeter, I turned my head to feel her hair tickle my face - shameful desire, almost teenage."
    th "Let me get closer!"
    th "Let me touch!"
    th "Let me dissolve into this longing with you, and not just stand on the shore and watch you slowly sink!"
    "Everything inside me screamed, making my heart clench in despair."
    "But Alisa's face remained the same impenetrable."
    "Her breath burned my shoulder, and I was afraid to move, so as not to deprive myself of at least this ridiculous intimacy."
    "I felt a strand of her hair in the corner of my lip and inhaled noisily, greedily absorbing a barely noticeable bitter aroma, trying to remember it with every cell of my body."
    "The mind drew a variety of pictures. From the completely obscene to the enthusiastically beautiful, weightless, impossible even in the quietest art-house films."
    scene bg ext_khruschevka_sunset_7dl
    show prologue_dream
    $ set_mode_nvl()
    "It's as if we are wandering somewhere along the broken districts, and Alisa has such lively and burning eyes, as if all the life of this universe was concentrated only in them."
    "It's like she's talking, talking, talking, and I can't even make out what - too mesmerized by the overflowing of her intonations, melodic, hoarse and just a little dreary."
    "It's like I'm pressing her against a cold, damp wall, blowing her cheek with my out of breath - hot, impatient, obscene. And she only tilts her head to one side, dutifully surrendering herself to my power."
    "As if…"
    nvl clear
    $ set_mode_adv()
    stop music fadeout 3
    scene black with clock_r
    $ alt_pause(1.0)
    scene cg d5_dv_sleep_together2_7dl with dissolve
    us "Now what the hell are you two doing in here?"
    play music music_list["timid_girl"] fadein 3
    me "Huh?"
    scene bg int_house_of_dv_day
    show us normal sport at right
    show dv closed_eyes pioneer2 close at left
    with dissolve
    "I reluctantly lifted my head, trying to understand where I had drifted."
    "And only Alisa's sleepy eyes, on the contrary, made me shudder, throwing off the remnants of sleep from me."
    hide dv with hpunch
    "My hand was on her waist and I hurriedly pulled her away as I jumped out of bed."
    me "Kid, you..."
    show us smile sport at right
    us "I live here, yeah. Would you like to come out?"
    us "I need to change!"
    show dv sad pioneer2 at left with dissolve
    "Glancing at Alisa again - she had already sat up on the bed, sleepily rubbing her eyes - I hastened to retreat from the cabin of the red beasts, diligently ignoring Ulyana's cunning squint."
    play sound sfx_close_door_1
    scene bg ext_house_of_dv_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    th "I had a great sleep. {w}I hope it doesn't occur to Alisa to thrash me for this after the fact..."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_dv_dj_map_square1:
    scene bg ext_square_day with dissolve
    "Be that as it may, curiosity turned out to be stronger than a healthy fear of getting into trouble, so I was hardly surprised when my legs themselves led me to the square."
    play sound sfx_punch_medium
    "And I immediately caught a pinecone with my back." with vpunch
    th "Does she carry a whole bag of them with her?"
    dreamgirl "Any idea where she's hiding it?"
    us "Ps, over here!"
    "Ulyana called me from the bushes, and I obediently moved towards her in the shelter."
    play music music_list["i_want_to_play"] fadein 3
    $ renpy.show("bg ext_square_day", what = Notch("bg ext_square_day"))
    show us smile sport close
    with dissolve
    me "Well, what do you want?"
    "The child beamed, predatorily looking around the square from behind the branches."
    us "Now, now. According to my intelligence, our operation will be ready in about ten minutes."
    th "What is she talking about?"
    us "Olga Dmitrievna will go to the kitchen, give orders about potatoes. Viola will go to the infirmary, she stayed up in the canteen today with Katushka."
    us "Then it will be possible to start!"
    me "Start what?"
    show us shy sport close with dissolve
    "Ulyana suddenly averted her eyes, blushing deeply."
    us "Well, you see…"
    us "Yesterday, after dinner, I was very angry with everyone, so I decided to play a joke - they will punish me anyway, I have nothing to lose."
    me "Get to the point!"
    "Taking a deep breath, Ulyana blurted out:"
    show us shy2 sport close with dissolve
    us "Panties."
    me "Huh?"
    "Stupidly I asked, staring blankly at the girl."
    us "I replaced the flag with Liska's panties."
    show us laugh sport close with dissolve
    "It seems that my face was noticeably distorted by this information - Ulyana giggled, ceasing to be embarrassed in a second."
    th "I wonder if that's the reaction she expected from everyone in the lineup?"
    dreamgirl "What a smart girl, unlike some!"
    dreamgirl "This way we'll see them at least once before the shift ends..."
    us "But, as you know, there was no lineup, and they didn't punish me either. So I thought..."
    me "Was this your conscience finally speaking up?"
    show us laugh2 sport close with dissolve
    "Ulyana snorted happily."
    us "Nope!"
    us "It's just that if Olga Dmitrievna understands that it's me, I'll get a hundred pounds. And she will understand, it doesn't take much intelligence."
    me "Does Dvachevskaya know that her underwear almost became public?"
    us "Actually, no. And you won't tell her anything!"
    me "What if I do tell her?"
    show us normal sport close with dissolve
    us "Then I'll tell her that you were the one who stole her panties."
    "The girl shrugged innocently."
    show us grin sport close with dissolve
    "And then slyly narrowed her eyes and added:"
    us "Who do you think she'll believe: her best friend or some perverted crook?"
    th "You little shit!"
    me "What tendencies did you find in me?"
    show us smile sport close with dissolve
    us "You think I didn't see you peeking at her in the infirmary?"
    me "That wasn't what you thought!"
    us "Just make excuses. I can see through people like you."
    us "So let's make a deal: you help me now, and I will be silent as a fish!"
    us "I don't need much from you - just stand on the lookout in case anything happens."
    show us grin sport close with dissolve
    "Her face shone with contentment, and I felt like a complete fool."
    th "Just shine. I fell into the clutches of a cunning child, capable of leaving Satan in debt!"
    th "Or is she just avenging my jokes from yesterday?"
    dreamgirl "That's how the karma police works, in case you didn't know."
    dreamgirl "Yesterday was fun for you, and today for her. Look how she grins!"
    play sound sfx_hiding_in_bush fadein 0
    show us normal sport close with dissolve
    "But suddenly the girl abruptly quieted down, looking out from behind the bushes."
    stop sound fadeout 1
    us "Olga has already turned to the canteen, Viola is also leaving. Now they will be out of sight, and then..."
    show ba normal uniform at fright with dspr
    "What would happen then, I never found out - Ulyana fell silent mid-sentence, peering with horror at the overweight figure on the horizon."
    us "I didn't take this into account..."
    "She muttered, biting her lip."
    "Indeed, the physical education teacher did not appear in any way in her insidious plans. And he was heading not just somewhere, but straight for the flagpole!"
    me "What are we going to do? He's clearly not going there just like that."
    show us dontlike sport close with dissolve
    us "Even a fool understands this!"
    "Ulyana hissed with irritation."
    us "Distract him!"
    th "AW HELL NO!"
    "Sanich was the last person in this camp with whom I wanted to contact, albeit under the threat of being unfairly accused of perverted inclinations."
    th "Nothing personal, child, I just value my skin a little more than yours!"
    me "You'll do much better."
    show us surp1 sport at left with vpunch
    play sound sfx_punch_medium
    play music music_list["always_ready"] fadein 3
    "With these words, I pushed her out of the bushes straight into the square."
    show us dontlike sport at left with dissolve
    us "You…"
    show ba em1 uniform at right with move
    ba "Why aren't you in your house? I thought the quiet hour was announced?"
    "Ulyana froze in a stupor while I giggled nastily behind her back."
    dreamgirl "Laugh, laugh. She'll go now and tell the physical teacher what you did with her in these bushes..."
    show us angry sport at left with dissolve
    us "Uncle Borya, there ..."
    us "Olga Dmitrievna was looking for you!"
    show ba evil uniform at right with dissolve
    ba "Why is that? She only came up to me during dinner, and asked me to raise the flag!"
    show us calml sport at left with dissolve
    "He frowned in disbelief, and Ulyana shifted awkwardly in place, wringing her hands behind her back."
    us "I don't know, maybe we need some help with the potatoes..."
    "Ulyana, without turning around, showed me her fist, making me laugh more than ever - with improvisation, she was so-so."  
    show ba normal uniform at right with dissolve
    ba "Of course, she always thinks of something dumb!"
    "Sanich snorted."
    ba "So it's gonna go like this: I'm delegating raising the flag to you, since you're hanging around here anyway."
    ba "And right after that, march to the cabin!"
    show us laugh sport at left with dissolve
    us "Hurrah!"
    us "Thank you, Uncle Borya!"
    show ba smile uniform at right with dissolve
    "Ambal warmly grunted - apparently he decided that Ulyanka considered it an honor to complete such a responsible task as raising the flag."
    hide ba with dissolve
    "With heavy steps, he retired to the canteen, along the way muttering something under his breath."
    scene bg ext_square_day with dissolve
    show us upset sport with dissolve
    "I came out of my hiding place, still chuckling. The girl grunted offendedly and leaned towards the flagpole."
    show us dontlike sport with dissolve
    us "That's bullshit!"
    me "What happened?"
    us "They got wet in the rain and won't come loose!"
    show us angry sport close:
        ypos 1.1
    with dissolve
    "Approaching her, I saw a very unattractive picture - a dirty and wet rag resemblng an item of lingerie very remotely laid next to a red banner."
    me "Maybe it's easier to cut them? Do you have a knife?"
    show us calml sport close with dissolve
    us "Definitely not!"
    "Ulyana pouted."
    show us upset sport close with dissolve
    us "This is damaging someone else's property!"
    th "What words she sang about!"
    th "Didn't she learn the word 'theft' at school?"
    me "Then would you kindly move over, thank you. The last thing we need right now is PE teacher also finding me here!"
    th "I've never felt so heroic about acquiring women's panties..."
    dreamgirl "Would you keep them as a trophy?"
    th "Yeah, I'll hang them on the wall."
    th "I'll show Olga and say, look how cool, you don't have such!"
    "Somehow untying the knot, I straightened up, proudly raising the looted item above my head."
    show us fear sport close:
        linear 0.3 ypos 1.001
        linear 0.3 ypos 1.1
        linear 0.5 ypos 1.1
        linear 0.3 ypos 1.001
        linear 0.3 ypos 1.1
    "Ulyana waved her hands in panic and rushed towards me, trying to grab the unfortunate piece of clothing."
    us "What are you doing? What if they see you?"
    show us calml sport close:
        linear 0.3 ypos 1.001
        linear 0.3 ypos 1.1
    me "And everyone would have seen it if it hadn't rained this morning!"
    show us calml sport close:
        linear 0.3 ypos 1.001
        linear 0.3 ypos 1.1
    "I deftly dodged another attempt by Ulyana to jump to my hand."
    us "Give it back!"
    me "And you take it away!"
    show us normal sport with dissolve
    "The girl ran back a couple of steps to gain momentum, but immediately stared in a panic towards the canteen."
    show us surp2 sport with dissolve
    us "Dammit! Uncle Borya is coming back!"
    scene bg ext_houses_day at running
    "Literally in two jerks, raising the flag and almost breaking the cable at the same time, Ulyana ran towards the houses, pulling me along with her on the go."
    me "Hey! We're real bandits!"
    "I shouted, waving in all directions the artifacts we had obtained."
    me "Fear every mortal who stands in our way!"
    scene bg ext_washstand_day with dissolve
    show us angry sport with dissolve
    stop music fadeout 3
    us "Can you not yell?"
    me "But then they won't be afraid!"
    show us laugh2 sport with dissolve
    play music music_list["timid_girl"] fadein 3
    "We slowed down at the washstands. I leaned against a tree, shaking with laughter, and Ulyana, unable to stand it, joined me, laughing loudly."
    show us smile sport with dissolve
    us "Damn you're good!"
    "She squeezed out enthusiastically through her tears."
    me "And you thought!"
    "I proudly tossed my head."
    "There was only one hitch left."
    me "Alisa should be given back what is rightfully hers..."
    show us sad sport with dissolve
    "Ulyana immediately became serious."
    us "I'll slip them over to her tonight when they're dry. She won't even notice."
    "I arched an eyebrow, lifting the wet cloth up to her face."
    me "Have you seen the state they're in? In your opinion, Alisa is either blind or a pig who makes everything look like this!"
    show us normal sport with dissolve
    us "Well, wash them!"
    me "Why is it just me?"
    th "First the adult hazes me, and now the kid. Not a camp, but a correctional colony!"
    us "I don't want to!"
    me "And I'm all burning with impatience!"
    me "You've made this mess, you're the one to clear it up."
    show us smile sport with dissolve
    "A little hesitant, Ulyana held out her fist to me."
    us "Rock-paper-scissors!"
    "…"
    me "Actually, the first round is scissors!"
    "…"
    if karma <= 0:
        th "What did I even expect with my karma?"
    show us grin sport with dissolve
    "Ulyana giggled, covering my fist with her palm."
    us "Go ahead, raccoon!"
    play sound sfx_open_water_sink
    play sound_loop sfx_water_sink_stream fadein 1
    scene bg ext_washstand2_day with fade2
    "In disgraceful acknowledgment of my defeat, I turned off the faucet. Washing in ice water did not seem to me to be at all pleasant."
    th "I hope they were clean at least before they hit the flagpole..."
    us "Wash, wash. They should dry before evening!"
    me "How can I do laundry without powder?"
    us "Diligently, very diligenty!"
    th "Not to say that this is the first time I have faced such a task - everything has happened in my life - but under such circumstances..."
    scene bg ext_washstand_day with dissolve
    stop sound_loop fadeout 2
    "After five minutes of punitive washing, my fingers hardly moved, but the panties acquired an almost marketable appearance."
    "I handed them to Ulyana, praying to all higher powers that they would not fall out of my hardened hands onto the washed out clay."
    me "Where are you going to dry them?"
    show us normal sport with dissolve
    us "I'll hang them behind the house."
    "I remember that it was there that I caught Alisa on that ill-fated day when my almost settled life in the camp decided to turn upside down."
    "I shook my head."
    me "It's better to hang outside the territory, well, or near warehouses. Only preferably in the sun."
    "Ulyana nodded."
    us "Will do!"
    hide us with moveoutleft
    "And sped away somewhere to the houses, without even saying goodbye."
    th "And they say you should help women!"
    dreamgirl "Especially redheads."
    th "That's right. And we have a fire just in the evening..."
    "I trudged into the house, simultaneously trying to move my fingers through the pain and agony."
    "After all these adventures, I wanted only one thing - to lie down in peace and quiet for at least an hour."
    stop music fadeout 3
    return

label alt_day5_dv_dj_map_library1:
    scene bg ext_library_day with dissolve
    "I wandered along the shady paths, wondering where to go. No ideas came to mind."
    th "Walk like this all the quiet time - will fly in a hat from Olga for sabotaging the daily regimen. She'll probably push work onto me too, she always has it... "
    dreamgirl "So you should've gone and slept! The redhead probably already warmed up a place for you!"
    th "She'll only hit me on the knee. She loves it."
    dreamgirl "Aren't you a masochist? I thought you liked it last time..."
    dreamgirl "Oh, look who's coming here!"
    th "Damn it!"
    show mt angry pioneer far at left with dissolve
    "Olga herself was heading straight towards me. I didn’t know what kind of fly had bitten her during lunch, but the squad leader’s face even from afar looked excessively severe."
    th "We should get the hell out of here, quick!"
    "The only escape route was the library, and I immediately slipped inside."
    play sound sfx_open_door_1
    stop ambience fadeout 1
    $ alt_pause(1)
    scene bg int_library_day with fade
    play ambience ambience_library_day fadein 1
    if ('library' in list_voyage_7dl):
        th "It is hardly worth seeking salvation in this abode of evil, but between an angry leader and an angry librarian, the choice is clearly not in favor of the first!"
    "The librarian's desk was empty, and I cautiously examined the shelves: oddly enough, no one wandered between them either."
    th "But if the Beetle isn't here, why is the door open?"
    stop music fadeout 2
    un "Zhenya?"
    if ('library' in list_voyage_7dl):
        "I heard a slightly frightened voice from the editorial office."
    else:
        "A slightly frightened voice came from behind the door to my left."
    play music music_7dl["take_my_hand"] fadein 2
    show un surprise pioneer at fleft with dissolve
    "Lena, who looked out, gasped, barely noticing who exactly was standing in front of her."
    un "Did you want to borrow a book?"
    me "Uh…"
    "For some reason I did not dare to lie."
    me "No. Just hiding from the squad leader."
    show un smile pioneer at fleft with dissolve
    "Lena smiled shyly, opening the door wider."
    un "You can sit here for now if you want."
    "It was impossible to refuse such a tempting offer, and I joyfully proceeded to Lena."
    play sound sfx_open_dooor_campus_1
    $ alt_pause(1)
    scene bg int_editorial_day_7dl
    with dissolve
    show un normal pioneer with dissolve
    if ('library' in list_voyage_7dl):
        me "Where are your colleagues?"
        un "Busy in their main club."
    else:
        me "It's cozy in here. What is this secret place?"
        un "Editorial office of the camp newspaper. I draw here, and Seryozha and Sasha write articles."
        un "Although, today they decided to spend the rest of the day in the clubs, because yesterday's work with the newspaper took them a lot of time."
    un "But I was instructed to collect all the remaining materials and conduct an inventory check."
    "The girl waved her hand at the mountains of rubbish behind her back. She had already organized some of the materials: all the pencils and brushes lay in neat bundles, tied with elastic bands, and next to them was a neat stack of some magazines."
    me "Can I help?"
    show un sad pioneer at vpunch, center
    "Lena shuddered and stared out the window, biting her lower lip."
    scene bg int_editorial_day_7dl
    show un sad pioneer
    un "Don't…"
    un "It's not much work, really. I can handle it."
    show un sorrow pioneer:
        linear 0.5 ypos 1.2
    "As if to confirm her words, she began to fuss, squatting down and starting to roll up large scraps of whatman paper into a tube. Her fingers trembled, and the paper fell awkwardly to the floor from the girl's hands."
    th "Does she dislike my company?"
    dreamgirl "Why no! She's just dreaming about you hanging around with her for two hours straight, watching her work intently."
    "I sank down in front of Lena, taking the drawing paper from her and folding it into an even scroll in one motion."
    show un shy pioneer:
        linear 0.5 ypos 1.0
    "The girl blushed, lowering her eyes to the floor."
    un "Thank you."
    "There was an awkward pause. It was not easy to talk to an unsociable girl - I knew firsthand."
    th "Remember that stupid breakfast..."
    "In order to somehow distract myself, I reached for a pile of drawings piled up nearby, and began to carefully align it, as if this activity was in any way useful for cleaning up this chaos."
    me "You know, it's been so long since I've been to camp that I forgot how busy it gets around the end of my shift."
    show un sad pioneer with dissolve
    un "I know."
    "Lena whispered softly, smiling sadly with only her eyes."
    th "Is it just me, or are there tiny beads of unshed tears in their corners?"
    un "I've been here for three years. {w}As a child, I dreamed of going here with Alisa, but my father was against it. He was afraid that something would happen to me."
    dreamgirl "Wow! Did you hear that?"
    th "Unbelievable! She squeezed out more than three words at once!"
    dreamgirl "Maybe she can even keep up the conversation instead of just blurting out something to get you off the hook?"
    th "I propose to arrange a sweepstakes."
    dreamgirl "I'll bet she'll be rewired and she'll shut up for the rest of the quiet hour."
    th "I don't even know..."
    th "Do you have a coin?"
    show un normal pioneer with dissolve
    stop music fadeout 3
    "Taking courage, Lena looked up at me."
    play music music_7dl["you_are_soul"] fadein 5
    un "Did Alisa tell you about this?"
    if not alt_day4_dv_dj_un_dv_question:
        un "We're in the same class with her after all, we've been together since childhood."
    "The girl continued to glare at me, causing an unbearable desire to crawl back to the door and rush away from this interrogation room."
    me "Well, actually…"
    me "She did. She's been going to the camp for as long as she can remember, and all that."
    th "What does she want from me?"
    show un smile pioneer with dissolve
    "Lena suddenly smiled, making me feel more uncomfortable than ever before."
    un "Did she tell you what happened in 1981?"
    "I mentally made complex calculations. According to the data I have, Alisa was eight at the time."
    show un normal2 pioneer with dissolve
    un "She and her parents moved to the appartment next to ours."
    th "So this was her first summer with foster familiy?"
    un "I'm afraid you won't be so interested in all the details of our girlish and naive friendship, but I still remember one act of hers every time, when it seems to me that the whole world has turned its back on me."
    "Lena pursed her lips and began to twist a glass of pencils in her hands. I nodded, showing my interest. In an attempt to occupy my hands, I began to mindlessly put inventory into an empty cardboard box."
    un "We quickly became friends. Alisa was good at making up stories, and I was good at putting her fantasies on paper."
    un "One album, stubs of pencils and whole worlds that we ran into, hiding from everyone in the world."
    un "And then she went to Sovyonok. Her parents said it was necessary for..."
    show un sorrow pioneer with dissolve
    "The girl looked down at the floor, frantically searching for the right words."
    me "Acclimatization?"
    show un surprise pioneer with dissolve
    "I helped her. Lena sighed in astonishment, rounding her eyes."
    me "I know about the situation in Alisa's family. She told me yesterday."
    me "So what happened when she left for camp?"
    show un normal2 pioneer with dissolve
    un "We agreed that every day we would continue to invent our common history so as not to lose it. And, as I understand now, not to lose each other either."
    un "But when we met again three weeks later, it turned out that our stories went completely different ways. That evening we had a terrible fight."
    un "I cried for half the night thinking we'd never be friends again."
    show un sad pioneer with dissolve
    "Sighing heavily, Lena dumped all the newspapers and magazines into the second drawer, which she had previously pointlessly aligned on her lap."
    show un normal2 pioneer with dissolve
    un "And three days later, Alisa came to me. She said that she didn't care about anything and she agreed with my story, and she tore up her album and threw it away."
    un "And even refused a ticket to another camp, so as not to leave me alone again!"
    show un sad pioneer with dissolve
    "Lena's voice trembled."
    un "She gave up what she held dear, and it was because of me, you know?"
    "Of course, I understood what she was trying to convey to me. But it was difficult for me to appreciate this sacrifice, both due to my advanced age and due to a vague understanding of the context."
    me "But you don't talk much these days."
    show un sorrow pioneer with dissolve
    "That wasn't a question. Lena nodded, lowering her head."
    show un normal2 pioneer with dissolve
    un "Sounds funny, but it happened just like that summer. Our paths parted, as did the continuation of that story."
    stop music fadeout 3
    un "But I owe... I can't help but repay her for what she did for me that summer."
    show un serious pioneer with dissolve
    play music music_7dl["to_the_sunrise"] fadein 3
    "The girl raised her eyes to me. Dry, clear, serious to the point of convulsive pain in that empty place where the heart should have been."
    un "So I beg you: until the end of this shift, until we get off the bus in the city, don't talk to me."
    un "Don't look for a meeting, don't nod when you notice - or better yet, don't look at all!"
    "Unable to stand it, she turned away, covering her mouth with the back of her hand."
    show un sad pioneer with dissolve
    un "{alpha=*0.5}Leave.{/alpha}"
    "The latter passed my ear in a low whisper, which seemed to not want to be heard. But, unfortunately or fortunately, I made out her quiet request."
    th "So you do for her what she once did for you?"
    "I smiled sadly with only the corners of my lips, rising from the floor."
    th "This is the most extravagant confession. But also - to be honest - the most elegant."
    show un sad pioneer far with dissolve
    "Lena stayed behind like a proud lady from old novels. Thin, delicate, but strong enough to rein in herself."
    me "I'm leaving."
    "The answer was a short nod - the girl did not trust her voice, and I understood her perfectly."
    me "Good luck."
    stop music fadeout 3
    play sound sfx_open_dooor_campus_1
    $ alt_pause(1)
    scene bg int_library_day with dissolve
    scene bg ext_library_day with fade
    play ambience ambience_camp_center_day fadein 3
    "Getting out of the library into the fresh air, I cheerfully shook my head, as if trying to get this chaotic scene out of my head."
    "Not thinking of anything smarter, I trudged to the cabin - to sleep."
    th "Of course I have something to think about..."
    th "But I'll think about it tomorrow."
    stop ambience fadeout 1
    return

label alt_day5_dv_dj_map_musclub1:
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_musclub_day with dissolve
    "No matter how hard I tried to pretend that I was just walking, I could not stop thinking about the ultimate goal of my route."
    th "Wandering around the camp for two hours under the scorching sun is a dubious pleasure. And stumbling upon a squad leader who always has a job in store for her beloved pioneer…"
    "Squinting from the blinding sun, I looked ahead: someone was sitting on the steps of the music club."
    stop music fadeout 3
    th "Nobody randomly comes here. There is only one option left then..."
    show mi smile pioneer far with dissolve
    play music music_7dl["what_am_i_doing_here"] fadein 1
    mi "Semyon!"
    "Joyfully, as if meeting an old friend in an unfamiliar place, I rushed to the Japanese girl."
    th "I don't think she's going to offer me any incredible entertainment, but she'll definitely brighten up my leisure time!"
    me "Hello, hello. Sunbathing?"
    show mi grin pioneer with dissolve
    "I sat down on the heated boards next to the girl. She seemed to be really trying to relax: throwing her head back, Miku stretched out her thin legs, as if exposing herself to the sun."
    th "Did you get cold in Japan?"
    dreamgirl "More like in her working dungeon. Don't you know that in her homeland the heat is worse than ours in summer!"
    show mi normal pioneer with dissolve
    mi "I'm gathering my strength for an important task. The morning broadcast was wonderful, don't think it, but it threw me off a bit."
    th "She even talks slowly!"
    "I squinted at the girl, trying to figure out what the catch was."
    me "And what kind of task is this?"
    mi "We need to get the costumes in order for tomorrow's concert. Iron something, hem something - after yesterday's concert it's such a mess, you should have seen it!"
    mi "They put everything on carefully, but they take it off..."
    show mi serious pioneer with dissolve
    "Miku straightened up, staring thoughtfully at her knees."
    mi "By the way, what about Alisa?"
    th "I wish your talent for changing the subject so easily and naturally!"
    me "She went to bed."
    if lp_dv < 16:
        me "She's not feeling too good."
    else:
        me "Apparently now she listens to music instead of sleeping at night. Soon I'll take this player away from her!"
    show mi upset pioneer with dissolve
    mi "Ah, so that's it?"
    "There was concern in Miku's voice."
    mi "You know, I have never seen her as exhausted as today. Sometimes she did not get enough sleep, but on such days she usually snapped at everyone, like a dog, but to be sad..."
    mi "I never saw that."
    "The girl got up from the steps, dusting off her skirt."
    show mi smile pioneer with dissolve
    mi "Perhaps it's time to get to work. If you want, you can sit with me, it's always more fun together!"
    th "Sit like a useless sack in the corner? No thanks!"
    "I wasn't a pro at sewing and ironing, so I just shook my head."
    me "Thanks for the offer, but I'll go. A little peace and quiet never hurts."
    show mi smile pioneer far with dissolve
    $ alt_pause(0.2)
    hide mi
    play sound sfx_close_door_1
    with dissolve
    "Smiling charmingly, Miku hid behind the door. I trudged into the house."
    scene bg ext_houses_day with slideawayright
    stop music fadeout 4
    th "So I'm not the only one who thinks there's something wrong with Alisa?"
    play music music_list["your_bright_side"] fadein 3
    "That was concerning. Miku was clearly not the first candidate for the top most insightful people in this camp."
    dreamgirl "Maybe there's something wrong with all of you?"
    dreamgirl "Or do you every time you see a person in a bad mood, call him a brigade from a psychiatric hospital, so that he would be drugged with haloperidol as soon as possible?"
    dreamgirl "First look in the mirror at your gloomy face, and only then tell others that they are not funny enough and spoil your mood with their appearance."
    th "Only you spoil my mood."
    scene bg ext_house_of_mt_day with slideawayright
    $ alt_pause(0.2)
    stop ambience fadeout 2
    scene bg int_house_of_mt_day
    with dissolve
    play sound sfx_unlock_door_campus
    $ alt_pause(0.5)
    play ambience ambience_int_cabin_day fadein 2
    "I made my way to the house: Olga, fortunately, did not like to spend a quiet hour in my company, so my haven was empty."
    th "Oh, but if I were really seventeen, I would gather the whole squad here to play cards..."
    th "What an adrenaline rush - gambling at a quiet hour, and even in the squad leader's house!"
    th "But I'm not seventeen, and there are only one or two players here."
    stop music fadeout 5
    "I collapsed onto the bed. My eyes slowly closed, letting my exhausted body drift off to sleep."
    stop ambience fadeout 3
    show blink
    $ alt_pause(0.2)
    scene anim_digi with fulldiam
    play music music_7dl["catalyst"]
    show prologue_dream
    $ set_mode_nvl()
    "{i}God bless each of us,{/i}"
    "{i}We are a broken people living at gunpoint.{/i}"
    "{i}And this cannot be overcome, not changed.{/i}"
    "{i}And this cannot be surpassed, cannot be avoided.{/i}"
    nvl clear
    $ alt_pause(1)
    scene cg d5_dv_dream_7dl with fulldiam
    show prologue_dream
    "I see a ruined cemetery under a ruined sky, as if the chessboard on which God played his cruel game turned over to the ground."
    "And along the wreckage of this board with a cannon at the ready, Miku walks in a fluttering black cloak."
    "{i}Another Miku. {w}Not like I remember her.{/i}"
    "The other Miku stops, looking ahead. {w}I look with her - at the horizon, which is hidden by the ruins of the dilapidated castle."
    "And she jumps down, into the void, into the abyss, and I want to scream, I want to beg her to stop this crazy flight, but I am assigned only the fate of a weak-willed observer."
    "Where she so desperately seeks, she is not expected at all. {w}But the other Miku stubbornly holds out her hand, offers it free of charge, thoughtlessly."
    "{i}She can offer at least all of herself - she hasn't had nothing to lose for a long time.{/i}"
    nvl clear
    $ alt_pause(1)
    "Punch from the left. {w}Punch from the right. {w}An answer as biting as the other Miku's rude intrusion into this abode of human despair."
    "{i}The other Alisa doesn't look like a person who would accept a helping hand.{/i}"
    "And the other Miku rises from the ashes again and again, she does not even think of giving up. She came here with only one goal - the most important and the last in her life."
    "{i}And I know for a fact that she won't agree to leave with nothing.{/i}"
    "The other Alisa advances, and advances, and advances, without slowing down. Her rage is growing."
    "{i}Her scythe is as sharp as...{/i}"
    "{i}What{/i}?"
    "{i}Can't remember.{/i}"
    nvl clear
    $ alt_pause(1)
    "The rumble shakes the walls, they are about to collapse, and I join my palms in prayer that they will not last long."
    "A sharp swing of the scythe - and the chessboard breaks in two, with a creak, with a crack, but still withstanding that touch of its former greatness."
    "And Miku is already flying into the abyss. {w}Another Miku from another world, where she had the courage to demand something."
    "{i}Demand that someone grabs the outstretched hand.{/i}"
    nvl clear
    $ alt_pause(1)
    "Each shot another Miku misses. Each blow only provokes, turns on, causes a sharp, painful desire in another Alisa."
    "{i}Admit it, you just love hurting others?{/i}"
    "Her weapon is chains. The rusty and probably sharp edges of their ugly links."
    "Other Miku's hands are tied. She is powerless."
    "{i}I don't want to watch you lose!{/i}"
    "But she can't be broken so easily. Like a phoenix, she is reborn again, comes to life, breaks free."
    "{i}And she'll definitely break out.{/i}"
    "She breaks out..."
    nvl clear
    $ alt_pause(1)
    "{i}God saves each of us,{/i}"
    "{i}Will we burn in the fire of a thousand suns?{/i}"
    "{i}For the sins of our hands, our tongue,{/i}"
    "{i}For the sins of our fathers,{/i}"
    "{i}For the sins of our youth?{/i}"
    stop music fadeout 3
    play ambience ambience_int_cabin_day fadein 2
    scene bg int_house_of_mt_day
    show unblink
    with dissolve
    $ alt_pause(0.5)
    $ set_mode_adv()
    show mt angry pioneer with dissolve
    mt "Get up!"
    me "Huh?"
    mt "You'll sleep through lunch."
    hide mt with dissolve
    "Olga left the house, and I again collapsed onto the bed, staring in bewilderment at the sloping ceiling."
    "They told me in my youth: there’s nothing to watch your Chinese porn cartoons all day long..."
    th "What a crazy dream!"
    "I rubbed my eyes and left the house. An afternoon snack would be very welcome."
    return

label alt_day5_dv_dj_map_cyber_club1:
    scene bg ext_clubs_day with fade
    play ambience ambience_camp_center_day fadein 1
    play music music_list["i_want_to_play"] fadein 3
    scene bg ext_clubs_day with dissolve
    "Aimlessly wandering along the houses, I hastened to leave for more neutral territory in order to avoid the temptation to look at Alisa."
    if lp_dv < 16:
        th "Who knows, what if she bites my head off..."
        dreamgirl "As if she showed a clear desire to mate with you!"
        th "What?"
        dreamgirl "What?"
    else:
        th "If she really just didn't get enough sleep, then why disturb her?"
        "She wasn’t hired as a nanny or animator to tirelessly entertain a bored kid, exhausted by the sun and an abundance of free time?"
    "I stopped at the clubs, looking thoughtfully at the gates of the camp."
    th "On the one hand, I could explore the area - you never know what surprises this forest hides besides the treehouse?"
    th "On the other hand, the prospect of being devoured by local mosquitoes right now, when in the evening there is a planned feeding of the wild inhabitants of the forest by our entire small society, does not warm the soul in the slightest..."
    "Sighing heavily, I went up to the porch."
    th "Still, sitting in the radio room and meditating is the only reasonable decision that can be made in such a desperate situation as a hated scheduling momet."
    stop ambience fadeout 2
    play sound sfx_open_door_clubs
    $ alt_pause(1)
    scene bg int_clubs_male_day
    with dissolve
    "But as soon as I opened the door, a pair of surprised eyes rose up on me."
    th "Who's that?"
    show ka pioneer shade with dissolve
    "A girl was sitting at the table clutching a thick skein of knitting thread in her hand."
    th "Seems like someone is also sabotaging nap time by devoting that time to needlework?"
    th "I don't mind the company, but here it is..."
    me "Hi."
    "I nodded awkwardly. The girl giggled."
    $ meet('ka', "Girl")
    ka "Well, hello. Come in, since you're here!"
    th "Why is she ordering me? This is my rightful job, by the way!"
    "I slammed the door and stepped forward, and the girl got up from the table. And then my eyes, clouded from the bright sun, deigned to show a terrifying picture..."
    show ka normal pioneer with dissolve
    "The badge on her chest is the same as Olga Dmitrievna's!"
    dreamgirl "Is that all you're confused about?"
    th "Well, you know, while she was sitting, I didn't pay attention!"
    dreamgirl "Commendable. You can be considered a decent pioneer who knows a lot about subordination."
    dreamgirl "Or an impotent incapable of appreciating such..."
    me "Oh."
    me "I'm sorry, I thought..."
    show ka laugh pioneer with dissolve
    "The squad leader giggled."
    $ meet('ka', "Squad leader")
    ka "Come on, I'll take it as a compliment. Girls love it when their age surprises men."
    show ka dontlike pioneer with dissolve
    "But her face hardened in an instant."
    ka "But still, it's quite curious what Olya's pioneer forgot here during quiet hour?"
    th "Oh yeah, I should be sniffing in my bed..."
    th "Unexpected encounters don't always turn out to be pleasant!"
    me "I didn't feel like sleeping, so I thought I'd tidy up the radio room a little while I didn't have to broadcast."
    "I blurted out the first thing that came to mind."
    show ka normal pioneer with dissolve
    "The squad leader cocked her head to one side."
    ka "So you are that Semyon Persunov?"
    me "It's-a me!"
    "Stupidly I repeated the unsuccessful introduction from the morning radio broadcast, smiling forcedly - maybe she'll take it for a joke."
    show ka smile pioneer with dissolve
    ka "Lovely!"
    "With a predatory smile, the girl squinted at the chair next to her."
    ka "Well, would such a responsible young man refuse to help a lady with a non-dusty, but very monotonous job?"
    th "Like I have a choice!"
    "I doomedly flopped down on the indicated chair, and a ball of green thread immediately appeared in front of me."
    ka "I'm doing 'hugs' for my squad here. Do you know what that is?"
    me "Ropes that are tied as a keepsake before leaving?"
    ka "That's right. I need thirty pieces - half an hour's work if we work with four hands."
    th "Wrapping threads on a piece of cardboard an infinite number of times, tying, cutting - there is nothing tricky in this work. But it's just boring..."
    show ka grin pioneer with dissolve
    "Catching my unenthusiastic look, the squad leader winked."
    ka "Don't be sour, Semyon. I can offer you a good deal."
    ka "For every 'hug', I offer you a valuable secret."
    th "What's the other secret?"
    dreamgirl "What if she lets you choose for yourself?"
    dreamgirl "I suggest you find out the color of her panties. She liked you, so she might even show them to you..."
    me "What's your name?"
    "For some reason, I decided it was time to get to know my employer."
    show ka smile pioneer with dissolve
    stop music fadeout 4
    ka "Just call me Katyushka. I'm the leader of the second squad."
    $ meet('ka', "Katyushka")
    th "Those dumbasses who always run around with Ulyana?"
    play music music_7dl["someone_like_you_guitar"] fadein 5
    show ka normal pioneer with dissolve
    "Having handed me an uneven cardboard, Katyushka returned to her work that had begun. Her ball of thread was red."
    th "Rewind, rewind, rewind…"
    th "In theory, thirty turns should be enough, but is it easy to keep track of how many have already been done?"
    th "Anyway, the 'hug' with no tassel left looks poor. I'll have to push it…"
    me "Done."
    "The first green “hug” lay on the table. The tassel came out crooked, and the knot on the string for the neck looked careless, but I didn’t say that I was a master, did I?"
    show ka laugh pioneer with dissolve
    "Katyushka chuckled."
    ka "Okay, here's your well-deserved reward:"
    "Leaning forward slightly, she whispered conspiratorially:"
    show ka smile pioneer with dissolve
    ka "Do you know why our art director doesn't show up on morning exercises?"
    th "She doesn't?"
    "To be honest, I didn't even notice it. And if I did, I didn't attach much importance to her absence."
    ka "Her uniform comes from Japan, like Miku herself. To be honest, it looks a bit... shocking to us."
    show ka happy pioneer with dissolve
    "Giggling, Katyushka continued:"
    ka "In a word, the head of the camp and your dear leader decided that one morning of education in the field of foreign culture would be enough for our pioneers."
    show ka normal pioneer with dissolve
    "And, as if nothing had happened, the squad leader straightened up, continuing to wind the threads around her cardboard."
    th "Yes, to be honest, I'm generally surprised that the first squad is also strained with morning exercises."
    th "Miku sits day and night in the music club, prepares concerts, Slavya runs around with a broom, then with unlucky newcomers, Zhenya sleeps in the library... Ah, right, physical activity definitely would not hurt her!"
    th "Lena draws in the newspaper, nerds-cybernetics also work there, and at our club, Alisa and I play the radio to the whole camp."
    th "Shouldn't there be some concessions for this?"
    dreamgirl "Hooo, don't you just want everything here and now!"
    dreamgirl "You're still on probation, and you won't be out of it until the end of your shift. And the rest get their own goodies anyway: they're allowed to have tea after lights out, and they'll give you a letter at the end of the shift."
    dreamgirl "And you two - are parasites and alcoholics!"
    th "What alcoholics? I don't drink at all!"
    dreamgirl "And how many days in the eye? Five?"
    me "Second one's ready."
    show ka smile pioneer with dissolve
    ka "You're curious!"
    ka "On the third day of her shift, Ulyanka got bored. Do you know how it usually ends?"
    "I nodded, anticipating something interesting."
    show ka happy pioneer with dissolve
    ka "She whispered to the fifth squad that one of my pioneers brought a box of plums with him to the camp. So until the end of the day they ran after him around the camp like mad and shouted: 'Vanya, we want plums!'"
    ka "Fortunately, my other pioneer, Sasha, decided to help out his comrade, and gave them a bag of apricots to be torn to pieces. The kids, however, turned their noses - the apricots, you see, were unripe."
    th "I see - she just tells me everything I missed."
    th "Well, not the worst you could expect!"
    "I began to wind the threads at an accelerated pace: Katyusha made 'hugs' twice as fast, but I really wanted to hear something about the pranks of the redhead..."
    me "Done."
    "The third tassel flew to the others."
    show ka normal pioneer with dissolve
    ka "What else can I tell you?"
    "Katyushka showed thoughtfulness on her face, but from her sly look and fool it would have become clear that she was waiting for a hint."
    me "And what, say, did my partner do until she was attached to the machine?"
    show ka smile pioneer with dissolve
    "My casual tone did not deceive the astute squad leader, and I looked down in embarrassment when I heard a quiet chuckle."
    ka "Alisa is an interesting person. Every day is like a powder keg!"
    ka "During the first week of camp, she decided to go on the run. She got tired, you know, of the camp. Got bored."
    ka "After dinner, she slipped away and went to the track to vote - hoping to catch a ride. She tied her tie around her arm to make it more noticeable."
    ka "And almost succeeded: she was picked up, and even almost taken to the city."
    "I tensed up."
    me "Then why is she still here?"
    ka "Her ride was the truck that carries food to the camp! The driver quickly realized that the lost tourist was actually a fugitive from the senior squads."
    show ka grin pioneer with dissolve
    "The girl chuckled, smiling at her memories."
    ka "They fed her at the warehouse, read the notation, and in the evening they returned to the camp - the driver took her in his passenger car and personally handed her to Olya."
    ka "But, to be honest, we were notably scared then. In my life, I never received such a headache from the authorities!"
    ka "But Alisa doesn't care at all. She still wears a tie on her arm - apparently she liked it."
    th "I wonder how my shift would go if she didn't get caught by the driver?"
    th "Alisa would travel around the cities, huddling in bunkhouses and looking for adventures on her... head, but what would I do here?"
    th "Would I fall in love with someone else if I didn't meet that red-haired beast here?"
    "I shook my head as if hoping to get those stupid thoughts out of it."
    th "Hardly. You won't find another like Alisa in the whole world - not like in the camp!"
    dreamgirl "You know, there's someone similar to her growing up here..."
    th "So she should grow up! And by the way, Ulyanka already has her own fiancé."
    me "What else is this camp hiding?"
    "Katyushka looked contentedly at the mountain of 'hugs': among them, however, there were only four green ones, as opposed to a couple of dozen red ones."
    show ka happy pioneer with dissolve
    ka "Did you know that Seryozha was the last to sign up for the newspaper?"
    th "Is that a secret?"
    ka "He didn't know where to go for a couple of days, until Slavya Shurik placed him under guardianship. And the next day, with his tail fluffed out, he rushed to the library: he was interested, you know, in reporting activities."
    th "So what's wrong with that?"
    th "Just think, he became friends with Shurik and decided to follow him everywhere!"
    dreamgirl "Do you have any imagination?"
    th "No, I won't believe that!"
    dreamgirl "You're also a pervert."
    "An inner voice drawled with disappointment."
    dreamgirl "Do you know how to build logical chains?"
    th "Why should I care about Syroezhkin anyway?"
    dreamgirl "What a fool."
    scene bg int_clubs_male_day with joff_r
    show ka normal pioneer with dissolve
    ka "That's all. This is the twenty-ninth."
    "I awkwardly tied a knot on the last tassel."
    me "Do you still have some secrets?"
    show ka smile pioneer with dissolve
    ka "Of course!"
    ka "Do you know what your leader's main weakness is?"
    "After a theatrical pause, Katyushka continued:"
    ka "Sweets!"
    ka "If you manage to get waffles for her at the end of the shift, you'll go home with a pile of certificates, medals and commendations!"
    th "Advice, of course, was good, but in my conditions it is completely useless!"
    "Having gathered all the hugs in an armful, Katyushka got up from the table."
    ka "Thank you for your help. Are you still going to clean the radio room?"
    me "Well, you know..."
    me "It's not such a mess."
    play sound sfx_close_door_1
    scene bg ext_clubs_day with fade
    play ambience ambience_camp_center_day fadein 1
    "Having gallantly held the door for the girl, I followed. Winking at me at the end, Katyushka left. I, putting my hands in my pockets, thoughtlessly stared into the distance."
    "I somehow got sick of meditating in the radio room. It would be even more strange to go to Alisa."
    "Without thinking of anything sensible, I trudged into the cabin - there was plenty of time to sleep."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_dv_dj_afternoon:
    scene bg int_dining_hall_people_day
    with joff_r
    play ambience ambience_dining_hall_full fadein 2
    play music music_list["get_to_know_me_better"] fadein 2
    show dv normal pioneer2 at cleft
    with dissolve
    "The pioneers in the canteen hummed sleepily, gobbling up sugary gingerbread."
    "Although the rain ended before dinner, in the quiet hour everyone sniffed peacefully in their beds."
    if alt_day5_dv_dj_map != "dv":
        th "Or they were doing important social work in the sun, which also does not contribute to a cheerful mood..."
    "Alisa who was standing beside me has already drained her glass of milk."
    if alt_day5_dv_dj_map == "dv":
        "She acted so naturally, as if there was nothing between us."
        th "But if you think about it, nothing really happened..."
        th "I shouldn't worry for the rest of my shift because I accidentally put my hand on her waist, right?"
    show dv grin pioneer2 at cleft with dissolve
    dv "Do you want some gingerbread? It's so sugary, I'm going to throw up!"
    "I happily reached for the extra portion, but then turned sour: the offer was not made for me."
    show us smile sport at right with dissolve
    "Stuffing the rest of her portion into her mouth, Ulyana greedily grabbed an unexpected gift of fate."
    us "Shpashiba!"
    show us grin sport at right with dissolve
    "The girl winked slyly, looking at my sour face."
    if alt_day5_dv_dj_map == "us":
        th "Could've at least given me a half of it as thanks for avoiding the fate of washing Alisa's underwear!"
    elif alt_day5_dv_dj_map == "dv":
        th "Probably thinking about what kind of gossip is more interesting to write about after what she saw after a quiet hour!"
    else:
        th "It's alright, friendo, it's while you're little all blessings fall on you from heaven on their own. But when you become old and ugly…"
    me "I assume there are no events planned right now?"
    show dv smile pioneer2 at cleft with dissolve
    dv "Uh-huh. So I think there's a nice prospect of getting some more sleep!"
    "She yawned widely and stretched with the most contented look."
    if loki:
        "Without a second's hesitation, I deftly tossed the rest of my gingerbread into her open mouth."
        me "Three-pointer!"
        show dv surprise pioneer2 at cleft with dissolve
        "Obviously not expecting such a setup, Alisa coughed, scattering crumbs all over the table."
    elif herc:
        "As the honorary owner of a four-legged creature, I had one extremely funny habit…"
        dv "Hmmm?!"
        show dv surprise pioneer2 at cleft with dissolve
        "Alisa's eyes almost popped out of their sockets in surprise when her teeth closed on my index finger."
    else:
        "After waiting for Alisa to open her mouth as wide as possible, I approached her ear and blurted out loudly:"
        me "The fly is coming!"
        show dv surprise pioneer2 at cleft with dissolve
        dv "Agh!"
        "The girl winced, convulsively rubbing her jaw."
        "I giggled: I knew firsthand that the sensations from such tricks are not the most pleasant."
    play music music_list["revenga"] fadein 2
    show dv angry pioneer2 at cleft with dissolve
    dv "Dumbass! Idiot!"
    show dv rage pioneer2 close at cleft with dissolve
    $ alt_pause(0.5)
    show dv rage pioneer2 close at fleft with move
    hide us with dissolve
    "She swung to hit me, but I jumped aside in time, laughing wickedly."
    me "How little you need to cheer up..."
    show dv rage pioneer2 at center with move
    play sound "<to 0.30>" + sfx_armature_swish
    "Putting the glass on the table with a crash, Alisa rushed in my direction. I went around the table in three jumps, being right in front of her."
    th "The most comfortable position for playing obstacle chasing."
    th "From a cornered victim, you instantly turn into Jerry, driving Tom wild for the thousandth time."
    show dv rage pioneer2 at cleft with move
    "Alisa twitched to the right, I twitched to the left."
    show dv rage pioneer2 at center with move
    "She abruptly changed direction, and in the same second I rushed to the right, guessing her maneuver."
    "The girl leaned angrily over the table, panting."
    "My lips stretched into a pleased smirk."
    me "Giving up?"
    "But the set-up, as usual, flew in from where I did not expect:"
    play sound "<to 0.30>" + sfx_armature_swish
    show us smile sport close at right with vpunch
    us "I'm holding him! Holdiiiing!"
    "Ulyana hung on my back, unpleasantly squeezing her neck with her grip."
    "Her sandals thumped painfully against my feet, increasing the urge to toss the little one right onto the tables behind."
    dreamgirl "And if you would've given her your gingerbread..."
    th "...it would be doubly insulting now!"
    show dv angry pioneer2 with dissolve
    "Alisa was quick on the uptake and immediately rushed towards me, skirting the table."
    "I, having lost a little mobility with my burden, tried to hide, but Ulyana's grip turned out to be surprisingly strong."
    me "That's not fair!"
    "Without much hope, I appealed to the conscience of the redheads."
    th "Though what am I talking about? They have no soul, no conscience, no compassion!"
    show dv rage pioneer2 with dissolve
    dv "Look who's talking about fairness, smartass!"
    show blink
    stop music fadeout 3
    "She swung, and I closed my eyes, waiting for a blow..."
    mt "What's going on here?"
    show unblink
    hide blink
    show mt angry pioneer behind us at fright
    with dissolve
    "Opening my eyes, I immediately stumbled upon the menacing look of the squad leader."
    show dv surprise pioneer2
    show us surp1 sport close at right
    with dissolve
    play music music_list["two_glasses_of_melancholy"] fadein 2
    "Caught by surprise, Alisa remained standing with her fist raised in the air, and Ulyana forgot to unhook me."
    th "An interesting picture opens before our dear and beloved leader!"
    me "Lunch."
    "My statement was hard to argue with."
    show mt normal pioneer behind us at fright with dissolve
    mt "Ulyana! Release Semyon immediately!"
    mt "Alisa! Get your uniform in order!"
    mt "Semyon!"
    $ alt_pause(0.3)
    "There was a slight lag."
    dreamgirl "How convenient!"
    show mt sad pioneer behind us at fright with dissolve
    mt "How do you always get into tomfoolery like this?"
    show dv normal pioneer at cleft
    show us fear sport at right
    with dissolve
    "We obediently dispersed: Alisa reluctantly smoothed her wrinkled shirt, and Ulyana rolled her eyes, as if she had been torn away from a terribly important task."
    show mt normal pioneer behind us at fright with dissolve
    mt "Ulyana is free. Radio hosts - follow me!"
    th "Wow, I got promoted again!"
    th "So I will reach the rank of general by the end of the shift..."
    dreamgirl "Keep dreaming! He has his own children."
    show us laugh sport at right with dissolve
    us "Yessir!"
    hide us with moveoutleft
    "Having bowed, Ulyana rushed out of the canteen like a bullet."
    show dv angry pioneer at cleft with dissolve
    "Alisa and I exchanged angry glances and followed Olga to the exit."
    th "I have a feeling our great battle is not over yet. I wonder how many seconds it'll take me to set up a barricade of improvised means in the radio shack?"
    $ alt_pause(1)
    scene bg ext_dining_hall_near_day with dissolve
    play ambience ambience_camp_center_day fadein 1
    show dv angry pioneer at left
    show mt normal pioneer at right
    with dissolve
    "On the porch Olga stopped, turning to us."
    "Her face was not stern, as I expected, but habitually cunning with a slight touch of laziness."
    th "Understood. Another party assignment..."
    show mt smile pioneer at right with dissolve
    mt "In case you forgot, I remind you that after dinner we have a hike. Of course, with a fire and a guitar."
    me "Of course."
    "I muttered."
    mt "I would really like you to perform a few songs live during the broadcast, with a guitar. Some of the simplest, camping ones - Alisa knows a few."
    mt "We need to refresh the lyrics in the memory of the junior squads, and at least give these songs to listen to those who came to the camp for the first time."
    th "It will be a lot of honor for them!"
    th "When they come for the second time - they'll definitely know them. Now why worry about them?"
    mt "Did you understand the task?"
    show dv dontlike pioneer at left with dissolve
    "I nodded. Alisa just looked away, her brow furrowed."
    show mt normal pioneer at right with dissolve
    mt "I won't delay you any further then."
    $ alt_pause(0.3)
    show mt normal pioneer far at right with dissolve
    hide mt with dissolve
    "Having appraised a last look at us, as if not completely trusting, Olga again disappeared in the canteen's door."
    show dv dontlike pioneer at center with dissolve
    "I turned to my partner."
    me "Let's get the guitar?"
    "Not answering my question, Alisa moved down the stairs."
    "I caught up with her, grabbing her hand."
    me "What's the matter with you, Liska?"
    "I began to regret my words literally a second before I opened my mouth."
    play sound sfx_angry_ulyana fadein 1
    show dv rage pioneer close:
        linear 1.5 zoom 1.3
        linear 1.5 ycenter(0.4)
    with dissolve
    dv "Don't.{w=.5} Call.{w=.5} Me.{w=.5}"
    with vpunch
    extend " That!"
    "She screamed in my face."
    "Her mouth twisted in anger."
    if lp_dv < 16:
        "Resentment stirred within."
        th "So Ulyana can call her that, but I'm just a passerby to her?"
    else:
        "I mentally slapped myself."
        th "I knew she didn't like it when personal boundaries were so rudely crossed..."
    me "Sorry, Dvachevskaya. Overheated in the sun."
    hide dv
    show dv normal pioneer with dissolve
    "Alisa forced out a semblance of a smirk."
    dv "You're quick to think."
    "But she still didn't seem to be at least in an acceptable state."
    me "So, the guitar?"
    show dv sad pioneer with dissolve
    "The girl nodded, turning dark again."
    dv "Let's go."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_dv_dj_radio_broadcast:
    scene bg int_clubs_dj_7dl with dissolve
    play sound sfx_open_dooor_campus_2
    play ambience ambience_clubs_inside_day fadein 1
    "In the radio room, everything was the same: silence, peace and despondency."
    "There was no feeling of comfort in this place, which was in all other clubs."
    "There was no lightness here, as in the music club, the appearance of vigorous activity, as in the main premises of clubs..."
    th "Even the library seems much nicer than this pathetic back room!"
    show dv normal pioneer2 with dissolve
    "Alisa was in full swing setting up the equipment, while I was stomping in the corner, squeezing the guitar in my hands."
    me "What are you going to perform, mass entertainer?"
    stop ambience fadeout 3
    play music music_7dl["lastlight_guitar"] fadein 3
    show dv tired pioneer2 with dissolve
    "Turning on the music, the girl leaned back in her chair wearily, her eyes boring into the ceiling."
    dv "I don't know. Nothing comes to mind."
    "I sat down beside her, carefully arranging the guitar in my lap."
    me "There was a grasshopper in the grass..."
    "This body did not have the skills to handle the instrument: the fingers could hardly find the right chord."
    show dv normal pioneer2 with dissolve
    "I looked up at Alisa, hoping to see a smile on her face. The girl forcedly lifted the corner of her mouth."
    show dv sad pioneer2 with dissolve
    dv "I'm tired of these songs, my strength is gone."
    "Alisa spoke indifferently, but there was a subtle irritation in her voice."
    dv "Every year it's the same thing: the kids sing along happily, the squad leaders look so tenderly, as if they'll burst into tears, making me want to give them a handkerchief!"
    dv "And I'm disgusted with all this. Today, Petka and Vitka sing about strong friendship, which does not break, and tomorrow their noses break."
    dv "This is a fake event, inside and out."
    th "Did she talk about anything for that long?"
    th "Unless she was telling tales, but here is a whole opus..."
    "I held my breath, as if absorbing this new Alisa."
    dv "Just like everything else here. All fake, fraudulent."
    dv "And if I close my eyes..."
    show dv closed_eyes pioneer2 with dissolve
    "She really closed them, bringing her eyebrows to the bridge of her nose and biting her bottom lip."
    show dv normal pioneer2 with dissolve
    dv "Give me the guitar."
    "Mournful daydreaming on the verge of doom disappeared from her intonations."
    "In front of me was the old Alisa again, who did not hesitate to slurp in the canteen and was ready to sell her soul in order to slip away from public works."
    "The girl arranged the guitar on her lap and thoughtfully turned the plectrum in her fingers."
    dv "Where should I sta..."
    show dv angry pioneer2 with dissolve
    "The pick slipped from her hand, falling to the floor."
    "Turning around its axis a couple of times, it sadly hooted into the very crack where a part of the Syroezhkin's soldering iron had rolled away the day before."
    if loki and alt_day5_dv_dj_map == "us":
        dreamgirl "See, the karma police does exist!"
    "Alisa muttered something abusive through her teeth as she sank to the floor."
    "I squatted beside her as if that could help in any way."
    me "Basically, if we pick it up with a ruler..."
    "The girl shook her head in annoyance."
    dv "What's the point? You can't see anything there."
    dv "We'll be crawling here until night if we try, so..."
    "She straightened up, a look of relief on her face."
    show dv smile pioneer2 with dissolve
    dv "Well, the plans are ruined, there is no hope left. The new arrivals will have to howl to the beat."
    me "Wait a minute, I had something here!"
    hide dv with dissolve
    show backpack at truecenter with dissolve
    play sound sfx_7dl["backpack"]
    "I dived into a backpack, which was abandoned in the radio room as unnecessary. If my memory did not fail me, then there was a wallet just lying around."
    th "Of course, the strings will quickly come to an end from such manipulations, but isn't it necessary to save the situation somehow?"
    hide backpack with dissolve
    show dv smile pioneer2 with dissolve
    me "Here."
    stop sound fadeout 1
    "I handed Alisa a five-ruble coin."
    "Of course, she could have questions, but I could always lie that it was a souvenir."
    "Questions have arisen, and clearly more than one."
    show dv surprise pioneer2 with dissolve
    "The girl looked at the coin with her mouth open, turning it over one side, then the other."
    play music music_7dl["laugh_throught_the_universe"] fadein 3
    $ renpy.show("bg int_clubs_dj_7dl", what = Dawn("bg int_clubs_dj_7dl"))
    with dissolve
    "Quietly creeping up from behind, I whispered in her ear."
    me "Looks like I screwed up."
    show dv shocked pioneer2 with dissolve
    "Alisa shuddered and froze, unable to move."
    $ renpy.show("bg int_clubs_dj_7dl", what = Desat("bg int_clubs_dj_7dl"))
    me "Now you know who I am. You already know the answer, don't you?"
    "I heard her swallow softly."
    me "Now I'll have to snap your neck and hitchhike out of camp."
    show dv scared pioneer2 with dissolve
    "I put my hands on Alisa's shoulders, causing her to shudder again - much stronger this time."
    me "Or we can make a deal."
    "Pausing, I shifted from her left ear to her right, breathing menacingly into the red head."
    me "You won't tell anyone that I..."
    stop music fadeout 1
    me "…am a counterfeiter?"
    play music music_list["went_fishing_caught_a_girl"]
    scene bg int_clubs_dj_7dl
    show dv scared pioneer2
    "Here I blundered: it was simply impossible to restrain laughter."
    show dv angry pioneer2 with vpunch
    "Alisa promptly turned around and slapped my forehead with all her might."
    me "Ouch!"
    dv "You're a clown, not a counterfeiter!"
    me "That hurt!"
    dv "And your jokes are idiotic!"
    me "I could have died! You could have killed me!"
    show dv grin pioneer2 with dissolve
    dv "You haven't got much yet!"
    "Alisa turned back to the table, throwing the coin there."
    show dv normal pioneer2 with dissolve
    dv "It won't do anyway. The strings will snap and Miku has almost no spares left."
    me "So what to do then?"
    dv "Take off your pants and run!"
    "The girl snorted."
    dv "Okay, I can play without a pick. Fortunately, there are nails on my right hand."
    "I looked at her thoughtfully."
    "Alisa still hasn't awoken any desire to entertain the audience with a live performance."
    menu:
        "Let me sing instead!":
            $ lp_dv += 1
            show dv surprise pioneer2 with dissolve
            "Alisa looked at me with disbelief - there was too much enthusiasm in this proposal."
            dv "Can you?"
            me "You're offending me!"
            "I tightened my throat and jaw - that's how you could achieve the most vile sound of a voice."
            me "Wiiiiiingeeeeeed swiiiiiings…"
            show dv scared pioneer2 with dissolve
            "Not expecting such a sonic assault, Alisa covered her ears in horror with her hands, wincing in pain, but I did not even think of stopping!"
            me "Flyyyyy-flyyyyyyy…"
            me "They are flyyyyyyyyyiiiiiiing!"
            show dv shocked pioneer2 with dissolve
            dv "Please stop!"
            "She shouted it from somewhere under the table - apparently, I underestimated my vocal abilities."
            me "So, what'd you think?"
            show dv grin pioneer2 with dissolve
            dv "You know…"
            "Alisa cautiously emerged from her hiding place, as if expecting another shockwave of sound."
            dv "I've heard a nail scratch glass, and it was three times more pleasant than your singing!"
            me "I can still do falsetto!"
            show dv scared pioneer2 with dissolve
            dv "Dear God…"
            "Alisa crawled under the table again."
            me "You'd better tell me this: after how many seconds of this performance will the Hat burst in here to smash the guitar on my head?"
            show dv normal pioneer2 with dissolve
            dv "I'd love to check it out, but I'm afraid I won't live to see her."
            "Alisa took the guitar and put it in a corner, leaning against the table."
            stop music fadeout 5
            dv "So let's put the camp out of its misery and just forget about that idiotic request from the squad leader?"
            me "Good offer!"
        "To hell them, both them and their tasks!":
            $ karma += 10
            me "First the morning circus, now sing songs live ..."
            me "What will they ask for next? Dance on the table?"
            show dv sad pioneer2 with dissolve
            dv "What's the point..."
            "She cut her speech off mid-sentence, meeting my sarcastic gaze."
            me "That's it. This background radio is needed so that the children run more cheerfully and breathe more deeply. And they are trying to make animators out of us!"
            me "So I suggest you safely give up on all the party tasks and just rest before the nightly feeding of mosquitoes."
            show dv grin pioneer2 with dissolve
            "Alisa chuckled."
            dv "For once you offer something sensible!"
            show dv normal pioneer2 with dissolve
            "She put her guitar back in the corner, leaning back in her chair, relaxed."
            stop music fadeout 5
            dv "It's nice to deal with a person with whom you think in the same direction!"
        "Sing already so they buzz off!":
            $ lp_dv -= 1
            me "A couple of songs and that's it, there's going to be nothing to complain about."
            show dv tired pioneer2 with dissolve
            "Alisa looked away."
            dv "Yeah you know..."
            dv "I just don't want to. Even if they leave me to starve until the end of the shift!"
            show dv sad pioneer2 with dissolve
            "She looked at me wearily."
            dv "You probably don't realize how disgusting it is to be asked to please someone."
            th "What is she talking about?"
            dv "All these songs, dances... First - to show themselves as good children. To be noticed and chosen."
            "I froze: I never considered being an orphan from such a position."
            dv "Then here at the camp, at concerts - to make your parents proud of you. As if they would be less proud if I played at home, in my room!"
            show dv sad pioneer2 with dissolve
            dv "I don't want to play for someone else's fun and pleasure. I want to play for myself and for…"
            "She froze, eyeing me suspiciously."
            if lp_dv < 16:
                dv "No matter."
            else:
                dv "…people I care about."
            show dv normal pioneer2 with dissolve
            dv "Don't worry. Just my troubles."
            stop music fadeout 5
            me "Sorry."
            "An awkward pause hung in the air."
    $ alt_pause(1)
    play music music_7dl["hear_a_love"]
    "Stretching, Alisa pulled a deck of cards from her pocket."
    show dv smile pioneer2 with dissolve
    dv "A couple rounds of «Durak»?"
    me "Why not?"
    "While the redhead dealt the cards, I sat with my cheek propped on my hand, and I lazily watched the movements of her hands."
    th "I wonder how many years it would take for her to let me at least as close as Ulyana?"
    dreamgirl "Wow, you set out to be her…"
    dreamgirl "…best friend?!"
    th "God forbid! That's not what I want!"
    dreamgirl "Then offer her to play cards at least for undressing!"
    th "And then I will undoubtedly be her best friend until the end of time. In the future, a drinking buddy."
    th "And in the longer term, a friend with privileges."
    dreamgirl "Is that not enough for you?"
    th "I don't need this!"
    th "What's the point of sharing a bed with someone who will never let you into their soul anyway?"
    dreamgirl "Let's imagine, purely hypothetically, that she jumps on you herself. Will you succumb or will you drag her to the registry office first?"
    "I could not dissemble: I would have succumbed."
    "I was generally ready for anything for the sake of my red-haired beast."
    th "But was she only mine?"
    show dv laugh pioneer2 with dissolve
    dv "And this is for your shoulder straps!"
    me "And my spider sense says you cheated!"
    show dv grin pioneer2 with dissolve
    dv "Your spider sense has no evidence!"
    "She began to shuffle the deck."
    "I followed the movements of her fingers without much hope: I knew that I couldn't catch her cheating anyway."
    th "But we could not play Durak now, but…"
    if alt_day5_dv_dj_map == "dv":
        "My thoughts again carried away to those marvelous and unrealizable pictures that were so vividly drawn in my head at a quiet hour."
        "Except that now they were much more casual, as if Alisa's smirk did not allow my mind to amp the drama to the maximum."
    else:
        "Thoughts clouded in a haze - slightly dull and grainy, like frames from an old and warm movie."
    $ alt_pause(1)
    $ set_mode_nvl()
    "{i}We could run away where no one can find us, and lie lazily under the caressing rays of the fading sun, exchanging easy joking phrases.{/i}"
    "{i}We could pull a couple of bicycles out of the inventory and drive forward for a long, long time, as if dreaming of escaping from the heat emitted by the asphalt heated during the long daylight hours.{/i}"
    "{i}Drive to the meadow and just sit in the company of chirping insects, watching the sun sink over the horizon.{/i}"
    "{i}Or swim on a wild beach, shouting loudly and splashing water at each other until you get bored.{/i}"
    "{i}And then to dry for a long, long time on the shore with lips blue from the cold, chattering teeth and exchanging name-calling - not offensive, no.{/i}"
    "{i}We just wouldn't be able to express our feelings otherwise.{/i}"
    "{i}We could...{/i}"
    $ alt_pause(1)
    $ set_mode_adv()
    show dv angry pioneer2 with dissolve
    dv "You're not fun to play with at all!"
    "Alisa threw her cards on the table in annoyance."
    "I didn't have to turn them over to realize I lost again."
    dv "You have your head in the clouds, you don't even follow the cards. Don't you know the most basic principle of playing Durak?"
    me "Shuffle the cards so as to completely dominate the enemy?"
    with vpunch
    "I didn't manage to dodge the flick."
    show dv normal pioneer2 with dissolve
    dv "Dumbass! You just have to remember which cards other players take!"
    th "It sounds simple in words, but in practice I have a hard time remembering my name in the morning!"
    me "Excuse me - I'm not the most inveterate gambler. Moreover, we don't play for money, what's the point of straining?"
    show dv grin pioneer2 with dissolve
    dv "You might think you're a rich Pinocchio!"
    me "Exactly."
    "I nodded solemnly."
    me "Because I don't play cards!"
    show dv grin pioneer2 close with dissolve
    "I grabbed her hand at my forehead and put it over my shoulder."
    "Not expecting such maneuvers, Alisa almost slammed into my face."
    show dv smile pioneer2 close with dissolve
    dv "Oh, you…"
    me "Who?"
    "Looking into her eyes with interest, I removed the strand from the girl's forehead with my free hand. Alisa did not start to be embarrassed - apparently, she did not fully realize what was happening."
    show dv smile pioneer2 close:
        linear 1.5 zoom 1.2 yoffset 200
    with dissolve
    me "Did you forget?"
    "I asked in an ingratiating tone, slowly approaching her lips."
    dreamgirl "What do I see!"
    dreamgirl "Did Don-Juan of the provincial kind slumber in our slowpoke all this time?"
    th "Petersburg is the second capital!"
    stop music fadeout 2
    $ volume(0.5, "sound")
    play sound sfx_7dl["eat_horn"] fadein 3
    "Control over the situation was lost: Alisa's gaze sharply changed from bewildered to wary. And a couple of seconds later the horn blew, calling the pioneers to the last meal for today."
    hide dv
    show dv normal pioneer2 with dissolve
    play music music_list["goodbye_home_shores"] fadein 3
    "Effortlessly freeing herself from my grip, the girl began to turn off the equipment with a straight face."
    th "Why the hell are you always showing up at the wrong time?"
    $ volume(1.0, "sound")
    dreamgirl "Who is to blame that you are more interested in your small homeland than girls?"
    me "Got an excuse for the Hat?"
    show dv smile pioneer2 with dissolve
    "Alisa chuckled as she pulled out the last plug."
    dv "Already had one when she came up to me with her stupid problem!"
    "She behaved as if nothing had happened. It was both pleasing and not."
    th "And managed to blunder at such a good moment!"
    show dv normal pioneer2 with dissolve
    dv "Let's go, we still have to listen to another lecture... to improve our appetite."
    hide dv wit dissolve
    "Snorting, I followed her. After all, I still had plenty of time."
    th "Right?"
    stop music fadeout 3
    return

label alt_day5_dv_dj_dinner:
    scene bg ext_dining_hall_near_sunset with dissolve
    play music music_list["your_bright_side"] fadein 3
    play ambience ambience_camp_center_evening fadein 2
    show dv normal pioneer at cleft
    show mt angry pioneer at right
    with dissolve
    "Olga Dmitrievna, without changing the tradition that had developed in recent days, was waiting for Alisa and me on the porch."
    "According to the same good tradition, she did not look the most rosy."
    th "I wonder why she never came up with the idea of starting all the nasty conversations after the meal?"
    dreamgirl "On a full belly, no conversation will be unpleasant."
    th "True."
    mt "As I understand it, Dvachevskaya, you decided to ignore my request?"
    th "What amazing insight!"
    show dv smile pioneer at cleft with dissolve
    dv "I had a problem with my guitar. A string broke."
    "Her lie sounded so confident, as if the whole evening the redhead diligently convinced herself that this was indeed the case."
    dreamgirl "Yeah, of course. She also rehearsed in front of the mirror when you blinked!"
    mt "Didn't think of replacing it?"
    show dv normal pioneer at cleft with dissolve
    "Alisa shrugged her shoulders indifferently. The leader's anger did not touch her in the slightest."
    dv "That's what I've been doing for the entire broadcast. It's not a five-minute task, you know."
    show mt normal pioneer at fright with move
    "Either Olga really did not understand anything about guitars, or she was not in the mood to bark - waving her hand, she kindly stepped aside, clearing the way for us to the canteen."
    mt "From now on, take the trouble to let me know about any problems!"
    show sl serious pioneer at fleft behind dv with moveinleft
    "Out of the corner of my eye, I noticed Slavya hurrying to the porch."
    show sl serious pioneer at center behind dv with move
    $ alt_pause(0.5)
    show sl sad pioneer far behind dv with dissolve
    $ alt_pause(0.2)
    hide sl with dissolve
    "She glanced furtively around before sneaking past the leader into the canteen."
    th "Wow! Is our pioneer-everyone's-example also shirking from important work, and now she is trying with all her might to elude justice?"
    "It didn't look like Slavya."
    show dv dontlike pioneer at cleft with dissolve
    "I exchanged a glance with Alisa - the girl frowned, also sensing something was wrong."
    th "She also clung to me! It's obviously not without reason…"
    scene bg int_dining_hall_people_sunset_7dl with dissolve
    play ambience ambience_dining_hall_full fadein 1
    show dv normal pioneer at cleft with dissolve
    "There was no queue for the distribution - all the pioneers were already sitting at the tables, humming happily in anticipation of the fire."
    "I turned to Slavya and the girl smiled."
    show sl smile pioneer at right with dissolve
    sl "It's been a nice evening today, warm."
    sl "I was already afraid that our trip would be canceled because of the morning rain!"
    "There was something unnatural, nervous in her speech."
    show dv grin pioneer at cleft with dissolve
    "Alisa grunted, looking at Slavya, but did not answer."
    me "Yeah, we're all fabulously lucky."
    show sl smile2 pioneer far at right with dissolve
    "Smiling even wider, Slavya with an unobtrusive movement circled Alisa and me, grabbing a tray from a pile on the go, and, without saying a word, began to pick up food for herself."
    dreamgirl "Strange things are happening here..."
    th "What are you on about?"
    dreamgirl "The fact that your red-haired girlfriend is silent!"
    "It didn't take a lot of intelligence to understand that Alisa strongly dislikes Slavya."
    "And the fact that the redhead left the object of her hatred without a single verbal stab made me seriously tense."
    th "If this whirlpool has calmed down, then the local devils had at least a Sabbath!"
    hide sl with moveoutright
    show dv angry pioneer at center with dissolve
    dv "Wow, what secrets do we have here!"
    "Alisa strained as soon as Slavya left with her tray towards the tables."
    "I looked at the girl with concern: she seemed to be devouring the retreating back of the activist's head with her eyes."
    me "What are you talking about?"
    dv "Ever since the beginning of the shift, I noticed that the upstart was stumbling around the tables after eating."
    dv "I recognize this look from a thousand: I have a sense for the most 'not hungry'."
    dv "And that radar also detects competition."
    dv "I thought she just didn't get enough - obviously not on children's portions her..."
    "Alisa traced two arcs in her chest with her hands."
    dv "...grew."
    show dv laugh pioneer with dissolve
    "Her lips curled into a smirk."
    dv "And now everything is clear!"
    th "Yeah, just like in the proof of any mathematical theorem: the cube has all square sides, which means that it is a perfect sphere."
    "Feeling like a complete idiot, I clarified:"
    me "Uh... what did you realize?"
    show dv normal pioneer at center with dissolve
    "Alisa rolled her eyes."
    dv "Did you see what she has on her shirt?"
    "To be honest, I had no idea what Alisa saw there."
    th "But wait a minute…"
    th "At first she clung to me to get past the leader, then she got nervous and twirled when I turned to her, and then she completely crawled in front of us to the distribution, which was already beyond any limits!"
    th "So, on her shirt..."
    show dv soft_smile pioneer at center with dissolve
    dv "Dirty paw prints, dumbass! She keeps a cat or a dog in the camp!"
    "Puzzle was solved: that's where she ran the first night before feeding me."
    if counter_sl_7dl == 0:
        th "And then, when I first arrived at the camp... she was in a hurry to her pet, wasn't she?"
    me "More like a dog."
    me "Cats are too headstrong to sit in one place for long, and they know how to find loopholes when they feel like walking."
    "Alisa and I stomped around at the end of the distribution with trays in our hands."
    show dv think pioneer at center with dissolve
    dv "What am I supposed to do with this information…"
    menu:
        "Just forget it":
            $ lp_dv -= 1
            $ karma += 10
            me "Seriously, why would you want to get into this? Even if Slavya really hides a dog in the camp, the truth will come out sooner or later."
            me "Or did you decide to act as a snitch?"
            stop music fadeout 3
            show dv rage pioneer with dissolve
            "Alisa flushed."
            dv "Hell no! I won't leave it like this!"
            play music music_7dl["sky_feather"] fadein 3
            dv "What does she think of she is? Does she think that since they are allowed to drink tea after lights out, it means that now there are no boundaries at all?"
            play sound sfx_drop_pipe fadein 0
            show dv angry pioneer with dissolve
            "The girl crashed her tray onto the nearest table."
            dv "Sit here."
            "She said in a commanding tone before she left."
            hide dv with moveoutright
            "I followed her with a long and hard look, lowering my tray opposite of hers."
            "Knowing Alisa, it was necessary to prepare at any moment to break up the fight."
            th "Even though Slavya would let this happen..."
            th "They don't have that much of a conflict, do they?"
            th "And I'm sitting on the sidelines again while someone makes a showdown. It's starting to become a habit."
            dreamgirl "So jump like a hog, solve questions - why do you wait?"
            th "No. If Dvachevskaya has some kind of plan, then I'm obviously not included in it, considering she left me here, ordering me not to interfere!"
            "What that plan was was anyone's guess."
            show dv angry pioneer far at cright with dissolve
            $ alt_pause(0.25)
            show sl surprise pioneer far at fright behind dv with dissolve
            "And Alisa was already hovering over the activist's table, saying something to her face."
            show dv smile pioneer far at cright with dissolve
            "Her lips curled into a smirk that grew wider."
            show dv laugh pioneer far at cright with dissolve
            $ alt_pause(0.25)
            show sl sad pioneer far at fright behind dv with dissolve
            "And the brighter Alisa's smile shone, the paler Slavya became."
            th "I don't like this..."
            th "Blackmailing? Possibly."
            th "Intimidating? Maybe."
            "No matter what Alisa said, Slavya was definitely not having fun."
            "Her brows furrowed, and her palm on the table clenched into a fist."
            "She began to slowly get up from the table, and I grouped myself, preparing to rush to the rescue - though not yet quite understanding who and from whom I would have to protect."
            dreamgirl "Wow, look - bread and circuses in one room!"
            dreamgirl "Personally, I'm betting on the blonde - her speed may be lower, but she noticeably surpasses the opponent in mass."
            show sl sad pioneer far at right behind dv with move
            "But Slavya walked past Alisa without even hitting her with her shoulder."
            show sl sad pioneer far at fleft behind dv with move
            show mt normal pioneer far at left behind sl with dissolve
            "She was heading for the leader's table."
            th "A wise decision for such a young person."
            th "If you're afraid of losing something, then lose it and don't be afraid anymore."
            hide sl
            hide mt
            with dissolve
            $ alt_pause(0.25)
            show dv smile pioneer at center with dissolve
            "And while the activist, with her head bowed, surrendered herself to Olga, Alia returned to me, chuckling quietly."
            dv "Did you see her face?"
            me "Uh-huh."
            "I didn't share Alisa's joy at all."
            "Her act seemed something nasty and vile, and I caught myself thinking that I was ashamed in front of Slavya."
            th "She didn't do anything bad to me, after all. I don't know all the ins and outs of their feud with Alisa…"
            dreamgirl "So don't bother. You didn't get up in their business?"
            dreamgirl "That's right, you didn't."
            dreamgirl "So there is no need to torment your conscience - you already torn it to shreds."
            th "That's right."
            me "Bon appetit."
            show dv normal pioneer with dissolve
            dv "Mhm."
            "We finished the meal in silence: I was in my heavy and senseless disputes with my conscience, Alisa - reveling in her triumph."
        "Show your imagination!" if not herc:
            $ lp_dv += 2
            $ karma -= 10
            $ alt_day5_dv_dj_sl_jeer = 1
            me "Just think: what a card you have up your sleeve - the most terrible secret of the most decent person in this almshouse!"
            show dv smile pioneer with dissolve
            "Alisa grinned, rapaciously looking for Slavya among the champing pioneers."
            stop music fadeout 3
            dv "I just need to check something..."
            dv "Let's go!"
            play music music_list["into_the_unknown"] fadein 3
            "We went straight to the table, at which our infallible lover of exotic (for a pioneer camp, of course) fauna was sitting alone."
            me "Do you mind if we join?"
            show sl scared pioneer at right with dissolve
            "Slavya shuddered, raising frightened eyes at us."
            th "It seems she realized. And judging by the fact that she is not happy with our company, we got it right too."
            "The girl shook her head negatively, pulling her tray closer. Her shoulders shrunk, and she seemed to be trying to shrink, just to avoid such inappropriate attention from the enemy."
            show dv laugh pioneer at cleft with dissolve
            dv "Bon appetit."
            show sl surprise pioneer at right with dissolve
            "Alisa licked her fork, impudently looking Slavya straight in the eye. Even though I didn't want to conflict so openly with the person who cared so much about my fate on the first day, I couldn't help but play along with the redhead."
            "From my smirk, the activist became frankly uneasy: her eyes ran around the canteen in search of an escape route."
            show sl scared pioneer at right with dissolve
            sl "You too."
            "The girl did not want to admit her defeat, no matter how obvious her failure was."
            "And Alisa was in no hurry to move on to the attack, leisurely eating dinner and throwing almost sympathetic glances at Slavya. She played with the victim, testing her endurance."
            th "A psychic attack like that can drive you crazy..."
            th "She has already spoiled the activist's appetite - our beauty is sitting there, picking her plate with a fork, a piece probably won't go down her throat."
            show dv grin pioneer with dissolve
            dv "Don't you think it smells of something in here?"
            dreamgirl "Whoa! Things are about to unfold."
            dreamgirl "Act two: hidden threats are replaced by bold hints like this..."
            "Alisa nudged me lightly with her knee, and I sniffed picturesquely."
            me "Yeah, there's something like that. It's like someone smells doggy."
            me "But you can't keep dogs in the camp?"
            show sl upset pioneer at right with dissolve
            "I asked this as if by chance, but without taking my eyes off Slavya, who was getting paler with every second."
            dv "Strictly forbidden. I read the rules three times - every time I got on the carpet to the director, I was forced to recite them by heart."
            me "And if, for example, someone decided to hide a dog, say, in a warehouse, then what would he do for it?"
            dv "Depends on age. A youngster would be forgiven - a child, does not understand anything."
            dv "But who is older - would go home with a certificate of honor about how stupid he is."
            "It seemed like another second, and Slavya would burst into tears."
            show dv smile pioneer with dissolve
            dv "Although I don't rule out that the squad leader would cover for some of her favorites - that's why they are favorites. Not everyone can crawl, some are born to fly."
            show dv laugh pioneer with dissolve
            dv "It's much more convenient to ignore the rules from a height, isn't it?"
            "She was grinning at Slavya. The circus was over."
            dreamgirl "Act Three: Attack!"
            dv "The Hat will cover you, you're very good friends for sure. But what would Alexei Maksimovich say?"
            "Slavya's lips trembled."
            show sl sad pioneer at right with dissolve
            sl "Why are you doing this?.."
            dv "Because I can, Feoktistova."
            show dv grin pioneer with dissolve
            "Alisa leaned back in her chair, gazing appraisingly at the cornered activist."
            dv "You've been snitching on me to the leader for the whole shift, because what?"
            dv "The rules of the camp were pricking in one place?"
            show sl angry pioneer at right with dissolve
            with hpunch
            sl "What's with the rules?"
            "Slavya slammed her hand on the table, leaning forward. Her eyes flashed dangerously in the red rays of the fading sun."
            sl "Someone always suffers from your antics! Do you think I should be silent, endangering others, if only not to become a snitch in your eyes?"
            "Slavya went on the attack so abruptly that I was taken aback."
            dreamgirl "It's not fair to translate arrows!"
            "But Alisa didn't raise an eyebrow."
            show dv smile pioneer with dissolve
            dv "Asthma. Allergies."
            $ alt_pause(3.0)
            $ volume(0.75, "music")
            show sl scared pioneer at right with dissolve
            th "If I knew that with just two words it's possible to shut a person up so well..."
            "The activist seemed to suffocate, choking on the claims stuck in her throat."
            me "And also distemper and rabies. Or did you show your dog to Viola?"
            me "Maybe you also vaccinated her?"
            th "God knows - I didn't want to jump in on the rampage…"
            th "But I won't let her whitewash her reputation by dragging Alisa through dirt!"
            th "My Alisa."
            me "You cuddle with your dog and go to the canteen without even bothering to wash your hands - I don't even talk about clothes. Do you even think with your head what awaits us all if you bring an infection here?"
            me "How many people from here can be taken to the hospital urgently?"
            me "How many braided girls like you will cry and curse you if you gift them a ringworm?"
            with hpunch
            sl "Enough!"
            show sl cry pioneer far behind dv at right with dissolve
            "Slavya jumped up from the table. Her eyes were red."
            sl "I've already realized that I'm doing something stupid. Excuse me if my apologies and my sincere remorse will get you anything."
            "She pushed her chair back and walked quickly forward."
            hide sl with moveoutleft
            "To squad leader's table."
            show dv normal pioneer at center with dissolve
            dv "Nice thinking - I didn't remember anything smarter than allergies."
            stop music fadeout 3
            "There was respect in Alisa's voice, which was a pleasant balm for my slightly hurt conscience."
            $ volume(1.0, "music")
            me "You can find danger in anything, even in the most harmless looking things. And putting pressure on a girl who already has a mess in her soul is a trifling task."
            me "She would have gone to turn herself in, even if the most terrible prospect was to scare one of the children who went to the need at night with barking."
            dv "It's a pity that she gave up so quickly. She could have bargained after all!"
            "I just threw up my hands."
            me "And what would you ask her? 'Give me your potatoes in the evening'?"
            me "You know, your every wish could do more damage to our good girl's reputation than hiding a little animal in the camp."
            me "So go ahead and chew, blackmailer!"
        "I'll handle this" if herc:
            $ lp_dv += 1
            $ karma += 5
            $ alt_day5_dv_dj_sl_jeer = 2
            me "And you'd better get us a seat for now."
            "Alisa looked at me with the deepest bewilderment, but my commanding tone did not allow her to argue. She moved to the nearest free table, and I - to Slavya."
            hide dv with dissolve
            th "I don't like showdowns, oh how I don't like them..."
            dreamgirl "That's why you climbed to the front line, putting the redhead in the rear?"
            stop music fadeout 2
            th "In this situation, I'm more likely to act as a bomb defuser."
            play music music_7dl["nobodys_secret"] fadein 3
            show sl surprise pioneer with dissolve
            "I carefully put my hand on Slavya's shoulder, causing the girl to flinch."
            me "Alisa knows about the dog."
            show sl serious pioneer with dissolve
            "I said quietly in her ear. Slavya exhaled noisily."
            me "I don't want you to be escorted out of camp with that dog in a sack, and she's perfectly capable of doing that if she wants to."
            sl "Is this a threat?"
            "The girl's voice was calm. Frighteningly calm."
            me "This is a warning."
            me "Alisa isn't going to snitch to the squad or the camp leaders, you know. So I'm hoping for your discretion."
            "We both knew perfectly well that Alisa was capable of the worst. Perhaps Slavya even understood this much better than me."
            me "Can you handle this situation yourself?"
            show sl sad pioneer far with dissolve
            "The answer was a short nod. Gently dropping my hand from her shoulder, Slavya got up from the table."
            show sl cry_smile pioneer far with dissolve
            sl "Perhaps I overplayed Anne Frank."
            "She smiled sadly at me before walking away."
            sl "Anyway, thanks for the warning."
            th "You're welcome, honey. Except I didn't do it for you at all."
            show sl cry_smile pioneer far at fleft with move
            show mt normal pioneer far at left behind sl with dissolve
            "If Alisa had figured out what to do with this unpleasant secret - and she certainly would have figured it out! - then both would have got in trouble."
            show mt shocked pioneer far at left behind sl with dissolve
            "Slavya bent over the leader's table, and I could only watch how Olga's face changed dramatically, listening to the sincere confession of her best pioneer."
            th "I may be betraying Alisa, but I'm only doing it for her good!"
            hide mt
            hide sl
            with dissolve
            "After reassuring myself with this, I returned to the table."
            show dv normal pioneer at cright with dissolve
            dv "Well, what did you say to her?"
            me "Nothing good."
            th "Nothing bad, though. Just the bare facts."
            me "Just a little scare."
            show dv laugh pioneer at cright with dissolve
            dv "A little?"
            show sl sad pioneer far at fleft
            show mt angry pioneer far at left behind sl
            with dissolve
            "Alisa raised an eyebrow, nodding at the leader's table. Slavya stood with her head down, while Olga said something obviously not very pleasant to her."
            hide mt
            hide sl
            with dissolve
            me "Who knew she'd get that scared!"
            show dv dontlike pioneer at cright with dissolve
            "The redhead rolled her eyes."
            dv "You're a fool, I'll tell you what. Straight as a rail!"
            me "And you are meandering, huh!"
            with vpunch
            "For such a well-aimed, but unsuccessful characterization from Alisa's point of view, I received a well-deserved kick on the long-suffering knee."
            th "The evening is saved, as is the rest of the shift. Where's my Nobel Peace Prize?"
            dreamgirl "Do you see there are two pies on the shelf?"
            dreamgirl "Yours is in the middle."
            th "I haven't dined with Petrosyan's jokes for a long time...{w} Do you know how to change the channel here?"
            dreamgirl "…"
            dreamgirl "Dude, you're competing in joking with the voice in your head. The house with the yellow walls is crying for you!"
            "I began to chomp with triple strength to drown out all the sounds around - both external and internal."
            th "Enough concerts for today!"
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day5_dv_dj_campfire:
    scene bg ext_square_sunset with fade3
    play music music_list["afterword"] fadein 3
    play ambience ambience_camp_center_evening fadein 1
    th "Who is walking in a row?"
    "Everyone was great at walking, but doing this simple task in a row..."
    $ meet('voice', "Squad leader")
    voice "Kids! In pairs!"
    voice "Pairs are two people! Why are there three of you?"
    $ meet('voice', "Voice")
    "While the leader of the youngest squad unsuccessfully tried to optimize her subordinates, Olga sternly looked at the few oversized dumbasses who were also in no hurry to set an example for the younger ones."
    show mt normal pioneer at left with dissolve
    mt "Seryozha and Sasha, okay, step forward... Lena, are you going with Zhenya?"
    mt "Who is Miku going with?"
    show dv normal pioneer with dissolve
    dv "With me."
    show mi smile pioneer at fright with dissolve
    show dv normal pioneer at cright with move
    "Alisa stepped forward, almost hitting me in the face with the neck of a guitar dangling from a girl on her back."
    "I felt like I've just been sucker punched." with flash_red
    th "What do you mean - with me?"
    dreamgirl "On foot, I guess."
    "An inner voice giggled nastily, adding nothing to the joy of this sharply clouded evening."
    show mt angry pioneer at left with dissolve
    mt "Excellent. Semyon?"
    "All that was left for me was to open my mouth like a fish stranded on dry land after a storm."
    th "And she didn't say a word, bastard! She didn't even look in my direction!"
    "I threw a gloomy look at Alisa, who was already listening attentively to Miku's chirping. She seems to have completely forgotten about my existence."
    me "Well, I don't really care. You can even pair me with a bag of potatoes."
    show mt normal pioneer at left with dissolve
    mt "Great, you're going with Ulyana then."
    show us dontlike sport close with dissolve
    us "What are those hints?"
    us "Do you think I'm worse than a sack of potatoes?"
    show mt angry pioneer at left with dissolve
    "Olga looked sternly at the girl."
    mt "If keep cracking jokes you'll be the one going with that sack. Do you like carrying heavy things?"
    show us calml sport close at fleft with move
    hide mt
    show mi smile pioneer at cright
    show dv normal pioneer at cleft
    with dissolve
    "Muttering something dissatisfied in response, Ulyana pulled me to the ranks. I stood right behind Alisa, diligently not keeping my eyes on the red head."
    th "What a grief - I wanted to chat with my girlfriend. As if we had to hang around together twenty-four by seven!"
    th "I have to admit that Alisa has worn me down a lot with her company all day. It would be better for both of us to get some rest from each other."
    show prologue_dream with dissolve
    dreamgirl "Go on, comfort yourself, sufferer!"
    th "What do you think I'm doing?"
    dreamgirl "Of course not one bit... {w} Wait a minute!"
    dreamgirl "Are you just going to admit that you've been hoping for nothing all this time?"
    th "Yeah. What's left for me?"
    th "I knew exactly what I was getting into. I saw with my own eyes how Alisa treated me, and I could calculate all the extremely predictable and disappointing prospects on the first day."
    th "It was foolish to expect anything beyond friendship from Alisa."
    dreamgirl "But you did expect?"
    th "Who said I'm smart?"
    "It seemed that confessing to myself should have made it easier, but the emptiness treacherously continued to eat my insides, killing the already meager remnants of a good mood."
    "A girl such as Alisa will never be with me."
    if lp_dv < 18:
        th "I'm sorry I'm not good enough to get even a fraction of your attention!"
        th "I'm sorry I run around you like a dog, begging for a little petting, only to get another kick in the stomach over and over again!"
        th "Maybe I should also apologize for trying to help you find yourself while you're running around and pretending like childhood is endless?"
    else:
        th "She would have to find someone stronger, stronger, more reliable. Not physically, - she herself is like Hercules with us - morally."
        th "What can I give to a lost girl, if I myself am only a lost wanderer here, who, by an inexplicable will of fate, found my temporary home in this warm world of carefree youth and summer?"
        th "I'll only further shake Alisa's already precarious state by extending my trembling hand to her."
    hide prologue_dream
    show us normal sport close at fleft
    with dissolve
    us "Newbie!"
    me "Where?"
    us "In Karaganda. Did you see Slavya?"
    "Apparently, my bitterness also dulled my eyesight - I did not notice that the activist had disappeared somewhere."
    th "Was she really deported?"
    "A chill ran down my spine."
    me "Didn't see her."
    th "And if Alisa and I are to blame for this..."
    "Joyfully seizing on this problem, as if on a saving straw, I began frantically to look for light braids among the pioneers."
    show mt surprise pioneer at fright with dissolve
    "For a second, my gaze met a pair of attentive green eyes."
    "Olga was also looking for someone."
    th "Did Slavya not stand the shame and went on the run with the dog under her arm? What a performance!"
    "And although my version looked ridiculously implausible, I could not find any other reason to trample on the square - all the pioneers had already calmed down and even managed to line up."
    show us surp1 sport close at fleft with dissolve
    us "Look, there they are!"
    hide mt
    hide us
    hide dv
    hide mi
    with dissolve
    $ alt_pause(0.5)
    show sl serious pioneer far at left with dissolve
    show cs normal far at right with dissolve
    "I turned in the direction indicated by Ulyana - indeed, Viola and the once most decent and responsible pioneer of the entire camp, now simply Slavya, were hurrying towards us from the side of the infirmary."
    th "Were they looking for fleas on her, or what?.."
    stop music fadeout 3
    hide sl
    hide cs
    with dissolve
    $ alt_pause(0.5)
    show mt smile pioneer with dissolve
    "Olga nodded in satisfaction, barely seeing the approaching couple."
    mt "Squads, line up! Attention!"
    show mt normal pioneer with dissolve
    mt "March!"
    play music "<to 95.6>" + music_7dl["nowyouseeme"] fadein 3
    scene bg ext_backroad_sunset_7dl with dissolve
    play ambience ambience_forest_evening fadein 2
    "In a buzzing line, we followed the cyberneticians assigned as honorary custodians."
    show dv normal pioneer at cleft
    show mi smile pioneer at right
    with dissolve
    "I tried my best to force myself to admire nature, and not listen to Alisa and Miku's conversation, but I was pretty shit at it."
    mi "...and then they started calling me to all the TV shows!"
    show dv dontlike pioneer at cleft with dissolve
    dv "You're funny. Are you okay with that?"
    show mi sad pioneer at right with dissolve
    mi "What's wrong with everyone being interested in you? It's such a breakthrough step for a career, Sakishita-san always said..."
    dv "Bad? I don't know."
    dv "Like being labeled with a label that you have to live up to until you die if you don't want to be forgotten?"
    show mi shocked pioneer at right with dissolve
    mi "But I just perform, sing my songs, and people love it!"
    show dv normal pioneer at cleft with dissolve
    dv "That's until you were replaced by, let's say, desperate Ami. What will you do when she gets on the front pages of all magazines?"
    dv "That's right, something that will be able to outshout it. And so on ad infinitum, Miku - hungry for fame are dime a dozen, and only the very lucky or very rich get it."
    show mi dontlike pioneer at right with dissolve
    mi "What nonsense! You're just a coward, admit it!"
    show dv smile pioneer at cleft with dissolve
    dv "And I'll admit it, if it makes you feel better."
    "I annoyed myself with the fact that I was about to start stepping on the heels of the girls, trying to catch their every word."
    show us smile sport close with dissolve
    us "It's not good to eavesdrop!"
    $ renpy.show("bg ext_backroad_sunset_7dl", what = Desat("bg ext_backroad_sunset_7dl"))
    with dissolve
    $ volume(0.3, "music")
    "In the blink of an eye, everyone around me fell silent. I literally felt the curious glances from behind with my shoulder blades."
    show mi surprise pioneer at right with dissolve
    mi "Who's eavesdropping?"
    show dv concent pioneer at cleft with dissolve
    "Miku turned around, wide-eyed, and began to look for a potential spy somewhere behind me. Alisa dropped her face into her hands with a loud pop."
    "Because of our hitch, the movement abruptly stopped, and the silence began to fill the discontented hum of the younger pioneers."
    $ volume(1.0, "music")
    show dv angry pioneer at left with dissolve
    show bg ext_backroad_sunset_7dl with dissolve
    dv "And what did you do again?"
    show us upset sport close with dissolve
    "The red-haired eldest shushed at the red-haired youngest. She sank her head guiltily into her shoulders."
    us "I got bored."
    us "And this unlucky one can't even talk - he can only hang his ears!"
    me "Oh you…"
    show mt angry pioneer far at cleft behind dv, us with dissolve
    mt "What's wrong with you again?"
    "The squad leader loomed over us, immediately shutting up everyone who wanted to express their claims."
    show dv normal pioneer at left with dissolve
    dv "Nothing. Miku's lace came undone."
    mt "That didn't make it necessary to stop everyone!"
    show mt normal pioneer far with dissolve
    show us angry sport close with dissolve
    "Having finally measured us with a prophylactic stern look, Olga shouted:"
    mt "Squads, march forward!"
    hide mt with dissolve
    show dv normal pioneer at cleft with dissolve
    $ alt_pause(0.3)
    show us angry sport behind dv with dissolve
    with vpunch
    $ alt_pause(0.2)
    show dv normal pioneer at fleft
    show us angry sport behind dv at left
    with move
    "Alisa grabbed the frowning Ulyana by the hand and pulled her towards her."
    dv "You're coming with me."
    "Certainly she declared."
    th "And I, as it turns out, inherited..."
    show mi smile pioneer close at cright with dissolve
    mi "Semyon!"
    mi "To be honest, I still didn't understand who was there and what was eavesdropping, but I noticed a long time ago that those boys from the second squad were acting strangely…"
    th "If I ignore it, it will go away."
    dreamgirl "Only if a bear jumps out of the bushes and drags it into the forest."
    th "God almighty, let that bear jump out of from my side!"
    show mi smile2 pioneer close at cright
    show dv angry pioneer at fleft
    with dissolve
    "Walking ahead, Alisa quarreled softly with Ulyana about something - Miku's cheerful chatter did not allow me to make out their conversation."
    th "I wonder how Alisa manages to completely forget about my existence at the snap of her fingers?"
    if lp_dv < 18:
        th "It's like I'm like this to her, a trinket toy - a more interesting activity appears on the horizon, as I immediately fly to gather dust on a shelf until the next bout of deadly boredom."
    else:
        th "I mean, I get it, but this is already starting to piss me off!"
    show mi grin pioneer close at cright with dissolve
    mi "...and then I found out that I would only have to sing them during the fire."
    me "Yeah, cool."
    show mi dontlike pioneer close at cright with dissolve
    "Miku blinked her eyes stupidly, staring blankly at my scowling face."
    mi "You weren't listening to me!"
    me "I've been thinking."
    show mi sad pioneer close at cright with dissolve
    "Japanese chuckled offendedly."
    mi "Then you could have at least not pretended to be interested!"
    th "Did I pretend?"
    th "If you, silly, read the expression “don't get in - you'll die” as the interlocutor's interest in the conversation, then you have obvious problems with empathy."
    me "How much longer do we have to go?"
    mi "We're there."
    th "Looks like she's really offended - that's the shortest sentence I've heard from her all shift!"
    stop music fadeout 3
    scene bg ext_polyana_night with fade3
    "In the meantime, the scenery really changed: we came to a campfire meadow. {w}There weren't any special sights here - except for a large fire pit and a pile of logs neatly laid out around."
    show mt smile pioneer with dissolve
    mt "Semyon, can you light a fire?"
    if herc:
        me "I haven't done this in years, so I can't promise anything…"
    else:
        me "Yu know, I'm a city guy…"
    play music music_7dl["fatest"] fadein 3
    show mt normal pioneer with dissolve
    "Olga waved her hand."
    mt "Men these days! Slavya!"
    hide mt with dissolve
    "The squad leader retired to the fire pit, where the cyberneticists were already trying to fit in a bag of potatoes. Both looked very rumpled - looks like the provisions were carried in turn."
    show mi normal pioneer with dissolve
    mi "I wonder why she didn't immediately ask Slavya, she always makes a fire, she's just a professional in this business!"
    "Looks like Miku's curiosity outweighed her resentment towards me."
    me "I have no idea. I guess she figured camping was my secret hobby."
    show mi dontlike pioneer with dissolve
    "Miku looked at me with annoyance again."
    mi "バカ!"
    hide mi with dissolve
    "And, defiantly with her nose up, she walked away - to Alisa, who was tuning her guitar on the nearest log."
    th "Well that was awkward…"
    th "And I don't know how to approach the redhead, and now I can't ask for the company of this crazy one. That's how you spit in the well!"
    play sound_loop sfx_forest_fireplace fadein 3
    "I sat on the edge of a log, standing on the outskirts, and stared at the flaring branches."
    "It was rapidly getting dark, and the firefield became smaller and tighter, as if the darkness advancing from all sides pressed us to each other. Only I sat cut off from the rest, not taking my eyes off the bright point in the distance."
    stop music fadeout 3
    "From copper-red hair, shimmering red in the firelight."
    $ alt_pause(1)
    play music music_7dl["hey_you"] fadein 3
    show dv sad pioneer far at right with dissolve
    th "Not looking."
    "Alisa plucked the strings without opening her mouth - only the children sitting around sang. Her eyes were lowered down, as if she did not want to see anything."
    th "Not looking for anyone."
    voice "{i}If everyone lived alone,{/i}"
    voice "{i}It's been in pieces for a long time{/i}"
    voice "{i}The Earth would probably fall apart...{/i}"
    th "Doesn't feel like something is missing."
    "A flock of squealing girls ran past me, followed by a boy of Ulyankin's years with a tiny snake in his hand."
    th "You were my only link to this world, Alisa. And now that I'm feeling abandoned and alone, there's nothing holding me back."
    show el smile2 pioneer with dissolve
    el "Olga Dmitrievna, the coals are ready! We are throwing in the first batch!"
    hide el with dissolve
    th "Those stupid childish gatherings..."
    th "One day I would have felt inexhaustible joy and even naive pride just to belong to this place. This camp, this motley but amazing squad."
    "I got up from the log and walked away without feeling a single glance on my back."
    stop sound_loop fadeout 2
    $ persistent.sprite_time = 'night'
    $ night_time()
    scene bg ext_path2_night with fade2
    th "I'm leaving. I'm leaving the way she taught me."
    th "Alisa doesn't say goodbye - she leaves the English way, only to return later as if nothing had happened. She doesn't rejoice at the meeting - casually nods her head to notify me that she is aware of my presence."
    th "Like she doesn't need me. Like she doesn't need anyone in the whole wide world - just her loneliness."
    th "A blank concrete wall separates us, and I sit by it for days, pressing my ear close and forgetting about breathing, just to hear something on the other side."
    th "I can't take it anymore!"
    th "And every damn time I think Alisa opens up, it turns out to be just my fantasy, infinitely far from reality."
    th "This wall is too high, and all my efforts are meaningless - I'll never break through it. But I can't get it out of my head either: obsessive thoughts devour the mind like earthworms."
    th "And you're not helping me! Not at all!"
    th "We're just dying quietly on opposite sides of the barricades."
    scene bg ext_lake_night_7dl with fade2
    play ambience ambience_lake_shore_night fadein 2
    "The path led me to a lake. I closed my eyes and took a deep breath of the damp night air, as if to soothe my burnt ego."
    show blink
    dreamgirl "Oh, how sorry you feel for yourself..."
    th "I don't feel sorry for myself. I grieve that I imagined myself a redheaded carefree happiness and believed that it was real."
    th "Only does it happen in this life that they bring happiness on a silver platter, carefully pushing you to it with their nose, so that you, a funny idiot, don't miss this tasty morsel?"
    th "I'm sorry for this wonderful world that exists only in my imagination. I'm sorry that it shatters into pieces over and over again when it collides with the real world."
    show unblink
    hide blink
    "The wind ruffled my hair, bringing a light aroma of smoke and nasty screams of someone else's fun to the point of pain in my teeth."
    th "I haven't really lost anything."
    th "To lose something, you have to have it. But who's to blame for the fact that I'm a fool, and a fool in an incurable stage?"
    "I sat down on the grass and put my head in my hands. I wanted to howl desperately."
    stop music fadeout 3
    dv "I kept wondering if you were going to get lost or not. You can congratulate me on another sure bet."
    play music music_7dl["sleeping_beauty"] fadein 3
    "Her voice pulled me out of my daze - just for a second and only to pull me into something much more: suffocating, icy, desperate."
    th "You torment me when you're not around, Alisa. And torment me a hundred times more when you're in my sight."
    me "Did I call you after me?"
    "I heard - {i}barely caught{/i} - a sharp sigh, as if my words had struck her to the core."
    th "Who are you trying to fool? We both understand that you know no other emotion than burning anger."
    dv "Why did you leave?"
    th "Because I'm tired of watching you not look at me!"
    me "A sense of tact, Dvachevskaya. Have you heard of such a thing?"
    me "I think I made it pretty clear that I don't want to see anyone."
    dv "Even me?"
    "Her voice cracked, turning the end of her sentence into a low squeak."
    me "What makes you different from the rest?"
    "I looked at the small ripples that carried the dim moonlight across the surface of the lake. I would not have had the courage to look back."
    th "Festering wounds must be opened if you want them to heal."
    "And I was literally oozing poison."
    th "So be it. Let her see what an ugly creature is circling around. Let her be horrified and run away before it's too late."
    th "And I will finally find peace. I will return to that spiritual coma in which I have been perfectly all these years - it's sickening there, but there is no place for pain."
    dv "What's the matter with you?!"
    "I grimaced - her scream made me flinch."
    th "Am I that weak?"
    th "Am I just going to turn around and forget everything? Am I going to let her keep me on a short leash without putting me down?"
    me "Go away, Alisa."
    th "Go away and don't let me cherish my false hopes anymore!"
    dv "You forgot that you are indebted."
    "She spoke evenly, without anguish, without malice. She spoke as if she agreed that this was our last dialogue."
    th "Ah, that's how it is..."
    th "You're a bigger bitch than I could have imagined. You only came because you need me for some dirty trick."
    th "Here and now. Take it out and put it in."
    th "Good Semyon, comfortable. You can pat his head and leave, throwing him out of your thoughts until it gets too boring!"
    me "I'll do whatever you say if you leave me after that."
    dv "Listen to me!"
    me "All in attention."
    show dv rage pioneer close with vpunch
    "A sharp tug on my shoulder made me turn around."
    "The heart sank with a thump, and the mind was clouded with haze."
    "Before me were her eyes. Evil, glowing."
    "So familiar."
    dv "That's my wish, idiot! I want you to listen to me!"
    show dv rage pioneer close at ba_sit_down_unfzdv
    show dv angry pioneer close with dissolve
    "Alisa sat down on the grass, almost burning me with her eyes. Not knowing what I was doing, I turned around, settling opposite her."
    th "I fail again."
    th "And I marvel at you again."
    $ alt_pause(1.0)
    "And Alisa studied me all this time, hypnotized me. Or maybe she was just gathering her courage."
    th "What's the difference anyway?"
    show dv guilty pioneer close with dissolve
    dv "Ever since you gave me the player, I've been feeling weird. I can't sleep at night, and I can't find the strength to live during the day."
    show dv sad pioneer close with dissolve
    dv "Nonsense, Semyon. It seems to me that everything that is happening is sheer nonsense."
    dv "It's like in an instant life has become a crappy school play that I'm being forced into."
    dv "And I can't find my old self, no matter how hard I try. I want to be that Alisa again who brings trouble and enjoys it, and not a pathetic parody!"
    show dv closed_eyes pioneer close:
        ypos 0.15
    with dissolve
    "She closed her eyes, wrinkling her forehead and rubbing it with her hand."
    dv "But inside something has changed. And I can't figure out what it is."
    dv "And every damn time I manage to sleep, I get nightmares."
    show dv sad pioneer close with dissolve
    th "What should I tell you in response to your confession?"
    me "Why are you telling me about this? You have Ulyana, Miku…"
    "Alisa shook her head."
    dv "They won't understand. I just feel…know you're just like me."
    dv "Lost."
    show dv sad_smile pioneer close with dissolve
    "She looked straight into my eyes and I froze, unable to look away."
    dv "When you're around, it's like I'm back to being myself."
    "Her hand timidly, centimeter by centimeter, approached mine. Her voice dropped to a barely audible whisper, forcing me to lean lower towards her face."
    dv "When you're around, it's so easy for me to convince myself that these nightmares are just bad dreams..."
    show dv shy pioneer close with dspr
    show dv shy pioneer close:
        linear 1.25 zoom 1.2
    "I squeezed her cold fingers. Alisa exhaled in amazement, raising her head and reducing the distance between us to mere millimeters."
    show dv sad_smile pioneer close:
        ypos 0.15
    with dissolve
    "Eye to eye. Like yesterday morning, like this afternoon, but at the same time completely different."
    "No antics, no laughter, no childishness."
    "For the first time, we dropped all the masks, showing ourselves to each other."
    show dv closed_eyes pioneer close:
        ypos 0.15
    with dissolve
    th "We are so different: icy Petersburg splashes in my eyes, rebellious youth blazes in her soul. So different, but for some reason…"
    window hide
    with flash_pink
    window auto
    me "I love you too."
    "I didn’t know what was more in this kiss - despair or hope. Or maybe both of them with a vengeance - too many feelings were mixed in me to understand at least something."
    "Alisa clung to me, digging her fingers into my shoulders, tangling her hands in my hair, biting my lower lip until it bled."
    th "You know that feeling when you've been looking for something unknown for ages and now you're trying to get it all?"
    "She buried her nose in my collarbones, and I, clenching my numb body to pain in my arms, inhaled the bitter aroma of disheveled hair - every breath is like the last."
    stop music fadeout 6
    me "What a fool you are, Alisa."
    show dv shy pioneer close with dissolve
    dv "Why so?"
    "The girl tried to pull away, but I only held her tighter against my chest."
    me "Because maybe."
    show dv smile pioneer close with dissolve
    dv "You're no better, and you're also name-calling!"
    "I kissed her gently on the top of the head."
    me "And we have a rule like this - whoever puts on the first coat is the doctor."
    show dv grin pioneer close with dissolve
    "Alisa snorted."
    dv "So what should I do with you now?"
    me "Cherish! Where else can you find such an enviable groom for yourself?"
    show dv laugh pioneer close with dspr
    show dv laugh pioneer close at stand_up_7dl
    $ alt_pause(1.0)
    "Smiling, the girl deftly got out of my hands."
    show dv grin pioneer with dissolve
    dv "I see you have no self-conceit. Let's go, enviable one!"
    me "Are we in a hurry somewhere? Just look, what a night..."
    show dv smile pioneer with dissolve
    dv "To the fire, bastard! My guitar's there!"
    th "Well, this, of course, is more important than any stupid rrromanticism out there!"
    dreamgirl "Of course!"
    dreamgirl "She has had a guitar for a long time, and this is the first time she sees this Semyon."
    "I got up after Alisa and held out my hand to her. The girl arched an eyebrow."
    show dv normal pioneer with dissolve
    dv "Afraid I'll run away?"
    me "Yes. Just you wait, tomorrow I'll get a leash!"
    show dv soft_smile pioneer with dissolve
    dv "We'll see who'll be the first to howl and go on the run!"
    show dv smile pioneer with dissolve
    "She squeezed my hand, pulling me with her to where the voices roared."
    scene bg ext_path2_night with dissolve
    play ambience ambience_forest_night fadein 3
    th "So what - all this time we could just talk?"
    dreamgirl "Both of you are clowns, no, not even that, you're the entire circus, what talking could there be?"
    dreamgirl "All you can do is juggle jokes."
    th "That's right."
    th "Except there's only one question left..."
    th "Which one is the real Alisa - the one that does not feel the strength to live, or the one that is able to turn all this life into a black joke?"
    scene bg ext_polyana_night with fade3
    play music music_7dl["wonderful_faraway"] fadein 3
    "It was noisy on the campfire - the camp was singing “Beautiful Far Away” with almost the entire staff, completely blocking Miku's accompaniment with their voices."
    we "{i}From a pure source,{/i}"
    we "{i}To a beautiful distance{/i}"
    we "{i}To a beautiful far away,{/i}"
    we "{i}I'm starting the journey!{/i}"
    th "And I think I started mine this night too."
    show un serious pioneer with dissolve
    "Alisa and I froze at the most distant logs. No one noticed our appearance - only Lena squinted, furrowing her eyebrows."
    if alt_day5_dv_dj_map == "un":
        show un sad pioneer with dissolve
        "Our eyes crossed literally for a moment - she immediately stared at the fire, continuing to sing. {w} I could not help noticing that the movements of her lips did not coincide with the words of the song at all."
    stop music fadeout 3
    scene bg ext_polyana_night with joff_r
    show mt normal pioneer with dissolve
    mt "Teams, thank you all for the excellent knowledge and sincere performance of the songs!"
    mt "Line up in pairs!"
    hide mt with dissolve
    show dv normal pioneer with dissolve
    "Alisa unobtrusively released her hand from mine."
    show dv grin pioneer with dissolve
    "I rolled my eyes theatrically, causing the girl to chuckle."
    dv "We're not in kindergarten to hold hands!"
    "And in the most kindergartenish way, she stuck her tongue out at me before moving towards the group gathering by the path."
    th "Well then, just go!"
    th "It's just her style. Annoying as hell, but almost familiar."
    th "She'll be back anyway. Now I'm sure of it."
    "I followed behind, hiding a stupid smile."
    scene bg ext_path2_night
    show dv normal pioneer
    with dissolve
    play ambience ambience_forest_night fadein 1
    play music music_7dl["fatest"] fadein 3
    "We left the forest only after making sure that the fire was completely extinguished."
    "The pioneers yawned in unison, and behaved uncommonly quieter than on the way to this parody of a hike."
    show dv think pioneer with dissolve
    dv "I wonder who ate the potatoes we were given?"
    "Aliska's neighbor's quiet giggle behind our backs answered this question quite exhaustively."
    dreamgirl "She went looking for you without waiting for the potatoes?"
    dreamgirl "It looks like serious feelings!"
    me "Well, at least we didn't drag her on our hump..."
    "The conversation didn't go well - we were both too exhausted, both physically and mentally."
    "I was almost sure that those soul effusions on the shore of the lake were hard for Alisa, oh how difficult they were, and from this a strange joy seethed inside."
    "Male and very, very possessive."
    th "You look like something one really wants to have, Alisa."
    th "Like something attractive, mysterious, but so inaccessible - even if you hurt yourself, you can't grab it with your hands."
    th "It's annoying, it's depressing, it makes you want to scream and howl like a wolf, sweeping away everything in its path."
    th "But at the same time, it gives strength to live, making you open your eyes every morning."
    th "Did I dare to dream that one day I would experience it all again?"
    scene bg ext_square_night with fade3
    play ambience ambience_camp_center_night fadein 2
    "On the square, the squads split up: the squad leaders led frankly sleepy kids to the washbasins, and we slowed down at the turn to the houses."
    show dv tired pioneer with dissolve
    "I looked at Alisa - she yawned, covering her mouth with her fist."
    show mt normal pioneer at left with dissolve
    mt "Hurry up to wash your face and go to sleep! Tomorrow we have a long and busy day, so no gatherings."
    "To my surprise, she kept her gaze not on the tandem of redheads, but on Miku and Lena."
    hide mt with dissolve
    th "I never thought those two would gossip at night under the same blanket!"
    dreamgirl "And why did you decide that there's only one blanket?"
    dreamgirl "However, it doesn't matter, I like your way of thinking!"
    show dv normal pioneer with dissolve
    "Alisa and I locked eyes."
    me "Goodnight?"
    dv "Uh-huh."
    show dv surprise pioneer close with dissolve
    "She was moving towards the fork, but I grabbed her by the elbow, turning her towards me."
    me "Not 'uh-huh', but 'good night, my dear and beloved Semyon'!"
    dv "You…"
    me "Dumbass, I know."
    window hide
    with flash_pink
    window auto
    "I gave her a quick kiss before she could respond - fortunately, the darkness kept us from potential onlookers."
    me "But still read books on etiquette when you have the time."
    show dv normal pioneer close with dissolve
    dv "Shove your books up your…"
    show us normal sport far at fleft with dissolve
    us "Liska! Are you coming or not?"
    hide us with dissolve
    show dv smile pioneer close with dissolve
    dv "Goodnight."
    th "Ho-ly shit!"
    th "At this rate, she'll be saying hello soon!"
    show dv smile pioneer with dissolve
    $ alt_pause(0.33)
    hide dv with dissolve
    "Smiling at the darkness in which Alisa disappeared, I trudged into the house."
    th "I'll wash myself, perhaps, in the morning. Olga won't force me to do it now, right?"
    stop ambience fadeout 3
    stop music fadeout 3
    return

label alt_day5_dv_dj_sleeptime:
    scene bg int_house_of_mt_night2 with fade3
    play music music_7dl["melancholy_sun"] fadein 3
    "As soon as I entered the house, I felt a leaden fatigue that rolled in, insanely pulling me to the bed."
    "It was only the pitiful remnants of my mind that forced me to undress before collapsing into a rough-and-ready bed."
    th "What a day!"
    "The eyes were closed, and in front of them, like a filmstrip, pictures pleasing to the eye and heart flashed."
    show blink
    $ alt_pause(0.5)
    scene anim prolog_2
    with fade
    $ alt_pause(1)
    $ set_mode_nvl()
    scene bg int_clubs_dj_7dl
    show el normal pioneer at fleft
    show dv laugh pioneer
    show mi smile pioneer at right
    show prologue_dream
    with dissolve
    $ alt_pause(2)
    "Our chaotic but still fun morning debut as radio hosts…"
    if alt_day5_dv_dj_map == "dv":
        nvl clear
        scene cg d5_dv_sleep_together2_7dl
        show prologue_dream
        $ alt_pause(2)
        "And our touching afternoon nap."
    elif alt_day5_dv_dj_map == "un":
        nvl clear
        scene bg ext_library_day
        show un sad pioneer
        show prologue_dream
        $ alt_pause(2)
        "And that strange confession of Lena, which gives more questions than answers."
    elif alt_day5_dv_dj_map == "us":
        scene bg ext_square_day
        show us smile sport
        show prologue_dream
        $ alt_pause(2)
        "And incredible races around the camp with Ulyana."
    elif alt_day5_dv_dj_map == "cyber":
        nvl clear
        show prologue_dream
        $ alt_pause(2)
        "And so many interesting things that I missed."
    else:
        nvl clear
        show prologue_dream
        $ alt_pause(2)
        "And that strange dream... wait, what did I even dream about?"
    nvl clear
    scene bg ext_lake_night_7dl
    show dv shy pioneer close
    show prologue_dream
    $ alt_pause(2)
    "My anxieties and torments, which I myself came up with..."
    "Alisa's revelations, which instantly overshadowed all this empty nonsense ..."
    "And our kiss."
    $ set_mode_adv()
    scene bg int_house_of_mt_night2 with fade3
    play sound sfx_open_dooor_campus_2
    "The door creaked softly."
    mt "Well, you're dirty! Even the appearance of a girl did not make you start washing."
    me "But I'm not sleeping with her!"
    "I grumbled into the pillow, turning to the wall."
    "Olga chuckled softly."
    mt "Good night, piggy."
    me "Who's name is…"
    "Whether I finished my sentence, and what I was for it, I was not destined to know."
    "I was dragged into my dreams."
    stop ambience fadeout 3
    stop music fadeout 3
    return

label alt_day6_dv_dj_morning:
    scene black with dissolve
    play ambience ambience_int_cabin_day fadein 3
    "The morning tried to take away from me all the touches of warm hands that I saw in that wonderful dream, but I desperately resisted."
    "I rushed about, kicked, covered myself with a blanket and screwed up my eyes with all the might in a vain attempt to swim back, but the singing of birds treacherously confirmed the fact:"
    play music music_list["timid_girl"] fadein 3
    scene bg int_house_of_mt_sunset with dissolve
    th "I'm already awake."
    show mt smile pioneer with dissolve
    mt "Did you know you talk in your sleep?"
    me "And what did I say?"
    show mt grin pioneer with dspr
    "Having admired my horror-contorted face enough, the squad leader giggled."
    show mt grin panama pioneer with dspr
    mt "Nothing compromising."
    show mt smile panama pioneer far with dissolve
    "And, before walking out the door, she winked at me:"
    mt "Wouldn't it be wrong if I said that your favorite movie is 'Guest from the Future'?"
    hide mt with dissolve
    play sound sfx_close_door_1
    dreamgirl "Invited her to show her your myelophone in the dream?"
    th "Confess, are you and Olga related?"
    "The alarm clock on the leader's nightstand said it was still early for the average pioneer trying to enroll to firefighters, so I rushed to the washbasins like a bullet."
    th "I've wasted too much time already!"
    th "I'll make up for it today!"
    stop ambience fadeout 1.6
    scene black with blinds_l
    $ alt_pause(0.5)
    scene bg ext_house_of_dv_day with blinds_r
    play ambience ambience_camp_center_day fadein 3
    "Having thrown the bathing supplies into the cabin (and, judging by the sound, scattering all the contents of the package on the floor in flight), I rushed along the shortest paths to the cabin, which was customary to pass by in this camp."
    show bg ext_house_of_dv_day:
        zoom 1.4
        align (0.7, 0.7)
    with dissolve
    "Olga was no longer there, and I sank down on the step with relief. I did not dare to go into the cabin."
    th "You never know - maybe the ladies are changing clothes..."
    dreamgirl "So you could stop by and see if they need any help."
    dreamgirl "Maybe suddenly something doesn't fit on the back!"
    th "Yeah, Ulyana's. She needs it the most!"
    play sound sfx_bush_leaves
    "The bushes to my right rustled, and I jumped in fright."
    th "If Olga sees me here..."
    th "Then what, exactly?"
    th "I'm not staring out the window, but sitting dignifiedly on the step, chastely turning my back on all sources of temptation for the young organism."
    th "Good pioneer, decent!"
    "A shaggy, curly head emerged from the bushes, followed by its owner."
    $ meet('dn',"Danya")
    show dn normal pioneer with dissolve
    "Danechka, Ulyankin's faithful comrade - also her “groom”."
    me "Good morning. Spying on girls changing clothes?"
    show dn dontlike pioneer with dspr
    "Pioneer looked at me with hostility."
    dn "Look at yourself!"
    me "Back at you!"
    dn "No, back at you!"
    "The conversation wasn't going well."
    "I graciously moved to the edge of the step, making way for the boy."
    show dn normal pioneer close with dissolve
    "He sank down next to me, but his face did not become more friendly."
    "For a minute we sat in silence, occasionally throwing inquiring glances at each other."
    dn "Alisa?"
    "Danya finally asked."
    "I nodded briefly."
    me "Ulya?"
    "I asked in return."
    "I received an equally reserved nod in response."
    show dn unsured pioneer close with dspr
    dn "They're taking a long time."
    me "Women usually don't gather quickly."
    show dn sad pioneer close with dspr
    "Danya sighed."
    me "Hey... you're planning to invite her to a slow dance?"
    "I asked almost in a whisper."
    show dn unsured pioneer close with dspr
    "The boy shivered."
    dn "It's kind of awkward…"
    me "And I'm embarrassed. But I have to."
    me "Such is our fate."
    dn "What if she comes in a dress, and I only have a uniform left of clean clothes!"
    me "Don't worry, it's an evening dance - it'll be dark."
    show dn sad pioneer close with dspr
    dn "That's what I hope for…"
    play sound sfx_open_dooor_campus_1
    scene bg ext_house_of_dv_day
    show dn surprise pioneer at right
    with dissolve
    "The door swung open, and we barely had time to jump to the side so as not to get our backs thrashed."
    show dv normal sport at left
    show dn normal pioneer
    with dissolve
    dv "And what are you two doing here?"
    show us dontlike sport far with dissolve
    "A second red head immediately sprouted from Alisa's shoulder."
    us "Why are you here so early? You knew I wouldn't get up on time today!"
    dreamgirl "Interesting..."
    dreamgirl "What did they do during the night so exhausting?"
    show dn normal pioneer
    show us normal sport
    with dissolve
    "Having rounded her friend, Ulyana jumped out into the street and ran up to Danya."
    "There was not a hint of embarrassment on the boy's face, and I seriously envied his ability to remain calm."
    hide dn
    hide us
    with moveoutright
    "The kids ran off to the square, leaving me alone with Alisa."
    me "Good morning."
    dv "Uh-h…"
    show dv shocked sport close with dissolve
    dv "AAAH!"
    "In order to drive the remnants of sleep from Alisa, it was enough just to grab her by the sides."
    show dv laugh sport close with dspr
    dv "Okay, okay, good morning, just stop tickling!"
    me "That's better."
    show dv shy sport close with dspr
    "Pecking my ill-mannered girlfriend on the forehead, I dropped my hands."
    show dv angry sport close
    with vpunch
    "And then got a sore flick!"
    me "And why me?"
    dv "And there is nothing to solicit in broad daylight. There are children walking around!"
    me "Fine, you've persuaded me: I'll start harassing you when the kids aren't around."
    show dv smile sport close with dspr
    stop music fadeout 3
    "Alisa chuckled (somehow approvingly?) and rushed to the square."
    scene bg ext_square_day with fade3
    "Exercising today was carried out by Sanich, with all his appearance eloquently demonstrating how he relates to this important morning event."
    show ba rage uniform with dissolve
    play music music_list["always_ready"] fadein 3
    ba "Move, get out! I can see you all, those who try to be lazy will do push-ups instead of breakfast!"
    "Olga covered her eyes with her palm, silently muttering either a prayer or a curse."
    "The red-haired leader of the second squad was frankly having fun, but the leader of the fifth squad was already mentally considering a list of psychological traumas with which her children would leave home."
    show ba evil uniform with dspr
    ba "Who yawned there? Ten squats out of turn!"
    show ba rage uniform with vpunch
    ba "FOR EVERYONE!"
    show dv angry sport close at right with dissolve
    dv "If I had known what this would lead to, I myself would have run to disguise Slavya's dog, so that it would certainly not be found..."
    "Alisa hissed, rubbing her ear deafened by the teacher's bassy voice."
    show dv scared sport close
    show ba evil uniform
    with vpunch
    ba "Conversations in formation!"
    show dv shocked sport close with dspr
    ba "Five more squats!"
    stop music fadeout 4
    stop ambience fadeout 3
    hide dv
    show ba em1 uniform
    with joff_r
    $ alt_pause(0.7)
    play music music_list["so_good_to_be_careless"] fadein 3
    play ambience ambience_camp_center_day fadein 2
    "Fifty-six squats later, only Ulyana's legs were bent, and even she did not show any desire to continue our punitive sports marathon."
    "Boris gloomily looked at the exhausted crowd."
    ba "And you weaklings still dare to be called the future of our country?"
    show ba evil uniform with dspr
    ba "In my time you would not have been accepted into the Komsomol with such physical training!"
    show ba normal uniform with dspr
    ba "Oh, I haven't worked on you in a long while, oh I haven't…"
    show mt normal panama pioneer at right with dissolve
    mt "Thank you, Boris Aleksandrovich. And now let's line up!"
    "Olga tried with all her might to stop the raging bear."
    "To everyone's relief, he had just completed his annual norm of educational work and was already looking impatiently towards the canteen."
    hide mt
    hide ba
    show dv tired sport close at cright
    with dissolve
    "Alisa and I set off towards our place, wincing in sync with every step we took."
    dv "Never before have I been so happy that there is no exercise on the last day."
    me "So we have how many days of suffering left?.."
    show dv normal sport close with dspr
    dv "Zero."
    dv "We're leaving tomorrow, dumbass!"
    th "What do you mean tomorrow?!" with vpunch
    hide dv with dissolve
    "While the pioneers reluctantly lined up, complaining loudly about the pain in their strained muscles, I tried to brainstorm what I had just heard."
    th "And what does it turn out - everything was in vain?"
    th "I hesitated so much and did not dare to approach Alisa, so that at that moment, when I believe that everything is real with us, will it end like this?"
    dreamgirl "Ah, well, if that's the case, then we'll have to make this shift everlasting!"
    dreamgirl "Who are you praying to so you don't remember God in vain? Random?"
    dreamgirl "So let your Random arrange everything!"
    th "More like him than your unsolicited jokes!"
    "I found Alisa's hand with my fingers and squeezed softly."
    "With all the despair that fills me."
    if lp_dv >= 18:
        show dv shy sport close at cright with dissolve
        "She squeezed my cold fingers painfully in response before gently releasing her hand."
    else:
        show dv angry sport close at cright with dissolve
        "The girl yanked her hand out of my grasp as if she had been burned."
        dv "Not in public!"
    hide dv
    show mt normal panama pioneer
    with dissolve
    mt "I also want to announce that our radio broadcast today will be special!"
    "Alisa and I didn't even need to look at each other to understand: it smells like kerosene."
    mt "Everyone can come and send greetings and wishes to their friends live."
    th "If the same guys who wrote the questions that we sent to the trash come, then Alisa and I will end our shift much ahead of schedule!"
    th "I am amazed at our leader: to strictly punish so that the broadcasts are serious and without missteps, and then let a crowd of unintelligent children into our radio room."
    th "Smells like mutually exclusive paragraphs."
    dreamgirl "And you take a piece of paper and write down who came and what time. Arrogant pranksters will greatly reduce it!"
    th "And in the first half hour we will have three Vasya Pupkins from the sixty-nineth squad, of course."
    dreamgirl "I wish I had your innate ability to whine..."
    mt "Now, everyone, five minutes to change, and I'll see you in the cafeteria!"
    scene bg ext_square2_day_7dl
    with dissolve
    "I looked after Alisa, who had gone after the crowd towards the houses, and sat down on the nearest bench."
    "My legs were buzzing so that I was ready to swear - I was destined to spend the rest of the shift chained by paralysis to this very bench."
    show mi happy pioneer with dissolve
    mi "Good morning!"
    "Miku chirped in my ear."
    th "Here's someone who will be alert and full of energy today! She wasn't at the exercises..."
    me "Yeah, yeah, I wish you also won't get sick."
    "Miku sank down beside me easily, stretching with delight."
    show mi smile pioneer close at cright with dissolve
    "A healthy blush on her cheeks said that she slept well."
    dreamgirl "Envy with dignity! Don't make a maniac face!"
    mi "It's good that Uncle Borya-sensei has already left. I can imagine how angry he would be if he knew that I missed my exercises!"
    th "You have no idea, darling."
    show mi upset pioneer close with dspr
    mi "By the way, was Lena at the exercises?"
    show mi shocked pioneer close with dspr
    mi "I just woke up and she wasn't there, although she usually wakes me up, I get up so hard in the morning, you should know!"
    "I shrugged."
    me "No, I haven't seen Lena. Maybe she's ill?"
    th "Oh, I wish Miku would have been more offended by me after yesterday."
    th "She doesn't have anything in her head, does she?"
    show mi upset pioneer close with dspr
    mi "Well, no, if she got sick - I would notice, she would cough for sure, and even though I sleep soundly, but sensitively."
    me "Miku, there are many different diseases."
    me "Especially for girls."
    "I said with emphasis on the last word."
    show mi shy pioneer close with dspr
    "The Japanese girl flared up like a poppy flower."
    mi "How can you talk about such things?"
    me "What's natural ain't supernatural..."
    show mi shocked pioneer with dissolve
    "Miku jumped up from the bench in horror."
    mi "I'm so hungry, I'm dying, I'll run to take a queue in the dining room!"
    hide mi with moveoutright
    "The girl was blown away by the wind, and I leaned back on the bench, laughing through the pain in my ribs."
    th "Such an interesting way to walk away from a conversation - I should make a note so I don't forget..."
    play sound sfx_7dl["eat_horn"] fadein 2
    "Finally, the horn sounded and I scraped myself off the bench with difficulty."
    scene bg ext_square_day
    show dv normal pioneer2
    with dissolve
    "A motley crowd was already hurrying through the square, among which I instantly found Alisa."
    me "I thought you were asleep."
    show dv laugh pioneer2 with dspr
    dv "And skipped breakfast? Hell no!"
    dv "I only have a siesta after a heavy meal."
    me "If you want a solid meal, and not two dried-up slices of bread, then push it. Or do your legs not walk after exercising?"
    show dv grin pioneer2 with dspr
    dv "Oh they walk alright!"
    scene bg ext_square_day at running
    with flash
    "We took off and ran forward, overtaking the bewildered pioneers."
    stop music fadeout 1.5
    stop ambience fadeout 1.5
    return

label alt_day6_dv_dj_breakfast:
    scene bg ext_dining_hall_near_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    play music music_list["everyday_theme"] fadein 3
    "Despite the fact that we overtook about half of the camp, the line for the distribution seemed endless and stretched even from the street."
    show dv smile pioneer2 at cright with dissolve
    "Alisa leaned on the porch railing, looking at the disgruntled humming pioneers, forced to hold the heavy door."
    dv "Well, last push and we're free as the wind."
    me "What are you on about?"
    dv "Today there will be only morning broadcast. What did you listen to the Hat with?"
    th "With the same thing I usually sit on."
    dreamgirl "It's noticeable."
    show dv normal pioneer2 with dspr
    dv "After a quiet hour, a concert, and immediately after dinner, dancing."
    "I gritted my teeth in annoyance."
    th "In the morning, Olga, at the behest of her left heel, turned our cozy radio room into a passage yard, at the concert Alisa will again be dragged onto the stage by the active Miku, and during the dances I will sit in the corner while the redhead plays records!"
    th "What is it like, on my last day at camp, I won't even be able to really enjoy Alisa's company?"
    show prologue_dream with dissolve
    th "Wouldn't it be nice if she told me:"
    show dv laugh pioneer2 with dspr
    dv "Yeah I don't care about any of them."
    dv "Let's hitchhike to town!"
    dv "Let's do the little things and ride the dog towards the sea."
    show dv grin pioneer2 with dspr
    dv "Or not, we'll travel with no tickets right away - it will be more fun that way. And in a week we'll be at the sea."
    show dv laugh pioneer2 with dspr
    dv "Let's eat sweet-sweet oranges and lie on hot pebbles."
    dv "Isn't it beautiful?"
    play sound sfx_punch_medium
    hide prologue_dream
    show dv normal pioneer2
    with flash
    dv "Hey! Are you even listening to me?"
    "If Alisa said something, it is clearly not what I so dreamed of hearing."
    "But admitting that I missed everything was tantamount to suicide."
    me "Yes. What?"
    show dv grin pioneer2 with dspr
    "The girl held out her hand to me."
    dv "So, bet?"
    menu:
        "Bet":
            $ lp_dv += 1
            $ karma -= 5
            $ alt_day6_dv_dj_bet = True
            "I shook her hand vigorously."
            me "I hope you're ready to accept defeat."
            th "Wish I knew what our conditions are..."
            show dv smile pioneer2 with dspr
            "Alisa stretched her lips into a smirk."
            dv "Ulyana, break it."
            show us grin sport at cleft with moveinleft
            "I was once again amazed at how the red-haired youngest managed to be there at the right and not so moments."
        "No dice":
            $ karma += 10
            me "Are we in kindergarten? All we do is bet!"
            show dv normal pioneer2 with dspr
            me "What's the next bet? That they'll have porridge for breakfast?"
            "Alisa rolled her eyes."
            dv "My obituary will list 'mortal boredom' as the cause of death."
    dv "Now it's our turn! Make way!"
    stop ambience fadeout 2
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 1
    "We squeezed into the canteen and each took a tray."
    "The desired porridge was already close."
    stop music fadeout 3
    stop ambience fadeout 2
    return

label alt_day6_dv_dj_broadcast:
    scene bg int_clubs_dj_7dl with dissolve
    play music music_list["my_daily_life"] fadein 2
    th "Eh, our miserable closet with two chairs and overweight equipment!"
    th "When did you manage to become so dear?"
    "I gazed lovingly at the modest furnishings of the radio room."
    "In less than three days, I got so used to the idea that this is my workplace that it was even a pity to tear it all away from my heart."
    th "This camp makes me sentimental."
    th "First I am touched by Alisa's champing in the dining room, then I yearn for some utility room..."
    th "What's next? Will I go to the factory to work for the glory of communism?"
    show dv normal pioneer2 with dissolve
    dv "Looks like the guests are not in a hurry to visit us."
    if alt_day6_dv_dj_bet:
        dv "Maybe we can arrange a contest? Shall we promise everyone who comes with a branded T-shirt with an autograph?"
    show dv dontlike pioneer2 with dspr
    stop music fadeout 5
    "I took the microphone from the table under the suspicious gaze of my partner."
    me "If the mountain doesn't go to Magomed..."
    show dv angry pioneer2 with dspr
    play music music_list["that_s_our_madhouse"] fadein 2
    dv "…then to hell with that mountain!"
    show dv angry pioneer2 close with dissolve
    dv "Put the mic down and nobody gets hurt!"
    "As if reading my intentions, Alisa loomed menacingly over me."
    play sound sfx_7dl["radiotune"]
    show dv dontlike pioneer2 close with dspr
    "I winked at her before flipping the switch."
    me "Good morning, Sovyonok!"
    me "Your favorite radio station is on the air and today we're saying hello! Yes, yes, you are too, so feel free to stop by for a light!"
    me "I, taking advantage of my official position, want to convey the very first greetings."
    show dv shy pioneer2 with dissolve
    "Alisa sank into her chair and put her head in her hands."
    "Her face blended with the tie tied around the girl's wrist."
    if lp_dv >= 19:
        me "I send my regards to Alisa Dvachevskaya, who has been with me since the launch of the radio station, and, I hope, will not leave even after our work in this camp comes to an end."
        show dv shocked pioneer2 with dspr
        me "Because I love her even though she's such a pain in the ass!"
        "Watching the redhead's face go from red to deathly pale was a treat!"
        dv "You... you..."
        me "Me!"
        show dv rage pioneer2 with dspr
        dv "Rocket head!"
        show dv rage pioneer2 at fleft with move
        show dv rage pioneer2 at fright with move
        show dv rage pioneer2 at center with move
        "I rolled with laughter as Alisa darted around the radio shack looking for a weapon heavy enough for my execution."
        dv "You wait, now the Hat will show you!"
        show dv rage pioneer2 with dissolve
        dv "Although I'll kill you first!"
        "She grabbed a tube from the closet and swung it."
        show dv angry pioneer2 with vpunch
        "I instantly dived under the table."
        me "Microphone, Dvachevskaya!"
        show dv surprise pioneer2 with dspr
        "The girl froze, looking warily at the microphone thrown on the table."
        show dv shocked pioneer2 with dspr
        me "It's off!"
        play sound "<to 0.5>" + sfx_armature_swish
        pause(0.2)
        play sound2 sfx_punch_washstand
        stop music fadeout 5
        show dv rage pioneer2 close with flash_red
        "Recklessly deciding that the danger had passed, I leaned out from under the table - and at the same second I hit the cumpol with a tube."
        dv "Your jokes are stupid!"
        show dv angry pioneer2 with dissolve
        play music music_list["what_do_you_think_of_me"] fadein 2
        me "Everything I said is absolutely true."
        "I grumbled offendedly, straightening up and dusting off my shorts."
        me "Have you never been declared in love?"
        show dv guilty pioneer2 with dspr
        "Alisa lowered her eyes and sank into her chair, throwing the ill-fated tube on the floor."
        dv "There were no such fearless ones."
        me "What about yourself?"
        show dv sad pioneer2 with dspr
        dv "What about me?"
        me "Am I your very, very first and very, very true love?"
        show dv shy pioneer2 with dspr
        pause(0.1)
        show dv grin pioneer2 with dspr
        "Once again the girl, who had begun to blush, snorted."
        dv "Oh, no!"
        dv "I never got to confess. I thought it was silly."
        me "And now you don't?"
        show dv smile pioneer2 with dspr
        dv "I do."
        dv "But I had to come to terms with the fact that all the kissing and cooing in the world is a variant of the norm, not a sign of mental retardation."
        me "Oh, so that's how it is!"
        show dv laugh pioneer2 close with dissolve
        "I pressed a laughing Alisa against me, burying my fingers in her hair."
        me "Pain in the ass!"
        dv "Dumbass!"
        "I lifted her face and looked into her eyes sternly."
        me "I bet I know more name-calls?"
        show dv smile pioneer2 close with dspr
        stop music fadeout 4
        dv "No I do!"
        play sound sfx_knock_door7_polite
        show dv surprise pioneer2 close with dspr
        "There was a delicate knock at the door, causing us to bounce off each other."
        show dv normal pioneer2 at right with dissolve
        play music music_list["my_daily_life"] fadein 3
    else:
        me "I want to send my regards to my partner Alisa, without whom this radio station would never have happened!"
        me "Thank you for all your hard work, Sovyonok will not forget you."
        show dv smile pioneer2 close with dissolve
        "With a grin, Alisa took the microphone from me."
        dv "And I want to say hello to my partner Semyon."
        show dv laugh pioneer2 close with dspr
        stop music fadeout 5
        dv "He is, of course, a terrible retard and sometimes a terrible nerd, but sometimes even he can be fun."
        show dv smile pioneer2 with dspr
        "I could almost physically feel the smile sliding off my face."
        play music music_7dl["out_of_painkillers"] fadein 3
        th "Is that all I deserve?"
        th "Sometimes it can be fun?"
        "Of course, you couldn't expect fervent declarations of love and fervent thanks from Alisa, but what she said..."
        "It was hurtful."
        th "Am I some kind of clown to her?"
        th "Couldn't you at least try not to make a fool of me in front of the whole camp?"
        me "Thank you. It's nice to hear that you think so well of me."
        show dv surprise pioneer2 with dspr
        dv "Are you offended?"
        th "My lady, you are the most perceptive!"
        me "No. Just drawing some conclusions."
        dv "What did I say wrong?"
        "She didn't seem to genuinely understand exactly what it was that offended me."
        show dv angry pioneer2 with dspr
        dv "I've told you a thousand times that you're a retard and a bore."
        dv "And I don't see anything wrong with that!"
        dv "Annoying, yes. Sometimes it's even annoying."
        dv "But I still accept you for who you are!"
        show dv surprise pioneer2 with dspr
        me "But can you turn on the microphone and say it to the whole camp right now?"
        show dv guilty pioneer2 with dspr
        "Alisa fluttered her eyes helplessly."
        me "That's right, you can't."
        me "But what you can do is throw a load of shit at me."
        show dv sad pioneer2 with dspr
        me "Make everyone laugh!"
        me "If you're having fun, why not make those around you laugh?"
        show dv guilty pioneer2 with dspr
        dv "I'm sorry."
        "The girl said it so quietly that I couldn't believe my ears."
        show dv sad pioneer2 with dspr
        dv "I didn't mean to offend you. It's just..."
        "She bit her lip, staring down at the floor."
        dv "Sometimes it's hard for me to know which jokes are for my own and which are for other people's."
        dv "I grew up in an environment where everybody laughed at everybody, you know?"
        show dv guilty pioneer2 with dspr
        dv "There you're either laughing with everyone else, or you're going to be recognized as a wimp. We never had anything about you that wasn't known, you know?"
        me "Haven't you learned anything in the last nine years?"
        "Perhaps I should have kept quiet, but my anger was stronger than myself."
        show dv angry pioneer2 with dspr
        dv "And what could I learn? No one can shut me up."
        dv "Only then I find out over the grapevine that someone holds a mortal grudge against me. You're the only one who's spoke up on the spot."
        me "Tell me you won't do it again, and I'll forgive you."
        show dv sad pioneer2 with dspr
        dv "I'll try, but I can't promise anything.."
        show dv surprise pioneer2 with vpunch
        stop music fadeout 2
        me "Then go to the corner!"
        me "For five minutes, as a prophylactic measure."
        play music music_7dl["everyday"] fadein 2
        show dv angry pioneer2 with dspr
        dv "No, you really are an ass!"
        show dv surprise pioneer2 at veryclose with dissolve
        "Alisa swung for a punch, but I habitually intercepted her arm, drawing the girl to me."
        show dv shy pioneer2 with dspr
        th "That's okay, we're going to reeducate you!"
        play sound sfx_knock_door7_polite
        hide dv
        show dv surprise pioneer2 at right
        with dissolve
        "There was a knock at the door, making us recoil from each other."
    play sound sfx_close_door_clubs_nextroom
    show dv normal pioneer2
    show el sad pioneer at left
    with dissolve
    el "I, uh, came here…"
    show el smile pioneer with dspr
    extend " to send my regards, yeah!"
    "The guy was very nervous, and this time clearly not because of Alisa's presence."
    "I kindly moved my chair, making way for the microphone."
    show el normal pioneer at left
    show dv normal pioneer2 at right
    with dissolve
    "Syroezhkin took the microphone, took a deep breath, closed his eyes..."
    show el upset pioneer
    show dv dontlike pioneer2
    with dspr
    el "I want to send my regards..."
    me "Click the toggle switch."
    show el surprise pioneer with dspr
    el "Huh?"
    show dv angry pioneer2 with dspr
    dv "And don't yell like that, or the whole camp will hear you even without a microphone!"
    show el shy2 pioneer with dspr
    "Blushing thickly, Electronik coughed and turned on the microphone, then looked at me questioningly."
    "I gave him a thumbs up."
    show el shy2 pioneer
    with dspr
    el "I want to say hello to Zhenya Zhukova from the first squad."
    show el shy pioneer
    show dv surprise pioneer2
    with dspr
    el "And to say that she is the most beautiful girl of the camp."
    show el shy2 pioneer with dspr
    el "And the most interesting. And the most..."
    show dv grin pioneer2 with dspr
    "He squinted, his lips curled, and was clearly agonizing over the right words."
    "Alisa looked at him with a sneer, but remained silent."
    "And I didn't understand what was going on here at all!"
    if lp_dv < 19:
        dreamgirl "And after that you get offended by “retard”?"
    show el shy pioneer with dspr
    el "Anyway, Zhenya, I'm asking you to dance tonight!"
    show el upset pioneer
    show dv normal pioneer2
    with dspr
    "The switched off microphone rattled down on the table, and Electronik leaned against the back of my chair, catching his breath."
    show el sad pioneer with dspr
    el "Was it bad?"
    me "Well, I wouldn't say it was very bad, more like..."
    show dv dontlike pioneer2
    show el surprise pioneer
    with dspr
    dv "Disgusting!"
    "Alisa rolled her eyes."
    dv "It's as if you told her to come to a showdown, not called her to squeeze to music in the square."
    th "Since when did she become aware of such things?"
    show el sad pioneer with dspr
    "Syroezhkin's drooped."
    el "You mean she won't go?"
    show dv normal pioneer2 with dspr
    dv "Why is that? She will."
    show el upset pioneer with dspr
    dv "Just don't be surprised if she starts punching your face instead of dancing!"
    me "Don't listen to her, she always has such stupid jokes."
    show dv angry pioneer2 with dspr
    dv "Hey!"
    show el sad pioneer with dspr
    me "You're good, Serega. I think she won't say no."
    show el smile2 pioneer with dspr
    "With an awkward smile, the guy hurriedly retreated."
    play sound sfx_close_door_clubs_nextroom
    hide el
    show dv dontlike pioneer2
    with dissolve
    "Alisa turned to me."
    dv "What a fool you are! Zhenka hates him!"
    me "What makes you think that?"
    show dv angry pioneer2 with dspr
    dv "Do you even look beyond your nose?"
    dv "She wouldn't come to any dances, she'd sit as far away from him as possible in the canteen, she'd run from one log to another at the campfire, just so that this clown wouldn't be around."
    dv "And now imagine how she felt now, when he embarrassed her in the whole camp?"
    th "Yeeah, this is a situation alright. Is it just me, or have I been moved off the pedestal of 'camp's biggest retard'?"
    if alt_day6_dv_dj_bet:
        show dv smile pioneer2 with dspr
        "But suddenly the redhead smiled predatorily."
        dv "So, ready to admit defeat?"
        me "Excuse me?"
        show dv angry pioneer2 with dspr
        "Alisa threatened to get very, very angry."
        dv "You made a bet, you jerk! I told you he'd be the first to come running!"
        th "Oh, so that's what we were arguing about!"
        me "What's my punishment?"
        show dv smile pioneer2 with dspr
        dv "You'll know later!"
    show dv normal pioneer2 with dspr
    play sound sfx_close_door_clubs_nextroom
    "The door swung open."
    show dn normal pioneer at left with dissolve
    "This time our visitor was Dan'ka."
    show dn unsured pioneer with dspr
    dn "I wanted to send my regards."
    show dn normal pioneer with dspr
    "I held out the microphone to him, glancing expressively at Alisa."
    show dv smile pioneer2 with dspr
    "She smirked, but didn't say anything."
    dn "Ulya, hello again."
    dn "I want you to know that even if it doesn't work out, we didn't come all this way for nothing."
    show dv surprise pioneer with dspr
    dn "You can always count on me."
    "He flicked the toggle switch and gave me the microphone back."
    dn "I'm done."
    hide dn with dissolve
    play sound sfx_close_door_clubs_nextroom
    "And Dan'ka walked away, ignoring my and Alisa's bewilderment."
    me "And what does all this mean?"
    show dv normal pioneer2 with dspr
    "The girl shrugged her shoulders indifferently."
    dv "What do I know? They have their own secrets, which they don't think it's proper to reveal to an outsider."
    play sound sfx_knock_door7_polite
    "There was another knock at the door."
    th "No privacy today..."
    "There were many, many people who wished to speak live."
    "Half an hour later, there was a line outside the door."
    hide dv with fade
    voice "Sending my regards to Polina from the fourth squad..."
    with fade
    voice "…so you never get sick!"
    with fade
    voice "…become the greatest footballer in the world!"
    with fade
    voice "…you are very beautiful and kind!"
    with fade
    voice "…I hope we don't lose each other after camp!"
    stop music fadeout 4
    $ alt_pause(1)
    show dv normal pioneer2 with fade3
    play music music_list["your_bright_side"] fadein 3
    "It was nearing dinnertime, and the cheers slowly dried up."
    "Alisa twirled the microphone thoughtfully in her hands."
    dv "I didn't think there'd be so many people willing to say something nice."
    dv "It's kind of... hypocritical or something."
    me "What's hypocritical about it?"
    dv "If you have something important to say, say it in person. Why trumpet it to the whole camp?"
    me "To show you're not the least bit ashamed of your feelings."
    me "I can tell you anything in person, but what good would it do to embarrass you and hide you from my friends?"
    show dv sad pioneer2 with dspr
    "Alisa twitched, as if my words had slithered to the stomach."
    dv "{i}Just don't tell anyone we're friends.{/i}"
    "Reluctantly, she repeated someone else's half-forgotten intonation."
    dv "{i}My mother would forbid me to go out if she knew we were talking.{/i}"
    show dv sad_smile pioneer2 with dspr
    "The girl's lips curled in a sneer."
    dv "If you have to choose between two kinds of hypocrisy, I like the first."
    show dv normal pioneer2 with dspr
    "And without saying a word, she yanked the player out of the amplifier."
    me "But how..."
    show dv smile pioneer2 with dspr
    dv "It's five minutes till dinner, and we still have to wind up the wires. I don't want to ruin a whole quiet hour by cleaning up!"
    "There was a tense silence."
    hide dv with dissolve
    "I folded the cables quickly into the box, glancing occasionally at Alisa."
    th "Is she so gnawed by the past that any occasional memory furrows the wounds that never healed?"
    $ volume (0.2,'sound')
    th "And I still don't know how I should react to it properly!"
    play sound sfx_7dl["eat_horn"] fadein 1
    "Before the muffled horn sounded from the street, Alisa never uttered a word."
    me "Congratulations on your release."
    stop sound fadeout 2
    show dv normal pioneer2 with dissolve
    dv "You too, partner."
    "She gave the radio room a long look."
    me "Will you miss it?"
    show dv smile pioneer2 with dspr
    dv "Nope!"
    dv "I'll take a couple notes, but in general…"
    show dv laugh pioneer2 with dspr
    dv "Out of sight, out of mind!"
    "She laughed, pushing up her chair."
    show dv smile pioneer2 with dspr
    dv "Let's go eat - I bet we're in for a royal lunch today!"
    $ volume (1.0,'sound')
    stop music fadeout 3
    return

label alt_day6_dv_dj_lunch:
    scene bg ext_dining_hall_near_day with dissolve
    play music music_list["smooth_machine"] fadein 2
    "Alisa wasn't lying - it was clear even on the porch that the cooks had decided to surprise the pioneers, who were hungry for junk food, one last time."
    me "Mmm... Solyanka?"
    show dv smile pioneer2 with dspr
    "My girlfriend was almost licking her eyes."
    dv "What's it worth to them to feed us human food every day? I already have a gag reflex from the sight of pearl barley in my plate!"
    scene bg int_dining_hall_people_day
    with dissolve
    play ambience ambience_dining_hall_full fadein 3
    show dv normal pioneer2 at right with dissolve
    "After getting a plate of pilaf and a glass of compote in addition to the hodgepodge, we went in search of a table."
    show mi upset pioneer far at cleft with dspr
    mi "Semyon, Alisa!"
    hide mi
    show mi upset pioneer at cleft with dissolve
    "Miku was sitting alone, and she looked extremely disturbed."
    th "Too impressed with traditional Russian cuisine?"
    stop music fadeout 3
    th "Well, it's nothing, it's not some surströmming. That's something even I wouldn't take in my mouth, and I'm not a fussy guy!"
    play music music_list["you_lost_me"] fadein 2
    mi "Lena isn't here!"
    show dv sad pioneer2 at right with dissolve
    "Alisa frowned."
    dv "What do you mean she isn't here? She couldn't have been picked up the day before the end of her shift!"
    show mi dontlike pioneer at cleft with dissolve
    mi "They certainly didn't take her away, all her things are there, her clothes, her albums, her paints, everything!"
    mi "I thought she might really be sick, I went to the nurse's office, but she wasn't there either, only Violetta Cernovna was filling out some journals."
    $ alt_pause(0.2)
    show dv angry pioneer2 at right with dissolve
    "Alisa's spoon hung in the air."
    dv "As for the shirts not tied by regulation, she is ahead of the locomotive, but as a pioneer girl is missing, she immediately shuts up!" with vpunch
    $ alt_pause(0.2)
    show dv rage pioneer2 at right with dissolve
    "The girl hissed. Her eyes became very, very unkind in an instant."
    me "After lunch, I suggest we go on a search."
    if alt_day5_dv_dj_map == "un":
        "I remember Lena strictly forbidding me to go near her."
        "But it's not about stupid bans anymore, a person's gone!"
    me "Any ideas where she might be?"
    show mi sad pioneer at cleft with dissolve
    mi "I don't know, probably somewhere off the grounds. I went around the camp today, checking the speaker lists, I would have noticed her if she was here."
    show dv think pioneer2 at right with dissolve
    dv "On the little rock. Of course, she used to go there often!"
    show dv dontlike pioneer2 at right with dissolve
    dv "I hope she was smart enough to bring provisions with her! Her father brought her so much the day before yesterday, she could eat to her heart's content for the rest of her shift."
    me "How do you know?"
    dv "We went out to see him together.{w} Lenka dragged me, she thought I'd get something from my parents through it."
    show dv angry pioneer2 at right with vpunch
    dv "Didn't get shit."
    $ alt_pause(0.2)
    show mi upset pioneer at cleft with dissolve
    $ alt_pause(0.1)
    show mi sad pioneer at cleft with dissolve
    "Miku looked anxiously at me and Alisa."
    show mi upset pioneer at cleft with dissolve
    mi "I want to go with you too, but... If I run away from the rehearsal, the concert won't happen at all!"
    hide dv
    hide mi
    with dissolve
    stop music fadeout 1
    us "No need for running."
    show us smile sport with dspr
    play music music_list["eat_some_trouble"] fadein 2
    "Ulyana appeared out of nowhere and made us all jump."
    us "Lena escapes on the last day every year, and no one has ever been able to find her."
    "In a conspiratorial tone, the girl whispered."
    show us grin sport with dissolve
    us "You'd only be wasting your time. And Olga Dmitrievna already knows, she personally let her go."
    show dv angry pioneer2 at right
    show mi surprise pioneer at left
    with dissolve
    "Alisa flashed."
    dv "And you kept quiet?!"
    show us upset sport with dissolve
    "Ulyana just threw up her hands."
    us "You didn't ask."
    hide us with moveoutleft
    stop music fadeout 3
    "And the little one galloped off on her insanely important errands, losing all interest in us. The girls and I looked at each other."
    play music music_list["goodbye_home_shores"] fadein 5
    show mi serious pioneer at left with dissolve
    mi "That's kind of weird, don't you think? Okay, they let her go, but why is she running away in the first place?"
    show dv dontlike pioneer2 at right with dissolve
    dv "Who can tell!"
    "Alisa sipped her kompot with irritation."
    dv "Lena hasn't let anyone in on her secrets for years. I don't care, though."
    th "So much that you almost went off looking for her, not giving a damn about anything else!"
    show dv normal pioneer2 at right with dissolve
    "I grinned bitterly as I watched the tension slowly let go of Alisa."
    dreamgirl "These girls are so mysterious..."
    dreamgirl "I didn't even look at my friend for the whole shift, and now I'm all worried!"
    th "An old friend is better than two new ones."
    dreamgirl "Better than a new boyfriend, anyway!"
    "My inner voice chuckled, voicing something I didn't even want to say in my mind."
    th "Even if she and Lena had lost each other long ago, Alisa would run to the ends of the earth for her, putting me out of her mind."
    if lp_dv > 19:
        th "And me... All I have to do is run after you, you redheaded bastard."
    else:
        th "And I'm as screwed as ever. So mundane that I almost effortlessly swallow it time after time."
    show mi smile pioneer at left with dissolve
    mi "Everything tasted so good today that I'd have another lunch like that, except I'm afraid I'll burst like a balloon!"
    show dv laugh pioneer2 at right with dissolve
    dv "You want too much! There are plenty of people here who want a second meal. And they, unlike some, aren't afraid to burst."
    "Alisa nodded at the crowd at the food counter, which was almost as long as it had been at the beginning of lunch."
    th "Goodbye, my second plate of hodgepodge..."
    dreamgirl "Stop thinking about food, you glutton!"
    dreamgirl "You've got something important to do, like getting some redhead into a more private corner..."
    th "It's about time you reminded me."
    th "Good thing Lena escapes every year!"
    show mi normal pioneer at left with dissolve
    mi "It's time to get everyone together. Alisa, don't forget the rehearsal!"
    hide mi with moveoutright
    show dv dontlike pioneer2 with dissolve
    "Picking up her tray, Miku left us. The redhead saw her off with a wry face."
    me "Let's go, too."
    dv "Are we going somewhere in a hurry?"
    me "Of course we are!"
    "I whispered, making big frightened eyes."
    me "To hide from Miku and her rehearsals!"
    show dv smile pioneer2 with dissolve
    "Alisa hummed contentedly."
    dv "Once a year, even you get a good idea in your head!"
    stop music fadeout 3
    stop ambience fadeout 2
    return

label alt_day6_dv_dj_siesta:
    scene bg ext_dining_hall_near_day with dissolve
    play ambience ambience_camp_center_day fadein 1
    "The children scurried away from the canteen - some to rehearse their performances for the concert, and some to commit the mischief that they didn't have time for during the once long, and now so short and fleeting, shift."
    show dv smile pioneer2 with dspr
    dv "So, where are we going?"
    play music music_7dl["let_me_down"] fadein 3
    me "I've got an idea…"
    scene bg ext_dining_hall_away_day with fade
    show dv surprise pioneer2 with dissolve
    "Grabbing the redhead by the arm and not listening to her indignant cries, I dragged the girl toward the square."
    show dv dontlike pioneer2 with dissolve
    dv "I don't like it when people don't ask my opinion!"
    me "Come on! You certainly won't mind."
    show bg ext_square_day with fade
    "The flock of pioneers in the second squad looked at us in bewilderment, but I didn't stop, and I didn't let go of Alisa's hand. A strange euphoria came over me from this little victory, to the point of trembling in my fingertips."
    th "Maybe I should have done that right away."
    th "Walked up, took her hand, didn't care what she thought about it, and it would have been easier for both of us."
    dreamgirl "Oh yes, sexual abuse is so easy!"
    th "There's no abuse. She just doesn't understand what she wants."
    dreamgirl "Good thing your head works for two. There is no 'I,' there is only 'we.'"
    "The inner naughty man changed his views on sexual relations so dramatically that I was taken aback. The former attitude threatened to fade at any moment."
    dreamgirl "Honey, our secretary has a baby from us!"
    th "Ugh!"
    th "You're just trying to make everything look bad!"
    scene ext_house_of_dv_day with guess_on
    show dv surprise pioneer2 with dissolve
    "I pulled up in front of Alisa's cabin. The girl looked at me perplexed."
    dv "And why did you bring me here?"
    me "Turn on the logic, Dvachevskaya. If you don't come to rehearsal, what will Miku think?"
    show dv think pioneer2 with dissolve
    dv "That I'm running away and slacking off somewhere where she won't find me..."
    "I think she's starting to get it."
    me "Exactly! If you want to hide something, put it in the most obvious place."
    hide dv with dissolve
    scene ext_house_of_dv_day:
        linear 1 zoom 1.5 align(0.4, 0.45)
    play sound sfx_open_door_1
    "I jumped up on the porch and opened the door with an inviting gesture."
    me "So welcome to our political asylum for the next two hours!"
    scene int_house_of_dv_day with fade
    play sound sfx_close_door_1
    $ alt_pause(0.4)
    play ambience ambience_int_cabin_day fadein 3
    show dv normal pioneer2 with dissolve
    stop music fadeout 5
    "As soon as the door slammed shut behind Alisa, my arrogance was suddenly diminished. It's one thing to get a girl into a secluded spot, but to logically pursue this endeavor..."
    dv "You sit down, don't just stand there."
    show dv sad pioneer2 with dissolve
    "Alisa nodded at her bed."
    play sound sfx_bed_squeak2
    "I obediently landed on the untucked bunk, keeping my gaze on the redhead."
    show dv shy pioneer2 close at ba_sit_down_unfzdv
    play music music_7dl["vale"] fadein 3
    "And it worked: now she was embarrassed."
    dv "Cards, maybe...?"
    me "What kind of cards? Is it your childhood in one place that's bothering you?"
    show dv shy pioneer2 close:
        linear 1.25 zoom 1.2
    "I pulled her to me so sharply that she exhaled in amazement."
    me "We're adults, after all."
    "Alisa swallowed noisily."
    show dv shy2 pioneer2 with dissolve
    dv "Yeah, you know, somehow..."
    "Her cheeks were drenched in paint, and I sincerely hoped I looked at least a little more confident."
    dv "That's weird."
    show dv closed_eyes pioneer2 with dissolve
    window hide
    with flash_pink
    window auto
    "With every second of my kisses, she thawed little by little, and her body, stiff with fear, became malleable, like a wax candle warmed by the warmth of my hands."
    th "Closer... even closer..."
    th "Just a millimeter!"
    "Sprawled out on the pillow, I squeezed her ribs, making Alisa arch back and forth, snuggling in and out of me again."
    th "You know I love emotional swings. And only you know how to rock me this hard."
    "Her fingers timidly crept up to my hair - only to tear with all their might, forcing me to bite her lower lip to the blood, suppressing a hiss."
    th "I may not be seventeen, but when you're around, I can easily dismiss the last ten years as something unnecessary."
    th "Wrong."
    play sound sfx_punch_medium
    show dv angry pioneer2 with vpunch
    "But as soon as I got close to the knot on her shirt, I immediately got a slap on my raking hands."
    dv "Don't do that!"
    show dv normal pioneer2 close with dissolve
    "Alisa straightened up, brushing her wet bangs away from her forehead. I grinned, helping her with my left hand. I ran my fingers across her heated cheek."
    "Unobtrusively, I lowered my palm to her thigh."
    me "Chickening out?"
    show dv sad pioneer2 close with dissolve
    dv "Or maybe I did chicken out!"
    "She turned away from the window, frowning her eyebrows. Inside her exuberant red head, two conflicting desires were clearly struggling."
    "I put my right hand on her other thigh and squeezed lightly."
    me "Who's there to be afraid of? Everyone's own!"
    show dv sad_smile pioneer2 close with dissolve
    "Alisa snorted, but she didn't drop my palms."
    dv "I imagined that my daughter would ask me, years from now, what my first time was like."
    dv "And what will I tell her? That there was this one jerk at my camp..."
    me "Yeah, her father wasn't much of a prince back then."
    me "But that's for now! Just give me time, and I'll put all the other candidates behind me."
    show dv grin pioneer2 close with dissolve
    "Alisa leaned over my face, smiling with just her eyes."
    dv "You're going to screw yourself over with your jokes..."
    dv "Do you know how strict my father is? Tomorrow right after the bus we'll go to the registry office!"
    me "What about the dress? I want my bride to wear the most beautiful dress!"
    show dv smile pioneer2 close with dissolve
    dv "You want too much, you won't get enough!"
    me "Sounds like a challenge!"
    stop music fadeout 1
    play sound sfx_open_door_kick fadein 0
    with vpunch
    show dv shocked pioneer2 close with dspr
    "I clutched Alisa to me again, and nearly jumped up with my burden when the door rattled open."
    play music music_list["i_want_to_play"] fadein 3
    show us normal sport at fright with dissolve
    us "Ew, what are you doing here, committing adultery?"
    me "Just cuddling, you ignorant child. And I don't even want to know where you heard that word..."
    th "And certainly none of us are married!"
    hide dv
    show dv shy pioneer2 at cleft with dissolve
    "The moment was ruined, finally and irrevocably: Alisa flared up and hurriedly got off me, fixing her skirt with."
    me "What do you want?"
    show us dontlike sport at fright with dissolve
    us "Well, first of all, I live here. There was no 'do not disturb' sign on the door!"
    "Ulyana glared at me angrily, not even attempting to tease the already embarrassed Alisa."
    show us normal sport at fright with dissolve
    us "And secondly, Olga Dmitrievna was looking for you. You in particular."
    "She didn't point her finger in my direction very politely."
    th "I s-e-e."
    th "This camp has extremely inventive methods of avoiding amorality."
    th "We'll load up the pioneers so they won't have the energy to do anything stupid!"
    show dv normal pioneer2 at cleft with dissolve
    "I looked longingly at Alisa buttoning her sandals."
    th "Well, nothing, if we manage to keep our relationship in its current status after the disco, we'll still make it!"
    dreamgirl "Will you send the little one under the tree to sleep? Or to her curly fellow?"
    th "We'll think of something. The bosses, of course, are clever, but crafty pioneer thinks three moves ahead!"
    show dv smile pioneer2 at cleft with dissolve
    dv "Shall we go?"
    "Alisa seemed, for the first time in her shift, to be excited about a sudden party assignment. I sighed."
    if lp_dv < 19:
        th "Doesn't trust me that much? Well, well."
        th "Could have just said, 'Get lost, buddy,' instead of playing games!"
    else:
        th "It seems that the battles in my head ended in a draw between the rational and the emotional. That's okay, I'll prove that the latter is worth listening to!"
    me "Let's go. What if suddenly the whole camp froze, waiting for the two most important workers and toilers!"
    stop music fadeout 3
    stop ambience fadeout 3

    scene bg ext_square_day with fade3
    play music music_list["everyday_theme"] fadein 3
    show mt normal pioneer far with dissolve
    show dv normal pioneer at fleft with dissolve
    show us dontlike sport at left with dissolve
    show el normal pioneer at fright with dissolve
    show sl normal pioneer at right with dissolve
    "Olga was standing in the middle of the square, waving her panama hat. Nearly all of our small troop crowded around her."
    mt "Here they are at last!"
    show mt angry pioneer far with dissolve
    mt "Alisa - march to rehearsal, Miku can't find you!"
    mt "Sergei and Sasha, check the equipment on stage. Slavya - you're still in charge of cleaning the warehouse."
    mt "Ulyana, get the garland from the clubs. And don't make that face!"
    show us normal sport with dissolve
    mt "If only someone would help Miku take the costumes to the stage and help me clear the stands..."
    show mt normal pioneer far with dissolve
    "The squad leader's gaze stopped on me."
    mt "Semyon, we're woefully short of hands, so you decide who you're going to help."
    th "Wow, what an indulgence!"
    "I mentally estimated which of the upcoming party tasks looked the least dusty."
    if (alt_day6_dv_dj_bet):
        $ alt_pause(0.5)
        "Someone to the left coughed softly."
    menu:
        "Help Ulyana with the garlands" if loki:
            $ karma += 10
            $ alt_day6_dv_dj_quest = 0
            th "On the one hand, there is not the slightest desire to crawl through trees with garland in my teeth, but on the other hand, to send Ulyana to this task is pure mockery!"
            me "I think I'll help Ulyana with the garlands. I can reach higher than that!"
            play sound sfx_wind_gust
            hide sl
            hide el
            hide dv
            with dissolve
            $ alt_pause(1)
            show us angry sport at left with dspr
            us "What kind of innuendo is that?"
            me "Not innuendos, but a statement of fact, petite: six-foot-five is clearly more than six feet tall."
            show us dontlike sport at left with dspr
            us "I'm 150 centimeters high!"
            show mt smile pioneer far with dissolve
            "Olga giggled quietly as she watched our altercation."
            stop music fadeout 2
            mt "Great. Then bring a ladder, too!"
            play music music_list["eat_some_trouble"] fadein 2
            th "Okay, stop!"
            th "What do you mean 'then'?"
            play sound sfx_wind_gust fadein 0
            hide mt
            hide sl
            hide el
            hide dv
            with dissolve
            $ alt_pause(1)
            "Olga went off on her own business (probably lying in a chaise lounge), as did everyone else (probably holed up in cool corners). The little one and I were left alone in the square, drilling each other with unfriendly glances."
            "Ulyana looked at me like I was an idiot."
            show us dontlike sport at center with dissolve
            us "Before you get in, I should have just brought the garland here for the cyberneticists to hang it up later!"
            "She hissed."
            us "But no, someone who's the smartest has to put their five cents in!"
            me "Don't be a whiner! Don't you want to work for your country?"
            "I've got a judgmental tongue twitch."
            me "I'll write a denunciation about you, and then you won't be accepted into the Komsomol!"
            show bg ext_houses_day with dissolve2
            "We reluctantly moved toward the clubs."
            show us laugh sport with dissolve
            us "And I'll write one about you, that you are a pervert!"
            me "And I..."
            if alt_day5_dv_dj_map == "us":
                me "And I'll write on you for being a kleptomaniac!"
                show us surp1 sport with dissolve
                us "Klepto-who?"
                me "It's someone who really likes to take other people's underwear without asking."
                show us shy sport with dissolve
                "The girl turned away embarrassed."
                us "There was no such thing! You made it all up, or you dreamed it!"
            else:
                me "I'll write that you eat too much!"
                show us smile sport with dissolve
                us "Is that a threat? I have a growing body!"
                me "Is that why you climb into the canteen at night?"
                "I sternly wagged my finger at the girl."
                me "That's burglary, you can't blame it on a growing body!"
                show us smile sport with dissolve
                us "You have no proof!"
            show us grin sport with dissolve
            us "In fact, I'm going to tell you that you're a slacker!"
            us "Turn on your electronic balalaika and go away for a walk."
            me "That's how you're gonna set Alisa up, you little twerp!"
            show us surp2 sport with dissolve
            us "How? She carries her post honestly, unlike some people."
            me "False denunciation is punished wtih a shooting squad!"
            show us laugh sport with dissolve
            us "And you'll be shot sooner anyway. I'm only fourteen, they'll understand and forgive me."
            us "You're the one with the big forehead - you won't be spared!"
            scene bg ext_clubs_day with dissolve2
            "At the clubs I stopped."
            show us normal sport with dissolve
            me "Come on, get that garland over here - I have no idea where it is anyway."
            us "Leave you here to run away? No way!"
            show us angry sport far at right with dissolve
            play sound sfx_open_door_clubs
            "Ulyana opened the door, looking at me sternly."
            us "Come in, come in."
            th "Yeah, sure!"
            th "I'm about to walk in with her into a lonely and empty club building, and then she'll write such a denunciation that it would be easier to hang myself on that garland on the spot!"
            dreamgirl "You're just a pessimist."
            dreamgirl "Turn it to your advantage, say she stole the government's bolts!"
            th "That's a thought..."
            stop ambience fadeout 3
            scene bg int_clubs_male_day with dissolve
            "The garland was found quickly - apparently, after last time, it wasn't put away far away."
            me "So, let's go get the ladder now?"
            show us upset sport with dissolve
            us "It's in the warehouse. It's such a long way..."
            me "Why are we so stupid?"
            "I slapped myself on the forehead."
            me "we're in a cybernetics club!"
            me "There's bound to be a teleporter around here somewhere. Why don't you look in those closets and I'll look under the table."
            show us dontlike sport with dissolve
            us "What a fool you are!"
            "Ulyana rolled her eyes."
            us "And what did Alisa find in you? Not only does she drag you around all day, but..."
            "She pretended to vomit."
            us "Kissing!"
            me "You just haven't tried it. You'll love it!"
            show us surp2 sport close with dissolve
            us "What are you…"
            show us fear sport close with dissolve
            play music music_7dl["genki"] fadein 3
            $ alt_pause (2)
            hide us with moveoutleft
            us "AAAAAAH!"
            "Ulyana jumped out of the clubs like she was scalded. I picked up the garland she'd thrown from the floor, wiping the tears from my eyes that had come out of laughter."
            dreamgirl "Congratulations, now her denunciation will be at least partly true."
            dreamgirl "Not so offensive now, is it?"
            $ alt_pause(1)
            stop ambience fadeout 3
            scene bg ext_square_day with dissolve
            play ambience ambience_camp_center_day fadein 1
            show us angry sport with dissolve
            us "Dumbass." with vpunch
            me "Pain in the ass."
            us "Cretin." with hpunch
            me "Leech."
            "We hung garland around the perimeter of the square in sweat. The only entertainment available was swearing."
            us "Spitfire!"
            me "There's no such word, kiddo."
            show us laugh sport with dissolve
            us "There is. You're just an uneducated... dumbass!"
            "I had nothing to object to."
            me "That was quick."
            show us dontlike sport with dissolve
            us "And you think that's fast? It's ten minutes till lunch!"
            us "Do you know how many useful things I could have done in that time?"
            me "I reckon there'd be no stone left unturned in the camp."
            show us grin sport with dissolve
            us "Is that what you think of me? That's okay, I'll remind you of that!"
            hide us with moveoutleft
            "With a sly squint, Ulyana raced toward her cabin. I sat down on the bench to wait for the other workers."
        "Clean up stands from newspapers" if dr:
            $ lp_dv -= 1
            $ alt_day6_dv_dj_quest = 1
            th "How many stands are there? Two or three, that's it."
            th "Certainly looks like an opportunity to stretch this event out over the entire quiet hour and enjoy a nice walk along the shady paths..."
            me "What's there to take off the booths?"
            show mt smile pioneer far with dissolve
            "Olga squinted happily, and I didn't like that one bit..."
            mt "Come, I'll tell you on the way."
            mt "Have you heard all your tasks? March!"
            play sound sfx_wind_gust fadein 0
            hide us
            hide sl
            hide el
            hide dv
            with dissolve
            $ alt_pause(1)
            hide mt
            show mt normal pioneer with dissolve
            "The square was empty in a second. I glanced at Alisa as she headed toward the music club."
            th "Will she make it to Miku's abode? Something tells me she won't."
            "With a quiet sigh, I turned to my newly minted partner."
            me "Well, let's get to work, shall we?"
            show mt smile pioneer with dissolve
            "Olga bobbed her fist."
            mt "You're such a nerd! Right away you ask about work!"
            "My mouth involuntarily dropped open."
            me "That's what you're..."
            mt "You'd expect it from your pioneer, yes. But would I want that?"
            show mt grin panama pioneer with dissolve
            "She looked at me expressively, slipping her panama over her head."
            mt "You have too much to do today to say goodbye to this place properly. So I want to show you the camp as you've never seen it before."
            mt "Look at it through my eyes."
            "The squuad leader moved forward, gesturing for me to follow."
            th "It's getting interesting..."
            th "Not only does she shirk her duties under the guise of a trivial task, but she convinces the pioneer to bum around!"
            th "Does she even get paid for her work?"
            stop music fadeout 6
            dreamgirl "Look at yourself!"
            dreamgirl "Aren't you the one living on the principle of “Do whatever, just to do nothing”?"
            th "In this, Olga and I are probably similar."
            play music music_7dl["your_life"] fadein 3
            me "You even were a pioneer here, weren't you?"
            show mt surprise panama pioneer with dissolve
            mt "And who ratted me out? You don't have to tell me, though - I can guess it myself."
            show mt normal panama pioneer with dissolve
            mt "I'll tell you even more - not only here, but also in the old camp. The tent camp."
            mt "The conditions there were, of course... Compared to this, this is a resort!"
            me "And isn't it strange... Well, you know - working here after coming here to rest and..."
            show mt grin panama pioneer with dissolve
            "I bit my tongue, but Olga only laughed."
            mt "If you want to, say so!"
            me "...and be outrageous."
            show mt normal panama pioneer with dissolve
            mt "You know, no, it's not strange at all. I'd even say very natural."
            mt "Who better than the ex-hooligans to understand the mischievous kids at camp? Who better than yesterday's bullies to discipline today's bullies?"
            scene bg ext_square2_day_7dl with dissolve2
            "We reached the first stand - I only noticed it out of the corner of my eye as I rushed to the canteen."
            me "Our daily routine at pioneer camp Sovyonok."
            "I read the garish headline on the wadpaper, floating and curled in the corners from yesterday's rain."
            show mt sad panama pioneer with dissolve
            "Olga sighed, looking at the ruined wall newspaper."
            mt "I don't feel sorry for the pictures; Boris will print new ones. He's stingy, but his memories of the camp are treasured. But Lena's drawings..."
            "I could hardly make out something on one of the drawings, something red and suspiciously familiar."
            scene bg ext_stand3_7dl with dissolve2
            th "Alisa!"
            "The picture, hopelessly blurred with water, showed a small, dark room, in which Ryzhevskaya was seated at a table in her own right."
            "There was a dark spot on her head - it must have been Lena's original idea that it was headphones. There was a microphone on the table in front of Alisa."
            "The note next to the picture was impossible to read, but the miraculously surviving picture of the twist-note next to the headline made it quite clear what the article was about."
            show mt sad_smile pioneer panama with dissolve
            mt "All our memories are like this newspaper. Today they are bright and colorful, but years later they will become an indecipherable mess of colored images."
            mt "You remember that it was great, but it's harder and harder to tell the difference."
            me "Is that why you're so drawn here?"
            show mt surprise panama pioneer with dissolve
            "The squad leader turned to me, raising her eyebrows in surprise."
            me "You don't want the picture to blur into one big slurry?"
            show mt sad panama pioneer with dissolve
            "With a sad grin, the squad leader began to pull out the stationery buttons. I rushed clumsily to hold up the paper."
            mt "That's what I thought, too. Now I realize it's self-delusion."
            show bg ext_square2_day_7dl with dissolve
            "She safely dumped the liberated paper on me."
            mt "It's quite the opposite: the longer I come here, the less I believe in things that once happened here to me and... other people."
            "We walked leisurely down the path."
            show mt smile panama pioneer with dissolve
            mt "Take Alisa for instance - as much as I look at her, I can't see the little girl who used to follow me and Mirya around the camp, begging me to invent some new game for them."
            me "You're a resident of another world to her now, aren't you?"
            mt "Yes. A world of boring adults who sneeze at every prank and have forgotten how to play."
            me "Have you forgotten how to play?"
            show mt grin panama pioneer with dissolve
            "Olga threw a sly look at me."
            mt "No. Learned to play by the new rules."
            mt "Let's say whoever is last to reach the stand shares their bun with the winner today!"
            show mt smile panama pioneer with dissolve
            hide mt with moveoutright
            show bg ext_square2_day_7dl at running
            "I, not expecting such a turn, gave the squad leader a good five meters head start before I rushed forward myself, waving the paper frantically."
            me "Unfair! Not fair!"
            show mt smile panama pioneer with moveinright
            mt "It's never fair in the adult world!"
            hide mt with moveoutleft
            "My long legs gave me a significant advantage in our impromptu race, and in the last meters I took the lead, slamming noisily into the booth at the gate."
            scene bg ext_stand3_7dl with dissolve
            "Olga slowed down next to me, catching her breath."
            show mt grin panama pioneer with dissolve
            mt "You're such a radish!"
            mt "You could have given way to a lady!"
            "I shrugged my shoulders, not hiding my own contentment."
            mt "Everything in the adult world is unfair."
            mt "So you won't be too disappointed if I eat my own bun?"
            me "No way! A deal is worth more than money."
            "After taking all the rain-beaten advertisements off the stand, Olga shoved them at me, then glanced at her wristwatch."
            show mt surprise panama pioneer with dissolve
            mt "Business! Boss' calls!"
            mt "Here's the deal: you take all the copies of the damaged papers in my nightstand and put them up on the stand. Pick the order you like."
            show mt normal panama pioneer close with dissolve
            stop music fadeout 3
            "She clapped me on the shoulder encouragingly."
            mt "And for a bun, come up to me at lunch."
            hide mt with dissolve
            play music music_list["smooth_machine"] fadein 3
            "Olga went to her superiors, while I went on my responsible assignment."
            "I undertook it with all responsibility and care."
            scene bg ext_dining_hall_near_day with joff_r
            "Slowly walked to the garbage cans by the canteen..."
            scene bg ext_house_of_mt_day with joff_r
            "Laid on a lounger, enjoying the evening sunshine..."
            $ alt_pause(0.2)
            stop ambience fadeout 2
            scene bg int_house_of_mt_day
            with dissolve
            play sound sfx_unlock_door_campus
            $ alt_pause(0.5)
            "Found the miserable papers in Olga's desk, while trying on her panama collection at the mirror..."
            scene bg ext_square2_day_7dl with dissolve2
            "Stuck announcements on flimsy buttons, flooding everything around with my massive supply of non-literary exclamations..."
            scene bg ext_square_day with dissolve2
            "And finally, with a sense of accomplishment, came to the square, sat on a bench - and waited for the afternoon meal."
        "Help with warehouse cleaning" if herc:
            $ lp_dv -=1
            $ alt_day6_dv_dj_quest = 2
            th "Slavya must have been loaded to the brim for yesterday's incident..."
            th "And I am, in a way, to blame for it. It's not good to leave it like that!"
            me "Let me help Slavya - in case something heavy has to be carried there, and she's a fragile girl, she'll be broken."
            show sl shy pioneer with dissolve
            "Slavya smiled timidly, lowering her eyes to the floor."
            show mt angry pioneer far with dissolve
            mt "Alright, go. Now all of you get to work, and don't let my eyes see you until noon!"
            sl "Let's go!"
            stop music fadeout 3
            "Quietly whispered the girl. The squad leader's pictorial anger seemed to massively scare her."
            hide us
            hide mt
            hide el
            hide dv
            hide sl
            with dissolve
            play music music_7dl["sad_piano"] fadein 3
            show bg ext_dining_hall_away_day with dissolve
            if (alt_day5_dv_dj_sl_jeer == 2):
                show sl shy pioneer with dissolve
                sl "Thank you for warning me yesterday."
                "Said Slavya suddenly, as we moved away from the square."
                show sl dontlike pioneer with dissolve
                sl "I can't imagine what Alisa would do with my secret!"
                me "Come on, I don't think she'd do anything outright bad."
            show sl normal pioneer with dissolve
            "I turned around to see if there were any extra ears around."
            me "And yet there's one question that haunts me..."
            show sl normal pioneer with dissolve
            sl "How did I manage to screw up so stupidly?"
            "The girl smiled, not the least bit angry."
            sl "Yesterday was such a hectic day because of the rain: in the morning I couldn't sneak out of the canteen to feed Pirate - I helped Anna tame her kids."
            sl "Immediately after dinner Olga Dmitrievna sent me to the fire glade, and I again failed to make it to the puppy. I kept thinking, how was he, poor thing!"
            sl "He's small, he can't stand it yet - I was afraid he'd attract attention to himself."
            sl "And then Lena and I were asked to clean up at the beach. Agreed with her and in the last fifteen minutes ran to Pirate in the warehouse."
            show sl sad pioneer with dissolve
            "Slavya sighed."
            sl "Only there's no clean uniform left in my size all day. I got spilled cocoa in the canteen, I got soiled in soot - in a word, it was a bad luck streak!"
            sl "And only near the canteen I noticed that Pirate smeared the last clean shirt. I wanted to run to wash, but it was too late - Olga Dmitrievna would have noticed and turned me back."
            show sl normal pioneer with dissolve
            sl "She looks strict, but in reality she won't leave any of her pioneers hungry!"
            sl "So I hoped it would be all right. But I tell you - a bad luck streak!"
            me "You weren't punished, were you?"
            show sl sad pioneer with dissolve
            sl "You know..."
            "The girl turned away."
            sl "They didn't punish me. Just checked for shingles and parasites."
            sl "But they don't trust me anymore."
            me "What about the dog?"
            show sl smile2 pioneer with dissolve
            "That question made Slavya cheer up a little."
            sl "All is well! Perfectly healthy, lives in the ferryman's cabin now. He likes him very much: he says Pirate is a good nickname!"
            th "I hope they didn't read through 'Mumu' at school..."
            scene bg ext_warehouse2_day_7dl
            with dissolve
            "At the warehouse, Slavya pulled a single key out of her pocket instead of the familiar bunch."
            if alt_day1_sl_keys_took == 2:
                th "I wonder if they don't trust her with the whole bundle after that failure, or just now they have demonstrably stripped all the privileges of an assistant squad leader?"
            else:
                th "It's kind of embarrassing - she probably got in trouble for her keys, too, and I never bothered to give the girl back her rightful bundle..."
            sl "Come in."
            play sound sfx_door_squeak_light
            scene bg int_attic2_day_7dl
            show sl normal pioneer
            with dissolve
            "There was a faint but distinctive smell of dog in the inventory room."
            th "And here's a box with rags, the standard shelter for the unfortunate animal built by caring backyard children."
            me "You haven't been feeding your animal enough."
            show sl laugh pioneer with dissolve
            "I poked the toe of my sandal into the hole that Pirate had chewed in the corner of the box. Slavya laughed."
            sl "I fed him all right, he ate plenty! He's just little - his teeth itched, so..."
            show sl scared pioneer with dissolve
            play sound sfx_brass_drop
            with vpunch
            sl "Ow!"
            "The girl squirmed, gripping her head with her palms. I threw myself at her before I could even think about what had happened, and..."
            me "{image=alt_KS_censor}!"
            show sl surprise pioneer with dissolve
            "Looking into Slavya's rounded eyes, I smiled guiltily and coughed involuntarily."
            me "What a curious situation, I say."
            me "Who thought of putting up this shelf here anyway?"
            show sl serious pioneer with dissolve
            sl "Sorry, I wasn't the one planning out the rooms."
            show sl normal pioneer far at cleft with dissolve
            $ alt_pause(1)
            show sl scared pioneer far at center with move
            "Slavya rushed to pick up the boxes that had fallen from the shelf. As she picked one up, she recoiled so sharply that she almost hit the shelf again."
            show sl scared pioneer at center with dissolve
            "I looked over her shoulder."
            me "That's..."
            show sl upset pioneer with dissolve
            sl "Rat poison."
            "In a halting voice, the girl said."
            sl "If it'd fallen earlier..."
            "She didn't need to go on. Judging by the crumpled edges of her pet's former abode, she could tell the puppy had been struggling to get out of the box, but he was doing just fine."
            "And I shouldn't have said anything about the itchy teeth."
            me "Don't worry so much, Pirate's not here anymore. I doubt the boatman has poison on every corner."
            show sl serious pioneer with dissolve
            "Slavya shook her head."
            sl "No, I'm just amazed at my own stupidity. Sticking Pirate in here and being glad no one would find him here, and not even bothering to look around the place properly!"
            "I put my hand on her shoulder."
            me "If we could have known in advance of all the troubles to come, humanity would have known no grief, Slavya."
            me "Just accept it as a fact: shit happens."
            me "And thank whoever you believe in that it all worked out this time."
            show sl sad pioneer with dissolve
            "The girl's shoulders slumped wistfully."
            sl "You're right. Let's clean up already!"
            me "What do you have to do?"
            th "Cleaning, as you know, is a very abstract concept. For some people it's about licking every scrap of space, and for others it's about removing socks and other traces of human activity from the floor."
            th "And I'm more of the latter."
            sl "Let's just say to clean up all traces of the Pirate's presence here, and to put away the inventory a little more carefully."
            me "Okay, I'll take care of the inventory."
            dreamgirl "You're squeamish, aren't you?"
            th "Well, it's not my dog, after all!"
            th "Besides, those shovels must weigh a ton..."
            scene bg int_attic2_day_7dl with joff_r
            "An hour later, the warehouse was still a mess, but everything my hands could reach was more or less level. Slavya had finished shoveling the white hairs out of all the corners, too."
            show sl normal pioneer with dissolve
            sl "It's just a little while till noon."
            "The girl looked at the fruits of my labors and sighed faintly."
            th "She would have been here..."
            scene bg ext_warehouse2_day_7dl
            with dissolve
            show sl smile pioneer with dissolve
            sl "I want to visit Pirate. Will you come with me?"
            "The offer was undeniably tempting, but I shook my head."
            "What the hell do I need that dog for? I've got my own things to do."
            dreamgirl "Dog stuff?"
            me "Run to your beloved already!"
            hide sl with moveoutleft
            "Laughing happily, Slavya closed the warehouse and hurried off down the path. After a little hesitation, I followed her toward the square."
            th "I'll sit there on the bench and think about eternal things. Isn't that the end of a beautiful day's work?"
        "Help with outfits":
            $ lp_dv += 1
            $ alt_day6_dv_dj_quest = 3
            th "The costumes hardly weigh too much for this task to be seen as work in principle."
            th "And Alisa will be there, too. Maybe I'll nestle in a corner and watch - they won't kick me out, will they?"
            me "I'll go get the costumes. What if Miku doesn't have time for everything?"
            "The squad leader nodded."
            mt "Good. Since everyone's got their tasks, I won't hold anyone back."
            hide us
            hide sl
            hide el
            hide dv
            hide mt
            with dissolve
            "The pioneers went on their errands, and I dashed toward the music club, hoping to catch up with the redhead."
            scene bg ext_musclub_day with dissolve
            "But no way!"
            "There's no sign of Alisa. That meant one of two things:"
            th "Either Alisa was so ashamed of herself that she galloped off to rehearsal, or, like the lazy one in the camp, she ran off in an unknown direction, and I couldn't find her until noon."
            "And knowing Dvachevskaya, I don't even need to guess - I won't see her in the music club."
            "I'm in a bad mood."
            th "But she could have waited for me! To catch me up and snatch me away, and save me from useless work!"
            "Thoughts were dragged into an already familiar and pleasant direction."

            show dv laugh pioneer2 with dissolve
            show prologue_dream
            dv "Hey, Semyon! Are you deaf?"
            dv "What costumes? Miku's not a little girl, and she seems to know Russian pretty well - she'll find someone to ask."
            dv "Let's go to the forest - I saw a wild apple tree there, I'm sure the apples are ripe."
            show dv grin pioneer2 with dissolve
            dv "Only I can't reach it myself. Can you give me a lift?"

            scene bg ext_musclub_verandah_day_7dl with dissolve
            "I reached the porch of the music club, but the miracle never happened. {w}With a heavy sigh, I knocked on the door."
            play sound sfx_knock_door2
            mi "Open!"
            pause(1)
            play sound sfx_open_door_2
            pause(1)
            scene bg int_musclub_day
            with dissolve
            play ambience ambience_music_club_day fadein 3
            play music music_7dl["what_am_i_doing_here"] fadein 1
            "Inside, to my surprise, it was empty. Only in the middle of the usual decoration of the music club was a rack, densely laden with rags."
            me "I thought there should have been a few more people at the rehearsal for the closing concert of the shift."
            "I muttered to myself."
            "And the hanger immediately rolled toward me!"
            th "What the hell!"
            dreamgirl "Didn't you hear the story of the coffin on wheels as a child?"
            mi "Semyon, is that you? Could you help me, if you don't mind, I can't see anything!"
            "With a slight panic in her voice the revived hanger asked."
            "I hurriedly took off Miku's mountain of costumes. The girl snorted and sneezed, shaking off the dust and fixing her muffled tails."
            show mi smile pioneer with dissolve
            mi "Thank you so much, what would I do here without you!"
            mi "You see, at first I saw everything perfectly, and then the hat came over my eyes, but I still remembered where I had to go, and then I bumped the trombone with my foot and turned around, forgetting that I was wearing this stupid hat, and I got completely lost..."
            me "Then why did you carry all your suits on you at once, you onion woe?"
            "I interrupted this fascinating monologue."
            show mi laugh pioneer with dissolve
            mi "The rehearsal is in full swing! Everyone's waiting for me!"
            th "Apparently I overestimated Miku's mental capacity when I suggested that she might have asked the speakers for help..."
            "Miku bent over, furiously shaking off her skirt from the clinging threads."
            mi "We'd better get going soon, or Danya's in there... Ah!"
            $ alt_pause(0.5)
            play sound sfx_body_bump
            $ alt_pause(1)
            show mi surprise pioneer with dissolve
            "Something small and colorful fell out of her pocket, and rolled across the floor with a clatter. I instinctively rushed to pick up the fallen object, forgetting the mountain of suits in my hands."
            play sound2 sfx_bodyfall_1
            hide mi
            with flash_red
            $ alt_pause(1)
            "Miku and I reacted so quickly and in sync that disaster could not be avoided."
            show mi upset pioneer with dissolve
            mi "Ow-ow-ow!"
            "Whimpered the Japanese girl, grabbing her forehead. I, on the other hand, tried my best to pretend that I couldn't see behind the pile of fallen suits how interesting her skirt had gotten up."
            dreamgirl "Wow!"
            th "Silence!"
            dreamgirl "So this is what we were always taught to rush to the rescue of those around us..."
            show mi sad pioneer with dissolve
            mi "And how will I perform if I have a bump on my forehead now?"
            mi "It's no big deal. Look how cool that hat is!"
            show mi surprise pioneer with dissolve
            "But Miku had already completely forgotten about the bump, noticing on the floor her unfortunate trinket that caused all this commotion."
            mi "Found it!"
            "She proudly raised it above her head..."
            th "Tamagotchi?"
            "I looked closely to see if my eyes were deceiving me. There could be no mistake - it was a pink and blue egg with a screen, which in my distant childhood were found on every corner."
            th "But they started making them in the mid-nineties, not before!"
            me "Where did you get that?"
            show mi smile pioneer with dissolve
            "Miku smiled happily as she showed me the toy."
            mi "Oh, it's a tamagotti, an electronic pocket pet. They started making them in my homeland a couple of years ago, and they don't import them here yet, although everyone at camp really liked him, the younger troop followed me around in droves the first few days, asking to see everything."
            mi "I had to tell them that I lost it and hide it away. I'd almost forgotten about it myself by now, there's so much to do in the last few days."
            th "But how? Isn't that too sophisticated a technology for the eighty-seventh year?"
            $ alt_day6_dv_dj_secret = (not alt_day4_dv_dj_radio_scoff and alt_day5_dv_dj_map == "un")
            if (alt_day6_dv_dj_secret):
                th "Although I have heard so many contradictory things in recent days that I am no longer sure of any dates..."
            me "Can I see it?"
            "A cheerful piece of plastic with a screen, three buttons, and a string on the side fell into my palm. I twirled it in my hands at a loss, trying to remember if there had been anything like it before the Tamagotchi I saw."
            show mi happy pioneer with dissolve
            mi "Alisa also liked it very much, I was even surprised, I thought she wasn't interested in such toys. She couldn't stop admiring it!"
            mi "She said she had something similar in her childhood, but she must have confused it with something else, even in our country it is still considered a fashionable novelty."
            show mi happy pioneer with dissolve
            "Miku pursed her lips thoughtfully.."
            show mi sad pioneer with dissolve
            mi "Maybe I should give it to her before we leave as a keepsake."
            if (alt_day6_dv_dj_secret):
                stop music
                $ volume(0.7, "sound")
                play sound sfx_scary_sting
                $ renpy.show("bg int_musclub_day", what = Desat("bg int_musclub_day"))
                with zoomin
                th "IN ALISA'S CHILDHOOD?" with vpunch
                $ volume(1.0, "sound")
                th "No, this is too much! There certainly wasn't anything like it in the early eighties!"
                th "Or did she just see it as similar to the Electronica's masterpiece based on «Nu, Pogodi»?"
                scene bg int_musclub_day
            show mi shocked pioneer with dissolve
            stop music fadeout 3
            "There were a lot of questions, but there were clearly no answers. Miku jumped up from the floor and hastily picked up the scattered costumes."
            play music music_list["smooth_machine"] fadein 5
            mi "They're waiting for me on the stage!"
            "I hurriedly gathered up the rest of my rags, still clutching the ill-fated toy in my hand."
            me "Then let's go already, Comrade Artistic Director!"
            $ alt_pause(1)
            play ambience ambience_camp_center_day fadein 2
            scene bg ext_backstage_alt_day_7dl
            with fade
            "The stage was a mess: the younger kids were having gladiatorial fights, threatening to blow branches off all the official equipment, and the older kids were just sunbathing on the wooden benches."
            "I dumped the costumes on the edge of the stage and looked sympathetically at Miku."
            me "Can you handle them?"
            show mi sad pioneer with dissolve
            "She nodded uncertainly."
            mi "It's nothing, it's just that sometimes it takes a long time to get in the mood before rehearsal..."
            "After making sure (or rather convincing myself) that the situation was under control, I shoved the tamagotchi in Miku's distraught hand and hurried away."
            "I really wanted to plug my ears with something to get rid of the intrusive thoughts in my head, but Alisa had the player, so I had to make do with whistling."
            scene bg ext_house_of_mt_day with guess_on
            $ alt_pause(0.2)
            stop ambience fadeout 2
            scene bg int_house_of_mt_day
            with dissolve
            play sound sfx_unlock_door_campus
            $ alt_pause(0.5)
            play ambience ambience_int_cabin_day fadein 3
            stop music fadeout 3
            "I didn't feel like looking for a new job, so I staggered back to the cabin for the remaining hour before noon."
            "Stretching out on the bed, I stared up at the beveled ceiling."
            if (alt_day6_dv_dj_secret):
                play music "<from 15.0>" + music_7dl["time_lapse"] fadein 3
                $ renpy.show("bg int_house_of_mt_day", what = Desat("bg int_house_of_mt_day"))
                with touch
                th "Why is my head so messed up?"
                th "What I've known all my conscious life is questioned every day in this strange place."
                th "Tamagotchi was released in the late eighties, and everyone knew about the band Splin a few years before it appeared. And then there's that unknown Genda..."
                th "There's obviously something wrong here. And something tells me that it's not with me, but with everything around me!"
                th "What did Alisa say?"
                show bg int_clubs_dj_7dl
                show dv sad pioneer2
                show prologue_dream
                with dissolve
                dv "It's like everything else here. It's all fake, it's all phony."
                hide dv
                hide prologue_dream
                $ renpy.show("bg int_house_of_mt_day", what = Desat("bg int_house_of_mt_day"))
                with dissolve
                th "It seems to me that someone is very inept at leading me astray. Fudging the facts, feeding me wrong information to..."
                th "To do what?"
                dreamgirl "You're paranoid, buddy!"
                dreamgirl "What's next? Decide that this camp is a testing ground where you've been shut down and told nothing about the world around you as part of an experiment?"
                th "But it does seem true, doesn't it!"
                th "I could hardly even find out the year. Where I am geographically, I haven't the faintest idea."
                dreamgirl "Because for those around you, this information is such a solid part of their picture of reality that it doesn't need to be voiced."
                dreamgirl "In your own words, default information. Both for themselves and for everyone they meet here."
                dreamgirl "If you weren't such a tightwad, you'd formulate questions that would require your squadmates to name specific cities and numbers."
                th "Yeah. And then I'll slip up, and a bunch of local SWAT teams will jump out of the bushes and put my face in the asphalt..."
                dreamgirl "So pessimistic..."
                th "I'm sorry, if you live with me, you'll forget how to believe in good things."
                stop music fadeout 3
                show blink with dissolve
                "My eyes were slipping against my will."
                th "It's okay, I'll figure it out..."
            else:
                "My eyes were closing against my will."
                show blink with dissolve
                th "It's okay, by noon someone will definitely remember me and wake me up."
                th "Surely..."
            scene bg int_house_of_mt_day
            show unblink
            with dissolve
            $ alt_pause(0.5)
            show mt normal pioneer with dissolve
            mt "Are you going for lunch or not?"
            me "Huh?" with hpunch
            show mt smile pioneer with dissolve
            "I almost fell off the bed out of surprise. Olga standing next to me giggled."
            mt "So you will. I won't get a second bun..."
            hide mt with dissolve
            play sound sfx_close_door_1
            $ alt_pause(1)
            "She went out the door, and I hurried to follow."
            if (alt_day6_dv_dj_secret):
                th "Questions are questions but food is on a schedule!"
        "Ask if there's anything else to do" if alt_day6_dv_dj_bet:
            $ alt_day6_dv_dj_quest = 4
            $ lp_dv += 1
            hide us
            hide sl
            hide el
            hide mt
            with dissolve
            "I threw a questioning glance at Alisa, who still hasn't left."
            show dv normal pioneer at fleft with dissolve
            me "You know, about the errands..."
            show mt sad pioneer far behind dv with dissolve
            mt "Well?"
            dv "Our amplifier's broken. We have to fix it while we have time."
            dv "You need it at the dances, too!"
            show mt angry pioneer far behind dv with dissolve
            "Olga looked at Alisa incredulously, then fixed her gaze on me."
            mt "Aren't you going to break it all the way down? I wouldn't want to take that risk."
            mt "Sergei and Sasha will be free in no time and they'll take a look right away."
            me "It's not a big deal, really - re-solder one input, put some tape on it, and you're good to go."
            me "It's just a matter of figuring out which one of the inputs is malfunctioning. Alisa's player will be needed."
            th "If you talk about something confidently enough, they'll believe you, no matter what nonsense you say."
            me "Don't worry, Olga Dmitrievna! I'll let Alisa go to rehearsal as soon as we find a way out, and then I'll fix everything."
            mt "Well, if you know what you're doing, get your feet in your hands and go!"
            show mt normal pioneer far behind dv with dissolve
            mt "Dvachevskaya, I'll ask Miku later if you were at the rehearsal!"
            scene bg ext_houses_day
            show dv laugh pioneer
            with dissolve
            "After bowing out to the squad leader, Alisa and I almost ran towards the clubs, hardly able to contain our laughter."
            dv "Well done, you're starting to think faster!"
            th "Madam, you're a master at compliments!"
            show dv smile pioneer with dissolve
            dv "You can count my exemption from rehearsal as my wish for today's argument."
            me "I hope karma doesn't punish us, and the amplifier doesn't deflate right during the disco."
            show dv grin pioneer with dissolve
            dv "What's that got to do with me? It's my job to find a bad input, you're the only one who signed up to be the repair master."
            me "Is that so? What about 'if the whole world turns against a man, the faithful wife will stand behind him and give him ammunition'?"
            show dv smile pioneer with dissolve
            dv "We're not married, stupid!"
            me "I see."
            "I stuck my hands in my pockets, making as indifferent a face as my rarely good mood allowed me to."
            me "So I'm just that to you, a summer resort fling?"
            dv "Yep. It's the eighth one this shift, by the way."
            me "And I thought you weren't like that! I couldn't imagine wanting a divorce before I was even married."
            show dv laugh pioneer with dissolve
            "Alisa laughed."
            dv "Look at him, he's so adamant! He was also planning to dress me in a burqa, so that no one else would have me!"
            me "And a chastity belt, too!"
            show dv grin pioneer with dissolve
            "I turned toward the clubhouse, but Alisa froze to the side with a questioning arched eyebrow."
            dv "Are you serious about sitting in the radio room?"
            me "We should at least put a piece of duct tape on the amplifier so Hat won't have any questions. She doesn't trust us very much as it is!"
            show dv dontlike pioneer with dissolve
            "The redhead just rolled her eyes."
            dv "What you can't do for your paranoia..."
            stop music fadeout 3
            scene bg int_clubs_male_day with touch
            play ambience ambience_clubs_inside_day fadein 1
            play music music_7dl["sily"] fadein 3
            "The cybernetic abode was clean. TOO clean."
            th "It seems that while we were saying hello this morning, the guys didn't waste any time: they put everything into boxes and shelves. Now how do you find anything in here?"
            "Back in the days when I lived with my parents, cleaning always meant one thing - all the necessary things from their usual places would be re-hidden in distant and not the most convenient corners. And now I couldn't see the cherished skein of blue, black duct tape that was always lying right in the middle of the desk."
            "I leaned over to the first drawer I saw."
            th "It seems the place will be even more of a mess after our search than before..."
            show dv normal pioneer with dissolve
            me "What are you standing around for? Help me look, or we'll be here for the rest of the shift!"
            scene bg int_clubs_male_day with joff_r
            "After a good half hour of chaotic searching and swearing, the clubhouse was once again in creative disarray, but the duct tape was finally extracted."
            me "Now all that's left to do is to stick it somewhere nice..."
            "I muttered to myself, dragging my booty into the radio room."
            "After making a nice little cross around one of the sockets, I looked at my work with satisfaction - it looked like some sort of manipulation of the amplifier had been done."
            me "Now we're free as birds in the sky, Dva..."
            me "What did you dig up there?"
            show dv think pioneer with dissolve
            "Alisa had an extremely confused expression on her face, and in her hand she was clutching some kind of tube."
            dv "Moment-1 glue. That's what a lot of people at the orphanage huffed."
            th "What's she getting at?"
            th "It's not like she's gonna..."
            me "Put the glue down! I won't let..."
            show dv sad pioneer close with dissolve
            dv "Come on! I'm not crazy enough to sniff that crap yet."
            show dv sad pioneer close at ba_sit_down_unfzdv
            "She sighed and returned the tube to where she had taken it, and then sat down on the floor with her head thrown back. I sank hesitantly down beside her."
            dv "I just remembered something: it was nighttime, everyone was in their bunks, and there was screaming in the hallway. I crawled out to see what was going on, made my way to the bathroom, where everyone was crowded together, and there was my bandmate, Valerka, lying on the floor."
            dv "Dead. And there's a bag next to him."
            show dv sad_smile pioneer close:
                ypos 0.15
            with dissolve
            "Alisa grinned, looking at my dumbfounded face."
            dv "In case you're wondering, I got my ass kicked. So I wouldn't talk about what I'd seen."
            show dv sad pioneer close with dissolve
            dv "But everyone found out anyway. Of course, they tried to tell us the story that Valerka had been taken into the family, but everyone knew that he was a sniffer. And I blabbed, what the hell?"
            dv "And after that the inspections started. There was a commotion - words can't describe it!"
            dv "Almost everyone had cigarettes and cigarette butts, glue was also not uncommon. Vodka was not hidden - if anyone got it in their hands, they drank it down in the same second."
            me "You had a lot of fun out there, though. Did you have any normal activities?"
            show dv smile pioneer close with dissolve
            dv "Activities? Come on!"
            dv "We went to exercise, ate some porridge, and then we're off to class. In the afternoon, you can have all the fun you want."
            dv "If you want, ride the streetcar without paying, if you want, collect bottles to buy a pie at the train station, if you want, look for lost cats in the ads, and maybe they'll give you a reward."
            dv "There was only one TV set for everyone in the hall, so it was always occupied by the elders. You could sit quietly with them, of course, but there were few good seats, and the floor froze my ass off badly."
            th "Somehow I saw the seventies of the USSR as more prosperous..."
            dv "We only went to the movies once a month on Saturdays. What a holiday that was!"
            dv "True, the last year of my life there I went to the movies often. I got in on the busiest days, when there were a lot of people and I could get lost in the crowd. I sat in the back row without moving and watched."
            dv "They took us to a children's show, but I loved action movies. I went to one of them three times, but I don't remember anything except the scene at the end, where the heroes were holding hands and there were explosions..."
            show dv think pioneer close with dissolve
            dv "Whoever I tell, nobody remembers it."
            th "I wouldn't hesitate to say 'Fight Club,' but it's obviously not that kind of thing."
            me "Do you want to go to the movies after camp?"
            show dv smile pioneer close with dissolve
            dv "I want to, of course! Something interesting must have come out there while I was rotting away."
            th "I wish I knew what was waiting for me after camp..."
            me "Do you think we'll make it to the movie?"
            show dv shy pioneer close with dissolve
            "I winked, and Alisa blushed to the roots of her hair."
            dv "Oh, you... Pervert!"
            "Laughing, I got up off the floor."
            stop music fadeout 3
            me "Let's clean this place up and go to lunch. It's taking too long to get our repairs done!"
            scene bg int_clubs_male_day with joff_r
            play sound sfx_7dl["eat_horn"] fadein 1
            "We tidied up the clubhouse just in time for the horn to sound. Although Alisa's stories almost made me lose my appetite."
            "To go through that kind of hell as a child and still be human is worth a lot. Lucky she was pulled out of that shit at eight instead of fifteen!"
    stop music fadeout 3
    stop ambience fadeout 5

    if (alt_day6_dv_dj_quest != 4):
        scene bg ext_square_day with fade3
        play ambience ambience_camp_center_day fadein 2
        play music music_list["your_bright_side"]
        "A noisy crowd of performers marched from the side of the stage. Of course, Alisa wasn't among them."
        th "Who could have doubted it..."
        th "If she was at rehearsal, she must have skipped out the second Miku blinked!"
        "As soon as the children, led by the hooter, disappeared, a redhead peeked out from behind the bushes, making me jump."
        me "Alisa?"
        show dv grin pioneer with dissolve
        "The girl smirked as she came up to me."
        dv "If Miku had noticed me, too much noise would have come out."
        me "How long have you been sitting there?"
        "Myself at this point was frantically wondering if I'd been picking my nose in the last five minutes."
        dv "As soon as things got quiet on stage, I went right out after them."
        me "So you spent the whole rehearsal sitting out there?"
        dv "Yeah."
        show dv smile pioneer with dissolve
        "Alisa stretched herself with pleasure."
        dv "Listened to the music in the tree behind the stage. But the rehearsers still managed to shout it out."
        dv "We're in for a hell of a concert!"
        show dv smile pioneer far with dissolve
        "Clapping me on the shoulder, the girl moved forward."
        dv "Let's go eat, labor hero!"
        stop music fadeout 3
        stop ambience fadeout 5

    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 2
    "There was a lively atmosphere in the canteen: those who were not gripped by the upcoming concert were anticipating the evening dances. The last one, and therefore special."
    if alt_day6_dv_dj_quest == 1:
        "I was munching on my second bun when Miku jumped up to me and Alisa."
    else:
        "I was already munching on my bun when Miku jumped up to me and Alisa."
    show mi dontlike pioneer with dspr
    mi "Alisa, did you forget about the rehearsal again?"
    show dv dontlike pioneer at right with dspr
    "The redhead quietly gritted something through her teeth before turning to the flustered Japanese girl."
    dv "To be honest, I wasn't gonna go there anyways. I'm not going to perform."
    th "What do you mean you won't?!"
    play music music_list["no_tresspassing"]
    show mt angry pioneer at left with dissolve
    mt "What do you mean you won't?!"
    "The squad leader, who appeared out of nowhere, was not happy about what she heard. She hovered over Alisa, but she didn't raise an eyebrow."
    show dv angry pioneer at right with dissolve
    dv "I don't want to. Anything wrong with that?"
    show mt rage pioneer at left with dissolve
    mt "So you're saying there will only be two performers from the first squad? From the first one, Dvachevskaya: all the younger kids look up to you!"
    th "'Look up' is a loud word!"
    "Unlike most camps I've been to, the local kids didn't pester the older ones, didn't make friends with Slavya, for example, and even the girls in the second squad didn't look up to the promising suitors from the first squad."
    th "Although prospective suitors here..."
    show dv rage pioneer at right with dissolve
    dv "Let them look up to Slavya and Miku. I'm, you know, a destructive element here - it's better not to show me to honest people at all."
    hide dv with moveoutleft
    show mi shocked pioneer with dissolve
    "Alisa finished her kefir in a gulp and walked away, ignoring the three indignant looks escorting her to the sink."
    mi "And what fly bit her?"
    "Miku seemed ready to cry. Olga's nostrils were steaming."
    th "Once again Alisa leaves others in an idiotic situation!"
    show mi dontlike pioneer with dissolve

    menu:
        "Run after Alisa":
            $ lp_dv -= 1
            $ alt_day6_dv_dj_dv_run = True
            stop music fadeout 3
            me "I'll talk to her."
            show mt angry pioneer at left with dissolve
            mt "And tell her that when she comes back, she'll have a thorough conversation with me, too!"
            scene bg ext_dining_hall_near_day with dissolve
            play ambience ambience_camp_center_day fadein 1
            play music music_7dl["too_quiet"] fadein 3
            "As I finished my kefir, I rushed after Alisa, who was already leaving the dining room."
            show dv angry pioneer far with dissolve
            me "Alisa!" with vpunch
            "She didn't react. She didn't flinch, she didn't turn around, she didn't slow down."
            me "Hold up!" with vpunch
            "No reaction."
            th "What is wrong with you?"
            hide dv
            show dv angry pioneer at center with dspr
            "I sped up, overtaking the girl and blocking her path."
            me "Are you going to talk to me or not?!"
            show dv rage pioneer with dissolve
            dv "Why are you bothering me?" with vpunch
            "Alisa shouted angrily. A couple of onlookers who had been watching me chase hurried away when they smelled something fishy."
            me "What was that?"

            show dv angry pioneer at center with dissolve
            dv "Why on earth would I owe them anything?" with vpunch
            "The girl glared at me with eyes burning with anger."
            dv "I'm sick of all this as it is!"
            me "Why?"
            show dv tired pioneer at center with dissolve
            "Turning away, Alisa exhaled noisily."
            dv "Just forget it. There are things I can't explain."
            th "Another bout of teenage rebellion?"
            if lp_dv <= 15:
                th "This is so annoying!"
                th "Why does she always force others to run after her and talk her into it?"
                th "Oh, Alysonka, would you be so kind as to be a DJ? We'll give you a player so that you don't have to deal with records, and we'll arrange a cozy room for you, and give you a partner so that you don't get overworked!"
                th "But you'll never be satisfied: you'll always be dissatisfied with something. Always!"
                th "Sometimes I begin to think that you only let people closer to you so that you can bite them more easily. To hurt them as hard as you can, to hurt them more."
                th "And do you really think I'm going to swallow that again?"
                "I looked at Alisa's absent face, forcefully suppressing my anger."
                th "I will swallow it. But I won't forget."
            else:
                th "How I sometimes wish I could just look inside your head, Alisa. See the world through your eyes, and understand why you do things the way you do."
                th "I know it's not just a fad -- I can see with my own eyes how bad you feel."
                th "But how can I help if I don't understand your problem?"
                "Alisa stood across from me with a detached face. I took her hand gingerly."
                me "It's not forever. It will get better."
                me "It will."
                show dv sad pioneer with dissolve
                "She only shook her head."
                dv "It will..."
                "Her fingers slipped out of my palm."
            dv "Shall we go to this idiotic concert?"
            me "If you don't want to, we can..."
            dv "It was a rhetorical question."
            show dv sad_smile pioneer with dissolve
            "Alisa grinned bitterly."
            dv "It's been three years since I sat in the audience. I'd forgotten what it was like."
            th "I don't understand her logic at all!"
            th "But if a woman's up to something, the chances of dissuading her are nil."
            me "Let's go."
            stop music fadeout 3
            "With the same mournful face, Alisa moved toward the stage, and I could only drag myself along, amazed at the sudden change in her mood."
        "Talk to squad leader":
            $ karma +=10
            me "Don't be angry with her, Olga Dmitrievna. She's going through a difficult period in her life, and..."
            mt "She is always going through a difficult period. I'm tired of putting up with all these tricks!"
            me "You could talk to her in a human way, not accuse her of all her sins!"
            show mt angry pioneer with dissolve
            stop music fadeout 3
            "The squad leader measured me with a murderous look."
            mt "What other recommendations for my work will I hear from my pioneer?"
            play music music_7dl["to_the_sunrise"] fadein 3
            show sl serious pioneer at right with dissolve
            sl "Semyon is right."
            if alt_day5_dv_dj_sl_jeer == 1:
                "That's exactly where I wasn't expecting help from!"
            else:
                "I had nothing against Slavya's help, but something told me it was no use: it would only add one more head to the pile."
            sl "Alisa doesn't have to perform. We have plenty of performances as it is!"
            sl "And she's also sick, so..."
            show mt normal pioneer with dissolve
            mt "Feoktistova, I don't remember asking for your opinion!"
            show sl sad pioneer at right with dissolve
            "Olga straightened up, and it was clear from her face: she would remain deaf to our pleas to pardon Alisa."
            mt "Don't be late for the concert. Some of you still have to perform."
            hide mt with dissolve
            "Miku, who had been silently observing the scene of the massacre, hurriedly shoved the remains of the bun into her mouth and raced toward the exit."
            hide mi with moveoutleft
            show sl sad pioneer at center with dissolve
            "I, in turn, looked gratefully at the pale Slavya."
            me "Thank you, of course, but you shouldn't have gotten into this..."
            show sl upset pioneer with dissolve
            "Slavya shook her head."
            sl "It's kind of a tradition already. I stand up for Alisa, and all I get is bumps from all sides."
            th "What?!"
            show sl smile pioneer with dissolve
            "Seeing my perplexed face, the girl smiled sadly."
            sl "Alisa didn't like me from the moment she walked into class. She was always picking on me, sometimes overstepping her boundaries so much that I would come home and cry from helplessness."
            sl "And then I found out... About some of the details of her past."
            me "About her being adopted?"
            show sl dontlike pioneer with dissolve
            "Slavya nodded, frowning her eyebrows."
            sl "Already whispered?"
            me "She told me herself."
            show sl upset pioneer with dissolve
            sl "When I learned that, I felt sorry for Alisa. I started defending her in front of her teachers and classmates, no matter what nasty thing she did."
            sl "But that only made her angrier. It was only much later that I realized that people don't like to be pitied. It's humiliating for them!"
            sl "But I can't help myself, Semyon! I feel sorry for everybody anyway."
            th "Both people and animals, yes, yes. We heard about that."
            show sl sad pioneer with dissolve
            sl "Alisa feels it and hates me!"
            me "And then, at the last concert, when you started saying nasty things about her - didn't you feel sorry for her then?"
            show sl upset pioneer with dissolve
            "Slavya lowered her eyes."
            sl "I felt sorry for you."
            show sl shy2 pioneer with dissolve
            sl "I see the way you look at her, the way you rush to help her, no matter what happens. Girls are sensitive - we feel and understand such things very well."
            sl "I just didn't want you to be hurt when you got to know the real Alisa. Maybe it's really none of my business, but..."
            me "You can't help yourself?"
            "I grinned, looking at the embarrassed Slavya."
            me "I don't hold a grudge against you, Slavya."
            if alt_day5_dv_dj_sl_jeer == 1:
                me "I hope you can forgive me, too."
                sl "Why should I forgive you? You told the truth yesterday: it was very selfish of me not to tell the adults about Pirate."
                sl "At least he's safe now, and he doesn't have to sit locked up in a dark warehouse anymore."
            show sl smile pioneer with dissolve
            "The girl smiled."
            sl "I better run before Miku gets worried."
            hide sl with dissolve
            stop music fadeout 3
            "I watched her leave. There was no animosity between Slavya and Alisa, just a deep misunderstanding and too different views of life."
            th "How complicated things are around here..."
            dreamgirl "You'd think you were simple!"
            "After I finished my kefir, I hurried after the last of them to the dining room door. Looking for Alisa was pointless, so all that was left was to go watch the local circus, called by the buzz word 'concert.'"
    stop ambience fadeout 3
    return

label alt_day6_dv_dj_concert:
    scene bg ext_stage_big_day_7dl with fade3
    play ambience ambience_camp_center_day fadein 2
    play music music_7dl["old_kiss"] fadein 3
    if alt_day6_dv_dj_dv_run:
        show dv normal pioneer with dspr
        "Alisa and I only got seats in the very last row."
        "It was hard to say, however, that this fact discouraged us in any way."
        "At the end of the day, we didn't care about the concert in the same way."
    else:
        "I was seated in the very last row. The concert didn't bother me at all, so this fact didn't upset me one bit."
        th "I wonder where Alisa is planning to hide?"
        show dv normal pioneer at left with dspr
        "But Alisa didn't seem to be planning on hiding. As if from nowhere, the girl landed on the bench next to me."
        me "Decided to watch the buffoonery?"
        show dv tired pioneer at left with dissolve
        "She shrugged indifferently."
        dv "What else can I do?"
    show dv smile pioneer at left with dissolve
    "Suddenly the girl raised her head, and her troubled face cleared up in an instant."
    dv "Ulyana! Come here!"
    show us normal sport at right with moveinright
    "A tardy Ulyana came galloping over to us, looking at Alisa with mild bewilderment."
    "And here you are? I thought that when everyone was busy, you'd go back to your carnal..."
    show mt angry pioneer with dspr
    mt "What's all this small talk? The concert's about to start!"
    "The squad leader measured Alisa with a heavy stare, but tactfully didn't start a showdown in front of the whole camp."
    hide mt with dissolve
    show us grin sport at center with move
    "With her lips pressed together, Olga retreated to the stage, and meanwhile the redhead managed to squeeze her little girlfriend onto the bench between us."
    us "Why aren't you performing?"

    dv "You know, I decided that since it's my last time at camp, I should enjoy all this shame!"
    show dv laugh pioneer
    show us laugh sport
    with dissolve
    "The girls giggled. I smiled faintly - I was clearly not invited to the conversation."
    if lp_dv >= 20:
        th "In general, who cares? The main thing is that Alisa is smiling."
        th "Almost sincerely."
    else:
        th "As usual, Semyon is put on the shelf when there are more interesting toys around."
        th "Well, it's almost a tradition."
    dv "What's your fiancé going to show us today?"
    show us angry sport with dissolve
    us "He's not my fiancé!"
    "Ulyana instinctively threw up her fists, charging under my ribs with her elbow. She didn't even notice it, though."
    us "And anyway, why doesn't your fiancé serenade you from the stage?"
    show dv grin pioneer
    show us dontlike sport
    with dissolve
    "Two looks came into my eyes: an angry, questioning one, and an indifferent, mocking one."
    me "I somehow..."
    dv "Not everyone is endowed by nature with talents as generously as Dan'ka, Ulyana."
    show us calml sport with dissolve
    "The girl flared up, and I felt myself beginning to boil over with her."
    th "If I'd said something like that about Alisa in her presence, my nose would have turned into a flapjack in a second. She's allowed, isn't she?"
    if lp_dv <= 15:
        th "I should understand insults as compliments, not otherwise. I'm a masochist, I like it when people spit in my face in public!"
    th "Why does Alisa never miss an opportunity to trample me? If it's such an extravagant way to show her love, why doesn't she go after Miku and Ulyana?"
    dreamgirl "Maybe you're on her special list?"
    th "Yeah, sure. That bucket of slop she has reserved exclusively for her heart's VIP guests!"
    "Two girls in rather shoddy cat costumes were leaving the stage, and Miku was announcing her own number."
    show us smile sport with dissolve
    us "I hope Miku comes next year. Without her, the concerts were just a bore of death!"
    show dv smile pioneer with dissolve
    dv "Remember how two years ago at the winter camp Dima's throat got sick, and the rest of the first squad had to perform the concert?"
    show us laugh2 sport with dissolve
    us "Yeah, that was quite a commotion! By the time they had decided on the roles and who was going after who, the concert was over."
    us "Remember last year when some smart guy brought a mirror and started blowing bunnies in the eyes of the performers?"
    show dv laugh pioneer with dissolve
    "Alisa laughed evilly."
    dv "He never confessed to you?"
    show us surp1 sport with dissolve
    us "Who?"
    dv "Danka! I'm the one who gave him the mirror!"
    show us angry sport with dissolve
    us "What a bastard! That's all right, I'll remind him of that..."
    th "I hate the moments when people in my presence start reminiscing about their shared past. I can't help feeling not just superfluous, but rather like an alien element that will never be my own."
    th "You are forever assigned the role of the newcomer, seems to be what Ulyana calls me? - who can always be forgotten."
    "I was frankly jealous of Ulyana, who had seen so much in Alisa's company. I was frankly angry with Alisa for never being as firmly entrenched in her life as Ulyana."
    th "This kid is a close person to her. She goes into fire and into water for her, and into the canteen after lights out."
    th "And I am forever assigned the role of a clown, which only strengthens their already strong friendship."
    scene bg ext_stage_normal_day
    show mi smile voca
    with dissolve
    mi "And now Daniil Sumarokov, second troop, performs for you."
    play sound sfx_7dl["applause_someone"] fadein 1
    stop sound fadeout 5
    scene bg ext_stage_big_day_7dl
    show dv normal pioneer at left
    show us angry sport
    with dissolve
    us "Alright!"
    us "If I hear one joke, I'll bite you."
    dv "You don't have to joke about it. He can handle himself."
    dv "I'd rather not serenade him than..."
    us "Oh, yeah!"
    $ alt_pause(0.33)
    show us angry sport at cleft with move
    play sound sfx_punch_medium
    with flash
    $ alt_pause(0.3)
    play sound sfx_punch_medium
    with flash
    $ alt_pause(0.1)
    play sound sfx_punch_medium
    with flash
    $ alt_pause(0.1)
    show dv surprise pioneer with dspr
    "Ulyana threw herself at her friend, carrying out her threat and clacking her teeth viciously next to Alisa's fending off arm."
    dv "All right, all right, calm down, not another word about your lover!"
    us "Uooh!"
    hide dv
    hide us
    with moveoutbottom
    "The girls fell on the grass behind the bench with laughter."
    dreamgirl "What a lovely scene!"
    dreamgirl "We ought to get them together more often..."
    scene bg ext_stage_normal_day with dissolve
    "I frowned as I turned away from the stage, feeling no desire to stare up Alisa's skirt."
    dreamgirl "What a fool."
    dreamgirl "The sun is warm, the birds are singing, the girls are shining in interesting places - live and enjoy!"
    dreamgirl "And what a musical accompaniment..."
    scene bg ext_stage_big_day_7dl
    show dv laugh pioneer at left
    show us laugh sport at center
    with dissolve
    "The disheveled girls returned to the bench just in time for the end of the sonic torture, proudly called the 'metallophone solo'. Alisa was wiping away her tears of laughter, and even Ulyana looked quite satisfied with her revenge."
    "She joined in the meager applause and then gave a thumbs-up to the 'groom,' smiling mischievously into her twenties and something."
    stop music fadeout 2
    "My redheaded girl friends have forgotten all about me."
    play music music_7dl["no_hope"]
    th "Once again, I have the feeling that somewhere I've been really warmed up."
    th "Why is it that Alisa, who has nightmares and who, for reasons unknown to anyone alive today, is sick of this damn world, appears only near me?"
    th "Next to others she comes alive, laughs, and looks as if nothing matters to her. Next to others, she's the Alisa who's going to show it to everybody."
    if lp_dv > 15:
        th "How many more excuses do I have to come up with to stop asking myself the same question day after day?"
    else:
        th "As if other non-verbal hints that she doesn't consider me a human being weren't enough for me!"
    hide us
    show dv laugh pioneer2 at center
    show prologue_dream
    with dissolve
    dv "Going to a concert? Are you overheating in the sun?"
    "Alisa from my thoughts laughs wickedly."
    dv "It's deadly boring anyway. Come, I'll show you such things..."
    show bg ext_library_day with diam
    stop ambience fadeout 1
    $ alt_pause(1)
    "She's leading me to the library, while she's also throwing barbs at everyone who's planning to speak at this idiotic event."
    play sound sfx_close_door_campus_1
    show bg int_library_day with diam

    play ambience ambience_library_day fadein 2
    dv "There's a spare ladder here so no one can steal it - even Zhenka goes to the library from under a stick, you can't think of a safer place!"
    show bg ext_sky_7dl with diam
    show dv soft_smile pioneer2 with dspr
    "On the hot roof, she stretches out, exposing her whole self to the sun. She opens one eye and looks at me, stretching her lips in a snide grin."
    dv "You really do seem like a retard..."
    "What about me?"
    "And I don't need to be asked twice!"
    show dv shy pioneer2 close with dspr
    "Her hands hastily loosen the tie around my neck as I untie the knot on her shirt."
    dv "Move it - the concert isn't endless!"
    "I bite her earlobe, running my fingers through her red hair..."
    with flash_pink
    stop music fadeout 1
    play ambience ambience_camp_center_day fadein 1
    scene bg ext_stage_big_day_7dl
    show dv normal pioneer at left
    show us normal sport
    with dissolve
    us "Hey, newbie!"
    me "Huh?"
    play music music_7dl["out_of_painkillers"] fadein 3
    "Ulyana pulled me out of my fantasies so abruptly that I involuntarily blushed, as if I had actually been caught doing something obscene."
    show us calml sport with dissolve
    us "Did you fall asleep in there?"
    us "Help me better solve the question, do the Japanese eat raw fish, or is Alisa pranking me again?"
    me "They do. With wasabi and ginger."
    me "It's quite tasty, by the way."
    show us dontlike sport with dissolve
    "Ulyana grimaced."
    us "You're just conspiring! Miku doesn't look like a savage to eat that kind of crap!"
    "All I did was snicker."
    me "Ask her yourself, you'll learn a lot about eastern food."
    th "I wonder if foreigners are so common here that no one has even asked Miku about her homeland?"
    show dv laugh pioneer at left with dissolve
    "Ulyana muttered something about rich people going abroad, and Alisa gave a triumphant chuckle."
    th "I bet as soon as we were alone with Alisa, she would immediately make a sorrowful face and not even want to have a polite conversation..."
    "The concert was coming to an end, and so was my patience."
    th "If she won't continue to explain anything, I'm not responsible for myself!"
    scene bg ext_stage_normal_day
    show mi smile voca
    with dissolve
    mi "Thank you for this wonderful concert to all the performers!"
    play sound sfx_concert_applause
    "The pioneers applauded noisily, more out of joy that the most boring part of the day was finally behind them. Only dinner and dancing awaited them ahead."
    "And perhaps some nighttime mischief, too. There was no toothpaste here, but no one had ever cancelled the good old green stuff, had they?"
    mi "See you next summer, Sovyonok!"
    scene bg ext_stage_big_day_7dl with dissolve
    "Everyone jumped sharply from their benches, stubbornly ignoring the calls of their squad leaders to line up, and hurried toward the canteen. In all the confusion, I lost sight of Alisa - she and Ulyana were the very first to rush out."
    th "Well, I'll talk to Alisa after dinner. I don't feel like making a scene in the canteen."
    "I wandered to the back of the noisy and hungry crowd, mentally preparing myself for more surprises from my fickle date. But something told me that nothing good was in store for me today."
    stop music fadeout 2
    return

label alt_day6_dv_dj_dinner:
    scene bg ext_dining_hall_near_sunset with dissolve
    play music music_7dl["fyrsta"]
    "The crowd on the porch hummed joyously, and the more the pioneers' merriment grew, the deeper I withdrew into myself."
    th "I guess I'm a selfish bastard after all, but I don't have the strength to suppress it: I can't share Alisa's happiness in those brief moments when she laughs."
    th "Because it is impossible to share what you are not offered!"
    "The noisy pioneers squeezed their way into the canteen, and I paced monotonously, driven forward by someone else's impatient whining behind me."
    th "Why am I so dreary on this fine evening?"
    th "Is it not because a few more rows of bricks have been erected right in front of my nose over a solid, impenetrable wall that seemed to me, even yesterday, to be about to collapse?"
    show mi normal pioneer with dissolve
    mi "Can I come with you?"
    "I nodded mechanically, not even bothering to think about the question."
    "The panting Miku had already changed into her uniform, and she looked extremely pleased. That meant only one thing-an unscheduled verbal rape was coming."
    th "If you, beautiful Japanese maiden, were the stereotypical anime schoolgirl - perpetually embarrassed and speechless at the sight of the opposite sex, you'd be worthless."
    th "It's true that for some reason this role was taken over by a totally Union cartoon schoolgirl from our squad..."
    show mi smile pioneer with dissolve
    mi "I was so afraid that I would get tired at the concert and not be able to dance at the disco, but somehow I think I have even more energy than usual - I could push a whole carriage!"
    th "So save your charge for the disco, sweetheart. It's obviously not enough to shake me up."
    "But instead, for some reason, I asked:"
    me "Who are you planning to dance with?"
    show mi surprise pioneer with dissolve
    "Miku clapped her eyes in surprise, as if I had asked my question backwards."
    mi "Dance? You mean the slow dance?"
    mi "There's no fast dancing here."
    show mi smile pioneer with dissolve
    "The girl's eyes brightened."
    mi "I get it!"
    mi "You want to invite me to make Alisa jealous. Don't you?"
    th "No way!"
    me "And I didn't do anything..."
    "But Miku was unstoppable:"
    show mi happy pioneer with dissolve
    mi "And then she'll make a scene for you at the dance, maybe you'll even fight a little bit, Alisa is so hot-tempered..."
    mi "And then she'll run back to her cabin and you'll be begging her forgiveness under her windows till morning, and by morning she'll let you in because she realizes she can't live without you!"
    mi "And then..."
    voice "Are you coming in or what?"
    show mi surprise pioneer with dissolve
    "With a loud 'ow', Miku ducked into the canteen. I followed, relieved, hoping to get lost in the crowd."
    with dissolve
    pause(1)
    play sound sfx_open_door_2
    scene bg int_dining_hall_people_sunset_7dl
    with dissolve
    play ambience ambience_dining_hall_full fadein 3
    "I wasn't hungry, so I grabbed the first food on my tray and glanced around the dining room. Alisa was sitting in the corner. Alone."
    me "You run fast."
    "No matter how hard I tried, the reproach didn't disappear from my voice."
    show dv sad pioneer at left with dissolve
    "Alisa looked up at me tiredly, and then stared down at her plate again. Her dinner looked untouched: she was picking at the garnish with her fork, resting her cheek with her left hand."
    "I sat across from her and began silently devouring my dinner. I was afraid that once I opened my mouth, it would be impossible to stop me."
    th "It's just as I thought. When Ulyana was gone, the fun was gone."
    th "For Semyon's sake, why try to at least give out a smile? He's unpretentious; a sour face is enough for him to be happy!"
    th "You don't have to tell him anything, he's not a kid anymore, he's had telepathy at school!"
    "With my side-eye, I noticed Olga coming towards our table."
    th "Apparently, I'm the only one in this camp who uses common sense and doesn't consider the canteen a place to have an argument..."
    show mt smile pioneer at right with dissolve
    mt "What did you think of the concert, Alisa?"
    "There was enough venom in those affectionate intonations to kill a squad or two."
    show dv normal pioneer at left with dissolve
    dv "The usual."
    show mt sad pioneer at right with dissolve
    "The girl didn't even look at the leader. Olga frowned."
    mt "I hope you realize that the whole camp is counting on you this evening?"
    show dv surprise pioneer at left with dissolve
    dv "Eh?"
    mt "Dancing, Dvachevskaya. As the staff DJ of camp radio, you're supposed to lead the disco."
    show dv sad pioneer at left with dissolve
    dv "Ask Semyon. I'm not going."
    "I tensed, expecting at least deafening screams. But the squad leader's tone remained the same calm and vulnerable:"
    show mt smile pioneer at right with dissolve
    mt "And a diploma for active participation in the life of the camp should I also only give to Semyon?"
    show dv angry pioneer at left with dissolve
    "Alisa clutched the edge of the table so hard that her knuckles turned white."
    dv "Hand it to whomever you want. I'll make do without it."
    hide dv with MoveTransition(0.5, leave=offscreenright)
    show mt shocked pioneer at right with dissolve
    "She got up from the table so sharply that all the dishes bounced. Before I could open my mouth, the girl ran out of the canteen, nearly knocking the door off its hinges."
    th "And what was that?"
    dreamgirl "You know you met at a strange time in her life..."
    dreamgirl "And Viola did warn you!"
    show mt normal pioneer at right with dissolve
    "I got up from my chair, and Olga measured me with an icy stare."
    mt "I can't rely on you, either."
    "She didn't ask - she asserted. And that was the only thing that saved her from my righteous wrath."
    hide mt with dspr
    "Forgetting about the trays, I rushed after Alisa."
    th "Well, hold on, Dvachevskaya, I'm going to tell you what I think about this!"
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day6_dv_dj_no_dance:
    scene bg ext_square_sunset with fade3
    play ambience ambience_camp_center_evening fadein 2
    play music "<from 41>" + music_7dl["so_be_it"] fadein 2
    "I caught up with Alisa only at the square. I didn't call out, because I knew she wouldn't turn around."
    show dv angry pioneer close with dspr
    "With a sharp jerk, I turned the girl toward me, making her look me straight in the eye."
    me "What. The fuck. Was. That?!"
    "Alisa broke free of my grip, bouncing back a good meter."
    show dv rage pioneer with dissolve
    $ alt_pause(0.3)
    dv "Not your." with vpunch
    extend " Fucking." with vpunch
    extend " Business!" with vpunch
    "She shouted back."
    dv "You're just like them! You're all the same! Dolls! Hollows!"
    "I was taken aback. It's not that I wasn't expecting the shouting back, but..."
    me "And you're the most special one? Not like the others?"
    me "The whole camp is carrying you around like a piece of crap, they're ready to carry you in their arms, if you press the 'play' button twice a day at the right time!"
    me "And what do you do in return? You spit in everyone's face!"
    me "Look how independent she is, she doesn't need a diploma!"
    show dv dontlike pioneer with dissolve
    dv "I don't need this diploma!"
    dv "What am I going to do with it? Show it at flatshows?"
    show dv angry pioneer with dissolve
    "Alisa's fists clenched."
    dv "I don't want your concern, I don't want it, I don't want it! Leave me alone, I don't care about any of you!"
    with flash_red
    "Somewhere in my chest it suddenly hurt."
    me "Me, too?"
    "In a steady voice I inquired."
    show dv rage pioneer with dissolve
    dv "You too! Go to hell!"
    dv "I don't need anybody, hear me? Nobody!"
    "In the ringing silence I thought my heart had stopped beating."
    show dv rage pioneer with dissolve
    "And Alisa..."
    "She was leaving."
    "Without saying goodbye, as she always does."
    show dv rage pioneer far with dissolve
    "But clearly not intending to return."
    hide dv with dspr
    stop music fadeout 5

    scene bg ext_square_sunset with fade3
    "The square was filling up with people, and I was still standing still, staring thoughtlessly at one point."
    play music music_7dl["what_if"] fadein 3
    th "And who was it that pulled my tongue?"
    th "Why did I even bring up that damned diploma? Who needs it anyway?"
    th "Idiot, idiot, idiot!"
    "I knew it wasn't about the letter. It wasn't even about how much Alisa didn't care about camp life."
    th "If only I knew how to talk to her properly..."
    th "And did she want to talk at all?"
    us "What did you do to Liska?" with hpunch
    show us sad sport with dissolve
    "Ulyana poked me in the side and stared angrily into my eyes."
    us "She was never like that, and you..."
    me "What's that got to do with me?"
    "I snapped back."
    me "Your friend has so many cockroaches in her head that no amount of insecticide will save her!"
    show us dontlike sport with dissolve
    "The girl grinned."
    us "She was normal before she met you!"
    me "Is she crying?"

    "Some inexplicable fear gripped me. Fear that I had once again broken what I dared to touch."
    us "Hell no! As if she'd be crying tears over random passerbys."
    us "She's lying on the bed, listening to your bling. She wouldn't talk to me, told me to shut up and get out."
    "Suddenly the girl showed her fist to me in a threatening manner."
    show us angry sport with dissolve
    us "If you touch her, I'll kill you!"
    if alt_dv_dj_ends == 'good':
        "Even without the little one's valuable advice, I knew it was a lost cause to talk to Alisa now."
        th "With two hot heads, we'll make such a mess of it..."
    elif (alt_dv_dj_ends == 'neu' or alt_dv_dj_ends == 'rej'):
        th "No way! I'll lose my voice from yelling so much."
        th "Surprisingly, I'm willing to listen to the kid this time. Maybe it would work itself out - aren't there miracles in life?"
        "But I knew perfectly well in my head that nothing would work itself out."
    elif alt_dv_dj_ends == 'true':
        show us dontlike sport with dissolve
        "I looked at Ulyana thoughtfully, and she shivered."
        us "Why are you staring at me?"
        me "Nothing. It's just..."
        me "Realized I had some things to think about."
    else:
        th "You'd think I'd want to try to get something out of that hysterical girl again!"
        "I was fed up with Alisa, and I didn't want to see her now, or today, or for the rest of this shift, or for the rest of my life."
    me "Don't worry, little girl, I'm not going to your girlfriend's house. And don't look at me like that - go hypnotize your fiancé."
    play sound sfx_punch_medium
    hide us with dissolve
    "I shoved the grunting girl aside and staggered away from the party of life to which I had again forgotten to be invited."
    "I gave the square one last frown, to make sure once again that no one here was going to cry for me."
    "Behind the turntables was Miku. She noticed my gaze and shouted something, waving vigorously, but I pretended her voice was lost in the first chords of the opening song."
    stop music fadeout 8
    th "If I stay here, I'm sure I'll kill someone. If not babbler Miku, then Her Redhead's brave protector, Ulyana."
    th "Or, at the very least, Slavya - there's always a reason for her."
    scene black with fade2
    play music music_7dl["beth"] fadein 3
    $ alt_pause(2)
    scene bg ext_playground_sunset_7dl with dissolve
    "Away from the noise, my mind became a little clearer. I stopped at the sportsground, wondering for a second what had happened between me and Alisa."
    th "She just cut me out of her life, didn't she?"
    th "Just as suddenly and abruptly as she opened her soul yesterday at the lake."
    th "Actually, what am I talking about? She doesn't have a soul."
    "I grinned mirthlessly at my own pun, which did not fit at all with the tragic notes of the evening."
    "My own words came to mind:"
    show prologue_dream
    me "I think I've made it pretty clear that I don't want to see anyone."
    me "Not even you. How are you any different from the others?"
    hide prologue_dream
    "I wasn't the only one who had to swallow grudges. I wasn't the only one who was sick of misunderstandings."
    "Maybe if I hadn't turned my back on her, if I hadn't hurt her with indifference and a harsh word, things would be different today."
    with vpunch
    "I shook my head."
    "It couldn't have been otherwise."
    th "Alisa probably thinks she's hurt me terribly with her shouting... if she thinks about me at all, of course."
    th "But she'll never get the idea that the silence has gotten to me much worse!"
    th "I guess I really am nothing to her."
    dreamgirl "Did she say otherwise?"
    th "And she didn't say otherwise. She didn't say anything at all about the bond that has developed between us these days."
    th "'I feel at ease with you' - the loudest words I've been honored with in all my efforts. For all my efforts to brighten her dreary existence in this retirement home mimicking a children's pioneer camp!"
    th "Apparently it's my destiny to drown and drown everyone who happens to be around. The more I tried, the more I wriggled around trying to evoke even a semblance of sincere emotion in Alisa, the more glassy her eyes became."
    th "She seems to have completely stopped paying attention to anyone other than herself."
    dreamgirl "I see, I see."
    dreamgirl "It's so hard with self-centered people..."
    th "And what am I, an old man, doing, killing myself over a girl who can't hold back her temper for the sake of basic respect for others?"
    th "And it's okay if she's snapping at me, a passing crocodile, but what did Miku, Ulyana, and even Olga Dmitrievna do to her?"
    $ renpy.show("bg ext_sky_7dl", what = Desat("bg ext_sky_7dl"))
    with fade
    "I leaned my back tiredly on the soccer goal frame, staring up at the blackened sky."
    th "And if I ask myself frankly, do I even love her?"
    if alt_dv_dj_ends == 'good':
        th "I love. I certainly do."
        show dv smile pioneer2 tr1 with dissolve
        th "For her cheerful laughter in those moments when she doesn't want to die."
        th "For her shenanigans that make me blush to the tips of my ears and burn with shame every time."
        th "For her recklessness and reliance on chance, for her laziness and brazen shirking of all work, for her weak-mindedness and daring..."
        th "Hell, I love her even for the fact that she loudly chomps in the canteen!"
        dreamgirl "My goodness, sir, you are insane!"
        dreamgirl "Think back, did somebody hit you on the head?"
        th "You nerd!"
        hide dv with dissolve
        "My hoarse laughter echoed across the empty lot."
        th "And I'm... and I'm pretty good myself."
        th "Instead of going and telling her about it all, I'm going crazy here in the company of my split personality."
        th "Only does she need to hear it all?"
        "I peeled away from the frame, pulling a stiff back."
        th "I don't know."
    elif alt_dv_dj_ends == 'neu' or alt_dv_dj_ends == 'rej':
        th "Tough question…"
        show dv normal pioneer2 tr3 with dissolve
        th "If so, why am I here now and not with her?"
        th "And if not, why won't she get out of my head?"
        hide dv with dissolve
        "With a quiet sigh, I straightened up."
    elif alt_dv_dj_ends == 'bad':
        th "Is it even love?"
        show dv sad pioneer tr1 with dissolve
        th "Just a parody. We're just kids who are bored and want to play at being adults."
        th "I don't care if one is in his thirties and the other is going to college in a year. They're a quarter of their brains apart."
        th "It's not love, and there's never been any love."
        th "But I can't let her go either. It's stuck, in pain, in sweat, in blood..."
        th "A suitcase without a handle, by golly."
        hide dv with dissolve
        "I straightened up."
    stop music fadeout 3
    scene bg ext_playground_night with dissolve
    th "I should go for a walk."
    th "God forbid one unstable madam gets tired of sitting in the cabin and decides to wander about the night camp!"
    play music music_7dl["nobodys_secret"] fadein 3
    scene bg ext_path_sunset with dissolve
    play ambience ambience_forest_evening fadein 3
    "Even on my first day here, I noticed a hole in the fence. Until today, there had been no time or reason to seek adventure, but now I had nothing to lose."
    th "If I get lost, they'll find me. After all, they won't pat Olga on the head for a missing pioneer..."
    scene bg ext_path2_night with dissolve
    "I could hardly make out the forest path, but it was clearly a walkable path, which definitely led to something interesting."
    th "What could be interesting here, though? Some glade with wild berries or a shack, or even a flooded ravine teeming with all sorts of amphibian nasties."
    "However, I had no other options for brightening up my lonely last night at camp."
    "But the change of location had no effect on my inner state; my thoughts were stubbornly confined to a single name."
    if alt_dv_dj_ends == 'true':
        th "Alisa is not like everyone else I've met here. And that's troubling."
        th "It's like she's out of the picture. A broken pixel on the monitor, which has no effect on the image transmission, but irritates the eye to the point of gritting my teeth."
        th "And it's not that she's rude or a bully - Ulyana's no angel either, and her friends..."
        th "There's just something foreign about her. Her look is too much like the one I've seen in the mirror since I was born."
        th "It's the look of someone who knows the world is going to the abyss and has no idea how to stop it."
        th "The look of a man from another world."
    else:
        th "Well, I'm rapidly catching up with my current appearance mentally: tomorrow there will be a scrapbook of disgusting poetry on the redhead's porch. And then I'll fight Ulyana for the right to sit with her friend on the bus."
        "It was ridiculously absurd: in my head, the possibilities of events were jumping from rosy to dystopian at the speed of light. It was hard for me to guess which ones were closer to reality."
        th "If I were a fatalist, I wouldn't torture myself with my speculation now, or later with regrets about all the times I took a wrong turn."
        "I sped up my pace, seriously regretting giving the Walkman to Alisa for the first time all week - the music might have drowned out my agonizing thoughts just a little."
        th "Things will get better."
        $ renpy.show("bg ext_path2_night", what = Desat("bg ext_path2_night"))
        with fade
        th "It's all over."
        scene bg ext_path2_night with fade
        th "Things will get better."
        $ renpy.show("bg ext_path2_night", what = Desat("bg ext_path2_night"))
        with fade
        th "It's all over."
        scene bg ext_path2_night with fade
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day6_dv_dj_un_night:
    play sound sfx_wind_gust
    "The trail turned sharply to the right, and I felt a gust of cold and wet wind."
    play music music_7dl["brigh_you"]
    scene cg d5_fz_un_pixies_7dl with dissolve
    play ambience ambience_boat_station_night fadein 2
    "The moonlit wild beach grew before my eyes."
    "And by the water, a lonely figure was barely discernible."
    th "Alisa?.."
    scene bg ext_un_hideout_night_7dl with dissolve
    show un surprise pioneer far with dissolve
    "As if she sensed the appearance of a stranger, the girl turned and flinched, meeting my gaze."
    th "There's our runaway. I wonder if she's been here all day."
    show un sad pioneer far with dissolve
    un "What are you..."
    "Lena whispered hoarsely, rising from the sand."
    show un sad pioneer far with dissolve
    "She took a timid step in my direction, and I froze in a stupor."
    "Uncomfortable questions were inevitable."
    show un cry_smile pioneer far with dspr
    un "Alisa, huh?"
    "Her voice sounded ingratiating."
    if (loki and alt_dv_dj_ends == 'bad'):
        stop music fadeout 4.5
    "I didn't see - rather felt - the corners of her lips lifting up in an understanding smile."
    if (loki and alt_dv_dj_ends == 'bad'):
        play music music_7dl["silent_angel"] fadein 4
        "In the nasty smirk of a divorcée who had finally gotten her way, and no longer had to hide her triumph."
        th "What a bitch you are!"
        th "Thought I didn't see all the looks you threw at me?"
        if alt_day5_dv_dj_map == "un":
            th "Thought you won my heart with that tearful confession?"
        th "Did you think this escape would be revenge for the fact that I didn't choose you?"
        me "What about Alisa?"
        show un sorrow pioneer with dspr
        "My feigned affectionate tone made Lena cringe."
        me "Disgraced and shamefully abandoned, and now lies in tears in her cabin."
        show un shocked pioneer with dspr
        "With a chuckle I muttered, stepping forward menacingly."
        me "That's what you want to hear, isn't it?"
        show un scared pioneer with dspr
        un "What are you talking about?"
        show un scared pioneer close with dissolve
        "The girl exclaimed in horror."
        un "You and her... And you left her?"
        "There was fear in her eyes."
        "She took a step back, but I grabbed her hand roughly, not letting her escape."
        me "Yes. To come running to you."
        me "This is what you've been waiting for all day, isn't it?"
        me "ISN'T IT?!" with vpunch
        un "Let me go!"
        "Lena was on the verge of panic, but there was no stopping me."
        me "So why aren't you so happy to see me, sweetheart?"
        me "You won, didn't you!"
        with hpunch
        "With a sharp movement, the girl tried to charge between my legs with her knee, but I dodged, anticipating this maneuver."
        play sound sfx_punch_washstand
        with flash_red
        "I pulled her arm toward me, and Lena smashed into my chin with her forehead."
        un "I'll scream!"
        play sound sfx_bones_breaking
        show un cry pioneer close with dissolve
        "Her fist almost reached my ribs, but I intercepted the girl's other hand as well, squeezing her thin wrist until it crunched."
        "Now she was at my mercy."
        me "And who's going to hear you? It's a kilometer to the camp, we're all alone here."
        me "Why aren't you still hanging around my neck?"
        play sound sfx_bodyfall_1
        with vpunch
        scene cg d6_un_rape_7dl with dissolve
        "Lena tried to break free again, but I pushed her without loosening my grip, and we flew straight to the sand."
        "She sighed in pain and fright as I pressed her with my whole body."
        un "Please don't..."
        "Quietly whispered the girl. Her eyes were wide open and tears were rolling down her face."
        "I put my hands behind her head, gripping them with one palm. With my free hand I clutched her chin."
        if  alt_day5_dv_dj_map == "un":
            me "Where are all those beautiful words you were saving for me? Have you forgotten the sudden happiness that came over you?"
        else:
            me "Why don't you tell me something romantic? You know, I'm tired of talking alone!"
        un "Stop..."
        "Her whole body was shaking in a coarse shiver."
        "I leaned into the girl's face, peering into eyes full of despair."
        me "You don't like it?"
        "I whispered furiously, making Lena whimper softly."
        scene cg d6_un_rape2_7dl with vpunch
        me "I don't like it when strangers pry into my soul, either!"
        "That last word I literally spit in her face."
        "The girl twitched and closed her eyes, as if expecting a blow."
        stop music2 fadeout 4
        scene bg ext_un_hideout_night_7dl with dissolve
        "Instantly unclasping both hands, I rolled to the side."
        show un cry pioneer with dissolve
        stop music fadeout 1.5
        "Lena jumped to her feet, breathing heavily."
        play sound "<to 3.0>" + sfx_7dl["cry"]
        play music music_7dl["lynn"] fadein 5
        "There was a loud sob on the beach as the stupor released my frightened victim."
        me "You can go - I don't need you for nothing. And don't you ever speak of Alisa again."
        un "You... You..."
        un "You will pay for everything!"
        hide un with moveoutleft
        "Shouted she, before running toward the path."
        "Staring up at the black sky, I howled softly."
        "I felt almost physically sick at what I'd done."
        dreamgirl "Don't you think it was too much?"
        th "I think so."
        dreamgirl "And you're not going to do anything about it, of course."
        th "What can I do? Admit that I'm a monster?"
        th "I'll gladly admit it."
        th "I shouldn't have taken it out on the girl, for sure she was the source of all my troubles, not myself."
        "I felt bad."
        "I wanted to throw myself in the river to cleanse myself of my own dirty deed."
        th "If she told anyone, in ten minutes the whole camp would be here with torches and pitchforks."
        th "At best, I'll be beaten to death, at worst, castrated."
        th "And if Alisa found out..."
        "Lena didn't seem capable of talking about this nightmare with even her nearest and dearest."
        "And that meant only one thing: this night I gave the girl a deep psychological trauma that will probably poison the rest of her life."
        th "What else will I have time to do before the end of my shift? Whose other fate am I going to meddle in?"
        "The splash of water was not soothing, no matter how hard I tried to muffle my unhappy thoughts."
        th "I wish I could drown and have no more problems. No more torment, no more remorse, no more anger."
        th "But alas, nature has made me too cowardly for such things."
        show black with fade
        "I closed my eyes tiredly."
        "The realization that the easiest way out was literally a few feet away made it worse."
        scene bg ext_un_hideout_night_7dl
        show unblink
        with dissolve
        "According to my senses, the dances should have been over by now."
        "Going back was scary, but I had no choice."
        "Without even bothering to shake off the sand from my uniform, I wandered slowly down the path toward the camp."
    elif ((not loki) and (alt_dv_dj_ends == 'bad')):
        "Only I didn't need the understanding of some pussy."
        th "I should have just turned around and walked away, but that leech won't get away with it..."
        show un sad pioneer with dissolve
        "Lena came closer."
        un "Did you two have a fight?"
        me "You're the shrewdest."
        show un surprise pioneer with dissolve
        "I grumbled acerbically. The girl flinched."
        un "If you don't want to talk about it..."
        me "Exactly, I don't want to. I don't remember you and I becoming buddies during this shift."
        if alt_day5_dv_dj_map == "un":
            me "And you, I remember, told me to stay away from you."
        show un serious pioneer with dissolve
        "Lena lowered her head and sighed softly."
        un "I understand you more than you think..."
        me "You're all so understanding, I can't get enough of you! This camp is a bunch of brainiacs!"
        show un scared pioneer with dissolve
        show un sad pioneer with dissolve
        "My scream made the girl shudder."
        me "Alisa is this, Alisa is that, I've known Alisa half my life, Alisa, Alisa, Alisa..."
        me "What do you think I am, the last idiot? Do I need a detailed manual to build my relationship with a person?"
        "I moved to the side, slowly circling around Lena but keeping my gaze on her."
        me "Is it so hard to let me work out my own problems with Alisa?"
        me "And keep your advice to yourself - I don't remember ever asking anyone for it!"
        stop music fadeout 3
        me "Or are you so eager to gloat over my grief just because I chose someone other than you?"
        hide un with dspr
        play music music_7dl["heartfelt"] fadein 2
        "Standing with my back to Lena, I closed my eyes, trying to suppress my anger."
        th "That last one was unnecessary. Who was pulling my tongue?"
        th "But if she doesn't leave, I won't stop yelling. I have too many grievances against those around me to hold back!"
        "There was a quiet sob in the silence. I shuddered."
        th "Sobbing girl is exactly what I need here right now!"
        show un laugh pioneer with dissolve
        "When I turned around, I saw Lena shaking. She wasn't crying - she was convulsing, laughing hysterically."
        un "Well, you..."
        show un evil_smile pioneer with dissolve
        "She wiped the tears of laughter from her eyes and straightened up. Her face was angry and stark."
        un "I was afraid it was him again. But you don't seem any better."
        th "What's she talking about?"
        show un rage pioneer with dissolve
        un "You say all these nasty things to me because I'm weaker than everyone else, right?"
        un "You don't have the guts to bicker with Slavya or Ulyana. Lena, on the other hand, is defenseless; you can pour your bile out on her without remorse!"
        show un angry pioneer close with dissolve
        "She flew up to me in three steps and slapped me in the face."  with hpunch
        me "Oh you…"
        show un rage pioneer close with dissolve
        "But the girl flashed her eyes angrily, silencing me."
        un "Remember: I won't let anyone - ANYONE - talk like that to me anymore! Not you, not him, not anyone else!!"
        show un serious pioneer with dissolve
        "Lena hissed, then stepped back and threw a look of disgust at me."
        un "Although I think I'm being vain here - you're completely deaf and blind when it comes to other people's feelings!"
        hide un with dspr
        "Lena left, leaving me utterly bewildered."
        th "Who was she talking about?"
        "I involuntarily touched my still sore cheek."
        dreamgirl "What difference does it make?"
        dreamgirl "I think she did the same thing you did."
        "..."
        th "Tell me more, please."
        dreamgirl "Took her anger out on the other person. Thought you were the only one so smart?"
        th "Yet my schizophrenia never tried to shame me!"
        "But let's face it, I was really embarrassed."
        if alt_day5_dv_dj_map != "un":
            "Accusing Lena of having any feelings for me (unless, of course, they were in my delusions) was supremely low."
        else:
            "After that touching confession, to use Lena's feelings to hurt her more was supremely swinish."
        "I sat down on the sand and put my arms around my head."
        th "And what kind of relationship would I need? I can't even talk to a girl I don't know without a scandal!"
        "By my reckoning, Lena was just about to make it to camp. And that meant that it was time for me to follow, too."
        th "I understood nothing, decided nothing for myself, made no conclusions, but gained a new enemy. A productive evening, nothing to say!"
        "I got up from the damp sand and wandered towards the camp."
        th "I'll have to put off all the hard thinking until tomorrow. They've worn me out too much, all these... natives with their cockroaches in their heads."
    elif alt_dv_dj_ends == 'neu' or alt_dv_dj_ends == 'rej':
        me "Alisa, yeah."
        show un sad pioneer with dissolve
        un "Whatever she said to you, don't take it personally, okay?"
        me "What makes you think she told me and not me told her?"
        show un laugh pioneer with dissolve
        "Lena chuckled."
        un "Because I know what it's like to fight with Alisa."
        if alt_day5_dv_dj_map != "un":
            "Didn't I tell you that we've been friends since elementary school?"
        show un normal pioneer with dissolve
        un "As a child, after each of our quarrels, it seemed to me that my world had collapsed, and that nothing good would ever come of it."
        "That was a surprisingly accurate description of how I felt in the square, looking into the back of the departing Dvachevskaya."
        hide un with dspr
        "The girl turned away and sat down again on the sand, gesturing for me to come down beside her."
        show un normal pioneer close with dissolve
        me "Alisa sent me away, and she sent me away in a very specific way. I think I was... kind of a way for her to kill time."
        un "You think?"
        show un serious pioneer close with dissolve
        "Lena tilted her head sideways, studying my face carefully."
        un "Alisa wouldn't hang out with someone she didn't like out of boredom alone. If she let you near her, you must mean something to her."
        "I chuckled bitterly at the naivety of my charming acquaintance."
        me "There are a great deal of gradations between a man who is unpleasant and a man who is pleasant, Lena. Being closer to the latter is undeniably nice, but, as you can see, not enough."
        "Leaning back, I put my hands behind my head and covered my eyes."
        scene stars with dissolve
        me "Alisa made it clear to me more than once that the company of Ulyana or Miku was preferable to mine."
        me "And she didn't snap at them - all I heard was for me alone."
        un "You've got it all wrong..."
        me "No. I got it right."
        show un normal pioneer close with dissolve
        "I opened my eyes and looked at Lena. The girl was still sitting nearby, with her legs tucked under her and leaning slightly in my direction."
        me "Did you know she wanted to go looking for you?"
        show un surprise pioneer close with dissolve
        "My question made her flinch."
        un "I didn't think she'd care about me."
        show un shy pioneer close with dissolve
        "Lena shamefully pressed her head into her shoulders."
        un "If you'd gone missing, she'd have raised the whole camp's ears, too. That's in the spirit of Alisa."
        un "She may be mad at you, but she would never leave you in the lurch!"
        me "I've been missing for two hours, but I haven't met a single search party in that time."
        me "Don't help me build air castles, Lena: I've been doing just fine on my own all week."
        me "Just because Alisa is wonderful and beautiful doesn't make her treat me any better."
        me "Why don't you tell me why you run away every year?"
        show un smile pioneer close with dissolve
        "The girl smiled and shook her head."
        un "I'm sorry, but there are things that are perfectly natural to me, but may seem completely illogical to everyone else."
        un "I can't explain it in a way that makes sense to you."
        th "Oh well: I wasn't going to pry into her soul, and asked out of politeness."
        th "You have to respect a depressed teenager's sacred right to be misunderstood!"
        "We sat in silence for a while. Lena looked at her watch, got up from the sand, and began to shake off her clothes."
        show un normal pioneer with dissolve
        un "Will you go to camp? It's twenty minutes before lights out..."
        "She awkwardly cut her sentence short and turned away, as if suddenly distracted by something."
        th "Doesn't want to go back to camp with me?"
        th "Isn't that why..."
        "I didn't really care about the reasons, though."
        hide un with dspr
        "I closed my eyes again."
        me "Go. I'll catch up later."
        me "I want to clear my head before I go to sleep."
        "Lena left quietly, without a word. After waiting about ten minutes, I followed."
        scene bg ext_path2_night with dissolve
        "My thoughts remained in utter disarray, though I felt better. And to this was added deadly fatigue."
        th "Sleep. Sleep and leave all questions for tomorrow!"
    elif alt_dv_dj_ends == 'good':
        "It made me involuntarily want to smile back, even though I felt bad."
        me "Who else."
        me "She is absolutely unbearable. She goes on a rampage, then she keeps quiet like a fish, then she flails her fists, then she sits quietly next to me like a stray kitten."
        show un sad pioneer with dissolve
        un "Is that why you love her?"
        "My lips finally stretched into a smile."
        me "That's why I love her."
        hide un with dspr
        "I sat down right on the sand, and Lena nestled across from me."
        show un smile pioneer close with dissolve
        un "Alisa can say mean things in a fit of temper, but she cools down very quickly. That's her character, you know..."
        me "I don't hold it against her. I'm like that myself, and I understand her feelings perfectly."
        "For some reason I felt light and bright, like after the first disco."
        th "Why did I really get worked up about Aliska's mood swings? As if it's the worst human behavior I've ever encountered!"
        th "After all, she really needs time to start thinking of me as 'hers' - it's all a big deal to people like her."
        "It made me want to laugh, whether it was from a feeling of unparalleled happiness, or the realization of my own stupidity."
        me "Have you ever had that strange feeling that everything was bound to be all right?"
        show un normal pioneer close with dissolve
        "The girl looked down."
        un "I had. But I'll never trust it again."
        "And before I could ask a question, she continued:"
        show un serious pioneer close with dissolve
        un "My life is not easy, Semyon. I'm not asking you to pity me, not at all!"
        un "It's just that happiness... I don't get it as often as I'd like."
        un "And Alisa is the kind of person who knows how to attract it. In spite of all adversity, she keeps laughing as if the whole world will always dance to her tune."
        un "She and I have parted ways, but you can still bring her back. Reach out and she will come to you."
        me "You think so?"
        "I asked incredulously. The hope in my heart flared with renewed vigor."
        show un laugh pioneer close with dissolve
        un "I know!"
        "Lena laughed back."
        "I jumped up from the sand, feeling in myself ready to run an entire marathon."
        show un laugh pioneer with dissolve
        me "Alright, I'm going to Alisa. And you…"
        show un smile pioneer with dissolve
        "Lena shook her head."
        un "I'd like to stay here a little longer. Run to your sweetheart already!"
        th "I'm so glad I met Lena!"
        th "I'll have to send her a box of chocolates and champagne after camp."
        dreamgirl "They won't sell it to you."
        th "Don't ruin this beautiful evening with your nerdiness!"
        hide un with dissolve
        "I rushed down the path like I was afraid I'd be late."
        th "As if five minutes would make a difference... But I don't want to be a second late!"
        th "I've already wasted too much time on empty grudges."
    elif alt_dv_dj_ends == 'true':
        play music "<from 15.0>" + music_7dl["time_lapse"] fadein 3
        "And then it was like it hit me: the answers to all my questions are closer than ever!"
        th "If anyone can help me make sense of all the strange things I've noticed about Alisa, it's Lena."
        me "Lena..."
        me "Have you ever noticed anything...shall we say, unusual about Alisa?"
        show un serious pioneer with dissolve
        un "What do you mean?"
        "Frowning, the girl asked."
        me "Has she ever talked about things you've never heard of? About music bands, about movies, about people, after all?"
        show un smile pioneer with dissolve
        "There was a look of relief on Lena's face."
        un "Oh, you mean that?"
        un "Yes, she has a sin like that. Alisa has always been such a fantasist!"
        th "Fantasist?"
        un "She used to tell me she was watching a cartoon where the girls were fighting the forces of evil by dressing up in sailors."
        un "I even drew pictures for her from this imaginary cartoon - so strange."
        show un grin pioneer with dissolve
        "The girl smiled dreamily at her memories. Only I wasn't in the mood for fun at all..."
        un "Those girls had big eyes and long legs, and their sailor suits looked not like the boys from Nakhimovka, but like Miku's stage costumes."
        un "And she called it..."
        me "Sailor Moon?"
        un "Oh, so she told you already?"
        "Lena didn't notice how my face stretched."
        show un cry_smile pioneer with dissolve
        un "And that's why you fought with her?"
        me "Not really, but..."
        un "Don't you dare think she's crazy! She has a rich imagination, but I think she herself believes the stories she tells. I read in one..."
        show un normal pioneer with dissolve
        "She hesitated, looking down."
        un "Well, it happens, Semyon. And it's perfectly normal-you shouldn't get mad at her for such silly things!"
        me "I'm not mad!"
        "Everything became abruptly clear as plain as day. But that doesn't make it any less confusing!"
        hide un with dissolve
        $ set_mode_nvl()
        scene bg int_house_of_dv_night
        show dv think pioneer at cleft
        show prologue_dream
        with dissolve
        pause(0.5)
        dv "Really sounds like «Splin»."
        nvl clear
        scene bg int_clubs_male2_night
        show dv concent pioneer2
        show prologue_dream
        with dissolve
        pause(0.5)
        dv "Can you imagine, I was dreaming about that song..."
        dv "From the movie. Where everything blew up at the end!"
        nvl clear
        scene bg ext_un_hideout_night_7dl
        show dv sad pioneer close at cleft
        show prologue_dream
        with dissolve
        pause(0.5)
        dv "When I was here with the orphans... I was eight back then..."
        nvl clear
        scene bg int_editorial_day_7dl
        show un normal2 pioneer with dissolve
        show prologue_dream
        with dissolve
        pause(0.5)
        un "Alisa came from Sovyonok... She even turned down a pass to another camp so she wouldn't leave me alone again!"
        nvl clear
        scene bg int_musclub_day
        show mi smile pioneer with dissolve
        show prologue_dream
        pause(0.5)
        mi "Oh, it's a tamagotti, an electronic pocket pet."
        mi "Alisa said she had something similar when she was a kid, but she must have mixed it up with something, it's still considered a trendy novelty even here."
        scene bg ext_un_hideout_night_7dl
        with dissolve
        pause(0.5)
        $ set_mode_adv()
        hide prologue_dream
        with fade
        th "Alisa isn't similar to me. She's just like me!"
        show un surprise pioneer with dissolve
        un "What's wrong with you?"
        "Lena finally deigned to notice that my body was shaking."
        me "Lena, would you think I was crazy if I asked one very strange question?"
        show un smile pioneer with dissolve
        un "I'm afraid you have nothing to surprise me with."
        "Quietly she grinned."
        me "Do you think time travel is... real?"
        show un serious pioneer with dissolve
        "The girl tilted her head sideways, studying me carefully."
        un "One thing's for sure: traveling between worlds is real. And you know it, too."
        "If the ground was out from under me before, now it was as if I was crashing into the concrete floor." with flash_red
        "I felt my legs wobble." with hpunch
        th "You mean... She knew?"
        th "They ALL knew that I..." with hpunch
        show un shocked pioneer with dissolve
        un "Semyon!"
        hide un with dspr
        scene stars
        with dissolve
        play sound sfx_fall_grass
        "The girl tried to pick me up, but she couldn't - my carcass obviously weighed more than she could lift if she wanted to." with vpunch
        show un shocked pioneer close with dissolve
        un "Shit-shit-shit-shit, not again!"
        show prologue_dream with dissolve
        "The panicked notes in her voice didn't move me. The picture was losing its clarity, and I was beginning to feel queasy."
        un "Don't you dare! Don't go!"
        if lp_dv < 16 or (loki and lp_dv >= 26):
            "Her screams sounded quieter and quieter."
            "And further on."
            th "Whose screams?"
            th "Who's there?"
            th "Where..."
            "I tried to open my eyes, but I couldn't do anything."
            if herc:
                scene bg int_store_7dl with fade
                play sound sfx_7dl["makarych"] fadein 0
                "They were flooded with something viscous, viscous, hot. And it seemed dark red."
                scene black with fade
                pause(1)
                play sound sfx_bodyfall_1
                pause(1)
                stop sound_loop fadeout 0
                play sound sfx_7dl["aunl"]
                $ sdl_persistent_inc("alt_lamp")
                show acm_logo_va_lamp with moveinright:
                    pos (1600, 1020)
                pause(7.4)
                scene gameover with flash
                with vpunch
            elif loki:
                scene bg ext_winterpark_7dl with dissolve
                pause(1)
                show spill_red
                "My eyelashes are stuck together. Froze with each other."
                stop sound_loop fadeout 0
                play sound sfx_7dl["aunl"]
                $ sdl_persistent_inc("alt_lamp")
                show acm_logo_va_lamp with moveinright:
                    pos (1600, 1020)
                pause(7.4)
                scene gameover with flash
                with vpunch
            else:
                play sound sfx_shoulder_dive_water
                pause(1)
                scene anim_underwater
                with dissolve
                "The thickness of the icy water around me made me immediately close them again."
                "A sharp pain pierced my whole body."
                th "I wish it would be over soon!"
                th "I wish..."
                play sound sfx_water_emerge
                stop sound_loop fadeout 0
                play sound sfx_7dl["aunl"]
                $ sdl_persistent_inc("alt_lamp")
                show acm_logo_va_lamp with moveinright:
                    pos (1600, 1020)
                pause(7.4)
                scene gameover with flash
                with vpunch
            return
        $ meet('am',"Me")
        am "Stop being hysterical."
        "Said someone else in my voice."
        am "Shut up, or you'll completely finish him off!" with vpunch
        show un scared pioneer with dspr
        "Lena was frightened into silence, bouncing back from me."
        hide un with dissolve
        dreamgirl "Wake up, man!"
        th "What..."
        th "What happened?"
        hide prologue_dream with dissolve
        "I was able to distinguish my surroundings again. And the trembling Lena a meter away from me."
        dreamgirl "It's okay. You were just nervous."
        th "But Lena..."
        dreamgirl "Forget about that psycho!"
        "My first attempt to get up failed - I got dizzy and collapsed on the sand again." with vpunch
        th "But she knows! She knows who I am!"
        dreamgirl "You do what I say, and take care of all your tender feelings later!"
        scene bg ext_un_hideout_night_7dl with dissolve
        "I'm back on my feet. Coordination is back to normal."
        dreamgirl "Not another word. Wave her off and get out of here."
        show un sad pioneer with dissolve
        un "Are you okay, Semyon?"
        "There was no face on Lena."
        "I could hardly squeeze a smile out of myself."
        me "I'm fine. My blood pressure must have spiked - it happens to me."
        un "Let me help you to the camp..."
        me "Don't. I'll manage on my own."
        th "It's not nice to leave her here alone, but..."
        th "I need to talk to Alisa right away!"
        th "And Lena - Lena would have had to go back alone anyway, if I hadn't wandered in here."
        me "I'll go."
        hide un with dspr
        "I quickly said before rushing towards the camp."
        scene bg ext_path2_night at running
        "Lena shouted something, but her words were lost in my heavy breathing."
        th "The same... The same..."
        th "Alisa came here from my world!"
        "I felt like if I didn't explain myself to her right now, my head would explode with all these thoughts."
        th "How did I not notice this before?"
        "As I picked up my speed, I rushed forward."
        th "The sooner I talk to her, the sooner I can calm down!"
    stop music fadeout 2
    stop ambience fadeout 3
    return

label alt_day6_dv_dj_sleeptime:
    scene ext_playground_night at running
    play ambience ambience_camp_center_night fadein 3
    "When I passed the stadium, there was a palpable burning in my side and my tongue was already glued to my palate, but I kept up the pace."
    "There was no music - the disco was over, which meant I had very little time left."
    th "If only Alisa were still awake!"
    scene ext_house_of_dv_night at running
    show mt pioneer shade at left
    with dissolve
    "At her cabin I noticed a dark silhouette and rushed forward with redoubled vigor...{w}"
    scene ext_house_of_dv_night
    with vpunch
    show mt normal pioneer at left
    with dissolve
    extend " To almost knock down the squad leader."
    mt "Semyon! Why aren't you still in the cabin?"
    th "Anything but this!"
    me "Ol.. ga.. Dmi… I… Ali…"
    "I bent in half, struggling to gulp air."
    th "Just let me catch my breath!"
    me "I... need... to... talk..."
    mt "All talk be kindly left for the morning. Lights out was ten minutes ago."
    me "But it's urgent!"
    show mt angry pioneer at left with dissolve
    mt "First of all, stop yelling. The younger squads are already asleep!"
    mt "Second of all, it was lights out for the whole camp. That includes you."
    show mt angry pioneer at center with dissolve
    "Olga stood right in front of the porch, blocking my way."
    mt "I hope you remember the way to your cabin?"
    mt "I'll give you five minutes to wash up. Chop-chop!"
    "Something told me that throwing a scandal was not the best strategy, no matter how much I wanted it now. Bowing my head, I turned and went back to my cabin."
    scene bg ext_house_of_mt_night with dissolve
    th "It's okay. I'll wait until she's asleep and then I'll sneak out quietly."
    th "Alisa isn't a little girl, she can handle a wake-up call."
    play sound sfx_open_door_1
    stop ambience fadeout 2
    pause(0.5)
    scene bg int_house_of_mt_night
    with dissolve
    play sound sfx_close_door_1
    play ambience ambience_int_cabin_night fadein 2
    "Her intervention at the porch cooled my ardor a little. I didn't even tear the door off its hinges as I entered my retreat."
    "Throwing off my clothes I laid them down so I could get dressed without making a fuss. Picked up the contents of my bag of washing supplies from the floor and placed them on the edge of the nightstand."
    play sound sfx_click_1
    scene bg int_house_of_mt_night2 with dissolve
    pause(0.3)
    play sound sfx_bed_squeak1
    "Turned off the light, crawled under the blanket, and lay quietly waiting for the squad leader."
    if alt_dv_dj_ends == 'good':
        th "I'm a fool after all. Could have just gone to make peace with Alisa instead of running around the camp playing hurtful!"
        th "And then no Olga would have been in our way."
    else:
        th "It took me too long to realize the obvious."
        th "It was easier for me to make an assumption, to pretend I didn't know the dates, than to believe such an incredible and ridiculous story!"
        th "If only I had asked on the first day..."
    play sound sfx_close_door_1
    "The door slammed quietly."
    "From the sounds of it, Olga was changing in the corner."
    "The other bed creaked under the weight of her body, and I tried to steady my breathing to let my leader's guard down."
    "The interminably long minutes stretched on."
    th "The main thing is to not fall asleep..."
    th "The main thing is to not fall asleep..."
    scene black
    show blink
    with dissolve
    th "The main thing…"
    stop music fadeout 4
    stop ambience fadeout 4
    return

label alt_day6_dv_dj_sleeptime2:
    play music music_7dl["unfulfilled"] fadein 3
    scene bg ext_house_of_mt_night with dissolve
    play ambience ambience_camp_center_night fadein 3
    "The light in the cabin was still on when I got back."
    if (loki and alt_dv_dj_ends == 'bad'):
        th "I hope there's no an ambush of the principal, the gym teacher, and a couple of plainclothes KGB agents, who just happened to show up in the local woods..."
        "But only the squad leader was found inside."
    play sound sfx_open_door_1
    stop ambience fadeout 2
    pause(0.5)
    scene bg int_house_of_mt_night
    show mt normal pioneer at right
    with dissolve
    play sound sfx_close_door_1
    play ambience ambience_int_cabin_night fadein 2
    "Olga stood at the closet with a gym bag and was putting her things in it."
    show mt angry pioneer with dspr
    "She frowned at the sight of me, but intense fatigue prevented the squad leader from expressing her displeasure fully."
    mt "You're here?"
    me "Uh-huh."
    mt "March to wash up and go to bed. Lights out was twenty minutes ago."
    show mt normal pioneer with dspr
    "She put the bag on the floor and pulled a nightgown out of the empty closet."
    th "Whether I want to wash my face or not is a matter of tenths. I'll have to go out anyway..."
    show mt angry pioneer with dspr
    mt "And we'll talk about your irresponsibility in the morning!"
    stop ambience fadeout 1
    scene bg ext_house_of_mt_night with dissolve
    play sound sfx_close_door_1
    play ambience ambience_camp_center_night fadein 3
    "After hastily picking up my washing supplies from the floor, which were still there after this morning's flight, I left the cabin."
    scene bg ext_houses_night_7dl with dissolve
    if alt_dv_dj_ends == 'bad':
        "I felt ashamed, disgusted, and wanted to get out of here as soon as possible."
        "Not tomorrow, but preferably right now. And preferably on an empty bus with no Alisa, no Olga, no Slavya, no Ulyana, no Miku..."
        scene bg ext_washstand_night_7dl with dissolve
        "And certainly no Lena."
        "I sincerely hoped she would be asleep by now."
        th "Sleeping, not crying, curled up in bed."
        th "What an idiot I am!"
    else:
        "Some part of me longed to find Alisa and still try to dot the I's and cross the T's..."
        scene bg ext_washstand_night_7dl with dissolve
        "...but the rational part has unapologetically postponed those attempts until the morning."
    scene bg ext_house_of_mt_night with fade3
    play sound sfx_open_door_1
    pause(0.5)
    scene bg int_house_of_mt_night with dissolve
    play sound sfx_close_door_1
    play ambience ambience_int_cabin_night fadein 2
    "On autopilot, after brushing my teeth, I returned to the cabin."
    "Olga was already lying in her bed, turned against the wall."
    mt "Would you be so kind as to turn off the light?"
    "Through sleep she muttered."
    play sound sfx_click_1
    scene bg int_house_of_mt_night2 with dissolve
    "I flicked the switch, threw my uniform on the chair, and climbed into bed."
    play sound sfx_bed_squeak1
    scene black
    show blink
    with dissolve
    "And contrary to my fears, sleep overtook me as soon as my head touched the pillow."
    stop music fadeout 4
    stop ambience fadeout 4
    return

label alt_day7_dv_dj_dream:
    pause(1)
    $ set_mode_nvl()
    scene anim prolog_2 with dissolve
    play music music_list["sparkles"] fadein 2
    if alt_dv_dj_ends == 'good':
        "The hubbub of the crowd, the roaring music, the smells of sweat, perfume and alcohol, the galloping circles of spotlights... Everything merges into a single mass, bright, shimmering, breathtaking."
        "And at the center of all this obscurantism is her. Redheaded, proud, independent."
        "I am drowning in those penny-sized pupils."
        "In the curves of her young body, slippery with glistening sweat."
        "In the glare of the spotlight on her copper hair."
        "But as soon as I take a tiny step, I lose her in a multicolored cloud of alcoholic fumes."
        me "Alisa!"
        "My voice drowns in the noise, in the light, in the smells, and I can hardly distinguish it myself."
        me "Alisa! Alisa!"
        "Behind someone's loud voice I see a familiar face, and I rush forward, struggling to squeeze between the blinding light of the dancers."
        "I imagined it. It's not her."
        "Nausea rushes to my throat."
        me "Alisa!"
        "With a tear in my throat, I scream."
        "It's no use. She won't hear it. But I persist in tearing my throat: I've waited too long for this, and I can't miss her!"
        me "Alisa..."
    elif alt_dv_dj_ends == 'true':
        "There are too many streets in this city. Infinitely the same streets, infinitely the same cars driving down infinitely the same roads to infinitely the same houses."
        "And on the edge of all this infinity is me: small, lonely, and desperately finite."
        "The essence of all infinity is emptiness."
        "And I have no idea how to find it in this emptiness."
        me "Alis!"
        "My voice doesn't even reach the corner of this street. And there are many streets - insanely many."
        "And on all of them endlessly the same people walk."
        "And she's gone."
        "I run, exhausted, but nothing changes. And it's beginning to dawn on me:"
        "There's none of that."
        "And she..."
        "And she's bound to be there!"
        "She can't not be!"
        "It can't be!"
        me "Alisa!"
    else:
        "In my left hand is the guitar's neck, in my right plectrum."
        "And my fingers are so wooden and unruly that a burning anger rises in my chest."
        "It must sound like her sleepy and angry face in the morning."
        "But the strings make only a sad squeak."
        "I just want to hear her sassy look again!"
        "It's a rattling sound in my ears again."
        "It's not working. It's not working!"
        "It never does."
        "It's like everything else I do."
        "It's my lot to quit halfway through."
        "So is playing the guitar."
        "So is trying to be an adult."
        "So is Alisa."
    pause(1)
    $ set_mode_adv()
    stop music fadeout 3
    return

label alt_day7_dv_dj_morning:
    scene black with fade3
    if alt_dv_dj_ends == 'good' or alt_dv_dj_ends == 'true':
        play ambience ambience_int_cabin_night fadein 2
        play music music_list["smooth_machine"] fadein 3
        mt "Wake up already! The whole camp is going to come running to your screams!"
        "I grimaced, throwing the squad leader's arm off my shoulder."
        scene bg int_house_of_mt_day
        show mt angry pioneer
        show unblink
        with dissolve
        me "I'm not screa..."
        "The words stuck in my throat."
        "It was sunny in the cabin."
        "Too sunny for eight in the morning."
        th "Don't tell me I overslept!"
        stop music fadeout 5
        mt "Go wash up, we're leaving in 40 minutes! Sandwiches are on the table."
        mt "I've already turned in your uniform, so check the rest of your things..."
        show mt normal pioneer with vpunch
        play music music_list["revenga"] fadein 3
        me "Fucking hell!"
        play sound sfx_bed_squeak2
        show mt normal pioneer at right with move
        "I jumped up from the bed, ignoring Olga's indignant sigh, and started pulling on my jeans as I went."
        th "What the hell?"
        th "Did the leaders serve breakfast in bed to everyone today, or was I the only one lucky enough to get a layover?"
        show mt angry pioneer with dspr
        mt "In case you haven't forgotten, you're still my pioneer, and I won't allow you to express yourself in my presence!"
        mt "Otherwise, instead of sandwiches, you'll get a visit to the principal's carpet."
        mt "Do you understand?"
        me "I got it, I got it!"
        "Shouted me, pulling on my shirt."
        me "Sorry-excuse me-I-won't-do-it-anymore!"
        "Jumping into my shoes, I rushed to the door."
        play sound sfx_open_door_1
        stop ambience fadeout 1
        scene bg ext_house_of_mt_day with dissolve
        play ambience ambience_camp_center_day fadein 2
        mt "You forgot your washing supplies!"
        play sound sfx_close_door_1
        "I managed to hear before I slammed the door."
        if alt_dv_dj_ends == 'good':
            th "How little time was left to me! How much I have to tell Alisa!"
        else:
            th "If only Alisa would forgive me..."
            th "I'll die of curiosity if I don't confirm my hunch!"
        th "And why did they put her so far away?"
        scene bg ext_houses_day with dissolve
        "Spitting on my untied shoelaces, I sprinted forward along the path, skirting the pioneers saying goodbye here and there."
    elif alt_dv_dj_ends == 'neu' or alt_dv_dj_ends == 'rej':
        play ambience ambience_int_cabin_night fadein 2
        mt "Semyon, get up!"
        "I struggled to open my eyes, squinting against the bright sunlight."
        th "Ohhhh, what a heavy head!"
        th "It's like I've been asleep for twenty-four hours..."
        mt "Forty minutes to go, so..."
        scene bg int_house_of_mt_day
        show mt normal pioneer
        with flash
        play music music_list["that_s_our_madhouse"] fadein 3
        me "Forty minutes?!"
        "I stared dumbfoundedly at the alarm clock."
        "The hands showed fifteen minutes past twelve."
        me "Then why the hell didn't you wake me up earlier?"
        show mt angry pioneer with dspr
        mt "First of all, watch your mouth! I'm not your girlfriend to make that kind of complaint."
        mt "Second of all, you could have thanked me - you've shown up after lights out yesterday and kicking my ass all morning when I tried to get you up."
        mt "I thought about throwing water on you, the old-fashioned way, but I took pity and let you sleep it off."
        show mt normal pioneer with dspr
        mt "Sandwiches are on the table. Go wash up, eat, and check all your stuff - we have to leave without being late."
        play sound sfx_close_door_1
        hide mt with dissolve
        "Olga came out, and I rushed to get dressed."
        "Instead of my uniform, my already forgotten jeans, T-shirt, and sweater were waiting for me on the chair."
        "Putting them on in this place was... strange."
        th "I didn't think they'd give me the uniform for nothing as a souvenir, did I?"
        play sound sfx_stomach_growl
        "My stomach rumbled, and I looked longingly at the sandwich bag."
        th "Breakfast would have been nice, but..."
        stop music fadeout 4
        scene black with fade
        $ alt_pause(1)
        "Taking a deep breath, I closed my eyes and counted to ten."
        scene bg int_house_of_mt_day
        show unblink
        with dissolve
        play music music_list["trapped_in_dreams"] fadein 3
        th "But I just have to talk to Alisa!"
        show cg d7_me_dahell2_7dl with dissolve
        "After a quick exploration of my surroundings for those willing to break into my cabin, I flipped open my closet and examined myself in the mirror."
        "Licked my hair, fiddled with it, and ruffled it again."
        "Tucked my T-shirt into my jeans and immediately pulled it back out."
        "Shook the invisible crumbs off my jeans and adjusted pockets."
        hide cg with dissolve
        th "Okay, I'm just afraid to go to Alisa!"
        th "When you realize you only have one chance, it's hard to take a step, because failure will burn all the bridges forever."
        th "But it's unbearable to sit idly by, because there will never be another chance!"
        play sound sfx_close_door_clubs_nextroom
        stop music fadeout 3
        stop ambience fadeout 2
        "I slammed the closet shut with a rumble and rushed outside."
        scene bg ext_house_of_dv_day with dissolve
        play ambience ambience_camp_center_day fadein 2
        "Alisa was sitting on the porch of her cabin, twirling the player in her hands."
        show dv normal sport with dissolve
        "I coughed awkwardly, making her look up."
        me "Hello?"
        show dv smile sport with dspr
        "For a second I thought I saw a look of relief on her face."
        show dv normal sport with dspr
        "She quickly pulled herself together, though."
        dv "Hi."
        dv "I thought you were avoiding me - didn't even show up for breakfast."
        me "Overslept. Who knew I'd have the honor of sleeping through lunch today?"
        show dv smile sport with dspr
        "Alisa grinned languidly, and I smiled back unabashedly."
        stop music fadeout 5
        "There was an awkward silence."
        $ alt_pause(1)
    else:
        play ambience ambience_int_cabin_night fadein 2
        mt "Semyon, get up!"
        th "Already? At least five minutes..."
        "I curled up, wrapping myself even more tightly in the blanket."
        "Olga shook my shoulder."
        mt "Have you decided to pass for fireman? It's forty minutes before we leave!"
        th "Forty minutes?"
        scene bg int_house_of_mt_day
        show mt normal pioneer
        with flash
        play music music_7dl["unfulfilled"] fadein 3
        "When I opened my eyes, I stared at the squad leader in confusion."
        me "Are we leaving this early at morning?"
        show mt smile pioneer with dspr
        mt "No. It's just someone sleeping too much!"
        "I sensed not an ounce of reproach in squad leader's joking tone."
        mt "I couldn't wake you up this morning, and just before breakfast they announced that the departure had been pushed back two hours due to a storm warning."
        mt "So march off to wash up! Your sandwiches are on the table."
        "Rubbing my eyes sleepily, I tried to figure out my next course of action."
        "What's basically left for me to do?"
        th "Kick my jaw, eat my sandwiches, slip my smartphone into my pocket, and I'm good to go."
        th "But Alisa..."
        mt "I'm going to go check on the packing."
        play sound sfx_close_door_1
        hide mt with dissolve
        "The leader walked out, leaving me alone with my torment."
        th "Of course, I should talk to Alisa. But how and about what?"
        th "Apologize for her acting like a pig and I didn't want to put up with it?"
        th "That's a lot of honor!"
        "But my brain, like a laughing matter, threw up one picture after another:"
        scene bg ext_square_day
        show dv smile pioneer2
        show prologue_dream
        with dissolve
        "Here Alisa and I are racing to the canteen, laughing and teasing each other..."
        show bg ext_houses_day
        show dv laugh pioneer2
        with dissolve
        "Here's Alisa laughing happily, causing a commotion for the whole camp on our first day of work..."
        scene cg d7_dv
        show prologue_dream
        with dissolve
        "Here we are sitting on the river bank, and her lips stretch into a smile from happy memories of camp..."
        $ persistent.sprite_time = "night"
        scene bg ext_lake_night_7dl
        show dv smile pioneer
        show prologue_dream
        with dissolve
        "And here she finds me by the lake, and says, says, says..."
        "And I move closer and closer and closer..."
        scene bg int_house_of_mt_day with flash
        $ persistent.sprite_time = "day"
        me "Enough!" with vpunch
        me "Yes, I feel good with Alisa. But at the same time, it's too lousy to continue."
        me "I'm not seventeen: in my venerable years, emotional swings make me sick."
        play sound sfx_bed_squeak2
        "I got out of bed with a sigh, got dressed, and gutted the sandwich bag."
        with fade
        th "It's only half an hour before we leave. Walk around the camp?"
        th "Oh, come on, I'm going to start thinking things again..."
        "This place was soaked in Alisa, it literally lived and breathed her."
        "Without her, the whole camp became just the setting for a fairy tale story about a forlorn man who got from winter to summer, from the gray adult routine to bright youth, from the city smog to the expanse of the forest."
        "Who went to heaven, but sat mediocrely at heaven's gate until the end of time."
        th "As it happens, I always take a bite I can't chew."
        th "Just like now - I wanted a carefree and combative girl, but forgot that there are two sides to the coin."
        th "And that behind every carefree fighting girl there are many pitfalls, whether they be psychological trauma, lack of proper empathy, or seven evil exes."
        "I got up from the table."
        th "To hell with it! Sitting around getting worked up when things are already bad is a dead end."
        th "I'd rather walk, really."
        play sound sfx_open_door_1
        scene bg ext_house_of_mt_day with dissolve
        show dv guilty sport with dissolve
        play ambience ambience_camp_center_day fadein 3
        stop music fadeout 2
        "But as soon as I stepped out the door, my heart sank into the abyss."
        "Alisa was standing on the porch, nervously scribbling the sand with the toe of her sneaker."
        me "Hello...?"
        dv "Hello."
        "I stood there like a fool, holding the door open with my hand, while she put her arm around my shoulders and stubbornly didn't look in my direction."
    return

label alt_day7_dv_dj_points:
    if alt_dv_dj_ends == 'neu' or alt_dv_dj_ends == 'rej' or alt_dv_dj_ends == 'bad':
        show dv sad sport with dissolve
        play music music_7dl["fogive_me"] fadein 3
        dv "I guess I'd like to apologize for... You know, for yesterday."
        dv "I didn't mean anything by it, just..."
        me "I know. And I don't hold it against you."
        th "I mean, I do, of course, but damn it, not when you're around me!"
        show dv sad_smile sport with dspr
        dv "Really?"
        "She looked at me with such genuine hope that I couldn't stand it and laughed in relief."
        if alt_dv_dj_ends == 'bad':
            dreamgirl "Who's too old for the swing? Who threw up in there again?"
            th "Nonsense! I'm still a big deal, I'll survive anything!"
        else:
            th "What do I see? Alisa apologizing!"
            th "And the first, too! That's a short course in raising a young lady in a week!"
        scene cg d7_dv_hugs_7dl with dissolve
        "I stepped forward and pulled the girl to me, burying my nose in the top of her head."
        me "Really, you bad head of mine!"
        scene cg d7_dv_hugs2_7dl with dissolve
        dv "Right back at you!"
        if alt_dv_dj_ends == 'bad':
            scene bg ext_house_of_mt_day
            show dv shy_smile sport
            with dissolve
        else:
            scene bg ext_house_of_dv_day
            show dv shy_smile sport
            with dissolve
        "Alisa pulled away."
        "Her face was red, but obscenely content."
        "And we were silent again, like two jerks."
        me "How badly did the squad leader hurt you?"
        "I asked cautiously, for fear of pissing Alisa off again."
        show dv smile sport with dspr
        "But she just waved it off."
        dv "Oh, what the hell, she yelled and threatened me with a letter to the school, the usual formalities."
        show dv normal sport with dspr
        "The girl's face became serious."
        dv "You're not staying here after camp. You'll go away and all that will be left is remembering you."
        "She didn't ask - she knew. And I knew it, too."
        "Didn't feel it, didn't fear it - knew exactly that my tale was coming to an end."
        if alt_dv_dj_ends == 'bad':
            th "There's no way in my life that a beautiful ending, music, credits, and they lived happily ever after."
            th "My maximum is a broken trough. And that's only if I'm lucky enough to have at least one left."
        else:
            th "Even the best movie in the world ends with a black screen and credits."
            th "It's like hearing the first chords of The Pixies..."
        me "We'll figure something out."
        "Not too reassuringly, I said"
        show dv guilty sport with dspr
        dv "I already…"
        show dv closed_eyes sport with dspr
        "Alisa sighed and closed her eyes."
        show dv normal sport with dspr
        dv "When I graduate from high school, I'm going to go to Leningrad and start my own radio station."
        dv "Maybe then you can at least hear me, if you need to. When I get it right."
        th "Somebody obviously skipped physics at school..."
        th "Well, what's physics anyway?"
        th "No radio waves can travel the distance of thirty years."
        show dv tired sport with dspr
        dv "And if it works out..."
        me "Will I be able to call on the air and say hello?"
        show dv dontlike sport with dspr
        dv "Damn you!"
        play sound sfx_punch_medium
        with vpunch
        "Alisa poked me in the side with her fist."
        dv "Sometimes I think you're ten years behind psychologically."
        me "And where did you learn such words? Did Viola lecture you while you were in the infirmary, slacking off on your exercises?"
        show dv angry sport with dspr
        dv "Oh you…"
        show dv surprise sport close with dissolve
        "Alisa took a swing, but I had already intercepted her hand in a familiar motion and pulled the girl to me."
        show dv sad sport close with dspr
        dv "Fool."
        me "You are one yourself."
        th "And yet I have a strange feeling that everything is not all right."
        th "We made up, but..."
        th "But we never understood why we were fighting."
        th "It was as if there had been no conflict at all-we fought over nothing, sat in different corners, and then we clasped our little fingers together, and all resentments were in the past."
        th "But that's not how you do it!"
        if alt_dv_dj_ends == 'bad':
            th "Well, we don't need to. Why spoil such a beautiful moment with some boring argument?"
            scene black with fade
            "I closed my eyes, running my hand gently over Alisa's back."
            th "We'll think about all the problems later. When they come."
        else:
            me "And yet, Alisa: why were you so boiling yesterday?"
            show dv guilty sport close with dspr
            dv "You know..."
            "She pressed harder against me - she probably just didn't want to make eye contact."
            dv "I began to think of the orphanage often. More often than ever."
            dv "And so much of camp reminds me of those times. About how I didn't belong to myself, and all that amateurism..."
            show dv sad_smile sport with dspr
            dv "Can we talk about this later?"
            me "Okay. That'll be my first on-air question I'll call on."
            dv "Fool."
            me "You're repeating yourself."
            scene black with fade
            "I rubbed my cheek against her hair, closing my eyes."
            th "And yet she's ready to open up to me."
            th "Not right away, not from the doorstep to give away her diaries and school notes, but one day..."
        dv "We'd better get going. The Hat will be here soon - you can hear the little ones have gone quiet."
        if alt_dv_dj_ends == 'bad':
            scene bg ext_house_of_mt_day
        else:
            scene bg ext_house_of_dv_day
        show dv normal sport
        show unblink
        with dissolve
        "I reluctantly peeled away from the girl."
        "And then a completely ridiculous, yet brilliant idea popped into my head."
        me "Alisa, can I take a picture of you?"
        show dv surprise sport with dspr
        dv "Huh?"
        me "As a memento. I'm going away, you know."
        show dv shy sport with dspr
        "The girl blushed in an instant."
        dv "I don't really like this stuff. And where do you get a camera?"
        "I took the phone out of my pocket."
        "The last percentages of the charge gave me hope that I could get at least one shot."
        show dv normal sport with dspr
        "The girl squinted at the phone in disbelief."
        show dv laugh sport with dspr
        show frame at truecenter:
            xalign 0.5 yalign 0.5 zoom 1.0
            linear 0.8 zoom 1.0 xalign 0.5 yalign 0.20
        show cam_ui at truecenter:
            xalign 0.5 yalign 0.5 zoom 1.0
            linear 0.8 zoom 1.0 xalign 0.5 yalign 0.30
        dv "And this is your camera? You forgot the lens!"
        me "Don't worry, I can manage without it."
        "And quickly, before she thinks of turning away or covering her face, flicked the camera."
        $ alt_pause(1)
        play sound sfx_7dl["snap"] fadein 0
        scene white with flash
        $ alt_pause(1)
        if alt_dv_dj_ends == 'bad':
            scene bg ext_house_of_mt_day
        else:
            scene bg ext_house_of_dv_day
        show dv smile sport
        with dissolve
        me "That's it."
        show dv normal sport with dspr
        dv "What if I blinked? Or is my face stupid in there?"
        "I grinned."
        "Whatever Alisa was, she was still a girl."
        me "Well, if you want, we can take a whole series of pictures: in the chaise lounge, in the leader's panama, with the sun on your palm..."
        show dv scared sport with dspr
        "Alisa waved her hands in fright."
        dv "No need for any series! We're going to miss the bus now as it is!"
        if alt_dv_dj_ends == 'bad':
            me "Come on then, I'll help you carry your suitcase."
        else:
            me "Then I'll take your suitcase now - and we're going."
        show dv normal sport with dspr
        "Alisa nodded."
        "I didn't hear, rather read her lips:"
        show dv smile sport with dspr
        dv "Thanks."
        stop music fadeout 3
        stop ambience fadeout 3
    elif alt_dv_dj_ends == 'good':
        scene bg ext_house_of_dv_day with dissolve
        "Already on the porch, I thought it would be a good idea to start by knocking, but I was too excited for rational action."
        me "Alisa!"
        play sound sfx_open_dooor_campus_1
        scene bg int_house_of_dv_day with dissolve
        play ambience ambience_int_cabin_day fadein 3
        "I swung the door wide open, literally falling in."
        show dv surprise sport at left with dissolve
        stop music fadeout 7
        "Alisa looked up frightened."
        "She was sitting by the bedside over her gym bag with her sandals in her hands."
        "We froze like two statues."
        dreamgirl "Great conversation starter!"
        play music music_7dl["youarenotalone"] fadein 3
        me "Alisa, I wanted to apologize for yesterday. I'm an idiot."
        show dv normal sport with dspr
        me "It's up to you what to do and for whom to do it. I've told you so much..."
        show dv guilty sport at cleft with dissolve
        dv "Come on. I'm no better."
        "She stood up, awkwardly pulling on her shirt and stubbornly looking at the floor."
        dv "None of that was true. You know, about me not needing you and all that..."
        show dv shy sport close with dissolve
        "I crossed the cabin in three steps and hugged Alisa gustily, exhaling with relief."
        scene cg d7_dv_hugs3_7dl with dissolve
        "Her hands clasped timidly behind my back."
        me "You know I'm always ready to come to you, if you just call."
        me "And it kills me when you don't talk!"
        dv "You know..."
        "Her fingertips ran smoothly down my spine, causing a frantic wave of goosebumps."
        dv "It's easier for me."
        dv "It's always been easier to keep quiet than to try to explain something."
        scene cg d7_dv_hugs4_7dl with dspr
        dv "I'm afraid that all my words won't sound the way they really are."
        dv "When I try to focus on something, to translate it into Russian, I get such nonsense that it makes me laugh."
        dv "That's what happened yesterday."
        dv "I don't know what's happening to me. I guess I've started to think about the orphanage too often, to compare..."
        "I ran my fingers through her hair."
        me "It's all in the past. And it won't happen again."
        scene bg int_house_of_dv_day
        show dv dontlike sport
        with dissolve
        dv "That's just it!"
        "Alisa pulled away, looking earnestly into my eyes."
        dv "I feel as if the Alisa Smoleva who lived there is dead."
        dv "And that makes it hard for me to understand: then who am I?"
        me "You are Alisa Dvachevskaya. Angry as the devil out of the snuffbox, lazy as a seal, and your manners are lame..."
        show dv rage sport with dspr
        dv "Hey!"
        show dv angry sport with dspr
        me "But at the same time sincere in your anger, inventive when you want to sneak out of responsibilities, and your rudeness pleases me like pictures of kittens."
        me "That's the way I love you."
        show dv shy sport with dspr
        me "I'm sick in the head, aren't I?"
        dv "Yes."
        show dv grin sport with dspr
        dv "They'll take you off the bus right away and put you in the hospital. I've already called and made arrangements."
        me "Oh, yeah?"
        show dv scared sport close with dissolve
        dv "Aah!"
        "She was scared piss and shitless of tickling, and I didn't hesitate to use it!"
        play sound sfx_bed_squeak2
        scene bg int_house_of_dv_day:
            zoom 1.4
            align(0.3,0.5)
        with dissolve
        "We collapsed on the bed with laughter, almost ripping the spring off."
        dv "You... you..."
        me "Who?"
        show dv smile sport close with dissolve
        "I stopped tickling her by locking my arms around the girl's waist and looking intently into her eyes."
        "She didn't respond."
        "She pulled me to her and kissed me, burying her fingers in my tangled hair."
        th "Not again, but once more."
        th "Screaming, scolding and violent scandals - and an equally violent reconciliation."
        th "How I've missed it..."
        th "How I long for being seventeen again, rooftops, phone calls in the middle of the night, porches, streetcar rails, guitar strumming!"
        th "And it will still happen. There's bound to be."
        "We settled on the bed, struggling to fit on a mattress that was small even for one."
        "Alisa laid her head on my chest, and I lazily ran my fingers over her cheekbone."
        dv "You know, this shift wasn't so bad."
        me "Really?"
        dv "Well, I ended up with something important..."
        th "Is she going to say it out loud?"
        show dv laugh sport close with dspr
        dv "My first serious dream."
        me "To get married?"
        show dv dontlike sport close with dspr
        dv "Hell no!"
        show dv smile sport close with dspr
        dv "I want to create my own radio. Without the boring news and weather forecasts."
        dv "Only music. Cool, new, foreign and domestic, from underground bands."
        "She rubbed her cheek affectionately against me, dreamily clasping her eyes."
        dv "Imagine that: a radio station that only plays music I like!"
        th "It's scary to even imagine..."
        show dv normal sport close with dspr
        dv "But first we'll have to break through to Leningrad somehow. I don't dream of going to Moscow, and I can't break through there either - all the places under the sun are already taken."
        dv "I'm even thinking of going to university..."
        me "Do you understand what happened, Dvachevskaya? We've got the most reliable proof of the theory of evolution!"
        stop music fadeout 3
        show dv normal sport close with dspr
        dv "Guh?"
        me "Labor made a human out of you!"
        play music2 music_list["always_ready"] fadein 3
        show dv angry sport close with dspr
        dv "You son of a bitch!"
        scene bg int_house_of_dv_day:
            zoom 1.4
            align(0.3,0.5)
        show dv angry sport close at left
        with dissolve
        "She slipped out of my arms and loomed over me menacingly."
        dv "And you're in no hurry to evolve - look at how your animal instincts work!"
        play sound sfx_punch_medium
        "The slight kick of my knee on my thigh made me blush a little." with hpunch
        me "Why shouldn't they work? There's the prettiest girl here next to me..."
        play sound sfx_open_dooor_campus_1
        show dv surprise sport close with dspr
        "The door swung open."
        scene bg int_house_of_dv_day
        show us dontlike sport at right
        with dissolve
        us "You're at it again!"
        us "There can be no peace in this cabin, only debauchery."
        show us dontlike sport close at right with dissolve
        "Ulyana made a disgruntled face as she walked past us to her bed."
        "Alisa, to my surprise, didn't run off and blush, just showed the little one her tongue."
        me "I bet you've been kissing your fiancé all morning!"
        show us grin sport close with dspr
        us "Why, are you jealous?"
        me "No, I'm more into girls..."
        play sound sfx_pat_shoulder_hard
        show dv angry sport close at left
        show us laugh sport close
        with flash
        "A pillow painfully hit my face."
        show us smile sport close with dspr
        us "Are you going to leave, or do you plan to stay here the whole shift?"
        play sound sfx_bed_squeak1
        show dv normal sport close at cleft with move
        "Alisa sighed and climbed over me and got out of bed."
        dv "Let's go before the Hat comes hurry us up. And she'll be yelling..."
        play sound sfx_bed_squeak2
        "I followed up, picking up Alisa's bag from the floor."
        show us grin sport close at cright with move
        "Ulyana immediately handed me hers."
        me "And what is this?"
        us "Carry it. You're the gentleman here!"
        me "You have a gentleman of your own."
        show us smile sport close with dspr
        us "And he's already loading on the bus."
        us "Do it, or I won't let Alisa marry you!"
        "Under such grave threats I had to give up."
        show dv tired sport close with dspr
        dv "What a great cabin we had after all..."
        show us grin sport close with dspr
        us "You'll have enough time for crying! Move it!"
        show dv normal sport close with dspr
        th "It's easy for her to move lightly!"
        "We noisily climbed out of the redhead cabin and moved toward the bus stop."
        stop music2 fadeout 3
        stop ambience fadeout 2
    else:
        stop music fadeout 3
        scene bg ext_house_of_dv_day with dissolve
        $ alt_pause(1)
        "At Alisa's cabin, I slowed down a bit."
        th "And what do I say to her?"
        th "How do you even start a conversation like that?"
        dreamgirl "Just tell her you know everything, and then she'll start laying out all the facts herself."
        th "Do you think it'll work?"
        dreamgirl "No, of course not!"
        "I didn't have any other ideas, though."
        play sound sfx_open_dooor_campus_1
        "I sighed and opened the door."
        stop ambience fadeout 1
        scene bg int_house_of_dv_day with dissolve
        play ambience ambience_int_cabin_day fadein 2
        play music music_list["trapped_in_dreams"] fadein 2
        "Alisa was squatting by her bed, putting things in her bag."
        show dv surprise sport at left with dissolve
        "She looked up at me with surprise."
        dv "Oh. You came after all..."
        show dv scared sport with vpunch
        me "Alisa, I know who you are!"
        "There was a completely idiotic silence."
        dreamgirl "..."
        dreamgirl "Are you serious?"
        me "I mean, I'm the same way. I'm from the future, too, and anyway..."
        show dv dontlike sport with dspr
        dv "What are you even saying?"
        "Alisa frowned, rising from the floor."
        dv "What future? Did you drink too much last night, or did you hit your head?"
        "I froze, flapping my mouth silently like a fish."
        th "No!"
        th "This can't be a mistake!"
        th "Sailor Moon, Tamagotchi, camp in superposition..."
        "Either she was lying so skillfully, or I turned out to be a complete idiot."
        dreamgirl "One does not rule out the other."
        me "Alisa, I'm not in the mood for silly jokes right now! I'm totally serious!"
        show dv tired sport with dspr
        "The girl looked at me sympathetically."
        dv "You couldn't think of a less idiotic reason to talk to me?"
        me "Answer me just one question: who was president before Genda?"
        show dv angry sport with dspr
        "Alisa began to boil over."
        dv "What president? Genda is the general secretary, and he's been the general secretary all my conscious life!"
        dv "I may look like a fan of funny pranks, but not this stupid!"
        dv "If you have something to say, say it, and if you don't, get out."
        th "Yup, that's the end of our talk."
        hide dv with dissolve
        th "Well, what do I do now?"
        "The phone was left on the nightstand, and I didn't have any other proof that I wasn't crazy."
        "I got ready to go after it, but something inside me just snapped."
        "I didn't feel like bringing it up anymore."
        th "I screwed up. I fucked up like I always do."
        th "Made up a convenient explanation for myself, believed it myself."
        show dv guilty sport at left with dissolve
        "I looked again at Alisa."
        "She stood hunched over, stifled, lost."
        "She was obviously hoping to hear something different from me."
        me "Fight Club."
        me "The movie where everything exploded at the end is called Fight Club."
        "Alisa didn't say anything back."
        hide dv with dissolve
        "I turned and headed for the door."
        th "After all, we'll part ways today, and I'll try to forget my shame and not go over this conversation in my head at night for the rest of my life..."
        stop music fadeout 3
        dv "Yeltsin…"
        "Alisa's quiet voice caught up with me."
        show dv guilty sport with dissolve
        me "What?"
        dv "Before Genda, Boris Nikolaevich Yeltsin was the president."
        play music music_7dl["nap_one"] fadein 2
        me "So you…"
        show dv cry2 sport with dspr
        dv "I don't know, Semyon. I don't understand!"
        "Tears were rolling down her cheeks."
        "Alisa stood staring at herself, and her face was something between despair and stupor."
        show dv cry sport with dspr
        dv "He stepped down in ninety-nine, during the New Year's Day address. We thought it was about the end of the world!"
        show dv cry sport close with dissolve
        "I rushed over to the girl and gently sat her down on the bed."
        me "And what year were you born?"
        show dv cry2 sport close with dspr
        dv "1990."
        dv "I'm not born until a year from now, you know?"
        me "And I wasn't born until this year."
        "If Alisa heard my words, she didn't comment on them."
        "A slight panic began to overtake me."
        me "How long have you been here?"
        dv "In camp?"
        me "In the past!"
        dv "I don't know. That's all..."
        show dv cry sport close with dspr
        dv "This is total nonsense!"
        dv "My head is so messed up it's about to explode!"
        "Alisa clenched her temples with her fingers."
        dv "I remember my biological parents, but I also know that I was taken into an orphanage when I wasn't even two, and they never visited me once."
        dv "I remember being given a Barbie by volunteers for my ninth birthday, but I know I celebrated my ninth birthday with my foster parents."
        dv "I remember going to camp near Leningrad..."
        show dv scared sport close with dspr
        dv "No, under St. Petersburg! At eight, but at eight I only went to the ”Sovyonok”."
        show dv shocked sport close with dspr
        dv "And you know what the strangest thing is?"
        "She looked at me with eyes full of fear."
        dv "I have the same dream every night."
        dv "In it, the girls in my room are beating me. And then the pain in my head..."
        dv "And I wake up totally convinced that I'm dead."
        "I put my hands on the girl's shoulders."
        scene cg d7_dv_hugs4_7dl with dissolve
        "She dug her nose into my neck and sobbed softly."
        me "One thing I don't understand is why you're only remembering this now?"
        dv "Some of the weirdness was when I was a kid."
        dv "No one knew about Sailor Moon or Freddy Krueger or the Ninja Turtles."
        dv "But the adults wrote it off as head trauma - I made it all up while I was in the hospital, and I believed it myself..."
        dv "I rarely remembered the orphanage - my foster parents did everything to make me a part of their family and not to bring up the past."
        dv "But when you gave me the player, the memories started coming back more and more. I heard music I'd forgotten about for nine years."
        scene bg int_house_of_dv_day
        show dv cry_smile sport close
        with dissolve
        "Alisa grinned hysterically."
        dv "Music that doesn't exist yet. Splin, Bi-2, King and Jester."
        th "It all makes sense now..."
        th "I set off a time bomb with my gift."
        th "Only how did they make Alisa forget half her life?"
        "I shuddered."
        th "And won't they do the same to me?"
        show dv sad sport close with dissolve
        "Alisa wiped away her tears."
        dv "Now how am I supposed to live with that? Who can I ask about it?"
        me "So you ended up in the hospital right after... How did you get here?"
        show dv guilty sport close with dspr
        dv "No."
        "Alisa took a deep breath."
        dv "Since you're also a bit of a..."
        show dv sad sport close with dspr
        dv "I died."
        scene black
        show prologue_dream
        with dissolve
        dv "At first it was dark, and then someone called out to me."
        show uvao_d1:
            alpha 0.2
        with dissolve
        dv "I thought it was an angel who came to take me to heaven."
        scene bg ext_sky2_7dl
        show prologue_dream
        with dissolve
        dv "And when I woke up, it was warm and sunny, and children..."
        dv "Only not in white dresses, like in the picture, but in pioneer uniforms."
        dv "I got scared and started crying and begging to go back, and they ran away."
        scene bg int_house_of_dv_day
        show dv sad_smile sport close
        with dissolve
        dv "And then... I don't remember, it got too bad, but I wanted to live so bad!"
        dv "And I thought only one thing: how much I didn't want to die!"
        show dv sad sport close with dspr
        dv "And then there was the hospital."
        dv "I was there for a long time, I don't know how long. And then they took me to my family."
        th "So Alisa didn't get on the bus that took her to who knows where. She says that there, in the future, she died."
        $ renpy.show("bg int_house_of_dv_day", what = Desat("bg int_house_of_dv_day"))
        show prologue_dream
        with dissolve
        "It felt cold inside."
        "For before I woke up in the sun-drenched cabin..."
        "I got off the bus, too."
        if herc:
            scene bg int_store_7dl
            show prologue_dream
            with dissolve
            "Went out for a shift, met a mugger and got two bullets in the forehead."
        elif loki:
            scene bg ext_winterpark_7dl
            show prologue_dream
            with dissolve
            "I came to the park, where Ksana's friends were already waiting for me, and I never left the park again."
        else:
            scene bg int_intro_liaz_7dl
            show prologue_dream
            with dissolve
            "Or rather, I didn't get off."
            "My route ended at the bottom of the icy Neva, and the last thing I remembered was water burning my lungs."
        scene bg int_house_of_dv_day
        show dv sad sport close
        with dissolve
        th "Just don't panic! Pull yourself together!"
        th "You've got a girl on the verge of a nervous breakdown on your hands, all we need is another hysterical girl!"
        me "And you didn't realize you were in another time?"
        "Alisa shook her head."
        dv "I do remember some things that didn't happen to me."
        dv "I remember my parents - biological - I remember learning the USSR anthem at school, playing 'rubber band' with the girls in the yard."
        dv "And I do not even know what is more real - the game of 'rubber band' or my bandmate, who died of glue!"
        me "I don't remember. It's like I was never here."
        me "It's like I came out of nowhere."
        stop music fadeout 3
        pause(0.5)
        hide dv with fade3
        pause(0.5)
        play music music_7dl["raindrops"] fadein 2
        "We sat in silence."
        "Alisa wasn't crying anymore - she sat quietly and didn't move, resting her head on my shoulder."
        th "It's a strange feeling-I was right, but I'm not happy about it..."
        th "Alisa is just like me, but what does that get me?"
        th "I've just turned a man's worldview upside down, and what's in it for me?"
        th "Alisa's broken psyche, which was already perfectly unhinged all these days?"
        "The only consolation was that sooner or later she would have figured it out on her own, all because of the player I handed her."
        th "And how could I not have thought of the consequences of my gift?"
        th "Even if Alisa had been an ordinary girl, she would have had to deal with the fact that she had listened to 'new music' in her seventeen years."
        th "And that would make a healthy person go crazy!"
        th "And it's kind of creepy to realize that we're technically dead somewhere in the future. It's like a parade of the living dead!"
        "More and more creepy theories were born in my head."
        th "What if this place is just the afterlife?"
        th "Everyone I've met in this camp is long dead, but they pretend to live here like normal people?"
        th "Or is this all a hallucination generated by my inflamed mind, and I'm still shuddering in death convulsions?"
        "It got frankly uncomfortable, and the dead-pale Alisa at my side didn't help my sanity one bit."
        dreamgirl "What else can you think of?"
        dreamgirl "That you're lying in a cryo-capsule with pictures being broadcast to your brain?"
        th "You know, even that doesn't seem crazy to me anymore."
        scene black with fade
        "I put my arm around Alisa, closing my eyes."
        th "I'll think about all that later. The important thing now is to help her get through this."
        th "If only I could..."
        play sound sfx_open_dooor_campus_1
        "The door swung open."
        scene bg int_house_of_dv_day
        show us grin sport at right
        show unblink
        with dissolve
        us "Aha!"
        show us normal sport with dspr
        "Ulyana opened her mouth to make some caustic joke, but immediately closed it when she saw our sorrowful faces."
        us "What, did someone die?"
        "Alisa twitched as if from a blow."
        me "No. We're saying a touching good-bye, parting for all eternity, don't you see?"
        me "Get out, don't spoil it."
        show us calml sport with dspr
        "The little one grimaced."
        us "That's a new one - all sorts of bums kicking you out of your own cabin!"
        us "You finish your farewells, the bus is here. Just waiting for us."
        show dv guilty sport close at left with dissolve
        "Alisa rose from the bed on autopilot, and I silently followed, picking up her bag from the floor."
        show us normal sport close at cright with dissolve
        "I thoughtlessly threw Ulyana's outstretched luggage on my shoulder, squeezed Alisa's cold palm with my free hand."
        me "We'll get through this. We definitely will."
        "I whispered."
        show dv sad sport close with dissolve
        "The girl nodded thoughtlessly, clutching my fingers painfully."
        show us smile sport close with dspr
        us "Move it, crying cows!"
        play sound sfx_open_dooor_campus_2
        "And I walked out of the cabin, taking Alisa with me."
        stop music fadeout 3
        stop ambience fadeout 3
    stop music fadeout 1.5
    return

label alt_day7_dv_dj_departure:
    scene bg ext_bus with dissolve
    play ambience ambience_camp_entrance_day_people fadein 2
    if alt_dv_dj_ends == 'true':
        play music music_list["memories"] fadein 2
    elif alt_dv_dj_ends == 'bad':
        play music music_7dl["tilltheend"] fadein 2
    else:
        play music music_7dl ["summer_ends_soon2"] fadein 3
    "When we got to the bus stop, the second squad bus was already pulling away."
    show mt sad panama pioneer with dissolve
    "Olga looked around nervously at her few pioneers, and only with our appearance did she nod contentedly."
    show mt angry panama pioneer with dspr
    mt "Finally! The poor lobster on the mountain is tired of whistling!"
    if alt_dv_dj_ends == 'good':
        "I tried to smile at her joke, but it came out extremely lousy."
    else:
        "I rolled my eyes - Olga is such a... leader!"
    show mt normal panama pioneer with dspr
    mt "Now that we're all here, it's time to give a tearful eulogy."
    "We gathered in a circle near her."
    if alt_dv_dj_ends == 'bad':
        hide mt
        show un normal dress at left
        with dissolve
        "Opposite me was Lena, and for a second I felt a suffocating nausea roll up to my throat."
        if loki:
            th "If she has any final revenge on me..."
        show un angry2 dress with dspr
        "The girl noticed me, too."
        "She gave me a hateful look and pretended to be completely focused on the squad leader's speech."
        hide un with dissolve
        "I lowered my eyes ashamedly."
        th "Oh, how I hope this is the last time we see each other in this life!"
    scene cg d7_pioneers_leaving with dissolve
    mt "Many of you have been in my squad more than once. Almost all of you were in my squad for the last time in your lives."
    mt "But that's no reason to get upset! There's so much more to come, you'll have no time to be bored."
    mt "However, I don't want you to forget this place. And especially this shift."
    mt "You've been the heart of this camp, you've given it so much that you can't imagine! And I hope you've learned a lot of things here that you didn't know before."
    if alt_dv_dj_ends != 'true':
        th "Drinking, smoking, and swearing?"
        th "We already knew how to do that!"
    else:
        th "Uh-huh. Some even got new mental disorders…"
    scene bg ext_bus
    show mt smile panama pioneer
    with dissolve
    mt "And also made new friends."
    mt "And I ask you not to lose each other - because the closer you are, the brighter your memories of your carefree childhood will be."
    show mt grin panama pioneer with dspr
    "Olga fell silent for a few seconds, then straightened up, giggling nervously."
    mt "Have all the tears been wiped away? Then get on the bus!"
    hide mt
    show dv normal sport close at cright
    with dissolve
    "I turned to Alisa."
    me "Shall we sit together?"
    if alt_dv_dj_ends == 'good':
        show dv smile sport close with dspr
        dv "Of course."
        dv "Dibs on the window!"
        me "On rock, paper, scissors."
        show dv grin sport close with joff_r
        dv "Well, sit there, roast in the sun!"
        me "Boo-boo-boo..."
        show dv angry sport close with dspr
        dv "What did you say?"
        me "Nothing."
        stop music fadeout 4
        me "Get on the bus, or you'll have to ride on the roof!"
        stop ambience fadeout 2
        $ alt_pause(0.9)
        scene bg int_bus_people_day with dissolve
        play music music_7dl["breath_again"] fadein 3
        "With noise and clamor we took our seats."
        "Electronik and Shurik were seated right behind the squad leader, and Lena and Zhenya sat on the left."
        "Slavya proudly sat alone, while Miku was already chirping merrily about something with a slightly frowning Ulyana."
        "Alisa and I were seated at the very end."
        "Olga gave the driver a wave of obvious relief:"
        mt "Let's go!"
        play sound_loop sfx_bus_interior_moving fadein 2
        "The gates of the camp were moving smoothly out of sight, replaced by lush thickets of grass."
        "Our squadmates were talking merrily, the engine humming, the heated metal of the bus making us pleasantly sleepy."
        "And right next to me sat my redheaded happiness."
        show dv normal sport close at cright with dissolve
        dv "Let's listen to a band..."
        me "Haven't you heard enough music during your shift, Dvachevskaya? Can't we at least talk?"
        dv "What's there to talk about? The only thing you can do on the road is tell stories, and I don't feel like it."
        me "Then I'll tell them, and you can listen to them."
        show dv angry sport close with dspr
        dv "Oh please! I'll have enough time to listen to them all."
        if alt_day6_dv_dj_quest == 4:
            show dv shy sport close with dspr
            dv "You also promised to take me to the movies..."
            me "And I will. Do I look like a liar?"
        show dv normal sport close with dspr
        "Alisa held out one earpiece to me."
        "I grimaced, but I took the earpiece, wondering what she was so eager to hear."
        "The first chords of ”Romance” began to play."
        show dv smile sport close with dspr
        th "Of course, the first song I showed her."
        th "She's so full of herself, but inside she's so..."
        th "Romantic?"
        "I looked at Alisa with apprehension."
        th "She'll beat me up for thinking that. I'd better get it over with."
        "The bus was picking up speed."
        scene cg d7_dv_epilogue_bus_7dl with dissolve
        "Alisa nestled on my shoulder and began to snooze."
        "Everyone else was quiet too, sweltering from the heat."
        th "And yet how well it ended. A wonderful reconciliation of two stroppy but madly in love with each other."
        th "And how well it goes on!"
        "I didn't know what awaited me after the bus came into town."
        th "Who will meet me and take me where?"
        th "Some parents I have - someone has handed me my own backpack."
        th "Then I won't be lost."
        th "What if it turns out we live in different cities?"
        "Finding Alisa's palm in my hand, I gently squeezed it."
        th "I can handle that."
        th "I'll run away from home, I'll hitchhike or hitchhike thousands of miles, but I won't lose what I unknowingly aspired to all my life!"
        th "Now no one will take Alisa away from me."
        scene bg int_bus_people_day with dissolve
        th "Nobody!"
        scene black with fade3
        stop music fadeout 5
        "I closed my eyes, not even trying to hide my happy smile."
        stop sound_loop fadeout 3
        "It was now possible to take a nap with a clear conscience."
        $ alt_pause(2)
        $ night_time()
        dv "Semyon!"
        "I shuddered."
        "Alisa's voice came out in absolute silence."
        "And it was very, very frightened."
        scene emptiness_7dl behind int_bus
        show int_bus_7dl
        show dv scared sport close:
            alpha 0.8
        with flash
        play music music_7dl["timetowakeup"] fadein 2
        "The bus cabin plunged into darkness."
        "The engine stopped, and all that was left was the rapid breathing of Alisa sitting next to me."
        me "What's going on?"
        show dv shocked sport close:
            alpha 0.7
        with dissolve
        dv "I don't know!"
        "She clung to my hand, but that touch was... strange."
        "As if intangible."
        show dv cry sport close:
            alpha 0.6
        with dissolve
        "And Alisa..."
        "It was like she was melting before my eyes."
        th "No..."
        me "No!"
        show dv cry sport close:
            alpha 0.5
        with dissolve
        me "Don't you dare! Don't disappear!"
        me "What do I do?!"
        dreamgirl "She's not disappearing. You're the one getting off at your stop."
        th "I can't leave! I can't leave her!"
        th "She's become all I want to live for!"
        show dv cry sport close:
            alpha 0.5
        with dissolve
        dreamgirl "So live for her."
        dreamgirl "God, Random - no matter who - will hear your prayers if you ask."
        dreamgirl "Live for the Alisa you loved."
        show black with fade
        "I squeezed my eyes shut with all my might."
        th "Please, please, please!"
        th "I want to be with her!"
        th "With the Alisa I have fallen in love with."
        th "In that world that will belong only to us. In a dimension where youth is infinite."
        "And suddenly my soul felt light and joyful."
        "Like that moment when Alisa forgave me."
        "An astonishing realization came: We will be together. Most certainly."
        hide black with fade
        "Smiling, I opened my eyes."
        "The translucent Alisa cried, and her hands passed helplessly through my palm."
        me "Don't cry, please."
        "Her mouth curled up in silent sobs."
        "My fingers slid across her disappearing cheek, wiping away the ghostly tears."
        me "Soon I will find you again."
        "She looked up at me hopefully."
        "I could hardly see her face anymore - it was like a haze."
        me "And this time I will find you sooner."
        hide dv with dissolve
        "Alisa disappeared, and I closed my eyes, sinking into a blissful darkness."
        stop music fadeout 5
        scene black with fade3
        th "I'll be sure to find you."
    elif alt_dv_dj_ends == 'true':
        show dv guilty sport close with dspr
        "The girl shook her head, looking somewhere into the void."
        dv "I want to be alone. Think it all over."
        "I put my arm around her and gave her an almost weightless kiss on the top of her head."
        stop music fadeout 3
        me "You can change your mind at any time."
        me "I will wait."
        stop ambience fadeout 2
        scene bg int_bus_people_day with dissolve
        play music music_7dl["tilltheend"] fadein 2
        "The pioneers, urged on by Olga, finally settled into their seats."
        play sound_loop sfx_bus_interior_moving fadein 2
        "Alisa whispered something to a pouting Ulyana and stared out the window with her ears covered with 'barrels.'"
        show us upset sport close at cright with dissolve
        "The little girl, who had been kicked off, flopped down next to me and crossed her arms over her chest in a hurtful way."
        us "You really blew her mind!"
        th "You should know how literally..."
        show us dontlike sport close with dspr
        us "Can you imagine, she chased me away! She needs to think!"
        "Ulyana looked at me suspiciously."
        us "You proposed to her and she's crying over her free life?"
        "The little one's clownery was beginning to annoy me."
        me "A half tone lower, please. I plan to go to sleep."
        show us upset sport close with dspr
        "The girl's face took on an extremely disappointed expression."
        us "Bo-ring!"
        scene cg d7_me_epilogue_bus_7dl:
            zoom 1.5
            align(0.1,0.2)
        with dissolve
        "I turned toward the window, and the dense thickets of grass were already floating by."
        th "I shouldn't be hurting the kid, of course, but I don't really care for her."
        th "After all, I have to think about what Alisa and I are going to do next."
        th "Judging from her story, I'd better not show that there's anything wrong with me. They'll put me in the hospital, wipe my memory like she did, and hello."
        th "And I don't want my memories of Alisa taken away from me!"
        "My inner voice laughed."
        th "What's wrong with you?"
        dreamgirl "Sorry, couldn't resist. Your sick fantasies keep getting more and more miraculous!"
        dreamgirl "You think she had her memory wiped; then how did she remember everything?"
        th "Yeah... that doesn't make sense."
        th "But what was done to her in the hospital for months?"
        th "It's unlikely her trauma was carried into this world with her-if it had worked that way, even Viola wouldn't have been able to pump me out."
        th "So her memory was suppressed. But how and why?"
        scene bg int_bus_people_night with dissolve
        "It got noticeably darker on the bus, and Ulyana, who was sitting next to me, was already falling asleep with her head on her chest."
        th "Well, whatever, I'll still have time to figure it out!"
        stop music fadeout 8
        scene black with fade
        "I pressed my forehead into the glass and closed my eyes."
        stop sound_loop fadeout 5
        "The steady hum of the engine made me drowsy."
        $ alt_pause(1)
        dreamgirl "You won't."
        th "Huh?"
        scene emptiness_7dl behind int_bus
        show int_bus_7dl
        show unblink
        with dissolve
        play music music_7dl["deadman"] fadein 2
        "An inner voice sounded in my head so distinctly that I jumped up, immediately throwing off my slumber."
        "The bus, plunged into darkness, stood still."
        "Ulyana wasn't beside me."
        th "Where has everybody gone? Are we there yet?"
        "I looked out the window, but all I saw was a black void, making it impossible to even guess where I was."
        dreamgirl "Sorry, buddy. Didn't mean to upset you prematurely, but you're not staying here."
        th "But why?"
        th "Alisa is..."
        dreamgirl "Alisa killed the person whose head she ended up in. Destroyed the consciousness and took the place of that Alisa who was born into this world."
        dreamgirl "That Alisa was seven when she confronted her guest. She could not resist the stranger, and their consciousnesses merged."
        dreamgirl "As you can see, not in favor of the body's owner."
        me "And you knew all this time?!" with vpunch
        me "But how?"
        dreamgirl "Rumors, buddy. I didn't know it was Dvachevskaya, but putting two and two together was very easy."
        dreamgirl "And, after all, it's always interesting to find out what paths your illness takes."
        "It was like I was paralyzed."
        th "So if I stay here..."
        dreamgirl "You'll kill me."
        "Bitterly grinned my inner voice... which turned out to be no voice at all."
        "And certainly not mine!"
        th "No! I can't do that!"
        th "What should I do?"
        dreamgirl "Exactly nothing. You're already leaving - right now, at this very moment."
        th "But where to?"
        dreamgirl "That's for you to decide."
        "I jumped to my feet."
        "For a moment I thought I saw something copper-red flicker behind the windshield..."
        if persistent.dv_dj_true:
            menu:
                "Charge ahead!":
                    $ alt_dv_dj_ends = 'exc'
                    stop music fadeout 1.5
                    scene bg int_bus_night with flash
                    play music music_7dl["so_be_it"] fadein 2
                    th "If I can decide where I'm going, I'm going to her!"
                    play sound sfx_bus_out
                    "I settled into the driver's seat, turned the key I'd forgotten in the lock, and accelerated as hard as I could."
                    "The bus roared off and rolled down the barely visible road, picking up speed."
                    th "I hope I'll get there in time..."
                    "The road slowly began to lose its clear outline."
                    scene bg int_bus_warp_7dl with dissolve2
                    "And then the cabin began to blur, like a rain-soaked drawing."
                    dreamgirl "Good luck to you, my friend. Wherever you're headed..."
                    stop music fadeout 5
                    scene black with fade
                    "His voice was blurred last before absolute darkness set in."
                    return
                "Must've been the wind":
                    pass
        else:
            th "Must've been the wind."
        "For Alisa, the same Alisa I love, remains in the only world to which I have no choice but to go."
        "With a heavy sigh, I sank back into my seat and closed my eyes."
        th "And it's time for me to go home."
        return
    else:
        show dv shy sport close with dspr
        "Alisa averted her eyes in embarrassment."
        dv "You know, I've already made arrangements with Ulyana. This wouldn't be nice..."
        "I hummed."
        me "Suit yourself."
        th "And here I get knocked over again. Just made up, and there you go!"
        hide dv with dissolve
        stop ambience fadeout 2
        if alt_dv_dj_ends != 'bad':
            stop ambience fadeout 2
            play music music_7dl["tilltheend"] fadein 2
        "With a wistful glance at the redheads, I followed them onto the bus."
        scene bg int_bus_people_day with dissolve
        th "And who knows if we'll ever see each other again. Doesn't she want to spend a little more time with me?"
        "I flopped down in one of the last seats, making sure I didn't let Alisa out of my sight."
        "She and Ulyana were already discussing something vigorously, and Miku, who sat in the front, turned to them, laughing happily."
        th "Fine!"
        th "I'll ride alone - the easier it will be to break up."
        "I had no more hope for staying with Alisa."
        "It was too beautiful a dream for such a thing to come true in my worthless life."
        "And Olga had already waved off the driver."
        play sound_loop sfx_bus_interior_moving fadein 2
        "We set off."
        $ night_time()
        scene bg int_bus_people_night with dissolve2
        "The grass outside the window changed to trees, and the clouds thickened: the bus was darkening rapidly."
        "I turned my head now and then, casting fleeting glances at the redhead."
        "Alisa was quiet, and even Miku was sitting still, having stopped pestering the slack-jawed tandem."
        "The stuffiness of the sun-heated bus had absolutely wiped out everyone."
        th "I wish I could plug my ears and play something unobtrusive, except I don't have a Walkman anymore."
        th "Oh well, I'll buy a new one, I won't go broke. After all, I'll listen to music a lot more often now."
        th "After all, if Alisa makes her dream come true..."
        th "Can a little independent radio station last thirty years?"
        if alt_dv_dj_ends == 'bad':
            th "Only where and in which city should I catch her wave?"
            th "On what frequency will she broadcast?"
            th "And will she?"
            "I realized that this was all just a small consolation for the forlorn sick man who is counting down his last days to the grave."
        else:
            th "It pains me to believe it. To believe and wait for such a native voice to announce:"
            dv "Hello, everyone! Here's your favorite station, and we're going to start the evening broadcast..."
        with fade3
        "My eyes began to slip."
        th "In fact, even if my story ends here and now, it wasn't all for nothing."
        th "I used to exist, but now it's like I've begun to live."
        stop music fadeout 7
        if alt_dv_dj_ends == 'bad':
            th "Only will I have something to live for when Alisa is gone?"
        else:
            th "And maybe the memories of one wonderful girl will make me go on living, instead of returning to my cozy moldy cocoon of alienation and loneliness."
        stop sound_loop fadeout 5
        scene black with fade3
        th "How I hate to go back..."
        $ alt_pause(2)
        dreamgirl "Hey!"
        scene emptiness_7dl behind int_bus
        show int_bus_7dl
        with flash
        play music music_7dl["laugh_throught_the_universe"] fadein 2
        "I opened my eyes."
        "The bus was standing still, and there wasn't even a glimmer of light outside the window."
        th "Accident?"
        th "Then why isn't anyone screaming, panicking, discussing what happened, after all?"
        "I lifted myself up and looked around."
        "It was completely empty."
        me "What the..."
        dreamgirl "You've arrived. This is the terminus."
        th "But what about..."
        if alt_dv_dj_ends == 'neu' or alt_dv_dj_ends == 'rej':
            th "What about Alisa?"
            "I knew how foolish it was to hope that she would go with me, but getting rid of that meaningless hope was beyond me."
            "And now that even she was gone, despair swept over me."
            dreamgirl "Hope never goes away, my friend. I know more about it than anyone else."
            th "What am I supposed to do?"
            dreamgirl "Wait and hope."
            th "Wait and hope..."
            scene black with fade
            "I leaned back in my chair and closed my eyes."
            "My mind was clouded with fog."
            th "Waiting for the worst, but hoping for the best."
            th "Some things will never change."
            stop music fadeout 4
            th "I've had an amazing journey, but all I'm left with is..."
            th "Waiting and hoping."
        else:
            th "But I'm not even home!"
            "In a panic, I jumped out of my chair and flitted around the cabin."
            th "What the hell is going on?"
            dreamgirl "Calm down already!"
            "I froze, suddenly listening to the tired voice of my schizophrenic self."
            th "Really, why the hysteria?"
            th "I've already done everything I can. Nothing can be changed."
            th "Time will not turn back, and I will not relive this shift."
            scene black with fade
            "Sinking into the nearest chair, I humbly closed my eyes."
            th "Nothing can be changed..."
            stop music fadeout 4
            "My head became heavy, as if a fog had filled my skull."
            th "Nothing can change..."
    stop music fadeout 1.5
    return

label alt_day7_dv_dj_bad:
    scene black with fade
    play sound sfx_7dl["single_pulse"]
    "Opening eyes in the morning is hard."
    scene bg semen_room with dissolve
    play music music_7dl["what_if"] fadein 3
    show telephone_dj_7dl with dissolve
    "So I put her picture on my lock screen so I wouldn't be tempted to close them and never open them."
    "A picture that just couldn't exist in my world."
    "A picture that I was able to convince myself I wasn't crazy."
    th "I didn't dream of my ginger girl. She exists!"
    $alt_pause(2)
    scene bg semen_room with dissolve
    "That's what I thought the day I woke up in my room with the strange feeling that I hadn't been home for a whole week."
    "The days are painfully long when you're waiting for something."
    "And when you're waiting for something unfulfilled, you just want to put yourself in hibernation mode and dust it on a shelf until a half-forgotten voice comes through the interference."
    "The voice of the girl I photographed at the last moment."
    "I took a picture, but I didn't even recognize the address where to find her."
    "The search engine either didn't understand what I was asking it, or it mocked me by displaying, time after time, 'nothing found by the query Alisa Dvachevskaya.'"
    "No social network, no phone book, no document listed a girl with that name."
    "No radio station broadcast on any frequency, where in the interludes between hits of rock music such a native voice announced:"
    play sound sfx_7dl["radioalice1"]
    $ alt_pause(7)
    play sound sfx_7dl["pinknoise"]
    "No sound irritated me as much as the white noise of empty frequencies."
    "In the rare pauses between another bottle and the empty crackle in my headphones, I would shift my gaze to the bookshelf."
    "Pulled out the dusty volumes, cracked open a random page and read, as if hoping that in those lines I would find my salvation."
    "And one day I didn't notice how the twelfth chapter was followed by the eleventh."
    "And by the first, all my questions had abruptly ceased to be pressing."
    scene bg int_semen_kitchen_7dl:
        zoom 1.4
        align (0.2,0.5)
    with fade3
    "Pouring my tenth shot into myself, I slid down the wall, grabbing my temple with my free hand and pushing the bottle off the table."
    "The sound of wheels clattering in my head."
    play ambience ambience_7dl["train"] fadein 2
    "And I realized it was always there."
    "The only place where it didn't exist was the camp."
    scene bg ext_entrance_night_clear_7dl with fade2
    scene bg int_semen_kitchen_7dl:
        zoom 1.4
        align (0.2,0.5)
    with vpunch
    stop ambience fadeout 1
    th "What an idiot I am!" with vpunch
    th "This was it, the station where I had to get off the train. But I couldn't."
    th "I was afraid to imagine life outside the stuffy carriage."
    th "Like the last coward I pretended not to notice that the train was hurtling at breakneck speed into the cliff!"
    stop music fadeout 2
    th "Now all I have to do is drive until I die... if I don't die of boredom along the way."
    $alt_pause(1)
    scene black with dissolve
    "Staggering, I got up from the floor and wandered to the bedroom, leaving an open book on the kitchen floor with its pages curled up from the alcohol."
    scene semen_room with fade2
    play music music_7dl["prologue_2"] fadein 2
    "From then on, the pounding of the wheels haunted me ceaselessly."
    "I fell asleep and woke up to it, and it didn't seem to leave me alone even in my sleep."
    play ambience ambience_7dl["train"] fadein 2
    "It made it hard to concentrate on anything, and it cost me a titanic effort not to grab my ears and scream when I went outside the house."
    "Because outside they were pounding much more distinctly."
    th "It felt like I wasn't even in the compartment."
    th "I'm a forgotten package in a freight car that was once impulsively ordered during a sale, and the second I forgot about it."
    scene bg int_train_7dl with fade2
    scene bg int_semen_kitchen_7dl:
        zoom 1.4
        align (0.2,0.5)
    with fade
    th "And I keep rolling back and forth, lying in a dark corner, and no living person will remember me until we get to the cliff."
    scene bg int_wagon_sunset_7dl with fade
    stop ambience fadeout 2
    scene bg int_semen_kitchen_7dl:
        zoom 1.4
        align (0.2,0.5)
    with fade2
    "The vestibule... or rather, the kitchen was almost indistinguishable behind a puff of smoke."
    "I pulled the crumpled pack to me, flipped the lid off the third time, and angrily cursed: I was out."
    "And the wheels kept pounding and pounding and pounding..."
    play ambience ambience_7dl["train"] fadein 2
    "Struggling to get through someone's suitcases - or my shoes? - I walked out the door."
    scene bg int_wagon_day_7dl with fade
    th "Day after day, from carriage to carriage. When is this damn train going to stop?"
    th "And will I meet her at the station, waiting for me with open arms?"
    th "After all, they have a life there, a real life. And me?"
    th "I'm just one of the faceless passengers who prefer not to think about what awaits them at the end of their journey."
    th "Unless I really want to get off..."
    stop ambience fadeout 2
    scene bg ext_city_night2_7dl with dissolve
    scene bg ext_city_night_7dl with fade
    stop music fadeout 5
    "My head spun, and I stopped, clinging to the cast-iron railing of the bridge."
    "My unseeing gaze rested on the black water."
    play sound sfx_7dl["pinksine"] fadein 1
    "Consciousness became crystal clear, and in the same second the pounding of the wheels disappeared."
    "I stood hovering down, and all I could hear was absolute silence."
    th "The train stopped."
    th "That means I'm getting off. I won't settle for less this time!"
    "That was my last thought before I was stunned by a splash of water."
    $ alt_pause(1)
    play sound sfx_shoulder_dive_water
    scene anim_underwater
    show blackout_exh
    with fade3
    "And then came the cold."
    scene black with dissolve2
    "And an unexpected calm."
    $ alt_pause(2)
    scene bg int_ward_day_kns with dissolve
    "When I woke up, there was absolute silence all around me."
    th "I did it! I did it! I..."
    "But it wasn't a camp. It wasn't even a train station."
    "I was lying in a hospital bed, surrounded by some strangers."
    me "Where am I?"
    "I asked the quite obvious question, but I couldn't hear my own voice."
    "But all the people turned around, as if they had clearly heard me speak."
    "One of them opened his mouth as if to say something, the other frowned, looking at the door."
    me "What the..."
    "Once again I opened my mouth - and once again I felt my ligaments tense, but there was no sound."
    "One of my roommates rushed toward me, moving his lips silently."
    "The door behind the other roommate closed abruptly, but completely silently."
    "And slowly a sticky, cold realization began to creep over me that something irreparable had happened."
    $ alt_pause(1)
    $ set_mode_nvl()
    scene bg int_opened_door_7dl with dissolve
    "The doctor talked to me for a long time. Or rather, he didn't talk - he wrote in a large notebook."
    "And from his explanations, written in his scrawling handwriting, I understood absolutely nothing: bilateral pneumonia, herpesvirus infection, hearing loss..."
    me "Will I be able to hear again?"
    "The doctor grimaced - my voice must have sounded too loud for him - and nodded, scribbling in his notebook."
    "There was a chance of restoring my hearing, but no one could give me any guarantees."
    "They gave me a whole list of tests and kept me in the hospital for a few more days before they let me go home."
    nvl clear
    scene bg int_hospital_hall_day_7dl with dissolve
    "I was in and out of hospitals for a month."
    "And the results of the examinations left me less and less hopeful."
    "Vestibulocochlear nerve damage on both sides. Irreversible."
    "Fourth degree hearing loss, aka profound hearing loss."
    "An offer of disability and the imminent prospect of job loss."
    "In my early thirties, I found myself a helpless cripple on the outskirts of life."
    $ alt_pause(1)
    $ set_mode_adv()
    scene bg int_semen_kitchen_7dl:
        zoom 1.4
        align (0.2,0.5)
    with fade3
    "This is the evening I've been spending in the kitchen."
    "The lights are off, and there's an old radio on the table - because the phone drowned in the Neva that ill-fated night when the wheels stopped pounding forever."
    th "And this is life? Real life outside the iron wagon?"
    if loki:
        "I used to think I lost everything when I couldn't play."
        "Now they've taken away my ability to teach others to play."
        "I wasn't Beethoven to go on in spite of my deafness."
    elif herc:
        "I had to leave work."
        "Zina said something in her tearful good-bye, and then she got up and started looking for a piece of paper, but I hurried to get out while she wasn't looking."
        "I didn't want another reminder of how pathetic I had become."
    else:
        "There was a lot less work to do."
        "Freelancing allowed me to get some crumbs on top of my disability pension, but without the ability to talk to a client outside of messenger, some projects simply could not be delivered on time."
        "And the lack of sound notifications was a major hindrance to my hard work."
    th "There was no station outside the window. Only a hard and dry mound of earth, which would be crushed to death by any madman who ventured to get off the train early."
    "And there was no white noise."
    "The radio was on all day and night, and I turned the knob aimlessly, hoping..."
    th "Hoping for what?"
    th "That the radio waves would start broadcasting right into my head?"
    "It's hard to live when the killer of your last hope is frowning at you from the mirror."
    "It's hard to live in absolute silence, but terribly afraid to hear the interference of an empty frequency again."
    th "And now I have no choice but to fly further into the cliff."
    th "For I shall never know when the wheels of the 'Yellow Arrow' will stop beating."
    $ sdl_persistent_inc("dv_dj_bad")
    show acm_logo_dv_dj_bad with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    pause(1)
    return

label alt_day7_dv_dj_neu:
    scene bg bus_stop with dissolve
    play sound_loop sfx_street_traffic_outside fadein 1
    "Another day at work is over, and I rush to the bus stop, passing crowds of frozen, angry and hungry people rushing to take refuge in their bright concrete boxes and pretend, at least for a few hours, that they live rather than exist."
    "For henceforth I am one of those who give them those few hours of life in the bleak gloom of the stuffy concrete of the big city completely gratuitously."
    "But, of course, that's not how it started."
    stop sound_loop fadeout 1
    $ alt_pause(1)
    play music music_7dl["nowyouseeme"] fadein 2
    scene prolog_4 with dissolve
    "I woke up and stared doomfully at the ceiling of my apartment."
    "The dream was a dream - what a surprise!"
    "But could a dream be so real?"
    "Could I have felt so real in the dream that I hadn't felt in years?"
    scene bg semen_room with dissolve
    "With trembling hands, I grabbed my smartphone from the nightstand and ordered myself not to get my hopes up."
    "I squeezed my eyes shut and clicked the gallery icon from memory."
    "And almost fell off the bed, either from shock or from the rush of such forgotten happiness."
    "Confused, bewildered, slightly frightened, and about to explode with anger-just the way Alisa looked at me from a picture that just couldn't be part of my reality."
    "But she was! And she was real!"
    "I stuck my head under an icy shower, reloaded my phone three times, and fearfully reopened the gallery, but the image hadn't changed a pixel."
    "And that could only mean one thing: it really did happen, and it happened to me."
    stop music fadeout 3
    $ alt_pause(1.8)
    $ set_mode_nvl()
    scene bg ext_city_night_7dl with dissolve
    play music music_7dl["prologue_1"] fadein 1
    "So I began a search."
    "An endlessly long search - I've combed through all the archives, all the reference books, all the forums, but I haven't found any information about the radio station that a young girl named Alisa created in the early nineties."
    th "Didn't keep her promise?"
    th "Or just couldn't find the strength to fight when faced with the difficulties of the organizational side of the issue?"
    nvl clear
    "My mind refused to accept these thoughts."
    "So I grasped the only clues and plunged into the archives with renewed vigor."
    "And the more I searched for information about Pioneer Camp Sovyonok and a certain Genda, the more questions arose."
    "After all, there had never been any camp with that name, nor had there ever been a Party official with such an exotic surname."
    nvl clear
    scene bg semen_room_window with dissolve
    "This only led to two versions."
    "The first was that I went crazy and mistook a fairy tale dream for events that really happened to me."
    "That version was collapsing on the picture I had thrown onto my computer and poured onto the cloud, so it would definitely not disappear anywhere."
    "Version two was much sadder, but it explained all the oddities at once."
    th "Alisa was from another world."
    th "And I was unknowingly in that world for a week, only to torment myself for the rest of my life with the fact that I couldn't go back."
    nvl clear
    "My hands were almost down."
    "I ate without tasting, slept without dreaming, went to work without noticing how the weeks passed."
    "For while my brief search and investigation were going on, the hope of finding Alisa again still lingered in me."
    "And now she was gone."
    "I lived for that hope, and when it was gone, all I had to do was lie on the floor and die quietly."
    nvl clear
    scene bg semen_room with fade3
    "But one night I literally forced myself to close all the tabs of information garbage I crammed into myself every day to pass the time to sleep and muffle unsolicited heavy thoughts, and there was only one site left in front of me."
    "And I sat at the monitor until dawn making a playlist."
    "The perfect playlist that Alisa would love."
    $ alt_pause(0.5)
    $ set_mode_adv()
    "At the last moment, before I crawled out from behind the computer and collapsed into bed, I clicked on the privacy settings button."
    "I hesitated for a few seconds, but still chose the 'for everyone' option, then closed the browser with a clear mind."
    th "Even if this playlist is never heard by Alisa, someone else like her in spirit will one day find something here for themselves at just the right time."
    stop music fadeout 5.5
    "This must be what she wanted when she lit up with the idea of starting her own radio station, right?"
    $ alt_pause(1)
    $ set_mode_nvl()
    scene bg int_semen_room_half_clean_7dl with fade3
    play music music_7dl["someone_like_you_guitar"] fadein 2
    "And two days later I found myself again in the middle of the night at the computer, making a new playlist."
    th "This is the music she would listen to when despair was overwhelming her."
    th "It's the kind of music she'd party to at an apartment party, pouring port into herself and dancing like it was the last time."
    th "And this... to this she would dream. But she'd never admit, even at gunpoint, that she listened to that!"
    nvl clear
    "I composed more and more situations in which Alisa might need music, and created, created, created..."
    "And my playlists were listened to."
    "Added to favorites and raced to repeat first dozens and then hundreds of listeners."
    "When the number of listens on the very first playlist passed ten thousand, I knew I had to move on."
    "I ordered a fancy microphone and started writing the lyrics for my first radio show, while simultaneously riveting a simple website for my future online radio station."
    nvl clear
    "The only question left was what to name her brainchild?"
    th "What would she call it?"
    "All sassy and defiant nonsense looked vulgar and inappropriate."
    "Alisa wouldn't pull any nonsense, because when it came to something she really liked, she was extremely serious."
    th "Remember at least the first concert she hadn't yet refused to perform at..."
    scene cg d4_dv_concert_7dl
    show prologue_dream
    with dissolve2
    $ alt_pause(2)
    scene bg int_semen_room_half_clean_7dl with dissolve
    "And I remembered."
    "I played that same song and repeated it for a week, trying to figure out why Alisa liked it so much."
    "And on the eighth day, Radio 'Night', whose short broadcasts lasted only four hours a day, from eight until midnight, appeared on the vast web."
    nvl clear
    if not herc:
        "Every day went the same way."
        "At work, I'd go over my upcoming short monologue in my head, which took up at most twenty minutes of the entire broadcast."
        "But it wasn't a big deal - the only chitchat I did was for formality's sake, usually giving dry reviews of music novelties."
        "It was much more my head about the opening song on the air."
        stop music fadeout 4
        "After all, that song was always just for her."
    else:
        scene bg int_store_7dl with dissolve
        "The days when I went to work flew by almost unnoticed."
        "Sitting in my corner, I gathered material for future broadcasts, so that on my day off I could quietly devote the evening to my life's new business."
        "And the business wasn't so much radio as it was the agonizing choice of the opening song on the air."
        "A song I put on just for her."
        stop music fadeout 4
    $ alt_pause(0.5)
    $ set_mode_adv()
    scene bg int_semen_room_half_clean_7dl with fade3
    play sound_loop sfx_7dl["pk_venti"] fadein 1
    me "Good evening, dear listeners."
    "Quietly I said into the microphone."
    $ volume(0.1,"sound")
    me "This is 'Night' Station, and today the band Amatory is playing for Alisa."
    play sound sfx_7dl["wakeup"]
    "I pressed 'play,' but in my headphones remained the same silence with a quiet and almost elusive crackle."
    th "What the..."
    "In a panic, I rushed to check the router without even bothering to take my headphones off."
    $ volume(1.0, "sound")
    play sound sfx_7dl["radiotune"]
    "And as I leaned under the table, the interference grew stronger."
    "And through them I heard her."
    th "That can't be!"
    "My breathing stopped involuntarily, and even my heart seemed to stop beating."
    "In the absolute silence, interrupted only by the crackle of interference, Alisa's quiet voice sounded:"
    dv "...and we won't let you get bored tonight!"
    dv "But before that, a song for the man I'm waiting for and missing very much."
    dv "And I really hope we meet again."
    th "I'm not crazy, am I?"
    "The interruptions subsided as abruptly as they began, but I still hesitated to breathe."
    play sound sfx_bodyfall_1
    "My head spun, and I collapsed on the floor." with flash_red
    stop sound_loop fadeout 1
    play music music_7dl["breathe_with_me"] fadein 2
    th "It was her! It really was her!"
    "The song I'd chosen for this evening for Alisa was playing in my headphones as if nothing had happened."
    "For Alisa, who waited and missed and hoped somewhere out there, in a world where I never existed."
    "I rolled over onto my back and laughed hysterically into the ceiling."
    th "I knew it! I knew she would keep her word!"
    "It wasn't all for nothing."
    "This camp, this meeting, these endless playlists and sleepless nights, I came all this way for a reason."
    th "The universe itself is giving me a sign to keep going."
    th "For if her voice has traveled through hundreds of thousands of worlds, then one day she herself will..."
    "It was too good to be true."
    "But now no one could take that hope away from me anymore!"
    scene black
    show blink
    with dissolve
    "Closing my eyes, I whispered the lines following the vocalist:"
    scene cg d4_dv_concert_7dl
    show prologue_dream
    with dissolve
    me "Breathe with me one more day"
    me "I'll be counting the hours"
    me "Press your hand against my chest..."
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("dv_dj_neu")
    show acm_logo_dv_dj_neu with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    pause(1)
    return

label alt_day7_dv_dj_rej:
    play music music_7dl["ask_you_out"] fadein 3
    scene bg ext_khruschevka_winter_7dl with fade2
    "With my cold fingers I put up flyers on the porches."
    "We have to get there before the residents wake up and go to work, or we'll have to listen to threats from those who got up on the wrong side of the tracks again."
    voice "Shat all over the walls with their posters, you damn hippies!"
    "A disgruntled man in a faded coat yells after me, and I realize it's time to skedaddle."
    "Home to a warm bed."
    "Cuddle up with her, listen to that sweet, 'Do you want to freeze me?' grunt. - and bury my nose in the pillow that smells of her hair."
    "And on the streets will be left to greet the dawn with multicolored advertisements:"
    th "La Vida Loca. Music that's not yet in your livers. 103.6 FM."
    "The idea is hers, the design is mine."
    $ alt_pause(0.5)
    $ set_mode_nvl()
    scene bg ext_city_night2_7dl with dissolve
    "Alisa and I met a year ago under very strange circumstances."
    "My friends from Mukha invited me to their first concert at the poorly run-down Technical Institute House, and I had no reason to refuse."
    "I had to go to this hick town with the anticipation of a wasted evening."
    nvl clear
    "But the concert was a success!"
    "The crowd was packed, the lights were suspiciously professional, the sound was fine, and the underground bar had a gym bag full of cash before the encore."
    "Even though they were copying Depeche Mode, the local crowd was unsophisticated and happily sang along to their biggest hit, 'City of Neon Lights'."
    "Not only was the evening not wasted, it was great! And I really didn't want to end it..."
    nvl clear
    $ meet('sh', 'Sasha')
    $ meet('voice', 'Igor')
    $ persistent.sprite_time = "day"
    scene bg int_bar_7dl with dissolve
    sh "You've got to be kidding me. Soon you'll be packing stadiums at this rate."
    "I managed to catch Igor in a crowd of tipsy groupies and drag him to the sidelines."
    "At the after-party, there was hardly an entire appreciative audience."
    "My comrade was already quite drunk and quite chatty, elated by his first sense of fame."
    voice "That's all our ginger treasure. Without Aliska we wouldn't even have ten people here!"
    sh "Your girl?"
    voice "If you're wondering for yourself..."
    nvl clear
    "Igor smirked, making me blush."
    voice "She's as free as the wind. Come on, I'll introduce you to her!"
    "Not listening to my objections, my buddy dragged me toward the stage, where almost the rest of the band was gathered."
    show dv laugh casual with dissolve
    nvl clear
    "And with them a girl."
    "Bright, lively, energetic."
    "They make you turn around when you walk past them on the street."
    "They make you feel particularly insignificant."
    "But for some reason she spoke to me."
    $ alt_pause(1)
    $ set_mode_adv()
    scene bg ext_roof_city_night_7dl with dissolve2
    "We stayed up all night talking about everything, and when almost everyone had left, we climbed the fire escape to the roof with the last surviving bottle of portwine."
    "Alisa's laughter made my chest clench."
    $ persistent.sprite_time = "night"
    "I madly to stroke her copper hair, but the mere thought of touching her made me tremble with fear."
    show dv smile casual with dissolve
    dv "It's time for bed."
    "She puffed, taking one last puff."
    sh "You can crash at my place-it's not far."
    "It came out against my will, and I instantly wanted to cover my face with my hands and run away."
    "To pretend those words never happened."
    dv "Let's go then. It's not that late, we'll catch a ride."
    "And I was almost sick with excitement at the thought of having to sleep in the same bed."
    $ alt_pause(1)
    $ set_mode_nvl()
    scene bg int_sam_room_7dl with dissolve
    "And just a week later, I had all of Alisa's stuff in my apartment - she had finally had a fight with her neighbors and was looking for a place to crash for a while."
    stop music fadeout 3
    "Needless to say, she was invited to stay as long as she wished?"
    nvl clear
    pause(1)
    play music music_7dl["uneven_me2"] fadein 2
    scene bg ext_city_night_7dl with dissolve
    "Alisa was a fickle roommate - she would travel to Moscow with her guys, then organize concerts in the region, then just disappear into apartment parties, occasionally offering to keep me company."
    "And every time we went out together, mysteriously curious looks were thrown at us."
    "But Alisa was also happy to intrigue, hugging me from behind and burying her nose in my neck."
    "Or laying her head on my lap, taking up the whole shabby couch and letting her short hair run endlessly over it."
    "And every time she'd come back from her travels, she'd give me a long hug in the hallway, giggling at the way I breathed down her collarbones."
    "And then we'd sit in the kitchen until the wee hours of the morning - she always brought a lot of stories with her."
    "And for those nights I always had her most favorite Indian tea and fresh puffs."
    nvl clear
    stop music fadeout 6
    "But my happiness could not last."
    "That evening Alisa returned unusually early."
    "In her bag, the bottles jingled."
    $ alt_pause(0.9)
    $ set_mode_adv()
    play music music_7dl["hll"] fadein 3
    scene bg int_semen_kitchen_7dl:
        zoom 1.5
        align(0.2,0.5)
    with dissolve
    show dv laugh casual with dissolve
    "We sat down in the kitchen, sipping port."
    "My neighbor looked worried."
    "And in the background, through the crackle of a cheap tape recorder, Letov was howling."
    show dv smile casual with dspr
    dv "I plan to leave organizational activities. I'm sick of it all."
    "The cigarette fell helplessly from my fingers onto the sticky cloth."
    sh "But... but you said it was your life's work!"
    dv "I was lying."
    "Alisa sipped from her glass."
    dv "Actually, I've been dreaming about something else all along."
    dv "A few years ago I broke up with the man I love. He left due to circumstances beyond our control."
    dv "But I promised him and myself that one day I would start a radio station so he could find me if he wanted to."
    "{i}Sparrow, fluttering, fiery, hoarse{\i}"
    "{i}An unbridled flock is crying out in me{\i}"
    show dv laugh casual with dspr
    dv "And a few days ago I got an offer to be a DJ, can you imagine?"
    "And what was I supposed to say to her?"
    "That it really hurt me that she didn't love me?"
    "{i}Sparrow, fluttering, fiery, hoarse{\i}"
    "{i}An unbridled flock is crying out in me{\i}"
    "But all I had to do was smile back."
    "It was impossible to be angry with Alisa when her eyes lit up like that."
    "In fact, she never promised me anything."
    sh "But being a DJ isn't the same as having your own radio station. You're going to be working for somebody..."
    show dv smile casual with dspr
    "Alisa only brushed it off."
    dv "Andrei said that everything is completely under my control."
    dv "He only has the organization and documents behind him, and I will be the face... or rather, the voice of his radio station."
    dv "And he has complete confidence in my taste in music!"
    dv "He even let me choose my own name."
    sh "And what did you choose?"
    show dv normal casual with dspr
    "Alisa's eyes studied my face carefully."
    dv "I wanted to ask for your help. I can't think of anything myself, and you know me better than anyone else."
    sh "La Vida Loca - crazy life. That's your style."
    show dv laugh casual with dspr
    "She laughed for a long time, bending over the table and driving me into the red."
    show dv smile casual with dspr
    dv "Why, that sounds good! So be it."
    hide dv with dissolve
    "Alisa fell silent, dreamily closing her eyes, and only the hoarse voice of Igor Fyodorovich remained with me."
    stop music fadeout 4
    "And in me a sparrow-like, pitch-black, fiery, hoarse, frantic flock of sparrows cried out."
    $ meet('sh', 'Shurik')
    $ meet('voice', 'Voice')
    $ alt_pause(1)
    $ set_mode_nvl()
    play music music_7dl["piknik"] fadein 3
    scene bg int_dv_radioroom_day_7dl with dissolve
    "Alisa needed an assistant on the radio."
    "Someone had to serve her tapes, keep an eye on the equipment, and make her favorite Indian tea."
    "And I didn't have to be persuaded to quit my job to do it."
    "Alisa breathed life into the uncomfortable radio room and then into the whole town."
    "It seemed like all there was around was talk of a new radio station."
    "And she managed to infect me with it."
    nvl clear
    "My life already belonged to her all these months, but now..."
    "Now we were living the same thing, and I sometimes even managed to forget that she'd started it all for a completely different person."
    "I wanted as many people as possible to admire her as much as I did."
    "So every morning colorful flyers would appear all over town, and people would roll their eyes before I could open my mouth in their presence - they knew it was going to be about radio."
    nvl clear
    "And about her."
    "So beautiful."
    "So inspiring."
    "So talented."
    "One that will never be mine."
    stop music fadeout 4
    $ alt_pause(1)
    $ set_mode_adv()
    scene bg int_dv_radioroom_night_7dl
    $ persistent.sprite_time = "day"
    show dv normal casual
    with fade3
    play ambience ambience_medstation_inside_day fadein 3
    dv "Almost eight. Stop."
    "Every day at eight o'clock sharp, she would play a song for him."
    "For a man who never thought to reappear in her life, but who had no intention of disappearing from her heart."
    "The music in our headphones fell silent. Alisa pulled the microphone toward her."
    show dv smile casual with dissolve
    dv "Still awake? La Vida Loca Station is here, and we won't let you get bored tonight!"
    dv "But before that, a song for someone I'm waiting for and missing very much."
    dv "And I really hope we meet again."
    show dv surprise casual with dspr
    play sound sfx_7dl["wakeup"]
    "And as soon as she gave me the go-ahead to start the song, a high-pitched squeak hit my ears."
    dv "What the..."
    "The squeak stopped as abruptly as it started."
    play sound sfx_7dl["radiotune"]
    "It was replaced by a noise - a strange, unlike a blank frequency."
    "Foreign."
    "But I couldn't reach the equipment: I was stopped by a muffled voice coming through my headphones:"
    dy "Good evening, dear listeners."
    dy "This is Night Station, and tonight the band Amatory is playing for Alisa."
    "The voice disappeared, replaced by a faint crackling sound."
    "The heart went down."
    "And Alisa..."
    stop ambience fadeout 4
    play music music_7dl["everlasting_spring"] fadein 2
    show dv laugh casual close with dissolve
    "And Alisa laughed, ripped the headphones off her head, and threw her arms around me, seriously threatening to break my ribs."
    dv "I knew it! I knew he wouldn't sit idly by!"
    dv "Well, Semyon, you bastard!"
    show dv smile casual with dissolve
    "She let me go, wiping her eyes with tears."
    dv "You heard that, didn't you? You heard it too?"
    "I nodded back confusedly."
    "Of course I heard it."
    "I heard that man rudely and as if nothing had happened, burst into the life of the girl I loved more than anyone else in the world."
    dv "He'll come back. He'll definitely come back."
    "Alisa whispered, smiling stupidly."
    "But this time I didn't squeeze a smile out of myself in return."
    th "He'll come back and take her away from me."
    hide dv with dissolve
    "I started a song."
    "A song that was always mine and only for her and about her."
    "The song she decided to give to him."
    th "And I'll be alone again. With the dull howls of Igor Fyodorovich."
    th "To spend my eternal spring in solitary confinement."
    $ meet('sh', 'Shurik')
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("dv_dj_rej")
    show acm_logo_dv_dj_rej with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    pause(1)
    return

label alt_day7_dv_dj_good:
    scene bg ext_camp_entrance_day
    show prologue_dream
    with dissolve
    play music music_7dl["thanks"] fadein 3
    $ alt_pause(1)
    $ set_mode_nvl()
    "I dreamt something strange."
    "Like I was almost an old man and I went to summer camp for some reason."
    "Pioneer, like in Soviet movies."
    show dv smile pioneer2 behind prologue_dream with dissolve
    "There was also a redheaded girl."
    show dv smile pioneer2 far behind prologue_dream with dissolve
    "And how I wanted to stay with her there, in that strange dream!"
    scene black with dissolve
    $ set_mode_adv()
    "But reality was, as always, too cruel."
    voice "You've been getting calls from your dolts for the last hour!"
    voice "Wake up, or next time I'll tell them you moved into an orphanage!"
    scene bg int_semen_room_alt_7dl
    show unblink
    with dissolve
    me "Yeah, good morning, mom."
    "I got out from under the covers, rubbed my eyes, and stumbled into the shower."
    "The guys will be pissed if I blow off rehearsal again."
    $ alt_pause(1)
    $ meet('ml','Goshan')
    $ meet('ml2','Ilyukha')
    $ meet('voice','Vasyan')
    scene bg int_warehouse2_day_7dl with dissolve
    ml "We thought you were dead after last night."
    "Goshan clapped me on the shoulder as I stumbled into the garage."
    "I grimaced: our vocalist sometimes forgot that he'd quit boxing three years ago."
    "As Vasyan the drummer behind him, a flimsy bespectacled guy with the face of a nerd from first grade, used to say behind his back, Goshan had once been told that the throat was also a muscle, and so he ended up in our humble vocal and instrumental ensemble."
    ml2 "That's enough talk! Syomych, we've got some news that'll blow your mind."
    "The guitarist, frontman, and our last hope to become popular at least among underage girls - in the world Ilyukha - has stepped forward."
    ml2 "My uncle let us play at his bar this weekend. And we don't have shit ready!"
    ml2 "Vasil only learned to hit the plates the day before yesterday, Goshan can't even sing three lines without paper, you're sleeping like an animal!"
    th "I'm the only smart one standing pretty in a white coat."
    "In my mind I finished."
    ml2 "Bass in your teeth and let's go!"
    ml2 "We have to show on Friday that at least we know how to hold our instruments the right way!"
    scene bg int_warehouse2_day_7dl with fade3
    th "It's been six months since we've been trying to be rock stars, but there's no success, no money, no fame."
    th "I should have listened to my mother and gone to college. Now I have to run away from the army because of those three jerks!"
    th "However, soon she'll stop feeding me on principle, and then there's a chance to get out of the army on underweight..."
    "Ilyukha waved his hand, announcing a smoke break."
    ml2 "Well, what can I say: we're not playing well."
    ml2 "The only thing we can count on is beautiful and tipsy ladies. Preferably deaf ones."
    "I reached for my cigarette, and that redheaded girl from the dream came to mind again."
    th "What was her name?"
    stop music fadeout 4
    th "And why can't she ever get out of my head?"
    $ alt_pause(1)
    scene cg epilogue_dv_2 with fade3
    play music music_7dl["hurricane"] fadein 2
    "The concert went... well, thanks for it at least going."
    "There weren't many listeners, and it was hard to gauge their reactions: I was too afraid of screwing up to watch the 'fans' too."
    "They didn't pelt me with tomatoes, thank you for that."
    scene bg int_bar_7dl with dissolve
    th "If that redhead had been here, I would have burned with shame."
    "I gratefully took the beer Vasya had handed me and brushed the wet bangs off my forehead."
    "And then I almost dropped the bottle on the concrete floor of the basement bar."
    show dv normal modern far with dissolve
    "Three meters away from me stood a girl who came straight out of my dream."
    "Redheaded, with two idiotic ponytails, tall, thin..."
    th "Such coincidences just can't happen!"
    "Shoving aside the indignant Vasya, I headed toward her."
    hide dv with moveoutright
    "And she was on her way out!"
    ml2 "What's the hurry, beautiful?"
    show dv surprise modern far at right with dissolve
    "Ilyukha beat me to it, once again making me want to punch him in his pretty face."
    "He blocked the redhead's path, smiling charmingly."
    show dv normal modern far with dspr
    dv "Home. It's pretty damp here."
    ml2 "You just haven't had enough to drink. But we're fun guys!"
    show dv angry modern far with dspr
    "The girl rushed to the side to go around him, but turned around and intercepted my gaze."
    show dv normal modern far with dspr
    "And her angry, pissed-off face became... thoughtful in a second?"
    show dv smile modern far with dspr
    dv "Alright, clowns. Make it fun for the lady!"
    show dv smile modern close with dissolve
    "She turned sharply, flew toward me in three steps, snatched the open bottle from my hands, and drained it in a volley."
    show dv grin modern close with dspr
    dv "And get me drunk, since you're boring otherwise."
    "The girl looked defiantly into my eyes, and her thin lips curled in a sneer."
    dv "I'm Alisa, by the way."
    me "I know."
    show dv normal modern close with dspr
    th "That's right! That was her name in my dream!"
    th "Now I know for sure that's no coincidence!"
    show dv grin modern close with dspr
    "Alisa looked at me with interest."
    dv "Don't tell me you had gypsies in your family."
    th "And she's exactly the same... obnoxious!"
    stop music fadeout 3.5
    $ alt_pause(1.5)
    scene black with fade3
    play music music_7dl["hey_you"] fadein 1
    me "And do you often spend your evenings like this with young and promising musicians, Alisa the fox?"
    "I whispered in her ear, unobtrusively pulling down her shorts and pushing aside the sticky fabric of her panties."
    "With my other hand I held the stepladder she was sitting on, her hands clutching at my shoulders."
    th "If I'd known we were going into that fucking backroom, I would have brought a flashlight!"
    dv "I'll tell you when I've spent one evening with an up-and-coming musician."
    me "Oh you..."
    "I entered sharply, deeply, making her cry out."
    "She responded by sinking her teeth painfully into my neck."
    "Grabbing her cheekbones, I turned her face to mine."
    "I kissed her sorely, bloodily, fiercely."
    "Fifteen minutes later, we were sitting on the floor of the back room, handing each other a samokurta."
    dv "Now you must marry me."
    me "Does someone marry you every night?"
    dv "No. You're the first lucky one."
    "The lights from the cigarette butt danced in her eyes, and I didn't quite know if she was joking or if she meant it."
    "I didn't want to understand it, though."
    stop music fadeout 4
    "I was happy with her here and now, and that was enough."
    $ alt_pause(1)
    $ set_mode_nvl()
    scene bg semen_room with fade
    play music music_7dl["sheiscool"] fadein 3
    voice "Has she decided to live here?"
    "Disgruntled, muttered Vas'ka, making his way through Alisa's scattered belongings to the balcony."
    nvl clear
    "Our career was going uphill in small steps."
    "For the last month we've been playing bars every weekend."
    "Even though the tickets cost a token couple of hundred, there were enough people willing to go to our concerts that we were finally able to move out of our parents' house."
    "Even if it was the whole band in one shabby apartment in the suburbs, it was just the beginning of real adulthood!"
    nvl clear
    "I wasn't worried about the comfortable existence in my own room being replaced by some wild mixture of a men's dorm, a nightclub, and a brothel."
    "Somehow I shuddered at the thought of living alone."
    nvl clear
    "Alisa visited us more often than any other fan."
    "And the guys were pretty annoyed, even though they only rolled their eyes silently when she occupied the bathroom for hours and swore quietly when she ate the last sausage."
    "Or just demanded that I make amends when there were only a few green crumbs left in the rusty jar with the 'tea' label, and crumpled cardboard filters with traces of her lipstick all over the balcony."
    dv "Mine doesn't care where I hang around at all."
    "Alisa answered my cautious question about whether her foster parents were looking for her."
    dv "They got themselves a whole bunch like me for the benefits. One mouthful more, one mouthful less, they won't even notice."
    dv "Oh, to hell with them! Let's get ready, we have a concert in three hours!"
    nvl clear
    "I took Alisa to concerts for free, even though Goshan kept whining that we'd go broke if we gave any pretty girl a pass."
    "But Alisa wasn't any pretty girl."
    "She was my pretty girl."
    stop music fadeout 4
    "And I was ready to send our whole group up their ass if they weren't happy with it."
    $ alt_pause(0.7)
    $ set_mode_adv()
    scene bg semen_room with fade3
    show dv angry modern with dissolve
    play music music_7dl["temptation"] fadein 3
    dv "You're just an actual bumfuck retard!"
    me "Shut up!" with vpunch
    show dv rage modern with dissolve
    play sound sfx_7dl["plates_broken"] fadein 1
    "A cup of tea broke under my feet."
    "My feet burned with boiling water, and I howled, spewing every swear word I knew at Alisa."
    dv "{image=alt_KS_censor}! I never want to see you again!"
    me "There, get the fuck out of here!"
    hide dv with dissolve
    "She slammed the door, and I waddled into the bathroom to stick my scalded feet in the cold water."
    pause(0.1)
    $ set_mode_nvl()
    scene black with dissolve
    play sound sfx_open_water_sink
    play sound_loop sfx_water_sink_stream fadein 1
    "Alisa didn't like to be rejected."
    "I didn't like it when she started begging."
    "And it turned into a terrible scandal every time."
    "She was like a child: she only knew the word 'want' and didn't understand the word 'no' at all."
    nvl clear
    "{i}You can't put pills in yourself every day. Toler, have you heard that word?{\i}"
    "{i}But I want to!{\i}"
    "{i}No.{\i}"
    stop sound_loop
    play sound sfx_close_water_sink
    pause(0.1)
    $ set_mode_adv()
    "The icy water brought almost instant relief, and I exhaled, closing my eyes and calming down."
    "Alisa will get over it and come back."
    "She always comes back."
    me "Ilyukha!"
    ml2 "What, the redhead ran away and there's no one to rub my back?"
    me "Do you have two thousands? You can deduct from my paycheck."
    stop music fadeout 4
    "For the last vestiges of my rationality evaporated when I thought of her."
    $ alt_pause(1)
    scene bg semen_room_window with fade3
    play music music_7dl["sid_and_nancy"] fadein 3
    me "Pass the lighter."
    pause(0.2)
    $ set_mode_nvl()
    "We huddled on the floor of the cluttered balcony."
    "That night, the whole shabby apartment belonged to us."
    nvl clear
    "Tonight was our first concert at the club."
    "The crowd of fans seemed endless, and we felt so wildly euphoric, like we'd packed an entire stadium."
    "I never imagined that one day someone would be bouncing to our songs with burning eyes."
    "Squealing when we show up on stage."
    "Throwing bras at our feet after the big hit."
    nvl clear
    "And Alisa stood backstage and sang with us."
    "Every song she put through her heart."
    "And without that, I never would have felt like we were doing something meaningful."
    nvl clear
    "The boys had gone to someone's country house, taking the most ardent groupies, and Alisa had asked to go home for some reason."
    "And now she was using the blunt side of a kitchen knife to smooth out two white stripes on an old stool without a leg."
    pause(0.1)
    $ set_mode_adv()
    me "What do you think is next in store for us?"
    show dv smile modern close with dissolve
    dv "Have you lost your mind completely? We're recording a new album in a week, then we're shooting a music video."
    "I looked at her carefully, shaking off the ashes."
    me "I'm not talking about the band. I'm talking about you and me, Alisa."
    show dv normal modern close with dspr
    "She twitched nervously."
    dv "Well, the same thing we always do, I guess."
    show dv grin modern close with dspr
    dv "What are you implying?"
    dv "You want a family life? A bunch of kids and evenings in front of the TV?"
    me "No way. We're just kids."
    show dv normal modern close with dspr
    "With my head up, I stared out the window, into the blackening sky."
    me "Do you have a dream?"
    dv "I want to go to the sea. I'm sick of this cold swamp!"
    show dv smile modern close with dspr
    dv "I want to lie on warm pebbles, eat oranges and listen to the sound of the surf."
    dv "And when it gets dark, I want to drink cocktails and dance at the bar until dawn."
    "And in that second it seemed to me that I wanted to do it myself."
    "It was like Alisa was always voicing my desires out loud."
    "It was just my job to realize the dreams that she was making up for the two of us."
    me "Then after we record the album, we'll go to the sea. Alone, like a normal couple."
    show dv normal modern close with dissolve
    dv "Do you consider us a normal couple?"
    "Alisa straightened up over the stool, wrinkling her face and clamping her nostril with all her might."
    "I took the empty pen case from her trembling hand."
    me "I think we're a totally insane couple. But what does it matter?"
    me "I still love you."
    "She didn't respond."
    "She never responded to words like that."
    "I leaned over the stool, taking a sharp painful breath."
    th "I don't need you to answer. I know everything myself."
    th "You love me, too. I see it every time I just look at you."
    th "We'll always be together, Alisa."
    th "And we won't live to retirement."
    $ meet('ml','Boy')
    $ meet('ml2','Boy')
    $ meet('voice','Voice')
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("dv_dj_good")
    show acm_logo_dv_dj_good with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    pause(1)
    return

label alt_day7_dv_dj_herc_exc:
    play sound sfx_hell_alarm_clock
    scene black with dissolve
    th "What a nasty alarm clock I have..."
    th "I'll have to change it on occasion."
    stop sound fadeout 1
    scene bg int_sam_room_7dl with fade
    "I grabbed my phone off the nightstand and pressed the 'drop call' button."
    th "Five more mi..."
    play music music_list["drown"] fadein 5
    scene
    $ renpy.show("bg int_sam_room_7dl", what = Notch("bg int_sam_room_7dl"))
    with vpunch
    "I jumped up out of bed so abruptly that my eyes went black."
    show tapochek_mobile_7dl with dissolve
    "I had an old blue Siemens in the palm of my hand."
    me "You got pretty wasted last night, my friend."
    "I mumbled as I looked at this wonder of technology that had been obsolete for twenty years."
    "But I didn't remember drinking yesterday."
    "But I remembered very well that I had bought this phone only a month ago, and I was very happy about it-mobile phones cost as much as an airplane wing, and here an acquaintance offered to get it for a pretty decent price."
    hide tapochek_mobile_7dl with dissolve
    th "Then why this feeling that something is wrong?"
    th "That I should have a different phone, and a different apartment, and a different... everything?"
    "I frowned, trying to remember my dream."
    scene bg ext_square_day
    show prologue_dream
    with dissolve
    "There was a summer camp, still Soviet."
    "And pioneer girls."
    show dv sad pioneer2 close behind prologue_dream:
        alpha 0.3
    with dissolve
    "And some redheaded girl who felt so bad, and there was nothing I could do about it."
    scene bg int_sam_room_7dl with dissolve
    th "I never thought that at my age senility would set in."
    th "Only nine years ago I was rejoicing with the whole country that the damned Soviet Union had fallen apart, the curtain had fallen, and now I'm nostalgic!"
    th "And what a beautiful camp it was, just like in the picture: new, clean, with neat houses. Not like the barracks I used to live in!"
    th "And that redhead... She didn't look like anyone I knew."
    "I can't believe I'm dreaming about this."
    "Sighing heavily, I got out of bed and stumbled into the kitchen. Dreams are good, but they don't work as an excuse for being late."
    stop music fadeout 5
    th "And where did I get this strange feeling that I have to save someone?"
    scene black with fade3
    $ alt_pause(1)
    $ day_time()
    scene bg int_liaz_city_7dl with dissolve
    play sound_loop sfx_bus_interior_moving fadein 4
    "Outside the bus window a sultry summer was raging."
    "Tourists in warm raincoats, who had been promised a rainy and gray swamp, looked up at the sky in disbelief, as if they thought the city authorities had put up a plywood sun to spite them."
    "And I smiled out the window like a fool, making them further doubt the reality of what was happening."
    "With a weighty folder of documents in a shabby bag, I was on my way to the most important meeting of my life."
    $ alt_pause(1)
    $ prolog_time()
    scene bg int_liaz_city_7dl
    with dissolve
    $ set_mode_nvl()
    play music music_list["lightness_radio_bus"] fadein 4
    "On that gloomy March evening I didn't go home after work, but decided to finally get to the electronics store."
    "I couldn't afford a computer because I hadn't yet recovered from buying a cell phone."
    "But I wanted to see what's new!"
    nvl clear
    "On the half-empty bus, I took a window seat."
    "It was a long ride, so I stared out the window, wiggling my leg to the beat of the song stuck in my head."
    "In my dreams, I was already listening to it right in my room, while playing doom on my brand-new computer."
    hide prologue_dream with dissolve
    pause(0.1)
    $ set_mode_adv()
    $ persistent.sprite_time = "night"
    th "Should I borrow from Pavlusha? He still owes me money for assembling the kitchen..."
    stop music fadeout 6
    "I didn't immediately find out that the seat next to me was taken by someone."
    show dvk normal casual close at right with dissolve
    play music2 music_list["just_think"] fadein 2
    $ meet('dv','Little thief')
    "I took a quick glance at a girl about ten years old, scruffy, in rags."
    th "You have to keep all your possessions close, or you might lose your wallet!"
    "And, as if she'd heard my thoughts, the girl looked around stealingly."
    hide dvk with dissolve
    "I acted as if I didn't even know she existed."
    "And her raking skinny hand was already reaching for the unbuttoned backpack of the girl sitting in front of us."
    th "Well, no way! I will not tolerate theft in my presence!"
    show dvk scared casual with dissolve
    dv "Ow!"
    "The girl exclaimed as I grabbed her arm."
    "The bus began to creak to a halt."
    me "Let's go talk!"
    dv "Don't!"
    "The unsuccesful thief shouted, scared."
    dv "Let me go! I didn't mean to do anything!"
    stop music2 fadeout 3
    "Passengers watched indifferently as I pulled a struggling girl off the bus."
    stop sound_loop fadeout 1
    $ alt_pause(1)
    hide dvk with dspr
    scene bg ext_street_night_7dl
    $ persistent.sprite_time = "day"
    show dvk sad2 casual
    show snow
    with dissolve
    play music music_list["tried_to_bring_it_back"] fadein 2
    "Pulling her away from prying eyes, I looked her sternly in the eye."
    me "So little, and already you're stealing! Shame on you!"
    me "I'll call the police, and they'll take you away from your parents and put you in jail."
    show dvk angry casual with dspr
    dv "And I have no parents!"
    "The little girl barked back."
    "I was taken aback."
    me "What do you mean, no...?"
    show dvk normal casual with dspr
    dv "My father was killed in Chechnya, and my mother died of grief."
    "I thought she said it with a kind of naive childish pride."
    th "Is she lying to get pity?"
    me "Then where do you live?"
    dv "In an orphanage. In the nineteenth, on Staro-Petergofsky."
    th "I don't think she's lying."
    th "Too young to be so well prepared for questions from adults."
    me "And what are they not feeding you there? Don't you have any toys?"
    me "Why steal?"
    show dvk sad2 casual with dspr
    "The girl's head is bowed."
    dv "It's my birthday today."
    "Her voice dropped to almost a whisper: she seemed to be holding back tears."
    show dvk guilty casual with dspr
    dv "So did she. But she had the party and the cake and the presents..."
    "Even if she was making it all up, I felt terribly sorry for the little thief."
    th "Dressed in worn-out clothes, skinny as a chip, unwashed."
    th "It must be hard for her, poor thing."
    th "To hell with the computer! It can wait, it won't get dusty!"
    me "What's your name, birthday girl?"
    show dvk normal casual with dspr
    $ meet('dv','Alisa')
    dv "Alisa."
    me "And how old are you?"
    dv "Ten."
    "I whistled - with a little more enthusiasm than I tried."
    me "Wow, an anniversary - and no cake! That's not right!"
    show dvk surprise casual with dspr
    me "Come on, Alisa, let's go celebrate your birthday."
    me "If you want to invite me, of course."
    show dvk dontlike casual with dspr
    "She looked at me incredulously."
    dv "Are you trying to make fun of me?"
    me "Not at all. You'll have cake and ice cream and whatever you want."
    show dvk normal casual with dspr
    me "But only on one condition: that you promise me that you won't steal anymore."
    dv "I promise!"
    me "That's the deal. Then let's go celebrate!"
    show dvk happy casual with dspr
    "The girl's face brightened, and she could no longer contain her smile."
    "And that's when I noticed..."
    th "She's a redhead!"
    th "Yes, and her face is like the pioneer girl in my dream."
    th "Except that one was a little older, but in general terms she was very similar."
    th "Maybe it was a sign."
    show dvk shy casual with dspr
    dv "And what's your name?"
    me "Semyon."
    me "And you don't have to be that polite with me - I'm not that old yet."
    stop music fadeout 5
    show dvk smile casual with dspr
    $ alt_pause(1)
    scene bg ext_childhouse_winter_7dl with dissolve2
    play ambience ambience_cold_wind_loop fadein 4
    $ persistent.sprite_time = "night"
    "After our humble feast, I volunteered to take a well-fed and contented Alisa to the orphanage."
    show dvk guilty casual with dissolve
    dv "Are you going to complain about me?"
    me "No. Why should I complain about you?"
    show dvk normal casual with dspr
    me "You promised you wouldn't do anything bad again."
    stop ambience fadeout 1
    pause(0.2)
    $ day_time()
    $ set_mode_nvl()
    scene bg int_opened_door_7dl with dissolve
    play music music_list["raindrops"] fadein 2
    $ persistent.sprite_time = "day"
    "After handing Alisa over to her caregiver, I quietly asked the guard to take me to the principal."
    "I wanted to know if there was any possibility of taking custody of the girl."
    th "Some people pick up stray cats, but I pick up children."
    th "That's how I lived to a ripe old age..."
    nvl clear
    scene bg ext_childhouse_winter_7dl with dissolve
    "Of course, things were more complicated with children than with cats."
    "There was a lot of paperwork to be done, and I was already figuring out how much money I should allocate for cognac and candy."
    "It was impossible for a single man, however decent-looking, to get custody without a fight."
    "The principal and I agreed that for the time being I could visit Alisa on weekends."
    "And I was already thinking how I could involve my mother in this reckless scheme."
    stop music fadeout 3
    $ alt_pause(1.7)
    $ set_mode_adv()
    scene bg int_childhouse_corridor_7dl with dissolve
    play music music_7dl["everlasting_summer_alice"] fadein 2
    show dvk happy dress with dissolve
    dv "You made it!"
    show dvk happy dress close with dissolve
    "Alisa galloped impatiently down the corridor and came running toward me, almost knocking me down."
    "Nearby stood her teacher with a small bag in her hands."
    me "Easy, you're choking me!"
    show dvk happy dress with dissolve
    "I laughed, putting Alisa on the floor."
    me "Now I'll get all your papers from the principal, and we'll go home."
    show dvk smile dress with dspr
    dv "For good?"
    "She's asked it a hundred times now, but I was ready to answer again:"
    me "For good, for good."
    show dvk happy dress with dspr
    scene bg ext_childhouse_day_7dl
    show dvk smile dress close
    with dissolve
    "And ten minutes later, when Alisa Smoleva was already officially part of my family, we went outside."
    dv "Are you glad I'm your daughter now?"
    me "Of course I am. How can you not be?"
    dv "Is grandma happy?"
    th "Hardly more than I am."
    th "Mother didn't expect any more grandchildren, and here's a present for her!"
    th "Oh, if it wasn't for her help, we wouldn't have settled this in ten years..."
    me "And she's glad. Do you want to go and visit her tomorrow?"
    show dvk happy dress close with dspr
    dv "Of course I do!"
    "Alisa was jumping around me like a wind-up."
    show dvk normal dress close with dspr
    "And then she slowed down, staring ahead."
    "A man was walking toward us, and on his shoulders sat a boy a little younger than Alisa, waving a plastic saber menacingly."
    show dvk shy dress close with dspr
    "My stepdaughter opened her mouth, but immediately blushed and stared at the pavement."
    "I couldn't stand it and laughed."
    me "Hop in already!"
    scene cg d7_dv_child_7dl with dissolve
    "I was walking toward the bus stop with my overly cheerful burden on my shoulders."
    "And who'd have thought that could happen if you just happened to go out after work?"
    "We'll wait on the computer. We have so much to buy for Alisa."
    "And I don't need it now. Those stupid toys..."
    "I'm big and responsible for someone now."
    "I can't get my childhood back, but at least someone else will have it."
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("dv_dj_herc_exc")
    show acm_logo_dv_dj_herc_exc with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    pause(1)
    return

label alt_day7_dv_dj_loki_exc:
    play music music_7dl["so_cold"] fadein 2
    $ set_mode_nvl()
    scene bg ext_city_night2_7dl with dissolve2
    "My life has gotten awfully slow."
    "I wait endlessly for my workday to end."
    "It takes me endlessly to get home, always getting stuck in evening traffic."
    "It takes me endlessly to fall asleep, and I even sleep endlessly."
    "And waiting endlessly for an answer from the salesmen, only to sigh doomfully over and over again."
    nvl clear
    scene bg semen_room with dissolve
    "The Internet is a big dump."
    "If you want to find something on it, you have to sweat it out, and sometimes it costs a pretty penny."
    "For the last month I've been scouring the archives of orphanages in St. Petersburg and the region for the nineties, but I haven't found a single girl who fits all the parameters I know."
    "All Alisas were either not born in the nineties or adopted before they were ten years old."
    nvl clear
    "Sometimes I was beginning to think it was all useless."
    "That there were more worlds than two, and Alisa had come to the camp world from another future-from a very similar future to mine, but not mine."
    nvl clear
    "I spent about a hundred thousand, but I never found her."
    "Despair was slowly but surely creeping up on me."
    "But I couldn't let it go any longer."
    "I was too far gone in my search to just give up on this foolish undertaking."
    nvl clear
    th "For if a person like me lives in that world, so can a person like me live in this one..."
    th "And in this one a person like Alisa can live."
    nvl clear
    "And that made it that much harder."
    "Because in this world, she might not have gotten into an orphanage at all."
    "Or live in a place other than St. Petersburg."
    "Or..."
    "There were so many 'ors' that my head was splitting."
    "One thing I knew for sure was that Alisa Dvachevskaya did not exist in this world."
    "And I never bothered to find out her real name."
    nvl clear
    "For a week I went like a drowned in water."
    "I had no idea exactly how I should continue my search."
    scene bg semen_room with dissolve
    "But one particularly lousy evening, I opened a file folder and a notebook."
    "And began methodically writing out all the Alisa's of the nineties that someone had taken into the family."
    "My humble list contained the names of seven girls and their guardians."
    $ alt_pause(1)
    $ set_mode_adv()
    "I crunched my stiff neck and unfolded my browser - I had the most exciting part ahead of me: searching social networks."
    "At first I searched by 'original' last names, and I wasn't too surprised at the failure."
    "After all, the girls were taken very early and had no reason to cling to the past."
    "I switched to the names of the guardians."
    "It was scary."
    "After all, if she was already married and had changed her last name again, I wouldn't even be able to know if she was okay!"
    "Six Alisa later I was ready to growl into the monitor."
    "The girls in the pictures didn't even closely resemble my Alisa."
    "By typing 'Alisa Arkatova' into the search engine, I was getting my hopes up."
    stop music fadeout 2
    play sound_loop sfx_7dl["pk_venti"] fadein 1
    "But when I clicked on the first link I almost fell off my chair."
    scene cg d7_dv_loki_exc_7dl with dissolve
    play music music_7dl["raindrops"] fadein 2
    "She was the one in the picture."
    "Not the way I remembered her at camp. Grown-up, serious."
    "Sitting in an ajar car with a cup of coffee, staring thoughtfully away, just like the cover of an art-house movie about the plight of millennials."
    "There was no doubt - Alisa was alive, and living quite well."
    "Sverige, Umeå was listed as her place of residence."
    "Her heart went down."
    th "Maybe it was just for fun. People like to put fancy countries and cities on their profiles..."
    stop sound_loop fadeout 3
    pause(0.5)
    $ set_mode_nvl()
    "But her whole profile said otherwise."
    "Photos of Scandinavian architecture, posts in Swedish, people with distinctive surnames in -son and -gren on her Friendlist all suggested that Alisa wasn't just spending her vacations there."
    "'När man talar om trollen så står de kanske där i farstun,' Alisa wrote in her status."
    nvl clear
    "I stared at the translator and couldn't figure out what she might have meant."
    "This Alisa I didn't know at all."
    scene black with fade3
    $ set_mode_adv()
    play sound_loop sfx_street_traffic_outside fadein 2
    "I spent half the night on her page, reading the crude translations of her posts."
    "I spent the rest of the half-night lying awake, trying to think about what I'd learned about this stranger with a face so painfully familiar."
    scene bg int_semen_room_window_day_7dl with dissolve
    "And before I left for work, I requested all the data on Alisa and her family."
    "Such information was worth more than some leaked archives during the digitization process."
    th "It's okay - it's time for me to lose weight. And I need to quit smoking..."
    stop music fadeout 2.5
    stop ambience fadeout 3
    $ alt_pause(1.7)
    $ set_mode_nvl()
    scene bg ext_childhouse_winter_7dl
    show prologue_dream
    with dissolve
    play music music_7dl["longing"] fadein 4
    "The Arkatovs took Alisa from the orphanage when she was four years old."
    "Father's a programmer, dropped out of university in the late '80s."
    "Mother is a former drummer in some perestroika band."
    "The family moved to Sweden in '97 because the head of the family was offered a job there."
    "They settled in Umeå."
    "That was the end of all the information available to me."
    "To find out about the family's life after emigrating, I was asked for so much money that I almost choked to death on such insolence."
    nvl clear
    scene cg d7_dv_loki_exc_7dl with dissolve
    "I didn't need that, though: Alisa shared her life on Facebook for free."
    "She graduated from university and worked as a producer for some tiny independent label."
    "Judging by the activity on her page, though, she didn't suffer from a lack of friends or finances."
    "For a week I sat with a translator, meticulously probing every detail of her life."
    nvl clear
    "Alisa didn't like cats, preferring them to dogs."
    "And all her friends seemed to be extremely offended by this fact."
    "Alisa played guitar, but only at parties."
    "And sometimes had mini concerts at a small bar with her foster mother."
    "Alisa listened to a lot of audiobooks and left detailed reviews of them, spicing them up with humor that was too peculiar for me."
    nvl clear
    "{i}Hello.{\i}"
    "{i}You know, I had the strangest dream: you and I were at a Soviet pioneer camp, and you were the DJ on the camp radio.{\i}"
    "{i}You were always slacking off, and I actively supported you in that. You had nightmares and memories of the orphanage, but you could only share them with me.{\i}"
    "{i}And I miss you so much, Alisa. I miss you so much.{\i}"
    stop music fadeout 6
    play sound_loop sfx_7dl["pk_venti"] fadein 1
    $ alt_pause(1)
    $ set_mode_adv()
    scene bg semen_room:
        zoom 1.4
        align (0.5, 0.5)
    with dissolve
    "I sighed and erased my message."
    "I closed the tab with her page and deleted the link to her from my bookmarks."
    $ alt_pause(1)
    stop sound_loop fadeout 3
    scene semen_room_window with dissolve
    play music music_7dl["fogive_me"] fadein 4
    "That wasn't my Alisa."
    "This girl grew up in a loving, wealthy family."
    "She spoke and probably even thought in a different language."
    "It was as if she and I lived in different worlds."
    "And why would she want a loser who only fell in love with an exact replica of her in some other reality?"
    "My Alisa stayed there at camp. And she'll be fine, too."
    "I really want to believe that."
    scene stars with dissolve2
    "For no matter how many millions of copies of Alisa exist in millions of copies of worlds - I don't want any of them to be unhappy."
    "But I only love one."
    "And to replace her with someone like her is to betray my memory of her."
    "A memory that will keep me from going mad."
    scene cg d7_dv_stars_7dl with dissolve2
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("dv_dj_loki_exc")
    show acm_logo_dv_dj_loki_exc with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    pause(1)
    return

label alt_day7_dv_dj_dr_exc:
    play music music_7dl["deadline"] fadein 3
    scene anim prolog_4 with dissolve
    $ set_mode_nvl()
    "My memory got worse every year."
    "First the names began to fade from my memory."
    "And then the faces."
    scene prolog_10 with fade
    "Vague images of voices, colors, smells, and emotions stayed with me a little longer, but eventually, quite legitimately, faded into oblivion with everything else."
    "I had absolutely no memory of what I ate for breakfast, and sometimes before going to bed I was somewhat surprised to realize that I had no idea what I had been doing all day."
    "Sometimes in the morning I had to take a long time to remember what I got out of bed for in the first place."
    scene bg semen_room with fade3
    pause(0.1)
    $ set_mode_adv()
    dreamgirl "You have a deadline in three days. I hope you still remember the task?"
    "Serviently prompted by my schizophrenia."
    th "It doesn't matter."
    th "It's like I promised something."
    th "But to whom and when? I can't remember the last time I talked to a living person."
    pause(0.5)
    $ set_mode_nvl()
    "Sometimes I stopped at a shelf of books."
    "It seemed to me as if it held some clue, some secret code I had left for myself."
    "But no matter how much I looked at the spines of the dusty volumes, the magical insight was unwilling to visit me."
    pause(0.5)
    $ set_mode_adv()
    th "Then why is it so restless inside?"
    "The monitor flickered softly in the semi-darkness of the apartment."
    "I paced from corner to corner, casting hateful glances toward the ill-fated shelf."
    th "Maybe it wasn't the books."
    "I opened the glass door and stared at the thickness of the dust."
    "A faint glare made me wince."
    "A pioneer badge."
    "An old one, left to me by my father."
    "At one time I didn't have the heart to throw it away."
    th "Life is so wonderful: a man is willing to keep the last memory of someone who, without blinking an eye, crossed him out of his memories."
    th "And I have too few of those memories left to throw away."
    "I took the badge in my hand and carefully wiped off the layer of dust with my fingers."
    scene bg semen_room:
        zoom 1.4
        align (0.5, 0.5)
    with dissolve
    "I sat down in an armchair and began to look at this artifact of a bygone era."
    th "I think Alisa had one of these..."
    play sound_loop sfx_7dl["pk_venti"] fadein 1
    stop music fadeout 1
    scene bg int_semen_room2_7dl:
        zoom 1.4
        align (0.5, 0.5)
    with dissolve
    $ alt_pause(0.5)
    "The monitor went out."
    "I stared dazedly into the darkness."
    play music music_7dl["breath_again_slow"] fadein 6
    "I couldn't forget the week I spent at camp, could I?"
    "A week in the past that had nothing to do with my reality?"
    th "It turns out I could."
    th "But how?"
    dreamgirl "You've been running from pain for so long, you do it quite naturally."
    dreamgirl "It's easy for you to blot out the faces of those you've lost forever. It's easy to cross out the images of those who, alas and ah, are happy without you."
    dreamgirl "Those who no longer care about you."
    dreamgirl "Because you yourself will never make an appointment, or dial a number, or even lift your eyes to a random passerby or subway passenger."
    dreamgirl "You'll always wait for things to come to you by themselves."
    th "That's not true!"
    th "I did... I did want to find her."
    th "At least find out what happened to her, if nothing could be fixed."
    th "She stayed there, and I had no place in that world. I wasn't ready to fight for it."
    dreamgirl "Looking for excuses for yourself?"
    th "There can be no excuses here!"
    th "I am not a murderer!"
    "Leaning back tiredly in my chair, I closed my eyes."
    th "Tomorrow I will go looking for her."
    th "And if I forget..."
    "But I was sure it would not happen again."
    "It was impossible to run away from myself for so long, though I considered myself almost a professional in this business."
    "Even though I had lost my mind, I wanted to save myself at least a little."
    "At least the part that loved Alisa."
    stop sound_loop fadeout 1
    $ alt_pause(1)
    $ set_mode_nvl()
    scene bg ext_city_night2_7dl with dissolve
    "There were many orphanages. So many."
    "I didn't know what I was hoping for, going to each one and asking the same stupid question."
    nvl clear
    "{i}Have you ever had a red-haired girl named Alisa?{\i}"
    "{i}Born in the nineties. Weren't you working at the time?{\i}"
    "{i}Then can I at least take a look at the records? I'm sure there's something left.{\i}"
    "{i}No? I'm sorry to bother you.{\i}"
    "{i}Goodbye.{\i}"
    nvl clear
    show bg semen_room_window with dissolve
    "It wasn't hard for me to talk to people."
    "The feeling of shame was forgotten, like everything else I'd experienced lately."
    "And I could hardly even remember the reason why I was still on this quest."
    show bg ext_city_night_7dl with dissolve
    "A new day, a new street."
    "A new place, reverberating with someone else's pain and despair."
    "Before I began my search, I was sure there was nothing in the world more desperate than my lonely abode."
    "Now I realized how naive and self-centered it was to believe something like this."
    dreamgirl "I suggest that after the orphanages are over, we start going to hospices."
    dreamgirl "Maybe it will make you stop feeling sorry for yourself, at least for a while."
    stop music fadeout 4
    pause(1)
    play ambience ambience_cold_wind_loop fadein 4
    $ set_mode_adv()
    scene bg ext_childhouse_winter_7dl with dissolve
    "I went outside, once again hearing the refusal to see the archives."
    "The slush beneath my feet, the slush over my head, the damp and dreary walls of the orphanage, all blended into one colorless mass."
    voice "Hey, kid! Looking for your kid, are you?"
    "I shuddered."
    $ meet('voice','Woman')
    "An obese woman in years, smoking a cigarette by the porch, looked at me mockingly."
    me "No. I'm looking for a girl who used to grow up in an orphanage."
    "Not quite sure why I replied to this taunt."
    me "Only that was a long time ago. Twenty years ago."
    "The woman perked up."
    voice "I've been working here since '93."
    voice "I don't remember all the kids, you know, but if your girl was notable..."
    "The colorless day was stirred up by a timid ray of hope."
    me "She was a redhead. Her name was Alisa."
    me "Born in '90, she'd been here as long as she could remember."
    "The woman's face took on a strange expression."
    voice "Wasn't it Smoleva?"
    "I shrugged."
    me "I don't know her last name. I didn't know her that long, so I didn't have time to ask around."
    voice"I'm afraid there's nothing for you to look for."
    "My companion shook her head."
    play music music_7dl["frostwithoutyou"]
    voice "Your Alisa died."
    voice "The other girls beat her to death for some toy."
    "She sighed, extinguishing her cigarette butt on the damp railing."
    voice "Times were tough back then."
    voice "They didn't pay much, the kindergarteners watched soap operas, a patron of the arts gave us cable TV back then."
    voice "Some went missing in some brothels, some got mixed up with all kinds of bad people out of hopelessness. You know, they seldom took anyone away. People had nothing to feed themselves."
    voice "Not long before your Alisa, there was another emergency: a boy from her group, Valera, got glue poisoning right in the toilet."
    voice "After she died too, everyone was sure we'd all be sent away."
    voice "But where would they put the kids? There was nowhere to put them. Nobody wanted them, those poor kids."
    voice "The teacher almost went to jail, but got only a suspended sentence: she had a young daughter and her husband had been killed in Chechnya."
    "I listened to her, and my heart ached."
    th "Alisa had been through it all."
    th "She had, but she could still laugh and rejoice in even the simplest little things."
    th "And I, the fool, was sulking at her for not wanting to talk to me about this nightmare!"
    me "Can you take me to her grave?"
    "The woman looked at me sympathetically."
    voice "Let's do it on my day off, honey. I can't leave kids now."
    "I took the number from this wordy woman, thanked her, and hurried home."
    stop music fadeout 5
    stop ambience fadeout 5
    "I had a lot to think about before Saturday."
    $ alt_pause(1.5)
    scene bg ext_smolensky_graveyard_winter_day_7dl
    show snow
    with fade3
    $ meet('voice','Tamara Ivanovna')
    play ambience ambience_cold_wind_loop fadein 4
    voice "It's snowing so hard! Don't they clean it at all?"
    "Tamara Ivanovna grumbled softly as she made her way through the drifts."
    "I followed, looking around."
    "The gravestones always caught my eye."
    "It wasn't hard to understand teenagers who liked to hang out in places like this."
    "In this realm of sorrow, one felt particularly keenly that one was still alive."
    play music music_7dl["knock"] fadein 3
    voice "Here cames your friend, Alisa."
    "The old educator brushed a cap of snow off the crooked cross with her hand, crossed herself, and smiled sadly."
    voice "I'm the only one who goes to them."
    voice "Without me there wouldn't be any crosses left, there were those who wanted to take the places for their own, but I'm the only one chasing, almost fighting to defend these graves."
    voice "They had nothing in their lifetime..."
    "With a heavy sigh, Tamara put her hand into her bag, took out a handful of sweets and carefully placed them at the foot of the cross."
    voice "Now I'm going to go see Valera. He's lying here, too."
    play sound "<from 18 to 20>" + sfx_intro_bus_stop_steps
    "She left, and I kept standing as a statue at the rusty cross."
    "{i}Smoleva Alisa Maksimovna{\i}"
    "{i}3.03.1990 – 3.03.2000{\i}"
    "Ten years she lived in hell."
    "Would she have gotten out of that hell if she hadn't been in the distant past?"
    "And why in this world do I go on living and she lies here?"
    "And why was she able to stay in that world and I went back to a place where she will never be again?"
    "So many questions. So few answers."
    me "Thank you."
    "I whispered, gently touching the plaque with my fingers."
    me "You're the only one in the world who showed me what it is to love life."
    $ meet('voice','Voice')
    stop ambience fadeout 5
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("dv_dj_dr_exc")
    show acm_logo_dv_dj_dr_exc with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    pause(1)
    return

label alt_day7_dv_dj_true:
    scene black with dissolve
    $ set_mode_nvl()
    play music music_7dl["sleeping_beauty"] fadein 4
    "They say that if you really, really wish for something, it's bound to come true."
    "You have to close your eyes on a special day - New Year's Eve or your birthday - think hard about what you wish for, and when you open your eyes, your dream will come true."
    "It's just all lies."
    "None of my wishes ever came true."
    nvl clear
    "But last night I still closed my eyes tightly and whispered:"
    dv "I wish I had a mom and dad."
    "It's not every day I turn ten, after all!"
    scene bg int_childhouse_room_day_7dl with dissolve
    nvl clear
    "But the miracle didn't happen, as usual."
    "I woke up in the same uncomfortable bed, under the same smelly blanket, and there was no birthday cake waiting for me, but liquid semolina."
    "We don't celebrate birthdays like in the movies or cartoons."
    "It's always so pretty: presents, guests, New Year's Eve decorations, mountains of delicious food, and always a cake with candles."
    "And we have a birthday party once a year, when the volunteers congratulate everyone at once, without even remembering our names."
    "And then the kindergarten teacher picks out the prettiest presents - she says we're old enough for them, and she'll give them to the younger group."
    "But I saw her nasty daughter combing my Barbie!"
    nvl clear
    scene bg ext_sky_7dl with dissolve
    "I didn't go to the playroom after breakfast."
    "I pulled my jacket off the rack and rushed outside."
    "I may not have a real birthday like in the movies, but I wanted something special!"
    "But first I had to get some money."
    nvl clear
    "Crawling around the bus stops looking for coins was useless in March - they were quickly lost in the muddy snow and water."
    "We were always chased away from the fountains by homeless people."
    "It was humiliating to ask, and scary: at the orphanage they could have dragged us by the ears for such a thing."
    "For those who lived on the other side of the fence, we were fine: four meals a day, volunteers, even some pat... kind man paid for cable TV."
    nvl clear
    scene bg int_liaz_city_7dl with dissolve2
    play sound_loop sfx_bus_interior_moving fadein 4
    "I had to choose the most unreliable way to 'make money' - the bus."
    "It's a delicate business: you have to pass on the fare, and you have to slip yourself a penny or two."
    "You can't take much, you'll get caught. You can't take too little, it's pointless."
    "I rode for half a day and managed to get almost twelve rubles."
    "Now all that was left was to get to the center and look for something nice."
    nvl clear
    "On another bus I sat behind a very cheerful and noisy family."
    "The girl had bright bows in her hair and was holding a Mickey Mouse balloon."
    "It made me jealous."
    "Do all the kids on the other side of the fence get balloons for nothing?"
    pause(0.1)
    $ set_mode_adv()
    $ meet('sl','Slavyana')
    $ meet('voice','Girl')
    voice "So, Slavyana, did you enjoy your party?"
    sl "Yes! And the clown was funny, and the cake was delicious!"
    sl "And what did Grandma get me?"
    $ meet('voice','Woman')
    voice "She wants to surprise you, honey."
    sl "Tell me, tell me! That pink horse, huh?"
    "So it was her birthday, too."
    "Only a real one, not like mine."
    $ meet('sl','Slavya')
    pause(0.1)
    $ set_mode_nvl()
    "She's been having fun and eating cake all morning, not rolling around, hungry as a dog, on buses."
    "And she gets gifts too..."
    "And I don't even have enough money for the same bows."
    "For some reason I felt like yanking Slavyana's braid."
    "I even leaned forward, when suddenly..."
    nvl clear
    "I noticed that the zipper on her little colored backpack had come undone."
    "And there was a tamagotchi looking right at me from above."
    "A real one! Just like in the picture!"
    nvl clear
    "I didn't have to convince myself - as soon as the bus started to slow down, I quietly snatched the cherished toy, hid it in my sleeve, and hurried to the exit."
    stop sound_loop fadeout 1
    scene bg bus_stop with dissolve
    nvl clear
    "That girl has everything anyways."
    "And a mommy, and a daddy, and a clown, and a cake, and a pink horse, and pretty bows."
    "And I would have, if my parents hadn't died."
    nvl clear
    "I used to think my parents were killed by robots from the future."
    "Then I thought they drowned on the Titanic."
    "But now I knew for sure that my father was a hero, and he was killed in Chechnya."
    "And my mother died of grief."
    "When I found out my dad was a hero, I thought she'd just abandoned me, and I was mad at her."
    "But then I heard on the show how someone died of grief, and I realized that the same thing had happened to Mom."
    nvl clear
    scene bg ext_winterpark_7dl with dissolve
    play ambience ambience_cold_wind_loop fadein 4
    "It was only after running away from the bus stop for a hundred kilometers that I decided to look at the Tamagotchi."
    "I held it tightly in my hands - I was afraid they were going to take it away."
    "I climbed a tree in the park and started to feed my new pet."
    stop music fadeout 3
    $ alt_pause(2)
    $ set_mode_adv()
    scene bg ext_childhouse_winter_7dl with dissolve
    "I didn't come to the orphanage until I was so cold that my fingers couldn't move."
    stop ambience fadeout 1
    scene bg int_childhouse_room_night_7dl with dissolve
    play ambience ambience_int_cabin_night fadein 2
    "Sneaked into the bedroom, slipped my money and tamagotchi under the pillow, then went to dinner with the others."
    stop ambience fadeout 2
    show blink
    $ alt_pause(2.5)
    play ambience ambience_int_cabin_night fadein 4
    scene bg int_childhouse_room_night_7dl with fade
    "After lights out, I was tossing and turning for a long time."
    "I thought that if I fell asleep, the Tamagotchi would disappear. That he was just dreaming."
    "I put my hand under the pillow and pulled out my pet."
    "He was there."
    "It was real. {w} Mine."
    play sound sfx_7dl["tamagochi"]
    "And then it beeped so loud that I jumped up."
    play music music_7dl["areyouabully"] fadein 3
    "The girls jumped out of bed in a flash, looking for the source of the noise."
    $ meet('voice','Girl')
    $ meet('unp','Girl')
    $ meet('pi','Girl')
    $ meet('mz','Girl')
    unp "What have you got there?"
    pi "Wow! Tamagotchi!"
    mz "Where did you get it?"
    voice "Let me see!"
    unp "Let me play!"
    "They swarmed me and started pushing each other and me."
    "Their hands reached for my tamagotchi."
    "My tamagotchi!"
    stop music fadeout 2
    dv "I won't! It's mine! Mine!"
    play music2 music_list["pile"] fadein 3
    mz "Oh so?"
    voice "Stingy!"
    with hpunch
    pi "We'll tell the teacher that you stole it!"
    unp "Give it to me nicely!"
    with vpunch
    voice "Me first!"
    with hpunch
    $ meet('unp','Pioneer')
    $ meet('pi','Pioneer')
    $ meet('mz','Zhenya')
    "In the ensuing scuffle, everyone got punched, but especially me."
    "I got angry, kicked them back, pressed my pet against me, and they pulled my arms, unclenched my fingers, tried to get at them with their teeth."
    dv "Get off me! I won't give it to you!" with vpunch
    stop music2 fadeout 4
    scene bg int_childhouse_room_night_7dl:
        zoom 1.0 xalign 0.5 yalign 0.15
        linear 10.0 zoom 1.75 xalign 0.5 yalign 0.45
    play sound "<to 6.0>" + sfx_7dl["mpbt"]
    with flash
    "One of the girls tripped me, and I felt myself falling."
    "I couldn't open my hands-they would have grabbed the Tamagotchi right away."
    play sound sfx_lena_hits_alisa
    scene black with flash_red
    "The back of my head pierced with pain."
    scene bg int_childhouse_room_night_7dl:
        zoom 2.0
        xalign 0.5
        yanchor 0.256
        rotate 70
    show alt_blink
    with fade
    play music music_7dl["wonderful_faraway"] fadein 4
    stop ambience fadeout 3
    "My eyes are blurry."
    $ meet('voice','Caregiver')
    voice "What's going on he..."
    voice "Smoleva!"
    "I heard her shriek as if from another room."
    show spill_red with dissolve2
    "There was a corner of the window sill above me, and something warm was spreading under my head."
    show prologue_dream with dissolve2
    "Did I drop the flowering watering can?"
    "I'm going to get killed for sure."
    play ambience ambience_camp_center_night fadein 3
    scene bg ext_entrance_night_clear_7dl
    show owl behind prologue_dream:
        pos (931, 88)
    show prologue_dream
    with fade3
    "And I don't want to die..."
    "I want to live on the other side of the fence..."
    scene bg ext_entrance_night_clear_7dl
    $ renpy.show("uvao_d1", at_list = [left], what = Notch("uvao_d1"))
    show prologue_dream
    with fade3
    show alt_credits "Will you go with me?" with dissolve2:
        pos (747,105)
    pause(3)
    scene bg ext_entrance_night_clear_7dl
    $ renpy.show("uvao_d1", at_list = [left], what = Notch("uvao_d1"))
    show prologue_dream
    with dissolve
    dv "I'll go anywhere if they're all not there."
    scene bg ext_entrance_night_clear_7dl
    show prologue_dream
    with dissolve2
    "Someone picked me up in their arms and carried me."
    "The pain was gone: it was warm and cozy."
    "Maybe it was my mother who came to take me to heaven."
    stop ambience fadeout 6
    scene black
    show prologue_dream
    with dissolve
    "I clutched the Tamagotchi in my hand and pressed my cheek against my mother's."
    stop music fadeout 5
    "Too many wishes came true on this birthday."
    scene black with dissolve
    $ alt_pause(3.5)
    play ambience ambience_camp_center_day fadein 4
    $ alt_pause(1)
    scene bg ext_sky2_7dl
    show unblink
    with dissolve
    $ day_time()
    "I woke up to someone screaming."
    "Summer. Sunshine."
    "And kids in pioneer uniforms - little kids about seven years old."
    "And Mom wasn't there."
    dv "No! I don't want to!"
    dv "Take me back! It's not fair!"
    dv "I don't want to live in heaven, I want to go to earth!"
    "The kids ran away."
    "I fell to the ground and cried."
    "I thought that's where my mom and dad would meet me..."
    stop ambience fadeout 1
    $ alt_pause(1)
    scene bg int_ward_sunset_kns with dissolve
    $ set_mode_nvl()
    $ meet('voice','Doctor')
    play music music_7dl["sky_feather"] fadein 3
    voice "There has been a complete substitution. I'm afraid there's nothing we can do."
    voice "PCR syndrome is rare in children."
    voice "It's a serious blow to their fragile psyche, especially if the visitor is older. And the girl says she's ten."
    nvl clear
    "I've been in the hospital for a very long time."
    "The doctors examined me and asked me strange questions."
    "Either they thought I was very stupid, or they were very stupid themselves if they didn't know what year it was."
    nvl clear
    "Also, an uncle and an aunt came by."
    "Very familiar looking, but I had no idea who they were."
    "Aunt was crying, and uncle was looking at me like an angry policeman at a criminal."
    "And now they were talking to the doctors in the hallway, thinking I was asleep."
    voice "We can try to get your daughter's memories out, but it won't bring her back."
    "The aunt began to cry. And the uncle started talking:"
    $ meet('ase','Man')
    ase "In that case, we are ready to write a waiver."
    ase "We can't raise someone else's child by seeing our daughter's face in front of us."
    $ meet('ase','Alisa')
    $ meet('voice','Voice')
    "They all left, and I turned my back against the wall, tears rolling down my face against my will."
    "Somehow I felt as if these vaguely familiar uncle and aunt had betrayed me."
    stop music fadeout 4
    $ alt_pause(2)
    $ set_mode_adv()
    scene bg int_ward_day_kns with dissolve2
    $ meet('hg','Man')
    play music music_7dl["youarenotalone"] fadein 4
    hg "Well hello, Alisa."
    "There's a man sitting on my bed."
    "I looked at him languidly."
    "These awful pills made me want to sleep all the time."
    "I can't wait to be discharged..."
    hg "Let's get acquainted."
    hg "My name is Vikentiy."
    $ meet('hg','Vikentiy')
    hg "I have a wife, her name is Olesya. Almost like you."
    hg "How old are you?"
    dv "Seven...{w} No, eight."
    dv "It was my birthday the other day."
    hg "Really? And I have just the present for you!"
    "The man held out a toy bear to me, and I hugged this unexpected gift unabashedly."
    hg "And what city are you from?"
    dv "From Leningrad. And you?"
    hg "From Kalinin."
    hg "My wife and I want to be your mom and dad."
    "Mom and Dad..."
    "It must be a dream."
    "The medication made it hard for me to know what was real, what I was dreaming and what I was imagining."
    hg "We'll come get you tomorrow. Do you want to come with us?"
    dv "Yes."
    $ meet('hg','Guy')
    show blink
    "My eyes finally closed, and I felt someone stroking my head affectionately."
    "Even if it is a dream, let it last longer."
    scene bg ext_entrance_night_clear_closed_7dl
    show prologue_dream
    with dissolve2
    "Maybe, at least in a dream, I'll see what life is like on the other side of the fence."
    play sound sfx_7dl["gate_open"]
    scene bg ext_entrance_night_clear_7dl with dissolve2
    stop sound fadeout 1
    pause(1)
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("dv_dj_true")
    show acm_logo_dv_dj_true with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    pause(1)
    return