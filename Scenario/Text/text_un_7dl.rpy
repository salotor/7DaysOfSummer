label alt_day4_un_7dl_begin:
    play music music_list["my_daily_life"] fadein 3
    scene bg int_house_of_mt_sunset with dissolve
    "Good morning, good morning, good morning..."
    "Not really understanding the reasons for my high spirits, I opened my left eye completely on my own."
    "Ten minutes before wake up (Almost said «alarm clock»') - almost a record! - {w} and immediately hid under my pillow."
    "I knew perfectly well what the red light and the fogged windows meant - yesterday's matinee was still alive in my memory."
    "Strange, actually. It wasn't like that on the second day, and it's summertime..."
    "Unless it's some kind of cyclone or anticyclone? Like, blowing from the river means it's cooling the camp, no?"
    dreamgirl "Well, that's great. We've talked about the weather."
    dreamgirl "Now we'll talk about the harvest, and then we can move on to discussing the exchange rate."
    dreamgirl "Small talk in all its glory."
    th "Why so furious this morning?"
    if loki and alt_day3_un_strip_pool_un != 5:
        dreamgirl "You may have forgotten, but there's a green-eyed hottie who misses us here...{w=0.2}{nw}"
        if alt_day3_un_strip_pool_un <= 4:
            extend " Fragile{w=0.2}{nw}"
            if alt_day3_un_strip_pool_un <= 3:
                extend ", with clear skin{w=0.2}{nw}"
                if alt_day3_un_strip_pool_un <= 2:
                    ", beautifully shaped breasts{w=0.2}{nw}"
                    if alt_day3_un_strip_pool_un <= 1:
                        extend " and a flat tummy that goes smoothly into..."
                    else:
                        extend "..."
                    th "Okay, stop! I've had enough of men's morning goodmornings - let's not make it worse!"
                    dreamgirl "Why me? You saw it yourself yesterday!"
                    dreamgirl "Too bad you're such a retard."
                else:
                    extend "..."
            else:
                extend "..."
    elif herc:
        dreamgirl "You've probably forgotten, but certain someone actually have a crush on you."
        dreamgirl "I'll remind you, in case the details have slipped your mind:"
        dreamgirl "The unwanted case of drawing supplies; your questioning of why you're needed; her clutching your hand."
        dreamgirl "And the confession of not breathing without you."
        $renpy.notify('«for the sake of red word» - to make what is said sound more impactful, witty, beautiful.')
        th "But it could have been said just for the sake of a red word!"
        "I tried to sluggishly fend off my own conscience. {w}Futile, of course."
        dreamgirl "Fool! A red word."
        dreamgirl "The only red word appropriate here right now is to write «donkey» in fuchsia marker on your forehead."
        dreamgirl "Do you remember how long a minute lasts while waiting for a dear one? Are you really willing to put a girl through something like that?"
        th "Oh, okay, damn it. Going up."
    else:
        dreamgirl "It's just that there's probably a madwoman waiting for you outside."
        dreamgirl "And as someone who's met an even crazier person than himself, I'm a little uncomfortable."
        th "Lena? Why is she suddenly a madwoman?"
        dreamgirl "Hi. Remember how the evening ended!"
    dreamgirl "Also, I hasten to remind you of how your dancing ended."
    dreamgirl "Moreover, that she herself, doesn't quite like the public - and while she squeezed you quietly on the pontoons to the accompaniment of a screaming counselor, almost laughed with delight..."
    "I didn't feel sleepy at all, so, ignoring the possible cold, I climbed out from under the blankets."
    "I know I'm going to regret my hasty decision a hundred times."
    show mt normal pioneer at center
    mt "Semyon! Awake? Very well."
    show backpack_tiny behind mt:
        pos(760,675)
    "She nodded at the suspiciously familiar blue backpack with the stenciled white print of a Greenders along it."
    th "That's my good old Grizzly! Where did she just get it?"
    mt "It's parents' day, your parents came to see you, brought you something. {w}will you look at it?"
    me "It won't run away."
    mt "Well... I passed the package - my conscience is clear."
    "The counselor nodded and walked out of the cabin."
    "And I rushed after her!"
    th "Parents!"
    th "What parents, damn it!"
    hide mt with dissolve
    th "Lena's waiting for me!"
    "I'm going to get ready quickly."
    scene bg ext_house_of_mt_sunset with dissolve
    extend " and jumped out of the cabin."
    "I would have yelled, «Ahaaah!»"
    "Smiled."
    "And there would be one more person loving the world on this Earth."
    show unblink
    "There was no one outside."
    "I looked around more closely."
    "No, it would have been foolish to hope so."
    "Still nobody."
    if loki:
        me "Man, I don't play like that..."
        "I was hoping we could continue our exciting evening of getting to know each other."
        show mi normal pioneer far with dissolve
        mi "Good morning, Semyon!"
        "Shouted Miku, coming out of her cabin..."
        "Her cabin!"
        me "Miku! Is Lena home?"
        "The little Jap shook her head negatively."
        mi "She went somewhere before wake up."
        hide mi with dissolve
        "Completely fulfilling her duty of courtesy, Miku turned around and went to wash her face."
    elif herc:
        "Already ready for this morning to go from just fine to great, I sighed sadly."
        me "It had all started out so well..."
        th "I hope she's just been delayed somewhere or busy with something, not maliciously ignoring me."
        me "Or shy."
        "A door creaked down the street, but I didn't pay much attention to it - my thoughts were occupied with far more important matters."
        "As I pondered, I automatically performed the necessary minimum of action - and struggled to come out of my musings only after I tried to lock the door for the fourth time."
    else:
        "So, negative karma in action?"
        th "More like negative luck..."
        me "Good morning, camp!"
        show mi laugh pioneer far with dissolve
        "Coming out of her cabin, Miku smiled and waved at me."
        "If you count that, she and Lena lived three cabins away from us - that's about fifteen meters in a straight line."
        "No wonder I slept so well!"
        hide mi with dissolve
        "The Japanese girl turned around and headed toward the washbasins - they were the closest to their cabin."
    scene bg ext_washstand_day with dissolve
    play music music_list["everyday_theme"] fadein 5
    "I peeked into Lena and Miku's cabin just in case - maybe Lena is here."
    if loki:
        "It could be that Miku was wrong, couldn't it?"
    "But Lena wasn't home."
    th "Bruh."
    "The simple selfish frustration over the absence of the pretty little person was beginning to give way to some serious anxiety."
    play sound sfx_slavya_run
    if loki:
        show dv normal sport with dissolve
        "It was only Alisa's timely appearance that kept me from jumping to conclusions and making unnecessary gestures."
        dv "Hello."
        "She said indifferently, stopping in front of me."
        me "And good day to you, too."
        "She was wearing her conspicuous orange zippered suit, somehow conjuring up associations with Pikachu."
        me "Are you in a hurry to exercise?"
        dv "Something like that. {w} Don't think I'm working on a package, but Lena really asked for it."
        me "What?"
        "I couldn't help myself."
        me "Kiss me on her behalf?"
        show dv smile sport with dspr
        dv "Yeah. {w} With a sledgehammer."
        dv "She said to tell you that her folks took her away so you wouldn't worry."
        "Wow!"
        me "Thank you so much!"
        "From the bottom of my heart I thanked, and, not knowing why, I added:"
        me "You too can be cool, can't you!"
        "You have to be a redhead to blush the way Dvachevskaya blushed."
        "Personally, I couldn't flare up like that, to the roots of the hair."
        "After gifting me a look, she ran off before I spewed something else."
    else:
        show sl smile sport at center with dissolve
        "It was only the timely appearance of Slavya that interrupted the tantrum at the root."
        "Slavya was good today."
        "She was good yesterday... and the day before that."
        "Dewy legs, wet T-shirt, tight shorts."
        "Black uniform with white piping... How could a simple Soviet pioneer girl get an Adidas uniform?"
        sl "Semyon, hello!"
        "She said hello..."
        dreamgirl "NO {image=alt_KS_censor} WAY!"
        me "Fizkult-hooray..."
        "I saluted languidly."
        me "If you have an errand to run, let's do it a little later, okay?"
        me "I'm missing something... {w}I mean, someone..."
        show sl laugh sport with dspr
        sl "If you mean Lena, I was just coming to tell you about her."
        "The activist laughed."
        sl "Her father picked her up this morning, before he got up."
        sl "Not that I care about your relationship: I'm generally against all attempts to pry into other people's lives..."
        sl "But I thought you should know."
        me "Thank you so much!"
        "I smiled."
        me "Just a mountain off my shoulders..."
        me "Not everyone would do such a thing for a comrade. Thank you again - you're the best!"
        sl "Oh, you say that too."
        "Girl waved her hands jokingly at me."
        sl "See you at exercise!"
        "She ran off toward the square."
    scene bg ext_washstand2_day
    with dissolve
    play sound sfx_open_water_sink
    pause(1)
    play sound_loop sfx_water_sink_stream
    me "A-a-a-a-a!" with vpunch
    "Meeting Place Cannot Be Changed!"
    "Me, the sink, the ice water."
    "Ulyanka was nowhere to be seen, but that's no indication. {w}She may have been hiding in plain sight."
    "So I, in between looking around, began my morning bath routine."
    "Water in the face, tooth powder, stiff, scratchy waffle towel."
    "And I wondered how it was that in the Soviet Union men didn't worry at all about irritation after shaving."
    scene bg ext_washstand_day
    "Shit, if only to imagine that they've been wiping with such towels their whole lives: it's not that the skin is rough - it's keratinized!"
    "Shaved, washed off the soap, cauterized the cuts with cologne, and rode on, tail up."
    "With my skin, the cologne step would have resulted in immediate hospitalization."
    "Or they'd have buried me right there."
    me "Good thing I'm seventeen!"
    "I was glad from the bottom of my heart."
    dreamgirl "You're over twenty-five, man."
    dreamgirl "And being imprisoned in the body of a seventeen-year-old pioneer didn't kill any of your cockroaches."
    if loki:
        dreamgirl "You're still the same crook who hopes hard to find good in people. {w} But in vain."
        $renpy.notify('«Log in your own eye» - means seeing/mentioning other peoples problems, while not seeing your own.')
        dreamgirl "Just as, however, in vain you wrinkle your nose at the thought of logs in your eye."
        dreamgirl "You manipulate others - and dream of meeting something light."
        dreamgirl "It's called a double standard."
        dreamgirl "And not the least of which is why you're here."
    elif herc:
        dreamgirl "You're still an unbelieving fool, sitting out your youth guarding someone else's cigarettes and vodka."
        dreamgirl "All your pseudo-education comes from being well-read."
        dreamgirl "Although you've also read all sorts of crap, like science fiction and historical novels."
        dreamgirl "All in all, you're a seasoned loser with a touch of misanthropy in sheep's clothing."
        dreamgirl "That's probably what attracted Lena to you."
    else:
        dreamgirl "You're still that frustrated astronaut-designer."
        dreamgirl "A man who, as he grew older, began to have eye problems."
        dreamgirl "And now his world with a pronounced sepia-filter on top of the picture."
        dreamgirl "Long dollar vs. dream."
        dreamgirl "Remember this? I'm the chemical solution in Jack's blood."
    th "But I think, feel, and act like a seventeen-year-old pioneer, with a vividness of feeling that is unique to the young."
    th "And so it doesn't matter who's inside."
    th "This vacation is a million points ahead of any Dubai."
    "One last handful of water - to wake up finally - and you can start the day!"
    "The minimum goal is to make it to breakfast!"
    th "And the maximum..."
    play sound sfx_close_water_sink
    stop sound_loop
    scene bg ext_houses_sunset with dissolve
    "After putting down the towel and powder, I went outside, trying to figure out how best to get away."
    "So I was not at all surprised to find Olga Dmitrievna waiting for me at the doorstep."
    "The tradition of the loser in action."
    show mt smile sport with dissolve
    mt "Have you washed your face yet? You're quick. Come on, to the exercise, let's go, let's go!"
    me "What's the hurry..."
    "The hope of getting away quietly and searching died by itself."
    "Though there is always the possibility of sending Olga away, wrenching her arm and bouncing aside."
    "But let's save that dubious method for when we're completely desperate."
    "Having made a tacit agreement with myself, I let myself be carried away to the square."
    "If they say she's with parents', then with parents'!"
    stop music fadeout 5
    scene bg ext_square_sunset with dissolve
    play ambience ambience_camp_center_day fadein 3
    if not alt_day3_duty:
        "Exercise number three."
    else:
        "Exercise number two."
    "True, this time there was neither pleasure nor any positive emotion to be gained from waving our arms together."
    "I guess I'm too picky. It's possible that I get used to good things too quickly."
    "And who's without sin, I've got all the stones, nobody's going to throw anything at me."
    if loki:
        show dv smile sport at center
        "Dvachevskaya was already here and winked back at my glance."
        th "An unequal substitute for the one I expected to meet here!"
        "Pretending not to notice anything, I turned away."
        "The mood was rapidly deteriorating."
        hide dv smile sport
    else:
        "Slavya had just moved to the flapping of her arms, so only I could see her quick smile."
        show sl smile sport at center
        "Smile, don't smile... Who cares."
        "I was rapidly becoming apathetic."
        "Still, I don't like how quickly this passion flared up."
        "It's as if I've had my fill of the sweet stuff - and now I have the tragedy of life from the absence of an object of sorrows."
    "The perception of time turned off quite automatically - counting the sluggish seconds was unbearable."
    "My sour face must have illuminated the whole lineup with a sour light, for, having finished squatting and dissolved the formation, Slavya immediately approached me."
    show sl serious sport with dspr
    sl "Look, I can't look at you like this!"
    sl "I understand, of course: you're worried and so on - but you're going to embarrass us in front of the parents' squad!"
    th "I'm being kind today. I didn't kill anyone today."
    me "What's next."
    "I sullenly dropped it."
    me "Put on a Hollywood smile and frighten passersby with a grin?"
    show sl laugh sport with dspr
    if loki:
        sl "No, but..."
        me "In that case, Slavya, a huge request."
        "My voice has dropped to a menacing hiss."
        show sl serious sport with dspr
        me "Mind your own business."
        hide sl with dissolve2
        "She turned away and walked away, almost ran away. {w}Sounds like she was offended."
        "I don't give a damn."
        "I've got a lot to do."
        "I have to pretend to be at the lineup. {w}And, of course, to suffer the separation - not without it."
        "Our squad began to line up, and I stood in the second line, hiding behind Alisa."
    else:
        sl "I don't know what your «Hollywood smile» means, but I don't think that's it."
        "She hesitated a little."
        sl "Look, if I'm not mistaken, Lena took her father to show her artwork in the wall newspaper."
        sl "Why don't you go and meet them, huh?"
        show sl shy sport with dspr
        me "Who's going to let me walk around camp instead of the lineup?"
        "I hesitated."
        sl "On my responsibility."
        menu:
            "Only on your responsibility":
                $ karma -= 10
                $ lp_un += 1
                $ alt_day4_un_7dl_morning_searching = True
                "I tried to hide the contented smile spreading across my face, turned around and ran toward the library."
                play music music_list["everlasting_summer"] fadein 3
                "It's amazing how little a person needs just to keep from grumbling and cackling."
                "A few words of encouragement, a demonstration that not everyone around here cares."
                with fade2
                "Yes, permission to go in search of the princess from the land of childhood."
                "How nice everyone here is... Life has taught me that the more sugary it is at first, the nastier the pit where I will inevitably be dunked."
                "And it will come. {w} It's inevitable."
                "But it will all come later. {w}Since I have no tomorrow, we live for today."
                "Let's make the most of our time."
                scene bg ext_lib_sunset_7dl with dissolve
                "I made it to the library in less than five minutes."
                "Somewhere on the edge of earshot an engine roared, which I automatically identified as a police 'bobik'."
                $renpy.notify('In USSR, police was called militia.')
                "Or, in this time frame, probably a militia car after all."
                show un normal pioneer with dspr
                "And Lena came into my view."
                "Or rather, Lena's back - she was closing the library."
                "How could I resist?"
                "I don't think I could have pulled off that trick with Slavya - she's a hundred points ahead of me and everyone I know - but it worked out well with the absent-minded artist."
                "I tiptoed toward the girl and covered her eyes with my hands."
                show un surprise pioneer with dspr
                un "Oi."
                un "Who turned off the lights?"
                "She stood there and made no attempt to break free - apparently already well aware of who in this camp could be so cavalier."
                me "Good morning, Princess!"
                show un smile2 pioneer with dspr
                un "Is that you..."
                me "Yeah. Good to see you."
                "I smiled."
                me "I'm told you took your parents to show off your art."
                un "Well, yeah. {w}But you missed by a little bit."
                un "They checked my artwork to be decent and drove off."
                if herc:
                    me "No wonder they praised you: you're a wonderful painter."
                    show un shy pioneer at center with dspr
                    un "Don't overdo it..."
                    "Girl softly rebuked me."
                    un "Or I'll be proud and hold my nose. Here..."
                "She gently freed herself from my embrace and, turning the key once more, hid it in her pocket."
                un "Let me ask you, why aren't you at the lineup?"
                "She fidgeted."
                me "Yeah, you know... After yesterday I wanted to see you. And you're nowhere to be found. Nowhere at all."
                show un laugh pioneer with dspr
                un "I didn't think you had to be warned about such things!"
                un "Besides, they talked about it at the lineup yesterday - where were you?"
                if alt_day3_duty:
                    me "Where, where... {w}On duty!"
                else:
                    dreamgirl "Over there, where..."
                    me "Standing and dreaming."
                me "In a nutshell, I made a deal with Slavya..."
                dreamgirl "Wow! That sounds serious! {w}There's guys with blinkers blocking traffic, and you're in a black limousine with your fingers spread."
                dreamgirl "Making deals."
                dreamgirl "Don't puff up your cheeks, big bird."
                show un smile2 pioneer with dspr
                "As if guessing my thoughts, Lena smiled softly and took my hand."
                un "Let's go to breakfast, the negotiator."
            "I would love to, but...":
                me "I'll have Olga Dmitrievna perform an early euthanasia session through a lobotomy."
                "With a shrug, Slavya turned away, remarking:"
                sl "Do as you like..."
                "And went off to change - it was only minutes before the lineup."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day4_un_7dl_lineup:
    scene cg d4_lineup_no_un_7dl with dissolve
    play music music_list["trapped_in_dreams"] fadein 3
    "The lineup today was a little different from the usual lineup we are used to."
    "It's worth starting with the fact that our squads were somewhat flattened to make some room for the new «squad» formed by the parents."
    th "Someone definitely has their childhood playing out in a certain place."
    "The parents of the younger children expectedly came in - those who wanted to walk around the camp, see it, see if their children were having a good time."
    "The relatives of the older campers were much rarer - not surprising, according to overheard conversations, most of the kids come here every summer."
    "And here, these moms and dads, pretty young - a little over thirty, maybe - holding hands touchingly, giving the Pioneer salute and looking three times as funny dressed in stylized uniforms, some no longer fitting on their bellies."
    "No one made fun of them. {w}It wasn't that they were afraid - on the contrary, they appreciated that a grown man had taken time out, thrown over his vacation, and instead of baking for his daily bread, got out to visit a child for the day."
    th "A touching concern for the younger generation.{w}I wish it would help them."
    "I was creeped out for a second by my own callousness and powerlessness - because I, with my knowledge of the future, could warn someone, tell them about tanks, a putsch, the shooting of the Supreme Soviet and the era of the next state system."
    "My fingernails had grown back unnoticed in three days and were now cutting painfully into the soft skin of my palms as I clenched my fists."
    "I swore that if I got out and anchored in this world..."
    th "I'll do something. {w}at least I'll try!"
    "Meanwhile, the lineup continued - Olga Dmitrievna was already assigning a chaperone to each family and outlining the key points of today's open house."
    "Breakfast-lunch, understandably, bathing, «Fun Starts», activities in clubs ... {w}«Pioneers» will not be bored all day."
    "And in the evening, they'll get a concert."
    "Knowing what a good concert costs - torn ligaments, bruised toes, stumbled feet, and millions of nerve cells - and having seen none of that, I already rated the upcoming concert as not worthy of attention."
    th "Not going."
    th "I wish I had come here in early June - there was a chance on the twenty-second to go up at four o'clock as part of a historical reconstruction, crawl on my belly over obstacles, fly on a bungee tour and cross the river over a rope bridge."
    "And, of course, after lunch at the beautiful green field kitchen, consisting of incredibly tasty buckwheat porridge with fibers of stew and strong tea with galettes, undergo a brief briefing..."
    "And fall on my stomach, clutching the oar of the Seventy-four to my shoulder."
    "I remember how frightened I was by the crackling of the very neighboring machine guns - even though I opened my mouth in a silent scream."
    "«Zarnitsa»... Constant running, dirt, but a lot of positivity, all day in the woods and half a round per brother at the expense of the local DOSAAF."
    "What a shame that childhood really can't come back..."
    "I woke up from my memories and looked around."
    scene bg ext_square_sunset with dissolve
    "Slavya, as usual, raised the flag."
    "Olga, as usual, was reading a thanksgiving to the activist."
    "And I - and this time it was no ordinary thing - kept tossing and turning to look at the empty place in the formation, where there was no familiar head with funny ponytails."
    th "I should never have come here in the first place. I should have rushed off looking for her right from the washbasins."
    th "Or ripped my arm out of the counselor's hand..."
    if not loki:
        th "Shit, at least agree to Slavy's offer!"
    "It became unbearable from the puffed-up, cheap pathos of the proclamations, from the USSR anthem blaring from the loudspeaker in the canteen, to which the camouflage cloth was hoisted upward."
    "From all the faces that never became anything closer than temporary companions."
    "They all have their own lives, their own ideals - which they are ready to defend with the maximalism of youth."
    "And I sit on the bench at the bus stop and watch them move and live."
    "I shudder at the occasional intercepted glance, I cringe at the glances thrown at me."
    "And I distinctly feel something in the base of my skull tremble if someone else's gaze lingers longer than a second."
    "Someone else's unfulfilled dreams, someone else's unrealized potential - they run, stretching at speed in glowing threads, leaving me short with loneliness and needlessness."
    th "Choosing from all the treasures of the world the warmth of my hands and the sparkle of my eyes, it is so easy to go bankrupt."
    "She hasn't seen me for only eight hours. I haven't seen her for a full five hundred minutes."
    "What are the odds of her being an hourglass person in time to get cold and frosty again?"
    "I smile at her cheerfully, like an old acquaintance, and in my nose I can clearly hear the smell of the St. Petersburg subway, the chill of the glass car stars under my fingers, and the «steemorolin» stolen during the kiss still holds the remnants of taste."
    th "And I really have nothing more to offer - just a ride in the subway, a walk through the park, pushing you beyond the yellow divider on the pier at Primorskaya and pointing your finger at the Lenexpo pavilions, telling you that there's a little art going on inside."
    th "And offer to stay. Forever."
    th "To sit next to each other at the bus stop, touching shoulders, watching the Personalities scurrying back and forth, trying to unravel their stories and mysteries."
    th "Then go to «Quo Vadis» and muffle unmercifully black Americana until morning to the sounds of deceased poets - to me and my time - but topical and relevant to her."
    th "And in the morning, when the white night breaks into the waking day, to get out on the street and walk down the middle of the sleeping Nevsky, waving to the rarely-often passing cars, dodging sprinklers and trying not to laugh out loud when the traffic police patrol that caught me will write out a personal fine for Golovach Andrey and his fiancée, Lena."
    th "And there's no passport - we left it at home!"
    "I didn't catch the moment myself, when the outside sounds were cut off by the scorps guitar breakdowns - now the song was «ours»."
    "The outside world lost meaning and curtailed to the size of an annoying factor."
    "All that's left is waiting - and breathing."
    "Perhaps someday I will remember with nostalgia both the funny pathos of the counselor and the proud posture of Slavya, and even the ridiculously funny fanfares played by the ungodly kick-ass pioneers."
    "And it probably will be."
    "The most precious treasure a man can have is his memory."
    dreamgirl "You don't have time to wield it, so your job is to take care of the present moment."
    dreamgirl "And therefore it is advisable to prepare an airfield."
    th "You mean the exchange of contacts? But the house where I lived in this time hasn't even been built yet!"
    dreamgirl "What difference does it make? Leave the contacts of grandmothers, parents, acquaintances - just not boy friends - you know, only the lazy won't bite on an ownerless hottie."
    dreamgirl "You can't trust paper - it doesn't last."
    "I see what that might mean."
    th "First of all, that between the Manson and Durst recordings there should be a new recording where my not-so-old high voice will dictate to her how to get me, should providence suddenly force us to part ways."
    "And if the player dies, it will only be six years before the USB, from this starting point, appears. She'll be twenty-two. {w}I think that's a fine age to start looking."
    dreamgirl "And suddenly fire will come - the esquire will not be protected by his shield or his armor... Syoma, what are you going to do?"
    dreamgirl "Letting things go is not a bad idea, but wouldn't you at least like to dust your eyes?"
    th "I'll take her contacts, if that's what you mean."
    "We both knew it was a lie. {w}Some underlying feeling made it clear that just writing down the six digits of the zip code and the area code with the phone number in our case was tantamount to doing nothing."
    "It takes something much more monumental. Put the numbers in a smartphone? That's not even a thought, but someone or something could clean them out of there if they cared."
    th "Let's try a mushroom move: let her write her address, phone number, or whatever is important, on a piece of paper - let's take a picture."
    "Delighted with my own ingenuity, I turned up the volume and automaticly turned left after Slavya, who had returned to the line, commanded something."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day4_un_7dl_breakfast:
    scene bg int_dining_hall_people_sunset_7dl with fade
    play ambience ambience_dining_hall_full fadein 3
    if alt_day4_un_7dl_morning_searching:
        "There were no free tables - I had to land next to the concentrated chewer Slavya, who responded to our greeting with an absent-minded smile."
    else:
        "Despite the addition of the «squad», there were plenty of empty seats - after all, most of the children had already been taken away by busy parents."
        "So it wasn't hard for me to find an empty seat."
        "Here, for instance, across from the ubiquitous Slavya. {w}I hope she doesn't talk more than usual."
        show sl normal pioneer at center with dissolve
        me "Bon appetit."
        "I wished as I sat down across from her."
        "Slavya smiled silently at me and ducked into her coffee."
        "From the looks of it, her mood was brooding... {w}Well, I, being an inveterate misanthrope, did not pry into other people's souls."
        scene black with guess_on
        pause(2)
        "So my first reaction to someone covering my eyes with their palms behind me was in the predictable spirit of «well, who has an extra jaw there?»"
        $ meet('un','Girl')
        un "Guess who?!"
        menu:
            "Alisa, you?":
                $ lp_un -= 1
                $ karma -= 10
                $ meet('un','Lena')
                scene bg int_dining_hall_people_sunset_7dl
                show un surprise pioneer at left
                with guess_off
                un "Didn't think my voice sounded like Alisa's."
                "Surprised, the girl sat down next to me."
            "Who, who, Lena!":
                $ lp_un += 1
                $ meet('un','Lena')
                scene bg int_dining_hall_people_sunset_7dl
                show un smile2 pioneer at left
                with guess_off
                un "All yours!"
                "She picked up the breakfast tray from a nearby table that had been set aside for the «surprise» and sat down next to me."
                "I was absolutely delighted, but Slavya didn't seem to like it very much."
            "Vyacheslav Andreyevich, stop fooling around!":
                $ karma += 15
                $ meet('un','Lena')
                "There was a muffled chuckle behind me"
                scene bg int_dining_hall_people_sunset_7dl
                show un laugh pioneer at left
                with guess_off
                extend " and Lena sank down next to me."
                un "Now he's calling me names, noted."
                "She giggled, sinking her fork into a pile of steaming rice and gravy."
                me "So why were you fooling, Vyacheslav Andreyevich?"
                me "There are such respectable people sitting here, consuming coffee and newspaper"
                "I shot my eyes at Slavya, who was carefully pretending she wasn't here, and we laughed out loud."
                me "-and you're fooling here."
    "They fed meat and rice for breakfast. Terrific."
    "A real bachelor's breakfast!"
    show sl normal pioneer with dissolve
    show un normal pioneer at left with dspr
    "Although looking at Lena, consuming her uncomplicated meals without question, I drew some pretty obvious conclusions."
    "Either their mother doesn't cook in the family, which is nonsense in the USSR."
    "Or the father is a spineless wannabe and cooks very, very often - which is also unlikely."
    "I liked the third option the least, but it was the most realistic."
    "Or Lena grows up without a mother and is already used to unassuming male cooking."
    "Probably, as she gets older, she gets up to the stove on her own more and more often to avoid eating another dumpling or macaroni, but the strength is not always there, and from old memory..."
    "Anyway, that's probably how it is."
    dreamgirl "Maybe that's just how their mother cooks, man-like."
    "The subconscious parried sluggishly."
    "A woman who could not cook, according to the Domostroy, was not to be given in marriage."
    "Although this book was an apotheosis of chauvinism, it still had some good points."
    "Even in our relatively liberal society, the «broke up because I don't cook well» themes are still relevant."
    me "Your father came to see you, didn't he?"
    show un serious pioneer at left with dspr
    un "How do you know?"
    "Share the fruits of your thoughts with her?"
    dreamgirl "Yeah. Burn, Sherlock, bang the girl all over the canteen!"
    me "Call it a hunch."
    "Seems like a neutral enough answer to me."
    me "What are you doing after breakfast?"
    if not alt_day4_un_7dl_morning_searching:
        "Nodding to us, Slavya got up from the table and left."
    hide sl with dissolve
    un "My father brought the results of the exams - I was accepted to the preparatory to the Polytechnic."
    un "So I guess I'll start studying."
    me "Prepare?"
    un "Well... As a humanitarian, I'm having a hard time with the sciences - I'll have to do algebra."
    play music music_list["eat_some_trouble"] fadein 3
    un "Will you help me?"
    if herc or loki:
        me "Polytechnic, you say?"
        me "And what we talked about as recently as two days ago doesn't mean anything?"
        show un shy pioneer with dspr
        un "No, but..."
        me "But?!"
        me "Of course, it's absolutely none of my business! {w}And I won't pry into anyone else's!"
        me "You want to do some blueprints and CNC for the rest of your life - {w} for Random's sake."
        th "It's all the same that you'll bury the talent. But the place will be warm!"
        "Enraged, I jumped out from behind the table and quickly left the canteen."
        stop ambience
        scene bg ext_dining_hall_near_sunset
        with dissolve
        "With a soulful pounding of the door against the jamb, I looked around and, for lack of alternatives, settled down right there on the bench to mull over the situation."
        "I've just been fucked - that's an objective fact."
        "Shove me in my place, gave out number six, if you will, and pointed a finger at an empty room, implying that everyone gathered there cared deeply about my personal opinion."
        th "Could this mean that Lena doesn't care about what I say?"
        th "Or is it about her father? Is he so menacing that he paralyzes the girl's will?"
        th "Or is he so helpless that he needs an eye on him?"
        "Or is it that I, as a representative of the transient, am disenfranchised?"
        "Little by little, I began to cool down, and the anger was replaced by sluggish apathy."
        dreamgirl "So what. «She didn't listen», phew."
        dreamgirl "But we went out for three whole days."
        dreamgirl "A reason to be proud of yourself, eh?"
        "It's hard, extremely hard to ignore the voice inside me. {w}But I've succeeded in that task."
        "The main thing is to just count the breaths, and you can turn on the music."
        "I didn't have time to listen to the song last time by the way."
        "Liquid melancholy rushed into my brain, leaving me alone in a familiar and beloved place - a tiny concrete patch leaning on the void and opening into the void."
        "I am against the whole universe. My existence is a brick in the current moment."
        "And though I still consider myself immortal, there is nothing to even hope to reach the present kali yuga."
        "And so my worries are ridiculous and dumb. {w}We must hurry to live."
        "So when she touched me unabashedly on the shoulder, I was almost not angry at all anymore."
        show un shy pioneer with dissolve
        me "Yes?"
        un "Are you offended?"
        "Oh, that mixed feeling of guilt and embarrassment! What fertile ground for realizing all your vicious tendencies!"
        me "You know, I'm not thrilled about when my words are suddenly worthless."
        me "If we weren't... Hmmm... Close?"
        "Catching an affirmative nod, I continued:"
        me "Well, if we weren't close, I'd spat and just leave."
        me "But your opinion means something to me. {w}And that's why it hurts."
        "With a heavy sigh, she sat down next to me."
        un "Don't sulk, okay?"
        un "I just want... For us to be together..."
        me "Lena, we are together. And if we run out of time, we can always do assignments together for the wall newspaper."
        me "You're risking your own future for nothing."
        un "Nonsense..."
        un "I just don't have much of a chance of getting into that one."
        if herc:
            play music music_list["tried_to_bring_it_back"] fadein 3
            me "No one promised it would be easy."
            un "How can you not understand..."
            me "I understand just fine! {w}I just thought you cared about what I say!"
            me "You understand one thing: you won't always be as old as you are now, and you won't always be looking at the future from a crossroads."
            me "A couple of years, and you pick a college, and God forbid you make a wrong choice."
            me "Because if you make a mistake, it will be your misfortune, guilt and a yoke for the rest of your life."
            me "A couple more years and you're in your third decade, you're still full of enthusiasm and life, but some things are already broken inside."
            "Getting heated, I jumped up and paced back and forth in front of the increasingly shrinking girl."
            me "Five more years and your eyes grow dim and your soul dies, unable to fulfill itself."
            me "Then husband-child-work-home-relatives, and the once cheerful, carefree girl, immensely cute to me, turns into the surface of an eraser - elastic, gray, and faceless."
            me "And by the time you're thirty, you become an unwanted, and therefore clinging, woman who, while still young, has completely forgotten how to dream."
            me "How's your perspective?"
            show un cry pioneer with dspr
            un "Why are you saying all this? Why?"
            "She curled up in a ball, resting her chin on her lap, and looked at me with weeping eyes."
            un "I..."
            "She cried, bitterly and inconsolably."
            "And I, suddenly losing my confidence, throwing away, discharging my own mortido, became fully aware of why people didn't love me."
            "And I rushed to run. {w} To the gate."
            "That's where it all began. {w}That's where it ends."
            scene bg ext_square_sunset at fast_running
            th "I hope I can catch a ride and escape from a place where nobody cares about me."
            "I hope so..."
            dreamgirl "What a fool you are, Semyon."
            dreamgirl "You fight with a girl, you make her cry, what's the point?"
            dreamgirl "Self-assertion? Self-actualization? Authority?"
            dreamgirl "Or do you think that if she didn't rush to tell her father that she's not going to any polytechnics because some Semyon told her to follow her dream, you're done? {w}Divorce and cactus between the beds?"
            th "Shut up!!!"
            dreamgirl "Hey, are you serious? What are you, dude!"
            dreamgirl "Chill out! I'm on your side."
            th "Fuck you..."
        else:
            me "And that's why you decided to pick a place where the water doesn't flow?"
            "I asked wryly."
            show un sad pioneer with dspr
            un "No."
            un "I don't know anything yet."
            un "The results are preliminary - everything can still be reversed."
            me "So why didn't you tell your father right away?"
            show un smile2 pioneer with dspr
            un "Who said I didn't?"
            "The girl smiled slyly."
            un "But only he knows about it, and about the preliminaries - counselor."
            un "So now we can get some smart books and, like, hide somewhere in the woods or the library and sit alone. What do you think of that idea?"
            me "Do we have to lie to do that?"
            show un normal pioneer with dspr
            un "I didn't lie to you. I wanted you to help me, so..."
            "I sighed."
            "Lena took me by the hand and, lifting me up, led me toward her cabin."
            hide un with dissolve
            stop music fadeout 3
    else:
        me "Let me ask you, what are you going to learn in the time left?"
        me "Or are you a math savant?"
        "I snorted."
        un "I'm sorry, what?"
        me "Nothing."
        if not alt_day4_un_7dl_morning_searching:
            show un shy pioneer at center with dissolve
            un "I'm sorry, I'm really being silly..."
            "She mumbled."
            me "Okay, let's go get as many books as we can."
            me "I still don't think it's a good idea, but you tell me."
            show un surprise pioneer with dspr
            un "What?"
            me "I say: let's close the subject."
        else:
            "She wanted to put her hand on my shoulder, but I twitched my shoulder unpleasantly."
            show un sad pioneer with dspr
            "She got sad."
            "All right, it's nothing, it's just a mundane thing."
            "I myself twisted at the falseness of the strained smile."
            me "All right, forget it. Let's get the books."
        "Lena took me by the hand and, lifting me up, led me toward her cabin."
        hide un with dissolve
        stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day4_un_7dl_entrance:
    scene bg ext_camp_entrance_day with dissolve2
    play ambience ambience_camp_center_day fadein 5
    "Once outside the camp, I found a place on the dusty curb, shook off the dirt, and sat down to indefinable, alien memories."
    th "Why and how do I know... Remember Lena?"
    "A comedy of errors..."
    "We walk, scooting each other - she pokes her finger in my side, to where she still touched her pads yesterday, scouting."
    th "Yeah, that girl doesn't do anything for nothing."
    "And I... Well, I pretend to want to get under her dress - not for the purpose of groping there or anything."
    "It's just a game, with no ulterior motive."
    "She pretends to believe me."
    me "You look incredibly beautiful in that dress."
    un "Yeah? So it's about the dress?"
    "My goddess grins."
    un "Shall we try it on you then? Get a live daffodil."
    me "It's about who's wearing the dress."
    "I don't get provoked."
    me "It just looks good on you."
    play music music_list["smooth_machine"] fadein 5
    "A Volga pulled up next to me with screeching tires, Violetta looked out and shouted at me:"
    show cs normal at center
    cs "Hello, pioneer."
    cs "Would you mind watching the car: I'll get to the boss'?"
    "I nodded silently, she thanked me with a look and disappeared behind the gate."
    hide cs with dissolve
    "The stop is a sigh-sob, if we were walking through a park, the rustle of the trees would be interrupted by the hum of passing cars, and a piece of nature would be trapped in a concrete, stuffy embrace."
    "I don't know why I thought of the city. It was like I was walking with her - there, somewhere, once upon a time."
    "The bitter, transparent scent of dead leaves lying golden beneath my feet."
    "Chipped chestnut fingers."
    "The tart taste of the acorn."
    "The funny sound of snowberry bunches bursting."
    "And a streetcar rushes past us in the distance, and we race, and the cold air seems to give us wings: me, in an old carjack, her, in a red hooded coat, which for some reason I have always called a spacesuit."
    "We run for a full fifteen seconds in line, until the carriage driver, after giving his farewell call, adds to his stride."
    "And we roll onto piles of leaves, and kiss until our temples ache from lack of oxygen, and her lips are soft, supple, but ruthlessly demanding."
    "Lena..."
    "Someone's silhouette blocked the sunlight, and I looked up."
    if lp_un > 17:
        $ alt_day4_un_7dl_calm = 'un'
        show un serious pioneer at center with dissolve
        "Lena was standing over me, looking at me with the sternest look in the unkind girl's arsenal."
        "I suddenly felt a prick of conscience, realizing belatedly that I'd been making her run after me all day."
        "I don't know about her, but I'd have been flipping out!"
        me "Hello again..."
        "I muttered."
        un "Hello again."
        un "Shall we talk?"
        show un normal pioneer with dspr
        "I shrugged."
        "As much as I'd like to pretend to be a hurt innocence and an insult to my best feelings right now..."
        "Damn this nonsense if it makes Lena cry!"
        show un serious pioneer with dspr
        un "I wanted to... {w} apologize."
        "I shook off the seat beside me and nodded - saying, «sit down»."
        "Sitting down next to me, Lena continued her confession."
        un "You see, I didn't believe you until the last. {w}That you were serious in your suggestions, in your plans..."
        un "I wasn't even sure you liked me... {w}I wasn't sure."
        me "And what's changed?"
        un "You're crazy."
        "She said it as a statement."
        "Brutal and true. The term is blunt."
        un "I'm sorry for not trusting you."
        me "You didn't trust me either..."
        me "What a lovely thing."
        show un shy pioneer with dspr
        un "I understand, I shouldn't have. But... {w}Well, I've already had an unpleasant experience."
        "An unpleasant experience is, I take it, someone either wooing or solely paying attention to a girl for that purpose?"
        me "What about the papers?"
        show un surprise pioneer with dspr
        un "What papers?"
        me "I mean the polytech."
        show un shy pioneer with dspr
        un "You see... I'm not sure I draw well enough to go there."
        me "Do you know why the Japanese are a great nation? {w}Because whoever doesn't sing, draws."
        me "They believe that every person has a talent."
        me "I have no idea how you sing, but you're at least a good drawer, I can tell you that!"
        show un serious pioneer with dspr
        un "But I draw everything equally, and not many people praise them... My drawings."
        me "You have to develop your talent. Ideally, you shouldn't have been sent to a high school, but to an art school..."
        un "It's just... I'll go there and they'll tell me to draw something."
        un "What if I don't draw well?"
        un "We don't have an art school in town, so I'll have to go to Leningrad, to Mukha."
        me "So what? They have their own dormitory there - they'll put you up; I'll give you some contacts just in case - you won't get lost."
        "She looked at me incredulously."
        show un sad pioneer with dspr
        un "You never told me: what would happen if I fail?"
        me "And you never told me what would have happened if I hadn't let my tongue loose on the porch."
        "I put my arm around her waist and pulled her to me."
        me "Some things just have to be done. Take a risk, you know?"
        "The gloomy pictures my brain was painting, I decided to keep to myself."
        "After all, a friend of mine managed to come from Togliatti, fail, and then get into the top ten scholarships the next year."
        "And that's in our dusky time, not in the sleepy sunny USSR."
        me "I'll give you some addresses - there are good people living there..."
        "I hesitated whether to tell you that they were my grandparents, and decided to settle on a less shocking half-truth:"
        me "These are my distant relatives."
        me "Anyway, go ahead."
        show un smile pioneer with dspr
        "She smiled slyly in response to my revelation."
        un "And that means you're not sulking anymore?"
        "Viola walked past and nodded appreciatively at me."
        "I outlined a slight bow in return."
        "And only after seeing the Volga off with a glance, I turned to Lena:"
        me "I didn't sulk for a minute."
    else:
        $ alt_day4_un_7dl_calm = 'dv'
        show dv angry pioneer at center with dissolve
        "Alisa. Whatever she wanted, it couldn't have ended well for me."
        "She was looking at me too threateningly."
        th "The donkey was angry today: he found out he was a donkey..."
        me "Will you explain to me why you're angry?"
        "I asked blankly."
        show dv rage pioneer with dspr
        dv "And you dare to ask?!"
        "Alisa seemed to be barely restraining herself from starting to hit me right now."
        "I was even a little frightened - but only just a little."
        me "Yeah. {w}I'm curious as to what I've angered Dvachevskaya herself into coming to beat me."
        "She took several deep breaths and exhaled, apparently reminding herself that she had to make a claim first."
        "Finally she calmed down enough to begin to articulate herself more or less clearly."
        show dv angry pioneer close with dspr
        "She came right up to me and hovered menacingly on top of me."
        dv "I don't know what's going on there with Lena..."
        dv "She keeps quiet when I ask her what's wrong."
        show dv grin pioneer close with dspr
        dv "But I know it's about you."
        me "So what?"
        th "If she also takes on the role of a caring moralistic mother..."
        "And Alisa surprised me."
        "She brought her face close to mine, as she was, and studied something in my eyes for a few seconds."
        dv "It's hardly the point here that you hurt her - you get the point."
        dv "Plus that silly expression saying that you... Fell for her!"
        dv "Anyway, she's my friend, and she's crying."
        show dv angry pioneer close with dspr
        dv "And when she cries, my sense of humor fails, okay?"
        dv "That's why you're getting your last Chinese warning, rookie - if one more time she cries over you... Watch out. Got it?"
        "I shrugged."
        me "I'm not the reason she's crying. It's because of her own indecision."
        show dv surprise pioneer close with dspr
        "Looks like I managed to surprise her."
        dv "Explain?"
        me "I mean the study."
        show dv surprise pioneer close with dspr
        dv "She didn't tell me anything - she just burst into tears and slammed the door to the cabin. {w}What happened?"
        "I really wanted to wave my hand, yell at her and put it in her place... But she's a friend, so she might have some advice."
        me "Lena's father came to see her today and brought the results of her preliminary exams."
        me "She's been accepted into the preparatory program. She's in a field of study that she doesn't need."
        me "Have you seen how she draws?"
        show dv normal pioneer close with dspr
        dv "Yeah, she draws great."
        me "Exactly."
        me "She shouldn't become a seamstress-motorist. Go to art school, become an artist - that's what she should do!"
        show dv laugh pioneer close with dspr
        dv "You can say that too! Have you seen our villages? We have one art school for the whole town - what school are we talking about!"
        me "Really?"
        show dv normal pioneer with dspr
        dv "No, I'm kidding."
        "Alisa got serious, taking one step back."
        dv "So you were swearing that she wants to go to Polytechnic?"
        me "Yeah... I really want her to do what she likes."
        me "Get your dream job and you won't work a single day in your life. Have you heard the saying?"
        "Alisa only snorted."
        dv "A dead giveaway. {w}She has to go to the capital, and there's no leads, no connections."
        me "That's not the problem..."
        "I've looked at who I might know who lived in the Northern Capital now. {w}A couple of names came up immediately, then various uncles and grandmothers... Anyway, there was a place to put a talented girl while she was enrolled."
        me "I'm ready to help her, and it's like I care more than she does about what her future will be."
        me "And she nods and agrees, but she still does it her own way!"
        "I went off on a scream."
        me "I've seen so many of them! I was like that myself, damn it! So what if didn't qualify in the kidneys: I could have gone to a sanatorium for treatment!"
        "The voice came off, and praise be to Random. It was strange and stupid to sit there and look up and confess the ruined dream of someone who still had everything ahead of her."
        me "I'm sorry. {w}But I won't forgive Lena if she gives up now."
        me "Her talent doesn't belong to her anymore."
        show blink
        hide dv with dissolve
        pause(4)
        hide blink
        scene bg ext_camp_entrance_day
        show unblink
        "A silence thickened over the red-hot asphalt, and a few minutes later I anticipated rather than felt someone sinking nearby on the concrete."
        "Green-eyed. With a purple sheen of thick mop of hair tied up in funny ponytails."
        "Alisa has already left."
        me "Heard everything?"
        show un smile pioneer with dissolve
        "She sighed guiltily and rubbed her forehead against my shoulder."
        un "Forgive me for my cowardice. {w}It's been a long, long time since anyone has cared for me like that."
        "Instead of answering, I exchanged nods with Viola and, after glancing at the Volga, turned to Lena:"
        me "I didn't sulk for a minute."
        me "I just almost drove away. Lucky you had time to intercept me."
    "Lena took me by the hand and, lifting me up, led me toward her cabin."
    hide un with dissolve
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day4_un_7dl_declaration:
    scene bg ext_house_of_un_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    play music music_list["your_bright_side"] fadein 3
    "We've worn ourselves out in these two days, together all the time."
    "Who knew what was really going on in our heads..."
    "I mean, I could vouch for myself, but about Lena..."
    play sound sfx_open_dooor_campus_2
    pause(1)
    scene bg int_house_of_un_day with dissolve
    show un normal pioneer at center with dissolve
    if loki:
        un "Here, look!"
        "She stepped back to the table and, taking one out of a pile of sheets of cotton paper, turned it over and handed it to me."
        me "What's this?"
        show un shy pioneer with dspr
        un "Your story... {w}About where did your stuff go."
        "The picture I held in my hands was both funny and hilarious - just as I had imagined while I was jabbering at the girl, trying to disconnect myself from some inexplicably grieving thoughts:"
        "A coniferous, pine-fir forest, the rain pounding oblique strokes into the greedy dry earth."
        "And under one of the bushes sits a boy who looks suspiciously like me - huddled together, trying to shelter from the rain..."
        "And he is protected from the rain by his ever memorable blouse - pink, with buttons around the neckline, the dimensions more like a tank sheath."
        "I guess laughter wasn't really appropriate here, but I couldn't help myself."
        show un smile pioneer with dspr
        un "Do you like it?"
        me "You're wonderful!"
        "Some things are better left as they are, some things are better made into a habit."
        "Those talented fingers - I kissed one by one - deserve to be kissed."
        dreamgirl "Deserve to wear a ring?"
        me "I can hardly fight the urge to kiss-miss you."
        show un shy pioneer with dspr
        un "Get yourself under control!"
        "I think I embarrassed her. {w} Once again."
        "Somewhere we lost that moment when a handsome person was handsome in everything, including outwardly and inwardly."
        "Of course, there was always room for silly girls. But more often than not, they turned out to be much smarter than those around them thought."
        "In Lena's case... She wasn't lacking in beauty. She wasn't lacking in intelligence."
        "And it was only her non-humanity - a consequence of some childhood trauma - that kept her from becoming something like Miku or Slavya or Olga Dmitrievna."
        "That might be a good thing - it means we can trust each other completely."
    "She walked past me and stood at the door, covering the exit with her own body."
    show un serious pioneer with dspr
    un "Semyon, you must promise me that you won't allow yourself such outbursts of irritation again."
    if not (loki or herc):
        me "I wasn't getting annoyed, I was just being flippant... Wrong way, that's all."
        un "Like I'm doing this for my own pleasure."
    un "I'm not trying to manipulate you or anything."
    if herc or loki:
        show un cry pioneer with dspr
        un "But I almost went crazy with fear when you rattled the door in the canteen!"
    else:
        show un sad pioneer with dspr
    "She looked at me helplessly."
    un "I'm very hurt and very scared when you swear or sarcasm."
    "And how can you not go and hug her like that?"
    "I know, not everyone likes girls to be taken care of... {w}Not gonna lie, I would have run away from possible responsibility a few days ago myself."
    "And that means... That means she's {w}influenced me. {w}Rebuilt me."
    "And even if a secret door opens right now, leading from dreamland back to the icy streets, I won't go back there the way I was."
    "Because that me no longer exists."
    me "On some level, your dream has also become my dream."
    me "It would be a shame if you refused."
    un "That's not true. {w}I've listened to you - I've drawn conclusions."
    un "Just... Don't do that again, okay? Don't hurt me."
    me "I promise."
    show un cry_smile pioneer with dspr
    un "You swear?"
    me "I swear."
    me "Shall we go for a walk?"
    show un sad pioneer with dspr
    un "Still, I'd like to make sure."
    un "I mean the books - let's at least take them for show, you don't even have to wear them."
    me "What about the tireless guard-dragon?"
    show un smile2 pioneer with dspr
    un "You know... For some reason she's not even mad. {w}I'm not sure if it's just me, though..."
    "And I'll have to check, then. I'll be like Tipanov, chest to chest."
    "Speaking of embrasures."
    "I suddenly remembered Olga Dmitrievna's words this morning about my parents' visit."
    me "How about we'll go to my place before going to the Buzzer?"
    un "Lets go."
    "I haven't moved from my place."
    un "If you want to go somewhere, you have to get out of the cabin first."
    "Girl reminded politely."
    me "You could lend me a hand you know. Help"
    "I grumbled."
    show un laugh pioneer with dspr
    un "When you're become old, then I'll lend it."
    play sound sfx_open_dooor_campus_2
    scene bg ext_house_of_un_day with dissolve
    show un normal pioneer with dspr
    me "I'll need you to do something for me, and then I'll do something for you."
    "I reprimanded.{nw}"
    if alt_day4_un_7dl_morning_searching:
        extend " — for the second time today —{nw}"
    extend ", looking at her back."
    dreamgirl "Yeah BABYYYYY! That's what I've been waiting for, that's what it's all about! First you do it for her, then she'll do it for you!"
    dreamgirl "Or you can do it at the same time and the pose will be called «69»!"
    dreamgirl "That sounds like Jimmy Bloodhound!"
    "And the inner voice howled:"
    show un shy pioneer with dspr
    stop music fadeout 3
    dreamgirl "You and me baby ain't nothin' but mammals!{w} So let's do it like they do on the Discovery Channel!"
    play sound sfx_7dl["mammal"] fadein 1
    "Damn eidetic memory reproduced everything, right down to the stupid rhythm of the song."
    "Memory and a little libido."
    "I stopped and took a breath."
    with fade
    "J-j-just stay calm... Nerve cells don't regenerate."
    "Suppressing the irrational urge to strangle the inner voice, I returned to the topic of conversation."
    play music music_list["your_bright_side"] fadein 3
    me "As part of our promise yesterday that we wouldn't let each other go to waste. Remember?"
    show un smile pioneer with dspr
    un "Of course I remember!"
    me "I realize, of course, that it's a little premature to talk about it now, but..."
    un "No, no..."
    "Looking at me seriously, Lena interrupted."
    un "Only three days to go, it's not the last day to make it."
    "I sat down where I was standing."
    "Luckily, the steps of the Balticon were very timely nearby."
    if alt_day_binder != 1:
        me "What do you mean, three days?!" with vpunch
        "I howled."
        me "Are you out of your mind? {w}Any normal camp has a three-week shift!"
        show un laugh pioneer with dspr
        un "It was three weeks: you just came late."
    else:
        me "To tell you the truth, I thought the shift was a little longer here."
        me "It's a shame to come for only a week, even though I understood from Slavya's explanation that I arrived not even in the middle of it."
    "Lena smiled and was about to sit down next to me, but I jumped up and paced back and forth, most hastily getting rid of the prospect of «plenty of time yet» in my own plans."
    scene bg ext_un_house_with_un_7dl with flash
    "And Lena, smiling serenely, dropped her sandals and stayed barefoot on the sun - warmed planks, playing with inbound butterflies."
    "Apparently used to men's tantrums."
    "And, of course, long ago she found the panacea: long, patient and unobtrusive waiting."
    "A short skirt, a loose shirt, a couple of buttons open so that you could see the pearly skin of her sunless belly - apparently, tanning was not among the priorities of the reading enthusiast."
    "So I ran around in circles for a few more minutes, after which the calm image of the tanning girl took effect."
    me "All right, let's move on to my cabin."
    "She rose easily, took my hand, clung her index finger to my pinky finger, and smiled warmly."
    un "Let's go!"
    scene bg ext_house_of_mt_sunset with dissolve
    "Fifteen steps are my fifteen steps if I run, sixteen steps if I walk, and thirty-two if I stride over the street, chest out with a wheel, and shoulders outstretched."
    "Walkining."
    show un smile pioneer with dspr
    un "You're fooling around again..."
    "She'd love to be strict, reserved, proper, judicious, and prudent."
    "But I'm bad, I'm a creep, and I won't let her go into herself and get lost there."
    play sound sfx_open_dooor_campus_1
    "The lock was one turn locked again - it didn't even seem to occur to Olga that someone might intrude on the counselor's house and try to open it."
    "So I had to fight with the lock before the wick agreed to give me the key."
    "Finally the stubborn lock was defeated, and I nodded invitingly."
    me "Come in and be a guest."
    show un shy pioneer at center:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 2.5 zoom 1.15 xalign 0.5 yalign 0.5
    "I politely let the girl go first."
    hide un with dissolve
    scene bg int_house_of_mt_sunset with dissolve
    play music music_list["a_promise_from_distant_days_v2"] fadein 3
    play ambience ambience_int_cabin_evening fadein 2
    show un serious pioneer with dspr
    un "Here we are. What did you want to ask me?"
    "And I am silent. I smile as I look at her, frozen in the middle of the room, and I remain silent."
    me "Sometimes I think it's all just a dream."
    "The best dream ever."
    "About a person I've never seen in my life, but always dreamed of meeting."
    "For whom I came into this world."
    me "I don't want to open my eyes and realize I was just dreaming."
    "Okay, the usual fears within a dream, but there's more at stake here."
    "I would pray if I knew how. Ask all the possible Gods, Devils, Buddhas, Krishnas and the like for such an essentially small thing..."
    "It will blur beneath my eyelids the lost sharpness of the subject, the sweetness of the lips, the silver of the voice."
    "And one day I will forget who she is and what she means to me...{w} As it always does with my most magical dreams."
    "Except this dream...{w} has been haunting me since I was a child."
    th "Could she be the girl?"
    "Hardly. That one looks older, almost my age."
    "A short dress, a traditional Russian braid resting on her shoulder, hazel eyes, and a wary smile."
    "It could hardly be Lena. {w} To be honest, I can hardly imagine her with her hair like that."
    "I lowered myself onto the bed and nodded invitingly to Lena:"
    me "If you still want to help me, come here."
    show un normal pioneer close with dspr
    un "Do you want me to sit on your bed?"
    un "And what would the counselor think if she caught us?"
    "I only brushed it off."
    "Olga Leninovna is now sunbathing without a moment's respite and duking it out with the gym teacher."
    "We could make a fire on the floor and dance around it, covered in soot, and no one would catch us."
    "I grinned as I visualized the situation - a bonfire made of the counselor's diary and chairs burning in the middle of the room, with us jumping around it, all dressed up, disguised and disheveled."
    show un laugh pioneer close with dspr
    "Lena laughed when I shared my vision of the situation with her."
    un "Well... smearing soot and making a fire isn't necessary at all, but about everything else..."
    "She was teasing me!"
    "A discrete separation of platonic crush and healthy expected hormone play."
    "And I thought I had outlived that infantile feeling in me."
    "I guess that's why I got into the body of a seventeen-year-old pioneer."
    "To remember that there's more to it than crumpled sheets?"
    with fade2
    "At last she made up her mind and lowered herself gently to the very edge of the bed, balancing herself on the carcass bearers. {w}Dreamed!"
    "I immediately grabbed her in an armful and dragged closer to me in a sort of makeshift hammock sagging almost to the floor on stretched springs."
    "Lena squeaked softly in surprise and, realizing that nothing was threatening her, fell silent."
    "Fragile."
    "Gentle."
    "And, in her own words, all mine."
    $ set_mode_nvl()
    "And my thoughts wonderfully echo those of a person who decided to cheat the inevitable adulthood by taking a job as a counselor."
    "But you can't catch the slipping childhood  when you're in your thirties, under a mask of benevolence and polite attention you hide an all-knowing cynic."
    nvl clear
    "The heart strikes first."
    "It skips almost a beat when the gray-green eyes stop on you."
    "And you realize you don't want to grab the wearer of those eyes and spin her in an impossible waltz, don't want to grab her palm and run somewhere behind the departing sun and laugh with happiness overwhelming your whole being."
    "No."
    "Now you're thinking about the fact that you might have to move up your schedule a little so that you have at least an hour a week to hold hands - and God forbid the pioneers find out about it."
    nvl clear
    with fade2
    "And then it turns out that you have pioneers making out. And it's an emergency for which heads can fly."
    "And then that loses its meaning, too."
    "Some of them have parents who died in the putsch. Everyone knows that officer training, among other things, includes such an unpleasant clause as making their family and friends aware «that their son received a Hero Star. Posthumously.»"
    "And who would teach that to a counselor? In general, is there a school that would teach to look calmly into children's eyes and say: «Pavlik, you will take the common bus. No, Mom's not coming to get you. Mom's dead.»"
    nvl clear
    $ set_mode_adv()
    "I struggled to get out of the tangle of several layers of reality and stared at Lena."
    "She was sitting practically in my lap, hugging my neck with her palms, stubbornly staring into my eyes, as if trying to see something."
    "It's a good thing the «walkman» was on the other side - to crush it now would have been extremely stupid and hurtful."
    "And in a few seconds was presented to the public."
    me "It's a «walkman»... You can call it a portable turntable - it won't be much of a mistake."
    me "We're interested in its other function. {w}Recording."
    me "The microphone is not very sensitive - you'll have to be close by."
    "After poking around in the menu, I noted with displeasure that there was half a cup of charge left - two, maximum, three hours of playback."
    th "Well, I guess I won't get too excited."
    me "So..."
    play music music_7dl["iamsadiamsorry"] fadein 3
    "I began by turning on the recording."
    with fade2
    me "Give me today's date."
    un "The twenty-second of July, one thousand nine hundred and eighty-nine."
    "The girl rambled on."
    pause(2)
    me "Record zero, certifying."
    me "My name is Semyon."
    me "Hi. Just hi."
    me "I'm really embarrassed to say hi to you in the future, hugging the real you, but - I have to!"
    me "How are you doing? How's your mood? Do you remember what position we were in when this voice was recorded? My voice letter to you in the future."
    me "My kiss to you from the past."
    me "Love is measured by the measure of forgiveness, affection by the pain of farewell. {w}And hatred - by the strength of the disgust, with which you remember your promises."
    me "So what I promised, I do. {w}Further is your turn: will you succeed, and more importantly, will you keep your promises?"
    show un surprise pioneer with dspr
    un "What is it that I promised you?"
    me "What do you mean, have you forgotten?!"
    "The recording is interrupted at the girl's squeak."
    with fade2
    me "Record number one. The date is the same, half an hour later."
    me "Where were we? Yep, salutations from the past."
    me "Say hello to Lena, Lena!"
    show un smile3 pioneer with dspr
    un "Hi there!"
    me "I don't quite understand how this mechanism works, but if you open your eyes in a time objectively close to me, not a word from here will be a mystery to you."
    me "Although the present you are now staring at me as if I had suddenly grown a second head."
    show un shocked pioneer with dspr
    un "So you're from the future, then?"
    me "Everything is relative."
    "I smiled softly."
    me "From my point of view, I'm from the present. {w} And you are from the past."
    show un normal pioneer with dspr
    un "And what's it like out there in your present?"
    "My throat caught, and I tried for half a second to cope with myself."
    me "There's a lot of pain. Almost as much as indifference."
    me "And more than anywhere else, the law of «homo homini lupus est» is relevant."
    un "How can you complain, it's your home!"
    me "Simple to the point of banality. My home is where my heart is. {w}And my heart is where you are."
    un "Are you hoping there's another me there, too? The other me?"
    "For a moment, displeasure slid into her eyes."
    me "The answer is no - to all parts of the question."
    "If only it were possible to put my thoughts into someone else's head - I would show «Peter» from the heights of St. Isaac's, let me feel the smooth side of the wooden rose from the souvenir rows by the aisle at «Mars Field» and..."
    "How strange are the tattered memories thrown into my head in a pile where she is ubiquitous."
    me "I don't hope, I absolutely know, that somewhere in my city there is you."
    show un surprise pioneer with dspr
    un "W-what?"
    me "Come on..."
    th "After all, she might just not remember... Or just not have time to catch up with that time. Yeah, a thousand reasons."
    "I sighed."
    me "Find me. {w}Just find me."
    "I tore out a few sheets from the counselor's diary and in bouncing handwriting jotted down a series of addresses there, where I, if not known, could at least tell you where to find me."
    me "Here is all the information about me. All my background. Just dare to lose it."
    "I added the city, my own, my parent's and my grandmother's, the phone numbers I could remember, and handed the paper thickly covered in alphanumeric ligature to the girl."
    show un serious pioneer with dspr
    un "I won't lose it."
    "Lena replied, hiding the notes in her breast pocket."
    me "You'll be able to find me at night in e-max and vadis, where I try to find the eyes I dreamed of."
    me "And if you suddenly have a computer with Internet and Skype, write, call - I'll be glad:"
    if loki:
        me "simeon-loki. The first «s» is like a dollar, with a hyphen between the names."
    elif herc:
        me "simeon-sychov. The first «s» is like a dollar, you'll figure it out from there.."
    else:
        me "Mail or ICQ."
    me "It's here too."
    me "Please. Just show up in my life - there, outside the camp!"
    with fade2
    "I clicked the record key."
    stop music fadeout 3
    "All this time the player was diligently winding up megabytes of raw sound."
    me "I don't really believe in paper, so besides it, hold on to - here."
    "I'm not sure the girl realized what was going on when she saw that particular bar of «volkman» in her unclenched palm."
    un "And why?"
    me "A margin of safety."
    me "A kind of magical amulet that will go with you through whatever happens. {w}He survived the journey with me, so he'll survive your journey too."
    me "The main thing is, don't let it out of your hands and don't give it to anyone - you hear me? - Don't give it to anyone."
    un "But what about you then?"
    "I just brushed it off."
    me "It's just music. I'll get over it. {w}The important thing is."
    "It was too close:"
    me "- keep it close to you! Constantly. And..."
    me "Find me."
    play music music_list["everyday_theme"] fadein 5
    "I must have looked like a real psycho, because Lena nodded, hesitating."
    un "I've been promising this for two days now, but - okay. {w}I promise."
    me "Thank you. {w}It means a lot to me."
    "Someone came up the stairs on the other side and stopped at the door, flapping their pockets."
    "Lena jumped up and immediately moved to the chair next to the bed."
    me "Open!"
    play sound sfx_open_dooor_campus_1
    "The door opened, and she appeared to us. {w}A counselor."
    show mt normal pioneer at left
    mt "Semyon, are you loafing?"
    me "No, I'm not. I'm helping Lena make a plan to prepare for exams."
    mt "Oh yes, that's right."
    "The counselor sighed."
    mt "I completely forgot about her father's request this morning."
    mt "Since you're busy now, I'll let you out of some activities: cleaning, duty."
    th "Hooray!"
    mt "Bathing, dancing."
    "The counselor went on to list."
    "She went back to her locker and was looking for something there."
    "Apparently, there was no way she could have done it without making a bit of a mess! Naughty. Lazy!"
    show mt grin pioneer at left with dspr
    mt "And don't look at me like that! You'll thank me when you get straight A's."
    th "Aha-ha-ha."
    "I winked at Lena and pointed my tongue at the counselor's back."
    mt "Gather round, lunch is coming up. {w}And, Semyon."
    "Olga turned around abruptly, so I barely had time to put a serene smile back on my face."
    mt "You point your tongue in my back again, I'll rip it, got it?"
    "She winked and, apparently having found what she was looking for in her locker, left me and Lena alone."
    hide mt with dissolve
    stop ambience fadeout 6
    return

label alt_day4_un_7dl_library:
    play sound sfx_unlock_door_campus
    pause(1)
    scene bg ext_houses_day with dissolve
    play ambience ambience_camp_center_evening fadein 2
    show un smile pioneer with dspr
    un "Do you think she has a clue?"
    me "More than sure."
    "Snorted me."
    me "But she has nothing to incriminate us, so she'll interfere to the best of her nasty abilities."
    show un laugh pioneer with dspr
    un "You're funny after all... That's probably why I..."
    me "What?"
    un "Nothing!"
    "That woman's way of grabbing your hand and dragging you somewhere instead of answering!"
    me "I'll easily go with you anyway, if you tell me where you're dragging me."
    "I smiled."
    show un normal pioneer with dspr
    un "In case you've forgotten: we got a little hectic yesterday when we kidnapped me after lunch."
    un "Gotta make it up to you."
    "I didn't believe my ears."
    me "Are you going to make up with a buzzer?!"
    show un smile pioneer with dspr
    "Lena only smiled."
    un "No, it's up to you to put up with her... And for me, I understand, Shurik and Electronik have taken care of it."
    me "Anything you want for your money..."
    scene bg ext_square_day
    show un normal pioneer
    with dissolve
    un "You know, I was thinking yesterday... About what you said."
    me "I said a lot of things yesterday..."
    un "About not wanting to let go. {w}And, you know, at some point..."
    "Slowly, as if overpowering herself, the girl began."
    un "I got the creepy truth of what you said."
    un "We could really only be here because we were looking for each other. {w}And if we miss our chance, waste it on silly fighting and quarreling, providence will separate us and push us together no more."
    "Remembering my first failed one, I nodded in agreement."
    me "Yes, there may not be a second chance."
    show un serious pioneer
    un "But you also understand. If you push me away, hurt me, or at least let me know that you're not interested in me anymore, I don't know if I can handle it."
    un "I'm not scaring you in any way. {w}Just explaining..."
    "The purple ponytails jumped amusedly, not keeping up with the gusty movement of her head."
    "Lena turned away and glowed like a poppy flower."
    "Instead of answering, I pulled her close to me and gently stroked her head."
    me "I won't."
    "I spoke with a confidence I didn't feel."
    show un smile pioneer with dspr
    un "Imagine tomorrow is the end of the world - what would you like to do in time?"
    me "I'd like to wake up in the same bed with you."
    show un surprise pioneer with dspr
    un "H-how..."
    me "No, not what you think! {w}It's just that I like the idea of waking up with you by my side."
    "I suddenly caught myself thinking that I was freely blabbing my own hidden fetishes to - kinda - an unfamiliar, girl."
    me "And then... What if the end of the world got delayed? And then we'll have..."
    un "What?"
    "The girl moved with interest."
    me "I don't know."
    "I smiled lightly."
    me "A shared house in the suburbs and growing old together surrounded by beautiful children with purple hair?"
    show un cry_smile pioneer with dspr
    un "Damn tempter..."
    "She squeezed my palm so hard it almost hurt."
    th "Still, I've learned to appreciate what I have..."
    scene bg ext_library_day
    play ambience ambience_camp_center_day
    th "A buzzer's den."
    stop ambience fadeout 2
    play sound sfx_knock_door7_polite
    pause(2)
    mz "Open."
    play sound sfx_open_door_1
    scene bg int_library_day with dissolve
    play ambience ambience_library_day fadein 3
    show mz normal glasses pioneer at center with dissolve
    "The buzzer was sitting in the den, unfriendly, wiggling its bugles."
    mz "Why did you come?"
    th "Burn it! Burn her alive!"
    me "She's a passer-by, and I'm coming to you."
    "Zhenya looked at me like I was a patient in a fun house with yellow walls."
    mz "That's it. And what do you want out from me?"
    "Lena stepped aside, leaving me alone with the mean librarian."
    me "Anyway, I mean. Don't hold it against me for yesterday, okay?"
    me "I'm sorry. Didn't mean to and all that."
    show mz smile glasses pioneer with dspr
    "A smile transformed Zhenya's unfriendly face, and it suddenly dawned on me that she was, on the whole, pretty! {w}Even though she has the cavalierness of an army warrant officer."
    mz "Have you come to maaaaaake up?"
    me "Yes."
    show mz shy glasses pioneer with dspr
    mz "I wasn't really mad actually."
    "Success!"
    me "I'll go then?"
    "Overjoyed, I was about to take a step away."
    mz "Not so fast."
    show mz bukal glasses pioneer at center with dspr
    mz "Since you're both here."
    "Both? Somebody remembered saying that somebody there was asking something for him!"
    "There was something in her tone! Something eh!"
    th "Now we're going to be plowed."
    "With the desperation of a doomed man, I suddenly realized."
    mz "Will you help me?"
    th "And yet she's a buzzer!"
    mz "Head to the left. Left is where I point it."
    "She seemed to enjoy mocking people."
    "We followed the direction of her gesture and found a whole bunch of thick, black-bound books with gold trimming and the familiar embossing from our childhood."
    "The Great Soviet Encyclopedia. Second Edition, abridged. 50 volumes."
    me "And?"
    show mz normal glasses pioneer at center with dspr
    mz "Take everything off, wipe down the bindings and shelves, then put it back. Get to it."
    "Random sees, if this had happened under any other circumstances, I'd have sent her far, far away and explained how to get there."
    "But since we're kind of making contact here..."
    dreamgirl "And the bespectacled troll in the blue corner wins this fight by a technical knockout!"
    th "Thanks for the support, asshole."
    dreamgirl "Appeal, darling. {w} Reminder: it's still not too late for you to escape."
    "Mocking. {w}How can you live in a world where your own subconscious is mocking you?"
    me "Okay, so we wash the Encyclopedia and you don't pout at us anymore? {w}You promise?"
    show mz shy glasses pioneer with dspr
    mz "Honest Pioneer's."
    "She smirked and walked away."
    hide mz with dissolve
    "The bucket with warm soapy water was already waiting, and there was a dirty gray rag in it - apparently, the Buzzer was not tall enough to reach the encyclopedia from the floor, and for some inexplicable reason she did not want to climb on the stool."
    "The bucket wasn't very heavy: well, library work doesn't involve much physical exertion."
    "The specifics of working in the Soviet Union are that - you're not required to kill yourself and take weights bigger than you're actually able to push."
    "No, you're given twenty kilos, which you have to push from here to lunch."
    "And ideally, also in the afternoon - but that's, of course, if you want to work out an extra two-thirds for the legendary «five years in three years.»"
    "Picking up the bucket with one hand, Lena with the other, and pretending it wasn't the least bit difficult for me, I commanded:"
    me "Let's go!"
    "And off we went to conquer the Great Soviet Encyclopedia!"
    show un smile pioneer at center with dissolve
    un "I knew it wouldn't just work out that way."
    me "I really, really hope it didn't just happen, and that the damn exploiter..."
    mz "I hear everything!"
    "Zhenya's voice got to us."
    un "Well... It's our own fault: we shouldn't have yelled at her."
    me "I would have fought with her, too!"
    "I yelled in a wary whisper."
    show un laugh pioneer with dspr
    un "I love you!"
    pause(1)
    show un shocked pioneer with dissolve
    "It came to her belatedly - what she'd just said out loud."
    "First her cheekbones flushed, then the paint ran swiftly down her temples, taking over her ears as well."
    "Well, yeah, said a lot of things, and the most important word - it's embarrassing for some reason!"
    show un shy pioneer with dissolve
    "It's fun to watch, like the ignition of spilled gasoline."
    show un angry2 pioneer with dspr
    un "That's what you've done..."
    un "I'm going to be embarrassed of you now!"
    me "What, more embarrassed than you already are?"
    me "I thought it was impossible."
    show un laugh pioneer with dissolve
    un "Screw you... Let's go wipe the books."
    "I couldn't agree more."
    with fade2
    "Quickly dropping the books on the floor, we hastily wiped them down and assigned duties:"
    "I climbed on the stool and took books volume by volume, trying to arrange them in alphabetical order - praise the nomenclature and regulations of multi-volume publications!"
    "And Lena, as a short girl, stood on the floor and, acting as quality control in between, handed the books up to me."
    "Something of the history of the encyclopedia I remembered: it seemed to have been written for more than twenty years, and each subsequent edition tended to reduce the volume - in fact, whole paragraphs were thrown out of the education of the nation."
    th "And then a dullard with no education came to power and deprived the BSE of the attributes of a bearer of truth. And the only virtue of this dullard was that he took a place that no one else wanted, because it was cashless."
    th "The eternal story of Russia is that fools are in power because the smart ones have no time to raise their heads."
    "My hands got tired. I stopped and shook my head negatively in response to another outstretched volume."
    show un normal pioneer at center with dissolve
    un "Are you tired?"
    me "My arms are tired. It's too fast."
    un "Let me rub it out."
    "She shook her head invitingly - saying it was time to get down - but I recused myself."
    me "It'll go away, no need in that."
    un "At least look down at me when you're doing something over your head. It makes me feel good, and your hands won't get stiff."
    "I snorted."
    me "Thanks for the advice, of course. But if I don't watch where I'm putting the books, I risk getting a tome in the kump!"
    "Lena looked at me for a while, clearly contemplating whether to be offended by the harshness or forgiven, and then she nodded sharply and smiled."
    show un smile pioneer at center with dspr
    un "All right. {w}Let's get some rest then."
    "After putting the book on the floor, the girl let herself stretch out, and I remained standing on the stool, stretching my shoulders."
    "But just standing there like that, the restless pioneer girl was certainly very bored, so, stepping on her toes, she crept to the exit from behind the cupboards and looked out from there."
    "Catching my gaze, she raised her thumb."
    un "Asleep."
    un "Which means..."
    "I really didn't like the look in her eyes."
    if loki or herc:
        th "If she starts her tickling again yesterday, I don't know what I'll do!"
        th "I'll... I'll tickle her back!"
        "I giggled and twitched." with vpunch
        extend ", but no!"
        me "Lena! Don't you dare!"
        "Making scary eyes, I hissed."
        "That's how she obeyed."
        th "If I try to get off now..."
        "I thought, dodging the insistent fingers poking me somewhere in my kidney area."
        th "...I'm going to tip over and flatten the girl..."
        "And then I felt the chair slide smoothly out from under me!"
    else:
        "And a few seconds later, I really didn't like what she did."
        me "Ahahaha! Let go, psycho, it tickles!"
        "I yelled in a wild whisper."
        "I think it was easier to yell to Zhenya than to Lena..."
        th "And she's not bad at anatomy!"
        "And it's no surprise that I, standing on a walking stool, ended up quite logically and predictably!"
    play sound sfx_chair_fall
    with vpunch
    play sound2 sfx_bodyfall_1
    pause(1)
    stop ambience fadeout 2
    play music music_7dl["take_my_hand"] fadein 5
    scene cg d4_un_7dl with dissolve
    "I flew down with a bang, pushing Lena under me in the process."
    "Gravity today is... Odd."
    "I lay there for a fraction of a second, enjoying the situation, the position, when she was finally close, close - under me."
    "She was looking up into my eyes from below, and as on the first day I couldn't, wouldn't find my way out of those bottomless eyes belonging to - well, who would have thought - a fragile young girl."
    "Thoughts lined up in queues, jumping out of the depths of my mind with disconcerting images."
    th "Lena. {w}Close."
    th "I think I flattened her."
    me "How are you?"
    "I'd be embarrassed if I could. {w}To the side, I'd help the girl up."
    "I could hear her heart beating so fast from here."
    un "Semyon."
    un "You're too close..."
    me "Is there a problem with that?"
    un "I need some air..."
    "She bit her lip and looked me defiantly in the eyes."
    "And I fell silent. We fell silent."
    "If coming to a strange place, we meet a charming stranger who needs only our silent approval and a little bit of participation."
    "If that stranger becomes the very meaning and purpose of life in a matter of twenty-four hours."
    "Can we call it fate? Or was it just coincidence that we found each other at camp?"
    $ set_mode_nvl()
    "Before my eyes, eclipsing the light but not hindering my enjoyment, a film chronicle of the events unfolded at great speed."
    "There was no way they could have happened, but I remembered them more clearly than my own name."
    nvl clear
    "The first decade of February, the first hints that winter can't last forever."
    "And I, returning from another 24-hour layover, get pumped up on cheap booze and, howling at the inadvertent loneliness, hole up in my notebook."
    "Turns out we have a lot of friends together. {w}But only one of them hasn't had time to successfully marry, have spinsters, and grow old, thereby remaining as if he were still part of our circle of twenty-five-year-old pranksters."
    "It's evening, February, just a little bit before Valentine's Day, which I never celebrated and never intended to, and then... She."
    "I practically immediately took her to my lap, and, despite all the screams of the host that the guest is supposed to be dancing and having fun - didn't let her go."
    nvl clear
    "And then..."
    "Then the usual long, long walk to the subway, marred by the fact that we, drunk and laughing, walked around in circles until about 1 a.m., and only managed to get our bearings after asking a twitching passerby for directions."
    "The subway ride - I'm standing on the escalator one step down, leaving our eyes aligned."
    th "You know how helpless I am against green eyes, don't you?"
    th "You know you can't build anything with what we have now."
    un "I don't care. Come closer to me."
    un "You're so good."
    "In one voice says the vision girl from my half dream and the girl lying beneath me."
    "We just went crazy. It's like putting the whole world on pause and forgetting, forgetting that there are opinions of those around us, there are those who think we belong to them. An icy February, a cold March, a dank April, a chilly May..."
    "All the way to November we lived a lifetime without separating the palms of our hands."
    "She kissed my cheeks, my eyelids, my eyelashes, ignoring the fact that there was a whole big world out there, and there was someone waiting for us outside the frame."
    $ set_mode_adv()
    me "It's you... You're good."
    me "And we're just crazy."
    "I can hardly keep from saying a few words, after which things usually get too complicated."
    "That's why I don't say anything."
    me "Let's get up."
    "I tried to roll away to the side, but the girl protested and pulled me to her side, resuming what I'd started."
    "It looks like she's having a good time as it is. And she doesn't care if we get caught here."
    th "Apparently..."
    "Maybe we should just spit on everything and take what we're given while we have the time."
    stop music fadeout 3
    play ambience ambience_library_day fadein 3
    mz "Finish kissing - finish cleaning up and go to lunch."
    scene bg int_library_day with dissolve
    stop sound fadeout 2
    "Looks like we woke up the librarian after all."
    show un laugh pioneer at center
    "The princess laughed, happy and surrendering to happiness all the way - as well as to everything that fascinated her."
    show un smile pioneer at center
    with dissolve
    "This time she didn't hold me down, and I was able to get up myself and help her."
    me "There, my arms rested too."
    show un laugh pioneer at center with dspr
    un "So let's just finish up here and go make up with Zhenya."
    me "What's that for?"
    "Lena looked at me with infinite patience:"
    un "We came to make up with her, right?"
    "I nodded."
    un "And you, I remember, were going to help me?"
    me "That's right, too."
    show un normal pioneer with dspr
    un "Well, what are you doing then? {w} She has a spare key to the library and the newsroom, so-"
    "She stopped talking halfway through."
    "She winked at me."
    un "Will you continue?"
    "Here, of course, she caught me - I bounced my fist, and nodded obediently."
    me "De-al. Let's finish up here and go lick your Zhenya."
    "Lena only shook her head."
    with fade2
    "We worked for another quarter of an hour, and the last volume, number «50» took its place at the same time as the horn sounded."
    me "On the job - and the reward!"
    show un smile2 pioneer with dspr
    un "Exactly."
    "The buzzer couldn't find anything to complain about - even though it took us longer to cuddle in corners than to actually work, we did everything good enough. {w}And that means admission to the library, the key, and the favor of the librarian was guaranteed."
    "Morning's a success!"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day4_un_7dl_dinner:
    play music music_list["eat_some_trouble"] fadein 2
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 5
    "Lunch went by somehow suddenly and at once."
    "Despite the apricot rice soup and lazy cabbage rolls handed out today, we rushed to finish lunch as quickly as possible: there was so, so much to do."
    "And high on the list was spending time together."
    if alt_day4_me_neu_transit == 'un_7dl':
        me "Do you have any plans?"
        "Lena hesitantly squinted at the counselor, then shifted her gaze back to me."
        show un shy pioneer with dissolve
        un "There are..."
        me "What kind?"
        un "Y-you..."
        me "Sounds good! Look, I don't remember everything, but the fact that the best company is yours, I know for a fact!"
        me "So finish with your shyness, I'm not going anywhere."
        "The girl lowered her eyes."
        un "T-thank you, by the way."
        me "For what?"
        un "For playing along."
        "Lena nodded toward the counselor."
        un "She would have kept up."
        me "You're welcome. But I didn't really understand what that question was about."
        show un smile pioneer with dspr
        "It was as if Lena had experienced something in her head. She smiled and looked at me."
        un "It doesn't matter now."
        "Well, I won't spoil the mood with silly questions."
        me "Okay. So where are we going?"
    else:
        me "Not so fast, pretty girl!"
        "I held Lena's hand as she finished her meal and tried to get up and run somewhere else."
        me "Let's decide first: where shall we go and what shall we do there?"
        show un serious pioneer with dspr
        un "And I thought we had already decided..."
        me "And yet!"
        un "Well..."
    "She looked at me."
    if loki:
        if alt_day4_me_neu_transit == 'un_7dl':
            show un shy pioneer with dspr
            un "W-well, I thought I'd show you my drawings..."
        else:
            un "You were going to look at my drawings, you didn't change your mind?"
            me "Not at all! It's just... You know, I thought we had more time."
            me "And it's only three days... You know?"
        show un grin pioneer with dspr
        "The pioneer girl flashed a fleeting smile - a triply valuable one, because I was now absolutely certain she didn't smile like that for anyone else - and stood up."
        un "Come on, let's go see what I've been up to."
        "Well, who, you ask, am I to refuse such invitations?"
        "Of course I nodded, and of course I let myself be carried away toward the cabin that Lena shared with Miku."
    elif herc:
        if alt_day4_me_neu_transit == 'un_7dl':
            me "I hear you draw. I could pose!"
            "I blushed."
            me "If you want, of course."
            me "I hear they draw in art schools..."
        else:
            me "I remember you asked me to pose..."
            "I blushed."
            me "Let's just say... In my natural state."
        show un surprise pioneer with dspr
        un "And you agree?"
        me "Let's just say, under certain conditions, I'm all yours. I promise."
        un "Promise?"
        me "What can I do with you... I promise, of course."
        un "Therefore... {w} seize the moment."
        show un laugh pioneer with dspr
        un "As my lord says..."
        "I think I've found a party to my liking... Someone I won't want to push away, even if it gets really bad."
    else:
        if 'nwsppr' in list_clubs_7dl:
            me "You mean the ill-fated article?"
            show un smile3 pioneer with dspr
            un "You have to prove there's a reason you were hired for the newspaper."
            "She smiled charmingly, and I could barely keep from kissing her right there in the canteen."
            me "Okay, an article is an article. {w}But will you walk with me?"
            show un laugh pioneer with dspr
            un "Yes, I'd love to! {w}Where do you want to start?"
            me "With Miku. She's in charge of that part - that's where we'll go."
            show un smile pioneer with dspr
            "Lena smiled and confirmed my decision with a vigorous nod."
            un "Well? Godspeed?"
            "And we headed out."
        elif 'badmin' in list_clubs_7dl:
            show un smile pioneer with dspr
            un "Have you forgotten? We're both signed up for badminton. Today is an even number, which means the tennis players are resting and we're playing."
            me "That's right! So we have the box all to ourselves?"
            show un smile pioneer with dspr
            un "And don't even think that I'm going to give in to you!"
        elif alt_day4_me_neu_transit == 'un_7dl':
            me "How about we play something then?"
            show un laugh pioneer with dspr
            us "Like what?"
            me "Uh..."
            "I looked around lost, and then it hit me:"
            me "How about we continue our badminton practice?"
            "After thinking about it, Lena nodded."
        else:
            un "I don't know about you, but I'm going to go out for a shuttlecock."
            "She glanced over her shoulder at me."
            un "How's about that? With me?"
            me "What a silly question. Of course I'm with you!"
    stop ambience fadeout 2
    stop music fadeout 2
    return

label alt_day4_un_7dl_day_loki:
    play sound sfx_door_squeak_light
    scene bg int_house_of_un_day with fade2
    play ambience ambience_int_cabin_night fadein 3
    play music music_list["confession_oboe"] fadein 3
    show un normal pioneer with dspr
    "Upon entering the house, she immediately sat down at the table and began to go through the sheets of wattan, as if choosing what to show me and what not to show me."
    "To my presence, as if it were something inconsequential, she paid no attention at all!"
    me "Let me guess, your bed is on the left?"
    "I walked over and plopped down on said bunk: carelessly tucked in, with a huge fancy suitcase with wheels and a pair of slippers of Lena's favorite color, blue, peeking out from under the shell."
    "What really gave her away was that there was no aquamarine hair on the pillow! {w}Judging by the preliminary analysis, both of the housewives in the house were some kind of slackers!"
    show un scared pioneer
    un "Ouch!"
    "She almost jumped up in her chair in surprise!"
    un "What are you doing?!"
    me "Since it's your bed - so I can lie on it!"
    if alt_day4_me_neu_transit == '':
        extend " You were lying on top of me in the library."
        show un shy pioneer with dspr
        un "Actually, it was you who was lying on me..."
    "She looked through something quickly, culling it, putting it back on the sled, and smiling approvingly at some of it and putting it in a smaller pile-apparently where the pre-screened papers were located."
    if alt_day4_me_neu_transit == '':
        me "You on me or I on you - what's the difference. You know, I wouldn't mind if you were on me, too-"
        "I giggled nervously as I imagined Lena, enlarged to compete in the weight class by about half her size, lying on top of me and sputtering to the floor."
    show un smile pioneer with dspr
    un "You're looking at me again like you've seen me before."
    me "Maybe I saw you in a dream?"
    me "Or met you in a past life?"
    if persistent.un_7dl_good_rf or persistent.un_7dl_good_ussr:
        call alt_day4_un_7dl_hentai
    else:
        un "Then I saw you, too."
        "She grinned - very mature somehow."
        un "The longer I've known you, the stronger the feeling in me that we've seen each other somewhere before."
        un "And my feminine intuition tells me that such feelings are not good."
        me "How harshly put! A woman's intuition!"
        "Lena poked her tongue at me."
    scene bg int_house_of_un_day
    show un grin pioneer with dspr
    play music music_7dl["take_my_hand"] fadein 4
    un "Now can we finish what we came here to?"
    me "We came here to spend time together, didn't we?"
    show un normal pioneer with dspr
    un "I thought about showing you some of my work, but if you're not interested..."
    "Man, what am I thinking of anyway!"
    if persistent.un_7dl_good_ussr or persistent.un_7dl_good_rf:
        me "No, honey, of course I'm interested. {w}It's just that after doing some things, it all slipped my mind."
        show un laugh pioneer with dspr
        un "Well... I hardly remembered it myself."
    "Nothing happened for a while, Lena paced through the works and picked out the ones I could see, separating out the ones I wasn't allowed to see."
    "The forced downtime was approaching ten minutes when a sudden sharp gust of wind, which dived through a window that had been opened because of the heat, tore her drawings out of her hands and scattered them evenly on the floor."
    show un surprise pioneer with dissolve
    un "Uh, what's wrong..."
    "Wailing, she squatted down and, with goose-steps, began to pick up the scattered treasures of fine art."
    un "How bad timing is all this: now everything will get dirty!"
    "And I would have helped her, but I was busy: holding a picture in my hand - another picture from the past."
    "The paper pelted my face, and as I took it off, I immediately noticed the incredibly realistic rendering of the image."
    "Here's a boy pounding his fists against the glass, and in the reflection you can see a crumbling airplane: pure graphics, no colors, conveying one word: grief."
    "Here's a boy and a girl climbing a tree and stepping from the branch straight into the void. It's a dream."
    "Here's a man in a ski jumpsuit sitting with his back against a Genda pedestal, his nose bleeding. Another dream."
    "And that's just what I managed to catch."
    "Here and there on the floor you could discern impossible, unbelievable pictures that I had never seen - and yet I knew them!"
    me "Len..."
    "The fear was cold."
    me "Is this all from your past? Or dreams?"
    me "I could have sworn there was definitely no airport in your town."
    show un shy pioneer
    un "Dreams..."
    me "So... And even -"
    "I twisted the name on purpose:"
    me "Spruce Glade?"
    show un angry2 pioneer with dspr
    "Measuring me with a condescending look, Lena dropped:"
    un "What's Spruce when it's Pine!"
    show un shocked pioneer with dspr
    un "Oi!"
    me "Aha. {w}You must have been dreaming about it, too."
    show un normal pioneer with fade
    "There was silence for a few minutes while we picked up her artwork from the floor, and Lena was careful not to look in my direction."
    "Pressing the girl now would be... unwise."
    "But I couldn't help myself."
    "My head was cracking: the memories of two, if not three, lifetimes as long as mine were comfortably housed in it."
    th "It's like it all started a bunch of years ago, when I was led by the hand to my first class, and our gazes crossed."
    th "And she went away for treatment a year later, and then our family moved out. {w}And we never, ever saw each other again."
    "But I remember the dark hair, the head too big for such a fragile figure, and the huge eyes, combined with the funny ponytails that made the owner look like a certain anime character."
    "Or maybe that's what it was all about. I, unsteady on my feet, after a twenty-four-hour ferry ride and a liter of vodka, which came only to me - and the whole carriage was humming! - I'm shitting on an unknown platform in an unknown city, and she catches me by the elbow in the underpass."
    "Grown-up, impossibly beautiful, in her bloody spacesuit - and I want to pull back the hood and let out her dark, purple hair."
    "I'm shaking all the way, and even when she sighs happily at the streetcar stop and rests her head on my shoulder, I can't let go of the jitters."
    "Come on, that's not how it was at all! {w}I've told you before! And about Pine Glade, and the piles of leaves, and the chestnuts and the running with the streetcar."
    me "It seems to me: I've known you longer than a lifetime."
    me "And so I won't ask how you know that Spruce Glade is really Pine Glade."
    me "And why aren't you surprised when I talk about how I would warm your hands in my pockets - in my memory, no girl has yet to resist trying what it would really be like."
    "I sighed."
    if (alt_day2_convoy == 'un'):
        "This conversation leads nowhere, and if yesterday or the day before yesterday I would not have chosen Lena as my escort, who knows, maybe I would now be torn with conflicting memories of someone else?"
    elif (alt_day2_convoy == 'sl'):
        "Even though the golden-haired girl became my escort, and, filled to the brim with her, I even saw her image in my dreams, she never became what Lena had become."
    elif (alt_day2_convoy == 'dv') and (not alt_day2_us_escape):
        "And I did my rounds of the camp with the redhead, and I even dreamt about her. {w}But for some reason I have no half-forgotten memories of her in my mind."
    me "Can you paint my portrait?"
    me "I'm not likely to hold still for the necessary amount of time, but..."
    show un grin pioneer close at center
    un "Spin all you want... I've got you firmly in my mind."
    "I was taken at gunpoint, Lena studied me over the pencil in her outstretched hand, sternly and unsmilingly."
    "A white piece of cotton paper was already waiting in her lap, and I was already curious as to what she would depict."
    "In the scope... Or in the viewfinder?"
    show un smile pioneer far with dissolve
    un "I warn you at once: it may get very strange. {w}I'm just removing unnecessary places on paper, and what's left..."
    "...is me."
    th "I get it already. I also read about Michelangelo Buonarroti."
    "She took one look at me - and then went deeper into her drawing. {w}I guess saying she remembered me VERY well wasn't that far from the truth."
    "Slightly slouching, shoulders slumped, she covered her eyes, sketching fluently across the white surface with her lead, working at once for sure, cleanly, using no guides or anything like that."
    "And for some reason I believed at once that it would turn out at least not bad. {w}The most trivial of all, it's the most trivial of miracles."
    "Except it could have been a little less time-consuming."
    "Half an hour later, I got bored and silently rose from my stool, walked around Lena's perimeter and peered over her shoulder."
    "My neighborhood. Familiar places where I used to rollerblade, walked around a lot, and as a result..."
    "Limited myself to the cigarette stand?"
    "An unusual angle, as if from somewhere above, showing snow-covered five-story hruschevkas something... beautiful?"
    "And just below the focus you could make out a slouching figure in either an overcoat or a jacket and baggy winter Burton's with the invariable torch across her chest."
    "She shrugged her shoulders helplessly."
    un "I see you like this..."
    me "Fantastic..."
    "I'd hardly be more surprised if she drew my den where the only source of light is the eye of the monitor."
    "And as if confirming my fears, Lena smiled."
    un "Although I wanted to draw you sitting in your underwear by the TV first... No, it's not a TV, it's called something else."
    me "Monitor?"
    show un surprise pioneer
    un "Exactly."
    show un smile pioneer with dspr
    if alt_day3_un_strip_pool_sp > 1:
        un "But I realized that I'd never seen you naked, so I might be lying about your proportions."
        th "Actually, partial nudity is enough for other artists."
        "But I didn't really focus on that."
    "I hope she's not hinting at anything right now?"
    me "If you want me to strip, you have to ask differently!"
    "I blushed, but kept the game going with all my might."
    un "No, I guess not. {w}We'll get busted anyway if they catch us here."
    if alt_day4_me_neu_transit == '':
        me "Then what about supposedly preparing for exams?"
        me "We were exempted from everything - from activities, from bathing - from everything!"
        un "Yeah? Do you see a lot of textbooks here?"
    play sound sfx_paper_bag
    "She finally finished the drawing and handed it to me."
    if alt_day4_me_neu_transit == '':
        "You didn't have to ask about that."
        me "And we'll say we ran through what we remembered during quiet time."
        "Disbelief was written all over her face."
        un "Yep. {w}And how much do you remember from your high school algebra curriculum?"
        "My hand reached for the back of my head on its own. {w}Although it probably would have been more appropriate if it had reached for my face."
        "I graduated from high school over ten years ago - nothing but X's in my memory at all... Even in spite of the damn medal... Which, by the way, was never useful to anyone."
        me "Honestly, I don't remember anything at all."
        me "But I think the counselor remembers even less."
        "Look at her face, she's a pure humanitarian."
        show un shy pioneer with dspr
        un "Okay."
        "She jokingly wagged her finger at me."
        un "But you'll improvise on your own!"
        dreamgirl "Don't worry, sine over cosine - we'll think of something."
        dreamgirl "At the very least, we'll mess with her head by solving quadratic equations."
        th "Do you remember the formula?"
        "I respectfully asked."
        dreamgirl "Uh... No. But there's definitely something with the root, as long as there's a root, and then we'll get through it."
        th "Hollow memory, other people's memories, zero information about the school curriculum, and, to top it off, a handicapped split personality. {w}Doctor, get me out of here! And give me some delicious square pills!"
        me "I'll improvise!"
        show un serious pioneer with dspr
        un "Really?"
        un "Can you handle it?"
        me "No."
        "Disconcertingly honestly, I admitted. I guess I'll have to sit with the books for a while after all."
        show un surprise pioneer with dspr
        un "But you..."
        me "I'm just being sober about my own chances and knowledge."
        me "Anyway, I'm going to have to stop by the buzzer's place. We're kind of friends now, aren't we?"
        th "So now we get up and move smoothly toward the storehouse of knowledge."
        play sound sfx_7dl["eat_horn"] fadein 1
        un "Maybe after lunch, huh?"
    un "It's time for something to chew on!"
    un "But in case you're too lazy to go to the canteen, they brought me something there..."
    "I'm at summer camp and the girls are feeding me from the parents' supplies!"
    me "Forget it! You've been brought something, you need it more."
    th "If I were to visit you in town, I'd make you jump at the stove, of course."
    th "Why not?"
    stop music fadeout 5
    stop sound fadeout 4
    stop ambience fadeout 2
    return

label alt_day4_un_7dl_hentai:
    scene bg int_house_of_un_day
    show un smile pioneer
    with dspr
    play music music_7dl["iamsadiamsorry2"] fadein 3
    $ alt_day4_un_7dl_hen1 = True
    "She froze, as if doubting, and I reached out my hand and drew her to me."
    me "Closer, darling... Please..."
    show un shocked pioneer at center with dissolve
    un "I'm sitting on top of you, how much closer do you want to get?"
    me "Trust me, okay? {w}You'll like it."
    me "And if you don't like it, we just won't go back to that moment. {w}I promise."
    "With a sigh, she lifted herself up and, carried away by the movement of the hands, climbed up me, sitting her hips on my shoulders, close-to-close, within breathing distance."
    "Vulnerable, desirable, trusting, irresistible... I wanted her to scream and fight and thrash and cringe."
    un "And then what?"
    me "And then..."
    "I said huskily, running my fingers down the side of her panties and exposing one of the most secret places on a woman's body to view and caress."
    "I wanted her to get off. In the very sense that there has been for as long as humanity has existed."
    un "W-what are you doing..."
    "She reminded me of some kind of animal, as if caught by the tail, suddenly stroked instead of kicked."
    un "Stop..."
    show un shy pioneer at center with dissolve
    "Whatever she was thinking, it's unlikely she was contemplating something like this."
    me "And then, from here on in, we'll do this."
    "She wanted, to the point of swallowing and growling wretchedly, not at all what I had in store for her."
    me "I wanted to do this..."
    me "And this..."
    "I wanted to make her feel good."
    "She would surrender to me - all of her, opening under the caresses, impossibly close, shuddering under the touches of the tongue as under the strokes."
    "And then... The image went in separate frames:"
    "A coarse shudder all over my body."
    "A body, against its will, sagging like a predator."
    "Moaning."
    "Fingernails digging painfully into my legs."
    scene black with fade
    pause(5)
    with dissolve
    stop music fadeout 3
    "She must have had something to say."
    "She even filled her chest with air."
    "But after a moment, she closed her eyelids and fell asleep peacefully."
    "Sunshine."
    "I don't know how long I sat like that, guarding her sleep, but she must have regained her strength and finally stirred and opened her eyes, wet with a twist."
    scene bg int_house_of_un_day with dissolve
    pause(3)
    show un normal modern with dissolve
    un "Hi…"
    "I smiled back."
    un "You know: I had such a dream..."
    show un shy modern with dspr
    un "There you and I..."
    "Her blanket opened a little, and I couldn't help myself from..."
    show un normal modern with dspr
    un "W-where are you wa... Oi."
    show un shy modern with dspr
    me "I suppose there's no point in talking nonsense about it not being a dream anymore?"
    un "You bring a new surprise every day."
    "She quickly cleaned herself up, and we didn't really take anything off her except her tie."
    "And put her feet down on the floor - except for the uncharacteristic blush on half of her cheeks, which was not her beautiful pale skin, she was perfectly ordinary."
    show un sorrow modern with dspr
    un "One minute you're allergic to latex, and now this..."
    "She involuntarily lowered her eyes in a known direction and blushed again."
    me "And this, too."
    "I handed her the camouflage petal, and she tied it with nervous, twitching motions."
    show un serious pioneer with dspr
    un "Yea, thanks."
    return

label alt_day4_un_7dl_day_herc:
    scene bg ext_library_day with dissolve
    stop music fadeout 2
    pause(2)
    play sound sfx_door_squeak_light
    scene bg int_library_day with dissolve
    play music music_list["what_do_you_think_of_me"] fadein 3
    show un normal pioneer with dspr
    menu:
        "Completely naked or...":
            $ karma -= 10
            show un grin pioneer with dspr
            un "Unless you really want to."
            "She looked at me slyly."
            un "You want?"
            "My cheeks flamed up again - I can't play the cool guy."
            "How funny it is when you have a wise-ass, slightly cynical and totally unbreakable voice sitting inside you, and you're embarrassed, embarrassed and blushing before you know what's even going on."
            me "You won't believe!"
            show un laugh pioneer with dspr
            un "Well, if you don't want to, just drop your shirt and sit down somewhere so I can remember you."
        "Without asking silly questions, take off your shirt":
            $ lp_un += 1
            "The tie was a little tangled - as it always is, though."
            "But the buttons, as if greased, popped out of their loops as soon as I touched them."
            "Now my shirt was on the table, and I grabbed my belt..."
            show un smile2 pioneer with dspr
            un "You're determined! No, you don't have to take your shorts off."
            un "Just torso is enough, or I'll be distracted all the time."
            "I smiled and sat down on the stool."
            me "I hope no one catches us here... I know some overly chatty individuals with excessive imagination."
            show un serious pioneer with dspr
    "In general, it's a strange feeling to be drawn from life."
    "I don't know what to compare it to. {w}Except the process of getting a passport."
    if dr:
        "I can't even remember now why we went to London, whether it was for a contest, a concert, or maybe a little of both."
        "Even now I try hard not to remember what that trip turned into - a fight and rain that was eerily indistinguishable from the drizzle in the air of my hometown."
        "The other thing is the biometric passport photo, when you have to straighten up so that your hypertrophied ribcage seems about to crack in half and your shoulders fall the hell off."
        "And those stupid crosses you have to look at when you're filming to get that «in focus» look."
        "What's the focus - if they're close to each other, and you have to squint your pupils to keep both in the field of view, the result is a frankly bad image that shows my progressive strabismus in the photo. {w} Ugh, man."
        "And so at customs, before I was allowed to go to the duty-free shops with a throwaway price for Beefeater, I was pestered for fifteen minutes, refusing to believe that I was me."
        "So what if I didn't shave before photo, then what? It's a free country, I can wear stubble as long as I want!"
        "Then a similar situation at Heathrow, where I met a Russian-speaking officer (yes, I broke my patience and began to speak exclusively in Russian swear words!) with already beveled pupils and an offer to hold me at the checkpoint for fourteen hours, to get the stubble through"
        $renpy.notify('«Crosses» - Local jail in St. Petersburg.')
        "It's a good thing my current appearance doesn't depend on such nonsense. Though I suspect I'd have to dodge «Сrosses» exactly the same."
    "Lena was drawing quietly, not distracted by the chirping of cicadas from outside the window and the distant cries of little kids from somewhere square-side."
    "She was studying me, and I was studying her. As is always the case in these situations, both are always to blame."
    "Guilty of not closing the gates and bristling with spades from the loopholes, of detachment and frostbite."
    "And in such a situation, any non «can't» automatically means «can»."
    "The first impression, the first glimpse, the first half-hour together."
    un "When you're done undressing me with your eyes..."
    "Without lifting her eyes from the sheet, Lena asked."
    un "...turn the other way, please."
    "I blushed."
    show un laugh pioneer with dspr
    me "I didn't..."
    th "How does she know?!"
    un "The look in your eyes is palpable simply. {w}Heavy and hot."
    "I turned away diligently and stared at the posters on the walls."
    "Lots of Lenin, Stalin, and absolutely idiotic slogans along the lines of «long live first of May» everywhere."
    "Morons, it's a date! Or what, we don't wish it health and the whole day is gone from the calendar?"
    "Or else we wish her happiness, prosperity and globalization."
    "You're damn crazy!"
    "Globalization is the integration of a country's strength into the world market."
    "How delightful! Forget intellectual potential, culture, minerals, we'll plow the country and sow everything with potatoes!"
    me "Still, it's no surprise that ours, our very own political engineers went to the States to read articles on the beginnings of targeted marketing."
    show un serious pioneer at center with dspr
    un "What?"
    me "Can't you see? Double-bottomed, triple-bottomed posters, slogans that seem normal to you, but in fact call for the smashing of dissenters."
    show un surprise pioneer with dissolve
    un "What are you talking about?"
    "I shrugged it off."
    me "Look at it yourself - the design, the execution, the aggressive colors, the appeals with an open undertone."
    "I poked my finger at one of the posters."
    me "Pioneer! Learn to fight for the cause of the working class. Do you feel the trap?"
    un "N-no... But."
    "I raised my eyes to the mountain."
    me "Can't you see? {w}You're required to learn to fight for some mythical working class cause."
    me "That means all it takes is one red-tongued schemer who can say he knows how to do the right thing, make logical justifications for, for example, the lynching of Central Asians."
    me "And that's it. Millions of spirited young men with fire in their eyes, piously sure they're right, hunt him down and hang him from the nearest lamppost."
    show un normal pioneer at center with dspr
    un "Well..."
    me "That's how the Komsomol orgs. and deputies managed to turn a man into a cog in love with the mechanism. And that's not propaganda anymore..."
    me "It's religion."
    un "So you're... this... dissident?"
    show un smile pioneer with dspr
    un "I had never seen a living dissident before."
    if alt_day4_me_neu_transit == '':
        me "Regarding you, I'm from the future, remember?"
        me "Have you ever read any Russian folk tales? About Svyatogor's dying breath, which Muromets refused?"
        "Waiting for a nod, I continued."
        me "The dying colossus, the most powerful system of Soviet education, no longer bound by shors and propaganda, poisoned all of us - those who studied at the time of the system's fall - by endowing us with an abiding longing for something that never was and never will be."
        me "We have been given great power to see things as they really are."
        me "The trouble is that this power, like every other gift of a dying Union, was dead, and could not produce anything viable."
        show un serious pioneer with dspr
        un "You were right: your world is a nightmare."
        "Tearing herself away from her drawing, Lena said."
        me "I warned you."
        me "And that's why I'm enjoying this time: the summer, your company, and the atmosphere of kind of stagnation, blissful ignorance, and down-to-earth happiness."
        me "Although the first McDonald's in Moscow City is going to be built in six months, and people will go there, just like they used to go and want to go to pastry shops."
        me "Celebrate birthdays with a bun with a cutlet of dubious quality and a soda more suitable for dissolving your teeth enamel than for actually eating."
        me "The world will be pointing the finger at us for years to come as we, wearing our fanciest jeans and pullovers, line up in lines for miles to get our hands on french fries and chicken McNuggets."
        me "It's a good thing this is a relative province, though, and the general hysteria of Westernization won't reach the local townships for a long time."
        show un sad pioneer with dspr
        un "So what do we do now?"
        "Asked the girl, looking over the edge of the paper."
        un "It's bad over there. {w}We'll soon be bad here, too.{w} Where's good then?"
        show un smile pioneer at center with dissolve
        un "Ah, I've got it!"
        me "What?"
        "Lena impolitely poked me with an eraser on the unsharpened end of a pencil."
        un "Let's do «good» where we are."
        me "That's what I think, good is where you are."
        show un surprise pioneer with dissolve
        me "I try to keep myself in line."
    me "By the way, how's it going?"
    "She just waved it off - say, go on with your babbling."
    show un smile3 pioneer with dissolve
    un "I'll finish - I'll show you!"
    "I sat back, wondering what else we could talk about."
    "The moment the girl drew, she loosened up completely, discarding unnecessary shyness, thoughtfulness, and absent-mindedness."
    "And I honestly didn't even know what sauce to use to get deeper into her soul in the moment of her maximum openness."
    "And did I want to? It always seemed to me that in any person must remain a bit of reticence, otherwise he quickly becomes uninteresting."
    "But there was still one topic that was important to couples of all ages. {w}Exes."
    me "Lena, let's play a game, shall we?"
    show un grin pioneer with dissolve
    un "Which one?"
    "The pioneer girl inquired, without taking her eyes off the paper."
    me "There's a game, though it's usually played in a larger group, but since we have a mutually interested group of two here..."
    me "The game is called truth or dare. {w} The rules are simple enough - there are two boxes: one with truth and one with wishes."
    me "You take a dime out of the truth box first and answer the question as truthfully and honestly as possible."
    show un sad pioneer with dspr
    un "What if I can't or won't be able to answer the question correctly?"
    me "So you pull a dime out of the wish box. {w}It's simple."
    "After hesitating a bit, she nodded."
    un "Okay, let's try it."
    "We cut up a blank sheet of paper and began to think of what tricky question we could ask the other - or wish."
    un "Can we wish for anything?"
    me "Within reason, of course."
    show un shy pioneer with dspr
    un "Then oops..."
    "She crumpled one of the wrappers and began to write the next one."
    "Finally the minimum supply for the game was made up, and after scattering the papers into boxes, we began the process!"
    "The first forfeit caused no difficulty, and after a jaunty questionnaire drew us both in."
    "{i}Is your heart free?{/i}"
    show un grin pioneer with dspr
    un "No, it's not."
    un "Your turn!"
    "It wasn't hard for me to answer either."
    me "No, not free. Next!"
    "{i}Do you love anyone?{/i}"
    show un shy pioneer with dspr
    un "Wish!"
    "I nodded encouragingly at her wish box."
    "After thinking for a while, she reached into the box, grabbed a paper and unwrapped it."
    me "Well, what's in it?"
    un "Take one thing off, any."
    me "So take it off! Shoes, for instance. Or, there's a tie."
    "She took my advice and, remaining barefoot, put her feet under her and nodded encouragingly."
    un "Now you."
    me "Bruh. It's hard to answer a question like that right away!"
    un "Then pull the wish!"
    "She got a little upset, but being able to mock me a little bit sweetened the pill."
    "What can you do, I had to pull a wish!"
    "The paper said:"
    "{i}Kiss the person in front of you for 20 seconds.{/i}"
    me "Don't think I'm doing this on a whim!"
    "I hovered over the girl and fairly counted down the allotted twenty seconds."
    me "Keep dragging!"
    show un smile pioneer with dspr
    un "Here!"
    "{i}How exactly do you like to kiss?{/i}"
    show un shy pioneer with dspr
    un "I don't know! I've only been kissed by you, and so far I like it all!"
    me "And I like... French. {w}I'll show you sometime."
    show un smile2 pioneer with dspr
    un "Why not now?"
    me "Because it's your turn to pull!"
    un "Okay."
    "She laughed and pulled the next blank."
    "{i}What is your favorite thing to do?{/i}"
    un "Well, it's quite easy! {w}I love to draw!"
    un "And you?"
    dreamgirl "Yeah, let's tell the girl that we prefer the computer to all other leisure activities."
    th "That's not true! I also love music. And reading."
    dreamgirl "And how long has it been since you've updated your music library?"
    th "Well, I haven't tried everything yet."
    dreamgirl "Cool excuses. Let's get the wish."
    me "Wish."
    "{i}Take an erotic photo.{/i}"
    "Nooooo! I was hoping Lena would get that part!"
    "As they say - what is bad luck, and how to deal with it."
    "Okay, I'm half-assed anyway, so by local puritanical standards, I'm pretty much a minimum starlet."
    me "All right, sit tight."
    "I walked over to Lena and, putting my arm around her shoulders, stretched forward with my phone. Selfies, yes."
    un "What are you doing?"
    "With one lip, Lena asked, dutifully scowling into the iris solution."
    me "Shooting on three! get ready!"
    me "One... three!"
    pause(1)
    play sound sfx_7dl["snap"] fadein 0
    scene white with flash
    pause(1)
    scene bg int_library_day
    show un smile pioneer at center
    with dspr
    un "You were taking pictures!"
    me "Yes. Here."
    "I held out my smartphone to her, where the photo had already finished processing."
    me "Now I'll have a piece of your memory, too."
    un "Good as. {w}So, next?"
    me "What a question! Of course, next!"
    show un surprise pioneer with dspr
    "{i}How often do you lie?{/i}"
    un "Bad question... Very bad."
    un "No matter how I answer, it won't be right. If I say I'm not lying, you won't believe me, and if I say I'm lying, then... Well, I choose wish."
    me "Come on..."
    show un shocked pioneer with dspr
    "It seems that the assignment from wish box surprised her even more than the question."
    me "What's in there?"
    "Instead of answering, she handed me a paper."
    "Unfolding it, I read."
    "{i}Touch tongues with the person in front of you for five seconds.{/i}"
    show un sad pioneer with dspr
    un "Why did you write such nasty wishes?"
    "Quietly she asked."
    th "Nasty? Well, man."
    dreamgirl "Forgot about the kissing? {w}You were the first one to kiss her, and she doesn't know any others except the ones made with the lips."
    me "Okay, relax and close your eyes."
    me "Trust me, okay?"
    show un surprise pioneer close at center:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 1.5 zoom 1.35 xalign 0.5 yalign 0.35
    "She swallowed hard and showed the tip of her tongue."
    "Squinted in horror."
    "Easily overcome by symbolic resistance, I was already touching the tip of her tongue a few seconds later."
    hide un
    show un angry2 pioneer
    with dissolve
    "And when I recoiled back five seconds later, she looked at me with some even indignation."
    un "Hey, where are you going? Come back here right now!"
    me "No way. My answer, and then you haul the next paper."
    me "There was a question about lying... It's no big deal. {w}I lie all the time. Next."
    "The girl burned me with a look, but she didn't argue and pulled out the next piece of paper."
    "{i}Do you like to cook?{/i}"
    show un normal pioneer with dspr
    un "I can't stand it. {w}But for the sake of my loved ones, I can, and I might even be able to enjoy it. {w}You?"
    me "I hate it. {w}Pizza ordering is our thing."
    "The easiest one - wish we'd started with it."
    me "There's still three left - bring it!"
    show un normal pioneer with dspr
    un "Yea..."
    "{i}What is your most cherished dream?{/i}"
    un "Uh... What if these dream... reverie... dreams?"
    me "Dreams, just dreams."
    un "Well, there's more than one. I want to exhibit, become something more than just another seamstress-motorist, learn to paint and become an artist."
    me "How long has it been?"
    un "Secretly all my life... But out loud... Two days."
    me "It's a beautiful dream. But you said there was more than one?"
    show un shy pioneer with dspr
    un "Y-yes n-no... Anyway, I can't say the second one!"
    dreamgirl "It's about time you showed gallantry and participation."
    me "You can't, so you can't. Now my dream..."
    "I've given it some thought."
    "Somehow it turned out that I hadn't dreamt of anything in a very long time. There were some momentary desires, needs, whims - but I'd be ashamed to call them dreams."
    "Unless..."
    me "And I want to get out of here and not lose you. {w}Or drag you out to my place. {w}Or stay with you."
    "A greedy, selfish desire to take my dream for myself and carry it everywhere with me."
    show un serious pioneer with dspr
    un "You make it sound so easy..."
    me "I don't see the point in being shy."
    "A slight shrug."
    "There's silence in the library."
    show un sad pioneer with dspr
    un "Am I pulling further?"
    "Silent nod."
    "{i}Do you like to meddle in other people's affairs?{/i}"
    un "No. {w}I can't stand prying and meddling."
    me "I agree. {w}I'm glad we're in solidarity here."
    un "But that doesn't mean I don't care about the people around me..."
    me "I get it."
    "Gently I interrupted the girl."
    me "Lena, I'm the same way myself, and I have the same kind of stiffness inside of someone else's pain."
    show un serious pioneer with dspr
    un "Yes…"
    with fade2
    "{i}What is your favorite color?{/i}"
    un "It's simple here. I love blue."
    me "Yeah, simple. And I..."
    play sound sfx_7dl["eat_horn"] fadein 1
    "I could not finish before the tinny loudspeaker began to blare, calling for starving pioneers to join the treasury of world cookery."
    show un smile pioneer
    un "That's it, thanks for the company!"
    "I just smiled and held out my hand to her."
    stop music fadeout 5
    stop sound fadeout 4
    stop ambience fadeout 1
    return

label alt_day4_un_7dl_day_dr_nwsppr:
    play ambience ambience_camp_center_day fadein 3
    play music music_7dl["what_am_i_doing_here"] fadein 3
    scene bg ext_musclub_day
    show un normal pioneer
    with dissolve
    un "Tell me, what do you think about music in general?"
    me "I used to do music. A million years ago."
    me "I mean, I'm not completely untalented, and I have some skills."
    show un smile pioneer with dspr
    un "Really? Do you have an ear and a voice?"
    me "You ask me... I've been singing for a while!"
    show un shy pioneer with dspr
    un "I've been told I have a voice, too... But I'm terribly shy to perform in public."
    "And that's where she and I are completely similar."
    "Except that I can just turn my stupid head off for a while and rehearse something like a clockwork, because the number of times I usually rehearse is comparable only to the number of times I'm willing to listen to a really catchy song."
    "Like any other retard, I get to the point where a song gets a little boring from the third time."
    "And so all the words, notes, movements, choreography, and even bowing with smiles grow up somewhere between unconditioned reflexes and reactions."
    me "I'll have to take you to karaoke sometime to hear you sing."
    dreamgirl "How low you have fallen!"
    me "Or to the Palace Arch: the acoustics there are amazing."
    show un normal pioneer with dspr
    un "You mean your hometown?"
    if alt_day4_me_neu_transit == '':
        me "I mean ours..."
    play sound sfx_open_door_2
    pause(1)
    "Miku wasn't there, but the door was open."
    "Very irresponsible!"
    if alt_day1_sl_keys_took in (1, 3):
        "After patting myself in my pockets, I looked around conspiratorially and locked the room."
        me "I can't help it. {w}I have a very high regard for musical instruments."
        me "And I'm afraid not everyone here shares my views."
        show un smile2 pioneer with dspr
        un "You're so thrifty!"
        "She complimented me."
        "And then immediately ruined half the feeling of the compliment by wondering in between."
        un "And where did you get the keys?"
        me "Where I got them, where I got them... Where I got them, there's no more."
        show un laugh pioneer with dspr
        un "Did you steal them from Slavya?"
        me "Actually, she left them when she fed me on the first day, so I took them."
        un "Very economical!"
    un "Shall we go look for Miku?"
    "I nodded and headed toward the stage - in light of the approaching concert, it was the most logical place to expect our art director."
    scene bg ext_stage_normal_day with dissolve
    "We weren't wrong in our predictions - Miku really was here."
    "And it's amazing how the short, frail little girl managed to take up so much space, seemingly being everywhere at once."
    "Here she is shouting at the editors directing the spotlights to the near third of the stage, here she is waving at Slavya, showing that the signal level is acceptable, catching a «cross» from the stage, cutting off the backing track and making the «little swans» run the performance again."
    show un smile3 pioneer with dissolve
    un "Staring, aren't you?"
    "Poked me in the side with her elbow and laughed, deliberately picking up my jaw and putting it back into place."
    me "Okay, three elements you can look at forever - burning fire, flowing water..."
    show un laugh pioneer with dspr
    un "And working people?"
    "Lena laughed."
    me "Yes! What's wrong?"
    un "Nothing. Let's go interview her for an article."
    "I completely agreed with Lena and, after giving her my hand, gallantly led her toward the DJ booth, completely occupied by Miku."
    show mi normal pioneer at left with dissolve
    mi "Oh, look who's here! Lenochka and Senya. You're very on time, very much! Do you want to see the concert or have you stopped by to talk about the day after tomorrow?"
    me "Actually, we came to see you in the hope of getting an interview."
    show mi happy pioneer with dspr
    mi "Oh, the interview! I love interviews! What do you want to talk about? If it's about my creative plans, I have to disappoint you - the next few years I'm going to devote only to my studies, and I won't go on stage at all, except for amateur performances."
    show un normal pioneer with dspr
    me "That's exactly what we came to talk about, the concert the day after tomorrow."
    "Politely, I replied, trying to ignore Lena's wince."
    if 'music' in list_clubs_7dl:
        show mi grin pioneer with dspr
        mi "Of course, of course! But haven't you forgotten, Senechka, that we're in the same club - which means you have to help me, look me in the mouth and praise me in every way?"
        "She enjoyed my dazed face for a few seconds."
        "And finally she couldn't stand it."
        show mi laugh pioneer with dspr
        mi "Oh, I can't! It always works, and everyone always makes such funny faces, like I said something obscene! My dad showed me that when he was explaining the beginnings of getting an audience's attention, and I took it from there."
        me "Yeah. So you made a joke about me having to help you?"
        show mi normal pioneer with dspr
        mi "No, of course not! I was only joking that you should praise me: I can see for myself that you are fully occupied by Lenochka, and she would scalp me for one look in your direction - and be fully in her right! And that means..."
        me "Yes?"
        mi "You know «little duck dance»?"
        $ alt_day4_un_7dl_ducks = True
        "Without waiting for my answer, she wrinkled her nose amusingly and hummed:"
        mi "They want to be like walking ducklings, and of course not for nothing, quack, quack, quack..."
        me "I know, I know!"
        "I hurriedly interrupted the girl before she drew the attention of a hundred percent of the cash audience."
        mi "That's fine - so you go upstairs, drag those little kids in gray suits to the far side of the stage so they don't get in the way, and rehearse with them, so they can do something by noon. Can you do that?"
        me "I don't know."
        "It was no use arguing with the rambunctious Japanese girl - in her usual state she was the personification of a machine-gun person, but here... Here it was either an anti-aircraft battery or a «Vulcan» with a rate of fire of a couple of thousand a minute."
        show un laugh pioneer with dspr
        un "Go on, try your hand at being a choreographer."
        show un smile pioneer far with dissolve
        "Lena was laughing heartily as she stepped back to the bench and, settling in as comfortably as possible, nodded encouragingly, saying, «Go»."
        "Well, I'll have to."
        hide un
        hide mi
        with dissolve
        "Feeling like a complete idiot, I leaned my palms on the painted boards of the stage and, pulling myself up, jumped up and looked around for my future charges."
        "The aforementioned «swan ducklings» piled lostly by the left backstage area, from which I picked them up:"
        me "Squad 6, huh?"
        "Waiting for the lost nods, I headed deep into the stage, throwing an unapologetic tone:"
        me "Follow me - and just you dare to get lost!"
        "A friendly stomp as a response best demonstrated to me that the boys had decided to heed the instruction."
        "The far edge of the stage was curtained with a white opaque cloth, perfect for watching movies outdoors."
        "The Americans had it implemented in concrete parking lots, but our pioneers might have neglected comfort for a good show."
        "«Chapay», «The Elusive», «Cowardly-Dummie-Beastly», so much of them."
        "And so along this very cloth we stretched in a line one by one - from my own experience of lineups I know very well that the second line consists of the most inveterate netizens, so I have abolished this element as a relic."
        "Not listening to the indignant cries, stood up in the very lurch where this stupid dance begins - everything for approval in the eyes of your loved ones..."
        dreamgirl "Yes, and for the sake of shutting up the machine-gun girl."
        me "Repeat after me, slowly."
        me "Hands in front of you, fingers folded together, facing the sun! {w}Stand up!"
        "I walked in front of the formation, correcting some who had decided to do a little panting, finally nodded satisfied and allowed to move on to the next element of the dance."
        me "Now, we close our folded fingers and thumbs as if trying to take something out of the air!"
        "..."
        play sound sfx_7dl["eat_horn"] fadein 1
        "I don't know where or how deep down in me the teacher-choreographer slumbered, or if there was one at all, or if anyone who could even remember the movements could have taught the primitive «little ducklings»."
        "But by the time the horn sounded at noon, the kids were quietly satanizing from the five hundredth repetition of the same thing."
        "But I was sure that wake them up in the middle of the night and they wouldn't screw up, and even in their half-asleep they would dance just right!"
        me "Dismissed."
        "I turned around and headed toward Lena, who was waiting for me."
        "I didn't even want to look at Miku."
        "The goddamn exploiter set me up for nothing."
        show un smile pioneer with dissolve
        un "And you're good!"
        "Lena smiled at me, accepting my offered hand and rising."
        un "Except that you totally unnecessarily rolled the kids, they're going to hate this dance now."
        me "What are they..."
        "I shrugged it off."
        me "They chose it, it's their own fault. I don't think they came to Miku and said, they want to perform, but they can't do shit."
        me "If I know your roommate even a little bit, she'd approach even such hopeless patients with a bit of imagination and fire."
        show un laugh pioneer with dspr
        un "By the way, I interviewed her - after lunch we'll rewrite it and you can consider that you passed the entrance exams to our wall newspaper."
        me "Thank you, oh benefactress!"
        "I jokingly bowed, dragging girl with me toward the canteen - after two hours of dancing, my appetite was running wild!"
    else:
        me "Miku, take a little break, and tell us everything you can about the next concert!"
        "I asked, politely taking the restless Japanese girl by the elbow."
        mi "I have no time, no time! I have to set up the numbers, the acoustics, coordinate the program, prepare the phonograms - no time, absolutely no time!"
        me "Okay, then just tell me how much time you have in two minutes!"
        show mi normal pioneer with dspr
        mi "Well, actually, it's a huge secret, but you probably need a lot of time to get the illustrations ready! Or will you be taking pictures?"
        me "I remember seeing cyberneticists with photo reactions..."
        "No, there's no time to think about that!"
        me "We'll draw: you're right - we need the information in advance."
        mi "That's what I immediately thought you would be painting. Because Lena is such a good artist, only for the last three days she has been drawing the same thing all the time - you!"
        show mi shy pioneer
        show un shy pioneer
        with dspr
        "Miku blushed, realizing that she had said too much, but immediately switched to a new channel."
        show mi normal pioneer with dspr
        mi "So that's what's going to happen."
        mi "Alisa promised to do something absolutely incredible, if I understood correctly, it will be a solo guitar number with a backing track, so you can draw it right with «Ural», won't be wrong."
        mi "Of course, I want to perform too! {w}I'll show Lena my dress tonight, but I daren't put it on yet - I tried to put it on once already, but they kicked me out of the canteen for immorality, so I had to wear pants till the night before they started giving out my uniform!"
        me "Yeah, they kicked you out of the canteen, and you dragged this beauty on stage?"
        show mi surprise pioneer
        show un smile pioneer
        with dspr
        mi "What's the big deal! It's a stage image, you know! It's not like I have to perform in uniform - I want to be dressed up!"
        "I only smiled. It's her choice after all, it's not me who gets the wick later from Olga Dmitrievna."
        me "I warned you."
        mi "Yes, and I listened to you! Damn!"
        show mi rage pioneer with dspr
        mi "I carried three suitcases here, and I wore a miserable uniform for the whole shift! I even had to get a dress from the costume shop for the dance! I want to look dressed up!"
        "She raked her shirt over her chest in a pleat with disdain:"
        mi "I feel dirty in this! No bright colors, no fit, not even normal tightness! So let them say what they want, but I'll wear a stage dress to my performance!"
        "Her hotness evoked the sincerest sympathy and the most genuine smile."
        me "Who else? I've only heard of you and Alisa. I don't believe the whole gala concert will be two performances."
        show mi normal pioneer with dspr
        mi "No, of course there's a pretty tight performance schedule, but out of our troop it's just Alisa, me... Oh, I totally forgot - we also have Electronik signed up, something about playing the xylophone."
        "My hand reached for my face. Dull xylophone players are the real muckrakers of any amateur concert..."
        me "We certainly won't write about that - we don't want to embarrass ourselves before posterity."
        me "That's it, not another word about Electronik."
        show un normal pioneer with dspr
        un "That's great."
        "Lena turned to Miku."
        un "Anything else we should know about?"
        mi "Of the really interesting stuff, only this. But I haven't watched all the performances yet."
        un "Well, I guess if you see something promising, let me know, just as a friend, as a neighbor."
        mi "Of course! I promise."
        hide mi with dissolve
        "Miku instantly lost interest in us and chased the «little ducklings» for the tenth repetition of their silly dance, and we headed toward the square."
        play sound sfx_7dl["eat_horn"] fadein 1
        "Halfway down the road, however, we were intercepted by a horn, dear to every pioneer's ear."
        un "How time flies by..."
        "Studying her palm thoughtfully, Lena said."
        "Correctly interpreting the hint, I grabbed her hand and pulled her toward the canteen."
    stop sound fadeout 4
    stop music fadeout 4
    return

label alt_day4_un_7dl_day_dr_badmin:
    scene bg ext_dining_hall_near_day
    show un normal pioneer
    with dissolve
    play ambience ambience_camp_center_day fadein 3
    "After standing for a while, she oriented herself and moved eastward toward the footbal field."
    show un normal pioneer far with dspr
    un "Why are you standing?"
    show un smile pioneer far with dspr
    extend " Let's go!"
    scene bg ext_playground_day
    with dissolve
    play ambience ambience_soccer_play_background fadein 3
    "The usually densely populated playground today was half-empty one half of the pioneers had not yet been returned to their homeland by their parents."
    "The other - under pressure from the relentless counselors, pulling their backs in front of the homegrown inspectors with all their might - sat in the cabins, serving their quiet time."
    "Which means the equipment and grounds are at our complete disposal!"
    show un normal pioneer with dspr
    un "Lets go to the box!"
    play sound sfx_open_door_clubs_2
    scene bg ext_tennis_court_7dl
    show un normal pioneer
    with dissolve
    "She fiddled with the door locking the court and waved her hand invitingly."
    if alt_day4_me_neu_transit == '':
        me "Is it even allowed?"
        show un laugh pioneer with dspr
        un "I told you, it's an even day. Badminton players occupy the court today."
        un "Boris Alexandrovich usually coaches the group as they form, so we can play for a while."
        me "Play?"
    show un grin pioneer with dspr
    if (alt_day2_date == 'un'):
        un "You showed me then how to pitch properly, and I got my hands on it pretty quickly."
        un "So don't expect an easy win!"
    "Going to the booth, Lena pulled out two racquets - this time quite serious, wicker ones, not the plastic nonsense she was trying to get her hands on - and, after poking around in the bags for a while, found a derelict shuttlecock."
    un "Live!"
    show un smile2 pioneer far with dissolve
    "Throwing me a racket, the pioneer took a seat on the other side of the net and, assuming a masharapova pose, nodded excitedly:"
    un "Thy end is now!"
    "The shuttlecock flew with terrific speed to my half of the court, and I had to literally pull it out of the air in a leap that would have done honor to any other football goalkeeper."
    play sound sfx_tennis_serve_1
    "The unfortunate feathered projectile flew into the sky in a glorious candle and landed right on Lena's propped up racket, where it rolled straight into my half."
    "I, still standing in a prostrate posture, could only watch helplessly as I was just beaten by a girl!"
    show un smile pioneer far with dspr
    un "One-zero to my favor! Give me the shuttlecock - my serve."
    "I obediently did as required and took my place in the middle of the court, determined that this time I would give the obnoxious girl a fight!"
    "And even fought off another slash, this time reducing it to a normal slash, which Lena could not drop on my half with a «snot», as she had done in the first round."
    "We raced the shuttlecock back and forth for a few minutes before she, becoming bolder, tried to cut again - but I was on my guard and this time just set my racket in the path of the cannon shot."
    "The shuttlecock blew up the lawn."
    me "One-One. Know our people!"
    show un smile2 pioneer far with dspr
    un "So you decided to resist?"
    show un serious pioneer far with dspr
    "She bit her lip and gave me a deliberately dismissive look."
    un "Come on! Show me what you can do!"
    show un smile pioneer far with dspr
    "And I showed it!"
    "A few points later, we both got into the game: the mind let go of the reins, leaving the body to reflexes and tactical thinking."
    "And each serve lasted longer and longer: I had to use dishonest tennis tricks - which, by the way, neither side was afraid of."
    "The easiest one is to get your opponent to defend the left edge until he goes all the way there. {w}And a few strokes later cut to the empty right side."
    "A little later she got her revenge on me."
    show un smile2 modern far with dspr
    "Lena, who was playing up, dropping her tie, unbuttoning the top two buttons of her shirt, turning pink, was passionately beautiful..."
    "And, of course, my aesthetic senses expectedly began to take control of my body, gradually abolishing my control of reflexes: I began to yawn serve after serve, to lose tempo, until, finally, I dropped the racket altogether when Lena increased the point gap to five."
    show un smile2 modern with dissolve
    un "Hooray! I won! Hooray! Hooray! Long live the magnificent me!"
    "She was laughing and goofing off heartily, I sat on the bench and couldn't say a word - Couldn't catch my breath."
    un "I've got you all wrapped up, haven't I?"
    me "I guess you could say that."
    un "And you held your own with dignity! And for that you deserve encouragement!"
    me "Encouragement?"
    "All of a sudden cookies, condensed milk and other sweets popped into my head. I don't know why. Maybe it's because even a man of unpretentious mind wouldn't call a meal nourishing?"
    show un smile2 pioneer close with dissolve
    "I had already heard almost distinctly: «sweet prize!» so the touch of soft lips on my cheek was a complete surprise."
    "Bruh..."
    "..."
    play music music_7dl["genki"] fadein 3
    show ba em1 uniform at left
    show un scared pioneer at right
    with fade2
    ba "Well, well, well."
    "Yeah, well, after the sweet stuff, Random always slips in a few kilotons of tar."
    ba "What am I observing? I'm observing a court, thrown away shuttlecocks and kissing pioneers."
    if ('badmin' in list_clubs_7dl) and (alt_day2_convoy == 'un'):
        ba "I guess you didn't hear me last time."
        ba "Though I'm sure you've heard what you're facing."
        "I just nodded dolefully, catching the synchronized movement of the purple-tailed head out of the corner of my eye."
    ba "Do you know what that means?"
    show ba normal uniform with dspr
    ba "Sixteen laps of the field! {w}That's what it means!"
    me "But why?!"
    "It came out of my mouth."
    ba "For turning a sports field into a brothel."
    ba "So the first round is on the house."
    ba "And the other fifteen, five for every piece of sports equipment thrown."
    if ('badmin' in list_clubs_7dl) and (alt_day2_convoy == 'un'):
        dreamgirl "Say thanks for that it's not promised twenty."
        "I Uh-huh'd accordingly."
    $ alt_day4_un_7dl_ba_alerted = True
    ba "Now put the shells back and get started."
    "He looked at the stopwatch:"
    ba "That's forty minutes till lunch - you'll make it."
    ba "Get to it!"
    hide ba
    show un smile pioneer with dspr
    "After handing out the valuable Directions, the gym teacher turned away and moved back to the indoor room. {w}Sleep, no doubt about it."
    ba "And don't even think about running away. {w}Try and the counselor will know what you've been doing naked in here."
    me "But we're dressed!!!"
    ba "Yes? {w}Strange. {w}And I could have sworn you were on the court with no clothes on!"
    th "Aaaaasshole!"
    ba "I love you too, pioneers!"
    "Finally he opened the door and hid inside."
    me  "Shit. He's got something to threaten me with."
    "And Lena stood with her head tilted to her shoulder, her eyes full of joy."
    un "I can't figure out what upset you more: teacher's cavalierness or the fact that he showed up too early?"
    me "You know!"
    "I said with annoyance."
    me "For a modest girl, you're making too many jokes about me!"
    show un laugh pioneer with dspr
    un "That's how bad I am as a prude."
    "She got up and put the equipment back where it belonged."
    un "So, who's first to the finish line?"
    scene bg ext_playground_day at running
    show un normal pioneer
    with flash
    "We locked the court and, in lazy jogging mode, we measured the assigned laps - and I wasn't a foot more angry with Sanich."
    "He's stupid, though is an adult."
    "Thought to punish us, but ended up encouraging us."
    show un smile pioneer with dspr
    "Lena very quickly got the blush back on her cheeks that had conquered me, and I seemed to turn pink, too, as she threw interested glances at me."
    un "You know, you'd look good with freckles."
    "Suddenly she said."
    me "What? Why?"
    un "You're so funny... Even though you're acting like a boo."
    "We've finished twelve laps, and by this point we've had time to adjust our breathing so that we still have enough to talk."
    un "I close my eyes and sometimes I see you with a scattering of freckles on your nose."
    me "You should see me every year after first contact with the first spring sun."
    me "I'm sure you'd like me a lot."
    show un smile2 pioneer with dspr
    un "You'll get freckles?"
    me "Yeah. Then the body pulls in, switches to spring-summer mode, but for a few weeks I go completely ginger."
    un "What a miracle you are!"
    me "You know..."
    scene bg ext_playground_day
    show un smile pioneer
    with dissolve
    "We crossed the finish line of the last lap and stopped to catch our breath."
    me "I would..."
    un "What?"
    me "I'd have been a couple more laps late..."
    me "If you know what I mean."
    show un laugh pioneer with dspr
    play sound sfx_7dl["eat_horn"] fadein 1
    "She laughed and gave me a deafening kiss on the nose, as the horn sounded over our heads, calling the pioneers to the lunch."
    show un smile3 pioneer with dspr
    un "Just in time!"
    "With a wave of our hand toward the indoor, we headed toward the canteen."
    stop sound fadeout 3
    stop music fadeout 3
    stop ambience fadeout 6
    return

label alt_day4_un_7dl_launch:
    play ambience ambience_dining_hall_full fadein 5
    play music music_list["silhouette_in_sunset"] fadein 3
    scene bg int_dining_hall_people_day
    show un smile pioneer
    with dissolve
    "Lena sat across from me with her leg under her and stared at me strangely."
    "I almost choked on a muffin."
    me "W-what?"
    un "I don't know what you do, how you do it, or why you do it, but I've spent more time with you today than I have with my dad all year."
    "She leaned toward me, looking furtively."
    un "And you know what? I'm not sick of you!"
    me "So what? Is that an achievement?"
    un "I get tired of people very quickly."
    show un serious pioneer with dspr
    "She shook her ponytails and stared at me angrily."
    un "It's like you know some recipe.{w} I've read mentions of such things, and as an artist I pick up on certain things - how you look, how you react, how you judge."
    dreamgirl "I think your trump card just got burned and pulled out of your sleeve."
    dreamgirl "I suggest you go off the deep end and deny everything!"
    dreamgirl "Otherwise, if she finds out you've been analyzing her all along, it'll be aye-aye-aye."
    me "Yeah, I've been taught to read some nonverbal symbols - it was required by my line of work."
    "I shrugged."
    me "Is that bad?"
    show un grin pioneer with dspr
    un "No way. {w}But you've been acting like a klutz from day one - awkward, clumsy..."
    show un shy pioneer with dspr
    extend " Oi, sorry."
    un "What I want to say is..."
    me "Yes, I know what you mean. Yes, I'm not as dumb as my face, and I'm not as dumb as I look."
    th "Maybe that's exactly why I still haven't bored you...{w} That I'm not as shallow as your peers."
    me "But I didn't mean it out of spite, honestly!"
    show un normal pioneer with dspr
    un "I wonder what else you're hiding..."
    th "What difference does it make if we already like each other... Let's stick to the set bar?"
    me "And my head hurts more about how we won't lose each other after camp."
    me "Contacts are good, of course - but how much can two teenagers, one of them already of call-up age, do?"
    me "All in all, I'm pretty pessimistic."
    me "You graduate high school, then move on to the capital for your dreams. {w}This means I'm not likely to see you next year."
    me "Maaaaaany!"
    show un angry2 pioneer with dspr
    un "Now let's lie down and suffer?"
    me "No, but..."
    "It suddenly occurred to me that I'm not tied to anyone or anything here. {w}And no one is forcing me to move to the Northern Capital."
    me "Actually, I have an idea."
    un "What is it?"
    me "I'll go with you. Where you are."
    show un surprise pioneer with dspr
    un "Do you want me to put you in my closet?"
    me "No, I'll try to socialize in your town, and then we'll see."
    show un grin pioneer with dspr
    un "You certainly know how to surprise, but you're underage - they'll send you home in a jiffy."
    if alt_day4_me_neu_transit == '':
        un "Although, yes... Your house hasn't even been built yet. {w}Well, I don't know. What do you think?"
    me "There are only two important milestones: your getting into art school, and my demobilization in three years."
    me "You just have to keep in contact and coordinate a little bit."
    "I was well aware that I was fantasizing as I went along: that nothing in this world, not even in the Soviet Union, was or would be easy, that there was a very good chance that I would just be taken back to where it all began..."
    "But I wanted to be ready for anything."
    dreamgirl "If we linger here... Just in this unlikely event."
    dreamgirl "I want to remind you that it's '89 and there's still a way for you to go into space."
    "It stings in my heart with a long-standing pain."
    "A dream that I had so foolishly and haplessly squandered."
    dreamgirl "Gagarinka is still recruiting, the main thing is to fly the right number of hours, and then..."
    show un sad pioneer with dspr
    un "Back in his head again."
    me "No. I just suddenly remembered that all my life I wanted to wave to Earth from outer space."
    show un surprise pioneer with dspr
    un "And you want to..."
    show un cry_smile pioneer with dspr
    "Lena looked at me with unconcealed respect."
    un "I'll believe in you as much as I can. But it must be hard to get there."
    th "No harder than when I took the tests."
    th "I got cut because of the kidneys, but this time..."
    "This time it's going to be my way!"
    me "I want you to be proud of me, and we don't have all this filth, little paychecks and domesticity in our lives. {w}You're a little miracle, an artist, and you don't deserve such a fate."
    show un serious pioneer with dspr
    un "What do I deserve?"
    me "The very best..."
    if alt_day4_me_neu_transit == '':
        extend " Everything that can be squeezed out of the remnants of a faithfully dying Union."
        dreamgirl "Watch your language."
        dreamgirl "The Union certainly doesn't have much left, but it still has enough power to crush the insignificant you."
        dreamgirl "Moreover, dissenters are best astronauts for sure!"
        dreamgirl "Anyway, let's get our heads in gear and start spinning."
    show un smile pioneer with dspr
    un "You finished the gingerbread, you know?"
    un "If you want to sit a little longer, I don't mind..."
    me "Oh, sorry."
    "I pushed the unruly, dancing thoughts away with an effort, and with a few breaths tried to bring order to my body, which was stirred by an almost tangibly achievable dream."
    th "Right now I need to focus on the thing that demands my attention here and now - our... ahem... novel."
    dreamgirl "Absolutely right. {w}The girl is certainly interested in you."
    dreamgirl "But if you don't pay attention to her, she'll get bored very quickly."
    me "Let's take a walk."
    un "Let's! Where do you want to go?"
    if alt_day4_un_7dl_ducks:
        "Remembering the hateful stares of the little pioneers, I felt my mood begin to improve rapidly."
        me "My charges, the ducklings."
    me "Shall we go see the concert? {w}What the kids are going to do for their parents."
    show un serious pioneer with dspr
    un "I hope you're not going to whistle or make fun of them in any way? It's hard enough for them."
    me "Come on, what are you doing? I want to sit in the back benches and sing along to them if the songs sound familiar."
    un "Well... All right, if that's the case."
    "She caught my palm and dragged me out."
    stop music fadeout 3
    stop ambience fadeout 6
    return

label alt_day4_un_7dl_concert:
    scene bg ext_stage_normal_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    play music music_list["everyday_theme"] fadein 5
    show mi normal pioneer far at center with dissolve
    if dr and 'nwsppr' in list_clubs_7dl:
        "We noticed Miku as we approached - just like in the afternoon, she was taking up an incredible amount of space."
    else:
        "We noticed Miku as we approached - she was taking up an incredible amount of space."
    show mi normal pioneer with dspr
    mi "Come to see the concert? Very good."
    mi "For some reason the other pioneers don't really like to see the performances. I'm glad I'm not the only one interested in amateur performances."
    me "We..."
    mi "Very good! Our seats are all back benches, they're for the big ones, like the older squads! I mean, for us. I mean, we won't be in anyone's way there."
    "After thanking Miku, we went to the designated places."
    hide mi with dissolve2
    "I took Lena to the back benches - the tallest, under the long legs of the older pioneers - and, sitting down myself, sat her down beside me, grasping the cool palm with graceful long fingers, that might have been the fingers of a doctor or a musician."
    "But they became the fingers of an artist."
    if alt_day4_un_7dl_ducks:
        me "Tell me if you see the «ducklings» before I do, I want to see how they learned their lesson."
        "Lena nodded in agreement and, with her finger to her lips, nodded eloquently toward the stage - the first performance in the concert had already begun."
    "While all sorts of childish nonsense sounded: songs that weathered from memory faster than the echo of their sound faded, poems of the same caliber."
    "The sixth through seventh squads were junior school plus an itinerant kindergarten."
    "I don't think they could have cooked up anything touching..."
    "I caught myself actively singing along to another chorus diligently deducing how for a week they were going to Komarovo."
    "Lena, after watching me incredulously for a couple of minutes, also lisped the lines familiar from her childhood."
    "And there the audience little by little got involved, and when the soloist on stage forgot the words - the audience took him out on his serve and their own shoulders."
    "A small miracle of collective performance."
    if alt_day4_un_7dl_ba_alerted:
        "And I automatically looked around at the people around me."
        show un laugh pioneer with dspr
        un "Looking for Boris Alexandrovich?"
        "Lena laughed, completely guessing my thoughts."
        me "If he makes us run around here too..."
        un "Don't worry, he's still lounging around, before dinner, such a bear."
        me "How do you know?"
        "I asked suspiciously."
        show un grin pioneer with dspr
        un "You must be jealous!"
        "I was embarrassed, but I didn't look away."
        me "So, how?"
        un "I was on duty at the football field... You were so lucky to arrive that you weren't put on duty anywhere at all."
    "There was some nitwit on stage raping the piano, and I realized I'd had enough of culture for one day."
    me "Shall we get out of here?"
    "Lena nodded in agreement and let herself be led away."
    stop music fadeout 3
    return

label alt_day4_un_7dl_dynamite:
    if alt_day4_un_7dl_calm == 'dv':
        play music music_7dl["dv_guitar"] fadein 7
        scene bg ext_house_of_dv_day with dissolve
        "I don't know how it happened, but as we passed Alisa's cabin, we heard guitar strumming, and we crept closer, trying not to crack the bushes."
        "There was Alisa, puffing a cigarette in between - touchingly naive, trying to look like a grown-up, nonstop - puffing her strings."
        "Ulyanka sat next to me and said something, Alisa nodded in time with the words."
        "We got a little closer, but I guess we were too late, because we only managed to catch a snippet of the phrase:"
        us "To make it explode better."
    else:
        scene bg ext_clubs_day with dissolve
        play music music_list["so_good_to_be_careless"] fadein 3
        show us normal pioneer at center with dissolve
        "We moved wherever we could see and ended up at the clubs."
        "Toward us came Ulyana, clutching some suspicious jar to her chest."
        show us smile pioneer with dspr
        us "Oh, rookie! Rookie, tell me, do you happen to know how to make saltpeter into explosives?"
        me "I happen to know. You add any kind of fuel, and voila."
        us "Thank you! You're not such a retard!"
        hide us with moveoutright
        "Ulyana cheered, and as she slipped past us, she disappeared into the bushes."
        me "I hope she was kidding about the explosives."
        show un serious pioneer with dissolve
        un "Ulyana never jokes about such things."
        "Something inside me broke off."
        me "W-what... is that, did I just..."
        un "Yes. Practically put an explosive in the hands of a child."
        un "Don't you have a guilty conscience?"
    me "We've got to stop them!"
    show un angry2 pioneer with dspr
    un "Don't. Stay out of it, please."
    me "Why?"
    un "Because... Because everyone has the right to go crazy as they please."
    menu:
        "Agree":
            $ lp_un += 1
            if dr:
                $ karma -= 10
            $ alt_day4_un_7dl_dv_us_explosives = True
            me "I will certainly regret it. {w}But when you ask me..."
            show un laugh pioneer with dspr
            un "A wise decision."
            un "It's about time for Alisa and Ulyana to take responsibility for their own actions."
            play sound sfx_7dl["eat_horn"] fadein 1
            "I shrugged, and the horn was already blowing over my head."
            me "Before I could even digest the gingerbread, I was already demanding supper!"
        "Disagree":
            me "I'm sorry, sweetheart, but we're not just talking about going crazy here."
            show un sad pioneer with dspr
            un "I hope you realize what you're getting into?.."
            "I smiled disarmingly."
            me "Again, I'm sorry. {w}I can't just walk by like that. I can't."
            me "First, the underage Ulyana. {w}And secondly, Dvachevskaya still needs an eye on her: she didn't get far from Ulyanka."
            me "And finally, thirdly - you do know that a badly made explosive can tear off arms, head, and so on?"
            me "And in a separate topic: it's unlikely that Ulyana would engage in terrorist acts alone - which means we have at least two headless victims."
            show un angry2 pioneer with dspr
            me "I don't know what connects you and Alisa, but I, practically a random passerby, can't pass by."
            me "Anyway, I'm going to stop them."
            scene bg ext_house_of_dv_day with dissolve
            if alt_day4_un_7dl_calm == 'dv':
                play sound sfx_hiding_in_bush fadein 0
                stop music fadeout 1
                $ persistent.sprite_time = "night"
                "Breaking through the bushes, I appeared before the stern gaze of the redheaded bandits."
                me "Okay, girls, I heard something about explosives."
                show dv angry pioneer at left with dspr
                dv "You were eavesdropping?!"
                me "I was also peeping!"
                if loki:
                    me "In case you're smoking in here!"
                elif herc:
                    me "Don't slide okay?!"
                else:
                    me "But we're talking about you now!"
                show us grin pioneer at right with dspr
                us "So you'll help us?"
                me "Of course I will. {w}I did some calculations - you have ammonia-saltpeter, don't you?"
                me "Fertilizer balls. {w}Like white ones, huh?"
                "Waiting for a wary nod, I held out my hand and demanded:"
                me "Give it to me."
                dv "And why should I listen to you?"
                me "It's fertilizer - there's a very high level of impurities in there, it'll never blow up. {w}And I know how to do it."
                show dv normal pioneer with dspr
                dv "Well, if you're lying..."
                "Alisa handed me a small - about a pound and a half - bag of fertilizer."
                me "Not a single thought."
                "I ripped open the bag and, moving deliberately slow, spilled the contents onto the ground."
                me "Forget about blowing anything up, all right!"
                show us angry pioneer close at right with dspr
                show dv rage pioneer close at left with dspr
                dv "You? What did you do?!"
                "They both clenched their fists and came at me..."
                me "You can pound me if you want."
                me "That seems like a good price to pay for saving your two worthless lives."
                show us dontlike pioneer close at left
                show dv angry pioneer close at right
                with dissolve
                dv "What? What are you talking about?"
                me "Yes what I'm talking about, you stupid creature, is that it's not an explosive, it's a surefire way to commit suicide."
                us "And why should we believe you?"
                me "Don't believe it. {w}I don't care at all."
                "I'm prepared for a beating. {w}As much as it was possible to prepare for them at all."
                me "It just occurred to me that Lena would be very hurt if her friend got her arms blown off. And you, Ulyana, your parents came to see you today - I hope you warned them that you were going to mutilate yourself?"
                show blink
                "I closed my eyes."
                hide dv
                hide us
                dreamgirl "And you're a damn hero..."
                "My subconscious respectfully stretched when, even ten seconds later, no fist flew into my face."
                th "I like them both."
                th "And the goddamn camp is pulling diligently forgettable traits out of me again."
                dreamgirl "Are you helpless against someone else's suicidal stupidity?"
                th "And against a whole bunch of different things I don't even want to remember."
                hide blink
                show unblink
                "On the other side of the open century was Dvachevskaya's cottage, but not a single redhead in the foreseeable vicinity."
                me "Did they really listen to the voice of reason?"
                un "I doubt it... More likely you scared them by threatening to rip their hands off."
                $ persistent.sprite_time = "day"
            else:
                "I turned and rushed after Ulyana, but I managed to catch the quick-footed girl only at her cottage."
                show us dontlike pioneer with dissolve
                us "What else?"
                "Unhappily asked Ulyana as I, putting my hand on her shoulder, turned the girl toward me."
                me "Ulyana, you must give up your terrorist scheme."
                show us angry pioneer with dspr
                us "Why should I listen to you?"
                me "Except that I'm going to go right now and tell everything - and not to the counselor, but directly to the head of the camp?"
                us "Snitch..."
                "Contemptuously threw, practically spat the girl."
                "And then I realized - oh, I assure you, I realized - what it means to try to help someone only to find out that that «someone» seems totally intent on driving you crazy!"
                me "You know: I have an unbearable temptation to leave things as they are and come back here in half an hour to see you, burned, wounded, with torn palms, bleeding."
                show us surp3 pioneer with dspr
                us "What are you saying?!"
                me "Saying what?"
                "I poked my finger in the girl's forehead, stimulating her thinking abilities."
                me "Let's get our heads in gear. Because of the high percentage of impurities, explosives behave unpredictably, there's no Bickford cord, and knowing your headlessness, I'm more than sure you'll run to check why it went pff and not bang."
                me "And then when you pick up the bag in your hand, it's going to f... uh... go boom. {w}And you'll be very lucky if it kills you right away, because you'll suffer like you've never suffered before."
                show us cry2 pioneer with dspr
                us "You're lying! Liar!"
                "The girl cried."
                us "You lie on purpose!"
                me "Understand at last."
                "I squatted down, making psychological contact between us."
                me "It didn't cost me anything to just let you do what you set out to do."
                me "If I really didn't care."
                show us shy pioneer with dspr
                us "Then stay out of it!"
                me "Whatever you say."
                "I'm up."
                me "Just promise me one thing, then - don't bring Alisa into this. {w}Let it cripple only you instead."
                me "I bet Mother will be glad when you come to her armless! And how many suitors will show up for your burnt face and burned eyes."
                "I was deliberately exaggerating, but I couldn't get through to the girl otherwise."
                me "Well, think about it."
                hide us with dissolve
                "Turning around, I headed toward the square."
                "And after fifteen yards I was intercepted by a chuckle coming from the bushes."
            show un serious pioneer with dissolve
            un "I can never understand those who do as you do. {w}And I can't help but envy you."
            me "Don't ever tell anyone about this..."
            "I grumbled."
            "It is very easy to be magnanimous in preventing the foolishness of an unwise child..."
            th "Or is shouting «bad, drop the bauble» - the limit of my generosity?"
            play sound sfx_7dl["eat_horn"] fadein 1
            show un normal pioneer with dspr
            un "Well, here comes the evening."
            "She held out her palm to me, inviting me."
    stop music fadeout 3
    stop sound fadeout 4
    stop ambience fadeout 6
    return

label alt_day4_un_7dl_supper:
    scene bg int_dining_hall_people_sunset_7dl with dissolve
    play ambience ambience_dining_hall_full fadein 5
    play music music_list["a_promise_from_distant_days"] fadein 5
    "How much has happened today, how much will happen today."
    show un normal pioneer with dspr
    "I am drawn and drawn to her. And the occasional flash of amazement peeking out from under my fluffy lashes shows that I'm not the only one."
    th "Maybe that's the reason I managed to get the best out of myself today."
    th "After all, to meet the girl we love, we try to wear only the most dressy, the most beautiful things."
    th "But I have only only pioneer uniform, which no matter how you clean it, no matter how you iron it, it doesn't get any prettier."
    th "So I have to conform, if not in appearance, then at least by actions."
    "Acting generous?"
    "Under that Novocain blockade, I can't be bothered with little things like making my loved ones uncomfortable."
    "After all, I have no loved ones."
    dreamgirl "And that clip with the choice for the mother of which of the two children to shoot, the adopted one or the native - which one would you shoot?"
    dreamgirl "Don't be a yuppie, answer the question."
    th "Honestly? {w}Myself in the head."
    th "I've wanted to see what's on the other side for a long time, but I'm too afraid of the pain."
    dreamgirl "Okay, then, scene number three."
    dreamgirl "If you're going to socialize, it'll be relevant enough for you."
    dreamgirl "You, your girl, the driveway, the gopniks."
    th "I mean, do you have the guts to hold back the mob while the girl does her feet and screams to the police?"
    th "I don't know. {w}The chance of getting out of there alive is minimal, healthy is zero."
    if not alt_day4_un_7dl_dv_us_explosives:
        dreamgirl "Then why did you sabotage the redheads' explosives if you don't care?"
        th "I don't know! I haven't known anything for a long time!"
    th "That's a lot of stress, and I don't know how I'm going to behave in a stressful situation!"
    dreamgirl "And by common sense?"
    if herc or loki:
        th "On second thought, I'll look for something more weapon-like, because in a situation like this, you have to hit only to kill."
        dreamgirl "Doubtful. You value people too much to kill them for nothing."
        th "It's force majeure."
        dreamgirl "Not for you."
    else:
        th "On common sense it would be a state of affect, and I've had them a countless number of times in my life, and I've behaved differently each time, so the tendency is very hard to detect."
        dreamgirl "You're just afraid to admit you're a coward."
    "Cut off the inner voice, shutting up."
    show un serious pioneer with dspr
    "Without preventing me from bickering with myself, Lena chewed unhurriedly, studying me surreptitiously."
    th "I guess I really do seem like a retard to her - especially with these occasional lags of mine."
    show un smile pioneer with dspr
    un "Have you finished your hard thoughts?"
    "Smiled the girl."
    me "You could say that."
    un "Very well. {w}How would you like to go to the pier after dinner?"
    me "I'm in!"
    "I pushed my plate away in disgust - I had no appetite at all."
    un "You haven't eaten anything."
    "Softly chided Lena."
    me "I don't want anything. Well, shall we go?"
    show un smile2 pioneer with dspr
    un "Lets go!"
    stop ambience fadeout 2
    return

label alt_day4_un_7dl_evening:
    scene bg ext_dining_hall_near_sunset with dissolve
    "We were lucky enough to get past both the counselor and Slavya, who was clearly looking for someone to clean up after the concert."
    scene bg ext_boathouse_sunset_7dl
    with dissolve
    play ambience ambience_lake_shore_night fadein 2
    show un normal pioneer at center with dissolve
    "It's just like yesterday - us, the evening, the pier. {w}The only thing missing was the counselor screaming at us."
    "And, of course, how Lena reacted to it."
    show un smile pioneer at center with dissolve
    me "What are you thinking about?"
    un "You won't believe it... About you."
    me "No, I..."
    show un shy pioneer at center with dissolve
    un "I honestly think about you... I can't think about anything else these days."
    un "I know it's wrong, and you can't have a person occupy so much space in one's thoughts."
    me "Yeah, the most important thing is to learn to remember your name at least a little less than once a minute."
    "Mutual infatuation is including similar reactions."
    show un smile pioneer at center with dissolve
    un "Yeah, that's kind of how it goes."
    "I put my arm around her shoulders, pulling her close to me."
    "The sun was going down little by little, and for some reason the streetlights never made it here, where we were standing for the second time."
    show un serious pioneer with dspr
    un "Have you noticed how sharp everything feels here?"
    me "Yeah. It's like the window's been wiped clean, and everything's so bright."
    "I wondered if I should tell her that besides seeing and hearing, people perceive the world with their other senses."
    "But on second thought, I decided to withhold the information - the last time I told a girl that I not only liked to see, but also smell her, she called me a goddamn fetishist."
    "A small thing, but a nuisance."
    "A very beautiful world, very beautiful pioneers, very beautiful feelings..."
    "And exactly the pinch of flaws in the form of redheaded bullies, a lazy counselor, and a narcissistic gym teacher that keeps the world from becoming a stone-frozen perfect statue."
    "Though I still can't shake the thought that I'm acting like I'm in someone's advertising window, and the slogans «undisguised passion», »real feelings«, and other nonsense of the same lapdoc system of savings discounts are blaring over my head."
    "So we sat side by side on the pontoons, dangling our feet in the warm water."
    "She with her head on my shoulder, and me with my arm around her waist..."
    show un shy pioneer at center with dissolve
    un "You like it?"
    "She giggled."
    me "You act like a hourglass-person - from Kaverin's fairy tale..."
    show un laugh pioneer at center with dissolve
    un "Read. {w}Well... Yeah, I guess you could say that."
    if loki:
        me "Are you shy of me, or what?"
    elif herc:
        me "You're so tender now... In the daytime, I had to keep pushing you to make you react in some way."
    un "I'm sorry... But you're still too little in my life."
    un "I paint in the evening, and at night I have colorful, three-dimensional dreams with surround sound, and that's how I take out what's going on inside."
    me "Why not experience emotions as soon as they come in?"
    un "Why?"
    me "So you don't have to worry about what you've experienced and what you haven't."
    show un smile pioneer at center with dissolve
    un "I'm sorry... But I've been used to doubting everything my whole life. {w}And you..."
    un "You've been acting wrong from day one, not the way I'm used to."
    if alt_day_binder != 1:
        un "Starting from the clubs, when instead of smiling or reacting in any way, you just stood there and looked, serious and meaningful."
    else:
        un "And when they sent me to help you, I thought I'd burn of shame."
        un "And yet you looked so serious, so meaningful."
    un "And I don't know how to react to someone's attention at all - not the usual polite, wary kind that I usually get. {w}But yours is... Enthusiastic."
    un "You came - it was the first night when I could not sleep. {w}There was too much to think about."
    with fade2
    "The silence was dragging on, and something urgently needed to be said."
    me "It's good here."
    "I opened my mouth to confess to her what was going on in my heart, but I said something completely different."
    me "Shall we go for a swim?"
    play music music_7dl["take_my_hand"] fadein 5
    "The look is not in the eyes, but in the soul. {w}Whoever knows how to look like that can be both the best friend and the worst enemy..."
    "Because he knows how to see what's going on inside of me."
    th "That's something I've never made a secret of."
    th "My needs are simple - summer, evening, warmth. {w}This girl's hand, responding to a light shake."
    "She thought for an endless half-second before she nodded."
    with fade2
    scene bg ext_underwater_7dl with dissolve
    "And we were in the water like a channel switch - I don't remember anything, neither how we went to the beach, nor why we neglected it and went on."
    "We headed a little farther out: to where the sandy spit went far into the spill, and to the side where no one could find us..."
    if loki:
        "Lena's secret place."
    un "No one will find us here."
    "She confirmed my thoughts."
    "Her head with its two funny ponytails towered over the water, but because of the moon only a silhouette was visible, and the occasional raking of the water with her hands."
    me "I don't think anyone will look for us - it's over an hour before lights out."
    "I lay down on the water and stared into the deep darkness overhead."
    "I don't know these constellations..."
    th "But maybe that's not such a bad thing?"
    th "Since they're derelict, not salivated over by numerous astronomers and sailors, why not take advantage?"
    "And someday someone will open a newspaper, the «horoscopes» section, and read, «Everyone born under the constellation Lena is guaranteed success in all endeavors today.»"
    un "What are you thinking about?"
    "Lena finally broke the silence."
    "Her voice sounded close to me."
    me "I think I'm lucky after all."
    un "Why?"
    me "If I'd refused to help at the infirmary then, or even earlier, to go with you to paint..."
    me "Things could have turned out differently, couldn't they?"
    un "I don't think so. {w}I had my eye on you from the first day I met you."
    un "You never had a chance."
    me "Really?"
    "I even lifted myself over the water to see the expression with which the girl uttered it."
    "She was smiling calmly and very warmly, looking at me."
    me "Wow. And you seemed so haughty to me. {w}A real prude."
    me "And also as if you were upset."
    if loki:
        me "Anyway, the fact that you brought me here the day before yesterday... I considered it a temporary weakness."
    elif herc:
        me "And I took your impromptu exposition as an attempt to get away from me."
    "You can bask in her eyes and even drown in them."
    "Her laughter can be taped and played in moments of depression, to remind you that all is not bad in this world."
    un "God..."
    "Laughing it off, she shook her head."
    un "How much time we've wasted..."
    me "You know..."
    "I swam closer to her."
    me "Since we see each other in our dreams anyway..."
    un "Let's act like this is a dream, too?"
    me "Yes! What would you like most?"
    "She swam close to me and put her hand on my chest and pushed me gently."
    un "God, what a fool you are, after all..."
    "I started to say something, but she almost literally jumped on me."
    "Actually, she just straightened up and put her hands on my shoulders and dug into my lips in a strange, familiar kiss, taking me deep."
    "Water rushed into my nose, into my ears, but I didn't pay much attention to it - I was all at her mercy..."
    "A strange kiss, with the tang of burning leaves, acorns, chestnuts, and creosote that reigned unabated over southwest Peter."
    "Time stretched out like a rubber band and made everything superfluous - except the greedy lips and what they wake with their touches - for as long as the breath in trained lungs will last."
    "..."
    "She asked for mercy first and, pushing away from me, surfaced."
    "As always, she wanted to be where the view was best."
    "And I spread my arms apart and let the water push me to the surface."
    "And she was already calling my name from the shore."
    un "Get out if you don't want to stay here tonight!"
    stop music fadeout 3
    "I hastened to follow her advice."
    with fade2
    scene bg ext_un_hideout_night_7dl
    with dissolve
    play ambience ambience_lake_shore_night fadein 2
    show un normal pioneer at center with dissolve
    stop ambience fadeout 6
    return

label alt_day4_un_7dl_evening_dr:
    scene bg ext_dining_hall_near_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 1
    play music music_7dl["dance_with_me"] fadein 2
    "Moving deliberately on tiptoe, we passed Slavya and Olga Dmitrievna - each of them was now fraught, judging by the wandering gaze, with at least an assignment for another plowing session."
    "It was as if I had not come to a pioneer camp to rest, but to some LTO! {w}And if it's a summer camp, where's my paycheck?"
    dreamgirl "Look who's flopping around."
    dreamgirl "You're a bird's-eye, so don't you sit there and chirp... stowaway."
    "We finally made it to the pier."
    scene bg ext_boathouse_sunset_7dl
    with dissolve
    play ambience ambience_lake_shore_night fadein 2
    show un normal pioneer at center with dissolve
    me "To the pontoons?"
    show un smile pioneer with dspr
    un "You ask... Of course, to the pontoons."
    me "In case you decide to go somewhere else..."
    show un smile pioneer at center with dissolve
    "Instead of answering, she pulled me with her, and I could almost hear the heels of undoubtedly far more graceful shoes than unified pioneer sandals tapping on the softened planks."
    "For a split second reality was overtaken by another picture - the leaden October sky, Lena, a little taller, a little more mature, dressed in her cherry down coat and soft gray suede boots, pulling me along with her to the edge of the pontoons."
    scene bg ext_boathouse_alt_day_7dl
    show un serious winter
    show anim_grain
    with dissolve
    un "For some reason I really like being here. And I like it a hundredfold when you're around."
    "Finally we got to the corner pontoon and, without talking, took off our shoes, dropped our socks, and dipped our feet into the warm water - the icy springs weren't getting us here anymore."
    "And thoughts were again occupied with the question - maybe we could steal a catamaran?"
    if alt_day2_us_escape:
        "There were no problems with the boat, but who knows: maybe after our Great Escape, security measures were tightened."
    scene bg ext_boathouse_alt_day_7dl
    with dissolve
    me "It's like we were here once."
    show un shy pioneer at center with dissolve
    un "Really?"
    me "Yes. And besides, were here like... I don't even know. Like very long and intimately acquainted people?"
    if alt_day4_me_neu_transit == '':
        un "I dreamt about you, too. But I dreamt rather strangely, as if we were riding on the subway, holding onto the handrail, the lights going out, and you placing your hand soothingly on top of mine."
        un "And then we get off the train and walk for ten minutes in the dark on the ramp."
        un "Someone is wheezing in the back, someone's already sick at heart, short of breath - and somehow I'm not scared at all."
        un "And I want to see your face... And I can't."
        "So some dream of a girl politely offering to go with her, and some dream of something else? Somebody dreams of a boy already leading somewhere?"
        me "And what makes you sure it's me?"
        show un laugh pioneer with dspr
        un "Yes, because from day one you've been acting like you from the dream - you don't ask for my wish, consent, or permission - you just drag me somewhere."
        me "But I didn't drag you anywhere... It was your idea that we went to badminton, and you didn't seem to mind seeing the concert..."
        show un grin pioneer with dspr
        un "I don't mind. On some subconscious level I feel that you won't hurt me."
        th "I wish I had at least fifty percent of that certainty."
        un "And as long as I'm around you, nothing, nothing bad will happen."
        "Holy simplicity."
    th "And a cat came to me and laid its whiskers, paws and belly on me, said «I love you», and licked my nose."
    th "And what I'm supposed to do about it now - no one cares."
    "I finally recognized that exciting sweet citrus scent emanating from her funny hair."
    me "Grapefruit."
    un "What?"
    "I smiled."
    me "Your hair smells like grapefruit. I have a very strong sense of smell working here, and I catch smells - so I'm slowly beginning to understand yours, too."
    show un smile pioneer with dspr
    un "Are there many of them, smells?"
    show blink
    "I smiled and closed my eyes."
    me "More than one. {w}The hair itself smells like grapefruit, but at the roots the smell fades away, leaving a healthy smell of clean hair."
    "Unable to resist, I ran my fingertips down her neck, and she giggled."
    un "More..."
    me "If you look further, you smell like some kind of parfume, but you've been using it since this morning, so it's almost weathered out, only a hint remains. The skin itself smells like sunshine and, for some reason, poplar blossoms."
    scene bg ext_boathouse_sunset_7dl
    show un grin pioneer
    show unblink
    un "You're strong! You have the nose of a sheepdog!"
    me "Thank you, I haven't been compared to a sheepdog yet..."
    "I grumbled, trying to disguise my embarrassment."
    un "Don't pout, I'm complimenting you."
    me "I'm not pouting. It's just..."
    "I waved my hand."
    show un grin pioneer close with dissolve
    "I pressed her to me and laughed."
    "Who cares! She can call me anything she wants."
    "The day was drawing to an evening - and in warm company twice as fast."
    stop ambience fadeout 6
    return

label alt_day4_un_7dl_dock:
    scene bg ext_boathouse_night with dissolve2
    play ambience ambience_boat_station_night fadein 3
    show un smile pioneer at center with dissolve
    un "And again you, me, the night and the pier."
    un "Do you think it's a coincidence?"
    "What do I think? I think you are very beautiful. I think you are incredibly intelligent. {w}A deadly combination."
    "I think I've lost what hope I have left. That it is the middle of summer, and I have a long black winter, in a whole lot of sense."
    "Petersburg. That it's cold, outside and inside."
    "A baggy coat, earplugs and depersonalizing bangs over my eyes."
    un "You're withdrawn, silent. Olga Dmitrievna said you have no friends at all."
    me "She didn't lie."
    "Morituri te salutant..."
    dreamgirl "What are you afraid of? {w}What do you want?"
    th "I'm afraid of my happiness, afraid to believe in it. {w}And most of all, I'm afraid to admit to myself how screwed up I am."
    show un grin pioneer at center with dissolve
    me "So my best friend is you. And part-time girlfriend."
    show un laugh pioneer with dspr
    un "Wow, what a responsibility."
    un "I hope I can do it!"
    "I think you can put a nice fat dot in the narrative here, so that Vasilisa the Beautiful never walks through the house in a dirty apron and Ivan the Tsarevich never shows up home drunk."
    "After all, nothing can spoil any most magical romantic tale so much as a domestic postscriptum."
    me "I'll help you."
    "Seriously I promised."
    un "How?"
    show un smile2 pioneer at center with dissolve
    me "Come on, sunshine."
    "I smiled, struggling to wipe the already heavy sleep from my eyelids."
    "It was late, and the moon, finishing its another supermoon, had made its way into the sky - and it seemed like I could reach out and take it."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day4_un_7dl_sleeptime:
    scene
    $ renpy.show("bg ext_square_night", what = Notch("bg ext_square_night"))
    with dissolve
    play ambience ambience_camp_center_night fadein 3
    play music music_7dl["melancholy_sun"] fadein 3
    "..."
    "Another day away, the centerpiece of my magical journey - but just the starting point in a far more exciting adventure whose name is Lena."
    "Maybe it's for a few months, maybe a couple of years."
    "But what the hell - it could be for life."
    "And it doesn't scare me. It's so weird. A girl from whom I would have run away myself in a past life..."
    scene bg ext_house_of_mt_night
    with dissolve
    play sound sfx_knock_door2
    pause(1)
    "No answer."
    play sound sfx_open_dooor_campus_1
    scene bg int_house_of_mt_night2
    with fade
    pause(1)
    play ambience ambience_int_cabin_night fadein 1
    "The picture of us stomping through the city toward each other, panting intently and looking under our feet:"
    "I - right hand in my pocket - earplugs - with a bag on my shoulder - with a cigarette wedged between the middle and ring fingers of my left hand."
    "She is in a beautiful cherry coat, with a bag on a low strap, slapping her hip with every step."
    "We meet eyes, cross paths, interlock... And after a second, shuddering, break contact."
    "We pass by."
    "We're both afraid of someone else getting into our souls and getting dirty."
    "Right now, these experiences bring only a kind, condescending smile."
    "Still, we found each other, and that's the most important thing."
    "I threw off my clothes and dove into the cool sheets, soaking up the buzz with all my senses, all my fibers - the stretching of my arms and legs, the memories of today, and most importantly, the anticipation of tomorrow."
    "Of course it is. It's only just beginning."
    th "What a silly smile I must be having right now."
    "Thought I, letting Morpheus take me to his domain."
    stop music fadeout 4
    with fade2
    "The way the door opened, the counselor, staggering and moving on wobbling legs, went to her bed without turning on the light, and stretched herself sweetly, I noted purely automatically."
    scene bg black with fade2
    pause(2)
    "I had a dream."
    "A dream in which a door opened inaudibly, and someone moved me, poking me painfully in the side with their fist, to the side and crept under my side."
    "I was about to wake up and curse, but «someone» showed wonders of coziness by instantly getting under me, and, covering with my paw like the warmest blanket, sighed happily."
    "And I sighed in unison, inhaling the already familiar - «multipassport» - bitter aroma."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day5_un_7dl_begin:
    play music music_list["waltz_of_doubts"] fadein 3
    play ambience ambience_7dl["rain"] fadein 3
    scene
    $ renpy.show("bg int_house_of_mt_sunset", what = Rained("bg int_house_of_mt_sunset"))
    with fade2
    "That dream was too sweet to be true."
    "It always is, though."
    "All the best things that happen to us happen in dreams."
    "And it doesn't matter if it's a dream of the mind, of the consciousness, or of that very sense of time that distinguishes humans from large predators."
    "I close my eyes in April and wake up in December, remembering that it turns out the London Symphony Orchestra was coming to town in the fall, and they even managed to get me out to see it."
    "And here... I closed my eyes after the dance and still don't seem to wake up."
    if alt_day4_me_neu_transit == '':
        "This is always the case when one begins to occupy too much space in one's head: little by little, the tired mind dumps some of the thoughts into the subconscious, and the result is the very dreams of which Lena spoke - colorful, colored, with a three-dimensional sound."
    "I dreamed of strands of dark, violet-colored hair, soft to the touch, tart to the smell - and the stirring intimacy of a very slightly wet girl's body."
    "The very impression that can latch on so firmly, that dreams begins to appear by themselves."
    "Sweet, sweet dreams in which she smiles and says hello. {w}And when the hormonal imbalance gets too much nerve, the ones where Lena comes to sleep over."
    th "I can't, shouldn't go crazy about anyone with that kind of power. Because only from the top can you see how deep the abyss is."
    th "My subconscious created Frankenstein's monster - for knowing what a girl smells like, how could I know what she feels like?"
    th "Of course we cuddled, but I didn't give my hands much free rein."
    "For lack of information one hundred percent was set up with something from my old experience."
    "She brought the icy cold with her and waddled into me, shivering, resting her icy heels against me, hiding her icy palms under my armpits."
    "My dream, my dream... There was no additional implication in her behavior, she just came and snuggled under my side."
    scene cg d5_un_bed_7dl with dissolve
    "And when I, smiling into a sweet sleep, tried to roll over onto my other side, she grumbled unhappily and put me back in my place."
    "Hiding between me and the wall from the rising Olga Dmitrievna."
    "If one could have dreams to order - those in which some part of objective reality remained intact as a framework - what would one fill one's dreams with?"
    "I had to learn by experience that all my former aspirations meant nothing more."
    "Perhaps that's why I didn't panic or be surprised when the sequence of events followed the slamming door and an adorable head with ubiquitous ponytails appeared from under the blanket, and the girl settled on my shoulder, after a little wiggle, and after a moment's hesitation opened her eyes."
    un "Hi..."
    "Makes sense."
    me "Hi."
    me "May I ask an immodest, indecent and deeply intimate question?"
    un "You can try."
    "She put her arm around me and rubbed her nose on my shoulder."
    me "You know you're in my bed, don't you?"
    un "Well...I guess."
    "The girl smiled slyly."
    me "And what are you doing here, may I ask?"
    un "Silly... lying. Don't you understand?"
    me "So the fact that I'm sharing a cabin with a counselor doesn't bother you?"
    un "Oh ... {w}Do you think she'll get jealous?"
    me "Lena!"
    un "Okay, okay... Just kidding. So what did you want to know?"
    me "Why did you come?"
    un "I got a little sad last night... And since some days I don't know any other way to fight moping than to snuggle up to you. Suffer with me now."
    me "Are you serious?"
    scene
    $ renpy.show("bg int_house_of_mt_sunset", what = Rained("bg int_house_of_mt_sunset"))
    if persistent.hentai_graphics_7dl:
        show un sad sleep
    else:
        show un sad pioneer
    with dissolve
    un "More than you think."
    "Quite seriously, the girl replied, throwing back the blanket a little, giving me a chance to appreciate the extravagance of her attire."
    "A gray-green nightie that looked more like a tank top and, judging by the fact that the bed wasn't full of sand, some sort of shoes."
    me "And you came in this? Are you crazy?"
    un "Yes!"
    "The madness splashing in her eyes would have been enough for some Ulyana or Slavya, but not for the melancholy child I knew Lena to be."
    me "What am I going to do with you?"
    "I sighed."
    "I tried to move away so as not to tease myself or embarrass her."
    dreamgirl "Oh yeah, she'll definitely be embarrassed!"
    me "You don't know what you're talking about."
    if persistent.hentai_graphics_7dl:
        show un surprise sleep with dspr
    else:
        show un surprise pioneer with dspr
    un "It's not like I'm ten years old..."
    "Softly she rebuked me, pressing herself even tighter against me."
    un "And I have a rough idea what it's about."
    "And how do you talk to her like that? She's like a cat in the middle of nowhere; she'll only listen to the voice of reason if it hits her on the head!"
    dreamgirl "Listen to me for once in your worthless life. Kick her out of bed. Kick her in the neck."
    th "Look who's singing! Is that you?"
    dreamgirl "Me, me... Events are not in your favor, that most amazing unfortunate combination of factors. If it had turned out any other way, she would never have gotten away with it."
    dreamgirl "That may have been the bet."
    dreamgirl "But if the counselor burns you - not only will she blow you away, she'll figure out how to settle you so that you'll not be able to contact till the end of the shift!"
    th "So what do we do?"
    dreamgirl "Kick her out. Use force if you have to."
    th "But I don't..."
    "Two things happened at the same time - the alarm clock rang, making the girl shudder, who had already found everything she wanted with her palm, and the silhouette of Olga Dmitrievna in her ubiquitous panama loomed in the swinging door."
    show mt normal panama pioneer at right with dspr
    stop music fadeout 1
    mt "Semyon, Go..."
    with fade
    "A silent scene."
    "The counselor caught sight of the girl lounging next to me, and purely mechanically took the fortissimo available to her."
    "Lena squeezed my hand in surprise, and I gave a half strangled grunt."
    "It's been quite a morning!"
    play music music_list["awakening_power"] fadein 2
    show mt angry panama pioneer with dspr
    mt "Semyon?!" with vpunch
    "Drunken-wrinkled pioneer counselor. {w}Judging by the distinctly green hue of her face, last night's party was a success, and our perfect counselor was now suffering from withdrawal syndrome."
    "She herself grimaced at her own scream, but decided to press on until she won."
    mt "Semyon, what's the pioneer girl doing in your bed?"
    me "Lying, don't you see?"
    if herc:
        me "Though something tells me that even if she wasn't just lying there - you wouldn't even pay attention at night!"
        mt "I don't quite understand what you..."
        me "Come on. I could see your condition just as well as your clothes."
        show mt surprise panama pioneer with dspr
        mt "So you..."
        "I nodded."
        th "In all detail."
        th "And if it hadn't been boring, you could have captured the shot for posterity."
        show mt angry panama pioneer with dspr
        mt "You were peeping!"
        me "Yep. You're in the middle of the room in your Eve costume, stretching and staggering around in a state of stupor."
        "I laughed."
        me "Of course I was peeping."
        show mt normal panama pioneer with dspr
        "Olga wanted to bark something, but, groaning, grabbed her temples and sank to her made-up bed."
        if persistent.hentai_graphics_7dl:
            show un scared sleep at left with dspr
        else:
            show un scared pioneer at left with dspr
        un "Olga Dmitrievna!"
        "Lena rushed to help the counselor - completely contradicting her own words about the eternally Swiss politics."
        mt "Leave me alone, pioneer girl, go get dressed better."
        if persistent.hentai_graphics_7dl:
            show un surprise sleep with dspr
        else:
            show un surprise pioneer with dspr
        un "But..."
        "Instantly realizing the meaninglessness of any words, Lena turned around and headed for the exit."
        "Throwing an indignant look at the counselor, I jumped up from the bed - as I was, in my boxers - and, catching up with the girl, embraced her."
        me "Olga Dmitriyevna, what do you think you're saying?!"
        me "In a nightgown through the waking camp. Can't give her even a shirt!"
    else:
        if persistent.hentai_graphics_7dl:
            show un sad sleep at left with moveinleft
        else:
            show un sad pioneer at left with moveinleft
        "Lena climbed over me and stood by the bed, stubbornly looking at the counselor."
        un "I did that."
        un "I came."
        show mt rage panama pioneer with dspr
        mt "I guessed it already!"
        me "I wonder what it was that you guessed about? You're still hung over..."
        "I grumbled, getting up."
    "I scratched the back of my head, wrapped the girl in the blanket that was lying there, and pushed her toward the exit - it wasn't appropriate to run naked through the street, but sitting here now was somehow... irrelevant."
    stop music fadeout 5
    mt "Don't go."
    show mt normal panama pioneer with dspr
    "The counselor cooling down."
    mt "It's raining - you'll be soaked in no time."
    mt "I'll get you some clothes: I have a spare set."
    if persistent.hentai_graphics_7dl:
        show un surprise sleep at left with dspr
    else:
        show un surprise pioneer at left with dspr
    un "T-thank you..."
    "I suddenly remembered the night painting... And then what was under my palms..."
    play music music_list["everyday_theme"] fadein 5
    show mt angry pioneer with dspr
    mt "Semyon, will you turn around?"
    "She finally threw off her now irrelevant panama and looked at me angrily."
    th "Why, I wonder? As if there's something else I didn't see?"
    hide mt
    hide un
    with dissolve
    "But obediently turned away - and immediately, slapping the forehead with the palm of my hand, reached for my shorts and shirt."
    "The costs of being raised in a sorority - sooner or later one completely stops being embarrassed about one's own nakedness in the company of women. Even if the women are conventional..."
    dreamgirl "Did you call the counselor a conditional woman? Or was it Lenochka?"
    th "Well... They're girls. Not women."
    dreamgirl "Uh-huh. Keep drowning yourself."
    dreamgirl "Don't you want to share with the non-women?"
    th "Point out which way to «... yourself»?"
    with fade2
    "Lena did it in a minute - almost within the army norm."
    show mt normal pioneer at cright
    show un normal pioneer at cleft
    with dspr
    "The uniform was clearly too big for her, but for lack of alternatives, it went as well."
    "Judging by the relatively stable condition of the counselor, she also managed to take a pill of citramon in between."
    mt "Okay, we're all dressed and packed. Let's talk."
    show mt angry pioneer at cright with dspr
    mt "Semyon, don't even think about turning this to giggles and farce."
    show mt normal pioneer at cright with dspr
    mt "According to camp rules, what happened is considered an extraordinary incident and is punished by the comrades' court for immorality."
    th "Is it the norm to drink after lights out and come in bare-assed?"
    th "Okay, whatever about bare ass, personally I'm all for it. What are we gonna do about the fact that I live in the same cabin with an attractive young counselor?"
    th "If I remember correctly, the impotent prudes in the prudish department were very fond of sending the caught ones to the opposite ends of the globe."
    "And the only way to save the relationship in this case was to immediately apply to the registry office."
    me "I love the Union."
    me "What do you suggest?"
    show mt sad pioneer with dspr
    mt "Nothing."
    $renpy.notify('VLKSM - All-unionized Lenins Communist Union of Youth.')
    mt "I'm writing a characterization of you to the VLKSM, as young people who prefer to work together... In a whole bunch of senses."
    show un shocked pioneer at left with dspr
    un "But how..."
    mt "And that's it. I'll keep that characterization for the rest of the shift."
    mt "I don't forbid you to see each other or anything like that."
    mt "But one more bed scene like that..."
    show un scared pioneer
    show mt angry pioneer
    with dspr
    extend " You understand?"
    "We nodded in unison. What's not to understand?"
    show mt smile pioneer with dspr
    mt "Great."
    "The counselor smiled and stretched until she crunched, tightening her full breasts with her wet shirt - and I realized that she hadn't had time to put on all her underwear since this morning."
    mt "I even regret, somewhere, that we came to an agreement."
    if alt_day4_me_neu_transit == '':
        mt "Who would have thought that two of my sullenest pioneers would get together."
        show un shy pioneer with dspr
        mt "And, most importantly, when did they have time..."
    mt "All right. {w}Get out of my sight."
    "She waved her hand, chasing us away, but I decided to clarify:"
    if herc:
        me "Allow a substantive question."
    else:
        me "Let me clarify something."
    "I threw a glance at the watch."
    me "It's close to nine, why aren't there lineups and exercises and the like?"
    show mt laugh pioneer with dspr
    mt "It's raining! Would you want to stand at the lineup in the rain?"
    me "Uh..."
    "I answered diligently."
    th "Who knows you fanatics."
    th "Maybe even death isn't an obstacle for you to attend the lineup. As long as the counselor's hopped up on the flyer."
    mt "Get your raincoats from that cupboard over there."
    un "No need... I have an umbrella."
    th "Mademoiselle knows a lot about romance."
    mt "As you wish."
    play sound sfx_7dl["eat_horn"] fadein 1
    mt "It's time for breakfast."
    "A little woodenly laughed the still-unrelaxed counselor."
    mt "Run along now!"
    play sound2 sfx_open_door_clubs
    pause(1)
    scene cg d5_rainy_idle_7dl with dissolve
    "And it really was raining outside!"
    stop sound fadeout 3
    stop music fadeout 3
    stop ambience fadeout 3
    with fade2
    return

label alt_day5_un_7dl_breakfast:
    scene bg int_dining_hall_people_rain_7dl with dissolve
    play ambience ambience_medium_crowd_indoors_1 fadein 3
    play music music_list["your_bright_side"] fadein 3
    "Breakfast was like breakfast: wheat porridge «Zarya Polya» with condensed milk, semi-sweet tea «White Nights» and two sandwiches with cheese and sausage."
    "Compared to yesterday, though, when we were almost fed cutlets for breakfast, it was a pretty decent ration."
    "It suddenly occurred to me that, for the pioneer-regimen of that time, the perpetual routine of adjusting the body like clockwork was more of a boon than a restriction - he was smoothly, almost without noticing the difference, joining the military first."
    "The latter, of course, had its difficulties, but they were psychosocial moments rather than regime ones."
    "And then the transition under the wing of the Union, to the state structure. At that time there were no private shops, and without exception everyone worked for the good of the motherland."
    "And what was it like for me, who had lived by a schedule since I was a toddler, who had built my body the way not every bodybuilder did, and who knew every strength and weakness thoroughly, to fall off at the finish line."
    "Just because I wanted to celebrate graduation with the boys one day, and there and granite slabs of cladding seemed appropriate for a nap."
    "Diagnosed with chilled kidneys, an end to a career in the Air Force and the loss of half the motivation to exist."
    "And yet I could do it. After all, I've been going for it all my life."
    "Seated next to me, Lena immediately nudged her plate toward me."
    show un smile pioneer at center with dspr
    un "Go ahead, I know you need to."
    me "I won't say no, of course, but you..."
    show un smile2 pioneer with dspr
    un "Eat, I know you need it more than that. {w}You still have to defend us from Olga Dmitrievna."
    me "Len, no kidding. I'm immensely flattered by what you did, but can we coordinate this a little bit? At least I'll steal the key to the cabin, where no one will disturb us."
    show un grin pioneer with dspr
    un "Oh, how thoughtful! Can you get the key?"
    if alt_day1_sl_keys_took in (1, 3):
        if not (dr and ('nwsppr' in list_clubs_7dl)):
            me "Actually, it's a secret."
            "Looking around, I switched to whispering."
            me "But I already have the key, and if you suddenly..."
            show un smile3 pioneer with dspr
            un "And where did you get that?"
            me "Company secret!"
            "I answered proudly."
    else:
        me "I can do it! I have some ideas."
        un "I believe in you."
        "A picture from the past: we shuffle through my backpack, my jacket, my pants looking for the key, looking and not finding it - we end up finding it in her pocket."
        "The door rattled against the lintel, slamming shut, but we didn't care anymore - like two sick, two crazy people, we couldn't and wouldn't unclench."
        "The clothes flew to the floor in the first twenty seconds, and through a brief struggle I still lifted her into my arms and solemnly carried her into the bedroom."
        "There were accusations of insanity, threats to flounder, statements that she was heavy - I listened to nothing. I'm like those same Chinese people who do their thing in silence."
    me "In my day, a girl wouldn't let me move on to the next stage until the second or third date..."
    "I grumbled."
    show un laugh pioneer with dspr
    un "So you do the math! A date lasts an average of four hours, so that if anything happens, people don't piss each other off."
    un "And how long have we been together? Practically forty-eight hours."
    "She threw off her sandal and stroked my foot under the table."
    un "You can consider this our ninth to tenth date, since you're suffering from your puritanical scruples. And we're by all your rules already late!"
    show un smile2 pioneer with dspr
    me "Your logic makes me sick. But... Okay. I like it just fine."
    th "Except for the girl's inexplicable enthusiasm for me."
    me "Lena, tell me..."
    "I asked cautiously."
    if alt_day4_un_7dl_calm == 'un':
        me "You said something about an unpleasant experience..."
    me "Did you date someone before, and did he hurt you?"
    show un sad pioneer with dspr
    pause(.3)
    show un smile pioneer with dspr
    "For a moment Lena's face transformed, but she quickly pulled herself together."
    "And I could have sworn I did - something stirred inside me at that moment."
    "Some gut feeling told me that the cause of the sadness and longing in her eyes was none other than me."
    dreamgirl "Yeah, and that feeling is called «ugly duckling syndrome.»"
    th "Screw you."
    un "Let's not talk about it, okay?"
    me "Whatever you say."
    un "Let's just say he didn't reach the bar."
    me "And I am?"
    show un grin pioneer with dspr
    un "Oh, you're setting new standards. You're as strange as I am, yet sometimes you look at me in a way that makes me lose my footing."
    me "All right, migratory bird."
    "I finished my porridge and put the plate aside."
    me "What silly things shall we do after breakfast?"
    show un normal pioneer with dspr
    mt "I don't know about silly things, but Lena will go to the wall newspaper, and you, Semyon, will be in charge of the younger squads' leisure time."
    show mt normal pioneer at right with dspr
    th "Uh, not again!"
    me "Why the hell would I do that?"
    "Judging by the resurrected skill of silent movement, Olga Dmitrievna has successfully eliminated the half-life products of alcohol from her blood."
    mt "Officially, because, excluding Slavya, you are the most responsible pioneer in the squad."
    if alt_day4_un_7dl_ducks:
        mt "You helped on the second day with the organization of the card tournament, on the third day you sorted out the medicine, and yesterday you showed the world the wonders of pedagogical talent, teaching the sixth squad to dance so that they took the audience award."
    else:
        mt "You helped on the second day with the organization of the card tournament, and on the third day you sorted out the medicine."
        show un surprise pioneer with dspr
        mt "Well, if I were Lena, I'd hold on to you more tightly."
    me "Only an idiot believes the official story."
    show mt grin pioneer
    show un smile pioneer
    with dspr
    mt "Look, you asked for it..."
    me "For what?"
    mt "I just know how much you don't care about adult inhibitions, especially when you're young, stupid and in love."
    mt "And you are in love. That's all."
    show un shy pioneer with dspr
    "I blushed."
    un "W-what..."
    show un surprise pioneer with dspr
    mt "That's why I'm doing this, so you two don't do anything stupid."
    me "Damn human soul engineers... Did they teach you that, too?"
    show mt laugh pioneer at right with dspr
    mt "We've been taught a lot of things."
    th "Yes. Especially to show up at a pioneer's cabin of the opposite sex in a state of stupor."
    if loki:
        me "And if we don't agree?"
        "I asked."
        mt "You have no choice. {w}It's either that or house arrest - for someone messing up a monument at night. And we have witnesses that Lena and you, Semyon, went out at night."
        th "What a goat!"
        th "{image=alt_KS_censor}!"
        me "Blackmail, huh? Well, well."
        me "You can try to force us."
        "I nodded to Lena and, taking her by the hand, dragged her with me, not listening to the shouting behind us."
        "Everything I wanted, I heard."
    elif herc:
        me "Olga Dmitrievna, may I have a word?"
    else:
        me "If you say so."
        "I nodded placidly."
        me "Leisure time so leisure time. But keep in mind: it's only until dinner!"
        me "And woe to whoever comes between me and him!"
        un "I shall miss you."
        hide un with dissolve
        "Lena kissed me on the cheek and ran away."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day5_un_7dl_breakfast_l:
    scene bg ext_clubs_rain_7dl with dissolve
    play music music_list["so_good_to_be_careless"] fadein 5
    "I don't know how to call what was going on inside me - a few words dropped by a seemingly stranger."
    "It's an old story - they both have a soft spot for each other. And they're both the last to know it."
    "One wants to laugh and cry with the overflowing ecstasy, not because one has gone mad, but because one is not alone."
    "A man can never have enough of a good thing; he wants the best."
    "As in my story, to hide from the rain under a bush, under a pink blouse."
    "I myself grinned at the picture."
    "We went on our way."
    if alt_day_binder != 1:
        "And they turned out to be looking in the direction of the same building where we first met."
    else:
        "And they appeared to be looking in the direction of the local tech headquarters."
    "So already there was Electronik, locking the door."
    "Dragging Lena with me, I ran onto the porch and shouted to the boy."
    me "Hey! What are you doing?"
    show el normal pioneer with dspr
    el "Oh, hey. And I'm closing the club."
    me "Really? And why is that?"
    el "Shurik's in the hospital, and I can't do cybernetics by myself."
    me "What do you mean, hospital?"
    "I was surprised."
    me "I just saw him healthy a couple of days ago!"
    show el normal pioneer with dspr
    el "Well... You refused to help us the day before yesterday... Just don't think I'm accusing you of anything - I understand when a girl demands..."
    show un angry2 pioneer at left with dspr
    un "Don't get distracted."
    "Lena quickly cut off all the sideways."
    el "That's what I said."
    "He was in a hurry."
    el "The day before yesterday Shurik climbed on the roof, slipped, fell and unluckily caught his hand on the edge of the roof - cut to the bone. That's it."
    show un surprise pioneer with dspr
    me "Wow! How is he?"
    el "He was still alive yesterday: Violetta took him to the district center - they haven't come back yet. So they'll probably put him in the hospital."
    me "That's a shame."
    th "Although, even if I was aware of it - to hell I would choose the safety of some unknown to me Shurik, when Lena is at my side asking to help sort out the medication."
    el "So I'm handing over the keys now to Olga Dmitrievna and I'm off to do the little ones' leisure activities. {w}All strictly in accordance with the order of the highest authority."
    "It occurred to me that I know practically nothing about Electronik - and now, if that last phrase had come out of my mouth, you could see the sneer there with the naked eye."
    "And he's smiling as if nothing had happened."
    me "There's no sun today, so she'll probably be in the indoor stadium."
    el "Thank you! Where are you going by the way?"
    me "Uh... well, we. Uh."
    show un smile pioneer with dspr
    un "And we're going to check the gatehouse."
    "Lena came to my rescue."
    un "Olga Dmitrievna told us to gather who we could - the corner was washed away by the rain."
    "I could see from the cyberneticist's face that he didn't want to end up in the role of a plowman, because he instantly hustled, scurried off, waved goodbye to us, and disappeared in an unknown direction."
    hide el with dissolve
    show un smile pioneer with dspr
    me "What a liar you are, crafty..."
    "I shook my head."
    $renpy.notify("Idiom - means «That's our principles».")
    un "That's where we stand!"
    "She wrapped her arms around me and exhaled hotly into my neck."
    un "So what? Where does a cavalier take his lady? {w}Not to the woods under a bush and a pink blouse?"
    "Looks like we were thinking in the same direction."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day5_un_7dl_clubs:
    scene bg ext_clubs_rain_7dl
    show un smile pioneer
    with dissolve
    play music music_list["you_won_t_let_me_down"] fadein 5
    me "Actually, I have a different idea."
    play sound sfx_keys_rattle
    "The bundle jingled in the palm of my hand."
    show un laugh pioneer with dspr
    $renpy.notify("Idiom - means «You have solution for everything».")
    un "It's hard to get lost with you! Open up!"
    me "Noooow..."
    hide un with moveoutleft
    show mt rage pioneer far with moveinright
    "I don't know why, but when I picked up the key, I kept looking around, which saved us from Olga Dmitrievna rushing to the gate."
    hide mt with moveoutright
    "We rolled instantly onto the concrete path behind the bushes and, crouched there, watched the counselor gallop off at full speed, muttering something about unwanted pregnancies and goddamn doofy-eyed kids."
    "The shirt gave up instantly - it was only worth breaking into the hawthorn bushes, and the freezing rain that rolled down my scruff made me forget to take a breath for a while."
    un "S-s-s-s-s..."
    "A few minutes later, Lena whistled through her teeth."
    "She was soaked through that her shirt, which had become see-through, clung to the shapes of the most seductive topology. But there was no time for silliness now - she already had blue lips."
    "Bruh."
    th "It would be perfect for her to catch a cold now..."
    "I shouted at my conscience."
    th "Or are we both..."
    "I shook my head in the negative."
    th "Sorry, honey, we'll just have to be patient for a while."
    "I pulled her to me, warming her as best I could - though what could I do, myself soaking wet?"
    "Kissing her with icy lips is warming except psychologically."
    "We sat there for ten minutes, until I, as the leader, almost lost my patience."
    "And just as I was about to go up to the porch and return to my glorious activities as a safecracker, the same Olga Dmitrievna dashed back the other way."
    show mt feared pioneer with moveinleft
    th "Holy crap, it's not even a year passed! The efficiency is off the charts."
    "All that's left in the world is damp, cold, and, I wondered to myself, Lena."
    th "Wow."
    th "I'd forgotten when I cared for someone like that... So..."
    "The arm around the girl was stiff, but I stoically clenched my teeth and didn't let myself move until Olga walked by."
    "The counselor was no drier than we were, and that was the only thing that warmed me up, for better or for worse."
    "And she wasn't even looking around anymore - no, this time her determination would have been the envy of any other locomotive: not feeling the ground beneath her, Olga raced, staring at one point."
    "Clearly in a hurry to change her clothes and get at least a little warm."
    "Hence the question - whether she even cared about silly things like searching for a lost couple - didn't even come up."
    hide mt with moveoutright
    "Fifteen seconds later, her stomping ceased around the corner, and I, with a nod to the girl, crept out of our hiding place."
    "She had warmed up, but she grumbled protestingly, not wanting to get out of any kind of warmth, so I actually had to carry her on my back to the clubhouse."
    scene bg int_clubs_male_rain_7dl with dissolve
    play music music_list["smooth_machine"] fadein 5
    "We crawled into the club and couldn't get warm for a long, long time."
    "We bared our teeth, fought and cuddled - the cold turned off half our instincts."
    "And a few seconds later, bales of unopened bed sets caught my attention."
    me "Get undressed."
    "I told her, not believing myself that I was suggesting such a thing."
    show un surprise pioneer with dspr
    un "What?!"
    me "Take off your clothes, I said."
    show un shy pioneer with dspr
    un "W-why?"
    th "Why-why, I'll pile on the table and there... What a question..."
    me "Do you trust me?"
    show un surprise pioneer with fade2
    un "Yes..."
    "She blushed and, lowering her eyes to the floor, slowly pulled her tie."
    me "What are you digging for!"
    "I walked right up to her and managed to unbutton her shirt, letting out her breasts, which had never been pulled together today by the extra protection of a bra."
    "And then it just dawned on me what I was even doing..."
    "But eyes - fear, hands - doing; there was no time for foolishness now, both risked coming down with pneumonia."
    "She dutifully turned around, putting her clasps and buttons under her hands, stubbornly looking at the floor and blushing her cheeks."
    "I wasn't paying attention to that - I was fighting with the skirt. It was only when it slid down to mid-thigh that I suddenly remembered..."
    me "Now yourself."
    "I was embarrassed myself, amusingly duplicating the reactions of a girl who, despite her redness and body-swallowing shame, was clearly going to move all the way - whatever that means."
    un "O-okay..."
    hide un with dissolve
    "She fiddled for a minute more, and then she called out."
    un "I'm finished..."
    if persistent.hentai_graphics_7dl:
        show un serious sleep with moveinleft
    else:
        show un serious pioneer with moveinleft
    "Well, I turned around..."
    hide un with moveoutright
    "...and then I turned back - Lena was standing across me, embarrassed beyond belief, but stubbornly refusing to cover herself."
    me "Are you going to stand there, my woe?"
    "I asked affectionately, glancing at the figure with interest."
    un "But we..."
    "She paused with a hint."
    me "No «but» until we're dry and warm. Here."
    "I threw her a package of fresh sheets."
    me "Open it up and wrap it around, we'll be like Roman patricians now."
    un "And y-you?"
    "She bared her teeth."
    me "I what? {w}I'm going to change too now!"
    un "Well... Somehow, I guess..."
    if persistent.hentai_graphics_7dl:
        show un sad sleep with dspr
    else:
        show un sad pioneer with dspr
    un "There..."
    "Now I felt much more confident."
    "Lena wrapped the sheet around her body and threw the loose corner over her chest so that it closed in a classic toga. {w}Flattering."
    "I loosened the strap and pulled my shorts down."
    un "Yeah, by the way... How about we warm up a little?"
    dreamgirl "And then she's like, turns off the lights, stabs you with a knife, and escapes via ventilation shaft!"
    th "Rambler..."
    "Lena looked for something in the nightstand and revealed a roll of twine."
    un "W-we'll h-hang the c-clothes now."
    "She still couldn't get warm, and was diligently pushing the shivers inside her."
    th "My poor sunshine. {w}Now."
    "The unpleasantly sticky clothes finally gave up and let themselves be removed, and a second later a cool, dry sheet lay on her shoulders."
    me "I'm all for it."
    me "Where to sit down... Or better yet, lie down."
    if persistent.hentai_graphics_7dl:
        show un serious sleep with dspr
    else:
        show un serious pioneer with dspr
    un "The cyberneticists here had a mattress. We can take it."
    me "And how do you know everything?!"
    "That girl surprised me sometimes!"
    if persistent.hentai_graphics_7dl:
        show un grin sleep with dspr
    else:
        show un grin pioneer with dspr
    un "Well... I've been here two weeks longer than you."
    un "I've learned a few things."
    me "Is there a tea and boiler here, too?"
    un "Of course there is."
    if persistent.hentai_graphics_7dl:
        show un laugh sleep with dspr
    else:
        show un laugh pioneer with dspr
    extend " Behind you."
    me "Shaman, no less."
    "I nodded meaningfully, pulling out a bar of pressed Kazakh black and a box of refined chocolate from the nightstand."
    me "Now we're going to get warm, and..."
    un "And?"
    if persistent.hentai_graphics_7dl:
        show un grin sleep
    else:
        show un grin pioneer
    "If it weren't for the unrelenting trembling of the girl's body, I could have sworn I could see the slyness in her eyes."
    un "What then?"
    me "What do you think?"
    "I tried to pretend to wink meaningfully, but it didn't work very well on my cold-stricken face."
    if persistent.hentai_graphics_7dl:
        show un serious sleep with dspr
    else:
        show un serious pioneer with dspr
    un "I can think of a lot of things. {w}No innuendos, please."
    me "I don't know... Personally, I wouldn't mind taking a nap. {w}I don't know about you, but I didn't get much sleep."
    me "You don't know why that would be?"
    if persistent.hentai_graphics_7dl:
        show un smile3 sleep with dspr
    else:
        show un smile3 pioneer with dspr
    un "I can't even guess. It's been a long time since I slept this sweet."
    "I couldn't help myself and poked my tongue at her, she smiled back and, sitting next to me, hugged me from behind, nuzzling my back and poking her cold nose into my neck area."
    "For ten minutes we hypnotized the jar where the aluminum TEH was forming bubbles."
    $renpy.notify('«Chifir» - is an exceptionally strong tea. «Hat» - in this context means «fake» or «bad».')
    "Another five minutes later, scalding, we handed each other the jar of peace, taking a bite of real tea, strong to the point of chifir, not unlike the hat that inhabits the shelves of stores that are modern to me."
    un "You brew hard, our man."
    "Lena nodded approvingly, tasting the hot beverage properly."
    un "I spit up all the time after the disgust they give me in the canteen."
    "We didn't take a lot of tea, but it was strong, even to the point of tartness - so we were crushing that poor liter of tea for quite a long time."
    un "We drank the tea, we warmed up, what's next?"
    me "First it would be nice to decide not what, but where that «next» is going to be."
    "I ran my hands around the rain-soaked windows."
    me "Right now, the rain is hiding us better than any invisible hat."
    me "But according to Crowe's quote, it can't rain forever."
    me "So I suggest we relocate to the back room."
    me "If I'm not confused: there are some particularly vicious nettles growing under the windows, so they can't spy on us."
    un "Mmmm... then what?"
    "Lena was standing next to me, shamelessly warming her palms on my stomach."
    th "I've heard that question somewhere before."
    me "And then it's up to the circumstances."
    if persistent.hentai_graphics_7dl:
        show un serious sleep with dspr
    else:
        show un serious pioneer with dspr
    un "All right... You're the man - you drive..."
    "She shrugged and released me."
    me "So, for starters, where was the mattress?"
    "I inquired, dodging a wet skirt hanging from the rope."
    un "In the back room, in some kind of closet..."
    "Lena smiled fleetingly at my equilibrium tricks and remarked in between:"
    un "I guess I'll have to put my clothes in there, too. They'll notice."
    me "Good girl."
    "I praised."
    me "You do that. I'll get us where to lie."
    play sound sfx_open_door_clubs_2
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    scene bg int_clubs_male2_night with dissolve
    "The mattress was found on one of the top shelves, occupying the entire space."
    th "Yeah... {w}I don't even want to think about where that mattress was or what he saw."
    "Wasn't too lazy to unpack two sheets at once to cover the pile of stains from reagents and bodily fluids."
    "Had to do the same with the pillow."
    "And when Lena stretched the rope across the room and hung our things there, I was already waiting for her and patted the place next to me invitingly."
    if persistent.hentai_graphics_7dl:
        show un smile3 sleep with dspr
    else:
        show un smile3 pioneer with dspr
    me "Crawl under my wing, it's warm and dry!"
    "Instead of answering, the girl laughed and, throwing off her sheet, slipped under my side."
    hide un with moveoutbottom
    "She fidgeted a little, getting comfortable, sighing."
    "Finally she turned to face me, and again she put her slender leg around my thigh, being suddenly so close - in every sense of the word - that I could feel that she was far from frozen!"
    un "You know... I'd do it right here and..."
    "She yawned."
    un "But you're right. I'm very sleepy."
    "I didn't argue, and just seconds after she rested her head peacefully on my chest and snoozed, I covered my eyes myself, lulled by the constant sound of rain outside the window."
    "And even the cries of the libido that all I had to do was move just a little towards her to take our relationship to the next level..."
    with fade2
    scene bg int_intro_liaz_7dl with fade
    play music music_list["sparkles"] fadein 3
    "I dreamt I was awake."
    "With an effort, I ripped off the hat stuck to the glass and looked around."
    "Everything was still the same here."
    play sound_loop sfx_bus_interior_moving fadein 4
    voice "Overslept, huh?"
    voice "I'm sorry, tried to woke you up, tried, and all you did was mooing."
    me "What?"
    "I looked out the window - the bus was coming up to my relative «Lomo», it had a loop here."
    "How convenient to get on at one terminus - and arrive at another terminus. You never oversleep."
    "You always wake up surrounded by familiar, familiar, but never favorite buildings."
    "Especially after something like this..."
    th "Discrete movement between two points, invented by me and embodied in my personal pocket reality - what the devil are you so boring and predictable?"
    "There are dreams that make you wake up in tears."
    "There are dreams that make your heart skip a beat for months."
    "And then there are dreams... After which you don't wake up. Someone else opens your eyes, someone who isn't you anymore."
    "An ultra-caine shot that freezes everything so much that even a thirty-degree frost feels like something insignificant."
    "I don't know what I've done to deserve this beautiful dream... And what I've done to deserve the end of it."
    "But...every story has an ending, doesn't it?"
    "I guess this one does, too."
    "I got up and headed for the back door."
    with vpunch
    un "Semyon!"
    "A very familiar voice called from somewhere behind me."
    "I turned around - but I didn't see anyone."
    with vpunch
    un "Semyon! Wake up!"
    me "What... What?"
    with hpunch
    stop music fadeout 5
    stop ambience fadeout 5
    stop sound_loop
    scene bg int_clubs_male2_night
    if persistent.hentai_graphics_7dl:
        show un angry2 sleep close
    else:
        show un angry2 pioneer close
    show unblink
    "Lena was lying next to me, shaking me without too much tenderness. And when I opened my mouth to ask something, she immediately shut me up with her palm."
    play music music_list["you_lost_me"] fadein 3
    un "Qui-et! I think they're looking for us."
    "I wanted to ask something, but I heard voices on the other side of the door..."
    if persistent.hentai_graphics_7dl:
        show un serious sleep at right with moveinright
    else:
        show un serious pioneer at right with moveinright
    "Lena quickly hopped to the door and silently turned the key in the lock, flashing her nakedness."
    "And, moving deliberately leisurely, she came back to me."
    if persistent.hentai_graphics_7dl:
        show un smile2 sleep at center with moveinleft
    else:
        show un smile2 pioneer at center with moveinleft
    un "Now we can also..."
    me "You god damn pervert."
    "I hissed."
    me "It feels like all you want is for someone to catch you in the middle of the process!"
    if persistent.hentai_graphics_7dl:
        show un grin sleep with dspr
    else:
        show un grin pioneer with dspr
    un "Oh... For some reason this turns me on."
    "She pushed me hard in the shoulder, turning me on my back, and after a little thought, sat on top of me, pinning me to the mattress."
    un "Oh you..."
    if persistent.hentai_graphics_7dl:
        show un smile3 sleep with dspr
    else:
        show un smile3 pioneer with dspr
    play sound sfx_steps_clubs_nextroom
    with dspr
    if persistent.hentai_graphics_7dl:
        show un scared sleep with dspr
    else:
        show un scared pioneer with dspr
    play sound sfx_close_door_clubs_nextroom
    "Someone jerked at the door, tried to turn the knob."
    voice "It's locked - they don't seem to be here."
    mt "So open it!"
    voice "It won't work. Only Shurik had the key, and he took it away."
    th "And then Olga Dmitrievna walks in and, without saying a bad word, takes a blunt knife and saws off my testicles."
    "That allowed me to muffle the urges of my flesh a little bit."
    me "I'm sorry, but right now I'm just scared."
    "I whispered, smoothly pulling her off me."
    if persistent.hentai_graphics_7dl:
        show un sad sleep with moveinbottom
    else:
        show un sad pioneer with moveinbottom
    "After threatening me with her fist, she finally stopped mocking me."
    un "It'd be my way anyway! {w}You can't fight back forever."
    me "As if I mind!"
    me "Just let it not be such idiotic circumstances?"
    th "It's nobody's fault I'm such a loser that I'm stupidly unlucky for convenient situations."
    dreamgirl "Well, maybe you should think about preparing the situation with your own hands."
    th "What?"
    dreamgirl "You have the key to the cabin. And you know what - or rather, who - to distract the counselor with. So tonight or tomorrow..."
    me "The farewell disco is tomorrow, right?"
    "After the girl nodded, something inside me sweetly whimpered in anticipation."
    "The observance of tradition, the farewell disco, farewell kisses, confessions and... yes, that's the one."
    "It took my breath away, my heart jumped and pounded like stunned."
    un "You act like you don't like me."
    me "Nonsense. I just don't enjoy making love to the accompaniment of stomping and negotiating."
    un "So they're all gone now."
    "I listened."
    me "They'll be back anyway. And the mood is... Not the same."
    "Lena's belly song confirmed what I was saying."
    me "And what's time..."
    "Thank goodness, I was smart enough to keep smart in its case, it didn't get damp and showed «18 hours»."
    me "Missed the lunch, but at least the clothes are dry."
    me "Let's rob cybernetics a bit more and go surrender to Olga."
    un "She'll 100 percent want payback for us running away."
    me "I don't care. She won't deprive us of dinner."
    un "Might forbid us to go to the bonfire."
    me "Let her try."
    "After listening to the silence outside the door for a few minutes, I nodded to the girl who was already dressed and turned the key."
    play sound sfx_open_door_clubs
    with fade
    $ persistent.sprite_time = "sunset"
    $ day_time()
    scene bg int_clubs_male_day with dissolve
    play music music_list["sweet_darkness"] fadein 3
    "The jar, which Lena economically threw out the window, was waiting in its place. There also lay the other components of the tea ceremony."
    show un smile pioneer with dspr
    un "Go and do something, or you'll make more chifir again."
    th "Wow, how thoughtful."
    th "Housekeeping... I have to decide what to do so that I don't interfere with the girl's care."
    return

label alt_day4_un_7dl_cinema:
    play sound sfx_open_door_clubs_2
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    scene bg int_clubs_male2_night with dissolve
    "In the absence of other activities, I headed back to the back room, where I straightened out our makeshift bed - almost becoming one in the most literal sense."
    "I rolled up the sheets and put them in a bale of dirty laundry, the roll found its place on the top shelf to the left... And then my attention was drawn to the impossible here, but so familiar, silhouette."
    "A SONY video double and a vertical shelf under twenty VHS tapes."
    th "Come on!"
    "Fingers slid over the ribbed, gripped paper stickers, signed anyhow, in the bouncing careless handwriting of a man rewriting a tape."
    "Here it was as if I had inhaled the icy air of my own eighty-ninth..."
    "The purple ball is Alisa Seleznyova, the mass hysteria over Natasha Guseva. Though, of course, that's just echoes of «Guest from the Future» already."
    "Of course, I remember that the real Alisa became big, grown up and very beautiful - and chose the stage over biology; but who knows, maybe it's not the past, but some parallel world?"
    "Zemeckis's Netflix, surprisingly appropriate here - really, no one offered me «DeLorean.» And Mikey Fox isn't shaking with Parkinson's yet."
    "The only whole paper box with Sigourney Weaver looking at the xenomorph with hatred. The beginning of a series and an entire universe."
    "«You Painted Bitch» - and pigeons. And a story about appreciating what's around."
    "Nikulin's work from the sixties."
    "There are also, apparently guided by a similar associative row to mine, several cassettes of Andryusha Mironov's writings."
    "And that's just what I could make out - in some places the inscriptions were faded to the point of illegibility, in some places there were no signatures at all."
    "Behind the TV itself, where I went to plug in the bells, I found a bottle of already dried cabernet and a plastic license case of «The Professional»..."
    "Funny how at one time this tape was the first one I ever bought. {w}And not the least of which was the gorgeous soundtrack by Ennio Morricone."
    un "Semyon, whatever you're doing, finish it. Let's go have tea."
    "Lena called."
    "This whole camp feels like it's lavishly laced with memory tags - I haven't experienced this many flashbacks since my last visit to my old camp, where I almost broke my neck trying to shake up the old days."
    "Simply put, I tried to run where I'd been running all my life. But I didn't take into account the fact that I got both bigger and heavier."
    "That's where the memory held me, so much so that I was far from being able to shed the shroud of memory from my eyes."
    "The warmth, the summer, the carefreeness of childhood and there's still a huge life ahead and all avenues are open."
    "And people don't hate each other yet. That's what it seemed to me at the time."
    "Of all the memories, perhaps the last was the one I longed for the most."
    "After lighting the tech to warm up, I shook my head and walked out into the main room."
    $ persistent.sprite_time = "sunset"
    $ day_time()
    scene bg int_clubs_male_day with fade2
    show un normal pioneer with dspr
    un "What did you find there?"
    me "Memory."
    "Short answer."
    un "What?"
    me "The video library is there. Movies. Do you want to watch something?"
    show un smile2 pioneer with dspr
    un "Of course!"
    "Lena winked."
    un "But what do we say to the counselor?"
    me "You ask strange questions... We'll say «hello» of course."
    show un laugh pioneer with dspr
    un "As you command. {w}What shall we watch?"
    me "I'm torn between Belmondo and Guseva."
    un "Is there a «Guest»?"
    me "No, «Ball»."
    un "A sequel?"
    me "You could say that."
    th "Can I not educate her about sequels, prequels, and sidequels?"
    dreamgirl "No, why? Let's give a lecture for half an hour now."
    th "Shush."
    "After wrapping a steamy, fragrant jar, I sneaked it back into the back room with me, leaving the rattan basket of cookies - I didn't know where it came from - on Lena's conscience."
    play sound sfx_open_door_clubs
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    scene bg int_clubs_male2_night with dissolve
    "The previous video technician turned out to be a rare wreck and left the rewinding of the tape to the conscience of the coming viewers."
    "Two triangles looking to the left. How simple everything is in the world of flash and digital music!"
    "At any rate, you don't have to wait ten or fifteen minutes for the tape to rewind."
    show un normal pioneer with dspr
    me "We wait ten minutes and then we can admire the naive retro-futuristic pictures of the future and Alisa Seleznyova."
    if alt_day4_me_neu_transit == '':
        un "The future... Speaking of the future. {w}You're from there. Will you tell me something?"
        me "I'm not quite sure I have the right to tell you anything. {w}But... what the hell!"
        me "Ask me what you're most interested in?"
        show un grin pioneer with dspr
        un "This is the future! I'm interested in absolutely everything!"
        me "Hmm... Why don't you narrow it down a bit? Give me the topical stuff!"
        show un smile pioneer with dspr
        un "Start with the differences! How is our time different from yours?"
        "After I was silent and gathering my thoughts, I sat down on a chair and motioned Lena to the one next to me."
        me "The main difference is in people. We are no longer friends, comrades, or brothers to each other."
        me "There, like in the 'balloon."
        "I nodded toward the buzzing tape recorder."
        me "It feels like the aliens from the Black Wanderer succeeded after all - and cracked the damn ball somewhere in the vast expanse of my homeland."
        me "It wasn't just that, out of nowhere, this frighteningly detached hostility, not even hatred, but indifference, had come from nowhere."
        me "Something inside me cringes when I see someone cut, when someone falls, when a heavy girl on a long-ago term gets on the bus, or when someone can't keep their balance on ice."
        me "I guess I'm just a moral freak."
        me "Relative to the measures of my world."
        me "Okay... That's all lyrics. Let's get to the other differences."
        show un serious pioneer with dspr
        un "Come on."
        me "The culture-including consumption-is totally copied from abroad, right down to the outlying malls."
        me "Malls are a kind of department store. Only they occupy huge buildings and are located away from the city, with their own structure ... And culture."
        me "And our culture is just a name."
        me "There's even an expression: pops. As an indicator of low-quality music."
        me "In general, in this respect, the West has also surpassed us."
        me "We either listen to «umts-umts» produced by foreign DJs, or we go to concerts of foreign stars."
        show un normal pioneer with dspr
        un "More..."
        me "We've forgotten how to work with our hands, and we've completely switched to the American way of life."
        me "Our new creed is consume, work, die."
        me "The paperworkers earn more than the slaughterhouse worker; the poorer one is to blame; one-third of the population are lawyers, one-third are economists, one-third are degenerates."
        me "More? Well. There are speed bumps everywhere, the streets are occupied by foreign cars, and the VHF band is full of commercial radio stations. There are so many channels on the TV, you can flick until you turn green."
        me "My toys - yes, the technological advances are great. But this is China, and the life of these toys a couple of years, so then bought a new one - spent..."
        me "And, of course, the Internet."
        un "Yes, you said something like that..."
        me "The Internet is hard to describe. It's life and stagnation all in one. The quintessence of knowledge, the materialized noosphere, if you will."
        me "It has everything to satisfy the thirst for knowledge and entertainment, from encyclopedias to YouTube. Although, as expected, well over two-thirds of the actual traffic is pornography."
        me "As for me, for me, the Internet is my loneliness. Empty, stupid, anonymous eyes staring out of the darkness of nothingness."
        me "A stinking cloaca from which you can only escape when your natural needs become unbearable."
        me "And, often, the only salvation for non-humans like me."
        me "Poetics aside, the Internet is a digital reflection of life. With minimal differences."
    "The tape recorder clicked, stopping and playing automatically."
    scene cg d5_un_film_7dl with dissolve
    play music music_7dl["liliac_ball"] fadein 5
    "The Mosfilm logo popped up on the screen and the familiar music from my childhood began to play."
    "This film was nowhere near as popular as the original, but personally I always liked it better than the original luscious pentalogy."
    "Simply because it was filmed with such charm, style and a sense of beauty that it was willy-nilly memorable - unlike Bekmambetov's and Bondarchuk's slag."
    "It was both funny and touching to see the retro-futuristic vision of what the possible technologies of a model future a hundred years away would be."
    "Already we had technology that surpassed anything depicted in the movie - and that's not to mention a much more advanced design."
    "But no one cared about that. Mankind turned its back on space, concentrated on the digital universe, shutting itself in."
    "An astronaut is no longer a dream, but an exotic, because an astronaut has no right to be selfish."
    "Although maybe that's not such a bad thing."
    "After all, without any medical training, I can take care of most of my own ailments just fine."
    "And the flashed memory of a familiar face growing feverishly flushed with red spots of anaphylactic shock after some pill..."
    "What would happen if I turned out to be an average member of the Soviet man?"
    "Would I have known where prednisolone was and when I could use it, how to clean the stomach and blood of someone dear to me?"
    "Yep. I'd dial 1-1-2, and wait meekly, praying to all the known deities."
    "It's like we've matured a little technologically, but we're late in developing culturally and morally, and instead of growing up chased the big buck."
    "I cast a glance at Lena, enthusiastically watching the movie: lip biting, eyes glistening, and complete focus on what was happening on the screen."
    "As a result, we've become technologically equipped barbarians, in some ways even inferior to girls like these."
    "Honor and conscience are still not ridiculous atavisms, and cynicism is not considered a virtue."
    voice "Do you know what ended up in the purple balloon? The Enmity virus."
    voice "If it gets into a man's lungs, he loses his mind."
    dreamgirl "Eighty-nine - Lithuania withdraws from the Komsomol, deciding to form its own communist union."
    dreamgirl "The giant let's out his first sneeze - and that's the beginning of the fall."
    voice "He hates absolutely everything."
    voice "Can you imagine? {w}People don't suspect anything. {w}Living, working."
    dreamgirl "The country - then still a country - announces an economic crisis, but nobody cares: they have perestroika, glasnost, freedom."
    dreamgirl "Freedom of empty counters and hungry children."
    voice "And suddenly they hate each other."
    dreamgirl "In Romania, Nicolae Ceauşescu is shot, the entire Caucasus is gripped by convulsions of «liberation» wars, in Kazakhstan, Zheltoksan is developing."
    dreamgirl "The country is beginning to die out - the death rate is almost twice as high as the birth rate."
    "I couldn't stand it and turned away from the screen."
    "Too eerily Alisa's words echoed with what was around me - there - left over the objective edge."
    "And as much as I wished I hadn't gone back there - as much as I wished I had stayed..."
    "The relentless voice of the beautiful girl from the era of the established Communist future got to me even in my silly clasped eyes and plugged ears. After all, I've seen this movie a thousand times."
    "I know those words by heart."
    voice "He hates absolutely everything."
    dreamgirl "The GKChP, Yeltsin's speeches from the tank, the approved position of president..."
    voice "He wants to kill."
    dreamgirl "September-October of '93. After two years of agony of Svyatogor being torn apart by metastases."
    dreamgirl "Tanks disperse the supreme council. More than a hundred and fifty people have been killed, far more than three hundred wounded - and this in the heart of Russia, and no one has yet heard of terrorist attacks."
    voice "There is a war going on. To the last man."
    th "We're all mad. There's a war going on."
    dreamgirl "And someday we will all be «liberated» with cheerful salutes of 5.56x45. The only thing stopping the «liberators» is that we'll have to be fed."
    dreamgirl "So they're just waiting for a generation to change."
    dreamgirl "2020. By then we'll either be extinct.{w} Or we'll turn into sterile mules."
    dreamgirl "And people like you, Semyon, are evidence that the States have won. Because there will be nothing left after you."
    dreamgirl "You are not a losing branch, you are a cauterized tip of a hair, dead, growing no further."
    dreamgirl "You are the end of the story of the House of Persunov - the one that, by some unknown miracle, existed before you appeared to the world."
    dreamgirl "A standing ovation to American political scientists for creating you and your kind of hickens."
    "I imagined a huge, rambling genealogical tree."
    "One child of two parents is the extinction of a nation, two children is keeping in the balance, three or more is prosperity and development."
    "Not without reason in all Russian families were considered small if they had less than three children, even the arithmetic was such - one child, two children, three children... {w}But four children."
    stop music fadeout 5
    stop sound
    stop sound_loop
    play ambience ambience_clubs_inside_day fadein 3
    "Thoughts jumped to «Guest»."
    "I wonder... What would Alisa have promised me?"
    "I remember that from what she promised her classmates, some of the real actors even came true."
    th "And you, Semyon, are going to be a /b/tard. You'll sit your pants by the monitor and live on two hundred dollars a month with no discomfort."
    th "You'll have a sweet, bright childhood, a funny and interesting adolescence. And it will all end in a vigil in front of a screen - day after day returning to the emotional vampire that all anonymous resources represent."
    scene bg int_clubs_male2_night with dissolve
    "The movie's over."
    me "Well... It was a very good movie."
    "I rose from my seat."
    me "But it's time to be honored. And I'd like to have dinner."
    "It was approaching eight o'clock, so Lena nodded accordingly and stood up next to me with ease."
    show un smile pioneer with dspr
    un "I can't say it happened the way I wanted it to... But it was interesting that way, too."
    me "Let's go eat, or we'll be hungry as well as interesting."
    "I didn't notice myself eating all the cybernetic cookies in between."
    stop ambience fadeout 3
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    play sound sfx_open_door_clubs_2
    scene bg ext_clubs_day with dissolve
    "We barely had time to go outside and latch the padlock."
    mt "SEMYOYOON!"
    play music music_list["awakening_power"] fadein 2
    show mt angry pioneer with dissolve
    me "Shit... Why is it always Semyon? I've been called responsible!"
    mt "Do you want to explain where you two have been hanging around all day today?"
    "The counselor started."
    me "We were out walking."
    "I was playing dumb."
    me "Since you told us not to do anything stupid, we decided to go all over camp. Here, now we were looking at the clubs."
    mt "Why are you making a fool of me?"
    mt "Where have you been, I ask you?"
    me "Don't you like the walk? {w}Okay, then we spent the whole day in bed. At your place, by the way! {w} We did so much that it's easier to say what we didn't do!"
    me "Why are you so inattentive to your beds when you're running around the camp?"
    dreamgirl "Strong, man! I don't think you'd get her any harder, even if you offered her to join as third."
    mt "Well, what do we have here, a damn comedian? Private joker, I admire your honesty."
    mt "Let's see how long you'll joke without dinner!"
    me "Yes, until the warden's office."
    "Serenely I shrugged my shoulders."
    me "There, where I'll tell him in detail how many moles you have and what hairstyle in the right places."
    mt "You... You... I'll send a letter today!"
    me "I don't give a damn. {w}Send it. {w}Let's see which comes first - mine to the Party Committee or yours to the Komsomol."
    me "Shall we play who'll knock who over?"
    show un angry pioneer at left with dissolve
    un "STOP IT!" with hpunch
    "Lena surprised us both by barking in a way I had never heard... Wait."
    "In the library, on the third day, when we were «sent off» to the quarry."
    show un angry2 pioneer with dspr
    un "What are you? Children? Semyon, give way. Apologize."
    un "Olga Dmitrievna, don't punish with food - it's not pedagogical."
    un "Do I really have to do all this for you?"
    "I only smiled broadly - I'd let Lena scold me all she wanted."
    "But the counselor seems to have had it coming."
    stop music fadeout 5
    show mt normal pioneer with dspr
    mt "Okay."
    "She muttered."
    mt "Go to supper. But don't forget, there's a bonfire after dinner. If you miss it too..."
    hide mt with dissolve
    "She left the end of the sentence in the air and walked away."
    play sound sfx_7dl["eat_horn"] fadein 1
    show un smile pioneer at center with moveinleft
    un "Well, here's dinner."
    "Lena smiled, grabbed my hand and dragged me toward the canteen."
    stop music fadeout 3
    stop sound fadeout 4
    stop ambience fadeout 6
    with fade2
    return

label alt_day5_un_7dl_cleaning:
    if loki:
        scene bg ext_clubs_rain_7dl with joff_r
        play music music_list["my_daily_life"] fadein 5
        "There were no keys and nowhere to hide - I had to get out."
        show mt normal pioneer with dspr
        mt "There you are."
        "The counselor caught up with us."
        mt "Well, that's it. I'm not going to scold or punish you for disobedience - you're not little kids, it's too late to whip."
        mt "But you'll do the camp some good anyway."
        mt "The rain is ending - you will go to the square, and run a clean sweep to make sure there are no wrappers or paper wrappers lying around. Is that clear?"
        un "Understood."
        "Lena hurriedly ended the comedy of disobedience."
        "That's right, you can't run around much longer."
        "Apparently, seeing on my face the sheepish desire to fight a little more, Lena jumped and, grabbing me under the elbow, dragged me away to the square."
        stop music fadeout 3
        pause(1)
    scene bg ext_warehouse_day_7dl with dissolve
    play music music_list["take_me_beautifully"] fadein 5
    "We reached the warehouse without incident and almost without getting soaked - confirming her status as an old-timer, Lena led us along such paths that the whole way came under the cover of branches."
    "The rain, indeed, was slowly but surely coming down."
    "After knocking briefly and waiting for an indecipherable cry from inside, I pushed the door open and, letting the lady go ahead, squeezed inside myself."
    scene bg int_warehouse_day_7dl
    show sl smile sport
    with dissolve
    sl "Hi, Semyon! {w}Hi, Lena!"
    "Our eternally optimistic activist smiled at us."
    sl "Are you here on business or just visiting?"
    th "Oh, of course we're visiting! To the linen warehouse."
    dreamgirl "Don't piss off, the girl's lonely here, and the rain makes it impossible to run around camp with her tail up."
    th "She doesn't have a tail."
    dreamgirl "Neither do you. But that doesn't stop you from acting like an animal."
    th "I don't understand something. That was an insult just now, wasn't it?"
    dreamgirl "Not in the least."
    "The inner voice chuckled nastily and fell silent."
    me "Looks like I've been made eternal plaza duty."
    "Can you guess why I came this time, too?"
    "Slavya laughed and, without saying a word, disappeared into the bowels of the warehouse."
    "She rattled off something in the background and returned five minutes later, handing us the necessary inventory."
    sl "There's a cart under the awning - take it, but don't forget to bring it back later."
    me "Yeah, got it, boss."
    "I put my hand to my empty head and retreated."
    stop sound
    stop sound_loop
    stop music
    scene bg ext_square_day with dissolve
    play music music_list["i_want_to_play"] fadein 5
    show un smile pioneer with dspr
    un "After all, our counselor is awfully smart."
    "Lena said thoughtfully, nodding as she let the cart stop and took the rake from there."
    me "What are you talking about?"
    un "Well... She did everything as she promised: she didn't separate us, and she didn't let us do anything stupid."
    th "On the whole, of course, it's true: you can't do much nonsense in the square - but not by virtue of shyness, of course. {w}It's because they're going to bore us with their advices."
    me "Two meters to the left to the elderberry bushes."
    show un grin pioneer with dspr
    un "And an icy rain behind your scruff to cool you down a bit."
    me "You're a killjoy. Evil man."
    show un normal pioneer with dspr
    un "I understood about the evil man, but what did the first word mean? I study German at school..."
    me "A person who likes to spoil the pleasure of others."
    me "Particularly, breaking plans."
    un "Don't be offended. Think of me as the voice of reason, okay?"
    show un smile pioneer far with dspr
    un "Dear old man, do god's mercy, take me home from here, to the country, there is no way I can... I bow at your feet and will pray to god forever, take me away from here, or I'll die..."
    me "You missed the part about the herring poking in the face..."
    "I snorted."
    show un smile3 pioneer far with dspr
    un "Well, it's not like anyone is poking me."
    me "Yeah. But with this kind of order, they'll start soon. They won't hesitate to comb your hair with a spandrel."
    show un grin pioneer far with dspr
    un "You grumble like an old grump! {w}Is it so hard to sweep the square?"
    me "It disgusts my laziness! Instead of getting on the couch with an interesting book and giving you a good time, I'm waving my rake here!"
    un "So it's in your best interest to finish things quickly - I promise I'll join you in bringing the program to fruition."
    dreamgirl "Aha-ha-ha, snuggle warmly under a warm plaid."
    "Snorted the inner voice."
    dreamgirl "Unfortunately, your plaid is left at home, what are you going to bunny up under? {w}With a sheet?"
    th "Even so. I guess she and I both subscribe to the clichéd notion that there's no place like heaven with a sweetheart."
    dreamgirl "Home, most importantly, do not invite her right away. At least until you throw out the bottles and mop the floor. Otherwise, you'll soon have a new life form in your «hovel», made of beer and dust. {b}B{w=0.1}e{w=0.1}e{w=0.1}r{w=0.1} g{w=0.1}o{w=0.1}l{w=0.1}e{w=0.1}m.{/b}"
    th "As if I had any chance of meeting her {i}there{/i}."
    "I frowned."
    th "As if {i}there{/i} would be any chance of her even paying attention to me..."
    dreamgirl "Well... She did here."
    th "Don't waste your breath."
    "Putting the garbage in another pile - analogous to the ones that piled up in abundance every ten meters - I picked up the cart and drove it to Lena's side: the girl was finishing cleaning up."
    me "Let's get this nightmare over with already."
    show un smile pioneer with dspr
    un "I don't really mind."
    "The girl smiled, squinting into the sun."
    un "As long as you're supervised. Otherwise someone else will pick you up."
    un "Oi!" with hpunch
    "She swung the broom unluckily, and I got splattered with mud."
    me "Hey, look out!"
    "I belatedly bounced back and looked over my shirt with my hands up helplessly."
    "I suspect the picture looked even sadder on my face."
    me "You're so good!"
    "I remarked wryly."
    me "Kitty-dogs usually mark their territory, and you've marked me so well that now even the most undemanding person won't sniff me out."
    show un shy pioneer with dspr
    un "Oh, forgive me please!"
    "Throwing her inventory on the ground, Lena walked over to me and, taking a handkerchief out of her pocket, tried to wipe my face a little."
    me "Don't waste your time. I'd better go to the sinks when we're done."
    play sound sfx_7dl["eat_horn"] fadein 1
    un "Will you make it?"
    "Asked a timely question Lena."
    me "No."
    "Disconcertingly honestly, I answered."
    "And after tossing all the brooms and rakes on top of the garbage, I took a low start to the warehouse - Slavya is bound to run in the front row to feed, so it would be advisable to intercept her before she could get very far."
    "Lena shouted something in her wake, something about the devils being smelly, but I wasn't paying attention."
    hide un with dissolve
    scene bg ext_square_day:
        pos (0,0)
        linear 0.1 pos (-5,-5)
        linear 0.1 pos (5,5)
        pos (0,0)
        linear 0.1 pos (0,-5)
        linear 0.1 pos (0,5)
        repeat (12)
    with dissolve
    "The cart rattled at the joints between the slabs, but it behaved quietly."
    scene bg ext_warehouse_day_7dl:
        pos (0,0)
        linear 0.1 pos (-5,-5)
        linear 0.1 pos (5,5)
        pos (0,0)
        linear 0.1 pos (0,-5)
        linear 0.1 pos (0,5)
        repeat (12)
    with dissolve
    "So I got to the warehouses in a matter of minutes - just when I realized that I've forgotten to ask what to do with all the garbage I've collected."
    "Well, Slavya's a smart girl, she'll think of something."
    stop music fadeout 6
    stop sound fadeout 3
    scene bg ext_warehouse_day_7dl
    show sl surprise pioneer with dspr
    play music music_list["glimmering_coals"] fadein 5
    "And when I saw her, I did what the logical thing to do was to cry out and run towards her."
    me "Ehehehe, Slavya! Wait!"
    show sl scared pioneer with dspr
    "But even though I was running fast, I could make out the expression of superstitious terror on the girl's face."
    "I guess if we weren't in the Soviet Union, I'd get a insigned with the cross or a stick between my ears."
    "I could almost see the puffy scarlet lips whispering «Holy, holy...» but it all happened in such a short period of time that I just didn't have time to react."
    "And with a rumbling cart, a humming stomp, and a noisy snort, stopped beside her, almost getting dirt on her perfectly white socks."
    me "Phew... Damn..."
    "I exhaled, looking up at her."
    show sl smile pioneer with dspr
    sl "Semyon, is that you?!"
    me "Who else would it be?"
    sl "Wow."
    show sl laugh pioneer with dspr
    sl "You should see yourself! Scruffy as the devil himself."
    me "Thank you, for a compliment. {w}I'm dabbling."
    show sl smile2 pioneer with dspr
    sl "Don't pout: I like you just the way you are."
    dreamgirl "Okay, this is where I'm torn in half. And I want details."
    dreamgirl "And it is highly desirable that the last phrase did not reach Lena's ears. From the word «at all», you know?"
    th "I'm not dumber than a locomotive."
    me "It's wonderful that you like. I'm only afraid Olga Dmitrievna won't appreciate your aesthetic endeavors."
    me "You're the castellan... Well, or VRIO... Maybe there's a way to change into something?"
    sl "Of course there is."
    "She searched her pockets for the key and unlocked the warehouse."
    show sl normal pioneer with dspr
    sl "You can shake out the cart for now. The bags are hanging on the nail where you took it."
    me "Uh... Okay."
    hide sl with dissolve
    "I dutifully wheeled the cart to the parking lot and, picking up a duffel bag from the nail, began shifting papers into it."
    "Not a particularly inspiring job, especially in view of the fact that there is, in fact, lunch!"
    "And Lena!"
    "But there was nothing to do: they wouldn't even let me on the doorstep of the canteen dressed like that."
    "Five minutes later, the activist also looked out from behind the warehouse door."
    sl "Finished? Good. {w}I left a kit on the table - you can change right there."
    me "Whatever you say, boss. What do I do with the dirty stuff?"
    "Slavya grimaced."
    sl "What are your words... Never mind. You throw the stuff in the basket labeled «Laundry» - I'll send it to the laundry tonight. Can you handle it?"
    th "Sure, Mom. I may be retarded, but I can do some things!"
    dreamgirl "Don't be a fool. She's about to peep, by the way - and she's not the least bit embarrassed about it."
    "The look the girl was giving me confirmed the speculation completely."
    th "I don't care. {w}It's a small price to pay for a salvation."
    "I pretended not to notice anything and squeezed past Slavya into the room."
    stop music fadeout 3
    play ambience ambience_camp_center_day fadein 5
    scene bg int_warehouse_day_7dl with dissolve
    if alt_day_binder != 1:
        "Nothing has changed here since my last visit."
    "A shelf of uniforms, linens, and bedding, a sling on the right side, and a boxed-in cubbyhole that appears to be a shelter for the castellan."
    th "I wonder what she's hiding in there?"
    dreamgirl "Nope, not interested. Go ahead and change your clothes."
    th "Why not? What if there's..."
    dreamgirl "...something you can't talk about out loud? A secret that will bind you in silence? {w}I assure you, my dear, you {b}don't{/b} want to make any extra connections right now."
    th "But that's not what it means!"
    dreamgirl "Just shut up and change. Don't forget, you've got a show to do."
    th "Go take a shower, nerd."
    dreamgirl "Speaking of baths - it would be nice to rinse yourself off. Find out where the showers are, or if I were Lena, I wouldn't let a dirtling guy like that near my body."
    th "What's wrong?"
    play sound sfx_7dl["blanket"] fadein 0
    "I crumpled up my shirt and launched a three-pointer into the basket at the front door."
    th "I'm going to change my clothes and wash my face and..."
    dreamgirl "...and stay sweaty and smelly and three days without washing?"
    dreamgirl "Okay, you'll wash the dirt out of your hair, but what do you want to do about the natural processes of pollution? {w} Lenochka, of course, is a patient girl, but don't you want to please her yourself?"
    th "I do."
    dreamgirl "Well, find out."
    "With my usual slightly audible click somewhere in the back of the interstitial ganglion, I was left alone."
    "The new unshrunk uniform - anyone who served knows that until the forty-fifth universal fits, you walk around in it like a tin case."
    "The shirt stabbed my neck, it was too tight on my shoulders, and the shorts didn't want to button up at first - the buttonholes were screwed on at a diameter that was way too small. {w}I'm not even going to describe the epic search for the heel of my socks."
    "I'll just say that instead of the expected two minutes I messed around for ten, and during that time I showed Slavya - if, of course, she hadn't lost interest in looking at my puny bodies - anything I could."
    "But, praise be to Random, and this arduous quest was completed - I tied my tie in a bow and walked out of the warehouse, nodding to Slavya on the way."
    scene bg ext_warehouse_day_7dl with dissolve
    show sl normal pioneer with dspr
    me "That's it, I'm ready - we can go eat."
    show sl smile pioneer with dspr
    sl "I see you weren't in much of a hurry!"
    "Laughed the girl."
    me "Come on, they're sewing those uniforms on some robots - it's uncomfortable!"
    show sl serious pioneer with dspr
    sl "Don't swear! The Party has given you everything you need! To adjust to yourself - that's your job!"
    me "Yes, yes... Fulfillment is duty, over-fulfillment is honor. We've heard that before. Are you going to lunch or do you want some more theological arguments?"
    sl "Theological? No. Will you wait for me? Let's go together."
    me "Okay."
    "I shrugged. {w} On the first day, Slavyana had demonstrated that under her command I was in no danger of going hungry, so finding myself in a similar situation, I, of course, hurried to hide behind her again."
    th "Work, activist!"
    "Quickly locking the warehouse, she hid the key in her pocket and gave a wave."
    sl "Let's go!"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day5_un_7dl_breakfast_h:
    scene bg int_dining_hall_people_rain_7dl with dissolve
    "I headed for the exit of the canteen without even looking to see if she was following me."
    "It's a local habit, what can you do?"
    "Stopping at a partition where no one could hear us, I waited patiently for the approaching counselor and began:"
    show mt normal pioneer with dspr
    me "Olga Dmitriyevna, of course I respect you a lot and everything."
    me "But don't get me wrong: in this state, Lena and I are capable of sending both your Komsomol and you to hell."
    show mt angry pioneer with dspr
    me "No, no offense."
    "I raised my palms in front of me, keeping her out of the monologue."
    me "Now I can only speak for myself - but personally, this girl is more important to me than all the Komsomol in the world. I even agree to an unflattering characterization to the local party committee."
    me "I don't want to part with her, I'm not going to part with her! {w} Not under any of the sauces you've come up with here."
    me "Again, I speak for myself and only for myself - but I only do what I think is right. And right now I need her. Do you want us to run away from the camp?"
    me "Or are you enthralled by the idea of having two offended pioneers in your squad? Notice, the offended by you, personally."
    hide mt with dissolve
    "I lowered my head and exhaled, resting my feet firmly on the floor, preparing to endure the supernova of our choleric counselor's wrath."
    "But the sound I heard made me blink in surprise."
    show mt laugh pioneer with dissolve
    "Olga Dmitrievna... laughed?!"
    "Suddenly there was an acute desire to pinch myself properly to wake up - had something been done to Olga? She didn't even scold the culprit properly!"
    show mt smile pioneer with dspr
    mt "I didn't know you were such a crybaby, Semyon."
    me "I'm not..."
    mt "Cry about it. I thought in your couple you belonged to the stabilizing element."
    mt "I read Lena's character reference from school. Do you know what they say? Subject to discrete emotional swings."
    mt "So one second she's pounding you, the next she's hugging you."
    mt "It's okay, and some people even like it. But stability and peace of mind, of course, are out of the question."
    me "And what would Lena do?"
    "I wondered."
    mt "She would have approached me and asked for an assignment to another area - one where you could work together."
    if alt_day4_un_7dl_dv_us_explosives:
        me "Like what?"
        "I inquired."
        mt "Well, someone defaced the monument in the night."
        mt "I don't just guess - I know exactly who did it."
        mt "I also guess who could have stopped them, but didn't."
        me "So what, you're going to send us to scrub it?"
        show mt laugh pioneer with dspr
        mt "What a curious thought. {w}How did it not occur to me?"
        "She shook her head."
        mt "But no. I wanted to commission you and Lena to catch the culprits and atone for the sin of inaction - get them to clean the monument."
        me "Really?!"
        show mt sad pioneer with dspr
        if alt_day4_un_7dl_ducks:
            mt "You disciplined the juniors pretty well yesterday on stage."
            mt "I don't think Dvachevskaya is any different from them."
            th "If that Dvachevskaya had heard us."
            "I glanced involuntarily at Alisa slouching at the table, diligently hiding her palms under the table - she flinched, as if sensing my gaze."
        me "No, do it yourself. I'm a worse enforcer than I am a janitor."
        show mt grin pioneer with dspr
        mt "I didn't expect a positive answer. {w}Although, hoped for it, yes. You have good pedagogical potential, Semyon."
    me "Fire away! Let's see what option you picked for Lena and me?"
    mt "It's simple: you set up the tables until noon, and then I'll send someone here to lead the toy library for the younger squads, and you go clean up the square."
    "I didn't want to clean the square."
    "But the alternative was either to clean Genda - and I had no doubt that I could get Aliska to clean something - I couldn't."
    "Or let Lena go to the library before lunch."
    "And that was something I wasn't prepared to do!"
    "So I nodded slowly."
    me "All right. A square means a square."
    show mt normal pioneer with dspr
    mt "Didn't doubt your answer."
    "Olga nodded at me and headed to her table - unlike me, who managed to grind two servings, she didn't even have time to touch her coffee."
    "The citramone worked well, but it'll be a while before she gets her appetite. No wonder she's so angry!"
    hide mt with dissolve
    show un normal pioneer with dspr
    un "What were we talking about?"
    "Lena inquired. There were already two empty cups next to her - the girl knew how to be as well as show patience."
    me "Yeah, I didn't like the idea of letting you go anywhere before dinner."
    show un smile pioneer with dspr
    un "And?"
    me "Haggled. Got us an order to clean the square."
    show un sad pioneer with dspr
    un "I was thinking of drawing..."
    if 'nwsppr' in list_clubs_7dl:
        extend " And you would do well to write an article about last night's concert."
        un "I'll have to proofread and rewrite it in print, and that'll take half a day."
        me "So it's not the concert's destiny to go into the annals."
        "I smiled."
    show un serious pioneer with dspr
    un "What about drawing? I had such good caricature ideas today..."
    me "Is that while you were sleeping by my side?"
    "After hesitating, Lena nodded."
    un "Mostly."
    me "After lunch you can draw! I'll even help you!"
    show un shy pioneer with dspr
    un "If it's going to be like yesterday - you'd better not help. Otherwise I'll never concentrate!"
    me "Boo! And okay, I didn't feel like it."
    "I poked my tongue at her and arrogantly turned my nose up."
    "With a stifled giggle, Lena put her palm on my shoulder."
    un "Why do you always make fun of everything around you?"
    me "I don't make fun, I look for the positives. You know, like fairies - transparent, cheerful. Positive people."
    me "For example, Olga scolds us, hands to her sides, and I can barely contain my laughter, remembering how she showed up yesterday. {w}And if I say even half of what I think out loud, that's where I'll get buried."
    me "Or you, while you still wouldn't let me get close to you - sitting pouting like a mouse on a croup, I was even thinking of getting close to you with a needle."
    show un surprise pioneer with dspr
    un "Why?"
    me "To pop, of course!"
    show un smile2 pioneer with dspr
    play music music_list["get_to_know_me_better"] fadein 5
    un "That's not my word, that's what Alisa says. But it fits you perfectly. {w}You're a mocker."
    me "But I do it with no malice!"
    un "No malice."
    "Nodded the girl."
    un "You're from good. And that's the most frightening thing."
    un "I can't imagine what would happen if you decided to make fun of me."
    me "I won't."
    "Seriously, I promised, looking around - the dining room had noticeably emptied during our conversation, and we could finally get down to the first part of the daunting quest."
    stop ambience
    stop sound_loop
    scene bg int_dining_hall_rain_7dl
    show un normal pioneer
    with dissolve
    me "Ssstart?"
    "I went up."
    "Lena nodded and followed my example."
    me "Shall we start at different ends, or shall we work in parallel?"
    show un smile pioneer with dspr
    un "Together! Let's have a chat, too!"
    un "While you were out walking, I learned so much news about yesterday. Somehow you and I got caught up in each other - we fell out of camp life."
    un "And meanwhile - life goes on!"
    "She clutched two stools and carried them to the wall."
    me "And what's the latest news?"
    "I inquired, lifting up the long bench."
    un "Where to begin..."
    me "In chronological order come on!"
    "Me encouraged."
    un "So let's start with the day before yesterday."
    un "Olga Dmitrievna scolded our cyberneticists for still not fixing the radio."
    un "And it broke a few days before your arrival - in fact, it's already been idle for five days."
    un "As if that wasn't enough: she ordered them to set up not only music and horn signals, but to broadcast in the spirit of radio stations, for better or worse."
    me "With anchors and blackjack and..."
    "I bit my tongue."
    show un serious pioneer with dspr
    un "I don't know what blackjack is, but I guess so."
    un "Anyway, it was about time you and I escaped to the warehouse: Slavya was looking all over the camp for you - she wanted to get you involved in cleaning the room, which had been converted into a radio room."
    un "Then, that same evening, they stipulated to watch the antenna - for some reason the transmitter was inactive."
    un "So they did - while you and I were on our way to the infirmary, Shurik climbed up on the roof and either immediately or a little while later flew out of there."
    me "But that must have been a panic in the camp - an emergency, after all."
    me "I didn't hear anything."
    un "That's because by then we'd already left the infirmary.{w} And panic - there was. Remember that the counselor went around calling us in the evening."
    un "Anyway, Shurik hurt his arm, and they took him to the town next day. Viola took him away, so Electronik is taking over her duties today."
    me "Still not back?"
    "I pictured the Volga looking sadly with its wheels into the sky from a wet ditch."
    un "Yes. Viola said it might be possible, if Shurik is hospitalized."
    me "What a plot... It's epic. That's all?"
    if alt_day4_un_7dl_dv_us_explosives:
        un "Not enough? Okay. Do you remember the explosives incident yesterday?"
        "I nodded. According to Lena's request, I didn't interfere."
        "Although I've already been given a slap on the wrist for indifference."
        un "Anyway, they made some explosives. They wanted to blow it up."
        un "As a result, Alisa has burns on her palms and Genda is a little smoky."
        me "Mmmm... Smoked Genda! What a spicy dish."
        show un laugh pioneer with dspr
        un "Another one.{w} Now Elektronik will go to his club before his shift in the infirmary and get some boxes of GOI paste - Slavya will give the tools..."
        un "Now guess who's going to rub Genda's bronze plaid to a mirror shine."
        "Smiled the girl."
    else:
        un "Generally…"
    show un shy pioneer with dspr
    un "Don't think I'm some kind of gossipy girl..."
    un "It's just that I need material for articles and drawings."
    if alt_day_binder == 1:
        show un smile pioneer with dspr
        un "So I'm sorry, but your basin stand..."
        "She giggled."
        un "I already drew it."
    else:
        if (counter_sl_7dl == 0):
            if loki:
                un "I drew your meeting with Alisa and Ulyana, too."
            elif herc:
                un "I captured your feat of carrying Alisa, too."
            elif alt_day1_el_followed:
                un "I drew your running around with Electronik, too."
        else:
            un "And the way Slavya drags you by the hand, I drew it too!"
    me "Will it go in the paper, too?"
    show un grin pioneer with dspr
    un "Sure! There's a whole column devoted to you."
    "Thank you, I've always wanted to be popular."
    "However, when I looked into the girl's eyes, I just nodded."
    me "Thank you, that means a lot to me."
    "As usual, the chitchat got the better of us, and we fought for the last chair for a few more seconds, not wanting to give it up."
    "Nodded synchronously in response to the cooks' question as to whether they could go home."
    "Let them go - what a pity..."
    "And the slamming of the service doors caught us already embracing, furiously, until our kissed lips hurt, digging into each other."
    "And somehow all the same, an injection of painkillers straight into the mind - so serotonin and endorphins feed the mind."
    "And the hamstring becomes susceptible to the sun's rays, writing directly into memory the very warm memories that the narrow-minded mind for some reason calls «lamp» - though I am three times funnier to hear that epithet."
    th "I never promised you a ray of light in a dark realm."
    "Thoughts jumped, startled by the inquisitive gaze of the emerald eyes."
    th "I never promised you it would be all right, or at least as it should be. {w}It's not in my power - and it's not in anyone else's."
    th "One thing I can promise with absolute certainty. {w}I will never care where you are or what's wrong with you."
    th "Because you are me."
    "And I don't even want to promise silly things like I'll remember for the rest of my life. Yes, I will."
    "Her name was Anastasia. We were - but what... acquaintances? Colleagues? Friends?"
    "I was just beginning to thaw out after my three-year black winter, remembered that a smile is more than an irritant, and that laughing sometimes makes you want to laugh back instead of grabbing for splitting temples."
    "It's just that I once said that out of thousands of my passers-by, she was the only one who aroused interest, a searing one that stayed on my palms and cheeks with the redness of a slap, that made me wake up and breathe a little deeper than a surface-sleeper."
    "Aroused. Arouse... Will arouse?"
    "We'd only known each other for two months. We'd only met twice - on a level that neither of us was comfortable with."
    "And almost passed the point of no return after which there is no «me» and no «her»."
    "And then there's February, the streets of Nizhny Novgorod, the thaw, the ice."
    "For a man who managed to survive, should I have been so relaxed and done what I did?"
    "And yet in my memory she remained not a jagged doll, staring unseeingly with green icicles into the whitish sky, but a smile, a wink, a reaction to my fingers touching her palm - a tickle, a laugh, an indignation."
    "So what right do I have to promise to remember? Can I promise that I will breathe? That I will exist?"
    "And only the not-so-hasty Olga Dmitrievna who showed up prevented us from doing a little more foolish things than we usually do."
    show mt normal pioneer at right with dspr
    mt "I see you're not bored. Finished setting up the tables?"
    "She looked around, and Lena, not even thinking of moving away from me, looked defiantly at the counselor."
    mt "Well done!"
    mt "Well, have you forgotten what your next party plan is?"
    me "Forgot. Off to bed, right?"
    show mt laugh pioneer with dspr
    mt "Sleep in the afternoon, but now - march to Slavya for equipment and to the square!"
    "As if to confirm Olga's words, the rain drizzling against the windows came down smoothly."
    "With a synchronized sigh of sorrow, we held hands and went outside."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day5_un_7dl_games:
    scene bg int_dining_hall_rain_7dl with dissolve
    play music music_list["everyday_theme"] fadein 5
    "What am I..."
    me "Electronik, can you help me put the tables away?"
    show el normal pioneer with moveinright
    "Stopped me somewhere purposefully headed cybernetic."
    el "What? Tables?"
    "I nodded patiently."
    el "Why?"
    me "To give the little ones something to do: games of dice, dominoes, checkers and chess..."
    el "Oh... Okay."
    "He helped me pick up the table and drag it to the walls, and then I noticed some unfamiliar detail."
    me "Where's your friend?"
    th "Don't tell me you're having a marital spat."
    me "The Shurik one."
    show el sad pioneer with dspr
    el "You didn't know?"
    "The blond guy was surprised."
    el "They took him to town - to the hospital."
    me "Nothing contagious, I hope?"
    el "We thought you were going to help us the day before yesterday, but you went off to help Elena with the medicine. {w}So we had to manage on our own."
    me "Don't tell me he got electrocuted."
    "I couldn't take it."
    show el serious pioneer with dspr
    el "Worse."
    "Electronik got serious."
    el "The antenna on the roof got damaged - he climbed up, because my doctors gave me a fear of heights."
    el "And he fell from there. {w}Not hard, but got his hand caught badly and cut his forearm."
    th "Yeah, only Shurik was capable of that."
    "I was the one who thought I was a dullard for a while."
    "But compared to Alexander, I'm the height of prudence and prosperity."
    el "You shouldn't laugh. {w}It turned out to be serious if Viola hasn't brought him in by now."
    me "Viola? Hmm. {w}What if some pioneer got injured?"
    show el grin pioneer with dspr
    el "She left a list of sicknesses and medicines for Olga Dmitrievna, and she has already assigned all this to me."
    me "Are you going to be on duty in the infirmary?"
    "I delighted."
    me "That's where..."
    dreamgirl "Rubber products number two. Yes."
    el "What?"
    "Immediately the boy became interested. {w}Aha. That's what I told you."
    me "It's quiet out there."
    show el normal pioneer with dspr
    el "Yeah. {w}But it's kind of boring. Unless I'm lucky enough to get a book from Zhenya that's interesting."
    "The cyberneticist was rambling, anticipating the end of his work."
    el "Everybody's in business today. {w}Slavya's guarding the warehouse, you're the little ones, Lena's on the paper, Zhenya's the same, and I'm in the infirmary."
    if alt_day4_un_7dl_dv_us_explosives:
        me "And Alisa and Ulyana?"
        el "I don't know the details, but it looks like they'll be sent to the music club to clean the pipes."
        me "Really?!"
        el "Well..."
        show el upset pioneer with dspr
        el "Olga Dmitrievna said something about GOI paste, chemical sponges and dry abrasives. {w} We don't have that much copper to clean..."
        me "Oh. Well, yeah."
        th "But we do have a whole bronze Genda, which someone made an attempt on yesterday."
        th "And it seems to have partly succeeded."
        me "But it won't be until it dries out."
        el "Why?"
        th "Because otherwise Genda will forever be a mess!"
        me "Never mind."
        "I brushed it off."
        me "And by the way, thanks for your help!"
    else:
        me "Really, everyone's doing their tasks."
        me "Thanks for your help!"
    show el normal pioneer with dspr
    el "You're welcomed."
    if 'nwsppr' in list_clubs_7dl:
        "He was about to leave, but stopped half a step away."
        el "Also, if you're going to sketch an article for the paper, the paper and pencils are in the same room where the games are kept."
        me "And where, where are they kept?"
        el "They didn't tell you? {w}Come on, I'll take you there."
        "The cyberneticist led me through the kitchen and poked at the first door on my left hand."
        el "Everything you need is in here. {w}I don't have the keys, though. {w}But I guess Olga Dmitrievna will be here soon - wait for her."
        me "As if I had any alternatives."
        "I muttered, nodding goodbye and walking back out into the hall."
    hide el
    with fade2
    "Little by little, the hall began to fill."
    show mt normal pioneer with dissolve
    mt "I see you've already set everything up."
    "Olga Dmitrievna left her raincoat at the entrance and came up to me."
    mt "Come on, let's go sort out the games."
    me "Are there a lot of them?"
    "I squinted skeptically."
    mt "What did you think.{w} There are thirty kids here - that means at least ten boxes of games, not counting the boards for checkers, go-reversi and backgammon."
    me "I thought poorly and irregularly."
    "I lamented."
    me "I had plenty to occupy my mind as it was."
    show mt grin pioneer with dspr
    mt "I noticed."
    mt "If you'd come in a little later, you wouldn't have anything left in your head at all."
    me "Enough, huh?"
    "I sighed tiredly, stopping at an already familiar door."
    me "Better tell if there are any tricks of the trade."
    mt "No tricks."
    play sound sfx_keys_rattle
    "Olga went through the bundle and, finding the right key, nodded contentedly."
    mt "The chips in all games are the same, the dice are the same - they are kept in your possession and handed out against your signature."
    me "Nothing complicated."
    mt "Well. {w}The boxes of chess and checkers are also kept by you, just spread the fields out on the tables."
    mt "If the kids want Monopoly, you give them a stack of betting cards in addition to chips and dice. I guess that's it."
    "In between, she was loading me up with boxes familiar from my childhood: «Lurkomory», «Very Merry Pictures,», «Well, wait a minute!», «Monopoly», «Slides and Ladders», a number of slightly less familiar titles."
    "Of course, on top of that were five flat cards with chess fields and plastic rounded boxes with checkers."
    me "More papers and what to write with, since I'm handing them out against my signature."
    show mt normal pioneer with dspr
    mt "Makes sense."
    "Nodded the counselor, stepping back to her desk and from there pulling out a notebook and a thick red and blue cartridge."
    "And while she was walking, I had my eye on the Rubik's Cube lying there."
    menu:
        "Steal the cube":
            $ karma -= 10
            "Barely balancing the games on one arm, I instantly covered the toy with the palm of my hand - and immediately hid it under the games."
        "Do not":
            th "Why do I need it at all?"
            "I shrugged my shoulders and paid no more attention to the toy."
    "Finally, on top of everything else, as if testing the limits of carrying capacity, a 96-sheet notebook lay on top of all the boxes - purely visually, already a lot lighter than my predecessors."
    mt "I'll give you a pen when we get there. {w}You'll lose it."
    "In an unapologetic tone the counselor said."
    "I nodded."
    if 'nwsppr' in list_clubs_7dl:
        th "I'll send her off, and then I'll write about what was lingering in my head after yesterday."
        "It didn't take much, but the skills of networking include such exotic things as generating water on any scale, in addition to making fun of your interlocutor."
        "Here, for example, is such a simple thing as a little duck dance."
        if alt_day4_un_7dl_ducks:
            "While the kids and I were learning three consecutive moves, I was learning a lot of new and interesting things about them."
            "And not one byte of this new information can be uttered aloud in decent society - and it is not advisable to print it either, even our relatively liberal censorship won't let it through."
            "But the side effect is an involuntary search for metaphors and comparisons."
        "When you watch three minutes straight of looped three movements, only a progressive-house and yak-tsup-tsup-trained mind helps out."
        "Plagued by repetition, it willy-nilly switches to more constructive things, like the synchronicity of the artists' movements."
        "The expressions on their faces."
        "The costumes."
        "Even the way they're greeted by the audience."
        "And then, lo and behold, three paragraphs of 300 words."
        "And all he said was nothing - how the dumb kids clapped their hands, swiveled their pelvises and danced with their elbows to the same tune."
        "There was something else in there... I don't remember. Somebody seemed to be singing. Or was it a backing performance?"
        "After scattering the playing fields over the tables, I sat down at the center table and, after letting the counselor go,"
        hide mt with dissolve
        extend " I was deep in thought as to whether the notion of dancing to veneer was known in the current time period."
        "Although you could twist yourself around and write about the triumph of unbearably developed socialism, open house, and the stoicism of parents who didn't even allow themselves to wince during the performances."
    else:
        "After spreading out the playing fields on the tables, I sat down at the center table and let the counselor go."
        hide mt with dissolve
    pi "Hello. Checkers for me, please."
    me "Checkers?"
    "A familiar red-eyed pioneer."
    pi "Yeah, I'll play Chapai."
    me "I wish I could forbid you..."
    "The pioneer froze."
    me "I don't care. Sign here and take a field to the corner table so the checkers don't get all over the dining room."
    pi "Thank you!"
    "He glowered and, signing in the signature column, whisked the future machine-gun battery away behind him."
    "It occurred to me that I wouldn't mind a game of dodgeball myself right now..."
    dreamgirl "Yeah, yeah... A game of dodgeball, a three-liter «Honey» and a fucked-up heart after «doggy buzz»."
    dreamgirl "Don't think your pioneer childhood was a blissful one. I'm not a memory, I remember everything."
    if 'nwsppr' in list_clubs_7dl:
        th "Screw you, goldfish. I'll write an article."
        "I nodded placidly and stammered on the subject of hordes of inspectors, Shchedrin's three generals for one soldier, and the beautiful concert host dressed in a stunning tight silk dress."
        dreamgirl "What are we writing about? About concerts?"
        th "What?"
        dreamgirl "Yes it seemed suddenly like you were writing a piece praising Miku. I'm not an advisor, but I don't think the last part of the article should be shown to Lena."
        "After rereading the last few lines, I grabbed my head and tore out the whole page."
        th "So what was it about, then..."
        dreamgirl "Yeah. No backspace???"
        th "Don't waste your breath. Give me a topic."
        dreamgirl "You have a topic. You just have to make it more open in a different way."
        dreamgirl "Remember your last festival and what you wrote about it? Try dancing on the same theme."
        th "The scale is not the same..."
        dreamgirl "It doesn't matter. Write about unification, artists, technique, and other nonsense. {w}No. Don't write about artists, I know you."
        "I nodded in agreement - and the pen ran through the blue cells again."
    "The rain drummed melanchologically on the windows, the pioneers moved chips leisurely across the fields - there was an atmosphere of lazy relaxation in the room, and so the appearance of Olga Dmitrievna made me shudder."
    show mt normal pioneer with dspr
    mt "How's it going?"
    me "Like soot."
    "I brushed it off."
    mt "It's one o'clock - time to set up the tables and let the men on duty work."
    me "And who's going to put them up?"
    show mt grin pioneer with dspr
    mt "And whoever you attract, that's who you'll have."
    "The counselor smiled slyly, never giving up on the idea of making me almost an educator."
    me "Okay."
    "I stood up and clapped my hands, drawing attention."
    hide mt with dissolve
    me "Dear visitors to the Toy Library, thank you for visiting our place."
    me "In half an hour we start getting ready for lunch, so I'm now announcing a giveaway tournament with a prize pool of..."
    "I wondered."
    me "Twenty candy!"
    me "The winner gets eight candies, second place six, third and fourth places three each."
    mt "Where are you going to get so much candy..."
    me "The general sponsor is Olga Dmitrievna."
    "I threw a generous gesture toward the counselor, but she was not confused."
    mt "And Semyon's backpack."
    if alt_day4_me_neu_transit == 'un_7dl':
        me "Excuse me?"
        show mt laugh pioneer with dspr
        mt "Oh, you don't know."
        mt "There's a guest waiting for you at home. From your parents."
        me "And you didn't say anything?"
        show mt grin pioneer with dspr
        mt "I didn't want to spoil the surprise."
    "As they say, the main thing is the right motivation."
    "The winner was determined in fifteen minutes - and I explained to him that the prize wouldn't be available until after lunch, and in order for lunch to take place..."
    "And so magically I had four helpers appear out of nowhere."
    "The counselor stood there, quietly dying of laughter."
    show mt laugh pioneer with dspr
    mt "What a bug you are, Semyon."
    "She moaned, wiping away unsolicited tears."
    mt "And if I refused to sponsor the tournament?"
    me "The redheads would have been ransacked."
    "Serenely I shrugged my shoulders."
    me "Also, taking your word for it, I got something from my folks there - I didn't set up the foundation empty-handed."
    show mt smile pioneer with dspr
    mt "That's right. Let's make it fair - we'll allocate half the fund from your «Start», and I'll provide the other half. All right?"
    "I shook the outstretched palm, which turned out to be surprisingly tiny relative to mine."
    show mt normal pioneer with dspr
    mt "Still... Think at your leisure about a career as a counselor. You're not hopeless."
    me "That's where we stand!"
    "Proudly I straighten my chest."
    mt "Don't be so proud. You still have to learn."
    me "I'm not proud... I've seen what you're capable of in terms of manipulating other people's behavior."
    me "I feel like you're at ULM studying political technology, not pedagogy."
    show mt grin pioneer with dspr
    mt "Like there's a difference."
    "The counselor smiled dazzlingly."
    mt "So long!"
    hide mt with dissolve
    "The clock read twenty-five minutes, so I decided not to go far and took a seat on the benches that stretched along the railing on the porch."
    with fade2
    $ persistent.sprite_time = "day"
    $ day_time()
    scene bg ext_dining_hall_near_day with dissolve
    play sound sfx_7dl["eat_horn"] fadein 1
    "After reading some book, I shuddered when the tin horns overhead shrieked, urging the pioneers to save their immortal stomachs."
    th "I hope it's not going to be some kind of fish... {w}However, fish day is supposed to be on Thursdays..."
    th "Who cares, really. Where's Lena?"
    "Crowds of wet pioneers were trickling past me into the canteen."
    "Even though I was staring, I couldn't see Lena among the pioneers."
    th "Didn't come?"
    show mt normal pioneer with dspr
    mt "Semyon, why are you sitting here?"
    "Asked the counselor, who looked out on the porch."
    me "Where did Lena go?"
    "Unfriendly, I muttered."
    mt "In the library, I've already told you."
    me "Yeah, and she got so caught up in it that she decided to skip dinner?"
    mt "Don't be silly. {w}Ask Zhenya at lunch if you want to. And now - march to eat."
    "When she spoke like that, it was better not to argue with her."
    stop sound fadeout 3
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day5_un_7dl_dinner:
    play music music_7dl["carefree"] fadein 2
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 5
    if dr:
        "The canteen hummed like a beehive - the pioneers, frozen during the morning, were urgently restoring the energy spent on heating."
        "Brine, pilaf, and compote are all the substances a man needs. A child risks being bloated to death with it. Although, you can't call a pioneer a regular kid."
        "Their metabolism is definitely faster."
        "Lena was running late, and I was all twisted up looking for the native ponytails."
        dreamgirl "There isn't one. Sit back and eat quietly: I'll let you know."
        th "It's just like yesterday. How can I eat quietly - I'm worried!"
        show mz normal glasses pioneer with moveinright
        "Buzzer walked by, and I stopped her with a question:"
        me "Zhenya, hi! Are you from the library?"
        mz "Wow. How did you guess?"
        me "Gifted since childhood."
        "I cut off."
        me "Can you tell me where Lena is? They took her to you."
        if alt_day4_me_neu_transit == '':
            mz "You were working for me yesterday for a duplicate key."
        mz "Said she'd lock up - stayed in the library."
        "Lena stayed in the library? She's not hungry? Doesn't want to see me? Anything else?"
        mz "I'm going to eat."
        hide mz with dissolve
        "She notified and, without waiting for an answer, headed for the distribution."
        "And I closed my mouth, put my jaw back in place, and asserted my desire to sit here - until I turned green, if necessary - but to wait for the princess from her voluntary confinement."
        sl "May I sit down?"
        "I raised my head."
        show sl smile pioneer with dissolve
        "Slavya... As usual, very pretty, smiling and disgustingly optimistic."
        me "Sit..."
    else:
        "Lena was nowhere to be seen."
    $renpy.notify('«Rassolnik» - One of the main types of hot soups in Russian cuisine.')
    "Slavya sat down next to me and, after placing the plates from the tray on the table, deepened into devouring the rassolnik."
    me "Bon appetit."
    "I wished."
    if dr:
        show sl smile2 pioneer with dspr
    else:
        show sl smile2 pioneer with dissolve
    sl "Thank you. You too."
    "I've already eaten everything I could reach and was stuffed to the brim, but I mumbled something inarticulate and thankful just in case."
    if dr:
        me "Slavya, is there anywhere you can wash up?"
        sl "Thought you wouldn't ask."
        "She smiled."
        sl "Our showers will be open in the afternoon."
        me "They were closed..."
        sl "Well, yeah. But they opened them up yesterday for the parents, cleaned them out and heated them up."
        me "Generous! What about today?"
        show sl smile2 pioneer with dspr
        sl "It's raining! The rules say the showers are supposed to work."
        "I've never heard of such rules, but I didn't argue. Here's more."
        me "Will you show me?"
        sl "I'd be right happy to."
        "She chewed for a while longer, thinking about something."
        "And then she decided that I already knew all the details."
        sl "Just be careful there: after cleaning the monument, Alisa and Ulyanka might be around."
        me "What are you talking about?"
        show sl shy pioneer with dspr
        sl "I thought you knew."
        sl "They wanted to blow up Ganda's monument yesterday."
        if alt_day4_un_7dl_dv_us_explosives:
            me "Ulyana said something like that, yes..."
        else:
            "It looks like the little one listened to me, but did it her own way."
        show sl smile2 pioneer with dspr
        sl "But instead they just got him dirty."
        sl "The soiled Genda... It's embarrassing. {w}The fact that it rained was probably a good thing."
        me "It's a good thing they didn't let them near the monument before the rain stopped, or they'd have been covered in soot, Genda and everyone else passing by."
        sl "Well, they're covered in soot anyway... {w}That's why they weren't at lunch."
        me "Thanks for the warning!"
        if (counter_sl_7dl >= 1):
            sl "You're welcome. You wouldn't want them to smear you or get your clothes dirty."
            "The compote, though I pulled it as hard as I could, ended up running out."
            show sl smile pioneer with dspr
            sl "But if you want, you can wait a little while, and I'll guard your things."
            me "You must have a lot to do..."
            "Struggling with laughter, I stretched out."
            sl "It's okay, half an hour..."
            show sl scared pioneer with dspr
            "Slavya was silent, looking over my shoulder."
            sl "I'm getting a little carried away."
            hide sl with dissolve
            "Suddenly she was scrambling, quickly putting the plates on the tray and retreating."
            "When I followed her frightened look, I smiled against my will."
            "Lena."
            show un angry2 pioneer with dissolve
            un "What, you're into blondes?"
            me "Very funny. Will you tell me where you've been?"
            show un smile pioneer with dspr
            un "Yes. Will you sit with me?"
            me "Sure."
        else:
            sl "You're welcome."
            hide sl with dissolve
            "Slavya smiled and left me alone."
            "Thank goodness, not for long - a few minutes later a very familiar voice asked from somewhere above:"
            un "Young man, is this place free?"
            show un smile pioneer with dissolve
            me "Lena..."
            un "She herself, yes. Is that okay?"
            "She outlined a pointing motion with her tray, and I realized."
            me "Oh, sorry. Of course."
        "Acting like a real gentleman, I helped the lady to her seat, set the table, sat across from her and took on the most high-minded of looks."
        show un laugh pioneer with dspr
        un "And how do you not get bored with wriggling?"
        me "A man should smile at least seven times a day - psychologists have counted."
        un "Yeah, or at least once a day punch someone in the face - I had to read that article, too."
        th "Yes, that's her, and she hasn't been replaced by anyone during her absence."
        "She did look a little different, though - like she'd dropped some of the weight on her shoulders."
        me "I was worried. What kept you?"
        un "I'm sorry."
        show un shy pioneer with dspr
        un "I got a little into drawing."
        dreamgirl "Yeah. Drawing."
        me "What have you been drawing?"
        show un smile pioneer with dspr
        un "The same thing I've been drawing for the last three days..."
        un "You."
        me "Will you show me?"
        show un shy pioneer with dspr
        un "W-well..."
        "For some reason she was embarrassed."
        un "Not now, okay?"
        th "She's acting weird. Is she hiding something?"
        dreamgirl "Hiding some thing. Though I assure you it's not at all what you think it is."
        th "How would you know if it is or isn't?"
        dreamgirl "Unlike you, I know exactly what her reaction, her look, even the frequency with which her chest heaves..."
        th "And you're going to tell me everything now, of course?"
        dreamgirl "No, of course not. Spoilers are for wimps - guess for yourself."
        "The inner voice went silent."
        me "And if I decide to insist?"
        un "Then you'll embarrass me even more, but I won't show you anything anyway."
        me "Fine."
        show un surprise pioneer with dspr
        "She opened her eyes in mute surprise when her feet made contact, but she was in no hurry to pull away."
        "It's not at all like stroking a foot - psychology works. The contact is a little closer, a little more intimate."
        if 'nwsppr' in list_clubs_7dl:
            me "And I wrote an article. About yesterday."
            "I bragged."
            show un smile pioneer with dspr
            un "You're so good! Will you let me read it?"
            me "Sure. Let's hide somewhere where Olga Dmitrievna can't pester us?"
            show un grin pioneer with dspr
            if alt_day4_me_neu_transit == '':
                un "Of course. Did we have to work for Buzzer for nothing?"
                mz "If you call me that again, you'll have to put up with me again!"
                "A librarian's voice came from afar."
                show un laugh pioneer with dspr
                un "What a keen ear. {w}Anyway, I'll finish this and then we'll go."
            else:
                "I'll finish this now, and then we'll go."
            me "Then bon appétit!"
            un "Yes."
            "The girl spooned up in a way that even Ulyana would have been able to shame."
            "Not ten minutes later - and we were already outside."
            play sound sfx_open_door_2
            stop music fadeout 3
            stop ambience fadeout 6
            with fade2
            return
        else:
            pass
    else:
        play music music_7dl["ask_you_out"] fadein 3
        sl "You spend so much time together."
        "Slavya licked her spoon and set her plate aside, immediately establishing her elbows in the vacated space."
        sl "You and Lena."
        $renpy.notify('«Under a stick» - without much enthusiasm.')
        sl "Not that I mind: before you came along, she was doing everything from under a stick, even painting reluctantly, and you had some effect on her."
        me "Wait. What are you telling me now? Are you hinting at something?"
        sl "Absolutely not!"
        "The activist smiled charmingly."
        sl "But around the squad, for instance, rumors are creeping in... And in camp you can't imagine one without the other anymore."
        me "That's the way we are - anywhere together."
        sl "I'm just curious, how serious is it with you two? Peace, friendship, bubblegum?"
        me "Uh..."
        "I blushed."
        me "You could say that."
        show sl shy pioneer with dspr
        sl "So it's nothing like that?"
        me "No."
        "Despising myself, still red as a crab, I replied."
        show sl smile pioneer with dspr
        sl "Very good! Oops."
        "She's got it all figured out."
        sl "I mean, if you're free, we could..."
        me "What?"
        show sl shy pioneer with dspr
        sl "No, nothing. I just."
        me "Slavya, I'm sorry, of course, but I have all the telepaths and clairvoyants on vacation, and your innuendos I just simply do not understand!"
        show sl normal pioneer with dspr
        sl "It's nothing. {w}You don't have to."
        "Losing interest in the conversation, I shrugged my shoulders and returned to my unfinished soup."
        "And Slavya was pensively silent, picking at the tablecloth with her finger."
        "At last she made up her mind."
        sl "But just in case... If you and Lena are really nothing serious, and you won't hurt her like this..."
        me "Then..."
        "Encouragingly, I stretched out."
        if alt_day2_bf == 'sl':
            sl "Remember on your second day, when you sat down next to me?"
            sl "I was still talking about dancing then, and you agreed to ask me out."
            if alt_day3_dancing1 == 'sl_1':
                sl "And we had a great dance!"
            else:
                show sl sad pioneer with dspr
                sl "But, you never invited me."
                sl "But I'm not offended, if you didn't invite me, you couldn't invite me, it happens."
            me "Yeah. What's your point?"
            "The girl's innuendo was pretty transparent, but it's better to ask twice."
            show sl smile2 pioneer with dspr
            sl "You figured it out just fine yourself!"
            "She laughed."
        sl "Tomorrow the farewell disco will be an hour longer, until midnight. {w}And if you're free, I'd like us to dance together, and-"
        th "Yeah, 'cause I forgot the last disco."
        sl "If you're free, of course."
        "With pressure, she repeated."
        me "But I don't..."
        th "Something I highly doubt our cardinaless could be unaware that the boy is busy."
        th "Why these games at all!"
        show sl normal pioneer with dspr
        dreamgirl "Of course. And she just licks her lips. And she touches you with her foot under the table, too."
        th "Foot? Get over it, it's... that... The post on which the table stands! Here."
        dreamgirl "Ahha. Stand. It's soft and it has a temperature of 36.6 degrees."
        "After figuring out what was really going on, I yanked my foot away."
        "And I stared silently at the activist girl... Active in all things."
        show sl surprise pioneer with dspr
        "She gave me back my own perplexed look, saying - Free, what's wrong?"
        "I had already opened my mouth to say it out loud - some things seem to have to be written in huge letters on banners, otherwise they won't be understood."
        show sl sad pioneer with dspr
        sl "So what?"
        me "Sorry."
        dreamgirl "You, girl, are awesome, but I'm not thrilled about this aggressive approach."
        th "Agreed."
        dreamgirl "Let's just take it easy, because Lena might notice."
        me "Make up your mind. Either take care of Lena or take care of yourself."
        th "It's like we're different people."
        me "I've made my choice - I'm going to stick with it."
        show sl smile pioneer with dspr
        sl "Well, at least I tried."
        "She smiled as hard as she could and stood up and nodded to the approaching Lena."
        sl "See you later."
        "Without looking back, she tossed over her shoulder, holding a posture that would put even a career officer to shame."
        me "Bye..."
        hide sl
        show un normal pioneer with dspr
        un "Hi. What were you and Slavya talking about?"
        me "Just... little things."
        show un serious pioneer with dspr
        un "Interesting."
        un "Will you tell me what it is about this little thing that makes the activist go away with the eyes of a battered dog?"
        me "There's been a misunderstanding."
        show un sad pioneer with dspr
        un "Which, of course, you're going to tell me about now."
        me "Uh, there..."
        show un angry2 pioneer with dspr
        un "Semyon."
        "Softly she interrupted me."
        un "Tell me."
        me "There's nothing to tell. It's just that the whole camp is buzzing about you and me going everywhere together."
        un "Let it buzz. Or are you afraid of being jinxed?"
        me "No. It's just that Slavya was just pestering me about the seriousness of what's between you and me."
        un "And you..."
        me "And I told her to stay out of our friendship."
        show un rage pioneer with dspr
        un "Friendship?!"
        "She got up off the bench."
        me "Hey, hey... Calm down."
        "I caught the girl by the arm, who was starting to boil, and sat her back down next to me."
        me "It's hard for me to talk to outsiders about how I feel about you. Especially when Slavya asks."
        un "Difficult? Or is it convenient? Just you tell me - I won't get in the way. We have a friendship, and she's had her eye on you for a long time."
        show un sad pioneer with dspr
        me "What? No, stop it."
        un "Well, I'm not stupid, Semyon."
        un "And I can see how she's been flirting around you."
        "Lena lowered her voice."
        un "Actually, I'm surprised she waited so long."
        me "Lena, you're jealous like you have a reason to be."
        "I grinned back."
        show un surprise pioneer with dspr
        un "What?! Jealous? Me? I'm not..."
        me "Jealous. {w} And for nothing, by the way."
        me "I've already told you who I want. {w}It's just... It's none of her business, really."
        me "Because if she sees immorality in our actions, she'll tell the counselor everything, confident that she's doing the right thing."
        me "By the way, she asked me to the dance tomorrow. She asked me to get her name in my ball book, too."
        show un angry2 pioneer with dspr
        un "No way!"
        "My chosen one snorted."
        un "I know - first you dance together, then you go out..."
        "I froze."
        th "How does she know about the invitation to the walk?"
        un "Don't turn pale - I saw you say no. But no dancing with Slavyana, understand?"
        me "Understood."
        "I smiled back."
        un "Glad we came to an understanding."
    show un smile pioneer with dspr
    "She pulled me up by my shirt and kissed me somewhere on my cheekbone."
    un "Are you going to go wash up after lunch?"
    me "Lena, I'm not going anywhere with you where I have to undress! And stop teasing me already!"
    show un laugh pioneer with dspr
    un "Literally nowhere?"
    me "Exactly!"
    show un grin pioneer with dspr
    un "Even on the beach?"
    if loki:
        un "On ours."
    elif herc:
        un "Yesterday's."
    me "Unless it's just to the beach."
    th "At least someone will be there to control me - the pesky pioneers, Olga Dmitrievna's bass, Boris Sanich's whistle..."
    dreamgirl "I liked about the bass, by the way."
    show un smile2 pioneer with dspr
    un "It's a deal! After lunch we go to the beach! And just dare to say no."
    me "I wouldn't dream of it."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day5_un_7dl_article:
    scene bg ext_dining_hall_near_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    show un normal pioneer with dspr
    un "Shall we go?"
    show un smile pioneer with dspr
    "Lena habitually already pinched my little finger and smiled."
    me "Let's go!"
    scene bg ext_library_day
    with dissolve
    show un normal pioneer at center with dissolve
    "We gave a tangible circle, circling the counselor standing in the square - we had to take a left through the warehouses, the volleyball field, the back of the infirmary, and the fun houses through the bushes."
    "It was worth it! Olga Dmitrievna would be sure to «forget» that I had agreed to slave only until lunchtime, and would be sure to write me another assignment for a useless activity."
    show un smile2 pioneer with dspr
    "We're walking by the hand again - I'm the pilot again, Lena's laughing again."
    "It's probably right that we got it so spontaneously."
    th "Otherwise we'd both be crumpled and embarrassed, and we wouldn't have relaxed to the point we wanted to at all."
    "Could I imagine a giggling Lena hiding behind my shoulder and pointing her finger at my side to keep my nose down?"
    "No way! She's so... so... Anyway, not our case."
    "The key turned noiselessly, and we fell into the room, slamming the door behind us."
    scene bg int_library_day
    with dissolve
    play ambience ambience_library_day fadein 3
    play music music_list["two_glasses_of_melancholy"] fadein 1
    show un smile pioneer with dissolve
    un "Well."
    "Lena began, catching her breath a little."
    un "We got away from Zhenya, and we got away from the counselor."
    "She climbed into one of the chairs and tucked her legs under her."
    un "Give."
    me "What?"
    show un laugh pioneer with dspr
    un "Everything you not greedy about!"
    me "And I'm greedy about everything!"
    "I answered in tone, taking a quadruple folded piece of paper in a box from my breast pocket."
    me "If you don't understand something, tell me, I'll translate it."
    "I warned her, handing her a draft of the article."
    show un normal pioneer with dspr
    un "Uh-huh."
    "Taking the sheet from me, Lena immersed herself in reading, unconsciously muttering aloud."
    un "Nothing foretold trouble. Written by Persunov Semyon."
    un "Uh-huh... uh-huh..."
    un "Yesterday, as part of the amateur concert for parents, there were a number of performances by pioneers from the younger squads."
    un "Nothing foretold trouble when they came onstage, the brutes of Squad 6, with their little duck dance."
    un "It started innocently enough: the music played, they got ready, and..."
    un "A few seconds later there were panicked cries of «Ahhhh, my eyes!!!» and «Make me unsee this, please!», some people's eyes were bleeding."
    show un angry pioneer with dspr
    un "What is this?!"
    me "Article."
    "I made innocent eyes."
    un "It's an article?! It's not an article, it's some kind of a nightmare!"
    me "Not some kind, it's exclusive."
    show un angry2 pioneer with dspr
    un "And what kind of a word is «unsee»?!"
    "I couldn't stand it and laughed."
    me "Turn the leaf over, miracle - the article is on the back."
    un "What's that?"
    me "Warming up, what."
    show un sad pioneer with dspr
    un "Caught me, didn't you? You must be pleased with yourself..."
    "Finding the article on the back, Lena immersed herself in reading."
    "And this time, she read in earnest."
    show un normal pioneer with dspr
    un "Yes, that's better."
    "She said, putting the paper aside."
    un "By the way, your handwriting isn't that terrible. You might as well try rewriting it yourself."
    "I waved my hands."
    me "Don't even think about it!"
    me "You're going to write... And I'm going to..."
    show un smile pioneer with dspr
    un "Yeaa-ah?"
    "She protested."
    me "And I'm going to hit on you!"
    un "Why don't you hit on me first, and then we'll go to the paper to file the story?"
    me "It's more interesting at the same time!"
    show un laugh pioneer with dspr
    un "...and forgive the uneven handwriting."
    me "Do you have jokes like that, too?!"
    un "No... It's just that my dad works for the police, and his jokes are..."
    me "Specific."
    "I nodded."
    "Suddenly I saw a picture in my head of a man in a police uniform pointing a finger at me - sequentially: «And if you don't get married, they'll declare you fit»."
    me "There's so much I don't know about you, it turns out."
    show un smile pioneer with dspr
    un "Have you tried asking?"
    "Without taking her eyes off the paper, the girl asked."
    me "I wish I knew what to ask."
    "I landed on the floor and threw my head back on the leather seat of the chair, where Lena had already thrown her legs on the armrest."
    "Her fingers immediately found my hair and dug deep into it, reminding me that the last time I washed was a hell of a long time ago."
    "And a haircut wouldn't hurt, either."
    dreamgirl "And shave."
    th "Mock more."
    me "It's good with you."
    "I sighed, quietly smiling under her touch."
    un "And that's why you write your bloodthirsty articles?"
    "She snorted, mechanically stroking my hair."
    me "No... I wrote that for the mood. {w}You smiled, so the mission is accomplished."
    un "I would have smiled anyway, without any duckies."
    "Hovering over me, she touched her lips to my forehead."
    me "So what about your drawing?"
    show un shy pioneer with dspr
    un "Drawing? {w}It's... It's not ready. And I don't want to show it yet."
    me "Lena."
    "Even though the mood wasn't conducive, I managed - I squinted suspiciously and asked:"
    me "So, spit it out - what are you hiding?"
    un "Nothing..."
    hide un with dissolve
    "She grew sad, jumped out of her chair and got lost behind the shelves, heading for the editing room."
    stop music fadeout 5
    "Somewhat discouraged by her silent response, I got up and followed her."
    me "Len?"
    "No answer."
    me "Lena?!"
    "Silence."
    stop ambience fadeout 6
    play sound sfx_open_dooor_campus_1
    return

label alt_day5_un_7dl_unl:
    scene
    $ renpy.show("bg int_editorial_day_7dl", what = Notch("bg int_editorial_day_7dl"))
    with dissolve
    "When I reached the door, I cautiously pulled it open and blinked into the unexpectedly dark, contrasting room."
    "Lena was standing at the table, holding a small, A4-sized piece of paper."
    show un serious pioneer far with dissolve
    "Looking closer, I could make out only the white background: apparently she was holding the drawing toward her, not anxious to show me her artwork."
    un "Semyon, I want to tell you one thing."
    me "Yes. Of course. What did you want to say?"
    "She handed me a drawing - the kind they call a linart in my day."
    "Basically, just an unpainted drawing with no shadows, halftones, or other nonsense."
    "Just finished outlines made with a thick graphite rod."
    "There... There she was. I. And..."
    me "And who's that?"
    un "It's..."
    "She inhaled several times, apparently gathering her strength."
    show un serious pioneer with dspr
    un "I wasn't always what I am now. There was something else...{w} Someone."
    un "One..."
    with vpunch
    play sound sfx_scary_sting
    "She opened her eyes, and once again I was flooded with memories."
    "This time, though, they were with someone else's scent, someone else's mind... They belonged to Lena."
    if alt_day_binder == 1:
        play music music_7dl["but_why"] fadein 5
    else:
        play music music_7dl["knock"] fadein 5

    scene anim prolog_1
    show prologue_dream
    with fade2
    $ meet('unp',"Alyona")
    $ set_mode_nvl()
    "{i}I'm screaming, blowing my vocal cords to zero.{/i}"
    "{i}And once again she takes me for the angels she loves so much.{/i}"
    nvl clear
    "The fulfillment of your deepest dreams, everything you ever wanted - nine millimeters to the head, a sharp feather tickling your wrist, and the weeping sky washing a halo of blood around your broken body at the foot of the skyscraper."
    nvl clear
    unp "{i}Hello, Lena.{/i}"
    "{i}She's smiling, almost invisible against the grayish pillowcases.{/i}"
    unp "{i}You're so beautiful today. {w}You can believe me - I can see it.{/i}"
    "{i}Yes.{w} She can see it.{/i}"
    "{i}Our names are similar, but how different we really are.{/i}"
    nvl clear
    "I am beating against the bars of the cage that holds me in this impossible reality."
    "I am the silent, only spectator in an abandoned movie theater, where «Nightmares on Elm Street» is looped on the screen, and tendrils stretch from my hands to the sky, puppetically making me move."
    nvl clear
    scene bg int_ward2_sunset_7dl
    show prologue_dream
    with flash2
    "{i}Junior. Alyona.{/i}"
    "{i}I pick up my notebook from the nightstand and I see the same angels with my eyes.{/i}"
    "{i}I've never been able to draw. {w}Never, you know?{/i}"
    "{i}It's very hard to put into words, and it's very infuriating that you can't just open your heart and let someone feel - what it really feels like when the only person you care about dies in your arms.{/i}"
    "{i}Big-headed, shaven-naked, with pale clear skin, eyes sunken after chemotherapy - she stares through the sideboard glass in silent reproach at what we did not save.{/i}"
    nvl clear
    unp "{i}Lena...{w} I wanted to learn how to draw.{/i}"
    unp "{i}I can see beauty - I just have to learn a little and I can show it to others.{/i}"
    un "{i}I know...{/i}"
    "{i}I hold her hand and keep quiet.{/i}"
    "{i}She was barely nine when the walls of her typical khrushchevka apartment were etched with the icy horror of diagnosis.{/i}"
    "{i}Bleakness. {w}The very, little-explained error in the workings of the blood cells when they forget what they're supposed to be doing.{/i}"
    unp "{i}Now I probably won't learn.{/i}"
    "{i}Her palm is hot and weightless, and somehow it reminds me of a bird's foot.{/i}"
    unp "{i}Do it for me, please...{/i}"
    un "{i}What? Do what, darling?{/i}"
    "{i}I would do anything for those pleading eyes.{/i}"
    un "{i}Ask anything you want.{/i}"
    unp "{i}Fulfill my dream, yourself...{/i}"
    un "{i}What?{/i}"
    unp "{i}Draw something, okay?{/i}"
    nvl clear
    "{i}And I've never held a pencil in my hands, but now..."
    "{i}The first lines were crooked, uneven, wrong, unfair. {w}They are inappropriate now, and therefore three times cruel.{/i}"
    "{i}I don't know that I'm going to get lines like that for a very, very long time.{/i}"
    unp "{i}Draw a dragon, please, like the one that burns me from inside.{/i}"
    un "{i}Yes, yes.{/i}"
    "{i}I look up at the ceiling and swallow often, drying my eyes.{/i}"
    un "{i}Now. I'll try.{/i}"
    "{i}The resulting monster looked like anything but a dragon, but Alyona smiled contentedly and leaned back on her pillow - achingly defenseless, mercilessly weak.{/i}"
    unp "{i}Thank you, Lena.{/i}"
    "{i}She whispers.{/i}"
    unp "{i}You're the best sister in the world.{/i}"
    un "{i}Yes...{/i}"
    "{i}I squeeze her hand and refuse to believe it's getting colder.{/i}"
    unp "{i}Promise you won't leave it.{/i}"
    unp "{i}Promise that one day you'll hang a picture on the wall of you and me and someone who loves you the way you love me.{/i}"
    nvl clear
    "{i}There are thousands of hours of frustration, tantrums, tears, and the desire to smash everything, including my own head, against the wall, but I clench my jaw until my cheekbones ache and keep scribbling on the paper with a pencil.{/i}"
    "{i}I nod, and instead of tears I remember her eyes - sapphire eyes, priceless, open to meet me...{/i}"
    "{i}As if they knew that their age was short, and therefore insatiably drank life itself, absorbing impressions as not every artist or writer can...{/i}"
    nvl clear
    scene anim prolog_1
    show un cry pioneer
    show prologue_dream
    with fade
    un "I hate drawing. {w}I never wanted to."
    un "But more and more often, if I don't think about anything, like now, talking to you, I get angels with sapphire eyes."
    un "And then there was the funeral, the stopped gaze of my mother, who only outlived Alyona by six months, and the icy sarcophagus in which I have lived for the last five years."
    un "She had unbearably sapphire eyes, looking at this world with the directness of a human being who believed that the world was not black, not meaningless."
    un "I guess only babies can do that... {w}And those who dying before their time."
    un "Can you imagine the irony that all these pictures - all this - were written by a dishonest crook, a person who takes hold of a pencil every time like a dangerous razor blade, trimming to the bone, crusting off the unhealed ulcer in her heart."
    nvl clear
    $ meet('unp',"Pioneer girl")
    $ set_mode_adv()
    show blink
    stop music fadeout 4
    "The eyelid drooped, cutting off someone else's background, leaving me tormented by belated remorse - because people don't just become like Lena for no reason!"
    "And splitting temples."
    scene bg int_editorial_day_7dl
    show un cry_smile pioneer
    show unblink
    play music music_7dl["old_kiss"] fadein 3
    un "But I don't know how to express myself any other way. {w} Perhaps Alyona would have been happy for me."
    un "And today I sat, painted and thought of you. Drawing you."
    un "And when she jumped out from under the pencil like alive.."
    un "...I couldn't calm down for a very long time."
    "I handed her a handkerchief and the girl nodded appreciatively, wiped her tears away."
    me "I'm sorry I insisted... I didn't know it was so personal."
    "For some reason, at this moment, the natural urge to hold the crying girl close to me could not override my usual stupor."
    "Though it seemed as if I had overcome it."
    show un normal pioneer with dspr
    "And she, as if understanding my awkwardness, turned away, leaned on the table with clenched fists, looked down and sighed deeply."
    un "I don't know why it happened, or why it came to mind."
    un "Maybe because of my attitude toward you... Or maybe because of what Olga Dmitrievna said at breakfast."
    me "And what did she say?"
    "I inquired, finally coming to my senses and taking a tiny step toward Lena."
    un "She said..."
    me "Yes..."
    "Stepping a little closer still."
    un "That..."
    me "Yes..."
    un "We..."
    me "We..."
    un "In lo..."
    show un normal pioneer close with dissolve
    "I snuck close enough to hug her and hold her to me."
    "I don't think hugs could ever solve anyone's problems. But at least they're comforting."
    "The very feeling I've been missing for the last few years - affirming me that I'm not quite lost to humanity yet."
    "While I feel tangibly stronger, basking dear one on my chest."
    me "And you're just saying that?!"
    show un serious pioneer close with dspr
    un "I only spoke for myself."
    un "I am sure of myself."
    me "But..."
    un "I'm sorry if I was wrong about you. {w}Let go."
    show un serious pioneer with dissolve
    "She broke free of my arms."
    me "No... It's just."
    show un shy pioneer with dspr
    un "What?"
    th "I'm without you, but... Uh... That's how it is - dead, deaf and not looking for an answer anymore. And I keep looking through the dirty window into the spring, where you were not and are not there."
    "I don't know what's harder, apologizing or confessing."
    "And how do you do that in the face of a wooden, bony Adam's apple, a parched larynx, your lungs unwilling to take in even a little air?"
    me "The counselor was not mistaken."
    "In an impossibly steady voice I uttered."
    me "Not in a single word."
    play sound sfx_7dl["eat_horn"] fadein 1
    "My torment was interrupted by the horn call."
    "But neither I nor she moved."
    "On the contrary, she slowly turned in my direction."
    show un serious pioneer with dspr
    "And after finally establishing eye contact - heavy as can be, but I'm not going to put my eyes down! - she blinked away the accumulated moisture and said:"
    un "Say that again."
    me "I said that... It-tt'-ss- t-true..."
    "Stammering like a drunk, I obediently repeated."
    me "E-every word."
    show blink
    "And closed my eyes."
    "Only to be immediately deafened in my left ear by the battle cry of some Mohawks and a most pleasant weight hanging around my neck."
    scene bg int_editorial_day_7dl
    show un smile2 pioneer close
    show unblink
    un "I knew it! I didn't doubt for a second!"
    "She babbled incoherently, covering my cheeks, my eyes, my lips with kisses."
    un "I knew from day one!"
    me "A little calmer..."
    "Trying to catch my breath, I smiled."
    th "Give me my nonchalance... I demand... I have the right to be a wreck."
    me "Let's go see what the kids are having for lunch today?"
    show un laugh pioneer close with dspr
    un "Why don't we lock the door and have some fun?"
    "Lena shot her eyes in the direction of the entrance."
    me "You're doing it again, aren't you?"
    show un surprise pioneer close with dspr
    un "What's wrong? You've gone soft - chin up!"
    me "You keep this up and we both risk doing something stupid that you'll no doubt regret."
    show un laugh pioneer close with dspr
    un "Next to you there is no foolishness that I will regret - don't you understand?"
    un "We're going to do it together!"
    me "..."
    th "You don't know what you're asking for, honey..."
    dreamgirl "Who knows. Maybe she's happy with the prospect of watching your back while you sit in your pants in the backyard."
    th "That's not going to happen. She and I..."
    dreamgirl "Five years later. She's on the couch with a tablet, you're in the chair in front of the monitor."
    me "Let's go already."
    "With a shrug, I called out."
    show un smile2 pioneer close with dspr
    "Lena smiled mischievously, took me under the arm, and kissed me on the cheek."
    show un laugh pioneer close with dspr
    un "Here we go!"
    stop sound fadeout 3
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day5_un_7dl_np:
    scene bg ext_beach_day with dissolve
    play ambience ambience_lake_shore_day fadein 3
    play music music_list["everyday_theme"] fadein 3
    "Despite the morning rain, the sun that firmly occupied the sky had managed to warm and dry the top layer of sand, so here and there you could see the pioneers stretched out on their bathing towels."
    "The industrious Lena brought a towel for me, too - we changed in the stalls and took a place in the lurch."
    if herc or loki:
        "It was lazy to walk to the place where we bathed yesterday - and the understanding girl got everything perfectly well without any extra words."
    else:
        "The place where I'd been floundering my feet not long ago seemed pretty good for swimming."
        "But it was too far away."
    show un smile swim with dissolve
    un "Semyon - you're a terrible slacker, you know that?"
    "I shrugged."
    me "That's something I've never considered a vice."
    me "Man is as lazy as any other creature that confronts entropy with its internal reserves of energy."
    show un smile2 swim with dspr
    un "Chatterbox..."
    "She laughed and, spreading out a towel, pointed at it invitingly."
    me "Thank you! And you?"
    un "And I'm going to swim now, and then you!"
    me "I don't feel like it... Maybe..."
    "It was lazy to swim - maybe when the sun gets a little more..."
    show un angry swim with dspr
    un "No «Maybe»!"
    "Girl got angry."
    un "When was the last time you washed your face?"
    un "I'm not going to kiss you that dirty, you know that!"
    "Now that was a serious threat!"
    "So I sighed and admitted defeat."
    me "Never mind, goldfish. I'll take all the baths you want."
    show un smile swim with dspr
    un "Good! {w}Don't be bored, I won't be long!"
    hide un
    with dissolve
    "The sight of her hips swaying excitedly, and the whole figure in general... exciting."
    th "I wonder what «bored» we could be talking about here?"
    "I set my back to the sun."
    th "Here?"
    dreamgirl "I'm always here, dear. What did you want?"
    th "It's kind of weird, don't you think? The camp, the girls with the figures of photomodels, but the mannerisms of Eve, with Lilith always in front of them...{w} You, again."
    dreamgirl "What's wrong with me?"
    if dr:
        th "Except that you've gone from «belly consciousness» with a sociable level of premonitions and reflexes to... turned to... what's your gender?"
        dreamgirl "As you feel more comfortable."
        th "In general, into an interlocutor, whole, reasonable one."
    th "I've read that it happens in split personalities - I remember about Milligan, too."
    dreamgirl "You won't get it: I don't claim control of the body."
    th "One way or another. You, camp, girls, no questions asked..."
    th "I'm behaving in an obscenely wrong way - not flailing about, not asking bad questions, not trying to find out what's going on here in the first place."
    dreamgirl "Enjoying life. And that's the right thing to do."
    dreamgirl "Or don't you like «Sovyonok»?"
    dreamgirl "It's like in the female police training program - if rape can't be avoided, relax and try to enjoy. {w}You're surrounded by warmth and care, you got yourself a girl - why else do you want, you ungrateful mug?"
    th "I don't mind."
    th "They even gave me some answers... Though I didn't ask any questions."
    if alt_day4_me_neu_transit == '':
        dreamgirl "I'm going to quote a very smart girl to you:"
        dreamgirl "Let's act like this is a dream, too."
    dreamgirl "Open your heart to the sky, make a wish - what do you want more than anything else?"
    dreamgirl "Compare it to what it was before camp... If at all."
    th "Right now, my biggest wish is that summer never ends. It's very scary that along with summer Lena will end too."
    dreamgirl "You've only known her for five days. {w}You don't know her at all."
    th "It doesn't matter. In order to know a person, you have to live a lifetime with them - which I agree to live with her."
    dreamgirl "What about old wishes? Still want a Sennheiser soundset? Or a 27-inch monitor - as if 24 wasn't enough?"
    th "You know... No. I don't want."
    th "It would distract me from the really important part of life."
    show un normal swim with dspr
    "The path of sunlight was blocked by a small, frail silhouette that was slowly becoming familiar."
    th "From her."
    show un smile swim with dspr
    un "G-g-give t-t-towel!"
    "She bared her teeth."
    me "I'm fine, thank you, I missed you too."
    "Who had any doubts that I didn't have it all figured out?"
    "I got to my feet and threw a towel over the girl's shoulders, noting in passing how great her wet skin looked with the huge goosebumps and the unhappy eyes she was looking at me."
    "And, with a sigh, I began to rub her."
    me "Is the water cool?"
    show un normal swim with dspr
    un "No. The water is warm."
    "For some reason I was reminded of a scene from Besson's Netflix... Automatic washing, huge eyes, a towel over her shoulders and orange hair - circumstances of general breath and a few centimeters to her lips."
    "True, my Leeloo didn't wear orange hair, but what did it matter."
    "The world froze..."
    with fade2
    "When she opened her eyes, she was no longer trembling - obviously, she had dried out in an instant."
    show un smile swim with dspr
    un "And HE called me crazy."
    "She smiled, but her eyes looked reproachful."
    un "Go swim, tempter."
    "Yeah, well, you shouldn't have done that on the beach. {w}Thank Random, no one noticed anything."
    "With a smile, I hurried to the water."
    scene bg ext_underwater_7dl with dissolve
    play music music_list["she_is_kind"] fadein 3
    play sound sfx_water_emerge
    "The water took me in its cool embrace. Twenty-three to twenty-four degrees, a heavenly temperature."
    "It still took my breath away, though."
    "Not the best substitute for a normal wash, of course, but Lena was right: the beast I'd turned into in the last few days, water procedures were strictly mandatory."
    "So I swam to a freer place and washed the dirt out of my hair and off my body where I could reach it, if possible."
    scene bg ext_beach_day
    with dissolve
    play ambience ambience_lake_shore_day fadein 3
    show un smile swim with dspr
    un "See, a completely different person now."
    th "I remember she didn't refuse a kiss at all."
    "Instead of answering, I stretched out on the towel beside her, touching her shoulder."
    "Probably should have been worried. Twitching even - looking for answers or something like that."
    "But as with the answers falling into my hands completely on their own, I let things slide."
    "It's more likely that something will work itself out. When playing plot games, you can never show an interest in events, and Fate will do its own thing to make us run into each other on the stairs."
    "Or ended up on opposite sides of the same wall."
    "In the same Skype conference."
    "Same bed."
    un "What are you thinking about?"
    "Without opening her eyes, Lena asked."
    me "About laziness."
    show un smile swim with dspr
    un "What's there to think about? You're a bum, and that says it all."
    me "Well..."
    "I didn't want to get into demagoguery, but I did have one irresistible argument for that."
    me "I see laziness as a religious aspect."
    un "How's that?"
    me "Buddhism. The Gautama there distinguished three kinds of laziness, and my laziness is of the first kind - the same kind of bumming that I'd love to do with you."
    me "The most harmless kind, by the way."
    un "So just because you're lazy to get up and do something, you consider it harmless?"
    me "Compared to the other two, the laziness of thinking, the so-called negative thinking, and the laziness of admitting yourself."
    un "I would look at a person who is lazy to think."
    me "Most people I know go through just the second part - they whine about how things don't work out in their lives because they're bad, or mean, or the environment is to blame, or whatever."
    un "Are you referring to me now?"
    if alt_day4_me_neu_transit == '':
        me "No. More like myself and a number of online acquaintances like me."
        un "Who's that?"
        "After figuring out how to answer without going into technical details, I tried to make my answer as honest as possible:"
        me "Pen pals of sorts. They're not hopeless, because if they find someone to kick them, or if they get wise to themselves... or at least get married... Let's say, all is not yet lost for them."
    else:
        me "No way!"
        me "You're the most nice and hardworking here!"
        show un smile2 swim with dspr
        un "Okay, flatterer!"
    un "Okay, that's been dealt with. What about laziness of admitting?"
    me "The most dangerous pest. I see it in you, in myself, in Olga Dmitrievna... A person who is afraid of themselves, who does not value their own life and the lives of those around."
    me "We are afraid to look inside ourselves and to see the reflection at the bottom of the well. And that means a lack of margin of safety. Potential suicides, job burners, heart attackers, hysterics."
    un "Scary thing, this religion of yours."
    if alt_day4_me_neu_transit == '':
        extend " It's a good we don't have it here."
    me "It's only scary because it doesn't hesitate to call a person who's afraid a coward."
    un "But I get your point. Indeed, compared to the rest of the kind, you are relatively harmless."
    show un smile swim with dspr
    un "Although I'd rather you didn't get lazy and take me out."
    "The girl hints at a walk. Makes sense. What else is there to do at camp but walk."
    un "All right, get lazy, then."
    "Sand sprinkled on my chest and I opened my eyes in surprise."
    me "What are you doing?"
    show un smile swim with dspr
    un "Don't you see? Burying you in the sand!"
    me "What's that for?"
    show un sad swim with dspr
    un "Stupid.{w} You're lazy anyway, so lie back and keep warm."
    "She's taken up earthworks in earnest."
    me "Aha-aha."
    "I muttered, watching my feet disappear under the sand little by little."
    $renpy.notify('Name «Lena» sounds almost like «Lazy» in Russian.')
    me "She was a very lazy girl. Her name was Leeeeeena."
    show un smile swim with dspr
    un "Keep talking, and I'll fill your mouth, too!"
    me "Okay, Okya, I'll shut up."
    "If a girl wants to play, who am I to argue?"
    with fade2
    stop ambience fadeout 2
    "The touch of the hot sand was like a relaxing massage, and I didn't notice how I dozed off."
    scene bg black
    with fade
    "Deeply-deep."
    scene bg ext_beach_day with dissolve
    show un smile swim with dspr
    if loki and (persistent.un_7dl_good_ussr or persistent.un_7dl_good_rf):
        "And I woke up only when Lena sat down on top of the resulting mummy."
        un "You fell asleep again!"
        me "That's it, the digging is over?"
        "In a hoarse, sleepy voice I inquired."
        un "Yes."
        "Looking around, she winked at me."
        un "Now we have to dig you out."
        "I could have easily stood up - the layer of sand was small - but I decided to play along with the girl jumping with enthusiasm."
        "And it wasn't until I felt the touch through that sand that I realized - where she was even sitting!"
        "And - yes, I totally got it right - the digging started in that exact area!"
        "There was no use in resisting, fighting, or in any way trying to stop the girl."
        dreamgirl "And we don't really want to, what's the harm in it."
        "And so I tried to relax and switched to watching the beach - the pioneers were busy with another game, started by Olga Dmitrievna, and did not pay attention to us."
        me "I'd better get in the shower."
        "Not that it necessarily had to be said, but since I volunteered to play the role of the innocent victim of molestation..."
        un "Absolutely right!"
        "Even Slavya could envy the enthusiasm of her nod."
        un "There you can get under a cold shower and not think about what's been nipping at my side this morning."
        "I just laughed."
        un "Also, there are no witnesses, and we can go a bit further..."
        "Dreamily she said."
        me "I don't mind, of course, but don't you think the idea of undressing me is a little... Hmm... intrusive?"
        un "Not at all. I'm an artist. Nature is important to me."
        dreamgirl "Nature? A cavernous body is a nature?"
        "The inner voice asked, and I could barely contain my chuckle as my swim trunks appeared from under the sand, and Lena slowly pulled them down."
        me "Right, let's show the world what's in my swim trunks!"
        un "Don't be afraid, no one's looking."
        "Her actions elicited a healthy and understandable reaction, so when the sun and sky finally revealed where the horny artist was aiming, I was about halfway to full alert."
        un "There you are."
        "Picturing the tapering shark, she ran her palm over the skin of the groin, gripping both thighs and the very pelvic bones that are called «handrails» in layman's circles - you know for which pose."
        "Finally, we got to the center of the action."
        show un shy swim with dspr
        un "Cold."
        me "What did you expect? I just got out of the water."
        "In an effort to hide my excitement, I spoke in a deliberately carefree tone."
        un "But..."
        "I never found out what «but» was, and I didn't care - we'd finally had enough foreplay with plants, groin, testicles, and who knows what else."
        "Lena's fingers were on the hero of the occasion."
        "That very nature."
        "And, squeezing lightly, they moved upwards."
        "I forgot how to breathe and concentrated on the sensation."
        un "A man's desire is a bone twenty-five centimeters long..."
        "Smiling, Lena quoted god-lnows who. She took that very «bone» down and, releasing it, laughed softly at the way it bounced elastically back to its original heaving state."
        me "It's not a bone..."
        un "I know. I studied anatomy."
        un "In terms of hardness, though -"
        "She clenched the head with her fist and pulled it up, and I realized I was balancing on the edge."
        un "It can even compete."
        "I rolled my eyes, anticipating the echoes of an impending orgasm."
        dreamgirl "And that's after two movements?! You should get married, sir! Also, I'd give that «bone» a 5/7."
        "And that's why I reacted to the rubber band of my swim trunks slamming on my belly in the only right way - with a growl."
        me "Lena, I'm going to..."
        show un smile swim with dspr
        un "What? Kill? Beat me up? Take to the bushes and do something obscene there?"
        "She tilted her head sideways."
        un "The counselor's looking at us, and only my thigh is very fortunate to hide what state you're in."
        un "And if she comes in here now..."
        "Well, that's something I've learned to deal with."
        "Squeeze the sphincter where necessary, redirect the flow of blood - and, after counting twenty seconds on a new round of blood supply, summarize that the erection is defeated."
        show un smile swim with dspr
        un "No..."
        "She poked her finger in the pecker."
        un "He's not nearly as funny that way. Put it back the way it was!"
        "The positions won from the libido have been shatteringly lost again."
        th "I wonder if she realizes that it's only my goodwill that keeps me from doing a stupid thing or two."
        dreamgirl "Judging by the buttery eyes, more than that."
        me "That's right, and let's go through the camp."
        "Shoving her off me and trying to breathe evenly, I replied."
        me "You, with the eyes of a March cat, and me with a hanging gun."
        show un sad swim with dspr
        un "Like something bad."
        me "Like something good!"
        "In tone with her, I replied."
        un "Where are you going, can you tell me?"
        play sound sfx_7dl["eat_horn"] fadein 1
        "A horn sounded from the camp."
        me "Any way."
        un "Let's..."
        "Her eyes lit up."
        un "We're not going anywhere! Let everybody else go, and we'll go to our beach, and there..."
        "She bit her lip and shot her eyes."
        me "Forget it, I said."
        th "Damn butterflies in the belly. They read their Mitchells and then think everything will be easy and airy and without consequences."
        stop music fadeout 5
        me "I don't know what your knowledge of the subject is, but I assure you there are a lot of negatives."
        me "So let's get together now and go check out what they're poisoning us with for lunch, okay?"
        "She reluctantly nodded."
        "I may have unreservedly ceded the decision to her on some matters, but here I've managed to hold my ground so far."
        me "Just don't think I don't like you. I like you, and I like you a lot."
        me "It's just... Not the time yet."
        "After hesitating, Lena nodded."
        un "Whatever you say. Let's go change... hero-lover."
        stop ambience fadeout 5
    else:
        "And I woke up only when Lena sat down on top of the resulting mummy."
        un "You fell asleep again!"
        me "That's it, the digging is over?"
        "In a hoarse, sleepy voice I inquired."
        un "Yes."
        "Looking around, she winked at me."
        un "Now we have to dig you out."
        "I could have easily stood up - the layer of sand was small - but I decided to play along with the girl jumping with enthusiasm."
        "I really didn't like the look in her eyes."
        "So I looked up at Miku with infinite gratitude."
        "I don't need any more public harassment from an underage pioneer girl!"
        show mi smile swim at cleft with dspr
        show un sad swim at cright with moveinleft
        mi "Hello, neighbor! Who's that you're sitting on?"
        "The carefree Japanese girl looked over Lena's blushing shoulder and smiled at me affably."
        mi "Hi, Semochka! Or should I say Senechka?"
        "I blushed."
        me "I'm surprised you asked. I prefer the name Semyon."
        mi "I read that you, in the Union, like diminutive forms of names like Lenochka and Senechka."
        show mi happy swim with dspr
        mi "Listen to how it sounds! It's so sweet!"
        "She closed her eyes in pleasure."
        show mi normal swim with dspr
        "And then, with a moment's hesitation, opened it."
        mi "Oh, I completely forgot. Lena, the counselor called you for something. Will you come over? I'll keep an eye on your boy, so he doesn't get stolen."
        me "You don't have to guard me!"
        "I resented it, but made no attempt to free myself."
        show un normal swim with dspr
        un "Then I'll go to the counselor, and you try not to get too rowdy here..."
        show un smile swim with dspr
        extend " Senechka!"
        pause(3)
        hide un with moveoutright
        "Like everyone else in this camp, Lena moved exclusively by running."
        show mi normal swim at center with dspr
        mi "Here we are alone..."
        "I didn't really like the sound of that, but I didn't have to be picky about the situation."
        "So I patiently tolerated the fact that a rolled up towel fell on my chest, and Miku, laying perpendicular to me with her head on that towel, used me as a pillow."
        "I just grimaced and asked to remove the strand of hair that had come loose from her ponytail."
        mi "Lena is so secretive..."
        "After turning around and making herself more comfortable, Miku began."
        mi "Never tells me anything. Well, that's right: what's a Japanese silly girl to tell - she won't understand anything anyway."
        mi "I feel like she's not six months older than me, but a year or more. It's like an arrogant age gap."
        mi "But I can see she's thawing out, her eyes are lively and healthy, and she's getting warmer colors in her pictures."
        mi "And even at night, when I was talking in my sleep, she didn't bark as usual, but shook my shoulder and told me to roll over on my side."
        me "And I don't know her any different."
        show mi upset swim with dspr
        mi "She was an acutely asocial person - in my country they call her..."
        me "Hikikomori. I know."
        show mi surprise swim with dspr
        mi "How do you know?"
        me "That's how, the earth is full of rumors. Go on - what did you find out about Lena?"
        mi "It's obvious - Lena's got someone."
        mi "I really thought it was Electronik. But as it turns out, he has a soft spot for our librarian. And Shurik... Well, you know."
        mi "I couldn't even think of you! Such a surprise..."
        th "Even the goddamn Japanese girl denies me a chance, putting Electronik and Shurik above. So much for that."
        "She patted the sand at my belly level."
        mi "No matter what, I'm very worried about her - she's like a sister to me practically."
        mi "So, Senechka. In addition to song and dance, I studied a number of other disciplines. {w}And if you hurt Lenochka..."
        me "What a beauty... In two days I've already been intimidated twice."
        me "Maybe Lenochka isn't such an asocial?"
        mi "I don't know. I've said everything."
        show mi smile swim at cright
        show un normal swim at cleft
        with dissolve
        "She rose easily from me and smiled at Lena, who was approaching with a most angry look."
        mi "So? What did she want?"
        un "Nothing! You tricked me!"
        mi "But I definitely heard... She asked someone to send Lena, so I sent her - as a friend!"
        un "She didn't ask for anything."
        mi "Yeah? So, my bad? I'm sorry, please."
        hide mi with dissolve
        "After giving us both a quick smile, the Japanese girl retreated."
        play sound sfx_7dl["eat_horn"] fadein 1
        "And from the direction of the camp came the familiar horn sound that spared us all unnecessary questions."
        me "Let's go lunching?"
        show un normal swim at center with dspr
        un "Yea, let's go. And I'll talk to Miku later, she's got a mind to chase me around for nothing!"
        un "Why are you lying there? Come on, get up!"
        "Reaching out to me, the girl easily lifted both me and the layer of sand."
        un "Let's go change."
    stop music fadeout 3
    stop sound fadeout 4
    stop ambience fadeout 6
    with fade2
    return

label alt_day5_un_7dl_launch:
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 5
    play music music_list["i_want_to_play"] fadein 3
    "I pretended to be a gallant gentleman and technically brushed Dvachevskaya aside, letting Lena through the open door."
    "The good and the curse of regime institutions is that they accustom you to some little things - in a matter of days, by the way! - and in the future it's hard for you to do without them."
    "You no longer regret getting up early in the morning - since you know you can always count on your rightful two hours of sleep in the afternoon."
    "And you react to sleeping in the afternoon in the sanest way possible, without a sore head and stiff limbs - you're used to it. {w}And some tasty muffin waiting in the canteen somehow lifts my spirits."
    "I had to play the gentleman to the end.{w} Miku, Ulyana, and Alisa, a little shocked by my behavior, rushed through the open door."
    "Sighing, I went in last, second only to Electronik. {w}But he seems to have settled in the infirmary."
    th "He must have found a box of «headache remedies» bequeathed by Violeta Zernovna!"
    show mt normal pioneer at center with dissolve
    mt "Semyon, a word!"
    "A counselor called out."
    "She looked surprisingly thoughtful, so I stopped without asking any questions."
    show mt sad pioneer with dspr
    if dr and ('nwsppr' in list_clubs_7dl):
        mt "How is the proofreading of the article going?"
        me "How are you even aware of the article?"
        show mt surprise pioneer with dspr
        mt "That's my assignment, isn't it?"
        "The squad leader was surprised."
        me "Yes, well, we're moving... Why?"
        show mt sad pioneer with dspr
        mt "That's all right. I got a magpie on my tail telling me that you weren't writing an article in the library, but..."
        me "I'm going to yank that magpie's red hair out."
        mt "So it's true?"
        me "What exactly?"
        mt "That you... well... in the library."
        "I could have sworn that the counselor was about to start picking at the floor with her sandal or making some other pointless gesture that is inherent in a person who feels uncomfortable."
        me "Are you interested for personal or business reasons?"
        show mt angry pioneer with dspr
        mt "Stop clowning around!"
        me "Okay, okay."
        "When she started yelling like that, she got wildly good - and I'd piss her off five times a day if I was free."
        "And the extra attention she was drawing to herself was also unwelcome."
        me "Yes, that's how it was."
        show mt rage pioneer with dspr
        mt "What did I tell you this morning?"
        me "We locked ourselves in the library, read an article, then she told me about her sister, we hugged, maybe there was even a kiss - I don't remember exactly."
        me "Big crime, yes. But we locked ourselves in thoroughly and were there during quiet time."
        me "Are you done?"
        mt "You know that after lunch..."
        me "I keep working on the article? Yes, I'm aware of that, thank you."
    else:
        mt "So, Semyon, what was that on the beach?"
        me "What exactly?"
        "I knew I shouldn't have let Lena do what she was doing!"
        if loki and (persistent.un_7dl_good_ussr or persistent.un_7dl_good_rf):
            "For «hand work» in public, in a children's camp... We'll be very lucky if we just get settled into different facilities!"
        else:
            "The whole thing smelled bad from the beginning, both with the burying in the sand and the swimming."
        mt "What did you do on the beach there?"
        if loki and (persistent.un_7dl_good_ussr or persistent.un_7dl_good_rf):
            dreamgirl "What did you do, what did you do. If it weren't for the general retardedness, we'd have made much more!"
        me "Yeah, you look at me accusingly and say you know everything, and I, tormented by my conscience, spill it all out."
        "I shook my head."
        me "It doesn't work with me, Olga Dmitrievna. It hasn't worked for five years now."
        th "After all, in order to repent there must be at least the rudiments of conscience. And I left it in my other pants."
        mt "You... You weren't with the squad!"
        th "A terrible sin. {w}We were swimming, too."
        me "It was quiet time, so it wasn't an event."
        mt "And sitting separately! Do you want everyone to whisper about you?"
        me "What is it?"
        "The desire to show my tongue to the over-active counselor was unbearable, and it cost me a lot of trouble to suppress it."
        me "A dog barks and the wind blows. Have you heard the saying?"
        me "We don't set you up, we don't do everything on public..."
        dreamgirl "Really?"
        "A picture flashed before my eyes - huge green eyes half a face, dark hair, and giant goosebumps under a big gray-brown towel."
        me "Anyway, no one saw us for sure."
        mt "Okay, I'm sick of this. I had an assignment for each of you for after lunch, but you seem to make instant martyrs of yourselves."
        mt "So get the hell out of my sight and into the woods, so no one can see you."
        me "You're kicking me out of the camp?"
        "Here it seemed to me that it would not be unnecessary to clarify."
        show mt smile pioneer with dspr
        mt "What? No. {w}You'll come to Slavya: we'll have to get the fire pit ready for the evening hike."
        mt "Yes, yes, I won't let you two go. Otherwise I know what will happen: a total misunderstanding and no preparation."
        dreamgirl "And we... And we... We'll put her as a third then!"
        me "You shouldn't... You should trust people."
        mt "And I do. That's why I won't make you drink bromine before you go. {w}I won't keep you any longer."
        "The audience ended, and I sat down next to Lena."
    hide mt with dissolve
    show un smile pioneer with dissolve
    un "What were you talking about?"
    me "She doesn't like us spending too much time together, you see."
    show un laugh pioneer with dspr
    un "Jealous, no less."
    "The girl giggled."
    un "Probably wants you in her cabin more."
    me "That's right."
    show un smile pioneer with dspr
    me "Thank you for taking lunch for me - I'm too lazy to stand in line."
    if dr and ('nwsppr' in list_clubs_7dl):
        me "After lunch, we stomp back to the library. And woe betide whoever this time decides to be distracted from why we're going there!"
        show un smile3 pioneer with dspr
        un "Why are we going there, exactly?"
        "Innocently, Lena flapped her eyelashes."
        me "To work!"
        show un laugh pioneer with dspr
        "I barked, eliciting a fit of laughter from the girl. {w}At that moment, even if things didn't work out with her, I realized how close she was to me."
        me "No, if you don't want to, we don't have to work. Who will be forced to write it then? Zhenya? Electronik?"
        show un sad pioneer with dspr
        un "What? Those two? No. I've seen their handwriting - like a chicken scratch."
        un "I guess we're going to have to work really hard. Just don't distract me, okay?"
        me "I will."
        "The promise came easy."
        un "Semyon! I mean it!"
        me "Me too. See how serious I am!"
        un "You're a clown! Don't know what I found in you."
        me "I'm not boring!"
        "I am selfishly pounding my chest."
        un "Only."
        "She finished the rest of the muffin and got up."
        show un normal pioneer with dspr
        un "Catch up."
        me "Jawohl."
    else:
        "After quickly finishing our buns, we went out on the porch"
        stop ambience fadeout 3
        scene bg ext_dining_hall_near_day
        show sl normal pioneer
        with dissolve
        play ambience ambience_camp_center_day fadein 3
        extend ", where Slavya was already waiting."
        sl "Are you ready to rehearse the hike?"
        me "If I say no, will it make a difference?"
        "I asked dejectedly."
        show sl smile pioneer with dspr
        sl "Of course it will! Then we'll sit on the bench and wait for you to be ready!"
        show un smile pioneer at left with dspr
        un "Come on, Semyon! A walk is not so scary!"
        sl "You're right. Through the woods, through the pine trees! What an air!"
        me "You act as if you were instructed by the party to sell me a batch of this air."
        dreamgirl "Heheh, pun intended!"
        me "What do you want me to do?"
        show sl normal pioneer with dspr
        sl "We need firewood - we'll get it at the firehouse at five per brother."
        sl "Garbage bags - I'll give them."
        sl "And some dry firewood - the kind that might be in the surrounding woods is wet because of the rain."
        me "So I'll get the firewood as the heaviest loader. You deal with the kindling and the bags."
        sl "All right!"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day5_un_7dl_library:
    scene bg ext_library_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    play music music_list["timid_girl"] fadein 3
    "Even though I made terrible sacrifices - I ate a quick bun and almost choked on it - jumped out ten seconds after Lena, I didn't catch up with her until just outside the library."
    "And it was worth it to run like that..."
    "She opened the door and slammed it shut almost under my nose."
    play sound sfx_open_door_clubs_2
    stop ambience fadeout 3
    scene bg int_library_day with dissolve
    play ambience ambience_library_day fadein 3
    "And when I got mad enough to go inside and was about to curse, something fell right into my hands and grabbed me, kissing me on the lips."
    "Lena."
    th "Geez!"
    "I exhaled a few minutes later, still pulling away from her as a result."
    me "You didn't look at me when you fell! What if it hadn't been me?"
    show un grin pioneer with dspr
    un "So someone else would have had the sweetness."
    "With a hint of taking a step even closer, she smiled."
    me "Sweet?"
    un "Yes!"
    "Her voice dropped sharply a couple of tones - into that same velvet gamut that makes any healthy guy's diaphragm twitch."
    un "And if you'd been a little faster, you'd have had time to notice what..."
    "She took another step, forcing me back toward the door, resting my shoulder blades against the painted plywood."
    un "But you didn't notice."
    show un sad pioneer with dspr
    un "You didn't seem to want to."
    me "Why should I notice?"
    un "Nothing. Let's go write an article."
    "She looked away for some reason."
    "And I, trying to figure out what was wrong, silently analyzed our behavior for possible mistakes - and didn't find any!"
    me "Lena... What's wrong?"
    un "Nothing."
    me "Are you sure? Then why are you acting like I let you down?"
    un "Let down? No..."
    show un shy pioneer with dspr
    un "Sorry..."
    "She flinched and stared at the floor."
    $renpy.notify("A quote from L. N. Tolstoy's novel «Anna Karenina».")
    th "It's all mixed up in the Oblonsky household..."
    me "I'm sorry I'm not a panacea or a prophet."
    me "And some stupidity can be forgiven me now..."
    show un surprise pioneer with dspr
    un "Why?"
    me "Because I'm young. Young and in love. And whoever is without sin, let him be the first to throw a stone at me."
    un "And where did you learn to say such silly things so smoothly..."
    "What is the proper response in such cases?"
    me "Can I go and work now?"
    show un normal pioneer with dspr
    un "Can't wait to get rid of the girl already?"
    "She slowly, reluctantly lifted her eyelids."
    "There was only a grain of humor in her joke, but I only snorted."
    me "Nah, I won't, I'll sit next to her. I can poke you in the side every five minutes to remind you of myself."
    un "Deal."
    with fade2
    play sound sfx_open_door_clubs_2
    pause(1)
    scene bg int_editorial_day_7dl with dissolve
    "The editing room was just as we'd left it - a half-dark, cool room, so comfortable for hiding from the scorching sun, apparently determined to get back at me for the morning."
    "Lena immediately sat down in the chief editor's chair and pulled up two pieces of paper and took my work in her hands, running her eyes over it once more."
    show un normal pioneer with dissolve
    un "You write well, by the way."
    "She praised."
    un "Do you want to try your hand at journalism?"
    un "Or writing..."
    "She tilted her head sideways and studied me thoughtfully."
    me "What?"
    show un smile pioneer with dspr
    if alt_day1_un == 2:
        un "And I listened to you - I took Strugatsky."
        un "And there the writer was... In «The Ugly Swans»... I read, and I saw - you."
        me "As helpless in the face of the unbelievable?"
        un "No. The same - in a white prickly sweater with a collar under the chin, suede inserts on the elbows - not of this world."
    else:
        un "Sometimes an image comes to mind."
    if loki:
        un "It's like you've got some weird thing in front of you, like the ones Miku has at the club."
        un "And you look at it so intently, but you pay no attention to me."
    elif herc:
        un "It's like you're walking through the winter streets, and it's like you can feel me next to you."
        un "You talk to me, you turn to me."
        un "And I am not there."
    else:
        un "You're sitting in a semi-darkened room with what you call a monitor in front of you, tapping the keys very fast."
        un "And it would probably sound annoying if it weren't for a certain, barely perceptible rhythm of thought beats slipping between tapping the space bar and a new drum line."
    un "What do you do for a living?"
    me "What do you mean?"
    un "Well..."
    show un grin pioneer with dspr
    un "I'm curious to know what my young man does.{w} What he lives, what he breathes."
    stop music fadeout 8
    if loki:
        un "For some reason I think you could be very good friends with Miku on the basis of music."
        un "And with Alisa."
    elif herc:
        un "There's something about you."
        un "I don't know! Like you could be a pretty good teacher."
        me "Holy crap!"
        show us laugh pioneer with dspr
    else:
        un "There's just something writerly about you. I can't picture you on a soccer field, kicking a ball around with a dozen boys."
        un "And I can hardly picture you on the factory floor either. That makes you an intellectual worker."
        th "Yes, where I've worked, you need more intelligence than a monkey could manage."
    me "Are you really interested? It's just that my work is kind of boring, and I don't know how to talk about it cheerfully."
    show un normal pioneer with dspr
    un "Well, let me decide that. Tell me while I'm rewriting here."
    play music music_list["afterword"] fadein 3
    me "Well."
    "I sighed."
    me "Then listen."
    if loki:
        "I don't know how Lena would feel about me teaching music."
        "That I'm an unformed musician myself."
        "The events - the plot of the last decade - scratched thinly in my memory."
        me "I once wanted to be a musician."
        show un serious pioneer with dspr
        un "And what prevented you?"
        "Oh, almost everything."
        th "I'm afraid you wouldn't appreciate it if I started naming names and events."
        me "Stuff..."
        "Evasively I replied."
        me "Bad luck, to make a long story short."
        show un sad pioneer with dspr
        un "I don't insist."
        "Lena looked me in the eyes."
        un "If you're uncomfortable about the subject, don't tell me."
        th "Very uncomfortable, to be honest."
        "But to refuse to talk now - then why start everything?"
        show un normal pioneer with dspr
        un "I'll understand."
        me "It's not that it's unpleasant."
        un "Can you think of any people you would definitely blame for what happened?"
        th "That's the thing, the first person to blame on such a list would have to be myself."
        me "I guess I could."
        un "Then don't torture yourself. Assign someone to blame and get on with your life!"
    elif herc:
        "Sure, so far I've guarded cigarettes and other crap, but my life wasn't limited to that alone."
        "There was a life before the store."
        "And beyond it."
        "Although how do you explain that to a girl who hasn't even seen a computer yet?"
        me "It's boring."
        me "Last time I worked as a watchman."
        "I reluctantly admitted."
        show un smile pioneer with dspr
        un "You - and a watchman?"
        "Lena had fun."
        th "Yeah, it's a real pain in the ass."
        me "In general."
        me "And in addition to my main job, I also help my acquaintances with small repairs of household appliances and computer settings."
        th "It's kind of boring, yeah."
        dreamgirl "What did you think! In order to brag to a girl about your work, you have to find one first."
        un "Computers?"
        me "Not everyone is good at figuring out where to click and what to do to make the shaitan machine work humanly."
        me "So when things get really sad, people call me for help."
        show un serious pioneer with dspr
        "Lena nodded gravely."
        un "Well, there you go. You say it's boring."
        "She went back to writing."
        un "And there's a lot to tell about you, if you really want to."
        th "But I don't feel like it."
        me "But the main occupation is watchman."
        un "I'm sure you didn't go there out of laziness."
    else:
        "Despite the fact that I worked in a newspaper, I would hardly have been able to provide a historical education for the uninitiated."
        "No, of course, I remembered Ivan Fyodorov, the First Printing House, and other milestones of publishing in Russia."
        "But the details... I'm sorry."
        me "I work for a newspaper. Or rather, in a publishing house."
        show un serious pioneer with dspr
        un "Are you a journalist?"
        "Of course. The first thing that comes to a pretty little head at the word «newspaper» is the specialty of journalism."
        th "I'm sorry, honey, but I'm a lot duller than even the latest greyhound scribbler."
        me "No. I'm not in the business of finding content, if that's what you mean. I'm in the business of shaping it."
        me "What I do is called design, layout, and prepress."
        th "I hope it's not too abstruse or too... hmm... Anyway, I don't want to look like a peacock at all."
        dreamgirl "Okay, let's keep it simple. We do the arranging, repainting, and fitting. Is that more to your liking?"
        un "Design?"
        me "I sit down at the computer with a number of disparate materials in hand and have to produce a print-ready file on the way out."
        th "And here the look becomes disappointed, the nose wrinkles and a cheeky «ew» is heard..."
        "But once again Lena surprised me."
        show un smile pioneer with dspr
        un "How interesting!"
        "She even pulled away from her writing and looked up, letting me know she wasn't mocking."
        un "So you're responsible for all those headlines, the pictures in the text, and the general appearance of the paper?"
        th "It's the first time I've ever met a person who's interested in such things..."
        me "It certainly looks different nowadays: it's a flowing business..."
        un "And what's with the scattered materials? Articles?"
    "I nodded.."
    if alt_day4_me_neu_transit == 'un_7dl':
        un "Really, I didn't understand how you managed to get through so much."
        me "Oh, I'll be sure to tell you later."
        "I promised."
        me "With all the details."
    "Outside the window, on the other side of the grove, you could see a badminton court and a piece of volleyball field - the rest was hidden behind the trees."
    "My lips parted in a smile of their own as I remembered how I lured the dragon minions out of here."
    dreamgirl "Yeah, you made a hell of a speech. At least they didn't notice you from the playground."
    th "Quiet time, who could?"
    dreamgirl "Sanich, for example?"
    show un grin pioneer with dspr
    un "Hey, on the barge, do you hear me?"
    "She waved her hand, getting my attention, and I flinched expectantly."
    me "Sorry, I was thinking. So what was I saying?"
    show un normal pioneer with dspr
    un "You were telling me - what you were thinking about."
    "Keeping a serious expression on her face, Lena replied."
    me "And honestly?"
    if herc or loki:
        show un smile pioneer with dspr
        un "You told me about how happy you were to be sitting here with me."
        me "That's right! Very happy."
    else:
        un "I was talking about materials: how you make a newspaper out of them."
        me "How I do it: I take them all and combine them into one file, comb a little text to match the style, arrange the pictures - in most cases stolen..."
        me "Like articles, though - these often end up on my desk with the same mistakes they were found on the Web."
        show un normal pioneer with dspr
        un "Doesn't anyone draw at all?"
        me "Why not... They do. Only those who draw well will never sink to the level of illustrators - they have enough to buy their own bread and caviar."
        me "And those who draw badly... In general, I have to work with those who draw «not very».{w} Wild times, wild capitalism."
        un "So you arrange the text, put the pictures. That's it?"
        "I didn't like the way it sounded - it made me want to pooh-pooh it right away. {w}But with Lena I could have been frank to the end."
        me "On the whole, yes. Nothing complicated."
        "For some reason I felt very ashamed of what I was doing - I remembered my childhood dreams, my talents..."
        "The Japanese fascinated me because they believed that every person had either a musical talent or an artistic talent."
        "That's why it was easy for me to accept that I could not and never would learn to draw."
        with fade2
        "And I turned to music. Nine years of lessons."
        play music music_7dl["beasteye"] fadein 5
        "For nothing. {w}We're warmer on a rock that's lying down. What in God's name am I doing?"
        un "You must have a lot of newspapers, if it's that easy."
        "For the umpteenth time, Lena brought me out of my self-abuse session."
        me "You have no idea how many."
        un "That's weird. We have magazines for young people, novel newspapers, different «truths», and we have no time to read them. And who reads yours?"
        me "People, who else. The Target Audience is the queen of print."
        dreamgirl "You sound as if you've already got a good substitute for your current occupation."
        th "Remember what my father used to say - you can't go into nowhere."
        dreamgirl "And that's why he once left his keys in the hallway and didn't pop up for 18 years?"
        dreamgirl "One can only go into nowhere. Otherwise it'll be tugging with memories."
        dreamgirl "Do you remember Gumilev's? Look into the eyes of the monsters. Think hard again - are you really doing what you're doing?"
        dreamgirl "You're still very young, you're not yet thirty... {w}And all paths are really open before you: you only need to take the first step on the endless road to yourself."
        dreamgirl "Just look into the eyes of yourself, the first monster, and read on their bottom the answer that answers most of life's important questions more faithfully than the proverbial Adams Forty-Two."
        dreamgirl "Is this really what you want to do for the rest of your life? Do you want to be proud of it in your old age and remember it before you die?"
        dreamgirl "And what right do {b}you{/b} have to do this with the priceless gift of life given to you by your parents? Spend it on office, epaulettes, career?"
        dreamgirl "Suicides are called sinners - and in this case you are the worst sinner. You've killed yourself alive, and turn you off from life - no one will even cry in silence."
        th "You're into existentialism... Have you read too much Sartre?"
        dreamgirl "Stand in the face of eternity, joker, and evaluate your own contribution to the eternal struggle against chaos. {w}What have you - personally - done to make this universe just a little bit brighter before you start whining that things are bad?"
        th "And what, just go into nowhere like that - with no guarantees or even hope that anything will even work out?"
        dreamgirl "Yes! Leave keys in the hallway, often only in slippers and with only what was in your pockets."
        dreamgirl "Jesus! You've been using that yourself for five days now, throwing the girl off-balance!"
        dreamgirl "Sometimes you just have to be able to go crazy at the right moment. To give up on guarantees, promises and stability - and just step into nowhere."
        show un serious pioneer with dspr
        "Losing the rest of my armor of cynicism and neglect, I rushed to the surface from the hollow, servile subconscious."
        "The whistling air sucked in through clenched teeth like an injection of painkillers into my brain, into my consciousness, into my conscience."
        me "People are all cynics, skeptics, educated, literate - but in the print media there is a flourish of conspiracy-type nonsense, in self-respecting publications horoscopes are published..."
        me "That's not to mention the flattering scandals that even the mentally retarded can't solve, the jokes and supposedly funny pictures pulled from the same Internet."
        dreamgirl "You're whining again. Unprompted and ineffectual."
        th "Touché."
        un "And you?"
        me "I'm sorry, I'm the one who pinches all those horoscopes with scandals. What can I do: I can't do anything else."
        "I remember the last order, scolding with the colorist, who was still trying to go to Chelyabinsk, to beat the local content manager for the ugly quality of the material."
        me "By the way, you wouldn't be lost on us. Looking at your cartoons, I realize that you could have lived happily in the spirit of those Kiiko, Buslovskiy and Tarasenko who make caricatures and sell them to newspapers like this one."
        un "I don't think I could do it..."
        me "I'm sure. The main thing is to be at least funny. And this..."
        "I jabbed my finger at the sheet of paper pinned to the board, where a girl with a pair of funny tails was hiding from a huge owl behind my broad back."
        stop music fadeout 5
        me "...it's good. Funny even."
        show un smile2 pioneer with dspr
        un "And you have people living like this? It's a real pleasure."
        me "As they say, get your dream job and you won't have to work for a day."
        me "I remember that you have an article for vagrancy here... But in my wild world there are certain pluses."
        un "So I'm going to sit at home and draw these cartoons and just send them out to the newspapers and make money?"
        "I didn't believe Lena."
        me "Not right away, of course. You'll have to work on your name, work with newspapers on a voluntary basis for a couple of years... But it's all temporary."
        me "In fact, there are only a handful of cartoonists with whom you can collaborate normally, thirty names maybe. I'm already getting good at identifying them by their style of drawing."
        me "And if your name comes up one day, I'm all for it."
        dreamgirl "Double for it if it's not «Tikhonova» but «Persunova»!"
        th "A little premature, don't you think?"
        "I shushed the inner voice."
        dreamgirl "What premature. We're already five days late!"
    show un smile pioneer with dspr
    un "Well..."
    "She put the scribble aside and, taking another sheet of paper, scribbled rapidly with a pencil."
    "The strokes were short, jerky, but the picture, the faces, and the context were easy to read - under Genda, adjusting the huge glasses on his nose, someone had planted dynamite."
    "And that «someone» was now crouched, eyes closed, and ears grotesquely plugged, waiting for a grandiose bang."
    me "Alisa and Ulyana blow up a monument - canvas, oil."
    show un laugh pioneer with dspr
    un "Aha. A picture with cheese. While I was on my way to your place last night, I heard a clap, but I didn't pay attention."
    me "But Olga Dmitrievna did."
    un "They're lucky it was raining in the morning - or they'd have gotten such a «bang» from the counselor..."
    me "See. {w}Fast, funny, and topical."
    th "In the nineties, topicality would be very much in demand."
    play sound sfx_7dl["eat_horn"] fadein 1
    un "How the time flew by!"
    me "Did you rewrite everything?"
    un "I've done it all. Now I..."
    "She dabbed a glue pencil around the perimeter of a sheet of paper written on the other side in beautiful, cursive handwriting, and pasted a new article into the almost finished wall paper."
    me "It's not bad!"
    show un normal pioneer with dspr
    un "Yes, I know. Thanks."
    un "Really, Shurik took his time leaving: he had a big review article on him about the whole shift. Now there's no one to write it."
    me "And Electronik? He's still bumming around in the infirmary!"
    un "It won't work. Ugly handwriting, ugly writing."
    me "Then we'll use your drawings."
    un "I guess we'll have to."
    show un smile pioneer close with dissolve
    "She got up from the table, came up to me and hugged me."
    "And I, unable to help myself, leaned over and touched with my lips just below her ear."
    un "Mmmm... And here we forget about dinner and stay here."
    me "Come on!"
    hide un with dissolve
    stop music fadeout 5
    play sound sfx_open_door_clubs_2
    scene bg int_library_day with dissolve
    "Freeing myself from her grasp, I nodded at the key and left the room."
    "Zhenya, expectedly, was no longer in sight. It was as if she hadn't even come in."
    th "Maybe she really didn't come in?"
    "The lock clicked behind me."
    show un normal pioneer with dissolve
    un "I'm ready!"
    me "Then let's go, feed! We'll need plenty of strength to survive the evening's bonfire!"
    show un smile pioneer with dspr
    un "You're always laughing!"
    stop sound fadeout 3
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day5_un_7dl_washing:
    play music music_list["everyday_theme"] fadein 5
    scene bg ext_path_day with dissolve
    play ambience ambience_forest_day fadein 3
    "A few minutes later, when I, bending under the weight of a dozen wooden stakes, came to the back gate, the girls were already waiting for me there."
    show un normal pioneer at cright
    show sl normal pioneer at cleft
    with dspr
    sl "Ready, I see? Then let's go."
    "I muttered something incomprehensible."
    "The silence that hung over the path even the thick-skinned man would call awkward."
    "But what do I care - I personally enjoy awkwardness, especially since the girls have both gone ahead, leaving me alone with the wood, the road, and a very, very good sight of beautiful forms!"
    "Slavya was walking on my left hand, a living hint of where I should go, if anything."
    "Taut, slender calves, giving away a lover a fruitful jogging."
    "Elastic thighs of moderate breadth, belonging not so much to an athlete as to one who is no stranger to physical labor."
    "Glutes not large, but firm even to the view revealed through the pleated skirt."
    "Hypertrophied shoulders for a girl and a well-developed back."
    "To get her naked, oiled up, and with her gorgeous body and equally gorgeous tan, she'd be a ready-made visual aid for any fitness club."
    "So the customers would swallow voluptuous saliva looking at the blonde poster, and the female customers would pant with admiring envious anger."
    "Lena was noticeably different in the first place because she was half a head shorter and showed no tendency toward fullness overflowed into muscle."
    "A small, frail girl."
    "Calves rather like to dance - soft, feminine, rounded."
    "But the thighs are wide-almost flush with what Slavya was showing. For a connoisseur of true Russian beauty."
    "So rounded soft shoulders and a whiplash back are quite expected with those proportions."
    "A small, fragile girl, piled above her own height, hiding behind a slouchy back and eyes to the floor."
    "Just straighten your shoulders and you can't take your eyes off her."
    "Of course, this took me even farther than I'd ever planned, but at twenty-five these things start to matter a little bit."
    "Finally Slavya got tired of the silence and asked the question that seemed to bother her all morning head-on:"
    sl "Lena, is it true that you and Semyon are... that?"
    show un surprise pioneer with dspr
    un "That?"
    sl "Yes!"
    un "«That» what?"
    sl "Well! It's embarrassing for me to say."
    th "It's embarrassing to ask, then. {w}Logic!"
    show un shy pioneer with dspr
    un "And you try."
    "I couldn't count on Lena's insensitivity - apparently she understood it the way I would have."
    "If this is about Miku, then..."
    "Honestly, I don't even know. It all depends on who knows how much and how chatty."
    show un normal pioneer with dissolve
    un "You, don't fool around - just tell it like it is."
    th "At lunch, of course, I said we had something. But the extent of that «something» was not illuminated."
    th "Olga knows we slept together. Well... Sleeping in the sense of sleeping."
    if alt_day4_me_neu_transit == '':
        th "Zhenka caught us kissing yesterday, but I'm not worried about her - she'll be the last one to gossip."
    if not ((loki and (persistent.un_7dl_good_ussr or persistent.un_7dl_good_rf)) or (dr and ('nwsppr' in list_clubs_7dl))):
        th "And Miku saw that Lena was rolling me in the sand. I don't remember if there's any reference to this action in Japanese culture."
        th "Well, like how hot springs are a direct invitation to have sex!"
    dreamgirl "So who's the chatterbox? Whose head is going to roll across the frontal area now?"
    dreamgirl "Drumroll!"
    show un serious pioneer
    show sl normal pioneer
    with dspr
    sl "Dating!"
    "I took a breath and would definitely have wiped the sweat off my forehead if I had at least one hand free."
    un "How do you know?"
    "I hid shamefully behind the wood."
    th "I repent, I repent, my fault!"
    un "Such knowledge in my and Semyon's life..."
    sl "But he himself told me that you have more than just friendship."
    "Slavya blushed."
    show sl shy pioneer with dspr
    me "Let me ask you, what's the purpose of your interest?"
    "I was panting from behind the stack."
    me "You never know..."
    sl "No reason. Academic interest."
    dreamgirl "Academic plus a little fluid exchange, I bet."
    th "Don't try to make her look unflattering. {w}She's not dating anyone, thought I was single, but she got burned."
    "The girls didn't turn in my direction, but Slavyana's flaming ears gave her away."
    show un serious pioneer with dspr
    un "Swear."
    "Lena demanded in her most serious voice."
    un "That you won't tell anyone anything."
    show sl serious pioneer with dspr
    sl "Are you serious?"
    "Lena nodded silently."
    sl "Okay! {w} I swear I won't tell anyone what I find out here!"
    sl "Not to the counselors, not to my friends, not to my boss."
    un "What do you swear?"
    sl "On my keychain!"
    if alt_day1_sl_keys_took == 1:
        th "Keychain, huh?"
    un "All right."
    dreamgirl "And now we're going to tell you our worst secrets, take you to where our treasures are buried, and call for a third in the WMW."
    un "Yes."
    "Lena answered simply."
    me "Pardon?"
    show un shy pioneer with dspr
    un "What?!"
    "Confused Lena."
    un "I heard the question - the answer is affirmative."
    me "Don't you think we could have been a little more courteous after such a terrible oath?"
    un "More courteous? Well, if you want, you can kiss her on the mouth. {w}Or what do you mean?"
    if persistent.sl_7dl_bad:
        scene anim prolog_1
        with fade
        "{i}Her braided hair, no longer held back by braids and rubber bands, floats in a sultry haze, surrounding us with a golden cloud.{/i}"
        "{i}Her eyes are bottomless, her lips sweet, bitter, salty with tears beating their way.{/i}"
        "{i}One second more, and the buttons of my shirt are splattered flat in different directions, revealing me to the sun, the air and her palms.{/i}"
        "{i}«How I would love you», she exhales. - «To the pain, to the tears, to the death. Till a first-born child with your look and gray hair».{/i}"
        "{i}Her hair smells of tar and lemongrass, and her skin has that perfect shade of tan that no tanning beds can earn, and smells of red-hot sand.{/i}"
        "{i}A few seconds later, and her skin, heated to wetness, meets the peeling paint of the gate with a quiet rustle...{/i}"
        "{i}Her eyes are just above mine as she sits on top of me, wrapping her legs around my thighs.{/i}"
        scene bg ext_path2_day
        with flash
        show un smile pioneer at right
        show sl smile pioneer at left
        with dissolve
    else:
        "{i}Too close, too warm.{/i}"
        "{i}Sigh, breathe, smell, touch.{/i}"
        "{i}Why the hell isn't she wearing a bust - it's a crime against pubescent humanity.{/i}"
        "{i}One step closer.{/i}"
        "{i}Lips salty, sweet, firm, naughty, unresponsive.{/i}"
        "{i}We're doing something strange and unnecessary.{/i}"
        "{i}Don't we need the world?{/i}"
        "{i}How easy, it turns out, to tear off those shining, infallible paladin's plates of His Imperial Majesty's from her.{/i}"
        "{i}Just a kiss, and the light and aegis turns into a confused wench.{/i}"
    "I shuddered, wiggling out of an eidetic image, unknown to me and clearly not my own, and listened in on the girls' conversation."
    "It had already taken on a carefree tone-apparently, I'd missed a lot."
    "Both have crossed a certain threshold in communication, after which shyness or attempts at silence become meaningless."
    "With men this period usually falls between the third and fourth."
    show un smile2 pioneer with dspr
    sl "I'm running around the camp, not a clue. {w}The counselor called me - said that by tomorrow's dance they would check out the forecast from the local hydrometeorologist, and if anything, they'll do it in the canteen."
    if alt_day3_dancing1 == 'sl_1':
        sl "Well, I went straight to Semyon - we danced so well the day before yesterday."
        sl "And he's taken!"
        "I couldn't help whistling «the third must go»."
    un "So I go up to the porch, and there's Ulyana. She says if you don't hurry up, Slavya will take your Senechka away!"
    un "Well, I run, and he's sitting there..."
    show un smile3 pioneer with dspr
    "They chuckled softly in tone, causing me justifiable irritation."
    me "Girls, it's easy for you, isn't it? Why don't you take a heel of wood while I stretch my shoulders?"
    sl "No!"
    "With a laugh Slavya retorted."
    $renpy.notify('«cards in your hand» - recognition of someone as more experienced, more suitable to perform some action.')
    sl "You're the man - cards in your hand!"
    un "Why didn't you tell me it was hard for you?"
    "Lena softly rebuked me."
    show un serious pioneer with dissolve
    me "I said. Right now."
    "I had to put on my sternest and sternest face to keep the laughter down a bit."
    me "This is very hard for me! Ah, I'm dying, and I'm bequeathing my knickers to the starving children!"
    show sl sad pioneer with dspr
    sl "How can you joke about such things?"
    "In my immodest opinion, that's the kind of thing you should joke about."
    "As it was in «That very Munchausen»..."
    "A smart face is not a sign of intelligence. {w}All the stupid things in the world are done with the most serious faces."
    me "No, well, I said I was having a hard time, and I'm generally dying of an acute attack of laziness. Who's going to take me in arms now?"
    show sl surprise pioneer with dspr
    sl "What?"
    me "It's hard for me - someone has to carry me."
    show un laugh pioneer with dspr
    un "You're the one... Who carried nonsense here."
    un "Stop teasing Slavya already."
    "Lena is defending a potential rival... {w}However, the latter's potential for me personally is somewhere on the doorstep."
    "Offers to kiss her on the mouth."
    "The old sad-modest Lena that I liked would have quietly slumped under the table, fainting at the mere hint of such a thing!"
    "It's all my goddamn corrupting influence."
    dreamgirl "Now what? Divorce and cactus between the beds?"
    th "It turns out, oddly enough, that's the kind of Lena I like too."
    me "Who am I teasing? {w}I'm just tired of fooling around. How long is it?"
    "I eloquently tossed the bundle in my hands, making myself comfortable."
    show sl normal pioneer with dspr
    sl "No, we're already there."
    scene bg ext_polyana_day with dissolve
    play music music_list["dance_of_fireflies"] fadein 3
    $renpy.notify('«as if from a bush» - easy, effortless.')
    me "Forty minutes - as if from a bush."
    stop ambience fadeout 2
    "I dropped the rattling logs to the ground, and only the innate intelligence of a native St. Petersburger prevented me from uttering an admiring, foul-mouthed hoot."
    me "On the spot!"
    sl "Do you like the clearing?"
    show un smile pioneer at left with dspr
    "I liked the end of my ordeal better, but I nodded politely, just in case."
    "I tried not to think about going back to dinner and back here with the squad."
    sl "We haven't been here in over a week - we need to clean up the clearing, see if the animals have savaged the fire pit, and return the rocks."
    me "Will we make a fire?"
    show un laugh pioneer at right with dspr
    un "Aha, didn't carry enough wood - want more?"
    me "Is it necessary to mock me?"
    me "Maybe I have a skinny stuffy... I mean, a delicate mental organization, and now I'm stressed, depressed, and a bunch of other scary words with a double whistle!"
    un "Not bad."
    "Nodded Lena."
    un "Are you going to do the campfire or are you going to clean up the clearing?"
    show un normal pioneer with dspr
    me "Can I not do anything?"
    $ meet('we',"Girls")
    we "Can't!" with vpunch
    $ meet('we',"Choir")
    "The girls answered in tune."
    th "When did they have time to get along?"
    "Sighing, I staggered toward the fire pit - a small burning circle looked relatively harmless compared to the enormous clearing, which was a hundred percent littered with garbage."
    me "Graze by yourselves!"
    show un smile pioneer
    show sl smile pioneer
    with dspr
    sl "I knew he'd pick the hardest one!"
    th "Hardest?"
    th "It's a small bloody circle! What could go wrong?"
    "How wrong I was!"
    "The fire pit was a shallow hole in the ground paved with black cobblestones covered with a thick layer of soot and grime."
    "These bricks proved to be the first snag - leaving greasy black marks on my hands that there was absolutely nothing to scrub away."
    "And yes - there really were fewer than there should have been - the girls kept calling out to me, finding another rock."
    "And there I was, handsome as a chimney sweep, dragging another ceramic bar, coughing up the unprintable."
    "The number two hitch was the ash and ash deposits - kudos to Random for nailing them with a rain, now I can painlessly bury or take them to the woods on a shovel..."
    "Of course, if we had brought a shovel with us!"
    "But, as they say, man is a god only in the subjunctive mood - or more simply, everyone's hindsight is strong."
    "I had to confiscate one of Slavya's bags and try to wield it directly, sneezing and coughing at the minute from the fine particulate matter flying in the air."
    "As a result, by the time the two beautiful roses met at the edge of the clearing, clapping palms together, I was still digging in, stacking the missing bricks."
    "And compared to them, the clean-cut, beautiful ones, I looked like that elusive character from the fairy tale «Morozko.»"
    show un laugh pioneer
    show sl laugh pioneer
    with dspr
    un "Wow!"
    "Lena shook her head."
    sl "What do you look like!"
    "Slavya played along with her."
    me "What, What... Mom and Dad."
    me "You can only laugh it seems, and I have to walk all the way to camp."
    show sl normal pioneer with dspr
    sl "Okay."
    "Slavya took pity on me."
    sl "There's actually direct access to our river."
    un "And the soap, knowing how dirty you are, I got in advance."
    me "Why do I feel like I've been abused again?"
    show un smile2 pioneer with dspr
    un "You're too vindictive. We act only for your good."
    me "The words of every parent, every executioner of all time."
    th "I hope they're not going to wash me themselves?"
    "Hopes fuel the young..."
    "And all that."
    $renpy.notify('«Look you in the mouth» - Care very much.')
    "The most important thing is to find a quiet, submissive girl who will fall madly in love with you and look you in the mouth."
    "And stick with her, because only with such it's possible, a quiet family haven, where you will come in the evenings to rest after a hard day's work."
    me "Will I have time to wash up in time for dinner?"
    un "Of course! We'll help you."
    "Not our case."
    show un smile pioneer with dissolve
    sl "Don't be shy, I have a few brothers, I've already had experience bathing them!"
    me "Remind me: you're relevant there, and since when did {b}she{/b} get access to the body?"
    show un smile3 pioneer with dspr
    un "Oh, come on, you're greedy or what?"
    me "The commissioner's body? Of course I am!"
    me "And anyway, I'm embarrassed of her."
    "I tried telling something else for a long time, proving it, persuading it with both cross and pestle."
    "I was very persuasive. If my talent was let into the trade, I could make money from it."
    "Slavya stood silent and waited for the verdict."
    "Needless to say, the three of us went to the water as a result?"
    "Lena's verdict."
    th "What the hell damn it?!"
    "I get the impression that I'm being smoothly disenfranchised in our couple!"
    dreamgirl "Surely you don't mind being washed by two beautiful girls, one of whom is your current date and the other doesn't mind becoming one, do you?"
    th "Man, that's just wrong! I'm the man of the house!"
    dreamgirl "Currently, you're a dirtling. Relax and enjoy yourself."
    show un laugh pioneer with dissolve
    un "You look so upset..."
    un "Well, you can go to camp dirty. Just don't get upset."
    "She sighed brokenly."
    me "What about the «wash myself» option?"
    show un serious pioneer with dspr
    un "Not considered. It's less than an hour until dinner, and we still have to walk back."
    me "Lena, a word."
    hide sl with dissolve
    show un normal pioneer at center with dspr
    "I took Lena to the side, where we could not be heard by unnecessary Slavya."
    menu:
        "Do what you think is right":
            "Sometimes it's better to just relax."
            "And give in to compulsion. Especially such sweet compulsion."
            $ alt_day5_un_7dl_washing = 'sl_un'
        "Just let me wash myself, without this tomfoolery":
            $ karma -= 10
            me "Lena."
            "I put some sternness in my voice."
            me "The pampering is over."
            me "I wash myself, and we go to camp."
            show un shocked pioneer with dspr
            un "B-but... I-..."
            me "Lena."
            show un sad pioneer with dspr
            un "Whatever you say."
            "She sighed."
            un "We'll wait for you here. The river is at the end of this path."
            "She pointed in the direction."
            $ alt_day5_un_7dl_washing = 'me'
        "I don't mind you":
            $ lp_un += 1
            $ karma += 10
            me "I don't want her there."
            un "What is it? Afraid you'll like it?"
            me "Lena..."
            "I rolled my eyes."
            "Then I'll wash myself."
            $ alt_day5_un_7dl_washing = 'me'
            un "Very well. We'll wait for you here."
            "I wandered down that path to where the water glistened through the foliage."
    scene bg ext_beach2_day_7dl with flash
    play ambience ambience_lake_shore_night fadein 3
    if alt_day5_un_7dl_washing == 'sl_un':
        "We went ashore, where the girls, dropping my shoes and socks, made me strip down to my swim trunks and drive me into the water just above my knee."
        dreamgirl "And then they, well, go into the water next to you..."
        "The girls stand up next to me."
        dreamgirl "They have their skirts and shirts tucked up - so they don't get wet."
        "And that's where the libido didn't lie."
        dreamgirl "You hold out your hand..."
        "I held out the hand."
        dreamgirl "And Lena moves your right palm to her breast and your left palm to Slavyana's breast."
        "Lena took my hand."
        "And put the soap in it!"
        un "Hold it for now!"
        dreamgirl "Bruuuuuuh!"
        dreamgirl "Okay, then all hope is for Slavya to get close to you now."
        "Slavya stands up close - the way you do when you're sitting in a hair salon and the stylist is so young, and while smoothing your temples, she supposedly accidentally lays on your shoulder."
        dreamgirl "There, there! She's about to touch you with her upper ninety..."
        "I didn't even look at it: I was all caught up in fighting my reactions to the pictures my imagination was painting."
        dreamgirl "And then watch - her hand crawling down your belly, under the elastic band of your swim trunks..."
        sl "Give me the soap!"
        dreamgirl "What soap for you, you fool! Get on with it while Lenka can't see a thing because of the sun!"
        "The soap from my left hand went to Slavya."
        "I could barely stop myself from staggering towards her."
        "And she acted extremely correct and, judging by her dexterous actions, didn't lie about her experience in bathing her youngest."
        "Immediately she told me not to fidget or try to wash - instead, she soaped up a washcloth and with movements totally devoid of any erotic context, brushed the ash off my skin completely in a few minutes."
        "If she did allow herself to overdo it - neither Lena nor I noticed it. {w}You can tell when they're trying to carefully peel off a layer of epithelium!"
    else:
        "Finding the said descent to the water, I dealt with the contamination at a brisk pace - simply by stripping naked and diving in."
        "I had to paddle underwater to get past the grease stain that had formed on the surface."
        "But it saved me a lot of time."
        dreamgirl "And also nerve cells from an unruly libido."
        "I was inclined to agree with that, if you wash, you wash, and if you pamper, you don't pamper, you don't pamper being drenched in ashes."
        "Having finished my business, I went ashore and, dressed, hurried upstairs."
    stop ambience fadeout 3
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene bg ext_polyana_sunset with dissolve
    show un normal pioneer at right
    show sl normal pioneer at left
    with dspr
    un "We still have time for dinner."
    "Lena threw a glance at her watch."
    me "Then let's roll. I hope we remember the road well and don't get lost within two hundred meters of the fence."
    sl "Don't worry - we've been here for years."
    me "It's more about me..."
    "I mumbled."
    sl "Let's go!"
    "Paying no more attention to us, Slavya headed toward the path leading to the camp."
    "Lena, grabbing my hand, rushed after her."
    "Are the glorious traditions of the early days coming back?"
    "Are we doing everything in a hurry again?"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day5_un_7dl_supper:
    play music music_list["eat_some_trouble"] fadein 2
    scene bg int_dining_hall_people_sunset_7dl with dissolve
    play ambience ambience_dining_hall_full fadein 5
    if alt_day5_un_7dl_washing == 'sl_un':
        "We were lucky - the horn caught us just as we were approaching the camp, and the evening sun dried the uniforms right on top of us."
        "So without further ado, we threw the garbage bags into the container by the gate and hurried to the temple of Mammon."
        "The three of us sat down without talking - having become firm friends over the past three days - and, as those responsible for cleaning up the campfire glade, we were not at all surprised that Olga Dmitrievna had taken the floor."
    else:
        "Dinner went on as usual, but Olga Dmitrievna decided to surprise everyone by taking the floor."
    show mt normal pioneer with dissolve
    mt "Dear Pioneers and Pioneer-Leaders! As you undoubtedly already know: an evening camping trip with a bonfire is planned for today."
    mt "I inform you that there is no change due to the rain - the squads will leave according to the schedule immediately after dinner."
    show us smile pioneer at cright with dissolve
    us "And potatoes?"
    "Ulyana spoke up."
    show dv laugh pioneer2 at fright with dissolve
    dv "Ulyana, you hungry little girl, aren't you full now?"
    show us sad pioneer with dspr
    us "You don't understand anything, it's a romance!"
    show dv grin pioneer2 with dspr
    dv "Romance of a stuffed belly, yes of course!"
    show mt laugh pioneer with dspr
    mt "Those who want potatoes can get them here - but they'll have to carry them themselves!"
    dv "Got it? You carry them, you boil them, you eat them!"
    show us dontlike pioneer with dspr
    us "Hey, that's not fair! I can't carry that much."
    hide dv
    hide us
    with dissolve
    "Ulyanka pouted and turned away."
    mt "The firewood is already in place, but because of the rain it's still wet. That's why only the best pioneers will be allowed to make campfires."
    mt "The main camp fire, as usual, is made by Slavya."
    mt "I'm done."
    hide mt with dissolve
    "Olga finished her speech and sat back down."
    show sl smile pioneer at left with dissolve
    me "Don't get cocky!"
    sl "What are you talking about?"
    me "The flag is yours, the fire is yours, the place by the rock is yours..."
    sl "The place by the rock?"
    me "Nevermind."
    hide sl
    show un smile pioneer
    with dissolve
    "I turned to Lena:"
    me "If they line me up in a line of two, will you come with me?"
    show un smile2 pioneer with dspr
    un "And you dare asking! Of course I will!"
    stop music fadeout 3
    scene bg ext_houses_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 3
    "«The road arises under the feet of the walker» - at first you take the first step, convincing yourself that it's «just a try», and then you begin to depend on the measured march of time."
    stop ambience fadeout 2
    scene bg int_house_of_mt_sunset with dissolve
    play ambience ambience_int_cabin_evening fadein 2
    "I touched my wash-soaked jeans with disgust."
    th "No, I'd rather wear shorts."
    "But I threw my sweater over my shoulders and tied the sleeves in a knot."
    stop ambience fadeout 2
    return

label alt_day5_un_7dl_campfire:
    scene bg ext_square_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 3
    play music music_list["lightness"] fadein 3
    "The raincoat has found its place, thrown over the elbow of my left hand, the right hand already firmly and unyieldingly clutched by greedy fingers."
    dreamgirl "And thou shalt be separated from thy father and mother, and thou shalt cleave to thy wife..."
    dreamgirl "And there will be no one closer to you, and only through her will you become great. And thy en..."
    th "You've been stormy all day today."
    dreamgirl "Don't mind it, it's just... Our shared intuition. Listen to the chill under your heart - can't you smell anything?"
    th "Since some time I prefer to accept all changes with gratitude. I can't influence them anyway."
    dreamgirl "Well, I smell change."
    th "A little more specific?"
    dreamgirl "I don't know! As soon as I'm at least fifty percent sure, I'll let you know."
    "There was only one fantastic suggestion..."
    "I was about to furtively glance at the serenely smiling girl, but I was distracted by Olga Dmitrievna taking the floor:"
    show mt normal pioneer far at center
    with dissolve
    mt "Squads, on the first-second, count!"
    "And a machine-gun line of tinkling voices broke out under the chestnut and pine trees - «first-second-second-second», in phantasmagoric morse code."
    mt "The second numbers - step forward."
    "Exactly half of the pioneers present stepped forward and, obeying the next order, turned right."
    mt "In a line of two."
    "We, as the two smartest, immediately calculated in pairs, but Olga Dmitrievna reacted faster:"
    mt "Semyon, you go with Elektronik, he has no pair. Lena, you go with Miku."
    me "Maybe we should hold hands, too?"
    "I quipped."
    mt "If I command it, you'll hold hands, too."
    "Counselor didn't pay attention to sarcasm it seems. She raised her voice, again addressing the whole camp."
    mt "Pioneers! Remember that you will always prioritize mutual help and support! {w}You must always be ready to come to the aid of someone in need, to rescue and encourage them."
    mt "And that's what we have to learn on this hike!"
    "The USSR anthem played in my ears again, and I shook my head, driving away the obsession."
    "Enough. Only Electronik in the pair is more than enough, actually."
    "Mindful that any arrangement can be pulled off with a well-developed diplomacy skill, I looked around for a way to make the exchange."
    "A dead giveaway - Syroezhkin wouldn't even tempt the Buzzer, let alone Miku."
    th "But maybe Miku could be bribed?"
    "Thinking over the possible amount of kalyma, I found the Lena-Miku pair and regretfully gave up the idea of doing everything quietly - so unambiguously and spitefully was Lena hissing something at the poor Japanese girl."
    "The Electronik guy, however, judging by his blank eyes, was in «standby» mode and not at all suitable for negociation."
    th "Hmmm... Maybe go for the fool at all, just take Lena by the hand, and..."
    mt "Semyon!"
    "The counselor's voice brought me out of my thoughts."
    show mt normal pioneer at center
    with dissolve
    "I swam with an effort out of the maelstrom of reflection."
    mt "I see you're not thrilled with Electronik?"
    me "You ask..."
    mt "I've decided to go along with you. I'll send Slavya with him: the girl will be able to see to it that all is well."
    "I started to nod, but stopped myself halfway through the move."
    th "But if Slavya goes with Al, then... Stop!"
    me "What, are you going to send me with the Buzzer?!"
    "Olga Dmitrievna smiled irresistibly."
    "And I felt like cracking my head on the corner of the pedestal. Truly, no matter how nightmarish things get, it will always turn out to be even worse."
    mz "I heard everything."
    "It creaked from behind."
    th "Of course you heard everything, you marginal misunderstanding."
    hide mt
    with dissolve
    show mz normal glasses pioneer at center
    with dissolve
    if alt_day4_me_neu_transit == '':
        "She and I have managed to fight and make up, but the whole time we haven't even exchanged a word."
    me "Please don't think I'm thrilled."
    show mz bukal glasses pioneer at center
    with dspr
    mz "Don't think I'm glad!"
    "In tune with me, the librarian replied. Our alliance may not be without its thorns, but we mutually respect the right to send anyone to the baths."
    me "Shall we swap?"
    "Without much hope, I asked."
    show mz angry glasses pioneer at center
    with dspr
    mz "I'd love to go alone. What can you suggest?"
    "I want to go with Lena! - almost jumped off my tongue. Yeah. Of course that's what I'll tell you."
    me "Looks like nothing..."
    mz "I'm not surprised."
    "She turned away."
    hide mz
    with dissolve
    th "Just don't think I'm going to argue or convince you. There's nothing else for me to do."
    "Fiercely I thought into the receding slouching back, left shoulder higher than right, slightly bouncing gait. Pierre Richard in a skirt, damn it. Only there's nothing puppyish about her - it's replaced by malice."
    stop music fadeout 3
    "Sighing doomfully, I followed Zhenya."
    stop ambience fadeout 2
    scene bg ext_backroad_day_7dl with dissolve
    play ambience ambience_forest_evening fadein 3
    "The point of moving in pairs was while we were walking through a clearing, then walking hiking trails."
    if alt_day5_un_7dl_washing in ('me', 'sl_un'):
        "By my reckoning, it was about half a kilometer to the firehouse when the trail narrowed to an individual non-wide one."
    "As a result, we still lined up in column one at a time."
    "That very path - I'm always amazed at the ingenuity of camp planners."
    "The distance is tangible, but if you look from above - the movement is in a straight line, and after a couple of walks back and forth you can orient yourself blindfolded."
    "But the scarlet evening glow, the slowly thickening evening shadows, and the spirit that is unique to the evening woods made the adventure a hundred times more exciting."
    if alt_day5_un_7dl_washing in ('me', 'sl_un'):
        "When I was dragging a pile of lumber here, it never occurred to me to feel any patriotic-social emotion or involvement in anything - just the sweat pouring to my eyes and hands pulled away."
        "This time, however, there were no distractions, and I felt exactly what I should have felt when I tripped, almost flew my nose into a tall ant hill, and Zhenya, catching my arm, held me back."
        me "Thank you."
        "I squeezed out."
        show mz normal glasses pioneer at center with dissolve
        mz "Let's not make a tradition out of this."
        me "Deal."
        hide mz with dissolve
        "Embarrassed by the fact that I was saved by a girl who obviously had a grudge against me, I doubled my vigilance and dodged roots, branches, pits and gullies as hard as I could the rest of the way."
    scene bg ext_polyana_sunset with dissolve
    if alt_day5_un_7dl_washing == '':
        "And then, finally, the coveted fire pit. How do I know? They're like subway stations - if you see one, you've seen them all."
    else:
        "A few minutes later the familiar campfire glade appeared between the parted trees."
    "A large space, cleared of vegetation, lined around the perimeter with thick tree trunks, so that the pioneers could sit down."
    "And, of course, a large fire pit lined with stones - after all, a campfire is a campfire, and a pioneer has to take care of the forest, too!"
    stop ambience fadeout 2
    show mt normal pioneer at center
    with dissolve
    mt "Let's make a stop here."
    hide mt with dissolve
    play music music_list["dance_of_fireflies"] fadein 3
    "You could see a few smaller campfires further away, just in case there was a squad-level event."
    "But now everyone was seated around the big campfire - apparently deciding to get involved in the social life of the camp first."
    "A little later a few more sparks would take over, the collective would split into a bunch of smaller circles... {w}Camp kids are the same at all times."
    "Slavya was already assembling a 'hut' out of logs - judging by her confident movements, not for the first or even the tenth time."
    play sound_loop sfx_forest_fireplace fadein 3
    "Here she poured a smaller firewood in the center, and, taking a box of matches out of her pocket, with a cheerful look lit the sulfur on the teal, and a flame was born."
    "In a minute the bark, wood chips, and cinderblocks were engaged - like a keen pioneer, Slavya did not use any paper when making a fire."
    "Olga, who was watching her, nodded in satisfaction and put the newspapers back in the bag."
    "I automatically noted that some newspapers were here after all, but immediately forgot about it."
    "Why do I care what's going on in the world? Nothing good was going on there a priori in '89."
    th "Slowly I was occupied by the very feeling that is only possible near a fire."
    dreamgirl "I'll sing... Like a glow from the sunset, the fire dances between the pines..."
    "I glanced around the clearing once more, and sighed, once again not finding the one I wanted."
    show sl normal pioneer at center with dissolve
    sl "What are you thinking about?"
    "Slavya came up to me."
    me "Why do you care..."
    "Philosophically I dropped into space."
    sl "Who knows. Maybe it matters to me."
    me "It can't be important to you, I'm sorry. It's none of your business."
    sl "I won't impose."
    hide sl with dissolve
    "She rose easily and vanished into the twilight."
    "And rightly so. A few more minutes in her lusciously optimistic company would have been too much for me."
    "And I sat there, counting the seconds that were wasted, when I finally found the one I should have found half an hour ago."
    stop music fadeout 3
    with fade2
    return

label alt_day5_un_7dl_evening_un:
    scene bg ext_polyana_sunset with dissolve
    "In the dusk descending on the forest, barely dispersed by the flare of the fire, I miraculously discerned a familiar hairdo."
    "I almost caught her gaze, fleetingly surprised that she wasn't looking the way I'd been used to over the past couple of days - softly, with a twist."
    th "And her lips are unpleasantly pursed. Arguing about something with Slavya."
    th "Does she trust the activist so much that she's willing to compromise even her own mask?"
    "Slavya seems determined to turn off the goody-good girl, too."
    "With a groan, I pulled myself off the log and wandered off to separate them."
    show un angry2 pioneer at cright
    show sl angry pioneer at cleft
    with dissolve
    sl "No one was stopping him from spitting on all the inhibitions. {w}If you're in love like that."
    un "What are you talking about?"
    sl "Ask him yourself."
    "Slavya nodded, having already noticed me."
    sl "What is it worth to him to have this affair of yours. {w}There he is, by the way."
    "My cover has been blown."
    me "Slavya."
    "I sighed wearily."
    me "You've been hovering around me for three days now. What the devil do you want, huh?"
    sl "Me? From you? Ha-ha-ha."
    "Her laugh sounded unnatural, and everyone here noticed it."
    me "Exactly. While I was free - you didn't care at all."
    me "And that official statement of the relationship seemed to change anything. {w}what, someone else's is sweeter, right?"
    "Slavya wanted to say something, but I looked at her with such dislike that the argument seemed to die right in her chest."
    hide sl with dissolve
    "Slavya got up and left, leaving us alone."
    "A tense silence rang out between us."
    un "Semyon, I don't believe half of what Slavyana says."
    un "But there's no smoke without fire..."
    if dr:
        me "I really should have been more decisive."
        me "It's a pity that it's so hard for me."
        me "Are you going to hate me now?"
        "She's gone silent."
        "Just as I expected."
        "All my relationships end on that note."
        "So the next time she says we have to break up, it won't hurt much anymore. I'm used to it."
        "But she surprised me again."
        show un smile pioneer with dspr
        un "Maybe, only for what you do to me."
        un "Hug me, please."
    else:
        play music music_list["you_lost_me"] fadein 3
        me "It happens."
        me "You made two mistakes - first, trusting me and her equally."
        me "And then by easily offering her to wash me."
        me "And now you have the conscience to ask me about smoke without fire?"
        dreamgirl "The narrator shoots himself."
        me "Go to hell with that claim."
        dreamgirl "Curtain."
        hide un with dissolve
        "And, having already turned around, disregarding the first sob behind my shoulder, left a pounding, preening kettlebell."
        me "You hurt a person. Are you glad?"
        "The resounding murmur of voices, guitar picks and laughter drowned out the sobbing soul."
        th "This time absinthe won't do it alone."
        th "How tired I am. To open my head, to shed light there, to throw away unnecessary memories. Formatting my memory with a high voltage cable."
        "Why can the slender edifice of a relationship be ruined by a few words of the occasional redneck with golden braids passing by?"
        "Why, in such a situation, is all the faith placed in the schemer, who has some purpose of her own, and not in the fully sincere me?"
        th "I wonder, of the existing and available possibilities, which death would be the most painless?"
        th "Pills? Or a rock around my neck and into the same miserable river? Or maybe take a dangerous razor from Sanich, and... I just have to hide somewhere where they won't find me for sure."
        "Covering my eyes, I let despair pick me up and drag me into the blackest and bottomless depths. I'm not here; I've been given a second chance to walk the same beloved blister a second time."
        "And to Lena sitting next to me, I reacted in the most correct way. No."
        th "Maybe they have some secrets of their own, and I'm here with my pig snout and romantic pretensions, sentimental, annoying bastard..."
        show un serious pioneer with dspr
        un "You have to swear that she lied about everything."
        me "You're wrong. I don't owe you anything anymore."
        un "Why? But we..."
        me "«We». There is no «us» anymore."
        me "And clear my personal space, please."
        "The hangman's pity is a steady hand."
        me "I promise to cram myself into the deepest hole for days before I leave, where I won't piss you off. And believe whoever you want, think what you want..."
        un "But I don't want... that. I want to be with you."
        me "Until when? Until Slavya tells you again about my fickleness or easy availability or something else?"
        "I picked up a lump from the ground and threw it into the fire."
        me "I'm sorry, Princess, but that's not how it works. You either believe it or you don't. Tertium non datur."
        "I may have acted dishonestly in telling you everything without concealment."
        "But a few seconds later, a miniature palm rested on my knee."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day5_un_7dl_evening_dv:
    scene bg ext_polyana_sunset with dissolve
    "Alisa and Lena were yelling at each other, but when I approached, Lena cried quietly and ran away."
    "I stared stupidly in her wake."
    show dv angry pioneer with dissolve
    dv "What are you sitting there for, retard!"
    "Alisa, who appeared out of nowhere, barked."
    dv "Run after her!"
    me "...where?"
    show dv normal pioneer with dspr
    dv "The only place where Lena hides to lick her heart wounds is the island. Nearby."
    dv "Try not to get lost on the way to the boathouse."
    me "I don't know why you're doing this, Alisa. But thank you."
    dv "Don't ever tell anyone about this."
    "She grumbled."
    dv "How much longer are you going to sit there?!"
    show dv angry pioneer with dspr
    dv "GO!" with vpunch
    hide dv with dissolve
    "I jumped up on the spot and headed toward the exit of the clearing, figuring out the direction."
    show us normal sport with dissolve
    us "Newbie!"
    me "Yes?"
    us "If Lena won't take you, come back to us!"
    me "Why?"
    show us grin sport with dspr
    us "Let's beat this camp!"
    "The compliment was dubious, but in my position I had no choice."
    me "Thank you!"
    hide us with dissolve
    "I shouted, switching to running."
    stop sound_loop fadeout 3
    scene bg ext_path2_night at fast_running
    play music music_7dl["sneakupon"] fadein 5
    "I don't even know what was more amazing."
    "Today, miracles came out of the horn of plenty."
    "And so... Why not have one more tiny miracle - one that will keep me from getting lost and lead me to the boat station?"
    scene bg ext_path_night at fast_running
    "At any other time I would have been terrified and frightened by the sounds of the forest at night - screeching, whooshing, screaming..."
    "But I turned on bulldozer mode and went ahead without fear of even breaking a leg."
    "After all, a broken leg is a sign that intuition and instinct are working against me, they are not subject to the general directive of falling in love."
    "And do I then deserve the right to a miracle if I am unable to negotiate even with Jungian depths?"
    "Two steps - inhale - two steps - exhale."
    "Night, summer, rolling moon."
    "A stab in my left side, a desperate desire, if not to make it, at least to try."
    "The sluggish saliva, the eye-blocking shroud of oxygen poisoning."
    "I ran like I'd never run before - through a strange, unfamiliar forest, with every chance of missing both the camp and the chance to make things right."
    "But ... everyone gets the reality they deserve."
    "The artist has it pictorial. An addict has it full of strings, centering and drugs."
    "I have dust, megabits and inches... At any rate, that's the way it was before camp."
    "My present reality for the first time is not about myself."
    "From the first thought - at a frequency of two hundred times an hour - to the passing out before sleep."
    "And so I wasn't surprised when I heard the splash of water and sprawled to force a two-meter brick barrier."
    "I had no right to screw up."
    $ persistent.sprite_time = "night"
    $ night_time()
    scene bg ext_boathouse_night with dissolve
    play ambience ambience_boat_station_night fadein 3
    "One boat was really missing - as was one set of oars."
    th "Pull, my dear! Help me out!"
    "I prayed to my guardian angel."
    th "I need that last bit of luck!"
    "The bottomless blackness of the night water took its first paddle with a quiet splash."
    scene cg d5_boat_night_solo_7dl with dissolve
    if alt_day2_us_escape:
        "With my physical fitness, which consists of a whole 200 meters on oars, it was pointless to think about doing everything smoothly, quickly, and like in the movies."
    else:
        "With my physical fitness, it was pointless to think about doing everything smoothly, quickly, and like in the movies."
    "Oh no, I tobaccoed for ten minutes first, aligning the bow on the course."
    "Then I tried to figure out how to row properly."
    "As a result, three hundred yards of the course turned into five hundred - ripped shoulder girdle muscles and pissed palms."
    "But I forbade myself to be distracted."
    "It wasn't until a shoal rattled beneath the bottom of the boat that I unbuckled with a groan."
    th "Goddamn it, I'm so tired!"
    "I pulled the boat as far as I could ashore and fell flat, trying to catch my breath."
    scene bg ext_island_night
    with dissolve
    "And I didn't care for the beauty of the surroundings, nor for the magical silence of the July night."
    "Very meaningful is the fact that I was constantly dragged by the hair somewhere by the plot of the local play, not allowing me to stop or look closely at the scenery."
    "Maybe they turn out to be cardboard, crudely painted, and I, like a clown, worrying for real, living for real - a silly mistake in the cyber play's code, determined to be a living real person."
    "Doubly stupid for daring to make any claims of her own."
    "I don't know how long I lay like that, but when I got up - I noticed that not far away, literally a couple of meters from my boat lies another boat - apparently, Lena is really here."
    "I didn't notice it while I was «parking» - Wasn't myself from fatigue."
    play sound sfx_boat_impact
    with vpunch
    "I poked the plastic side with my fist in anger - as if the unfortunate watercraft was guilty of something."
    "Though now I was ready to assign blame to anyone - after all, the hardest thing to admit your own guilt was to yourself."
    th "I hope she will at least listen to me."
    "Not that she has an extensive choice."
    "But I'd rather be listened to «because of love»."
    stop music fadeout 3
    stop ambience fadeout 2
    with fade
    play music music_7dl["rewind"] fadein 5
    "I don't know what she was doing here, or why she was here."
    un "Don't come closer..."
    "Without turning around, Lena warned."
    me "I've come to repent and ask to be taken back."
    "All my contrived cheerfulness was enough for exactly that phrase."
    me "That's it."
    "I mumbled inaudibly."
    un "Not a step closer."
    dreamgirl "That's close enough."
    "She repeated."
    me "You want me to talk to your back?"
    "She didn't answer anything. That's right, of the two of us, it's my fault - it's up to me to adjust."
    me "As my princess commands."
    scene cg d5_un_island
    with dissolve
    "We took seats on opposite sides of the same tree and looked up at the same stars, breathed the same air - infinitely close, infinitely alien."
    me "Wow, you have such checks here."
    un "Here?"
    "She clarified blankly."
    "She seems to have reached the point after which depression ceases to be inside and in smooth jerks, obeying the beat of her heart, paints the whole world in doomed gray tones."
    me "I mean Slavya."
    "I prudently remained silent about the details. There was no need for Lena to know about them."
    un "How did you find me?"
    me "There are no barriers to true desire."
    un "And yet..."
    me "Redheads."
    un "Makes sense. Only Alisa knew..."
    me "Whether Slavya knew what she was doing is a really interesting question."
    un "She cared."
    me "To the point where she's willing to get into a candidate's soul? Why do you let her do that?"
    "A hit-and-run wasn't the best tactic in the situation, but I had nothing else to do - my head was empty and ringing."
    me "Or is she on your clearance committee, before allowing anything else?"
    un "And you yourself are without sin, aren't you?"
    me "What?"
    un "If I hadn't been there, she would have seduced you. Even at lunch... You think I didn't saw it?"
    me "Len... I have instincts after all."
    un "So now what? I'm supposed to melt down and throw myself into your arms just because you managed to whitewash yourself?"
    "The bitterness in her voice could match the strength of my favorite absinthe. Splash it soldier-like, in thick slices, and drown your teenage love - so you don't get sick of the pink sugary goodness."
    me "No. Just don't let her near me anymore."
    "I don't know if I can hit a girl, but I can break an arm for sure - need will teach me, need will force me."
    un "So she won't come near you again. You are declared unfit."
    me "By whom?"
    un "By whom what?"
    me "Declared unfit by whom? By you? By her?"
    un "What difference does it make?"
    me "The difference, honey, is that it is not her who'll live with the consequences of the choice. It is your heart and yours alone."
    me "I'm not promising love till the grave or safe haven or anything like that."
    me "But I know for a fact - I'll be always important to me to know where you are or what happens to you."
    me "I want to hold your hand and know every cockroach in your head inside and out."
    un "Words again..."
    me "Yes. What's wrong with that?"
    "She sobbed."
    un "Just words."
    me "But..."
    "The right thing to do would be to hold her close to me, kiss her and whisper something comforting."
    "But what am I to do if I can't, dare not look behind the tree?"
    "There was another soft sob behind the tree, and I, trying to move silently, went around the obstacle, and..."
    scene bg ext_island_night
    show un cry pioneer
    with dissolve
    "My only one sat on the bare ground, arms around knees, crying silently into the starry sky."
    "And I, only I was both the cause and the deliverance."
    th "Why can't everything be simple?"
    with fade
    th "Why can't it be without pain?"
    th "Can't two people just become one - do they have to listen to the opinions of others?"
    "Even if it's the refined happiness of teenage love."
    "Or rather, because it's about it."
    "And I've already flopped down on the ground and hugged Lena."
    "As if there was any other choice."
    "She mumbled, shaking her head, trying to pull away - but in vain."
    me "It's okay, honey... It's okay."
    un "It's not okay. You can't even make sense of yourself."
    un "You came here for some unknown reason, and you sailed after me for some unknown purpose."
    un "Why? What do you want here?"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day5_un_7dl_runaway:
    scene bg ext_polyana_sunset with dissolve
    play music music_list["reflection_on_water"] fadein 3
    show un normal pioneer with dissolve
    "And when the nerdy guitar riffs played by a Japanese girl disconnected from the tourist industry, and therefore without soul, bored me to the point of nausea, Lena rose easily and pulled me along with her."
    un "Let's go, Senechka. Let's go."
    me "Where to?"
    show un laugh pioneer with dspr
    un "How naive you are, after all. Where do you go at night from the fire?"
    dreamgirl "In the bushes?"
    un "You're running away!"
    stop sound_loop fadeout 3
    scene bg ext_path_night
    show un normal pioneer
    with dissolve
    "She guided me confidently through the gullies, finding by her own intuition the indistinguishable paths in the night forest."
    "Pale transparent skin, huge green eyes, and lips - ruby, rowan blood on the freshly fallen October snow."
    "I confessed it to myself a long time ago, but I never had the guts to breathe it out."
    "She was slowly and surely driving me crazy, looking unsmiling, distrustful, and not yet fully aware of how serious everything was."
    "And the surrounding forest held thousands of the same tales and mysteries - and here and there in the bushes you could already distinguish the chuckles, the sounds of hot kisses and accidental moans of first love."
    dreamgirl "Hey, hey, horny jokes are my kind of thing! Don't steal my bread."
    th "He who had the time, ate the time."
    "The vigilant pines watered my lungs with ineradicable ozone, and I wanted to walk like this forever, holding the dear creature by the hand, and drink, drink this night, and the tart air and the sweetest thing, the anticipation."
    $ persistent.sprite_time = "night"
    $ night_time()
    scene bg ext_boathouse_night
    with dissolve
    "We got out on a narrow sandy spit, at the far edge of which we could discern the illumination of the local lights near the brig and the glimmers walking on the night water, three times as bright as the impenetrable southern night."
    th "We have everything as people do - night, summer, kisses, intoxicating even without wine. A brief resort romance with length of seven days of summer."
    th "How I don't want it to end, Lord."
    "Bind, glue, diffuse through, becoming one... {w}We have no right to part, we are too much a part of each other - the rearranged metabolism can no longer handle it alone."
    show un normal pioneer at center
    with dissolve
    "The boatman was asleep."
    if alt_day2_us_escape:
        "However, last time I ran away he was asleep too."
    me "We've already run very far. Is that enough, or do we keep running?"
    show un serious pioneer with dspr
    un "Keep. Take the boat."
    me "I don't think this is the best time to go boating..."
    me "But whatever you say."
    "While I was unhooking the boat from the edge, Lena had time to go get the oars and the rowing rods."
    show un smile pioneer at center
    with dspr
    un "Swim!"
    "And immediately occupied the back bank. The hint as to who's going to row is obvious enough."
    th "Well. Then it's my fate to be constantly engaged in unnecessary physical activity."
    "The oars went into the ledges, and, after a little tabbing, the bow of the boat pointed straight to the island «Close» - at least that's what the local charts said."
    me "Are we sailing to the island?"
    "Lena nodded."
    scene cg d5_un_boat_7dl
    with dissolve
    "I don't want to remember the nightmare my shoulders were subjected to; merciful memory has removed it from the list of impressions."
    "That may be right. There's no reason at all to mar such a magical night with lowly bodily inconveniences."
    "And if there's the most magical girl around, and the promise in her eyes passes for the part of miracles that no religion can explain - what right have I to complain here?"
    "Three hundred yards to that shore, with palms worn to the bone, with four breaks and Lena's mysterious smile."
    me "So this isn't your first year here?"
    "Lena smiled, realized she was sitting hunched over, and straightened her back."
    if alt_day_binder == 1:
        un "I told you already."
    un "Yes. A kind man shared a trip with us."
    if herc or loki or not ('nwsppr' in list_clubs_7dl):
        un "And before that, my father was given it through the committee as the caregiver."
        un "Because mother..."
        "Lena was silent."
        "There are words you don't have to finish."
        "Their essence becomes clear when you hear the person's voice droop."
        "You see how she bites her lip, trying to hold back the emotion bursting out."
        "Wounds to the heart heal with time, but they always leave scars."
        un "In short, it doesn't matter."
    un "It was even enough as long as I went here - the counselor knows not to shake me, I know to get involved in camp life."
    "Her voice sounded quieter and quieter, as if losing what remains of the determination with which it lifted me up and dragged me through the thicket."
    un "Until I..."
    th "Didn't meet me. It makes sense."
    me "Sorry, didn't mean to be a note of dissonance. {w}Do you want to play it all back?"
    stop music fadeout 5
    "Instead of answering, she scorched me with a look."
    play music music_7dl["unforgotten"] fadein 6
    $ lp_un += 1
    un "I'll crack you in the forehead if you say that again. It'll hurt."
    th "And she will."
    "Lena had the most determined look."
    "I guess I'd even be scared, if that last sentence hadn't been a tribute to half-suffocated politeness and common sense."
    me "I knew you'd say no."
    "The bottom of the boat rattled on the sandbank, and I hurriedly jumped ashore."
    scene bg ext_island_night
    with dissolve
    play ambience ambience_lake_shore_night fadein 3
    "After dragging the boat up as far as I could, I threw the noose of to the bushes and fell flat, trying to catch my breath."
    "The shirt could be wrung out, but the young body came to its senses very quickly - not a minute later, and I was already rising from the sand."
    "Lena was standing on the shore, looking toward the camp, her back to me."
    "I walked up to her, hugged her from behind. {w}She silently caught my palm and pressed her cheek against it."
    "There were bats hovering sleepily overhead, which in a couple of hours would begin their games over the water, frightening the neighborhood dogs with an ultrasonic sound."
    th "Though what dogs are there, three hundred kilometers from the nearest settlement..."
    "On the other side, paused, the usually pounding life of the camp - appealing, kind, sweet, childlike and direct."
    "What a pity that most children change from childhood to mere boring adulthood."
    "How fortunate that the universe has found an equal replacement for this girl."
    dreamgirl "Your ego, of course..."
    th "But I'm really going to keep her from becoming a grown-up, boring aunt. I won't let."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day5_un_7dl_island_hen:
    scene bg ext_island_night with dissolve
    "I turned the girl toward me, tried to hug her, but she ducked easily, released from my arms - and, putting an end to the eternal argument, pressed her forehead against my shoulder. She won, she trusted."
    show un normal pioneer close with dissolve
    if alt_day4_me_neu_transit == '':
        un "This camp had better be made up."
        me "If the camp is made up... Then you're made up, too. Isn't it scary?"
        un "No."
        "She looked up, flickering wet in the glow of the waning moon."
        show un smile pioneer close with dspr
        un "I'm not afraid to be made up. I don't care."
        me "But then I'll be fiction, too. Is that what you want?"
        show un normal pioneer close with dspr
        un "What are you... Of course not."
        me "Then don't talk nonsense."
        un "Nothing that you wouldn't think. See how honest I am?"
        un "Love is measured by the measure of forgiveness... Semyon, which one of us is talking nonsense?"
        me "Both of us, darling, both of us..."
    un "What do we do now?"
    th "There is nothing for us to do. {w}I can make plans."
    "Trying to get my breath back from the steel hoop of longing in my chest, I thought fiercely."
    th "To bloodily stamp my fists on a brick wall, just to forbid myself to be."
    th "But if the damned Demiurge should think of tearing us apart - what could I do?"
    th "If he's like the goddamn Ocean Thinking, unknowable and unattainable - I can't even punch him in the face, trying to put things back the way they were."
    "It's not my world, not my time, but integrating into society would be an acceptable sacrifice for... Leaving things as they are? To go with the flow, conscience of my own and obscurity absolved of any little responsibility?"
    "This girl to love, again, what about all the women's novels, there's no nine millimeter butterflies in the belly here, there's such despair that if something happened to one of us... I dread to even think."
    un "Hug me."
    "Lena asked."
    un "Please."
    hide un with dissolve
    "I kissed her gently, like she's a child."
    if herc:
        "Five days away, harnessed like a three, from the indifferent Semyon Sychev to the Shakespearian-obsessed me."
    else:
        "Five days away, harnessed like a three, from the indifferent Semyon Persunov to the Shakespearian-obsessed me."
    "What's all this for?"
    "If one day I can open my eyes on the icy leatherette of the LIAZ."
    "Open my eyes to my native Peter, where I never was and never will be again?"
    "Back to my home, to dusty shelves and a twenty-megabit existence with a twenty-four-inch screen."
    un "What a nice night..."
    "I was silent."
    "And she hugged me and smiled - I could feel it even in the dark."
    un "Do you think we could do something totally crazy yet?"
    "I shifted my gaze to her and she was already unbuttoning her shirt."
    scene black with fade
    play music music_7dl["take_my_hand"] fadein 3
    "She shuddered at every touch as if she'd been electrocuted, and when I found the coveted cleft between her breasts and buried my nose in it, she moaned long and squeezed me so hard that I was afraid for a second that my nose was safe."
    "What she was saying is a separate story. An incoherent babble, interspersed with sighs and sobs."
    "Could I have imagined there could be so much energy in a small, fragile body? Was it realistic to imagine that a quiet, modest girl would turn out to be so passionate in love?"
    un "Ah... Don't stop. Love... Love me."
    un "Go on..."
    "And I went on."
    "The shirts were hanging from the raspberry bushes like frightened birds, and only my shorts and her skirt separated us from the most important moment of our lives, when she suddenly stopped herself."
    un "Look... I don't want to do it like this, on the bare, dirty ground."
    dreamgirl "It's a typical woman's trick to get you to boil state, and then stop!!!"
    me "Naked-dirty? Let's go to the boat then."
    "I wasn't confused."
    "And Lena laughed."
    un "You're a genius!"
    scene black
    with fade2
    "We anchored fifteen meters from the shore, leaving an abyss on all sides-top, bottom, sides."
    "And an energy no longer grounded bubbled and swirled in such monograms under my half-covered eyelids with barely contained desire that I had long ago abandoned sight in favor of tactile sensation."
    "We never put our shirts on, tossing them carelessly on the bow of the dinghy."
    me "Come to me."
    un "Now? Is this going to happen now?"
    dreamgirl "You keep babbling, nothing's going to happen!"
    "I smiled silently, waiting for her to finally get her act together. The water splashed overboard, and in the moonlight her waist-naked figure awoke the most poetic sentiment."
    if alt_day4_un_7dl_hen1:
        un "Like yesterday?"
        me "Yes. Just remember, we're on a boat after all..."
    "She only smiled, pulling off the rest of her clothes, remaining completely naked under the moonlight."
    un "So what's next?"
    me "Come to me."
    "I whispered."
    me "Trust me."
    scene bg ext_island_night with fade
    me "We didn't take headache remedies from Viola..."
    un "I wanted it to be real."
    "She answered, already lying on my shoulder."
    un "Besides, you're allergic to latex."
    me "Babies can spawn after that, remember?"
    dreamgirl "I hope this bug gets patched out in the next version."
    "I wasn't happy with myself. After all, I'm older, control should be my thing."
    un "That's what doesn't scare me. Not at all."
    "She was lying on my chest and looking into my eyes."
    un "If it makes a baby, I'll love it the way I love you."
    me "And if not?"
    un "You can always try again."
    un "How long do you want to try?"
    un "I'm willing to try all my life. Are you?"
    "Her fingers slid mindlessly over my chest."
    "I pulled her against me and touched my lips to her high forehead and let myself close my eyelids."
    "And her fingers immediately traveled downward."
    me "Do you want to do it again?"
    un "Can it be more than one?"
    "I smiled."
    me "You can have exactly as much as you want."
    un "Well, then..."
    un "Then..."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day5_un_7dl_sleeptime:
    if not (loki and (alt_day1_sl_keys_took in (1, 3))):
        scene bg ext_house_of_mt_night_without_light with fade
        play ambience ambience_camp_center_night fadein 1
        play music music_list["a_promise_from_distant_days_v2"] fadein 2
        "We were on our way back to camp when the edge of the sky was gilded by the waking sun."
        "Tired, but pleased with ourselves and each other beyond belief."
        show un smile pioneer with dissolve
        un "Would you like to spend the night at my place?"
        me "I'd love to, but..."
        if alt_day1_sl_keys_took in (1, 3):
            "I had a better idea."
            "I planted a bunch of keys in the palm of my hand."
            me "Let's sleep somewhere else."
            show un laugh pioneer with dspr
            un "You're wonderful!"
            "She gave me a ringing kiss on the nose and dragged me along in search of a cabin on the side."
        else:
            me "Wait for me here.."
            with fade2
            scene bg int_house_of_mt_night2 with dissolve
            "I crept into the cabin, trying not to squeak on the floorboards and looking away from Olga, who was spread out on the bed, throwing off her blanket."
            dreamgirl "Wow! The tanks are already empty, and he's still looking to the side."
            "The keys were found where I expected to find them - on the desk, between the alarm clock and the day planner. The unoccupied cabins lay separately, marked with a pasted-up piece of paper."
            "One of those keys I clawed."
            play sound sfx_open_dooor_campus_2
            scene bg ext_house_of_mt_night_without_light with dissolve
            show un normal pioneer with dissolve
            "Lena humbly waited for me at the entrance. Good girl."
            un "Well?"
            "I showed the key."
            me "A lover's cottage."
            show un laugh pioneer with dspr
            un "You're wonderful"
    scene bg ext_house_of_el_night_7dl with dissolve
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg int_extra_house_7dl
    show un smile pioneer
    with dissolve
    "We unwrapped the roll right there, and, lying on the same bed, we hugged each other and closed our eyes in sync."
    "I didn't have the strength to take stock of the day - so much had this girl rolled off my back."
    "I pulled her against me and, smiling at her almost audible purr, let myself fall asleep."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day5_un_7dl_video:
    scene bg ext_polyana_sunset
    show un normal pioneer
    with dissolve
    un "Do you miss it?"
    "She sat down next to me and put her head on my shoulder."
    me "Not anymore."
    me "Will you tell me what you've been up to?"
    un "Nonsense."
    me "Really?"
    un "Trite, in general - asserting my own right to you..."
    "She mouthed and corrected herself."
    un "I mean... to us."
    me "And?"
    show un smile pioneer with dspr
    un "Failed."
    "She smiled disarmingly."
    un "Miku and Slavya are in the woods, but they'll be here in fifteen minutes - and they're going to tell something to the counselor..."
    me "So what are we sitting around for? Let's get out of here!"
    show un laugh pioneer with dspr
    un "I thought you'd never ask."
    "She pulled me along."
    "Into a land of magical anticipation, reverie, and the almost tangible touch of lips."
    "And the bushes all around looked so comfortable."
    stop ambience fadeout 3
    stop sound_loop fadeout 3
    scene bg ext_path2_night
    show un normal pioneer
    with dissolve
    "It's a pity both she and I turned out to be such snobs, fastidiously turning our noses up at «a-naturairel» in nature."
    me "Are you thinking what I'm thinking?"
    un "I don't know."
    "Lena innocently shrugged it off, which, coupled with her determined gait, looked extremely amusing."
    un "I was thinking about finishing what we started at the club."
    me "Oh, you mean cleaning?"
    show un laugh pioneer with dspr
    un "Ahha. Exactly."
    me "You're not going to tell me exactly what Miku and Slavya are going tell?"
    show un shy pioneer with dspr
    un "You know, I shared a little bit about what we did this afternoon."
    un "And in what way..."
    me "A chatterbox is a spy's find."
    show un smile2 pioneer with dspr
    un "True."
    me "Ture."
    show blinking
    scene bg ext_camp_entrance_night
    with dissolve
    play ambience ambience_camp_center_night fadein 3
    "After breaking through some thickets, we came to the gate."
    "The camp was quiet, reminiscent in some ways of my home metropolis - which is only an hour a day, from four to five in the morning... The most generous time for couples and lonely romantics occupying rooftops."
    scene bg ext_clubs_night with moveoutright
    show un smile pioneer with dspr
    me "Lena, won't they look for us?"
    un "Of course they will. But who's going to find us?"
    me "And if they find us here...?"
    show un sad pioneer with dspr
    un "They won't. Open up quick, I'm freezing already!"
    "With a snort, I turned the key in the padlock and, letting the lady go forward, created the appearance of a locked room."
    $ persistent.sprite_time = "night"
    $ night_time()
    play sound sfx_close_door_clubs_nextroom
    scene bg int_clubs_male2_night_nolight
    show un normal pioneer
    with dissolve
    play music music_7dl["rewind"] fadein 5
    "Gently closing the door behind me, I turned to Lena, about to say something, but..."
    "She was already impossibly close - so close that her hot breath burned my skin, and her hot gaze scorched me like the very candle flame that had lured me - a moth."
    "Ineptly, awkwardly, baring her teeth, but making up for it with all the passion and enthusiasm possible, Lena kissed me on her own accord."
    "And her hands walked where they wanted and did what they wanted, and I was surprised to learn that besides the ribbing, you could get goosebumps all over me just by running cool fingers down my spine."
    "Though maybe it was the fact that all the walls here reeked of unfulfilled desire - our shared desire left over from the day we slept next to each other."
    show un smile2 pioneer with dspr
    un "You're so red..."
    me "What, can you see well in the dark?"
    un "No, it's just that your skin is hot."
    me "And yours is cool. Dead, so it's cool?"
    un "Screw you!"
    "She fought with every button on my shirt, trying to undo it, but either her fingers wouldn't listen or we buttoned it too well - the last two had to be torn off."
    "Compared to what I did to her shirt, it was child's play."
    "The buttons rattled to the floor and rolled in different directions, revealing the weasel's seductive forms."
    "The view was very poor - the light that came in through the window was not enough."
    "But that didn't bother us - I, who was used to living in semi-darkness, was happy with that level of light, and Lena..."
    "She closed her eyes from the moment she dug a kiss into my lips."
    "And she relied entirely on me and her remaining four senses."
    "So I guess you could say we did it the sanctimonious way - with the lights off and our eyes closed."
    $ lp_un += 1
    scene bg int_clubs_male2_night_nolight with fade
    th "If love is joy, happiness, positivity... Why does everyone make love with such serious faces?"
    "It's inappropriate to think of it all of a sudden."
    show blinking
    "I opened my eyes the next time - no one was hugging me with their arms and legs anymore, and Lena, sitting on the table in one of my shirts, was looking at me sternly and unsmilingly."
    scene bg int_clubs_male2_night_nolight
    show un normal pioneer
    with dissolve
    un "We did manage to make it unforgettable after all."
    me "As if we could have done anything differently."
    "I wonder if she's aware that..."
    un "I know."
    me "But why take such a risk?"
    un "Do you mind?"
    me "Nah, don't even think about it."
    "I snorted."
    "It's past the time when I could be embarrassed by a silly question."
    me "You're not getting away from me now."
    show un laugh pioneer with dspr
    un "Like I wanted to do something like that."
    "She laughed."
    show un normal pioneer with dspr
    un "I wanted it to be real. So..."
    me "Real?"
    th "Do you need bed scenes for it to be real?"
    show un serious pioneer with dspr
    un "I believe you. I believe that it's not up to you whether you're here or gone."
    un "Don't blame me for putting away in five days what others put away in years of their lives."
    un "I want to have something left if you..."
    "She was silent."
    "I found her hand in the darkness and squeezed it encouragingly."
    me "As long as anything depends on me, I won't leave you. I swear on everything I can."
    show un normal pioneer with dspr
    un "Where shall we sleep?"
    me "I don't know. Here, right? Or..."
    "I remembered about the keys."
    me "We could take any of the vacant cabins, and make ourselves comfortable there."
    show un smile pioneer with dspr
    un "Good point!"
    "She nodded, gathering our things around the room."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day6_un_7dl_begin:
    scene bg int_extra_house_7dl with dissolve
    show prologue_dream
    play music music_list["timid_girl"] fadein 3
    "I was having a nightmare."
    "I was dreaming about the day before yesterday."
    "It was like I was running around looking for Lena and I couldn't find her anywhere."
    "And even knowing it was just a dream and I could feel her sleeping warmth next to me - even though we woke up one more time - and it was still scary."
    "That warmth served as an anchor, comforting, telling me everything was okay."
    "And when it was gone by the time I finally woke up - I screamed in terror and woke up."
    scene bg int_extra_house_7dl with dissolve
    "Lena wasn't there!"
    "Nowhere? I even looked under my pillow. There wasn't!"
    th "What the..."
    "A scrap of paper in a familiar handwriting caught my attention."
    "{i}Sorry, I'm running away: I need some time to think and be alone. I love you. Me.{/i}"
    me "Be alone? What the fuck is that?"
    "I got up with a groan, feeling how worn out I was yesterday: the lactic acid was breaking my whole body."
    th "Well, when I find the lousy girl... She won't pay me back in kind!"
    dreamgirl "You're hurting the girl again..."
    th "Shouldn't have run away."
    if loki:
        "Although I'm already guessing where she is now."
    "On the table there were some candy, a phone with an open gallery with the last picture being Lena's selfie, and my backpack that came from somewhere."
    th "Oh, shi! It's the second day I can't get a look in there."
    if dr:
        th "Although I remember yesterday the work in the canteen was partly sponsored by the bowels of it."
        th "If you believe the counselor, of course."
    "With a quiet rustle, the absolutely anachronistic plastic «ten» here came apart, revealing a bag of «Start» candies and a number of smaller items."
    "One unopened deck of cards -, one Swiss all-purpose knife. A roll of kapron cord and a bunch of assorted carabiners. Tourist matches, a shapeless piece of lead for sinkers."
    if alt_day_binder != 1:
        "In the flat pocket was a wallet with cash, which I had lost with my coat on the bus, and next to it was my passport and two sets of keys."
    else:
        "In the flat pocket was the familiar bundle of bolts and intercom token."
    "Well, in the change pocket I found another note from Lena:"
    "{i}Where we first got close.{/i}"
    th "Equipment for all occasions... I wonder what these hypothetical «parents» might have sent the kid with sinkers, a knife, and salt?"
    dreamgirl "Don't let your green headache about that: concern yourself better with solving a charade from your shyster."
    me "A hiding place?"
    me "What the hell is this?"
    if loki:
        th "Our beach! The place where she said she was hiding."
    elif herc:
        th "I remember she showed me her artwork in the cabin. Maybe there?"
    else:
        "Lena and I became closer on the first day... As close as possible between people like me and her."
        "I remembered our midnight conversation and smiled quietly."
        th "So she's waiting for me at the square?"
    "The phone was flashing its last pendants of energy in the charging sector, and I seriously considered setting up some kind of homemade device."
    "Realizing that, with my skills in electrical engineering, the best I could do was a detonator for the grenade the phone would turn into, I regretfully gave up on the idea."
    stop music fadeout 3
    return

label alt_day6_un_7dl_search:
    play music music_list["sweet_darkness"] fadein 3
    if dr:
        scene bg ext_square_sunset with dissolve
        play ambience ambience_camp_center_day fadein 3
        th "We got closer... We were never really apart actually."
        th "As soon as we hit on each other on the first day, we..."
        if alt_day_binder != 1:
            th "That's why clubs are off the table - that's where we first saw each other."
        else:
            th "I doubt very much that she was alluding to the bench outside Slavya's house."
        th "So that leaves what? That's right: the square, Genda, and the second bench on the left."
        th "That's where the light from the lantern falls very comfortably, and you can read until the camp is called off."
        th "Of course, I wouldn't have been able to see anything in the dark myself - but Lena had clearly demonstrated that she was a very unusual girl."
        th "And, remembering how she led me after the dance to the infirmary, I realize that for this kind of vision, reading by lantern light is quite comfortable."
        th "Busy thinking, I turned out onto the square, glanced around the left row of benches without catching anyone's eye."
        th "The right..."
        "Lena wasn't here."
        th "Damn."
        th "Think, think, head! I'll buy a carthusis."
        dreamgirl "REAL SHIT?!"
        th "Putting my hand on my foot I promise!"
        dreamgirl "Let's use logic!"
        th "Come on."
        dreamgirl "What was she doing here? Reading?"
        th "And?"
        dreamgirl "And where could she have gotten the book?"
        th "At the library. And what does that have to do with bonding?"
        dreamgirl "That from her point of view it might well be that you became «closer» when you snatched her from under the noses of the Buzzer and her cronies."
        "That makes sense."
        "I had to admit it."
        dreamgirl "That's right. Don't forget, you're wearing a cap."
        "I grinned, and, orienting myself, pointed my feet in the direction of the temple of knowledge."
    else:
        if loki:
            scene bg ext_un_hideout_day_7dl with dissolve
            "Hardly anything could be a more eloquent definition of the word «closer» than what happened here four days ago."
            "I involuntarily smiled as I remembered how spontaneously and naturally we went from being semi-familiar to... what? A couple? Dating?"
            "Whatever. This is where it all happened anyway."
            "Except..."
            "She wasn't here!"
            "She wasn't, that's all."
            "I've combed the cape all over - looked behind every bush, visited our little beach, the campfire glade with the three logs..."
            "Lena was nowhere to be found."
            "Even went to the memorial spot where we... well, I see."
            "To no avail."
            "All the time I was searching, I couldn't get rid of the feeling of staring at my back, but every time I turned around, it was just my hypochondria."
            "Here we go again: the rustle of branches being pushed aside behind me, the tickling sensation between my shoulder blades, and..."
            "No one."
            th "She won't hide from me, will she?"
            th "Or would she?"
            "Some sort of completely unhealthy panic gripped me, and I slammed my fist with all my might into the completely uninvolved trunk of a pine tree."
            "Only to slash my hand."
            "Leaning my back against the rough bark, I closed my eyes."
            th "Where could she be?"
            "Despair gripped me more and more - and at the same time there was absolutely no energy to rush around the unfortunate bark in panic."
            show blink
            "I must have fallen asleep."
            pause(2)
            $ persistent.sprite_time = "day"
            $ day_time()
            hide blink
            show unblink
            "Because the next time I opened my eyes, the sun had reached its zenith and was burning mercilessly."
            "With nothing to eat, I went back to camp."
        else:
            scene bg int_extra_house_7dl with dissolve
        th "It seems that it will be useless to look for her on our own."
        th "We'll try to involve other pioneers."
        th "And we should start with her roommate: who if not Miku to know where Lena might be?."
        scene bg ext_house_of_un_day with dissolve
        play ambience ambience_camp_center_day fadein 3
        "And as I was already putting my hand out to knock, I caught myself thinking that maybe I wasn't doing too well."
        th "Maybe Lena isn't here for objective reasons."
        th "Maybe she does need some time alone."
        dreamgirl "You're a newfound couple."
        dreamgirl "What kind of «alone» can there be? You should count the seconds without each other!"
        "I thought the same."
        "And that's why I kept moving my hand."
        play sound sfx_knock_door7_polite
        th "What if Lena is here? And I'm worried for nothing."
        mi "Come in!"
        "Miku answered."
        play sound sfx_open_dooor_campus_2
        pause(1)
        scene bg int_house_of_un_day with dissolve
        show mi normal pioneer at center with dissolve
        mi "Hi, Senechka, you look depressed. You didn't get much sleep, did you? And Olga Dmitrievna said that you didn't come home last night - you were out all night, weren't you?"
        me "Greetings to the most talented girl in camp."
        "I waved my hand dejectedly."
        mi "You're rambling again."
        "She laughed."
        me "Sort of. Have you seen tour neighbor? I have business with her..."
        show mi surprise pioneer with dspr
        with dspr
        mi "No. She wasn't at the lineup, and she wasn't at breakfast, and then I went to club, to get ready for the concert, and I got caught up."
        me "So you don't know."
        "Well, that's to be expected."
        "If Lena wants to hide, with her intelligence she can hide in such a way that few will be able to find her."
        show mi serious pioneer with dspr
        with dspr
        mi "No. But she will!"
        "The Japanese girl exclaimed."
        me "Is that so? Why?"
        mi "Well, how can you not understand! It's the last day, tradition!"
        show mi upset pioneer with dspr
        mi "Going to a concert, eating a farewell dinner, that's a sacred thing for pioneers!"
        "Miku seemed to know absolutely nothing about her roommate."
        me "Thank you. You've been very helpful."
        scene bg ext_house_of_un_day with dissolve
        "I thanked politely and silently shut the door behind me."
        "Lena will be at the concert because the concert is sacred."
        "That simplicity is worse than theft."
        th "But where could she be in this case?!"
        th "I'll go check at the library - maybe she's hurriedly finishing her cartoons for the wall newspaper..."
    scene bg ext_library_day with moveoutright
    "The library."
    "For as long as I can remember, it is with books that I have the most indelibly warm memories."
    "Truly funny, truly sad - concentrated emotions written in the pen of talented classics rivaled in intensity even my new home."
    "Love to the grave, passion to the gnashing of teeth and shortness of breath, hatred to shivers and bloodshot eyes."
    "And is it any wonder that, compared to such emotions, everything that had happened to me in my life seemed something... something fake."
    "It's like untalented actors playing their parts and being tormented by it themselves and not being able to do anything about it - it's supposed to be like people, right?"
    "One thing I can say in my own defense: I never «acted»  because politeness or rules or who knows what else demanded it."
    "If I felt life was beginning to grow old, I'd change it for a new one."
    "At least in the nuances."
    "Until one day I got bogged down..."
    "But that's a different story. The present one is about a miracle, ordinary, everyday, but no less beautiful for it."
    "This story is about Lena."
    "And so the library becomes a scaffolding no less than the canteen or the beach."
    "This is where we conquered the dragon, where we became truly close to each other, for a moment opening the veil of silence."
    "Just gave in to desire one day and spit on the fact that «no one does that.»"
    "Question or desire? Truth or deed?"
    dreamgirl "You're standing on the doorstep like you're afraid to see her eyes again."
    dreamgirl "Are you feeling guilty about not having good quality sex last night?"
    dreamgirl "That's normal. Statistically, few couples can boast of quality sex, and on average, it doesn't last more than two minutes a week."
    th "Uh... And what can be accomplished in two minutes?"
    dreamgirl "How should I know? You ask me that as if I was the one who gathering statistics."
    th "Well, then don't say anything."
    "I pushed the door."
    stop ambience fadeout 3
    scene bg int_library_day with dissolve
    play ambience ambience_library_day fadein 3
    play music music_list["she_is_kind"] fadein 3
    "Nothing has changed here since my last visit."
    if alt_day4_me_neu_transit == '':
        "The same books on the shelves - I nodded contentedly, seeing the Encyclopedia's spines burning with washed gold - the same posters with aggressive propaganda, the same list of Marxism-Leninism classics."
    else:
        "The same books on the shelves, the same posters with aggressive propaganda, the same list of classics of Marxism-Leninism."
    "Even Zhenya was in place - except she looked a lot less aggressive than usual."
    th "Maybe she is sick?"
    show mz normal pioneer with dissolve
    mz "Don't stand in the doorway - come in."
    "She muttered."
    "Not a «hello», of course, but compared to our last conversation, clear progress!"
    me "Hello."
    "I obediently walked over to the table."
    mz "Listen, not for service, but for friendship."
    if alt_day4_me_neu_transit == '':
        extend " Since you and I are friends."
    "There was a whiff of «volunteers» in the air."
    "That she will going to try to put me down was obvious, but to what end?"
    me "Yes?"
    mz "Help me move the table: I can't do it alone."
    me "And the magic word?"
    show mz bukal pioneer with dspr
    mz "Is it hard for you?"
    "I sighed."
    me "You're a boo, Zhenya. {w}All right, let's move it."
    "We grabbed her desk, the most ordinary desk with a nightstand and a tabletop just below the floor, allowing us to stretch out our legs."
    me "One... two... got it!"
    "Looks like Zhenya didn't think to unload the books - or whatever it was - first."
    "What's the matter, even the cactus, managing to look miserable, was still standing at my edge in a pot."
    "So in addition to carrying capacity I had to show off my equilibrium skills."
    "Fortunately, not for long - a couple of meters later Zhenya nodded contentedly, and we brought the table back to sinful ground."
    me "That's it?"
    mz "Not really. Your eyes are strong, look for the small metal screw on the floor."
    me "How small?"
    "Stupidly I clarified, as if I had a whole cluster of iron under my feet."
    mz "Very small!"
    "Zhenya cut off."
    mz "From the glasses."
    "I finally understood why I thought she looked unusual. Her glasses!"
    "And if it had been about anyone else, I could have sworn it was an unconscious signal of attention. Well, as it usually happens if a girl wears glasses and takes them off in your presence..."
    "But Zhenya..."
    "On the same table I discerned a pair of glasses with a bent shackle."
    th "That's it."
    me "Is there a magnet?"
    mz "On the side of the bureau."
    "With my hands and eyes searching for such a small detail would not have been too sensible - however, considering that even under Zhenya's desk it was practically sterile..."
    "A couple of minutes of driving the round black toroid magnet over the floor - and the search was successful: the fugitive was located, captured, and handed to the owner..."
    "All this I did as if in third person - detached and unconcerned."
    "Oh, I was well aware of Murphy's laws - never show you're in a hurry, they'll harness you for two days to sort it out."
    "Under no circumstances must you show that you are engaged in a very important quest - otherwise every cross-eyed man will have a quest for you of no lesser caliber than saving the galaxy."
    th "Perhaps if I obediently do everything she demands, I'll finally get a few questions answered - and either be guided to the right path by giving a clue, or let go and get back to my search."
    mz "Fine! Give it to me."
    "With a confidence that showed considerable experience, Zhenya put the shackle back in place and in a few turns secured it."
    "And immediately she put on her glasses."
    show mz bukal glasses pioneer with dspr
    "Turning back into a Buzzer!"
    mz "Put the table in its place. On three: one, two..."
    "Ten more seconds of balancing cacti, tea cups, and desk lamps, and the table is in place."
    "Hallelujah!"
    mz "That's nice. Now I can work again."
    me "Finally."
    th "Hopefully now I can work a little too."
    mz "What's your... Semyon!"
    "She called out."
    th "You f..."
    me "What?"
    show mz shy glasses pioneer with dspr
    mz "Look, I don't know how to say thank you, but I have to thank you somehow."
    dreamgirl "Just stop grabbing my hands, you goggle-eyed misunderstanding!"
    "My inner voice screamed in a way that made my temples ring."
    mz "Would you like a cup of tea? I know you haven't had breakfast."
    me "Tea? What's the tea with?"
    mz "With this."
    "She pouted."
    th "And with the pinky finger off. I don't have time!"
    me "No, I won't have tea with a spoon as a snack."
    "I politely declined and finally reached the editorial office of the wall newspaper...{nw}"
    play sound sfx_open_door_clubs_2
    pause(1)
    scene bg int_editorial_day_7dl with dissolve
    extend " Only to make sure that it is empty."
    dreamgirl "Yeah... You could have taken your time."
    scene bg int_library_day with dissolve
    "On my way back to Zhenya's house, I decided to check just in case:"
    me "Tell me, did Lena come by today?"
    show mz normal glasses pioneer at center with dissolve
    mz "No, only Electronik came by today - for some reason he was all red, muttering something about the last day and the last chance."
    mz "There's an event going on at camp, and I don't know about it?"
    th "Yep. An event. It's called «how to tell a girl you like her if she doesn't think of herself as a girl». Performed for the first time, by E. Syroezhkin."
    mz "Ah, who am I asking. You must have been up half an hour ago."
    me "It's nothing like that!"
    show mz laugh glasses pioneer with dspr
    mz "Look at your face."
    "I think I've been admitted to the higher circles of the local Illuminati: the Buzzer has risked showing me another one of her emotions."
    "Laughter."
    th "Wow, I thought she couldn't even laugh."
    dreamgirl "You keep this up, you'll be dating her before you know it."
    th "Holy crap!"
    show mz normal glasses pioneer with dspr
    mz "Before you look for Lena, go wash your face, Tristan."
    me "Is it that bad?"
    mz "I wouldn't go out with you."
    dreamgirl "And who asked?"
    hide mz with dissolve
    "The conversation was over, and I left in English."
    th "I don't want the Buzzer to start riding me."
    $ persistent.sprite_time = "day"
    $ day_time()
    scene bg ext_library_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    "If this keeps up, it'll soon get to the point where I'll have to sit in the cabin around the clock."
    th "Although... There's Olga Dmitrievna - and she doesn't mind having a little laugh at my expense, either."
    dreamgirl "Hello, offended! Moscow on the phone."
    th "What?"
    dreamgirl "Make up your mind, what's more important to you now - to keep your dignity or to find your beloved?"
    th "As if you can't combine the two."
    "I snorted."
    play sound sfx_7dl["eat_horn"] fadein 1
    dreamgirl "You can. But first..."
    th "Looking for Lena - no lunches until then."
    dreamgirl "Will you convince her of that?"
    th "Who?"
    show sl smile pioneer with dissolve
    sl "Hello, Semyon!"
    "Slavya smiled."
    sl "So, how did it go yesterday?"
    me "Begone."
    stop music fadeout 5
    "I muttered, cautiously pulling away."
    sl "Are you sulking? At what?"
    me "Because some people like to stick their noses into things that aren't theirs, I guess..."
    "I shrugged indifferently."
    sl "That's exactly my question."
    me "I don't even want to know what that could mean."
    me "What do you want?"
    show sl shy pioneer with dspr
    sl "That's okay. I was on my way to pick up Zhenya for lunch. Will you come with us?"
    me "Would it make any difference if I said no?"
    "I politely clarified."
    show sl laugh pioneer with dspr
    sl "No!"
    me "For some reason I thought so."
    hide sl with dissolve
    "Slavya disappeared behind the library door and, two minutes later, she was back - already in the company of the Buzzer."
    show sl smile pioneer at cleft
    show mz normal glasses pioneer at cright
    with dissolve
    sl "Let's go! We're in for the tastiest lunch of the shift!"
    me "Why would that be?"
    sl "It's a farewell!"
    me "I thought it was going to be a farewell supper."
    sl "Dinner, too!"
    "The activist cut us off and dragged us toward the canteen."
    stop sound fadeout 3
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day6_un_7dl_dinner:
    play music music_list["silhouette_in_sunset"] fadein 3
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 5
    "To my delight, the far seat in the corner was vacant."
    "I sat down and tried to make a «don't get in, I'll kill» face."
    "Just to sit alone and think.{w} You can't educate an established man for a week in paradise: his cockroaches will come out sooner or later anyway."
    "That's the way it is here - I didn't want to see, hear or perceive anyone."
    show sl normal pioneer at center
    with dissolve
    sl "Hello again! Can I?"
    me "No..."
    "Without much hope I replied."
    sl "And I'm going to sit down anyway!"
    me "I'm not surprised."
    show sl surprise pioneer at center
    with dspr
    sl "What happened to you?"
    me "I don't want to talk about it."
    me "Leave me alone."
    sl "As long as you're in my squad, I'm responsible for you!"
    "Any way you look at it, she was right. Which means I'm going to have to stick my shamed ego deep down and try to interact with her."
    th "Uh-huh, duels were forbidden by the highest edict, but..."
    "Slavyana's promised «incredibly tasty» lunch turned out to be Ukrainian-style hodgepodge and pilaf."
    "I would have called this lunch «death of the pancreas», but that it was really tasty was impossible to deny."
    me "Did we miss much last night?"
    "I finally inquired, pushing my plate aside."
    show sl normal pioneer at center
    with dspr
    sl "Well, no. Miku annoyed everyone, so Olga Dmitrievna took the guitar."
    show sl shy pioneer with dspr
    sl "And then I left."
    me "Left?!"
    sl "Yes, I needed to be alone."
    th "Everybody around here needs to be alone all the time."
    th "It's like an epidemic of individualism."
    me "Must have been a guilty conscience?"
    "I guessed. What the hell if she does have one?"
    show sl smile pioneer at center
    with dspr
    sl "Well you say that too!"
    "She laughed."
    sl "It's just this camp... I've been coming here a long time."
    "I grinned meaningfully, not taking my eyes off the pilaf."
    "And Slavya went on, as if finding an appreciative listener in my face:"
    show sl shy pioneer with dspr
    sl "But I'm out of circulation and won't be able to come here next year."
    me "Do you want to?"
    sl "Very much..."
    "With a vague longing she whispered."
    sl "My heart is here."
    th "So is mine."
    th "The individual cosmos - a rescue package, living water scarring unhealed wounds that hurt far more than physical wounds."
    "Green-eyed cosmos."
    th "I wish the whole silly story about a nearly thirty year old loser being embedded in a pioneer body and getting his second chance had really been made up."
    th "New life? A new job? A care for opportunities that are not only ahead of us, but also within reach?"
    "A new sense of existence."
    "I want to stay here by her side."
    "I want to take her with me."
    "I want to open my eyes to a world where she lives parallel to me."
    th "Don't they all have anything else to do?"
    "It's like they were all in superposition, and nothing was going on before I got here."
    me "Haven't you tried anything else?"
    "I quipped."
    show sl normal pioneer at center
    with dspr
    sl "Well... Tonight is the concert - by the way, Olga Dmitrievna told me to make sure you were there."
    sl "There's a farewell disco in the evening."
    sl "Turnout is mandatory for everyone without exception."
    me "Do you know where I can find Lena?"
    show sl surprise pioneer at center
    with dspr
    sl "Weren't you two together?"
    me "We were together. But she said she had to think about something, wrote me a note to look for her..."
    "I spread my arms."
    me "That's it, now I'm looking for her."
    show sl normal pioneer at center
    with dspr
    sl "It's no use. If Lena doesn't want anyone to find her, they won't find her."
    sl "It's not the first time she's been here - she's got a knack for it. Even I can't find her."
    me "You don't have to."
    "I whispered."
    sl "You should, by the way. She's being treated sympathetically - there's no reason to hide."
    sl "But she prefers to decide for herself. So she decided for you."
    me "So have you."
    sl "So have I."
    "Slavya nodded and stood up."
    sl "See you at the concert. I hope you two will be found by then."
    hide sl with dissolve
    "I was really hoping for that outcome, too."
    "It seemed very important to spend the last day that could rightfully be called ours together."
    th "We both deserved it, didn't we?"
    if loki:
        "Mending the hole where my heart was supposed to be - I needed Lena the most right now."
        "It might not work out in the distant and overcast future - but here and now the years that had passed, the ones I had tried to scrape myself off the floor - seemed unimportant."
        "Here and now I lived."
        th "She is my third chance to live my life, since music and space didn't work out."
        th "To live, not to exist."
        th "So I'll run till night if I have to - but I'll find her!"
    stop ambience fadeout 2
    scene bg ext_dining_hall_away_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    "After successfully passing the absent-minded counselor looking under my feet, I trickled outside."
    th "So I looked for her on the camp grounds-anywhere I could."
    th "The fact that I wasn't able to find her tells me either that she doesn't want me to find her, or that it's time to switch to looking outside the grounds."
    "Deciding not to spoil my already gloomy mood, I decided to go with the second postulate and covered my eyes to see where outside the territory the girl might be."
    "Only the sand pit came to mind."
    th "Though what could she be doing there?"
    th "Go to sprinkle lingonberries goodbye? Without me? That doesn't sound right."
    dreamgirl "Don't you brood, come on, let's go look for it!"
    "On your mark..."
    stop music fadeout 5
    stop ambience fadeout 2
    return

label alt_day6_un_7dl_career:
    scene bg ext_path_day with dissolve
    "The whole world is saturated with you."
    "Memories."
    show un serious pioneer at right
    pause(0.3)
    hide un with dissolve
    th "You - as my personal Tyler Durden - exist only when I do not exist."
    th "And that's why our romance turned out to be so improbably kind and spikeless."
    "The sun disappeared behind the clouds - so another fit of despair seized me when neither at the quarry itself nor in the lingonberry forest surrounding it could I find Lena."
    "The day was indeed rapidly turning overcast, if it's going to repeat a yesterday's rain."
    "I wouldn't care for it now, though."
    scene bg ext_sandpit_day_7dl with dissolve
    "I walked up to the sandy bluff and kicked the pebble, watching it fly vertically and land with an audible slap on the sand, which was not yet dry."
    play music music_list["dance_of_fireflies"] fadein 3
    "And, obeying some impulse, I pulled a knife out of my shorts pocket - the same one my hypothetical «parents» had sent me."
    "Found a convenient pine tree that stood far enough away to avoid attracting attention, unfolded the blade and set to work."
    "In the obliquely and crookedly carved heart fit her name and my initials. Hooliganism, of course, is silly and wrong, but..."
    "Maybe one day I'll come back here, and..."
    scene cg d5_un_carrier_7dl
    pause(.2)
    scene bg ext_sandpit_day_7dl
    with fade
    "My attention was drawn to the inscription on a nearby tree."
    "As I got closer, I grinned."
    th "Well, of course."
    "A crookedly carved heart with the name «Lena» on it."
    th "The one, huh? The one that didn't make it through the contest?"
    th "I wonder if he hugged her like that, kissed her? And did she squint and smile at him and be all his?"
    th "And what should have been my all - important possession, was she giving it to him? An outsider?"
    dreamgirl "Don't get yourself worked up. First of all, you didn't exist in her life by then."
    dreamgirl "And secondly... Maybe there's another explanation."
    dreamgirl "Maybe it was written to another Lena."
    th "And you believe that? Or maybe yesterday's revelations have slipped your mind?"
    dreamgirl "In any case, now is not the time or the reason to be jealous."
    dreamgirl "Especially since..."
    "Another heart with Lena's name caught my eye, then Alisa's, Zhenya's... Interested, I followed someone's memory milestones, reading someone's awkward, crookedly carved confessions."
    "And came out almost to the very edge of the pit - but on the other side."
    "Lena wasn't here, so it was time to head back to camp."
    "The only thing left to decide was where to continue my search."
    "With that in mind, I headed toward the camp."
    stop music fadeout 5
    th "Perhaps it makes sense to question Dvachevskaya - as she defended Lena so diligently, perhaps she knows her a little better than everyone else and could be useful to me."
    th "Makes sense. Let's try."
    return

label alt_day6_un_7dl_music_club:
    play music music_list["everyday_theme"] fadein 5
    scene bg ext_house_of_dv_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    show us normal pioneer at center with dissolve
    "A conspicuous cottage with straight slopes instead of the usual barrels, distinguished by the fact that there was no bench beside it, and the glass of the front door was hung with a Jolly Roger."
    "The place itself seemed to shout that trouble dwelt here."
    "After convincing myself that I had enough trouble for one day, I was about to decide to go up and knock when I was hailed from behind."
    show us normal pioneer with dspr
    us "Hey! What are you doing here?"
    me "Hi, Ulyana."
    "I forced a smile."
    me "I'm here to see Alisa."
    show us grin pioneer with dspr
    us "What, are you sick of Lenka already?"
    "The little one giggled."
    me "How can you say that?! I'm trying to find her."
    me "By the way, maybe you know something?"
    show us normal pioneer with dspr
    us "About Lena?"
    us "I know she goes somewhere every year where no one can find her."
    show us smile pioneer with dspr
    us "Although you could have followed up, since you care so much about her!"
    me "I'll ask Alisa just in case..."
    us "Alisa isn't here. She's rehearsing at Miku's club."
    me "Rehearsing?"
    show us grin pioneer with dspr
    us "Aha! There's a concert tonight, so she's preparing a performance."
    us "They're kind of friends. Ask them!"
    me "Gran merci!"
    hide us with moveoutright
    "I turned around and walked as fast as I could toward the music club."
    "Ulyana shouted something, but I couldn't hear it."
    scene bg ext_musclub_day with dissolve
    "The more my mood deteriorated, the more the weather frowned."
    "As if to answer my mood!"
    "I might have thought so had I not remembered yesterday and waking up in the arms of my dear creature."
    "Why, you ask, would I have been grieving at that moment?"
    "And yet the weather turned bad. Yes, so much so that in the clothes in which Lena ducked to my bed, she was determined not to be driven back!"
    th "But now we're on the same wavelength as the world around us."
    th "Maybe yesterday was the final measuring of us - me and this camp?"
    "After all, this place clearly exists for a reason."
    "Even considering that I certainly don't act as a point of reference and the beginning of coordinates, I have a role clearly defined."
    "And that just means that someone else's will is behind my miraculous movement here, and it's not the will of chance at all!"
    dreamgirl "Super conclusion! What makes you think you have any part to play here, I wonder?"
    th "From the fact that I got to the set? All those hearts on the quarry, the abuse from Slavya, and a number of other oddities - they are due just to the fact that instead of blindly following the role, I..."
    stop ambience fadeout 2
    play sound sfx_open_door_2
    pause(1)
    scene bg int_musclub_day with dissolve
    play ambience ambience_music_club_day fadein 3
    "Alisa was gone. Lena wasn't there."
    "But Miku was."
    "Yeah, in terms of taking the mind out of the brain, this chatterbox could replace them both."
    "Especially since the latter aren't particularly chatty."
    show mi smile pioneer at center with dissolve
    "She was scribbling something on the sheet music stand, but instantly turned away when she heard the door creak and smiled dazzlingly at me."
    mi "Hello there, Senechka! How's your search going?"
    me "Honestly, not good. I thought I'd catch Alisa here - maybe she knows something."
    mi "Good idea! They're friends, who better than Alisa..."
    "I looked around the room eloquently."
    show mi normal pioneer with dspr
    mi "Well yeah, she's not here, she went to the stage to rock that acoustic."
    "I was just about to turn around..."
    if 'music' in list_clubs_7dl:
        mi "Senechka, will you help me?"
        me "Help? How?"
        mi "I have to take the stand for the xylophone: I can't lift it by myself - it's very heavy, and you're so strong."
        me "Oh, yeah. And who's the xylophone player?"
        mi "Well, Electronik. He's got some performance of his own - he's got percussion, triangles, timpani, cymbals."
        me "it must be Mike Oldfield's fame that's bothering him."
        show mi laugh pioneer with dspr
        mi "That's right!"
        "The Japanese girl laughed."
        mi "And how do you know Oldfield?"
        me "I'm a meloman... I know a lot of music."
        "I don't have to tell her I have a couple of tracks by this artist on my player. Although «Let there be light» is a little too much for Electronik to handle - you have to coordinate a whole orchestra there."
        "But under the leadership of our charming artistic director, I think we could manage - Alisa on guitar, Elektronik on xylophones-metallophones, Slavya alone will replace the choir, and I would...{nw}"
        if loki:
            extend " Since I'm healthy for now{nw}"
        extend " Stand up on the brass - trumpet or baritone."
        "And, of course, Miku herself for the synthesizer - I saw a derelict «Heuner» somewhere."
        if loki:
            th "Actually, my dear, it's not a royal affair to drag all those stands for Electronik."
            th "But for music..."
        me "Give me the stand, I'll help you carry it."
        mi "Wait a minute: I'm getting ready for the concert."
        hide mi with moveoutleft
        "She hid somewhere behind the piano and rustled something there."
        mi "Why don't you want to do a concert? I can pick you something dressy if you want."
        "It made me cringe."
        me "Holy crap!"
        show mi laugh voca with moveinleft
        mi "You don't have to answer."
        "The Japanese girl laughed."
        hide mi with dissolve
        "She turned her back to me and pointed to the clasp."
        mi "Zip it up."
        "I blushed."
        th "And then there's Olga Dmitrievna... Or Lena? I don't even know which option scares me more?"
        dreamgirl "Slavya... Our paladin without fear and dill."
        th "Don't mention her!"
        "I obediently took hold of the doggie's thin tongue and, trying to keep contact to a minimum, gently pulled it up."
        mi "What are you digging in there?"
        "She yanked her head irritably."
        mi "Just zip it up - it's hard for me to reach."
        "This time I acted more confident and handled the unruly dog faster."
        mi "Thank you!"
        "She adjusted her dress to her chest and danced around her axis:"
        show mi normal voca with dissolve
        mi "It's okay, isn't it? I don't talk to Lena much..."
        "And I stood there, red as a cancer, most afraid that the one I'd been looking for all morning would find me herself..."
        dreamgirl "Yes, you and I have a talent for getting into situations."
        show mi smile voca with dspr
        mi "But I appreciate how caring and considerate you are."
        me "I... ahem..."
        "Stuck up."
        "But, coping with my voice, I, still a little hoarse, protested."
        me "I'm not caring, and..."
        mi "You supported her, didn't forget a word she said, and now you're running all over camp looking for her."
        show mi grin voca with dspr
        mi "Will you invite me to the wedding?"
        me "What wedding..."
        "I'm blushed again."
        mi "And I'm certainly very embarrassed to distract you from your quest, but I can't do it myself."
        show mi upset voca with dspr
        mi "Do you even like the dress?"
        "She glanced at me from under her fluffy lashes - no other reason than that it was specially tinted in honor of such an occasion."
        "The dress was the perfect length, in my opinion - but from the point of view of the local puritans..."
        dreamgirl "If you were a candy, I'd eat you."
        me "Awesome!"
        "Honestly I replied."
        me "But isn't it a little short?"
        show mi serious voca with dspr
        mi "I {b}don't{/b} care! {w}They wrapped me up on the first day! {w}Today is my day, my concert! And like hell I'm going to change."
        me "I must say, you've mastered Russian idioms to perfection."
        show mi smile voca with dspr
        mi "Thank you!"
        mi "So you like the dress?"
        me "Are you kidding? It's gorgeous!"
        show mi normal voca with dspr
        mi "Perfect. Then I'm ready."
    else:
        show mi smile pioneer with dspr
        mi "I'd ask for your help, but since you're not in my club, I can't trust you, hee-hee!"
        me "It's a little late for that..."
        show mi normal pioneer with dspr
        mi "You had other interests there, as I can see, so it's useless - I just wanted to remind you that we have a concert, and I'd really like you to listen to my song at least!"
        me "Actually, I have to look for Lena..."
        "Gloomily I replied."
        show mi serious pioneer with dspr
        mi "Everyone says to you in one voice: she's not missing, she's hiding! {w}Senecka, you can't find her: she's the best at hiding!"
        "Miku amusedly turned up her nose in pride at her friend."
        me "What am I going to do now?"
        show mi happy pioneer with dspr
        mi "To brighten up the wait with a concert, of course! {w} I've prepared a very special song!"
        me "What's your song?"
        "I was involuntarily interested."
        mi "It's called «Outer Science» - I've wanted to sing it for a long time!"
        me "Wait... I know that song! But it's about..."
        show mi grin pioneer close with dspr
        "I wanted to continue, but Miku gagged me without too much tenderness."
        mi "Well no one here speaks Japanese anyway, hee-hee-hee! {w} It's a good song."
        me "Since you say so... When's your turn again?"
        show mi shy pioneer with dspr
        mi "I'm opening the concert!"
        me "Oh, that's it. It's a deal, I'll be there."
    stop ambience fadeout 2
    return

label alt_day6_un_7dl_concert:
    scene bg ext_stage_normal_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    play music music_7dl["nobodys_secret"] fadein 3
    "Any search for and expectation of a dear one is divided into several stages, familiar to anyone who has been in this situation at least once."
    "First you worry and don't know what to think."
    "Then you get mad at the runaway."
    "Then you call morgues and hospitals, wishing on an X, on cracks in the floor and clouds in the sky that if it works there, it will work here too - and everything will be okay."
    "And finally depression - when nothing changes, despite all the effort you put in."
    "You sit with your arms crossed over your chest and stare disbelievingly at the ceiling - how can it be?! How! After all, the classic said that nothing is impossible - you just have to make the effort!!!"
    "One feels cheated: you are practically destroyed, leisurely drifting face downstream, letting go of the swift run of time."
    "And at last you hear the doorbell ring."
    show dv normal pioneer far with dissolve
    "Alisa took her place at the very edge of the stage and leisurely plucked the strings, honing her playing to perfection."
    if alt_day4_un_7dl_ducks:
        "Yeah, you don't have to say the same thing five hundred times to feel confident."
        "You can't lose your talent."
    if 'music' in list_clubs_7dl:
        "As I unloaded my rack to a monster drum kit standing nearby, I walked over to Alisa."
    else:
        "I winked goodbye to Miku, promising that I would definitely watch her performance, and walked over to Alisa."
    show dv normal pioneer with dissolve
    me "Hello, Alisa."
    "Without answering, she nodded, continuing to pluck the strings."
    me "Lena and I missed each other somewhere. I'm running around, looking for her."
    show dv smile pioneer with dspr
    "Alisa swatted the strings with her palm and blew her bangs out of her eyes."
    "I noticed she was smiling."
    "But not angrily or arrogantly, in her vein, but somehow... Understanding, or something?"
    dv "What, did your Juliette run away from you?"
    me "Not that she ran away..."
    dv "Hiding, then."
    "Alisa smiled serenely."
    dv "Lena might, she is like that."
    me "And where to look for her now?"
    dv "Nowhere. Ulyana said she runs off like that every shift."
    dv "She'll be back in the evening."
    me "But that's not normal! A pioneer girl runs away for a whole day, and nobody even cares?"
    show dv sad pioneer with dspr
    dv "Who's cow is mooing now."
    me "What?"
    if loki and (alt_day1_sl_keys_took in (1, 3)):
        dv "Where were you all day yesterday? Just showed up at the bonfire."
        th "As if I tell you!"
        dv "Not much difference for me: yesterday you two were gone all day - today her alone."
    elif dr and ('nwsppr' in list_clubs_7dl):
        dv "What you heard."
        dv "Where were you all day yesterday?"
        dv "The counselor was looking for you, by the way."
        me "Well..."
        dv "Hell."
    else:
        dv "Nevermind."
    dv "Your Juliet will come back - she's not going anywhere."
    dv "Relax and wait."
    me "But how?! What if she's there..."
    show dv normal pioneer with dspr
    dv "I tell you, relax. Lena knows how to take care of herself better than any of us."
    dv "Did you know that her father works for the police? He taught her a thing or two about standing up for herself. You don't need to know more than that."
    th "Exactly, but I know that you, Dvachevskaya, are useless and I'm wasting my time here."
    hide dv with dissolve
    th "How useless were Slavya, Miku, Zhenya, Ulyana... I'm sure if I wanted to ask the counselor about it, she wouldn't be able to say anything either."
    th "And here she is, by the way."
    show mt angry pioneer far with dissolve
    pause(1)
    show mt normal pioneer far with dspr
    "The counselor frowned when she saw me at the stage, but, after a moment, she nodded hello and pointed to our seats with a hint."
    "The hint was clear: if one Semyon wasn't at the concert, he would be given a lavish funeral at the house's expense."
    hide mt
    scene bg ext_stage_normal_day
    with dissolve
    "In the absence of alternatives, I took the back seats assigned to the senior squads and sulked in anticipation of the concert."
    th "Okay, I'll watch the opening of the concert - I promised Miku - and I'll keep looking!"
    "I consoled myself."
    dreamgirl "You've been looking for her since noon... And now it's almost four o'clock."
    dreamgirl "I don't think anything will change."
    th "Negative thinking. Stop it."
    dreamgirl "Because you're a loser."
    th "Is that how you help?"
    stop music fadeout 4
    dreamgirl "I'm not helping losers."
    "The image broadcast to my brain could be interpreted as a resentful turn away."
    th "What a nightmare. I am incapable of negotiating even with my own intuition."
    play music music_7dl["tellyourworld"] fadein 3
    "Meanwhile, the seats were filling up, and Miku burst onto the stage, causing a synchronized exhale from the male section of the audience."
    "If they knew what she was going to sing about, though..."
    "But who cares when the girl is wearing {b}that{/b} dress."
    "She greeted those present loudly, lamented that the shift was ending, and how much she didn't want to leave."
    "But since we have to say good-bye anyway... Let it be at least memorable!"
    "She spun around on her axis, and nodded to Alisa sitting at the console - the phono started at full volume."
    "A song about what a man deserves, what he gets rewarded with."
    "From fifth to tenth, I sang along to Miku, eliciting surprised looks from the pioneers sitting next to me."
    th "Well, yeah, why?! I used to listen to those songs at home!"
    "I tried my best to pretend that I was very passionate about the concert."
    "Very much!"
    "And I think I succeeded!"
    "After Miku, there were some dolts from the third squad with some kind of humorous verse, and Olga got a little bored."
    if alt_day4_un_7dl_ducks:
        "And when those were replaced by my charges from the day before yesterday, who never seemed to remove their masks of exasperation from their young faces, it was pathetic to look at Olga."
    "At last she could not stand it."
    "Trying to move as quietly as possible, she slid sideways off the bench and, looking around now and then, went somewhere."
    th "That's right, go. Go."
    stop music fadeout 5
    "For peace of mind, I waited a few more minutes and followed the counselor upstairs."
    "I paid my debt to this camp in full, I looked at Miku's performance - there she was, writhing in the role of compere in the wings."
    "And..."
    show mt angry pioneer with dspr
    mt "Semyon, where are you going? The concert isn't over yet!"
    "She seems to be very upset by my unauthorized attempt - see how she clenched her fist!"
    "Only one. Because in the second one she was clutching a bag - judging by the most attractive aroma coming out of it - with a dry ration instead of a lunch."
    me "I was just stretching my legs..."
    "I mumbled, looking away diligently."
    me "They're stiff."
    show mt normal pioneer with dspr
    mt "Forget about that! You'll stretch them after the concert.  March back to your seat."
    me "Answer one question, and I'll do as you say."
    mt "If you mean where your date went, I don't know. Satisfied?"
    play music music_list["doomed_to_be_defeated"] fadein 3
    me "Are you all out of your mind?!" with vpunch
    "I yelled, not paying attention to the people around me."
    me "What kind of counselor are you that doesn't know where her pioneers are?!"
    show mt feared pioneer with dspr
    mt "Semyon, I understand your frustration, but..."
    me "You don't understand anything! Or your responsibility doesn't bother you?"
    me "So I'll go to the boss if I have to!"
    "And then Olga immediately calmed down."
    show mt normal pioneer with dspr
    mt "You will, after the concert."
    mt "In the meantime, march to your seat."
    if loki:
        me "No way."
        "The only thing that could stop me now would be a tranquilizer shot or..."
        "I cast a glance at the rising activist."
        show sl angry pioneer at right with dspr
        th "Yes, or Slavya."
        th "But who would give her that opportunity."
        me "Are you all sick or something? Or you stubbornly just don't care?!"
        "I shouted and, not knowing the road, rushed off somewhere, spurred on by rage."
        hide mt with easeoutleft
        hide sl with easeoutright
        "In a straight line, of course, Slavya would have caught up with me."
        "Twisted and would have delivered me to the counselor."
        "But she didn't have the incentive that moved me."
        "And emotional motives should never be underestimated."
        "..."
        stop ambience fadeout 2
        scene bg ext_boathouse_day
        with dissolve
        play ambience ambience_boat_station_day fadein 3
        with dissolve
        "My God, how I ran!"
        "I've never run like that in my life!"
        "Not even as a kid, when I used to rob the neighborhood apple orchards a little bit, had I ever had to run away like that."
        "I felt as if a lot depended on the speed of my legs."
        "And so I ran."
        "I ran until my blood boiled in my veins and my lungs, poisoned by excess oxygen, intoxicated my head."
        stop music fadeout 9
        play sound sfx_boat_impact
        "And then I rolled over the sand."
        "Realizing I was hopelessly late for something."
        "But for what?"
        with fade2
        "When I had caught my breath and was able to perceive my surroundings, I realized that my feet had taken me to the boathouse."
        th "Trust your instincts?"
        th "Maybe they remember something?"
        "The instincts were generally right: there was another «unifying» memory associated with the pier, a dance, an affirmation of madness - both of them."
        "Except that..."
        "Lena wasn't here either."
        "I slammed my fists helplessly against the sand."
        "For a second I was scared - what if... What if..."
        "The images came into my head, from drowning to fleeing the camp, but I fought them off as best I could."
        "But in this battle, the forces are always unequal."
        "The chandra took hold of me with renewed vigor, and when the degree of melancholy in my blood had reached the necessary point, I rose from the sand and wandered up the pontoon - to where we had hugged three days ago, hiding in the moonlight."
        "There, where..."
        "My attention was drawn to a piece of paper taped to a medium metal tube. If you don't know where to look, you won't find it."
        "Familiar beautiful handwriting."
        "I took a deep breath."
        "And unwrapped the note."
        un "{i}Hooray! You found it! So you really do care, don't you?{/i}"
        th "Of course I fucking care! Does that really require any further proof."
        un "{i}I'm on our cape.{/i}"
        un "{i}Me{/i}"
        me "But I've been checking there since this morning!"
        un "{i}P.S.: Since you're bumming around out there anyway, grab me something from supper, okay?{/i}"
        me "Thanks for asking my opinion!"
        "I replied wryly to the empty air, carefully tearing the note into little shreds and letting them go to the wind."
        "I was inclined to ignore the postscriptums and simply drag the fugitive into the canteen - where she could have a proper meal."
        play sound sfx_7dl["eat_horn"] fadein 1
        "But the horn has put everything in its place."
        "With a sigh, I staggered into the canteen, wondering what I could get for a hungry girl."
    else:
        "I wanted to get out and run, but then Slavya arrived."
        show sl serious pioneer at left with dissolve
        "Resistance was useless."
        "Sometimes this girl could extinguish a conflict simply by frowning or sighing."
        "A killer combination of leader's charisma, beauty, and strong fists."
        th "Strange that they didn't become friends with Dvachevskaya. Their methods of peace and goodness are very similar."
        mt "Excuse me!"
        "Loudly Olga Dmitrievna apologized."
        mt "Today was a difficult day for everyone - we were all overexcited. But I won't let anyone ruin our celebration!"
        mt "Please continue!"
        "Miku nodded, and the phonogram resumed its sound."
        mt "Semyon, don't make me angry, please."
        "The counselor asked lazily."
        mt "Calm down and sit, or something might happen."
        me "I don't care about you."
        "I muttered."
        me "What kind of a counselor doesn't know where her pioneer girl goes."
        mt "Well, I'm sorry, I have an agreement with the pioneer girl. As for you..."
        "She hesitated."
        mt "Let's put you where you'll do the least harm - between me and Slavya."
        stop music fadeout 3
        th "Uh..."
        hide mt
        hide sl
        with dissolve
        "For some time now I've preferred to have something immovable between me and the blonde - whether it was her too affectionate gaze, or I don't know what else..."
        "She also sat down so... awkwardly!"
        "She pressed her foot against my..."
        th "Shit. Shit!"
        "I tried to move away, but Olga Dmitrievna was already sitting next, and the alternative to sitting on her neck was only patience."
        th "I am surrounded by sick people."
        th "One blatantly shirks her own duties and for some reason blames it on me!"
        th "And another has a complete lack of personal space when communicating."
        "The activist herself didn't react to my grimaces: she was all there on stage, where Alisa was strumming, humming something from Yanka Diaghileva in a husky voice."
        "And I was sitting hunched over, curled up like a virgin girl on a first date."
        "And if it weren't for Slavya's complete enthusiasm for the concert, I would have thought she was doing it on purpose."
        "Thank Random, the agony didn't last very long."
        "After Alisa came the Electronik with his killer solo on xylophone and timpani, followed by a choreographic quartet with Russian folk dances, and..."
        "Slavya rose from her seat!"
        dreamgirl "Pick your jaw up off the floor."
        "The inner voice advised it."
        dreamgirl "As if I never knew the activist could sing."
        th "Yes, I did! But to sing like that..."
        "In a sundress with a kokoshnik and scarlet boots, Slavya embodied what at all times was called Russian beauty."
        "And when she, brushing aside Miku with her microphones, phonograms, and amplifiers, stepped to the middle of the stage and, chest full of air, melancholy sang:"
        sl "The pretty maiden fell in love, fell in love with a boy, sighed and sighed..."
        "I couldn't stand it and started clapping to the beat."
        "I did not react to the heads turning in my direction - just as I did not react to Olga Dmitrievna squirming in displeasure."
        "I made a bet that Communism was a religion."
        "All these youthful collective games, the feeling of being involved in something big and undoubtedly important..."
        "And my palms clap, and my foot swats by itself, beating out the rhythm."
        "And ten seconds later, the kids from the front rows join me, then some counselor wants to join in, she encourages the pioneers, and..."
        "That's how I am... two-faced - instead of running around looking for my one, precious one, I sit and commune with the energy of the masses."
        "And so when Slavya returned and sat down again almost on top of me - I didn't move away any more - it really didn't seem to mean anything to her."
        "So we hide our intolerance to other people's touch and tolerate it, especially since we have a little less than half an hour before dinner."
    stop sound fadeout 3
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day6_un_7dl_supper:
    scene bg ext_dining_hall_away_sunset with dissolve
    play ambience ambience_camp_center_day fadein 3
    th "The bun the counselor loaned me went down my stomach like into a bottomless pit."
    th "And if I'm not going to do whale songs when I find Lena, I should be fully fueled!"
    stop ambience fadeout 2
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg int_dining_hall_people_sunset_7dl with dissolve
    play ambience ambience_dining_hall_full fadein 3
    "Exactly."
    if loki:
        "Dinner passed my attention, but I took a couple of the tangy ones they had on display at the food counter. I was very fond of that citrus hybrid myself, and the girls were always squeamish about tangerines."
        "It would have been nice to steal some buns or something to drink, but... Ah, screw it!"
        th "If we get that hungry, we'll audit the supplies! I'll lend some candy, for example."
        "After encouraging myself in this way, I looked around and, making sure no one was watching me, slipped out of the dining room."
    else:
        "Dinner had no taste whatsoever."
        "I don't know what the local cooks had planned to surprise the pioneers with, but I chewed melancholy on some gruel with a delightful cardboard flavor, paying no attention to taste or consistency."
        if alt_day_binder != 1:
            "I suppose if Ulyana decided to diversify my diet with Chinese food, I wouldn't notice."
        "My thoughts were far away - they were speculatively scouring the camp and surroundings for the hundredth time, looking for the one person who matters."
        stop ambience fadeout 2
        scene bg int_dining_hall_sunset with dissolve
        "I went so deep into a trance that I returned to objective reality only when the ringing silence startled me with the contrasting sound."
        "With a sigh, I got up and headed aimlessly to wander around the camp."
        if herc:
            th "I'll check out our beach."
        else:
            th "I'll check out the beach."
        th "Maybe she's in there?"
        "After making sure no one was watching me, I headed toward the pier."
    stop ambience fadeout 6
    return

label alt_day6_un_7dl_catapult:
    scene bg ext_boathouse_sunset_7dl with dissolve
    play ambience ambience_boat_station_day fadein 6
    "A lethargic sleep of dozens of useless years, and, like screaming through your teeth, but no one on Earth hears you."
    "I wanted to kill - and the «myself» option was seen as acceptable."
    "But instead I am a living primate of self-preservation instinct over expediency, scurrying along the beach, kicking the bumps that turn up."
    sl "Semyon?"
    "The voice is familiar, but so unlovely!"
    "I grimaced as if I'd eaten a lemon, but I can't try to run away from her now, can I?"
    "And turned back to the blonde with displeasure."
    show sl smile pioneer with dissolve
    sl "Here I found you."
    th "Wonderful. Can I go now and perform the ritual excarnation?"
    sl "Why did you run off from supper? I wanted to talk to you about something."
    me "About what?"
    show sl upset pioneer with dspr
    "The girl looked around restlessly."
    sl "Can we go somewhere where no one can hear us?"
    me "No. I'm not going anywhere with you."
    show sl smile2 pioneer with dspr
    sl "I won't eat you, don't be afraid. It's just that the information I have for you is not for other people's ears."
    me "I want to take a walk somewhere. I have business there."
    me "So if it's urgent, you can keep me company."
    "The activist nodded and joined me, trying to keep up with me."
    "In her left hand, in marked contrast to her smart uniform, hung a gray sack of sod with something heavy in it."
    "I instantly regretted my suggestion, but it didn't seem very decent to chase the hindrance away with a stick."
    th "Maybe she'll peel of herself?"
    dreamgirl "What is she?, three inches of dirt on your skin to peel of?"
    th "Be patient. She's in the mood to scratch her tongue."
    stop ambience fadeout 2
    scene bg ext_un_hideout_day_7dl with dissolve
    sl "Well, here will be fine."
    "I stopped and looked at Slavya questioningly."
    me "Speak."
    show sl shy pioneer with dissolve
    sl "I..."
    "She started, and then stopped."
    me "Amazing."
    "Without hiding sarcasm, I admired."
    me "If that's all you wanted to talk about, before the dance then."
    sl "Wait a minute!"
    "She caught me with her free hand."
    "I looked curiously at her fingers clutching my forearm, and watched until, embarrassed, she let me go."
    "She's not really going to scream and grab my hands in a «I can't do it without you, and you're not mine» kind of way, is she?"
    me "I'm waiting, I'm waiting. I'm tired already."
    sl "I don't feel comfortable asking you for favors."
    sl "And you, like Moscow, would not believe the tears - but I'm really very worried about Lena."
    th "Those worries were especially evident not so long ago, at dinner."
    "But my famous self-controt didn't let me down this time either."
    me "How does this relate to each other?"
    "I politely clarified."
    me "All those bookish turns, the concern for Lena and the favors."
    show sl sad pioneer with dspr
    sl "Here's the thing... If you're going to run away..."
    "She miffed."
    sl "Can I come with you?"
    show sl smile pioneer with dspr
    sl "Please."
    show sl normal pioneer with dspr
    "She wanted to smile, but immediately gave up."
    sl "This is extremely important to me."
    "The logic was elusive, but by some unknown instinct I knew that we were talking about a little more than just trying to leave the camp territory."
    "And it was this reluctance to call things by their proper names that convinced me better than a dozen minutes of persuasion and irresistible evidence."
    "She very carefully placed the bag on the ground and turned to me."
    sl "Lena had already had a bad affair once last year, and was very good at hiding the identity of her chosen one."
    sl "But it ended with him dumping her."
    sl "And she owes it to a miracle that I was there to do something."
    show sl sad pioneer with dspr
    me "Okay, I'm jealous. What's next?"
    show sl serious pioneer with dspr
    sl "Semyon."
    "That impossible girl gave me that mature look."
    sl "The time for jokes is over."
    sl "I'd rather walk you out of here and show you the way than let your story go too far."
    dreamgirl "Oopsie."
    "Thoughtfully stretched out the inner voice."
    dreamgirl "Looks like our broomstick fool is a little more competent than I thought."
    "I shrugged."
    me "How would you know if our story went far or not so far?"
    "I asked unkindly ."
    sl "How can I explain it to you..."
    show sl normal pioneer with dspr
    sl "«Far» will be when the one whose rightful possession you are will give up on you."
    sl "Now you still have an opportunity to remove yourself before you do too much damage to those around you."
    me "Remove?"
    "I cast the last stone."
    sl "To your {w}world."
    "The word has been spoken."
    me "So you..."
    if alt_day_binder != 1:
        sl "I witnessed the nightmare you're guilty of."
    else:
        me "Okay, I get it, you want to send me back and supervise delivery."
        me "Where's your flying saucer or whatever it is you're flying between worlds."
    "And flying a moment later felt her close, close, very close."
    sl "All you have to do is - wish for it."
    sl "Realize there's nothing holding you here - and let yourself go."
    me "What about Lena, then?"
    sl "She'll stay alive. If you care even the slightest bit about her fate..."
    me "I do care."
    "I interrupted her."
    me "Why can't I stay near her?"
    sl "Because you can't."
    "Calmly she replied."
    show sl angry pioneer with dspr
    sl "Listen to yourself: you know you can't promise even that!"
    sl "Let yourself go!"
    "I've suffered that, too; I've given up."
    "Because that same million-dollar feeling told me: this blonde was right, she was right."
    "If I stay, I'll only make things worse for everybody."
    if karma < 0:
        "And I let myself go..."
        $ alt_day_catapult = True
    menu:
        "And I let myself go":
            $ alt_day_catapult = True
        "I don't know...":
            $ alt_day6_un_7dl_agreed = True
            $ lp_un -= 10
            show sl angry pioneer with dspr
            sl "You already tried it. Last year."
            sl "You already know how it ended."
            sl "Don't you really care that much about the consequences?"
            menu:
                "No, I care":
                    show sl normal pioneer with dspr
                    sl "In that case..."
                    sl "Let's go."
                    $ alt_day_catapult = True
                "Home? But Lena...":
                    $ lp_un += 3
                    "I hesitated."
                    me "I don't want to leave Lena, I don't want to hurt her."
                    sl "You..."
                    play sound sfx_hiding_in_bush
                    show sl normal pioneer at right with dspr
                    "There was a rustling sound from behind, and Lena appeared out of the bushes."
                    show un cry pioneer at left with moveinleft
                    "Her eyes were wet."
                    me "I want to stay with her. I'm willing to risk it."
                    "Slavya bit her lip."
                    show sl sad pioneer with dspr
                    sl "You're crazy. You're bloody selfish."
                    "Her eyes gleamed and, moving like a poorly assembled puppet, she gathered the bag from the sand, turned around and..."
                    show sl cry pioneer far with dspr
                    "For a second, I thought I heard a sobbing in the clear solution of the noise of the surf."
                    hide sl with dissolve
                    "And it was just me and Lena."
                    un "So you..."
                    "I shook my head:"
                    me "She was so desperate to help you."
                    show un normal pioneer at center with move
                    if loki:
                        me "Even told me about your affair last year."
                        "Lena flinched:"
                        un "And you?"
                        me "And me, I was jealous."
                        "I confessed."
                        show un smile pioneer with dspr
                        un "You're a dummie..."
                        "The girl visibly relaxed and immediately asked:"
                        un "Did you bring me anything?"
                        "I gave her a tangy and sat down on the log next to her."
                        un "Delicious!"
                        "Quickly peeling one fruit, she instantly devoured half and handed me the other."
                        un "Would you like one?"
                        me "No, thank you."
                        "I smiled."
                        un "Well, suit yourself."
                        "Like all good things in this life, the tangis ran out disastrously fast, and Lena rested her head on my shoulder."
                    else:
                        un "Still haven't found my note, huh?"
                        me "What note?"
                        un "Never mind. A pity you didn't."
                        "She sat down on one of the three logs surrounding the fire pit and pulled me along."
                    un "Look what you've done."
                    "She said pitifully."
                    un "You know how much I missed you!"
                    me "I missed you even more!"
                    me "After all, it wasn't me who ran away."
                    show un smile pioneer with dspr
                    un "I'm sorry. I had my reasons."
                    "She pressed tighter against me and closed her eyes."
                    show blink
        "I'm willing to take a risk":
            sl "You realize you're being selfish, don't you?"
            sl "You can't promise anything..."
            me "Sometimes you just have to go crazy."
            "I confessed."
            me "And with Lena it's like that all the time - the risk is there, but I'm willing to take it."
            sl "I promised I wouldn't get involved if things went too far."
            "She hid her face in her hands for a few minutes."
            sl "But it looks like things have {i}already{/i} gone too far."
            sl "Good luck to you."
            "With a diligent look away, she picked up the bag from the sand and, turning around, set off along the edge of the beach."
            hide sl with dissolve
            "Her shoulders were trembling small for some reason."
            "And behind me I heard someone sobbing in tune."
            "And slowly and slowly I turned around."
            show un sorrow pioneer with dissolve
            "Behind my back, Lena wiped her eyes."
            me "Hi."
            "She nodded hesitantly, frozen."
            "And then, throwing herself on my chest, she burst into tears."
            me "Shh, shh, it's okay, it's okay."
            "I led her to a comfortable log, where I sat her down."
            "It took a few more minutes of exhortation and stroking for the sobs to subside."
            "Eventually I didn't notice my own eyes begin to close."
            scene cg d5_un_sleep
            with dissolve
            $ lp_un += 5
            "It's been too much of a wet day."
            "I put my arm around the girl's waist and held her lightly against me."
            me "I missed you so much."
            un "Me too."
            show blink
            un "Very..."
    if alt_day_catapult:
        "It occurred to me that now, instead of looking for Lena and spending time with her, I would simply run away."
        "But Slavya's logic was ironclad, irresistible, and it hit home."
        "What's much worse, she was completely consistent with what I had always known underneath all along:"
        th "If I leave, it would be better for everyone."
        th "Better." with vpunch
        show blink
        "I closed my eyes."
        $ persistent.sprite_time = "prolog"
        $ prolog_time()
        "Either reality swam or it was just tears, but for a second I suddenly stopped seeing the forest, the river, and the sun overhead."
        if loki:
            play music "<to 52.94>" + music_7dl["herc_death"] fadein 5
            show blink with dissolve
            scene bg ext_winterpark_7dl
            pause(1.5)
            "We were thrown back to the beginning of the story."
            "Back where the fairy tale girl took me to dreamland."
            "{i}The Snow Queen kissed Kai once more, and he forgot both Gerda and Grandma and all the pets.{/i}"
            "And all was right, and the perfect icy features became a light that cut the already ice-covered eyes, and the carmine-red lips - generous handfuls of exhaled dream - on the snowy field."
            "Her kiss was icy and reached all the way to my heart, which already refused to beat."
            "Slavya won."
            "Lena will live."
            "And Loki is sentenced to death by Asgard."
            show prologue_dream
            "I smiled, not paying attention to the figure in the stupid pioneer uniform that was wandering around in the periphery of my vision."
            show blink
            "And closed my eyes."
        elif herc:
            play music "<to 52.94>" + music_7dl["herc_death"] fadein 5
            scene bg int_store_7dl with fade
            "{i}The poems, in which every line, were bitter with thy beauty.{/i}"
            "The moment I realized that I had chosen all the limits of expectation and elasticity of time - I knew I had reached my goal."
            "At least one thing I could really be proud of had been accomplished."
            "The only problem is that I can't be proud of anything else."
            "For I'm dead already - and not in a figurative sense."
            show prologue_dream
            "The lead ball pierced the moment that had stretched for far too long and found its place in my forehead."
            "The leaden indifferent tear of the frozen St. Petersburg sky."
            play sound sfx_7dl["makarych"] fadein 0
            scene black with fade
            play sound sfx_bodyfall_1
        else:
            scene black with fade
            $ volume(0.5, 'music')
            scene bg intro_xx with dissolve
            stop ambience fadeout 2
            play sound_loop sfx_bus_interior_moving fadein 4
            show prologue_dream
            "Instead, the bus engine rumbled in my ears, and the gray hulk of the metropolis stretched outside the window."
            sl "Perhaps now you've done the best thing in your life."
            show prologue_dream
            "Slavi's calm voice came from somewhere on the side."
            sl "You wouldn't be proud of it."
            scene bg intro_xx with flash
            show sl cry pioneer with dspr
            sl "But at least Lena will live. And maybe one day she'll meet a really decent young man."
            sl "Not a world-jumper."
            "We plopped down on the icy seat of the LIAZ. Me - and still clutching my hand, the never-existing Slavya."
            show sl sad pioneer with dspr
            sl "That's it."
            "She patted me on the shoulder and stood up."
            sl "Looks like this is my stop."
            "Across the street from the sign next to the ubiquitous Bill's lit up four neon circles depicting a stylized cat's paw."
            "Vet Clinic, it said in a smaller font at the bottom."
            hide sl with dissolve
            "And I was left alone."
            "Just like at the beginning of the story."
            "Pulling out of the bus stop, the bus began to climb the hump of the Volodar Bridge."
            "Because I belong to my loneliness, because only a tumbleweed like me could once fall into a current capable of tossing you in another time."
            "Which means there's a lot more truth in Slavya's words than she thinks."
            scene black with fade2
            "So I wasn't too surprised when the bus broke through the railings of the bridge and plunged down into the black icy water."
            play sound sfx_shoulder_dive_water
        scene gameover with flash
        play sound sfx_7dl["aunl"]
        $ sdl_persistent_inc("alt_lamp")
        show acm_logo_va_lamp with moveinright:
            pos (1600, 1020)
        pause(7.4)
        return
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day6_un_7dl_dance:
    scene bg ext_un_hideout_day_7dl
    show unblink
    "I think we fell asleep, because when I opened my eyes, I spent a long time trying to figure out where I was and what was wrong with me."
    scene cg d5_un_sleep
    with dissolve
    play ambience ambience_boat_station_night fadein 3
    "And then there's this impenetrable southern night."
    "Lena stirred sleepily on my shoulder."
    un "Mmmm... Slept well. Wasn't I heavy?"
    me "No. I..."
    scene bg ext_un_hideout_night_7dl
    show un smile pioneer
    with dissolve
    "I was slowly getting used to the darkness, and soon I could make out her features."
    "Lena was sitting there, smiling peacefully."
    un "Hello."
    un "Can we not go? Let's sit here..."
    me "What are you saying! It's a farewell disco!"
    me "Where else will we get a chance to have an experience!"
    un "I've had enough."
    "The tsarevna pouted, capriciously."
    me "Oh, no! I want to see you in a dress, hugging and dancing."
    me "Do this little thing for me."
    un "All right."
    "Rising from the log, the girl held out her hand to me and helped me up."
    un "Dancing then."
    stop ambience fadeout 3
    play music music_list["lightness"] fadein 5
    scene anim_square_party with dissolve
    "The clock showed ten minutes to eleven, the peak time when the fast dancers are already firmly occupying the water fountains."
    "And the slower dancers are already releasing the brakes little by little: pressing a little closer while spinning, saying a little more daring things..."
    if 'music' in list_clubs_7dl:
        "And as if to mark the last thought, the host changed the tune to a slow one, and Miku jumped up to me:"
        show mi upset dress with dspr
        mi "Oh, Lenochka, I'm going to steal your cavalier for one dance, may I?"
        "She gibbered."
        mi "I promise to bring him back safe and sound, even unscratched."
        me "But we just got here..."
        "I tried to raise my voice."
        mi "That's good!"
        "Without listening to anyone's objections, the active Japanese girl dragged me to the dance floor."
        show mi normal dress with dspr
        mi "You know, in Japan, slow dancing is a whole choreography."
        "She took me to the center of the dance floor and held me close to her, fixing one arm with hers and nestling the other one somewhere palpably below my waist."
        scene cg d3_mi_dance_close_7dl at zenterright
        with dissolve
        if alt_day4_un_7dl_ducks:
            "I dutifully let her abuse me - after all, after all we'd been through together, it was okay to let her take some liberties."
        else:
            "And I endured. What else could I do?"
            dreamgirl "It's so painful and scary when you get squeezed by a pretty girl like our Hatsune, isn't it?"
        mi "And we have this as a dance. Not as a stomping around."
        mi "One good thing about it is that it's convenient enough for both chatting and squeezing."
        me "What part are you in?"
        "I couldn't resist asking."
        mi "I'm - just here!"
        "She bit her lip and shot her eyes."
        mi "Though I like the idea of rubbing you."
        scene cg d3_mi_dance_afar_7dl
        with dissolve
        "I blushed, eliciting a silver chime of a girl's laughter."
        me "What? But..."
        mi "Relax. I'm just kidding."
        "Was it just me, or did she snuggle a little closer than the rules of the dance require?"
        me "Miku, you're too close."
        "I whispered."
        "You can't tell if she's joking or if she's serious."
        mi "Too close?"
        me "Snuggle any closer, and we'll be asked out of the dance for immoral behavior."
        "The Japanese girl pouted and pulled back, and I finally remembered how to breathe and sucked in air with a whistle."
        dreamgirl "Rape on the dance floor. Practically a plot for a rock ballad."
        th "Mock harder."
        dreamgirl "Although no. Considering you're the victim of molestation - this would be more appropriate for whiny emo bands like The Used."
        "At one turn I caught Lena's gaze."
        "She wagged her finger at me, though her eyes were laughing."
        mi "Thanks, by the way, for keeping your promise. I heard you sing along."
        "I blushed again."
        me "I just know the words, that's all."
        mi "I wonder how?"
        me "Well..."
        "Miku was quiet for a while, gathering her thoughts."
        mi "Your voice isn't the worst, by the way. Have you thought about doing music? I could patronize you."
        th "And then we seamlessly move on to the number exchange."
        dreamgirl "And explaining to a live, current girl the reasons for this exchange."
        "I wondered."
        th "On the other hand, if I stick around, some kind of connection wouldn't be out of place."
        "So I nodded in agreement."
        me "Come on."
        me "I'll text you the number, we'll call each other sometime."
        mi "Deal!"
        scene anim_square_party
        show mi normal dress at cright
        show un normal dress at cleft
        with dissolve
        "The music ended, and Miku convoyed me to Lena."
        mi "Here. Handing over, safe and sound."
        show un smile dress with dspr
        un "A little wrinkled, though."
        "Lena muttered, smiling."
        hide mi
        show un smile dress at center
        with dissolve
        "Luckily, Miku didn't hear that, as she jumped back onto the floor, waving her arms."
    else:
        "We got there just in time - as the host was playing a record of a slow song."
        play music music_list["raindrops"] fadein 3
        show un normal dress with dspr
        "Lena looked at me sideways, clearly hinting that she didn't mind..."
        me "May I ask you to dance?"
        "I held out my hand to her."
        show un smile dress with dspr
        un "You may!"
        "She accepted my hand and allowed herself to be led away."
        scene cg d3_un_dance with dissolve
        "We were in that happy, candy-coated, bouquet-like state when you just have to be together, smoothing over rough edges and sharp edges, lapping it up, selflessly taking advantage of the anesthesia of falling in love."
        "The great age of compromise, when you do something just because you can do it - but not for your own sake."
        "And if we'd had at least a couple of weeks more time..."
        "We were separated by two layers of tissue, but the sensation of living skin contact was so strong in the memory that even here it seemed that we had turned our nervous systems into one."
        un "What are you quiet about?"
        "Lena whispered in my ear."
        me "About you."
        "In tone, I replied."
        un "Specifically?"
        th "Well, my dear girl, good is not enough for the man - he wants the best."
        th "It's not enough for me to be with you here and now: I also need assurances that it won't end in the near future."
        me "I saw your selfies on my phone, they were funny."
        un "Selfies?"
        me "When a person takes a picture of themselves. But you'd better take a picture of yourself with a piece of paper and a phone, just in case."
        un "Don't worry, there's no way I'm letting us get lost."
        th "I wish I had at least a modicum of your confidence, honey."
        if alt_day4_me_neu_transit == '':
            me "What do you think of our memories together?"
            me "I could have sworn we hadn't met before."
            un "B-but..."
            me "What?"
            un "No, nothing. But these memories don't seem fake to me - there's so much in them."
            "Her cheeks turned pink in the light of the garlands in the trees."
            un "Especially... these moments..."
            me "Which ones?"
            un "Well... These!"
            me "Can you tell me which «these» ones you mean?"
            "Lena blushed like she probably hasn't blushed since day one."
            un "Intimacy. I mean..."
            me "Oh... That's what you mean.{w} I'm sorry for my cluelessness."
            un "It's okay. It's just that the body remembers, and the real experience didn't happen - it's like a split personality."
            me "Now I've had the experience."
            un "Yeah... And I'll say it's a lot better than the memories."
        show blink
        "It was a little awkward to kiss in front of the whole dance floor, but I didn't care about the rules of decorum or the attention of others."
        pause(1)
        scene anim_square_party
        show dv smile dress far at fleft
        show unblink
        "And when I opened my eyes, stared at Dvachevskaya dancing."
        show el normal pioneer far at left behind dv with dissolve
        "That in itself would have been surprising enough, but what was shocking was that none other than Electronik danced with her!"
        show dv soft_smile dress far with dspr
        "She intercepted my gaze and winked."
        hide dv
        hide el
        with dissolve
        show cs grin at fright
        "Viola winked, too, as she made her way between the pioneers."
        hide cs with dissolve
        show mt smile dress far at center with dspr
        show ba smile uniform at fright behind mt with dissolve
        "His embarrassed gaze jumped further to Olga Dmitrievna smiling and Sanich hugging her around the waist,"
        hide mt
        hide ba
        with dissolve
        show mi normal dress at right
        extend " to a smiling Miku."
        hide mi with dissolve
        show sl smile dress far  at fleft
        "Slavya, standing behind the turntables, nodded and turned away."
        hide sl with dissolve
        "And I couldn't shake the feeling that I was in some kind of happy ending, that the frame was about to slam backstage and the credits would float across the screen."
        "The tune ended, and we went back to our bench."
    stop music fadeout 5
    scene cg d3_disco with dissolve
    "People were having so much fun, it was like there would never be a tomorrow!"
    play music music_list["farewell_to_the_past_full"] fadein 3
    "And you can't blame them for that."
    "Pretty soon the summer will be over, they'll go to town, they'll go back to school - and it'll be coming of age, and the state will softly remind them that it's time to make their own way in life."
    dreamgirl "There's nothing else for you to do. Go ask a girl to dance again."
    dreamgirl "The unwritten rules of ballroom dancing require you to dance with the lady you brought at least once, and preferably more. So do it."
    th "I'd be right happy to."
    scene cg d3_un_dance with fade
    "There was a second dance, and a third, until the camp called it quits."
    "And Lena and I were still sitting here, on our favorite bench."
    scene cg d6_un_evening_0_7dl
    with dissolve
    "And kept quiet."
    "How wonderful it is, after all, when you don't have to talk to a person at all."
    "When you can just sit next to them and not be embarrassed."
    "Just - silent - next to each other."
    scene cg d6_un_evening_0_1_7dl
    with dissolve
    "I glanced at Lena, who was leaning back and admiring the night sky."
    scene stars
    with dissolve
    if alt_day4_me_neu_transit == '':
        un "How beautiful it is. The sky."
        "She smiled dreamily."
        un "I can't believe you volunteered to give it up."
        me "We didn't give it up."
        me "What happened was what's called progression - the savage was given a Kalashnikov assault rifle instead of a stick. The technological level was raised, but the cultural level remained at the level of the early twentieth century."
        un "Do you think it's time for mankind to grow up?"
        scene cg d6_un_evening_0_2_7dl
        with dissolve
        "She smiled quietly and moved her palm, lying on the bench, toward mine."
        me "At least a little."
        "I nodded."
        me "When entering the universe, you should wipe your feet. Otherwise you might get kicked out."
        th "We, humanity, are at that adolescent stage where we can both exalt ourselves and cripple ourselves."
        th "And so it is inevitable that there will be kinks - all those things that break a single person are symptoms of the pubertal stage of humanity as a whole."
        "And whether humanity, when it grows up, will become human, or turn into a hermit, a boor, or a selfish cynic, depends only on ourselves."
        dreamgirl "How amazingly your thoughts have changed these days."
        dreamgirl "What about your whining and complaining?"
        th "I've just changed. That's all."
    else:
        "A few days ago, it would have been completely different."
        "I'd be sitting next to her, shaking with an all-burning desire to put my hands on her shoulders, to hold her close to me."
        "Just wanting her to be a little more relaxed and comfortable around me."
        "And agonizing over the fact that I don't dare."
        "And now..."
        "What has changed?"
        "Said?"
        "Done?"
        me "I won't talk nonsense about the stars."
        scene cg d6_un_evening_0_2_7dl
        with dissolve
        un "Is that so?"
        me "No, I'll just go there one day instead."
        un "That's a good dream."
        me "It's not a dream."
        "I shook my head."
        me "It's a plan-determination."
        un "What a determined young man..."
        "It suddenly occurred to me that if it hadn't been for that overheard conversation at the cabin, we wouldn't be sitting like this, together."
        "And a chill ran down my spine at the feeling that somewhere in another universe a certain Semyon was sitting all alone on the bench."
        "And I felt so sorry for him that I hid the sadness behind a silly remark:"
        me "Hold on to me, there's more to come."
        "Lena remained silent, though the mute question hung in the air."
        "Unfamiliar alien stars circled above us like this."
        "And in the western part, which was still albeit barely visible, but poured with burgundy, you could see three stars fancifully frozen against each other."
        "One was bigger and was at the bottom."
        "Two smaller."
        me "Look how funny they're stacked up."
        un "Yes."
        "Lena got excited."
        "Like a head with ears. It's so funny."
        dreamgirl "You yourself... head with ears."
        "Disappointedly dropped the inner voice."
        me "These are the windows of the house."
        me "The universe is our home. And in any house someone is waiting for someone."
    scene cg d6_un_evening_2
    with dissolve
    un "Well said."
    "The palm moved even closer, and..."
    scene cg d6_un_evening_3_7dl
    with dissolve
    extend " covered my fingers."
    "I nodded."
    if alt_day4_me_neu_transit == '':
        me "It's just a pity it's not working yet. Neither mankind, nor I."
        un "But you said yourself the day before yesterday about a new chance."
        me "And you were skeptical about waiting for me on Earth."
    else:
        me "But no one is waiting for me."
        un "What do you mean no one? What about me?"
        me "What about you?"
        un "Do you want me to wait for you?"
        if loki:
            me "Besides, space is just a magical dream, like a fairy tale."
            me "In fact, I'm afraid of even heights, let alone skydiving or trying to get beyond the earth's atmosphere."
        un "That doesn't mean I won't support you."
        if alt_day_binder == 1:
            un "No matter what happens to you, no matter where you are, I will always be at your side."
            un "It was obvious to me back then, at Slavya's cabin."
            "I smiled:"
            me "She'd been pissing me off all week, and she turned out to be..."
            un "Yes. Our guardian angel."
        elif (counter_sl_7dl >= 1):
            un "Your successes are my successes, too."
            un "I want to be proud of you."
            "She blushed a little."
            un "Such a selfish wish."
        else:
            un "It's very important to me that you be happy - living with that battered young man who stared at me at the gate must be such a drag!"
            un "It's a good thing I was wrong in my estimation."
        scene stars
        with dissolve
        if alt_day_binder == 1:
            "I smiled and put my arm around the girl's shoulders."
        else:
            "I didn't dissuade her, I just pulled her to me, hugging her shoulders."
        th "Mine."
        "The girl purred softly and snuggled into me."
        un "No. You are mine."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day6_un_7dl_sleeptime:
    play ambience ambience_camp_center_night fadein 1
    play music music_list["a_promise_from_distant_days_v2"] fadein 2
    scene bg ext_house_of_el_night_7dl with dissolve
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg int_extra_house_7dl
    show un smile pioneer
    with dissolve
    "Last day at camp."
    "Last dance, last supper."
    "It was like everything was screaming - Remember! Take it with you in your memory! Every note, every grunge, every millimeter."
    "Smells, colors, sounds, tastes - accumulate it all for years to come, looking up above the heads of fidgeting passersby, soaked in summer in every cell of the body."
    "And most importantly, of course, her."
    "Lena."
    "If we don't get to see each other after camp, if things don't work out, I want to at least remember her."
    show un normal pioneer with dspr
    me "What are you thinking, sunshine?"
    "I inquired."
    "Yes, a silly question, and yes, I repeat it every day at least once."
    "But it's interesting, isn't it!"
    un "I'm thinking about what we did yesterday."
    un "And why did we do that yesterday."
    "We're on the same bed - it's customary for me and her to be on the left side of the door."
    me "Really? What did we do?"
    dreamgirl "Right, turn on the fool."
    me "I mean, we went all the way, of course, but-"
    un "That's exactly the «but» I want to talk about."
    "She pulled a memorable gray paper bag out of her pocket."
    me "Product number two? But where did you..."
    "She put her finger on my lips."
    show un serious pioneer with dspr
    un "Shut."
    th "Yeah."
    th "That's how it starts. First they shut me up, then they ride me."
    dreamgirl "Don't whine, huh? You're distracting me from the movie."
    un "I know it's a little late to drink borjomi after our madness last night, but if I have my mother's gynecology, we have to try and try harder before there are consequences."
    me "You mean all those stupid innuendos from Slavya..."
    un "Were pure bluff."
    un "There are no guarantees, of course. But the chance itself..."
    me "So you want me to..."
    show un shy pioneer with dspr
    un "I want to."
    "She flipped the bag on her hand."
    show un serious pioneer with dspr
    un "So that this crap wouldn't be in our lives."
    "The product flew somewhere in the corner, and I involuntarily followed its flight."
    "And when I returned my gaze to Lena - you could see such a bunch of stuff in her eyes!"
    "Waiting, caring, tenderness, affection... And - desire."
    un "Come to me."
    "She whispered, grabbing me by the lapels of my collar, pulling me against her and kissing me hotly."
    un "Come..."
    scene black
    with fade2
    "Clothes flew to the floor, and the heated air scorched the walls of the cabin when we finally became one."
    "Lena was close, very close: she was near, outside, and around, and I couldn't get enough of her - until she, protesting, interrupted our marathon."
    un "Save some for after camp, too, okay?"
    "She grumbled, falling asleep."
    "And I lay there for a few more minutes, leaning on my elbow, studying her facial features with my gaze."
    "Until, at last, fall asleep."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day7_un_7dl_begin:
    scene black with dissolve
    play music music_list["orchid"] fadein 3
    pause(2)
    scene bg int_sam_house_clean_7dl with fade
    "Evil morning to you, hateful den, evil morning to you, hateful gray city outside the window."
    "We hate each other long, habitually, and for nothing."
    "Client's uptime is over sixty hours, which is how long I haven't left the apartment."
    "I was awakened by a distinctive ICQ's «oh-oh». It's amazing, I haven't used the client in years, and I still can't get around to tearing it down. Who could possibly want me there?"
    "Grunting, I gathered myself out of bed and, squinting into my left eye, tried to reconsider the eye-punching monitor light."
    scene black
    with fade3
    stop sound_loop
    pause(3)
    show laptop_7dl
    show laptop_un_epilogue
    if loki:
        show laptop_un_epilogue_loki
    elif herc:
        show laptop_un_epilogue_herc
    else:
        show laptop_un_epilogue_dr
    with dissolve
    play sound_loop sfx_keyboard_mouse_computer_noise fadein 3
    "The recoil hurt my pupils, but I was able to make out the title of the message."
    "The rare seven-digit number that I learned by heart in my day, stronger than my own name and even my phone number."
    if alt_day_binder != 1:
        th "Or is it five digits?"
        "I tried to look closely and count the numbers, but they were floating in my eyes."
    if loki:
        "Ksana?"
        "What the hell does she want?"
        "Our story is over, over!"
        "We cursed each other and parted like ships at sea. Why get involved in my life again?"
    elif herc:
        th "Ex. {w}What the hell does she want?"
        "After she got married either because she got knocked up or to annoy me, we haven't exchanged a word."
        "Does she really need me for something? Or is she writing out of boredom again?"
        "It's always boring to sit at home with a child, so she gets mad in her own way."
    else:
        "But... How?!"
        "That's impossible, it's been ten years..."
    voice "I'm sorry I did that to you. I'm sorry."
    voice "And please wake up!"
    me "What?"
    voice "Wake up!"
    me "Why? Why do you care?"
    voice "I... I care."
    if loki:
        me "Ksyush... Come on, stop your foolishness already."
        me "You have not brought anything good into my life, have the conscience to back off."
    elif herc:
        me "I have different information. And even if I'm wrong, it's all gone."
        me "I already drove to your place halfway across town at midnight, I was punching faces and getting punched in the face because you felt bad."
    else:
        me "You're gone. You're..."
    me "That's it. {w}We're done."
    if loki:
        extend " You sat remarkably silent for ten years."
    elif herc:
        extend " We are strangers, and that suits us both."
    me "I suggest we leave the status quo intact."
    voice "No. After all, if I had only then told you..."
    me "Told what?"
    voice "Never mind. {w}Just wake up. {w}Please."
    scene bg int_sam_house_clean_7dl
    show laptop_7dl
    show laptop_un_epilogue
    if loki:
        show laptop_un_epilogue_loki
    elif herc:
        show laptop_un_epilogue_herc
    else:
        show laptop_un_epilogue_dr
    with dissolve
    "Two drops slithered across the monitor and headed down a parallel course."
    voice "I weep for you, Semyon. {w}I weep for our unfulfilled dreams."
    voice "And the daughter who could have been yours."
    voice "But wake up! {w}Please! {w}Otherwise you will lose what little you have left!"
    me "Stop it."
    voice "PLEASE WAKE UP!"
    with vpunch
    "The monitor shuddered from the scream, and the picture was cut in half - in one part was a sunny summer morning cutting through a narrow window, and in the other was my dusty pigsty, beloved and familiar."
    scene black
    show laptop_7dl
    show laptop_un_epilogue
    if loki:
        show laptop_un_epilogue_loki
    elif herc:
        show laptop_un_epilogue_herc
    else:
        show laptop_un_epilogue_dr
    with dissolve
    "And the messages jumped up and down fast."
    "It was as if she really was, gibbering - fast, fast, not letting a word in or interrupting for such little things as breathing."
    voice "Don't sit there grinning skeptically and spinning the mouse wheel."
    voice "Take your chin off your palm."
    voice "Straighten up."
    "Wake up.{w} Wake up!" with hpunch
    voice "Turn your head away from the monitor and look at it with your peripheral vision."
    voice "To where the most prominent spot of color is."
    voice "It ripples and goes bodily - because the mind doesn't know how to construct pictures according to the algorithm monitors use. That means you're asleep. WAKE UP!"
    play sound sfx_break_monitor
    show prologue_dream
    "I sat there like I was paralyzed, and something struck the monitor from within, leaving serpentine cracks behind it."
    "Something was tearing outward, into my world. Something..."
    play sound sfx_7dl["ringtone"] fadein 8
    stop sound_loop
    "WAKE UP!"
    "The cell phone rang - I turned it off."
    stop sound
    play sound sfx_home_phone_ring
    "The apartment phone rang."
    scene bg int_sam_house_clean_7dl at zentercenter
    "I cautiously picked up the phone."
    play sound sfx_home_phone_take
    th "Who could it be? {w}Who knows my apartment phone?"
    "I put the phone to my ear."
    play sound sfx_7dl["wakeup"]
    dreamgirl "Wake up."
    th "I know that voice, don't I?"
    th "That voice curses the leaden sky every day and wheezes at the stall, demanding a pack of «Diablo Nero»."
    "It would be strange not to recognize my own voice."
    if dr:
        "And it would be doubly strange not to recognize the very voice that has accompanied me for almost a decade - my inner rebel, vulgarizer, and part-time conscience."
    dreamgirl "Wake up!"
    "I very gently put the phone away without hanging up, and from there, words was already yelling in different voices."
    voice "Wake up!"
    voice "Wake up!"
    me "A-a-a-a!"
    stop music
    scene black
    with fade3
    show alt_credits "WAKE UP" at truecenter with flash
    pause(2)
    scene black
    return

label alt_day7_un_7dl_day:
    scene bg int_extra_house_day_7dl with fade3
    play sound sfx_bodyfall_1
    with vpunch
    pause(1)
    play ambience ambience_int_cabin_day fadein 2
    "I flew off the bed and thundered across the floor.{w} Hurt my elbow, but woke up as a result."
    "Woke up!"
    th "So it was just a dream?"
    "I was relieved to catch my breath."
    th "I can't believe it!"
    "The phone was on its last gasp and was powered solely by its own stubbornness."
    "The time glowed on the screen: 17 hours."
    "Considering that I went to bed at midnight..."
    "Before my eyes rose the events of yesterday: Lena's disappearance, the search in our reserved place, the shocking information from Slavya..."
    "Could she really have done something wrong if I'd picked the wrong one?"
    "And my ever-present stupor."
    "A tongue clenched to the larynx, capable only of issuing one-syllable interjections."
    "Was it hard for me to say the most important thing?"
    "My inner voice was yelling, screaming that this was the key turning point!"
    "That I would either say the most important thing now or I would never say it!"
    th "I just have to admit - first to myself, then to her - that it's all for a reason."
    th "That this isn't a resort-camp romance whose only purpose has always been to have a nice time together. It's more than that."
    dreamgirl "Name, sister, name!"
    "I hope she gives me a chance."
    "At least this time."
    "She won't pester me with questions, demanding that I give her an immediate and clear wording..."
    "How do I know why I was looking for her - so much so that I even walked to the cape!"
    th "I don't know! {w}I just feel really bad without her, that's all."
    scene bg ext_house_of_un_day with dissolve
    "I closed the door behind me and headed for her cabin, hoping to catch her there."
    "She told me that sometimes she liked to just sit on the porch barefoot, exposing her feet to the sun, and watch the clouds."
    "And as much as I longed to meet her, I feared the same."
    "We are the worst of what has happened in the other's life. {w}We are the source of each other's trouble."
    "And I have nothing to lie about or confess. {w}I open wide the untamed soul and present it for inspection as the very duplicate of a priceless cargo."
    "I can neither scold her nor ask her forgiveness. {w}It's just...{w} It's just that I can't be without her anymore."
    if loki:
        "And like the first day, this burden is too heavy for me alone."
    "I have to tell her about it. {w}Just because you can't keep quiet about such things."
    "And I think I'm only now realizing it fully - not yesterday, when something inside was tearing with longing, settling in fat flakes of ash somewhere in my throat area, a shapeless, bitter lump."
    stop ambience fadeout 2
    scene bg ext_houses_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    "I moved around the camp, trying to see at least anyone. But it was as if the camp had died out - no one was around."
    scene bg ext_square_day
    with dissolve
    "It's so weird, like everyone's gone out to dinner or gathered at the swimming hole for another Neptune's Day."
    scene bg ext_dining_hall_away_day
    with dissolve
    "Even the canteen was closed. {w}Amazing."
    scene bg ext_dining_hall_near_day
    show un normal modern far
    with dissolve
    if alt_day4_me_neu_transit == '':
        "However, not as surprising as the fact that on one of the benches, Lena was sitting and listening to music from the «walkman» presented to her."
    else:
        "However, not as surprising as the fact that on one of the benches, Lena was sitting"
    if alt_day4_me_neu_transit == '':
        "Her head was bobbing in an extremely familiar rhythm, her fingers were tapping something on the banister, and I recognized Lara Fabian's «Je t'aime» in the rhythmic pattern with surprise."
        th "How remarkably similar our tastes are."
        "So I didn't disturb her and sat quietly on the steps, patiently waiting for the song to finish."
    show un normal modern with dspr
    th "It's warm here...{w} And without the crowds of pioneers, it's very, very intimate. {w}Cozy."
    th "And there's no need to yell at the nagging conscience. Why? We're honest with each other."
    dreamgirl "One can live quietly, without looking back or regretting, love this girl, accepting her and her world as a burden. What more could it take?"
    dreamgirl "Answers? {w}Who needs answers?"
    "I got here by a miracle, and any miracle is not tolerate when you try to dissect it in terms of logic or common sense."
    "Even though it is a miracle only that I, having earned nothing, still got my seven days of summer."
    th "Seven days of summer."
    dreamgirl "Yes..."
    th "One day, when it gets really boring, I'll open my notebook and fill it with several hundred pages, where I'll tell everything in detail."
    th "What I saw, what I felt, what I breathed. {w}And call the resulting stack of pages «Seven Days of Summer»."
    th "And I will tear and burn and crush the ashes - because it is only mine. My own Schrodinger summer."
    th "Whatever happens, this camp will be the most wonderful thing that has ever happened to me."
    "I swear to the unfolding bottomless sky."
    me "What can compare to that?"
    un "Love?"
    if alt_day4_me_neu_transit == '':
        "Asked Lena, who noticed me and hid her Walkman in a pocket on her chest."
    else:
        "Asked Lena, who noticed me."
    me "Love...{w} Maybe."
    "I smiled warmly at the girl."
    me "You disappeared so suddenly yesterday.{w} I missed you."
    show un shy modern with dspr
    un "I had to think."
    me "Think?"
    un "Yes. {w}So much has happened this week. And you..."
    "She seemed to have lost the thread of reasoning and was picking at the board of the bench she was sitting on thoughtfully with her fingernail."
    stop ambience fadeout 2
    play music music_list["into_the_unknown"] fadein 3
    me "Where did the pioneers go?"
    un "Gone."
    me "Gone?"
    un "Home."
    "Lena continued to pick at the miserable bench with a stubbornness worthy of a better use."
    un "The shift was over and they left."
    me "And we?"
    show un smile modern with dspr
    un "Stayed."
    me "I don't understand..."
    me "Why were we left behind?"
    show un smile2 modern with dspr
    "She was quiet for a while."
    un "I... Convinced the counselor."
    me "Convinced her to what?"
    un "To leave us here."
    me "Us?{w} You and me?"
    show un smile modern with dspr
    un "Yes."
    me "Don't you find that a little fantastical?"
    "Calmly I asked."
    me "You asked, and she suddenly did what you wanted?"
    un "Oh. I have my own methods of persuasion."
    me "Sure: I don't want to meet them."
    un "Yes. I don't want to convince you of anything.{w} I want you to choose for yourself."
    me "I wish I knew between what and what. {w}Are you sure you told me everything?"
    show un smile modern with dspr
    un "I didn't say that."
    me "Why don't you tell me?"
    un "Well, I told you the main thing already: I asked that we be left in the camp. {w}And we were left."
    "I still couldn't believe the reality of the situation, to the extent that it was phantasmagoric. {w}It seemed as if the boys were about to jump out of the bushes, from behind the closed door of the canteen, and shout: «surprise!»"
    "But time went on, and no one was in any hurry to jump out of nowhere.{w} So I had to accept Lena's version as a working one."
    me "What are we going to do now?"
    un "I don't know."
    "She twitched her shoulder."
    un "You're the man, you decide."
    me "I want this circus to stop immediately."
    "I sighed wearily."
    me "Everything was hellish with this camp from the start."
    me "I'm not talking about the fact that I got here straight out of late 2018, but now that there's a chance to get out of here, it turns out that the girl asked for a counselor and she gave in to her. Yep."
    show un shy modern with dspr
    un "You're talking nonsense."
    "She came over and placed her palm on my forehead, caringly."
    un "Do you have a fever?"
    me "Stop being ridiculous, Lena. {w}You know very well that I didn't come here from the next village."
    me "What's the matter, it wasn't a secret to anyone in the camp. {w}Or do you think that this..."
    if alt_day4_me_neu_transit == '':
        "I poked my finger at the player."
        me "Or this..."
    "And slappd the smartphone in my pocket."
    me "Any factory of this time period capable of producing?"
    un "The Japanese probably can."
    "Lena speculated."
    me "What Japanese are there when the engraving on the gold says «made in Hungary»?"
    th "The Japs don't have the necessary technological processes right now.{w} And the Magyars don't even have to talk about them: they only capable to produce «Ikarus'», and thank goodness for Random."
    un "Well, then I don't know."
    "With childlike directness the girl smiled."
    un "I don't care. {w}It's more important that you're here."
    me "What's that got to do with..."
    un "Syom, I'm not stupid. {w}And I heard perfectly well yesterday. {w}Even though you were so diligent and pussyfooting around."
    me "And?"
    un "What other «ands» do you want?"
    un "You wanted it, you got it. Rejoice."
    me "So that's how it is? {w}I made a wish, and you got it?"
    "I wasn't hiding sarcasm."
    show un normal modern with dspr
    un "Yes.{w} You wanted to be with me, didn't you?"
    "I sighed."
    me "With you. {w}Of course I'm with you."
    un "There you go. {w}It's easy."
    un "We'll be together now. {w}And neither Slavya nor Alisa will bother us here."
    me "That's wonderful, of course.{w} But what's next?"
    un "There's something wrong for you again."
    me "I mean, what are we going to do next?"
    un "We? {w}You talking about us?"
    me "Of course. {w}It's just the two of us here."
    show un smile2 modern with dspr
    un "I don't know."
    "She covered her eyes and smiled dreamily."
    un "Do you have any wishes?"
    me "Except gastronomically, no, not yet.{w} I've got a gut beating on my head."
    "She stood up, came closer, and held out her hand to me."
    un "Let's go."
    me "What? Where?"
    show un smile modern with dspr
    un "We'll feed you!"
    "She took a bunch of keys out of her pocket and jingled them in front of me."
    if alt_day1_sl_keys_took in (1, 3):
        un "You're not the only hoarder here."
    me "Good for you! What's next? Do you think there are provisions in the canteen?"
    un "I'm sure. {w}There's a third shift coming up. All the people are gone on vacation, so we've got a whole week..."
    me "Alone with a canteen full of food!"
    dreamgirl "Who's going to cook, I wonder..."
    play sound sfx_open_door_clubs
    stop music fadeout 3
    return

label alt_day7_un_7dl_dinner:
    scene bg int_dining_hall_day with dissolve
    play ambience ambience_dining_hall_empty fadein 3
    play music music_list["smooth_machine"] fadein 3
    th "Why not me?"
    "When Lena opened the door, she let me through, and I rushed toward the refrigerator - this magnificent structure had saved me many millions of times in the past, would save me from starvation now."
    "The only difference was that the current refrigerator was about the size of my apartment, and mostly stored all sorts of meat - which I didn't want."
    "Scratching the back of my head, I wandered further down the hall, hearing Lena humming something in the background, judging by the rustling, actively trying to fire up the stove."
    "Finally, my feet led me to the dry vault - and that's where I found everything!"
    with fade2
    show un normal modern with dspr
    "Heavily laden, I went back to Lena and dumped the groceries on the table."
    un "W-what's that? I thought you were going to make us a sandwich..."
    me "That, my dear, is what I call the one bright acquisition from the decadent west!"
    show un smile modern with dspr
    un "Really? And what is that? Some kind of pastry?"
    me "Yea! That's the one. Can you handle the stove?"
    "She nodded."
    me "Then get ready for a benefit from the chef."
    "The dough managed to bake on the first try, the sauce turned out pretty good, too - but we almost fought over the gherkins and sausage while slicing: everyone was trying to eat off a piece on a «well, just a bit!» basis."
    "But finally, that stage was passed, too, and a layer of pastry was placed on a margarine-lubricated baking tray, smeared with sauce and topped with grated cheese, slices of sausage, pickles, and red peppers."
    show un smile modern with dspr
    me "Now fifteen minutes, and we can eat."
    un "Nightmare! Is that dish called «the end of your figure» by any chance?"
    me "No! And by the way, just so you know, literally seventy years ago girls, on the contrary, were getting their cheeks full in order to marry well!"
    un "Diet to get fatter? {w}I don't believe in such a thing!"
    th "I wonder why I know her story better than she does?"
    me "Well, it's up to you!"
    "The intoxicating smells of browned dough, melted cheese, and melted sausage circles floated around the room."
    "And..."
    me "European-style pizza!"
    "I imagined, yanking the tray with two grubs out of the oven and setting it on top of the stove."
    un "Pizza?"
    me "Yes! Let's slice it up and we can eat it."
    un "I'm not going to eat it."
    "Lena tried to pull back."
    me "Whatever you want! More for me!"
    "I fetched a knife from the sink and plated the pizza pancake into eight classic slices - although, due to my crookedness, they turned out... and the pizza itself, for crying out loud... crooked and flawed."
    "However, their smell and drool-inducing appearance offset any possible complaints."
    me "So I'll start in the center, where there's more cheese. And will..."
    "I turned to the girl stubbornly pretending she wasn't here."
    me "CONSUME EVERYTHING!" with vpunch
    me "And then I'm going to crunch the crust, tug on a slice, and watch the cheese stretch."
    "After properly huffing the first slice, I took the first bite - and rolled my eyes: the highly concentrated taste made my hungry cheekbones cramp."
    me "Mmmm... belissimo!"
    me "You, Len, go to the dining room so you don't get embarrassed. And I'll - by myself - will."
    me "CONSUME EVERYTHING!" with hpunch
    show un shy modern with dspr
    un "Why are you so noisy... Don't you see, the girl is hungry. Give me a piece, too."
    me "You didn't want one, did you?"
    un "I still..."
    "She gulped and diligently looked away."
    me "As you wish."
    "I put the slice I had held out to her back to the main mass."
    un "Give it to me!"
    "She snatched the portion out of my hands and grimaced."
    un "It's greasy, it's dirty, it gets dirty... Is that how you're supposed to eat it?"
    me "Yes!"
    "With a doubtful look at the unfamiliar dish, Lena summed up doomfully:"
    un "I'm going to regret this."
    "And took the first bite!"
    with fade2
    "I froze, and I think, even stopped breathing."
    show un smile modern with dspr
    un "Delicious!"
    "I took a breath with relief."
    "It's better she doesn't know that this is one of the few dishes I can cook at all."
    un "Now it's clear who's going to be cooking in our house!"
    me "Forget even thinking about it."
    "I cut it off."
    dreamgirl "Flexed, huh? Now you're gonna have to clean it up."
    me "All right, have a good one! Let's take what we got and go!"
    show un shy modern with dspr
    un "Why? It's cozy here!"
    me "Because I don't feel comfortable here, and I don't want to wash the tray!"
    "After the kitchen experiments, I wiped the sweat from the excess heat that the cooling stove was actively sharing with the room."
    show un smile modern with dspr
    un "Is it cozier for you outside?"
    me "Yes. At least it's cooler there!"
    un "Okay."
    "We cut up some leftover pizza and put it on a plate."
    un "Where shall we take it?"
    me "To your place, of course! Food has always been kept by a woman!"
    show un smile2 modern with dspr
    un "As you command... Man."
    stop ambience fadeout 3
    play sound sfx_open_door_clubs_2
    pause(1)
    scene bg ext_dining_hall_near_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    "We walked the same way, holding hands, and smiling contentedly at each other and the world."
    "And everything was simple, requiring no elaboration."
    "I tried to resurrect that half-forgotten feeling of childlike spontaneity..."
    "I couldn't."
    "There was no place for innocent childhood friendship anymore.{w} Here...There was something else going on here, something greater, and I wasn't sure I was happy about the replacement."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day7_un_7dl_hysterics:
    scene bg int_house_of_un_day with dissolve
    play ambience ambience_int_cabin_day fadein 3
    show un smile2 modern with dissolve
    "It wasn't long before we were in the cabin, Lena took my plate and put it on the cupboard."
    un "It's cooler there - it won't spoil that fast."
    me "Yes, the dish has a life span of twenty-four hours. And in that time you have to eat the whole thing."
    un "Now how can you think about food in a situation like that!"
    me "I'm taking care that we don't starve to death!"
    "I strictly replied."
    me "Since I'm the lesser wrecker of the two of us, I hold the cards."
    show un normal modern with dspr
    if alt_day4_me_neu_transit == '':
        un "You're so thoughtful... I guess in your world every chick is yours, huh?"
    else:
        un "You're so thoughtful... Every chick is yours, huh?"
    "I just grinned."
    th "That's right, more like, no chick is mine!"
    show un serious modern with dspr
    un "What's so funny?"
    "She frowned."
    me "You were making a joke of humor. So I laughed. Shouldn't have?"
    un "You are..."
    me "Yeah? Who?"
    "With interest I clarified."
    un "..."
    show un laugh modern with dspr
    un "Dummie!"
    "After hesitating a bit, Lena chose the most eloquent epithet."
    me "And I hear that from a slacker!"
    "I grinned my thirty-two."
    show un smile2 modern with dspr
    un "Well, now that we've dealt with the most pressing issues..."
    "She hung the end of the sentence in the air, letting me figure it out on my own."
    "I looked at her questioningly, and she came toward me. A little closer. Sat next to me on the bed and snuggled up against my shoulder."
    show un smile modern with dspr
    un "Syom..."
    "Dreamily she said."
    me "Yes?"
    "Businesslike, I asked."
    un "Uh..."
    "The cool reception on my part seemed to shake her newfound confidence somewhat."
    me "What?"
    show un shy modern close with dspr
    un "I don't know."
    "She whispered, looking at the floor. {w}Her cheeks suddenly flushed."
    un "Maybe..."
    stop ambience fadeout 2
    play music music_list["confession_oboe"] fadein 3
    me "What?"
    "I didn't understand her innuendo, and frankly, I was starting to get a little tense."
    "You know, if you want to hint at something to a man, write it on a huge banner, take your clothes off, and walk under his window."
    "Then maybe something will get through to him."
    show un smile2 modern close with dspr
    un "Don't you want something special?"
    "Her voice trembled dangerously, but she quickly pulled herself together."
    un "Something you haven't done before?"
    dreamgirl "Actually, there aren't many things we haven't done before..."
    "And I wondered."
    "There were a lot of plans, especially under the circumstances."
    th "We've got a whole week here! A week!"
    "You could've been hustling and looking for a way out or an escape or something."
    "The question is, why?"
    "I've got something... Someone far more important than all the answers and escapes."
    "Lena."
    dreamgirl "She almost explicitly suggests being with her - in every sense. {w}Is that so incomprehensible?"
    th "I don't know."
    "I exhaled convulsively. {w}I was palpably shaking."
    "Lena moved even closer and threw her arms around my neck, covered her eyes and stretched toward me, reaching for me, not so much with her lips as with her very being, as if I were the sun and she were some strange flower with purple petals."
    "And that made my own cheeks blush, my thoughts go into complete chaos, and my inner scruffy man chuckled jubilantly and rubbed his hands together:"
    dreamgirl "Just don't resist her!{w} Just let her take what she wants!"
    show un smile modern close with dspr
    un "And if you think about it?"
    "She purred, without opening her eyes."
    me "If you think about it... {w}If you think about it, it's kind of weird."
    show un shy modern close with dspr
    un "What?"
    "She flinched and opened her eyes."
    show un angry2 modern with dspr
    un "What are you talking about?"
    "There was that expression in her eyes that I remembered from the dream - demanding, greedy."
    "And not that I mind this metamorphosis - it's better than the shy kid of the first two days, but..."
    un "You said it yourself yesterday..."
    "Her whisper scorched my ear."
    un "Were you lying?"
    me "No, but..."
    un "Then what's the problem?"
    me "I'm not sure it's right."
    show un normal modern with dspr
    un "We are in a place where no one can see us."
    un "I want you. {w}You want me. {w}What could possibly be wrong with that?"
    "She bit her lip."
    un "What has changed in two days? {w}You no longer like me?"
    me "No, I... like you. Very much."
    un "And I like you. Problem solved."
    show un smile modern close with dspr
    "The girl ran her hands under my shirt and chased waves of goosebumps with a ticklish caress, mingling at my sincere reaction."
    un "I like you very much."
    hide un with dissolve
    "She drew me to her and kissed me with surprising skill, spreading the lips with an unguarded tongue, wrapping one of the best French kisses I had ever experienced."
    th "No match for the day before yesterday..."
    "Without pulling her lips away, she threw her leg over me, settling on my lap, facing me, and catching my palm, established that one on her thigh, letting me know she wasn't wearing any underwear."
    "I was shaking and pounding with a sweet exhaustion of anticipation."
    "My eyes darkened with anticipation and longing for intimacy with the most beautiful, most desirable girl."
    "That same magic of the early days when you can't get enough of the attention, the caresses - even the very presence of a girl in your life."
    "Her lips were hot and sweet, and her skin smelled of tar and lime."
    "She seemed to be seriously preparing herself for what was about to happen."
    "Her touch was intoxicating, her scent took me to a heavenly height from which all the fumbling in the crumpled sheets seemed ridiculous."
    "But she was there, and I was drowning in her eyes, and all my longing for it to be beautiful was drowning there, too."
    "She was from day one - the most interesting, the most mysterious."
    "Shirts flew in different directions, letting the heated skin touch."
    "The most beautiful and the most desirable."
    dreamgirl "And most beloved?"
    "I suddenly realized that I was just about to sleep with a girl I liked - no soul, only on teenage enthusiasm and hormonal overdose."
    "I stopped and, as gently as I could, pulled her away from me."
    show un smile modern close with dissolve
    un "W-what?"
    "Her breathing became intermittent with excitement, and she could hardly tell where she was or what was wrong with her."
    me "Sorry. I can't."
    show un normal modern close with dspr
    un "What?!"
    me "I can't."
    "I repeated, feeling like the last bastard."
    me "Lena."
    "I started."
    me "I understand: we're young and everything."
    me "But don't the two of us have anything else to do?"
    "I eloquently circled my arms around «us»."
    me "Am I so boring to you that you're not interested in anything else about me besides debauchery?"
    show un smile modern close with dspr
    un "Stupid."
    "She kissed my neck."
    stop music fadeout 5
    un "We should take advantage of the time while we are together and alone. You know?"
    me "No. I don't understand. Are you bored talking to me, spending time with me? What is it?"
    show un shy modern close with dspr
    play music music_7dl["sorrow"] fadein 3
    "Her eyes went dark."
    un "You don't like me anymore? Or..."
    "She bit her lip."
    if persistent.mt_7dl_good:
        un "You remember everything, don't you?"
        show un scared modern with dspr
        "She shivered in horror, cowering in the far corner of the bed."
        un "Remember?!"
        me "Lena."
        show un cry modern with dspr
        un "I'm sorry, I couldn't help myself, I can't do it without you!"
        "She screamed in my face."
        un "And you're always leaving, you're always leaving!"
        show un scared modern close with dspr
        "I tried to catch her and calm her down, but she recoiled from me, staring with the same horror."
    else:
        show un normal modern close with dspr
        un "What, words of that bitch still bothering you?!" with vpunch
        me "What has Slavya got to do with it at all?"
        "I sighed."
        me "She just said that if I wanted to go back..."
        show un angry modern close with dspr
        un "Well, go then! Get out!"
        show un cry modern with dspr
        "Tears spurted from her eyes and she tried to jump off me, but I held her in place."
    me "Lena!"
    show un sorrow modern close with dspr
    un "Get off me!"
    me "Lena!!!"
    un "Get your hands off."
    "There's no way. As if I'll let her go like that."
    "Instead I pressed her against me even harder."
    me "I won't get it off until you calm down."
    "Unwillingly inhaling the scent of her hair, I replied."
    "And smiled again at the citrus scent."
    me "You don't want to talk to me anymore? We're either screaming or fighting, what is it?"
    un "What?"
    "I sighed."
    me "Where did the girl you were the day before yesterday go? We were having so much fun together!"
    if persistent.mt_7dl_good:
        show un cry_smile modern close with dspr
        un "I'm betraying someone else's memory - is that how I grow?"
        "Inexplicably she asked."
        me "What are you talking about?"
        un "There is so much evil in people, I kept vowing to myself never to be like them."
        un "I wanted to be like Slavya and believe in good."
        show un cry modern close with dspr
        un "Who knew it would hurt so much to be good to the end. {w}To give up on you."
        "Lena trembled in my arms, but made no more attempts to break free."
        un "And now I am just like these people. {w}There's no forgiveness for me."
        "She shivered, and I was able to draw her to me, stroking her dark hair comfortingly."
        hide un with dissolve
        me "The most important thing is that you're with me, isn't it?"
        "Quietly I ask the silence."
        me "And I am with you. {w}I have no idea what kind of betrayal you're talking about, but it's going to be okay now."
        "Now everything will be - {i}just as it should be{/i}."
        with fade2
        "I talked about something else until I felt a lack of response and movement."
        "A brief flash burned all the girl's strength, and she slept quietly in my arms."
        show blink
        "After kissing her forehead, I put my arms around her and closed my eyes."
    else:
        show un cry_smile modern close with dspr
        un "I have changed. Happy now?"
        me "So now we have nothing to talk about?"
        me "I know how a relationship ends with too much bed... And then there's another man-hater calling all men assholes."
        "She didn't say anything."
        me "What are you silent about?"
        show un serious modern close with dspr
        un "You should have told me right away that you don't like me."
        un "I'm not completely clueless and not at all obtrusive - I'll take a hint and blow it off in the cold."
        hide un with dissolve
        "I rolled my eyes and wanted to bark something about who was being silly, but... I couldn't help myself."
        th "At least someone has to be reasonable, since the other one is going crazy."
        dreamgirl "Didn't you refute her nastiness?!"
        dreamgirl "Semyon, are you sick? {w}Are you retarded? {w}Tell her immediately that you like her. {w}Or in love, there, confess - it's high time, retard."
        me "I like you. A lot."
        "Quietly I uttered."
        "No answer."
        me "Lena?"
        "Silence."
        "I turned my head and looked at the girl - she was sleeping quietly, snuggled up against me with all her strength."
        "My palm ran itself through her smooth hair, a hot forehead beneath my lips."
        me "Sweet dreams, little one."
        show blink
        "I wished, and closed my eyes."
    stop music fadeout 3
    return

label alt_day7_un_7dl_pills:
    scene bg int_house_of_un_night
    show unblink
    play ambience ambience_int_cabin_night fadein 3
    "When I opened my eyes again, Lena was gone, and it was dark outside."
    "I'm sleepy... All I do is eat and sleep."
    "You sleep, you can eat, you eat, you can sleep."
    "The pizza plate was still on the cupboard, waiting to starve."
    "I looked for my shirt and, without bothering to tie it, put it on as it was and went out at the body's demand - it really wanted to visit the funhouse «WC»."
    stop ambience fadeout 3
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg ext_houses_night_7dl with dissolve
    play ambience ambience_camp_center_night fadein 5
    th "Surprisingly, I did not hear any anger or tantrums from her."
    if persistent.mt_7dl_good:
        "Although there was something doomed about her behavior, it doesn't mean that-"
        "Or does it?"
        "It made me very uncomfortable."
    else:
        th "Just the quiet tears of someone who cared enough about me to accept my choice?"
        th "Does that mean she's come to terms with it? {w}Is she up to something?"
        "I'm used to perceiving Lena as a frightened but reasonably sane child, but the events of the past day have made me question the validity of my assessment."
        "She could have been... Any!"
    scene bg ext_square_night with dissolve
    "I got worried and hurried to finish my business quickly, before the worry turned into panic."
    un "Semyon!"
    show un smile2 modern poisoned with dissolve
    "A cheerful voice called out from behind me, and I hurried to turn around."
    "Lena, alive and well."
    "Her face seemed pale for some reason, but I chalked it up to the moonlight."
    me "Lena! I was worried."
    un "You've been asleep a long time.{w} I decided not to wake you up. {w}I thought I'd take a walk."
    me "A walk?"
    "She seemed kind of morbidly excited."
    un "Yeah. I thought I'd better let you get some sleep."
    "She giggled stupidly and took a few steps in my direction."
    "Her legs buckled."
    play music music_list["torture"] fadein 5
    show un sorrow modern poisoned with dspr
    "And I recognized that gait with horror and disgust."
    "And the pallor, turning blue."
    "What's more, I saw that picture in the mirror as recently as a few years ago, when I had two hundred nostril pills digested in my stomach."
    "Unfortunately, my heart turned out to be too strong{nw}."
    if loki:
        extend ", and I just laid it off."
    else:
        extend ", and I inexplicably, unnecessarily - survived."
    show un sorrow modern poisoned at zentercenter
    with dissolve
    "I rushed toward her, picking her up on a half-fall. {w}Soft feet, fingers that had lost sensation. {w}Well, chemistry, of course."
    me "God, stupid! {w}Stupid! {w}What did you took, answer me!"
    hide un with fade
    "She flailed around in my arms without a care in the world."
    "Growling curses, I hoisted her onto my back and dragged her toward the toilets: there was cold water, there was a chance to flush her stomach before it was too late."
    if persistent.mt_7dl_good:
        un "I'm disgusting.."
    else:
        un "It was too late, when you didn't even want the body."
    "Without opening her eyes, Lena said quietly."
    if persistent.mt_7dl_good:
        un "I am a thief. I stole you from the one whose rightful possession you are."
        "I didn't understand what she was ranting about, but rightly decided that dealing with such matters could be put aside for later."
    else:
        un "I feel so useless."
    stop ambience fadeout 3
    play sound sfx_open_door_kick
    pause(1)
    scene bg int_toilet_night_7dl with dissolve
    me "No, baby. {w}Not this time. {w}I'm not letting you go that easily."
    "I bellowed, kicking the door of the boys' ward open with my foot, and piling in."
    play sound sfx_open_water_sink
    play sound_loop sfx_water_sink_stream fadein 2
    "Trying to move as carefully as possible, I unloaded the priceless cargo with my back against the tiled wall and, opening the water, looked around for some vessel from which this stupid girl could drink."
    "I couldn't find it, so she had to drink from the palms of my hands."
    me "Lena! Lena!"
    play sound sfx_face_slap
    with vpunch
    "She was already falling asleep, and I had to whip her lightly on the cheek."
    me "Don't sleep, silly girl! Fight it! {w}You have no right to end up here in my arms! Not this time, you understand!"
    "She opened her eyes and stared blankly, incomprehensibly through me."
    me "Open your mouth!" with vpunch
    "I yelled. {w}Took a handful of ice-cold water and held it to her mouth."
    me "Drink!"
    un "For... Why?"
    me "DRINK, I SAID!"
    "She obediently drank the water."
    me "More! More! {w}No, don't pass out!"
    "I flipped her over with her belly down and, with my knee propped up, fixed her and ran my fingers into her mouth."
    "Now it's going to be very uncomfortable and probably even painful if she closes her jaws."
    "But life has never been presented as a pleasant and painless thing."
    "Fingers fumbled for the base of her tongue and pressed down, holding it in place, keeping her mouth from closing."
    "She coughed and tried to turn inside out."
    "A hot stream of vomit hit my palm."
    "It would have been disgusting if it hadn't been so creepy - almost pure stomach juice, with white, half-dissolved mugs of pills piled up in it like mugs of fat in a sausage."
    me "Drink more!"
    "I took off my shirt and wiped her watery eyes."
    me "Drink, I said!"
    "She obeyed, unhesitatingly. {w}The main thing is not to be too late."
    "Judging by the reactions, it's a sleeping pill, and I have no idea how much of that stuff it would take to guarantee to finish the girl off."
    "There were noticeably more pills this time - it looks like we got to the bulk of the poison."
    me "Don't fall asleep! {w}Don't pass out, you hear me! {w}When did you take the pills?"
    un "Two hours...or more."
    "I drank her and got the rest of the chemo out of her stomach, realizing that now even one forgotten pill might be enough."
    "All I could do was pray to random and hope that her organism was strong enough."
    "Finally, she threw up the same water she'd just been drinking."
    "There were no more pills in her vomit, only pure bile and water."
    stop music fadeout 3
    "It means there's only that stuff left that's been sucked into the bloodstream. {w}Two hours. {w}It's over. {w}There's nothing I can do. Or?"
    me "Where did you get that stuff?"
    play music music_list["orchid"] fadein 5
    "I shook her by the shoulders."
    me "Don't sleep! Answer me!" with vpunch
    un "In the infirmary. I have the key."
    "Languidly she uttered."
    me "The key?"
    un "Pills... For a headache."
    "She tried to smile, but her facial muscles seemed to be already failing her, as she got a creepy grimace."
    th "Viola was sympathetic and left the key?"
    me "Lena, listen to me very carefully."
    "I shook her up and wrapped my arms around her head and turned her around to face me."
    me "So I'm going over there now, and you stay here and try your best not to lose consciousness!"
    me "Do you hear me? This time I'm not letting you go anywhere! {w}And when I come back with the medicine, we'll-"
    stop sound_loop
    play sound sfx_close_water_sink
    pause(1)
    un "Two hours, Semyon. I'm already gone."
    scene bg ext_aidpost_night at fast_running
    with flash
    "I gritted my teeth and jumped out of the bathroom, dashed across the camp to the infirmary building, and with shaking hands I couldn't get into the keyhole for a long time."
    scene bg int_aidpost_night
    "Bloody Soviet medicine! {w} I couldn't buy myself some phenobarbital at my time, and here the fool just climbed into the camp infirmary and found everything needed."
    "Two hours. {w}She's right: the chance is vanishingly small."
    "I have to make it in time. I have no right to make a mistake or delay."
    "The medicine - all that Lena and I had carefully collected and counted - flew to the floor!"
    "Everything that might come in handy - charcoal, analeptics, prednisolone, even the damn suprastin and insulin - scattered in my pockets and, not caring to close the door, ran back."
    scene bg int_toilet_night_7dl with fade2
    play sound sfx_open_door_kick
    pause(1)
    "She was right where I left her, half-sitting with her back against the wall."
    "And I knew by the mere sight of her that I was too late."
    "Her lips were blue, and her depressed breathing indicated that she might be breathing her last moments."
    "I, not knowing what I was hoping for, was cracking vials, preparing injections, already useless."
    "She might have been saved by a paramedic team specializing in just this type of poisoning."
    "And not me, who has had an injection once in my life.{w} But the plunger goes down and the solution goes under the skin."
    me "Fight it, girl. Fight it, I need you."
    un "Will you pity me one little bit?"
    "She asked blankly, staring at the ceiling, not noticing me."
    un "At least a little."
    me "Yes."
    "I kissed her bluish lips and squeezed her hands as hard as I could."
    me "Yes, you just...{w} Don't you dare, do you hear?"
    me "We've been through so much together. Lena!"
    "I shook her."
    un "All right."
    "In the same undead voice she replied."
    un "Because I..."
    "And she exhaled - as if extinguishing a candle."
    "A round plastic vial rolled out of her weakened hand. Empty."
    "And I howled, holding her close to me, unable yet to realize one simple thing - she was gone."
    "With her usual gait, lifting up slightly on her toes. {w}Gone. {w}And she will never, ever be again."
    "A dreadful and unnecessary death."
    scene cg d7_un_reanimation_7dl with dissolve
    me "No. No!"
    "Quiet the trembling in my hands. {w}Stop the hysteria. {w}Breathe in deeply and on the exhale..."
    "Another syringe pierced her skin, stimulating her breathing, and I laid her on her back, shrugging off the squeamishness, and pressed my lips to her lips, blowing sharply twice."
    "I didn't know if I was doing what I was doing right, but sitting still seemed like a crime to both myself and her. Roughly figuring out where to squeeze, I folded my arms and pressed sharply, almost hitting her chest once, twice, three times."
    "I listened for breath and, not hearing it, started again."
    "I alternately pressed on her chest and ventilated her lungs until my own lungs began to burn with fire and my hands were sore..."
    "Even the will to live has limits, even if you really don't want to let someone go, your arms always get weak as a result..."
    "I yelled at her, shook her hands, coaxed her, threatened her, promised everything in the world - she just needs to open her eyes!"
    with fade3
    "I'm tired. I forgot how to breathe."
    "I'd tear a chunk out of my life just to have you come alive."
    "For how long - a year? Ten years? All that's left?"
    th "God, why..."
    stop music fadeout 5
    me "I'm sorry. Just sorry."
    "I put my palm on her forehead and smoothed her dishevelled hair."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day7_un_7dl_miracle:
    scene bg int_toilet_night_7dl with fade
    play music music_7dl["loki_on_3"] fadein 5
    "I needed a miracle."
    me "Live."
    me "Do you hear?"
    me "Please."
    me "I can't, I can't without you. {w}Live."
    me "LIVE!"
    if herc or loki:
        if herc and (karma >= 50):
            "And she jumped up, almost arched, and frantically took the first gulp of air, as if she were diving out of the abyss."
            "I picked her up, running my hands between her armpits, and squeezed."
            "Out of her mouth, out of her nose, the rest of the crap, that was clogging her airway, immediately spurted out."
        else:
            if loki and (alt_day1_sl_keys_took in (1, 3)):
                "She looked at the world with open eyes."
                "Despite everything the world had done for her, she believed in it."
            else:
                "She was from day one - the most real, the most priceless."
        if persistent.mt_7dl_good:
            "She was longer than I knew, leaving hooks in my memory."
            "A girl looking at my back, picking up footsteps in the cold night."
            "The princess of the land of memory."
        "And I habitually grinned at her name, dropping «your perfection» into the night air."
        "I knew no one better than her."
        "She was alive..."
        "And I went on, despite my burning lungs, the pain in my shoulders..."
        "Until the next batch of air was answered by slimy, cold lips... My favorite lips."
        "On the back of the neck, a transparent vein moved faintly."
        with vpunch
    else:
        if 'nwsppr' in list_clubs_7dl:
            "She loved to draw."
            "And she hated erasing angels from the margins of notebooks."
        "I didn't know anyone better than her."
        "She was alive..."
        "..."
        "Feel like a hamster."
        "Feel like a philistine praying to numbers."
        "9-1-1. Or 1-1-2?"
        "Emergency phone."
        "Please, I need an emergency rescue."
        "Save my happiness, save my space."
        "Miracle, two cubes, urgent."
        show blinking
        "I couldn't believe my own ears when I heard a quiet cough."
        "Lena coughed!"
        "I immediately picked her up, put her on my chest, and squeezed her."
        "The coughing got worse - until a huge yellowish clot came out of her throat."
    if persistent.mt_7dl_good:
        un "You... You shouldn't have."
    else:
        un "Semyon... Why?"
    "She collapsed in my arms and wept helplessly."
    "Yes, she wasn't exactly a model of beauty - pale green, sunken eyes, and an exhausted look."
    "Even her perky tails were drooping and staring down at the floor."
    me "Alive. Alive, for God's sake!"
    "I leaned helplessly against the same wall and stared mindlessly at the same ceiling."
    "Something wet and cold touched my hand. {w}Her hand. {w}She squeezed my fingers."
    me "My little fool."
    "I said affectionately."
    me "Decided everything for everyone around you again?"
    if persistent.mt_7dl_good:
        un "I shouldn't be here."
        "She clenched her teeth and banged the back of her head on the tile."
        un "Not me."
        un "I don't deserve the right..."
        me "Shut up."
        "I cut her off."
        me "And cut the «deserve» crap already."
        me "I need you. That's what's important."
    else:
        un "You don't need me..."
        "She murmured."
        un "No one needs me."
        me "That's the least of your worries right now. {w}You owe me your life now."
        me "Which means you have no right to dispose of it."
    "As sternly as I could say."
    me "Do you understand me?"
    un "Yes..."
    me "Fine."
    "I handed her a packet of absorbent."
    me "Now, be a dear and eat four of them and don't be stubborn."
    scene bg int_toilet_night_7dl
    show un sorrow modern
    with dissolve
    "With my help, she got up and, supported on one side, she took the pills with a bang."
    if persistent.mt_7dl_good:
        "And I stroked her cheek and apologized:"
        me "Please forgive me."
        un "For what?"
        me "For letting you doubt."
        me "Slavya told me that you were once abandoned and that I was a bad match for you."
        show un normal modern with dissolve
        un "Is that so?"
        me "Yeah, because I can't promise anything - I might disappear from the bus seat."
        me "And this time I won't be able to be around to help if you decide to chop something... like that again"
        show un sorrow modern with dspr
        un "But I need you by my side!"
        me "Not like that."
        "I shook my head."
        me "You have to swear first."
        "I put my fist out in front of me with my little finger protruding:"
        me "First Slavya, now me - you've wasted two lives, and you're far from a cat, you don't have nine of them."
        me "So swear."
        "My little finger touched her cold pinky finger unabashedly."
        un "Swear what?"
        me "Repeat after me..."
        me "I am where you are, and we are one..."
        un "I am where you are... And we are one..."
        me "I trust you, and I'll always be by your side..."
        "The old, old formula from the land of children's fairy tales."
        "From a world where sunnies are the living sun bunnies, and the green-eyed ones are the happiest."
        with fade2
        "And as the echo of the last words froze in the air, from within echoed:"
        dreamgirl "Captured."
        me "Now forgive me."
        show un normal modern with dissolve
        un "But for what?"
        "I bounced to the faucet and, turning the water regulator to full power, directed the jet toward the girl."
        me "For shock therapy..."
        hide un with dissolve
        "The squeal hit my ears."
        scene black
        with fade2
    else:
        me "Now we'll go to the cabin and get something to drink while the body deals with the rest of the crap."
        "Tenderly I persuaded her."
        me "You've got a good, strong organism - he can handle it."
        "I took her out into the square, into the clean air."
        scene bg ext_square_night
        show un shy modern
        with dissolve
        un "And then what?"
        me "Let's get you cleaned up and wait for the counselor."
        me "If there's going to be one, then there's going to be a transport, right?"
        "She nodded and, leaning on my shoulder, closed her eyes..."
        me "No, my dear, you're awake tonight. {w}At all, I said. {w}Not sleeping at all."
        un "How's that?"
        show un smile2 modern with dspr
        "She groaned and pressed her hands to her mouth in a familiar gesture."
        un "A whole night?"
        me "Thirty-six hours. {w}The half-life of this abomination you've had."
        un "And what are we going to do for those thirty-six hours?"
        show un shy modern with dspr
        un "If you said I shouldn't sleep, you should keep me awake."
        me "I have a couple of ideas on how to keep you awake."
        "I grinned, feeling no less like Tyler Durden."
        un "And was it worth it to refuse at the cabin back then..."
        "I found no objection and just nodded."
        un "What a fool you are, Semyon."
        me "Fool."
        show un smile modern with dspr
        un "Give me a hug?"
        "She asked."
        "I silently obeyed."
        scene black
        with fade2
        "We spent more than a day together, never getting out from under the blanket for more than a few minutes to run to the bathroom or for a drink."
        "We got to know each other greedily and insatiably, and the kisses lasted up to an hour, and our legs buckled from the excitement we felt."
        "And the strength seemed to have nowhere to come from- and we drew it from each other, from each other's mutual tenderness and madness at each other."
        "And when the sun touched the horizon a second time, I, utterly devastated, fell asleep..."
    stop music fadeout 3
    return

label alt_day7_un_7dl_rollback:
    scene bg ext_square_day with fade
    show un smile modern with dspr
    play music music_list["tried_to_bring_it_back"] fadein 3
    un "Wake up, sleepyhead."
    "Softly she called."
    un "I've seen you sleep sitting up, but to fall asleep looking up at the sky while hugging a girl is something - you've surpassed yourself."
    un "I'm here waiting for him to kiss me, and he's asleep!"
    "She modernized her uniform in the most serious way by taking off her tie and undoing a couple of top buttons."
    "It looked exciting and beautiful. {w}I looked around - the place where Lena and I were sitting and looking at the stars."
    me "What are we doing here?"
    show un normal modern with dspr
    un "Hello. You're the one who said we'd wait for the counselor in the square."
    me "I didn't say that!"
    un "You did. You said that after my stunt yesterday I shouldn't be allowed near people, so we'll sit apart, trying not to piss people off."
    me "Wait. What day is it?"
    un "For you? Seven. For me it's the twenty-first."
    show un smile2 modern with dspr
    "She smiled."
    un "Did you lose count? You found me on the beach yesterday... {w}You almost ran away yourself, though."
    me "And you didn't eat a sleeping pill to the point of a coma, and I didn't clean your stomach?"
    show un normal2 modern with dspr
    "She thought for a moment."
    un "No. {w}Nothing like that. {w}It was a dream - you must have eaten something at dinner."
    me "Really?"
    "I jumped up and pointed an accusing index finger at her."
    if persistent.mt_7dl_good:
        me "Yeah, and I didn't spill on you, and you didn't chase after me with a twisted face?!"
        show un smile modern with dspr
        "Lena smiled and shook her head:"
        un "Is that what you are into?"
        me "Nothing like that!"
        show un laugh modern with dspr
        "I protested, but Lena only smiled more."
    else:
        me "Maybe you'll also tell me we didn't have pizza and a thirty-six hour marathon in bed!"
        show un shy modern with dspr
        "She blushed."
        un "Semyon... Now that you say it."
        show un shy_smile modern with dspr
        "She giggled."
        un "I think that's a pretty good idea. {w}But it wasn't. {w}Nothing like that happened."
    me "And you..."
    show un normal modern with dspr
    un "Yes."
    "She nodded."
    un "Whatever nightmare you had, it has nothing to do with reality."
    me "And reality..."
    show un sad modern with dspr
    un "Is that we're leaving in half an hour."
    "I seem to be caught in some kind of tricky space-time topology right now."
    "The Demiurge has shown power, brute."
    show un surprise modern with dspr
    un "What is it?"
    me "I'm scared."
    show un normal modern with dspr
    un "Amazing."
    "She shook her head."
    un "But what could happen?"
    me "I don't even want to think about it."
    "I cut it off."
    me "It's horrifying! {w}Do you still have my contacts?"
    show un smile modern with dspr
    un "Yes!"
    "She patted herself on the breast pocket."
    show un smile modern at right
    show mt normal pioneer at left
    with dissolve
    mt "Guys, let's go!"
    "The counselor shouted."
    if persistent.mt_7dl_good:
        show mt smile pioneer with dspr
        "She calmly met my gaze and smiled."
        "As if nothing had happened."
    mt "Or do you want to be..."
    show mt laugh pioneer with dspr
    "She laughed infectiously, emphasizing the significance of the joke."
    hide mt with dissolve
    "Turned around and, waving her hand over her head, set off for the final check of the cabins."
    "And it looked so natural and effortless that I forbade myself to doubt it."
    "A dream is a dream. A delusion is a delusion."
    "Lena - there she is, alive, real and mine, sitting next to me!"
    show un normal modern at center with dspr
    "I put my hands on the girl's shoulders and looked sternly into her eyes:"
    me "Remember. You promised me you wouldn't let us get lost."
    me "Just. {w}Remember. {w}Deal?"
    show un smile2 modern with dspr
    "She looked at me in surprise, but nodded obediently."
    "And we hurried to the bus."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day7_un_7dl_bad:
    scene bg int_toilet_night_7dl with fade
    play music music_7dl["danceagain"] fadein 5
    "The ultimate injustice of any dream is that it ends sooner or later."
    pause(3)
    scene cg d7_un_suicide:
        pos (0,-360)
        linear 10.0 pos (0,0)
    with dissolve
    "And it doesn't matter if it was the alcoholic visions that preceded death at dawn, the fantasies of an impressionable nature after reading a book, or the giddiness of an unhinged subconscious."
    "It's just that one day you open your eyes and come to terms with the fact that no one is sitting on the edge of the bed, the warmth of the touch of your lips is illusory, and there is no note or gun under the pillow."
    "And you want to go back, to prolong it even for a few seconds - please, what's so hard for you!"
    "And we run into dreams, clinging in vain to alcohol, drugs and anything else that can expand the mind - just because it's better there."
    "I've been lucky enough to experience a dream in real life. Lucky. How can I put it. I'm holding on to a splitting, square head, scrolling through what's left on the other side of the line."
    "Time has stopped and a thickened drop hangs over my head, tossing me back down the steps of memory..."
    "She is like a golden statue, frozen in rigor, her dark to purple hair a mournful halo scattered across the floor, shading the fragile, icy beauty of her perfect face."
    "The gaze looks somewhere far away, through me, through the ceiling, into the void, to where she, very soon, too will be heading."
    "Sometimes just a desire to save bluntly isn't enough."
    "Especially when the opponent to the amateur-savior is this ignominious demise - on the stained tile floor of a toilet."
    "I hug her and hold her to me, howling helplessly into the indifferent ceiling."
    "And she looks through me with the dead glassy look of her long stopped eyes - and that's it, she's not here anymore."
    "My God, was that really the sacrifice? The very toll of a trip into the unknown to a fake summer and genuine passions?"
    "And we, naive as we were, thought that just her blood was enough... Just a little bit. And that's it, we're tied tighter than if we'd once exchanged rings in the face of a few witnesses."
    "The terrible sacrifice is life, the priceless life of a priceless girl."
    "And only now do I realize how much I hate the one who did this to me."
    "I hate - myself."
    "I have no idea how long I sat next to her like that, cradling her head in my lap."
    "We sat together, chatting about everything in the world, and we had no fates or judgments - just her soft soprano and my husky tenor."
    "We entered the fire that mangles souls but leaves bodies imperishable."
    scene bg ext_square_night with dissolve
    "I... I couldn't, I had no right to leave her here."
    "I haven't done everything for her yet, and I haven't had time to say the most important thing."
    "Weightless in normal life, she weighed several times her usual weight now, but it was acceptable."
    "It would also be acceptable to tread naked feet on blades and knives so that every step I took would let out an unrelenting inner pain."
    "And if you cover your eyes and don't look at the eerily still beautiful features, you can think that all is not still hopeless, that there was no stupid conversation, no sleep, no pizza and piles of pills."
    "When I realized I was crying, I wasn't surprised."
    "I carried her through the camp - to the place where the most important thing in our lives happened, where she was able to trust me..."
    "And I betrayed her."
    if loki:
        scene cg d2_un_kissing_7dl
        show prologue_dream
        with dissolve
        "Our first kiss..."
    elif herc:
        if alt_day_binder != 1:
            scene cg d1_un_book0_7dl
            show prologue_dream
            pause(2)
            scene cg d1_un_book_7dl
        else:
            scene bg ext_house_of_sl_day at zenterleft
            show un shy pioneer at cleft
        show prologue_dream
        with dissolve
        "Our first meeting..."
    else:
        scene cg d2_sovenok
        show prologue_dream
        with dissolve
        "Owlet..."
    scene bg int_library_day
    show un normal pioneer
    show prologue_dream
    with dissolve
    "Drawings..."
    scene cg d3_un_dance
    show prologue_dream
    with dissolve
    "Our dance..."
    "It was as if a dam had burst somewhere, and memories equivalent to several lifetimes in duration poured into my head."
    scene bg ext_un_hideout_night_7dl with dissolve
    "And as I carried her to the cape itself and laid her down on the warm sand, the ability to think was mercifully cut off by inhuman fatigue."
    with fade2
    "Now I could already say."
    th "What's the point of fooling around now??"
    me "You know... I love you."
    me "Not in the way you would put that word."
    me "It's much worse than that."
    me "I think of you as a part of me - the one without which I am incomplete. It's like I'm non-existent, and I'd curl up next to you."
    me "But there is no you."
    "There was nowhere to go and no reason to go."
    "I would have met the ninety-third here and gone with chest on the tanks."
    "And in passers-by I would always look for her eyes."
    "The worst thing about any dream is that you wake up from it."
    if herc:
        "But while the eyes were still closed, I need to tell her about the boy with green eyes and long bangs who had the last name Sychev, and about the girl who was two years younger than him."
    else:
        "But while the eyes were still closed, I need to tell her about the boy with green eyes and long bangs who had the last name Persunov, and about the girl who was two years younger than him."
    "They are beautiful, for they are her children."
    $renpy.notify('«The Fly» - Baron Stieglitz Art School.')
    "And we meet the year two thousand and twentieth, and no one rushes to conquer us, and our grown-up children storm «The Fly» as their mother once stormed it."
    "The touch of icy lips is like a farewell gesture."
    "A pebble-lined «Lena» near the head."
    "And the painful bruise under the eye: I had to punch myself in the face with my fist as hard as I could to force myself - just dare - to throw the first handful of sand on her face."
    th "I guess... I guess that's it?"
    th "What do you think?"
    "No one answered me."
    stop music fadeout 5
    "Everybody left me. And Lena. Even my damn inner voice."
    "A face lifted to the night sky with eyes full of tears."
    "And a wolf's howl into the lifeless sky."
    me "Damn you all."
    "In a voice ringing with tension, I say."
    me "Take me away from here."
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    play music music_7dl["misery"] fadein 5
    scene op_back with dissolve2
    "At six o'clock and forty-one minutes, the space on the back lot of Route 410, following from the Volga Recreation Center, the former Sovyonok Pioneer Camp, crumpled up and spit out a young man."
    play ambience ambience_cold_wind_loop fadein 3
    scene bg intro_xx with fade
    pause(3)
    "I was not dressed for the weather - a light, short-sleeved shirt, shorts - all covered in some brown streaks and sand."
    "Space tossed me to my favorite spot above the wheel, and there it froze me, leaving me with what was left."
    "Not much was left - something extremely important was left where I came back from. Something died there."
    "I guess it makes sense that of all the hickeys in the universe, I'm the only one who's ever had the misfortune to end up where I ended up."
    with fade
    "I used to break acquaintances easier than make new ones."
    "I'm a person who doesn't exist. {w}And if anything happened to me, no one would know anything about it for a long, long time."
    "Like that story about the French retiree who, after he died, lay in his apartment so long that he was mummified before the cops took the door off its hinges."
    "Yanked forward by inertia, and pneumatics hissed hysterically, folding the door in an accordion. {w}My stop."
    play sound sfx_intro_bus_stop_steps
    pause(3)
    scene anim intro_4 with fade
    "I was carried outside, in one summer shirt, toward the icy, pre-New Year's Eve Peter."
    "The scarlet neck handkerchief, torn off with anger, flew to the side and spread itself out in a blood-red splotch on the virgin white of the snowfield."
    "And I grabbed my temples, trying to keep the sobs from bursting out."
    scene anim intro_3 with fade
    "What have you done, girl...Why, why!"
    scene anim intro_8 with fade
    "It's so comfortable to walk against the wind, pretending to blink away unwanted tears, and not caring about the cold somehow, when everything inside is frozen solid."
    "This must be the «red corridor» that any suicidal man passes through in his selfish quest for self-destruction."
    "Tears fog the eye and immediately accumulate in the corners of the eyes as icy crusts solidifying the grotesque makeup of a sad clown."
    "Wiping my eyes with my sleeve moment by moment, I move on autopilot toward the den, and after another turn, it opens."
    scene bg int_home_lift_7dl
    with fade2
    "Well, hello, unloved and unkind home."
    play ambience ambience_7dl["elevator"] fadein 3
    "I pushed the jerked concierge aside without looking, and it was only a few moments later in the elevator, idly noting the clanking of the shutters, I realized that my mind had absolutely no sense of the floor whose button my fingers had chosen."
    "It might be for the best."
    "I cowered in the far dark corner and sat on the floor, pressing my knees to my chest."
    "Why did I come back?"
    "What am I to do here?"
    show blackout
    "Fifth floor, the lights always go out for a split second here because of a faulty joint in the carriers. {w}For someone who blinks, it won't even be noticeable."
    "But reflexes honed by network battles make it possible to track it, too."
    "Like the fact that the mirror has stopped displaying a slouching figure in a stained white shirt and idiotic pioneer-style short pants."
    stop music fadeout 3
    "Now there was she."
    $ persistent.sprite_time = "day"
    stop ambience fadeout 3
    play music music_7dl["meetmethere_tts"] fadein 5
    scene anim prolog_2
    show un serious dress
    show prologue_dream
    with dspr
    me "Lena."
    "I swallowed the bitter lump in my throat with difficulty, putting my palm to the cold glass."
    me "Why... {w}Why? {w}Couldn't we have..."
    hide un
    scene anim prolog_1
    show un serious dress anim
    show prologue_dream
    with dissolve2
    un "We couldn't, Semyon."
    "She shook her head."
    un "No one stopped you from taking me as I am. {w}Without a second thought, without a doubt."
    if alt_day_binder != 1:
        un "I loved you from the first day, from that meeting at the clubs. {w}How could you not see that?"
    else:
        un "Since the day I first saw you on that bench."
    me "But did I have the right to interfere?  {w}I was in a strange world, a strange time..."
    un "Meanness is not measured in years and kilometers, Semyon."
    un "You intervened already when you didn't chase me away. {w}You gave me hope you had no right to give."
    un "And that's the worst part - it's like you killed me yourself, fed me those pills."
    un "I don't care anymore. {w}Now you have to live with it."
    "It dripped off the mirror with drops of blood and the radial pattern of a cracked mirror under the fist."
    play sound sfx_broken_dish
    scene anim prolog_2
    with vpunch
    un "And I will never be again."
    me "LEENAAAAA!!!" with vpunch
    "I shouted, panting."
    hide un with pixellate
    "It's no use. {w}She's gone. {w}And will never be again."
    "Besides, my floor... {w}My floor was beyond number seven, and the elevator rumbled past."
    scene bg int_home_lift_7dl
    show blackout
    with fade2
    "From the speaker hissed another commercial, and the information panel was occupied by another «Jeans» with its naively threatening mournful «no adverts allowed» chants."
    "They say that if grief becomes too much, the body loses what little self-preservation instinct it has left and can stop the heart on its own."
    "But that's not me, and for that I hate myself even more - even an empty shell clings to the remnants of existence for some unknown reason."
    "And they also say that New Year's Eve is the most magical time in which the most cherished dreams come true."
    "Memory goes sector by sector again, throwing out alternate plots, developments of events and what could have happened."
    "It's called eidetic reduction, and if you really want to, you can relive several lives at once, cramming days into seconds."
    "And my heart sinks at the amount of meanness, filth and lies, like a boot print on a clean carpet, that I left behind at the «Sovyonok»."
    "If Alisa, Slavya, Miku come after Lena..."
    "It can't be ruled out that everything that's been happening to me for the past week is giddy delirium, take for example the fact that I've managed to get close to a girl like Lena in a week."
    "But then what is reality? {w}That which can be touched, smelled, tasted?"
    "If I remember the taste of skin, if my fingers remember the touch, and the suffocatingly luscious smell of half-decomposed pills seems to be embedded in the mucosa of my nose."
    "The heart remembers. {w}Which means that reality has more right to exist than the dumb house nine floors below."
    stop ambience fadeout 3
    "I stifled the body-pounding tremor by pushing it inside and, burning myself on the icy steps of the ladder, climbed up to the trapdoor to the attic."
    play sound sfx_fall_metal_door
    "The lock was never here, so a few minutes later I was already on the roof."
    scene anim intro_2
    play ambience ambience_cold_wind_loop fadein 3
    with fade
    "I'm not a crying gymnasium girl who cuts her wrists for lack of attention, nor am I an emo kid who's decided he's just in everyone's way."
    "I'm just done. There on the beach, throwing the first handful of burial earth on the face I love."
    play sound_loop sfx_street_traffic_outside fadein 2
    with dissolve
    "So don't shake, don't dare."
    "At least now, don't shiver and dirty up a magical evening with your reflections."
    "Especially since right beneath my feet, far below, bristled with such pertinent concrete blocks blocking the driveway to the house. It's going to be very quick, very ugly."
    "And very surely."
    "Only a firearm would give a greater guarantee, but where would one get one?"
    "I have made my most important wish, my deepest wish."
    "It's bound to come true: it's New Year's Eve. The most magical time."
    "Turned my back on the abyss and,"
    scene anim intro_1 with dissolve
    play sound sfx_wind_gust
    extend " spreading my arms, rolled over into the icy embrace of the wind."
    scene cg d7_un_epilogue_bad_7dl:
        xalign 0.5 yalign 0.5 zoom 1.45
        linear 3.5 zoom 1.0 xalign 0.5 yalign 0.45
    pause(3)
    "And three kilometers to the west, a green-eyed brunette cried out, waking up, clutching her heart and crying softly."
    un "It will."
    play sound sfx_7dl["mpbt"] fadein 6
    scene white
    show spill_red
    with flash
    pause(2)
    scene cg d7_un_epilogue_bad2_7dl
    show spill_red
    show alt_credits "Will you go with me?" with dissolve2:
        pos (747,115)
    with flash
    pause(6)
    stop sound_loop fadeout 0
    scene anim prolog_2 with fade3
    "\[Bad ending unlocked - «Dream on»\]"
    pause(4.4)
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("un_7dl_bad")
    show acm_logo_un_7dl_bad with moveinright:
        pos (1600, 1020)
    pause(4.4)
    with vpunch
    call alt_7dl_titles
    pause(2)
    return

label alt_day7_un_7dl_departure:
    play music music_7dl["tilltheend"] fadein 3
    scene cg d7_un_modern_epilogue_bus_7dl with dissolve
    play sound_loop sfx_bus_interior_moving fadein 2
    "How many things there were, how many things could have been."
    "I still didn't understand: was that epic bathroom scene real, or was I really dreaming it all?"
    "And if I had dreamed it all, where had the whole morning of my seventh day gone?"
    "But I didn't care too much about that right now."
    "After all, she was there for me, and as far as possible, everything was go{w=.3}od{w=.3}!"
    "Although I don't believe in too much «good» and out of my long-standing habit of looking for a catch even where there isn't and shouldn't be one."
    "Now, for instance - we had a warm, summer romance that ended with us arriving separately but leaving together."
    "I almost said «resort», but it's a little more serious than that."
    "Only time will tell how much more serious."
    scene bg int_bus_people_night with fade2
    "The day outside the window changed to evening, then to night."
    "Time, while we were around, flew by."
    "She was still in her modernized pioneer outfit, with her shirt half unbuttoned and her neckerchief missing."
    "And to my reasonable question, she replied that the uniform belonged to her, that she'd been wearing her shirt like that all her life, and in fact, Aliska had copied everything from her."
    th "Well yes, yes, of course."
    "I smiled and watched her chortle."
    th "How you've changed, girl..."
    "Or maybe it's just that she's always been like that, she just couldn't show her real self with outsiders."
    "Something must have connected her and Dvachevskaya, after all!"
    "Something..."
    "I didn't have time to think it through."
    stop sound_loop
    scene bg int_bus_night with fade2
    "Two things happened at the same time:"
    "I caught her palm and squeezed it gently, struggling with an unforeseen fear."
    "And the image outside the window faded, lost its colors."
    me "What..."
    "I realized the bus had stopped."
    "And we were alone in the cabin - me, Lena and my Tyler Durden."
    dreamgirl "It's been a hell of a week, Semchik."
    th "You sound like you're saying goodbye..."
    dreamgirl "I am."
    dreamgirl "You know what to do, don't you?"
    "After thinking for a moment, I shrugged my shoulders."
    "Of course I didn't know."
    "This is my first time here, I'm completely clueless about the rules of the game, and I have no idea what I should do in order to get a particular result!"
    "And yet something inside was calm."
    "Knowledgeable."
    show blink
    scene black
    "My eyes began to slip."
    if alt_day_binder != 1:
        "Someone big and kind is leading me down the street, and he has huge stiff palms, in which it is so comfortable to warm my fingers, chilled with frost."
        th "Father..."
        "He knows everything, he can do everything."
        "My first sincere wish is to be the same."
        voice "Sometimes you just have to keep your happiness."
        voice "Just take it and don't let it go."
        "The warm palm unclenched, leaving me alone on a gray street littered with faceless pedestrians."
        "Alone against a whole hostile world."
        voice "After all, if you are so easily willing to part with the most important thing - maybe it wasn't so important?"
        voice "Goodbye."
        if persistent.alt_binder:
            menu:
                "No!":
                    pass
                "My story ends here":
                    $ alt_day7_un_7dl_shard_end = True
                    return
        else:
            th "No!"
        "I closed my eyes and summoned up the remnants of that ten-million-dollar sense of direction that has always been with me, always helped me find the right path."
        "And as I listened to it, I turned, took a deep breath."
        "Ran."
        "And found the only colors in the world."
        "The only person who cared."
        "And with all the strength in the fingers of a five-year-old child, he grabbed, squeezed his hand."
    else:
        "And while I was asleep, someone pushed back the backdrops with the decorations."
        "And forgot to put the new ones in."
    stop ambience fadeout 2
    $ persistent.sprite_time = "night"
    $ night_time()
    scene emptiness_7dl behind int_bus
    show int_bus_7dl
    with fade
    if karma >= 75:
        dreamgirl "You're on your own from here on."
        dreamgirl "Try to play your cards right, so it's not all for nothing."
        th "What? What do you mean?"
        "There was no answer. Instead, I felt terribly tired, as if I'd been accumulating it all this crazy week."
        "The last thing I saw was Lena sleeping peacefully in the seat next to me."
        "Consciousness fell asleep."
    else:
        dreamgirl "Okay, let's just do this and go our separate ways."
        me "Do what?"
        dreamgirl "Forget the regulations? {w}Magic girls have no place in the land of domesticity."
        dreamgirl "Kiss her quick, before she completely loses her materiality, and goodbye."
        show un sorrow modern tr1 with dissolve
        "I turned to Lena, who resembled an immaterial shadow."
        "She looked stern and sad, as if she understood something extremely important."
        un "You knew, didn't you?"
        "Quietly she whispered."
        show un sorrow modern tr2 with dissolve
        un "Knew it all from the beginning..."
        "She was dissolving into the thin air."
        un "And still tried."
        "The creepiest thing was that there wasn't an ounce of accusation in her eyes."
        "Only the quiet and humble expectation that she would..."
        show un sorrow modern tr3 with dissolve
        me "No, that's not true: I knew nothing, nothing - I swear to you."
        "I tried to catch her hand, but my fingers went through."
        dreamgirl "Farewell."
        show un modern tr4 with dissolve
        un "Farewell."
        "The voice is gone."
        "A barely discernible silhouette is left of Lena."
        me "Hey, I didn't sign up for that!!!" with vpunch
        "I hit the innocent back of the chair in front of me with all my might."
        me "You can't do that, you hear?!"
        me "Why let it attach to a man and then take him away?"
        me "You can't do that, it's cruel, it's wrong..."
        "Not fair."
        "I grinned bitterly."
        "What should I do? Live and work and wait for you to come? Syom, there's something wrong with your eyes... No... It's all right. It's the rain."
        if persistent.mt_7dl_good and (alt_day4_me_neu_transit == ''):
            "I felt as empty and impersonal as the darkness surrounding the bus."
            "And no matter what I thought about, no matter what I wanted, it essentially came down to one simple question:"
            menu:
                "Do I deserve a miracle?":
                    "And I knew very well I don't."
                    "I don't."
                    "And even if I do... This question would be followed by others, pulling out things I never knew or remembered."
                    "But ignorance has never absolved anyone of responsibility."
                    "I curled up in a ball on the chair and closed my eyes."
                    $ alt_day7_un_7dl_rej_end = True
                    return
                "Will you go with me?":
                    scene bg int_bus_night:
                        zoom 1.0 xalign 0.5 yalign 0.4
                        linear 6.0 zoom 2.0 xalign 0.5 yalign 0.4
        "Just beyond the cut of the steps, beyond the open doorway, was a black, featureless void."
        "In which there was absolutely nothing."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade2
    return

label alt_day7_un_7dl_good_ussr:
    scene black
    with fade3
    pause(3)
    $ set_mode_nvl()
    $ prolog_time()
    play music music_7dl["please_reprise"] fadein 3
    "I'm unneeded."
    "In a little over thirty years, I've learned absolutely nothing that could be really useful, detached from civilization."
    if loki:
        "Music? Songs and dances? I'm pretty good at that."
        "But if there's no instrument?"
        "Or if people just don't want what I like?"
    elif herc:
        "A security guard? Please."
        "Sales manager? Even worse."
    else:
        "The same French novel in which the most useless members of mankind were stranded on a desert island came to mind periodically."
        "Bureaucrats, pop singers, political technologists, psychoanalysts, PR executives."
        "And, of course, our artel."
        "Designers."
    "I can't do anything."
    "Wasn't capable of anything."
    "To fix, assemble, chisel, debug - I could hardly even make my own lunch, if it was more complicated than pasta and a half-finished cutlet."
    "Gotta learn something."
    "Become something."
    "Otherwise, what's the point?"
    nvl clear
    "Why did I need camp, summer, Lena?"
    "Thanks a lot to Slavyana - she really helped me get settled in a new place."
    "After those scenes on the beach and in the woods, I seriously began to hate her, but after all she had done for me, I could no longer hold a grudge against her."
    "She told me about the connection between Lena's previous suitor and me."
    "The only difference was that he left and I didn't."
    nvl clear
    "My parents here, though they were strangely aloof, helped me get a room in the dormitory in Kalinin and transferred me to the local school, in the tenth grade."
    "I seriously feared that they would persuade me to go to Cuba with them, but that didn't happen."
    "I told them about my plans, and they just looked at me with surprise and decided not to get in my way."
    "It wasn't without the help of Olga, who promised my parents to keep an eye on her former ward."
    "After all, it wasn't her first time."
    "Another year I was in school, and in May of '90 I got drafted."
    "Of course, I remembered the hazing, the horrors of the military, the fact that for two years I would be torn from my most precious."
    "But now I felt I was doing something very good."
    "Something very right."
    "And, after finishing my farewell to a civilian with a traditional feast, I showed up at the military recruitment office the morning of October 11, 1990, with my things."
    "Someone suggested that I take a pass by mentioning my parents, but that wasn't part of my plan."
    "I needed a military ID to achieve my goal."
    "In my world it was of no use in normal life, but it's different here."
    nvl clear
    "After a series of tests, I was deemed fit to do anything other than swing a shovel."
    "But that will come later, after the young fighter's course."
    nvl clear
    "The ninety-first year I met under the shoulder straps, and with a dreadful sinking in my heart awaited the beginning of what had once happened in my past."
    "But month after month passed, and all the decent deadlines for perestroika had been missed, and USSR was still standing, and still was going to stand, by all appearances."
    "Hence I concluded that I was not quite in my own world, and the journey was not through time at all."
    "Which means..."
    nvl clear
    "I was supposed to meet the ninety-third as a civilian, armed with knowledge of the future."
    "But here my knowledge didn't work."
    "So I applied to Kuybyshevka with a clear conscience."
    "Studying was easy: I had been attracted to airplanes all my life, my coordination of movements was all right all my life, and my technical mindset allowed me to absorb knowledge like a sponge."
    "It wasn't exactly service, so I saw Lena from time to time - she had grown up, got prettier, and listened to my request after all."
    "Except that seeing each other was depressingly rare - it was a long way from Kuibyshev to Leningrad, and every meeting was a grand event."
    "But that must have been how it really was."
    nvl clear
    "School, flying, school, flying..."
    "We signed our names in '95, when Lena graduated from Mukhinskoe."
    "For a couple of years after that, though, she kept arguing, signing her paintings «Tikhonova» out of habit, and I reminded her that she was now a married lady."
    "Leningrad won her over."
    "No wonder."
    "So we moved there pretty quickly for permanent residence."
    "Lilya Alekseevna Persunova, in common parlance - grandmother, who lived there, helped me a lot with the move."
    nvl clear
    "After a few more years of grueling training, education, and tests."
    "In spite of the acute lack of time, we managed to find time to see the camp kids."
    "And once I even met our Violetta Cernovna!"
    "We crossed paths during another physical, where she was invited as a psychiatric specialist."
    "Yes, it was a hard, crazy time. But all my efforts paid off."
    nvl clear
    "And here I sit in a nearly horizontal unfolded chair, automatically checking the device readings."
    voice "Ground - Board."
    "I nodded and lifted my thumb - the telemetry catches."
    voice "How are you feeling?"
    me "Excited."
    "Honestly, I answered."
    "Who wouldn't be?"
    voice "Preliminary... Main... Up!"
    "And I covered my eyes, gratefully accepting the painfully familiar overload."
    "Overload means inertia, inertia means motion, motion means life."
    nvl clear
    voice "Registering takeoff."
    me "Affirmative.Well, let's go."
    voice "Fifteen seconds of flight, no problems."
    voice "The stage engines are operating normally."
    "I nod, watching the fuel readings."
    "Overload increasing slowly but steadily."
    voice "One minute into the flight, readings are normal."
    "Just a few more minutes, and I'll feel that lingering drop."
    "The gentle embrace of space."
    "No matter how much you prepare, you can never be completely ready."
    stop music fadeout 3
    nvl clear
    scene stars
    play music music_7dl["ppk"] fadein 3
    "It's a little shaky, but it's all within normal limits."
    voice "Board, what's that black mirror you have in your camera?"
    me "That's mine."
    me "Haven't exceeded weight limits."
    voice "Yeah, we got it."
    voice "Talisman, huh?"
    me "Sort of. Feeling normal."
    "Overloads are rising."
    "The step is gone."
    "The fairings..."
    "And..."
    scene cg d7_un_epilogue_d1_7dl with flash
    $ set_mode_adv()
    me "Hello, dream."
    "I don't know what to compare that feeling to."
    "When you can fit a fragile blue ball in the palm of your hand."
    "And you are separated from the abyss of the universe by only a few centimeters of skin and insulation."
    voice "Board, ground."
    "I was checking the clasps of the scaffold, so I didn't answer right away."
    me "Yes?"
    voice "The maternity hospital called. You have a son."
    me "Roger that. Thank you. Stand down."
    "The hands holding the swivel wheel trembled subtly."
    voice "Board, your pulse is racing, breathe out."
    me "Yes..."
    "I answered."
    me "Yes..."
    "Tears in weightlessness gather in balloons, almost invisible in the harsh, shadowless light of our little star."
    "A smartphone from a company that never existed."
    "And a picture of a girl who once cared."
    nvl clear
    "Whoever you are, wherever you are."
    "Thank you, Demiurge."
    "Thank you."
    "I stroked the transparent plate that hid a picture of a very pretty girl in a pioneer uniform - our «Falcons» allowed excesses for some."
    "Stretched out palm toward the Earth."
    "And waved."
    scene bg ext_earth_7dl with dissolve
    show frame at truecenter with dspr
    $ set_mode_adv()
    me "There are so many good things ahead."
    show frame at truecenter:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 0.5 zoom 1.0 xalign 0.7 yalign 0.5
    show cam_ui at truecenter:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 0.5 zoom 1.0 xalign 0.6 yalign 0.5
    "Ahead - whole life!"
    pause(1)
    play sound sfx_7dl["snap"] fadein 0
    scene white with flash
    pause(1)
    scene bg ext_earth_7dl
    scene anim prolog_2 with fade3
    "\[Good USSR ending unlocked - «Unneeded»\]"
    pause(4.4)
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("un_7dl_good_ussr")
    show acm_logo_un_7dl_good_ussr with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    pause(2)
    return

label alt_day7_un_7dl_good_rf:
    scene emptiness_7dl behind int_bus
    show int_bus_7dl
    with dissolve
    th "Like hell it was!"
    "I moved into the driver's seat and, after thinking for a while, remembered where which pedal was located."
    "The gas, I think, was on the right."
    "I pressed the door-lock button and pushed the pedal to the floor."
    "The bus lurched forward, piercing the emptiness."
    scene black
    with dissolve
    $ prolog_time()
    "And this time I didn't wake up on a bench or under a blanket or anywhere else."
    "I woke up in my goddamn reality feeling like I was some dorky hero of some dorky computer game who had just passed the last level, kicked the last boss, and become irrelevant."
    "As is always the case with computer game heroes."
    stop ambience
    play music music_list["raindrops"] fadein 3
    pause(3)
    scene anim prolog_2
    $ set_mode_nvl()
    with fade
    "As I had expected, providence played a cruel joke on me, waking me up in that unfortunate «LIAZ», a mere fifteen minutes after I had closed my eyes."
    if loki:
        "I jumped into the subway, fleeing the bitter cold, realizing that I missed something somewhere."
        "It wasn't until I checked my pockets again that I realized there was no player!"
        "Something inside me twitched at the memory of holding it in front of my nose, dangling on the wire like a mouse by the tail, and typing names, addresses, contacts into it."
        "And across sits a girl."
        "Time heals, after all. You just gotta let it run its course."
        "I passed both Krestovsky Island and Staraya Derevnya, only coming to my senses at the terminus."
        "And when I got off at Komendantsky, I sat down on a bench in the lobby, struggling with a pounding heart, afraid to believe in the reality of the miracle that had happened."
        "Isn't that..."
    elif herc:
        "And as I got off the bus, I frantically leaned against the metal support of the bus stop - suddenly I felt dizzy, and it was as if a door had been opened in my memory."
        "And summer memories rushed into my head - kids, camp, summer."
        "Lena."
        "Still, it was good damn seven days."
        "The memory spring unwound and unwound until a picture came into view - the last frame before the whole story began."
        "And if you believe that all reality depends only on you and your actions, the most sensible thing to do would be to take me out of the tonight's equation."
    else:
        "He and I pretended that I'd just dreamt the whole thing - except for the player being missing - probably stolen on the bus - and the smartphone being empty - I was listening to music, you know."
        "I went out at night and rushed to work - my services were suddenly required because another headless user decided to download some archive and as a result turned his machine, as well as the entire local cluster, into a bitcoin mining system."
        "It's not the first time, no big deal."
    nvl clear
    if loki:
        "I don't remember how long I sat like that, but when I got up, I didn't remember the arrangement with Oksana or what my life had become in the last ten years."
        "It had all lost meaning."
        "My old enemy-lover-traitor friend tried to throw me a tantrum, but rattled off to the blacklist with no mercy."
        $renpy.notify('«Mr. Freeman» - an animated web series that appeared on YouTube on September 21, 2009, and has gained considerable popularity in Ru. segment of internet.')
        "I sat back and mercilessly cut out of my life whatever was pulling me to the ground - in full compliance with Mr. Freeman's postulate: do you have the guts to format your computer's hard drive?"
        "I have. And yes, although it reeks of suicide, there is no more effective way to start over."
    elif herc:
        "All I had to do was dial my bosses and tell them I was quitting, and no, I didn't care who was working on New Year's Eve or that I wouldn't get paid for my shift."
        "I don't care. Life isn't worth any money."
        "Especially since it doesn't belong to me alone now."
        "I found a place on the bench and sat there, enjoying the way the world around me sounded in a whole new way - without the usual notes of hopelessness."
    else:
        "I didn't notice how the evening flew by during work, so I decided not to go anywhere, instead hiding in my favorite corner, where my favorite board and anonymous people of all stripes were waiting for me."
    "I didn't sit for long - a body that still remembered fervor and youth demanded action. {w}Anything.{w} Preferably aimed at my current super task: to meet a girl named Lena with dignity."
    "I didn't doubt for a second that she would show up sooner or later: if the subconscious includes someone's face in your dream, it means that your life paths have either already crossed or will inevitably cross."
    "And I didn't think of camp as anything other than a dream now."
    "I ravaged the card, bought myself some shaving supplies, some household chemicals, and spent the next few days cleaning out the den until I turned it into something more or less decent.{w} Of course, it would be nice to get some repairs done here, but that'll do for now."
    "Numerous bottles, pouches, and bags fit into four large trash bags, and taking each one out was like bringing the day of Lena's arrival into my life closer."
    nvl clear
    if herc:
        "I left my job knowing full well how my previous place had ended, and after dialing a few numbers, I began to prepare for my reinstatement at uni."
        "I may be a bastard and a cynic, but I want to be at least an educated bastard and a cynic - better than sitting around the store."
    else:
        "Colleagues at work began to reach out to me little by little, even my boss noted that I had become noticeably friendlier, more patient, and he raised in salary - a small thing, but a pleasant one."
    "Life began to unfold, taking on a new rhythm and sound."
    if loki:
        "In spite of my depressed alveoli and inability to play, my knowledge of sheet music had not gone anywhere from my poor head."
        "And so one day I got to one of the officers' houses, where I offered myself as conductor."
        "The brass was a little hesitant, but..."
        "I was scheduled for a review hearing in early February."
    else:
        "Finally, I got my hands on one of the officers' houses and got a referral to the orchestra there.{w} They lauhged at me threw me out on the street, but they agreed to put me in the active band if I bought an instrument and tightened up my sound."
    "I began to look at people as equals: there was no more vertical assessment, I could go and smile at them if I was in a good mood, and in the «walkman» - the twin of the one I gave Lena - positive songs were now much more frequent guests."
    nvl clear
    "Lena gave me a taste for life. {w}That, and the impressions  «Sovyonok» gave me, were all I had inside me."
    "And I began to realize, with surprise, that even that was more than enough!"
    "In my search for the application of unexpected energy, I squandered the New Year's holidays, vacations, and all of January."
    play music music_list["everlasting_summer"] fadein 3
    nvl clear
    "But as time went on. My stock of vivacity began to wane, and little by little I began to lean toward the status quo."
    "Some changes, however, were already so firmly ingrained in my skin that I would not give them up for anything. {w}Walking, for instance."
    if loki:
        "That, and the fact that they refused me a conductor's position, but persuaded me to teach solfeggio at one of the schools..."
        "After all, I fooled the detractors, fate and Oksana - and still connected my life with music. Even if a little differently than I had planned from the beginning."
        "I suddenly woke up to a very long dormant talent for putting notes together into compositions that I played out with my charges."
        "So now I was walking along humming something, already imagining what it would sound like in an arrangement of basses and tenors."
    else:
        "I loved walking with earplugs all over again. {w}When I was eighteen, I preferred to plug my ears with Amica or Tricky and go wandering in the rain more than any other entertainment."
        "That very, very special relationship with the primordial nature of water. And that habit came back to me, so I wasn't the least bit hesitant when it snowed outside the window."
    "Loneliness is when two hundred rubles on the account is enough for four months, and one full charge is enough for a week. I felt lonely even in the thickest of crowds, and the music pouring into my soul only exacerbated that impression."
    "But for the first time in many years this loneliness was not negative - it was calm and light, half consisting of gratitude for the miracle and the other half..."
    "It was a doomed and quiet expectation."
    "I wasn't praying, I wasn't begging - I was just winding laps through the icy mush of Petersburg and waiting for us to finally meet."
    nvl clear
    scene bg ext_city_night_7dl with dissolve
    "The route I was accustomed to was from Moskovsky Station through all of Nevsky, turning to Dvortsovaya, and across the bridges, past the Rostral Columns, on to the Aurora..."
    "I didn't demand a miracle - I just waited patiently for it to happen at last, and wandered along the embankment, guiding the rough granite of the facing with my palm, jumping at the joints."
    un "Happy Valentine's Day!"
    "A familiar, familiar but somehow very strained voice came from behind me."
    "I, not believing my own ears, turned around. {w}Lena. {w}Lena?!"
    "Just a couple kissing."
    "I must have imagined it."
    nvl clear
    "I, shuddering, turned to go on, and again I heard the familiar voice."
    un "Semyon. I am here."
    "A gust of wind carried to me the tones of laughter belonging to only one being in this universe."
    th "Where did that voice come from?!"
    "I looked around."
    "And I found it."
    "It was like a cold, wet brush on my back, a metallic taste in my mouth..."
    "I, not believing my own eyes, took a few steps on trembling legs, hating myself for my inability to express emotion, for my tongue being wooden and my back slouching."
    me "Thank you."
    "My voice was disobedient and sounded more like a cackle."
    me "And...to You."
    $renpy.notify('In Russian language you (1 person) and you (2+ persons) are different words, second variant could be also used when talking to strangers.')
    un "Us?"
    "She smiled tensely."
    un "Or are you and I talking by «You» now?"
    th "We? With you? We are strangers."
    nvl clear
    pause(3)
    scene cg d7_un_met_7dl
    "She was sitting behind the wheel of a «Beetle» parked nearby - unfamiliar, grown-up, confident. And, of course, no purple hair or tails. Just familiar facial features, just familiar bottomless eyes."
    un "I've been looking for you so..."
    "She whispered, giving me a chance to read her lips."
    "The icy wind from the Neva intensified: its icy fingers crept under my coat and mistook there."
    "She opened the door and nodded."
    un "Get in. We have so much to discuss..."
    "Still the same unsmiling one."
    "And even if she's not the modest girl I was used to - this Lena was clearer to me - an adult."
    "All those convex character traits that would inevitably flatten with age, all those flashy details of appearance - all gone into oblivion, leaving a lovely young woman about my age. And even if there were a few silver streaks in her hair, even if there were faint wrinkles in the corners of her eyes..."
    "But at the bottom of the green abyss, the evil devils snapped their tails, and for a moment I saw the one I had longed for, the one I wanted."
    "The one."
    "And I climbed into the warm womb of the Nissan next to Lena."
    nvl clear
    pause(3)
    me "Nice car."
    "Average walking fan neutrally praised car enjoyer."
    un "Very. After a bunch of swaps and moving to where you used to live, I had to choose between it and a renovation."
    un "I lived for two months where the walls remembered you before you showed up at Sovyonok. {w}And two more months before I intercepted you at the Arrow."
    un "You made me run around a lot..."
    "She tried to smile, but instead she cried somehow quietly - how only a person, who is trying to live up to some point on stubbornness solely and finally getting to it can cry..."
    "And, guided by some instinct, I leaned toward her and lightly touched my lips to the girl's temple."
    "Her tears dried in amazement, and she stared at me."
    me "Here we go."
    nvl clear
    pause(3)
    scene anim prolog_2
    un "Can you imagine that set-up with the bus!"
    "Excitedly, she said half an hour later, as we turned into one of my favorite coffee shops on Gorkovskaya and grabbed each other a pastry and coffee."
    un "I remember running away from you, from the whole camp, and you found me."
    un "Didn't forget, brought me back and sat with me until departure."
    "She shrugged her shoulders."
    un "And at the same time for some reason I remember hesitating between the knife and the pills, and I chose the pills."
    "She smiled unabashedly, staring diligently into the table, and I couldn't bring myself to reach out and just touch."
    un "Just thought I'd be covered in blood and you'd find me like this.{w} Didn't want to get you dirty."
    if dr:
        me "And praise be to Random that it wasn't a knife. I don't know how to revive bloodletters. And I'm very afraid of the sight of blood."
    else:
        me "And praise be to Random that it wasn't a knife. I don't know how to revive bloodletters."
    "Outside the window, the breath of the metropolis rumbled quietly, and she had an alluring look, just the tiniest bit tainted by insecurity."
    "And then we got on the bus, and I opened my eyes already behind the wheel, standing in traffic on Dalnevostochny. I sobbed into the steering wheel like a jerk when I realized I'd imagined the whole thing."
    "She looked at me with some incomprehensible hint, but I didn't understand anything and just shrugged."
    un "And then."
    "Slowly she said."
    nvl clear
    un "I took the player out of my pocket. A player, you know! Of course, little wonder about the player - though I prefer to listen to music on a boombox."
    pause(3)
    "I was frankly admiring the current her."
    "The way she waves, the way she breathes, even the fact that her hair isn't purple, but banal black. But I've always loved brunettes, so that only makes me feel better."
    "I watched the movement of her lips, her pearly teeth, the glow of headlights from passing cars reflected in her eyes. Tall, in impractical gray suede boots and a burgundy coat that would be warm except in the womb of a «Beetle»."
    un "Much more surprising was in the recorder folder, where the first entry was that stupid message to future us."
    un "Remember?"
    me "Yes."
    un "It had my voice on it, a child's voice."
    un "And yours."
    nvl clear
    pause(3)
    "She took a sip of coffee, grimaced, and, retreating to the counter, fetched a small glass of Irish «Baileys»."
    un "My nerves went to hell. {w}I went through the whole car. Three times! Even considered tearing off the upholstery and panels. But the result was the same: I couldn't find the piece of paper you wrote down your contacts. It seemed to have evaporated."
    stop music fadeout 5
    me "And I was just waiting for you to show up. {w}There was no chance we wouldn't meet."
    "Lena smiled and held out one earpiece to me."
    nvl clear
    pause(3)
    scene cg d7_un_take_my_hand_7dl with dissolve
    play music music_7dl["happy_ending"] fadein 5
    "And there someone's very familiar voice said:"
    me "{i}Give me today's date{/i}."
    un "{i}The twenty-second of July, one thousand nine hundred and eighty-nine{/i}."
    me "{i}Record zero, certifying{/i}."
    me "{i}My name is Semyon{/i}."
    me "{i}Hi. Just hi{/i}."
    me "{i}I'm really embarrassed to say hi to you in the future, hugging the real you, but - I have to!{/i}"
    me "{i}How are you doing? How's your mood? Do you remember what position we were in when this voice was recorded? My voice letter to you in the future{/i}."
    me "{i}My kiss to you from the past{/i}."
    me "{i}Love is measured by the measure of forgiveness, affection by the pain of farewell. {w}And hatred - by the strength of the disgust, with which you remember your promises{/i}."
    me "{i}So what I promised, I do. {w}Further is your turn: will you succeed, and more importantly, will you keep your promises? {/i}"
    un "{i}What is it that I promised you?{/i}"
    me "{i}What do you mean, have you forgotten?!{/i}"
    "The recording is interrupted at the girl's squeak."
    nvl clear
    pause(3)
    show blackout_exh2
    me "{i}Record number one. The date is the same, half an hour later{/i}."
    me "{i}Where were we? Yep, salutations from the past{/i}."
    me "{i}Say hello to Lena, Lena!{/i}"
    un "{i}Hi there!{/i}"
    me "{i}I don't quite understand how this mechanism works, but if you open your eyes in a time objectively close to me, not a word from here will be a mystery to you{/i}."
    me "{i}Although the present you are now staring at me as if I had suddenly grown a second head{/i}."
    un "{i}So you're from the future, then?{/i}"
    me "{i}Everything is relative{/i}."
    me "{i}From my point of view, I'm from the present. {w} And you are from the past{/i}."
    un "{i}And what's it like out there in your present?{/i}"
    me "{i}There's a lot of pain. Almost as much as indifference{/i}."
    me "{i}And more than anywhere else, the law of «homo homini lupus est» is relevant{/i}."
    un "{i}How can you complain, it's your home!{/i}"
    me "{i}Simple to the point of banality. My home is where my heart is. {w}And my heart is where you are{/i}."
    un "{i}Are you hoping there's another me there, too? The other me?{/i}"
    me "{i}The answer is no - to all parts of the question{/i}."
    me "{i}I don't hope, I absolutely know, that somewhere in my city there is you.{/i}."
    un "{i}W-what?{/i}"
    "I remembered the face she made after those words, and involuntarily smiled."
    me "{i}Come on…{/i}"
    "A soft sigh."
    me "{i}Find me. {w}Just find me{/i}."
    hide blackout_exh2 with dissolve
    nvl clear
    pause(3)
    "With a quiet click, the recording cut off, and I returned the earpiece to its owner."
    "Lena smiled."
    un "There, I found you. Can I give you your player back now?"
    me "No. Why? Are you going anywhere?"
    nvl clear
    pause(3)
    "We went outside and were awkwardly silent for a while, gazing one at the other."
    me "So..."
    "We started at the same time - and laughed."
    me "You first."
    un "No, you."
    me "Okay. I was thinking about camp. Why don't we pick up where we left off?"
    un "You mean where you punch me in the face and call me stupid?"
    "She smiled slyly."
    me "If your house is practicing S&M."
    "I muttered."
    me "No, I mean the place where I kept you awake. You can take your time, though."
    un "Yes. We can take our time now."
    "She spread her arms as I did then - young, in love, and immensely grateful to Fortune for the evening - and laughed toward the heavy leaden sky."
    un "After all, we have our whole lives ahead of us now!"
    $ set_mode_adv()
    scene anim prolog_2 with fade3
    "\[Good RF ending unlocked - «Whole Life Ahead»\]"
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("un_7dl_good_rf")
    show acm_logo_un_7dl_good_rf with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    if persistent.alt_binder:
        call alt_day7_un_7dl_good_rf_ps
    return

label alt_day7_un_7dl_good_rf_ps:
    $ alt_pause(1)
    $ meet('am', "Semyon")
    play sound_loop sfx_bus_interior_moving fadein 3
    scene black
    show prologue_dream
    am "Get up. Your prince rode off into the sunset."
    play music music_7dl["let_me_down"] fadein 4
    scene bg int_bus_people_day
    show am normal pioneer
    show unblink
    show prologue_dream
    with dissolve
    "He shook my head roughly off his shoulder, and my heart sank."
    th "Rode off.."
    th "So it's just like last time?"
    "A chuckle escaped my lips, though my eyes filled treacherously with tears against my will."
    hide am with dissolve
    "The brute turned away from the window with an indifferent face."
    "And beyond the glass, the city was already flickering."
    am "You know it was another man, don't you?"
    un "I know."
    "I squeezed out a pathetic semblance of the caustic smile that Alisa so often displayed."
    un "You want to make fun of me?"
    "He shrugged."
    show am normal pioneer behind prologue_dream with dissolve
    am "Rather understand why you went to him in the first place. Would you settle for an identical copy, with the only defining thing for you being the face?"
    hide am with dissolve
    "Now I've turned my back."
    un "You wouldn't understand anyway."
    "After all, I didn't fully understand everything that's been raging inside me for this insanely short week."
    stop sound_loop fadeout 2
    "The brakes squealed."
    "Olga Dmitrievna began to reassure Ulyana, who had jumped up from her seat, and the rude man suddenly looked right at me."
    show am normal pioneer behind prologue_dream with dissolve
    am "So it was your conscious decision?"
    "I didn't answer."
    show am sad_smile pioneer with dspr
    "He grinned - bitterly, almost sympathetically."
    show am normal2 pioneer close with vpunch
    am "I hope you clearly understand now that the responsibility for your actions rests on your own shoulders?"
    "His hand squeezed my forearm so sharply that I cried out."
    "Not so much from pain as from fright."
    "And his angry eyes literally burned through me."
    show am pathetic pioneer close with dspr
    am "So try not to get any more outsiders involved!"
    hide am with dissolve
    "He got up unceremoniously and moved toward the exit following the others."
    th "Outsiders?"
    "There was a pang of almost forgotten anger in my chest."
    th "She wasn't just standing on the sidelines then!"
    "Dad tapped on the glass, and I rose from my chair with a sigh."
    "It seemed to me that if I took my time a little longer, the brute would get far enough away that I could resist the temptation to take one last look at him."
    "And yet, as I got off the bus, it wasn't my father I was looking for with my eyes at all."
    $ meet('am', "Me")
    stop music fadeout 4.10
    $ alt_pause(1)
    scene black with dissolve2
    $ alt_pause(2)
    scene stars with fade
    $ set_mode_nvl()
    play music music_7dl["iknowit"] fadein 3
    "When I was a kid, I thought the scariest thing was getting a 'D' at school or tearing my new dress."
    "But life immediately laughed at my naivete and showed me that the scariest thing is losing the people you love."
    "It was scary to think that I was only minutes away from death."
    "It was scary to look a loved one in the eye and know that someone else had taken his place."
    "And now the only thing that scares me is my future. The unknown was more frightening than anything I'd ever experienced before."
    nvl clear
    "I began to guess what was going on quickly."
    "Literally the moment my stomach didn't start aching painfully."
    "Nor did it start after a week or two."
    "And then in September, I started throwing up."
    "At school it became unbearable: those who were smarter gave me meaningful looks, and the others..."
    voice "Has your daddy forgotten how to cook?"
    voice "Or did our valiant militia quietly steal the warehouse of moldy stewed stew?"
    "This went on until Alisa smashed one of the particularly sarcastic jokers' noses."
    "Like the time five years ago when he made a joke about Alena's hair falling out."
    $ alt_pause(0.5)
    $ set_mode_adv()
    scene bg ext_childhouse_day_7dl
    show dv normal casual
    with dissolve
    dv "How long are you going to pretend you're okay?"
    "This is the first time we've walked together after school in three years."
    "Alisa was smoking, and I tried not to inhale the smoke: it's not good for..."
    dv "The teachers are already guessing what an interesting situation you're in. Does your father know?"
    "I shook my head, stubbornly looking under my feet. Somehow I felt insanely ashamed in front of Alisa."
    show dv tired casual with dspr
    dv "Oh, you've done a lot of things, Lenka..."
    "She threw her cigarette butt into a pile of wet leaves."
    show dv normal casual with dspr
    dv "Tell him yourself, before the pitiful ones do not bother. It will be easier for him to hear it from you."
    "Alisa didn't ask too many questions, and yet I could see she was bursting with curiosity."
    "The only question was how much of her contrived tact was enough."
    show dv think casual with dspr
    dv "One thing I don't understand: when did you have time?"
    un "Last year."
    show dv surprise casual with dspr
    "My friend's face twisted, and I giggled quietly."
    stop music fadeout 4
    "We all have our secrets, don't we?"
    $ alt_pause(2)
    $ set_mode_nvl()
    play music music_7dl["ineedhim"] fadein 4
    scene bg int_sam_room_7dl with dissolve
    "My father took the news exactly as I expected him to."
    "At first he slapped me in the face and screamed so badly that the neighbors started banging on the radiators."
    "And then he sat at the table and was silent for a long time, pressing his lips together and staring ahead with unseeing eyes."
    "I felt like a traitor."
    "As if I'd just taken and, with a snap of my fingers, shattered all the hopes he'd had for me."
    "I was ashamed to even look up at him."
    "And then he started talking about abortion. Harshly, unapologetically, without even asking my opinion."
    "And it was at that moment that something unknowable, wild and completely alien to me ignited in me: it was as if I had become a bear, ready to tear anyone apart for her cub."
    $ alt_pause(0.5)
    $ set_mode_adv()
    un "If you make me do this, I won't leave this world a chance, do you hear me?"
    un "I'll see it through to the end, and no ambulance will help me!"
    play sound sfx_slam_door_campus
    scene bg int_mt_sam_room_7dl with dissolve
    "I shouted, before I slammed the door of my room."
    "It was cruel."
    scene cg d7_un_cry2_7dl with dissolve
    "I put my hand on my stomach and closed my eyes: cruel but right."
    "I needed this baby. I needed some reason to go on living."
    $ alt_pause(0.3)
    $ set_mode_nvl()
    "What I came to was solely my choice. From the beginning to the end."
    "And when there's no one to blame, there's no reason to be afraid."
    "And for the first time in years, I'm not running away, but facing my fear."
    nvl clear
    "Things will definitely get better."
    "I'll finish evening school, and in a few years I'll go to college."
    "I won't be left without a crust of bread, and my father will always help me."
    "I know he forgave me the moment he started to tear and throw."
    "And even if he's against calling my daughter Alyona, he'll accept that choice. Superstitions are superstitions not to come true, aren't they?"
    $ alt_pause(0.3)
    $ set_mode_adv()
    scene cg d7_un_cry_7dl with dissolve
    un "You're bound to be the happiest girl in the world."
    "Lips stretch involuntarily in a smile."
    un "Much happier than your parents."
    stop music fadeout 5
    $ alt_pause(3)
    return

label alt_day7_un_7dl_true_tran:
    scene bg int_toilet_night_7dl with dissolve
    "I wanted to do so much and say so much."
    "But I am not there, and I have only regrets."
    me "We will surely meet... again."
    show blink
    "I said a phrase that came out of nowhere."
    "Obviously not mine, I don't express myself so flamboyantly, and the setting was..."
    play music music_7dl["exodus"] fadein 3
    scene
    $ renpy.show("bg ext_busstop_dust_7dl", what = Notch("bg ext_busstop_dust_7dl"))
    show unblink
    "I looked up, finding myself somewhere, not at all where I'd closed my eyes."
    "Though my fingers still remembered the touch."
    "Yes, the tired sun was shining from somewhere over my shoulder."
    "I remembered, without any surprise, that the last time I clocked, the moon was already climbing into the sky."
    "But now..."
    "Everything here was gray and flat and unimpressive."
    "A surprisingly accurate cast of my soul."
    "Even when I tripped and, falling down, gave myself a good skinned wrist, the fresh abrasion looked like just a reddish shade of gray."
    "Only a certain cube sticking out in the distance willy-nilly caught my attention."
    "In the absence of alternatives, I headed toward it."
    with fade
    "Distance in this wonderful two-dimensional world was extremely deceptive."
    "I'd been walking for an hour, but the unfortunate cube had only slightly increased in size."
    "Perhaps it was because I was barely walking."
    "Perhaps it was the fact that I was momentarily chasing away the ghost of a girl who had never existed."
    show un sorrow modern tr1 with dspr
    pause(.05)
    hide un
    th "Perhaps, all that I remember, it just wasn't?"
    "A few more hours later I managed to get to the cube."
    "As it turned out, it was a bus stop - an ordinary, concrete bus stop, the kind everyone has seen at least once in their lives."
    "And next to it was a broken highway."
    "Shaking off the bench, I sat down and habitually patted my pockets."
    "Cigarettes turned up in the left one, as they always do."
    "Somehow I've been pretending to be left-handed all my life."
    "But all the same life has always made me work with my right hand - first in the person of my elementary school teacher with the long meter."
    if loki:
        "Then in the form of musical instruments."
        "I {b}had to{/b} learn to use my right hand to grip the pipe."
        "They say, of course, that there are special pipes for left-handers, but I personally have never met them."
        "So I had to do what everyone else does - hold with my right hand, press the valves with my left."
    else:
        "Then, in the image of computer hardware and peripheral manufacturers."
        "Quick keys were impossible, impossible to press with the right hand, it turned out not to be adapted to it."
        if herc:
            "Mouse, keyboard, gaming devices."
            "Even the damn WASD was invented by right-handed people and for right-handed people."
        else:
            "When I bought a tablet with shortcut keys, it turned out that I wasn't allowed to use my left hand because my wrist kept nagging to press something there somewhere."
    "I can't tell you how infuriating that is."
    "That's why things that are symmetrical and equally (un?)comfortable for everyone, I respected."
    "Guns, for instance."
    "Or, here, cigarettes."
    "With a flick of a match, I let out a bluish puff of smoke toward the sky."
    "It was sucked into the low clouds, barely leaving my lungs."
    "The clothes remained the same as they had been in the camp, and it was strange."
    "What was strange, too, was that she was all in some kind of crap."
    "I guess I got dirty while I was trying to pump out..."
    show un sorrow modern tr1 with dspr
    pause(.05)
    hide un
    "I coughed."
    "Ripped my tie and wiped my hands for a long, long time, as if trying to clean not so much my skin as my soul."
    "The feeling of being soiled, of being raped in some way, wouldn't leave me."
    th "And who was stopping me from doing it right, I ask you?"
    $ meet('uv','Girl')
    uv "And do you know how to… right?"
    me "What?"
    show uv smile at left with dissolve
    "When I began to realize reality again, it turned out that I was not alone."
    show cg d7_trio_7dl with dspr
    pause(.2)
    hide cg d7_trio_7dl
    "Walking fanservice was seeking my company."
    "Slender legs, nice figure..."
    "And a tail and ears, of course."
    me "I guess I do. Would you like one?"
    "I handed her a pack of cigarettes, but she shook her head."
    "She sat down next to me, her tail around my ankles."
    "With her tail twitching finely - it was especially noticeable in the local scattered light."
    "She fell silent, studying me."
    "Mentally she pulled on her short dress."
    "It didn't really cover anything, but it didn't embarrass the girl at all."
    "She smiled at me in a friendly way, like an old acquaintance."
    uv "Does it hurt?"
    "She touched the abrasion with her finger, immediately yanked it away."
    me "Not here."
    show uv normal with dissolve
    "I must confess, I had already forgotten about this trifle."
    uv "Where then?"
    "I pointed to my chest."
    "As if it could be explained in words - a steely thorn in my chest, a bleeding regret."
    show un sorrow modern tr1 with dspr
    pause(.12)
    hide un
    show uv guilty with dspr
    uv "So you don't know how to do it right either?"
    me "And who can? Who are you anyway? Why am I being frank with you?"
    show uv surprise with dspr
    uv "Me?"
    me "You."
    "I answered with a frown."
    uv "I don't know. I'm always here. Or not here?"
    show uv grin with dspr
    uv "But I know you're definitely not supposed to be here."
    me "Where is it, here?"
    show uv normal with dspr
    uv "On this road."
    me "And who determines norms and measures?"
    "Slowly enraging, I began."
    me "Why can't you just let me be happy?"
    "And the girl pressed her ears to her head and answered guiltily:"
    uv "I don't know. But it seems to me that you're forbidding yourself."
    "She lowered her head penitently."
    "Yes, and I've gone down, too. On some level I realized she was right."
    "Whispered:"
    me "There's no more Lena?"
    "The girl sighed:"
    uv "There is."
    show uv guilty with dspr
    uv "She sometimes forgets you just to survive."
    uv "Sometimes she remembers - just to feel alive."
    uv "You're out of luck this time."
    me "This time? {w}Like I'll have any more times!"
    uv "Would you like to?"
    me "Stop mocking me."
    show uv upset with dspr
    uv "I'm serious! Do you want to try again?"
    me "How is that possible? Who can turn back time? Is it you?"
    me "I don't see you with a halo or a time machine."
    show uv normal with dspr
    uv "You don't need them here."
    uv "Just a warning: no one knows how it's going to turn out this time."
    uv "Not me, not you."
    "How am I supposed to believe that? That's bullshit!"
    "Bullshit."
    "Really?"
    "And I, like diving into cold water, blurted out:"
    me "Can't you do it in a human way? To remember and... So she doesn't..."
    uv "You don't bargain with the last chance, Semyon."
    uv "You either agree... Or you don't."
    "And then I asked the question head-on:"
    me "Do you have a problem with Lenka?"
    show uv laugh with dspr
    uv "Have mercy on the Creator!"
    "This impossible girl laughed."
    "She whipped her tail at her feet and stood up."
    show uv normal with dspr
    uv "I've only met her twice. {w}Do you know where?"
    "I shook my head."
    uv "You knooooow."
    "She purred."
    me "Where from?!"
    uv "Here. On the pier, the October wind was blowing, and she was wearing this coat, you know..."
    th "Where from?!"
    uv "And such wonderful boots - gray, nubuck."
    uv "It's a pity they were spoiled by St. Petersburg's municipal workers with their reagents."
    uv "They sprinkled to melt the snow, but it turned out to melt the shoes."
    me "Ahem... And the second time?"
    "Barely got it out of my mouth."
    show uv normal with dspr
    uv "The second time it was somewhere in the southwest."
    uv "She missed the streetcar again, and ran so funny after it."
    uv "Teenagers cheered her on from the back yard, flattened their noses against the windows and called her an athlete."
    uv "She was running."
    uv "Thought of a boy who was happy now because it was fall, his favorite city, and music on his headphones."
    uv "That he is panting somewhere behind about thirty meters away, but is about to catch up, wrap his arms around her and twirl her around, kissing her."
    uv "Turns around - and he's not there."
    "The girl is silent."
    me "Who the hell are you?"
    "I asked tiredly."
    "The strength to wonder about retelling something I wouldn't have even trusted Lena if she hadn't drawn it herself was gone."
    "There was only the desire to sit there, smoking a cigarette."
    "And a tiny hope for a miracle."
    uv "I told you. I don't know."
    uv "But it doesn't matter."
    uv "Far more important is the other thing."
    "The girl has caught my thoughts again."
    uv "She's alive, Semyon."
    scene cg d7_bus_night_7dl with dissolve
    uv "You didn't ask, but... how about a chance?"
    uv "Just because. To try to make it right?"
    "A bus pulled out from behind the hills, bouncing on the potholes, dabbed a sheaf of headlights at the stop, began to approach thoughtfully."
    "On its windshield I saw a license plate I wasn't even surprised to see."
    uv "Do you want to - let's go home?"
    uv "Only it's cold at home."
    if loki:
        uv "And painful."
    elif herc:
        uv "And dirty."
    else:
        uv "And wet."
    uv "Make your choice."
    play sound sfx_intro_bus_door_open
    pause(3)
    scene anim intro_11
    with fade
    uv "The bus won't wait."
    "Before me, with a familiar hiss, the shutters swung open..."
    scene black
    with fade
    stop music fadeout 3
    stop ambience fadeout 3
    play sound sfx_7dl["aunl"]
    stop sound_loop fadeout 3
    pause(7.4)
    with vpunch
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    "Okay, okay..."
    "Believe it?"
    scene bg ext_railbridge_sunset_7dl with dissolve
    play music music_7dl["sad_piano"] fadein 3
    $ set_mode_nvl()
    "Okay, there was actually a whole bunch more."
    "There was sunshine and summer and happy laughter."
    "Except it was a whole other story."
    if loki:
        "Yeah, nobody beat me up."
        "Honestly, honestly."
        "Don't you dare believe it when they say they once found a frostbitten half-dead man in a state of painful shock on the paths of the Central Park of Culture and Recreation."
        "They say he kept saying two names and then he died without regaining consciousness."
        "Well, I'm telling you, it's a load of crap!"
        "In fact, I didn't even get on that bus taking me straight to fairyland."
        nvl clear
        "When I hung up after talking to Ksyusha, I thought for a long, long time, and then I blacklisted her."
        "I wondered to myself, but yes!"
        "It was as if having new powers now, I was rooting out everything that had connected me with my previous life."
        "Now a different name sounded in my heart."
        "Which meant that life was much brighter and clearer."
    elif herc:
        "And nobody shot me."
        "What nonsense!"
        "Don't you dare believe it if somebody tells you that Semyon Sychev was shot with a traumatic weapon in the line of duty."
        "In fact, I didn't even go to work at the time."
        "My back hurt, so I called work and said I wasn't going out."
        "And while I was lying there thinking, I suddenly realized I wasn't going back there."
        nvl clear
        "Those must have been signals from my pessimistic subconscious, calculating all the options in the world and choosing the worst one?"
        "Or did I suddenly realize that I was starting to get dumb at such a job?"
        "Either way..."
        "Once stopped life went back to the way it was."
        "It cost me a lot of effort just to go to the unemployment office to close an old, high school debt."
        "Career guidance."
        "And guess what I became?"
    else:
        "And I didn't drown on the bus."
        "I'm telling you straight up, that's bullshit."
        "Drowning on a bus... You might as well say 'flying on a boat'."
        "I was too lazy to go to the bus stop and instead used a simple TeamViewer to get to the bottom of what happened."
        "The thing is, I completely forgot about my sociophobia."
        nvl clear
        "But I remembered perfectly the colorful dream of a week long."
        "Name."
        "Eye color."
        "I dread to think how many rejected and wasted poems I wrote and dedicated to a girl who didn't exist."
    "So all was well with me."
    scene bg ext_city_night_7dl
    nvl clear
    "I wish I could say no one died."
    "But unfortunately..."
    nvl clear
    "I can't lie in the story of my own life, otherwise it will become another unnecessary fiction."
    "I woke up, and Lena wasn't there."
    "She wasn't."
    "And I would have put up with it, but one day I found something else in my mailbox besides bills."
    "A gray, crumpled envelope with corners weathered by age and dampness."
    "A letter from the past?"
    "A picture. One and only one."
    scene bg int_staircase_7dl
    nvl clear
    "Not very good quality, obviously printed from film."
    "It had a close-up of a tombstone."
    "With the name that gave me life."
    "It made me want to scream out in pain, out of a sense of the wrongness of what was happening."
    "But who was it ever going to help?"
    nvl clear
    "I went out to the store, bought some forty-degree crap and drank in the kitchen for a long time, trying to believe what had happened."
    "I cried and walked from corner to corner, pulled out my old smartphone and stared disbelievingly into the captured eyes."
    "Unsmiling, stern - as if she knew by then that nothing was going to work out."
    "And I wanted so badly..."
    nvl clear
    "I drank and didn't get drunk, just got darker and darker."
    "Just like that, to see the world crumble overnight - I wasn't ready for that at all."
    "I wasn't ready to live in a world that her eyes couldn't see."
    "And never to hear her laugh again..."
    stop music fadeout 6
    "The last thing I remember before I passed out was the chill from the wide-open window and the wail, drilling into the low sky:"
    me "Leeeeeeeeeenaaaaaa!"
    with vpunch
    nvl clear
    scene bg int_sam_room_7dl
    play music music_7dl["feel_you_inside"] fadein 3
    "I woke up this morning completely empty and sterile."
    "No, outwardly it was all right - I went to work, sometimes I even smiled."
    "And I was very afraid of the night, because that's when loneliness came."
    "And I was scared shitless of loneliness."
    "Now that there was no one to come and rescue me like in superhero movies."
    "A dark, scary night."
    "I screamed into my pillow like a little baby and wished to all the possible gods that none of this would happen."
    "That only she would come!"
    "Or at least I could get to where she is."
    nvl clear
    "And one day that's what happened."
    "Really!"
    "When the stock of vivacity and life from camp began to run out little by little, and I was back in a state of manic depression, what happened happened."
    "I had gaunted a lot in those six months, so it didn't take much absinthe anymore to pass out."
    "The lock clicked in the hallway."
    "And Lena, my Lena, was on the doorstep."
    "Wearing the same clothes I remembered her wearing."
    "And obviously not very happy."
    nvl clear
    scene bg int_sam_house_clean_7dl
    show un angry modern at zenterleft
    with dissolve
    $ set_mode_adv()
    un "Well, the hell are you doing, tell me? Why do you keep calling me?"
    me "Lena?!"
    "I was dumbfounded by the mad happiness and fear that this was all just a dream to me."
    un "And who were you expecting to see? General Secretary Ikari?"
    show un normal modern with dspr
    un "You can touch if you're afraid of ghosts."
    "I got up and walked over to her and held out my hand unbeknownst to her."
    me "Lena."
    "Her cheek was alive and warm. And her teeth clicked dangerously close to my fingers."
    un "Lena, Lena."
    show un sorrow modern with dspr
    un "You're so helpless, huh? Get on with your life and leave me alone!"
    "«But you died», — I wanted to say, but instead I said:"
    me "But I don't want to… leave you alone."
    show un smile modern with dspr
    un "So what? Died and died, whatever."
    un "Not the biggest drawback, you know."
    me "I'm dreaming of you, right?"
    show un smile2 modern with dspr
    un "Fool, oh, what a fool."
    "Said she, sitting down next to me on the couch."
    un "How can someone like you say such stupid things?"
    un "It's obvious."
    show un smile modern
    with fade
    un "Death is just the beginning!"
    un "And anyway, I want to eat and lie down and be in your arms."
    "And here I unreservedly believed."
    "I decided this: let the dream be. To hell with it."
    "I took Lena in my arms and carried her to the kitchen, where a couple of patties and spaghetti were waiting in a skillet under a lid."
    "Not God knows what, of course, but I'm afraid I can't take another pizza."
    "We ate and talked about everything until dawn, and in the very morning, which was no different from the night before, a thick glass bottle with bright green contents flew out the window."
    "And we met the dawn together."
    "She was warm, she was mine."
    "And she smelled the way I remembered her."
    me "Will you stay?"
    "I suggested."
    show un shy modern with dspr
    un "Finally. I thought you'd never suggest it."
    me "I am."
    "I smiled."
    "I no longer cared where she came from or how she found me."
    "I didn't give a damn about that."
    hide un with dissolve
    "So we went back to the couch together."
    "Lena was alive, real, still the same fragile girl."
    "I suddenly realized I didn't want to die for her. I want to live for her."
    "So..."
    "As we, weary of the sweet reunion, lay looking up into the slowly gaining light, I asked:"
    scene cg d5_un_bed_7dl with dissolve
    me "Lenka, honestly - why did you decide to do to yourself..."
    "She, lying on my shoulder, shook her head."
    un "Let's not, okay?"
    un "I had my reasons. And they were very unpleasant."
    me "And that's okay. The important thing is that we're together again."
    un "For good."
    "My eyes are stinging with impossible, immense happiness."
    un "Just keep in mind that I can't be with you all the time. Do you understand?"
    un "I'm dead, remember?"
    "She looked me in the eye."
    un "Believe me, it's not because I don't want to be with you."
    me "But this is nonsense."
    un "Nonsense."
    "She nodded."
    un "But your time is the future...{w} And mine..."
    me "What?"
    "I really didn't like the way that sounded."
    un "And I'll stay that way forever now."
    "She smiled quietly."
    un "Change is the prerogative of the living."
    me "Me too, then, neither will I!"
    "Lena hugged me as hard as she could, and I felt her trembling."
    un "Stop it."
    me "Why?"
    un "You can't not change. You have to, do you hear?"
    un "I don't owe anybody anything."
    un "You owe at least to me, Semyon. You've got to stop spitting on yourself, you've got to pull through and survive."
    me "Don't I live?"
    "Lena shook her head:"
    un "Now you're dying of cold in a freezing cold room, so come on, sweet Semyon."
    un "Come on."
    un "Come to your senses."
    scene
    $ renpy.show("bg int_sam_room_7dl", what = Desat1("bg int_sam_room_7dl"))
    with dissolve
    "And I came to myself, shivering with cold."
    "The window was really wide open, with snow drifting into the room, and my head was cracking and aching."
    "I got up, closed the window, closed the whole episode of my life."
    $ set_mode_nvl()
    "Got on with my life."
    "I'd pretend to go to bed, but really open the door and wait until midnight."
    "And sometimes the door would open and Lena would show up on the doorstep."
    "She would come, and in the morning I would wake up sick and broken again."
    "But full of lust for life."
    "Thirsty to live to see her again!"
    "That's what gave me strength."
    "Meaning, if you like."
    "We stayed the same, which meant there was a tiny, exciting mystery in every encounter."
    "The excitement of a youth that got to the sweet stuff."
    "And we chatted in the kitchen, the two of us cooking something very delicious, sometimes watching a movie, sometimes going out for a walk in the city at night."
    "Loved each other."
    nvl clear
    "Can't say I like it."
    "I can't get enough of the good stuff, I want the best."
    "That's why these rare meetings - like Japanese love: cold, aloof and once a month - depressed me."
    "Lena noticed my condition, but she couldn't help me."
    "Until one day I threw a tantrum, not wanting to go to sleep or break up with her."
    "It was, I think, the fourth time I'd met her, just celebrating the anniversary of my return from camp."
    "And all the day that I had been pacing the granite-lined, windswept embankments, I had fought with longing, perfectly aware of the nature of both Lena and our relationship."
    $ set_mode_adv()
    play music music_7dl["youre_not_real"] fadein 3
    "I was afraid to admit it to myself."
    "But the sick, inquiring mind touched and touched this place, like a tongue licks the pit of a tooth that has been extracted."
    "That's why it was so vile and disgusting."
    "Lena came that same evening."
    "She listened to me wailing for a long time, not daring to say a word."
    "Then she sighed deeply:"
    show un normal modern with dspr
    un "And why aren't you living your own life?"
    me "Because you're not in it. And seeing you in my dreams is even worse."
    show un sorrow modern with dspr
    un "You were given a second chance, and you spit in the creator's face."
    un "Why are you such an impossible man, Semyon?"
    "I shrugged it off."
    me "I want a fairy tale, you know?"
    show bg ext_entrance_night_clear_7dl
    pause(.15)
    hide bg ext_entrance_night_clear_7dl
    un "I know."
    "Lena got up."
    un "I know…"
    "And offered me her hand."
    scene cg d7_un_epilogue_bad2_7dl
    show spill_red
    show alt_credits "Will you go with me?" with dissolve2:
        pos (747,115)
    with flash
    with dissolve
    pause(6)
    stop sound_loop fadeout 0
    scene anim prolog_2 with fade3
    "\[True-Transit ending unlocked - «Will you go with me?»\]"
    play sound sfx_7dl["aunl"]
    stop sound_loop fadeout 3
    $ sdl_persistent_inc("un_7dl_true_tran")
    show acm_logo_un_7dl_true_tran with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    pause(1)
    return

label alt_day7_un_7dl_rej:
    scene black with fade
    play music music_7dl["youre_not_real"]
    "The whole thing smelled bad from the beginning."
    "Me, somehow falling in love at first sight."
    "And my memory, which now and then threw me pictures that had nothing to do with my life experience."
    "Lena, in her own words, is a dishonest and unprincipled bitch."
    "Or is she?"
    scene bg int_sam_house_clean_7dl with dissolve
    "And outside is spring, deciding it's summer."
    "And the sun cuts in half frost and ice - in my eyes, in my hearts."
    "The cigarette ran out and I crushed it in the ashtray, walked to the window and pressed my forehead against the cold glass."
    scene bg int_semen_room_window_day_7dl with dissolve
    "My March, mine - and not a word from a magic dream, nothing."
    "We can see out of the corner of our eye a face in a crowd, or create an image by synthesizing it from several images. And then see it in a dream."
    "So should I consider Lena a synthesized image?"
    "Or have I really met her once - but completely forgotten?"
    "Or had I forgotten that even when I had met her, my body and soul belonged to someone else?"
    me "Ticket to Novokuznetsk, please."
    "And the first rain outside, everything is like Yurochka Shevchuk's, everything is like his."
    "Although until May there's..."
    voice "With a layover in Moscow, departing today at seventeen o'clock from the Moscow station, will that be all right?"
    me "That's fine."
    voice "Booking."
    "The woman hung up and passed out."
    "And I held the phone stupidly to my ear for a few more seconds."
    "I'm getting old, I'm getting old - my reactions aren't the same, it's harder and harder to remember new information..."
    "Even what I'm in such a hurry to get to Kuznya has to be repeated several times a day so I don't forget."
    "So I don't have to dial the number of the agent who handled my settlement and yell at him - for managing to do the impossible for the huge federal search machine."
    "He found my father. A man I thought was either an astronaut or a scout in the enemy's camp."
    "A traitor who abandoned me when I needed him most."
    $ renpy.show("cg d5_rainy_idle_7dl", what = Desat("cg d5_rainy_idle_7dl"))
    with dissolve
    "Through an agent, however, I successfully sold my old apartment and moved into a new one."
    "The buyer and I met only once - and it was a shapeless pile of scarves and hats that I didn't look closely at."
    "She's clearly not the kind of person who's now throwing off her hoods and laughing into the low St. Petersburg sky, welcoming a new life."
    "It's raining outside."
    "She is now the rightful owner of the place that never managed to become my home."
    scene bg int_excalator_7dl with fade
    "And that's great: out of sight, out of mind."
    play ambience ambience_7dl["railroad"] fadein 3
    show un sorrow modern tr1 at left
    show mt2 sad sport tr1 at right
    with dissolve
    "Except that all the way to the subway I was tormented by images of two beautiful green-eyed girls."
    pause(1)
    scene bg int_excalator_7dl
    with dissolve
    "And in no way could I choose one of them, as the memory suddenly woke up and told me everything."
    "And so with all this {i}everything{/i}, I ride the escalator down, mindlessly gazing into the faces of those passing by."
    "I have too much to fix, too many to apologize for: I don't even know where to start."
    "That's why I was no longer surprised when a familiar girl with a mop of brown hair drove past me downstairs."
    me "{i}Olga!{/i}"
    "{i}I shouted.{/i}"
    "{i}And tried to catch up with her, ran up the moving escalator.{/i}"
    "{i}Shouting and shouting her name.{/i}"
    "{i}In vain.{/i}"
    "{i}At some point the passengers became too many, and she never heard me, shutting her ears with the music, killing attention to those around her to a dim glow in the green ice-green pupils.{/i}"
    "It suddenly made me very sad that she would go away like that."
    "Still won't understand what I understood as I ran to the station."
    "But that's her personal choice. Hers."
    scene anim prolog_2 with fade
    "I went down."
    "{i}Forgetting the shame and the danger of getting sick with complications, people met the thunder in the rain like a salute - the first thunder of spring…{/i}"
    "I was on my way to meet my debts and my personal future."
    "In which there is no place for the one who laid down her life on the scaffold."
    "Nor one who loved so much that she was willing to do anything."
    "And I didn't deserve it."
    "What's worse, I didn't want it."
    scene anim prolog_2 with fade3
    "\[Reject ending unlocked - «Once, It Was Quiet Here»\]"

    with dissolve
    play sound sfx_7dl["aunl"]
    stop sound_loop fadeout 3
    $ sdl_persistent_inc("un_7dl_rej")
    show acm_logo_un_7dl_rej with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    pause(1)
    return

label alt_day7_un_7dl_shard:
    scene bg int_un_stud_7dl with dissolve
    $ prolog_time()
    $ set_mode_nvl()
    play music music_7dl["tears_of"] fadein 2
    "When the city falls asleep, I open the creaking windowpane wide open, light a large floor lamp, and remove the dim canvas from the easel."
    "And then I stand in the middle of the room until dawn, staring at the faded sketch, hoping that I can see in the chaotic lines the city that has plagued me for nine years."
    nvl clear
    scene intro_2
    show prologue_dream
    with fade
    "A city that no road leads to."
    "A city that is not on any map or in any guidebook."
    "The city where no one can buy a ticket."
    scene intro_6
    show prologue_dream
    with dissolve
    nvl clear
    "The city in which He lives."
    scene bg int_un_stud_7dl with fade3
    $ set_mode_adv()
    "My back stiffens from my immobile posture, and I turn off the lamp with a sigh."
    "I draw the curtains, hiding from the first rays of the morning sun, climb into bed without undressing, and close my eyes."
    show blink
    th "This girl was so lazy that they even called her that - Lena."
    "If it were up to me, I would never wake up."
    "For in my dreams I see this city so clearly, as if I had spent my whole life there."
    "And sometimes I see it, too. And every morning after such dreams my pillow is wet with tears."
    play sound sfx_hell_alarm_clock
    show unblink
    hide blink
    "The alarm clock rattled so that I jumped up."
    "My head was like in a fog: I hadn't slept an hour."
    th "Why did I even set it..."
    th "Exhibition! Today is the opening of my exhibition!"
    "As I pulled myself out of the blanket, I panicked and scrambled out of bed and ran around the room."
    "I caught a glimpse of myself in the mirror and gasped: what a monster!"
    "I was looking at a nervous and shaggy woman with two huge bags under her eyes."
    "There was nothing in common between her and the sixteen-year-old girl I still felt I was."
    "I didn't know who this woman was or why she got up in the morning in the first place."
    "Shaking my head, I began to throw off my clothes."
    "I had my whole life to sigh over my bitter fate, and the exhibition was only two hours away."
    stop music fadeout 3
    $ alt_pause(1.5)
    scene bg int_un_exhibition_7dl with dissolve2
    play music music_7dl["breath_again"] fadein 3
    $ meet('am','Voice')
    $ meet('voice','Old lady')
    $ persistent.sprite_time = "day"
    "The organizer of the exhibit, whose clumsy name I couldn't keep in my head, clucked his tongue at my tardiness, but smiled welcomingly nonetheless and held out his hand to lead me to the first guests."
    th "This is not my life. Not my paintings. This is just a dream."
    th "And the real life... It's on that canvas that I still can't finish."
    "I nodded confusedly at all the compliments and looked at my own work with a hint of curiosity."
    "Nothing in my chest rose when I cast a glance at them."
    th "There's nothing about it. It's hollow, a fiction."
    th "An exercise for a hand that misses the hard wood of the brush."
    th "And all these onlookers go about examining the soiled canvases with an important look, as if they really see some meaning in them!"
    "I suddenly found myself laughing outrageously."
    "After all, I only painted it all to stifle my desire to paint a city that didn't exist."
    "The only painting that was worthy of hanging here stubbornly refused to come out from under my brush."
    "Just at some point I realized that I would start going crazy if I kept looking at my lifeless sketches."
    "And then they began to be born, the fruits of my helplessness. Paintings without a soul."
    "But the visitors didn't care about the soul."
    "All they needed was a beautiful gallery, quiet music and bubbles of champagne for the exhibition to be considered a social event worthy of their cultural level."
    stop music fadeout 2
    am "Grandma, what's that strange horse?"
    "For a split second the world stopped."
    "The music fell silent, the voices fell silent, the footsteps fell silent, and even the bubbles in the champagne stopped popping to the surface."
    th "So that's what it means to fall asleep on the move..."
    play music music_7dl["unforgotten"] fadein 2
    voice "It's a centaur, Senya. A mythical creature, half man, half horse."
    am "Like the Egyptian gods?"
    "I turned as slowly as if Medusa Gorgon were standing behind me."
    $ meet('am','Semyon')
    show ars laugh casual at center
    show bba smile at cright
    with dissolve
    am "Look how beautiful the mermaid is! She looks like auntie Miku!"
    "My heart stopped."
    "That's the face I've seen in front of me every time I've closed my eyes for nine years now."
    "Just the way I remembered it that damned summer."
    th "I must have been out of my mind. This can't be!"
    th "He couldn't have..."
    "And Semyon finally turned to me."
    "An electric shock went through my body."
    "And in that second I wanted to fall to the floor and burst into tears, forgetting about all those snobs sipping champagne. To fall down and never get up again."
    "There was a child looking at me."
    "With the face of a seventeen-year-old boy, tall, broad in the shoulders, but with an infinitely naïve childlike gaze and an enthusiastic smile."
    "Hasn't changed a bit since the last time we met."
    "And that could only mean one thing."
    show ars smile casual
    show bba normal
    with dspr
    voice "You are Elena, right?"
    "I nodded, not even hearing the question."
    "A gaunt, intelligent old woman in her eighties was looking at me sternly, and Semyon...{w} or rather, who used to be him, was trying ridiculously to hide behind her, throwing curiosity-filled glances at me."
    am "Did You draw all this?"
    "Instead of words, a muffled squeak escaped my throat."
    show ars laugh casual with dspr
    am "Very beautiful!"
    voice "Your technique is amazing, Elena."
    show ars smile2 casual with dspr
    "The old lady said dryly, squeezing her grandson's hand."
    voice "I hope you have a great future ahead of you. Don't squander your potential, there's not enough room in the sun for everyone."
    show ars sorrow casual with dspr
    am "Grandma, I'm hungry."
    "The “boy” said mournfully."
    show bba sad with dspr
    "The old lady sighed."
    voice "Sorry, kids his age get tired quickly. Let's go, Senya."
    show ars smile2 casual
    show bba smile
    with dspr
    voice "Have a nice day!"
    show ars laugh casual with dspr
    am "Goodbye!"
    hide ars
    hide bba
    with dissolve
    "They left, and I'm still standing there, as if pinned down."
    $ meet('am','Me')
    $ meet('voice','Voice')
    th "So that's it?"
    th "They cured him?"
    "It couldn't be called a cure - except euthanasia. But the fact remained:"
    th "He's not coming back. He's never coming back!"
    "The world around me was rapidly falling to pieces."
    "People were walking around, looking at the pictures, talking, and I was hurtling into the abyss."
    "Or rather, I was finally at the bottom of it."
    stop music fadeout 3
    $ alt_pause(2)
    scene bg ext_city_night2_7dl with dissolve
    play music music_7dl["devastated"] fadein 3
    "That night I didn't light the lamp when the sun sank below the horizon."
    "I must have resembled a thief, prowling the streets with a huge canvas in my hands."
    "The passers-by, however, didn't care."
    show alt_credits "It's all over" with dspr:
        pos (245, 330)
    $ alt_pause(0.3)
    show alt_credits "It's all over" with dspr:
        pos (893, 690)
    $ alt_pause(0.3)
    show alt_credits "It's all over" with dspr:
        pos (245, 690)
    $ alt_pause(0.3)
    show alt_credits "It's all over" with dspr:
        pos (560, 690)
    $ alt_pause(0.1)
    show alt_credits "It's all over" with dspr:
        pos (560, 490)
    $ alt_pause(0.1)
    show alt_credits "It's all over":
        zoom 1.5
        xcenter 810
        ycenter 540
    with hpunch
    $ alt_pause(1.5)
    scene bg ext_winter_night_7dl with dissolve2
    play sound_loop sfx_forest_fireplace fadein 3
    $ alt_pause(2)
    scene cg d7_un_fire_7dl with dissolve2
    $ alt_pause(6)
    scene cg d7_un_fireyes_7dl with dissolve2
    $ alt_pause(6)
    scene cg d7_un_firebridge_7dl with dissolve2
    $ alt_pause(1.6)
    "«It's all over.»"
    "It was like this mantra was helping me not to lose my mind completely."
    "To finish what I left the house for in the first place."
    "Every artist who paints in oil always has a supply of gasoline."
    "But not every artist is willing to put it to work when it's time to burn bridges."
    "The wasteland was flooded with bright flames, and I watched with unseeing eyes as the strokes of hundreds of thousands of failed sketches went black."
    "This painting is not destined to see the light of day."
    "The city that doesn't exist will stay where it was meant to be, and I will go forward."
    "Because there is no going back."
    show cg d7_un_firebridge2_7dl with dissolve2
    $ alt_pause(1)
    show cg d7_un_firebridge3_7dl with dissolve2
    pause(4)
    scene anim prolog_2 with fade3
    "\[Memory Shard - «Burning Bridges»\]"
    pause(4)
    play sound sfx_7dl["aunl"]
    stop sound_loop fadeout 3
    $ sdl_persistent_inc("un_7dl_shard")
    show acm_logo_un_7dl_shard with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    pause(1)
    return
