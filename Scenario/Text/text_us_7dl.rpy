label alt_day6_us_7dl_begin:
    play music music_7dl["so_lonely"] fadein 5
    play ambience ambience_int_cabin_day fadein 2
    scene bg int_house_of_mt_sunset with dissolve
    "And again the rain whispers, again the silent voice in the silence of loneliness from which there is no escape, no way out."
    "It whispers that all it takes is to pick yourself up, to shake yourself up, and you can break through this insulating dome with your finger, through these walls with which you have punished yourself."
    "It would seem that punishment is an educational thing; it only serves to teach a person something."
    "But they are so dear to us, these seemingly immutable walls, that we cling to them, forgetting that this captivity is voluntary."
    "Only a few manage to do something, and then it is only an open chest and a scarred heart that in the first moments of freedom realizes: this world is plastic!"
    "The world that is up to your throat can be changed!"
    "Or to change yourself. {w}You just have to accept the idea that you can't do without difficulties."
    "Make the decision to change something at any cost."
    "That's it."
    "The outcome may or may not be liked, may be more difficult, unpleasant or even dangerous."
    "But it absolutely won't be the same thing you ran away from."
    "Like I did once."
    if counter_us_7dl_px >= 2:
        "And let the bright yellow tennis ball that turned into a star watch us!"
    with fade
    "Through half-closed eyelids the golden dawn knocked into consciousness, and there was no one on the next bed anymore."
    play sound sfx_knock_door2
    "There was a soft knock at the door, I wrapped myself in a blanket and shouted,"
    me "Open!"
    play sound sfx_open_door_strong
    show dv normal pioneer at zenterleft
    show sl normal pioneer at zenterright
    with dissolve
    "The door swung open, and at once the room became perceptibly small."
    "People I never thought I'd see together came in!"
    "And they didn't come in right."
    "It was the pioneers, the youth, the bubbling blood! They were supposed to come in crowds, laughing and jabbering, chatting excitedly and interrupting each other."
    "And these, however, entered officially, one by one, nodded to me demurely, and froze in the doorway."
    me "Hello."
    "I waved my hand from under the blanket."
    me "And you're here... Why?"
    show dv grin pioneer at left with dspr
    dv "Still asleep, sleepyhead?"
    "For a moment the old Dvachevskaya glimmered."
    "I glanced at my watch - it was still about fifteen minutes before I got up."
    show dv normal pioneer
    show sl smile pioneer
    with dspr
    sl "I'm sorry we did this without knocking and inviting you in. Have you seen Olga Dmitrievna?"
    "I shook my head slowly, catching a vibe of trouble in the air with my gut."
    me "She must be at the meeting."
    sl "Oh, yeah. Right."
    dv "We'll come back later then."
    with fade2
    "They hesitated, and I wondered:"
    me "What happened?"
    dv "Oh, never mind. Let's go, Slavya."
    "Slavya obediently nodded and, waiting for Alisa to come out, vacated the room herself."
    "My questioning cries they ignored completely."
    play sound sfx_open_dooor_campus_1
    hide sl
    hide dv
    with moveoutbottom
    "They did everything in a grotesquely correct and uncluttered manner."
    "Nodded to me, turned over the left shoulder."
    play sound sfx_close_door_1
    "Exaggeratedly neatly shut the door behind them."
    me "It doesn't make any sense."
    "I summarized, and after waiting for the footsteps on the stairs to subside, I climbed out from under the covers."
    "I wasn't in the mood for any more sleep."
    dreamgirl "They looked like they were missing something."
    th "Why do you think so?"
    dreamgirl "The eyes."
    "The inner voice grinned."
    dreamgirl "Like a battered dog, or a man who is late, stubbornly not noticing the keys in his hand, and keeps looking around the house for them."
    "After getting dressed, I went to the window and looked thoughtfully at what was going on outside."
    "Yesterday's obsessive crizzalism had faded into oblivion - the nature was no longer raging outside the window, and the dark under-bedroom comfort no longer seemed the most appealing thing in the world."
    "No, it was the most mundane summer dawn, the dew sprinkled on the lilac leaves in large drops, and it was quiet, as you only get just before you get up."
    "I knew it would be like this one day - I would wake up forgotten, and people passing by would only ask me about someone else."
    "That my half-forgotten {i}present{/i} would catch up with me here."
    "But I could not have known it would be so vile."
    "Staring out the window, I sang:"
    me "Shouldn't I sing a song... Shouldn't I sing? Huh? Shouldn't I sing?"
    "I sighed."
    me "No, I shouldn't."
    "There was a barely audible horn from the river - the forest curtain dampened all sound perfectly."
    if counter_us_7dl_px >= 2:
        "As stupid as Danechka's idea was, I saw a rational basis in it."
        "And even a desire to become a lighthouse keeper."
        th "Perhaps this boy will become something like me in the future?"
        "It suddenly occurred to me."
    "Anyway, it's time to get outside."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_exercises:
    scene bg ext_houses_sunset with fade
    play music music_list["my_daily_life"] fadein 5
    "A chill reeked in the air of the reluctant night, making me squirm and wrap myself vainly in a fleece shirt in search of the remnants of warmth."
    me "The people here are certainly good workers."
    "I muttered, recalling that in some of the camps, by the way, the enclosures are warm, stone, with bathrooms..."
    "Though what kind of camp would it be in that case?"
    "Well, a sanatorium."
    "The camp was waking up."
    "The squad leaders were already poking around between the cabins, knocking on doors and breaking into rooms."
    "And here's the thing - the older the squad was, the rarer the last one was."
    th "Afraid the pioneers might throw something in their sleep?"
    dreamgirl "Rather, they respect the right of teenagers to be a little embarrassed by their young, handsome squad leaders."
    dreamgirl "Although some don't understand the meaning of the word at all. Here, for example."
    "On the porch of the cabin Miku was sleepily stretching, clearly in no hurry to wash her face or wake up at all."
    "I waved at her, and she smiled at me, but then, with an owl, she covered her yawn with her hand."
    th "Sleepy sleepyhead."
    "I grinned, turning onto the path that led to the washbasin."
    if counter_us_7dl_px == 3:
        scene bg ext_washstand_day
        with dissolve
        "As I approached the washbasins, I noticed that I had company to splash."
        show el normal pioneer with dspr
        el "Good morning."
        "Smiled Electronik."
        el "Do you know yet?"
        me "Know what?"
        "Electronik was easy to talk to - he didn't make a big deal out of himself, didn't get cocky, and generally talked briefly and to the point."
        el "Lena and Ulyana are missing."
        me "What do you mean, missing?"
        "Elektronik smiled lightly and twitched his shoulder."
        el "Slavya went out for a jog in the morning, and there's Alisa - she doesn't know where her roommate went."
        show el smile pioneer with dspr
        el "Started looking around the camp, and there's Miku out of the house."
        el "It turned out that Lena had also disappeared somewhere."
        me "And you talk about it so calmly?"
        show el normal pioneer with dspr
        el "I'm not really worried about Lena.Firstly, Her father's a policeman! Taught her all sorts of things."
        me "And secondly?"
        "He shook his head lightly."
        el "And secondly, she runs away like that every year on the last day, she has that habit."
        el "And she runs away so well, they couldn't find her."
        show el smile pioneer with dspr
        el "That's the way it is."
        "He swirled the water and waved to me:"
        el "See you later."
        hide el with dissolve
    "The Meeting Place can not be changed, meet me in hell!"
    "The brass and tile monster lurked in its place and smirked carnivorously, waiting for its next victim."
    me "You have no power here, washcloth."
    "I squinted, gathering my wits."
    scene bg ext_washstand2_day at zentercenter
    with dissolve2
    play sound sfx_open_water_sink
    pause(1)
    play sound_loop sfx_water_sink_stream
    "No power, yeah..."
    me "A-ah!" with vpunch
    "Except the power over the breath."
    "And over the lucidity of the camp around me."
    "It suddenly occurred to me that if this were all a banal dream, how could I have imagined and enacted such a nightmare?"
    "Oh, so what?"
    th "Is all this for real?"
    dreamgirl "There is some doubt..."
    me "Ahhhh!" with vpunch
    "No! There are no doubts."
    "After gutting the box of powder, I worked up a brush, wary of staying away from the liquid ice."
    "Naively hoping that now the water would come off a little, and..."
    "The sun should be starting to warm it up by now!"
    me "Yh!" with vpunch
    dreamgirl "To be healthy - harden yourself! Bare belly on a nail and spin!"
    "Now, instead of being a blatant prankster, the inner voice had switched to quite innocent sneers."
    "And I wasn't sure I was happy about the replacement."
    "After all, it's not much nicer to think about girl-s than spinning your belly on a nail."
    dreamgirl "You should have gotten up early, then you would have had something to think about!"
    th "Thanks, no."
    "I can take a hint."
    th "I'm still ashamed of my attempts to peek under the covers."
    dreamgirl "I'm not the least bit embarrassed. And I got to see a lot more while you were sniffing."
    th "I wasn't sniveling!"
    dreamgirl "Wash your face. You'll be sublimating creativity or some other sport."
    dreamgirl "Since you're such a freak."
    "While I was scrubbing my jaw and arguing with my inner chatterbox, the water didn't warm up a degree."
    "So I had to endure the torment and deprivation once more."
    me "Brrrrr."
    stop sound_loop
    play sound sfx_close_water_sink
    pause(1)
    scene bg int_house_of_mt_sunset at zentercenter
    show mt smile sport
    with fade
    if counter_us_7dl_px == 3:
        "When I got home washed up, I found the squad leader there."
        "Despite Al's tales, she didn't look frightened or depressed."
        "She was smiling and blooming like a rose of May."
    else:
        "Olga Dmitrievna was still sitting in her seat, as if she hadn't gone anywhere."
        "It seems that she decided not to remember yesterday's adventures of mine."
        th "Or she was planning some particularly devious trick to take revenge on me for thousands of years of deprivation."
    mt "Yesterday's indulgences are over, it's time to get back on track!"
    "she reported cheerfully."
    mt "I hope you slept well and gained strength, for today will be a long day."
    "All in the same tone, as if it were the best news you could ever hear."
    if counter_us_7dl_px == 3:
        me "What about Lena and Ulyana?"
        show mt normal sport with dspr
        mt "Tikhonova asked me if she can leave yesterday, I let her go. But Ulyanka will get hers!"
        "That's where I don't understand at all."
        me "What do you mean, «asked me if she can leave»?"
        mt "Literally. I have an arrangement with her father, and... It's a long story."
        mt "What's more important now is morning exercise!"
        "I thought this prioritization seemed strange and opened my mouth to argue, but she had already jumped in:"
    else:
        "There was no sadness."
        me "Why the long one?"
        mt "You'll find out at the lineup!"
        me "I figured as much."
        mt "What do we always have before the lineup?"
        me "Coffee and buns?"
        "The squad leader laughed:"
    mt "For exercise run... March!"
    play sound sfx_open_dooor_campus_1
    scene bg ext_house_of_mt_sunset with fade
    play ambience ambience_camp_center_day fadein 3
    "After pushing me out the door, the squad leader locked the cabin:"
    show mt normal sport with dspr
    mt "I know you! You're bound to come back to sleep."
    me "Didn't even thought of it!"
    show mt smile sport with dspr
    mt "Yes, yes. March!"
    "She turned me around to face the square and nudged me."
    scene bg ext_square_sunset with dissolve
    "I've always wondered how it is that Olga manages to get all this crowd here?"
    "Personally for me it was more like trying to juggle a dozen balls at once."
    "No matter how nimble you are, you can't keep it all in the air at once."
    "So it is here: you chase one, the second one settles, you pick it up, the third one escapes."
    "But Olga seemed to think juggling ten balls was a very doable job."
    "Nodding to us, she stood just behind the crowd, keeping a watchful eye to make sure no one got separated from the herd."
    "And a minute later our sportswoman appeared."
    show sl smile sport with easeinright
    "As irresistible as ever, squeaky clean and disgustingly chipper."
    th "Nothing pisses me off in the morning like everything."
    "But Slavya can't be beaten even with a crowbar. She looked us over, stood in front of the podium and waved her hand dashingly."
    play music music_list["always_ready"] fadein 3
    sl "Fizkult-hello!"
    "The herd grimaced, apparently expressing how immensely excited they were to start exercising, although I heard something like «yeah go shave» from the back rows."
    "Or perhaps I imagined it all, and the people around me are asleep and dream of waving their arms?"
    "I looked around."
    "No, it's crazy."
    sl "Legs shoulder width apart, arms swinging, and - one!"
    hide sl with dissolve
    "The workout started."
    show mi normal casual at zenterright with dissolve
    "There was a person I never expected to see here today."
    "Miku."
    "In a sort of semi-sporty outfit, she was waving her limbs around and enjoying life with all her Japanese strength."
    "But her roommate could not be seen."
    "I even suspected that Miku had come on purpose to replace Lena in case we were suddenly counted by the heads."
    hide mi with dissolve
    if (loki and counter_us_7dl_px >= 1) or (counter_us_7dl_px >= 2):
        show dn sick pioneer at zenterleft
        show tn shy pioneer at fleft behind dn
        show al normal pioneer at cright behind dn
        with dissolve
        "Danechka and his companions were here, too."
        "That's to be expected: the future lighthouse keeper must be fit."
        "Though I could tell by the look on Danechka's face that he'd seen such a fit in his grave."
        hide dn
        hide al
        hide tn
        with dissolve
    if counter_us_7dl_px == 3:
        show dv sad sport with dissolve
        "Alisa was clearly worried about her absent friend, she twisted and looked around for red tails."
        "In vain, of course."
        hide dv with dissolve
    else:
        show dv normal sport at left
        show us normal sport at right
        with dissolve
        "The tandem of redheads was also present in full - in solidarity with me, they were asleep on foot."
        "With eyes open."
        "A rare skill!"
        "Sensing my gaze, they responded with sour smiles and went back to sleep."
        hide dv
        hide us
        with dissolve
    th "My squad."
    th "My."
    "And I could hardly associate myself with all those young men."
    "No, I didn't feel like a stranger, and my conscience didn't bother me."
    "It's like being a no-squad person, free of all the regime moments and showing up on the territory while the rest of pioneers are busy with some regime blizzard."
    "And you look at each other like that - with mutual, mutual envy."
    "Pioneers are sick and tired of all this regime nonsense, they should take a vacation..."
    "Or let it rain or something."
    "Then no one will be chasing you anywhere, you can lie in bed, read a book."
    "Take a break from the hustle and bustle of camp."
    "And you're fed up with being a loner."
    "Though we're both well aware of the pluses of our situation."
    "But it's not for nothing that they say someone else's is sweeter."
    "After finishing her pelvic girdle warm-up, which looked extremely erotic in her performance, Slavua shouted something and ran off for a jog."
    "Some of the pioneers reached for her."
    show mt smile  pioneer with moveinleft
    mt "Why didn't you go for a run?"
    "The squad leader, who inexplicably had time to change her clothes, came up to me and clapped me on the shoulder."
    mt "Running is good for your health!"
    me "You yourself..."
    "I mumbled."
    show mt grin pioneer with dspr
    mt "I can't."
    "Olga sighed."
    mt "I have a lineup to lead, else I'd definitely go for a run."
    me "Yeah sure."
    "Olga laughed and scurried off to the podium."
    hide mt with dissolve
    stop music fadeout 3
    "I went to our squad place."
    "To lineup."
    "A few minutes later I was joined by Slavya and the other pioneers I had already noticed."
    "Lena was absent."
    if counter_us_7dl_px == 3:
        "Ulyanka disappeared into nowhere."
    show sl normal pioneer with dspr
    sl "Semyon, have you seen Lena?"
    "Slavya looked worried, obviously lost someone."
    me "No. She's not at morning exercise either."
    sl "She's nowhere to be seen at all. {w}And Olga Dmitrievna told me not to look for her."
    me "Maybe she's on a responsible party assignment?"
    show sl smile pioneer with dspr
    sl "Good attitude. And you looked pretty good at the exercise, too."
    show sl normal pioneer with dspr
    sl "If it wasn't for the last day, I'd even recommend you to Olga Dmitrievna to lead the exercise."
    me "And you?"
    "I didn't get it."
    sl "We'd work in shifts, two by two!"
    me "Thanks, but I'll pass."
    show sl laugh pioneer with dspr
    sl "That's okay, I could have talked you into it."
    "Slavya laughed, and we were shushed from the podium."
    "We were immediately silent and feigned official zeal."
    if counter_us_7dl_px == 3:
        scene cg d4_lineup_no_un_us_7dl
    else:
        scene cg d4_lineup_no_un_7dl
    "In vain, though - it was only our squad that lined up in full."
    "Well... As far as it was possible under the circumstances."
    "The other squads didn't have the same discipline, so it was fine to chat some more."
    "Especially since I don't mind."
    "And Slavya?"
    "After squinting at her, I gave up on the idea with a sigh."
    "She bulged her eyes, her chest was puffed out, and she stretched out, but the faint haze in her gaze gave her away."
    th "A curious form of trance."
    "The speakers yelled something resembling a horn, and Olga Dmitrievna cleared her throat."
    mt "Good morning, Sovynok!"
    "She barked."
    voice "Boo... boo-boo-boo..."
    "The pioneers called out."
    mt "Pioneers, stay awake! Good morning, camp!"
    "The ranks drew up, a thunderous voice thundered into the morning air:"
    voice "Hello! Jalam! Tovarisch senior squad leader!"
    mt "That's right!"
    scene bg ext_square_sunset
    show mt normal  pioneer at zenterleft
    with dissolve
    "After looking over the ranks again, the squad leader nodded contentedly."
    mt "Dear friends, today is the last day of the second session, so it's farewell day."
    "Sergeant Hartman would kill himself for a voice like that."
    "But in private she's all right, such a nice girl, her voice husky, velvety."
    mt "Today you need to finish all the things you haven't done, turn in all your debts, and get a good last rest."
    mt "Even those of you who are staying for the third session will have to meet it in a clean and tidy camp, so the duty squad will have to work hard!"
    show mt normal pioneer with dspr
    mt "But the most important thing is tonight's gala!"
    mt "So those of you who are involved in the program will be relieved of all duties and responsibilities this afternoon."
    mt "My condition is one!"
    "Olga Dmitrievna continued to rumble."
    show mt angry pioneer with dspr
    mt "You {b}are obliged{/b} to be at the rehearsal!"
    mt "If I find out that you slack off and don't show up at the stage... Well, I've warned you!"
    th "Oh, how scary."
    if counter_us_7dl_px == 3:
        "In case of what we did yesterday with the little one and her disappearance today..."
        "To make a long story short, the threats didn't scare me."
        "I felt the corners of my lips move apart against my will as I remembered how we had gone on a mission as a gang."
        dreamgirl "The bandits. The bandits are real!"
        th "Envy is a bad feeling."
        dreamgirl "I didn't feel like it."
        th "Yeah. Yeah."
    else:
        "I'm not going to be on duty or singing today."
        "Even though I've had my share of bad luck with the squad leader, it ended up being relatively harmless this time."
        "They didn't even put me on canteen duty!"
        "How do I know?"
        "So they didn't get me up half an hour before we got up, like last time!"
    mt "And in the evening after dinner, a farewell disco!"
    mt "Since it's a holiday, it will be extended for a whole hour for the older squads!"
    play sound sfx_7dl["eat_horn"] fadein 1
    "A jubilant shriek drowned out both the words of the squad leader and the horn that screamed in no hurry."
    play ambience ambience_camp_center_evening
    "Olga Dmitrievna said something else, but no one listened to her."
    show mt normal pioneer with dspr
    "In the end she just sighed and with a gracious wave of her hand blessed the pioneers to go to the canteen."
    hide mt with dissolve
    "Turning around with everyone else, I went as well."
    stop music fadeout 3
    stop sound fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_breakfast:
    scene bg int_dining_hall_people_sunset_7dl with dissolve
    play ambience ambience_dining_hall_full fadein 3
    play music music_list["everyday_theme"] fadein 5
    "Despite the fact that we were sort of the first squad, in fact, we were always the last to get to the canteen."
    "I don't know why is that, but there's only one way to eat quietly."
    "A nighttime break-in."
    if alt_day_binder != 1:
        if (counter_us_7dl_px == 2) and (not alt_day5_me_neu_us_stores):
            "Although, remembering yesterday, it's not exactly a peaceful option either."
            "And all because of one little walking disaster."
        else:
            "As Alisa and Ulyana tried to do a few days ago."
            "Unsuccessfully, of course - they didn't eat anything, and moreover got caught by Slavya."
        "And now, Ulyana was standing in line in front of me, and she was looking at the squad leader."
        if (counter_us_7dl_px == 2) and (not alt_day5_me_neu_us_stores):
            "Dummie."
        else:
            "Two dummies."
    else:
        "Ulyana was standing in line in front of me, but she kept looking at the squad leader."
    "Olga, on the contrary, felt quite wonderful in the midst of this commotion, smiling, exchanging some phrases with the leader of the second squad standing there."
    "They're the lucky ones, they're the ones on duty!"
    "Anyway, my turn came up, and I took a plate of porridge and a couple of sandwiches and started figuring out where to sit."
    menu:
        "Sit with Miku" if (alt_day2_date == 'mi') and (alt_day2_mi_date != 2):
            $ alt_day6_us_7dl_mi_friends = 1
            "Miku was sitting alone, as usual."
            "And this was completely out of my mind."
            "For all her faults, like her talkativeness and total lack of tact, the Japanese girl had one undeniable advantage."
            "She was a very beautiful."
            "Hell, just to talk to a pretty girl, some people would put up with a lot more than that."
            dreamgirl "After all, there is such a thing as training."
            th "Pardon?"
            dreamgirl "Uh, I mean, compromise, yes."
            show mi normal pioneer with dspr
            mi "Oh, a company."
            "Miku nodded to me."
            mi "What typhooned you to us?"
            "I smiled:"
            me "Just felt like sitting next to you. May I?"
            "Her flippant tone didn't deceive me, as she diligently finished her chewing and only then looked up at me:"
            show mi sad pioneer with dspr
            mi "What, do I look that bad?"
            th "No, you look just fine."
            me "Judging by the fact that today you perform the role of Lena sitting with a dejected expression, so that even the squad leader did not notice anything..."
            me "By the way, where is your roommate?"
            show mi normal pioneer with dspr
            mi "God knows."
            mi "Packed up at about six in the morning, went outside. I haven't seen her since."
            me "Do you know where she might have gone?"
            "I had a hunch or two, sure."
            show mi smile pioneer with dspr
            mi "Judging by the swimsuit under her uniform - somewhere to the water for sure. To swim, probably, or to make a campfire and swim too."
            me "Not a bad way to spend the last day either. Bon appetit, by the way."
            "Miku nodded."
            show mi normal pioneer with dspr
            mi "I think differently. You can spend the day alone at home. You don't have to go to some camp for that at all, do you think?"
            me "What's the right way?"
            show mi happy pioneer with dspr
            mi "You have to sing like it's the last time, dance like nobody can see you, enjoy the people around you! And..."
            show mi upset pioneer with dissolve
            mi "Communicating..."
            "She faded."
            me "Why don't you go to the disco then, too?"
            show mi smile pioneer with dspr
            mi "We still have to survive till disco. And the most important thing is my concert tonight."
            if alt_day3_date == 'dv':
                mi "I thought you played the guitar pretty well. Would you like to participate?"
                me "Participate in what? Making fun of Semyon with a guitar?"
                me "With my playing class, I'll be able to take only three blatant chords."
            else:
                mi "You don't sing or dance, by any chance?"
                me "Only foul ditties."
            show mi laugh pioneer with dspr
            mi "Thank you, we don't need that kind."
            "Miku laughed, shaking her head."
            "She seemed to be starting to come around, little by little-at least, there was more of the familiar Miku in her now."
            me "That's all I know."
            show mi sad pioneer with dspr
            mi "Sen, you should have applied, we would have made something up for you."
            mi "We would have put on and rehearsed something."
            me "Gopac?"
            "No, the sense of rhythm and the voice didn't go anywhere, but something didn't warm me up to performing."
            me "You know, you can't learn anything harder in four days."
            show mi smile pioneer with dspr
            mi "That's what you think, but when the need comes up... The need will teach you, the need will make you! Does that seem right?"
            "I nodded."
            "The Japanese girl was right about something: force majeure sometimes makes a man perform even more miraculous things."
            "But I didn't want to become a victim of force majeure or a guinea pig of this spirituality."
            "So I shook my head."
            me "Now there is no point in talking about what I'm capable of and what I'm not. The train has left."
            mi "Yeah, I guess..."
            show mi happy pioneer with dspr
            "That's where she glowed."
            mi "You can still do a good deed though!"
            show mi normal pioneer with dissolve
            me "Which one is that, I wonder?"
            mi "As a real cavalier, you shouldn't leave a girl in trouble, and I need help!"
            dreamgirl "Cavalier?"
            me "Help?"
            mi "I've got a whole lot of work to do right now, setting up and decorating."
            "She leaned closer to me and lowered her voice:"
            mi "Honestly, I have a hard time understanding how they've managed it all these years, until the camp's unreliable Hatsune came along?"
            th "With God's help, how."
            me "What's required of me?"
            "I protracted, already guessing where she was going with this."
            show mi normal pioneer with dspr
            mi "No, you don't have to carry anything heavy! Well, almost."
            mi "It's just nice to have you around to talk to. Sometimes, when you don't talk all the time, you work and work and work! And you don't talk!"
            if alt_day3_date == 'mi':
                mi "You, for example, came - but then quickly ran away! Few people can stand me for long at all."
            "She sighed."
            mi "Such a longing."
            me "Shall I keep you company at the music club?"
            show mi shy pioneer with dspr
            "The Japanese girl shook her head:"
            mi "No, not there. Although..."
            me "Okay, once you figure out your split personality, let me know. I'll think about it."
            dreamgirl "Hey, I'm a unique phenomenon!"
            th "Shh... Unique phenomenon."
            show mi laugh pioneer with dspr
            mi "Okay, okay! I need an assistant, a partner, and someone to talk to me!"
            th "You need a boy. Someone who's not too shy or embarrassed."
            dreamgirl "Are you offering yourself as a candidate?"
            th "I don't think that's a good idea."
            dreamgirl "You should!"
            show mi smile pioneer with dspr
            mi "Can I count on you?"
            me "Count on it, but I'm not sure I can make it yet."
            mi "Tell Olga Dmitrievna you're coming to help me, and she'll let you go right away!"
            mi "She won't even check."
            th "I can guess why."
            me "I'll think about it, okay? Half an hour won't make a difference."
            show mi serious pioneer with dspr
            hide mi with easeoutright
            "Miku bit her lip, but without saying anything back, she got up, leaving me alone."
        "Sit with Slavya":
            $ alt_day6_us_7dl_sl_friends = 1
            show sl smile pioneer with dissolve
            "Slavya smiled when I inquired:"
            me "May I?"
            "And nodded at the seat next to me."
            me "Bon appetit!"
            sl "You too!"
            "Sandwiches and porridge are our food."
            "Today for a change we were not poisoned with cocoa with condensed milk."
            "In fact, I'm getting a little too demanding, yeah."
            "Compared to the unearthly cuisine I had at home, when I had a choice of Doshirak with mayonnaise and Doshirak with no mayonnaise, the local cuisine was very refined."
            "That's just me getting cocky."
            sl "You'd better fill up, there's a lot of work to be done."
            sl "Olga Dmitrievna knows how to set tasks so that before lunch there's no time for a break."
            me "I thought you were happy with that?"
            "Well, of course, the military logic: whatever a soldier does, he should be tired all the time."
            show sl smile2 pioneer with dspr
            sl "I haven't been given any assignments for a long time."
            me "You don't look like a skive."
            "I pointed out."
            show sl normal pioneer with dspr
            sl "I have more trust."
            "Slavya didn't hesitate long with her answer."
            "Apparently she had been asked more than once about that, too: the patiently tired notes of a tech-support specialist evidently crept into her tone."
            me "Do you really go around collecting assignments to the bulletin board?"
            "I grinned."
            show sl smile pioneer with dspr
            th "They give you exp, gold, and..."
            dreamgirl "Hit with a broom!"
            sl "Actually, I've been making up my own activities for a very long time."
            me "Making up? Why don't you come up with an activity for us to go to the beach, then?"
            show sl laugh pioneer with flash
            "It wasn't a bad try, it was definitely worth a try."
            sl "No! I must have misspoken."
            sl "But I have a list of responsibilities, and I do them to the best of my ability."
            me "Voluntary, I guess, responsibilities."
            show sl smile pioneer
            with fade2
            "Slavya nodded."
            sl "I just got some time today to sort out some uniforms and underwear in the warehouse."
            sl "Gotta get ready for the next shift."
            show sl normal pioneer with dissolve
            sl "Actually, I didn't ask Olga Dmitrievna for people, but if you ask, I'm sure she'll let you go help me."
            "The girl said it in such a tone, as if refusal was knowingly impossible."
            th "Insolence is another blessing!"
            if loki:
                me "Help you?"
                sl "Yes, if you want."
                me "And if I don't?"
                show sl serious pioneer with dspr
                "Slavya sighed:"
                sl "I could do it alone, but you have other things to do besides the tasks from the squad leader, don't you?"
                "She looked toward Ulyanka with a hint."
                with flash_pink
                "I felt my cheeks turn red, and hastened to refute all the insinuations:"
                me "Of course there is! But it has nothing to do with Ulyana."
                show sl laugh pioneer with dspr
                sl "I figured as much. But if you suddenly decide to do something - alone, without Ulyana - you can volunteer to help me in the warehouse."
                sl "Think about it."
            else:
                me "Do you think they'll just let me go?"
                sl "You know, I think Olga Dmitrievna is going to have too much to do right now, and besides persuading me to get busy cleaning up the territory or getting ready for the concert."
                me "What other options are there?"
                show sl smile pioneer with dspr
                sl "Plenty of options!"
                "Slavya began to curl her fingers:"
                sl "Cleaning the area with the duty squad - one."
                sl "Preparing for the concert with Miku - two!"
                sl "Help with the warehouse - three."
                sl "The wall newspaper, four!"
                "Here she lowered her voice:"
                show sl normal pioneer with dspr
                sl "Although, Lena is missing somewhere, and I'm very worried about her."
                me "Not for the paper?"
                show sl sad pioneer with dspr
                sl "I've known Lena for years, and when she starts acting {i}strange{/i}, It makes me worry."
                me "How long have you known each other?"
                "I wasn't interested in their history, but I should be polite."
                show sl surprise pioneer with dspr
                sl "You know..."
                "Slavya slowly began, looking at me strangely somehow."
                sl "We go to the same school."
                sl "But sometimes I feel like I've only really gotten to know her recently."
                me "Did something happen?"
                "Slavya reluctantly nodded."
                show sl serious pioneer with dspr
                sl "There was... a reason, yes."
                sl "But it's a long story, I won't tell it now."
                me "Is that how it is?"
                me "What if I came to your warehouse to help?"
                show sl normal pioneer with dspr
                sl "Seyomushka, have a conscience!"
                sl "It's not just my story, it's also Lena's story."
                me "Fine."
                "I mumbled."
                me "As if I was interested..."
                "Slavya went up."
                sl "Think about my offer, though, okay?"
            me "Okay."
            "As if I had any choice."
            hide sl with easeoutleft
            extend " And Slavya, lighting me up with one last smile, ran away."
        "Sit with Ulyana":
            $ counter_us_7dl += 1
            "Actually, I thought I'd sit next to Ulyanka-I had something to talk to her about, but the little one flopped down on a bench in the middle of nowhere, so I had to choose a seat in the middle of nowhere."
            dreamgirl "The men-cave."
            th "Thank you, nerd."
            "Well, it looks like we'll really have to sit somewhere alone."
            "Sneaking between the pioneers and the window, where Electronik had just finished his meal, I hurried to take a seat."
            "I had things to think about and things to be quiet about."
            "Like what?"
            "Yes, about strange disappearances, for instance."
            "The strange behavior of some pioneers and pioneer girls."
            if counter_us_7dl_px > 1:
                "About the totally inexplicable abilities of some local chegevars."
            else:
                "About the obsession with «not dating» by one mischievous toddler that keeps driving me into the red, finally!"
            "There was a lot to talk about."
            "Fortunately, today I wasn't in any hurry to prove anything to anyone."
            me "Itadakimasu."
            "I wished, and after bowing out to Miku, who had turned around at the sound of her native language, took my meal."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_separation:
    scene bg ext_dining_hall_near_day with dissolve
    play ambience ambience_camp_center_evening fadein 3
    play music music_7dl["temptation"] fadein 3
    "Ulyana had already finished breakfast and was sitting on the porch, legs overhung, leaning against the lower longitudinal tube of the fence - throwing pebbles."
    "Somebody drew «classics», and there was already a palpable sort of pile of limestone stumps huddled in the «cauldron» - hits."
    me "Are you waiting for me?"
    "Without turning around, she twitched her shoulder."
    me "Who then?"
    "Zero reaction again."
    me "Did something happen?"
    show us normal pioneer with dissolve
    us "Does something have to happen?"
    me "You're just kind of... I don't know. Weird?"
    us "I just think."
    me "About what?"
    us "That it's not me that's weird, it's you."
    me "What do you mean?"
    "Ulyana, looking somewhere off to the side, spoke:"
    if counter_us_7dl_px >= 2:
        us "We believed you, you know?"
        us "Me, Danka, the boys."
        us "It seemed like you could replace Mirya."
        me "Can't I?"
        us "I don't know. Can you?"
        me "Well..."
        show us dontlike pioneer with dspr
        us "See."
    elif counter_us_7dl_px == 1:
        us "You tried so hard then to get to the pier, to our pier."
        us "You have succeeded. Now what?"
        me "Go all the way, you said so yourself."
        show us calml pioneer with dspr
        us "But can you do it?"
    else:
        us "You wooed me so touchingly yesterday."
        if alt_day5_me_neu_us_potato:
            us "I even shared a potato when I was punished."
        me "You mean I shouldn't?"
        show us shy pioneer with dspr
        us "I don't know!"
        "Desperately cried out the girl."
        us "I thought yesterday, today."
        us "What do you want from me, Syomych, can you tell me? Why do you follow me?"
        with flash2_red
        "I felt myself blushing."
        me "It's nothing! Don't you need any excuse to help a comrade?"
        show us normal pioneer with dspr
        us "You're a fool, Syomych."
        "Ruthlessly nailed Ulyana."
        us "And you don't know what you want, and you're in my way."
        me "What did I do?"
    show us sad pioneer with dspr
    us "Lately, if you're anywhere near me, I'm always out of luck."
    us "You're like bad sign, you know?"
    us "Loser syndrome."
    me "What did I do?"
    stop music fadeout 3
    show us normal pioneer with dspr
    play music music_list["you_lost_me"] fadein 3
    us "Nothing."
    us "And that's the worst part. And I had so much to do, the boys and I almost found-"
    "She cut herself off."
    us "No, you don't need to know that."
    "She looked me in the eyes for the first time in the whole conversation:"
    us "Please, Syomych. Don't follow me. Okay?"
    me "But..."
    us "At least let me have something today. Give me a gift like that."
    th "She's not speaking in her own words."
    "It suddenly occurred to me."
    th "Alien, indifferent, rehearsed to the shine and bounce of her teeth."
    "Though this indifference itself is not fatal."
    "Much worse than that: the man who taught Ulyana these words does not himself understand why they are alien and indifferent."
    "Why they do not come from the mouth of an immediate and sunny child."
    "And this... teacher of hers."
    "Me, too, of course."
    "We, too, when we were children, were so generous."
    "So forgiving in our youth."
    "But as soon as we got a little older, it all disappeared."
    "Gone with ashes and dust, no epithet is enough to answer one simple question."
    th "Where have the young us gone?"
    me "You know, Ulyana."
    "I began, smiling diligently."
    me "You and I aren't a couple in love to break up so dramatically, are we?"
    show us shy pioneer with dspr
    me "You could have just told me something like «piss off, you're hindrance», couldn't you?"
    me "What's this all about then?"
    show us shy2 pioneer with dspr
    us "Oh, you're such a fool, Syomych."
    us "That's right Aliska said - you are so retarded that you do not understand even the obvious."
    us "And I..."
    "Shaking her head, she stood up."
    show us laugh2 pioneer with dspr
    "She shook herself all over, like a dog shaking off after a bath."
    "And melancholy, like water, dripped from her, frozen in puddles floating in the sun at her feet."
    us "Since you ask so desperately..."
    show us laugh pioneer close with moveinbottom
    "She was suddenly right up close, so I could smell the tooth powder and the elusive scent emanating from her hair."
    us "Piss off! You're hindrance!" with vpunch
    "I flinched and squinted in surprise."
    show blink
    pause(3)
    scene bg ext_dining_hall_near_day
    show unblink
    "And when I opened my eyes, I found I was alone."
    "Only the echoes of laughter came from somewhere behind me."
    me "Well..."
    "I stretched out and sat down on the bench."
    "I need to come to my senses."
    th "What kind of fly bit her...?"
    "I asked myself."
    show dreamgirl_overlay with dsps
    dreamgirl "Syomych, no offense, but you're a retard."
    dreamgirl "And it's not some kind of mental illness, you are a redditoid."
    th "What are you all talking about?!"
    dreamgirl "About..."
    stop music fadeout 3
    return

label alt_day6_us_7dl_helping:
    scene bg ext_dining_hall_near_day with dissolve
    "My inner voice started, but it stopped immediately: we had company."
    play music music_list["take_me_beautifully"] fadein 1
    show sl smile pioneer with dissolve
    sl "Hi again."
    "I waved to her."
    me "How can I?.."
    show sl smile2 pioneer with dspr
    sl "You can, Syomushka, you can."
    if alt_day6_us_7dl_sl_friends == 1:
        sl "Thought about my offer?"
        me "Are you sure you want my help?"
        "I squinted suspiciously."
        show sl normal pioneer with dspq
        sl "Not really. I'm fine on my own."
        sl "But it's more fun together! What do you think?"
        "I had an opinion about that."
        me "It's more fun to bum around together."
        sl "Bummer."
        me "That's where we stand!"
        sl "So you refuse?"
        me "I didn't say that."
        show sl laugh pioneer with dspr
        sl "Women's logic played by Semyon."
        sl "But you'll still have to do something, if the squad leader finds you loitering, you and I will be screwed."
        "I rolled the thought around in my head."
        if loki:
            me "What other options are there?"
            show sl serious pioneer with dspr
            sl "There are a lot of different ones."
            sl "The most important ones are the completion of the wall newspaper, the concert, and the general cleaning of the camp."
            sl "I also heard that Boris Sanich is recruiting a group to look for Lena."
            me "Doesn't she have an arrangement with a squad leader?"
            show sl surprise pioneer with dspr
            sl "I haven't heard anything like that. And even if I have, what kind of arrangement is this?"
        else:
            me "So helping you - and no options?"
            show sl laugh pioneer with dspr
            sl "It's not all that sad. We need different people."
            me "I can't draw, so there's nothing else to do."
            show sl normal pioneer with dspr
            sl "Yes, we can't finish the newspaper without Lena."
            sl "But if you don't want revenge that badly, you'd better help me."
    elif alt_day6_us_7dl_mi_friends == 1:
        th "Work will be real in..."
        "I predicted it, and I wasn't wrong."
        sl "Now there's final preparations around the camp, newspapers... Well you know already."
        me "Yes. And?"
        sl "And? We've got to help. We've all got to work hard together, and..."
        if loki:
            me "Togeeether?"
            "I muttered, quietly furious."
            show sl surprise pioneer with dspr
            me "Is it okay that the only person you have on your hands to prepare and conduct the concert is frozen on the brink of depression? How about helping her?"
            me "Is it okay that only one person spoke to her today, and that person is me?"
            me "What is she to you, a day laborer for three pennies? A pariah?"
            sl "That's not true, Semyon, we all love Miku very much, and..."
            me "Like hell you do!"
            "I got up from the bench."
            me "She's just as much a pioneer as you and me, and has exactly the same rights."
            me "What's wrong with this camp?"
            show sl serious pioneer with dspr
            sl "I'd love to talk to her, but you know I have a lot to do."
            me "See."
            "I jabbed an accusing finger at her."
            me "Even you, as many people here say, «the best pioneer», can't solve one little problem of the lonely art director."
            show sl smile pioneer with dspr
            sl "You know, if you want, you can keep her company."
            "Slavya smiled."
            sl "And I'll be free by one o'clock, we can go to the beach together then."
            me "That's something at least."
            "I grumbled, cooling down."
            "Not so indifferent people after all, as it seemed."
            dreamgirl "It turned out they weren't."
        else:
            me "You know, I chatted with Miku at breakfast."
            if (alt_day2_date == 'mi'):
                me "I've been watching her for a while; well, she really needs company."
            else:
                me "I don't know what happened here before I got here, but now she's desperate for company."
            show sl normal pioneer with dspr
            sl "Lena used to talk to her, but now... You can see for yourself."
            me "So there's no way to help her?"
            sl "Why not? You could go to her club and help her with the equipment."
            th "Or find her roommate, since she's such a helper."
            me "That's not a bad idea."
        sl "Then I note that you're going to help Miku?"
    else:
        sl "Do you happen to know anything about hardware?"
        "I'm wary."
        me "What, are cyberneticists lost somewhere?"
        show sl laugh pioneer with dspr
        sl "They are! I fought my way out of half their clubhouse, so they're sitting there right now making sure the freewolly club doesn't break anything inadvertently."
        me "Got it. What's my knowledge for?"
        sl "Miku need help with taking the equipment apart and getting ready for the concert. You'll help, won't you? You gotta help!"
        me "What do you mean help? What about Lena?"
        show sl normal pioneer with dspr
        sl "Lena is on uncle Borya and Violetta Cernovna."
        sl "But if you suddenly don't understand anything about all these wires, I just need an assistant in the warehouse."
        "She smiled dazzlingly."
        sl "You will help, won't you?"
    "I sighed."
    menu:
        "Go with Slavya":
            if alt_day6_us_7dl_mi_friends == 1:
                me "No, I'll go help you."
                "Slavya was right: if we get it over with quickly now, we can join in for preparing the next performance."
                "And together we'll manage faster and better anyway."
                dreamgirl "And swim! Imagine Miku in a swimsuit!"
                "I had nothing against that idea."
                "Though it did leave something on my heart - a residue, an understatement."
                th "Did I have a conscience?"
                "However, it was too late to play it out."
                if loki:
                    me "Just remember, you promised you wouldn't let Miku get bored today. You promised!"
                    show sl smile pioneer with dspr
                    sl "I promised, I will deliver. So are we going?"
            else:
                "The sooner we start, the sooner we finish."
                me "I'll help, of course."
            me "I hope they don't put me in front of a basin of cold water."
            "I grumbled."
            me "My name isn't Martin Eden after all."
            "Slavya giggled, clearly catching the reference and, taking my hand, dragged me along toward the warehouse."
            $ alt_day6_us_7dl_sl_friends = 2
        "Help Miku" if (alt_day6_us_7dl_mi_friends == 1):
            if loki:
                me "This is going to sound stupid and edgy, but Miku has to be saved."
                show sl shy pioneer with dspr
                me "And since you don't want to do it, and Lena's gone somewhere, I'll have to try on Batman's leotards."
                dreamgirl "Don't fall in love before your time, sir."
                "The split personality has spoken."
                th "Until when, you blabbermouth? We're leaving tomorrow."
                dreamgirl "You know... Falling in love is like catching a cold. It's a matter of a second."
            else:
                me "I'll tell you a silly thing, probably, but I understand it like no one else."
                me "Because I understand the meaning of the word «loneliness» perfectly."
                me "No one deserves that."
                me "Especially if he hasn't done anything wrong."
                show sl sad pioneer with dspr
                sl "No one has done anything wrong, Syomushka."
                sl "Olga Dmitrievna really picked Miku the best roommate: nobody knows how to listen like Lena."
                sl "If she hadn't decided to run off today for some unknown reason..."
                "Slavya shook her chin and smiled slyly:"
                show sl happy pioneer with dspr
            sl "You like her yea?"
            me "Who? Lena?"
            show sl laugh pioneer with dspr
            sl "Miku of course!"
            with flash_red
            me "No I don't! It's just... Not right."
            show sl smile2 pioneer with dspr
            sl "All right, all right. I'm signing you up as a concert assistant."
            sl "Just watch out, I'll be making my rounds of the camp in an hour!"
            sl "If you're not there, I'll write it down."
            me "I will, I will..."
            "After getting up, I headed for the music club."
            $ alt_day6_us_7dl_mi_friends = 2
        "Escape" if counter_us_7dl >= 7:
            me "I heard we need to clean up?"
            "I inquired."
            me "I've got some thinking to do, and it's good over monotonous labor."
            show sl laugh pioneer with dspr
            sl "Honestly, I'm surprised at your choice."
            sl "You don't look like someone who likes to clean."
            me "And who does the?"
            "I'm offended."
            me "You maybe?"
            show sl normal pioneer with dspr
            sl "Yes. Me."
            "Didn't hurt the girl one bit."
            sl "That's all I've been doing all session. Not because they made me do it, but I just like having my house in order."
            me "I see what's wrong with you. Well, where to go, where to sweep?"
            show sl smile pioneer with dspr
            sl "Stay on the square, I'll send Sergei soon with a cart and equipment."
            sl "Just don't run away, okay?"
            me "Sergei... Cybernetics?"
            "Slavya nodded."
            me "Isn't he defending the hardware from some mug now?"
            show sl smile2 pioneer with dspr
            sl "Well. Then I'll come myself. Just don't run away, okay?"
            th "Of course I will!"
            me "What do you take me for?"
            show sl normal pioneer with dspr
            sl "A slacker. Mind you, I'm going on rounds in an hour, if you're not there, I'll mark it that way."
            "Reported the girl, guessing my intentions."
            "And the intentions were simple."
            "To escape."
            "And not just run away, but..."
            "I was uneasy, to be sure."
            "It seemed strange and wild how calm everyone was about missing pioneer girls."
            "That's why Commissar Cattani takes over the investigation."
            show sl serious pioneer with dspr
            "With another suspicious look at me, Slavya turned around and went to the warehouse."
            hide sl with dissolve
            sl "I'll check!"
            "Her voice reached me."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_preps:
    scene bg ext_musclub_day with dissolve
    play ambience ambience_camp_center_day fadein 6
    play music music_7dl["to_the_sunrise"] fadein 3
    "When I approached the clubhouse, there wasn't a sound coming from there."
    "And it was extremely strange — after all, someone was calling and waiting for me to help in all sorts of preparations."
    "Perhaps she is sitting there quietly and alone."
    "All alone."
    "A{w=.05}l{w=.15}o{w=.3}ne."
    "Of course, if we were where I was from, only two things would come to mind."
    "Either the Japanese girl is very busy on a romantic date."
    dreamgirl "Right, in a giant light aquarium, a romantic date - so the whole camp can watch."
    "Or she's leaning over a smartphone screen, cutting off the abyss inside her from the world around her with headphones, and listening to music."
    if alt_day_binder != 1:
        "I checked, though - there's no signal here."
        "The nearest LTE tower covering the local region is still about twenty years away."
        "Although... Even I had a collection of music and videos on my old balalaika."
        "In that case, how is a high-tech Japanese any worse?"
    else:
        "I pulled my smartphone out of my pocket, which I put into fly mode automatically after waking up, and tried to reconnect."
        with fade2
        "With the expected result."
        "With a sigh, I recovered the status quo and put the phone back in my pocket."
    "The children of today are all so self-sufficient."
    "They're not terrified of loneliness or boredom at all - you just need battery power."
    "If Miku had come here with some Asus with a 32-gigabyte card, she wouldn't have been bothered by the silence of those around her, or their unwillingness to give her the slightest bit of attention."
    "But first of all, it's not the 2000s, which means that Miku simply can't have any phone, tablet, or laptop."
    "And second of all..."
    "Somehow it seemed to me that even in my home world, time or however that sounds right, Miku would be a companionable person, appreciative of people and friendship."
    "A sort of Eastern version of Slavya, it seemed to me."
    "Only with her priorities tilted toward music."
    "Shaking my head, I pushed open the front door, which was unlocked."
    stop music fadeout 3
    play sound sfx_open_door_clubs
    pause(1)
    scene bg int_musclub_day
    with dissolve
    play ambience ambience_music_club_day fadein 3
    play music music_7dl["what_am_i_doing_here"] fadein 1
    "Club was empty."
    th "Where could she have gone?"
    "I couldn't see an active Japanese girl anywhere."
    "I looked around the room."
    if ('music_club' in list_voyage_7dl):
        "I even looked under the belly of the piano - what if she's sitting there again?"
    "Nowhere."
    "Silence."
    "I listened."
    "I heard a barely audible squeak somewhere along with a giggle."
    if counter_mi_7dl == 2:
        me "That's what I thought!"
        "Miku climbed into the prop room again and pretended to be Godzilla."
        "Or a page-boy."
        "Or Freddy the Fastbear maybe."
        "Miku is like war: never changes."
        "As I crept to the door, I listened."
        "Quiet laughter did indeed come from here."
        "The door must have done a pretty good job of soundproofing, despite its flimsy appearance."
        "I pushed the door open..."
    else:
        th "What the..."
        "I looked around more closely."
        "For some reason I thought this room occupied the entire music club space, but now, on second thought, I realized that it was too small."
        th "There must be another room in here!"
        th "Or a nook."
        "Miku obviously had to store props for performances somewhere, and the stage was totally unsuitable for that purpose-no matter how well-built it is, there are items that can't tolerate moisture, cold..."
        "So I set out in search of a stash!"
        with fade
        "Well, like, a hiding place..."
        "The door wasn't much of a hiding place, really."
        "It was just inconspicuous, painted the same color as the walls, and located in the far corner."
    play sound sfx_open_door_2
    pause(1)
    scene
    $ renpy.show("bg int_wardrobe_7dl", what = Desat("bg int_wardrobe_7dl"))
    with flash
    $ persistent.sprite_time = "night"
    "And blinded for a moment by the contrast between the brightly lit music hall and the darkness of the den."
    "The only source of illumination was a light bulb hanging from the ceiling."
    "And that's all I could see."
    "For one moment I was still standing there, looking closely, and the next moment..."
    "Some kind of monster rushed at me!"
    play sound sfx_scary_sting
    with flash2_red
    mi "Got you!"
    "I jerked with a shriek, took a step back, got tangled in my legs, and..."
    play sound sfx_bodyfall_1
    with vpunch
    show blinking
    "I thought only a moment had passed, but when I came to my senses, I found myself lying on the floor, with the very monster that had frightened me jumping and wailing over me."
    if counter_mi_7dl == 2:
        th "It's not the first time I've seen it, time to get used to it..."
    "Now all the imperfections of her camouflage were visible - and the thin voice, and the white shirt, out of place on the behemoth."
    "And the long hair whipping around her legs."
    "And..."
    "Against my will, I traced my legs upward, then, realizing where I was looking, flinched and turned away."
    mi "Senya! What are you doing, get up, come on!"
    "The monster kept harassing me."
    me "Ahem... Miku, would you mind taking that horror off?"
    mi "What's wrong with it? I think it's a wonderful mask! Or rather, even a whole head, only - phhh! - It's a bit dusty, and-"
    "That's when she got up."
    mi "Why are you lying on the floor, come on, get up!"
    "She bent down to me, reached out her hand and helped me up."
    "She laughed her unearthly - sunny! - laughter and pulled the papier-mâché mask off her head."
    show mi smile pioneer with dissolve
    "Underneath the mask was Miku: covered in dust, some hair, her cheeks all messed up, her eyes burning..."
    mi "Well, how was it?"
    "She looked extremely pleased with herself, smiling and glowing with happiness."
    "For which some people, it turns out, need so little."
    "Just to frighten one's neighbor."
    me "Fear and hunger."
    "Honestly I confessed."
    show mi laugh pioneer with dspr
    mi "Well, I'm sorry. I didn't think you'd react that way! And you're here to help me, aren't you?"
    me "I thought you could really use the company."
    show mi happy pioneer with dspr
    mi "And you decided to make it up to me? It's so cuuuute!"
    "She said something else, too, and I was silent, listening to her voice."
    "It came to me with great delay how beautiful her voice was."
    "I wanted to smile, to laugh, to put my fingers out in front of me with a dapper viewfinder, to chill in my chest and respond with an obedient «captured»!"
    "So that she, covering her eyes, folding her palms against my cheek, would remain forever in my memory, eternally young, real."
    "That one day the subconscious, going through the storerooms, would be generous enough to bring her back to me."
    "And for sure the sky touches the ocean, and the quiet whisper of the waves tells of how good it's been here for the last billion years."
    "How we, too, are to return one day, to realize that all our torment and worry have no meaning in the face of eternity."
    "We'll take each other's hands, dissolve into the endless surf, and whisper stories, too, of how two lonelinesses once met in the same camp."
    stop music fadeout 5
    show mi normal pioneer with dspr
    play music music_7dl["what_am_i_doing_here"] fadein 3
    mi "What?"
    me "What?"
    mi "You're looking at me so strangely, Senya. Did I get that dirty?"
    me "To tell you the truth, yes."
    "Critically examining her, I nodded."
    me "But that's not what I really wanted to say."
    th "As if I ever can say what I really wanted to say."
    me "And here you are with your mask... I've lost all thought."
    show mi smile pioneer with dspr
    mi "What a horror! You've lost your thoughts! Get them together and tell me right away! I'm burning with curiosity!"
    "I exhaled and tried to choose my words as carefully as possible:"
    me "Have you really been here all shift?"
    show mi normal pioneer with dspr
    mi "Well... Yes! It's fun here! I love music, I love the stage! And there are so many costumes here, you can change into new ones every day and act out skits! You know, I used to do Kabuki skits about peace, war and winter."
    mi "And I'm not bored at all!"
    "It flowed from one pose to the next - imperceptibly so, in one smooth movement."
    mi "I like shosagoto most, it suits me so well! You don't have to sing, just recite the lyrics, and..."
    "She did some half-ballet pas, wrapped herself around her axis."
    hide mi with dissolve
    play sound sfx_alisa_falls
    "Just then she tripped (and this is Miku, born on stage!), started to fall, and I barely had time to pick her up."
    "She turned out to be light, almost weightless - perfect to carry in your arms and not feel the weight at all."
    "I exaggeratedly set her down gently on the ground."
    show mi shy pioneer close with dissolve
    mi "One-One."
    "She babbled, coming very close."
    mi "I saved you, and you saved me."
    me "And if I hadn't been here?"
    show mi upset pioneer close with dspr
    mi "Don't you dare feel sorry for me! I'm fine, I'm fun, and I'm not bored one bit!"
    me "And not lonely either."
    "I nodded."
    mi "Don't take..."
    "I, obeying some inner impulse, put my arms around the girl and held her close to me."
    show mi surprise pioneer close with dspr
    me "Now you won't be lonely anymore. I promise."
    "With one lip I said."
    "Miku was sniffling and crawling somewhere on my chest, and I was smiling at how everything was just right now."
    th "Yes, you're a strong, confident, almost established artist."
    th "You get so mad when someone sees your weaknesses and dares to pity you."
    th "But all it takes is for your only companion to disappear, and there you are."
    th "Lonely Miku. Sounds like the title for a vulgar vaudeville."
    mi "Let me go."
    show mi shy pioneer close with dspr
    "Embarrassed, the Japanese girl asked."
    mi "I can already stand."
    me "Yes."
    "Barely getting rid of the smile that had climbed onto my lips, I let her go and took a half step back."
    me "You can. But it's better not to let you out in public."
    show mi dontlike pioneer close with dspr
    mi "Why?!"
    me "Have you seen yourself?"
    hide mi with dissolve
    "Miku instantly bounced to the truffle stand against the far wall and clutched her head as she gazed into her reflection."
    mi "Yes. It's better not to be out in public."
    mi "Wait here, I be right back!"
    play sound sfx_open_door_strong
    "The door rattled, and I was alone."
    "Again, with a goofy smile that came out of nowhere."
    "The mood was great."
    stop music fadeout 3
    play sound sfx_open_door_clubs
    pause(1)
    scene bg int_musclub_day with dissolve
    play music music_7dl["tellyourworld"] fadein 3
    "When I opened the door, I stepped out into a better lighted area."
    "You never know..."
    if counter_mi_7dl == 2:
        "I've had enough of the last time the squad leader caught us here!"
    else:
        "If the leader sees us here together, she could think about anything."
    th "Though she swore she was so busy today, so busy..."
    "My experience with the pedagogical staff of various camps suggested that if you just get a little privacy with a pretty pioneer girl, the leaders will instantly run out of things to do, and they will come running, tail between their legs."
    "No, I wasn't planning on getting a private session with Miku, of course..."
    dreamgirl "Okay, that last one wasn't clear. Do you mind?"
    th "Of course not! But we're not even dating."
    dreamgirl "That's the problem. You know, in nature, they don't even ask each other's names. Or registration."
    th "That's nature. Human supposed to be smarter than that!"
    dreamgirl "You're just a dull bore. And you're the one who should have been doing Lena's part today, not Miku."
    dreamgirl "Because you're the dullest thing in the whole world."
    "After nailing me with a verb and giving me one last picture of an obscene gesture, my subconscious calmed down: a Japanese girl was just entering the room."
    $ persistent.sprite_time = "sunset"
    show mi normal pioneer with dissolve
    "She had already cleaned herself up completely and looked nothing like the slob from the closet."
    me "Hello, Cinderella."
    "I smiled."
    mi "Cinderella? Ah! That's from fairy tales."
    mi "By the way, I made such a song for the concert!"
    me "A good one?"
    mi "Very good!"
    mi "Do you want to hear it?"
    me "Go ahead."
    "Miku went to the tape recorder and after looking there, she put the tape on."
    play music music_7dl["shib_stereo"] fadein 3
    "Nothing happened for a while, apparently going blank, and then there was music, which in no way could belong to this world or time."
    "And a voice..."
    hide mi with dissolve
    "I mean, I suspected Miku could sing before, but not like this!"
    "If we were on the stage, I'd think she was singing through a reverb, and not just with videotape."
    "But here, now she was standing next to me, I could hear her breathing, see her dancing."
    "And again I didn't understand: how, well, how did such a talent manage to be shoved into a far dark corner where all she could entertain herself with was dusty props?"
    "Miku sang and looked at me, smiling, pleased with her unwitting spectator."
    "Spun on the spot in a dance and winked."
    "And I felt like I was at a superstar concert."
    th "Best sits in a house."
    stop music fadeout 10
    "Little by little, the music began to fade, and the girl stopped next to it."
    show mi happy pioneer with dspr
    "Her breathing was light and unruffled, as if she hadn't just danced."
    play music music_7dl["what_am_i_doing_here"] fadein 3
    mi "Rehearsed for half a day yesterday!"
    me "Great."
    "I honestly admitted."
    me "Is that the song you're performing tonight?"
    show mi normal pioneer with dspr
    mi "And not just this one! I've got three songs ready for the concert!"
    show mi sad pioneer with dspr
    mi "True, Olga Dmitrievna-san probably won't let me perform that much."
    mi "She says that after my performances no one wants to go on stage - they compare. And I'm here not for comparison, creativity should bring pleasure."
    me "You know."
    "I reported."
    me "If I was preparing a performance and someone like you was performing in front of me, I'd think three times whether I should go on stage."
    show mi laugh pioneer with dspr
    mi "Chatterbox!"
    "Miku brushed it off."
    mi "Actually, redundancy is needed in case someone suddenly can't make the stage, you know?"
    "She bit her lip."
    show mi upset pioneer with dspr
    mi "Gets sick. Or will be embarrassed."
    mi "That's where I come to the rescue with my songs."
    me "Yeah, it's a total mess, of course. But I didn't come here for nothing."
    show mi smile pioneer with dspr
    mi "What, not even to chat with me?"
    me "That, too. But the most important thing right now is to get ready for the concert."
    me "So if you need to carry round things, roll square things, come to me."
    show mi happy pioneer with dspr
    mi "Helper, helper! Hooray! I have my own adjutant."
    "Stretching into a frunt, she commanded:"
    mi "Adjutant! Listen to my first command...!"
    "I snorted."
    th "Looks like it's going to be another morning..."
    mi "Senya, don't boo! You're the one who came and offered your help."
    show mi grin pioneer close with move
    "She came closer to me and fixed my tie."
    mi "No turning back! Now to the cyberneticists! For the cords and the remote control."
    stop music fadeout 3
    scene bg ext_musclub_day with fade2
    show mi smile pioneer with dspr
    play ambience ambience_camp_center_day fadein 3
    play music music_list["everyday_theme"] fadein 1
    "After closing the door behind her, Miku looked at me for a while and smiled."
    "Just a few seconds, but it surprised and confused me, too."
    me "Hey, hello garage! Moscow on the phone!"
    "I waved my hand in front of her face."
    me "Don't sleep, you'll freeze!"
    show mi laugh pioneer with dspr
    mi "Oh, I was daydreaming!"
    "Miku chirped, shuddering and coming to her senses."
    me "Daydreaming about what?"
    show mi shy pioneer with dspr
    mi "Secret!"
    me "Of course."
    "I sighed."
    with fade2
    pause(2)
    scene bg ext_clubs_day with dissolve
    "The club was wide open, with a padlock hanging from the banister, so no one interrupted our entrance."
    scene bg int_clubs_male_day with dissolve
    play ambience ambience_clubs_inside_day fadein 1
    "And the scene that opened up to us completely answered the question of all the weirdness!"
    if alt_day3_technoquest2:
        show el normal pioneer at cright
        show sh normal pioneer at fright
        with dissolve
        "Shurik and Electronik were huddled in the corner behind the table, soldering and twisting something."
    else:
        show el normal pioneer at zenterright with dissolve
        "Electronik sat proudly alone, blocking the aisle with his feet, pretending with all his might to be extremely busy reading some book."
    "Meanwhile, there was clearly a riot on the ship."
    "First of all, the cybernetic diocese was occupied by the youngsters of squad four or five."
    "They were led by some kind of squad leader: apparently that was the reason the little ones still hadn't been asked to leave."
    "Secondly, a good half of the aisle was barricaded and blocked off by some kind of junk, clearly designed to protect what was most sacred from the little ones encroachment."
    "So on the left there was a whispered explanation of how to spread one's fingers and thread a shuttle between them in order to bind the thread as nicely as possible..."
    "And on the right there was a tense and highly disapproving silence."
    show mi smile pioneer at zenterleft with dissolve
    if alt_day3_technoquest2:
        mi "Oh, boys. Why are you all decked out like you're in a war?"
        "Zero attention, pound of contempt."
        mi "Hello?"
        "Shurik only pulled his head into his shoulders."
        mi "Shurik, El, stay awake!"
        "Like talking to a wall."
        "The kids on the left hand whispered and giggled."
        "The leader didn't seem to care at all about my torment."
        me "Looks like I'll have to go rock climbing."
        "I sighed as I looked at the future Mont Blanc."
        me "As they say, if the mountain won't go to Mohammed..."
        with fade
        "The first chair still more or less held my weight."
        "But the second chair, which had been placed on it, was already down."
        th "Why don't people fly like birds?"
        "I sighed bitterly."
        "And then I discovered that..."
        "There's no third chair under my foot!"
        "I put my foot on the void with all my might, I stumbled..."
        scene bg int_clubs_male_day:
            zoom 1.0 xalign 0.5 yalign 0.45
            linear 0.3 zoom 1.3 xalign 0.5 yalign 0.15
        "And with all my might, he slammed my face against the table."
        show blink
        play sound sfx_bodyfall_1
        "I roared and forced the remnants of the barrier with anger as a power source."
        scene bg int_clubs_male_day
        show sh scared pioneer
        with dissolve
        "I couldn't control myself very well at that moment; I think someone was yelling something from behind, Electronik was trying to pull us apart, but he wasn't very good at it."
        "I gave Shurik a couple of whacks in the neck, though."
        "Let's do it."
        "And then I heard an extremely suspicious creaking sound behind me, which I had recently (for about fifteen seconds) associated with pain and a broken nose."
        hide sh with dissolve
        "This time the entire male population of the club reacted, rushing to catch our beautiful starlet."
        "Lucky me, of course."
        show mi angry pioneer at zenterleft with dissolve
        mi "Shurik, Senya! Stop it at once."
        "Angrily demanded the Japanese girl, not even trying to get off my arms."
        "As a matter of fact, there was nowhere to put her - everything was blocked off."
        me "Next time he won't ignore his comrades."
        "Shurik stubbornly looked past me, so Electronik joined the conversation:"
    else:
        mi "Sergei, why did you blocked everything?"
    show el sad pioneer at right with dissolve
    el "Well, you see, the camp leader ordered us to squeeze in a little bit."
    el "And to them."
    "He waved his hand in the direction of the little ones listening to us."
    el "No faith. They're bound to either pull something down or drop something."
    el "Defending here."
    show mi upset pioneer with dspr
    mi "I don't know who came up with this, but stop this mess immediately and clean this place up. It's a real head-scratcher!"
    show el upset pioneer with dspr
    el "I don't think that's a good idea."
    "The blond guy got nervous."
    el "We've tried it once before and everything..."
    me "Shortly, Sklifosovsky."
    "I interrupted him."
    me "We didn't come here to get into the intricacies of parenting. We're here for the equipment. That's all."
    show el laugh pioneer with dspr
    el "Why didn't you say so in the first place!"
    "The cyberneticist laughed in relief."
    el "Here I'll..."
    "He jumped up on the table, ran across it and rushed to the inconspicuous far door."
    hide el with easeoutright
    play sound sfx_unlock_medpunkt_door
    pause(1)
    el "Please!"
    "He invited, unlocking the lock."
    "After a quick glance at Miku, we struggled our way through the barricade and approached him."
    show el normal pioneer behind mi with dissolve
    el "All the equipment is stored here, there's nothing else anywhere else."
    el "What exactly do you need?"
    show mi smile pioneer at zenterright with dissolve
    mi "We'll figure it out, Sergei."
    "Miku smiled, letting him know that we'll take it from here."
    "El nodded indifferently."
    play sound sfx_close_door_clubs_nextroom
    scene bg int_clubs_male2_night
    with dissolve
    "Miku looked around and became sad:"
    show mi upset pioneer at zenterleft with dissolve
    mi "Uncle Borya-sensei has put everything on the top shelves again."
    "She complained."
    mi "It's good for him, he's big."
    me "It's bad to be small, isn't it?"
    show mi angry pioneer with dissolve
    mi "And you don't mock me!"
    me "Okay, okay!"
    "I raised my palms in front of me, admitting my final surrender."
    me "Tell me what to get and out of where?"
    me "I'll get it."
    "I can't help myself."
    me "I'm big."
    "Miku rolled her eyes."
    dreamgirl "You're as smart as the people out there, who stealing wire from cyberneticists in order to make dolls out of it."
    show mi serious pioneer with dspr
    mi "I keep forgetting your stupid Russian humor.(Translator note: Umm, fuck you, miku?)"
    mi "But to the point: I need the boxes with tapes, the shelf next to the stairs, the tape recorder from there, too."
    "I nodded and obediently climbed the stairs."
    hide mi with dissolve
    mi "He left the bag with cords in the closet - oh goodness!"
    "Miku scurried around the room, checking the list."
    dreamgirl "Too bad it wasn't her who climbed the stairs, right?"
    dreamgirl "Sanich obviously put the boxes up high for a reason!"
    dreamgirl "Maybe you should offer her to switch places then?"
    th "How? Tell her, «Hey, baby, do you want to be on top?»"
    dreamgirl "Wow! You're a heartbreaker!"
    th "This ain't no slapstick, you, naughty..."
    dreamgirl "I'm not naughty. I'm an erotic joker."
    th "That too."
    mi "Don't just stand there! Pass me the boxes."
    mi "We'd better get it done before lunch..."
    me "Do you think we'll make it?"
    play sound sfx_7dl["eat_horn"] fadein 1
    mi "No."
    "With discouraging honesty the Japanese girl replied."
    play sound2 sfx_open_door_clubs_2
    show el normal pioneer at zenterleft
    with dissolve
    el "Folks, let's pace ourselves. I don't want to be late for lunch."
    "Electronik tossed the key in his palm."
    "There was no sound from the main room."
    "Looks like the invaders and enslavers rushed to lunch at the first sound of the horn."
    el "I'd leave it all to you to close up, but I'll be charged by Slavya later!"
    "I could see that Slavya frightened him much more than Olga Dmitrievna."
    "So we had to speed up our packing."
    scene bg ext_square_day
    with dissolve
    "We got through in twenty minutes, of which fifteen minutes was spent looking for and putting everything we needed, and five minutes was spent running around the camp all soapy, from the clubs to the stage and back again."
    "Anyway, we weren't nearly late for lunch."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_warehouse:
    play ambience ambience_camp_center_evening fadein 3
    play music music_7dl["old_kiss"] fadein 3
    scene bg ext_warehouse_sunset_7dl with dissolve
    me "It was the last day of vacation, what can I say."
    show sl smile2 pioneer with dissolve
    sl "Don't boo, Semyon."
    "Slavya smiled."
    sl "The two of us can manage quickly. And then - what kind of vacation if you're not working yet?"
    "I turned away arrogantly, letting her know I was ignoring her slander."
    "Actually, I wasn't that sad, to be honest."
    "There was just something inside that demanded a mandatory remark."
    "So that no peeping over my right shoulder would dare accuse me of going to work myself(!) voluntarily(!) when I might as well be stretching my thighs on the beach."
    play sound sfx_unlock_door_campus
    pause(1)
    "Slavya unlocked a huge padlock with her key and waved her hand invitingly:"
    show sl laugh pioneer with dspr
    sl "Welcome to our hut!"
    "I have no choice but to take advantage of her invitation."
    play sound sfx_open_door_strong
    pause(1)
    scene bg int_warehouse_day_7dl with fade
    play ambience ambience_int_cabin_evening fadein 2
    $ persistent.sprite_time = "night"
    "The warehouse was dry, dusty, and subtly smelled of something familiar."
    "I thought for a few seconds before I realized that the smell was the most common wormwood."
    "An odd smell, to me, for a linen warehouse."
    show sl normal pioneer with dissolve
    sl "You like the smell, don't you?"
    "Who knows if I like it or not..."
    "I was kind of indifferent to wormwood - just as long as it wasn't part of an interesting drink."
    show sl smile pioneer with dspr
    sl "Wormwood is wormwood."
    sl "I clean my skin with it."
    me "I didn't think you needed any cleansing."
    "She certainly surprised me here."
    show sl laugh pioneer with dspr
    sl "It's better to think about it beforehand than deal with the consequences later."
    me "I think it's all nonsense. {w}You're pretty enough as it is."
    show sl normal pioneer with dspr
    sl "Careful with the compliments, Syomushka."
    "Slavya wagged her finger at me."
    sl "I can believe it, you know."
    me "As you say."
    show sl shy pioneer with dspr
    sl "I'm glad of course! It's just that I know about your complicated relationship with..."
    "She sighed and forced herself not to continue."
    "And I was interested:"
    me "Well, well, well, who are you talking about?"
    show sl laugh pioneer with dspr
    sl "No! I'm not going to get into who you like and don't like, I'm not going to try."
    me "It's just funny. Turns out I'm in some kind of relationship and I don't know anything about it."
    show sl serious pioneer with dspr
    "Slavya got sad."
    sl "Not a clue."
    sl "It's probably for the best."
    sl "All right, we've got a long way to go, let's start by doing what we came to do."
    hide sl with easeoutleft
    "She stepped back to the far rack and snatched from there two even looking heavy bales marked with a red star with flames."
    th "Not much, didn't lie."
    "Surprised me."
    "And then Slavya went to the closet for the next batch."
    "And also..."
    "When she stopped mocking me and halted, there were already a good dozen bales piling up on the floor at my feet."
    me "And what are they?"
    "Confusedly I clarified."
    show sl surprise pioneer with dspr
    "Wiping the sweat from her forehead, Slavya straightened up and looked at me perplexed."
    sl "Uniforms."
    sl "The shift is ending, we'll have to dress the ones coming in August, too."
    me "And what, half of China will come here?"
    show sl smile pioneer with dspr
    sl "No, of course not."
    sl "We can only accommodate sixty people, there's no room for more."
    sl "But everyone's size is different. And you never know who's going to get dirty or tear anything."
    me "Reserve, huh?"
    show sl normal pioneer with dspr
    sl "Yes. You have to unpack your uniform, iron it, put the strap in the loops on your shorts or skirt, and hang it all on a hanger over here."
    "She pointed to the empty hangers-springs."
    sl "This used to be where the uniforms for guys of this shift wear now used to hang."
    sl "Your too."
    "I nodded."
    me "What will become of it?"
    sl "The usual: we collect it, send it to the laundry, then iron it and put it back in circulation."
    me "You mean someone wore my uniform before me?"
    "I got a palpable twitch."
    show sl smile2 pioneer with dspr
    sl "What's the big deal?"
    me "I don't like to wear other people's clothes."
    sl "You're weird. I've been in a big family all my life, we've been taking things off each other all our lives."
    sl "But since you're so squeamish, I'll make you feel better."
    sl "Your uniform size is so big, you probably got a new set."
    me "That's comforting..."
    sl "I wouldn't dream of it."
    show sl normal pioneer with dspr
    sl "You really are big."
    me "You're not that big."
    "She looked over at me and nodded in agreement."
    sl "Not that big. But we do have kits here for smaller kids."
    me "So what do you want me to do?"
    sl "Take your pick! Will you stand with the iron or hang up the uniforms?"
    "Considering that I prefer a sweater to any other form of clothing, I have a long-standing and mutual love for the iron..."
    me "Nah, I don't know how to iron. Let me fold."
    sl "Then get ready!"
    "Slavya warned, stepping back to the ironing board and turning on the iron."
    sl "Because I'll iron quickly, and I don't want to sit here extra time at all."
    "Here goest the first shirt..."
    stop ambience fadeout 3
    stop music fadeout 3
    scene anim prolog_1
    $ timeskip1 = "Two hours later..."
    show alt_credits timeskip1 at truecenter
    pause(4)
    with dissolve2
    pause(1)
    scene bg int_warehouse_day_7dl with fade
    play ambience ambience_int_cabin_evening fadein 2
    play music music_list["my_daily_life"] fadein 3
    "The monotonous work wasn't exciting at all, and we ran out of topics to talk about pretty quickly."
    "No, I didn't mind talking to a girl like that at all."
    "But she was acting kind of strange, looking at me with either a challenge or a question."
    "There was a kind of aloofness that even a thick-skinned Semyon like me felt perfectly well."
    "After making a few runs at the conversation, I spat and concentrated entirely on my work."
    "So those few hours seemed endless to me."
    "And by the end, my back was aching."
    me "I'm not going to help you anymore. Just so you know."
    show sl laugh pioneer with dissolve
    sl "You won't."
    sl "We're going home tomorrow."
    me "That's little consolation."
    "I grumbled."
    show sl happy pioneer with dspr
    sl "I have better consolation!"
    dreamgirl "A beautiful lady's kiss?"
    "Immediately the inner voice responded."
    "And I even voiced that suggestion."
    show sl shy pioneer with dspr
    "Just for the pleasure of admiring a blushing Slavya."
    sl "Bathing! {w}However, I'll certainly think about your offer."
    me "Think it over, think it over."
    show sl normal pioneer with dspr
    sl "Fine. In that case, go change your clothes and come straight to the beach."
    me "Won't anyone chase us from there?"
    "Slavya glanced at her watch."
    sl "No, I had arranged for thirteen o'clock, that I would go for a swim and bring a couple of pioneers with me."
    me "A couple?"
    sl "Miku."
    sl "She obviously deserves a little entertainment today."
    "I shook my head, roughly guessing who that «entertainment» would be."
    me "See you on the beach."
    stop ambience fadeout 5
    play sound sfx_open_door_strong
    pause(1)
    scene bg ext_warehouse_day_7dl with dissolve
    $ persistent.sprite_time = "day"
    $ day_time()
    play ambience ambience_camp_center_day fadein 3
    "No, I didn't want to become a laughingstock or a figure of amusement for two chattering, laughing girls."
    "It completely contradicted my nature as a sociophobe and an unsociable person."
    "But..."
    dreamgirl "Slavya and Miku in bathing suits, can you imagine!"
    "And it completely reconciled me to possible future bullying."
    stop music fadeout 3
    play music music_list["she_is_kind"] fadein 3
    play ambience ambience_int_cabin_evening fadein 2
    scene bg int_house_of_mt_day with dissolve
    th "Oh, yeah."
    th "And who ever said Monday sucks?"
    dreamgirl "It's Friday, actually."
    th "Shut up, nerd!"
    "Humming, I snapped the cabin door shut behind me, loosened the strap on my shorts and let them run down my legs to the floor."
    "With my butt bare, I danced my way to the nightstand, where on the top shelf my - government property tho - trunks were supposed to be waiting for me."
    dreamgirl "I'm going to throw up..."
    th "You're just jealous."
    "I parried."
    "After wrapping myself around my axis once, I flopped down on the bed and, pulling on my swim trunks, proclaimed:"
    me "I'm in green tights, I'm in nature, and a four-legged pussy won't notice me!"
    dreamgirl "Kill me..."
    me "I don't need a gun, I'm not that kind of guy! I'll kill all the beasts with my beauty!"
    dreamgirl "Maybe you shouldn't go to the beach with the girls."
    "The bifurcation inquired, ingratiatingly."
    dreamgirl "Since you've changed so dramatically. Tights, pussy..."
    th "You don't know anything about beauty."
    th "You're a nerd."
    "Jumping back into my shorts, I tidied up my clothes with excitement like I was going on a date."
    play sound sfx_open_dooor_campus_1
    pause(1)
    play ambience ambience_lake_shore_day fadein 3
    scene bg ext_beach_day with dissolve
    "And with the same sense of impending rendezvous, went ashore."
    with fade
    "To put it shortly, it didn't smell like a date."
    show sl smile swim at zenterleft
    show mi smile swim at zenterright
    with dissolve
    "The girls had just come out of the water, so when they saw me, they came right up."
    sl "You took a long time, Semushka."
    "Slavya smiled."
    mi "Yes! We already had time to take a dip. True, we had to take a line, but that's okay, we took a line for you too."
    me "Okay. Thank you."
    "To think, young, athletic figures, water running down your skin, yeah..."
    if (loki and counter_us_7dl_px >= 1) or (counter_us_7dl_px == 2):
        "And on the left is the fifth squad playing volleyball, and on the right again they are sandbagging Danechka for something."
    "So how do you relax in these conditions?"
    me "How soon will it be our turn?"
    "I inquired, with an effort to squeeze the libido out of my head."
    mi "Twenty minutes total. Come with us, Senechka!"
    "She pointed to two white towels spread out right on top of the sand."
    show mi sad swim with dspr
    mi "There are no loungers, so we'll do it the easy way."
    me "I don't know, it's kind of uncomfortable."
    show sl surprise swim with dspr
    sl "What's uncomfortable? You got the towel, and I sent you to get the trunks."
    sl "Or didn't you find them?"
    me "No, I found them."
    "I mumbled."
    mi "That's it! Spread out, sit down next to me, let's have a chat."
    show sl shy swim with dspr
    sl "Or..."
    "Slavya shot a glance."
    sl "Is our new cavalier shy of his ladies?"
    th "Manipulative bloody woman!"
    "I cursed to myself, but out loud I said neutrally:"
    me "Not at all."
    hide sl
    hide mi
    with fade
    "And, stepping a little further away, I spread out a towel."
    "My back was to the girls, and I thought I'd lie down on my stomach."
    "But just as I was about to sit down on the towel and take up an observation post, Slavya spoiled the whole raspberry."
    sl "Oh, you know, I don't want to just lie there. It's kind of boring."
    sl "Let's go to volleyball?"
    dreamgirl "Also not a bad way to see everything you wanted to see!"
    "So I said yes."
    "Why not?"
    with fade
    "We played two-on-two, classic beach volleyball."
    "Or rather, first we took half the field while the other half played hot potato, then I had to stand alone against two girls at once."
    "It wasn't until the second half that I was strengthened a bit: on my half, Olga Dmitrievna's green-and-black swimsuit shone."
    mt "If we lose, I'll make you clean up after the disco."
    "Charmingly she smiled."
    "And, swinging her hips, she turned to face the net."
    th "How am I supposed to play under these conditions?"
    "I cried out in despair."
    dreamgirl "With pleasure!"
    "A split-sided laugh."
    dreamgirl "With great pleasure!"
    with clock_l
    "This and the next game we lost."
    "The last one went toe-to-toe, can after can..."
    play sound sfx_7dl["eat_horn"] fadein 1
    "It was only the dinner horn that kept us from finding out which of us was the dandy."
    "Too bad."
    "I so wanted a rematch!"
    "Most of the time, though, I didn't see the ball at all."
    "Didn't look at it."
    "There was enough to look at without it."
    "And the girls were winking and doing such poses... Tracer is no match."
    "Long story short, I'm on duty tonight after the disco."
    "Bruh."
    stop sound fadeout 3
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_un_met:
    scene bg ext_square_sunset with dissolve
    play ambience ambience_camp_center_day fadein 3
    play music music_list["waltz_of_doubts"] fadein 5
    "I was worried about a certain debt I've had lately."
    "To whom?"
    "That's another story."
    "So I lied to our activist with a light heart, took advantage of her trust..."
    "And you know what? My conscience didn't bother me at all!"
    if alt_day6_us_7dl_mi_friends:
        "Perhaps it was the bad mood of one Japanese girl who found herself too dependent on other people's doubts."
        "Or it might have been Ulyana's yelling, thinking that one silly act could ruin a budding friendship."
    "Anyway, I sat down on the bench and waited diligently until Slavya finally rolled away on her urgent matters and I would attend to what I considered most important myself."
    scene bg ext_backdoor_sunset_7dl
    with dissolve
    "A couple of minutes and I was at the far gate, the one where they used to drop off groceries and other necessities, rightly believing that a truck didn't belong where the pioneers went in formation."
    th "Everybody seems to be busy with their own personal business."
    play ambience ambience_forest_day fadein 3
    "I summarized, and after another look around to be sure, I scurried out the gate."
    scene bg ext_backroad_day_7dl with dissolve
    "From the very gate to the south led a well-paved track - clearly in demand."
    "But it wasn't quite the way I wanted to go."
    "There was something inside, some sense of direction, or rather instinct, telling me where to step, where to turn."
    "Whispering to me that matters of interest could not be resolved on the thorny road."
    "So I decided, for a change, to listen to it and turned down a barely visible path."
    "Fortunately, the sun had already managed to dry out the woods a little, so I was deprived of the pleasure of getting a shower of cold dew down my scruff."
    "And that was probably the only thing that made me happy."
    scene bg ext_path_day
    with dissolve
    "I couldn't explain to myself why I needed to find this girl."
    if alt_day6_us_7dl_mi_friends:
        "It's not just about Miku's sadness, is it?"
        "Well, it's about her, too."
    "But something told me that the mysterious business of Ulyana, which I «interfere» with, is also directly related to Lena's disappearance."
    th "Perhaps they have their personal hiding place there?"
    dreamgirl "Where they make plans to enslave the universe?"
    dreamgirl "Or not. Where they... By the way, how do you feel about the Yuri genre?"
    th "What genre?"
    dreamgirl "No, no, never mind."
    th "Come on! You're no use at all."
    dreamgirl "Why not? I can also embroider..."
    th "I'm sure you can."
    "In spite of all the foolishness of the subconscious, there was a certain uneasiness in his unsolicited voice."
    "Not some polite, aloof sympathy, but real concern."
    "It was as if this girl mattered to me, and a great one at that."
    if alt_day2_date == 'un':
        "We may not have succeeded the first time, but we can always try again!"
        th "You can, can't you?"
        "The inner voice was skeptically silent."
    th "Do you think we'll find her?"
    th "Or so the fool has gone into the woods."
    if counter_us_7dl_px >= 1:
        dreamgirl "I think after the day before yesterday we could find anyone at all."
        dreamgirl "Or anything."
        th "Did you get a sniff like a sheepdog?"
        dreamgirl "Practically. Go ahead, call out your instincts."
        th "Flair. Call it out. Yes."
        dreamgirl "I mean it. Better yet, imagine a place relative to yourself where Lena absolutely is."
        dreamgirl "Do you feel one cheek warmer than the other?"
        th "No."
        dreamgirl "Idiot. Just keep stomping down that path, okay?"
        dreamgirl "Don't turn anywhere."
    else:
        dreamgirl "The devil knows. It all depends on luck, don't you think?"
        "I didn't know, and I honestly admitted it."
        dreamgirl "How about a little logic?"
        dreamgirl "It's unlikely that Lena went into the deep woods - after all, no one cancelled the wild beasts."
        dreamgirl "So she's gone somewhere relatively civilized, but abandoned."
        th "Which one is that, I wonder?"
        dreamgirl "To an old camp, for instance."
        th "The old camp?"
        "I was involuntarily interested."
        dreamgirl "Yes. You probably don't know much about it, but Sovyonok was originally a couple of miles east."
        dreamgirl "Though on second thought... I don't think she's there.{w} Still, the place is notorious."
        th "Then where else?"
        dreamgirl "Could have gone somewhere on the shore to make a fire there and enjoy the best company - her own."
        dreamgirl "In that case you could be looking for her for a very long time, with no guarantee of results."
        th "Okay, that's understandable. Where else?"
        dreamgirl "A Quarry."
        th "The Quarry?"
        dreamgirl "The Forest of Memory. We're just walking down the path that leads to it."
    "Indeed - not half an hour later, a patch of bottomless blue sky peeked out between the parted pines, and the pine cushion crunched springily beneath my feet."
    scene bg ext_sandpit_day_7dl
    with dissolve
    play ambience ambience_old_camp_outside fadein 3
    if counter_us_7dl_px >= 2:
        "Nothing has changed here in the last twenty-four hours."
        "It suddenly occurred to me that there is no a separate word for «24 hours» in other languages."
        $renpy.notify('Literal translation is «day to night – day away.»')
        "And it's no use trying to translate to some Americans: «день да ночь — сутки прочь»."
        "It made me sad, for that was the saying that popped into my head, as I walked out to the wooden railing, holding back the emptiness from the awkward pioneers."
        th "Empty and lonely."
        "I liked the place, and therefore it might as well have been liked by someone else."
    else:
        "And a few minutes later I came out where I didn't expect to come out at all."
        "A huge sand pit, obviously dug by man, once representing an ulcer on the body of nature."
        "But the years go by, nature heals her wounds."
        "Sooner or later the bare sand will be covered with pine needles again, young pine trees will appear above the surface, the flocked berries will blossom lushly."
        th "In an hour it is just earth, in two there are flowers and grass..."
        "And a few years later, only the rugged terrain will remind you that once there was a huge pit where the pioneers used to jump with wild screeching and barking."
        "Where I once jumped, too."
    "I leaned over the railing and looked up, and in some places the steep slope beneath me was overgrown with moss, and in other places the sand, sand that had hardened to a rocky state, glistened in the sun."
    "I shouldn't even think about going crazy for a second and jumping."
    dreamgirl "Well, you can jump."
    dreamgirl "It's like mushrooms, you know? They're all edible, but some are only for once."
    stop music fadeout 3
    "I grinned, but didn't react to another stiletto."
    "A bird was singing overhead, and for the first time in hours I felt peaceful."
    "It felt like home."
    "In a thoroughly native hermitage."
    play music music_list["silhouette_in_sunset"] fadein 3
    "I ran my palm over the railing, and my hand stung painfully with a splinter."
    "When I yanked my hand away, I saw that the plank itself was by no means smooth."
    "Polished by a thousand touches, yes."
    "But also shredded by a thousand vain hands."
    "A place of memory. A Forest of Memory."
    "At my old camp, such a place was the gazebo-smoking place near the dance floor, where other people's desperate affirmations of being nested by the hundreds on the ceiling, floor, and walls."
    "Here, however, it was somewhat different."
    "Though I could have sworn that even in the camp, in some hard-to-reach places - on the underside of the benches, for example - one's initials could also be spotted."
    "But still, most of the chroniclers were marked here."
    "The splintering «Alyona» was written out carefully and with pressure."
    th "The author clearly wanted to remember this girl as best he could."
    "Next to her you could see an obliquely carved heart, where someone's irrepressible design talent had inscribed a couple of symbols."
    "I walked along the railing and read, delving into someone else's stories."
    "A man is always, for some reason, much more interested in watching, peering into other people's lives than in living his own."
    "We are all voyeurs to one degree or another."
    th "Why else would there be such a frenzy of demand for reality TV?"
    th "I don't really want to force myself to do anything drastic so that one day I can have the legal right to hug someone else's pretty girl by the waist, seriously considering that she's mine now."
    th "But I'd love to watch a show about someone else doing it."
    if alt_day2_date == 'un':
        "I suddenly remembered why I was here."
        "I almost seriously wondered what would have happened if Lena had suddenly become my girlfriend."
        "Or rather, she would have seriously thought she is my girlfriend."
        "After all, she let me know that she wasn't so disgusted with me."
        if loki or (dr and persistent.dv_7dl_tran_un):
            "And that kiss..."
        th "What would happen in such a case?"
        th "What would she... We do?"
        dreamgirl "Japanese love. You know, coldly-choirly in the style of London dandies."
        dreamgirl "Only those spouses are seen at least once a day for breakfast. {w} Sometimes for fife-o-clock."
        dreamgirl "And the Japanese can go weeks without seeing each other."
        th "Japanese..."
    "For a moment I felt I was no longer alone in this clearing."
    "Some gut feeling, a tickle between the neurotic's shoulder blades, giving off a straight look in the back."
    "And just beneath my palm were the letters, blackened by time and moisture, from nowhere:"
    "«Lena»"
    show un serious pioneer at zenterleft
    with dissolve
    me "Found you."
    un "W-what? Was I lost?"
    me "You wasn't?"
    "I was surprised."
    if alt_day6_us_7dl_mi_friends:
        me "No one seen you all day today, and your roommate's been sad this morning."
        "That last one sounded weird, like they were having a marital spat."
    me "I mean..."
    stop music fadeout 3
    show un shy pioneer with dspr
    un "I u-understood."
    un "Yes. I haven't worked as a vest and grateful listener this morning."
    play music music_list["goodbye_home_shores"] fadein 3
    show un normal pioneer close with move
    "She came closer to me, but stood purposely against the sun."
    "Must not have wanted me to look her in the eyes?"
    "Or..."
    "Either way, we ended up too close together."
    "If we were dancing, I'd call that distance a penalty."
    "But otherwise..."
    "It suddenly occurred to me that I was the one paying too much attention to how far we were standing."
    "Lena might as well not have been paying attention."
    th "She might have been."
    un "And y-you know what? I don't regret it one bit."
    me "What about Miku?"
    show un grin pioneer close with dspr
    un "Miku is much stronger than you think."
    "With a tenderness that surprised me, Lena said." 
    un "She spent her whole life pretending and hiding her feelings. {w} Why do you think they put us together?"
    me "I thought it was because you're both creative girls."
    "I mumbled."
    show un sad pioneer close with dspr
    un "No. It's just that we're both good liars."
    "She leaned her hand on the same railing that I was still frantically clinging to."
    "Surprisingly, with this innocent gesture, she shortened the distance even more."
    show un surprise pioneer close with dspr
    "She followed my gaze, owed, and took her hand away."
    if alt_day2_date == 'un' and not herc:
        "She's shy, yeah."
        "Even in spite of those parodies of us dating a few days ago."
        menu:
            "Take Lena by the hand":
                $ alt_day6_us_7dl_un_friends = 2
                "And it suddenly occurred to me again that we could have been..."
                "I don't know how it happened, but I caught her hand on the exhale, and I took a step toward her."
                "In the blink of an eye, here we are standing against each other, and here I am gently embracing her."
                show un cry_smile pioneer close with dspr
                "Lena crumpled for a moment, her eyes sparkling wetly, and she reached for me."
                "Not to my lips, as she should have, no."
                "Somewhere to her chin."
                "It's like we've known each other a hundred years, and we've had it all for a long time."
                "There's our own - only our own! - song.{w} Only our words and jokes that only the two of us understand."
                "Only our rituals."
                play sound sfx_wind_gust
                "I had no time to understand what she wanted to do when the wind that blew through the crowns swept away the obsession."
                show un sad pioneer with dissolve
                "Frustration flashed in the green abyss, and Lena freed herself from my arms in one cohesive motion."
                un "So romantic, eh?"
                "No longer stammering, she shook her head."
                show un serious pioneer with dissolve
                un "Such sunshine, and it's just the two of us."
                un "How's the poor girl can resist?"
                with fade
                un "Why are you doing this?"
                un "We tried it, it didn't work, so I calmed down: that's it, you can stop trembling."
                "Lena didn't take half a step back, she still stood there, alive and trembling."
                me "Do you think I know? I just had a craving, so..."
                "I really couldn't explain to her why I'd spent almost a week doing something I didn't understand, and then, just as I was leaving, I decided to play at romance."
                me "I... I can't explain."
                me "I know I act weird sometimes, but just cut me some slack, okay?"
                "Lena remained silent, and I rushed through my choice of epithets:"
                me "It seemed to me that I was bothering you too much, demanding too much of your attention."
                me "It suddenly became very important to me."
                me "And you didn't seem to say no."
                show un serious pioneer with dspr
                un "It doesn't matter what the girl didn't said."
                "With a sigh, she shook her head."
                "As if I should have said or done something right."
                "But simply didn't get the job done."
                me "It's not as if I had any dirty intentions."
                "I made another attempt to justify myself."
                "I don't think I fixed anything. It only made it worse."
                un "Intentions."
                show un normal pioneer with dspr
                "She's completely changed her pattern of behavior; it's as if I've somehow untied her hands by my action."
                un "You're not going to lie about coming on to me out of great love, are you?"
                me "Whether it was from a great love or not..."
                "I was embarrassed."
                un "Then don't lie to me or to yourself."
                "She interrupted my torment."
                un "Especially since I'm very special to you."
                un "You could join our liar's club."
                if loki:
                    th "And lie to each other outright?"
                    th "Thanks, I've had enough of that in my past life."
                else:
                    me "To the club? Why?"
                dreamgirl "Are you a fool to ask such questions?!"
                dreamgirl "We'd make a threesome! Can you imagine the prospects!"
                stop music fadeout 2
                th "Calm down, sucker."
                play music music_7dl["breath_again"] fadein 3
                "We stood against each other, silently staring into each other's eyes, as if trying to win at least that little."
                "And I kept thinking about how easily I could have fallen in love, could easily have fallen victim to love's addiction."
                "I would only be happy when she came, depressed when the door closed."
                "And «no» from a distance of warmth drove me into a stupor."
                "Would share moments and moods."
                "Would be cheerful when she was cheerful."
                "Would be sad when she was sad."
                "But realizing that such an addiction never leads to happiness and is essentially just a form of depression, would one day slit my wrists in the bathroom."
                "I'd get in with my clothes on, let the water run hot, and ponder until dawn about what I'm worth and why I'm worth..."
                "I could have easily poisoned myself with it."
                show un angry2 pioneer with dspr
                un "Thank you for your honesty."
                un "Otherwise I would have stopped respecting you altogether."
                "I blushed."
                un "Though I'd give a lot to stand like that, with all the right to do so."
                un "But I don't want to. There must at least be something honest left..."
                me "I could die for you, it seems to me."
                "I tried to summon the most honest thing I could in my chest."
                "It burned cold."
                me "But I don't know if I could have lived for you."
                un "I do. I've already been answered that question once... Syomchik."
                if loki:
                    show un smile2 pioneer close with dspr
                    un "And I paid too much for this answer then."
                    "She smiled too diligently, and tried to hide too much by looking away."
                    "There, at the bottom of her pupils, unpleasant events were unfolding, somehow having to do with the strange dialogue we had."
                    un "So I learned to be afraid, Syomchik."
                    "She exhaled the name as if she were repeating after someone."
                    "I expected a reaction-but a different one this time."
                    show un surprise pioneer with dspr
                    "And stared at me in amazement, not waiting."
                    un "Why are you silent?"
                    me "What is there to say?"
                    "How should I know..."
                    me "I've had enough hard lessons in my life, too."
                    me "So I'm not afraid anymore."
                    show un cry_smile pioneer with dspr
                    un "And I do."
                    me "Of what?"
                    un "Of what will happen the same way it did then."
                    un "What are you..."
                    "She exhaled convulsively and shook her head."
                else:
                    me "How do you say it..."
                    un "That's not me."
                    un "That's a completely different person. Who once took from me what belonged to him."
                    un "Gods see, I didn't know it hurt that much."
                    un "Even Slavya couldn't help me then."
                    th "Slavya generally has trouble helping in really critical situations."
                    "It must be downright contraindicated for some to get into a place where only the surgical precision of questioning and helping is possible."
                    me "What happened?"
                un "Nevermind."
                un "It's all in the past now..."
                "Lena suppressed the groan that burst inside her and now smiled as hard as she could."
                show un smile pioneer with dspr
                un "Soon the shift will be over, soon everything will be over."
                me "Soon."
                "I grumbled."
                me "But, you know... I wish there were as few people sad today as possible."
                me "I wish you wouldn't be sad."
                show un shy pioneer with dspr
                "Lena remembered how to be shy again, otherwise, where did that blush on her cheeks came from?"
                me "I don't know your past, I don't know why you're acting like this."
                un "Actually, you..."
                "Lena began, but I interrupted her:"
                me "That's why I can only act at random."
                me "So I want to ask you to dance tonight."
                show un shocked pioneer close with dspr
                un "M-me?"
                me "Yes. But it requires one tiny condition."
                un "W-what's that?"
                me "In order to ask a girl to a slow dance, the presence of that girl is required."
                "I patiently explained."
                me "Got it?"
                show un surprise pioneer with dspr
                un "B-but why?"
                "Lena seems to be completely confused."
                un "Why would you do that?"
                me "It's simple."
                th "Or rather, it's simple right now."
                th "We're not dating yet - and we're not likely to be. That's why I have both my tongue and my hands free."
                me "I like you, and I don't want you to be sad."
                dreamgirl "Wow! Alpha male in the enclosure, everybody pose!"
                th "I need more applause."
                show un shy pioneer with dspr
                un "And what about Ol..."
                me "Who?"
                show un normal pioneer with dspr
                un "Are you sure you want this?"
                me "Of course I'm sure!"
                th "Those are some strange warnings."
                un "Mind you, there's no going back."
                un "Exactly one year ago I promised this world exactly one chance."
                "Stepping back, the girl said."
                th "You are cold, clever, vicious. Your eyes give you away..."
                "And no, I wouldn't want to confess any love, and it wouldn't be too right now."
                "But here and now I wanted more than ever to say to hell with all the rules."
                "To do only as my heart demanded."
                "And so my heart demanded to take one more step towards her."
                "To find her lips with mine."
                if (alt_day2_date == 'un') and (loki or (dr and persistent.dv_7dl_tran_un)):
                    "And be surprised again at how sweet it is to kiss her."
                else:
                    "And marvel at how familiar the taste of a kiss is."
                "That's the right thing to do, isn't it?"
                show un smile pioneer with dspr
                un "I'll be there after dinner, I promise."
                "Lena smiled."
                un "I promise you one dance."
                un "Now I'm going to leave. And don't follow me."
                un "Please."
                hide un with dissolve
                "She nodded to me and disappeared again among the thicket."
                "I did not pursue her, respecting someone else's right to privacy."
                "After all, I needed to understand, too - why I was doing what I was doing."
                "Sitting on the very edge of the slope, with my feet hanging down between the railing posts, I pondered."
                "Covered my eyes."
                "And as I listened to the sound of footsteps fading in the distance, I found myself wishing, for some reason, that evening would come sooner."
                stop music fadeout 3
                stop ambience fadeout 3
                with fade
                return
            "Doesn't matter...":
                pass
    stop music fadeout 9
    me "Anyway, you should have gone back to camp."
    "Is that what I'm going to tell her? That we all miss you?"
    "That would be an obvious lie. It seemed that everyone in the camp didn't seem to give a damn about Lena."
    "Squad leader going to scold? That's just ridiculous."
    play music music_7dl["pixies_playing"] fadein 3
    show un serious pioneer with dissolve
    "Lena recoiled from me. Inexplicably, almost without moving, she shattered all the intimacy of the distance that had been between us a moment before."
    "Like a partisan creeping through the woods carelessly stepped on a dry branch, frightening the night's silence with a deafening crackle."
    un "Why do you want it?"
    "It sounded like an accusation from her lips."
    me "It's not right for a girl to run away from the feast of life to wallow in the woods."
    show un grin pioneer with dspr
    "Lena grinned bitterly. I think I hit something with my words that she'll never tell me about."
    un "Where do you see a feast there? I don't see it, for the life of me."
    hide un with dissolve
    "She swayed on her toes, gripping the railing tightly with her thin fingers."
    un "It looks to me like there's no life there, either."
    me "You're too pessimistic."
    un "Sorry to spoil your mood with my sad face."
    show un cry_smile pioneer with dissolve
    "Lena turned to me with a strange, forced smile. It seemed that a little more and she would explode."
    un "But there are things I can't just leave behind and move on with my life."
    show un rage pioneer with dissolve
    un "I'm pretending to be all right as it is: I can't go around the camp making mischief so that everyone will believe it for sure!"
    "I could have expected anything: tears, hysteria, even a punch in the face."
    hide un with dissolve
    "But the girl, strangely enough, quickly pulled herself together and turned away again."
    if loki:
        me "I'm not saying you have to do that. You put yourself in limits, and you suffer because of it."
        me "You have to take it easy, Lena. And life will get easier."
        dreamgirl "Look, we have a pain expert on our hands!"
        dreamgirl "You tell her that things will get better, that everything will be fine!"
        dreamgirl "That her problems are nothing, less significant than a grain of sand on the scale of the universe."
        dreamgirl "And that she'll laugh about it all when she grows up."
        "I didn't have to voice it, though - Lena managed to interpret my line in the worst possible way herself."
        show un angry pioneer with dissolve
        un "What do I even know about life, huh? I made up my own headache and I'm dealing with it. How silly of me."
        "Her tone was already very frightening."
        me "Don't twist my words. All I meant to say was that you don't have to act like you're okay with everything. You want to be sad, you're welcome to be sad, but you don't have to run off into the woods to do it!"
        "I've got it all wrong. That's not what I meant to say at all!"
        un "I didn't ask you to look for me!"
        "The knuckles of her fingers clutching the wooden railing turned dangerously white."
        show un angry2 pioneer with dspr
        un "Go away. Go away before I want to disprove what you said about how easy my life is and how I make things difficult."
        hide un with dissolve
        "I turned sharply and staggered toward the camp. There was nothing else for me to do: everything I could and could not say, I had already said."
        "I was angry at myself, angry at Lena, angry at this stupid camp. I had nothing but anger right now."
        dreamgirl "You'd make a pretty good retardologist. Clients would need an infinite number of sessions."
        th "Go to hell!"
    else:
        me "What if I want to see the real you?"
        "Or I want you to be the one I was able to see in you."
        show un angry2 pioneer with dissolve
        me "I don't want to make you bounce around camp with Ulyana if you don't want to. But I don't want you to be sad here alone."
        show un evil_smile pioneer with dissolve
        "Lena grinned unkindly."
        un "You have to decide what you want. And what makes you think I have anything to show you?"
        me "I just feel it."
        show un angry2 pioneer far with dissolve
        "I reached out my hand to touch her shoulder reassuringly, but she jerked away like scalded."
        un "And you think you can pry into my life just like that, on some whim of yours?"
        show un normal pioneer far with dissolve
        "Abruptly shutting up, Lena seemed to calm down, but her shoulders were still shaking with rage."
        un "Go away. Just go back to camp, Semyon."
        "My words were powerless. The surest decision was to go to camp before she sent me somewhere else."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_dinner:
    play music music_7dl["afraid_of_destiny"] fadein 2
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 5
    "Upon entering the canteen, I stopped in bewilderment."
    "The dinner was crowded and hellish."
    "It was nauseating to think of wading into all that pomp and clamor."
    "Especially after this morning."
    if alt_day6_us_7dl_mi_friends == 2:
        "Miku sat down next to me without waiting for an invitation."
        show mi smile pioneer at zenterleft with dissolve
        mi "Well, we didn't manage to finish everything."
        "The Japanese girl held up her hands."
        mi "What the boys have set up in there is, of course, utter horror."
        show mi laugh pioneer with dspr
        mi "How could it have occurred to them?"
        "I pretended to smile politely."
        "The psychological issues of the local pioneers bothered me far less than the contents of the plate on the table."
        "So did the Japanese girl, by the way."
        dreamgirl "Look how she's winding it up! It makes my ears pop."
        th "Of course it does. It's a hodgepodge."
        show mi normal pioneer with dspr
        "Sensing my gaze, Miku raised her head and mumbled something indistinctly."
        me "I'm sorry, what?"
        mi "Itadakimasu, I say!"
        me "Ah, thank you. Enjoy your meal, too."
        "I nodded."
        me "What do you think of the national cuisine?"
        mi "Unusual, spicy, greasy, but delicious!"
        "She smiled contentedly:"
        mi "Death to the figure!"
        "Looking at her skinny relics, I thought a plate of hodgepodge certainly wouldn't hurt her."
        "Not out loud, of course."
        me "Once a year you can!"
        "Miku nodded enthusiastically."
        show mi happy pioneer with dspr
        "It seems the way to her heart was through her stomach, too."
        me "After lunch, back to the stage?"
        mi "Yes! There's less and less time, and there's a sound check."
        mi "It starts at four o'clock, and I still have to sing and stretch out."
        show mi upset pioneer with dspr
        "Miku sighed, nearly splashing the contents of her spoon."
        mi "What a mess."
        "She complained."
        mi "Everything, it seems, was done beforehand, so there was time to spare, no?"
        me "It was."
        "I obediently acquiesced."
        mi "Then why are we doing everything again in a hurry and at the last minute?"
        th "Because proper planning also includes being able to tell everyone to piss off at the key moment."
        "From my point of view, Miku didn't have the latter talent at all."
        "I wanted to say what I thought right away, of course, but right now the idea didn't seem reasonable to me at all."
        me "Because that's the mentality."
        show mi surprise pioneer with dspr
        mi "What's wrong with the mentality?"
        me "What, what... The Russian man is a slob by nature."
        mi "And you?"
        me "I am in the first place!"
        "Couldn't help bragging, yes."
        if (alt_day2_date == 'mi') or (counter_mi_7dl == 2):
            mi "Senya, I've known you for days! I would definitely pay attention!"
        else:
            mi "Nonsense, I've been with you since morning! I would have noticed."
        me "It's just the middle arithmetic."
        "I parried."
        me "You are extremely responsible, I am extremely irresponsible."
        me "Together we add up to something of average responsibility."
        show mi smile pioneer with dspr
        mi "Is that so?"
        "Miku stretched."
        mi "What an interesting theory."
        me "Like with opposites, you know? Opposites converge."
        "I continued to sneer."
        mi "Yes. That means that..."
        "She hesitated, then rubbed the air with her palm:"
        show mi normal pioneer with dspr
        mi "It still doesn't make sense. If you put me next to you, it won't make me sing any worse!"
        mi "And less to worry about, too."
        show mi angry pioneer with dspr
        mi "You and your jokes again, eh?"
        "Trying my best to keep a straight face - which was incredibly difficult with the corners of my lips parting in different directions - I shook my head:"
        me "You're failing wrong."
        mi "Wrong... what?"
        "Again the Japanese girl got puzzled."
        "And here I couldn't take it anymore - I laughed out loud."
        "I got hit in the forehead with a spoon, but it was really worth it."
        "Miku pouted and turned her nose up, but she finished her soup and went outside, putting the dirty plates in the sink."
        hide mi with dissolve
        "Shaking my head, I followed her out."
    elif alt_day6_us_7dl_sl_friends == 2:
        "Two creepy, pissy cheaters, who'd had time to sing and play, were now sitting across from me."
        "The two of them."
        th "That's what you get for doing good things."
        "It crossed my mind."
        if alt_day6_us_7dl_mi_friends == 1:
            "It seems that Slavya listened to what I said about the loneliness of certain art directors and decided to eradicate the situation."
        "Miku bloomed and smelled."
        dreamgirl "Did you smell her?"
        th "Well, I mean, like the rose of May."
        show mi happy pioneer at zenterleft
        with dissolve
        th "Happy, ruddy, contented..."
        dreamgirl "Happy."
        th "Yes."
        show sl happy pioneer at zenterright
        dreamgirl "And Slavya is happy too."
        "The subconscious mind continued its Jesuit whisper."
        dreamgirl "Look how the eyes sparkle!"
        with dissolve
        th "Aha... Hey, what are you implying?!"
        dreamgirl "No, no, I'm not implying anything at all."
        dreamgirl "But just so you know, when Miku gets Slavya into the cabin and seduces her there, you'll get that star - your victory."
        dreamgirl "You can safely try on your matchmaker outfit."
        me "Girls? What are your plans for this afternoon?"
        sl "Clean up!"
        mi "Rehearse!"
        "In one voice they shouted."
        show sl laugh pioneer
        show mi laugh pioneer
        with dissolve
        "They looked at each other and laughed."
        show mi normal pioneer with dspr
        mi "Actually, I would have slept a little during quiet time."
        "Miku covered her yawn with her palm."
        mi "I got the set ready, and the match made me a little tired."
        mi "But I have a few hours to get myself cleaned up before the performance."
        show sl smile pioneer with dspr
        sl "And I never run out of work."
        me "Why?"
        show sl normal pioneer with dspr
        sl "Because there's always a place to clean up, a place to put things in order."
        sl "But I'll definitely come to the concert, don't you doubt it!"
        th "Of course you will."
        th "The head paragon and champion of camp rules missing the event? No, no, don't even think about it."
        show sl smile2 pioneer with dspr
        sl "And you, Semushka, where are you going?"
        "Slavya pursed her lips, just a polite question."
        "But I saw something gleam in her eyes."
        "It was as if I had been presented with a choice: to comfort an already cleaned up and warmed Miku or to help an Atlantean hold the sky."
        "My help was not really required by either of them."
        "And only my heart could serve as my only counselor."
        dreamgirl "And also the adrenal glands!"
        "So it is. If I had spent a little more time with any of them, I could now choose based solely on my desire to be closer to my passionate."
        "And for better or for worse, none of them could boast of such a title."
        "The title of Semyon's Passion."
        "I shook my head indefinitely."
        me "Who knows. I'll walk around camp, I guess."
        me "But it's quiet time now... I'm going to sleep, that's it."
        show sl sad pioneer
        show mi sad pioneer
        with dissolve
        "And the girls looked at me with the same disappointed expression."
        if loki:
            "Fortunately, I stopped caring about girls' opinions on any of these issues about ten years ago."
        else:
            "I blushed a little, embarrassed."
            me "S-Schedule."
            "Ulyana giggled stupidly behind me, and I shut up."
        dreamgirl "The hopes of the young nourish the young, the refreshment of the old."
        dreamgirl "They were counting on you, Syom Syomych. How could you let their expectations down?"
        th "I know how! With great pleasure."
        dreamgirl "Ay, well done! Give me five!"
        "The inner voice approved of me."
        me "Excuse me, I have to go to my quiet time."
        hide sl
        hide mi
        with dissolve
        "Nodding goodbye to each of the hushed girls, I rose, gathered my plates, and departed."
        "Where I was going and why I was going was classified information."
        "They weren't supposed to know."
    else:
        "Ulyanka was sitting by the window, and I, hesitating, headed toward her."
        me "May I?"
        "Squinting at me, the little one reluctantly nodded."
        show us normal pioneer
        with dissolve
        us "As you wish."
        "Indifferently she dropped."
        "I wanted to sit next to her."
        "That's what I did."
        "I had a whole bunch of questions."
        "And the most important one in particular was:"
        "What did that scene in the canteen after breakfast mean?"
        show us smile pioneer with dspr
        us "Are you going to keep staring at me?"
        us "I feel like I'm under interrogation."
        me "For a D and a broken glass?"
        show us normal pioneer with dspr
        us "For a B and dirty tights."
        "She cut it off."
        me "A B? A normal grade, what's wrong with it?"
        us "That's not what my grandfather and father think."
        show us shy pioneer with dspr
        "Ulyana reported and, embarrassed, hid herself in a bowl of soup."
        "I guess she wasn't going to give me such details about herself."
        "Well, that's right, we're not that close."
        "We're already... too close."
        "Too close for our age difference."
        me "And what do you think?"
        show us smile pioneer with dspr
        us "I think I have to study for two years, and then it's over."
        me "What about university?"
        us "There I'll live in a dorm, and no one will interrogate me every night."
        show us calml pioneer with dspr
        us "Actually, I don't want to talk about it anymore."
        us "Don't you have anything else to talk about? It's summer!"
        me "Summer..."
        "I sighed, trying in vain to squeeze out a topic for the next conversation."
        "Thoughts flashed fruitlessly through my head, but they all mostly concerned only questions like «what are you doing» and «what are you planning to do»."
        "And Ulyana clearly demonstrated her aversion to platitudes."
        me "And I found Lena."
        "I said it just to say something."
        show us surp1 pioneer with dspr
        us "Tishu? How did you manage?!"
        me "I managed, as you can see."
        "A little confused I replied."
        us "Even I can't find Tisha if she's hiding."
        me "Why, have you tried looking yet?"
        show us smile pioneer with dspr
        us "She already ran away like that last year."
        us "So I went looking for her."
        me "And?"
        "I encouraged."
        show us sad pioneer with dspr
        us "Nothing. Didn't find her!"
        "The girl confessed."
        us "And I - by the way - I looked all over the camp and everything around it!"
        us "I looked very well!"
        show us normal pioneer with dspr
        me "And how did it end?"
        us "With nothing."
        us "She came out by herself, and then some nasty thing happened!"
        me "What nasty thing?"
        us "I don't know! But when we came back from the camp, a policeman came to our house and asked all kinds of silly questions."
        us "Something about the camp, relations between pioneers, about friends. Some nonsense. He didn't explained anything."
        show us dontlike pioneer with dspr
        us "All I know is that something happened in their town, and that's what started it all."
        me "Maybe Lena's father? I hear he's police officer."
        show us normal pioneer with dspr
        us "Are you stupid or what?"
        us "Her father's a colonel, don't you think I can recognize his shoulder straps?"
        me "I have no idea."
        dreamgirl "Colonel, that's nothing. Let him catch us first!"
        me "Personally, I don't know anything about such things at all."
        us "Yea-ah?"
        show us smile pioneer with dspr
        "The girl looked at me suspiciously."
        us "And I thought you, an ambassador's son, were supposed to know that."
        me "As if I have nothing else to do."
        me "To be shoulder strap expert."
        show us laugh pioneer with dspr
        us "Yeah, yeah, yeah! One more year to go and you'll be under the shoulder straps yourself."
        "The girl laughed, and that made me even more upset."
        us "Serve well, and I'll be friends with you!"
        me "Thank you. All my life I've dreamed of it."
        show us surp2 pioneer with dspr
        us "You don't want to?"
        me "Be friends with you?"
        us "Yes!"
        me "Weird. I thought we already..."
        show us laugh pioneer with dspr
        us "Huh! You have to deserve it first."
        hide us with moveoutright
        "With another smirk, she jumped up and ran away."
        "I'd like to point out, leaving all her dirty plates on me!"
        "You little creep."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_soundcheck:
    scene bg ext_square_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    play music music_7dl["breath_me"] fadein 3
    if alt_day6_us_7dl_sl_friends == 2:
        "Very classified, yes."
        "I headed for the stage!"
    "Just to be clear, I wasn't the least bit thrilled that I was going to be under the intense cross-attention of a bunch of people for an hour."
    if alt_day6_us_7dl_mi_friends == 2:
        "Although I must admit that the morning I spent with Miku couldn't be called dull and ordinary."
        "No way."
        "Certainly I assumed we'd be singing and dancing in the club, I'd be yawning and scraping away stalactites of gum under the reclining seats."
        "And maybe I'd be dumbing down my phone, too - if it weren't for the miserable percentage of charge left there."
        "But no. We were scaring each other, hugging each other..."
        if alt_day3_technoquest2:
            extend " and then saved each other from an avalanche of chairs in the cybernetics closet."
        "It was fun, all in all."
        "So I went to the sound check without much enthusiasm, but with high expectations."
    elif alt_day6_us_7dl_sl_friends == 2:
        "The other thing is the beach."
        "That's where it was great!"
        "I may have lost a volleyball game, but I had two consolations!"
        "In blue and and blue-green swimsuits."
        "I don't get any of that on the stage."
        th "Skip the soundcheck... Maybe?"
        "I almost seriously considered it."
        "And then I felt someone's eyes on my shoulder blades."
        "Olga Dmitrievna."
        "She stood there smiling kindly, Bolshevik-style."
        th "Brrrr."
    scene bg ext_stage_big_clear_day_7dl
    with dissolve
    play ambience ambience_medium_crowd_outdoors fadein 3
    "From a distance you could hear the eerie cacophony coming from the stage."
    "Before they turned on the equipment that spread the sound almost all over the camp, everyone was in a hurry to tune their instruments and check the sound."
    "No, there were coordinated teams, too."
    "But when «Hotel California» comes from one side of the stage and «we wish you happiness» from the other, the timing is still a bit off."
    "Miku was also jumping and humming something to her ear."
    scene bg ext_stage_near_clear_7dl
    with fade
    show mi smile pioneer far at fleft with dissolve
    "Then she suddenly stopped when she saw me."
    if alt_day6_us_7dl_sl_friends == 2:
        show mi grin pioneer far with dspr
        mi "Off to bed, are you?"
        me "Uh-huh."
        mi "Okay!"
    mi "Senya, turn on the remote, please. Just on a quarter volume for now."
    me "And it turns with...?"
    "I clarified."
    mi "The white button on the side. But first signal down, channels four, six and seven."
    "I nodded and, having done as required, clicked the power button."
    "The speakers barely audibly hummed."
    "It didn't make much of a difference, though."
    "Voices were heard on all sides, talking at random, each about something different."
    "I got a headache after a few minutes of torture with that noise."
    "Unfortunately, Miku seemed to feel quite confident and well here."
    "She still hasn't changed - nothing surprising, really."
    "But she was holding a binder with a pile of papers and some incomprehensible thing subtly resembling a tambourine."
    th "Like a fish in water, uh-huh."
    mi "Senya, ah Senya!"
    me "Yes?"
    mi "There's a tape recorder next to you, turn it on! Now let's see how I sound."
    stop music fadeout 3
    "With an obedient nod, I complied this task as well."
    "I think I'm going to be here a while."
    "The Japanese gril scurried around the stage, making room for «breathing», as she put it."
    "Waved a tambourine-like thing in the air, slammed it on the folder, and nodded contentedly."
    $ volume(0.3, "sound")
    play music music_list["miku_song_voice"] fadein 3
    "And freeing up a tiny spot right between the speakers, where the most tangible stereo is, she stood, clutching the microphone, and, waiting for the intro to end, began to sing."
    hide mi with dissolve
    with fade
    "No, it wasn't a song in the literal sense of the word."
    "Rather, I would call it a kind of singing exercise, or whatever professional vocalists call it."
    "There's a lot of «nya» and «pa» that don't make any sense at all."
    "The people around me looked at the Japanese girl strangely, but they seemed to be used to her eccentricity."
    "Or did they put it down to the fact that she was a foreigner after all?"
    "Anyway, it didn't embarrass Miku herself: tilting her head now and then to the left and to the right in a sort of parody of dancing, she kept shouting her «nya» and smiling frantically."
    "It was quite obvious that this was something she sorely missed."
    "The stage, the performances, the attention... Yes, the attention was probably the most important thing."
    stop music fadeout 3
    show mi dontlike pioneer far at fleft with dissolve
    "When she finished warming up, she shook her head and looked at me unhappily."
    $ volume(1.0, "sound")
    play music music_list["everyday_theme"] fadein 3
    mi "Senya, I told you to turn down the seventh channel."
    me "What did I do?"
    mi "Not enough! You're skewed, the upper speakers are yelling louder than the lower speakers. Level it out."
    "She started humming something again while I equalized the sound balance."
    show mi smile pioneer far with dspr
    mi "That's better."
    "She praised."
    show mi upset pioneer far with dspr
    mi "But now you can hear that the left side sounds louder than the right."
    th "Rrrrr..."
    show mi normal pioneer far with dspr
    mi "Align the balance, please."
    mi "A little more to the right side. {w}That's it, yes."
    "She ignored the camp band that kept making noise the whole time."
    "Or not."
    "Pulling what appeared to be a little kid from third Squad running by out of thin air, she handed him one piece of paper from her folder."
    mi "Put it on the floor under the speaker, got it?"
    mi "So you can read it as you walk by."
    "The kid obediently nodded and, clutching the paper, headed for the edge of the stage."
    show mi smile pioneer far with dspr
    mi "They're bound to forget something."
    "A Japanese girl smiled at me."
    show mi smile pioneer at cleft with move
    "She jumped off the stage and ran up to me."
    mi "Thanks for your help, Senya."
    "She gave me a happy smile."
    mi "You know how hard it is to tune the sound alone! Always having to run back and forth, back and forth... Hey!"
    show mi angry pioneer with dspr
    "The girl suddenly barked somewhere in the direction of the stage."
    mi "Dan, look at me!"
    show dn upset pioneer at fright with dissolve
    if (loki and counter_us_7dl_px >= 1) or (counter_us_7dl_px == 2):
        "I don't know why Danechka, who was here, sighed, winking slyly at me with his left eye."
    else:
        "The curly-haired pioneer, who she called «Dan», reluctantly nodded."
    with fade
    show mi angry pioneer with dspr
    mi "That's not how you sing and herd off the stage, that's not how you do it!"
    mi "If people clap, you have to stop and bow, are you an artist or where?"
    me "The best pearls of the Russian language..."
    hide dn with dissolve
    show el sad pioneer at fright with dissolve
    "After waving me off, Miku went on to reprimand the artists."
    mi "And you, Sergei, you're good too! {w}You have to make sure that I adjust the microphone to your thing!"
    mi "So, finished - look at me, I'll nod."
    mi "You're not counting crows, you're looking at me."
    "Electronik nodded with a martyr's look."
    "From the look on his face, he's already regretted getting involved in this venture a hundred times."
    "But, unfortunately, it's too late to play it back."
    hide el with dissolve
    show mi normal pioneer with dissolve
    mi "Wonderful!"
    mi "In the line now please."
    "The hubbub didn't die down, though some reached for the stairs."
    show mi upset pioneer with dspr
    "The girl's face darkened, she bit her lip."
    mi "And that's the way it always is."
    mi "They think that since I'm small, they can ignore me."
    mi "Eh. And I have to take care of my ligaments."
    mi "Give me a sec."
    hide mi with dissolve
    "She leaned over me and reached out for the remote control."
    "In fact, she practically laid down on top of me!"
    dreamgirl "Don't waste time, Sir! Catch her, catch her!"
    "She had a wicked smile on her face."
    "Grabbing the microphone off the counter, without looking, she dragged the knob to a position close to maximum and barked:"
    show mi normal pioneer with dissolve
    mi "Squads one to three - march off the stage!"
    mi "Squad four will perform in the order of precedence!"
    "That's the kind of argument the pioneers clearly listened to and hurried to clear the stage."
    stop music fadeout 3
    with fade
    play ambience ambience_camp_center_day fadein 3
    play music music_7dl["what_am_i_doing_here"] fadein 3
    "The conversations were cut short at once, and everyone got in flocks."
    "And quietly-peacefully lined up next to the steps to the stage."
    th "That's what a life-giving swear does!"
    mt "Well, who's yelling?"
    "A squad leaders's voice came out."
    "From behind, as always."
    show mi upset pioneer at left with move
    show mt normal pioneer at zenterright
    mi "Here comes the backup."
    "She whispered unhappily."
    me "Backup, why aren't you happy?"
    mt "It's because, Semyon, I don't let her take up the whole stage and start her long-playing concert again."
    show mi shy pioneer with dspr
    mi "Uh, and it was only once."
    "A Japanese girl protested."
    mi "And no one objected. They weren't, were they?"
    show mt grin pioneer with dspr
    mt "Considering that the concert was for parents, I'm not the least bit surprised."
    me "What happened?"
    "There was a guy onstage with frosty eyes, and my gut told me he was going to yell."
    "Not singing, screaming!"
    "So I turned off his microphones in advance and then turned to the leader."
    "It really was a fertile topic."
    show mt laugh pioneer with dspr
    mt "What a curious young man you have, don't you think?"
    show mi dontlike pioneer with dspr
    mi "He's not mine! He's just helping me on a case, that's all!"
    if counter_mi_7dl == 2:
        show mt grin pioneer with dspr
        mt "Like the last time yeah?"
        "She made me blush again."
        "Miku didn't raise an eyebrow, though."
    if alt_day6_us_7dl_mi_friends == 2:
        mi "And he also sat with me in the morning because Lena wasn't there, and I got lonely and sad."
        show mi shy pioneer with dspr
        mi "Also... oi."
        mi "I'm gibbering, aren't I?"
    th "She's nervous."
    "Came to mind."
    th "Why should she? Semyon's not a bird to be embarrassed for him."
    dreamgirl "Self-criticism is very good. But don't be self-deprecating."
    if (alt_day2_date == 'mi') or (counter_mi_7dl == 2):
        th "I've known her for, like, a week."
    else:
        th "No, what's wrong? We talk to her for a day or two."
    dreamgirl "Some don't even need a day. A couple of seconds is enough."
    show mt smile pioneer with dspr
    mt "I know. I know."
    "The squad leader smiled."
    mt "I just couldn't help it, you two look so touching together."
    with fade
    show mi normal pioneer with dspr
    mt "As for the concert, during the second week of the shift, when it was Parents' Day, our star had somehow decided that the «from the Pioneers to the Parents» concert should actually be considered a Hatsune concert."
    "The leader began her story, flatly ignoring Miku's disgruntled look."
    mt "It was always like this, the kids prepared a performance for the parents, preparing, trying."
    me "And then Miku comes on stage?"
    "The leader nodded."
    mt "Although we don't usually perform as a squad, since the amount of work on the Parents' Day is quite large, here we still scratched some time."
    mt "Even Slavya came to sing something."
    mt "So we came. Performed."
    mt "Miku performed third, passed Slavya ahead of her, as if to warm up, and then climbed out on stage herself."
    show mi shy pioneer with dspr
    mi "It wasn't my fault! I specifically went and asked who rehearsed, if anyone was nervous, and..!"
    mi "It wasn't my fault that half of the performers hadn't even learned their performance yet!"
    me "You had to come out and save the day?"
    "I voiced the obvious solution to the question and got a double nod."
    "True, the mood was somewhat different: full of sneer from the leader and somehow desperate and outspoken from the Japanese girl."
    mi "Exactly! You shouldn't have shown unrehearsed performances, it's embarrassing!"
    show mt normal pioneer with dissolve
    mt "This is how our star «saved» our..."
    "Olga made quotation marks in the air with her fingers."
    mt "...position."
    me "Don't scold her, she really did a good thing."
    show mt laugh pioneer with dspr
    mt "'Ery nice!"
    mt "Especially if you ask her how many performances she took to her Japanese chants."
    "I raised an eyebrow questioningly and shifted my gaze to Miku."
    show mi happy pioneer with dspr
    mi "Eight."
    me "Eight performances?!"
    mi "Yes. It was a great concert, you should've see how they clapped for me!"
    mi "It was a good audience."
    show mi sad pioneer with dspr
    mi "But after that Olga Dmitrievna for some reason forbids me to approach the microphone without supervision."
    me "And I'm - the supervisor?"
    hide mi with dissolve
    show mt smile pioneer with dspr
    "Miku was embarrassed and turned away."
    "Noticing something on the stage, she switched over there and yelled for the third squad to get out and make room for the performances."
    "Something was answered to her, and she took the microphone again with the volume turned up:"
    mi "Second squad to the stage."
    mt "Almost, yea. By the way, thanks for watching her while I was gone."
    "I felt the tips of my ears flare up."
    me "I wasn't supervising."
    me "And I'm not supervising!"
    mt "Of course you're not supervising! You are a friend!"
    dreamgirl "Not a sausage!"
    show mi smile pioneer at left with dissolve
    mi "But I got so much clapping! Like no one else."
    "Olga threw a strange look at Miku:"
    mt "Of course they clapped. After what you did on stage - I'm surprised."
    mt "That you didn't get flowers."
    show mt normal pioneer
    show mi serious pioneer
    with dspr
    "They exchanged dagger stares."
    me "So I don't get it: they couldn't pull her off the stage or something?"
    show mi smile pioneer with dspr
    mi "They didn't want to!"
    mi "When they tried to stop the tape, the back rows would start whistling and demanding me."
    mi "I did and sang! Wasn't I a good girl?"
    show mt smile pioneer with dspr
    mt "Good, good. But you can't be allowed on stage next to amateurs."
    mt "They'll get complexes."
    show mi normal pioneer with dspr
    "After these words, Miku calmed down completely."
    "Staring at the squad leader, in the bridge of her nose, she chided:"
    mi "If they don't want to screw up, they should rehearse."
    hide mi with easeoutleft
    "And, rising, went to the stage."
    "The second squad had finished their performances; it was time for the heavy artillery."
    show mt grin pioneer with dspr
    "The squad leader was not at all impressed by this demarche."
    "She winked at me and settled down on a nearby bench and covered her eyes."
    hide mt with dissolve
    th "Passion boils over here, of course."
    "Something told me this wasn't the first, or even the fifth time, such conversation between the art director and the squad leader happens."
    "And they're not getting into it to change someone's mind or to get them on their side."
    "It's... for fun."
    "Exactly."
    "Miku wasn't embarrassed by what should have been embarrassing, and Olga wasn't annoyed by the girl's insubordination."
    "They certainly bumped heads more than once or twice, defending their interests."
    "But twenty days later they came out of the perpetual debate very warmly relating to each other."
    "Let the loneliness in Miku's eyes shine through - she doesn't blame it on the leader."
    "After all, she has me now."
    "Miku caught my eye and winked."
    if alt_day6_us_7dl_mi_friends == 2:
        "No matter how bad she feels in the morning, these are the moments when you stand with a microphone in your hands..."
        "When the music pours and the song bursts from your chest not with a moan, but with a scream."
        "It's moments like these that redeem everything."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_button:
    play music music_list["i_want_to_play"] fadein 3
    scene bg ext_dining_hall_near_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    "When I came out of the canteen, Ulyana was nowhere to be seen."
    "No wonder - that fidgety girl was up to no good, she had no time for silly things like talking to boring and lazy Semyon."
    "I myself could hardly understand what our communication was all about."
    "Except for a few adventures she got me into a few days ago..."
    if counter_us_7dl_px >= 1:
        "And this semi-mystical tale of The Flares, searchings."
        dreamgirl "And Danechka, who wants to be a lighthouse keeper."
        "I nodded in agreement."
        "There were a lot of ambiguities and white spots in this story to consider it just fiction or games of «belief»."
        "Except that there was some obstacle, that no matter how hard I tried, I couldn't get over."
        "They wouldn't let me go any further."
    else:
        "Well, of course, I didn't leave the girl alone in the time of need."
        if alt_day5_me_neu_us_potato:
            th "Fed the suffering with potato."
        th "A hero, isn't I?"
        dreamgirl "You didn't get a kiss from the beautiful lady as appreciation."
        dreamgirl "So there's no smell of heroism here. Friendzone at best."
        th "It all comes down to one thing with you!"
        dreamgirl "Well, yes actually! I'm not a prude like you."
    "Waving my hand, I decided to go find the girl after all, spitting all her «piss offs»."
    "It was hard for me to admit to myself, but I was used to her, seeking her attention..."
    "I never had it as easy as I did with this kid."
    "And I really appreciated it."
    scene bg ext_house_of_dv_day
    with dissolve
    "The citadel of redheads looked closed."
    "Nothing had changed here: still the same open window, still the same net."
    "The unchanged jolly Roger scowled familiarly at me through the glass of the door."
    "There were no shoes on the balcony window, so no one was here and..."
    "I heard some inaudible mumbling."
    "Muffled, barely audible."
    "It came out in such a way that I couldn't tell where it was coming from."
    "Looking for the voice, I went up to the porch - the steps didn't even creak."
    scene bg ext_house_of_dv_day:
        linear 0.5 zoom 1.3 xalign .5 yalign .35
    pause(1)
    play sound sfx_knock_door_closed_hard1
    "It's locked."
    "And the voice is silent, too."
    "Not for long."
    with fade
    "Soon he resumed his muttering song again."
    th "What a miracle."
    dreamgirl "Maybe it's time to turn around and go to Viola."
    th "What do you mean?"
    dreamgirl "Well, that's it! The cuckoo's up, THE VOICES ARE YELLING."
    th "Thanks for your help, nerd."
    scene bg ext_house_of_dv_day
    with dissolve
    "I stepped off the porch and listened."
    "The voice was everywhere and nowhere again."
    play sound sfx_bush_leaves
    scene bg ext_path_day
    with dissolve
    "I guessed that Alisa and Ulyana would not have enough room in the cabin for both of them."
    "So I was not at all surprised when an almost invisible path led me to a tiny clearing surrounded by dense vegetation."
    "Here was everything I needed to spend time alone: a log, a hole in the ground lined with cobblestones, and a small canopy of branches."
    th "Yeah, that's if the redheads wanted to hide from everyone, they wouldn't have to, run outside the territory, like Lena."
    "Not a bad find, but it's still a little different than what I was looking for."
    "The muttering could be heard here too, but it was a little weaker."
    "I deduced that it was coming from the cabin."
    "There's nowhere else."
    "And since it's closed..."
    "I crept back up the path to the bend and turned at the back wall."
    "From there you could see the window was wide open because of the heat."
    th "Now we'll see."
    "I got closer and peered through the window."
    stop music fadeout 3
    scene bg int_house_of_dv_day
    with diam
    play music music_7dl["wheres_wonderland"] fadein 3
    "What I saw there was unexpected to say the least."
    "I froze."
    "Ulyana, the ever combative, cocky, and perky, Ulyana, who never goes overboard, was sitting on the bed playing with the bear."
    if alt_day2_us_escape:
        "With a big plush toy, which she had once already taken with her when we ran away from camp together."
        "I noticed back then that she didn't take a mountain of clothes or a backpack of food with her."
        "No. She took the most important things."
        "That bear and the bag of candy."
    "Next to Ulyana's bed was a makeshift crib made of boxes and some red T-shirts with «USSR» insignia."
    th "So she's not running around in the same thing all the time?"
    "It came to me belatedly."
    th "It's just that she has a bunch of these T-shirts?"
    "And it was pretty obvious who she made that bed for."
    "Nice, naive picture."
    "Somewhere I was even a little jealous of her, because I lost something like that."
    "Even in the most enclosed and sheltered place I can't allow myself to relax and remember the things that were really important as a child."
    "Not problems and heartaches, but a bedtime bear."
    "The girl must have really felt extremely secure now."
    "Clutching the teddy to her chest, the girl smiled with genuine sincerity."
    "There was real happiness in her eyes, real adoration."
    "In this closed cabin, in the quiet hour, when no one can disturb and break into the holy of holies, Ulyanka could allow herself to be what she had always been."
    "A child."
    "Leaning over the bear, dressed in red pants and a blue polka-dot apron, she cooed softly:"
    us "Good Misha, good Misha."
    us "May you dream of something bright and sunny."
    "She stroked the bear's head."
    "Suddenly the immortal lines came to mind:"
    th "And forgave the coming and the caprices and the pranks of the sweet little girl..."
    us "And tomorrow will be morning, Misha."
    "She laid the bear down on the crib, covered the top with a T-shirt, tucked the corner in."
    us "And I'll take you on the road. Do you want to go on the trip with me?"
    us "We'll go home again, you and me."
    us "I'll come to you every night to tell you a story."
    if counter_us_7dl_px >= 1:
        us "I learned a new fairy tale."
        us "You know, I learned the beginning last year, but the - end just now."
        us "About wasted time, childhood and forgotten toys."
    us "Really, you do? So do I."
    "She leaned over the crib and said something already quite indistinguishable."
    "And I..."
    "Humans is overwhelmingly stupid after all."
    "I tried to treat her as an equal for some reason."
    "Like an adult who thinks and does only after consulting with his head."
    "Chalked up her mischief and pranks to her just having a bad temper."
    "Or family problems."
    with fade
    "How many other things could explain a man's behavior?"
    "And was wrong."
    "We were all wrong!"
    "Except for Olga Dmitrievna, who let the girl get away with a lot."
    "That's the one who probably didn't make a mistake and try to bring up Ulyana as a relatively mature person."
    "And what kind of adulthood and responsibility can we talk about when the girl locks herself in at quiet time so that no one will find her when she is at her most vulnerable."
    with fade
    "At a loss, I took a step back."
    play sound sfx_bush_leaves
    "The leaves rustled."
    "The muttering was silent again, but it didn't embarrass me anymore."
    "I was more confused by the secret I was discovering, which was like a suitcase without a handle: hard to carry and hard to throw away."
    "And who am I going to tell that the only child in our squad is actually a real child?"
    th "Huf... what a big secret huh."
    stop music fadeout 3
    return

label alt_day6_us_7dl_deserter:
    scene bg ext_house_of_dv_day with fade
    "After walking around the citadel of redheads, I sat down on the steps."
    play music music_list["get_to_know_me_better"] fadein 5
    "I wasn't afraid of getting caught, and the fact that Ulyana would figure it out didn't scare me nearly as much."
    "I should have come to my senses and thought about what I'd seen."
    play sound sfx_unlock_door_campus
    pause(1)
    show us shy sport
    with dissolve
    "The lock clicked, and the little one sat down on the step next to me."
    us "You saw that, didn't you?"
    me "Your cooing was hard to miss."
    "I smiled."
    me "So I got curious."
    show us normal sport with dissolve
    us "So be it! I'm not the least bit ashamed of it!"
    show us shy sport with dissolve
    me "Not a bit."
    "I confirmed, watching her ears scarlet."
    "For some reason I didn't feel like teasing her at all, though I wouldn't have missed my chance before."
    "After all the things she's done to me? That's a sacred thing to do."
    "Not this time."
    "Ulyana pulled up her tank top and, grasping the big round metal button on her shorts, twisted it, apparently struggling with embarrassment."
    me "Military button?"
    "Pointed my finger."
    show us grin sport with dspr
    us "Oh, man! He doesn't know about epaulets and stars, but he knows about buttons."
    me "Uh-huh."
    "She twisted the button again in response."
    us "Why aren't you going to rehearse or clean up?"
    me "And you?"
    show us surp1 sport with dspr
    us "What a joke of humor! Me - and clean up!"
    us "I'm not allowed! I'm a child, child labor exploitation!"
    me "You've been listening to a lot of nonsense, now you're repeating it."
    us "It's not nonsense at all."
    show us upset sport with dspr
    "Ulyana turned her nose up and looked down at me."
    me "What a pantomime."
    th "Looks like she got over her embarrassment."
    th "What embarrassment, though. As if I caught her naked..."
    if lp_us >= 9:
        th "Though I've already caught her once, yes."
    dreamgirl "I suppose it would embarrass her a lot less. The kids at school don't laugh at you for being naked."
    "With a sigh, I was forced to agree with that thought as well."
    show us laugh2 sport with dspr
    us "So you're a deserter today?"
    us "Confess!"
    me "What kind of deserter am I..."
    if not herc:
        extend " I didn't even serve."
    show us laugh sport with dspr
    "Ulyana laughed in response, jumped up from the step and jumped around me, shouting:"
    us "Deserter! Deserter! Three out of order!"
    me "And doesn't it bore you?"
    "Melancholy I murmured."
    show us normal sport with dspr
    "In response, the girl thought for a second."
    show us grin sport with dspr
    "Then her face brightened:"
    us "Don't worry, deserter! I've thought of a way to save you!"
    if counter_us_7dl_px >= 1:
        me "Rescue? What about your searchings?"
        show us surp1 sport with dspr
        us "And how did you... Ah, yes."
        us "Then you're a double deserter! And you promised me you'd finish that case."
        me "Case?"
        us "The search! {w} Me and the boys found The Old Road today, there in the creek they were launching new Flares."
        us "And where were you at that time?"
        me "Pissed off."
        "I grumbled."
        me "Just like you told me to."
        show us laugh sport with dspr
        us "What an obedient deserter."
    hide us with moveoutleft
    show us smile sport with moveinright
    "She went around me one more time, then nodded sharply."
    us "Get up!"
    "She commanded."
    us "Let's go!"
    me "Where to?!"
    show us laugh sport with dspr
    us "Let's go, let's go!"
    us "You'll see."
    "Jumping up to me, she yanked my arm, and I willy-nilly got up."
    me "Can you explain clearly where you're dragging me?"
    "I demanded."
    show us smile sport with dspr
    us "You'll see. Move, don't just stand there!"
    us "If Auntie Olya sees us now, we're screwed, screwed aaand... Screwed!"
    "Ulyana started to run."
    th "Child."
    "Once more I reminded myself."
    th "You can't be mad at her."
    "Though I wanted to, to be honest."
    scene bg ext_house_of_dv_day at fast_running
    with flash
    "But somehow, we raced through camp, skilfully maneuvering between the squad leaders, the pioneers..."
    "Who are supposed to be asleep, for it's quiet time around camp!"
    "Or at least rehearsing."
    stop music fadeout 3
    scene bg ext_square_day at fast_running
    with flash
    play music music_list["went_fishing_caught_a_girl"] fadein 3
    us "Syomych, if you make that face, I'll take you to Viola to give you a laxative."
    "Ulyana snorted, not slowing down her step."
    me "And you always keep mocking!"
    "I exhaled."
    "Ulyana laughed and added to her stride."
    scene bg ext_clubs_day
    with dissolve
    "As it turned out, our destination was the clubs."
    "Closed, of course."
    me "And why are we here?"
    show us grin sport with dissolve
    us "You'll see."
    "Ulyana glanced around cautiously and headed for the porch."
    "She didn't go up the stairs, though; she turned onto the concrete walkway by the wall and staggered to the far corner."
    us "Don't just stand there, follow me!"
    me "What are you going to do?"
    me "Do something nasty again?"
    show us laugh sport with dspr
    us "Don't worry."
    "She laughed."
    us "We won't blow anyone up or poison anyone. I give you my word."
    me "I don't think so."
    us "You're so afraid. A grown-up, fat, lazy Semyon shouldn't be like that."
    me "Hey! I'm not lazy!"
    "I resented it."
    show us laugh2 sport with dspr
    us "So you have no objection to everything else?"
    me "And not fat. But mature!"
    us "Very mature."
    "We went into stealth mode, so she no longer cackled at the top of her lungs."
    "But that didn't make her slips any less offensive."
    us "It was especially mature when you defied your squad leader to make your own rules."
    me "It's a heightened sense of justice!"
    if counter_us_7dl_px >= 1:
        me "I was worried about you!"
        us "Thank you. Very touched."
        us "But what Aunt Olya would think, of course, you forgot."
    else:
        us "For sharing, of course, thank you!"
        us "But what you did is in spite of the leader, did you think?"
        us "She punished both me and Alisa on purpose. For a reason!"
        us "And you interfered."
    "I didn't find an answer."
    "Yes, strictly speaking, the act was rather infantile."
    "But at the time I thought I was doing the right thing."
    th "And it turned out that even in the eyes of my «savior» I was acting like an overgrown fool."
    me "Okay, forget it."
    show us laugh sport with dspr
    us "Forget-forget!"
    us "Fat and lazy ungrown Syomych!"
    me "Stop it."
    "Ulyana giggled."
    show us smile sport with dspr
    "Then suddenly she hissed."
    us "Wait, I think we're there."
    "We stopped at a blind window, barred by a sheet of paper of some kind."
    us "Give me a lift."
    me "I've got a bad feeling about this."
    us "Don't shake, you little coward. You'll be all right!"
    show us grin sport with dspr
    "Ulyana winked at me and shook her head demandingly."
    "With a sigh, I obeyed."
    hide us with dissolve
    "A moment, and she clung to the slope, clinging to everything she could."
    us "Let me go."
    "She hissed."
    us "Glass down for you, take it."
    "She fumbled, snatched a hairpin from one of her tails, and, acting with it like a pair of pliers, successively bent back the four nails holding the glass."
    us "Take it! Don't you slow down."
    me "Of course. The glass with your bare hands."
    us "Then take off your shirt."
    me "It wasn't for you that my rose bloomed!"
    "Proudly I turned up my nose."
    "She laughed and let out the glass with laughter."
    "I didn't even have time to say anything."
    "The glass came crashing down, and I was about to close my eyes, saving them from the slashing shards, and..."
    show us smile sport with dspr
    "Ulyana snorted:"
    us "At least you're lucky for something!"
    "At the concrete walkway itself, the glass inexplicably glided sideways and, breaking through the bushes, got stuck near the ground."
    me "Lucky, so lucky."
    show us grin sport with dspr
    us "Yes!"
    "Ulyanka shrieked excitedly, and then she immediately realized."
    show us shy sport with dspr
    us "Oi!"
    me "Incredible! The whole camp hasn't heard us yet.!"
    show us smile sport with dspr
    us "Ne-rd!"
    "Reacted the girl."
    us "Okay, go ahead, set your hump, I'll get in."
    hide us with dissolve
    me "Won't you tell me what you forgot there?"
    us "I told you: salvation! A place where no one will find you, a deserter."
    "She swung her foot impatiently in the air and immediately, with an owl, grabbed the frame."
    us "Well help me, I can't reach it."
    "For the umpteenth time, sighing, I put first my arm and later my shoulder."
    "Upstairs there was a noisy squawk, reached up, then froze."
    me "What else?"
    stop music fadeout 3
    with fade
    pause(1)
    play music music_7dl["catch_the_hedge"] fadein 3
    us "Oi!"
    "Ulyana babbled this with such directness that I didn't even get angry."
    me "What's wrong?"
    us "I... I'm stuck."
    "She stretched."
    me "Can't you get in or something?"
    us "Yes, I can! I'm caught on something!"
    me "Come on."
    me "On your head, come on! Three..."
    "She rushed forward, and the silence of the camp cut through with a palpable ripping sound."
    play sound sfx_7dl["tearing"] fadein 0
    dreamgirl "Four."
    "Something hard fell on my head."
    "And a moment later, Ulyana disappeared through the window like a fish."
    us "Did you catch it? Caught it?!"
    me "Caught what?"
    us "A button! I caught it on a nail!"
    th "That's the answer to what hit me in the head."
    me "Uh, no. Something fell on me, but I don't know what it was."
    us "Look it up, will you?"
    "My Rapunzel showed her nose out the window."
    us "Because I can't button my shorts. They're falling down!"
    me "And what's torn there?"
    "Ulyana blushed."
    us "It's a button, I tell you!"
    me "With that sound? I don't think so."
    "With a throaty growl, Ulyana disappeared."
    "And a couple of seconds later, from the club room came the following:"
    us "Not a word to anyone."
    me "Tell me about it."
    us "I ripped my pants, right down the middle, from fly."
    "She giggled nervously."
    us "So now I don't have shorts, I have two halves."
    us "And not just them."
    "She sighed and called out:"
    us "Okay, are you climbing?"
    "And then I realized, oh, I assure you, I realized one simple truth."
    "Whatever happened now, we shouldn't be seen around while she's like that."
    "There's no way we should be."
    dreamgirl "You know, I'm usually always for you. And if you were there together, but in a normal way, I'm all for it!"
    dreamgirl "But if the leader catches you there with ripped shorts and panties... I can't even imagine what that would mean."
    dreamgirl "Word would get around for sure."
    "Ah, what a beauty - unanimity in the body!"
    me "No, I won't."
    us "What? Why?"
    if counter_us_7dl <= 6:
        me "What do you think?"
        us "Why?"
        me "You know, I don't want to be lynched on the spot by your best friend."
        us "Lyn... what?"
        me "I don't want any trouble."
        me "So I'm sorry, of course, but you certainly didn't save me."
        us "And you're just gonna walk away now? You're going to leave me like this?"
        "That's not a bad idea, by the way."
        me "I can send Alisa to get you a change of clothes."
        us "So go away. Traitor!"
        "Ulyana rattled something inside, letting me know that the conversation was over."
        "With a sigh, I left the scene of the failed autodaphe."
    else:
        me "Because I don't want anything to do with you!"
        "I exploded."
        me "You're the one who's been screaming about being a grown-up and all that crap, but now!"
        me "How by the God's sake did you do that?"
        me "You're gonna find a damn hole, in the middle of nowhere, and you're gonna fall in it."
        us "What, are you gonna leave me now?"
        "Ulyana whispered quietly."
        us "Since I'm such a loser."
        us "Will you leave?"
        "I sighed."
        me "No. But I'm not going inside either, not while you're like this. Do you have any idea..."
        us "Wee!"
        "With a shriek, Ulyana leaned over the frame and patted me on the top of the head."
        us "Even though you didn't find the button, thank you, Semishe!"
        me "Mm-hmm. Now all I have to do is figure out what to do."
        "The situation is stalemated, that's for sure."
        "Ulyana, on the other hand, didn't seem at all embarrassed."
        us "What's there to think about? If you're so embarrassed of me, go to my place and get me a change of shorts!"
        "I remembered how she made a bed for her bear cub out of several absolutely identical scarlet shirts, so why shouldn't she have a couple or three identical shorts, too?"
        us "Will you?"
        us "And then I'll show you something interesting!"
        dreamgirl "I'm afraid there's nothing to show... yet."
        th "Shush."
        menu:
            "Are you nuts?":
                "I imagined in my mind, Alisa walking into the house, where I was rummaging through Ulyanka's things."
                "Clothes, in particular."
                "Or maybe underwear, too."
                "Maybe she's not lynch me right on the spot."
                "But she can castrate me with rusty pliers."
                me "What if I get caught? Or even caught with your stuff in my hands?"
                us "What a coward. And you'll run away!"
                me "Exactly. Right into the wall with my head."
                us "Well, what do we do then?"
                "The girl got angry."
                me "Nothing. I refuse to go through your things, and I can't leave you like this."
                me "I'll go try to find your roommate."
                us "Come on..."
                "Ulyana grimaced."
            "And how I'll get into the cabin?":
                us "Nah, Alisa should be there."
                "Ulyana made a pretty strong argument."
                "Fortunately, I had an even stronger one."
                me "Right. She should be. And I have to look in your bags for spare shorts in front of her."
                us "Mm-hmm. Bad idea."
                "I could see that she didn't want to give me her key at all."
                me "And then. If she's not here, do I have to run all over camp and risk getting caught by the leader?"
                me "And you'll be sitting here all the time, naked, until someone opens the door."
                me "That'll be a surprise!"
                us "What a surprise, no one will tell you anything."
                me "They won't tell yes, but they can hit me in the face without any questions."
                me "You're my friend, but you're not that good!"
                us "Impossible man."
                "I don't know to whom Ulyana complained."
                us "Catch it this time, will you? You crooked monster."
                me "Hey! I can hear everything!"
                us "Put your hand up, I said!"
                "A key tied to a ladybug-shaped keychain fell into my hand."
                "A very strange keychain, though."
                "It used to be a traditional red and black beetle."
                "But over time, it wore out..."
                us "What?"
                "Ulyana snorted unhappily when she saw me staring at the green and blue monster with multicolored dots."
                us "Yes, I painted it. I'm allowed, I'm a kinder."
                me "Wait for me, kinder."
                "I grinned."
                me "A couple of minutes and you're saved."
                us "You're such a lifesaver."
                "A farewell sounded in my back."
                $ alt_day6_us_7dl_help = True
    stop music fadeout 3
    return

label alt_day6_us_7dl_ghost:
    scene bg ext_square_day with fade
    play music music_list["smooth_machine"] fadein 5
    "The camp emptied completely."
    "The squad leaders worked neatly, the ambushes were well organized - in short, the pioneers were gone from the street."
    "So we had to move exclusively by short runs."
    "I was well aware that if someone met me, I would be in the club until dark, until I could slip out and get to the cabin."
    "Which means good-bye, dinner, disco, and good cheer."
    "I was mad, of course, but not that mad."
    "So from shelter to shelter, march! March!"
    scene bg ext_house_of_dv_day
    with dissolve
    "It took me much longer to get to Alisa and Ulyana's house than it would have if I had walked very leisurely but directly."
    "So without delay I sprinted up the stairs to the door."
    play sound sfx_unlock_door_campus
    pause(1)
    "I purposely checked to make sure the lock clicked - I'd hate to see Alisa inside."
    "No shoes outside, obviously."
    "But I fell for that once, and I won't fall for it again."
    stop ambience fadeout 3
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg int_house_of_dv_day
    with dissolve
    play ambience ambience_int_cabin_day fadein 3
    "After figuring out where things of everyday wear might be stored, but things more... ahem, intimate would not be, I reached under the bed in search of her bag."
    "And just as I dove down into the dusty gloom..."
    play sound sfx_open_door_kick
    pause(1)
    dv "And what do we have here?"
    play music music_list["awakening_power"] fadein 2
    dv "And what an interesting pose!"
    "I straightened up."
    "At the door of the cabin hands at sides stood..."
    scene bg int_house_of_dv_day
    show dv angry pioneer2 at zentercenter
    with dissolve
    "Alisa!"
    "And she looked creepy."
    "All smeared with something black and greasy."
    "Tired - as you could see in her sunken eyes."
    "And very, very angry!"
    dv "Rookie."
    "Sweetly she sang."
    dv "You don't want to"
    show dv rage pioneer2 with dspr
    extend " EXPLAIN YOURSELF?!"
    me "Iiiyymm…"
    "I baa'd."
    show dv normal pioneer2 with dspr
    dv "As I thought."
    "Alisa nodded calmly."
    play sound sfx_lena_hits_alisa
    pause(1)
    scene black
    with fade
    stop music fadeout 3
    pause(1)
    show unblink
    scene bg int_house_of_dv_day
    show dv normal pioneer2
    with dissolve
    play music music_list["eat_some_trouble"] fadein 2
    "When I opened my eyes, Alisa was sitting on the bed, looking at me sideways."
    me "And what did you hit me for?"
    "With surprising calmness, I asked."
    me "I didn't steal anything, I didn't touch anything of yours."
    dv "So you didn't rummage under Ulyanka's bed.?"
    me "Well, I did, but for a reason!"
    show dv angry pioneer2 with dspr
    dv "I'll take you to Sanich, he'll show you the reason!"
    me "Then take me there!"
    me "Let Ulyanka continue to sit in her rags."
    show dv shocked pioneer2 with dspr
    dv "Rags? What happened?"
    me "What a clever, and more importantly, timely question."
    "Me squaled."
    me "She ripped. When she climbed where she shouldn't have climbed."
    me "Now she's sitting there in one T-shirt, waiting for me to get her something to cover her shame."
    show dv shy pioneer2 with dspr
    dv "Why didn't you say so right away?!"
    me "Right away?!"
    "I felt myself boiling over."
    me "Go you know yourself where? Did you give me that «right away»?"
    me "No - you «right away» started swinging your rake."
    me "If you have PMS, it's not my fault."
    show dv guilty pioneer2 with dspr
    dv "Don't sulk. It's just a hit."
    dv "Scars make a man look good."
    me "Scars! Not a punch in the schnopak."
    show dv shy pioneer2 with dissolve
    dv "Well, should I what? Apologize to you now?"
    dv "It happens, I cracked in the heat of the moment. We're all human."
    me "As if I can get it from you."
    "I grumbled."
    me "Help me find Ulyanka's shorts and we'll call it even."
    dv "A sec..."
    "Unlike silly me, Alisa didn't hesitate to go straight into the closet."
    hide dv with dissolve
    "And it didn't take her, unlike me, even a few seconds to find what she was looking for."
    dv "Catch!"
    "She threw her shorts over the door."
    dv "And... Don't hold a grudge, please."
    me "Where did you come from so pretty?"
    dv "Are you still here?"
    me "Mm-hmm. So where from?"
    "Dvachevskaya was quiet, but eventually reluctantly admitted:"
    dv "I punched one guy in his pumpkin, so he wouldn't talk too much."
    me "Can't you use words?"
    dv "They don't understand words!"
    dv "He pissed me off ever since the concert, when he decided to open his mouth to those who have no parents."
    if alt_day4_me_neu_volley:
        me "What concert? You were playing with us."
        dv "Are you retarded? {w}You think there's one concert for the whole shift?"
        dv "Last concert just made me want to punch him."
    dv "But he didn't give me a reason."
    me "And now he did?"
    show dv normal pioneer2 with dissolve
    dv "And that was a good hit!"
    me "And you were punished."
    show dv angry pioneer2 with dspr
    dv "Made me clean that campfire cleaning, damn it."
    dv "Just got free now. Don't you know if lunch is coming up?"
    "On the job - and the reward?"
    "Only it looked like Alisa's reward was lack of lunch."
    me "Lunch has been over for an hour."
    "Alisa looked at me incredulously, and then muttered a profanity."
    dv "I knew it! I should have left it there as it was!"
    me "And how are you now?"
    if alt_day5_me_neu_us_stores:
        "I had nothing to offer Alisa - yesterday's supplies given to both redheads, Ulyanka successfully ground herself."
    show dv sad pioneer2 with dspr
    dv "I don't know. I'll think of something."
    me "Why don't you go look for Olga? Or go straight to the canteen?"
    show dv grin pioneer2 with dspr
    dv "By the way, yes! I've been working, I'm due!"
    dv "An upstart gets fed whenever she asks for it. How am I any worse?"
    if loki and (alt_day_binder != 1):
        me "And if they don't feed you, you can always rob them."
        me "It's not the end of the week, the groceries are all in the canteen."
        "Alisa narrowed her eyes unkindly, remembering her previous attempted burglary, but remained silent."
        "Right now she was only concerned with gastronomic matters."
        me "Okay, good luck finding provisions."
    else:
        me "At the very least, you can steal a bun if you can't wait another hour until noon."
    play sound sfx_open_door_strong
    pause(1)
    scene bg ext_house_of_dv_day
    with dissolve
    "Alisa nodded and, pushing me out of the cabin, rattled around with something."
    "Looks like she was going to put on her makeup before she went to high society."
    scene bg ext_clubs_day
    with dissolve
    "When I went back to Ulyana's place, clamping my nose shut, no one seemed to be there."
    me "Ulyanka, get your shorts."
    "I barked."
    "After the meeting with Dvachevskaya, the mood was not rosy to say the least."
    "Silence."
    me "Ulyanka, hello, awake!"
    "No answer!"
    "Worried, I tiptoed up to see what was going on inside at all."
    "Of course I wasn't tall enough."
    th "Where could she have gone?"
    "Remembering where she'd put her feet when I dropped her off, I used Ulyana's example and grabbed the ledge and pulled myself up."
    "The ledge crept leisurely toward my chin."
    "White, though dirty."
    "And then, once I was up there, I realized that it wasn't just the ledge that was white."
    scene black with dissolve
    "Out of the half-darkness of the room, something white and shapeless was looking at me."
    play sound sfx_scary_sting
    with flash2_red
    us "Boo!"
    "It howled in Ulyanka's voice."
    "And I was surprised to see it open its arms."
    play sound sfx_bush_body_fall
    scene bg ext_clubs_day with dissolve
    with vpunch
    "With a shriek I flew down."
    dreamgirl "What's the difference between falling from the first floor and falling from the tenth floor?"
    "Inserted by the inner voice."
    play sound sfx_bush_body_fall
    stop music fadeout 3
    "I bumped my soft spot and almost bruised my coccyx."
    "It didn't hurt so much physically, but mentally."
    play music music_7dl["anglegrinder"] fadein 3
    me "ULYANAAA!"
    "I yelled."
    "There was a laugh from the window, and a ghost flew out of the window above me with a white lightning bolt."
    "Laughing with a familiar laugh!"
    if persistent.hentai_graphics_7dl:
        scene cg d6_us_ghost_hole_7dl with flash
    else:
        scene cg d6_us_ghost_7dl with flash
    "It grouped up, rolled over, and, howling and hooting, darted away."
    "Well, I followed it."
    th "If I catch her, I'll whip her."
    "I promised myself."
    "My inner voice tried to add some obscenities, but I was now driven by the thirst for educational revenge!"
    "Ulyanka, in an blanket cover she got from nowhere it seems, was running ahead of me and waving her arms."
    "I couldn't shorten the distance, but she couldn't break away."
    "So we had a kind of parity."
    "In fact, I'm surprised no one noticed us during that run."
    "I mean, no one noticed me last time either."
    "But now... When there's a shrieking and giggling procession rushing through the camp, with half of them waving their arms like wings, tucked into a blanket cover, and the other half waving with shorts angrily over their heads..."
    "We weren't caught, we weren't seen, and..."
    scene bg ext_boathouse_day with dissolve
    play ambience ambience_boat_station_day fadein 3
    "We rolled out to the boat station, and the ghost, still waving his paws, bogging down in the sand, ran toward the pontoons."
    "I wasn't quite sure why I was running anymore."
    "Then I noticed that I was still clutching a certain object in my hand."
    dreamgirl "She's there under the duvet cover in just a T-shirt."
    dreamgirl "Think about it!"
    th "Give me a break, nerd."
    "She didn't have much room to run, so I slowed down, took a step."
    "It stung in my side, and I couldn't get my breath back."
    "But she's not going anywhere now."
    "She's going to get it now!"
    th "I. Ran. For the goddamn. Shorts. And you. Here. Arranging?!"
    "Like an idiot playing stealth, getting punched in the nose by Dvachevskaya - and all for that?"
    me "You won't get away now."
    "The only way out for Ulyana now was to dive."
    "Well, or turn around to me and pretend to be the cat from Shrek."
    "Though I don't think the latter will get through me."
    "I was going to punish and kill."
    show us shy sport with dspr
    "Something similar seemed to shimmer in my eyes, as Ulyanka, turning to me and making the face of an adorable little girl"
    show us surp2 sport with dspr
    extend ", groaned and retreated."
    show us grin sport with dspr
    "And then, with a sly wink at me, she turned around and took a short run..."
    hide us with dspr
    "Time stood still."
    "I rushed after her, not wanting to lose my prey!"
    "No, I definitely shouldn't have let her go in the water."
    play sound sfx_shoulder_dive_water
    pause(1)
    scene anim_underwater
    play ambience ambience_7dl["underwater"] fadein 3
    "Only it was me who ended up in the water, not her."
    "The old, old trick from Ivan Vassilievich."
    "And I, the fool, bought it."
    "The water was freezing!"
    with vpunch
    "It took my breath away."
    "Through the water I heard Ulyana's gushing laughter, someone's shorts floating bubbly over my head."
    th "The narrator shoots himself. Roll the credits."
    "The thought went through my head grimly, as I folded my arms across my chest and drifted off to the bottom."
    "I really wanted to strangle someone."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_fiasco:
    scene bg ext_house_of_dv_day
    show dv normal pioneer2
    with dissolve
    play music music_list["afterword"] fadein 3
    "I was just coming up to Ulyana and Alisa's cabin when I noticed Dvachevskaya on the porch."
    me "Alisa! Hey!"
    "She was just closing the door."
    show dv grin pioneer2 with dspr
    dv "Who do we have here?"
    "Alisa squinted."
    dv "Isn't that my friend's best knight?"
    me "Humor me. We have a situation here, well..."
    show dv normal pioneer2 with dspr
    dv "Did something happen to Ulyana?"
    "That's when the redhead came up."
    me "Nothing happened to her. But with her clothes..."
    show dv shy pioneer2 with dspr
    dv "Did you..."
    me "You're crazy! How could I."
    me "No, she was trying to get in one window and slashed her shorts."
    show dv normal pioneer2 with dspr
    dv "Shorts. Slashed."
    "I nodded."
    me "She got caught on a nail while she was climbing and yanked, so now she's got two halves of shorts instead of one whole."
    dv "How do you know that?"
    me "I was lifting her."
    show dv laugh pioneer2 with dspr
    dv "Who'd have doubted it!"
    dv "And now she's in the window and you're here?"
    me "Practically."
    show dv normal pioneer2 with dspr
    dv "So, where did it all happen?"
    me "At the cybernetic club."
    dv "Going for the saltpeter again."
    "Alisa nodded understandingly."
    me "So will you help?"
    show dv grin pioneer2 with dspr
    dv "Can't leave you in the lurch, since you're such a klutz."
    dv "Wait here."
    play sound sfx_open_door_2
    pause(1)
    hide dv with dissolve
    "She disappeared behind the door, and I sat down on the step again."
    me "Why did I ever get into this in the first place..."
    "It felt like four o'clock, which meant the concert was about to start."
    "The squad leader obviously wouldn't pat me if she find out that I'm missing."
    th "Maybe just drop this whole thing."
    "Sorrow and despair it is."
    stop music fadeout 4
    mt "I don't know what you got yourself into, but I'm taking you."
    play music music_list["doomed_to_be_defeated"] fadein 0
    show mt smile pioneer with dspr
    "Ninja of the Village of Hidden Laziness - Olga Dmitrievna appeared, as usual, completely silently."
    "She smiled, and in her smile I saw something sinister."
    show mt rage pioneer with dspr
    mt "To the concert. Now!"
    "She barked in a way that, if I hadn't been sitting down, I would have been."
    "The frantic gathering at my back went silent for a few seconds, too, while Alisa listened to the threat."
    "But they soon resumed."
    me "I'm sorry, Olga Dmitrievna, but we can't right now."
    show mt angry pioneer with dspr
    mt "We? Who are you talking about?"
    "Pulling me aside, the leader climbed the stairs and opened the door."
    play sound sfx_open_dooor_campus_2
    pause(1)
    mt "Un-der-stan-dable."
    "She muttered.."
    mt "Dvachevskaya, out."
    "Something was muttered indistinctly from inside, and the squad leader was finally furious:"
    show mt rage pioneer with dspr
    mt "Did you not understand?! Out. Now!"
    show dv angry pioneer2 at left behind mt
    with dissolve
    th "Looks like Ulyana going to walk around with her butt naked today."
    "I concluded."
    th "Unless, of course, a miracle happens."
    dv "And what are you going to do to me? Send me to clean the clearing again?"
    dv "I'm very scared, I'm trembling all over."
    show mt angry pioneer with dspr
    mt "Dvachevskaya, don't get bogged up again."
    show dv rage pioneer2 at right with dissolve
    dv "Bogged up? Me?!"
    "Alisa got mad."
    dv "So sending me to work for no good reason and then depriving me of my lunch, that's not you getting bogged up?"
    dv "Do you know how funny it was when I got to the cafeteria and they told me lunch was over and there was no food?"
    dv "Joke of the century!"
    show mt normal pioneer with dspr
    mt "No one made you stay that long. If you'd done it quickly, you'd have gotten your lunch."
    show dv smile pioneer2 with dspr
    dv "I heard ya. And I'm also at fault."
    "Alisa calmed down at once."
    dv "I'll go talk to Alexei Maksimovich about it.{w} Maybe he thinks so, too."
    "Alisa threw me the shorts and slammed the door, turned the key in the lock."
    dv "It even made me wonder."
    show mt sad pioneer with dspr
    "I can't say that Alisa's remark frightened the leader, but it did bother her."
    mt "Where are you going?"
    dv "Did you not hear well? I'm going to the head of the camp."
    "Alisa bowed picturesquely."
    dv "If he, too, thinks that making pioneers work and starve them to death is normal, fine."
    dv "Or else he might feed me at least."
    show mt shocked pioneer with dspr
    mt "Dvachevskaya - and snitching?"
    dv "Why «snitching»? He and I will have a friendly chat."
    "I imagined in detail all the consequences of such a «friendly chat» and inquired:"
    me "Maybe you have anything?"
    me "Anything to eat."
    show mt normal pioneer
    show dv surprise pioneer2
    with dspr
    me "That really isn't fair."
    "Alisa stared at me in surprise, but Olga didn't raise an eyebrow."
    "She seems to have pulled herself together by now."
    mt "I'm going to the cafeteria in half an hour to get scones for the afternoon snack, because of the concert."
    show mt grin pioneer with dspr
    mt "I can get Alisa a double portion, since she's so hungry."
    show dv normal pioneer2 with dspr
    dv "Not lunch, of course..."
    me "But better than with an empty belly."
    show mt angry pioneer with dspr
    mt "Provided - I repeat! That you both go to the concert now."
    show dv sad pioneer2 with dspr
    dv "Concert..."
    "Alisa was sad-apparently she was preparing something for the show, too, but to go with such a mood to perform..."
    mt "And yes, Semyon."
    "The leader turned to me."
    show mt normal pioneer with dspr
    mt "Why do you need Ulyana's shorts?"
    th "Eh, two deaths can't happen!"
    "I thought about it and confessed:"
    me "It's for Ulyanka."
    "Alisa didn't seem to like my frankness."
    "There must have been something in her look."
    "Or in the silently whispered «snitch» lips?"
    mt "Torn somewhere again?"
    "I nodded."
    mt "I'll take it. And you go to the concert. Both of you."
    mt "Shorts to me, now."
    "Alisa reluctantly nodded, and I held out the shorts."
    mt "Again, where does Ulyana sit?"
    dv "Don't tell her."
    me "And leave her there like that? No way."
    me "She's in the back room of cybernetics club."
    show mt normal pioneer with dspr
    mt "Thanks."
    mt "Now to the le-ft! To the concert - march!"
    "The squad leader froze in place, seeing us off."
    mt "I'll be back in half an hour with an afternoon snack, and both of you better be at the concert!"
    stop music fadeout 3
    scene bg ext_square_day with dissolve
    "The whole time we walked to the square, I felt her eyes on my shoulder blades."
    "And Alisa was muttering something to herself."
    "She was careful not to notice me."
    "And on the square we were intercepted by Sanich, who escorted us to the stage."
    "A worn-out machine, my ass."
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_rendezvous:
    scene anim_underwater with dissolve
    play music music_7dl["dance_with_me"] fadein 3
    play ambience ambience_7dl["underwater"] fadein 0
    "This is not how I imagined my last day at camp."
    "Not at all."
    "I dreamed of games, laughter, loving eyes, and happiness soaked into the pine trunks that beckoned to come back here again year after year."
    "Something important."
    play sound sfx_water_emerge
    pause(1)
    play ambience ambience_boat_station_day fadein 3
    scene bg ext_beach2_day_7dl
    with dissolve
    "I came up, grabbed air with my mouth, and looked around..."
    "Ulyana was nowhere to be found."
    th "Ran away."
    "Cursing, and, with difficulty restraining my trembling, I scrambled toward the pontoons, praying to Random that I wouldn't cramp up."
    "Though drowning now would have been the logical conclusion to today's underdog benefit."
    scene bg ext_sky_7dl
    with fade
    "When I reached the pontoons in a few strokes, I clung to the railing with the last of my strength, pulled myself up, and, slipping moment by moment, scrambled out onto the dry boards and, coughing profusely, rolled over onto my back, staring up at the sky."
    "Of course I didn't catch up with Ulyanka."
    "Of course I got soaked to the skin."
    "Makes sense after swimming in your clothes, doesn't it?"
    "But something worse happened."
    scene bg ext_boathouse_alt_day_7dl
    with fade
    "I found my pocket suddenly empty and sat up jerkily with my knees to my chest."
    "Checked again - no."
    "Considering that I was used to feeling it in my pocket all the time, I would definitely feel it, if it suddenly tumbled out of my pocket."
    "The fact remained, I could feel it in my pocket before I jumped, after I jumped, I couldn't."
    th "I drowned the phone. Great."
    "Even though it had some kind of protection in the specs..."
    "I guess there aren't many models that can function successfully in a depth of ten meters."
    dreamgirl "Do you want to try dive in and get it?"
    th "In icy water? Random forbid!"
    "It took me a long time to discover what was missing."
    "Ulyanka owed me another favor."
    "And here she is."
    show us sad sport
    with dissolve
    us "Syomych, Syomych..."
    "Brokenly, she sighed."
    "The girl stood as if she hadn't just run through the territory with gyrating and waving her arms."
    "She breathed easily and freely."
    "But she looked sad."
    us "What are you sitting here for? You'll catch a cold."
    me "I'm dry."
    "I didn't want to talk. I wanted to find some source of warmth."
    show us surp1 sport with dspr
    us "Are you offended or something?"
    me "No. I'm dry."
    me "What more do you want?"
    "Warm, warm..."
    "Ulyana pouted, but chose to remain silent."
    hide us with easeoutleft
    "But where can we get it here, on the far side of the brig, where the pioneers come very rarely?"
    "So the answer was one-worded and dry."
    dreamgirl "What a pun."
    th "I'll catch a cold, I'll die, and you'll get it then!"
    dreamgirl "I will, of course. Do you know what they call your behavior?"
    dreamgirl "I'll freeze my ears off to spite my mother."
    th "Your usefullnes is..."
    "With all the bickering with my inner voice and trying to keep the shivers away, I didn't notice Ulyana had disappeared."
    "I found myself proudly alone."
    "And rightly so. I don't give a damn about any company."
    "I'm wet, pathetic and disgusted with myself."
    "So now I have every right to privacy."
    stop music fadeout 3
    play sound sfx_7dl["blanket"] fadein 0
    show us normal sport
    with dissolve
    us "Here."
    play music music_list["timid_girl"] fadein 3
    "Smiling happily, Ulyana turned to me."
    me "What «here»?"
    us "You're certainly mean, lazy, and old, Syomishe."
    us "But I don't want you to get sick. So wipe yourself off."
    "I noticed what she threw beside me."
    "The same blanket cover, in which she cosplayed the most annoying ghost in the world."
    "Dirty, wrinkled, but at least it's relatively dry."
    th "Salvation!"
    me "Thank you, of course, but how am I going to dry myself here?"
    show us smile sport with dspr
    us "Go to the bushes, wring out your clothes."
    us "I promise to peep."
    me "Pardon?"
    show us grin sport with dspr
    us "Come on. {w}It's not like I'm some kind of girls' window peeper."
    me "Touché."
    hide us with dspr
    "I muttered, and rising, I went into the bushes."
    "I economically wrapped blanket cover around my shoulders to keep me at least a little warm."
    "But it's not a lake, it's a river. The wind blows here all the time, so it'll be cold the whole time you stay wet, too."
    scene bg ext_path_day
    with dissolve
    play sound sfx_bush_leaves
    me "Brrr!"
    "Feeling the small girl's mocking gaze on my back, I broke into the bushes, trying to leave as much distance between me and her as possible."
    "Something told me that I would be somewhat defenseless naked, and therefore would not be able to resist the terrorist in any way."
    "So, forward, march!"
    "I went down to a small gap, overgrown with acacia and willow-herb, and here I decided to change my clothes."
    "The place wasn't ideal, of course, no doubt."
    "It was uncomfortable, prickly branches biting, a few stinging nettles on my bare feet, and red ants scurrying back and forth in the grass beneath my feet."
    th "But it's better here than on the beach, isn't it?"
    if lp_us >= 9:
        "Although if she gets the idea of getting even for the day before yesterday..."
        th "Oh, no, I won't give her that pleasure!"
    "I successively threw off my unpleasantly sticky shirt, tie, shorts, and socks, leaving me in just my boxers, rubbing my body to the redness with my already wavy blanket coverlet."
    th "That's the fate of bedclothes - first to run all over the camp, then to save the health of one pioneer."
    "I had no idea what to do with it after, to be honest."
    "In a good way, I shoul hand it over to Slavya."
    "But she'll start asking questions, prying... I don't feel like it."
    with fade
    "Looking around cautiously for possible observers, I pulled off my boxers and, wrapping my cold shirt around my loins, began to wring them out, too."
    "It was certainly a little warmer here than on shore."
    "But if anyone saw me like that..."
    th "And why didn't she run to the beach?"
    "I spat in my heart."
    th "I'd go to the dressing booth now and I'd have no trouble."
    me "Little shit."
    "The bushes nearby chuckled, and I reflexively covered myself with my palms."
    "The boxers fell to the ground, of course."
    me "Get out of here!"
    "The bushes giggled again."
    "Then came the sound of a bear breaking through the raspberries, and I let go of the feeling of prying eyes."
    th "Pervert."
    dreamgirl "Yeah. It's that age when they think of all sorts of stupid things."
    "The lost clothes on the ground is already occupied by ants."
    "I think they've decided to set up their own city or something."
    me "The apocalypse is coming!"
    "I grinned, shaking the insects off the cloth."
    "Squeeze-wring, wipe-wipe."
    "But if you keep this up, pretty soon I'll start getting chilly again, and then I'll definitely catch a cold!"
    "Not to mention what my uniform has become like."
    "All wrinkled, wet, cold..."
    "If I show up to the lineup tomorrow looking like this, Olga Dmitrievna will definitely crucify me."
    dreamgirl "There's no lineup tomorrow."
    th "Dinner, then."
    dreamgirl "I suppose, after you've blown off the concert, a crumpled uniform will be the least of your problems."
    th "I have a different opinion."
    "After getting dressed, I returned to the shore."
    stop music fadeout 3
    scene bg ext_boathouse_day
    show us laugh sport
    with dissolve
    play music music_list["that_s_our_madhouse"] fadein 5
    us "You should see yourself, Syomych!"
    "She laughed."
    us "Are you going to walk around the camp looking pretty now?"
    me "And what am I supposed to do?"
    me "You're the one who can be thrown in the water and have something to change into, and I don't have that pleasure!"
    show us surp1 sport with dspr
    us "Didn't they give you a second set?"
    me "I have no idea."
    "I grinned."
    me "It wasn't relevant to me before!"
    show us surp2 sport with dspr
    us "What are you mad about? It's no big deal, crumpled his clothes. Didn't rip at least!"
    th "But drowned my smartphone. And that's much, much worse."
    th "And it's all your fault!"
    th "But how do I tell you about it?"
    "I couldn't think of anything."
    show us laugh2 sport with dspr
    us "Are you going to pout now?"
    me "What am I supposed to do? Run around looking for Slavya or Olga"
    me "So they'll send me straight to the concert - all in the same uniform."
    show us smile sport with dspr
    us "Poor-poor, Semyon!"
    "The obnoxious girl squeaked sneeringly."
    "And the lust for murder, which had been quenched, awakened in my chest again."
    "But not for long."
    show us grin sport with dspr
    us "All right, I'll save you, all right."
    us "But you'll owe me one!"
    me "How, I wonder, in what way? Do you suddenly have a size 48 men's pioneer uniform in your pocket?"
    show us surp1 sport with dspr
    us "What? How did I get a man's uniform?"
    me "You're the one who suggested it."
    show us surp2 sport with dissolve
    us "Me?! Suggested?! What?"
    "That's when I couldn't take it anymore, and I went at her in the best Romero zombie tradition: with my arms outstretched and mooing:"
    me "Straaaangle..."
    show us surp3 sport far with ease
    us "Hey, get a grip on yourself! Are you crazy or something?"
    me "I'd rather get your neck in my hands!"
    me "So you can stop mocking me!"
    show us smile sport far with dspr
    us "I wasn't mocking you, I really want to help you."
    me "How?!" with vpunch
    us "I've got an iron!"
    "It looked so strange that I stopped."
    me "An iron?"
    show us smile sport at voy_left with move
    us "Yes!"
    "Ulyanka Shouted, warily peering out from behind the railing."
    us "Real one! I brought it with me!"
    th "I'd sooner believe that Slavya has an iron than that little..."
    me "Why?"
    "Stupidly I asked."
    show us laugh sport at left with move
    "Ulyana finally got bolder and came closer."
    us "Why? So that I could arrive clean and tidy in time for their command."
    me "Bad habits in the family, I see."
    us "An officer's granddaughter, an officer's daughter! Jealous!"
    me "Uh-huh."
    me "Do you know how to iron?"
    show us laugh sport with dspr
    us "You ask! You know how I do the arrows on the pants!"
    me "I don't want arrows, I just want my clothes ironed."
    show us smile sport with dspr
    us "Who said I was going to iron?"
    us "Noooo! You do it yourself, and I'll just give you the iron. And you do it in front of me."
    me "But of course..."
    show us normal sport with dspr
    us "I feel guilty. But not that guilty!"
    us "Let's go!"
    "She grabbed my arm and dragged me along."
    with fade
    scene bg ext_house_of_dv_day with blind_l
    play ambience ambience_camp_center_evening fadein 3
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    "We whirled through the camp again, and the careful hostess even managed not to lose her wet, dirty, and crumpled blanket cover anywhere."
    "So she flew around camp - Semyon in one hand, a blanket cover in the other."
    dreamgirl "And broom underneath."
    th "Makes sense!"
    show us normal sport at zenterleft
    us "Give?"
    me "Give what?"
    us "Give me my key, dummie!"
    "I was paralyzed with icy terror for a split second at the thought that I might have drowned the key, too..."
    "But no, nothing happened to it - it was still lying in my right pocket."
    show us laugh sport with dspr
    us "Were you afraid of drowning it? Too bad!"
    "After taking the key from me, Ulyanka tapped me on the forehead with a ladybug."
    "The sound was wooden."
    us "The keychain is hollow on the inside - it would float!"
    play sound sfx_unlock_door_campus
    pause(1)
    us "Aliska's not here, it seems."
    us "Crawl in."
    hide us with dissolve
    "She disappeared out the door."
    "Just in case, after a quick glance around, I followed Ulyanka out the door."
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg int_house_of_dv_day
    with dissolve
    play music music_list["smooth_machine"] fadein 5
    "When I got inside, I saw a most curious picture."
    "Ulyana upside down, with her head under the bed."
    "No, I wasn't at all inspired by her puny strength."
    "It was just funny that a little over an hour ago I was sitting like that, and when I straightened up, I got hit in the face."
    "Plus there's the added urge to get the strap out, strap this little shit, and get off on the soft spots properly."
    dreamgirl "That's not pedagogical."
    us "Lagging again? Come on in."
    "She muttered from under the bed."
    us "Gimme a sec."
    me "Should I lock the door?"
    us "So everyone will wonder what we're doing here?"
    "She giggled."
    us "You can try it!"
    us "Found it!"
    show us smile sport with dissolve
    "Surprisingly, she didn't come out all dusty and cobwebby, as I'd feared."
    "In fact, the last few hours in the little one's company have caused me to change my opinion of her a little."
    "Yes - she's a bloodsucker."
    "But a very disciplined and clean-cut bloodsucker!"
    "She was holding a small iron in her hand, which, as far as I knew, was called either a hiking or a travel iron."
    us "Here!"
    "The girl poked the iron almost in my face."
    us "Are you grateful?"
    me "Very much."
    "I mumbled."
    me "Why don't I take it to my place and give it back to you later?"
    us "No, I don't trust you! And anyway!"
    "She nodded at my bed."
    us "I'll iron everything myself, I won't let you hold anything."
    me "Why is that?"
    show us laugh sport with dspr
    us "Glass - one!"
    "Ulyana began to curl her fingers."
    us "Me and my shorts - two."
    us "The thing you were carrying in your pocket and ended up drowning - three!"
    th "Gee, she noticed the smart..."
    show us laugh2 sport with dspr
    us "If I give you an iron, you'll either break it or lose it. So shish!"
    us "So give me your uniform, I'll iron it myself."
    with flash_red
    me "Are you crazy? We barely got out of one of those messes anyway!"
    show us surp1 sport with dspr
    us "What kind of trouble?"
    me "With your shorts!"
    show us laugh sport with dspr
    us "Phew, shorts."
    "After turning on the iron and setting it on the table, Ulyana turned to me and, putting her finger to the bridge of her nose, clearly cosplaying Viola, stretching her consonants a bit, ordered:"
    us "Get undressed, pioneer."
    th "Seven deaths shall not be..."
    "Doomed, I thought, and began unbuttoning my shirt."
    with fade2
    me "Don't you have anything to eat at least?"
    "We successfully missed our afternoon snack, so my tummy was already feeling a little sick."
    show us grin sport with dspr
    us "Yep, a whole lot of munchies."
    if counter_us_7dl_px == 3:
        us "Or have you suddenly forgotten how we robbed the canteen yesterday?"
        me "Well, maybe? I was just asking."
    elif counter_us_7dl_px == 2:
        us "There's just a little problem with it."
        me "You ate it all, didn't you?"
        "Ulyanka nodded."
    else:
        us "A big pile, yes."
        me "And where is it?"
        us "Eaten!"
        "Ulyana snarled, not turning away from the iron."
        if alt_day5_me_neu_us_potato:
            us "You think I'd accept your potatoes yesterday if I had a supply?"
    show us normal sport with dspr
    us "No food, no."
    "It seems the question was a burning one for more than just me, as she poked the iron particularly viciously into her shorts."
    "There was a hiss."
    "A few more seconds and my shorts flew toward me."
    "I looked them over: quite decently ironed."
    "Talent!"
    th "Not quite, though."
    me "You're a negligent wife, Ulyanka - I wouldn't marry you."
    show us shy sport with dspr
    us "Why is that?"
    "Ulyanka blushed."
    me "Because she managed to iron it! But feed the man?"
    us "What man? You?!"
    me "Me, yes. And you, you negligent one. {w}So we're not getting married."
    me "We're not, yes."
    us "Semyon's fool! {w} What's that got to do with getting married?"
    show us shy2 sport with dissolve
    us "You and I aren't even dating!"
    me "How are we not dating?"
    us "Silently! We're not dating!"
    me "But we spend a lot of time together."
    us "Not really."
    me "We follow each other around for three days in a row! Is that «not really» to you?"
    show us shy sport with dissolve
    us "Well, and?"
    me "Yes! That's what they call dating."
    us "No!"
    me "Yes!"
    us "No!"
    me "I know better! I'm older!"
    show us smile sport with dspr
    us "You're a fool, Syomych, and a scarecrow."
    "Ulka threw me a neckerchief."
    "Now I looked like the handsome man from the Playgirl spread: in shorts and a tie."
    "Well, I wasn't as muscular, but that's okay."
    us "If you don't know, you have to take care of your wife first! My mother's first month my father even carried her in his arms!"
    me "Yeah, you'll be dragged, sure."
    "I snorted."
    me "So all you need to be happy about is climbing into my arms?"
    me "So that's easy for me."
    show us shy sport far with move
    us "Syomych!"
    "Ulyanka shrieked and jumped to the far edge of the table."
    "I didn't move at all, just sat on the edge of her bed."
    th "Nervous."
    me "See, you don't want to."
    us "And you didn't even woo after me at all."
    if counter_us_7dl_px == 2:
        me "I sure did. I even kept an eye on your gang."
        me "And I agreed to go on the work with you yesterday, though I could have refused."
    else:
        me "I'm always helping you with everything, with all your silly things."
        me "What other kind of courtship can there be?"
    show us laugh sport far with dspr
    us "What a suitor!"
    us "SueTor!"
    me "As you are. Lousy beard, lousy head."
    me "Isn't he an eligible groom?"
    show us sad sport far with move
    "Ulyana looked at me helplessly, obviously not knowing what else to say."
    "And then she took a breath in her chest and blurted out:"
    show us laugh2 sport far with dspr
    us "We haven't even kissed once!"
    stop music fadeout 3
    pause(2)
    play music music_7dl["genki"] fadein 1
    show us shy sport far with dspr
    us "Oi..."
    if loki:
        "Ulyanka seemed to be frightened by her own words: she took a step back, pulling her head into her shoulders."
        me "No kiss?"
        "Me grinned."
        me "So it's a fixable thing. Com tse the world."
        "As I was in my playboy bunny uniform, wearing shorts and a naked body tie, I got up."
        me "Kissing in general is highly overrated, but since you insist so much..."
        show us shy2 sport with dspr
        us "I don't insist on anything, Syomych, what are you doing?"
        me "Come here, Come here."
        "I made a move."
        us "Get lost, you bastard! Get lost, I said!"
        show us shy sport with dspr
        us "Don't come any closer, I'll fight! With an iron!"
        us "Somebody save me! Maaaaaaamaaaaaaa!"
        me "Mama is in town."
        "I smirked."
        us "Get lost. Get lost. Get lost!"
        show us fear sport close with move
        us "Don't come any closer! Alisaaaaaa!"
        "Someone came through the door, but only added a step when they heard our voices."
        me "Alisa is not here too."
        "I wasn't hiding a smile anymore."
        hide us
        show cg d6_us_kiss_7dl
        with flash_pink
        play sound sfx_7dl["kissing_sound"]
        pause(3)
        hide cg with dissolve
        pause(0.5)
        show us shy sport with dissolve
        me "That's it, and you were afraid."
        us "You're a brute, Syomych. You bastard. First kiss, and you..."
        me "Appreciate the trust."
        us "Get out of my house."
        me "You're going to iron my shirt and you're going to do it right away."
        us "Boor."
        me "That's where we stand."
        us "Get out when you get your shirt, instantly."
    elif herc:
        me "Hmm, that's true. We must make amends."
        "Ulyanka was embarrassed: she took a step back, pulling her head back into her shoulders."
        us "What are you up to?"
        me "I want to kiss you, Milady! Will you allow me to do so?"
        "I gave a demonstrative bow."
        show us shy2 sport far with dspr
        us "Syomych, what are you doing?"
        "I took a step."
        me "I've been dreaming about it since the first time I saw you!"
        "Ulyana stood as if she were standing still."
        me "You're just an extraordinary girl, Julianne!"
        show us shy2 sport with dspr
        "I took another step."
        me "Forgive me my assertiveness, but you have become my life, my meaning."
        show us shy2 sport close with dspr
        "We were right up against each other."
        "Ulyana just didn't seem to know how to react."
        "Well..."
        hide us
        show cg d6_us_kiss_7dl
        with flash_pink
        play sound sfx_7dl["kissing_sound"]
        pause(3)
        hide cg with dissolve
        pause(0.5)
        show us shy sport with dissolve
        "I stopped hiding the smirk."
        me "That's it, now I'm a real Earl?"
        show us angry sport with dspr
        "Ulyana woke up and immediately changed her face."
        us "You!"
        me "Is something wrong?"
        us "Clown, that's what you are! You ruined such a moment."
        us "Take your shirt and get out!"
    else:
        play sound sfx_angry_ulyana
        with flash_red
        "I felt myself blushing."
        "And here we are, two such red handsomes, looking into each other's eyes."
        "Handsomes."
        "And then I couldn't stand the tension of the moment."
        "Or maybe it was because Ulyana's left eye was starting to squint?"
        "I threw my head back to the ceiling and laughed."
        me "Bruh, what are you saying!"
        show us laugh sport with dspr
        us "And you, yourself! Did you believe it?"
        me "I believed it. But that face of yours, that's just something!"
        us "You should see yourself!"
        "We laughed and laughed at the same time, until Ulyanka, after a moment's hesitation, turned to the iron."
        "A little more and she would have burned my shirt to hell."
        us "So what was that you were saying about marriage, lover boy?"
        me "That I won't marry you."
        us "And I ain't gonna go out with you."
        me "And you're small!"
        us "And you're a barmale!"
        me "And you're a radish!"
        "Ulyana snorted."
    show us smile sport with dspr
    us "Catch."
    play sound sfx_7dl["blanket"]
    "The ironed shirt smelled nice - as only a freshly ironed shirt can smell."
    "But most importantly, it was warm, unabashed, and even relatively clean."
    me "Good girl, Ulyana. Thank you!"
    "From the bottom of my heart I thanked."
    "Ulyana pointedly ignored me."
    me "You're not as bad as I thought you were."
    show us grin sport with dspr
    us "You're not hopeless either. That's it, get out."
    me "Goodbye chat."
    hide us with dissolve
    "I buttoned up, checked my neckerchief and house key, moved my shoulders, getting used to my pressed shirt, and headed for the door."
    "And I was about to grab the knob when I heard a soft voice behind me:"
    us "Syomych."
    "I turned around."
    me "Yes?"
    show us shy sport with dspr
    "Ulyana stood in the middle of the room, crumpling the hem of her T-shirt in her hands."
    "She looked embarrassed, but determined, too."
    "Like she had something important to tell me."
    me "What did you want to say?"
    "Even more embarrassed, the girl looked somewhere in the distance and barely said,"
    us "You know... Today was... fun."
    "A hard confession, right."
    "Even harder than telling your best friend that he's your best friend."
    "For why?"
    "I smiled."
    me "I liked it, too. Too bad, the last one."
    play sound sfx_7dl["eat_horn"] fadein 1
    "The girl wanted to add something else, but she was interrupted by the horn."
    me "There. Now, if my negligent wife won't feed me, I'll go get my own sustenance."
    "A pillow smashed into the door over my head, and I jumped out laughing."
    stop music fadeout 3
    stop sound fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_concert:
    scene bg ext_stage_big_day_7dl with dissolve
    play ambience ambience_medium_crowd_outdoors fadein 2
    play music music_7dl["lastlight_piano"] fadein 3
    if counter_us_7dl_px == 3:
        "Concert."
        "Closing concert - the kids perform in front of the other squads, show off what they've made - and like a fish in water, in this catastrophe, Miku remains the happiest, who certainly doesn't need any escapades or adventures."
        "Why would she do that when she has the adrenaline of the scene?"
        "The people around her, listening to her songs, seeing her off with looks."
        "She's sitting on a needle of public attention."
        "Without it, she would stunt and die."
        th "And without what will I wither and die?"
        "And there is no answer."
        mt "Semyon, straighten up, you're slouching like a poker."
        "I jerked my shoulder in annoyance."
        "Watching the concert, listening to the whispering, singing and clapping to the beat, I didn't feel like it at all."
        "I wanted to go where the creek runs down the slope of the quarry, where it rises to the horizon, and far, far away you can see the highway, which isn't on the map."
    elif (alt_day6_us_7dl_mi_friends == 2) or (alt_day6_us_7dl_sl_friends == 2):
        "Meanwhile, the clock struck four, and the wake-up call from quiet time sounded over the camp."
        "Today it meant something different, today it called the pioneers to take one last look at their friends, to sing a song with them in chorus..."
        "To feel like an integral part of this young, friendly and undoubtedly living organism - Sovyonok Camp."
        "I wasn't expecting any revelations or accomplishments from the concert."
        "I just loved the very thought of sitting alone now - not out of the crowd! Out of the collective! - and there's a girl on stage who I seriously consider a friend."
        "Or rather, a friend."
        "Miku ran off to change, and on some subconscious level I already knew what dress she would return in."
        "I had a certain impression that was hard to fight."
    else:
        "I didn't really understand why I was brought here."
        "Honestly."
        "Unlike the dozens of people who were already seated, cheering, talking excitedly, I didn't feel any emotional lift inside."
        "After all, Alisa and I, unlike them, were not brought here voluntarily."
        "Plus, my mission to rescue one little girl from naked captivity will now be carried out by someone else entirely."
        "Probably the person I'd least like to see in that role."
        "I could almost see with my own eyes as the leader walks into the room, into the second room, sees the exposed glass in the window, and only then turns her gaze to Ulyana."
        "Scarred, crumpled and miserable."
        "Honestly, I was no longer afraid of what the leader might think at that."
        "What I felt more sorry for was Ulyanka."
        "And my one potential ally with the lightning tails pointedly ignored me."
        "She branded me a coward, a traitor - and such people Alisa was used to writing off alive."
        me "Everything is wrong with this camp, everything."
        "I sighed."
    scene bg ext_stage_normal_day
    with dissolve
    "The first squad always sits on the back benches."
    "The rule of thumb is that the little ones can't see anything from a distance, and if the older ones sit in front of them..."
    "So the longest-legged ones get the highest benches."
    "Although it would be more fun to sit where the sound guy sits."
    "You could also swear into the microphone and demand that the stage be cleared."
    "Working while others are having fun."
    "Cruel."
    "The benches were filling up little by little - the squad leader and PE teacher knew their business and were catching pioneers all over the camp at the level of internal affairs commissars."
    show sl smile pioneer with dissolve
    sl "Resting?"
    "I raised an eyebrow questioningly."
    sl "This concert is special to me."
    "Slavya confessed."
    sl "And not just for me."
    if alt_day6_us_7dl_un_friends > 0:
        sl "I heard you found Lena?"
        "I was confused."
        show sl smile2 pioneer with dspr
        sl "I knew right away that you wouldn't clean up."
        sl "So... Did you find her?"
        "I nodded."
        sl "Good. So she's all right, and she'll show up to the dance for sure."
        me "What's she got to do with it?"
        show sl shy pioneer with dspr
        sl "How can I tell you..."
        sl "We have a lot in common, really."
        sl "More importantly, this year for me and for her..."
    show sl serious pioneer with dspr
    sl "With the exception of only Ulyana, the entire first squad will never return to camp again."
    sl "So this is a special farewell evening, after which it's all over."
    me "Life goes on."
    "Philosophically, I remarked, and Slavya shook her head and lowered her voice."
    sl "Life goes on, but next year only Olga Dmitrievna and Ulyana will be left."
    if counter_us_7dl_px >= 1:
        me "And her guardsmen too."
        "Slavya nodded."
    sl "Okay, we'll talk later, it's starting already."
    hide sl with dissolve
    "The girl sat aside, leaving me alone with the music and Miku popping up on stage."
    show mi normal voca far with dissolve
    mi "Hey, Camp!"
    "Miku shouted into the microphone."
    mi "How's the mood?"
    "Camp mumbled something indistinctly, but the Japanese girl was satisfied with that answer."
    "Got herself a sweet tooth."
    "So it was hard to accuse her of somewhat ignoring the audience's reaction."
    "So be it."
    if alt_day6_us_7dl_mi_friends == 2:
        th "I wonder if she's going to sing that song she showed me at the club?"
        "The phono in the background was playing pretty sad, so it seemed unlikely to me that the concert would open with a minor tune."
        "That's pretty weird, I think."
        "And Miku didn't disappoint."
    else:
        "I hadn't known the Japanese girl long enough to make any predictions, but the way she walked, the way she held herself, the way she spoke..."
        "Everything about her was not just a stage lover, but a fierce professional."
        "Who, on top of everything else, loves what she does."
    stop music fadeout 3
    scene bg ext_stage_big_day_7dl
    with fade
    "The piano tunes fell silent, and silence fell over the camp for a fraction of a second."
    play music music_7dl["bad_apple"] fadein 3
    "Which immediately was literally swept away by a sound totally out of place, time even..!"
    "The compressor, the broken drumming, the rolling bass - it sounded more like music from somewhere in the raves of my half-forgotten homeland."
    "But Miku knew and liked that music."
    "What's more, she was going to sing along to it!"
    "She didn't seem to have any prejudices about it."
    "Moreover, she was holding her hand with the microphone in such a way that it was obvious that specifically for this song she was accustomed to a hanging «tendril» freeing her hands."
    "But even with one busy hand, she managed to give off some very, very good choreography!"
    "Well, as far as I could tell, of course."
    "And yet!"
    "I could definitely see some of her moves in some of the dances that were already modern to me - from the robot dance to the «butt step» from tectonics."
    "The unsophisticated spectators around me weren't trying to show off for who knows what and were just enjoying a really cool show."
    stop music fadeout 10
    "But all good things must come to an end."
    "Miku's performance ended, too."
    "And after her..."
    play music music_list["reflection_on_water"] fadein 3
    "Everything seemed bland and poorly rehearsed."
    if alt_day6_us_7dl_mi_friends == 2:
        "And this despite the fact that each of them was given the opportunity to prepare properly, allocated time on stage..."
    if counter_us_7dl_px == 3:
        "I fidgeted, looking around, Ulyana and the boys were nowhere to be seen."
        "It seems they decided to take a chance and stay in the story with-an-alien-side."
        "So I was abandoned, leaving only the possibility of hiding the worries in the Forest of Memory, as a legacy."
        "I felt like the streets of my native cloudy capital again: there were lots of people around, and they were happy, cheerful, purposeful."
        "And it only shaded my own loneliness."
        "It seems that the only person who could have been a real friend to me preferred a fairy tale than my dreary society."
        me "No wonder."
        "I squealed."
        if alt_day6_us_7dl_px_sl_join:
            show sl shy pioneer close with dissolve
            sl "Pouting again?"
            "Slavya crouched close to me again, and the whisper of her breath scorched my ear."
            "It tickled the tingle, but somehow it was unsettling and made me want to move away."
            sl "In fact, I would have been ready to leave with you even when you asked."
            "She opened her blue eyes, and I realized suddenly that she wasn't lying."
            "Not because of her eyes, but because she doesn't know how to."
            "It's as if she has the attitude to always tell only the truth."
            me "So why didn't you?"
            show sl sad pioneer close with dspr
            "Slavya got sad:"
            sl "Responsibility. Yes, I know, I sound like a nerd."
            sl "Like I'm forty years old, I'm a granny with a bag that only knows how to grouch."
            me "You certainly don't sound like a granny."
            show sl smile pioneer close with dspr
            sl "Thanks."
            me "You say nerdy things anyway, though."
            show sl sad pioneer close with dspr
            sl "I can't do it any other way. It just doesn't work."
            "Some boy in a starched shirt came on stage and sat down at the piano, so Slavya moved even closer to me, almost touching my ear with her lips."
            me "And if it doesn't work out this time too?"
            show sl smile pioneer close with dspr
            sl "This time it will work out. Remember what I told you?"
            sl "This is the last time I'm here, so I want to try to do something that I don't regret remembering."
            "She smiled quietly in response to my leering look."
            sl "I know that Ulyana and her buddies know how to do something impossible, that they have found something incredible."
            me "And that's why you want to join in?"
            show sl sad pioneer close with dspr
            sl "Looks mercantile, doesn't it?"
            me "Well, yes."
            "I snorted."
            me "Aren't you too old to believe all that nonsense?"
            show sl shy pioneer close with dspr
            sl "And you?"
            "She parried."
            "I couldn't think of an answer."
            "Strictly speaking, we were, if not the same age, then kinda close."
            "There was nothing for me or Slavya to catch in Ulyanka's tale."
            sl "Then I had a whole reason to try to run away with you."
            me "What was it?"
            "At this time, the distempered piano faded, and the speakers, in Miku's voice, announced:"
            dy "The concert closes with a song sung by Feoktistova Slavyana!"
            show sl smile pioneer with dissolve
            "Slavya, rising easily, shook my fingers."
            "Smiled:"
            sl "This. I hate performing."
            hide sl with dissolve
            "She hurried toward the stage, leaving me alone with my loneliness and conscience."
        else:
            mt "Syomych, Syomych..."
            "Squad leader sighed, sitting down next to me."
            show mt normal pioneer with dissolve
            mt "And why are you so lightheaded?"
            me "I'm heavyheaded I'd say."
            "Instantly I bristled."
            me "The heaviest even."
            show mt sad pioneer with dspr
            mt "I see..."
            "Squad leader answered very vaguely."
            mt "I see."
            show mt normal pioneer with dspr
            mt "You're trying to get mixed up in something you don't understand."
            me "As if you understand."
            show mt smile pioneer with dspr
            mt "Yeah, I know a thing or two."
            me "You?!"
            "The skepticism in my voice could have poisoned half the local river."
            mt "What's wrong with that? Melt-Melt, all that... I've been through it all, Semyon."
            mt "I grew up."
            me "I see. Thank you. Congratulations. A heartfelt shake your - manly? Feminine? I can't decide."
            show mt laugh pioneer with dspr
            mt "And you're still the same pest."
            mt "But I'll tell you one name, and you'll understand."
            me "What name?"
            show mt normal pioneer with dspr
            mt "Mirya."
            me "Ahem."
            "I nodded warily, watching as Miku climbed once more onto the stage, ignoring the leader's menacing glances."
            mt "I see this name is familiar to you."
            "Olga continued as the tapping of percussion broke into the silence."
            me "It is."
            "I didn't deny it."
            me "Mirya, or Dima Mironov, your brother."
            me "But which one, the older or the younger one?"
            "For some reason I clarified."
            show mt laugh pioneer with dspr
            mt "What's the difference? The main thing is that I know something about your ships."
            mt "And how they work, too."
            with fade2
            mt "Don't be a sourpuss, Syomych. In fact, I'm not accusing you of anything."
            mt "I even support you in some ways. It wasn't you who started the search, was it?"
            "I cautiously cleared my throat, keeping my eyes on Miku, who had finished singing."
            "In her place stomped some nerd in glasses and a shirt - more than obviously a musician."
            if loki:
                "Chamberlain."
            "And so it was: he went to the piano, opened the lid, and put his hands over the keys."
            me "But I took part in them entirely voluntarily. So I would ask."
            show mt grin pioneer with dspr
            mt "The request is denied. Slavya."
            "She called to the girl sitting nearby."
            mt "You close the concert, get ready."
            "Slavya nodded without much enthusiasm."
            show mt normal pioneer with dspr
            mt "And to you, Semyon, I ask only one thing. Please, I'm begging you."
            mt "Don't do anything stupid."
            mt "Can you promise me that?"
            "And how can you promise something like that? Or demand to promise something like that?"
            "What nonsense."
            me "I don't know."
            "A dry throat wheezed."
            me "I'll think about it."
            mt "That's good enough for me."
    elif (alt_day6_us_7dl_mi_friends == 2) or (alt_day6_us_7dl_sl_friends == 2):
        "But since I came here of my own free will..."
        if alt_day6_us_7dl_mi_friends == 2:
            "Since I personally helped prepare all this..."
        "I'll have to drink the cup to the bottom."
        show mi serious voca far with dissolve
        "I saw Miku turn around, looking for someone in the crowd."
        "Completely unknowingly, I raised my hand and waved, drawing attention."
        "Miku glared and waved both hands invitingly."
        "Well, I had to get up and make my way through the crowd."
        show mi smile voca with dissolve
        mi "So, how's it going?"
        "Miku looked extremely pleased with herself and what was happening on stage."
        me "Why are you here and not at the console?"
        show mi laugh voca with dspr
        mi "There will be poems now, followed by a performance on the piano."
        mi "My services are not needed."
        me "Poems? Without a microphone?"
        "I didn't believe it."
        show mi happy voca with dspr
        mi "Yes! Dunno if you remember or not - there was one boy in the third squad who thought that the louder you yell a march, the better."
        mi "He was convinced that it was better to read poetry."
        show mi grin voca with dspr
        "Miku giggled into her palm:"
        mi "And with his voice he doesn't need any amplification at all."
        me "I see gloating in your speech."
        me "The path leads to the dark side!"
        show mi surprise voca with dspr
        mi "You know that, too?! What an interesting boy you are, Senechka!"
        "It would be strange if I didn't know the cinematic classics. Especially since the first three parts came out about ten years ago."
        "Then I noticed that we'd been talking for a couple of minutes and no one was coming on stage."
        show mi sad voca with dspr
        mi "It's the same as always - first we shout the loudest, then we're afraid to go on stage."
        "Miku looked extremely annoyed."
        me "Now what?"
        mi "Nothing."
        show mi serious voca with dspr
        "She shook her head, expressing disapproval."
        mi "I'll go perform instead of him, that's all."
        mi "Like it's the first time, heh..."
        me "You like performing, don't you?"
        mi "I like performing. The inconstant screamers I don't like. Bye!"
        hide mi with dissolve
        "Catching Olga Dmitrievna's nod, Miku started the paused phonograph tape and jumped on stage."
        "Looks like she's going to get her full fifteen minutes of fame tonight."
        "I didn't see anything wrong with that."
        "Especially from the place I now held as assistant art of director."
        "But everything comes to an end."
        "Miku's performance ended, too."
        "She smiled at me and stood next to me, but didn't say anything."
        "And a couple of minutes later I realized why she wasn't sitting down - performing Slavya, appeared to be wrapping up the concert."
        "So we looked at each other, turned off the equipment, and, while the pioneers were sorting themselves out by squad, we unplugged the most important cords."
        "And only after that did we go out to the canteen."
    else:
        th "Just let me escape - I won't miss my chance!"
        "We exchanged glances with Dvachevskaya - she seemed to have had exactly the same thought."
        "We grinned synchronously."
        with fade2
        "But who would let..."
        "On the left was the second squad leader, and on the right, Sanich."
        "Both of them were dancing to the music, applauding the young talents, but never for a moment losing kindness in their squint."
        "So I had to sit back and be quiet."
        "The only thing that brightened the picture a little was Ulyana, whom Olga brought in half an hour later - red, embarrassed, and indignant."
        "She flopped down on the bench beside me, crossed her arms over her chest, and did not respond to careful questioning."
        "Must have been offended."
        "But everything has an end, even concerts."
        "Some fellow with a music folder and a bow-tie came out on the stage."
        "He was replaced by Slavya with some folkloric howls - and, finally, Olga Light Dmitrievna uttered her most coveted phrase:"
        mt "The concert is declared closed, squads, march to dinner."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_supper:
    scene
    $ renpy.show("bg ext_dining_hall_away_day", what = Dawn("bg ext_dining_hall_away_day"))
    with dissolve
    play sound_loop ambience_medium_crowd_outdoors fadein 2
    play ambience ambience_camp_center_evening fadein 4
    play music music_list["trapped_in_dreams"] fadein 3
    "There was a small line at the cafeteria door, so I stood apart, leaning my shoulder against the wall of the cafeteria."
    "Shoving to get your portion of potatoes and meat before anyone else?"
    "I'm sorry. Not my case."
    if alt_day6_us_7dl_sl_friends == 2:
        "A few minutes later, Slavya stopped next to me."
        show sl surprise pioneer with dspr
        sl "Escaped preparations?"
        "Semi-confidently she inquired."
        me "No. No one told me anything."
        sl "Very strange. Usually, if there's a disco after the concert, they always gather us to help out."
        sl "You know, take something to the square, hook it up..."
        me "No. I think Olga Dmitrievna would make an announcement if she wanted us to participate, don't you think?"
        show sl shy pioneer with dspr
        sl "I ran away, too."
        "In confidence informed the girl."
        sl "As soon as she finished performing, she went right..."
        me "You?!"
        "I didn't believe it."
        sl "I don't like to perform."
        "The girl admitted it."
        sl "There was a choice, either to put on another Miku song or leave a hole of three minutes."
        me "Do you really dislike her performances that much?"
        show sl laugh pioneer with dspr
        sl "What are you saying, of course I like them."
        sl "I'd love to give way to someone who's at least good at it."
        me "So what happened?"
        show sl sad pioneer with dspr
        sl "Olga Dmitrievna banned."
        "Slavya sighed."
        sl "Said Miku had too many performances as it was, there was nothing for her..."
        sl "Why didn't you perform by the way?"
        me "I couldn't think of anything, simply."
        if loki:
            "Although I could have done something for them, like that goofball in the starched shirt."
        me "And anyway, I don't like performing."
        show sl smile pioneer with dspr
        sl "I see."
        sl "I wish I could wag my finger at you right now and tell you to make sure you do it next time."
        me "Except there won't be a next time."
        "I nodded understandingly."
        me "And that's okay. It's not only about performances..."
        hide sl with dissolve
        "We were silent for a while, looking at each other and smiling."
        "I suddenly caught myself thinking that I felt surprisingly serene and warm at heart around this girl."
        "Like that sun over the sands that can both kill and scorch away all that is harmful and unnecessary from the soul and body, leaving only a tanned shell and an eternally youthful gaze."
        "I had once deduced a simple tenet."
        "If a person makes you feel at ease and silent, grab them in an arm and drag them to you."
        "Lift them up in your arms, for across the doorstep you must carry them in your arms and only so."
        "Of course..."
        "How else can you bring happiness into the house?"
        "But Slavya is not my happiness. We parted like ships at sea."
        "From the first moments of our acquaintance, while we exchanged studying glances, I should have begun to hollow out a path to her heart."
        "Then perhaps we could have had something more than we have now."
        "Yes, man is a god in the subjunctive mood."
        "I wasn't complaining, though. I was fine with what was already going on between me and this pretty girl."
        if loki:
            "The most important thing was that I didn't feel any anger from her!"
            "I wanted to catch her by the hand and ask her to stay - dunno why."
            "Looking for faults in her: just because there can't be a perfect person!"
            "And in the end just make one up for her."
            "Because it's pressing to see a flaw in an icy image."
            "You can't fall in love without it."
            "Just... Wanted to."
            "But as it happens, I chose my own loneliness, and I'm not interested in anything but it."
            "People did their best. Perfectly handsome, lively, cheerful."
            "I should crawl into my shell, where there's a gun and a note from the girl from my dreams waiting under my pillow."
            "Even my foolish vendetta, I finished it out of nothing but an empty and misplaced desire to always finish what I started."
        else:
            "I had never before interacted with people like her."
            "Moreover, I suspected that in ordinary life someone like me was simply not interesting to her."
            "There was no self-deprecation in understanding this simple fact."
            "It's just that there are human beings, there are non-human beings."
            "And while I've often heard that everyone gets the reality they deserve..."
            "All I've always heard in this, is that you choose your own rails on a daily basis."
            "Take a little turn off the beaten-path and you'll see that the world is much bigger than your washed-out horizon, that it has never grown with you, but has always been huge."
            "Slavya would have had enough powder to turn the arrow of her ways every day."
            "And I... Well, I was really lucky to meet a person I didn't fully believe existed myself."
        stop sound_loop fadeout 5
        show sl smile pioneer with dissolve
        "The pioneers slowly dispersed in front of the entrance, making way for the older squads, and Slavya pushed me with her elbow."
        sl "Let's go refuel before the last dance!"
    elif alt_day6_us_7dl_mi_friends == 2:
        "Something's mixed up somewhere."
        "And not in my head."
        if (alt_day2_date == 'mi') or (counter_mi_7dl == 2):
            "Someone must have just decided to give me another chance?"
            "Things didn't seem to start out so bad for me and Miku."
            "I was the one who was dumb, and she was the one who was excited about me!"
        else:
            "For example, it was completely incomprehensible to me how it happened, that we were hand in hand with one Japanese star stomping through dinner in the pioneer canteen."
        "Sounds surreal, doesn't it?"
        "But Miku didn't seem embarrassed by it at all."
        show mi smile voca with dissolve
        mi "Well done!"
        me "Don't you feel bad going to dinner in a dress?"
        mi "No way."
        "Miku waved off."
        mi "Nothing will happen to it, I know how to eat carefully!"
        mi "And if I do get dirty, the fabric is dirt-repellent! Super, right?"
        me "Super, of course."
        "Deeply thoughtful I nodded."
        me "You're going to the disco in that, too?"
        show mi shy voca with dspr
        mi "No, of course, who do you take me for?"
        "Miku go a little embarrassed."
        mi "I was just too lazy to go home to change into my uniform, then go home again after dinner to get dressed up for the dance. So much running around, Uh!"
        me "Bummer."
        "I smiled."
        show mi smile voca with dspr
        mi "Why a bum? It's just not-ex-pe-di-ent!"
        "The Japanese spelled it out."
        mi "But I'm taking a risk, of course."
        me "What do you mean?"
        show mi happy voca with dspr
        mi "You probably don't know this, but on the first day of my shift I got kicked out of the canteen from dinner."
        mi "They scolded me, saying my dress was too short, and told me to go change."
        "I took a step back and looked around at the girl."
        show mi sad voca with dspr
        mi "And don't look so closely! The dress is the same, but you know how low I had to put the skirt on!"
        "Miku angrily informed."
        mi "I have a rubber band almost on my knees to «cover my shame»."
        mi "It's like I'm walking around naked!"
        me "And you're not?"
        show mi laugh voca with dspr
        mi "Senya!"
        mi "Quite a decent suit with a skirt. What's wrong?"
        me "I kind of like everything."
        "I basically liked every outfit she wore. Including the Godzilla head."
        "It looked really nice on her."
        me "I just couldn't help myself."
        me "I'm sorry."
        show mi normal voca with dspr
        "Miku waved it off:"
        mi "I've gotten used to your constant jokes."
        mi "At first I thought it was because you were mean, but you're not mean at all."
        show mi smile voca with dspr
        mi "So now I don't know how to react to it. I'm resigned to it."
        "Immediacy in all its glory."
        "Miku kept saying something else."
        "I was listening to the voice."
        "For some time now, we were already connected by some threads."
        "Indistinguishable, but already unbreakable."
        "Or rather, in the case of my star, I would not call them binding threads..."
        "But binding strings."
        "Between us stretched taut strings of nerves, fluttering in the wind, playing a strange solo that made me want to cry and laugh at the same time."
        "I wouldn't call it a love, but I certainly liked her."
        "What's more, I already knew very definitely who I was going to ask to the slow dance tonight."
        stop sound_loop fadeout 5
        "But that's later, and for now I'm listening to her talk."
        "Not a bad way to brighten up the wait for dinner."
        show mi happy voca with dspr
        mi "Path is open! Cheers!"
        hide mi with dissolve
        "She rushed into the canteen, shouting and chanting something about workers' children and hungry growing bodies."
        "Chuckling, I followed her."
    elif counter_us_7dl_px == 3:
        "I summarized, not finding the girls at dinner either."
        "Potatoes and meat, a glass of milk - a distorted reflection of my first day here."
        "Like an episode of a sitcom in which the hero begins and ends the series in exactly the same position: if he found a million dollars, he'll give it away; if he gained powers, he'll inevitably lose them."
        "The simplest condition is that both he himself and his soul must meet the credits wearing exactly the same gray sweater as they came out on the stage in the beginning."
        "Otherwise it's a development, not a sitcom."
        "Miku was cracking something under her side, but I wasn't really listening, all busy feeling sorry for myself, reveling in my own, carefully cherished loneliness and longing."
        "And the fact that there's even a disco coming up, and it's like the last weekend of summer: the very chance to do something I've been meaning to do all summer - but never got around to."
    else:
        "Ulyana wanted to run into the crowd, elbow and knee everybody, but I stopped her, putting my hand on her shoulder."
        show us dontlike sport with dspr
        us "What?"
        "I nodded at the approaching squad leader."
        "I didn't want to provoke a conflict, since we would immediately be reminded of our constant absence from camp activities."
        "Yes, we all have something to learn."
        "We don't really have any other choice."
        "For me, to stop being a nuisance."
        "And Ulyana... No. She's a little more human than I am."
        show us sad sport with dspr
        us "Boring."
        "She complained, leaning against the wall with her back right in front of me."
        if alt_day6_us_7dl_help:
            us "Now it's time to shake and dance!"
            me "You can dance?"
            show us laugh sport with dspr
            us "You bet! I've had some teachers!"
            "She started, but then she faded away."
            show us calml sport with dspr
            us "They taught me the polka, the waltz and the minuet, but they didn't teach me how to dance in a disco!"
            us "And why do I even need teachers like that then?"
            me "There are all kinds of dances..."
            us "I had to peep how others move. And repeat."
            me "It works?"
            show us surp1 sport with dspr
            us "How would I know?"
            us "I just dance the way I like."
            "Squad leader on the horizon spotted us and started pushing in closer to say a few nice things."
            "But who'd let her..."
            "The pioneers were standing tight and rushing into the canteen as soon as a seat became available."
            "So the leader just powerlessly waved her fist at us from afar."
            me "A very frightening threat."
        else:
            show us normal sport with dspr
            us "Actually, I should be pouting at you for leaving a damsel in distress."
            me "If it were up to me..."
            show us upset sport with dspr
            us "You didn't try hard enough! You should try harder!"
            me "I don't understand a bit."
            "I started it."
            me "Are you asking me to fight with the squad leader?"
            me "For the honorable right to carry you a change of clothes instead of a concert?"
            show us laugh2 sport with dspr
            us "Why fight? We could just sneak past them!"
            us "Or just run away!"
            "No, she's definitely a long way from human."
            "Olga was still gone, so we weren't in much of a hurry to move."
            me "I see. Well, if you want to be offended, be offended. I'll understand."
            show us laugh sport with dspr
            us "And I won't!"
            me "Can't understand you!"
            us "You don't have to! You have plenty of other virtues!"
            me "What are they?"
            show us smile sport with dspr
            us "Here!"
            "She spread her palm out and began to curl her fingers:"
            us "You're sensible! And calm! And... and..."
            show us surp3 sport with dspr
            us "Hey! Why am I complimenting you? It should be the other way around!"
            me "We have equal rights here!"
            show us smile sport with dspr
            us "Equal lefts."
            "Ulyana poked her tongue at me."
        show us laugh sport with dspr
        "We laughed."
        "And fell silent."
        show us shy sport with dspr
        us "Syomych, hey Syomych?"
        me "In touch."
        "I waved my paw lazily."
        us "And you... Well..."
        me "Me, me. What?"
        show us shy2 sport with dspr
        us "You're going to the disco, aren't you?"
        me "Even if I didn't want to, I have to."
        show us surp1 sport with dspr
        us "Why?"
        me "Because Olga Dmitrievna."
        show us sad sport with dspr
        us "A..."
        me "Why do you ask?"
        us "No reason. I'm just asking. I'm going."
        if loki or herc:
            me "Are you hinting at a slow dance?"
            "I cold-bloodedly clarified."
            me "No problem, I will invite you."
            show us laugh2 sport with dspr
            "Ulyanka blushed, but smiled far too contentedly."
            me "Since you feel like it."
        else:
            "There was an awkward silence."
            me "Really, I can't dance at all."
            show us surp1 sport with dspr
            us "You - and you don't know how?"
            me "What's the big deal?"
            if alt_day3_dancing1 != 'me_1':
                us "You danced at the last disco!"
                me "Is that dancing? It's just... stomping around."
                show us laugh2 sport with dspr
                us "I always knew you were a bear."
                me "Thank you."
            else:
                us "I remember your outfit. You look just like a dandy. So overgrown."
                me "Thank you. I've never been called a dandy before."
            show us laugh sport with dspr
            us "Don't pout! Well, do you want me to teach you how to move your arms?"
            me "Not really."
            "That prospect didn't inspire me at all."
            me "I don't want to learn the local fast dances at all."
            us "What about slow dances?"
            me "You'll see at the disco!"
        stop sound_loop fadeout 3
        "Ulyana took a swing at me, but then I discovered that while we were talking, the pioneers had already dispersed."
        me "Hooray! Consuuume! On the assault!"
        hide us with dspr
        "I shouted and rushed toward the canteen."
        "Behind me, there was a bounce, and a moment later my stomping was joined by the clatter of small heels."
    stop music fadeout 3
    scene bg int_dining_hall_people_sunset_7dl
    with dissolve
    play ambience ambience_dining_hall_full fadein 3
    play music music_list["smooth_machine"] fadein 3
    "The canteen was buzzing and crackling behind my ears."
    "It was hard for me to understand one thing, why to make living space for sixty people and a dining room for forty."
    "Encouraging natural selection?"
    "Whoever had time to eat?"
    "Anyway, this time I was not allowed to choose with whom and where to sit - moreover, the pioneers who had already had time to pick up their tray sat down, as they call it, «by cooldown», and the pioneers on duty were sewn up, not having time to collect the dishes."
    "So I got an aisle to seat."
    "On the left, squad six was still chewing; on the right, squad three was just sitting down."
    "There wasn't even anyone to talk to."
    "With a sigh, I put my spoon in my plate."
    "For lack of alternatives, I had to do what I came here to do."
    "To eat."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_disco_prepare:
    scene anim_square_preparty with dissolve
    play music music_list["lightness"] fadein 5
    play ambience ambience_medium_crowd_outdoors
    if alt_day6_us_7dl_un_friends == 2:
        "Sometimes I feel like it's all made up around me."
        "That people waste time on things they're not interested in at all just because someone else made it up."
        "Like dancing, for instance."
        "I didn't want to go. Didn't want to."
        "And neither did I want to use those conventions."
        "But this morning at the quarry, those very conventions helped me shake up one green-eyed loner."
        "I don't know if she'll keep her promise, but..."
        "I'm sure I will now. {w} I have no right not to."
    "By the time I got to the square, she was already fully prepared for the event to come."
    if alt_day6_us_7dl_help:
        "The people had their share of bread, and now they were hungry for entertainment."
    else:
        "And the pioneers were more enthusiastic about the event than the last concert!"
        "Of course, there are exceptions..."
        "One of those exceptions was staring at me and smiling:"
    show mi smile voca with dissolve
    mi "Senya, I have a surprise for you!"
    me "I hate surprises."
    "I grumbled."
    show mi happy voca with dspr
    mi "And you're going to love this one, that's for sure!"
    me "I doubt it would be a million dollars."
    if alt_day6_us_7dl_help:
        th "Or at least a smart, to replace the drowned one."
    show mt smile pioneer at zenterright
    show mi normal voca at left with move
    mt "Miku made you a nice costume for the dance."
    if counter_mi_7dl == 2:
        me "The same as last time?"
        show mi happy voca with dspr
        mi "Fully washed and ironed!"
        me "Well, ironed..."
        "I didn't hold back a chuckle."
        me "You got me!"
    else:
        me "Yeah? That's great. But what makes you think I'm going to wear it?"
        th "One hundred percent, some kind of homoerotic with frilly jabots."
        "I didn't know much about the leaders's predilections, but for some reason I firmly thought the costume would represent some kind of gayness."
        show mt angry pioneer
        show mi upset voca
        with dspr
        mt "Semyon, stop being capricious. You have to go to the farewell disco dressed up."
        me "Who needs it?"
        me "Why should I?"
        "I got furious."
        me "Give me one reason why I should dress in what you made up for me?"
        show mt sad pioneer with dspr
        mt "The first reason is that it took me half an hour before I ironed and tidied it."
        me "I'm sorry for your loss."
        "I nodded."
        me "Is that all?"
        "And turned around already, to leave."
    if alt_day6_us_7dl_mi_friends == 2:
        show mt normal pioneer at cleft behind mi
        show mi normal voca
        with move
        if counter_mi_7dl == 2:
            mi "You'll be the most dressed up person on the dances again!"
            th "If it would help me in any way..."
            dreamgirl "There's an opinion that only a head pill by Cobain will help you."
            dreamgirl "Because if a man is an idiot, it's for a long time!"
            th "What's wrong?"
            dreamgirl "Oh, that's it."
            me "So I'm going to go change?"
        else:
            mt "And the second reason is her."
            "Olga Dmitrievna put her hand on Miku's shoulder."
            mt "Since you don't respect my work, respect hers."
            show mi sad voca with dissolve
            mi "It's really beautiful, it'll suit you very well."
            "They both looked at me in anticipation."
            "And I gave up."
            me "Okay."
            "I didn't want to give in, but under team pressure..."
            me "I'll go see what the costume is."
            show mi happy voca with dspr
            mi "Yes!"
            me "But if there's some kind of ruched thing... I won't wear that."
        mt "Go, go."
        "Olga nodded."
    elif alt_day6_us_7dl_sl_friends == 2:
        mt "Don't you want to dance with Slavya tonight?"
        "Squad leader asked my back."
        me "Slavya is perfectly okay with uniform."
        me "Or not. But what does the costume have to do with it?"
        "The squad leader couldn't find an answer."
    elif alt_day6_us_7dl_un_friends == 2:
        mt "How about asking your girlfriend to dance?"
        if loki:
            me "She doesn't dance.."
        else:
            "I was silent, and for a moment I was glad that I had already turned away."
            "My cheeks flushed."
    else:
        mt "But you're must to be dressed up at the dance!"
        me "Why must? Who said so?"
        me "I don't want to go to any of your damn dances."
        me "The only reason I go is because I don't want to be brought there by force."
        me "So what the hell difference does it make what I'll be wearing, if I don't want to be there?"
        "With a satisfied nod, I withdrew."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade2
    play sound sfx_open_dooor_campus_1
    pause(1)
    return

label alt_day6_us_7dl_makeup:
    scene bg int_house_of_mt_sunset with diam
    play music music_7dl["someone_like_you_guitar"] fadein 3
    play ambience ambience_int_cabin_evening fadein 2
    "The cabin was empty and lonely."
    "It was the same as always - scattered things, dust particles playing in the sunset rays, and the spirit of a place where one comes only to spend the night."
    "For curiosity's sake, I decided to see what Miku and Olga had in store for me."
    if alt_day6_us_7dl_mi_friends == 2:
        "What if they really didn't lie?"
        "To please Miku by dancing with her dressed up... There was something about that."
    else:
        "I didn't plan to wear it, but just to please the curiousity..."
    play sound sfx_open_cabinet_2
    "As I opened the flap of the closet, I looked around at what was offered to me as an evening tuxedo."
    if counter_mi_7dl == 2:
        "Same cool dark-colored suit and a pair of shoes that had already been carefully polished."
    else:
        "It really wasn't all that sad."
        "A dark, sheeny burgundy shirt, slacks smoothed down to sharp arrows, and boots - my size - that came out of nowhere."
    "I even remembered the name of them."
    me "Mocassins."
    me "I'm going to put these on, mop up my haircut and walk around the square in style."
    dreamgirl "All the girls will be yours!"
    th "Not interested."
    "I cut it off."
    if alt_day6_us_7dl_mi_friends == 2:
        "Not interested in all of them."
        "But one..."
        dreamgirl "Are you going to put it on or what?"
        me "I will. What can else can I do."
        "The clothes were all a little too small."
        "Although in my case it wasn't critical: I wasn't going to break-dance, I wasn't going to wave my arms around."
        "And for stomping around the square woodenly, cradling one sad-eyed Japanese hottie, that was enough."
        "After I got dressed and manicured, I straightened up and took a critical look at myself in the mirror."
        scene cg d3_me_mirror_bordo_7dl
        with dissolve
        "Nothing has changed in appearance."
        "Except a little calmer compared to the one who looked like that three days ago."
        "And compared to someone who still calls himself «I»..."
        "Not all changes are for the better, no doubt. But I was happy with this one in particular."
        "If you add to that the fact that there's a girl who wants my attention, it's a total disaster."
        "It's like winning a car in the lottery, and you get a forehead: «wait a minute, there's a prize from the audience!»"
        "And they bring me out a box with what that suit should have been."
        dreamgirl "In your dreams."
        th "I agree."
        th "To hell with a million. Give me Miku."
        scene bg int_house_of_mt_sunset
        with dissolve
        "After admiring myself one more time, looking into my eyes and finding no despair at the bottom, I slammed my locker shut."
        "Something was waiting for me, and I was anticipating that «something»."
    else:
        "I decided for myself that I wasn't going to wear anything."
        "You might say I went on principle."
        dreamgirl "An idiotic and stupid principle."
        th "What can I do if my principles are basically what I have left?"
        dreamgirl "Shoot yourself and vacate the living space, for example?"
        th "An option too, ye."
        "Actually, I didn't know why I came here in the first place."
        "I could have wandered around the camp, seen how life was boiling around."
        "I'm sitting here instead, hiding from prying eyes."
        "I'm wondering if I should lock myself in from the inside so it doesn't get too sour."
        dreamgirl "Why is it sour?"
        th "I don't know."
        "I snapped."
        if (alt_day6_us_7dl_un_friends > 0) or (counter_us_7dl_px == 3):
            "I was embarrassed and burdened by a certain sense of loss, of missed opportunities."
            "No, I'm already on the plus side, no matter what the outcome."
            "My life is richer by one person who means something to me."
            if alt_day6_us_7dl_help or (counter_us_7dl_px == 3):
                "Ulyana was a kind of forget-me-not: they stay in your memory no matter what happens to you."
            else:
                "Lena has become a person I want to please for some reason."
                "I don't know why, but I had an irresistible urge to bring a smile to her face."
            "But there was something beyond that."
            "As if chasing the unfulfilled, I missed the chance to get something... I don't even know."
            "A bigger one? Less? Just different?"
            "Like a teenager growing up in an information vacuum, feeling the love longing inherent in his age, can't explain to himself - what's going on with him."
            "Alive, healthy, fed, cheerful, doing what he loves; and still something weighs on him."
            "I was like that teenager, only unlike him, I didn't have any longing."
            "It wasn't a noble sadness that was weighing on me, but the most bourgeois greed."
            "I wanted everything at once."
            if alt_day6_us_7dl_un_friends > 0:
                if alt_day6_us_7dl_help:
                    "I wanted a faithful friend, a role for which Ulyana was perfectly suited."
                    "Wanted a fiancee, from whose format Ulyana fell completely out."
                else:
                    "I wanted Lena - without unnecessary fidgeting, running outside the camp territory, and «happily ever after»."
                    "I wanted «together forever,» but it was like when I was a kid - suddenly, I couldn't imagine the enormity of the years ahead."
                    "And together with Lena, I must walk through them."
                    "What if she doesn't agree?"
                "I've never had much luck with girls, though."
                "So let's skip that point and calm our hormones."
            else:
                "However, it all sounded somewhere on the periphery of my consciousness, not bothering me at all."
                "The instincts and needs that had moved me before sounded muffled in the background, and far more concerned with making sure the people around me were nice and didn't swear too much."
                "So my greed was purely speculative."
        else:
            "I wanted to run away from camp and lock myself in here for the whole disco at the same time."
            "I wanted to go crazy and invite all the girls of our squad, including Alisa and Zhenya."
            "I wanted to get drunk and run away with the boys to the shore-slope, to burn fires until morning and sing about being sad and funny and spinning memories..."
            "And in the morning to fall asleep, smiling happily into the busy dawn, to wake up to the shouts of a pushing squad leader and realize that this is it..."
            "It's the last time."
            "Damn it. The last time."
            th "I did have it once, didn't I?"
            "That was my «last» time, which I successfully mourned and buried in the depths of my memory, preoccupied with far more important things."
            if loki:
                "By love and revenge."
                "By revenge and death."
            else:
                "Trying to survive."
                "Trying to make myself feel something every day."
            "And in all that, I somehow lost sight of the fact that I was forgetting to do the most important thing."
            "I was forgetting to live."
            "And now all this unlived stuff was swinging back at me and kicking me in the gut, knocking the air out with mixed thoughts."
            "I wanted to do something I can remember."
            "Even if I woke up and realized I'd been freezing over the wheel of my bus the whole time."
            "I want to remember something."
        "As I decided on my desires, I suddenly realized how much easier it became."
        "Turns out it's not a bad therapy for moping either."
        "Just sitting down and sorting out your head."
        "After winking at myself in the mirror, I closed the door and went outside."
    stop music fadeout 3
    play sound sfx_open_dooor_campus_1
    pause(1)
    return

label alt_day6_us_7dl_disco:
    scene anim_square_party with dissolve
    play ambience ambience_camp_center_evening fadein 3
    play music music_7dl["beat_symphonic"] fadein 3
    "Meanwhile, the dancing had already begun."
    "There weren't too many people on the set, most of them preferring to sit on the side for now."
    "But soon, very soon..."
    "Our squad were all here, too."
    if counter_us_7dl_px == 3:
        "All who was missing was Ulyana and Lena."
        "After looking around for a squad leader and earning my affirmative nod, I made myself comfortable on the bench."
    else:
        "Ulyanka was already wriggling almost at the speakers."
        th "Unspoiled child, eh."
        "After admiring her grimaces for a while, I smiled and sat down on the bench."
    "This time the host decided to put on something that even I thought was danceable enough."
    "So for a couple of minutes I went through the «try not to stomp on the beat» challenge."
    "It was hard to do, to be honest."
    "On the other hand, and all sorts of nonsense, like unnecessary reflexions and torments were ruthlessly banished from my mind."
    "Not bad therapy, if you put it that way."
    "I made a note to get some better headphones with good bass response in case I get a mopey future."
    "And kicking out with super-low frequencies what's not supposed to be there."
    "Feeling someone's gaze, I looked up."
    if alt_day6_us_7dl_mi_friends == 2:
        show mi smile dress with dissolve
        "Miku didn't cheat.."
        if (alt_day3_dancing1 == 'mi_1') or (alt_day3_dancing2 in ('mi_2', 'mi_12')):
            "I've seen this dress before, and it hasn't gotten any worse since."
            "It's also plain on the face of it, but it emphasizes everything that needs to be emphasized."
        else:
            "The dress she changed into looked even better than the one she performed in."
        "Intercepting my gaze, she laughed and shook her head, beckoning."
    elif counter_us_7dl_px >= 1:
        show dn grin pioneer
        show al smile pioneer at left
        show tn laugh pioneer at right
        with dissolve
        "Ulyanka's guard was here in full force, too."
        "Danechka, in his unchanged disheveled uniform, was either a helicopter or a tectonic dancer."
        "He shouted something."
        "«Let's dance», I read his lips."
    else:
        show sl happy dress with dissolve
        "Slavya was having the time of her life."
        "And unlike Ulyanka's awkward knees, Slavya's looked pretty decent."
        "She was the one who was looking at me and, catching my gaze, she smiled and beckoned me with her hand."
    "I shook my head negatively."
    "Although the music was somewhat more decent than expected, I was by no means in a hurry to dance."
    scene anim_square_party with dissolve
    "No, I used to go to discos back in the day, and I even danced there along with the others."
    "But now I wasn't in the mood."
    show mt smile dress with dissolve
    mt "Why aren't you dancing?"
    "Squad leader, who happened to be nearby, asked."
    "Without asking permission, she plopped down next to me - almost on my lap."
    me "I'm not much of a dancer."
    show mt grin dress with dissolve
    mt "Disco is a social event!"
    me "Well, you know!"
    show mt laugh dress with dspr
    mt "Just kidding, just kidding, Syomych. Why are you so tense."
    mt "I'm not going to force you to dance if you don't want to."
    me "Wow..."
    me "What happened to you? Got sick?"
    show mt smile dress with dissolve
    mt "You can think what you want about me, Semyon, but you have to understand one thing."
    mt "I'm an educator. I know how to get someone to do something."
    mt "But I also know when not to make him do it."
    me "And when is that?"
    show mt grin dress with dspr
    mt "When people are having fun for example."
    mt "I can't make you have fun and be happy."
    me "You can't."
    "I nodded Accordingly."
    show mt normal dress with dspr
    mt "Besides, as I see it, you're already quite satisfied - you're waving your haer to the beat."
    me "Haer?!"
    show mt laugh dress with dspr
    pause(.3)
    hide mt with easeoutleft
    "Olga laughed, jumped off the bench and got lost in the crowd of dancers."
    stop music fadeout 2
    "Only after listening I understood why."
    play music music_7dl["stilllovingyou"] fadein 3
    "I was even a little taken aback when the painfully familiar tunes came out of the speakers."
    "A song that has been making people's hearts beat in unison for decades."
    return

label alt_day6_us_7dl_us_dancing:
    scene anim_square_party with dissolve
    "I got up and went looking for Ulyana on the benches."
    "And soon found her."
    me "Let's dance?"
    if alt_day6_us_7dl_un_friends == 2:
        "That's a question I should have asked Lena, since I called her out on it."
        "I guess I was not nice to her."
        "Well, it doesn't really matter anymore."
        "It's Ulyana who matters."
    show us smile dress with dissolve
    us "Are you really going to dance?"
    if loki:
        "I smiled as broadly as I could:"
        me "After everything you've done to me, you owe to marry me."
        show us laugh dress with dspr
        us "No way! We've been through marriage before!"
        me "See, you don't even want to get married."
        me "Eh, Sadge that I don't have a folder with a shotgun to force you."
        "Ulyana rose from the bench:"
        us "My father has an Reward-PM. Will it do instead of a shotgun?"
        me "Quite. Are you going dancing?"
    elif dr:
        "I was embarrassed."
        "No, it wasn't any trouble for me to come up and ask."
        "It was just enough to remind myself of the age difference."
        "Yeah the fact that I don't really care much about her romantically."
        dreamgirl "Don't care?"
        "The inner voice inquired, ingratiatingly."
        dreamgirl "Not at all? Not even a little bit?"
        me "You don't want to?"
    if herc:
        "I straightened up and put on a noble expression."
        me "Milady, will you give me a dance on this fine evening?"
        show us laugh2 dress with dspr
        us "Stop the wriggling, rookie! It won't work a second time."
        me "Won't it work, you sure?"
        us "It definitely won't next time!"
    else:
        show us laugh2 dress with dspr
        us "No. I don't want to. And anyway, where are your manners?"
        us "What's a «Let's dance» huh?"
        me "Oh, excuse me. May I have permission to ask you to dance?"
        show us smile dress close with dissolve
        us "There! That's better already."
        "She prodded her elbow, and I immediately remembered her words about the ballet school of dance."
        th "Mamselle."
        "I thought with amused anger."
        "And dragged her to the dance floor."
    scene cg d6_us_dance_7dl
    with dissolve
    "We pushed through to the very middle, accompanied by stares and, in some places, hooting."
    "Ulyana was definitely known, definitely loved."
    "Such a strange child, who somehow appeared in the first squad."
    "Leaving all her friends in the others."
    "Ulyana was shorter than me, so I had to slouch habitually already, let her put her hand on my shoulder."
    us "Calancha."
    "Girl giggled."
    us "You must be uncomfortable?"
    me "It's okay."
    us "Maybe I just get on your neck and dance like this?"
    me "How about you don't whine and we just dance?"
    us "You're mean."
    "Mumbled Ulyana, catching my hand in a honed motion."
    "I used to be able to doubt her words, but that's only possible through long practice."
    "So she didn't lie?"
    "We joined the crowd spinning in the dance and were silent for a while, trying to get used to each other."
    with fade
    me "I believe now"
    us "Believe what?"
    me "That you took dance lessons, didn't lie."
    us "Hey, I rarely lie at all. Almost never."
    me "You?!"
    us "What's wrong? When have I ever lied to you?"
    "There was no need to think about it here:"
    me "Well, when you dragged me to «save» me!"
    me "As a result, I got a bad report card from Rizhevskaya."
    us "But got a cold compress all over your body!"
    "The girl giggled."
    us "There won't be a bruise now."
    me "It's not your merit."
    "Ulyana wondered:"
    us "How is that, not mine?"
    us "Who do you think took you there?"
    me "You didn't! I was chasing you in the first place."
    us "There! My mother told me «Act natural and the boys would follow you around»."
    us "Herds or not, there's one running!"
    us "I'm going the right way!"
    if loki or herc:
        me "And not just running."
        us "Yeah..."
        "She gave me a strange look."
        us "You were so used to hitting on me! Many years of experience?"
        th "None, really."
        th "The dozen years given to a man to be fully socialized, I simply missed it."
        th "Tirelessly and senselessly."
        "My mood began to roll into the negative, and fleeing from the boredom that came over me, I shook my head."
        me "What kind of experience is there if it was all mutual."
        us "Mutu... what?"
        me "Mutually, I say. When a boy wants it, a girl wants it."
        us "I didn't want anything! You did it all by yourself! By force!"
        me "Murderer and rapist, yes."
        us "Well, yes you are!"
        "It finally dawned on her that I was just kidding, and she went quiet for a while, pouting."
        "As a matter of fact, she didn't let go of my hands, and she wasn't in any hurry to leave."
    else:
        me "I'm not running at all."
        us "But you're looking for my attention, aren't you?"
        me "I'm not looking at all!"
        us "You're repeating yourself."
        "Ulyana pointed out ."
        me "That's because you're trying to knock me off my feet."
        us "I don't knock you off anywhere, it's just that you can't dance."
        th "Rrrr..."
        me "You just like to mock me, admit it."
        "Ulyana smiled, answering nothing."
        th "They're definitely taught that."
        th "They've been taught since they were kids. In a special school for women."
        "I guessed it."
    with fade2
    "After thirty seconds, I got tired of being silent:"
    me "Aren't you going to tell me how you got into the first squad?"
    us "Do you think I'm too bad for first squad?"
    me "You're younger than the other pioneers."
    us "I knew it! Age! Age again!"
    us "So what if I'm younger! I run faster than anyone else! And I do my work just as well as anybody else."
    if alt_day2_us_escape:
        me "Equal."
        "I was forced to admit it."
    else:
        me "The work of running away, maybe."
        me "And cake-eating."
        us "I forgive you this time."
        "Girl graciously nodded."
    me "Come on, stop being offended. I was just asking."
    us "You sure know how to ask questions, Syomych."
    "Ulyana looked at me unhappily."
    us "I can feel the incrimination."
    me "What?"
    us "It's when people are forbidden to do something. {w}They say «you're too small» or «you're too big.»"
    us "Or «you're a girl.»"
    me "Ah, discrimination."
    us "That's right. Boring, stupid word. Who invented it?"
    me "Don't talk back to me."
    us "Maybe I don't want to answer!"
    me "Some big secret? Scary secret?"
    "She was so reluctant to answer, the more I got curious."
    "That's right, the more closely guarded the secret, the more interesting it is."
    "Ulyana, on the other hand, was as silent as a partisan, so I stepped up the pressure a little:"
    me "If you don't want to tell me, don't tell me. I'm not interested at all."
    me "So what, in the first squad."
    "Of course she couldn't take it."
    "Of course she didn't."
    us "I just have a friend here!"
    me "Alisa? It's not much of an occasion, to be honest."
    me "You could be friends even if you were in different squads."
    me "I'm telling you, I have a lot of experience with that."
    us "No."
    "Ulyana was embarrassed."
    us "Not her."
    us "Oh, I mean, she's too, but she's not the first."
    me "Not the first?"
    us "Aunt Olya called me."
    "At last Ulyana confessed."
    us "I've been in her squad for years, so we're always together."
    th "And why hide it?"
    me "What's the big secret here?"
    us "Yeah, it's that you... oops. No."
    "She shook her head."
    us "Don't even ask! I won't tell."
    me "Why not?!"
    us "Look, why don't you ask me about something else?"
    us "What do you usually do? What do you like, what don't you like?"
    us "Go on, woo a girl."
    "I nodded."
    me "And what do you like?"
    us "I know what I don't like."
    me "Stupid questions?"
    stop music fadeout 3
    scene anim_square_party
    show us sad dress
    with dissolve
    "The music faded smoothly, and we let go of our hands."
    us "And you had to ruin it."
    me "What?"
    us "You're a fool, Syomych. Stooge."
    "Shaking her head, Ulyana went somewhere away."
    play music music_7dl["unfulfilled"] fadein 3
    $ persistent.sprite_time = "night"
    $ night_time()
    scene bg ext_backdoor_night_7dl with clock_r
    play ambience ambience_camp_entrance_night fadein 3
    "I was able to find Ulyana again only half an hour later."
    "And even then, with difficulty."
    "By the same inexplicable instinct that told me where to look for her."
    "She was sitting on a log by the left gateframe, looking thoughtfully at something beneath her feet."
    "When I came closer, she didn't even move."
    "As if she hadn't noticed."
    "After hesitating, I sat down next to her."
    "From here, life seemed like a leisurely flow, where you could do whatever you liked, as much as you liked, with enough time to do it all."
    "It was as if the flaps had cut off the frantic life of the camp from us, which had hissed and left the two of us alone on the sand."
    "And it's so strange and funny that there are so many interesting people my age around."
    "Intelligent, interesting, beautiful. Readable, after all."
    "And I still chose to communicate with a child."
    th "Could it be because I still haven't grown up myself?"
    "I demanded an answer from the silent stars."
    "They remained silent, as the well-bred stars should, continuing to wink at me indifferently from above."
    "The song of the cricket was heard from somewhere in the distance, the surrounding bushes were lined with fireflies, and it seemed as if the night had no beginning and no end, and we could sit here for a very long time."
    "Yes, it was as if we had actually been sitting there."
    me "Mademoiselle, may I address you?"
    "Remembering her «lesson in good manners», I began."
    show us normal dress with dspr
    us "What a gallant gentleman."
    "Unhappily Ulyana smiled."
    me "A deceiver, yes."
    us "Tell me, do you have to pry into someone else's soul?"
    me "No. But I'm interested."
    me "I'm interested in you."
    show us sad dress with dspr
    us "That's the problem. You're prying into things you're not asked to."
    us "I don't know how else to tell you to stop."
    me "But it's just a squad issue!"
    show us smile dress with dspr
    us "I have nothing more to add."
    us "We're friends with Auntie Olya, my dad trusts her, I'm in her squad."
    us "That's all."
    me "What's the big deal?"
    us "Will you stop asking me questions now?"
    if loki:
        me "Only for one more kiss."
        us "Stop it!"
        me "But it's just a kiss. One. A quick one."
        me "You know, the kind that doesn't commit to anything."
        me "Though of course I don't insist. You're so disgusted!"
    elif herc:
        me "No, I won't."
        us "Mind your own business!"
    else:
        me "If I'm that annoying to you..."
        "I twitched my shoulder."
        me "I'd better go."
    hide us with dissolve
    "And no matter how hard I tried to feel sincere and honest..."
    "I felt like a manipulator."
    "Playing on the psychology of a child, working backwards and, in fact, getting what I wanted."
    "But I wasn't her teacher to get that deep inside."
    "It was a stretch to call me even a friend."
    "But I honestly tried to get up and leave."
    "Honestly."
    "Even took a few steps."
    with fade2
    us "Hey."
    "There was a muffled voice."
    "I stopped."
    us "You're a creepy bore, you know that?"
    me "I know."
    us "You make me do strange things."
    me "I didn't do it on purpose."
    us "Close your eyes."
    me "Are you gonna hit me?"
    us "Close your eyes, I say!"
    show blink
    "I had to obey."
    us "Don't peek."
    "Her voice came from somewhere very close, and I could hardly keep my eyelids from fluttering open."
    scene cg d5_us_kiss_dress_7dl
    with flash_pink
    "I felt something wet and soft touch my cheek."
    "And immediately I opened my eyes."
    th "Wow."
    scene bg ext_backdoor_night_7dl
    show us shy dress
    with dissolve
    us "I told you not to peek!"
    hide us with easeoutleft
    me "I'm not ..."
    "I didn't have time to finish, because I found myself alone."
    me "That's it."
    "My ears and cheeks were burning, but my expression must have been very pleased!"
    "There was no more pulling to the disco, so my way was to my home, my favorite cabin."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_no_dancing:
    scene anim_square_party with dissolve
    "I got up and went looking for Ulyana on the benches."
    "And soon found her."
    me "Are you going to dance?"
    "Ulyana looked me over from head to toe and jumped."
    show us laugh dress with dissolve
    us "Dance? With you?"
    me "What's wrong?"
    if loki or herc:
        me "You were the one who was hinting."
    else:
        me "Do I displease you in some way?"
    show us laugh2 dress with dspr
    us "Shall we hold hands and dance hands?"
    us "Or will you lean over and I'll tiptoe over to hug your neck?"
    me "We'll think of something."
    "Undeterred, I replied."
    show us smile dress with dspr
    us "No way, Syomych. I won't dance with you."
    "She sat down on the bench and folded her arms across her chest, letting me know that the conversation was over."
    me "But why?!"
    me "We're having such a great time together!"
    show us shy dress with dspr
    us "Exactly. That's great. So let's not spoil it."
    us "I'd go dancing with you, but you're bound to think of something stupid."
    show us shy2 dress with dspr
    us "I don't want to."
    me "Your will."
    "I sighed."
    hide us with dissolve
    "I, too, returned to my bench."
    with fade
    "Dancing looks dull and boring if you don't have anyone to wiggle with."
    "No one to tease."
    "Just to have some company."
    "But dancing alone..."
    "I got up from the bench, went to Genda, hid behind his pedestal and was sad with the General Secretary himself."
    "But he, unlike me, was trying to understand far more important things - for instance, why does a man need a man?"
    me "I'm still loving you..."
    "With one lip I sang, and the thought that I had essentially no one to say those words hit me."
    "It hurt for some reason."
    "The mood was finally ruined."
    "And I knew it was time to leave."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_un_dancing:
    scene anim_square_party with dissolve
    "I got up and went looking for Lena on the benches."
    "The problem was, no matter how many times I looked for Lena, I couldn't find her."
    "There, somewhere in the back of the street, I glimpsed familiar tails, and I went there, she wasn't there."
    th "You didn't dare? Find something more interesting to do?"
    "I had given up hope and was about to leave when a familiar voice came from behind me:"
    un "D-do you want to dance?"
    show un shy dress with dissolve
    if counter_un_7dl >= 5:
        un "R-remember, a song like then..."
    "A hesitant voice, twitching ponytails..."
    th "It cost someone no small effort just to say one word to me."
    if counter_un_7dl >= 5:
        me "Of course. {w}It's not possible to say no to a girl when «Scorps» are there!"
    else:
        un "Y-you i-invited me."
        me "Yes. Let's go, Lena."
    show un smile dress with dspr
    "Smiling, the sad girl let me take her hand and lead her to the dance floor."
    "We shifted hands awkwardly for a few seconds, until finally I embraced her in a waltz-like grip that was as old as the world."
    scene cg d3_un_dance
    with fade
    me "You called me just in time."
    "I shared."
    un "W-why?"
    "She was looking anywhere - at the dancers, at the sky... As long as it wasn't in my eyes."
    me "I was just about to leave. So just a few more seconds, that's it."
    un "Y-yeah, lucky me."
    "Her back was stiff, and the girl herself was very tense."
    me "Are you uncomfortable?"
    un "W-well, no..."
    "She wanted to say something else, but she shook."
    "So I decided not to torment her, and we danced in silence for a minute."
    un "Have you been looking for me since this morning?"
    "Finally, Lena broke the silence."
    me "Looking..."
    un "Why-why?"
    me "I don't know."
    "I sighed."
    me "You can call it nonsense, but I wanted to see you."
    me "To find you."
    me "Somehow it seemed very wrong for you to be alone."
    un "I'm not afraid of being alone."
    me "It's not about being alone. {w}You know, I've been thinking about you."
    if alt_day2_date == 'un':
        un "And it seemed to me that you just stopped being interested."
    else:
        us "For six days you hadn't thought, and now suddenly..."
    "She whispered, but I heard."
    if alt_day2_date == 'un':
        me "I thought you just didn't like me. {w}Forgive a fool, eh?"
    else:
        me "That's how slow I am. Sorry."
    un "For what?"
    "Lena raised her surprised eyes."
    "And this time she didn't look away. She even stopped trembling."
    un "You have nothing to apologize for."
    me "I think I do."
    me "And those hearts on the quarry... I think they make some sense..."
    un "There's your name on there, too."
    me "Is that so?"
    un "I cut it out."
    "I wanted to say something, but I didn't have time."
    "Lena pressed herself against me as hard as she could, squeezing my hands until they hurt."
    "No, there were no tears, no fear."
    "She just froze, stiffened, huddled as if some big trouble was about to happen."
    "And I, too, froze, afraid to even breathe."
    "There wasn't a person in these universes I wanted to understand and protect like that."
    "From what?"
    "I don't know."
    "Not from me, not from myself."
    "From the world?"
    "And it got bad because I couldn't figure out how."
    un "I ran away because there are too many of you in my life."
    me "But... I'm..."
    un "There's a lot you don't know. Just trust me."
    un "And that's what I ran away from today."
    "Her speech straightened out, as if these were the exact words she had repeated in her head many, many hundreds of times."
    "Rehearsing before the crucial speech."
    "And there it was."
    un "And you found me for some reason."
    un "Now you don't know why."
    me "So what? So now you've asked me to a slow dance."
    me "It's a sign of attention, for which I'm really grateful."
    un "H habit."
    me "Asking the boys to dance?"
    un "Not boys."
    "Lena shook her head."
    un "You."
    stop music fadeout 3
    scene anim_square_party
    show un serious dress
    with dissolve
    pause(1)
    un "Get me out of here, please. {w}My legs can't hold me."
    me "But where?"
    show un smile dress with dissolve
    un "Wherever you want."
    "With a smile, the girl whispered."
    $ persistent.sprite_time = "night"
    $ night_time()
    scene bg ext_un_hideout_night_7dl
    with touch
    play music music_7dl["pixies_playing"] fadein 3
    play ambience ambience_lake_shore_night fadein 5
    "At some point it turned out that it wasn't me who was leading her."
    "It was her, taking my hand, guiding and pointing the way."
    "Fingers trembling, tenderness mixed with panic in her eyes."
    "She was like a wild animal who had become disillusioned with human kindness."
    "And now it was up to me to tame her again."
    th "And do I even need to?"
    show un normal dress with dissolve
    if loki and (alt_day2_date == 'un'):
        un "Remember this place?"
    else:
        un "This is my second favorite place at the camp."
    "Lena ran her hands over the sprawling wild beach, relegated to lazy waves from a lonely growing crooked pine tree."
    un "I look at the waves and calm."
    if loki and (alt_day2_date == 'un'):
        "I nodded."
        me "It's probably silly to say this now, but... Thank you for trusting me."
        me "Even though I acted like a pig after all."
    else:
        un "I never took anyone here. Never."
        me "So I'm a pioneer here? A pioneer heh."
    show un shy dress with dspr
    un "Just don't think I'm saying this to everyone."
    un "It's really, really hard for me to talk to you like this, eye to eye."
    me "Turn around then?"
    "Half-jokingly, I suggested."
    "And Lena took it seriously."
    hide un with dissolve
    "After looking around, she spotted a pine tree and, taking my hand, led me uphill."
    "Her actions seemed determined enough, though it was obvious that the girl was desperately nervous."
    "Here's looking for an opportunity to help herself a little."
    "So when I was on one side of the pine tree and she was on the other and exhaling in relief, I knew the conversation was yet to come."
    scene cg d5_un_dress_island_7dl
    with fade
    un "You know, I've read so many books on the subject."
    un "I dreamed that everything would be like there - love at first sight, happy reunited lovers..."
    un "But for what happened to me - to us - the books didn't prepare me for that."
    me "What happened?"
    un "Semyon."
    "Lena turned to me seriously."
    if alt_day4_me_neu_date == 'un':
        un "You said yourself that we only knew each other for a little while."
        un "Don't you remember anything?"
        me "Don't remember what?"
    else:
        un "How long have we known each other?"
        me "I don't know... six days?"
    un "Third year, Semyon. And last year we were together."
    un "You left me, Semyon. You didn't leave me for someone else, you just left me."
    if alt_day4_me_neu_date == 'un':
        un "I don't know why you never remembered anything, but..."
        un "It seemed to me that everything that happened last year would still remain as that."
    else:
        me "But I don't remember any of that!"
        un "I know."
    with fade
    un "Then there was a gigantic scandal, I was forbidden to come near you, so as not to make things worse."
    un "And how much worse could it get..."
    un "So I forbade myself to come near you. I thought if I couldn't, I would just watch from a distance."
    un "Maybe I'll be a part of your happiness, just standing on the sidelines."
    "Her voice trembled."
    un "Only there was no happiness. And I don't know what to do now!"
    if alt_day2_date == 'un':
        un "And suddenly you paid attention to me, you asked me out on a date."
        un "Why did you ask me out, and then you pretended like it was nothing."
    else:
        un "You are neither mine nor somebody's else! And I'm afraid even just to touch you."
    un "And it hurts a lot."
    un "When I want to laugh with your laughter, cry with your tears."
    "Her voice broke off, and she was silent."
    "And I was silent myself. I listened and did not know how to help this girl, who had made up all sorts of nonsense for herself and believed it sacredly."
    "If I were ten years younger, if I didn't know that she hadn't invented anything new, that all this had already been suffered by mankind, I would have stood there now and kept quiet."
    "Which is exactly what I'm doing now."
    "But the difference is that I see the mask with which she covered the old pain, which she should have let go - but she keeps fingering the wound."
    me "And that's why you've wasted so much time?"
    un "What?"
    me "Instead of just coming up and holding out your hand."
    if alt_day2_date == 'un':
        un "And I approached you."
        me "No, I approached you, and it was like you accepted my advances, and the next morning you just shrugged it off."
        me "You know, this is all new to me, and I look at you as a half-stranger."
        me "A very beautiful half-stranger I know nothing about."
        un "Then maybe I should ask you."
        me "So we'll sit on different shores, waiting for the other to make the first move."
        me "It doesn't work that way. It never has."
    th "You're so afraid I'll feel sorry for you, you silly girl in love."
    th "And you're even more afraid because you realize somewhere inside that it's empathy that you need the most right now."
    "With some incomprehensible exasperation, I muttered to myself."
    th "And quite to the point of panic is the thought that one day you will have to cast off your mask as no longer necessary. You will have to stand naked against the world, to become part of it..."
    th "And having dissolved into real feelings, realize: there was never any point in this behavior."
    th "To realize that you were wrong - and then, by obeying some strangers rather than your own heart."
    th "And now."
    un "I am afraid, Semyon."
    un "I painted you. I wrote you poems."
    un "Why is everything so wrong? It should have been the other way around - a handsome boy, walking me home, reading me poems, giving me flowers."
    un "To hell with the flowers. You were supposed to be mine."
    un "Selfish, eh?"
    th "What am I supposed to do now?"
    "Frantically I pondered, ignoring the tree bark that had burrowed into the skin of my palm to the point of pain."
    th "I don't know, I can't, I'm incompetent to save a girl from herself!"
    th "Especially a young girl who hasn't yet established herself as a human being."
    th "You need a soul mate and a humanologist of no lesser caliber than Violetta Cernovna, and what kind of a rescuer am I?"
    me "A man can't be somebody's, otherwise he ends up being a human."
    un "And I don't care!"
    "Girl exhaled."
    un "I want, want to hug your face with my palms, search your lips and understand what you think of me."
    un "Not to think about all that nonsense, but just to touch."
    menu:
        "So what is stopping you?":
            "Lena was silent for a few minutes."
            "And just as I was about to remind myself, she looked up:"
            un "W-what?"
            me "I'm saying... If you feel like it - touch it."
            th "Let's pretend we're eighteen again, that we're drunk with each other, and the world around us simply doesn't exist."
            th "Only it's not «again» for you."
            th "That's the saddest thing."
            th "That's the worst part."
            th "That you're not eighteen, not even twenty-three - catching happiness out of thin air."
            th "What a convenient time it was!"
            th "You could console yourself with the nonsense of your youth - that you didn't need girls, that love was invented by the idle impotents of the poets' union, that life was over and it was time to go on a reset."
            th "Holy time."
            th "But when you've been given a second chance, and you yourself can't figure out how old you really are, it's somehow very easy to accept the fact that you can't do without her anymore, and you don't know what to do about it. What to do with yourself."
            th "That's it."
            "A few steps around the tree."
            scene bg ext_un_hideout_night_7dl
            show un serious dress
            with dissolve
            "Lena stopped in front of me, sat down, and looked into my eyes for a few seconds."
            "I don't know what she was looking for, but for a moment it was as if her inner rod had been taken out."
            hide un with dissolve
            "She threw herself on my chest and cried."
            un "God..."
            "She repeated."
            un "What a fool I am, God. How much time I've wasted."
            me "Why wasted? I'm still here."
            un "Yes. You're here."
            un "For some reason I want to dive into you and trust you like I've never trusted anyone before."
            un "I'm a total psychopath, aren't I?"
            me "No."
            "I was hugging her and I didn't want to waste my energy and time on idle chitchat."
            me "It's just that you..."
            "My voice trailed off."
            me "Love."
            un "Yes."
            "She murmured, taking her time to get out of my embrace."
            un "L-o-v-e."
            "She didn't ask me for reciprocity, and I was grateful for that."
            "Young love is generous, she is happy just by the fact."
            "Everything else starts much later."
            "Though Lena has had it for a year now."
            un "Will you kiss me?"
            me "You need it?"
            "Lena took her head off my chest and looked into my eyes."
            un "Very much."
            "Her tone was murderously serious."
            "And I kissed her."
            $ alt_day6_us_7dl_un_friends = 3
            scene black with dissolve2
        "But for what purpose?":
            us "So it wouldn't be so empty."
            "Lena squeezed her eyes shut and whispered:"
            un "And so painful."
            me "I'm sorry."
            un "It's nothing."
            "There seemed to be a reason for her sadness, there was..."
            un "I'm used to it."
            un "Walk me home, okay?"
            "It was the least I could do for her."
            "I got up off the ground and held out my hand to Lena."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_mi_dancing:
    scene anim_square_party with dissolve
    "So I got up and went looking for my partner on the benches."
    "And soon found her."
    show mi smile dress with dissolve
    "Miku waved at me from across the square and jumped up somehow in a flash."
    mi "Let's go! Let's dance! Let's go!"
    "She dragged me to the dance floor."
    scene cg d3_mi_dance_afar_bordo_7dl
    with dissolve
    "We stomped in place for a few seconds before Miku broke the silence:"
    mi "What's on your mind, Senya?"
    me "The hell I know."
    "My head was blank, so why not share?"
    me "Nonsense comes into my head."
    mi "Really?"
    "Her eyes lit up."
    mi "Like what?"
    me "Like the letter «S»."
    "For some reason, the fifth element came to mind."
    me "It's a wonderful letter!"
    mi "And what's so great about it?"
    me "There are a lot of great words that start with it."
    mi "What kind?"
    me "Sunny. Strong."
    me "Crazy beautiful."
    mi "Semyon."
    "Miku tipped off."
    me "Yea, Semyon too."
    th "Actually, I'm thinking of you, vocaloid girl."
    "Even as I was sitting on the bench, trying to figure out how I knew that choreography, that clapping of palms over my head, and the way you was acting in general, I started to remember something."
    "Until on an associative chain, I pulled from my memory millions of YouTube views, enchanting vocals and lyrics too deep for such a girl."
    "She. Miku-yamaha, singing in the voice of a seiyu, but no less beautiful from that."
    th "Now that I remember who and what you are, it gives me goosebumps to dance with you."
    th "To hold you in my arms, to feel your body - alive."
    dreamgirl "peeking through your cleavage."
    th "That too."
    "I agreed."
    "The crazy idea of kissing her popped into my head."
    "Right there on the dance floor."
    "But Miku ruined it by smiling contentedly and laying her head on my shoulder."
    mi "It's calm with you. Peaceful. You're phlegmatic, Senya."
    me "Maybe."
    mi "And, for some reason, I like it so much... And you?"
    me "I like you."
    "I confessed."
    mi "What about your young girlfriend?"
    me "What are you saying! My girlfriend is just a friend."
    me "She's just a kid. Though I don't argue, she'll grow up to be a beauty."
    mi "Yes."
    me "Like you. And kind, like you."
    mi "You overdo it, Senya. I'll get proud, and pull my nose up."
    "Miku quietly laughed."
    me "All right, I won't. You're ugly and mean."
    "Miku laughed."
    mi "Now that's better. I was starting to get a little nervous, even from what you said."
    me "Why?"
    mi "Because it doesn't happen like that, that I'd sit through an entire shift and then you'd come in - and turn out to be so... So... I don't know!"
    mi "It bothers me."
    me "It's okay."
    "I patted her on the shoulder."
    me "I'm shy around you, too. But that's not a bad thing either."
    me "Shows that I care."
    mi "You have an answer for everything."
    "She laughed."
    "Instead of answering, I pressed her against me a little harder."
    "That answer suited me much better."
    "Vocaloid Girl. A digital goddess, existing only on the expanse of the Internet and in the solutions of holoprojector screens."
    "How many millions of people would lay down their left fangs to be in my shoes right now?"
    "To see her in the flesh."
    "Real, laughing. Alive."
    "To see the vein of her neck pounding, to smell the eucalyptus her hair smells faintly of."
    "Just to hear her voice - the moonlight silver, the bells."
    me "Can I invite you again?"
    mi "Do you think you should?"
    me "I wish I could."
    "Miku thought about it, and then said."
    mi "I'd like to go on a date."
    me "Romantic?"
    mi "Yes. With you."
    me "Candlelight dinner, soft music, red wine?"
    mi "No, you could just hold my hand and go for a walk."
    if (alt_day2_date == 'mi'):
        me "We've already had one of those, with a walk."
        mi "There! I can't get enough, I want more!"
    mi "I'm starved for attention, Senya."
    "She complained."
    me "Easy."
    stop music fadeout 5
    "I agreed when the music ended and the dancers stretched back toward the square."
    scene anim_square_party
    show mi smile dress
    with dissolve
    me "Let's go."
    mi "Right now? Really?"
    me "Why not? Let's go."
    "Miku put her hand in mine and ordered."
    mi "Lead on."
    $ persistent.sprite_time = "night"
    $ night_time()
    scene bg ext_admins_night_7dl with dissolve
    play music music_7dl["lastlight_piano"] fadein 3
    play ambience ambience_camp_center_night fadein 5
    "We didn't go far at all."
    "Just a little bit, toward the administration building."
    "But it was hard to hear the sounds from the dance floor, so we could hear each other's breathing."
    "Listening for footsteps."
    "Smiling at how trusting the girl you're with."
    show mi normal dress with dissolve
    me "You know, there's a place here that almost nobody knows about."
    mi "Will you show me?"
    me "That's where I'm going."
    "We walked around the front of the administration, and I, after a few seconds of war with the pawl, unlocked the wicket and waved invitingly."
    me "Please!"
    scene bg ext_stairs_night_7dl
    with dissolve
    mi "It's great here."
    "Miku noticed, shaking off the step and sitting down next to me."
    mi "No one can see you, but you can see everyone from above."
    me "Yes. The best seats."
    "Miku put her head on my shoulder again."
    "Smiled dreamily:"
    mi "Who would have thought it would end like this."
    if (alt_day2_date == 'mi') or (counter_mi_7dl == 2):
        mi "That one day someone like this would knock on the door and I would feel easy and relaxed with him."
        me "It's a little late to propose dating."
        mi "It's never too late, Senechka."
        "Girl rubbed her cheek against my shoulder and smiled dreamily."
        mi "And it's never too early."
        mi "You know, even then, when we met, I suddenly realized that I couldn't let you go!"
        mi "That if anyone could be a true friend to me, it was you!"
    else:
        mi "That I would be cooped up for three weeks and then one day, just one day I would be friends with someone like you."
        me "There's nothing special about me."
        mi "Be quiet. I know better. After all, I'm the victim of circumstance."
        me "So much time wasted. So only one day happened to us."
        me "But what a day!"
        mi "Life is a strange thing. You go around in the same circle for years, and then, one day, all you have to do is get a little out of line, and they send you someone who becomes your friend in less than a day."
    menu:
        "Only a friend?":
            mi "You could have been something more. Only we didn't have enough time for that."
            mi "Senya-Senya... Where were you before?"
            "Miku sighed."
            mi "Hug me?"
            "The wind from the river mussed her hair, and her tails wrapped around me like living tails, enclosing us in an outlandish cocoon of aquamarine color."
            th "She speaks so confidently. And not afraid of anything at all."
            "I thought, hugging and holding the hot body."
            th "It's like I'm just another trophy on her shelf, not the most distinguished, but in the right place."
            th "Hence the question: should a trophy be proud to be better at something than its shelf neighbors?"
            me "I've only been here a week."
            "Slowly I began."
            me "And you... Are like this."
            mi "Like what?"
            me "Beautiful. How can I approach you like that?"
            mi "I've never thought of myself as beautiful, Senya. I'm ordinary. I was just taught to sing and made to perform."
            mi "And so I'm just a normal human being of flesh and blood."
            me "A beautiful human being."
            "I repeated stubbornly."
            mi "I'm not from another planet or something."
            mi "I need affection, care and warmth, too."
            me "And when you look at it from my side, you know how uncomfortable it is?"
            me "It's a kind of ugly man syndrome."
            me "I look at you and I can't believe that such beauty belongs to no one, walking around derelict."
            mi "Belongs?"
            "A smile was walking on Miku's lips, and I stared."
            "Shuddered, I came to my senses."
            if (alt_day2_date == 'mi') and (alt_day2_mi_date != 3):
                me "You told me yourself - the social abyss."
                mi "And you told me it was all nonsense! What am I supposed to do now?"
                me "I don't know. Enjoy life?"
            else:
                me "You have to go out with someone, there's no question about that."
                me "Which means there's no reason for me to approach you, only to get upset."
                mi "I don't belong to anyone. I don't date anybody."
                mi "That's it, you can stop being afraid."
                me "I'm not afraid anymore."
                "Indeed, there's no trace of fear now."
            if (alt_day2_date == 'mi'):
                mi "From the look of you, you didn't really enjoy it."
                mi "You ran away from me, and I waited and waited..."
                me "I'm afraid of boring you, I'm sorry."
            else:
                me "My only regret is that on my second day I didn't come to your club to get to know you better."
                mi "And we would have had so much more time."
                th "Much more than that."
            "I kissed the top of her head."
            "Miku giggled."
            mi "I'd sit here forever. But I feel too good here; I'm afraid I'll get used to it."
            $ alt_day6_us_7dl_mi_friends = 3
        "It's hard for me to get along with people too":
            mi "You hit it off pretty easy with me."
            "She giggled."
            me "Too bad, not for long."
            mi "Well, I hope we get to see each other again!"
    me "Yeah, when? We're leaving tomorrow already, so we'll part after we've barely met."
    mi "Look, let's..."
    "Miku's eyes gleamed with excitement."
    mi "Let's not leave each other?"
    me "But how?"
    mi "Name me something so I can find you."
    mi "And I'll name something in return!"
    mi "Then one day we can find each other again!"
    me "Do you think we can?"
    mi "Yes! I live in Tokyo now, but when I finish music school, I'll go back home to Sapporo. We'll memorize with mnemonics! Look: Sapporo, Odori Park, subway side house."
    me "Sapporo, Odori Park, subway side house."
    mi "Apartment 3108, like my birthday, easy to remember!"
    me "3108."
    "Obediently, I repeated."
    mi "And now you!"
    me "Uh... Well. St. Petersburg."
    mi "Where's that?"
    "Miku frowned."
    me "That's another name for Leningrad."
    mi "Got it! The city of Leningrad..."
    me "I live in a sixteen-story building at 69 Dalnevostochny Prospect."
    me "Odori Park, subway side house."
    mi "You won't forget?"
    me "No. Though I highly doubt I'll ever be in Hokkaido."
    mi "Who knows, Senya. Life is an interesting thing."
    me "Yes."
    "I smiled."
    me "Very interesting."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_sl_dancing:
    scene anim_square_party with dissolve
    "I got up and went looking for my victim on the benches."
    "And soon found her."
    show sl normal dress with dissolve
    "Slavya stood at Genda's pedestal and looked around with a smile."
    "It suddenly occurred to me that it might be appropriate to ask her to dance."
    "Why not?"
    me "Shall we dance?"
    show sl smile dress with dspr
    "Slavya smiled and put her palm in mine."
    sl "Of course."
    scene cg d3_sl_dance
    with fade
    "There was something stirring about such intimacy."
    "Something that confused my thoughts and prevented me from constructing an inner monologue."
    sl "Heard about your exploits today."
    "Slavya smiled when she realized that I didn't intend to start the conversation myself."
    me "Really? Like what?"
    sl "I'm talking about helping around the camp."
    sl "Wow, you only been here a week, and already setting an example for everyone how a real pioneer should behave."
    "Her voice was jocular, but there was no sarcasm or mockery in her tone."
    sl "If there was a lineup tomorrow - you would certainly be called up to raise the flag as the most active."
    me "And what about you?"
    sl "Well... What are you saying. It's you who need to put in effort in order to be like that."
    sl "And I, I live like that."
    "Just said Slavya, and I believed at once: yes, that's the way she lives."
    "She can't think of herself any other way."
    sl "This camp is my home; and I'm glad it's finally home to you, too."
    with fade
    th "None of this is mine."
    th "Not mine!"
    th "Not my beautiful girl, not my stars in the sky, alien and indifferent."
    th "And the eyes - of people who never belonged to my world."
    "Which hurt, for I wanted so much to be with them."
    "Even Slavya, who smiles hard, but really hides anxiety."
    me "What is troubling you?"
    sl "Lena."
    "Slavya got it right."
    sl "What worries me is that she could just go somewhere, and this is a forest, civilization is several hundred kilometers away."
    sl "And she didn't come to the concert."
    sl "Yeah, I'm explicitly told to keep my head down - it seems to be under control."
    sl "But I can't do otherwise, I don't know how."
    me "What can happen to her..."
    sl "Semyon, you don't understand: this is the first time I've had someone just run away."
    sl "It's never happened before. Never."
    "She murmured to me somewhere in my chest."
    sl "Never happened!"
    sl "I can't have something happen to someone I care about! It can't happen that way!"
    th "It can, honey."
    "And out loud I clarified:"
    me "Are you worried about Lena?"
    "Slavya gave me another smile:"
    sl "I'm worried about you too, silly Semyon."
    "She didn't mean anything, that funny silly girl - just scared and worried."
    "Just a vague worry, like an exhale over her shoulder, stirred her soul."
    "And that means Slavya is growing up."
    sl "Was I really wrong?"
    sl "Have I been wrong all this time..."
    me "Yes."
    sl "I'm scared."
    me "Why?"
    sl "If I can be wrong about little things, one day I might be so wrong that..."
    sl "I don't even want to think about it."
    th "And I'm a grandmaster of mistakes, blunders and nonsense."
    th "It's all right, I'm not dead at least."
    "I don't think that would have comforted the girl. {w} There's not much consoling her now, except simple human sympathy."
    me "And don't think about it. Why spoil your mood for nothing?"
    me "And don't worry about Lena - I know for a fact that she's all right."
    sl "How?"
    me "I can feel it."
    with fade
    scene anim_square_party
    show sl normal dress
    with dissolve
    sl "Well. You can't discount premonitions."
    sl "But still, my heart's not in the right place."
    "She looked at me like she was waiting for me to say something."
    "But I didn't say anything."
    "Slavya sighed, got sad."
    show sl sad dress with dspr
    sl "I'm going to go play the next record."
    me "And I'm going for a walk. See you later."
    hide sl with dissolve
    "Slavya nodded in response and turned back to the host's table."
    "I took the opportunity to remove myself immediately to the quietest and loneliest place now."
    "To the pier."
    $ persistent.sprite_time = "night"
    $ night_time()
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_tea:
    scene bg ext_house_of_mt_night with fade
    play ambience ambience_camp_center_night fadein 5
    play music music_7dl["melancholy_sun"] fadein 3
    "When I returned to the cabin after a walk, I found a squad leader sitting there on the steps."
    dreamgirl "One day Father Onuphrius, walking around the vicinity of Lake Onega, found Olga naked."
    dreamgirl "Yes, that would have been nice!"
    "She was sitting on the third step, so that her elbow rested comfortably on the balcony, there was a glass next to it."
    show mt smile dress at zentercenter with dissolve
    mt "Oh, our wanderer has come."
    "Olga waved to me."
    mt "Join our warm company."
    if alt_day6_us_7dl_help:
        show us smile sport at zenterright
        show mt normal dress at cleft with move
        us "Are you stalking me or something?"
        "Giggled Ulyana from the chaise lounge."
        me "Yes, stalking, screaming and begging to give you a palm frisk!"
        show mt smile dress with dspr
        mt "Casanova."
        "Olga smiled."
        mt "Don't you spoil my pioneer girl!"
        me "She's the one who can..."
    else:
        show us dontlike sport at zenterright
        show mt normal dress at cleft with move
        us "As if we need him here."
        "Ulyana snorted from the hammock."
        me "Hello to you, too, little one."
        "She didn't pay any attention to me."
        "And that's after all we've been through together!"
        th "What have we been through? Lots of stuff!"
    "They were obviously arguing about something until I showed up, and neither side came out satisfied."
    "So they continued the argument as soon as the pleasantries were over."
    me "What was the conversation about?"
    us "Oh, nothing. Little things."
    me "May I ask what little things?"
    show us dontlike sport with dissolve
    us "No."
    me "Great. I mean, now they're secretive from me, too."
    me "I'm don't want to have any business with you. You betrayed my trust, battle buddy!"
    show us calml sport with dspr
    us "See!"
    "Ulyana spread her hands."
    us "He basically doesn't take anything seriously."
    show mt laugh dress with dspr
    mt "He doesn't have to."
    mt "You have a lot of important things to do, and Semyon has one important thing to do."
    show us surp1 sport with dspr
    us "Yeah? What is that?"
    mt "You know what! A proper rest!"
    show us sad sport with dspr
    us "It's always like this, Ol'dmitrievna. Always mocking me."
    show mt smile dress with dissolve
    mt "Not mocking. Just teasing."
    mt "You get away with a lot. Do you know why?"
    show us smile sport with dspr
    us "Because I'm a kid, and you can't hit kids?"
    mt "Because you don't want to be one."
    mt "Here, ask Semyon how to behave on vacation. He'll tell you. He's an expert on that subject."
    show us normal sport with dspr
    us "You're teasing me again."
    "Ulyana guessed."
    mt "Just a little bit."
    "It seemed to me at times that all of the leader's craziness, her frivolous behavior, was simply an attempt to keep something extremely precious inside her."
    "Elusively blue and fragile, unsettled and light."
    "How can you say that out loud?!"
    "I knew perfectly well that the squad leader could forgive me a great many things, but not the unraveling of her as a person."
    "So I pretended I wasn't there and enjoyed the company."
    play sound sfx_open_dooor_campus_1
    pause(0.5)
    play sound sfx_open_dooor_campus_2
    scene bg ext_house_of_mt_night
    with fade
    "I went to the cabin, got myself a glass of tea, too, and settled down next to the squad leader on the porch."
    me "And I thought you forgave her so much just because you were kind?"
    show mt laugh dress at zenterleft
    with dissolve
    mt "Me? Kind?"
    show us normal sport at zenterright
    with dissolve
    us "Ol'dmitrievna is not kind."
    me "No way, she's evil?"
    show mt normal dress with dspr
    mt "No. But I try to respect everyone's will."
    us "Understand now?"
    me "What?"
    show us laugh sport with dspr
    us "He's a little retarded after all."
    "The little one complained to the leader."
    show mt smile dress with dspr
    "What's most offensive, the last one nodded accordingly!"
    "What is this? A woman's rebellion?"
    me "Explain it me, the retard. If it's not too difficult."
    show mt smile dress
    show us normal sport
    with dissolve
    mt "It's very simple, I don't treat you like children."
    mt "I treat you like..."
    show us laugh2 sport with dspr
    us "Humans!"
    "Ulyana shouted out."
    us "That's why she's my favorite squad leader!"
    mt "Don't suck up."
    us "Why? As soon as we met, I immediately asked to join your squad! And I've never regretted it."
    th "So it's not about laziness?"
    "I was surprised."
    th "What a miracle."
    show mt normal dress with dspr
    mt "I'll still have to report to your father about your behavior."
    us "Oh, report it! What's the big deal! He won't even scold me while Grandpa's home."
    show us laugh sport with dspr
    us "And Grandpa will be here until the first of September! Yoo-hoo!"
    mt "Don't forget your promise."
    show us smile sport with dspr
    us "I won't forget! I'll be the last of the squad to come here next year!"
    us "I'm the squad's heir!"
    show mt smile dress with dissolve
    mt "Fine, heir."
    "Olga finished her tea and set the glass aside."
    mt "Come on, I'll walk you home."
    hide us
    hide mt
    with dissolve
    "They waved at me and melted into the darkness."
    "Apparently it's a habit by now - leaving dirty dishes and an unassembled chaise longue on me."
    "Grumbling softly, I set about cleaning up."
    "Not realizing I was smiling stupidly the whole time."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_sleeptime:
    play music music_list["a_promise_from_distant_days"] fadein 2
    scene bg ext_house_of_mt_night with dissolve
    play ambience ambience_camp_center_night
    "The camp danced their legs off and went to bed."
    "It was time for me, too."
    if (alt_day6_us_7dl_mi_friends == 3) or (alt_day6_us_7dl_un_friends == 3):
        "Although I didn't expect a simple, boring evening of a loner like me could escalate into something more."
        "But... I just got too lucky, which means it makes sense to expect some nastiness in the future."
        "So don't relax, by no means relax!"
    else:
        "I managed to strike a shaky balance between me-old and me-new."
        "I was turning back into me that was left on the frozen streets of St. Petersburg."
        "And at the same time, I managed not to think people were bastards."
        "How did I do that? I don't know."
    "But the place I consider my home is waiting."
    "Even if that'd be my last night at home."
    play sound sfx_open_dooor_campus_2
    pause(1)
    scene bg int_house_of_mt_night2 with fade
    play ambience ambience_int_cabin_night fadein 1
    "It was hot inside, smelling of heated metal and damp."
    "Here they boiled water, drank tea."
    "Resting."
    "So first of all, I opened the window, breathed in the fresh night air, which seemed impossibly delicious from here."
    "And, throwing off my clothes, I went to bed."
    if alt_day6_us_7dl_mi_friends >= 2:
        "There was absolutely no energy left to hang out a fancy suit."
        th "The squad leader will scold..."
    "I closed my eyes."
    "Before my eyes unfolded the images of the day that had passed."
    if alt_day6_us_7dl_help:
        "A continually infuriating and yet continually disturbing story with this little one."
        "Her unwillingness to talk about the simplest things."
        "What's it all about?"
        "To lure me off the territory and kiss me on the cheek?"
        "Who's manipulating who huh..."
    elif alt_day6_us_7dl_un_friends >= 2:
        scene cg d5_un_island
        show prologue_dream
        with dissolve
        "The confused, hot-headed confessions from the green-eyed girl with the sad look."
        if alt_day6_us_7dl_un_friends == 3:
            "And her amazing determination."
            "Or was it both of us trying?"
    elif alt_day6_us_7dl_mi_friends >= 2:
        scene cg d3_mi_dance_close_bordo_7dl
        show prologue_dream
        with dissolve
        "An evening with Miku."
        "Or rather, a whole day with her."
        "And no, I don't mean to say that I fell in love - after all, time's a-wasting."
        if alt_day6_us_7dl_mi_friends == 3:
            "Even though..."
            "I don't know. I like her - that's the most important thing."
    elif alt_day6_us_7dl_sl_friends == 2:
        scene cg d3_sl_dance
        show prologue_dream
        with dissolve
        "Trying on Slavya's image, her way of life."
        "Understanding that I'm not likely to make it."
    elif counter_us_7dl_px == 3:
        scene cg d4_us_stardust_7dl
        show prologue_dream
        with dissolve
        "Strange things happening around me."
        "But not frightening, only exciting, for some reason."
        "Like the light that suddenly fluttered from the palm of my hand."
    scene cg d1_end_of_day_7dl with dissolve
    "And, falling asleep:"
    if alt_day6_us_7dl_help:
        me "Little sh..."
        "I felt myself smiling."
    elif alt_day6_us_7dl_un_friends == 3:
        me "Lena..."
    elif alt_day6_us_7dl_mi_friends == 3:
        me "Miku..."
    else:
        me "Sleeeep..."
    "Fell asleep."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_px_begin:
    play music music_7dl["unfulfilled"] fadein 5
    play ambience ambience_int_cabin_day fadein 2
    scene anim prolog_1 with dissolve
    "I had some strange dream last night."
    "The kind that you forget even faster than consciousness reluctantly returns to you."
    "But the familiar warmth of the sun on my cheeks and palms was well imprinted in my memory."
    "Only more this time, much more - as if a starry sky had opened in the middle of the night, revealing a sun on the underside."
    "Or at least a ray of sunshine."
    "Even better, two sun bunnies!"
    "Let them bounce around the room and play, scurrying across the ceiling and blanket, tickling the nose and making a sleeping Olga Dmitrievna smile in her sleep."
    "And when one of them gets to the closet where the mirror awaits its hour... Ooh, so much excitement and dancing!"
    "So it was, so it is."
    with fade
    "Because I think it's the right thing to do!"
    "Then it'll be right, and it won't hurt me to wake up."
    "The bunnies will dive into my palm again, burning it in the very middle, but it's different now."
    "Now I feel them as part of me, a fiery melt beating through my veins, burning everything out of my blood that is inappropriate in this particular moment."
    "What is inappropriate in human life in general."
    "I realize now that blood poisoning dampness and drabness were never a part of me, it was all brought in from the outside."
    "And the body has to get rid of all that nasty stuff sooner or later."
    "Otherwise it gets sick."
    "So I looked inside myself - where two tiny stepsons of the sun were frolicking and playing - and smiled at them."
    me "Melt-Melt..."
    scene bg int_house_of_mt_sunset
    mt "Good morning to you, too."
    "That's what I heard from the neighbouring bed."
    mt "Though you should be flogged, in a good way, for your antics last night."
    mt "What are you doing up so early? It's only eight o'clock."
    me "And I can't."
    "I smiled."
    me "I had such a dream and I can't remember it."
    me "And I slept well too."
    mt "And got drunk on squad leader's blood."
    "She squeaked back."
    mt "Are you going to turn around and let me get dressed, or going to get up yourself?"
    me "I will!"
    "I exclaimed."
    "It was like rubbing my shoulders in the cold - as if a good gallon of hot blood was stagnant in my deltoids, and if you move it, waves of goose bumps ran through your body."
    "I, on the other hand, clearly had a good liter of highly concentrated energy stagnating in my deltoids."
    "I drew in a breath, and in a peculiar way, the sagging shell beneath me creaked up, flexing with a faint creak."
    "It was as if for a split second I had managed to make myself childishly weightless - that half-forgotten skill."
    with vpunch
    "I jumped off the bed with a sharp exhalation, still noting in the air the position of the neatly folded uniform."
    "For the umpteenth time, I was surprised that Slavya's uniform fit so well."
    "A chuckle came from under the blanket."
    me "Hey, no peeking!"
    mt "All right, all right, I'm turning around."
    mt "You made me bet half a pound of lemons, by the way."
    me "How's that, I wonder?"
    "I clarified, tightening my strap and promising myself to find Slavya and get a good deal."
    mt "We had a bet, me and Katyushka, that you were a vicious sleeper and your best friend was an alarm clock."
    mt "I bet you had no conscience, and you'd sleep sweetly till morning."
    mt "And Katyushka had the nerve to say that because of the torments of conscience you will also wake up before me."
    me "Hmm. Not bad. Will there be my ten percent?"
    mt "For what?"
    me "Commission! For the use of my bright face."
    mt "Go wash it first, bright face."
    "And me, smiling, plopped outside."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_px_breakfast:
    scene bg int_dining_hall_people_sunset_7dl with dissolve
    play ambience ambience_dining_hall_full fadein 3
    play music music_list["everyday_theme"] fadein 5
    "Despite the fact that we were the first squad, in fact, we were always the last to get to the canteen."
    "I don't know by whom, but there's only one way to eat quietly."
    "In the case of a nighttime break-in."
    "As Ulyana and I did yesterday."
    "Honestly, I still don't understand why we didn't get punished for all the good stuff we did."
    "Except that Ulyana had disappeared, and I was more and more worried about the obnoxious girl."
    "Not that I don't care about Lena's fate, but... Priorities, priorities..."
    "Anyway, my turn came, and I got my plate of porridge and a couple of sandwiches."
    "I decided that having breakfast alone wouldn't be the worst idea."
    "Neither Ulyana nor Lena ever came back."
    "That was rather strange: after all, the same Ulyana had eaten properly yesterday... When? At breakfast."
    "Olga, on the other hand, acted as if she had everything under absolute control."
    "But where is that control if she doesn't know where she's got who?"
    th "Maybe she just does not care?"
    "The thought seemed wild, but still."
    "That's unlikely, though."
    "No matter how bad you are as an educator and a human being, you still have motivating beginnings."
    "If not intelligence, honor and conscience, then at least the fear of being kicked in the head in the event that your superiors casually ask, «'What the hell is happening here»?"
    dreamgirl "Drunk, drunk!"
    "My schizophrenia laughed."
    th "I'm worried, by the way."
    dreamgirl "And for whom more? For the daughter of a police colonel or the granddaughter of a KGB officer?"
    th "For both!"
    "I barked, but immediately cooled down."
    th "For Ulyana, a little more."
    "We got pretty close while we went through hunger, cold and hardship together yesterday."
    "So I was really worried about her and kept wondering where to find her."
    dreamgirl "Don't you dare. She's not even sixteen."
    th "Ugh, you pervert!"
    "I remembered the pesky «satisfaction» song and hummed it to myself to drown out the cries of the eternal vulgarity, and started on my breakfast."
    "Very tasty, by the way!"
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_px_carrier:
    scene bg ext_dining_hall_near_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 3
    play music music_7dl["escape_2"] fadein 3
    "Memory has the magical property of opening doors from childhood - right into the classroom."
    "But more often in the rain. And only rarely in the summer."
    "But should we be discouraged about it?"
    "You have to be very, very happy to let a miracle into your soul. {w}And definitely a child."
    "And absolutely - jumping in puddles and laughing so hard that the corners of your lips hurt to smile already."
    "Then you might just be able to snuggle a tiny winged wonder in your backpack, and find a room with a couch, a TV... and an exit to your parents' bedroom in the thicket of the woods."
    "You might stop being afraid of open windows and upper floors, because even without wings you can take to the sky."
    "How? The recipe is ridiculously simple. {w} A lot of faith in yourself and your father's black umbrella that says «VISION» from top to bottom and «NOISIA» from bottom to top."
    "Although the umbrella probably isn't that necessary. {w}You could just make an airplane."
    "If it's big enough, you can fly up to the moon - much higher than the swing flies."
    "Treat your memory well, because it's the one thing that can't be taken away."
    "Like my, now eternal memory of a certain red-headed pest who disappeared early this morning, and now she."
    "Sitting there like nothing had happened, smiling, looking up from under her bangs."
    show us smile sport with dspr
    us "Hey, Syomishe."
    "She reacted to my appearance by instantly jumping up from the bench and flying over to me."
    us "Lost me this morning, huh? Worried? Looking for me?"
    me "Where have you been?"
    show us surp1 sport with dspr
    us "So you were worried! Yay."
    me "Worried, of course."
    "I admitted it."
    show us normal sport with dspr
    us "And I dreamed that Flared led us to The Old Road. So great!"
    me "And what's so great about The Old Road?"
    show us surp2 sport with dspr
    us "Don't you get it? The Road is the way. It's not just some fairy tale!"
    me "Get it. The Road is the way."
    show us laugh sport with dspr
    us "Don't pretend to be smarter than you really are!"
    us "It's an unusual highway. You've seen it yourself."
    me "Little matters what I see. So you went to check it out?"
    show us normal sport with dspr
    "Ulyana nodded."
    us "But, I'm stuck halfway there, like I'm about to find it, but I keep going around in circles."
    us "I can't do it by myself. Can you help me?"
    show us sad sport with dspr
    "The girl held out her palm to me and looked pleadingly into my eyes."
    us "Will you?"
    "I nodded. What else could I do?"
    show us laugh sport with dspr
    "Ulyana glowed and clutched at my palm, pulling me along with her."
    scene bg ext_dining_hall_away_sunset
    with dissolve
    "Unlike me, she never doubted anything."
    "There was something primal and appealing about that directness."
    "Like savages dancing around a campfire, not caring who saw them dancing, who thought what..."
    "What confused me was the far-fetched nature of the story."
    "And that's not counting the threats from the podium this morning."
    "By all the laws of meanness, I should have been caught now and voluntarily or involuntarily sent to community service."
    "By either Olga or her assistant."
    scene bg ext_square_sunset
    with dissolve
    "Or somebody else."
    "But the strange thing is that the whole time we were moving through the camp, it was as if no one cared about us."
    "And it wasn't because of the secret paths we took, not at all."
    "No, we walked brazenly, almost running through the busiest parts of the camp."
    "As if running into trouble."
    stop music fadeout 3
    scene bg ext_backdoor_sunset_7dl
    with dissolve
    play ambience ambience_old_camp_outside fadein 3
    play music music_7dl["lynn"] fadein 3
    "The sun had finally risen by the time we got to the back gate."
    "The morning grocery car had already rolled back into town, so it was empty and deserted."
    "In fact, so deserted that I couldn't stand it and turned back, checking to see if the camp had suddenly disappeared behind our backs."
    "No, it's still there."
    "Though I wouldn't be surprised - too much unthinkable stuff has happened to me in the last few days."
    "And against the backdrop of the most important miracle - my moving here - even things like the Ulyanka's Flares paled in comparison."
    "A couple of decades into the past, and not just backwards, but sideways."
    "Away, not yet sucked up by the drooling fantasies of writers, into the world of «what if.»"
    "What if Genda came to power in the Union?"
    "What if there could be perfect, infallible people in the world - and not at all the icy statues of Efremov?"
    "What if once there was a boy who managed to escape from a camp from which there was no way out but to leave, who just foolishly notched up his thrashing?"
    "What if he then returned to the camp and delivered what he had notched to his followers in the form of some kind of ritual?"
    "And water does find a way."
    "And now one of those followers is dragging a big-headed oaf, who hardly believes it himself, in the middle of nowhere."
    "Because she, unlike the aforementioned nitwit, believes it all."
    "The only thing I don't understand is."
    th "Why would she do that?"
    "I could understand boys, boys have always been captivated by the romance of the quest."
    "Even if you're just working as a lighthouse keeper, you're part of it."
    "You show the way to someone who's lost in the dark."
    scene bg ext_path_day
    with fade
    play ambience ambience_forest_day fadein 3
    "Explaining the miracle by the fact that Ulyana was a patsy was very reluctant."
    "It would have looked like a dirty handprint on a white canvas."
    "And I was just starting to {i}believe{/i}."
    "I didn't want to explain away the miracle with vulgarity. I didn't want to reach for a miracle at all."
    show us normal sport with dspr
    us "Wider step, Syom, we're almost there."
    me "You're in such a hurry, as if the ships will run away in this time."
    us "They won't, but..."
    show us smile sport with dspr
    us "Aren't you curious yourself?"
    th "Curious?"
    th "I'm already in this whole thing, so..."
    "I have to go all the way."
    "The first step led me to the sand pit, the second..."
    "Well, actually, not too far from that quarry was the very cove where the ships found harbor."
    "And so today I walk, guided no longer by someone else's hands, but only by desire and the burning in my palms, scorched with a tiny burn."
    "In spite of all the doubts, all the confusion - why this place has not yet been found!"
    scene cg d5_un_carrier_7dl
    with dissolve2
    "The trees parted again, revealing a back covered in a white pioneer shirt."
    "Slightly twitching purple ponytails and a melancholy contemplation in the pose."
    "The same emotion that always made a loved one come up and hug quietly. Silently."
    "Unless, of course, that loved one is waist-deep in oak and has at least the rudiments of empathy."
    "But - perhaps fortunately, perhaps unfortunately - we weren't any close to Lena."
    "Ulyana pressed her finger to her lips, telling her not to disturb the moping Lena, and we walked, sideways, down the far path."
    "To where the last of the ships were yesterday, in the creek."
    stop music fadeout 3
    scene bg ext_sandpit_day_7dl
    with dissolve
    play music music_7dl["out_of_painkillers"] fadein 3
    "The sky above my head was a sultry, whitish solution, but in the shade of the birch the heat was hardly noticeable."
    "Only here and there were fleshy green lingonberry leaves peeking out of the mossy cushions - not in season, at least a couple more weeks, until August, but..."
    "This shift won't get a single clump of lingonberries - tomorrow we'll get in our cars and rush off to the new school year, and some of us will go on to adulthood."
    "We were walking the wrong way yesterday, because instead of a comfortable path there was a well-trodden dusty slope, and the familiar burning in the palms of my hands from sleep."
    "Like a child's old game of «hot-cold», for me now it was «hot» and «hot»."
    "I had to wander around, because not all the places were passable, and in some places there was polished, slippery salt."
    th "And all for the sake of not disturbing the moping girl, whom Ulyana had only mocked before."
    th "Since when did Ulyana become so sensitive?"
    scene bg ext_lake_day_7dl
    with dissolve
    play ambience ambience_lake_shore_day fadein 3
    "The Flares that had started up yesterday were gone, and I had to move forward without letting go of Ulyana's palm, because she suddenly stumbled on a clean spot and looked around confusedly."
    "It was as if she woke up, as if she no longer knew where she was."
    show us dontlike sport
    with dissolve
    us "What the..."
    me "What happened?"
    us "I lost the way."
    me "What do you mean? What's that?"
    "I pointed to the path we've been following so far."
    show us calml sport with dspr
    us "That's not it! I can't feel The Road!"
    us "There's no direction!"
    "The girl didn't look happy."
    us "That's what was going on this morning, too."
    us "Walked around in circles for an hour. And nothing!"
    me "Direction, you say?.."
    show us surp1 sport with dspr
    us "Do you feel something?"
    "Instead of answering, I raised my palm in front of me, where both lights dived in my sleep."
    "My hand was red and itchy."
    show us sad sport with dspr
    us "Wow. That's not fair, though! I've been looking for it so long, and you just came and found it."
    me "That's the main function of a man."
    "I stated admonishingly."
    show us laugh sport with dspr
    us "All right, man. You drive then."
    me "You know what to do, don't you?"
    "She nodded and whispered softly:"
    us "Melt-Melt, away you left..."
    "I advanced to the head of the procession, and we continued on our way."
    stop music fadeout 5
    scene bg ext_busstop_dust_7dl
    with fulldiam
    play ambience ambience_ext_road_day fadein 3
    "I don't know how long we walked, but at some point both the quarry and the thicket ended, and the forest path we had been walking the whole time merged into the highway."
    us "The Old Road."
    "Said Ulyana from over her shoulder."
    us "Looks like our search is over?"
    th "Over?"
    "I looked around."
    "The road was strange, vaguely familiar, but the grass, overgrown here and there through cracks in the asphalt, indicated that no one had used it in a long time."
    "I didn't see anything here that could be called the purpose of the search."
    me "The Road. So?"
    us "Come on, you'll see!"
    "Ulyana lunged ahead again, and I had no choice but to hurry after her."
    "The old, old road, all potholed, here and there the asphalt pavement bulged, pierced by the sprouting green..."
    scene
    $ renpy.show("bg ext_busstop_dust_7dl", what = Desat("bg ext_busstop_dust_7dl"))
    with dissolve
    "I don't know how long we walked, but at some point the air suddenly became very familiar, the colors thickened and went into a much calmer range - faded, dull..."
    play music music_list["no_tresspassing"] fadein 3
    "A hundredth sense, a gamer's intuition, a sense of direction - you can call it anything you want, one thing became clear: we were passing very close to where my home was at hand."
    "We passed a drainage pipe coming out of the pavement - a sluggish trickle almost completely soaked into the parched soil, but a puddle could be discerned in the distance."
    "A small, shallow one - a chicken could wade through it, but..."
    scene
    $ renpy.show("bg ext_busstop_dust_7dl", at_list = [sdl_transform8], what = Desat1("bg ext_busstop_dust_7dl"))
    with fade
    pause(1)
    scene
    $ renpy.show("bg ext_busstop_dust_7dl", what = Desat1("bg ext_busstop_dust_7dl"))
    "I looked closely, and my temples ached, the world had made one very bad turn counterclockwise: bumping their noses into the fleshy trunks of sedges, on the other side of the puddle two ships were swaying lazily, with their candles as masts already extinguished."
    "So I turned sharply and, without letting go of Ulyana's hand, dragged her back."
    show us dontlike sport with dissolve
    us "Hey, stop, wait!"
    me "No. We have to get out of here, and as soon as possible."
    hide us with dissolve
    "After these words, the little one was silent and followed me obediently for a few minutes, without arguing. {w}It didn't last long, though:"
    show us calml sport with dissolve
    us "Where are you dragging me?"
    play sound2 sfx_intro_bus_stop_steps
    me "Back. I'm not sure we should st..."
    with flash
    play sound sfx_fall_wood_floor
    play ambience ambience_7dl["explosive_post"]
    "Like a fall deep into my own subconscious before I fall asleep, making my legs twitch, a Volga rushed past me in the frosty air. An imaginary one."
    play ambience ambience_ext_road_day fadein 3
    me "No, let's get out of here."
    us "No, we have to go this way!"
    me "Under the wheels? No way."
    show us dontlike sport with dspr
    us "You don't understand!"
    "Ulyana stopped and took her palm away."
    us "Mirya tried to send me on this road in his last summer. {w}He was just talking about what could be here."
    me "Who is this Mirya?{w} I mean, I know he was the leader of the «guardsmen» before you, but what kind of man he was?"
    show us surp2 sport with dspr
    us "You didn't know?"
    me "What?"
    us "Mirya is Dima Mironov. Olga Dmitrievna's brother."
    me "Wow. She also had a brother..."
    show us normal sport with dspr
    us "Yes. He's the one who taught us how to launch The Flares and told us how to get out of here."
    me "Look, he had to get out, let him get out. {w}I don't... I don't need to go out there."
    show us dontlike sport with dspr
    us "How do you know?"
    th "Because I was there once. {w}Wouldn't it be possible to say about my whole previous life - once?"
    me "Nevermind. We're leaving."
    show us normal sport with dspr
    us "But we'll come back."
    me "No."
    us "We'll come back with help."
    "As if not listening to me, the girl continued."
    us "Because we can't do it alone."
    me "No."
    us "Semyon..."
    "This is the first time she's called me by my name."
    us "It's very important. Believe me, please."
    me "Why?"
    us "I... I can't tell you."
    me "More kindergarten games. I'm off."
    stop music fadeout 3
    scene bg ext_busstop_dust_7dl
    with dissolve
    "I waved my hand and headed for the footpath, already visible from here."
    "Away from the smell of the big city and the disappointment of a lifetime."
    "There was silence all around, uninterrupted even by the ubiquitous cicadas."
    "It was as if exactly «here» and «now» were billions of miles without anyone living around us."
    "It was as if we had become in a different quality - an alien world, those very halls."
    play sound sfx_slavya_run
    "That's why the rhythmic pounding caught my attention."
    "I froze, listening, and for a full second I realized that it was nothing more than the most ordinary tapping of sandals on the pavement."
    "Ulyanka was running after me:"
    show us normal sport far with dissolve
    us "Wait, damn it!"
    me "What?"
    us "I can't tell you everything, you know? It's too early."
    me "Is it too early for logic too?"
    show us normal sport with move
    us "What kind of logic? If you're talking about how Mirya knew..."
    me "No, that's not what I mean. You said yourself that if you were shown the way, you could go out to any such enclosed place."
    us "Well?"
    me "So then why didn't Olga Dmitrievna go after Lena? {w}If she's Mirya's sister, then he obviously took her to the Forest of Memory."
    show us dontlike sport with dspr
    us "Maybe he did, maybe he didn't. I don't know."
    us "When I first came here, Mirya came over just once, to say goodbye to Olga, we were a little friends then, so he told me how to do all that..."
    me "Then why don't you tell me what all this running after The Flares is about?"
    show us shy sport with dspr
    us "Well, it's..."
    me "You are hopeless, I get it."
    hide us with dissolve
    "I hurried down the road without listening to another word."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day6_us_7dl_px_dinner:
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 3
    play music music_list["my_daily_life"] fadein 3
    "At lunchtime Ulyanka didn't even want to look in my direction."
    "In fact, she wouldn't have looked, but there was a squad leader standing outside the canteen who didn't like to see her two favorite headaches staring at each other."
    "She said so herself, honest to goodness!"
    scene bg ext_dining_hall_near_day
    show prologue_dream
    show mt normal pioneer at zenterleft
    show us dontlike sport at zenterright
    with dissolve
    "So to begin with, she took the sweet couple back to the sinks, scrubbing off their grubby palms, and later refused to let them eat at all until the two fools had made up."
    "And how! Little fingers, «make up», paw shake, and «peace»."
    "Who, in their right mind, would hold a grudge after that?"
    "She should have turned around and walked away proudly, but the whale song of her tummy and the silly laughter of her squad leader ruined everything."
    "Nothing to do, hunger is known to be a bitch, so I had to put up with it."
    scene bg int_dining_hall_people_day
    show us angry sport
    with dissolve
    us "That doesn't mean I've forgiven you!"
    "She declared, just as they squeezed through the canteen door."
    me "Oh, for heaven's sake."
    "I didn't feel guilty at all."
    me "I didn't like feeling like a Champignon anyway."
    show us surp1 sport with dspr
    us "Huh?"
    me "Guh. Those are mushrooms, you know? They grow in the dark, fertilized with you-know-what. Didn't like it."
    us "Hm, can't remember you drinking this morning."
    "She sniffed suspiciously."
    me "And I can't remember you lying this morning."
    hide us with dissolve
    "I shut up and gave my full attention to lunch. {w}I was offended."
    "There was silence at the table for some time, interspersed only by the clatter of spoons on plates."
    "I drifted off into my own thoughts, while Ulyanka tried to find her loyal guardsmen from the second squad, with Danechka at the head."
    "Catching their gaze at last, she pointed to the door with significance and raised an eyebrow questioningly."
    "The curly head bobbed - the «guardsman» definitely understood the pantomime."
    scene bg ext_dining_hall_away_day
    show us normal sport at zenterright
    show dn normal pioneer at zenterleft
    with dissolve
    "And so it turned out - by the time she left the canteen, Ulyanka could see Danya propping up a pine tree by the canteen."
    "Comfortably nestled, in the shade, inconspicuous, if you don't know what's there - you can't see it!"
    me "Hello."
    "I followed the girl for some reason, thought I should say hello."
    "Danya didn't even look at me."
    dn "Why did you call?"
    us "We..."
    "After looking around to see if anyone was eavesdropping, Ulyanka confessed:"
    us "We found the Road."
    show dn surprise pioneer with dspr
    dn "Seriously? That's great!"
    "The curly-haired got excited."
    dn "When are you going?"
    us "Already. There's nothing for the two of us to do there."
    show dn smile pioneer with dspr
    dn "And you want me to go with you?"
    us "No. Only with me. He's not going."
    "I nodded, confirming her words."
    show dn unsured pioneer with dspr
    dn "Then what is he doing here?"
    us "Nothing."
    "Ulyana turned around and, gritting through her teeth, reported:"
    show us angry sport with dspr
    us "He is leaving already."
    "I guess, she was waiting for my reaction?"
    scene bg ext_dining_hall_near_day at zenterleft
    "I turned and backed away, taking my place on the bench, where I couldn't be seen but was perfectly audible."
    dn "What was he even doing here?"
    "A few minutes later Curly inquired."
    us "He... Well... He's the one who found The Road."
    dn "And you just chased him away like that?"
    "There was something strange in Dan'ka's voice."
    dn "He found it, and you chased him away?! You know what it's called, don't you?"
    "He fell silent, and judging by the shuffling of his soles, he turned around on the spot."
    dn "Treachery, Ulya."
    "Gone."
    "There were clearly tears in the question thrown in his wake:"
    us "So what, you're just going to leave like that?! That's your dream, too!"
    dn "I was put in charge of the squad at the concert."
    "Danya cut off."
    us "What am I supposed to do?"
    "She cried."
    dn "I don't know. Try to be human."
    "Gone. Leaving a thunderclap rolling over the square, a hydroacoustic thud - an ostracism."
    "A little while later, Olga Dmitrievna came out of the canteen."
    "But I didn't want to talk to her anymore."
    scene bg ext_houses_day
    with dissolve
    "Ulyana caught up with me only at the crossroads - it was the afternoon, and I didn't want to waste it on something I didn't understand."
    show us sad sport with dissolve
    us "Syomych."
    "She caught up and took my little finger unabashedly."
    me "What?"
    "The indifference in my voice was enough. {w}But I was in no hurry to remove my finger."
    show us smile sport with dspr
    us "We are not allowed to fight. Remember? Make-up make-up make-up."
    me "I didn't fight with you. But I'm sick of being taken advantage of. {w}You either tell me everything or I'm going to bed."
    "After hesitating, Ulyana reluctantly nodded:"
    show us normal sport with dspr
    us "But not now, okay? I'll have to explain right away to everyone. {w}Don't want to repeat."
    "The excuse was so-so, but it was also progress compared to the old «no»."
    "Maybe that's why I bought it:"
    me "Who do we take with us? Is there someone you trust?"
    us "I only trust myself."
    "Not funny, Ulyanka joked."
    us "But you can't take someone too old."
    me "You mean me, too old?"
    us "No. I'm not talking about age, but..."
    "She waved her hand."
    us "By the way, Alisa won't go, she's too old."
    me "No wonder, she's the oldest in the squad."
    show us laugh sport with dspr
    us "No, you fool! I'm saying we need someone who can believe. In any fantasy."
    me "Then Alisa is definitely out. Your guardsmen?"
    show us sad sport with dspr
    us "Busy."
    "The girl reported cheerlessly."
    us "They've been put in charge of the concert."
    me "Concert? Hmm... Then Miku definitely won't go, and I don't trust Zhenya and Electronik. {w}Only Lena and Slavya are left. But Slavya certainly won't agree."
    show us smile sport with dspr
    us "Did you decide to go alone after all?"
    if persistent.us_7dl_px_good:
        me "No, why. Let's go find Slavya."
        us "But first, get Lena!"
        "Girl shouted, dragging me along."
    else:
        me "Won't try - won't know!"
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day6_us_7dl_px_party_un:
    scene bg ext_un_hideout_day_7dl with dissolve
    play ambience ambience_lake_shore_day fadein 3
    play music music_7dl["take_my_hand"] fadein 3
    "I thought we were going back to the quarry, where Lena could stand for hours, leaning on the miserable railing, riddled with initials of all stripes."
    "But instead Ulyana dragged us in the direction of the beach - strictly to the south, only at the very shore steeply taking a left - to where a sand spit, densely overgrown with spruce in the middle, was far into the water."
    "At the quarry are heart-cut trees."
    "There's the Forest of Memory, it contains memories of many."
    "And from here it's so good to look at the water..."
    "The bushes parted and revealed to our view a scattering of large granite rubble, one of which was saddled by a familiar, slightly hunched, frail figure, concentrating on something."
    "Suddenly Ulyana cried out, sticking her finger in her mouth."
    show us smile sport with dspr
    us "Leeeenkaaaa!"
    "Ulyana jumped up to her and babbled about something."
    "I joined her a little late."
    show un normal pioneer at zenterleft behind us with dissolve
    show us smile sport at cright with dspr
    un "Why are you here?"
    "She tried to hide a shredded piece of bark in her pocket, in which I recognized - with a doomed sort of understanding - the crooked, blank Flare."
    me "We've been looking for you."
    un "Well?"
    "She wasn't surprised."
    un "Why?"
    us "We're going on a trip!"
    "Ulyanka enthusiastically reported."
    us "Don't you want to come with us?"
    show us laugh sport with dspr
    show un laugh pioneer with dspr
    un "With you?"
    "She laughed artificially."
    un "Where? Why?"
    show us upset sport with dspr
    us "What do you mean why... It's such an adventure!"
    show un serious pioneer with dspr
    un "Not interested."
    "Sad girl cut off."
    "The laughter subsided. And Lena, looking incredulously at Ulyana, stood up and turned to face us entirely."
    un "Why should I go there?"
    me "It smells like wormwood in there."
    "I shared."
    me "Do you know what that means?"
    "Certainly she knew."
    "Do you know that absinthe smells like a thousand herbs - and one bitter regret?"
    un "Where to go and what to take?"
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day6_us_7dl_px_party_sl:
    play music music_7dl["one_little_lone_cloud"] fadein 3
    scene bg int_warehouse_day_7dl
    show sl normal pioneer at zenterleft
    with dissolve
    "Slavya was sitting at the table near the linen warehouse, writing something into a huge household book in neat, round handwriting."
    "Without even lifting her head, she recognized us unmistakably:"
    with dissolve
    sl "Semyon and Ulyana. Are you being naughty again?"
    me "Are you still working?"
    sl "And I would advise you to do the same!"
    show us smile sport at zenterright
    with dissolve
    us "We can't. We have a new adventure!"
    show sl serious pioneer with dspr
    sl "Beyond the camp territory?"
    "Activist squinted suspiciously."
    show us laugh sport with dspr
    us "Of course. It's not fun running from the toilet to the infirmary!"
    "Shaking her head, Slavya put her pen away."
    sl "And who gave you permission to go there?"
    show us surp1 sport with dspr
    us "But we have a reason!"
    sl "What reason?"
    us "We know where Lena escapes to every year, so we're going to get her back!"
    show sl sad pioneer with dspr
    "Slavya sighed heavily:"
    sl "Enough with the composing already. Where are you going?"
    show us calml sport with dspr
    us "We're not..."
    "Ulyana started, but I interrupted her:"
    me "We found a very strange place. And it seems to be in dire need of being cleaned up."
    sl "What has Lena got to do with it?"
    me "Actually, that's where she's running off to."
    show us surp2 sport with dspr
    us "Yes! It's a very special place, you can't just go there!"
    show sl normal pioneer with dspr
    sl "For some reason, that's what I thought. So where is this place?"
    us "We'll show you!"
    show sl smile pioneer with dspr
    sl "I'll go with you."
    "Slavya smiled."
    sl "But on one condition."
    me "And the condition is...?"
    sl "I want you to go to the concert after that."
    me "But it's evening, disco. How are we going to make it in time?"
    show sl smile2 pioneer with dspr
    sl "And we're not going to make it today. That's why I said yes."
    sl "I can't just let you go."
    sl "So let's go tomorrow."
    $ alt_day6_us_7dl_px_sl_join = True
    show us sad sport with dspr
    "Ulyana certainly didn't like it."
    "But she didn't say anything. Apparently, she realized that there was really no hurry to argue."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day6_us_7dl_px_far_gate:
    scene bg ext_backdoor_day_7dl with dissolve
    play ambience ambience_camp_center_evening fadein 3
    play music music_7dl["sneakupon"] fadein 3
    "We made an appointment to meet at the south gate of the camp."
    "Ulyana, Lena. {w}And yours truly."
    "Can you think of any stranger company?"
    "But, unfortunately or fortunately, we didn't care much for it."
    "The problem was something else - we had agreed to get ready to go and gather at four o'clock, but it was the beginning of five, and still no girls to be seen."
    "I was shifting from foot to foot at the gate and feeling more and more foolish by the minute."
    "And I felt like a fool when the bushes next to me stirred and giggled."
    me "Ulyanka!"
    us "Shush!"
    me "How long have you been here?"
    us "Fourty years! Lena's here, too! Will you get in?"
    "Before I could answer, some movement in the periphery of my vision caught my attention, and I turned my head there painfully slowly."
    "That's right - at that end of the path, Trouble was moving in my direction with recognizable strides."
    th "Boris Alexandrovich?! What is he doing here?"
    show ba em1 uniform with dissolve
    ba "Hey there, wimp!"
    "The PE teacher rumbled as he approached."
    ba "Lazying?"
    me "Hey, hello."
    ba "That's what Olga said about you climbing somewhere. Where's your friend?"
    me "Which one?"
    ba "The prettiest one, of course!"
    "He snorted."
    ba "Soccer player."
    "The bushes behind me giggled."
    me "I have no idea."
    "I made the most honest eyes."
    show ba normal uniform with dissolve
    ba "Too bad, too bad. Okay, let's go."
    me "Where to?"
    ba "The concert. In fifteen minutes I want to see you on the bench of squad 1. So go..."
    me "But I really have to!"
    ba "You'll endure it. After supper you'll do your business."
    ba "Now, march to the concert."
    stop music fadeout 3
    stop ambience fadeout 1
    return

label alt_day6_us_7dl_px_disco:
    scene anim_square_party with dissolve
    "I was even a little taken aback, that she wasn't clinging onto me for dancing."
    "Didn't really feel like it, anyway."
    "I didn't really want to go to the disco, either."
    "I had very different interests in a very different place."
    if alt_day6_us_7dl_px_sl_join:
        "But somehow, in my tenth instinct, realizing that Slavya felt guilty, and therefore, would try to make amends, I decided to go."
        "Slavya's «sorry» sounded like «let's go to the dance, I'll invite you, and you also need a sensible suit also you need to have fun and enjoy life»."
    else:
        "Dancing looks dull and boring if you don't have anyone to wiggle with."
        "No one to tease."
        "Just to have some company."
        "And dancing alone is..."
    "That's the most disgusting interpretation, if you ask me. {w}Taste is a matter of opinion, of course, but..."
    "Take your hands off my inner rain. {w}I'll do it myself. Myself."
    "I'll crawl quietly into a corner, listen to stupid music, try to understand how people dance to it - maybe even dance?"
    "Just don't yank me, or there's a fortune cookie paper inside me that's about to tear."
    "I wish I had a cigarette in here. {w}Smartphone with a book and headphones, with a full charge."
    "We've succeeded in isolating ourselves from those around us, now it's almost impossible to even catch a pretty girl's eye on the subway - because she's submerged in her «stump»."
    "What's she got to do with a staring unshaven red-eyed guy? That's just it."
    "I'd like... loneliness."
    "Rising from the bench, I went to Genda and hid behind his pedestal, leisurely sad with the General Secretary himself."
    "Only he, unlike me, was trying to understand far more important things - for example, why does a man need a man?"
    me "I'm still loving you…"
    "With one lip I sang, and the thought that I had essentially no one to say those words hit me."
    "It hurt for some reason."
    "The mood was finally ruined."
    "The people around me were having fun, dancing as if tomorrow would never come."
    "And I sat alone, feebly, and counted my heartbeats to myself."
    scene anim_square_party
    with fade
    "They tried to get me to dance a few times, but I shook them off."
    "And the invitees were more out of politeness - they'd hardly want to see my lean face on the dance floor."
    "Or to have that lean face hugging them during the slow dance."
    "So I sat, bored, and listened to the music."
    "I didn't really understand why I was here."
    "There were a few of us, looking lost and untidy."
    "I even managed to spot Zhenya and Alisa on the set."
    "Surprisingly, they were instantly taken apart to dance when another dance was replaced by thoughtful interludes of slow dancing."
    "I realized suddenly that I knew nothing, absolutely nothing, about this camp."
    "Didn't have time to figure it out."
    "Didn't want to."
    "And that made me a little sad, I wanted to go back to that week."
    "But that's the good thing about vacations, they fly by, only leaving a sun-scorched spot in the soul, full of the smells of grass and the laughter of friends."
    "It's like flying to Dubai, for free, at an all-inclusive and then wishing a week later that you'd gone around all the markets and tried all the exotic food."
    "But my Dubai, on the other hand, is slowly receding into the past with every beat of music."
    "And do what you want, there's no way you can turn back time, start over."
    "Soon I became quite bored, so I waited for the squad leader to leave, and I left on my own."
    "Went wherever I wanted to go."
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day6_us_7dl_px_afterwords:
    scene bg ext_boathouse_night with dissolve
    play ambience ambience_boat_station_night fadein 6
    play music music_7dl["red_lights"] fadein 3
    "It was empty and deserted."
    "The perfect place to hide from the world, close your mouth, take a deep breath, and gaze long and long into the black water, in which, like a mirror, the sky, the tilted pines from the opposite shore."
    "I got so used to the constant hermitage that at some point it became almost an urgent need."
    "And there's always someone around here, they're all noisy, cheerful, enjoying life so much it makes your teeth grind."
    "I don't belong with them."
    "It's different here."
    if alt_day_binder != 1:
        "I smiled and, dropping my shoes and socks, sat down on the pontoon, leaned on the railing and lowered my feet into the water."
        "Warm."
        "Now if I could just get a cigarette to complete the buzz, but I could do without it."
    play sound sfx_wood_floor_squeak
    "And just as I was getting in a positive mood, a board creaked beside me, and I realized I wasn't alone again."
    th "When will it all end?"
    "Sadly I turned to the sky."
    show sl smile dress with dissolve
    sl "Escaped from the dance?"
    "Slavya smiled. She didn't manage to sneak up silently this time, and that lifted my spirits a little."
    "The thought immediately came to my mind, though, that the perfect girl Slavya, with all her sensitivity, could have just caught that moment."
    "And play along with me."
    th "So she deliberately made me hear her approach?"
    "The mood jumped to zero again."
    sl "The whole squad scattered."
    "Slavya reported in confidence."
    "She stood beside me and followed my gaze."
    sl "You almost got away once."
    me "Only to woke up in the same place where it all began."
    sl "The camp knows how to defend for itself..."
    me "Yeah..."
    "Tired of staring at one point, I turned away, staring at the silver of the moonlight splashing in the water."
    "Soon it will be lights out, the camp will be put to bed."
    "And tomorrow... Yes."
    "The camp seemed asleep - if it weren't for the sound of music wafting across the water."
    me "It's so wonderfully hidden that if it weren't for the pier, you could float by the river and never know there was a camp here."
    show sl normal dress with dspr
    sl "The builders were trying hard not to ruin the place."
    "I took the smart out of my pocket - although I'd turned off all the services and put it completely offline, there was exactly two percent charge left."
    "So it was only good as a watch."
    sl "What an unusual watch you have."
    me "A watch? Oh, yes... The time: 22:54... {w}You remember what that time is, don't you? Don't you remember?"
    "Of course you don't. You're so right."
    "Well, what are you... Let me light a cigarette, and... a warm place, but the streets are waiting..."
    sl "I'm not that dumb. {w} I know Tsoi."
    me "Tsoi? Where from? He's a rebel, always against the rules."
    show sl smile dress with dspr
    sl "Rules are not always a bad thing."
    me "Absolutely. But what rules govern happiness?"
    "Slavya was quiet."
    "When I was almost sure she was about to leave, she, without turning around, dropped:"
    show sl normal dress with dspr
    sl "If you want happiness, one day you have to take it from someone."
    "Her voice trembled."
    me "Someone, me?"
    sl "Living by the rules is not the only way to achieve happiness, that's what I realized."
    stop music fadeout 3
    sl "Sometimes you just have to go crazy to be happy. {w}And to hell with all the inhibitions. And just get what's rightfully yours. But here's the problem..."
    scene cg d3_sl_evening
    with fade
    play music music_7dl["my_only_hope"] fadein 3
    "Slavya stood beside me, diligently looking up at the sky, and in her head, and in her trembling voice, I could read that our Miss Infallible, too, sometimes lets her guard down."
    sl "It's like water on the seashore - you can dig a hole, and sooner or later the surf will fill it."
    sl "And it doesn't seem to mean anything, but I know that the level of the world's ocean has dropped another fraction of a millimeter."
    sl "The world's supply of happiness has diminished so that I can smile even wider."
    me "Is that bad?"
    sl "I can't afford such a sacrifice. Somebody might not get it, you know?"
    sl "And that's not a price I'm willing to pay."
    if alt_day6_us_7dl_px_sl_join:
        me "That's why you agreed so easily..."
        sl "Yes. Though it's not a decision either, it's a flight. {w}I'm a terrible coward, Semushka."
    "Helplessly shrugged this impossible girl."
    sl "I'm scared of hurting people, even if I have to take the hit in return."
    with fade
    sl "Launch a boat for me please?"
    "I didn't even pretend to be surprised. I'm used to it."
    me "Who do you want to find?"
    sl "Not for myself. I want a way for these two... irresponsible ones!"
    "I shook my head, trying with all my might to ward off the thought that there was... envy in Slavya's voice?"
    me "Right now?"
    sl "I'm afraid we simply won't have any more time."
    "With a wistful expression, she said."
    sl "Though you're probably right - we never had any."
    sl "I'm sorry I'm imposing here. {w}I'm going to go bring happiness to others."
    sl "Since I didn't get any."
    scene bg ext_boathouse_night
    with dissolve
    "Gone. But the guilt remains. {w}Or is it responsibility for those you didn't tell to piss off in time?"
    "Whatever you call it, it's all green and insignificant."
    "I'm sick of it. {w}Especially the silence."
    dreamgirl "I can't understand you, it's loud for you, it's quiet for you."
    th "And you, shut up."
    "My right palm was unbearably stinging - I must have been leaning it against a sharp edge for half an hour, unnoticed."
    "But it was something real that I was at least able to fight."
    "Not like trying to cut a water - what I was doing the last six months."
    with fade2
    "I could have done something!"
    "Something that..."
    with flash_red
    "With a cry, I twitched my arm, trying to escape the pain - but in vain."
    "It didn't seem to be piece of iron at all."
    "What was it, then?"
    "I had to part with the cozy darkness and the splash of water."
    "I opened my eyes with an effort - my right palm was red and sore."
    "For a second I suddenly imagined that a Flare had rolled across it - someone else's, on its way in search."
    th "Mine would never burn. {w}Right?"
    "Is it..."
    "Really?"
    "I wasn't sure of the answer, but I wasn't really intimidated by any prospect."
    "Particularly the risk of looking like an idiot."
    "Bringing the red palm close to my face, I looked it over carefully and, unexpectedly to myself, said:"
    me "Melt-melt, away you left..."
    "The palm glowed softly in the half-light - and from the center of it, forming a glow, a cozy yellow ball bounced onto my middle finger."
    "Angrily he jumped up, clearly unhappy with how long it took me to call him."
    me "Help us find our way elsewhere..."
    "I asked. And The Flare exchanged anger for mercy."
    "Rolling over my arm once more, mopping up the scars and burns with its light, rose into the air and, thinking, struck the twilight with all its might, piercing through it and pacing far, far away-somewhere to the north."
    "Fused with the starry sky, becoming just one of the stars."
    scene stars with dissolve
    "By some intuitive gut feeling I could trace his path."
    "Most importantly, I could trace his direction - he was looking for extra power."
    "On its own, the chick could do almost nothing except heal."
    "But when there were a lot of them..."
    "So he was looking for more chickens - to team up with them to help the foolish master again."
    "It must have been about an hour, for the music from the square died down completely."
    "The sky overhead became bottomless, and I finally lost faith in miracles."
    "But still I continued to sit and sit, alone, abandoned and almost weeping with self-pity."
    scene bg ext_boathouse_night with dissolve
    "And from across the chasms a piece of bark floated right under my feet, with a glow on its mast... A Flare."
    "I picked it up, and I heard a shout:"
    us "Hey, that's mine!"
    "Angrily waving her arms, Ulyana hurried toward me."
    "And only here, only now, did the needle - prick of anxiety in my heart - begin to let go."
    me "Ulyana."
    "Foolishly I smiled."
    show us normal sport with dspr
    us "Not for you I launched it, not for you to touch, got it!"
    "She pushed me aside."
    "And we stood side by side, watching the current carry another plea for help past us."
    us "That was it."
    "Ulyana declared as the ship finally disappeared into the darkness."
    us "To this day I owe nothing more."
    me "That's right."
    us "Sleep?"
    me "Uh-huh."
    hide us with dissolve
    "After turning around, I went to my place of lodging."
    stop music fadeout 3
    stop ambience fadeout 1
    return

label alt_day7_us_7dl_begin:
    scene bg int_house_of_mt_sunset with dissolve
    play ambience ambience_int_cabin_evening fadein 2
    play music music_7dl["will_you"] fadein 3
    "Day and night - day away."
    "A professional slacker and procrastinator, confidently finishes off the unintentional summer and buys ferry tickets home, to where the frost is."
    "Even though the weathermen brag that this year's December is almost the warmest it's been in sixty years, where is the heat?"
    "I can't feel it, hiding in my stone cave, I can't see it in the eyes and faces of passersby."
    "All of us, scowling, hurtling through the ice in the middle of nowhere."
    "More than that, I don't know why."
    if (counter_us_7dl_px == 3) or alt_day6_us_7dl_help:
        "And I'm so sick and tired of it, I'm sick and tired of it!"
        "I'm ready for any kind of movement to stir up this swamp."
        "It's easy, you pick a track, you look at it, you try it on."
        "And then you just give up and go where you want to go, not where the track takes you."
        if (counter_us_7dl_px == 3):
            "So The Old Road, wherever it leads me, is my chance."
    elif alt_day6_us_7dl_sl_friends == 2:
        "But even in this life-neglecting turmoil you can see something good."
        "All one has to do is to look closely!"
        "I don't think an adult can be so easily changed, much less by something as stupid as occupational therapy."
        "But a few hours side by side with Slavya did change something in me."
    elif (alt_day6_us_7dl_mi_friends == 3) or (alt_day6_us_7dl_un_friends == 3):
        "I didn't think about it yesterday, now my conscience torments me."
        "It's just my path, my choice to be forever smeared by the velocity of the rushing grayness."
        "I can't, have no right to drag anyone else there."
        dreamgirl "And what makes you think you're going to drag someone away?"
        th "I'll be back. It's inevitable, isn't it?"
        th "It'll be the same as always - the bus, the dream..."
        dreamgirl "Except you'll wake up alone. You're not God, Semyon."
        dreamgirl "You don't know how to make a girl you like out of snot."
        if loki:
            dreamgirl "Otherwise, a long time ago you would have had someone better than Ksana."
        elif dr:
            dreamgirl "Otherwise, you could easily make up for the loss you've been carrying around like a fool for the past year."
        else:
            dreamgirl "But well, you don't have to, though. You're strong and independent, with a cat."
        "I smiled, remembering last night's languid, warm evening."
        "It seems that there is a person walking beside you, happy."
        "Smiling, enjoying life."
        "But dig deeper and the truth comes out in all its unsightliness."
        "Maybe I shouldn't have poked into someone else's soul."
        if alt_day6_us_7dl_mi_friends == 3:
            "Shouldn't have felt sorry for the lonely starlet who died of loneliness."
            "Because everyone should have their own story."
            "It doesn't take much heart to go into each one."
            "My conscience will eat me up, constantly reminding me that I could have helped by intervening."
            "And I didn't."
            "That's why it's better to stay out of everyone else's soul."
        else:
            "All these tales of a lifelong romance and humble waiting since last year."
            "Lena won't wait."
            "She may be a quiet, modest woman, but in some cases she has a lot of determination."
    "For some reason I distinctly thought it was raining outside again."
    "It's pouring from the sky again with blurry melancholy, and you can take your time, not get up early to wave your arms and listen to another batch of the squad leader's ramblings."
    "You can sleep until nine o'clock, then throw something in your stomach..."
    "And with the full connivance of the leaders, go to bed before dinner."
    with fade
    "Except it wasn't raining."
    "There was no noise outside, no prickly spray blowing through the open window."
    "It was the most ordinary summer dawn outside."
    "Midsummer, the break of summer, the velvet season was yet to come."
    "And here it would be welcomed."
    "Not all pioneers are going back to town today, clever parents buy tickets for the whole summer."
    "And then they go to the sea!"
    "Or the other way around. To work, to work... To take Thursdays off from their shift to visit their child - and back again."
    dreamgirl "Cycle cannot be broken."
    th "Mock harder."
    "Olga Dmitrievna had already taken off somewhere, leaving me proudly alone."
    "However, judging by the fact that the loudspeakers were silent, the rise had not yet come."
    "The old trick for making yourself work: you have to set no deadlines."
    "Or set one, but a very big one, with plenty to do everything."
    "And a man just from idleness and a dangling reminder in his head will do everything precisely and accurately."
    "So it is here: I extremely leisurely got up, dressed, even made my bed."
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg ext_house_of_mt_sunset
    with dissolve
    "And all around is grace - I can't see a damn thing."
    me "Good morning!"
    "I shouted to nothing."
    dreamgirl "...mother! Mother! Mother!"
    dreamgirl "The echo answered familiarly."
    "From somewhere to the south, a gust of wind brought an answering shout."
    "There, too, someone had already managed to scrape himself off the bed."
    "He, too, must have been anxious to finally end this ordeal and find out what lay ahead."
    if (counter_us_7dl_px == 3) or alt_day6_us_7dl_help:
        if counter_us_7dl_px == 3:
            "So do I. I have an urgent, fainting need to get everything done, whatever the counselor demands of me."
            "Otherwise, I won't have time to run to where I shamefully retreated from yesterday before I leave."
            dreamgirl "Tactically."
            "I was in no hurry to admit to Ulyana that the people we were recruiting allegedly for the company, I needed for absolutely different purposes."
            if alt_day6_us_7dl_px_sl_join:
                "And Slavya... Well, that person is more solidly grounded than anyone I know."
                "And if thunder comes, if the cold streets pull me mercilessly toward them, as they did the last time, perhaps Slavya will be my salvation."
            else:
                "Ulyanka alone would simply not be able to hold me if cars drove by again, if the dampness of the Neva reeked, and if slumber knocked on my soul again."
            "Perhaps those who had already passed through here once before (and had they? That's the question) were much more protected than I was."
            "They simply had nowhere to go back to, so there was no fear of the unknown at all."
        scene bg ext_washstand_day
        with dissolve
        play sound_loop sfx_water_sink_stream fadein 1
        "Ulyana was already scrubbing her jaw when I approached the washbasins."
        "She greeted me cheerfully: she waved her arms, tried to yell something, but choked on the powder and coughed."
        if counter_us_7dl_px == 3:
            "She seemed to be pounding with anticipation, too."
        "With difficulty rinsing out the powder, she turned to me.{nw}"
        if alt_day6_us_7dl_help:
            show us laugh pioneer with dissolve
            extend " and grinned:"
            us "Look who the typhoon brought in!"
            us "It's Jacomo Kasemena himself!"
            me "You've got to be kidding me."
            us "How did you like last night?"
            me "I feel like a scoundrel and who seduced an innocent soul."
            "Mumbled I."
            if loki:
                me "So as if I didn't have to use a Makarov pistol."
                show us laugh2 pioneer with dspr
                us "If you behave, I'll put in a good word for you."
                me "Thank you, of course."
                us "And you won't get executed right away!"
            elif herc:
                show us laugh2 pioneer with dspr
                us "Are you going to repent after all?"
                me "Yeah, I'm a rapist and an abuser!"
                us "Abu-who? Oh, piss off! I don't even want to know."
            else:
                show us laugh pioneer with dissolve
                us "Strictly speaking, it was me who seduced you."
                me "How do you even know such words?"
                "Faintly I wondered."
                me "Aren't you a little young?"
                show us normal pioneer with dspr
                us "If you live with me, you won't be like that."
                "In the tone of a woman with a lifetime of experience, Ulyana said."
            "Just then I noticed the girl's rather strange attire."
            me "And why are you in uniform today? I thought you couldn't stand the uniform?"
            show us smile pioneer with dspr
            us "Why is that? I like it."
            us "And the skirt is pretty."
            "She picked up the edges of the skirt with both hands and twirled her arms left and right with a pie-girl look."
            us "I'm an excellent student and the pride of the class!"
            us "Really, I got mixed up with some bad company..."
            me "The company is Alisa?"
            "Ulyana nodded."
            show us laugh pioneer with dspr
            us "It's comfortable to run and climb trees in a sports uniform, it doesn't get in the way."
            us "But since I'm a fluttering mamzelle today, I'll wear a skirt and smile modestly."
            me "You? Modestly?"
            "I didn't believe it."
            me "Aren't you a walking disaster..."
            play sound sfx_water_emerge
            "I didn't have time to finish."
            "Ulyana turned in my direction, put her palm under the stream of water, and with a sniper salvo, she launched a shot of icy water right into my mouth."
            me "Ahem... Ahem... Disaster!"
            show us smile pioneer with dspr
            us "Tasty water?"
            "Businesslike, the obnoxious girl inquired."
            us "Want some more?"
            me "I'll give you more myself!"
            show us laugh pioneer with dspr
            hide us with easeoutright
            "I jerked sharply toward the wretch, but she had already jumped back and was breaking the distance with a laugh."
            "With a sigh, I turned back to the sink."
        else:
            show us laugh sport with dissolve
            extend ":"
            us "Hi, Syomych! Well, have you changed your mind?"
            me "Not at all."
            "I smiled."
            me "Hello to you too. Why are you so chipper and cheerful this morning?"
            me "There's still time to get up."
            show us smile sport with dspr
            us "I've been up all night! Aliska told me in confidence that it was a royal night, so we should expect friends with pasta."
            us "So we chatted with her until deep into the night."
            us "We waited and waited for you to come and visit. And you didn't come."
            show us laugh sport with dspr
            us "Aliska bet me a candy."
            me "I might have come. But I'm off right till morning."
            me "It was such a busy day yesterday, I was exhausted."
            us "That's all right. Look how exhausted you'll be today!"
            me "Aren't you going to pack?"
            show us normal sport with dspr
            us "If all goes well, we won't need any."
            "Ulyana unhappily snorted."
            us "But the most important things, of course, I'll take."
            me "The most important things?"
        us "Keep your head down, wash up!"
        stop sound_loop
        play sound sfx_close_water_sink
        hide us with easeoutleft
        "After closing the water and waving me goodbye one more time, Ulyana flew away."
    elif (alt_day6_us_7dl_mi_friends == 3) or (alt_day6_us_7dl_un_friends == 3):
        "And what's waiting for me?"
        "Well, leaving, that's understandable."
        "I have almost no belongings, nothing to pack, so I could spend time with my chosen one if I wanted to."
        "If only she wants to see me."
        if alt_day6_us_7dl_un_friends == 3:
            "Lena will probably be happy, though."
            "Maybe she'll stutter and blush a little, but she'll still end up smiling."
            "Her confession last night... The addiction is obvious. A real love addiction."
            "So as long as I feel a little better than average, there will be peace and quiet in her eyes, too."
            scene bg ext_washstand_day
            with dissolve
            "When I got to the washbasins, it turned out that someone was already waiting for me there."
            show un shy pioneer with dspr
            un "H-hi."
            me "Still nervous?"
            show un smile pioneer with dspr
            un "Rather, can't believe it."
            me "I won't run away."
            "I promised."
            me "And, well, where am I supposed to run to? I have to brush my teeth."
            show un smile2 pioneer with dspr
            un "You're always joking. Sometimes I think you can't be serious at all."
            th "Oh, you should know how serious I am where I live."
            me "Let me fool around. I don't have much time left."
            show un surprise pioneer with dspr
            un "Why?"
            me "Because departure."
            un "Departure. But you're not going anywhere off the bus. We'll get to town together, and..."
            "I smiled and stroked her head."
            "I'd lay a finger on it for everything to happen, like that sad girl says."
            "Except I know my luck, I know my karma."
            "No matter how big of a mess I've built up in my imagination, life will still make edits and surprises."
            "I have a quota of foolishness for the day, shaky fingers and a complete lack of luck in all endeavors."
            "So I don't even know how it's going to turn out."
            me "I'll leave you the address."
            "The promise was somehow very easy to make."
            me "Memorize it as best you can, just in case."
            me "If anything happens, you can find me one day."
            un "Are you going somewhere?"
            me "No."
            "I sighed."
            th "But no one's asking my opinion on that."
            show un normal pioneer with dspr
            un "Okay, don't worry about it."
            play sound sfx_open_water_sink
            play sound_loop sfx_water_sink_stream fadein 1
            "Lena nodded obediently, then leaned over the washbasin."
            hide un with dissolve
            "I followed her example, and when I unfolded, saw that I was alone again."
            "Lena left in English."
            stop sound_loop
        else:
            "I don't think her roommate would appreciate me, though."
            "Lena is kind of unsociable, sometimes I think it's all because of some childhood trauma."
            "Because a person who reads beautiful books shouldn't be like a shell, closed off, blinkered."
            "Have to get Miku outside, get in the way of her picking up her many thousands of Japanese bags."
            "For some reason I had no doubt that Miku must have an awful lot of bags, from stage costumes and cosmetics to everyday clothes... which are rejected here."
            "I don't understand why kids bring suitcases of stuff to this camp."
            "If parents know this place is full of everything, except for underwear... Logic is nowhere near here."
            "Unless it's to show off to each other on parents' days and on departure..."
            scene bg ext_washstand_day
            show mi normal pioneer at zenterright
            with dissolve
            th "Speak of the devil."
            mi "Hello, Sen."
            "The Japanese girl nodded to me."
            mi "How did you sleep?"
            me "Had nightmares."
            show mi shy pioneer with dspr
            mi "Nightmares? Weird! I mean, I'm... oops."
            mi "I mean, scary nightmares?"
            me "Come on."
            "I couldn't take it anymore and smiled."
            me "I'm just kidding. In fact, I blacked out until the morning."
            me "Although the last person I thought about yesterday was you."
            show mi happy pioneer with dspr
            mi "That's nice."
            me "I liked it, too. That's why I didn't have time to understand the difference between falling asleep and waking up."
            mi "I hope you thought only good things?"
            th "What can I say..."
            dreamgirl "Good, good! Since it was good for you, it's definitely good!"
            me "Did you bring a lot of stuff with you?"
            mi "Not much, but I won't refuse help! Uncle Borya helped me on the first day, but now there are no helpers."
            mi "By the way, do you know why there is no horn? It's half past nine on the clock."
            th "So I'm woke up not before everyone else?"
            me "Who knows?"
            me "Maybe the radio's broken?"
            dreamgirl "The radio man got drunk and didn't go to work. From happiness."
            me "Maybe on the departure day all those things don't work."
            show mi upset pioneer with dspr
            mi "What about breakfast then? We'll be late!"
            me "We won't be late! Now let's wash up in a hurry and run to the canteen!"
            play sound sfx_open_water_sink
            play sound_loop sfx_water_sink_stream fadein 1
            "Miku and I exchanged glances and, bending over the sinks in sync, started to brush."
            stop sound_loop fadeout 3
    stop music fadeout 3
    stop ambience fadeout 3
    with fade
    return

label alt_day7_us_7dl_breakfast:
    scene bg int_dining_hall_people_sunset_7dl with dissolve
    play ambience ambience_dining_hall_full fadein 3
    play music music_7dl["will_you"] fadein 3
    "The sleepy, sour pioneers settled into their seats, only the first squad again had to stand in line at the handout."
    "Now, for some reason it was incredibly infuriating."
    "It was as if you'd stepped up to the podium for an encore."
    "To the audience's much-loved shooting of the naked soul, watch it soar down from the eighth floor."
    "Hear that? That cry for help, touching, isn't it?"
    "There was a distinct reek of cold in the air and a reluctance to let summer end."
    "The pioneers worked busily with their spoons, but they talked reluctantly, and looked more inward, into themselves, than at others."
    "And I was one of them, too."
    dreamgirl "This music makes me sick, these songs make me shake..."
    th "Then what's it all for?"
    dreamgirl "Do I know? There's something vicious about this whole system of camps, meetings and breakups."
    dreamgirl "It's as if children are being toughened up, taught to live with a broken heart."
    th "Or maybe it's the other way around? Teach them to make friends, to make buddies..."
    dreamgirl "Lovers. And break up with them."
    dreamgirl "Lucky if you and your girl live in the same city. And if not?"
    if dr:
        dreamgirl "Think of your Ryoko for example."
        "I frowned."
    if alt_day6_us_7dl_help:
        play sound sfx_pat_shoulder_hard
        "And then a small but firm hand flew on my shoulder."
        show us laugh pioneer with dspr
        us "Don't be sour!"
        "I was cheered up by «mamzelle»."
        me "Uh-huh... Hang from the ceiling."
        us "Didn't you get enough sleep?"
        us "Or are you offended by the water shenanigans?"
        me "No."
        "I'm just waving it off."
        me "Just a bad mood, it happens to me."
        show us normal pioneer with dspr
        us "It's all nonsense."
        "Ulyanka declared authoritatively."
        us "That's because you're a boo and a spiteful person. You fill your head with nonsense."
        me "Oh. Well, that's what I thought."
        "I nodded accordingly."
        show us shy pioneer with dspr
        us "And then you also drive the girl crazy with this nonsense."
        me "And who, do you think, I drove crazy?"
        show us laugh pioneer with dspr
        us "Me, of course!"
        us "See, I even dressed up today because of you!"
        me "In uniform?"
        us "Appreciate it!"
        me "Appreciate it, appreciate it..."
        "I nodded, fighting the urge to strangle this little shit again."
        us "Will you go to walk with me after breakfast?"
        me "Should I?"
        "In tone I asked."
        show us normal pioneer with dspr
        us "We've got to get you out of the abyss of depression!"
        me "Where'd you get those words again..."
        show us smile pioneer with dspr
        us "Remember, I'm an excellent student and a very smart girl."
        us "Yes! And also very pretty."
        me "And modest..."
        us "Yes! Are you coming?"
        me "Yes, of course I'm coming."
        "Can't refuse now."
        us "Then it's a deal!"
        hide us with easeoutleft
        "Ulyanka evaporated, leaving dirty plates on me again."
        "Some things in this world don't change at all."
    elif alt_day6_us_7dl_mi_friends == 3:
        show mi smile pioneer with dspr
        "Miku, who pushed through the line and stood next to me, wrinkled her nose questioningly:"
        mi "What are you, Seneca, unhappy? Why are you hanging your head?"
        me "Grief is gnawing at my breast..."
        "I'm singing in tune."
        me "And the boat's driving me on..."
        show mi laugh pioneer with dspr
        mi "You're so funny! And Olga Dmitrievna told me that you're always walking around angry, shunning people."
        me "She didn't lie."
        "I confessed candidly."
        me "I do shun people."
        mi "How can you shy away when you talk to me and don't even try to get away quicker?"
        "She sighed furtively, apparently recalling a couple of precedents."
        show mi upset pioneer with dspr
        mi "Or... Are you implying that I'm not a human?"
        me "No. You're a human for sure. But for your sake I'm making some exceptions."
        show mi smile pioneer with dspr
        mi "Even so? Thank you, I'm flattered."
        th "But, nothing will grow out of this exception anyway. It won't make it."
        "I added to myself."
        mi "It's always gratifying when a person is able to do something for you that they wouldn't normally do."
        mi "Change shows he cares."
        me "Don't overdo it."
        "Struggling with the approaching déjà vu I asked."
        me "I'm just trying to do right by my conscience."
        show mi laugh pioneer with dspr
        mi "Oh, you sound almost exactly like Slavya!"
        me "Mimicry."
        "I agree."
        mi "Yea, I already see a braid growing on your head."
        show mi smile pioneer with dspr
        "Miku chuckled."
        "And then she asked right in the face:"
        mi "Will you help me pack?"
        "At first I thought I'd misheard."
        me "Do you really want me to pack your personal things?"
        show mi serious pioneer with dspr
        mi "Personal, probably not."
        "Miku stretched thoughtfully."
        mi "But all machinery is better left in men's hands - that's what Pa always told me."
        me "He's the right man. Reasonable advice."
        mi "So will you help me?"
        me "Of course I will."
        show mi happy pioneer with dspr
        mi "Oi thanks! I'll be in my cabin then!"
        hide mi with dissolve
        "She got up, winked at me goodbye, and disappeared."
    elif alt_day6_us_7dl_un_friends == 3:
        "Lena, who was standing next to me, exchanged an understanding look."
        show un normal pioneer with dspr
        un "You feel it too, don't you?"
        me "What?"
        un "People. It's like they're saying goodbye. Such a funeral ritual."
        me "Well said, funeral ritual."
        un "Because it's true."
        "Lena was surprised."
        un "All this time it was as if they were living, starting a new life, which like shoes would be left at the camp gate."
        un "And it's hard to rebuild. That's why they bury themselves alive, forgetting that they somehow lived in the city, too."
        me "And you?"
        show un serious pioneer with dspr
        un "And I'm - where you."
        "A girl brought it to my attention."
        show un smile2 pioneer with dspr
        "She suddenly smiled and sang softly:"
        un "If you're out on the road with a friend, if you're out on the road with a friend..."
        "She picked up the filled tray from the serving table and, nodding to me, went into the hall."
        hide un with dissolve
        "I was right behind her, so it wasn't even a couple of minutes before I rejoined the girl at the table."
        show un smile pioneer with dspr
        un "Do you think they're pointing the finger at us yet?"
        me "Why?"
        un "We've practically been walking hand in hand since last night. It's not quite usual in the camp."
        me "That's the least of my worries."
        "I muttered."
        me "You tell me if anybody points a finger, I'll break that finger."
        show un serious pioneer with dspr
        un "What a touching reaction."
        "She didn't move an eyebrow, she must have been preparing for that answer."
        "Or, on the contrary, did she expect me to crumple and mumble?"
        if loki:
            "Self-control was instilled in me almost before I was taught music."
            "Though in many years of hermitage, it was already shabby and dusty."
            "Lying in a far corner of my memory like an old leather raincoat."
            "But I could pick it up at any time, dust it off, and try it on again to see if it was too tight on my shoulders."
        me "I don't really care."
        me "I've stopped having doubts since last night."
        show un shy pioneer with dspr
        un "And I..."
        "Lena whispered."
        me "Doubt?"
        show un sad pioneer with dspr
        un "Afraid. It's like I'm lost in my thoughts and dreams, and now I'm afraid I won't be found."
        un "You flicker among them a lot, so I'll just wake up from you one day, and then..."
        "She shook her head."
        un "No, I don't even want to think about it."
        me "Don't think about it. Let's just talk."
        show un smile pioneer with dspr
        un "I wouldn't mind."
        "Lena smiled."
        un "But I can't, when there are so many people around."
        me "So let's finish eating and go somewhere where there are no people."
        show un smile3 pioneer with dspr
        "She shined:"
        un "Let's go!"
        un "Will be waiting for you on the porch."
        hide un with dissolve
        "She finished her tea in a gulp and got up from the table, gathering the dirty dishes."
    else:
        "I didn't want to think about it, didn't want to remember things I should have forgotten long ago."
        "It was as if it were my past, but from here, it looked like the future."
        "And in a very different place, too, where the stone buildings cast sharp, contrasting shadows on the pine cushion, and the lush bass of a slow song burst out of the dance floor's wide-open doors."
        "Echoing the silent cry of the invisible - how to pick the right words to tell a man that it's about to get painful and bad, and maybe even long."
        "But things are bound to get better in the end."
        "It always gets better - the grid of scars on my heart is evidence of that."
        "I left only tea and two sandwiches on the tray - I didn't feel like eating at all."
        "I thought something in this camp was going to change me for the better."
        "But the hopes of the southern sun had crumbled - nothing in me had scorched and purged, leaving me naked and present."
        "I remained the same cold and sullen Semyon, who had failed to beguile the magical tale of a dwelling of happiness existing under an impossibly blue sky."
        "The only thing I regretted was that I had left my Walkman in the cabin, and now I really wanted to plug my ears from the noise, to abstract myself and remind myself once again that I was not with them."
        "After letting my tea and sandwiches go to their proper purpose, I headed for the exit."
    stop music fadeout 3
    stop ambience fadeout 1
    return

label alt_day7_us_7dl_photo:
    scene bg ext_dining_hall_near_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 3
    play music music_list["went_fishing_caught_a_girl"] fadein 5
    "As it was written in the old librettos: same people, same place."
    "When I came out of the canteen, Ulyana was sitting on the railing with her back to me and throwing at the classics drawn on the ground, each time aptly hitting the «cauldron»."
    "I tried to walk quietly, and before me and after me the door slammed the same way, letting the fed-up pioneers through."
    "But only in my case did the girl's shoulders flinch a little, and she turned in my direction."
    "Instantly she jumped off the railing and ran up to me."
    show us smile pioneer with dspr
    us "Took you long enough."
    "She chided me."
    me "You have to chew carefully to make your stomach work."
    "Really, you can't take a lecture from a little girl who sweeps everything off the table like a meteor."
    "It's not like I'm late for a date."
    th "Or..."
    show us laugh pioneer with dspr
    us "Well, don't just stand there, let's go!"
    "She shouted, grabbing my hand."
    me "Where to?"
    show us laugh pioneer with dspr
    us "You're stupid, Syomych! You wanted to walk! Let's go for a walk! Let's go!"
    "Apparently, she already had a cultural program."
    "And to the first point of that program she was dragging me now."
    "I could only hope it wouldn't be the cabin, clubs, or pier."
    "These were places with which I had formed very strong negative associations."
    scene bg ext_square_day with dissolve
    me "Will you tell me where we're going for a walk?"
    me "Or is that classified information?"
    "Demanded I, when we came out into the square."
    show us smile pioneer with dspr
    us "Secret!"
    "She was obviously pleased with herself."
    "Her blue eyes were so full of slyness that I automatically assumed she was planning some sort of parting mischief."
    me "Don't forget."
    "I reminded her, just in case."
    me "You're a mademoiselle in a skirt tonight, so you must behave decently and not annoy others."
    show us laugh pioneer with dspr
    us "I'm behaving very decently! More decent than anyone else in the world!"
    us "You remind me of my grandfather when he takes me to the park."
    us "He's always grousing about how to behave and conform."
    me "He's right, by the way!"
    show us smile pioneer with dspr
    us "It's high time those who are responsible for us understood!"
    "With her finger outstretched, she said."
    me "And I'm responsible for you?"
    show us laugh2 pioneer with dspr
    us "You're dragging me around the camp by the hand. What do you think?"
    me "I don't think, I ask."
    us "You'll see, let's go!"
    scene bg ext_playground_day
    with dissolve
    "She pulled me toward the soccer field, where some boys were already playing."
    "They responded with a welcoming shout - they seemed to know my companion, and they knew her quite well."
    show us normal pioneer with dspr
    us "Second squad's team."
    show us smile pioneer with dspr
    us "Last game we beat them 3-2."
    "She bragged."
    me "That's where Danya is from?"
    us "Danya doesn't play soccer, he's got better things to do. All right, let's go!"
    "I think I'm beginning to guess where she's taking me."
    "The question is, why?"
    stop music fadeout 3
    play sound sfx_open_door_kick
    pause(1)
    play ambience ambience_int_cabin_day fadein 3
    scene bg int_sporthall_day_7dl
    show us laugh pioneer
    with dissolve
    play music music_list["eat_some_trouble"] fadein 5
    us "Uncle Borya, I'm here!"
    "The girl screamed, kicking the door open."
    ba "And there's no reason to yell like that."
    "A voice came to us from across the hall."
    play sound sfx_open_cabinet_2
    pause(1)
    show us laugh pioneer at right
    show ba em1 uniform at left
    with move
    "A second later, the door clicked shut, unnoticed until now, releasing the gym teacher to us."
    "I caught a glimpse of the fact that the lighting in the room behind him was sparse."
    ba "Wow, you even brought the wimp with you."
    ba "Stubby, what are you doing dragging around with the kid? If I'll know you've being hurting her..."
    "He waved a fist as big as my head."
    show us smile pioneer with dspr
    us "Uncle, I'm here for the cards!"
    show ba smile uniform with dspr
    ba "Right."
    "He smiled."
    ba "Wimp, do you need one too?"
    me "What?"
    ba "Well, well..."
    "The gym teacher scratched the back of his head and turned to Ulyana:"
    ba "Why are you associating your life with a retard?"
    if loki:
        me "Hey, I'm still here!"
        "I couldn't take it."
        ba "It's okay. I forgive you."
    else:
        "I blushed with anger, but decided to ignore the asshole."
    show us laugh pioneer with dspr
    us "Cards, you fool! Photos!"
    me "What kind?"
    show us sad pioneer
    show ba em1 uniform
    with dspr
    "The girl and the bear looked at each other and gave me the same sympathetic look."
    "I felt like an idiot."
    dreamgirl "Habitual existence, eh?"
    "The inner voice didn't fail to take advantage of the opportunity, either."
    show us normal pioneer with dspr
    "Ulyana sighed:"
    us "I thought you knew! Uncle Borya not only teaches gymnastics, he's also a photographer."
    if (counter_sl_cl >= 5) or (('soccer' in list_joined_clubs_7dl) or ('volley' in list_joined_clubs_7dl) or ('badmin' in list_joined_clubs_7dl) and not alt_day4_me_neu_escape):
        me "And what, he's just going to give them away?"
        us "Why not?"
    elif alt_day2_mi_snap:
        me "I saw him with a camera once, but I thought it was just pampering."
    else:
        me "I've never seen him with a camera."
        "I didn't believe it."
        show ba normal uniform with dspr
        ba "Because you have to open your eyes off sometimes."
        ba "By now, they should probably be developed."
    hide ba with moveoutleft
    "The gym teacher went back into the dark room, flicked the switch."
    "Outside lay a path of red light."
    me "The red room!"
    show us smile pioneer with dspr
    us "You figured it out at last."
    show us surp1 pioneer with dspr
    if (counter_sl_cl >= 5):
        me "I didn't know it was this serious."
    else:
        us "Uncle Borya tries to take pictures of all the important moments in camp, you know what a stockpile of pictures he has, wooooo!"
    if alt_day2_mi_snap:
        me "I wonder if he'll give a picture with Miku...?"
    else:
        me "Where did he get my pictures? I don't remember him taking pictures of me."
    show us normal pioneer with dspr
    us "Don't worry, there's a couple for you, too. Well, what is it?"
    show us smile pioneer far at cright
    show ba normal uniform at left
    with move
    "She ran up to the gym teacher coming out of the closet."
    ba "I've got something. There's almost a dozen with you, but I won't give you all of them."
    show us dontlike pioneer far with dspr
    us "Whyyyyyy? I'm on them, they're mine!"
    show ba normal uniform with dspr
    ba "Because the best ones will go to the camp archive! You want to find yourself in an album later, don't you?"
    us "I don't want anything, let me, let me, let me!"
    "She jerked, trying to snatch the pictures from Sanich's hands, but he elusively lifted them higher, to a place where Ulyana, if she wanted to, would not have been able to jump."
    ba "So, 'starts' in any case go to the archive, the squad at the first disco too."
    "Mumbled the gym teacher, flipping through small 10x12 cards."
    ba "Well, take this one, I have two of them."
    ba "This one too..."
    ba "And that's when your wimp arrived, snapped it just in time. Take that one."
    if (alt_day_binder != 1) and (counter_sl_7dl == 0) and not herc:
        if loki:
            "Ulyana clutched the picture and, looking closely, blushed."
            show us shy pioneer far with dspr
            us "What a bug you are, Uncle Borya! You stood there on purpose!"
            me "What is it?"
            "I got curious."
            show us shy pioneer with dspr
            us "Nothing."
        elif dr:
            show us smile pioneer far with dspr
            "Upon receiving the pictures, Ulyana was the first to be enamored."
            show us laugh2 pioneer far with dspr
            "Then she shifted her gaze to me and laughed."
            us "Ahaha, what a great shot!"
            me "What is it?"
            show us laugh2 pioneer with dspr
            "I got closer, and the evidence of shame was revealed to me."
            "There were three actors on it."
            "Alisa."
            "Ulyana."
            "And, as Sanich put it, a wimp."
            "The latter looked deplorable."
            "Who wouldn't be, being doused head to toe with standing water from a fire barrel with a fire cone on his head."
            "Ulyana was exhausted with a giggle:"
            show us laugh pioneer with dspr
            us "Oh, I can't! That's us then... when we met! Ahahaha!"
            me "Give it to me, I'll tear it up."
            us "Oh, I won't."
    else:
        "I caught a glimpse of some white blur before the picture was pulled out from under my nose."
    "Ulyana exaggeratedly carefully tucked the pictures away in her pocket."
    me "And there's nothing for me?"
    show ba em1 uniform with dspr
    ba "And you, wimp, did you have time to become famous for something?"
    "Maybe I have..."
    me "Maybe I have. Maybe I didn't."
    show ba smile uniform with dspr
    ba "Don't be sour, you wimp. Here. There's a little present for you, too."
    "He handed me another wet picture."
    "What did I find on it?"
    "Oh, of course."
    scene
    $ renpy.show("bg int_sporthall_day_7dl", what = Desat("bg int_sporthall_day_7dl"))
    show cg d6_us_photo_7dl
    with dissolve
    "Chasing one extremely annoying ghost."
    "It's in the duvet, and I'm the one waving my shorts over my head."
    th "Fifteen minutes of fame."
    ba "I made another copy, it's going in the archives, too."
    scene bg int_sporthall_day_7dl
    show ba smile uniform at left
    show us normal pioneer close at cright
    with dissolve
    us "What's in there? Show me!"
    me "No. That's my picture!"
    us "Let me see it, I won't take it away!"
    "With a sigh, I reluctantly handed her the card."
    "Of course, Ulyana clung to it like a tick!"
    show us sad pioneer close with dspr
    us "Gimme, gimme! Come on, please!"
    me "Yeah, and then I'll have nothing at all!"
    me "Have a conscience, you have four and I have one!"
    show us calml pioneer close with dspr
    us "You're greedy, aren't you? Give it to me!"
    "She ripped the picture at herself."
    scene
    $ renpy.show("bg int_sporthall_day_7dl", what = Desat("bg int_sporthall_day_7dl"))
    show cg d6_us_photo_7dl
    with dissolve
    "And I ripped it at myself…"
    play sound sfx_7dl["paper_torn"]
    show cg d6_us_photo_torn_7dl with flash
    "And the card split in half with a paper crackle, leaving a ghost on one half and a 'hunter' with shorts on the other."
    stop music fadeout 1
    "There was silence in the room."
    scene bg int_sporthall_day_7dl
    show ba evil uniform at left
    with dissolve
    ba "Children, children..."
    "The gym teacher sighed."
    ba "Is there anything you can be trusted with?"
    show us sad pioneer at cright with dissolve
    "It was pathetic to look at Ulyana."
    us "Well... Maybe she could be glued?"
    ba "A picture?"
    ba "Who would glue a picture? Certainly not me."
    show us normal pioneer with dspr
    us "And I'll do it myself! I'll take..."
    me "Blue duct tape."
    "I hinted to her."
    us "Yes! Blue duct tape, and..."
    ba "I knew there'd be trouble."
    "He flipped through the stack of pictures one more time and gave Ulyana an exact copy to replace the torn one."
    show ba em1 uniform with dspr
    ba "We'll have to leave the archive without this masterpiece."
    ba "And for you, wimp, I've got nothing else to offer. I'm sorry, but you can't even be trusted with this."
    me "What's that got to do with me?"
    ba "It's because you're a loser. Now go. Don't rub it in."
    hide ba with dissolve
    "Letting it be known that the conversation was over, he staggered back to the developing room."
    show us sad pioneer with dspr
    us "I'm sorry, Syomich."
    me "Yeah..."
    "I picked up the scraps from the floor."
    th "Maybe I could use some transparent scotch tape..."
    dreamgirl "And then there's digitizing and a little Photoshop touch-ups."
    dreamgirl "Wake up! There won't be any of that here for another ten years."
    th "Whatever."
    "I jerked my head stubbornly and hid the scraps in my pocket."
    "For some reason it seemed like something extremely important."
    "To whom?"
    "Well, there was no answer to that question."
    stop ambience fadeout 3
    play sound sfx_open_door_2
    pause(1)
    return

label alt_day7_us_7dl_treehouse:
    scene bg ext_playground_day with dissolve
    play ambience ambience_camp_center_day fadein 6
    play music music_7dl["iwantmagic"] fadein 3
    "Still in the same silence, we walked out of the gym into the street."
    show us normal pioneer with dspr
    us "Are you sulking?"
    me "It wasn't so long ago that you didn't care."
    us "Well, I'm a proper and well-mannered mamsel now, remember?"
    me "Uh-huh."
    us "Syomich, stop it."
    me "Oh please."
    "I waved my hand."
    us "I know how to cheer you up! You know how?"
    me "I don't even want to guess."
    show us smile pioneer with dspr
    us "Don't be a drag, let's go!"
    "That's it, the girl had thirty seconds of conscience, mission accomplished, box ticked off."
    "The square, the cabins, the canteen, flashed by again..."
    scene bg ext_backroad_day_7dl
    with dissolve
    "As it turned out, our path lay beyond the territory."
    "After finding a tree she knew well, Ulyana told me to wait, and she climbed up."
    th "In the skirt. She's completely out of her mind."
    dreamgirl "That's right. If you were a normal person..."
    th "Leave those vile innuendos out of it."
    "Something shook from above, pine needles sprinkled on me, and a pinecone neatly pounded on the top of my head."
    us "Syomich, get in!"
    me "How?"
    us "Go around the tree, you dumbass, there are steps!"
    "Following her advice, I went around the pine tree and indeed found wooden planks nailed right on top of the bark, which with some wiggle might well serve as stairs."
    "For someone like Ulyana."
    "And for me?"
    "With a sigh, I spat on my hands and, fittingly, began my ascent of Everest."
    with fade
    "The journey cost me a few abrasions on my arms and legs, but in the end I conquered this peak as well."
    "How could you not?"
    "True, I ended up almost toppling down when the branches above me suddenly spoke."
    dreamgirl "In a human voice!"
    us "Be careful up here, don't mess me up."
    scene bg ext_tree_house_7dl
    show us normal pioneer
    with dissolve
    "When I looked up and took a closer look, I found what I expected to see."
    me "A hut."
    show us dontlike pioneer with dspr
    us "Hey, it's a palace!"
    me "Yeah."
    "I agreed."
    me "A palace on a tree."
    scene bg int_tree_house_7dl
    show us normal pioneer
    with dissolve
    "It was almost invisible from below; if you don't know where to look, you can't see it!"
    "But if you climbed..."
    "There was a pinned platform of planks, covered by a tent of twigs."
    "Here were some boxes and two stakes, apparently used as chairs."
    "There was plenty of room for the two of us, and there was even a kind of recliner a little further away that I could have fit into."
    "With my knees tucked in, of course."
    stop music fadeout 3
    us "So, how do you like my palace?"
    play music music_7dl["lastlight_guitar"] fadein 3
    me "Is it yours?"
    us "Well..."
    "Ulyana averted her eyes."
    us "Not really mine, of course!"
    us "Aunt Olya showed it to me, a long time ago! But then it was just a big box between the branches."
    us "And now look - you can even live here!"
    me "Live?"
    show us smile pioneer with dspr
    us "I even spent the night here once. Our troop went to find me, and Auntie Olya went and found it right away."
    us "As if she knew!"
    me "Did she really build it herself?"
    show us laugh pioneer with dspr
    us "Her? No, of course not! It was Mirya!"
    if counter_us_7dl_px >= 1:
        me "There's that Mirya again."
        "I grumbled."
        me "Like Strelok, practically. Ubiquitous, omniprese..."
    us "He built it! He lived here!"
    me "And what, no one was looking for him?"
    show us laugh2 pioneer with dspr
    us "Who would be looking for him? If he ran away, the whole camp could breathe easy."
    us "So he ran, and ran, and ran... And ran too much."
    us "He once found something..."
    me "What?"
    if counter_us_7dl_px >= 1:
        us "I've told you before."
    else:
        us "I don't know how to explain it, but he always thought there was something wrong with this camp."
        us "He was trying to find and figure out what it was."
    me "Did he find it?"
    show us sad pioneer with dspr
    us "He did. But it was too late."
    us "Mirya later regretted it very much - the road was closed for him."
    us "He said something about childhood, I couldn't remember."
    us "Left a trail, and I, instead of looking for it, am sitting with you now."
    show us shy pioneer with dspr
    us "And guess what?"
    me "What?"
    us "I don't regret it one bit!"
    us "Somehow I know that both you and I can try again one day!"
    us "And we'll make it!"
    us "We just have to not grow up. Let's promise each other, shall we?"
    me "Not growing up?"
    dreamgirl "And it's so scary to wake up one day as an adult..."
    us "For as long as we can."
    me "Do we have the right to that promise?"
    show us cry pioneer with dspr
    us "And I don't care!"
    "The girl's eyes gleamed."
    us "I want to! I have the right not to think about all your adult nonsense!"
    me "So it's 'yours' after all?"
    show us normal pioneer with dspr
    us "Okay, not 'your'. What's the other way around? Theirs."
    "I grimaced."
    me "Just 'their'."
    "For a split second I felt creepy, as if those same 'Theirs' were standing on the other side of the high wall cutting us and them off, and peering over the wall, overhead."
    "They're tall, huge, and we really have no business in their world."
    "They've all learned from incompetent teachers in a lying-through school of life, and now their graduate degrees are only good enough to flicker under the gray clouds as a blue crust and spread out on the cold surface of the Neva."
    "I was dreadfully reluctant to go to them."
    "But who asked my desire?"
    us "Well? Promise?"
    me "I promise."
    us "Wrong. Let's do it the normal way?"
    me "How?"
    show us smile pioneer with dspr
    us "Pinkie Swear! It's never broken!"
    me "It doesn't break?"
    us "Yes."
    "She held out her fist to me with her pinky finger outstretched."
    us "Grab it!"
    "And I, feeling like the last fool, grabbed her little finger."
    us "I swear..."
    me "I swear..."
    us "To never grow up..."
    me "To never grow up..."
    "The words dripped and dripped into the silence of the wary morning forest."
    "And believed now that this oath and truth would help cheat the immutable laws of existence."
    "And every year it would be like this - a little girl with scarlet hair and a slightly older teenager sitting across from her with long bangs."
    "No one asked for my wish. Nobody."
    "It's just that I'm used to the fact that one day it's going to happen this way and not any other - and me, the relentlessly young looking inside, and me, the lazy and already aged piece of meat, are going to get further and further apart."
    "Until young me one day stops opening my eyes altogether."
    th "I don't want to!"
    "A cry rumbled in my chest."
    th "I don't want to!"
    us "Don't get big and stupid..."
    us "Stay always as I am..."
    us "I swear!"
    "And I bellowed with a fervor that surprised me:"
    me "I swear!"
    show us sad pioneer with dspr
    us "Mirya swore, too."
    "Ulyana looked away, letting go of my little finger."
    us "Except he's studying somewhere in Kirov now."
    us "Grown up, big."
    us "A stranger."
    me "With me it will be different."
    us "I wish."
    "Ulyana sighed."
    us "I wish. Let's go to camp before they miss us."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day7_us_7dl_packing_us:
    scene bg ext_house_of_dv_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    play music music_7dl["more_than_alive"] fadein 3
    th "You saw me off at the outskirts..."
    show us normal pioneer with dissolve
    us "Aren't you going to pack?"
    "I spread my hands:"
    me "To a beggar to pack is only to gird himself."
    me "Especially since the most important thing got drowned by your fault."
    show us surp2 pioneer with dspr
    us "So dive in and get it!"
    me "No. First of all, it's awfully cold."
    us "Do you want me to dive in?"
    me "Didn't you hear me?! It's freezing!"
    show us fear pioneer with dspr
    "I barked, and Ulyana was silent in a moment."
    "She looked at me sideways."
    us "You're a dangerous man..."
    me "And secondly, it doesn't work anymore."
    me "So there's no point."
    show us normal pioneer with dspr
    us "So there's nothing to pack?"
    me "Just a change of clothes. I'll leave the uniform in the closet."
    show us smile pioneer with dissolve
    us "Then... will you come in? Help me pack."
    "You can't refuse an offer like that."
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg int_house_of_dv_day with dissolve2
    play ambience ambience_int_cabin_day fadein 6
    "When I walked in, I found that Alisa's half had already been thoroughly cleaned up, her things were gone, her bedding was missing, and her mattress and blanket and pillow were rolled up in a neat roll in the headboard."
    show us normal pioneer at zenterleft
    with dissolve
    "Alisa certainly wasn't going to stick around for an extra second."
    me "She doesn't like camp, I guess?"
    "I said thoughtfully."
    th "Always going somewhere, doing something. {w}And why don't you ask her what?"
    th "It's pretty obvious how she would answer a question like that. {w}Nothing censorious, nothing of substance."
    me "It's as if she's trying to escape from here, as if she's doing her prison time here."
    show us surp1 pioneer with dspr
    us "Don't you know?"
    me "Regarding what?"
    us "Alisa is not here of her own free will. {w}She was exiled here by her parents."
    me "Wasn't her opinion asked?"
    show us surp2 pioneer with dspr
    "Ulyana stared at me in a kind of amazement."
    us "Are you stupid or something? Who asks a child's opinion on such things?"
    th "Well, let's just say I was asked."
    "I've gone to one and only one camp all my life. {w}A place I loved near the Finnish border."
    "Tried a couple of times to change locations - thought maybe other places were just as good."
    "No. It's not the same. Not the same atmosphere, not the same spirit."
    "The place you want to go back to sounds and looks very different."
    "And it breeds fans already of the jaded, sitting in social media groups, collectively pining for the irretrievably gone, gathering in squads and cavalcade in five cars, getting out sometimes to the place where they once understood the meaning of 'happiness.'"
    show us laugh2 pioneer with dspr
    us "Well, I'm lucky to have Auntie Olya, so I like camp, too."
    me "So camp is just a place for you?"
    show us laugh pioneer with dspr
    us "What else?"
    "She laughed."
    me "Indeed..."
    "Now her panicked reluctance to grow up was obvious to me."
    "She must be terrified of one day becoming one of those cavalcade people."
    "To arrive where she's been drawn to for the last ten years."
    "And find there only a gatehouse guarding no one else's territory."
    "To climb up the slope and realize, with horror and a sinking heart, how essentially tiny the place was."
    "We all, as children, have a secret feeling that this isn't forever."
    "Perhaps that's why we are in such a desperate hurry to live."
    show us grin pioneer with dspr
    us "Are you also going to say that the camp is first of all people?"
    me "Aren't they?"
    show us smile pioneer with dspr
    us "I don't think so."
    "The girl shook her head."
    me "Why?"
    us "Why do you think? None of ours will come here next year."
    us "Neither Liska, nor Tisha, nor Slavya and Zhenya."
    show us normal pioneer with dspr
    us "I mean, the latter two will come. But to work."
    us "Will it make the camp worse?"
    "Even though there was truth in what he said, I couldn't agree with it for some reason."
    me "But if you take everybody and move them all somewhere else..."
    "I began."
    show us surp1 pioneer with dspr
    us "It's going to be a reunion night!"
    "Ulyana finished her sentence ruthlessly."
    us "You know how many of them I've seen!"
    me "Where could you have seen them?"
    us "But I have! That's not it at all."
    me "Meeting night...{w} But I was talking about another camp. Imagine: the same squad leader, all of us together..."
    show us grin pioneer with dspr
    us "It won't work, Syomich."
    "Smiled the girl."
    us "You think you're the first one so smart?"
    me "Why not?"
    show us dontlike pioneer with dspr
    us "That's because it won't be the same."
    us "Even if you get us all in here next year, it's not the same!"
    me "Why not?!"
    us "Because there'll never be anything like today."
    us "There's nothing to even try."
    "Very maturely said Ulyana; these words didn't sound like something imposed from the outside: she really thought so."
    me "Then what to do?"
    show us normal pioneer with dspr
    us "What to do... Live. Don't forget your vows and remember your friends."
    me "Oh yeah, I'll forget you alright..."
    "I grumbled."
    show us grin pioneer with dspr
    us "Is there something you don't like?"
    "Innocently said the little girl, fluttering her eyelashes."
    me "No, I like everything. And so do you."
    us "There! You should tell yourself that more often."
    us "Even when things get boring. Especially when you're bored."
    me "Does that help in any way?"
    show us shy2 pioneer with dspr
    us "Will our silly oath help us?"
    me "I don't know."
    show us sad pioneer with dspr
    us "Neither do I..."
    "She didn't finish."
    stop music fadeout 8
    play sound sfx_open_dooor_campus_1
    pause(1)
    show us normal pioneer at left
    show dv grin sport at zenterright
    with move
    play music music_7dl["shehasgone"] fadein 3
    dv "Are you two lovebirds cooing?"
    "Alisa gave us a condescending look."
    dv "And there will be no lunch."
    show us calml pioneer with dspr
    us "What do you mean?"
    dv "Like that."
    "Cut off Alisa."
    dv "The carriage came early, so everyone has an hour to pack, they'll give out some munchies on the bus."
    show dv sad sport with dspr
    dv "They have everything in one place..."
    me "What the hell."
    us "Where's your stuff?"
    show dv normal sport with dspr
    dv "Already there, your archrivals are guarding them."
    "Serenely explained Alisa."
    dv "I've already been on my suitcases all morning. I advise you to do the same."
    show dv grin sport with dspr
    dv "And don't you dare kiss here: the Hat goes around the patrol... and so on."
    hide dv
    with easeoutbottom
    pause(1)
    play sound sfx_close_door_1
    "Slamming the door, Alisa walked out of the cabin."
    "This time Ulyana wasn't even embarrassed or blushing anymore."
    "She managed in some unthinkable way to make sure that we weren't teased around camp by the 'tili-dough.'"
    "How did I figure it out?"
    "So much so that even the eternal ulcer Alisa left the last stiletto for last and didn't even stop to admire our embarrassed faces."
    "Knew there'd be nothing to admire."
    show us normal pioneer
    with move
    us "Here comes the departure."
    me "Departure. Does your request for help still stand?"
    me "Or do I go to change?"
    "Ulyana shook her head."
    us "It'll take you five seconds to change, but it'll take me a long time to fold neatly."
    me "We have an hour."
    show us surp1 pioneer with dspr
    us "Of course we do. But it would be hard for me to carry the bags to the gate myself."
    show us smile pioneer with dspr
    us "You're going to help the mamselle, aren't you?"
    "I nodded, and Ulyana turned into a whirlwind in tie and a skirt."
    "A dozen identical Union T-shirts, shorts, dresses of some kind flew toward me..."
    "They were all surprisingly undamaged, and I, recalling a half-forgotten skill in suitcase-picking, unzipped a large leather suitcase with a tug strap and began to pile the items I received into it."
    with fade2
    "There was a surprisingly large number of things, so that I was able to get the suitcase off the ground with great difficulty."
    "Ulyanka herself was flaunting another smaller bag, stenciled with an owl and the date '1987'."
    "There she hid the most important things: an iron, a downed volleyball."
    "And the bear, of course."
    us "And how'd you get that in there all by yourself?"
    show us smile pioneer with dspr
    us "A poor girl sometimes has to resort to the help of strangers."
    me "And who was that stranger?"
    "I looked at my watch. {w}It was another forty minutes before we left."
    show us smile pioneer with dspr
    us "Uncle Borya, of course. My guards just wouldn't lift that suitcase."
    "We went silent."
    me "Shall we sit for the road?"
    "Throwing off the bed with the bedclothes folded into a single pillowcase and the mattress roll, we sat down on the panelled netting, which sagged with a pitiful groan under our weight almost to the floor."
    "So we found ourselves involuntarily pressed against each other."
    us "Thick and heavy Syomich."
    us "Squeezed the bed!"
    me "I did."
    "I agreed."
    show us normal pioneer with dspr
    us "Either way..."
    "Ulyana began, and I continued:"
    me "That was the best shift ever!"
    "Laughter resiliently rose to the sloping vaults of the cabin."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day7_us_7dl_packing_mi:
    play music music_7dl["you_are_soul"] fadein 3
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg int_house_of_un_day with dissolve
    play ambience ambience_int_cabin_day fadein 3
    if not (loki and (alt_day2_date == 'un')):
        th "I've never been here before."
        "With withering surprise, I stated."
    show mi normal casual with dissolve
    "I was dragged all the way to the cabin, but left at the door with instructions to wait."
    "I was let in only a few minutes later, during which time the girl had time to change into the outfit I already knew."
    mi "Come in."
    play sound sfx_close_door_campus_1
    "Miku let me into the cabin and slammed the door behind my back."
    "It looked as if she had lured me into the cabin with some far-reaching purpose."
    "Although I didn't mind at all, part of me knew that someone like me would never shine with someone like Miku."
    "Cutting in its bitter frankness of understanding."
    me "Where do you grab what? Round carry, square roll?"
    "I rubbed my hands together, pretending with all my might to be enthusiastic."
    show mi smile casual with dspr
    mi "You don't have to do anything."
    "Miku looked at me with a {i} special{/i} look."
    mi "I just wanted us to spend some time together."
    me "Together..."
    mi "Will you sit with me? Because we're leaving soon, and..."
    "She cut herself off."
    th "Departure? {w}And I wish I had a little more time - a couple or three days at least!"
    "Again the same prayer to random."
    "Again I knew I wouldn't have enough of those days, no matter how many."
    me "I will, of course."
    "Miku burrowed into the closet, rattling something there and periodically pulling out various strange things in boxes of hieroglyphics."
    "She identified them in a stiff red-and-black satchel open on the table."
    th "I'm willing to sit for as long as it takes. If it's next to you."
    me "Where do you go next? After camp?"
    show mi serious casual with dspr
    mi "I don't know. I'm not sure."
    mi "But I remember your address."
    me "And I remember yours - house by the park on the subway side."
    "We fell silent, Miku - continued to gather."
    "And me - continuing to admire the figure flying around the room, the honed movements..."
    me "I don't know where or how after camp myself. It's like a void, and no one's waiting for me there."
    mi "Completely and utterly?"
    me "It's hard to say...{w} I'd like to believe that somebody needs me there."
    mi "But no matter how you spin it, it's not even fifty percent certainty."
    show mi surprise casual with dspr
    mi "I've been told about your parents being on a diplomatic mission."
    me "Who told you?"
    "I was involuntarily interested."
    show mi smile casual with dspr
    mi "Olga Dmitrievna told me! She said that you continued your studies somewhere in Havana, so communication through embassies would be difficult..."
    "Miku waved her tails nonchalantly."
    mi "But nothing! We'll get through!"
    me "We'll get through..."
    mi "And if we don't, there will always be your address in Leningrad."
    th "What a shame it will be if this house isn't even built yet?"
    me "The main thing is not to arrive at a closed, empty apartment."
    show mi happy casual with dspr
    mi "It's so great that you care! I thought we'd feel like strangers after we left, like we were real just here."
    th "And we are, it seems."
    "A wistful rush went through my head."
    th "I have a great experience of not recognizing my old friends on the street."
    me "We won't."
    "I assured."
    me "It's hard for me to promise anything, but this I'll try to keep."
    show mi normal casual with dspr
    mi "You can't promise."
    me "Why not?"
    mi "I don't know... It's like I have this premonition..."
    "She hesitated."
    show mi upset casual with dspr
    mi "It's like the Senechka who's sitting here - and the one who'll end up on the bus... They're different people."
    me "Am I going to grow a second head?"
    mi "My greatest fear is that you will lose the desire to communicate with me."
    "Miku whispered."
    me "Why should I?"
    th "Now that I know who and what you are, I will try with all my might not to let you go!"
    mi "I don't know. It just seems that way to me."
    show mi sad casual with dspr
    "Miku looked at me guiltily."
    mi "Baka, huh?"
    "I got out of bed and walked over to her."
    me "You betcha."
    "And again, habitually gentle and as if rightfully so, I took her in my arms."
    me "How could I not want to communicate with you?"
    "I whispered, burying my nose in the top of her head."
    me "When you seem so alluring, so unattainable, from the first day."
    me "And now I'm hugging you. And it's like dreaming in real life, I wouldn't trade it for anything."
    show mi serious casual with move
    mi "I don't have so much luck so that it'd happen, Senechka."
    "I turned my nose up at her, and I said pompously:"
    me "And we don't need luck."
    show mi smile casual with dspr
    mi "We have a chance?"
    "Almost unmistakably she finished the quote."
    "Although in that case it was talking about ammunition."
    me "Right. A chance is all we need."
    show mi normal casual with dspr
    "Miku freed herself easily from my grasp and took half a step back."
    "You could still see doubt and uncertainty in her eyes."
    "But she was determined to try not to break her arms."
    "And so all I had to do was support her."
    mi "Thank you."
    "She smiled."
    mi "For everything. Now run and pack your things, we're leaving very soon."
    me "What about you?"
    show mi smile casual with dspr
    mi "Don't worry, meet me there, I'll carry the bags myself."
    me "Are you sure? I can help?"
    mi "Senya... Go."
    show mi cry casual with dspr
    mi "Go already!"
    stop music fadeout 3
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg ext_house_of_un_day
    with dissolve
    play ambience ambience_camp_center_day fadein 6
    play music music_7dl["exodus"] fadein 3
    "She pushed me out of the cabin, not understanding anything, in the most upset feelings."
    me "And what was that?"
    "I turned to the red-hot sky."
    "Silence was the only answer."
    play sound sfx_knock_door7_polite
    "I tried knocking on the door, but no one answered."
    "With a sigh, I went to pack my things."
    play sound sfx_open_dooor_campus_2
    pause(1)
    scene bg int_house_of_mt_day
    show mt normal pioneer
    with dissolve
    "Olga was in the house; she was writing something in her beautiful diary again."
    "I could only guess at what kind of notes she might have kept."
    "Compromise? Characteristics on subordinates? A personal diary?"
    th "Either way, I'll never know."
    mt "What's with the face?"
    "Olga was all participation."
    me "Ate too many lemons."
    "I snapped."
    show mt smile pioneer with dspr
    mt "Aren't they Japanese?"
    me "How did you...{w} Oh, I see. It's a polychinelle secret, isn't it?"
    show mt normal pioneer with dspr
    mt "The whole camp already knows about you. {w}I get it, the blood's boiling and all, but hugging on the roof in the middle of camp!"
    me "Scold me then."
    if counter_mi_7dl == 2:
        me "Or send me to bed, like last time."
    "Grimly I suggested."
    mt "You'd be welcome. {w}It's me, your old and stupid squad leader, remember?"
    mt "I'm well aware that you will punish yourselves far more severely than any scolding."
    me "Not necessarily."
    show mt smile pioneer with dspr
    mt "Unavoidable. You can hold on now and brave it all you want, but we're leaving."
    mt "And the camp stays. That's the biggest tragedy of all."
    me "I don't see any tragedy."
    show mt sad pioneer with dspr
    mt "Is that so? In that case, tell me, Semyon."
    "She leaned back and stared at the bridge of my nose with her fingers interlocked on my knee."
    mt "How many successful relationships have you had since camp?"
    mt "Don't rush to answer that. I'm talking specifically about successful ones."
    "No answer. There's no way."
    mt "I'm not saying you're two losers and can't write to each other."
    mt "But I've seen too many promises like that."
    "She got up."
    mt "I'd hate to see another one like that as an empty shake of the air."
    mt "Think about it."
    hide mt with dissolve
    "She left me alone, silently shutting the door behind her."
    "And I ripped my tie with surprising anger, yanked the belt from my shorts."
    "For some reason it seemed that the official things had suddenly become alien and prickly."
    "Uncomfortable and completely out of shape."
    "As it turned out to be the whole time I was wearing them."
    stop music fadeout 3
    stop ambience fadeout 1
    return

label alt_day7_us_7dl_packing_un:
    play music music_7dl["deadman"] fadein 3
    scene bg ext_dining_hall_away_day with dissolve
    play ambience ambience_camp_center_day fadein 6
    show un shy pioneer with dissolve
    me "Ready to go for a walk?"
    show un serious pioneer with dspr
    "She nodded, and when I held out my palm to her, she grabbed at it with a strength not unexpected for such a girl."
    hide un with dissolve
    "And she led the way, almost dragged me along."
    "My head was swirling with ideas as to why Lena would want to take me anywhere."
    "Of course, the perpetual naughty man offered some rather curious possibilities, but, I'm afraid, on the second day after the actual beginning of the relationship... unscientific fiction."
    if alt_day2_date == 'un':
        dreamgirl "Renewed relationships."
        th "Were there any?"
        dreamgirl "Lena thinks there were. {w}You are her second chance, given to the world. Don't let them both down."
    else:
        "Why am I talking about day two, despite Lena's assurances about a year-long wait and a second chance for this world?"
        "Because I don't know any of that, and I can't know any of it."
    "To me, Lena is just a pure, naive girl who prioritizes her crush over wanting her chosen one to do well."
    "That's why the very idea that we could be doing something like this now - in the face of the coming Unknown - seemed blasphemous."
    dreamgirl "What's wrong with that? It's well known that in extreme cases the instincts are heightened."
    dreamgirl "The body senses death and tries to do its best to save itself... Or at least the genetic information."
    dreamgirl "Remember, like in that song: to the position of a girl... and from the position of a mother."
    th "Come on, shush!"
    "I shouted at the raging libido."
    "Especially since we seem to be getting there."
    scene bg ext_un_hideout_day_7dl
    with dissolve
    play ambience ambience_lake_shore_day fadein 3
    "We came out on a sandy beach that jutted far into the creek, seemingly a stone's throw from the island and the string of steel rails that stretched along the shore."
    "And it seemed, too, if you looked long and hard at the water bubbling over the granite wreckage, that we were leisurely casting off and heading somewhere far, far away."
    "The journey of a lifetime."
    if not (loki and (alt_day2_date == 'un')):
        me "Where did the place for the fire come from?"
        "The silence was getting quite heavy."
        show un normal pioneer with dspr
        un "I burn sometimes. It's a good place, no one can see it, no one will find it."
    me "You like places where no one can find you, I see."
    un "It's not the place... It's just a good memory here."
    me "What kind?"
    show un shy pioneer with dspr
    un "You k-kissed me here for the first time... {w}a year ago."
    me "Even so..."
    "I brooded, and Lena spoke, hurriedly, confused:"
    un "I remember it because I was with you. And as long as I'm with you, I don't care where."
    un "I don't care so much, as long as you are, that I'm ready to hate you."
    un "For some reason I think of you, but I see a blue whale floating between skyscrapers."
    un "A very strange association, but it is dear to me for some reason."
    me "Blue whale?"
    "I had a memory associated with that as well."
    "Lena nodded."
    show un serious pioneer with dspr
    un "The cold city, the damp wind, and the silence that appears on film."
    un "People are like particles in a Brownian motion, moving faintly, and therefore the cold is only more palpable."
    un "I'm being silly, aren't I?"
    "I shook my head."
    un "Nonsense."
    "She nodded affirmatively."
    un "It's just you... I don't even know how to say it."
    un "It's like a creative itch on my fingertips, and I should write you to soothe my racing heart - and I can't."
    un "As I sit down at my desk, I close my eyes - and there you are again."
    th "A kind of depression."
    "I remind myself."
    me "We might not have met at all."
    un "But we did meet. Now it's too late to be offended or pretend it never happened."
    me "I don't want to pretend."
    show un sad pioneer with dissolve
    un "And I want to stay for one more shift. It just takes one call."
    me "With me?"
    un "With you."
    un "It shouldn't be hard for you to renew, I know that."
    me "You'll have to drive into town for that. Plus a week for a shift change."
    th "Is that enough of a wait for you, girl?"
    "Came over suddenly with associations of those very whales."
    "Yes, and there was a familiar glint in Lena's green eyes."
    "Depression."
    "And a depressed person is as close as ever to the brink, which it is better not to cross."
    me "No, I don't want to stay in the camp."
    show un serious pioneer with dspr
    un "You don't want to..."
    me "You listen first."
    "I interrupted."
    me "It's a place for kids, recreation, that sort of thing, right?"
    "Lena nodded obediently."
    me "Lots of rules, restrictions, you can't date, you can't kiss. I don't even have anywhere to take you, if anything."
    un "Don't take me anywhere."
    "Lena protested."
    me "And if I want to? At least take me to see a movie together."
    show un shy pioneer with dspr
    un "T-that is... Y-you..."
    me "I want to carry on in the city. Normally, like white people do, without hiding in nooks and crannies."
    th "Maybe then you can come to your senses."
    "I couldn't say I was straight up in love with this girl, but I didn't care at all."
    "Besides, I'd heard that this tantrum could eventually wear off and take on the features of what she was pretending to be for the time being."
    "Real feelings that shouldn't be locked up under a mask."
    "And for that, I was willing to do a lot."
    "To grow into the local society without knowing how to do anything."
    "Becoming someone she could be proud of."
    "Even marrying her eventually - that didn't scare me at all now."
    stop music fadeout 5
    "Lena looked at her watch and owed:"
    show un sad pioneer with dspr
    un "Noon. We have to get ready in time."
    me "Is the bus coming?"
    "She nodded."
    un "And you have nothing to pack, I know. Would you like to come with me?"
    "Sure, I wanted to."
    stop ambience fadeout 6
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg int_house_of_un_day at zentercenter
    show mi normal casual at left
    with fade
    "When we entered the cabin, we found Lena's neighbor sitting right there."
    "Unlike the scattered things on Lena's side, Miku had already managed to pack everything, change her clothes, and even pack her suitcases."
    show un normal pioneer at zenterright with move
    un "Where are you going so early?"
    mi "Lenochka, haven't you heard? The departure was postponed because of the storm warning."
    un "Another one?"
    "Lena squinted at me incomprehensibly."
    show mi sad casual with dspr
    mi "Yes, there's some kind of front coming at us, so we decided to leave early."
    mi "If we leave in the afternoon, we're bound to get caught in it! This way we have some chance of getting through."
    th "Trouble never comes alone."
    un "And when do we leave?"
    "Miku looked at the clock woven into her kumuhimo."
    mi "In half an hour."
    show un shocked pioneer with dspr
    "Lena groaned."
    un "So what are we standing here for? We have to get ready right away!"
    mi "I'm all packed, I've been waiting for you."
    mi "If I hadn't waited, I would have started packing your things myself in ten minutes."
    mi "Even though it's wrong! But I wouldn't leave you alone in the camp."
    show un normal pioneer with dspr
    un "Thank you."
    "Seriously thanked Lena."
    "She pulled a huge bag from under the bed, where she placed a shelf removed straight from the table with the drawings lying drawn side down."
    "Moments later, there flew clothes from the closet, lingerie, and something else lacy that I couldn't find a definition for."
    th "And why would she have such a thing in camp?"
    show un shy pioneer with dspr
    "Then Lena noticed that I was still standing in the doorway, staring at her gathering, and she was embarrassed"
    show un normal pioneer with dspr
    extend ", but quickly regained her composure:"
    un "Are you still here? Go get your things now!"
    me "Sir, yes, sir!"
    un "I want to ride on the bus with you, mind you!"
    un "But that requires you to get on that bus!"
    un "So ziegel ziegel, march!"
    "Putting my hand to my empty head, I jumped out into the street."
    stop music fadeout 5
    play sound sfx_open_door_kick
    pause(1)
    scene bg int_house_of_mt_day
    with dissolve
    play ambience ambience_int_cabin_day fadein 5
    play music music_7dl["seven_summer_days"] fadein 3
    "There was no one else in the cabin."
    "Some of the leader's things were packed, but it was obvious that she was going to be back here soon."
    "Only the essentials were taken."
    "And on the table, pressed by a glass, was only a note that said in huge letters:"
    "PACK UP!"
    th "How they all take care of me."
    "I've got a lot of sympathy."
    me "I'm coming, I'm coming, you don't have to tell me twice."
    play sound sfx_open_cabinet_2
    pause(1)
    "The clothes were found in the closet, washed, ironed, and folded neatly."
    if dr and (counter_sl_7dl == 0):
        "There was no trace of the shame I'd felt before."
    "So I took off and hung my shirt and shorts and tied my tie on top."
    me "Hello, things."
    "The clothes were still falling off, and if they weren't so tight - I'd have to walk, supporting my pants as I went."
    "But in my pocket I found the player I'd been ignoring all this time."
    th "I should let Lena hear it."
    "It crossed my mind."
    "But time is of the essence."
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg ext_house_of_mt_day
    with dissolve
    play ambience ambience_camp_center_day fadein 6
    "Jumping into my boots and throwing my coat over my elbow in the manner of a waiter, I stepped outside and slammed the door behind me."
    th "As if for the last time."
    "It flashed in my mind."
    play sound sfx_lock_close
    th "Maybe it really is the last one."
    th "I'd better remember to give the key to the squad leader, or else..."
    scene bg ext_house_of_un_day
    with dissolve
    play sound sfx_knock_door6_closed
    "As expected, Lena's house was closed."
    "Neither she nor her roommate was there."
    me "And do you have to be so rambunctious and out of place?"
    "I sighed."
    "I guess it has to be."
    "I headed for the gate."
    stop music fadeout 3
    stop ambience fadeout 1
    return

label alt_day7_us_7dl_packing:
    scene bg ext_house_of_mt_day with dissolve
    play music music_7dl["thousand_little_things"] fadein 3
    play ambience ambience_camp_center_day fadein 3
    "And it's... summer."
    "We've been grumbling all year about how nice it would be if summer came."
    "Well, here it is. What are you going to do with it now?"
    "Waste it on trips to some country house or on the computer again?"
    "Or will you go outside and one day open your chest and breathe it in in all its glory?"
    "Remember it as it is, imprint it inside you."
    "And one day you will write to someone very close instead of a letter: and I remember the summer."
    th "Will I remember this summer?"
    th "Just for a week, but..."
    "An unsolicited reminder came back into my head that everyone around me was in pairs, threesomes... collectives."
    "Each of them will be remembered by at least one person."
    th "And who will remember me?"
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg int_house_of_mt_day
    with dissolve
    "And my head's been cracking this morning with a bad omen."
    "A clear hint that the voucher is about to expire permanently."
    "And then you'd better get off, the train's not going any farther."
    "That's why I usually rip it off in one fell swoop to keep the unpleasantness at bay."
    play sound sfx_open_cabinet_2
    pause(1)
    play sound sfx_blanket_off_stand
    "When I opened the closet, I pulled out a hanger and threw it on the bed."
    "Jeans, a T-shirt and sweater, and a pair of black socks were found on the top shelf."
    if loki:
        th "Mine."
        "I nodded."
        "There was a rough darning between my fingers and at my heels - absolutely my doing."
    else:
        "I recognized them by the trademark pair of holes in the heels."
        dreamgirl "Shame. And the squad leader used to take them in her hands, give them over to the laundry."
        th "So what? I don't take my shoes off in front of her."
        dreamgirl "What if you have to?"
        th "I'll just slide the holes down so nobody can see them."
        dreamgirl "You're a nightmarish neighbor."
    "After six days of incessant wear, the uniform was already frayed and crumpled in shape."
    "It certainly didn't smell like roses - I hadn't even bathed."
    "So it was reasonable to ask:"
    me "Shall I hang it on the hanger or give it to Slavya as a dirty lump?"
    if loki:
        me "At the very least, she'll take it off herself and throw it in the laundry basket."
        "I decided."
        "I tried to be careful with my clothes."
        "Not even mine, actually."
        "Or rather, especially not mine."
        "It was the shorts that caused the most trouble, but I ended up hanging them up too."
    else:
        "Deciding not to bother with such nonsense, I threw off my clothes, leaving me in just my boxers and wrapped everything in my shirt, throwing a red tie on top."
        "The cougar petal I was so used to, I didn't even notice it anymore."
    "The bedding had to be packed, too."
    "Remembering what it was like at the camp I went to all my life, I tucked everything into one pillowcase, folded a blanket and pillow over the bare mattress, and wrapped it all up in one big roll."
    me "That's it now?"
    with fade2
    "Dressed back in my familiar, but perceptibly oversized clothes, I walked over to the mirror."
    scene cg d1_me_dahell_7dl
    show mouth_dull
    with dissolve
    "All the unspoken words... The unlived seconds."
    me "Nothing's changed, has it?"
    "The reflection made disciplined faces at me."
    "I decided not to wear a sweater, tied my sleeves around my waist."
    if alt_day_binder == 1:
        "I left my coat, too - I can't lug it around the camp."
    if dr and (alt_day_binder != 1) and (counter_sl_7dl == 0):
        "I felt the lining: it had already had time to dry in that time."
    "I wasn't going to leave it at camp, because for some reason I was pretty sure I wasn't going to make it to the city for the rest of the summer."
    "I won't make it, I definitely won't make it."
    stop music fadeout 3
    play sound sfx_open_dooor_campus_2
    pause(1)
    scene bg ext_houses_day with dissolve
    play music music_7dl["the_way"] fadein 3
    "But I can pay off all my debts, for instance."
    "Or at least the biggest ones."
    scene bg ext_warehouse_day_7dl
    with dissolve
    "The warehouse door was wide open, and you could see the pioneers scurrying in and out."
    if loki:
        "Once again weighing the clothes rack in my hand and the laundry bale in the other, I headed inside."
    else:
        "After twisting the crumpled lump of dirty laundry and clothes around in my head with doubt, I decided it was too late to go back and went to turn in the castellan."
    scene bg int_warehouse_day_7dl
    with dissolve
    play ambience ambience_int_cabin_evening fadein 3
    "There was an uproar and a commotion inside, and I lost my melancholy mood for a split second as I watched in a daze as the kids rolled the sheets across the floor, threw a few dozen of her mates in, and tied the resulting bale with a big-eared knot on top."
    "They did it all coherently and busily, obviously not for the first or tenth time already."
    show sl normal pioneer with dspr
    sl "Hello."
    "Slavya nodded as she approached."
    sl "Are you here to drop off your things?"
    me "I have to do something while waiting for the bus."
    show sl smile pioneer with dspr
    sl "You could help out around the warehouse if you don't have anything else to do."
    me "Thanks, I'll refrain!"
    show sl laugh pioneer with dspr
    sl "You're lazy, Semushka, as it is, you're lazy."
    me "Not lazy. I'm here on vacation, pioneering! All in that spirit."
    th "I'm also surprised I haven't been run through the lists and kicked out."
    "Instead, they retroactively set me up a legend and completely legalized me here."
    "Only why..."
    "I didn't have to go on any top-secret mission here."
    "Neither did seducing fatal beauties or firing a Walther PPK at point-blank range."
    "So I wasn't James Bond either."
    show sl normal pioneer with dspr
    sl "I'm a pioneer, too. But that doesn't stop me from taking care of my house."
    me "Yeah, yeah... Maybe you just have too much free time."
    sl "You have less of it?"
    me "Yes, I'm always busy doing something!"
    show sl smile2 pioneer with dspr
    sl "That's what I thought for some reason."
    sl "So will you help me?"
    mt "He won't help you, and you go ahead and wrap it up here."
    show sl surprise pioneer at left with move
    show mt normal pioneer at zenterright with dspr
    "The squad leader dazed me."
    me "I might have agreed."
    "The decorum of good manners should have been respected, though I was glad of the unintentional rescue."
    show mt smile pioneer with dspr
    mt "You wouldn't make it in time. There's a storm warning for the area, and we're expecting it to happen by nightfall, so it's been decided to move out a little early."
    show sl normal pioneer with dspr
    sl "How early?"
    mt "Noon. In fact, the buses have already arrived, so you have twenty minutes to pack, then I'll wait for you on the bus stop."
    mt "You're already changed, good, I won't have to wait for you."
    if alt_day_binder == 1:
        mt "Don't forget your coat."
    hide mt with moveoutleft
    "The squad leader nodded to us and slipped past Slavya into the door."
    sl "Well, well..."
    "The blonde babbled confusedly."
    sl "I'm sure I won't make it!"
    me "Hurry up! Schneller, schneller!"
    hide sl with dissolve
    "With an obedient nod, Slavya also evaporated."
    "And I got a new companion."
    show ba normal uniform with dissolve
    ba "They don't do anything right, do they, skinny boy?"
    me "I have a name."
    show ba smile uniform with dspr
    ba "What about the name? Mommy and Daddy gave you a name, but what you become doesn't depend on the name."
    ba "If you're a wimp, you should be called a wimp."
    if loki:
        me "Ah. Got it. So, should I call you Fatty the Viper?"
        show ba em1 uniform with dspr
        ba "Why are you like this."
        "He sighed contritely."
        play sound sfx_face_slap
        with flash_red
        with vpunch
        "I didn't have time to think or react before I got a palm on the back of my head."
        "Slap."
        "It was a slight, one-tenth of his power, but I bit my tongue and my ears rang."
        ba "You're a cheeky man."
        "Respectfully sauntered the gym teacher."
        ba "With character. That's praiseworthy."
        me "What the hell are you doing with your hands?!"
        ba "You don't know who to show your temper to, so you're reprimanded."
        ba "With a censure to your chest."
        "He clenched his big fist, and I involuntarily took a step back."
        show ba smile uniform with dspr
        ba "Don't worry, we don't punish you twice for one thing. You run along and get what you need, and I'll take a look here."
    elif herc:
        me "A wimp? I actually se..."
        dreamgirl "This really isn't a good time."
        "Just in time my inner voice stopped me."
        show ba normal uniform with dspr
        me "I think I'm in good physical shape for my age."
        ba "Yeah? How long ago have you checked? How fast you run the distance?"
        me "Twelve and five."
        "The gym teacher looked at me skeptically."
        ba "Not bad. But you shouldn't forget about your muscle corset either."
        ba "All right, run along, athlete. I'll make sure it's all right here."
    else:
        me "Don't you realize that this is at least unpleasant?"
        show ba em1 uniform with dspr
        ba "The truth is unpleasant? Welcome to real life, son."
        ba "Do understand, I'm not hurting you here for my own pleasure."
        me "It's for the greater good, yeah."
        ba "That's right!"
        "He's pleased."
        ba "I'm glad you understand."
        ba "If I can get you through this, you might want to pay attention to your form."
        ba "You have to get your body in shape when you're a kid, but you're not out of the woods yet."
        me "I don't give a damn about the culture."
        ba "Spit on it all you want. Only when your body responds with the same spit in the form of a sore back and arms, remember Uncle Borya, the stupid and fat gym teacher."
        show ba normal uniform
        with fade
        ba "Now go. I'll make sure it's all right here myself."
    me "Aren't you coming with us?"
    ba "If you can give me one good reason why we need a PE teacher in the cavalcade."
    me "Uh... Security."
    show ba smile uniform with dspr
    ba "From flying waffles, maybe."
    ba "Go, wimp. Good luck."
    "Nodding goodbye, I left my unsigned official belongings and went outside."
    "According to Olga, I have very little time."
    "I should have hurried."
    stop music fadeout 3
    stop ambience fadeout 1
    return

label alt_day7_us_7dl_leaving:
    scene bg ext_camp_entrance_day with dissolve
    play ambience ambience_camp_entrance_day_people fadein 3
    play music music_7dl["so_cold"] fadein 3
    if alt_day6_us_7dl_help:
        "By the time Ulyana and I brought her huge suitcase in, it appeared that everyone around was already assembled."
        "It seemed like they were only waiting for us."
        play sound sfx_bus_honk
        "Everyone immediately murmured, waving their hands, beckoning, and Aliska, running into the cabin, slammed on the steering wheel, producing a long, lingering beep from the horn."
        "Whale song."
        "Olga immediately barked something at her, but Alisa brushed it off and pushed her way toward us:"
        show dv grin sport at left
        show us normal sport at right
        with dissolve
        dv "So, have you had enough time for kissing?"
        "On her shoulder was a black gym bag with an orange zipper badge, somehow vaguely familiar."
        me "Nah, remember - Hat's a sentinel..."
        show us smile sport with dspr
        us "But we held hands!"
        show dv smile sport with dspr
        dv "Our archer is everywhere in time."
        "Alisa looked at me respectfully."
        dv "And got you ready, and dressed himself, and held hands."
        us "Yes! He's not such a retard."
        me "Hey!" with vpunch
        me "I heard that!"
        show us laugh sport
        show dv laugh sport
        with dspr
        "The friends looked at each other and laughed in unison."
        me "Do you hear that?"
        "The twin voice of the one that greeted us at the bus stop came from somewhere far away."
        "There, our good nurse's Volga was climbing up the road to the first hill, and behind her the red-skinned child of the Hungarian car industry was strolling leisurely."
        me "The first children were taken."
        show dv normal sport with dspr
        dv "These are the littlest ones, the fifth through sixth squads."
        show us smile sport with dspr
        us "So we'll be taken soon, too!"
        me "Departing... I'm in such a good-natured, lazy, calm mood now."
        me "I can't even swear and be offended by your ginger couple. It doesn't work."
        show dv grin sport with dspr
        dv "What a loss!"
        "Dvachevskaya snorted."
        me "You two are so beautiful, so interesting... You have become too much for me, and too quickly."
        me "Though Ulyanka, of course, is a little more; Alisa, don't be jealous."
        dreamgirl "A threeesooome? Threeesoooomeeee?"
        "Waving it off, I headed for the bus."
        show us shy sport
        show dv shy sport
        with dissolve
        "The girls' faces stretched, they both got a little embarrassed and blushed."
        "So when I got on the bus - I felt completely avenged!"
        "Even my suitcase-stomped limbs stopped bothering me."
    elif alt_day6_us_7dl_mi_friends == 3:
        "I tried to put the gloomy prophecies of the squad leader out of my head."
        "I wanted to believe that the world wasn't black, and that even I could find a place in it."
        "And the tiniest bit of luck."
        me "I'm taking a lot more out of camp than I brought in."
        "I whispered thoughtfully."
        show us grin sport with dissolve
        us "Did you steal the towels?"
        me "What? No, I'm talking about... Ugh!"
        "Ulyana stood across from me and looked at me mockingly."
        us "Syomich, why do all the seniors always choose only problems between interest and problems?"
        me "What do you mean?"
        if counter_us_7dl_px >= 1:
            us "I'm about your abandoned searches."
            us "You should have known what we found! {w}Only I won't tell you anymore."
            show us grin sport with dspr
            "She took a step back and gave me a mocking look."
            us "You're interested in older boys' toys now."
            me "What are you talking about?"
            show us smile sport with dspr
            us "Mikuska. Pretty, funny, and goofy. A boy's toy."
            us "Just don't throw this one away when you get tired of it, okay? She's human, after all."
            show us grin sport with dspr
            hide us with dissolve
            "She winked at me and disappeared in the bus."
        else:
            show us smile sport with dspr
            us "You're big, aren't you? Big."
            me "So?"
            us "You should have asked to stay! There, as an assistant watchman of some sort."
            me "And why would they keep me?"
            show us laugh sport with dspr
            us "They're keeping Zhenka. See, she's not coming with us."
            me "Suppose I'm allowed to stay, but what about Miku?"
            show us laugh2 sport with dspr
            us "Let her ask for it too!"
            me "That won't work. Besides, she's a citizen of another country."
            show us grin sport with dspr
            us "Citizen, citizen! See, I'm right!"
            me "No."
            us "Right-right-right! You could have chosen interest, but you choose trouble."
            us "You're a nerd, Syomich."
            hide us with dissolve
            "She shook her head and went into the bus."
        with fade2
        show mi smile casual with dspr
        "And a few minutes later, Miku joined me."
        "She was carrying a suitcase in her left hand, and behind her moved a testament to the era, a cart bag painted with some anime characters with a long handle."
        mi "There you are..."
        me "Why did you send me away? We would have made it all in time."
        show mi shy casual with dspr
        mi "Just... Don't ask me, okay?"
        mi "I'm so used to being alone all the time, now I just run over there."
        mi "I talk fast, but sometimes it's hard to think, especially when I have to think about something as important and complicated as us."
        me "What's there to think about? You have to do it."
        show mi happy casual with dspr
        mi "At least one of us is confident about the future."
        "And I wasn't. I was trying to be brave."
        "Silenced the voice of foreboding, ordered myself not to be nervous, and tried my best not to hurt my lips against the clingy mask of the dim-witted fool who thinks 'everything will work out.'"
        "We're all going to die sooner or later, so what's the point of lying on our side and crying?"
        "We have to live. Live."
        me "Can I ask you something?"
        mi "Sure. What about?"
        me "Don't be surprised, but I want to take a picture of you."
        show mi surprise casual with dspr
        if counter_mi_7dl == 2:
            mi "Oh, that weird machine of yours?"
            me "Yeah, get in the frame!"
        else:
            mi "I didn't see your camera!"
            me "I have one. That's it, make it quick, the battery is almost dead."
        "The last percentage of charge was blinking red in the screen solution."
        th "Just as long as it's enough."
        "I prayed to Random and pointed the viewfinder at the girl."
        show frame at truecenter:
            xalign 0.5 yalign 0.5 zoom 1.0
            linear 0.8 zoom 1.0 xalign 0.5 yalign 0.20
        show cam_ui at truecenter:
            xalign 0.5 yalign 0.5 zoom 1.0
            linear 0.8 zoom 1.0 xalign 0.5 yalign 0.30
        me "Here comes the birdie…"
        pause(1)
        play sound sfx_7dl["snap"] fadein 0
        scene white with flash
        pause(1)
        scene bg ext_camp_entrance_day
        show mi smile casual
        with dissolve
        "The phone buzzed and went off."
        "I didn't even get a chance to see if the picture was still there."
        mi "Let me see, huh? How did I turn out?"
        me "I'm afraid that's impossible."
        "I showed the girl a completely discharged machine."
        me "Until it's charged... You know."
        mi "Eh... Let's get on the bus then."
        "The first buses had already started to leave the parking lot, so we all got on the bus, too."
    elif alt_day6_us_7dl_un_friends == 3:
        "Lena, of all people, was already there."
        "In 'civvies' - yeah, right, what pioneer in his right mind would want to carry a uniform beyond what's necessary."
        "I glanced at Slavya."
        "Even our activist, good and in every way correct girl preferred dress to the uniform."
        show un smile dress with dissolve
        "When Lena saw me, she immediately threw her bag into the open luggage compartment and rushed toward me."
        me "I have a favor to ask of you."
        un "What is it?"
        me "I'm afraid that one day I won't be able to believe myself, so..."
        show un normal dress with dspr
        un "What do you need to believe?"
        me "Stand at the gate and freeze."
        "I checked the charge - exactly one percent."
        "Lena frowned, but obediently complied."
        show frame at truecenter:
            xalign 0.5 yalign 0.5 zoom 1.0
            linear 0.8 zoom 1.0 xalign 0.5 yalign 0.20
        show cam_ui at truecenter:
            xalign 0.5 yalign 0.5 zoom 1.0
            linear 0.8 zoom 1.0 xalign 0.5 yalign 0.30
        me "Don't stand there with a sour face."
        show un smile dress with dspr
        pause(1)
        play sound sfx_7dl["snap"] fadein 0
        scene white with flash
        pause(1)
        scene bg ext_camp_entrance_day
        show un normal dress
        with dissolve
        "The phone buzzed and went off."
        "I didn't even have time to see if the picture was still there."
        un "That's it?"
        "One would hope..."
        un "Did you really come in winter clothes?"
        me "Obviously."
        un "How did you get here?"
        th "You ask strange questions, girl, oh, strange questions."
        if loki:
            me "If you've really known me for more than a year..."
            show un serious dress with dspr
            un "The truth. Never doubt it."
            me "Then it's time you got used to my weirdness!"
            show un smile2 dress with dspr
            me "Who knows! Maybe next time I'll come straight in a balloon!"
            me "I'll smile fiercely, twist my mustache in a Hussar-like way, and urge people to escape the captivity of their habits."
            un "Not your words?"
            me "Why it's not mine."
            "That was mean."
            me "They're very much mine! And very much about me!"
            me "I got you out of captivity, didn't I?"
            show un laugh dress with dspr
            un "Thank you, oh savior!"
            me "That's right! Remember that and never forget it!"
            me "Now let's go. Our Jacob's Ladder awaits us."
        else:
            me "Somehow it just happened, it wasn't me!"
            show un surprise dress with dspr
            un "Not you?"
            me "Honest pioneer word! I had nothing to do with it!"
            show un laugh dress with dspr
            un "And who 'had something to do' with it? Olga Dmitrievna?"
            "I threw a long, appraising look at the squad leader."
            me "You know, she might as well have been!"
            me "I always suspected something strange about her."
            un "You mean she changed you into winter clothes on the bus while you were sleeping?"
            th "Yes. And the cops planted the coke on me."
            me "She also put various gadgets in my pocket."
            show un smile3 dress with dspr
            un "Gad... what?"
            me "Come on, I'll show you on the bus!"
            "I grabbed her by the arm and, ignoring the startled oohing, dragged her after me into the cabin."
    else:
        "Feeling like an intruder at someone else's wedding, I went out the gate."
        "And there the whole troop had already gathered. All of them."
        "Even Slavya, who had run away not long ago, was flaunting a dress and an imposing suitcase."
        "I'm the only handsome one: in winter boots, thick jeans{nw}"
        if alt_day_binder == 1:
            extend " and a coat hanged on my arm."
        else:
            extend "…"
        show us laugh sport with dspr
        us "Oh, our retard is here! That's it, we can leave!"
        me "Thank you, glad to see you too."
        show us laugh2 sport with dspr
        us "Really glad?"
        me "Yes. I can't wait to never see you again."
        show us grin sport with dspr
        us "That's an easy fix!"
        "Ulyana folded her fingers into a 'goat' and poked it in my direction."
        me "I prefer the more natural way."
        show us smile sport with dspr
        us "Bo-ring!"
        "Ulyana looked away, and I called out to her."
        me "Hey."
        show us normal sport with dspr
        us "What do you want?"
        me "How can I tell you..."
        us "What?"
        "I hesitated. For some reason it seemed terribly wrong for me not to say a few words now."
        "It just wouldn't come out of my throat."
        "It's like they're stuck there."
        us "Is there something you want to say? Or should I go?"
        me "..."
        us "Well, I'm going."
        hide us with dissolve
        "Ulyana headed for the bus, and I found it very easy to talk to her back:"
        me "I... I'm going to miss you. Honestly."
        show us normal sport with dspr
        "Ulyana turned to me and nodded gravely:"
        us "I believe you will. And that's very good."
        us "So it's okay, and you're not thick-skinned and stale, like Alisa says."
        hide us with dissolve
        "She winked at me and jumped on the bus."
    play music music_7dl["tilltheend"] fadein 3
    scene bg int_bus
    with dissolve
    "Hot in the sun, the womb of the bus welcomed us and spread us out according to the chain of command."
    "Those who had made friends sat next to each other."
    "Those who didn't... Well, it was a big bus, and there were less than a dozen of us."
    "There was plenty of room for everyone, including the counselor and the drypacks, who took the second two seats right behind the faculty."
    show mt normal pioneer with dissolve
    mt "Are you all seated?"
    "Olga walked down the rows, noting who was sitting where, counting us by our heads."
    "She lingered beside me for a moment, apparently about to say something."
    if alt_day6_us_7dl_help or (alt_day6_us_7dl_mi_friends == 3) or (alt_day6_us_7dl_un_friends == 3):
        "But when she saw my neighbor, she sighed and gave up on her idea."
    else:
        mt "Semyon?"
        me "Yes, comrade squad leader!"
        "Cheerfully I put my hand to my empty head."
        mt "Do you want to sit with me?"
        me "No, I'm generally fine here."
        "I was going to plug my ears with earplugs and spend the rest of the time I had left before throwing myself into the unknown just for myself and the music."
        "The leader didn't fit into this picture in any way."
        show mt sad pioneer with dspr
        mt "Is that so..."
        mt "Well."
        "She nodded to some thoughts of her own and backed away from me."
    hide mt with dissolve
    if alt_day6_us_7dl_help:
        "Alisa wanted to invite Ulyanka to sit with her, even retrieved a deck of cards from nowhere, but when she saw that the red-haired traitor preferred my company to hers, she shrank back."
        "Put the deck back."
        "And for a moment I felt a prick of conscience, as if I were some kind of divorcer, breaking up a couple."
        "But then I got distracted, and Ulyanka tugged at my sleeve."
        show us smile sport with dspr
        us "Syomich, when's your birthday?"
        me "Not happening in a while. What do you need it for?"
        "I thought that Ulyanka was so attached to me that she was even ready to think of some birthday present."
        "But she immediately ruthlessly shattered all illusions:"
        show us surp1 sport with dspr
        us "So that's it! If you're not old enough, maybe you'll come here in the winter too!"
        me "And you?"
        us "I will! I always come here now!"
        show us shy sport with dspr
        us "You will come, won't you? Please!"
        me "I can't promise."
        "Her directness was both endearing and confusing."
        "The other thing was more important."
        "It suddenly dawned on me that I didn't want to hurt this girl in word or deed."
        "If it's within my power to do anything..."
        me "But I will absolutely try."
        us "You promise? You promised!"
    elif alt_day6_us_7dl_mi_friends == 3:
        show mi smile casual with dissolve
        mi "Senya, do you want to go to the window?"
        me "No."
        "For some reason it was very lazy to get up, to change places."
        mi "You're sitting against the light, so I can see you better!"
        show mi happy casual with dissolve
        mi "Why would you want to see me better?"
        me "So that I can eat you!" with vpunch
        "I barked."
        "And attacked laughing Miku with tickles."
    elif alt_day6_us_7dl_un_friends == 3:
        show un smile dress with dissolve
        "Lena took my hand on the bus and wouldn't let me go."
        "Even when we got to the seats that looked good to her, and settled there."
        "And it was me at the window."
        "Of course, Lena sat next to me."
        un "Your hands are so cold. Why?"
        th "What can I tell you about IBS..."
        "I wondered. And I showed my tongue."
        me "Dead, so that's why I'm cold."
        show un laugh dress with dspr
        un "Semyon, Semyon…"
        show un smile dress with dspr
        "She put her head on my shoulder and rubbed her cheek with undisguised tenderness."
        un "We could have known each other for a year by now."
        un "We could have been together for a year by now."
        me "We'd have had enough of each other and we'd have strangled each other."
        show un smile3 dress with dspr
        un "Don't even dream of it."
    else:
        "I took a place on the margins - neither at the beginning nor at the end."
        "To be away from everybody."
        "The only neighbors I had were Lena and Miku, chattering away, clearly on their own."
        "I guess they didn't talk enough at camp."
        "I was about to plug my ears with my headphones, but then Olga stood in the aisle."
    scene
    $ renpy.show("bg int_bus", what = Dawn("bg int_bus"))
    show mt normal pioneer
    with dissolve
    mt "Well? Ready?"
    "And we bellowed in tune:"
    voices "Let's go!"
    "The bus hurled itself into the red-hot day."
    stop ambience fadeout 3
    scene bg int_bus_people_day with fade
    play sound_loop sfx_bus_interior_moving fadein 2
    "I was tormented by an inescapable déjà vu, as if I had been here more than once or even ten times."
    "But the sun warms my side, and the pioneers beside me are so carefree..."
    "We rolled leisurely through the shattered secondary, and next to me kept laughing, quarreling, making peace - living - people."
    "Camp on wheels, and spit on those who say camp is a place."
    "Camp, like home, is people."
    "My «Sovyonok» consists of Alisa, Slavya and Olga Dmitrievna."
    if alt_day6_us_7dl_help:
        "Lena and Miku."
        "And, of course, a smiling Ulyanka at my side."
        scene cg d7_us_epilogue_bus_7dl
        with dissolve
        "I caught her palm and squeezed it."
        stop music fadeout 5
        "To the surprised look I answered with a smile and somehow naturally reported:"
        me "I'm happy with you."
    elif alt_day6_us_7dl_mi_friends == 3:
        "The mischievous Ulyanka, the ever-frowny and sad Lena."
        "And, of course, the chatty and so charming Japanese beauty."
        mr "I wish I were dead - so happy I am now."
        scene cg d7_mi_epilogue_bus_7dl
        with dissolve
        stop music fadeout 5
        "Miku came at me with a scolding, but I wasn't listening anymore."
        "I covered my eyes and absorbed with all my pores the feeling I'd always wanted, but never deserved."
    elif alt_day6_us_7dl_un_friends == 3:
        "A jet-setting child and one chattering giggler."
        "And, of course, a sweetheart at my side."
        "I only realized and accepted it now."
        scene cg d7_un_epilogue_bus_7dl
        with dissolve
        stop music fadeout 5
        "Just as naturally and calmly as I would one day suggest she take my last name."
        "Wasn't worried at all for some reason."
    else:
        stop music fadeout 5
        "And all the others, even if I can't remember their names now."
    play music music_7dl["uneven_me"] fadein 3
    scene bg int_bus_black
    with fade2
    $ night_time()
    "All around, the pioneers homed on, not paying attention to anything - not the approaching night, or the strangeness with the world outside the bus."
    "I was the only one who didn't feel right."
    "Everything seemed fine and normal."
    "Only one person, as usual, was uncomfortable with something."
    "Only the day outside the windows faded and faded, involuntarily taking my perception to my usual vision through the loopholes of my eyes, through a dirty light filter."
    "A ten-millionth sense that like a gut tells you unmistakably if you're near a place where you belong."
    "Home."
    scene bg int_bus_black
    with dissolve
    dreamgirl "There it is."
    "An inner voice sounded in my head."
    "It sounded kind of brooding and self-conscious now."
    th "What?"
    dreamgirl "The point of no return. {w}This is where we say goodbye to you, Semchik."
    th "Are you going somewhere?"
    dreamgirl "More like you. {w}It's been a wonderful week, too bad you picked the wrong things and the wrong people."
    if karma >= 50:
        dreamgirl "But you lived it according to your conscience, for which I thank you."
    else:
        dreamgirl "Though you've done some things you're hardly proud of."
        dreamgirl "But you lived your life the way you knew how, and for that, thank you especially."
    th "But I don't want to!"
    dreamgirl "Nobody wants to. But there are rules you can't break, even if you really want to."
    dreamgirl "Promise me to remember everything that happened to you properly, okay?"
    "I obediently nodded, watching as the bus found itself inside a void with no sound or light..."
    stop sound_loop fadeout 6
    scene bg int_bus_night
    with fade2
    "All that was left last was the beating of my heart and the fading echoing hum of the bus engine."
    if persistent.alt_binder:
        menu:
            "I didn't know what would happen next":
                pass
            "My story ends here":
                $ alt_day7_us_7dl_story_end = True
                stop music fadeout 3
                stop ambience fadeout 1
                return
    if alt_day6_us_7dl_help:
        "And we were left alone in silence."
        show us sad sport with dissolve
        "Ulyana was sitting next to me, looking at me with unspeakable anxiety."
        "As if she guessed what was about to happen."
        "And I put my arm around her shoulders, ignoring her astonished look, and pressed her to me."
        th "I won't let go! You hear me, you! No way!"
        "And she didn't pull away for some reason, just looked stern and a little mocking."
        "It was as if I were the child in our couple."
        "Me."
        "And not that little gunman in shorts and a T-shirt."
        "Amazingly handsome and never letting you forget for a second that she's a girl."
        "A girl, yes."
        "Girls are to be loved and carried in your arms, not dragged along in exploration."
        me "I feel bad for some reason."
        "I confessed."
        us "Are you afraid of something?"
        scene cg d7_us_epilogue_bus_7dl
        with dissolve
        "Ulyana moved even closer to me and laid her head on my shoulder."
        "So naturally and trustingly that I gasped for a moment in overwhelming tenderness."
        "And to whom?"
        me "I'm afraid to wake up where there's no you."
        th "I'm afraid of waking up where you were never there."
        th "Because then there would be no point in our friendship, nor in what it is about to become."
        me "Where there is nothing at all but a half-forgotten apartment on the seventh floor and a monitor screen."
        "I didn't want to explain anything, because there was no need to now."
        me "And on that monitor is you. The first rendition on request."
        "Ulyana smiled."
        "She wasn't bothered by all this nonsense, she was around someone she trusted."
        "And everything else..."
        "Vanity."
        "Suddenly, I was dying to kiss her."
        if loki:
            "Not like the cabin, where I basically just stole a kiss."
            "I wished it had happened differently."
        elif herc:
            "Not like then, in jest, but sincerely."
        "But outside the windows you can only see the emptiness that has swallowed almost everything and has now taken over the bus."
        "It's just the two of us on the seat."
        "And a desperate unwillingness to lay down and give up."
        stop music fadeout 5
        me "Two from the bus."
        "I mumbled."
        scene
        $ renpy.show("bg int_bus_night", what = Desat("bg int_bus_night"))
        show us normal sport
        with dissolve
        play music music_7dl["timetowakeup"] fadein 3
        me "Just you and me."
        us "Two?"
        "Ulyana asked again."
        me "Yes. And no one else around."
        "The bus engine finally died down."
        "The world narrowed to eye contact."
        "Outside the tunnel vision there was already a void, and somehow I knew that nothing good would come of meeting that void."
        "The simplest laws of physics; cold draws out heat and emptiness draws in matter."
        dreamgirl "You have a few seconds."
        "Suddenly sounded in my head."
        th "What?"
        dreamgirl "Wave your hand, show her you care."
        me "But…"
        show us normal sport tr1 with dissolve
        "Ulyana looked at me calmly and a little tired."
        us "Syomich, don't you dare."
        dreamgirl "Ulyana will stay where she belongs."
        dreamgirl "In the place where she belongs."
        us "Don't you dare, you hear!"
        with hpunch
        "She slapped me, but I felt almost nothing."
        dreamgirl "All you can take away from here is memory."
        dreamgirl "So remember her. As hard as you can!"
        me "I don't want toooooo!"
        "I shrieked, watching the silhouette of my best friend grow translucent."
        "A confidant."
        "Beloved."
        play sound sfx_face_slap
        show us normal sport tr2 with dissolve
        "I wanted to scream, but I could barely get my lips apart."
        "Ulyana clutched at my shirt and shook it as hard as she could, screaming in my face, spitting spittle."
        "And I sat there as if in a stupor, only shaking my head involuntarily in time with the jerks."
        us "Fight it, Syomich! We need you!"
        "The feeling you'd give your left arm for a chance to sleep."
        "Just to sleep."
        th "And dream, maybe. That's the difficulty... What kind of dreams would one have in a deathly sleep?"
        "Ulyana kept shaking and yanking me, not allowing me to drift off and simply turn off."
        "Now that she was a translucent shadow, a ghost of an idea and a belief that would ever get better."
        "Like a girl from a dream."
        "It only cost me the rest of my strength, a simple question:"
        me "You?"
        "It was just the two of us on the bus. Or rather, there was nothing left of the bus."
        "And all around us was an unknown something, the only escape from which all our lives have been waking up in a sweat."
        us "We're all here! Syomich, all of us. Look, you may just not see us, but we're here."
        us "We're all around you. Come on, help me!"
        "She cried."
        us "Please!"
        us "Help me, I can't do it without you, I can't!"
        dreamgirl "Goodbye."
        us "I won't let go. You hear me, don't you dare."
        play sound sfx_face_slap
        "She gave me another slap and leaned over and dug her lips into mine."
        us "Come on. Open your eyes!"
        play sound sfx_face_slap
        "Another slap."
        play sound sfx_face_slap
        "Another."
        dreamgirl "Summer came to an end."
        us "It's time... time to wake up, Syomich!"
        if (persistent.us_7dl_tran_un or persistent.us_7dl_tran_mi) and persistent.us_7dl_px_good and (counter_us_7dl_px >= 1):
            "The blows were sticking into me."
            "It was as if I myself had become a void, no longer able to see or perceive my surroundings."
            "And it made me afraid."
            "No, it didn't make me feel anything."
            stop ambience fadeout 3
            stop music fadeout 3
            scene anim prolog_2
            with dissolve
            "That's when I got scared."
            play music music_7dl["abyss_call"] fadein 3
            $ prolog_time()
            "There was no wind here, but the icy breath of the abyss could be felt with every inch of my skin, with every ruffled hair on my neck."
            "And the blows kept hammering and hammering me into nothingness."
            "And I..."
            "Let them through me."
            "Someone shouted somewhere, something rumbled somewhere."
            "But a moment later, I wasn't sure I'd heard anything."
            "Because following the blows into nothingness flew... me?"
            "Who's that?"
            scene anim_underwater
            with dissolve
            "Is it a red spark flickering in the darkness?"
            "Or maybe I imagined it all?"
            "I was the only one here."
            "Even that's not certain."
            "You can't be sure of anything."
            "Even the air here is only the air I have in my lungs."
            "Fortunately, it won't run out."
            "Because time isn't here either."
            "In this darkness anyone can wait as long as they want, without spoiling or growing old."
            "There... Can you feel it?"
            "An icy paw on my back, sharp claws on my skin, easily tearing into the epithelium."
            "Only it's not bleeding."
            "And it doesn't hurt."
            "The nerve signal has to reach the brain to trigger the experience."
            "But it takes time for that to happen."
            "Which isn't here."
            "There's only one observer."
            "Is that You?"
            "Or is that Me?"
            "And who is «you»?"
            "I think, therefore I am?"
            "Wait, who even is this «me»?"
            "And does this «me» think?"
            "Nonsense, it doesn't happen that way."
            "It's only bad."
            "The hair on the back of my neck still remains ruffled."
            "Goosebumps gathered to march down my body, stuck somewhere in my shoulders, on a frozen wave of warm blood."
            "It was the strangest thing around."
            "The strangest thing."
            "It was visible, tangible, understandable."
            "Although the termin «was» did not work here."
            "You're here forever."
            "I'm here forever."
            "The longing multiplied by eternity made me shudder."
            "Because the pain of the soul is illusory."
            "It is like imagination, like fantasy, with infinite speed."
            "And takes no time to hit the brain properly."
            "It makes me want to bark: Give me back my time!"
            "Give me back my pain."
            "But there's no one here to bark."
            "No one to complain, either, it seems."
            "There's nothing here."
            "That's why nothing works."
            "A single fraction of a moment stretches as viscous as a drop of tar that immediately becomes amber."
            "The most beautiful exhibit in the local museum without visitors."
            "And somewhere close by beats in the shadows of emptiness another bright life."
            "You can't see it because your eyes don't work here."
            "It cannot be heard for the same reason."
            "And yet it can be felt in some incredible way."
            "Apparently, all the same roguish instincts manage to catch it beating, fiercely, desperately."
            "How once there was a pulsating lump called «Me»."
            "Fading with every non-moment."
            "Pity."
            "It would be so nice to socialize, to share time with each other."
            "Maybe even go somewhere less boring."
            "So great..."
            "Fear appeared again."
            "Fear became Me, and something happened in this world."
            scene anim_digi
            with fade
            play ambience ambience_7dl["underwater"] fadein 3
            "I opened my eyes."
            "Into the void."
            "I remembered that 'I' is the most important thing there is."
            "That it is only on 'me' that I will be."
            "That only I see, I hear, I understand, I feel, and I love."
            "It was a confrontation with nothingness."
            "Foolish, doomed in advance to failure, like trying to fight death, but 'me' couldn't stop anymore."
            me "There is no boredom, there is a fight, an invisible fight."
            "Not for life, but for existence."
            "I began to speak incomprehensible, silly words with my empty tongue."
            me "The thirst for blood should quench it, but it does not..."
            "The strangest fight of my life."
            "Building chains of emotions and associations."
            "I had to build myself from scratch."
            "In this world where only Nothing exists, even a simple 'I' is already a huge victory."
            "The Void takes its time."
            "You're not going anywhere anyway."
            "And time... Time is all she has at her disposal."
            "Except I'm not here."
            "This paradox breathed new strength into me."
            "And I became me."
            show dreamgirl_overlay
            with flash
            "I looked around panically."
            "The emptiness and timelessness were spread out enough for me to breathe and move."
            "But it wasn't enough for me."
            "I knew, I understood!"
            "If there is anything in this void, it ceases to be so."
            "Then we need..."
            "Something blindingly bright streaked from the bleeding back in all directions."
            me "My eyes are clear again, the adrenaline is overwhelming!"
            "There it is, the most terrifying weapon against the void that I smuggled in here."
            "I brought «we»."
            "Us."
            "Not alone, a paradoxical phenomenon."
            "And the scarlet light fluttered slower and more reluctantly."
            "Its flicker was like a dying man's cardiogram."
            "Weaker and weaker."
            "Weaker."
            me "Ulyanka!"
            "Shouted I and rushed over there."
            "A light dispelling the darkness."
            "A dash."
            "A dash!"
            with vpunch
            "Palm."
            "Warm."
            "We rushed to the surface!"
            scene bg ext_emptiness_7dl at running
            with touch
            "Leaving behind us an inversion of speed, running away from something that couldn't possibly be, we were going faster and faster!"
            "The walls of the personal paradox were closing in around us, and I prayed for one thing only: to make it!"
            "Before..."
            "There were sounds all around us, and that indicated that we were almost there."
            "Only they sounded inside me."
            "A strange resonating echo that could, if listened to, be put into words."
            "Voices... Familiar!"
            "Asking."
            "Tempting."
            voice "Don't go on the road without a guide."
            voice "You must make a wish."
            voice "Do you want to start your life over?"
            voice "Do you want to know how to do the right thing?"
            "The emptiness knew where to strike."
            "Knew all my weaknesses."
            "Except I wasn't there now."
            "And while the transparent Ulyanka is unconscious in my arms, it's Us!"
            "The last obstacle had to be broken through by force."
            "Space inflated like a rubber ball, resiliently suppressed, but in no hurry to let through."
            "To the hardest blows, it responded in kind."
            "But eventually that problem was solved, too."
            "I've already figured out how things work here."
            "What powers have paradoxes and precedents."
            stop music fadeout 3
            stop ambience fadeout 3
            "As a result, the space wrinkled and spit us out on the bus."
            scene bg int_bus_night
            with dissolve
            play music music_7dl["emptiness"] fadein 3
            "And immediately We ceased to exist."
            play sound sfx_face_slap
            with vpunch
            with flash_red
            show us angry sport close with dissolve
            "My cheek was burned with an unkindly evil slap."
            us "What have you done, you bastard! You bastard!"
            me "Calm down."
            hide us with dissolve
            "I pressed her against me, dodging fists flickering in the air."
            us "Give me back! How could you?"
            me "You can't!"
            us "You can!"
            "Tears spurted from the girl's eyes."
            "She shook her head so violently that her 'rockets' lost their shape."
            "And I got hit in the nose with a half-braided tail."
            with vpunch
            with flash_red
            "And while I was squinting and groping to check for an eye, I got another kick in the stomach."
            "Ulyana bounced back."
            show us2 dontlike sport with dissolve
            us "I'll never forgive you."
            me "You could have died, you fool!"
            us "So?! I want to do it myself, it's my choice!"
            me "Die?"
            show us2 calml sport with dspr
            us "Even if I die! {w}It pisses me off that everyone is always deciding everything for me!"
            us "Haven't I waited long enough? Haven't I been patient enough?"
            us "Take me back! {w}I'm almost... I'm almost there!"
            me "You don't know what you're doing!"
            show us2 upset sport with dspr
            us "Really? Look."
            "With terrifying calm, the girl picked up the hairpin from the floor and drove it into her palm with all her might."
            me "Stupid!"
            "Something inside me gave me a little hiccup, and I rushed to her, snatching the dangerous object away."
            me "You're bleeding."
            "For some reason I said."
            show us2 angry sport with dspr
            us "I don't give a damn. I'm sick of doing what I'm told."
            us "You have no idea how old I am."
            us "Nobody around here has a clue, and I'm stuck here! In this here."
            "Ulyanka poked a bloody finger on her cheek in disgust."
            us "Stuck, can't mature, and you're pissing me off!"
            me "What have I done?"
            us "You exist! I'm drawn to you, and sometimes I want to kill the hell out of you!"
            us "And you know the worst part: there's no way that's going to change."
            us "No matter what I do or how I do it!"
            us "I'll wake up tomorrow the same way I was."
            us "Everything will disappear, from and to!"
            us "Stop tormenting me, let me go!"
            us "Nothing will happen to me, I'll be all right!"
            us "Even if something happens to me, it's better this way than doing what they tell me to do again, wearing those damn rockets and feeling like I'm forever a junior."
            us "A little doggie is a puppy all his life."
            us "That's the way it is."
            us "I hate being a puppy!"
            show us2 angry sport close with dissolve
            "I caught her again."
            "And even though she kept pounding me, I kept holding her to me."
            "Stupid girl doesn't understand what happened to her or where she ended up."
            "She can't understand."
            "She's sure she's found a loophole, only that loophole isn't where she needs to go at all."
            "She needs someone who knows at least a little bit about it."
            "And that's obviously not me."
            "But what can I do about it?"
            "I can't bring her back."
            "I don't know how."
            "Well, you would..."
            me "Do you want to go back to the camp? Back to your own people?"
            show us2 dontlike sport close with dspr
            us "I don't want to."
            "Grumpily informed Ulyana."
            us "I want to go back."
            me "You can't. I barely got you out."
            us "Fool, I don't want to go into the void, I want to go where it leads!"
            me "Where?"
            show us2 sad sport close with dspr
            us "Do you know why Alisa and I always called you rookie?"
            me "A nickname? I'm the new guy, I came..."
            show us2 smile sport close with dspr
            us "No. It's a nickname for a donkey like you."
            me "Thanks for the 'donkey,' that's very nice."
            us "Olga also asked so tearfully."
            "She mimicked the squad leader's voice ridiculously:"
            us "Please don't remind him, it's not good for him, he's very sick."
            us "Now there's a nickname stuck to you. Eternal Rookie."
            me "But what's that for? What's the point? If you all have known me for years, why all this farce?"
            us "Not for the first year only me, Olga and Lena have known you. Knew you."
            us "And with Alisa you met one winter, but you were not introduced to her."
            show us2 normal sport close with dspr
            us "But that's the way it was until last year."
            me "You're talking some nonsense."
            "I grimaced. Surprisingly, I was already missing it."
            us "Nonsense? Is it you who comes here every year and keeps forgetting everything?"
            us "Or is it you who comes back every time at the end of a shift and then just keeps on living?"
            me "I don't really know what you mean."
            us "And no wonder. You're not very bright at all."
            me "So be it. Now what?"
            show us2 smile sport close with dspr
            us "Uh... Let's go!"
            "She jabbed her finger at the button and nodded contentedly as the pneumatics hissed and opened the door."
            "There was exactly nothing visible on the other side, just an emptiness that emitted not a photon of light."
            me "Back?!"
            show us2 laugh sport with dissolve
            "There's no way I would have agreed to..."
            "And Ulyana, without letting me change my mind or do anything, jumped down the steps at a run, taking me with her."
            "Back!"
            show blink
        else:
            "And I woke up."
    elif alt_day6_us_7dl_mi_friends == 3:
        "We seem to have stopped, as the feeling of movement has gone somewhere."
        me "What happened?"
        show mi scared casual with dissolve
        mi "I don't know..."
        "Miku looked scared and depressed."
        me "I'll go check."
        mi "Maybe we should go together?"
        "From the looks of it, Miku suggested it out of mere politeness."
        "She really didn't want to leave the seemingly safe chair."
        "Except that safety is imaginary."
        scene bg int_bus_night
        with dissolve
        "When I got up and looked around, my eyes did not fail me."
        "It really was just the two of us."
        "In the whole bus."
        "Miku squeaked something behind me, but I couldn't afford to be distracted."
        "It felt like seconds were melting away, and there was nothing left to do before something extremely bad happened."
        mi "Senya..."
        "Without turning around, I waved."
        "I got to the driver's seat, and it was empty, too."
        "That's when I turned around."
        show mi sad casual tr1 with dissolve
        "And I almost lost my mind."
        "Miku went pale, faded, and looked translucent, like a ghost."
        me "Miku?!"
        "She lifted her trembling fingers to her eyes and looked at me through them."
        dreamgirl "It's time to say goodbye, Syomich."
        "The voice in my head was calm and full of empathy."
        dreamgirl "I wish you could have stayed together longer, but... You see."
        mi "What's going on, Senya?"
        dreamgirl "You have a few minutes to say the most important things to each other."
        th "But Miku..."
        dreamgirl "What?"
        th "I don't want to."
        dreamgirl "Do you think she wants to?"
        dreamgirl "You were too late in the game, it took you too long to find each other's hands."
        dreamgirl "You'd like a few more days, wouldn't you?"
        th "Yes..."
        dreamgirl "And they won't be enough, either. You understand, don't you?"
        dreamgirl "Besides, the laws of your universe deny her existence, remember?"
        th "But..."
        "I sighed."
        th "I'm going to miss her."
        dreamgirl "And rightly so! Bore, pine, grieve! Live!"
        dreamgirl "It's not a fact that you can meet someone like her once, but for the sake of what happened, for the sake of what didn't happen..."
        dreamgirl "You have to live."
        show mi sad casual tr3 with dissolve
        th "I'll live, I'm an immortal bastard."
        me "I don't know."
        "I honestly admitted."
        "It never occurred to me before that something like this could happen to a person - a living, real person! - could have something like that happen."
        mi "It can't be..."
        "She reached out to me, tried to touch my cheek, but missed me, went right through."
        "I didn't even feel anything, no wind, no cold."
        "Nothing."
        dreamgirl "Sorry."
        hide mi with diam
        "Miku shattered with a quiet, sad ringing, leaving me on the bus."
        me "Noooo!"
        "I rushed to catch her, but my hands grasped only emptiness."
        "And a tiny blue weightless ball of light sat on my nose."
        "It sat there, shining for a while, drowning it out."
        "All the while I stood there, fluttering my eyelashes stupidly."
        "In my chest an abscess ripened a feeling of the cruelest deceit, the kind that only comes in very early childhood when you first encounter injustice."
        me "You can't... You can't do that."
        "A moment later, something clicked in my head, and I realized I was left completely alone."
        me "Shit."
        "The world around me was covered in waves and blurred."
        "I fell into a chair and closed my eyes."
    elif alt_day6_us_7dl_un_friends == 3:
        stop music fadeout 6
        me "Something happened."
        un "I know."
        me "What? How?"
        show un serious dress with dissolve
        un "It will be over soon, Semyon. But right now I need to talk to you."
        me "Talk?! Look around you! Everyone's gone, we're standing in the middle of nowhere, and there's all this smoke!"
        un "We have a few minutes."
        me "How do you know?"
        show un normal dress with dspr
        un "Sit down, calm down, and listen."
        me "But..."
        un "It won't run away, honestly."
        me "How can you be so calm?"
        un "Prioritize, Semyon."
        "Cold-bloodedly declared Lena. And, realizing that I was all ears, she began:"
        play music music_7dl["iamsadiamsorry2"] fadein 3
        un "It all started last year. When there was you, there was me, and it wasn't enough to be Us."
        un "You left then, leaving me alone because you remembered something."
        un "And I..."
        show un serious dress with dissolve
        un "I was treated for four months in a closed hospital after I cut my wrists."
        un "I was silly, I cut myself shallow, and I cut myself crosswise. That's when Slavya intercepted me."
        "Lena exhaled convulsively."
        un "She asked me to give the world another chance."
        un "Naive idiot. {w}What more chance does this world need if it doesn't have you in it?"
        me "Where am I then?"
        un "Don't you get it? You're walking, smiling, talking, but it's not you."
        un "I know you. The way you move, the way you talk."
        un "So I waited and waited, came here in winter, but you didn't even recognize me."
        un "Patience kept melting and melting, and the only chance I gave the world was expiring like an expiration date."
        me "But I didn't know..."
        show un sad dress with dspr
        un "And if you did, would it make any difference? Even when I started recognizing you in you, you didn't remember me even then."
        un "So one day I just got fed up."
        "Lena smiled bitterly."
        un "There had been legends going around the camp for a long time about why they closed the old one, why they moved the new one east."
        un "And I knew."
        un "Knew everything. From my father. He was privy to the details of the case."
        me "Was someone killed here?"
        un "Not murdered. Much worse."
        "Lena shook her head, and I got a chill from the anticipation of something I really wasn't going to like."
        "In fact, her conversation gripped me so that I stopped paying attention to the strangeness of my surroundings and listened and listened, while pictures of the events described unfolded before my eyes."
        with fade
        me "What could be worse than death?"
        un "You can ask Ulyana about it. She knows for sure."
        un "And as of late, so do I."
        "The girl was talking all this nonsense with a look of utter seriousness, but since I promised to listen to her..."
        un "Ulyana had a brother, Anton. Who died in Afghanistan."
        un "1974, the same year a nurse hanged herself in the camp. There are still stories about it."
        un "And Ulyana... When she heard the news of her brother's fate, she ran away that same day after dinner and went to the place where rumor has it there is something that can grant a wish."
        me "A monolith of some kind."
        "Mumbled I."
        me "And really, no?"
        show un grin dress with dissolve
        un "You listen, the most interesting thing is ahead."
        "After looking at me again, Lena nodded and continued."
        show un normal dress with dspr
        un "The adults did not immediately notice the loss, but when they realized what was going on, they immediately rushed after her."
        un "Boris Alexandrovich, as luck would have it, was out of town and couldn't help the case."
        un "I don't know exactly what happened, but that same night she was brought to the camp. Only it was no longer Ulyana. Her personality became like a blank slate. Such people are called erased."
        un "She hasn't grown up or aged for a very long time, and in fact she's older than even our squad leader."
        me "Who isn't there now."
        "I noticed."
        un "I'll be gone soon, too. But I wanted to tell you the most important thing:"
        "The last words were definitely hard for her."
        un "After our conversation at the quarry, I went where Ulyanka once went."
        un "I went to a place where you can make a wish and it will surely come true."
        un "You see, the chance you give to the world is worthless by itself if you don't back it up with something. And I needed certainty."
        un "Ulyana was the last victim of the old camp."
        un "She is erased, Semyon. Restored erased, a secondary birth certificate..."
        un "And I now have at least the certainty that we can at least have something."
        me "But what's the point? Why? Couldn't I have done it myself..."
        show un sorrow dress tr1 with dissolve
        un "You thought you were following your heart, your will."
        un "In fact, you were just fulfilling the desperate wish of a fool in love with you."
        un "And now you're doing it."
        me "I chose you myself. Consciously!"
        show un sorrow dress tr2 with dspr
        un "I know."
        "The transparent lips already smiled."
        un "Because I wished for you."
        un "I loved you so much I couldn't wish for anything else."
        show un sorrow dress tr3 with dspr
        un "And now goodbye."
        me "What? But what about your wish?"
        un "It will surely come true."
        "Almost silently she murmured."
        un "Just meet me on the other side."
        un "Goodb..."
        hide un with diam
        "With a faintly mournful groan, the translucent figure of a girl burst into violet sparks, warm to the touch, kind, affectionate."
        "They fell to the floor, frozen underfoot as a parody of the starry sky."
        "And it seemed sacrilegious to trample them as the last memory of a girl who never existed."
        "I climbed into a chair with my feet and, hugging myself to my knees, closed my eyes."
    else:
        "And I closed my eyes, feeling as cozy as if I were at home under a blanket."
        "There was no bitterness, no regret."
        "Only an irresistible desire to sleep and a foreboding sense of impending denouement."
    stop music fadeout 3
    stop ambience fadeout 1
    return

label alt_day7_us_7dl_wakeup:
    scene bg intro_xx with fade
    play sound_loop sfx_bus_interior_moving fadein 4
    "I woke up to an unfamiliar voice and incessant poking on my shoulder."
    voice "Hey, wake up, man!"
    me "Uh... What?"
    "Everything in front of my eyes was floating and my head was splitting."
    "But that, too, bothered me less than the fact that it hit my brain:"
    th "Sovyonok!"
    "Camp, children, friends - easy come, easy go?"
    "But how come there's a wound in the soul of that size?"
    voice "You overslept, didn't you?"
    voice "Sorry, I tried to wake you up, and you're like a drunk, just mooing something."
    me "T-thank you..."
    "I squeezed out."
    "And as I looked out the window, I realized I hadn't overslept at all."
    "My subway station was at the terminus, so there was absolutely no way I could oversleep or pass."
    "With my lifestyle, all days are like one another, and what happened last year and the year before feels like it happened yesterday."
    "Like, for example, my route toward the abyss."
    "I wanted to throw a tantrum, but I habitually pushed my emotions inside."
    "With an appreciative nod to the conductor, I stepped outside."
    stop sound_loop
    scene bg ext_city_night_7dl
    with dissolve
    play ambience ambience_cold_wind_loop fadein 3
    play music music_7dl["fsl_tn"] fadein 3
    if alt_day6_us_7dl_un_friends == 3:
        "My icy, unsociable autumn."
    else:
        "There's a winter in town. A soul-wrenching, tear-wrenching winter."
    "It rings the wires with a requiem for the unfulfilled, it picks me up as if on wings and carries me toward nonexistence and oblivion."
    "But much more often it just slams me against the nearest wall with all its might."
    if alt_day6_us_7dl_un_friends == 3:
        "Oh the fists of the people I shrug at, wandering the streets in a half-drunken delirium."
    else:
        "Winter doesn't like me, she's jealous that I managed to escape for a whole week from a place from which it seemed impossible to escape."
    "I spit blood and get up for the umpteenth time already."
    "I wish I could just go to sleep one day and not wake up."
    "So that there, on the other side of my closed eyelids, I could see what I once lost."
    "What was this camp? Why did it happen to me?"
    "And in the quieter voice, the way a man's conscience usually speaks to his conscience:"
    th "Did it really happen?"
    "I really wanted it to be."
    "Perhaps I should have done something, changed somehow, just clung to the most important thing for me and held on tighter?"
    "No one will say anymore."
    if alt_day6_us_7dl_help:
        "It's another December on the calendar."
        "Time to decorate the tree, run to the nearest supermarkets for goodies for the New Year."
        "And, of course, chocolates for the smiling tiny sweet tooth."
        "Then rushing home, anticipating the door swinging open after the bell, my personal miracle smiling blue-eyed, jumping on my neck, shouting 'Syomich has arrived!'"
        "I imagine this picture so often that I almost believe it as I step off the bus."
        "I almost earnestly expect to dial the doorbell and hear the grinning, grumpy: 'Well, who's there?'"
        "That sometimes I even forget to take my keys out of my pocket and can listen to the scattered trills of the bell for several minutes."
    elif alt_day6_us_7dl_mi_friends == 3:
        "The holidays are coming. The New Year is coming."
        "And one must go out, meet the happy looks, smile back at them, wish them happy holidays in return."
        "Gotta live."
        "And I can't feel life, it's like some half-needed organ inside me that's been responsible for it all my life has bloated and died out."
        "I still exist, satisfy the needs of the body, even sometimes feel a kind of withering interest in what's going on."
        "But long forgotten and buried are the loud passions, the anticipation to shivers and happiness to tears."
        "As if dimmed and dimmed inside the light, lowered the volume of sounds."
        "I am overgrown with dust."
    elif alt_day6_us_7dl_un_friends == 3:
        "The water is raging, breaking the black waves and breaking the ice that has frozen the shores, blowing piercingly, and getting cold fingers under my clothes."
        "And I sit on the shore and stare into nothing, seeing with my own eyes a very different picture, a very different society."
        "It's as if a plaid plaid is spread out on a bench next to me, with a metal thermos of herbal tea and a charger with headphones for my phone nestled on it."
        "And about to run in, my sunshine will come back, throw the blanket over my shoulders, I'll turn the lid off, splash on some warming, and we'll sit in silence looking at the black stretched nerve of the horizon."
        "I squinted at the seat beside me."
        "It was snowed in."
        "The same one that wrapped a cozy blanket around my shoulders, too."
        "I am alone. All alone."
    "The only salvation, the kick in the ass to myself, is a reminder:"
    me "Remember, just remember."
    "I say to myself."
    me "You don't have a soul, you fool. You are the soul. You have a body."
    me "It'll happen, just wait."
    "I've been waiting. Almost a year now."
    "It hasn't been hard or easy."
    "In fact, I didn't feel any different from before that ill-fated bus."
    if loki:
        "I still got on the subway in the morning and went to work."
        "I carried music into the hearts and souls of children, for which their parents were grateful."
        "The motivator for the last line of defense that got me moving a little bit was just that incident in the park."
        "Numerous fractures, frostbite, bruised internal organs..."
        "I spent two months in the hospital, half of which I was on painkillers."
        "They were the only thing that saved me when I wanted to howl."
        "But they discharged me in February, recommended a lot of diets to recover."
        "Recover. Ha."
        "What diet would get me back into music?"
        "What treatments would find another key to the door to summer?"
        "A cobbler without boots, a music teacher incapable of extracting even a few notes without breaking into a bloody cough."
    elif herc:
        "They say a man gets used to everything."
        "Lottery winners don't feel as good after a year as they did when they won."
        "Conversely, a totally paralyzed person doesn't feel as miserable as one might think."
        "I was luckier - I only lost an eye."
        "Going to the other world piece by piece."
        "Now I see the world around me as flat and without depth."
        "At last my physical vision is in harmony with my mental vision."
        "It took Maha a while to get used to my new appearance. But it took her a lot less time than it did for me."
        "At least they think I'm a hero now."
        "Exceptionally heroic, catching a bullet with your head. Fortunately, the second one didn't hit the target."
        "But you could go on sleeping for money if you were completely paralyzed."
    else:
        "True, I was in the hospital for a month after they fished me out of the bottom of the Neva."
        "Our valiant rescuers, connoisseurs of human souls."
        "I could almost believe it was about to end."
        "That I would breathe this bitter death and it would put me out of my misery."
        "Instead it was the Botkin Hospital, bilateral pneumonia and a course of antibiotics."
        "When I got home, it was all dusty and there were nothing but utility receipts waiting for me."
        "I'd like to believe that at least someone remembers me."
        "But machines did all the calculations a long time ago."
        "Like the one ten years ago that found no crime in the actions of a car skidding on wet asphalt, keg balling a strike."
        "Must be solidarity?"
    "That's why there's silence and crackling keys in my apartment."
    me "Hello?"
    ai "Hello."
    me "How are you?"
    ai "Fine."
    me "And I'm... fine."
    "I'm so scared to be alone, because when I close my eyes, faces and events and names come to mind..."
    "No chatbot can help me deal with that."
    "Only time. They say it heals."
    me "But why so slow? And why does it hurt so much..."
    play sound sfx_intro_bus_stop_steps
    pause(3)
    scene anim intro_4
    show blind2_1
    with fade
    "Sometimes I see someone on the street, and something stops inside."
    "I run after them with a scream, catching up with them... I apologize."
    "Lately, so many people have started dyeing their hair exotic colors, getting exotic hairstyles."
    "Even walking and acting so... {w}that I involuntarily see things in them that I wish I could forget and stop torturing myself."
    "Every such encounter is a knife to my heart."
    "It makes me want to beat my fists into unfamiliar faces that dare not be you."
    hide blind2_1
    show blind2_2
    with dissolve
    "I look in you for what I have lost in others."
    "That which..."
    "Bottomless eyes from one, hair and a smile from the other-I'm so diligently assembling your image that it feels like you're about to step off the glossy cover, smile and embrace me."
    "Just a little more."
    "So I walk around the city, catching snowflakes with my heated lips, and I'm afraid."
    "The dark hulk of a house that hates me, lurking in the twilight, when only hunger and fatigue drive me into a stone embrace."
    hide blind2_2
    with dissolve
    if alt_day6_us_7dl_help:
        scene
        $ renpy.show("bg ext_mv2_7dl", what = Desat("bg ext_mv2_7dl"))
        with fade
        "And more and more often I catch myself coming to my senses at Moskovsky Station."
        "It's like I'm drawn there by some unknown thing, some unknown why."
        "Maybe it's just that I have nowhere to go back to."
        "Maybe it's something still hidden in the back of my mind."
        "One day it will wake up, but I won't wake up anymore."
        "Unless I wake up late, when the ticket has been postponed and the houses are running back outside the windows."
        with fade
        "I don't doubt that at all."
        "And I'm not afraid."
        "Somehow I'm pretty sure I'll have someone to meet me at the station."
    elif alt_day6_us_7dl_mi_friends == 3:
        "And sends me dreams accordingly."
        "I see how we became together."
        "As the wind tears our clothes, as we seek warmth in each other's arms."
        "How the long tails of the hair embrace us."
        "And your lips are sweet."
        with fade
        "After these dreams my eyes are always wet, and I don't want to live at all."
        "But I'm still holding on."
        "I still have hope."
    elif alt_day6_us_7dl_un_friends == 3:
        "She's waiting for me. And I'm waiting for the moment."
        "One day it will become too nothing, when nothing can touch me at all."
        "Then I'll make up my mind."
        "I'll remember what it's like to catch the wind with my wings open."
        "And I'll dive into the low, leaden sky."
        with fade
        "I both dread it and wait for it with the sweet and enthusiastic faltering that only comes at the edge of an abyss."
        "The green-eyed abyss."
    else:
        "I live in constant fear of something."
        "Constantly afraid of something."
        "Sometimes I think I wish I'd never regained consciousness in that hospital."
        "Everybody would have been better off."
        "Everyone would have been happy, and we'd all have remembered without shouting."
    scene bg int_sam_room_7dl
    with dissolve
    if alt_day6_us_7dl_help:
        "But I try not to pine for much, I chortle and keep my tail between my legs."
        "I know for a fact you wouldn't approve of the sissy I'm turning into."
        stop music fadeout 5
        "Sometimes it gives me the strength to go on living."
        "But only sometimes. After all, a whole year has passed."
    elif alt_day6_us_7dl_mi_friends == 3:
        "When I charged and plugged the phone in, I found a whole one missed call."
        "What's much worse, I found there..."
        scene bg ext_camp_entrance_day
        show mi smile casual
        show prologue_dream
        with dissolve
        "With a sigh, I reached out my fingers and touched the cold glass of the photo portrait standing on the table."
        "I remember when I was doing a printout at the atelier, the employee smiled understandingly and lowered his voice:"
        voice "Cosplay, huh? Very nice."
        me "It is."
        voice "What's the anime, can you tell me?"
        "I wish he knew what that anime was."
        "But that's a secret I'll keep forever unsolved."
        "I won't show anyone, just like I won't show pictures of a very beautiful girl who, by all canons, shouldn't exist."
        "She shouldn't."
        "But the picture is right here."
        "I remember every last second of it."
        "Smiles, laughter, tears. The silver bell of the voice."
        "And the way the vein on her alabaster neck was pounding."
        "Shouldn't exist."
        "She's more real than anything around me!"
        "I mean..."
        scene bg semen_room_window
        play sound_loop sfx_street_traffic_outside fadein 2
        "I reminded myself of an old art-house photograph done in sepia technique."
        "A girl walking her dog."
        "A huge Mastino Neapolitano, wiry, creased, heavy even in appearance, frozen in a moment's fall."
        "The clawed paws, a bit of inertia sideways from his body, a doomed expression on his muzzle..."
        "A huge, but already very old dog."
        "He must have spent days in the same place - I've heard that in some homes they set aside a separate chair for a beloved dog - and kept waiting for that very, inevitable one to come."
        "Yearned and anguished with conscience at leaving his human."
        "A man is foolish and weak, he's bound to get into trouble, he needs an eye on him."
        "But at night I dream of him as a puppy running after a ball, and how good his mother's belly smells, and how funny the squeak of a bundle he once brought."
        "The dog sniffs the bundle and realizes it's his man now."
        "And now twenty-five years have passed."
        "The old dog's paws twitch in his sleep as he runs after the ball."
        "He whines, licking the crying face of something upsetting the man."
        "He's pining and very guilty."
        "The photographer managed to catch the moment and capture exactly what was needed."
        "The dog's realization that he can't get up anymore."
        "The guilt of having to go on alone."
        "Because the frail girl on whose leash the hero of the story was walking would never in her life be able to lift him up."
        with fade
        "That's what I am."
        "My legs have already broken, I'm already falling sideways."
        "Just a moment before I hit it, and I'm frozen, too."
        "And in a way, it's a good thing Miku isn't around. Because she wouldn't have been able to pick me up either."
        "I love and believe in her very much."
        stop music fadeout 5
        "But that's a burden she can't bear."
        "I extinguished the cigarette butt, threw it out the window, and walked away from the window."
        stop sound_loop
    elif alt_day6_us_7dl_un_friends == 3:
        "There were lines going round and round in my head..."
        "But the bloody traitor - memory remained deaf to my prayers."
        "I couldn't remember the address you left me."
        "If you ever did."
        scene bg ext_camp_entrance_day
        show un smile dress
        show prologue_dream
        with dissolve
        "By the way, after I charged my phone, I found a picture of you in my phone."
        "Incredibly bright, impossibly beautiful."
        "There's no such person by definition, otherwise all the star models would kill themselves with envy."
        "They spend a lot of time on makeup and staged shots."
        "And this is just an amateur phone-camera photo, not the best quality either."
        "And you can barely see the pouty lips that adorn the girl."
        "Of course not. The best part's coming up."
        "I smiled involuntarily as I remembered our time together."
        "That must have made me do something completely crazy."
        "I gutted the picture in the editor and pulled out the metadata."
        "EXIF, where the geographic location is written, if you have that turned on in your settings."
        "I had."
        "Moreover, even though I couldn't pick up any satellites or cellular operator signals at the time, something did add to the properties of the picture."
        "Funny, isn't it?"
        "And Google Maps gave up a point in an empty field where no campsites had ever been."
        "It's very simple."
        "This world can't produce Lena's beauty, Slavi's empathy, Ulyanka's flightiness, and Miku's incredible attraction."
        stop music fadeout 5
        "The problem is in the source material."
        "You can't make a diamond out of mud."
        "No matter how hard you try."
    stop ambience fadeout 1
    return

label alt_day7_us_7dl_tran_mi:
    play music music_list["farewell_to_the_past_edit"] fadein 5
    scene
    $ renpy.show("bg ext_city_night_7dl", what = Desat("bg ext_city_night_7dl"))
    $ set_mode_nvl()
    "I soon realized that I wasn't quite where I was supposed to be."
    "It was very easy to realize that, from the first few months of my life here."
    "Or should I say, the first two..."
    "Well, a man shouldn't be able to survive the situation I'm in!"
    "It doesn't happen, because it doesn't happen at all!"
    if loki:
        "The heavy pounding I had to endure was set up for a strictly defined purpose."
        "I wasn't intimidated, punished, or brought up."
        "No, I was purposefully killed. {w}And quite successfully, as far as I can tell."
    elif herc:
        "I distinctly remember being shot. Twice."
        "But here I woke up in the hospital, with my head in pieces."
        "Yes, I lost an eye, but after something like that I shouldn't have woken up at all."
    else:
        "A bus that flew eighteen meters vertically, plunging into the depths with all its might..."
        "When I was very young, I tried to fight my hydrophobia through education."
        "I told myself that I needed to know the enemy, and I studied everything I could find about swimmers, behavior on the water."
        "So I knew very well how long a man could last in icy water."
        "Knew how long it would take him to spend without air to be guaranteed to go sunbathing on a slimy couch in a morgue."
        "So I didn't believe in miracles."
        "And my fear ended up killing me."
    nvl clear
    pause(3)
    "It would seem - here it is, a new chance, a new life! Try it!"
    "But what's there to try if no one in this life had ever heard of a performer like Hatsune Miku."
    "And there wasn't much to learn on the Internet either: things must have gone a little differently here, and «Yamaha» didn't license the vocal processor."
    "In my eyes, of course, this world has become noticeably impoverished."
    "But the people around me didn't think so."
    "They had enough foolishness without mass hysteria over one non-existent girl."
    "So did I."
    if loki:
        "I continued to work at the same pioneer house, only now it sounded more like a mockery than a respect for the institution that used to be here."
    elif herc:
        "I continued to sleep for money in the same store. Zina thought I was a hero. I just thought I had worked off my paycheck for the rest of my life."
    else:
        "I continued to work as a freelancer, occasionally going out to visit an organization where I worked part-time as an IT guy."
    "New life and new chances of continuing to be a vegetable."
    "There was absolutely no incentive or need to keep going."
    "But little by little I began to learn Japanese hiragana and katakana."
    "No, not for self-development, solely for other purposes."
    "I moved almost entirely from the Runet to the Eastern sector, where without knowledge of hieroglyphics there was nothing to be found."
    "And I searched."
    "I searched forums, news feeds, social networking sites."
    "One of them had a name that sounded like a taunt: Mikushi."
    nvl clear
    pause(3)
    "Just one mention was enough for me."
    "Just one tiny hint."
    "And I would have jumped out of my seat and taken the next plane to Sapporo."
    "After all, it's been a hell of a year!"
    nvl clear
    pause(3)
    "Every night I logged on to Mikushi, Facebook, Nico-Nico, Twitter and Amoeba with the despair of a doomed man..."
    "I spent all my time before bedtime searching for the queries «Miku», «Hatsune», «Fujita», «Saki»…"
    "And I didn't find anything. There were namesakes and people using these words as pseudonyms."
    "But the very manner of their speech gave away the impostors headlong."
    "I could not imagine that the things they wrote could be voiced with a silver bell."
    nvl clear
    pause(3)
    "The money was coming in, and I hardly spent it, saving it for the very time I needed to get out."
    "Jesus, I even got myself a guarantor in Japan in case I needed an emergency visa!"
    "On that very same «Mikushi»."
    if loki or herc:
        "She was interested in my country, culture, people."
        "Moreover, she even wrote decent Russian."
        "She was going to be in St. Petersburg next summer and made me promise to accompany her."
        "She herself was willing to act as a guarantor for the embassy, confirming that my goals were strictly tourist and romantic."
        "Her name was Ryoko."
    else:
        "Totally by accident."
        "Missed a key during another search, and my fingers typed a different name instead of «Miku»."
        "It came up with about a thousand different people, but she was the first one on the list."
        "When I opened the page, I stared at the half-forgotten features of her face for a long, long time."
        "Perfect trim, black hair, and a brown-eyed squint."
        "The only person who never caused a scandal or tried to educate me in any way."
        "Once just self-effacing out of my life."
        "The eternal child, Ryoko."
    nvl clear
    pause(3)
    "Except I didn't need that visa."
    "I didn't meet anyone I knew, even though I scoured millions and millions of people."
    "To make matters worse, there wasn't that house on the map of Sapporo between Odori Park and the subway."
    "And, therefore, neither was Apartment 3108."
    "And it could hardly have been a new development - the Japanese are extremely zealous about their parks to allow anyone to develop."
    nvl clear
    pause(3)
    "I could have lied as if I thought Ryoko was jealous of my quest."
    "She's a girl, and girls care about attention."
    "But instead she treated my story with lively sympathy."
    if dr:
        "Apparently our brief affair left a good impression on her mind, too, I don't know."
        "I never loved her, maybe that's why I didn't try to blow her mind."
    "What's more, she tried to find my starlet, too, through some channels of her own."
    "In vain. In vain."
    "Only greasy fingerprints on the glass, clearly visible from this angle because of the reflections from the street."
    "There must be 365 by now, by the number of days I've shown up as a self-confident reality conqueror at my house."
    "Confident that true love and adventure and a happy reunion at the end awaited me here..."
    "But the creator, as always, had his own plans for me."
    "If you can call it a plan to sit by the monitor."
    nvl clear
    pause(3)
    "My Miku."
    "I see you in other people, in other faces."
    "Sometimes I think we might well have lived in the same city, even on the same street."
    "We just didn't know it."
    "And now that I've been looking for you for so long, we'll meet."
    "Right now. Just like now."
    nvl clear
    pause(3)
    "You're a laughing girl, you're a moe girl."
    "And it makes me want to take a line from a fellow entertainer and rework it a little."
    me "My moe, please don't throw me ashore..."
    stop music fadeout 3
    scene bg intro_xx
    with dissolve
    play sound_loop sfx_intro_bus_engine_loop fadein 3
    "Can you hear my thoughts? Can you feel even remotely?"
    "Do you remember?"
    "I looked through the frozen glass of the bus and couldn't convince myself that she could hear. Remember."
    "Or at least exists."
    nvl clear
    $ set_mode_adv()
    "Some near-political goofballs started broadcasting on the radio, and the stern driver, after mentioning God, soul, and mother, twirled the receiver knob, switching the wave."
    play music music_7dl["shib_mono"] fadein 3
    "And I froze, once free of moping and melancholy."
    "From the radio came a half-forgotten, half-familiar tune."
    "And I tried, but I couldn't remember it."
    "Something was on the tip of my tongue, but I couldn't remember it."
    "Something I'd heard a long time ago, something I firmly associated with only the best thoughts and experiences."
    "The funny thing is that the vocabulary I've learned in a year is enough to know what the song is about."
    "And why it so easily resonates with me."
    "Except I couldn't remember where I'd heard it."
    "And I would cry tears of anger."
    "And melt into tears."
    "But I can't."
    stop sound_loop
    stop music fadeout 3
    "I leaned my head against the glass again and covered my eyes."
    play music music_7dl["deep_inside"] fadein 3
    scene anim intro_3
    show blind1_1
    with dissolve
    "And all day long I was sick as hell from misunderstanding."
    "I walked the streets, trying to remember or conjure up a chain of associations."
    "What's more, I recorded a tune that I hummed as best I could so I wouldn't forget it."
    "And nothing... Nothing."
    hide blind1_1
    show blind1_2
    with dissolve
    "When I finally came to my senses, it was early eleven o'clock, and I could feel how frozen my fingers were."
    "And - nothing."
    "Like cutting off something that should have helped me."
    hide blind1_2
    "And somehow I knew it was important."
    "Not with my luck."
    "Figuring out which way my house was, I headed that way."
    scene bg int_home_lift_7dl
    with fade2
    play ambience ambience_7dl["elevator"] fadein 3
    "I got home at midnight, slipped past the disgruntled stare of the concierge, called the elevator."
    "I kept humming and humming that tune, trying to remember it properly."
    "I had some music recognition software, and I wasn't going to just give up."
    "And this is me, the perpetual indifferent and calm, humbled and accepting of the fact that I'm a loser."
    "It was so unlike me..."
    stop ambience fadeout 6
    scene bg int_sam_room_7dl
    with dissolve
    "Most of the people around here were already asleep."
    "It was time for me, too, I guess..."
    "Shazam couldn't figure out the tune, neither could his alternates."
    "So tonight was a night of disappointment. Another one."
    "And not to make matters worse, we should go to bed."
    me "Bad day. Tomorrow will be better."
    "I muttered under my breath, about to send the computer to bed and follow suit myself."
    "But there was a sudden rumbling, clattering noise under the window..."
    "From the sound of it, it was some pretty powerful engine, as if not a bus engine."
    me "A VIP take-home delivery?"
    "I grinned, falling at the..."
    play music music_7dl["shib_stereo"] fadein 3
    "And then immediately surged as the silence cracked under the thump of the super-heavy bass!"
    "A very, very familiar bass!"
    "The same song, the same harmonics."
    "And it got even stranger when the familiar silvery bell of the voice joined in the overflow of the bass:"
    mi "Hitorigoto furete..."
    "Not believing my own ears, I went to the window and carefully looked out into the street."
    me "No way."
    "Confused, I said."
    me "The year..."
    "But it was exactly as it was."
    "Downstairs, under the windows in front of the bus that had opened the luggage compartment doors, where the speakers still appeared to be hiding, in the same fur coat with the microphone stood..."
    stop music fadeout 5
    me "Miku."
    "In a faltering voice I stated."
    me "But you don't exist, you…"
    play music music_7dl["semische"] fadein 3
    voice "Stop hooliganing, I'll call the police!"
    "A squeaky voice came from somewhere."
    "But I couldn't hear it anymore."
    scene bg int_access_day_7dl
    with dissolve
    "Putting on the first thing I could get my hands on, I raced down the stairs!"
    "Seven floors... Six... Five..."
    play sound sfx_open_door_kick
    pause(1)
    scene bg ext_khruschevka_winter_7dl
    show mi happy winter
    with flash
    "When I jumped outside, the music had already stopped, everything had been turned off, and there she was, standing in front of the door."
    me "Miku."
    "Clapping my eyes stupidly, I said."
    mi "Senechka, you promised me something! It's time to keep your promise!"
    me "But..."
    mi "No time to explain! Get on the bus before the police really come and arrest us all!"
    me "I've been waiting for you for a year, and you just show up and say..."
    show mi sad winter with dspr
    mi "Senya, I really don't have time. At all."
    me "Can you at least tell me where you've been all year!"
    show mi laugh winter with dissolve
    mi "Where we're going now!"
    "Listening to no more of my objections, she grabbed me and dragged me along."
    mi "And this time you're coming with me!"
    me "Where?"
    show mi normal winter with dissolve
    mi "To «Sovyonok», Senechka."
    "There was something in my chest, all the words were suddenly forgotten."
    "I stepped on the first step of the bus."
    scene anim prolog_2 with fade3
    "\[Miku ending unlocked - «You're coming with me!»\]"
    $ sdl_persistent_inc("us_7dl_tran_mi")
    play sound sfx_7dl["aunl"]
    show acm_logo_us_7dl_tran_mi with moveinright:
        pos (1600, 1020)
    pause(7.4)
    call alt_7dl_titles
    return

label alt_day7_us_7dl_tran_un:
    play music music_7dl["so_lonely"] fadein 3
    scene bg ext_winterpark_7dl with dissolve
    $ set_mode_nvl()
    "You know I come here every month, on the twenty-fifth."
    "Just because a sad girl once wiped tears from her green eyes and asked me to meet her on the other side."
    "And here I am. Again."
    "And here little and seldom changes-the grumpy seagulls seem to be nailed tightly to the sky, the wind blows on the same cheek every time."
    "Only once in a while does one get lucky and a sunset sun peeks through the scattered clouds, tinting the world purple and gold."
    "A new cigarette, an old track in my headphones - as a sign of the continuity of everything."
    nvl clear
    pause(3)
    "We were saints in our philistine simplicity, we lived without trouble, simply because we didn't know happiness either, and we had nothing to compare it to."
    "And a man who has learned happiness does not want to live."
    "No, he wants to escape life and save his tiny native from the cold wind and indifferent looks."
    "So I'll never show you to them."
    "I'd rather smoke a new cigarette, set my sober eyes to the wind, and spit on the fear of getting cold and sick again."
    "It's as if everything vulnerable and weak had frozen out of me that December, crusted and splattered with shards, leaving me present."
    "Poems under absinthe, frantic crying, empty texts sent to the silly address of 'please let the one read them.'"
    "You told me that you had backed up, that you had thought of everything, and that I had no free will except to go along with you."
    "And here I am. Tired of being afraid, tormented and exhausted, spitting on logic and continuing to blindly hope in the middle of nowhere."
    nvl clear
    pause(3)
    "I had one single clue that I took advantage of, and all I had to do now was just wait."
    "A month, a year, ten years..."
    "I knew full well that my visits would probably end in nothing good."
    "In perfect harmony with my karma and good fortune, I'm only supposed to fail at the end of a lifelong race."
    "But a man must live for something!"
    "And that city waiting for me is not mine. It's made up and embodied in concert with someone else's speculation about what St. Petersburg should look like."
    "Except..."
    "My St. Petersburg has never been obscured by fog."
    "Yes, it hated me and tried to grind me with millstones as it raced forever from womb to grave."
    "But he was mine. And as I see it now, that's where I think there could have been a place for both of us."
    "Foggy fog... Only once in a while will throw a handful of my native rain in my face, which at all times has spit on gravity and warm clothing."
    "I will shudder, I will gape and see how far I have come, horrified at the thought that there is no more way back."
    "But that, too, is gradually ceasing to matter."
    nvl clear
    pause(3)
    "It's different here, different... My only clue led me here."
    "And it turns out that there was never any camp here."
    "All I could find was a painfully familiar bend in the river, two islands, and a string of steel rails pulling together the far banks."
    "There was only a debarker on this side."
    "A wharf for small ships and boats of the kind that could pass through here."
    "There was never any camp here. None."
    "My instinct for self-preservation cries out, If so, then I'm just dreaming!"
    "So I have to pick myself up and go on living in full agreement with the signal from my subconscious."
    "It wanted to live, and I was burying myself alive under a thickness of dust, that's just the self-motivator!"
    "Except I could never make up a girl like you."
    "A fragile figure, funny ponytails and a desperate plea not to leave you here, where without me there is no life or meaning."
    "I remember everything."
    "So this shore is all mine. {w}The bench, the awning, the smoky fire there, it's all my doing."
    nvl clear
    pause(3)
    "In my head, incoherent fragments flashed, making me angry, smiling, and choking with the tenderness that came over me."
    "I look up into the unfriendly sky and repeat with one lip:"
    me "Lena."
    "The only warming and toning on this shore."
    "Short name, four letters."
    "The whisper echoed, scattered by the wind, scattering the name in snowflakes."
    "And soon they were gone too, leaving only me, the black water and the icy wind, from which I was saved by a ski jacket and tea in a thermos."
    "I'm stubborn."
    "Surprisingly so, isn't it? All my life I've drifted with the current, and now all of a sudden I get my horn and I come and I come here..."
    "Just because a green-eyed girl with a sad look once told me a scary tale and asked me to meet her on the other side."
    nvl clear
    pause(3)
    "And again another man's memory."
    "Again my legs are humming from running after the streetcar."
    "Again we walk side by side, laughing till our stomachs hurt, tickling, bouncing, rejoicing."
    "We are full of happiness and life."
    "The most important thing is that we're together."
    "We've been together since first grade, when I was led by the hand into a new school, introduced to the class, and I immediately noticed the dark hair, the too-big head, and the huge green eyes."
    "I was seated at the desk next to her and she giggled and held out her palm to me and introduced herself."
    un "Lena. Shall we be friends? I love to draw and one day I want to draw the whole world! And you?"
    me "And I... I don't know."
    "I just couldn't fit a dream of this magnitude in my head."
    "So somehow at once and without inner resistance I knew I had to stick with someone like that."
    "Of course I'll be friends with you."
    "But man assumes, and randomness, as you know... We made him laugh with our plans, we made him laugh."
    nvl clear
    pause(3)
    "Six months later, Lena was in the hospital for surgery, and for about six months she was being treated and homeschooled."
    "I ran to her every day, carrying carrots and blueberries, because they were said to be good for the eyes."
    "I whistled under the window, climbed up the trunk of the linden tree leaning against her house, and jumped onto the floor of the room covered with drawings, each time more and more skillful."
    "She seemed to me, even then, with her bandages on, her huge round glasses, the most beautiful thing in the world."
    "And what was her attraction to the awkward tomboy? Who knows. But she was always so happy when I came over."
    stop music fadeout 4
    nvl clear
    pause(3)
    play music music_7dl["misery"] fadein 3
    "And would keep coming, and we'd have a silly, corny story about the kids being together since first grade."
    "As if it wasn't enough, my parents moved away and I went back to a new school."
    "Lena waved her fists and demanded that I stay."
    "Called my mom and asked that she be sent to that other school, too, but... rehab, you know."
    "For a while I spent my breakfast money on my way to my best friend's house, carrying fruit and some goodies."
    "Until I got caught doing that one day."
    nvl clear
    pause(3)
    "So the next time we met was when we were sixteen years old."
    if loki:
        "I got into music, got more serious, no time for nonsense."
        "But how can I stay serious when one day at the medical center where I came to give blood, I saw familiar ponytails on the couch in the lobby."
    else:
        "Not knowing where to go, I decided to try my hand at being an eccentric."
        "Programmer. So I went to a preparatory course."
        "I needed to get a proper medical card, so I had to go to clinics and medical centers."
        "And then at one..."
    "She wasn't wearing glasses anymore - she'd switched to contact lenses, but it was still the same Lena."
    "Still smiling naively at the world, looking at it with wide-open eyes."
    "Although there was a tiny bit of bitterness in her gaze."
    "We sat there for several minutes, not knowing what to say or where to put our hands."
    "Two silly teenagers."
    "And here again she was much more reasonable and gracious than me: she put the clipboard aside, got up, and ran to me."
    "Choking, she talked about something on the run, tripped..."
    "I caught her by the floor."
    "How much easier it would be now, when all I had to do was exchange contacts, phone numbers..."
    nvl clear
    pause(3)
    "We dated for a while, walking together in the park, shelling each other with chestnuts and going into the water of the Gulf of Finland for two hundred yards, just tucking our pants in."
    "We held hands and people around us called us a beautiful couple, but back then I just didn't think about things like love, living together, other stupid things."
    "We were kids, and that's the only thing that justifies me."
    if loki:
        "Because when Ksyusha came into my life and I reported it, Lena just smiled and wished me luck."
        "She said that if I needed help or advice, I could always turn to her."
        "She looked away, though, for some reason."
        nvl clear
        "She hasn't written or called once since."
        "Her phone was constantly disconnected, so I figured she'd changed numbers and tried her best to uproot me from her life."
        "But I didn't care too much at the time."
        "Ksyusha's last visit nearly sent me to the morgue, so lying in my hospital bed, I took words like 'toxemia' cold and distant with my medication-floating mind."
        "So Lena... I was really sorry."
        "But I didn't even know where she lay now. I never went. Not once."
    else:
        nvl clear
        "Though I'll never forgive myself."
        "I should have been a little smarter, a little angrier, a little..."
        "A little more human."
        "And not having her along on that unfortunate trip."
        "We had to postpone ticket purchases because Lena's visa was being fiddled with."
        "It seemed easier - Ryoko. She had a green light on all the countries in Europe, she'd love to go with me."
        "But somehow it seemed to me that Lena would be more appropriate there."
        "More appropriate! Jesus, you jerk. What a jerk, God..."
        nvl clear
        "That's when, sitting at the zinc box, I could have cried out and said everything I should have, but didn't have time to."
        "And how I couldn't do it without her, and how I had no idea how I was going to live, or if I should."
        "What's much worse, when I went to visit her one day at Smolenka, there was another slab beside her."
        "Tikhonova Alyona, 1993-2003, in memory from a loving sister."
        "Here we have found each other, here we have met."
        "Tikhonova Anna, 1970-2004."
        "Mother..."
        "I turned and ran from there when I realized the simple ruthless logic of numbers."
        "While I was doing nonsense, getting carried away with nonsense, Lena lost her closest people overnight, a year apart."
        "Now I understood what she might have forgotten in that medical center."
    nvl clear
    pause(3)
    "No matter how hard I tried, I could not separate my memory from that which gradually filled the emptiness."
    "Because the past was becoming too inseparable from the present me."
    "Too lucid and logical an explanation for the last ten years of sidelining myself."
    "When you should have just come to your senses and embraced the man standing in front of you."
    "The man who has put up with his whole life just to make you feel better."
    "To wipe the rotten tomatoes off his back that she's been protecting you from all her life."
    "To take his hand and say a simple 'I'm with you.'"
    "I don't know what I lacked in my time, but this is my voluntary penance, my cross."
    "So I come here every month."
    "I promised."
    "I will wait as long as it takes."
    nvl clear
    stop music fadeout 4
    $ set_mode_adv()
    pause(1)
    scene bg ext_boathouse_alt_day_7dl
    with dissolve
    play ambience ambience_lake_shore_night fadein 3
    "Standing up from the bench, I shook the snow off my head and shoulders and rolled up my headphones and tucked them into my pocket."
    "It was getting late, and I still had to walk to the bus stop."
    "It's about eleven kilometers from here to the highway, and for the umpteenth time I swore to myself that next time I'd take my bike with me."
    "But not this time..."
    "So I have my two hours on foot waiting for me."
    "I walked along the pontoons to the far side that dropped straight into the water, stood there and threw my head back to the sky, sucking in the bitter clear smell of the fading forest."
    "Winter is coming, and then it won't be so cozy here at all."
    "And the scent of autumn stabs the heart, evoking the taste of lips and the ringing of laughter."
    "With my face still thrown back to the sky, I took in more air in my chest and shouted, startling the seagulls that had landed:"
    me "Leeeeenaaaaaaaa!" with vpunch
    with fade2
    play music music_7dl["take_my_hand"] fadein 3
    un "W-why are you yelling…"
    "It cut sharply on the nerves with such an inappropriate brittle voice here."
    "And I, fearing more than anything else in the world to wake up now, slowly turned around."
    show un normal winter with dissolve
    un "You've been gone for ten months yourself, and now..."
    "She made a stern face"
    show un sorrow winter with dspr
    extend ", but, unable to stand it, she cried and took a step toward me.."
    "It really was Lena. It was her."
    "In spite of my stupid memory, in spite of everything I'd imagined, it was her."
    "Half-forgotten childhood love, half-lost adult love."
    "Still with the same hair color, but no longer dressed in a silly pioneer uniform."
    me "Lena."
    "Stupidly I repeated."
    "Strength and faith returned to my voice."
    me "Lenka!"
    "She ran toward me, stumbling, shouting something incoherent and waving her arms, sprinting at full speed while I stood and remembered how to breathe."
    "Feeling weightless, fourteen years old, as if in a dream treading on the surface of a rainbow that had descended from the sky."
    show un cry_smile winter close with dspr
    with vpunch
    "Until a whirlwind came, pushing into my chest, pressing me against it..."
    "Lena's shoulders shook."
    un "Found..."
    "She whispered frantically into my chest, choking back tears."
    un "I found you..."
    me "But where were you?"
    un "I was looking for you, I almost lost my mind when you weren't there. And you..."
    me "I promised I'd meet you on the other side, remember?"
    "I lifted her chin, kissing her lips curving into a disbelieving smile."
    "Lena pressed herself against me as hard as she could."
    un "Now I won't let go. No way!"
    me "We never had a chance not to meet."
    un "Yes. Not a chance..."
    show un smile3 winter close with dspr
    "She pulled away a little, looked into my eyes:"
    un "Come, I'll introduce you to someone very important."
    me "Someone?"
    show un smile2 winter with dspr
    un "My sister."
    scene anim prolog_2 with fade3
    "\[Lena ending unlocked - «Not a Chance!»\]"
    $ sdl_persistent_inc("us_7dl_tran_un")
    play sound sfx_7dl["aunl"]
    show acm_logo_us_7dl_tran_un with moveinright:
        pos (1600, 1020)
    pause(7.4)
    call alt_7dl_titles
    pause(2)
    return

label alt_day7_us_7dl_good:
    play music music_7dl["iamagod2"] fadein 3
    scene bg ext_winterpark_7dl with dissolve
    "But some things have changed."
    "I don't know exactly what it has to do with, but things have changed."
    "Maybe I should start with the fact that I've stopped being haunted by minor setbacks."
    "Some inexplicable stupor in situations where I used to freeze up and wait out trouble was gone."
    "What's more, I even started thinking about taking up self-education again!"
    if loki:
        "Although I won't feel any other instrument like the trumpet, some kind of surrogate consolation might be something else."
        "Like the guitar. A piano. Yes, a drum kit, after all."
        "I decided to start with the piano."
        "At my age, the learning schedule is nowhere near as brisk as when I was a kid, but I'm determined to go all the way."
    else:
        "I always wanted to learn how to draw."
        "At least at the level of simple sketches. So..."
        "But I wouldn't be me if I didn't start doing everything in one place."
        "I didn't buy a pencil and a sketchbook, I bought an expensive tablet from a Chinese manufacturer."
        "Clawed at it and scratched the plastic with my stylus for a week until the so-called 'callus' swelled up on my ring finger."
    "There were plenty of other changes."
    "But most of all, I wanted that summer back, the camp, the kids..."
    scene
    $ renpy.show("bg bus_stop", what = Dawn("bg bus_stop"))
    with diam
    "And I'm standing at the bus stop, and there's liquid longing in my headphones again."
    voice "Boy, give way."
    "There's a voice over my shoulder."
    th "What kind of a boy am I?"
    "I grumbled to myself, but I obediently stood up."
    me "Sit down."
    voice "Thank you, boy."
    th "Rrrr..."
    "And there's nothing you can do about it."
    play sound sfx_intro_bus_engine_start
    pause(3)
    play sound_loop sfx_intro_bus_engine_loop fadein 3
    $ set_mode_adv()
    scene bg intro_xx
    with dissolve
    "As they say, a little dog is a puppy all his life."
    "And until I'm fifty they'll call me a boy."
    "I'm not successful, I don't have charisma, I don't look my age, that's the result."
    with fade
    play sound sfx_intro_bus_door_open
    pause(2)
    play ambience ambience_7dl["railroad"] fadein 3
    scene bg ext_mv2_7dl
    with fade
    stop sound_loop fadeout 4
    "Once again my semi-consciousness pulls me to the train station."
    "I wish I knew why..."
    stop music fadeout 3
    "But it's better than sitting at home feeling sorry for myself anyway."
    "I stepped out into the lightroom and, with my head tilted back, began to study the map for the umpteenth time, figuring out how to get to..."
    "This is where it always hit a snag, because I couldn't name a place where the camp could be."
    "And the place by the river where the children's resting place is..."
    "It's easier to find a needle in a haystack, there are too many places like that."
    play music music_7dl["my_only_hope"] fadein 3
    scene cg d7_leaving_no_sh_7dl
    show prologue_dream
    with dissolve
    "I hadn't seen Ulyanka for a year."
    "But on some level I felt that everything that was going on there was for a reason."
    "That Ulyanka was a very special girl who could do things that others simply couldn't."
    "She managed to shake me up, managed to linger by my side - all for the sake of getting off the bus together."
    "Now I wonder if that was the bus."
    "What was the special meaning of all this?"
    "Where and why did the pioneers disappear?"
    if alt_day2_us_escape:
        scene cg d2_us_trainhop_7dl
        show prologue_dream
        with dissolve
    "But instead of answers, all I have is the feeling that I didn't get here at all because all paths eventually lead home."
    "How can you consider home a place you don't love?"
    "Much more home I thought of as this lightroom, where I would occasionally go with my smartphone and scour maps of rivers and lakes, trying to find the very bend that the railroad tracks ran past."
    "And then searched the map for a way to get there."
    "Any way you like - on foot, by train, by car..."
    "And I couldn't find it."
    "But I never gave up."
    "It's the easiest thing to cripple yourself with problems! All you have to do is put your paws down and tell yourself you can't handle it."
    scene bg ext_mv2_7dl
    with dissolve
    "But that's not what I promised Ulyanka!"
    "Get a physics student to calculate the trajectory of a rock, taking into account gravity, wind, and other factors, and it will take him half an hour to do it."
    "Throw the same stone to a kid and he'll intuitively calculate everything and easily catch the stone."
    "So I rely on intuition and my vow to never become stupid and boring."
    "And it's not just some mythical sense of responsibility and honor that helps me do that, no."
    "People, people, the very society that treats me with disdain and doesn't count me out."
    "Condescension."
    "The unwillingness to listen."
    "Plus that constant 'boy'..."
    scene
    $ renpy.show("bg ext_mv2_7dl", what = Noon("bg ext_mv2_7dl"))
    with dissolve
    "It would be fair to say that people drove me into that very childhood, and I didn't get in their way!"
    "For it is not enough to feel like a teenager. You have to be one, too."
    "And that implies stupidity and infantile thinking."
    "But what can I do about the fact that it's not a respectable gentleman looking at me from the mirror?"
    "That's right."
    "Nothing."
    "And you know what?"
    "I like it!"
    scene
    $ renpy.show("bg ext_mv2_7dl", at_list = [zenterleft], what = Dawn("bg ext_mv2_7dl"))
    show us smile sport at zenterleft
    with dissolve
    us "Hey... boy!"
    "Ulyana giggled, struggling to chew on a Twix stick and holding the other one out to me."
    us "Still trying to figure out where our camp was?"
    "Confused, I nodded and took the candy bar."
    show us laugh sport with dspr
    us "Don't look, I found it."
    "Ulyana handed me a printout of a map, suspiciously familiar."
    "It was only when I looked closely that I realized what it reminded me of."
    th "It's a map of the camp with the buildings blotted out."
    us "You like it? There's even a brig with boats on it."
    show us smile sport with dissolve
    us "True, it's been abandoned for five years, so the boats have probably all rotted away."
    me "How can that be? Where then..."
    "Ulyana shook her head."
    us "If you haven't changed your mind, let's go."
    me "But where is it...?"
    "After thinking for a while, she pulled an exact copy of my smartphone out of her pocket and delved deeper into her search."
    "After a few minutes she glowered:"
    show us surp1 sport with dspr
    us "Tver region! Now by train, then by bus."
    me "Well that's no short road."
    show us normal sport with dspr
    us "If you're afraid, we won't go."
    me "We have to find out."
    show us laugh sport with dspr
    us "We have to!"
    us "Then let's go get the tickets!"
    "She jumped up and pulled me along."
    "She who made me worry."
    "I don't know where she was for the few months I spent looking for her, but finding me at the same train station one day, she still looked the same tomboy I remembered her to be."
    "I, on the other hand, had grown a great deal younger, and now looked only a little older than she did."
    stop music fadeout 5
    "Because of the vow."
    "Because..."
    play music music_7dl["happy_ending"] fadein 3
    us "Let's go, Syomische! There aren't enough tickets!"
    scene anim prolog_2 with fade3
    "\[Good ending unlocked - «Syomische!»\]"
    $ sdl_persistent_inc("us_7dl_good")
    play sound sfx_7dl["aunl"]
    show acm_logo_us_7dl_good with moveinright:
        pos (1600, 1020)
    pause(7.4)
    call alt_7dl_titles
    if loki:
        stop music fadeout 3
        pause(3)
        play music music_7dl["beasteye"] fadein 3
        play ambience ambience_cold_wind_loop fadein 3
        scene bg ext_road_winter_7dl
        "When we got from the bus stop to the very spot where I reckoned the camp should be, there was nothing there."
        "Ulyana and I looked all over the place, searched every place - no, no, and no."
        "And how could it be in a world where no one had ever heard of Genda?"
        "Who would they put in the central square then? Lenin? Or Joseph Vissarionich?"
        "We shouldn't have gone."
        "Well, I went alone, but Ulyanka came with me for company."
        "Legend has it that I became her guardian and protector, since she was too young to even get her passport."
        "Guardian, ha."
        "Looking a little older than his kid."
        with fade
        "But what we have is what we have. We're together all the time now."
        "Like Sherocha and Masherocha."
        "Except she wouldn't get out of the car, she said, 'No way, no one's stupid enough to freeze'."
        "So this time I had to climb alone."
        "So I climbed alone through the snowdrifts and gullies, knowing full well that there was no camp here and could not be."
        "Eventually I realized that, too."
        "I sighed and headed back."
        "But I didn't make it."
        "Halfway there, I was intercepted:"
        show us smile sport with easeinleft
        us "Tudu-tu-tu! Happy Birthday!"
        "Ulyanka shouted, holding out some rectangular object to me."
        me "Wow... And I almost forgot. Thank you."
        us "Here, and remember my kindness."
        show us grin sport with dspr
        "She smiled slyly."
        "Unwrapping the wrapper and opening the case, I stared at Ulyana perplexedly."
        me "A trumpet? But why?!"
        show us shy2 sport with dspr
        "The girl stared at her feet, picking at the snow with the heel of her boot."
        us "I see how you yearn. I see it."
        us "You really need music, so I saved up a little, and here..."
        "I clutched my head and groaned:"
        me "I can't do that, don't you see? I have a trauma, I start coughing up blood right away..."
        show us smile sport with dspr
        us "That was what old you had, you fool."
        us "Don't you get it yet? Everything here works the way we want it to!"
        us "And I want you to stop being sad."
        show us laugh sport with dspr
        us "If I have to put up with your squeaking for a while, I'm ready!"
        me "I haven't practiced in a long time..."
        show us smile sport with dspr
        us "You don't have to. You're good, I really believe in you."
        me "Since you believe..."
        "I took a deep breath, anticipating an instant stabbing."
        "And it didn't take long."
        "Now mouthpiece to lips, create an air column, and curl up in pain."
        "That's the way it's always been."
        "But I don't want to upset Ulyanka."
        "So I endure the pain."
        "I do."
        "And suddenly I realize that despite the discomfort, I'm not fainting or coughing up pussy."
        "A long, lingering 'doo' sounded over the snowy plain."
        "Nervous, uncertain..."
        "And I, unconcealed and unashamed of my wet eyes, ran the gamut back and forth."
        "Whether it was pain or something else I couldn't name, it poured into my eyes, made the world shudder, and rolled down my cheeks."
        "Everything froze in a single fragile moment."
        "I took in more air in my chest, and..."
        play sound sfx_7dl["moment"] fadein 3
        "Under the whitewashed sky a half-forgotten song fluttered up, the one I've probably longed for the most all this time."
        us "Syomich, you're crying."
        me "I know."
        stop sound fadeout 3
        me "It's from happiness."
        $ alt_pause(3)
    if persistent.alt_binder:
        call alt_day7_us_7dl_good_ps
    return

label alt_day7_us_7dl_good_ps:
    $ alt_pause(1)
    show bg ext_adductius_7dl with fade3
    play music music_7dl["pixies_playing"] fadein 4
    $ alt_pause(1)
    $ meet('am', "Rookie")
    "As a little girl I thought you could become an adult in an instant."
    "You blow out the candles on the birthday cake, raise your head, and out of the mirror you see a serious woman dressed as an adult, who will cook dinner for the whole family in the morning and then hurry off to her boring job."
    "From the mirror I continue to be looked at by the same Ulyana who used to run around with the boys at camp and peel potatoes with enviable regularity as punishment for her shenanigans, but this Ulyana has eyes..."
    "...of an adult."
    play sound_loop sfx_bus_interior_moving fadein 3
    scene black
    show prologue_dream
    with dissolve
    am "Get up, kid. We've arrived."
    scene bg int_bus_people_day
    show am normal pioneer
    show unblink
    show prologue_dream
    with dissolve
    us "Ah?"
    am "Beh. Make way, I'm telling you."
    "That wasn't the Rookie."
    $ meet('am', "Major")
    us "You… you, bastard!"
    us "Where did you put him?"
    show am grin pioneer with dspr
    "Everything fell into place abruptly."
    "His lapses in memory, his changing character from year to year, his knowledge of the Old Road, which also vanished without a trace after the first shift at camp..."
    "I was looked at indifferently by the boy-major who once broke our ships."
    am "I didn't take him anywhere. They come and go, and you know that's not my doing."
    "They come and go, like trains. They linger at the station for a while before they set off again."
    "Our perpetual Rookie was indeed a rookie - or rather, even rookies. If, of course, it was correct to call every new PCR that."
    "And for some reason I felt cheated. After all, he must have gone where he wanted to go - to a world where he would never grow up."
    "But we were going there together! We made a vow!"
    show am normal pioneer with dspr
    am "And forget about the Old Road, little one. You don't need to go there, you'll be in for a world of hurt."
    hide pi with fade
    "The major climbed over my lap and walked to the exit of the bus. There was a private driver waiting for him outside the window and a long drive to the airport."
    "And all that was waiting for me was my father. Danka wasn't with him."
    th "What a fool I am!"
    stop music fadeout 5
    stop sound_loop fadeout 3
    $ alt_pause(2)
    scene black with fade3
    $ alt_pause(2)
    scene bg ext_khruschevka_rain_7dl with guess_on
    $ set_mode_nvl()
    play music music_7dl["summer_ends_soon2"] fadein 3
    "The sky was frowning for the second week, and the sun didn't even think of peeking out from behind the clouds. And the mood was the same as the sky - gray and dull."
    "Is it always like this when childhood comes to an end?"
    "At the end of summer I celebrated my fifteenth birthday. My first real birthday."
    "It never happened to Alisa, which meant only one thing: I was starting to grow up. My mother was overjoyed to buy dresses that were so far too big around my chest - just to grow out."
    "Only I didn't share her joy."
    $ set_mode_adv()
    show bg int_school_corridor_7dl with dissolve
    show dn normal pioneer at cleft with dissolve
    dn "Hi."
    "Danka always said hello to me in the school hallways, but that's where our communication with him ended."
    hide dn with dissolve
    "He no longer waited for me after school, no longer threw pebbles through my classroom window when he ran out of last period, no longer came to pick me up on Sundays to call me to play soccer."
    "It was like I was just one of many other girls who went to school. Like we didn't have a common secret, a common goal, a common mission."
    "And it made me terribly angry. It pissed me off in a strange, incomprehensible way, not at all like before."
    us "Danya!"
    "I called out to him before he opened his classroom door."
    show dn normal pioneer at center with dissolve
    "He reluctantly turned around."
    "What's wrong with him?"
    us "Shall we go to the river today?"
    "Danka shook his shaggy head."
    show dn upset pioneer with dissolve
    dn "It's going to rain this afternoon, they said on the radio this morning."
    us "And tomorrow? If it doesn't rain tomorrow, shall we go?"
    "He looked intently into my eyes."
    show dn dontlike pioneer with dissolve
    dn "Why?"
    "His answer made me feel pain - like he'd hit me. It also made me feel terribly ashamed."
    us "You can't talk about such things, they'll hear... It's our secret!"
    dn "There is no secret, Ulya. We were just playing in the camp."
    us "What a coward! You should have said right away that you were just afraid!"
    dn "I'm not afraid of anything. I just know it's all nonsense."
    dn "Get those Flares out of your head, Ulyana, we're not children anymore."
    "It's not Danka, it's someone else, terribly like him..."
    "Danka would never treat something that was so important to all of us like that!"
    us "You promised you wouldn't become an adult!"
    show dn sad pioneer with dissolve
    dn "But you were the first to break your promise."
    hide dn with dissolve
    stop music fadeout 7
    play sound sfx_close_door_campus_1
    "The door to the classroom closed behind him, and I leaned my forehead helplessly against the cold wall of the school hallway."
    "Why do all the most important people just pick up and go their separate ways, leaving me alone?"
    $ alt_pause(1)
    scene black with fade
    $ alt_pause(1)
    play music music_7dl["deep_inside"] fadein 4
    show bg ext_us_lake_7dl with touch
    play ambience ambience_forest_night fadein 1
    "The power of one Flare is not enough - they will only show the way when a whole flotilla of them is assembled. But one Flare is better than none."
    us "Melt-melt, away you left..."
    "My knees were frozen to the point where I could feel the heat in them, and my school tights were soiled in the wet sand."
    "As I finished reciting, I unclenched my stiffened fingers."
    show cg d5_un_fz_twinkles_1_7dl with dissolve
    $ alt_pause(1)
    play sound sfx_scoop_water_cup
    show cg d5_un_fz_twinkles_2_7dl with dissolve
    $ alt_pause(2)
    show bg ext_us_lake_7dl with touch
    "The boat collapsed dead weight on the water and flipped upside down. The swift current picked up its wreckage and carried it down."
    "And with it sailed my hopes of reaching the Old Road."
    "To hell with all of them, to hell!" with vpunch
    "And that guest, whose stupid love made me grow up, and Danka, who somehow thought that all this time we were just playing, and the rain, and the wind, and the wet sand, and the sunken ship..."
    us "To hell!" with vpunch
    stop music fadeout 1
    $ alt_pause(1)
    scene bg ext_us_lake_7dl at running
    play music music_7dl ["escape_2"] fadein 3
    "I jumped to my feet and raced along the shore, not even bothering to shake off the sand on my knees."
    "I can manage on my own, without them. I don't need anyone, no one!"
    play sound sfx_wind_gust
    scene bg ext_path_day at running with dissolve
    "The nasty wind crept up my collar, icy teeth digging into my neck."
    "And I felt lousy and lousy, as if nothing happy would ever happen in my life again."
    "They all betrayed me!"
    "The wet, heavy sand under my feet was flying in all directions."
    "And somewhere out there, near the school, Danka must have been carrying some girl's briefcase with long braids."
    "You're welcome, damn it!"
    show ftl_anim
    with Shake((0, 0, 0, 0), 3.0, dist=10)
    "With my eyes squeezed shut, I picked up the pace."
    "I ran well, better than anyone in the class - because Alisa was better at it than anyone else."
    "I wish I could find it! I wish I could find..."
    play sound sfx_wind_gust
    stop sound_loop
    $ day_time()
    scene bg ext_busstop_dust_7dl with blind_d
    "The wind died so suddenly that I stopped."
    "I stopped, and I gasped in amazement."
    "There was no wind, no cold, no river, no sand underfoot, and not even time in this strange place."
    "But there was an old concrete stop and an endless asphalt road, as if leading everywhere and nowhere at the same time."
    us "The Old Road…"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    $ alt_pause(3)
    return

label alt_day7_us_7dl_true:
    play music music_7dl["ask_you_out"] fadein 3
    play ambience ambience_cold_wind_loop fadein 6
    play sound_loop ambience_7dl["night_city"] fadein 6
    scene anim intro_2 with dissolve
    "The city dyes before going out in public."
    "He had mercy on me and gave me two new colors in the gray palette."
    "Red and white, white and red."
    "Freshly fallen snow and freshly shed blood."
    "Carmine lips and transparent skin."
    "White and red."
    "The city stands, squeezing out the red, opening its arms to the white."
    "The parking lights of departing cars and the white lights of incoming cars."
    "And from whichever side you look, you get your dose of white and red."
    scene anim intro_1
    with fade2
    "Red, gray, white."
    "Lines from a half-forgotten book come to mind."
    "The author must have written them when he finally got tired of the predetermination."
    "{i}…No, not everything in this raging world is ghostly, brethren.{/i}"
    "{i}From the subjects living in the houses to the facades of the houses.{/i}"
    "{i}From unbridled authors to fucked-up readers.{/i}"
    "{i}From meaningless words to dumb, wordless volumes…{/i}"
    play sound sfx_7dl["brake"] fadein 4
    "And I, moving like a badly made puppet, turned toward the growing hood of the pearly 'Goetz', squeezed my eyes shut, preparing for a collision..."
    with vpunch
    "And then my hand yanked, and it almost broke my wrist!"
    voice "Hey, assholes, have you had enough to live for?"
    "barked the driver from under the downed window."
    th "Us?"
    "That's when I noticed I was still holding someone's hand and slowly turned around."
    scene anim intro_7
    show us2 laugh2 sport
    with dissolve
    "And I gasped with happiness as I cradled the squeaking Ulyanka in my arms."
    "How did I manage to pull her along with me? No one knows."
    "But we were holding hands, and I almost broke my wrist when she hung on me with all her weight."
    "And then... This is important: I heard her reluctance to break up, I reciprocated."
    "I wanted not to break up."
    "I wanted to."
    me "Could this even happen?"
    "I didn't want to let Ulyanka go, but..."
    show us2 sad sport with dissolve
    us "Brrr, it's so cold in here."
    "She complained, hugging herself by the shoulders."
    us "Where are you drag me to?"
    me "What in the world am I... Now!"
    hide us2 with dissolve
    "Throwing off my coat, I immediately wrapped the chilly girl up."
    "I had a T-shirt, I had a sweater - some time I could hold out."
    "Unlike her, dressed in nothing but a thin Union T-shirt."
    scene anim intro_3
    with dissolve
    "After warming up a bit, she looked around her surroundings with eager curiosity."
    us "Are we in your world?"
    me "Practically."
    play sound sfx_7dl["car_passing"]
    "It was only a five-minute walk from here to my den."
    "Maybe if it had been a little farther away, I never would have made it outside in my life."
    "And this stupid, random story wouldn't have happened."
    "Which ends in this strange way."
    us "Then take me home."
    stop music fadeout 3
    "The girl jumped up on the spot, yanked my sleeve:"
    us "Come on!"
    stop ambience fadeout 6
    stop sound_loop fadeout 5
    scene bg int_sam_house_clean_7dl
    with dissolve
    play ambience sfx_street_traffic_outside fadein 2
    play music music_7dl["thousand_little_things"] fadein 3
    "We dropped our shoes and coat at the entrance, after which I immediately sent Ulyanka into the shower."
    "You know... I didn't want her to catch a cold."
    "Now there were a number of small and not-so-small matters to be resolved."
    "I didn't need anything myself; if I'd been here all by myself, I wouldn't have had to change anything at all."
    "But - the child needed winter clothes, winter shoes."
    "Feeding her dumplings alone was no good, either."
    "And that's assuming we don't have to figure out what to do with her at all."
    "What if she's got mommies-daddies with shotguns here, too?"
    "Although..."
    me "Little one, what's the last thing you remember before we were in the driveway?"
    "I shouted as the noise of the water died down."
    us "The bus, what else?{w} Syomich, you didn't forget did you?.."
    "It came back from the bathroom, and she appeared to me in the same sports uniform."
    show us2 smile sport with dissolve
    us "So this is how you live..."
    "She looked thoughtfully at the dusty chandelier, the bunches of peeling and curling wallpaper..."
    me "I live, as you see."
    show us2 sad sport with dspr
    us "This is no good. Some bachelor's place."
    me "It is!"
    "I put my hand to an empty head - say, that's where we stand!"
    us "It needs a woman's hand here."
    me "Don't be ridiculous, woman."
    show us2 grin sport with move
    us "Yes. A woman."
    "Ulyanka showed her tongue."
    "White and red: scarlet T-shirt, scarlet hair - and the silvery moonlight from the moon peeking through the window."
    us "Get used to the idea that there's a woman in your li..."
    play sound sfx_stomach_growl
    show us2 sad sport with dissolve
    us "Listen, do you have anything to eat? I'm starving!"
    "She groaned pitifully."
    "I laughed and reached for the phone, remembering the pizza and sushi delivery address as I went."
    with fade
    show us2 surp1 sport with dissolve
    us "Are you sure it's edible?"
    "The delivery arrived with an hour's delay, as is to be expected on New Year's Eve."
    "We waited for it, drinking tea and occasionally knocking off each other's last packet of dumplings."
    "So we greeted the square boxes far without the enthusiasm that sounded in our voices when I hung up the phone and informed that food was coming."
    show us2 smile sport with dspr
    "Ulyana picked up the spotted roll with a fork and poked it with her finger doubtfully."
    me "It's delicious, try it yourself."
    if alt_day_binder != 1:
        us "It looks more suspicious than that bug in your plate."
        me "W-what bug?!"
        show us2 laugh sport with dspr
        us "The one I planted for you at camp!"
        "Now I actually remembered some variety in my diet, but I decided to control it just in case, so there would be no surprises."
        "Ulyana watched me and laughed every time I suspiciously examined a roll or a slice of pizza."
        "She only dared to eat one herself, binging on the floury stuff."
        "All the Japanese food went into my stomach."
    show us2 smile sport with dspr
    us "Delicious."
    "She smiled."
    us "And now, as a woman, I declare: you sleep on the floor."
    me "Why should I?"
    us "Because that's why! That's what I said."
    me "So I found an oppressor on my neck. But my misfortunes were just beginning."
    show us2 laugh2 sport with dspr
    us "That's right!"
    hide us with dissolve
    "I just waved my hand and went to wash up."
    "There must be a foam pillow and a spare blanket somewhere in the storeroom."
    "And if I'm lucky, a cot, too."
    stop music fadeout 6
    scene anim prolog_15
    with diam
    "And in the morning they woke up."
    "When I opened my eyes, I stared at the ceiling for a long time, trying to figure out why the angle was so strange."
    "It was as if he had grown taller."
    th "Must have fallen off the couch in the night."
    scene anim prolog_4
    with dissolve
    "And then I remembered everything."
    play sound sfx_7dl["reverse_bell"]
    "But there was no one in the spread and crumpled bed."
    "Nobody!"
    "I almost went gray with horror."
    th "Was it all a dream?"
    me "Ulyanaaaa!"
    us "Don't scream, Syomische!"
    "Was heard from the kitchen."
    us "I almost knocked the cup over myself!"
    th "Phew..."
    "I exhaled."
    us "I found some unwanted loafs at your place, and there's this pizza of yours left over from yesterday."
    us "Come on up, let's have breakfast."
    stop sound_loop fadeout 6
    scene bg int_semen_room_window_day_7dl
    with fulldiam
    $ set_mode_nvl()
    play music music_7dl["sh_ai_rejuv"] fadein 3
    "Two weeks have passed since then."
    "The computer moved away from the window, because there are very comfortable, wide window sills, on which one pesky girl with a cup of tea could fit admirably."
    "And Ulyanka liked to sit there, and I, moving to the far corner, worked, glancing sideways at the way the silver moonlight shaded her fiery red hair advantageously."
    "The window froze, covered in winter patterns, white and red lay in whimsical patches on the ceiling of my apartment."
    "I mean, already ours."
    "Ours."
    "I teased Ulyanka and her serious attitude about everything, still seeing her as a simple tomboy."
    "Short, infantile..."
    "Only I was infantile myself, and the height..."
    nvl clear
    pause(3)
    "Well, she was short, but I've known some who were only slightly taller than my friend."
    "Older, grown-up moms with kids and husbands and established tastes."
    "I had a short mother too, which didn't stop me from growing to 185 centimeters."
    "What's more, Ulyana, with a truly feminine perfectionism, took over my place, cleaned out all the junk, repapered the wallpaper..."
    "Before I knew it, I was almost a married man."
    "Although, of course, it was wild living in the same apartment as a teenager. Basically nonexistent."
    "No, she got to know the whole building by calling me her guardian, but that didn't change the point."
    "She was a girl from the land of fairy tales, in a world where fairy tales have no place."
    "Except she had a very different opinion."
    nvl clear
    pause(3)
    "She believed that anything in life is possible, you just have to want it and try."
    "You have to try hard enough."
    "And I didn't have the heart to put her down and pry into her pure soul with my homegrown cynicism."
    "The only thing I could do was to believe in her, and to legalize her little by little in society."
    "I've applied for a residency, it'll be considered for a couple of weeks, so I don't have to worry - just wait."
    "That's what I told her when I got home."
    "And she, without turning away from the window, put a cup on the windowsill and nodded."
    nvl clear
    pause(3)
    $ set_mode_adv()
    me "Is everything okay?"
    "I cautiously approached her from behind, preparing to either recoil or hug her."
    show us2 normal dress with dspr
    "And she turned around."
    us "Syomich, we need to talk."
    "Usually all trouble starts with this phrase."
    "So I braced myself for trouble and cautiously clarified:"
    me "About what?"
    us "Can you tell me about how you ended up in the camp?"
    me "Um... Why do you need to know that?"
    show us2 sad dress with dspr
    us "Syomich, just tell me, okay?"
    "The memories came flooding back to me, I had to take a deep breath and calm down for a few seconds."
    "The feeling of fear, of helplessness, that had been painstakingly pushed inside, came back into my mind."
    "For a second it even felt like I was there again - in a ruthless, icy death."
    me "It's hard."
    show us2 normal dress with dspr
    us "I'm sorry. But I really need to know."
    me "Why?!"
    us "Trust me. Just tell me..."
    me "Okay."
    "After going to the kitchen and clapping a hot drink to keep my hands from shaking, I sat down on the bed and began:"
    me "The thing is, I ended up in camp as a result of an accident."
    show us2 surp1 dress with dspr
    us "What was so unfortunate about camp?"
    me "Not camp, but... Long story short, before I woke up on the bus, I died."
    show us2 fear dress with dspr
    us "What do you mean, you died?"
    me "Quietly."
    us "Maybe you were dreaming?"
    if loki:
        me "There were four of them, extremely angry, wearing heavy boots and killing on purpose."
        me "They had their reasons."
        me "Moreover, I even believe they had their own right."
        show us2 normal dress with dspr
        us "They just beat you like that?"
        me "No, it's a much longer story. But all you need to know is that when they finished their job, they left an unviable piece of meat in the snow, incapable of further existence."
        me "Add to that the thirty-degree frost, and you get the answer to the question of whether I could have dreamed that."
        me "I've been in this company once before."
        me "There's no mistaking that feeling."
    else:
        me "You know, when water pours into your lungs, it's a sensation you can't mistake."
        me "And even more so when you see it in your dreams."
        us "So what happened?"
        me "Nothing much, really."
        me "I got on the bus, we drove out on the bridge, we skidded on the ice and spit."
        me "I don't know if many people survived, but the last thing I remember is running out of air and reflexively taking a breath."
        me "Water pours down my throat. That's it."
    us "And then?"
    me "You see... I've been dreaming about this strange girl all my life."
    show us2 smile dress with dspr
    us "Go on."
    me "About your height, a brown-haired girl in a short red dress."
    me "Every time she appeared in a new set, she held out her hand to me and asked me if I would go with her."
    us "And you...?"
    me "I refused. For some reason it seemed to me that if I went, there would be no going back."
    me "And that's very scary. Nobody wants to die, even like that."
    us "This time, you took it, you didn't refuse?"
    me "No. There was no point in refusing - all the strings were cut."
    me "I took her hand, and we went."
    me "I woke up on the bus."
    me "Happy now?"
    show us2 sad dress with dspr
    us "It all adds up."
    "Ulyana muttered thoughtfully."
    me "What does?"
    us "I know who you are! You're a PCR."
    me "PCR? What's that?"
    show us2 smile dress with dspr
    us "A settler."
    me "I don't understand anything."
    us "You are a temporarily freed soul, a spirit, a consciousness, if you will."
    us "You can find a person willing to accept you and stay there for a while."
    us "I don't know how it works, but you must be similar."
    us "That's why you and that Syomich from camp look like twin brothers."
    show us2 laugh dress with dspr
    us "Only that one is younger and my type."
    me "And me?"
    show us2 laugh dress with dspr
    us "And you're an old fart."
    "She laughed."
    me "Thank you. It's a pleasure."
    show us2 smile dress with dspr
    us "Don't pout."
    "She sat down next to me on the couch and poked me in the side with her fist."
    us "You're a very nice man, too."
    me "It's all such nonsense that you have to believe it."
    us "We've already learned how to find people like you, even use them."
    us "But we haven't learned how to cure them."
    me "Good. What about you, then?"
    me "And if we're back home, why am I alive and talking to you now?"
    us "That's the thing, Syomich."
    show us2 normal dress with dspr
    "Ulyana stopped smiling and looked genuinely serious."
    us "We're not at your home now. And we can't go back."
    stop music fadeout 5
    us "And as for me..."
    "She shook her head."
    scene bg int_sam_room_7dl
    show us2 normal dress
    with dissolve
    play music music_7dl["out_of_your_tier"] fadein 3
    us "It's not that easy with me, Syomych."
    me "Yes, it's not easy - you're not at home, you can't go back, and you and your mysteries..."
    show us2 sad dress with dspr
    us "Be quiet and listen, okay?"
    "Quietly the little woman asked, and I shut up."
    "Ulyana, on the other hand, hesitated, sat down on the far corner of the couch, put her feet under her."
    "For a few seconds she wondered where to begin, and then she began again."
    us "I knew the secret of our camp. {w}I knew the secret of the old camp."
    us "Just because I've been to both."
    me "But wasn't the old camp closed 15 years ago?"
    us "Closed."
    "Reluctantly she nodded, shaking her tails."
    us "Partially because of me."
    me "Fifteen years ago you were not even in the draft..."
    us "Nevertheless."
    "She looked sternly into my eyes."
    us "Those like me are called «erased», Semyon."
    me "Erased?"
    us "People who have had their identities completely erased."
    me "And why would one be subjected to such a thing? You didn't kill anyone, did you?"
    show us2 smile dress with dspr
    us "Only myself."
    "Bitterly grinned the girl."
    show us2 sad dress with dspr
    us "Chronologically, I'm not the 14 I look like."
    us "But biologically, and mentally..."
    me "You sound like an adult."
    "I pointed out."
    us "Right. It's a fact that makes you have to grow up."
    us "You realize that you are not the first owner of your body, that you were not made this way by mom and dad, but by social educators."
    us "A side effect..."
    "She yanked her tail with displeasure."
    us "A complete lack of change. I can't even get a haircut, as everything is restored as it was, in a week."
    us "I don't get sick, I don't grow up, I don't change..."
    me "So that's practically immortality!"
    "I exclaimed."
    us "If only. I don't mind prolonged childhood, but childhood is eternal..."
    us "Besides, I'm going to start changing soon. Grow."
    us "Another week or two and it'll start."
    me "So you don't know why the first one was erased?"
    "For some reason it seemed as if that question might somehow hurt Ulyanka."
    us "I wondered, of course. You'd have to be an idiot not to guess."
    us "I had a document there, at home. It's called «secondary birth certificate», so it wasn't long it was a mystery to me who I was."
    scene bg ext_railbridge_sunset_7dl
    with fade
    $ set_mode_nvl()
    "Then I started digging."
    "I needed reasons, I needed an understanding of what was going on, why and how."
    "My father was silent, burned the family archives, trying to keep me safe."
    "Protect."
    "But even servicemen have a heart, there are things you simply can't get your hand on."
    "On a picture of a family of five, a father and mother and three children."
    "The girl looks a lot like me, though, with the name 'Alisa' on the caption."
    "And the older brother looks a lot like father."
    "Strange, very strange."
    nvl clear
    pause(3)
    "He didn't burn a yellowed letter from Afghanistan."
    "And a funeral letter from the same place."
    "It turned out to be dull and simple, it was enough just to compare the dates."
    "My 'secondary certificate' and the funeral letter that came in."
    "My father wasn't my father and my grandfather wasn't my grandfather."
    "It's all mixed up, a generation apart."
    "And finding out how the erasure happened wasn't a problem at all."
    "I did well in school, Syomich."
    "I know very well the biography of our General Secretary."
    "So there's no shame in being erased, no shame at all."
    with fade
    "Grandpa didn't want to let me go to camp, we fought about it for a long time. That's the kind of man he is, always standing his ground."
    "He must have remembered very well what it was like back then."
    "But a kid has to socialize, right?"
    stop music fadeout 5
    "That's how I ended up in «Sovyonok» four years ago."
    "And a year later I met Olga."
    nvl clear
    $ set_mode_adv()
    scene bg int_sam_room_7dl
    show us2 normal dress
    with dissolve
    play music music_7dl["pixies_playing"] fadein 3
    us "And her subordinate, a certain pioneer Persunov."
    me "Okay, stop."
    "All these revelations made my head spin."
    me "But I only went to camp this year!"
    me "Can you die three times and not remember it?"
    us "That's right. You only got in this year, and before that there was... What was."
    me "So that Semyon that was there, he's like a passing yard or a train station?"
    us "Looks like it."
    us "Only we witnessed it."
    me "Like someone... ahem... possessed him?"
    show us2 sad dress with dspr
    "Ulyana nodded."
    us "When he arrived, he was just a boy-major, rich parents, imported jeans..."
    us "Said strange things, believed that the dollar would save mankind."
    us "Didn't give a damn about anybody else's authority."
    me "That doesn't sound like me."
    "I mumbled."
    us "And it wasn't you. I don't think you'd mock a squad leader's assistant for launching boats with the little ones."
    us "I don't think you would have fist-bumped him when he threw you off trying to trample those very ships."
    us "But he did. And Mirya beat him up pretty good."
    me "How angry."
    us "Very angry. He took offense at that, too, and ran off into the woods for two days."
    us "They looked for him, of course. They didn't find him."
    me "Did he come back on his own?"
    us "And it wasn't him at all anymore."
    us "It was a man who recognizes no one, and his memories are alien, alien..."
    with fade
    us "He didn't try to break anyone else's ships anymore, but instead began to cut his own."
    us "And he was doing fine, except that the ships were going somewhere no one could find them."
    me "Flares?"
    us "Yeah. We started asking him why and how and what, and he kept talking about some kind of ritual, about a search."
    us "About the Old Road."
    us "And one day he got all the people who liked to be on the beach together and told them about how they had to launch ships to find something."
    us "Told them that there were so many worlds, and they were all united by the Old Road."
    us "He knew how to use it, for he came from a place where this road became part of folklore, it was learned to be used..."
    us "One condition only."
    us "The way out on the road is open only to children. Only they are capable of intuitively making the right choices and taking the right steps."
    with fade
    show us2 smile dress with dissolve
    us "This year I wanted to go on the road, but I met you again."
    show us2 shy dress with dspr
    us "And you weren't interested in all that anymore."
    us "You've become too old."
    show us2 shy2 dress with dspr
    us "And so did I, it seems."
    me "So why did you need all this in the first place? Is this such a game?"
    show us2 dontlike dress with dspr
    us "You're the game!"
    show us2 normal dress with dspr
    us "It's important for me to figure out what the first me wished for."
    us "Whether she succeeded.{w} And I'm not ready to die or kill you just to check."
    us "And it won't work.{w} I'll just temporarily replace someone in one of the worlds that has my likeness."
    us "And that's only if I'm lucky. I'm not a PCR, Syomych. I'm erased."
    me "Yeah..."
    "I scratched the back of my head as I listened to all this nonsense."
    me "So what do we do now?"
    show us2 normal dress with dspr
    us "I don't know, Syomych. I wish you wouldn't go anywhere."
    us "But... I have a wish, and you can help me make it happen."
    me "Wave my wand and yell 'sim salabim'?"
    "I joked. It came out sluggish and inexpressive."
    "That's what Ulyana told me when she slammed her fist into my head."
    us "You should be able to. You know how. You may not remember, but it all happened to you."
    us "Try to remember. If you can, you can help me."
    us "If you don't..."
    stop music fadeout 5
    "She sighed."
    us "Well, I was going to stay with you anyway..."
    scene bg semen_room_window
    with dissolve
    play music music_7dl["lullaby2"] fadein 3
    "The evening passed harshly and silently."
    "I listened to music on my headphones and couldn't bring myself to take the girl's words seriously."
    "And she ran around the house with a mop again, cooked something relatively edible, and fed me dinner."
    "She ended up climbing on the windowsill again with her feet up and looking outside."
    "What did she see out there? People and cars and houses?"
    "For some reason I doubted it."
    "And for some reason I really wanted to help her."
    "Even though I didn't know how."
    scene anim intro_15
    with dissolve
    "Closing my eyes, I saw summer again."
    "I looked into summer."
    "I wished it was all back, that we could run around camp again, get a scolding from the squad leader and feel this life as our own."
    "That there wouldn't be frost, that there wouldn't be people who didn't care about everyone around them."
    "To have one little girl get her stupid and illogical wish, which only little girls have."
    "And I didn't know how to help her."
    "Somehow I believed her unconditionally, even though her tales were fantastical."
    "It wasn't that I didn't mean to offend or anything."
    "No. It's just that the most fantastic thing has already happened."
    "I inexplicably ended up there, the same fantastic way I managed to drag the girl down with me."
    th "How she disrespected the one who was the very first, the healthiest. The boy-major."
    "And how now she hugs my neck and smiles when my stubble tickles her nose."
    "A lot has changed, a lot."
    "And me, too."
    "From the moment I didn't push Ulyana away, I'm responsible for her."
    "I have to keep her safe and protect her. From everything."
    "Including the injustice of this life. And if a child believes in a fairy tale, my first duty is to provide her with that fairy tale."
    "Even if it's all nonsense."
    "Nonsense."
    "The little palm in my hand responded weakly to the shake-Ulyana thought too, but little by little she fell asleep."
    "And I wished with all my might that we could have something."
    "Even if I have to go through this nightmare all over again to do it."
    stop music fadeout 5
    stop ambience fadeout 6
    th "I guess I'll have to go back to camp, and there, according to Mirya's and myself's precepts, start launching those ships?"
    "I relaxed, recalling the sensations that preceded my awakening in the red-hot Icarus, exhaled, and..."
    $ persistent.sprite_time = "day"
    $ day_time()
    play sound sfx_7dl["intro_dr"] fadein 6
    scene bg ext_railbridge_sunset_7dl
    show uv dontlike
    with dissolve
    play music music_7dl["escape_2"] fadein 3
    "The picture before my eyes changed, and a certain extremely angry person appeared to me."
    uv "Would you look at these stupid idiots!"
    "The girl exclaimed, pressing her ears to her head."
    uv "You do everything for them, everything! If they need warmth - here! If they need love, no problem!"
    uv "Kiss and breed, what more do you want?"
    uv "No, let's die! Let's get hurt and fuck up everything we've accomplished!"
    show uv dontlike at right
    show us2 dontlike dress at zenterleft
    with move
    us "Who are you anyway, lady?"
    "Only now did I notice that I was still clutching Ulyana's palm in my hand."
    "And so I wasn't at all surprised to see her around."
    show uv rage with dspr
    uv "And you have the gall to ask? You ungrateful, little shit!"
    uv "That's right they say, don't do good - you won't get evil! If I would see you off one more time..."
    me "But we really don't know who you are!"
    "I resented it."
    me "I was going to bed, thinking... About things. And here you are. And you're screaming."
    show us2 smile dress with dspr
    us "Angry cat!"
    show uv surprise2 with dspr
    uv "So you don't know or remember anything?"
    me "Don't remember what?"
    show uv surprise with dspr
    uv "And then how did you end up here?"
    "Ulyana and I looked at each other."
    show us2 normal dress with dspr
    us "Auntie, where did you get the cat ears?"
    show uv shocked with dspr
    uv "Get off my ears!"
    "The girl turned to me."
    show uv normal with dspr
    uv "Can you tell me, you two imbeciles, for what reason did you need to go back to camp for?"
    uv "You've already been given both hands of happiness, what more do you want?"
    show us2 sad dress with dspr
    us "Syomich, who is that?"
    me "I don't know. But she seems to know us."
    show uv smile with dspr
    uv "And extremely well at that! So are you going to tell me or are you going to wake up?"
    "I pinched myself."
    me "Ow!" with flash_red
    me "But we're not sleeping!"
    show uv laugh with dspr
    uv "Not quite asleep, but if you keep being retarded, you'll wake up where you fell asleep."
    me "And she's laughing too..."
    show uv normal with dspr
    uv "I repeat the question for the third time: why did you need to go back to camp?"
    show us2 calml dress with dspr
    "Ulyana looked at me again, and I nodded."
    "She didn't like it very much, nevertheless, she chimed in:"
    us "There's a dock there from which..."
    show uv grin with dspr
    uv "Yes, I've heard about these schizoid ramblings of yours. But what does this have to do with camp?"
    show us2 surp3 dress with dspr
    us "What do you mean?! The Flares can only be launched from there!"
    show uv laugh with dspr
    uv "You really are idiots. The flares can be launched from anywhere."
    show us2 dontlike dress with dspr
    us "Lady, stop calling me names! I tried launching it, it didn't work!"
    uv "You didn't try hard enough! You've got to try harder."
    me "Okay, you got what you wanted from us, now it's your turn to answer the questions."
    show uv guilty with dspr
    uv "Not yet, Syomische. It's still early."
    us "But that's not fair!"
    show uv smile with dspr
    "The girl immediately shook herself up, shed her bad mood, and sparkled her eyes mischievously again:"
    uv "Life in general is a complicated thing. Get used to it."
    uv "But I understand correctly that you two morons are going to die to get back to camp?"
    show us2 shy dress with dspr
    "We looked away in sync."
    uv "All for some stupid rituals?"
    uv "Flares?"
    me "We need to."
    uv "What you need to is to get out on the Old Road."
    "The girl cut off."
    uv "And you don't have to do any nonsense at all to do that, like the one you have in mind."
    uv "If you can go straight to the Road."
    show us2 normal dress with dspr
    us "Syomich, can I strangle her?"
    me "I'm struggling with the same urge myself."
    show uv shocked with dspr
    uv "What a touching unanimity. You can tell you're an established couple."
    uv "But, Syomische, isn't she a little small for you?"
    show us2 angry dress with dspr
    us "{b}KILL!{/b}"
    "Shouted Ulyanka, lunging at the cat-eared woman."
    show uv laugh far with move
    uv "Hands off! Catch!"
    "She bounced a good meter away from us all at once."
    hide uv with easeoutleft
    us "Syomich, she's mine!"
    hide us2 with easeoutleft
    "Ulyanka ran after the girl as fast as she could."
    "And I had no choice but to run after them."
    with dissolve
    "And so, with laughter and jokes, we ran along the railroad tracks, not paying attention to the way the light around us turns gray and yellow, the way the vegetation descends little by little to a complete absence..."
    "At one point the girl with the ears turned away from the tracks and rushed somewhere into a clear field."
    "Ulyanka ran after her, waving her fists and inarticulate shouting something."
    "And my side was starting to sting."
    "Only our mocker didn't seem to be tired at all."
    stop music fadeout 3
    "Ran and laughed and shouted some hurtful things."
    scene bg ext_busstop_dust_7dl
    with dissolve
    play music music_7dl["thousand_of_pixies"] fadein 3
    "And then she disappeared altogether."
    "It was as if she hadn't existed."
    "Ulyana ran on inertia for a few meters, then realized that there was essentially no one to chase."
    "She stopped and turned to me."
    show us2 dontlike dress with dspr
    us "Well, where did that bastard go?"
    "She looked angry and disgruntled."
    me "I don't know..."
    "I snorted."
    me "I didn't see."
    us "Too bad. Ugh, I would have her!"
    "She expected me to back her up, but I just shook my head."
    "The girl was clearly tougher and stronger than Ulyana, even with all the nonsense the latter had told me tonight."
    th "Tonight."
    me "Save your fantasies for later. Right now it's more important to figure out where we're going and how to get out of here."
    $ persistent.sprite_time = "night"
    $ night_time()
    scene
    $ renpy.show("bg ext_busstop_dust_7dl", what = Notch("bg ext_busstop_dust_7dl"))
    with dissolve
    show us2 smile dress with dspr
    us "Syomich, do you know where we are?"
    me "Where?"
    show us2 laugh dress with dspr
    us "You're a retard, Syomich! I told you so! And so did that wench."
    me "I didn't understand anything."
    "Honestly, I confessed."
    us "We're on the Old Road, Syomich! Okay?!"
    us "It's just as he described: a broken highway, a concrete stop."
    me "Great. And?"
    us "Look!"
    "Ulyana turned my head toward the highway."
    scene cg d7_bus_night_7dl
    with dissolve
    "On the broken asphalt, a painfully familiar red-bellied «LiAZ» was climbing toward us."
    "And even from here you could easily make out the number: 410."
    "Ulyana pulled me along."
    us "Let's run! Or they'll leave without us!"
    "And we ran."
    "It occurred to me that Ulyana should probably thank the stranger for simply taking us out on the road."
    "For giving us a chance to do things the right way, without taking any unnecessary risks..."
    "Here's to another escape for me and her."
    scene
    $ renpy.show("bg ext_road_day", what = Desat1("bg ext_road_day"))
    with dissolve
    play ambience ambience_ext_road_day fadein 3
    "Ulyana was not mistaken."
    "That mean-spoken and intemperate girl did indeed do for us what we could not have done for ourselves."
    "She led two people to the Old Road. A place I'm not really allowed to go."
    "Nor, strictly speaking, is Ulyana."
    "But that's according to that same Ulyana's confused explanations."
    "Somehow I thought it was more complicated than that."
    "But the bus that picked us up in the night had already thrown us out in the morning."
    $ persistent.sprite_time = "day"
    $ day_time()
    play sound sfx_7dl["footsteps_grass"]
    scene bg ext_road_day
    with touch
    "And we go, holding hands, going back to where it all began."
    "But only here it's different, it's not like that at all."
    "There was no concrete patch, no walls, no gates..."
    "There was no camp at all!"
    show us2 sad dress with dspr
    us "It doesn't work like that."
    "Ulyana whispered, taking me with her to the barely visible path that led into the woods."
    us "It can't be."
    "I glanced at my watch in passing - the date was off again."
    "The signal wasn't picking up again. It's the same as always."
    me "Will you tell me where you're taking me?"
    show us2 normal dress with dspr
    us "Please, Syomich! It's very important!"
    "Well, if it's important..."
    scene bg ext_old_building_day_7dl
    show prologue_dream
    with fade
    "We reached the old camp forty minutes later."
    "Or rather, it was the old camp to her and me."
    "And here it was the only one."
    "The place where the tents are stretched out, the kids are buzzing on the merry-go-rounds, and one red-haired little girl is hugging her brother by the neck..."
    play sound sfx_7dl["footsteps_grass"]
    us "Shhhh."
    "Ulyana takes a step back without turning around and makes way for me."
    us "Don't. I understand everything now, I've seen everything."
    me "But..."
    "When the girl turned to me, I froze as if struck by thunder."
    "There was happiness in her eyes."
    "There were tears in her eyes."
    "She hugged me as hard as she could and whispered."
    us "Thank you."
    scene bg ext_road_day
    show us2 sad dress
    with dissolve
    pause(2)
    hide us2
    show us normal grow_dress
    with dissolve2
    "By the time we got out on the road, Ulyana had already changed a little."
    "Her shoulders straightened, her posture straightened."
    "Her facial features had become finer and more graceful."
    "Now she looked more like a teenager than that splinter."
    me "You cheated. And you promised not to grow up."
    us "So did you."
    "Ulyanka parried."
    us "Oathbreaker."
    show us laugh grow_dress with dspr
    "We looked at each other for a long time, and then we laughed."
    scene anim prolog_2 with fade3
    "\[True ending unlocked - «It Can't Be»\]"
    $ sdl_persistent_inc("us_7dl_true")
    play sound sfx_7dl["aunl"]
    show acm_logo_us_7dl_true with moveinright:
        pos (1600, 1020)
    pause(7.4)
    call alt_7dl_titles
    pause(2)
    return

label alt_day7_us_7dl_bad:
    scene bg int_sam_room_7dl with dissolve
    play music music_7dl["misery"] fadein 3
    "The bell trilled down the street as I, smiling stupidly, waited for something to click and a child's voice to ask: 'Who's there?'"
    "I smiled and answered, 'Open up, owl! The bear is here'!"
    "There he is."
    "With difficulty coming to my senses, I shook my head, driving away the intrusive obsession."
    scene bg int_access_day_7dl
    with fade
    "I almost met again today."
    "I almost agreed to deceive myself once and to be deceived again."
    "I ran screaming 'Ulyanka!' so much that passersby turned around and twiddled their thumbs."
    "And I didn't care."
    "It seemed like if I caught up with you now, grabbed your hand, everything would be all right."
    "It will be, won't it?"
    "Of course it will."
    "There's a reason I've been running around all year, looking and waiting."
    "I don't believe it was all for nothing."
    with fade2
    "Sometimes I get discouraged, I want to sit on the floor and distinctly hate everything around me."
    "The people, their unique stories, their unique inner universes."
    "Except I can't afford it."
    "Because one day you might get hit - I'll never forgive myself for that."
    if loki:
        "I've been taught too well by life once; I know all too well what it is to be the object of hate."
        "That's why I've forbidden once and for all to treat anyone badly."
        "Just because I remember all too well the gut-wrenching feeling of someone praying at your picture, 'Die, please.'"
    else:
        "I let myself do something like that once before - I was a fool, young, stupid."
        "And it ended so badly that I swore I'd never do it again."
        "It's too destructive a weapon, to punish with it is like cutting off heads for pranks."
    with fade
    "And on the whole, nothing has changed in life."
    "The world has changed, the rules have changed."
    "Except I'm still the same. You know, the same..."
    "For some time now I realized that the camp as I remembered it could only be perceived by the enthusiastic consciousness of the creator."
    "That only in the process of creating it could all the bad things be completely cut out, which still cannot be eradicated, no matter how communism is poured around it."
    "So I took a close look at everything I could remember - just for the sake of not repeating it again."
    with fade2
    "Such a sobering remedy for reverie."
    "Take one capsule three times a day, with plenty of bitterness and self-deprecation."
    "Combine with reason and logic is strictly forbidden."
    "Otherwise the question automatically arises:"
    me "Couldn't I have invented... Even you?"
    "And I'm afraid to even think such a thing."
    "Because it automatically means that since there's nothing, since you don't exist, I'm not needed."
    "It's like you're not real, coming out of concrete boxes with unhealed stigmata, unrelenting anger."
    "True, the shrugging people on the street still attest to what I am."
    "Or are they shoving me just because they point-blank don't notice?"
    "An aura of failure? The emptiness in the gaze?"
    "I've worn my body like an unwanted old sweater, just waiting for an opportunity to shed it and change into someone who at least knows you."
    "Highly reactive, funny and smarmy, causing reciprocal sparks of interest in your eyes."
    "But where would I find such a 'someone'?"
    "Somehow I didn't doubt that I - really couldn't be interesting."
    "And instead of doing something about myself, to change somehow, I went on and on, winding my circles around St. Petersburg."
    "In a year, I'd gone the distance of perhaps the equator and not even found a trace."
    "This only made me angrier at myself, more and more hated myself, my body."
    scene
    $ renpy.show("bg ext_winterpark_7dl", what = Dawn("bg ext_winterpark_7dl"))
    with fade2
    "I left another bleak evening behind me and went outside, listening to the liquid melancholy in my headphones, involuntarily fingering the tonal line of songs."
    "And, of course, feeling sorry and hating myself again."
    "Frost and sunshine... Horrible day."
    $ alt_pause(1)
    scene bg int_metrostation_7dl with dissolve2
    "Once in the subway, I stared at the map for a long time, then squinted and poked at the first station I could find."
    if loki:
        "Of course, it turned out to be Krestovsky Island."
        "A wonderful station with so many warm and happy memories."
        "Despite the fact that the four were caught, tried and sent to prison."
        "From then on, the Park of Culture and Leisure awoke in me very negative associations."
        "I never would have dared to go there of my own volition."
        "There was still too much tugging of the edge of death's wing."
        "I didn't rejoice in the trial, I wasn't afraid of their evil looks."
        "I didn't care."
        "It was just that this story had to end one way or another."
        "Besides, I was on painkillers all the time, so my consciousness was a bit floaty."
        "Now that the novocaine blockade has been lifted, I'm fully aware of my surroundings."
        "And I really didn't like the idea of going there."
        "That's why I decided to try it."
    else:
        "The Old Village. There used to be a park there, I think."
        "Not bad. You can wander the trails, imagine that there aren't many people around, that it's just the woods around the camp are snowed in since New Year's Eve is upon us."
    scene
    $ renpy.show("bg ext_winterpark_7dl", what = Dawn("bg ext_winterpark_7dl"))
    with fade3
    "I couldn't understand why people around me were happy, why they smiled when you weren't there."
    "How dare they...?"
    "How do they..."
    "I threw my head back toward the sky, a patchwork of branches peering between them, accusing fingers poking me right in the eye."
    "Three hundred years could pass here and nothing would change."
    "Time converged at one point, and one could step from here to anywhere."
    "Even back to where we were together."
    "It just won't be my December 28th, but yours."
    "Now, after all this time, you can stop fooling around and say to yourself,"
    me "Yes."
    "I whispered with dry lips."
    me "Even though in my own way, I loved you. {w}And I miss you very much."
    me "Very much."
    "A familiar laugh echoed between the trees, the footsteps of bare feet on the pavement were heard for a split second..."
    "The park swirled around me and hit my temple."
    scene black
    with fade
    stop music fadeout 3
    "My body, my old sweater responded to my dislike."
    "In full reciprocity."
    "Only not with a sore back and legs, but..."
    play music music_7dl["unfinished_life"] fadein 3
    "The bus raced through the night, carrying a dozen of the planet's future greatest men, but for now, just simple pioneers."
    "And me."
    "A rogue, an impostor, a man who had joined a stranger, and for that he was now receiving."
    "When I woke up on the hospital sheets, it was a week later, New Year's Eve had passed, and I hadn't met anyone."
    "And everything just turned off for me, waking up only now."
    "No, the doctor didn't talk to me."
    scene anim prolog_14
    show spill_red
    with dissolve
    "No one spoke to me at all, for the reason that I could no longer speak."
    "All I could remember was the terrible tearing sensation at the base of my skull when I almost managed to change from winter to summer."
    "And darkness."
    "All I could do now was squint my eyes at the flip calendar hanging above my head with the date: January 4th."
    "Looking at the calendar, but seeing smiles, laughter, the river flowing over the horizon..."
    "And perpetually red at the very edge of my vision - hard to see, incomprehensible."
    "What is it? Hair? Clothes?"
    "I couldn't see it. I couldn't remember."
    "It was scary, like I'd lost something important."
    "Something that kept me alive until now."
    "And now the question became more and more acute: Why me?"
    "What for?"
    "Who needs me so fake?"
    "Night fell on the city again, which I could only see by the lights in the corridor."
    "I myself lay in darkness."
    "And, once again trying to make a sound, I made only a pathetic half-snarl:"
    me "U… Uly…"
    th "Ulyana."
    th "And what do I do now?.."
    "No, that's no good."
    "I have to do something. Something..."
    "The equipment in the headboard beeped, noting the increased heartbeat."
    "That's what gave me the idea."
    "There wasn't much of me left, but there should have been enough to execute the idea."
    show spill_gray
    with dissolve
    "Cursing and torching myself with the last words, I clenched my shaking fingers into a fist and, step by step, began to reclaim space from nothingness."
    "I felt no friction of bodily cotton against my skin, no temperature, nothing."
    "All I had at my disposal was a single path through the crack of crumbling teeth."
    "They said I would never move."
    "But they kept fighting for me."
    th "Why?! Idiots! God, what idiots!"
    scene bg ext_winter_night_7dl
    show prologue_dream
    with dissolve
    "I took it millimeter by millimeter, and before my eyes stood the rushing winter road."
    "I knew where it was going to take me, I just had to keep going."
    "Millimeter by millimeter."
    "I don't know how long it took me, but I kept trying."
    scene bg ext_entrance_night_clear_7dl
    show prologue_dream
    with dissolve
    "And when the sky outside the window began to turn gray..."
    "A seemingly insensitive hand struck all those idiotic tubes, wires, drips..."
    "Winter changed to summer."
    "A warm summer night in which lived one funny girl..."
    hide prologue_dream
    with fade
    "With a sharp meow the equipment responded, but it didn't bother me anymore."
    play sound sfx_metal_door_heavy_close
    pause(.5)
    scene bg ext_entrance_night_clear_closed_7dl
    "I became real."
    show spill_red with dspr
    pause(2)
    scene anim prolog_2 with fade3
    "\[Bad ending unlocked - «Become Real»\]"
    $ sdl_persistent_inc("us_7dl_bad")
    play sound sfx_7dl["aunl"]
    show acm_logo_us_7dl_bad with moveinright:
        pos (1600, 1020)
    pause(7.4)
    call alt_7dl_titles
    pause(2)
    return

label alt_day7_us_7dl_shard:
    $ persistent.sprite_time = "prolog"
    $ day_time()
    play music music_7dl["forest_of_memories"] fadein 3
    scene bg ext_adductius_7dl with dissolve
    show anim_grain
    "I have disliked the phrase “you'll get it when you grow up” since I was a child."
    "Even the most complicated things can be spelled out on your fingers if you're good at them."
    "And certainly if you don't grow and change for years, it sounds like mockery."
    "That's why Anton and Senya knew from a very young age that their mother was erased."
    "Yes, I've been told all my life that I could get over it once I outgrew my age and started to grow up further, and then I could easily pretend I was a normal person."
    "A perfectly normal person, just like everyone else. Only somehow without baby pictures and with very young parents."
    "But how can you forget that someone had to die for your birth?"
    "And even though I was twice as old as Alisa when she was gone, I couldn't stop thinking about her even for a day."
    "Did she get what she really wanted?"
    "She's fine there, I thought, looking at the only picture of our family that Grandpa didn't have the heart to burn with all the others."
    "It wasn't her father who came to see her on parents' day with bad news, but her beloved older brother. Her parents hadn't lost two children that summer."
    "And from the day I made a promise not to seek the Road, I had only to believe."
    "To believe that it worked out just the way she wanted it to."
    stop music fadeout 3
    scene bg ext_khruschevka_rain_7dl with fade
    "On that overcast summer morning I was packing a bag of food for the kids at camp, and my thoughts involuntarily went back to that shift when we said goodbye to Eternal Rookie forever."
    $ alt_pause(1)
    $ set_mode_nvl()
    play music music_7dl["sad_piano"] fadein 3
    scene bg ext_no_bus
    show prologue_dream
    with dissolve
    "How many times did he and I cross paths at camp? I couldn't remember anymore."
    show bg ext_bus
    show prologue_dream
    show am normal pioneer behind prologue_dream
    with dissolve
    "He burst into Sovyonok's life abruptly, noisily and with a fight, but as if from day one he had become an integral part of it. And just as abruptly disappeared from it."
    hide am
    $ renpy.show("bg ext_no_bus", what = Sepia("bg ext_no_bus"))
    show prologue_dream
    with dissolve
    "And then eight years later, Liska called me."
    "She yelled into the phone so loud I thought I was going deaf:"

    dv "He got erased! Right after camp!"
    "She must have been perplexed as to what a boy-major living in Cuba and riding to a provincial camp like an exotic resort could want."
    "I wonder if he told anyone besides me that he was long since doomed?"
    nvl clear
    show bg int_us_kitchen_7dl with dissolve
    show prologue_dream
    with dissolve
    "Immediately after Liska called, I checked the envelope stored in the back of the closet."
    "Only then did I understand why he had left me that letter."
    "As well as the reason why he had chosen me."
    "Then I was waiting for him to show up on my doorstep, getting ready to meet him, anticipating telling him everything he had longed to know..."
    "And he didn't show up."
    "He hasn't shown up in a year or two."
    nvl clear
    $ set_mode_adv()
    hide prologue_dream with dissolve
    "Five years later, that call from Liska seemed like a vague dream, an obsession that I could never shake off."
    "The letter, gathering dust in my closet until it was claimed, weighed heavily on my soul, which had never been at peace without it."
    "One must have a high purpose, mustn't one?"
    "An idea to die for, a mission he carries on his shoulders against the world."
    stop music fadeout 6
    play sound sfx_7dl["ringtone"] fadein 1
    "The cell phone rang so unexpectedly that I almost dropped the bottle of lemonade from my hands."
    "This number was unfamiliar to me, but the first digits matched Liska's number."
    th "She lost her cell phone again and is calling from Sashka's?"
    stop sound
    us "Hello?"
    play music music_7dl["thousand_of_pixies"] fadein 3
    "From the voice I heard on the other end, the unfortunate bottle of lemonade involuntarily slipped from my fingers and rolled with a hiss across the floor."
    $ meet('am','Semyon')
    am "Excuse me for disturbing you, is this Ulyana Sumarokova?"
    us "Yes, it's me!" with vpunch
    "I shouted into the phone a little louder than I meant to."
    "He found me! He found me after all!"
    $ meet('am','Arseniy')
    am "This is Arseniy Persunov, your number was given to me by Lig... Alisa Dvachevskaya. I'd like to..."
    "There was a silence: he obviously didn't know how to start a conversation."
    "I was frantically choosing words myself, slicing around the kitchen."
    th "What would I want to hear from my own family when I found out the whole truth?"
    "Anything at all. I wanted to hear anything!"
    us "So, Arseniy, are you in Leningrad?"
    am "No, I'm in Kalinin, but..."
    us "Oh, that's a good! Can you come over to my place? You can come over anytime, even now!"
    am "Wait, let me ask my parents!"
    "Him being polite made me laugh."
    "I involuntarily looked at my face in the reflection of the microwave."
    "Well, yes, a grown-up aunt, thirty years old, though sometimes she's mistaken for a schoolgirl because of her height."
    "However, if you live too long with the same face, your brain learns to ignore all the changes very cleverly."
    "I managed not to notice even a huge belly, what about wrinkles..."
    am "I'm coming!"
    "My new-old acquaintance shouted happily into the phone."
    us "Write down the address..."
    scene bg int_us_livingroom_7dl with dissolve
    "I threw my cell phone aside and sank to my stool, catching my breath, but immediately sprang to my feet."
    "I was overcome by unparalleled anticipation, curiosity, and simply a sense of something meaningful, something incredible."
    "The last time I experienced something like this was during the launch of the Flares."
    "Taking the letter from the closet, I carefully placed it on the shelf in the hallway."
    "With quick strides I walked around the entire apartment, ran out to the balcony, opened the window, and shouted:"
    us "It wasn't all for nothing!"
    play sound sfx_water_emerge
    "I recoiled frightened from the window, ran into the bathroom, and splashed a handful of cold water in my face to calm myself."
    "I almost dragged myself into the hall, turned on the TV to pass the time, but still jumped at every rustle - what if he was already at the door and didn't dare to call?"
    play sound sfx_door_bell
    "And when the long-awaited bell rang, it took me barely a second to get to the door."
    scene bg int_us_frontdoor_7dl with dissolve
    show ars surp casual with dissolve
    us "Well hello!"
    show ars smile2 casual with dspr
    "I smiled broadly, and the boy standing outside the doorstep smiled back unabashedly."
    "A boy! How strange that was..."
    "When we met, we looked the same age."
    "But he was growing inexorably older and changing, like everyone else, and was quite the grown-up uncle the last time we met."
    "And now I was all grown up."
    "And I was getting to know him all over again. Who knew the nickname 'Eternal Rookie' would become so prophetic?"
    us "Come on in, don't just stand there. I'll make some tea!"
    show ars sad_smile casual with dspr
    "The rookie hesitated."
    am "Only I won't be long, my parents are waiting for me..."
    show ars surp casual with dspr
    us "It's okay, they'll wait. I've got something for you!"
    hide ars with dissolve
    "He cautiously entered the apartment, taking off his shoes as he went."
    scene bg int_us_livingroom_7dl with dissolve
    "I grabbed the envelope from the shelf and almost skipped to the kitchen."
    scene bg int_us_kitchen_7dl with dissolve
    "As soon as Rookie sat down at the table, I put the envelope in front of him."
    show ars surp casual close with dissolve
    am "What is this?"
    us "Liska told you I was erased too, right?"
    show ars scared casual close with dspr
    "The boy twitched like he'd been hit."
    "He's probably not used to hearing this kind of thing right in the forehead, but I was too excited for delicate conversation."
    us "On his last shift, Semyon left this for me, and asked me to give it to you when you found me."
    us "I don't know what's in there, I haven't read it, though I suppose it answered all your questions."
    show ars normal casual close with dspr
    hide ars with dissolve
    "The newbie began to open the envelope impatiently, and I turned my back to the stove, pretending to be busy organizing the tea party."
    "But every now and then I looked back - I was terribly curious how Rookie would react to a message from the past."
    am "Here my story began - here it ends..."
    "I turned again to the table to place the cups."
    show ars laugh casual close with dissolve
    "The rookie was smiling stupidly, looking somewhere in front of him."
    am "And you were in the same squad as him?"
    "I nodded cheerfully, pouring tea into cups."
    show ars smile casual close with dspr
    us "Yes, once we were in the same squad, although we crossed paths every year before that."
    us "Semyon was a busy man, every year there were surprises..."
    show ars laugh casual close with dspr
    "The boy's eyes lit up."
    am "Could you tell..."
    show ars surp casual close with dspr
    extend " oh!"
    "He wanted to slip the letter back into the envelope, but something prevented him."
    "When he looked inside, he pulled out another sheet of paper, folded in quadruplicate, with bewilderment."
    am "It's written here “give this to the kid”…"
    with flash_pink
    "I snatched the sheet from him, feeling myself blush."
    stop music fadeout 6
    "I shouldn't have thought well of him - even if he's gotten smart with age, he's always been an ass!"
    "I put the sheet aside - I was too eager to talk to my guest."
    scene black with joff_r
    play music music_7dl["finale_farewell"] fadein 3
    scene cg d7_us_bedroom_7dl with dissolve
    dn "So he knew what he was talking about when he forbade us to look for the Road."
    "We lay in bed, though I was so stressed out from this long day that I had absolutely no idea how I was going to sleep now."
    "We didn't talk to Rookie-Arseniy for long at all - I managed to tell him literally a couple of stories from camp before his parents called him."
    "And then I couldn't find myself a place for another hour."
    "What does the hero do after he's accomplished his mission? Live happily ever after?"
    "But I did live happily ever after, didn't I? I had Danka, our boys, my friends, my job at the children's sports school..."
    "But I didn't have a mission anymore. And I didn't know if that made me sad or happy."
    show cg d7_us_bedroom2_7dl with dissolve
    us "And I believed him right away."
    us "He was so sincere about his imminent demise, it was hard not to believe him."
    "I took the note he had left for me from the nightstand and reread it again."
    stop music fadeout 3
    $ alt_pause(2)
    $ set_mode_nvl()
    show bg ext_square_day
    show am smile pioneer
    show prologue_dream
    with dissolve
    window show
    play music music_7dl["happy_ending"] fadein 2
    "{i}Hey kid!{/i}"
    "{i}If you are reading this, I am no longer in your world. But don't weep for my fate - I'm better off than all of you!{/i}"
    show am smile2 pioneer with dspr
    "{i}Just kidding. Actually, if you're reading this, you're pretty smart.{/i}"
    "{i}I really believed you'd leave that stupid idea with the Old Road, know that.{/i}"
    show am smile pioneer with dspr
    "{i}Live in the present, you only have one.{/i}"
    "{i}I don't know if you're still friends with your guard, or if you've managed to lose each other, but I sincerely hope that each of you has already found your way.{/i}"
    show am normal pioneer with dspr
    "{i}The real way, which does not require the mythical Road from fairy tales.{/i}"
    show am think pioneer with dspr
    "{i}Do you want to know what those who choose to be erased are thinking? About what they can't ask of the universe, God, or anyone else in this world.{/i}"
    "{i}We hold no grudge against those who will live in our bodies after us, Ulya. And no one would ever blame a new person for a decision made by a previous one.{/i}"
    show am normal pioneer with dspr
    "{i}Never grieve for a past that hasn't even touched you. Give thanks to those who gave you the opportunity to see the future.{/i}"
    show am smile pioneer with dspr
    "{i}Best wishes, for now, Semyon Persunov.{/i}"
    show am grin pioneer with dspr
    "{i}P.S. For heaven's sake, don't put any scolopendras in his plate! It's wrong to mock children.{/i}"
    window auto
    $ alt_pause(1)
    $ set_mode_adv()
    scene cg d7_us_bedroom3_7dl with fade
    $alt_pause(0.5)
    scene cg d7_us_bedroom4_7dl with dspr
    "I folded the sheet again, turned off the lamp, and tucked my nose into Danya's shoulder."
    "For the first time in my life, there was no weight on my soul."
    $ meet('am','Me')
    $ sdl_persistent_inc("us_7dl_shard")
    play sound sfx_7dl["aunl"]
    show acm_logo_us_7dl_shard with moveinright:
        pos (1600, 1020)
    pause(7.4)
    call alt_7dl_titles
    pause(2)
    return

label alt_day7_us_7dl_px_breakfast:
    scene bg int_dining_hall_people_sunset_7dl with dissolve
    play ambience ambience_dining_hall_full fadein 3
    play music music_7dl["will_you"] fadein 3
    "The sleepy, sour pioneers settled into their seats, only the first squad again had to stand in line at the handout."
    "Now, for some reason it was incredibly infuriating."
    "It was as if you'd stepped up to the podium for an encore."
    "To the audience's much-loved shooting of the naked soul, watch it soar down from the eighth floor."
    "Hear that? That cry for help, touching, isn't it?"
    "There was a distinct reek of cold in the air and a reluctance to let summer end."
    "The pioneers worked busily with their spoons, but they talked reluctantly, and looked more inward, into themselves, than at others."
    "And I was one of them, too."
    dreamgirl "This music makes me sick, these songs make me shake..."
    th "Then what's it all for?"
    dreamgirl "Do I know? There's something vicious about this whole system of camps, meetings and breakups."
    dreamgirl "It's as if children are being toughened up, taught to live with a broken heart."
    th "Or maybe it's the other way around? Teach them to make friends, to make buddies..."
    dreamgirl "Lovers. And break up with them."
    dreamgirl "Lucky if you and your girl live in the same city. And if not?"
    if dr:
        dreamgirl "Think of your Ryoko for example."
        "I frowned."
    show sl normal pioneer at zenterright
    "Slavya, standing in front of me in line, turned around, as if sensing my gaze."
    sl "Is something wrong, Syomushka?"
    th "Wow."
    "I wondered."
    th "I'm «Syoamushka» now. Syooooomushka. Sounds like the name of a cheap burlesque."
    th "About the idiot who came to the audition for the Most Beautiful."
    sl "You look upset."
    me "I am upset."
    "I snapped."
    me "Pisses me off."
    show sl surprise pioneer with dspr
    sl "What?"
    me "Pretty much everything. And the fact that I arrived late, and the fact that everything goes wrong somehow."
    show sl smile2 pioneer with dspr
    sl "I don't want to leave either."
    "Slavya confessed."
    sl "I'm used to this place. Merged with it."
    sl "And now I can only come back here as an assistant of the squad leader."
    hide sl with fade
    if alt_day6_us_7dl_px_sl_join:
        "She put the plates on the tray and, smiling at me, stepped back to an empty table."
        "And soon I joined her."
        show sl normal pioneer with dissolve
        sl "Yes, I remember my promise."
        sl "We have the morning, so I'll keep an eye on you, all right."
        show us normal sport at zenterright
        show sl normal pioneer at left
        with move
        us "Do you think she'll manage to pass?"
        "Shook her head doubtfully as Ulyana appeared out of nowhere."
        me "If we don't try, we won't know, right?"
        us "And if she doesn't?"
        show sl serious pioneer with dspr
        sl "Pass where? You're not going to crawl somewhere right?"
        me "Are you claustrophobic?"
        sl "Claus... Oh, no. I'm not afraid of enclosed spaces."
        show us smile sport with dspr
        us "And what are you afraid of then?"
        "Slavya hesitated:"
        sl "Well, I'm afraid... Hey! I shouldn't say such things!"
        sl "Especially to you!"
        show us laugh sport with dspr
        us "Eh, almost worked!"
        "Ulyana wasn't the least bit upset."
        us "But if anything, you will lead her by the hand, okay, Syomych?"
        me "I will."
        "I agreed."
        show sl normal pioneer with dspr
        sl "But just so we're back in time for dinner. Will we make it?"
        "Ulyana and I looked at each other."
        "Personally, I had the feeling that if we succeeded, if we succeeded..."
        "Then neither Ulyana nor I would have to go back."
        "Slavya would have to go to the camp alone."
        "There's no reason for her to go anywhere. She's all right here."
        "It occurs to me that Ulyana has no place to go either."
        "She has some kind of search for that road, which we'll conclude tonight at the very end."
        "Let's close the gestalt, and then we can leave."
        with fade2
        me "Basically, it's not that long of a walk."
        "I figured it out."
        me "So it won't take long to get there and back, and if there are no delays, we'll be back in time for lunch."
        show sl smile pioneer with dspr
        sl "Remember, Syomushka, you promised."
        show us surp1 sport with dspr
        us "Syomushka?"
        me "Don't even ask."
        "I brushed it off."
        show us smile sport with dspr
        us "There is nothing to ask, it's all clear."
        us "But it's none of my business. Do what you want, but after breakfast I'll wait for you at the canteen."
        hide us with easeoutleft
        "She took off and raced away."
        sl "What's so important there I wonder?"
        "As if to herself, Slavya muttered."
        "I took the question as rhetorical and answered nothing."
        "Then we worked with our spoons in silence."
    else:
        "As I glanced at her, I didn't notice the breakfast being piled on my tray."
        "I was thinking about something, but I couldn't even remember what it was."
        "I just flinched when the cook shouted."
        th "I'm getting a little bit carried away."
        "Suddenly a definition from my past-future came to mind."
        "Which was as if it had never happened, and everything before last week's events was just a bad dream."
        "A false memory that I had filled my own head with, trying to justify my own unsociability."
        "Muttering an apology, I picked up my tray, giving way to the Electronik standing behind me."
        with fade
        "Ulyana intercepted my gaze from afar and waved frantically, beckoning me to her."
        show us normal sport with dissolve
        "And I approached. It's not hard for me."
        us "Sit."
        "After waiting for me to sit down and arrange my plates, Ulyana leaned toward me and, lowering her voice, announced:"
        us "We leave right after breakfast. No packing, we don't need anything."
        me "What about a supply of provisions for the long journey?"
        show us smile sport with dspr
        us "Syomych."
        "Ulyana looked at me like I was child."
        us "We're not going out for long. It'll either work out or not."
        me "Can't you tell me what's supposed to work?"
        us "No."
        "She cut it off."
        us "You'll see on the spot."
        me "Investigation, intrigue..."
        "The suspense was a little unnerving, but I decided to play along with the girl."
        "It was still fresh in my mind how yesterday's attempt to press on and find out everything I needed to know."
        "Somebody might have been embarrassed by Ulyana's proper manner of speech and her calm demeanor."
        "I mean, calm - in her spare time of trickery."
        "But she was and still was just that middle-school-aged girl - flighty, unsettled."
        "Unplayful."
        show us laugh sport with dspr
        us "Syomych, don't sulk."
        "She clapped me on the shoulder."
        us "Either it works out, and then we won't need any supplies; or it won't."
        me "You said that already."
        "I pointed out."
        me "About the stuff."
        show us laugh2 sport with dspr
        us "That's right! We don't need any stuff or food, if anything happens, we'll come back."
        me "What do you mean? Is there an option not to go back?"
        us "Have you been banging your head lately?"
        "Ulyana nodded sympathetically."
        us "Or do I need to remind you what we're looking for?"
        me "A way out of the camp."
        show us normal sport with dspr
        us "That's what you have to remember. Never forget it."
        "It seems it was really important for her to find the unfortunate loophole."
        "For what purpose, why - there was no answer to that, and the girl was in no hurry to be frank."
        "So I obediently nodded and spooned."
        us "Will be waiting outside."
        hide us with dissolve
    stop music fadeout 3
    stop ambience fadeout 1
    return

label alt_day7_us_7dl_px_escape:
    scene bg ext_dining_hall_away_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    play music music_7dl["unfulfilled"] fadein 3
    "After dodging the squad leader, who was obviously looking for something, I slipped out of the canteen and took a place in the far corner, ready to dive for cover at any moment."
    if alt_day6_us_7dl_px_sl_join:
        "It wasn't that I craved Slavyana's company in our little circle, but for some reason Ulyana was sure that without the activist we wouldn't get anywhere."
    else:
        "I had a strong feeling that nothing good would come of our venture, but I obediently stood and waited for Lena and Ulyana to approach."
        "As if the two of us couldn't make it."
    "And that was pretty weird."
    show us normal sport with dissolve
    us "So, are you ready?"
    "Ulyana, it seems, wasn't preparing at all."
    "The attitude was lighthearted, but... she wouldn't be Ulyana any other way, right?"
    me "I'm ready, waiting for our guest star."
    show us smile sport with dspr
    us "Star! What a choice of words you have."
    me "I am, I can do. Ah, there she is.."
    show us normal sport at left with move
    if alt_day6_us_7dl_px_sl_join:
        show sl normal pioneer at zenterright
        sl "Ready for a hike?"
    else:
        show un normal pioneer at zenterright
        un "Well, l-let's go?"
    "Ulyana and I nodded in unison."
    "Actually, we've been in rare unanimity with her lately."
    "Maybe it had something to do with our search, or maybe it had something to do with the fact that we were about the same size now, and she could always kick me in the neck if she wanted to."
    if alt_day6_us_7dl_px_sl_join:
        show sl smile pioneer with dspr
        sl "Well then, lead."
        us "Uno momento!"
    else:
        us "Catch up!"
    hide us with easeoutleft
    "Ulyana shouted and ran toward the south gate."
    if alt_day6_us_7dl_px_sl_join:
        "At first I didn't understand her strange enthusiasm, and then I followed Slavya's gaze."
        "And, of course, the squad leader came out on the porch."
        th "Who would have doubted it."
        "I wasn't the least bit surprised."
        me "Let's go, quick!"
        hide sl with dissolve
        "I shouted, and, catching Slavya's hand, ran after Ulyanka."
    else:
        hide un with easeoutleft
        un "Run!"
        "Lena took off, and there was nothing left for me to do but follow her."
    scene bg ext_backdoor_day_7dl
    show us normal sport at left
    if alt_day6_us_7dl_px_sl_join:
        show sl normal pioneer at zenterright
    else:
        show un normal pioneer at zenterright
    with dissolve
    "When we ran out the gate, Ulyana was already sitting there, picking the ground with the toe of her sandal with a bored look."
    us "Took you a long time."
    "She remarked, shaking her head disapprovingly with a look as if she had been sitting there for hours."
    "This time, I didn't react to her quip."
    if alt_day6_us_7dl_px_sl_join:
        "And Slavya didn't seem to care at all."
        show un normal pioneer at fright behind sl with dissolve
        "Lena, who unobtrusively joined the company, showed no emotion either."
    else:
        "Lena just shrugged her shoulders."
    show us laugh sport with dspr
    us "You're not even going to be offended? Ugh, how boring."
    me "Let's get it over with."
    show us normal sport with dspr
    us "As you command, Your Excellency!"
    "Ulyana jumped to her feet and waved her hand invitingly."
    scene bg ext_backroad_day_7dl
    with dissolve
    "She headed forward at a fairly brisk pace, so we had to work hard to catch up to the little one, too."
    "Though what kind of little girl is she now..."
    if alt_day6_us_7dl_px_sl_join:
        us "It's about an hour's walk."
        "She shared with Slavya."
    us "Tish, won't they be looking for you? What if we miss the bus?"
    "Lena indefinitely shook her shoulder and smiled."
    us "And that's considering we are taking a shortcut."
    stop music fadeout 3
    us "But that's okay. If we take the boring route, we won't get through the evening."
    scene bg ext_sandpit_day_7dl
    with dissolve
    play ambience ambience_forest_day fadein 5
    play music music_7dl["guitar_under_the_window"] fadein 3
    "I didn't really trust what Ulyanka said about coming faster if you walk right."
    "It wasn't that I didn't trust her."
    "It's just that I thought it was possible that she was playing, and that she might as well be lying because of that."
    "Not out of spite, but out of mischief of her personality."
    if alt_day6_us_7dl_px_sl_join:
        show sl normal pioneer at right with dissolve
        sl "Quarry? And what are we doing here?"
        show us normal sport at left
        show un normal pioneer at fleft behind us
        with dissolve
        us "Be patient, you'll soon see."
        sl "Yes, I've heard about this place more than once, there's nothing interesting here."
        show us smile sport with dspr
        us "That's because you're very boring, nothing interesting."
        dreamgirl "Yeah, no sweeping up or picking up papers."
        "Slavya frowned and wanted to say something in the vein of Ulyanka about particularly uncaring children, but I put my hand on her shoulder:"
        me "We're just not there yet. You'll see."
        show sl smile pioneer with dspr
        sl "But there's really nothing interesting there."
        sl "I've been here plenty of times, I know!"
        show us laugh sport with dspr
        us "You did?"
        "Smirked Ulyanka."
        us "So you know what's in the middle of the pit there, huh?"
        sl "Okay, not right there. Not far away."
        sl "And there's nothing much there. It's just overgrown and sandy in places."
        sl "Even if you play there, there's nothing to see."
        show us laugh2 sport with dspr
        us "Nothing-nothing?"
        show sl normal pioneer with dspr
        "Slavya pondered, rubbing her braid mechanically."
        "She looked at me, Ulyanka and Lena one by one."
        "Then she looked again at the railing, riddled with vain pioneers."
        sl "And though... This is the Forest of Memory! Some irresponsible people leave their autographs here."
        show sl serious pioneer
        show us shy sport
        show un shy pioneer
        with dissolve
        sl "And you know what? If you are going to engage in vandalism, then I strongly do not support you!"
        sl "What's more, I'm going back to camp now! I'm not going to take part in this."
        sl "If you care so much about a person, tell them straight out! Why cripple the tree?"
        show us laugh sport with dspr
        us "You are saying this now because you yourself don't have a heart like that here!"
        us "No one has written your name or circled it with a heart!"
        show sl laugh pioneer with dspr
        sl "Ulyana is as usual in her repertoire."
        show sl normal pioneer with dspr
        sl "But no. I don't want to see my name on a tree. I'm against it, okay?"
        show us normal sport with dspr
        us "I hear you. No, we're not cutting any trees."
        us "And you say it's just thickets and sand down there, right?"
        sl "Yes! I've been down there more than once."
        "Ulyana looked at me eloquently, and I hastened to intervene in the conversation:"
        me "And if you go further, it's just a forest, isn't it?"
        sl "That's right. You guys are asking some weird questions, did you forget where you were going yourself?"
        me "You mean just the woods and nothing else?"
        "I continued to persist."
        me "And if we go down now, we won't find a pond or a dirt road or a highway down there?"
        show sl surprise pioneer with dspr
        sl "A highway? It's just a sand quarry, it's not passable, why is there a highway?"
        show us grin sport with dspr
        us "You see, Syomych, this is what happens when you come here the wrong way!"
        us "Or too old."
        me "Or a fool."
        show us calml sport with dspr
        us "Hey, I haven't gotten to that point yet."
        me "Slavya, hold on to my hand and keep up, okay?"
    else:
        show un normal pioneer at right
        show us normal sport at left
        with dissolve
        un "We're not in much of a hurry, are we?"
        us "That's up to you."
        un "I'd like to do something."
        show us smile sport with dspr
        us "Some thing?"
        show un smile pioneer with dspr
        "Lena smiled, nodding at the railing."
        "It's quite obvious that she'd like to leave her mark here."
        us "Again..."
        show un shy pioneer with dspr
        "Lena was embarrassed, but nodded."
        un "I want..."
        show us laugh sport with dspr
        us "Come on. Make it quick!"
        "Permission granted."
        "Lena nodded obediently, was about to go somewhere, but immediately turned back to us in confusion."
        un "Ulyana, will you lend me that?"
        show us laugh2 sport with dspr
        us "The Cobbler Without Shoes!"
        show un normal pioneer with dspr
        "She must have enjoyed poking fun at her older friend little by little."
        "And if it wasn't for the embarrassing factor of me here, Lena wouldn't have raised an eyebrow."
        "After all, she is the more mature one."
        if (alt_day_binder != 1) and (counter_sl_7dl == 0):
            dreamgirl "Aren't you forgetting about the grasshopper, big boy?"
            th "That's right, too. That was quite a concert."
        hide un
        show us smile sport
        with dissolve
        "Lena, having gotten what she wanted, set off to maim the trees, and I smirked to see her off."
        me "And why do you keep terrorizing her?"
        us "To keep herself in control and her hands on the blanket!"
        me "That way you'll only make it worse..."
        show us laugh sport with dspr
        us "You're as dumb as you are, Syomych!"
        us "You just haven't seen the real her when she's not trying to get under the bench and sit there."
        us "When you're not there, she's a normal girl."
        un "I can hear you."
        show us normal sport with dspr
        us "See? There's nothing wrong. It's not for resentment or anything."
        us "As a friend, you know?"
        show un normal pioneer at right with dspr
        un "I finished."
        "Lena came back a little out of breath, but clearly pleased with herself."
        "In between, she rubbed her palm-apparently her hands weren't used to working with a knife."
        un "But I must warn you."
        "Immediately she informed me."
        un "I only went down to the pond, and then that was it."
        me "Why did you have to do that?"
        show un smile pioneer with dspr
        un "Because I was curious of course."
        show us grin sport with dspr
        us "Haven't you tried any further?"
        us "Ms Lazy Lazyness?"
        un "No."
        show un shy pioneer with dspr
        un "I've tried... It just won't let me go any further. It's like I'm going around in circles."
        us "Nonsense! We'll get you through!"
    "The whole thing sounded like a silly hoax, but I decided to be on the safe side."
    me "Stay on the path, let's go down and see if there's anything down there."
    if alt_day6_us_7dl_px_sl_join:
        show sl normal pioneer at center with move
        hide un with dissolve
        "Slavya obediently nodded and took Ulyana and me by the hands."
        sl "Let's go!"
        "Lena joined us in the keel."
    else:
        hide un with dissolve
        "Lena obediently stood behind us."
    "Once below, we looped along the paths for some time, until our eyes were opened to..."
    scene bg ext_lake_day_7dl
    show us smile sport at left
    if alt_day6_us_7dl_px_sl_join:
        show sl surprise pioneer at right
        show un normal pioneer at fleft behind us
        with dissolve
        us "Aha!"
        sl "No way! I've crawled all over this place."
        us "Crippled!"
        "Ulyanka jumped to the edge of the pond and stared into the water, looking for something there."
        me "How could you go around and not notice a pretty big pond?"
        sl "I don't know. But I really was here."
        "There was a look of bewilderment and resentment in Slavya's eyes."
        sl "I certainly would have noticed if I'd seen it."
        "Finding something in the water, Ulyana rushed back."
        us "There!"
        "She almost shoved her hand in Slavya's face with something green in her palm."
        "Probably thought to scare her like she did with Lena a few days ago, only she attacked the wrong person this time."
        "Keeping her cool, Slavya pulled away, turned Ulyana's hand around."
        "And on the palm of that hand proudly sat a tiny frog."
        "He looked alternately at me, at Slavya, and then he squawked."
        us "This one isn't real too?"
        show sl normal pioneer with dspr
        sl "Ulyana, let the animal go. Okay, okay, I believe, I believe. Are you satisfied?"
        show us normal sport with dspr
        us "That's it!"
        "She ran back to the pond and let the frog go there."
        us "So, what's next?"
        show sl sad pioneer with dspr
        sl "So we're not there yet?"
        sl "You sure we have enough time?"
        "Slavya looked up at the sky doubtfully."
        show us smile sport with dspr
        us "Don't be a coward! We'll make it! March, march!"
        "Ulyana dragged our procession forward again."
    scene bg ext_busstop_dust_7dl
    with fade
    play ambience ambience_camp_entrance_day fadein 3
    stop music fadeout 5
    "All in all, the way to the right point took about an hour."
    if alt_day6_us_7dl_px_sl_join:
        "Of course, it took a little effort when Slavya got the idea to walk in circles on the dirt road, but eventually we overcame this trouble as well."
    else:
        "Lena obediently followed us, and at just the right moment put her hand on my shoulder, albeit blushing hotly again."
        "Apparently, she realized that she couldn't go on without our help."
        "And she did!"
    "When the broken asphalt hit the soles of my sandals, I involuntarily shivered - too vivid a memory of yesterday's experiences, cold and fear."
    "It's too easy to remember that I don't actually belong here."
    if alt_day6_us_7dl_px_sl_join:
        play music music_7dl["sneakupon"] fadein 3
        show sl normal pioneer at right
        show us normal sport at left
        show un normal pioneer at fleft behind us
        with dissolve
        sl "How long do we have to walk like this?"
        "Ulyana raised her palm in front of her, covered her eyes, and, looking for directions, pointed toward the hillside on the horizon."
        us "That's as far as that stop, and then we'll take it from there..."
        us "Melt-melt, away you left..."
        sl "Do you want to find something else?"
        "Slavya worried."
        me "You'll see on the spot."
        "I got ahead of Ulyana and hurried off in the right direction."
        hide us
        hide sl
        hide un
        with dissolve
        "I headed out first, Slavya following right behind me."
        "I'd already been here yesterday, so I wasn't the least bit surprised when a thick concrete pad, holding up a pair of columns and a roof with a back wall, reappeared behind the parted trees."
        "The pavement was old and broken, and here and there the vegetation that had broken through indicated that the road was seldom used."
        "And a very long time ago - for the last time."
        "And yet we came here today for a reason."
        "I turned back for the first time - for a second I thought the asphalt pavement shook, as if smoothing out."
        "And a little deeper from the road, a few yards on the other side of the thicket was a small pocket with a fire pit lined with smoked stone, and a canvas bag hanging from a road sign."
        "Somehow I knew there was salt, matches and a compass."
        "The broken, abandoned bus stop was our landmark, serving as a relay point on our way to the future."
        show sl smile pioneer at right
        show us dontlike sport at left
        show un normal pioneer at fleft behind us
        with dissolve
        sl "That's where cleaning is needed... Get to work!"
        "Ulyana grimaced unhappily, but swallowed that, too."
        "The work boiled on - we undermined the sign and set it strictly upright, knocked the dust off the bench, cleared the road of attacking pebbles and branches."
        "The departure was supposed to happen in about three hours, but no one complained or rushed anywhere."
        "I think we found our own way."
        scene bg ext_busstop_sun_7dl
        with dissolve
        "And it's correctness was confirmed by the cheerful, bassy humming from across the horizon."
    else:
        play music music_7dl["exodus"] fadein 3
        "Another hour later we were there."
        "At that long-abandoned bus stop."
        me "So, what next?"
        show us normal sport with dspr
        us "I don't know exactly... I've never managed to get this far."
        me "So you're going out in the middle of nowhere, not even knowing what you'll end up doing?"
        show us dontlike sport with dissolve
        us "Yes, I don't know! Now what?"
        hide us with dissolve
        "She mumbled something to herself, pacing the area in front of the bus stop."
        show un shy pioneer with dissolve
        "And Lena and I sat down on the slightly sagging, but still firmly held bench."
        un "Do you think we'll make it?"
        me "Depends on what you mean by 'make it'."
        "I had a few ideas about why the hell we got in here, where no one could find us, even if they looked for us on purpose."
        "One was more fantastic than the next."
        "Some of it was even suggested by an inner voice, and after considering it, I found it very amusing, but totally illegal."
        "Lena was silent, too."
        "At first she sat beside me, trying her best not to blush."
        show un normal pioneer with dissolve
        "And then she grew weary of the silence, interspersed only by the muttering of our Susanin."
        un "S-Semyon?"
        me "Yes?"
        un "Why do you need it?"
        "The question was an interesting one. But there was no answer."
        "I mean, you could fit the base, make up your own motivation."
        "But it was all a flat-out lie."
        me "I don't know."
        "Because I really didn't know. Or didn't want to?"
        me "I'm curious to know where this search will eventually take us, how far those who did it before us..."
        un "Just curiosity?"
        me "Right."
        "Lena sighed and stared at her feet, drawing something in the sand with the toe of her shoe."
        "She didn't seem to be at all satisfied with my answer."
        me "And you?"
        show un surprise pioneer
        with dissolve
        un "Me?"
        me "Why did you go searching with us?"
        un "You know, I once made a wish..."
        me "What?"
        show un serious pioneer with dspr
        un "It's not a big deal."
        me "If you don't want to, don't tell me."
        un "It just hasn't come true, and it's not likely to come true."
        me "And what does this have to do with where we are now?"
        show un sad pioneer with dspr
        un "N-nothing, I guess..."
        un "But it seemed to me that if I could get away from here any other way, I could get away from there -"
        "She waved her hand in the air, apparently referring to the mainland."
        un "It'll be somehow different there, too."
        "I didn't understand anything, but I chose to remain silent."
        "So we sat there for a while."
        "And then Lena looked at the heart-shaped watch on her wrist."
        un "It didn't seem to work out."
        "She whispered."
        me "Why?"
        un "Because it's noon... We're leaving in an hour."
        "As she stood up, she waved her hand at Ulyana, beckoning her."
        show us dontlike sport at right
        show un normal pioneer at left
        with dissolve
        us "What do you want?"
        un "I'm leaving."
        "Lena's voice was calm, she seemed to have already thought it over, accepted it, and accepted it."
        un "This is as far as we go, we're not looking for anything else."
        show us sad sport with dspr
        us "You're right..."
        "Ulyana shook her head unhappily."
        un "So I'll go to camp. I'll have to go back the usual way."
        us "But I'll find it, I will!"
        un "Without me."
        hide un with dissolve
        me "Without me too."
        me "I was interested in confirming your theory... About how there's no other way to get out of here than by bus."
        me "So that's a lie. I'm going to camp."
        hide us with dissolve
        "Signing off, I nodded and followed Lena."
    stop music fadeout 3
    stop ambience fadeout 1
    return

label alt_day7_us_7dl_px_bus:
    scene cg d7_bus_night_7dl with dissolve
    play music music_7dl["escape_2"] fadein 3
    "Slavya frowned and spoke, but waved her hand and stepped aside, but Lena, on the other hand, perked up."
    "She jumped up, ran to the very edge of the roadway, waved her hand."
    "Of course she was noticed, of course she was reacted to."
    "Of course they did... Already she seemed destined to draw admiring attention."
    "Except that I was thinking about it in a detached way and without the healthy interest I expected."
    play sound sfx_bus_honk
    "The bus greeted her with a signal, and Lena laughed contentedly."
    "Ulyanka stood inaudibly beside me."
    "Found my palm."
    "Her fingers were hot and dry."
    us "Look."
    "She pointed her finger."
    us "The bus."
    me "Yes. What's wrong with it?"
    th "There shouldn't be any buses here."
    "With surprising clarity I realized."
    th "Nobody's been using this highway for a very long time."
    play sound sfx_intro_bus_door_open
    pause(3)
    scene anim intro_11
    with fade
    "Evoking a strange sense of déjà vu, the bus stopped right in front of us, I found myself in front of the doors - and the flaps hissed in different directions."
    me "Are we really just going to go like this? What about..."
    "I turned around, but all I saw were encouraging nods of encouragement from the girls."
    kids "Come on!"
    "Slavya held out her thumb, and Lena nodded unabashedly and smiled."
    "Ulyanka, on the other hand, was absolutely thrilled!"
    play sound sfx_slavya_run
    pause(2)
    "There was a stomp of footsteps behind me, and the same trio flew into the bus stop."
    dn "Phew, that was close!"
    dn "Get out of the way!"
    "After shoving me off, Danechka and his companions disappeared inside."
    "And I, looking after them, hesitated."
    menu:
        "Let's go!":
            $ alt_day7_us_7dl_px_escaped = True
            scene op_back
            with fade
            us "Yay!"
            "Ulyana jumped up, pushed me into the cabin, and dragged me to a seat over the wheel."
            show us laugh sport at right with dissolve
            us "The best view. I guarantee it."
            "I guess... What did she want to show me, I wonder?"
            show un normal pioneer at left with dissolve
            "Lena followed us in and sat in the seat next to us, the same one we had on the elevated seat above the wheel."
            "And Slavya stayed."
            "She shook her head and waved her hand and turned away."
            "And soon disappeared."
            "Outside the window, for some reason, it darkened rapidly, and I suddenly realized what confused me about the whole picture."
            "There."
            "The palms of hands caught my head and turned it violently to the side."
            "To the side... The window. {w}The window was dark as a poke in the eye."
            "And that's why it reflected so wonderfully the contents of the cabin. Empty."
        "I'm staying":
            "I didn't trust that Liazik."
            "Ulyana threw me a sympathetic look."
            us "Suit yourself."
            "After pushing me aside, she ran in after the boys."
            "Lena came in after her, giving me one last sympathetic look."
            "The doors closed, and it was just the two of us at the bus stop."
            scene bg ext_busstop_sun_7dl
            show sl normal pioneer
            with dissolve
            sl "Why didn't you go with them?"
            me "What's the point?"
            me "I got the answer to the question of whether there's any way to escape from here."
            me "So I guess we'll stop there."
            show sl smile pioneer with dissolve
            sl "So, we're going back then?"
            me "Yes."
            sl "I didn't remember the way."
            me "Nothing."
            "I smiled."
            me "I'll walk you."
    stop music fadeout 3
    stop ambience fadeout 1
    return

label alt_day7_us_7dl_px_wastelands:
    play ambience sfx_bus_interior_moving fadein 2
    "Just a boy and a girl sitting in the same seat. {w}And a girl sitting across the aisle."
    "Peers, the red-haired girl, probably even a little older than everyone else."
    "I smiled quietly. The cabin reeked of warmth and the smell of wormwood."
    "A silent blanket descended on our shoulders, a fairy tale."
    scene
    $ renpy.show("op_back", what = Noon("op_back"))
    with dissolve
    $ set_mode_nvl()
    play music music_list["raindrops"] fadein 3
    "What happened next?"
    "Well, you can stop being skeptical for a second and just let yourself believe."
    "After all, we're all only here because we once wanted a fairy tale."
    "So the fierce enemy is defeated, the princess is returned (or even taken to the wedding), half the kingdom is presented, and Sister Alyonushka is revived."
    "They began to live happily ever after, and..."
    nvl clear
    pause(1)
    "In fact, the Road wasn't exactly a road, and the bus wasn't exactly a bus."
    "But I figured that out before I even got on the bus."
    "By the uncompacted grass, by the lush blossoms of the wilts."
    "By the rapture in the eyes, reflecting that very color."
    "The bus that appeared out of nowhere, so sudden and extremely fortunate to find itself next to the pioneers ready for the road..."
    "There were many, many mysteries."
    "But today I was not at all eager to solve them."
    nvl clear
    pause(1)
    "We drove on and on, losing track of time, with no discomfort whatsoever, like a desire to eat or go to the bushes."
    "It was as if time stood still for all of us at one point, swaddling us in a tight harness of stasis, but - suddenly - leaving our hands and tongue free."
    "At first we sat each in our own place, as if we were trying to shut ourselves off from our surroundings."
    "Much later I began to understand why."
    "But that was later."
    "In the meantime..."
    "First, Lena moved in with us."
    nvl clear
    scene
    $ renpy.show("op_back", what = Dawn("op_back"))
    pause(1)
    "A little embarrassed of me, she talked to Ulyana about something while I looked out the window."
    "It was dark and gray."
    "Empty."
    "And there was an understanding from somewhere that it wasn't at all because it was night now and you just couldn't see anything."
    "It was more likely that there was nothing there."
    "But really! Doesn't that make sense?"
    nvl clear
    pause(1)
    "Some incredible mechanism, a machine capable of taking a passenger exactly where he wants to go - on what principles should it operate?"
    "First it must go to the common denominator of everything."
    "And that, as you know, is the void."
    "From there, it's a stone's throw from anywhere."
    nvl clear
    pause(1)
    "Danka and his companions sat apart for a long time, whispering about something, but in the end they gave up, too."
    "Danka himself was not capable of anything extraordinary; he was simply the leader of the remnants of his star."
    "If there were five of them, they could do anything-so he thought."
    "Alka shook his head, clearly not sharing his commander's opinion."
    "Tonik, on the other hand, paid no attention to the chatter; he just stared into the dark glass, where we were reflected."
    "And after a few seconds, events in the cabin and in the reflection began to differ."
    nvl clear
    pause(1)
    "The darkness in the cabin began to turn gray little by little, as if it were dawn outside."
    "The sun peeked into the cabin, casting harsh, unnaturally contrasting shadows, and in the windows visible in the reflection one could see five-story buildings, parks, cars running backward..."
    "The reflected bus was slowing down, its smooth run on the asphalt replaced by a vaguely familiar jolt."
    "A silent bell rings, and the doors open."
    "That's when Lena clutched Tonik's shoulders and ordered him not to show it!"
    nvl clear
    $ set_mode_adv()
    show un serious pioneer with dissolve
    un "Don't you dare, do you hear?! You can't!"
    tn "But I'm interested!"
    un "No! You'll jinx it! Turn off your TV, I don't want to see!"
    "She exhaled convulsively."
    un "I don't want to know."
    "With an indifferent motion of his shoulder, Tonik reached out to the glass and made a motion as if wiping something off the blackboard."
    "The reflection instantly disappeared - for a while there was bare blackness staring back at us."
    stop music fadeout 3
    "But a few seconds later everything was back to normal."
    hide un
    with fade2
    play music music_7dl["afraid_of_destiny"] fadein 3
    "It took me five hours to figure out where Lena was getting hysterical from."
    "During that time we fell asleep, and woke up to some strange sobbing."
    "As it turned out, it was Lena."
    "As it turned out, it had been daytime outside the windows, and the bus, which was now more like a streetcar, raced through vaguely familiar autumn streets, leaving the developments on the right side and the flat, flooded meadows on the left."
    "Parallel to us the tram tracks ran off into infinity, and with each thump at the junctions Lena shuddered and pulled her head into her shoulders."
    "The fingers on the rail turned white with strain."
    "And the girl herself was diligently looking only out the window, as if trying to discern familiar places there."
    with fade
    "And in spite of the nervous trembling of her lips, the intermittent breathing, it was obvious that we were somewhere in places she liked."
    "Which she... Remembers."
    "And when the viaduct, littered with cars and streetcars, flashed outside the window, I suddenly remembered the place myself."
    "I stared at Lena suspiciously, but I didn't think to ask her anything now."
    "There was no point now..."
    "Our bus-not the bus, the tram-not the tram, began to slow down."
    play sound sfx_bus_stop
    "Suddenly the smell of fallen leaves and creosote wafted in through the open window."
    play ambience ambience_camp_center_day fadein 3
    play sound sfx_bus_out fadein 0
    "We stopped altogether, the doors hissed open."
    "And Lena, on trembling legs, set out into the unknown."
    "She was pounding and shaking."
    "But she stubbornly walked, as if she knew what might lie ahead."
    "As I followed her gaze, I saw a certain couple sitting at the bus stop: a boy in a baseball cap, looking down at his feet, and a girl of about sixteen with a rather strange hair color."
    "The strange girl was holding a clipboard suspiciously similar to the one Lena had been carrying."
    "Only unlike our green-eyed girl, this one just waved the tablet around like a fan."
    "Yes, sometimes she looked in our direction with her eyes slanted."
    "Somehow she looked a lot like Lena. But in what way?"
    "The guy didn't react at all to the stopped traffic, seeming to be completely lost in his own thoughts, but the girl jumped up and down, jammed her neighbor, continuing to shoot in our direction with slanted eyes."
    "And got her way - the guy paid attention to us after all."
    "Raised his head."
    "From under his visor he looked at us with extremely familiar gray eyes."
    "And somehow he was suddenly there all at once, his neighbor, like a flag tied in the wind, flying after him."
    "One moment he was there, and now, here, giving Lena a hand."
    us "Gallant gentleman."
    "Giggled Ulyana, who was watching the action."
    "But she allowed herself nothing further as our 'gentleman,' after helping Lena down, grabbed her in an armful and pressed her against him with all his might."
    "The rascal stood back and politely waited for attention to come to her."
    voice "Lenka!"
    "He exhaled."
    voice "Finally! Where were you?"
    voice "And when did you have time to change?"
    "We didn't hear the girl's answer as the doors closed again and the transport came in motion."
    play sound sfx_intro_bus_door_open
    play ambience sfx_bus_interior_moving fadein 2
    "I hurried to the back ground - after cuddling up, Lena turned her attention to the third actor."
    me "And they look alike!"
    "It suddenly dawned on me."
    me "Lena and that..."
    "They stared at each other for a long, hard look, and then Lena suddenly settled where she stood - the slanted one barely had time to pick her up."
    us "Reunion."
    "Ulyana waved at the figures already almost indistinguishable on the horizon - the bus was picking up speed."
    me "Are these her acquaintances?"
    us "Family, more like."
    me "And this guy I've seen somewhere before..."
    "I shared."
    us "Syomych, sometimes you're such a retard, I can't help it!"
    me "What's the big deal?"
    me "What did I say?"
    "Ulyana shook her head and turned away."
    "However, I could see the sly smile on her lips."
    scene op_back
    with dissolve
    "A few hours later the trio of 'Guardsmen' got off at some half-stop and apologized to Ulyana for not being able to continue their service."
    "Two boys of their age were waiting for them, one of whom bore an uncanny resemblance to Olga Dmitrievna, and on seeing the other, Ulyana shuddered and sank into gloomy contemplation for a beating hour."
    "She didn't respond to questions, so I had to guess at the possible unpleasant history behind that boy on my own."
    "I don't think it was about any resentment or anything else..."
    with fade
    "I'm not particularly good at exploring human souls, especially when it comes to a child."
    "Yeah, well, now I'm a child myself."
    "With all my memories, all my bitter experiences..."
    "The question is, do I need it now? And if I do, why?"
    "No one could tell me the answer to that question: how to get rid of the cynic who sees the trick in everything."
    scene bg ext_railbridge_sunset_7dl
    with flash
    play ambience ambience_camp_entrance_night fadein 6
    "The next time we woke up, it was sunset outside the windows, and the bus was cooling off at the very stone headstock of the railroad bridge."
    "The doors were wide open, there was no one in the driver's seat."
    "And it was quiet and quiet all around..."
    "Only the singing of crickets and the barely audible movement of the grass around."
    show us smile sport with dissolve
    "Ulyana stretched out, looked around, and glowed:"
    us "Here we are!"
    "Here we are..."
    stop music fadeout 4
    play music music_7dl["wonderful_faraway"]
    hide us with dissolve
    "I don't know exactly how to describe the place where we found ourselves."
    "But one thing Ulyana and I agree on is that we liked it here."
    "They never heard of Sovyonok, Genda, computers, or the symptoms of the era."
    "But summer here lasts a long, long time and only ends when the kids get tired of playing."
    "A loophole into the impossible."
    with fade
    "There was a small, half-empty town just off the road, and there was easily a place for us."
    "That's where we settled down."
    "Ulyana needed someone to wait for her, and she knew for sure that she would only wait here."
    "There was no logic here at all, but from what I gather, it doesn't work well here at all and every once in a while."
    "Or she's just different here."
    with fade2
    "So we settled here, spending time together, playing, building huge structures out of derelict tires and train wrecks..."
    "It turns out that when you stop acting like an adult, a lot of things in the world become a lot less boring."
    "So we weren't bored."
    "Not bored at all."
    scene bg int_opened_door_7dl
    with diam
    "And then one day there was a tentative scratch at our door, and through the white glow beating across the threshold, the same guy who had met Danechka at the half-station stepped into the room."
    "Ulyana shrieked and threw her head against his shoulder and grabbed his arms..."
    "And he reached over her head and introduced himself to me with a brittle bass:"
    voice "Anton. The brother of this... schmuck."
    "Ulyana snarled angrily, and we laughed."
    "I couldn't help thinking that our summer was just beginning..."
    voice "Welcome to the Wastelands."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day7_us_7dl_px_true:
    play music music_7dl["tears_of"] fadein 3
    "And to put a full-stop here, conclude the narrative and let the reader go, shaking his manly paw, satisfied with himself and his time."
    "But I can't, you know?"
    "I can't lie, especially not in such things as the story of the boy Semyon, who nevertheless cheated both time and loneliness."
    "You can, of course, succumb to conjecture, make up a happy, unripe ending..."
    "But you can't."
    "Do you understand?"
    scene bg ext_railbridge_sunset_7dl
    show prologue_dream
    with dissolve
    "Persunov Semyon didn't live to be thirty just a few days."
    "After all, the Wastelands were not such a rescue."
    "Still, even here, in the land of eternal children's laughter, there are hardships and worries."
    "Even here, summer is by no means endless."
    "And, once upon a time, Semyon, now Semyon, or more often just Semich, one day, he gave up his life."
    "Just at some point he suddenly realized that the Wastelands around him, his friends, the established star-thing, that was his dream."
    "A lifelong dream."
    "And the laws of this same stupid life often dictate very unpleasant outcomes for us."
    "If you have nothing to live for, you don't live at all."
    "So he stopped. So silly, silly..."
    if loki:
        "It must have been a legacy of the old life."
        "A cursed memory that could never be uprooted to the end: lungs chopped off, fingers ground up, spleen torn apart."
        "Something inside always knew he was living on borrowed time."
        "And one day it demanded a loan payment."
    else:
        "The borrowed dream didn't last long. For the longest time, the responsibility for his seemingly peers, and in fact, his children, was held."
        "But even responsibility has its limits."
        "He walked around the cabins, asking if everyone was happy with everything, if their wishes were fulfilled, and if they wanted anything else."
        "It turns out that everything is wonderful."
        "Which means..."
    "All he had the strength to do was hold my fading consciousness, hold my warm twitching fingers in my hand, and smile."
    me "It's okay, little one. It's okay."
    "Maybe if there had been an ambulance crew, they could have both pumped out and brought the boy to consciousness."
    "But in the Wastelands no one ever gets sick or dies."
    "And winter is coming up from the periphery - but not mild and not at all affectionate."
    "So I'm cold now, and I don't know what to tell the reader so as not to upset him even more."
    "Perhaps about Anton, and Alka, and Tonik, and Danya, staring devastatedly at the barely-appeared link?"
    "About how desperately Ulyanka smiled with bitten lips, just to keep from howling with longing?"
    "No, of course not."
    "There must be hope, you hear?"
    "There is."
    "Autumn may be someday - even in the Wastelands, and the endless journey over them in search of the desperate and lonely."
    "Let even the maples drop their palms to the ground, and the children run screaming, scattering piles of leaves with their feet."
    "It's not autumn yet."
    "It's far from autumn."
    scene bg ext_busstop_sun_7dl
    show prologue_dream
    with dissolve
    "That's why Semchik still walks his summer."
    "And he hasn't worn out his pioneer tie or his sandals, which are too big for him now."
    "Which means he can be saved."
    "How?"
    "Don't close this book."
    "Don't close your heart from other people."
    "As long as there are people somewhere smiling with happiness, Semchik will live."
    "And his summer will be everlasting."
    scene anim prolog_2 with fade3
    "\[True-Int ending unlocked - «Summer Will Be...{w=1} E{w=0.1}v{w=0.1}e{w=0.1}r{w=0.1}l{w=0.1}a{w=0.1}s{w=0.1}t{w=0.1}i{w=0.1}n{w=0.1}g{w=0.1}»{w=0.1}\]"
    $ sdl_persistent_inc("us_7dl_px_true")
    play sound sfx_7dl["aunl"]
    show acm_logo_us_7dl_px_true with moveinright:
        pos (1600, 1020)
    pause(7.4)
    call alt_7dl_titles
    pause(2)
    return

label alt_day7_us_7dl_px_mourning:
    play music music_list["door_to_nightmare"] fadein 4
    scene bg ext_backdoor_day_7dl with dissolve
    play ambience ambience_camp_entrance_night fadein 5
    "We got to camp pretty quickly."
    "About forty or fifty minutes, maybe."
    "It was like we had a tailwind, and our legs stopped getting tired."
    "So we walked fast, too."
    with fade2
    "But, as it turns out..."
    "Not fast enough."
    if alt_day6_us_7dl_px_sl_join:
        "Slavya suddenly stopped."
        show sl surprise pioneer with dissolve
        sl "Did you hear that?"
        me "Hear what?"
        sl "Here..."
        $ volume(0.3, "sound")
        play sound sfx_bus_honk
        "I listened..."
        me "Sounds like a bus horn."
        show sl sad pioneer with dspr
        sl "But the departure was scheduled for three hours, I specifically checked!"
        sl "Run!"
        play ambience ambience_camp_center_day fadein 7
        scene bg ext_dining_hall_away_day at fast_running
        with flash
        "She took off in the direction of the square, and I ran after her."
        $ volume(0.8, "sound")
        scene bg ext_square_day at fast_running
        with flash
    else:
        "Lena went away instantly, as soon as we got to the gate."
        "I sat down on the log at the entrance and wondered."
        th "And was it worth it?"
        "All this foolish searching, all these unnecessary attempts to escape..."
        play sound sfx_slavya_run
        "I heard the sound of footsteps and slowly raised my head."
        show us sad sport with dissolve
        me "How was the search?"
        "I wasn't hiding sarcasm."
        me "Did you find anything?"
        us "Don't mock me, Syomych. It didn't work this time, so it'll work next time!"
        show us smile sport with dspr
        us "Why are you sitting there? And where did you lose Tisha?"
        me "She went to get ready."
        us "And what about you?"
        me "I don't have to pack..."
        us "Let's go!"
        "Ulyana, having already coped with her own misfortune, hurried to cheer me up as well."
        "With a pat on the shoulder. Well, of course. Plus a hundred for morale."
        us "If Auntie Olya finds us here, she'll punish us again."
        me "She won't. We're already leaving."
        show us laugh sport with dspr
        us "You don't know Auntie Olya very well, she'll think of something! And she will!"
        me "Whipping in the square?"
        show us laugh2 sport with dspr
        us "Don't get sour, let's go!"
        scene bg ext_square_day
        with dissolve
        play ambience ambience_camp_center_day fadein 3
        "When we entered the square, we found it quiet and desolate."
        show us surp1 sport at left with dspr
        us "Wow, how hard everyone is gathering."
        un "They're not gathering."
        show un serious pioneer at zenterright with dissolve
        "Reported a discreetly creeped up Lena."
        show us normal sport with dspr
        us "What do you mean?"
        show un normal pioneer with dspr
        un "When I came home, I saw that Miku's things were gone, and she herself was gone."
        us "Packed up and went to the gate?"
        un "Until departure..."
        "Lena looked at the watch on her wrist."
        un "Two more hours exactly. We were supposed to be taken away in the afternoon."
        un "I don't think she'll be standing at the gate for two hours."
        me "What's that supposed to mean?"
        show us smile sport with dspr
        us "Let's run to the gate, let's see!"
        hide us with easeoutleft
        "Ulyana darted off her place."
        "Lena and I exchanged glances, and an ice ball rolled down my back."
        "I gulped involuntarily."
    "Even though I hadn't cared about my fate before, for some reason I suddenly felt uncomfortable when we jumped out into the square and found no one there."
    if alt_day6_us_7dl_px_sl_join:
        sl "No way, are we too late?"
    scene bg ext_clubs_day at fast_running
    with flash
    "Another dash to the gate."
    "Usually there was always someone here, either kids playing or cyberneticists building something."
    "But this time..."
    scene bg ext_camp_entrance_day with flash:
    with dissolve
    play ambience ambience_camp_entrance_day fadein 3
    if alt_day6_us_7dl_px_sl_join:
        show sl normal pioneer with dissolve
        sl "Look! Look!"
        "I turned around sharply, looking where she was pointing."
    else:
        "When we ran out to the gate, there was no sign of Miku or anyone else."
        "There was a faint whiff of gasoline in the air, and the square in front of the gate was strewn with paper and garbage."
        "Ulyanka yelled something indecipherable, waving somewhere in the direction of the road."
        "I turned painfully slowly and looked in the same direction she was waving."
    scene bg ext_road_day
    with dissolve
    "In the distance, a bus was scrambling toward the horizon as a barely visible dot."
    if alt_day6_us_7dl_px_sl_join:
        show sl surprise pioneer with dissolve
        sl "They left... They left without us!"
        me "They left."
        hide sl with dissolve
        "Slavya sat down on the curb and covered her face with her hands."
        "And I stood there, not daring to put my arms around her and comfort her."
        "She was a stranger, so I didn't even think to open my arms."
        "After all, she's strong."
        "She'll be all right."
        show sl sad pioneer with dissolve
        sl "Now what?"
        "She mumbled."
        me "Next shift's in a week, you know."
        "I've never stayed late like this before, but for some reason it seemed like they knew how to look for and catch a stowaway here."
        sl "What are we going to do this week?"
        sl "What are we going to eat?"
    else:
        show un serious pioneer at zenterright
        show us laugh sport at cleft with dspr
        "Lena frowned, and Ulyana laughed:"
        us "Hooray-hooray! They left without us!"
        me "Do you think that's something good?"
        us "Of course! They'll be looking for us and they're bound to find us. Here."
        us "But it'll be two days for sure before the car goes there and back."
        show us laugh2 sport with dspr
        us "Can you imagine? Two days without obligation and other regime crap!"
        un "Have you thought about what we'll eat for those two days?"
    ba "The canteen is still open for the staff."
    "Like everyone else in this camp, Sanich has mastered the art of instant transmission."
    "So now he appeared behind my shoulder, making me wince."
    if alt_day6_us_7dl_px_sl_join:
        show sl normal pioneer with dspr
    else:
        show us normal sport at fleft
        show un normal pioneer at cleft
        with move
    show ba evil uniform at fright with dissolve
    ba "But first we have one small problem to solve."
    me "We already have one."
    ba "Fortunately, this one is quick and easy to solve."
    if alt_day6_us_7dl_px_sl_join:
        sl "What's the problem?"
    else:
        "The girls looked at the gym teacher questioningly."
    "And he came closer to me."
    ba "Put your palms on top of each other."
    me "Why?"
    ba "Wimp, is there something you don't understand?"
    "Sighing, I did as he told me."
    ba "Now on your forehead. On the back side."
    "I did that, too."
    play sound sfx_lena_hits_alisa
    with vpunch
    if alt_day6_us_7dl_px_sl_join:
        show sl scared pioneer
    else:
        show us fear sport
        show un shocked pioneer
    with flash_red
    "And he struck me briefly, without a swing, right in the middle of my palms."
    "I recoiled, my head humming like a bell."
    if alt_day6_us_7dl_px_sl_join:
        "Slavya was about to start saying something..."
    else:
        "The girls were shouting at each other..."
    ba "That's for being the only man in this crib and acting like a deer."
    ba "That's how you get your horns kicked."
    ba "Now about the broads..."
    if alt_day6_us_7dl_px_sl_join:
        show sl sad pioneer with dspr
    else:
        show us sad sport
        show un sad pioneer
        with dspr
    "He turned away from me and spoke."
    "No, he didn't use profanity, he didn't resort to personalities, and he was generally correct."
    "But for all that, he managed not to repeat himself once, and in the process, he managed to stomp on any self-esteem."
    "I could see that Sanich had been in the military and had worked with children for years."
    "He yelled so hard I went deaf in my left ear."
    "He yelled for a long time, with taste."
    if alt_day6_us_7dl_px_sl_join:
        ba "...the best pioneer! Squad leader's assistant! And who are you after that?"
        "Slavya lowered her head; she was well aware that by her levity she had simply ruined her own reputation."
        "Even the fact that she had questioned her departure three times did not whitewash her in the slightest."
    else:
        ba "...the earth bears! And you have yet to procreate, who will you be able to give birth to, with such genealogy?"
        "The girls were ashamedly silent."
        "They knew they were wrong all round, all round. You can't fight off the herd and all that..."
    ba "Viola's coming tomorrow, so you'll go into town tomorrow, too."
    ba "Now march to lunch and go home. There's a storm warning for the region."
    stop music fadeout 5
    play sound_loop ambience_7dl["rain"] fadein 5
    scene bg ext_houses_rainy_day_7dl with dissolve
    play music music_7dl["what_cost"] fadein 3
    "That's what happened in the end."
    if alt_day6_us_7dl_px_sl_join:
        "Slavya, apparently feeling a guilt complex, did not leave the cabin, doing something there alone."
        "I, too, was sitting in my room, muffling unsweetened tea and looking out the window."
        "Had time to read 'White Nights,' discovered on the squad leader's shelf."
        "I couldn't get my head around how they could just take off and leave us here?"
        "But I guess there was something I didn't know about this time, this world, after all."
    else:
        "We gathered in Ulyana's house and watched through the window as the rain and wind whipped Genda, as the roof boards creaked..."
        "The mood was no different from what was going on outside."
        "Dull, dull, gray."
    "So the appearance of the nurse in the car was somehow even relieved."
    "Violetta Cernovna showed neither delight nor anger at finding us in the dining room, only nodded and ordered:"
    cs "Pack."
    "What's there to pack, though - we were already sitting on our suitcases."
    scene
    $ renpy.show("bg ext_road_day", what = Desat1("bg ext_road_day"))
    with dissolve
    "We let her wash, eat and tidy herself up, and the return trip awaited us."
    "And here I sit in the car, feeling a warm presence nearby."
    if alt_day6_us_7dl_px_sl_join:
        "Slavya came to her senses a little and responded to my glances with an unfailing smile."
        "She will one day remember this incident as an amusing adventure."
        "With her inherent ease of character she is capable of laughing even at herself."
        "But me? Could I?"
        "And I didn't know the answer."
    else:
        "Ulyanka sat in the front seat, and Lena and I took a seat in the back."
        "The green-eyed girl was still a little embarrassed by me, though not as thoroughly as she had been a couple of days ago."
        "She leaned back and looked alternately at me and at the situation overboard."
        "It looked funny."
    "But there was a worm of doubt inside."
    "It seemed for some reason that my main difficulties were yet to come."
    "And the censure of local society did not seem to be the greatest of them all."
    "I was afraid I would fall asleep on the way, and..."
    show blink
    "That's how it turned out."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day7_us_7dl_px_good:
    play music music_7dl["pathways"] fadein 3
    scene anim intro_14 with dissolve
    play sound_loop sfx_bus_interior_moving
    play ambience ambience_cold_wind_loop fadein 3
    "In each of my lives, for some reason I've tried to stay away from people."
    "They're nobody to me, I'm nobody to them - everybody's happy."
    "And let them think of me as a silent man with an inferiority complex - I work hard, I do my job duties, and that's all I need."
    "There is absolutely no need for anyone to know how music sounds in my heart, how lines are written in the evenings in a book that I will one day publish."
    "There's absolutely no point in letting anyone in."
    "It's been known for a long time..."
    "Only those close to you can betray and hurt you."
    "That's their prerogative."
    stop sound_loop fadeout 6
    scene anim intro_7
    with dissolve
    "That's why I'd rather be a silent man with an inferiority complex."
    if loki:
        "That doesn't stop me from continuing to teach music to children - since I myself have long since been deprived of access to that country."
        "And the bitterer the envy, the heavier - the more sincere the lines are put to paper in the evenings."
    else:
        "After all, I have me. We'll definitely get through this."
        "One day I'll let go of the memory with gratitude for what she was."
        "But now she is, in fact, me."
        "And I feel like screaming into the faces of passersby sometimes."
        "People! Cherish your memory! It's your only treasure."
    scene anim intro_9
    with dissolve
    "And it's nobody's fault."
    "It's just life. It is what it is."
    "You're supposed to spend the day doing good for other people, but the whole evening is yours."
    "Because it's empty outside, if fate hasn't bumped you together once, it's like you don't even exist for each other on the street."
    "You pass one through the other, cold limbs with a ghostly touch, flinch, turn around..."
    "No, it just looked like that."
    stop ambience fadeout 6
    scene bg int_sam_room_7dl
    with fulldiam
    "Only, more and more often, it was no longer a guest but a mistress in my heart."
    "It squeezed my heart with a sense of the irreparability of the passing, as if it whispered that there would never be a right time, only wasted time."
    "But it never answered the question - how the hell am I supposed to do the right thing!"
    "Nobody knew. Neither did I."
    scene bg int_semen_bath_7dl with dissolve
    play sound_loop sfx_water_sink_stream
    "And when the longing became too much, I went to the bathtub, turned on the hottest water I could tolerate, and immersed myself in it, leaving only my mouth and nose outside."
    "To breathe, and..."
    me "God, I feel sick. What do I do?"
    scene anim intro_15
    with fade
    "Who am I asking for advice?"
    me "Why isn't this the right way? What am I doing wrong?"
    with fade
    "And why am I asking anyone for advice?"
    me "I'm sick of it. It's like I'm living last days of my life - just a little while longer, and the pieces will start falling off."
    with fade
    "I'm sick of it. Especially the silence."
    "I got along fine with loneliness for a while, but sometimes there comes a point when you just can't handle it."
    "My right palm was burning unbearably - I must have been leaning on a hot pipe for half an hour."
    "But it was something real, something I was at least able to fight."
    "Not like a sour cut-the result of the last six months."
    "I could have done something!"
    "Something, something that..."
    "With a shriek, I yanked my arm, trying to escape the burning-but in vain."
    "It didn't seem to be the boiling water at all."
    "What was it, then?"
    "I had to part with the cozy darkness and the splash of water."
    "I opened my eyes with an effort - my right palm was red and burnt."
    "For a second I imagined suddenly that a Flare had rolled across it - someone else's, on its way in search of it."
    "Mine would never burn. Wouldn't it?"
    stop sound_loop
    "Really?"
    "I wasn't sure of the answer, but I wasn't really intimidated by any prospect."
    "Particularly the risk of looking like an idiot."
    "Bringing the red palm close to my face, I looked it over carefully and said, unexpectedly to myself:"
    stop music fadeout 3
    me "Melt-melt, friendly gale…"
    scene cg d7_us_tai_tai_7dl
    with dissolve
    play music music_7dl["your_life"] fadein 3
    "The palm glowed softly in the half-light-and from the center of it, forming a glow, a cozy yellow ball bounced onto my middle finger."
    "Angrily he jumped up, clearly unhappy with how long it took me to call him."
    me "Help me find my way elsewhere…"
    "I asked. And Flare exchanged anger for mercy."
    with fade
    "Rolling over my arm once more, mopping up the scars and burns with its light, it rose into the air and, thinking, hit the wall with all its might, piercing through it and pacing far, far away - somewhere in the direction of the north."
    scene bg ext_winter_night_rotate_7dl
    show prologue_dream
    with fade
    "By some intuitive gut feeling, I could trace his path."
    "Most importantly, I could trace his direction - he was looking for extra power!"
    "On its own, the chick could do almost nothing except heal."
    "But when there were lots of them... Then they really had to be reckoned with!"
    if alt_day6_us_7dl_px_sl_join:
        "As I once had to..."
        "But Ulyana wasn't confused, she was just looking for something that only semi-mystical entities, whose only purpose is to help a person find the way, can give her."
        "The way to what? That's a whole separate story."
    else:
        "So he was looking for more Flares - to team up with them to help the foolish master again."
    scene bg ext_winter_night_7dl
    with dissolve
    "I've seen this place before, so I recognized it right away."
    "The place where the light was guiding me."
    "Though I still didn't understand why I still had it."
    "My world denies the existence of miracles and thus resembles that of an orthodox Christian."
    "And I'm... I'm too old. Too old."
    with fade
    "But here it is, the place of dreams, and here it is and me."
    "Standing on the bridge over the brook on the way to Shuvalovsky Park."
    "What and why I'm looking for here - I don't know exactly, but it's not the first time I've made it to 'Parnassus', where it's a twenty-minute walk to the park."
    "I walk here, look at the trees, climb Shulkova Hill, from which, according to legend, you can see the whole city in general."
    "But I much prefer the quieter, quieter places, where no one walks and you can throw your head back into the sky, gaze at the lazy rustling of the branches of the pine trees."
    "And lose sense of time for a few minutes."
    "To feel, to understand that these pines stood here three hundred and five hundred years ago - before Peter came and drove the Finnish fishermen out, wishing to 'open a window to Europe'."
    "They have seen everything."
    "And ready to share the knowledge, ready to send you wherever you want to go."
    "You could go to the eighty-ninth, why not? By their standards, it's a moment."
    "Close your eyes and it's done..."
    scene
    $ renpy.show("bg ext_winterpark_7dl", what = Dawn("bg ext_winterpark_7dl"))
    with fade
    "But today I didn't go to the pines."
    "Today I froze on the bridge because my Flare was smelling something... Something..."
    "The unfrozen brook, unwilling to submit to winter, was carrying dead leaves, twigs, and other debris."
    "But something on the water caught my attention, forcing me to look closely."
    "And yes."
    "A piece of bark with a glow on its mast floated right under my feet... A light."
    me "It can't be."
    "I heard my voice hoarse from long disuse."
    me "Unscientific fiction."
    "I picked it up, and I heard a shout:"
    us "Hey, that's mine!"
    "It couldn't have been either."
    "But nevertheless, it was."
    "I realized I wasn't dreaming."
    "I realized that once dreamed, the story has a sequel!"
    with fade
    $ set_mode_nvl()
    "She turned out exactly as I remembered her."
    if alt_day6_us_7dl_px_sl_join:
        "It's unclear why she came back."
    else:
        "Looking challengingly, instantly recognizing me."
    "And she was exactly as she had been in the camp."
    "Hasn't changed one bit."
    us "Not even six months later, showed up."
    us "And acting the same way!"
    "Except she had changed her unchanged T-shirt for a much more seasonally appropriate down jacket and winter pants."
    "She wasn't alone; she was accompanied by a guy about twenty-three, who looked a lot like her."
    "He had a sour expression on his face; apparently he didn't enjoy these walks at all."
    "I froze for a second, trying to figure out his kinship."
    th "Brother? Father? Uncle?"
    th "He was too young for a father, though."
    nvl clear
    "And Ulyana came up to me and snatched the ship out of my hands."
    us "Not yours, don't touch it, okay?"
    "I shrugged. What's not to understand?"
    "And she laughed and hugged me gustily."
    us "Syomische! Hooray! Syomische!"
    "And there was something else."
    "Someone."
    voice "Anton."
    "A guy held out his hand to me."
    voice "How do you know my sister?"
    me "It's a very long story."
    me "It's more like she knows me, but I..."
    "Ulyanka squealed and wouldn't let go of me, and Anton pulled her by the legs with a laugh."
    nvl clear
    scene bg int_sam_room_7dl
    with dissolve
    "Some things have changed in my life since then."
    "For some reason I can't be alone anymore."
    "Too much Ulyanka in my life."
    "Now she comes over for tea, chatting, playing on the computer."
    "Just to be quiet, remembering our silly adventures."
    if alt_day6_us_7dl_px_sl_join:
        "She doesn't talk about her bus route, not wanting to tell me."
        "I don't insist."
    else:
        "More often than not, she cringed because she never figured out how to behave at that stop."
        "What to do?"
        "She thought for a long time, but never came up with anything."
    "Never once did she start a conversation about what happened in an obscure summer of obscure places."
    "Only once I stumbled across a manuscript and shouted at it and read it."
    "She withdrew into herself and didn't show up for a week."
    "So that's probably where the story should have ended."
    "Really?"
    stop music fadeout 4
    $ set_mode_adv()
    play music sfx_7dl["ringtone"]
    "The phone rang. {w}Ulyana?"
    "I was just in the kitchen working on another masterpiece of meatballs and pasta, so I didn't hear the phone right away."
    "But when I heard it, I rushed into the room."
    stop music fadeout 3
    play ambience ambience_cold_wind_loop
    us "Hi. We need to meet and discuss something."
    me "When and where?"
    us "In an hour. On that bridge, remember?"
    me "Yes."
    scene cg d7_us_pixie_7dl
    with dissolve
    "Ulyana stood at the railing and looked at the frozen water, rubbing the folded paper boat in her hands mechanically."
    "She looked thoughtful."
    play music "<from 208.03 to 292.27>" + music_7dl["thousand_of_pixies"] fadein 8
    me "Hi."
    us "I remembered everything about camp."
    "Ignoring the greeting, she began."
    us "Remembered what these ships are for and what they are for."
    me "It's the Flares."
    us "You know?"
    me "Of course. IT can find something. Or help someone find their way."
    us "So. It has power. {w}It's not much, but if you combine the power of a thousand Flares, they can find their way from anywhere to anywhere!"
    us "Except there are almost none."
    us "It's just you and me here."
    us "The last of the Flares."
    me "So what? We already found a way once."
    if alt_day6_us_7dl_px_sl_join:
        me "You left without me!"
        us "I wish you were with me this time."
    else:
        me "But we couldn't figure out what to do with it."
        us "We did. But aren't you curious to keep looking?"
    me "What do you mean?"
    "Ulyana gave me a very mature look:"
    us "Don't you feel the limitations of this world yourself? It has so many boundaries. {w}And that means there is always somewhere to go!"
    me "To the adjacent world?"
    "There was unconcealed skepticism in my voice..."
    "But that was only because I was desperately afraid of being exposed."
    "To see my irrepressible thirst for life, my thirst for memories."
    "I have to do everything I can to one day say about my past, 'yes, it really was a great life'!"
    "And because..."
    if loki:
        us "To all the adjacent worlds!"
        me "How long are we going to search like this?"
        us "As long as you want! Don't you wonder what lies beyond?"
        me "I wonder."
        us "But remember, we don't have Danka or his boys. {w}We have a lot of work to do."
        me "That's nothing."
        "I smiled."
        me "We'll make it."
        us "We'll make it!"
        "Taking a candle out of her pocket, Ulyana hawked it to the paper boat and whispered:"
        us "Melt-melt, away you left…"
    else:
        "I got dizzy and had a real Deja Vu visit:"
        us "Fool! Why do we need the adjacent world?"
        "She shook her head sadly."
        us "I miss the girls. Liska, Tisha, Slavya. {w}Can we go back?"
        "And I, after hesitating, agreed."
        "As I stood up, I gave my hand to Ulyana, helping her up as well."
        "We only had one Flare so far."
        "And there was still a lot of work to be done."
        "Ulyana raised her palm, with the ship at eye level, and whispered:"
        us "Melt-melt…"
        "On the tip of her finger fluttered a tiny yellow ball."
        "After a moment's hesitation, it moved over to the paper boat."
        "And the ship instantly disappeared over the chasms."
        us "Now you!"
        "She pulled another folded ship out of her pocket, held it out to me."
        us "Come on."
        "I smiled and nodded."
        "Whispered:"
        me "Melt-melt…"
    scene anim prolog_2 with fade3
    "\[Good-Int ending unlocked - «Melt-Melt...»\]"
    $ sdl_persistent_inc("us_7dl_px_good")
    play sound sfx_7dl["aunl"]
    show acm_logo_us_7dl_px_good with moveinright:
        pos (1600, 1020)
    pause(7.4)
    stop music fadeout 6
    play music music_7dl["happy_ending"] fadein 1
    call alt_7dl_titles
    pause(2)
    return
