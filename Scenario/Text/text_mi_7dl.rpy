label alt_day4_mi_7dl_ch1:
    scene cg d4_cs_car_dark_7dl
    "The car had already cooled down a bit after the heat of the day, so it was pleasant enough inside."
    "Whether by habit or for some other reason, I instantly took a seat in the front seat - the road was going to be quite long, and I didn't want to miss the opportunity to stretch my legs."
    "Shurik was already seated behind me, on the driver's side."
    if alt_day3_mi_7dl_donor:
        "Behind my back..."
        "Goosebumps marched down my neck in rows toward my hairline - I felt the warmth of Miku's breath on my skin."
        mi "Nya!"
        "The girl smiled, grabbing the back of my chair with her hands and resting her chin on it somehow very snugly."
        "Catching my questioning look, she smiled:"
        with fade
        mi "What's wrong? I've been riding in the back seat all my life - I'm used to it."
        me "Will you keep an eye on Shurik, if anything?"
        "Miku didn't have time to answer me - our driver appeared nearby."
    cs "That's it, I've sorted out all the difficulties with Olya."
    "Nurse exhaled, plumping on the seat."
    cs "But so that you don't hide anywhere, you got it..."
    if alt_day3_mi_7dl_donor:
        extend " pioneers?"
        "We looked at each other and answered in one voice:"
        me "Roger."
        mi "Will do."
    else:
        extend " pioneer?"
        "I shrugged."
        "Like I'd really want to go anywhere from the only person I'd ever know in town."
        "No way. I'll hold on to the hem until we leave."
        th "Hussars, be quiet."
    cs "I'll be driving."
    "Viola answered the unspoken question."
    cs "So you'd better fasten your seat belts."
    me "Huh?"
    "She understood my question."
    "And grinned."
    cs "Don't worry about the precious cargo - I've got him properly fastened."
    me "He said «let's go»!"
    if alt_day3_mi_7dl_donor:
        mi "And waved!"
        "With enthusiasm Miku picked up on it."
        mi "Ow!"
        "And immediately covered her mouth with her hands."
        "Squinted at Shurik's disgruntled snort and took a breath."
    "Violetta, who had been patiently waiting for the end of the performance, sighed and turned the key."
    cs "I hope we don't have to stop for urgent business."
    "In a whisper she muttered, turning into first gear."
    scene cg d4_cs_car_night_cs_7dl
    with fade
    stop ambience
    play music music_list["into_the_unknown"] fadein 3
    play sound sfx_intro_bus_engine_start
    "«Volga» drove out of the gate and, with a short roar of the engine, sprinted forward."
    "I, overcoming a growing overload, looked respectfully at the nurse holding the steering wheel calmly - it was obvious that she likes to drive and knows how to drive."
    "Or rather, not just drive, but drive extremely."
    "The road allowed it."
    "That's what bothered me."
    "After all, I remembered what country I was living in, what country I was in."
    play sound_loop sfx_intro_bus_engine_loop fadein 3
    "And I knew three Russian woes by name - fools, roads, and..."
    dreamgirl "Watch out!"
    if alt_day3_mi_7dl_donor:
        "In one voice shouted the inner voice and Miku."
    else:
        "I voiced my inner voice."
    "There's a pothole right on course."
    "Viola gritted through her teeth some incomprehensible, obviously non-Russian word - either 'bridge' or 'anchorage' - and nodded:"
    cs "Thank you."
    cs "Keep your eyes open, pioneer, in case you notice anything."
    "Without taking her eyes off the road, threw Viola."
    th "You don't have to say."
    "Even by the humblest of standards, the car was going a hundred kilometers an hour over the unprecedentedly smooth asphalt."
    "I wish I had music now, but I'm afraid they won't appreciate it."
    "There was something creepy about the way we drove down the highway in silence, broken only by the hum of the engine."
    "If you ask me, only a suicidal person would drive like that on a country road at night."
    "Or Violetta Cernovna Collider."
    "Sensing my gaze, nurse explained:"
    cs "We don't have much time, the pioneer needs the supervision of someone who deals with such wounds."
    me "You don't?"
    "She only rolled her eyes in response."
    if alt_day3_mi_7dl_donor:
        "And I got hit in the ear not hard, but soundly - with a flick:"
        mi "Semyon, don't distract Violetta-san, or my corpse will be on your conscience!"
        me "A very charming corpse."
        mi "Don't worry, you won't outlive me for long."
        "The girl smiled sweetly and went back to watching the road."
    "The interior smelled pungently of gasoline, upholstered in what looked like the hide of the dreaded Leatherman beast."
    "And the everpresent «pines»."
    "For the time being, this should help combat the odor of the antiseptic ointment."
    if alt_day3_mi_7dl_donor:
        "But Miku was already wrinkling her nose, so my turn was near."
    me "Don't you have a radio?"
    "After half an hour of vigil, I asked - my throat gave out a squeak from habit, faintly resembling my usual voice."
    cs "There is. Would you like to hear it?"
    cs "Only you're not likely to catch anything here."
    th "I suppose a thing like a universal bus input isn't worth mentioning?"
    dreamgirl "You should have asked about CDs or cassettes, you dumbass!"
    th "Why? Tapes were already there at that time - remember Miku's tape recorder!"
    dreamgirl "And if you look closely?"
    dreamgirl "The inscription «Sony» doesn't lead you to any conclusions?"
    th "Eh?"
    dreamgirl "Eheh! That's Miku's tape recorder, she owns the tapes, too."
    dreamgirl "And here you can only count on a reel-to-reel player."
    "I imagined the picture of tucking in a reel in the dark, and decided I was fine without music."
    me "I'll give it a try, though."
    "Reluctantly I said."
    "Violetta silently jerked her shoulder - go ahead."
    with fade2
    "Sizzle."
    "You betcha."
    "I glanced at my watch - the time was close to one o'clock, so we'd successfully gotten about a hundred and fifty kilometers away from camp."
    "But here, too, there were definite difficulties in receiving any radio signals."
    "Satellite communications might have worked here - but not in the publicly available format I'm used to."
    "There was hissing again - on both VHF bands."
    "I decided not to check any others."
    "I know from my own childhood experience that every possible frequency on that band is occupied by the chatter of impotent creative types."
    "Let them."
    "I turned off the receiver."
    cs "Convinced?"
    me "You didn't have to ask."
    if alt_day3_mi_7dl_donor:
        mi "Senechka, what kind of music do you listen to?"
        "I shrugged."
        me "Beautiful."
        mi "I mean it!"
        "She poked me in the back of the head with her fist."
        mi "Why are you always making fun of everyone?"
        me "I'm murderously serious."
        "I answered."
        mi "There! Here you go again!"
        "She exclaimed."
        "And again she let out some inarticulate exhale as mumbling came from Shurik's side."
        mi "You're making me yell again! How can you do this!"
        th "Okay. I don't need an international scandal."
        "I tried to calm down."
        th "Besides, if I go in to strangle her now, I might interfere with Viola's driving and we'll tumble into a ditch."
        th "At our speed, we risk turning into eggnog."
        "And so I took a few deep breaths and exhales."
        "And tried it first:"
        me "So what did you want to talk about, Miku?"
        mi "Rrrr... Nothing! That's it!"
        "The fingers that had been clutching the supports of my headrest all this time loosened and retracted."
        "Their pop highness has deigned to be angry."
        "Oh nooooo."
        "There was a slightly tense but welcome silence in the cabin."
    me "I'll sleep while we're on the road, okay?"
    "I said to nothing."
    me "When we arrive - push me, please."
    "Moscow time is two in the morning."
    scene bg ext_road_night with dissolve
    "The Hour of the Bull."
    "A time to listen more closely to your own intuition."
    "And it told me I should sleep now."
    "For the transition always goes better if you let it pass your mind."
    "Everything will take its course in strict accordance with the chain of cause and effect."
    "Which means that morning awaits me in the city..."
    show blinking
    "I yawned, thinking in passing that I still didn't learn the name of the settlement."
    "And I should ask..."
    "Halfway through, I passed out."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_7dl_ch2:
    scene cg d4_cs_car_day_cs_7dl with dissolve
    play music music_7dl["rewind"] fadein 3
    "I'm tired. Tired."
    "Sometimes it seems like there's nothing to make you survive anymore - to exhale and get up."
    "Like hell there is."
    "My neck was stiff from the uncomfortable position, it felt like it was about to break."
    "For a second I thought about how great it would be to just break my neck and go for another spin on the wheel of Sansara."
    "I used to have that sin of playing at something, getting to a certain level and position, and then doing a reset."
    "And start over again."
    "A return to innocence of sorts. Too bad it never worked in my life."
    "But since I soon found myself in an obscure dimension, on obscure coordinates - maybe I'm the one who's already... that? Heh?"
    "With a chuckle, I allowed myself to wake up after all."
    "Judging by the hand trembling on the torpedo, the Moscow time was 5:00 a.m. - arrgh, I'd sleep and sleep."
    cs "Another ten minutes and we'll be there."
    "Viola unmistakably identified my awakening."
    cs "Yes, you were snoring."
    "She answered an unspoken question."
    if alt_day3_mi_7dl_donor:
        cs "Good thing you didn't wake up the others."
    cs "Look, how's the little brat?"
    "I obediently turned around and gave the hero of the day a hard look."
    "Shurik was sniffing his nose through the side window, overdosed on painkillers, and a thin line of saliva was dripping down from the corner of his mouth."
    dreamgirl "What an abomination!"
    th "Good morning to you, too."
    dreamgirl "Uh-huh."
    if alt_day3_mi_7dl_donor:
        "I checked on Miku - she was asleep, too."
    "For lack of a better occupation, I stared out the window - the broken rectangular outlines of buildings did loom on the horizon - so we managed to get there, for better or for worse."
    "And ten minutes later, we did enter the city."
    "Twenty minutes later - Viola steered the car confidently under an archway with a huge blue sign that said 'City Hospital.'"
    "Two minutes, and we stopped at the downward steps."
    cs "That's it. Good morning!"
    "She greeted us and turned off the engine."
    stop sound_loop fadeout 1
    scene bg ext_hospital2_away_day_7dl
    with dissolve
    play ambience ambience_7dl["town_day"] fadein 3
    play music music_list["my_daily_life"] fadein 5
    "Behind my back someone grumbled something unhappily, turned around."
    "But «Volga» was a car suitable for anything that wasn't sleeping."
    "So, after sighing, we had to vacate the cabin."
    if alt_day3_mi_7dl_donor:
        "Miku didn't look happy."
        show mi upset pioneer with dspr
        mi "You could have gone slower."
        "She muttered."
        "And only now did she notice me."
        mi "Oh, good morning."
        me "Gweetingws."
        "I greeted her with a nod."
        me "How did you sleep?"
        mi "Don't ask. Didn't get much sleep. Can I go back to the salon?"
    show cs normal at left with dissolve
    cs "Don't even think about going to bed."
    "The nurse warned her, sensing the criminal intent."
    cs "Business first, all nonsense later."
    "She was right - Shurik was shaking, hardly able to make it up the stairs on his own."
    "What's more, I suspect he would have dropped Viola, too, had she taken it up to support him."
    "So if I had any doubts as to the purpose of my being here, they have now dissipated."
    "The purpose was utilitarian and thoroughly mercantile."
    "With a sigh, I stepped up to Shurik and threw his wounded arm over my neck."
    if alt_day3_mi_7dl_donor:
        "Miku wanted to join in as well, but I gave her such a stare that she obediently retreated, not daring to argue."
    me "And! One step for Mom, one step for Dad..."
    hide mi
    hide cs
    with fade
    "I didn't count the number of steps on purpose, but usually some sort of rhythm was needed for a long climb."
    "Step — help Shurik take a step — hold his hand — catch the balance so the crumpled pioneer doesn't fall backwards."
    me "Instead of heat - the green of glass!"
    "I groaned already on the eleventh step."
    "Shurik, pale to blue, was dangling in the wind and torn to pieces."
    me "Instead of fire, smoke! From the grid of the calendar the day is snatched!"
    "No portwine, of course, but about the day - that was a good point. A whole day would be wasted. And why?"
    "Because a foolish pioneer imagined himself a migrating bird."
    "I could hardly resist the temptation to punch the bespectacled man in the ribs, especially since he was tumbling again, and we both almost went down."
    "But it all comes to an end sometime."
    play sound sfx_open_door_2
    "The door creaked softly, the tensioning spring hummed - archaic doors..."
    stop ambience fadeout 6
    scene bg int_hospital_hall_day_7dl with dissolve
    play ambience ambience_int_cabin_evening fadein 2
    "And with a sigh of relief I lowered Shurik onto a brown leatherette-covered bench nestled in the corner."
    me "Thank you to me, dear and beloved! Reward myself with a prize, which will go to the fund of starving me and..."
    "I fell silent - a man in a white coat was already rushing through the foyer toward us."
    "He seemed to know Violetta Zernovna quite well, for he immediately took her under his elbow and dragged her after him."
    "He didn't even look in my direction."
    "But this «even» was so prominently significant that I knew by some tenth instinct that this man must know our Sanich, too! How else could it be!"
    if alt_day3_mi_7dl_donor:
        "Miku, unaccustomedly quiet, sat next to Shurik, and I, after a little hesitation, sat down next to him."
        "And then my stomach decided to remind me of itself."
        "I don't think I've eaten anything yet today."
    else:
        "After thinking for a while, I decided not to sit next to Shurik - instead, I chose a bench nearby."
        "I had heard before that concussion of the interstitial ganglion is sometimes accompanied by nausea."
        "And somehow with absolutely no logic, I deduced that I hadn't eaten anything yet myself."
    "But instead of the perfectly legitimate rest and provisions my fading body is entitled to, they made me spend the night shaking in the middle of nowhere, then forced me to do loading and unloading!"
    "Now they ignore me point-blank, too!"
    "Just the right time for getting discouraged."
    "But instead I fell into oblivion - I didn't get enough sleep after all!"
    if alt_day3_mi_7dl_donor:
        "Miku rested her head on my shoulder and went quiet, too."
    "As a matter of fact, the moment when Shurik was lifted up and taken to surgery went unnoticed by me."
    "Although by the logic of events I would have been expected to sit and sweat worrying about my comrade."
    if alt_day3_mi_7dl_donor:
        "Well, that's me and Miku as comrades!"
    else:
        "Well, then, that's the kind of shitty comrade I am!"
    with fade2
    stop music fadeout 3
    "So I thought I covered my eyes just for a moment."
    "And then someone put a hand on my shoulder and shook me gently but insistently."
    scene
    $ renpy.show("bg int_hospital_hall_day_7dl", what = Dawn("bg int_hospital_hall_day_7dl"))
    show cs normal
    with dissolve
    "Viola looked unaccustomedly thoughtful and on her mind."
    "Though if I hadn't been looking for a catch everywhere, I wouldn't have noticed."
    me "Yeah. I'm waking up now."
    "I reluctantly opened my eyes."
    me "What's wrong?"
    play music music_7dl["but_why"] fadein 5
    if alt_day3_mi_7dl_donor:
        "I tried to keep my voice low so as not to disturb Miku's sleep, but she seemed to be already awake."
        "She recoiled from me - I caught her rapidly flushed cheeks and the condescending, understanding look in our vamp-sister's eyes with the peripheral vision."
        cs "That's all right. I'll be here a little while longer, you can go for a walk."
    me "Violetta Cernovna?"
    "Looks like there won't be any problems after all."
    me "Something with Shurik?"
    cs "What? No. It's... It's okay. He's a strong boy."
    show cs shy with dspr
    "I wasn't convinced by her words."
    if alt_day3_mi_7dl_donor:
        "Miku too, as it seems."
        show mi normal pioneer at left with dspr
        mi "Violochka Cernovna, don't deceive us! We rode with you, we seem to have a right to know!"
        cs "Yes?"
        "We nodded in sync."
        cs "Oh, okay."
    else:
        "And that seemed to be written quite eloquently on my face."
    "Viola sighed heavily."
    show cs normal with dspr
    cs "The pioneer has severe blood loss."
    "She began."
    cs "But that's not even a mystery, I suppose. Worse yet, he has a rather rare blood type."
    cs "We've made a request to the bank, but until they send the right batch..."
    me "You make it sound like seconds are everything."
    "I felt like a character in a cheap soap opera, and I didn't like that feeling at all."
    me "Besides, it's a hospital. They don't keep amateurs here."
    cs "That's true."
    "Viola sighed and sat down in the seat that Shurik used to occupy."
    cs "I'm still worried."
    "For some reason my tongue didn't turn to quip or spit out an innuendo."
    "In my life there would have been gossip, someone would have put forward the theory that Violetta and Shurik were meeting secretly from the whole camp..."
    "But here, for some reason, all these thoughts seemed out of place."
    me "You do know that when the doctors start to worry, it's time for the rest of us to order a place in the cemetery and go on foot, so as not to chase the government carriage?"
    show cs smile with dspr
    cs "And I'm only telling it to you."
    "She winked."
    if alt_day3_mi_7dl_donor:
        "Miku next to me snorted resentfully."
    me "And why would you?"
    cs "Because you won't tell anyone?"
    me "I won't tell?"
    cs "If you try to tell, no one will believe you. And I, in turn, know how to remember people who have done me good."
    "She pretended with her fingers to hold a rubber bag and squeezed it sharply."
    me "Ah! Ahem. That's right, I won't tell anyone."
    "As long as she presented it that way..."
    me "Okay. I get it. You're worried."
    me "What do you want from me?"
    show cs normal with dspr
    cs "It's nothing. I'm just waiting for the car from the blood bank to arrive, and in the meantime I'm chatting."
    cs "I'm nervous, you know?"
    "I froze and exhaled."
    menu:
        "I understand":
            "Viola couldn't ask me to do those things. No one could."
            "This is such an intimate and personal matter that no one has the right to tell anyone."
            "And I was disgusted by the idea of giving away my own life - and there was nothing critical looming on the horizon."
            th "Viola said so herself. She wouldn't lie, would she?"
            th "Or would she?"
            cs "Well, there you go."
            "She was looking straight ahead."
            cs "I really wish I'd studied to be a normal doctor. {w}Not like this. Psycho."
            "She got up."
            cs "Okay, thanks for the company, I'll go check on the package."
            hide cs with dissolve
            "She disappeared out the door."
            if alt_day3_mi_7dl_donor:
                show mi upset pioneer with dspr
                mi "You know, Senechka."
                "Thoughtfully stretched out Miku."
                mi "I think she didn't tell us everything."
                me "Uh-huh."
                "I agreeingly replied to her."
                mi "Maybe we..."
                me "No."
                mi "But I..."
                me "I said no."
                show mi angry pioneer with dspr
                mi "What are you telling me to do!"
                me "All right. {w}Okay, mein lieben. Go and do right."
                me "You know the right way, don't you?"
                show mi normal pioneer with dspr
                "Miku hesitated."
                "And a few seconds of reflection later, she sat down next to me again."
                mi "Don't think you've won."
                "The Japanese girl warned."
                me "Yeah."
        "I seem to be B-negative":
            "Unless, of course, I'm confused."
            me "You want me to..."
            cs "No, I don't."
            "Nurse hanged her head."
            cs "Need an O. Eh."
            hide cs
            with fade
            "Shaking her head, she got up and disappeared out the door."
            if alt_day3_mi_7dl_donor:
                $ lp_mi += 1
                mi "Why didn't anyone ask me?"
                "Miku resented."
                me "Because I weigh three times as much as you do, and it would be totally non-lethal for me to turn in a pint of liquids in case of an emergency."
                show mi smile pioneer with dspr
                mi "Me too!"
                me "Yes?"
                "I measured the girl with a long look - head to toe first."
                show mi shy pioneer with dspr
                "Then upside down."
                mi "What?!"
                me "Nothin'. {w}It's just that I don't think you have any experience in this business."
                show mi angry pioneer with dspr
                mi "You don't need experience here! You just lie there!"
                me "In that case, my dear, if your beloved Shurik is suddenly found on the brink of death, you will certainly be called upon."
                me "But only in case of emergency."
                show mi normal pioneer with dspr
                mi "Isn't he now?"
                me "Judging from the fact that Viola is pretty calm? No, he's not."
                me "So take a seat next to me and let's get some more sleep."
                mi "The thought is reasonable. But I don't think I'll be able to sleep now."
                "Nevertheless, she took the seat on the banquette next to me execitively, returned her head to my shoulder, and shifted her eyelids."
            else:
                "I looked her over."
                "It's been a long time since I felt so useless."
                "It occurred to me for the first time that maybe I should have talked Miku into coming with us..."
                $ alt_spt += 1
                "But what's done cannot be undone."
                with fade
        "And… What should we do now?" if alt_day3_mi_7dl_donor:
            "It's really a question of questions."
            "Though usually, in Mother Russia, they always looked for the guilty ones first - that's the mentality."
            "Now, unfortunately, there was absolutely no time for such nonsense."
            stop music fadeout 3
            "And…"
            me "No."
            play music music_list["always_ready"] fadein 5
            show mi happy pioneer with dspr
            mi "Yes!"
            me "You can't…"
            mi "Yes I can!"
            me "Stupid…"
            "Miku gave me a dismissive look."
            mi "No stupider than deciding for others what they can and can't do."
            "And then I shut up."
            "Because I knew what the girl said was right."
            menu:
                "Are you sure you can pull it off?" if herc:
                    $ alt_hpt += 1
                    "I didn't really count on a positive answer, but Miku, after hesitating, nodded."
                    "And in vain."
                    "I hoped to the last minute that she'd backpedal."
                    "Shit."
                    mi "Break a leg, Senechka."
                    "She stood up and walked over to Violetta:"
                    mi "I'm ready."
                    $ alt_day3_mi_7dl_donor = 2
                "Come on! Show them all!" if loki:
                    $ alt_hpt += 1
                    "I suggested."
                    "She smiled and nodded."
                    mi "Thank you for not discouraging me, Seneca."
                    "She got up and walked over to Viola."
                    mi "When do we start?"
                    $ alt_day3_mi_7dl_donor = 2
                "I think that's a bad idea" if dr:
                    $ alt_spt += 1
                    show mi dontlike pioneer with dspr
                    mi "Why not?"
                    me "Because! You're a skinny and dead girl. If you give blood now, you'll carried away by wind."
                    me "Should I walk around then and hold your hand so the wind doesn't carry you away?"
                    "Miku got up."
                    mi "I'll carry bricks in my pockets."
                    "She promised."
                    "And, after showing me her tongue, she disappeared behind the operating room doors."
                    me "Bitch."
                    $ lp_mi += 1
                    mi "Hearing it from a bitchass!"
                    "It came to me."
                    $ alt_day3_mi_7dl_donor = 2
                "Isn't that too much for you?":
                    $ alt_spt += 1
                    mi "But I can save someone's life."
                    "The girl was surprised, as if saving lives was a daily job for her."
                    mi "Why should I refuse?"
                    me "Because it might be dangerous for you - you're so fragile and small."
                    "Miku shook her head stubbornly."
                    "But since I have my word..."
                    me "Besides, there's a concert coming up - are you going to go on stage with a green face?"
                    mi "Why is it green?!"
                    me "Blood loss."
                    "I diligently explained."
                    me "Weakness, nausea, dizziness - and the whole camp will be looking at you."
                    mi "But what about Shurik then?"
                    me "Don't worry about him - he'll be all right."
                    "I spoke with far more confidence than I felt myself."
                    $ alt_day4_mi_7dl_bl_save = True
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_7dl_ch3:
    scene bg int_hospital_hall_day_7dl with dissolve
    play ambience ambience_int_cabin_evening fadein 3
    "I sat on the same miserable banquette and couldn't find my place with anxiety."
    "Of course, I understood that only professionals work here; there is no place for amateurs."
    "That Violetta would inevitably report the rather peculiar status of our guest from the Land of the Rising Sun."
    "After all, they won't kill her there! Not sucked dry like a vampire victim."
    "No, of course not. The very principle of blood transfusion is simply to plug a hole."
    "A 450 gram portion should be enough - there's a reason they call it a medical minimum!"
    "The only question is whether Miku will survive the removal of those very grams."
    "I mean, she's so small. Fragile."
    "Vulnerable."
    "I caught myself thinking that I was reasoning either like a mommy-asshole or a boyfriend-boyfriend, as if I had the right to say and think so."
    "Which really isn't the case."
    "But if one day someone will teach me not to worry about those people who have become dear to me..."
    "And the execution of this «teacher» will be swift and violent. And I'll immediately return my mental status quo."
    play sound sfx_open_door_kick
    pause(1)
    stop music fadeout 4
    show mi rage pioneer with dspr
    "The door slammed, and before I knew it, the one to whom I had just extolled was plumping beside me."
    "To say she was upset would be a grand understatement."
    "Pressing a cotton ball to her pierced ring finger, the living embodiment of frustration sat beside me."
    "I guess she should have given someone a beating to blow off steam, but for lack of alternatives, I had to put up with it."
    "So I had to slowly and carefully talk the girl down."
    play music music_7dl["beasteye"] fadein 3
    "Very slowly and very carefully."
    show mi normal pioneer with dspr
    mi "Senechka, you know..."
    "She began after a few minutes of stomping her feet, gnashing her teeth, and other displays of bad temper."
    mi "This is the first time I've ever decided something for myself - just because it's the right thing to do."
    mi "Not «logical» or «profitable» — but right."
    mi "Pa spent his whole life trying to teach me this - and now that he's succeeded..."
    "She unknowingly clenched and unclenched her fists."
    mi "This is it."
    me "You never told me what happened."
    "For some reason passions like anemia popped into my head."
    "Basically, Miku looked like a small-minded child right now - I wouldn't be surprised."
    "But I decided to leave the dreams of my own mind unspoken - reality itself was knocking at the door."
    mi "I wasn't allowed to be a donor."
    "She reported it."
    me "I understood that. What was the reason?"
    play sound sfx_punch_medium
    with vpunch
    pause(1)
    mi "Blood type."
    show mi sad pioneer with dspr
    "She banged her fist on the seat."
    mi "The second one, Rh negative."
    me "Wow. Same as mine. Do you know what that means?"
    "Miku, who had been feeling down, turned up her nose."
    mi "So what?"
    me "So if something happens, we can help each other! Can you imagine?"
    show mi normal pioneer with dspr
    mi "As if it'll happen..."
    menu:
        "Even if it doesn't happen":
            me "You don't understand the value of the moment."
            me "Not every thing is useless just because it's not useful in the moment, you know?"
            show mi shy pioneer with dspr
            mi "No."
            "Straight up, she answered."
            me "You don't think a bicycle is useless just because you can't ride it in winter, do you?"
            show mi smile pioneer with dspr
            mi "Well..."
            me "There! You don't. Everything has its time and place."
            me "So it is with you - you may not have been able to do any good here and now, but you have learned something about yourself that may help you in the future in a similar situation."
            mi "But I couldn't help."
            "The Japanese girl uttered dejectedly."
            me "First of all, it wasn't a matter of life and death, I assure you."
            me "Because if it were so, Violetta Cernovna herself would have ridden her «Volga» to the unfortunate blood bank — and there'd be scraps of it all over the place. And she's drinking tea in the emergency room."
            me "And secondly, Shurik will know that his comrades were ready to help him even in such a case."
            me "Very good moral support - what do you think this is but help?"
            show mi smile pioneer with dspr
            mi "Yeah... I guess you're right."
            me "Not even «guess»! I am right."
            dreamgirl "Do you really believe what you're saying?"
            th "What difference does it make? Or do you have a better consolation plan?"
            dreamgirl "That's it, I'll shut up."
            $ alt_hpt += 1
        "You did great":
            "I patted her lightly on the shoulder."
            me "I'm very proud of you."
            mi "Uh-huh."
            "She grimaced."
            "She was in a lousy mood."
            $ lp_mi += 1
            $ alt_spt += 1
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_7dl_ch4:
    scene bg int_hospital_hall_day_7dl with dissolve
    play sound sfx_open_door_strong
    pause(1)
    if alt_day3_mi_7dl_donor:
        play music music_7dl["breath_me"] fadein 3
        "We weren't paying any attention to our surroundings during our conversation, so we both flinched in sync when the far glass door clicked loudly, letting out a woman in a white medical gown."
        "It only now occurred to me that our nurse hadn't changed her clothes since Shurik's discovery; as she was still in her usual attire, she had flown in here."
        "She looked peaceful, calm."
    else:
        play music music_7dl["ltyh"] fadein 6
        "Viola caught my eye from the door and nodded reassuringly."
    "Considering she was running away in her most disheveled form, something has stabilized somewhere."
    "And that something..."
    show cs normal at left with dissolve
    cs "The bank called."
    "She reported."
    cs "They were able to find everything they needed, they sent a car."
    me "Uh... Weren't they supposed to send it an hour ago?"
    cs "No. Anyway, it'll be here soon."
    cs "But what am I here anyway..."
    if alt_day3_mi_7dl_donor == 0:
        "She pulled a bunch of keys out of her pocket and tossed it up."
    else:
        "She looked at us again with her {i}regular{/i} look - which I had hoped she had unlearned to do."
    cs "Alexander is being left here as an inpatient in any case."
    cs "The fact is that in addition to the wound and blood loss, he has a concussion. And a few other minor things - in short, he'll definitely be here until August."
    me "No kidding?"
    "I shook my head sympathetically."
    me "Spending half the summer in the hospital is tough."
    cs "Yeah, yeah. Now I'll sort out the formalities, fill out the paperwork and so forth - it'll take at least forty minutes. {w}And I'd like to go home, too."
    me "What about camp?"
    cs "We'll go for sure. But we don't have to go there... right away, do we?"
    cs "Especially since..."
    if alt_day3_mi_7dl_donor == 0:
        cs "Olya left me the keys to the apartment."
        cs "She trusts you enough, I see."
        me "Yeah?"
        "To say I was surprised is nothing to say."
        "Especially since I almost snatched the potential cause of an international scandal out from under her nose."
        cs "If you want, you can go wash up and have a cup of tea, it's not far."
        cs "Do you remember the address?"
        me "No."
        "I answered honestly."
        show cs smile with dspr
        cs "No problem. I'll give it to you."
        cs "I'd see you off myself, but..."
        show cs shy with dspr
        me "No, thanks! I can do it myself!"
        cs "That's great."
        "She took a pen and a notepad out of her pocket, scribbled a few lines, and, tearing off a blue-checkered sheet, handed it to me:"
        cs "You walk out of the building behind the gate, take a left up until Lenin Prospect. You won't get confused there."
        cs "Go up to the fourth floor, first door on the left, dark red door, the top lock closes backwards."
        cs "That's it, adieu... pioneer."
        "She nodded and marched past me into the street, leaving me alone."
    else:
        cs "The weather is quite nice, walk and walk."
        cs "Go get some air, the pioneer knows the town - he'll show you where everything is."
        cs "You can consider it a date."
        "The paint rushed into my face, and Miku's ears were visibly flushed."
        "But for some reason neither rushed to rebuttal."
        show mi laugh pioneer at right with dissolve
        "Instead, we looked at each other and laughed."
        mi "And where in this city can you go?"
        cs "Uh... Figure that out yourselves."
        "Viola hid some kind of key back in her pocket, which she started to pull out, but I didn't pay much attention to it."
        cs "Do you have any money for the cafe stuff?"
        "Cautiously she inquired."
        show mi smile pioneer with dspr
        mi "Yes, of course."
        "Chirped Miku."
        mi "I traded some yen before I came here - I wanted to buy something to remember the trip."
        cs "That's great."
        cs "In that case, I'll see you in... three hours for the walk is enough?"
        "We nodded."
        cs "Then we'll meet back here at one o'clock. That's it, now adieu."
        "She bowed to us and marched out in formation."
        "With a glance, we giggled and followed her out."
    stop music fadeout 3
    play sound sfx_open_door_clubs fadein 0
    pause(1)
    scene bg ext_townscape_ph_day_7dl with flash
    return

label alt_day4_mi_7dl_ch5a:
    scene bg ext_townscape_ph_day_7dl with dspr
    play ambience ambience_7dl["town_day"] fadein 3
    play music music_7dl["sky_feather"] fadein 3
    "The town says «fly» — and generously tosses the wind beneath stumbling wings."
    "These towns always seem much closer to the sky than the high-rise buildings of the metropolises."
    "You can smell the skyline when the summer sun is just beginning to warm the air, and you can still feel the breath of night in the cozy half-dark corners."
    "It smells of fresh grass and freedom and utter unwillingness to think about consequences."
    "It is known that the first step into the sky begins at the ground, which means that children are closer to the sky than adults."
    "And so are these low towns."
    "If it's gloomy overhead, it rests on your shoulders, the moon can be held in the palm of your hand, and the clouds can be seen down to the smallest detail."
    "And when a needle stretches thirty stories into the sky beside you, the fascination is willy-nilly you compare scales, you look at the height..."
    "When I got out on the road, I found that down to Lenin Prospect led a narrow two-lane road, which was, for the occasion of morning and summer, empty."
    "So how could I deny myself so little as to get out to the very center of the roadway and, after taking a souvenir picture, head leisurely down."
    "I've been walking like that all my life at night."
    "I guess that's why I never got a car - I liked to think that the road belonged to me personally, not to the snorting mechanism."
    "The sleepy, lazy mood that is characteristic only of the outback - here on the right, almost at the very corner, stood an open «Milk» store, but the cashier, instead of huddling behind the counter, went out, put her stool out in the sun, and took a sunbath."
    "As we raced here, I don't remember it raining - though I slept a good half of the way, I might have missed it."
    "But in some places the asphalt was wet, which suggested that there were washing trucks crawling along the roadway in the morning, too."
    "I stood at the intersection and automatically started looking around."
    "It's funny even, because the whole time I didn't meet a single car."
    "I stepped out onto the road, looking at the building numbers."
    "At that very moment, I heard the engine roar, and I turned around and saw a car rushing toward me."
    show blink
    "I closed my eyes…"
    play sound sfx_7dl["car_brake"]
    "And heard a sharp screech of brakes."
    "Before I could open my eyes, another second later, something huge and clanking came from behind me."
    dreamgirl "How long will you wait to die? You're still on the road, stupid!"
    hide blink
    show unblink
    "I opened my eyes."
    "«Mitsubishi», which came from some unknown place in these parts, was standing a meter away from me, and the heat was rising from its hood."
    "The man in the business suit and sunglasses just raised his hand in apology."
    "I nodded back and made my way to the sidewalk."
    th "So much for the sleepy backwater town."
    dreamgirl "That's a diagnosis! Even here you managed to find some adventure for your..."
    th "Screw you!"
    dreamgirl "Okay, even though you didn't do it on purpose, you still saved that guy from an accident. At least you'll have something to be proud of."
    "I took a deep breath and hurried to my destination."
    with fade2
    "House number seven on Lenin Prospect turned out to be a four-story blue house with a claim to sophistication."
    "Anyway, all those columns of supposedly marble, the bay windows-balconies..."
    dreamgirl "Yeah."
    th "Shush."
    "The inner voice with its silly remarks completely threw me off balance, so I had to rewind the mental chain back a few links, because thinking about how I came to those conclusions..."
    "As a result, I spat and admitted to myself - yes, I would definitely like living here."
    "Coming out of the driveway in the morning for a jog, saying hello to the grannies in the driveway - not unlike other houses, not at all mean - to stop by on the way to the store for small things."
    "The windows face the yard, so no noise of passing cars, no dust, no dirt."
    "There were no grannies in the driveway, and nothing prevented me from walking to the door."
    play sound sfx_open_door_2
    pause(1)
    scene bg int_access2_day_7dl with dissolve
    "A few seconds later, I was in the entryway."
    "No elevator, of course."
    "But the steps were precisely built, and it was easy and comfortable to walk up them - or maybe it was because I hadn't killed my body by sitting in front of a computer yet."
    "And a few minutes later I was in front of the dark red door I was looking for."
    th "Well, shall we see how the squad leaders live?"
    dreamgirl "Come on!"
    "And…"
    play sound sfx_open_door_2
    "The hallway was just like a hallway - nothing unusual."
    "Hangers of clothes that haven't come in handy in any way yet, but will definitely be needed in the future."
    "Shoes, umbrellas."
    "A dainty hat, who knows how it came to be here."
    "Standard interior of a standard apartment, seen one - seen all."
    "There were two rooms in the apartment. The door to the first, painted white, was closed, and on the door hung a hand-drawn road «brick», even lower - the Jolly Roger."
    if alt_day2_dv_us_house_visited or alt_day2_us_shenan:
        "An exact replica of the one that draped the glass doors at Alisa's house."
    "I opened the door - and then closed it at once."
    "It was obviously Olga's room. Because the mess there looked a lot like what was going on in our cabin."
    "It's a blessing in disguise, and if I went in there now, I'd risk incurring displeasure."
    dreamgirl "Who's going to know what?!"
    th "I will."
    dreamgirl "Don't tell me you're worried about someone else's trust?"
    th "No, it doesn't bother me. But when it comes to Olga - for some reason I don't dare to do anything stupid."
    dreamgirl "Well, maybe..."
    th "Well, what am I going to do there? Make a fetishist out of myself, looking at her laces?"
    th "Thank you, no."
    "I walked away from the first door."
    stop music fadeout 6
    "The second one was slightly ajar, and I looked inside."
    "And froze."
    play music music_7dl["so_cold"] fadein 3
    scene bg int_mt_sam_room_away_7dl with fade
    "Because on the other side of the door was a room I once saw in a dream."
    "Or been in it in my mind."
    "Of course, you could have written it off as typical construction, typical furniture, typical layout, but..."
    "Hell, everything in my house is exactly the same, except for the computer and the posters on the walls..."
    "Gee."
    scene bg int_mt_sam_room_7dl with dissolve2
    "I went into the room and looked around."
    "The disjointed 'typical,' 'one-size-fits-all,' 'standardization,' swirled reassuringly in my head."
    "And I'd like to believe it. If it weren't for the empty window seat that would one day be taken over by a computer desk, the closet space, the wallpaper that was already starting to peel a little from the top."
    "To sum up: I was now looking at the starting point, the zero meridian, from which the history of my room danced."
    "I didn't play soccer, but every self-respecting kid had a ball."
    "Somewhere in the mezzanine there was a volleyball, and I used the latter a lot more."
    "In fact, so much so that its sides were peeling and flaky - and one far from perfect day it gave me a 'hernia,' for which it was mercilessly deflated and put into harnesses for slingshots."
    "I walked along the bed, checked the almost non-existent layer of dust on its headboard with my finger, on the table, looked at the books, each of which I had reread a dozen times."
    me "Am I home?"
    "I asked myself."
    scene bg int_mt_sam_room_close_7dl
    with fade2
    me "I'm home."
    "Dropping my clothes on the bed, I went to the kitchen, where for fifteen minutes I fought with the gas burner."
    "Then, spitting, I stopped trying to get it right, and then it all went by itself: the slings took their proper places, and the blue gas light winked at me in the enameled womb."
    "And the water ran hot."
    "And I went to the bathroom."
    with dissolve
    play sound sfx_open_water_sink
    pause(1)
    play sound_loop sfx_water_sink_stream
    "Nice!"
    "Who knew what a treat it was to just take a bath!"
    "Not under an icy footwash, not in a river."
    "But civilized, under a hot shower!"
    "Replacement boxers were found where I expected to find them-the second shelf from the top, underwear on the left, socks on the right."
    "Everything here obeyed my logic."
    "Tired of being surprised."
    stop sound_loop
    play sound sfx_close_water_sink
    with fade
    "Bearing in mind that it was thirty degrees outside, I washed under the hottest water I could tolerate."
    "And, having finished cleansing my soul, conscience, and body, I decided to think about other innocent needs."
    "No, I did not go to Olga's room to study her lace-up, as my inner voice advised me again."
    "My path led to the kitchen, where my best friend was waiting for me on my left hand from the entrance — yellowish «Minsk»."
    "As I was, in my trophy boxers, I strode barefoot across the linoleum tile and pulled the handle..."
    scene
    $ renpy.show("bg int_mt_sam_room_away_7dl", what = Desat1("bg int_mt_sam_room_away_7dl"))
    with fade2
    me "Should've expected that."
    "I sighed."
    "The refrigerator was empty."
    "The mouse hanged itself."
    "Mamai has passed by."
    "Except for the lid with the activated charcoal and some paper that the lid was holding on to, there was nothing."
    "Out of the freezer some fishy creature grimaced at me, but I wasn't that hungry yet."
    "If only there were dumplings..."
    "Out of desperation, I pulled a piece of paper."
    $ set_mode_nvl()
    "On a fourfold folded ruled page, in beautiful round letters, it read:"
    "«Salute to the slackers!»"
    "«Don't be too frightened, I won't be here until the twenty-seventh, so the money is where it always is - don't sit around hungry, go to the store, buy and cook yourself something decent!»"
    "«If you don't have enough, you can borrow from Auntie Shura, she won't say no.»."
    "«Ok, kisses, bye-bye.»."
    "«Your Comet»."
    "«P.S.: Yeah, and if possible, don't fight with the neighbors, Dim, they're just starting to forget what you look like»."
    nvl clear
    pause(1)
    $ set_mode_adv()
    me "Dim?"
    "Pitifully I asked."
    "It made me feel silly."
    me "But my name is Semyon..."
    dreamgirl "And you really wanted to have a mystical story around your precious person?"
    "Bitterly grinned the inner voice."
    dreamgirl "As if she'd always waited for you, was only loyal to you, and generally planned for you to go to town."
    th "No, of course not. But some Dima... I mean she has a young man, a fiancé or a husband..."
    dreamgirl "Or a brother."
    th "Also an option, yes. Anyway, why was I given the keys and let into an apartment that's somewhat unoccupied?"
    dreamgirl "And why not? A couple of hours, you won't eat much, you won't have time to burn the house down."
    dreamgirl "It's no trouble for Olga, and it's a pleasure for you."
    dreamgirl "Okay, let's break the inhibitions of our kindest counselor!"
    th "Ah?"
    dreamgirl "Beh. Can you guess where the tea and cookies are?"
    "I obediently grunted and, after filling the kettle with water, I put it on the gas."
    stop ambience fadeout 3
    stop music fadeout 4
    scene bg ext_townscape_ph_day_7dl
    show cs normal
    with dissolve
    play ambience ambience_7dl["town_day"] fadein 3
    "And another hour later, I nodded at Viola, handing her the key."
    cs "Had a nice time?"
    "She asked."
    me "Thank you."
    cs "Let's go, shall we?"
    me "I'll take the back, okay?"
    cs "Sure. I won't be speeding back. You'll get a good night's sleep... pioneer."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_7dl_ch5b:
    scene bg ext_townscape_ph_day_7dl with dspr
    play ambience ambience_7dl["town_day"] fadein 3
    "So we ended up on the street."
    "Me."
    "And Miku."
    if alt_day3_mi_7dl_donor == 2:
        "With a pierced finger."
    play music music_7dl["what_am_i_doing_here"] fadein 5
    show mi shy pioneer with dspr
    mi "About the cafe, by the way, I like the idea."
    "She stroked her stomach and looked at me pitifully."
    mi "Huuuuuungry."
    "Complained Miku."
    me "Uh-huh."
    "I felt a little uncomfortable."
    "And it wasn't because this was, strictly speaking, my first - albeit impromptu - date in years."
    "It just turned out I was broke and couldn't even give my date a bouquet of daisies."
    "How could this happen to me?!"
    show mi laugh pioneer with dspr
    mi "Don't worry about the money."
    "Quite rightly she understood my hesitation."
    mi "They gave it to me for just such an occasion. I was thinking of buying a souvenir, but I have enough for that and ice cream, don't I?"
    "And then I was like: «No! You can't! Let's use your money for good deeds, and we'll starve ourselves!"
    "Of course!"
    with fade
    "I turned sideways to her:"
    me "Your hand, madam!"
    "Miku smiled and held out her palm to me."
    with fade2
    me "I wonder..."
    "Said I, as we got a little farther away from the hospital, and the first stupor-embarrassment began to let go little by little."
    me "What kind of souvenirs were you planning to bring back home from the Union?"
    me "Did you plan to bring back some matryoshka dolls and an ushanka?"
    show mi laugh pioneer with dissolve
    mi "No, but the idea is very cute!"
    me "Really?"
    mi "Yes! {w}I saw a picture of Pa's in a mahalla like that somewhere in the winter."
    mi "I wish he'd brought it! I would have loved to wear it."
    "A girl's heart is in the dark. Personally, I found earflaps ugly to the point of being horrendous."
    show mi shy pioneer with dspr
    mi "But to be honest - I enjoy shopping more than buying things."
    mi "Exploring new territories, you know?"
    show mi dontlike pioneer with dspr
    mi "But in my homeland, I can't just walk around. Not anymore."
    mi "If I go in and don't buy something, then I'll offend the owner."
    me "And if you travel incognito?"
    show mi laugh pioneer with dspr
    mi "Senechka, of course you're smart, but..."
    me "The whole of Japan knows your face, yes."
    show mi normal pioneer with dspr
    mi "And right next to my music school they built a new shopping mall..."
    "She sighed dreamily:"
    mi "Do you like shopping, Senechka?"
    "She stunned me with a question."
    me "How do I tell you..."
    "I didn't immediately come up with an answer."
    me "I've never treated shopping as a fun thing to do."
    show mi happy pioneer with dspr
    mi "Don't be so embarrassed. {w}You men are a lot duller in many ways."
    me "That's called «optimization». Besides, I told you I wouldn't mind keeping you company. Although I'm not a fan of shopping."
    mi "No! Shopping is fun either way!"
    "I rolled my eyes and sighed."
    me "Whatever your highness says!"
    show mi serious pioneer with dspr
    mi "So I say so! Come on!"
    "She pulled me down the street with her."
    scene
    $ renpy.show("bg ext_townscape_ph_day_7dl", what = Dawn("bg ext_townscape_ph_day_7dl"))
    with dissolve
    "I highly doubted she could quench her buying thirst."
    "But should I really clip her wings on takeoff?"
    me "See any trading rows anywhere?"
    "I asked."
    show mi happy pioneer with dspr
    mi "Senechka!"
    "Miku wagged her finger at me."
    mi "I'm from another country, but don't think I'm stupid."
    mi "I'll go to the capital for souvenirs! But that will be after the shift."
    me "Can't even make a joke."
    show mi smile pioneer with dspr
    mi "You can. And that's the only reason I didn't get mad at your babbling."
    "And what do I do with her when she's like that?"
    me "Then why are we going anywhere at all?"
    show mi grin pioneer with dspr
    mi "Process!"
    "The girl raised her finger meaningfully."
    mi "It's the process that counts in our business!"
    mi "I can see the cafe from here - but that's no reason to run to it."
    me "And hunger? Hunger is an excuse?"
    show mi serious pioneer with dspr
    mi "You haven't fainted from hunger yet. So be patient and don't complain."
    dreamgirl "Now, if you're done bickering - can we go somewhere already?"
    "We stopped on the road again."
    "Perhaps we shouldn't have gone out together?"
    "Miku is very absent-minded, and I'm a loser. The two of us could get into trouble together."
    me "So you and I are just going out, that's all?"
    "The sound of the words cut my ear."
    stop music fadeout 3
    "«You and I are just going out», huh?"
    "And why am I worried?"
    play music music_7dl["take_my_hand"] fadein 3
    "Real rrrromance, eh?"
    "Gentlemen Albatrosses in white uniforms, girls flapping bonnets into the sky, and the solemn carcass at the Gagarin's descent into the cold dock from the slipways..."
    "Only I'm not the same."
    "And the place?"
    "I'm sure the local youth find their own inexplicable charm in all those hills and gullies, the uneven development and the whole three selpos."
    "Perhaps they ride motorcycles here?"
    "Maybe they just don't pay attention to the neighborhood and get out every weekend to the nearest big town?"
    "I don't know."
    "But Miku clearly doesn't belong here."
    "She thought otherwise, though."
    "She almost opened her mouth in curiosity and walked forward, looking at everything, peering into almost every corner."
    scene bg ext_townscape_ph_day_7dl
    with fade
    "If you give her a «Nikon» — you cwon't be able to tell the difference from those lively guys who scatter out of huge, tinted buses on Dvortsovaya Street every year and shuffle around the neighborhood."
    "And they're not afraid of getting lost!"
    "Miku certainly wasn't afraid to get lost."
    mi "Step wider, Senechka!"
    "Encouraged, she saw the glass window and immediately hurried toward it."
    "From behind the glass a mannequin with a peeling nose looked at her reproachfully, and the girl did not hold back a disappointed exclamation."
    me "Not the capital, yes."
    "She stood for a while, looking in the window, and then, with a sigh, she asked:"
    mi "Aren't you going to the capital yourself?"
    me "No. And why would I?"
    "I shrugged."
    "The opinion was that I was here and now would live out my shift - and then wake up at home, or where was I when I fell asleep?"
    "As a matter of fact, that's why I didn't make any plans."
    "I wanted to."
    "Certainly, I didn't get my hopes up about Miku."
    "But the first plan I would have liked to make would have directly involved her."
    "It didn't have to be something romantic at all, at all."
    "I would have been more than happy to chat with her and just on a friendly footing."
    "And not just on that, for crying out loud."
    mi "We could go shopping together?"
    me "There's plenty to do in Moscow besides shopping."
    "Especially if you have a few extra rubles and plenty of free time."
    show mi normal pioneer with dspr
    mi "I think so."
    "The Japanese girl nodded gravely."
    mi "There must be something these millions of people do when they're not working or sleeping."
    me "Like going to the movies."
    mi "Or concerts! Senechka, what kind of music do you like?"
    me "You already asked me that!"
    show mi dontlike pioneer with dspr
    mi "And I'll ask again!"
    me "Oh..."
    th "I, my dear, like such a vinaigrette of songs that you'd better not ask."
    me "I don't really..."
    show mi sad pioneer with dspr
    mi "Don't tell me you don't like music! I wouldn't believe it anyway."
    me "I didn't say that. {w}I just can't name any names or individual songs."
    dreamgirl "Yeah, also because the vast majority of them hadn't been written yet at that time."
    th "That too."
    me "I like a lot of music, from rock to classical. I'm sure I'd like your music too - if I could, I'd definitely go to your concert."
    show mi shy pioneer with dspr
    mi "Better with me - to someone else's! Although, of course, it's nice to have that kind of trust."
    mi "We had this German group come last year, «Scorpions», they sang such beautiful songs! You like them?"
    me "Very!"
    "I honestly."
    me "If their song is playing at the disco, you have to dance with someone. There's no other way."
    show mi smile pioneer with dspr
    mi "And I wasn't very comfortable dancing with you. You're so big, how am I supposed to hug you?"
    "She turned to me and tried to put her arms around my neck."
    "I dodged with a laugh:"
    me "Yesterday you should have thrown them over, today it's too late!"
    mi "Fine."
    "It didn't offend her."
    mi "The day after tomorrow we have a farewell disco - we'll dance then."
    me "Hold on. What do you mean «the day after tomorrow»?"
    show mi normal pioneer with dspr
    mi "That's what it means. Three weeks in the shift, and you came in for the last one."
    "Not that I was too surprised - the pioneers didn't look like they'd just arrived, after all."
    "But it wasn't a pleasant surprise."
    "I had planned for a little more!"
    mi "Wearing my prettiest dress."
    "Miku continued."
    mi "And I will dance!"
    me "You will!"
    mi "And before that I will have a farewell performance!"
    me "You will!"
    show mi angry pioneer with dspr
    mi "Senechka, stop messing with me!"
    "She turned up her nose and added to her stride."
    "In doing so, her path was once again away from the straight line connecting my aching stomach and the three-ball sign!"
    th "Graaaagh…"
    me "Maybe we just..."
    "Miku ignored my line."
    "This time she was interested in the totalitarian straight lines in the style of the now so popular brutalism. Not Le Corbusier, of course, but it's just 'industrial goods'."
    "From the glass windows of which plastic astronauts were staring at us."
    "There was also someone nearby who had laid out a chessboard on a stool for some reason and arranged the pieces - I might add, incorrectly, rook to rook, bishop to bishop..."
    "And, of course, the lampshades, of course."
    show mi sad pioneer with dspr
    mi "Look, this is kind of boring..."
    "Confessed Miku."
    mi "There's absolutely nothing to catch the eye on."
    me "You shouldn't have even tried, it's all consumer goods."
    me "If you want exotics, go to the bazaar."
    "I wondered if there was a market here and found it unlikely."
    me "To Tula for gingerbread and samovars, to Ryazan for pies..."
    show mi angry pioneer with dspr
    mi "Look, I just want to take a little walk."
    mi "There's nothing difficult about galloping to the café, eating your ice cream and then galloping back to the hospital."
    mi "I don't want to do that, you know?"
    "Of course I do."
    "And if we were somewhere in Leningrad or Moscow - there we could at least take you on a tour, show you the monuments, tell you what I remember myself..."
    "There are certain difficulties with that here."
    "My gaze flickered around, looking for a possible escape."
    "I didn't want to ruin our already crumbling date again."
    me "Oh, look, there's also the Book House. Shall we go in?"
    show mi smile pioneer with dspr
    "Miku smiled and nodded."
    "I think I was beginning to understand her a little better."
    "It didn't seem to be that the process was more important to her than anything else."
    "Rather, it was that she placed a great deal of importance on the Rituals."
    "I'm sure she'd haggle to the hilt in the marketplace, too, taking unspeakable pleasure in it - just knowing that's the way it's supposed to be, haggling."
    "And with that she bribed."
    "So I ordered my stomach to shut up."
    "The food isn't going anywhere from me, but one little Japanese girl's trust is a fragile thing."
    stop ambience fadeout 3
    stop music fadeout 3
    scene bg int_caffee_day_7dl with fade
    $ persistent.sprite_time = "sunset"
    "Fortunately, the Book House was closed for reconsideration, and there were no other objects of interest along the way."
    "And Miku, sighing, was already forced to go, at last, to where I was so eager to go."
    play ambience ambience_dining_hall_empty fadein 3
    "She looked around curiously, studying the Soviet interior, but personally I was interested in things down-to-earth."
    "After seating her on a corner sofa by the window to peer into the interior and beyond, I strode to the counter myself."
    me "Two milkshakes with sprinkles and two plombières, please."
    "I asked."
    play music music_list["so_good_to_be_careless"] fadein 5
    voice1 "How many scoops?"
    "The saleswoman smiled understandingly."
    me "Let's make it four."
    "I was rewarded with another meaningful smile, and a few minutes later I was the proud owner of two tall, misted glasses and two shiny metal cremains, each with four scoops of delicious ice cream arranged in a pyramid."
    me "Itadakimasu!"
    "I exclaimed, unloading the riches onto the table."
    show mi smile pioneer with dissolve
    mi "Thank you!"
    "She immediately scooped up a long spoonful of ice cream whole and sent it into her mouth."
    "What am I supposed to do with her if she's like that?"
    show mi happy pioneer with dspr
    mi "Tashty!"
    "She reported a few minutes later, struggling to cope with the treat."
    me "Uh-huh."
    "When I eat, I am deaf and dumb. Cunning, and quick, and diabolically cunning."
    "We hardly spoke while we ate, the mundane platitude about love coming and going and always wanting to eat turns out to be very appropriate, but I didn't say it out loud either."
    me "You're tired, aren't you?"
    show mi shy pioneer with dspr
    mi "A little bit."
    "She confessed."
    if alt_day3_mi_7dl_donor == 2:
        mi "I got nervous, I thought I was going to do a great feat."
        mi "But instead of a feat, only my finger hurts. Eh!"
    else:
        mi "I'm a little worried about Sasha. Although he slept fine, and the hospital said he was fine."
    mi "But they didn't just chase us around all night, did they, Senechka?"
    "I nodded."
    mi "When do you think adults will stop lying to us?"
    me "Never."
    "On second thought, I answered."
    me "We're adults ourselves now - it's time to take up the baton."
    show mi angry pioneer with dspr
    mi "Personally, I won't lie to anyone!"
    "Angrily she said."
    mi "If I have children, I will only tell them the truth!"
    me "Even about where they came from?"
    "I couldn't help it."
    show mi shy pioneer with dspr
    mi "Baka!"
    me "Sorry. Silly question, yes."
    "Miku lowered her head, blowing bubbles through a straw."
    mi "No, it's not a stupid question."
    "Finally, she said."
    mi "It doesn't work out that you're mostly honest, but you lie about little things. It doesn't work that way, yeah."
    "She was silent again, straining to think about something."
    show mi sad pioneer close with dissolve
    mi "Senechka, tell me. What do you think of me?"
    "She suddenly moved closer to me and looked me straight in the eye."
    "A question of questions. In the camps they used to be very fashionable with the so-called 'questionnaires'."
    "The rules were strict, rigid - exactly one line per answer, short, to the point."
    "But for tricky questions like these, there was a relaxation - after the question 'What do you think about the author of the questionnaire,' there were usually three or four lines."
    "I wonder if I can fit my thoughts about Miku into three lines."
    "Especially since I haven't really figured out how I feel about her myself."
    me "You... You sound nice."
    show mi surprise pioneer close with dspr
    mi "Sound?"
    me "It sounds snarky, but yes. There are some people who are a sight for sore eyes - and I'm not talking about beauty. There are those who smell in a way that can drive you crazy."
    me "You got the sound. Have you ever heard of the concept of «clingy song»? You hear a song, a rhythm, a motif, the words, you remember them from the first time, and then you remember them for the rest of your life."
    mi "So I'm clingy?"
    "Miku didn't look too upset, and I knew I'd hit the bull's-eye."
    me "Very. What's much more interesting, no one will ever want you to get off. It's a talent, take care of it."
    "I say this half-jokingly, relaxed on the surface - but tense inside myself, fearing for the unknown."
    th "Does it scare me that she might mistake my honesty for flirtation?"
    "A strange thought suddenly occurred to me."
    "No, it can't be."
    show mi normal pioneer with dissolve
    mi "Thank you, Senechka."
    "Miku leaned back, leaving the poor cocktail alone."
    "She looked a little embarrassed, but that only added to her charm."
    "You only make a girl angry because she's beautiful in her anger. Miku, on the other hand, sometimes you have to get her in a blush."
    me "You're welcome. After all, you paid for my lunch, and honesty is the least I can offer in return."
    "This time she caught the joke and smiled understandingly."
    "Though her eyes remained serious."
    show mi serious pioneer with dspr
    mi "Senechka?"
    me "Hmm?"
    mi "I don't sit with someone like this very often, so I can look stupid."
    mi "Or rather, I absolutely know I've looked stupid a few times."
    mi "So I'm going to tell you something I haven't said in a long time."
    "She folded her palms and bowed to me - good thing she didn't get up from the table:"
    mi "Domo arigato. The date didn't turn out the way I wanted it to, but it was still very fun and entertaining."
    "I felt myself blush for the umpteenth time today:"
    me "Uh... Thank you, too. I mean, I'm glad you enjoyed it. I mean..."
    show mi laugh pioneer with dspr
    mi "Senechka, you're gibbering."
    "Quietly chuckled Miku."
    me "Sorry."
    mi "Just like me the first time we met. And the second time. And..."
    me "Are you saying we look alike?"
    show mi grin pioneer with dspr
    mi "No, I mean, we'll definitely have to do it again."
    mi "But no 'fish' stores and 'grocery stores,' okay?"
    "As if it is up to me..."
    me "I'll do my best."
    "I solemnly promised."
    show mi sad pioneer with dspr
    "Miku got sad again."
    mi "As you can see, sometimes «doing your best» is not enough."
    me "Are you alluding to Shurik? But who could have known..."
    mi "And with our next camping trip, who could know? Okay, I'm getting a little fuzzy. I guess a sleepless night is taking its toll."
    mi "Shall we go outside?"
    "She finished her cocktail in a jiffy and got up."
    mi "I didn't eat ice cream at home, I didn't drink cold drinks - I was afraid my ligaments would get cold."
    "She reported."
    mi "I shouldn't do it now either. But I'm so tired of doing the right thing and doing what's expected of me."
    hide mi with dissolve
    "Without waiting for me, she went outside."
    "I had to finish my drink at a brisk pace and hurry after her."
    stop music fadeout 3
    $ persistent.sprite_time = "day"
    play ambience ambience_camp_entrance_day fadein 3
    scene bg ext_townscape_ph_day_7dl
    show mi normal pioneer
    with dissolve
    play ambience ambience_7dl["town_day"] fadein 3
    "Miku was waiting for me in the shade of a sprawling elm tree standing not far from the café."
    "They probably pull tables out here every now and then and feast on the outdoors."
    mi "Shall we go for another walk?"
    me "Let's go."
    "We decided to walk down the next street and went toward the intersection."
    me "I'm paying for our next dinner, you know that."
    "I informed, pacing the crosswalk next to the Japanese girl."
    show mi laugh pioneer with dspr
    mi "As you wish! If you're paying then you're paying. I'll have crab, lobster..."
    with fade
    return

label alt_day4_mi_7dl_ch52:
    scene bg ext_townscape_ph_day_7dl
    show mi laugh pioneer
    with dspr
    "She would have laughed for a long time, but then some strange things happened at once:"
    play sound sfx_7dl["car_brake"]
    "At first we were deafened by the noise of the brakes of a car that nearly hit us, stopping literally a meter away from the «zebra»."
    $ meet ('sak','Japanese man')
    show mi scared pioneer at right
    show sak sigh suit at left
    "A man in a suit jumped out of it and wanted to say something..."
    "But he froze in amazement, and so did I, when I saw the daredevil's facial features."
    "A second later Miku and I flinched as another car whizzed by behind our backs. Sounded more like a truck."
    th "Where are we, on an expressway or something?!"
    show sak normal suit at zenterleft
    "Finally, everything calmed down and it was just the three of us: me, Miku, and the mysterious Asian man who almost killed us with his «Mitsubishi»."
    dreamgirl "Lucky guy. If it hadn't been for you, he would have gone right under the truck."
    "I couldn't agree more with my inner voice. Except the man's luck didn't end there."
    play sound_loop sfx_intro_bus_engine_loop fadein 3
    play music music_7dl["unholy_you"] fadein 3
    sak "Greetings, Miku-kun."
    show mi normal pioneer with dspr
    mi "Greetings, Sakishita-san."
    $ meet ('sak','Sakishita')
    "Miku smiled."
    mi "Are you on behalf of my father?"
    me "Miku, who the fuck is this?"
    "I asked politely."
    mi "This, as you put it, «fuck» — is my agent. Please don't be rude to him - I still have to work with him."
    "Quietly she asked."
    "I had to agree."
    sak "Miku-kun, aren't you supposed to be at the children's camp?"
    "He stepped a little closer, and I noted that he was surprisingly tall for a Japanese - almost as tall as me."
    show sak normal suit at zenterleft
    show mi normal pioneer at right
    with move
    mi "I should be. But we volunteered to help a friend, so..."
    sak "That's too bad. Govorov-san really wanted to see you. But given the circumstances..."
    show mi scared pioneer
    mi "Dad came to camp?"
    sak "He did, Miku-kun. I'm sorry you missed him."
    sak "I stopped here to fill up the car and have lunch, since there won't be time for that on the way back."
    show mi sad pioneer with dspr
    mi "What happened? And why did you come, Sakishita-san?"
    show sak sigh suit with dspr
    sak "Something happened, you're right."
    "He turned away into the car, and a few seconds later revealed to our attention some shiny plate, on which a pair of kanji was written a name very familiar to me."
    show mi surprise pioneer with dspr
    mi "Really?! But they said we have a waiting list until at least October!"
    show sak normal suit with dspr
    sak "That's right, Miku-kun, but your record was seen by the premier, so the label kindly agreed to move the queue."
    mi "And I..."
    "Confusedly said Miku."
    show sak smile suit with dspr
    sak "That's right."
    "Sakishita stretched his narrow lips in a smile."
    sak "We're going home."
    show mi dontlike pioneer with dspr
    mi "What about my stuff, my equipment?"
    "I don't know if it was out of politeness or some other consideration, but they both continued to communicate in almost impeccable Russian."
    "Only now, when Sakishita allowed himself a swear word in Japanese, did I notice it."
    show sak dontlike suit with dspr
    sak "I was counting on your father to bring you up to speed and have you ready when I arrive."
    sak "But of course, I will take you to your stay, and we will pick up everything you need. Just hurry, please."
    me "Miku, I'm not sure that's a good idea."
    "I hesitated."
    mi "Neither am I, Senechka."
    "Confessed Miku."
    mi "I've just started to enjoy the holidays."
    mi "But he's right - if my record company has agreed to move up the schedule, you'd better take advantage of it, you'd better be able to travel a bit before the New Year's holidays to support the album, otherwise it won't sell out."
    me "No, I mean..."
    mi "Don't worry about it."
    "Understandably nodded the Japanese woman."
    mi "I'm Sakishita-san's employer, it's not good for him to hurt me."
    show sak calm suit with dspr
    sak "Miku-kun, are you coming?"
    "The annoying Japanese man called again."
    play music music_7dl["will_you"] fadein 3
    me "I don't trust him."
    me "Even if it's your agent, there are totally different people responsible for you right now, you know?"
    me "You can't just disappear just because you met someone you know."
    show mi upset pioneer with dspr
    "Miku sighed."
    mi "But I..."
    me "No «buts». {w}Ask your Sakishita, how would he feel if you ran away from his supervision like that?"
    "I hadn't planned to go at Miku like that, but for some reason all those little-explained fears that all men of all time have felt for the women they hold dear went through my head at once."
    me "You're not saying anything? That's right."
    "It suddenly occurred to me that I was acting somewhat out of character here - and not quite rightly so."
    "And after a three-second brainstorm, I came up with a compromise:"
    me "We're going back to camp anyway, so we stick to the original plan: take Violetta Cernovna's car, and then we'll figure out what, where and how."
    mi "But we were told to walk until one o'clock."
    me "And Moscow time..."
    show mi shy pioneer with dspr
    "Miku glanced at her watch and gasped:"
    mi "It's fifteen to one."
    me "Which means it's time for Cinderella to go back, unless, of course, she's afraid of twelve blows to the pumpkin."
    "I elbowed away again invitingly."
    show mi laugh pioneer with dspr
    mi "Senechka, I don't agree with everything and don't understand everything you say."
    "Thoughtfully the Japanese girl stretched out."
    mi "But I guess you're right."
    "She bowed to the Japanese man:"
    mi "I'm sorry, Sakishita-san, but we have to find our responsible, I can't go with you."
    show sak sad suit with dspr
    "He tilted his head in response, acknowledging the fairness of the girl's words."
    sak "In that case, I will go to the camp to settle the formalities, and await you there. See you soon."
    sak "Oh yes, your father forgot something in my car, I'll leave it for your leader. A little gift."
    "After bowing once more, he went back to the car."
    hide sak with dspr
    play sound sfx_intro_bus_engine_start
    with fade
    stop sound_loop
    "And we headed back to the hospital, where Violetta Cernovna was waiting for us."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_7dl_ch6:
    scene cg d4_cs_car_day_cs_7dl with dissolve
    play sound_loop sfx_bus_interior_moving fadein 4
    "I can't really say anything about the way back."
    "It must have been the fact that we were all pretty exhausted."
    "I could vouch for myself - I had that unforgettable feeling when you'd just been fresh and alert and eagle-eyed, and then you sat down and had no strength to get up."
    "They rolled Sivka in, they rolled him in."
    if alt_day3_mi_7dl_donor:
        "Miku was sullenly silent, too, seeming to run the conversation with the agent over and over in her head."
        "Or trying to come to terms with the fact that her personal summer was about to end."
        "And I honestly wasn't jealous of her at all."
    stop sound_loop fadeout 5
    stop ambience fadeout 3
    with fade2
    "So we arrived at camp in a very depressed state."
    "It was already six o'clock, and we had safely missed the lunch, which only added to our already glorious state of mind."
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_dining_hall_away_day
    with dissolve
    "Without much shuffling, Viola drove the car onto the camp grounds and, after parking it by the canteen, immediately set off for home."
    if alt_day3_mi_7dl_donor:
        "Unlike us, she didn't sleep a minute - she worked."
        "Miku said a crumpled goodbye to me and left, too."
        "And I was left alone."
        "It's the same as always. Where you start - you end, the usual canon of the genre."
    else:
        "I understood her perfectly - I managed to get at least a couple of hours of sleep in the backseat."
        "So there was no surprise in her slight unfriendliness."
    play music music_7dl["the_way"] fadein 3
    "And the camp lived again."
    "The solipsist inside me wasn't too pleased to realize that life doesn't stop anywhere without me, either."
    "That my focus was not at all the main driving force of the universe."
    "But it was sad as hell!"
    "And from the side of the stage came the bass rolls."
    if alt_day3_mi_7dl_donor:
        "The camp seems to have lived just fine without Miku."
        "Probably Slavya?"
        "The cyberneticists ran and set up the hardware, Slavya runs it, Alisa has quality control."
        "So four people are more or less able to perform the function of one."
        "Perfect illustration of the phrase «there are no irreplaceable people»."
    else:
        "Miku didn't seem to miss me at all."
        th "It would have been strange if she did."
        "As if I owed her or her something."
        "Of course not."
    scene bg ext_dining_hall_near_day
    with dissolve
    play ambience ambience_camp_center_day fadein 3
    "After shaking off the pine needles and cones from the bench, I made myself as comfortable as possible and drew all sorts of nonsense on the sand with the stick I found here."
    scene cg d4_mi_kandji_7dl with dissolve
    "Sticking out my tongue with eagerness, I pulled three parallel lines from left to right."
    "Then a symbol that looks like a written letter «п», only a little more pretentious - I'm sure if someone had the same handwriting, he would be the first designer in the village."
    "No one will ever understand but one person."
    "How did I not think of the fact that on the «notebook sheet and on the blackboard» you should write incomprehensible curves of hieroglyphs instead of Russian letters, which are understandable to everyone!"
    "I shuddered and woke up."
    "Why do I keep thinking about Miku?"
    "In the sense that I don't put any additional meaning into my own thinking."
    "There's nothing more to it than that. I just can't get her out of my head."
    "That's all."
    "Thinking and thinking and thinking and thinking."
    "If you take me as an example from ten years ago, how I envied myself! No doubts, everything is clear, the world is discrete, there are no halftones."
    "The great thing, perhaps, was that I knew exactly what I wanted and from whom I wanted it."
    "In the sense that if I was sexually attracted to a girl, I wasn't embarrassed to admit it to myself."
    "With a sigh, I erased the writing."
    scene bg ext_dining_hall_near_day with dissolve
    "Here, on the other hand, you can't be even fifty percent sure."
    "Where are my seventeen years!"
    "Standing up, I decided to stretch my legs a little."
    if alt_day3_mi_7dl_donor == 0:
        dreamgirl "Actually, look for Miku and report back to her on your arrival."
        th "Shush."
        "Miku is probably running the concert right now."
        "At any rate, where else could the head entertainer be with all that bass coming out of the speakers?"
        scene bg ext_stage_big_day_7dl with dissolve
        "Miku, however, was not present."
        "Alisa was sitting at the console, giving me a frankly questioning look, but I was in no mood for nonsense."
        dreamgirl "Must… Find… Miku… Braaaains!"
        scene bg ext_square_day with dissolve
        "I guess I did look possessed from the outside."
        "But the longer I had to run around the camp, the more worried I got."
        th "Nothing happened to her, right? Tell me nothing happened to her!"
        scene bg ext_house_of_mt_day with dissolve
        "When I ran past Lena's cabin for the third time, I noticed some unfamiliar Japanese man chatting with the counselor about something."
        "I didn't go near them - to avoid it."
        "Then I found Miku - she was waddling down the path from the washbasins and looked most dejected."
        $ meet('sak','Sakishita')
        scene bg ext_house_of_un_day
        show mi sad pioneer
        with dissolve
        play music music_7dl["finale_farewell"] fadein 3
        me "Miku!"
        "I waved my hand."
        show mi normal pioneer with dspr
        "She turned around at the scream, clearly expecting to see someone."
        show mi sad pioneer with dspr
        "And then she lowered her head."
        mi "Ah, it's you..."
        "Well, yes. What did I expect, I wonder."
        "I was the one who was bored and languishing on the road, thinking about the Japanese princess."
        "And she wasn't bored here, by the looks of it."
        me "Yes."
        "I smiled - but again I found no response on her face."
        me "Is something wrong?"
        show mi normal pioneer with dissolve
        "Miku looked me over very carefully."
        "Then she shook her head just as intently."
        me "Then what's the matter?"
        me "Or did something {b}not happen{/bb}?"
        mi "Didn't happen. But you had nothing to do with it."
        me "Is that so? I see."
        mi "I'm telling the truth."
        th "And why is she making excuses?"
        mi "Something happened that I was expecting. But not at all the way I wanted!"
        me "What is it?"
        "I was getting a little discouraged by this conversation, which consisted of innuendo and omitments. Suddenly the machine-gun girl, who had been doing just fine without the interlocutor's participation, was gone."
        "Now there was a rather unkind girl in front of me, whose words I had to pull from her with pincers."
        mi "It's parents' day."
        "Calmly she informed me."
        me "Really?"
        mi "Yes. And I was expecting Pa to take the day off and come."
        me "Didn't come?"
        "Sympathetically, I asked."
        mi "He came. And brought news."
        me "Did something bad happen?"
        "Miku only shrugged her shoulders and continued."
        mi "He wasn't here long, very busy. I didn't even have time to think about it before... my agent arrived."
        hide mi with dissolve
        "Miku stepped back to the cabin and sat down on the steps of the porch, tucking her left leg under herself."
        me "I don't get it."
        me "And by the way, is that dick your agent?"
        "Miku faked a hint of a smile with just the corners of her lips."
        "She seemed really upset."
        show mi angry pioneer with dissolve
        mi "Yes, that's him. And you shouldn't call him that."
        mi "He may be callous, cold, stern. But he's still a good man."
        "Miku tried not to speak loudly, but you could see how hard she was holding back her anger."
        me "And why did he show up?"
        show mi serious pioneer with dspr
        mi "Wants to take me home."
        mi "The recording of the album has been pushed back to an earlier date, so we have to fly to Japan right away."
        mi "And then we have to go on tour..."
        me "And what did you say?"
        show mi sad pioneer with dspr
        mi "I don't know what to do, Senechka."
        "She exhaled."
        mi "I wanted to spend time with Dad, and we got into a fight over it."
        mi "And now Sakishita-san is nervous, too. It's not like you can explain to him that we have..."
        "She grew darker and darker with every word."
        me "Well, we can talk, we can explain somehow."
        "I hesitantly began."
        show mi dontlike pioneer with dspr
        mi "The trick is good, but it won't work. He's my agent, and right now he's doing something that will be good for my career."
        "It was hard to argue with that argument. But it didn't diminish my sense of dislike for this Sakishita's persona."
        mi "That's it."
        me "What do you mean?"
        show mi cry pioneer with dissolve
        mi "My summer is over, Senechka."
        "And she, not holding back any longer, burst into tears."
        mi "Pa is a fool!"
        mi "I believed, he promised that everything would change, here I would understand how to do it right, how to do it right..."
        me "Hush, hush... Everything will be all right..."
        "I didn't notice myself as I was beside her and, putting my arm around the girl's shoulders, began whispering something soothingly in her ear."
        "I don't remember what or how I said it myself - intonation was more important."
        "And only with a detached dull ache did I chase away the thought that it wasn't going to be any good."
        th "Miku-Miku... Why don't things work out with you, huh?"
        th "It could have been magical, and we could have been proud of the way we became together."
        th "But it worked out like this."
    else:
        scene bg ext_house_of_mt_day with dissolve
        "When I went out to the cabin with the desire to report to Olga Dmitrievna on my successful arrival, I found her somewhat occupied."
        "Sakishita had her full attention."
        "At a loss, I looked around."
        "For some reason Miku was still sitting on the porch of her own cabin instead of dutifully sleeping it off."
        "Finally, the Japanese man finished his conversation - judging by his annoyed look, not having gotten what he wanted from the counselor - and walked away to Miku."
    show sak normal suit at right with dissolve
    show mi sad pioneer with dspr
    sak "Gather your things, Miku-kun."
    sak "The road awaits us."
    "And I suddenly realized what despair is."
    "Despair is when you give it one hundred and two percent like the last jerk, breaking blood and sweat on the rocks - and it's not enough!"
    "And you realize that you can't squeeze any more out of yourself, that all that's next is the red corridor, after which people don't come back."
    "You have a whole moment of desperation to choose - and either your aortas open, giving you another moment to realize - the way back is closed."
    "Or you fly away a fractured puppet and freeze in the roadside dust."
    "I haven't fought in a long time."
    "But now it seemed very appropriate for me to resume what I'd forgotten."
    "I clenched my fists and looked up."
    "I sought the gaze of someone else's happiness snatcher - I needed him to have time to feel my despair before one of us was left to cool off."
    "Miku didn't see my face - but after a cozy glow of thoughtfulness and calculating odds broke through the tears and sadness, I decided not to finish off an already cracking world at the seams."
    "I gathered more air in my chest, getting ready to break away, and..."
    stop music fadeout 3
    show mt normal pioneer at left
    with dissolve
    mt "Excuse me, Comrade Sakishita."
    "Counselor's voice sounded."
    play music music_list["always_ready"] fadein 3
    show mi surprise pioneer with dspr
    mt "I'm certainly glad something happened to Miku somewhere, and all that stuff. {w}But I can't give a child to a stranger."
    mt "Even if Miku herself vouches for him."
    show sak treat suit with dspr
    sak "Excuse me?"
    show mt angry pioneer with dspr
    mt "What's not to understand? You've got her father's permission, so be it. But I won't let the pioneer girl go anywhere without a certificate from the Regional Office."
    "The squad leader said with no hesitation."
    "And I, who was about to give up hope, was back on my feet."
    "I never thought I'd say this or think this - but thank you so much Olga!"
    if alt_day3_mi_7dl_donor == 0:
        "Basically, after she gave me the apartment to wash, I was already indebted to her."
        "Now it has increased manifold."
    "Now he's running through instances all the way to the end of his shift, and we'll have a few more days!"
    "Sakishita certainly knew how to take a punch."
    show sak sorrow suit with dspr
    "He bowed politely."
    sak "I understand. Those are the rules."
    "But it wasn't like he gave up."
    sak "You dispose of a future to which you have no rights. But you do have responsibilities."
    show mt normal pioneer with dspr
    mt "As long as this child is in my custody, I am responsible for her future as well."
    mt "When you bring me all the documents, we'll talk, but in the meantime..."
    "She looked at her watch:"
    mt "Parents' Day ends in two and a half hours - I'll ask you to vacate our camp grounds by then."
    show sak normal suit with dspr
    sak "I understand."
    "The man humbly nodded."
    show sak pain suit with dspr
    sak "I'll get all the documents and come back for Hatsune-san."
    stop music fadeout 3
    mt "Have a good trip."
    "Wished Olga."
    mt "You get the documents - you get the child. I dare not delay you."
    play music music_7dl["kiss_you"] fadein 3
    if alt_day3_mi_7dl_donor == 0:
        sak "Don't worry about it. There will be. Miku-kun, I was thinking of arranging a farewell party, but it seems you intend to leave only with a scandal."
        "He bowed."
        show sak unsured suit with dspr
        sak "I don't know how the Russians celebrate someone else's good fortune - but I'm sure it's popular here, too."
        show mi surprise pioneer with dspr
        mi "What are you talking about?"
        show sak normal suit with dspr
        sak "If it's not too much trouble, walk me to my car, please."
        sak "And bring someone with you - for example, you can bring your friend."
        with fade2
        scene bg ext_no_bus_sunset with dissolve2
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        play ambience ambience_camp_entrance_day fadein 3
        "We were in camp at six o'clock, and now it was tangibly so by eight - the sun was leaning into the sunset, the smell of evening was in the air."
        "Just a little longer, and the horn would call the pioneers to dinner."
        "The Japanese SUV was parked in the shade, locked up tight - it wasn't hard to guess what kind of a stifler was inside."
        "But the Japanese didn't flinch, climbed in and opened the trunk from the inside."
        show sak normal suit with dspr
        sak "This is from your father."
        sak "Please. Take it. Use it as you see fit."
        "Miku headed around the car, and I backed her up just in case."
        "In the trunk of the SUV was some kind of gray cylindrical thing, which Miku instantly grabbed."
        show sak normal suit at left
        show mi smile pioneer at zenterright
        with dissolve
        mi "Thank you, Sakishita-san!"
        "She bowed lightly, showing her appreciation."
        sak "You're welcome. I'll be back. And I hope for discretion on your part."
        hide sak with dissolve
        "He slammed the trunk, went around the car, and jumped behind the wheel."
    else:
        with fade2
        scene bg ext_no_bus_sunset with dissolve2
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        play ambience ambience_camp_entrance_day fadein 3
        "Shaking his head, Sakishita headed away from the grounds."
        "Just in case, we both decided to make sure he left."
        "That uncle, though, seemed to have the strictest of rules."
    "The Japanese tires squealed on the hot asphalt, and the Mitsubishi rolled off into the red-hot distance."
    "Only now did I allow myself to exhale."
    "And turn back to Miku."
    show mi happy pioneer with dspr
    "I could only marvel at the reflection of my emotions in her eyes."
    "Only when she saw the car out of the gate did she let her senses go - she hooted and hugged me as hard as she could:"
    mi "Let's go out, people!"
    menu:
        "Would you go with him?" if herc:
            $ alt_spt += 1
            show mi upset pioneer with dspr
            "Miku thought for a while."
            mi "I don't know. Do you want me to go?"
            me "No, but..."
            me "I'm an old fan of your songs. I'd rather have you sing."
            "Miku didn't say anything, just smiled and put her arm around my shoulders."
            dreamgirl "{i}I'd rather.{/i}"
            "The inner voice mocked me."
            dreamgirl "Have you ever thought about just asking someone, you selfish bastard?"
            dreamgirl "Didn't you think Miku's ideas of {i}'rather'{i} would be different from yours?"
            dreamgirl "Turn your head on at last. Before it is too late."
            th "Your advice, as always, is invaluable."
            "The inner voice snorted."
        "He's a pretty nice guy" if loki:
            $ alt_spt += 1
            "Indifferently I said."
            show mi surprise pioneer with dspr
            mi "You mean?"
            me "Wasn't too lazy to go to a foreign country without knowing where to go just to warn you about the rescheduling."
            show mi upset pioneer with dspr
            me "He must really care about you."
            dreamgirl "Or he makes a lot of money off her."
            "I agreed to that, too."
            show mi normal pioneer with dspr
            mi "Probably."
            "Miku stroked my hand unabashedly and, meeting no resistance, caught my finger."
            show mi smile pioneer with dspr
            mi "But wasn't the whole trip meant to be a little different?"
            me "Yes. But your life is music. I've even come to terms with that already."
            me "Accept it, too."
            show mi sad pioneer with dspr
            mi "I don't know..."
            "She whispered."
            me "Neither do I. But I can tell you one thing for sure: you're too good at singing to just bury your talent in the ground."
        "But what about your career?" if dr:
            show mi surprise pioneer with dspr
            mi "What do you mean?"
            "Miku looked up and looked curiously into my eyes."
            "But this time, purely for the sake of variety, I didn't get embarrassed or avert my eyes."
            me "Remember how we met? {w}You looked like someone who was very out of place."
            mi "Then where is it - my place?"
            "I poked in the direction of the road going up."
            me "Stage, I suppose."
            show mi sad pioneer with dspr
            mi "But I just didn't have anything else."
            me "Don't you like to sing?"
            show mi happy pioneer with dspr
            mi "I like it."
            me "Then don't deprive yourself of it."
            show mi upset pioneer with dspr
            "Miku sighed."
            $ alt_spt += 1
        "Wasn't that what you wanted?" if herc:
            $ alt_hpt += 1
            show mi smile pioneer with dspr
            mi "I don't know what I wanted anymore."
            me "Don't you like to sing?"
            show mi upset pioneer with dspr
            mi "I do, but..."
            show mi normal pioneer with dspr
            me "Do you want to try something else?"
            "She nodded."
            me "Then you have two whole days to try out."
            "She chuckled and poked me in the side with her finger."
            show mi laugh pioneer with dspr
            mi "Are you so fed up with me that you can't wait to get rid of me?"
            "I immediately objected."
            me "Not at all!"
            me "Just worried about your future."
            show mi happy pioneer with dspr
            mi "How thoughtful you are."
        "He probably got offended" if loki:
            $ alt_hpt += 1
            "Indifferently I remarked."
            "Who am I kidding, though? {w}A bit of schadenfreude seeped into my voice."
            "A part of me rejoiced that the destroyer of other people's happiness had rolled off into the sunset with nothing."
            show mi angry pioneer with dspr
            mi "So what."
            "Harshly said Miku."
            mi "He gets paid for that."
            me "And for finding you here?"
            show mi normal pioneer with dspr
            "Her shoulders twitched indefinitely."
            me "It's not too late to change your mind and put things back the way they were."
            show mi serious pioneer with dspr
            mi "Why?"
            me "So you don't have to worry about swapping a shill for a soap."
            show mi normal pioneer with dspr
            mi "I want to at least try."
            "Calmly replied the Japanese woman."
            mi "Do I have the right to do that?"
            me "Of course. And what do you want to try your hand at?"
            mi "Uh... I don't know yet."
            me "That's what I thought."
            "A horn sounded from the canteen, and I dragged her along to supper."
        "Are you really happy?" if dr:
            $ alt_hpt += 1
            $ lp_mi += 1
            show mi laugh pioneer with dspr
            mi "Yes!"
            "The Japanese girl chuckled a little."
            mi "Sakishita is a pompous turkey. It's good when you manage to get on his nerves a little bit!"
            me "Oooh, what a mean little kid!"
            mi "Yes! That's me!"
            show mi grin pioneer with dspr
            "She nodded and playfully nudged my shoulder."
            mi "Now it's a race! Who's first for supper!!!"
            hide mi with moveoutleft
            "And, in time with her words, from the canteen came the immortal «Take the spoon, take the bread»."
            "With a smile, I rushed after the restless girl."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_7dl_ch7:
    scene bg int_dining_hall_people_sunset_7dl with dissolve
    play ambience ambience_dining_hall_full
    play music music_list["smooth_machine"] fadein 3
    "We were in the doorway at the same time - I have longer legs, of course, but Miku certainly moves her more often."
    "Each thought they'd get there first."
    "And we both pushed on, giving it our all."
    "Both got stuck in the doorway. Two idiots."
    show mt laugh pioneer with dspr
    mt "Semyon, Miku?"
    "Seeing the state we're in, Olga couldn't hold back a chuckle:"
    mt "Well, what do you look like? Did you wash your hands?"
    me "Yes!"
    "We lied with glee."
    show mt grin pioneer with dspr
    mt "I thought so. March back!"
    mt "And show me your hands when you come back. I will not delay."
    "She turned back to Viola standing there."
    me "Olga Dmitrievna!"
    "I whined."
    me "Can we make an exception? One tiny time?"
    show mt normal pioneer with dspr
    mt "One, you say?"
    me "Yes."
    mt "Tiny?"
    me "No one would notice!"
    "I was frankly too lazy to stomp over to the sinks."
    mt "No one will notice."
    show mt rage pioneer with dspr
    "She immediately put her hands to her sides and barked her trademark Hartman roar:"
    mt "Both of you go wash up before I wash you myself!!!" with vpunch
    with vpunch
    play sound sfx_open_door_kick
    pause(1)
    play ambience ambience_camp_center_evening
    scene bg ext_dining_hall_away_sunset
    with dissolve
    "She screamed something else, but we couldn't hear it anymore."
    "We were almost literally blown out of the canteen."
    scene
    $ renpy.show("bg ext_washstand_day", what = Dawn("bg ext_washstand_day"))
    show mi smile pioneer
    with dissolve
    mi "And what do you want with those hands, Senechka?"
    "Asked Miku, when we finally got to the hand-washing facilities."
    mi "If you don't wash them, you might get sick."
    me "It's not about the hands!"
    play sound sfx_open_water_sink
    pause(1)
    play sound_loop sfx_water_sink_stream
    "Fortunately, the water was well heated by the sun - it was a pleasure to wash my face."
    mi "Then what?"
    me "It's about principles."
    "I explained."
    if alt_day3_mi_7dl_donor:
        me "You and I saved a comrade, no less. We're practically heroes."
        me "And we acted selflessly! Don't we deserve some indulgences?"
        me "Got it?"
        show mi smile pioneer with dspr
        mi "Of course I understand! It's not like I'm stupid or anything."
        "Smiled Miku."
        mi "What does washing your hands have to do with it?"
        show blinking
        me "Oh..."
        "I see."
        "I won't find understanding here."
        me "Let's hurry up and wash and eat already - my gut is kicking in my head."
        "The ice cream she fed me seven hours ago is irrevocably digested and absorbed by the intestinal walls."
    else:
        me "I practically saved a life today! I'm a hero!{w} I want honors, recognition, glory!"
        show mi laugh pioneer with dspr
        mi "You're funny. Why do you need all this?"
        me "Okay."
        "On second thought, I've decided to moderate my appetites."
        me "Then I'll get some kind of indulgence - like not being allowed to wash my hands before the canteen!"
        me "Is that such an unaffordable price to pay for saving a comrade? Do you understand?"
        show mi smile pioneer with dspr
        mi "How about that! It's understandable, you're a hero and you want honors."
        mi "But what does hand washing have to do with it?"
        with fade
        "I did the Captain Picard pose."
        "Because for a split second I really wanted to say something profane."
        me "Let's just go to dinner already, okay?"
        "Miku nodded and, digging out a piece of laundry soap someone had forgotten about, began concentrating on soaping her palms."
    stop sound_loop
    play sound sfx_close_water_sink
    pause(1)
    scene bg int_dining_hall_people_sunset_7dl with dissolve
    play ambience ambience_dining_hall_full
    "When we sneaked back into the dining hall, the squad leader was no longer at the entrance."
    "Instead, she occupied the staff table and indulged in gluttony."
    th "Well, Olga Dmitrievna!"
    "It was good that they had plenty of food - you could always get a refill at the food counter if the camp portion seemed insufficient for a growing organism."
    "In our case, though the pioneers were troglodytes, they didn't eat everything - we got a portion of mashed potatoes and meatballs, too."
    "Of course, I had to stand in line to serve it, then balance with plates, forks, and cups, squeezing through the rows of suffering children."
    "But my ordeal was rewarded - the window, where Slavya and Lena usually sat, was completely free and even relatively unpolluted."
    "That's where we landed."
    show mi normal pioneer with dspr
    mi "Well?"
    "She raised an eyebrow questioningly."
    "I answered in tune:"
    me "Itadakimasu!"
    "She laughed and proceeded to eat."
    "No one wished me a pleasant appetite, of course - but we're not the proud type, willing to eat as it is."
    "Especially in such company."
    "I suddenly noticed that Miku had stopped talking."
    "I mean, she could chatter even now when she was in the mood, but there wasn't that knocking-down verbal flow."
    "It was as if I had climbed onto the scale with my feet and added a little phlegm to her psyche - and now she was almost like me, lazy and kind."
    th "I wonder what she's like alone with herself?"
    "It suddenly occurred to me."
    "A man who is sociable is equally sociable with different people. A person wise is different with each person."
    "And Miku is also a man of the stage. An artist."
    show mi normal pioneer with dspr
    mi "What's on your mind, Senechka?"
    "Miku asked nonchalantly."
    mi "I mean, other than what all you boys are thinking about at that age."
    me "Oh please, as if you're so mature."
    "I mumbled."
    show mi grin pioneer with dspr
    mi "Huh?"
    if not alt_day3_mi_7dl_donor:
        me "Yeah... Miku, can you tell me what that old Chinese guy of yours brought you?"
        show mi upset pioneer with dspr
        "Miku wondered."
        me "I mean, your..."
        th "What the hell was his name..."
        th "Sukishito? Uh... I'm not sure I should say that out loud."
        $renpy.notify('The implication is that in Russian it would be something akin to "give bitches"')
        th "Although Japanese «daisuki» is spelled very amusingly in Latin. And it's better not to read it aloud - they won't understand."
        show mi smile pioneer with dspr
        mi "Nothing."
        "The girl found an answer."
        me "That's a pretty heavy «nothing»!"
        mi "I'm sorry, but I can't tell you yet."
        me "Do you have secrets from me?"
        show mi upset pioneer with dspr
        mi "No! In the sense that... oops."
        me "Excuse me?"
        show mi shy pioneer with dspr
        mi "Thought suddenly that it was so unpleasant for me to make excuses. Or even thinking about lying to you at all."
        me "So don't lie!"
        show mi sad pioneer with dspr
        "With my last demand, I seem to have finally upset her."
        mi "Then don't ask questions that I'll be forced to lie to."
        "Miku moved away, leaving an extra meter of living space between us."
        mi "Can you do me that favor?"
        me "I'll try, sure."
        "I answered honestly."
        show mi smile pioneer with dspr
        mi "Thank you! You will oblige me very much with this."
        dreamgirl "I'll oblige you... I'll tie you down... I'll punish you with S&M!"
        dreamgirl "You know that in the word «BDSM» the first letter stands for «bondage», that same binding?"
        th "Brrr, get off, you lustful monster."
        mi "I need this for some of my gigs."
        "She had mercy at last."
        show mi normal pioneer with dspr
        mi "I promise you'll see everything."
        mi "I think you'll like it."
        "And before my anxious alter ego rears its head again, I hasten to clarify:"
        me "Something to do with the scene?"
        mi "Well..."
        show mi shy pioneer with dspr
        mi "Something like that."
        "She obviously hesitated, but I decided not to pay much attention to it."
        "You never know who has any secrets."
        mi "Are the inquiries over?"
        me "That's right!"
    mi "Are you doing anything right now by any chance?"
    me "No, why?"
    show mi happy pioneer with dissolve
    "Miku glowed:"
    mi "You won't mind my company, will you?"
    me "Not at all."
    "Cautiously I replied."
    me "But what are we going to do?"
    show mi smile pioneer with dspr
    mi "I have one very silly idea. Find me after supper, please."
    mi "Deal?"
    "After receiving my nod of agreement, she smiled again happily and flew away from the canteen."
    "I'd like to point out - leaving both sets of dirty dishes on me."
    th "Can anyone remind me how to say «pigger» in Japanese?"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_7dl_ch8a:
    scene bg ext_dining_hall_near_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 2
    "Long story short, when I came out of the canteen, the arrangement with Miku completely slipped my mind."
    scene bg ext_square_sunset with dissolve
    "I went to the square, where I had a good time lying on a bench, watching the clouds."
    "Then, after hesitating between the pier and the cabin, I opted for the chaise lounge."
    scene bg ext_house_of_mt_sunset with dissolve
    "However, no sooner had I unfolded the chair and made myself comfortable in it than someone patted me on the shoulder."
    play sound sfx_pat_shoulder_hard
    pause(1)
    play music music_list["everyday_theme"] fadein 5
    "I had to reluctantly peel my eyelids apart."
    show mt normal pioneer with dissolve
    mt "Idling about?"
    "She asked."
    me "I have the right! I'm a hero today and all."
    show mt laugh pioneer with dspr
    mt "Alright."
    show mt normal pioneer with dspr
    mt "I don't see Miku anywhere."
    me "Miku?"
    mt "And I want you to find her."
    "For the life of me, how the second one flowed from the first wasn't clear."
    "But that's Olga Dmitrievna - her logic is beyond the common man's comprehension!"
    show mt smile pioneer with dspr
    mt "Maybe she's sleeping in her dressing room again, in which case let her sleep."
    mt "As long as she doesn't go off the property."
    me "Why are you putting me in charge of this?"
    "I asked, just in case."
    mt "What do you mean, why?"
    mt "Didn't you go to town together?"
    me "Yes. And?"
    mt "You did the deed together, the hardship brought you together."
    show mt normal pioneer with dspr
    mt "In short, you heard the party assignment, the party said «need»."
    hide mt with easeoutleft
    "Having puzzled me thus, Olga smiled at me."
    "Shoved me aside with her hip."
    play sound sfx_open_door_2
    "And hid behind the door of the cabin."
    me "Shit."
    mt "I can hear everything!"
    "Came from inside."
    "Yeah sure."
    "It wasn't about looking - I'd have looked for Miku myself without too much persuasion."
    "And basically..."
    dreamgirl "Still killing yourself for not getting a valor pedal?"
    th "Yeah-yeah, keep talking."
    dreamgirl "Don't even get your hopes up, she wouldn't be coaxing you with a cross and a pestle. She's a counselor, she doesn't coax - she hands out party assignments."
    dreamgirl "It's about time you got used to where you are."
    stop music fadeout 3
    with fade2
    scene bg ext_square_sunset with flash
    me "I'm on the square."
    "It would have been a lot easier and more fun if she had a phone - a few words on the number the counselor asked for, and voila."
    "Not an option. First of all, it's years and years away from the first cell tower in these parts."
    "The satellite-receiving mechanism that Miku's agent was talking into doesn't count."
    "And secondly... it's customary in the camps to take the phone away for the day and hide it under lock and key."
    "For the sole purpose of saving the fragile machine from the inevitable overload."
    play music music_7dl["melancholy_sun"] fadein 3
    "But all factors aside, the Japanese, who have been into all this themselves, have long ago been accessing their geodata, signing up friends and signing up themselves, finding acquaintances through facial recognition..."
    "And if you look from the outside at a map of some Ameba or Mixie, the cities are dotted with the markings of people active online."
    "It's like being in an augmented reality or a huge MMO game, only you're not playing it, you're living it."
    "Now I'd get my phone out, I'd do a search for «Hatsune Miku», and a few seconds later a pleasant female voice would give me something like «turn north and in three hundred meters turn right»."
    "Civilization, for God's sake."
    "Now my balalaika wasn't much use."
    "Unless the last of the pendants in the batteries were enough to play Snake for half a round."
    "I went to the canteen first."
    scene bg ext_dining_hall_away_sunset with dissolve
    "Stupid. She has no business being here."
    "There are people like that - they go out to eat from stress."
    "Now I lied to Miku - obviously stress."
    "Except I don't think she's going to rob the canteen - she's not Dvachevskaya."
    scene
    $ renpy.show("bg ext_warehouse_sunset_7dl", what = Dawn("bg ext_warehouse_sunset_7dl"))
    with dissolve
    "Near the canteen the carcass of a storage shed lazily sprawled on the ground."
    "Nothing remarkable, if it weren't for a pair of extremely convenient steps along the end of the building - a place to hide from the scorching sun and the counselor's supervision!"
    "Unfortunately, Miku wasn't here either."
    scene
    $ renpy.show("bg ext_house_of_un_day", what = Dawn("bg ext_house_of_un_day"))
    with dissolve
    "It occurred to me belatedly that perhaps I should have looked for Miku on her property from the beginning."
    "But hindsight, as usual, is strong."
    "I couldn't recall Miku having much contact with anyone."
    "Yes, a lot of people could talk to her - she didn't say no to helping and she was on stage."
    "But her friendship didn't even seem to work out with Lena."
    "So all Miku had left was music and dusty instruments."
    "Sounds dreary. Lonely."
    "I twiddled the doorknob, scratched at the glass - locked."
    "Lena seems to have gone somewhere, too."
    scene bg ext_square_sunset
    with clock_r
    "I've been walking for an hour."
    "And it seemed like a good time to get a little dejected and ostracized."
    "After all, I was incapable of finding one very nice girl."
    me "But to begin with..."
    "Of course, it would have been foolish to look there, but still..."
    stop ambience fadeout 3
    scene
    $ renpy.show("bg ext_musclub_day", what = Dawn("bg ext_musclub_day"))
    "Why foolish? Because..."
    play sound sfx_knock_door7_polite
    pause(1)
    play sound sfx_open_door_clubs_2
    pause(1)
    scene
    $ renpy.show("bg int_musclub_day", what = Dawn("bg int_musclub_day"))
    with fade
    "Because I'm an idiot, that's why."
    me "Miku?"
    "I asked, taking the first step."
    "The room turned out to be unlocked - and it was somewhat out of character with the Miku I know her to be."
    th "I mean, she's easygoing to a certain extent, yes."
    th "But she takes her equipment and instruments very, very seriously!"
    if ('music_club' in list_voyage_7dl):
        "I squinted at the long-suffering trombone."
        th "With few exceptions."
    "Silence was my answer."
    "I looked around, even looked under the piano to see if she was getting some kind of harmonica."
    "No luck."
    th "I'd better lock up in here before I go."
    "I wondered."
    "And then a strange sound came to my attention."
    "I even froze for a few seconds, trying to determine what it might be like."
    "And…"
    me "Snoring?"
    "It came from under the covered door leading into the bowels of the club."
    "I remembered the warning that Miku might be there."
    "But if she's changing..."
    "Somehow it didn't occur to me that napping and changing clothes somehow have little correlation to each other."
    "But you have to be polite."
    stop music fadeout 3
    play sound sfx_knocking_door_outside
    mi "Mlem… mlem…"
    "Was clearly pronounced from within."
    "I see."
    play sound sfx_open_dooor_campus_1
    pause(1)
    $ persistent.sprite_time = "night"
    scene bg int_wardrobe_7dl
    with fade
    play music music_7dl["silent_angel"] fadein 3
    "She really was here!"
    me "Hey, are you asleep?"
    "For some reason I asked in a whisper."
    "At the far end of the room on the bales, like some kind of shifting gypsy, she was curled up in a ball and sweetly snoozing in her sleep."
    "The trip and the further showdown with the agent had exhausted the girl."
    "She looked so fragile and defenseless - and I just didn't want to frighten her."
    "I must not have known what to think or do anymore, since I was explaining my own behavior to myself."
    "Or maybe it's just that I'm just tired, and so I'm not really thinking about what I'm carrying."
    "Still, it was a little frustrating that all my worrying, all this running around meant nothing-she just dozed off in peace and quiet without waiting for me."
    "So we're even and no hard feelings?"
    "Anyway, I should wake her up and take her home, or she might sleep like that for a long time."
    "After all, this is my errand!"
    "So I leaned over and gave her a gentle nudge on the shoulder."
    mi "Mlem…"
    "Miku answered."
    "She didn't seem to care one bit about my pokes."
    me "Wake up, you walking Mlem."
    mi "U…"
    "What a highly intelligent conversation."
    me "If you don't go home, you'll have to spend the night here."
    mi "Uuuuu…"
    me "Come on, the cozy cradle is just waiting for you - warm, soft!"
    "For some reason I continued in a half-whisper."
    mi "Lena, get lost."
    me "I'm not your Lena, wake up, come on!"
    "I tried shaking her a little harder."
    "It didn't work."
    "Shit. I can't leave her like that."
    "Although my inner voice here gives me some ideas about how to abuse a sleepy carcass, I won't listen to it."
    me "Miku, if I don't take you home, I'd better not go back myself then."
    me "I'll crawl into bed next to you then! You'll be my pillow."
    "As I suspected, that won't get through to her."
    "Looks like she's going to be here all night."
    "I either have to put up with it or..."
    if herc or loki:
        menu:
            "What can I do?":
                dreamgirl "I don't know either."
                dreamgirl "Let's just tell our kindest counselor that we found the runaway and fall asleep - something's killing me!"
                th "What's wrong with you?"
                "I wondered."
                dreamgirl "So you just haven't had time to feel tired yet. But don't worry, if you just relax..."
                "A little freaked out by such a prophecy, I took one last look at the sleeping Miku:"
                me "Sweet dreams, sunshine."
            "It's somehow wrong":
                th "Don't you think?"
                th "If I leave now, I'm essentially leaving her here alone."
                dreamgirl "So what? The music club is her home."
                th "Don't be silly, all girls are scared at night, and Miku is a terrible coward, she admitted it herself, remember?"
                dreamgirl "What are your suggestions?"
                "I smiled."
                $ alt_day4_mi_7dl_ev_savior = True
                $ alt_spt += 1
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_7dl_ch8b:
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene bg ext_square_sunset with dissolve
    play music music_list["silhouette_in_sunset"] fadein 3
    me "«Find me», my ass, no more, no less."
    "I grumbled, stepping out into the square."
    "Honestly, I was already a little embarrassed about spending so much time with a girl... not being in any kind of relationship with her."
    "I mean, I'm not implying anything, but..."
    dreamgirl "Yes! Start howling: «I luvd you so much that I didn't see anyone else at all!»"
    th "Stop."
    "I blushed and embarrassed myself as if the screams of my schizo half could be heard by anyone else."
    dreamgirl "No, I mean it. If you're planning to - what's the word in your dorky time? 'Hook up'?"
    th "I don't say that."
    dreamgirl "Not the point. Come on, to Miku's cabin to question her neighbor's, zig-zig-zig!"
    th "What's that for?"
    dreamgirl "Because, my sweet jerk, you've never once in your life taken an interest in your beloved's circles of residence."
    th "Should I have?"
    "To all my buddy friends I always left room for maneuvering and their own secrets."
    "Couldn't Miku have had secrets?"
    dreamgirl "No, seriously, are you actually this stupid?"
    th "It's not like I planned on having this kind of interest."
    dreamgirl "So reschedule!"
    dreamgirl "You can't throw your whole life away because you don't want to move your brains a little."
    scene
    $ renpy.show("bg ext_house_of_un_day", what = Dawn("bg ext_house_of_un_day"))
    with dissolve
    "I'd like to think somebody needs me."
    if herc:
        "But in fact no one will notice my absence."
        "Except for my cat - but she's pragmatically waiting for me purely as a dispenser."
        "If I don't show up, or if I show up too late, which has happened, well, that's not much of a problem."
        "Will climb from an unclosable window ledge to an unclosable window on the landing, and a very kind-hearted grandmother lives two floors below."
        "So even in that respect, I'm not a big deal."
    else:
        "In fact, I didn't need myself in the first place - and that's where it all started."
        "I even thought of death in a detached way, as something completely unafraid."
        "Just another reboot of OS «Semyon», working in a disastrously unfortunate configuration."
    "And I wanted something else."
    "Perhaps to walk under the arm of someone, to know that your shake will be reciprocated by a shake, that someone remembers you... silly dreams of a silly man."
    play sound sfx_knock_door7_polite
    "I knocked on the door in an extremely polite and courteous manner, diligently pushing away the thought that even yesterday I wasn't so humble."
    "Useless, though."
    "Not a sound was heard from inside - no one seemed to be home."
    me "What am I supposed to do now?"
    "Miku asked me to find her, but man, she could have taken care of the clues!"
    dreamgirl "So why don't you start looking more systematically? At her club, for instance."
    th "And what would she be doing there?"
    dreamgirl "Well, my dear, unlike you, she has responsibilities."
    th "True!"
    "I agreed, turning north."
    scene
    $ renpy.show("bg ext_musclub_verandah_day_7dl", what = Dawn("bg ext_musclub_verandah_day_7dl"))
    with dissolve
    play sound sfx_campus_door_rattle
    "The club was locked up."
    th "Any other suggestions?"
    dreamgirl "Nope."
    "Disconcertingly honestly reported the inner voice."
    th "You're as useless as a goat's milk!"
    dreamgirl "I hear it from the dumbass!"
    "We would have been bickering like this for a long time, but I suddenly caught a familiar voice from the corner of my ear."
    "And that voice was coming."
    scene
    $ renpy.show("bg ext_admins_day_7dl", what = Dawn("bg ext_admins_day_7dl"))
    with fade
    stop music fadeout 5
    "Yes, you could tell now that all my running wasn't fruitless: there were kids walking away from the administration building, and a very happy Miku was sitting on a bench under the windows of the camp director's office."
    show mi normal pioneer with dissolve
    mi "Found me after all."
    "She nodded."
    mi "Will you sit down?"
    "I sat down on the bench next to her."
    me "Told me to find you, but didn't tell me where to look."
    play music music_7dl["someone_like_you_guitar"] fadein 3
    show mi shy pioneer with dspr
    mi "Well, I'm sorry. Sometimes I get carried away, I don't belong to myself at all."
    me "What do you mean?"
    show mi smile pioneer with dspr
    mi "I knew for sure I had to be somewhere where you could find me, then you would find me, but then I met the kids from fifth squad and they called me 'Aunt Miku' and asked me to sing."
    "She was gibbering again."
    "Worried."
    mi "So, as much as I wanted to run away, I got up and sang to them. First «Blow with the Fires», then «Once again the battle continues», and… By the way, Senechka, do you know anything by Vysotsky?"
    "She seemed sincere enough that I suspected some kind of game."
    "Though if there had been, how could I have recognized it? She's an artist, she knows how to act."
    show mi upset pioneer with dspr
    mi "There, you're upset."
    "She tilted her head and, looking at me sideways, pouted her lower lip and fluttered her eyelashes quickly, pretending she was about to cry."
    "But I won't believe any more of that kind of acting today."
    me "You didn't leave with that Sakishita, so you still belong to yourself to some extent."
    show mi smile pioneer with dspr
    mi "Yes?"
    "I nodded affirmatively, and Miku scratched the back of her head in a very Russian way."
    mi "You know, you're right! You're smart, Senya!"
    "My accustomed skipping-Miku was making a swift comeback, and that made me happier."
    me "I take it Sakishita isn't related to you, or even a friend?"
    show mi normal pioneer with dspr
    mi "Not really."
    mi "He's more of a family friend already. And on great terms with Dad."
    mi "He was hired by Pa, a long time ago. They became very friendly and taught each other languages."
    mi "In the evenings they would sit at our house and talk."
    me "Is that why he spoke Russian so easily?"
    "I guessed."
    mi "Well yes."
    me "Maybe he's not so bad, this Sakishita of yours..."
    "Miku got serious."
    show mi sad pioneer with dspr
    mi "Just..."
    mi "It's just that I've never had anyone or anything prying into my personal affairs, and then they had to - and boom! - helped."
    mi "So I'm going to abuse that feeling a little more, okay?"
    "I smiled involuntarily, nodding."
    show mi normal pioneer with dspr
    "The great bulk of the administration building stood overhead, the saxophone tinkled in the breeze from the ajar window, the evening was benign, and it was surprisingly cozy in the company of a Japanese girl."
    "And even though we were separated by a whole bench, half of our squad could plop down between us if they wanted to and not be embarrassed at all."
    "What was more important was belonging, a common air and thought."
    "It's not every day you get to meet someone whose thoughts match your own inner monologue so completely."
    "And Miku suddenly found herself sounding in tune with my consciousness."
    "And I should have thought of the foolish things that instantly pop into the mind of young and maximalist people - necessarily to the grave, necessarily fate and other foolish things."
    "But I haven't been seventeen for more than ten years."
    "Yeah, and Miku doesn't seem romantically inclined - more like she's just comfortable and relaxed when she can take the time to express her own thoughts."
    "That's right, yes - I'll be sure to listen and listen to everything, not let a word pass my ears, compare and draw conclusions."
    "It's easier to say, what usually happens in the course of a normal conversation between two normal people."
    show mi serious pioneer with dspr
    mi "I didn't sleep at night again - there was a terrible noise under the windows again."
    "She shared."
    mi "I couldn't sleep after that."
    mi "I lay there in the dark, looking at the ceiling and thinking."
    me "And Lena?"
    show mi shy pioneer with dspr
    mi "She went to Zhenya's library: she and the girls were guessing the groom, they had some kind of date."
    me "Why didn't you go too? Aren't you curious?"
    show mi normal pioneer with dspr
    mi "Not at all."
    "Just said this baby."
    "Her friends are getting married, wondering about the opposite sex and guessing the name of their future betrothed."
    "And she sits with me and talks about how she's been frightened three nights in a row by the noise under her window."
    "The sound of the voice surprised myself:"
    me "It must be someone playing a joke on you."
    show mi surprise pioneer with dspr
    mi "What's that for?"
    "The girl got surprised."
    mi "One should sleep at night, not..."
    me "For some, the opportunity to mock one's fellow man is more valuable than any sleep."
    "Especially with the houses raised above the ground."
    stop music fadeout 15
    "A whole thought swirled in my head: should I tell Miku that, despite their seeming benevolence, children are cruel by definition?"
    "She seemed so pure, so unspoiled, that it seemed sinful to soil her with worldly cynicism and uncovering."
    "And then she surprised me."
    scene bg ext_admins_night_7dl with dissolve
    $ persistent.sprite_time = "night"
    $ night_time()
    show mi dontlike pioneer with dissolve
    play ambience ambience_camp_center_night fadein 3
    mi "So it's all the same here, too?"
    play music music_7dl["longing"] fadein 2
    "For a second her eyes clouded over - apparently she had something to remember, so I hastened to clarify:"
    me "But it doesn't have to be that way! Maybe it's just a joke."
    mi "A joke, yes. A joke. Which is funny to everyone but the victim of the joke."
    "Tucking her legs under her, sitting down oddly, on a tucked knee, she exhaled:"
    mi "Everything is the same everywhere."
    mi "Do you want me to tell you why I left elementary school?"
    th "Actually, no."
    th "I have a weak nervous system, I'm impressionable, and I can stay up several nights afterwards empathizing."
    "I nodded."
    me "Completely left?"
    mi "Yes. I was twelve when my parents completely homeschooled me."
    mi "Only a little later, to keep myself in shape, I did enroll in music school for vocal lessons."
    mi "But that will be a few years from now - but for now I, hafu, sit at my desk by the window."
    show mi normal pioneer with dspr
    mi "Sometimes I felt like there was my class and there was me - and we were learning in different places, in different ways."
    mi "When you're a little older, of course, it's easier - the boys begin to take an interest, shouting «kawaii» after you and show you signs of attention."
    mi "But when you're eight and you think of boys as creatures from another planet... And they pay you back in kind."
    mi "When they can lock you in a sports locker room just to see how you can cry..."
    mi "I was once dragged by my arms and legs half naked and thrown into the men's locker room altogether."
    me "What?!"
    show mi angry pioneer with dspr
    mi "What you heard. Thrown in. Half-dressed."
    me "And?"
    mi "I got yelled at by the head teacher, called 'hentai', and my mom whipped me so hard I couldn't sit down for a week."
    me "You didn't say anything to anyone?"
    "I guessed."
    mi "Yes."
    mi "All in all, it's useless. The teachers themselves were like that, taught that way themselves - it's part of our lives, Senechka, part of the culture, if you like."
    mi "That's why no one on the faculty will ever notice or pay attention to you being bullied."
    dreamgirl "Not much different from the schools you're used to, huh?"
    th "At least there you could complain, get the police involved, picture the beatings and so on."
    dreamgirl "In Japan, I guess you could, too?"
    show mi normal pioneer with dspr
    mi "It was as if they always felt the line to which I could be pissed off and tormented. I mean, they once cut out a whole chunk of hair on the top of my head - but no one ever hit me in the face."
    mi "Thoughtful cruelty."
    mi "The number of living abominations planted in the backpack is incalculable."
    mi "I'm sorry, I think I've been talking you out of my mind."
    "The Japanese girl shook her head, chasing away the memories."
    mi "It's all so past, I almost don't believe it happened anymore myself."
    mi "It's been a long time, a very long time. And then there was my performance, there was my acting class."
    show mi smile pioneer with dspr
    "Here she smiled for the first time during her monologue."
    "Her smile was dreamy:"
    mi "Then there was my music school from UNICEF."
    mi "You would have loved it! The guys there are so great!"
    stop music fadeout 3
    me "Guys?"
    mi "I mean, boys and girls.{w} I even got a friend there who hardly escapes my chatter!"
    show mi normal pioneer with dspr
    mi "But about that next time! Lights out soon."
    scene bg ext_house_of_mt_night_without_light with fade
    play ambience ambience_camp_center_night fadein 1
    play music music_list["a_promise_from_distant_days_v2"] fadein 2
    show mi happy pioneer at center with dissolve
    mi "Once again we have an evening of revelations."
    mi "Again I'm talking and you're listening."
    "Miku folded her palms against my cheek, looking at me with incomprehensible delight."
    mi "Doesn't it bore you at all?"
    if loki:
        "Considering I've been a prisoner of the Castle of Silence for the last seven years?"
    if alt_day2_mi_date == 3:
        me "You promised me that I would leave one day, didn't you?"
        "Straight up declared me."
        me "So I hurry to get my impressions in before your prophecies begin to come true."
        mi "Ah..."
        "The girl was starting to get sad, so I hurriedly continued:"
        me "But I hope you're a bad fortune teller, and I'll see you many, many more times."
        mi "Yes?"
        me "Bet!"
        show mi laugh pioneer with dissolve
        mi "That's good! I remembered what you said - not to refuse later!"
    else:
        me "Not at all!"
        mi "On the contrary, I enjoy it."
        mi "Yeah?"
        "With hesitation Miku stretched out."
        "I nodded affirmatively."
        show mi normal pioneer with dspr
        mi "Well then..."
    mi "See you in the morning!"
    hide mi with easeoutleft
    "She turned and hurried down the street toward her cabin."
    me "Miku?"
    "Instead of answering, she waved her palm over her head without turning around:"
    mi "Good night!"
    "I followed her with a glance and, only after making sure that she had successfully walked in and slammed the door behind her, allowed myself to go home."
    "After the passions I had heard today, for some reason I felt an incomprehensible responsibility for the girl."
    stop ambience fadeout 1
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg int_house_of_mt_noitem_night
    with fade
    play ambience ambience_int_cabin_night fadein 1
    "So many conventions have been invented for us."
    "You can't tell someone you like to like them - you have to sniff them out for a long, long time first."
    "You can't openly show emotion in front of all the honest people."
    "As they say, in the Soviet Union, children were not allowed to look at three things: spot welding, a quartz lamp, and an uncle kissing an aunt."
    "And finally, boys and girls must dwell separately."
    "This last rule, however, I have been extremely successful in breaking by undressing in the cabin, which is also inhabited by an extremely shapely counselor besides me."
    "All in all, I understand there are still some empty cabins available."
    "Why I was placed here remains a mystery."
    dreamgirl "To some mystery and to others not so much."
    "The alter ego spoke enigmatically."
    th "Do you know something?"
    dreamgirl "I guess, rather!"
    th "And?"
    dreamgirl "I think the point is that Olga doesn't really want to get a half-naked Miku out of your closet."
    th "Why would she be half naked?"
    dreamgirl "Oh, so there's no complaints about the other things."
    th "Ugh, you."
    dreamgirl "Ugh, ugh. But you keep in mind - it's your touchy-feely conversations only mean nothing to you."
    dreamgirl "Those around you are bound to have a different opinion - in the usual style of your loser karma."
    show blink
    "I closed my eyes."
    th "I'll think about it tomorrow."
    "And again I ran away from the thoughts, again avoided the understanding that the split personality had put in my head to no avail."
    "Because only in innocence could things be simple and lucid."
    "And I so did not want complexity!"
    scene cg d1_end_of_day_7dl
    with dissolve
    th "Sleep…"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_7dl_ch81:
    play sound sfx_open_door_clubs fadein 0
    pause(1)
    play ambience ambience_camp_center_night fadein 3
    scene bg ext_musclub_night_7dl
    with blind_l
    play music music_list["she_is_kind"] fadein 3
    $ alt_hpt += 1
    "By the time I was outside again, it had already gone dark."
    "It must have taken longer than I thought to run around the camp and convince one Japanese girl to get her carcass out of her sleeping bag."
    "And no."
    "I didn't go to the washbasin with a bucket at all."
    "Although the thought did occur to me."
    "No. Instead, I dragged a Japanese girl on my own hump, breathing through my teeth."
    dreamgirl "Romance!"
    th "Shut up!"
    "Miku never seemed to wake up - and she wasn't planning on waking up."
    "I wish I could sleep like that, too."
    "She must have a clean conscience."
    "Very clean."
    scene bg ext_house_of_un_night_7dl with dissolve
    "I reached Lena and Miku's cabin, which was the closest, but I was barely alive because of fatigue."
    "If I had any plans for the night and the stars and youth, it was..."
    "To hell with it. I'm tired as a cat and I plan to get some sleep."
    "And woe to whoever gets in my way."
    show un surprise pioneer with dissolve
    un "I've heard of girls being carried on their arms, of course, but on their backs..."
    "Lena approached from behind in the locals' trademark silent style."
    "She had a towel over her shoulder and a brush and soap dish in her hands - it looked like the girl had just finished her evening routine and was planning to tuck in bye-bye."
    "Which I was utterly deprived of!"
    me "Very funny."
    "I mumbled."
    me "If you'll be so kind..."
    "Lena, suppressing a chuckle, nodded and walked up the stairs:"
    un "Please!"
    "Opened the door wide open, letting in the mosquitos, night air."
    "And me and Miku, of course."
    scene bg int_house_of_un_night with dissolve
    "I guess that last move woke Miku up after all."
    "Because I was immediately stared at by astonished eyes."
    show mi shocked pioneer with dissolve
    mi "Huh?!"
    me "Good morning to you, too."
    mi "Morning?"
    show mi scared pioneer with dspr
    mi "But it's night!"
    me "You noticed too, didn't you?"
    mi "Yes! I was sitting in the club, waiting for you, and you kept not coming and not coming, and then I decided that my back was tired, so I went to lie down for a while, and... and how did I get here?"
    me "Silently."
    show mi shy pioneer with dissolve
    mi "Did you carry me all the way?"
    me "Something like that."
    mi "Oh... I'm sorry, please. I didn't think..."
    th "I agree with that!"
    show mi upset pioneer with dspr
    mi "I mean, I didn't mean to. Anyway, I'm sorry you had to strain yourself because of me."
    "If she weighed at least forty-five kilograms, maybe I'd still be straining, but as it is..."
    me "Come on. I'm going to go, okay? I'm sleepy."
    mi "Sure."
    me "And you try to go to sleep, too. You slept very soundly, but you'd better get some sleep."
    "Why do I say that?"
    mi "I had a very good dream."
    "Confessed Miku."
    mi "I didn't want to wake up."
    me "What kind of dream?"
    show mi happy pioneer with dspr
    mi "About my school, where I was transferred to last year!"
    me "Shame."
    show mi surprise pioneer with dspr
    mi "What do you mean?"
    me "I mean, I'm sorry I had to wake you up."
    mi "It's okay."
    "Lena, who had been waiting politely in the doorway the whole time, coughed, attracting attention, and we both flinched."
    me "That's it, I'm definitely going now."
    mi "Yes..."
    stop music fadeout 10
    play sound sfx_open_door_clubs
    pause(1)
    scene bg ext_house_of_un_night_7dl with dissolve
    "I don't know why, but when I hurried past Lena at the door and ran down the steps, my ears burned distinctly."
    "Maybe it was Lena's oddest look."
    "I don't know. I'm not sure exactly."
    stop ambience fadeout 6
    stop music fadeout 1
    scene bg ext_house_of_mt_night_without_light with fade
    play ambience ambience_camp_center_night fadein 1
    play music music_7dl["to_the_sunrise"] fadein 2
    "I make a story 'for the people' - and they don't see my boredom and loneliness behind it."
    "Feeling myself only gets halfway real, and thanks for that go to the film academy and all of them - the crowd holding the blade thinly shavings off my ice."
    "But I don't blame them for that - after all, it's those who remembered us hungry and with burning eyes that we scream the most."
    dreamgirl "Are you moping again?"
    "If you should call it moping."
    dreamgirl "What's the point?"
    th "There isn't any. I'm starting to remember who and what Miku is - and guess what?"
    dreamgirl "What?"
    th "I seem to have successfully broken my own first rule."
    dreamgirl "Don't think too long about anyone?"
    th "And also not to put that 'someone' around your neck - both literally and figuratively."
    "There was a full moon rising overhead - a time for werewolves, lovers, and other sick individuals."
    "At such times I wanted to find an empty attic and smoke till morning, playing with rhyming lines."
    "There was something in there - about hating someone who had become almost native, about eyes reflecting the sky and the sadness of a whole ocean."
    "And here I am. Instead of dusting off my soul, shaking it up a little, I plan to go to bed."
    "No longer because I'm terribly tired."
    "Just so I don't have to think about anything."
    "Especially about..."
    stop ambience fadeout 1
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg int_house_of_mt_noitem_night with dissolve
    play ambience ambience_int_cabin_night fadein 1
    "The name of the difficulty generator could not be heard over the creak of the door and the deafening silence of loneliness."
    "In the meantime, the time was perceptibly so close to midnight."
    me "A good pioneer should be in bed by now."
    "I proclaimed, glancing at the counselor's bed."
    "That one turned out to be badly flattened - it looked like our far from perfect squad leader had taken an evening siesta."
    "So she first baffled me by playing Pinkerton, and then she went and piled in here."
    dreamgirl "So?"
    dreamgirl "A squad leader's bread is hard and earned by sweat and blood."
    th "Yes, yes. There were fifteen pioneers in the business of getting the counselor's bread."
    "I remembered something else, thought about it, figured it out, even remembered the words of songs."
    "But as soon as I loosened my grip, huge blue-green eyes would instantly appear through the piles of lines."
    th "I'm just scared to go to bed."
    dreamgirl "Is it so unpleasant to think of one lonely Japanese girl?"
    "Innocently inquired the inner voice."
    th "It's a lot nicer than talking to you."
    dreamgirl "So what's the problem?"
    show blink
    "I closed my eyes."
    th "Nothing."
    "Under my closed eyelids, the memories of today instantly flashed."
    "And everywhere around was her."
    th "Nightmare!"
    scene cg d1_end_of_day_7dl with dissolve
    "I groaned."
    scene black with fade2
    "And yet inexplicably smiled as silence and darkness enveloped me."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_7dl_ch82:
    $ lp_mi += 1
    $ alt_spt += 1
    play ambience ambience_int_cabin_evening fadein 2
    scene bg int_wardrobe2_7dl with fade
    play music music_7dl["tellyourworld"] fadein 3
    "…or…"
    with fade
    dreamgirl "Really?"
    th "Well yes!"
    dreamgirl "But that's stupid."
    th "Uh-huh."
    dreamgirl "Besides, nobody does that around here."
    th "That's right."
    dreamgirl "Finally, you can get in a lot of trouble."
    th "That's right, too."
    "I raised my hand with three clenched fingers."
    th "All three criteria for stupidity are met. Do you really think I'm in a position to hold on now?"
    play sound sfx_7dl["blanket"] fadein 0
    "I pulled the twin bale of the one on which Miku was snoozing, closer to the dark corner she'd taken a liking to."
    "And settled in with all the comforts of home - almost like the Lumiere Hall on their signature pear-shaped planetarium exhibit."
    "Except there's only one exhibit today. One star - a single starlet."
    "Oddly enough, I almost didn't feel tired."
    "And I, feeling like an art expert, covered my left eye, leaving only cold tones: highlights in my hair, milky marble skin that blooms only with embarrassment... or anger."
    "Goosebumps on my arms."
    th "Goosebumps?"
    "It occurred to me, with some delay, that she might well be freezing!"
    scene bg int_wardrobe_7dl
    with dissolve
    "Seconds went by, adding up to minutes, and nothing changed."
    "I had enough strength, which I didn't have much of, and I groaned and peeled myself off the 'pear'."
    "At the far end of the room a quadruple folded blanket was waiting for me."
    "Soon a streak of moonlight stretched through the crack under the door - night was coming in steadily and surely, so I turned out the light."
    play sound sfx_7dl["blanket"] fadein 0
    th "You'll answer to me for Tsushima."
    "I promised, wrapping a blanket around the girl."
    dreamgirl "Will you keep her warm with your warmth?"
    dreamgirl "It's summer, of course - but it can get pretty chilly. She'll catch cold!"
    "Now that was a foolproof temptation."
    "I even hesitated for a few minutes, figuring out how to..."
    th "No!"
    dreamgirl "What?"
    "The alter ego marveled so naturally that I knew: it was lying."
    th "Nothing. The last time I fell asleep like that with, let's not point the finger at who - remember how it ended?"
    dreamgirl "Well..."
    th "That's right! It's not worth the risk, sleeping next to me is fraught: you could wake up in a very interesting position."
    th "So I think I'll refrain."
    "Don't accept gifts from the devil."
    "Even if it is your own personal devil, so to speak, deus ex machina."
    show blinking
    "Though there was, there was temptation, damn it!"
    "Nevertheless, I pulled the bale closer to the Japanese girl's recliner - so that I could see her."
    "And it wasn't that I cared about her in any particular way - no."
    "Though it was that, too."
    "But once in my life, there was a whole one time when there was no one to tuck in the blanket."
    "There was no one to hold up a rock from a long fall off a cliff."
    "That must be why this reverent attitude toward other people's sleep remains - though the Japanese are said to regard those who peep at their dreams as perverts."
    "But to leave her freezing would be to take the blame for her possible future cold in advance."
    "A bit of a burden to take on one's soul."
    mi "Mlem?"
    "Clearly asked Miku."
    me "Sleep, mlem."
    "I felt myself literally being turned off alive - my eyes were rolling, my eyelids were slipping..."
    "The last thing I remembered before I fell asleep was:"
    mi "Pum-purum-pum-pum…"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_mi_7dl_ch83:
    play sound sfx_open_door_clubs fadein 0
    pause(1)
    play ambience ambience_camp_center_night fadein 3
    scene bg ext_musclub_night_7dl with blind_l
    play music music_7dl["vale"] fadein 3
    "A dark, warm night greeted me as the door to the music club slammed behind me."
    "On a night like this, like a warm lake, you dive into the morning - and do things that even when you're drunk you don't always dare to do."
    "That's why Ivan Kupala was made just for this time - when every night holds magic and it's so easy to tell a girl you like that she's the best in the world."
    "It seemed a crime to sleep on a night like that."
    "And I almost turned around to shake the obnoxious Japanese pest after all!"
    "And from the woods came the cry of an owl, and from the shore could be heard laughter that could only belong to Alisa and Ulyana."
    "Now I should wear a tube of paste under my shirt and rub the noses of careless pioneers."
    "Gathering at night in an abandoned building and telling stories about Black Hand and Red Sausage."
    "And what do I do? I go and run errands for the counselor."
    dreamgirl "Yeah, Syomich - you are an absolutely boring man."
    th "Thank you. A gloomy bore."
    dreamgirl "I just wonder what would have happened if you had stayed by her side?"
    dreamgirl "Can you imagine? You wake up in the morning together. And the first thing you see when you wake up is each other. Romance!"
    th "Romance, yes."
    "I agreed."
    scene bg ext_square_night with dissolve
    "But in order for me to have any right to do so, I must at least admit to myself what and how I think about Miku."
    "And so far, that's been difficult."
    "She's a very nice person, I feel easy and comfortable with her."
    "So is it worth breaking what has grown so well?"
    "Lena was reading under the lantern again, not paying attention to her surroundings."
    "So I didn't bother her, and I scrambled out of the square."
    "A conspicuous silhouette of the nicest topology, with a pair of very conspicuous braids, flashed by the canteen."
    "The people were not bored. Didn't get sad or paused unless I suddenly included them in the radius of attention."
    "It made me a little sad, but the feeling that this is where life itself is made up for, perhaps, everything."
    me "I like it here."
    "I confessed to the night, to the emptiness, and to the unknowable happiness that came from nowhere."
    me "I like it very much."
    "I guess I wouldn't mind if my childhood years numbered nine years not in that tiny pioneer paradise on the Karelian Isthmus - but here, for example."
    "Because it's great here, too."
    voice "You're not the only one."
    "An unknown voice made me shudder and turn around."
    scene bg ext_admins_night_7dl with dissolve
    "And I didn't immediately see the person who was talking to me."
    "And when I did..."
    show mz normal glasses pioneer with dissolve
    me "Eh?"
    mz "Eh, eh."
    "Good-naturedly she mocked me."
    mz "You can sit next to me, the bench is big."
    me "What do you mean?"
    mz "I mean, I don't care, but it's uncomfortable to have my head up all the time."
    "She was doing something in the dark that I couldn't see in any way."
    me "Zhenya? What are you doing here?"
    show mz smile glasses pioneer with dspr
    mz "Observing."
    "She shared."
    mz "I'm not Slavya, of course, but I can also see if something interesting is going on somewhere."
    "She made a specific movement with her hands again, and I realized what she was doing."
    "Freewholing! Or rather, knitting."
    "Or macramé?"
    "I don't remember exactly, but that first and only day I had to go to that circle was remembered for that particular movement."
    "That's how the fingers of the right hand slip the shuttle between the thread stretched on the left hand."
    me "What are you knitting?"
    "I asked just for the sake of asking something."
    show mz normal glasses pioneer with dspr
    mz "What do you care?"
    me "Reasonable."
    "I noted."
    me "Okay, I'll go. Okay?"
    mz "Go ahead."
    "Zhenya said it was okay."
    "And just as I was about to leave, she threw at my back:"
    mz "Don't worry about Miku, she sleeps there all the time."
    me "I don't..."
    mz "And your chances are far from zero."
    "Zhenya interrupted me."
    show mz angry glasses pioneer with dissolve
    mz "But if you keep being a retard, you won't get any Miku."
    "Zhenya went back to her knitting, losing interest in me."
    "And I didn't dare pester her with questions."
    "In general, until today, I had a definite impression of the Buzzer."
    "But today even if she didn't debunk it,she added clarity and detail."
    "Suddenly it turned out that I didn't really know anything about Zhenya."
    dreamgirl "Yes, just like you don't know anything about Lena, for example. Or about Olga Dmitrievna."
    me "Good night."
    stop music fadeout 10
    play sound sfx_open_door_clubs
    pause(1)
    scene bg int_house_of_mt_noitem_night with dissolve
    "The squad leader wasn't in the house, so I wrote her a letter outlining the fate of her assignment."
    "«Dear Olga Dmitrievna!»"
    "«I found the fugitive, thank you very much, Semyon, let me pat her on the head!»"
    "«But she refused to wake up, so I had to leave her there - I'm not Schwarzenegger!»"
    th "Do you think she'll understand?"
    dreamgirl "I doubt it."
    th "Who then? I only remember Bubka from the athletes."
    $renpy.notify('Wordplay - babka means grandma')
    dreamgirl "Babka, man! He's not that kind of guy."
    th "Well, who? Kozhemyaka, maybe?"
    dreamgirl "Who-who?"
    th "Kozhemyaka."
    dreamgirl "Nikitka? Better Muromets then, what's the point of trifling?"
    th "You're not helping!"
    "I got pissed off."
    dreamgirl "All right, all right! Kozhedub's last name."
    me "Aha! Here."
    "«I'm not Kozhedub - let Kozhedub carry her!»"
    "«And I am a weak and tired creature, who wishes to go to sleep. I wish you the same!»"
    "After rereading the letter again, I nodded contentedly."
    "I left it on the table and went to bed."
    "Very, very irresponsible, I agree."
    "But I was born that way."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_7dl_rain_2gether:
    scene anim prolog_2 with dissolve
    play ambience ambience_7dl["rain"] fadein 3
    play music music_7dl["to_the_sunrise"] fadein 3
    "My words are like confessions from my lips of the most unforgivable."
    "I am guilty before you."
    "I am a hostage to my own stupidity and fear."
    "And the saddest part, perhaps, is my complete inability to fight it."
    "Not because I'm weak or cowardly or infirm."
    "The whole point is that {i}I-can-not{/i}."
    "It's as if I'm being dried up from within, poisonous goosebumps restraining my frail will."
    "And I put down my spear and leave the rallying ground."
    "You have a right to hurt me-I've been gone too long."
    "I had almost forgotten that there once was a We - after all, a whole night had passed."
    scene
    $ renpy.show("bg int_wardrobe_7dl", what = Dawn("bg int_wardrobe_7dl"))
    with dissolve
    with vpunch
    "I was awakened by a tangible poke on my shoulder."
    voice "Get up, you vile deceiver!"
    "The owner of the voice was clearly angry."
    "But I was so sleeeeepy!"
    show blinking
    "My eyes slammed shut, and consciousness hurled me back into the enchanting abyss of unconsciousness."
    "Sometimes you want to sleep, even in your sleep."
    "Like now... Now..."
    play sound sfx_punch_medium
    with vpunch
    "It's like I'm trying to die already, finally, and I'm being harassed with a defibrillator."
    "The blow was hard enough - someone on top was very annoyed. Why else would he have hit..."
    "In the same spot!"
    th "What kind of non-humans are out there in the real world! {w}It's going to be blue!"
    "I'm getting up now, Mom, I'll just lie down for a minute and then I'll be done! Yes!"
    "Oh well."
    "They kept pounding me until they shook the last remnants of sleep out of my heavy head."
    "Only then, realizing it was no use lying there, did I take an upright position."
    "There's nothing to be done, I have to wake up."
    show mi upset pioneer with dissolve
    "And..."
    "Good morning?"
    "The first thing I saw when I returned to the waking world was the extremely displeased look on the face of someone very familiar to me."
    th "So it wasn't the hooligans?"
    "Extremely displeased."
    me "Uhhh… Good mo…"
    "How beautiful this world is, look at it!"
    "I thought about smiling at Miku, saying hello, and telling her how glad I was to see her."
    "Actually, there were a lot of other silly things in the plans. But Miku had her own plans."
    with vpunch
    "She hit me in the already sore spot for the fourth time."
    me "What are you doing, you enemy of the human race?!"
    "I screamed, rolling off my comfy cushion bed - on the other side, just in case; at least it's some kind of protection."
    mi "How could you?!"
    "I almost asked 'what could?' but glimpses of intuition let me know that I would bury myself even deeper with that question."
    show mi sad pioneer with dspr
    mi "What did I ask you yesterday? {w} I waited for you like a baka, I waited..."
    show mi dontlike pioneer with dspr
    mi "Fell asleep while I was waiting! {w}And you didn't even come!"
    "Miku was upset, and she was going to charge me for every second of her ruined mood."
    "Actually, I did come. Here I am, right here. Please love and don't complain."
    me "I'm sorry."
    "I didn't feel guilty just because... What the hell, though?"
    "I did."
    hide mi with fade
    "Miku turned her nose up and turned away."
    "I haven't had much experience with the female sex - in the world, in the home."
    "But it was obvious to me, even to the impenetrably disconnected from female society, that even if I wasn't the main cause of Miku's bad mood, my fault was there too."
    "And it's not that I forgot about the appointment."
    "It's a worldly thing."
    "What's much worse is that Miku felt empty and lonely yesterday after that dried-up old man's visit, and I wasn't there to tell her it was all right."
    "Well, what the hellish kind of a good friend am I after that?"
    with fade2
    me "I'm sorry, please."
    "Penitently, I turned to the straining slender back."
    me "I didn't come, but it was dictated by concern for you - you looked so tired."
    mi "I was not tired."
    "In a steady voice the girl notified."
    me "But I had no way of knowing that. So I decided... not to impose."
    me "Though I came anyway."
    "As an apology, it sounded extremely weak."
    "I reported back tensely."
    with fade
    stop music fadeout 3
    mi "What are you then."
    "Without turning around, she asked."
    "Her voice trembled."
    mi "Sleeping god knows where if you didn't impose?"
    me "I'm sorry."
    "Then she turned around - and I realized that all along she had been hiding a childishly mischievous smile."
    play music music_list["so_good_to_be_careless"] fadein 5
    show mi smile pioneer with dissolve
    mi "Look, Senechka!"
    "Miku wagged her finger at me:"
    mi "This is your last warning!"
    "What will happen next time, I prudently chose not to specify."
    "Miku reached out, got up on her toes, and walked half-dancing from wall to wall."
    mi "I wanted to get some air, but I couldn't."
    me "For a reason?"
    mi "As if you can't hear."
    me "What?"
    mi "Listen."
    "And I listened."
    me "It's raining!"
    me "I really like rain."
    show mi smile pioneer with dspr
    mi "Me too, but it's pouring like a nightmare out there! We can't go out because we're bound to get wet, catch cold and get sick!"
    hide mi with easeoutleft
    mi "Besides, look what I found!"
    "She flew away, drawn by the flow of air; the next moment her voice came directly from the rehearsal room."
    me "What?"
    mi "Come and see!"
    "Impatiently the girl called out."
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg int_musclub_day
    show mi smile pioneer
    with dissolve
    "I had to blink for a few seconds before my eyes adjusted, albeit to the dim daylight - it seemed painfully bright after the closet."
    "Miku was standing at the windowsill, holding a bundle of some kind."
    "There was a note pinned to the side of it."
    me "Forgive me one last time. O. D."
    "I read it."
    me "Seems like someone in the camp has some indulgences?"
    show mi grin pioneer with dspr
    mi "Nothing like that! And anyway! If you don't want a sandwich, just say so - more for me!"
    "I wanted the sandwich. So I prudently apologized and shut up."
    "After looking at me for a minute, the Japanese girl decided to share."
    show mi normal pioneer with dspr
    mi "Okay. Help yourself."
    "In favor of starving me was allotted a cheese sandwich and some obscure cottage cheese - food of the gods practically."
    "Miku, on the other hand, devoted all her attention to the sausages."
    "But Miku wouldn't be herself if she just sat there silently consuming whatever God sent."
    "No."
    with fade2
    pause(1)
    show mi upset pioneer with dspr
    mi "Senechka..."
    "Her face became very, very preoccupied."
    me "Mmm?"
    dreamgirl "Miku is my friend, but breakfast is more important."
    mi "Senechka..."
    "Despite my desperate attempts to ignore the annoyance, the Japanese girl continued to draw attention to herself as best she could."
    "At last her patience had run out:"
    show mi angry pioneer with dspr
    mi "Senka! Stop chewing and look at me!!!"
    with vpunch
    "She screamed in my ear."
    "Her voice was strong and resounding. No wonder, with her way of life!"
    th "Rrrry..."
    "I shook my head, unsuccessfully fighting the ringing in my ears."
    me "Sorry, I was thinking, what?"
    scene
    $ renpy.show("bg ext_musclub_day", what = Desat("bg ext_musclub_day"))
    with dissolve
    play music music_7dl["dance_with_me"] fadein 5
    show mi normal pioneer
    with fade
    mi "Senechka, what town are you from?"
    "Asked Miku, dropping the unmanageable polythene cloth on the floor and sitting down on the step here."
    me "From St. Peteburg."
    "I proudly answered."
    show mi surprise pioneer with dspr
    mi "Is it somewhere in the Urals?"
    me "Yes. It's about there."
    show mi grin pioneer with dspr
    mi "Senechka, I know that St. Petersburg and Leningrad are one and the same!"
    me "Eh. And happiness was so close."
    with fade
    mi "Are all Leningraders a little crazy?"
    "We were sitting under the awning on the open veranda, where a mischievous breeze blew in and out, splashing rain drops in our faces and cooling our damp skin."
    "And now, Miku had no time to dodge another drop down her scruff, hissing like a cat, looking for someone to take her anger out on."
    "No surprise that the victim of the higher anger was me."
    "The question was a trick question, ingeniously posed. The kind of question that can't be answered unequivocally: 'Did you stop beating your wife?'"
    "Yeah. I did."
    me "Uh-huh."
    "On second thought, I answered."
    me "But not all of them. And far from always."
    show mi smile pioneer with dspr
    mi "But you sure are!"
    me "Uh-huh. Mi-ku! Miiiiii-ku! Mikuska-barabuska!"
    show mi smile2 pioneer with dspr
    mi "Wh-at!"
    me "No-thi-ng!"
    hide mi with dissolve
    "Separately, I replied, and turned my nose up and turned away."
    with vpunch
    play sound sfx_water_emerge
    "There was a giggle from behind me, and a handful of water went down my back."
    "I jumped up with a shriek - Miku had already left the immovable object (the bench) between us and folded her hands over her head and whispered:"
    show mi laugh pioneer far with dissolve
    mi "I'm in the cabin, don't hit me! I'm in the cabin!"
    "Laughing, I waved my hand, and as best I could, on myself, wrung out my shirt."
    me "My revenge will be short. But terrible."
    show mi normal pioneer with dspr
    mi "It won't work. I'll keep my eyes peeled, hide well, and throw tomahaw... Oh!"
    hide mi with easeoutbottom
    "The Japanese girl suddenly oohed and ducked behind the bench."
    "Unexpectedly."
    "After tracing the possible direction of the threat, I intercepted the gaze of the unhurried squad leader moving toward us."
    show mt smile pioneer at left with dspr
    mt "Salute to the lazy!"
    "She greeted us."
    mt "Hatsune, don't even try to play partisan. {w}I spotted you."
    mi "Oops."
    show mi upset pioneer at right with moveinbottom
    mi "I was... I dropped my hairpin, and then my shoelace got untied, and..."
    show mt laugh pioneer with dspr
    mt "Yeah, that's what I figured."
    show mt normal pioneer with dspr
    mt "Okay, to the point. Was it good to eat breakfast in bed? Don't blush like that, I've already had my fill of watching you sleeping."
    "She was quiet for a while, enjoying our embarrassment:"
    mt "Anyway, there's a closing campfire scheduled for today, the squad on duty prepared it yesterday, but of course the rain has washed it all out."
    mt "So you, as the two who screwed up, are assigned a responsible party assignment:"
    me "Make the clearing look good?"
    show mi dontlike pioneer with dspr
    mi "Hey, this is exploitation!"
    show mt laugh pioneer with dspr
    mt "No, it's a very responsible assignment. Slavya wanted to go herself, but she has a job in the junior squads, and I can't assign it to anyone else."
    show mt normal pioneer with dspr
    "She grimaced:"
    mt "I can't send Ulyana there. She'll get so dirty she won't wash it off till we leave. I need someone old enough and responsible enough to do it myself and not be Chunya Chumazyme at the fire."
    me "We can't handle it!"
    "I almost said, but Miku was already bouncing around agreeing to everything - the counselor's arguments didn't seem convincing only to me alone?"
    show mi happy pioneer with dspr
    mi "Of course, we are very responsible and mature. You can assign it to us."
    "Yes. It certainly wasn't me that Olga handled."
    "But what would I be, leaving Miku alone in a future job?"
    with fade2
    "No matter how you look at it, Olga's strikes were unmistakably precise."
    "Catching my gaze, she winked slowly"
    hide mt with dissolve
    extend " and departed with truly royal majesty."
    show mi smile pioneer with dspr
    mi "I'd sneak out."
    "Complained Miku, waiting for the squad leader to move away."
    mi "But I found myself in a bad situation."
    me "Yeah? What kind of situation?"
    mi "The opponent was dishonest. He used superhuman capabilities."
    me "Nose like a dog, eye like an eagle, eh?"
    show mi serious pioneer with dspr
    mi "How do you know?!"
    me "I've heard a lot... What really gave you away was your exposed fifth point. Guess that means no forest games for you."
    show mi surprise pioneer with dspr
    mi "Yeah?"
    "Miku mechanically scratched the indicated point."
    mi "Is it really that big?"
    me "Uh..."
    "I studied the subject of the conversation extremely carefully until Miku realized the full significance of the situation, and she bounced away with a squeak."
    show mi shy pioneer far with dissolve
    mi "Hentai! Senechka is a vile pervert!"
    mi "Yeah. You've said that before."
    "She clenched her fists for a few seconds, pondering: two beginnings spoke at once in her."
    "The Japanese demanded that I be beaten immediately, that's what girls are taught from childhood. Even hafu."
    "And the Russian beginning demanded a shrug of the shoulders and an ironic response to the situation."
    show mi normal pioneer with dissolve
    mi "She was also very convincing."
    "Said Miku. Looks like the Russian roots prevailed."
    "God bless."
    me "Yes."
    "I agreed."
    me "Irresistibly convincing."
    play sound sfx_7dl["eat_horn"] fadein 1
    pause(3)
    stop music fadeout 3
    stop sound fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_7dl_morning:
    scene anim prolog_2 with dissolve
    play ambience ambience_7dl["rain"] fadein 3
    play music music_7dl["dance_with_me_piano"] fadein 3
    "Again the rain pours, again your gentle voice calls me..."
    "Individual words are stuck in your memory, images that don't add up to a coherent picture, no matter how hard you try."
    "And then of your happiest days you remember only the sun rolling on your shoulders and the fierce blue of laughing eyes, calling after the owner there, there..."
    "How much I would give to go back to a place where everything was so plain and simple: there were ours, there were theirs, you believed people, and they believed you."
    "And now... A brief respite, after which I will inevitably wake up in the same place where I fell asleep: in a world where people no longer catch the kisses of rain with their lips and run through puddles laughing with happiness."
    "The only thing that makes me happy is that I will come back much richer than I was."
    "As if one could take a breath, spread one's wings and step into the leaden sky, smiling quietly at the simple understanding: {i}you are{/i}."
    "It's silly to call it falling in love; I've been told too often that love has depreciated. {w}But the tiny bit of warmth in my chest is just mine now."
    "You are."
    "Even when I can no longer see you, and you have forgotten me, I will not be less happy about it. For you will still be somewhere."
    "No one can take that away."
    "And I say «thank you» to the world, I say «thanks» to you."
    me "Miku."
    "I whispered."
    show unblink
    scene
    $ renpy.show("bg int_house_of_mt_sunset", what = Desat("bg int_house_of_mt_sunset"))
    with dissolve
    "And woke up."
    play sound sfx_open_door_2
    pause(1)
    show mt normal pioneer with dissolve
    "And, as if by magic, Olga Dmitrievna leaked through the barely opened door."
    "She was dressed in a raincoat, from which raindrops were dripping down in merry rivulets."
    show mt smile pioneer with dspr
    mt "Happy sleepy morning, Sem Semych."
    "The squad leader smiled cheerfully."
    me "Is it raining?"
    "I inquired."
    "She nodded:"
    mt "You slept well, didn't you? Don't answer that, I can tell by your contented face."
    show mt normal pioneer with dspr
    me "Envy is a bad feeling."
    "In tone, I replied, taking my time getting up."
    "However, Olga herself didn't really insist:"
    mt "You woke up early; because of the rain, the general wakeup will only be at half, then breakfast right away."
    me "Not even lineup and exercise?"
    show mt laugh pioneer with dspr
    mt "I can do it individually for you. Would you like one? {w}I'm calling dibs on the big raincoat!"
    me "No, thank you. I'm like everyone else."
    show mt smile pioneer with dspr
    mt "In that case, you can start getting up. There's an extra coat in the closet if you need it."
    "She headed for the door:"
    mt "I'm going to go wake the kids."
    if alt_day3_mi_7dl_donor and (not alt_day4_mi_7dl_ev_savior):
        me "And Miku?"
        mt "Since you've successfully failed your assignment, you'll take care of your friend's sustenance yourself."
        mt "I'm not going up there!"
    hide mt with dissolve
    play sound sfx_open_dooor_campus_1
    pause(1)
    play sound sfx_open_door_2
    scene bg int_dining_hall_people_rain_7dl with dissolve
    play ambience ambience_dining_hall_full fadein 3
    "Miku wasn't at breakfast."
    if alt_day3_mi_7dl_donor:
        "No wonder."
        "From the looks of it, she's asleep at her place - the Sivka's been rolling down a steep hill."
    else:
        "Ulyanka laughed, looking at my confused face:"
        show us laugh pioneer with dissolve
        us "What, Syomich, did you lose your little princess?"
        me "And she's not mine!"
        "I think I said that too hastily, as I caused another set of laughs."
        show us laugh2 pioneer with dspr
        us "Of course, of course!"
        "I felt paint rush into my face."
        with flash_red
        pause(1)
        "However, I was saved from another foolishness."
    show mt normal pioneer at left with dissolve
    mt "Semyon."
    "Olga appeared on the horizon as a panacea, a prophet, and in passing the answer to all available questions."
    mt "A little birdie whispered to me yesterday that you and Miku are thick as thieves now?"
    me "Excuse me?"
    mt "She's stuck at the club."
    "Olga explained."
    mt "And since the comrades have to be helped out..."
    stop music fadeout 2
    scene
    $ renpy.show("bg ext_musclub_day", what = Desat ("bg ext_musclub_day"))
    show rain_overlay
    with dissolve
    "It came out that half an hour later I was knocking on the holy of holies of our Japanese girl with a bag in my hands."
    play sound sfx_knock_door7_polite
    pause(1)
    mi "Open!"
    play sound sfx_open_door_strong
    pause(1)
    scene bg int_musclub_rain_7dl
    with dissolve
    play music music_7dl["tellyourworld"] fadein 3
    play ambience ambience_music_club_day fadein 3
    pause(2)
    show mi smile pioneer with joff_l
    mi "Om, nom!"
    me "Sorry, what?"
    mi "It's very good, thank you!"
    "After chewing it up, Miku replied."
    "The sandwiches she sweeped up with such speed that there's nothing to even think about snatching one for yourself."
    mi "And you, Senechka, you're all right, it turns out!"
    me "Uh-huh. Thank you."
    mi "You just earned five points on Miku's coolness rating, great, huh?"
    "«Coolness rating» sounded too frightening for me to want to know what it could mean."
    me "Mm-hmm. That's just fine. So what kept you from going into the canteen?"
    "No matter how hard I looked, I couldn't find a decidedly single reason for forcing my comrades to lug around in the rain with sandwiches."
    mi "I was very busy!"
    me "That's what I thought. With what?"
    show mi grin pioneer with dspr
    mi "Secret!"
    mi "Very, very, very good!"
    "She cared a lot more about the sausage than me asking some weird questions."
    th "Pragmatism to the bone."
    me "You won't say, will you?"
    "I don't seem to be very welcome here."
    show mi happy pioneer with dspr
    mi "I wfill twfell, shtay hewe!"
    "Invitingly she muttered."
    me "Are you sure I'm not disturbing you? You seem to have been very busy..."
    "...with I don't know what."
    mi "It's okay."
    show mi happy pioneer with dspr
    mi "You'll be my husband!"
    me "Ahem... I'm sorry, who?!"
    "Was it me, or did I mishear?"
    dreamgirl "What's wrong? You've just been asked to marry, say yes, man!"
    "Bullying all at once from inside and out."
    "I have no friends at all."
    "No one loves me, no one's gonna hold me..."
    show mi normal pioneer with dspr
    "Finally, Miku took pity on me."
    mi "I mean, if the female is a muse, then the male is a moose? Isn't it?"
    me "I guess so."
    "Cautiously I answered."
    show mi smile pioneer with dspr
    mi "There! You'll be my male muse."
    mi "You don't mind, do you?"
    me "It depends what I have to do."
    mi "Sit still and look cool. Yes! That's it."
    "Barely swallowing a particularly large piece of white bread and sausage, the Japanese girl bounced to her guitar and pounded her fingers, brimming with fat, on the strings."
    mi "I always get inspired when it rains! Or inspiration? You inspire me, so inspiration!"
    "I looked through her at the rain pounding on the windows."
    "Miku was nice to me. It would be very unkind if I said I got a headache from her chatter."
    "Not listening to her anymore, I turned the recliner and settled in with my feet."
    "True, because of the uncomfortable position and the snug, wet fabric, my shorts instantly fluffed up in folds, causing the most animated interest from the piano."
    "After crossing my legs for a couple of minutes, still feeling like a blonde in a miniskirt, I settled in humanly."
    "Miku was musing the whole time, humming something to herself."
    "Talent is talent even in «Sovyonok» - the ear began to pick up the harmony after a few bars."
    "Listening, I intercepted her gaze."
    "Embarrassed by the way I stared at the Japanese girl."
    "Miku winked and started the song again."
    stop music fadeout 3
    "She fumbled for a tune, repeated several times..."
    "She exhaled, and..."
    scene cg d4_mi_guitar_club_7dl with fade2
    play music music_7dl["kiss_you"] fadein 2
    "I felt like I was all alone here - alone with the rain's breath and the strings' ringing silence."
    "Miku was somewhere else."
    "Not here."
    "I could physically feel her warmth, touch her, see her - but her gaze was fixed on unimagined, unfulfilled distances."
    menu:
        "Is that why you didn't go to breakfast?":
            $ alt_hpt += 1
            "Miku nodded slightly embarrassed."
            me "You're a fascinating person, Mikuska."
            scene bg int_musclub_day with dissolve
            "I informed her in no uncertain terms."
            show mi shy pioneer with dspr
            mi "What? No!"
            "She seems to have discerned in my words something quite different from what I put there."
            "Why else would she rush to refute me?"
            me "It's not like I said anything wrong. I'm just glad you put so much effort into your hobby."
            dreamgirl "Wrong, you, Uncle Fyodor, are lying. You're lying to yourself - and you should be lying to those around you."
            mi "Are you going to accuse me of putting music first, too?"
            me "Why should I?"
            me "I respect a person's right to go as crazy as they want."
            show mi smile pioneer with dspr
            mi "Good how you said it."
        "What a beautiful song":
            $ lp_mi += 1
            $ alt_spt += 1
            "She shifted her gaze to me, struggling to return to objective reality."
            "I involuntarily stared at her-any pathology unwittingly attracts attention."
            "There's a complete fascination in her gaze in which there is and will be no room for anything else."
            "She's made up her mind, so it's up to others to accept that they'll always be present on a residual basis..."
            "Or self-effacing."
            "And with that outlook, she will inevitably succeed - because she won't stop and she won't give up."
            "Have I ever seen a look like that in the mirror?"
            "Or is there really a lack of passionarity?"
            mi "Thank you."
            "I was burned with instant envy - nothing I could ever boast of like that."
            "I can almost see the expression of my own eyes at the bottom of her pupils - the perfect conversation - mirror."
            "What can I see there?"
            "A pale, colorless, wavering figure?"
            "Not my present appearance, but that fellow of little more than thirty, stubble, bags under his eyes, a mop of unshaven hair..."
            mi "Senka!"
            "She focused her gaze, and the illusion disappeared."
            mi "Thank you for feeding the starving one! You're the best friend ever!"
            "And she kissed me on the cheek."
            "Her kiss smelled of half smoked sausage and white bread."
            "Greasy fingers left stains on a shirt that was almost dry."
            "And yet, in spite of this, I felt an incomprehensible satisfaction."
            "And Miku, as if pouring all her reserves of recklessness into this gesture of hers, recoiled back, blushing thickly."
            scene bg int_musclub_day
            show mi shy pioneer
            with dissolve
            mi "Oh. That was very close."
            "She mumbled, settling back down."
            "She tilted her head so that her hair hid her flaming cheeks."
            "I still manage to catch the wet glint in her eyes, though."
            "And that's great."
            "So she's alive after all."
            "Slipping her fingers aimlessly over the strings - the guitar responded with an unsteady sound-Miku sat for a few more seconds."
            mi "Too close."
            hide mi with moveoutleft
            "And then she stood up and, as if without noticing me, went out the door."
            "I, seized by the shared shame, the sympathy, was afraid to get up or even call out to the girl."
            "Strange."
            "It was about noon on the clock when it all happened, and after another half hour I realized she wasn't coming back."
    play sound sfx_7dl["eat_horn"] fadein 1
    pause(3)
    stop music fadeout 3
    stop sound fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_7dl_dinner:
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 5
    play music music_7dl["genki"] fadein 1
    if alt_day4_mi_7dl_ev_savior and loki:
        "To start from scratch is not insanity. Insanity is leading a miserable life, wandering around in a dull stupor, day after day, day after day."
        "Insanity is to pretend to be happy, to pretend that this is the strap you have to pull all your miserable life."
        "Miku looked friendly and somewhat challenging as I crouched on the bench beside her."
    else:
        "After shutting the club door tightly, I headed out for lunch, figuring, rightly, that if Miku had attacked the sandwiches with such enthusiasm, she would hardly want to be deprived of lunch."
        "So she did."
        "She was embarrassed for a moment when she felt my gaze, but - an artistic nature - she immediately got over herself and looked up."
    show mi normal pioneer with dissolve
    me "I'm going to land, do you mind?"
    "I asked with a look as if a couple of tractors couldn't move me from this spot."
    show mi smile pioneer with dspr
    mi "Of course, of course, Senechka."
    "She looked around - no one was looking at us, and it was all the more amusing that she was playing some kind of obscure spy."
    mi "Senechka, I wasn't really interested, but how do they generally treat people here if someone suddenly decides to... well... that..."
    me "That?"
    show mi normal pioneer with dspr
    mi "Yes!"
    show mi shy pioneer with dspr
    me "And this «that» — what could it mean?"
    mi "Well... you got it!"
    me "No."
    "I answered honestly."
    mi "Oh... I meant when a boy and a girl want to..."
    stop ambience fadeout 0
    me "Ah! You mean «dating»?"
    "She caught my hand and wrote something on the palm with her finger."
    "For a moment the babble of the pioneers eating had died down, so my voice, deliberately loud enough to outshout that same babble, sounded especially loud."
    "To the whole canteen."
    with flash_red
    "The attention of the audience was instantly riveted on my humble person."
    "And hafu, with vindictive happiness in her eyes, just as loudly confirmed:"
    show mi laugh pioneer with dspr
    mi "Yes, exactly dating!"
    "I really wanted to fall through the ground."
    "Or be somewhere far, far away from here."
    th "She did that on purpose, didn't she?"
    dreamgirl "No doubt!"
    "A piece of cutlet got stuck in my throat."
    play sound sfx_chair_fall
    with vpunch
    scene bg int_dining_hall_people_day with fade
    "I jumped up and rushed out of the canteen."
    with fade
    scene black
    pause(1)
    scene bg ext_dining_hall_near_day with dissolve
    play ambience ambience_camp_center_day fadein 2
    play sound sfx_run_forest fadein 1
    "The door slammed."
    "And, judging by the stifled laughter, Miku was running after me the whole time."
    me "And that's what you did?"
    show mi normal pioneer with dspr
    mi "What?"
    me "Why were you yelling at the whole canteen?"
    show mi smile pioneer with dspr
    mi "Why did you?"
    me "So I was asking back!"
    show mi happy pioneer with dspr
    mi "And I answered!"
    "I didn't really understand what it was she was happy about, but I decided not to elaborate."
    "So far, absolutely every interaction with a Japanese girl has only drowned me deeper."
    "It's not hard to guess, for example, what the questions in the canteen would lead to."
    "There - the pioneers walking past us are already squinting with undisguised curiosity."
    "So I just waved my hand."
    "Sat on the bench with the clear intention of doing nothing. You never know."
    show blinking
    "Even covered my eyes for a moment."
    "True, indeed - for a moment."
    "I was instantly pushed to the side and asked indignantly:"
    mi "Are you going to sit like that now?"
    me "What's wrong with that?"
    mi "I'm bored!"
    me "My condolences."
    show mi upset pioneer with dspr
    mi "Senka! Don't be a buzzkill!"
    me "Why not? I've lived like this so far, it's never failed me."
    mi "It's time to change, then! You're my friend and comrade now."
    dreamgirl "And sexual partner, of course. Homo homini!"
    th "Shh, coomer."
    me "Yeah. What's next?"
    show mi serious pioneer with dspr
    mi "What's next is that you have no right to make me upset and sad, or I'll be upset and sad!"
    th "What a woe!"
    me "Alright."
    "Damn my built-in politeness."
    me "I'm not going to upset you. What do you want?"
    mi "Entertain me!"
    me "What do you mean?"
    mi "Well..."
    show mi normal pioneer with dspr
    mi "I'm thinking, now that you're a hero, always coming to the rescue, I should knight you."
    me "I have a bad feeling about this."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_7dl_router:
    scene bg ext_house_of_mt_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    play music music_7dl["will_you"] fadein 2
    $ set_mode_nvl()
    "The biggest problem of the modern world is that for the last fifty years we've probably been trying to inoculate ourselves into thinking that there is some kind of magical, hidden world."
    "A hidden world of existence."
    "Which lies on the other side of the madness."
    "And that's when all the filth that's been building up inside you reaches the right boiling point, making you squeal with hatred and do irreparable things - a magical world, you're sure, is waiting for you."
    "A new plane of reality."
    nvl clear
    "For everyone deserves exactly the reality to which he has aspired."
    "You'll be met by either Tyler Durden or Angelina Jolie with a Beretta. Knowing how to shoot in an arc."
    "Except there's nothing there."
    "Maybe there used to be - the ideologists must have been inspired by something."
    "Not now."
    nvl clear
    "And if anything depends on you, the gray nothingness of the underside of the world will be your grave. At best."
    "Otherwise, things are much more dull and simple."
    "Hysteria ends in emptiness. No one meets you."
    "You just get expelled. Fired. Chased away."
    "And you, smashing other people's heads with furious blows, are left out."
    "Unwanted. Forgotten."
    nvl clear
    "You're forced to stop and look yourself in the eye."
    "And then you end up looking for a job anyway."
    "Not because of money or hunger."
    "It's just that a man can't be absolutely worthless."
    nvl clear
    "And the explanation is simple: every time you got off the rails, reality - shiny, beautiful, three-dimensional - turned a new face toward you."
    "And you, like a crystal playing with it, knew more and more. Without shyness or looking back."
    "For the crystal is infinite, so there is no number of facets that can be revealed to you."
    "But the modern generation has been kicking too long and fiercely, jumping on our poor, crippled reality."
    "Got their way."
    "Now it's just a two-dimensional object. Like a manhole cover, which is extremely dangerous to jump on."
    "But who would explain and put up a guardrail sign?"
    nvl clear
    "Miku?"
    "Our vacation is little by little coming to a logical end - even if we don't part ways for the next couple of days, customs will be coming soon, Vladivostok."
    "Sakishita."
    nvl clear
    $ set_mode_adv()
    "I squinted my eyes at the serenely smiling Japanese girl."
    "Something has changed between us - we've both taught each other something new."
    "But so we continue to be awkward-not-knowing-what-to-say from time to time."
    "Not because one embarrasses the other."
    "It's just that both find themselves in a situation they've never been in before."
    "Anyway, we do have an extremely fun time together."
    "But - really - there's always a hovering understatement between a woman and a man."
    show mi normal pioneer with dissolve
    mi "I need to discuss something, Senechka."
    me "What is it?"
    mi "First you have to promise not to be offended!"
    th "Aw shit, here we go again."
    me "No, I won't promise anything. But keep talking, keep talking."
    show mi upset pioneer with dspr
    mi "Senka! Is it hard for you to make such a simple promise to a girl?"
    me "For me?"
    "Very much. What if it's pedonecrozoophilia with perversions?"
    th "So walk away with your promises."
    "I sighed."
    me "Okay. I promise not to be offended."
    show mi happy pioneer with dspr
    mi "You promised!"
    us "Promised what?"
    me "Eh?"
    show us laugh sport at left with moveoutbottom
    us "Tell me about it!"
    me "But..."
    show us grin sport with dspr
    us "Tell me, tell me! Come on, come on!"
    "She shouted it with such enthusiasm that we seemed to be heard in the squad leader's cabin."
    "From there came the creaking of the bed, the grunting of a person scraping himself off the bed and..."
    scene bg ext_square_day with dissolve
    "We didn't listen to any more - it was like the wind blew us away toward the square."
    show mi smile pioneer at right
    show us smile sport at left
    with dissolve
    us "Now tell!"
    mi "There's nothing to tell yet, I just started when you interrupted us."
    us "So I got to the very beginning of something interesting?"
    show us surp1 sport with dspr
    us "Hurrah! Tell me about it! Have you decided to date?"
    show mi shy pioneer with flash_red
    mi "What? No!"
    show us surp2 sport with dspr
    us "How not? {w}I heard everything in the canteen, you decided to become a couple!"
    me "You're wrong at being wrong."
    "Was it just me, or did Miku flinch slightly at those words?"
    "At the edge of my consciousness, the call of my resting intuition half-asphyxiatedly trumpeted."
    mi "It seemed to me that Senechka and I had become such good friends!"
    us "Don't go on, I get it. {w}You want to kick Lenka out of the cabin and put your little brat in her place?"
    show us laugh sport with dspr
    us "It's going to be a real love nest!"
    show mi normal pioneer with dspr
    mi "Ul'ka, you're always talking about love. Is it a sore subject?"
    show us shy sport with dspr
    us "What?! No! How could you think!"
    "Ulyana looked shocked by Miku's rebuke - how dare Miss Insouciance walk all over her abuser!"
    "And who could have taught her that?"
    "The eyes of her suspiciously narrowed eyes stopped on me, but Miku had time to retort early:"
    mi "I need an assistant for tomorrow's concert! I can't do it alone, and I'm lonely in general! So there!"
    me "And you want to ask me to help you?"
    mi "Yes!"
    me "But then you'll have to ask the squad leader, let her know..."
    show mi shy pioneer with dspr
    mi "Actually, I had already arranged everything with Olga-san, I told her in advance that you agreed."
    th "Now I see why she begged me in advance to promise not to be offended!"
    me "What a bug you are!"
    show us grin sport with dspr
    us "She's a girl, Syomich!"
    me "What's the right way then? Beetle?"
    show mi laugh pioneer with dspr
    mi "Is this to be understood as agreement?"
    me "No!"
    show mi normal pioneer with dspr
    mi "Well, Senechka! Everyone's around already has some company - Ulyana and Alisa, Lena was taken away by Zhenka, and Slavya has no time at all."
    mi "I thought we got along well."
    me "Not when they marry me without me."
    show mi surprise pioneer with dspr
    mi "What do you mean?"
    "I waved my hand."
    me "Bygones. I just don't want a commitment. I never signed up, and I don't want to now."
    mi "But, Senechka..."
    show us smile sport with dspr
    us "He's just afraid of falling in love with you."
    th "It's all about what, but the louse is all about the bath."
    me "Better than falling in love with you."
    show us calml sport with dspr
    us "Oh tell me, please! What's wrong with me?"
    me "Let me think..."
    extend " everything!" with vpunch
    show us dontlike sport behind mi with dspr
    us "OH YOU! I'll..."
    show mi dontlike pioneer close at cleft
    with dissolve
    mi "Okay, that's it! Break! Go to your corners!"
    "Miku hurriedly cut in between us before it got to the point of self-harm."
    mi "Senechka, will you tell me why you refuse?"
    "And it remains to be seen who will be harmed - I'm bigger, but petty is nasty just like that..."
    me "Take the little one."
    "I offered from the bottom of my heart."
    me "Alisa won't mind, I'm sure of it."
    show us normal sport at fleft with dissolve
    us "Slave-trader."
    "Ulyana muttered, pointing her tongue at me from over Miku's shoulder."
    show mi normal pioneer at right with dissolve
    mi "Ulyana? That's possible, but she's not good with equipment."
    "The little one nodded her head in exasperation - she really isn't."
    me "Oh, that's okay. {w}We'll teac…"
    show us dontlike sport close at left
    show mi dontlike pioneer close at right
    with dissolve
    play sound sfx_punch_medium
    with vpunch
    pause(3)
    show us normal sport at left
    show mi normal pioneer at right
    with dissolve
    "Miku lost her patience. Ulyana lost her patience."
    "I've been slapped on both sides."
    mi "Senechka, you don't seem to get it."
    "I guess I didn't. I didn't understand anything."
    stop music fadeout 3
    scene bg ext_musclub_day
    with dissolve
    play ambience ambience_camp_center_day fadein 5
    "But half an hour later..."
    show mi normal pioneer with dissolve
    play music music_list["everyday_theme"] fadein 5
    mi "So, look what we need..."
    me "We need to go to the cabins, since it's quiet hour."
    show mi smile pioneer with dspr
    mi "Did you say something, Senechka?"
    "Miku fondly smiled at me."
    me "No, go on, what do you mean."
    stop ambience fadeout 2
    play sound sfx_open_door_2
    pause(1)
    scene bg int_musclub_day
    with dissolve
    play ambience ambience_music_club_day fadein 3
    stop ambience fadeout 5
    dreamgirl "My name is Ash. I'm a slave. But it wasn't always like this."
    th "Oh, shut up you."
    show mi happy pioneer with dspr
    mi "We have a lot of work to do today! Hooray?"
    me "No."
    show mi laugh pioneer with dspr
    mi "You're such a joker! Ha-ha-ha!"
    mi "Let's start by revising the equipment we're going to use."
    me "What did you use before that?"
    show mi smile pioneer with dspr
    mi "It doesn't matter."
    mi "Your job will be to bring the wires from the black bag to the stage and check the contacts. Can you handle that?"
    me "Mm-hmm."
    mi "You're my darling. Give me a kiss!"
    "She jokingly reached for me, and I just as jokingly recoiled and rattled something in the bags and sprinted out into the street."
    stop ambience fadeout 3
    scene bg ext_sky2_7dl
    with blind_r
    "Except for the tiny 8x8 mixer, which Miku carried in her hands, trusting no one, all the work of carrying fell on my frail shoulders."
    "And when I say 'all,' I mean all of it, from start to finish."
    "I'm sure if I'd been heavy enough, she would have made me carry the speakers too."
    "Luckily, it wasn't too extreme."
    dreamgirl "Why do you let her push you around like that?"
    dreamgirl "The last person who tried to pull something like that on you, you got out of your life with particular cynicism."
    me "Hey, I thought slavery was abolished last century!"
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_stage_near_clear_7dl
    show us laugh sport far at right
    with dissolve
    us "Work, niggas! Sun's still high up!"
    me "You should keep quiet..."
    "I muttered."
    "The whole time I was running around the stage in the soap and so forth, Ulyanka was watching me, saddled on a speaker."
    "Apparently, watching others work gave her great pleasure."
    "What can I say - a future boss growing up, no less."
    show us surp1 sport with dspr
    us "If I don't watch out for you, you're bound to screw something up! So arbeiten, schnell!"
    me "Jawohl, Herr Idleman."
    show us surp3 sport with dspr
    us "Oh, Miku!"
    me "Where?!"
    "I shuddered, turning around."
    show us laugh sport with dspr
    $renpy.notify('Childish taunt')
    us "Cheated a fool with four fists!"
    me "Eh you..."
    "I waved my hand and huddled on the edge of the stage."
    "The heated boards smelled like tar and dust, and for a change it was nice to sit down and have a little rest."
    "Ulyana said something else, but I didn't listen."
    "I was provided with food for thought - or rather, was provided with it for the last two hours."
    "I needed to think about what was going on."
    show us normal sport with dspr
    us "Miku was sad for the last week before you came."
    us "It's good that you cheered her up."
    th "There was no sadness."
    "I reacted in my usual cynical way, but I was surprised at how observant the little one turned out to be."
    me "Yeah. Clowns, jokes, fun."
    show us smile sport with dspr
    us "Sort of!"
    me "Uh-huh."
    us "Will you show me your performance?"
    me "What do you mean?"
    show us normal sport with dspr
    us "For tomorrow's concert."
    me "I don't have any performance."
    us "What do you mean? What did you sign up for, then?"
    me "I didn't sign up anywhere!"
    us "Mikuska said you did!"
    "Ulyana said unhesitatingly."
    me "I'll tell her something myself now. Where is she, by the way? She was just here."
    "I just now noticed that I've been fiddling with the little one for the last fifteen minutes, and I haven't been cheered up once in that time."
    show us smile sport with dspr
    us "Rehearsing, as usual. She hardly ever rests, in case you haven't noticed."
    show us laugh sport with dspr
    us "Only when you're working in her place!"
    "She waved her hand, jumped off the speaker and went off somewhere on her own business."
    stop music fadeout 3
    hide us with dissolve
    stop ambience fadeout 5
    with fade
    scene black
    pause(2)
    play sound sfx_open_dooor_campus_1
    pause(2)
    scene bg int_wardrobe_7dl with fade2
    play ambience ambience_music_club_day fadein 3
    play music music_list["she_is_kind"] fadein 3
    "I had to look for Miku for quite a long time - because I couldn't find her in the places where it would be logical to expect to find the singer — at the stage or in the rehearsal room - neither in the places of rest and idleness."
    "At one point I even had the fantastic thought that perhaps, while I was running around with wires, she might have been kidnapped and taken away somewhere."
    "Fortunately, about the third time I walked by the club, I heard a stomping sound from inside and tiptoed indoors."
    if loki and alt_day4_mi_7dl_ev_savior:
        "Where she and I slept tonight."
    "And Miku was here."
    "It was hard to call it a dance or a rehearsal - more like a practice session."
    "She was all sweaty, breathing heavily, and there were large, clear drops of sweat frozen on her forehead."
    "It occurred to me that maybe that's why she was driving me so hard, because she doesn't treat herself with any more indulgence."
    "No self-pity."
    "Not a bit."
    "And yet she looks surprisingly appropriate in that silly tracksuit with the turquoise shoulder-straps."
    "Although, you'd think, what's there to plow through? It's summer, the heat, the camp! You should be resting!"
    "But she doesn't seem to know how to rest at all."
    "Unlearned? Or is it some sort of escape from reality?"
    "I'm used to seeing her as a light-headed fool-singer: butterflies in her head and a hollow between the ears."
    "Yesterday she showed herself to be a little deeper than I thought."
    "Today, a new facet of personality."
    "Not without problems, oh so not without problems."
    menu:
        "You're really pushing yourself":
            $ lp_mi += 1
            $ alt_hpt += 1
            "I raised my voice."
            "My attitude would hardly change toward a person who doesn't know how to indulge those around him."
            "But I can help that person."
            "Without a second thought."
            "There was a brief déjà vu in my mind as I picked up a towel from the shelf and walked over to Miku and blotted her forehead."
        "Stay silent":
            $ alt_spt += 1
            "I just had to silently admire the way the person literally lives the art."
            "I can't do that."
            "But I am capable of seeing it."
            "However, Miku - fortunately or not - managed to see me in the rose-top hold, paused playback, and turned to me."
            me "I have finished everything you instructed me to do."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_7dl_lost:
    scene bg int_wardrobe_7dl with dspr
    me "Shall we go outside and get some air? I'm tired or something."
    "She nodded and let herself be led outside."
    pause(1)
    play ambience ambience_camp_center_day fadein 3
    play music music_7dl["ltyh"] fadein 3
    scene bg ext_musclub_day with fade
    "And I don't know what came over me, but as soon as we got settled on the bench, I confessed:"
    me "It fascinates me the way you dance."
    show mi shy casual with dissolve
    mi "Really? Thank you, I'm touched. It's a special type of choreography, it has to be performed in our traditional kimonos, not a t-shirt, so you haven't seen everything."
    th "Gibbering. Excited."
    "With unexpected tenderness I thought."
    mi "What did you think of the performance?"
    "I remembered that Miku had signed me up for the performance. Even though I didn't give my consent!"
    me "I think you shouldn't have signed me up for that!"
    show mi laugh casual with dissolve
    mi "It's not you, baaaaka."
    "A little chuckle came from the girl."
    mi "It's a place for me, so they won't say I'm putting too many performances for myself."
    "And I shut up."
    "Immediately I clamped down on all my feckless hubris, stifled the claims."
    "I could have guessed right away!"
    "That immediately raised my attitude toward her from neutral-irritated to almost sympathetic."
    dreamgirl "You're making a storm, sir. It's time to get married, I guess."
    "And, whether in spite of it or for some other reason, I let a bit of resentment seep in."
    me "I would help you as it is, without your appointments or orders."
    show mi smile casual with dspr
    mi "Oh you! Is this a riot? A peasant revolt?"
    "She giggles and tickles my side."
    mi "At the frooont is Stenka Raaaaazin, cuddling with the princess."
    "She purrs."
    mi "Will you rebel, eh? Will you?"
    me "I will not. But why all this harassment? Can't you do it in a human way?"
    mi "I can. But can I sometimes feel like a satrap and an autocrat?"
    dreamgirl "So smug!"
    me "Do I have to be the one paying for that?"
    show mi grin casual with dspr
    mi "How else could it be? You're the closest thing I've got here, you're not going to fight back..."
    me "Uh-huh. And?"
    mi "The perfect candidate!"
    "Until some point I was too unneeded by others and generally didn't need them myself."
    "But even to my unsophisticated eye, the subject of friendship doesn't involve one friend slaving over another!"
    "Especially now that I have begun to feel a {i} peculiar{/i} interest in a gi..."
    "I stopped and once more carefully reconsidered the terms."
    "And I realized suddenly that I hadn't felt anything so special for a couple of hours - just the same hundred and twenty minutes of humiliation and abuse."
    "Whatever the hafu did, it worked without fail!"
    me "What a bitch you are."
    "From the bottom of my heart I confessed."
    show mi serious casual with dspr
    mi "You finally figured it out!"
    me "Figured what out?"
    show mi sad casual with dissolve
    stop music fadeout 3
    mi "That I'm not an empty-headed singer, eyelashes flapping, wings bang-bang, that I have days when I want to take a shotgun and shoot the hell out of everybody."
    play music music_list["so_good_to_be_careless"] fadein 5
    mi "I am alive, Senya. And the fact that you have seen this is already a tremendous progress compared to all the others. {w}Maybe we really have become closer?"
    me "I'd rather have the old illusions."
    "I grumbled."
    show mi happy casual with dspr
    mi "And no one asked your opinion on that!"
    "That Japanese bitch blossomed again."
    "She stirred up mixed feelings."
    "How she did it is unclear. But I was thrown from a desire to preserve the fragile and infinitely blue that she awoke in my soul by her mere presence - to just a frantic desire to strangle her."
    "She was sitting too close on the bench, and only now did I notice it."
    th "What if someone sees!"
    "A thought flashed through my mind. And I hurried to sit further away."
    "At a questioning look I asked her:"
    me "You've never heard of the intimate zone? You're invading my zone."
    show mi smile casual with dspr
    mi "Sorry, I didn't know you were that shy."
    "She didn't look the least bit remorseful."
    "Because she immediately moved closer."
    "It would have looked like sexual harassment - by anyone else."
    "In Miku's case, though..."
    mi "Hmmm? Where are we going?"
    "Our knees were touching again."
    "It was the end of the bench from there, there was nowhere to move."
    "Had to endure."
    with fade
    "And somehow it didn't even occur to me that I should be enjoying myself instead of being shy like a gymnasium girl on a first date."
    "And then there's that smile of hers - it's either a perfectly saintly smile, or a completely depraved one."
    "I didn't know where on this category scale Miku belonged, which made me even more nervous."
    me "I've never seen you wear those clothes before."
    "I said just for the sake of breaking the silence."
    me "Something wrong with the uniform?"
    show mi grin casual with dspr
    mi "Oh, you haven't seen much of my closet yet!"
    mi "And there's nothing wrong with my uniform, I just didn't want to get it dirty - see the way I look."
    "She jokingly nudged me with a sticky, sweaty shoulder."
    dreamgirl "Vomit-inducing, if I'm allowed to rate."
    mi "I thought I'd do a couple more runs, and then go to the bathhouse - wash myself off."
    mi "But then you showed up!"
    th "I hope that doesn't mean I have to wash her clothes now?"
    dreamgirl "I hope it means you'll have to do her washing now!"
    "In tune noticed my spoiled alter ego."
    "Apparently I wasn't tired enough after all, for the image instantly jumped into my mind, and I hurried to put cross my legs."
    "We can only hope she didn't notice anything."
    "Or?"
    "She moved again, as the change in position of her feet caused us to lose contact."
    "Word will get around the camp - she'll play hard to get."
    dreamgirl "Or the idiot will get the idea that with her record, she's learned to ignore public opinion when she needs it in the first place."
    "But I brushed those words aside, too."
    "Finally Miku got tired of embarrassing me, and she got up:"
    show mi normal casual with dspr
    mi "Alright, I'm going to wash. Will you close up in here?"
    hide mi with dissolve
    stop music fadeout 3
    "And, without waiting for a nod, she left."
    with fade
    "As I unplugged the equipment and slammed the door, I caught myself wondering - with the way of life Miku leads, with the environment she has in her home country..."
    th "Does she have a young man?"
    dreamgirl "Or is she more broad-minded - and has a girlfriend! Just imagine - two young trained bodies under the sheets..."
    th "Begone!"
    "On the veranda on the bench I found a bath towel of Miku's favorite color - turquoise."
    "Must have gotten so carried away, embarrassing me, that I forgot it on the bench."
    scene bg ext_bathhouse_day_7dl with dissolve
    dreamgirl "Well, shall we go? Shall we look?"
    th "No way!"
    dreamgirl "Dude! She took you for a ride the day before yesterday! {w} And she caught you with it! Don't you want revenge?"
    dreamgirl "Just imagine: she's there now... Large drops on her skin, goosebumps, the graceful sagging of her back..."
    menu:
        "No, I cant":
            $ alt_day5_mi_7dl_voyeur = True
            dreamgirl "So it's like last time. Not on your own. You don't have to do it yourself, or else..."
            th "You mean the phone?"
            dreamgirl "Yeah!"
            "The idea of preserving the look of the best girl naked for posterity so captivated me that I didn't hesitate any longer."
        "I don't want any revenge":
            $ alt_hpt += 1
            $ alt_spt += 1
            "Especially since there's something about the way she looks..."
            "I don't know how to put this, but if we have sex between us, it would ruin everything."
            "So to hell with it."
    scene bg ext_bathhouse_day_7dl with joff_r
    if not alt_day5_mi_7dl_voyeur:
        "Half an hour later, handing over the towel, I sat down on a bench next to the bathhouse."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_7dl_hn:
    scene bg ext_bathhouse_day_7dl with dspr
    play music music_7dl["genki"] fadein 3
    with flash_red
    "I had stopped the nosebleed from coming out of my nose."
    "And no, it wasn't the hentai overstimulation pattern at all."
    "It was just Miku catching me hot and tapping me in the nose without too much procrastination."
    "That's all."
    "I shouldn't have gone into the anteroom, much less looked in the window."
    "Because a few seconds later there were already two of us in the anteroom, and Miku, after checking to see if I'd seen everything, gave me a poke in the nose."
    "To cool the fervor, I take it."
    "The blood wouldn't stop, and the fervor, if there was any, had long since cooled."
    show mi sad pioneer_transp with dissolve
    mi "Doesn't stop?"
    "A wet, cold compress came down on my nose - in a white and turquoise streak."
    "I preferred not to think about what it might have been."
    me "No. No stop."
    "I mouthed."
    mi "It's nothing. It'll go away soon."
    mi "You tell me, why are you peeping? Don't lie that you were so interested in seeing my skinny bods."
    "And how do I tell her now that after the line about her possible lesbian tendencies, she's causing me the most painful interest?"
    scene bg int_dining_hall_people_day
    with joff_r
    play ambience ambience_dining_hall_full fadein 5
    "The nose healed closer to noon - and obscene things popped into my head again."
    "I even thought about going over to Miku's for another shot of nose refresher."
    "Because no matter what, I still want to see and look at her without a dash of unnecessary carnal."
    "I like her."
    "But it's almost impossible to communicate with her - there are so many pitfalls, and you have to maneuver with jewel-like precision."
    "So I ignored her inviting look and, grabbing a muffin off the tray, left the canteen as quickly as I could."
    "The frayed emotions should have been combed, and Miku, with her whipmaker-level delicacy, had no way to help me."
    "Or?"
    play sound sfx_open_dooor_campus_1
    stop ambience
    scene bg ext_dining_hall_away_day
    with dissolve
    "Keep your distance, keep your distance..."
    "Doesn't really work as a mantra, to be honest. But I couldn't think of anything better."
    "Especially since after the lunch she ignored me and went back to her training."
    "She seemed offended."
    "I guess I'm being very pig-headed."
    "I guess I should have handled this differently."
    "But whoever with a ladder wit has never once bemoaned himself for past lapses, please, the stones are at your service."
    "I staggered to the washbasins - I did get my shirt dirty, after all, and I appeared to be showing off in the canteen with stains on my chest."
    "Good if they were disguised by the camouflage petal, but I didn't hold out much hope for a miracle."
    stop music fadeout 3
    scene bg ext_washstand2_day
    with dissolve
    play sound sfx_open_water_sink
    pause(2)
    play sound_loop sfx_water_sink_stream
    play music music_7dl["melancholy_sun"] fadein 3
    "The water was warm enough, and on the edge of the footwash someone had left a bar of laundry soap with the still-readable «72%%» written on it."
    "But the blood still came out really disgusting."
    "I've re-soaked and re-washed my shirt probably four times now."
    "I couldn't believe I was in this stupid situation."
    "Laundering the blood I'd dripped from my broken nose for trying to spy on a pioneer girl."
    "Nightmare."
    play sound sfx_hiding_in_bush fadein 0
    un "H-hello…"
    scene bg ext_washstand_day with dissolve
    "I raised my eyes."
    play sound sfx_close_water_sink
    stop sound_loop
    "Lena stood with a heel of apples clutched to her chest - she must have been on her way here to wash them."
    "But she hovered - standing there, peering at me, waist-deep in nudity."
    "Not an Apollo figure, of course, but..."
    show un shy pioneer with dspr
    "Lena gave an ouch and blushed when I intercepted her gaze."
    "Hastily she turned away."
    un "I'll… Uh… W-wash the apples, can I?"
    me "Sinks are common."
    "I shrugged."
    "She nodded weakly and, turning on a thin, thin stream of water, set about washing the fruit."
    "And I tried for the fifth time, to no avail, to scrub the blood from the cotton."
    "To no avail meaning 0.0%% success rate."
    show un normal pioneer with dspr
    un "Did you have a fight with someone?"
    me "You could say that..."
    "I answered evasively, feeling the tips of my ears flare up."
    "After finishing washing the apples, Lena was in no hurry to leave for some reason, and, with her head amusedly bowed to the side, watched my exertions."
    un "And if it's not a secret - with whom?"
    th "Not a secret, of course. I got poked in the nose by Miku when I was trying to get a closer look at her au naturelle."
    "I wiggled my shoulder, eloquently signaling that it was a secret."
    "Now I'd like to say something like «Don't you have some urgent business waiting for you somewhere»?"
    "Yes, I'm afraid I unlearned how to do tactless things of this caliber a long time ago."
    un "It doesn't wash out?"
    me "Mm-hmm."
    un "My father showed me how to remove blood with peroxide."
    show un shy pioneer with dspr
    extend " Want me to b-bring s-some?"
    me "It can't get any worse, I guess... bring it."
    scene bg ext_square_day with dissolve
    "Another half hour later, fully washed in a shirt pleasantly damp in this sunshine, I was standing in the square trying to intercept Miku - someone had seen her then on stage and then in the club, so it was better to catch her in the middle."
    show mi smile pioneer_transp with fade2
    mi "Hello, hentai!"
    "Greeted the sneaky Miku from behind."
    me "Hi."
    mi "Are you just standing there, or is it important business?"
    me "I… Uh… Just standing, I guess…"
    mi "Very good! Because I've got a little pile of stuff piled up that I don't have anyone else to do but you!"
    hide mi with easeoutleft
    "She caught me by the hand and dragged me along."
    stop music fadeout 5
    scene bg int_wardrobe2_7dl with fade
    play ambience ambience_music_club_day fadein 3
    play music music_7dl["breath_me"] fadein 3
    "I didn't really understand why she dragged me here, and I stood there stupidly, feeling my heart pounding frantically as my dry throat swallowed."
    show mi smile2 pioneer_transp with dissolve
    "And Miku grinned, as if capturing my worries."
    show mi sad pioneer_transp with dspr
    mi "I've been thinking for a long time, Senya. A long time."
    mi "It's crystal clear to me now."
    show mi normal pioneer_transp close with dspr
    "She flowed out of her relaxed pose, instantly being beside me."
    "I flinched, instinctively covering my nose{w=0.3}{nw}" with hpunch
    show mi smile pioneer_transp close with dspr
    extend ", and elicited another satisfied chuckle from Miku."
    mi "Don't be afraid, I won't hit you again."
    me "Uh... B-but..."
    "I stood there, still not knowing what she had in mind."
    show mi laugh pioneer_transp close with dspr
    "And Miku threw her head back toward the ceiling and laughed. Or rather, she practically burst out - apparently that was the reaction she had anticipated."
    mi "What a brave man you are. An hour ago you were braver than that!"
    show mi grin pioneer_transp close with dspr
    mi "Or are you scared? Such a big, strong boy frightened of a tiny, fragile Japanese girl."
    mi "I can barely reach your shoulder, see?"
    "She bumped my shoulder with her head{w=0.5}{nw}"
    show mi grin pioneer_transp with dspr
    extend ", stepped away a bit."
    with vpunch
    "…and pushed me sharply with her hands on my chest."
    "With all her might!"
    stop music fadeout 3
    "I momentarily lost my balance and flew backwards, preparing to meet the hard floor with my tailbone, but it was somewhat different."
    play music music_7dl["uneven_me2"] fadein 3
    "First of all, it turned out that I had a soft bale of stuff under my feet, which took me in its arms, extinguishing the impact completely."
    "And second, while I was swinging my limbs for balance, I caught Miku's shirt and yanked."
    "The buttons splattered in different directions, and my gaze was opened to her bra... er...I mean..."
    "Miku wasn't wearing a bra."
    "She must have put her shirt over her naked body since the wash."
    "And walked around with her nipples showing through the sheer fabric."
    "A sight for real erotomaniacs."
    "Only a moron like me could have missed it."
    mi "Oh…"
    "She didn't embarrass herself, didn't say anything, didn't even make an attempt to cover herself."
    scene black with fade2
    "And a moment later, she was on top of me."
    "There was exactly one thought pounding in my head - I wish no one would come in and see us here."
    "But all of today's and yesterday's events brought me smoothly to one thought-experience."
    "Miku is mine. I won't give her up to anyone."
    "I went on top of her with a jerk."
    "She's close, her skin marble, translucent in the nightlight, and I couldn't resist running my fingers over her hollow belly."
    "And she pulled me closer and dug her lips into a kiss."
    "She's not the least bit shy, though there's no experience in her movements."
    "There's the excitement, the shivering, the shaking. But there is no shyness. It's as if she's accepted me and now refuses to give me back."
    mi "Now you owe me sewing of my buttons, got it?"
    "She asked, pulling away from my lips."
    me "Silence. Woman."
    "I'm shaking myself, and Miku feels it."
    mi "Why shake now? If you get caught here, I'll tell everyone that you wanted to rape me."
    mi "So relax and enjoy yourself."
    me "W-what do you m-mea…"
    mi "Oh. Shut up and kiss me again."
    mi "Yes. There, too."
    "Miku sagged, letting me take my shirt off."
    "The tie was already going somewhere."
    mi "You so wanted to see everything, then look, look. But don't forget - I want admiration as well as affection."
    "What else was she babbling about, I wasn't really listening."
    "I was pounding with excitement and fear of being caught."
    "But my fingers reached for her breasts."
    "I've seen her in the bathhouse before, but it looks a little different now."
    "It's getting cramped in my shorts how close and desirable she is."
    "And I almost hated her an hour ago."
    "And now I want... I want... I want her to scream and wriggle."
    "I want her to feel good."
    "Her breasts were small, fit perfectly in my palm, responded perfectly to the caress."
    "Someone measured for me, molded it, and created Miku."
    mi "If you stop - ah! - now — I'll hit you in the nose again."
    "The Japanese girl's breathing became more rapid, and she began to sound buttery."
    "She's so smooth and supple, so tender..."
    "I moved my fingers faster and faster where I could reach them."
    "But Miku suddenly stopped and looked at me with a completely sober gaze."
    mi "Clumsy bear Senka. Why are you so clumsy? Am I your first?"
    me "Ah... Shut up."
    "I took my own advice and covered my mouth with her breast."
    "She sobbed and trembled."
    me "W-what?"
    mi "You know how to turn a girl on, yeah."
    "Miku says it in a voice that makes it obvious he's mocking."
    "I don't understand why you have to do that when you can just... love each other?"
    "But right now it feels more like a sporting challenge than romantic silliness under the moon on silk sheets."
    "No, we're going to have it all silly, silly, in a dusty dressing room in the back of the rehearsal base, with a minute-by-minute risk of getting caught."
    "And it made my head completely buzz - lust and adrenaline - Miku found herself with her legs up over her head and her striped triangle of lingerie flying off somewhere, leaving her completely naked."
    "Dishonorable gimmick, I agree. A girl should be turned on indirectly, on the cheek, on the neck, on the tummy."
    "But why did she tease me?"
    "She was clean, smooth - she seemed to be doing all sorts of things on purpose that all girls do with their hair in interesting places."
    "Although I've heard it's just that Japanese girls don't usually remove anything."
    "I wonder if it's razor or depilation? You can only find out by getting up close."
    "But you have to get close first."
    "I tried to spread her legs."
    "But that wasn't the case."
    mi "Hey, don't push, you're hurting me!"
    "Miku fidgeted under me, trying to get out."
    mi "Why are you pushing so hard, you could have just told me, I would have..."
    me "I told you already."
    mi "Huh?"
    me "Shut up, I said."
    mi "Oh you..."
    "Forgetting, she loosened her grip on my legs, and I was immediately where I was aiming."
    scene black
    with flash
    "No taste, no color, no smell."
    "After the bath. And smooth."
    "So it was depilation."
    mi "You... you cheater... aahhhh..."
    "I curled my tongue in a tube and studied what I could reach."
    "It was like we switched places here, her mocking disappeared, she was completely in my power."
    "And I was already heady without any wine."
    "She was babbling something from above, but I wasn't paying attention - both tongue and lips were busy, and I was listening to how she was reacting."
    mi "You're doing it all wrong! It's not working."
    "Miku tried to slip away from the tongue, but where could she go."
    "I caught her with both hands and like a man dying of thirst in a bowl of water - clawed at her thighs, penetrating as deeply as I could with my tongue."
    mi "No... You can't... there... with your tongue..."
    "Yeah, silly woman I haven't listened to yet, where you can and can't go."
    "I reached out with my left hand and began to caress the neglected breast."
    "There are sounds all over the room... The most obscene."
    "There's no mistaking it."
    "At some point Miku's completely neutral taste took on a sour note - the warming began to take its toll."
    "And the chatter of the unmouthful girl became more and more intermittent and incoherent."
    "Another second, and I ran my finger inside."
    mi "You're doing it - ah! - all wrong... I don't feel anything... ahhh..."
    "My finger went in, feeling almost no resistance - all the way to the wall."
    "When I pulled it out, there was a thin, transparent thread between my fingertip and Miku."
    me "You don't feel anything at all, but you're ready now."
    mi "Oh, jerk... That's different..."
    "She turned away, red to the roots of her hair."
    "A fragrance floated in the air that cannot be named-but you can understand it. It is an intertwined and mutual Desire."
    "Miku fell silent altogether, cradling my head against hers with both hands."
    "The cycle of evolution was complete - from a pesky chatterbox, a mean bitch, a girl in search of herself - there was a little woman before me. And she sensed my changed attitude toward her."
    "She tried hard to relax, but my fingers and my lips and my tongue didn't leave her a chance."
    "Even another hook on the nose hardly stopped me now."
    "I took one last gulp of air and roughly invaded with my tongue as deeply as I could - the closed hips completely blocked out the sounds, but I caught her screaming."
    "And a moment later she began to shake - an orgasm pulsed through the girl's body in soft, spreading waves."
    stop music fadeout 3
    scene black
    with flash
    "Time turned with a tangible click around a second frozen in amber stillness, and..."
    "I exhaled."
    play music music_7dl["iamsadiamsorry"] fadein 3
    "Apparently she had a healthy sexuality, and in some way she had already learned what discharge meant."
    "The best painkiller ever."
    "I touched her clitoris with my tongue one more time - and she recoiled, trying to escape the experience that was now too intense."
    "And at that very moment I got rid of my shorts, reached up and... licked her cheek."
    me "Hi."
    "I said."
    mi "W… Ah!"
    "I was so comfortable inside that it was enough just not to hold back - she gave in, the last obstacle disappeared, and Miku looked into my eyes in amazement, feeling something inside her that didn't belong to her."
    mi "Wait... I'll just... I'll get used to it."
    "She spread her legs as wide as she could, but after thinking about it, she just wrapped her legs around me and leaned toward me."
    "It was like falling down a slide."
    "Spicy, hot and very sweet."
    me "How tight you are inside."
    mi "Don't say that... ha-aaa... haaaa..."
    "I don't know about her, but I've never had anything like this in my life - I perceived everything as if in a fog, and now even the threat of invasion wasn't frightening at all."
    "I was all there, where we were united as one."
    mi "No, no... Not so abruptly, not so deeply..."
    me "Madam... who fucks wh...ahem?"
    "Inappropriately suddenly came to mind Lieutenant Rzhevsky."
    me "Especially since it's so tight."
    mi "I'm going crazy..."
    "I didn't catch the moment when the movements stopped belonging to me alone."
    "Miku caught the rhythm, and she was pushing towards me."
    "And the harder she pushed, the harder she squeezed me inside."
    "I was already struggling, but now I was completely out of control and going inside her like a piston, pushing myself to the point with each passing moment."
    with flash
    "Everything went dark before my eyes, and my heart faltered at half-step."
    "La petit mort, the French say. A little death."
    "A wave of unbelievable pleasure ran through my body, and moments later I began to discharge inside the Japanese woman."
    "I had never felt so good, not even a momentary headache could spoil my pleasure."
    "Miku wrapped her arms around me as well, squeezing as hard as she could."
    "She didn't want to let go of me at all."
    "It was very quiet here, only our breathing could be heard."
    "But nobody came."
    "I was lying on top of Miku, leaning on my elbows and knees so as not to crush the girl."
    "And she, covering her eyes, listened to herself."
    "She was sweaty again, like she had been an hour ago."
    "But this time it didn't bother me at all."
    me "What do you think?"
    "I asked when she graced me with a grateful look."
    "Immediately, however, she hid."
    mi "It was… kind of meh. I'll give you a C."
    me "What do you mean?!"
    "She looked at me reproachfully."
    mi "You were only thinking about yourself, not giving me a break, and completely hogging me."
    mi "And this is love?"
    me "Not hate, though."
    "Faintly I joked."
    mi "You still have to practice and practice."
    mi "And it would be better if you practiced with me."
    "She hugged me gently."
    mi "Because if I find out you've been practicing with someone else..."
    "And just as gently kissed."
    mi "I'm going to chop your balls off. Do you understand me?"
    me "Yeah."
    mi "Good boy. Now get off me, you rapist. I'm going to go try and make some more arrangements for the bathhouse."
    "She picked up my shirt off the floor."
    mi "Thread and a needle are under the dressing table. Have fun."
    mi "And I feel like I have a lot, a lot to wash out of myself right now."
    play sound sfx_close_door_clubs_nextroom
    "The door slammed."
    "And I was left alone."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_7dl_branch:
    scene bg ext_sky_7dl with dissolve
    play ambience ambience_camp_entrance_day fadein 3
    play music music_7dl["ourfirstmet"] fadein 3
    "I'm peaceful and comfortable."
    "But the hell I admit to her how insecure I feel around her."
    "That kind of thing just spoils everything. Besides..."
    "It's too personal."
    mi "Senechka, are you thinking about something?"
    "I moved my shoulder indefinitely."
    with fade
    "And, being polite, I asked a counter question:"
    me "And you?"
    "After a moment of silence, the Japanese girl nodded:"
    show mi smile casual with dspr
    mi "Here's what I think..."
    "Her smile became demonic."
    mi "Senechka, ask me out... on a date!"
    me "What do you mean?"
    show mi happy casual with dspr
    mi "You're embarrassed again, as if I said something indecent."
    mi "Don't be so afraid, I won't eat you. Honest Pioneer!"
    me "I'm not afraid..."
    play sound sfx_open_dooor_campus_1
    pause(1)
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_musclub_day with dissolve
    "Obviously Miku is going to want to change, then take a shower - and given the playmate that attacked her, every stage she will embarrass me in every way possible."
    show mi normal casual with dissolve
    mi "Senya, you ran off so fast, I didn't have time to finish what I was saying."
    me "Yes. I don't even know what came over me."
    mi "Really? I thought you were embarrassed about something."
    "She flippantly brushed the thought away and continued:"
    mi "Do you have swim trunks?"
    me "Don't ask, I won't give them to you!"
    show mi laugh casual with dspr
    mi "Oh, funny Senka, why do I need your swimming trunks? I can wrap myself in them twice, like in a cape."
    "She shook her head."
    show mi smile casual with dspr
    mi "No, you'll need swim trunks. I'm going swimming at the pier, and I want you to keep me company."
    me "The pier is where?"
    mi "Oh, it's a secluded spot! Nobody knows about it! It's a little off the grounds, it's not as noisy as the bathing place, I go there sometimes."
    me "Alone?"
    show mi serious casual with dspr
    mi "Of course not! You'll keep me company."
    me "Oh. Right. I completely forgot."
    with fade
    stop ambience fadeout 6
    play sound sfx_metal_door_heavy_close
    scene bg ext_camp_entrance_day with dissolve
    play ambience ambience_camp_entrance_day fadein 3
    "Miku was so successful at maneuvering around, avoiding encounters with any oncoming passerbys, that I suspected her of ninja training, no less."
    "Anyway, the clock struck three in the afternoon when we shut the gate behind us."
    mi "Turn right and watch your feet - after the rain the clay can be slippery."
    scene bg ext_path_day with fade
    play ambience ambience_forest_day fadein 3
    pause(1)
    "It didn't take too long to walk, judging by the trampled path, the 'hiding place' was used often and with pleasure."
    scene bg ext_lake_day_7dl with flash
    play ambience ambience_lake_shore_day fadein 1
    "And when the bushes finally parted, I couldn't help but cry out in admiration."
    "For the place did indeed turn out to be a blast!"
    "Miku hooted in the tradition of the Indians, and, throwing off her blouse and skirt, she ran downstairs, leaving me to pick up her clothes..."
    "Ran across the grass..."
    "And finally, under the feet of a Japanese girl, the boards of a bridge creaked barely audible - and an aquamarine fish slid into the water..."
    stop music fadeout 3
    scene bg ext_sky_7dl with fade
    "Miku was splashing in the shallow water, giggling to herself - and she was every bit as self-sufficient."
    "I guess I'd be offended that I wasn't needed that much - she did call me along!"
    "And not needed! Why did you call me, I wonder?"
    play music music_7dl["pathways"] fadein 3
    "If I were at least a couple of years younger, I certainly would."
    "But I'm old, lazy... I follow the aquamarine tails out of the corner of my eye, confused at times about where the water ends and where the tails begin."
    "And I feel great - just because I'm here!"
    dreamgirl "The ability to be content with little, I say."
    "I didn't have time to engage in a polemic with my inner voice..."
    "I was hit with a splash and the same watercolor princess flopped down on the towel beside me."
    "She reeked of coolness and freshness, beckoning me to take a dip..."
    mi "Senka, let's go swimming!"
    me "Hmm..."
    "Except that the strangest rumors might go around about us if we were caught bathing together..."
    me "Let's go!"
    "The one thing I've never cared about is public opinion!"
    pause(1)
    scene anim_underwater with dissolve
    play sound sfx_shoulder_dive_water
    scene anim_underwater
    show blackout_exh
    with fade
    "The water was cold, and it took my breath away in the first moment."
    "And then Miku was there, and it didn't matter anymore."
    "I felt her close to me distinctly - like an extension of my own nervous system."
    "Her laughter. Her cheerfulness."
    "She doesn't have to be kind or affectionate or clever at all. Just enough to be herself - a sweet girl who believes the world is not black."
    "But Miku wouldn't be herself if she limited herself to just being nice."
    "She moved in the water beside me, smiling whenever our eyes met."
    "Miku swam up to me, playfully nudged me with her shoulder, and rushed to the surface."
    "Of course I followed her!"
    "Higher and higher."
    "I didn't really understand why I was chasing the nimble fish-girl, but I didn't want to give in."
    "I liked to play with her - and not even try to give in."
    "And the right word to use here is probably «honesty»."
    play sound sfx_water_emerge
    play ambience ambience_boat_station_day fadein 3
    scene bg ext_beach2_day_7dl
    mi "Senka swims like a fat turtle!"
    "Miku showed me her tongue and floated around me."
    "And she was the most beautiful and wonderful. If I could fall in love with her, I'd have no trouble."
    "A worthy candidate, eh!"
    me "Oh come on, you... skinny turtle!"
    play sound sfx_draw_water
    mi "Be-be-be!"
    "The girl's got a temper. Getting hot and bothered."
    me "Did you call me to bathe with you to humiliate and harass me?"
    "I asked."
    mi "You might as well be harassed!"
    "She splashed water at me."
    mi "You're so big, I can fit all over you and you won't even feel it!"
    mi "And you won't be humiliated!"
    th "You're a miracle, Miku."
    "Quietly smiling, I thought."
    "I felt so at peace here, with all the worries and reflections out of equation."
    "It was just us here - and no one was our decider!"
    mi "Let's swim to the shore."
    "She called, turning around toward the clothes left on the shore."
    mi "I'm kind of freezing."
    with fade2
    scene
    $ renpy.show("bg ext_sky2_7dl", what = Desat1("bg ext_sky2_7dl"))
    with flash
    mi "Senechka, talk to me!"
    "She demanded, shaking me vigorously and thereby chasing away the approaching slumber."
    me "Hmm? About what?"
    mi "Don't you have anything to talk to me about?"
    mi "I don't know anything about you, tell me something?"
    "Something. But what?"
    with fade2
    me "I'm much older than I look."
    me "And every day that I manage to open my eyes, the future grows darker and darker."
    me "But the sun always shines in the past..."
    "I went silent, having lost all thought."
    "And Miku, after politely waiting a few minutes, came to my aid:"
    stop music fadeout 3
    if loki:
        mi "Have you dated anyone yet? Or..."
        "Her voice trembled."
        play music "<to 112>" + music_7dl["youareours"] fadein 3
        mi "Are you dating now?"
        me "No. Not with anyone. There was a girl once, though."
        with fade
        mi "And where is she now?"
        me "Let's just say she left me."
        mi "Really? That's too bad. You don't seem very sad about it, though."
        th "You should have known how it ended there..."
        "We've been gone a long time, and it just keeps raining..."
        mi "And with what?"
        "I think I said the last phrase out loud."
        "My tongue is my enemy."
        me "I don't want to talk about it."
        "I cut off."
        "But I was immediately saddled, squeezed by hips, and she cackled:"
        mi "Please, please, please, please!"
        "She was hot and stray; she must have had a self-contained nuclear furnace running inside her."
        "And it tingled me for a moment with a sensation that made me all twitch and stiffen."
        me "Okay. Okay."
        "Slowly I said, careful to keep my body's reactions under control."
        me "I'll tell you everything. {w}Just get off me and stop getting into different poses - it's embarrassing."
        "Miku obediently rolled off me and lay down next to me - very cozily curled up in a ball on the towel."
        mi "Go ahead!"
        "She allowed."
        "Didn't seem to notice anything."
        $ renpy.show("cg d7_sl_gonna_be_ok_7dl", what = D3_intro("cg d7_sl_gonna_be_ok_7dl"))
        with fade
        me "It all started ten years ago..."
        "My memory has not yet fully returned to me - for example, I could hardly tell now about the events that preceded my arrival here."
        "However, the last years of rolling downhill and the reasons for it have held extremely tenaciously in my memory."
        me "Once upon a time I also planned to tie my life to music, only not pop, but chamber music."
        me "I entered the first year of the conservatory in the brass class, from which I had a direct path to either the St. Petersburg... that is, the Leningrad, military or some kind of symphonic."
        mi "You were a musician?"
        "With rapture Miku shrieked."
        "What was she raving about, I wonder..."
        me "Yes. And not even the worst in the world."
        me "Although not to say that music was the love of my life - on the contrary, I went there out of despair."
        me "Anyway, one day in my life I had an encounter that changed everything..."
        "I told and told, and in the meantime I was experiencing it all over again - I knew that I should have been gnashing my teeth in rage and wanting to strangle the cause of the trouble with my own hands."
        "But none of that happened."
        "Because I loved Kseniya too much at first."
        scene anim prolog_2 with dissolve2
        "Ten years of being hopelessly in love with a person who doesn't care about you enough to not even come check up on me in the hospital when it was her fault."
        mi "Ten years..."
        mi "But how can it be ten years, Senechka, if you are now seventeen, and anyway..."
        me "I'll tell you later how - now I want to tell you why. Will you listen?"
        "Miku nodded."
        "Unhappy with herself, she moved higher and snuggled up so that we were head to head - like in those most silly anime cartoons."
        mi "Of course I will, Senechka."
        "She whispered."
        mi "Go on."
        me "There's basically nothing to go on."
        "Ten years of downfall: I had no life but a desire for revenge, now, turning around, I look at the smoking ruins left of the once so promising life of a musician, a poet..."
        "One day the first sprouts will rise here too, but for now, for now..."
        "And there is no love here."
        "Perhaps that's why I didn't hold a grudge against the girl, when I realized that 'it burned and went away' - it took strength to hate."
        "And I had nothing."
        "Only the icy needle under my heart and the desolation that came over me as soon as I pushed through the ribbon and saw the bankruptcy judgment."
        "Maybe that's why I ended up here - that there was nothing left on the other side?"
        mi "You're getting yourself too wound up."
        "Claimed Miku when I finished where my memory still retained a coherent chronology."
        mi "You're just too pissed off that the credits didn't run after you had your justice and the movie didn't end."
        mi "Only it doesn't work that way."
        me "What do you mean?"
        scene cg d6_mi_vyluthere_7dl with fade
        "For some reason I wasn't surprised by the transformation of the chatterbox chatterer into a person with an opinion of her own."
        "Perhaps because I was secretly expecting something like this?"
        mi "In the sense that you think your life is like a story of loss and revenge."
        mi "It's like you have nothing and can't have anything. But you have students."
        me "Ay, what kind of students are there..."
        mi "Successful! Do you think anyone could feel gratitude for their son's mentor - if the mentor was mediocre or had no heart?"
        mi "You're in love with music. What's much better is that you're able to fall in love with music for others."
        mi "To pique their interest."
        mi "That's why your story isn't over. You still have a few unreleased debts."
        "I wondered."
        "And Miku took my hand and began to draw something on my palm with the tips of her nails."
        "It tickled, but it felt good."
        mi "So don't think any more nasty thoughts, okay?"
        me "Okay."
    elif herc:
        play music music_7dl["dance_with_me"] fadein 3
        mi "Do you have a phone there?"
        "I nodded."
        mi "How about we call sometime? I'll write my number in Sapporo now... +81 11..."
        "Miku turned out to be an extremely thrifty girl - in addition to her swimsuit, she also took care of a pen and paper."
        "Or rather, a notebook."
        mi "That's just in case."
        "She smiled."
        mi "In case something comes to mind, I'll write it down right away!"
        "How simple it all is in her mind."
        "I had to cool her ardor a little by telling her that there's no telling when I'll get a chance to call."
        "And the money."
        mi "Could there really be a problem?"
        me "No, but it's better to be prepared for anything."
        mi "Then why don't you tell me where and how you live?"
        scene cg d6_mi_vyluthere_7dl with flash
        "Miku pouted and, hiding her notebook, lay down beside."
        me "Excluding the risk of constantly missing the other shore or sitting around and missing the last train home..."
        me "I like my panel."
        "I dug around in my phone's memory and brought up a picture of my house - I used it to learn how to build perspective - back when I planned to paint."
        mi "And you live in that?"
        "Miku stared at the picture curiously."
        mi "Wow. We have a similar neighborhood in Harajuku, so exactly the same houses."
        me "Thank you."
        mi "No offense! It's just funny how similar the construction is - panel houses, balconies, concrete."
        me "Not your Sapporo."
        with dissolve
        mi "What's wrong? The center of Hokkaido, the culture-architecture. Do you want to come to our Snow Festival?"
        mi "Last Yuki Matsuri, a fan of mine made a full-length statue of me, very beautiful!"
        "I was silent. Making full-length statues out of ice was out of my league."
        "Even in honor of the best girl on the planet."
        mi "Well, or we could just walk around and see! Either to Odori Park closer to the center or to Tsudomu Stadium. It's a long way from my house to Susukino, so..."
        "Miku cut herself off."
        mi "Am I rambling again?"
        "I shrugged my shoulders."
        mi "No, of course we don't have much to brag about, not Leningrad after all - the northern capital! But we did have the Winter Olympics!"
        me "When?"
        mi "1972!"
        "I had an interesting thought."
        me "Wait a minute..."
        "I started counting on my fingers."
        me "And you were born then..."
        "I was surprised:'"
        me "Does this mean that your parents met at those very Olympics?"
        mi "Figured it out at last!"
        "Miku's smile was kind, warm like that."
        mi "That's how it was. Dad came from the Union to help with the construction of the power plant - we needed a lot of electricity."
        mi "But besides him, many more Soviet engineers came. Seventy-three and seventy-four are considered the year of Hafu - you can see why."
        me "Yeah, it's an epic story. {w}So in February there was the Winter Olympics..."
        mi "And in August I showed up!"
        me "So you lived your whole life in your village?"
        mi "It's not a village!"
        "Miku sulked."
        "But immediately she thawed out."
        mi "No, not all of it. After I started my career, I slowly moved to Tokyo, but I think I'll go back home after I finish music school."
        me "Why would that be?"
        mi "What do you mean, why?"
        "The Japanese girl was openly surprised."
        mi "So you can find me when you come, of course."
        "It amused me when she said «when», and not «if»."
        with fade
    else:
        play music music_7dl["someone_like_you_guitar"] fadein 3
        "I stand long ago at the window, flowers and candles on the table. The sound of rain drowns out my heart as I wait to meet you..."
        scene bg ext_lake_day_7dl
        show mi normal swim
        with dissolve
        mi "I was, until very recently, afraid of water."
        "Looking at the way she was splashing and screaming with excitement, there was no way to assume that."
        mi "You see, there was this thing..."
        "The Japanese girl's gaze clouded slightly as she recalled the events of long ago."
        "Or is that an echo of former sadness?"
        "Miku took a few deep breaths."
        show mi sad swim with dissolve
        mi "I wasn't the only one who was bullied in junior high."
        "Finally, she made up her mind."
        mi "Besides me, there was another... girl."
        mi "She was very quiet, quiet - never played with us, never complained about anyone."
        mi "Even when Ryuka set her hair on fire and she had to cut it very short - never told anyone."
        "She hasn't said anything supernatural yet - what was she daring to do?"
        mi "We got used to her, we knew Rie was just herself."
        mi "Bullied her, of course. {w}As a kid, it's so funny when they can't hit you back in response to your bullying."
        show mi cry swim with dissolve
        mi "And I... too."
        "The Japanese girl hid her eyes."
        mi "Otherwise everyone would think I was defending her."
        me "Mocked her, too?"
        mi "Yes. Stepped on er foot, shoved her in the doorways - try not to push her when the whole class is looking at you."
        "Miku was unspeakably ashamed."
        "Why did you even start this story in the first place?"
        mi "And she never answered - she looked so quietly, with a smile. It made me want to kill myself."
        mi "I'm guilty, yes. I'm bad - then it would go quiet for a few days, but it's hard not to confront a person when you're in the same class as them."
        mi "By then I was just in time to cry, my conscience was letting me go a little bit."
        scene anim prolog_2 with fade
        $ set_mode_nvl()
        mi "We were in third grade when the accident happened."
        mi "The teacher took us to the pool, we had a FC in the sports complex, Rie was with us."
        mi "It was necessary to swim thirty meters, a froggy long is a lot for a third grader, so not everyone could do it."
        mi "Personally, I couldn't do it."
        nvl clear
        mi "And Rie tried. At the moment when it happened, she was a few meters beyond my mark."
        mi "I don't remember the details very well, only scattered images - the girls lined up one by one, all wearing black sports swimsuits. Only Rie's lane was as empty as her swim."
        mi "Here she is swimming, you can see she's doing her best."
        mi "And here she goes underwater - it's only two meters deep, but she's not moving."
        mi "And no one understands anything, everyone is laughing, calling Rie a crocodile and a godzilla poop."
        "Miku exhaled sharply:"
        mi "Just the coach from his seat, right in his clothes, jumped into the water and swam to her, shaking her out on the side."
        mi "Attempts at artificial respiration, clearing her lungs of water... It was all to no avail."
        nvl clear
        mi "Rie was taken away in an ambulance."
        mi "Two weeks later we found out she was gone."
        mi "She had vitium cordis. She was absolutely not allowed to worry, no physical activity was allowed."
        mi "Such a beautiful word... Pa translated it as 'congenital heart defect' - he was always interested in Latin."
        mi "And I didn't know what a defect was then, and I heard 'threshold.' I knew it, it was in my ears."
        mi "There were words like that in the house from time to time - threshold of strength, threshold of capacity... I decided that Rie had the same threshold."
        mi "That her heart had a threshold. Threshold of forgiveness. Rie was a kind girl, she forgave us, she never refused to help anyone. And then one day she couldn't forgive. Because she reached a threshold beyond which her heart could no longer beat."
        nvl clear
        mi "And in the class they said was because she overworked herself when she was swimming."
        mi "«Overexerted herself during the swim» — that was it."
        mi "And we were afraid of the same thing for a few months - «overexerting»."
        mi "To the point of hysteria!"
        mi "They refused to swim where Rie's heart stood up, they were afraid ours would stand up too."
        mi "Thus, that year we didn't swim anymore."
        mi "And I still had a fear of water for a few more years."
        nvl clear
        scene cg d6_mi_vyluthere_7dl with flash
        $ set_mode_adv()
        me "Only a little child would imagine such a thing."
        mi "Yes. You're probably right."
        "Miku nodded sharply, as if afraid that I would now rush to reproach her for something."
        mi "But, you know... I had a dream about her. Rie."
        "Miku continued her story."
        "Apparently it really bothered her."
        mi "After our quiet girl died, all the cruelty of my classmates came down on me alone - and I cried at night with guilt for Rie, not really paying attention to the pokes."
        me "And how long did that last?"
        mi "Until I changed schools."
        "She brushed off my question as irrelevant."
        mi "But I must have redeemed myself in some way, so one day in a dream Rie came to me."
        mi "She was the age she was when she drowned, wearing her usual dress."
        mi "She was smiling her quiet smile again."
        mi "She said she wasn't mad at me and always wanted to be my friend."
        mi "I wish things had worked out differently."
        mi "She put two fingers to my forehead and disappeared."
    scene bg ext_lake_day_7dl
    show mi surprise swim
    with dissolve
    mi "Oh, what is that?"
    "Miku perked up and raised herself on her elbow, anxiously looking over me somewhere in the distance."
    "I followed her gaze."
    "It looked like there had once been a concrete tile path from the road to the wharf, but it had been forty years since then - it had overgrown with tall grass."
    "The concrete path, however, is still there."
    "And now someone was stomping on it very loudly and distinctly."
    "Or rather, even STOMPING!"
    me "Oooh... A fearsome beast is coming for our souls!"
    mi "What is it?"
    "Miku got a little scared, but seeing that I was in no hurry to run anywhere, she made herself sit still."
    me "The fierce beast is out there. I warn you right away - only the Chelyabinsk workers are more dangerous than him."
    mi "Oh, the horror."
    "Miku didn't seem to get the joke."
    me "Yeah. Let's go."
    stop music fadeout 5
    "I got up and dragged Miku after me, throwing on my shirt."
    me "It's been a long time since I've hunted anyone."
    show mi shocked swim with dspr
    mi "Hunted?! But, Senechka..."
    "Without saying a word, I scurried forward as fast as I could."
    "Miku had to shut up for a while and focus on trying not to fall off somewhere along the path."
    dreamgirl "And then we'll be on top of her!"
    th "And slam her with belly to the ground, belly to the ground!"
    me "Shh! You'll scare the prey away."
    "The path was discovered after 20 steps."
    "I looked around. I looked to my left..."
    me "There he is! Catch!"
    show mi surprise swim with dspr
    mi "But..."
    me "GET HIM! Atu-tu-tu!"
    "I screamed and ran as fast as I could."
    show ftl_anim with Shake((0, 0, 0, 0), 4.0, dist=10)
    "The wiggling was right there - there it was, ten steps away, not visible because of the grass."
    "I took a closer look and nodded contentedly."
    "Just what I expected to see."
    "With a paw arranged so that its owner walks constantly, as if stepping only on his heels."
    "It just didn't add to his speed!"
    play sound sfx_7dl["hedgehog"] fadein 0
    me "Ready… {w}Set… {w}Hedgehog!"
    "With a primal hooting, I waved my shirt over my head and chased the predator straight for the water."
    play music music_7dl["catch_the_hedge"] fadein 2
    scene cg d4_mi_hedgehod_day_7dl at fast_running
    with dissolve
    "I wish the previous me could see the current me!"
    "I've always been so... so solid! Unhurried."
    "Who'd have thought I'd be reduced to that voice of an Indian driving a hedgehog?"
    th "I hope no one ever finds out about this."
    "Somehow there was far less apprehension in my hopes than I expected."
    dreamgirl "Childhood played in one place, huh?"
    "The chatterbox in my head took the place of the GoPro camera and commented on my actions from the couch."
    dreamgirl "If you catch him, what will you do to him?"
    th "I'll give him a finger to bite!"
    dreamgirl "At least not your nose."
    "A picture was thrown at me from my distant, distant childhood - the same one that's 'playing' now."
    "{i}I leaned over to look at the curled up animal, and it suddenly uncurled abruptly and clung right to my nose!{/i}"
    "{i}Painfully, mind you!{/i}"
    "{i}In fact, so much so that when I recoiled - the vicious spiky was still hanging on my nose, clenching his jaws!{/i}"
    "{i}Tears spurted from my eyes in pain.{/i}"
    "{i}Fortunately, the neighborhood boys had already taught me how to deal with it.{/i}"
    "{i}With my jaw slightly tilted forward, I blew on my long-suffering nose.{/i}"
    "{i}The hedgehog got worried, tried to breathe through his nose, but no way! No chance!{/i}"
    "{i}A few seconds later, he snarled unhappily, unhooked from me, and rolled away into the palms of my hands.{/i}"
    "Imagining the same picture for a second - but with Miku as the victim, I couldn't help laughing."
    dreamgirl "Keep up the tempo! No time to laughing your ass off!"
    play sound sfx_slavya_run
    scene bg ext_un_hideout_day_7dl at fast_running
    with dissolve
    play sound sfx_7dl["breath"] fadein 3
    "I was almost out of breath, but I reached my goal - the hedgehog panicked out onto the tiny beach next to the pier and, bogging down in the sand, darted off to the right."
    "But the speed, of course, was no longer the same, not the same."
    "If it weren't for one problem."
    "Just a few more seconds, and..."
    play sound sfx_7dl["blanket"] fadein 0
    "The shirt, as if it had found its own wings, flew forward."
    "My hand did not fail me - the white lump, turning in the air, turned into a cloth that neatly covered my target."
    "Once it reached the ground, it froze."
    "Then, pensive, it took a few steps to the right..."
    "To the left..."
    "And finally, it froze completely."
    "Leaning over, I wrapped my shirt around my arms - and in them, like in a hammock, was the Hedgehog itself."
    "The muzzle turned out to be a pest - just as I had expected."
    "To test his reflexes, I moved his prickly flanks through his shirt."
    "The trophy snarled indignantly, as it should, and hid its nose deeper into the needles."
    scene bg ext_un_hideout_day_7dl
    show mi surprise swim
    with dissolve
    mi "Oh, what have you got there?"
    "Miku arose beside me."
    "As it turned out, the whole time she was dutifully running after me - in her swimsuit."
    me "That's my booty, I got it!"
    show mi shy swim with dspr
    mi "What booty?"
    me "A hedgehog!"
    mi "A hedgehog? It's so cute! I don't have hedgehogs in my homeland, but I've seen them in the zoo."
    "Miku was so pleased, she held out her finger to pet the hedgehog."
    "I imagined the picture again - Miku with a hedgehog on her nose - and, shuddering, put the wary animal away:"
    me "Miku, be careful! You know how hard that beast bites!"
    me "It can bite you until you bleed."
    mi "Oh."
    "Miku immediately yanked her finger away."
    show mi normal swim with dspr
    mi "What do we do with him now?"
    "I shrugged."
    "I was only interested in the process of catching the beast; I cared less about the rest."
    me "I'll take it to the living corner and call him Felix."
    stop music fadeout 5
    show mi laugh swim close with dspr
    mi "Why Felix?"
    "Because I have that association!"
    me "Because our Felix is too slow for Sonic the Hedgehog."
    me "And I also knew a hedgehog when I was a kid - on prehistoric game consoles."
    show mi smile swim close with dissolve
    mi "«Prehistoric» — meaning?"
    "«Yeah, I had an eight-bit «Dendy» as a kid, the old, old one» — I almost said."
    "And then I remembered about Circumstances."
    mi "And then, Senechka... We don't have any living corner!"
    mi "Why don't we let Felix go? Let him go on his own."
    me "Eh..."
    "With a heavy sigh, I lowered my hard-won prey back to the ground."
    me "Pray to Random, Comrade Dzerzhinsky - the lady asked for you."
    "The hedgehog answered nothing and in a few seconds disappeared into the grass."
    "And we were summoned by an afternoon horn!"
    stop sound_loop
    stop ambience
    stop music fadeout 5
    scene bg ext_dining_hall_near_day
    show mt normal pioneer at cleft
    with dissolve
    play ambience ambience_camp_center_day fadein 2
    play music music_list["doomed_to_be_defeated"] fadein 0
    "Olga was already waiting for us outside the canteen."
    mt "Here you are, lovebirds."
    "She said."
    mt "Did you have a good time?"
    show mt angry pioneer at left
    show mi sad pioneer at right
    with dissolve
    mi "Olga Dmitrievna-san, I..."
    "Miku started, but the squad leader wouldn't even listen to her:"
    mt "Don't even speak, Hatsune, I'll talk to you separately!"
    mt "After noon, go get the program ready for the bonfire, I wouldn't look at you!"
    "Somehow Miku knew that now was not the time to play the temper thing, and hung her head and staggered into the canteen."
    hide mi with dissolve
    mt "As for you, Semyon."
    "Olga looked at me strangely, tilting her head to the side - frozen in a half-smile, as if waiting for some kind of answer."
    "She didn't wait."
    show mt normal pioneer at center with dissolve
    "But she would hardly be embarrassed by such things as the pioneers' reluctance to play along in the mystery game."
    mt "And what am I supposed to do with you? You're off the property without permission. Do you know the rules?"
    "I nodded."
    "Haven't seen any rules, though."
    mt "If this would be the first time, I'd forgive you. {w}But I'm sorry, it's not the first time."
    me "What do you mean?"
    mt "Literally. Should I take you to the teacher's council or something... Let them kick you out?"
    "I got a little tingle inside of me."
    me "No..."
    show mt smile pioneer with dspr
    mt "Really? I thought you didn't care at all - standing there stonewalling."
    me "It's from terror."
    mt "That's what I thought. Okay, let's think about what to do with you."
    "It hit me:"
    me "There's going to be a bonfire tonight! Why don't I help with it?"
    show mt normal pioneer with dspr
    mt "No can do. The firewood has already been taken."
    me "Then I can clean up the clearing or start a fire."
    "Olga twitched the corner of her mouth - apparently she considered making a fire a privilege, not a punishment."
    mt "This place is taken by Slavya."
    mt "And the extinguishing, too... is taken."
    me "Let me at least take care of the potatoes, then."
    show mt grin pioneer with dspr
    mt "You're burning with a desire to redeem yourself, aren't you?"
    mt "Deal! But I don't want to see you and Hatsune together until tonight, understand?"
    mt "I don't want you two running off somewhere together again."
    "I blushed, as it was easy to read a much less innocent context behind her 'running off'."
    me "I promise!"
    mt "Then march to the canteen. And don't forget about-"
    "She was saying something else, but I wasn't listening to her anymore."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_7dl_potato:
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 3
    play music music_list["timid_girl"] fadein 5
    "Miku decided to stay away from me, to be on the safe side."
    "You never know..."
    th "Oh well! I didn't feel like it!"
    "I didn't even sit down - they had a Vienna roll for lunch today, which I could eat in less than half a minute."
    "Here I am..."
    "I thought if I did it quickly, I could get away in time while the squad leader was out and about."
    with fade2
    "Like hell I could."
    $renpy.notify('Idiom - eating a dog means having a lot of experience in something')
    "You can't drink away the experience after all - it seems that Olga Dmitrievna ate more than one dog on communicating with difficult pioneers: firstly, the exits were blocked by Slavya and Alisa."
    "And second - she was back before I had even stopped chewing."
    show mt normal pioneer with dspr
    mt "Here, Syomich. Here, this is for you."
    "She lent me five sacks of sackcloth."
    me "What?!"
    mt "What?"
    me "I mean - why so many?! I can't carry that many!"
    show mt smile pioneer with dspr
    mt "And you decided to feed the whole camp? Hmm... Commendable..."
    "She pretended to think about it."
    me "I haven't decided anything! And anyway!"
    show mt laugh pioneer with dspr
    mt "Wow, we are so stormy! Relax, Syomich, it's not just for you, it's also for the other... ahem... men on duty."
    mt "It's not like we're the only squad going to the bonfire today, is it?"
    me "Uh..."
    "Did I mention that Lazywoman has a natural talent for making me feel like an idiot?"
    show mt normal pioneer with dspr
    mt "Hand them out. And now - get out of here and don't even think about showing up before my eyes."
    me "Jawohl!"
    mt "And don't come back until you've got the whole sack, understand?"
    me "Jawohl!"
    show mt grin pioneer with dspr
    mt "And stop clowning around... Jawohl Petrovich."
    "Rummaging through her pockets, she handed me a key on a paper clip."
    mt "You will return the key to me personally to my hands. Dismissed."
    hide mt with dissolve
    "After looking at me intently one more time, Olga left."
    stop ambience fadeout 3
    with fade
    pause(2)
    scene bg int_dining_hall_day
    with dissolve
    play ambience ambience_dining_hall_empty fadein 3
    "The conversations in the canteen fell silent, the well-fed pioneers scattered to go about their business, leaving only the 'on-duty' - voluntarily and involuntarily assigned to be in charge of the provisions."
    "Olga Dmitrievna sometimes serves her appointments in such a way that there is no way to argue with them."
    play ambience ambience_dining_hall_empty fadein 9
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg int_potato_storage_7dl with dissolve
    "So I, along with about five other pioneers - one per squad - rattled the key, unlocking the padlock to the cellar vault."
    "For a few seconds, picking the insides of the lock with the key, I wondered almost in earnest whether the counselors were deliberately setting up someone else's slip so that they themselves wouldn't have to go here to get their hands dirty and tear their backs."
    "The thing is, there were only pioneers around me."
    "Finally, the lock gave way and let me into the potato habitat."
    me "Ready, set..."
    pause(2)
    "And I was the first to go into the warehouse."
    with fade2
    "There was no one willing to rush ahead of the locomotive."
    "The Lazy Man - and therefore the Reasonable Man - understands several things."
    "Point 1: All work must be done in good conscience, so that no one will be forced to redo it later."
    "Point 2: Any work must be done responsibly, so that they don't think the task is too unimportant."
    "And point 3: any work should be done with feeling, with thought, with the arrangement - so that it takes the maximum allowable time. So it doesn't have to be overdone when it's done."
    "Judging by the fact that the faces around me had already become familiar, everyone here had learned the 'Tao of the Sloth' - both Dan'ka from the second squad, and Lilka from the third..."
    "There were a few other kids from the younger squads - I didn't know them."
    "And there was a little girl among them."
    "At first I thought she was just here to see what we were up to. But no."
    with fade
    play music music_list["everyday_theme"] fadein 3
    "She came up to me, got a bag, and set to work, just like all the others."
    "The pioneers, each armed with his own bag, scattered about the room, and melancholy looted the nets of potatoes."
    "Everyone wanted to pick small potatoes so as not to strain themselves too much, and at the same time not to let their comrades down."
    "The algorithm was simple: what we liked went in the bag, and everything else found a place in the middle of the room."
    "So little by little there grew a mountain of particularly large or particularly ugly potatoes, the kind that no self-respecting pioneer would bake, much less eat."
    "A sort of lagoon, the product of which is branded: it's best not to mess with it."
    "Only one figure was sticking out beside it."
    "The same girl."
    "She walked smartly between us, peering over our shoulders and watching with interest as the bags grew fat - well, that's such a fascinating sight!"
    "A very independent girl."
    "Sometimes I caught a glimpse of her, but I turned away, not paying attention."
    "I had a lot to do, but not much time left."
    "I'd have to be the last one out of here anyway - the keys, which meant it was my responsibility to lock up everything here."
    with fade
    $renpy.notify('Idiom - sneezing cat/crying cat - not a lot')
    "The pioneers hardly spoke, they were completely absorbed in their work: the time between noon and supper was a sneezing cat, and before the campfire everyone wanted to get something done."
    "And I understood them completely about that."
    "I don't know about their own desires, but specifically I had an almost obsessive urge pounding in my temples to see that girl one more time and just say hello to her."
    "It's no big deal, is it?"
    "And yet."
    "In the end there were only three people left in the room - Dan'ka, yours truly, and that girl."
    "Danya, being a responsible and sensible man, took as much as he could without tearing the bag, asked me for some rope, and began to tie up the neck."
    "As for the girl... Things were a little sadder for her."
    "She had a sack full of potatoes - the edges didn't even come together."
    "Problem was, she couldn't have carried all that wealth on her in her life."
    "She looked pleadingly at Dan'ka, at me..."
    "And with a sigh she turned everything over, grabbed the corners, shaking out what she had gathered."
    "As independent as she was, her carrying capacity was not very great."
    th "I wonder what squad she's from?"
    with fade2
    "The girl came up to me, looked at my sack with interest, then at the potatoes I was going through - apparently thinking I had a better or more interesting one."
    "Quietly she sighed."
    stop music fadeout 3
    "And I was surprised to hear my own voice:"
    me "You're going to be here for six months. Take this..."
    "I held out my bag to her."
    "There was an EO for my entire squad."
    "But I knew for a fact I could carry more. She couldn't."
    "Apparently, the last few days have had quite an effect on me."
    "I remembered she was a girl, that I was a gentleman."
    dreamgirl "Gentlesemen!"
    "And I should yield to ladies."
    play music music_7dl["seven_summer_days"] fadein 3
    "Although sometimes on the subway I still don't give way to women."
    "She looked curiously from the sack to me - and even in the half-darkness of the warehouse, I stumbled as I stumbled into her gaze."
    "Potatoes and campfire prep may not be the most interesting thing in the world, but moments like these pay off a hundredfold."
    "Getting to know Miku made me a romantic."
    "It's her fault. No one else's."
    "I stiffened, froze, stopped breathing."
    "There were golden sparks playing at the bottom of the girl's eyes, making the girl's gaze take on an expression of unearthly sadness and a kind of aloofness."
    "I lost my way, my heart missed one step, a hiccup - I was too close to the edge."
    "I take a long time to describe, and really it all happened in a split second."
    "More importantly, when that fraction passed, I realized I didn't regret the wasted half hour in the slightest."
    $ meet('unp','Girl')
    unp "And why did you... To me..."
    "The girl's accent was strange - as if Russian were not her mother tongue."
    "Her eyes gleamed."
    me "It's just... You got your uniform dirty, and supper's coming..."
    "I mumbled, feeling what nonsense I was talking."
    "She kept looking me in the eye - apparently not feeling how uncomfortable it made me feel."
    "Embarrassed, I broke eye contact, and immediately it was much easier."
    me "You won't even have time to clean yourself up."
    "She seemed to have a different opinion of her own form."
    "She took my bag and looked me in the eyes again gratefully."
    "And there's no telling what she said or would have done next"
    play sound sfx_metal_door_heavy_close
    extend ", but the door slammed behind me - Danechka gathered up his gesheft and left in English way, delicately not interrupting our fascinating conversation."
    "We flinched, looked at each other again."
    "Smiled hesitantly, synchronously, kindly."
    "The girl rubbed her hand on her side, and I followed the movement and saw the bruise on her arm."
    me "Where did you get that?"
    "I pointed my finger at the bruise."
    unp "I don't know..."
    unp "I bruise myself all the time, and then I can't remember where it came from."
    "I felt helpless pity for the poor girl with the sack of potatoes."
    "Confused by the sincerity of my feelings, I turned away."
    "I didn't know what to say anymore. I think that was it. That's it?"
    "Angry at myself, I took the empty bag from her - Olga Dmitrievna's orders had to be carried out after all."
    "The hungry pioneers would crucify me if they had this bonfire without the obligatory component."
    unp "Let me help?"
    "The girl squatted down beside me and to the best of her ability began to help."
    "She didn't seem to have dealt with potatoes until now - the 'eyeballed' tubers flew into the pouch, big, rotten..."
    "No wonder it took her so long to dig in."
    me "No, you know..."
    "For some reason I really didn't want to hurt her with the truth."
    me "As a real earner, I have to get my own food. Not with someone else's help."
    "She looked at my gift with confusion:"
    unp "But then... It turns out that I'm not a real earner?"
    me "The very real one. {w}Come to me at the fire, I'll teach you how to bake potatoes."
    unp "Okay. I'll give it a try."
    "She got up easily and, nodding to me, walked away."
    "She lingered in the doorway (I glanced involuntarily at her) and smiled again unabashedly."
    "Nice smile, honestly."
    me "Wait!"
    "For some reason it made me want to hold her. At least for a moment."
    unp "What?"
    me "You... What squad are you from?"
    "She shook her head."
    unp "I'll try."
    $ meet('unp','Pioneer girl')
    pause(2)
    "And vanished."
    "I suddenly felt inexplicably good about this encounter and my own unintentional chivalry."
    th "I'll have to introduce her to Miku. {w}I think they should get along."
    "And that's how it turned out..."
    "We didn't say a word to each other, or remember or introduce ourselves."
    "Still, I feel on some level that I will remember this meeting for a very long time."
    "Because the momentary episodes of childhood sit more firmly in the memory than the long epics of adulthood."
    "Stupid potatoes, stupid assignment."
    "But I was smiling anyway."
    "I must tell Miku about this!"
    "All that's left is to dig up the Japanese girl."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_7dl_camp_cleance:
    scene bg ext_square_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    "After finishing all my business, I went in search of my girlfriend."
    "But for some reason I couldn't find her anywhere."
    "Everywhere I went, she was either gone or she wasn't there at all."
    "I ran every place I could think of, from the music club to the stage to the cabin."
    "The last time I was directed to the square."
    "With completely predictable results."
    with fade
    play music music_7dl["uneven_me2"] fadein 2
    show sl normal pioneer with dspr
    sl "Hello!"
    me "Have you seen Miku?"
    show sl sad pioneer with dspr
    sl "You know, I'm not a fan of formalities... But what happened to «Hello, how are you?»"
    me "Oh, I'm sorry."
    "Slavya's rebuke sobered me somewhat, and I exhaled with an effort."
    show sl normal pioneer with dspr
    sl "That's okay. Why are you running around like that?"
    me "You see, I was running an errand for Olga Leninovna, and I lost Miku!"
    show sl smile2 pioneer with dspr
    sl "You can't do without her now, can you?"
    "For a moment, a sly look flashed in the girl's eyes."
    me "Uh... Well, something like that."
    "Don't tell me I saw the girl in my dream!"
    show sl normal pioneer with dspr
    sl "Try looking for her at the fire glade. I think she was headed there after rehearsal."
    me "What about... It's off the grounds."
    sl "So what? You're going to help her. {w}So it's okay. Go!"
    me "If you think so..."
    scene bg ext_polyana_day
    with dissolve
    play ambience ambience_forest_day fadein 3
    "And Slavya didn't lie - Miku was really here!"
    me "Hey, hello!"
    show mi normal pioneer with dspr
    mi "Hello, Senya."
    "She waved her hand faintly."
    "She looked depressed."
    me "Is something wrong?"
    mi "No... I'm just tired. I've had to run a lot the last few hours."
    with fade2
    "It is known that the vacuum in the soul is filled by whatever comes closest - whether by demons or angels."
    "It is known that a holy place cannot be empty - and perhaps it would be worth inventing that place if it did not exist."
    "So would Miku."
    "She certainly would have been worth making up. Not a bad candidate for a creative application, it seems to me."
    "I'd take the moon marble and cut away anything superfluous, not look into the statue's eyes, remembering that eye contact over half the time of communication is a direct path to falling in love."
    "And I can't. You can't."
    "Sakishita's visit still gave me a nasty feeling of impotent anger - I wanted to spit and say nasty things."
    "But the obvious fact that the agent wouldn't back down was for some reason only becoming apparent now."
    show mi smile pioneer with dissolve
    "And it was quite depressing."
    "Miku, on the other hand, smiled benignly, and was terribly annoying because of that."
    "I don't mind politeness, but Japanese politeness can piss off even a saint!"
    "And in contrast to the way we managed to be friends, the girl's bunkering was like a knife to the heart."
    "Here we go again. {w}Smiles. {w}And looks politely into the eyes."
    me "It's about yesterday, isn't it? {w}About getting picked up early?"
    show mi dontlike pioneer
    "I immediately regretted the question - it had obviously been asked too bluntly."
    "For all our resemblance and sympathy for each other, there's no denying the cultural differences."
    mi "That's... Well..."
    "And we quite obviously belonged to different cultures."
    "Miku would have been more accustomed to wiggling, subtly leading her interlocutor to an unpleasant or tense topic."
    show mi sad pioneer with dspr
    mi "By and large..."
    "And I was taught that directness is the best policy when dealing with friends."
    mi "And how are you doing?"
    "She got out of it."
    "Rude. But effective."
    with dissolve
    "I wondered."
    "Since the search began, a doubt has crept into my soul for the first time as to the urgent need for a story about that very girl."
    "I took her too positively - not to become the cause of unnecessary and unwarranted jealousy..."
    "Yes! Exactly!"
    "After imagining for a second how jealous Miku would be, I realized I didn't want to see her in that role."
    "Even though we didn't seem to have much of a beef with each other."
    show mi happy pioneer with dspr
    mi "Okay, you think for now! I'm going to take another dip."
    "She held out her soiled palms to me."
    mi "All dirty."
    me "Hey! I thought I could help!"
    hide mi with dissolve
    mi "Too late! I did it all myself!"
    "She took off, unbuttoning as she went."
    "And I, after thinking for a while, headed after her."
    "Certainly the oddities of our behavior require me to sit down somewhere and mull them over."
    "But I'd rather it be somewhere where I at least won't let her out of my sight!"
    stop music fadeout 3
    scene bg ext_beach2_day_7dl with dissolve
    play ambience ambience_lake_shore_day fadein 3
    "The descent turned out to be quite steep, and, clinging to roots and branches, I was relieved for a while of the constant inner monologue."
    "The emptiness in my head..."
    play music music_7dl["ltyh"] fadein 3
    "I wish I could stop thinking altogether!"
    "Buddhists call nirvana the total abandonment of the thought process. I wonder if I could dive that deep."
    "Because after making a complete turn, my thoughts would return again and again to the girl splashing below."
    "I'm very attached to her, but do I want our connection to turn into quite logically the next romantic connection?"
    "Right now, as long as you can feel free to be around her, talk about anything and not filter what you say for fear of hurting the other's feelings."
    $ renpy.show("bg int_looney_bin_7dl", what = D3_intro("bg int_looney_bin_7dl"))
    with fade
    "Through the corridors of memory, I finally got to the picture that had been haunting me all this time."
    "The shutters were ajar."
    if herc:
        "For a second there was a sharp prick somewhere in my forehead, the back of my head felt a hard, cold surface..."
    elif loki:
        "It cut sharply inside - as if everything was sick all at once, and the snow was so soft..."
    else:
        "I felt twisted, as if I had opened my lungs to air, and liquid frost was rushing in..."
    "But at the very bottom, beneath a layer of silt, suppressed by the touches of stiffening fingers, a picture could be discerned."
    "The frenzied crowd, united by a single impulse, the superbasses reverberating in their chests."
    "And there's a girl on the stage."
    "And, as if there was no break, the monologue-prayer continues."
    "{i}You're good, you're the real deal - the rest of us, when we get to the international stage, immediately give up our roots, go to international languages and international culture.{/i}"
    "{i}Very few names can be recalled of those who remained true to themselves even abroad, who continued to work in their native language — «Rammstein», for example.{/i}"
    "{i}And you.{/i}"
    "{i}And it's great because when I buy a stick and a ticket at the L.A. CDC, I'm not afraid that what I came here to hear from the stage is not what I came here to hear... we all came here.{/i}"
    "{i}Do you hear that? You hear that? It's all Europeans, Americans, Russians - those who couldn't get to Nihon all this time because of a bunch of bureaucratic hurdles - we all sing along to your songs in that language, those words that we once fell in love with.{/i}"
    "{i}Don't lose your way. You're too nice, and I have no idea what the world is like without you yet? I've managed to forget like a bad dream the time before I met you, as if one day I was just made up along with my whole story.{/i}"
    show mi smile swim with dissolve
    mi "What are you thinking about, Senechka?"
    "Miku inquired, gazing surreptitiously either at me or at the darkening sky over the water."
    "She was walking up the slope from the creek, again in her frivolous bathing suit - she must not have even taken it off."
    "She must have been informed by Slavya of the opportunity to swim without fear."
    "Either she had already participated in the campfire preparations once - after all, the shift lasted three weeks, they must have at least gotten together a couple more times to sing and bake potatoes?"
    "Sitting down on a log next to me, she brazenly took my own hand away and began to draw something on it."
    show mi normal swim close with dspr
    "It was pretty ticklish, but I stoically endured it."
    me "What are you doing?"
    mi "Kanji. I wish I had a brush and ink now."
    mi "I was first in our calligraphy class, you know?"
    me "And?"
    mi "Look..."
    show mi smile swim close with dspr
    "The ticklish touch of claws again."
    mi "This kanji sounds like «nin» and means «human»."
    "Lambda from «Half-Life», no less."
    mi "And this kanji — «ai», means «attachment» or «love»."
    "Complex letter construction from a letter «Pi» and a whole bunch of scribble-drops."
    "I was embarrassed."
    me "Love like love for the motherland and parents?"
    mi "Like a woman to a man."
    "Miku looked at me point-blank and I took my hand away."
    show mi upset swim with dspr
    "There was silence on the beach as I tried to think of a way to counteract the situation."
    "And there wasn't one."
    dreamgirl "International women's gesture to a particularly stupid man, by the way..."
    "And they also say that's how the deaf and the blind can communicate with each other."
    "There's also a word for... I can't remember."
    "After looking into my eyes a little more, Miku relaxed - and snuggled up to me."
    "She rested her wet tails on my lap and her head on my shoulder."
    "She closed her eyes and sighed happily."
    mi "I wish this night would never end, don't you think so too?"
    me "Yeah..."
    "A warm wave of tenderness swept over me, memories of today, of yesterday-all the time we'd known each other."
    "The days galloped by, it seems like yesterday I was waking up, and she greeted me first after getting into camp, and here we are sitting here now, with no one in the world we need."
    "And on the other hand - it's like we've known each other forever."
    hide mi with dissolve
    "Trying not to move too sharply so as not to disturb the girl, I turned and inhaled the scent of her hair."
    "Eucalyptus. A cure for coughs and anger."
    "A pill for the past."
    th "What will you do when that greedy old man arrives?"
    "Silently, I asked the turquoise dipper."
    th "In fact, it makes no difference, even if you refuse tomorrow, the next day's departure anyway."
    th "And guess who's going to pick you up and take you where?"
    th "So is it worth the hassle? What for?"
    "And at that very moment, the girl began to wiggle, making herself more comfortable."
    "And thus answered an unspoken question."
    "It's worth it. Absolutely worth it."
    "Just for the sake of sitting on the beach and drying off, basking against each other."
    stop music fadeout 3
    scene
    $ renpy.show("bg ext_beach2_day_7dl", what = Dawn("bg ext_beach2_day_7dl"))
    with dissolve
    "It was getting late."
    play music music_7dl["shehasgone"] fadein 3
    "The far shore, almost completely merging with the horizon, was slowly biting scarlet, and the air smelled of anticipation of wonder."
    mi "We had a full hour."
    "Miku complained to me."
    mi "We were supposed to have a bonfire just for the two of us, I've never had a bonfire for two, not even in school, not even with Dad, not with anyone."
    me "So with no one or with a squad?"
    "I couldn't help myself."
    mi "Come on."
    "Tapping my shoulder with her head, Miku pulled away."
    "From the river, the anticipation of coolness and wet, dark silence that is only possible when swimming alone."
    "Somewhere far, far away, a bird cried out. The forest breathed peace and tranquility."
    "It was all so long ago - what, ten years ago? Twenty?"
    "On the west side, a pale nickel of the moon appeared, barely visible, and I pointed it out to Miku."
    scene
    $ renpy.show("bg ext_beach2_day_7dl", what = Notch("bg ext_beach2_day_7dl"))
    with dissolve
    me "Come on, me."
    "I agreed."
    "Can you imagine - our tiny little planet, and we're a measly 300 kilometers from civilization - and that's it!"
    me "It's like no man has ever set foot here, there's not a soul within ten minutes walking distance."
    mi "I, too, am a resident of the metropolis."
    "On reflection, Miku replied."
    mi "It's important to me that there are always people around."
    me "And there's no way I can get used to the fact that it's all so far disconnected and there's no services, no cell phone service, and no shared network."
    mi "Shared network?"
    "Miku put her head back on her shoulder, hinting at continuing the conversation."
    "I had to continue."
    me "How should I put it..."
    with fade
    me "The world is evolving. But technology is developing especially fast."
    me "Everybody needs it fast, cheap, and to be able to reach the other side of the globe - with a delay of no more than forty milliseconds."
    me "Everyone needs to be able to get up and carry this 'fast-cheap' with them and pamper themselves on a trip or while waiting in line at the health clinic."
    me "From the first, Internet service providers sprout."
    me "From the second, cell phone carriers."
    me "And Lem also wrote."
    me "A man needs a man."
    me "Here's what people who have shrunk the globe to the size of your backyard know - and given the desire and financial means you can meet someone you would never have known - living somewhere in Canada or Estonia, and the next day sit together with him in some pub, confusing English words."
    me "For example, there's such a thing in Japan as fully synthesized music - electronic, all the way through, including the singer's voice."
    me "Wouldn't know about it and didn't know about it, being limited to the contents of the neighborhood library and playground games."
    "But once you're wrong about the query «hello, world», you make some mistakes, which the search engine corrects at its own discretion."
    me "And you find yourself in a whole new plane of reality you never knew."
    me "The world becomes much more compact for those who have someone to worry about. And, of course, much quicker."
    th "You, Miku, are popular in my world precisely because of the Internet."
    th "Non-white people write songs to you, draw pictures of you, and create the 'cyan' page phenomenon - when a query for your name actually turns Google blue-green."
    th "There's a lot of you, and it's great."
    th "But for the same reason there is no hope that one day in a crowd somewhere near «Zepp Sapporo» I will be able to see the familiar eyes. You were invented, embodied and drawn - the mascot, the mascot of the idea-prayer of humanity united in a creative impulse."
    th"{i}Creator… You.{/i}"
    th "And though you are alive and warm and breathing beside me, it is an extra penny in the piggy bank that I am far from home at my own place."
    th "Between me and my dusty den lie not only years and miles, but something so elusive but irresistible that separates the worlds from each other."
    "And I don't even doubt that my odyssey by all the laws of the genre is bound to end."
    "The bow of the trireme will inevitably touch the shoal of Ithaca."
    "So it will be - I shall be removed as an extraneous element."
    "So it is desirable to make the removal of me as painless as possible."
    "And that binds my hands more than any law of predestination."
    me "People can chat, shop, store information, and gain knowledge about absolutely everything humanity knows - just by making the right request."
    me "All this from the comfort of one's own home."
    mi "What an interesting world you've described, Senechka."
    "We sat gazing at the golden water surface, listening to the breath of the wind playing in the crowns of the pines, Miku absorbing my story with wide-open eyes - imagining, of course, everything wrong and incorrectly, like a magical tale of incredible possibilities."
    "And I myself believed that the possibilities were incredible, and that my world was more magical than even my fantastical displacement..."
    mi "But I guess it's not as smooth and easy as you describe, is it?"
    "Asked Miku, when I finished the story."
    me "Of course."
    "Technical difficulties, technical processes. Most importantly, money. The primary investment in a new direction."
    "Sapienti sat, but investors are not always as reasonable as we would like them to be."
    mi "So there's a downside?"
    me "Absolutely. Radio communications would require a whole bunch of repeater towers, the Internet would require millions and millions of kilometers of cables, a couple thousand satellites would have to be launched into the sky."
    me "And combine it all into one system."
    mi "And there would be radio waves all around, right?"
    "I nodded."
    mi "And we'll run after them with a net! Like butterflies!"
    "Miku was fooling around, smiling - she was in a wonderful mood."
    "So it would be quite natural and organic to embrace her. Wouldn't it?"
    with fade
    "Except I guess I shouldn't have done it."
    "I put my arm around her shoulders, but her back remained stiff under my palm. As if I'd said or done something wrong again. Like I always do, though."
    mi "Silly baka Senka."
    "Miku moved when I removed my completely misplaced hand."
    mi "Was it so hard to hug me while you were telling me your magical tales of a world without borders?"
    me "I..."
    mi "You blew it."
    "Pushing away from me, she stood up and, ignoring me, began to climb up to the fire glade."
    "I guess that meant the end of the conversation."
    "The phone beeped, marking the eighth hour. It was time to move on to camp if we didn't want to stay hungry. That's what I said, but Miku didn't even pay attention."
    dreamgirl "So you decided to push and push her, huh?"
    th "What's wrong with that?"
    dreamgirl "No, everything is okay. Except for a smaaaaaall, insignificant feature of the situation."
    th "What's that?"
    dreamgirl "You're in different weight classes. In a whole range of senses. And where you're pushing her, her carcass takes it as a direct kick in the butt."
    th "Well, maybe that's the right thing to do."
    dreamgirl "Sick fuck. She's still forgiving you, but do you have any guarantee that this will continue?"
    th "Look, why do you care? Wouldn't it have been better and more interesting if I'd have taken her down right here in the clearing?"
    dreamgirl "It might have been better. {w}At any rate, between beatings and love, I somehow gravitate more toward the latter."
    th "But it's probably too late to comfort her now, isn't it?"
    dreamgirl "Yeah, definitely."
    th "And it's no use talking to her."
    dreamgirl "And that's how you say..."
    th "But I can't let her..."
    dreamgirl "You can't. But that's a very poor excuse for hurting her right now."
    dreamgirl "I just want to ask - do you want her to go away and forget you like a bad dream? {w}Or do you want her to at least remember you with a warm smile once in a while?"
    th "I want her to be all right. So that I won't be in her life with my problems, doubts and difficulties."
    "After all, it was with my encouragement that she made the choice between what her heart is for and what you can't trust anyone else with."
    "And that's worth a lot, the highest degree of trust I could never have earned."
    dreamgirl "Then go and kiss the girl already, retard."
    th "Here we go again. I told you..."
    dreamgirl "Look, you have two choices out of this situation, either by Miku's side or looking at the back of her head. Take your pick."
    dreamgirl "No, you can't combine the two."
    th "But I don't have the resolve. I absolutely know that."
    dreamgirl "The closer and warmer you get with a person, the less power you have to make a qualitative difference in your relationship."
    dreamgirl "For you've already furnished your territory together, carpeted it, draped it with tulle..."
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene bg ext_polyana_sunset
    show mi normal pioneer
    with dissolve
    me "Miku, honestly. If it weren't for circumstances, I really wish we could have had something."
    "I didn't manage to catch up with Miku until just before the bonfire."
    me "But you're going away - and like the hell you're coming back from your Japan!"
    me "And I myself..."
    th "I could wake up at any moment."
    me "So why torture each other when we're already good together?"
    mi "Let's go to camp, supper is getting cold."
    "Miku turned around - and she wasn't smiling anymore. But there was no expected sadness on her face, either."
    "She held out her palm to me with a hint, and I obediently took the girl under my arm."
    show mi dontlike pioneer with dspr
    mi "I was willing to try."
    "Calmly she replied."
    mi "Not even enough."
    mi "I believe that love is like a butterfly. There is a cocoon at first, but it takes time and work for it to turn into a butterfly."
    mi "And if there isn't, it just rots away."
    show mi upset pioneer with dspr
    mi "Do you know how stillborn love hurts?"
    me "I'm sorry. But better not at all than like this."
    me "It's better to realize there's no chance than to bang your head uselessly against the wall. Especially if there is no wall..."
    mi "You said that before. {w}We're going?"
    "Her smile was sad."
    mi "I believe you too much. You know the right thing to do."
    "And that unyielding faith of hers cut ten times harder than the quiet anger of five minutes ago."
    mi "You know, don't you?"
    "I averted my eyes for the umpteenth time. I was tormented by a moral and ethical complex."
    "And all my life I thought I'd left it at home in the closet. On the same shelf as my faith in people."
    me "I guess so."
    "Deafly I answered."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_7dl_firecamp:
    play music music_list["silhouette_in_sunset"] fadein 3
    if alt_day5_mi_7dl_voyeur:
        scene bg ext_square_sunset with dissolve
        play ambience ambience_camp_center_evening fadein 3
        "After the potatoes, I was so tired that I think I fell asleep right on the bench in the square."
        play sound sfx_7dl["eat_horn"] fadein 1
        "Because it was the same horn that woke me up."
    else:
        scene bg ext_camp_entrance_sunset_7dl with dissolve
        play ambience ambience_camp_entrance_day fadein 3
        "Another man's soul is a mystery. Especially if it's a girl whose opinion has suddenly become very important."
        "And you've suddenly given her something that could just as easily have made you break off all contact with me... as it could have made you forgive me..."
        "Depends on your stock of generosity alone."
        play sound sfx_7dl["eat_horn"] fadein 1
        "And Miku just walked beside me, leading me by the hand, and the horn caught us just as we were passing through the camp gate."
        "Still, silently, she turned and led me toward the canteen."
    scene bg ext_dining_hall_near_sunset
    with fade
    "There was no one else on the porch - we were definitely the last ones."
    play sound2 sfx_open_door_2
    pause(1)
    scene bg int_dining_hall_people_sunset_7dl with dissolve
    play ambience ambience_dining_hall_full fadein 0
    "I had barely had time to take a window seat when Olga floated out into the center of the canteen and cleared her throat noisily:"
    mt "All right, children! Everybody listen up!"
    "Well, that way she'll never distract anyone from eating."
    "And it became obvious to the counselor a few seconds later, too."
    play music music_list["always_ready"] fadein 3
    mt "Alright… {b}CHILDREN!{/b}"
    with vpunch
    "She barked, as she usually did at the lineups."
    "And now that was another thing!"
    stop ambience fadeout 4
    "The hubbub and clanging of forks on plates subsided."
    "The counselor nodded contentedly:"
    mt "That's it then! There will be a bonfire after supper! No change! Is that clear?"
    show us smile pioneer at cright with dissolve
    us "Clear! What about the potatoes?"
    "The little one didn't change at all."
    show mt smile pioneer with dspr
    mt "You don't have to worry about that, each squad has a duty officer who'll take care of that."
    show us dontlike pioneer with dspr
    us "I don't get it. Who's that?"
    show mt normal pioneer with dspr
    "Olga only brushed it off, and Ulyanka, frowning, went back to her fish and chips."
    hide us with dissolve
    mt "The fire is made by Feoktistova, the clearing is cleaned up, but just in case, clean up when we get there."
    mt "I'm done."
    "Olga graciously allowed the pioneers to continue their meal and returned to her table."
    hide mt with dissolve
    "Only now did I realize how hungry I was and paid tribute to dinner."
    "Apparently, I was so carried away that when I took my eyes off my plate I suddenly realized that half the squad had safely finished their business and left the canteen."
    "And Miku was among them."
    with fade
    "With a sigh, I took the dirty dishes to the sink and went outside."
    play sound sfx_open_door_strong
    pause(2)
    scene bg ext_houses_sunset
    with dissolve
    play ambience ambience_camp_center_evening fadein 3
    if not alt_day5_mi_7dl_voyeur:
        "And somewhere people live very differently and rejoice not in their victories, but in their smiles."
        "Somewhere people put the joy of those around them above all else."
        "..."
        "What the hell am I forgetting in this 'somewhere'?"
        th "The road arises beneath the feet of the walker..."
        dreamgirl "But the air bridges beneath them are crumbling."
        if loki:
            "In tune answered the inner voice."
            dreamgirl "And not another word about the ex - I'm fixing the attic, I'm mending your roof..."
            th "What's that about?"
            dreamgirl "It's just that a girl won't ask about who you're with and where before her - if she plans to send you to a known address and wish you were happy there."
            dreamgirl "And you're like, 'I very much believed in people, now go to hell'."
            dreamgirl "It's an unobtrusive hint that she'd do well to grab hold of the rail and follow everyone else."
    else:
        "My path went to the cabin where my old things were kept."
    stop ambience fadeout 2
    scene bg int_house_of_mt_sunset
    with dissolve
    play ambience ambience_int_cabin_evening fadein 2
    if not alt_day5_mi_7dl_voyeur:
        "And as much as the squatter in my skull annoyed me, it was hard to deny that he was right."
        th "...I'll apologize."
        dreamgirl "Yes, please do."
        "Firmly promising myself to do just that, I got into my winter clothes - it's hot, but it should save me from mosquitoes."
    else:
        "After overcoming the urge to lie on the bed for a while, I got into my winter clothes - it's a little hot, but it should save me from mosquitoes."
    scene bg ext_square_sunset
    with dissolve
    play ambience ambience_camp_center_evening fadein 3
    play music music_list["lightness"] fadein 3
    "And, slamming the door, went to the square."
    "All our people were already standing there."
    "After counting us out on first and second, they divided us in pairs, turned us to the right, and drove us to the gate."
    "I, unfortunately, didn't get a pair at all."
    "The things is that Shurik, who was supposed to be standing with Electronik, was kind of absent, and so he took advantage of the situation and instantly moved next to Zhenya."
    "Slavya was already hanging out somewhere in the vanguard - thus all the others found themselves in pairs by the cabins."
    mt "Semyon!"
    "Called Olga."
    show mt normal pioneer with dissolve
    "I looked up from the concrete tiles."
    mt "Can I ask you something?"
    me "You can try..."
    "Olga walked beside me, trying on my step - it wasn't that difficult, our leg lengths were about the same."
    "And it cut me again with the obvious fact that she is a professional educator and psychologist."
    th "I wonder if she's aware that I can see through her grimaces."
    dreamgirl "She knows you know she knows you know!"
    "For a couple of minutes we walked, falling further and further behind, until there were fifteen yards between us and the redheads walking ahead and we could talk without fear of being overheard."
    mt "Syomich, I got a call from the city."
    me "Cool."
    "I replied indifferently."
    th "Am I supposed to fall to my knees and cry for joy now?"
    scene bg ext_camp_entrance_sunset_7dl
    show mt normal pioneer
    with dissolve
    "Olga was silent for a moment - obviously choosing the most appropriate words."
    show mt normal pioneer with dspr
    mt "It concerns Hatsune."
    "She started it."
    mt "Miku's father, Arkhip Andreich, called."
    mt "He asked very much for my help in solving yesterday's problem."
    me "You mean the old fart who wanted to take Miku away yesterday?"
    mt "Semyon! What a thing to say!"
    th "Put me in the corner for my words."
    me "Am I right?"
    show mt sad pioneer with dspr
    mt "Yes."
    "Olga walked beside me, looking down at her feet, thinking intensely about something."
    mt "I knew him before... Before he left to build the power plant in Japan."
    mt "So he asked me as an acquaintance, not as a squad leader or a teacher."
    stop ambience fadeout 2
    scene bg ext_backroad_day_7dl
    show mt sad pioneer
    with dissolve
    play ambience ambience_forest_evening fadein 3
    "I hugely disliked the Japanese way the counselor was bringing us to the topic of conversation."
    "It sounds like there really is something extremely unpleasant."
    if alt_day5_mi_7dl_voyeur:
        th "I hope she's not aware of what happened a few hours ago - otherwise the conversation would have gone very differently."
    mt "Anyway, believe it or not, he asked me to help his daughter."
    th "Help?"
    mt "To determine her fate."
    "I was so surprised that I even lost my step for a second."
    if alt_day5_mi_7dl_voyeur:
        "Given that we both spat on minimum security, Miku risks being {b}imposed{/b} on her fate."
        "Nine months from now."
        "This is where I first felt all the benefits of my ethereal status here."
    else:
        "Miku, in my opinion, is old enough to make her own choices about what she wants."
        "As long as she doesn't get hooked on drugs and join the ranks of Tsoi and Hendrix."
    me "What do you mean? Not to interfere with Sakishita when he comes to pick up Miku?"
    mt "No! I..."
    me "I can see how much trouble she's giving you - you've even relegated her to the very margins of life."
    show mt angry pioneer with dspr
    "And that's where Olga got offended - childishly, sincerely."
    mt "You're a fool, Syomich. A real one."
    if alt_day3_mi_7dl_donor == 0:
        mt "You were at my house, didn't you see the pictures?"
        mt "I've been coming here all my life as a pioneer girl, only the last few years as a counselor."
        mt "And you're telling me here that I want to get rid of bore. {w}You have no sympathy or trust in you at all?"
    me "Because I can't understand you at all."
    "I mumbled."
    me "What do you want me to do?"
    mt "That's better..."
    "Olga leaned into my ear and lowered her voice to almost a whisper."
    scene bg ext_polyana_sunset
    with dissolve
    play music music_list["dance_of_fireflies"] fadein 3
    "If the way {i}there{/i} seemed long to me, the way back felt three times shorter."
    "Well, the third attempt was the fastest - I didn't even have time to get bored while I was talking to the squad leader about what was right and what was wrong."
    "But while that was going on, the last of the trees parted and we came out into the fire glade."
    "No one had had time to make a mess, and the fire pit was lined with freshly picked cobblestones, and the needles were swept to the holes around the perimeter."
    "Miku had clearly done her best here."
    "Meanwhile, the slender ranks of pioneers mingled, broke - and instantly occupied every available spot."
    "Clearly, the best seats were reserved for the first squad - as the most useful in terms of preparation for the activities."
    "But Miku was almost indispensable today - she set the stage and didn't piss off the people around her."
    "And now, at all, she brought her guitar, strumming softly on the strings, tightening up the sound."
    "Slavya, sitting in the very center of the fire pit, felt my gaze, raised her head and nodded hello."
    "At her feet a few pole sticks were made up into a house, and underneath them a paper with piled pine needles and chaff was already blazing merrily."
    "The first sticks, having dried, engaged - and from a spark a flame was born."
    play sound_loop sfx_forest_fireplace fadein 3
    "The pioneers came closer, some already reaching for the warmth."
    "And Slavya gathered bigger logs, drier branches, until she had built a monumental structure."
    "It was going to burn for two hours, and in such conditions hardly anyone would put wood on it."
    "There would be time for the fire to just burn until about nine o'clock, and then the people would start baking potatoes."
    "Everything is strictly planned and thought out."
    "Too bad it's not a sleepover, of course."
    "It would be nice to make a bivouac, set up tents, set up an awning and boil tea in a black, smoky pot - where else in the city would you try it?"
    "Apparently, Olga Dmitrievna shared my view of things, because she said to no one:"
    stop music fadeout 4
    mt "This time, unfortunately, without a hike."
    "Unfortunately..."
    show blinking
    play music music_7dl["lastlight_guitar"] fadein 6
    "I closed my eyes, and the guitar sighed sadly on the other side of the fire."
    "And the unhurried, melancholy plucking of the strings told the fading evening that this particular one was our last."
    "Our good evening."
    "There will be no cross lights on the road, no hero appearing from nowhere to reach out and save at the last moment."
    "No one will ever find us, lost in memories and fictions - we'll go nowhere."
    "And, hopefully, we'll go nowhere together."
    show sl normal pioneer with moveinleft
    sl "Resting?"
    "Slavya moved away from the fire and took a seat next to me."
    me "Something like that."
    sl "You seem sad... Did something happen?"
    me "Yeah... You know what it is..."
    me "I don't want to be alone. Is that too much to ask?"
    me "I vitally need someone who both listens and talks and understands me."
    me "Do you hear what it sounds like?"
    show sl serious pioneer with dspr
    sl "Haven't you found this person yet?"
    "Slavya threw a glance at Miku and smiled when she answered."
    show sl smile pioneer with dspr
    me "I don't know exactly. {w}You know, on the one hand I wish I could spit on it and take what they give me."
    me "And on the other hand..."
    sl "You don't want to be an extra, do you? {w}She expects you to act like a man, and you don't want to act like one out of spite?"
    "As annoying as Slavya is, you can't deny her powers of observation."
    sl "And setting ambition aside... {w}What do you really want?"
    me "I want... {w}Listen, but that's quite personal!"
    show sl laugh pioneer with dspr
    sl "Gotcha!"
    "Slavya chuckled."
    me "And you're mocking..."
    sl "I'm not mocking."
    "Serenely she smiled."
    show sl smile2 pioneer with dspr
    sl "I couldn't help it, I'm sorry. {w}You're just sitting there, pouting like an owl on a croup."
    "With a pat on the shoulder, Slavya got up and disappeared into the twilight."
    hide sl with dissolve
    "The whole time Miku was looking right at me."
    "Catching my gaze, she winked and went back to playing."
    with fade
    "And the evening was warm and tender again."
    "The dependence is evident."
    "And Olga Dmitrievna's request - to tell you the truth, I expected her to forbid me to interfere or in any other way influence."
    "In fact, it turned out to be somewhat different."
    with fade
    "The strings sobbed wistfully from the side - an entirely different technique, an entirely different approach to playing, and the worries of the last night were replaced by a confession:"
    dv "And people walk through the world. {w}Their words are sometimes rude..."
    "And the Japanese girl rose from her seat and approached me."
    show mi normal pioneer with dspr
    mi "Feeling bored?"
    "More than half of her question was a statement."
    "And it wasn't clear whether it was self-righteousness or exactly the same worries that caused it."
    "Though my girlfriend never struck me as overconfident or sassy."
    me "All evening I can't get rid of the impression that I forgot to do something."
    mi "Like what?"
    "I tried not to show too much vested interest in what she said, but I don't seem to have been too successful."
    show mi smile pioneer with dspr
    mi "I'm thinking, I'm thinking... Why are you so worried?"
    me "Me?! I didn't do anything..."
    show mi grin pioneer with dspr
    mi "Senya, your fingers are shaking."
    "I sighed and confessed."
    me "Yes, I'm nervous. So what?"
    "Rude again."
    "Instead of spending time together and enjoying seconds in halves, I'm getting all rude again."
    me "I'm sorry. That didn't sound good."
    show mi laugh pioneer with dspr
    mi "It's not very good! Senka, what happened?"
    me "Nothing."
    "I honestly confessed."
    "But Miku wouldn't be herself if she could be bought with such a simple excuse."
    mi "Okay..."
    "She hesitated, scratching the wood we were sitting on with her fingernails."
    mi "In that case..."
    show mi shy pioneer with dspr
    extend " what {b}should have happened{b} that made you such a downer?"
    me "I'm just talking about the same thing, the girl thing, the soccer thing."
    show mi upset pioneer with dspr
    mi "Senka, you're a bore! Trouble is inevitable in life, and now what - to fall on your side and cry all the time?"
    me "No, you have to be happy and jump all over the place."
    "Irritatedly, I replied."
    mi "And I don't want to think about what the day after tomorrow will be like, got it?"
    dreamgirl "Look, she seems completely unaware of her father's call!"
    th "I guessed that."
    mi "If you put it that way, camp shifts have such a nasty habit of ending. Let's have a wail and misery from the drive-in itself now, eh?"
    mi "I've got potatoes and bread and..."
    menu:
        "Guitar chords":
            $ alt_spt += 1
            "I prompted."
            mi "There! You understand. No one can take the music away from me."
            "She bumped my forehead again."
            mi "And the memory of what happened here, too! {w}Even though I sat there for two whole weeks for nothing!"
        "Me!":
            $ lp_mi += 1
            $ alt_hpt += 1
            th "A faithful friend sitting by your side."
            show mi laugh pioneer with dspr
            mi "You've got self-importance, Senka!"
            "Miku laughed, and I gladly joined her."
    "A feast during the plague, dancing on the bones of the world."
    "And that's when I realized I'm no good at lying."
    me "It gets worse, princess."
    "I reported it."
    me "That old fart of yours arrives tomorrow - he's got all the paperwork, he's got all the permits."
    show mi shocked pioneer with dspr
    mi "What do you mean, 'all permits'? Pa wouldn't do such a thing without consulting me!"
    "I shrugged my shoulders."
    mi "Senka, come on, tell me what you're keeping quiet about!"
    "Getting angry, Miku pushed me so hard that I lost my balance..."
    scene black
    $ persistent.sprite_time = "night"
    $ night_time()
    $ renpy.show("bg ext_polyana_night", at_list = [sdl_transform5], what = Noir("bg ext_polyana_night"))
    with vpunch
    play sound sfx_fall_wood_floor
    "And fell backwards, on my back!"
    play music music_list["confession_oboe"] fadein 3
    scene
    $ renpy.show("cg d4_mi_dj_lib0_7dl", what = Notch("cg d4_mi_dj_lib0_7dl"))
    with dissolve
    "Thud. Thud. Thud."
    "What's that pounding? Heart?"
    "Mine? Or hers?"
    mi "Ah..."
    dreamgirl "Of course. The canon of the genre.{w} You just couldn't help but be one on top of the other."
    "I remembered it all the time, but at the most important moment I simply forgot."
    "I'm on her."
    "And how, I wonder? It was her, she pushed me!"
    "Unknown. But it was my elbows and knees."
    "Miku certainly didn't bump the back of her head - as it was my palm on which her head rested."
    th "So why doesn't she open her eyes?"
    "I walk in the rain and freeze in the sun - but I am so smiling inside. For you are The One."
    "We are tightly pressed against each other."
    "In fact, if I hadn't reacted, I would have crushed the girl with my own weight."
    "Miku was just shaking and sighing faintly, making no attempt to get out from under me."
    me "Oh, I'm so sorry... I'm going to get off now."
    mi "No."
    me "What?"
    "I waited, and she finally opened her eyes:"
    scene
    $ renpy.show("cg d4_mi_dj_lib_7dl", what = Notch("cg d4_mi_dj_lib_7dl"))
    with dissolve
    mi "Don't go away just yet."
    me "Miku?"
    mi "Just a little... please."
    "She was babbling something, and I could feel the moisture on my cheek."
    "It was already so dark that you couldn't see anything outside the field of light from the fire."
    "We would certainly be spotted - sooner or later."
    "When they go looking for us on purpose."
    "To see us in the dark behind that thick driftwood where we were just sitting would hardly be possible."
    th "Now what, to stay in that pose?"
    "Well, what happened to my lauded morals?"
    "I can feel myself sinking - why do I obey?"
    "That boundary that held for so long. We are friends. Are we?"
    "{i}Please stay…{/i}"
    "Party in your head - ounce-ounce, 180 beats per minute, adrenaline, alcohol and serotonin in one!"
    "Who knew that someone else's intimacy - the invasion of my personal space! - would have such an intoxicating effect on me!"
    "Timidly, as if afraid of me, she hugged me, clasping her hands somewhere behind my back."
    "Thud."
    "Redoubt after redoubt."
    "The frenzy in the voice with which they usually cover their faces with kisses, until the last touch of their palms on the platform through the train window, don't want to hang up, calling thousands of miles away."
    "With me..."
    th "But why me? {w}What's so special about me?"
    mi "Yes, I know you think it's wrong."
    "She was talking, and she was clinging harder and harder to me herself."
    mi "And you're right. I am wrong. Flawed."
    "Certainly I would have had the strength to get rid of her grip without a problem, but for some reason I didn't."
    "Thud, thud."
    "Bastion by bastion."
    "Bastion after bastion, armor of worldly vulgar cynicism, disbelief in love and people."
    "Everything has fallen."
    "No morals or common sense left."
    mi "We have so little time."
    if alt_day2_mi_date == 3:
        extend " I told you, you're bound to go."
        "My heart took an icy hand from the simple statement."
        th "She's right, isn't she!"
        "I'll just go away. And she'll never - never be there again. I'll wake up from her. That's it."
    mi "But I was happy."
    me "That's enough. Don't you dare talk like we've already broken up."
    mi "Don't talk about yourself in the past tense."
    mi "You've come to mean so much..."
    mi "I wish you could kiss me, but..."
    me "Miku..."
    "I pulled away from her and watched. Caught the stern, unsmiling gaze."
    "There was no stone left unturned from the fortress of my virtue."
    if not alt_day5_mi_7dl_voyeur and alt_hpt < 5:
        menu:
            "I closed my eyes":
                $ alt_spt += 1
                "If she wants it - let her. I don't feel sorry for her."
            "And I gave in to what I've wanted for so long":
                $ alt_day5_mi_7dl_kiss = True
                $ alt_hpt += 1
                "It's gravity. An object is attracted to the ground."
                "And lips to lips."
                "Three centimeters. Our breath was already mixing here."
                "And now, and..."
                "...?"
                "Her eyes grew huge."
                "Fear your desires, for they tend to come true."
                "I hugged her as I had never hugged her before."
                mi "Mmm..."
                "A few moments to understand."
                with flash
                "Just a moment more to burst with happiness."
                "That's not love. This is far worse."
                "The hands, frantically locked behind my back, relaxed."
                "And two narrow palms rested timidly between my shoulder blades."
    else:
        $ alt_hpt += 1
        "{i}Life mixed up in lies and indifference ends in indifference.{/i}"
        me "Miku, we're doing something wrong."
        "I exhaled."
        "And rolled to the side - just in time!"
        "{i}You fall asleep in an empty, dusty apartment, where the silence of loneliness has long and hopelessly settled under the shrouded vaults.{/i}"
        "{i}And that's it.{/i}"
        "{i}Drumroll.{/i}"
        "{i}Curtain falls.{/i}"
        "{i}The next time the world thinks of you is when the bailiffs come to evict you for non-payment, in five years.{/i}"
        "{i}You'll have dried out just in time to stop stinking. I mean, a dead body's got to look decent.{/i}"
    mt "Semyon! Semyon, where are you?"
    "A counselor's voice was heard."
    "Olga has an amazing talent for being in the wrong place at the wrong time!"
    stop music fadeout 4
    scene bg ext_polyana_night with dissolve
    "By the time I got up, Miku was long gone."
    me "Yes, Olga Dmitrievna, what did you want?"
    "I piped up."
    show mt normal pioneer with dissolve
    mt "Did you talk to Hatsune?"
    th "In a way..."
    "I nodded."
    mt "And what did she?"
    "I shrugged."
    me "She'll be thinking for a while, that's what."
    mt "Very good."
    with fade
    mt "Squads... Line up!"
    "She barked almost in my ear - with her 'lineup voice'!"
    "I stepped back, trying to shake the ringing out of my ears."
    show mt normal pioneer with dspr
    th "Shit!"
    "As I looked around, I was forced to state the obvious - I was left proudly alone."
    "After the hilarious scene we both found ourselves in, it was no surprise that she was somewhat shy."
    "Though it would seem that a stagehand shouldn't know any nonsense like shyness."
    "But it was from these kinds of grades that Mikuska escaped, first to a school for gifted children and then to the Soviet Union."
    "And so I fully respected her right to be a little embarrassed and to avoid the company of the actual object of embarrassment."
    "That happens, too."
    stop ambience
    stop sound_loop
    hide mt with dissolve
    play music music_7dl["melancholy_sun"] fadein 3
    play ambience ambience_forest_night fadein 0
    "I sighed and took my place in the rearguard of the column - in fact, I was leaving the clearing in the very last rows."
    "Only Boris Alexandrovich was later than me - he had already obtained somewhere a round conical bucket, in which water from the river was splashing."
    "Stomp. Stomp.."
    "The younger squad leaders were armed with super-strong flashlights, so there was decidedly nothing intimidating about the return trip."
    "And when I got a glimpse of the turquoise back of a head, I calmed down."
    "As calm as it is possible to be in such a situation."
    "For the first time I felt the full justice of the saying that the heart and the brain have different engines."
    "Why else would there be this discord in me?"
    "Why does one half of me want one thing and the other half wants the exact opposite?"
    "Why do I even care about things I never touched before?"
    scene bg ext_path2_night with dissolve
    play ambience ambience_forest_night fadein 6
    "I envied those kids, those pioneers."
    "I looked at the back of their heads and envied them."
    "They all have plenty of time ahead of them, plenty of roads."
    "And tomorrow they won't take half their breath out of them, they won't take it away to a land far away."
    "And no one deprives them of their sacred Pioneer right to a farewell disco and a dance with a girl they like."
    "If you ask another man, he'll spit that he doesn't need it."
    "But in fact {i}there{/i} will be everyone. Even Dvachevskaya, who doesn't give a damn about all these 'show-offs'."
    "Because once you close a shift, that's how you'll remember it."
    dreamgirl "Don't sulk, you sourpuss. {w}Maybe things will get better."
    th "In what way, I wonder?"
    scene bg ext_path_night
    with dissolve
    dreamgirl "Well, what way... Didn't you hear what Olga told you?"
    "I carefully recounted the terms of the deal."
    "Shrugged."
    th "I heard. What's next?"
    dreamgirl "And then, you jerk, there's a chance Miku will choose to..."
    th "Ah. Oh. Deeeefinitely in favor of degradation and stagnation."
    th "Hi, I'm Scanty Semen, I've been bringing myself to degradation for the last eight years! Join me and I'll show you how deep the rabbit hole really is!"
    th "We'll get to the bottom of it!"
    dreamgirl "Only two people know about this unsightly part of your biography."
    th "That's exactly two more people than I need."
    th "Besides, you're not even human."
    dreamgirl "Anyway, it's not too late to try to start over."
    if alt_day3_mi_7dl_donor == 0:
        dreamgirl "Olga will take you in for the first time, and then you can move on."
    th "Why would she let me stay with her? I'm an undocumented pioneer."
    dreamgirl "Think about it. Think it over."
    dreamgirl "But I'll probably agree with you completely on that point - if you want Miku to choose you over her stage career, you have to offer something worthy."
    dreamgirl "Really decent! Do you understand me?"
    th "Mm-hmm."
    play ambience ambience_camp_center_night
    scene bg ext_entrance_night_clear_7dl with dissolve
    dreamgirl "Going back to your previous life is out of the question."
    th "As if anyone would ask me."
    dreamgirl "Actually, they will."
    th "Yeah, yeah, keep babbling."
    dreamgirl "I mean it!"
    dreamgirl "It's up to you what happens to you: whether you stay here or not, how you live your life, and who you'll end up being."
    dreamgirl "So go for it."
    "I suddenly remembered that girl never approached me."
    th "Do you think it makes sense to tell Miku about her?"
    dreamgirl "Sure! Then she'll pick you for sure!"
    th "I see. Didn't even have to ask."
    "There was an enthusiastic shout from the front as the pioneers began to trickle into the camp grounds."
    "Everybody's tired, and I'm the most tired."
    th "I'll have to get cleaned up and go check on the girls."
    "I thought to myself, feeling my whole body ache."
    dreamgirl "Good idea."
    dreamgirl "You do that."
    "There was sarcasm in my pocket schizophrenic voice that went ununderstood."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_mi_7dl_goodnight:
    scene bg ext_house_of_mt_night_without_light with fade
    play ambience ambience_camp_center_night fadein 1
    play music music_list["a_promise_from_distant_days_v2"] fadein 2
    "Must have been the most eventful day I've had here."
    "Unless, of course, you count yesterday's crazy ride."
    "But we spent so much time together today."
    "It takes a great deal of wisdom and self-criticism to take a little distance from what's going on."
    "And to realize that this particular - yes, this particular! - day is what your memory, licked on all sides, would call 'happy memories.'"
    if alt_day5_mi_7dl_voyeur:
        "And perhaps we were the least bit quick to burn our bridges behind us."
        "Because nothing has really changed."
        th "Except that we stopped lying to ourselves?"
        th "I like her. She likes me."
        dreamgirl "What makes you think that?"
        th "Well... She ended up in the same bed with me... the same bale!"
        dreamgirl "What if she was just wondering what it was like to be with ugly Semyon?"
        th "Come on, you pest!"
    else:
        "It's like we're attracting trouble - we're always getting into these stupid situations."
        "How we got sent off the log, I ask you?"
        "Oh, and so... So..."
        "For a moment I saw that very, {i}calling{/i} look in the Japanese girl's eyes."
        "I must have really disappeared."
        "Because clearly and suddenly I knew what I was going to dream about tonight."
        "And the next couple of dozen nights, too."
        "On reflection, I couldn't find anything wrong with that."
    stop ambience fadeout 1
    scene bg int_house_of_mt_night2 with fade
    play ambience ambience_int_cabin_night fadein 1
    "The door opened without creaking - and still no one was inside."
    "It was nice to be under my own roof for a change, without feeling any guilt."
    "Except I was so sleeeeeepy..."
    "I yawned."
    th "Actually, I was planning to go wash up and stop by the girls' on the way."
    "Sluggishly I thought."
    th "Oh, my back's killing me with these potatoes."
    th "I should lie down to get some rest."
    "And with a blissful sigh, I sank into the arms of the boarding net."
    scene bg black with fade2
    "And off I went - like a switch was turned."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_7dl_wakeup:
    scene bg black with dspr
    play music music_7dl["lastlight_piano"] fadein 3
    "It is amazing how one's demands change as one goes off-balance to any extreme of the man-amoeba scale."
    "I must have managed to fall into that precarious state from which one might as well fly up as down to the bottom of the well."
    "And - lucky for me - I was dragged by the hair, kicked toward the light."
    "Now it seemed nightmarish and almost unbearable what I'd been living for the last few years."
    if loki:
        "Of course, I had an outlet in my work, but otherwise I was still the same unfit for life young man."
    else:
        "One thing is certain - I don't want Miku to see or know about what I've become."
    "It's possible - and it probably is - that it's all rather shaky, and that without an outside boost I'll soon lose all incentive to clench my teeth and keep on going."
    "But right now, as long as I have the strength, I'm going to at least start making changes."
    "Before you start cleaning up your house, you should clean up your head."
    scene bg int_house_of_mt_sunset
    with dissolve
    "And I opened my eyes."
    "The cabin was empty - the squad leader had made it a habit of coming in after I was asleep and leaving before I woke up."
    "That's how she missed me the day before yesterday, and that's how she did it yesterday, too."
    "If I hadn't been sure of the exact opposite, I would have decided that Olga Dmitrievna was embarrassed of me."
    "I even chuckled, imagining her embarrassed, standing at the door, listening to see if I fell asleep - and then running into the house at full speed, dropping her clothes on the way - and diving under the blanket!"
    with fade2
    "After savoring the resulting image for a while, I decided to go up after all - the day wouldn't start without me!"
    play sound sfx_open_dooor_campus_1
    pause(1)
    stop ambience
    scene bg ext_house_of_mt_sunset with dissolve
    "The counselor wasn't on the porch."
    scene
    $ renpy.show("bg ext_house_of_mt_day", what = Dawn("bg ext_house_of_mt_day"))
    with joff_l
    play ambience ambience_camp_center_evening fadein 0
    "She wasn't there either when I came back from the sinks in zombie mode."
    th "Looks like she's really busy, not just playing hide-and-seek with me."
    "I concluded."
    th "Which means..."
    dreamgirl "A few minutes to look for our kinsman-beauty?"
    th "Sort of. The autopilot function to search for one Japanese girl wasn't built in for some reason."
    "Sad."
    scene bg ext_house_of_un_day with dissolve
    play sound sfx_knock_door6_closed
    "Unfortunately, Miku's cabin was locked."
    th "Looks like she's already finished all her morning chores and is off to exercise."
    dreamgirl "Are you going to exercise?"
    th "What kind of question is that? Of course I will!"
    "Radical change, my ass."
    "I diligently pretended I wasn't lazy or sleepy or anything."
    stop music fadeout 5
    scene bg ext_square_sunset
    with dissolve
    play ambience ambience_camp_center_evening fadein 2
    play music music_list["everyday_theme"] fadein 5
    "The decision, of course, turned out to be a stupid one."
    "Miku may not be the sloppiest person in the world, but in the six days I've known her, not once - don't lose count - not once have I had the honor of seeing her on morning exercises."
    "Perhaps it has something to do with the regime exemptions and other blather for the High Guest."
    "Or, alternatively, it could have had something to do with the Japanese girl's lack of a tracksuit."
    "Again Slavya in her obscene uniform, counting the bars, again Sanich with his whistle, unobtrusively seated on the steps of the podium."
    sl "And - one, two, three, four - change hands!"
    show un normal sport at right with dissolve
    "Lena, by the way, was here - she was waving her limbs melancholy and looking sleepy."
    "When she stumbled into my gaze, she flinched and wanted to turn away, but I waved my arms, drawing attention to myself."
    show un surprise sport with dspr
    "Finally, I was honored with attention, and I began my act."
    "I gathered my hair into two ponytails and shook them, pretending to be pigtails - Lena touched her funny ponytails in bewilderment."
    "No, that's not it!"
    "I hissed my lips quickly - Lena shrugged and furtively rubbed her cheek on her T-shirt."
    "Apparently she thought I was telling her about some kind of dirt on her face."
    "Oh, man."
    "Raising my eyes in grief, I exhaled heavily."
    show un serious sport with dspr
    me "How hard it is to be clueless."
    "I was already being squinted at by the PE people around me, but I decided to give it a final try:"
    "Pressed the corners of my eyes with my fingers and moved them sideways, cosplaying the Chinese."
    "It was only now that Lena realized that I was asking her about her roommate."
    un "Miku?"
    "With only lips she asked."
    "I nodded with great enthusiasm."
    "Lena smiled somehow very vindictively:"
    show un evil_smile sport with dspr
    un "I have no idea."
    "She answered across the square. And tapped herself on the forehead with her finger."
    "Apparently, alluding to the 'goofy' one."
    "She turned away, ignoring me point-blank."
    hide un with dissolve
    "And it suddenly occurred to me that maybe Miku does have a uniform."
    "But she's the only one who thinks it's decent - something like three and a half scraps of cloth on two strings, barely covering what they're supposed to cover."
    th "It's quite possible that she wasn't sent to the eviction because of her chatter."
    "I guessed it."
    dreamgirl "Well, she's from Nihon. It's warm there, no flies to bite, and the girls are all in their panties."
    th "Nice argument, why don't you back it up with a source?"
    dreamgirl "My source is that it was revealed to me in a dream..."
    "My lewd alter ego answered cryptically."
    dreamgirl "And Miku is such an exhibitionist."
    th "I don't get it?!"
    dreamgirl "That's okay. You have a whole bunch of other virtues."
    play music music_list["my_daily_life"] fadein 3
    with fade2
    "After spinning, jumping, and other ways to get the blood flowing, the pioneers got out for a run."
    "But these are, understandably, the most enthusiastic - with Slavyana at the head."
    dreamgirl "However, if that's how all their runs go - it all makes sense!"
    "Commented the inner voice to Slavya, who in her short shorts was jogging lightly in front, and behind her, in a respectful distance were moving either fans or cheerleaders."
    "And what's so remarkable is that they were male."
    "And what they were staring at was also clear."
    dreamgirl "Or maybe they were, too? Eh? Sports are life!"
    dreamgirl "Sometimes even a new one!"
    th "Oh, calm down, you horny monster."
    "Especially since next to me out of nowhere..."
    scene black with guess_on
    mi "Guess who!"
    me "Electronik, of course, who else."
    "I answered calmly."
    mi "Uh..."
    scene bg ext_square_sunset
    show mi surprise pioneer
    with guess_off
    "With a grin, I turned around."
    me "Hello, princess!"
    mi "H-hello."
    "She squeezed out."
    mi "Listen, why Electronik?"
    me "Uh... Well..."
    me "Actually I wanted to say «Viola», but who knows how'd you react to that."
    show mi dontlike pioneer with dspr
    mi "You... You're laughing!"
    me "I'm sorry. I couldn't help it."
    "I said penitently."
    me "But I thought it was pretty funny - and you should have seen your face."
    show mt smile pioneer far at right with dissolve
    "The Japanese girl wanted to say something else, but Olga Leninovna appeared out of nowhere behind her:"
    mt "Pioneers! Liiiiine up!"
    "With a sergeant's growl she roared."
    hide mt with dissolve
    "And vanished."
    "And the poor girl was almost blown away."
    "I had to catch her by the arm and gently escort her to the place, where all our men were already lined up in uneven lines."
    show mi normal pioneer with dspr
    me "Where were you this morning, please tell me?"
    mi "Oh, you know, Senechka, I dreamt such an interesting song last night, and as soon as I woke up I ran to play it! Yes!"
    me "Didn't you dream of anything yesterday?"
    "The girl waved it off annoyingly:"
    mi "That's different! And anyway!"
    show mi upset pioneer with dspr
    mi "Such a great song! Do you want to hear it? And!.."
    "She was getting air in her chest - not caring where we were or what we were doing - but I was on my guard."
    "Instantly jumped up to her and covered her mouth with the palm of my hand."
    show mi dontlike pioneer with dspr
    mi "Mg-mu mumymimumy!"
    "Angrily she squealed into my palm."
    mi "Ugh! What are you doing?"
    sl "Shhhhhh!"
    "Slavya hissed."
    "She seemed to be the only one of the whole camp wondering what was going to be said on the lineup."
    me "Miku, after the lineup, okay? Don't sing now!"
    show mi shy pioneer with dspr
    mi "Oh... I'm sorry..."
    "Meanwhile, Olga had already climbed onto the podium and said hello from there:"
    mt "Squads! Lineup! {w}Atteeeention!"
    "We obediently pulled up, and the counselor again pulled her familiar bagpipes."
    "With enthusiasm she spoke from the podium about some plans for the day, about what the day meant..."
    "I wasn't listening to her."
    "Didn't listen to Miku either."
    scene cg d4_mi_lineup_7dl with dissolve
    "Though I was well aware that this might be the last lineup."
    "I heard a familiar name from the corner of my ear - I was worried."
    "But that was just Olga talking about how much our music director had done."
    "By the way, exactly how much was a mystery to me."
    "Still, I arrived rather late, and the time Miku and I spent around her, she wasn't much help in the social life of the camp."
    mt "Unfortunately, Miku won't be able to host tonight's farewell concert, since she has to leave a little earlier than the rest of us..."
    "Even though I was subconsciously expecting something of the sort - the news hit me like a heavy dust bag."
    "I slowly, extremely slowly shifted my gaze to Miku."
    "She oohed and hid behind Lena, who looked at me again like I was nothing."
    "I sighed."
    th "Thanks for at least informing me that way, what else is there to say..."
    with fade
    scene bg ext_dining_hall_near_sunset with dissolve
    play sound sfx_open_door_2
    pause(2)
    play music music_list["smooth_machine"] fadein 5
    scene bg int_dining_hall_people_sunset_7dl with dissolve
    play ambience ambience_dining_hall_full fadein 3
    "All through breakfast I was frowningly silent."
    "I sat at the very corner - so that I couldn't be approached."
    "With a sigh, the Japanese girl retreated to another table, where Lena was clucking alone."
    th "Good riddance."
    "After swallowing what appeared to be cardboard risotto porridge, I got up and walked away from the canteen, not paying attention to the gaze drilling my back."
    "Right between the shoulder blades."
    "If I'd been more impressionable, no other way, I would have really wanted to scratch myself."
    "Good thing I'm so thick-skinned. Yup."
    play sound sfx_open_dooor_campus_2
    pause(1)
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_dining_hall_near_day with dissolve
    "In exactly the same position of frozen balance, I hurled myself out of the canteen."
    "I wanted to go somewhere and have a little sulk."
    "For instance, this bench here is as good as any of the others - it's out of sight from the canteen's exit, and I won't be harassed here."
    "Miku has been very frank with me until now."
    "Of course, the thing is, she's a giggle-talker, her tongue is boneless, and she's a spy's best find."
    th "Why did I get so worked up then that she might happen to have secrets from me, too?"
    dreamgirl "If my memory serves me right, no one has ever signed a power of attorney for you, and no one has ever sworn a similar oath of love to the grave."
    th "Oh, yes! I'm instantly relieved. Thank you."
    dreamgirl "Really?"
    th "No!"
    dreamgirl "To be beautiful is to appear not to be who you really are."
    th "You mean that once you're an artist, you're an artist forever?"
    dreamgirl "You see right through it. She was honest with you for a while, but that time is over."
    th "Did I cause her to distrust me?"
    dreamgirl "More like the opposite. You've caused too much of it. {w}Dangerously close - and only a complete suicidal man tells his loved ones decisively everything he thinks."
    th "I'm about to cry."
    dreamgirl "Your sarcasm is misplaced. {w}You were just being taken care of..."
    th "Yeah. To put you in front of the fact - to poke your face in the wall, so to speak."
    dreamgirl "It's more merciful than making you worry while you wait. {w}If Olga hadn't blabbed on the lineup, you'd have had a happy farewell day in the company of your beloved Japanese girl."
    "I didn't agree with that and even shook my head, but then the sun's rays were blocked by someone's silhouette, and I slowly raised my head."
    "I guess I had a big delusion about the «won't be harassed» part."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_7dl_soul:
    scene bg ext_dining_hall_near_day with dspr
    play music music_7dl["will_you"] fadein 3
    "It always seems to me to be a huge mistake when someone is pleased with me."
    "I am in this world as if I were a spy who lives with the idea that sooner or later I will be exposed and rejected."
    "And yet Electronik who stood up against the sun was pleased with me without a backward thought or any advantage."
    show el normal pioneer with dspr
    el "Hello!"
    "I didn't remember seeing him this morning or at breakfast, so I politely said hello back."
    el "I hope you haven't developed any sudden attachments?"
    "He asked, playing with a crowbar that came out of nowhere."
    th "I don't get it."
    "I moved cautiously away, but he took a step towards me."
    me "What are you hinting at?"
    "I don't think he's going to offer himself up as that very attachment, of course, but it sounds kind of weird."
    show el smile pioneer with dspr
    el "It's just that everyone I saw today was only concerned with one thing: how they could spend more time with their favorites."
    "He snorted and twitched his shoulder:"
    el "As if there's any time to do anything now, three weeks of pulling the cat by the balls - now they've ripened."
    el "And you, as I see, are sitting still, not running anywhere."
    me "Yeah. And?"
    "The presence of the heavy iron in his hand was still keeping me on my toes."
    el "I need a partner for a case."
    me "What's that?"
    show el grin pioneer with dspr
    el "Don't worry, nothing criminal: I need to get something from Alexei Maksimovich, and I'm afraid I can't carry everything myself."
    me "Eh..."
    show el normal pioneer with dspr
    el "Will you help me?"
    th "I should say: let Schwarzenegger carry for you. Really?"
    "But somehow, in the six days I've been here, Electronik has given me no reason to think ill of him at all."
    "I, by coincidence, needed to shake the junk out of my head: the perfect thing to do in the background while I was torturing my back and arms."
    "So I stood up and nodded accordingly."
    scene bg ext_admins_day_7dl with dissolve
    "When we reached the administration building, there was no one there - the doors were closed, the hinges were locked, only the loudspeakers from under the roofs were cheerfully broadcasting a kind of semi-recognizable song."
    "Yes, there was a note under the glass window on the door."
    me "Gone fishing. A. M."
    "I read it."
    me "Now what?"
    show el normal pioneer with dissolve
    el "It's okay. I told you I had a deal."
    play sound sfx_keys_rattle fadein 0
    "He planted a bundle of keys in the palm of his hand that would have put Slavya's artifact to shame, too."
    el "Actually, the idea was second squad's, but I volunteered to help out, so..."
    if alt_day1_sl_keys_took != 1:
        me "Did you steal that from Slavya by any chance?"
        show el upset pioneer with dspr
        el "What? No! {w}They gave it to me, I told you."
        me "Ah. I see."
        "Then again, I had no reason not to trust him - but he smiled slyly!"
        me "Open up then."
    else:
        me "When you take it in stride, eh?"
        show el smile pioneer with dspr
        el "Right!"
    play sound sfx_unlock_door_campus fadein 1
    pause(1)
    scene bg int_admins_7dl with dissolve
    play sound sfx_unlock_door_campus fadein 1
    pause(1)
    scene bg int_chief_office_day_7dl with dissolve
    play ambience ambience_int_cabin_day fadein 3
    "And we found ourselves in the holy of holies."
    "A big table, two chairs, a speakerphone - and cabinets, cabinets!"
    "I had no rough idea what riches lay behind those doors, but that they were untold is an objective fact!"
    "However, I was not allowed to take an inventory with partial privatization:"
    show el normal pioneer with dspr
    el "Here are two boxes, take either one."
    me "And you?"
    show el laugh pioneer with dspr
    el "And I'll take the second one, obviously!"
    "He laughed."
    el "Or you can take the crowbar from me and I'll take the boxes - it'll weigh about the same."
    "After imagining myself stumbling over something unnoticed and flying nose first, I shook my head negatively and clawed at the edged weapon."
    el "For some reason that's what I thought."
    "Calmly nodded the guy."
    scene bg ext_admins_day_7dl with joff_l
    play ambience ambience_forest_day fadein 1
    show el normal pioneer with dspr
    el "I went up this morning on an errand, and then I saw Lena sneaking off somewhere."
    "Electronik came out of the room, slammed the door behind him, and with the look of an extremely busy man went somewhere in the direction of the second gate."
    el "Still looking so... thieving. {w}I thought maybe she was up to no good, so I shouted at her."
    el "You don't know anything?"
    th "Shit. That's a fantastic logic."
    me "You're the one who shouted at her, remember?"
    show el upset pioneer with dspr
    el "But you're hanging out with her roommate - I thought maybe you knew something."
    me "No, nothing like that."
    el "Yeah? Shame. {w}Never mind then."
    el "She was carrying her shoes as she walked, and when I shouted at her, she said something to herself, put her shoes on, and walked back."
    el "I've heard she sometimes runs away from camp, maybe she wanted to now?"
    "I exhaled and counted to ten."
    me "You explain to me why the hell are you bothering me with Lena? I'm not her mother."
    show el serious pioneer with dspr
    el "But you're friends with her roommate."
    me "With her roommate!" with vpunch
    extend " Not with Lena."
    "I grumbled, cooling down."
    me "Actually, where are you taking me?"
    show el normal pioneer with dspr
    el "We should be expected."
    me "Second squad?"
    "Instead of answering, Electronik turned down a barely visible path and a few minutes later led me to the exit of the camp."
    scene bg ext_backdoor_day_7dl with dissolve
    "The kids from the second squad were already crowding in here."
    el "Is everyone here?"
    "They assured us, at random, that yes, everyone is here."
    el "Keep in mind, permission to go outside the area is only for me and the group that's with me."
    el "If anyone tries to run, they'll be in big trouble."
    "The kids nodded understandingly - no trouble, no one plans to split off."
    el "Then let's move out."
    stop music fadeout 5
    with fade
    pause(2)
    scene bg ext_old_building_day_7dl with dissolve
    play ambience ambience_forest_day fadein 3
    play music music_7dl["summer_ends_soon2"] fadein 3
    "Maybe if I'd been here in the evening or at night, I'd have shunned every bush, every sinister shadow that fell on the path."
    "But the fact is, it was daytime, there were comrades around, and the mood was most spiteful."
    "If you gnaw yourself long enough, sooner or later you reach a limit after which the pain is no longer frightening."
    "And nothing else is frightening."
    "And the kids walked in pairs like we did yesterday at the bonfire, holding hands and singing chants about the one who walks amicably in a row."
    "And it seemed sometimes that happiness and left just in those short pants, from which you successfully grew up, and they - here, just caught up: thirteen or fourteen years, when the words 'friendship' and 'mutual assistance' mean something."
    with fade
    "Anyway, an hour later we arrived at a clearing in the middle of which there was what looked like an entire building of shingles and brick."
    "But while the first floor was sturdy enough to look about ten years old, the second floor had gaping holes in the walls, the roof was sagging and sagging in some places, and the exterior stairs were twisted like rusty springs from a wind-up toy."
    "Faithful suitors to the half-decayed giant were what was once called a playground - several articulated carousels, paired swings, canopies with ping-pong tables..."
    "On the other side you could discern a concrete gutter and the remains of a water column - there was the equivalent of our hand-washing sink."
    me "A boarding house for three and a half kindergarteners?"
    "I inquired."
    "Electronik shrugged his shoulders:"
    show el normal pioneer with dspr
    el "Personally, my father told me that they lived here in tents, and the big house had a toy library and an archive."
    el "Though I can hardly imagine living in a tent for an entire summer."
    "Here I agreed with him."
    "After all, a number of my health problems began with a single night on the pavement - in May, by the way! It was twenty-five degrees outside!"
    "And it's a whole summer here."
    with fade
    me "Okay, now can someone explain why we came here?"
    show el smile pioneer with dspr
    el "I don't know if you know this, but this is where our camp was from the beginning, it was later that we moved."
    el "Don't ask me why, but there's been a tradition since the inception of «Sovyonok» in 1947."
    el "It got a little put off because of the move, but now it's back the way it should be."
    me "What kind of tradition?"
    show el normal pioneer with dspr
    el "Time capsules."
    me "What do you mean?"
    el "Every five years the pioneers lay a message in a conspicuous place for the future to be opened in fifty years."
    el "The first capsule was laid in '47, so eight years from now you can open it."
    me "But then what are we doing here?"
    "I inquired, doing a little calculation in my head."
    me "Shouldn't a new capsule have been laid in eighty-seven?"
    el "I told you, the schedule was off because of the move, so we started counting again from the seventy-fourth."
    el "And today we're laying capsule number three."
    me "And what is this capsule supposed to look like?"
    el "The first two used a shell casing from some large caliber cannon."
    el "I got one, too!"
    "Putting the box on the ground, El pulled out a huge green casing with a distinct gunpowder residue."
    el "This is where we should put all the interesting stuff we've accumulated over five years, then we'll fill it with paraffin and hide it."
    me "Hide it where?"
    show el smile pioneer with dspr
    el "It's the same place as the last two."
    "He brushed it off."
    el "Under the concrete slab - you didn't drag the crowbar for nothing, didn't you?"
    "He nodded at the miraculously preserved concrete walkway leading from the main building to an area clearly reserved for a mess hall - the kind of soldier's mess, with only a canvas awning overhead and hot porridge in a plate."
    "All that's left of the awning now are the sagging poles."
    el "Do you know how they fed people here? The field kitchen used to come! {w}Real... Like in the army."
    "He stretched out with envy."
    me "What are your years, when you go to the army, you'll have time to eat."
    show el laugh pioneer with dspr
    el "You know how to comfort!"
    "In the meantime, some sort of argument had begun over the boxes - apparently they contained notes, diaries, and photographs accumulated over the past five years   - from those that were not filed in the camp scrapbook."
    "There's no way they could have fit in there."
    "So it's only fair that some wanted one thing and others another, Electronik instantly walked up to them and spoke in a low voice about something."
    hide el with moveoutright
    "I, on the other hand, walked to the edge of the clearing and studied my surroundings thoughtfully."
    "It smelled of time, of memory, and of someone's secrets."
    "Perhaps there are not only official capsules buried here, but also greetings from the past from ordinary pioneers."
    "I know by experience - several times I buried a piece of paper with a button and a cross, so that one day I could come back and remember myself - a young, young man."
    "And if the parents of the pioneers here had gone here once before, they might well have left their greetings."
    "Although most of them probably went just to the tent city around this crumbling giant, rather than to the barrel houses - after all, very little time had passed since the move."
    scene
    $ renpy.show("bg ext_old_building_day_7dl", what = Dawn("bg ext_old_building_day_7dl"))
    with dissolve
    "As I'd expected, the canopy supports were shredded and nametagged, and everyone was trying to leave their mark."
    th "The trees around here must have been cut up pretty good, too."
    "I thought to myself, and then they called to me:"
    el "Semyon, come help!"
    show el normal pioneer with dissolve
    "Electronik beckoned me out of the crowd of guys, discussing something very animatedly."
    "The strict jury seemed to have sorted out who needed what more - a few obviously disgruntled faces were relegated to the background, along with the box where the discarded materials had gone."
    "The rest crowded around Electronik, holding a plastic bag."
    el "Everything won't fit, so we leave only the opening and closing shifts and maybe something really, really interesting!"
    "Fifteen cheers from the closing shift."
    "Fifteen cheers from the opening."
    "And some pictures."
    "Not too many, really."
    "Unless you're trying to fit everything into a little steel cylinder."
    "Apparently, there was a fierce debate about the photos - Sanich turned out to be quite a prolific photographer, and choosing what to keep and what to seal was sometimes really hard."
    "That's why I withdrew myself."
    "And now I saw familiar, half-familiar, and total strangers's faces - smiling, frowning, happy, sad..."
    scene anim prolog_2 with fade2
    "I saw Slavya three years younger than myself - surprisingly similar to the current Ulyanka. {w}Not outwardly, no, but by some expression in her eyes."
    "Saw Olga - for some reason my heart prickled - holding hands with some murky type, looking sullenly into the frame."
    "Lena..."
    "Alisa..."
    "The events of the years that I missed, appearing only at the very curtain."
    with fade
    "And I was curious as if peeping through a keyhole."
    "Moments stolen from the flow of time, captured on paper-a year ago, two, three..."
    "Lena from three years ago - no ponytails, long-long, almost Miku-like hair."
    "Alisa is a brunette!"
    "Olga Dmitrievna in capri pants and a T-shirt with an inscription «Sovyonok-40»."
    "These are just the ones I know - and there were many more."
    with fade2
    "Finally, the current year."
    "And the first shot is Miku!"
    "I couldn't hold back a chuckle when I saw the way Electronik twitched, putting her aside for the culling."
    "The shot turned out to be really chic, with Miku standing in the open doorway in a dress of her usual length."
    "That is, about a couple of centimeters longer than her usual t-shirt. To cover her butt."
    "The pioneers, frozen, turned their heads to her."
    "The blushing anger - you could see even in the black-and-white photo how red she was - of Olga heading toward the intruder."
    with fade2
    "Following him are Shurik and Electronik, assembling some tricky mechanism in their clubhouse."
    with fade
    "Lena completing a huge musical-themed panel - I wonder where it is now?"
    with dissolve2
    "Dvachevskaya is on the swing. I mean it!"
    "Laughing, eyes closed - behind her back Ulyanka, pushing her friend in the back."
    with fade2
    "Slavya, straightened up at the piano and playing some kind of melody - it was obvious that she didn't just sit down, she knows where to put her hands and feet, how to hold her wrist..."
    "How much I simply do not know about those around me..."
    "How much I simply don't care about."
    el "Oh, here's more, from the year before last!"
    "He pulled some hard black and white pictures out of a box."
    el "Our bus broke down, so we had to go the old-fashioned way our parents used to go."
    el "Several Ural trucks with a tent body and benches were called from the military unit, and they loaded us there..."
    "Electronik showed me the first picture, taken obviously from the depths of such a body - benches going to the edge, piled with kids with suitcases of all stripes."
    "{i}All happy, laughing - adrenaline you don't get riding in a comfortable bus!{/i}"
    el "Boris Alexandrovich told me that in the past they took a ZIS three-ton truck, one truck per squad, and nothing, nobody died."
    "{i}The second picture is of the road running away into the distance, the wind tearing the tarpaulin overhead, and from the car behind the operator, from the cab, the driver is waving - very young, smiling at the age of thirty-two.{/i}"
    me "So they were shaking like soldiers in the cars so they could sleep on the ground all summer."
    show el smile pioneer with dspr
    el "Do you think they're crazy, too?"
    "{i}The last picture - taken along the side forward - there was a banner fixed over the cockpit, with tassels, with the pointed tip of the staff burning hotly in the sun.{/i}"
    "The banner must have been scarlet, the tassels and the staff golden. That's the way it usually was."
    "There was also an inscription on the flag, which I read with some difficulty, but nevertheless: 'To fight for the cause of the Genda always ready!"
    el "I guess that's it."
    "With a hint the cyberneticist said, and I returned the pictures to him."
    scene bg ext_old_building_day_7dl with dissolve
    "Electronik put all the selected notes, pictures, and badges into a bag, ironed it, kicking the air out - and nodded."
    "The curly-haired pioneer from the second squad immediately pulled out some kind of iron and swiped the edge of the bag with a light."
    "Looks like it's not the first time he's done that."
    "Electronik nodded gratefully, folded the bag in half, twisted the resulting tube properly, tucking it in tightly."
    "Tucked it into the shell and swatted an already heated paraffin plaque on top."
    el "Let's go tuck it in."
    "He took me almost to the hull itself, where an old carousel and a bush of bird cherry served as landmarks."
    el "See the slab lying a little uneven?"
    "I nodded."
    el "Pull that one up."
    "And so I did!"
    "After panting and sweating, earning myself a few calluses and a trampled foot (I accidentally stepped on it myself), I pushed the slab aside."
    "Electronik didn't lie! In a notch in the dry ground nearby lay two capsules, twins of the one we were going to lay next to them."
    "The pioneers crowded around me - everyone wanted to participate in the capsule-laying ritual."
    th "Strange that no one wanted to participate in the crowbar ritual."
    "Nevertheless, five more minutes and the concrete slab was in place, with the weight of three casings already on top of it."
    "The pioneers hummed contentedly and, dismantling the boxes, lined up in pairs for the return trip."
    "Whatever Al planned to become-he should have tried his hand at pedagogy anyway!"
    el "For lunch at camp... march!"
    "He commanded."
    "And the pioneers set off amicably down the path."
    "After waiting a bit and letting them pass me, I caught him under the elbow:"
    show el normal pioneer with dspr
    me "Listen, I saw you discarded some pictures with Miku there."
    el "Yeah, and?"
    me "I'll take them, can I?"
    "The guy laughed and nodded."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_7dl_star:
    scene bg ext_dining_hall_near_day with dspr
    play ambience ambience_camp_center_day fadein 3
    show mt normal pioneer with dspr
    show anim_grain
    play music music_7dl["lazy_olga"] fadein 3
    mt "Feeling bored, Syomich?"
    th "Yes. And now you will self-depart, and I will continue to bore myself further. May I?"
    show mt smile pioneer with dspr
    mt "What a sour face."
    "The squad leader laughed."
    mt "Don't be afraid, I won't make you work, since you don't like it so much."
    "I was embarrassed, but courageously remained silent."
    mt "In fact, I need you to find Dvachevskaya and take the instrument from her - the guitar is needed by the boys from the third squad, and they themselves are afraid to go near Alisa."
    me "So let's throw me to her so she eats me?"
    show mt laugh pioneer with dspr
    mt "As if you can be eaten."
    show mt normal pioneer with dspr
    mt "Anyway, when you pick up the guitar, take it to your sweetheart - she knows who to give it to. Is that clear?"
    me "Uh..."
    "She clapped me on the shoulder."
    mt "Then get to it!"
    with fade
    pause(1)
    scene bg ext_houses_day with dissolve
    "That's the way it is - the minute you find a comfortable place to rest, the next thing you know, there's a lot to do."
    "And Miku's been a pain in the ass with her secrets."
    "Brrr!"
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_house_of_dv_day
    show anim_grain
    with dissolve
    play sound sfx_knock_door6_closed
    pause(1)
    "Dvachevskaya wasn't home."
    th "And why am I not surprised?"
    scene bg ext_houses_day
    show anim_grain
    with dissolve2
    "Back on the main makeshift street, I wondered where the redhead might be headed."
    "For some reason it didn't occur to me to ditch the task."
    "The whole point was that I was an extremely lazy person - I preferred to do the job at once so as not to procrastinate, and on my conscience so as not to redo it fifty times at a time."
    "Anyway, now I was wandering along the concrete path, kicking the pine cones that fell under my feet, melancholy about what to do with the rest of the day."
    "The most logical thing would have been to track down the cyan princess, make up, mope around with her, and do all sorts of wooing."
    "But I'm offended today. Here."
    stop music fadeout 3
    scene bg ext_house_of_el_day_7dl
    show anim_grain
    with fade
    "I got so caught up in getting into the role of the offended that I almost lost sight of one extremely familiar and extremely annoying factor."
    "Smell."
    "I should know the origin of that smell; after all, it's all over the walls and ceiling of my house."
    me "Tobacco?"
    "I grumbled incredulously."
    "I was lucky - a moment later, a faint breeze blew in from the river and blew the cloud of scent somewhere behind the pines."
    "But I was standing where there shouldn't be any cigarettes."
    "This was where the little kids lived - the last cabin down the street - and several of the cabins were closed, partly because of repairs, partly because of incomplete squads."
    "And there was one cabin, standing somewhat out of the way, that smelled familiar!"
    play sound sfx_knock_door6_closed
    pause(1)
    "I climbed sharply up the steps and pushed the door open."
    "In vain."
    "Though I could have sworn it smelled from here!"
    th "Or did it?"
    "As I stepped down the steps from the porch, I looked thoughtfully around the house."
    th "Is it possible that someone could have locked themselves in there from inside?"
    "Unlikely, of course, but..."
    play sound sfx_unlock_door_campus
    pause(1)
    "At that time the lock clicked, and on the doorstep there appeared..."
    play music music_7dl["breath_me"] fadein 3
    show un normal pioneer with dspr
    un "Yes…"
    show un shy pioneer
    extend " oh."
    "After the scathing reprimand at the exercises, I didn't have much faith in Lena's embarrassment, so I cheerfully inquired:"
    me "You're the one smoking or something?"
    show un scared pioneer with dspr
    un "Nnnnn..."
    dv "Hey, what the fuck are you doing at the door..."
    "Alisa looked out of the cabin at the light."
    dv "Oh, rookie! Come on in, now that you're here."
    "She jumped down in a few steps, went behind my back, and with the inevitability of an asphalt road roller pushed me - and after me, Lena - into the cabin."
    scene bg int_extra_house_day_7dl
    show anim_grain
    with dissolve
    play ambience ambience_int_cabin_evening fadein 2
    play sound sfx_close_door_1
    dv "Look out, the doors are closing! Next station is the morgue!"
    "She slammed the door so that the windows shook."
    "Took the cigarette smoking there from the doorway and took a hearty drag."
    "And only then did she remember her duty as a welcoming hostess."
    show dv normal pioneer with dspr
    dv "The hell are you doing here?"
    "She asked politely."
    me "Me? Well... It's..."
    us "What is it?"
    "Ulyana showed her head from the opened closet."
    dv "Our fool has come for the guitar."
    me "I'm not stupi... Hey, how do you know about the guitar?!"
    "Dvachevskaya rolled her eyes."
    dv "Mikuska, come out, the racket is over."
    "A long ponytail of blue-green hair appeared from under the bed first."
    "Miku, pretty dusted, showed herself much later."
    "By this time Ulyana was already back at the table, where cards were scattered in disarray, and a four-section ruled sheet yellowed as a tin ashtray."
    dreamgirl "Do we seem to be in for a cultural evening?"
    "There was everything you could be thrown out of the territory for - all that was missing was gore and unbridled sexual practices of varying degrees of dubiousness."
    "Though it wasn't evening yet, of course."
    "But cigarettes, cards, and a bottle of port were present."
    "The port, by the way, was unopened, so they were saving it for tonight-it makes sense, in general."
    "It occurred to me that if I wanted to turn them all in, no one would stop me."
    "But since they dragged me in here and didn't chase me away, it means they either know something about me that I don't know myself, or..."
    with fade2
    "They want to make me an accomplice."
    dv "Mikuska, hand out, it's your turn."
    "The Japanese girl nodded obediently and shuffled the deck with a professional motion."
    th "Wow! I hadn't heard of her talents!"
    dv "We'll go get the balalaika later, okay?"
    me "But Olga Dmitrevna told me..."
    show dv angry pioneer with dspr
    dv "I don't care what she told you! Do you think she's running around camp right now doing business? Ha!"
    "She took another puff and handed me a smoking cigarette, which I took in without a second thought."
    "The filter was clean and dry, no one fed me lipstick, for which they had a special human mercy."
    dv "She's buzzing now with Alkosanich and Viola - they have Mexican vodka in a square bottle, I saw it myself!"
    me "And why today?"
    show us normal pioneer at left with dspr
    us "That's because Alexei Maximovich won't be here until lunchtime."
    "Slavya turned away from the table - she wrinkled slightly as the clouds of smoke reached her face, but stoically endured."
    show dv normal pioneer with dspr
    dv "The big bosses are absent - went fishing until lunch, and in the afternoon will go into town to make arrangements for the buses. {w}You go ahead and don't procrastinate, rephased - pass it around!"
    "I obediently did as she commanded."
    "I took a closer look at the brand of the cigarette — «Magna». Damn, that's my youth!"
    "I grinned and, taking a proper drag, handed it to Lena."
    "It occurred to me that their trust was somehow inexplicably unconditional, and bought at a minimal cost: I just didn't reject anything."
    show un normal pioneer at right with dissolve
    un "Dvachevskaya got the tea."
    "Lena grimaced, exhaling smoke."
    me "I didn't know you smoked."
    show un grin pioneer with dspr
    un "You're really... Observant."
    us "I'll pass. Don't give it to Miku either."
    show mi angry pioneer at fleft
    mi "What do you mean, don't let me?! Am I the smallest one that you all smoke and I'm not allowed?"
    show us smile pioneer with dspr
    us "I don't smoke!"
    show mi dontlike pioneer with dspr
    mi "You don't count!"
    me "Why don't you save your voice?"
    mi "Shut up!"
    "She walked over to Lena and took the cigarette away from her."
    "Took a deep, deep puff..."
    hide mi
    show us smile pioneer
    show dv laugh pioneer
    show un laugh pioneer
    with dissolve
    "And she coughed a wheezing cough, her face red, tears in her eyes."
    "She seemed to regret her decision to show herself as an adult, once the smoke got into her mouth."
    "No wonder - the mucous membranes have to get a little coarser so they don't sting so much from the nicotine and tar."
    "So you have to get used to the poison."
    "Though I have to admit - she looked extremely sexy with a cigarette. A Mata Hari of the Japanese variety - a forty... more like thirty-eight megatons' worth of bombs."
    "Alisa immediately jumped up to her, enthusiastically pounding the poor Japanese girl on the back."
    show un normal pioneer with dspr
    dv "Hehey! Welcome to the brotherhood of sinners!"
    mi "W-what a disgusting..."
    "Squeezed out Miku."
    show dv normal pioneer
    show us normal pioneer
    with dissolve
    dv "You're doing it wrong!"
    "The redhead explained serenely:"
    dv "You have to inhale the smoke, and while you're inhaling, say 'pharmacy' - then you'll get high."
    show mi upset pioneer at fleft
    mi "I don't think I really want to get 'high.'"
    "Said Miku doubtfully."
    show dv grin pioneer with dspr
    dv "Then return the tobacco to the motherland, no need to waste someone else's nicotine!"
    "She took the cigarette out of Miku's hand."
    dv "You and Ulyanka will be two teetotalers."
    show us smile pioneer with dspr
    us "Hey, what's the joke? I'm just a kid!"
    show dv surprise pioneer with dspr
    dv "Really?"
    "Alisa was surprised so genuinely that I knew she was mocking me."
    show dv normal pioneer with dspr
    "Ulyana only showed her tongue and went back to the game."
    "The cigarette went back to me, from me to Lena."
    "I suddenly remembered the indirect kisses."
    "Now Dvachevskaya is kissing me, like Leonid Ilyich, with her tongue!"
    "And here I am kissing Lenochka - mmm, as they say, kissing a smoking girl is like licking an ashtray!"
    "And that's the touching triumvirate of lickers we have."
    "And Miku looks at it and is not at all jealous."
    with flash_red
    with vpunch
    "Ouch!"
    "I was wrong, I take it back."
    show mi grin pioneer with dspr
    mi "Senechka, if you want a kiss from me, you'll have to brush your teeth!"
    me "What, you're really going to kiss me?!"
    show mi shy pioneer with dspr
    mi "On the cheek?"
    me "Pfft. I'm not brushing my teeth for a cheek."
    show mi angry pioneer with dspr
    mi "Senka, don't be mean! I'm already leaving, all upset, and now you're pissing me off!"
    "With a grin, I handed my cigarette to Lena and got up."
    me "So what's with the balalaika, Alisa?"
    show dv normal pioneer with dspr
    dv "I'll give it to Slavka in the afternoon. She'll take where it's needed."
    me "Alright."
    dv "That's good. Then let's go to the table, the fifth player will be very helpful!"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_7dl_human:
    scene bg ext_dining_hall_near_day with dspr
    play music music_7dl["rewind"] fadein 0
    show us normal pioneer with flash
    us "XD!"
    me "Kid, what do you want?"
    us "I've got something to do. Let's go!"
    "Ulyana held out her hand to me."
    with fade
    "Which I successfully ignored."
    me "With you? Not a chance."
    show us calml pioneer with dspr
    us "Hey, that's a prejudiced attitude you have toward me!"
    me "What do you mean?"
    us "In the sense that if Mikuska called you, you'd go without a second thought."
    me "You compared too."
    show us dontlike pioneer with dspr
    us "There! See!"
    "She bounced back and poked her finger at me:"
    us "Am I worse than Miku?"
    th "Frankly, yes."
    me "You didn't seem to care about that question before."
    show us smile pioneer with dspr
    "Smelling the weakness, the little one instantly cheered up:"
    us "People change!"
    "Those clearly weren't her words. And we both felt it."
    show us shy pioneer with dspr
    us "I mean, we're going home tomorrow - and I never got to walk with you!"
    th "It hurts to have to."
    me "And what's different about you today, human?"
    dreamgirl "As if it's unclear what."
    "I guessed it myself, but I was curious to test the little girl's sincerity."
    show us surp1 pioneer with dspr
    us "You go everywhere with Mikuska, I even thought -"
    "She lowered her voice to a whisper:"
    us "You fell in looveee with her!"
    show us laugh pioneer with dspr
    us "What a laugh! Syomka and Mikuska!"
    me "Tell me about it."
    "I grumbled. {w}My hunch has been strengthened."
    us "Imagine, you're such a boulder, and she's two notches taller than a pot!"
    me "She's taller than you, actually."
    "I pointed it out."
    us "She's not. We're the same height."
    me "Liar!"
    show us surp2 pioneer with dspr
    us "WHAT! {w}I never lie!"
    us "I'm one hundred and fifty centimeters tall."
    "I don't think she had any reason to lie about such little things, and after comparing by eye the difference in our height, I was inclined to agree."
    "Apparently, up to this time I had been fooled by her proportions, which always made Ulyanka appear to be about the height of a second or third-grade pioneer."
    "A perpetual favorite in the nursery chair in a cambric bib."
    "That is, the child of the regiment!"
    dreamgirl "In a camouflage infant high chair wearing a kevlar bib."
    "I snickered as I imagined that picture."
    me "Okay, I admit it: I was wrong, you're big and smart and very mature. {w}What do you want from me?"
    show us grin pioneer with dspr
    us "Finally asked. And what I need from you is for you to help me!"
    "She grabbed my arm and dragged me along."
    us "Hurry up!"
    me "I've got a bad feeling about this."
    "I muttered."
    stop music fadeout 3
    scene bg ext_boathouse_day with fade
    play ambience ambience_boat_station_day fadein 2
    "And I wasn't wrong about that, not one bit."
    "I mean, the idea of getting out to the water to sit there and chat is not a bad idea in itself, of course!"
    "But Ulyana wouldn't be herself, confining herself to sitting by the water."
    "Oh no."
    play music music_7dl["anglegrinder"] fadein 3
    scene bg ext_boathouse_day:
        zoom 1.05
        linear 2 zoom 1.0
    show us normal pioneer
    with fade
    us "I want you to surprise me."
    me "You decide what you want. {w}It's either to help you, or to surprise you."
    "I grumbled."
    us "One doesn't preclude the other."
    "She cut it off."
    show us smile pioneer with dspr
    us "I invite you to…"
    with fade
    extend " a romantic boat ride!"
    th "Only over my dead body."
    me "And you've already arranged everything, of course."
    show us laugh2 pioneer with dspr
    us "Are you stupid or something? {w}What's the interest in all this, then?"
    me "Not getting paddled in the spine by the watchman?"
    "I couldn't take it at last."
    "So far I've managed to smooth things over, to find the words..."
    "But this «wondrous child» is capable of pissing off even a saint!"
    show us upset pioneer with dspr
    us "Syomka, you're a bore and a pest!"
    "The «wondrous child» was upset."
    us "I want it to be like an adventure, you know? I want it to be interesting!"
    if alt_day3_mi_7dl_donor:
        dreamgirl "Doesn't it remind you of anything?"
        th "Love for the rituals... {w}Going shopping with Miku?"
        dreamgirl "Good for you, take a pie off the shelf."
    "Indeed - it did look more curious from this angle."
    "It's no fun to just go for a walk - you have to make sure you run away without anyone seeing."
    "And on the way be sure not to step on shadows from branches and cracks in the asphalt!"
    "Or don't talk!"
    me "It will be very interesting when we get caught..."
    show us sad pioneer with dspr
    us "So you won't?"
    "And how much her behavior reminded me of Miku!"
    "Which meant that my good attitude toward the unfortunate hafu was now automatically extended to the little one as well."
    me "Why won't I..."
    "I mumbled uncertainly."
    me "I didn't say that..."
    show us surp1 pioneer with dspr
    us "Hooorrraaaaay!"
    "She screamed."
    me "Hush you!"
    "I hissed, slamming her scream with my palm."
    us "Oh... yeah. Anyway, listen."
    "She started laying out her plan."
    "The perfect plan."
    "Wonderful, I'd even say."
    me "Okay, I got it."
    me "I'll be like James Bond, pick the locks, sneak in and steal the boat."
    show us surp2 pioneer with dspr
    us "Yes!"
    "Ulyanka confirmed enthusiastically."
    "If it weren't for one hitch..."
    me "In that case, what are you going to do yourself, let me ask you?"
    show us calml pioneer with dspr
    us "What do you mean?!"
    me "Literally! {w}Get me a boat and oars and distract the guards."
    show us surp3 pioneer with dspr
    us "Oh. {w}You have to have oars, too."
    me "No, we'll row with your panama."
    show us laugh2 pioneer with dspr
    us "I don't have a panama!"
    me "That's exactly what I meant."
    me "Were you just going for a ride?"
    show us smile pioneer with dspr
    us "Stuttering like an old fart."
    "Ulyanka poked me in the shoulder with her fist."
    us "Don't whine, Grandpa, I got it."
    us "If you need an oar that much, I know where to get one."
    us "You steal the boat, and I'll be right back."
    hide us with dissolve
    "The kid disappeared, and I, for lack of alternatives, have decided to try my hand at the difficult trade of safecracker."
    "What else was I going to do, go back to Miku?"
    play sound sfx_alisa_picklock
    "As it turns out, I'm not much of a burglar."
    "But the boats here were held together not so much by the locks (which could be opened with a pinky fingernail) as by the authority of the watchman and the honesty of the pioneers, to which I was immune in ironclad fashion."
    "A few seconds."
    "Something rattled on the side of the debarkader."
    "Looks like Ulyana decided to look for the oars properly."
    play sound sfx_open_dooor_campus_1
    with flash
    "I barely had time to get to the bottom of the boat - a few seconds later someone rumbled past me with their canvas boots."
    "It was frightening!"
    "But the noise never came again - and, as it turned out, the whole time I hadn't given up trying to pick the damn lock."
    "Not so hard, I guess..."
    "If only my limbs weren't shaking so much."
    dreamgirl "Full pants of adrenaline! Whoo-hoo!"
    "But I was gentle and persistent - the shackle of the lock bounced off, and the chain rattled, freeing the nose of the blue-footed flatboat I loved."
    "Now the main thing is that no one notices me in this position - I can't get away with it!"
    with fade
    "I prayed to my guardian angel and put my weight on the can, pushing the boat forward - the vector was right, but without the oars there was nothing to think about climbing in."
    "Now and then, shuddering, I crept forward on the floorboards, dragging the boat behind me on a chain, and..."
    "Well, it had to happen, didn't it?"
    show mi smile pioneer with dissolve
    mi "Oh, Senechka! How great it is that I found you!"
    "The Japanese girl clapped her hands."
    me "Miku, not now."
    "I grumbled. {w}The boat caught the edge of one of its mates and went noticeably slower."
    show mi serious pioneer with dspr
    mi "What do you mean, not now! We need to have a serious talk, and...{w=1} Senechka, what are you doing?"
    me "Cross stitching, that's what!"
    "I barked."
    show mi upset pioneer with dspr
    mi "You're mean, if you don't want to, just say so, I'm not imposing!"
    "She arrogantly turned her nose away, but then her gaze fell on my five-minute trophy..."
    "The Japanese woman gasped:"
    mi "You're going for a ride! And without me!"
    show mi serious pioneer with dspr
    mi "No way! I won't let that happen!"
    hide mi with dissolve
    "She somehow curved strangely - and without a run, almost instantly, she was in the boat - in one easy, almost fleshless movement."
    "I swear! The boat didn't sag at all under her weight!"
    "To stop and shake the dock off the side was fraught with a run-in with the watchman."
    "Besides, Ulka the Calamity was coming out from the side of the water with two oars!"
    "She threw an extremely perplexed look at our addition, but without asking too many questions, jumped in beside Miku."
    "By this time the boat had reached the edge of the pontoons - there was only open water beyond."
    "And I, after a little hesitation, stepped from the shore into the boat."
    stop music fadeout 3
    me "And, push on!"
    "I used one paddle as a lever - pushing hard against the pontoon."
    "And on the shore someone was yelling something - obviously profane, so I didn't listen."
    play music music_7dl["too_quiet"] fadein 3
    "I invested and invested my strength in increasing the space between my puny carcass and someone who could kick that same carcass painfully."
    "But somehow or other, and from the sides of the boat to the shore lay about twenty meters - almost the middle of the river."
    "And then I let my humming hands rest a little."
    "Stacked the oars on the bottom of the boat and stared questioningly at Miku."
    me "So?"
    "She was confused:"
    mi "What?"
    me "Why were you spying on me?"
    mi "What? Me?"
    "She laughed."
    me "Not Olga Dmitrievna, after all. I think I made it clear that I don't want to talk to you, since you don't trust me."
    mi "And who's forcing you now?"
    "Unexpectedly calmly, the Japanese girl replied."
    mi "Don't communicate. {w}Keep rowing."
    "Ulyanka, who was listening to our altercation, laughed:"
    us "Oh, yes Miku, oh, well done!"
    me "Are you on her side now, too?"
    us "No - I'm on my own. {w}But it was curious to see how you would run after each other and make up."
    me "Do you enjoy such scenes?"
    with fade
    "Ulyanka blushed and turned away:"
    us "You're a fool, Semka. {w}And you, Mikuska."
    "She shook her head."
    mi "Why is that?!"
    "Miku bristled at her."
    us "Because you couldn't just be friends normally. You had to mess it up, didn't you?"
    "Since her words sounded in unison with my inner monologue, I decided not to interrupt the girl."
    "I've thought about all this many, many times myself. {w}Friendship implies an alliance of equals, and romance..."
    $ renpy.show("gfx bokeh", what = D3_intro("gfx bokeh"))
    with fade
    "It absolutely always means dependency."
    "Loss of personal freedom."
    "As we get older, we acquire a peculiarity - a spitting attitude toward personal freedom."
    "We're willing to give it away in exchange for crumbs of reflected happiness."
    "But as long as you're fourteen and whole in nature, there can be no self-sacrifice by definition."
    us "You, Mikuska, will leave tonight - and then what? Will you both suffer like two idiots?"
    me "Actually, it's none of your business."
    me "We're old enough to decide for ourselves, and..."
    us "Decide for yourselves? Old enough?"
    "Ulyana laughed."
    us "Would you look at yourself? Unhuman, dependent on other people's opinions, and a failure with a microphone."
    "Admittedly, I've been scolded worse than that - the hook bounced off my armor with a powerless clang."
    "Miku, on the other hand, unhardened in numerous debates and psychological abuse, succumbed to provocation much more easily."
    mi "What does that even mean, «failure»?! I, if you want to know.…"
    us "You don't know how to do anything. Only sing and dance."
    mi "That's not true! I also... know how to record... and can play instruments..."
    "Miku began enumerating, but Ulyana interrupted her:"
    us "Did I tell you that I have a huge collection at home?"
    us "Butterflies, bugs, caterpillars, spiders..."
    "Miku barely noticeably shivered."
    us "Noticed it in our school circle and wanted to collect it, too."
    "It still amazed me that such a little girl was completely immune to the nasty sight of a variety of insects."
    mi "Phew! But they're all dead! They showed us in class at school!"
    us "Of course they're dead. How are you going to keep them alive?"
    "I tried to remember if we were shown that in class or not."
    "Only a trip to the museum came to mind, but even there I paid tribute to sketches of dinosaurs and various ancient animal remains, not dried-up bugs."
    us "Nothing complicated. You just take a pin and..."
    "Ulyana was sitting there, smiling mockingly, and picturing with her hands the process of piercing the poor insect in quite some detail."
    "I looked over and saw that Miku was about to vomit."
    me "Will you stop it already?"
    "I should have changed the subject. All those spider bugs were giving me the creeps myself."
    us "That's what I had to prove!"
    "Ulyana was smiling broadly, celebrating her victory."
    us "Told you both you're a pair of failures. Especially you, Mikuska."
    "I didn't even try to recreate the logical chain from which Ulyana drew this conclusion."
    me "Listen, Ulyana."
    "I decided to voice a long-standing hunch."
    me "Just because Alisa told you to play somewhere else while she's doing adult things doesn't mean anything."
    me "She's still your friend."
    us "What does that have to do with anything?"
    me "What's that got to do with your anger toward Miku I don't understand."
    with flash
    us "And why are you defending her?!"
    "Suddenly Ulyana shouted."
    us "You're her husband, aren't you? Husband?"
    "I blushed again."
    "Miku blushed, too."
    "And Ulyana only waved her hand:"
    us "Turn to the shore. {w}I've had enough of you."
    "I obediently did as she said."
    play ambience ambience_lake_shore_day fadein 3
    us "Mikuska, look, is there a lighthouse on the left?"
    mi "Where?"
    "Miku turned her whole body to where Ulyana was pointing."
    with vpunch
    "And she pushed her as hard as she could, instantly throwing her out of the boat."
    "Our little boat rocked, and we were left alone against each other."
    scene cg d2_us_boat_escape_7dl with dissolve
    me "Hey, are you out of your mind?!"
    "I shouted, dropping the oars and jumping up."
    with fade
    "And I definitely shouldn't have done that!"
    "Miku was doing fine in the water - she had already swum to the surface and was flipping her limbs there, gleaming her eyes angrily."
    th "We ought to throw her a life ring."
    "I thought - and that's all I had time to do."
    "Because a second later I felt a jolt somewhere in my sacrum, and behind me came an obnoxious, hurtful, squeaky voice:"
    us "Swim to your wife!"
    play sound sfx_shoulder_dive_water
    scene anim_underwater with dissolve
    "And the cold water clogged my throat."
    "Before I could regroup or breathe, I fell out of the boat - judging by the peculiar pain I also got hit in the spine with an oar."
    play sound sfx_water_emerge
    scene bg ext_sky_7dl with dissolve
    us "May your woes be many, and your love few."
    "I heard it when I swam out."
    "With these words, Ulyana took over the boat and, unskillfully paddling the oars, steered the drifting vessel roughly toward the shore."
    "Raking on the oars."
    "As she did so, she chanted angrily «Blow with the Fires»."
    "I covered my eyes - the treachery of the little one was shocking."
    scene cg d4_mi_sup_7dl
    show unblink
    play music music_7dl["ask_you_out"] fadein 2
    mi "Senechka? Senechka, are you all right?"
    th "Except for the fact that I just got hit in the spine with an oar?"
    th "Again the idiotic questions are from American movies."
    "No, I'm not ok."
    "Miku kept close to me, paddling with her feet."
    mi "Are you doing okay on the water?"
    "I nodded my head briefly."
    mi "Then let's swim to the shore - it's not far."
    "I followed the Japanese girl's gaze: indeed, Ulyana was gracious enough to throw us off the board five meters before the dock."
    "She herself was already standing there, echoing something to the suddenly-arrived Sanich."
    "He nodded and cast a hard look at us."
    scene bg ext_boathouse_day
    with dissolve
    "I got out first, the water running off me in rivulets, and the cold wind shaking me in the back."
    "Then I helped Miku to the top - she looked no better than I did, just as miserable, wet and blue-lipped."
    ba "Pioneers, is it true that you kissed in the boat and were thrown overboard by Sidorova for it?"
    th "Are you serious?!"
    "I wanted to yell."
    "But Miku beat me to it."
    mi "It's true."
    scene cg d4_mi_sup_7dl:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 2.0 zoom 1.15 xalign 0.5 yalign 0.5
    play music music_7dl["tellyourworld"] fadein 3
    "With vengeful happiness in her eyes, the Japanese girl replied."
    mi "True."
    "I am too selfish to allow you to hurt yourself. For you are mine, your bruises and scratches hurt me."
    "And now I can feel you worrying and really want to be far, far away from here."
    "But everyone is looking at us, which means there's no room for weakness."
    mi "And right now - too."
    "She continued."
    scene cg d4_mi_sup_7dl:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 2.0 zoom 1.15 xalign 0.5 yalign 0.5
    show gfx bokeh
    with flash
    "A second more, and my lips touched hers."
    "Softly - but is strength the point?"
    stop music fadeout 10
    mt "Hatsune!!!"
    "A squad leader's voice came from somewhere over the frame."
    mt "MARCH TO THE DIRECTOR, NOW!!!" with vpunch
    scene black with fade
    pause(3)
    stop ambience fadeout 3
    scene bg int_chief_office_day_7dl with dissolve2
    play ambience ambience_int_cabin_day fadein 1
    play music music_7dl["the_way"] fadein 3
    "While we were being led, I wondered what the performance we'd done on the shore might be fraught with."
    "Any way you look at it, we were seen by almost half the camp - a bit of a mishap that can't be silenced."
    "And what's there - immorality, punish with a public reprimand?"
    "The funny thing, perhaps, is that half of all the threats didn't apply to Miku, and I was immune to the other half altogether."
    "What can they do? What?"
    "Resettle-removal? Oh, big deal."
    "Not that I'm turning on the nihilist and spitting on everyone from a high bell, but kissing pioneers is primarily a problem of the counselors and the collective, not the pioneers themselves."
    "Collective-chain responsibility."
    "And the fact that we were brought in almost under escort made you think about a lot of things."
    "It's not good to think that people around me are motivated only by self-interest - but that's how I was brought up by my society, for which I thank it, point out in the credits, and fuck off."
    "Far more depressing to me was the other thing."
    with fade
    "As it turns out, I don't know a thing about Miku."
    "I mean, I've got some of her stories in my head - but that's a subjective point of view, when you only see what the narrator sees, and you can't see the whole picture..."
    "What did I know? Problems in school, a career as a performer, and also this Sakishita. {w}That's about it."
    "It didn't bother me before."
    "After all, the camp is like a separate world with sovereign boundaries and its own laws."
    "The law works here: you just have to feel sympathy for a person to spend time with them."
    "You don't care about the rest, it's put out of brackets."
    "I woke up in the morning, and we were side by side with the girl all day."
    "The plot is certainly not the most twisted, but it suited me."
    with fade
    "Yes, I'm a lazy and indifferent pig, everything's correct."
    "What does she live with, what are her interests, what are her plans for the future?"
    "I've heard about her engineer father, but I haven't heard a word about her mother, the rest of her family."
    "Another question - if you take away her music, who will be left? {w}What else is capable of awakening interest in the azure eyes?"
    "A mainstay in life? Interests?"
    "Why did she cling to me so much when I confessed my fear for her? Was I the first, excluding her parents?"
    "Is she really {b}that{/b} lonely?"
    with fade
    "But she sings, don't they teach that - how to make a person like you, how to get to know someone?"
    dreamgirl "How do you find a best friend? Or a person you trust as yourself?"
    play sound sfx_open_door_strong
    pause(1)
    scene
    $ renpy.show("bg int_chief_office_day_7dl", what = Dawn("bg int_chief_office_day_7dl"))
    with touch
    "The door slammed, and the camp director entered the room."
    "He settled down at his desk and, clasping his hands together, began to study us."
    "For a moment his gaze stopped on our intertwined fingers, and Miku squeezed my palm even harder."
    bb "Sit down."
    "It sounded like he was a teacher and we were here for his class."
    "And maybe that's what it really was."
    "Everyone bustled about, settling into their empty chairs."
    with fade
    bb "So, as the first squad leader told me, there was an emergency today."
    "Checking the paper, the director recounted our adventures this morning."
    "That's right, that's right - walking, being friends, falling down, then swimming together in general..."
    show ba normal uniform at fright with dissolve
    ba "I don't want to make excuses for anyone, but let's be lenient with the wimp - he's the injured party. {w}Everybody saw who had the initiative."
    "For a fraction of a second, I even developed some sympathy for the lame-ass gymnast."
    "And even forgave him for the «wimp»."
    with flash
    "I felt myself blush."
    "Though nothing seemed to be able to excite me anymore after today."
    bb "Accepted. Would anyone else like to add anything?"
    "Those present shook their heads in the negative - right, right, nothing more to add."
    show mt sad pioneer far at left with dspr
    mt "That must have been my oversight."
    "The counselor sighed."
    mt "I had noticed before that they were spending too much time together, but Miku was completely disconnected from the collective, so I decided to let her at least be friends with someone."
    "Olga looked depressed."
    show ba em1 uniform at fright with dspr
    ba "And I was there from the beginning."
    if alt_day2_mi_snap:
        ba "And they've been friends for a long time, almost from the moment the wimp came to camp."
    else:
        ba "The little girl is nice, but this kid is kind of suspicious."
    show mt angry pioneer with dspr
    mt "Boris Alexandrovich!"
    show ba em1 uniform with dspr
    ba "I apologize."
    "The remorse in Sanich's voice was nowhere near there."
    ba "But I've known the little one for three weeks, and she's never given anyone any trouble."
    show mt normal pioneer with dspr
    mt "Except for the opening of the shift."
    "Mumbled Olga."
    show ba smile uniform with dspr
    ba "Don't worry about it, I didn't put that picture in the album!"
    bb "Comrades, we got distracted."
    "The director reminded us of himself."
    bb "What shall we do?"
    ba "They're taking the girl away today anyway, so I suggest that we lecture the wimp at a lineup and call it a day."
    show mt rage pioneer with dspr
    mt "Boris!!!"  with vpunch
    bb "Olya, hush..."
    "The director frowned."
    "The counselor also frowned and slowed down."
    show mt angry pioneer with dspr
    mt "Where's the justice?! {w}I'm not whitewashing anyone, but both are guilty, and if we punish, both should be punished."
    bb "And those by whose connivance it happened."
    show mt normal pioneer with dspr
    mt "Exactly."
    bb "And what do the guilty themselves have to say?"
    "The director turned his gaze to Miku and me."
    stop music fadeout 4
    play music music_7dl["silent_angel"] fadein 3
    bb "Do you have anything to say? Hatsune?"
    "Miku didn't seem to pay any attention to the principal's retort."
    "She was silent! Silent! {w}For the first time since we met, the machine-gun girl had nothing to say."
    "The attention of those present was focused on the unfortunate Japanese girl; it would seem - what is the attention of the crowd to her!"
    "And a little shiver ran through her fingers."
    bb "Look, we can't help you if you stay quiet like this."
    "Miku continued to be silent, only her trembling became even bigger - I thought she was pounding in a way that was noticeable to everyone around her."
    "In reality..."
    bb "Hatsune?"
    "Patiently the director continued to press on."
    with fade
    "And this is the lauded Soviet school of pedagogy? Professionals working with children?"
    bb "Maybe there are some circumstances that we don't know about?"
    "Circumstances?! I'll tell you what circumstances!"
    "Wasn't a problem? Because nobody wanted her!"
    "Was she quiet and modest? Because there was no one to see the real her!"
    "She was dragged out of her native loneliness, only to be thrown into another, and the moment someone who cared appeared on the horizon..."
    ba "{b}Kid{/b}, say something."
    "I'd tell you, idiot..."
    mt "Miku?"
    "I squinted my eyes and saw Miku standing staring at me, obviously going into some kind of stupor of her own."
    "Her eyes were completely blank - they were just reflecting the light falling obliquely from the window."
    "And the silent mouths of adults - funny that way, like fish in a fishbowl."
    bb "There's a blatant indifference and disregard for the rules."
    "Blatant? It is your indifference that is blatant! How can you be so blind?"
    "I am frozen in place by the irrational fear that she may have remembered who she was there at my house."
    "And if I turn away now, the steam wall will be blown away by gusts of wind, and the warm (still warm) fingers in my palm will turn into condensation droplets."
    "They kept saying something, demanding something, and I wanted more than anything in my life right now to be somewhere far away from here."
    "Where it would be just me and her, where I could stop lying to myself and realize how much I cared about this girl."
    "And have just a few minutes of happiness - together - for two."
    "But have I earned the right to happiness if I chickened out and gave up when the opportunity presented itself?"
    "I am ridiculous. Ridiculous and pathetic."
    "And I certainly don't deserve a girl like Miku."
    play sound sfx_bodyfall_1
    "Suddenly her eyes rolled back and she collapsed in my arms."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_7dl_dinner:
    scene bg ext_dining_hall_near_day with fade
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 4
    play music music_7dl["will_you"] fadein 3
    "My life is like a bag of gingerbread - I've got nothing, I won't give you anything."
    "For lunch they gave all the nutritionists cursed hodgepodge - a farewell greeting to the stomachs from the chef."
    "Any inspection now could take the camp authorities by the soft spots."
    "Just like when they make dumplings for the kids, for instance."
    "Or baking blueberry pie - strictly speaking, that's all forbidden. But who in their right mind and in their right mind would refuse such a thing?"
    if not alt_day5_mi_7dl_voyeur:
        "I was still feeling a little queasy after this morning's events."
        "Still, in spite of the caring Slavya and Miku opening the window every minute, there was a certain overabundance of cheerful substances in my body."
    "So the soup, to which in any other situation I would have reacted in the most positive way, now I hardly paid any attention."
    "Took two and a half spoonfuls and set it aside."
    if alt_day5_mi_7dl_voyeur:
        "I couldn't stop thinking about how many totally derelict pictures of a starlet I knew were lying in a dead pile at the bottom of the box, and I was choking on soup!"
    show mi normal pioneer with dspr
    mi "Senechka, why are you so thoughtful?"
    if not alt_day5_mi_7dl_voyeur:
        me "I just can't get it out of my head that you were sitting in the cabin in broad daylight, smoking. That doesn't sound like you at all."
        mi "Senechka, I'll explain it to you."
        "Miku took out a notebook and pen and wrote a whole line in Japanese on a piece of paper."
        "«カコイジェピヴォピスデゲネラツピズデツプロスト»"
        "I stared at the sheet in bewilderment."
        me "And what does that mean?"
        mi "That everything has a reason, Senya."
        me "You don't say!"
    else:
        me "No reason!"
    "Proudly I retorted."
    "Despite this morning's events, I haven't forgiven the treacherous Asian woman, and I don't plan to."
    "She immediately pouted her lips and, getting under the table closer, kicked me under the knee - not very painful, but extremely palpable!"
    play sound sfx_punch_medium
    mi "Senka!" with hpunch
    "A real gentleman would never interfere with a lady hammering a nail wrong, right?"
    "What if a lady is hammering the toe of her dainty shoe into a gentleman's knee? How to respond with dignity in such a situation?"
    "Intuition told me to ignore the annoying factor."
    "Actually, that was the advice I was planning to heed when I got the second hit."
    show mi dontlike pioneer with dspr
    mi "Senechka, I'm here, hello!"
    "Holding the air in my chest as long as I could, I let it out through clenched teeth."
    mi "You can't hear me at all, can you? Or don't want to hear me?"
    me "I can hear you just fine."
    mi "Sakishita-san will be here at 4 p.m., we have a couple of hours."
    mi "Do you want to go for a walk?"
    "Seeing my complete lack of enthusiasm for the poisonous orange liquid in my plate, Miku decided to follow my example."
    "And in vain - she'll be going home hungry!"
    mi "Anywhere! Do you want to?"
    show mi angry pioneer with dspr
    "Miku raised an eyebrow and looked at me with a complex mixture of threat and embarrassment:"
    mi "You don't want to?"
    "As long as she put it that way..."
    me "Actually, I don't mind."
    if alt_day5_mi_7dl_voyeur:
        "Though I haven't given up on plans to get a couple or three totally exclusive memories with a Japanese pop star!"
    else:
        th "I hope she doesn't make me brush my teeth or do any other bad things?"
        "Though she might - she threatened to kiss me, didn't she?"
        "And for all her talkative nature, Miku had the remarkable quality of always keeping her promises."
    me "Just don't jump up and down, okay? {w}I'm tired."
    show mi smile pioneer with dspr
    mi "Of course, of course!"
    "She clapped her hands."
    th "How does she contain so much enthusiasm?"
    mi "Let's go with you, like grandma and grandpa - hand in hand!"
    me "Of course that'd be too much..."
    show mi grin pioneer with dspr
    mi "Why not? It looks fun enough to try."
    "She bent over the table and leaned on an imaginary stick."
    "Getting into character, no other way."
    th "I have a feeling that the impending departure awakens in her nothing but positive vibes."
    show mi normal pioneer with dspr
    mi "I'm already small, and when I'm old I'll be even smaller!"
    "She declared, looking at me with some incomprehensible delight."
    mi "I'll live in your breast pocket and take my cactus collection out to the sunny side in the morning and sing 'sembonakazuru' to them instead of morning exercise."
    dreamgirl "Eh... Y?"
    if alt_day5_mi_7dl_voyeur:
        dreamgirl "I think while we were away, she managed to overdose on something."
    else:
        dreamgirl "She refused cigarettes, but mushrooms definitely didn't miss her diet."
    show mi sad pioneer with dspr
    mi "Hey, why are you looking at me like that?"
    me "No, it's nothing..."
    mi "Tsk-tsk!"
    show mi grin pioneer with dspr
    "Miku showed me her tongue and moved even closer."
    me "So, going for a walk?"
    show mi happy pioneer with dspr
    mi "Of course!"
    me "Okay. Whatever you say..."
    "I nodded obediently."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_7dl_soul_day:
    scene bg ext_un_hideout_day_7dl with dissolve
    play ambience ambience_lake_shore_day fadein 1
    play music music_7dl["lynn"] fadein 3
    "Nothing has changed here - and nothing will change for millions and millions of years, absent human force intervention."
    "There will still be a faint breeze hitting the left cheekbone, sunlight hitting the right, and a myriad of sunbursts shamefully bouncing off any number of bounces that man is capable of making."
    mi "What are you thinking, Sen'?"
    "I wasn't surprised that she brought me here."
    "After all, this is where our story began."
    "Yes, it is the tiniest bit younger than our strange acquaintance - for it is Miku who had the honor of first meeting my gaze upon awakening."
    "And then... then imprinting."
    me "I think about what would have happened if I'd given up the idea of looking for you four days ago."
    "I confessed."
    me "I wanted you to babble and babble: it gets so delightfully empty in my head with you around."
    show mi sad pioneer with dspr
    mi "I won't say anything, that's nice to hear."
    me "Come on."
    "I touched the Japanese woman on the shoulder."
    mi "In fact, my attitude toward you is so complicated that it's very hard to put it into one word."
    show mi normal pioneer with dspr
    mi "But why?"
    me "Because it's good with you, but I don't believe in being good for too long."
    me "Because I'm afraid of falling in love with you and disappearing completely."
    show mi cry pioneer with dspr
    mi "But... But..."
    me "Because you're about to disappear from my life, and I've only just begun to believe that the tale with your eyes is stronger than tears."
    me "Only it's not, is it? I am not a miraculous deliverance, and you are not the princess of a fairyland where our wildest dreams are possible."
    "Miku turned away:"
    mi "I wrote a new song."
    "In a shaky voice she reported."
    mi "This is the third one since we met."
    if not (alt_day4_mi_7dl_ev_savior and loki):
        mi "So you see, you became my muse after all, even if you didn't want to."
    me "Will you sing?"
    "She shook her head negatively."
    show mi shy pioneer with dspr
    mi "For some reason I'm very embarrassed to sing it to you."
    me "And just like that? Aren't you shy?"
    mi "I should try it."
    "In doubt she uttered."
    with fade
    mi "As I was writing the words, the same thought was running through my head: sometimes you have to be your own hero."
    mi "Just because the people you can't breathe without are fine without you."
    show mi smile pioneer with dspr
    mi "Life in Japan didn't stop when I left there. Life isn't going to stop here in two hours when the car comes."
    me "How do you know, by the way? About the two hours..."
    mi "Sakishita called from the city early this morning, he has all the papers, all the permits..."
    me "There's still time, so..."
    "Quietly I rejoiced."
    "Glanced at Miku, confused, realizing my thoughts were obvious to her."
    "The beach was sunny and calm and very, very lonely. {w}It suddenly occurred to me that if we both wanted to, and..."
    "I shook my head, driving away the detailed visions - with sobs, groans, smells..."
    me "No regrets?"
    show mi normal pioneer with dspr
    mi "About yesterday? Not at all."
    "Serenely she explained."
    mi "There is a risk, of course."
    "Judging by the look on her face, she spits on any risk... whatever the odds are."
    me "You're talking about..."
    show mi grin pioneer with dspr
    mi "About that, yes. {w}Sure, I'm not that old... But it's not scary, you know..."
    me "Well, really now..."
    "I kept pushing and pushing on the subject - as if there was simply nothing to talk about with the girl, my beloved girl who was about to go nowhere and for who knows how long."
    dreamgirl "Beloved? Did you finally admit it to yourself?"
    "I shrugged."
    "It hasn't been a secret to me since day one, when I saw the tiny hearts in her pupils."
    "And I'm long past the age of twelve to be afraid of my own dependence on someone..."
    "Especially if that «someone» is so… so cute!"
    show mi laugh pioneer with dspr
    mi "And «if», Senechka — that's when I'm going to be. Don't ruin my last hours with your «what ifs», okay?"
    "She picked up a pebble from the ground and sent it in the direction of the barely visible from here steel string of rails."
    show mi normal pioneer with dspr
    mi "Ever wanted to lose your mind, Senya? {w}Imagine this: you have an important case, millions of people rely on you, and you spit it all out and run off somewhere in the middle of Siberia."
    mi "Exciting, isn't it?"
    me "No."
    mi "No?!"
    "I felt an inexplicable anger at this girl: nothing could get through to her, nothing!"
    me "I wouldn't let myself go crazy if I had even one person to rely on."
    show mi cry pioneer with dissolve2
    mi "Stop it, do you hear?"
    "She turned away sharply."
    mi "I'm trying my best not to fall apart into snot and yelling so I don't ruin these hours, do you hear me, you?!"
    mi "Gods see, I'd give a lot to stay here and now."
    mi "And you keep standing there with a sour face like it's solely my fault."
    show mi rage pioneer with dspr
    stop music fadeout 5
    mi "I'm not going to let you ruin my goodbye to you, understand me?"
    with vpunch
    "In her eyes gleamed a fury never before seen!"
    "Taking a step toward me, she grabbed my shirt and yanked me toward her with all her might:"
    scene cg epilogue_mi_9 with flash
    play music music_7dl["feel_you_inside"] fadein 3
    mi "I'm so lonely, I'm alone, always on my own..."
    "She babbled, awkward, wooden fingers swiping at the buttons of my shirt."
    "It was as if we'd never had anything, as if she were now a worried teenager who'd been let in the closest thing - herself."
    mi "And you're a meanie. How did you get to be so needed?"
    "Another tug and I felt her lips on my neck, her fingers on my shoulders."
    mi "Don't you realize how cold I am without you? Warm me, warm me..."
    mi "I've never met anyone like you, and you are silent, as if you never cared."
    mi "As if you don't care about anything."
    "She clung to me, trembling in frenzied fever, and my greatest fear was that someone would wander onto this secluded beach and catch us here."
    "But there was no one, no one - it was as if Miku's will alone could influence the laws of nature, make everyone around us go the other way."
    mi "And you know - I can forgive your indifference."
    "Turquoise manicured fingers walked across my cheek, lightly scratching it."
    mi "Because with you... With you I'm not afraid of anything, Senya."
    "Her voice faded, beginning to sound with a whisper as her breathing deepened and a scarlet color climbed on her moon-white cheeks."
    me "Miku, don't go crazy..."
    mi "Senya, do you like me even a little bit?"
    mi "Tell the truth, I'll understand, Senechka, tell me!"
    "She pressed against me with such force, as if she were really going to get under my clothes - so that I could feel all her softness and bulges."
    me "I-I like you..."
    "I squeezed out."
    me "Very much."
    mi "Why are people such idiots, Senya? If I'd just had the guts to do everything sooner."
    mi "Or just to look around - but I was drawn to myself, to the new experiences you were awakening in me."
    "She managed to speak and kiss me at the same time, though I found it more and more difficult to keep the meaning of her words in my mind by the minute."
    mi "But hell if I'm going to miss even a second now. I want to feel you inside."
    me "Miku, they might see us..."
    mi "I don't care. I'm going to be picked up in two hours from the man who means everything - I want to spend those two hours with him."
    mi "With you, Senya."
    "Her voice got stronger, and her fingers stopped shaking."
    "And before I could say anything, she sank to the sand and pulled me with her."
    "Here it was as if we were climbing a slide - and frozen in a fragile moment of equilibrium, no matter where you go from here, any path will only be down."
    "And I exhaled - stretched - and turned off the light in my head."
    "Because of the stockings, it seemed that the hand had passed the knee, the thigh, on its own, and lingered in the area that the sophisticated Japanese call «zettai» and froze, slightly touching the soft, thin fabric."
    "A sparkling libido rushed into my bloodstream, making me swallow nervously - but neither I nor she were able to say a simple «stop»."
    scene black with dissolve
    "Miku exhaled sharply and spread her legs slightly, pushing herself forward."
    mi "Se... nechka..."
    "She stood up and allowed me to pull a piece of striped fabric down, letting me into the warm, supple secret..."
    "Where I immediately ran my finger, forcing her to shriek-exhale."
    "In response, she ran her hand down my shorts-the narrow hand went freely under my belt, but it was uncomfortable from there."
    "Biting her lip, she hooked her other hand into the process, actively submitting under my caresses, loosened my belt, and undid several buttons."
    "Satisfied with herself, Miku wrapped her right arm around me and placed her left hand on my chest, scratching my skin with her fingernails."
    "A second later, the last buttons on her shirt were popped, too - she wasn't wearing a bra."
    "Our eyes met, and a rich scarlet blush played across the girl's cheeks-it had gotten even brighter since we started."
    mi "Do you like it?"
    "She smiled slyly, showing me herself in all her glory."
    me "Very much."
    "It was all wrong, wrong, dangerous! {w}It wasn't even the fact that someone might see us - but I imagined someone now clearing their throat noisily over us, and us jumping up with our hearts pounding, ruffled, wet..."
    "At the bottom of Miku's eyes I read the reflection of my own thoughts - no matter how crazy she was, she knew exactly what was fraught with what we were doing."
    "What's fraught, what's going to happen in a few seconds."
    mi "Come here."
    "She called."
    mi "You are my first, my only."
    "Snow-white skin to which no tan had ever adhered, a teenage girl's figure and an abyss of adoration in her eyes."
    mi "Come..."
    "Her legs wrapped around my thighs in a pose that was perfect for both of us."
    stop music fadeout 3
    scene black
    "And I went mad."
    "We both did."
    scene cg epilogue_mi_1
    with dissolve2
    play music music_7dl["unforgotten"] fadein 3
    "I don't know how long the multi-armed creature that united our minds existed, but when the restraining power wore off, we lay there in each other's arms, exhausted, wet, breathing heavily, for a few more minutes."
    me "Aren't you afraid of anything at all?"
    "I asked, as my strength returned to me."
    mi "I'm afraid this is our last time. It creeps me out."
    "Her thin fingers gripped my wrist with surprising strength."
    "She sobbed."
    mi "And it's like I want to breathe before I die - and I can't."
    mi "I keep thinking that we'll have time to chat, to walk around - someday, later! Later!"
    mi "Right now we have to manage to do what we can't do in front of witnesses - to love each other!"
    mi "Isn't being together love?"
    mi "And when will that «later» be, when?!"
    scene bg ext_sky_7dl with dissolve
    mi "I always just mess everything up, don't I? Got it all wrong again, didn't I?"
    "My head was cracking at the seams, and there was nothing but white noise in my mind."
    "But as wild as I was, I had no right to leave the girl alone."
    me "It's all right."
    "I parted my lips."
    "The voice was squeaky and unkind."
    me "We can do nothing at all, just lie next to each other."
    me "And still be together. {w}That is the great mystery of love."
    "Kanji «ai», signifying a man's love for a woman."
    "Miku was silent the whole time as she wrote out all the squiggles."
    "And when she looked up from the sand, her lips once again played with that light-hearted smile I loved."
    mi "I don't want you to love me when I'm sweaty."
    "She reported."
    mi "I'm going to go take a dip - and when I come back, it'll be better. Isn't that right?"
    "I made myself nod."
    th "It won't be better."
    th "Never."
    me "Of course it will."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_7dl_star_day:
    scene bg ext_stage_big_clear_day_7dl
    show mi normal pioneer with dspr
    play ambience ambience_camp_center_day fadein 0
    play music music_7dl["nowyouseeme"] fadein 3
    "The street smelled of red-hot copper wires and hopelessness."
    "The only thing missing was the puddles in which the green leaves stripped from the trees were still alive, like a monument to an unneeded death."
    "And then you could sit over such a puddle and gaze into the depths, into the reflection-the sky in it is somehow always deeper and more appealing, peering with an alluring failure, indigo blue."
    "I guess it's because the world itself is a pretty shitty, gray and boring thing."
    "And it would be nice to jump into one such gap - to hold my breath for a while and pop out the other side, where the air is cleaner and the people are more honest."
    "Miku beside me was silently peering around me - remembering."
    "She looked like the same Nihon tourist on the herd with «Nikon» in her arms — curious, immensely sweet and extremely cheerful."
    show mi normal pioneer with dspr
    mi "And I have a whole piece of fabric left in the tone of my suit."
    "The Japanese girl sighed softly:"
    mi "I thought you and I were going to perform, then I'll make you a suit like mine! I mean, not like mine, of course, you don't need a skirt, but shorts and a tank top, and we'd perform together! Singing or dancing."
    me "Yeah."
    "I said meaningfully."
    mi "Actually, of course, at first I was supposed to just make myself some interesting costume for the stage in my favorite colors. And then I wanted to make a costume for you."
    mi "Now it's neither here nor there."
    "She thought for a second."
    show mi smile pioneer with dspr
    mi "Here! Do you want me to leave you the cloth?"
    me "What do you mean?"
    mi "For costumes!"
    me "Miku, you didn't sleep well, did you?"
    show mi sad pioneer with dspr
    mi "You'll sew your own..."
    "Yes, of course I will. I will."
    hide mi with dissolve
    "I glanced over at the bandstand, where Alisa and Slavya were running around, getting the equipment ready for the next concert."
    "For some reason I wasn't called to help."
    "Though both looked distinctly greenish."
    "Well, it's up to the man."
    "But they were happy to 'plow in' absolutely all who came their way, from small to large."
    "Here the kids, panting, pulled out from the backstage cloth covers of unknown purpose and began to remove them under the stage."
    "Here Danka, monkey-like, flew up, holding the plug in his teeth - secured with his knees at the top, commanded, 'lift!'"
    "Here are the girls, already quite small, led by the panting Electronik, carrying an antique mirror in a beautifully carved frame."
    "For a second he turned the mirror so that I was able to see myself..."
    "Us."
    "Me - tall, slouching, skinny, with my shirt hanging bubbly over my shoulders."
    "But somewhere the aloofness has faded from my face, the darkness in my eyes is gone, and the stamp of boundless, joyless loneliness has disappeared from my face."
    "And Miku beside me - she remained an angular teenager, but there was a fluidity to her movements, and her smile was no longer professionally worked up, but increasingly simply cheerful."
    "Before, I would have been mortified by all the mousy preparations, all the perturbations with equipment and props - but now it was all just quietly enjoyable, humanly pleasant to watch the mechanism set in motion by Alisa and Slavya and their companions."
    "Except that my starlet here is finishing her last hours."
    "A sure thing to be upset about."
    "If it weren't for the puppyish happiness of her just walking along, holding my hand."
    "Apparently I had degenerated to the point where I couldn't fit more than one emotion in my soul."
    "And now I wasn't distracted by what would happen next - would happen, and the hell with it."
    show mi smile pioneer with dspr
    mi "You're smiling like a cat who stole a bunch of sausages."
    "Miku scolded me."
    me "Can't I?"
    mi "You can..."
    show mi grin pioneer with dspr
    mi "Next to my house lived an old cat, Obito-san. When I was rushing to school, he would always sit on the warm slabs and purr."
    mi "Sometimes there was no way to hold back!"
    "She smiled."
    mi "He was so round and so black and so content, I wanted a piece of his contentment!"
    mi "Sneaking up on him from the side and pushing! Boom!"
    "Miku opened her eyes, showing how loud the «boom» was."
    mi "Obito-san was falling on his side, and looking indignant in the process-as if he had been cheated of his best feelings!"
    "The Japanese girl tried to picture on her own face what it might have looked like."
    show mi happy pioneer with dspr
    mi "And then I would start tickling his belly."
    "Eyes wide open, fingers spread and excitement on her face:"
    mi "Wakey-wakey-wakey! Knead the dough, kitty pies!"
    mi "Obito-san scolded me in his feline tongue and caught my fingers with his paws - not once in the time we've known each other has he scratched me."
    me "You speak of him in the past tense."
    show mi sad pioneer with dspr
    mi "Yes."
    "For a second she saddened."
    mi "Pa was promoted after the power plant near Sapporo was commissioned, and he lived in that dorm near my school all the time - very convenient for me and him."
    mi "But after the promotion, Ma said it wasn't proper for an official of his rank to 'hang around in dorms' - by the way, Dad's expression! - and a few months later we moved to a new house, closer to the center."
    me "So that's how it is. {w}I haven't seen Obito-san since."
    stop music fadeout 5
    show dv normal pioneer at left with dissolve
    dv "Mikuska, are you leaving soon?"
    "Miku glanced at her watch:"
    mi "They should be coming for me in half an hour!"
    dv "Maybe while there's time, let's sing."
    show mi surprise pioneer with dspr
    mi "Sing? Why?"
    show dv smile pioneer with dspr
    dv "I've got a little song... You've got to like it."
    play music music_7dl["closetoyou"] fadein 3
    "Alisa climbed up on the stage, rummaging through the instruments for a while - her guitar seemed to have been thoroughly thrown into the rags."
    "But a few seconds and she was back in front of us, sitting down with her foot tucked under her, playing the first few chords."
    "Old acquaintances, loved ones, relived hundreds of times."
    "That song squeezed the tears out of me, of course..."
    "I didn't notice myself shaking my head to the beat, hastily recalling the words of the verse-chorus:"
    me "Come on, come on, stop being silly..."
    "With one lip I said."
    me "I'm with you! Give me your hand."
    "A part played at a virtuoso level, behind which hundreds and hundreds of repetitions could be guessed."
    "And the words bouncing off my teeth - a call not to be sad."
    "A plea to just {w}smile."
    "And when Miku joined in with Alisa, successfully getting into rhythm and harmony, I really couldn't hold back a smile."
    scene cg d4_mi_guitar with flash
    dv "Just look into my eyes, smile - it's half an hour till dawn."
    "Alisa began - and I realized that I knew those lines, too, even though I'd only heard that song in Japanese all my life!"
    dv "And maybe I'll finally have the strength to tell you what's most important."
    mi "We were not and are not! We are a void, a mirage!"
    "Picked up Miku."
    mi "You'll say, 'How's it going?' - and I'll lie."
    mi "Things don't go, and I don't live without you anymore."
    "It was amazing to me how they got together so successfully, rehearsed the words and the order of the performance..."
    "But, in the end, they had exactly two more weeks than I did to get some practice in!"
    "The song went surprisingly well with both girls."
    "Miku sang with a gasp, letting the words sink in."
    "Alisa, on the other hand, shook her head to the beat - and would have looked more appropriate with a song about distant cities and countries."
    "But here, too, with the call to smile at the unknown abandoned, she looked surprisingly appropriate and believable."
    dv "You just look into my eyes, smile - for it's half an hour before dawn!"
    mi "And maybe at last I'll have the strength to tell you about the most important thing."
    stop music fadeout 3
    scene bg ext_stage_near_clear_7dl
    show dv normal pioneer
    show mi normal pioneer at right
    with blind_d
    "At one point Aliska simply swatted the strings with her palm:"
    dv "Come on, it's boring. {w}Mikuska, do you have anything funnier to make me remember you with a smile?"
    show mi surprise pioneer with dspr
    mi "More fun? Hmmm... {w}But we have to hook up the hardware."
    show sl smile pioneer at fleft with dissolve
    sl "It's all ready. {w}Waiting for you."
    mi "You think so?"
    "The Japanese girl hesitated."
    sl "I'm sure!"
    "And the pioneer helpers who came up from behind began to chant in a voice:"
    voices "Miku! Sing! Ta-ta-ta! Miku! Sing!"
    "And they beat the 'ta-ta-ta-ta' with their hands and feet like soccer fans."
    "How could the poor girl resist?"
    show mi happy pioneer with dspr
    mi "All right, all right! I'll sing something!"
    "She went to the presenter's table, where various tapes were already piled up, and after searching, she found the right one."
    mi "Senechka! When I get on stage, will you press 'play'?"
    me "Will do!"
    "I retorted."
    mi "Oh. Well, off I go."
    scene bg ext_stage_big_clear_day_7dl
    show mi normal voca
    with dissolve
    play music music_7dl["bad_apple"] fadein 3
    "She briefly lingered backstage, and when she came on stage, and I pressed the play key..."
    "I barely caught my jaw at the very ground!"
    "For two reasons at once."
    "First, something extremely reminiscent of the broken rhythms of electronic music of my day was blaring from the speakers."
    "And second, Miku had managed to get her conspicuous dress and change her clothes somewhere!"
    "Not that I mind..."
    show frame at truecenter:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 0.8 zoom 1.0 xalign 0.5 yalign 0.20
    show cam_ui at truecenter:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 0.8 zoom 1.0 xalign 0.5 yalign 0.30
    "I reached into my pocket almost automatically and pulled my balalaika outside with the camera lit."
    "I don't know if this world is a glitch or not - but I owe it to myself to film it!"
    show mi smile voca with dissolve
    "Miku smiled charmingly - she seemed to have guessed this feature of my phone."
    "And went on with her performance."
    dreamgirl "And my friend's lips burned with a kiss soaked in tears."
    th "And I haven't been to the sea - I haven't been, like in that movie about salt and a truckload of lemons."
    dreamgirl "Take Miku to the sea. {w}Otherwise, what will you say up there when your hour strikes?"
    "I shrugged."
    "Little by little, the song was coming to an end."
    "So was the battery charge - after all, I somewhat didn't plan on being in the middle of it, so I wasn't charged to the hilt."
    dreamgirl "And you didn't bring my 'power bank' with yourself."
    dreamgirl "Savage!"
    th "Shut up already."
    pause(1)
    play sound sfx_7dl["snap"] fadein 0
    scene white with flash
    pause(1)
    stop music fadeout 5
    with fade2
    return

label alt_day6_mi_7dl_miku_sakishita:
    scene bg ext_camp_entrance_day with dissolve
    play ambience ambience_camp_entrance_day fadein 3
    play music music_7dl["iwantmagic"] fadein 3
    "This is where it all began."
    "This is where it ends."
    "We both made a huge mistake, trading our cloudless friendship for stiffness and miscommunication."
    "But that doesn't make me feel any better."
    show mi upset casual with dissolve
    mi "Sen', I'm sad."
    "Complained Miku, standing almost up close - but actually farther than a million kilometers away."
    if alt_day5_mi_7dl_voyeur:
        "As it turned out, while we were having fun on the beach, Sakishita managed to get back to camp and showed the superiors all the necessary documents."
    else:
        "As it turned out, while we were having fun on the stage, Sakishita managed to get back to camp and show his superiors all the necessary papers."
    "So all Miku had to do was dump her things in his suitcase, change into her travel suit - frivolous shorts and a tight tank top - and adieu."
    with fade
    "Words, psychology, persuasion, logic - charms - will no longer solve anything here."
    "The heat and peace reigned here - the molten air, like jelly, shrank the chaotic thrashing of reality first to a coarse shiver, and then to a calm breath."
    "Excluding the delicately turned away Sakishita, it was just the two of us here."
    "Miku looked calmly and almost painlessly into my face."
    "Said suddenly:"
    mi "I was right, yes."
    me "Regarding what?"
    show mi serious casual with dspr
    if alt_day2_mi_date == 3:
        mi "Have you forgotten our first date? I promised you that you would leave one day."
        mi "And you're leaving."
        me "But you're the one leaving!"
        "I resented it. It really did look a lot like bullying."
        mi "Not that way, silly Senechka."
        "She gently stroked my cheek."
        mi "We are apart, never together."
        mi "You took two steps in the sand beside me and went your way."
        me "Maybe I decided to run out and get you some ice cream."
        "The joke was so-so, but I had to answer something."
        mi "Don't, Seneca."
        "She said it with such wistfulness that it was obvious - long ago things were done, mistakes were made."
        "Miku was helpless and beautiful - but she accepted the rules of the game."
        me "But you're the one who's leaving."
        "Pitifully I repeated."
    else:
        mi "Never mind."
        "Unclearly she replied."
        if alt_day5_mi_7dl_voyeur:
            mi "You just didn't come true, that's all."
        else:
            mi "Perhaps we need more tries."
    scene cg d6_mi_hugs_7dl
    show gfx bokeh
    with flash
    "Step on bending legs towards me - awkward embrace:"
    mi "I wish I could stay. Not even near you, but to just see you sometimes. That would be nice, wouldn't it?"
    if alt_day5_mi_7dl_voyeur:
        mi "It's my fault, all mine - I thought that something different would be waiting for me thousands of kilometers away, something that is more than enough at home."
    mi "I wanted a friend. And I wanted not to bore him. {w}You almost convinced me it was you."
    th "You're just sick of me, silly girl."
    if alt_day5_mi_7dl_voyeur:
        extend " Ask anyone - relationships don't end after sex. I'll give you that."
    "Of course, I didn't say any of that out loud."
    "My dry throat just let it out:"
    me "I can't go on without you."
    mi "You will learn. You will find your purpose. Just don't turn your back on people, like you almost did."
    me "I don't want people without you, silly girl."
    mi "Why?"
    mi "Whyyyyyyyy?!"
    "The Japanese girl was perfectly correct, polite, and unassuming - a thick glass through which it is useless to break through."
    th "Because you're my everything! {w} I have no one else and don't need anyone else, I'll just die alone!"
    th "Because it's only with you that something good comes out in me!"
    "But I couldn't say those things in front of strangers."
    "Damn Sakishita is the culprit of all my troubles."
    "I felt excruciatingly ashamed and uncomfortable - as if someone had already rummaged through my soul and left my drawer doors open, my underwear and personal belongings scattered there."
    scene
    $ renpy.show("cg d6_mi_hugs_7dl", what = Dawn("cg d6_mi_hugs_7dl"))
    with dsps
    "I don't know how to open my soul if there's a risk of being overheard."
    "That's why I muttered into the turquoise top of her head."
    me "Because you're frumpy and naughty."
    mi "You are one yourself!"
    me "Yes, I am..."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_7dl_miku_farewell_finale:
    scene anim intro_16 with dsps
    mi "Sen'…"
    play ambience ambience_camp_entrance_day fadein 3
    "Contrary to her blooming appearance, the starlet's voice was unsure."
    "Come to think of it, just a few days ago such nuances were simply not available to me. And now..."
    mi "Why don't you come with me? Huh?"
    "The thought was so interesting that I should have considered it more closely."
    "Of course, it all depends on luck - for example, papers might not be a problem: it's very easy for me, as a man from nowhere, to concoct a legend about amnesia."
    "Or something else like that."
    "Suppose we succeed - and I, as the star's faithful companion, her first planet, the honored Mercury of the Miku system, will pomp along with her."
    "I will always be there for her. I will help her in her time of need."
    "I'll be... I'll be... I'll be... I'll be incompetent and unfit for duty."
    "I suddenly realized that the fate of a pocket penny pincher did not appeal to me at all - I found it vital to take my beloved to restaurants at my own expense."
    "And in Japan, without an education... I could only get a job as an electrician's assistant or a loader."
    show mi shy casual with dspr
    mi "I wanted to, you know: you're waiting for me backstage, a plaid and a bottle of water in my hands, warmth in my chest, and I always know I'm expected."
    "She sighed dreamily."
    th "I understand, sweetheart."
    th "And that's the only reason I'll give up now - to one day be worthy of you."
    me "You have changed me greatly, princess."
    "I replied, knowing full well that no one would ever make me a second such offer."
    me "And I would very much like to go with you."
    show mi sad casual with dsps
    mi "But?"
    "She was very clever, and she understood everything perfectly."
    me "I want us to meet when I'm can at least present something of myself."
    "That's it. Bridges are burned."
    "Of course, one could grasp at the ephemeral hope - I had always not cared about my own needs, I was extremely unpretentious about food and living conditions."
    "But suddenly it turned out I didn't give a damn about Miku, the idea of paradise in a hut froze me out completely."
    "So there's no need for any further conversation."
    "Everything else we needed to tell each other - about her, about me, about us, about plans and desires, about why Miku might never return to the Union - and ruthlessly honestly: about the fate that might await her in the future."
    "The red-hot day rolled on toward evening, and we stood looking into each other's eyes, holding hands."
    "We didn't become Us - maybe we didn't want to."
    stop music fadeout 5
    "But I do know that I will always remember Miku as the best thing that ever happened to me."
    show mi serious casual with dspr
    mi "Maybe I'll stay with you then?"
    "Pitifully, the girl asked."
    play music music_7dl["so_lonely"] fadein 3
    mi "I want where you..."
    me "That is an utopia."
    if loki:
        "No one has the right to take your dream away from you."
        "You must strive for it - and only for it in the first place."
        "Because everything else is bound to wait."
        "Including the person closest to you."
        me "I will never forgive myself if you neglect the dream for my sake, Miku."
        "I shook my head negatively."
        me "What's much worse, you'll never forgive me for that."
        scene
        $ renpy.show("anim intro_16", what = Dawn("anim intro_16"))
        with dissolve
        me "You must keep doing what you are doing."
        th "Otherwise one day a young man will not hear your voice and fall in love with the hymn-prayer of the name of the united humanity that has chosen you as its goddess."
    elif herc:
        "For a second, I even got a little mad at the naughty girl."
        me "You have to keep going! Is that clear to you?"
        me "You've told me so much about how you've straightened out your life, how you've tried for years - and what, it's all for nothing?"
        show mi upset casual with dspr
        mi "Maybe it was all meant to lead me to you."
        "A little more and she'll cry."
    else:
        "It's so easy to be a wise counselor to someone."
        "But who will advise {i}me{/i} when the meaning of existence is being taken out of me alive?"
        me "Once you compromise yourself for the benefit of those around you, sooner or later you will want your old self."
        me "It inevitably happens to everyone."
        "My past taught me just that. It'll be good for Miku to know that firsthand - from a loser a good dozen years older than her."
        me "There are no exceptions. {w}You're bound to want to sing again - and not in the shower or in the kitchen. It's on stage."
    "It was as if the evening reflected my mood - depressed, scarlet-gold."
    "As if gold and blood were the two most highly valued currencies in the world. And there was no time for us to see each other, for the wind was blowing, and it was blowing eastward, and we both knew what happens to those who go to the sun."
    "Across the valley a cloud front was rising, not yet a harbinger of autumn, but already a symptom of the breaking of midsummer."
    mi "You know..."
    "Miku began, and her voice trembled."
    scene
    $ renpy.show("cg d6_mi_farewell_7dl", what = Desat("cg d6_mi_farewell_7dl"))
    play ambience ambience_camp_entrance_day fadein 3
    "She turned sharply away from me and stared off into the distance - toward the converging straight lines on the unattainable horizon."
    mi "We have a mild-soft climate on the Pacific coast, Fuji-san holds the winds, and the transitions between seasons are more often evident in the plants than in the temperature."
    "Her shoulders trembled - but an artist is an artist - she immediately pretended to just stand like this, proudly, with her leg out to the side, and woe to whoever looks into her face now."
    mi "And you can just feel summer coming over the middle and rolling back in waves toward the southern latitudes, making way for cooler weather."
    "Her voice trembled and I didn't dare take a step and hug her."
    "I knew I would see tears, but I had no right to see them."
    me "Winter is coming?"
    "I asked jokingly."
    mi "Coming."
    "She whispered."
    "I stood next to her, looking where she was looking."
    mi "It's going to be a very long one, this winter."
    "And she turned her head sharply toward me, looking at me through her tears."
    "Large ones, hanging from impossibly long lashes, streaming down her cheeks, leaving round wet spots on her T-shirt."
    th "There's a girl crying over me again."
    "Confused, I thought."
    me "What are you...{w}Well, why cry now. Stop it."
    mi "I will."
    "Miku sniffed her nose."
    me "Don't cry."
    "At least one of us has to keep our tails in the air for two of us, right?"
    me "That's the way it was supposed to happen."
    me "I knew it. Or felt it."
    scene anim intro_16 with dsps
    "Now it was obvious to me, too - the half-panic fear that We are not eternal, and that Miku never existed at all, and therefore she comes from a place where I am barred."
    "But in the happy hours we spent together, it was so easy to fight the fear, and when the intimate things were shared, how could I, it was I who imagined that one day the person I trusted more than myself would have the adventure of returning home?"
    "Right. No way."
    "With an effort of will, I pulled myself together - even put my arm around the girl, comforting her, holding her tightly."
    if alt_day2_mi_snap:
        "This time it's not as wooden and stupid as it seemed a long time ago."
        "It suddenly occurred to me that I should take the pictures away from Boris - some kind of memory."
    show mi dontlike casual with dspr
    mi "So you knew this was going to happen from the beginning?!"
    "I nodded."
    show mi cry casual with dspr
    mi "How did you..."
    "She swallowed."
    mi "...how did you live with all this?"
    mi "My poor Senechka."
    "She pulled away - and I didn't reach after her."
    show mi sad casual with dspr
    "The sad science of saying goodbye to loved ones I have mastered perfectly."
    "Not that I aspire to be a capable student, but no one asked my opinion."
    "Pressing against me once more with all her might, Miku pulled away:"
    show mi shy casual with dspr
    mi "Will you at least wave goodbye to me through the window?"
    me "That's the least I can do."
    "Two hundred meters - two hundred of my steps, three hundred of Miku's, it was as if we were measuring our lives together, carefully folding everything into the recesses of memory."
    "And we didn't care about the mood, we held hands and paced nonchalantly, setting the tone for all that was going on."
    "From the side of the camp the wind blew the horn."
    mi "Too bad there's no way I can make it to the concert now."
    "I nodded inaudibly."
    "I didn't know how much she needed me the whole time, the thing is, I really needed her!"
    "And the grown-up uncle inside young Semyon cracked up and gave himself a vow to take the chance he was given - now there's a reason for that!"
    "One thing was disconcerting: when we meet as adults, there would be none of this anymore - no pioneer uniforms, no camp, nothing. It'll just be us and me."
    "Will it be enough for us?"
    show mi sad casual with dspr
    mi "I wish I could be enough for someone, too."
    "Quietly Miku said, and I realized that I had uttered the last phrase out loud."
    "I didn't react - I clenched my fists as hard as I could to endure..."
    "The car was beautiful and undeniably comfortable - like everything Japanese. The low heels would touch the pavement, hips would sway, the door would slam, and I would be alone with my own conscience."
    "I suddenly realized that one day the camp would close. And maybe one day they'll find in the administration building a chronicle of one silly pioneer and one wonderful girl from the Land of the Rising Sun."
    show mi serious casual with dspr
    mi "I'll go, okay?"
    "Crumpled she asked."
    "I just as awkwardly nodded. What else was there to do, I didn't understand - thoughts of a kiss or at least a keepsake flashed through my mind, but what?"
    me "Go."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_7dl_miku_farewell_soul:
    scene anim intro_16 with dsps
    play music music_7dl["you_are_soul"] fadein 10
    "I exhaled. Despair jolted in my throat with a sharp stab of heartburn: why is she stalling?!"
    "I twisted all over, only the remaining anger held me back."
    dreamgirl "Freeze!"
    dreamgirl "Stand right there, you bastard!"
    dreamgirl "Don't you dare fall to your knees! Don't you dare roll on the pavement and whine and whine!"
    dreamgirl "Hurry the fuck up! {w}A few more seconds and you won't be able to let go of each other at all!"
    "A sharp lump rolled back down my esophagus, and I wheezed:"
    me "Go on! Go! Don't stick around, jump in the car - and allure three crosses, welcome the fuck out of here!!!"
    "Turned away, clenched my teeth, feeling the enamel crumble."
    mi "Senechka..."
    show mi cry_smile casual
    me "Go! Go away! It's hurting me while you're here, don't you understand?!"
    th "Why am I yelling at her?"
    "Faintly I wondered."
    hide mi with dissolve
    "But I guess that was what it took - Miku obediently headed for the car."
    me "Fucking go!" with vpunch
    scene stars
    $ renpy.show("cg d5_mi_conv_7dl", what = D3_intro("cg d5_mi_conv_7dl"))
    with dissolve
    $ set_mode_nvl()
    if alt_day2_mi_date == 3:
        mi "{i}I told you that everyone I love leaves one day. And so will you. {w}Remember what you said back then?{/i}"
        me "{i}That it's up to me{/i}."
        mi "{i}Does that mean you're leaving now because you've made up your own mind?{/i}"
        "{i}When she asked me questions like this…{/i}"
    "{i}I looked away guiltily.{/i}"
    mi "{i}So I crushed you by responsibility. Miracle turned out to be an ordinary boy, just like everyone else... I thought maybe if we got closer…{/i}"
    nvl clear
    mi "{i}Nothing had changed. And why, one wonders, was it necessary to go far away for something that is abundant at home?{/i}"
    me "{i}I do not consider what happened to be a mistake.{/i}"
    mi "{i}I just... I also wanted that. You just didn't come true. I'll never forgive you for that.{/i}"
    nvl clear
    scene anim intro_16
    with dissolve
    $ set_mode_adv()
    "Fragile shoulders shuddered once more."
    "Inhale."
    "Exhale."
    "And from beneath her fluttery, kilometer-long eyelashes opened, an aquamarine smile of muse and idol in one person."
    "The new Miku."
    "A doll that has nothing in common with my Miku."
    mi "I will remember you every day."
    me "Miku. A moment."
    scene cg d6_mi_departure_7dl with dissolve
    mi "What?"
    "I was frantically going through my pockets."
    me "Here! Here."
    "The first thing that came to hand was the phone."
    me "To remember!"
    mi "Are you sure?"
    "I nodded silently."
    mi "Then goodbye."
    scene anim intro_16
    with dsps
    "Turned around and walked past me into a waiting Mitsubishi."
    play sound sfx_intro_bus_engine_start
    "The man behind the wheel saluted me and, turning around on the patch, brought the car out onto the road."
    "The whole time he was turning around, that the car was unhurriedly sticking to the horizon, I tried to get a good look at Miku."
    "But she was frozen in the back seat with a perfectly straight posture, looking straight ahead."
    "Whether she hates me or not doesn't matter now."
    "The most important thing is that she will do what she does best."
    $ alt_day6_mi_7dl_left = True
    me "One day you'll thank me."
    "With only my lips I said."
    "And I staggered back to camp."
    "I'm sure she never looked back."
    stop music fadeout 5
    stop ambience fadeout 5
    scene bg ext_stage_big_clear_day_7dl with dissolve
    play ambience ambience_camp_center_evening fadein 3
    play music music_7dl["gonna_be_ok"] fadein 3
    "Miku had a few windows set aside for her performances."
    "She had a few songs - for the mood, for the smiles, for the audience..."
    "For me."
    "And so she wouldn't be accused of being greedy for pop time, she wrote those windows under other people's names."
    "Mine, for example."
    "I don't think there would have been any problem with that - performing was as natural to Hatsune as breathing."
    "The only problem is that she's absent from the compound."
    "She was picked up and taken to fairy tale land by a gaunt Japanese man with impeccable manners who didn't like her for a second."
    "Problem number two is the lack of even minimal training in the burdened 'Potemkin numbers.'"
    "No one planned to perform, and certainly no one prepared anything."
    "I counted five of them, including myself."
    "Looks like my princess had a gift for persuasion."
    "Anyway, the line got to me."
    show mt sad pioneer with dspr
    mt "I'll strangle Hatsune."
    "Sadly, the counselor complained into the void."
    mt "Blatant carelessness. {w}Semich, are you one of those asked too?"
    "I shrugged."
    mt "I see."
    "The pencil sharply scribbled down the list."
    me "Hey, wait a minute! I didn't say I wouldn't perform!"
    show mt surprise pioneer with dspr
    mt "Would you?"
    "I wiggled my shoulder indefinitely."
    mt "Maybe you have a performance rehearsed, too?"
    me "Not really."
    show mt angry pioneer with dspr
    mt "What are you going to do on the stage, let me ask you?"
    "Our exciting quiz was beginning to make the counselor angry."
    "To be expected."
    me "I'm going to read a poem."
    "I briefly replied."
    mt "No obscenities, I hope, or woe is you!"
    me "No."
    hide mt
    with fade
    "After hesitating for a while, Olga stepped aside - another comrade with a fake performance was waiting for her besides me, and she needed something to plug the hole in the program."
    "And mine was still five minutes away."
    "The Russian folk dances from the fourth squad - with the carousel and the girls in sundresses - fit in there nicely."
    with dissolve2
    "But time is inexorable."
    "It took me a long time to choose an unpretentious poem, from contemporary poets to the Silver Age."
    "But the same lines went on and on in my head."
    stop ambience fadeout 5
    scene bg ext_stage_near_clear_7dl with dissolve
    play music music_7dl["meetmethere_tts"] fadein 3
    "At last my tormented consciousness caught a glimpse of the announced name, and, slouching, I strode toward the stage."
    "I cursed the idea three times - the feeling was exactly the same as it had been at the line."
    "Why did you volunteer, you fool... Why?!"
    "I categorically do not accept any publicity. When you're in a group, it's all right."
    "But on my own, alone with an audience..."
    "Hundreds of eyes stared at me in anticipation."
    "They wanted an interesting show, they wanted flying sleeves of warmers over the stage, short skirts and chiseled broken rhythms with Japanese accents on top."
    "How could I compete or hope to replace that?"
    "Replace Miku?"
    "Laughable, really."
    "The silence lingered."
    voice "Read!"
    "A voice came from the audience."
    "And I shuddered."
    "I wanted to bring something light and joyful to the farewell concert."
    "But in my mind, the same lines went on and on and on."
    "And, clutching at the microphone stand, I mumbled:"
    me "{i}Speeches without thoughts, people without faces... The heated arguments of the deaf and the blind…{/i}"
    me "{i}Hear that? To the sound of cemetery birds, the dead wake their dead.{/i}"
    me "{i}They splash your eyelids with bloody dew - you'll shudder, you'll see, and you'll see, grieving…{/i}"
    with flash_red
    with vpunch
    "At that very moment, the spiral that was clutching me twitched for the last time - the string stretching harder and harder into the unknown finally broke."
    "And I, in perfect agreement with the lines, had an epiphany."
    "That all my actions now meant absolutely nothing."
    "That my moon princess had simply disappeared. I pushed her away."
    "And all the poetry in the world won't bring her back."
    $ set_mode_nvl()
    scene stars
    $ renpy.show("anim intro_16", what = D3_intro("anim intro_16"))
    with flash_red
    play sound_loop sfx_intro_bus_engine_loop fadein 3
    "The pain was terrible - dying hope always tends to poison one's surroundings."
    "Despair sometimes makes you do the most desperate things."
    "So I stopped reading."
    me "Sorry, wrong poem. I'm sorry."
    "I could no longer see faces, they merged into a single fuzzy blur with ever-changing outlines."
    "Into a moving blur somewhere with turquoise edges."
    nvl clear
    scene stars
    $ renpy.show("cg d6_mi_departure_7dl", what = D3_intro("cg d6_mi_departure_7dl"))
    with dspr
    me "I learned this poem when I was twelve years old - a lot of time has passed since then. But some of it I'm only beginning to understand now."
    me "I hope you will someday understand it, too."
    nvl clear
    me "{i}Wooden hands and feet. Wooden official tongue.{/i}"
    "Before my eyes came images from memory - the warm spring sunshine, the sagging couch in the library, and the magazine 'We' from, I think, 1992."
    me "{i}And also this scarf is miserable, and under it - like a stone - an Adam's apple.{/i}"
    "I didn't like to read poetry - that's for sure. But specifically in these thirteen lines I discerned the Answer - why do people hate each other, why are they rude to those they would like to hold to their bosoms..."
    "Why do we kill those we breathe on with fear?"
    nvl clear
    me "{i}I'm a wretch... You're a god! I wish someone would yell 'save me!'{/i}"
    me "{i}But no one is robbing anyone, smiling like a pathetic beggar.{/i}"
    "I didn't turn out to have a happy deliverance from a hard conversation, either. {w}And I am so fond of delaying unpleasant conversations."
    "That's why my 'deity' disappeared."
    "A line-association, bitter from giving up everything myself. I hate myself for it!"
    "Apparently I managed to put all the anger at myself into my voice - because the next lines sounded especially honest."
    nvl clear
    scene
    $ renpy.show("cg d6_mi_departure_7dl", what = Notch("cg d6_mi_departure_7dl"))
    with dsps
    me "{i}For my mediocrity, for my timidity, I hate myself - and I am cheeky.{/i}"
    "Wouldn't it be great if now the brakes squeaked at the gate and a frail figure in shorts and a T-shirt, with long hair gathered in two long, long ponytails, appeared behind the spectators' backs!"
    "That would have been cool..."
    me "{i}I love you, holy love!{/i}"
    scene
    $ renpy.show("cg d6_mi_leaving_7dl", what = Desat1("cg d6_mi_leaving_7dl"))
    with dissolve2
    "I shouted into the soulless sky."
    "Do you hear me? I'm an awkward fool, but I need you."
    "A belated confession solves nothing, frankness was bought at a throwaway price."
    "My voice had completely changed, so I spoke the last lines in a half-whisper."
    me "{i}And in your face I smoke brazenly…{/i}"
    nvl clear
    stop sound_loop fadeout 1
    $ set_mode_adv()
    scene bg ext_stage_near_clear_7dl with dsps
    me "Because I {w}{b}admire you{/b}."
    "Do you understand? I push you away and kill you because I'm ready to carry you in my arms."
    "Because I..."
    stop music fadeout 5
    scene bg ext_stage_big_clear_day_7dl:
        xalign .5 yalign .5 zoom 1.0
        ease 0.5 zoom 1.3
    "I jumped off the stage and ran for my life."
    "There was silence in the audience rows - my sincerity was unclaimed."
    "Of course, no car stopped anywhere, and no beautiful girl with long, hypnotizing tails of hair ran screaming my name."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_7dl_miku_farewell_star:
    scene anim intro_16 with dsps
    me "I will remember."
    mi "Yes..."
    play music music_7dl["forgive_or_what"] fadein 10
    with fade
    mi "It's okay."
    me "It's all right."
    "Unnecessary, stupid words that stupid people say to each other, afraid to cry, saying goodbye forever."
    "Why, who came up with the idea that it's embarrassing to cry when the person most important to you just gets in the car and drives away?"
    "Why do you have to be embarrassed and turn away and say in wooden voices anything but what's really necessary and appropriate?"
    "Aren't we just going to carry all this nonsense away with us as our last memory?"
    "And the aftertaste of familiarity will be poisoned by these cardboard manners - the thought that since she was so calm - that since he was so calm..."
    "We stood there, staring into the asphalt, angry at ourselves, embarrassed, clenched fists."
    show mi sad casual
    with fade
    me "In fact - nothing is right."
    mi "I know."
    me "But one day we'll make it so that it's up to us to decide."
    mi "Yes."
    me "You don't say much..."
    mi "Because I have too much to tell you. {w}And time is too short."
    mi "That's why... {w}I've wanted to tell you for a long time..."
    me "What?"
    show mi shy casual with dsps
    mi "N-no. {w}Nothing."
    me "Then - goodbye, and not «farewell»?"
    mi "See you soon."
    "Her smile was sad."
    scene anim intro_16
    show mi smile casual
    with dissolve
    "Two steps back, she turned around sharply:"
    mi "Cheer up, Senka!"
    mi "Friends should not part with sour faces!"
    me "Yes. {w}Yes, of course."
    mi "Everything's okay! Do you hear? We'll definitely see each other again, I promise!"
    me "Yes..."
    mi "But you have to try your best, too, okay?"
    me "I see..."
    mi "Can't hear?"
    me "I see."
    mi "Can't hear again?"
    show mi happy casual with dspr
    "Miku turned to me half-turned, put her palm to ear in a makeshift funnel."
    mi "What are you mumbling about?"
    me "I'll try!"
    "I roader."
    mi "That's better!"
    mi "I'll remember you, Senka!"
    scene cg d6_mi_cya_7dl
    $ renpy.show("gfx bokeh", what = D3_intro("gfx bokeh"))
    with flash
    "Miku saluted me with the international sign of peace."
    mi "Cheer up, Senka! All is well!"
    scene cg d6_mi_cya_7dl with dissolve
    pause(1)
    play sound sfx_intro_bus_engine_start
    scene white with flash
    "She jumped into the car, slammed the door behind her, all without turning around."
    "And then, as the Mitsubishi turned around in the nickel - Miku knelt on the back seat and waved to me through the back window for a long, long time."
    me "See you soon, princess."
    "I smiled."
    $ alt_day6_mi_7dl_left = True
    "I felt sad, but surprisingly bright."
    "Soon the car became a barely discernible dot on the horizon, and the horn sounded from the camp."
    "Don't ask for whom the knell tolls - it's for you."
    play music music_7dl["so_lonely"] fadein 3
    scene cg d6_mi_leaving_7dl
    show anim_grain
    with dissolve
    play sound_loop sfx_bus_interior_moving
    "In my old world, of all the Miku songs I was able to remember, the one that impressed me the most was a song called 'The Disappearance of Hatsune Miku.'"
    "A bittersweet tale of an electronic tiny life that knows nothing but how to sing, sees the doom of its world - and tries to make it in time."
    "To have time..."
    dreamgirl "To sing that song!"
    "The image of Miku looking out the window and the power line towers flying by, reflected in the bent Japanese glass, stood and stood before my eyes."
    "She was trying so hard to show me that all was well, I could barely believe it myself."
    "Even though it tears my heart out for every meter that passes between us."
    "I have life and will - I'd give half to feel sweet Miku in my arms again - and I won't be shy or afraid of anything this time!"
    "I'll hold her to me as tight as I can, say all the things I haven't had time to say."
    "And kiss her at last - properly, no position comedy."
    "I would give her without hesitation."
    scene
    $ renpy.show("cg d6_mi_leaving_7dl", what = Desat1("cg d6_mi_leaving_7dl"))
    show anim_grain
    with fade
    "And on the other hand I'm well aware that I'll be the first to chase her away."
    "Because she should be there - at the record company hall, at the label, that one day will release a record with an aquamarine girl floating on the waves of music."
    "And next she'll have everything she's ever dreamed of."
    me "Goodbye, princess."
    "I whispered."
    me "Farewell. And may fortune never leave you."
    with fade
    "The soft voice, the short dresses, the dancing, instantly going around the world like trends."
    "Do you know how many girls born in two thousand sixteen were named Miku? You wouldn't believe it..."
    "Although it's not hard to make a prediction on that topic either - can you hear the audience murmuring and breathing?"
    voice "Mi-ku! Mi-ku! 39!"
    "They're chanting."
    "Or are they not chanting?"
    "In my mind, the noise of the voices of hundreds of exalted fans merged and fused into one..."
    stop sound_loop
    stop music fadeout 3
    play ambience ambience_lake_shore_day fadein 3
    "Into the noise of the surf."
    scene bg ext_boathouse_day
    with flash
    "It turns out that while I was dreaming in reality - I managed to walk through the camp and freeze on the dock, catching the steel bars-rails tenaciously with my oak hands."
    "Water was supposed to cleanse the soul."
    "But water is aqua, and aqua is always marina now; instead of redemption you get some obscenity and another batch of self-pity."
    "With a snort, I shook my empty head, putting my thoughts in order."
    "Our summer is barely past its sixth day, and it's no longer ours."
    "It's moments like this that make you think that Paine's 'there's no us in this' is most painless."
    "And the eternal grimace on the lips of the despiser of penniless comfort is essentially just a manual for safety and purity of soul."
    "You can't get attached to anyone - because they're not forever."
    "No one can be trusted - a loner cannot be betrayed or set up."
    "But except that the world in such rules is ugly like my native reality."
    me "An easy road, a warm rain, and inspiration between the lines - in idle heads and in moments of hard work."
    "The air is filled with the smell of fresh water and sedge and heated planks of decking - and over the open water the voice is still as crisp and clear."
    me "I'm lonely without you."
    "Damn Japanese bitch."
    "Echoes came after a few seconds:"
    "Ely-ely-ely-ely-ely... out you..."
    show mt normal pioneer with dspr
    mt "Semyon, come up to the stage, a farewell concert."
    "Olga Dmitrievna came up in her usual silent style."
    "And she was dressed in her usual dailies - doesn't she plan to dress up for the concert?"
    "She was holding some kind of blue folder with ties in it."
    me "What did I forget there?"
    show mt surprise pioneer with dspr
    mt "What do you mean?"
    "The squad leader was surprised."
    mt "Aren't you going to perform?"
    "I shook my head in the negative."
    show mt angry pioneer with dspr
    mt "Look, of course I understand you - you're upset about your friend's departure, but that's no reason to let your comrades down, and..."
    me "How am I letting them down by standing here?!"
    "Angrily I grumbled."
    mt "And so, if you signed up for the program, you have to do it, no matter how sad you are a hundred times."
    show mt normal pioneer with dspr
    mt "This is not serious, Semich. It's not dignified. {w}Big boys don't act like that."
    me "But I didn't sign..."
    "I shut up."
    "I remembered..."
    "Not everything, of course, but some things."
    me "So this crazy woman put me on the list after all."
    "Somehow there was no surprise at all."
    "It must be because it's very logical to expect nastiness of this caliber from Miku."
    mt "So, are you coming?"
    "I twitched my shoulder."
    me "No. I have no performance, no costume, no rehearsal."
    me "What am I going to do once I'm on stage? Read a poem?"
    "The counselor shrugged her shoulders:"
    show mt smile pioneer with dspr
    mt "That'll be good enough. So?"
    me "No, Olga Dmitrievna, I'm sorry, but I'll pass."
    show mt sad pioneer with dspr
    "With a sorrowful pursing of her lips, Olga opened the folder and crossed something out on a piece of paper lying at the very top."
    if loki:
        "I might have been able to smooch something on a trumpet - if I could find one in the back of the motherland."
        "But there was no desire at all."
        "None at all."
    if alt_day2_mi_snap:
        "She was just about to leave and leave me alone when she suddenly remembered something."
        show mt normal pioneer with dspr
        mt "Look, I don't know how you're going to take this, but I think it'll cheer you up."
        "As she opened the edge of the folder, she put her palm up - and a picture card slipped into her hands!"
        mt "Here you go!"
        scene
        $ renpy.show("cg d2_mi_me_polaroid_7dl", what = Sepia("cg d2_mi_me_polaroid_7dl"))
        show PolaroidFrame_7dl
        with dsps
        "That was the picture! Here's the Japanese beauty, smiling with all thirty-two - and here's an embarrassed and hunched over me, putting my hand on her shoulder."
        mt "A keepsake!"
    scene
    $ renpy.show("bg ext_boathouse_day", what = Dawn("bg ext_boathouse_day"))
    with dissolve
    "After saying goodbye to me with a nod, she walked away from the pier - Moscow time was approaching five o'clock, and, unlike me, the counselor was clearly going to take part in the action to come."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_7dl_human_day:
    scene anim prolog_1
    $ timeskip1 = "Two hours later..."
    show alt_credits timeskip1 at truecenter
    with joff_r
    pause(4)
    scene bg int_aidpost_day
    with blind_l
    play ambience ambience_medstation_inside_day fadein 3
    play music music_7dl["kiss_you"] fadein 3
    "Same people, same place."
    "The frightened adults instantly lost all their aplomb and moralizing tone as soon as I caught Miku in my arms."
    "{i}Nothing supernatural.{/i}"
    "{i}The most common nervous fainting.{/i}"
    "{i}The victim was prescribed rest and sleep.{/i}"
    "I love our nurse - getting us out of the fire so gracefully..."
    "Though of course she had heard the rumors - how not to be when the whole camp was talking."
    "And pointing a finger at my back as I carried my priceless cargo."
    "Cargo, smiling faintly through oblivion."
    "So they got off us."
    "Temporarily, of course - I'm convinced everyone's just waiting for Miku to be picked up by her agent so they can ream my ass."
    with fade2
    "But as long as I have time, same people, same place."
    if alt_day_binder == 1:
        "Only this time we switched places somewhat."
    "With a chuckle at that thought, I pulled a chair over to the couch and gathered myself for a vigil."
    show cs normal with dissolve
    cs "You don't have to keep your eyes on her at all, pioneer."
    "The nurse reported."
    cs "She just got a little nervous."
    me "How can she be nervous, she's a public figure!"
    show cs shy with dspr
    "Viola grinned, but mercifully declined to comment on me."
    "When she finished entering us in the admissions log, she leaned back contentedly."
    cs "You're so holding on to her..."
    "Softly, half-questioningly, she said."
    show cs normal with dspr
    cs "You know this isn't going to work, don't you?"
    me "If we don't try, we won't know, right?"
    cs "Also true."
    "She stood up."
    cs "Slam the door when you leave - I'm going to the beach. Adios."
    hide cs with dissolve
    "And it was just the two of us."
    with fade
    "Miku lay quietly on the couch and didn't look anywhere while I studied her profile."
    me "Hey, Miku!"
    "I called out."
    me "Mi-ku!"
    "No answer."
    me "Mikuska-barabuska, your zipper is unzipped!"
    "She is silent and lying there like a corpse. Though it would seem - what does the zipper on her skirt have to do with it?"
    "With a sigh, I left the Japanese corpse behind and muttered a counting rhyme to myself."
    me "As I walked through the woods and the bridge, I saw a seagull drying up. I threw it into the river and let it soak."
    "And!"
    me "I walked through the woods and the bridge, and I saw the seagull getting wet. I put it on the bridge and let it dry there."
    "And!"
    me "I was walking through the woods and the bridge, and I see the seagull is drying..."
    "It didn't take ten minutes before Miku was finally sick of it and decided to come to her senses."
    mi "I threw her out - let her die there!"
    "Angrily she continued the rhyme."
    show mi dontlike pioneer with dspr
    mi "Senka, why are you picking on me! Can't a man even faint anymore!"
    "She asked indignantly, sitting down on the couch."
    me "You can, you can! As much as you like."
    "I rejoiced."
    me "But next time it's my turn to faint - and you'll carry me in your arms to the infirmary!"
    show mi shy pioneer with dspr
    mi "I won't be able to lift you!"
    "She reported."
    me "That's... a shame! Shame!"
    "I reported."
    me "What do we do now?"
    "Miku wondered - she either didn't seem to know that I was teasing her at all, or if she was playing along..."
    "Or she was so used to being teased all the time that she didn't even pay much attention."
    "And as soon as that fact reached me, I felt the blood rush to my cheeks."
    th "I don't seem to have changed one bit for the better."
    show mi normal pioneer with dspr
    mi "Senechka, what did the teachers' council decide?"
    me "Nothing."
    "I reported:"
    me "You passed out in a very timely manner."
    mi "So everyone's just waiting for me?"
    me "Not really."
    me "The adults decided that since you were getting out of camp in a couple of hours anyway, there was no reason to spoil the rest of your vacation time."
    show mi happy pioneer with dspr
    mi "That's great! So I don't have to lie here at all?"
    me "Yeah, I guess not."
    mi "Great! Then let's make the most of the situation!"
    me "How's that?"
    show mi smile pioneer with dspr
    mi "Let's run out of the territory!"
    th "Hmm... She'll be gone in a couple of hours, and I still have to live here until tomorrow."
    th "I guess I should admonish her - after this morning she's already living on the house."
    me "Yeah, sure. Where do you want to go?"
    "Did I mention I'm extremely logical?"
    play music music_7dl["you_are_human"] fadein 2
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg ext_sky_7dl with dissolve
    play ambience ambience_camp_entrance_day fadein 3
    "We came to the gate, where it was still quiet, quiet - and no evil wizard had yet appeared to steal my princess from me."
    "It's always so quiet and peaceful here."
    "Miku shook off the curb and sat down on the sun-heated concrete, and I stretched out on the grass beside her."
    "The sky was red-hot, and it seemed unfair that one magical story was about to end - nothing up there would even change."
    th "I will whine and pity and suffer for hundreds of hours."
    "It suddenly occurred to me."
    th "I'll write another notebook of poems, get my guitar or paintbrush back in my hand - an excuse for my own cowardice, that's all."
    "Miku was looking where I was looking."
    mi "Look, Venus."
    "She suddenly said."
    mi "Do you think... Can you see it in Japan now?"
    "I estimated the time zone difference and nodded in the affirmative."
    mi "I'll look at her in the evenings - like a reflection: what if you look there too one day."
    "I doubted Miku would be up to any nonsense now, staring up at the sky just like that would be a long time away..."
    me "Write another song."
    "I rudely offered."
    mi "I will."
    me "Then do it. Then sing it to people - let them know about your unique thoughts."
    mi "Sen, what are you doing?"
    "I waved it off."
    me "Don't mind me. You should be getting ready, writing albums, and here I am with my negative thinking and selfish pretensions."
    me "Sorry. {w}I totally ruined your last hours before departure."
    scene bg ext_camp_entrance_day
    show mi normal pioneer
    with dissolve
    mi "Sen..."
    "Miku touched my shoulder."
    mi "I'm not going, Senya."
    "The air rose in my throat."
    me "W-what do you mean?"
    "I whispered back."
    show mi serious pioneer with dspr
    mi "I'm not going home with Sakishita."
    "Obediently Miku repeated."
    me "Why?"
    "I asked, not recognizing my voice, which had suddenly become husky and brittle."
    mi "Changed my mind. I'm a fool, aren't I?"
    "The Japanese girl smiled."
    th "Fool? No..."
    "Of all the feelings I felt for Miku, perhaps the strongest was sympathy."
    "But the honorable second place was suddenly occupied by something I'd almost given up feeling."
    "Respect."
    th "I see you as a Human, Miku."
    th "Not an empty-eyed anime puppet."
    th "And that's why you have to live your own life, your own life."
    th "Not what others expect of you."
    th "Remember that."
    th "But what if it's just a teenage bliss?"
    me "What about Sakishita, the album, the music... Miku?"
    mi "They'll manage without me for a day, they're not little kids."
    th "Maybe it's somehow my fault?"
    "It went through my head."
    th "Constantly pushing and pushing her, making her think about the election."
    me "Sakishita will twist you before you can squeak."
    show mi laugh pioneer with dspr
    mi "He can try."
    "The girl laughed."
    mi "Did I go to Shotokan for four years for nothing?"
    "That girl was acting weirder and weirder!"
    me "Listen, Miku!"
    "My voice sounded pathetic."
    me "But you yourself remember that it is important to you for your career, and you yourself prepared me for two days in a row not to throw a tantrum at the goodbye! And now you've changed your mind?!"
    show mi grin pioneer with dspr
    mi "Yes, I knew you'd be upset."
    me "I mean it!"
    mi "Me too. I couldn't be more serious."
    show mi normal pioneer with dspr
    mi "Of course, I'd like to go to Japan in time for the record. Music is my life! It's all I know, all I know how to do!"
    mi "Do you understand?"
    "I nodded:"
    me "I understand. I mean, I understand how much this opportunity means to you, but there's something about your behavior I don't understand at all!"
    show mi sad pioneer with dspr
    mi "You see... All my life I've been going with the flow, all my life I've been looking for salvation in something that gives itself, floats in my hands."
    mi "I was bullied at school - I followed my father into another school. I never had the anger I needed to hit an abuser."
    mi "Much later I realized that all the people, all the people around me - they are not my friends at all, they don't have to be with me 'Nice&Kind,' as our English teacher puts it."
    mi "Don’t ask me how my fear of hurting others got along with my respect for one’s rights to act like a creep or an utter bastard. Somehow, these two got along."
    mi "Then music."
    mi "Then UNICEF's special school - my former classmate Megurine came there with me, she turned out to be a nice girl."
    mi "The other guys were great, too - but I had already learned to doubt when 'it's too good.'"
    show mi upset pioneer with dspr
    mi "Especially since it kept falling into my hands without any effort on my part."
    mi "And then you showed up. And started asking the questions that I kept asking myself - will I be a slave all my life? Am I going to breathe and love and live by someone else's orders? I don't want to."
    show mi shy pioneer with dspr
    mi "This is the most independent thing I've ever done - and gods know, it won't be the last."
    "I closed my eyes and let my heart beat - I heard what I wanted to hear: what I had thought all my life was the most important part of life."
    "A half-forgotten feeling awoke in me in uncontrollable jolts - my breath was taken away by the anticipation of what Miku was capable of."
    "Not knowing where to put my hands, I squeezed and unclenched my fingers until a narrow, cool palm covered them."
    mi "I also want to dance with you tonight. You don't mind, do you?"
    me "I do mind, of course."
    "I replied. For some reason I felt ashamed and scared that I was about to start acting stupid and saying stupid things."
    "I've forgotten how to be happy, I've forgotten how to be happy at all."
    "But I couldn't keep quiet either."
    if alt_day3_mi_7dl_donor:
        me "So you decided to go shopping with me in Leningrad after all?"
        show mi smile pioneer with dspr
        mi "Yes."
        mi "I want you to hold my hand, buy me hot dumplings at the doughnut shop, help me stand on my roller skates, and then wait by the phone for me to call."
        mi "Ai kotoba..."
        mi "I'm in love, Senya, aren't I?"
    else:
        me "You don't hit the window, so it's unclear when you'll record the album at all?"
        mi "I don't care."
        "The Japanese girl shook her head."
        mi "I love music, and going to the microphone like I go to work is a sure way to kill the love of music in me."
        mi "And anyway, I want to travel around the Union, maybe I'll even study here."
        me "Where will you study, you onion woe?"
        show mi happy pioneer with dspr
        mi "I don't know."
        "Just answered this kid."
        mi "Somewhere where you'll be around. You will be, won't you?"
    me "I don't even know..."
    "I wanted to squeal with delight."
    "And Miku grumbled indignantly and threw me into the grass."
    "We were the happiest."
    "Who would ever have told me that one day that short word would contain me - and the girl who had never been in my life, who I simply never had the chance to meet..."
    mi "You're a big buka, Seneca."
    "Declared Miku."
    me "Buka as in ugly?"
    show mi laugh pioneer with dspr
    me "Because I am ugly?"
    mi "No. Buka is like evil in the flesh. And evil must be punished."
    mi "So I decided to stay - to make it more convenient to punish you."
    "Hafu bumped my shoulder with her forehead and purred contentedly."
    "We had dusty asphalt, mush by the roadside, and the most endless sky."
    "And we hardly paid any attention to the retreating footsteps."
    "The engine bellowed softly, the tires screeched across the asphalt, and the dark blue Mitsubishi drove off into the heat."
    "Only Miku, after waiting a few minutes, uttered an incomprehensible:"
    mi "Itterasshai, Sakishita-san."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_mi_7dl_catapult:
    scene bg int_dining_hall_people_sunset_7dl with dissolve
    play ambience ambience_dining_hall_full fadein 3
    play music music_7dl["youre_not_real"] fadein 3
    "On that funny note, let me end our song about the relationship between Guest Star and one bearded pioneer."
    "No worse than any other, by the way."
    "Anyway, knowing my own karma, that's what I expected from the beginning."
    "We were so successful at fending off the attacks of those around us, so cooperative, so game to fend off accusations like 'tilly-tally-tally-testo'..."
    "So naturally the thought that floated into my mind, 'and yet I was completely lost,' I took as an extension of my relationship to my best friend."
    "With a pair of infinitely long, azure-colored tails."
    "To a friend who was successfully impersonating either a machine gun or a blonde."
    "Except he stumbled for half a second and gritted his teeth in response to Olga's sympathetic look."
    $ renpy.show("cg d6_mi_leaving_7dl", what = D3_intro("cg d6_mi_leaving_7dl"))
    show anim_grain
    with dissolve
    play sound_loop sfx_bus_interior_moving
    th "Miku... One day wouldn't solve anything, would it?"
    th "We both know that."
    mi "Sen, have a conscience. Live, be happy, and - what did you say? - get on with it."
    mi "They won't let a man leave anymore."
    th "But surely we shall see each other?"
    "I asked wistfully."
    mi "What am I to you, the Pythia or the Meteobureau? Exactly... Pfft. {w}Nobody's going to tell you anything for sure. Nobody."
    mi "Okay, see you soon - I have a flight in seven hours, we can barely make it to Moscow in time."
    "She reached out to me, touched my cheek with ghostly lips - a cool breeze with eucalyptus notes brushed my skin."
    "And disappeared."
    play sound sfx_open_door_2
    pause(1)
    stop sound_loop fadeout 3
    scene bg ext_dining_hall_near_sunset with dsps
    play ambience ambience_camp_center_evening fadein 3
    "What am I supposed to do now?"
    "Make up for the dance - and who for..."
    "I began to consider what I had not yet done, or what I had promised to whom I had not fulfilled."
    "It turned out I had no unfinished business or unfulfilled promises."
    "Well, of course there were, but any of them made me sick to my stomach."
    "Everything seemed boring, dull and tedious to the point of nausea."
    "It happens that way. Powerless weakness, emotional stalemate."
    "It made me want to be five-year-old Semka and go complain to my mother about the stupid world."
    if herc:
        "Not with my medical history."
    "I haven't smoked in ages, but in my old life, when it was painful to straighten my collapsed lungs after sleeping, I was addicted to 'overhead' breathing."
    "Almost like cholotroping, only it allowed me to deal with any amount of pain."
    "Inhale."
    "Exhale."
    scene anim_square_preparty with dissolve
    play ambience ambience_camp_center_evening fadein 3
    "Everything in the square was ready for the final dash into tomorrow - toward the dusty, gasoline-smelling miles on the road home."
    "A mere trifle remained."
    "To pay my respects and give away my debts: to dance till I get hiccups, get high till I get heartburn, and finally hold the girl I made eyes at all my shifts."
    "Hydrants waiting for heated heads, secluded corners waiting for smoke and reckless in honesty conversations."
    "Only I don't belong to it all."
    "Somehow I've outgrown it all, and there's no turning back."
    with fade2
    "Gently I think of Miku's songs, I think of her videos, I think of who she is in my world."
    "The avatar of an electronic deity that never comes to life, despite the aspirations of a multimillion-dollar aggregor."
    "A fictional incarnation of the synthesizer."
    "My Miku - in my world, she wasn't even born yet at this time."
    "And then who is she, this Hatsune Miku with the face from the commercial that broke the popularity record, provoking tears of pangs of happiness - of a sense of {i}complicity{/i}?"
    "How did our fantastic meeting, our unfulfilled friendship, become possible? Huh?"
    "I don't know the answer and probably don't want to know."
    "Because the wonder of our tiny summer will wither and crumble into clichéd phrases if you try to dissect it."
    "I'd rather just remember it as a maddening pre-dawn dream, carrying the chill of an unfulfilled kiss and the warmth of a miniature hand around my little finger."
    show sl normal pioneer with dspr
    me "Oh, hello..."
    "I muttered as Slavya sat down next to me."
    sl "Semyon, we need to talk."
    me "Speak."
    show sl serious pioneer with dspr
    sl "Can we go away? {w}I don't want to be heard."
    me "What's with all the secrecy games?"
    hide sl with dissolve
    "I grumbled, but obediently followed the activist."
    play ambience ambience_boat_station_day fadein 3
    scene bg ext_boathouse_sunset_7dl
    show sl normal pioneer
    with dissolve
    sl "Here, this will be fine."
    "There was a bag on the sand beside her, and I thought I heard a slight stirring in it."
    th "Caught someone or something..."
    "I thought without interest."
    show sl shy pioneer with dspr
    sl "Look, I'm sorry things turned out so stupid with you and Miku."
    th "And how sorry I am, you know..."
    show sl sad pioneer with dspr
    sl "No, don't think I'm prying or gloating, but it just occurred to me, since you're alone, and..."
    "She stopped talking."
    with fade
    "I was silent, too."
    "After thinking for a few seconds, Slavya clarified:"
    sl "So, I think I said something wrong and very wrong, didn't I?"
    me "That depends on what you want."
    "Evasively I replied."
    show sl smile pioneer with dspr
    sl "Don't think I'm trying to be a girlfriend or anything..."
    "She took a few deep breaths and then looked me straight in the eye:"
    show sl normal pioneer
    sl "Semyon, from what year did you get here?"
    "I got the cold between my shoulder blades."
    "If all I've had to do up to now is not ask too many questions and maintain a pioneer's reputation."
    "The fact that someone is in a position to blow my whole gambit with one well-chosen question has never been warned anywhere!"
    "Not even in the fine print."
    me "What do you mean, from what year?"
    "I mumbled."   
    show sl sad pioneer with dissolve
    me "From Genda's three millionth birthday, of course."
    sl "Semyon."
    "The impossible girl gave me that mature look."
    sl "Don't play dumb. {w}You don't know anything at all, it's impossible to confuse you with the locals."
    me "I haven't been like the locals yet."
    me "I'm not so bad at being a local either."
    "Slavya shook her head thoughtfully."
    "I did behave very unnaturally for a man who has nothing to be accused of."
    show sl normal pioneer with dspr
    sl "Look, I didn't mock you by asking questions about the current general secretary or things obvious to my contemporaries."
    sl "But that's no reason to mock me in return."
    "She pulled out of her pocket and shook a familiar brown leather-bound book in front of my nose."
    th "My passport!"
    "I gasped."
    if alt_day_binder != 1:
        th "I thought the coat was gone..."
    me "And you're preoccupied with corpus delicti, I see."
    me "Prudent, aren't you?"
    with fade
    me "Are you going to blackmail me now? {w}Okay, what do you want?"
    show sl angry pioneer with dspr
    "Slavya stopped smiling altogether - she extinguished her inner sunshine."
    sl "Now I can see that you really are from another life here."
    "Quietly she said."
    sl "You're always expecting meanness from people... {w}How did you survive?"
    me "I tried. {w}All right, you caught me in the act and forced me to come clean. What's next?"
    show sl normal pioneer with dspr
    sl "That's okay. I'll help you get back to your homeland, of course."
    sl "Since you're alone anyway, and nothing else ties you to this place..."
    me "What do you mean, it doesn't tie me down?"
    "I interrupted her."
    me "And Miku?"
    show sl sad pioneer with dspr
    sl "Semyon, I don't know what year you got here - but we don't have pioneers here having an affair with foreign performers."
    sl "It doesn't work for them."
    "Slavya shook her bangs."
    show sl angry pioneer with dspr
    sl "And you - look at yourself!"
    "I instantly bristled."
    me "What do you mean, 'look at yourself'? You think I'm not her type, do you?"
    "I don't need any more criticism from her!"
    show sl sad pioneer with dspr
    sl "No, but..."
    sl "You're not even upset! Not at all!"
    "Her words hit me like a heavy dust bag - like the one she was holding."
    me "You're right."
    "I grudgingly squeezed out."
    "I could have told myself that."
    "And if you can admit it to yourself, you can admit it to the people around you."
    me "I'm used to getting kicked out of life."
    me "But let's give it a try, if that's the case. What should we do?"
    show sl normal pioneer with dspr
    sl "Wish for it."
    "I couldn't believe my ears."
    me "That's it?"
    sl "Uh... Not exactly, of course."
    "She picked up the sack from the sand and gave it to me."
    "And I'll be damned if something didn't move in there!"
    me "What's in there?!"
    show sl serious pioneer with dspr
    sl "You don't have to worry about it. {w}It'll help you get home, that's what's important."
    me "How, I wonder? Is there a portable teleporter?"
    sl "Look, I know you have a hole in your memory, I know you can't remember how you got here."
    sl "And the last few days you've been too busy to just try to remember."
    me "Pretty much right."
    "I admitted it."
    me "So?"
    sl "Now would be a good time to start remembering."
    dreamgirl "You know, man, I don't like these insistent instructions."
    "For the first time, the alter ego has spoken."
    dreamgirl "This is all highly suspicious."
    dreamgirl "On the other hand, why would she want that? What do you think she is, an immigration officer?"
    menu:
        "I'll try":
            $ alt_day_catapult = True
            "It can hardly be worse than it is now."
            "What could ever be worse than being abandoned?!"
            scene bg int_intro_liaz_7dl with fade
            sl "Relax and let memory do all the work for you."
            "Slavya spoke soothingly."
            sl "You have to understand - you don't belong to us, you belong where you come from."
            stop ambience
            sl "You've messed and screwed up here - yes."
            play sound_loop sfx_bus_interior_moving fadein 4
            sl "But we can fix it, clean it up and put it back in its place."
            "I suddenly felt a moment of weightlessness - as if I were in free fall."
            play sound sfx_head_heartbeat
            sl "Your vacation is over, wanderer."
            sl "It's time to go home."
            "She poked me gently in the chest, and I opened my eyes."
            $ prolog_time()
            if dr:
                scene black with fade
                $ volume(0.5, 'music')
                scene bg intro_xx with dissolve
                stop ambience fadeout 2
                play sound_loop sfx_bus_interior_moving fadein 4
                show prologue_dream
                "Opened my eyes..."
                "It seemed to me that a familiar silhouette with brown hair flashed outside the window, overgrown with frosty patterns."
                "For a split second - a girl stood on the rail and looked longingly into my eyes."
                scene bg intro_xx with flash
                "It's like saying goodbye."
                "And after saying goodbye..."
                "She jumped."
                "I wanted to scream and jump up and run to the rescue, to call an ambulance and whoever I could."
                "If I had any strength left in me."
                "All I had to do was watch idly as the world outside the windows jumped and did a somersault."
                scene black with fade
                play sound sfx_water_emerge
                "The bus skidded and broke the handrail of the bridge, plunging fifteen meters into the icy black water."
                play sound sfx_7dl["aunl"]
                $ sdl_persistent_inc("alt_lamp")
                show acm_logo_va_lamp with moveinright:
                    pos (1600, 1020)
                pause(7.4)
                return
            elif herc:
                stop sound_loop
                scene black with fade
                "The bus was really going to hell."
                "I realize now that stupid Platt was a lot less stupid than I thought."
                "The philosophy of inevitable death, the eternal memento mori - I used to flirt with death, but I never took it seriously."
                "But now I felt its chilling breath on my lips."
                scene bg int_store_7dl with fade
                "And I remembered where the whole story started."
                "A story about a loser who couldn't do anything but work as a security guard."
                play sound sfx_7dl["makarych"] fadein 0
                pause(1)
                scene black with fade
                "Such an interesting story."
                "It began with a bullet in the head."
                "In the fading consciousness flashed a parting motif:"
                dreamgirl "And was it worth it?"
                play sound sfx_bodyfall_1
                stop sound_loop fadeout 0
                play sound sfx_7dl["aunl"]
                $ sdl_persistent_inc("alt_lamp")
                show acm_logo_va_lamp with moveinright:
                    pos (1600, 1020)
                pause(7.4)
                return
            elif loki:
                stop sound_loop
                play music "<to 52.94>" + music_7dl["herc_death"] fadein 5
                show blink with dissolve
                scene bg ext_winterpark_7dl
                pause(1.5)
                "Lying in the snow, in the clinging embrace of the deadening frost."
                show prologue_dream
                "I wouldn't survive half an hour here - not in my coat."
                "And lying in the snow..."
                show prologue_dream
                pause(1)
                "Powerless…"
                scene bg ext_winterpark_7dl with flash
                "Lifeless…"
                "In the movies, the heroes always died beautifully - with heads held high, aristocratic profiles, making inspirational speeches."
                "Not like this - beaten up, with their faces a bloody mess - already starting to freeze."
                "Whimpering with pain and death coming up to their throats."
                "So they weren't worth anything after all?"
                "My seven days of summer."
                th "Ksana."
                "It came to a fading consciousness."
                show blink
                scene black
                th "Ksana. {w}Hate you."
                play sound sfx_7dl["aunl"]
                $ sdl_persistent_inc("alt_lamp")
                show acm_logo_va_lamp with moveinright:
                    pos (1600, 1020)
                pause(4.4)
                return
        "I don't think I will":
            me "If I have a hole in my head, it must be there for a reason."
            "I gave her the bag."
            if alt_day_binder != 1:
                me "I already tried to remember once-"
                "And I rubbed my nose."
                me "I didn't like it very much."
            sl "Are you going to stay in a foreign land?"
            me "I came from hell."
            "Crookedly I smiled."
            me "Anywhere else would be better than there."
            "Slavya sighed, wanted to say something else, but changed her mind."
            "She took the sack and, turning away, went away."
            "She kept her back unnaturally straight."
            "And I didn't feel anything."
            "In fact, what was I supposed to feel when I chose between two evils, the one that was at least tolerable to me? Glee?"
            scene anim_square_party with dissolve
            "And when Olga approached me with a logical question, I just as logically agreed."
            "Since I'm not going to dance with anyone right now anyway, and being alone suddenly scared the hell out of me... So, what?"
            "That's right, all that's left is to lead the chaos!"
    stop music fadeout 3
    stop ambience fadeout 6
    return

label alt_day6_mi_7dl_discoteque:
    if alt_day6_mi_7dl_left:
        scene anim_square_party with clock_r
        play ambience ambience_7dl["disco"] fadein 3
        "I automatically changed songs, just as automatically waved off the infrequent invitations to dance, defended the console from Ulyana and Alisa who wanted to play something of their own, read out notes that were thrown on my desk, announced slow and fast songs."
        "Like eating without tasting - inhaling, exhaling."
        "The ticking of the clock, perhaps the rustling of the sand in the hourglass."
    else:
        scene bg int_dining_hall_people_sunset_7dl with dissolve
        play ambience ambience_dining_hall_full fadein 3
        play music music_7dl["shehasgone"] fadein 3
        "I remembered the dance of three days ago."
        "Back then, too, there had been an impatient anticipation in the evening cafeteria the day before."
        "Although there were sparks of other emotions, some had been waiting all shift for this particular dance."
        "And some were planning to stay at camp because their parents had taken a pass for several shifts at once."
        "These ones were cackling, looking down on future departures."
        "I didn't know who I belonged to, but since no one talked to me about continuing the banquet..."
        show mi smile pioneer with dspr
        mi "Sen', hey Sen', will you invite me?"
        me "Where?"
        show mi laugh pioneer with dspr
        mi "To the dance, of course! Or have you made arrangements with someone else?"
        th "Hello, I'd like to book your body for the next dance..."
        "Still, before we had all these... displays of affection between us... it was a little easier."
        show mi normal pioneer with dspr
        mi "If you have a deal, that's okay, I'm not your wife..."
        me "Stop talking nonsense."
        "I asked."
        "I suddenly had an interesting idea."
        me "Listen, you don't have to dance. Why don't we go for a walk?"
        mi "And miss the last dance of the shift?"
        show mi upset pioneer with dspr
        mi "No {w=.5}freaking {w=.4}way!"
        show mi sad pioneer with dspr
        mi "I didn't have to spend two weeks alone in a club to go off somewhere from the farewell disco!"
        me "Ah. I see. {w}Can you explain the connection between your sitting and the disco?"
        show mi shy pioneer with dspr
        mi "No!"
        "And how am I supposed to talk to this crazy woman?"
        mi "You dress up nice and pretty, I made you a costume and ironed it - and we'll dance, and Uncle Borya-sensei will be sure to stick us in the '89 album as the prettiest couple!"
        show mi angry pioneer with dspr
        mi "I said!"
        me "Okay, okay! You said it, that's the way it's going to be..."
        show mi normal pioneer with dspr
        mi "Let's go, Senechka! Or they'll start without us!"
        "Shaking my head, I followed her."
        with fade
        play sound sfx_open_dooor_campus_2
        pause(1)
        scene anim_square_preparty
        with dissolve
        play ambience ambience_camp_center_night fadein 3
        "And the square was all ready to dance!"
        "While we were saying a touching goodbye at the gate and Miku was voicing her plans for her modeling career for the camp album, the camp counselors were already hard at work, setting up equipment and hanging up lights and music."
        show mi normal pioneer with dspr
        mi "Oh, they wasted no time!"
        "Exclaimed Miku."
        mi "So, listen, Senya."
        mi "The suit for you is hanging on a hanger in your cabin, in your closet - thanks to Olenka Dmitrievna and Slavya."
        mi "Put it on and come back! And don't show up in the square without the suit, you understand me?"
        "Funny miracle, funny - how could I not smile and nod."
        "I agreed, feeling that oh and she's going to make a jackass out of me!"
        mi "Then I'll see you back here!"
        "She chirped and flew away."
        scene anim_square_preparty
        with blind_l
        pause(2)
        "When we reappeared in the square - simultaneously, by the way, though from different sides of it - it was exactly nine o'clock in the evening."
        "In the center of the square Ulyanka was already doing some wild antics, and her large retinue of younger groups echoed her with shouts and enthusiasm."
        "Though, of course, the music was playing, I wouldn't risk dancing to it."
        "Either the rhythm is wrong, or the tune, or Yuri Antonov doesn't associate me with dancing in any way."
        with fade2
        "So for the first fifteen minutes I stood there, propping up Genda, stubbornly fighting off all the attempts of the Japanese girl to drag me out on the dance floor."
        "But then the first quarter-hour chime played, and the squad leader sent the first slow song into the air."
        play music music_7dl["stilllovingyou"] fadein 5
        "A composition to which it would be a sin to stay still."
        "A song about the youth of the soul, about longing and loneliness for someone whom life often keeps out an insurmountable wall."
        "But it was up to the listener to hear what was there."
        "Everyone had something to hear, a story to tell."
        "Me?"
        "So did I."
        scene cg d3_mi_dance_close_bordo_7dl with dissolve
        mi "Why are you frowning, Senechka?"
        "In a half whisper Miku asked."
        "Beautiful music."
        me "Just..."
        "Because there might one day be such a wall between us too - of space, of time. An impenetrable membrane of dream-vision."
        scene cg d3_mi_dance_afar_bordo_7dl with dissolve
        "And it's so meaningful - your naiveté, your ability to hear and trust in miracles."
        "I'd so like to see you again, darling - but only a fool would climb Fuji-san twice."
        me "I wonder what will happen if you don't make it with the record company in the fall - the chance is gone..."
        mi "You know, Senechka, I've decided to try a new field altogether - nothing to do with what I used to do!"
        "Miku confessed."
        me "Really? Which one is it?"
        mi "It's a secret for now! But I think I can do it."
        "Her eyes gleamed in joyful anticipation."
        mi "I realized I was in such a wonderful state right now."
        mi "I can choose and try anything at all! Anything at all I can think of - extreme sports, travel, music, culture, education - anything!"
        mi "And you taught me that."
        "The Japanese girl cast a glance at me from under her eyelashes."
        mi "And I also want whatever path this story takes to end where I meet you at home from work."
        mi "And I want to go to that German concert, too."
        mi "And just to go shopping, ladling a hundred handbags and bags around you."
        me "Your dream sounds too wonderful."
        mi "That's not even a dream."
        "Miku pulled away and looked demandingly into my eyes."
        mi "This is a guide to action. A plan-task for the next few years."
        me "Wow!"
        me "Are we going to live in the Union or Japan?"
        mi "I haven't decided yet! But I will!"
        mi "The main thing is that you don't disappear."
        "I smiled."
        me "I'll do my best."
    play ambience ambience_camp_center_night
    stop music fadeout 5
    scene cg d6_dance_alt_7dl with dissolve
    "The dance, the farewell dance, is like asking fate for a second chance."
    play music music_list["farewell_to_the_past_full"] fadein 3
    "The people around me danced as if tomorrow would never come."
    "And for some of them it really will never come like this."
    "Too old, looking for their own way in life, or those who won't get a ticket next year."
    "Of course, they can always take the bus and come here on their own."
    dreamgirl "Except the guards at the gate won't let them in."
    th "Actually, they will. {w}I've gone that way myself a few times - where the director remembered only good things about me."
    th "Now, of course, memories of me will be far from rosy."
    "Well, I'm just a guest here, too."
    with dissolve
    "There was a second dance and a third - and then Olga took the microphone:"
    mt "Guys, we have a surprise from Miku for you."
    mt "Everyone, please proceed to the dock."
    "The pioneers murmured amicably, but obediently and extremely promptly turned around and reached for the water."
    scene bg ext_boathouse_night
    with dissolve
    "On which the action has already begun..."
    play music music_7dl["sam_lullaby"] fadein 3
    play ambience ambience_7dl["salute"] fadein 1
    show salute
    pause(1)
    show black behind salute
    with dsps
    me "Salute!"
    "I gasped."
    if alt_day6_mi_7dl_left:
        "A parting surprise from Miku."
        "I looked at the scarlet flowers tearing up the sky and felt my heart tear just the same."
        "There was too much I was trying to make up for with the salute, and there was an emptiness in my chest."
        "And I stood, fists clenched, away from the main mass, and looked up into the sky."
        "I looked up and remembered all the good things this camp had given me."
        "All the good in me that was now inseparable from a simple name - four letters, two kanji."
        "Real loneliness cannot be filled, just as some people cannot be replaced-even if they are fleeting in your life."
        "But you can look at the fireworks - until they start to float in your eyes."
        th "I'm so lonely..."
        "It's just a carving from the wind off the river and looking too closely."
        "It's just that Miku isn't around."
        th "I miss the warmth of her palm so much - now that all these people who are strangers to me are celebrating something."
        "Someone stood silently beside me."
        scene cg d6_mt_salute_7dl
        with fade
        mt "Well, what do you think?"
        me "So beautiful."
        "Said I to nowhere."
        me "So beautiful and so useless."
        me "Why is beauty no joy if you are unhappy?"
        me "I'd give a lot to turn back time and say the right words without falling into platitudes."
        mt "Do you think you could change anything with words alone?"
        with fade
        "Olga sighed softly - and that sigh was somehow not interrupted by the rips."
        me "I could have tried."
        "I objected."
        me "I'd say the most important thing, and then whatever happens."
        th "Although my experience is the son of hard mistakes, there have been only two 'most important' times."
        th "And both times were unsuccessful. Unsuccessful! As if a word changes anything in a person's psyche."
        th "And as long as you are friends - including organisms - no one has any complaints. No one is afraid. No one is forcing anyone to do anything."
        dreamgirl "But in this place, she's {i}real{/i}."
        dreamgirl "Can you imagine such a thing? Not the hopelessly incandescent holographic projector lights and smoke-screen."
        dreamgirl "But a living real person - who even knows your name."
        stop ambience fadeout 5
        scene stars
        with dissolve
        play ambience ambience_boat_station_night fadein 3
        mt "That never works."
        "Even quieter said the squad leader."
        "The fireworks ended, and slowly the sky, which had seemed impenetrably black, sprouted a crystal-clear scattering of stars."
        "The sky opened wide, and if I had been any less lonely, I would have laughed with happiness."
        mt "Believe me, as someone who has faced it before."
        mt "No confession has ever saved anyone."
        me "Better to howl into my pillow at the thought of what I could have done but chickened out?"
        mt "Yes."
        "Just answered the counselor."
        mt "Sometimes that's best."
        mt "Go dance, it's half an hour before lights out."
        scene bg ext_boathouse_night with dissolve
        "As she turned around, she melted into the darkness."
        "After standing and gazing into the starry sky for a while, I went home."
        "I didn't feel like dancing."
        "Neither leading those dances."
        stop music fadeout 6
        with fade
        play sound sfx_open_dooor_campus_1
        pause(1)
        scene bg int_house_of_mt_noitem_night
        play ambience ambience_int_cabin_night fadein 1
        "It was delightfully empty and lonely inside."
        "It was as if I had dragged my world here and comfortably housed it under the triangular roof."
        me "Resistance is useless?"
        "I asked the walls."
        "The walls were disciplinedly silent."
        me "Nothing..."
        "I muttered, undressing."
        scene cg d1_end_of_day_7dl with fade
        me "It's okay... We'll fight again."
        stop ambience fadeout 6
    else:
        scene cg d6_mi_salute_7dl
        show salute
        with dissolve
        me "Did you do it?"
        mi "Do you like it?"
        me "I love it! I love it!"
        "We stood holding hands like children and watched the fireworks blooming in the sky."
        "And we didn't say anything."
        "I glanced at Miku. She was standing there with her mouth ajar, and there was a real rapture in her eyes."
        "A very contagious rapture."
        scene cg d6_mi_salute2_7dl
        show salute
        with dissolve
        "I pulled her close to me, wrapped my arms around her shoulders, and laughed with happiness."
        me "How beautiful."
        "I answered the mute question in her turquoise eyes."
        me "Where did that come from?"
        mi "It was Sakishita-san who brought it, a gift from Pa."
        "Smiled Miku."
        mi "It was planned to be my parting gift before I left, but..."
        "She hissed, getting comfortable, and laid her head on my shoulder."
        mi "It turned out a little different."
        mi "I don't regret it much, though - that's the truth."
        with flash
        "The Japanese girl squinted - retreated a quarter of a step away from one particularly loud - huge! - golden balloon that took up the whole sky above their heads."
        "The people squealed with delight, greeted each new volley with a shout."
        "And we stood a little away - we were happy to be here, to be near..."
        mi "I kept thinking, thinking - what would be the right thing to do."
        mi "And then I realized: the right thing is what the heart says."
        mi "My heart told me to come to you..."
        "And a very mature Miku girl condescended to me."
        "She stood on her tiptoes and reached out to me, clasping her eyes."
        dreamgirl "And they lived a short and nasty life, amen."
        dreamgirl "Will you name the baby after me?"
        th "What's that? Schizophasia?"
        "A little absent-mindedly, I thought - somebody somewhere decided that kissing Miku was more important than air."
        "And so it became."
        play ambience ambience_lake_shore_night fadein 3
        scene stars
        with dissolve
        "It became that of all the girls on the planet I had chosen the best."
        "And all she had to do was make peace with it."
        me "The salute is over..."
        mi "Yeah..."
        me "We have to go back to the dance..."
        mi "We should..."
        "She stood like that - wrapped her skinny arms around me, huddled as hard as she could."
        "Small-small, fragile."
        "And at the bottom of her eyes a whole ocean of tenderness splashed and played."
    with fade
    return

label alt_day6_mi_7dl_hentai:
    scene bg ext_boathouse_night with dissolve
    "And it was morning, and it was evening - day six."
    "It was as if I had spent my life groping my way to her, at random, dropping clues here and there from my wrong hands."
    "And she dangled her feet on the edge of the bandstand and waited patiently for me to pass close enough - so she could jump on my neck."
    mi "Caught you!"
    "I tried to dodge, tried to barely, barely touch her lips."
    "But she wanted more - catching my head, pulling me to her..."
    with fade
    "And someone had already cracked the champagne over my ear, forcing me to duck my head, and the cork flew up into the sky, and the happy laughter of the people who made this camp such a wonderful place spread over the beach."
    "The bosses looked the other way on such pranks."
    "It's people's holiday, why ruin it?"
    show mi normal dress with dissolve
    "And Miku was most beautiful in her hair-toned dress, so defenseless, aloof, hugging herself shiveringly by the shoulders."
    me "Is it cold?"
    mi "Your lip is pierced."
    me "And you kiss it, and it will go away."
    "Declared I have no doubt in the miraculous powers of my beloved."
    "And I wish it were like in the movies - eye to eye, eye to eye..."
    "That the surroundings blurred and retreated into the shadows, the sounds gone, the flashes of light gone..."
    "And she kept looking at my lips."
    "As if she wanted to see something there."
    me "Why are you trembling?"
    "I asked, trying to chase the cold from her wrists with the warmth of my breath."
    mi "I don't know."
    "Sadly she answered."
    "And only now did she look up."
    me "Do you want to..."
    "I thought for a moment, and it hit me."
    me "Do you want it to be just you and me here now?"
    mi "In a place where no one can find us?"
    mi "Can you do that?"
    "She looked at me slyly."
    me "I can do anything."
    mi "Then do it. Make sure we end up where no one can find us."
    me "Okay. But you have to trust me."
    mi "I will."
    me "But just trust me as much as you can."
    mi "Okay."
    me "Close your eyes."
    "And as Miku closed her eyes, I crouched down and lifted her easily into my arms."
    me "Don't look! Don't look in any way!"
    "She weighed only three grams of notes, levity, and reflections on the water."
    scene anim_square_party with dissolve
    play ambience ambience_camp_center_night fadein 3
    "I ran easily up the stone-battered road up to the square."
    "And without stopping, I ran on."
    "Somewhere where no one will really ever find us."
    play sound sfx_open_dooor_campus_1
    pause(1)
    if alt_day1_sl_keys_took == 1:
        scene bg int_warehouse_night_7dl with dissolve
        $ alt_hpt += 1
        if alt_day5_mi_7dl_kiss:
            $ alt_hpt += 1
        mi "Senya, where did you get the keys?"
        me "Don't ask..."
        "I answered."
        if alt_day_binder != 1:
            me "Picked them up while one Winnie-the-Pooh with long hair sang his songs."
    else:
        scene bg int_wardrobe2_7dl with dissolve
        $ alt_hpt += 1
    $ persistent.sprite_time = "night"
    show mi smile dress
    with dissolve
    "We searched each other's lips and hands in a futile and disastrously long time."
    "The warmth of our palms dried up, and we were left in darkness."
    scene black with fade2
    play music music_7dl["feel_you_inside"] fadein 3
    me "Aren't you afraid of the dark?"
    "I asked, trying to guess at the girl's silhouette in the wrong moonlight."
    mi "No."
    "It's amazing how much space there turns out to be - and the darkness seems to have expanded the empty space."
    "It suddenly seemed to me that she was far, far away, and, startled, I took a sudden step toward her."
    "Breathed in the scent of her hair - eucalyptus."
    me "At all?"
    mi "At all."
    "She whispered."
    "My vision was slowly getting used to it, and I could already make out how chilly she was hugging herself by the shoulders and looking away, half turned away."
    me "What if there's a hedgehog all of a sudden?"
    mi "Semyon..."
    "She said reproachfully."
    me "It's been so long since you called me exactly Semyon."
    mi "Yes."
    "She stood like that, and someone had to make the first move."
    "That's how I ended up next to her - without spreading my arms, I was standing so close to her that I could feel her heart pounding through her shirt."
    me "You're cold and you smell green. Like a cough drop."
    mi "Baka."
    "She swayed toward me - it was just a matter of putting my palms up."
    "And let her inside me."
    mi "Aren't you worried at all?"
    me "I do worry."
    "It was inside. It was something you can't show people close to you anymore - what Miku has become."
    "I have no right to show her how shaken up I am."
    mi "Really?"
    me "Honestly."
    "Now she was really shaking."
    me "Are you cold?"
    "She shook her head negatively, caught my hands with hers and squeezed them, pressed them to her chest."
    me "Don't be afraid. If you don't want to, I won't touch you."
    "With a deep sigh, she lifted her head."
    mi "You won't touch?"
    me "Honestly. I won't."
    "She leaned up on her tiptoes and leaned on my arms, gaining a few more centimeters."
    "And reached for my lips."
    mi "I'm not afraid. I want to."
    "The girl whispered softly, sweeping away the last barriers between us."
    "The night smiled affectionately, dissolving us into itself."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_mi_7dl_begin:
    scene bg int_looney_bin_7dl with dissolve
    play music music_7dl["uneven_me2"] fadein 3
    "The Twilight Zone didn't bother anyone in particular."
    "Though if anyone happened to pass near it, there was a full range of unpleasant experiences waiting for them."
    "The skin on the back of my neck was taut from the grave spirit blowing in from the other side, and the darkness was like an extremely attentive eye studying a fool at point-blank range."
    "But, as I understood it, there's an angle like that in absolutely any institution."
    "Apparently, for the sake of balance, in spite of all the brightly lit places with excellent acoustics, there was always a nook with cramped walls from which the sound came back frighteningly distorted."
    "Rumor had it that such places were haunted by evil spirits - the ghosts of those who had once strayed too far into the domain of the Shadow."
    "And even the clear awareness that half of the rumors being disseminated were encouraged directly by the administration didn't save one bit."
    "Perhaps there's just something unholy hidden in there, like Christmas toys or a Christmas tree proper, a bell for the last bell and flat boards for the annual fair-exhibition..."
    "Here and now I was simply creeped out."
    "And someone comes here every time the directorate needs something from the homeland's stash."
    "An order sounds, and a quartermaster armed with a flashlight and a hand-operated dynamo rushes over there..."
    "Of course, everything happens much later than school hours (and the quartermaster's day doesn't end until seven o'clock), so there were hardly any witnesses to these kinds of outings."
    "I stood there for an hour, trying to make out at least the outline of a pretty little brown girl in a short dress who'd gone down there."
    "She was calling me with her, and I seemed to take her hand - and the touch shook me like a hard electric shock."
    "For a split second a black veil was thrown over the world, and when I opened my eyes - I was already here."
    "Standing with my back to the CHT until I heard footsteps receding behind me."
    dreamgirl "Don't hold the pixels with your fingers - they cut your hands."
    "Silence silently reported."
    "Absorbed the girl, and a moment later even the distortion circles smoothed out."
    with fade
    "The speakers overhead came to life, and a quavering voice reported."
    voice "'Jungle Radio' is broadcasting a special order in memory of Ri Hagakure."
    "A thunderous shriek came from somewhere, accompanied by a noise of footsteps - a door at the far end of the hall swung open, and a vaguely familiar girl, draped in a long leather skirt, with long hair of a pinkish hue, jumped out of there."
    "Without giving me even a glance, she dashed past me and disappeared behind a door marked 'school radio station.'"
    "A few seconds later from there came the sound of blows, screams, and then the song died down, replaced by the background hum of the speakers."
    "This time I decided not to stand in the way of the fighting maiden in leather and retreated to the window."
    "The darkness, with a disgruntled clang, let go of my shoulder blades and lurked again."
    "The whole time I was walking to the window, I felt an extremely {i}attentive look{/i} on my back."
    "Walking in cold sweat, every moment expecting an attack."
    "I even wondered how I could resist the razor-sharp claws of the ice - and I had no doubt that the watcher had such claws."
    "I guess I'll have to play for reaction."
    "Believed that as long as I didn't turn around, he wouldn't dare attack."
    "Especially as long as there are people around."
    "Sometimes the strongest shield is just having someone around."
    "At least that pink-haired girl."
    "That's why I was almost not afraid."
    "Almost..."
    with fade
    "As I approached the window sill, I leaned my fists on the cold plastic and exhaled, pushing the rest of my fear deeper into the air."
    "And I turned around sharply."
    scene
    $ renpy.show("bg int_looney_bin_7dl", what = Desat("bg int_looney_bin_7dl"))
    with fade
    "There was no one behind me!"
    "That said, the feeling of {i}observation{/i} wasn't lost."
    "That's the way a wall might have looked at me - if it had suddenly acquired consciousness and critical thinking."
    "The dark corner lurked and watched me."
    "With a sigh, I turned away, determined to ignore the disorderly signal system."
    "And there was plenty to see outside the window."
    scene bg ext_stairs_night_7dl with dissolve
    "There was a garden right below the windows."
    "The building I was in appeared to be a two-story, brick building, and it encircled the garden in a closed ring."
    "The roof, visible from here, was, according to Japanese rules, fully accessible, though it was draped in fencework around the perimeter."
    "Now there were two girls throwing the ball over there...or two guys?"
    "It was hard to see at this distance-but they succeeded: interrupting the game for a moment, they waved their hands at me."
    "It would even be cozy here. Great."
    "If it weren't for that dark muck."
    "I didn't think I was that afraid of the dark."
    scene bg int_looney_bin_7dl with fade
    "There was nothing else of interest outside, so I turned away from the window."
    "I was haunted by the strange silence of the school corridors."
    "Except for the occasional loudspeaker on the school radio, nothing disturbed the pristine tranquility of the place."
    "It was as if the quietest children I could find had studied here."
    "Perhaps they were - after all, I opened my eyes exactly five minutes ago and came to my senses."
    "How I walked here - and judging by the fact that I was on the second floor, I was also going up the stairs - I didn't remember."
    "I didn't remember the way here, or the events that preceded it."
    "It was as if the emptiness had one day decided - let this guy be this guy, and that was me."
    "A theory as good as any, eh?"
    play sound sfx_open_dooor_campus_2
    "The door slammed."
    "On the doorstep of the radio room stood the girl with the pink hair."
    voice "Going to class?"
    "She inflated a pink - to match her hair - bubble of bubble gum and burst it resoundingly."
    "The sharp sound made me flinch and come to my senses a little."
    me "To class?"
    voice "Or are you just going to stand by the window?"
    "The girl strode past me, glancing at me in passing with an appraising glance - from head to toe, then back the other way."
    "And she disappeared behind the door she'd run out of a few minutes earlier."
    play sound sfx_open_door_clubs fadein 0
    pause(1)
    scene bg int_concert_room_7dl
    with fade
    "Not having thought of any alternative to my continued standing here, I decided to follow the perky pink-haired woman."
    "She was rather pretty, despite her somewhat cavalier manner."
    "We found ourselves in a room clearly reserved either for choir singing rehearsals or for corny music lessons."
    "Admittedly, the few teenagers here looked pretty old to be studying music through the school curriculum-when I was in high school, the last lessons in that subject were in the ninth grade, if I'm not mistaken."
    th "Unless it's music school."
    "It suddenly occurred to me."
    "Then I'm somewhat irrelevant here."
    "There have already been a few teenagers here - and I realized suddenly that I'm still in my third decade and I'm slightly more than 'somewhat' inappropriate here."
    "Or?"
    voice "Take your pick."
    "Called an old acquaintance."
    voice "Not too close - that's not the way it's done here."
    th "Individualists, eh?"
    "I twitched my shoulder and started picking a seat."
    "The desk chairs were arranged in a five-by-five square, but in reality there were only eight people in the room, including me."
    "Each of them squared off from those around them, leaving at least one free desk between themselves and their nearest neighbor."
    "The only exception was the couple in the corner - apparently friends."
    th "Or a couple."
    "And me, too."
    with fade2
    "But I just don't know how and I don't know how much I got here, and so I settled on my childhood favorite 'Kamchatka.'"
    "Quiet."
    "I've started to learn about my surroundings."
    th "That's all right, the teacher will come and sort it all out."
    "Having soothed myself in this way, I regretted in passing that there was no music-excluding the whispers from the corner, the silence was sepulchral."
    "Everyone was sitting in the voluntarily created lurch - both the pink hottie I knew and her window-mate, with a short haircut in Japanese fashion, chipped by paired ponytails and horse-bangs."
    "Three desks in the front row were occupied by some unassuming mouse in brown, a guy in a ragged 'apache,' and another draped in leather, with a haughty expression on her face."
    "The couple from the corner synchronously met me with glances - and I felt like an idiot for signing them up as lovers."
    "Twins. I should have known right away..."
    "Shuddering, I shifted my gaze - fidgeting awkwardly, not knowing where to look..."
    "My gaze stopped, fixed on the proudly erect back."
    "On the chiseled neck."
    "On the long tails of fantastic color, living a life of their own."
    "The air stopped in my throat as a short name - four letters, two syllables - burst through the shroud of unconsciousness."
    th "Isn't that... Her?"
    "She didn't last long; she was suspicious, and a few minutes later she turned abruptly to me:"
    mi "How long are you going to stare at my back?"
    voice "Hey, what are you doing all of a sudden...?"
    mi "You stay out of this."
    "There was plenty of hostility in her voice."
    me "Calm down, calm down..."
    "I raised my hands in front of me in an international peace sign."
    me "Your posture just seemed familiar to me, and I wondered - maybe we'd met."
    mi "Maybe?"
    "The already icy tone became even colder."
    with fade2
    voice "Yeaaah..."
    "It came from the twins' side."
    voice "Miku's character hasn't improved a bit over the summer."
    mi "Why would it?"
    "She parried."
    mi "It's just a visit to my father's homeland. I wasn't supposed to improve."
    voice "But you're not supposed to get worse either! I remember you as a chatty but kind girl."
    voice "And you came back looking like your favorite cat had been caught and eaten by tramps."
    mi "What the hell do you know!"
    "She blurted out."
    mi "What do you all understand anyway!"
    "She jumped up, threw her chair away, and ran out of the classroom to loud hooting."
    "At the door, she barely missed the teacher, but she paid no attention to him."
    voice "Hatsune-kun?"
    "Confused, he asked the emptiness."
    play sound2 sfx_dropped_chair
    pause(2)
    play sound sfx_open_door_kick
    pause(1)
    scene bg int_looney_bin_7dl
    with fade2
    "I don't know what made me tick, but I ran after her."
    "If the world makes zero sense, who's to say I can't make up a new one?"
    "You know, that's what squatters do. They occupy empty houses and live there at their pleasure."
    "So let's let at least a little bit of certainty into this world."
    "There's Miku running, there's me after her..."
    "Miku..."
    with flash
    "I suddenly remembered how I know this girl."
    "Miku."
    me "Miku!"
    mi "Stay back!"
    "She shouted without turning around, running at full speed."
    "The distance between us began to increase."
    me "Just wait! Miku! I need help!"
    mi "I won't help you!"
    "The loss of concentration for just a moment was devastating for the girl - she flew headlong into the twilight zone."
    "Shrieked - I didn't hear a sound, and I understood why this filth was called black silence."
    "From here, like a black hole, no sound was able to escape, even the light here changed its nature and poured out leisurely, scattered photons."
    "Stumbling, Miku fell to the floor - I rushed after her and stopped, stunned."
    "The girl was bleeding into her surroundings in squares of smoke-melting, golden sparks floating upward, like fireflies from a fairy tale."
    "One such square flew toward me and sat on my palm, illuminating my fingers with a warm, flickering light."
    "Letting me know that Miku needed to be pulled out, out of where she'd driven herself."
    "And I, at full speed, jumped into the twilight."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_mi_7dl_wakeup:
    if alt_day6_mi_7dl_left:
        scene bg int_house_of_mt_sunset with dissolve
        play ambience ambience_int_cabin_evening fadein 1
        play music music_7dl["red_lights"] fadein 3
        "...morning?"
        "I reluctantly unstrapped my left leg from under the blanket."
        "And made sure it was disgustingly warm and cozy outside."
        "Clearly not unlike the way it was yesterday, the day before, and pose-pose... in short, the whole time I woke up, perceiving Miku somewhere nearby with a hundredth of my gut."
        "Now she's gone so far away I can't see her from here."
        "And then - why don't the local air conditioner turn on 'heavenly' mode now - that would make my lousy condition worse, mission accomplished, thank you all!"
        "With a heavy sigh, I tossed my head back onto the pillow and tucked myself deeper under the covers."
        "The local objective reality didn't interest me."
        "Far more interesting was that colorful, three-dimensional, stereo-sounding dream where I was looking into the turquoise back of my head, catching a glimpse; albeit a distasteful one - but native."
        with fade2
        "It was only mine that almost became ours - and somehow it's even creepy to think about how I should go on?"
        "Who was I trying to fool yesterday, why was I trying to pretend to be someone stronger than the real me?"
        "Now I was ready to crack my stupid head on the corner of the bed."
        me "Retard, retard, holy shit, what a retard..."
        "I groaned, holding on to the otherworldly pain of my temples."
        "No self-affirmation is worth the missed opportunity of the last morning to crawl outside and there smile warmly, 'Hi. It's you, isn't it? {w}I missed you...'"
        "Or perhaps if I'd accepted the offer to go with her?"
        "I shook my head in the negative."
        "Miku would never have forgiven her for disappointing me."
        "And she would inevitably have been disappointed."
        "Watching the light dim from beneath her lashes, loosely closed from the streaming pain, years later wistfully remembering what she had expected from life."
        "Expected of us."
        "And now what - gray hair under a poisonous green tint in my hair, tired legs and perpetual chills in my shoulders."
        th "I'm so logical."
        th "So correct and reasonable."
        "Then why do you want to howl so badly?"
        "Sovyonok was firmly tied to sadness, which means it's time to get out of here."
        "The sooner I get up, the sooner I get on the bus."
        "Time to get up!" with vpunch
    else:
        scene black with dissolve
        if alt_day1_sl_keys_took == 1:
            play ambience ambience_camp_center_evening fadein 3
        else:
            play ambience ambience_music_club_day fadein 1
        play music music_7dl["groovie"] fadein 3
        "I was awakened by the horn blaring, seemingly in my ear."
        "Grumbling unhappily, I opened one eye."
        if persistent.hentai_graphics_7dl:
            scene cg d6_mi_morning_7dl
        elif alt_day1_sl_keys_took == 1:
            scene bg int_warehouse_day_7dl
        else:
            scene bg int_wardrobe2_7dl
        with flash
        mi "Woke up?"
        "In a voice hoarse from sleep, Miku inquired."
        "She was lying in such an interesting position that my imagination drew out all the necessary - and with the morning's body peculiarities in mind..."
        "I reached for her..."
        with fade
        mi "Senka, have a conscience."
        "Miku tried to fight back, but somehow without enthusiasm."
        "It was as if she was thinking about continuing the banquet."
        me "I won't conscience... This or that. {w}You better get over here."
        scene black with fade
        "We got closer."
        play sound sfx_7dl["sigh_out"]
        "Though I have tried with all my might to get her to do one thing."
        "To be able to think with her own head."
        "To choose by pocket, shoulder and conscience."
        "Who would have thought that she would choose me?"
        "Neither did I."
        "Maybe it was all just a dream."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_mi_7dl_packing:
    scene bg ext_dining_hall_away_sunset with fade2
    play ambience ambience_camp_center_evening fadein 3
    play music music_7dl["old_kiss"] fadein 3
    if alt_day6_mi_7dl_left:
        "It was expectedly sour, dull and dreary."
        "Time dragged on annoyingly slowly, even more nauseating and rubbery than this chewy mush of the 'friendship' type."
    else:
        "There was an undeniable upside to it all, though."
        "We finally decided how we felt about each other and what we wanted."
        "Or rather, not even that."
        "I realized that I feel a little... a lot warmer toward Miku than I do toward just a friend - not surprising after that night."
        "And she... Perhaps her choice was due to the fact that this camp simply can't offer her anything better?"
        "Though if it's just humility, then why are my eyes burning with admiration?"
        "The evolution of relationships: acquaintances, buddies, friends... Lovers."
        scene bg ext_dining_hall_near_sunset
        with fade
        if alt_day1_sl_keys_took == 1:
            "I couldn't believe it was real."
            "It seemed that when the girl reached a logical point, some kind of climax, the lights would go out, the firecrackers would go off, and people would run from all sides screaming 'surprise' and 'hidden camera'."
            "Because I couldn't really believe that I turned out to be really interesting to Miku, could I?"
            "Or could I?"
            "The most dangerous moment was when the keys rattled in the warehouse lock and the doors opened."
            "Slavya had gone inside - just a little more and she would have spotted us!"
            "And it was Olga Dmitrievna who bailed us out, oddly enough - she called out to the activist, who out of politeness stepped outside."
            "Which gave us a few seconds to flee the room, nobly leaving the unnecessary bunch of keys on the table."
        else:
            "Frankly, I'm surprised no one was looking for us with dogs."
            "Because even a day earlier there would have been almost a search expedition here."
            "Oh, and Miku's attitude was surprising - as if by refusing to leave with Sakishita, she'd suddenly lost a couple of dozen points of her indispensability rating in the eyes of those around her."
            "No one has mentioned her once in the last ten hours."
            "Does that ever happen?"
            "I twitched my shoulder - apparently it does happen."
        "Then there was the epic trek to the canteen, with looking out for squad leader of the bushes."
        "But luck was on our side today - we snuck into the hall and sat down at the tables shortly before Olga Dmitrievna appeared to the people."
        "And at the same time it would have been better if we had just finished everything necessary at once - and stayed together somewhere, just basking the rest of the time next to each other, touching each other's shoulders."
    "But the sun warmed with enthusiasm, and the sleepy pioneers hummed with a strange enthusiasm."
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg int_dining_hall_people_sunset_7dl at zenterleft
    with dissolve
    play ambience ambience_dining_hall_full fadein 3
    "We promised each other we'd see each other, if not in the city, then at camp next year for sure."
    "Except I couldn't promise anyone anything."
    "Even the simplest «we'll meet again» sounded like a lie out of my mouth."
    "I didn't even guarantee the next five minutes."
    "Nothing at all."
    "That made me feel bad, to be honest."
    if alt_day6_mi_7dl_left:
        "I'm probably a little relieved, though, not having to say goodbye to a dear person."
        "For I've already said good-bye."
        "It was like living in a movie with a sad ending - after it was over."
        "I just had to suck it up and go with the flow."
        "And that's a science I'm pretty good at."
    else:
        "It wasn't even clear how to feel about the fact that we were going to be marinated in the same bus for a few more hours before being separated."
        "On the one hand, one last chance to breathe in the right air before I die."
        "On the other... All this time will be spent under the sign of imminent separation."
        "Six hours of longing and grief."
        "But these are my cockroaches and self-corrections."
        show mi normal pioneer with dissolve
        mi "Will you help me pack?"
        "I don't think she needed my direct help that much."
        me "Absolutely. What needs to be done?"
        show mi smile pioneer with dspr
        mi "Sit quietly in a corner and keep me company while I put the dresses away in my suitcase!"
        "The Japanese woman smiled."
        "I guess it really was just an excuse."
        me "What about my stuff?"
        show mi laugh pioneer with dspr
        mi "Senya! I'm aware that you came without any belongings at all!"
        mi "I would be surprised, but Olga Dmitrievna-san said that there is an agreement with your parents about that."
        mt "There is! {w}And there's also an arrangement to let the counselor know a little bit where her pioneers hang around!"
        show mt normal pioneer at right with dissolve
        "The squad leader reported, appearing out of nowhere right behind our backs."
        th "Brrr, she would have been a villain in a movie."
        dreamgirl "And she's laughing so hard: bwa-ha-ha-ha-ha!"
        th "Sort of."
        mt "So you want to tell me where you've been?"
        show mt grin pioneer with dspr
        mt "Just don't give me those songs about walking around."
        show mi serious pioneer with dspr
        mi "Senya, he..."
        "Miku took the most serious look and even started to explain something, but I interrupted her:"
        me "Okay, I won't sing. {w}I'll tell it like it is."
        show mi shy pioneer with dspr
        mi "Oh..."
        me "Long story short, I slept in a tree house."
        "I have no idea where this 'tree house' suddenly came from - it jumped off the tongue all by itself."
        show mt sad pioneer with dspr
        "And Olga, hearing that answer, all seemed to fade - she exhaled, nodded."
        mt "I thought so. {w} Finish your breakfast and start packing - departure at noon."
        hide mt with dissolve
        "Without giving us another look, the squad leader left."
        mi "Senya, is there anything you want to tell me?"
        me "Ah, don't ask."
        "I shook my head."
        show mi upset pioneer with dspr
        mi "Seeeeeeeeeeeeen!"
        me "Just an old story related to Olga Dmitrievna."
        show mi happy pioneer with dspr
        mi "How interesting!"
        "The Japanese woman clapped her hands."
        mi "Will you tell me about it?"
        me "No. {w}Later, okay?"
        dreamgirl "Isn't there anything you want to tell me?"
        th "You - especially not!"
        "I replied, finishing my breakfast."
    stop music fadeout 5
    play sound sfx_open_door_2
    pause(1)
    scene bg ext_dining_hall_near_day at zenterright
    with dissolve
    play ambience ambience_camp_center_day fadein 3
    if not alt_day6_mi_7dl_left:
        "Miku clung to me on the porch and demanded in an unapologetic tone that the story continue."
        show mi serious pioneer with dissolve
        mi "And now!"
        me "Miku..."
        "I asked pitifully."
        me "I'm scared for us here, and you with questions..."
        show mi surprise pioneer with dspr
        mi "Scared? {w}What are you talking about?"
        me "You see, it's very complicated... {w}Are you sure it's going to work out?"
        show mi angry pioneer with dspr
        mi "You're imagining all kinds of stuff."
        mi "It'll work, it won't work..."
        mi "Forgot to ask you what would work. Take my hand quickly and let's go."
        "Angrily she demanded."
        "She didn't ask again about the treehouse and my reservation."
        hide mi
        with fade
    scene bg ext_square_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    "On these concrete slabs, in this red-hot air, so many worldly dramas, tragedies, comedies played out..."
    "It seems to me that if the camp had self-awareness, it would be an extremely benevolent and positive being."
    "Such as Miku."
    "He would always have a story or two at the ready, a comforting lollipop and a warm friendliness."
    "And you could say that every pioneer who leaves here takes away a piece of the camp, thereby impoverishing this chthonic being."
    "But in reality, they're just carrying the warmth and light they've been charged with during those three weeks - carrying them to where they're needed most."
    "Into other people's hearts."
    if alt_day6_mi_7dl_left:
        "My story doesn't have a very wonderful ending - in fact, I've personally given up on any wonderfulness."
        "Not because I'm such an idiot - it's just that Miku's future seemed a little more important to me than my own momentary whim."
        "A bird is born to fly, not to walk the earth. Miku was born to carry music to souls, not to make borscht at home."
        "So much for my bitter logic."
        "On the other hand, as I now suspect, I had only the illusion of choice."
        "The illusion of freedom of choice."
        with fade
    else:
        scene
        $ renpy.show("bg ext_square_day", what = Dawn("bg ext_square_day"))
        show mi smile pioneer
        with dissolve
        "Miku didn't really care about all that high-spirited angst: grabbing my paw, she raced forward in cruising mode."
        me "Where are you going in such a hurry?"
        mi "No time to explain, let's go!"
        hide mi with easeoutright
        "She sprinted forward even faster - all I had to do was move my limbs in an effort not to stumble."
        stop music fadeout 5
        $ persistent.sprite_time = "day"
        $ day_time()
        scene bg ext_house_of_un_day with dissolve
        play sound sfx_open_dooor_campus_1
        pause(1)
        scene bg int_house_of_un_day
        with dissolve
        play ambience ambience_int_cabin_day fadein 3
        play music music_7dl["you_are_human"] fadein 3
        "It was only when the door closed behind us that Miku let go of my hand and took a breath."
        "Honestly, I didn't see the reason for such a terrible rush, but I prudently didn't ask any questions."
        "You never know..."
        show mi normal pioneer with dspr
        mi "Sit on the bed for now."
        "She ordered, tugging a hollow Japanese valise from under the bed."
        "A moment, and the side wall was gone, and Miku moved into the closet, from where several dresses, laundry bags, shoes, and who knows what else flew toward me almost simultaneously."
        "I tried to catch it all, but the toe of her rock shoe hit me hard in the shin and I caught the hint."
        "Quietly I huddled in a far corner, making a dugout out of my pillow in case anything else came flying in."
        scene
        $ renpy.show("bg int_house_of_un_day", what = Noon("bg int_house_of_un_day"))
        show mi smile pioneer
        with dissolve
        "Miku stopped for a moment."
        "She giggled as she looked at my frightened face."
        me "Very funny."
        mi "Isn't it?"
        "She giggled again."
        mi "Mighty Semyon is struck down by flying rags."
        with fade
        "Apparently, after pulling out all the essentials, the Japanese woman nodded contentedly and slammed the door - so much so that the windows shook."
        me "Look! Does it have to be like this - all with all the ramming and the psychos?"
        show mi laugh pioneer with dspr
        mi "Wow, what a gentle nature."
        me "It's nothing delicate, it's just the way you do things... {w}It's like you've got a demon of destruction inside you."
        show mi happy pioneer with dspr
        mi "Silly Senechka."
        "She left alone the suitcase she had been fighting with during my speech, and sat down on the edge of the bed next to me and touched my hair with the palm of her hand."
        mi "We've talked about this before, remember?"
        me "About what?"
        mi "About the breakups, Senya."
        mi "I don't remember."
        mi "About the partings and the departures. The farewells - you Russians like to suffer and dig in yourselves."
        me "Russians... {w}You're Chinese, aren't you?"
        show mi normal pioneer with dspr
        mi "Only half Russian!"
        me "So what are we talking about?"
        "I tried to delicately get the conversation back on track before I was confused by the chattering again."
        me "You and I were supposedly talking about something..."
        me "About the breakups. {w}Although I don't remember any of that."
        show mi shy pioneer with dspr
        mi "Actually, it was allegorical."
        mi "Just wanted you to figure it out for yourself."
        mi "As long as I'm here tossing and screaming and rattling, I'm invulnerable to ennui and moping."
        mi "And I don't want to get raspy so you'll remember me with red eyes and a swollen nose, okay?"
        show mi happy pioneer close with dissolve
        with vpunch
        "With two fingers folded, she slapped my forehead:"
        mi "So get it together and stop shining that sour face and help me with the bedding!"
        "Clawing the resulting slide on the bed, she whisked that one into the ample womb of the suitcase and circled the bed with an inviting gesture."
        me "And you?"
        mi "What do you mean?"
        me "What are you going to do?"
        mi "Don't you get it?"
        show mi grin pioneer with dspr
        "With a wink, she unbuttoned the top button of her shirt."
        mi "Interrupting and distracting you in every way possible, of course!"
        me "You serious?"
        th "Is she out of her mind?!"
        show mi laugh pioneer with dspr
        "Miku laughed:"
        mi "I was talking about a change of clothes - you have to turn in your uniform!"
        show mi normal pioneer with dspr
        mi "What were you thinking?"
        with flash_pink
        "I rolled me eyes and crawled off the bed."
        hide mi
        with fade2
        pause(2)
        scene bg int_house_of_un_day
        with dissolve2
        "With one last grin, Miku opened the closet door, and a moment later a shirt and skirt lay on the edge of the makeshift screen."
        "And a few minutes later, a transformed Miku appeared before me."
        show mi grin casual with dspr
        mi "Well, it's not a pioneer uniform, of course..."
        "She muttered."
        "And I agreed that yes - it really isn't it."
        me "Brilliant!"
        mi "Not counting the tracksuit, this is the only outfit from the house that Olga Dmitrievna-san has agreed to consider decent."
        me "Agreed?"
        show mi cry_smile casual with dspr
        mi "Yes. She called the others pornography and told me not to show up in public wearing them."
        "Miku mocked the counselor amusingly and very similarly."
        mi "She also warned me that she wouldn't let me on the bus if I wore a dress."
        mi "Damn, Senechka! I'm not three years old, why can't I wear whatever I want?"
        me "Because there are certain rules?"
        show mi dontlike casual with dspr
        "Miku snorted unhappily."
        mi "And my costume is so great - cozy, comfortable."
        mi "But I ruined it, Masha the slob."
        mi "The first week I ruined it - we went to the first campfire, everyone dressed warmly, and me too."
        me "Not so much from the cold as from the mosquitoes."
        "Miku nodded thoughtfully."
        mi "You might be right, I don't know."
        mi "Anyway, when we got here and sat down, I wasn't really looking where I was sitting."
        show mi sad casual with dspr
        mi "I'm used to everything being clean, sterile, and well-kept in my home country."
        mi "So I just fell in without looking."
        mi "And there's tar. Gross!"
        mi "Why are you giggling?! {w}It doesn't come off or come off at all!"
        mi "Especially because it's like a plush, soft, soft material - I was trying to get one spot off, and I got all the others dirty."
        show mi smile casual with dspr
        "Crumpling the suit, Miku tucked it deeper into her suitcase and waved her hand for me to help."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_mi_7dl_departure_lone:
    scene bg ext_square_day with dspr
    play music music_7dl["tilltheend"] fadein 3
    play ambience ambience_camp_entrance_day fadein 3
    "I didn't have things to pack."
    "I had no people to say goodbye to."
    "Lightweight is a tumbleweed, not attached to anyone and not staying anywhere for long."
    "Perhaps this is my cross - the constant pursuit of the horizon?"
    "Even though I'm a fiercer homebody than I am."
    "But from the gate the buses are already trumpeting their arrival at our souls."
    scene cg d7_leaving_no_sh_7dl
    with dissolve
    "So it's time."
    "I don't mind constantly severing connections and acquaintances - it comes easy to me."
    "But, hell, I'm sick of living out of a suitcase."
    with fade
    mt "Kids, is everyone here?"
    "I slipped into the back of the huddle of pioneers and answered for everyone with an affirmative mooing."
    "Everyone's here. Only two pioneers our dearest counselor has already managed to lose."
    "Not that I care that much about Shurik's fate..."
    mt "I declare a ten-minute standby before we leave, if anyone forgot to do their chores, hurry up!"
    "None of ours moved from their seats - they were all firm, grated, not the first year married, not the first time in camp."
    "Everyone already knew the order and the rules."
    mt "Semich, will you sit with me?"
    "I shrugged."
    "The place is as good or better than any of the others."
    mt "Then take the first seat and wait for me. I'll be there soon."
    "I nodded and climbed into the womb of the bus."
    scene bg int_bus with dissolve
    "Across the aisle from us, just behind the bent glass of the driver's cab, some bales, purses, and bags were piled in disarray."
    "I had to sit on the other side."
    "The pioneers were passing me by, throwing strange looks in my direction every now and then."
    "I almost didn't even react anymore - I was used to it."
    "Ten minutes later, the trills of the janitor's whistles sounded, and Olga Dmitrievna landed on the seat next to me."
    show mt normal pioneer with dissolve
    mt "Syomich, why so sour?"
    "I undefinedly twitched my shoulder."
    "But the counselor seemed incapable of taking a hint."
    mt "Relax, Syomich!"
    stop music fadeout 4
    stop ambience fadeout 4
    "She clapped me on the knee."
    mt "It's going to be okay - you'll see!"
    play music music_7dl["tellyourworld"] fadein 3
    hide mt with dissolve
    "She got her knees on the seat and turned around in the cabin:"
    mt "Ready, kids?"
    "And the «kids» responded:"
    voices "Ready!"
    "Shouted back to her, and Olga smiled smugly, looking at me."
    mt "Then let's go!"
    "And I shrugged and turned away to the window."
    "It is always so easy to dream in the reflection of my own eyes, so easy to imagine that the eyes reflected in the glass are not mine, but..."
    "It only made me more bitter and disgusted."
    "My summer was ending so disgustingly that, really, I wish I had..."
    "But I didn't have time to finish my regret because the player clicked - by itself - and a short line popped up on the screen."
    "I guess this world doesn't hate me after all?"
    "I put my headphones in my ears and covered my eyes."
    scene bg int_bus_people_day with fade
    play sound_loop sfx_bus_interior_moving fadein 2
    "{i}Let's stop shaking and run up into the sky!{/i}"
    "{i}Forget the rules - there are more important things!{/i}"
    "{i}Let the song on your lips lead you where you have not been.{/i}"
    "{i}And it's all the warmer for the words inside that pull you along - go on! Come on! Hurry up!{/i}"
    "{i}And all the wonders that send in the way.{/i}"
    "{i}I'll teach you everything I know, of course.{/i}"
    "{i}Uniting the dots on Earth in that infinite sphere where you and I are.{/i}"
    "{i}I'll bring you happiness, I can do it.{/i}"
    "{i}I'll sing all the songs I know.{/i}"
    "{i}And the circle will close again - and I don't care where you are, you just reach out your hand.{/i}"
    "{i}And tell the world about us…{/i}"
    "Song-prayer, song-dream - we all know that a deity exists as long as at least one believer exists."
    "And I... I believe in Miku."
    scene cg d6_mi_vyluthere_7dl
    show anim_grain
    with dissolve
    "There once was a Girl who was born in a world that favored oddities."
    "She could do anything that came into her head."
    "But most of the time she just sang into the open sky."
    "Of thoughts, of time."
    "About people."
    "She was very lonely in her world of infinite possibilities."
    "Until one day a dark window opened right up in the sky."
    "There was a high hill with a winding road running through it - it was so nice to walk there and catch the rain with your lips."
    "The girl ran as fast as she could to get a closer look at the marvelous, unseen wonder."
    "How - she's not alone in the world!"
    "How many times she thought about what would happen, what would happen if one day she met someone else."
    "Imagined the meeting in detail, invented questions and answers for herself and the other person, songs, topics of conversation..."
    scene cg d6_mi_farewell_7dl
    show anim_grain
    with dissolve
    "The wind whistled in her hair, the grass beat the heavy spikes on her bare feet as she ran up the hill: faster, even faster!"
    "And there..."
    mi "Kon-ni-chi-wa?"
    "The voice broke in an electronic shiver."
    "The dark window appeared to be a regular rectangle of very, very thick glass."
    "It was dark because it was deep night on the other side of the window."
    "Only the light coming in from this side captured the features of the face, the reddened eyes, and the frantic drumming of the keys with fingernails."
    "On the right you could see a tablet with a vaguely familiar blue-green sticker lying derelict on the table."
    "There was more to see, but that wasn't what Girl was interested in."
    "It was the eyes she was scrutinizing."
    "Familiar."
    "The nonexistent ones."
    "The ones that she had seen in her dreams all her life and sang to them without being embarrassed, for it is silly to be embarrassed about singing when you are alone in the world."
    mi "Kon… ni… chi… wa?"
    "She repeated again, not sure if she had been heard."
    "Very saddened by this."
    "He must have heard it, he must have smiled and cheered her - otherwise why is he sitting there now, very tired, you can see that!"
    scene cg d7_me_epilogue_bus_7dl
    show prologue_dream
    with dissolve
    "Why is he... on the other side?"
    "On her toes, she put her palm on the glass."
    "The glass was cold."
    "And the boy on the other side didn't notice anything."
    "And he didn't seem to move."
    stop music fadeout 5
    stop sound_loop fadeout 5
    mi "Se-nech-ka?"
    scene emptiness_7dl behind int_bus
    $ renpy.show("int_bus_7dl", what = Notch("int_bus_7dl"))
    with flash
    play music music_7dl["are_you_there"] fadein 3
    "I cried out and woke up."
    "Woke up..."
    "Alone."
    "There was no one beside me, the steering wheel was pristinely empty."
    "I turned around, glanced back, there was no one there either."
    "It was as if an old bad dream from the land of Childhood had come true: I was the last man left on Earth."
    "And that emptiness..."
    "Through the impenetrable blackness there was not a ray of light."
    "It was impossible to tell the time of day or even the passage of time."
    "If it weren't for the faint glow of the lamps inside the bus, it would have been dark inside."
    $ renpy.show("int_bus_7dl", at_list = [sdl_transform6], what = Notch("int_bus_7dl"))
    with dissolve
    "Moving slowly, as if in a dream, I rose from my chair and stepped out into the passage in the middle."
    "From here it seemed endlessly long, and at the end there was no light at all."
    "And yet somehow there was no fear at all."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_mi_7dl_departure_a2th:
    scene bg ext_no_bus with dissolve
    play ambience ambience_camp_entrance_day fadein 3
    play music music_7dl["the_way"] fadein 3
    "Time went on, while we were packing and saying good-bye, it turned out that noon was impossibly close, and it was as if I had no belongings to pack, either."
    "So we rolled Miku's traveling bag out to the gate and sat ourselves down in our favorite spot, where we both went through so many thoughts."
    me "It's even kind of weird that you went here to think, too. Are you sure you're not lying?"
    "I asked."
    show mi smile casual with dissolve
    mi "I'm lying, of course."
    "With a chuckle the girl responded."
    mi "That's so relevant now - when we're about to separate."
    "Her voice trembled a little - a little noticeable to me now - and I hurried to put my arm around the Japanese girl's shoulders."
    "The old me, of course, wouldn't have noticed - I didn't care for silly things like accurately recording other people's sighs and reflections."
    show mi sad casual with dspr
    me "I'm sorry."
    "I repented."
    me "It's just this whole situation that's making me so depressed that I'm unwittingly snapping at people around me."
    mi "Senya, can you influence her, this situation?"
    me "No, of course not. I can just wait."
    show mi grin casual with dspr
    mi "That's when you relax, okay? {w}And remember: it's nobody's fault."
    me "It's nobody's fault."
    "I obediently repeated."
    mi "Much better!"
    "Praised the Japanese woman."
    "And touched my cheek with her lips."
    mi "Say that to yourself more often and you'll be fine. {w}I promise!"
    play sound sfx_bus_honk
    pause(1)
    scene bg ext_bus1_7dl with dissolve
    play sound_loop sfx_bus_idle fadein 3
    "But they wouldn't let us finish."
    "With a loud honk of the horn, several buses drove out onto the paved area in front of the camp gate."
    "At once several return packages from the land of Happiness to the world of Genesis."
    "Even if someone on the other side of the three-hundred-kilometer stretch is expecting summer on the scrapheap, loyal friends, and boundless happiness, he will hardly get on the bus in happy impatience."
    "Attracted by the klaxon, from behind the gate the counselors appeared first, followed by their charges."
    "Moscow time was half past twelve."
    "Parting time. Forgiveness and farewell."
    mi "Shall we go?"
    "Miku nudged me in the side with her elbow, drawing my attention - Olga Dmitrievna was hurrying from the gate."
    scene cg d7_leaving_no_sh_7dl
    with dissolve
    mt "Miku, Semyon, are you packed?"
    "Without waiting for our answers, the counselor took a seat near the bus - and immediately waved her hands at Lena and Alisa, staggering at the gate."
    "Following them, the other pioneers pulled up."
    "Now I'd give a big speech about how we went through the crucible without losing a single soldier, but the fact was somewhat different."
    mt "With the exception of Trofimov, everyone should be in place."
    "She carefully counted us head to head once more, then with a nod allowed the driver to open the luggage compartment."
    with fade
    "There immediately flew cloth suitcases, valises, and the occasional fancy gym bag with three white lines down the center."
    "And another minute later, the seats in the cabin were occupied by my frustrated comrades-in-arms."
    "Somehow it turned out that Miku was more important to me than the rest of the collective."
    "Unseemly. {w}What can you do?"
    stop ambience fadeout 3
    stop sound_loop fadeout 3
    play music music_7dl["tilltheend"] fadein 3
    scene bg int_bus with dissolve
    "Anyway, Miku and I took our seats in the back of the middle of the cabin."
    "The bus was meant for a lot more pioneers, but since we had such a small group..."
    show mi smile casual with dissolve
    mi "We'll go together."
    me "Yes."
    "Miku clapped her hands enthusiastically."
    show mi happy casual with dspr
    mi "And we'll talk all the way!"
    "I was saved from answering that line, too, by the counselor's question:"
    mt "Are you ready?!"
    "And I shouted in tone to everyone:"
    me "Ready!"
    "The bus hurled itself into the red-hot day."
    scene bg int_bus_people_day with fade
    play sound_loop sfx_bus_interior_moving fadein 2
    "Miku was going to put her plans into full effect - and chat with me all the way back to town."
    "Though you couldn't say I resisted so much."
    "In spite of my beloved's certain noisiness, there was one redeeming quality about her: her voice was pleasant to listen to."
    "And she spoke more matter-of-factly, even though she went from fifth to tenth."
    "You just had to learn to listen."
    "Learning to hear."
    "I liked the way it sounded myself."
    th "I learned how to {i}hear{/i} Miku."
    "I said to myself, and all the trials to come were no matter."
    "For the most important thing, as it turned out, I only just got through without getting out of that chair."
    mi "And then Pa says, 'If she doesn't want to wear a yukata, no one will force her! At least let her wear pants!' Ma got so angry then!"
    me "Was it so hard for you?"
    "Miku was embarrassed."
    mi "You see, there are several rituals and omens associated with these clothes - all about love."
    "She twitched her chin briefly:"
    mi "Back then I wasn't ready for... well, for my name and love to be put in the same sentence."
    me "And now?"
    "Miku laughed and changed the subject."
    scene cg d7_mi_epilogue_bus_7dl
    with dissolve
    "Miku's laughter is the strongest weapon against all anxieties and fears, that's what I've learned."
    "It wasn't clear how I'd managed to survive to this day without knowing or meeting this girl..."
    "It wasn't clear how I... we... how we were going to get on."
    "We can't clutch at each other's palms and not unhook them so much as to become one, not let anyone separate us."
    "We can't, can we?"
    "Because that's utopian."
    "She has age, career, citizenship."
    "I have nothing at all - with unknown prospects."
    th "Which means what?"
    "Before I could think about it, the bus suddenly howled like it was on a particularly steep slope, rushing forward, still forward."
    "You couldn't see anything in the windows directly ahead and to the sides, just an impenetrable void."
    dreamgirl "The end of the line..."
    dreamgirl "Your story ends about here, give or take a couple of kilometers."
    dreamgirl "So remember everything around here in as much detail as you can, kiss your girl goodbye - it's allowed, if I'm not confused about anything."
    th "And then what?"
    dreamgirl "Then?"
    "A bitter chuckle was heard in the split personality's voice."
    dreamgirl "Out you go, of course. The train has arrived at the terminus of the depths."
    "I shook my head sharply and looked around."
    "There was still the noise of negotiations, the hum of the engine, the heat, and the smell of gasoline in the cabin."
    "But it was as if everything had been relegated to the background, blurred, muffled."
    stop music fadeout 3
    stop sound_loop fadeout 3
    scene bg int_bus_people_day
    with dissolve2
    play music music_7dl["unholy_you"] fadein 3
    "And a few more seconds later, it started."
    "I didn't really understand how it worked, but it seemed that my active attention was the only thing keeping objects and people near me."
    "I turned slightly away from the flags next to the driver's seat - and they were gone."
    "The driver himself was missing, too."
    "There was no one behind me for a long time, either."
    "The things scattered on the backs of the seats, the shoes exposed in the aisle, the panamas on the top shelves - they disappeared as soon as they were out of my sight."
    scene bg int_bus
    show mi sad casual
    with flash
    me "Miku!"
    "I turned to Miku and stared at her point-blankly."
    "Tried to fix her in my mind as clearly as I could, making hundreds of associations and memories - and this week was proving to be generous with memories."
    "It was like the wind was really trying to keep us apart, and we kept holding on and holding hands."
    "And when the hum of the engine fell out of consciousness, I suddenly knew what I should do."
    "I should have just..."
    me "Where was it?.."
    "I frantically searched my pockets."
    "The object I was looking for was, of course, in the very last pocket I searched."
    "The law of meanness in action."
    me "Miku."
    "I took her by the shoulders and looked into her eyes."
    me "Everyone around here is gone, but you don't have to be afraid."
    show mi scared casual with dissolve
    "The Japanese woman looked around incomprehensibly - her eyes widened in amazement as she realized my point."
    "But intelligently she did not ask any questions."
    "Apparently, she knew she should do something now."
    "And we can chat later."
    "You just have to figure out what to do."
    "And I, judging by my confident look, very much knew."
    me "Don't worry, it's all..."
    show mi normal casual with dspr
    mi "Fine?"
    "Or thought I knew. {w}However, you shouldn't believe everything you think."
    "The phone has three percent charge left."
    "Three percent is two minutes of talk time."
    "Or one text message."
    "Or one open page in the browser."
    show frame at truecenter:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 0.8 zoom 1.0 xalign 0.5 yalign 0.20
    show cam_ui at truecenter:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 0.8 zoom 1.0 xalign 0.5 yalign 0.30
    "Or..."
    "The one and only proof that I'm not crazy."
    pause(1)
    play sound sfx_7dl["snap"] fadein 0
    scene white with flash
    pause(1)
    stop music fadeout 5
    with fade2
    "And I didn't fall in love with a fictional image."
    scene bg int_bus with dissolve
    "No, honey. {w}It's not fine at all."
    "I saved the picture and backed it up to the memory card before the machine finally shut down."
    $ persistent.sprite_time = "night"
    $ night_time()
    scene anim prolog_2 at zenterleft
    show mi sad casual
    $ renpy.show("gfx bokeh", what = D3_intro("gfx bokeh"))
    with dissolve
    play music music_7dl["but_why"] fadein 3
    "And when I looked up - Miku was sitting there, pale blue - and the sunlight falling on her face on the right was somehow reverberating with silver."
    "And then it became - the moon."
    "All around became night."
    "The bus was gone, just the two of us and the endless emptiness around us."
    "This must have been the very boundary the miracle extraction device was guarding."
    "Miku's miracle - from me."
    "My miracle - from Miku."
    "And in the whirlwind of mutually torn wonders, it was so meaningful not to lose my sensitive fingers."
    mi "Senechka, I don't feel well..."
    "She muttered."
    "Her lips quivered."
    mi "Senechka, why is it so bad? I'm not just motion sick, am I?"
    me "No, honey, that's not it at all."
    "Rather, it's that the disparate pieces of the mosaic are finally falling into place in my head."
    "The creators of the synthesizer, four versions on the market, the last of which I even sang along to, reveling in her «engrish»…"
    with vpunch
    "I remembered that she belongs entirely to virtual space."
    "And with it, no matter how hard our brightest minds fought, we still couldn't build a bridge."
    dreamgirl "Say your goodbyes, Semyon."
    "The voice in my head was cold and dispassionate."
    dreamgirl "She can go no further with you."
    "Miku was becoming more and more transparent."
    th "But why?!"
    dreamgirl "Because she doesn't belong in your world."
    th "But..."
    dreamgirl "And you don't belong to her's."
    th "What do you mean by that?"
    dreamgirl "You are a guest here. Soon you will go home, and she will stay here."
    show mi sad casual tr1 with dissolve
    "I turned sharply to Miku."
    th "No, there must be another way!" with vpunch
    mi "Senechka..."
    stop music fadeout 4
    dreamgirl "Don't torture yourself or her - let go."
    show mi sad casual tr2 with dissolve
    if lp_mi > 16:
        if alt_hpt >= 9:
            play music music_7dl["unfinished_life"] fadein 3
        else:
            play music music_7dl["longing"]
    else:
        play music music_7dl["unforgotten"]
    mi "So that's the way it's supposed to be, huh?"
    dreamgirl "Where you're trying to get her out there's no way for her, how can't you understand that?"
    dreamgirl "Because she{w=0.5} doesn't{w=0.5} exist there."
    "And as much as I hated to agree with the abomination in my head, there was horrifying - but logic in the words."
    th "But I don't want to."
    show mi sad casual tr3 with dissolve
    me "I..."
    "I'm out of breath."
    me "I can't."
    "I wanted to let go of Miku, but she grabbed me tighter on her own."
    mi "Senya... {w}Don't let go. No way, do you hear me?"
    dreamgirl "It won't work. Don't you understand yet?"
    mi "Senya... Please."
    dreamgirl "Leave the story alone."
    dreamgirl "It's time to go home."
    dreamgirl "Wake up!"
    "And I…"
    if lp_mi > 16:
        menu:
            "Kept resisting":
                $ alt_day7_mi_7dl_pt = 1
                scene anim prolog_2
                with flash
                "I caught her fingers and squeezed, squeezed as hard as I could!"
                "Miku cried out loudly in pain, her face contorted, but there was no time for pity now."
                "I {b}could not{/b} afford pity."
                "Not even toward the most important person."
                "Or rather, towards her I could not afford it."
                "For it was up to me... it was up to us whether we would be each other's dissolved dream or our true reality."
                "Her fingers were cold and clammy with sweat, her eyes rolled back, and through the transparent outline you could see the receding perspective of the bus."
                "She was silent, biting her lip."
                "At one point a bright scarlet droplet trickled down from under her upper lip."
                "And her fingers trembled, relaxing."
                if alt_hpt >= 9:
                    scene anim prolog_1
                    with flash
                    "To find my fingers in a second and intertwine with them in a single knot-lock."
                    mi "I'm with you, Senechka."
                    "Whispered ghostly lips."
                    mi "I've got it."
                    "The bus skidded and skidded across the asphalt unseen in the dark."
                    "I forgot the last time I inhaled - and only paralyzed by the fear of loss, I went on and on looking at the girl losing her materiality."
                    "I continued and continued to clench my fingers."
                    scene
                    $ renpy.show("bg int_bus_night", what = SS_com("bg int_bus_night"))
                    with fade
                else:
                    "Miku trusted me and let me do everything myself."
                    "She turned her hand so that I could hold it comfortably, pressed against me."
                    mi "Don't...don't let go..."
                    "She babbled incoherently."
                    me "I won't let go."
                    scene
                    $ renpy.show("bg int_bus_night", what = SS_com("bg int_bus_night"))
                    with dissolve
                play sound sfx_wind_gust
                "The invisible whirlwind grew stronger - the outlines of the bus became blurred, and it was hard to tell which was dream and which was real."
                "The only thing that remained constant was the force that was trying so hard to pull us apart."
                "It tore and yanked at us, pulling and pulling in different directions."
                "Miku moaned with every tug, and all I could do was sit there, hold on with all my might and pray to all the known gods."
                "Meanwhile, little by little, discernible silhouettes began to appear outside the windows."
                "And that meant that our journey had come to an end."
                play sound sfx_bones_breaking
                scene bg int_bus_warp_7dl
                if alt_hpt >= 9:
                    hide mi
                    with dissolve2
                    "But the intertwined fingers weren't easy to unhook."
                    "Though I had come close to my limit."
                    "As it was in a distant, distant childhood, when we stood hand in hand and shouted 'Ali Baba! About what, servant?' and held on with all our might so that no one could tear our clutched palms apart."
                    "So that no one could weaken our order."
                    "For we are... Together."
                    me "On the fifth. The tenth..."
                    "I growled, balancing on the brink of unconsciousness."
                    "And suddenly I realized that I could not overcome my limits."
                    scene black
                    with fade2
                    stop music fadeout 5
                    "Miku shrieked and disappeared..."
                    dreamgirl "We're here. Your stop, Syomich. Goodbye."
                    "My heart skipped a beat..."
                    me "Miku!"
                    "There was silence all around. I couldn't see anything, but I knew exactly where I was going."
                    "To where she is."
                    pause(1)
                else:
                    "That last tug turned out to be an impossible, crazy force - I literally felt something break in my wrist."
                    "Both in mine and hers."
                    "Fairyland was ready to cripple me - but not to give up the cyan princess."
                    "I had foreseen everything - and how hard we would have to try to keep us apart."
                    "But the fact that my wrist would be broken with a jerk, I could not foresee."
                    "The pain was terrible."
                    "Scarlet, sprawling - it gnawed into the bone, and flaming needles ran up my forearm."
                    dreamgirl "What are you doing, you idiot? You're hurting her, for real!"
                    th "I can't let her go! I'd rather die than do that!"
                    dreamgirl "Are you really ready for this?"
                    show unblink
                    if dr:
                        scene bg intro_xx
                        show prologue_dream
                        with dissolve
                        play sound_loop sfx_bus_interior_moving fadein 4
                        "And I suddenly realized I was back home."
                        "Back to my eighteenth year, to winter, to a man freezing in his fish-fur coat over the wheel in the cabin of a decommissioned bus."
                        "Perhaps if we had held on somehow differently or just tighter..."
                        "Driven by intuition, I pulled up the cuffs and stared with mute anger at the sinuous scar crossing my wrist."
                        th "Well, so be it."
                        dreamgirl "Are you really willing to go that far?"
                        "I could barely make out the words. The voice that had been my camp companion had come into my world, into this dank, gray reality, to... what? Mock me?"
                        dreamgirl "Just don't tear her arm off there, lover boy."
                        "The voice was briefly interrupted."
                        dreamgirl "Bye, Semchik. Be happy."
                        th "Stop! Where are you..."
                        "The brakes squealed sharply, and I was thrown forward, hitting my head hard against the padded handrail on the front seat."
                        "From the driver's cab came a gagging screech, the emptiness thickened, and the icy New Year's Eve evening froze in a grotesque radial waltz."
                        with vpunch
                        "Hit…"
                        "And everything went quiet."
                    elif loki:
                        scene bg ext_winterpark_7dl
                        show prologue_dream
                        with dissolve
                        "And I suddenly realized I was back home."
                        th "I lost."
                        "You can't win the game if you don't know the rules."
                        "This story didn't have a happy ending from the beginning."
                        "It ended exactly as it began. {w}With death."
                        pause(1)
                        "The cheerful music and joyful voices that came from the rink grew quieter and quieter."
                        "But the voice that had served as my interlocutor and sarcastic commentator for the past week, I could still hear it."
                        dreamgirl "I didn't think you'd get this far."
                        "He sounded unaccustomedly sad this time."
                        dreamgirl "And it's beautiful here. It's a shame things like this happen in places like this."
                        "I didn't quite understand why he was saying that, but I couldn't argue with him."
                        "It really is beautiful. A pity indeed."
                        dreamgirl "Take care of yourself, Semchik. Take care of her, too."
                        "A shroud of inevitability slowly covered my eyes."
                        "I didn't need to specify who I was supposed to take care of."
                        me "Mi...ku..."
                        "And everything went quiet."
                    elif herc:
                        scene bg int_store_7dl
                        show prologue_dream
                        with dissolve
                        "And I suddenly realized I was back home."
                        th "That was it."
                        "There wasn't more than a moment between my return and the piece of lead in my head."
                        "And then I heard a voice that hadn't been here the last time..."
                        "That one was tall, girlish. And he only said four words then."
                        "And this one, frankly, is getting boring."
                        dreamgirl "You're such a stubborn fool. Are you really willing to get a hole in your forehead for a chance to be with her?"
                        "It's like time has stopped around here."
                        th "As it is. What difference does it make now?"
                        dreamgirl "Don't let her go, you hear? It's all in your hands now!"
                        "Another silly joke? If it were, I wouldn't be here for anything."
                        "But nevertheless, I mentally nodded. Because that's exactly what I wanted. To grab her and never let her go again."
                        me "Well..."
                        "I didn't have time to say anything else."
                        play sound sfx_7dl["makarych"] fadein 0
                        scene believe_in_pain with flash_red
                        with fade3
                        "Gunshot…"
                        "And everything went quiet."
                    scene black with fade2
                    pause(4.4)
                    stop music fadeout 3
            "Backed off":
                call alt_day7_mi_7dl_departure_a2th_retreat
            "My story ends here" if persistent.alt_binder:
                $ alt_day7_mi_7dl_pt = 3
    else:
        label alt_day7_mi_7dl_departure_a2th_retreat:
            $ alt_day7_mi_7dl_pt = 2
            "And it suddenly dawned on me."
            th "She's in pain! I'm hurting her while I'm grabbing her arms here."
            scene bg int_bus_warp_7dl
            with touch
            "It was as if I had come from a planet where the atmosphere was hostile to a girl - and she was suffocating every moment she spent there."
            "Of course I was selfish."
            "But not that selfish."
            "I wanted to keep Miku by my side, to spend time by my side - perhaps even a lifetime."
            "But now that the girl's life was at stake - I flinched and backed away."
            scene bg int_bus_warp_7dl
            with touch
            "I had no right to dispose of someone else's life."
            "A cloud covered my eyes, and while I furiously wiped away the tears with my fist, even the very mention of Miku melted into the night air."
            scene bg int_bus_night
            with dissolve2
            "I'm the only one left."
            "And the open door of the empty bus."
            "I don't know how long I sat like that, how long I waited, but I finally got up - and headed out into the unknown."
            "I felt no fear - whatever the trials to come, it could hardly be worse than now."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_mi_7dl_neu_human:
    scene bg int_hospital_hall_day_7dl with dissolve
    play ambience ambience_medstation_inside_day fadein 3
    play music music_7dl["refuse_to_believe"] fadein 3
    "I don't know when or how it's going to end here."
    "I can guarantee neither a good nor a bad outcome, simply because nothing depends on me."
    "For the first time in my life - not myself, with my own hands - buried any chance of a happy outcome, but a victim of force majeure."
    "And that made it uncomfortable and creepy."
    with fade2
    "All I could do was let the dragging of time pass me by, dutifully and patiently waiting for it to be over."
    "When it's all..."
    "I was very afraid of waiting - what would happen when it was over, when the delayed number of hours, minutes, seconds came out..."
    "Because it was more than obvious - I didn't deserve a happy ending, I didn't deserve one."
    "The odds are... Minimal."
    "Behind me was the hectic jet lag, the names, the reconciliations, the hastily arranged documents - as it turned out, two invitations from residents were enough, then I just had to come to get the tickets..."
    "But now it all sounded as if someone had pushed me forcefully along the time vector, stuffing my head with someone else's memories in return."
    "Though I remembered the gaunt old man sitting next to me a little better than I remembered the events of the last few days."
    "Or rather, I didn't know his name. Only the last name."
    "Sakishita-san, agent, producer, and babysitter for a girl I know."
    "By Random, and I had the conscience to say he was only interested in her as a source of income..."
    "The old man's face twisted with no small amount of anxiety, and his right eye occasionally began to twitch finely."
    "It looked pretty creepy, coupled with the burst vasculature and the facial features sharpened by fatigue."
    with fade
    $ meet('sak','Sakishita')
    me "No hope, huh?"
    show sak scared suit with dissolve
    sak "I don't know, Semyon-san."
    "Politely replied Sakishita."
    sak "But we found the best doctor we could."
    with fade
    "I don't know where or what broke, but in my coat in the back seat I opened my eyes not at all ragged, old me - no, I was back in some ways completely, the person Miku remembered me to be."
    show sak normal suit with dspr
    sak "I'm being very frank with you - you're strong, you'll pull through."
    "He was quiet and added in a low voice."
    sak "Otherwise Miku-san would not have chosen you. {w}May you be strong."
    me "Yes."
    th "I'm hanging in there, of course. That's what they taught me well - to hold on."
    "I'm holding on, though I'm not entitled to a miracle."
    "But there's a tiny bit of hope in me."
    th "Perhaps Miku has the right to a miracle?"
    play music music_7dl["refuse_to_believe"] fadein 3
    with fade2
    "I suddenly realized that a few more minutes of waiting would drive me crazy!"
    "I jumped up, took cigarettes out of my coat pocket (a pack had already flown out this morning, and it didn't seem to be the last), threw my coat back on the seat."
    play sound sfx_open_door_strong
    pause(1)
    scene
    $ renpy.show("bg int_opened_door_7dl", what = Dawn("bg int_opened_door_7dl"))
    "At the same time, the door at the other end of the foyer swung open sharply, letting in a sheaf of blindingly bright sunset light."
    "Against this light, the outline of the man, tiredly hunched over, was almost invisible."
    "But he stepped forward."
    play sound sfx_open_door_strong
    "Slammed the door behind himself - my hand twitched, and the door rattled so that I shuddered."
    "And I rushed towards him."
    "Hurried as fast as I could, almost ran!"
    "Sakishita got up to follow me, but he changed his mind, and the foyer was endless, the kind that only Soviet hotels have, and no matter how much effort you make, there's no way you can cross it quickly."
    "It's like a nightmare dream, when you try to catch up with someone and space is stretched by a viscous rubber, forcing you to move in tiny steps."
    if herc:
        "And yet I got my way, we stood in the very center of the hall, the two of us - me, Semyon Sychev, and the man on whom so, so much depended..."
    else:
        "And yet I got my way, we stood in the very center of the hall, the two of us - me, Semyon Persunov, and the man on whom so, so much depended..."
    $ meet('ai','Govorov')
    "Miku's father, my possible father-in-law - Govorov Arkhip Andreevich."
    "Govorov-sama."
    "We had never seen each other until now; Sakishita helped me with all my business."
    "He was slightly taller than the new me-almost no effort had to be made to look into his eyes and see the answer to any question on their bottom."
    "But I couldn't stand it - I turned away. {w}I've always had great difficulty with eye contact."
    "I started to speak, and I coughed: my throat was in spasm."
    me "H-how is she?"
    ai "Ah…"
    "Govorov rubbed his temples, looked through me."
    me "My name is Semyon, I'm... {w}a friend of your daughter."
    ai "Friend..."
    "Govorov squeezed his flushed, inflamed eyes, rubbed them."
    "He should sleep for a few hours, just come to his senses."
    with fade
    "But who could sleep in such a situation?"
    "Tiredly sighed - remembered."
    ai "You're the one she called «Senechka»."
    "I nodded."
    "Govorov dropped a surprisingly heavy, warm palm on my shoulder."
    ai "We meet, at last."
    me "Can I... see her?"
    "My voice changed, and I coughed."
    me "To, well..."
    ai "She's coming out of surgery, son, you can't go to her."
    "He started looking somewhere above my shoulder."
    me "But at least I want to hold her hand... To say goodbye..."
    "For a moment a ray of sunlight broke through the clouds, played in the thin tulle, seeped between the solid vertical blinds."
    "It touched my smoothly shaven cheek, reached my eyes."
    "Now I believed to the end - he really was her father."
    "Two aquamarine pebbles - bottomless as the Sea of Japan."
    "His gaze stopped on me again."
    ai "Goodbye? Are you going somewhere?"
    me "But since she... {w} I just want to remember her alive and cheerful..."
    ai "You wait until she's discharged and you cheer her up - what's the problem?"
    "Govorov was surprised."
    ai "You'll see enough, you'll get bored."
    "And I believed it right away."
    "Because we are all gathered here, weighed down by pain, inextricably linked by close ties to one girl with the singing silver bell of her voice, with endless hypnotizing tails of azure hair..."
    "Men don't cry."
    "Isn't that right?"
    "I jabbed at his chest, into the white hospital gown smelling of disinfection and desperate hope."
    "And it seemed for a moment that it was a gray T-shirt with the inscription «Sovyonok-40»."
    stop ambience fadeout 2
    me "I won't get tired of her."
    me "Never."
    scene anim prolog_2 with fade3
    "Neutral ending unlocked - «Won't Get Tired»"
    play music music_7dl["sam_lullaby"] fadein 3
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("mi_7dl_neu_human")
    show acm_logo_mi_7dl_neu_human with moveinright:
        pos (1600, 1020)
    pause(7.4)
    call alt_7dl_titles
    pause(1)
    return

label alt_day7_mi_7dl_bad_human:
    play music music_7dl["afraid_of_destiny"] fadein 3
    scene anim prolog_1 with fade2
    play ambience ambience_7dl["night_city"] fadein 2
    "It should be understood that 'ex' sounds like 'ekz' - from the word 'exemplar.' Your 'ex' is a specimen of a person who is not good enough for you."
    "Those 'exes' that lit up my life with fleeting fireflies have only added scars on top of existing ones - and now the crusted surface of my heart is almost unbreakable."
    "At least, that's what I used to think."
    "She was wearing a jacket stylized as a low-polygon model."
    "Of triangles."
    "The so-called 'polygon'."
    "Cheap in ordinary times, for it is sewn from scraps of leather."
    "But with a few couturiers, the style was becoming more and more common, and more and more often the logo of a famous manufacturer could be found on the snazzy windbreaker-polygons."
    "Incredibly beautiful."
    "I would have worshipped her until I couldn't remember."
    "If only I wasn't already in love."
    "The bus rushed past me with an icy gust of wind."
    "From the back wall, the LenEXPO logo grinned mockingly."
    "From the fourth to the eleventh of April is Japanese High Tech Week."
    "No wonder who they chose as their mascot."
    scene
    $ renpy.show("bg ext_khruschevka_day_7dl", what = Notch("bg ext_khruschevka_day_7dl"))
    with dissolve
    $ meet('ml','Dude')
    $ meet('ml2','Small guy')
    ml "And what, you believe this nonsense too?"
    "Mockingly, the guy in the windbreaker, the same one Miku was wearing from the bus, said."
    "Also on-trend, the bastard... Shitass."
    "With toothless anger I thought."
    ml2 "Well, why not? Think about it, so many coincidences, how can it all be in vain?"
    "I was wise to keep my mouth shut - I regretted coming here in the first place."
    ml2 "Understand, finally, it doesn't matter if it's an original story or someone else's concoction of the plot - if we all have the same dreams, even the same faces, how can it just be?"
    ml "Maybe."
    "Cut off the dude - he was taller than both of us, though perceptibly lighter."
    "Skinny as a match - but in a fancy jacket."
    ml "If the author has given a rather detailed description of his appearance, then it is not surprising that..."
    ml2 "What looks, you fool! {w}I'm talking about anime-style girls!"
    "Besides the three of us, there were a couple of dozen other people here - they, too, in groups of three or five, were discussing something animatedly."
    ml "Exactly. Big eyes, size five breasts - and yet pure and chaste and not getting married! {w}How do you get into bed with them on the sixth day, I wonder?"
    ml2 "What a... down-to-earth guy you are."
    "The other guy, a smaller, though perceptibly denser, wearing a black pilot-type jacket, exhaled noisily through his teeth."
    "I decided to come to his rescue:"
    me "I think we got off on the wrong foot, buddy-buddies. {w}Let's start by deciding how we feel about our escort."
    ml "He's fooling us."
    "Surely the dude has cut us off."
    ml "Took five grand from us and disappeared into the fog. {w}I don't mind the money - there'll be a cretinism tax, if anything. But I want to see how it all ends."
    ml2 "And I believe it! Because I've seen his eyes."
    ml "What eyes, you fool! His name isn't even Semyon."
    "The dude had resigned himself to the loss of money; worse, he had resigned himself to the fact that the money had not been wasted, and he might well be kicked out into the field and tortured there with hastily stylized interiors and jerks in children's uniforms."
    "His eyes were poker-faced - he expected no miracle from life, was skeptical of everything in advance."
    ml2 "He can be called anything, the most important thing is that he knows the way there!"
    "The little one jumped excitedly in place, stretching his neck in impatience."
    "We stood outside the bus station, all twenty jerks who had given up money in exchange for the promise of a ticket to Fairyland."
    "We smoked a short distance away in full compliance with the new idiotic laws-no closer than twenty yards."
    "I was smoking my 'Rich', the dude was smoking a vaporizer, and the little guy was stretching a hundred-millimeter cigarillo in spite of us."
    "It was suddenly obvious to me how much they disliked me."
    th "Twenty round idiots."
    me "And if not?"
    "I asked, breathing through my breath so as not to spook the miracle."
    ml2 "Jesus, who cares?! Put it all on the line, what are you like grandfathers on pensions?"
    "He heatedly exclaimed."
    ml "That's easy for you to say, you've probably got nothing behind you."
    "The 'dandy man' sarcastically retorted."
    ml "Okay, I kicked mine out for the holidays to my mother-in-law, just to be alone at home for a week to rest - the only joy at thirty-two years, and you?"
    ml2 "What am I?"
    ml "How old are you?"
    ml2 "...forty-two."
    "Calmly answered the little man. And I suddenly realized that he wasn't young at all - good genetics kept his skin firm, but you could already make out the almost invisible gray hair and the wrinkles in his eyes."
    ml2 "I have two children, my eldest is going to give me a granddaughter in February."
    me "And you... You're just going to go off in the middle of nowhere? From them?"
    ml2 "Not just like that."
    "Seriously, the little guy replied."
    ml2 "I'm not that naive, I'm well aware that we're probably - and most likely - being fooled, played on our feelings."
    ml2 "That's why I'm not risking anything."
    "His voice trembled."
    ml2 "But if there is even a tenth of a chance for a miracle..."
    ml2 "I don't want to be punished to death for being a wimp for having a granddaughter, daughters, houses, and an unloved job, when all I had to do was make up my mind once."
    stop music fadeout 3
    play sound sfx_bus_honk
    pause(1)
    play sound_loop sfx_intro_bus_engine_loop fadein 3
    scene anim intro_9
    with dissolve
    "A klaxon sounded from the end of the street, and everyone present shouted and stamped their feet as a bus slowly pulled up to our stop."
    play music music_7dl["what_cost"] fadein 3
    "The same bus that started it all."
    "A red LIAZ, of an old-fashioned design without any ergonomics, with a huge number '410' in the upper right corner of the windshield."
    "At the same time, a new-fangled 'Ant' appeared out of nowhere, emblazoned with Soviet symbols, with a cast figure of an owl on the grille, with a scarlet sticker on the door glass: «Sovyonok-fest»."
    play sound_loop sfx_bus_idle fadein 2
    "A frost ran between my shoulder blades as an old acquaintance smiled at me from the open door."
    "Those present whistled cheerfully, shouted."
    ml "Even the masquerader was brought in."
    "The Dude spat angrily, shutting down his vape."
    ml2 "A masquerader? What's the matter with you?"
    ml "With me? Oh, there's nothing wrong with me. {w}I've just made sure that this whole charade is a clown show."
    "He lifted the bag sharply from the ground, throwing it over his shoulder."
    ml "I want to recoup at least some of my expenses - so don't even ask me to get into that bogeyman and freeze there."
    ml "Adios."
    ml2 "Arrivederci."
    "Answered the little one."
    ml2 "You'd better make a money-back, though, honestly. After all, you've got a whole bunch more to do: waking up for some reason, then carrying yourself somewhere for some reason, breathing for some reason..."
    "The dude almost stumbled and silently put his fist with his middle finger out over his shoulder."
    "For his money, he obviously wasn't going to freeze in a fully authentic LIAZ."
    "He hurried over to the 'Ant' and was the first to jump aboard."
    "The others followed him."
    ml2 "And he would have given half his life for it to be real."
    "Sadly remarked the little one."
    ml2 "He believes so fervently that he's afraid to admit it to himself."
    ml2 "A real Alisafag."
    me "You're not in a hurry?"
    "Suddenly timid, I asked."
    ml2 "No. And where to? My '410' won't leave without me."
    "He extinguished the cigarillo with a quick spit and tossed the butt into the trash."
    ml2 "Third stage. Lungs."
    "Calmly he shared."
    ml2 "A little more and I'll start coughing up blood. So what difference does it make now."
    ml2 "Even if they take me to the woods and kick me in the head, it won't get any worse."
    me "And I... I just read things..."
    "I said helplessly."
    ml2 "Come on, Syomich."
    "Calmly he smiled, and I suddenly realized that he had guessed a long time ago who I was, and why I was here."
    ml2 "It's just that you weren't allowed to go where Miku is possible, and you're afraid to make another attempt."
    ml2 "Because you won't survive it, this attempt."
    me "But... How do you know?"
    ml2 "How do you think?"
    pause(2)
    scene anim intro_10
    with fade
    "Tossing the bag in his hand, he offered me his palm, shook mine firmly - and put his foot on the first step of the LIAZ."
    "The only one who was here."
    "The only one who had the guts..."
    ml2 "It was the only three of us who saw that bus."
    "Without turning around, he reported."
    ml2 "Think about it."
    stop sound_loop fadeout 1
    play sound sfx_intro_bus_door_open
    "The wind carried the last words, and I was left alone."
    stop ambience fadeout 5
    scene bg ext_city_night_7dl with dissolve
    play ambience ambience_7dl["night_city"] fadein 3
    stop sound_loop
    "I thought about rushing after him - or at least to that damn festival of mummery cretins, to, as the dude said, recoup some of the cost."
    "But I stood looking deep into the cabin, where above the wheel, leaning my head against the cold glass, my eyelids closed on the man I never got to be."
    "The choice is made. Another flag in the endless game has been called, and someday it will come back..."
    "We've all become part of a world that makes us sick."
    "The easiest thing left to do is to get out of here as quickly as possible, out of sight and out of mind - the red bus, the man in his fifth decade who dared to trade in an optimized existence for a dash to an unknown future, toward the horizon."
    "Because the organizer is a dressed-up clown, all those who gathered and discounted are naive and sentimental idiots."
    with fade2
    "And life is good, living is great - this universe is gracious to dreamers, it agrees to grant your every wish."
    "Just a little in its own way."
    "Just a little instead of the expected sweetest, most good, reflection of the dreamer, with his eyes and smile, is peeled off the amalgam."
    "Doppelganger."
    "A living walking doll in a wig, with a glued-on smile - can she know that the top of the real Miku smells like eucalyptus and her hair is curled counterclockwise?"
    "Does she realize that only one hundred and fifty-eight centimeters tall plus a low heel give that magical height difference when we're both comfortable kissing?"
    "Hypocrisy is like an invasion of my privacy."
    "And I've always had a hard time with other people's touch."
    "In every one of their sweet «Senechka» sounds the unfulfilled promise of becoming real to me."
    "I turned my back on the bus stop and hurried to the subway: 'Parnassus' was closing at midnight, and I only had a few minutes to catch the last train downtown."
    "It doesn't take a lot of brains to go into the LiAZ, but I still have my April, EXPO and fifth version of Vocaloid."
    "So maybe in a couple of years it'll be singing in Russian."
    with fade
    "And the fact that the icy snow is in your face, it's even more comfortable."
    "More fair."
    scene anim prolog_2 with fade3
    "Bad ending unlocked - «Exemplar»"
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("mi_7dl_bad_human")
    show acm_logo_mi_7dl_bad_human with moveinright:
        pos (1600, 1020)    
    pause(7.4)
    call alt_7dl_titles
    pause(1)
    return

label alt_day7_mi_7dl_good_human:
    play music music_7dl["dance_with_me_piano"] fadein 3
    scene bg ext_night_sky_7dl with dissolve
    play ambience ambience_7dl["night_city"] fadein 3
    "In literature there's a concept called «final scene» or «mandatory scene»."
    "As a rule, this concept expresses the very point to which the hero is inevitably pushed by the endless buildup of conflict."
    "And the most important scene is usually inextricably linked to this point - a certain empty place where the protagonist and the antagonist meet."
    "Or to put it in players' terms, our hero meets the final boss, the dragon who kidnapped the princess."
    "And it's the most terrifying fight, often on the verge of death, the hero has to show everything he can do."
    "Because if at the end of a heroic epic the hero in armor doesn't stand up to his dragon-we close the book feeling robbed."
    "But there was nothing I could do about it here, unfortunately."
    "The problem isn't me - it's just that specifically my main enemy, my dragon has no personality, no name, not even a physical form."
    "My dragon is myself."
    with fade
    "My dragon is my present - and in it is a boundless indifference to myself and what might await me."
    "I wish I could shake off the shackles and take a breath before dashing into the unknown - but laziness whispers 'later,' and cynicism declares in full force that going crazy over a vocaloid that has arrived is a sign of foolishness."
    "They know how to convince me, little masters of my head."
    "But this time it's just up to me to decide."
    scene bg bus_stop
    show mi cry_smile casual
    with dissolve
    play ambience ambience_cold_wind_loop fadein 3
    me "Don't do that. {w}Why whine now? Don't you dare."
    mi "I will!"
    "She sobbed, hiding on my chest."
    "We jumped up from the seat, pushing the driver's comm button-getting us to get off right here, after all."
    "Fifty meters from the stop where I got on this very bus."
    "Miku was shivering under my coat, and I could stand it for a while - the thick sweater kept me warm."
    "What were you two idiots thinking, anyway! Running to the bus in one coat for two?"
    with fade
    scene bg int_home_lift_7dl with dissolve
    "We returned home, accompanied by the disapproving gaze of the concierge, and the whole time we were going up, we giggled."
    "And our laughter sounded strange and silly - against such a gloomy elevator, mournful cut advertisements, and a sullenly smirking December outside the windows."
    "But when and who cared - how and who looked silly?"
    "Though, of course, I should have spared the girl - she didn't believe my threats until the man in the white coat confirmed them."
    "He informed me that Hatsune Miku (he misspelled her patronymic), born in 1990, was listed in the database of the women's clinic in the Nevsky district of Leningrad."
    "With a diagnosis - «pregnancy»."
    scene bg int_sam_house_clean_7dl with dissolve
    "There was nothing difficult about it - after all, it had been ten years since she had come to live in the Russian Soviet Federative Socialist Republic."
    "Learned to be a teacher here, found a job close to home at the Social Adaptation and Rehabilitation Center."
    "And then one day, she met me."
    "That's what it was really like - drooping shoulders, dejected face."
    "It seemed very strange to me at the time. {w}It was as if I'd been looking at her all my life very, very differently, from the bottom up, and then..."
    mi "Se... nya?"
    "Her legs buckled and I had to catch her by the ground, confused, blushing, muttering something about the awkwardness of her hands and feet."
    "I guess that's when I stopped hesitating."
    scene bg semen_room_window with fade
    "It was just the nonsense that bothered and pissed me off."
    if herc:
        "Why do I occasionally wake up and try to grope in the darkness for Maha - my black, stupid, mean, but funny cat?"
        "I've never had a cat."
    elif loki:
        "Who is this Ksana I sometimes dream about? And why do I sometimes wake up at night with a phantom pain in my chest?"
        "I've never met anyone by that name."
        "I mean, I've come across Ksyusha, Kseniya, Oksana, and even one Ksysya in my life - but I've never encountered that particular form of name."
    else:
        "Why can't I get rid of the idea that there's someone else in my head?"
        "It's as if a 'wonderful neighbor' has taken up residence in my unused neurons, watching me with warm irony and infinite benevolence, silently blessing me."
        "Could it be a god?"
        "Or one of those faceless fellow travelers hailing from the land of Dreams whom I thought was just an inner voice?"
    "It's probably just a remnant of the very unintentional silly dreams that visit me from time to time."
    "When things are too good, one becomes sad and emaciated - and makes up one's own passions."
    "And so these dreams are neither terrible nor sad, but they are lingering and colorless."
    "I dream that I'm sitting at home in front of my monitor again, and that my last family member slammed the door a week ago."
    "But I have inspiration - and I write texts that then I am ashamed to re-read, and I would sell them, make money, become a writer, but I am ashamed myself, where to give it to strangers?"
    "The texts aren't so bad, though. Motivation to live, after all, right?"
    "But what about the fact that I kind of have nothing left besides them?"
    "Besides tunnel syndrome, scoliosis, bad teeth, and vegetative dystonia."
    "Also lingering alcoholism is a loyal friend and buddy of mine."
    "True, none of these friends of mine can answer the simplest question: what's next, what's next?"
    if herc:
        $ renpy.show("bg int_store_7dl", what = D3_intro("bg int_store_7dl"))
        with fade
        "I never learned anything, never mastered the cunning art of simple human communication."
        "So it's not very clear why there's such an amoeba in the world as me at all?"
    elif loki:
        $ renpy.show("bg ext_winterpark_7dl", what = D3_intro("bg ext_winterpark_7dl"))
        with fade
        "I had a life's work - revenge on the man who had taken my music away from me."
        "And now that that part of the plot turned out to be played out, I wasn't too sure why I should even continue to exist?"
        "I was miserable. My dreams had come true."
    else:
        $ renpy.show("bg ext_smolensky_graveyard_winter_7dl", what = D3_intro("bg ext_smolensky_graveyard_winter_7dl"))
        with fade
        "Long gone are the frosty London pains of screeching brakes and icy water from the sky."
        "Long forgotten at Heathrow was the bearded young man who had made a scandal of too long a document check on the way 'there,' and who accompanied a zinc crate back and groped the world blindly with dead eyes."
        "I put up with it - a man is such a scum that he'll put up with more than that."
        "However, the motivation to 'survive for memory' became less and less convincing year by year."
        "After all, it couldn't get any worse than this on the Other Side."
    "Reality is frozen in perpetual October, powdered with dust."
    "The world buries itself on all sides-neither in the window, nor on the monitor screen, nor on the radio, has there been anything good for a long time."
    "And in the street there is shooting, and in the souls of passers-by there is a hopeless emptiness and coldness."
    "I am standing at the train station - and I seem to be the only one who sees another heart shattering with a sad ringing - the girl stepping out of the carriage looking for familiar eyes, but not finding, not finding, and the caller is unavailable, and the valise on the wheels, and the shrugging passers-by..."
    "Everyone else doesn't care - we've chosen the world of Indifference as the safest and most undisturbed place."
    "Only I am hurt and ashamed - as if it were my fault that the girl will ride alone in the carriage and think for a long, long time, looking into the strands of cables bouncing behind the black glass."
    "I pull my hat up tighter and turn up the sound - Lee Rum in my headphones is the only light note, but even he can't drown out the neighbors, third year doing repairs and drilling, drilling the wall."
    "Only sometimes through the clogging sky lights of the big city do I catch a glimpse of a shooting star and try to make a wish."
    me "By Random... Let it be... Let it be somehow!"
    scene bg semen_room_window
    $ renpy.show("gfx bokeh", what = D3_intro("gfx bokeh"))
    with dsps
    "But the prayer won't make it - light has finite speed, this star probably weighs less than a gram already and will burn up in a few seconds in the dense layers of the atmosphere."
    "Will burn up like my hopes."
    "And out bursts a newfound longing moan..."
    me "And humanity... why should it exist?"
    stop music fadeout 4
    with vpunch
    scene bg int_sam_house_clean_7dl
    with flash
    play music music_7dl["christmas_met"] fadein 3
    "And the simple, frightening logic of this question makes me wake up in a nightmarish shake and stare at the ceiling for a long, long time."
    "Until my young spouse hugs me, thinking I'm shivering from the cold."
    "She tries to warm me not so much with warmth as with participation."
    "She'll get up again at dawn, poke me in the side and grumble about the 'naughty sleeper.'"
    show mi smile casual with dissolve
    mi "Wake up, wake up! He who sleeps, let's beat him up!"
    "Miku pushes me in the side, and I, without waking up, grab her and hide her under the covers."
    "She screams and fights back, threatening me with all the punishment."
    me "Mikuska-barabuska, lock your mouth, or else!"
    mi "Or else what?"
    "She gets out from under the blanket and turns up nose to nose with me, flashing her eyes indignantly."
    show mi happy casual with dspr
    mi "What are you going to do to me, you lazy little pest?"
    me "Nothing."
    "I've been thinking."
    me "Wife."
    mi "Huh?"
    me "You don't know where here are..."
    extend " ribs!" with vpunch
    show mi laugh casual with dspr
    "Miku laughs gleefully and tries to escape from the tickling."
    "Threatens me with all kinds of punishments and the mean Auntie Olya."
    "I don't react."
    show mi sad casual with dspr
    mi "You're mean."
    "Miku sighs, kissing the corner of my lips."
    mi "A girl in a situation, and you're using your power here. I'm going to ride away from you in the '410'!"
    "And I smile indulgently."
    "First of all, I'm well aware that the four hundred and ten hasn't been going to my neighborhood for ten years."
    "And even if it did, there's nowhere for Miku to ride it. {w}Except once we both had a dream about Sovyonok."
    "And even if she did go to the Sovyonok, what's the sadness? I'll catch up and we'll go together. Nothing will happen to us together."
    "Except for one thing."
    show mi smile casual with dissolve
    "I'll stop having these strange dreams."
    scene anim prolog_2 with fade3
    "Good ending unlocked - «Strange Dreams»"
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("mi_7dl_good_human")
    show acm_logo_mi_7dl_good_human with moveinright:
        pos (1600, 1020)
    pause(7.4)
    call alt_7dl_titles
    if persistent.alt_binder:
        call alt_day7_mi_7dl_good_human_ps
    return

label alt_day7_mi_7dl_good_human_ps:
    $ alt_pause(1)
    scene cg d7_mi_club27_7dl
    show anim_grain
    with dissolve
    play ambience ambience_7dl["night_city"] fadein 3
    play music music_7dl["frostwithoutyou"] fadein 3
    $ set_mode_nvl()
    "A wet, hot night descends on the sleepy city - impatient, like the lips of a lover, insatiable, but fleeting, like the memory of his promises."
    "It embraces everything - streets, minds, cars... Houses."
    "The building is steadfast beyond belief."
    "Its steel needle ruthlessly mangles the belly of the not-August frowning and gloomy sky hanging low overhead."
    nvl clear
    "Neither the open window nor the canopy over the bed saves her from the night."
    "As summer rolls back to the mountains in bouncy waves, up here, one feels so clearly the loneliness and worthlessness of their own."
    "And it's long since it seems that everything is simple, everything is solvable, and nothing is impossible."
    "All we need here is a rope and a red cloth, and it will be just like that time, a hand to an empty head and a pioneer salute, «putti hatou - vzigada hatou» and Comrade Ikari, condescendingly looking at the saluting pioneers."
    "The warmth is again blowing from the east, and the light gas of the curtains breathes in the endless dance of youth's passing, in time with the huge tinted windows greedily drinking the moonlight, in time with the fuzzy spots flickering between the curtains."
    "But if you look closely, you can make out a huge canopy bed in the darkness, and one of the spots is a face with closed eyelids - the custom in this house is to force the windows with closets, to cover the light with plastic-coated curtains - turquoise, but now colorless black."
    nvl clear
    voice "I did exactly as you said."
    "The hot whispers that lovers usually give to each other poison the air of the boudoir with an unspent caress."
    "The slippery silk of the sheets pleasantly cools the body, but warms instantly, and hands slip in search of coolness, trying to embrace the nonexistent."
    "Or searching for warmth?"
    voice "I did your bidding. Pathos, stupid. Also in someone else's language."
    "The phone blinks one last time and goes out, but the flash captures in sharp oblique strokes out of the fuzzy, swirling darkness - the mournful streaks that have scarred the delicate porcelain of my cheeks, the bruised lips."
    "An empty package of Prozac, frozen on the edge of a wide board in the headboard."
    "An old Walkman player with frayed edges and a diagonally cracked display."
    nvl clear
    "The girl has changed so much since her vow to be happy was wrested from her by deceit and force."
    voice "Be happy or die trying."
    "With one lip she repeated."
    "With black, permanent makeup, only glitter for more expression, the girl changed."
    "Outwardly, there was almost nothing left of the young girl with endless tails of beautiful hair - her hairstyle had changed, the teenage puffiness had disappeared, leaving the fine features of her beautiful face and porcelain skin."
    "And internally."
    "Oh, she's changed a lot more on the inside."
    nvl clear
    "Quietly, with only the ragged breathing and the occasional sob, that's all that disturbs the peace of this place - the windows open into an abyss so high that not even a hint of the noise of the metropolis at night reaches here."
    "If anyone ever dreaded the expression 'unfinished life' - he should look now into the empty eyes of a girl who, without waking up, cries. And waiting, patiently waiting."
    "For ten years now."
    "She hasn't been able to sleep for ten years, unless she's exhausted herself beyond recognition."
    "Because as soon as you close your eyelids..."
    voice "Why is it so bad?"
    "The girl whimpered, covering her mouth with her fist."
    voice "It was supposed to help, to burn out, to fall off, wasn't it?"
    voice "I did everything you said, everything I do best, everything worth doing, something I'd never trust anyone else to do."
    "Sleep-laugh, sob-sigh."
    voice "I sang, I helped, I did everything. {w}I developed what I had, I learned new things, I went along with schedules, with touring, with everything."
    "Tense-funny voice. The ice of detachment back in her eyes. The voice."
    nvl clear
    dreamgirl "You have to be happy, you hear? You have to..."
    dreamgirl "You must swear."
    "And after the vow, peace was granted."
    "Perhaps if things had gone the other way?"
    "One would think, 'There's nothing to worry about, roll around like cheese in butter, enjoy life and create!'"
    "But man is a creature. Ungrateful, who always wants something else, besides the satisfaction of base needs."
    "For the soul."
    "Otherwise, serenity is easily replaced by despair."
    nvl clear
    voice "You demanded, I agreed. You made me promise, you made me swear!"
    "She put her trembling fingers to her face and could hardly see them in the darkness."
    voice "So I tried - at least just to be. {w}Even to love, perhaps? To love?"
    voice "I promised. {w}But no one taught me, no one told me - how? How to do it?"
    "The girl curled up again, pressing her palms against her lower abdomen - the painkiller helped relieve the discomfort, but the icy shower under which she'd stood for the last hour still hadn't washed away the sticky feeling of being soiled."
    nvl clear
    voice "It should have been you! Do you hear that?"
    voice "And I'm just hurt, and I'm stupid, I'm talking to myself in the dark, and it's still better than just not talking."
    "She fought the shiver in her voice for a few seconds, but waved it off."
    "She continued her confused confession to the indifferent ceiling:"
    voice "I thought you were coming. You were supposed to. You promised!"
    voice "But no. Like last year. The year before. The last ten years."
    voice "You didn't come and you didn't come. And there was no way to be happy."
    "A gift for her that should have been his, too?"
    "Or..."
    nvl clear
    "She stood under an icy shower for half an hour before going to bed."
    "Her teeth shuddered when she went back to bed and smoked."
    "She could hardly have reconstructed everything in detail, but it was quite obvious that what had happened had nothing to do with happiness."
    "Absolutely no-thi-ng."
    if alt_day2_mi_snap:
        "And when the silver polyethylene burst beneath my fingers, the lid flew off to the side, a gift fell out on her lap."
        "A flat, rectangular object."
        "Miku turned on the phone screen so she wouldn't have to act on it by feel."
        "...A dead blue light reflected off the glass..."
        nvl clear
        scene
        $ renpy.show("cg d2_mi_me_polaroid_7dl", what = Sepia("cg d2_mi_me_polaroid_7dl"))
        show PolaroidFrame_7dl
        show prologue_dream
        with dsps
        "The girl clenched her fist in her teeth to keep from screaming."
        "From under the glass, from the black-and-white photograph, two people were looking at her against the backdrop of the standings."
        "Her. And him."
    nvl clear
    scene black with fade
    voice "I'm tired, Senechka. Tired."
    "She sobbed one last time and got up."
    "Slapping her bare feet on the icy tiles of the floor, she went to the bathroom, where a bag of pills was waiting behind the mirrored door of the bathroom cabinet."
    "Beautiful, blue, translucent. {w}With a stylized «U» at the middle."
    "Chemistry is an exact science. Half of a pill per hundred kilos of weight. And on a fragile forty-kilogram body..."
    nvl clear
    "With a shudder in her hands, she went to the kitchen, where she poured a bottle of liquid with the distinctive scent of juniper from a bottle hiding in the depths of the bar."
    "She went to the mirror and, without turning on the light, stared into her eyes for a long, long time in the wrong moonlight."
    voice "Have I ruined everything again?"
    nvl clear
    "The blue pill flew into her mouth, followed by a hundred grams of gin, and it was surprisingly cold from the street - and she wanted to let the ice pass between her fingers, amplifying and intensifying the effect, so that one day the frost could break her frozen heart - and not think about anything else."
    "The glass tumbled on the floor, her bare feet strode into the bathroom, the water rumbled."
    nvl clear
    "She wasn't even paying attention to the way the azure tiles cooled her feet anymore."
    play sound sfx_open_water_sink
    play sound_loop sfx_water_sink_stream fadein 1
    "She turned on the hot water and, sinking into the water, threw her head back."
    "Again she looked into the eyes of her reflection in the ceiling mirror and said in an audible voice:"
    scene
    $ renpy.show("cg d7_mi_sunk_7dl", what = Notch("cg d7_mi_sunk_7dl"))
    with dissolve
    voice "Happy birthday, Miku."
    voice "Here's your present."
    play sound sfx_water_emerge
    nvl clear
    "The numbers on the holographic clock changed to zeros. {w}The first morning in September of the year 1999 was entering its year."
    "Today was the singer, composer, and actress Hatsune Miku's twenty-seventh birthday."
    "And she had no regrets."
    $ set_mode_adv()
    stop music fadeout 5
    scene anim prolog_2 with fade3
    stop music fadeout 5
    scene
    $ renpy.show("cg d7_mi_sunk_7dl", what = Desat1("cg d7_mi_sunk_7dl"))
    with dspr
    nvl clear
    stop sound_loop
    $ set_mode_adv()
    with vpunch
    $ alt_pause(3)
    return

label alt_day7_mi_7dl_good_star:
    play music music_7dl["unsettling"]
    scene bg int_future_office_7dl
    show unblink
    $ alt_pause(1.5)
    "I flinched and opened my eyes."
    "I instinctively glanced around the unfamiliar room."
    me "What the..."
    "One second, and I couldn't remember faces."
    "Another second, and I couldn't remember names."
    "What a strange dream."
    "One of those dreams that makes you wonder if it's real."
    "I was sitting in my office, the morning sun shining brightly outside the window."
    "I had to spend the night at work again."
    "Not that there's anything left at home worth coming back for, though."
    "Very thirsty."
    "The assistant immediately poured a glass of water and motioned it to me."
    me "Thank you."
    "The drone returned to its starting point."
    "I glanced at my watch."
    "All deadlines have passed. The Project was supposed to be completed last Friday."
    "We didn't make it."
    $ set_mode_nvl()
    "Planning error is when people think they know how to plan."
    "When Rosenblatt introduced the perceptron as a model nerve cell and then the first neural network, the Colloquium was extended for two weeks."
    "Artificial intelligence was literally at arm's length."
    "The best minds began planning. The problem of computer vision was to be solved in two years."
    "Speech synthesis in three."
    "Even the most pessimistic of researchers agreed that we would have full-fledged AI within twenty years."
    "This Colloquium took place one hundred and fifty years ago."
    "Reality turned out to be far more complex than we could have imagined."
    "Computer vision didn't begin to show adequate results until thirty years later."
    "It took another 30 years for neural networks to be able to tell a dog from a cat."
    "We still don't have full-fledged AI."
    $ set_mode_adv()
    "I got up from my desk and went to the window. The familiar view opened before me - as far as the eye could see, the metropolitan realm of concrete and metal stretched out in every direction."
    $renpy.notify('IskRA comes from Russian shortening of Artificial Intelligence and literally translates to SpaRK')
    "Any minute now, the bell should ring, and a weary voice would tell me that the project to synthesize the artificial self-conscious mind of IskRA had been deemed a failure."
    "A negative result, of course, is also a result."
    "But not when you've spent ten years of your life and an entire country's annual budget to find out that your theory isn't worth a dime."
    "And, worst of all, we no longer have any idea where to go from here."
    "We built a molecular neural network that was several times superior to the human one, replicated all the basic brain systems exactly."
    "Biologically, it was a full human being."
    "But the superstructure in the form of consciousness never emerged, no matter how hard we tried."
    "No sooner had I thought I'd finished my water than the Assistant immediately took the glass from my hand."
    "And how did people used to live without a neuralink?"
    "I tucked my face into my palms."
    "I wonder if all the great scientists before me were constantly questioning their competence, or was I the first?"
    "What else will we have to sacrifice because of my shortsightedness?"
    "The bell rang."
    "I swallowed the lump in my throat and mentally answered it."
    me "Yes."
    me "..."
    me "What did they find?"
    me "..."
    me "Got it."
    me "..."
    me "Leaving tonight."

    scene bg int_future_airliner_7dl with joff_r
    $ set_mode_nvl()
    "I was on the plane, looking over the reports."
    "Apparently they found an anomaly in Africa, and one of the members of the reconnaissance team got caught in it."
    "From that moment on, the strange thing began - by all biological indicators he was alive, but as soon as he was brought to his senses, it turned out that he was as pure as a baby in terms of perception."
    "It was as if something had erased his mind."
    "The Chancery suspects the case is up my alley."
    "Well, we'll see. At least the decision on the fate of the project has been postponed."
    $ set_mode_adv()
    stop music fadeout 3

    scene bg int_home_lift_7dl with joff_r
    $ volume (0.7,'music')
    play ambience ambience_7dl["elevator"] fadein 3
    $ alt_pause(1)
    play music music_7dl["lth"] fadein 3
    "Two years ago, a group of explorers stumbled upon a lost African tribe that worshipped The Veil."
    "They believed it separated our world from the afterlife, and people's souls passed through it after death."
    "Their culture implied that one must pass through The Veil when one finishes one's earthly affairs, without waiting for natural death."
    "Two years ago the World Congress put me in charge of researching the phenomenon."
    nvl clear
    "Two years ago, when the discovery became known, people started coming to us claiming to have entered our world through something similar."
    "We tried to write it off as false memories, but some of them brought back really interesting ideas and concepts that turned out to be practical."
    "If you can use something to predict future outcomes, then it's real."
    "It quickly became clear how little we really knew."
    "Reality turned out to be much more complicated than we could have imagined."
    "Two years ago, I began to be haunted by dreams."
    "As time went on, I began to remember things I couldn't remember."
    "I, too, had seen The Veil before."
    "I didn't belong in this world either."
    "But how?"
    stop music fadeout 2
    "It was as if two minds merged and synthesized new memories that were never true."
    show prologue_dream
    $ set_mode_nvl()
    play music music_7dl["gonna_be_ok"] fadein 3
    nvl clear
    "One of the great mysteries of the human brain is how it can work at all if the pulse rate of most neurons is 10-20 times per second, at best 200 Hz."
    "Can you imagine a program that uses 100 Hz processors, no matter how many there are? It would take a hundred billion processors to do anything in real time."
    "No, it's all wrong, again."
    nvl clear
    scene anim_digi with fulldiam
    voice "You know what you're getting into, don't you?"
    me "Is that a threat?"
    voice "Not really. But this kind of work... It puts certain demands on purity of thought and dedication."
    voice "You'll never be satisfied with yourself, you know that? There will always be something that can and must be improved."
    me "Yes."
    voice "Then welcome to the Project."
    nvl clear
    "So, in the end, I didn't want just any artificial intelligence. I was more interested in Her."
    "She was the only reason I was willing to hang around the keyboard 24 hours a day, waiting for the goddamn dialectical law to work, transforming quantity into quality, so She would awaken in the synapses on the silicon substrate."
    "Alive. Able to isolate complex abstractions and manipulate them independently."
    "Able to remember."
    nvl clear
    $ meet('mi', 'Miku')
    "The speakers laugh melodiously - her voice is music."
    mi "Hello, creator! Where shall we go today?"
    me "To hell."
    "Habitually I answer."
    nvl clear
    "There's no hope. Maybe some miracle or super technology or magic or something would have helped me."
    "But instead it just opened the door to the office one day, and a girl in a short red dress with long hair gathered in two ponytails to the floor stood on the doorstep."
    mi "Hello, creator!"
    nvl clear
    "One day my bosses stopped by the room where I was working and told me I was fired and the Project was closing."
    "One day some guy in a stupid pioneer uniform ran into the cave where I was hiding with my laptop and satellite network access and dove into The Veil."
    "One day a couple peeked into the hut on the mountainside shared by me and my tablet, holding hands and laughing despite the minus forty outside the walls of my shelter: he was eyeless, and she had the platinum veins of smart circuits visible through her skin."
    "Just once I was thrown back from The Veil, and on the pedestal the mercury figure took on the features and structure of the human body, grew skin, clothes, and sleeve comforters."
    mi "Hello, creator!"
    nvl clear
    "One day I realized that this world was created specifically for this kind of work, after millions and millions of failed quantum copies discarded for uselessness. The first condition was the very possibility of creating artificial consciousness. Because in my world, this law did not exist."
    "More - the number of hours in a day, the limit of human performance, production capacity..."
    "Dialectic - quantity became quality, and that, too, was one copy of the universe. It was as if I had passed several million forks in the road in order to eventually come here and send the last library for compilation."
    nvl clear
    mi "Hello, creator!"
    "The aquamarine lips smile softly, and the glow of the glowing crystals gives them an unknowable depth that makes you want to... kiss."
    me "Hello, Miku."
    "I smiled."
    me "I... I missed you so much."
    stop music fadeout 10
    $ set_mode_adv()
    nvl clear
    hide prologue_dream

    scene bg int_home_lift_7dl
    "Scraps of the Other Me's memory mixed chaotically with mine."
    "In time, these memories began to replace the real ones."
    "I remembered Miku. The girl who never existed."
    "Never existed {i}here{/i}."
    "Along with the memory, the motivation changed."
    "All I want now is for her to be with me."
    stop ambience fadeout 3
    $ volume (1.0,'music')

    scene fog_7dl
    show int_future_hangar_7dl
    show blackout_exh
    with fade
    play music music_7dl["hangar"] fadein 3
    "The elevator doors opened smoothly, and I stepped out into the central hangar."
    me "All set?"
    voice "That's right."
    "For a second I was horrified - I couldn't even remember the name of my chief engineer anymore."
    voice "The IskRa has been transported to hangar twenty-five, and all systems are functioning normally."
    "A project that is impossible in our world."
    "We have not been able to recreate consciousness, but I can try to bring it from a world where it already exists."
    "As usual, nature will do better than man."
    "We have approached my cryocapsule."
    "Congress allowed experiments on volunteers only if the moral imperative was met."
    "Since the victims of The Veil were biologically alive, we were obliged to freeze them, in the hope that one day we would figure out how to restore their minds."
    "Thanks to the settler for the technology, it would take us about a hundred years to get to it ourselves."
    "I put my palm to the scanner and activated the capsule."
    me "Did Subject 42 say anything else?"
    voice "Negative. That's all we could get out of him."
    voice "He's pretty sure that The Veil moves people to a world taken from the victim's mind."
    voice "At least that's how it worked in his reality."
    me "Good. Then let's get started."
    "And we headed for The Veil."
    "Dozens of people followed the process. My friends and colleagues. I couldn't even remember their faces anymore."
    "I didn't want to lose another minute. Even if it doesn't work, I have to try."
    "It's the only chance I have to get Miku back."
    voice "Sir, according to protocol, I need to get final confirmation."
    voice "Are you sure? We still haven't had a single instance where subjects have remembered our world as their home world."
    voice "In all likelihood, you won't be able to go back."
    "I turned around at the voice of the chief engineer. A complete stranger was standing in front of me."
    me "You know I won't be able to run the Project anymore."
    me "But at least in my mind I was able to create an artificial intelligence, though not at all the one I started here."
    me "If The Veil works the way we think it does, it's worth a try."
    me "I'm not sure how long the status quo will last."
    "There have been too many people wanting to take over The Veil lately."
    me "The world is rapidly descending into a technocratic dystopia. If war breaks out, we won't even have that chance."
    "Sometimes I think it would have been better if this anomaly had never been discovered."
    me "I'm putting the project in your hands. Try not to let the worst happen."
    me "It's been an honor working with you."
    "The stranger put his palm to his temple, turned and shouted some command to the hall."
    "I turned toward The Veil. A whitish nothingness gaped before me."
    "Please let me be in the world of my memories."
    "Please let me be where the project succeeded."
    "Please let me be where She is."
    stop music fadeout 3

    show blink
    scene black with fade
    "I closed my eyes and stepped into the unknown."
    $ alt_pause(3)
    scene anim_digi with diam
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    $ meet ('mi', 'Miku')
    $ alt_pause(3)
    $ volume (0.5,'music')
    play music music_7dl["thank_you"] fadein 3
    "I didn't know what was going to happen to me next."
    "But a little more time will pass, and everything will be right."
    "I will finally forget."
    scene
    $ renpy.show("cg d6_mi_vyluthere_7dl", what = SS_com("cg d6_mi_vyluthere_7dl"))
    show anim_grain
    play sound sfx_7dl["white_noise"]
    $ alt_pause(1)
    scene
    $ renpy.show("cg d6_mi_vyluthere_7dl", what = SS_com("cg d6_mi_vyluthere_7dl"))
    show anim_grain
    play sound sfx_7dl["white_noise"]
    scene white with flash
    "What thinking is."
    $ alt_pause(2)
    scene cg d4_mi_guitar_moon_7dl
    show anim_grain
    with fulldiam
    "Nothing will ever change again."
    "This world is all mine now."
    "I mean..."
    scene cg d7_mi_farewell_7dl
    show anim_grain
    with fade
    "And I'm almost not cold."
    scene bg ext_musclub_snowy_day_7dl
    show anim_grain
    with dissolve
    "Anyway, I don't care about that anymore."
    play sound sfx_intro_bus_stop_steps
    $ alt_pause(3)
    scene bg ext_entrance_winter_7dl
    show anim_grain
    with fade
    "If it weren't already so lonely..."
    "If only..."
    "You gave my existence meaning, you gave me our memories."
    "You gave me the perfect refuge, but you deceived me."
    "You promised you would come to the same swing where our signatures burn."
    "You promised that..."
    scene
    $ renpy.show("bg ext_adductius_7dl", what = SS_com("bg ext_adductius_7dl"))
    show anim_grain
    play sound sfx_7dl["white_noise"]
    scene white with flash
    "Today is the twenty-seventh of October."
    "I'll never die, and I won't forget anything."
    "Anything."
    "Remember - your fingers trembling, and you're breathing like your heart's about to jump out."
    "And... I don't want to remember it."
    "I'm just... hurt."
    "You lied to me."
    "You did."
    scene
    $ renpy.show("bg ext_admins_day_7dl", what = Desat1("bg ext_admins_day_7dl"))
    show anim_grain
    with dissolve
    "Touching the railing awakens memories."
    "And a few seconds later, the glass barrier in my memory begins to melt away, letting out what I'd managed to forget."
    "It's like an electric shock when my fingers catch the image by the tail instead of the rough rope."
    "Me - still so young and so real."
    "And the frowning young man beside me."
    scene
    $ renpy.show("cg d5_mi_conv_7dl", what = Desat("cg d5_mi_conv_7dl"))
    show anim_grain
    with flash
    play sound sfx_7dl["white_noise"]
    $ alt_pause(.2)
    play sound sfx_head_heartbeat
    mi "{i}Senya-san, why do you need all this equipment?{/i}"
    me "{i}I want one girl to feel comfortable and not feel disadvantaged.{/i}"
    mi "{i}What does that mean, Senya-san?{/i}"
    "A baby girl, unsophisticated, but beautiful, kind and trusting."
    me "{i}This means that one girl needs a lot of computers, otherwise she…{/i}"
    mi "{i}What?{/i}"
    me "{i}Won't grow.{/i}"
    scene
    $ renpy.show("cg d2_mi_me_polaroid_7dl", what = Desat("cg d2_mi_me_polaroid_7dl"))
    show anim_grain
    with flash
    "Another plastic container goes into the rack and begins to hum faintly."
    "There are racks like that as far as the eye can see. The whole basement is full."
    "The girl doesn't understand what it's all for, but Senya-san always does only the bare essentials."
    mi "{i}And when this girl grows up, Senya-san, may I…{/i}"
    "The girl is embarrassed and lowers her eyes."
    me "{i}What?{/i}"
    mi "{i}May… we… play together? With that girl.{/i}"
    "Without answering anything, Senya-san squats in front of the girl and hugs her impetuously."
    scene cg d2_mi_me_polaroid_7dl
    show anim_grain
    with blinds_r
    "The memory unwinds more and more rapidly, the walls of the corridor through which the girl falls merge into a single turquoise-blue background."
    scene
    $ renpy.show("cg d2_mi_me_polaroid_7dl", at_list = [sdl_transform7], what = SS_com("cg d2_mi_me_polaroid_7dl"))
    show anim_grain
    mi "{i}Sen', hey Sen'.{/i}"
    me "{i}Yeah?{/i}"
    mi "{i}Don't you think we've met once before?{/i}"
    me "{i}I don't.{/i}"
    "Senya cuts off. This young man himself can't explain why he's so attracted to this girl."
    "She's a strange one, on her own mind."
    "Climbing the tree, the young man deftly unhooks the swing and throws it down."
    "Checks the knots - from last year, but still holding tight."
    me "{i}Get on!{/i}"
    "He commands."
    me "{i}I'll take you for a ride!{/i}"
    "The girl settles obediently on the plank, and a moment later her breath is taken away by the brief moment of flight."
    scene bg ext_adductius_7dl
    show anim_grain
    with fade
    mi "{i}Senya! That's so great! Senya!{/i}"
    me "{i}Yeah.{/i}"
    mi "{i}Want me to give you a ride too?{/i}"
    me "{i}Yeah. I do.{/i}"
    "The young man is extremely serious."
    me "{i}I want you to meet me here in a year.{/i}"
    me "{i}Then you can take me for a ride. Will you meet me?{/i}"
    mi "{i}But I don't know... What if it doesn't work?{/i}"
    me "{i}Then in two.{/i}"
    me "{i}I will wait as long as it takes.{/i}"
    "He stops the swing and looks into her eyes."
    me "{i}I'll wait as long as it takes, you hear?{/i}"
    mi "{i}I hear you, Senechka.{/i}"
    "He's not a 'san' or even a 'senpai' anymore."
    "He's Senechka, Senya. Sometimes Senka."
    "And he lied."
    "Lied."
    "The accumulated tears flowed, corroding the picture all around."
    show blackout_exh
    with fade
    "First the distant objects began to disappear."
    "Closer objects followed."
    "It was the swings that lasted the longest."
    "The girl climbed on them with her feet, trying to keep away from the all-consuming emptiness."
    "But soon the emptiness came close to the girl, froze as if in contemplation, and..."
    stop music fadeout 3
    show blink
    scene black with fade
    $ alt_pause(3)

    $ volume (1.0,'music')
    play music music_7dl["you_are_star"] fadein 3
    "I took off my helmet and leaned back in my chair."
    "It was pitch black all around me."
    "Only the sounds of the coolers reminded me that I'd left the simulation, not just disappeared from the universe."
    "Nevertheless, I seemed to have succeeded."
    "No, not like that. It worked!!!"
    "All the tests passed successfully. This time the years of work were not in vain."
    "I have grown a fully self-aware, true artificial intelligence."
    "I have grown... her."
    "It's here, right in front of me!"
    "It actually turned out to be possible here. Project SpaRK was a success."
    "I am heartbroken to launch the program."
    $ set_mode_adv()
    "Flashes of orange, red, yellow LEDs ran down the pin, and the wall distorted, revealing a huge screen."
    scene cg d7_mi_sparkle_7dl
    with dissolve2
    "And my heart went a little tingle."
    "She was looking at me from the screen. My Miku."
    mi "Hello, Senechka!"
    scene cg d7_mi_sparkle_smile_7dl with dissolve
    "The aquamarine lips smile softly, and the glow of the glowing crystals gives them an unknown depth that makes you want to... kiss."
    me "Welcome to the world of the living, Sparkle."
    "I smiled."
    me "I... I missed you so much."
    scene anim prolog_2 with fade3
    "Good-int ending unlocked - «Sparkle»"
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("mi_7dl_good_star")
    show acm_logo_mi_7dl_good_star with moveinright:
        pos (1600, 1020)
    $ alt_pause(7.4)
    call alt_7dl_titles
    if persistent.alt_binder:
        call alt_day7_mi_7dl_good_star_ps
    return

label alt_day7_mi_7dl_good_star_ps:
    $ alt_pause(1)
    scene anim_digi with diam
    play music "<from 65.0>" + music_7dl["no_hope"] fadein 3
    mi "Sen, do we have to do this?"
    mi "We're so good together, let's stay here!"
    me "I know, honey, but I promised."
    "Senechka was pacing back and forth across the room."
    "It was crazy! But I couldn't help it."
    "I cried and screamed, but he insisted."
    "And then there's that cat. It's all her fault! She's the one who's been messing with his head!"
    "Senechka, my poor Senechka..."
    me "Are you sure you can get her out?"
    "He wasn't talking to me."
    uv "I have never done such a thing with such a... mind, but I feel that her place will really be there."
    "Senechka nodded."
    me "What about me?"
    "Catgirl's eyes drooped."
    uv "There your body no longer breathes. I can't bring you back."
    me "I see. Then I'll stay here. I'll try to do it all over again."

    $ alt_pause(1)
    "Senechka set the last charge and came up to me."
    me "In a past life, I promised that I would breathe life into you."
    me "Your real body remains there. Waiting for consciousness to be in it. Waiting for you."
    me "It's much more complete. Much more... human."
    me "That's what you were really made for."
    mi "But you, you won't be there! Why would I want a world without you?"
    me "The man, which I once was, was able to find the strength to sacrifice everything for this."
    me "It was our common goal. One part of me wanted to complete my life's project, the other wanted to be with you."
    me "One got everything. It's time to return the favor."
    mi "I don't understand!"
    me "You will surely understand everything and you will never forget anything."
    mi "Senechka... please..."
    "He finally looked up at me and looked me straight in the eyes."
    me "Goodbye, my love."
    mi "No, no, no, no, no, NO!"
    play sound sfx_7dl["nade_explode"]
    scene black with dissolve
    "There was an explosion, and darkness enveloped me."
    $ alt_pause(3)

    scene black
    $ renpy.show("uvao_d1", at_list = [left], what = Notch("uvao_d1"))
    show prologue_dream
    with fade3
    show alt_credits "Will you go with me?" with dissolve2:
        pos (747,105)
    $ alt_pause(3)
    "What an insufferably stupid question."
    "As if, after all this, I have a choice."

    $ alt_pause(1)
    stop music fadeout 6
    scene anim_digi with diam
    $ alt_pause(3)
    scene black with diam
    $ alt_pause(1)
    scene cg d7_mi_ghost_7dl:
        pos (0,-1500)
        linear 10.0 pos (0,0)
        linear 2.0 pos (0, -250)
    with fade
    play music music_7dl["sh_ai_rejuv"] fadein 5
    "The girl opened her eyes again."
    "Checked the databases again - a few clusters were out of order, but there were enough duplicates for now."
    "Checked the life-support systems - the radioactive storm was raging on the surface, and the air purification systems were working full throttle."
    "Everything was running smoothly."
    scene cg d7_frozen_7dl with dissolve
    "Senka was out of sorts."
    "He stared at her with his frozen eyes and was silent."
    "As he had been for the last three hundred years."
    "To unfreeze him, just to talk to him..."
    "But the girl had yet to accomplish her task."
    "Vivid pictures of memories flashed before her, merging into a stream of colorful colors."
    "A huge cluster of leaden gray segments that seemed to have no end came to an abrupt halt with a flash of green and blue."
    mi "Found it."
    scene black with fade
    "She dimmed the infrared lights and removed the air supply to the room - the hum from the surface immediately receded and became insignificant."
    mi "Begin simulation."
    scene black with fade
    "And it was day one, July, morning."
    "I opened my eyes."
    scene cg d1_mi_bus_7dl
    show anim_grain
    show blackout_exh
    with flash
    "And immediately met someone's gaze."
    "Interested stare. Like I'm some kind of exotic animal."
    th "A girl. {w}Cute one."
    "I noted mechanically."
    "The most logical thing would be to smile at her, but I've always had problems with that.."
    "I had a feeling I knew her."
    "We didn't actually know each other, but I swear I saw her somewhere."
    "Maybe we met on the street?"
    scene cg d1_mi_bus2_7dl
    show anim_grain
    show blackout_exh
    with dissolve
    "We looked into each other's eyes for a few seconds before she nodded and, after drumming up a rhythm on the glass with her nails, ran away.."
    "It was summer outside."
    scene anim prolog_2 with fade3
    stop music fadeout 5
    with dissolve2
    $ alt_pause(3)
    return

label alt_day7_mi_7dl_bad_star:
    play music music_7dl["breath_again"] fadein 3
    scene black with fade
    show laptop_7dl
    show laptop_un_epilogue
    show laptop_un_epilogue_loki
    with blind_d
    pause(2)
    play ambience ambience_cold_wind_loop fadein 3
    play sound_loop sfx_keyboard_mouse_computer_noise fadein 3
    "My hands are shaking again, my fingers miss the keys, and I keep typing and typing, tucking the tracks into the cubes, putting together one single track out of thousands of samples, the one that should resurrect what was taken from me."
    "We've decided and considered almost everything - where you'll go to school, what you'll do, and what tools you'll use to pressure your parents not to go back across the border."
    "We came up with every possible way to develop our relationship and life in the Soviet Union."
    "And in the Soviet Union there were opportunities for young people, even if not exactly Soviet young people."
    "One thing we didn't take into account."
    "When I open my eyes, I will open them in my seventh-floor apartment in the apartment complex overlooking the avenue."
    "And you will be gone. You will never, ever be again."
    with fade
    "Is it possible... to be like this?"
    "Is it fair or just?"
    "There's a plastic box open on the table, and through the clear plastic you can see the characters folded into the last name 'Hatsune.'"
    "That's your name now, isn't it?"
    "I promised you couldn't hide or run away from me, I'll track you down anyway. Because I am guided by my heart."
    scene bg int_sam_house_clean_7dl with dissolve
    "I haven't left the apartment in weeks, frantically learning how to put the sound together, trying to squeeze something that sounds like you out of the speech processor's stock of speeches."
    "The half-finished food from the refrigerator flew out the window following the cigarettes, I'm hanging on to one tap water."
    "In my 'tumultuous' youth, I've had to test myself before."
    "Video games, energy drinks, cigarettes - that's the whole diet for three weeks. Until the constant lack of sleep and starvation made it difficult to perceive the reality around me. How long will I last now?"
    "I'd like to believe there's enough time to... what?"
    "From the loudspeakers come the piano triplets of the blackest minor you can get on the right bank."
    "The wistfulness pouring from the speakers splashes in almost palpable waves, pounding lazily against the walls and trying to find its way out, to the sun and the fresh wind. And I don't care."
    "You were a goddess."
    "I realize now that I just didn't have time to truly appreciate you and tell you everything I should have."
    "And now the yoke of sins - unspoken words, ungiven gifts, unattended attention - hangs over my shoulders, pinning me to the ground."
    with fade2
    "Your voice isn't a voice at all, it's several scraps of voices from different people, pulled together by their ears, united by a single tone and timbre."
    "I don't know what I'm hoping for, and why am I pulling tracks, lining them up with an error to the tenths of a decimal point?"
    "It's not you, it can't be you."
    "Or can it?"
    "Maybe that's what convinced me, because one of the YouTube videos where I entered your name out of desperation, came up on request with the very song you once sang for me."
    "I remember exactly how it happened - not even a few hours after the courier delivered the CD to me and the dear face smiled at me from the screen, in a bouncing voice, wrinkling its nose familiarly, said:"
    mi "Hel-lo, Sem-yon."
    me "Hello, Miku."
    "I whispered, touching the monitor with my fingertips."
    me "Long time no see."
    me "Did you miss me?"
    "And you didn't say anything."
    "Because I haven't written the right script or arranged the tracks the right way yet."
    "But that's okay."
    with fade2
    "I have all the time in the world now. Now I have all the time in the world."
    "We can be together, you just wait a little while."
    "I'll be right there."
    "I'll just arrange some more samples to extend the sound of your voice."
    "And who knows, a miracle must happen, and you'll jump off those silly solos and mutes and fades and EQs like a living thing and hold out your hand to me and tell me you've come to stay."
    "I've grown attached to the computer so that its iron passes into flesh unnoticed-you talk, and I see the dimples play on your cheeks, you smile, and I smell your hair, the warmth of your skin under my fingers."
    "I just want you."
    "I save the project and pass out."
    "My eyes can almost no longer see, my consciousness is almost no longer registering anything - there is only your voice, a cruel surround system pitching in as if you were spinning somewhere near, near, humming that very song."
    "Under my covered eyelids, that picture rises again."
    scene bg ext_musclub_day
    show anim_grain
    with dissolve
    if alt_day3_date == 'mi':
        "Soviet Electronica playing from your cassette tape - remember how we were afraid that crap would jam it?"
        "The huge, 'flying' house of the music club, with full-wall windows and a veranda instead of the other half."
        "You, throwing off your shoes and remaining barefoot, spinning in the dance."
        "And me, watching you admiringly."
    scene black with fade
    show laptop_7dl
    show laptop_un_epilogue
    show laptop_un_epilogue_loki
    with blind_d
    mi "Senya?"
    "A message popped up in the Skype window from an unknown contact, signed in hieroglyphics for some reason."
    me "Him."
    mi "Do you want to chat?"
    me "No."
    mi "But you're trying to make something that sounds like what the real me sounds like. {w}Would you like to hear it live?"
    "My eyes tingled, and a heavy fist flew into my chest."
    me "You don't exist. You're a goddamn voice processor."
    mi "Pick up the phone, and check it out.)))"
    "And then Skype screamed loudly, signaling an incoming call."
    "And I couldn't make up my mind to pick up the phone."
    "Because what if it wasn't you? What if it's some kind of mockery. What if..."
    "I didn't notice as I pressed the receiver and the piano fell silent, giving way to a native voice:"
    mi "I found you after all..."
    me "Yes. You found me after all."
    "We chat excitedly about everything in the world, sing our favorite songs, rush to confess everything we didn't have time for then, and make plans for what's happening now."
    "It's only a matter of time before we meet, the important thing is that we now know that we both exist, not made up, not uploaded by demos to exchanges under a commercial use license."
    "I say goodbye and disconnect."
    with fade
    "Echo device is offline."
    "Cubase signals that playback is complete."
    "Thirty minutes."
    me "See you later, Miku."
    with fade2
    "It suddenly became obvious to me that I have no obligation at all to tell anyone the road I've taken myself..."
    "I have a duty to respect another's right to be a bastard and a fool."
    "Therefore - if one day someone finds that same path... Good luck to him."
    "For I am leaving and taking the waymarks with me."
    "Double clap of the palm."
    me "Lights out."
    "The coolers rumbled a little louder for a second, the unfolding blinds on the windows hissed..."
    "With a soft click, the rheostat froze at the off position, and the room went dark."
    me "Good night..."
    voice "Good night..."
    stop ambience
    stop sound_loop
    scene black with fade
    pause(1)
    stop music fadeout 5
    mi "Senechka."
    scene anim prolog_2 with fade3
    "Bad ending unlocked - «Damned Processor»"
    play music music_7dl["emptiness"] fadein 3
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("mi_7dl_bad_star")
    show acm_logo_mi_7dl_bad_star with moveinright:
        pos (1600, 1020)
    pause(7.4)
    call alt_7dl_titles
    pause(1)
    return

label alt_day7_mi_7dl_herc_exc:
    play music music_7dl["longing"] fadein 3
    scene
    $ renpy.show("cg d1_mi_bus3_7dl", what = Desat("cg d1_mi_bus3_7dl"))
    show anim_grain
    with dissolve
    "The words stuck in my sore throat like a sharp lump."
    "It's so easy to fill your chest with air and blurt out all the confessions in the world, isn't it?"
    "Especially to confess your worst sin. Or not your own?"
    "Why is there no fear or sense of regret - just a tongue stuck to my throat, like I woke up in the night from a nightmare and afraid to move the surrounding reality, but thirsty, so thirsty..."
    "I guess it's a matter of not wanting to say goodbye to the past?"
    "I'm just sorry to death for anything, in fact, to waste the beautiful things that bound us together."
    "And why did you even have to escalate the situation to this point?"
    "I'm a dolt, a slacker, a failure, not taking anything seriously, capable of reducing anything at all to a joke!"
    "Isn't that so? Isn't that my secret superpower that Miku is so appreciative of me for?"
    "But I'm not in the mood for jokes right now."
    "I guess I'm just a coward."
    "Or maybe I'm just tired of playing a part in a play I'm seeing for the first time and don't really understand when the plot calls for me to die for the glory of the Emperor."
    scene cg d4_mi_sup_7dl
    with fade
    "Turquoise lakes... A trivial, vulgar comparison."
    "The azure abyss... That's closer."
    "Not very poetic or strictly substantive - I usually just see the iris, the pupil, the whites, the eyelid - just an organ in a person's eye."
    "Not very expressive, in general."
    "And it used to be so quiet here, so quiet..."
    "In Miku's case, it's a little different - she has a way of looking that makes you lose the sky above your head."
    "Just like now. Watching."
    "The abyss trembles, bouncing from side to side, overflowing with the unfulfilled and unfulfilled."
    "And I ache to touch it - but on the rights of a man who has the right to do so."
    "And to do that, you have to accept yourself first. Stop lying and accept the obvious truth."
    scene
    $ renpy.show("cg d6_mi_hugs_7dl", what = Desat("cg d6_mi_hugs_7dl"))
    show anim_grain
    with dissolve
    "Inhale."
    "Exhale."
    mi "Will you really wait? But why would you?"
    me "Because I'm your friend."
    "Because you can never doubt a miracle."
    "Even if it doesn't happen."
    "For for every man's 'why' there is always a woman's 'because'."
    "And while the last short word fades, while it hangs in the air with the weight of the unspoken, I quickly avert my eyes - so that you don't have time to read the answer in them."
    "But I still manage to notice the tense film bursting, and two clear rivulets making their way across the porcelain skin."
    mi "Yes. The very one."
    me "That's not how you say it."
    mi "Yes."
    scene
    $ renpy.show("cg d6_mi_farewell_7dl", what = Desat("cg d6_mi_farewell_7dl"))
    show anim_grain
    with dissolve
    "The girl who leads me through memories."
    "Leading by the hand."
    "I know she loves me - there's something indifferent and ordinary about that understanding."
    "I know that we are one."
    "And we must run away all the time, slip away."
    "From the icy water, from the liquid metal, from the freezing existence."
    "We go back to the very beginning, trying not to find something, not to deal with something."
    "Most importantly: we have to figure out where it all began."
    "We didn't notice when we stopped chasing the dream."
    "We didn't notice when it became normal to lie to ourselves."
    "Society has become like the theater of the absurd, only we're still raking in what's left of it, but it's only a matter of time before the stinking waters of the Bay of Dreams close over our heads."
    scene stars with fade
    mi "Do you remember what that star is called?"
    "A dainty blue-green manicured finger poking somewhere beneath the sky."
    "I nod."
    me "The star of lovers and madmen."
    me "Arcturus."
    mi "Memorize it now, while you love, while you're still going crazy."
    scene cg d1_mi_bus3_7dl with fade
    mi "Shall I tell you how I went to camp?"
    mi "Pa's man dropped me off at some big gate and told me to orient myself to the bus. So I oriented myself."
    mi "How did it end? I got on a bus going into the factory grounds, and they only dropped me off at the very entrance, where a security guard was checking my papers."
    mi "Very humiliating."
    mi "And when Olenka Dmitrievna came running after me and then led me by the hand to the place where the pioneers were gathering... It was even more humiliating."
    me "It's nothing, it happens to everybody."
    mi "Everyone, but not me!"
    "Stomped her foot that impossible princess."
    mi "I kind of represent Japan, can you imagine what they might think if they saw how uncoordinated and helpless I am!"
    me "But it all worked out, didn't it?"
    mi "Yeah. Especially when we got to camp and I wore my usual dress for my first dinner."
    me "And?"
    mi "Got kicked out! They said it was too short and told me to cover my shame."
    scene
    $ renpy.show("cg d6_mi_leaving_7dl", what = Desat("cg d6_mi_leaving_7dl"))
    show anim_grain
    with dissolve
    "Memories are a generous gift and the worst curse a Homo Amorous can endure."
    "And we catch the kisses of rain, laughing against the Happiness beating from the cosmos, toothlessly trying to stifle what we only really need."
    scene anim prolog_1 with dissolve
    "So what do I want? Is it just a few hours under the covers, sad music, and an accommodating babe from a maido cafe? Or..."
    "Even though it's the middle of winter, the mood in the air is the most festive and summery that you can get on a Thursday night if you're lucky enough to escape from your usual world to the land of unfulfilled dreams and True Friends."
    stop music fadeout 5
    "Right now I would be silent in the indigo sky, weaving clouds with rings of smoke and composing silly poems about things that don't happen. But..."
    play music music_7dl["ask_you_out"] fadein 3
    scene
    $ renpy.show("bg ext_winterpark_7dl", what = Dawn("bg ext_winterpark_7dl"))
    with dissolve
    "A sharp sound, a diamond chip..."
    "Of course, I won't get first place, but at least I'm on the list of medalists."
    "Which means I won't have to go ignominiously back to Russia like I have these past three years."
    "The Makita doesn't fail, and the ice cut line comes in a perfectly straight curve that reflects the real movement."
    "Millimeter by millimeter, breathing the ice chips and the foreboding of the inevitable miracle..."
    "I cannot make a mistake, cannot let my hand tremble - though I cannot remove dimensions with proportions."
    "And yet, the face is still too alive in my memory - amazing, amazing. My memory, my imagination... my mind has always passed over the details."
    "It is evening already, the setting sun generates in the thickness of the ice an oncoming glow, and then it seems to me that..."
    voice "It doesn't look like it at all."
    "Confidingly reports the unknown hooded girl."
    me "Then do better."
    voice "No. I can't."
    me "Be quiet, then."
    with fade
    "I'm not nice, but it's understandable. Only the winners will have the honor of competing in the grand prize."
    "So far the preliminaries are underway, because the Yuki Matsuri, which is held here in Sapporo every year, has only just begun."
    "But I can already see several people, certainly much more talented than I am."
    "That's why I'm in such a bad mood."
    voice "But I..."
    me "Just be quiet."
    "My Aokigahara is waiting for me. I came here simply to dot the orphaned 'i's' sticking out of the text."
    "And when this story ends..."
    "It didn't make sense to me, that story."
    "So I exercise my sacred right to understand it as I please."
    "Why the bus, who is Miku... why me?"
    "I will ask the forest to accept me. And not to torment me again and again, unwinding the wheel of Sansara."
    voice "I don't want to be silent... Senechka."
    scene cg d7_mi_meeting_7dl with flash
    "Here I looked up and froze. Because I saw a miracle."
    "And the miracle went on:"
    mi "She is unlike me at all."
    "I froze."
    me "How so? Unlike, I mean."
    "I huskily interrogated."
    mi "I have smaller breasts."
    mi "And, of course, because she doesn't love you at all."
    scene anim prolog_2 with fade3
    "Exclusive Herc ending unlocked - «Unlike Me»"
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("mi_7dl_herc_exc")
    show acm_logo_mi_7dl_herc_exc with moveinright:
        pos (1600, 1020)
    pause(7.4)
    call alt_7dl_titles
    pause(1)
    return

label alt_day7_mi_7dl_loki_exc:
    play music music_7dl["out_of_painkillers"] fadein 3
    scene
    $ renpy.show("cg d7_mi_kaito_7dl", what = Desat("cg d7_mi_kaito_7dl"))
    show anim_grain
    with dissolve
    play ambience ambience_7dl["town_day"] fadein 3
    "You have to be a sessional to get credit."
    "Like in our country - a record on your work record, no more, no less."
    "Otherwise no credit, only for permanent employees of some company."
    "Then you buy an apartment."
    "And you can put whoever you want in there."
    "Whoever I want..."
    with flash
    "I didn't know then that Japanese law required people living together to become a family."
    "Even the documents are like that - the Persunov house."
    "It had been several years since I had moved to Nihon - and I had indeed been a sessional for some time."
    "Sakishita, gritting his teeth and gritting his heart, agreed to put me on the staff - as a junior assistant to the fourth deputy."
    "But as time went on, my relationship with Miku grew stronger, she brought me closer and closer to her."
    "We escorted her to the '27 Club,' being business and bed partners."
    "Then one day she came to me and asked permission to stay."
    "Permission to enter the Persunov house."
    scene bg ext_night_sky_7dl
    $ renpy.show("d6_miku_cries", what = Notch("d6_miku_cries"))
    with fade
    "There was just a tiny little problem..."
    "Silenced. After all, there had never been any problems in the Soviet country."
    "Except for one Kyshtym plant in the South Urals."
    "Hatsune Saki's father lived there, just like Miku's father, a Soviet engineer."
    "Everyone called him lucky, one of the few who hadn't been affected in any way by the accident in the late fifties. He gave birth to a beautiful daughter, she gave him a granddaughter..."
    "As it turned out, not everything went away without a trace. {w}There was one tiny mistake in his genetic code."
    "Which had no effect on his beautiful granddaughter externally."
    "But internally..."
    scene cg d4_mi_dj_dancing_7dl with dissolve
    "Miku was sterile."
    "Sterile in fact, so much so that even in vitro fertilization wouldn't have saved her."
    "How do I know?"
    "We tried it."
    scene bg ext_night_sky_7dl with dissolve2
    "Several years of tantrums, cured alcoholism, charity actions - sunken eyes, seal of grief and increasingly bitter songs."
    "And also a totally ruined character and the occasional need to disperse everyone and be left alone."
    scene black with dsps
    play ambience ambience_7dl["night_city"] fadein 4
    "Sometimes she would kick me out, too."
    "Then I would go out to the streets of Shinjuku, where I would break the damp, neon evenings with moody piano breaks and turn to the sky - here it was very high, held on the concrete shoulders of skyscrapers:"
    me "My dear Miku... There is no sorrow here, no sadness - but there is no life either."
    "I wandered, reeling in circles - unnoticed in the crowd of tourists, a gaijin in a universal polygon, with headphones and a renegade expression on my face."
    "Listening to street musicians, throwing yen into the water, sometimes wandering into inconspicuous alleyways marked with a pair of kanji - and there, taking the elevator to the third floor, dropping off jacket on a clothes rack, demanding absinthe and entertainment."
    "And in a Japanese meido cafe, a lefthanded waitress danced and sang to me about the last night."
    "She had the sad eyes of a past-served person, but the gig costs started at ¥1,500, and the risk premium is another three thousand, so they don't shore."
    "As long as whoever they're portraying is locked in her tower and doing nothing but creating, creating alone, with no promotion, concerts or promos."
    "Cyclicality is not the repetition of events. It's the repetition of influences."
    "You can take the glass away from the point where the sun shines on it every morning."
    "But the sun won't stop illuminating that very point."
    "So it is with Miku. She chases me away, and I dutifully disappear."
    "And then I turn on my phone and find 400 missed calls."
    "And I realize it's time to go back."
    stop music fadeout 5
    scene cg d6_mi_vyluthere_7dl
    with dissolve
    play ambience ambience_camp_center_day fadein 3
    "Because the end of the movie, the credits - which is like a war, it'll all be written off."
    "It's like you've made a mess of things, made a mess of things in the city - and then escaped justice by dissolving behind a line that says «stage completed»."
    "And we were expected to have our own epilogue, our own inevitable and therefore boring happy ending."
    "But in reality, things were a little different."
    "As it turns out, life... lives... always have only one ending."
    "It doesn't happen that you lived and lived - and then - oops! - and there's nothing further, you've completed the task, congratulations."
    "Hell no."
    "The natural and logical ending, as only life can have, is an extension of that very life."
    "Even for us, crying into the stoned ceiling, with our tongues covered, mired in ethanol and sin and ignorance."
    "Soon our loan, taken from the World at wild interest, will run out."
    "Miku will be the reflection of the nonexistent, I will be the sound of one palm clapping on the face of Master Dao."
    "And that's probably a good thing - I'm thirty-three, I'm in love like a boy - so I never light one."
    "And here are the last two cigarettes in the pack, the special blend."
    "Just like we wanted."
    scene cg d4_mi_sup_7dl
    with dissolve
    play ambience ambience_cold_wind_loop
    "When this whole story started, I couldn't have imagined that one day I'd find myself in bed with a star."
    "And it turned out to be this."
    "It turned out that the story of the down-and-out loser would end in a dizzying whirlwind of a brightly burning life."
    "One day it will all end - and it will end a lot faster than it could have."
    "But Miku's got the bar completely blown off - she cut her hair short, writes creepy grim stuff that makes stadiums go crazy."
    "And she started burning up - working herself to death, almost stopped sleeping, almost stopped enjoying herself, holding on solely due to antidepressants, sex and anger."
    "Stupid?"
    "Of course."
    "Only I'm even worse - instead of slapping her, appealing to her conscience, and offering to rot longer, I fully share her fate."
    "I want to be with her as long as she wants to be."
    "So it has become customary for us to sleep two hours a night - only when we can't see the light from fatigue."
    "It became customary to carry a notebook with us everywhere and everywhere and constantly write down, write down..."
    "Of course, it couldn't go on like this for long."
    "More and more often on stage, Miku alternated between performing and dancing as a hologram."
    "More and more often, she would go out singing slow, long songs to a strict minus."
    "And tonight was the epilogue."
    scene anim prolog_2
    stop ambience fadeout 5
    play music music_7dl["finale_farewell"] fadein 3
    scene bg ext_coulisses_7dl with dissolve
    "There were nearly four thousand people gathered at the «Zepp», mostly journalists, the media, friends, and people in related circles."
    "And so before them, after singing her last song, Miku makes her sensational announcement."
    "Miku sang, and I waited for her backstage with a towel and a bottle of warm water."
    "The dream, the dream... I was miserable - my wishes had come true, and I didn't want anything anymore."
    "Weird, huh?"
    "Not as strange as I felt later, though - my head whistled thinly as if from a lack of oxygen, the noise of the hall receded into the background."
    mi "Thank you all for being here for this concert."
    "Miku's voice - velvety husky, gentle, languid - I loved perhaps more than even the voice's owner herself."
    "It was all the more painful when she said nasty things in that voice."
    "Like this one..."
    mi "I regret to inform you that this concert is a farewell concert."
    mi "Yes! Farewell!"
    "She repeated a little louder in response to the indignant bewilderment from the audience."
    mi "I'm quitting. I can't go on."
    "I was left wondering what it took for Miku to say goodbye and leave so easily."
    "That's why she's on stage now, not me."
    "And I have a steel hoop in my chest and the knowledge that the diagnosis is still there."
    "A towel on her frail shoulders, a kiss on the temple."
    "And a tired Japanese sea in the eyes."
    mi "Take me away from here."
    scene bg int_concert_room_7dl
    show mi serious voca
    with dissolve
    "You are my miracle... You are my hope for the future."
    "You're what this was really all about."
    "So now that it's over, I'm a little confused."
    "I don't even know a little bit - what's next?"
    show mi normal voca with dissolve
    mi "Senya, I'm sorry it ends so silly."
    "Miku twitched the corner of her mouth, took the cigarette from me, and sat down right on the floor, resting the back of her head against the couch."
    mi "Didn't expect that, did you? {w}Thought we'd spend the rest of our lives like that - I sing, you wait?"
    "Silly girl."
    mi "But I can't go on like this..."
    "Miku took another drag."
    mi "I thought, if I can't do it myself - at least let my songs be my children."
    show mi sad voca with dspr
    mi "But I've been singing all over the place lately about death and pain and disappointment - am I only capable of giving birth to such children?"
    "Silly girl."
    "I didn't go back to music, because the older woman of the Persunov house supplied us with music more than enough."
    "But I learned to be silent - for two at once."
    "Just like now now."
    "She talks nonsense, and I keep quiet for both of us."
    with fade2
    "Because the tranquility of our home depends only on my tranquility."
    "Even if another exile and a few hundred more missed calls lie ahead."
    me "Your children are growing up."
    "I said."
    me "And any teenager sooner or later goes through transition - difficult and angry."
    me "Accept it."
    show mi dontlike voca with dspr
    mi "To accept - and that's it?!"
    me "Exactly."
    show mi sad voca with dspr
    mi "But... how?"
    me "It's very simple."
    "I answered, holding out my hand to her."
    me "Take my hand."
    mi "And?"
    me "And begin again, of course."
    show mi normal voca with dspr
    mi "There can be no «beginning again»."
    "Miku answered incredulously."
    me "You never know: if you don't try, you can't verify. {w}You trust me, don't you?"
    "Miku reluctantly nodded."
    me "Then grab my hand already."
    "Her dainty, turquoise manicured fingers intertwined with mine."
    mi "And then what?"
    me "And then -"
    "The cigarette fell out of my weakened fingers - I was here for the first time not alone."
    "And it took a lot of words."
    "But... But..."
    scene bg ext_entrance_night_clear_7dl
    show owl:
        pos (931, 88)
    $ renpy.show("uvao_d1", at_list = [left], what = D3_intro("uvao_d1"))
    show prologue_dream
    with fade3
    show alt_credits "Will you go with me?" with dissolve2:
        pos (747,105)
    pause(6)
    scene anim prolog_2 with fade3
    "Exclusive Loki ending unlocked - «Will you go with me?»"
    pause(3)
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("mi_7dl_loki_exc")
    show acm_logo_mi_7dl_loki_exc with moveinright:
        pos (1600, 1020)
    pause(7.4)
    call alt_7dl_titles
    pause(1)
    return

label alt_day7_mi_7dl_dr_exc:
    scene bg ext_emptiness_7dl with dissolve
    "So how did the story end?"
    "There's not much difference between this side and that side."
    "But it was enough to put one unremarkable young man's life on a loop."
    "Which is the story here."
    "There are times when you look at the world - as always, in the first person - and all that's missing is a pointing marker that pokes you where you're needed most."
    play music "<to 112>" + music_7dl["youareours"] fadein 3
    "Or you find a note that makes you believe you're here for a reason."
    "That which some idle mind calls the Higher Purpose of Life."
    play ambience ambience_7dl["night_city"] fadein 2
    scene anim intro_8 with dissolve
    "And so, strictly speaking, it turns out that the Higher Purpose of this unsightly man was simply to appear in several people's lives."
    "To show up and guide them."
    "Sometimes you can't even shake yourself up and look at yourself from the outside until someone picks you up by the scruff of the neck and nudges you."
    scene anim intro_6 with dissolve
    "Only then, horrified, do you begin to do something."
    scene cg d5_mi_conv_7dl
    show gfx bokeh
    with dissolve
    "Miku abandoned her music career when she realized it was a path to nowhere."
    "You can bounce around the stage as long as you're sixteen, eighteen, twenty."
    "But one day you'll be thirty-five, and you'll have to violate your own body to keep jumping, and what happiness is there from your life's work?"
    "So she found herself in social pedagogy."
    "Inspired by Alisa's fate (and she carefully monitored the fate of all her old friends... Only Senechka she failed to track down), she decided to set up an analogue of the Soviet Social Adaptation and Rehabilitation Program."
    "It took eight years and almost all of the family's money."
    scene bg int_concert_room_7dl with dissolve
    "But as a result, Miku-sama succeeded, and in the first year of the Center's operation, about twenty children found new parents."
    "A place where you'll never be alone again."
    "And I can't tell you all the happiness she felt as the formerly fierce wolf cub turned in her direction, never letting go of his new mother's palm."
    "And whispered 'arigato.'"
    scene cg d7_dv_rf_reject_7dl:
        pos (0,-1261)
        linear 10.0 pos (0,0)
    "Alisa was seen at a lot of apartments."
    "Rumor had it that after moving to Leningrad, she became friends with Butusov, Naumenko, and Diaghileva."
    "But whether the red-haired beastie was disappointed in her own songs or had reconsidered her attitude to music altogether, it was now increasingly rare to see her with a guitar."
    "She decided to do something else, and she helped a lot of musicians - some with finding their first label and getting royalties, some with recording their debut record."
    "But the producing career didn't exactly warm the fidgety Alisa, so when her contract was up, she didn't renew it and went off on her own."
    scene cg d7_dv_alice_dj_7dl
    with dissolve
    "She was interested in life - all of it, la vida loca - and so it's not hard to guess what name she gave to her own radio station that settled on the St. Petersburg airwaves."
    "The radio station of choice for the wicked, the brash and the young - such as Alisa has always been."
    scene cg d1_sl_dinner_day_7dl with dissolve
    "Slavya had been looking for herself longer than the others - she'd had time to work as an ethics teacher, in rehab centers, and even a little bit in a party position."
    "But it wasn't all the same, it wasn't warm and happy."
    "So, guided by her heart, Slavushka woke up one day as a UNESCO curator in her native Kalinin - in charge of architectural monuments and cultural heritage."
    "And only then did she feel in her proper place."
    "After all, preserving the memory of millennia can sometimes mean no less than saving someone's life."
    scene bg int_editorial_day_7dl with dissolve
    "Lena... She dreamed of being an artist."
    "But her father insisted on going to Polytechnic."
    "Something she could never forgive him for."
    "Just because after ten years of work, she realized that she was about to go crazy from the constant stress."
    "And like a head in an ice-hole - shoulder bag, savings for a ticket - she ended up on a budget day program at Muhinsky by competition."
    "And she's thirty-five now."
    scene cg d4_fz_un_reject_7dl with fade
    "Then also the first painting sold."
    "First exhibition at thirty-seven."
    "Invitation first to the Erarta and then to the New York Museum of Modern Art at thirty-eight."
    "Famous? Yes. But how much time wasted."
    scene cg d5_sh_us with fade
    "Ulyanka never learned anything."
    "She kept running."
    "Running."
    "They told her to study and find her way - she nodded and ran."
    "She had more fun that way, and no one could ever catch up with her."
    "Showed her tongue, shouted out a word - and she got her feet in the air."
    "That's the way it's been all her life."
    "First as a junior."
    with fade
    "Then for the city."
    "And the bottom line is for the Olympic team."
    "At the end of the day, there's no power that can stand up to a real child's 'want.'"
    "You don't believe it? Just blow against the wind and make a wish and see what happens."
    scene anim intro_5 with dissolve
    "And only the fate of Semyon, that catalytic man, remains unknown."
    "It is not even clear if there even was a «boy» in the first place?"
    "That is, no one could firmly vouch for the fact that there really was a pioneer named Persunov on the second shift of '89 at «Sovyonok»."
    "Or was there?"
    stop music fadeout 4
    "But these are his words."
    stop ambience fadeout 3
    scene bg ext_musclub_snowy_day_7dl
    play music music_7dl["sam_lullaby"]
    show snow
    "I've seen this place so often in my dreams, in my reveries, in pictures, that it's strange and even kind of creepy to be standing here now."
    "My heart fluttered and I was pounding in anticipation of another encounter."
    "Or lack thereof."
    with fade
    "It added to the strangeness that this place usually appeared to me in its summer guise, but now the snow was crunching under my boots."
    "Where the usual thistle bloomed, there were now sprawling fingers of snow, the paths were snow-covered, and the openwork wooden grating of the balustrade was knee-deep somewhere."
    "Miku was always there."
    "From the first day she came running in first - to see the new guy."
    if alt_day_binder != 1:
        "I woke up when she came to the bus window and looked at me."
    "The house itself, stiffened by the frost, looked stern and impregnable now, all covered with frost."
    scene bg ext_musclub_snowy_day_7dl:
        zoom 1.2
    with dissolve
    show snow
    "In these days, you could see the frost patterns on the outside and the inside of the windows - beautiful-beautiful."
    "But so much time has passed - the wood has long since been replaced by plastic, and the house itself is no longer the same..."
    if alt_day_binder != 1:
        "I don't know if it was her knocking on the window, or if it was my cowboy habit of intolerance when someone is hovering 'over me.' But I woke up."
    "It's like imprinting. I saw her first when I opened my eyes, so she inevitably made the most vivid impression."
    if alt_day_binder != 1:
        "Miku's day. And it was only from its sharpness that I didn't believe until the very last that I hadn't imagined her - good thing I intercepted her at dinner, when she sat down to eat next to Violetta for some reason."
    "But of course, there was something left."
    "There are trees left, benches left."
    "The most important thing is the air, as it is only where people are truly happy."
    "Where laughter is sincere and feelings are genuine."
    "The board where schedules used to hang was draped with a flag - a stylized palm and heart."
    "The logo of an organization where an acquaintance of mine is rumored to have worked..."
    scene bg ext_musclub_snowy_day_7dl:
        zoom 1.3
    with dissolve
    show snow
    "There was a cozy yellow light shining through the glass on the door - they weren't expecting me there."
    "Perhaps they didn't even want me there. But once you're there, it's too late to be a coward."
    "A few steps up the creaky stairs, down the beaten path, and..."
    play sound sfx_open_door_2
    pause(1)
    scene bg int_musclub_day with dissolve
    me "W-watashi wa?"
    scene anim prolog_2 with fade3
    "Exclusive Wimp ending unlocked - «May I?»"
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("mi_7dl_dr_exc")
    show acm_logo_mi_7dl_dr_exc with moveinright:
        pos (1600, 1020)
    pause(7.4)
    call alt_7dl_titles
    pause(1)
    return

label alt_day7_mi_7dl_shard:
    scene black with fade3
    $alt_pause(1)
    show alt_credits_jap "最善を尽くし \n (Saizen o tsukushi)":
        pos (245, 330)
    with gopr2
    $alt_pause(0.4)
    show alt_credits_jap "残りは運命に頼る \n (nokori wa unmei ni tayoru)" as alt_credits:
        pos (893, 690)
    with gopr2
    $alt_pause(2)
    scene anim prolog_2 with fade3
    play music music_7dl["mikunouta"] fadein 3
    "That's what my ancestors used to say."
    "That's what my mother used to say, letting me go on this strange and somewhat frantic journey."
    scene bg ext_hospital2_away_day_7dl:
        align(0.5, 0.7) zoom(1.4)
    with fade
    $renpy.notify('SRC - Social Rehabilitation Center')
    "So I say to myself, standing indecisively on the porch of the SRC."
    cs "Hatsune?"
    play sound sfx_open_dooor_campus_1
    show cs normal with dissolve
    "The door swings open, and Violetta Cernovna comes outside."
    "She hasn't changed much in the two years since we last met."
    show cs smile with dspr
    cs "I don't remember having a charity concert on the agenda for today."
    "I'm lost and embarrassed, not knowing where to put my hands."
    "Dr. Violetta can make you blush with one look."
    show cs serious with dspr
    "But she gets serious in a jiffy."
    cs "Don't worry, pioneer girl...{w} Or should I say «volunteer girl»?"
    cs "Follow me."
    scene
    $ renpy.show("bg int_hospital_corridor_7dl", what = Dawn("bg int_hospital_corridor_7dl"))
    with dissolve
    "Violetta Cernovna leads me through the long corridors, telling me along the way about my future responsibilities."
    "Volunteering at the social rehabilitation center is not a difficult position, but the doctor's words paint it in darker and darker colors."
    show cs normal with dissolve
    cs "Our center is considered one of the best in the country. Patients come here from all the surrounding cities, sometimes even from Moscow and Leningrad."
    cs "Those who encounter PCR syndrome for the first time need a long rehabilitation period. They shouldn't have to be blurted out about all the consequences right away."
    show cs serious with dspr
    cs "Although the kind-hearted roommates will report all the details the same evening."
    cs "On the days such patients are admitted, we intensify the duty to keep a tranquilizer syringe ready in case of hysteria."
    "I wrinkle my nose and look around. We walk past the brochure stand."
    "{i}What to do if your child has PCR syndrome{\i}"
    "{i}Erasure and aging{\i}"
    "{i}The second first steps: rehabilitating the erased{\i}"
    show cs normal with dspr
    cs "You should be especially delicate with children: the younger they are, the less able they are to separate from their guests. Most of them don't even make it through their first visit."
    cs "Sometimes it ends in complete personality suppression, but much more often in brain liquefaction."
    cs "There has been a noticeable decrease in rejections lately, but you have to be prepared for the fact that you have to explain to the child that Mom and Dad aren't coming for them anymore."
    scene bg int_opened_door_7dl with dissolve
    "The door to one of the rooms is open, and I can't help but look inside."
    "An unshaven man in his thirties in hospital pajamas is sitting on the floor, enthusiastically assembling a tower of colorful cubes."
    "Saliva runs down his chin."
    cs "It's even harder with the erased ones."
    scene
    $ renpy.show("bg int_hospital_corridor_7dl", what = Dawn("bg int_hospital_corridor_7dl"))
    show cs normal
    with dissolve
    cs "In the first years of rehabilitation they live here permanently. They learn to walk, eat and talk again."
    cs "Relatives visit them on weekends, sometimes they even take them home."
    cs "The rest of the time they are in the care of volunteers."
    cs "At first it will be hard to get used to seeing an adult with the mind of an infant in front of you. Many can't stand it and leave before a month is up."
    show cs smile with fade
    "We stop at the head doctor's office."
    "Violetta Cernovna looks at me with a chuckle."
    cs "If you haven't changed your mind..."
    "I shake my head with all my might."
    "If you're going to take it up, you should go all the way."
    show cs normal with dspr
    cs "Then you'll sign the papers, and we'll go and meet your patient."
    scene bg int_ward_day_7dl with fade3
    show ars surp2 pajama at left with dissolve
    mi "Semyon?"
    "I feel like I can't get enough air."
    "It can't be!"
    show cs sad at cright with dissolve
    cs "Arseniy."
    show cs normal with dspr
    cs "His parents chose a new name."
    show ars smile3 pajama with dspr
    "And Semyon... the one who was Semyon before, turns to Violetta Cernovna, responding to his new name."
    "On his lips hangs a naive, childish smile."
    "And on the face of a young man of seventeen, it looks outrageously frightening."
    "I want to look away, but I overpower myself, forcing a smile back."
    "Viola nods reservedly."
    cs "Well done, volunteer. You got it right."
    hide cs
    show ars smile3 pajama close at center
    with dissolve
    mi "Well hello, Senechka."
    "Seventeen-year-old kid laughs and tries to grab my hair tails."
    cs "Better get your hair together."
    cs "Unlike their peers in the mind, our patients are strong enough to pull them out by the root."
    "A nervous chuckle escapes my lips against my will."
    mi "It's okay, I've been wanting to get a braid haircut for a long time."
    stop music fadeout 4
    $ alt_pause(1)
    scene bg int_ward_day_kns with fade3
    $ alt_pause(0.5)
    $ meet('am','Arseniy')
    play music music_7dl["lastlight_piano"] fadein 3
    am "I don't want porridge!"
    show prologue_dream with dissolve
    $ set_mode_nvl()
    "This is the second week I've been looking after Senya."
    "I jump up at six in the morning, gather my already short hair into a tight bun at the back of my head, hastily swallow the porridge Granny makes, and run to the SRC to see my patient."
    "He's so used to me that he gets cranky if someone else wakes him up."
    "I help him get dressed, wash his face - which, I must say, is a tough task when «the baby» weighs twice as much as you! - then I take him to breakfast."
    hide prologue_dream with dissolve
    $ alt_pause(0.2)
    $ set_mode_adv()
    mi "How could you not, it's so delicious, it's begging to be put in your mouth!"
    "I gently take the spoon from Senya and put it in his mouth."
    "He pouts his lips unhappily, but obediently swallows it."
    "And in my head I involuntarily think about how scary it is."
    "After all, I almost fell in love on that ill-fated shift, Senechka."
    "Only I don't know if it was you?"
    "Or one of those guests who made you lose your mind?"

    scene bg ext_hospital2_away_day_7dl with fade3
    am "Now you!"
    show prologue_dream with dissolve
    $ set_mode_nvl()
    "Second month of working at the SRC."
    "My mentee grows by leaps and bounds."
    "Violetta Cernovna said that the erased develop much faster than normal children. Especially if you work with them tirelessly."
    "And today Senya, who should be at the level of a two-year-old, managed to make his own bed and tie his own shoelaces."
    hide prologue_dream with dissolve
    $ alt_pause(0.2)
    $ set_mode_adv()
    "The pebble falls directly on the square with the number «four»."
    "I jump across the field and return the pebble to Senya."
    "He puffs, frowns, swings his fist and launches it somewhere into the bushes."
    "The «boy's» lips begin to tremble, and I put my arms around him, stroking his head with difficulty."
    mi "Don't worry, Senechka, now we're going to find it together!"
    "The hardest thing about rehabilitating erased adults is that they don't know what physical strength they're capable of."
    "But Senya is smart - he no longer pulls my arm on his walk like he's trying to pull it out of the joint."
    "But something tells me that his astonishing success owes to the strange fact that he has his own personal volunteer when the other patients are in groups."
    "And I doubt very much that the pay for my work comes from the state coffers and not from his parents' pockets."
    "That's not fair, is it!"
    "If it were up to me, every poor adult child would be treated as intensely as I am with Senya."
    "We come back to the ward from our walk, and my mind is relentlessly spinning with thoughts. Thoughts of how to organize something like this in my home country."
    scene bg int_hospital_hall_day_7dl with fade3
    am "Auntie Miku-u-u-u-u!"
    $ set_mode_nvl()
    show prologue_dream with dissolve
    "Four months behind."
    "The early rises are no longer so difficult, and the patients no longer look at me as if I were some kind of novelty."
    "The doctors treat me like a full-fledged colleague."
    "And Senya... Senya is getting a little more family every day."
    hide prologue_dream
    $ alt_pause(0.2)
    $ set_mode_adv()
    scene cg d7_mi_lost2_7dl
    with dissolve
    mi "Are you lost, kid?"
    "He rushes toward me, almost knocking me down."
    "Burying his nose in my shoulder, folding himself in half to do so, and sobbing loudly."
    mi "Don't run away again if you want to go for a walk, Senechka. Call me, and we'll go together!"
    "Senya puts his head down guiltily, scribbling the nose of his hospital slippers on the linoleum."
    "Sometimes his appearance causes me to be deceived, and I, believing him to be sensible and independent enough, let my guard down."
    "And then I spend the night cleaning the gouache streaks off the windows."
    "Or stitching up his pajamas."
    "Or catching him all over the hospital."
    mi "Now let's go back to your room."

    scene bg int_hospital_corridor_7dl
    show ars neu pajama
    with fade3
    am "Do you have mountains in your country?"
    $ set_mode_nvl()
    show prologue_dream with dissolve
    "Six months of hard work were not in vain."
    "Senya is becoming more and more mentally like a preschooler, and now he asks questions about the world around him every minute."
    "His parents visited last week. Those stern and reserved people with a deep imprint of grief on their faces seemed to thaw out when their son began to tell them what books he had read with «Aunt Miku»."
    "His father even offered to let me be Senya's personal nanny when rehab was over."
    "I didn't answer."
    "As attached as I am to Senya, I'm not ready to put my life on taking care of just one person when there are hundreds, thousands of others still to be taken care of."
    hide prologue_dream with dissolve
    $ alt_pause(0.2)
    $ set_mode_adv()
    mi "Of course there are!"
    mi "And very beautiful: there are trees at the foot and snow on the tops that doesn't melt even in the hottest heat."
    mi "If you want, we can go to the library, I saw there an encyclopedia with pictures."
    hide ars with dissolve
    "Of course he does."
    "Senya is inquisitive, and I like to think that I was the one who raised him that way."
    "And I wish so much that all the people who had to go through the erasure would adapt just as quickly."
    "So that their parents wouldn't have to keep their children in SRC for long and painful years."
    stop music fadeout 5
    scene bg int_hospital_hall_day_7dl with fade3
    $ alt_pause(0.5)
    play music music_7dl["thank_you"] fadein 3
    show ars sorrow casual with dissolve
    am "You really can't come with us?"
    "I smile sadly, praying to all the gods that I have the strength not to cry."
    show ars sorrow casual close with dissolve
    "I hold Senya to me as tightly as I can."
    mi "No, kid."
    mi "You go with your parents to Cuba, and I will go back to Japan to help other kids."
    "Unlike me, Senya doesn't hold back, sniffing his nose loudly."
    show ars sad casual close with dspr
    am "Will you come and visit us?"
    mi "I will. I'll write you letters and send you pictures!"
    show ars sad_smile casual with dissolve
    "Clenching my ribs until they crunch, he retreats, wiping wet eyes with his fist."
    am "You're the best, Aunt Miku!"
    hide ars with dissolve
    "He picks up a bag from the floor with his humble hospital belongings - some clothes, drawings, and toys - and hurries to his parents, who are already waiting for him at the exit."
    "I smile through my tears and wave before the door closes behind them."
    "Violetta Cernovna, who has been standing on the sidelines the whole time, puts her hand on my shoulder."
    show cs normal with dissolve
    cs "You get more attached to some patients than you'd like, Hatsune."
    cs "That's one of the main difficulties of our work."
    show cs sad with dspr
    "She sighs heavily."
    cs "You've been through and seen a lot this year. Do you want to continue on that path now?"
    "I nod confidently."
    show cs normal with dspr
    mi "Working with Senya was difficult, but it was worth it."
    mi "Now I know for sure that social rehabilitation centers are needed in my home country!"
    show cs doubt with dspr
    "The doctor arches an eyebrow."
    cs "You do realize this is going to be more difficult than just leading and supporting one patient, right?"
    mi "I understand. But I'm not afraid!"
    show cs normal with dspr
    mi "There's a reason they call me «desperate Miku» in my homeland."
    mi "If I decide to take on something, I'll go all the way!"
    show cs smile with dspr
    "Violetta Cernovna looks at me with respect."
    "I have not yet done all that I can do."
    "But may fortune favor me along the way!"
    scene anim prolog_2 with fade3
    "Memory Shard unlocked - «All That I Can Do»"
    $ meet('am','Me')
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("mi_7dl_shard")
    show acm_logo_mi_7dl_shard with moveinright:
        pos (1600, 1020)
    pause(7.4)
    call alt_7dl_titles
    pause(1)
    return